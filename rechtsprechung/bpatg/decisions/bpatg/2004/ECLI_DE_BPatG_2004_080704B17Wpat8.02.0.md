---
ecli: "ECLI:DE:BPatG:2004:080704B17Wpat8.02.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 8/02"
decided: "2004-07-08"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=70&nr=19486&anz=2061&pos=1059&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-07-08_17_W-pat_8_02_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 8/02 vom 2004-07-08

## Entscheidung

BUNDESPATENTGERICHT



    17 W (pat) 8/02
_______________________

    (Aktenzeichen)




                              BESCHLUSS

                            In der Beschwerdesache


                 betreffend die Patentanmeldung 100 44 246.3-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts in
der Sitzung am 8. Juli 2004 unter Mitwirkung des Vorsitzenden Richters
Dipl.-Phys. Dr. Fritsch sowie der Richterin Eder und der Richter Dipl.-Ing. Bertl und
Dipl.-Ing. Prasch




BPatG 152
10.99

                                     -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluß der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 14. September 2001 aufgehoben und die Sache zur
       weiteren Prüfung an das Deutschen Patent- und Markenamt zurückverwiesen.


       Die Rückzahlung der Beschwerdegebühr wird angeordnet.


                                  Gründe


                                      I.


Die vorliegende Patentanmeldung mit der Bezeichnung


                  "Verfahren zum Verwalten von Meldungen"


wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts zurückgewiesen. In den Gründen ist ausgeführt, daß der Anmeldungsgegenstand nicht so deutlich und vollständig offenbart sei, daß ein Fachmann ihn
ausführen könne. Dies sei nur bei Kenntnis des Quellcodes eines zugehörigen
Programms möglich.


Gegen diesen Beschluß richtet sich die Beschwerde der Anmelderin.

                                        -3-



