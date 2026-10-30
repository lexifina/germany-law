"""Independent letters-and-digits check of every version against its raw Transparenzportal page (regex only).

    python -X utf8 check_letters.py [part.json ...]

Private. The document text (from the first "jgwsAiZDoc" block to "DocInhaltEnde", the Stand table removed), reduced to
letters and digits, must equal the version's files (000-titel, which repeats the page title, left out) placed one
after another in source order.
"""
import hashlib, html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ld(s):
    return ''.join(ch for ch in s if ch.isalnum())


def source(raw):
    i = raw.index('<div class="jgwsAiZDoc"')
    s = raw[i:raw.index('<a name="DocInhaltEnde"', i)]
    first_end = s.find('<div class="jgwsAiZDoc" id=', 10)
    if 'class="standangaben"' in s[:first_end]:  # the frame block: Stand line and its notes, not law text
        s = s[first_end:]
    return ld(html.unescape(re.sub(r'<[^>]+>', ' ', s)).replace('­', ''))


def main(paths):
    bad = total = 0
    files = {}
    for f in (HERE / '.cache' / 'url').glob('*.html'):
        files[hashlib.sha256(f.read_bytes()).hexdigest()] = f
    for p in paths:
        for a in json.load(open(p, encoding='utf-8'))['acts']:
            for v in a['versions']:
                src = source(files[v['sha256']].read_text(encoding='utf-8', errors='replace'))
                rest = {}
                for k, u in v['units'].items():
                    if k == '000-titel':
                        continue
                    t = u['text']
                    # A heading the page shows only in its table of contents (Eingangsformel) is the label, not text.
                    head = f'# {u["label"]}\n'
                    if head in t and not re.match(r'^(Artikel|Art\.|§)', u['label']):
                        t = t.replace(head, '', 1)
                    rest[k] = ld(t)
                pos = 0
                while rest:
                    hit = max((k for k, t in rest.items() if src.startswith(t, pos)), key=lambda k: len(rest[k]), default=None)
                    if hit is None:
                        break
                    pos += len(rest.pop(hit))
                total += 1
                if rest or pos != len(src):
                    bad += 1
                    print(f'MISMATCH {a["slug"]} {v["from"]}: {pos}/{len(src)}; next {src[pos:pos+70]!r}; unplaced {list(rest)[:4]}; url={v["source_url"]}')
    print(f'{total} versions checked, {bad} mismatches')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or sorted(str(p) for p in (HERE / 'corpus.d').glob('*.json'))) else 0)
