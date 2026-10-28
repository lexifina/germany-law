"""Builds the Grundgesetz record from c3e/grundgesetz: the data behind lexifina.com/watch/grundgesetz and a public git
repository in which every amending law is one commit, dated the day it took effect.

    python -X utf8 scripts/grundgesetz/build.py --source ../gg-source [--site saas-webpage] [--repo ../grundgesetz]

The source is a clone of https://github.com/c3e/grundgesetz: one commit per version of the Basic Law since 1949, with
meta.json describing each amending law (dates, signatories, Federal Law Gazette citation, votes). Each version is a full
snapshot, so the changes are found by comparing consecutive snapshots article by article. Each article's words are then
attributed to the law that wrote them, and each change carries the date it took effect.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Dates the source lacks or gives for only part of a law, each with the evidence. Article-level dates override the
# law's own; "inForce" replaces it.
CORRECTIONS = {
    58: {
        'inForce': '2010-07-27',
        'why': 'The source gives no date. Article 2 of the law puts it in force on the day after promulgation, '
               'and it was promulgated in BGBl. I Nr. 38 of 26 July 2010.',
        'sources': ['https://www.buzer.de/gesetz/5041/l.htm', 'https://www.umwelt-online.de/recht/allgemei/z10_0944.htm'],
    },
    33: {
        'inForce': '1976-08-28',
        'articles': {'39': '1976-12-14', '45': '1976-12-14', '45a': '1976-12-14', '49': '1976-12-14'},
        'why': 'The law took effect on the day after promulgation (27 August 1976), except its changes to Articles 39, '
               '45, 45a and 49, which took effect on 14 December 1976, the first day of the next Bundestag.',
        'sources': ['https://dserver.bundestag.de/btd/07/055/0705527.pdf'],
    },
}

ORDINALS = {}


def git(repo: Path, *args: str, env: dict | None = None, input: str | None = None) -> str:
    out = subprocess.run(['git', *args], cwd=repo, capture_output=True, text=True, encoding='utf-8', env=env, input=input)
    if out.returncode:
        raise SystemExit(f'git {" ".join(args)} failed: {out.stderr}')
    return out.stdout


# ---------------------------------------------------------------- reading the source

def unit_key(name: str) -> str:
    m = re.fullmatch(r'(\d+)([a-z]?)\.md', name)
    return f'{int(m.group(1))}{m.group(2)}' if m else ''


def clean(line: str) -> str:
    line = re.sub(r'\[([^\]]+)\]\(#[^)]*\)', r'\1', line)   # in-page links: keep the words
    return re.sub(r'\s+', ' ', line).strip()


def parse_file(name: str, text: str) -> dict[str, dict]:
    """One source file as {unit key: {'section': heading or None, 'paras': [...]}}."""
    units: dict[str, dict] = {}
    section = None
    current = None
    for raw in text.split('\n'):
        if raw.startswith('%'):
            continue
        if raw.startswith('## '):
            current = unit_key(name) or clean(raw[3:]).lower()
            units[current] = {'section': section, 'paras': []}
            section = None
        elif raw.startswith('# '):
            heading = clean(raw[2:])
            if name == '000.md':
                current = {'Eingangsformel': 'eingangsformel', 'Präambel': 'praeambel'}.get(heading, heading.lower())
                units[current] = {'section': None, 'paras': []}
            else:
                section = heading
        elif raw.strip() and current is not None:
            units[current]['paras'].append(clean(raw))
    return units


def unit_order(key: str) -> tuple:
    if key == 'eingangsformel':
        return (-2, '')
    if key == 'praeambel':
        return (-1, '')
    m = re.fullmatch(r'(\d+)([a-z]?)', key)
    return (int(m.group(1)), m.group(2))


def label(key: str) -> str:
    return {'eingangsformel': 'Eingangsformel', 'praeambel': 'Präambel'}.get(key, f'Art. {key}')


def file_name(key: str) -> str:
    if key in ('eingangsformel', 'praeambel'):
        return f'{key}.md'
    m = re.fullmatch(r'(\d+)([a-z]?)', key)
    return f'{int(m.group(1)):03d}{m.group(2)}.md'


def read_source(src: Path):
    meta = json.loads((src / 'meta.json').read_text(encoding='utf-8'))
    revs = meta['revisions']
    commits = git(src, 'log', '--reverse', '--format=%H').split()
    assert len(commits) == len(revs), (len(commits), len(revs))
    # Every file of every version through one `git cat-file --batch`, keyed by blob so unchanged files parse once.
    listing = {h: [line.split(None, 3)[2:] for line in git(src, 'ls-tree', h).splitlines()] for h in commits}
    blobs = sorted({b for files in listing.values() for b, f in files if re.fullmatch(r'\d+[a-z]?\.md', f)})
    proc = subprocess.run(['git', 'cat-file', '--batch'], cwd=src, input='\n'.join(blobs).encode() + b'\n', capture_output=True)
    raw, pos, content = proc.stdout, 0, {}
    for b in blobs:
        header_end = raw.index(b'\n', pos)
        size = int(raw[pos:header_end].split()[2])
        content[b] = raw[header_end + 1:header_end + 1 + size].decode('utf-8')
        pos = header_end + 1 + size + 1
    parsed: dict[tuple[str, str], dict] = {}
    snapshots = []
    for h in commits:
        units: dict[str, dict] = {}
        for b, f in listing[h]:
            if not re.fullmatch(r'\d+[a-z]?\.md', f):
                continue
            if (b, f) not in parsed:
                parsed[(b, f)] = parse_file(f, content[b])
            units.update(parsed[(b, f)])
        snapshots.append(units)
    return meta, revs, snapshots


def read_docpatch(dev: Path):
    """DocPatch (c3e/grundgesetz-dev): the 1949 text in src/ and one quilt patch per amending law, in the order of
    src/patches/series. Each patch is applied in a scratch copy, and the text after each is one version."""
    import tempfile
    meta = json.loads((dev / 'etc' / 'meta.json').read_text(encoding='utf-8'))
    revs = meta['revisions']
    work = Path(tempfile.mkdtemp(prefix='docpatch-'))
    shutil.copytree(dev / 'src', work / 'src')

    def snapshot() -> dict:
        units: dict[str, dict] = {}
        for f in sorted((work / 'src').glob('*.md')):
            if re.fullmatch(r'\d+[a-z]?\.md', f.name):
                units.update(parse_file(f.name, f.read_text(encoding='utf-8')))
        return units
    snapshots = [snapshot()]
    for name in (work / 'src' / 'patches' / 'series').read_text(encoding='utf-8').split():
        patch = (work / 'src' / 'patches' / name).resolve()
        head = patch.read_text(encoding='utf-8')[:300]
        # Most patches name files a/NNN.md and b/NNN.md; the later ones src.orig/NNN.md and src/NNN.md.
        cwd, level = (work, '-p0') if re.search(r'^(Index: src/|--- src)', head, re.M) else (work / 'src', '-p1')
        out = subprocess.run(['patch', level, '-s', '--no-backup-if-mismatch', '-i', str(patch)], cwd=cwd, capture_output=True, text=True)
        if out.returncode:
            raise SystemExit(f'DocPatch patch {name} did not apply: {out.stdout} {out.stderr}')
        snapshots.append(snapshot())
    shutil.rmtree(work, ignore_errors=True)
    assert len(snapshots) == len(revs), (len(snapshots), len(revs))
    return meta, revs, snapshots


# ---------------------------------------------------------------- the official text (Gesetze im Internet)

# Converts Gesetze im Internet XML content to lines, as scripts/bundesrecht/build.py does, kept here so this file
# builds on its own.
GII_BLOCK = {'P', 'DT', 'DD', 'LA', 'row', 'Title', 'Subtitle', 'pre', 'TOC', 'kommentar'}
GII_SKIP = {'fussnoten', 'Footnotes', 'Footnote', 'FnArea', 'FnR', 'noindex', 'colspec', 'Accolade'}


def _squash(s: str) -> str:
    return re.sub(r'[ \t   ]+', ' ', s).strip()


def _flow(el, out: list[str], cur: list[str]) -> None:
    def flush():
        line = _squash(''.join(cur))
        if line:
            out.append(line)
        cur.clear()
    if el.tag in GII_SKIP:
        return
    if el.tag == 'BR':
        flush()
        return
    if el.tag == 'DL':
        flush()
        items = list(el)
        i = 0
        while i < len(items):
            ch = items[i]
            if ch.tag == 'DT':
                sub: list[str] = []
                if i + 1 < len(items) and items[i + 1].tag == 'DD':
                    _flow(items[i + 1], sub, [])
                    i += 1
                out.append(_squash(f"{''.join(ch.itertext())} {sub[0] if sub else ''}"))
                out.extend(sub[1:])
            elif ch.tag not in GII_SKIP:
                _flow(ch, out, cur)
                flush()
            i += 1
        return
    if el.text:
        cur.append(el.text)
    for ch in el:
        if ch.tag in GII_BLOCK or ch.tag in ('DL', 'table'):
            flush()
            _flow(ch, out, cur)
            flush()
        else:
            _flow(ch, out, cur)
        if ch.tail:
            cur.append(ch.tail)
    if el.tag in GII_BLOCK:
        flush()


def gii_units(xml: bytes) -> tuple[dict[str, dict], str]:
    """The Grundgesetz as Gesetze im Internet publishes it: {article key: {'section', 'paras'}} and the Stand note."""
    import xml.etree.ElementTree as ET
    root = ET.fromstring(re.sub(rb'<!DOCTYPE[^>]*>', b'', xml, count=1))
    norms = root.findall('norm')
    stand = ' '.join(_squash(s.findtext('standkommentar') or '') for s in norms[0].iter('standangabe'))
    units: dict[str, dict] = {}
    section = None
    for n in norms[1:]:
        md = n.find('metadaten')
        if md is None:
            continue
        g = md.find('gliederungseinheit')
        if g is not None:
            section = _squash(f"{g.findtext('gliederungsbez') or ''} {g.findtext('gliederungstitel') or ''}")
            continue
        en = (md.findtext('enbez') or '').strip()
        key = {'Eingangsformel': 'eingangsformel', 'Präambel': 'praeambel'}.get(en)
        if not key and re.fullmatch(r'Art\.?\s*\d+[a-z]?', en):
            key = en.split()[-1].replace('Art', '').strip('. ').lower()
        if not key:
            continue
        lines: list[str] = []
        content = n.find('textdaten/text/Content')
        if content is not None:
            cur: list[str] = []
            for ch in content:
                _flow(ch, lines, cur)
                if ch.tail:
                    cur.append(ch.tail)
            if _squash(''.join(cur)):
                lines.append(_squash(''.join(cur)))
        units[key] = {'section': section, 'paras': [clean(x) for x in lines if x.strip()]}
        section = None
    return units, stand


def read_gii(archive: Path) -> list[dict]:
    """Every version of the Grundgesetz in QuantLaw's archive of Gesetze im Internet, oldest first."""
    path = 'data/items/gg/BJNR000010949.xml'
    log = subprocess.run(['git', '--git-dir', str(archive), 'log', 'data', '--reverse', '--format=%H %s', '--', path],
                         capture_output=True, text=True, encoding='utf-8').stdout.split('\n')
    out = []
    for line in filter(None, log):
        h, subject = line.split(' ', 1)
        blob = subprocess.run(['git', '--git-dir', str(archive), 'show', f'{h}:{path}'], capture_output=True)
        if blob.returncode:
            continue   # a scrape that missed the file (5 May 2026)
        units, stand = gii_units(blob.stdout)
        m = re.search(r'scrape (\d{4}-\d{2}-\d{2})', subject)
        out.append({'commit': h, 'day': m.group(1) if m else '', 'units': units, 'stand': stand})
    return out


