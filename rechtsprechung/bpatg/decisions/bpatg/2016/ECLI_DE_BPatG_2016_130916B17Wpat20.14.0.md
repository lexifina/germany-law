---
ecli: "ECLI:DE:BPatG:2016:130916B17Wpat20.14.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 20/14"
decided: "2016-09-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2016&Sort=1&Seite=39&nr=28495&anz=906&pos=585&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2016-09-13_17_W-pat_20_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 20/14 vom 2016-09-13

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 20/14                                                      Verkündet am
_______________                                                     13. September 2016
    (Aktenzeichen)                                                          …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 11 2009 004 371.2


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 13. September 2016 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                      -2-



beschlossen:


                    Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                       I.


Die vorliegende Patentanmeldung geht hervor aus der internationalen Anmeldung
PCT/JP2009/065860, die am 10. September 2009 eingereicht wurde und die Priorität einer japanischen Patentanmeldung vom 15. Januar 2009 beansprucht. Sie
trägt in der deutschen Übersetzung die Bezeichnung


   „Kollisionsbestimmungsvorrichtung und Kollisionsbestimmungsprogramm“.


Die Prüfungsstelle hat die Patentanmeldung mit dem in der Anhörung am
26. Februar 2014 verkündeten Beschluss zurückgewiesen. Zur Begründung führt
sie aus, dass der Gegenstand des jeweiligen Patentanspruchs 8 des damals geltenden Hauptantrags und der damals geltenden Hilfsanträge 1 und 2 dem Patentschutz nicht zugänglich seien. Durch die Gegenstände dieser Ansprüche werde
kein technisches Problem mit technischen Mitteln gelöst, die über den bestimmungsgemäßen Einsatz einer Datenverarbeitungsanlage hinausgingen.


Gegen den Beschluss wendet sich die am 15. April 2014 eingegangene Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:

                                     -3-



       gemäß Hauptantrag mit
       Patentansprüchen 1 bis 8 vom 18. Juni 2014,
       Beschreibung Seiten 1 bis 17 und
       4 Blatt Zeichnungen mit Figuren 1, 2A, 2B, 3 und 4, jeweils vom
       13. Juli 2011;


       gemäß Hilfsantrag 1 mit
       Patentansprüchen 1 bis 8 vom 18. Juni 2014,
       im Übrigen wie Hauptantrag;


       gemäß Hilfsantrag 2 mit
       Patentansprüchen 1 bis 8 vom 18. Juni 2014,
       im Übrigen wie Hauptantrag;


       gemäß Hilfsantrag 3 mit
       Patentansprüchen 1 bis 6, überreicht in der mündlichen Verhandlung,
       im Übrigen wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist folgende
Druckschrift genannt worden:


       D1: DE 10 2006 059 829 A1.


Vom Senat wurden zusätzlich eingeführt:


       D2: US 6 714 213 B1

       D3: US 2004/0010346 A1

                                        -4-



         D4: Y. Huang, J.H. Oliver: “Integrated Simulation, Error Assessment, and
         Tool Path Correction for Five-Axis NC Milling”, Journal of Manufacturing
         Systems, Vol. 14, No. 5, pp. 331 – 344.


