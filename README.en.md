# Germany: law history in git

**English** · **[Oder auf Deutsch lesen](README.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="German law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of Germany as a git history: one file per article of the Grundgesetz and per provision of every other federal act, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a provision; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Germany's federal law, which global-law reads at `germany/bund/acts/`.

**What is in it now:** the Grundgesetz with every version since 1949 (the 1949 text and its 69 amending laws, in 72 commits), and 6,147 other federal acts from Gesetze im Internet, with 16,392 versions since 10 June 2019. [`verzeichnis.json`](verzeichnis.json) lists every act with its abbreviation, title and Gazette citation; [`grundgesetz/gesetze.csv`](grundgesetz/gesetze.csv) lists the amending laws with their dates and votes.

The Grundgesetz is in `grundgesetz/artikel/`, one file per article (`109.md` is Article 109, the budgets of the Federation and the Länder); every other act is a folder named as on Gesetze im Internet, one file per provision (`burlg/0003.md` is § 3 of the Bundesurlaubsgesetz, the Federal Leave Act).

The text is in German, as Gesetze im Internet publishes it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 109 of the Grundgesetz | `git log -p --word-diff -- grundgesetz/artikel/109.md` |
| Which amending law wrote each line of Article 109? | `git blame grundgesetz/artikel/109.md` |
| Every version of Article 109, with the day each took effect | `git log --format="%h %(trailers:key=In-Kraft,valueonly,separator=) %an" -- grundgesetz/artikel/109.md` |
| Article 109 as in force on 1 January 2025 | `python tools/stand_am.py 2025-01-01 109` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about German law](https://global-law.lexifina.com/v1/try_claude?country=germany)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=germany)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=Jahresurlaub&jurisdictions=germany)**: a search of German law for "Jahresurlaub", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in German or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add germany/bund/acts
python3 tools/law.py show 2026-01-01 germany/bund/acts/grundgesetz/artikel/109.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Europe/Berlin, on the day the version took effect, and carries it in its `In-Kraft:` trailer:

- for the Grundgesetz, the day each amending law took effect, and, where known, the days it was passed, signed and promulgated (`Beschlossen:`, `Ausgefertigt:`, `Verkuendet:`); where a law sets no day, Article 82(2) GG puts it in force on the fourteenth day after the Bundesgesetzblatt issue appeared;
- for other federal law, the day the change first appeared on Gesetze im Internet, which consolidates changes as they take effect (the archive read it weekly until May 2020, daily since); where the act's footnotes give an earlier in-force day (`mWv 21.5.2003`), the commit also carries `In-Kraft-laut-Fussnote:`;
- git cannot store dates before 1970, so Grundgesetz commits for earlier changes are dated from 1970-01-01, one second apart, with the real day in `In-Kraft:` and in the `in-kraft/YYYY-MM-DD` tags. Ask for a date with `tools/stand_am.py`, not `git log --before`.

Each change is credited to the law that made it: `69. Änderung (2025)` for the 69th amending law to the Grundgesetz, or `G v. 22.12.2025 I Nr. 371` for federal law, as the act's Stand note names it. Changes no law explains are labelled, never credited to a law: `Gesetze im Internet (Bestand)` for the first state of 2019, `Textänderung ohne neue Standangabe` (1,160 of 3,232 federal commits), `Neu aufgenommen` and `Nicht mehr veröffentlicht`.

## How it is checked

- The Grundgesetz's final text equals today's official text on Gesetze im Internet, article for article. DocPatch's text differed from it in 43 articles; the official text replaces it from each article's last change on, and every correction is listed in [`grundgesetz/KORREKTUREN.md`](grundgesetz/KORREKTUREN.md).
- The dates of the 64th to 69th amending laws were checked against each law in the Bundesgesetzblatt.
- The build is deterministic: the commands in [`REPRODUCE.md`](REPRODUCE.md) give the same 3,304 law commits with the same hashes.
- History is append-only: later runs add commits on top, dates never decrease, and nothing is replaced.

## What it does not show

- **Federal law before 10 June 2019**, other than the Grundgesetz. Gesetze im Internet keeps only the current text; rebuilding the earlier versions from the Bundesgesetzblatt is planned.
- **Older Grundgesetz versions checked against the Gazette.** The versions of an article before its last change before 2019 are DocPatch's transcription.
- **The exact in-force day** of a federal change where the footnotes do not give it, and the stages of a law that takes effect in several steps under one Stand note.
- **Footnotes and images.** Footnotes are left out; images are marked `[Bild: …]`.
- **State law, case law and EU law.** global-law holds state law and federal court decisions in [their own repositories](https://github.com/lexifina/global-law/tree/main/germany) (`germany/bavaria/acts`, `germany/bgh/caselaw` ...).

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Gesetze im Internet](https://www.gesetze-im-internet.de) (Bundesministerium der Justiz) | Official consolidated text of federal law | no, the current text only | Every act, and the Grundgesetz from 2019; only the Bundesgesetzblatt is authoritative |
| [QuantLaw/gesetze-im-internet](https://github.com/QuantLaw/gesetze-im-internet) | Archive of Gesetze im Internet | yes, weekly from 10 June 2019, daily from May 2020 | Where the past versions of federal acts come from |
| [DocPatch](https://github.com/c3e/grundgesetz-dev) | The Grundgesetz of 1949 and its 1st to 63rd amending laws, as patches | yes, every version | With dates, signatories, Gazette citations and votes |
| [Deutscher Bundestag, Datenhandbuch](https://www.bundestag.de/datenhandbuch) | Dates of the 64th to 69th amending laws | | Checked against the Bundesgesetzblatt |

## Licence

See [`LICENSE`](LICENSE). German statutes are not protected by copyright (§ 5 Abs. 1 UrhG); DocPatch's own content is CC BY-SA 3.0 DE and QuantLaw's archive BSD-3-Clause. This repository is released under CC0 1.0.

This repository is not legal advice and not an official publication. No AI model wrote or changed legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
