---
ecli: "ECLI:DE:BPatG:2015:101215B17Wpat13.13.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 13/13"
decided: "2015-12-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=54&nr=27758&anz=851&pos=814&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-12-10_17_W-pat_13_13_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 13/13 vom 2015-12-10

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 13/13                                                  Verkündet am
_______________                                                 10. Dezember 2015
    (Aktenzeichen)                                                      …




                             BESCHLUSS

                           In der Beschwerdesache


            betreffend die Patentanmeldung 11 2009 000 411.3 - 53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 10. Dezember 2015 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, des Richters
Dipl.-Ing. Baumgardt und des Richters Dipl.-Ing. Hoffmann


beschlossen:


                     Die Beschwerde wird zurückgewiesen.


BPatG 154
05.11

                                        -2-



                                     Gründe


                                         I.


Die vorliegende Patentanmeldung ist eine PCT-Anmeldung in nationaler Phase,
welche die Priorität zweier Voranmeldungen in den USA vom 20. Februar 2008
und 10. April 2008 in Anspruch nimmt und als WO 2009 / 105 594 A1 in englischer
Sprache veröffentlicht wurde. Ihr PCT-Anmeldetag ist der 20. Februar 2009. Sie
trägt in der deutschen Übersetzung (DE 11 2009 000 411 T5) die Bezeichnung


    „Verfahren und System zum Implementieren eines virtuellen Speicherpools
                          in einer virtuellen Umgebung“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts vom 13. November 2012 mit der Begründung
zurückgewiesen, dass der Gegenstand des Hauptanspruchs mangels erfinderischer Tätigkeit nicht gewährbar sei, weil er durch die Druckschrift D2 (s. u.) nahegelegt sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie reicht
ein geändertes Patentbegehren ein und führt aus, dass der nunmehr beanspruchte Gegenstand, ausgehend vom Stand der Technik gemäß einer der Druckschriften D1 bis D4, nicht nahegelegt sei.


Die Anmelderin stellt mit Eingabe vom 30. November 2015 (Seite 4) sinngemäß
den Antrag,


        den Beschluss der Prüfungsstelle vom 13. November 2012 aufzuheben und ein Patent auf der Grundlage der folgenden Unterlagen
        zu erteilen:

                                        -3-



        Patentansprüche 1 bis 15 vom 30. November 2015, eingegangen
        per Telefax am 1. Dezember 2015;
        (ggf. noch anpassbare) Beschreibung Seiten 1 bis 18 eingeg. am
        20. August 2010,
        sowie 6 Blatt Zeichnungen mit Figuren 1 bis 6, eingeg. am
        20. August 2010.


Der nunmehr geltende Hauptanspruch, hier mit einer möglichen Gliederung versehen, und mit einer redaktionellen Korrektur in Merkmal (b), lautet:


        (a)   Ein System zum Implementieren von verteilter nicht-flüchtiger Datenspeicherung, das folgende Merkmale umfasst:


        (b)   eine Mehrzahl von Virtualisierungsservern, von denen jeder
              verfügbaren nicht-flüchtigen Datenspeicherressourcen zugeordnet ist, und eine oder mehrere virtuelle Anwendungsmaschinen durch eine entsprechenden Virtualisierungsschicht
              unterstützt;


        (c)   eine Mehrzahl von virtuellen Speichermaschinen, von denen
              jede einem entsprechenden und teilnehmenden Virtualisierungsserver zugeordnet ist; und


        (d)   einen virtuellen Speicherpool, wobei jede virtuelle Speichermaschine den Export und die Ansammlung der verfügbaren
              nicht-flüchtigen Datenspeicherressourcen, die einem entsprechenden Virtualisierungsserver zugeordnet sind, in den
              virtuellen Speicherpool ermöglicht,


        (e)   wobei die virtuellen Speichermaschinen ausgelegt sind, um
              zusammenzuarbeiten, um den virtuellen Speicherpool ohne

                                         -4-



              externen gemeinsam verwendeten Speicher zu implementieren, und


        (f)   wobei der virtuelle Speicherpool virtuelle Volumen aufweist
              und Daten eines oder mehrerer der virtuellen Volumen zu
              einem anderen Volumen des virtuellen Speicherpools reproduziert sind.


Zu den selbständigen Ansprüchen 12 und 15 sowie den Unteransprüchen 2 bis 11
und 13, 14 wird auf die Akte verwiesen.


