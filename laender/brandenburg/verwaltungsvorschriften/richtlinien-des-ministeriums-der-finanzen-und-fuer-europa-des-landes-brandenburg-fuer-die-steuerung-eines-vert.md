# Richtlinien des Ministeriums der Finanzen und für Europa des Landes Brandenburg für die Steuerung eines verteilten NFM-Betriebes im Land Brandenburg

- Herausgeber: Land Brandenburg
- Datum: 2022-03-18 (jüngstes Datum im Kopf des Dokuments)
- Quelle: https://bravors.brandenburg.de/verwaltungsvorschriften/nfm_2022
- Text: HTML-Seite der Stadt, als Text
- Hinweis: BRAVORS, Lesefassung der Landesregierung; maßgeblich ist die amtliche Veröffentlichung

---

Richtlinien des Ministeriums der Finanzen und für Europa des Landes Brandenburg für die Steuerung eines verteilten NFM-Betriebes im Land Brandenburg

vom 18. März 2022

(ABl./22, [Nr. 31], S.678)

Inhaltsverzeichnis

1 Präambel

Geltungsbereich der Richtlinie

Abkürzungsverzeichnis

SAP Glossar

2 Allgemeines

3 Organisation

3.1 Lizenzen und Pflegekosten

3.2 Supportlevel

3.3 Systemerweiterungen und Releasewechsel

4 Betrieb

4.1 Technische Vorgaben

4.2 Organisatorische Vorgaben

4.3 Schnittstellen

5 Datenschutz und IT-Sicherheit

5.1 Rollen und Berechtigungen

5.2 Secure Network Communication (SNC)

6 Inhaltliche Vorgabe

6.1 Fachkonzepte

6.2 Modulspezifische Vorgaben

7 Erläuterungen zur Richtlinie des verteilten NFM-Betriebes

8 Inkrafttreten, Außerkrafttreten

1 Präambel

Diese Richtlinie dient der Organisation und Steuerung eines verteilten Betriebes im Neuen Finanzmanagement (NFM) (vgl. Geltungsbereich der Richtlinie).

Hierdurch wird die Zusammenarbeit zwischen den beteiligten Organisationseinheiten des Landes Brandenburg unter der Maßgabe eines verteilten NFM-Betriebes ausgestaltet. Gegenwärtig sind das Competence Center of Expertise (CCoE) im Ministerium der Finanzen und für Europa (MdFE) und die Landesbetriebe an dieser Zusammenarbeit beteiligt.

Die zentralen Regelungen des Dokumentes sind im Zusammenwirken des CCoE mit den Landesbetrieben entstanden.

Durch die Regelungen dieses Dokumentes werden die Landesbetriebe in die Lage versetzt, den Betrieb ihres Rechnungs­wesens technisch selbstständig, unabhängig und im Ergebnis flexibel durchzuführen. Das nachstehende Regelwerk beschreibt organisatorische, technische und inhaltliche Vorgaben für den NFM-Betrieb in einem verbindlichen Mindestumfang. Diese Vorgaben sind notwendig, um ein standardisiertes Rechnungswesen - im Sinne des Neuen Finanzmanagements - im Land Brandenburg, unter Gewährleistung einer notwendigen Zusammenführungsoption, sicherzustellen.

Diese Richtlinie ersetzt mit Inkrafttreten bisher bestehende Vorgaben des Referats 28 im MdFE. Der durch diese Richtlinie verbindlich definierte Mindestumfang berücksichtigt somit die von allen Beteiligten angestrebten Freiheitsgrade, die sich aus den bewusst ungeregelten Sachverhalten ergeben. Mit diesen Möglichkeiten schafft das Land Brandenburg alle denkbaren Freiräume, um den wachsenden und sich ändernden Bedürfnissen der Landesbetriebe gerecht zu werden und gleichzeitig den zentralen NFM-Standard des Landes Brandenburg weiterhin sichern und entwickeln zu können.

Der Verteilungsgrad des NFM-Betriebes soll den Bedürfnissen der Landesverwaltung gerecht werden und weiterhin anpassungsfähig bleiben. Aus diesem Anspruch resultiert einerseits die Möglichkeit eigenverantwortlichen Handelns und anderseits der Auftrag zur Wahrnehmung zentraler Verantwortung für den NFM-Gesamtbetrieb.

Die Zusammenarbeit zwischen CCoE und den Landesbetrieben ist grundsätzlich kooperativ zu gestalten und auf eine optimale Aufgabenerfüllung auszurichten, sofern sich nicht aus der Systemverantwortung gegenüber dem Lizenzgeber SAP oder dem Handeln als zentrale Instanz gegenüber der Landesverwaltung des Landes Brandenburg eine zentrale Regelungshoheit für das CCoE ergibt. Das CCoE und die Landesbetriebe verfolgen im Zuge ihrer Aufgabenerfüllung gemeinsam die Ziele,

Aufgaben klar zu definieren und zuzuweisen,

Aufgaben und Leistungen gegenseitig zu respektieren sowie

voneinander zu lernen und gemeinsam den verteilten NFM-Betrieb zu optimieren.

Das CCoE informiert die Landesbetriebe regelmäßig über allgemeine Entwicklungen im SAP und NFM.

Sollten eine oder mehrere Bestimmungen dieses Dokumentes nichtig sein, so bleiben die übrigen Bestimmungen hiervon unberührt. Die nichtigen Bestimmungen sind durch eine ihrer Zielsetzung am nächsten kommende Regelung zu ersetzen.

In den Erläuterungen zu dieser Richtlinie wird auf einzelne Sachverhalte genauer eingegangen. Dies schießt Regelungen über mögliche Fristen mit ein.

Geltungsbereich der Richtlinie

Diese Richtlinie beschränkt sich vorerst auf die doppisch buchenden Organisationseinheiten der Landesverwaltung Brandenburg, die technisch nicht im zentralen NFM-Verbund produktiv sind.

Abkürzungsverzeichnis

| ADONIS

| Geschäftsprozessmanagementwerkzeug der Firma BOC


| BAPI     

| Business Application Programming Interfaces


| BLB      

| Brandenburgischer Landesbetrieb für Liegenschaften und Bauen


| CATS

| Cross Application Time Sheet


| CCoE    

| Competence Center of Expertise


| EDV      

| Elektronische Datenverarbeitung


| GUI       

| Graphical User Interface (grafische Benutzer­ober­fläche)


| GWG    

| Geringwertige Wirtschaftsgüter


| IT

| Informationstechnologie


| ITIL

| IT Infrastructure Library


| KST       

| Kostenstelle


| LFB       

| Landesbetrieb Forst Brandenburg