# The amending laws after DocPatch's last (the 63rd), from the Bundestag's Datenhandbuch, chapter 13.2 (as of
# 16 May 2025), checked against each law in the Bundesgesetzblatt. The vote on the 69th is the Bundestag's record.
LATER_LAWS = [
    {'id': 64, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 72, 105 und 125b)', 'passed': '2019-10-18', 'date': '2019-11-15',
     'announced': '2019-11-20', 'effectiveSince': '2019-11-21', 'gazette': 'BGBl. I 2019 S. 1546', 'term': '19',
     'initiativeOf': 'Fraktionen der CDU/CSU und SPD (BT-Drs. 19/11084)'},
    {'id': 65, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 104a und 143h)', 'passed': '2020-09-17', 'date': '2020-09-29',
     'announced': '2020-10-07', 'effectiveSince': '2020-10-08', 'gazette': 'BGBl. I 2020 S. 2048', 'term': '19',
     'initiativeOf': 'Fraktionen der CDU/CSU und SPD (BT-Drs. 19/20595)'},
    {'id': 66, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 87a)', 'passed': '2022-06-03', 'date': '2022-06-28',
     'announced': '2022-06-30', 'effectiveSince': '2022-07-01', 'gazette': 'BGBl. I 2022 S. 968', 'term': '20',
     'initiativeOf': 'Regierungsvorlage (BT-Drs. 20/1410)'},
    {'id': 67, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 82)', 'passed': '2022-12-01', 'date': '2022-12-19',
     'announced': '2022-12-23', 'effectiveSince': '2022-12-24', 'gazette': 'BGBl. I 2022 S. 2478', 'term': '20',
     'initiativeOf': 'Regierungsvorlage (BT-Drs. 20/2729)'},
    {'id': 68, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 93 und 94)', 'passed': '2024-12-19', 'date': '2024-12-20',
     'announced': '2024-12-27', 'effectiveSince': '2024-12-28', 'gazette': 'BGBl. 2024 I Nr. 439', 'term': '20',
     'initiativeOf': 'Fraktionen von BÜNDNIS 90/DIE GRÜNEN, CDU/CSU, FDP und SPD (BT-Drs. 20/12977)'},
    {'id': 69, 'title': 'Gesetz zur Änderung des Grundgesetzes (Artikel 109, 115 und 143h)', 'passed': '2025-03-18', 'date': '2025-03-22',
     'announced': '2025-03-24', 'effectiveSince': '2025-03-25', 'gazette': 'BGBl. 2025 I Nr. 94', 'term': '20',
     'initiativeOf': 'Fraktionen der CDU/CSU und SPD (BT-Drs. 20/15096)', 'votes': {'yes': 512, 'no': 206, 'abstentions': 0}},
]

