# Anlage - Schnittstellenbeschreibung für die Datenübernahme von Insolvenzverwalterinnen und Insolvenzverwaltern in gerichtliche Systeme
Anlage
(zu § 2 Absatz 1 und 2)
Schnittstellenbeschreibung für die Datenübernahme von Insolvenzverwalterinnen und Insolvenzverwaltern in gerichtliche Systeme
1. Einleitung
Diese Anlage entspricht der „Schnittstellenbeschreibung für die Datenübernahme von Insolvenzverwaltern in gerichtliche Systeme“ der Bund-Länder-Kommission für Informationstechnik in der Justiz in Version 01.000c mit Stand 23. Mai 2019.
2. Datenübersicht
Die Schnittstelle beinhaltet die folgenden Entitäten:
- Forderungsanmeldungen
- Gläubiger
- Vertreter des Gläubigers
- Mitglieder einer Gläubigermehrheit
- Vertreter eines Mitglieds (einer Gläubigermehrheit)
- Erklärung des Verwalters zur Forderungsanmeldung
- Debitor
- Vertreter des Debitors
- Abstimmungsgruppen
Für diese Entitäten gilt das folgende Beziehungsdiagramm, wobei 1:n bedeutet, dass ein Datensatz der linken Entität mit mehreren Datensätzen der rechten Entität verknüpft ist. Beispiel: Ein Gläubiger kann mehrere Forderungen anmelden.
In der Entität Gläubiger werden die personenbezogenen Daten aller Gläubiger und Gläubigermehrheiten erfasst.
Zu einem Gläubiger können in der Entität Vertreter des Gläubigers mehrere Vertreter mit Unterstrukturen erfasst werden.
In der Entität Mitglieder einer Gläubigermehrheit werden die personenbezogenen Daten der einzelnen Mitglieder erfasst.
Zu einem Mitglied einer Gläubigermehrheit können in der Entität Vertreter eines Mitglieds mehrere Vertreter mit Unterstrukturen erfasst werden.
Zu einem Gläubiger können in der Entität Forderungsanmeldung mehrere Forderungen erfasst werden.
In der Entität Erklärung kann der Verwalter mehrere Erklärungen zu jeder Forderungsanmeldung eintragen.
Für die Daten der Debitoren (Schuldner des Schuldners) und ihrer Vertreter sind die Entitäten Debitoren und Vertreter des Debitors vorgesehen.
Abstimmungsgruppen werden über die Entität Abstimmungsgruppe übergeben.
3. Festlegungen für die Datenübertragung
3.1 Dateiname
Pro Verfahren wird eine Textdatei übermittelt. Der Dateiname besteht aus 8 + 3 Zeichen; er darf keine Sonderzeichen enthalten.
Die letzten 3 Zeichen (Dateinamenerweiterung) dienen der Kennzeichnung als Insolvenzdatenübergabedatei und sind konstant mit ITR zu belegen.
Die ersten 8 Zeichen sind wie folgt zu codieren:
1. Zeichen: | Enthält eine Verarbeitungskennung und eine Zielangabe mit folgender Codierung: |  | 
 |  | A | Insolvenzverwalter -> Gericht
 |  | B | Gericht ->Insolvenzverwalter (z. Zt. noch ohne Bedeutung)
2.- 4. Zeichen: | Eindeutige Absenderkennung (wird vom Gericht vergeben) |  | 
5. - 8. Zeichen: | Laufende Nummer der Dateierzeugung auf Absenderseite |  | 
 | (Insolvenzverwalter bzw. Gericht); eindeutig codiert mit 00-99, AA-ZZ |  | 
Das gerichtliche Aktenzeichen ist nicht im Dateinamen, sondern im Anfangskennsatz enthalten.
Beispiel für einen Dateinamen: ANNN000A.ITR
(Es handelt sich um eine Insolvenzdatenübergabedatei, die vom Absender NNN stammt und die laufende Codierung 000A hat.)
3.2 Zeichensatz
Als Zeichensatz ist ISO-Latin-1 (ISO 8859-1) zu verwenden.
3.3 Übertragung
Eine Übertragung ist nach Maßgabe der geltenden Bestimmungen der Länder und des Bundes zum Elektronischen Rechtsverkehr möglich.
3.4 Aufbau der Schnittstellendatei
3.4.1 Versionskennung
Die Schnittstellendatei beginnt mit einer Versionskennung in der ersten Zeile mit folgendem Inhalt:
BLK-InsO-Austauschformat-(01.000c)-
Die Versionsangabe umfasst Major- (2 Ziffern), Minor- (3 Ziffern) und Bugfix-(Buchstabe) Angaben.
Die Versionskennung wird mit CR/LF (carriage return/linefeed) beendet.
3.4.2 Daten
Die Übertragung der Daten erfolgt satzweise. Dabei wird für jeden Datensatz aus den unter Punkt 2 beschriebenen Entitäten eine Zeile in der Schnittstellendatei gefüllt. Jeder Datensatz wird mit CR/LF (carriage return/linefeed) beendet.
Am Anfang jedes Satzes steht ein Satzkennzeichen, das die Zuordnung zu einer der o.g. Entitäten festlegt. Die Daten werden von einem Anfangs- und Endekennsatz eingerahmt. Folgende Satzkennzeichen werden dabei verwendet:
• 11 | Anfangskennsatz
• 20 | Forderungsanmeldung
• 30 | Gläubiger
• 40 | Mitglieder einer Gläubigermehrheit
• 50 | Vertreter des Gläubigers
• 55 | Vertreter eines Mitglieds
• 60 | Erklärung des Verwalters
• 70 | Debitor
• 75 | Vertreter des Debitors
• 80 | Abstimmungsgruppe
• 99 | Endekennsatz einschließlich Prüfsumme
Die einzelnen Felder eines Datensatzes werden durch ein Semikolon (;) voneinander getrennt (Trennzeichen).
Als Entwerterzeichenfindet der vorangestellte Backslash (\) Verwendung. Damit sind insbesondere Semikola oder CR/LF-Kombinationen in Bemerkungsfeldern zu entwerten. Soll ein Backslash als Dateninhalt übergeben werden, wird er selbst entwertet (\\).
Der Anfangskennsatz ist wie folgt aufgebaut:
Satzkennzeichen: | 11
Kennzeichen für den Typ der Schnittstellendatei: | ITR
Gerichtliches Aktenzeichen: | 43 IN 25/19
Absenderkennung (wird vom Gericht vergeben und entspricht der Kennung im Dateinamen) | NNN
Beispiel für einen Anfangskennsatz:
11;ITR;43 IN 25/19;NNN
Die einzelnen Datensätze sind wie folgt aufgebaut:
Satzkennzeichen: | 20 (bzw. 30, 40, 50, 55, 60, 70, 75, 80)
Feld 1 - n: | (siehe Punkt 3)
Der Endekennsatzist wie folgt aufgebaut:
Satzkennzeichen: |  | 99
Erstellungsdatum: |  | 28.03.2019
Erstellungsuhrzeit: |  | 10:00
Prüfsumme: | 45678 | 
Die Prüfsumme wird nach einem 32-Bit-CRC-Verfahren (vgl. Anlage) gebildet und umfasst alle Zeichen der Datei vom ersten Zeichen der Versionskennung bis zum letzten Zeichen vor der Prüfsumme (Semikolon nach der Erstellungsuhrzeit).
Beispiel für einen Endekennsatz:
99;28.03.2019;10:00;45678
3.4.3 Verschlüsselung
Ob und welche Verschlüsselungstechniken Verwendung finden, regeln die jeweiligen Landesjustizverwaltungen der Länder.
3.5 Regelungen zur Übergabe
Es ist stets der komplette Datenbestand eines Verfahrens zu übergeben.
Die gerichtsinterne Behandlung der übergebenen Daten (Überschreibung, Teilaktualisierung) hängt von dem jeweiligen Gerichtssystem ab.
4. Aufbau der Datensätze
4.1 Formatfestlegungen für Datenfelder
Mögliche Datentypen:
String(n): | Zeichenkette mit n Zeichen (max. 255 Zeichen) | 
Integer: | Ganze Zahl im Bereich von -32.768 bis 32.767 | 
Long: | Ganze Zahl im Bereich von -2.147.483.648 bis 2.147.483.647 | 
Währung: | Gleitkommazahl max. 15-stellig; Punkt(.) als Dezimaltrennzeichen z.B. 350670.87 | 
Datum: | tt.mm.jjjj | (z.B. 28.12.2017)
Uhrzeit: | hh:mm | (z.B. 14:35)
Boolean: | 0 = nein | 
 | 1 = ja | 
