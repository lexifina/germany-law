---
ecli: "ECLI:DE:BPatG:2017:170117B17Wpat49.14.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 49/14"
decided: "2017-01-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=1&nr=29008&anz=809&pos=27&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-01-17_17_W-pat_49_14_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 49/14 vom 2017-01-17

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 49/14                                                     Verkündet am
_______________                                                      17. Januar 2017
    (Aktenzeichen)                                                          …




                               BESCHLUSS

                             In der Beschwerdesache


               betreffend die Patentanmeldung 11 2008 003 486.9


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die     mündliche    Verhandlung   vom   17. Januar 2017   unter   Mitwirkung   des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                         -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G06T des Deutschen Patent- und Markenamts vom 21. Oktober 2014 aufgehoben und das Patent gemäß
       Hilfsantrag mit folgenden Unterlagen erteilt:


               Patentansprüche 1 bis 4 und
               Beschreibung Seiten 1 bis 3, 13, 23, jeweils überreicht in der
               mündlichen Verhandlung,


               Beschreibung Seiten 5 bis 12, 14 bis 22 und
               5 Blatt Zeichnungen mit Figuren 1, 2A bis C, 3,
               jeweils vom 23. Juni 2010.


       Im Übrigen wird die Beschwerde zurückgewiesen.




                                      Gründe


                                            I.


Die vorliegende Patentanmeldung geht hervor aus der internationalen Anmeldung
PCT/JP2008/073375, die am 24. Dezember 2008 eingereicht wurde und die Priorität einer japanischen Patentanmeldung vom 25. Dezember 2007 beansprucht. Sie
trägt in der deutschen Übersetzung die Bezeichnung


                      „Bewegungszustand-Schätzvorrichtung“.


Die Prüfungsstelle für Klasse G06T hat in der Anhörung am 21. Oktober 2014 die
Anmeldung zurückgewiesen, da die Gegenstände des jeweiligen Patentan-

                                        -3-



spruchs 1 gemäß Hauptantrag und gemäß den damals geltenden Hilfsanträgen 1,
2 und 3 mangels erfinderischer Tätigkeit nicht patentierbar seien.


Gegen den Beschluss wendet sich die am 27. November 2014 eingegangene
Beschwerde der Anmelderin.


Die Vertreter der Anmelderin stellten den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        gemäß Hauptantrag mit

        Patentansprüchen 1 bis 4 vom 27. November 2014,
        Beschreibung Seiten 1 bis 23 und
        5 Blatt Zeichnungen mit Figuren 1, 2A bis C, 3, jeweils vom
        23. Juni 2010;


        gemäß Hilfsantrag mit

        Patentansprüchen 1 bis 4, überreicht in der mündlichen Verhandlung,
        Beschreibung Seiten 1 bis 3, 13, 23, überreicht in der mündlichen
        Verhandlung,
        Seiten 5 bis 12, 14 bis 22 vom 23. Juni 2010,
        Zeichnungen mit Figuren wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: EP 1 431 120 A1 (Mitglied der Patentfamilie zu der in der Anmeldung
        genannten JP 2004-198211 A)

                                        -4-



        D2: K. Yamaguchi et al.: „Vehicle Ego-Motion Estimation and Moving
        Object Detection using a Monocular Camera“, 18th International Conference on Pattern Recognition (ICPR'06), IEEE 2006

        D3: C.G. Harris: „Determination of Ego-Motion from Matched Points“,
        Proceedings of the Third Alvey Vision Conference, 1987, pp. 189 – 192

        D4: M. Mählisch et al.: „Sensorfusion Using Spatio-Temporal Aligned
        Video and Lidar for Improved Vehicle Detection“, IEEE, Intelligent Vehicles
        Symposium 2006, June 13–15, 2006, Tokyo, Japan

        D5: N. Kaempchen et al.: „Feature-Level Fusion for Free-Form Object
        Tracking using Laserscanner and Video“, IEEE Proc. Intelligent Vehicles
        Symposium, 2005.


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 gemäß
Hauptantrag (mit Korrektur eines offensichtlichen Fehlers) betrifft eine


        Bewegungszustand-Schätzvorrichtung mit:

        a)   einem Kennzeichnungspunkt-Kandidaten-Extrahierteil (10), der eingerichtet ist zum Extrahieren von Kennzeichnungspunkt-Kandidaten in
        einem zu einem ersten Zeitpunkt (T1) von einem an einen sich bewegenden Körper (V1) montierten Bildgebungssensor (2) aufgenommenen Bild,

        b)   einem Positionsverhältnis-Gewinnungsteil (11), der eingerichtet ist,
        auf der Basis einer Ausgabe einer Distanzmesssensors (3), der an dem
        sich bewegenden Körper (V1) montiert ist, ein Positionsverhältnis einer
        aktuellen Position jedes Kennzeichnungspunkt-Kandidaten in Bezug auf
        den sich bewegenden Körper zu bestimmen,

        c)   einem Kennzeichnungspunkt-Auswählteil (12), der eingerichtet ist,
        auf Basis des Positionsverhältnisses einen Kennzeichnungspunkt-Kandidaten als einen Kennzeichnungspunkt auszuwählen, wobei das Positionsverhältnis eine Differenz von Distanzen zwischen jeder der aktuellen Posi-

                                         -5-



         tionen der Kennzeichnungspunkt-Kandidaten und dem sich bewegenden
         Körper, eine wie von dem sich bewegenden Körper aus gesehene Richtung der aktuellen Position des Kennzeichnungspunkt-Kandidaten oder
         eine Relativgeschwindigkeit der aktuellen Position des Kennzeichnungspunkt-Kandidaten in Bezug auf den sich bewegenden Körper aufweist,

         d)     einem Entsprechungspunkt-Extrahierteil (13), der eingerichtet [ist],
         um in einem von dem Bildgebungssensor (2) zu einem zweiten Zeitpunkt (T2) aufgenommenen Bild einen zu dem ausgewählten Kennzeichnungspunkt korrespondierenden Entsprechungspunkt zu extrahieren, und

         e)     einem Bewegungszustand-Schätzteil (14), der eingerichtet ist, um
         auf Basis der Koordinaten der ausgewählten Kennzeichnungspunkte und
         der Koordinaten der Entsprechungspunkte einen Bewegungszustand des
         sich bewegenden Körpers (V1) von dem ersten Zeitpunkt (T1) zu dem
         zweiten Zeitpunkt (T2) zu schätzen.