Der mit einer möglichen Gliederung versehene Patentanspruch 1 des Hauptantrags betrifft eine


         a) Kollisionsbestimmungsvorrichtung (100), Folgendes aufweisend:

         c) eine Formdatenspeichereinheit (102) zum Speichern sowohl von Voxelmodelldaten (106), die eine Form eines ersten Objekts durch ein Voxelmodell darstellen, als auch Umrissdarstellungsmodelldaten (107), die eine
         Form eines zweiten Objekts durch ein Umrissdarstellungsmodell darstellen, wobei das Voxelmodell durch ein Koordinatensystem deﬁniert ist, das
         am ersten Objekt festliegt, wobei das Umrissdarstellungsmodell durch ein
         Koordinatensystem definiert ist, das am zweiten Objekt festliegt;

         d) eine Zielzellenbezeichnungseinheit (101) zum Bezeichnen einer Zielzelle unter den das Voxelmodell bildenden Zellen, um eine Kollision zu bestimmen;

         e) eine Bestimmungstestpunktgenerierungseinheit (103) zum Generieren
         von Bestimmungstestpunkten, um eine Kollision für die Zielzelle zu bestimmen;

         f)   eine Raumkurvenerzeugungseinheit (104) zum Erzeugen einer räumlichen Kurve als Bahnkurve des Bestimmungstestpunkts, indem eine relative Starrkörperbewegung des ersten Objekts im Hinblick auf das zweite
         Objekt an jeden der Bestimmungstestpunkte angelegt wird;

         g) eine Kurvenüberschneidungsbestimmungseinheit (105) zum Bestimmen, ob jedes Umrisselement des Umrissdarstellungsmodells die räumliche Kurve schneidet oder nicht;

                                       -5-



        h) eine Abstandsberechnungseinheit (105) zum Berechnen des kürzesten Abstands von der räumlichen Kurve zu einer Umrissfläche des Umrissdarstellungsmodells, wenn ein durch die Kurvenüberschneidungsbestimmungseinheit bereitgestelltes Bestimmungsergebnis zeigt, dass die räumliche Kurve kein Umrisselement schneidet; und

        i)   eine Kollisionsbestimmungseinheit (101) zum Bestimmen auf Grundlage sowohl des von der Kurvenüberschneidungsbestimmungseinheit bereitgestellten Bestimmungsergebnisses als auch des von der Abstandsberechnungseinheit bereitgestellten Berechnungsergebnisses, ob die Möglichkeit einer Kollision zwischen beiden Objekten besteht.


Im Patentanspruch 1 des Hilfsantrags 1 ist gegenüber dem Anspruch 1 des Hauptantrags das Merkmal f) ersetzt durch


        f‘) eine Raumkurvenerzeugungseinheit (104) zum Erzeugen einer räumlichen Kurve als Bahnkurve für jeden Bestimmungstestpunkt durch Bewegen des Bestimmungstestpunkts auf Grundlage von eingelesenen Starrkörperbewegungsdaten (108), die für eine relative Bewegung des starren
        Körpers des ersten Objekts im Hinblick auf das zweite Objekt stehen;


Der ebenfalls mit einer möglichen Gliederung versehene Patentanspruch 1 des
Hilfsantrags 2 betrifft eine


        a) Kollisionsbestimmungsvorrichtung (100), Folgendes aufweisend:

        b) einen Eingang zum Einlesen von Starrkörperbewegungsdaten (108),
        die für eine relative Bewegung des starren Körpers eines ersten Objekts
        im Hinblick auf ein zweites Objekt stehen,

        c) eine Formdatenspeichereinheit (102) zum Speichern sowohl von Voxelmodelldaten (106), die eine Form des ersten Objekts durch ein Voxel-

                               -6-



modell darstellen, als auch Umrissdarstellungsmodelldaten (107), die eine
Form des zweiten Objekts durch ein Umrissdarstellungsmodell darstellen,
wobei das Voxelmodell durch ein Koordinatensystem definiert ist, das am
ersten Objekt festliegt, wobei das Umrissdarstellungsmodell durch ein
Koordinatensystem definiert ist, das am zweiten Objekt festliegt;

d) eine Zielzellenbezeichnungseinheit (101) zum Bezeichnen einer Zielzelle unter den das Voxelmodell bildenden Zellen, um eine Kollision zu bestimmen;

e) eine Bestimmungstestpunktgenerierungseinheit (103) zum Generieren
von Bestimmungstestpunkten, um eine Kollision für die Zielzelle zu bestimmen;

f‘‘) eine Raumkurvenerzeugungseinheit (104) zum Erzeugen einer räumlichen Kurve als Bahnkurve für jeden Bestimmungstestpunkts durch Bewegen des Bestimmungstestbunkts auf Grundlage der Starrkörperbewegungsdaten (108);

g) eine Kurvenüberschneidungsbestimmungseinheit (105) zum Bestimmen, ob jedes Umrisselement des Umrissdarstellungsmodells die räumliche Kurve schneidet oder nicht;

h) eine Abstandsberechnungseinheit (105) zum Berechnen des kürzesten Abstands von der räumlichen Kurve zu einer Umrissfläche des Umrissdarstellungsmodells, wenn ein durch die Kurvenüberschneidungsbestimmungseinheit bereitgestelltes Bestimmungsergebnis zeigt, dass die räumliche Kurve kein Umrisselement schneidet;