Fett formatierte Felder sind für eine konsistente Weiterverarbeitung bei den Gerichten notwendig, deren Systeme diese Daten verarbeiten (Minimalangaben, die durchaus ergänzungsbedürftig sein können).
4.2 Forderungsanmeldung (Satzkennzeichen 20)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 20
2 | Nr. der Forderung | Long | Interne Nummerierung der Forderungsanmeldung (beim Insolvenzverwalter eindeutig innerhalb des Verfahrens)
3 | Nr. des Anmeldegläubigers | Long | Verweis auf den Anmeldegläubiger
4 | Datum der Anmeldung | Datum | 
5 | Angemeldeter Rang | String(30) | Mögliche Ränge:
 |  |  | Vorrang
 |  |  | Rang 0
 |  |  | Rang N I
 |  |  | Rang N II
 |  |  | Rang N III
 |  |  | Rang N IV
 |  |  | Rang N V
 |  |  | Rang N VI
 |  |  | Für Nachlassinsolvenz zusätzlich:
 |  |  | Rang N VI A
 |  |  | Rang N VII
 |  |  | Rang N VII A
 |  |  | Rang N VIII R1
 |  |  | Rang N VIII R1 A
 |  |  | Rang N VIII R2
 |  |  | Rang N VIII R2 A
 |  |  | Rang N VIII R3
 |  |  | Rang N VIII R3 A
 |  |  | Rang N VIII R4
 |  |  | Rang N VIII R4 A
 |  |  | Rang N VIII R5
 |  |  | Rang N VIII R5 A
 |  |  | Rang N VIII R6
 |  |  | Rang N VIII R6 A
 |  |  | Rang N VIII R7
 |  |  | Rang N VIII R7 A
 |  |  | Rang N VIII R8
 |  |  | Rang N VIII R8 A
 |  |  | Rang N VIII R9
 |  |  | Rang N VIII R9 A
 |  |  | Rang N VIII R10
 |  |  | Rang N VIII R10 A
 |  |  | Rang N VIII
 |  |  | Rang N VIII A
 |  |  | Rang N IX
 |  |  | Rang N IX A
6 | Lfd. Nr. / Kennung innerhalb des Ranges | Long | Auf Verwalterseite vorgenommene Kennzeichnung der Forderung innerhalb des Ranges (nicht eindeutig)
7 | Währung | String(2) | DM oder EU (Euro)
8 | Betrag der Hauptforderung | Währung | 
9 | Grund der Hauptforderung | String(255) | 
10 | Betrag der Zinsen | Währung | 
11 | Grund für die Zinsen | String(255) | 
12 | Betrag der Kosten | Währung | 
13 | Grund für die Kosten | String(255) | 
14 | Tituliert | Boolean | Angabe, ob der Forderung ein vollstreckbarer Titel (z.B. Urteil) zugrunde liegt
15 | Titel bei der Akte | Boolean | Angabe, ob der vollstreckbare Titel zu den Akten gereicht worden ist oder nicht
16 | Für den Ausfall | Boolean | Angabe, ob die Forderung für den Ausfall angemeldet wird
17 | Geschäftszeichen der Forderung | String(50) | Geschäftszeichen der Forderungsanmeldung
18 | Bemerkungen | String(255) | Textfeld für Bemerkungen
19 | Blattnummer der Anmeldung | String(50) | Erscheint im Tabellenauszug
20 | Nr. der Abstimmungsgruppe | Long | Verweis auf die Gruppe, der die Forderung bzgl. der Abstimmung über den Insolvenzplan zugeordnet ist
21 | Unerlaubte Handlung | Boolean | Angabe, ob der Forderung eine vorsätzlich begangene unerlaubte Handlung (§ 174 InsO) zugrunde liegt
Beispiel für einen Datensatz dieser Entität:
20;23;12;12.02.2019;Rang 0;2;EU;2340.50;Lieferung von Waren;24.69;Zinsen für 2018; 100.00;Kosten für Zwangsvollstreckung;1;1;0;23 xy 98;;234;34;0
4.3 Gläubiger (Satzart 30)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 30
2 | Anmeldegläubiger | Boolean | Angabe, ob der Gläubiger Anmelde- oder sonstiger Gläubiger ist.
3 | Nr. des Gläubigers | Long | Interne Nummerierung des Gläubigers (beim Insolvenzverwalter eindeutig innerhalb des Verfahrens)
4 | Anrede | String(20) | Mögliche Werte:
 |  |  | Behörde(w)
 |  |  | Behörde(m)
 |  |  | Behörde(s)
 |  |  | Firma(w)
 |  |  | Firma(m)
 |  |  | Firma(s)
 |  |  | Frau
 |  |  | Herr
 |  |  | Rechtsanwalt
 |  |  | Rechtsanwälte
 |  |  | Rechtsanwältin
 |  |  | Rechtsanwältinnen
 |  |  | Rechtsbeistand
 |  |  | Rechtsbeistände
 |  |  | Rechtsbeiständin
 |  |  | Rechtsbeiständinnen
 |  |  | Sonstige(w)
 |  |  | Sonstige(m)
 |  |  | Sonstige(s)
 |  |  | Individuelle Eingaben sind nicht zulässig.