| LGB       

| Landesvermessung und Geobasisinformation Brandenburg


| LS         

| Landesbetrieb für Straßenwesen


| LHO       

| Landeshaushaltsordnung


| MdFE    

| Ministerium der Finanzen und für Europa


| MV        

| Modulverantwortlicher/Modulverantwortliche


| NFM      

| Neues Finanzmanagement


| OSS      

| Online Service System


| PSP       

| Projektstrukturelement


| SNC       

| Secure Network Communication


| SolMan

| Solution Manager


| SPS       

| Support Package Stack


| ZIT-BB    

| Brandenburgischer IT-Dienstleister


SAP-Glossar (für dieses Dokument notwendiger Auszug)

Add On

SAP Add On sind ergänzende Lösungen, die den Basis-Funk­tionsumfang von SAP um spezifische Funktionen erweitern. Add On werden sowohl von SAP selbst als auch von zertifizierten Partnern (Software Solution Providers, SSPs) angeboten.

BAPI

Mit der BAPI-Technologie hat die SAP AG eine objektorientierte Technologie in die Software eingeführt. Prozesse und Daten werden in Form von sogenannten SAP-Business-Objekten verfügbar gemacht. Auf die SAP-Business-Objekte können externe Anwendungen über standardisierte, plattformunabhängige Schnittstellen, den sogenannten BAPI, zugreifen. Die SAP-Business-Objekte und ihre BAPIs bieten eine offene, objektorientierte Sicht der Geschäftsprozesse und Daten eines SAP-Systems. Die Einzelheiten des Prozesses sind für das Client-Programm unsichtbar, da die exportierten Datenstrukturen in Objekten gekapselt sind.

Modifikation

Modifikationen sind kundenindividuelle Änderungen an der SAP-Standardsoftware, sie sind nicht releasefest und müssen bei Änderungen seitens SAP überprüft und gegebenenfalls angepasst werden. Ein Wartungsanspruch durch SAP ist nicht gegeben.

User Exit

Vorgedachte Erweiterungsoption des SAP-Standards. Poten­zielle Kundenanforderungen, die nicht als Standard ausgeprägt sind, werden als leere Entwicklungshülse vorgedacht und können beim Anwender des Systems mit eigener Logik (zulässige Eigenentwicklung) ausgestaltet werden.

Modul

Der modulare Aufbau des SAP-Systems entspricht der in vielen Organisationen üblichen Struktur. Die Module sind nicht im informationstechnischen Sinne unabhängig (modular), vielmehr sind die Funktionen eng miteinander verzahnt (Funktionsinte­gration). Module im SAP-Sinne sind zum Beispiel das Modul FI (Finanzwesen) oder CO (Controlling) oder PSM (Public Sector Management).

OSS

Online Support System der SAP AG Walldorf. Die SAP-Produktunterstützung im Rahmen eines Vertrags über Software-Wartung wird weitgehend über im Internet zugängliche Systeme abgewickelt, die unter dem Namen SAP Service Marketplace zusammengefasst werden. Dort können bestimmte SAP-Anwender Problemmeldungen an SAP schicken und weiterverfolgen. Im gleichen Rahmen besteht hier die Möglichkeit, zum Beispiel Dokumentationen, Installationsmedien oder Programmkorrekturen zu beziehen.

SPS

In regelmäßigen Abständen erfolgt das Einspielen des Support Package Stack (von SAP definiertes Paket von Einzelkorrekturen in Form von SAP-Hinweisen).

Damit entfallen umfassende Analysen der Einzelkorrekturen zu den Abhängigkeiten zwischen einzelnen SAP-Hinweisen, da diese bereits durch den Softwarehersteller SAP geprüft werden.

Zentralkonzept (Zentraler Landesstandard NFM)

Im Ergebnis der Einführung des NFM im Land Brandenburg wurden Festlegungen mit dem Ziel der Einführung eines Landesstandards innerhalb der Landesverwaltung getroffen. Durch die Umstellung aller Systeme auf den neuen SAP S/4HANA-Standard werden erweiterte Regelungen/neue Vorgaben notwendig. Diese werden in der Erweiterung zum bisherigen Zentralkonzept formuliert.

Mit Beginn des verteilten Betriebes gelten folgende Sachverhalte zur Beibehaltung konsolidierbarer Ergebnisse

Basisfestlegungen

Hier handelt es sich um Festlegungen allgemeiner Art, die zwingend für alle Landesbehörden einheitlich zu treffen sind. Beispielhaft sei die Festlegung „Euro“ als Währung genannt.

Integrative Sachverhalte

Zur Abgrenzung der einzelnen Behörden sind Stammdatenstrukturen aufzubauen, die die einzelnen Organisationseinheiten voneinander abgrenzen. Beispielhaft sei hier die Nomenklatur der Kostenstellen genannt. Jede Kostenstelle darf nur einmal im System vorkommen und sollte eindeutig einer Organisationseinheit zugeordnet werden können.

Konzeptionelle Sachverhalte

Konzeptionelle Sachverhalte umfassen Festlegungen, die zur Erlangung konsolidierbarer Ergebnisse notwendig sind. Beispielhaft sei der Umgang mit interner Leistungsverrechnung genannt.

Technische Sachverhalte

Zusätzlich gibt es Sachverhalte, deren Standardisierung aus technischen Gründen unumgänglich ist, wie zum Beispiel die Mandantenstruktur.

Fachkonzept

Fachkonzepte stellen auf Grundlage der Sachverhalte des Landesstandards die modulspezifischen Einstellungen in den jeweils doppisch buchenden Landesbetrieben dar. Sie zeigen darüber hinaus die genehmigten Abweichungen und Weiterentwicklungen zu diesem auf.

Die Fachkonzepte beschreiben jedes Modul in sich abgeschlossen. Sie können sich dabei zwischen den einzelnen Landes­betrieben unterscheiden. Die Anzahl der jeweils vorgehaltenen Fachkonzepte richtet sich danach, wie viele Module im Landesbetrieb genutzt werden.

SAP-Modullandschaft

Das SAP ERP hat einen modularen Aufbau. Die Gesamtheit aller der in der ausgeprägten Installation genutzten Module wird als Modullandschaft bezeichnet.

Die Module der Anwendungsbereiche Rechnungswesen, Logistik und Personalwirtschaft unterteilen sich weiter in Komponenten.

Die Module innerhalb der Modullandschaft sind im informationstechnischen Sinne voneinander abhängig (Funktionsintegration).

2 Allgemeines

Das CCoE sichert folgende Verträge exklusiv für alle Bereiche der Landesverwaltung des Landes Brandenburg:

