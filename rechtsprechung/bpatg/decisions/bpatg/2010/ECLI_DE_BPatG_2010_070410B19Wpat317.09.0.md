---
ecli: "ECLI:DE:BPatG:2010:070410B19Wpat317.09.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 317/09"
decided: "2010-04-07"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2010&Sort=1&Seite=25&nr=16453&anz=1397&pos=384&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2010-04-07_19_W-pat_317_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0021.md", "germany/bund/acts/patg/0147.md"]
---

# Bundespatentgericht, 19 W (pat) 317/09 vom 2010-04-07

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 317/09                            Verkündet am
_______________                               7. April 2010
    (Aktenzeichen)                                 …




                      BESCHLUSS

                     In der Einspruchssache


…




BPatG 154
08.05

                                         -2-



…




                          betreffend das Patent 103 12 256


hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 7. April 2010 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Ing. Bertl,   der   Richterin   Kirschneck,   und   der   Richter
Dr.-Ing. Kaminski und Dr.-Ing. Scholz


beschlossen:


                       Das Patent 103 12 256 wird widerrufen.


                                      Gründe


                                           I


Das Deutsche Patent- und Markenamt hat für die am 19. März 2003 eingegangene Anmeldung ein Patent mit der Bezeichnung "Überwachungsverfahren für eine
Steuerung eines Spritzgießprozesses" erteilt, und die Patenterteilung am
28. Juli 2005 veröffentlicht.


Gegen das Patent haben die Firmen A… GmbH & Co. KG mit Schriftsatz vom
18. Oktober 2005, eingegangen am 19. Oktober 2005, und P…
… AG mit Schriftsatz vom 27. Oktober 2005, eingegangen per Fax am gleichen Tag, Einspruch erhoben. Zur Begründung haben sie vorgetragen, der Gegenstand des Patents sei nicht neu beziehungsweise beruhe unter Berücksichtigung des Standes der Technik nicht auf einer erfinderischen Tätigkeit.

                                         -3-



Die Einsprechenden stellen den Antrag,


        das Patent 103 12 256 in vollem Umfang zu widerrufen.


Die Patentinhaberin beantragt,


        das angegriffene Patent beschränkt mit folgenden Unterlagen aufrechtzuerhalten:
        Patentansprüche 1 bis 7, überreicht in der mündlichen Verhandlung,
        übrige Unterlagen wie erteilt.


Die Patentinhaberin tritt den Ausführungen der Einsprechenden in allen Punkten
entgegen und hält den Gegenstand des Streitpatents für patentfähig.


Wegen weiterer Einzelheiten wird auf den Akteninhalt verwiesen.


                                          II


Die gemäß § 147 Abs. 3 Nr. 1 PatG a. F. begründete Zuständigkeit des Bundespatentgerichts für die Entscheidung über die am 19. und 27. Oktober 2005 eingelegten Einsprüche besteht auch nach Aufhebung dieser Bestimmung zum
1. Juli 2006 (vgl. Art. 1 Nr. 17. u. Art. 8 des Gesetzes z. Änd. d. patentrechtl. Einspruchsverfahrens u. d. PatKostG v. 21. Juni 2006; BlPMZ 2006, 225, 226, 228)
nach dem allgemeinen verfahrensrechtlichen Grundsatz der "perpetuatio fori" fort
(vgl. u. a. BGH GRUR 2009, 184, 185 (Nr. 5) - Ventilsteuerung).


Die statthaften und auch sonst zulässigen Einsprüche haben Erfolg.

                                         -4-



1. Das Patent betrifft ein Überwachungsverfahren für eine Steuerung eines Spritzgiessprozesses, wobei Istwerte des Spritzgießprozesses erfasst und einem Rechner zugeführt werden. Die Patentschrift führt dazu aus, dass hierfür eine Vielzahl
von Software-Werkzeugen (Tools) erhältlich sei, die überlagert zu der Steuerung
einer Spritzgießmaschine eine Prozessüberwachung und -optimierung vornehmen. Jedes dieser Tools benötige als Eingangsdaten den zeitlichen Verlauf relevanter Prozessgrössen, z. B. des Druckes, der Geschwindigkeit, des Temperaturverlaufs usw. (vgl. Abs. 0004 der Streit-Patentschrift).


Der Patentschrift zu Folge laufen üblicherweise die Tools auf einer PC-Hardware
unter einem PC-Betriebssystem ab. Die Istwerte werden von eigenen Sensoren
erfasst und dem PC über eine entsprechende Peripheriebaugruppe zugeführt. Die
Prozesssignale werden also vom Rechner direkt an der Spritzgiessmaschine abgegriffen und als Messkurven im PC aufgezeichnet.


Hieraus ergibt sich die Aufgabe, die Istwerte dem Rechner auf einfachere, kostengünstigere und insbesondere auch universellere Art und Weise zuführen zu können (Abs. 0007).