5 | Titel | String(20) | z.B. Dr., Prof. Usw.
6 | Vorname | String(50) | 
7 | Nachname | String(255) | 
8 | Namenszusatz | String(50) | z.B. Junior, Senior
9 | Straße | String(50) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist.
10 | Hausnummer | String(10) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist.
11 | Landeskennzeichen | String(5) | Länderkürzel am 01.09.1999 abgeschafft. Dieses Feld ist als Leerfeld zu übergeben.
12 | Land | String(50) | Landesbezeichnung in Großbuchstaben, z.B. ITALIEN
13 | Postleitzahl | String(10) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist.
14 | Ort | String(50) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist.
15 | Postleitzahl für Postfach | String(10) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist.
16 | Bezeichnung des Postfachs | String(30) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu erreichen ist. z.B. Postfach, P.O. Box
17 | Nummer des Postfachs | String(10) | Bestandteil der Anschrift, unter der der Gläubiger postalisch zu
 |  |  | erreichen ist.
18 | Zusatz zu Anschrift | String(50) | Der Adresszusatz wird innerhalb der Anschrift nach dem Nachnamen ausgegeben, z.B.: Peter Müller c/o Nirgendwo GmbH
19 | Weitere Anschrift | String(255) | Textfeld zur Erfassung einer für das Tabellenblatt relevanten Anschrift (z.B. Firmensitz laut HR, Privatanschrift des Einzelkaufmanns)
20 | Telefonnummer | String(20) | 
21 | Telefaxnummer | String(20) | 
22 | Email Adresse | String(50) | z.B. mustermann@netz.de
23 | Zustellungsart | String(20) | Mögliche Werte:
 |  |  | Aufgabe zur Post
 |  |  | Zustellungsurkunde
 |  |  | Empfangsbekenntnis
 |  |  | Weitere Werte sind nicht zulässig.
24 | Geschäftszeichen | String(50) | Zeichen des Anmeldegläubigers
25 | Ansprechpartner | String(50) | Name des Ansprechpartners
26 | Beruf | String(30) | Angabe des Berufs bei natürlichen Personen
27 | Geburtsdatum | Datum | 
28 | Geburtsname | String(30) | 
29 | Übertragungsweg | String(30) | Mögliche Werte:
 |  |  | Brief per Post
 |  |  | Brief per Fach
 |  |  | Fax
 |  |  | Email
 |  |  | ERV
 |  |  | Weitere Werte sind nicht zulässig.
30 | Handelnd unter | String(255) | z.B. handelnd unter „Atelier Peter Müller, Efeuweg 4, 12345 Irgendwo“
31 | Massegläubiger | Boolean | Angabe, ob der Gläubiger Massegläubiger ist
32 | Absonderungsgläubiger | Boolean | Angabe, ob der Gläubiger Absonderungsgläubiger ist
33 | Nachranggläubiger | Boolean | Angabe, ob der Gläubiger Nachranggläubiger ist
34 | Postempfänger | Boolean | Angabe, ob der Gläubiger Postempfänger ist. (bei gesetzl. Vertreter oder Verfahrensbevollmächtigten ist ggf. dort der entsprechende Hinweis vorzunehmen) (Vorschlagswert des Verwalters für das Gericht)
35 | Gesamtgläubiger | Boolean | Ja = es handelt sich um einen Gesamtgläubiger Nein = es handelt sich um einen Gläubiger bzw. um eine Gläubigergemeinschaft
36 | SAFE-ID oder De-MailAdresse | String(100) | Rechtsverbindlicher elektronischer Kommunikationsweg
Beispiel für einen Datensatz:
30;1;2;Herr;Dr.;Peter;Mustermann;;Testweg;10;;ITALIEN;12345;Musterort;12346;Postfach; 12400;;;0423/5600-0;0423/560010;pm@test.it;Aufgabe zur Post;;;;11.09.1945;;ERV;;0;0;0;0;0;peter.mustermann@xyz.de-mail.de
4.4 Mitglieder einer Gläubigermehrheit (Satzkennzeichen 40)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1. | Satzkennzeichen | Integer | 40
2. | Nr. des Mitglieds der Gläubigermehrheit | Long | Interne Nummerierung
3. | Nr. des Gläubigers | Long | Verweis auf den Gläubiger
4. | Anrede | String(20) | vgl. Entität Gläubiger (Satzart 30)
5. | Titel | String(20) | z.B. Dr., Prof. usw.
6. | Vorname | String(50) | 
7. | Nachname | String(255) | 
8. | Namenszusatz | String(50) | vgl. Entität Gläubiger (Satzart 30)
9. | Straße | String(50) | vgl. Entität Gläubiger (Satzart 30)
10. | Hausnummer | String(10) | vgl. Entität Gläubiger (Satzart 30)
11. | Landeskennzeichen | String(5) | vgl. Entität Gläubiger (Satzart 30)
12. | Land | String(50) | vgl. Entität Gläubiger (Satzart 30)
13. | Postleitzahl | String(10) | vgl. Entität Gläubiger (Satzart 30)
14. | Ort | String(50) | vgl. Entität Gläubiger (Satzart 30)
15. | Postleitzahl für Postfach | String(10) | vgl. Entität Gläubiger (Satzart 30)
16. | Bezeichnung des Postfachs | String(30) | vgl. Entität Gläubiger (Satzart 30)
17. | Nummer des Postfachs | String(10) | vgl. Entität Gläubiger (Satzart 30)
18. | Zusatz zu Anschrift | String(50) | vgl. Entität Gläubiger (Satzart 30)
19. | Weitere Anschrift | String(255) | vgl. Entität Gläubiger (Satzart 30)
20. | Telefonnummer | String(20) | 
21. | Telefaxnummer | String(20) | 
22. | Email Adresse | String(50) | vgl. Entität Gläubiger (Satzart 30)
23. | Zustellungsart | String(20) | vgl. Entität Gläubiger (Satzart 30)
24. | Geschäftszeichen | String(50) | Zeichen des Gläubigers
25. | Ansprechpartner | String(50) | Name des Ansprechpartners
26. | Beruf | String(30) | Angabe des Berufs bei natürlichen Personen
27. | Geburtsdatum | Datum | 
28. | Geburtsname | String(30) | 
29. | Übertragungsweg | String(30) | vgl. Entität Gläubiger (Satzart 30)
30. | Handelnd unter | String(255) | vgl. Entität Gläubiger (Satzart 30)
31. | Postempfänger | Boolean | Angabe, ob das Mitglied Postempfänger ist (Vorschlagswert des Verwalters für das Gericht)
32. | SAFE-ID oder De-Mail-Adresse | String(100) | vgl. Entität Gläubiger (Satzart 30)
Beispiel für einen Datensatz:
40;2;3;Herr;Dr.;Peter;Meier;;Testweg;10;;ITALIEN;12345;Musterort;12346;Postfach; 12400;;;0423/5600-0;0423/5600-10;pm@test.it;Aufgabe zur Post;;;Bäckermeister;11.09.1950;;ERV;;1;peter.meier23@xyz.de-mail.de
4.5 Vertreter des Gläubigers (Satzkennzeichen 50)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 50
2 | Nr. des Vertreters | Long | Interne Nummerierung
3 | Nr. des Gläubigers | Long | Verweis auf den Gläubiger
4 | Level 1 | Integer | Verschlüsselung der Vertreterstruktur*)
5 | Level 2 | Integer | Verschlüsselung der Vertreterstruktur
6 | Level 3 | Integer | Verschlüsselung der Vertreterstruktur
7 | Level 4 | Integer | Verschlüsselung der Vertreterstruktur
8 | Level 5 | Integer | Verschlüsselung der Vertreterstruktur
9 | Art des Vertreters | String(50) | Mögliche Werte (nur Singular möglich):
 |  |  | Betreuer
 |  |  | Betreuerin
 |  |  | Nachlasspfleger
 |  |  | Nachlasspflegerin
 |  |  | Testamentsvollstrecker
 |  |  | Testamentsvollstreckerin
 |  |  | Liquidator
 |  |  | Liquidatorin
 |  |  | Geschäftsführer
 |  |  | Geschäftsführerin
 |  |  | Gesellschafter
 |  |  | Gesellschafterin
 |  |  | Partner
 |  |  | Partnerin
 |  |  | Pfleger
 |  |  | Pflegerin
 |  |  | Persönlich haftender
 |  |  | Gesellschafter
 |  |  | Persönlich haftende
 |  |  | Gesellschafterin
 |  |  | Mutter
 |  |  | Mitreeder
 |  |  | Mitreederin
 |  |  | Vater
 |  |  | Vormund
 |  |  | Vorstand
 |  |  | Verfahrensbevollmächtigter
 |  |  | Verfahrensbevollmächtigte
 |  |  | Zustellungsbevollmächtigter
 |  |  | Zustellungsbevollmächtigte
 |  |  | Sonstige
 |  |  | Individuelle Eingaben sind nicht zulässig.
