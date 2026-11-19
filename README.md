# Deutschland: die Geschichte des Rechts in Git

**Deutsch** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/de/effort-dark.svg">
<img alt="Deutsches Recht in diesem Repository: Inhalt, Änderungen nach Jahr des Inkrafttretens, Vollständigkeit gegenüber den amtlichen Quellen und Richtigkeit des Enthaltenen" src="data/de/effort-light.svg" width="880">
</picture>

Das Recht Deutschlands als Git-Historie: Bundes-, Landes- und Ortsrecht, Gesetz- und Amtsblätter, Parlamentsdokumente und Gerichtsentscheidungen, eine Datei je Norm oder Dokument, ein Commit je Fassung oder amtlichem Dokument an seinem Tag (Inkrafttreten, Ausgabe, Sitzung oder Entscheidung), und als Autor des Commits das Gesetz oder die Stelle, von der es stammt. `git blame` nennt zu jeder Zeile das Gesetz, das sie geschrieben hat; `git log` listet jede Änderung einer Vorschrift auf; ein gewähltes Datum ergibt den an diesem Tag geltenden Text.

Teil von [lexifina/global-law](https://github.com/lexifina/global-law), einer Git-Historie für das Recht jedes Landes: global-law liest aus diesem Repository das Bundesrecht unter `germany/bund/acts/` ein.

**Was es jetzt enthält:** rund 6,7 Millionen Commits (19. November 2026): das Grundgesetz seit 1949, jede Rechtsvorschrift des Bundes seit 2019 (für rund 2.000 auch ältere Fassungen) und das Bundesgesetzblatt seit 1949 ([`grundgesetz/`](grundgesetz/), [`bund/`](bund/)); das konsolidierte Landesrecht von sieben Ländern und die Gesetzblätter und Landtagsdokumente der meisten ([`laender/`](laender/)); Entscheidungen der Bundesgerichte und von Gerichten in zehn Ländern ([`rechtsprechung/`](rechtsprechung/)); Drucksachen und Plenarprotokolle des Bundestages seit 1949 und des Bundesrates seit 2000 ([`bundestag/`](bundestag/), [`bundesrat/`](bundesrat/)); Ortsrecht und Ratsinformationen der Gemeinden ([`kommunen/`](kommunen/)); und vier historische Verfassungen ([`historisch/`](historisch/)). Die Quelle jedes Teils: [`REPRODUCE.md`](REPRODUCE.md).

Das Grundgesetz liegt in `grundgesetz/artikel/`, eine Datei je Artikel (`109.md` ist Artikel 109, Haushaltswirtschaft in Bund und Ländern); jede andere Rechtsvorschrift des Bundes ist ein Ordner in `bund/gesetze/`, benannt wie auf Gesetze im Internet, mit einer Datei je Norm (`bund/gesetze/burlg/0003.md` ist § 3 des Bundesurlaubsgesetzes). Bis zum 17. November 2026 lagen diese Ordner in der obersten Ebene des Repositoriums (`burlg/`); `git log --follow` folgt der Verschiebung, und [`data/paths.json`](data/paths.json) nennt zu jedem alten Ordner den neuen.

Der Text ist deutsch, so wie seine Quellen ihn veröffentlichen. Eine englische Übersetzung ist nicht Teil dieses Bestands.

## Fragen als Git-Befehle

| Frage | Befehl |
| --- | --- |
| Jede Änderung von Artikel 109 des Grundgesetzes | `git log -p --word-diff -- grundgesetz/artikel/109.md` |
| Welches Änderungsgesetz hat jede Zeile von Artikel 109 geschrieben? | `git blame grundgesetz/artikel/109.md` |
| Jede Fassung von Artikel 109, mit dem Tag ihres Inkrafttretens | `git log --format="%h %(trailers:key=In-Kraft,valueonly,separator=) %an" -- grundgesetz/artikel/109.md` |
| Artikel 109 in der am 1. Januar 2025 geltenden Fassung | `python tools/stand_am.py 2025-01-01 109` |

**Außerhalb von Git** stellen wir diesen Bestand auch öffentlich und kostenlos bereit:

- **[Claude zum deutschen Recht fragen](https://global-law.lexifina.com/v1/try_claude?country=germany)**: öffnet Claude mit einer vorbereiteten ersten Frage.
- **[ChatGPT fragen](https://global-law.lexifina.com/v1/try_chatgpt?country=germany)**: dieselbe Frage in ChatGPT.
- **[Im deutschen Recht auf unserer Website suchen](https://lexifina.com/law?country=germany&q=Jahresurlaub)**: eine Suche nach „Jahresurlaub“, mit dem Text jeder Vorschrift und ihren Fassungen, ohne Konto.
- **[REST-API für Entwickler](https://global-law.lexifina.com/v1/search_law?query=Jahresurlaub&jurisdiction=germany)**: dieselbe Suche als JSON, ohne Schlüssel. Die [Dokumentation steht hier](https://lexifina.com/api/global-law).

Beide Assistenten lesen den Bestand über den kostenlosen Global-law-Connector (MCP, `https://global-law.lexifina.com/mcp`); beim ersten Mal gibt der Chat Ihnen den Link, mit dem er hinzugefügt wird. Fragen Sie auf Deutsch oder auf Englisch.

**Einfach selbst betreiben.** Es braucht nur Git und Python, und die Werkzeuge laufen auf Ihrem Rechner:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add germany/bund/acts
python3 tools/law.py show 2026-01-01 germany/bund/acts/grundgesetz/artikel/109.md
```

In Claude Code, Cursor, VS Code oder Codex geöffnet, startet der Klon auch einen lokalen MCP-Server mit denselben Werkzeugen ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Daten

Jeder Commit des Grundgesetzes und des Bundesrechts ist auf 12 Uhr Berliner Zeit (Europe/Berlin) an dem Tag datiert, an dem die Fassung in Kraft trat, und trägt diesen Tag in seinem Trailer `In-Kraft:`; die übrigen Teile sind auf den Tag ihres Dokuments datiert (Ausgabe, Sitzung, Entscheidung oder Beginn der Gültigkeit):

- beim Grundgesetz der Tag, an dem jedes Änderungsgesetz in Kraft trat, und, soweit bekannt, die Tage, an denen es beschlossen, ausgefertigt und verkündet wurde (`Beschlossen:`, `Ausgefertigt:`, `Verkuendet:`); bestimmt ein Gesetz keinen Tag, tritt es nach Art. 82 Abs. 2 GG am vierzehnten Tag nach Ausgabe des Bundesgesetzblattes in Kraft;
- beim übrigen Bundesrecht der Tag, an dem die Änderung zuerst auf Gesetze im Internet erschien, das Änderungen mit ihrem Inkrafttreten konsolidiert (das Archiv las es bis Mai 2020 wöchentlich, seitdem täglich); geben die Fußnoten des Gesetzes einen früheren Tag des Inkrafttretens an (`mWv 21.5.2003`), trägt der Commit zusätzlich `In-Kraft-laut-Fussnote:`;
- Git kann keine Daten vor 1970 speichern, daher sind Commits für frühere Tage ab dem 1970-01-01 datiert, Sekunden auseinander; der tatsächliche Tag steht beim Grundgesetz in `In-Kraft:` und in den Tags `in-kraft/YYYY-MM-DD`, sonst am Anfang der Betreffzeile. Ein Datum fragen Sie mit `tools/stand_am.py` ab, nicht mit `git log --before`.

Jede Änderung wird dem Gesetz zugeschrieben, das sie vorgenommen hat: `69. Änderung (2025)` für das 69. Gesetz zur Änderung des Grundgesetzes oder `G v. 22.12.2025 I Nr. 371` beim Bundesrecht, wie der Standvermerk des Gesetzes es nennt. Änderungen, die kein Gesetz erklärt, werden gekennzeichnet und nie einem Gesetz zugeschrieben: `Gesetze im Internet (Bestand)` für den ersten Stand von 2019, `Textänderung ohne neue Standangabe` (1.160 der 3.232 Bundesrechts-Commits des ersten Aufbaus), `Neu aufgenommen` und `Nicht mehr veröffentlicht`.

## Wie es geprüft wird

- Der Endtext des Grundgesetzes stimmt Artikel für Artikel mit dem heutigen amtlichen Text auf Gesetze im Internet überein. Der Text von DocPatch wich in 43 Artikeln davon ab; der amtliche Text ersetzt ihn ab der letzten Änderung des jeweiligen Artikels, und jede Korrektur ist in [`grundgesetz/KORREKTUREN.md`](grundgesetz/KORREKTUREN.md) aufgeführt.
- Die Daten des 64. bis 69. Änderungsgesetzes wurden anhand des jeweiligen Gesetzes im Bundesgesetzblatt überprüft.
- Der erste Aufbau ist deterministisch: Die Befehle in [`REPRODUCE.md`](REPRODUCE.md) ergeben seine 3.304 Gesetzes-Commits (Grundgesetz und Bundesrecht bis zum 28. Oktober 2026) mit denselben Hashes.
- Die Historie wird nur fortgeschrieben: Spätere Läufe fügen Commits obenauf hinzu, und nichts wird umgeschrieben; Rücknahmen und Berichtigungen sind eigene, gekennzeichnete Commits (`Kind: withdrawal`, `Kind: correction`).
- [vulnerabilities/](vulnerabilities/): mögliche Redaktionsfehler im deutschen Bundesrecht, von den Detektoren von global-law gefunden und von Hand geprüft.

## Was es nicht zeigt

- **Das ganze Bundesrecht vor dem 10. Juni 2019**, außer dem Grundgesetz. Gesetze im Internet hält nur den geltenden Text vor; ältere Fassungen von rund 2.000 Gesetzen sind aus dem Bundesgesetzblatt rekonstruiert ([`bund/fassungen-vor-2019/`](bund/fassungen-vor-2019/)), oft nur wenige Fassungen zurück.
- **Am Bundesgesetzblatt geprüfte ältere Fassungen des Grundgesetzes.** Die Fassungen eines Artikels vor seiner letzten Änderung vor 2019 sind die Transkription von DocPatch.
- **Den genauen Tag des Inkrafttretens** einer bundesrechtlichen Änderung, wo die Fußnoten ihn nicht angeben, und die Stufen eines Gesetzes, das unter einem Standvermerk in mehreren Schritten in Kraft tritt.
- **Fußnoten und Bilder.** Fußnoten sind weggelassen; Bilder sind als `[Bild: …]` markiert.
- **Das konsolidierte Landesrecht der übrigen neun Länder** (ihre Gesetzblätter liegen hier, außer denen des Saarlandes und Sachsen-Anhalts), **EU-Recht und das Ortsrecht der meisten Gemeinden.** Gesperrte oder nicht frei zugängliche Quellen nennt [`REPRODUCE.md`](REPRODUCE.md).

## Quellen

| Quelle | Art | Frühere Fassungen | Anmerkungen |
| --- | --- | --- | --- |
| [Gesetze im Internet](https://www.gesetze-im-internet.de) (Bundesministerium der Justiz) | Amtlicher konsolidierter Text des Bundesrechts | nein, nur der geltende Text | Jede Rechtsvorschrift und das Grundgesetz ab 2019; maßgeblich ist allein das Bundesgesetzblatt |
| [QuantLaw/gesetze-im-internet](https://github.com/QuantLaw/gesetze-im-internet) | Archiv von Gesetze im Internet | ja, wöchentlich ab 10. Juni 2019, täglich ab Mai 2020 | Herkunft der früheren Fassungen der Bundesgesetze |
| [DocPatch](https://github.com/c3e/grundgesetz-dev) | Das Grundgesetz von 1949 und sein 1. bis 63. Änderungsgesetz, als Patches | ja, jede Fassung | Mit Daten, Unterzeichnern, Fundstellen und Abstimmungsergebnissen |
| [Deutscher Bundestag, Datenhandbuch](https://www.bundestag.de/datenhandbuch) | Daten des 64. bis 69. Änderungsgesetzes | | Am Bundesgesetzblatt überprüft |
| Die Herausgeber der weiteren Teile (Gesetzblätter, Parlamente, Gerichte, Räte, Städte) | Gesetzblätter, Parlamentsdokumente, Entscheidungen, Ortsrecht | wie veröffentlicht | Jede Quelle mit Zugang und Bedingungen in [`REPRODUCE.md`](REPRODUCE.md) und [`LICENSE`](LICENSE) |

## Lizenz

Siehe [`LICENSE`](LICENSE). Gesetze, Verordnungen, amtliche Bekanntmachungen und Gerichtsentscheidungen sind nicht urheberrechtlich geschützt (§ 5 Abs. 1 UrhG); anderes Material behält die Bedingungen seiner Quelle (darunter CC BY-SA 3.0 DE für DocPatch, BSD-3-Clause für QuantLaw, die Datenlizenz Deutschland und ein Bibliotheksscan zur nicht kommerziellen Nutzung), alle in `LICENSE` aufgeführt. Lexifinas eigene Arbeit wird unter CC0 1.0 veröffentlicht.

Der Rechtstext stammt aus den Quellen (Scans per OCR, gekennzeichnet); ein KI-Modell hat die Skripte geschrieben und die gekennzeichneten Berichtigungen erarbeitet, jede mit ihrem Beleg (siehe [`REPRODUCE.md`](REPRODUCE.md)).

Dies ist eine Übersetzung der englischen Fassung ([README.en.md](README.en.md)); bei Abweichungen gilt die englische Fassung.

## Visualisierungen

- [visualisations/](visualisations/): Diagramme aus diesem Repository. Noch nicht gezeichnet.

## Mehr

Aus dem Repository [lexifina/global-law](https://github.com/lexifina/global-law) (auf Englisch):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): alle Funktionen und was jedes Korpus unterstützen muss (`git blame`, `law.py`, MCP-Werkzeuge)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): Fragen und Antworten · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): Änderungen vorschlagen · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): MCP-Server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): wie es erstellt wurde · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): wie aktuell jedes Korpus ist · [Überwachung](https://github.com/lexifina/global-law/tree/main/monitoring): ob die Aktualisierungen funktionieren · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): wie jede amtliche Quelle auf Änderungen überwacht wird
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): wie schnell die Werkzeuge sind, gemessen
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): Diagramme und Verbindungen im Recht der ganzen Welt
- [Schwachstellen](https://github.com/lexifina/global-law/tree/main/vulnerabilities): Fehler in Rechtsakten, wie sie veröffentlicht wurden