Zur Lösung dieser Aufgabe wird eine Architektur mit einer echtzeitfähigen Steuerung vorgeschlagen die die Signale der Sensoren aufnimmt und an den Rechner (PC) mit nicht echtzeitfähigem Betriebssystem überträgt. Die Steuerung ist dabei gemäß dem in der Verhandlung vorgelegten, gültigen Anspruch 1 als Softwareprozess ausgebildet, der ebenfalls auf dem Rechner läuft.

                                         -5-



Der der geltende Anspruch 1 (mit einer für diesen Beschluss eingefügten Gliederung) beschreibt das wie folgt:


        1. "Betriebsverfahren für eine Steuerung (2) eines Spritzgiessprozesses und einen Rechner (16),


        a) wobei von der Steuerung (2) Istwerte (T, p, n, v) des Spritzgiessprozesses erfasst


        b) und an den Rechner (16) übermittelt werden,


        c) wobei die Istwerte (T, p, n, v) vom Rechner (16) unter einem


        c1) nicht echtzeitfähigen Betriebssystem entgegen genommen
            werden,


        d) wobei die Steuerung (2) als Softwareprozess (2) ausgebildet
            ist, der vom Rechner (16) unter einem echtzeitfähigen Betriebssystem quasiparallel zum Entgegennehmen der Istwerte (T, p, n, v) ausgeführt wird."


2. Für diesen Sachverhalt sieht der Senat einen Diplomingenieur (FH) der Fachrichtung Elektrotechnik oder Informatik mit Erfahrung in der Entwicklung von digitalen Steuerungssystemen als Fachmann.


3. Einzelne Merkmale des geltenden Anspruchs 1 bedürfen näherer Erläuterung:


Der geltende und der erteilte Anspruch 1 sind auf ein Betriebsverfahren gerichtet.
Im Unterschied dazu war der ursprüngliche Anspruch 1 auf ein Überwachungsverfahren gerichtet. Der Fachmann sieht diese Begriffe als gleichbedeutend.

                                        -6-



Der Begriff "echtzeitfähig" wird allgemein so verstanden, dass das Betriebssystem
bzw. das unter ihm laufende Programm in der Lage sein muss, die notwendigen
Rechenschritte dann durchzuführen, wenn sie gebraucht werden. Wie schnell das
im Einzelnen ist, richtet sich nach der jeweiligen Anforderung des Prozesses. Ein
nicht echtzeitfähiges Programm oder Betriebssystem hat diesbezüglich keine besonderen Anforderungen zu erfüllen. Als Beispiel für ein solches System ist in der
Patentschrift Absatz 0020 "Windows®" genannt.


Die "Steuerung" ist zwar in der Regel bei Spritzgießmaschinen ein eigenes in der
Spritzgießmaschine eingebautes System, das mit einem Leitrechner außerhalb
der Maschine verbunden sein kann. So ist das auch in dem Ausführungsbeispiel
nach Figur 1 der Patentschrift. Im nun beanspruchten Fall ist das aber anders: Die
Steuerung ist ein Softwareprozess, der auf dem Rechner 16 abläuft. Das ist in Figur 2 der Patentschrift dargestellt und in Absatz 0023 beschrieben. Ob der Rechner 16 dabei in die Maschine eingebaut oder außerhalb der Maschine angeordnet
ist, bleibt offen. Der Anspruch 1 ist auch nicht auf eine vollständige Integration von
Steuerung und Rechner beschränkt. Das wäre auch gar nicht ohne Weiteres realisierbar, denn Teile der Steuerung, wie die Sensoren, Aktoren, Wandler und Leistungsverstärker befinden sich regelmäßig außerhalb des Rechners.


Der Ausdruck "Quasiparallel" wird in dem in Absatz 0023 aufgezeigten Zusammenhang vom Fachmann als die nahezu gleichzeitige Aktivität zweier Betriebssysteme auf einem Rechner verstanden. Eine streng gleichzeitige Abarbeitung der
Rechenschritte zweier Betriebssysteme auf einem Prozessor ist nicht möglich. Die
von der Patentinhaberin dazu skizzierte wechselweise Aktivierung der beiden Betriebssysteme in kurzen Intervallen mit Vorrang des Echtzeitsystems erscheint
zwar grundsätzlich möglich, ist aber in der Patentschrift nicht offenbart. Der Fachmann muss deshalb fundierte Kenntnisse in der Erstellung und Arbeitsweise von
Betriebssystemen haben, die es ihm ermöglichen ein echtzeitfähiges und ein nicht
echtzeitfähiges Betriebssystem zeitgleich "quasiparallel" auf dem gleichen Rechner zu betreiben, wie es nun beansprucht ist.

                                        -7-



Wenn die Steuerung auf dem Rechner läuft, werden die Istwerte nach Merkmal b),
c) und c1) innerhalb des Rechners übertragen. Diese Merkmale haben nach Überzeugung des Senats deshalb insoweit keine technische Bedeutung mehr. Technisch wäre es zwar möglich den Betriebssystemen getrennte Speicherbereiche
zuzuordnen, und dann die Werte von einem Speicherbereich in den anderen zu
übertragen, aber dazu ist nichts offenbart.