i)   eine Kollisionsbestimmungseinheit (101) zum Bestimmen auf Grundlage sowohl des von der Kurvenüberschneidungsbestimmungseinheit bereitgestellten Bestimmungsergebnisses als auch des von der Abstandsbe-

                                           -7-



       rechnungseinheit bereitgestellten Berechnungsergebnisses, ob die Möglichkeit einer Kollision zwischen beiden Objekten besteht; und

       j)     eine Ausgabeeinrichtung, die ein Ergebnis der Bestimmung der Möglichkeit einer Kollision ausgibt.


Im Patentanspruch 1 des Hilfsantrags 3 (mit Korrektur eines offensichtlichen Fehlers) ist an die Merkmale a) bis i) des Anspruchs 1 gemäß Hauptantrag angefügt,
dass


       k) die Voxelmodelldaten (106) unter Verwendung eines adaptiv erfassten
       Distanzfelds zum Darstellen einer Form auf Grundlage eines vorzeichenbehafteten Abstands von jedem Abtastpunkt zum Umriss einer Form des
       ersten Objekts dargestellt werden, wobei sich der Abtastpunkt auf jedem
       Rasterpunkt eines Raumunterteilungsrasters in einer Baumstruktur befindet,

       l)     die   Bestimmungstestpunktgenerierungseinheit (103)   als   Bestimmungstestpunkte Rasterpunkte [generiert], die sich an Ecken der Zielzelle
       befinden,

       m) die Kollisionsbestimmungseinheit (101) auf Grundlage des durch die
       Kurvenüberschneidungsbestimmungseinheit (105) bereitgestellten Bestimmungsergebnisses, des durch die Abstandsberechnungseinheit bereitgestellten Berechnungsergebnisses und der Distanzfeldwerte der Bestimmungstestpunkte bestimmt, ob eine Möglichkeit einer Kollision besteht,
       und

       n) wenn die Möglichkeit einer die Zielzelle betreffenden Kollision nicht
       bestimmt werden kann, die Zielzellbezeichnungseinheit eine Tochterzelle
       als neue Zielzelle bezeichnet.

                                       -8-



Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da die Gegenstände des jeweiligen Patentanspruchs 1 nach Hauptantrag sowie nach den Hilfsanträgen 1, 2 und 3 nicht auf
erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die Patentanmeldung betrifft Kollisionsbestimmung. Die Auftrittsmöglichkeit
oder Nichtauftrittsmöglichkeit einer Kollision zwischen Objekten soll bestimmt werden, die sich in einem zwei- oder dreidimensionalen Raum bewegen. Im Spezielleren soll eine Kollision zwischen einem mechanischen Bestandteil einer Werkzeugmaschine und einem Werkstück in einer Simulationsvorrichtung zum Simulieren
des Schneideprozesses in der Werkzeugmaschine bestimmt werden (deutsche
Übersetzung DE 11 2009 004 371 T5 Abs. [0001]).


Bei bekannten technischen Verfahren zum Erfassen einer Kollision zwischen bewegten Objekten wie dem kontinuierlichen Sweep-Verfahren oder dem diskreten
Zeitdivisionsverfahren träten Probleme auf, etwa im Hinblick auf die universelle
Anwendbarkeit für beliebige Bewegungen eines starren Körpers sowie hinsichtlich
der Gesamtspeichermenge (Abs. [0003] bis [0008]).


Auf dem Gebiet der Schneidprozesssimulation für Werkzeugmaschinen werde
z. B. ein Werkstück bei fortschreitender Bearbeitung in der Form verändert, wodurch es während des Prozesses kompliziertere Formen aufweise. So werde die
Form des Werkstücks oftmals durch ein Raumrastermodell wie etwa ein Voxel-Modell dargestellt, das keine Einschränkungen bezüglich der Phasenstruktur
habe. Jedoch habe die Verwendung des Raumrastermodells, um für die Kollisi-

                                       -9-



onsbestimmung etwa ein mechanisches Bauteil einer Werkzeugmaschine darzustellen, erhebliche Nachteile bei der zuvor erwähnten Speichermenge und sei
nicht praktisch (Abs. [0009]).


