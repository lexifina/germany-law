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