Rahmenverträge:


SAP

Betriebsverträge:


SAP-technischer Betrieb (Hosting)

Ende-zu-Ende-Verschlüsselung (SNC).

Das CCoE schreibt gemeinsam mit den Landesbetrieben den technischen SAP-Betrieb (Hosting) aus. Die aus diesen Verträgen abzuleitenden Verantwortlichkeiten obliegen dem Landesbetrieb.

Die Absicherung der Applikationsbetreuung erfolgt durch die Landesbetriebe individuell über eigene Betriebsverträge. Die aus diesen Verträgen abzuleitenden Verantwortlichkeiten obliegen dem Landesbetrieb.

Das CCoE behält sich vor, in Abstimmung mit den obersten Landesbehörden und den ihnen zugeordneten Landesbetrieben die Richtlinie anzupassen (vgl. Erläuterungen).

3 Organisation

3.1 Lizenzen und Pflegekosten

Der Lizenzbestand des Landes Brandenburg wird durch das CCoE verwaltet.

Für die Nutzung in den SAP-Systemen sowie für zentral einzusetzende Software (zum Beispiel Verschlüsselung) werden Softwarelizenzen benötigt. Diese Lizenzen werden durch das CCoE auf Antrag und Genehmigung dem Bedarfsträger zugeteilt. Der Landesbetrieb ist verpflichtet, nicht mehr genutzte Lizenzen dem CCoE zurückzugeben. Das CCoE behält sich in begründeten Fällen vor, Lizenzen unter Einhaltung von Fristen einzuziehen (vgl. Erläuterungen).

Die Systemvermessung wird auf Anforderung des CCoE stichtagsbezogen durch den Landesbetrieb durchgeführt. Auf Verlangen des CCoE kann die Firma SAP (Vertragspartner Enterprise-Support) im Landesbetrieb Vermessungsarbeiten durchführen. Die Ergebnisse dieser Vermessung sind dem CCoE dann im Originalformat vorzulegen (vgl. Erläuterungen).

Die Pflegekosten für Softwarelizenzen sind durch den Landesbetrieb zu tragen. Diese orientieren sich an den durch den Landesbetrieb genutzten Lizenzen und werden auf Basis eines landesweit abgestimmten Verteilungsschlüssels ermittelt (vgl. Erläuterungen).

3.2 Supportlevel

Die Supportstruktur ist gemäß ITIL in drei Ebenen zu organisieren (1st, 2nd und 3rd Level Support). Nachstehende Struktur wird empfohlen:

Mindestaufgabenstruktur für den 1st Level Support:

Betriebsverantwortlicher/Betriebsverantwortliche

namentlich zu benennender Ansprechpartner, zu benennende Ansprechpartnerin für das CCoE

Schnittstelle zwischen Key-User/Modulverantwortlichem oder Modulverantwortlicher und der Haus-IT zum 2nd Level Support einschließlich Budgetverwaltung

Bindeglied zum CCoE

Organisation, Koordination und Leitung von eigenen SAP-Projekten (zum Beispiel Umstrukturierung)

Koordinieren der Arbeiten im Betrieb mit den Modulverantwortlichen

Koordinierung des Schulungsbedarfs

Key-User/Modulverantwortlicher oder Modulverantwortliche (MV)

(MV ist Teilmenge der Key-User)

Erster Ansprechpartner für den Endanwender SAP

Bearbeitung von Support- und Changeprozessen im Meldungstool (SolMan) für das jeweilige Modul


Überprüfung der Änderung auf Vereinbarkeit mit den vom CCoE vorgegebenen Richtlinien

Überprüfung der Umsetzbarkeit

Erarbeiten und Dokumentieren von Lösungsvorschlägen

Abstimmung der Modulverantwortlichen untereinander

Steuerung von Test- und Entwicklungsprozessen für die Inhalte der jeweiligen Module; gegebenenfalls Beauftragung 2nd Level Support

Überwachung und Steuerung des 2nd und 3rd Level Support, einschließlich Test und Abnahme der Änderungen

Einarbeiten von umgesetzten Änderungen in die Fachkonzepte

Benutzer/Berechtigungen

Haus-IT/Netzwerk (SAP-Basis)

Gewährleistung des technischen Supports

Planung, Aufbau und Administration des SAP-Systems

Administration des Meldungstools (SolMan), einschließlich der Administration des Korrektur- und Transport­wesens innerhalb des SAP-Systems

Administration der Schnittstellen

Administration des Frontendsystems (SAP-GUI) und der Druckereinrichtung

3.3 Systemerweiterungen und Releasewechsel

Genehmigungen für Modifikationen sind durch den Landesbetrieb beim CCoE zu beantragen (vgl. Erläuterungen).

Genehmigungen für Erweiterungen im Rahmen von User Exit, BAPI, Add On etc. sind durch die Betriebsverantwortlichen beim CCoE zu beantragen (vgl. Erläuterungen). Die Entwicklerrichtlinien SAP des Landes Brandenburg sind zwingend zu beachten.

Die Gestaltung der SAP-Modullandschaft der Landes­betriebe ist grundsätzlich dem CCoE vorbehalten. Die Nutzung der Module Finanzwesen (FI), Anlagenbuchhaltung (FI-AA) und Controlling (CO) im Land Brandenburg ist fest vorgeschrieben. Die Einführung von weiteren Modulen ist möglich (vgl. Erläuterungen).

Releasewechsel durch den Landesbetrieb sind dem CCoE vor Durchführung anzuzeigen (vgl. Erläuterungen).

Die Landesbetriebe sind verpflichtet, die SAP-Systeme auf einem aktuellen Stand zu halten: Neben dem Releasewechsel betrifft dies auch das Durchführen von SPS-Projekten (SAP-Hinweise).

4 Betrieb

4.1 Technische Vorgaben

Als technisches Administrationswerkzeug ist der Solution Manager zu verwenden.

Für Änderungen und Support ist der Solution Manager zu verwenden.

4.2 Organisatorische Vorgaben

Die Prozesse zwischen Dienstleister und Landesbetrieb sind im Rahmen des Hosting- und Applikationsvertrags zu beschreiben. Die internen Prozesse und Verantwortlichkeiten des Landesbetriebes sind unter Berücksichtigung der ressortspezifischen Vorgaben ebenfalls zu dokumentieren. Bezüglich dieser Dokumentationen hat der Landesbetrieb mindestens ein Dokument zu erstellen. Darüber hinaus hat der Landesbetrieb ein Notfallhandbuch zu erstellen. Diese Dokumentationen sind aktuell zu halten und auf Anforderung dem CCoE vorzulegen (vgl. Erläuterungen).