Eine konkrete Aufgabe ist weder in der Anmeldung noch im Laufe des Prüfungsverfahrens angegeben worden. Der Zurückweisungsbeschluss bezieht sich auf
Seite 1 Zeile 18 bis Seite 2 Zeile 12 der Beschreibung (eingegangen am 20. August 2010) und entnimmt dort als Aufgabenstellung, „eine unter einer virtuellen
Serverschicht liegende Serverspeicherung flexibel bezüglich Lokalität und Kapazität zu implementieren, ohne die Hinzufügung anderer externer Speichermechanismen“. Die nunmehr geltende Anspruchsfassung will ferner Sorge tragen, dass
Daten, die auf der Hardware eines ausgefallenen Virtualisierungsservers angeordnet sind, nicht verloren sind (siehe Eingabe vom 30. November 2015, Seite 2
Absatz 2).



                                          II.


Die frist- und formgerecht eingelegte Beschwerde ist zulässig. Sie bleibt jedoch
ohne Erfolg, weil das beanspruchte System zum Implementieren von verteilter
nicht-flüchtiger Datenspeicherung gemäß Patentanspruch 1 nicht auf einer erfinderischen Tätigkeit beruht (§ 4 PatG).

                                       -5-



1.     Die vorliegende Anmeldung betrifft die Implementierung eines virtuellen
Speicherpools für virtualisierte Programmausführungs-Umgebungen (siehe deutsche Übersetzung gemäß DE 11 2009 000 411 T5, insbesondere Absatz [0002]).


1.1    Nomenklatur


Ein „Virtualisierungsserver“ 110A, 110B … 110N ist ein realer Rechner (siehe
Absatz [0026]: PC, Notebook, Server, Großcomputer usw.) mit CPU 211, Speicher 212, Festplatte 214 (nicht-flüchtiger Speicher, auch als „Datenressourcen“
bezeichnet) und Netzwerkschnittstellenkarte (NIC) 213, über welche er mit anderen Virtualisierungsservern verbunden ist (siehe insbesondere Figur 1 / Figur 2
und die Absätze [0026], [0027]). Insoweit handelt es sich also um ein übliches
Rechner-Netzwerk, wobei diese Rechner jedoch eine (Betriebsprogramm-) Umgebung bereitstellen, in welcher „virtuelle Anwendungsmaschinen“ laufen können
(Absatz [0030]: „… virtuelle Umgebung 215, die durch eine Virtualisierungsschicht
(nicht gezeigt) unterstützt wird“).


Eine „virtuelle Anwendungsmaschine“ oder „virtuelle Maschine“ VAM 220, 231,
233… stellt einen virtuellen Rechner mit eigenem Betriebssystem, zugeordnetem
Speicher und Ressourcen dar, die ihr vom Virtualisierungsserver bereitgestellt
werden; dabei können auf einem „realen“ Rechner 110 eine (220) oder mehrere
(231, 233) VAM laufen (siehe Absatz [0030] / [0031]).


Nach der Lehre der Anmeldung läuft auf jedem Virtualisierungsserver zusätzlich
eine „virtuelle Speichermaschine“ 222A, 222B … 222N, welche eine eigene virtuelle Maschine darstellt, die die (nicht-flüchtigen) Datenressourcen 214 jedes Virtualisierungsservers verwaltet (Absatz [0032]). Die virtuellen Speichermaschinen 222A bis 222N kommunizieren über das Netzwerk (NIC 213, gestrichelte
Linien 261, 262, 263), um einen „virtuellen Speicherpool“ 250 zu bilden. Dadurch wird ein verteilter, für alle Virtualisierungsserver verfügbarer Speicher geschaffen (Absatz [0033] / [0034]).

                                       -6-



Dabei stellt der virtuelle Speicherpool 250 einen „Mechanismus zum Ansammeln
und Organisieren der Blockspeicherung, die von jedem Virtualisierungsserver …
exportiert wird, in eine kohärente virtuelle Speicherung“ dar (siehe Absatz [0037]).
D. h. dass jede virtuelle Speichermaschine den Speicher „ihres“ Virtualisierungsservers dem virtuellen Speicherpool 250 zur Verfügung stellt (im Patentanspruch 1, Merkmal (d): „den Export und die Ansammlung der verfügbaren nichtflüchtigen Datenspeicherressourcen … in den virtuellen Speicherpool ermöglicht“).


Innerhalb des virtuellen Speicherpools 250 können daraus dann „virtuelle Speichervolumen“ 250A bis 250X gebildet werden, auf die jeder Virtualisierungsserver zugreifen kann (siehe Absätze [0037] bis [0039] und Figur 2, durchgezogenen
Linien 271, 272 und 273).


