"""Independent letters-and-digits check of every version against its raw REVOSax page (regex, no HTML parser).

    python -X utf8 check_letters.py [part.json ...]

Private. The text of <article id="lesetext"> without the footnote list, footnote markers and sentence numbers,
reduced to letters and digits, must equal the version's provision files placed one after another in source order.
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ld(s):
    return ''.join(ch for ch in s if ch.isalnum())


def number_items(m) -> str:
    typ = re.search(r'type="(\w)"', m.group(1))
    start = re.search(r'start="(\d+)"', m.group(1))
    n = [int(start.group(1)) if start else 1]

    def mark(_):
        x = n[0]
        n[0] += 1
        return f'<li>{chr(96 + x) if typ and typ.group(1) == "a" else x} '
    # items of a <ul> nested in the list carry no number (2026-10-30, first seen in Verordnungen)
    parts = re.split(r'(?s)(<ul[\s>].*?</ul>)', m.group(2))
    return ''.join(p if p.startswith('<ul') else re.sub(r'<li[^>]*>', mark, p) for p in parts)


def source(raw: str) -> str:
    s = raw[raw.index('id="lesetext"'):]
    s = s[s.index('>') + 1:s.index('</article>')]
    s = re.sub(r'(?s)<footer.*?</footer>', '', s)
    s = re.sub(r'(?s)<ol([^>]*)>(.*?)</ol>', number_items, s)  # the numbers the browser shows
    s = re.sub(r'(?s)<a [^>]*href="#FNID[^"]*"[^>]*>.*?</a>|<sup class="satzzahl[^"]*">.*?</sup>', '', s)
    # only real tags: a bare "<" in the text ("Klasse 3 < 10") is text, as a browser shows it
    return ld(html.unescape(re.sub(r'<[A-Za-z/!][^>]*>', ' ', s)).replace('­', ''))


def main(paths):
    bad = total = 0
    for p in paths:
        c = json.load(open(p, encoding='utf-8'))
        for a in c['acts']:
            i = a['url'].rsplit('/', 1)[1]
            for v in a['versions']:
                n = v['source_url'].rsplit('/', 1)[1]
                f = HERE / '.cache' / 'act' / i / (f'v{int(n.split(".")[1]):03d}.html' if '.' in n else 'current.html')
                src = source(f.read_text(encoding='utf-8'))
                rest = {k: ld(u['text']) for k, u in v['units'].items()}
                pos = 0
                while rest:
                    hit = max((k for k, t in rest.items() if src.startswith(t, pos)), key=lambda k: len(rest[k]), default=None)
                    if hit is None:
                        break
                    pos += len(rest.pop(hit))
                total += 1
                if rest or pos != len(src):
                    bad += 1
                    print(f'MISMATCH {a["slug"]} {v["from"]}: {pos}/{len(src)}; next {src[pos:pos+70]!r}; unplaced {list(rest)[:4]}')
    print(f'{total} versions checked, {bad} mismatches')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or sorted(str(p) for p in (HERE / 'corpus.d').glob('*.json'))) else 0)
