---
ecli: "ECLI:DE:BPatG:2001:180901B20Wpat16.00.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 16/00"
decided: "2001-09-18"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2001&Sort=1&Seite=86&nr=21169&anz=1792&pos=1291&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2001-09-18_20_W-pat_16_00_NA_0.txt"
---

# Bundespatentgericht, 20 W (pat) 16/00 vom 2001-09-18

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 16/00                                         Verkündet am
 _______________                                       18. September 2001
    (Aktenzeichen)                                              …




                          BESCHLUSS

                        In der Beschwerdesache


                     betreffend das Patent 44 38 793


…




BPatG 154
6.70

                                        -2-



hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 18. September 2001 durch den Vorsitzenden
Richter Dr. Anders sowie die Richter Dipl.-Ing. Obermayer, Dipl.-Phys. Kalkoff und
Dr. van Raden


beschlossen:


               Die Beschwerde wird zurückgewiesen.


                                     Gründe


                                         I.


Das Patentamt hat das Patent in vollem Umfang aufrechterhalten. Der Gegenstand des erteilten Anspruchs 1 sei gegenüber


                                 (1) EP 0 604 780 A1


neu und erfinderisch.


Dagegen wendet sich die Beschwerde der Einsprechenden. Sie stellt schriftsätzlich den Antrag,


          den angefochtenen Beschluß aufzuheben und das Patent zu
          widerrufen.


Die Patentinhaberin beantragt,


          die Beschwerde zurückzuweisen.

                                         -3-



Der Anspruch 1 lautet:


           "1.   Verfahren zum Erkennen eines manuellen Eingriffs an
                 Einrichtungen zum Einstellen von elektrischen Signalen
                 in Regieanlagen, insbesondere zum Einstellen der Verstärkung von Audiosignalen in Tonregieanlagen mittels
                 eines Stellgliedes (S), das zur Einstellung der gewünschten Signalveränderung entlang eines Stellweges
                 (SK) bewegbar ist, wobei die Bewegung des Stellgliedes (S) manuell oder automatisch erfolgt, dadurch gekennzeichnet, daß durch einen, Mikroprozessor (DSP)
                 die Position des Stellgliedes (S) festgestellt, die Abweichung von der Ruheposition sowie auch eine Abweichung von einer vorausberechneten Position in der
                 durch einen automatischen Betrieb hervorgerufenen
                 Bewegung des Stellgliedes (S) ermittelt und zum Erkennen einer Handbetätigung genutzt und diese Abweichung zwischen Ist- und Soll-Position des Stellgliedes
                 (S) als Kriterium zum Erkennen des Umschaltens auf
                 einen manuellen Betrieb gleich einem Sensor genutzt
                 wird."


Wegen des Wortlauts der Ansprüche 2 bis 12 wird auf die Streitpatentschrift verwiesen.


                                          II.


Der Anspruch 1 ist rechtsbeständig, sein Gegenstand patentfähig.


1. Die Erfindung gilt als neu.

                                        -4-



Dies ergibt sich bereits daraus, daß (1) nur die Bewegungsphase des Stellgliedes 10 der bekannten Vorrichtung anspricht (Sp 1 Z 7 bis 10, Sp 5, Z 40 bis 45).
Von einer Überwachung der Ruheposition ist keine Rede.


2. Die Erfindung gilt als auf einer erfinderischen Tätigkeit beruhend. Der Senat ist
nicht davon überzeugt, dass sich der Gegenstand am Anmeldetag in naheliegender Weise aus dem Stand der Technik ergab.


2.1 Der Senat sieht den Kern der Lehre in Folgendem:


Von einem Mikroprozessor wird die Lage des Stellgliedes festgestellt. Wenn es in
Ruhelage ist, wird die Abweichung von dieser Ruheposition ermittelt, wenn es sich
bewegt, um im automatischen Betrieb die vorausberechnete Lage einzunehmen,
so wird eine Abweichung von dieser vorausberechneten Position festgestellt. Die
jeweils erkannte Abweichung, d.h. die Abweichung zwischen Ist- und Sollposition
des Stellgliedes, wird zum Erkennen eines Handeingriffs benutzt, um daraufhin auf
den manuellen Betrieb umzuschalten.


2.2 Der Stand der Technik nach (1) beschreibt eine Vorrichtung zum Einstellen der
Verstärkung von elektrischen Signalen in Regieanlagen, bei denen die Verstärkung mittels eines Stellgliedes 10 eingestellt wird (Fig und Anspruch 1). Es wird
ein Weg aufgezeigt, wie ohne Zuhilfenahme eines gesonderten Sensors durch
Nutzung ohnehin bei der Vorrichtung bereits vorliegender Bauteile die Berührung
des Stellgliedes mit der Hand zu erkennen ist, indem nämlich die bei der Verstellung am Stellglied anfallende Kraft genutzt wird (Sp 1 Z 57 bis Sp 2 Z 13).


Zur Einstellung der gewünschten Signalveränderung wird das Stellglied 10 entlang
einem skalierten Stellweges 11 bewegt. Die Bewegung erfolgt manuell oder automatisch. Einem Mikroprozessor (µP) 15, der mit einem Zentralrechner 17 in Verbindung steht, wird durch eine Meldeleitung 13 über einen A/D-Wandler 14 die
Position des Stellgliedes mitgeteilt (Sp 3 Z 17 bis 23). Der µP 15 liefert über eine

                                       -5-