Die Berechtigung zur Vergabe, Verwaltung und zum Entzug von Entwickler- und Objektschlüsseln (SSCR-Schlüsseln) wird durch das CCoE personengebunden zugewiesen. Die Zuweisung wird auf die Installationsnummern der SAP-Systeme des Antragstellers beschränkt (vgl. Erläuterungen CCoE).

Der Landesbetrieb erhält die Möglichkeit, für seine Installation eigenständig OSS-Meldungen zu erstellen und einzusehen. Diese Möglichkeit, eigene Meldungen auszugeben, kann durch das CCoE beschränkt werden. Diese Beschränkung erfolgt dann, wenn die Qualitätskontrolle der OSS-Meldung durch das CCoE ergibt, dass notwendige Standards (vgl. Erläuterungen) nicht eingehalten werden.

Der Landesbetrieb und seine ihm vorgesetzte oberste Landesbehörde sind gehalten, alle Aktivitäten, die Einfluss auf das NFM-System haben, mittel- und langfristig zu planen und das CCoE darüber zu informieren. Hierzu zählen insbesondere folgende Aktivitäten:

die Anforderung des Lizenzerwerbs an das CCoE,

die Planung von Umstrukturierungsmaßnahmen, wie zum Beispiel:


Fusionen,

Ausgliederungen,

Überführungen in andere Rechtsformen,

Rücküberführung in oberste Landesbehörden.

4.3 Schnittstellen

Setzen die Landesbetriebe Fach- und Vorverfahren zu ihrem NFM-System ein, dann sind diese für die Wirtschaftlichkeit, Ordnungsmäßigkeit und Sicherheit ihrer Verfahren verantwortlich.

Soll die Anbindung oder Veränderung dieser Fach- oder Vorverfahren durch den Landesbetrieb erfolgen, muss der Betriebsverantwortliche oder die Betriebsverantwortliche des Landesbetriebes das CCoE in der Planungsphase zur Beschaffung des Verfahrens unterrichten (vgl. Erläuterungen).

5 Datenschutz und IT-Sicherheit

Dem CCoE sind der oder die IT-Sicherheitsbeauftragte und der oder die Datenschutzbeauftragte in Bezug auf das NFM namentlich zu benennen (vgl. Erläuterungen).

Die Landesbetriebe sind gehalten, ihre SAP-Sicherheitskonzepte auf einem aktuellen Stand zu halten.

5.1 Rollen und Berechtigungen

Unter Berücksichtigung geltender Vorschriften (unter anderem Landeshaushaltsordnung, Brandenburgisches Datenschutzgesetz, Sicherheitsrichtlinien) - vorbehaltlich lizenzrechtlicher Fragestellungen - ist der Landesbetrieb in der Gestaltung seiner Rollen und Berechtigungen grundsätzlich frei. Das CCoE empfiehlt, das zum Übergabezeitpunkt angewendete Rollen- und Berechtigungskonzept (Fachkonzept) beizubehalten.

Der Landesbetrieb ist verpflichtet, ein Rollen- und Berechtigungskonzept vorzuhalten und fortzuschreiben.

Der Landesbetrieb ist verpflichtet, die technischen Umsetzungsstände dieses Rollen- und Berechtigungskonzeptes zu dokumentieren. Die Dokumentation ist dem CCoE auf Verlangen vorzulegen (vgl. Erläuterungen).

5.2 Secure Network Communication (SNC)

Die technische Kommunikation zwischen den SAP-Clients und den Servern im Rechenzentrum beim Dienstleister ist Ende-zu-Ende zu verschlüsseln. Die Produktvorgabe und der Betrieb erfolgt durch das CCoE.

Die Anbindung der SAP-Server und SAP-Clients an die zentrale SNC-Infrastruktur liegt in der Zuständigkeit der Landesbetriebe.

6 Inhaltliche Vorgabe

6.1 Fachkonzepte

Jeder Landesbetrieb ist verpflichtet, ein auf sein spezifisches Bedürfnis zugeschnittenes Fachkonzept für die produktiv eingesetzten SAP-Module zu erstellen, zu pflegen und auf Verlangen dem CCOE vorzulegen (vgl. Erläuterungen zu Nummer 6.2).

6.2 Modulspezifische Vorgaben

6.2.1 Doppik/Finanzbuchhaltung (Modul FI)

6.2.1.1 Geschäftsjahresvariante

Geschäftsjahresvariante K4 muss beibehalten werden.

6.2.1.2 Buchungsschlüssel

Buchungsschlüssel sind gemäß Zentralkonzept zu verwenden. Neudefinitionen müssen beim CCoE beantragt werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.1.3 Sachkonto

Die Sachkontenanlage erfordert die Genehmigung durch das CCoE. Die Neuanlage von sekundären Kostenarten (9’er Bereich) ist dem CCoE gegenüber nur noch anzeigepflichtig (vgl. Erläuterungen zu Nummer 6.2).

In SAP S/4HANA ist die Sachkontenanlage mit der Sachkontenart Sekundärkost dem CCoE gegenüber ebenfalls nur anzeigepflichtig.

Bestimmungsmerkmale von Sachkonten erfolgen durch das CCoE nach Vorschlag des Landesbetriebes zentral (vgl. Erläuterungen zu Nummer 6.2).

6.2.1.4 Debitor/Kreditor/Geschäftspartner

Die Nomenklatur der Kontengruppen (Debitor/Kreditor) sowie der Gruppierungen (Geschäftspartner) und die gesteuerten Merkmale der Kontengruppen und Gruppierungen müssen erhalten bleiben.

Neue Kontengruppen/Gruppierungen und ihre gesteuerten Merkmale müssen beim CCoE beantragt werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.1.5 Belegarten

Neue Belegarten oder deren Änderungen sind mit ihren Bestimmungsmerkmalen beim CCoE zu beantragen (vgl. Erläuterungen zu Nummer 6.2).

6.2.1.6 Periodische Arbeiten: Mahnen

Neue Mahnverfahren oder deren Änderungen sind mit ihren Bestimmungsmerkmalen beim CCoE zu beantragen (vgl. Erläuterungen zu Nummer 6.2).

6.2.2 Kosten- und Leistungsrechnung (Modul CO)

6.2.2.1 Kostenartenhierarchie

Die Kostenartengruppe KOA_GES darf nicht geändert werden. Auch eine Erweiterung ist nicht zulässig.

6.2.2.2 Kostenstellenstandardhierarchie

Der oberste Knoten der KST-Standardhierarchie wird wie folgt benannt:

| •

| BB         

| Land Brandenburg


| •

| S

| Staatskanzlei