Der Patentanmeldung soll die Aufgabe zugrunde liegen, diese Probleme zu lösen
und eine Kollisionsbestimmungsvorrichtung und ein Kollisionsbestimmungsprogramm bereitzustellen, das die Notwendigkeit einer Bearbeitung bei hohem Rechenaufwand abschafft und Kollisionen bei hohen Geschwindigkeiten mit hoher
Zuverlässigkeit unter Einsatz einer reduzierten Datenspeichermenge bestimmen
kann, während die Möglichkeit gesenkt wird, dass Kollisionen versehentlich nicht
erfasst werden (Abs. [0010]).


Die Lehre der vorliegenden Anmeldung besteht im Wesentlichen in Folgendem:


Für die Kollisionsbestimmung zweier Objekte werden Daten der beiden Objekte
gespeichert, und zwar für das erste (bewegbare) Objekt Voxelmodelldaten, die
eine Form des ersten Objekts durch ein Voxelmodell darstellen, dessen Koordinatensystem am ersten Objekt festliegt, und für das zweite (ortsfeste) Objekt Umrissdarstellungsmodelldaten, die eine Form des zweiten Objekts durch ein Umrissdarstellungsmodell darstellen, dessen Koordinatensystem am zweiten Objekt festliegt (Merkmale a), c)). In einem Umrissdarstellungsmodell wird im Fall eines dreidimensionalen Objekts dessen Oberfläche durch eine Vielzahl von Flächen, Kannten und Ecken und deren Beziehungen zueinander dargestellt (Abs. [0020]). Das
Voxelmodell kann als adaptives Distanzfeld ausgebildet sein, in dem in einer
Baumstruktur (von grob zu fein) für Raumpunkte deren kürzeste Entfernung zum
Umriss der dargestellten Form (mit Vorzeichen) enthalten ist (Abs. [0021], Merkmal k)).
Unter den das Voxelmodell bildenden Zellen wird eine Zielzelle festgelegt, um eine
Kollision zu bestimmen (Merkmal d)). Als Zielzelle wird im Ausführungsbeispiel
gemäß Fig. 2A eine im Bereich der Oberfläche des ersten Objekts liegende
Zelle (202) gewählt.

                                         - 10 -



Sodann werden Bestimmungstestpunkte generiert, um eine Kollision für die Zielzelle zu bestimmen (Merkmal e)). Insbesondere können Eckpunkte (204, 205) der
Zielzelle als Bestimmungstestpunkte gewählt werden (Fig. 2B, Merkmal l)); diese
können aufgrund der Oberflächenlage der Zielzelle außerhalb (204) oder innerhalb
(205) des Objekts liegen.
Für jeden Bestimmungstestpunkt (204, 205) wird eine räumliche Bahnkurve (206,
207 in Fig. 2B) erzeugt, anhand einer (vorgegebenen) relativen Starrkörperbewegung des ersten Objekts im Hinblick auf das zweite Objekt (Merkmal f)). Die Starrkörperbewegung kann z. B. aus der Kombination einer Rotation und einer Translation über die Zeit bestehen, wodurch sich eine parametrierte Bahnkurve ergibt
(Abs. [0025]).
Es wird ermittelt, ob „jedes“ Umrisselement des Umrissdarstellungsmodells (des
zweiten Objekts) die räumliche Kurve schneidet oder nicht (Merkmal g)). Wie der
Fachmann (hier ein Informatik-Ingenieur mit Erfahrung auf dem Gebiet der computergestützten Simulation und Modellierung, insbesondere für Werkzeugmaschinen)
erkennt, ist damit gemeint, dass die Überschneidungsbestimmung für jedes Umrisselement des Umrissdarstellungsmodells durchgeführt wird bzw. dass bestimmt
wird, ob irgendeines der Umrisselemente die Kurve schneidet.
Falls die räumliche Kurve kein Umrisselement schneidet, wird der kürzeste Abstand von der räumlichen Kurve zu einer Umrissfläche des Umrissdarstellungsmodells berechnet (Merkmal h)).
Auf Grundlage sowohl der Überschneidungsbestimmung als auch der Abstandsberechnung einschließlich des Distanzfeldwerts wird in einer Kollisionsbestimmungseinheit (101) bestimmt, ob die Möglichkeit einer Kollision zwischen beiden
Objekten besteht (Merkmale i), m)), wobei ein Sicherheitsabstand einbezogen
werden kann, vgl. Abs. [0027], [0033].
Gemäß Fig. 3 und 4 mit Beschreibung wird das beschriebene Verfahren zunächst
in einer relativ groben Rasterung für im Oberflächenbereich des ersten Objekts liegende Zielzellen durchgeführt. Wenn für eine Zielzelle nicht festgestellt werden
kann, ob eine Kollision auftritt oder nicht, wird die Zielzelle unterteilt (in acht kleinere Zellen), und eine der durch die Teilung entstehenden Tochterzellen wird als

                                         - 11 -



