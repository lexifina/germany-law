# Bavaria: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Bavaria, Germany, which global-law reads at `germany/bavaria/acts/`.

The law of the Free State of Bavaria (Freistaat Bayern) as a git history: generally one file per Artikel or Paragraph, with each of the nine Verwaltungsvorschriften in one text file. The text is German, the only official language.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

**Current text only, not yet a history.** BAYERN.RECHT publishes only the consolidated version of each act that is in force, so each act is one commit holding its whole current text, dated by the day that version came into force and credited to the publisher ("oldest version available"), not to an amending law. For Gesetze and Rechtsverordnungen, `000-titel.md` keeps the list of amending acts the portal prints.

| Folder | Act | Versions |
| --- | --- | ---: |
| `bayverf/` | Verfassung des Freistaates Bayern (BayRS 100-1-I) | 1 |
| other folders | the Bavarian Gesetze listed by BAYERN.RECHT, one folder per act (by its document id, e.g. `baybo/`) | 1 each |
| other folders | the Bavarian Rechtsverordnungen listed by BAYERN.RECHT (486), one folder per act (by its document id, e.g. `bayabfzustv/`) | 1 each |
| `bayvwv*` and `bayvv-*` folders | nine Bavarian Verwaltungsvorschriften from BAYERN.RECHT, each with the complete current XML body in one text file | 1 each |

Other Verwaltungsvorschriften and Staatsverträge are not included yet.

## Source

[Bürgerservice BAYERN.RECHT](https://www.gesetze-bayern.de) of the Bayerische Staatskanzlei: the consolidated Bavarian law, prepared by Verlag C.H.Beck on behalf of the Free State. Each act's XML download is the source; its sha256 is recorded with each version in `data/versions.json`.

## Dates

Each version is dated by the day BAYERN.RECHT says its consolidated text applies from ("Text gilt ab"), at noon in Munich; where it gives none, by the Ausfertigung date. For some acts that day is earlier than the last amending act the portal lists; the portal's date is kept as given. Versions in force only after the retrieval date (30 October 2026) are on the `zukunft` branch.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The XML of each act becomes one file per provision. Headings of the Teile and Abschnitte stand above the first provision under them. Footnotes and the sentence numbers the portal adds are left out; tables are one line per row, with cells separated by ` | `; images are left out.

## How it is checked

Every version is read back from git on the day it took effect (`tools/check_repo.py`) and must match the corpus; an independent letters-and-digits comparison of every act against the source XML must show no difference. Results are in `REPRODUCE.md`.

## What "author" means

The author of each commit is the publisher (BAYERN.RECHT), with an e-mail address that cannot exist; the committer is always Lexifina.

## Limits

Only the current consolidated text is here: no earlier versions, and not the acts as enacted. The text is not the official version: only the Bayerisches Gesetz- und Verordnungsblatt is authoritative. Footnotes are left out.

## Licence

See [LICENSE](LICENSE): the law texts are free of copyright (§ 5 Abs. 1 UrhG) and BAYERN.RECHT's terms allow their unrestricted reuse, commercial or not. Quelle: Bürgerservice BAYERN.RECHT, Bayerische Staatskanzlei.
