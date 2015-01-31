# Anlage 3 (zu § 18 Abs. 4)
Rahmenlastenheft über Integrierte Regionalleitstellen im Freistaat Sachsen (Rahmenlastenheft)
Inhaltsverzeichnis
Inhaltsverzeichnis
Lfd. Nr. | Titel
1. | Leitstellenstruktur
1.1 | Begriffe
1.2 | Aufgaben der Technikzentralen
1.3 | Leitstellennetzwerk
2. | Prozesse
3. | Daten- und Informationsfluss
3.1 | Datenverarbeitung
3.2 | Mindestanforderungen
4. | Technische Anforderungen
4.1 | Grundsätzliche Anforderungen
4.2 | Systembezogene Anforderungen
4.2.1 | Hard- und Softwarekonzept
4.2.2 | Rollenkonzept/Berechtigungsverwaltung im System
4.2.3 | Definition der Arbeitsplätze
4.2.4 | Einsatzleitsystem (ELS)
4.2.5 | Funk-/Notruf-Abfragesystem (FNAS)
4.2.6 | Audiodokumentationsanlage
4.2.7 | Anbindung peripherer Systeme
4.2.8 | Alarmierungsnetze
4.2.9 | Wachalarmsystem
4.2.9.1 | Bedienung
4.2.9.2 | Anschaltung Alarmtableaus
4.2.10 | Statusinformation
4.2.11 | Betriebs- und Sonderfunk
4.2.12 | Sonstige Einrichtungen der IRLS
4.2.12.1 | Audio-Visuelle-Medien
4.2.12.2 | Einsatznachbereitung und -abrechnung
4.2.12.3 | Fahrzeugortung
4.2.13 | Qualitätsmanagementsystem Rettungsdienst
4.2.13.1 | Grundlagen des Qualitätsmanagementsystems
4.2.13.2 | Voraussetzungen der Mobilen Datenerfassung
4.2.13.3 | Einsatzdaten aus der Mobilen Datenerfassung
4.2.14 | Schnittstellen
4.2.14.1 | Grundsätzliche Anforderungen an Schnittstellen
4.2.14.2 | Grundsätze des Betriebes der Schnittstellen
4.2.14.3 | Schnittstellen mit einheitlichen Funktionen
4.2.15 | Übertragungsnetze
4.3 | Leitstellenbezogene Anforderungen
4.3.1 | Raumfunktionskonzept
4.3.2 | Technikräume
4.3.3 | Raum für Disponentenarbeitsplätze (Leitstellenraum)
4.3.3.1 | Ergonomische Anforderungen
4.3.3.2 | Beleuchtung
4.3.3.3 | Lärmschutz
4.3.3.4 | Klimatechnik
4.3.3.5 | Drucker
4.3.4 | Antennenanlagen
4.3.5 | Stromversorgung
4.3.5.1 | Anforderungen
4.3.5.2 | Unterbrechungsfreie Stromversorgung (USV)
4.3.5.3 | Netzersatzanlage (NEA)
4.3.6 | Haustechnik/Technische Gebäudeausrüstung
5. | Verfügbarkeit
5.1 | Anforderungen an die Verfügbarkeit
5.2 | Grundsätze der inneren Redundanz
5.3 | Grundsätze der externen Redundanz
5.3.1 | Organisatorische Anforderungen
5.3.2 | Konzeptionelle Anforderungen (Redundanzkonzept)
5.3.3 | Technische Anforderungen
6. | Anforderungen an den Betrieb der IRLS
6.1 | Alarm- und Ausrückordnung
6.2 | Dokumentation, Statistik und Archivierung
6.2.1 | Dokumentation
6.2.2 | Statistik
6.2.3 | Archiv
7. | Schulungskonzept
8. | Abkürzungsverzeichnis
1. Leitstellenstruktur
1.1 Begriffe
Der Betrieb der IRLS für Feuerwehr/Rettungsdienst sowie der Lehrleitstelle in der Landesfeuerwehrschule erfolgt innerhalb des im Aufbau befindlichen Leitstellennetzwerks der Behörden und Organisationen mit Sicherheitsaufgaben in Sachsen (BOS-Sachsen). In diesem werden darüber hinaus die besonderen Führungseinrichtungen der unteren Brandschutz-, Rettungsdienst- und Katastrophenschutzbehörden integriert. Kernstück des Leitstellennetzwerks ist das einheitliche ELS aller IRLS und ein gemeinsames FNAS aller BOS auf der Basis von zwei Technikzentralen zur Anschaltung an den Digitalfunk. Erläuterung der im Folgenden verwendeten Begriffe: „Technikzentralen“: Redundant eingerichtete Technikstandorte zur Sicherstellung des Zugangs zum Digitalfunknetz für die Leitstellen und zur Nutzung gemeinsamer Ressourcen. „Leitstellenverbund“: Verbund der IRLS mittels Technikzentralen zur Anbindung an den BOS-Digitalfunk und zur Sicherstellung der Redundanzfunktion. „Leitstellennetzwerk“: Gesamtheit der aktiven Netzwerkkomponenten und notwendigen Übertragungswege zwischen Technikzentralen, den Leitstellen der polizeilichen- und nichtpolizeilichen Gefahrenabwehr sowie der Zugänge zu Alarmierungseinrichtungen und Funknetzen. „Prozess“: Gesamtheit von aufeinander einwirkenden Vorgängen in einem System, durch das Informationen empfangen, umgeformt, transportiert/kommuniziert oder auch gespeichert werden.
1.2. Aufgaben der Technikzentralen
Die wichtigsten Aufgaben der Technikzentralen sind:
1. der zentrale Anschluss der IRLS an die Leitstellenschnittstelle des BOS-Digitalfunks (inklusive Verschlüsselung, Ansteuerung und Konfiguration der Anschaltung und Anschaltungsbaugruppen);
2. die zentrale Bereitstellung von Infrastrukturdiensten (zum Beispiel Anmeldeserver);
3. die zentrale Hardwareüberwachung/Monitoring für FNAS und ELS;
4. die zentrale Bereitstellung der Datenbank des ELS (automatische Synchronisationsfunktion mit Datenbanken der IRLS) als Redundanz- und Rückfallebene bei Ausfall der operativen Datenbank einer IRLS;
5. die zentrale Realisierung der Telefonbuchdatenbank Sachsen (ZTDB);
6. die zentrale Bereitstellung der Datenbank für Digitalfunkendgeräte;
7. die zentrale Sicherstellung des Telefonübergangs für die Digitalfunkteilnehmer im Leitstellenbereich sowie die Sicherstellung eines UMS-Dienstes und einer Telefonalarmierung für alle Leitstellen im Freistaat Sachsen;
8. die zentrale Sicherstellung des sekundären Notrufanschlusses und Weiterleitung an einen Standort des Notdienstträgers ohne Notrufanschluss;
9. die zentrale Bereitstellung des nutzereigenen Managements im Digitalfunk für die Leitstellen;
10. die zentrale Bereitstellung von Konfigurations- und Administrationswerkzeugen für die Leitstellen zur Nutzer-, Rollen- und Rechteverwaltung aller Systeme im Verantwortungsbereich der Leitstellen;
11. die zentrale Bereitstellung von Geo-Basisdaten auf Basis einer Geodateninfrastruktur mit den Leitstellen (Datenpflege und permanente Fortführung durch den Bereich Geoadministration der BOS Sachsen oder der Geoadministration der jeweils zuständigen IRLS);
12. der zentrale Betrieb des Systemdienstes FMS/SDS/GPS aller Kräfte und Mittel;
13. die zentrale Realisierung der Sprachaufzeichnung von Digitalfunkgesprächen mit Systeminformationen sowie bei Bedarf eine Backup-Aufzeichnung von Notrufen mit Gesprächsdaten und von Telefongesprächen (unabhängig von der Aufzeichnung in den IRLS);
14. die Ermöglichung einer Konfiguration und Wartung von Arbeitsplätzen und den zugehörigen Bedienoberflächen;
15. die Ermöglichung der Einrichtung der Notruf-, Draht- und Funkanschaltung (pegel- und funktionsgerecht) und der Bedienoberflächen;
16. die Sicherstellung der Redundanz der jeweils anderen Technikzentrale.
1.3 Leitstellennetzwerk
Das Leitstellennetzwerk hat umfassend sicherzustellen, dass auch für gemeinsam genutzte zentrale Anlagen eine vollständige Mehrorganisationsfähigkeit gesichert ist. Für gemeinsam genutzte zentrale Anlagen ist eine entsprechende Nutzer- und Rechteverwaltung vorzusehen, die die Verantwortungsbereiche der jeweiligen Leitstellen trennt und vor dem Zugriff Dritter sichert.
2. Prozesse
Folgende interne und externe Prozesse sind im Rahmen des Betriebes einer IRLS zu realisieren:
1. die Annahme von Hilfeersuchen;
2. die Erstellung und die Bewertung von Meldebildern;
3. die Umsetzung des Meldebildes – Disposition;
4. die Alarmierung der notwendigen und geeigneten Kräfte und Mittel;
5. die Führung der Kräfte und Mittel zum Einsatzort;
6. die Unterstützung der Einsatzleitung vor Ort;
7. die Information notwendiger Stellen, Behörden und Institutionen;
8. die Unterstützung der Dokumentation und Aufbereitung von Lageinformationen;
9. die Bearbeitung von Auskunftsersuchen;
10. der Einsatzabschluss und die Synchronisation von Daten;
11. die Unterstützung bei einsatzvorbereitenden Maßnahmen;
12. die Durchführung von Probe- und Übungsalarmen;
13. die Sicherung des eigenen Dienstbetriebes;
14. die Zusammenarbeit mit anderen IRLS;
15. die Auftragsabwicklung – Feuerwehreinsatz;
16. die Auftragsabwicklung – Rettungsdiensteinsatz;
17. die Auftragsabwicklung – Katastrophenschutz;
18. die Auftragsabwicklung – Großschadenslage;
19. die Bereitstellung von Daten zur Abrechnung und Erstellung von Berichten;
20. die Umsetzung der Einsatzplanung;
21. die Bürokommunikation mit den Verwaltungsbehörden und Externen.
3. Daten- und Informationsfluss
3.1 Datenverarbeitung
In der IRLS werden umfangreich Daten und Informationen vorgehalten, erhoben, verarbeitet, weitergeleitet, gespeichert und bereitgestellt. Die Daten sind dort vorzuhalten, wo sie für das echtzeitfähige Gesamtsystem, für die Sicherstellung der Aktualität, für die Integration und für die volle Funktionsfähigkeit von Rückfallebenen notwendig sind. Parallele Prozesse müssen auf die Daten zugreifen können, ohne dass weiterer Datenpflegebedarf entsteht. Alle Datenänderungen müssen fortlaufend bei der Berechnung und Disposition von Einsatzmittelvorschlägen berücksichtigt werden. Die erforderlichen Informationen (zum Beispiel des Einsatzmanagements, der Statistik, der Einsatzabrechnung) sind dabei zu berücksichtigen.
3.2 Mindestanforderungen
Für die technische Lösung sind die nachfolgenden Mindestanforderungen bezüglich des Daten- und Informationsflusses umzusetzen:
1. die vollständige Abbildung der dargestellten Prozessabläufe der IRLS im ELS durch Nutzung optimaler Kommunikationssysteme;
2. die Meldungssignalisierung/-aufnahme/-übernahme aus dem Kommunikationssystem mit Auflösung der verfügbaren Melderinformation (zum Beispiel Anruferdaten, Standortdaten, Melderdaten);
3. die Meldungsübernahme von angeschlossenen Übertragungseinrichtungen für Brandmeldungen;
4. die automatische Eröffnung von Einsätzen bei elektronischer Übernahme von Einsätzen und Rückbestätigungsinformationen an den Übergebenden (technische und manuelle Quittung);
5. die Möglichkeit der Integration einer skriptgesteuerten Notrufabfrage nach erprobten und geprüften Abfragealgorithmen;
6. die Einsatzmitteldisposition unter Berücksichtigung statischer und dynamischer Daten;
7. die Optimierung des Einsatzmittelvorschlages durch Einbindung von satellitengestützter, zyklischer Ortung aller Einsatzmittel in der Notfallrettung und für ausgewählte Fahrzeuge der Feuerwehr und des Katastrophenschutzes auch über den Leitstellenbereich hinaus mit abgestimmten Einsatzmitteln anderer Leitstellen;
8. die Einleitung und die Überwachung komplexer Alarmierungsvorgänge (zum Beispiel Wachalarm, analoge und digitale Alarmierung, Alarmserver für Telefon/SMS/Fax);
9. die echtzeitnahe Einleitung und Überwachung des einsatzbezogenen Informationsaustausches zwischen der IRLS, Einsatzkräften/-mitteln und weiteren an der Abwicklung des Einsatzes fachlich Beteiligten;
10. die Zusammenführung und die einfache Recherchierbarkeit aller im Zusammenhang mit einem Einsatz erfassten Daten (zum Beispiel Verbindungsdaten, Sprachdokumentation, Status, Kurznachrichten, Meldungen);
11. der Einsatz eines geografischen Informationssystems (GIS) für die Bereit- und Darstellung navigationsfähiger Vektordaten von:
a)
Karten auf der Grundlage von amtlichen topographischen Geobasisdaten des Staatsbetriebes Geobasisinformation und Vermessung Sachsen;
b)
aktuellen Lagen;
c)
Zuständigkeitsbereichen und Bereichsfolgen;
d)
Verwaltungsstrukturen bis in die Ortsteilebene und Grenzen der Ausrückebereiche;
e)
einer dynamischen Abbildung innerhalb der Hilfsfrist abgedeckter Flächen entsprechend den übermittelten Standortkoordinaten;
f)
Objektinformationen mit Zuordnung von Einsatzplänen, Brandmeldeanlagen (BMA) und Lageplänen;
g)
berechneten Alternativen in der „Fahrzeug-Strategie“ („Routing“);
h)
aktuellen Standorten und dem Status der Einsatzkräfte;
i)
Ereignis- und Einsatzorten oder auch Teilmengen davon sowohl als Punkt- als auch als Flächenobjekt;
j)
Verkehrseinschränkungen und deren Einbeziehung in Navigationsberechnungen;
k)
Meldebildern;
l)
speziellen Gefahrenbereichen;
12. die Realisierung von Dispositions- und Kommunikationsfunktionen sowie Datenabfrage aus Einsatzmasken und dem GIS;
13. die Integration von GIS-Funktionen für die Datenerfassung und Datenpflege;
14. die Übernahme oder die Abgabe von Einsätzen an andere Arbeitsplätze und IRLS;
15. die Einsatzmittelanforderung bei anderen IRLS;
16. die Auskunftserteilung zu Alarm- und Einsatzplänen, zu Anfahrtswegen, zu Straßensperrungen et cetera;
17. die Überwachung, die Darstellung und die Führung der Prozesse in der IRLS oder an einem Standort innerhalb der Vernetzung der IRLS und an abgesetzten Arbeitsplätzen;
18. die Übergabe und die Übernahme der einsatzrelevanten Informationen von und zu mobilen Datenerfassungssystemen in den Einsatzmitteln für die Einsatzunterstützung (Einsatzbericht, Transportbericht, Rettungsprotokoll, Notarztprotokoll, Erfassung von Patientendaten);
19. die dynamische Anpassung von vorgehaltenen übersichtlichen Vorplanungsmodulen für einen effektiveren Fahrzeugeinsatz im Krankentransport an das Ist-Geschehen und die „Stammkunden-Verwaltung“ mit zyklischen Terminen;
20. die Darstellung der allgemeinen Lage für das aktuelle Einsatzgeschehen im Raum der IRLS und zeitgleich in anderen Lage- und Führungsräumen der besonderen Führungseinrichtungen der unteren Brandschutz-, Rettungsdienst- und Katastrophenschutzbehörden über abgesetzte Arbeitsplätze;
21. die Betriebsleitung BOS-Funk im Leitstellenbereich für zugewiesene Funkverkehrskreise/Digitalfunkteilnehmer und -gruppen;
22. die Einbindung mobiler Kommunikationssysteme mit ihren Diensten;
23. die Darstellung der Gefahrenlage über unterschiedliche Abfragen (zum Beispiel Gebiet, Stichwort) und die elektronische Übergabe an das Informationsprogramm für das Katastrophenmanagement gemäß § 36 Abs. 1 Nr. 10 SächsBRKG ohne Integration in das ELS;
24. der schnelle Zugriff auf Daten zum Erteilen von Gefahrstoffauskünften;
25. die Gewährleistung der Zusammenarbeit mit benachbarten IRLS, Leitstellen (auch grenzüberschreitend) und Führungs- und Lagezentren der Polizei;
26. die vorrangige Sicherstellung der IuK unter Nutzung von BOS-eigenen Strukturen;
27. die Präsentation von Einsatzinformationen über Multimediadienste auf mindestens zwei gesonderten Präsentationsflächen mittels Großbildprojektion;
28. die Bereitstellung wieder verfügbarer Einsatzmittel für neue Einsätze und Aufgaben aus laufenden Einsätzen;
29. die Integration der zuständigkeitsbezogenen Sprach- und Datenaufzeichnung als Gesamtlösung zur komplexen Dokumentation und Protokollierung von Zuständen und Ereignissen für:
a)
einsatzbezogene Recherchen (nachträglich und während des Einsatzes);
b)
systembezogene Recherchen/Störungssuche;
c)
systemübergreifende Recherchen einschließlich Schnittstellenprotokollierung;
d)
Zusammenführung von Sprach- und Datendokumentation (zum Beispiel Sprachaufzeichnung zur Anruferliste und Zuordnung zum Einsatzprotokoll);
30. die Übernahme erfasster Transportdaten und Einsatzberichte (mobil und stationär);
31. die Statistik- und Recherchefunktionen mit umfangreichen vordefinierten Abfragen;
32. die Bereitstellung von Daten zur Erstellung von Gebührenbescheiden;
33. die Einleitung und Überwachung des Datenaustausches für die Qualitätskontrolle;
34. die Realisierung eines eigenen Qualitätsmanagements und die Erstellung von Statistiken, in Echtzeit verfügbar;
35. die Einholung von Auskünften;
36. die Übernahme von Meldungen der die IRLS betreffenden Störmeldeanlagen der Haustechnik und der peripheren Alarmierungstechnik;
37. die Übernahme von Meldungen der internen Gefahrenmeldeanlage;
38. die Sicherstellung einer langfristigen Archivierung von Einsatzunterlagen, die unabhängig von den eingesetzten Systemen und Datenbanken recherchierbar sind;
39. die Absicherung der datenschutzrechtlichen Forderungen zur Trennung von Einsatz- und personenbezogenen Daten und deren Anonymisierung;
40. die Anpassung der Arbeitsweise in den IRLS bei Großschadenslagen:
a)
Teambildung mit getrennten Verantwortungsbereichen mit Gebiets- und Aufgabenbezug;
b)
Trennung von Notrufabfrage und Disposition;
c)
Blockvergabe von Einsätzen an Einsatzabschnitte;
d)
Eindämmung der Informationsflut für die Disponenten durch Änderung von Signalisierungen und zusätzliche Filtermechanismen.
4. Technische Anforderungen
4,1 Grundsätzliche Anforderungen
Die IRLS sind entsprechend rechtlicher Vorgaben und zusätzlich nach den gesicherten arbeitswissenschaftlichen Erkenntnissen, den anerkannten Regeln der Technik (DIN), den VDE-Bestimmungen, den Vorschriften, Merkblättern und Richtlinien der gewerblichen Berufsgenossenschaften und des Verbandes der Sachversicherer, den Grundlagen der IT-Grundschutzkataloge des Bundesamtes für Sicherheit in der Informationstechnik und den Anforderungen aus dem gemeinsamen Betrieb des BOS-Digitalfunks zu projektieren, zu errichten und zu betreiben. Neben den allgemeinen technischen Anforderungen sind die besonderen Anforderungen, die sich durch die Einbindung der einzelnen IRLS in das Leitstellennetzwerk ergeben, zu berücksichtigen. Dabei ist zwischen systembezogenen und leitstellenbezogenen Anforderungen zu differenzieren. Die systembezogenen Anforderungen beziehen sich auf das Gesamtsystem (ELS, FNAS) in jeder IRLS. Die leitstellenbezogenen Anforderungen beziehen sich auf die einzelne IRLS, in der die Umsetzung der Anforderungen jeweils entsprechend der lokalen Rahmenbedingungen erfolgen muss.
4.2 Systembezogene Anforderungen
4.2.1 Hard- und Softwarekonzept
Zur Umsetzung der geforderten Funktionalität (Nummern 2 und 3) sind die erforderlichen Hardwarekomponenten, Betriebssysteme, Datenbank-(management-)Systeme und Applikationen sowie die für die Realisierung der nachrichtentechnischen Kopplungen erforderlichen Schnittstellen (Hard- und Softwarekomponenten) als komplexe Gesamtkonfiguration zu realisieren. Alle voneinander abhängigen Teilkomponenten müssen aufeinander abgestimmt sein und ein fehlertolerantes System repräsentieren. Zur Sicherstellung einer späteren Migration sind alle Einzelsysteme als Modulkomponenten aufzubauen, die in einer Migrationsphase angepasst und ausgetauscht werden können, ohne das Gesamtsystem in seiner Funktionalität und Eignung zu beeinflussen. Das Hardwarekonzept ist entsprechend der geforderten Ausfallsicherheit und auf den Schutz vor unberechtigten Zugriffen auszurichten. Die Dimensionierung der einzelnen Hardwarekomponenten muss erweiterbar sein. Die Zugriffszeiten auf interne und externe Speicherbereiche müssen eine Verarbeitung der im Netz entstehenden Datenmengen ohne Zeitverzug ermöglichen. Für alle Server, Anlagen und Arbeitsplatzrechner muss eine gemeinsame Konsolenverwaltung, auch im abgesetzten Betrieb von Arbeitsplätzen, durch Systemadministratoren möglich sein. Zusätzlich ist eine gemeinsame Verwaltung der aktiven Netzwerkelemente von einer zentralen Stelle über Softwaretools vorzusehen. Das Hardwarekonzept muss die Realisierung von abgesetzten Arbeitsplätzen unterstützen. Abgesetzte Arbeitsplätze sind so zu konfigurieren, dass nur zugewiesene Aufgaben und Funktionen bedient werden können. Der Eingriff in sicherheitstechnische Belange der IRLS ist auszuschließen. Die Software muss an die Anforderungen der zu erfüllenden Aufgaben angepasst werden können. Dem Benutzer müssen unmittelbar oder auf Verlangen Angaben über die jeweiligen Dialogabläufe angezeigt werden. Dem Benutzer muss es möglich sein, die Dialogabläufe zu beeinflussen. Eventuelle Fehler müssen beschrieben werden und es muss möglich sein, diese mit begrenztem Arbeits- und Zeitaufwand zu beseitigen. Zur Erfüllung der Funktionalität muss der Anbieter die Datenbankstrukturen und die Spezifikation von Schnittstellen sowie notwendige Anpassungen an Hard- und Software offenlegen.
4.2.2 Rollenkonzept/Berechtigungsverwaltung im System
Im Gesamtsystem ist ein Rollenkonzept für die Zugriffs- und Editierrechte der Nutzergruppen festzulegen. Dazu sind im System mindestens Berechtigungsstufen für die folgenden Funktionen zu vergeben:
1. Disponent;
2. Schicht-/Dienstgruppenführer;
3. Leiter IRLS und stellvertretender Leiter IRLS;
4. Administrator IRLS;
5. Administrator Technikzentrale Digitalfunk;
6. Aufgabenträger für den Rettungsdienst;
7. Kostenträger im Rettungsdienst;
8. Landesärztekammer;
9. Rechtsaufsichtsbehörden;
10. Datenpfleger;
11. Untere Brandschutz-, Rettungsdienst- und Katastrophenschutzbehörden.
Entsprechend der Berechtigungsstufen ist die Funktionalität der Bedienoberflächen anzupassen. Die Zugriffsrechte auf die im Folgenden dargestellten Arbeitsplätze resultieren aus dem Rollenkonzept und der territorialen Zuständigkeit. Das Rollenkonzept und die Berechtigungsstufen werden durch die autorisierte und vorgehaltene Stelle des BOS-Digitalfunk Sachsen nach den Vorgaben der Betreiber der IRLS umgesetzt. Die Systemadministration der IRLS erhält die notwendigen Rechte und Verwaltungswerkzeuge, um eine eigenverantwortliche Nutzerverwaltung innerhalb ihres Verantwortungsbereiches durchzuführen. Die Vorgaben der Geheimhaltung und des Datenschutzes aus dem BOS-Digitalfunk bleiben hiervon unberührt.
4.2.3 Definition der Arbeitsplätze
Die Arbeitsplätze sind aufgrund der betrieblichen Erfordernisse und zur Erledigung der Aufgaben in unterschiedlicher Ausstattung einzurichten. Jeder Arbeitsplatz besteht aus einer Bedienoberfläche mit festgelegter Funktionalität. Disponentenarbeitsplatz: Der Disponentenarbeitsplatz ist der Standardarbeitsplatz in der IRLS zur Notrufannahme, Disponierung und Alarmierung der Einsatzkräfte und -mittel, der Lenkung der Notfalleinsätze im Rettungsdienst sowie der Führungsunterstützung. Durch die Anmeldung muss er als Arbeitsplatz des Disponenten, des Lagedienst-/Schichtführers, der Systembetreuung/Datenpflege oder zur Schulung verwendet werden können. Er bildet die gesamte technische Funktionalität des ELS und des FNAS ab. Die Einsatzbearbeitung, Einsatz-/Fahrzeugübersicht und das GIS sind übersichtlich in voller Funktionalität als Mehrfach-Bildschirm-Arbeitsplatz darzustellen. Das FNAS ist über einen separaten Bildschirm oder Touchscreen zu realisieren. Der Disponentenarbeitsplatz hat keine vom Leitstellennetz unabhängige Zugangsmöglichkeit für externe Datenträger. Über geeignete EDV-Konzepte ist von diesem Platz der Zugriff auf die Bürokommunikation des Betreibers der Leitstelle zu ermöglichen. Abhängig von der Berechtigungsstufe des angemeldeten Benutzers muss eine statistische Auswertung von gespeicherten Daten, der Sprachaufzeichnung und des aktuellen Einsatzgeschehens am Arbeitsplatz möglich sein. Hierzu sind geeignete Werkzeuge vorzuhalten. Notruf-Annahmeplatz (Ausnahme-Arbeitsplatz): Notrufannahmeplätze dienen der Entlastung der IRLS bei Großschadenslagen/Katastrophen mit hohem Anrufaufkommen. Der Notrufannahmeplatz ist als Ein-Bildschirmarbeitsplatz mit reduzierter technischer Ausstattung und reduzierter Funktionalität des ELS oder als Abfrageplatz des FNAS mit funktioneller Trennung zwischen Einsatzannahme und Disposition zu realisieren. Die erforderliche geräusch- und wärmeemissionsoptimierte Hardware kann dabei in unmittelbarer Nähe aufgestellt werden. Der Arbeitsplatz muss mit Notebook und Systemtelefon betrieben werden können. Abgesetzter Arbeitsplatz: Abgesetzte Arbeitsplätze sind zur Informationsbereitstellung und Datenpflege einzurichten. Eine Notrufannahme wird hier nicht durchgeführt. Sie befinden sich nicht im regulären Disponentenarbeitsraum der IRLS. Sie können zum Beispiel an den nachfolgenden Orten innerhalb des Leitstellenbereiches eingerichtet werden:
1. innerhalb des Landratsamtes zur Informationsbereitstellung;
2. in Einsatzabschnitten zur Führung von Kräften und Mitteln;
3. in Technischen Einsatzleitungen (TEL) oder Stäben zur Informationsbereitstellung und -gewinnung.
Der abgesetzte Arbeitsplatz ist mit reduzierter technischer Ausstattung und reduzierter Funktionalität des ELS zu realisieren. Die Bedienung muss als Terminalserver oder vorzugsweise als webbasierte Lösung über einen Standardbrowser möglich sein. In Ausnahmesituationen kann er als Disponentenarbeitsplatz mit reduzierter Ausstattung verwendet werden. Systemadministratorarbeitsplatz: Der Systemadministratorarbeitsplatz ist der Standardarbeitsplatz zur Datenpflege und Systemadministration und muss über den vollständigen Funktionsumfang des FNAS inklusive der Sprachdokumentation, des ELS und der GIS verfügen. Dieser muss die Prüfung der Auswirkungen von Änderungen im Rahmen der Datenpflege/-bereitstellung oder technischer Erneuerungen im System und auf die Bedienoberflächen der Nutzergruppen (Rollen) ermöglichen. Als getrennter Arbeitsplatz ist er als Mehrfach-Bildschirm-Arbeitsplatz auszuführen und muss den Import von Daten von externen Datenträgern ermöglichen.
4.2.4 Einsatzleitsystem (ELS)
Das ELS ist das zentrale Steuerungsinstrument der IRLS. Es setzt sich aus dem Einsatzleitrechner (ELR = Gesamtheit aller Rechnersysteme und Netzstrukturen inklusive Betriebssystem zur Aufnahme der Einsatzleitsoftware) und der Einsatzleitsoftware (Steuerungsprogramm inklusive aller Schnittstellen, Datenbanksysteme und Reporting-/Auswertungstools) zusammen. Das ELS ist ein autarkes, nach außen abgeschirmtes, redundantes System für den Dauerbetrieb. Dieses hat die Aufgaben der IRLS zu gewährleisten, indem die Prozesse (vergleiche Nummer 2) der IRLS und Schnittstellen (vergleiche Nummer 4.2.14) umfassend integriert sind. Es ist jeweils in den IRLS und den Technikzentralen zu betreiben und hat sich über das Leitstellennetzwerk zu synchronisieren.
4.2.5 Funk-/Notruf-Abfragesystem (FNAS)
Das FNAS hat die Funktionen Funk, Notruf, Telefon und IP-Schnittstelle zum ELS abzubilden. Gleichzeitig sind leitstellenbezogen weitere Funktionen, zum Beispiel Audiodokumentation, Alarmierung, elektrische Lautsprecheranlage (ELA), Haustechnik anzuschließen.
4.2.6 Audiodokumentationsanlage
Die Bedienung der lokalen und zentralen Audiodokumentationsanlage hat über eine Client/Server-Lösung oder Browser-Anwendung im Intranet zu erfolgen. Die IRLS vergibt die Rechte für Zugriff und Recherche innerhalb ihres Verantwortungsbereiches. Die IRLS verwenden eine einheitliche Audiodokumentationsanlage. Die Aufbewahrung von Sprachaufzeichnungen muss mindestens 24 Monate erfolgen. Die Audiodokumentationsanlage muss mindestens 180 Tage einen sofortigen Zugriff ermöglichen. Darüber hinausgehende Regelungen bleiben hiervon unberührt.
4.2.7 Anbindung peripherer Systeme
Für die Anschaltung von Landratsämtern, Abrechnungsstellen im Rettungsdienst und Brandschutz sowie Feuer- und (Rettungs-) wachen sind, sofern notwendig, die erforderlichen Übertragungswege einzurichten. Es ist eine Mitnutzung der errichteten Infrastruktur des Leitstellen- und Anbindungsnetzwerkes für den Digitalfunk als wirtschaftliche Lösung anzustreben.
4.2.8 Alarmierungsnetze
Die Bedienung der Alarmierungsnetze hat über den ELR mit redundant ausgeführten und netzwerkfähigen Digitalen Alarmgebern (DAG) zu erfolgen. Die DAG sind in den Technikräumen der IRLS oder geeigneten Standorten innerhalb des Leitstellennetzwerkes zu installieren. Als Notfalleingabeplatz ist auf dem DAG ein Bedienungsmodul als Rückfallebene zur Verfügung zu stellen. Die Bedienung der Rückfallebene muss von mindestens einem Drittel der Leitstellenarbeitsplätze möglich sein. Bei Bedarf soll auch die Funktion Multialarmgeber unabhängig vom FNAS anzubinden sein.
4.2.9 Wachalarmsystem
Wachalarmsysteme ständig besetzter Feuer- und Rettungswachen sind über ein Steuersystem als speicherprogrammierbare Steuerung (SPS) einzurichten. Das Ein- und Ausschalten hat alarmierungs-, zeit- oder statusabhängig zu erfolgen.
4.2.9.1 Bedienung
Die Bedienung folgender Systeme muss aus dem ELS und dem FNAS möglich sein:
1. Alarmlicht und Alarmierungsampeln;
2. ELA mit und ohne Alarmgong;
3. Tor- und Türsteuerung sowie Lüftungsanlagen;
4. Lichtsignalanlagen;
5. Alarmtableau mit und ohne Kartendarstellungen;
6. Alarmdrucker, Alarmfax;
7. Videoaufschaltungen für Ausfahrtkameras;
8. Telefonbenachrichtigungssysteme;
9. Einsatzplan- und Objektkartenschränke.
Alle Systeme müssen auch unabhängig voneinander oder kombiniert ansteuerbar sein. Bestehende ELA sind über die Standardschnittstelle des ELS und des FNAS anzusteuern. Alle abgegebenen Signale sowie die wesentlichen Zustände der Tür- und Torsteuerungen sind dem Disponenten anzuzeigen.
4.2.9.2 Anschaltung Alarmtableaus
Vorhandene Alarmtableaus sind über die örtliche Infrastruktur anzuschalten. Die Anschaltung ist dabei je nach Anforderung fahrzeug- und einsatzabhängig zu steuern. Folgende Informationen sind bereitzustellen:
1. die Einsatzart (Rettungsdiensteinsatz/Brandeinsatz/Technische Hilfeleistung);
2. die Freigabe von Sonderrechten;
3. die notwendigen Kräfte und Mittel;
4. die Alarmierungszeit;
5. der Einsatzort;
6. das Einsatzstichwort;
7. der Sachverhalt;
8. ein frei einstellbarer (parametrierbarer) Kartenauszug des Einsatzorts.
Für den Alarmdrucker und das Alarmtableau sind analoge Informationen aus dem ELS zur Verfügung zu stellen.
4.2.10 Statusinformation
Das ELS muss den Versand und den Empfang sowie eine fahrzeug- und einsatzbezogene Anzeige von Funkmeldesignalen (FMS/SDS-Signale) über das FNAS und das ELS realisieren. Die Daten sind automatisch in beiden Systemen zeitgleich zu harmonisieren. Die FMS/SDS-Kennung, die Teilnehmeridentifikation im Digitalfunk und der Rufname des angeschalteten Teilnehmers muss im Klartext dargestellt werden. Das FMS/SDS-Notrufsignal und die Notrufmeldung im Digitalfunk sind als spezieller Notruf zu signalisieren. Deren Bearbeitung hat mit höchster Priorität zu erfolgen. Sprechwünsche und Fremdanmeldungen im Analog- oder Digitalfunk sind optisch und akustisch zu signalisieren. Bei Bestätigung des Ereignisses ist eine Sprechaufforderung zu senden und die Sprachverbindung zu schalten. Für die Ereignisse Sprechwunsch, Notruf, Fremdanmeldung und Eintreffen am Einsatzort sind die Fahrzeugidentifizierung und mit der Nutzung des Digitalfunks gleichzeitig eine Ortung durchzuführen. Eingehende FMS/SDS-Signale sind aus allen Hörwegen auszublenden. Der Empfang, die Übermittlung und die Auswertung von FMS-Telegrammen aus den angeschalteten analogen Funknetzen sind zu ermöglichen. FMS/SDS-Quittungen sind nur auf parametrierten Funkverkehrskreisen zu übermitteln. Soweit die Fahrzeuganlage es ermöglicht, ist bei jedem übertragenen Einsatzstatus eine Ortungsinformation abzufragen. Status- und Ortungsinformationen der Fahrzeuge und des ELS sind auf einem zentralen Server der Technikzentralen in einer Datenbank bereitzustellen. Diese Datenbank dient zugleich als Rückfallebene, dem Informationsaustausch mit anderen IRLS und der Synchronisation der Leitstellensoftware nach Ausfall von Komponenten.
4.2.11 Betriebs- und Sonderfunk
Wird Betriebs- oder Sonderfunk eingerichtet, sind diese im FNAS und dem ELS vorzusehen.
4.2.12 Sonstige Einrichtungen der IRLS
4.2.12.1 Audio-Visuelle-Medien
In der IRLS sind ein Rundfunk- und ein TV-Gerät mit Flachbildschirm vorzusehen. Das TV-Bild muss von allen Disponentenarbeitsplätzen eingesehen werden können. Das Tonsignal dieser Systeme ist auf die Niederfrequenzhörwege der Plätze zu führen. Es sind Möglichkeiten zum langfristigen Mitschneiden von mindestens zwei Kanälen für Video/Audio-Informationen in der Leitstelle vorzuhalten. In der IRLS sind beschriftungsfähige Karten und Plantafeln für eine direkte, visuelle Darstellung in geeigneten Maßstäben für mindestens den Leitstellenbereich und angrenzende Gebiete bis circa 30 km bereitzuhalten. Die Großbilddarstellung ist mittels fernbedienbaren, geräuscharmen Projektors oder anderer Großbildsysteme nach dem Stand der Technik zu realisieren. Die Darstellung muss tageslichttauglich sein. Die Großbilddarstellung muss von jedem Disponentenarbeitsplatz aus eingesehen werden können. Die Signale von folgenden Geräten und Systemen sind anzuschalten:
1. Videorekorder/DVD-Player;
2. TV-Empfänger;
3. Informationen/Karten aus dem ELS;
4. Rückfallebenen für Statusübersichten;
5. Informationen/Karten aus dem Verwaltungsnetz;
6. Arbeitsplätze, die im Netzwerk der IRLS arbeiten;
7. Überwachungs- und Videokameras;
8. Echtzeit-Videos (Video-Streams) aus dem Netzwerk;
9. Fahrzeugzustandsanzeigen (FZA).
Eine einfach zu bedienende Oberfläche muss an dem Platz des Schicht-/Dienstgruppenführers zur Umschaltung der Quellen vorhanden sein. Das Bild ist über das Netzwerk durch geeignete Übertragungsverfahren zur Darstellung an anderen Orten (zum Beispiel an besondere Führungseinrichtung der unteren BRK-Behörde) weiterzugeben.
4.2.12.2 Einsatznachbearbeitung und -abrechnung
Zur Einsatznachbearbeitung und -abrechnung sind erfasste Grunddaten über eine Exportschnittstelle oder direkte Übergabe in eine Datenbank zu übermitteln. Ein beendeter Einsatz ist automatisch oder auf Anforderung in ein Datenarchiv zu übertragen. Jeder Einsatz muss mit allen relevanten Daten eigenständig im Archiv änderungsresistent und beweissicher gespeichert werden. Das sind insbesondere:
1. das Einsatzdatum und die einsatzrelevanten Zeiten (Einsatzannahme, Disposition, Alarmierung, Einsatzübernahme, Eintreffen am Einsatzort, Patientenübernahme, Eintreffen am Zielort, Freimeldung und Einsatzende), bezogen auf alle eingesetzten Kräfte und Mittel;
2. der Einsatzort (Objekt, Straße, Hausnummer, Ort, Zusatzinformation);
3. der Zielort (Objekt, Straße, Hausnummer, Ort, Zusatzinformationen);
4. das Einsatzstichwort, die Notfallart und Einsatzinformationen;
5. der Anrufer, der Meldeweg, die Zeit des Eingangs;
6. die übernehmenden Einsatzkräfte und Einsatzmittel mit Standort bei Übernahme;
7. die Lagemeldungen;
8. die jeweils handelnden Personen/Funktion;
9. der Einsatzabschluss durch die IRLS.
Es ist sicherzustellen, dass nach Einsatzabschluss ein mit dem Einsatzleiter abgestimmtes und festgelegtes Abschlussstichwort nachgetragen werden kann.
4.2.12.3 Fahrzeugortung
Zur Fahrzeugortung sind nachfolgende Kommunikationswege vorzusehen:
1. Analogfunk unter Nutzung des FMS mit Folgetelegramm;
2. GSM und dessen Datendienste;
3. BOS-Digitalfunk mit Ortungsprotokoll LIP.
Die Abfrage der Ortungsdaten muss dabei zyklisch oder auf Anfrage möglich sein. Spontane Meldungen der Fahrzeuge sind zuzulassen.
4.2.13 Qualitätsmanagementsystem Rettungsdienst
4.2.13.1 Grundlagen des Qualitätsmanagementsystems
Für das Qualitätsmanagement, die Bereichsplanungen, Entgeltverhandlungen und rechtsaufsichtliche Prüfungen durch die entsprechenden Aufsichtsbehörden im Rettungsdienst ist eine gesicherte und einheitliche Datenbasis zu schaffen. Als Grundlage einer solchen Datenbasis ist neben den bereits vorhandenen Einsatzdaten im ELS die Übernahme des minimalen Notarztdatensatzes nach DIVI in der aktuellen Version für Rettungsdiensteinsätze vorzusehen. Die Übernahme kann neben einem automatisch generierten Datensatz aus einem System zur Mobilen Datenerfassung im Rettungsdienst auch über ein Formular im Internet (Web-Front-End) erfolgen. Hierfür sind die entsprechenden Grundlagen in den IRLS und Technikzentralen zu schaffen. Zur Sicherstellung des Datenschutzes sind standardisierte Verschlüsselungstechniken für internetbasierte Anwendungen zu verwenden sowie eine zentrale Benutzerrechteverwaltung zu integrieren. Der erzeugte Datensatz ist automatisch auf seine Plausibilität mit den im ELS bereits erfassten Daten (zum Beispiel Alarmierungs- und Statuszeiten) zu prüfen und Differenzen sind im Datensatz zu kennzeichnen.
4.2.13.2 Voraussetzungen der Mobilen Datenerfassung
Das ELS muss das Datenprotokoll für die mobile Datenerfassung vorgeben. Die Mehrfacherfassung gleichartiger Daten ist auszuschließen. Die notwendigen Datenaustauschsysteme (zum Beispiel FMS mit Folgetelegramm, GSM, SDS im BOS-Digitalfunk) sowie deren Schnittstellen (zum Beispiel XML-Formulare) sind vorzusehen. Insbesondere sind folgende Daten aus dem ELS an das System der Mobilen Datenerfassung zu übergeben:
1. Einsatzauftrag mit Einsatznummer;
2. Einsatzort mit geografischer Referenz;
3. Anruferdaten;
4. Patientendaten;
5. Indikation/Einsatzstichwort;
6. Bemerkungen und zusätzliche Sachverhaltsschilderungen;
7. Zielort.
Für den Krankentransport sind zusätzlich die Abholzeit und der Abholort aus den Vorplanungen zu übernehmen.
4.2.13.3 Einsatzdaten aus der Mobilen Datenerfassung
Zur Sicherstellung eines Qualitätsmanagementsystems für den Rettungsdienst ist die Übernahme folgender Daten aus der Mobilen Datenerfassung in die Datenbanken der IRLS und Technikzentralen vorzusehen:
1. Konkretisierung des Einsatzortes;
2. Patientendaten nach Einlesen der Chipkarte;
3. Übertragung fahrzeugspezifischer Einsatzdaten;
4. Angaben über Krankenhaus und Station, auf die der Patient angewiesen wurde;
5. Minimaler Notarztdatensatz nach DIVI in der aktuellen Version.
4.2.14 Schnittstellen
Zur Realisierung der unter Nummer 2 beschriebenen Prozesse und des unter Nummer 3 beschriebenen Daten- und Informationsflusses im Leitstellennetzwerk ist die Verknüpfung der Systemelemente mittels Schnittstellen erforderlich.
4.2.14.1 Grundsätzliche Anforderungen an Schnittstellen
Nachfolgende grundsätzliche Anforderungen an Schnittstellen sind zu realisieren:
1. die vollständige Beschreibung der Schnittstellen (auch für Softwareschnittstellen) als Bestandteil der Lieferleistung für alle Komponenten;
2. die Sicherstellung, dass der Auftraggeber das Recht erwirbt, die Schnittstellenbeschreibung für die Weiterentwicklung der Systeme sowie den Austausch von Komponenten verwenden zu dürfen.
4.2.14.2 Grundsätze des Betriebes der Schnittstellen
Grundsätze des Betriebes der Schnittstellen sind:
1. die Vorhaltung gleichartiger Datenbestände innerhalb der Teilsysteme (Datensynchronisation zur Gewährleistung von Rückfallebenen und Redundanzen);
2. die Verwendung offener Standards/Spezifikationen;
3. die Bereitstellung mehrfacher Schnittstellen für einzelne Prozesse, um unterschiedliche Herstellersysteme und Standorte anzuschalten;
4. der Betrieb einzelner Systeme und deren Redundanzen unabhängig von den eingerichteten Schnittstellen.
4.2.14.3 Schnittstellen mit einheitlichen Funktionen
Folgende Schnittstellen mit einheitlichen Funktionen sind zum Betrieb der IRLS einzurichten:
1. ELS – FNAS;
2. ELS – Empfangseinrichtung BMA;
3. ELS/FNAS – UMS (E-Mail, Fax, SMS et cetera);
4. ELS/FNAS – automatischer Notruf gemäß § 108 des Telekommunikationsgesetzes (TKG) vom 22. Juni 2004 (BGBl. I S. 1190), das zuletzt durch Artikel 2 des Gesetzes vom 17. Februar 2010 (BGBl. I S. 78, 79) geändert worden ist, in der jeweils geltenden Fassung;
5. FNAS – Telefonanlage;
6. FNAS – analoge Funknetze;
7. ELS/FNAS – BOS-Digitalfunk;
8. ELS – FMS/SDS/GPS;
9. ELS – Videosystem;
10. ELS/FNAS – Analoge Alarmierung;
11. ELS – Digitale Alarmierung;
12. ELS – Sirenensteuerung;
13. ELS/FNAS – Wachalarmierungssystem (ELA-Aufschaltung);
14. ELS – Telefonalarmierung;
15. ELS – sonstige Alarmierungssysteme;
16. ELS – Faxalarmierung;
17. ELS – Alarmdrucker;
18. ELS – andere IRLS;
19. ELS – Führungseinrichtungen (Feuerwehr und Katastrophenschutz);
20. ELS – Einsatzfahrzeuge;
21. ELS – Server Geobasisdaten;
22. ELS – Datennetze der Verwaltung;
23. ELS – Internetdienste (Hochwasserzentrum et cetera);
24. ELS – Objektdaten;
25. ELS – Wetterstation IRLS;
26. ELS – Datensicherung;
27. Computersysteme – Zeitsynchronisation;
28. Hardwarekomponenten – unterbrechungsfreie Stromversorgung;
29. ELS/FNAS – ADA (Audiodokumentationsanlagen);
30. ELS – DISMA (Programmsystem zur Notfallplanung und zum Notfallmanagement);
31. ELS – Abrechnungssysteme/QM-Rettungsdienst;
32. alle Systeme – Infrastrukturdienste (zum Beispiel Anmeldung, Adresszuweisung, Zeitdienst).
4.2.15 Übertragungsnetze
Alle IRLS haben für Daten- und Sprachkommunikation Übertragungsnetze mit einheitlichen Anforderungen zu verwenden. Es müssen mindestens die nachfolgenden Übertragungsnetze eingerichtet werden:
1. das Leitstellennetzwerk (Verbindung zwischen IRLS und Technikzentralen);
2. das Netzwerk innerhalb der einzelnen IRLS;
3. die Vernetzung des Leitstellennetzwerks mit anderen Behörden/Verwaltung;
4. die Zugangsnetze zum Leitstellennetzwerk für Fernwartungsfunktionen;
5. die Zugangsnetze für Feuer- und Rettungswachen;
6. die Zugangsnetze für Dritte (einzelne Feuerwehren et cetera);
7. das Zugangsnetz Internet. Die Übertragungsnetze müssen Datentransferraten realisieren, die den leistungsfähigen Betrieb des Leitstellennetzwerks und der Netzwerkkomponenten sicherstellen. Alle Übertragungsnetze müssen über Sicherheitseinrichtungen und Zugangsbeschränkungen verfügen, die einen unberechtigten Zugriff wirkungsvoll unterbinden. Eine Netzwerktrennung zwischen Leitstellennetzwerk und Büro-/Verwaltungsnetzwerk des Betreibers ist sicherzustellen.
4.2 Leitstellenbezogene Anforderungen
4.3.1 Raumfunktionskonzept
Die IRLS ist als nicht öffentlicher Bereich mit Zugangsbeschränkung auszuführen. Der Leitstellenraum ist zu klimatisieren und mit einer Geräuschdämmung auszustatten. Natürlicher Lichteinfall ist vorzusehen. Für die Reduzierung des Wärme- und Lichteinfalls sowie zum Blendschutz sind Möglichkeiten zu schaffen. Es sind die in der Tabelle 1 aufgeführten Räume mit höchstens der dort genannten Flächen einzurichten.
Tabelle 1: Raumprogramm der IRLS
Raumprogramm der IRLS
Nr. | Raumbezeichnung/Platzbedarf | Fläche pro Einheit [m²]
Nr. | Raumbezeichnung/Platzbedarf | Fläche pro Einheit [m²]
1 | Disponenten-Arbeitsplatz | 20
2 | Notruf-Annahmeplatz | 8
3 | Büro Dienstgruppenführer inklusive Disponentenarbeitsplatz | 28
4 | Büro Leiter IRLS | 18
5 | Büro stellvertretender Leiter IRLS | 18
6 | Arbeitsplatz für Datenpflege und Systemadministration | 15
7 | Besprechungs-, Lage- und Führungsraum | 25
8 | Aufenthaltsraum, Teeküche | 25
9 | Drucker/Kopierer | 10
10 | Lager/Archiv | 30
11 | Umkleideraum/Dusche Damen | ArbStättV***
12 | Umkleideraum/Dusche Herren | ArbStättV
13 | Ruheraum Damen* (2 Betten) | 16
14 | Ruheraum Herren* (2 Betten) | 16
15 | WC-Anlage Damen | ArbStättV
16 | WC-Anlage Herren | ArbStättV
17 | Putzmittelraum | 3
18 | Technikraum 1 (Informations- und Kommunikationstechnik) | 3 je Systemschrank**
19 | Technikraum 2 (Informations- und Kommunikationstechnik) | 3 je Systemschrank**
20 | Technikraum 3 (Klima/HLK)* | 40 bis 60
21 | Technikraum 4 (USV 1)* | 10
22 | Technikraum 5 (USV 2)* | 10
23 | Technikraum 6 (Dieselnotstromaggregat)* | 25
24 | Technikraum 7 (Hausanschlüsse, Kommunikation, Elektroversorgung, Ver- und Entsorgung)* | 12
25 | Technikraum 8 (Hausanschlüsse, Kommunikation, Elektroversorgung, Ver- und Entsorgung)* | 12
26 | Technikraum 9 (Zugang für Fremdfirmen zum Beispiel BMA) | 20
27 | Sanitätsraum* | 10
28 | Funkwerkstatt (DWS-Betrieb et cetera) | Einzelfallprüfung
29 | Verkehrsfläche | 15 Prozent
* Die gekennzeichneten Bereiche können auch in Nebenräumen untergebracht werden.
** zuzüglich der für die Verkehrswege notwendige Flächen
*** § 6 der Verordnung über Arbeitsstätten (Arbeitsstättenverordnung – ArbStättV) vom 12. August 2004 (BGBl. I S. 2179), die zuletzt durch Artikel 4 der Verordnung vom 19. Juli 2010 (BGBl. I S. 960, 965) geändert worden ist, in der jeweils geltenden Fassung
4.3.2 Technikräume
Die Vorgaben der Bausteine „Infrastruktur“ der Grundschutzkataloge des Bundesamtes für Sicherheit in der Informationstechnik (BSI) sind umzusetzen. Die nachfolgenden Räume sind den Bezeichnungen nach BSI-Grundschutz gleichzusetzen.
Tabelle 2: Gleichsetzung der Raumbezeichnungen
Gleichsetzung der Raumbezeichnungen
Nr. | Technikräume IRLS | Bezeichnungen nach BSI-Grundschutz
1 | Technikräume IRLS | Bezeichnungen nach BSI-Grundschutz
2 | Technikraum IuK | Rechenzentrum/Serverraum
3 | Technikraum Klima, HLK, USV, NEA, Hausanschlussraum | Raum für technische Infrastruktur
4 | Archiv | Datenträgerarchiv
5 | Besprechungs-, Lage- und Führungsraum | Besprechungs-, Veranstaltungs- und Schulungsraum
Die Grobtechnik (Energieversorgung, Klimatechnik) und Feintechnik (Informations- und Kommunikationstechnik) sind räumlich zu trennen. Die Anlagen der folgenden technischen Einrichtungen sind jeweils in einem eigenen Raum (separate Brandabschnitte) unterzubringen:
1. der Informations- und Kommunikationstechnik;
2. der Klimatisierung und Lüftung;
3. der Energieversorgung (NEA, USV);
4. des Lagers sowie der Ver- und Entsorgung.
Gedoppelte Systeme sind in zwei voneinander getrennten Technikräumen in separaten Brandabschnitten einzurichten, um den Anforderungen der Redundanz gerecht zu werden. Die Räume sind mit einem Doppelboden auszustatten. Soweit der Doppelboden zur Klimatisierung genutzt wird, muss seine Höhe mindestens 500 mm betragen. Der Doppelboden muss ab einer Höhe von 20 cm eine Brandschutzqualität von F30 in geschlossenem Zustand aufweisen. Die Doppelböden und – sofern vorhanden – abgehängte Decken müssen mit den Seitenwänden des IT-Raumes abschließen. Die Räume der IuK müssen getrennte, unabhängige Zuführungen für Elektro- und Fernmeldekabel und Verteiler aufweisen. Die Installation hat in den Freiräumen des Doppelbodens und über Kabeltrassen an den Wänden sowie im Deckenbereich zu erfolgen. Die Trassen der Ver- und Entsorgungsleitungen des Gebäudes sind nicht durch sensible Bereiche der IRLS oder in deren unmittelbarer Nähe zu führen. Eine ausreichende Stellfläche für die Technikschränke unter Beachtung der Bewegungsfreiheit und der Freihaltung der Fluchtwege bei geöffneten Schranktüren ist sicherzustellen. Eine Reservestellfläche für zwei Technikschränke ist zu realisieren. Jeder Technikschrank ist mit einem Festanschluss mit Potentialausgleich auszustatten. Neben oder in jedem Technikschrank sind Doppelsteckdosen 230 V/16 A für Service- und Wartungszwecke zu installieren. Zur Aufnahme von Messtechnik ist ein Arbeitstisch (mindestens 1 500 x 800 mm) vorzusehen. Am Arbeitstisch sind ausreichend Steckdosen und eine zusätzliche Arbeitsplatzbeleuchtung bereitzustellen. Für die zugehörige technische Dokumentation ist ausreichend Platz vorzuhalten.
4.3.3 Raum für Disponentenarbeitsplätze (Leitstellenraum)
4.3.3.1 Ergonomische Anforderungen
Jeder Disponentenarbeitsplatz muss in seiner Struktur einem Bildschirmarbeitsplatz entsprechen. Aktuelle Erkenntnisse der ergonomischen Gestaltung sind umzusetzen. Der Disponentenarbeitsplatz ist wie folgt einzurichten:
1. die Breite (1 800 bis 3 000 mm), die Tiefe (800 bis 1 500 mm) und die Platzreserve zur Möglichkeit der Nutzung als Arbeitsplatz für eine zweite Personen;
2. der Beinraum von nicht weniger als 1 000 mm Breite, 600 mm Tiefe und 650 mm Höhe mit höhenverstellbarer und rutschfester Fußstütze;
3. die elektrische Höhenverstellbarkeit (circa 700 bis 1 250 mm) zur Nutzung als Sitz-/Steharbeitsplatz;
4. die separat höhenverstellbare Monitorstellfläche/-befestigung für vier Flachbildschirme in einer Ebene sowie Verstellbarkeit des Sichtabstands;
5. die reflexionsarme Oberfläche und die blendfreie Arbeitsplatzbeleuchtung;
6. die Mindestarbeitsfläche von 1 m²;
7. die Aufnahmemöglichkeiten für entkoppelte Lautsprecher sowie die Integration von Bedienelementen für Zusatzgeräte mit hochbelastbaren geschützten Kabelführungen;
8. die Kommunikationsverbindungsanzeige (Leuchte);
9. die Ablagemöglichkeiten für Technik der Rückfallebene sowie für Büromaterial.
Das Kommunikationssystem ist unabhängig vom ELS über ein Touchscreenbedienfeld (verstellbar in der Neigung) oder wahlweise als Flachbildschirm integriert in die Bildschirmreihe (4. Bildschirm) des Tisches einzubauen. Die Tastatur/Maus des ELS kann zugleich für das Kommunikationssystem Verwendung finden. Zur Verminderung von Wärme- und Geräuschlasten sind keine PC-Komponenten am Disponentenarbeitsplatz zu betreiben. Alle Disponentenarbeitsplätze sind mit einem ergonomisch gestalteten und standsicheren Arbeitsstuhl für dynamisches Sitzen auszustatten (Prüfsiegel einer Landesgewerbeanstalt für 24 h-Betrieb). Darüber hinaus sind zusätzliche Stühle vorzuhalten. Der Arbeitsplatz des Dienstgruppenführers ist für Arbeiten in der Büroumgebung zu erweitern und muss zusätzliche Flächen zur Ablage von Karten und Unterlagen bieten.
4.3.3.2 Beleuchtung
Unabhängig vom Tageslichteinfall ist der Leitstellenraum, entsprechend den allgemeinen Regeln der Technik für ständig besetzte Arbeitsplätze, zusätzlich zu beleuchten. Eine individuell einstellbare Arbeitsplatzbeleuchtung, die keinen Schattenwurf verursacht, ist vorzusehen. Die Anforderungen der folgenden Normen sind mindestens zu berücksichtigen:
1. die DIN EN 12464 „Licht und Beleuchtung – Beleuchtung von Arbeitsstätten“ – Teil 1: „Arbeitsstätten in Innenräumen“, Deutsche Fassung EN 12464-1:2002, Ausgabe: März 2003;
2. die DIN 5035 „Beleuchtung mit künstlichem Licht“ – Teil 7: „Beleuchtung von Räumen mit Bildschirmarbeitsplätzen“, Ausgabe: August 2004;
3. die Berufsgenossenschaftliche Regelung (BGR) 131 „Natürliche und künstliche Beleuchtung von Arbeitsstätten“, Ausgabe: 2008, herausgegeben von der Deutschen Gesetzlichen Unfallversicherung e. V. und zu beziehen über Carl Heymanns Verlag;
4. die Berufsgenossenschaftlichen Informationen (BGI) 856 „Hilfen für die Planung von Beleuchtungsanlagen von Räumen mit Bildschirm- und Büroarbeitsplätzen“, Ausgabe: März 2005, herausgegeben von der Verwaltungs-Berufsgenossenschaft und zu beziehen über C. L. Rautenberg-Druck.
4.3.3.3 Lärmschutz
Lärmschutzmaßnahmen sind einzurichten und durch entsprechende Messungen vor der Inbetriebnahme und während des Regelbetriebes nachzuweisen. Folgende Normen sind mindestens zu berücksichtigen und deren Vorgaben sind einzuhalten:
1. die Verordnung zum Schutz der Beschäftigten vor Gefährdungen durch Lärm und Vibrationen (Lärm- und Vibrations-Arbeitsschutzverordnung – LärmVibrationsArbSchV) vom 6. März 2007 (BGBl. I S. 261), die zuletzt durch Artikel 3 der Verordnung vom 19. Juli 2010 (BGBl. I S. 960, 964) geändert worden ist, in der jeweils geltenden Fassung;
2. die VDI-Richtlinie 2569 „Schallschutz und akustische Gestaltung im Büro“, Ausgabe: Januar 1990, in den jeweils geltenden Fassungen, zu beziehen über die Beuth Verlag GmbH, Berlin, und beim Deutschen Patentamt archivmäßig gesichert niedergelegt.
4.3.3.4 Klimatechnik
Die Klimatisierung des Leitstellenraums ist für eine Temperatur von 19 bis 24 °C und eine relative Luftfeuchtigkeit zwischen 40 und 70 Prozent auszulegen. Die Raumbelüftung muss mit einer Luftgeschwindigkeit von 0,1 m/s erfolgen. Folgende Normen sind mindestens zu berücksichtigen und deren Vorgaben sind einzuhalten:
1. die Technische Regel für Arbeitsstätten ASR A3.5 „Raumtemperatur“, Ausgabe: Juni 2010 (GMBl Nr. 35 vom 23. Juni 2010, S. 751);
2. die Technische Regel für Arbeitsstätten ASR 5 „Lüftung“, vom 22. August 1979 (BArbBl. 10/1979 S. 103) berichtigt durch Bekanntmachung des BMA vom 13. September 1984 (BArbBl. 12/1984 S. 85);
3. die DIN 33403 „Klima am Arbeitsplatz und in der Arbeitsumgebung“ – Teil 3: „Beurteilung des Klimas im Warm- und Hitzebereich auf der Grundlage ausgewählter Klimasummenmaße“, Ausgabe: April 2001;
4. die DIN EN 13779 „Lüftung von Nichtwohngebäuden – Allgemeine Grundlagen und Anforderungen für Lüftungs- und Klimaanlagen und Raumkühlsysteme“, Deutsche Fassung EN 13779:2007, Ausgabe: September 2007.
4.3.3.5 Drucker
In der IRLS sind zwei Drucker zu installieren, die über Netzwerkanbindung alle für den Dienstbetrieb der IRLS relevanten Informationen ausdrucken können. Diese sind in Druckernischen anzuordnen. Es sind Flächen/Sideboards zur Aufstellung von Faxgeräten, erweiterten Bedieneinrichtungen und zur Unterbringung von Einsatzunterlagen vorzusehen.
4.3.4 Antennenanlagen
Antennenanlagen müssen für einen Nutzungszeitraum von mindestens 15 Jahren ausgelegt sein und mindestens 120 Prozent der zu erwartenden maximalen Windlast aufnehmen können. Der Antennenträger ist richtfunktauglich zu gestalten. Durch die Anordnung der Antennen mit einem Entkopplungsabstand (Koppeldämpfung) von 60 bis 80 dB ist die Interkanalmodulation zwischen den Sendern und die Desensibilisierung der Empfänger (Zustopfeffekt) zu verhindern. Bei den nachfolgend aufgeführten Frequenzbereichen sind bei einer Entkopplung von 40 dB folgende Mindestabstände erforderlich.
Tabelle 3: Mindestabstände der Antennen
Mindestabstände der Antennen
Funkbereich | vertikale Anordnung | horizontale Anordnung
Funkbereich | vertikale Anordnung | horizontale Anordnung
4 m | 6 m | 52 m
2 m | 3 m | 26 m
70 cm | 1 m | 9 m
Die vollständige Entkopplung ist über ergänzende Maßnahmen (zum Beispiel Einsatz von Weichen, Isolatoren) zu erreichen. Die ausreichende Entkopplung ist nachzuweisen. Ist der Standort der IRLS Standort für eine/mehrere Basisstation/en des Digitalfunks, sind die Vorgaben des Lieferanten umzusetzen. Antennenanlagen der IRLS sind mit einem inneren und einem äußeren Blitzschutz nach DIN EN 62305; VDE 0185-305 „Blitzschutz“ – Teil 1: „Allgemeine Grundsätze“, Deutsche Fassung IEC 81/335/CDV:2009, Ausgabe Januar 2010, Teil 2: „Risiko-Management“, Deutsche Fassung IEC 81/336/CDV:2009, Ausgabe Januar 2010, Teil 3: „Schutz von baulichen Anlagen und Personen“, Deutsche Fassung IEC 81/337/CDV:2009, Ausgabe Juni 2010, Teil 4: „Elektrische und elektronische Systeme in baulichen Anlagen“, Deutsche Fassung IEC 81/338/CDV:2009, Ausgabe März 2010 auszuführen. Die vorgegebenen Biegeradien verwendeter Antennenkabel sind durch bauliche Maßnahmen umfassend zu sichern. Die Kabeltrassen oder -leiter müssen 50 Prozent Reserven aufweisen.
4.3.5 Stromversorgung
4.3.5.1 Anforderungen
Die elektrischen Anlagen sind als TN-S-Netz nach DIN VDE 0100-100 „Errichten von Niederspannungsanlagen“ – Teil 1: „Allgemeine Grundsätze, Bestimmungen allgemeiner Merkmale, Begriffe“; Deutsche Übernahme HD 60364-1:2008, Ausgabe Juni 2009, auszuführen. Es ist ein zentraler Erdungspunkt für das gesamte elektrische Netz einzurichten. Die Stromversorgung der IRLS ist nach Möglichkeit über zwei separate Einspeisungen sicherzustellen. Der Überspannungsschutz im Netz der IRLS, bestehend aus den elektrischen Versorgungsnetzen, den Fernmeldenetzen, den Datennetzen sowie sonstigen Signalnetzen, ist mit Grob-, Mittel- und Feinschutz gemäß VDE-Vorschriften auszuführen. Alle Festverbindungen sind mit Überspannungsschutz auszurüsten. Innerhalb des Gebäudes ist das Netz für die IRLS und für die Gebäudeversorgung zu trennen. Die Stromversorgungstechnik ist zentral in den Technikräumen zu installieren. Bei allen modularen Netzgeräten ist die Stromversorgung als „n+1 Redundant“ auszuführen. Eine unterbrechungsfreie Stromversorgung (USV) und eine Netzersatzanlage (NEA) sind als Notstromversorgung vorzusehen. Das Notstromnetz ist ein Teil des gesamten Stromnetzes einer Liegenschaft mit separat geführten und abgesicherten Stromkreisen.
4.3.5.2 Unterbrechungsfreie Stromversorgung (USV)
Für den ELR, die Kommunikationsserver und alle Disponentenarbeitsplätze ist eine modular aufgebaute, redundante USV nach DIN IEC 62040-3; VDE 0558-530:2009-07 „Unterbrechungsfreie Stromversorgungssysteme (USV)“ – Teil 3: „Methoden zum Festlegen der Leistungs- und Prüfungsanforderungen“, Deutsche Fassung EN 62040-3:2001, Ausgabe Juli 2009, als Online-USV vorzusehen. Bei Ausfall von Teilkomponenten der USV muss für die zentralen Komponenten und die Hälfte der Disponenten- Arbeitsplätze die Stromversorgung sichergestellt sein. Die USV muss auch bei einer Auslastung von 50 Prozent den maximalen Wirkungsgrad erreichen. Die nachfolgend genannten Überbrückungszeiten sind sicherzustellen:
1. für die Datentechnik für das ELS (unter anderem Server, Storage, aktive Netzwerkkomponenten) ein Zeitraum von 30 Minuten;
2. für den BOS-Funk, die Notrufabfrage, die Alarmierung, das FMS, die Übertragungsanlage für Brandmeldungen, die Sprachdokumentation, den Wachalarm, die ELA und das GSM-Netz ein Zeitraum von acht Stunden.
3. eine 50-prozentige Teilbeleuchtung der Leitstelle. Zudem ist zu sichern, dass die IuK-Technik in den Technikräumen über 30 Minuten im spezifizierten Temperaturbereich gehalten wird.
4.3.5.3 Netzersatzanlage (NEA)
Eine stationäre Netzersatzanlage ist für den durch Notstrom abzudeckenden Energiebedarf einzurichten. Kraftstoff zum Betrieb der Notstromaggregate muss für die Dauer von zwölf Stunden zur Verfügung stehen. Soweit die zwei separaten Einspeisungen nicht wirtschaftlich sichergestellt werden können, muss Kraftstoff für 48 Stunden zur Verfügung stehen. Der Standort der Netzersatzanlage muss Gefährdungen durch Naturereignisse und technische Havarien berücksichtigen und ist gegen unbefugten Zutritt zu sichern. Ein Einspeisepunkt für die Anschaltung von mobilen NEA ist vorzusehen. Beim Anschluss einer mobilen NEA muss eine Trennung aller Pole des Netzes innerhalb der IRLS und dem öffentlichen Stromnetz erfolgen. Die USV und Netzersatzanlage muss als funktionsfähige Einheit nachgewiesen werden.
4.3.6 Haustechnik/Technische Gebäudeausrüstung
Einbruchs- und Zugangssicherung: Für die IRLS ist ein baulicher und technischer Einbruchschutz vorzusehen (BSI-Maßnahmekatalog M 1.19 „Einbruchsschutz“ und BSI-Publikation „IT-Sicherheit durch infrastrukturelle Maßnahmen“). Die Eingangstüren zum Gebäude und des Leitstellenbereichs sind mit einem Türöffnungs- und Zutrittssystem mit Videokontrolle und Gegensprechanlage auszustatten. Eine Integration der Öffnungseinrichtung in die Bedienoberfläche der FNA/Leitstellentische ist vorzunehmen. Die Technikräume sind gemäß Widerstandsklasse WK 3 auszuführen und auf Einbruch zu überwachen. Bedienung und Kontrolle: Die Zustandsanzeigen der leitstellenrelevanten Haustechnik müssen im Leitstellenraum angezeigt, die Funktionen bedienbar sein.
5. Verfügbarkeit
5.1 Anforderungen an die Verfügbarkeit
Für den Schutz vor möglichen Bedrohungen sind über den IT-Grundschutz hinaus nachfolgende Verfügbarkeiten je Kalendermonat (30 Tage/24 Stunden) zu gewährleisten. Die Verfügbarkeit endet mit der Mängelanzeige und beginnt mit der Inbetriebnahme nach Mängelbeseitigung und schriftlichem Nachweis. Die Sicherstellung der Verfügbarkeit der Notrufannahme kann auch durch organisatorische Maßnahmen (zum Beispiel die Inbetriebnahme von Rückfallebenen) erfolgen.
Tabelle 4: erforderliche Verfügbarkeiten von Anlagen der IRLS
erforderliche Verfügbarkeiten von Anlagen der IRLS
Nr. | Anlage | monatliche Verfügbarkeit | monatliche Ausfallzeit
Nr. | Anlage | monatliche Verfügbarkeit | monatliche Ausfallzeit
1 | Kommunikationstechnik (Funk-Notrufabfrage, Funkanlagen und Alarmierungssysteme) | 99,9 Prozent | 
2 | ELS der Informationstechnik (Systemserver, Disponentenarbeitsplätze, Notannahmeplätze) | 99,0 Prozent | 
3 | Netzsysteme, bestehend aus den angeschalteten Übertragungsnetzen und den Datennetzen innerhalb der IRLS | 99,9 Prozent | 
4 | Stromversorgung (allgemeine Stromversorgung, USV-Netz, Netzersatz) | 99,9 Prozent | 
5.2 Grundsätze der inneren Redundanz
Der Ausfall einzelner Dienste, wie Notruf, Sprach- oder Datenübertragung, ist durch technische Maßnahmen vor Ort aufzufangen. Dieses hat durch redundante Netzanbindungen, gedoppelte Komponenten und Notebenen zu erfolgen. Hierbei sind folgende Anforderungen zu realisieren:
1. die Sicherung des Normalbetriebs an mindestens 50 Prozent der installierten Disponentenarbeitsplätze durch redundante Baugruppen und Systeme einschließlich der Haustechnik und Energieversorgungssysteme bei Teilausfällen innerhalb der IRLS;
2. die USV als gedoppelte Anlage mit Bypassfunktion, jede USV sichert bei 75 Prozent Auslastung 50 Prozent der Maximallast der IRLS;
3. die Anschaltung der sicherheitsrelevanten Komponenten mit gedoppelten Netzteilen;
4. die Zuführung beider USV-Stromkreise und der Stromversorgung für Anlagen der Kommunikationstechnik in alle Leitstellenräume;
5. die redundante Auslegung der Klimaanlagen (zwei Einzelanlagen klimatisieren die Wärmelast zu je 50 Prozent);
6. die Platzierung der Trassen und Steigwege zwischen den Geschossen, so dass die Ausfallquote 50 Prozent der maximalen Kapazität in den Technikräumen und Leitstellenbereich (LAN, TK, Strom) nicht übersteigen kann;
7. die Darstellung der geforderten Ausfallsicherheit der Server über Methoden der Virtualisierung, Clusterung sowie Blade-Technologie und deren Verwendung für Speicherkonzepte;
8. die Onlineführung der Datensicherungen zu Standorten außerhalb der Liegenschaft, bei Verhinderung ist wöchentlich eine Datensicherung zu erstellen und der Sicherungsdatenträger an einen anderen Standort zu verbringen;
9. die Sicherstellung, dass die Datensicherung auch bei einem Hardwareausfall ohne Verzug die Wiederherstellung des Gesamtsystems zulässt;
10. die Bereitstellung von Verfahren, um bei Systemausfällen eine schnelle Wiederherstellung der vollen Funktionalität zu erreichen (Notfallhandbücher);
11. die Begrenzung der Störwirkreichweite auf das jeweilige Anlagenteil und auf das beteiligte Softwaretool, die Verhinderung von Kettenreaktionen sowie Dominoeffekten durch Sicherstellung der Betriebsfähigkeit jeder Einzelanlage;
12. die Einhaltung der Datensicherheit durch unter anderem den Einsatz eines Echtzeit-Virenscanners, das Einspielen sicherheitsrelevanter Updates von Betriebssystemen und den Einsatz von Softwareverteilungstools.
5.3 Grundsätze der externen Redundanz
5.3.1 Organisatorische Anforderungen
Der Ausfall ist unter anderem dadurch gekennzeichnet, dass Notrufe nicht angenommen, Einsätze nicht disponiert, Einsatzkräfte nicht alarmiert oder Einsatzunterstützung nicht geleistet werden können (Grundfunktionen). Ein erhöhtes Anrufaufkommen kennzeichnet nicht den Ausfall. Es erfolgt keine automatische Lastverteilung im Regelbetrieb. Bei Ausfall des Leitstellenstandortes ist die Aufgabenerfüllung von einem anderen Ort innerhalb der Zugangsnetze abzusichern. Die Redundanzleitstelle übernimmt Aufgaben beim Ausfall einer anderen IRLS. Die Aufgabenübernahme ist durch technische und organisatorische Maßnahmen vorzubereiten. Dabei sind die folgenden Fälle zu erfassen:
1. die IRLS unterliegt einem technischen Komplettausfall, das Personal steht für die Arbeit an einem anderen Ort zur Verfügung;
2. die IRLS ist technisch funktionsfähig, kann aber aufgrund zum Beispiel einer Räumung nicht genutzt werden, das Personal steht für die Arbeit an einem anderen Ort zur Verfügung;
3. die IRLS ist technisch funktionsfähig, aber das Personal steht teilweise oder vollständig nicht für die Arbeit in der IRLS zur Verfügung (zum Beispiel Pandemie). Die Aufgabenübernahme ist durch die Vernetzung mit einer benachbarten IRLS organisatorisch vorzubereiten und abzusichern. Der Übernahmefall ist gemeinsam zu üben. Für alle Disponenten sind gegenseitige Hospitationen vorzusehen. Für die Übernahme der Aufgaben bei Ausfall einer anderen IRLS ist bereits zur personellen Verstärkung bei besonderen Lagen im eigenen Zuständigkeitsbereich (zum Beispiel Unwetter, Großschadensfälle) ein Konzept zur schnellen Personalverstärkung zu erstellen. Bis zur personellen Verstärkung sind vorrangig die zeitkritischen Einsätze zu bearbeiten.
5.3.2 Konzeptionelle Anforderungen (Redundanzkonzept)
Mit dem Redundanzkonzept ist sicherzustellen, dass die Arbeitsfähigkeit einer IRLS unverzüglich wieder hergestellt wird oder eine sofort wirkende Alternative zur Verfügung steht. Der Ausfall technischer Einrichtungen muss bei vorübergehender Einschränkungen der Funktionalität unter Aufrechterhaltung der Grundfunktionen unverzüglich kompensiert werden. Dabei sind für abschätzbare Ausfallzeiten die nachfolgenden Maßnahmen einzuleiten:
Tabelle 5: Maßnahmen bei abschätzbaren Ausfallzeiten
Maßnahmen bei abschätzbaren Ausfallzeiten
Ausfallzeit | Maßnahme
Ausfallzeit | Maßnahme
bis zu 3 Stunden | „sofortige“ Übernahme der zeitkritischen Aufgaben durch Personal der übernehmenden IRLS
3 Stunden bis 7 Tage | Unterstützung durch Personal der ausgefallenen IRLS am Standort der übernehmenden IRLS
ab 8 Tagen | Realisierung einer Notleitstelle am Standort der ausgefallenen IRLS (oder in anderer Liegenschaft)
Mindestinhalte des Redundanzkonzeptes sind:
1. die Identifikation möglicher Störgrößen;
2. die Ermittlung und die Dokumentation von Ausfallszenarien jeder Störgröße;
3. die Minimierung der Zeit bis zur Feststellung einer Störung durch technische Maßnahmen;
4. die Beschreibung der Maßnahmen zur Kompensation eines Ausfalls;
5. die Minimierung der Zeit bis zum Wirksamwerden der erforderlichen Maßnahme. Das Vorgehen ist im Notfallhandbuch zu dokumentieren. Im Redundanzfall sind abweichende Betriebsabläufe, wie zum Beispiel das Melden eines Status und das Nachtragen im Einsatzprotokoll von Hand, zulässig.
5.3.3 Technische Anforderungen
Für die Sicherstellung der Übermittlung von Informationen bei Einsätzen, die den eigenen Bereich überschreiten, ist bereits für den Regelbetrieb die Datenübertragung von einer IRLS zu einer anderen IRLS vorzusehen. Über technische Voraussetzungen sind für den Redundanzfall zusätzlich die weiteren Kommunikationsformen, insbesondere Alarmierungs- und Funknetze zu bedienen. Hierfür sind die Anlagen zu verwenden, die die IRLS zur Erreichung der hohen Verfügbarkeit selbst vorhalten muss, um beispielsweise einem Ausfall von Verbindungswegen zu kompensieren. Folgende Möglichkeiten sind über das Leitstellennetzwerk für die Redundanzleitstelle einzurichten.
Tabelle 6: Vorgehensweisen im Redundanzfall bezogen auf die Kommunikationsformen
Vorgehensweisen im Redundanzfall bezogen auf die Kommunikationsformen
Nr. | Kommunikationsform | Vorgehensweise
Nr. | Kommunikationsform | Vorgehensweise
1 | Notruf 112 19222 19296 19292 | Das Routing/die Umleitung des Netzbetreibers zu einer anderen Stelle, die durch die übernehmende IRLS gezielt abgefragt werden kann (zum Beispiel zu vordefinierten Anschlüssen bei den Technikzentralen), ist zu gewährleisten.
2 | Alarmierung | Reserve-Alarmgeber, die innerhalb der Alarmierungsnetze in einer anderen Liegenschaft über das Netzwerk erreicht werden können (zum Beispiel in einer Feuerwache), sind zu nutzen. Als Notebene kann auch eine Nachalarmierungszentrale von Feuerwehren besetzt werden. Die Nutzung weiterer Medien, beispielsweise für die Alarmierung im Rettungsdienst (Analog- oder Digitalfunk, GSM), ist zulässig.
3 | Analogfunk | Reserve-Funkgeräte, die innerhalb der Funknetze in einer anderen Liegenschaft über das Netzwerk erreicht werden können (zum Beispiel in einer Feuerwache), sind zu nutzen. FMS-Dienste stehen hierbei möglicherweise nicht gesichert zur Verfügung, so dass der Status angesagt werden muss.
4 | Digitalfunk | Der Zugriff erfolgt über den eigenen Zugangsweg zum Digitalfunknetz mit Freischaltung der zusätzlichen notwendigen Berechtigungen für den Bereich der ausgefallenen IRLS. Dabei sind Einschränkungen bei automatisierten Datendiensten und Managementfunktionen aus dem ELS zulässig. Die Möglichkeiten des Netzes und dessen Managementkomponenten (zum Beispiel DWS) sind zu nutzen.
5 | Statusinformationen | Ein zentraler Systemdienst, der den Informationsabgleich zwischen den IRLS sichert, ist zu nutzen. Diese Funktion ist insbesondere im Digitalfunk als zentraler Status- und SDSSystemdienst an den Standorten der Technikzentralen vorzusehen.
6 | Geo-Basisdaten | Die IRLS halten den gesamten Kartenbestand und Adressverzeichnisse für ganz Sachsen und angrenzende Bereiche für eine gesicherte Ortsabfrage bereit. Notwendige Geobasisdaten werden den IRLS über einen zentralen Server in den Technikzentralen bereitgestellt.
7 | Objektdaten Einsatzpläne | Der gegenseitige Austausch von Objektdaten und Einsatzplänen sowie der festgelegten Zuständigkeitsbereiche und der Alarm- und Ausrückeordnungen ist zu sichern (zum Beispiel elektronischer Versand von pdf-Dokumenten). Hierfür ist ein zentraler Server oder Backupserver, welcher den Informationsabgleich zwischen den IRLS sichert, vorzusehen. Diese Funktion ist in den Technikzentralen einzurichten.
8 | Alarmempfangs- einrichtung für BMA | Die Maßnahmen zum Routing/zur Umleitung für Übertragungsanlagen für BMA sind zwischen dem Betreiber und der IRLS festzulegen.
6. Anforderungen an den Betrieb der IRLS
6.1 Alarm- und Ausrückordnung
Von allen IRLS ist zur Realisierung der Redundanzanforderungen eine normierte Alarmordnung im ELS vorzuhalten um sicherzustellen, dass landesweit einheitliche Alarmstichwörter und -kategorien verwendet werden. Die Alarm- und Ausrückordnungen müssen daher die Vereinheitlichung der Alarmstichwörter und -kategorien, die Reduzierung der Gesamtzahl der Alarmstichwörter und -kategorien auf ein notwendiges Maß und die Ergänzung der Alarmstichwörter und -kategorien in einheitlicher Form realisieren. Die Alarmierung enthält die zwei Hauptbestandteile „Alarmstichwort“ und „Alarmkategorie“. Diese können abhängig vom Alarmstichwort durch das „Ergänzungsstichwort“ und die „Ergänzungskategorie“ präzisiert werden. Die Alarmstichwörter sind:
1. Brand,
2. Hilfeleistung,
3. ABC-Einsatz,
4. Feuerwache/Feuerwehrgerätehaus besetzen,
5. Katastrophenabwehr,
6. Notfallrettung,
7. Krankentransport,
8. MANV. Zusätzlich sind bei Bedarf die Alarmstichwörter KV-Vermittlung und Service/Sonstiges zu verwenden. Den Alarmstichwörtern Brand, Hilfeleistung und ABC-Einsatz werden folgende Alarmkategorien zugeordnet, die das jeweilige Alarmstichwort hinsichtlich der Intensität beziehungsweise des Gefährdungsgrades differenzieren. Die Alarmkategorien sind in Tabelle 7, Tabelle 8 und Tabelle 9 dargestellt.
Tabelle 7: Alarmkategorien zum Alarmstichwort Brand
Alarmkategorien zum Alarmstichwort Brand
Alarmstichwort | Alarmkategorie | Merkmale
Alarmstichwort | Alarmkategorie | Merkmale
Brand | klein | Kleinbrände ohne Tendenz zur Ausbreitung
mittel | Brände mit Tendenz zur Ausbreitung, Gefahr für Personen, Tiere, Umwelt und Sachwerte
groß | Brände mit starker Tendenz zur Ausbreitung, Gefahr für größere Anzahl von Personen und Tieren sowie Umwelt und erhebliche Sachwerte, hoher Löschmittelbedarf
BMA | Feuermeldung durch Brandmeldeanlage
Tabelle 8: Alarmkategorien zum Alarmstichwort Hilfeleistung
Alarmkategorien zum Alarmstichwort Hilfeleistung
Alarmstichwort | Alarmkategorie | Merkmale
Alarmstichwort | Alarmkategorie | Merkmale
Hilfeleistung | klein | einfache technische Hilfeleistung mit geringem Umfang
mittel | technische Hilfeleistung, Gefahr für Personen, Tiere, Umwelt und Sachwerte
groß | technische Hilfeleistung mit größerem Umfang, Gefahr für größere Anzahl von Personen und Tiere sowie Umwelt und erhebliche Sachwerte
Tabelle 9: Alarmkategorien zum Alarmstichwort ABC-Einsatz
Alarmkategorien zum Alarmstichwort ABC-Einsatz
Alarmstichwort | Alarmkategorie | Merkmale
Alarmstichwort | Alarmkategorie | Merkmale
ABC-Einsatz | klein | Freiwerden einer geringen Menge eines identifizierten, umweltgefährdenden Stoffes, geringe Toxizität und Mobilität/Ausbreitung
mittel | Freiwerden von geringer Menge nicht identifizierten Stoffes oder einer größeren Menge eines identifizierten Stoffes mit geringer Toxizität, geringe Mobilität/Ausbreitung
groß | alle übrigen Fälle
Zur Ergänzung der Alarmstichwörter und -kategorien sind Informationen bezüglich der Personengefahr, der Objektart und der Objektnutzung anzufügen (Tabelle 10).
Tabelle 10: Ergänzung der Alarmstichwörter und Alarmkategorien
Ergänzung der Alarmstichwörter und Alarmkategorien
Ergänzungsstichwort | Ergänzungskategorien
Ergänzungsstichwort | Ergänzungskategorien
Personengefahr | keine
unbekannt
> 5 Personen
Objektart | Gebäude
Autobahn
Wald
et cetera
Objektnutzung | Theater
Betrieb nach Störfall-Verordnung
et cetera
Beim Alarmstichwort Notfallrettung werden die Alarmkategorien entsprechend Tabelle 11 zugeordnet.
Tabelle 11: Alarmkategorie und Merkmale des Alarmstichworts Notfallrettung
Alarmkategorie und Merkmale des Alarmstichworts Notfallrettung
Alarmstichwort | Alarmkategorie | Merkmale
Alarmstichwort | Alarmkategorie | Merkmale
Notfallrettung | ohne Notarzt | RTW
Bergwacht
Wasserwacht
RTW-Verlegung
RTW-Diagnostikfahrt
Entlassung beatmet
mit Notarzt | Einsatzmerkmale laut Notarztindikationskatalog
Beim Alarmstichwort Krankentransport werden die Alarmkategorien entsprechend Tabelle 12 zugeordnet.
Tabelle 12: Alarmkategorie und Merkmale des Alarmstichworts Krankentransport
Alarmkategorie und Merkmale des Alarmstichworts Krankentransport
Alarmstichwort | Alarmkategorie | Merkmale
Alarmstichwort | Alarmkategorie | Merkmale
Krankentransport | mit Stuhl | KTW normal
Diagnostikfahrt
Verlegung Fernfahrt
Dialyse
sitzend | KTW normal
Diagnostikfahrt
Verlegung Fernfahrt
Dialyse
liegend | KTW normal
Diagnostikfahrt
Verlegung Fernfahrt
Dialyse
RTH-Sekundär | RTH
Das Alarmstichwort MANV ist in die Alarmkategorien MANV 1 bis MANV 4 zu unterteilen.
Weitergehende Anforderungen sind zwischen den Betreibern im Einvernehmen mit den Trägern der IRLS festzulegen. Die erforderlichen Festlegungen bezüglich der Alarmreaktion und der Ausrückordnung sind durch die Träger des Brandschutzes und die Träger des Rettungsdienstes zu treffen. Bereichsfolgen sind zu berücksichtigen.
6.2 Dokumentation, Statistik und Archivierung
6.2.1 Dokumentation
Die IRLS erfasst, speichert und stellt Daten für eine differenzierte und regelmäßige Einsatzauswertung dem zuständigen Träger des Rettungsdienstes sowie den örtlichen Brandschutz- und Rechtsaufsichtbehörden zur Verfügung. Für die Notfallrettung ist der minimale Notarztdatensatz nach DIVI in der aktuellen Fassung abzulegen. Die Datenerfassung in der IRLS kann um Daten erweitert werden, die für das Qualitätsmanagementsystem erforderlich sind. Darüber hinausgehende Dokumentationen sind vom Träger des Rettungsdienstes im Benehmen mit den Kostenträgern sowie von der örtlichen Brandschutzbehörde und der unteren BRK-Behörde im Benehmen mit dem Träger der IRLS festzulegen. Die Daten sind so aufzuarbeiten, dass eine landesweite Vergleichbarkeit gegeben ist. Eine zentrale Archivierung der statistisch relevanten Daten ist vorzunehmen. Die Statistikdaten (standardisierte Berichte/Rapport) des Rettungsdienstes sind den Kostenträgern und den Trägern des Rettungsdienstes regelmäßig zur Verfügung zu stellen. Einsatzdaten des Brand- und Katastrophenschutzes, die für statistische Zwecke benötigt werden, sind regelmäßig den örtlichen Brandschutzbehörden und den BRK-Behörden zur Verfügung zu stellen. Alle nutzungsrelevanten Aktivitäten des ELS der IRLS sind zu dokumentieren. Dabei sind folgende Mindestangaben regelmäßig sicherzustellen:
1. die Aufkommensverteilung nach Tageskategorien und Stundenintervall von RTW, NEF, KTW sowie von Fahrzeugen des Brand- und Katastrophenschutzes, differenziert nach Fahrzeugtypen, und bei Bedarf die Einsätze des Kassenärztlichen Notfalldienstes von:
a)
Montag bis Freitag;
b)
Samstag;
c)
Sonntag;
d)
Feiertag;
2. die Echtzeiten zur Einhaltung von Hilfsfristen:
a)
Zeit des Beginns der Disponierung;
b)
Zeit des Endes der Disponierung (Alarmierung);
c)
Abfahrt der Einsatzmittel (Status 3);
d)
Ankunftszeit (Status 4) nach:
aa)
Fahrten unter Sondersignal;
bb)
Alarmierung außerhalb des Standortes;
cc)
Einsatzorte an öffentlichen Straßen;
dd)
Einsatzorte an nichtöffentlichen Straßen (Anliegerstraßen, Privatwegen, Sonstige);
3. die Unterteilung der Einsätze nach:
a)
Paralleleinsätze;
b)
Einsätze von nachalarmierten Rettungsmitteln;
4. die sonstigen Einsatzzeiten:
a)
Zeitpunkt der Annahme des Gesprächs zu Hilfeanforderungen;
b)
Zeitpunkt des Endes des Gesprächs zu Hilfeanforderungen;
c)
Freimeldung (Status 1);
d)
Zeiten der Rückkehr zum Standort (Status 2);
e)
Wiederherstellung der Einsatzbereitschaft;
5. die statistische Auswertung des Anruferverhaltens:
a)
Häufigkeit des Auflegens durch den Anrufer vor Beginn der Abfrage über die Notrufnummer 112;
b)
Häufigkeit des Auflegens durch den Anrufer vor „Ansage vor Abfrage“ über die Nummer 19222 und Sonstige;
c)
Häufigkeit des Auflegens durch den Anrufer während der „Ansage vor Abfrage“ über 112;
d)
Häufigkeit des Auflegens durch den Anrufer während der „Ansage vor Abfrage“ über 19222, Sonstige;
e)
Anrufwartezeit vor Abfrage über die Notrufnummer 112;
f)
Anrufwartezeit vor Abfrage über die Nummer 19222 und Sonstige;
g)
Häufigkeit des Duplizitätsfalles (höhere Anzahl eingehender Notrufe als freie Disponenten verfügbar sind; hiervon nicht betroffen sind Notrufe, in denen die Anrufwartezeit nicht mehr als 15 Sekunden beträgt) der Notrufnummer 112;
h)
Häufigkeit von Anrufen aus dem Festnetz und Handynetzen.
6.2.2 Statistik
Für die Statistik sind entsprechende Druck- und Layoutformate einzustellen und zu konfigurieren. Die Statistik muss neben der freien Auswertung an die offiziellen Statistikdaten und Auswertungen der Feuerwehr und des Rettungsdienstes über vordefinierte änderbare Filter durch den Administrator anzupassen sein. Die Statistik soll unmittelbar nach durchgeführten Einsätzen zu erstellen sein. Das Datenbankschema und alle Tabellen- und Datensatzbeschreibungen sind bereitzustellen. Die Statistik ist in benutzerdefinierten Zeiträumen als Tagesstatistik, Wochenstatistik, Monatsstatistik, Jahresstatistik oder Mehrjahresstatistik auszugeben. Zusammengestellte Daten sind über eine entsprechende Exportschnittstelle in andere Programmmodule, zum Beispiel Microsoft Office, für weitere Bearbeitungen und Auswertungen sowie für die Erstellung von Grafiken zu übertragen und hier für die Bearbeitung einzurichten. Im System sind Hauptgruppen mit frei einstellbaren Untergruppen zur Auswertung bereitzustellen. Im Statistikmodul ist ein Login für die Benutzung mit Anmelde- und Passwort der berechtigten Personen einzurichten, damit der Anwender auf unterschiedliche Menüpunkte des Statistikmoduls zugreifen und diese bearbeiten kann. Bestehende Statistiken sind über entsprechende Filtertools abzufragen, zu ändern und durch neue Ergebnisse zu ergänzen, zu ändern und zu bearbeiten. Grundlage der Statistik ist die Datenbankanwendung in einem Datenmodell mit Festlegung der Informationen in:
1. Tabellen;
2. Datenfeldern mit entsprechenden Formaten;
3. Beziehungen der Tabellen untereinander.
6.2.3 Archiv
Die abgeschlossenen Einsätze sind mindestens über einen Zeitraum von 120 Monaten zu archivieren, soweit nicht anderslautende Vorschriften eine längere Archivierung erfordern. Dabei sind die datenschutzrechtlichen Bestimmungen einzuhalten. Die Archivierung hat unabhängig von den Daten des ELS zu erfolgen. Es sind allgemein übliche Standardformate zu verwenden. Über Informationsdateien muss zusätzlich begleitendes Schriftgut verwaltet werden können. Das Archivtool muss Quer- und Quellverweise in der Dokumentation verwalten. In der Archivierung sind Suchkriterien über die Archivdokumentation/das Archivmanagement zu unterstützen, zum Beispiel Suche nach:
1. dem Einsatzmittel;
2. der Einsatzart;
3. der Einsatznummer;
4. dem Einsatzdatum;
5. dem Namen;
6. dem Einsatzstichwort;
7. dem/der/den Melder/Meldergruppe/Melderattributen und
8. dem Einsatzort. Die archivierten Datensätze sind auf den Verwaltungsserver und parallel auf externe Datenträger zu übertragen. Nach Beendigung der Archivierungsdauer sind die Einsätze über die Systemadministration als zu löschende Dateien anzuzeigen. Der Systemadministrator muss nach einer Auswahl Datensätze löschen oder archivieren können.
7. Schulungskonzept
Auf Grundlage des Rollenkonzepts (Nummer 4.2.2) ist entsprechend der Aufgaben der Nutzergruppen ein Schulungskonzept festzulegen. Die Schulungsinhalte ergeben sich dabei aus den nachfolgend genannten Aufgaben der Nutzergruppen:
1. Disponent – Bedienung der technischen Systeme bezüglich der Einsatzsachbearbeitung;
2. Schicht-/Dienstgruppenführer – erweiterte Bedienung der technischen Systeme bezüglich der Einsatzsachbearbeitung;
3. Systemadministratoren – Systemadministration, Datensicherung, Fehlersuche und Störungseingrenzung innerhalb der IRLS sowie Zusammenarbeit mit Dritten;
4. Datenpfleger – Datenerfassung und -pflege, Datenabfrage innerhalb der Datenbanken;
5. Führungs- und Organisationspersonal (Managementebene) – Grundlagenwissen sowie Planungs-, Organisations- und betriebliche Aspekte.
Während des Betriebes sind Fortbildungen, zum Beispiel aufgrund technischer Neuerungen oder organisatorischen Änderungen, durchzuführen. Hierzu ist ein Übungsmodul zu verwenden, das eine Beeinflussung der operativen Daten von ELS und FNAS wirksam verhindert. Entsprechend erzeugte Daten sind als Übungsdaten zu kennzeichnen. Die Inhalte der Fortbildungen werden durch den Leiter der IRLS festgelegt.
Die Aus- und Fortbildungen haben schwerpunktmäßig auf die fehlerfreie Bedienung der Systeme sowohl in Standard- als auch in Ausnahmesituationen (zum Beispiel besondere Einsatzlage, Großschadenslage, Katastrophenszenarien, Beherrschung von unvorhersehbaren Zwischenfällen) abzuzielen. Sie bestehen aus einem theoretischen und einem praktischen Teil.
8. Abkürzungsverzeichnis
Abkürzungsverzeichnis
Abkürzung | Erläuterung
ABC | Atomare, biologische oder chemische Stoffe
ADA | Audiodokumentationsanlage
BMA | Brandmeldeanlage(n)
BOS | Behörden und Organisationen mit Sicherheitsaufgaben
BSI | Bundesamtes für Sicherheit in der Informationstechnik
DAG | Digitaler Alarmgeber
DAU | Digitaler Alarmumsetzer
DIN | ursprünglich „Deutsche Industrienorm“, Dokument vom Deutschen Institut für Normung
DISMA | Disaster Management (rechnergestütztes Gefahrenabwehrsystem)
DIVI | Deutsche Interdisziplinäre Vereinigung für Intensiv- und Notfallmedizin
DWS | Dispatcher Work Station (Verwaltungseinrichtung für Teilnehmer)
EDV | Elektronische Datenverarbeitung
ELA | Elektronische Lautsprecheranlage
ELR | Einsatzleitrechner
ELS | Einsatzleitsystem
FMS | Funkmeldesystem
FNAS | Funk-/Notrufabfragesystem
FwH | Feuerwehrhaus
FZA | Fahrzeugzustandsanzeige
GIS | Geografische(s) Informationssystem(e)
GPS | Global Positioning System (Globales Navigationssatellitensystem)
GSM | Global Standard for Mobile (Mobiltelefonstandard)
HLK | Heizung, Lüftung, Klima
IRLS | Integrierte Regionalleitstellen
IuK | Information und Kommunikation
KatS | Katastrophenschutz
KTW | Krankentransportwagen
KV | Kassenärztliche Vereinigung
LAN | Local Area Network (lokales Netzwerk in der Computertechnik)
LIP | Location Information Protokoll (Protokoll für Anforderung und Aussendung der Positionierungsdaten)
MANV | Massenanfall von Verletzten und Erkrankten
NEA | Netzersatzanlage
NEF | Notarzteinsatzfahrzeug
QM | Qualitätsmanagement
RTW | Rettungswagen
RTH | Rettungshubschrauber
SDS | Short Data Service (Kurznachrichtendienst im Digitalfunk)
SMS | Short Message Service (Kurznachrichtendienst bei Mobiltefonen)
SPS | Speicherprogrammierbare Steuerung
TK | Telekommunikation
TEL | Technische Einsatzleitung
UMS | Unified Messaging System (Einheitliches Nachrichtenübertragungssystem)
USV | Unterbrechungsfreie Stromversorgung
VDE | Verband der Elektrotechnik, Elektronik, Informationstechnik e. V.
XML | Extensible Markup Language (erweiterbare Auszeichnungssprache)
ZTDB | Zentrale Telefonbuchdatenbank Sachsen
