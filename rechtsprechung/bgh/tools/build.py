"""One German federal-court case-law repo from Seán Fobbe's CC0 "Corpus der Entscheidungen" CSV (Zenodo), straight into
git fast-import.   python build.py <court> <csv>[,<csv>...] <out repo dir> --today YYYY-MM-DD --snapshot YYYY-MM-DD --record <zenodo id>
(The BGH is built from two CSVs: CE-BGH, 2000 on, and BGH-Strafsachen-20Jhd, the criminal senates 1950-1999.)

One commit per decision (Kind: court), dated the day decided (noon Berlin); then one Lexifina documentation commit with
README, REPRODUCE.md, corpus.json, decision-index.tsv, unresolved.csv and the judgment overlay
judgments/germany/bund/acts/<path>.jsonl: citations found in the text ("§ 823 Abs. 1 BGB", "§§ 280, 281 BGB",
"Art. 3 Abs. 1 GG", "§ 15 SGB V") linked to germany-law files, each row pinned to the article's own version on the day
decided (reconcile.fix_row). Deterministic for the same input."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import duckdb
import regex

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'nl-caselaw'))
from reconcile import fix_row, versions  # noqa: E402  (law_commit = the article's own version)

LAW_CORPUS = 'germany/bund/acts'
BERLIN = timezone(timedelta(hours=1))
COMMITTER = b'Lexifina <corpus@lexifina.com>'
EPOCH_NOON = 11 * 3600
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}$')
COURTS = {'bverfg': 'Bundesverfassungsgericht', 'bverwg': 'Bundesverwaltungsgericht', 'bfh': 'Bundesfinanzhof',
          'bag': 'Bundesarbeitsgericht', 'bpatg': 'Bundespatentgericht', 'bgh': 'Bundesgerichtshof'}
# Courts built with the later readings (Resolver joined_qualifiers, path_of --2 suffixes): from the BGH on.
JOINED_QUALIFIERS = {'bgh'}
DOCKET_EXAMPLE = {'bverfg': '1 BvR 123/20', 'bverwg': '2 C 12.19', 'bfh': 'IX R 12/19', 'bag': '5 AZR 123/19',
                  'bpatg': '35 W (pat) 12/19', 'bgh': 'VI ZR 123/20'}
# The Zenodo datasets a court's repo is built from (README, REPRODUCE, corpus.json).
DATASETS = {'bgh': 'the CC0 "Corpus der Entscheidungen des Bundesgerichtshofs" (CE-BGH, Zenodo record 15153244, decisions from 2000) '
                   'and "Entscheidungen des Bundesgerichtshofs in Strafsachen aus dem 20. Jahrhundert" (BGH-Strafsachen-20Jhd, '
                   'Zenodo record 4540377, CC0, the criminal senates 1950-1999), both by Seán Fobbe'}
NOT_SHOWN = {'bgh': (' Before 2000 only the criminal senates (1 to 5; nothing of the 6th, 1954-1956): no open corpus holds the '
                     "civil senates' older decisions. The texts of 1950-1999 were read from scans (OCR), so they contain "
                     'recognition errors. Decisions after the CE-BGH snapshot are added by the nightly runner from the '
                     "court's RSS feed of new decisions (bundesgerichtshof.de), so the months between the snapshot and the "
                     "runner's first day are a gap until a newer CE-BGH version fills it.")}
ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIV': 14}
SIGN = re.compile(r'§§?|\bArt(?:ikel|\.)|\bArtt\.')
QUAL = r'(?:Abs\.|Absatz|Satz|S\.|Nr\.|Nrn\.|Buchst\.|lit\.|Alt\.|Halbsatz|Halbs\.|Hs\.|Var\.|Unterabs\.|UAbs\.)'
# The body between the sign and the abbreviation: numbers, qualifiers and joiners only (bounded: at most 120 chars).
BODY = regex.compile(r'\s*((?:\d+\s?[a-z]?\b|' + QUAL + r'|und|bis|sowie|oder|,|;|–|-|\s)+?)\s*'
                     r'(SGB\s+[IVX]+|[A-ZÄÖÜ][A-Za-zÄÖÜäöüß]*[A-ZÄÖÜ][A-Za-zÄÖÜäöüß0-9]*(?:\s(?:19|20)\d\d)?|GG)\b')
NUM = re.compile(r'(' + QUAL + r')?\s*(\d+)\s?([a-z]?)\b')


def akey(s: str) -> str:
    s = re.sub(r'\bSGB\s+([IVX]+)\b', lambda m: f'SGB{ROMAN.get(m.group(1), m.group(1))}', s.strip())
    return re.sub(r'[\s.\-]', '', s).lower()


def slug(s: str) -> str:
    return re.sub(r'-{2,}', '-', re.sub(r'[^A-Za-z0-9._-]+', '-', s)).strip('-.')[:120] or 'x'


def email_local(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60] or 'decision'


class Resolver:
    def __init__(self, idx, joined_qualifiers: bool = False):
        self.aliases, self.arts = idx['aliases'], idx['arts']
        self.timeouts = 0
        self.miss = {}  # abbreviation that names no germany-law act -> times cited (unresolved.csv)
        # "§ 535 Abs. 1 Satz 1 und 2 BGB": the 2 is a Satz, not § 2. Read so from the BGH on; the five courts built
        # before keep the first reading, so that their nightly re-renders do not turn into corrections.
        self.joined = joined_qualifiers

    def numbers(self, body: str) -> list[str]:
        """The § numbers of a citation's body: not those after Abs./Satz/Nr. (nor, with joined_qualifiers, those joined
        to such a number by "und", "oder", "sowie" or "bis")."""
        if not self.joined:
            return [f'{int(n)}{suf}' for q, n, suf in NUM.findall(body) if not q]
        out, qual, prev_q, joined = [], False, False, False
        for t in re.finditer(QUAL + r'|(\d+)\s?([a-z]?)\b|\b(?:und|oder|sowie|bis)\b|[,;]', body):
            tok = t.group(0)
            if t.group(1):
                is_q = qual or (joined and prev_q)
                if not is_q:
                    out.append(f'{int(t.group(1))}{t.group(2)}')
                prev_q, qual, joined = is_q, False, False
            elif tok in (',', ';'):
                qual = joined = False
            elif tok in ('und', 'oder', 'sowie', 'bis'):
                joined = True
            else:
                qual = True
        return out

    def from_text(self, text: str) -> list[tuple[str, str]]:
        out = []
        for s in SIGN.finditer(text or ''):
            win = text[s.end():s.end() + 160]
            try:
                m = BODY.match(win, timeout=0.05)
            except TimeoutError:
                self.timeouts += 1
                continue
            if not m:
                continue
            folder = self.aliases.get(akey(m.group(2))) or (self.aliases.get(akey(m.group(2).rsplit(' ', 1)[0])) if ' ' in m.group(2) else None)
            if not folder:
                k = re.sub(r'\s+', ' ', m.group(2))
                self.miss[k] = self.miss.get(k, 0) + 1
                continue
            files = self.arts.get(folder, {})
            how = re.sub(r'\s+', ' ', text[s.start():s.end() + m.end()]).strip()[:160]
            for num in self.numbers(m.group(1)):
                p = files.get(num)
                if p:
                    out.append((p, how))
        return out


def rows_of(court: str, csv: str) -> list[dict]:
    """The decisions of one or more CSVs (comma-separated paths), as dicts; "NA" read as missing."""
    if ',' in csv:
        return [r for one in csv.split(',') if one.strip() for r in rows_of(court, one.strip())]
    con = duckdb.connect()
    con.execute("SET memory_limit='24GB'")
    src = f"read_csv_auto('{Path(csv).as_posix()}', sample_size=-1, max_line_size=50000000, all_varchar=true)"
    cols = {r[0] for r in con.execute(f'describe select * from {src}').fetchall()}
    g = lambda c: c if c in cols else 'NULL'
    if court == 'bag':
        q = (f"select doc_id, text, Datum as datum, SpruchkoerperAZ || ' ' || Registerzeichen || ' ' || Ordinalzahl || '/' || "
             f"right('0' || Eingangsjahr, 2) || coalesce(nullif(ZusatzAZ, 'NA'), '') as aktenzeichen, NULL as ecli, NULL as url, NULL as typ, NULL as leitsatz, "
             f"NULL as titel from {src}")
    elif court == 'bgh':
        # CE-BGH's "leitsatz" is a flag ("LE"), not the text: the Leitsatz stays in the decision's text; its "name" is the
        # decision's popular name ("Trabrennbahn"). BGH-Strafsachen-20Jhd has no ECLI, URL or type.
        q = (f"select doc_id, text, datum, aktenzeichen, {g('ecli')} as ecli, {g('url')} as url, {g('entscheidung_typ')} as typ, "
             f"NULL as leitsatz, {g('name')} as titel, {g('spruchkoerper_db')} as spruchkoerper, NULL as bverfge, "
             f"NULL as zitiervorschlag, {g('bemerkung')} as bemerkung from {src}")
    else:
        url = 'url_html' if 'url_html' in cols else g('url')
        leit = 'leitsatz' if 'leitsatz' in cols else g('text_leitsatz')
        q = (f"select doc_id, text, datum, aktenzeichen, {g('ecli')} as ecli, {url} as url, {g('entscheidung_typ')} as typ, "
             f"{leit} as leitsatz, {g('titel') if 'titel' in cols else g('name')} as titel, {g('spruchkoerper_az')} as spruchkoerper, "
             f"{g('bverfge')} as bverfge, {g('zitiervorschlag')} as zitiervorschlag from {src}")
    cur = con.execute(q)
    names = [d[0] for d in cur.description]
    # The corpora write a missing value as the string "NA" (R's convention): read it as missing, everywhere.
    return [{k: (None if isinstance(v, str) and v.strip() in ('NA', '') else v) for k, v in zip(names, r)} for r in cur.fetchall()]


def path_of(r: dict, court: str, used: set) -> str:
    """decisions/<court>/<yyyy>/<ECLI, or Aktenzeichen and day>.md; where two share a name, the later one gets a doc_id
    suffix (the five courts built first) or, from the BGH on, --2, --3: the doc_id's "NA" (missing) fields gave the BFH
    and BAG files names like NA--... and cut suffixes like --952-07-10_3_StR_302_52_a."""
    day, az = r['day'], (r.get('aktenzeichen') or r['doc_id']).strip()
    base = slug(r['ecli'].replace(':', '_')) if r.get('ecli') else slug(f'{az}-{day}')
    path = f'decisions/{court}/{day[:4]}/{base}.md'
    if path in used and court in JOINED_QUALIFIERS:
        n = 2
        while path in used:
            path, n = f'decisions/{court}/{day[:4]}/{base}--{n}.md', n + 1
    elif path in used:
        path = f"decisions/{court}/{day[:4]}/{base}--{slug(r['doc_id'])[-24:]}.md"
    used.add(path)
    return path


def render(r: dict, path: str, court: str, res: Resolver, ver: dict, extra: tuple = ()):
    """One decision as (file bytes, author, email, commit message bytes, [(law path, overlay row)], [index references]).
    Shared by the full build and the nightly appends; a Corrected: trailer in `extra` makes the commit Kind: correction."""
    name, day = COURTS[court], r['day']
    az = (r.get('aktenzeichen') or r['doc_id']).strip()
    cites = res.from_text(r['text'])
    refs = sorted(x for x in {az, r.get('ecli') or ''} if x)
    fm = {'ecli': r.get('ecli'), 'court': name, 'spruchkoerper': r.get('spruchkoerper'), 'aktenzeichen': az, 'decided': day,
          'typ': r.get('typ'), 'bverfge': r.get('bverfge'), 'zitiervorschlag': r.get('zitiervorschlag'),
          'bemerkung': r.get('bemerkung'), 'source_url': r.get('url'), 'corpus_doc_id': r['doc_id']}
    lines = ['---'] + [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fm.items() if v not in (None, '', 'NA')]
    uniq = sorted({p for p, _ in cites})
    if uniq:
        lines.append('cites_law: ' + json.dumps([f'{LAW_CORPUS}/{p}' for p in uniq], ensure_ascii=False))
    title = (r.get('titel') or '').strip()
    title = f'{name}, {az} vom {day}' + (f': {title}' if title and title != 'NA' else '')
    lines += ['---', '', f'# {title}', '']
    if r.get('leitsatz') and r['leitsatz'] not in ('NA', ''):
        lines += ['## Leitsatz', '', r['leitsatz'].strip(), '']
    lines += ['## Entscheidung', '', r['text'].strip(), '']
    body = '\n'.join(lines).replace('\r\n', '\n').encode('utf-8')
    author = f'{name} {az}'.replace('<', '').replace('>', '')[:200]
    email = f'{court}-{email_local(az)}@caselaw.invalid'
    kind = 'correction' if any(t.startswith('Corrected:') for t in extra) else 'court'
    tr = [f'Kind: {kind}', f'In-force: {day}', f'Decided: {day}', f'Court: {name}', f'Docket: {az}']
    if r.get('ecli'):
        tr.append(f"ECLI: {r['ecli']}")
    if r.get('url') and r['url'] != 'NA':
        tr.append(f"Source: {r['url']}")
    seen = set()
    for p, how in cites:
        if p not in seen and len(seen) < 60:
            seen.add(p)
            tr.append(f'Cites: {LAW_CORPUS}/{p} ({how[:120]})')
    tr += list(extra)
    what = (r.get('typ') or 'Entscheidung')
    msg = (f'{name} {az}: {what}'[:200] + '\n\n' + '\n'.join(tr) + '\n').encode('utf-8')
    counts = {}
    for p, _ in cites:
        counts[p] = counts.get(p, 0) + 1
    rows, done = [], set()
    for p, how in cites:
        if p in done:
            continue
        done.add(p)
        row = {'decided': day, 'name': f'{name} {az}', 'court': name, 'citation': r.get('ecli') or az,
               'url': r.get('url') or '', 'how': how, 'mentions': counts[p], 'decision': path}
        rows.append((p, fix_row(row, p, ver)))
    return body, author, email, msg, rows, refs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('court'), ap.add_argument('csv'), ap.add_argument('out')
    ap.add_argument('--today', required=True), ap.add_argument('--snapshot', required=True), ap.add_argument('--record', required=True)
    ap.add_argument('--law-repo', default=str(Path.home() / 'Documents' / 'caselaw-law-mirrors' / 'germany-law.git'))
    ap.add_argument('--chunk-bytes', type=int, default=2_500_000_000)
    ap.add_argument('--chunk-commits', type=int, default=40_000)  # pushed in steps of at most this many commits
    a = ap.parse_args()
    court, name = a.court, COURTS[a.court]
    out = Path(a.out)
    res = Resolver(json.load(open(HERE / 'de_index.json', encoding='utf-8')), joined_qualifiers=court in JOINED_QUALIFIERS)
    ver = versions(Path(a.law_repo), ref='main')
    recs = [r for r in rows_of(court, a.csv) if (r.get('text') or '').strip()]
    for r in recs:
        r['day'] = (r['datum'] or '')[:10]
    recs.sort(key=lambda r: (r['day'] or '9999', r.get('aktenzeichen') or '', r['doc_id']))
    print(f'{court}: {len(recs)} decisions', file=sys.stderr, flush=True)
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f'{out} is not empty')
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'init', '-q', '-b', 'main', str(out)], check=True)
    fi = subprocess.Popen(['git', '-C', str(out), 'fast-import', '--quiet', '--done', f'--export-marks={out / ".git" / "marks"}',
                          '--big-file-threshold=64m'], stdin=subprocess.PIPE)
    w = fi.stdin.write
    overlay, dindex, used, undated = {}, [], set(), []
    mark = raw = clamp = 0
    checkpoints, first = [], None
    for r in recs:
        day = r['day']
        if not ISO.match(day or ''):
            undated.append(r)
            continue
        first = first or day
        path = path_of(r, court, used)
        body, author, email, msg, rows, refs = render(r, path, court, res, ver)
        dindex += [ref + chr(9) + path for ref in refs]
        raw += len(body)
        d0 = date.fromisoformat(day)
        if d0.year < 1970:
            clamp += 1
            ts = EPOCH_NOON + clamp - 3600
        else:
            ts = int(datetime(d0.year, d0.month, d0.day, 12, tzinfo=BERLIN).timestamp())
        mark += 1
        w(b'commit refs/heads/main\nmark :%d\n' % mark)
        w(b'author %s <%s> %d +0100\ncommitter %s %d +0100\n' % (author.encode('utf-8'), email.encode(), ts, COMMITTER, ts))
        w(b'data %d\n%s\n' % (len(msg), msg))
        w(b'M 100644 inline %s\ndata %d\n%s\n' % (path.encode('utf-8'), len(body), body))
        if raw >= (len(checkpoints) + 1) * a.chunk_bytes or mark - (checkpoints[-1] if checkpoints else 0) >= a.chunk_commits:
            checkpoints.append(mark)
        for p, row in rows:
            overlay.setdefault(p, []).append(row)
    docs = {}
    for p, rows in overlay.items():
        rows.sort(key=lambda x: (x['decided'], x['citation']))
        docs[f'judgments/{LAW_CORPUS}/{p[:-3]}.jsonl'] = ''.join(json.dumps(x, ensure_ascii=False, sort_keys=True) + '\n' for x in rows)
    docs['decision-index.tsv'] = 'reference' + chr(9) + 'path' + chr(10) + ''.join(x + chr(10) for x in sorted(set(dindex)))
    unres = ['kind,reference,detail']
    for r in undated:  # no decision date in the corpus: no commit can be dated, so the decision is listed here instead
        unres.append(','.join(json.dumps(x or '', ensure_ascii=False) for x in ('undated decision', r.get('aktenzeichen'), r['doc_id'])))
    for k, n in sorted(res.miss.items(), key=lambda x: (-x[1], x[0])):  # cited abbreviations that name no germany-law act
        unres.append(','.join(json.dumps(x, ensure_ascii=False) for x in ('abbreviation not in germany-law', k, f'{n} citations')))
    docs['unresolved.csv'] = chr(10).join(unres) + chr(10)
    dataset = DATASETS.get(court, f'the CC0 "Corpus der Entscheidungen" CSV on Zenodo (record {a.record})')
    ex = DOCKET_EXAMPLE.get(court, '1 BvR 123/20')
    n_refs = sum(len(v) for v in overlay.values())
    in_rec = sum(1 for v in overlay.values() for x in v if 'law_commit' in x)
    gl_path = f'germany/{court}/caselaw'
    docs['corpus.json'] = json.dumps({
        'corpus': f'de/{court}/caselaw', 'path': gl_path, 'name': f'Case law: Germany, {name}', 'label': f'Germany case law ({name})',
        'language': 'de', 'kind': 'judgments', 'history': 'in-force',
        'coverage': f'{mark} published decisions of the {name}, one file and one commit each, dated the day decided; {n_refs} citations of federal law linked to germany-law ({in_rec} inside its record).',
        'history_from': first, 'record_to': a.snapshot, 'checked_on': a.today,
        'record_note': 'Court decisions, not laws: every commit is Kind: court. In-force is the day decided. The record ends at the corpus snapshot named in REPRODUCE.md.',
        'in_force_trailer': 'In-force', 'correction_trailer': 'Corrected',
        'dates': {'commit': 'decided', 'time': '12:00 Europe/Berlin'},
        'source': {'publisher': name, 'dataset': f'Corpus der Entscheidungen ({court.upper()}), Zenodo record {a.record}' if court not in DATASETS else dataset, 'updated': a.snapshot},
        'licence': 'CC0 1.0 (the decisions are official works, § 5 UrhG)',
        'overlay': {'path': f'judgments/{LAW_CORPUS}/<path>.jsonl', 'law_corpus': LAW_CORPUS},
    }, ensure_ascii=False, indent=2) + '\n'
    docs['README.md'] = f"""# German case law: {name}

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the case law of the {name}, Germany, which global-law reads at `{gl_path}/`.