neue Zielzelle bezeichnet (Merkmal n)). Mit den für eine Kollision in Frage kommenden Teilzellen als Zielzellen kann das Verfahren erneut durchlaufen werden.


Im Anspruch 1 des Hilfsantrags 1 ist in Merkmal f‘) klargestellt, dass die Bahnkurve für jeden Bestimmungstestpunkt durch Bewegen des Bestimmungstestpunkts auf Grundlage von eingelesenen Starrkörperbewegungsdaten berechnet
wird, die für eine relative Bewegung des starren Körpers des ersten Objekts im
Hinblick auf das zweite Objekt stehen.


Sinngemäß ist diese Ergänzung auch in den Merkmalen b) i. V. m. f‘‘) des Anspruchs 1 gemäß Hilfsantrag 2 enthalten. Zudem wird hier nach Merkmal j) das
Ergebnis in einer Ausgabeeinrichtung ausgegeben.


Da der Fachmann bereits bei Merkmal f) des Anspruchs 1 gemäß Hauptantrag
mitliest, dass die Starrkörperbewegung des ersten Objekts relativ zum zweiten
Objekt vorgegeben und somit zu irgendeinem Zeitpunkt von irgendwoher (z. B.
von einer Eingabeschnittstelle oder von einem anderen Softwaremodul) eingelesen werden muss, und er zudem bei Merkmal i) gedanklich ergänzt, dass das
Ergebnis der Kollisionsbestimmung irgendwohin (z. B. an einen Bildschirm) ausgegeben werden muss, geht der jeweilige Anspruch 1 der Hilfsanträge 1 und 2 inhaltlich nicht über den Anspruch 1 des Hauptantrags hinaus.


2.    Die Vorrichtung des Anspruchs 1 nach Hauptantrag und ebenso die Vorrichtungen des jeweiligen Anspruchs 1 nach den Hilfsanträgen 1 bis 3 sind nicht
patentfähig, da diese Vorrichtungen nicht auf erfinderischer Tätigkeit beruhen.


Aus der Druckschrift D1 ist ein Universalcomputer bekannt, in dem alle notwendigen Hardware- und Softwarekomponenten in einem Gehäuse vereinigt sind (Mikroprozessor, Hard-Disk, Arbeitsspeicher, Monitor, DVD/CD-Laufwerke, Tastatur
usw.), siehe die Zeichnung und die Bezugszeichenliste.

                                       - 12 -



D1 zeigt somit einen übliche Komponenten aufweisenden Computer, also eine
Vorrichtung, die für Berechnungen auf unterschiedlichsten Gebieten einsetzbar ist.


Bei der Beurteilung der erfinderischen Tätigkeit sind nur solche Anweisungen zu
berücksichtigen, welche die Lösung eines technischen Problems, das durch zumindest einen Teilaspekt der unter Schutz gestellte Lehre bewältigt wird, mit technischen Mitteln bestimmen oder beeinflussen; vgl. BGH GRUR 2011, 125 – Wiedergabe topografischer Informationen (m. w. N.).
Im Fall einer Datenverarbeitung verwendenden Lehre liegt gemäß der Entscheidung „Dynamische Dokumentengenerierung“ (BGH GRUR 2010, 613) die Lösung
eines technischen Problems mit technischen Mitteln vor, wenn eine der folgenden
Voraussetzungen erfüllt ist:
   -   Es werden Systemkomponenten modifiziert oder in neuartiger Weise adressiert, oder
   -   der Ablauf eines Datenverarbeitungsprogramms, das zur Lösung des Problems eingesetzt wird, wird durch technische Gegebenheiten außerhalb der
       Datenverarbeitungsanlage bestimmt, oder
   -   die Lösung besteht gerade darin, ein Datenverarbeitungsprogramm so auszugestalten, dass es auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt.