10 | Anrede | String(20) | vgl. Entität Gläubiger (Satzart 30)
11 | Titel | String(20) | vgl. Entität Gläubiger (Satzart 30)
12 | Vorname | String(50) | 
13 | Nachname | String(255) | 
14 | Namenszusatz | String(50) | z.B. Junior, Senior
15 | Straße | String(50) | vgl. Entität Gläubiger (Satzart 30)
16 | Hausnummer | String(10) | vgl. Entität Gläubiger (Satzart 30)
17 | Landeskennzeichen | String(5) | vgl. Entität Gläubiger (Satzart 30)
18 | Land | String(50) | vgl. Entität Gläubiger (Satzart 30)
19 | Postleitzahl | String(10) | vgl. Entität Gläubiger (Satzart 30)
20 | Ort | String(50) | vgl. Entität Gläubiger (Satzart 30)
21 | Postleitzahl für Postfach | String(10) | vgl. Entität Gläubiger (Satzart 30)
22 | Bezeichnung des Postfachs | String(30) | vgl. Entität Gläubiger (Satzart 30)
23 | Nummer des Postfachs | String(10) | vgl. Entität Gläubiger (Satzart 30)
24 | Zusatz zu Anschrift | String(50) | vgl. Entität Gläubiger (Satzart 30)
25 | Weitere Anschrift | String(255) | vgl. Entität Gläubiger (Satzart 30)
26 | Telefonnummer | String(20) | 
27 | Telefaxnummer | String(20) | 
28 | Email Adresse | String(50) | vgl. Entität Gläubiger (Satzart 30)
29 | Zustellungsart | String(20) | vgl. Entität Gläubiger (Satzart 30)
30 | Geschäftszeichen | String(50) | Zeichen des Vertreters
31 | Vollmacht | Boolean | Angabe, ob eine Vollmacht vorhanden ist
32 | Untervollmacht | Boolean | Angabe, ob eine Untervollmacht vorliegt
33 | Übertragungsweg | String(30) | vgl. Entität Gläubiger (Satzart 30)
34 | Blattzahl der Vollmacht | String(20) | 
35 | Postempfänger | Boolean | Angabe, ob der Vertreter Postempfänger ist (Vorschlagswert des Verwalters für das Gericht)
36 | SAFE-ID oder De-MailAdresse | String(100) | vgl. Entität Gläubiger (Satzart 30)
Die Felder Level1 - Level5 dienen zur Verschlüsselung der Vertretungshierarchie. Dabei sind 5 Hierarchieebenen möglich:
Der 1. direkte Vertreter des Gläubigers auf Ebene 1 wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 0 | 0 | 0 | 0
Der 2. direkte Vertreter des Gläubigers auf Ebene 1 wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
2 | 0 | 0 | 0 | 0
Der 1. Vertreter des 1. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 1 | 0 | 0 | 0
Der 2. Vertreter des 1. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 2 | 0 | 0 | 0
Der 1. Vertreter des 2. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
2 | 1 | 0 | 0 | 0
usw.
Beispiel für einen Datensatz dieser Entität:
50;12;3;1;0;0;0;0;Verfahrensbevollmächtigter;Herr;Dr.;Heinz;Müller;;Musterweg;20;;;12345;Musterort;;;;;;0435/8979-0;0435/8979100;HM@Test.it;;;1;0;ERV;;1;DE.ABCDE.4d12b24e-993b-15e3-aa13-2c718a4f9bf6
4.6 Vertreter eines Mitglieds (Satzkennzeichen 55)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 55
2 | Nr. des Vertreters | Long | Interne Nummerierung
3 | Nr. des Mitglieds der Gläubigermehrheit | Long | Verweis auf das Mitglied einer Gläubigermehrheit
4 | Level 1 | Integer | Verschlüsselung der Vertreterstruktur*)
5 | Level 2 | Integer | Verschlüsselung der Vertreterstruktur
6 | Level 3 | Integer | Verschlüsselung der Vertreterstruktur
7 | Level 4 | Integer | Verschlüsselung der Vertreterstruktur
8 | Level 5 | Integer | Verschlüsselung der Vertreterstruktur
9 | Art des Vertreters | String(50) | vgl. Entität Vertreter des Gläubigers (Satzart 50)
10 | Anrede | String(20) | Vgl. Entität Gläubiger (Satzart 30)
11 | Titel | String(20) | z.B. Dr., Prof. usw.
12 | Vorname | String(50) | 
13 | Nachname | String(255) | 
14 | Namenszusatz | String(50) | z.B. Junior, Senior
15 | Straße | String(50) | Vgl. Entität Gläubiger (Satzart 30)
16 | Hausnummer | String(10) | Vgl. Entität Gläubiger (Satzart 30)
17 | Landeskennzeichen | String(5) | Vgl. Entität Gläubiger (Satzart 30)
18 | Land | String(50) | Vgl. Entität Gläubiger (Satzart 30)
19 | Postleitzahl | String(10) | Vgl. Entität Gläubiger (Satzart 30)
20 | Ort | String(50) | Vgl. Entität Gläubiger (Satzart 30)
21 | Postleitzahl für Postfach | String(10) | Vgl. Entität Gläubiger (Satzart 30)
22 | Bezeichnung des Postfachs | String(30) | Vgl. Entität Gläubiger (Satzart 30)
23 | Nummer des Postfachs | String(10) | Vgl. Entität Gläubiger (Satzart 30)
24 | Zusatz zu Anschrift | String(50) | Vgl. Entität Gläubiger (Satzart 30)
25 | Weitere Anschrift | String(255) | Vgl. Entität Gläubiger (Satzart 30)
26 | Telefonnummer | String(20) | 
27 | Telefaxnummer | String(20) | 
28 | Email Adresse | String(50) | z. B. mustermann@netz.de
29 | Zustellungsart | String(20) | Vgl. Entität Gläubiger (Satzart 30)
30 | Geschäftszeichen | String(50) | Zeichen des Vertreters
31 | Vollmacht | Boolean | Angabe, ob eine Vollmacht vorhanden ist
32 | Untervollmacht | Boolean | Angabe, ob eine Untervollmacht vorliegt
33 | Übertragungsweg | String(30) | Vgl. Entität Gläubiger (Satzart 30)
34 | Blattzahl der Vollmacht | String(20) | 
35 | Postempfänger | Boolean | Angabe, ob der Vertreter des Mitglieds Postempfänger ist (Vorschlagswert des Verwalters für das Gericht)
36 | SAFE-ID oder De-Mail-Adresse | String(100) | Vgl. Entität Gläubiger (Satzart 30)
Die Felder Level1 - Level5 dienen zur Verschlüsselung der Vertretungshierarchie. Dabei sind 5 Hierarchieebenen möglich:
Der 1. direkte Vertreter des Gläubigers auf Ebene 1 wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 0 | 0 | 0 | 0
Der 2. direkte Vertreter des Gläubigers auf Ebene 1 wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
2 | 0 | 0 | 0 | 0
Der 1. Vertreter des 1. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 1 | 0 | 0 | 0
Der 2. Vertreter des 1. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
1 | 2 | 0 | 0 | 0
Der 1. Vertreter des 2. Vertreters des Gläubigers wird wie folgt verschlüsselt:
Level1 | Level2 | Level3 | Level4 | Level5
2 | 1 | 0 | 0 | 0
usw.
Beispiel für einen Datensatz dieser Entität:
55;12;3;1;0;0;0;0;Verfahrensbevollmächtigter;Herr;Dr.;Heinz;Müller;;Musterweg;20;;;1 2345;Musterort;;;;;;0435/8979-0;0435/8979-100;;;34 vc 98;1;0;ERV;;1;DE.ABCDE.4d12b24e-993b-15e3-aa13-2c718a4f9bf6
4.7 Erklärung des Verwalters (Satzkennzeichen 60)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 60
2 | Nr. der Erklärung | Long | Interne Nummerierung
3 | Nr. der Forderungsanmeldung | Long | Verweis auf die Forderung
4 | Neuer Rang | String(50) | Falls der beanspruchte Rang bestritten wird, neuen Rang angeben
 |  |  | Mögliche Ränge:
 |  |  | Vorrang
 |  |  | Rang 0
 |  |  | Rang N I
 |  |  | Rang N II
 |  |  | Rang N III
 |  |  | Rang N IV
 |  |  | Rang N V
 |  |  | Rang N VI
 |  |  | Für Nachlassinsolvenz zusätzlich:
 |  |  | Rang N VI A
 |  |  | Rang N VII
 |  |  | Rang N VII A
 |  |  | Rang N VIII R1
 |  |  | Rang N VIII R1 A
 |  |  | Rang N VIII R2
 |  |  | Rang N VIII R2 A
 |  |  | Rang N VIII R3
 |  |  | Rang N VIII R3 A
 |  |  | Rang N VIII R4
 |  |  | Rang N VIII R4 A
 |  |  | Rang N VIII R5
 |  |  | Rang N VIII R5 A
 |  |  | Rang N VIII R6
 |  |  | Rang N VIII R6 A
 |  |  | Rang N VIII R7
 |  |  | Rang N VIII R7 A
 |  |  | Rang N VIII R8
 |  |  | Rang N VIII R8 A
 |  |  | Rang N VIII R9
 |  |  | Rang N VIII R9 A
 |  |  | Rang N VIII R10
 |  |  | Rang N VIII R10 A
 |  |  | Rang N VIII
 |  |  | Rang N VIII A
 |  |  | Rang N IX
 |  |  | Rang N IX A