Der mit einer möglichen Gliederung versehene Patentanspruch 1 des Hilfsantrags
betrifft eine


         Bewegungszustand-Schätzvorrichtung mit:


         a)     einem Kennzeichnungspunkt-Kandidaten-Extrahierteil (10), der eingerichtet ist zum Extrahieren von Kennzeichnungspunkt-Kandidaten in
         einem zu einem ersten Zeitpunkt von einem an einem sich bewegenden
         Körper montierten Bildgebungssensor (2) aufgenommenen Bild,


         a1) wobei der Bildgebungssensor (2) zum Aufnehmen eines Bildes rund
         um den sich bewegenden Körper dient,


         f)     einem Distanzmesssensor (3) zum Gewinnen von Information bezüglich einer Relativposition zwischen einem Objekt rund um den sich bewe-

                              -6-



genden Körper und dem sich bewegenden Körper und zum Berechnen
der räumlichen Distanz oder der Richtung zwischen dem Objekt rund um
den sich bewegenden Körper und dem sich bewegenden Körper, und der
Relativgeschwindigkeit des Objektes in Bezug auf den sich bewegenden
Körper,


b1) einem Positionsverhältnis-Gewinnungsteil (11), der eingerichtet ist
zum Gewinnen eines relativen Positionsverhältnisses zwischen einer aktuellen Position jedes Kennzeichnungspunkt-Kandidaten und einer aktuellen
Position des sich bewegenden Körpers auf Basis einer vom Distanzmesssensor (3) gemessenen räumlichen Distanz zwischen einer aktuellen Position eines von dem Kennzeichnungspunkt-Kandidaten-Extrahierteil (10)
extrahierten Kennzeichnungspunkt-Kandidaten und dem Distanzmesssensor (3) oder auf Basis einer von dem Distanzmesssensor (3) gesehenen,
von einer aktuellen Position eines Kennzeichnungspunkt-Kandidaten in
Bezug auf den Distanzmesssensor (3) definierten Richtung, und auf Basis
einer Relativgeschwindigkeit einer aktuellen Position eines Kennzeichnungspunkt-Kandidaten in Bezug auf den Distanzmesssensor (3),
wobei der Positionsverhältnis-Gewinnungsteil (11) die räumliche Distanz
oder die aktuelle Richtung, und die Relativgeschwindigkeit, die für jeden
Kennzeichnungspunkt-Kandidaten erlangt wurden, in Relation zu dem
jeweiligen, von dem Kennzeichnungspunkt-Kandidaten-Extrahierteil (10)
gespeicherten Koordinatenwert jedes Kennzeichnungspunkt-Kandidaten
speichert,