# A temporary article's end, which is a change in its own right: Art. 2 Satz 2 of the 65th amending law
# (BGBl. I 2020 S. 2048): "Artikel 143h des Grundgesetzes tritt am 31. Dezember 2020 außer Kraft."
EXPIRIES = {65: {'date': '2020-12-31', 'articles': ['143h'],
                 'why': 'Article 143h expired under Article 2, second sentence, of the 65th amending law: "Artikel 143h '
                        'des Grundgesetzes tritt am 31. Dezember 2020 außer Kraft." The Bundestag\'s Datenhandbuch '
                        '(chapter 13.2) gives 31 December 2021, which the law\'s text contradicts; its chapter 13.3 agrees '
                        'with the law.',
                 'sources': ['https://media.offenegesetze.de/bgbl1/2020/bgbl1_2020_44.pdf#page=2']}}

STAND_LAW = {'15.11.2019': 64, '29.9.2020': 65, '28.6.2022': 66, '19.12.2022': 67, '20.12.2024': 68, '22.3.2025': 69, '28.3.2019': 63}


def stand_law(stand: str) -> int | None:
    m = re.search(r'Zuletzt geändert durch .*?G v\. (\d{1,2}\.\d{1,2}\.\d{4})', stand)
    return STAND_LAW.get(m.group(1)) if m else None


def same(a: dict | None, b: dict | None) -> bool:
    return (is_repealed(a) and is_repealed(b)) or (a is not None and b is not None and a['paras'] == b['paras'])


def reconcile(snapshots: list[dict], official: dict[str, dict], at: int) -> list[dict]:
    """Make version `at` match the official text, article by article. Where they differ, the official text replaces
    the source's from the article's last change up to `at`, because no law changed it in between. Returns one record
    per article corrected."""
    fixes = []
    for key in sorted(set(official) | set(snapshots[at]), key=unit_order):
        if same(snapshots[at].get(key), official.get(key)):
            continue
        last = 0
        for i in range(1, at + 1):
            if not same(snapshots[i].get(key), snapshots[i - 1].get(key)):
                last = i
        before = snapshots[at].get(key)
        after = official.get(key)
        for i in range(last, at + 1):
            snap = snapshots[i] = dict(snapshots[i])
            if after is None or is_repealed(after):
                if key in snap and not is_repealed(snap[key]):
                    snap[key] = {'section': snap[key]['section'], 'paras': ['(weggefallen)']}
            else:
                section = snap[key]['section'] if key in snap else after['section']
                snap[key] = {'section': section, 'paras': list(after['paras'])}
        fixes.append({'article': key, 'from': last,
                      'before': [] if is_repealed(before) else before['paras'],
                      'after': [] if is_repealed(after) else after['paras']})
    return fixes


def reconciliation_notes(fixes: list[dict], revs: list[dict]) -> list[dict]:
    """One correction note per reconciled article, with the words removed and added."""
    out = []
    for f in fixes:
        a, b = ' '.join(f['before']), ' '.join(f['after'])
        ops = difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).get_opcodes()
        parts = []
        for op, i1, i2, j1, j2 in ops:
            if op == 'equal':
                continue
            old, new = ' '.join(a.split()[i1:i2]), ' '.join(b.split()[j1:j2])
            parts.append(f'"{old}" became "{new}"' if old and new else f'"{new}" added' if new else f'"{old}" removed')
        since = 'the text of 1949' if f['from'] == 0 else f"the {f['from']}th amending law ({(revs[f['from']].get('effectiveSince') or '')[:4]})"
        out.append({'articles': [f['article']], 'law': f['from'], 'auto': True,
                    'why': f"The source's text differed from the official text of 2019; the official text is used from {since} on, "
                           f"when the article last changed. Differences: {'; '.join(parts[:6])}{' …' if len(parts) > 6 else ''}.",
                    'sources': ['https://www.gesetze-im-internet.de/gg/']})
    return out


