"""Builds a git history of all German federal law from QuantLaw's daily archive of gesetze-im-internet.de.

    python -X utf8 scripts/bundesrecht/build.py --archive <QuantLaw_gesetze-im-internet.git> --repo <out> --docs-date YYYY-MM-DD

The archive is a git repository whose `data` branch holds one commit per scrape of gesetze-im-internet.de (weekly from
10 June 2019, daily from May 2020), each with the official XML of every act. This script:

1. reads every scrape in order, with the blob of each act file that changed (one `git log --raw`),
2. converts each act's XML to Markdown (one heading per norm, one line per paragraph or list item), dropping the
   publisher's build stamps and footnotes, so that only changes to the text count,
3. groups the acts whose text changed in a scrape by the amending law named in their new "Stand" note
   ("Zuletzt geändert durch Art. 1 G v. 22.3.2025 I Nr. 94"), and writes one commit per amending law per day, with
   that law as the author, using `git fast-import`.

The first scrape becomes one commit holding every act as it stood that day. A change whose Stand note names no new law
is committed under its own label. The same archive gives the same commits.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

COMMITTER = 'Lexifina <bundesrecht@lexifina.com>'
SOURCE = 'https://www.gesetze-im-internet.de'

# ---------------------------------------------------------------- time

def last_sunday(year: int, month: int) -> dt.date:
    d = (dt.date(year, month + 1, 1) if month < 12 else dt.date(year + 1, 1, 1)) - dt.timedelta(days=1)
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)


def berlin_offset(day: dt.date) -> int:
    """Hours ahead of UTC at noon in Berlin (summer time from the last Sunday in March to the last Sunday in October)."""
    return 2 if last_sunday(day.year, 3) <= day < last_sunday(day.year, 10) else 1


def noon(day: str) -> str:
    d = dt.date.fromisoformat(day)
    off = berlin_offset(d)
    return f'{int(dt.datetime(d.year, d.month, d.day, 12, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())} +0{off}00'

# ---------------------------------------------------------------- XML to Markdown

BLOCK = {'P', 'DT', 'DD', 'LA', 'row', 'Title', 'Subtitle', 'pre', 'TOC', 'kommentar'}
SUPER = str.maketrans('0123456789abcdefghijklmnoprstuvwxyz', '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ')
SKIP = {'fussnoten', 'Footnotes', 'Footnote', 'FnArea', 'FnR', 'noindex', 'colspec', 'Accolade'}


def squash(s: str) -> str:
    return re.sub(r'[ \t   ]+', ' ', s).strip()


def flow(el: ET.Element, out: list[str], cur: list[str], depth: int) -> None:
    """Walk mixed content: text runs into the current line, block elements and <BR/> end it."""
    def flush():
        line = squash(''.join(cur))
        if line:
            out.append(('  ' * depth) + line)
        cur.clear()
    tag = el.tag
    if tag in SKIP:
        return
    if tag == 'IMG':
        cur.append(f"[Bild: {el.get('SRC') or el.get('src') or ''}]")
    elif tag == 'SUP':
        cur.append(''.join(el.itertext()).translate(SUPER))
        if el.tail:
            pass
        return
    elif tag == 'BR':
        flush()
    elif tag == 'row':
        flush()
        cells = [squash(''.join(e.itertext())) for e in el.iter('entry')]
        out.append(('  ' * depth) + '| ' + ' | '.join(cells) + ' |')
        if el.tail:
            cur.append(el.tail)
        return
    if el.text and tag not in ('IMG',):
        cur.append(el.text)
    if tag == 'DL':
        flush()
        items = list(el)
        i = 0
        while i < len(items):
            ch = items[i]
            if ch.tag == 'DT':
                label = squash(''.join(ch.itertext()))
                sub: list[str] = []
                if i + 1 < len(items) and items[i + 1].tag == 'DD':
                    flow(items[i + 1], sub, [], 0)
                    i += 1
                first = sub[0].strip() if sub else ''
                out.append(('  ' * depth) + squash(f'{label} {first}'))
                out.extend(('  ' * (depth + 1)) + x for x in sub[1:])
            elif ch.tag not in SKIP:
                flow(ch, out, cur, depth + 1)
                flush()
            i += 1
        return   # the caller adds this element's tail
    child_depth = depth
    for ch in el:
        if ch.tag in BLOCK or ch.tag in ('DL', 'table'):
            flush()
            flow(ch, out, cur, child_depth)
            flush()
        else:
            flow(ch, out, cur, child_depth)
        if ch.tail and ch.tag != 'row':
            cur.append(ch.tail)
    if tag in BLOCK:
        flush()


def content_lines(el: ET.Element | None) -> list[str]:
    if el is None:
        return []
    out: list[str] = []
    cur: list[str] = []
    for ch in el:
        flow(ch, out, cur, 0)
        if ch.tail:
            cur.append(ch.tail)
    line = squash(''.join(cur))
    if line:
        out.append(line)
    return out


UMLAUT = str.maketrans({'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'})


def norm_slug(label: str) -> str:
    """A file name for a norm from its label: '§ 433' -> '0433', '§ 32a' -> '0032a', 'Art 1' -> 'art-1',
    'Anlage 2 (zu § 5)' -> 'anlage-2-zu-5'. A leading number is padded so the files sort in order."""
    s = label.lower().translate(UMLAUT)
    tokens = re.findall(r'[a-z]+|\d+[a-z]?', s.replace('§', ' '))
    if not tokens:
        return ''
    if re.fullmatch(r'\d+[a-z]?', tokens[0]):
        m = re.fullmatch(r'(\d+)([a-z]?)', tokens[0])
        tokens[0] = m.group(1).zfill(4) + m.group(2)
    return '-'.join(tokens)[:80]


def paragraph_lines(body: list[str]) -> list[str]:
    """One paragraph number per line ("(3)"), so renumbering changes that line only and blame keeps the words' author."""
    out = []
    for line in body:
        m = re.match(r'^(\s*)\((\d+[a-z]?)\)\s+(.*)$', line)
        if m:
            out += [f'{m.group(1)}({m.group(2)})', f'{m.group(1)}{m.group(3)}']
        else:
            out.append(line)
    return out