5 | Vorläufig bestritten | Boolean | Angabe, ob die Forderung nur vorläufig bestritten wurde
6 | Festgestellter Betrag | Währung | in der Währung der Forderungsanmeldung (Satzart 20)
7 | Festgestellter Betrag für den Ausfall | Währung | in der Währung der Forderungsanmeldung (Satzart 20)
8 | Festgestellter Betrag als aufschiebend bedingt | Währung | in der Währung der Forderungsanmeldung (Satzart 20)
9 | Festgestellter Betrag als auflösend bedingt | Währung | in der Währung der Forderungsanmeldung (Satzart 20)
Anmerkung:
Die Summe der Beträge aus den Feldern 6 bis 9 aller zu einer Forderung abgegebenen Erklärungen kann maximal die angemeldete Forderungshöhe ergeben.
Beispiel für Erklärungen zu einem neuen Rang (Feld 4 „Neuer Rang“):
Angemeldete Forderung: 10.000,00
1. Erklärung des Verwalters:
 | festgestellt im Rang 0 (entsprechend der Forderungsanmeldung in Satzart 20) | 
 |  | in Höhe von 500,00 (Feld 6 „Festgestellter Betrag“)
 | und | 
 |  | in Höhe von 6.000,00 für den Ausfall (Feld 7 „Festgestellter Betrag für den Ausfall“)
 | sowie | 
 |  | in Höhe von 1.500,00 als aufschiebend bedingt (Feld 8 „Festgestellter Betrag als aufschiebend bedingt“).
