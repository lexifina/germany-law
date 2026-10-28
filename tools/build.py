"""Builds lexifina/germany-law: German law as one git history.

    python -X utf8 scripts/germany-law/build.py --docpatch <c3e/grundgesetz-dev> --archive <QuantLaw_gesetze-im-internet.git>
                                                --repo <out> --docs-date YYYY-MM-DD

Two parts, interleaved by date into one history:

- bund/gg/      the Grundgesetz, every version since 1949, one file per article
                (built by grundgesetz.py: DocPatch reconciled with the official text, then the official text)
- bund/gesetze/ every other federal act on Gesetze im Internet, every change since 10 June 2019, one file per act
                (built by bundesrecht.py from QuantLaw's daily archive)

State law (laender/) is to follow. Each commit is one law taking effect, credited to that law; the documentation commit
comes last, dated --docs-date, so the same sources give the same commits.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMMITTER = 'Lexifina <germany-law@lexifina.com>'
GG_DIR = 'grundgesetz'
READER = 'https://lexifina.com/watch/grundgesetz/gesetze'


def load(name: str, *candidates: Path):
    for path in candidates:
        if path.exists():
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module, path
    raise SystemExit(f'cannot find {name}: {candidates}')


# In the repository the three scripts sit side by side in tools/; in Lexifina's own repository they are in
# scripts/grundgesetz/ and scripts/bundesrecht/.
gg, GG_FILE = load('grundgesetz', HERE / 'grundgesetz.py', HERE.parent / 'grundgesetz' / 'build.py')
br, BR_FILE = load('bundesrecht', HERE / 'bundesrecht.py', HERE.parent / 'bundesrecht' / 'build.py')


def noon(day: str, seq: int) -> str:
    """Noon in Berlin on the day. Git cannot store a time before 1970 (UTC): earlier days are 1 January 1970 UTC, a
    second apart in order, with the real date in the message and the tags."""
    d = dt.date.fromisoformat(day)
    off = gg.berlin_offset(d)
    stamp = int(dt.datetime(d.year, d.month, d.day, 12, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())
    return f'{seq + 1} +0000' if stamp <= seq else f'{stamp} +0{off}00'


def gg_commits(laws: list[dict], articles: dict) -> list[dict]:
    """The Grundgesetz as commits: one per law and day in force, in order."""
    events: dict[tuple[str, int], list[tuple[str, dict]]] = {}
    for key, a in articles.items():
        for v in a['versions']:
            events.setdefault((v['inForce'], v['nr']), []).append((key, v))
    parts_of = defaultdict(int)
    for (_, nr) in events:
        parts_of[nr] += 1
    seen = defaultdict(int)
    out = []
    for day, nr in sorted(events):
        law = laws[nr]
        seen[nr] += 1
        part = f'Teil {seen[nr]} von {parts_of[nr]}' if parts_of[nr] > 1 else None
        keys = sorted(((k, v['kind']) for k, v in events[(day, nr)]), key=lambda x: gg.unit_order(x[0]))
        ops = {}
        for k, v in events[(day, nr)]:
            path = f'{GG_DIR}/artikel/{gg.file_name(k)}'
            ops[path] = None if v['repealed'] else gg.article_md(k, v['paras']).encode('utf-8')
        out.append({
            'day': day, 'name': law['short'], 'email': f'grundgesetz-{nr}@bgbl.invalid',
            'message': gg.message(law, keys, day, part) + f'Reader: {READER}/{nr}\n', 'ops': ops,
            'tags': [f'in-kraft/{day}'] + ([f'gg/{nr:02d}'] if seen[nr] == parts_of[nr] else []),
        })
    return out


def federal_commit(c: dict) -> dict:
    subject, body = br.message(c)
    if c.get('bootstrap'):
        name, email = 'Gesetze im Internet (Bestand)', 'bestand@gesetze-im-internet.invalid'
    elif c['key'] in ('Nicht mehr veröffentlicht', 'Textänderung ohne neue Standangabe', 'Neu aufgenommen'):
        name, email = c['key'], 'ohne-gesetz@bgbl.invalid'
    else:
        name, email = br.law_author(c['key'])
    ops = {}
    for slug, a in c['acts'].items():
        # Each act is a folder: one file per norm and index.md. Norms that went away are deleted.
        new = {} if a['kind'] == 'removed' else a['files']
        for file in a.get('old_files', []):
            if file not in new:
                ops[f'{slug}/{file}'] = None
        for file, text in new.items():
            ops[f'{slug}/{file}'] = text.encode('utf-8')
    return {'day': c['day'], 'name': name, 'email': email,
            'message': f'{subject}\n\n{body}', 'ops': ops, 'tags': []}


class Writer:
    def __init__(self, repo: Path, append_from: str | None = None):
        self.repo = repo
        self.mark = 0
        self.tags: dict[str, int] = {}
        self.parent = append_from        # the commit the first new commit follows, when appending
        self.written: dict[str, bytes] = {}   # path -> digest of the text last written there, so unchanged norms are skipped
        self.checkout = False
        if append_from:
            self.fi = subprocess.Popen(['git', '-C', str(repo), 'fast-import', '--quiet', '--done', '--force'],
                                       stdin=subprocess.PIPE, bufsize=1 << 20)
            self.out = self.fi.stdin
            return
        earlier = (repo / '.git').exists() and subprocess.run(['git', '-C', str(repo), 'cat-file', '-e', 'HEAD:REPRODUCE.md'],
                                                               capture_output=True).returncode == 0
        if repo.exists() and any(repo.iterdir()) and not earlier:
            raise SystemExit(f'{repo} is not empty and is not an earlier build of this repository; refusing to write into it')
        remote = None
        if (repo / '.git').exists():
            got = subprocess.run(['git', '-C', str(repo), 'remote', 'get-url', 'origin'], capture_output=True, text=True)
            remote = got.stdout.strip() or None
            # git's object files are read-only on Windows, so clear the flag before deleting.
            def force(func, path, _):
                os.chmod(path, stat.S_IWRITE)
                func(path)
            shutil.rmtree(repo / '.git', onerror=force)
            for f in repo.iterdir():
                shutil.rmtree(f, onerror=force) if f.is_dir() else f.unlink()
        repo.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'init', '-q', '-b', 'main', str(repo)], check=True)
        subprocess.run(['git', '-C', str(repo), 'config', 'core.autocrlf', 'false'], check=True)
        if remote:
            subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', remote], check=True)
        self.fi = subprocess.Popen(['git', '-C', str(repo), 'fast-import', '--quiet', '--done'], stdin=subprocess.PIPE, bufsize=1 << 20)
        self.out = self.fi.stdin

    def data(self, b: bytes) -> None:
        self.out.write(f'data {len(b)}\n'.encode())
        self.out.write(b)
        self.out.write(b'\n')

    def commit(self, c: dict) -> None:
        self.mark += 1
        when = noon(c['day'], self.mark)
        self.out.write(b'commit refs/heads/main\n')
        self.out.write(f'mark :{self.mark}\n'.encode())
        self.out.write(f"author {c['name']} <{c['email']}> {when}\n".encode())
        self.out.write(f'committer {COMMITTER} {when}\n'.encode())
        self.data(c['message'].encode('utf-8'))
        if self.mark > 1:
            self.out.write(f'from :{self.mark - 1}\n'.encode())
        elif self.parent:
            self.out.write(f'from {self.parent}\n'.encode())
        for path in sorted(c['ops']):
            body = c['ops'][path]
            if body is None:
                self.written.pop(path, None)
                self.out.write(f'D {path}\n'.encode())
            else:
                # An act's commit carries all its norms; only those whose text changed need to go to git.
                digest = hashlib.sha1(body).digest()
                if self.written.get(path) == digest:
                    continue
                self.written[path] = digest
                self.out.write(f'M 100644 inline {path}\n'.encode())
                self.data(body)
        for t in c['tags']:
            self.tags[t] = self.mark

    def docs(self, files: dict[str, bytes], day: str) -> None:
        self.commit({'day': day, 'name': 'Lexifina', 'email': 'germany-law@lexifina.com',
                     'message': 'Dokumentation, Verzeichnisse und Werkzeuge\n', 'ops': files, 'tags': []})

    def finish(self) -> str:
        for t, m in sorted(self.tags.items()):
            self.out.write(f'reset refs/tags/{t}\nfrom :{m}\n\n'.encode())
        self.out.write(b'done\n')
        self.out.close()
        if self.fi.wait():
            raise SystemExit('git fast-import failed')
        if self.checkout:
            subprocess.run(['git', '-C', str(self.repo), 'config', 'core.bare', 'false'], check=True)
            subprocess.run(['git', '-C', str(self.repo), 'checkout', '-q', '-f', 'main'], check=True)
        else:
            # Writing 100,000 files to disk takes minutes on Windows, and nothing here needs them: pushing, check_order and
            # stand_am all read git's objects. The build is left without a working tree (core.bare) so it does not show
            # as changed; --checkout writes the files.
            subprocess.run(['git', '-C', str(self.repo), 'config', 'core.bare', 'true'], check=True)
        return subprocess.run(['git', '-C', str(self.repo), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()


def convert_in_parallel(archive: Path, cache: Path, workers: int) -> None:
    """Fill the conversion cache with several processes, each converting its share of the archive's blobs."""
    procs = [subprocess.Popen([sys.executable, '-X', 'utf8', str(BR_FILE), 'convert', '--archive', str(archive), '--cache', str(cache),
                               '--shard', str(i), '--shards', str(workers), '--exclude', 'gg'])
             for i in range(workers)]
    if any(p.wait() for p in procs):
        raise SystemExit('a conversion worker failed')