def act_from_xml(data: bytes) -> dict:
    """An act as files: one per norm (`0433.md`), and `index.md` with the title, the act's divisions and its norms in
    order. 'markdown' is all of them joined, for telling whether the act changed."""
    data = re.sub(rb'<!DOCTYPE[^>]*>', b'', data, count=1)
    root = ET.fromstring(data)
    norms = root.findall('norm')
    head = norms[0].find('metadaten') if norms else None
    meta = {
        'jurabk': (head.findtext('jurabk') or '').strip() if head is not None else '',
        'amtabk': (head.findtext('amtabk') or '').strip() if head is not None else '',
        'title': squash(head.findtext('langue') or head.findtext('kurzue') or '') if head is not None else '',
        'ausfertigung': (head.findtext('ausfertigung-datum') or '').strip() if head is not None else '',
        'fundstelle': ' '.join(squash(''.join(f.itertext())) for f in head.findall('fundstelle')) if head is not None else '',
        'stand': [(squash(s.findtext('standtyp') or ''), squash(s.findtext('standkommentar') or '')) for s in head.findall('standangabe')] if head is not None else [],
    }
    notes = [squash(' '.join(f.itertext())) for n in norms for f in n.iter('fussnoten')]
    index = [f"# {meta['title'] or meta['jurabk']}", '']
    files: dict[str, str] = {}
    unnamed = 0
    for n in norms[1:]:
        md = n.find('metadaten')
        g = md.find('gliederungseinheit') if md is not None else None
        if g is not None:
            level = max(2, min(5, len((g.findtext('gliederungskennzahl') or '000').strip()) // 3 + 1))
            index += ['', '#' * level + ' ' + squash(f"{g.findtext('gliederungsbez') or ''} {g.findtext('gliederungstitel') or ''}"), '']
            continue
        enbez = squash(md.findtext('enbez') or '') if md is not None else ''
        titel = squash(''.join(md.find('titel').itertext())) if md is not None and md.find('titel') is not None else ''
        heading = squash(f'{enbez} {titel}')
        body = paragraph_lines(content_lines(n.find('textdaten/text/Content')))
        if not heading and not body:
            continue
        name = norm_slug(enbez) or norm_slug(titel)
        if not name:
            unnamed += 1
            name = f'text-{unnamed}'
        if name == 'index':
            name = 'index-norm'
        base, k = name, 1
        while f'{name}.md' in files:
            k += 1
            name = f'{base}-{k}'
        files[f'{name}.md'] = (f'# {heading}\n\n' if heading else '') + '\n'.join(body).rstrip() + '\n'
        index.append(f'- [{heading or name}]({name}.md)')
    files['index.md'] = '\n'.join(index).rstrip() + '\n'
    joined = files['index.md'] + ''.join(f'\n<!-- {k} -->\n{v}' for k, v in files.items() if k != 'index.md')
    return {'meta': meta, 'files': files, 'markdown': joined, 'notes': [x for x in notes if 'mWv' in x]}

# ---------------------------------------------------------------- amending laws

REF = re.compile(r'durch\s+(?:(?:Art\.|Artikel|§|Nr\.)\s*\d+[a-z]?(?:\s*(?:u\.|und|,|bis)\s*\d+[a-z]?)*\s+)*(?P<ref>(?:[A-ZÄÖÜ][\w-]*\.?\s+)?v\.\s*\d{1,2}\.\d{1,2}\.\d{4}(?:\s+(?:I|II|III))?(?:\s+(?:S\.|Nr\.)?\s*[\w/]+)?)')


def amending_law(stand: list[tuple[str, str]]) -> str | None:
    """The law named by the "Stand" note: 'Zuletzt geändert durch Art. 1 G v. 22.3.2025 I Nr. 94' -> 'G v. 22.3.2025 I Nr. 94'."""
    # "Neugefasst durch Bek. ...;" and "zuletzt geändert durch G ..." can be separate Stand entries: the last law named
    # in them is the one that last changed the act.
    found = [m for typ, text in stand if typ == 'Stand' for m in REF.finditer(text)]
    return squash(found[-1].group('ref')) if found else None


MWV = r'mWv\.?\s*(\d{1,2})\.(\d{1,2})\.(\d{4})'


def in_force_from_notes(ref: str, notes: list[str], observed: str) -> str | None:
    """The day the law named `ref` took effect, from the act's own footnotes ("IdF d. Art. 1 G v. 15.10.2026 I Nr. 307
    mWv 22.10.2026"): the latest such date on or before the day the change was observed."""
    core = r'\s+'.join(re.escape(w) for w in ref.split())
    days = []
    for note in notes:
        for m in re.finditer(core + r'[^;()]{0,60}?' + MWV, note):
            d = f'{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}'
            if d <= observed:
                days.append(d)
    return max(days) if days else None


def law_author(ref: str) -> tuple[str, str]:
    """A git author for a law reference: the reference as the name, and an address that cannot exist."""
    m = re.search(r'v\.\s*(\d{1,2})\.(\d{1,2})\.(\d{4})', ref)
    day = f'{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}' if m else 'undatiert'
    kind = re.match(r'([A-ZÄÖÜ][\w-]*)', ref)
    site = re.search(r'\b(I{1,3})\s+(?:(S\.|Nr\.)\s*)?([\w/]+)\s*$', ref)
    tail = f"-bgbl{len(site.group(1) or 'I')}-{'nr' if site.group(2) == 'Nr.' else 's'}{site.group(3)}" if site else ''
    local = re.sub(r'[^a-z0-9-]+', '-', f"{(kind.group(1) if kind else 'law').lower()}-{day}{tail}".replace('/', '-')).strip('-')
    name = ref if ref.startswith(('G ', 'V ', 'VO ')) or not kind else ref
    return f'{name}', f'{local}@bgbl.invalid'

# ---------------------------------------------------------------- reading the archive

def scrapes(archive: Path):
    """Yield (commit, iso time, [(status, new blob, path)]) for each scrape on the data branch, oldest first."""
    log = subprocess.run(['git', '--git-dir', str(archive), 'log', 'data', '--reverse', '--raw', '--no-abbrev', '--no-renames',
                          '--format=@%H %aI %s', '--', 'data/items'], capture_output=True, text=True, encoding='utf-8').stdout
    cur = None
    for line in log.splitlines():
        if line.startswith('@'):
            if cur and cur[2]:
                yield cur
            h, date, subject = (line[1:].split(' ', 2) + [''])[:3]
            m = re.search(r'scrape (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', subject)
            cur = (h, m.group(1) if m else date[:19], [])
        elif line.startswith(':') and cur is not None:
            info, path = line.split('\t', 1)
            parts = info.split()
            if path.endswith('.xml'):
                cur[2].append((parts[4], parts[3], path))
    if cur and cur[2]:
        yield cur


class Blobs:
    def __init__(self, archive: Path):
        self.p = subprocess.Popen(['git', '--git-dir', str(archive), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, sha: str) -> bytes:
        self.p.stdin.write(sha.encode() + b'\n')
        self.p.stdin.flush()
        header = self.p.stdout.readline().split()
        size = int(header[2])
        data = self.p.stdout.read(size)
        self.p.stdout.read(1)
        return data

# ---------------------------------------------------------------- writing the history

def path_of(slug: str) -> str:
    first = slug[0] if slug[0].isalpha() else '0'
    return f'gesetze/{first}/{slug}.md'


# Bump when the conversion to Markdown changes, so cached conversions are not reused.
CONVERT_VERSION = 5
MISSING_DAYS = 14   # an act counts as removed once it has been missing this many days


def cache_path(cache: Path, blob: str) -> Path:
    return cache / f'v{CONVERT_VERSION}' / blob[:2] / f'{blob}.json.gz'


def convert(data: bytes) -> dict:
    act = act_from_xml(data)
    act['hash'] = hashlib.sha256(act['markdown'].encode('utf-8')).hexdigest()
    return act


def cached(cache: Path | None, blob: str, blobs: 'Blobs') -> dict:
    """An act's conversion, from the disk cache when another run (or a worker) already made it."""
    import gzip
    if cache:
        f = cache_path(cache, blob)
        if f.exists():
            return json.loads(gzip.decompress(f.read_bytes()))
    act = convert(blobs.get(blob))
    if cache:
        f = cache_path(cache, blob)
        f.parent.mkdir(parents=True, exist_ok=True)
        tmp = f.with_suffix('.tmp')
        tmp.write_bytes(gzip.compress(json.dumps(act, ensure_ascii=False).encode('utf-8'), 6))
        tmp.replace(f)
    return act


def convert_shard(archive: Path, cache: Path, shard: int, shards: int, exclude: set[str] = frozenset()) -> int:
    """Fill the cache for this worker's share of the archive's blobs (those whose hash falls in its shard)."""
    blobs = Blobs(archive)
    done = 0
    seen = set()
    for _, _, changes in scrapes(archive):
        for status, blob, path in changes:
            if status == 'D' or path.split('/')[2] in exclude or blob in seen or int(blob[:8], 16) % shards != shard:
                continue
            seen.add(blob)
            if not cache_path(cache, blob).exists():
                try:
                    cached(cache, blob, blobs)
                    done += 1
                except ET.ParseError:
                    pass
    return done


def iter_commits(archive: Path, state: dict, stats: dict, exclude: set[str] = frozenset(), limit: int | None = None,
                 cache: Path | None = None, after: str | None = None, until: str | None = None):
    """Yield the history's commits in order, as dicts, keeping `state` current:
    state = {'acts': {slug: {'hash', 'meta'}}, 'missing': {slug: day first missing}, 'scrape': last scrape read}.
    Only scrapes after `after` (a commit of the archive) and up to `until` are read, so a run can continue where the last
    one stopped and give the same commits as one long run. Acts named in `exclude` are left out."""
    blobs = Blobs(archive)
    acts = state.setdefault('acts', {})
    missing = state.setdefault('missing', {})
    started = after is None
    for n, (h, when, changes) in enumerate(scrapes(archive)):
        if not started:
            started = h == after
            continue
        if limit and n >= limit:
            break
        day = when[:10]
        changed: dict[str, dict] = {}
        for status, blob, path in changes:
            slug = path.split('/')[2]
            if slug in exclude:
                continue
            if status == 'D':
                # A gap in the archive or a removal: decided once it has been missing long enough.
                if slug in acts:
                    missing.setdefault(slug, day)
                continue
            missing.pop(slug, None)
            try:
                act = cached(cache, blob, blobs)
            except ET.ParseError as e:
                stats['parse_errors'] += 1
                print(f'parse error {path} at {day}: {e}', file=sys.stderr)
                continue
            old = acts.get(slug)
            if old and old['hash'] == act['hash']:
                stats['unchanged_rebuilds'] += 1
                old['meta'] = act['meta']
                continue
            changed[slug] = {'kind': 'added' if not old else 'changed', **act, 'old_files': (old or {}).get('files', [])}
        for slug, since in sorted(missing.items()):
            if (dt.date.fromisoformat(day) - dt.date.fromisoformat(since)).days >= MISSING_DAYS and slug not in changed:
                changed[slug] = {'kind': 'removed', 'meta': acts[slug]['meta'], 'since': since, 'old_files': acts[slug].get('files', [])}
        for slug, c in changed.items():
            if c['kind'] == 'removed':
                missing.pop(slug, None)
        state['scrape'] = h
        state['scrape_day'] = day
        if until and h == until:
            limit = n   # read this scrape, then stop
        if changed:
            if not acts:
                yield {'day': day, 'when': when, 'scrape': h, 'bootstrap': True, 'acts': changed}
            else:
                groups: dict[tuple[str, str], dict] = defaultdict(dict)
                for slug, c in changed.items():
                    if c['kind'] == 'removed':
                        key = 'Nicht mehr veröffentlicht'
                    else:
                        ref = amending_law(c['meta']['stand'])
                        prev = amending_law(acts[slug]['meta']['stand']) if slug in acts else None
                        key = ref if ref and (c['kind'] == 'added' or ref != prev) else ('Neu aufgenommen' if c['kind'] == 'added' else 'Textänderung ohne neue Standangabe')
                    ref = key if key not in ('Nicht mehr veröffentlicht', 'Neu aufgenommen', 'Textänderung ohne neue Standangabe') else None
                    effective = in_force_from_notes(ref, c.get('notes', []), day) if ref else None
                    groups[(key, effective or '')][slug] = c
                for key, effective in sorted(groups):
                    yield {'day': day, 'when': when, 'scrape': h, 'key': key, 'inForce': effective or None,
                           'acts': groups[(key, effective)]}
            for slug, c in changed.items():
                if c['kind'] == 'removed':
                    acts.pop(slug, None)
                else:
                    acts[slug] = {'hash': c['hash'], 'meta': c['meta'], 'files': sorted(c['files'])}
            stats['scrapes_with_changes'] += 1
        if n % 100 == 0:
            print(f'{day}: {len(acts)} acts', flush=True)
        if until and h == until:
            break


def build(archive: Path, repo: Path, docs_date: str, docs: Path, limit: int | None = None) -> dict:
    state: dict = {}
    stats: dict = defaultdict(int)
    writer = Writer(repo)                # commits go to git fast-import as they are made
    for c in iter_commits(archive, state, stats, limit=limit):
        writer.commit(c)
    writer.finish(state['acts'], docs_date, docs)
    return {'commits': writer.mark - 1, 'acts': len(state['acts']), **stats}


def message(c: dict) -> tuple[str, str]:
    acts = c['acts']
    if c.get('bootstrap'):
        subject = f"Bestand von Gesetze im Internet am {c['day']}"
        body = [f'{len(acts)} Gesetze und Verordnungen, wie Gesetze im Internet sie an diesem Tag veröffentlichte.', '']
    else:
        key = c['key']
        names = sorted({a['meta']['jurabk'] or s for s, a in acts.items()})
        subject = f"{key}: {', '.join(names[:3])}{' u. a.' if len(names) > 3 else ''}"
        if len(subject) > 72:
            subject = f'{key}: {len(names)} Vorschriften' if len(f'{key}: {len(names)} Vorschriften') <= 72 else key[:72]
        body = []
        for slug in sorted(acts):
            a = acts[slug]
            m = a['meta']
            stand = next((t for typ, t in m['stand'] if typ == 'Stand'), '')
            verb = {'added': 'neu', 'changed': 'geändert', 'removed': f"entfernt, fehlt seit {a.get('since', '')}"}[a['kind']]
            body.append(f"- {m['jurabk'] or slug} ({verb}): {m['title']}" + (f' — {stand}' if stand else ''))
        body.append('')
    author = c.get('key') if not c.get('bootstrap') else None
    # In-Kraft is the day the change took effect in the consolidated text, which Gesetze im Internet publishes as changes
    # take effect: the commit's own day, so the history stays in in-force order and only ever grows. Where the act's
    # footnotes give an earlier date (a late consolidation, or a change with retroactive effect), that is kept too.
    trailers = [f"In-Kraft: {c['day']}"]
    if c.get('inForce') and c['inForce'] != c['day']:
        trailers.append(f"In-Kraft-laut-Fussnote: {c['inForce']}")
    trailers += [f"Beobachtet: {c['when']}", f"Quelle: {SOURCE} (Archiv QuantLaw/gesetze-im-internet, Commit {c['scrape'][:12]})"]
    if author and author not in ('Nicht mehr veröffentlicht', 'Textänderung ohne neue Standangabe', 'Neu aufgenommen'):
        trailers.insert(0, f'Gesetz: {author}')
    return subject, '\n'.join(body + trailers) + '\n'


class Writer:
    """Writes the history with `git fast-import`, one commit at a time, then the documentation commit and the tags."""

    def __init__(self, repo: Path):
        if repo.exists() and any(repo.iterdir()) and not (repo / '.git').exists():
            raise SystemExit(f'{repo} is not empty and not a git repository; refusing to write into it')
        remote = None
        if (repo / '.git').exists():
            got = subprocess.run(['git', '-C', str(repo), 'remote', 'get-url', 'origin'], capture_output=True, text=True)
            remote = got.stdout.strip() or None
            subprocess.run(['git', '-C', str(repo), 'checkout', '-q', '--detach'], capture_output=True)
            subprocess.run(['git', '-C', str(repo), 'update-ref', '-d', 'refs/heads/main'], capture_output=True)
            for t in subprocess.run(['git', '-C', str(repo), 'tag', '-l'], capture_output=True, text=True).stdout.split():
                subprocess.run(['git', '-C', str(repo), 'tag', '-d', t], capture_output=True)
        else:
            repo.mkdir(parents=True, exist_ok=True)
            subprocess.run(['git', 'init', '-q', '-b', 'main', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'config', 'core.autocrlf', 'false'], check=True)
        if remote:
            subprocess.run(['git', '-C', str(repo), 'remote', 'set-url', 'origin', remote], check=True)
        self.repo = repo
        self.fi = subprocess.Popen(['git', '-C', str(repo), 'fast-import', '--quiet', '--done'], stdin=subprocess.PIPE)
        self.out = self.fi.stdin
        self.mark = 0
        self.tag_for_day: dict[str, int] = {}

    def data(self, b: bytes) -> None:
        self.out.write(f'data {len(b)}\n'.encode())
        self.out.write(b)
        self.out.write(b'\n')

    def header(self, name: str, email: str, when: str, text: str) -> None:
        self.mark += 1
        self.out.write(b'commit refs/heads/main\n')
        self.out.write(f'mark :{self.mark}\n'.encode())
        self.out.write(f'author {name} <{email}> {when}\n'.encode())
        self.out.write(f'committer {COMMITTER} {when}\n'.encode())
        self.data(text.encode('utf-8'))
        if self.mark > 1:
            self.out.write(f'from :{self.mark - 1}\n'.encode())

    def commit(self, c: dict) -> None:
        subject, body = message(c)
        if c.get('bootstrap'):
            name, email = 'Gesetze im Internet (Bestand)', 'bestand@gesetze-im-internet.invalid'
        elif c['key'] in ('Nicht mehr veröffentlicht', 'Textänderung ohne neue Standangabe', 'Neu aufgenommen'):
            name, email = c['key'], 'ohne-gesetz@bgbl.invalid'
        else:
            name, email = law_author(c['key'])
        self.header(name, email, noon(c.get('inForce') or c['day']), f'{subject}\n\n{body}')
        for slug in sorted(c['acts']):
            a = c['acts'][slug]
            if a['kind'] == 'removed':
                self.out.write(f'D {path_of(slug)}\n'.encode())
            else:
                self.out.write(f'M 100644 inline {path_of(slug)}\n'.encode())
                self.data(a['markdown'].encode('utf-8'))
        self.tag_for_day[c['day']] = self.mark

    def finish(self, state: dict, docs_date: str, docs: Path) -> None:
        # Documentation last, dated by the caller, so a rebuild gives the same commit.
        name, email = COMMITTER.split(' <')
        self.header(name, email.rstrip('>'), noon(docs_date), 'Dokumentation, Verzeichnis und Werkzeuge\n')
        for f in sorted(docs.rglob('*')):
            if f.is_file():
                self.out.write(f'M 100644 inline {f.relative_to(docs).as_posix()}\n'.encode())
                self.data(f.read_bytes())
        self.out.write(b'M 100644 inline tools/build.py\n')
        self.data(Path(__file__).read_bytes())
        index = [{'slug': k, 'path': path_of(k), 'jurabk': a['meta']['jurabk'], 'amtabk': a['meta']['amtabk'], 'title': a['meta']['title'],
                  'ausfertigung': a['meta']['ausfertigung'], 'fundstelle': a['meta']['fundstelle'],
                  'stand': [list(x) for x in a['meta']['stand']]} for k, a in sorted(state.items())]
        self.out.write(b'M 100644 inline verzeichnis.json\n')
        self.data((json.dumps(index, ensure_ascii=False, indent=1) + '\n').encode('utf-8'))
        for day, m in sorted(self.tag_for_day.items()):
            self.out.write(f'reset refs/tags/stand/{day}\nfrom :{m}\n\n'.encode())
        self.out.write(b'done\n')
        self.out.close()
        if self.fi.wait():
            raise SystemExit('git fast-import failed')
        subprocess.run(['git', '-C', str(self.repo), 'checkout', '-q', '-f', 'main'], check=True)


def main():
    # `convert` fills the conversion cache for one shard; germany-law runs several at once before building.
    if len(sys.argv) > 1 and sys.argv[1] == 'convert':
        ap = argparse.ArgumentParser()
        ap.add_argument('cmd')
        ap.add_argument('--archive', required=True)
        ap.add_argument('--cache', required=True)
        ap.add_argument('--shard', type=int, required=True)
        ap.add_argument('--shards', type=int, required=True)
        ap.add_argument('--exclude', default='')
        a = ap.parse_args()
        n = convert_shard(Path(a.archive), Path(a.cache), a.shard, a.shards, set(filter(None, a.exclude.split(','))))
        print(f'shard {a.shard}/{a.shards}: {n} converted', flush=True)
        return
    ap = argparse.ArgumentParser()
    ap.add_argument('--archive', required=True)
    ap.add_argument('--repo', required=True)
    ap.add_argument('--docs-date', required=True, help='date of the documentation commit, YYYY-MM-DD')
    ap.add_argument('--limit', type=int, help='stop after this many scrapes (for testing)')
    args = ap.parse_args()
    result = build(Path(args.archive), Path(args.repo), args.docs_date, Path(__file__).parent / 'repo', args.limit)
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