| •

| F0

| Ministerium der Finanzen und für Europa


| •

| I

| Ministerium des Innern und Kommunales


| •

| J

| Ministerium der Justiz


| •

| A

| Ministerium für Soziales, Gesundheit, Integration und Verbraucherschutz


| •

| B

| Ministerium für Bildung, Jugend und Sport


| •

| L

| Ministerium für Landwirtschaft, Umwelt und Klimaschutz


| •

| V

| Ministerium für Infrastruktur und Landesplanung


| •

| T0

| Ministerium für Wirtschaft, Arbeit und Energie


| •

| W

| Ministerium für Wissenschaft, Forschung und Kultur


| •

| P

| Landtag


| •

| R

| Landesrechnungshof


| •

| G 

| Verfassungsgericht


6.2.2.3 Nummernkreisintervall Kostenstellen

Vorhandene Nummernkreisintervalle müssen beibehalten werden.

6.2.2.4 Nummerierung der Leistungsarten

Der Landesstandard gibt fünf verbindliche Leistungsarten vor:

einfacher Dienst

mittlerer Dienst

gehobener Dienst

höherer Dienst A

höherer Dienst B

Diese sind mindestens zu berücksichtigen.

6.2.2.5 Numerik der Produkte

Vorhandene Nummernkreisintervalle müssen beibehalten werden.

6.2.2.6 Numerik für Querschnittsprodukte/Fachprodukte

Die vorgegebenen statistischen Querschnittsprodukte und der durch das MdFE bestätigte Produktkatalog des Bund-Länder-Arbeitskreises in der bestätigten Fassung sind zwingend zu verwenden. Eine Änderung dieser ist nicht zulässig. Ein einheitlicher Wechsel auf die echten und erweiterbaren Querschnittsprodukte des kameralen Systems ist möglich und beim CCoE zu beantragen (vgl. Erläuterungen zu Nummer 6.2).

6.2.3 Cross Application Time-Sheet (Modul CATS)

6.2.3.1 Numerik Personalbereich/Teilbereich/-nummern

Nummernkreisobjekte im Personalbereich sind so beizubehalten, wie sie übergeben wurden. Notwendige Änderungen obliegen dem Vorbehalt durch das CCoE (vgl. Erläuterungen zu Nummer 6.2).

6.2.3.2 Mitarbeitergruppen

Die vorhandenen Mitarbeitergruppen sind zwingend beizubehalten. Eine Anpassung ist nur durch Zentralvorgabe des CCoE zulässig (vgl. Erläuterungen zu Nummer 6.2).

6.2.3.3 Infotypen

Es sind nachfolgende Infotypen zu pflegen:

0000 Maßnahmen

0001 organisatorische Zuordnung

0002 Daten zur Person

0105 Kommunikation

0315 Vorschläge Arbeitszeitblatt

Die vorhandenen Infotypen mit ihren Steuerungsmerkmalen sind beizubehalten. Eine Anpassung ist nur durch Zentralvorgabe des CCoE zulässig (vgl. Erläuterungen zu Nummer 6.2).

6.2.4 Projektsystem (Modul PS)

6.2.4.1 Neuanlage und Änderung von Schlüsseln

Änderungen und Neuanlage von Schlüsseln für

die Bezeichnung des Verantwortlichen

die Bezeichnung des Antragstellers

die Benutzerfelder

die Projekt-ID

die PSP-Elemente-Gruppen

die Projektklassen

das Projektprofil

das Selektionsschema

das Abrechnungsprofil

sind durch das CCoE zu genehmigen (vgl. Erläuterungen zu Nummer 6.2).

6.2.4.2 Projektedition

Die bei Übergabe erlaubten Zeichen für die Gliederung der Projektnummer, von Projektdefinition und PSP-Elementen sind nicht zu ändern.

6.2.5 Materialwirtschaft (Modul MM)

6.2.5.1 Materialarten

Für das Land Brandenburg werden folgende Materialarten verwendet:

BB Geschäftsbedarf

BB Reparaturmaterial

BB Betriebsstoffe

BB Ausstattung/Geräte

BB Dienstleistungen

BB Rechte/Dienste

Die vorhandenen Materialarten sind beizubehalten. Neue Materialarten dürfen nur nach Genehmigung des CCoE angelegt werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.5.2 Warengruppenstrukturen und Bewertungsklassen

Zusammen mit anderen Faktoren bestimmt die Bewertungsklasse die Sachkonten, die bei einem bewertungsrelevanten Vorgang (zum Beispiel Warenbewegung) fortgeschrieben werden. Die vorhandenen Warengruppenstrukturen und Bewertungsklassen - inklusive ihrer Zuordnung - sind beizubehalten. Anpassungen dürfen nach Genehmigung des CCoE vorgenommen werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.5.3 Kontierungstypen

Für das Land Brandenburg sind folgende Kontierungstypen relevant:

BB Auftrag

BB Kostenstelle

BB Anlagenverrechnung

BB Anlage

BB Produkt/Kostenstelle

BB Projekt

BB Immobilien

Unbekannt

Die vorhandenen Kontierungstypen sind unverändert beizubehalten. Erweiterungen sind genehmigungspflichtig (vgl. Erläuterungen zu Nummer 6.2).

6.2.5.4 Belegarten

Die mit Übergabe des Systems vorhandenen Belegarten sind unverändert weiter zu verwenden.

Neue Belegarten oder deren Änderungen sind mit ihren Bestimmungsmerkmalen beim CCoE zu beantragen (vgl. Erläuterungen zu Nummer 6.2):

Belegarten für Beschaffungsanträge

Belegarten für Anfragen

Belegarten für Bestellungen

Belegarten für Rahmenverträge

Belegarten für Material und Inventur

6.2.6 Instandhaltung (Modul PM)

6.2.6.1 Typen für technische Plätze

Für das Land Brandenburg sind folgende Typen für technische Plätze relevant:

| •

| I

| RE Immobilien


| •

| M

| Technisches System - Standard


| •

| S

| Kundenplatz


| •

| H

| Hochbau


| •

| Z

| Zentrale


Typen für technische Plätze sind beizubehalten. Notwendige Änderungen obliegen dem Vorbehalt durch das CCoE (vgl. Erläuterungen zu Nummer 6.2).

6.2.6.2 Equipmenttypen

Für das Land Brandenburg sind folgende Equipmenttypen relevant:

| •

| G

| Geräte - Gerätenachweis mit Wartungsplanung und Fristenverfolgung


| •

| K

| Kraftfahrzeuge


| •

| A

| Anhänger


| •

| H

| Hochbau


| •

| B

