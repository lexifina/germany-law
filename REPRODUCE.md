# How this history was made, and how to make it again

This file records how the repository was built: the sources, the commands, the software, the decisions made by hand,
and what an AI model did and did not do. The build script fills in the numbers below, so they always describe this
build. Anyone with Python, git and `patch` can rebuild it and get the same commits.

## Short version

```sh
git clone https://github.com/c3e/grundgesetz-dev gg-dev
git -C gg-dev checkout dea0774d4fc049c7ef2a4b56c5757f66750bd89d
git clone --mirror https://github.com/QuantLaw/gesetze-im-internet gii.git
git --git-dir gii.git update-ref refs/heads/data 648cd775796104cb60e306e1bf9596a2af53df2e
python -X utf8 tools/build.py --docpatch gg-dev --archive gii.git --repo rebuilt --site site --docs-date 2026-10-28
```

This gives 3304 law commits (72 for the Grundgesetz, 3232 for other federal law)
and one documentation commit, with the same hashes as this repository. QuantLaw's archive only grows, so later
clones contain the pinned commit.

## Sources

| What | Where | Version |
| --- | --- | --- |
| The Grundgesetz of 1949 and the 1st to 63rd amending laws, with dates, signatories, Gazette citations and votes | [c3e/grundgesetz-dev](https://github.com/c3e/grundgesetz-dev) (DocPatch): `src/*.md`, the patches in `src/patches/series`, `etc/meta.json` | commit `dea0774d4fc049c7ef2a4b56c5757f66750bd89d` |
| The official consolidated text of every federal act, including the Grundgesetz, from 10 June 2019 | Gesetze im Internet (Federal Ministry of Justice), as archived by [QuantLaw/gesetze-im-internet](https://github.com/QuantLaw/gesetze-im-internet), branch `data` | commit `648cd775796104cb60e306e1bf9596a2af53df2e` |
| Dates of the 64th to 69th amending laws to the Grundgesetz | Deutscher Bundestag, Datenhandbuch, chapter 13.2 (as of 16 May 2025), checked against each law in the Bundesgesetzblatt | `LATER_LAWS` in `tools/grundgesetz.py` |

Nothing was typed in, summarised or rewritten, except the corrections listed in `grundgesetz/KORREKTUREN.md`, each with its
evidence.

## The scripts

| File | Git blob | Does |
| --- | --- | --- |
| `tools/build.py` | `ae5d26d204eeb811042e6fce3447dd7ce3315733` | Runs the two parts, interleaves them by date and writes the history with `git fast-import` |
| `tools/grundgesetz.py` | `19e0a1499f3099230c648487ad9a978602fbf1b1` | Builds the Grundgesetz record (also the data behind lexifina.com/watch/grundgesetz) |
| `tools/bundesrecht.py` | `40e5a5ce64becc35f94192f7ef252be3821ccc6b` | Turns the archive into the federal-law commits |
| `tools/stand_am.py` | | Prints the law on a day from the tags |

They use the Python standard library, git and GNU `patch`, and were run with Python 3.12.10 and git 2.46.0 on Windows 11.
They are the same files as `scripts/germany-law/build.py`, `scripts/grundgesetz/build.py` and `scripts/bundesrecht/build.py`
in Lexifina's own repository.

## The Grundgesetz, step by step

1. **DocPatch.** The 1949 text is copied to a scratch folder and each patch in `src/patches/series` is applied in turn
   (`patch -p1`, or `-p0` for patches naming `src/` paths). The text after each patch is one version: 64 in all.
2. **The renumbering of 1968.** The 16th amending law repealed Article 96 and renumbered Article 96a as Article 96.
   DocPatch builds later versions of Article 96 from the repealed 1949 text and keeps Article 96a; from 1968 on, Article
   96a is dropped and Article 96 keeps the 1968 text's paragraphs 1 to 3.
3. **Reconciliation.** DocPatch's 2019 version is compared with the first archived official version that names the 63rd
   amending law. 43 articles differed. For each, the official text replaces DocPatch's from the article's last
   change on.
4. **The later laws.** Each later official version is compared with the one before; the articles that changed are taken
   from it and credited to the law its Stand note names. A change with no new law is the publisher correcting itself:
   the corrected words replace the version of the law that last changed that article. Article 143h's expiry on
   31 December 2020 (Art. 2 Satz 2 of the 65th amending law) is a step of its own.
5. **Check.** The final text equals today's official text on Gesetze im Internet, article for article.

The record and the corrections are written to `grundgesetz/` (`gesetze.json`, sha256 `909fadd1039089b53f660da73fa7607c3d06802ff19ae7ea6e956e33fb6d027f`;
`gesetze.csv`; `KORREKTUREN.md`; `artikel/README.md`).

## Federal law, step by step

1. `git log data --reverse --raw` lists every scrape with the blob of each act file it changed. The scrape's time comes
   from its message, because the archive's 2019 commits were made in May 2020. The archive's first real scrape is
   10 June 2019; its commits of 31 December 2018 are empty.
2. One long-lived `git cat-file --batch` reads each changed blob. Each act's XML becomes Markdown: one heading per norm
   and per division, one line per paragraph or list item (a list item's number joined to its text), superscript
   sentence numbers, tables as `| … |` rows and images as `[Bild: …]`. Footnotes, `noindex` content and build stamps
   are left out.
3. An act whose Markdown did not change (a rebuild by the publisher) is skipped. A file missing from one scrape that
   reappears later is a gap in the archive, not a removal (3,646 files were missing on 5 May 2026). The Grundgesetz
   (`gg`) is left out here, since `grundgesetz/` has its full history.
4. The acts that changed in a scrape are grouped by the law their Stand note names; the last law named across all Stand
   entries is taken ("Neugefasst durch Bek. …;" and "zuletzt geändert durch G …" can be separate entries). Changes with
   no new law get their own label.
5. Each commit is dated, and its `In-Kraft:` trailer set to, the day of the scrape that first showed the change: Gesetze
   im Internet consolidates changes as they take effect, and this keeps the history in in-force order and append-only.
   Where the act's footnotes give that law's in-force date (`… G v. 16.5.2003 I 660 mWv 21.5.2003`) and it is earlier,
   the latest such date on or before the scrape is kept as `In-Kraft-laut-Fussnote:`.
6. The index of acts is written to `verzeichnis.json` (sha256 `63a43e0a34e0e97563943b0e62a26b079b0acc7d8dfba0685f0143b91eeb1b22`), 6147 acts.

## One history

Grundgesetz commits go in before the first federal change observed on or after their in-force date, so the history runs
in in-force order and dates never decrease. Each run ends with its own documentation commit, and later runs append on
top of it (`--append`); nothing is ever replaced. The runs so far are 2026-10-28 (archive `648cd77579`). A rebuild with `--replay
stand.json` ends runs in the same places and gives the same commits. Every commit is dated at noon in Berlin (before 1970: 1 January 1970 UTC, a second apart). The author is the
law, at an address ending `.invalid`; the committer is `Lexifina <germany-law@lexifina.com>`. Tags:

- `in-kraft/YYYY-MM-DD`: the Grundgesetz as in force on that day (each day an amending law took effect);
- `gg/NN`: each amending law to the Grundgesetz;
- `stand/YYYY-MM-DD`: every federal act as Gesetze im Internet published it that day.

The documentation commit comes last, dated `2026-10-28`, so a rebuild gives the same commits.

## Decisions made by hand

1. Dates are dates in force, because they decide which text applies.
2. The Grundgesetz's dates not in the source: the 58th amending law in force 27 July 2010; the 33rd in two parts
   (28 August and 14 December 1976); Article 143h expiring 31 December 2020 (the Datenhandbuch's 2021 is contradicted by
   the law's own text). All in `grundgesetz/KORREKTUREN.md`.
3. The official text is preferred wherever it and DocPatch differ, from the article's last change on.
4. For federal law, the amending law is the one the act's Stand note names, and the in-force date is taken from the
   act's footnotes where they give it. Changes no law explains are labelled, never credited to a law.
5. Footnotes are left out of the federal text, because they record history rather than law.
6. Gaps in the archive are not removals.

## What an AI model did

This repository was built on 28 October 2026 in **Claude Code**, Anthropic's coding tool, by the model **Claude Opus
5.5** (model id `claude-opus-5-5`), working from goals set by the user at Lexifina: a git history of the Grundgesetz with
proper dates, then all German law in one repository named for the country, kept up to date with every correction found.

The model wrote the scripts and these files, chose the design, found the problems corrected above (including by
comparing DocPatch with the official text and the Bundesgesetzblatt), checked dates against the Datenhandbuch and the
laws in the Gazette, ran the builds and checked the results. It did **not** write or edit any legal text: every word
comes from DocPatch or Gesetze im Internet, and every date, title and vote from the sources above, except the corrections
listed with their evidence. No AI model is called when the history is built; rebuilding it needs no model.

The work was not reviewed line by line by a lawyer. Only the Bundesgesetzblatt is authoritative.

## Changes to this history

- **28 October 2026.** First published as `grundgesetz` (the Grundgesetz to 2017, from c3e/grundgesetz), then rebuilt
  from DocPatch and the official text to the 69th amending law.
- **28 October 2026.** Renamed `germany-law` at the user's request, so that every country has one repository named
  `<country>-law` with federal law as one part. Rebuilt with the Grundgesetz under `grundgesetz/` and all federal law under
  one folder per act (`bgb/`, `stgb/` …). All commit hashes changed. Refresh existing clones with `git fetch --force --tags`.

## Parts added on 17 November 2026

Each part is written by a bulk runner (one commit per official record, dated by its day, the record named as author)
and replayed onto main. Rates are the ones used; robots.txt is treated as advisory (Alan, 2026-11-08) and noted here.

| Part | Source | Access, rate | robots.txt / reservation |
| --- | --- | --- | --- |
| `bund/gesetze/` (new versions) | Gesetze im Internet via QuantLaw/gesetze-im-internet's daily archive (BSD-3), read with `tools/bundesrecht.py` | git, hourly check | GII: robots allow all, no TDM header |
| `bund/bgbl/teil-1`, `teil-2` 1949–2022 | OffeneGesetze (api.offenegesetze.de, OKF DE), a copy of the Bundesgesetzblatt: title, dates, page, the PDF's text layer (unchecked, two-column pages interleaved) | documented API, 1 request in flight, ≥ 1 s | content-signal comment block without values |
| `bund/bgbl/` 2023– | www.recht.bund.de, the binding electronic Bundesgesetzblatt: page metadata, ELI, PDF text layer; PDF MD5 checked against the page | 1 request every ≥ 30 s (robots Crawl-delay 30) | robots allows /bgbl/ |
| `laender/<land>/` | lexifina/germany-{bavaria,saxony,brandenburg,bremen,north-rhine-westphalia,hamburg}-law, replayed commit for commit (same blobs, same dates, trailer `Uebernommen-aus:`), tree SHA checked per 2,000 commits | git | as recorded in each source repository; landesrecht-hamburg.de (juris) sends `tdm-reservation: 1` |
| `rechtsprechung/<gericht>/` | lexifina/germany-{bverfg,bgh,bverwg,bfh,bag,bpatg}-caselaw and germany-hamburg-caselaw, replayed the same way | git | as recorded in each source repository |
| `rechtsprechung/<gericht>/` (new decisions, BSG) | www.rechtsprechung-im-internet.de (BMJ/juris): rii-toc.xml and one XML zip per decision; Leitsatz, Tenor, Tatbestand, Entscheidungsgründe, Gründe, abweichende Meinung written; Titelzeile, Orientierungssätze and Normenkette left out | 1 request in flight, ≥ 3 s | robots `Disallow: /` for `*`; HTTP header `tdm-reservation: 1` |
| `bundestag/vorgaenge/` | DIP, Deutscher Bundestag/Bundesrat (search.dip.bundestag.de/api/v1, the public key from the DIP API help page): every Gesetzgebung Vorgang since 1949, one commit per procedural step | documented API, ≥ 1 s | DIP Nutzungsbedingungen (27.02.2023): machine access through the API; data may be reused with the source "Deutscher Bundestag/Bundesrat – DIP" |
| `kommunen/` | Destatis GV-ISys, Gemeindeverzeichnis, Gebietsstand 30.09.2026 | one file | reproduction permitted with source credit |

**Reservations of text and data mining.** rechtsprechung-im-internet.de, the juris-run Landesrecht portals, NI-VORIS and
gesetzesportal.de send `tdm-reservation: 1` (NI-VORIS also a `tdm-policy`). Alan decided on 17 November 2026: statutes and
court decisions are official works without copyright (§ 5 UrhG), so a § 44b(3) UrhG reservation does not cover their
texts; they are taken, official text only (no editorial headnotes, summaries or annotations), at the pace above, and any
block page, 401/403/429 stops that host.

## Parts added on 18 November 2026

Same method as the parts of 17 November: one bulk runner per source, one commit per official record dated by its day
(issue day, sitting day or in-force day; before 1970 the commit date is 1970-01-01 plus seconds and the real day opens the
subject line), the record or the issuing body named as author, replayed onto main. Every runner of these parts shares one
per-host budget: at least 10 s between two requests to the same host from any runner, at most 3,000 requests a host a
day; six connection failures in a row, any check page, 401, 403 or 429 stop that host for good (only Alan lifts a stop).
Documents that name private persons (awards, appointments, lists of names, public service of notices, lost savings books
and the like) are recorded with their metadata and source link only. Text is the PDF's text layer (pdftotext) unless a
file says OCR (Tesseract, not proofread).

| Part | Source | Notes |
| --- | --- | --- |
| `bund/fassungen-vor-2019/<act>/` | Earlier versions of federal acts, rebuilt from the Bundesgesetzblatt: the Fundstellennachweis A (recht.bund.de) names each act's base text and every amending act; their text comes from the BGBl issue PDFs (OffeneGesetze); the amending instructions are applied forwards from the base and undone backwards from the 2019 text of Gesetze im Internet | A version is written only where applying the instructions gives the next known text; anything not readable safely is left out (held). Corrections are separate commits with `Kind: correction` |
| `bundestag/plenarprotokolle/` | Bundestag open data (www.bundestag.de/services/opendata): pp01–pp19 zip archives, one XML per sitting for WP 20–21 | one commit per sitting |
| `bundestag/drucksachen/`, `bundesrat/drucksachen/` | DIP API `drucksache-text` (public key from the DIP help page, read at run time, never stored) | full text for legislative documents; other kinds metadata and link |
| `laender/<land>/gvbl/` | Land law gazettes from official non-juris hosts: Hessen (Landtag StarWeb archive, 1946–), Baden-Württemberg (Landtag sitemap, 1950–), Berlin (Senatsverwaltung für Justiz, berlin.de, 2004–), Rheinland-Pfalz (Staatskanzlei, 2004–), Thüringen and Mecklenburg-Vorpommern (Landtag ParlDok), Schleswig-Holstein (GVOBl 1946– in the Landtag's LIS-SH), Brandenburg (GVBl Teil I via the Landtag), Bayern (verkuendung-bayern.de), Nordrhein-Westfalen (recht.nrw.de), Niedersachsen (Verkündungsplattform 2024–) | one commit per issue or publication; scanned issues OCR'd, labelled |
| `laender/<land>/mbl/`, `laender/bayern/baymbl/` | Ministerialblätter: MBl. NRW (recht.nrw.de), BayMBl (verkuendung-bayern.de, 2019–), Nds. MBl (Verkündungsplattform Niedersachsen, 2024–) | notices naming private persons: metadata only |
| `laender/<land>/landtag/` (and `abgeordnetenhaus/`, `buergerschaft/`) | The Landtage's own document stores: Baden-Württemberg (sitemap), Bayern (Drucksachen store), Berlin (PARDOK open-data export, dl-de/by-2-0), Brandenburg and Rheinland-Pfalz (eUI/StarWeb portals), Bremen, Hessen (StarWeb cache), Mecklenburg-Vorpommern and Thüringen (ParlDok), Niedersachsen (public document list; NILAS not used), Nordrhein-Westfalen (document archive), Sachsen (EDAS), Sachsen-Anhalt (PADOKA), Schleswig-Holstein (LIS-SH) | Drucksachen, Plenarprotokolle, Beschlüsse as published; Eingaben and other papers naming private persons: metadata only. Hamburg's ParlDok is stopped (connection failures) |
| `laender/niedersachsen/vorschriften/` | NI-VORIS (Wolters Kluwer for the Land): the official text of Niedersachsen's laws and ordinances with their dated versions | official text only; publisher's notes, footnotes and abbreviations left out; `tdm-reservation` header: see the reservation note above |
| `laender/nordrhein-westfalen/amtsblaetter/bezreg-<bezirk>/` | Amtsblätter of the Bezirksregierungen Arnsberg (2010–), Detmold and Köln, from the authorities' own sites | one file and commit per numbered notice (`<year>/<nr>/<lfd. Nr.>.md`, head and contents in `index.md`); notices naming private persons metadata only; garbled text layers OCR'd, labelled |
| `rechtsprechung/bayern/` | BAYERN.RECHT (www.gesetze-bayern.de), the Free State's own portal: the decision XML | one commit per decision |
| `kommunen/<ARS>/vorlagen/` | The councils' OParl APIs (open standard; endpoint list in `data/oparl/endpoints.yml`): papers that are Satzungen or Verordnungen | hosts behind an interactive check are skipped |
| `kommunen/<ARS>/ortsrecht/` | The cities' own Ortsrecht collections: München (every published version), Köln, Dresden, Nürnberg, Münster, Heidelberg, Stuttgart | one file per Satzung, its versions as commits dated by the latest date in the document's head; the collections are not the binding promulgation (said in each file). www.stuttgart.de's robots.txt disallows ClaudeBot; Alan decided on 18 November 2026 to take its Stadtrecht anyway ("stuttgart take"; robots.txt advisory, rule of 8 November 2026), at the pace above |
| `kommunen/<ARS>/amtsblatt/` | Amtsblatt der Stadt Köln; Amtsblatt für die Region Hannover und die Landeshauptstadt Hannover | as the Regierungsbezirk Amtsblätter |
| `historisch/verfassungen/` | Verfassung des Norddeutschen Bundes 1867, Reichsverfassung 1871, Weimarer Reichsverfassung 1919 from de.wikisource ("fertig" transcriptions, each page tied to its gazette scan); the Paulskirchenverfassung (below) | |

**Historical constitutions (Paulskirchenverfassung).** `historisch/verfassungen/paulskirchenverfassung-1849/`: the
Verfassung des deutschen Reiches of 28 March 1849, as issued in the Reichs-Gesetz-Blatt 1849, 16. Stück, pp. 101–147.
Source: the scan of the Bayerische Staatsbibliothek (https://www.digitale-sammlungen.de/view/bsb10518698,
urn:nbn:de:bvb:12-bsb10518698-5), read through its IIIF image API, one request every ≥ 10 s. The library labels the
scan NoC-NC 1.0 (no copyright, non-commercial use of the digitisation); Alan decided on 18 November 2026 that such
official scans may be used, non-commercially, with this note. The law's text is an official work (§ 5 UrhG). Text:
Tesseract OCR with the Fraktur model `deu_latf`, one file per printed page with its scan image named (the volume's images
are not bound in page order). A labelled correction (18 November 2026) transcribes § 87 with its two tables and § 88
(pp. 115–116) from the scan and sets the § headings the OCR misread; the rest is not proofread. (This note was first
written on 18 November but did not reach main; it is given here.)

**Not used.** Hosts that answered with an interactive check or blocked this machine stay stopped and are not reached by
any other route: all juris-run hosts (since 17 November 2026), the NRW e-Pflicht archives of the university libraries,
the Deutsche Digitale Bibliothek item pages, ALEX (ÖNB), Wikimedia uploads, Parlamentsspiegel, the Hamburgische
Bürgerschaft's ParlDok, sitzung-online.de council systems.