Nach diesen Kriterien tragen die über einen Computer mit üblichen Komponenten
(wie er etwa aus D1 bekannt ist) hinausgehenden Merkmale des Anspruchs 1
nach Hauptantrag und nach den Hilfsanträgen 1, 2 und 3 nicht zur Lösung eines
technischen Problems mit technischen Mitteln bei und sind daher bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen.


Welches technische Problem durch eine Erfindung gelöst wird, ist objektiv danach
zu bestimmen, was die Erfindung tatsächlich leistet (BGH GRUR 2005, 141 – Anbieten interaktiver Hilfe).

                                      - 13 -



Die beanspruchte Lehre leistet es, für als Datensätze in einem Computer gespeicherte, virtuelle Objekte, die sich entlang vorgegebener, im Computer gespeicherter Bahnen (ebenfalls virtuell) bewegen sollen, eine Kollisionsbestimmung durchzuführen, und löst damit ein entsprechendes Problem. Die Objekte und ebenso die
Bewegungen, die diese ausführen sollen, sind als Daten in einem Computer vorhanden. Einen Bezug auf reale Objekte oder reale Bewegungen enthält der Anspruch nicht. Die gesamte Kollisionsbestimmung für diese virtuellen Datenobjekte
einschließlich aller Berechnungsschritte wird ausschließlich im Computer durchgeführt. Für die einzelnen hierfür verwendeten Einheiten werden übliche Komponenten eines Computers wie Speicher und Prozessoren verwendet.
Die Kollisionsbestimmung selbst erschöpft sich in einer reinen Modellierung und
Simulation unter Zuhilfenahme mathematischer Methoden. Ein technisches Problem wird hierdurch nicht gelöst, es handelt sich vielmehr um ein reines Problem
der Datenverarbeitung ohne technischen Bezug; vgl. BGH GRUR 2011, 610
– Webseitenanzeige.


An dieser Feststellung vermögen auch die einzelnen Einheiten der beanspruchten
Vorrichtung nichts zu ändern. Diese tragen über die Verwendung üblicher Komponenten eines Computers hinaus nicht zur Lösung eines technischen Problems bei.


Dies gilt zum Einen für die Formdatenspeichereinheit (Merkmal c)), welche eine
übliche, technisch nicht näher ausgebildete Speichereinheit darstellt, in der spezielle Daten (Voxelmodelldaten und Umrissdarstellungsmodelldaten) gespeichert
sind. Die Art der gespeicherten Daten (siehe auch Merkmal k)) ist bedingt durch
den speziellen Kollisionsbestimmungsalgorithmus, der im Rahmen der Modellierung und Simulation verwendet wird und lediglich Probleme der Datenverarbeitung
löst. Einen Beitrag zur Lösung eines technischen Problems liefern weder dieser
Algorithmus noch die zu seiner Durchführung gespeicherten, speziellen Daten.


Auch der Eingang zum Einlesen von Daten und die Ausgabeeinheit (vgl. die Merkmale b) und j)) sind in technischer Hinsicht nicht speziell ausgebildet und stellen

                                      - 14 -



lediglich Komponenten eines üblichen Computers dar. Die durch sie eingelesenen
bzw. ausgegebenen Daten sind reine Modelldaten, ein Bezug zu realen Objekten
ist nicht erkennbar. Ein technisches Problem wird durch die Art der eingelesenen
bzw. ausgegebenen Daten nicht gelöst.


Entsprechendes gilt für die übrigen Einheiten des jeweiligen Anspruchs 1 gemäß
Hauptantrag und gemäß den Hilfsanträgen 1 und 2 (Zielzellenbezeichnungseinheit, Bestimmungstestpunktgenerierungseinheit, Raumkurvenerzeugungseinheit,
Kurvenüberschneidungsbestimmungseinheit, Abstandsberechnungseinheit, Kollisionsbestimmungseinheit), zu deren Ausbildung in technischer Hinsicht der Anmeldung nichts zu entnehmen ist. Aus dem Kontext heraus erkennt der Fachmann,
dass es sich hierbei um reine Softwaremodule handelt. Die durch diese Einheiten
ausgeführten Vorgänge sind reine Berechnungsschritte des zur Kollisionsbestimmung verwendeten Algorithmus ohne technischen Bezug. Auch hier ist kein Beitrag zur Lösung eines technischen Problems ersichtlich.


