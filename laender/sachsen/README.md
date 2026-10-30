# Saxony: law history in git

The law of the Free State of Saxony (Freistaat Sachsen) as a git history: one file per Artikel or Paragraph, one paragraph per line, one commit per amending act on the day the new version took effect. `git blame` names the act behind each change; `git log` lists every change; picking a date gives the text in force that day. The text is German.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

Every version of each act that REVOSax keeps under "Historische Fassungen", from the oldest it holds to the current one. For the Verfassung that is the whole history since 1992; for most other acts the history starts with the oldest version REVOSax holds (often from the 2000s), which is credited to the publisher as "oldest version available".

| Folder | Act | History |
| --- | --- | --- |
| `verfassung/` | Verfassung des Freistaates Sachsen vom 27. Mai 1992 | every version since 6 June 1992 |
| other folders | Saxon Gesetze, one folder per act (named by its abbreviation) | every version REVOSax holds |
| other folders | Saxon Verordnungen, one folder per act (named by its abbreviation, or `vorschrift-<REVOSax id>` where it has none), added in parts | every version REVOSax holds |

Verwaltungsvorschriften are not included yet.

## Source

[REVOSax - Recht und Vorschriftenverwaltung Sachsen](https://www.revosax.sachsen.de), the Saxon State Government's database of Saxon law: the current and the historical versions of each act. The sha256 of each page a version was read from is in `data/versions.json`.

## Dates

Each version is dated by the day REVOSax gives as the start of its validity ("Fassung gültig ab"), at noon in Dresden. Versions in force only after the retrieval date (30 October 2026) are on the `zukunft` branch.

## What "author" means

A provision that changed between two versions is credited to the amending act its footnotes name ("... geändert durch Gesetz vom ... (SächsGVBl. S. ...)"), taking the latest such act dated on or before the version's first day. That act is the commit's author, with an e-mail address that cannot exist. A change whose footnotes name no act is committed by the publisher and labelled unexplained. The committer is always Lexifina.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Each REVOSax version page becomes one file per provision. Headings of Teile and Abschnitte stand above the first provision under them. Footnote markers and the sentence numbers REVOSax adds are left out; tables are one line per row, cells separated by ` | `.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match the corpus; an independent letters-and-digits comparison of every version against its source page must show no difference. Results are in `REPRODUCE.md`.

## Limits

History only as far back as REVOSax holds it; the acts as enacted are not here unless REVOSax keeps the original version. Credits come from REVOSax's footnotes, which name the amending act but not always the provision of it that made the change. The text is not the official version: only the Sächsisches Gesetz- und Verordnungsblatt is authoritative.

## Licence

See [LICENSE](LICENSE): the law texts are free of copyright (§ 5 Abs. 1 UrhG). Quelle: REVOSax - Recht und Vorschriftenverwaltung Sachsen, Sächsische Staatskanzlei.
