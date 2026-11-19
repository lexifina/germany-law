"""Compute every number of the page from the extracts in .build/ (written by make.py) into .build/data.json.

All classification rules are here. Titles are matched with word boundaries; whatever no rule recognises is counted
as "other" and shown as such.
"""
import collections, csv, datetime as dt, json, math, os, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, '.build')
INFO = json.load(open(os.path.join(B, 'info.json'), encoding='utf-8'))
D = lambda s: dt.date.fromisoformat(s)


def jl(name):
    with open(os.path.join(B, name), encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def median(xs):
    return statistics.median(xs) if xs else None


def quant(xs, q):
    if not xs:
        return None
    xs = sorted(xs); k = (len(xs) - 1) * q; f = math.floor(k); c = math.ceil(k)
    return xs[f] + (xs[c] - xs[f]) * (k - f)


OUT = {}
PROFILE = {'head': INFO['head'], 'head_date': INFO['head_date'], 'pinned': INFO.get('pinned')}

# =====================================================================================================================
# legislative procedures (DIP), 7th to 21st Wahlperiode
# =====================================================================================================================
V = list(jl('vorgaenge.jsonl'))
for r in V:
    r['wp'] = int(re.search(r'/wp(\d+)/', r['path']).group(1))
    m = re.search(r'BGBl (I|II) (\d{4}), (\d+)([a-z]?) \((\d{4}-\d\d-\d\d)\)', r.get('Verkündung', ''))
    r['vpart'], r['vyear'], r['vpage'], r['vdate'] = (m.group(1), int(m.group(2)), int(m.group(3)), m.group(5)) if m else (None, None, None, None)
    m = re.match(r'^(\d{4}-\d\d-\d\d)', r.get('Inkrafttreten', ''))
    r['ik'] = m.group(1) if m else None
    r['law'] = 'Verkündung' in r and r['vdate'] is not None
    r['first'] = min((s[0] for s in r['steps']), default=None)
    # the last plenary step of Bundestag or Bundesrat; DIP's promulgation entry is used for timing only when it falls between that
    # step and a year after it (for some treaty laws and for older records it cites a later Gazette entry)
    parl = [s[0] for s in r['steps'] if (s[1] == 'BT' and re.match(r'(2\. Beratung|3\. Beratung|Abstimmung über)', s[2])) or (s[1] == 'BR' and re.match(r'(2\. Durchgang|Durchgang|BR-Sitzung)', s[2]))]
    r['parl'] = max(parl) if parl else None
    r['vok'] = bool(r['vdate'] and r['parl'] and -3 <= (D(r['vdate']) - D(r['parl'])).days <= 365)
WPS = sorted({r['wp'] for r in V})
WPMAX = max(WPS)
LAW = [r for r in V if r['law']]
PROFILE['vorgaenge'] = len(V); PROFILE['laws'] = len(LAW)
PROFILE['wp_from'], PROFILE['wp_to'] = min(WPS), WPMAX

# the years of each Wahlperiode, from the dates of its Bundestag steps
wpyears = {}
for w in WPS:
    ds = sorted(s[0] for r in V if r['wp'] == w for s in r['steps'] if s[1] == 'BT')
    lo, hi = ds[int(len(ds) * 0.002)], ds[-1]   # ignore stray early dates of carried-over records
    wpyears[w] = [int(lo[:4]), int(hi[:4])]
OUT['wpyears'] = wpyears

LAND = ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
        'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
PARTY = [(r'CDU/CSU', 'CDU/CSU'), (r'\bSPD\b', 'SPD'), (r'\bFDP\b', 'FDP'), (r'(?i)grünen|bündnis 90', 'GRÜNE'), (r'(?i)\blinke\b|\bPDS\b', 'LINKE'), (r'\bAfD\b', 'AfD'), (r'\bBSW\b', 'BSW')]


def party(p):
    for pat, k in PARTY:
        if re.search(pat, p):
            return k
    return p.strip()


def initiators(r):
    s = (r.get('Initiative') or '-').strip()
    parts = [p.strip() for p in s.split(',') if p.strip()]
    if s == 'Bundesregierung':
        return 'breg', None
    if parts and all(p in LAND for p in parts):
        return 'br', parts
    if 'Fraktion' in s or 'Gruppe' in s:
        return 'bt', sorted({party(p) for p in parts})
    return 'other', None


for r in V:
    r['ik_kind'], r['ik_who'] = initiators(r)

# the coalition of each Wahlperiode: the groups that brought in the most bills together; a coalition that changes during
# a term shows as a second combination whose bills all come after the first one's (the 9th Wahlperiode)
coal = {}
for w in WPS:
    combos = collections.Counter()
    first, last = {}, {}
    for r in V:
        if r['wp'] == w and r['ik_kind'] == 'bt' and len(r['ik_who']) >= 2 and r['first']:
            k = tuple(r['ik_who']); combos[k] += 1
            first[k] = min(first.get(k, '9'), r['first']); last[k] = max(last.get(k, '0'), r['first'])
    top = combos.most_common()
    a = top[0][0]; spans = [[set(a), '0000-00-00']]
    for k, n in top[1:]:
        if n >= 3 and len(k) == 2 and not set(k) <= set(a) and first[k] > last[a]:
            spans.append([set(k), first[k]])
            break
    coal[w] = spans


def coalition_at(w, day):
    cur = coal[w][0][0]
    for s, d in coal[w]:
        if day and day >= d:
            cur = s
    return cur


OUT['coalitions'] = {w: [[sorted(s), d] for s, d in coal[w]] for w in WPS}
for r in V:
    if r['ik_kind'] == 'bt':
        c = coalition_at(r['wp'], r['first'])
        who = set(r['ik_who'])
        r['grp'] = 'koal' if who <= c else 'opp' if not (who & c) else 'mixed'
    else:
        r['grp'] = r['ik_kind']

# ---------------------------------------------------------------- c01 who brings in bills and whose become law
GRP = ['breg', 'koal', 'opp', 'br', 'mixed', 'other']
c01 = {'rows': []}
for w in WPS:
    row = {'wp': w}
    for g in GRP:
        rs = [r for r in V if r['wp'] == w and r['grp'] == g]
        row[g] = [len(rs), sum(r['law'] for r in rs)]
    row['lapsed_breg'] = sum(1 for r in V if r['wp'] == w and r['grp'] == 'breg' and r.get('Beratungsstand') == 'Erledigt durch Ablauf der Wahlperiode')
    c01['rows'].append(row)
tot = lambda g, f=lambda r: True: [sum(1 for r in V if r['grp'] == g and f(r)), sum(1 for r in V if r['grp'] == g and r['law'] and f(r))]
c01['tot'] = {g: tot(g) for g in GRP}
c01['opp_since14'] = tot('opp', lambda r: r['wp'] >= 14)
c01['opp_laws'] = [[r['wp'], r['title'][:160], r.get('Initiative', '')] for r in V if r['grp'] == 'opp' and r['law']]
c01['done'] = {g: tot(g, lambda r: r['wp'] < WPMAX) for g in GRP}
OUT['c01'] = c01

# ---------------------------------------------------------------- c02 how long: first step to promulgation (government bills),
# final Bundestag vote to promulgation (all laws)
FINAL = re.compile(r'^(3\. Beratung|2\. Beratung und Schlussabstimmung)')


def final_vote(r):
    f = [s[0] for s in r['steps'] if s[1] == 'BT' and FINAL.match(s[2])]
    if not f:
        f = [s[0] for s in r['steps'] if s[1] == 'BT' and s[2].startswith('2. Beratung')]
    return max(f) if f else None


for r in V:
    r['fv'] = final_vote(r)
c02 = {'rows': []}
for w in WPS:
    a = [(D(r['vdate']) - D(r['first'])).days for r in LAW if r['wp'] == w and r['grp'] == 'breg' and r['first'] and r['vok']]
    b = [(D(r['vdate']) - D(r['fv'])).days for r in LAW if r['wp'] == w and r['fv'] and r['vok']]
    a = [x for x in a if x >= 0]; b = [x for x in b if x >= 0]
    c02['rows'].append({'wp': w, 'n': len(a), 'med': median(a), 'q1': quant(a, .25), 'q3': quant(a, .75), 'nb': len(b), 'medb': median(b), 'q1b': quant(b, .25), 'q3b': quant(b, .75)})
OUT['c02'] = c02

# ---------------------------------------------------------------- c03 the month of the final vote
c03 = collections.Counter()
for r in LAW:
    if r['fv']:
        c03[r['fv'][:7]] += 1
OUT['c03'] = {'ym': dict(sorted(c03.items())), 'n': sum(c03.values()), 'first': min(c03), 'last': max(c03)}

# ---------------------------------------------------------------- c04 how bills end (Wahlperioden 16 to 20, where DIP records the
# end of the term as an outcome of its own)
OUTC = [('law', None), ('rej', r'^(Abgelehnt|Einbringung abgelehnt|Zustimmung versagt|Bundesrat hat Zustimmung versagt)'),
        ('lapsed', r'^Erledigt durch Ablauf der Wahlperiode'), ('done', r'^(Für erledigt erklärt|Zurückgezogen|Zusammengeführt|Für gegenstandslos)')]


def outcome(r):
    if r['law']:
        return 'law'
    s = r.get('Beratungsstand', '')
    for k, pat in OUTC[1:]:
        if re.match(pat, s):
            return k
    return 'other'


c04 = {'rows': [], 'status_wp': {}}
for w in WPS:
    c04['status_wp'][w] = sum(1 for r in V if r['wp'] == w and r.get('Beratungsstand') == 'Erledigt durch Ablauf der Wahlperiode')
for g in ['breg', 'koal', 'opp', 'br']:
    for span, (a, b) in [('16-19', (16, 19)), ('20', (20, 20))]:
        cnt = collections.Counter(outcome(r) for r in V if r['grp'] == g and a <= r['wp'] <= b)
        c04['rows'].append({'g': g, 'span': span, **cnt})
OUT['c04'] = c04

# ---------------------------------------------------------------- c05 roll-call votes: how often two groups vote the same way
VOTES = list(jl('abstimmungen.jsonl'))
FRN = {'DIE LINKE.': 'Die Linke', 'Die Linke': 'Die Linke', 'BÜ90/GR': 'Grüne'}


def position(v):
    ja, nein, enth = v[0], v[1], v[2]
    m = max(ja, nein, enth)
    if m == 0 or [ja, nein, enth].count(m) > 1:
        return None
    return ['ja', 'nein', 'enth'][[ja, nein, enth].index(m)]


c05 = {}
for w in sorted({int(v['wp']) for v in VOTES}):
    R = [v for v in VOTES if int(v['wp']) == w]
    pos = []
    for v in R:
        p = {}
        for f, x in v['fr'].items():
            if f == 'Fraktionslos':
                continue
            p[FRN.get(f, f)] = position(x)
        pos.append(p)
    facs = sorted({f for p in pos for f in p}, key=lambda f: (-sum(1 for p in pos if f in p), f))
    m = {}
    for i, a in enumerate(facs):
        for b in facs[i + 1:]:
            n = s = 0
            for p in pos:
                if p.get(a) and p.get(b):
                    n += 1; s += p[a] == p[b]
            m[a + '|' + b] = [s, n]
    seats = {f: max((sum(v['fr'][k]) for v in R for k in v['fr'] if FRN.get(k, k) == f), default=0) for f in facs}
    c05[w] = {'n': len(R), 'from': min(v['date'] for v in R), 'to': max(v['date'] for v in R), 'facs': facs, 'm': m,
              'nf': {f: sum(1 for p in pos if p.get(f)) for f in facs}, 'seats': seats}
OUT['c05'] = c05
PROFILE['votes'] = len(VOTES)

# =====================================================================================================================
# Bund und Länder
# =====================================================================================================================
GG = {r['gesetz']: r for r in csv.DictReader(open(os.path.join(B, 'grundgesetz__gesetze.csv'), encoding='utf-8'))}
REFORM = GG['52']['in_kraft']          # the 52nd amending law to the Grundgesetz (Föderalismusreform)
OUT['reform'] = {'in_kraft': REFORM, 'titel': GG['52']['titel'], 'n': '52'}


def zust(r):
    s = r.get('Zustimmungsbedürftigkeit') or ''
    m = re.search(r'(Ja|Nein), laut Verkündung', s)
    if m:
        return m.group(1)
    m = re.match(r'^(Ja|Nein)\b', s)
    return m.group(1) if m else None


lday = lambda r: r['vdate'] if r['vok'] or not r['parl'] else r['parl']
c06 = {'rows': []}
for w in WPS:
    parts = [('', lambda r: True)] if w != 16 else [('a', lambda r: lday(r) < REFORM), ('b', lambda r: lday(r) >= REFORM)]
    for suf, f in parts:
        rs = [r for r in LAW if r['wp'] == w and f(r)]
        z = collections.Counter(zust(r) for r in rs)
        c06['rows'].append({'wp': w, 'k': f'{w}{suf}', 'ja': z['Ja'], 'nein': z['Nein'], 'na': z[None], 'from': min(lday(r) for r in rs), 'to': max(lday(r) for r in rs)})
pre = [r for r in LAW if lday(r) < REFORM]; post = [r for r in LAW if lday(r) >= REFORM]
c06['pre'] = [sum(zust(r) == 'Ja' for r in pre), sum(zust(r) in ('Ja', 'Nein') for r in pre)]
c06['post'] = [sum(zust(r) == 'Ja' for r in post), sum(zust(r) in ('Ja', 'Nein') for r in post)]
OUT['c06'] = c06

# ---------------------------------------------------------------- c07 the mediation committee and the vetoes
VA = re.compile(r'Anrufung des Vermittlungsausschusses')


def has(r, pat):
    return any(re.search(pat, s[2]) or any(re.search(pat, b) for b in s[3]) for s in r['steps'])


c07 = {'rows': []}
for w in WPS:
    laws = [r for r in LAW if r['wp'] == w]
    c07['rows'].append({'wp': w, 'laws': len(laws), 'va': sum(has(r, VA) for r in laws), 'va_all': sum(has(r, VA) for r in V if r['wp'] == w),
                        'versagt': sum(has(r, r'Zustimmungsversagung|Versagung der Zustimmung|Zustimmung versagt') for r in V if r['wp'] == w)})
vers = [r for r in V if has(r, r'Zustimmungsversagung|Versagung der Zustimmung|Zustimmung versagt')]
einsp = [r for r in V if has(r, r'Einspruch des BR|Einspruch eingelegt|Einlegung eines Einspruchs')]
c07['versagt'] = [len(vers), sum(r['law'] for r in vers)]
c07['einspruch'] = [len(einsp), sum(has(r, r'Zurückweisung des Einspruchs') for r in einsp), sum(r['law'] for r in einsp)]
c07['bpraes'] = [[r['wp'], re.sub(r'\s*\(G-SIG: \d+\)', '', r['title']), max(s[0] for s in r['steps'])] for r in V if 'Bundespräsident' in r.get('Beratungsstand', '')]
c07['bverfg'] = [[r['wp'], re.sub(r'\s*\(G-SIG: \d+\)', '', r['title']), r['Beratungsstand']] for r in V if re.search(r'nichtig|unvereinbar', r.get('Beratungsstand', ''))]
c07['va_by'] = {k: sum(has(r, 'Anrufung des Vermittlungsausschusses durch ' + p) for r in V) for k, p in [('br', 'den BR'), ('breg', 'die BRg'), ('bt', 'den BT')]}
OUT['c07'] = c07

# ---------------------------------------------------------------- c08 bills brought in by the Länder (since the 12th Wahlperiode,
# the first with all sixteen in the Bundesrat)
c08 = {l: {'n': 0, 'solo': 0, 'law': 0, 'n_all': 0} for l in LAND}
for r in V:
    if r['ik_kind'] != 'br':
        continue
    for l in set(r['ik_who']):
        c08[l]['n_all'] += 1
        if r['wp'] >= 12:
            c08[l]['n'] += 1; c08[l]['solo'] += len(r['ik_who']) == 1; c08[l]['law'] += r['law']
br12 = [r for r in V if r['ik_kind'] == 'br' and r['wp'] >= 12]
OUT['c08'] = {'l': c08, 'n': len(br12), 'law': sum(r['law'] for r in br12), 'joint': sum(len(r['ik_who']) > 1 for r in br12), 'all16': sum(len(set(r['ik_who'])) == 16 for r in br12)}

# ---------------------------------------------------------------- c09 the municipalities of each Land
G = list(csv.DictReader(open(os.path.join(B, 'kommunen__gemeindeverzeichnis.csv'), encoding='utf-8')))
LANDN = {r['ars']: r['name'] for r in G if r['ebene'] == 'Land'}
CL = [('a', 0, 500), ('b', 500, 2000), ('c', 2000, 10000), ('d', 10000, 100000), ('e', 100000, 10 ** 9)]
c09 = {}
for r in G:
    if r['ebene'] != 'Gemeinde' or 'gemeindefrei' in r['art']:
        continue
    l = LANDN[r['ars'][:2]]; p = int(r['bevoelkerung_2025'] or 0)
    x = c09.setdefault(l, {'n': 0, 'pop': 0, 'area': 0.0, 'p': [], **{k: 0 for k, _, _ in CL}})
    x['n'] += 1; x['pop'] += p; x['area'] += float(r['flaeche_km2'] or 0); x['p'].append(p)
    for k, lo, hi in CL:
        if lo <= p < hi:
            x[k] += 1
for l, x in c09.items():
    x['med'] = median(x.pop('p')); x['area'] = round(x['area'])
free = sum(1 for r in G if r['ebene'] == 'Gemeinde' and 'gemeindefrei' in r['art'])
OUT['c09'] = {'l': c09, 'free': free, 'stand': '2026-09-30'}
PROFILE['gemeinden'] = sum(x['n'] for x in c09.values())

# =====================================================================================================================
# what laws are about and when they apply
# =====================================================================================================================
TREATY = re.compile(r'^(Gesetz|Entwurf eines Gesetzes) zu (dem|den|der)\b|\bVertragsgesetz\b')
BUDGET = re.compile(r'Bundeshaushaltsplan|Haushaltsgesetz|Haushaltsbegleitgesetz|Nachtragshaushalt|Haushaltsstrukturgesetz')
EU = re.compile(r'[Rr]ichtlinie\b|[Rr]ichtlinien\b|Rahmenbeschluss|Verordnung \((EU|EG|EWG)\)|\((EU|EG|EWG)\) (Nr\. )?\d|EU-[A-ZÄÖÜ]|\bder Europäischen Union\b|\bgemeinschaftsrechtliche')
MANTEL = re.compile(r'\b(weiterer|anderer|sonstiger)\s+(Gesetze|Vorschriften|Rechtsvorschriften|Bestimmungen|Gesetzes)\b')
AMEND = re.compile(r'\b(Änderung|Änderungen|Ergänzung|ändern|Änderungsgesetz|ÄndG)\b|änderungsgesetz\b')
KINDS = ['treaty', 'budget', 'eu', 'mantel', 'amend', 'other']


def kind(t):
    t = re.sub(r'\s*\(G-SIG: \d+\)', '', t)
    if TREATY.search(t):
        return 'treaty'
    if BUDGET.search(t):
        return 'budget'
    if EU.search(t):
        return 'eu'
    if MANTEL.search(t):
        return 'mantel'
    if AMEND.search(t):
        return 'amend'
    return 'other'


for r in V:
    r['kind'] = kind(r['title'])
c10 = {'rows': []}
for w in WPS:
    k = collections.Counter(r['kind'] for r in LAW if r['wp'] == w)
    c10['rows'].append({'wp': w, **{x: k[x] for x in KINDS}})
c10['ex'] = {x: [re.sub(r'\s*\(G-SIG: \d+\)', '', r['title'])[:140] for r in LAW if r['kind'] == x][-3:] for x in KINDS}
OUT['c10'] = c10

# ---------------------------------------------------------------- c11 subject areas (DIP Sachgebiet; given from the 9th Wahlperiode)
c11 = {'n': {}, 'share': collections.defaultdict(dict), 'tot': collections.Counter()}
for w in WPS:
    rs = [r for r in LAW if r['wp'] == w and r.get('Sachgebiet', '-') not in ('-', '')]
    if len(rs) < 0.5 * sum(1 for r in LAW if r['wp'] == w):
        continue
    c11['n'][w] = len(rs)
    cnt = collections.Counter(s.strip() for r in rs for s in r['Sachgebiet'].split(';'))
    for s, n in cnt.items():
        c11['share'][s][w] = n; c11['tot'][s] += n
c11['top'] = [s for s, _ in c11['tot'].most_common(12)]
c11['share'] = {s: c11['share'][s] for s in c11['top']}
c11['tot'] = {s: c11['tot'][s] for s in c11['top']}
c11['missing'] = [w for w in WPS if w not in c11['n']]
OUT['c11'] = c11

# ---------------------------------------------------------------- c12 the other parties to the treaties approved by law
ISO = [  # pattern in the German name -> world-atlas id (ISO 3166-1 numeric), German and English short names
    (r'Österreich', '040', 'Österreich', 'Austria'), (r'Schweiz', '756', 'Schweiz', 'Switzerland'), (r'Niederlande', '528', 'Niederlande', 'Netherlands'),
    (r'Volksrepublik Polen|Republik Polen|\bPolen\b', '616', 'Polen', 'Poland'), (r'Tschechische', '203', 'Tschechien', 'Czechia'),
    (r'Französische|Frankreich', '250', 'Frankreich', 'France'), (r'Vereinigten Staaten von Amerika', '840', 'Vereinigte Staaten', 'United States'),
    (r'Luxemburg', '442', 'Luxemburg', 'Luxembourg'), (r'Israel', '376', 'Israel', 'Israel'), (r'Kanada', '124', 'Kanada', 'Canada'),
    (r'Italienische', '380', 'Italien', 'Italy'), (r'Schweden', '752', 'Schweden', 'Sweden'), (r'Finnland', '246', 'Finnland', 'Finland'),
    (r'Norwegen', '578', 'Norwegen', 'Norway'), (r'Brasilien', '076', 'Brasilien', 'Brazil'), (r'\bMalta\b', '470', 'Malta', 'Malta'),
    (r'Volksrepublik China|\bChina\b', '156', 'China', 'China'), (r'Belgien', '056', 'Belgien', 'Belgium'), (r'Indien', '356', 'Indien', 'India'),
    (r'Arabischen Emirate', '784', 'Vereinigte Arabische Emirate', 'United Arab Emirates'), (r'Marokko', '504', 'Marokko', 'Morocco'),
    (r'Philippinen', '608', 'Philippinen', 'Philippines'), (r'Dänemark', '208', 'Dänemark', 'Denmark'), (r'Mexikan', '484', 'Mexiko', 'Mexico'),
    (r'Lettland', '428', 'Lettland', 'Latvia'), (r'Vereinigten Königreich', '826', 'Vereinigtes Königreich', 'United Kingdom'),
    (r'Singapur', '702', 'Singapur', 'Singapore'), (r'Rumänien', '642', 'Rumänien', 'Romania'), (r'Tunesi', '788', 'Tunesien', 'Tunisia'),
    (r'Türkei', '792', 'Türkei', 'Türkiye'), (r'Republik Korea', '410', 'Südkorea', 'South Korea'), (r'Kuwait', '414', 'Kuwait', 'Kuwait'),
    (r'Liechtenstein', '438', 'Liechtenstein', 'Liechtenstein'), (r'Uruguay', '858', 'Uruguay', 'Uruguay'), (r'Venezuela', '862', 'Venezuela', 'Venezuela'),
    (r'Australi', '036', 'Australien', 'Australia'), (r'Bulgarien', '100', 'Bulgarien', 'Bulgaria'), (r'Ungar', '348', 'Ungarn', 'Hungary'),
    (r'Litauen', '440', 'Litauen', 'Lithuania'), (r'Slowenien', '705', 'Slowenien', 'Slovenia'), (r'Slowakische', '703', 'Slowakei', 'Slovakia'),
    (r'\bIrland\b', '372', 'Irland', 'Ireland'), (r'Südafrika', '710', 'Südafrika', 'South Africa'), (r'Jamaika', '388', 'Jamaika', 'Jamaica'),
    (r'Portugiesische|Portugal', '620', 'Portugal', 'Portugal'), (r'Zypern', '196', 'Zypern', 'Cyprus'), (r'Ägypten', '818', 'Ägypten', 'Egypt'),
    (r'Paraguay', '600', 'Paraguay', 'Paraguay'), (r'Saudi', '682', 'Saudi-Arabien', 'Saudi Arabia'), (r'Ecuador', '218', 'Ecuador', 'Ecuador'),
    (r'Indonesien', '360', 'Indonesien', 'Indonesia'), (r'Algerien', '012', 'Algerien', 'Algeria'), (r'Kenia', '404', 'Kenia', 'Kenya'),
    (r'Argentin', '032', 'Argentinien', 'Argentina'), (r'Neuseeland', '554', 'Neuseeland', 'New Zealand'), (r'Panama', '591', 'Panama', 'Panama'),
    (r'Simbabwe', '716', 'Simbabwe', 'Zimbabwe'), (r'Chile', '152', 'Chile', 'Chile'), (r'Russische', '643', 'Russland', 'Russia'),
    (r'Albanien', '008', 'Albanien', 'Albania'), (r'Namibia', '516', 'Namibia', 'Namibia'), (r'Estland', '233', 'Estland', 'Estonia'),
    (r'Ukraine', '804', 'Ukraine', 'Ukraine'), (r'Belarus|Weißrussland', '112', 'Belarus', 'Belarus'), (r'Moldau', '498', 'Moldau', 'Moldova'),
    (r'Usbekistan', '860', 'Usbekistan', 'Uzbekistan'), (r'Kroatien', '191', 'Kroatien', 'Croatia'), (r'Turkmenistan', '795', 'Turkmenistan', 'Turkmenistan'),
    (r'Mauritius', '480', 'Mauritius', 'Mauritius'), (r'Island', '352', 'Island', 'Iceland'), (r'Liberia', '430', 'Liberia', 'Liberia'),
    (r'Jordanien', '400', 'Jordanien', 'Jordan'), (r'Spanische|Spanien', '724', 'Spanien', 'Spain'), (r'Guatemala', '320', 'Guatemala', 'Guatemala'),
    (r'Malaysia', '458', 'Malaysia', 'Malaysia'), (r'Syrische', '760', 'Syrien', 'Syria'), (r'Sri Lanka', '144', 'Sri Lanka', 'Sri Lanka'),
    (r'Elfenbeinküste|Côte d', '384', 'Côte d’Ivoire', 'Côte d’Ivoire'), (r'Papua-Neuguinea', '598', 'Papua-Neuguinea', 'Papua New Guinea'),
    (r'Bangladesch', '050', 'Bangladesch', 'Bangladesh'), (r'Oman', '512', 'Oman', 'Oman'), (r'St\. Lucia', '662', 'St. Lucia', 'Saint Lucia'),
    (r'Gabun', '266', 'Gabun', 'Gabon'), (r'Bahrain', '048', 'Bahrain', 'Bahrain'), (r'Georgien', '268', 'Georgien', 'Georgia'),
    (r'Kuba', '192', 'Kuba', 'Cuba'), (r'Kasachstan', '398', 'Kasachstan', 'Kazakhstan'), (r'Thailand', '764', 'Thailand', 'Thailand'),
    (r'Pakistan', '586', 'Pakistan', 'Pakistan'), (r'Islamischen Republik Iran|\bIran\b', '364', 'Iran', 'Iran'), (r'Vietnam', '704', 'Vietnam', 'Vietnam'),
    (r'Costa Rica', '188', 'Costa Rica', 'Costa Rica'), (r'Ghana', '288', 'Ghana', 'Ghana'), (r'\bJapan\b', '392', 'Japan', 'Japan'),
    (r'Armenien', '051', 'Armenien', 'Armenia'), (r'Antigua', '028', 'Antigua und Barbuda', 'Antigua and Barbuda'), (r'Tadschikistan', '762', 'Tadschikistan', 'Tajikistan'),
    (r'Kirgis', '417', 'Kirgisistan', 'Kyrgyzstan'), (r'Angola', '024', 'Angola', 'Angola'), (r'Jemen', '887', 'Jemen', 'Yemen'),
    (r'Sambia', '894', 'Sambia', 'Zambia'), (r'Trinidad', '780', 'Trinidad und Tobago', 'Trinidad and Tobago'), (r'Haiti', '332', 'Haiti', 'Haiti'),
    (r'Griechenland|Hellenische', '300', 'Griechenland', 'Greece'), (r'Togo', '768', 'Togo', 'Togo'), (r'Aserbaidschan', '031', 'Aserbaidschan', 'Azerbaijan'),
    (r'Mongolei', '496', 'Mongolei', 'Mongolia'), (r'Nordmazedonien|Mazedonien', '807', 'Nordmazedonien', 'North Macedonia'), (r'Serbien', '688', 'Serbien', 'Serbia'),
    (r'Montenegro', '499', 'Montenegro', 'Montenegro'), (r'Bosnien', '070', 'Bosnien und Herzegowina', 'Bosnia and Herzegovina'), (r'Kosovo', '-99', 'Kosovo', 'Kosovo'),
    (r'Katar', '634', 'Katar', 'Qatar'), (r'Libanon', '422', 'Libanon', 'Lebanon'), (r'Nigeria', '566', 'Nigeria', 'Nigeria'), (r'Senegal', '686', 'Senegal', 'Senegal'),
    (r'Kamerun', '120', 'Kamerun', 'Cameroon'), (r'Bolivien', '068', 'Bolivien', 'Bolivia'), (r'Peru', '604', 'Peru', 'Peru'), (r'Kolumbien', '170', 'Kolumbien', 'Colombia'),
    (r'Honduras', '340', 'Honduras', 'Honduras'), (r'Nicaragua', '558', 'Nicaragua', 'Nicaragua'), (r'El Salvador', '222', 'El Salvador', 'El Salvador'),
    (r'Dominikanische', '214', 'Dominikanische Republik', 'Dominican Republic'), (r'Tansania', '834', 'Tansania', 'Tanzania'), (r'Uganda', '800', 'Uganda', 'Uganda'),
    (r'Äthiopien', '231', 'Äthiopien', 'Ethiopia'), (r'Sudan', '729', 'Sudan', 'Sudan'), (r'Mali', '466', 'Mali', 'Mali'), (r'Niger\b', '562', 'Niger', 'Niger'),
    (r'Burkina', '854', 'Burkina Faso', 'Burkina Faso'), (r'Benin', '204', 'Benin', 'Benin'), (r'Ruanda', '646', 'Ruanda', 'Rwanda'), (r'Burundi', '108', 'Burundi', 'Burundi'),
    (r'Kongo', '178', 'Kongo', 'Congo'), (r'Mosambik', '508', 'Mosambik', 'Mozambique'), (r'Madagaskar', '450', 'Madagaskar', 'Madagascar'),
    (r'Lesotho', '426', 'Lesotho', 'Lesotho'), (r'Botsuana|Botswana', '072', 'Botsuana', 'Botswana'), (r'Malawi', '454', 'Malawi', 'Malawi'),
    (r'Sierra Leone', '694', 'Sierra Leone', 'Sierra Leone'), (r'Guinea\b', '324', 'Guinea', 'Guinea'), (r'Mauretanien', '478', 'Mauretanien', 'Mauritania'),
    (r'Tschad', '148', 'Tschad', 'Chad'), (r'Afghanistan', '004', 'Afghanistan', 'Afghanistan'), (r'Nepal', '524', 'Nepal', 'Nepal'), (r'Laos', '418', 'Laos', 'Laos'),
    (r'Kambodscha', '116', 'Kambodscha', 'Cambodia'), (r'Myanmar|Birma', '104', 'Myanmar', 'Myanmar'), (r'Irak', '368', 'Irak', 'Iraq'), (r'Libyen', '434', 'Libyen', 'Libya'),
    (r'Barbados', '052', 'Barbados', 'Barbados'), (r'Grenada', '308', 'Grenada', 'Grenada'), (r'Dominica\b', '212', 'Dominica', 'Dominica'), (r'Belize', '084', 'Belize', 'Belize'),
    (r'Guyana', '328', 'Guyana', 'Guyana'), (r'Suriname', '740', 'Suriname', 'Suriname'), (r'Seychellen', '690', 'Seychellen', 'Seychelles'),
    (r'Fidschi', '242', 'Fidschi', 'Fiji'), (r'Brunei', '096', 'Brunei', 'Brunei'), (r'Andorra', '020', 'Andorra', 'Andorra'),
    (r'San Marino', '674', 'San Marino', 'San Marino'), (r'Monaco', '492', 'Monaco', 'Monaco'), (r'Heiligen Stuhl|Vatikan', '336', 'Heiliger Stuhl', 'Holy See'),
    (r'Kap Verde', '132', 'Kap Verde', 'Cabo Verde'), (r'Syrien', '760', 'Syrien', 'Syria'), (r'Seschellen', '690', 'Seychellen', 'Seychelles'),
    (r'Zaire', '180', 'DR Kongo (Zaire)', 'DR Congo (Zaire)'), (r'Somalia', '706', 'Somalia', 'Somalia'), (r'Dominicanischen Bund', '212', 'Dominica', 'Dominica'),
    (r'St\. Vincent', '670', 'St. Vincent und die Grenadinen', 'Saint Vincent and the Grenadines'), (r'Mongolisch', '496', 'Mongolei', 'Mongolia'), (r'Libanesisch', '422', 'Libanon', 'Lebanon'),
    (r'Macau', '446', 'Macau', 'Macao'), (r'[Mm]azedonisch', '807', 'Nordmazedonien', 'North Macedonia'), (r'Palästinensisch', '275', 'Palästinensische Gebiete', 'Palestinian territories'),
    (r'Libysch', '434', 'Libyen', 'Libya'), (r'Jersey', '832', 'Jersey', 'Jersey'), (r'Guernsey', '831', 'Guernsey', 'Guernsey'), (r'Insel Man|Isle of Man', '833', 'Isle of Man', 'Isle of Man'),
    (r'Timor', '626', 'Timor-Leste', 'Timor-Leste'), (r'Hongkong', '344', 'Hongkong', 'Hong Kong'), (r'Gibraltar', '292', 'Gibraltar', 'Gibraltar'), (r'Anguilla', '660', 'Anguilla', 'Anguilla'),
    (r'Kaimaninseln', '136', 'Kaimaninseln', 'Cayman Islands'), (r'Turks- und Caicos', '796', 'Turks- und Caicosinseln', 'Turks and Caicos Islands'), (r'Jungferninseln', '092', 'Britische Jungferninseln', 'British Virgin Islands'),
    (r'Bermuda', '060', 'Bermuda', 'Bermuda'), (r'Montserrat', '500', 'Montserrat', 'Montserrat'), (r'Cookinseln', '184', 'Cookinseln', 'Cook Islands'), (r'Kitts', '659', 'St. Kitts und Nevis', 'Saint Kitts and Nevis'), (r'Malediven', '462', 'Malediven', 'Maldives'), (r'Bahamas', '044', 'Bahamas', 'Bahamas'), (r'Äquatorialguinea', '226', 'Äquatorialguinea', 'Equatorial Guinea'), (r'Swasiland|Eswatini', '748', 'Eswatini', 'Eswatini'),
]
HIST = [(r'Deutschen Demokratischen Republik', 'DDR', 'Deutsche Demokratische Republik', 'German Democratic Republic'),
        (r'Sowjetrepubliken|Sowjetunion', 'SU', 'Sowjetunion', 'Soviet Union'), (r'Jugoslawien', 'YU', 'Jugoslawien', 'Yugoslavia'),
        (r'Tschechoslowak|Tschechischen und Slowakischen', 'CS', 'Tschechoslowakei', 'Czechoslovakia'), (r'Serbien und Montenegro', 'SCG', 'Serbien und Montenegro', 'Serbia and Montenegro')]
BI = re.compile(r'zwischen (?:der Regierung )?der Bundesrepublik Deutschland(?:,[^,]*,)? und (.{0,200})')
CUT = re.compile(r' (?:über|zur|zum|betreffend|zu|auf dem|auf den|hinsichtlich|im Bereich|bezüglich|für|vom|gegen|in Bezug|zwecks|sowie)\b')
ORG = re.compile(r'Europäische|Vereinten Nationen|Organisation|Laboratorium|Zentralbank|Schulen|Gerichtshof|Seegerichtshof|Agentur|Kommission|Institut|Bank\b|Konferenz|Gemeinschaft|Atomenergie|Zentrum|Fonds|Sekretariat|Akademie|Behörde|Universität')
EUM = re.compile(r'(Europäischen Gemeinschaft(?:en)?|Europäischen Union|Europäischen Atomgemeinschaft)[^;]*?(?:einerseits|und ihren Mitgliedstaaten)')
INLAND = re.compile(r'Zentralrat|Kirche|Evangelisch|Heiligen Stuhl|zwischen den Ländern|\bLand Berlin\b|Staatsvertrag')


def partner(t):
    """'bi' with one state, 'hist', 'org' (an international organisation), 'eu' (an EU agreement), 'inland' or 'multi'"""
    t = re.sub(r'\s+', ' ', t)
    m = BI.search(t)
    if m:
        seg = m.group(1)
        c = CUT.search(seg)
        seg = seg[:c.start()] if c else seg
        for pat, code, de, en in HIST:
            if re.search(pat, seg):
                return 'hist', code
        for pat, code, de, en in ISO:
            if re.search(pat, seg):
                return 'bi', code
        if INLAND.search(seg):
            return 'inland', None
        if ORG.search(seg) or re.search(r'Treuhandfonds|Hauptquartier', seg):
            return 'org', None
        return 'bi?', seg
    if INLAND.search(t) and not re.search(r'Republik|Königreich', t):
        return 'inland', None
    if EUM.search(t):
        return 'eu', None
    return 'multi', None


TR = [r for r in LAW if r['kind'] == 'treaty']
c12 = {'iso': collections.Counter(), 'hist': collections.Counter(), 'kind': collections.Counter(), 'unk': [], 'dec': collections.defaultdict(collections.Counter)}
for r in TR:
    k, code = partner(r['title'])
    c12['kind'][k] += 1
    c12['dec'][str(int(lday(r)[:4]) // 10 * 10)][k if k in ('bi', 'hist', 'eu', 'multi', 'inland', 'org') else 'bi'] += 1
    if k == 'bi':
        c12['iso'][code] += 1
    elif k == 'hist':
        c12['hist'][code] += 1
    elif k == 'bi?':
        c12['unk'].append(code)
NAMES = {code: [de, en] for _, code, de, en in ISO}
NAMES.update({code: [de, en] for _, code, de, en in HIST})
c12['names'] = {k: NAMES[k] for k in list(c12['iso']) + list(c12['hist'])}
c12['n'] = len(TR)
c12['iso'] = dict(c12['iso'].most_common()); c12['hist'] = dict(c12['hist']); c12['kind'] = dict(c12['kind']); c12['dec'] = {k: dict(v) for k, v in sorted(c12['dec'].items())}
OUT['c12'] = c12

# ---------------------------------------------------------------- c13/c14 the day a law takes effect (laws other than treaty laws: a treaty
# law's in-force entry often gives the treaty's own date)
NT = [r for r in LAW if r['kind'] != 'treaty' and r['ik'] and r['vok'] and r['ik'] >= '1949' and abs((D(r['ik']) - D(r['vdate'])).days) <= 3653]
OUT['nt_dropped'] = sum(1 for r in LAW if r['kind'] != 'treaty' and r['ik']) - len(NT)
OUT['nt_noik'] = sum(1 for r in LAW if r['kind'] != 'treaty' and not r['ik'])
md = collections.Counter(r['ik'][5:] for r in NT)
OUT['c13'] = {'md': dict(md), 'n': len(NT), 'first_of_month': sum(1 for r in NT if r['ik'][8:] == '01')}
LAGK = [('rb', -10 ** 6, -32), ('ra', -31, -1), ('d0', 0, 0), ('d1', 1, 1), ('d2', 2, 31), ('d3', 32, 10 ** 6)]
c14 = {'rows': []}
for w in WPS:
    cnt = collections.Counter(); jan = 0
    for r in NT:
        if r['wp'] != w:
            continue
        lag = (D(r['ik']) - D(r['vdate'])).days
        for k, lo, hi in LAGK:
            if lo <= lag <= hi:
                cnt[k] += 1
        jan += r['ik'][5:] == '01-01'
    c14['rows'].append({'wp': w, **{k: cnt[k] for k, _, _ in LAGK}, 'jan': jan})
ret = [r for r in NT if (D(r['ik']) - D(r['vdate'])).days < -31]
c14['ret_kinds'] = dict(collections.Counter(r['kind'] for r in ret))
c14['ret_budget'] = sum(1 for r in ret if r['kind'] == 'budget')
c14['ret_tax'] = sum(1 for r in ret if re.search(r'[Ss]teuer|Abgabe|Besoldung|Versorgung|Rente', r['title']))
c14['ret_n'] = len(ret)
c14['ret_long'] = sorted([[(D(r['vdate']) - D(r['ik'])).days, r['wp'], re.sub(r'\s*\(G-SIG: \d+\)', '', r['title'])[:120], r['ik'], r['vdate']] for r in ret], reverse=True)[:5]
OUT['c14'] = c14

# =====================================================================================================================
# the federal law in force (Gesetze im Internet, 28 October 2026) and its changes since 10 June 2019
# =====================================================================================================================
VZ = json.load(open(os.path.join(B, 'verzeichnis.json'), encoding='utf-8'))
commits = []
cur = None
for line in open(os.path.join(B, 'fedlog.txt'), encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('@@@'):
        h, an, ae, ad = line[3:].split('\t'); cur = {'an': an, 'acts': [], 'tr': {}}; commits.append(cur); continue
    m = re.match(r'^- (.+?) \((geändert|neu|entfernt[^)]*)\): (.*)$', line)
    if m:
        cur['acts'].append((m.group(1), m.group(2), m.group(3))); continue
    m = re.match(r'^([A-Z][A-Za-z-]+): (.*)$', line)
    if m:
        cur['tr'][m.group(1)] = m.group(2)


def ckind(an):
    if re.match(r'^G v\.', an): return 'G'
    if re.match(r'^V v\.', an): return 'V'
    if an.startswith('Textänderung'): return 'T'
    if an.startswith('Neu aufgenommen'): return 'N'
    if an.startswith('Nicht mehr'): return 'X'
    if re.match(r'^\d+\. Änderung', an) or an.startswith('Grundgesetz'): return 'GG'
    if an.startswith('Gesetze im Internet'): return 'B'
    if an == 'Lexifina': return 'doc'
    return 'O'


for c in commits:
    c['k'] = ckind(c['an']); c['day'] = c['tr'].get('In-Kraft')
FED = [c for c in commits if c['k'] in ('G', 'V', 'T', 'O')]
first_day = min(c['day'] for c in commits if c['k'] in ('G', 'V', 'T', 'O', 'N', 'X') and c['day'])
last_day = max(c['day'] for c in commits if c['day'])
PROFILE['fed_commits'] = sum(1 for c in commits if c['k'] not in ('GG', 'doc', 'B', 'Lexifina'))
PROFILE['fed_from'], PROFILE['fed_to'] = first_day, last_day
PROFILE['acts'] = len(VZ)

versions = collections.Counter(); peryear = collections.defaultdict(collections.Counter)
for c in FED:
    for a, s, _ in c['acts']:
        if s == 'geändert':
            versions[a] += 1; peryear[a][c['day'][:4]] += 1
byabk = {}
for a in VZ:
    for k in (a['jurabk'], a['amtabk']):
        if k:
            byabk.setdefault(k, a)


def vkind(title):
    t = re.split(r'[\(\[]', re.sub(r'\s+', ' ', title))[0]
    if re.search(r'(?i)^(Bekanntmachung|Anordnung|Erlass|Erlaß|Richtlinie|Beschluss|Satzung|Vertrag|Abkommen|Übereinkommen|Vereinbarung|Staatsvertrag|Allgemeine Verwaltungsvorschrift|Verwaltungsvorschrift|Geschäftsordnung)\b', t):
        return 'S'
    if re.search(r'(?i)verordnung', t):
        return 'V'
    if re.search(r'(?i)gesetz', t):
        return 'G'
    return 'S' if not re.search(r'(?i)ordnung\b', t) else 'O'


# ---------------------------------------------------------------- c15 the age of the acts in force, and which of them changed since 2019
c15 = {'dec': collections.defaultdict(lambda: collections.Counter()), 'kinds': collections.Counter()}
changed = set(versions)
for a in VZ:
    y = int(a['ausfertigung'][:4]) if a['ausfertigung'][:4].isdigit() and a['ausfertigung'][:4] != '0000' else None
    if y is None:
        c15['nodate'] = c15.get('nodate', 0) + 1; continue
    k = vkind(a['title']); c15['kinds'][k] += 1
    ch = a['jurabk'] in changed or (a['amtabk'] and a['amtabk'] in changed)
    c15['dec'][y // 10 * 10][k + ('c' if ch else '')] += 1
old = sorted([[a['ausfertigung'], a['jurabk'], re.sub(r'\s+', ' ', a['title'])[:110], versions.get(a['jurabk'], 0)] for a in VZ
              if a['ausfertigung'][:4].isdigit() and '1000' < a['ausfertigung'][:4] < '1949'])
c15['old'] = old[:8]
c15['pre1949'] = len(old)
c15['pre1949_changed'] = sum(1 for o in old if o[3] > 0)
c15['pre1900'] = sum(1 for o in old if o[0] < '1900')
c15['codes'] = {k: [byabk[k]['ausfertigung'], versions.get(k, 0)] for k in ['BGB', 'StGB', 'HGB', 'ZPO', 'GewO', 'GVG', 'StPO', 'AO'] if k in byabk}
c15['dec'] = {str(k): dict(v) for k, v in sorted(c15['dec'].items())}
c15['kinds'] = dict(c15['kinds'])
c15['n'] = len(VZ)
c15['changed'] = sum(1 for a in VZ if a['jurabk'] in changed)
OUT['c15'] = c15

# ---------------------------------------------------------------- c16 the acts changed most often since June 2019
years = sorted({c['day'][:4] for c in FED})
top = versions.most_common(20)
c16 = {'rows': [], 'years': years, 'n_acts': len(versions), 'n_versions': sum(versions.values())}
for a, n in top:
    v = byabk.get(a)
    c16['rows'].append({'abk': a, 'title': re.sub(r'\s+', ' ', v['title']) if v else '', 'n': n, 'y': {y: peryear[a][y] for y in years}})
vs = sorted(versions.values(), reverse=True)
c16['top100'] = sum(vs[:100]); c16['top10pct'] = sum(vs[:max(1, len(vs) // 10)])
c16['jan1'] = sum(1 for c in FED for a, s, _ in c['acts'] if s == 'geändert' and c['day'][5:] == '01-01')
c16['jul1'] = sum(1 for c in FED for a, s, _ in c['acts'] if s == 'geändert' and c['day'][5:] == '07-01')
c16['acts_on_gii'] = len(VZ)
OUT['c16'] = c16

# ---------------------------------------------------------------- c17 amending laws named in the most acts' notes since June 2019
named = collections.defaultdict(set); maxart = collections.Counter()
LAWREF = re.compile(r'Art\.\s*(\d+)[^;]*?\b(G|V)\s+v\.?\s*(\d{1,2})\.(\d{1,2})\.(\d{4})\s+I\s+(Nr\.\s*\d+|\d+)')
for c in commits:
    if c['k'] in ('GG', 'doc', 'B'):
        continue
    for a, s, rest in c['acts']:
        if s not in ('geändert', 'neu'):
            continue
        stand = rest.split(' — ', 1)[1] if ' — ' in rest else ''
        for m in LAWREF.finditer(stand):
            day = '%s-%02d-%02d' % (m.group(5), int(m.group(4)), int(m.group(3)))
            key = (m.group(2), day, re.sub(r'\s+', ' ', m.group(6)))
            named[key].add(a); maxart[key] = max(maxart[key], int(m.group(1)))
# titles: laws from the DIP procedures; ordinances (and laws DIP gives no citation for) from the Bundesgesetzblatt entries
vt = {}
for r in LAW:
    if r['vpart'] == 'I':
        vt[(r['vyear'], r['vpage'])] = re.sub(r'\s*\(G-SIG: \d+\)', '', r['title'])
bg = {}
for e in jl('bgbl1.jsonl'):
    m = re.match(r'BGBl\. I (\d{4}) S\. (\d+)', e['fundstelle']) or re.match(r'BGBl\. (\d{4}) I Nr\. (\d+)', e['fundstelle'])
    if m:
        bg.setdefault((int(m.group(1)), int(m.group(2))), e['title'])


def law_title(key):
    k, day, cite = key
    num = int(re.sub(r'\D', '', cite)); y = int(day[:4])
    for yy in (y, y + 1):
        if k == 'G' and (yy, num) in vt:
            return vt[(yy, num)]
        if (yy, num) in bg:
            return bg[(yy, num)]
    return None


rank = sorted([kv for kv in named.items() if kv[0][1] >= first_day], key=lambda kv: (-len(kv[1]), kv[0][1]))
c17 = {'rows': [], 'n_laws': len(rank)}
for key, acts in rank[:15]:
    c17['rows'].append({'k': key[0], 'day': key[1], 'cite': f"{key[0]} v. {int(key[1][8:])}.{int(key[1][5:7])}.{key[1][:4]} I {key[2]}", 'acts': len(acts), 'art': maxart[key], 'title': law_title(key)})
sizes = [len(a) for k, a in rank]
c17['bins'] = [sum(1 for x in sizes if x == 1), sum(1 for x in sizes if 2 <= x <= 4), sum(1 for x in sizes if 5 <= x <= 9), sum(1 for x in sizes if 10 <= x <= 19), sum(1 for x in sizes if x >= 20)]
c17['laws_G'] = sum(1 for k, a in rank if k[0] == 'G'); c17['laws_V'] = sum(1 for k, a in rank if k[0] == 'V')
OUT['c17'] = c17

# =====================================================================================================================
# the Bundesverfassungsgericht and the constitutions
# =====================================================================================================================
BV = list(jl('bverfg.jsonl'))
NORM = re.compile(r'§|Artikel \d+[a-z]? (?:Absatz|Satz|Nummer|des|der)|\bArt\. \d|Gesetz|Verordnung|Satzung|Staatsvertrag')
FEDREF = re.compile(r'Bundesgesetzblatt|BGBl')
LANDREF = re.compile(r'Gesetz- und Verordnungsblatt|Gesetzblatt für|Gesetzblatt der|Gesetzblatt des|GVBl|GV\. ?NRW|Amtsblatt|Landes(?:gesetz|verfassung)|'
                     r'(?:Bayerisch|Niedersächsisch|Sächsisch|Hessisch|Hamburgisch|Bremisch|Berliner|Brandenburgisch|Thüringer|Saarländisch|Schleswig-Holsteinisch|Rheinland-Pfälzisch|Mecklenburg|Sachsen-Anhalt|Baden-Württemberg|Nordrhein-Westfalen)')
MON = {m: i + 1 for i, m in enumerate(['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'])}
DL = re.compile(r'(?:bis zum|bis spätestens zum|spätestens bis zum|spätestens zum|längstens bis zum|längstens bis|bis längstens zum|bis spätestens|spätestens bis) (\d{1,2})\. ?(' + '|'.join(MON) + r') (\d{4})')
c18 = {'y': collections.defaultdict(collections.Counter), 'lvl': collections.Counter(), 'empty': 0, 'pre': 0}
c19 = []
for d in BV:
    t, day = d['tenor'], d['decided'] or ''
    if not t:
        c18['empty'] += 1; continue
    ni = bool(re.search(r'\bnichtig\b', t)); uv = bool(re.search(r'\bunvereinbar\b', t))
    if not (ni or uv) or not NORM.search(t):
        continue
    if day < '1998':
        c18['pre'] += 1; continue
    cls = 'nichtig' if ni else 'unvereinbar'
    lvl = 'bund' if FEDREF.search(t) and not LANDREF.search(t) else 'land' if LANDREF.search(t) and not FEDREF.search(t) else 'beide' if FEDREF.search(t) else 'na'
    c18['y'][day[:4]][cls] += 1; c18['lvl'][(cls, lvl)] += 1
    name = d['title'].split(': ', 1)[1] if ': ' in d['title'] else d['az']
    # a deadline: a later day the tenor sets for a new rule or until which the provision still applies
    dl = None
    for m in DL.finditer(t):
        win = t[max(0, m.start() - 260):m.end() + 160]
        if not re.search(r'Gesetzgeber|Neuregelung|neu zu regeln|anwendbar|fortgelten|fort zu gelten|weitergelten|weiter gelten|verpflichtet', win):
            continue
        x = dt.date(int(m.group(3)), MON[m.group(2)], int(m.group(1)))
        if x > D(day) and (dl is None or x < dl):
            dl = x
    if dl:
        c19.append({'d': day, 'dl': dl.isoformat(), 'name': name.replace('-', ' '), 'az': d['az'], 'cls': cls, 'lvl': lvl,
                    'm': round((dl - D(day)).days / 30.44, 1)})
c18['y'] = {y: dict(v) for y, v in sorted(c18['y'].items())}
c18['lvl'] = {f'{a}|{b}': n for (a, b), n in c18['lvl'].items()}
c18['senate'] = len(BV); c18['all'] = INFO.get('bverfg_all')
c18['from'] = min(d['decided'] for d in BV if d['decided'] and d['decided'] >= '1998')
c18['to'] = max(d['decided'] for d in BV if d['decided'])
OUT['c18'] = c18
c19.sort(key=lambda r: r['d'])
OUT['c19'] = {'rows': c19, 'med': median([r['m'] for r in c19])}
PROFILE['bverfg_senate'] = len(BV); PROFILE['bverfg_all'] = INFO.get('bverfg_all')

# ---------------------------------------------------------------- c20 five constitutions
T = json.load(open(os.path.join(B, 'verfassungen.json'), encoding='utf-8'))
WORD = re.compile(r'[A-Za-zÄÖÜäöüßſ]+')


def body(txt):
    """the legal text of one file: without its heading, metadata lines and scan references"""
    out = []
    for line in txt.split('\n'):
        if line.startswith('#') or line.startswith('- Scan') or line.startswith('Scan:') or re.match(r'^- (Fundstelle|Datum|Text|PDF|Quelle):', line):
            continue
        out.append(line)
    return '\n'.join(out)


def words(s):
    return len(WORD.findall(s))


con = []
# Grundgesetz 1949 and today: one file per article (Art. 1 to 19 are the basic rights)
for key, label, year in [('gg1949', 'gg1949', 1949), ('gg', 'gg', int(INFO['head_date'][:4]))]:
    files = T[key]; arts = {p: body(x) for p, x in files.items() if re.search(r'/\d{3}[a-z]?\.md$', p)}
    live = {p: x for p, x in arts.items() if not re.fullmatch(r'\s*\(?(weggefallen|aufgehoben)\)?\s*', x.strip()) and words(x) > 2}
    allw = sum(words(body(x)) for p, x in files.items() if not p.endswith('README.md'))
    rights = sum(words(x) for p, x in live.items() if int(re.search(r'/(\d{3})', p).group(1)) <= 19)
    con.append({'k': label, 'year': year, 'units': len(live), 'words': allw, 'rights': rights})
# the historical constitutions (Wikisource transcriptions; 1849 is uncorrected OCR, one file per printed page)
H = T['hist']
for folder, label, year, rights_from, rights_to in [('verfassung-norddeutscher-bund-1867', 'ndb1867', 1867, None, None),
                                                     ('reichsverfassung-1871', 'rv1871', 1871, None, None),
                                                     ('weimarer-reichsverfassung-1919', 'wrv1919', 1919, 109, 165)]:
    arts = {p: body(x) for p, x in H.items() if f'/{folder}/artikel-' in p}
    allw = sum(words(x) for x in arts.values())
    rights = sum(words(x) for p, x in arts.items() if rights_from and rights_from <= int(re.search(r'artikel-(\d+)', p).group(1)) <= rights_to)
    con.append({'k': label, 'year': year, 'units': len(arts), 'words': allw, 'rights': rights})
pages = sorted((p for p in H if '/paulskirchenverfassung-1849/seite-' in p), key=lambda p: int(re.search(r'seite-(\d+)', p).group(1)))
txt = '\n'.join(H[p].split('\n---\n', 1)[1] if '\n---\n' in H[p] else body(H[p]) for p in pages)
paras = [int(m.group(1)) for m in re.finditer(r'§\. (\d{1,3})\.', txt)]
i130 = txt.find('§. 130.'); i190 = txt.find('§. 190.')
con.append({'k': 'pk1849', 'year': 1849, 'units': max(paras) if paras else None, 'words': words(txt), 'rights': words(txt[i130:i190]) if 0 < i130 < i190 else None, 'ocr': True})
con.sort(key=lambda c: c['year'])
OUT['c20'] = {'rows': con, 'pk_marks': len(set(paras))}

# =====================================================================================================================
OUT['profile'] = PROFILE
OUT['geo'] = json.load(open(os.path.join(HERE, 'laender.topo.json'), encoding='utf-8'))
PROFILE['dip_to'] = max(s[0] for r in V for s in r['steps'] if s[0] <= '2099')
PROFILE['built'] = max(PROFILE['dip_to'], PROFILE['fed_to'])
json.dump(OUT, open(os.path.join(B, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('data.json', os.path.getsize(os.path.join(B, 'data.json')), 'bytes')