c1) einem Kennzeichnungspunkt-Auswählteil (12), der eingerichtet ist,
um auf Basis des Positionsverhältnisses einen Kennzeichnungspunkt-Kandidaten als einen Kennzeichnungspunkt auszuwählen,

c11) wobei der Kennzeichnungspunkt-Auswählteil eingerichtet ist zum
Bestimmen ob der Kennzeichnungspunkt-Kandidat stationär ist oder nicht,
auf Basis der durch den Positionsverhältnis-Gewinnungsteil (11) erlangten

                               -7-



Relativgeschwindigkeit der aktuellen Position eines Kennzeichnungspunkt-Kandidaten in Bezug auf den Distanzmesssensor (3), und zum Auswählen des Kennzeichnungspunktes aus stationären Kennzeichnungspunkt-Kandidaten,

c12) wobei der Kennzeichnungspunkt-Auswählteil (12) auf Basis der
räumlichen Distanz, welche die Distanz zwischen der aktuellen Position
des Kennzeichnungspunkt-Kandidaten und dem Distanzmesssensor (3)
ist, den Kennzeichnungspunkt-Kandidaten, dessen räumliche Distanz die
kleinste oder größte unter den Kennzeichnungspunkt-Kandidaten ist, als
einen ersten Kennzeichnungspunkt unter mehreren Kennzeichnungspunkt-Kandidaten auswählt
und der Kennzeichnungspunkt-Auswählteil (12) als einen zweiten Kennzeichnungspunkt unter mehreren Kennzeichnungspunkt-Kandidaten denjenigen Kennzeichnungspunkt-Kandidaten auf Basis der räumlichen Distanz des ersten Kennzeichnungspunktes und der räumlichen Distanzen
anderer Kennzeichnungspunkt-Kandidaten auswählt, dessen Differenz
zwischen seiner räumlichen Distanz und der räumlichen Distanz des ersten Kennzeichnungspunktes die kleinste unter den Kennzeichnungspunkt-Kandidaten ist und größer als oder gleich wie ein vorbestimmter Wert ist,

oder wobei der Kennzeichnungspunkt-Auswählteil (12) auf Basis der aktuellen Richtung, welche die vom Distanzmesssensor (3) gesehene, von der
aktuellen Position des Kennzeichnungspunkt-Kandidaten in Bezug auf den
Distanzmesssensor (3) definierte Richtung ist, als den ersten Kennzeichnungspunkt den Kennzeichnungspunkt-Kandidaten auswählt, dessen
aktuelle Richtung in Bezug auf eine vorbestimmte Richtung die nächste an
einem vorbestimmten Winkel ist und größer als oder gleich wie ein vorbestimmter Winkel ist,
und der Kennzeichnungspunkt-Auswählteil (12) als einen zweiten Kennzeichnungspunkt unter mehreren Kennzeichnungspunkt-Kandidaten denjenigen Kennzeichnungspunkt-Kandidaten auf Basis der aktuellen Rich-

                                      -8-



       tung des ersten Kennzeichnungspunktes und der aktuellen Richtung
       anderer Kennzeichnungspunkt-Kandidaten auswählt, dessen Winkel zwischen seiner aktuellen Richtung und der aktuellen Richtung des ersten
       Kennzeichnungspunktes die kleinste unter den Kennzeichnungspunkt-Kandidaten ist und größer als oder gleich wie ein vorbestimmter Wert ist,

       c13) und wobei die übrigen Kennzeichnungspunkte in der gleichen Weise
       ausgewählt werden wie der zweite Kennzeichnungspunkt,


       d)    einem Entsprechungspunkt-Extrahierteil (13), der eingerichtet ist, um
       in einem von dem Bildgebungssensor zu einem zweiten Zeitpunkt aufgenommenen Bild einen zu dem ausgewählten Kennzeichnungspunkt korrespondierenden Entsprechungspunkt zu extrahieren, und


       e)    einem Bewegungszustand-Schätzteil (14), der eingerichtet ist, um
       auf Basis einer zweidimensionalen Koordinate des ausgewählten Kennzeichnungspunktes und einer zweidimensionalen Koordinate des Entsprechungspunktes einen Bewegungszustand des sich bewegenden Körpers
       von dem ersten Zeitpunkt zu dem zweiten Zeitpunkt zu schätzen.


