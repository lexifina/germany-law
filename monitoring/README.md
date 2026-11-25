<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Beobachtung: was gelesen wird und was daraus folgte

[English](README.en.md)

Wie global-law jedes Land beobachtet: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Diese Seite zeigt dasselbe nur für Deutschland: jedes Lesen einer amtlichen Quelle, wann, und was daraus folgte (Vorschriften hinzugefügt, geändert und entfernt). Maschinenlesbar in [data/checks/](../data/checks/) (JSON Lines, Schema `lexifina-check/1`), in `git log` als Commits mit `Kind: check` und Monat für Monat in [checks/](checks/).

**Letzte Prüfung:** 2026-11-25 07:00 UTC, Gesetze im Internet (Bundesministerium der Justiz): 7072 Adressen gelesen; 3 hinzugefügt, 28 geändert, 3 entfernt; Änderungen gefunden; 14 nicht veröffentlicht, davon 0 ohne Grund. Hinweise: `verify-differ`.

## Quellen

| Quelle | Ordner | Wie oft | Letzte erfolgreiche Prüfung | Letztes Ergebnis | Stand |
| --- | --- | --- | --- | --- | --- |
| [Gesetze im Internet (Bundesministerium der Justiz)](https://www.gesetze-im-internet.de) | `bund/gesetze/`, `grundgesetz/` | täglich | 2026-11-25 07:00 UTC | Änderungen gefunden | beobachtet |

## Die letzten 30 Tage

| Beginn (UTC) | Quelle | Gelesen | Hinzugefügt | Geändert | Entfernt | Nicht veröffentlicht (ohne Grund) | Ergebnis | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-25 05:01](checks/2026-11.md#de-gii-20261125t050103z) | gii | 7072 | 3 | 28 | 3 | 14 (0) | Änderungen gefunden `verify-differ` | [3](https://github.com/lexifina/germany-law/compare/5dabc17ee120...b6a371018158) |
| [2026-11-24 05:08](checks/2026-11.md#de-gii-20261124t050802z) | gii | 7054 | 1 | 12 | 1 | 8 (0) | Änderungen gefunden `audit-disagrees` | [4](https://github.com/lexifina/germany-law/compare/42644a9080d2...b54399c9f0a8) |
| [2026-11-23 21:34](checks/2026-11.md#de-gii-20261123t213453z) | gii | 7038 | 0 | 0 | 0 | 4 (0) | keine Änderung `verify-differ` `audit-disagrees` | — |
| [2026-11-23 17:42](checks/2026-11.md#de-gii-20261123t174212z) | gii | 7077 | 0 | 0 | 0 | 8 (0) | Änderungen gefunden `audit-disagrees` | [4](https://github.com/lexifina/germany-law/compare/a629f1a377f6...860263ebb5fe) |

## Selbst prüfen

```
python tools/checktrail.py                      # die letzte Prüfung jeder Quelle
python tools/checktrail.py --day 2026-11-23     # jede Prüfung eines Tages
python tools/checktrail.py --act <id>           # wann eine Vorschrift gesehen und veröffentlicht wurde
git log --grep='^Kind: check' --format='%ci %s'  # die Prüfungen in der Historie
```

Rechtskraft hat nur die amtliche Verkündung; die Texte hier sind Kopien zum Lesen und Suchen.