Im Anspruch 1 des Hilfsantrags 3 sind weitere Schritte des Modellierungsalgorithmus angegeben, die in den bereits erwähnten Einheiten durchgeführt werden.
Auch diese Schritte gehen nicht über reine Datenverarbeitung hinaus, ohne Bezug
zur realen Welt. Ein technisches Problem wird dadurch nicht gelöst.


Letztendlich verbleibt als Gegenstand des jeweiligen Patentanspruchs 1 gemäß
Hauptantrag und Hilfsantrag 1, 2 und 3 ein herkömmliches Datenverarbeitungssystem, auf dem ein Kollisionsberechnungsverfahren als Computerprogramm
implementiert ist, welches keine Lösung einer technischen Problemstellung zum
Inhalt hat.


Die Anmelderin bringt vor, die beanspruchte Vorrichtung skizziere einen Algorithmus, der zu Zeit- und Speicherplatzersparnis führe. Die verwendete Datenstruktur
(Baumstruktur, Hilfsantrag 3) trage hierzu bei. Zudem weist sie auf die Entschei-

                                       - 15 -



dung des Bundespatentgerichts 17 W (pat) 32/09 hin, der ein ähnlicher Sachverhalt zugrunde liege wie der vorliegenden Anmeldung.


Dieses Vorbringen konnte zu keiner anderen Beurteilung führen.


Der in der Anmeldung skizzierte Algorithmus stellt eine reine Maßnahme der
Datenverarbeitung dar und hat keinen technischen Hintergrund. Insbesondere
dient die Verwendung einer Baumstruktur allein einer effizienten Organisation von
Daten und löst allenfalls organisatorische Probleme. Eine möglicherweise durch
die Lehre der Anmeldung erreichte Zeit- und Speicherplatzersparnis beruht ausschließlich auf dem verwendeten Datenverarbeitungsalgorithmus. Dies kann nicht
als Lösung eines technischen Problems mit technischen Mitteln angesehen werden, nachdem in der gesamten Anmeldung weder eine besondere technische Ausgestaltung zu erkennen ist, etwa in Form einer speziellen verwendeten Hardware,
noch eine Rücksichtnahme auf spezielle Gegebenheiten der Datenverarbeitungsanlage, noch irgendein Bezug auf technische Gegebenheiten außerhalb der Datenverarbeitungsanlage, etwa in Form einer Verarbeitung von Messdaten oder
einer Auswirkung auf technische Gegebenheiten (z. B. auf die Bewegung einer
Werkzeugmaschine).


Auch die von der Anmelderin genannte Entscheidung 17 W (pat) 32/09 steht dieser Beurteilung nicht entgegen. Dort wurde ein Patent erteilt für ein Verfahren, mit
dem Messwerte ausgewertet wurden, wobei in den Messwerten spezielle Muster
(Lumen in einer anatomischen Struktur) segmentiert wurden. Im vorliegenden Fall
ist Derartiges nicht ersichtlich.


Damit sind diejenigen Merkmale des jeweiligen Anspruchs 1 gemäß Hauptantrag
und gemäß den Hilfsanträgen 1, 2 und 3 bei der Beurteilung der erfinderischen
Tätigkeit nicht zu berücksichtigen, welche über einen Computer mit üblichen Komponenten (wie er etwa in D1 ausgewiesen ist) hinausgehen.

                                            - 16 -



Der jeweilige Anspruch 1 des Hauptantrags und der Hilfsanträge 1, 2 und 3 ist
nicht gewährbar.


3.      Auch die übrigen Patentansprüche des Hauptantrags und der Hilfsanträge 1, 2 und 3 sind nicht gewährbar, da über einen Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120 „Elektrisches Speicherheizgerät“).




                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


     das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
        kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg
        abgelehnt war,
     einem Beteiligten das rechtliche Gehör versagt war,
     ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
        nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
        hat,
     der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
     der Beschluss nicht mit Gründen versehen ist.

                                         - 17 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                Eder               Dr. Thum-Rung                  Dr. Forkel




                                                                                     Fa
