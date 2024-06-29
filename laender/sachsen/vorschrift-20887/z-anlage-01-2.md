# Anlage 1 zu Beschluss bundesweites Clearingverfahren zur Zuscheidung der Einnahmen aus dem Deutschlandticket auf Basis des „Leipziger Modellansatzes“
Verfahrensbeschreibung Datenmeldung Deutschland-Ticket
1. Grundsätzliches
–
Die Vertriebsdatensammlung (VDS) durch die Clearingstelle (light) muss frühestmöglich nach Verkaufsstart beginnen können
–
Daher geht Schnelligkeit und Einfachheit in der Meldung vor Detailierung
–
Die vertreibenden Unternehmen müssen schnellstens über Anforderungen und Meldewege informiert werden, um möglichst zeitnah alle Anforderungen an die Datenstruktur der Meldungen umsetzen zu können.
–
Die Meldung erfolgt „kaskadierend“/stufenweise:
•
Vom VU/Verkäufer an die „gewohnte“ Tariforganisation (TO), z. B. Verkehrsverbünde (TO=Tarifgeber: umfasst alle Verbünde, Landestarife, DTV, Haustarifgeber etc.).
•
Von der TO an die Clearingstelle
•
Haustarife können selbst direkt an Clearingstelle melden oder an „nahestehende“ Verbundorganisation
–
Der Ablageort muss sicher genug sein, aber allen Beteiligten Zugriff gewähren
•
Vorschlag: einfacher Sharepoint auf den alle TO ihre Excel-Tabelle ablegen. Ob ggf. weitere Formate (csv, xml) möglich sind, ist mit der Clearingstelle operativ zu klären.
•
Rechteverwaltung einrichten
•
Formularvorlage als Anlage erstellen
–
Die Meldung der Deutschlandtickets an die Clearingstelle erfolgt bis zum 20. Kalendertag des Folgemonats.
–
Es sind in einem Monat alle verkauften Deutschlandtickets zu melden. Im Regelfall sind das Deutschlandtickets, deren erster Geltungstag im jeweiligen Meldemonat liegt (d. h. bspw. für die Meldung vom 20. Juni alle Deutschlandtickets mit erstem Geltungstag im Mai).
–
Die Meldung der restlichen Angebote an die Clearingstelle erfolgt bis zum 50. Tag nach Ende eines Monats (z. B.: Verkäufe des Mai bis zum 20. Juli
–
Grundsatz: jedes D-Ticket ist, unabhängig vom letztlichen Abgabepreis, zu 49 € zu melden, einzige (!) Ausnahme: Jobticket à 46,55 € bzw. (nur 2023) zu abweichende Preisen im Solidarmodell und Starterkarten. Die 49 € sind auch zu melden für Semesterticket-Upgrades, Schülertickets, Seniorentickets etc.
2. Datenstruktur
Es gibt drei Säulen bei der Datenmeldung (Im besten Fall können alle drei Säulen über dieselbe technische Schnittstelle gemeldet werden):
1.
Die D-Ticket-Verkaufsmeldung
2.
Die Verkäufe aller anderen Tickets „Restliches Angebot“
3.
Soll-Einnahmen (einmalig)
Jede Datenmeldung enthält Dimensionen zur Aggregation (wie Verkaufs- und Geltungsmonat), Stammdaten (wie den Namen der Tariforganisation) und die Eigentlichen Meldedaten (Bruttoerlös und ggf. Stück). Bei bundeslandübergreifenden Tariforganisationen ist ein Indikator für die Aufteilung auf die Bundesländer mitzuliefern.
–
D-Ticket-Aggregationsebenen, Datenstruktur und Stammdatum:
Hinweis: PLZ des Kundenwohnorts müssen bereits mit Start des Verkaufs des D- Tickets vom Kunden abgefragt und so zeitnah wie möglich, aber spätestens ab 01.10.2023, in die Meldungen integriert werden. Nicht in allen Fällen liegen die organisatorischen und technischen Voraussetzungen für eine Meldung der Wohnort-PLZ vor oder können bis zum Januar 2024 geschaffen werden. Daher ist in einigen eng umgrenzten Sondersituationen ein Übergangszeitraum bis Ende September 2024 nötig. Dies betrifft Konstellationen, in denen die Abwicklung der Ticketausgabe an den Endkunden nicht durch die Verkehrsunternehmen oder Verbünde erfolgt, sondern über branchenfremde Dritte. In diesen Fällen gelten folgende Hilfsregeln:
•
Bei Jobtickets kann, wenn die Wohnort-PLZ nicht vorliegt, hilfsweise und übergangsweise bis einschließlich September 2024 die PLZ der Betriebsstätte (alternativ zum Wohnort des Kunden) verwendet werden.
•
Bei Semestertickets, bei denen die Abwicklung des D-Ticket-Upgrades durch die Hochschulen erfolgt, sowie in einem eventuellen D-Ticket- Solidarmodell ab 2024, kann hilfsweise und übergangsweise bis zum Ende des Sommersemesters 2024 die PLZ des Hochschulstandorts verwendet werden. Voraussetzung für eine Meldung der Wohnort-PLZ bei Studierenden ist, dass die Hochschulverwaltungen in Vollsolidarmodellen die notwendigen Daten zuliefern.
•
Bei Schülertickets, deren Abwicklung über die Schulverwaltungen oder Schulsekretariate erfolgt, kann, wenn die Wohnort-PLZ nicht vorliegt, hilfsweise der Schulstandort verwendet werden, da davon auszugehen ist, dass in diesen Fällen Schul- und Wohnort unmittelbar beieinander liegen und nur in seltenen, vernachlässigbaren Ausnahmenfällen in verschiedenen Bundesländern.
Der Meldung an die Clearingstelle ist ein Hinweis hinzuzufügen, ob die Meldung (insgesamt, nicht je Datensatz) Daten enthält, bei denen an Stelle der Wohnort-PLZ die Betriebsstätten-, Hochschulort- oder Schulort-PLZ enthalten ist.
•
erster Geltungstag (am Anfang immer der erste des Geltungsmonats)
•
Ticketart (gemäß Tarifbestimmungen, z. B. Standard, JobTicket, ab 2024 ggf. SemT) -> numerische Codierung für Ticketart festlegen (1: normal, 2: JobT, 3. JobT im Vollsolidarmodell oder Starterkarte zu abweichendem Preis (nur 2023); 4. sonstige Sonderfälle, später zusätzlich ggf. 5: Ergänzungskarten, 6. D-Ticket-Semestertickets im bundesweiten Vollsolidarmodell, …)
•
Wohnort-PLZ des Kunden (ab 01.10.23 Pflichtfeld, bis dahin fakultativ). Bei Jobtickets und Semestertickets hilfs- und übergangsweise bis Ende September 2024 der Arbeits- bzw. bis Ende des Sommersemesters 2024 der Hochschulort, wenn keine Wohnort-PLZ vorliegt. Bei Schülertickets hilfsweise dauerhaft der Schulort, sofern keine Wohnort-PLZ vorliegt. Bei ausländischen PLZ den ISO-Ländercode (alphanummerisch zweistellig: CH, AT, Pl…)
•
Stück (falls Einzeldatensätze geliefert werden, ist Stück = 1 zu melden)
•
Gesamteinnahme der Tariforganisation (immer Brutto und immer inkl. eventueller Auffüllbeträge einzelner Bundesländer) -> (Stornos sind negative Einnahmen und werden saldiert)
■
Korrekturen aus dem Vormonat werden mit der nächsten Monatsmeldung nachgemeldet bzw. storniert.
■
Das Inkassorisiko liegt beim verkaufenden VU
•
Tariforganisation/Tarifgeber
•
(Verkaufendes Unternehmen -> muss beim Tarifgeber vorgehalten werden – > aber nicht gemeldet)
–
Bei länderübergreifenden Tariforganisationen/Tarifgebern ist zu Reporting- und Monitoringzwecken die voraussichtliche Schlüsselung auf die beteiligten Bundesländer nach EAV zu melden. Restliches Angebot (exkl. D-Ticket):
•
Meldemonat (alle Einnahmen, die im Vormonat gemeldet wurden)
•
Korrekturen werden für dem Monat in die Meldung aufgenommen, in dem sie gemeldet werden
•
Ticketgruppe: 1–4 (siehe Abschnitt 3)
•
Gesamteinnahme
•
Tariforganisation/Tarifgeber
•
Bei länderübergreifenden Tariforganisationen/Tarifgebern ist zu Reporting- und Monitoringzwecken die voraussichtliche Schlüsselung auf die beteiligten Bundesländer nach EAV zu melden.
–
Soll-Einnahme inkl. tariflicher Fortschreibung gemäß Musterrichtlinie (einmalige Meldung – monatsscharf)
•
Monat
•
Gesamteinnahme = Sollerlöse/Erwartungswert monatsscharf für Nachteilsausgleich (2023) (Anteilig für Mai–Dezember)
•
Tariforganisation/Tarifgeber
•
Bei länderübergreifenden Tariforganisationen/Tarifgebern ist zu Reporting- und Monitoringzwecken die voraussichtliche Schlüsselung auf die beteiligten Bundesländer nach EAV zu melden.
Lieferzeitpunkt: 1. Mai 2023 (im Vorlauf zur ersten D-Ticket-Meldung), frühestens jedoch drei Wochen nach Veröffentlichung der Musterrichtlinie
3. Definition Ticketgruppen: Definition der Ticketgruppen analog zur VDV-Corona-Abfrage (etabliert und vergleichbar)
Ticketgruppen
Bezeichnung der Ticketgruppe | Einzel- und Mehrfahrtenkarten | Tages- und Mehrtageskarten | Zeitkarten ohne Abos (>24h) | Abos exkl. D-Ticket
Bezeichnung der Ticketgruppe | Einzel- und Mehrfahrtenkarten | Tages- und Mehrtageskarten | Zeitkarten ohne Abos (>24h) | Abos exkl. D-Ticket
Codierung Ticketgruppe | 1 | 2 | 3 | 4
Enthält Angebote | – Einzelfahrkarten Erwachsene/Kinder/Gruppen – Hin/Rück – Streifenkarten – X-Fahrten-Karten – Fahrradkarten – Sonstiges (alles, was nicht eindeutig zugeordnet werden kann) | – Pauschalpreistickets (Ländertickets, QdL, etc.) – Tageskarten/Gruppentageskarten | – Formen von Mehrtageskarten – Wochenkarten (Ausbildung/Erwachsene) – Monatskarten (Ausbildung/Erwachsene) – 10er Tagesticket | – Alles, was im Normalfall mehr als einen Monat gilt – Abo-Jahreskarten (Ausbildung/Erwachsene) – Abo-Monatskarten (Ausbildung/Erwachsene) -> keine D-Tickets – Jobtickets – Semestertickets – Azubitickets – Netzkarten
Zu einzelnen, noch festzulegenden Zeitpunkten ist das restliche Angebot aufgegliedert nach einzelnen Ticketarten zu melden. Dies kann auch den Monat April 2023 zwecks Bestimmung des Zustands vor Einführung des D-Tickets betreffen. Die Details hierzu werden rechtzeitig durch die Clearingstelle kommuniziert.
4. Erläuterungen (FAQ):
Anmerkung 1: Anforderungen an die Datenstruktur und den Meldeprozess müssen bis spätestens Anfang März vorliegen, damit bis zum Verkaufsstart am 03.04.2023 die Verkaufs-/Buchungssysteme ggf. entsprechend ertüchtigt werden können.
Erläuterung zu Anmerkung 1: Die Datenstruktur ist mit diesem Dokument und dem Excel-Anhang spezifiziert. Der genaue Meldeprozess muss mit der operativen Stelle abgestimmt werden, die von der Arge aus VDV, DTV, BSN und BDO spezifiziert werden muss.
Frage 2: Wer trägt die Verantwortung für die rechtzeitige Datenlieferung Dritter?
Erläuterung zu Frage 2: Jeder Tarifgeber trägt die Verantwortung für die rechtzeitige Meldung in seinem Tarif verkaufter Tickets.
Frage 3: Wie wird mit Sondersachverhalten vorgegangen, die zu verspäteten Meldungen führen (Nachmeldungen, Stornierungen, Rückrechnungen etc)?
Erläuterung zu Frage 3: Verspätete Meldungen und Korrekturmeldungen erfolgen immer in der nächsten Monatsmeldung nach Bekanntwerden des Sondersachverhalts.
Frage 4: Genügt für die Meldung eine Aggregation auf Ebene der Tariforganisation oder ist eine Differenzierung nach KVP notwendig?
Erläuterung zu Frage 4: Eine Aggregation auf Ebene der Tariforganisation (bspw. Verbund) genügt.
Frage 5: Ist eine Gesamtstückzahl des D-Tickets zu melden oder ist eine Differenzierung ist in reguläre Deutschlandtickets, Starterkarten, Upgradekarten, subventionierte Versionen des Deutschlandtickets etc.?
Erläuterung zu Frage 5: Alle Karten, die 49 € melden, werden in der D-Ticket- Meldung im Feld Ticketart mit Code 1 gemeldet. Dies betrifft vorerst alle (!) Karten mit den folgenden beiden, klar definierten Ausnahmen: JobTickets, Starterkarten. JobTickets mit 5 % Rabatt werden im Feld Ticketart mit Code 2 gemeldet. Nur im Jahr 2023 werden JobTickets im Vollsolidarmodell und Starterkarten ohne Preisangabe, d. h. nur mit Stückzahl und Gesamteinnahme, im Feld Ticketart mit Code 3 gemeldet.
Frage 6: wie ist die Schlüsselung auf die Bundesländer für bundeslandübergreifende Verbünde herzuleiten?
Erläuterung zu Frage 6: Diese Information kann, sofern keine monatsaktuelle Information vorliegt, beispielsweise aus der vergangenen Jahresabrechnung oder einer vergleichbaren Quelle hergeleitet werden.