def read_stand(repo: Path) -> dict | None:
    """The state an earlier build left at HEAD (stand.json), or None."""
    got = subprocess.run(['git', '-C', str(repo), 'show', 'HEAD:stand.json'], capture_output=True)
    return json.loads(got.stdout) if got.returncode == 0 else None


def docs_files(state: dict, gg_part: dict, counts: dict, run: dict, runs: list[dict]) -> dict[str, bytes]:
    """The documentation commit's files: tables, tools, the act index and the state the next run continues from."""
    laws, articles, sections, pending, fixes, sources = (gg_part[k] for k in ('laws', 'articles', 'sections', 'pending', 'fixes', 'sources'))
    tmp = Path(tempfile.mkdtemp(prefix='germany-law-'))
    (tmp / GG_DIR / 'artikel').mkdir(parents=True)
    gg.write_repo_tables(tmp / GG_DIR, laws, articles, sections)
    files: dict[str, bytes] = {}
    for f in sorted(tmp.rglob('*')):
        if f.is_file():
            files[f.relative_to(tmp).as_posix()] = f.read_bytes()
    shutil.rmtree(tmp, ignore_errors=True)
    for f in sorted((HERE / 'repo').rglob('*')):
        if f.is_file():
            files[f.relative_to(HERE / 'repo').as_posix()] = f.read_bytes()
    files['tools/build.py'] = Path(__file__).read_bytes()
    files['tools/grundgesetz.py'] = GG_FILE.read_bytes()
    files['tools/bundesrecht.py'] = BR_FILE.read_bytes()
    acts = state.get('acts', {})
    index = [{'slug': k, 'path': f'{k}/index.md', 'jurabk': a['meta']['jurabk'], 'amtabk': a['meta']['amtabk'],
              'title': a['meta']['title'], 'ausfertigung': a['meta']['ausfertigung'], 'fundstelle': a['meta']['fundstelle'],
              'stand': [list(x) for x in a['meta']['stand']]} for k, a in sorted(acts.items())]
    files['verzeichnis.json'] = (json.dumps(index, ensure_ascii=False, indent=1) + '\n').encode('utf-8')
    # Everything the next run needs to continue exactly as one long run would, and the runs so far, so a rebuild
    # (--replay) puts the documentation commits in the same places.
    stand = {'archive': 'https://github.com/QuantLaw/gesetze-im-internet', 'scrape': state.get('scrape'), 'scrape_day': state.get('scrape_day'),
             'last_observed': counts['last_observed'], 'acts': acts, 'missing': state.get('missing', {}),
             'gg_commits': counts['gg_written'], 'gg_messages': [c['message'] for c in pending[:counts['gg_written']]],
             'law_commits': counts['law'], 'federal_commits': counts['federal'], 'runs': runs}
    files['corpus.json'] = (json.dumps({
        'corpus': 'de/bund/acts', 'name': 'germany-law', 'label': 'Germany', 'language': 'de',
        'history_from': '1949-05-24', 'record_to': state.get('scrape_day') or run['until'][:10],
        'record_note': 'Grundgesetz from 1949 (DocPatch reconciled with the official text, then Gesetze im Internet); '
                       'all other federal law from 10 June 2019 (Gesetze im Internet via QuantLaw\'s daily archive). '
                       'Checked against Gesetze im Internet on the record_to day.',
        'in_force_trailer': 'In-Kraft', 'baseline_trailer': 'Beobachtet', 'correction_trailer': 'In-Kraft-laut-Fussnote',
        'has_future_branch': False,
        'dates': {
            'commit': 'in-force',
            'other_trailers': ['Beschlossen', 'Ausgefertigt', 'Verkuendet', 'In-Kraft-laut-Fussnote', 'Beobachtet'],
            'time': '12:00 Europe/Berlin',
            'before_1970': 'git cannot store dates before 1970: those commits are dated 1970-01-01T00:00:00Z, one second '
                           'apart in order; the real date is in the In-Kraft trailer and the in-kraft/YYYY-MM-DD tag',
            'federal_in_force': 'for federal acts other than the Grundgesetz, the day Gesetze im Internet published the change; '
                                'In-Kraft-laut-Fussnote gives the date the footnotes state where it differs',
        },
        'modifies': {'trailer': None, 'kinds': [],
                     'note': 'no record yet of law that changes in effect while its words stay the same'},
        'changes': {
            'kinds': {'changed': 'the text of an act changed', 'added': 'an act first published (Neu aufgenommen, or under its amending law)',
                      'removed': 'an act no longer published for 14 days (Nicht mehr veröffentlicht)'},
            'note': 'One commit per amending law per in-force day, across every act it changed; the author is the law.',
        },
        'scope': {
            'trailer': None,
            'groups': None,
            'conditions': None,
            'when_absent': 'no scope note is recorded in this history (no Applies lines yet); not a statement that a change reaches every case',
            'default_reach': {
                'rule': 'Rückwirkungsverbot (prohibition of retroactivity)',
                'meaning': 'a law may not attach new burdens to facts already completed before its promulgation (true retroactivity, '
                           'echte Rückwirkung), save narrow exceptions; it may in principle reach facts that began earlier and are still '
                           'ongoing (false retroactivity, unechte Rückwirkung), subject to proportionality and legitimate expectations; '
                           'criminal law is never retroactive (Art. 103(2) GG)',
                'authority': 'Rechtsstaatsprinzip, Art. 20(3) GG, as applied by the Bundesverfassungsgericht (e.g. BVerfGE 135, 1); Art. 103(2) GG',
                'decided_here': False,
            },
        },
        'citation': {'file': '(grundgesetz/artikel)/0*([0-9]+[a-z]?)\\.md', 'cites': '(Artikel|Art\\.) ?{n}([^0-9a-z]|$)'},
        'tool': 'python tools/stand_am.py DATE [ARTICLE ...] | python tools/stand_am.py DATE --gesetz <act>',
    }, ensure_ascii=False, indent=1) + '\n').encode('utf-8')
    files['stand.json'] = (json.dumps(stand, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8')
    numbers = {
        'DOCPATCH_COMMIT': sources['docpatch'], 'ARCHIVE_COMMIT': state.get('scrape') or run['until'],
        'GG_COMMITS': str(len(pending)), 'FEDERAL_COMMITS': str(counts['federal']), 'LAW_COMMITS': str(counts['law']),
        'ACTS': str(len(acts)), 'RECONCILED': str(len(fixes)), 'DOCS_DATE': run['docs_date'],
        'RUNS': ', '.join(f"{r['docs_date']} (archive `{r['until'][:10]}`)" for r in runs),
        'BUILD_BLOB': blob_id(files['tools/build.py']), 'GG_BLOB': blob_id(files['tools/grundgesetz.py']),
        'BR_BLOB': blob_id(files['tools/bundesrecht.py']),
        'GESETZE_JSON_SHA': hashlib.sha256(files[f'{GG_DIR}/gesetze.json']).hexdigest(),
        'VERZEICHNIS_SHA': hashlib.sha256(files['verzeichnis.json']).hexdigest(),
    }
    for name in ('README.md', 'REPRODUCE.md'):
        if name in files:
            text = files[name].decode('utf-8')
            for k, v in numbers.items():
                text = text.replace('{{' + k + '}}', v)
            files[name] = text.encode('utf-8')
    return files


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--docpatch', default=str(ROOT.parent / 'gg-dev'), help='a clone of c3e/grundgesetz-dev')
    ap.add_argument('--archive', default=str(ROOT.parent / 'german-law-sources' / '03-git' / 'QuantLaw_gesetze-im-internet.git'),
                    help="a clone of QuantLaw/gesetze-im-internet with its 'data' branch")
    ap.add_argument('--until', help='the last archive commit to read (default: the tip of its data branch)')
    ap.add_argument('--repo', default=str(ROOT.parent / 'germany-law'))
    ap.add_argument('--site', default=str(ROOT / 'saas-webpage'), help='where the Grundgesetz reader data goes')
    ap.add_argument('--cache', default=str(ROOT.parent / 'german-law-sources' / 'cache' / 'gii-markdown'),
                    help='conversions of archive blobs, reused across runs')
    ap.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2) - 2), help='processes that convert XML in parallel')
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--append', action='store_true', help='add the archive\'s new scrapes on top of HEAD (no rewrite)')
    mode.add_argument('--replay', help='rebuild from scratch, ending a run (with its documentation commit) wherever this '
                                       'stand.json (from an earlier build) says, then add this run')
    ap.add_argument('--docs-date', required=True)
    ap.add_argument('--limit', type=int, help='stop the federal part after this many scrapes (testing)')
    ap.add_argument('--checkout', action='store_true', help='also write the files of main to disk (slow; not needed to push)')
    args = ap.parse_args()
    archive, repo, cache = Path(args.archive), Path(args.repo), Path(args.cache)
    until = args.until or subprocess.run(['git', '--git-dir', str(archive), 'rev-parse', 'data'], capture_output=True, text=True).stdout.strip()

    # The Grundgesetz (seconds): always computed whole; an append writes only the commits not yet in the history.
    revs, steps, fixes, publisher, sources = gg.assemble(Path(args.docpatch), archive)
    gg.TEXT_CORRECTIONS.extend(gg.reconciliation_notes(fixes, revs))
    gg.TEXT_CORRECTIONS.extend(gg.publisher_notes(publisher, revs))
    laws, articles, _ = gg.build_record(revs, steps)
    sections = gg.sections_of(articles)
    gg.write_site(Path(args.site), laws, articles, sections, sources, args.docs_date)
    pending = gg_commits(laws, articles)
    gg_part = {'laws': laws, 'articles': articles, 'sections': sections, 'pending': pending, 'fixes': fixes, 'sources': sources}
    print(f'Grundgesetz: {len(pending)} commits, {len(fixes)} articles reconciled', flush=True)

    # Federal law: convert in parallel into the cache first, then read the cache in order.
    if args.workers > 1:
        convert_in_parallel(archive, cache, args.workers)

    this_run = {'until': until, 'docs_date': args.docs_date}
    stats: dict = defaultdict(int)
    if args.append:
        previous = read_stand(repo)
        if not previous:
            raise SystemExit('nothing to append to: HEAD has no stand.json; run a full build first')
        if previous['scrape'] == until:
            raise SystemExit('nothing new in the archive since the last run')
        gg_written = previous['gg_commits']
        if [c['message'] for c in pending[:gg_written]] != previous['gg_messages']:
            raise SystemExit('the Grundgesetz record changed before its last written commit: a rebuild is needed (tell gitlaw-global)')
        state = {'acts': previous['acts'], 'missing': previous['missing'], 'scrape': previous['scrape'], 'scrape_day': previous['scrape_day']}
        counts = {'gg_written': gg_written, 'law': previous['law_commits'], 'federal': previous['federal_commits'],
                  'last_observed': previous['last_observed']}
        done_runs, todo = previous['runs'], [this_run]
        head = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
        writer = Writer(repo, append_from=head)        # on top of the last documentation commit: nothing is replaced
    else:
        earlier = json.loads(Path(args.replay).read_text(encoding='utf-8'))['runs'] if args.replay else []
        state, counts = {}, {'gg_written': 0, 'law': 0, 'federal': 0, 'last_observed': None}
        done_runs, todo = [], [r for r in earlier if r['until'] != until] + [this_run]
        writer = Writer(repo)
    writer.checkout = args.checkout

    for run in todo:
        for c in br.iter_commits(archive, state, stats, exclude={'gg'}, limit=args.limit, cache=cache,
                                 after=state.get('scrape'), until=run['until']):
            while counts['gg_written'] < len(pending) and pending[counts['gg_written']]['day'] <= c['day']:
                writer.commit(pending[counts['gg_written']])
                counts['gg_written'] += 1
                counts['law'] += 1
            if counts['last_observed'] and counts['last_observed'] != c['day'] and writer.mark:
                writer.tags[f"stand/{counts['last_observed']}"] = writer.mark
            writer.commit(federal_commit(c))
            counts['last_observed'] = c['day']
            counts['federal'] += 1
            counts['law'] += 1
        if counts['last_observed'] and writer.mark:
            writer.tags[f"stand/{counts['last_observed']}"] = writer.mark
        # Grundgesetz commits up to the last day read, so the next run continues in the same order.
        read_to = state.get('scrape_day') or ''
        while counts['gg_written'] < len(pending) and pending[counts['gg_written']]['day'] <= read_to:
            writer.commit(pending[counts['gg_written']])
            counts['gg_written'] += 1
            counts['law'] += 1
        if run['docs_date'] < (state.get('scrape_day') or ''):
            raise SystemExit(f"--docs-date {run['docs_date']} is before the last day read ({state['scrape_day']}): dates would run backwards")
        done_runs = done_runs + [run]
        writer.docs(docs_files(state, gg_part, counts, run, done_runs), run['docs_date'])
        print(f"run to {run['until'][:10]} ({run['docs_date']}): {counts['law']} law commits so far", flush=True)
    head = writer.finish()
    print(json.dumps({'head': head, 'appended': bool(args.append), 'runs': len(done_runs), 'law_commits': counts['law'],
                      'federal_commits': counts['federal'], 'acts': len(state.get('acts', {})), **stats}, indent=1))


if __name__ == '__main__':
    main()