Die Unteransprüche 2 bis 4 des Hilfsantrags lauten:


       „2.   Bewegungszustand-Schätzvorrichtung gemäß Anspruch 1, wobei
       eine Steuervorrichtung (1) für jeden ausgewählten Kennzeichnungspunkt
       ein Luminanzmuster derjenigen Pixelgruppe speichert, in der der Kennzeichnungspunkt existiert, so dass ein Entsprechungspunkt, welcher zu
       dem Kennzeichnungspunkt korrespondiert, aus einem nachfolgend aufgenommenen Bild extrahiert werden kann.


       3.    Bewegungszustand-Schätzvorrichtung gemäß Anspruch 2, wobei die
       Steuervorrichtung (1) dazu ausgelegt ist, durch Verwenden des Entsprechungspunkt-Extrahierteils (13) und mittels Abgleichens des Luminanz-

                                         -9-



        musters in einem beschränkten Bereich mit dem jeweiligen Luminanzmuster des Kennzeichnungspunktes ein Musterabgleichverfahren für jeden
        beschränkten Bereich des Bildes durchzuführen und das zentrale Pixel
        des übereinstimmenden Luminanzmusters als den Punkt zu extrahieren,
        welcher zu dem Kennzeichnungspunkt korrespondiert.


        4.   Bewegungszustand-Schätzvorrichtung gemäß Anspruch 1, wobei die
        Steuervorrichtung (1) dazu ausgelegt ist, durch Verwenden des Kennzeichnungspunkt-Auswählteils (12) und basierend auf der durch den Positionsverhältnis-Gewinnungsteil (11) erlangten aktuellen Position des Kennzeichnungspunkt-Kandidaten, der durch einen Geschwindigkeitssensor (4)
        ausgegebenen Geschwindigkeit des sich bewegenden Körpers und der
        durch einen Sensor (5) ausgegebenen Fahrtrichtung für jeden Kennzeichnungspunkt-Kandidaten zu bestimmen, ob die aktuelle Position des Kennzeichnungspunkt-Kandidaten stationär bleibt oder in Bewegung ist.“


Zu den weiteren Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat insoweit Erfolg, als ein Patent gemäß Hilfsantrag erteilt wird.


1.    Die Patentanmeldung betrifft eine Bewegungszustand-Schätzvorrichtung.


Der Patentanmeldung soll die Aufgabe zugrunde liegen, eine Bewegungszustand-Schätzvorrichtung bereitzustellen, welche eine genauere Schätzung eines Bewegungszustands eines sich bewegenden Körpers auf Basis von von einem an dem
sich bewegenden Körper montierten Bildgebungssensor aufgenommenen Bildern
erzielt (geltende Beschreibung S. 3 Abs. 1, DE 11 2008 003 486 T5 Abs. [0007]).

                                       - 10 -



Die Lehre der vorliegenden Anmeldung, für die mit dem Anspruch 1 des Hauptantrags Schutz begehrt wird, besteht im Wesentlichen in Folgendem:


Der Eigen-Bewegungszustand (Translation und Rotation) eines Fahrzeugs („sich
bewegender Körper“) soll geschätzt werden. Hierfür werden verschiedene am
Fahrzeug vorhandene Sensoren verwendet, insbesondere eine Kamera und ein
Distanzmesssensor. Die Kamera nimmt ein erstes Bild der Fahrzeugumgebung
und zu einem etwas späteren Zeitpunkt (an dem sich das Fahrzeug einschließlich
der Kamera bereits ein Stück weiter bewegt hat) ein zweites Bild der Fahrzeugumgebung auf. Im ersten Bild werden mehrere Kennzeichnungspunkte (z. B. Punkte
einer Fahrbahnmarkierung) bestimmt, und im zweiten (späteren) Bild werden die
den Kennzeichnungspunkten entsprechenden Punkte (Entsprechungspunkte) ermittelt. Anhand der Lage der Kennzeichnungspunkte und der Entsprechungspunkte wird der Bewegungszustand des Fahrzeugs (anhand der Abweichung in
Position und Orientierung der Kamera zwischen dem ersten und dem zweiten Bildaufnahmezeitpunkt) abgeschätzt.


Das bisher Erläuterte soll aus dem              Stand der Technik bekannt sein
(DE 11 2008 003 486 T5 Abs. [0002] bis [0005]).


Die Patentanmeldung behandelt das Problem, wie geeignete Kennzeichnungspunkte gefunden werden können.