Der geltende Patentanspruch 1 lautet:


       "Verfahren zum Verwalten von Meldungen betreffend Betriebszustände einer Anzahl von Komponenten (OIN) eines Systems, bei
       welchem      von    einer   Meldungsverwaltung (ALA)     Meldungen (ALO,ALO') betreffend eines Komponenten-Betriebszustands
       verwaltet werden und eine Meldungsausgabe für zumindest einen
       Teil (ALO) der vorliegenden Meldungen veranlasst wird,
       dadurch gekennzeichnet,
       dass in einem anfänglichen Zustand (M1) aus einer Abfolge (TAB)
       von zumindest zwei Budgets das erste als gültiges Budget (B=1)
       ausgewählt wird,
       und in der Folge in Abhängigkeit von einer die Anzahl aller jener
       Meldungen (ALO), für die eine Meldungsausgabe erfolgt und hinsichtlich des betreffenden Komponenten-Betriebszustands gültig
       ist, beschreibenden Ausgabezahl bei jedem Hinzukommen zumindest einer Meldung die Meldungsausgabe (M1,M2,…,Mn) dieser
       Meldung(en) veranlasst wird, soweit die Ausgabezahl geringer ist
       als ein dem jeweils gültigen Budget (B) zugeordneter oberer
       Grenzwert (g1,g2,…,gn), jedoch die Meldungsausgabe dieser Meldung(en) unterbleibt (D1,…,Dm,Dn), solange dieser Wert erreicht
       oder überschritten ist,
       wobei der obere Grenzwert (g2,…) jedes nicht-ersten Budgets
       nicht kleiner ist als der obere Grenzwert (g1,…) des ihm vorangehenden Budgets,
       und bei Eintreten eines in Abhängigkeit von dem gültigen Budget (B) festgelegten Ereignisses (12,…,mn), welches zumindest
       darin besteht, dass die Ausgabezahl den oberen Grenzwert (g1,g2,…,gn) des gültigen Budgets erreicht und dem gültigen
       Budget in der Budget-Abfolge (zumindest) ein weiteres Budget

                                       -4-



        nachfolgt, anstelle des gültigen Budgets das nach diesem nächste
        als gültiges Budget ausgewählt wird."


Die Anmelderin weist mit Schriftsatz vom 11. Juli 2001 an das Deutsche Patentund Markenamt darauf hin, daß in der Beschreibungseinleitung ausdrücklich erwähnt wird, dass die in der Anmeldung behandelten Komponenten grundsätzlich
Hardware-mäßig oder Software-technisch realisiert sein könnten. Die Lehre stelle
auf die Verwaltung von Komponenten-Betriebszuständen betreffenden Meldungen
durch ein Meldungsverwaltungssystem ab und beziehe sich somit auf ein technisches Verfahren, das in einem technischen System eine technische Wirkung erreiche.


Die vorliegende Anmeldung sei auch nicht auf den Fall des Ausführungsbeispiels
eingeschränkt; so würde es eine unbillige Einschränkung bedeuten, in den Hauptanspruch Merkmale aufzunehmen, die lediglich für ein EWSD-System oder ein
Computerprogramm spezifisch seien.


Sie stellt den Antrag,


        den angefochtenen Beschluß aufzuheben.


                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie hat auch Erfolg, da den
Anmeldungsunterlagen eine technische Lehre zu entnehmen ist, die für den Fachmann auf dem Gebiet der elektronischen Datenverarbeitung nachvollziehbar ist.


Bei der vorliegenden Anmeldung geht es darum, auf Meldungen über Änderungen
der Betriebszustände von Komponenten eines Datenverarbeitungssystems, insbesondere eines EWSD-Systems in geeigneter Weise zu reagieren. Es sind insbesondere Ausfallsmeldungen, d.h. Alarme zu verwalten und auch anzuzeigen (Be-

                                       -5-



schreibung Seite 1, Zeilen 5 bis 20). Eine große Anzahl von Meldungen, z.B. bei
dem Ausfall einer Komponente, kann eine Zahl von weiteren Ausfällen nach sich
ziehen und weitere Ausfälle verursachen (Beschreibung Seite 2, Zeilen 22 bis 36).
Eine große Anzahl von Meldungen, die in einem Bereich gespeichert und bearbeitet werden, führt sonach zu Beeinträchtigungen der Verarbeitung (Beschreibung,
Seite 2, Zeilen 1 bis 20).


Der Fachmann, ein Ingenieur, der Datenverarbeitungssysteme, insbesondere für
Vermittlungsstellen entwickelt, entnimmt den Anmeldungsunterlagen folgende
Lehre zur Bewältigung dieser Problemstellung.


Die Verwaltung der Meldungen von den Rechnerkomponenten erfolgt an einer
zentralen Stelle des Datenverarbeitungssystems (Meldungsverwaltung ALA), bei
der die Betriebszustände einer Anzahl von Komponenten (OIN) dieses Systems,
als Meldungen (ALO, ALO’) und eine Meldungsausgabe für zumindest einen
Teil (ALO) der vorliegenden Meldungen veranlasst wird.


Im einzelnen wird dabei in einem Anfangszustand (M1) aus einer Abfolge (TAB)
von zumindest zwei Budgets (Speicherbereiche, in die die Meldungen eingeschrieben werden) das erste als gültiges Budget (B1) ausgewählt.


In der Folge wird bei jedem Hinzukommen zumindest einer Meldung die Meldungsausgabe (M1, M2, ... , Mn) dieser Meldung(en) veranlasst. Dies erfolgt in
Abhängigkeit von der Anzahl aller jener Meldungen (ALO), für die eine Meldungsausgabe erfolgen soll und die hinsichtlich des betreffenden Komponenten-Betriebszustandes gültig ist, solange die Ausgabezahl geringer ist als ein dem jeweils
gültigen Budget (B) zugeordneter oberer Grenzwert (g1, g2, ... , gn).

                                        -6-



Jedoch unterbleibt die Meldungsausgabe dieser Meldung(en) (D1, ... , Dm, Dn),
solange dieser Wert erreicht oder überschritten ist, wobei der obere Grenzwert
(g2, ...) jedes nicht-ersten Budgets nicht kleiner ist als der obere Grenzwert (g1,
...) des ihm vorangehenden Budgets.


Bei Eintreten eines in Abhängigkeit von dem gültigen Budget (B) festgelegten Ereignisses (12, ... ,mn), welches zumindest darin besteht, daß die Ausgabezahl den
oberen Grenzwert (g1, g2, ... , gn) des gültigen Budgets erreicht und dem gültigen
Budget in der Budget-Abfolge (zumindest) ein weiteres Budget nachfolgt, wird anstelle des gültigen Budgets das nach diesem nächste als gültiges Budget ausgewählt.


In analoger Anwendung der gefestigten Rechtsprechung des BGH ist hierin eine
klare technische Lehre zu sehen. Die Angaben in den Anmeldungsunterlagen setzen den Fachmann auf dem Gebiet der Datenverarbeitung in die Lage, das Prinzip
der Lehre nachzuvollziehen. Dabei braucht dem Fachmann im Patentanspruch
nicht in allen Einzelheiten vorgeschrieben werden, was er zu tun hat. Es wird als
ausreichend angesehen, wenn die Anmeldung dem Fachmann die entscheidende
Richtung angibt (BGH "Garmachverfahren", GRUR 1968, Heft 6, Seite 311, 313,
linke Spalte, Absatz 2).
Eine immer noch recht ungenaue Verhaltensregel kann als eine fertige Lehre zum
technischen Handeln anerkannt werden, sofern dem Fachmann der spezielle Lösungsweg ohne weiteres zu Gebote stand (BGH "Rohrdichtung", GRUR 1962,
Heft 2, Seite 80, 81, linke Spalte, Absatz 2), so daß der erstrebte Erfolg bei Einhaltung des angegebenen Lösungswegs unter Benutzung der vorhandenen Hilfsmittel in praktisch ausreichendem Maße erreicht werden kann (ebenda vorletzter Absatz).

                                       -7-



Beschränkt sich die Mitteilung der beanspruchten Lehre auf die Darstellung eines
(technischen) Prinzips, das der Fachmann aufgrund seines Fachkönnens zur Erreichung des angestrebten Erfolgs praktisch verwirklichen kann, dann ist es nicht
notwendig, ihm in der Anmeldung darüber hinaus weitere technische Einzelheiten
zu vermitteln, die ihm ohnedies schon zur Verfügung stehen (BGH "Isolierglasscheibenrandfugenfüllvorrichtung", GRUR 1984, Heft 4, Seite 272, 273, rechte
Spalte, Absatz 4).


Das Patentgesetz bietet sonach keine Grundlage dafür, die in einer Patentanmeldung enthaltene Lehre nur dann als ausreichend offenbart anzusehen, wenn eine
konkrete Ausführungsform in allen Einzelheiten angegeben ist.
Erst recht kann keine rechtliche Grundlage dafür erkannt werden, bei technischen
Erfindungen, die mit Mitteln der Datenverarbeitung realisiert werden, also computerimplementierten Erfindungen, die Angabe des Quellcodes als Voraussetzung
für eine ausreichende Offenbarung zu verlangen, wie dies von der Prüfungsstelle
gefordert und bspw in dem Aufsatz "Anforderungen an einen Patentschutz für
Computerprogramme" von Joachim Weyand und Heiko Haase (vgl GRUR 2004,
198) vertreten wird. Denn Gegenstand eines Patents ist regelmäßig nicht eine
konkrete Ausdrucksform einer Lehre, sondern ein (übergeordnetes) technisches
Prinzip. Ergibt sich dieses technische Prinzip für den Fachmann aus den Anmeldeunterlagen, so ist die Lehre ausreichend offenbart. Dass dem Fachmann zur Implementierung einer bestimmten technischen Lehre durch ein Computerprogramm
im Rahmen seines fachmännischen Handelns ein breiter Gestaltungsbereich zur
Verfügung steht, ändert hieran nichts und unterscheidet sich auch nicht von anderen Lehren, die nicht mit Mitteln der Datenverarbeitung implementiert werden.

                                       -8-