Every published decision of the {name} in the corpus this is built from, as a git history: one file per decision, one
commit per decision, dated the day it was decided. {mark:,} decisions from {first} to {a.snapshot}.

## Questions as git commands

| Question | Command |
|---|---|
| A decision | `cat decisions/{court}/<year>/<ECLI or Aktenzeichen>.md` |
| By Aktenzeichen or ECLI | `git log --grep='^Docket: {ex}$' --stat` · `grep '{ex}' decision-index.tsv` |
| Decisions given in a window | `git log --since=2024-03-01 --until=2024-03-31 --format='%ad %an' --date=short` |
| Decisions citing § 823 BGB | `cat judgments/germany/bund/acts/bgb/0823.jsonl` |
| The provision as the court applied it | each overlay row's `law_commit` is the provision's own version in germany-law on the day decided; germany-law's record for acts other than the Grundgesetz starts 2019-06-10, so older decisions give `law_record_from` instead |
| Who wrote a line? | `git blame decisions/...`: each line is credited to the decision (court and Aktenzeichen) |

## Dates and authors
The commit date is the day the decision was given, at noon Berlin (`In-force:` and `Decided:`). The author is the court
and the Aktenzeichen, at an address that cannot exist. These are court rulings, not laws: every commit is `Kind: court`.