Hierzu werden im ersten von der Kamera aufgenommenen Bild zunächst Kandidaten für die Kennzeichnungspunkte extrahiert (Merkmal a)). Für jeden Kandidatenpunkt wird mit Hilfe eines Entfernungssensors (Distanzmesssensors) ein Positionsverhältnis (Distanz des Punkts vom Fahrzeug und/oder Richtung des Punkts
vom Fahrzeug aus gesehen und/oder Relativgeschwindigkeit des Punkts im Vergleich zum Fahrzeug) ermittelt (Merkmale b), teilweise c)).
Abhängig vom Positionsverhältnis werden aus den Kandidatenpunkten geeignete
Kennzeichnungspunkte ausgewählt (restlicher Teil des Merkmals c)); z. B. werden

                                      - 11 -



diejenigen Kandidatenpunkte verworfen, die sich an bewegten Objekten befinden
(Fig. 2A mit Beschreibung), und es werden Kennzeichnungspunkte ausgewählt,
die sich in unterschiedlichen Entfernungen (Fig. 2B) und/oder in unterschiedlichen
Richtungen (Fig. 2C) in Bezug auf das Fahrzeug befinden.
Für die ausgewählten Kennzeichnungspunkte werden im zweiten Bild Entsprechungspunkte ermittelt, und anhand der Lage der Kennzeichnungspunkte und der
Entsprechungspunkte wird die Fahrzeugbewegung abgeschätzt (Merkmale d), e)).


In dem Anspruch 1 des Hilfsantrags ist konkretisiert, dass die Kamera ein Bild
rund um das Fahrzeug aufnimmt (Merkmal a1)), dass über den Distanzmesssensor für jeden Kandidatenpunkt das Positionsverhältnis ermittelt und gespeichert
wird, d. h. die räumliche Distanz oder die Richtung sowie die Relativgeschwindigkeit zwischen dem Fahrzeug selbst und einem in der Umgebung des Fahrzeugs
befindlichen Objekt, an dem der Kandidatenpunkt sitzt (Merkmale f), b1)).
Anhand der ermittelten Relativgeschwindigkeit wird bestimmt, ob ein Kandidatenpunkt stationär ist oder nicht; die Kennzeichnungspunkte werden nur aus stationären Kandidatenpunkten ausgewählt (Merkmal c11) i. V. m. c1)).
Zudem wird entweder als erster Kennzeichnungspunkt derjenige unter den Kandidatenpunkten ausgewählt, dessen räumliche Distanz zum Fahrzeug die kleinste
oder größte ist, und als zweiter Kennzeichnungspunkt derjenige unter den Kandidatenpunkten, dessen räumliche Distanz vom ersten Kennzeichnungspunkt die
kleinste, aber größer als ein vorbestimmter Wert ist, oder es wird als erster Kennzeichnungspunkt derjenige unter den Kandidatenpunkten ausgewählt, dessen
Richtung einer vorbestimmten Richtung am nächsten kommt und größer oder
gleich einem vorbestimmten Winkel ist, und als zweiter Kennzeichnungspunkt derjenige unter den Kandidatenpunkten, für den der Winkel zwischen seiner Richtung
und der Richtung des ersten Kennzeichnungspunkts der kleinste, aber größer als
oder gleich wie ein vorbestimmter Wert ist (Merkmal c12)).
Die übrigen Kennzeichnungspunkte werden dann jeweils in gleicher Weise ausgewählt wie der zweite Kennzeichnungspunkt (Merkmal c13)).

                                         - 12 -



Als Fachmann sieht der Senat hier einen Ingenieur der Informatik mit vertieften
Kenntnissen in der digitalen Bildverarbeitung und mit Erfahrung in der Entwicklung
von Fahrassistenzsystemen, insbesondere von Trackingsystemen einschließlich
Eigenbewegungsschätzsystemen an.


2.    Der Anspruch 1 nach Hauptantrag ist nicht patentfähig, da sein Gegenstand
über das in den ursprünglich eingereichten Unterlagen Offenbarte hinausgeht.


Dies betrifft insbesondere die Angabe in Merkmal c), wonach das Positionsverhältnis eine Differenz von Distanzen zwischen jeder aktuellen Position der Kennzeichnungspunkt-Kandidaten und dem sich bewegenden Körper sein kann.