Steuerleitung 18 einen dynamisch errechneten, als "Soll-Strom" bezeichneten
Strom I0 (Sp 3 Z 44 bis Sp 4 Z 3) an einen Motor 20, der über eine Wirkverbindung 22 auf das Stellglied 10 einwirkt und dessen Position entlang dem Stellweg 11 verändert, dergestalt, daß es daraufhin die vom Zentralrechner 17 bestimmte Position einnimmt (Sp 3 Z 24 bis 32).


Über eine Meßleitung 23 und einen weiteren A/D-Wandler 25 wird dem µP 15 in
jeder Bewegungsphase des Stellgliedes der Ist-Strom des Motors 20 gemeldet, so
daß durch Vergleich von Soll- und Ist-Strom - allgemein (nach Anspruch 1) der am
Stellglied anfallenden Soll- und Ist-Kraft - vom µP 15 erkannt werden kann, ob ein
automatischer oder manueller Betrieb stattfindet, da bei Handbetrieb Ist- und Soll-Strom bzw. -Kraft voneinander abweichen. Diese Abweichung stellt der µP sofort
fest und schaltet vom automatischen Betrieb auf Handbetrieb um (Sp 4 Z 4 bis
23).


2.3 Der als Fachmann hier anzusetzende Elektroingenieur mit guten Kenntnissen
der Regelungstechnik mag ausgehend vom Stand der Technik nach (1) zwar erwägen, daß das dort beschriebene Verfahren zum Erkennen des Handeingriffs
nicht nur auf die Bewegungsphasen anwendbar ist, sondern auch bei Handeingriff
in eine Ruheposition vorgesehen werden kann. Weiter wird er sich routinemäßig
bemühen, die im Stand der Technik vorgegebene Erfassung der Kraft am Stellglied 10 bzw. des Ist-Stroms des Stellmotors 20 möglichst zu vereinfachen und für
die Krafterfassung andere Möglichkeiten als die Messung des Motorstroms in Betracht zu ziehen. Der Stand der Technik vermittelt aber keine Anregung dafür, zum
Erkennen eines Handeingriffs von der Erfassung der Stellkraft abzugehen und an
einer anderen Stelle im Regelkreis einzugreifen, und schon gar nicht dafür, daß
dies die Position des Stellgliedes sein könnte, im vorliegenden Regelkreis die Regelgröße.


Zwar weiß der Fachmann grundsätzlich, daß und wie die Regelgröße (hier Position des Stellgliedes 10) und die Stellgröße (hier Kraft am Stellglied 10 bzw. Strom

                                       -6-



im Stellmotor 20) in einem Regelkreis zusammenhängen. Dies bedeutet aber
nicht, daß der Fachmann in jedem Anwendungsfall Stellgröße und Regelgröße als
Alternativen in Betracht zieht. Denn im Gegensatz zur Stellkraft, deren Ist-Wert
beim Stand der Technik nach (1) ohne Handeingriff - bei Fehlen anderer Störungen - dem vom µP 15 dynamisch bestimmten "Soll-Wert" entspricht, ergibt sich für
die Ist- und Soll-Position des Stellgliedes eine andere Sachlage. Die Ist-Position
wird nämlich, solange das Stellglied im automatischen Betrieb bewegt wird, stets
von der vorausberechneten Soll-Position abweichen - unabhängig davon, ob ein
Handeingriff vorliegt oder nicht.


Die Erfindung beruht auf der Erkenntnis, dass gleichwohl die Abweichung zwischen Ist- und Soll-Position des Stellgliedes auch im automatischen Betrieb zum
Erkennen eines Handeingriffs genutzt werden kann. Damit geht die Erfindung über
den Gedanken des Stands der Technik, ohnehin im Regelkreis vorhandenen Bauelementen eine neue Funktion zu geben, noch einen Schritt hinaus: Einem ohnehin vorhandenen Meßwert, dem Ist-Wert des Stellgliedes, wird eine neue Funktion
zugewiesen; einer gesonderten Meßwerterfassung wie beim Stand der Technik
bedarf es nicht mehr.


Im Nachhinein - in Kenntnis der Erfindung - mag es sehr einfach aussehen, bei
der Abweichung der Meßgröße einzugreifen. Dies ist aber in der Einfachheit so
überzeugend, daß auch aus diesem Grunde für den Senat Zweifel übrig bleiben,
ob es für den Fachmann aufgrund seines Wissens und Könnens auf der Hand lag,
den vom Erfinder gewiesenen Weg zu gehen. Möglicherweise weitere Vereinfachungen im Bauelementeaufwand der Einstelleinrichtung nach (1) sind nicht so
schwerwiegend, daß dies ausreichend Anlaß wäre, von der bewährten bekannten
Methode abzuweichen und auf die im Patent vorgeschlagene Lösung zu verfallen.


2.4 Die Ansprüche 2 bis 12 haben gleichfalls Bestand. Die Vorrichtung nach Anspruch 8 ist sinngemäß aus den gleichen Gründen wie das Verfahren nach Anspruch 1 patentfähig. Im Anspruch 8 sind Vorrichtungsmerkmale korrespondierend

                                    -7-



zu sämtlichen Verfahrensmerkmalen des Anspruchs 1 enthalten und durch diese
umschrieben. Die Ansprüche 2 bis 7 und 9 bis 12 beziehen sich auf besondere
Ausführungsarten des Verfahrens und der Vorrichtung nach Anspruch 1 und 8.




Dr. Anders             Obermayer             Kalkoff            Dr. van Raden




                                                                             Ja
