# Bremen: law history in git

The law of the Freie Hansestadt Bremen as a git history: one file per Artikel or Paragraph, one paragraph per line, one commit per amending act on the day the new version took effect. `git blame` names the act behind each change; `git log` lists every change; picking a date gives the text in force that day. The text is German.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

Every version of each act that the Transparenzportal Bremen lists under "Frühere Fassungen", plus the current one.

| Folder | Act | History |
| --- | --- | --- |
| `verfassung/` | Landesverfassung der Freien Hansestadt Bremen vom 21. Oktober 1947 (Neufassung vom 12. August 2019) | 37 versions, from 22 October 1947 to today |
| one folder per act | 158 Gesetze: the Stammgesetze in the portal's list of Gesetze und Rechtsverordnungen (amending acts and Ortsgesetze left out) | 1,376 versions |
| one folder per act | Verordnungen: the entries of that list whose title names a Verordnung (amending Verordnungen left out), 644 in all | every version the portal lists |

Of the 161 Stammgesetze in the portal's list, 3 are left out because their page gives no first day of validity (GrEStVG, BremBrexitÜG, BremFidatasG); a few single versions are left out too. They are listed under "Decisions made by hand" in REPRODUCE.md.

The Verordnungen are added in parts of 50, in list order, under the same rules; REPRODUCE.md names the parts published so far and the versions left out. Rechtsverordnungen titled otherwise ("...ordnung", such as Prüfungs- or Gebührenordnungen) and Verwaltungsvorschriften are not included.

## Source

The Vorschriften section of the [Transparenzportal Bremen](https://www.transparenz.bremen.de/vorschriften-72741): each act's current text, its "Frühere Fassungen" and its "Änderungshistorie". The sha256 of each page a version was read from is in `data/versions.json`.

## Dates

Each version is dated by the first day of validity the portal gives it ("gültig von"); the current version is dated the day after the newest earlier version ends. Commits are at noon in Bremen. Versions in force only after the retrieval date (30 October 2026) are on the `zukunft` branch.

## What "author" means

Each provision that differs from the version before is credited to the latest amendment in the portal's "Änderungshistorie" that names that provision (or says "mehrfach geändert") and is dated on or before the version's first day. The changes the Neufassung of 12 August 2019 shows are credited to that Bekanntmachung. A change with no such amendment is committed by the publisher and labelled unexplained. The committer is always Lexifina.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Each version page becomes one file per provision. Headings of Hauptteile and Abschnitte stand above the first provision under them. Numbered entries are one line each; tables are one line per row, cells separated by ` | `. Editorial notes the portal prints with a provision stay with it.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match the corpus; an independent letters-and-digits comparison of every version against its source page must show no difference. Results are in `REPRODUCE.md`.

## Limits

Credits are matched from the Änderungshistorie by provision number and date, so an amendment that names a provision only indirectly can be missed (then the change is labelled unexplained). The text is not the official version: only the Bremisches Gesetzblatt is authoritative.

## Licence

See [LICENSE](LICENSE): the law texts are free of copyright (§ 5 Abs. 1 UrhG). Quelle: Transparenzportal Bremen, Freie Hansestadt Bremen.