def publisher_notes(corrections: list[dict], revs: list[dict]) -> list[dict]:
    """Gesetze im Internet correcting its own text after first publishing a law."""
    out = []
    for c in corrections:
        a, b = ' '.join(c['before']), ' '.join(c['after'])
        ops = difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).get_opcodes()
        parts = [f'"{" ".join(b.split()[j1:j2])}" added' if i1 == i2 else f'"{" ".join(a.split()[i1:i2])}" became "{" ".join(b.split()[j1:j2])}"'
                 for op, i1, i2, j1, j2 in ops if op != 'equal']
        out.append({'articles': [c['article']], 'law': c['law'], 'auto': True,
                    'why': f"Gesetze im Internet first published the {c['law']}th amending law's text with an error and corrected "
                           f"it on {c['day']} ({'; '.join(parts)}). The corrected text is used from that law on.",
                    'sources': ['https://www.gesetze-im-internet.de/gg/', 'https://github.com/QuantLaw/gesetze-im-internet']})
    return out


def is_repealed(unit: dict | None) -> bool:
    return unit is None or not unit['paras'] or all(re.fullmatch(r'[\[(]?(weggefallen|aufgehoben)[\])]?\.?', p, re.I) for p in unit['paras'])


# The one renumbering in the record. The Sixteenth Amendment (1968) repealed Article 96 and renumbered Article 96a as
# Article 96. The source applies it in 1968 but builds every later version of Article 96 from the repealed 1949 text,
# and keeps Article 96a. From 1968 on we drop Article 96a, and later versions of Article 96 take paragraphs 1 to 3
# from the 1968 text, which no later law changed, with the source's own paragraphs 4 and 5.
TEXT_CORRECTIONS = [{
    'articles': ['96', '96a'],
    'law': 16,
    'why': 'The Sixteenth Amendment (1968) repealed Article 96 and renumbered Article 96a as Article 96. The source '
           'applies this in its 1968 version, but builds every later version of Article 96 from the repealed 1949 '
           'text and keeps Article 96a. From 1968 on, Article 96a is dropped, and Article 96 keeps paragraphs 1 to 3 '
           'of the 1968 text, which no later law changed, with the later laws\' paragraphs 4 and 5.',
    'sources': ['https://www.gesetze-im-internet.de/gg/art_96.html', 'https://dejure.org/gesetze/GG/96.html'],
}]


def correct_snapshots(snapshots: list[dict]) -> None:
    moved = snapshots[16]['96']['paras'][:3]
    for nr in range(16, len(snapshots)):
        snap = snapshots[nr] = dict(snapshots[nr])
        snap.pop('96a', None)
        if nr > 16 and snap['96']['paras'][:3] != moved:
            snap['96'] = {**snap['96'], 'paras': moved + snap['96']['paras'][3:]}


# ---------------------------------------------------------------- the laws

def first_date(value: str | None) -> str | None:
    m = re.match(r'\d{4}-\d{2}-\d{2}', value or '')
    return m.group(0) if m else None


def short_name(rev: dict) -> str:
    nr = rev['id']
    if nr == 0:
        return 'Grundgesetz (1949)'
    year = (rev.get('date') or rev.get('announced') or '')[:4]
    return f'{nr}. Änderung ({year})'


def law_record(rev: dict) -> dict:
    nr = rev['id']
    fix = CORRECTIONS.get(nr, {})
    raw = rev.get('effectiveSince')
    gazette = []
    year = (rev.get('announced') or rev.get('date') or '')[:4]
    for s in rev.get('sources', []):
        part = s['title'].replace('BGBl. BGBl.', 'BGBl.').strip()
        gazette.append(f'{part} {year} S. {s["pages"]}')
    if rev.get('gazette'):
        gazette.append(rev['gazette'])
    if nr in EXPIRIES:
        e = EXPIRIES[nr]
        fix = {**fix, 'why': ((fix.get('why') + ' ') if fix.get('why') else '') + e['why'], 'sources': fix.get('sources', []) + e['sources']}
    votes = rev.get('votes')
    return {
        'nr': nr,
        'title': re.sub(r'\s+', ' ', rev['title']).strip(),
        'short': short_name(rev),
        'passed': rev.get('passed'),
        'signed': rev.get('date'),
        'promulgated': rev.get('announced'),
        'inForce': fix.get('inForce') or first_date(raw),
        'inForceSource': raw,
        'correction': {'why': fix['why'], 'sources': fix['sources']} if fix else None,
        'gazette': gazette,
        'signers': [{'name': p['name'], 'role': p['role']} for p in rev.get('signedOffBy', [])],
        'votes': {k: votes[k] for k in ('yes', 'no', 'abstentions', 'notVoted', 'invalid') if k in votes} if votes else None,
        'votesSource': votes.get('uri') if votes else None,
        'term': rev.get('term') or (rev.get('legislativeSession') or {}).get('id'),
        'initiative': rev.get('initiativeOf'),
    }


def in_force(law: dict, key: str) -> str:
    fix = CORRECTIONS.get(law['nr'], {})
    return fix.get('articles', {}).get(key) or law['inForce']


# ---------------------------------------------------------------- words and authorship

TOKEN = re.compile(r'\n|[^\S\n]+|[\w§]+|[^\w\s]')


def tokens(paras: list[str]) -> list[str]:
    return TOKEN.findall('\n'.join(paras))


