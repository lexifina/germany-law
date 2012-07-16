---
ecli: "ECLI:DE:BPatG:2012:160712B7Wpat94.11.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 94/11"
decided: "2012-07-16"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2012&Sort=1&Seite=56&nr=23746&anz=1451&pos=840&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2012-07-16_7_W-pat_94_11_NA_0.txt"
cites_law: ["germany/bund/acts/gvg/0013.md", "germany/bund/acts/patg/0039.md", "germany/bund/acts/patg/0100.md", "germany/bund/acts/zpo/0145.md"]
---

# Bundespatentgericht, 7 W (pat) 94/11 vom 2012-07-16

## Entscheidung

BUNDESPATENTGERICHT



    7 W (pat) 94/11
_______________________

    (Aktenzeichen)




                              BESCHLUSS

                            In der Beschwerdesache


              betreffend die Patentanmeldung 11 2004 002 505.2-53
                              (hier: Teilanmeldung)


…




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
16. Juli 2012 durch den Vorsitzenden Richter Dipl.-Ing. Univ. Höppler und die
Richter     Dipl-Phys.    Dipl.-Wirt.-Phys.Maile,   Schwarz   und   Dipl.-Phys.
Dr. Schwengelbeck




BPatG 152
08.05

                                           -2-



beschlossen:


       1.      Das Bundespatentgericht ist für die Prüfung der am
               3. April 2012   erklärten   Teilung   der   Patentanmeldung
               11 2004 002 505.2-53 nicht zuständig.


       2.      Das aufgrund der Teilung durchzuführende Anmeldeverfahren wird zur weiteren Bearbeitung an das Deutsche Patentund Markenamt verwiesen.


       3.      Die Rechtsbeschwerde wird zugelassen.




                                      Gründe


                                            I.


Die Anmelderin hat am 19. Juni 2006 nach Einleitung der nationalen Phase der
internationalen Anmeldung PCT/US2004/043036 unter Inanspruchnahme des Prioritätstages der US-Anmeldung 10/745,527 vom 29. Dezember 2003 die Erteilung
eines Patents mit der Bezeichnung


       Entkoppeln der Anzahl der logischen Threads von der Anzahl der
       gleichzeitigen physischen Threads in einem Prozessor


beantragt.


Die ursprünglichen nebengeordneten Ansprüche 1, 19, 23 und 28 der insgesamt
36 Patentansprüche umfassenden Anmeldung lauten:


     1. Verfahren zum Managen von Threads, umfassend:

                                      -3-



Unterstützen einer Mehrzahl von logischen Threads mit einer Mehrzahl von gleichzeitigen physischen Threads.


