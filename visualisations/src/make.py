"""Rebuild visualisations/deutsches-recht-in-20-grafiken.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF] [--skip-extract] [--no-fetch]

The repository is very large (millions of files and commits), so nothing here walks the whole history or the whole
tree. Everything is read from git objects, in a partial clone, and only the objects the charts use are fetched, in
batches (never one at a time, and never by a lazy fetch: GIT_NO_LAZY_FETCH=1):

  1. history: only the 3,305 commits of the federal-law build of 28 October 2026 (tag global-law/pinned-20261028-*,
     fetched without trees if missing) and the tag gg/00 (the Grundgesetz of 1949)          -> .build/fedlog.txt
  2. trees: the tree objects on the way to the folders read below (fetched one level at a time if missing), and the
     whole subtree of each folder read in full
  3. blobs (about 22,000 files, some 160 MB):
       bundestag/vorgaenge/          every legislative procedure since the 7th Wahlperiode (DIP)
       bundestag/abstimmungen/       every roll-call vote with its result per parliamentary group
       rechtsprechung/bverfg/        the decisions of the two Senates of the Bundesverfassungsgericht (tenor only kept)
       bund/bgbl/teil-1/2019-2023    the heads of the Bundesgesetzblatt entries (titles of amending ordinances)
       verzeichnis.json, kommunen/gemeindeverzeichnis.csv, grundgesetz/, historisch/verfassungen/
                                                                                         -> .build/*.jsonl, *.json, *.csv
  4. prep.py turns those into .build/data.json; build.py fills page.tpl.html with it.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--skip-extract', action='store_true', help='reuse .build/ from a previous run (prep and build only)')
ap.add_argument('--no-fetch', action='store_true', help='never download missing objects (fail instead)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
os.makedirs(B, exist_ok=True)
NOLAZY = dict(os.environ, GIT_NO_LAZY_FETCH='1')   # nothing is fetched behind our back
GIT = ['git', '-C', a.repo, '-c', 'core.quotepath=off']
PINNED = 'refs/tags/global-law/pinned-20261028-6f3913a35a'   # the end of the federal-law build of 28 October 2026
GG0 = 'refs/tags/gg/00'                                        # the Grundgesetz as promulgated on 23 May 1949


def git(*args, inp=None, ok=False):
    r = subprocess.run([*GIT, *args], input=inp, capture_output=True, env=NOLAZY)
    if r.returncode and not ok:
        sys.exit('git ' + ' '.join(args[:4]) + ': ' + r.stderr.decode(errors='replace'))
    return r.stdout if not ok else (r.returncode, r.stdout)


def fetch(oids, filt, what):
    """fetch these objects explicitly, in batches; an empty list fetches nothing (an empty --stdin would fetch main)"""
    oids = sorted(set(o for o in oids if o))
    if not oids:
        return
    if a.no_fetch:
        sys.exit(f'{what}: {len(oids)} objects missing and --no-fetch')
    for i in range(0, len(oids), 5000):
        part = oids[i:i + 5000]
        print(f'  fetching {len(part)} {what} ({i + len(part)} of {len(oids)}, filter {filt})', flush=True)
        r = subprocess.run([*GIT, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                            '--recurse-submodules=no', f'--filter={filt}', '--stdin'], input=''.join(o + '\n' for o in part).encode(), capture_output=True)
        if r.returncode:
            sys.exit('fetch failed: ' + r.stderr.decode(errors='replace'))


def missing(oids):
    oids = sorted(set(oids))
    if not oids:
        return []
    chk = git('cat-file', '--batch-check', inp=''.join(o + '\n' for o in oids).encode()).decode().split('\n')
    return [l.split()[0] for l in chk if l.endswith(' missing')]


def ensure_tag(ref):
    if git('rev-parse', '--verify', '-q', ref + '^{commit}', ok=True)[0] == 0:
        return
    if a.no_fetch:
        sys.exit(ref + ' missing and --no-fetch')
    print('fetching', ref, '(commits only)', flush=True)
    r = subprocess.run([*GIT, 'fetch', '-q', '--filter=tree:0', '--no-tags', 'origin', f'{ref}:{ref}'], capture_output=True)
    if r.returncode:
        sys.exit('fetch failed: ' + r.stderr.decode(errors='replace'))


def tree_entries(oid):
    """direct entries of one tree object: {name: (type, oid)}; the object is fetched alone if missing"""
    if missing([oid]):
        fetch([oid], 'tree:0', 'tree')
    out = {}
    for rec in git('ls-tree', '-z', oid).decode('utf-8').split('\0'):
        if rec:
            meta, name = rec.split('\t', 1)
            out[name] = (meta.split(' ')[1], meta.split(' ')[2])
    return out


def resolve(root, path):
    """the oid of path below the tree root, walking one tree object at a time"""
    oid = root
    for part in [p for p in path.split('/') if p]:
        ents = tree_entries(oid)
        if part not in ents:
            sys.exit(f'no {path} in the tree')
        oid = ents[part][1]
    return oid


def subtree_blobs(oid, prefix):
    """[(path, blob oid)] of a whole subtree; its trees are fetched together (no blobs) if any is missing"""
    rc, out = git('ls-tree', '-r', '-z', oid, ok=True)
    if rc:
        fetch([oid], 'blob:none', 'subtree')
        out = git('ls-tree', '-r', '-z', oid)
    items = []
    for rec in out.decode('utf-8').split('\0'):
        if rec:
            meta, name = rec.split('\t', 1)
            if meta.split(' ')[1] == 'blob':
                items.append((prefix + '/' + name, meta.split(' ')[2]))
    return items


def read_blobs(items):
    """yield (path, bytes) for (path, oid) pairs, one blob at a time; missing blobs are fetched first, in batches"""
    fetch(missing([o for _, o in items]), 'blob:none', 'blobs')
    p = subprocess.Popen([*GIT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=NOLAZY)
    for path, oid in items:
        p.stdin.write((oid + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        if len(head) < 3 or head[1] == b'missing':
            sys.exit('cannot read ' + path)
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        yield path, data
    p.stdin.close(); p.wait()


ref = a.ref
if not ref:
    ref = 'origin/main' if git('rev-parse', '--verify', '-q', 'origin/main', ok=True)[0] == 0 else 'HEAD'
sha = git('rev-parse', ref + '^{commit}').decode().strip()
root = git('rev-parse', sha + '^{tree}').decode().strip()
info = {'ref': ref, 'head': sha, 'head_date': git('log', '-1', '--format=%cs', sha).decode().strip()}
print('ref', ref, sha, flush=True)


def jl(name, rows):
    with open(os.path.join(B, name), 'w', encoding='utf-8', newline='\n') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


if not a.skip_extract:
    # ---------------------------------------------------------------- 1. the federal-law history (commits only)
    ensure_tag(PINNED); ensure_tag(GG0)
    print('federal-law log', flush=True)
    with open(os.path.join(B, 'fedlog.txt'), 'wb') as f:
        subprocess.run([*GIT, 'log', '--no-renames', '--format=@@@%H%x09%an%x09%ae%x09%ad%n%B', '--date=short', PINNED], stdout=f, check=True, env=NOLAZY)
    info['pinned'] = git('rev-parse', PINNED + '^{commit}').decode().strip()

    # ---------------------------------------------------------------- 2./3. trees and blobs
    def one(path):
        """one blob at REF"""
        parent, name = path.rsplit('/', 1) if '/' in path else ('', path)
        ents = tree_entries(resolve(root, parent) if parent else root)
        return [(path, ents[name][1])]

    # the federal acts in force (index of Gesetze im Internet, 28 October 2026) and the municipal register
    for path, data in read_blobs(one('verzeichnis.json') + one('kommunen/gemeindeverzeichnis.csv') + one('grundgesetz/gesetze.csv')):
        open(os.path.join(B, path.replace('/', '__')), 'wb').write(data)

    # legislative procedures (DIP)
    print('bundestag/vorgaenge', flush=True)
    rows = []
    for path, data in read_blobs(subtree_blobs(resolve(root, 'bundestag/vorgaenge'), 'bundestag/vorgaenge')):
        t = data.decode('utf-8', 'replace'); lines = t.split('\n')
        r = {'path': path, 'title': lines[0][2:].strip() if lines[0].startswith('# ') else ''}
        for line in lines[1:40]:
            m = re.match(r'^- (Vorgang|Initiative|Beratungsstand|GESTA|Zustimmungsbedürftigkeit|Sachgebiet|Verkündung|Inkrafttreten): (.*)$', line)
            if m:
                r[m.group(1)] = m.group(2).strip()
        steps, cur = [], None
        for line in lines:
            m = re.match(r'^- (\d{4}-\d\d-\d\d) ([A-Za-z]+): (.*)$', line)
            if m:
                cur = [m.group(1), m.group(2), m.group(3)[:160], []]; steps.append(cur); continue
            m = re.match(r'^  - (.*)$', line)
            if m and cur is not None:
                cur[3].append(m.group(1)[:200])
        r['steps'] = steps
        rows.append(r)
    jl('vorgaenge.jsonl', rows)
    print(' ', len(rows), 'procedures', flush=True)

    # roll-call votes
    print('bundestag/abstimmungen', flush=True)
    rows = []
    for path, data in read_blobs(subtree_blobs(resolve(root, 'bundestag/abstimmungen'), 'bundestag/abstimmungen')):
        t = data.decode('utf-8', 'replace')
        g = lambda k: (re.search(r'^- ' + k + r': (.*)$', t, re.M) or [None, None])[1]
        sec = t.split('## Ergebnis nach Fraktionen und Gruppen', 1)[1].split('## ', 1)[0] if '## Ergebnis nach' in t else ''
        fr = {}
        for line in sec.split('\n'):
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(c) == 6 and c[1].isdigit():
                fr[c[0]] = list(map(int, c[1:]))
        rows.append({'path': path, 'title': t.split('\n')[0][2:], 'date': g('Datum'), 'wp': g('Wahlperiode'), 'total': g('Gesamt'), 'fr': fr})
    jl('abstimmungen.jsonl', rows)
    print(' ', len(rows), 'votes', flush=True)

    # the decisions of the Senates of the Bundesverfassungsgericht: head and tenor only
    print('rechtsprechung/bverfg (Senates)', flush=True)
    START = re.compile(r'(f\s*ü\s*r\s+R\s*e\s*c\s*h\s*t\s+e\s*r\s*k\s*a\s*n\s*n\s*t\s*:|b\s*e\s*s\s*c\s*h\s*l\s*o\s*s\s*s\s*e\s*n\s*:|entschieden\s*:)', re.S)
    END = re.compile(r'\n\s*(G\s*r\s*ü\s*n\s*d\s*e\s*:?|Gründe\s*:?|A\s*\.\s*\n|I\s*\.\s*\n)\s*\n')
    items = [it for it in subtree_blobs(resolve(root, 'rechtsprechung/bverfg/decisions'), 'rechtsprechung/bverfg/decisions')]
    n_all = len(items)
    items = [it for it in items if re.search(r'_[a-z]s\d{8}\.', it[0])]   # ECLI type letter + "s": a decision of a Senate
    rows = []
    for path, data in read_blobs(items):
        t = data.decode('utf-8', 'replace')
        head = re.search(r'^# (.*)$', t, re.M)
        fm = lambda k: (re.search(r'^' + k + r': "(.*?)"\s*$', t, re.M) or [None, None])[1]
        ten = None
        m = re.search(r'^## Tenor\s*\n(.*?)\n## ', t, re.S | re.M)
        if m:
            ten = m.group(1)
        else:
            m = START.search(t)
            if m:
                rest = t[m.end():m.end() + 30000]; e = END.search(rest)
                ten = rest[:e.start()] if e else rest[:4000]
        rows.append({'path': path, 'title': head.group(1) if head else '', 'decided': fm('decided'), 'az': fm('aktenzeichen'), 'typ': fm('typ'),
                     'tenor': re.sub(r'\s+', ' ', ten or '').strip()[:8000]})
    jl('bverfg.jsonl', rows)
    info['bverfg_all'] = n_all
    print(' ', len(rows), 'Senate decisions of', n_all, flush=True)

    # heads of the Bundesgesetzblatt Teil I entries 2019-2023 (titles of the amending ordinances)
    print('bund/bgbl/teil-1 2019-2023', flush=True)
    rows = []
    items = []
    for y in range(2019, 2024):
        items += subtree_blobs(resolve(root, f'bund/bgbl/teil-1/{y}'), f'bund/bgbl/teil-1/{y}')
    for path, data in read_blobs(items):
        t = data.decode('utf-8', 'replace')[:3000]
        title = (re.search(r'^# (.*)$', t, re.M) or [None, ''])[1]
        fs = (re.search(r'^- Fundstelle: (.*)$', t, re.M) or [None, ''])[1]
        typ = (re.search(r'^- Typ: (.*)$', t, re.M) or [None, ''])[1]
        rows.append({'path': path, 'title': title, 'fundstelle': fs, 'typ': typ})
    jl('bgbl1.jsonl', rows)
    print(' ', len(rows), 'entries', flush=True)

    # the Grundgesetz of 1949 (tag gg/00) and today, and the four earlier constitutions
    print('constitutions', flush=True)
    gg0 = git('rev-parse', GG0 + '^{tree}').decode().strip()
    texts = {}
    for key, items in [('gg1949', subtree_blobs(resolve(gg0, 'grundgesetz/artikel'), 'grundgesetz/artikel')),
                       ('gg', subtree_blobs(resolve(root, 'grundgesetz/artikel'), 'grundgesetz/artikel')),
                       ('hist', subtree_blobs(resolve(root, 'historisch/verfassungen'), 'historisch/verfassungen'))]:
        for path, data in read_blobs(items):
            texts.setdefault(key, {})[path] = data.decode('utf-8', 'replace')
    json.dump(texts, open(os.path.join(B, 'verfassungen.json'), 'w', encoding='utf-8'), ensure_ascii=False)

    json.dump(info, open(os.path.join(B, 'info.json'), 'w', encoding='utf-8'), indent=1)

print('prep', flush=True)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py')], check=True)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py')], check=True)
