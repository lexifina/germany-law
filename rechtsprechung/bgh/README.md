# German case law: Bundesgerichtshof

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the case law of the Bundesgerichtshof, Germany, which global-law reads at `germany/bgh/caselaw/`.

Every published decision of the Bundesgerichtshof in the corpus this is built from, as a git history: one file per decision, one
commit per decision, dated the day it was decided. 113,604 decisions from 1950-10-02 to 2025-04-07.

## Questions as git commands

| Question | Command |
|---|---|
| A decision | `cat decisions/bgh/<year>/<ECLI or Aktenzeichen>.md` |
| By Aktenzeichen or ECLI | `git log --grep='^Docket: VI ZR 123/20$' --stat` · `grep 'VI ZR 123/20' decision-index.tsv` |
| Decisions given in a window | `git log --since=2024-03-01 --until=2024-03-31 --format='%ad %an' --date=short` |
| Decisions citing § 823 BGB | `cat judgments/germany/bund/acts/bgb/0823.jsonl` |
| The provision as the court applied it | each overlay row's `law_commit` is the provision's own version in germany-law on the day decided; germany-law's record for acts other than the Grundgesetz starts 2019-06-10, so older decisions give `law_record_from` instead |
| Who wrote a line? | `git blame decisions/...`: each line is credited to the decision (court and Aktenzeichen) |

## Dates and authors
The commit date is the day the decision was given, at noon Berlin (`In-force:` and `Decided:`). The author is the court
and the Aktenzeichen, at an address that cannot exist. These are court rulings, not laws: every commit is `Kind: court`.

## The judgment overlay
Citations of federal law in the decision's text ("§ 823 Abs. 1 BGB", "Art. 3 Abs. 1 GG") are linked to the provision
files of lexifina/germany-law by the official abbreviations in its `verzeichnis.json`: 527,538 links, 134,291 of them
inside germany-law's record. Abbreviations two acts share are not linked.

## Source and licence
The decisions are official works of the Bundesgerichtshof (§ 5 UrhG); each file links to the court's own page where the corpus gives
one. Built from the CC0 "Corpus der Entscheidungen des Bundesgerichtshofs" (CE-BGH, Zenodo record 15153244, decisions from 2000) and "Entscheidungen des Bundesgerichtshofs in Strafsachen aus dem 20. Jahrhundert" (BGH-Strafsachen-20Jhd, Zenodo record 4540377, CC0, the criminal senates 1950-1999), both by Seán Fobbe (snapshot 2025-04-07). This
repository is dedicated to the public domain under CC0 1.0.

## What it does not show
Decisions the court did not publish, and decisions after 2025-04-07. Before 2000 only the criminal senates (1 to 5; nothing of the 6th, 1954-1956): no open corpus holds the civil senates' older decisions. The texts of 1950-1999 were read from scans (OCR), so they contain recognition errors. Decisions after the CE-BGH snapshot are added by the nightly runner from the court's RSS feed of new decisions (bundesgerichtshof.de), so the months between the snapshot and the runner's first day are a gap until a newer CE-BGH version fills it.
Decisions the corpus gives no date for cannot be dated as a commit: they are listed in `unresolved.csv` (2,284),
with the cited abbreviations that name no act in germany-law.