1.2   Die Lehre der Anmeldung


Der Patentanspruch 1 ist auf ein System gerichtet, welches das Verfahren gemäß
Figur 6 ausführt und damit zum Implementieren von verteilter nicht-flüchtiger
Datenspeicherung (Merkmal (a)) ausgelegt ist. Ausgangspunkt ist eine Mehrzahl
von Virtualisierungsservern mit zugeordneten nicht-flüchtigen Datenspeicherressourcen, wobei auf den Virtualisierungsservern jeweils eine oder mehrere virtuelle
Anwendungsmaschinen laufen (Merkmal (b)).


Jedem Virtualisierungsserver ist eine virtuelle Speichermaschine zugeordnet
(Merkmal (c)), welche den Export der verfügbaren nicht-flüchtigen Datenspeicherressourcen in einen (gemeinsamen) virtuellen Speicherpool ermöglicht, wobei die
verfügbaren nicht-flüchtigen Datenspeicherressourcen in diesem virtuellen Speicherpool angesammelt werden (Merkmal (d)).


Die virtuellen Datenspeichermaschinen arbeiten zusammen, d. h. verwalten den
virtuellen Speicherpool als für alle Virtualisierungsserver gemeinsam verfügbare
Speicherressource (Teil von Merkmal (e)).

                                       -7-



Dadurch seien das sog. „Lokalitätsproblem“ und „Kapazitätsproblem“ (Absatz
[0003] / [0004] der DE 11 2009 000 411 T5) gelöst, dass die für einen Virtualisierungsserver verfügbare Speicherkapazität nicht auf die ihm unmittelbar zugeordneten Speicherressourcen beschränkt bleibt.


Zwar könnten beide Probleme bekannterweise durch „netzwerkbasierte Speicherung“ („NAS“ = network attached storage, oder „SAN“ = storage area network) verringert werden. Der Nachteil davon sei aber, dass es sich dabei um „zusätzliche
Komponenten“ handele, die „außerhalb“ lägen und von der Virtualisierungsumgebung unabhängig seien (Absatz [0003] / [0004]).


Sinngemäß lässt sich daraus bzw. aus Absatz [0005] der DE 11 2009 000 411 T5
die Aufgabe ableiten, die Begrenzung der Speicherkapazität auf die lokalen Ressourcen zu überwinden, ohne dafür separate, externe Speichergeräte einzusetzen.


Die Lösung besteht anspruchsgemäß darin, dass die virtuellen Speichermaschinen der Virtualisierungsserver zusammenarbeiten und die lokalen Speicher-Ressourcen als Teil eines „virtuellen Speicherpools“ für alle Virtualisierungsserver
bereitstellen (siehe die Merkmale (c), (d) und teilweise (e)). Dadurch kann auf
separate, externe Speichergeräte verzichtet werden (Rest von Merkmal (e)).


In dem virtuellen Speicherpool lassen sich virtuelle Speicher-Volumen einrichten,
wobei zum Schutz vor Datenverlust eine Reproduktion (vollständige Kopie) eines
oder mehrerer der virtuellen Volumen zu einem anderen Volumen des virtuellen
Speicherpools vorgesehen ist (Merkmal (f)).


Als Fachmann, dem die Aufgabe gestellt wird, in einer Virtualisierungsumgebung
die Speicher-Bereitstellung zu verbessern, ist ein Entwicklungsingenieur der Elektrotechnik oder ein Informatiker mit mehrjähriger Erfahrung in Speicherverwaltung
und Virtualisierungs-Programmierung anzusehen.

                                        -8-



2.    Das System zum Implementieren von verteilter nicht-flüchtiger Datenspeicherung gemäß dem geltenden Patentanspruch 1 ergab sich für den Fachmann
vor dem Prioritätszeitpunkt in naheliegender Weise aus dem Stand der Technik.


2.1   Von besonderer Bedeutung hierfür ist die Druckschrift


        D4   US 2006 / 75 199 A1.


Sie zeigt insbesondere im Ablaufdiagramm der Figur 12 eine Implementierung von
verteilter nicht-flüchtiger Datenspeicherung (Merkmal (a)), wobei unterschiedliche
Hardware-Konfigurationen zugrundeliegen können. Gemäß Figur 8 ist eine Mehrzahl von Virtualisierungsservern 802A, 802B … vorgesehen, von denen jeder verfügbaren nicht-flüchtigen Datenspeicherressourcen (storage disks 820A, 820B …)
zugeordnet ist, und eine oder mehrere virtuelle Anwendungsmaschinen (Figur 3:
306, 312 – siehe Absätze [0025], [0027]) durch eine entsprechenden Virtualisierungsschicht (z. B. 304) unterstützt (Merkmal (b)).