19. Verfahren zur Unterstützung einer Mehrzahl von logischen
Threads mit einer Mehrzahl von gleichzeitigen physischen Threads,
umfassend:
Abbilden von mit einem ersten logischen Thread verknüpften Makroanweisungen auf einen NIP (nächster Anweisungszeiger) eines
gleichzeitigen physischen Threads;
Überwachen eines Prozessors auf ein Triggerereignis zu einer ersten
Zeit;
Halten des ersten logischen Threads in einem aktiven Zustand, bis
das Triggerereignis vorliegt;
Anhalten des Abbildens und Umschalten des ersten logischen
Threads in einen Drain-Zustand, wenn das Triggerereignis vorliegt;
Überwachen des ersten logischen Threads auf einen unterbrechbaren Punkt;
Halten des ersten logischen Threads im Drain-Zustand, bis der unterbrechbare Punkt angetroffen wird;
Schalten des ersten logischen Threads in einen Stillstandszustand,
wenn der unterbrechbare Punkt angetroffen wird;
Überwachen eines Prozessors auf ein Triggerereignis zu einer zweiten Zeit;
Halten des ersten logischen Threads im Stillstandszustand, bis das
Triggerereignis nicht vorliegt;
Schalten des ersten logischen Threads in einen Wartezustand, wenn
das Triggerereignis nicht vorliegt;
Überwachen der Mehrzahl von gleichzeitigen physischen Threads
auf einen verfügbaren physischen Thread;
Halten des ersten logischen Threads im Wartezustand, bis der verfügbare physische Thread angetroffen wird; und

                                      -4-



     Umschalten des ersten logischen Threads in den Wartezustand,
     wenn der verfügbare physische Thread angetroffen wird.


     23. Thread-Management-Architektur, umfassend:
     eine Zustandsmaschine zur Unterstützung einer Mehrzahl von logischen Threads mit einer Mehrzahl von gleichzeitigen physischen
     Threads durch Halten jeder der Mehrzahl von logischen Threads in
     einem Wartezustand, einem aktiven Zustand, einem Drain-Zustand
     und einem Stillstandszustand.


     28. Computersystem, umfassend:
     einen Direktzugriffsspeicher zum Speichern von Makroanweisungen;
     einen Systembus, der an den Speicher gekoppelt ist; und
     einen Prozessor, der an den Systembus gekoppelt ist, um die
     Makroanweisungen abzurufen, wobei der Prozessor eine Thread-Management-Architektur mit einer Zustandsmaschine aufweist, die
     zur Unterstützung einer Mehrzahl der den Makroanweisungen entsprechenden logischen Threads mit einer Mehrzahl von gleichzeitigen physischen Threads dient, indem jeder der Mehrzahl von logischen Threads in einem Wartezustand, einem aktiven Zustand, einem Drain-Zustand und einem Stillstandszustand gehalten wird.


Im Erteilungsverfahren hat die Anmelderin die Erteilung des Patents mit geänderten Ansprüchen laut dem am 12. September 2008 eingegangenen Schriftsatz vom
11. September 2008 gestellten Hauptantrag sowie einem hilfsweise in der Anhörung vom 23. Oktober 2009 eingereichten Anspruchssatz nach Hilfsantrag; der
sich in der vorderen Tasche der Verwaltungsakte des Patentamts befindet, beantragt. Die nebengeordneten geänderten Ansprüche 1 und 10 laut dem nunmehr
insgesamt 18 Ansprüche umfassenden Hauptantrages entsprechen dabei den ursprünglichen Ansprüchen 19 und 28. Anspruch 1 des Hilfsantrags ist ausweislich
des angefochtenen Beschlusses vor dem Wort "umfassend" um den Zusatz "wo-

                                       -5-



bei ein physischer Thread einen Next-Instruction-Pointer (NID) aufweist, der effektiv die Adresse der zu verarbeitenden Makroanweisung eines logischen Threads
darstellt" ergänzt.


Mit Beschluss vom 23. Oktober 2009 hat die Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts die Patentanmeldung mit der Begründung
zurückgewiesen, dass der Gegenstand des Anspruchs 1 sowohl in der Fassung
des Haupt- als auch in der Fassung des Hilfsantrags mangels erfinderischer Tätigkeit nicht patentfähig sei.


Gegen diesen ihren Verfahrensbevollmächtigten am 23. Dezember 2009 zugestellten Beschluss hat die Anmelderin mit beim Patentamt am 22. Januar 2010
eingegangenen Anwaltsschriftsatz vom 21. Januar 2010 Beschwerde eingelegt.


Mit Schriftsatz vom 3. April 2012 hat sie unter Zahlung der Gebühr nach § 39
Abs. 2 PatG die Teilung der Anmeldung erklärt, hierzu Anmeldeunterlagen eingereicht und nach Hinweis des Senats auf die Entscheidung des 21. Senats des
Bundespatentgerichts vom 7. Dezember 2010 (21 W (pat) 10/09, veröffentlicht in:
GRUR 2011, 949 - Teilung einer Patentanmeldung im Beschwerdeverfahren) sich
mit einer Verweisung der Teilanmeldung zur weiteren Bearbeitung an das Deutsche Patent- und Markenamt einverstanden erklärt.

                                       -6-



                                        II.