Aus    dem      ursprünglichen    Anspruch 2      sowie    Abs.     [0009]     der
DE 11 2008 003 486 T5 geht hervor, dass das Positionsverhältnis eine Distanz
zwischen der aktuellen Position des Kennzeichnungspunkt-Kandidaten und dem
sich bewegenden Körper sein kann. Gemäß dem ursprünglichen Anspruch 4 werden Kennzeichnungspunkte so ausgewählt, dass eine Distanzdifferenz zwischen
einer aktuellen Position jedes Kennzeichnungspunkt-Kandidaten und dem sich
bewegenden Körper größer oder gleich wie ein vorbestimmter Wert ist, d. h. die
einzelnen Kennzeichnungspunkte um mehr als eine vorbestimmte Distanz voneinander entfernt sind; vgl. auch Abs. [0042] und [0048]. Dies gilt nur für die Auswahl mehrerer Kennzeichnungspunkte.


Die in Merkmal c) enthaltene Auswahl eines Kennzeichnungspunkts (der auch der
erste Kennzeichnungspunkt sein kann) anhand eines Positionsverhältnisses, das
eine Distanzdifferenz zwischen mehreren Kandidatenpunkten sein kann, ist den
ursprünglichen Unterlagen nicht zu entnehmen.


Auch die übrigen Patentansprüche des Hauptantrags sind nicht gewährbar, da
über einen Antrag nur einheitlich entschieden werden kann (BGH in GRUR 1997,
120 „Elektrisches Speicherheizgerät“).

                                       - 13 -



3.     Die Unterlagen des Hilfsantrags liegen im Rahmen der ursprünglichen
Offenbarung.


Der Anspruch 1 des Hilfsantrags geht hervor aus den ursprünglichen Ansprüchen 1, 2 und 3 sowie aus der DE 11 2008 003 486 T5 Abs. [0026], [0028], [0036],
[0037], [0038] und [0040] bis [0045] bzw. aus den entsprechenden Beschreibungsteilen in den ursprünglichen Unterlagen, in Verbindung mit Fig. 3.


Die Merkmale des Unteranspruchs 2 gehen zurück auf Abs. [0050] und [0066], die
des Unteranspruchs 3 auf Abs. [0068], und die des Unteranspruchs 4 auf Abs.
[0063] der DE 11 2008 003 486 T5, bzw. auf die jeweils entsprechenden Beschreibungsteile der ursprünglichen Unterlagen.


Alle Ansprüche sind somit ursprünglich offenbart.


Die ebenfalls zulässigen Änderungen in der Beschreibung betreffen teilweise die
Darlegung des Standes der Technik, teilweise ergeben sie sich aus den geänderten Ansprüchen.


4.     Die Vorrichtung gemäß dem Anspruch 1 des Hilfsantrags ist neu gegenüber
dem belegten Stand der Technik und beruht auf erfinderischer Tätigkeit.


Dies ergibt sich aus der Würdigung der zum Stand der Technik genannten Druckschriften und Unterlagen.


4.1.   Aus dem druckschriftlich belegten Stand der Technik war vor dem Anmeldetag der vorliegenden Patentanmeldung Folgendes bekannt:


Die Druckschrift D1 behandelt eine Vorrichtung, mit deren Hilfe die Umgebung
eines bewegten Körpers, insbesondere eines Fahrzeugs überwacht wird (Abstract
mit Figur). Mit einer am Fahrzeug befindlichen Kamera werden Bilder der Fahr-

                                     - 14 -



zeugumgebung aufgenommen, und in zwei nacheinander aufgenommenen Bildern werden mindestens vier Kennzeichnungspunkte („feature points“) verfolgt
und daraus die Positionsveränderung der Kamera (und damit des Fahrzeugs) zwischen der ersten und der zweiten Bildaufnahme abgeschätzt (Abstract, Abs.
[0017]). Hierfür ist gemäß Abs. [0054] eine Steuervorrichtung 10 vorgesehen mit
(unter anderem) einem Kennzeichnungspunkt-Extrahierteil FD (was eine Bestimmung von geeigneten Kandidatenpunkten voraussetzt), einem Kennzeichnungspunkt-Verfolgungsteil FT, das im zweiten Bild die den Kennzeichnungspunkten
entsprechenden Punkte (Entsprechungspunkte) detektiert (Abs. [0060]), und
einem Bewegungszustand-Schätzteil MS, das die Lage des Fahrzeugs am ersten
und am zweiten Bildaufnahmezeitpunkt und damit den Bewegungszustand schätzt
(Abs. [0061]). Der Bewegungszustand-Schätzteil erzeugt aus den zweidimensionalen Bildkoordinaten eines Kennzeichnungs- und eines Entsprechungspunktes (m1, m2) eine Homographie und schätzt damit die die Translation und Rotation
des Fahrzeugs ab (Abs. [0059], [0069] bis [0073], insbesondere [0072] i. V. m.
Fig. 8). Verfolgbare Kennzeichnungspunkte können anhand charakteristischer
Muster im Bild gefunden werden, z. B. an weißen Linien, Umrissen von Flecken
oder Schatten auf einer Straßenoberfläche, an Mauerflächen usw. (Abs. [0062]),
[0066]). Zur Verfolgung des Entsprechungspunkts in einem Folgebild wird der Entsprechungspunkt anhand der Korrespondenz zum Luminanzmuster ermittelt (Abs.
[0067] und [0068] mit Gl. (3)).
Die Verwendung eines Distanzmesssensors ist in D1 nicht ausgewiesen.