4. Ob der Anspruch 1 unzulässig erweitert ist (§ 21 Abs. 1 Nr. 4 PatG), wie die
Einsprechende II behauptet, kann dahinstehen, da das dort beanspruchte Verfahren nicht auf einer erfinderischen Tätigkeit beruht (§ 1 Abs. 1 Nr. 1 i. V. m. § 4
PatG).


Die Firmenschriften "Arburg AQS: Online-Überwachung und Dokumentation der
Produktqualität", beziehungsweise "Arburg Quality Control AQC: Effiziente Prozessoptimierung, automatische Prozessüberwachung" der Arburg GmbH und Co.
tragen den Druckvermerk "52035_de_022000 Änderungen vorbehalten" beziehungsweise "AQC0397.TI D 04/98 Änderungen vorbehalten". Dem entnimmt der
Senat die Druckdaten Februar 2000 und April 1998. Der Senat hat die Originale
der Druckschriften in Augenschein genommen und sich davon überzeugt, dass es
sich um Firmenprospekte handelt, wie sie nach Art und Aufmachung regelmäßig
zur baldigen Verteilung vorgesehen sind. Der Senat hat keinen Zweifel daran,
dass dies auch geschehen ist, wie von der Einsprechenden I vorgetragen und von
der Patentinhaberin nicht bestritten wurde.


Die Firmenschrift "Arburg AQS: Online-Überwachung und Dokumentation der Produktqualität" beschreibt ein auf einem handelsüblichen PC unter Windows® lauffähiges Programmmodul mit dem Namen AQS zur Online-Überwachung einer
Spritzgießmaschine (Überschrift und 1. Absatz auf der 2. Seite sowie Kapitel
"Technische Daten Rechner Hardware" und "Betriebssysteme" auf der letzten Seite). Es werden bis zu acht ausgewählte, qualitätsrelevante Produktions- und
Spritzparameter zyklisch über die Maschinensteuerung erfasst, dem PC über ei-

                                       -8-



nen V.24 Maschinenanschluss übergeben und entsprechend vordefinierter Prüfplankriterien aufbereitet (S. 2, Sp. 1, Abs. 4., Sp. 3, Z. 11 bis 15, S. 3, re. Sp.,
Z. 15 bis 32).


Damit ist mit den Worten des Anspruchs 1 bekannt ein:


        1. "Betriebsverfahren für eine Steuerung (Maschinensteuerung)
            eines Spritzgießprozesses und einen Rechner (PC),


        a) wobei von der Steuerung Istwerte des Spritzgießprozesses erfasst


        b) und an den Rechner (über den V. 24 Maschinenanschluss)
            übermittelt werden,


        c) wobei die Istwerte vom Rechner (PC) unter einem


        c1) nicht echtzeitfähigen Betriebssystem (Windows®) entgegen
            genommen werden.


Im Unterschied zum Verfahren nach dem geltenden Anspruch 1, Merkmal d) ist
dort die Maschinensteuerung ein vom Rechner (PC) getrenntes, der Maschine zugehöriges System.


Die Firmenschrift "Arburg Quality Control AQC: effiziente Prozessoptimierung, automatische Prozessüberwachung" beschreibt ein weiteres Modul ACQ des gleichen Qualitätsüberwachungssystems, das auch zusammen mit dem Modul AQS
und einem Leitrechner ALS eingesetzt werden kann (le. S., re. Sp., Abs. 1). Dort
wird auch ausgeführt das dieses Modul mit reduziertem Funktionsumfang auch an
Maschinen mit SELOGICA Maschinensteuerung eingesetzt und mit diesem teilintegriert werden kann (letzte Seite, Kapitel "Kombinationsmöglichkeiten").

                                        -9-



Nach Überzeugung des Senats ist das für den Fachmann Anlass, die Teilintegration der ähnlichen Komponente AQS mit der Steuerung ebenfalls zu realisieren.
Die Kenntnisse des Fachmanns zur Realisierung eines quasiparallelen Betriebs
der beiden Systeme sind hier ebenso wie bei dem patentgemäßen Verfahren zu
unterstellen (siehe Punkt 3 dieses Beschlusses).


Damit kommt der Fachmann ohne erfinderische Tätigkeit, ausgehend von einem
Programmmodul AQS mit den Merkmalen a bis c1, zu einem Betriebsverfahren
bei dem nach Merkmal:


        d) "die Steuerung (SELOGICA) als Softwareprozess ausgebildet
            ist, der vom Rechner (Steuerrechner oder PC, auf dem die
            teilintegrierten Module AQS und SELOGICA laufen) unter einem echtzeitfähigen Betriebssystem (für die Steuerung betriebsnotwendig) quasiparallel zum Entgegennehmen der Istwerte (T, p, n, v) ausgeführt wird."


Der geltende Anspruch 1 ist damit nicht patentfähig; ebenso die auf ihn rückbezogenen Ansprüche 2 bis 7. Das angegriffene Patent war deshalb zu widerrufen
(§ 21 Abs. 1, Nr. 1 PatG).




Bertl              Kirschneck                 Dr. Kaminski             Dr. Scholz




                                                                              Pü