Die Teilanmeldung ist gemäß § 17 a Abs. 2 i. V. m. § 13 GVG, 39 Abs. 1 S. 3
PatG mangels funktioneller Zuständigkeit des Bundespatentgerichts an das Deutsche Patent- und Markenamt zu verweisen.


A.   Die nach Einlegung der Beschwerde erklärte Teilung der im Beschwerdeverfahren allein streitgegenständlichen Anmeldung mag zwar dazu geführt haben, dass die Teilanmeldung beim Bundespatentgericht anhängig geworden
     ist. Dieses ist aber für die Entscheidung über die Teilungsanmeldung unter
     keinem Gesichtspunkt zuständig.


     Weder die Anhängigkeit der Teilanmeldung noch die Tatsache, dass die Teilung nach Einlegung der Beschwerde erklärt wurde, führt dazu, dass das Gericht für die Prüfung der Teilungsanmeldung zuständig ist. Die gegenteilige
     Auffassung beruht auf der Annahme, dass es sich bei der Teilung nach § 39
     Abs. 1 PatG um einen der Prozesstrennung nach § 145 ZPO vergleichbaren
     Vorgang handelt (vgl. BGH GRUR 1999, 574 ff. - Mehrfachsteuersystem;
     GRUR 1998, 458, 460 - Textdatenwiedergabe). Wie der 21. Senat des Bundespatentgerichts aber in der von der Anmelderin genannten Entscheidung
     (BPatG [21. Senat] GRUR 2011, 949 - Teilung einer Patentanmeldung im
     Beschwerdeverfahren) im Einzelnen dargelegt hat, ist dies jedoch nicht der
     Fall. Danach entsteht bei einer Teilung nach § 39 PatG vielmehr ein neuer
     Verfahrensgegenstand, der im bisherigen Erteilungsverfahren bis zur Erklärung der Teilung keine Rolle gespielt hat. Dementsprechend fällt der Gegenstand der Teilungsanmeldung auch nicht in der Beschwerde an. Denn der
     Beurteilung durch das Beschwerdegericht unterliegt ein Rechtsschutzbegehren nur insoweit, als darüber in der Vorinstanz entschieden wurde. Nur in diesem Umfang kommt einer Beschwerde Devolutiveffekt zu (sog. Anfallwirkung). Sie ist das Mittel, um angegriffene Entscheidungen in der höheren gerichtlichen Instanz nachprüfen zu lassen. Entscheidend ist, dass das Rechts-

                                     -7-



     mittelgericht alleine über das prozessuale Schicksal des erstinstanziellen
     Streitgegenstandes entscheidet (vgl. Bay VGH NVwZ 2000, 210 f. m. w. N.).
     Demgegenüber ist die erstmalige Prüfung von Patentanmeldungen - wozu
     auch die Prüfung einer Teilanmeldung gehört - grundsätzlich Sache des
     Deutschen Patent- und Markenamts als Verwaltungsbehörde. Wegen der
     Einzelheiten wird zur Vermeidung von Wiederholungen auf den o. g. Beschluss des 21. Senats Bezug genommen, dem sich der erkennende Senat
     in vollem Umfang anschließt.


     Da es somit an einer funktionalen Zuständigkeit des Bundespatentgerichts
     zur Entscheidung über die Teilanmeldung mangelt, war diese daher durch
     Beschluss gemäß § 17 a Abs. 2 i. V. m. § 13 GVG, § 39 Abs. 1 S. 3 PatG an
     das Deutsche Patent- und Markenamt zu verweisen (vgl. BPatG, a. a. O.).


B.   Die Zulassung der Rechtsbeschwerde ist nach § 100 Abs. 2 Nr. 2 PatG erforderlich, da der Senat zwar mit der Rechtsprechung des 21. Senats des
     Bundespatentgericht übereinstimmt, hiermit aber von der bisherigen Rechtsprechung des Bundesgerichtshofs abweicht.




Höppler                   Maile              Schwarz           Schwengelbeck


                                                                               Hu