D2 zeigt die Schätzung der Eigenbewegung eine Fahrzeugs und zur Detektion
bewegter Objekte mit Hilfe einer am Fahrzeug befestigten monokularen Kamera
(Titel). Zur Schätzung der Eigenbewegung eines Fahrzeugs auf einer Straße werden Kennzeichnungspunkte verwendet, die nicht auf bewegten Objekten liegen
(Abstract). Bei der Extraktion geeigneter Kennzeichnungspunkte werden Punkte
auf (vorher gefundenen) bewegten Objekten eliminiert; außerdem wird das Bild in
unterschiedliche Regionen eingeteilt (Straße, Region mit niedrigen Objekten, Region mit höheren Objekten; Fig. 2), und aus jeder Region wird eine festgelegte

                                        - 15 -



Anzahl von Kennzeichnungspunkten extrahiert. Dadurch werden die Kennzeichnungspunkte einheitlicher über das Bild verteilt, und einige Punkte auf dem Fahrzeug werden entfernt (S. 2 re. Sp. unten, Fig. 3(a), (b)).


D3 betrifft die Bestimmung der Eigenbewegung einer Kamera aus korrespondierenden Punkten auf zwei Bildern. In der Praxis kommt es vor, dass ein Entsprechungspunkt nicht exakt seinem richtigen Ort zugeordnet wird, sondern einem Ort
in der Umgebung des richtigen Ortes. Um dadurch entstehende Fehler zu minimieren, wird ein iterativer Algorithmus verwendet, der auch eine Gewichtung vornimmt (Titel, Abstract, Kap. „Introduction“ und „Theory“). Gemäß D3 Kap. „Results“ Abs. 2 werden gute Resultate erzielt, wenn die Qualität der Daten gut ist;
hierzu gehört u. a., dass die Punkte sich hinreichend über den Raum erstrecken
(„if … the points adequately span the 3D space“).


D4 betrifft die Fusion von Daten mehrerer Sensoren, insbesondere eines Lidar-Entfernungsmessers und einer Videokamera, um Fahrzeugdetektion zu verbessern. Das Ausrichten der Sensoren erlaubt die Verwendung der Daten multipler
Sensoren in einem Detektions- und Verfolgungsnetzwerk (Titel, Abstract, S. 424
re. Sp. Abs. 2). Kap. III zeigt die Fahrzeugerkennung mittels mehrerer Sensoren.
Hierbei werden die einen örtlichen Bereich kennzeichnenden Daten des Abstandssensors in die Bilddatendomäne übertragen (S. 427 li. Sp. Abs. „A. Video data processing“, Fig. 8 mit rautenförmigen Markierungen der Abstandsbereiche). Bildbereiche („subwindows“), für die kein ausreichendes Entfernungssignal vorhanden
ist, werden von der weiteren Verarbeitung ausgeschlossen, so dass die Zielsuche
auf wenige Kandidatenbildbereiche beschränkt werden kann; zudem erlaubt das
Einbeziehen der gemessenen Entfernungen eine Einschränkung der Größe der
Kandidatenbildbereiche (S. 427 li. Sp. Kap. III.A. „Video data processing“). Die gefundenen Sichtmerkmale werden klassifiziert (S. 427 Abs. „B. Target classification“).

                                        - 16 -



D5 beschreibt die Fusion von Sensordaten (Laserscanner zur Entfernungsmessung, Videobilddaten), wobei niederschwellige Messmerkmale kombiniert werden
(Titel, Abstract). Auf S. 453 re. Sp. le. Abs. ist eine Beschränkung des Suchraums
im Videobild durch die Messergebnisse des Laserscanners angesprochen (vgl. D4
S. 427 li. Sp. Kap. III.A. „Video data processing“).