| Gruppengeräte (GWG in Gruppen zusammengefasst zur Wartungsplanung)


| •

| I

| Inventar-GWG (Nachweis ohne Wartungsplanung und Fristenverfolgung)


| •

| T

| Technische Anlagen BLB


Typen für Equipment sind beizubehalten. Notwendige Änderungen obliegen dem Vorbehalt durch das CCoE (vgl. Erläuterungen zu Nummer 6.2).

6.2.7 Vertrieb (Modul SD)

6.2.7.1 Materialarten

Für das Land Brandenburg werden folgende Materialarten verwendet:

BB Geschäftsbedarf

BB Reparaturmaterial

BB Betriebsstoffe

BB Ausstattung/Geräte

BB Dienstleistungen

BB Rechte/Dienste

BB Produkte

Die vorhandenen Materialarten sind beizubehalten. Neue Materialarten dürfen nur nach Genehmigung des CCoE angelegt werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.7.2 Warengruppenstrukturen und Bewertungsklassen

Zusammen mit anderen Faktoren bestimmt die Bewertungsklasse die Sachkonten, die bei einem bewertungsrelevanten Vorgang (zum Beispiel Warenbewegung) fortgeschrieben werden. Die vorhandenen Warengruppenstrukturen und Bewertungsklassen - inklusive ihrer Zuordnung - sind beizubehalten. Anpassungen dürfen nach Genehmigung des CCoE vorgenommen werden (vgl. Erläuterungen zu Nummer 6.2).

6.2.7.3 Kontierungstypen

Für das Land Brandenburg sind folgende Kontierungstypen relevant:

BB Auftrag

BB Kostenstelle

BB Anlagenverrechnung

BB Anlage

BB Produkt/Kostenstelle

BB Projekt

BB Immobilien

Unbekannt

Die vorhandenen Kontierungstypen sind unverändert beizubehalten. Erweiterungen sind genehmigungspflichtig (vgl. Erläuterungen zu Nummer 6.2).

6.2.7.4 Belegarten

Die mit Übergabe des Systems vorhandenen Belegarten sind unverändert weiter zu verwenden.

Neue Belegarten oder deren Änderungen sind mit ihren Bestimmungsmerkmalen beim CCoE zu beantragen (vgl. Erläuterungen zu Nummer 6.2):

Belegarten für Kundenanfragen

Belegarten für Kundenauftragsarten

Belegarten für Lieferarten

Belegarten für Rahmenverträge

Belegarten für Fakturen

7 Erläuterungen zur Richtlinie des verteilten NFM-Betriebes

Zu Nummer 1 Präambel

Die nachfolgenden Erläuterungen konkretisieren die in den Richtlinien des CCoE für die Steuerung eines verteilten NFM-Betriebes im Land Brandenburg allgemein formulierten Bestimmungen.

Hierbei werden insbesondere die einzuhaltenden Prozesswege zwischen den verschiedenen Beteiligten festgelegt. Die Festlegungen beziehen sich dabei nur auf die Prozesse, bei denen das CCoE zwingend involviert ist. Bei den Prozessen zwischen dem Landesbetrieb und Dritten besteht dagegen Ausgestaltungsfreiheit.

Wird in diesem Dokument auf Antragsformulare referenziert, so werden diese durch das CCoE über das Intranet (BB-intern) zur Verfügung gestellt. Für den Fall fehlender Formulare können diesbezügliche Anträge formlos gestellt werden.

In gemeinsamer Abstimmung zwischen dem CCoE und den Landesbetrieben kann die Richtlinie angepasst werden.

Prozess

Änderungsbedarf an der Richtlinie kann seitens des CCoE oder der Landesbetriebe entstehen. Das CCoE oder die Landesbetriebe erarbeiten einen Änderungsvorschlag, der gemeinsam besprochen und entsprechend angepasst wird. Die Fachaufsicht der Landesbetriebe ist zu beteiligen.

Eine Änderung der Richtlinien mit Systemrelevanz führt möglicherweise zu einem Folgeprozess (vgl. Erläuterungen zu Nummer 6.2).

Zu Nummer 3.1 Lizenzen und Pflegekosten

Folgende Lizenztypen werden bisher durch das CCoE zentral vorgehalten:

Verschlüsselungslizenz (SNC)

Developer

Professional

Limited Professional

Sondernutzer 15 Transaktionen

Employe CATS Eigene Zeiterfassung

Sondernutzer Employe CATS Sammelerfassung

HANA-Datenbank

1. Für die Umstellung der SAP-Systeme auf S/4HANA wurde 2021 für den gesamten Lizenzbestand eine „Contract Conversion“ durchgeführt. Dadurch ergibt sich folgendes Mapping der bisher verwendeten Lizenzen unter Beibehaltung der bisherigen Anzahl der im Land genutzten Lizenzen, inklusive der HANA-Datenbank.

| 


Altprodukte

| 


S/4HANA Conversion Produkte

| 


SAP Business Suite Developer

| 


S/4HANA, Developer access

| 


SAP Business Suite Professional

| 


S/4HANA Enterprise Management for Professional Use

| 


SAP Business Suite Limited Professional

| 


SAP SN 15 Transaktionen

| 


SAP SN Employe CATS Sammelerfassung

| 


SAP SN Employe CATS Eigene Zeiterfassung

| 


S/4HANA Enterprise Management for Productivity Use

| 


SAP Real Estate Mgmt. -

Office, Retail + Ind.

| 


S/4HANA contract, lease and real estate management

| 


Verschlüsselungslizenz (SNC)

| 


SAP Single Singn-On

Das Mapping der bisher verwendeten Lizenzen in die S/4HANA-Produkte erfolgt mit der Durchführung der im Land erforderlichen Umstellungsprojekte auf S/4HANA. Sobald eine S/4HANA-Umstellung abgeschlossen wurde, sind die neuen Lizenztypen zu verwenden.

2. Zusätzlich wurde zur Anbindung von Nicht-SAP-Systemen an das SAP-System von dem bisher genutzten „Named User-Ansatz“ auf den „Digital Access-Ansatz“ der Indirekten Nutzung gewechselt. Dabei werden künftig nicht mehr die Nutzer, sondern die Anzahl der vom Vorsystem übertragenen Dokumente gezählt.

| 


Lizenztyp

| 


Vermessungseinheit

| 


SAP S/4HANA Digital Access

| 


Anzahl der übertragenen Dokumente

3. Für das SAP Grantor Management werden zentral folgende neue Lizenzen genutzt:

| 


Lizenztyp

| 


Vermessungseinheit

| 


SAP Tax, Benefits and Payment Processing for Public Sector for S/4HANA

| 