## The judgment overlay
Citations of federal law in the decision's text ("§ 823 Abs. 1 BGB", "Art. 3 Abs. 1 GG") are linked to the provision
files of lexifina/germany-law by the official abbreviations in its `verzeichnis.json`: {n_refs:,} links, {in_rec:,} of them
inside germany-law's record. Abbreviations two acts share are not linked.

## Source and licence
The decisions are official works of the {name} (§ 5 UrhG); each file links to the court's own page where the corpus gives
one. Built from {dataset} (snapshot {a.snapshot}). This
repository is dedicated to the public domain under CC0 1.0.

## What it does not show
Decisions the court did not publish, and decisions after {a.snapshot}.{NOT_SHOWN.get(court, '').format(undated=len(undated))}
Decisions the corpus gives no date for cannot be dated as a commit: they are listed in `unresolved.csv` ({len(undated):,}),
with the cited abbreviations that name no act in germany-law.
"""
    docs['REPRODUCE.md'] = f"""# Reproducing this repository

Input: {dataset}: the CSV "Datensatz" file(s) (snapshot {a.snapshot}); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py {court} <csv>[,<csv>] <empty folder> --today {a.today} --snapshot {a.snapshot} --record {a.record}
```

Gives {mark:,} decision commits and one documentation commit.
"""
    for f in ('build.py', 'de_index.py'):
        docs[f'tools/{f}'] = (HERE / f).read_text(encoding='utf-8')
    ts = int(datetime.fromisoformat(a.today + 'T12:00:00+01:00').timestamp())
    msg = f'Documentation: README, REPRODUCE, corpus.json, decision index and the judgment overlay ({n_refs} citations)\n'.encode()
    w(b'commit refs/heads/main\nauthor Lexifina <corpus@lexifina.com> %d +0100\ncommitter %s %d +0100\n' % (ts, COMMITTER, ts))
    w(b'data %d\n%s\n' % (len(msg), msg))
    for p in sorted(docs):
        b = docs[p].encode('utf-8')
        w(b'M 100644 inline %s\ndata %d\n%s\n' % (p.encode('utf-8'), len(b), b))
    w(b'done\n')
    fi.stdin.close()
    if fi.wait():
        raise SystemExit('fast-import failed')
    marks = dict(l.split() for l in (out / '.git' / 'marks').read_text().splitlines())
    (out / '.git' / 'push-checkpoints').write_text(''.join(marks[f':{m}'] + '\n' for m in checkpoints))
    print(json.dumps({'group': court, 'decisions': mark, 'undated': len(undated), 'overlay_rows': n_refs, 'in_record': in_rec,
                      'regex_timeouts': res.timeouts, 'raw_gb': round(raw / 1e9, 2), 'checkpoints': len(checkpoints)}), flush=True)


if __name__ == '__main__':
    main()
