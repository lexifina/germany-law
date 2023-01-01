# Anlage Vorgaben für das elektronische Belegverfahren

1 Allgemeine Vorgaben zum Ausfüllen des Abgabebelegs
1.1 Für jeden Teil des Abgabebelegs werden auf der Internetseite des Bundesinstituts für Arzneimittel und Medizinprodukte (BfArM) Musterdateien zur Verfügung gestellt.
1.2 Abgabebeleg-Nummern
1.2.1 Jeder Abgabebeleg ist mit einer Abgabebeleg-Nummer zu versehen.
1.2.2 Die Abgabebeleg-Nummern sind achtstellig und mit führenden Nullen anzugeben.
1.2.3 Die Bundesopiumstelle des BfArM teilt jedem Abgebenden auf Anforderung einen Nummernkreis zu, der den Bedarf des Abgebenden nach dem für ihn zu erwartenden Umfang des Betäubungsmittelverkehrs für mindestens drei Jahre deckt. Nachdem der zugeteilte Nummernkreis aufgebraucht wurde, kann er erneut verwendet werden.
1.3 Vorgaben zur Angabe spezifischer Daten
1.3.1 Das Abgabedatum ist sechsstellig mit führenden Nullen im Format TTMMJJ anzugeben.
1.3.2 Die BtM-Nummer des Abgebenden ist siebenstellig und mit führenden Nullen anzugeben.
1.3.3 Die Pharmazentralnummer ist achtstellig und mit führenden Nullen anzugeben.
1.3.4 Die BtM-Nummer des Erwerbers ist siebenstellig und mit führenden Nullen anzugeben.
1.3.5 Die Anzahl der abgegebenen Betäubungsmittel darf maximal fünfstellig sein und ist ohne führende Nullen anzugeben.
1.3.6 Die Packungseinheit gemäß verwendeter Pharmazentralnummer ist maximal vierstellig und ist ohne führende Nullen anzugeben.
2 Allgemeine Vorgaben für die Signierung und Übermittlung von Abgabemeldungen und Lieferscheindoppeln
2.1 In Abgabemeldungen sind elektronisch die Unterschrift sowie der Name der abgebenden Person in Klartext einzufügen.
2.2 Abgabemeldungen sind in dem nach Nummer 2.3 zu verwendenden elektronischen Format über einen File-Transfer-Protocol-Zugang (FTP-Zugang) an das BfArM wöchentlich zu übermitteln.
2.3 Vorgaben zur Form und Dateigröße
2.3.1 Abgabemeldungen und Lieferscheindoppel sind in Form von PDF-Dateien im A4-Format zu übermitteln.
2.3.2 Abgabemeldungen und Lieferscheindoppel haben dem Format der nach Nummer 1.1 zur Verfügung gestellten Musterdateien hinsichtlich Layout, Beschriftung, Schriftart und Schriftgrad zu entsprechen.
2.3.3 Die Dateigröße der Abgabemeldung darf jeweils 30 KB nicht überschreiten.
3 Spezifische Vorgaben für die Übermittlung von Abgabemeldungen
3.1 Vorgaben zu den PDF-Dateien
3.1.1 Die Dateinamen der PDF-Dateien haben sich aus der Abgabebeleg-Nummer, einer nachfolgenden vierstelligen laufenden Nummer und der Dateinamenerweiterung „.pdf“ zusammenzusetzen (zum Beispiel 000000010001.pdf, 000000020002.pdf etc.).
3.1.2 Die PDF-Dateien sind in einem Ordner zusammenzufassen.
3.1.3 Die vierstellige laufende Nummerierung der PDF-Dateien hat in jedem neuen Ordner wieder mit 0001 zu beginnen.
3.2 Vorgaben zu den Ordnern
3.2.1 Die Namen der in Nummer 3.1.2 genannten Ordner haben sich aus der BtM-Nummer des Abgebenden sowie einer fortlaufenden dreistelligen Nummer (zum Beispiel 0012345001 für den nach Verfahrensbeginn ersten übermittelten Ordner, 0012345002 für den zweiten übermittelten Ordner) zusammenzusetzen.
3.2.2 Von jedem Ordner ist eine ZIP-Datei mit gleichem Namen zu erzeugen (zum Beispiel 0012345001.zip).
3.2.3 Die ZIP-Datei hat zusätzlich den Ordnernamen als Pfad zu enthalten.
3.3 Rahmenbedingungen für die Übermittlung von ZIP-Dateien
3.3.1 Für die wöchentliche Übermittlung der in Nummer 3.2.2 genannten ZIP-Dateien wird vom BfArM ein FTP-Zugang über einen FTP-Server zur Verfügung gestellt.
3.3.2 Für jeden Abgebenden wird auf dem FTP-Server des BfArM ein Konto eingerichtet, auf das mittels Benutzerkennung und Passwort nur dieser Abgebende und das BfArM Zugriff haben.
3.3.3 Benutzerkennung und Passwort werden vom BfArM auf Anforderung mitgeteilt.
4 Spezifische Vorgaben für die Übermittlung von Lieferscheindoppeln
4.1 Vorgaben zu den PDF-Dateien
4.1.1 Die Dateinamen der PDF-Dateien haben sich aus den vorausgehenden Großbuchstaben „LD“, der Abgabebeleg-Nummer, einer nachfolgenden vierstelligen laufenden Nummer und der Dateinamenerweiterung „.pdf“ zusammenzusetzen (zum Beispiel LD000000010001.pdf, LD000000020002.pdf etc.).
4.1.2 Die PDF-Dateien sind in einem Ordner zusammenzufassen.
4.1.3 Die vierstellige laufende Nummerierung der PDF-Dateien hat in jedem neuen Ordner wieder mit 0001 zu beginnen.
4.2 Vorgaben zu den Ordnern
4.2.1 Die Namen der in 4.1.2 genannten Ordner haben sich aus den vorangehenden Großbuchstaben „LD“, der BtM-Nummer des Abgebenden sowie einer fortlaufenden dreistelligen Nummer (zum Beispiel LD0012345001 für den nach Verfahrensbeginn ersten übermittelten Ordner, LD0012345002 für den zweiten übermittelten Ordner) zusammenzusetzen.
4.2.2 Von jedem Ordner ist eine ZIP-Datei mit gleichem Namen zu erzeugen (zum Beispiel LD0012345001.zip).
4.2.3 Die ZIP-Datei hat zusätzlich den Ordnernamen als Pfad zu enthalten.
4.3 Rahmenbedingungen für die Übermittlung von ZIP-Dateien
Für die Übermittlung der in Nummer 4.2.2 genannten ZIP-Dateien ist der FTP-Zugang zu nutzen, der für die Übermittlung von in Nummer 3.2.2 genannten ZIP-Dateien genutzt wird.