2. Erklärung des Verwalters:
 | festgestellt im Rang N I (Feld 4 „Neuer Rang“) | 
 |  | in Höhe von 300,00 (Feld 6 „Festgestellter Betrag“)
 | und | 
 |  | in Höhe von 200,00 als aufschiebend bedingt (Feld 8 „Festgestellter Betrag als aufschiebend bedingt“)
3. Erklärung des Verwalters:
 | festgestellt im Rang N II (Feld 4 „Neuer Rang“) | 
 |  | in Höhe von 200,00 als auflösend bedingt (Feld 9 „Festgestellter Betrag als auflösend bedingt“)
usw.
Beispiel für einen Datensatz dieser Entität:
60;12;2;;0;124000.89;0;0;0
4.8 Debitor (Satzkennzeichen 70)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 70
2 | Nr. des Debitors | Long | Interne Nummerierung
3 | Anredeschlüssel | String(20) | vgl. Entität Gläubiger (Satzart 30)
4 | Titel | String(20) | z.B. Dr., Prof. usw.
5 | Vorname | String(50) | 
6 | Nachname | String(255) | 
7 | Namenszusatz | String(50) | z.B. Junior, Senior
8 | Straße | String(50) | vgl. Entität Gläubiger (Satzart 30)
9 | Hausnummer | String(10) | vgl. Entität Gläubiger (Satzart 30)
10 | Landeskennzeichen | String(5) | vgl. Entität Gläubiger (Satzart 30)
11 | Land | String(50) | vgl. Entität Gläubiger (Satzart 30)
12 | Postleitzahl | String(10) | vgl. Entität Gläubiger (Satzart 30)
13 | Ort | String(50) | vgl. Entität Gläubiger (Satzart 30)
14 1 | Postleitzahl für Postfach | String(10) | vgl. Entität Gläubiger (Satzart 30)
15 | Bezeichnung des Postfachs | String(30) | vgl. Entität Gläubiger (Satzart 30)
16 | Nummer des Postfachs | String(10) | vgl. Entität Gläubiger (Satzart 30)
17 | Zusatz zu Anschrift | String(50) | vgl. Entität Gläubiger (Satzart 30)
18 | Telefonnummer | String(20) | 
19 | Telefaxnummer | String(20) | 
20 | Email Adresse | String(50) | z.B. mustermann@netz.de
21 | Zustellungsart | String(20) | vgl. Entität Gläubiger (Satzart 30)
22 | Geschäftszeichen | String(50) | Zeichen des Debitors
23 | Beruf | String(30) | Angabe des Berufs bei natürlichen Personen
24 | Geburtsname | String(30) | 
25 | Übertragungsweg | String(30) | vgl. Entität Gläubiger (Satzart 30)
26 | Postempfänger | Boolean | Angabe, ob der Debitor Postempfänger ist (Vorschlagswert des Verwalters für das Gericht)
27 | SAFE-ID oder De-Mail-Adresse | String(100) | vgl. Entität Gläubiger (Satzart 30)
Beispieldatensatz:
70;2;Herr;Dr.;Peter;Mustermann;;Testweg;10;;;12345;Musterort;12346;Postfach; 12400;;0423/5600-10;;pm@test.de;;;;;ERV;0;peter.mustermann@xyz.de-mail.de
4.9 Vertreter des Debitors (Satzkennzeichen 75)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 75
2 | Nr. des Vertreters | Long | Interne Nummerierung
3 | Nr. des Debitors | Long | Verweis auf den Debitor
4 | Level 1 | Integer | Verschlüsselung der Vertreterstruktur (siehe Entität Vertreter des Gläubigers - Satzart 50)
5 | Level 2 | Integer | Verschlüsselung der Vertreterstruktur
6 | Level 3 | Integer | Verschlüsselung der Vertreterstruktur
7 | Level 4 | Integer | Verschlüsselung der Vertreterstruktur
8 | Level 5 | Integer | Verschlüsselung der Vertreterstruktur
9 | Art des Vertreters | String(50) | Siehe Entität Vertreter des Gläubigers - Satzart 50
10 | Anrede | String(20) | Vgl. Entität Gläubiger (Satzart 30)
11 | Titel | String(20) | z.B. Dr., Prof. usw.
12 | Vorname | String(50) | Vgl. Entität Gläubiger (Satzart 30)
13 | Nachname | String(255) | Vgl. Entität Gläubiger (Satzart 30)
14 | Namenszusatz | String(50) | Vgl. Entität Gläubiger (Satzart 30)
15 | Straße | String(50) | Vgl. Entität Gläubiger (Satzart 30)
16 | Hausnummer | String(10) | Vgl. Entität Gläubiger (Satzart 30)
17 | Landeskennzeichen | String(5) | Vgl. Entität Gläubiger (Satzart 30)
18 | Land | String(50) | Vgl. Entität Gläubiger (Satzart 30)
19 | Postleitzahl | String(10) | Vgl. Entität Gläubiger (Satzart 30)
20 | Ort | String(50) | Vgl. Entität Gläubiger (Satzart 30)
21 | Postleitzahl für Postfach | String(10) | Vgl. Entität Gläubiger (Satzart 30)
22 | Bezeichnung des Postfachs | String(30) | Vgl. Entität Gläubiger (Satzart 30)
23 | Nummer des Postfachs | String(10) | Vgl. Entität Gläubiger (Satzart 30)
24 | Zusatz zu Anschrift | String(50) | Vgl. Entität Gläubiger (Satzart 30)
25 | Telefonnummer | String(20) | 
26 | Telefaxnummer | String(20) | 
27 | Email Adresse | String(50) | 
28 | Zustellungsart | String(20) | Vgl. Entität Gläubiger (Satzart 30)
29 | Geschäftszeichen | String(50) | Zeichen des Vertreters
30 | Vollmacht | Boolean | Angabe, ob eine Vollmacht vorhanden ist
31 | Übertragungsweg | String(30) | Vgl. Entität Gläubiger (Satzart 30)
32 | Blattzahl der Vollmacht | String(20) | Im Falle des Verfahrensbevollmächtigten.
33 | Postempfänger | Boolean | Angabe, ob der Vertreter des Debitors Postempfänger ist (Vorschlagswert des Verwalters für das Gericht)
34 | SAFE-ID oder De-Mail-Adresse | String(100) | Vgl. Entität Gläubiger (Satzart 30)
Beispieldatensatz:
75;12;13;1;0;0;0;0;Verfahrensbevollmächtigter;Herr;Dr.;Heinz;Müller;;Musterweg;20;;N IEDERLANDE;12345;Musterort;;;;;0435/8979-0;0435/8979-100;;;34 vc 98;1;ERV;;1;DE.ABCDE.4d12b24e-993b-15e3-aa13-2c718a4f9bf6
4.10 Abstimmungsgruppe (Satzkennzeichen 80)
Die Datensätze dieser Entität sind wie folgt aufgebaut:
Nr. | Feld | Datentyp | Mögliche Werte bzw. Hinweis
1 | Satzkennzeichen | Integer | 80
2 | Nr. der Abstimmungsgruppe | Long | Interne Nummerierung
3 | Bezeichnung | String(50) | 
Beispieldatensatz:
80;3;Arbeitnehmer
Anlage:
CRC-Prüfsummenbildung
/********************************************************************** |  | 
 | * | Name: crc.c
 | * | Date: 15.04.91
 | * | Author: Andre Koppel (akoppel@akso.de)
 | * | Inhalt: Berechnung von 16- und 32-Bit CRCs basierend auf überall
 | * | hinreichend gut dokumentierten Quellen. Um die Verarbeitungsgeschwindigkeit zu steigern, greifen die Funktionen auf statische Tabellen zurück, die jeweils Stützwerte enthalten, auf deren Basis weitergerechnet werden kann.
 | * | Funktionen: Alle enthaltenen Funktionen liefern als Ergebnis einen
 | * | 16- oder 32-Bit CRC-Wert. Gleichermaßen erwarten alle Funktionen einen Start-CRC-Wert, auf dessen Basis der nächste CRC-Wert errechnet wird. Für das erste Byte eines zu berechnenden Datenstromes ist der Startwert = 0.
 | * | Für jedes weitere Byte ist der Startwert gleich dem CRC-Wert der letzten Berechnung.
 | * | Die Parameterübergabe und Ergebnisse der Funktionen sind leicht aus den Funktionsdefinitionen ersichtlich (s.u.)
**********************************************************************/ |  | 
static unsigned crctab[] = { |  | 
 | 0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7, 0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef, 0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6, 0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de, 0x2462, 0x3443, 0x0420, 0x1401, 0x64e6, 0x74c7, 0x44a4, 0x5485, 0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d, 0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4, 0xb75b, 0xa77a, 0x9719, 0x8738, 0xf7df, 0xe7fe, 0xd79d, 0xc7bc, 0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823, 0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b, 0x5af5, 0x4ad4, 0x7ab7, 0x6a96, 0x1a71, 0x0a50, 0x3a33, 0x2a12, 0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a, 0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41, 0xedae, 0xfd8f, 0xcdec, 0xddcd, 0xad2a, 0xbd0b, 0x8d68, 0x9d49, 0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70, 0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78, 0x9188, 0x81a9, 0xb1ca, 0xa1eb, 0xd10c, 0xc12d, 0xf14e, 0xe16f, 0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067, 0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e, 0x02b1, 0x1290, 0x22f3, 0x32d2, 0x4235, 0x5214, 0x6277, 0x7256, 0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d, 0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405, 0xa7db, 0xb7fa, 0x8799, 0x97b8, 0xe75f, 0xf77e, 0xc71d, 0xd73c, 0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634, 0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab, 0x5844, 0x4865, 0x7806, 0x6827, 0x18c0, 0x08e1, 0x3882, 0x28a3, 0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a, 0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92, 0xfd2e, 0xed0f, 0xdd6c, 0xcd4d, 0xbdaa, 0xad8b, 0x9de8, 0x8dc9, 0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1, 0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8, 0x6e17, 0x7e36, 0x4e55, 0x5e74, 0x2e93, 0x3eb2, 0x0ed1, 0x1ef0, | 
 |  | };