Gemäß Schritt 1202 der Figur 12 wird aus den lokalen Speicherressourcen ein virtueller Speicherpool gebildet, der im Schritt 1204 in virtuelle Speichervolumen aufgeteilt werden kann. Auf jedem Virtualisierungsserver läuft eine Virtualisierungssoftware („gatekeeper“), welche die virtuellen Speichervolumen verwaltet und insbesondere die Zuweisung der lokalen Ressourcen an den virtuellen Speicherpool
steuert (also „den Export und die Ansammlung … ermöglicht“, siehe Absätze
[0061], [0066], [0069] – wesentlicher Teil der Merkmale (c) und (d)). Während in
der Ausbildung gemäß Figur 2 die Speicherressourcen - im Gegensatz zur Anmeldung - aus einem externen, gemeinsam verwendeten Speicher (SAN) bestehen,
zeigt Figur 8 eine Ausbildung, bei der die „Gatekeeper“-Software für die Speicher-Virtualisierung auf allen einzelnen Servern läuft und zusammenarbeitet, um den
virtuellen Speicherpool nur aus dem jeweiligen lokalen Speicher, d. h. ohne externen gemeinsam verwendeten Speicher, zu implementieren (Merkmal (e)).

                                       -9-



Ferner enthält Absatz [0070] der D4 noch den Hinweis: „the method 1200 further
comprises mirroring the virtual storage volume across a plurality of storage devices (e.g. RAID1)“. Wie dem Fachmann vertraut ist (siehe z. B. den Auszug aus
der englischsprachigen Wikipedia vom 4. Februar 2008 zum Thema „Disk mirroring“: https://en.wikipedia.org/w/index.php?title=Disk_mirroring&oldid=189087627),
wird bei dieser Spiegelung („mirroring“) ein Speichervolumen vollständig auf ein
zweites Speichervolumen kopiert (i. d. R. um einem Datenverlust vorzubeugen).
Demnach weist auch der virtuelle Speicherpool der D4 virtuelle Volumen auf, und
Daten eines virtuellen Volumen sind zu einem anderen Volumen des virtuellen
Speicherpools reproduziert (Merkmal (f)).


Zwar beschreibt D4 nicht ausdrücklich „virtuelle Speichermaschinen“ auf den Virtualisierungsservern, die Gatekeeper-Software erfüllt aber deren Funktion in gleicher Weise (siehe Absatz [0069], z. B. „gatekeeper software resides in the virtual
machine monitor of each of the host computers…“).


2.2   Die dagegen gerichtete Argumentation der Anmelderin vermochte nicht zu
überzeugen.


Die Anmelderin hat vorgebracht, dass die Gatekeeper-Software der Druckschrift
D4 keine virtuelle Speichermaschine darstelle, wie sie in den unabhängigen Ansprüchen der vorliegenden Anmeldung definiert sei.


Dem ist entgegenzuhalten, dass im Patentanspruch 1 - wie auch in den übrigen
Ansprüchen - der Begriff „virtuelle Speichermaschine“ gar nicht weiter definiert
wird; es wird lediglich beansprucht, dass „… jede virtuelle Speichermaschine den
Export und die Ansammlung der verfügbaren nicht-flüchtigen Datenspeicherressourcen… in den virtuellen Speicherpool ermöglicht“ (Merkmal (d)), und dass „die
virtuellen Speichermaschinen ausgelegt sind, um zusammenzuarbeiten, um den
virtuellen Speicherpool ohne externen gemeinsam verwendeten Speicher zu implementieren“ (Merkmal (e)). Beides sind keine typischen Eigenschaften einer „vir-

                                        - 10 -



tuellen Speichermaschine“, sondern spezielle Maßnahmen nach der Lehre der
Anmeldung; die beiden Maßnahmen sind jedoch aus der Druckschrift D4 vorbekannt, dort allerdings ausgeführt von der beschriebenen „Gatekeeper“-Software.


Viel mehr zur Erläuterung des Begriffs „virtuelle Speichermaschine“ findet sich
auch in der Anmeldung nicht. In Absatz [0032] heißt es: „Die virtuelle Speichermaschine 222A ist ihre eigene virtuelle Maschine, die eine Anwendung ausführt, um
eine Schnittstelle zu bilden mit Datenressourcen 214, die durch den entsprechenden Virtualisierungsserver 110A verfügbar sind.“ Ferner „kommunizieren die virtuellen   Speichermaschinen     (z. B.   222A - N)    auf    jedem   Virtualisierungsserver 110A - N miteinander durch ein Kommunikationsnetzwerk (z. B. Netzwerk 120), um einen virtuellen Speicherpool 250 zu implementieren“ (Absatz
[0033]). Gemäß Absatz [0034] „sind die virtuellen Speichermaschinen als eine
Gruppe in der Lage, alle verfügbaren Datenressourcen zu kombinieren, die durch
die Virtualisierungsserver 110A - N präsentiert werden“. Letztlich wird somit die
„virtuelle Speichermaschine“ durch ihre Funktion definiert, eine Schnittstelle zu bilden für die Maßnahmen gemäß den Merkmalen (d) und (e).


All dieses leistet aber die in D4 beschriebene „Gatekeeper“-Software in gleicher
Weise, so dass kein signifikanter Unterschied zur Lehre der Anmeldung erkennbar
ist. Generell waren dem Fachmann vor dem Prioritätszeitpunkt verschiedene Arten
der Implementierung virtueller Speichervolumen, und ebenfalls deren jeweilige
Vor- und Nachteile bekannt (siehe z. B. den Auszug aus der englischsprachigen
Wikipedia    vom    24. Januar 2008      zum       Thema    „Storage    virtualization“:
https://en.wikipedia.org/w/index.php?title=Storage_virtualization&oldid=186628027
Abschnitt 5: „Implementation approaches“). Die Verwendung virtueller Maschinen
zur Implementierung eines virtuellen Speicherpools basierend auf den Speicher-Ressourcen mehrerer Virtualisierungs-Server ist ferner explizit in der im Prüfungsverfahren entgegengehaltenen Druckschrift D1 (DE 10 2006 032 832 A1) vorbeschrieben (siehe dort insbesondere Zusammenfassung / Figur 1, ferner die Absätze [0016] / [0017]). Die in der vorliegenden Anmeldung getroffene Auswahl einer

                                      - 11 -



geeigneten Implementationsform beruht sonach lediglich auf fachmännischem Abwägen bekannter Vor- und Nachteile, womit sich das Vorliegen einer erfinderischen Tätigkeit nicht begründen lässt (vgl. BGH GRUR 2006, 930 - Mikrotom).


Die Anmelderin hat noch eingewendet, dass die eine Verwendung virtueller Speichermaschinen beschreibende Druckschrift D1 sich auf flüchtigen Speicher (RAM)
beziehe und der Fachmann diese Lehre nicht ohne spezielle Veranlassung auf
Festplattenspeicher übertragen hätte. Zwar ist zuzustimmen, dass der Fachmann
grundsätzlich zwischen flüchtiger und nicht-flüchtiger Speicherung unterscheidet.
Die Lehre der D1 ist aber nicht ausdrücklich auf „flüchtigen“ Speicher bezogen, sie
besagt vielmehr ganz allgemein, „einen Teil des jeweiligen lokalen Speichers“ als
globalen virtuellen Speicherbereich zur Verfügung zu stellen (siehe Zusammenfassung, Absatz [0036]). Erst bei genauerem Studium erkennt man, dass die konkret
beschriebenen Ausführungsbeispiele wahrscheinlich von einem flüchtigen Speicher ausgehen. Eine derartige Einschränkung in Ausführungsbeispielen hätte den
Fachmann jedoch nicht gehindert, die Lehre als „allgemein“ zu verstehen. Irgendein technischer Grund, warum die Lehre der D1 nur für flüchtigen Speicher geeignet wäre, lässt sich der D1 jedenfalls nicht entnehmen.


Soweit die Anmelderin noch geltend macht, dass der Stand der Technik keinen
Hinweis in Richtung des zusätzlichen Merkmals (f) gebe, Daten eines oder mehrerer virtueller Volumen zu einem anderen Volumen „zu reproduzieren, d. h. zu replizieren“, kann dem unter Bezug auf D4 Absatz [0070] (s. o.) ebenfalls nicht gefolgt
werden.


3.    Mit dem nicht gewährbaren Patentanspruch 1 fallen auch die übrigen Ansprüche, weil über einen Antrag nur einheitlich entschieden werden kann.

                                       - 12 -



                              Rechtsmittelbelehrung

Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
      Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
      sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
      zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
      Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.



Dr. Morawek                 Eder                Baumgardt                 Hoffmann




                                                                                  Fa