Anzahl der im CRM-System eingerichteten Geschäftspartner

Hier nicht aufgeführte Lizenztypen können durch den Landesbetrieb auf eigene Kosten über das CCoE beschafft werden. Dazu hat sich der Landesbetrieb rechtzeitig vor Beschaffung an das CCoE zu wenden.

Unterscheidung Anschaffungs- und Pflegekosten

Lizenzkosten für die Nutzung des SAP-Systems/der SAP-Systeme werden grundsätzlich unterschieden in Anschaffungs- und Pflegekosten:

Anschaffungskosten: Die Anschaffung und die dafür notwendige Bereitstellung von Haushaltsmitteln zentral vorgehaltener Lizenzen obliegen dem CCoE. Diese Lizenzen werden in einen zentralen Lizenzpool eingestellt und bei Bedarf/bei Anfrage an die Landesbetriebe ausgegeben.

Pflegekosten: Durch die Beschaffung von Lizenzen fallen grundsätzlich Pflegekosten an. Der Landesbetrieb ist an diesen zu beteiligen. Diese Beteiligung wird für die zentral vorgehaltenen Lizenztypen und die genutzten Vermessungseinheiten für Digital Access und SAP Grantor Management durch Berechnung einer Umlage und für nicht zentral vorgehaltene Lizenztypen durch unmittelbare Zuordnung ermittelt. Der Landesbetrieb hat entsprechend Haushaltsvorsorge zu tragen.

Lizenzen und Lizenzpool

Lizenzen werden nach Auslastungsgrad im Lizenzpool bei Bedarf durch das CCoE nachbeschafft.

Beantragung Lizenzen aus Lizenzpool

Je nach zu erfüllenden Aufgaben des einzelnen Nutzers in SAP sind die passende Lizenz und die genutzten Vermessungseinheiten für Digital Access und SAP Grantor Management (CRM-System) aus dem Lizenzpool (zentral vorgehaltene Lizenzen) des CCoE rechtzeitig zu beantragen. Hierzu hat der Landesbetrieb einen ausgefüllten Antrag an das CCoE zu übersenden.

Nach dem internen Genehmigungsprozess (maximal acht Wochen) des CCoE wird der Landesbetrieb über die Lizenzbereitstellung beziehungsweise durch eine begründete Ablehnung informiert.

Lizenzen, die dem Landesbetrieb aus dem zentral vorgehaltenen Lizenzpool zugeteilt waren und vom Landesbetrieb nicht mehr benötigt werden, sind zurückzugeben.

Systemvermessung

Für die Ermittlung der Umlage der Lizenz-Pflegekosten ist zyklisch und bei Bedarf eine Systemvermessung durchzuführen1.

Hierzu informiert das CCoE den Landesbetrieb über die anstehende Systemvermessung und gibt den Auftrag, die Vermessung durchzuführen.

Der Landesbetrieb führt im Nachgang die Systemvermessung durch und sendet die Vermessungsstatistiken und die Protokolle der Systemvermessungen an das CCoE innerhalb der gesetzten Frist zurück.

Neben den Vermessungen zur Bestimmung der genutzten Lizenztypen für die Berechnung der Lizenz- und Pflegekosten behält sich das CCoE vor, weitere Vermessungen anzufordern.

Berechnung der Lizenz- und Pflegekosten

Das CCoE hält ein Lizenzportfolio vor, um Bedarfsschwankungen innerhalb des Landes kurzfristig - gegebenenfalls auch durch höherwertige Lizenztypen (Lizenzupgrade) - auszugleichen. Die Pflegekosten für Softwarelizenzen sind durch Verträge mit der SAP bestimmt. Der Landesbetrieb beteiligt sich anteilig an diesen Pflegekosten. Dieser Anteil ergibt sich aus einem Einzel- und Gemeinkostenanteil.

Einzelkosten

Sämtliche direkt zuordenbare Pflegekosten je Lizenztyp sind Einzelkosten.

Gemeinkosten

Sämtliche nicht direkt zuordenbare Pflegekosten sind Gemeinkosten.

Verteilungsschlüssel der Gemeinkosten

Die Gemeinkosten werden über einen Schlüssel landesweit umgelegt. Die Höhe des durch den Landesbetrieb zu tragenden prozentualen Gemeinkostenanteils errechnet sich aus dem Verhältnis der Einzelkosten je durch die Behörde genutzter Lizenzen zu den Pflegekosten der gesamten genutzten Lizenzen im NFM-Verbund.

Nutzerzahl

Maßstab für die Nutzerzahl bei der Berechnung der Pflegekosten ist die Anzahl der genehmigten Einzellizenzanträge. Sollte eine Vermessung zum Ergebnis führen, dass der Landesbetrieb mehr als durch das CCoE genehmigte Nutzer im System hat, werden als Maßstab für die Nutzeranzahl diese zugrunde gelegt (vergleiche Fußnote 1).

Berechnung der Einzelkosten für jeden Lizenztyp

Die Höhe des Betrags der durch den Landesbetrieb zu tragenden Pflegekosten pro genutzte Lizenz ergibt sich aus den Pflegekosten gemäß SAP-Rahmenvertrag pro Lizenz multipliziert mit der Zahl der tatsächlichen Nutzungsdauer des Landesbetriebes in Tagen geteilt durch 360.

Zahlungsverkehr

Die Pflegekosten sind in drei Abschlagszahlungen (30. März; 30. Juni; 30. September) und einer abschließenden Endabrechnung (15. Dezember) an das MdFE zu entrichten.

Die Summe der einzelnen in gleicher Höhe zu leistenden Abschlagszahlungen (30. März; 30. Juni; 30. September) im Folgejahr bestimmt sich aus den tatsächlich dem Landesbetrieb zugeordneten Pflegekosten (Einzel- und Gemeinkosten) des laufenden Jahres.

Für den Fall, dass dem Landesbetrieb mit Erstellen der End­abrechnung eine Gutschrift zusteht, wird ihm diese mitgeteilt.

Zu Nummer 3.3 Systemerweiterungen und Releasewechsel

Modifikationen, User Exit, BAPI, Add On, SPS etc.

Der Landesbetrieb hat mit seinem Antrag folgende Nachweise vorzulegen:

Änderungsantrag (Change) beim Systembetreiber einschließlich der Bestätigung der generellen Umsetzbarkeit

Erforderlichkeit des Vorhabens einschließlich der Prüfung von Alternativen (zum Beispiel SAP-Hinweise, OSS etc.)

Nach dem internen Genehmigungsprozess (maximal acht Wochen) des CCoE wird der Landesbetrieb über die Genehmigung, gegebenenfalls mit Auflagen, beziehungsweise durch eine begründete Ablehnung informiert.