4.2.   Die Vorrichtung des Anspruchs 1 gemäß Hilfsantrag ist gegenüber diesem
Stand der Technik neu und beruht auf erfinderischer Tätigkeit.


Aus den Druckschriften D1, D2 und D3 sind Verfahren und Systeme zur Schätzung der Eigenbewegung eines Fahrzeugs bzw. einer am Fahrzeug vorhandenen
Kamera bekannt, die jedoch nur auf der Basis von zweidimensionalen Kamerabildern ohne Distanzsensoren arbeiten.
D4 und D5 zeigen die Fusion von Daten eines Distanzsensors mit Kameradaten,
wobei jedoch die Schätzung der Eigenbewegung eines Fahrzeugs nicht angesprochen ist.


Das Verfahren des Anspruchs 1 gemäß Hilfsantrag ist somit neu.


Der bisher bekannt gewordene Stand der Technik legt es auch nicht nahe, in einer
Vorrichtung zur Schätzung der Eigenbewegung eines bewegten Körpers, die sowohl Kameradaten als auch Daten eines Entfernungssensors verwendet, Kennzeichnungspunkte aus Kandidatenpunkten anhand ihrer räumlichen Distanzen
oder ihrer Raumrichtungen gemäß den Merkmalen c12) und c13) auszuwählen
derart, dass alle Kennzeichnungspunkte voneinander mindestens einen vorgegebenen Minimalabstand haben, oder dass sich die Richtungen aller Kennzeichnungspunkte relativ zu dem bewegten Körper mindestens um einen vorgegebenen
Minimalwinkel unterscheiden.
Gemäß D1 können verfolgbare Kennzeichnungspunkte anhand charakteristischer
Muster im Bild gefunden werden. D1 enthält jedoch keine Hinweise auf die Auswahl von Kennzeichnungspunkten aus einer Menge von Kandidatenpunkten.

                                      - 17 -



Aus D2 ist es bekannt, ein Kamerabild in mehrere Bereiche einzuteilen und aus
jedem Bereich eine Anzahl von Kennzeichnungspunkten auszuwählen. Wie
Fig. 3B der D2 zeigt, liegen die in den einzelnen Bereichen ausgewählten Kennzeichnungspunkte teilweise sehr dicht beieinander; die Berücksichtigung einer
Mindestabstands oder eines Mindestwinkelabstands legt D2 nicht nahe.
Der Hinweis in D3 (Kap. „Results“ Abs. 2) auf eine hinreichende Erstreckung von
Kennzeichnungspunkten über den Raum lässt eine Vielzahl von Gestaltungsmöglichkeiten für die Punktauswahl zu und kann die anmeldungsgemäße, spezielle
Auswahl mit Berücksichtigung eines Mindestabstands oder eines Mindestwinkelabstands ebenfalls nicht nahelegen.
Gemäß D4 werden Kandidatenbildbereiche, für die kein ausreichendes Entfernungssignal vorhanden ist, von der weiteren Verarbeitung ausgeschlossen; zudem
erlaubt das Einbeziehen der gemessenen Entfernungen eine Einschränkung der
Größe der Kandidatenbildbereiche (S. 427 li. Sp. Kap. III.A. „Video data processing“). Die spezielle anmeldungsgemäße Auswahl von Kennzeichnungspunkten
aus einer Menge von Kandidatenpunkten mit Berücksichtigung eines Mindestabstands oder eines Mindestwinkelabstands legt auch D4 nicht nahe.
D5 geht in Bezug auf die anmeldungsgemäße Einbeziehung von Abstandsdaten
nicht über D4 hinaus.


Ohne Hinweis und Anregung im Stand der Technik war die spezielle anmeldungsgemäße Auswahl von Kennzeichnungspunkten aus einer Menge von Kandidatenpunkten mit Berücksichtigung eines Mindestabstands oder eines Mindestwinkelabstands auch für den Fachmann nicht von sich aus naheliegend.


Damit ist dem Verfahren des Patentanspruchs 1 gemäß Hilfsantrag eine erfinderische Tätigkeit nicht abzusprechen.


5.    Der Patentanspruch 1 des Hilfsantrags ist gewährbar.

                                            - 18 -



Die abhängigen Patentansprüche 2 bis 4 des Hilfsantrags sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.




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


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                  Eder                Dr. Thum-Rung                 Dr. Forkel




                                                                                        Fa
