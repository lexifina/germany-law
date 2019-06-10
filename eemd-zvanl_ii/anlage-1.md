# Anlage 1 zum Vertrag über die Durchführung des Europäischen elektronischen Mautdienstesauf Bundesfernstraßen im Geltungsbereich des Bundesfernstraßenmautgesetzes(EETS-Zulassungsvertrag)

Zusatzvereinbarung
zwischen
der Bundesrepublik Deutschland, vertreten durch das Bundesministerium für Verkehr und digitale Infrastruktur (BMVI), dieses vertreten durch das Bundesamt für Güterverkehr (BAG), Werderstraße 34, 50672 Köln, dieses wiederum vertreten durch seinen Präsidenten
– Mauterheber –
und
[Name Anbieter], [Adresse Anbieter], vertreten durch [Vertretung Anbieter], [registriert gemäß Artikel 3 der Entscheidung 2009/750/EG in …] [Nachweis der Registrierung]
– Anbieter –
Inhaltsverzeichnis
1 Vorbemerkung
2 Schnittstellen – Übermittlungsfristen
3 Bereitstellung von EETS-Fahrzeuggeräten
1 Vorbemerkung
Diese Zusatzvereinbarung ergänzt den Vertrag über die Durchführung des Europäischen elektronischen Mautdienstes auf Bundesfernstraßen im Geltungsbereich des Bundesfernstraßenmautgesetzes (EETS-Zulassungsvertrag).
In der in § 1 Absatz 2 des EETS-Zulassungsvertrags in Bezug genommenen EEMD-Gebietsvorgabenverordnung sind in Anlage 1 Nummer 2 Schnittstellen benannt, über die das Teilsystem des EETS-Anbieters verfügen und gemäß den Vorgaben des Mauterhebers bedienen muss. Vorgaben für die Schnittstellen mit IT-Unterstützung stellt der Mauterheber durch die entsprechenden Spezifikationen der Datenobjekte und der jeweiligen Schnittstellen zur Übertragung der Datenobjekte öffentlich zur Verfügung (Schnittstellenspezifikationen).
2 Schnittstellen – Übermittlungsfristen
Die untenstehenden Übermittlungsfristen zu den genannten Schnittstellen gelten unmittelbar und ergänzen die Schnittstellenspezifikation SST 001 bzw. konkretisieren einige der in den Spezifikationen genannten Richtwerte der Schnittstellenspezifikationen SST 001, 002, 006, 007 und 008.
SST 001, Blacklist (Dokument 4.3.2_EETS_SST_001, Kapitel Kommunikationsabläufe):
Die Übertragung der EETS-Blacklist vom EETS-Anbieter an den Mauterheber erfolgt periodisch. Das Zeitintervall, nach dem eine erneute Übertragung stattfinden muss, beträgt maximal 24 Stunden. Die Häufigkeit wird über den Parameter „SST001-Aufruffrequenz“ angegeben (Übermittlung einmal pro Tag. Dadurch ist gewährleistet, dass die aktuellen Sperrinformationen zeitnah weiterverarbeitet werden können).
SST 002a, Whitelist (Dokument 4.3.3_EETS_SST_002, Kapitel Kommunikationsabläufe):
Die Whitelist wird periodisch an das EETS-Teilsystem des Mauterhebers übermittelt. Die Häufigkeit der Übertragung ist über den Parameter „SST002a-Aufruffrequenz“ (Übermittlung aufgrund der großen Datenmengen frühestens alle vier Stunden, spätestens alle 24 Stunden, um die Aktualität der Daten zu gewährleisten) gegeben.
SST 006, abschnittsbezogene Erhebungsdaten (Dokument 4.3.4_EETS_SST_006, Kapitel Kommunikationsabläufe):
Der EETS-Anbieter soll regelmäßig die abschnittsbezogenen Erhebungsdaten übertragen, wobei die Häufigkeit über den Parameter „SST006-Aufruffrequenz“ (Übermittlung alle 24 Stunden) gegeben ist. Dies gilt auch, wenn die maximale Anzahl für ein Transaktions-Paket noch nicht erreicht ist. Die Zeitdauer zwischen Befahrung eines mautpflichtigen Abschnitts und dem Eingang der entsprechenden abschnittsbezogenen Erhebungsdaten beim Mauterheber ist durch den Parameter „SST006-Übermittlungsfrist“ (maximal 72 Stunden) gegeben.
SST 007, Mautbuchungsnachweise (Dokument 4.3.5_EETS_SST_007, Kapitel Kommunikationsabläufe):
Der EETS-Anbieter soll regelmäßig die Mautbuchungsnachweise übertragen, wobei die Häufigkeit über den Parameter „SST007-Aufruffrequenz“ (Übermittlung alle 24 Stunden) gegeben ist. Dies gilt auch, wenn die maximale Anzahl für ein Transaktions-Paket noch nicht erreicht ist. Die Zeitdauer zwischen erfolgreicher Übermittlung der abschnittsbezogenen Erhebungsdaten und dem Eingang der Mautbuchungsnachweise, in denen darauf referenziert wird, ist durch den Parameter „SST007-Übermittlungsfrist“ (maximal 72 Stunden) gegeben.
SST 008, Tagesberichte (Dokument 4.3.6_EETS_SST_008, Kapitel Kommunikationsabläufe):
Die Häufigkeit der Übermittlung des Tagesberichts ist über den Parameter „SST008-Aufruffrequenz“ (werktäglich) gegeben. Das gilt auch in den Fällen, in denen keine Auskehr vom EETS-Anbieter vorgenommen wurde.
[…]
Dabei ist zu berücksichtigen, dass alle Berichte am auf den Stichtag folgenden Werktag übermittelt werden müssen. Die Zeitdauer zwischen Beginn des auf den Stichtag folgenden Werktages und Eingang des Tagesberichts beim Mauterheber ist durch den Parameter „SST008-Übermittlungsfrist“ (maximal 15 Stunden) gegeben.
3 Bereitstellung von EETS-Fahrzeuggeräten
Sofern der Anbieter durch den Mauterheber zugelassen wurde oder sich in der Phase 3 (Pilotbetrieb) befindet, muss er dem Mauterheber unaufgefordert fünf (5) EETS-Fahrzeuggeräte, die jeweils den im Produktivsystem eingesetzten Software- und Hardwarestand aufweisen zur Verfügung stellen. Der Mauterheber wird die EETS-Fahrzeuggeräte dem Mautbetreiber (Toll Collect) bereitstellen, damit dieser sie bei Bedarf im Rahmen von Tests zur Sicherstellung der Rückwirkungsfreiheit der EETS-Fahrzeuggeräte auf die Kontrolleinrichtungen des Mautbetreibers (Toll Collect) verwenden kann. Der EETS-Anbieter ist für die Wartung und Instandhaltung der EETS-Fahrzeuggeräte verantwortlich.