SAP-Modullandschaft

Der Landesbetrieb hat mit seinem Antrag über die Einführung oder den Wegfall von Modulen folgende Nachweise vorzulegen:

Änderungsantrag (Change) beim Systembetreiber einschließlich der Bestätigung der generellen Umsetzbarkeit

Erforderlichkeit des Vorhabens einschließlich der Prüfung von Alternativen

Genehmigung der Fachaufsicht

Darstellung erwarteter Lizenzbedarf

Wirtschaftlichkeitsbetrachtung

Nach dem internen Genehmigungsprozess (maximal acht Wochen) des CCoE wird der Landesbetrieb über die Genehmigung, gegebenenfalls mit Auflagen, beziehungsweise durch eine begründete Ablehnung informiert.

Releasewechsel

Der Landesbetrieb hat unaufgefordert und unverzüglich das CCoE über den Releasewechsel (geplantes Produktivsetzungsdatum, neuer Releasestand) zu informieren.

Mit dem Releasewechsel einhergehende (auch außerplanmäßige) finanzielle Auswirkungen gehen zu Lasten des Landesbetriebes.

Zu Nummer 4.2 Organisatorische Vorgaben

Entwicklerschlüssel

Grundsätzlich wird die Verwaltung der Entwicklerschlüssel für die SAP-Systeme über einen SAP-Marktplatz-Nutzer durchgeführt.

Dazu übersendet der Landesbetrieb bei Bedarf einen ausgefüllten personenscharfen SAP-Marktplatz-Nutzerantrag an das CCoE mit der Benennung der Installationsnummern der SAP-Systeme, die von dem Landesbetrieb genutzt werden.

Nach dem CCoE-internen Prozess der Nutzeranlage auf dem SAP-Marktplatz wird der Landesbetrieb über die Anlage des SAP-Marktplatz-Nutzers, inklusive des Initialpasswortes, informiert.

OSS-Meldungen

Notwendige Standards für OSS-Meldungen sind wie folgt definiert:

SAP-Hinweis Nr. 67739 „Definition der Prioritäten“

SAP-Hinweis Nr. 16018 „Situationsbeschreibung“.

Mittel- und langfristige Planung

Der Landesbetrieb hat unaufgefordert das CCoE über Planungen zu Aktivitäten mit Auswirkungen auf das NFM-System zu informieren.

Mit den geplanten Aktivitäten einhergehende (auch außerplanmäßige) finanzielle Auswirkungen gehen zu Lasten des Landesbetriebes.

Zu Nummer 4.3 Schnittstellen

Bei der Planung von Veränderungen an vorhandenen beziehungsweise bei Neuentwicklungen von Schnittstellen ist das CCoE zur Vermeidung wirtschaftlicher Risiken bei den Landesbetrieben rechtzeitig in Kenntnis zu setzen, um mögliche Auswirkungen auf das Lizenzmodell (durch indirekte Nutzung) frühzeitig zu erkennen.

Dazu ist eine Vorhabenbeschreibung in geeigneter - prüfbarer - Form auf Basis des Antragsformulars „Richtlinie CCoE“ aus BB-intern zu übermitteln.

Für die Planung der Digital Access-Lizensierung ist eine Schätzung der Anzahl der durch die Schnittstelle übermittelten Dokumente erforderlich.

Zu Nummer 6.1 Fachkonzepte

Das CCoE fordert die jeweiligen Fachkonzepte direkt beim Landesbetrieb an.

Der Landesbetrieb hat die angeforderten Dokumente zusammenzustellen und an das CCoE zu senden.

Bei Feststellung nicht genehmigter Systemabweichungen wird das CCoE einen entsprechenden Genehmigungsprozess initiieren.

Führt dieser initiierte Genehmigungsprozess zu einer Ablehnung, veranlasst das CCoE - gegebenenfalls mit einer angemessenen Fristsetzung (Einzelfallentscheidung) - den Landesbetrieb, die Rücknahme des Sachverhalts zu seinen Lasten vorzunehmen.

Der Landesbetrieb informiert das CCoE über die erfolgte Rücknahme.

Zu Nummer 6.2 Modulspezifische Vorgaben

In Kapitel „6.2 Modulspezifische Vorgaben“ der Richtlinien des CCoE für die Steuerung eines verteilten NFM-Betriebes im Land Brandenburg wird an verschiedenen Stellen von einer Beantragung, Genehmigung oder dem Vorbehalt durch das CCoE im Zusammenhang mit der Anpassung von modulspezifischen Einstellungen gesprochen.

Genehmigung von modulspezifischen Anpassungen der Module FI, CO, CATS, PS, MM, PM, SD

Neudefinitionen müssen beim CCoE beantragt werden.

(…) erfordert die Genehmigung durch CCoE.

(…) obliegen dem Vorbehalt durch das CCoE.

usw.

Der Landesbetrieb hat mit seinem Antrag folgende Nachweise vorzulegen:

Änderungsantrag (Change) beim Systembetreiber einschließlich der Bestätigung der generellen Umsetzbarkeit

Erforderlichkeit der modulspezifischen Anpassungen einschließlich der Prüfung von Alternativen

Nach dem internen Genehmigungsprozess (maximal acht Wochen) des CCoE wird der Landesbetrieb über die Genehmigung, gegebenenfalls mit Auflagen, beziehungsweise durch eine begründete Ablehnung informiert.

Nach Genehmigung der modulspezifischen Einstellungen werden diese dann eine Zentralvorgabe im Sinne des NFM-Landes-Standards.

Der NFM-Landes-Standard wird durch das CCoE in seinen zentralen Vorgaben in Dokumenten nachgehalten, die den Landesbetrieben im gleichen Sinne wie der Verwaltungskonten­rahmen (VKR) zur Einsicht bereitgestellt wird.

8 Inkrafttreten, Außerkrafttreten

Diese Richtlinien treten am Tag nach der Veröffentlichung im Amtsblatt für Brandenburg in Kraft.

Gleichzeitig treten die Richtlinien des CCC für die Steuerung eines verteilten NFM-Betriebes im Land Brandenburg (nebst Durchführungsbestimmungen) vom 24. März 2010 (ABl. S. 619), die durch die Bekanntmachung vom 10. Oktober 2012 (ABl. S. 1615) geändert worden sind, außer Kraft.

1 Unregelmäßigkeiten zwischen den tatsächlich genutzten und den beantragten Lizenzen beim Landesbetrieb können zu Nachzahlungen an SAP führen. Diese Kosten sind durch den verursachenden Landesbetrieb zu tragen.
