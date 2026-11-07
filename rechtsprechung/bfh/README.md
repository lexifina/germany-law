# German case law: Bundesfinanzhof

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the case law of the Bundesfinanzhof, Germany, which global-law reads at `germany/bfh/caselaw/`.

Every published decision of the Bundesfinanzhof in the corpus this is built from, as a git history: one file per decision, one
commit per decision, dated the day it was decided. 10,885 decisions from 2010-01-04 to 2025-01-14.

## Questions as git commands

| Question | Command |
|---|---|
| A decision | `cat decisions/bfh/<year>/<ECLI or Aktenzeichen>.md` |
| By Aktenzeichen or ECLI | `git log --grep='^Docket: IX R 12/19$' --stat` · `grep 'IX R 12/19' decision-index.tsv` |
| Decisions given in a window | `git log --since=2024-03-01 --until=2024-03-31 --format='%ad %an' --date=short` |
| Decisions citing § 823 BGB | `cat judgments/germany/bund/acts/bgb/0823.jsonl` |
| The provision as the court applied it | each overlay row's `law_commit` is the provision's own version in germany-law on the day decided; germany-law's record for acts other than the Grundgesetz starts 2019-06-10, so older decisions give `law_record_from` instead |
| Who wrote a line? | `git blame decisions/...`: each line is credited to the decision (court and Aktenzeichen) |

## Dates and authors
The commit date is the day the decision was given, at noon Berlin (`In-force:` and `Decided:`). The author is the court
and the Aktenzeichen, at an address that cannot exist. These are court rulings, not laws: every commit is `Kind: court`.

## The judgment overlay
Citations of federal law in the decision's text ("§ 823 Abs. 1 BGB", "Art. 3 Abs. 1 GG") are linked to the provision
files of lexifina/germany-law by the official abbreviations in its `verzeichnis.json`: 76,530 links, 25,424 of them
inside germany-law's record. Abbreviations two acts share are not linked.

## Source and licence
The decisions are official works of the Bundesfinanzhof (§ 5 UrhG); each file links to the court's own page where the corpus gives
one. Built from the CC0 "Corpus der Entscheidungen" CSV on Zenodo (record 14622341) (snapshot 2025-01-14). This
repository is dedicated to the public domain under CC0 1.0.

## What it does not show
Decisions the court did not publish, and decisions after 2025-01-14.
Decisions the corpus gives no date for cannot be dated as a commit: they are listed in `unresolved.csv` (0),
with the cited abbreviations that name no act in germany-law.