def attribute(prev_toks: list[str], prev_by: list[int], toks: list[str], nr: int) -> list[int]:
    by = [nr] * len(toks)
    sm = difflib.SequenceMatcher(None, prev_toks, toks, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            by[b + k] = prev_by[a + k]
    # A space between two words by the same law belongs to that law.
    for i in range(1, len(toks) - 1):
        if toks[i].isspace() and toks[i] != '\n' and by[i - 1] == by[i + 1]:
            by[i] = by[i - 1]
    return by


def runs(toks: list[str], by: list[int]) -> list[list[list]]:
    """Per paragraph, [[text, law], ...] with neighbouring words by the same law joined."""
    out: list[list[list]] = [[]]
    for t, n in zip(toks, by):
        if t == '\n':
            out.append([])
            continue
        line = out[-1]
        if line and line[-1][1] == n:
            line[-1][0] += t
        else:
            line.append([t, n])
    return out


def redline(old: list[str], new: list[str]) -> list[list]:
    """Word-level differences as [[kind, text], ...], kind '=' kept, '+' added, '-' struck."""
    a, b = tokens(old), tokens(new)
    out: list[list] = []

    def push(kind: str, s: str):
        if out and out[-1][0] == kind:
            out[-1][1] += s
        else:
            out.append([kind, s])
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal':
            push('=', ''.join(a[i1:i2]))
        else:
            if i2 > i1:
                push('-', ''.join(a[i1:i2]))
            if j2 > j1:
                push('+', ''.join(b[j1:j2]))
    # A single kept space between two changes reads as part of them.
    merged: list[list] = []
    for i, seg in enumerate(out):
        if seg[0] == '=' and seg[1].strip() == '' and 0 < i < len(out) - 1 and out[i - 1][0] != '=' and out[i + 1][0] != '=':
            seg = ['-', seg[1]]
        if merged and merged[-1][0] == seg[0]:
            merged[-1][1] += seg[1]
        else:
            merged.append(list(seg))
    return merged


# ---------------------------------------------------------------- the record

def build_record(revs: list[dict], steps: list[dict]):
    """Each step is one law's change to the text: {'law': nr, 'units': the whole text after it, 'inForce': date or
    None}. A law can have more than one step (a temporary article's later expiry)."""
    laws = [law_record(r) for r in revs]
    snapshots = [s['units'] for s in steps]
    keys = sorted({k for s in snapshots for k in s}, key=unit_order)
    articles = {}
    mismatches = []
    for key in keys:
        versions = []
        prev = None
        prev_toks: list[str] = []
        prev_by: list[int] = []
        for step in steps:
            nr, snap = step['law'], step['units']
            unit = snap.get(key)
            gone = is_repealed(unit)
            if prev is None and gone:
                continue
            if prev is not None and (gone and prev['repealed'] or (not gone and not prev['repealed'] and unit['paras'] == prev['paras'])):
                continue
            law = laws[nr]
            kind = 'created' if prev is None or prev['repealed'] and not gone else 'repealed' if gone else 'updated'
            paras = [] if gone else unit['paras']
            toks = tokens(paras)
            by = attribute(prev_toks if prev and not prev['repealed'] else [], prev_by if prev and not prev['repealed'] else [], toks, nr)
            versions.append({
                'nr': nr, 'kind': kind, 'inForce': step.get('inForce') or in_force(law, key), 'repealed': gone, 'paras': paras,
                'runs': runs(toks, by) if paras else [],
                'redline': redline(prev['paras'] if prev and not prev['repealed'] else [], paras) if nr else [],
            })
            prev, prev_toks, prev_by = versions[-1], toks, by
            if nr and 'articles' in revs[nr]:
                listed = revs[nr].get('articles') or {}
                bucket = {'created': 'created', 'updated': 'updated', 'repealed': 'deleted'}[kind]
                if key not in (listed.get(bucket) or []) and key not in ('eingangsformel', 'praeambel'):
                    mismatches.append((nr, key, kind, {k: v for k, v in listed.items() if v}))
        # The order of changes must not depend on whether we sort by law or by date in force.
        dates = [v['inForce'] or '' for v in versions]
        assert dates == sorted(dates), (key, dates)
        last_section = None
        for snap in snapshots:
            if key in snap and snap[key]['section']:
                last_section = snap[key]['section']
        articles[key] = {'key': key, 'label': label(key), 'file': file_name(key), 'sectionStart': last_section, 'versions': versions}
    for law in laws:
        law['changes'] = [
            {'key': k, 'kind': v['kind']}
            for k, a in articles.items() for v in a['versions'] if v['nr'] == law['nr'] and law['nr']
        ]
    return laws, articles, mismatches


def sections_of(articles: dict) -> list[dict]:
    """The Basic Law's own sections in order, each with its articles."""
    out: list[dict] = []
    for key in sorted(articles, key=unit_order):
        a = articles[key]
        if a['sectionStart'] or not out:
            out.append({'title': a['sectionStart'] or 'Eingang', 'keys': []})
        out[-1]['keys'].append(key)
    return out


# ---------------------------------------------------------------- the site's data

def write_site(site: Path, laws: list[dict], articles: dict, sections: list[dict], sources: dict, built: str):
    data = site / 'app' / 'watch' / 'grundgesetz' / '_data'
    if data.exists():
        shutil.rmtree(data / 'artikel', ignore_errors=True)
    (data / 'artikel').mkdir(parents=True, exist_ok=True)
    index = []
    for key in sorted(articles, key=unit_order):
        a = articles[key]
        vs = a['versions']
        index.append({
            'key': key, 'label': a['label'], 'changes': sum(1 for v in vs if v['nr']),
            'first': vs[0]['inForce'], 'lastChange': next((v['inForce'] for v in reversed(vs) if v['nr']), None),
            'repealed': vs[-1]['repealed'],
            'opening': (vs[-1]['paras'] or next((v['paras'] for v in reversed(vs) if v['paras']), ['']))[0][:180],
        })
        (data / 'artikel' / f'{key}.json').write_text(json.dumps(a, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    meta = {
        'source': 'https://github.com/c3e/grundgesetz-dev', 'sourceCommit': sources['docpatch'],
        'official': 'https://www.gesetze-im-internet.de/gg/', 'officialArchive': 'https://github.com/QuantLaw/gesetze-im-internet',
        'officialVersions': sources['gii'],
        'first': laws[0]['inForce'], 'last': max(l['inForce'] for l in laws if l['inForce']),
        'built': built,
        'textCorrections': TEXT_CORRECTIONS,
    }
    (data / 'laws.json').write_text(json.dumps(laws, ensure_ascii=False, indent=1), encoding='utf-8')
    (data / 'index.json').write_text(json.dumps({'meta': meta, 'sections': sections, 'articles': index}, ensure_ascii=False, indent=1), encoding='utf-8')


# ---------------------------------------------------------------- the public repository

def last_sunday(year: int, month: int) -> dt.date:
    d = dt.date(year, month + 1, 1) - dt.timedelta(days=1) if month < 12 else dt.date(year, 12, 31)
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)


def berlin_offset(day: dt.date) -> int:
    """Hours ahead of UTC at midnight in Berlin. Summer time returned to West Germany in 1980; until 1995 it ended on
    the last Sunday in September, since 1996 on the last Sunday in October. Clocks change at night, after midnight."""
    if day.year < 1980:
        return 1
    start = last_sunday(day.year, 3)
    end = last_sunday(day.year, 9 if day.year < 1996 else 10)
    return 2 if start < day <= end else 1


def commit_date(day: str, seq: int) -> str:
    """Midnight in Berlin on the day a change took effect. Git cannot record a time before the start of 1970 in UTC,
    which is 1 a.m. in Berlin, so changes in force before then are dated 1 January 1970 (UTC), a second apart in the
    order they took effect; their real dates are in the message and the tags."""
    d = dt.date.fromisoformat(day)
    off = berlin_offset(d)
    stamp = int(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())
    if stamp <= seq:
        return f'@{seq + 1} +0000'
    return f'@{stamp} +0{off}00'


def docs_stamp(day: str) -> str:
    """Noon in Berlin on the given day: the documentation commit's date, given on the command line so that a rebuild on
    another day makes the same commit."""
    d = dt.date.fromisoformat(day)
    off = berlin_offset(d)
    return f'@{int(dt.datetime(d.year, d.month, d.day, 12, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())} +0{off}00'


def article_md(key: str, paras: list[str]) -> str:
    head = {'eingangsformel': 'Eingangsformel', 'praeambel': 'Präambel'}.get(key, f'Artikel {key}')
    # The paragraph number goes on a line of its own, so renumbering ("(3)" becoming "(7)") changes that line only and
    # blame keeps crediting the words to the law that wrote them. Markdown renders it the same.
    body = [re.sub(r'^\((\d+[a-z]?)\)\s+', lambda m: f'({m.group(1)})\n', p) for p in paras]
    return f'# {head}\n\n' + '\n\n'.join(body) + '\n'


def message(law: dict, keys: list[tuple[str, str]], day: str, part: str | None) -> str:
    title = law['title']
    # The subject stays within 72 characters so git's one-line views show it whole; the full title follows.
    what = {'repealed': 'aufgehoben'}.get(keys[0][1], '') if len({k for _, k in keys}) == 1 else ''
    arts = ', '.join(label(k) for k, _ in keys)
    subject = f"{law['short']}: {arts}{' ' + what if what else ''}"
    if len(subject) > 72:
        subject = f"{law['short']}: {len(keys)} Artikel{' ' + what if what else ''}"
    lines = [subject, '', title + (f' ({part})' if part else ''), '']
    changed = {'created': [], 'updated': [], 'repealed': []}
    for k, kind in keys:
        changed[kind].append(label(k))
    names = {'created': 'Eingefügt', 'updated': 'Geändert', 'repealed': 'Aufgehoben'}
    for kind, items in changed.items():
        if items:
            lines.append(f'{names[kind]}: {", ".join(items)}')
    lines.append('')
    if law['passed']:
        lines.append(f'Beschlossen: {law["passed"]}')
    if law['signed']:
        lines.append(f'Ausgefertigt: {law["signed"]}')
    if law['promulgated']:
        lines.append(f'Verkuendet: {law["promulgated"]}' + (f' ({"; ".join(law["gazette"])})' if law['gazette'] else ''))
    lines.append(f'In-Kraft: {day}')
    if law['correction']:
        lines.append(f'Nachweis: {law["correction"]["sources"][0]}')
    for s in law['signers']:
        lines.append(f'Unterzeichnet: {s["name"]}, {s["role"]}')
    if law['votes']:
        v = law['votes']
        lines.append(f'Abstimmung: {v.get("yes", 0)} ja, {v.get("no", 0)} nein, {v.get("abstentions", 0)} Enthaltungen')
    if law['initiative']:
        lines.append(f'Initiative: {law["initiative"]}')
    lines.append(f'Gesetz: {law["nr"]}')
    return '\n'.join(lines) + '\n'


def write_repo(repo: Path, laws: list[dict], articles: dict, sections: list[dict], docs: Path, docs_date: str,
               sources: dict | None = None, reconciled: int = 0):
    # A rebuild starts from an empty history but keeps the remote, so it can be pushed where it came from.
    # It deletes whatever is in the target, so it only accepts an empty folder or one of its own earlier builds.
    if repo.exists() and any(repo.iterdir()) and not ((repo / '.git').exists() and (repo / 'KORREKTUREN.md').exists()):
        raise SystemExit(f'{repo} is not empty and is not an earlier build of this repository; refusing to delete it')
    remote = None
    if (repo / '.git').exists():
        got = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=repo, capture_output=True, text=True)
        remote = got.stdout.strip() or None
    if repo.exists():
        shutil.rmtree(repo / '.git', ignore_errors=True)
        for p in repo.iterdir():
            if p.name != '.git':
                shutil.rmtree(p) if p.is_dir() else p.unlink()
    repo.mkdir(parents=True, exist_ok=True)
    git(repo, 'init', '-q', '-b', 'main')
    git(repo, 'config', 'core.autocrlf', 'false')
    if remote:
        git(repo, 'remote', 'add', 'origin', remote)
    # One commit per law and date in force (a law with two dates is two commits), in the order they took effect.
    events: dict[tuple[str, int], list[tuple[str, dict]]] = {}
    for key, a in articles.items():
        for v in a['versions']:
            events.setdefault((v['inForce'], v['nr']), []).append((key, v))
    by_law: dict[int, int] = {}
    for (_, nr) in events:
        by_law[nr] = by_law.get(nr, 0) + 1
    seen_parts: dict[int, int] = {}
    tags: dict[str, str] = {}
    (repo / 'artikel').mkdir()
    for seq, (day, nr) in enumerate(sorted(events)):
        law = laws[nr]
        for key, v in events[(day, nr)]:
            path = repo / 'artikel' / file_name(key)
            if v['repealed']:
                path.unlink(missing_ok=True)
            else:
                path.write_text(article_md(key, v['paras']), encoding='utf-8', newline='\n')
        git(repo, 'add', '-A')
        seen_parts[nr] = seen_parts.get(nr, 0) + 1
        part = f'Teil {seen_parts[nr]} von {by_law[nr]}' if by_law[nr] > 1 else None
        when = commit_date(day, seq)
        env = {**os.environ, 'GIT_AUTHOR_NAME': law['short'], 'GIT_AUTHOR_EMAIL': '', 'GIT_AUTHOR_DATE': when,
               'GIT_COMMITTER_NAME': 'Lexifina Watch', 'GIT_COMMITTER_EMAIL': '', 'GIT_COMMITTER_DATE': when}
        keys = sorted(((k, v['kind']) for k, v in events[(day, nr)]), key=lambda x: unit_order(x[0]))
        git(repo, 'commit', '-q', '--allow-empty-message', '-F', '-', env=env, input=message(law, keys, day, part))
        head = git(repo, 'rev-parse', 'HEAD').strip()
        tags[f'in-kraft/{day}'] = head
        if seen_parts[nr] == by_law[nr]:
            tags[f'gesetz/{nr:02d}'] = head
    for name, head in tags.items():
        git(repo, 'tag', name, head)
    # The documentation comes last, by Lexifina Watch, so it never appears as the author of the law's words.
    for p in docs.rglob('*'):
        if p.is_file():
            dest = repo / p.relative_to(docs)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)
    shutil.copyfile(Path(__file__), repo / 'tools' / 'build.py')   # the exact script that built this history
    write_repo_tables(repo, laws, articles, sections)
    # REPRODUCE.md describes this build: its numbers are filled in here, so they cannot go stale.
    rep = repo / 'REPRODUCE.md'
    if rep.exists() and sources:
        script = Path(__file__).read_bytes()
        fill = {
            'DOCPATCH_COMMIT': sources['docpatch'],
            'GII_VERSIONS': f"{len(sources['gii'])} archived versions, " + ', '.join(f'{d} (`{c[:10]}`)' for d, c in sources['gii']),
            'LAW_COMMITS': str(len(events)),
            'LAST_LAW_COMMIT': git(repo, 'rev-parse', 'HEAD').strip(),
            'BUILD_BLOB': hashlib.sha1(b'blob %d\x00' % len(script) + script).hexdigest(),
            'GESETZE_JSON_SHA': hashlib.sha256((repo / 'gesetze.json').read_bytes()).hexdigest(),
            'GESETZE_CSV_SHA': hashlib.sha256((repo / 'gesetze.csv').read_bytes()).hexdigest(),
            'RECONCILED': str(reconciled),
            'DOCS_DATE': docs_date,
        }
        text = rep.read_text(encoding='utf-8')
        for k, v in fill.items():
            text = text.replace('{{' + k + '}}', v)
        rep.write_text(text, encoding='utf-8', newline='\n')
    git(repo, 'add', '-A')
    now = docs_stamp(docs_date)
    env = {**os.environ, 'GIT_AUTHOR_NAME': 'Lexifina Watch', 'GIT_AUTHOR_EMAIL': '', 'GIT_AUTHOR_DATE': now,
           'GIT_COMMITTER_NAME': 'Lexifina Watch', 'GIT_COMMITTER_EMAIL': '', 'GIT_COMMITTER_DATE': now}
    git(repo, 'commit', '-q', '-m', 'Dokumentation, Tabellen und Werkzeuge', env=env)
    return len(events), len(tags)


