# German case law: Bundespatentgericht

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the case law of the Bundespatentgericht, Germany, which global-law reads at `germany/bpatg/caselaw/`.

Every published decision of the Bundespatentgericht in the corpus this is built from, as a git history: one file per decision, one
commit per decision, dated the day it was decided. 31,203 decisions from 2000-01-05 to 2025-07-08.

## Questions as git commands

| Question | Command |
|---|---|
| A decision | `cat decisions/bpatg/<year>/<ECLI or Aktenzeichen>.md` |
| By Aktenzeichen or ECLI | `git log --grep='^Docket: 1 BvR 123/20$' --stat` · `grep '1 BvR 123/20' decision-index.tsv` |
| Decisions given in a window | `git log --since=2024-03-01 --until=2024-03-31 --format='%ad %an' --date=short` |
| Decisions citing § 823 BGB | `cat judgments/germany/bund/acts/bgb/0823.jsonl` |
| The provision as the court applied it | each overlay row's `law_commit` is the provision's own version in germany-law on the day decided; germany-law's record for acts other than the Grundgesetz starts 2019-06-10, so older decisions give `law_record_from` instead |
| Who wrote a line? | `git blame decisions/...`: each line is credited to the decision (court and Aktenzeichen) |

## Dates and authors
The commit date is the day the decision was given, at noon Berlin (`In-force:` and `Decided:`). The author is the court
and the Aktenzeichen, at an address that cannot exist. These are court rulings, not laws: every commit is `Kind: court`.

## The judgment overlay
Citations of federal law in the decision's text ("§ 823 Abs. 1 BGB", "Art. 3 Abs. 1 GG") are linked to the provision
files of lexifina/germany-law by the official abbreviations in its `verzeichnis.json`: 92,410 links, 0 of them
inside germany-law's record. Abbreviations two acts share are not linked.

## Source and licence
The decisions are official works of the Bundespatentgericht (§ 5 UrhG); each file links to the court's own page where the corpus gives
one. Built from the CC0 "Corpus der Entscheidungen" CSV on Zenodo (record 15754093, snapshot 2025-07-08). This
repository is dedicated to the public domain under CC0 1.0.

## What it does not show
Decisions the court did not publish, and decisions after 2025-07-08.