static unsigned long crctab32[] = { |  | 
 | 0x00000000L, 0x77073096L, 0xee0e612cL, 0x990951baL, 0x076dc419L, 0x706af48fL, 0xe963a535L, 0x9e6495a3L, 0x0edb8832L, 0x79dcb8a4L, 0xe0d5e91eL, 0x97d2d988L, 0x09b64c2bL, 0x7eb17cbdL, 0xe7b82d07L, 0x90bf1d91L, 0x1db71064L, 0x6ab020f2L, 0xf3b97148L, 0x84be41deL, 0x1adad47dL, 0x6ddde4ebL, 0xf4d4b551L, 0x83d385c7L, 0x136c9856L, 0x646ba8c0L, 0xfd62f97aL, 0x8a65c9ecL, 0x14015c4fL, 0x63066cd9L, 0xfa0f3d63L, 0x8d080df5L, 0x3b6e20c8L, 0x4c69105eL, 0xd56041e4L, 0xa2677172L, 0x3c03e4d1L, 0x4b04d447L, 0xd20d85fdL, 0xa50ab56bL, 0x35b5a8faL, 0x42b2986cL, 0xdbbbc9d6L, 0xacbcf940L, 0x32d86ce3L, 0x45df5c75L, 0xdcd60dcfL, 0xabd13d59L, 0x26d930acL, 0x51de003aL, 0xc8d75180L, 0xbfd06116L, 0x21b4f4b5L, 0x56b3c423L, 0xcfba9599L, 0xb8bda50fL, 0x2802b89eL, 0x5f058808L, 0xc60cd9b2L, 0xb10be924L, 0x2f6f7c87L, 0x58684c11L, 0xc1611dabL, 0xb6662d3dL, 0x76dc4190L, 0x01db7106L, 0x98d220bcL, 0xefd5102aL, 0x71b18589L, 0x06b6b51fL, 0x9fbfe4a5L, 0xe8b8d433L, 0x7807c9a2L, 0x0f00f934L, 0x9609a88eL, 0xe10e9818L, 0x7f6a0dbbL, 0x086d3d2dL, 0x91646c97L, 0xe6635c01L, 0x6b6b51f4L, 0x1c6c6162L, 0x856530d8L, 0xf262004eL, 0x6c0695edL, 0x1b01a57bL, 0x8208f4c1L, 0xf50fc457L, 0x65b0d9c6L, 0x12b7e950L, 0x8bbeb8eaL, 0xfcb9887cL, 0x62dd1ddfL, 0x15da2d49L, 0x8cd37cf3L, 0xfbd44c65L, 0x4db26158L, 0x3ab551ceL, 0xa3bc0074L, 0xd4bb30e2L, 0x4adfa541L, 0x3dd895d7L, 0xa4d1c46dL, 0xd3d6f4fbL, 0x4369e96aL, 0x346ed9fcL, 0xad678846L, 0xda60b8d0L, 0x44042d73L, 0x33031de5L, 0xaa0a4c5fL, 0xdd0d7cc9L, 0x5005713cL, 0x270241aaL, 0xbe0b1010L, 0xc90c2086L, 0x5768b525L, 0x206f85b3L, 0xb966d409L, 0xce61e49fL, 0x5edef90eL, 0x29d9c998L, 0xb0d09822L, 0xc7d7a8b4L, 0x59b33d17L, 0x2eb40d81L, 0xb7bd5c3bL, 0xc0ba6cadL, 0xedb88320L, 0x9abfb3b6L, 0x03b6e20cL, 0x74b1d29aL, 0xead54739L, 0x9dd277afL, 0x04db2615L, 0x73dc1683L, 0xe3630b12L, 0x94643b84L, 0x0d6d6a3eL, 0x7a6a5aa8L, 0xe40ecf0bL, 0x9309ff9dL, 0x0a00ae27L, 0x7d079eb1L, 0xf00f9344L, 0x8708a3d2L, 0x1e01f268L, 0x6906c2feL, 0xf762575dL, 0x806567cbL, 0x196c3671L, 0x6e6b06e7L, 0xfed41b76L, 0x89d32be0L, 0x10da7a5aL, 0x67dd4accL, 0xf9b9df6fL, 0x8ebeeff9L, 0x17b7be43L, 0x60b08ed5L, 0xd6d6a3e8L, 0xa1d1937eL, 0x38d8c2c4L, 0x4fdff252L, 0xd1bb67f1L, 0xa6bc5767L, 0x3fb506ddL, 0x48b2364bL, 0xd80d2bdaL, 0xaf0a1b4cL, 0x36034af6L, 0x41047a60L, 0xdf60efc3L, 0xa867df55L, 0x316e8eefL, 0x4669be79L, 0xcb61b38cL, 0xbc66831aL, 0x256fd2a0L, 0x5268e236L, 0xcc0c7795L, 0xbb0b4703L, 0x220216b9L, 0x5505262fL, 0xc5ba3bbeL, 0xb2bd0b28L, 0x2bb45a92L, 0x5cb36a04L, 0xc2d7ffa7L, 0xb5d0cf31L, 0x2cd99e8bL, 0x5bdeae1dL, 0x9b64c2b0L, 0xec63f226L, 0x756aa39cL, 0x026d930aL, 0x9c0906a9L, 0xeb0e363fL, 0x72076785L, 0x05005713L, 0x95bf4a82L, 0xe2b87a14L, 0x7bb12baeL, 0x0cb61b38L, 0x92d28e9bL, 0xe5d5be0dL, 0x7cdcefb7L, 0x0bdbdf21L, 0x86d3d2d4L, 0xf1d4e242L, 0x68ddb3f8L, 0x1fda836eL, 0x81be16cdL, 0xf6b9265bL, 0x6fb077e1L, 0x18b74777L, 0x88085ae6L, 0xff0f6a70L, 0x66063bcaL, 0x11010b5cL, 0x8f659effL, 0xf862ae69L, 0x616bffd3L, 0x166ccf45L, 0xa00ae278L, 0xd70dd2eeL, 0x4e048354L, 0x3903b3c2L, 0xa7672661L, 0xd06016f7L, 0x4969474dL, 0x3e6e77dbL, 0xaed16a4aL, 0xd9d65adcL, 0x40df0b66L, 0x37d83bf0L, 0xa9bcae53L, 0xdebb9ec5L, 0x47b2cf7fL, 0x30b5ffe9L, 0xbdbdf21cL, 0xcabac28aL, 0x53b39330L, 0x24b4a3a6L, 0xbad03605L, 0xcdd70693L, 0x54de5729L, 0x23d967bfL, 0xb3667a2eL, 0xc4614ab8L, 0x5d681b02L, 0x2a6f2b94L, 0xb40bbe37L, 0xc30c8ea1L, 0x5a05df1bL, 0x2d02ef8dL | 
 |  | };