def write_repo_tables(repo: Path, laws: list[dict], articles: dict, sections: list[dict]):
    rows = []
    for law in laws:
        dates = sorted({v['inForce'] for a in articles.values() for v in a['versions'] if v['nr'] == law['nr']})
        rows.append({
            'gesetz': law['nr'], 'titel': law['title'], 'beschlossen': law['passed'] or '', 'ausgefertigt': law['signed'] or '',
            'verkuendet': law['promulgated'] or '', 'fundstelle': '; '.join(law['gazette']), 'in_kraft': '; '.join(dates),
            'geaendert': ' '.join(label(c['key']) for c in law['changes'] if c['kind'] == 'updated'),
            'eingefuegt': ' '.join(label(c['key']) for c in law['changes'] if c['kind'] == 'created'),
            'aufgehoben': ' '.join(label(c['key']) for c in law['changes'] if c['kind'] == 'repealed'),
            'ja': (law['votes'] or {}).get('yes', ''), 'nein': (law['votes'] or {}).get('no', ''),
            'enthaltungen': (law['votes'] or {}).get('abstentions', ''),
        })
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    (repo / 'gesetze.csv').write_text(buf.getvalue(), encoding='utf-8', newline='\n')
    (repo / 'gesetze.json').write_text(json.dumps(laws, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')

    out = ['# Artikel', '', 'Jeder Artikel mit der Zahl seiner Änderungen und dem Tag, an dem die letzte in Kraft trat.',
           'Every article, with how often it was changed and when the last change took effect.', '']
    for sec in sections:
        out += [f'## {sec["title"]}', '', '| Artikel | Änderungen | Zuletzt geändert |', '| --- | --- | --- |']
        for key in sec['keys']:
            vs = articles[key]['versions']
            n = sum(1 for v in vs if v['nr'])
            last = next((v['inForce'] for v in reversed(vs) if v['nr']), '')
            name = label(key) + (' (aufgehoben)' if vs[-1]['repealed'] else '')
            link = f'[{name}]({file_name(key)})' if not vs[-1]['repealed'] else name
            out.append(f'| {link} | {n} | {last} |')
        out.append('')
    (repo / 'artikel' / 'README.md').write_text('\n'.join(out), encoding='utf-8', newline='\n')

    fixes = ['# Korrekturen / Corrections', '',
             'Wo die Quelle ein Datum nicht oder nur für einen Teil eines Gesetzes angibt, steht hier, was wir eingesetzt haben und warum.',
             'Where the source lacks a date, or gives one for only part of a law, this is what we used and why.', '']
    for nr, fix in sorted(CORRECTIONS.items()):
        law = laws[nr]
        fixes += [f'## {law["title"]}', '', f'- In Kraft / in force: {fix["inForce"]}']
        for k, d in fix.get('articles', {}).items():
            fixes.append(f'- {label(k)}: {d}')
        fixes += ['', fix['why'], ''] + [f'- <{s}>' for s in fix['sources']] + ['']
    for fix in TEXT_CORRECTIONS:
        fixes += [f'## {", ".join(label(k) for k in fix["articles"])} (Text)', '', fix['why'], '']
        fixes += [f'- <{s}>' for s in fix['sources']] + ['']
    (repo / 'KORREKTUREN.md').write_text('\n'.join(fixes), encoding='utf-8', newline='\n')


def assemble(dev: Path, archive: Path):
    """The whole history as steps: DocPatch's 64 versions (1949 to the 63rd amending law), reconciled with the
    official text of 2019, then each later amending law as Gesetze im Internet first published it."""
    meta, revs, snapshots = read_docpatch(dev)
    correct_snapshots(snapshots)
    gii = read_gii(archive)
    base = next(i for i, g in enumerate(gii) if stand_law(g['stand']) == 63)
    fixes = reconcile(snapshots, gii[base]['units'], 63)
    steps = [{'law': i, 'units': u, 'inForce': None} for i, u in enumerate(snapshots)]
    state, prev, applied, unexplained = snapshots[63], gii[base]['units'], {63}, []
    for g in gii[base + 1:]:
        changed = sorted((k for k in set(prev) | set(g['units']) if not same(prev.get(k), g['units'].get(k))), key=unit_order)
        prev = g['units']
        if not changed:
            continue
        new = dict(state)
        for k in changed:
            u = g['units'].get(k)
            new[k] = {'section': (state.get(k) or u or {}).get('section'), 'paras': list(u['paras']) if u else ['(weggefallen)']}
        law = stand_law(g['stand'])
        if law and law not in applied:
            steps.append({'law': law, 'units': new, 'inForce': None})
            applied.add(law)
        elif law in EXPIRIES and set(changed) <= set(EXPIRIES[law]['articles']):
            steps.append({'law': law, 'units': new, 'inForce': EXPIRIES[law]['date']})
        else:
            # No law took effect: the publisher corrected its own text. The corrected words belong to the version made
            # by the law that last changed each article, so they replace that version and every later one.
            for k in changed:
                last = max(i for i, st in enumerate(steps) if i == 0 or not same(st['units'].get(k), steps[i - 1]['units'].get(k)))
                for st in steps[last:]:
                    st['units'] = dict(st['units'])
                    st['units'][k] = new[k]
                unexplained.append({'day': g['day'], 'article': k, 'law': steps[last]['law'],
                                    'before': (state.get(k) or {}).get('paras', []), 'after': new[k]['paras']})
        state = new
    revs = revs + [dict(r) for r in LATER_LAWS]
    assert [r['id'] for r in revs] == list(range(len(revs))), [r['id'] for r in revs]
    sources = {'docpatch': git(dev, 'rev-parse', 'HEAD').strip(),
               'gii': [(g['day'], g['commit']) for g in gii[base:]]}
    return revs, steps, fixes, unexplained, sources


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--docpatch', default=str(ROOT.parent / 'gg-dev'), help='a clone of c3e/grundgesetz-dev')
    ap.add_argument('--archive', default=str(ROOT.parent / 'german-law-sources' / '03-git' / 'QuantLaw_gesetze-im-internet.git'),
                    help="a clone of QuantLaw/gesetze-im-internet, with its 'data' branch")
    ap.add_argument('--site', default=str(ROOT / 'saas-webpage'))
    ap.add_argument('--repo', default=str(ROOT.parent / 'germany-law'))
    ap.add_argument('--no-repo', action='store_true')
    ap.add_argument('--docs-date', required=True, help='date of the documentation commit and of the build (YYYY-MM-DD)')
    args = ap.parse_args()
    revs, steps, fixes, unexplained, sources = assemble(Path(args.docpatch), Path(args.archive))
    TEXT_CORRECTIONS.extend(reconciliation_notes(fixes, revs))
    TEXT_CORRECTIONS.extend(publisher_notes(unexplained, revs))
    laws, articles, mismatches = build_record(revs, steps)
    sections = sections_of(articles)
    write_site(Path(args.site), laws, articles, sections, sources, args.docs_date)
    print(f'{len(laws)} laws, {len(steps)} steps, {len(articles)} articles, '
          f'{sum(len(a["versions"]) for a in articles.values())} article versions, {len(sections)} sections')
    print(f'{len(fixes)} articles reconciled with the official text of 2019')
    for u in unexplained:
        print(f"publisher correction on {u['day']}: Art. {u['article']}, applied to the version of law {u['law']}")
    if not args.no_repo:
        commits, tags = write_repo(Path(args.repo), laws, articles, sections, Path(__file__).parent / 'repo', args.docs_date,
                                   sources, len(fixes))
        print(f'repo: {commits} law commits, {tags} tags -> {args.repo}')


if __name__ == '__main__':
    main()