Den Schutz einer konkreten Ausdrucksform eines Computerprogramms, wie sie
der Quellcode darstellt, leistet bevorzugt das Urheberrecht, das auf Computerprogramme die für Sprachwerke geltenden Bestimmungen anwendet und den Schutz
von Ideen und Grundsätzen, mithin auch von technischen Lehren, die einem Computerprogramm ggf zugrunde liegen, ausdrücklich ausnimmt (vgl § 69a UrhRG).


Bei der vorliegenden Patentanmeldung wurde bisher noch nicht geprüft, ob die
Voraussetzungen für die Erteilung eines Patents erfüllt sind. Da das Patentamt damit noch nicht in der Sache selbst entschieden hat, war sie daher – auch um der
Anmelderin keine Tatsacheninstanz zu nehmen – zurückzuverweisen. Dabei wird
aus der Lehre, die sich aus den Unterlagen ergibt, ein entsprechendes Patentbegehren und eine konkrete technische Aufgabe zu formulieren sein.


Es wird die Rückzahlung der Beschwerdegebühr gemäß § 80 Abs 3 PatG aus Billigkeitsgründen angeordnet. Ursächlich für die Zurückweisung der Patentanmeldung war nämlich die Forderung der Prüfungsstelle, die relevanten Teile des
Quellcodes eines Programms zur Ausführung des Verfahrens nach dem Patentanspruch 1 vorzulegen, was weder durch die Amtspraxis noch durch die ständige
Rechtsprechung gerechtfertigt ist. Es wäre somit bei sachgerechter Behandlung
nicht zu dem Beschwerdeverfahren gekommen.




Dr. Fritsch                 Bertl                 Prasch                    Eder




                                                                               Pü