/* |  | 
* NOTE: Bitte beachten, das erste Argument muss im Bereich 0 bis 255 liegen. |  | 
* | Das zweite Argument wird zwei mal verwendet, daher kann diese Funktion nicht als Macro implementiert werden. | 
*/ |  | 
unsigned short updcrc(unsigned short cp,unsigned short crc) |  | 
{ |  | 
return(crctab[((crc >> 8) & 255)] ^ (crc << 8) ^ cp); |  | 
} |  | 
unsigned long updcrc32(unsigned short cp,unsigned long crc) |  | 
{ |  | 
return(crctab32[((short)crc ^ cp) & 255] ^ ((crc >> 8) & 0x00FFFFFFL)); |  | 
} |  | 
unsigned short crccalc(unsigned short crc,void *in,int len) |  | 
{ |  | 
unsigned char *zeile = in; |  | 
 | while(len--) | 
 |  | crc=updcrc(*zeile++,crc); return(crc);
} |  | 
unsigned long crccalc32(unsigned long crc,void *in,int len) |  | 
{ |  | 
unsigned char *zeile = in; |  | 
 | while(len--) | 
 |  | crc=updcrc32(*zeile++,crc); return(crc);
} |  | 
Fußnoten
*) Zur Verschlüsselung der Vertreterstruktur
*) Zur Verschlüsselung der Vertreterstruktur
Einzelansicht Seitenanfang
