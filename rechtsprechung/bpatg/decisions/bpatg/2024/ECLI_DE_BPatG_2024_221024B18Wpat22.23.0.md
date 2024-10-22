---
ecli: "ECLI:DE:BPatG:2024:221024B18Wpat22.23.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 22/23"
decided: "2024-10-22"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=21&nr=44332&anz=391&pos=323&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2024-10-22_18_W-pat_22_23_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 22/23 vom 2024-10-22

## Entscheidung

BUNDESPATENTGERICHT


18 W (pat) 22/23
_______________________

(Aktenzeichen)




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2015 007 145.9
…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts in der
mündlichen Verhandlung vom 22. Oktober 2024 durch den Vorsitzenden Richter
Dipl.-Phys. Dr. Morawek sowie die Richter Kätker, Dr.-Ing. Flaschke und der
Richterin kraft Auftrags Dipl.-Phys. Dr. Schenkl




ECLI:DE:BPatG:2024:221024B18Wpat22.23.0

                                      -2-



beschlossen:



       Auf die Beschwerde der Anmelderin wird der Beschluss der
       Prüfungsstelle für Klasse G 06 V des Deutschen Patent- und
       Markenamts vom 9. November 2022 aufgehoben und das Patent
       DE 10 2015 007 145 erteilt.

       Bezeichnung: Verfahren zur automatischen Fahrroutenbewertung

       Anmeldetag: 3. Juni 2015

       Der Erteilung liegen die folgenden Unterlagen zugrunde:

        - Patentansprüche 1 bis 7, überreicht in der mündlichen
           Verhandlung,

        - Beschreibung, Seiten 1 bis 17, überreicht in der mündlichen
           Verhandlung,

        - Zeichnungen, Figuren 1 bis 4, eingegangen am 3. Juni 2015.


                                     Gründe


                                       I.



Die vorliegende Patentanmeldung 10 2015 007 145.9 trägt die Bezeichnung

„Verfahren zur automatischen Fahrroutenbewertung“

und wurde am 3. Juni 2015 am Deutschen Patent- und Markenamt eingereicht. Mit
Beschluss vom 9. November 2022 hat die Prüfungsstelle für Klasse G 06 V des
Deutschen Patent- und Markenamts die Patentanmeldung in der Anhörung
zurückgewiesen. Die Prüfungsstelle hat ihren Zurückweisungsbeschluss sinngemäß damit begründet, dass die Gegenstände der damals geltenden jeweiligen

                                       -3-

Patentansprüche 1 nach Haupt- und Hilfsantrag nicht auf einer erfinderischen
Tätigkeit beruhten.

Dabei hat sie auf die folgende Druckschrift verwiesen:

  D2 DE 100 05 780 A1

Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.



Die weiteren Druckschriften aus dem Prüfungsverfahren sind

  D1 CH 176381 A,
  D3 DE 10 2009 005 259 A1,
  D4 DE 10 2007 037 329 A1,
  D5 Farabet C., [et al.]: Learning Hierarchical Features for Scene Labeling. In:
      IEEE Transactions on Pattern Analysis and Machine Intelligence, 2013,
      S.1915-1929.
  D6 Elias B.: Extraktion von Landmarken für die Navigation, Dissertation, 2006,
      S. 1 – 153, ISSN 0174-1454
  D7 Zheng Y.-T., [et al.] : GPSView: A Scenic Driving Route Planner. In: ACM
      Trans. Multimedia Computing, Communications and Applications, Vol. 9,
      2013, No. 1, S. 1-18.


Zudem hat der Senat noch die folgenden Druckschriften ermittelt:

  D8 Nagata, Daichi, [et al.] : SakuraSensor: A Participatory Sensing System for
      Detecting Flowering Cherries with Car-Mounted Smartphones. Poster auf der
      HotMobile 2015, Intern. Workshop on Mobile Computing Systems and
      Applications, 12-13.02.2015; URL:http://www.hotmobile.org/2015/papers/
      posters/Nagata.pdf [abgerufen am 03.07.2024]

  D9 OpenCV-Internetseite:       ABOUT;      URL:        https://web.archive.org/web/
      20150315004357/http://opencv.org/about.html [abgerufen am 04.07.2024]

                                             -4-

Die Anmelderin hat in der Verhandlung vom 22. Oktober 2024 den Antrag gestellt,
den angefochtenen Beschluss aufzuheben und das Patent mit folgenden
Unterlagen zu erteilen:

          - Patentansprüche 1 bis 7, eingereicht in der mündlichen
             Verhandlung,

          - Beschreibung, Seiten 1 bis 17, eingereicht in der mündlichen
             Verhandlung,

          - Zeichnung, Fig. 1 bis 4, eingegangen am 03.06.2015.



Der Patentanspruch 1 lautet:
1. Verfahren zum Auswerten eines optischen Erscheinungsbildes einer Fahrstrecke
(28, 29, 30), wobei
- aus zumindest einem Kraftfahrzeug (3), das auf der Fahrstrecke (28, 29, 30) fährt
oder gefahren ist, Videodaten (6), die eine Bildsequenz (13) der Fahrstrecke (28,
29, 30) enthalten, die über eine jeweilige Kommunikationsverbindung (7) an eine
Recheneinrichtung (4) übertragen werden, empfangen werden und
- durch eine Analyseeinrichtung (12) auf der Grundlage der Videodaten (6) zu
Bildern (14) der Bildsequenz (13) jeweils ein Übereinstimmungswert (15) betreffend
einen Grad einer Übereinstimmung des Bildes (14) mit einem vorbestimmten
Attraktivitätskriterium ermittelt wird und
- die Übereinstimmungswerte (15) der Bilder (14) zu einem Bewertungssignal (10)
für die Bildsequenz (13) kombiniert werden und
- das Bewertungssignal (10) als eine Beschreibung des Erscheinungsbildes der
Fahrstrecke (28, 29, 30) bereitgestellt wird und
- ein Maximalbereich (16) des Bewertungssignals (10) detektiert wird, in welchem
zumindest einer der Übereinstimmungswerte (15) des Bewertungssignals (10)
größer als ein vorbestimmter Schwellenwert (17) ist, und
- aus der Bildsequenz (13) zumindest ein zu dem Maximalbereich (16)
korrespondierendes Bild (14) der Bildsequenz (13) ermittelt und ausgegeben wird,
und

                                        -5-

- zu den Bildern (14) der Bildsequenz (13) jeweils ein anhand eines vorbestimmten
Qualitätsmaßes festgelegter Qualitätswert (18) einer optischen Qualität des Bildes
(14) erzeugt wird, wobei das Qualitätsmaß ein Signal-zu-Rausch-Verhältnis
und/oder eine Bildschärfe angibt, und
- die Qualitätswerte (18) zu einem Qualitätssignal (11) kombiniert werden und
- das zumindest eine korrespondierende Bild (14) aus dem Maximalbereich (16) in
Abhängigkeit von dem Qualitätssignal (11) ermittelt wird und wobei




- eine Abspieldauer desjenigen Teils der Bildsequenz (13), für welchen das
Bewertungssignal (10) den Maximalbereich (16) aufweist, ermittelt wird und
- in Abhängigkeit von der Abspieldauer entweder ein Videosignal oder nur ein
einzelnes Bild (14) ausgegeben wird,
wobei
- für eine Routenbewertung jedes Bewertungssignal (10), durch Bildung eines
Mittelwerts, zu einem einzigen Gesamtwert (31) zusammengefasst wird, um eine
kompakte Aussage zu einer Fahrstrecke zu erhalten, und
- der Gesamtwert (31) für eine Fahrstrecke und die extrahierten Bilder durch die
Recheneinrichtung (4) bereitgestellt werden und
- ein Navigationssystem (21) eines Fahrzeugs (5) und die Recheneinrichtung (4)
eine Kommunikationsverbindung (22) aufbauen und
- das Fahrzeug (5) die extrahierten Bilder und die Gesamtwerte aus der
Recheneinrichtung (4) bezieht und sie als Routenvorschau und Routenbewertung
grafisch an den Fahrer zurückgibt.

Wegen des Wortlauts der abhängigen Ansprüche 2 bis 7 und der weiteren
Einzelheiten wird auf die Akte verwiesen.


Die Beschwerdeführerin vertritt die Auffassung, dass die Ansprüche zulässig und
die Gegenstände der Ansprüche patentfähig sind.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                        -6-

                                          II.



Die zulässige Beschwerde hat in der Sache Erfolg. Sie führt zur Aufhebung des
angefochtenen Beschlusses und zur Erteilung des nachgesuchten Patents. Denn
der zweifelsfrei gewerblich anwendbare Gegenstand des nunmehr geltenden
Patentbegehrens ist gegenüber dem im Verfahren befindlichen Stand der Technik
neu und beruht auf einer erfinderischen Tätigkeit. Auch die weiteren Voraussetzungen zur Patenterteilung sind erfüllt (§§ 1 bis 5, § 34 und § 38 PatG).



1.   Die Patentanmeldung betrifft ein Verfahren zum Auswerten eines optischen
Erscheinungsbildes einer Fahrstrecke, wobei durch die Auswertung ermittelt wird,
ob die Fahrstrecke oder Teile der Fahrstrecke zum Beispiel landschaftlich
besonders schön sind oder architektonische Sehenswürdigkeiten aufweisen (vgl.
Offenlegungsschrift (OS), Abs. [0001]). In der Beschreibungseinleitung wird
ausgeführt, dass Verfahren bekannt seien, bei denen durch Kraftfahrzeuge
Videodaten mit Bildsequenzen von Fahrstrecken erzeugt würden. Die Videodaten
würden zentral in einem Server gesammelt und einem Benutzer angezeigt, wenn
sich dieser über eine Fahrstrecke informieren möchte. So sei es einem Fahrer
möglich, vor Antritt einer Fahrt einen Eindruck von verschiedenen Fahrrouten zu
gewinnen, die zu einem von ihm gewählten Ziel führten. Um eine Routenauswahl
automatisiert durchzuführen, müsse das Bildmaterial von der Route vorab von
Personen ausgewertet und kategorisiert werden, was eine subjektive Bewertung zur
Folge habe. Zudem sei der Aufwand der Sichtung bei einer großen Menge an
Videodaten wirtschaftlich nicht vertretbar (vgl. OS, Abs. [0002] bis [0007]).



2.   Ausgehend von diesem Hintergrund besteht das technische Problem darin,
ein optisches Erscheinungsbild von Fahrstrecken hinsichtlich eines Attraktivitätskriteriums automatisch auszuwerten, um eine systematische Suche einer Fahrroute
in Abhängigkeit von diesem zu ermöglichen (vgl. OS, Abs. [0008]). Zudem sollen
dem Benutzer eines Navigationssystems neben den Ergebnissen der Auswertung
auch aussagekräftige Videos oder einzelne Bilder, welche besonders repräsentativ

                                           -7-

in Bezug auf das Attraktivitätskriterium sind, bereitgestellt werden (vgl. OS, Abs.
[0020]).

Diese Aufgabe wird gelöst durch das Verfahren gemäß Patentanspruch 1, der
seitens des Senats mit einer Merkmalgliederung versehen wie folgt lautet:

 M1.1      Verfahren zum Auswerten eines optischen Erscheinungsbildes einer
           Fahrstrecke (28, 29, 30), wobei


 M1.2      - aus zumindest einem Kraftfahrzeug (3), das auf der Fahrstrecke (28, 29,
           30) fährt oder gefahren ist, Videodaten (6), die eine Bildsequenz (13) der
           Fahrstrecke    (28,   29,   30)    enthalten,   die   über    eine    jeweilige
           Kommunikationsverbindung (7) an eine Recheneinrichtung (4) übertragen
           werden, empfangen werden und
 M1.3      - durch eine Analyseeinrichtung (12) auf der Grundlage der Videodaten (6)
           zu Bildern (14) der Bildsequenz (13) jeweils ein Übereinstimmungs-wert
           (15) betreffend einen Grad einer Übereinstimmung des Bildes (14) mit
           einem vorbestimmten Attraktivitätskriterium ermittelt wird und
 M1.4      - die Übereinstimmungswerte (15) der Bilder (14) zu einem Bewertungssignal (10) für die Bildsequenz (13) kombiniert werden und
 M1.5      - das Bewertungssignal (10) als eine Beschreibung des Erscheinungsbildes der Fahrstrecke (28, 29, 30) bereitgestellt wird und
 M1.6      - ein Maximalbereich (16) des Bewertungssignals (10) detektiert wird, in
           welchem    zumindest    einer     der   Übereinstimmungswerte        (15)   des
           Bewertungssignals (10) größer als ein vorbestimmter Schwellenwert (17)
           ist, und
 M1.7      - aus der Bildsequenz (13) zumindest ein zu dem Maximalbereich (16)
           korrespondierendes Bild (14) der Bildsequenz (13) ermittelt und ausgegeben wird, und
 M1.8      - zu den Bildern (14) der Bildsequenz (13) jeweils ein anhand eines
           vorbestimmten Qualitätsmaßes festgelegter Qualitätswert (18) einer
           optischen Qualität des Bildes (14) erzeugt wird, wobei das Qualitätsmaß
           ein Signal-zu-Rausch-Verhältnis und/oder eine Bildschärfe angibt, und

                                     -8-

 M1.9   - die Qualitätswerte (18) zu einem Qualitätssignal (11) kombiniert werden
        und
 M1.10 - das zumindest eine korrespondierende Bild (14) aus dem Maximalbereich (16) in Abhängigkeit von dem Qualitätssignal (11) ermittelt wird
        und wobei
 M1.11 - eine Abspieldauer desjenigen Teils der Bildsequenz (13), für welchen
        das Bewertungssignal (10) den Maximalbereich (16) aufweist, ermittelt
        wird und
 M1.12 - in Abhängigkeit von der Abspieldauer entweder ein Videosignal oder nur
        ein einzelnes Bild (14) ausgegeben wird, wobei
 M1.13 - für eine Routenbewertung jedes Bewertungssignal (10), durch Bildung
        eines Mittelwerts, zu einem einzigen Gesamtwert (31) zusammengefasst
        wird, um eine kompakte Aussage zu einer Fahrstrecke zu erhalten, und
 M1.14 - der Gesamtwert (31) für eine Fahrstrecke und die extrahierten Bilder
        durch die Recheneinrichtung (4) bereitgestellt werden und
 M1.15 - ein Navigationssystem (21) eines Fahrzeugs (5) und die Recheneinrichtung (4) eine Kommunikationsverbindung (22) aufbauen und
 M1.16 - das Fahrzeug (5) die extrahierten Bilder und die Gesamtwerte aus der
        Recheneinrichtung (4) bezieht und
 M1.17 sie als Routenvorschau und Routenbewertung grafisch an den Fahrer
        zurückgibt.



3.   Der zuständige Fachmann ist ein Master of Science oder Diplomingenieur der
Fachrichtung Informationstechnik, der über mehrere Jahre Berufserfahrung in der
Bildverarbeitung und der Entwicklung von Navigationssystemen verfügt.

                                              -9-



4.    Die Merkmale des Patentanspruchs 1 bedürfen der Auslegung.
Das     Verfahren    zum     Auswerten        eines
optischen Erscheinungsbildes einer Fahrstrecke (M1.1) analysiert Videodaten (6),
welche von einem die Strecken fahrenden
Kraftfahrzeug (3) erfasst werden. Die Videodaten    enthalten    eine   Bildsequenz       der
Fahrstrecke. Die Daten werden entweder
bereits während der Fahrt oder im Anschluß
über eine Kommunikationsverbindung (7) an eine Recheneinrichtung (4) übertragen
(M1.2), in der die sich anschließende Analyse der Videodaten erfolgt (vgl. Fig. 1).




Wie in Figur 2 beispielhaft dargestellt, wird zunächst für jedes Bild (14) ein
Übereinstimmungswert (15) betreffend den Grad der Übereinstimmung mit einem
vorbestimmten       Attraktivitätskriterium    (C1)   ermittelt   (M1.3).   Die   einzelnen
Übereinstimmungswerte werden zu einem Bewertungssignal (10) für die
Bildsequenz kombiniert (M1.4) und dieses als Beschreibung des Erscheinungsbildes der Fahrstrecke bereitgestellt (M1.5). Ein Bewertungssignal (10) kann, wie in
Figur 2 gezeigt, eine Funktion über die Zeit, gemäß Abs. [0047] die Zuordnung eines

                                       - 10 -

Übereinstimmungswertes zu einem Bild (14) oder gemäß Abs. [0036] eine
Kombination von Übereinstimmungswerten sein.


Die sich anschließenden Schritte betreffen die Auswahl der aussagekräftigen,
repräsentativen Bilder:
Es wird ein Maximalbereich (16), in dem zumindest einer der Übereinstimmungswerte größer als ein vorbestimmter Schwellenwert (17) ist, detektiert (M1.6). Zu den
Bildern der Bildsequenz werden zudem anhand eines vorbestimmten Qualitätsmaßes, welches gemäß Merkmal M1.8 ein Signal-zu-Rausch-Verhältnis und/oder
eine Bildschärfe angibt, Qualitätswerte (18) erzeugt. Die Qualitätswerte (18) werden
zu einem Qualitätssignal (11) kombiniert (M1.9).


Abhängig vom Qualitätssignal wird zumindest ein korrespondierendes Bild aus dem
Maximalbereich ermittelt (vgl. M1.7, M1.10). Schließlich wird die Abspieldauer der
Bildsequenz des Maximalbereichs ermittelt, um als extrahierte Bilder entweder ein
Videosignal oder nur ein einzelnes Bild auszugeben (M1.11, M1.12). Gemäß
Beschreibung ergebe sich dadurch der Vorteil, dass keine unerwünscht kurzen
Videosignale präsentiert werden, die vom menschlichen Betrachter nicht mental
verarbeitet werden können. In diesem Fall sei es sinnvoller, ein Standbild bzw. ein
ruhendes Einzelbild bereitzustellen (vgl. OS, Abs. [0022]).
Für eine Routenbewertung wird jedes Bewertungssignal entlang der Fahrstrecke
durch Mittelwertbildung zu einem einzigen Gesamtwert (31) zusammengefasst
(M1.13), welcher dann zusammen mit den extrahierten Bildern (Videodaten oder
einzelnen Bildern) auf der Recheneinrichtung (4) bereitgestellt wird (M1.14). Von
dieser kann ein Navigationssystem (21) eines Fahrzeugs (5) über eine
Kommunikationsverbindung (M1.15) die extrahierten Bilder und Gesamtwerte
beziehen (M1.16) und sie als Routenvorschau und Routenbewertung grafisch an
den Fahrer zurückgeben (M.17).

                                                - 11 -

5.    Die Änderungen im Patentanspruch 1 sind zulässig (§ 38 PatG).

Die   Merkmale     des   Patentanspruchs 1                sind   durch       die   ursprünglichen
Patentansprüche 1, 5, 6, 7 und 8 sowie die ursprünglich eingereichte Beschreibung
(vgl. OS, Abs. [0021], [0034], [0040], [0049], [0051], [0054]) und Figur 4 als zur
Erfindung zugehörend offenbart.

Auch die weiteren Patentansprüche beinhalten keine unzulässige Änderung. Die
Beschreibung wurde entsprechend angepasst.



6.     Alle Merkmale des Patentanspruchs 1 sind bei der Prüfung der
Patentfähigkeit zu berücksichtigen (§ 1 PatG).

Entgegen der Auffassung der Prüfungsstelle stellen die Merkmale M7 bis M10
technische Merkmale dar, die bei der Beurteilung der Neuheit und der
erfinderischen   Tätigkeit      zu      berücksichtigen      sind.     Der     Gegenstand    des
Patentanspruchs      1       betrifft     ein      Verfahren,        bei     dem     über    eine
Kommunikationsverbindung             übermittelte        Videodaten        nach    vorbestimmten
Attraktivitätskriterien ausgewertet werden. In Abhängigkeit von der Auswertung und
dem Kriterium der optischen Bildqualität wird ein entsprechend repräsentativer
Videoausschnitt ausgewählt, der dem Benutzer des Navigationssystems bereitgestellt wird. Das mit diesen technischen Mitteln gelöste technische Problem
umfasst neben der Auswertung der Videodaten zudem, dem Benutzer neben der
Routenbewertung bezüglich eines vorbestimmten Attraktivitätskriteriums auch
aussagekräftige, qualitativ hochwertige Videos oder Einzelbilder zur Verfügung zu
stellen. Daher trägt auch die Auswahl des zu mindestens einen korrespondierenden
Bildes aus dem Maximalbereich in Abhängigkeit vom Qualitätssignal zur Lösung
des technischen Problems bei.

Des Weiteren wird der Nutzer durch die Auswahl der extrahierten Bilder in die Lage
versetzt, sich einen guten Eindruck über die Attraktivität der ausgewählten Route zu
verschaffen. Statt unerwünscht kurze Videos zu präsentieren, welche vom menschlichen Betrachter mental nicht verarbeitet werden können (vgl. OS, Abs. [0022]),
wird bei einer ermittelten zu kurzen Abspieldauer statt eines Videos des
Maximalbereichs nur ein repräsentatives Einzelbild aus diesem ausgegeben. Dies

                                       - 12 -

betrifft somit Programm-Anweisungen für die Präsentation von Bildinhalten in einer
Weise, die auf die physischen Gegebenheiten der menschlichen Wahrnehmung
und Aufnahme von Information Rücksicht nimmt und dabei darauf gerichtet ist, die
Wahrnehmung der gezeigten Information durch den Menschen in bestimmter Weise
überhaupt erst zu ermöglichen, zu verbessern oder zweckmäßig zu gestalten. Sie
dienen der Lösung eines technischen Problems mit technischen Mitteln und sind
somit bei der Prüfung auf erfinderische Tätigkeit zu berücksichtigen (vgl. BGH Urteil
vom 26. Februar 2015, X ZR 37/13, GRUR 2015, 660, Rn. 35 – Bildstrom).

Somit liegt mit dem Verfahren des Patentanspruchs 1 eine technische Lehre vor,
die als Erfindung dem Patentschutz zugänglich ist.



7.   Der Gegenstand des Patentanspruchs 1 ist gegenüber dem im Verfahren
befindlichen Stand der Technik neu (§ 3 PatG).

Die wissenschaftliche Veröffentlichung D8 betrifft ein Sensorsystem, mit dem die
Kirschblüte entlang einer Fahrstrecke detektiert und deren Intensität bewertet
werden kann. Einem Anwender sollen dabei Informationen über die Fahrroute und
Bildsequenzen zur Kirschblüte zur Verfügung gestellt werden. Die D8 offenbart
damit ein Verfahren zum Auswerten eines optischen Erscheinungsbildes einer
Fahrstrecke, (vgl. Fig 1, Titel: SakuraSensor: A Participatory Sensing System for
Detecting Flowering Cherries with Car-Mounted Smartphones M1.1).

                                         - 13 -

Hierbei werden aus mindestens einem Kraftfahrzeug, das auf einer Fahrstrecke
fährt oder gefahren ist, Videodaten, die eine Bildsequenz der Fahrstrecke enthalten
(vgl. 2.: At the smartphone side, while a car is traveling, the smartphone
continuously records GPS logs and videos captured by its camera.) und über eine
jeweilige Kommunikationsverbindung an eine Recheneinrichtung übertragen
werden, empfangen (vgl. Fig. 1; 1: which employs participatory sensing to collect
information about cherry-lined routes (including images and videos) from carmounted smartphones and shares collected information among its users. M1.2).

Durch eine Analyseeinrichtung wird auf der Grundlage der Videodaten zu Bildern
der Bildsequenz jeweils ein Übereinstimmungswert betreffend einen Grad einer
Übereinstimmung des Bildes mit einem vorbestimmten Attraktivitätskriterium
ermittelt (vgl. 2.: a color histogram that represents the color distribution of flowering
cherries is generated in advance using various images that contain flowering
cherries. … for each pixel of each frame, the frequency that the pixel belongs to
flowering cherries is calculated; 1.: that quantifies the amount of flowering cherries
recorded in the videos captured by car-mounted smartphones teilweise M1.3ohne
Analyse auf der Rechenvorrichtung).


Die Übereinstimmungswerte der Bilder werden in Form eines Bewertungssignals
als Beschreibung des Erscheinungsbildes der Fahrstrecke ermittelt (vgl. 2: The
cherry intensity is calculated for each frame as the mean value of the frequency of
all pixels in the frame. … About 5000 short videos (each is 1 second long), which
are extracted from the recorded videos, are classified into multiple classes
depending on the amount of flowering cherries contained in each video using
SakuraSensor; M1.4, M1.5).

Für die Routenvorschau werden Übereinstimmungswerte für eine Fahrstrecke und
die extrahierten Bilder aus dem Maximalbereich für den Fahrer bereitgestellt (vgl.
Fig. 1; 1: Based on the collected information, a scenic routes recommendation
service with up-to-date information can be provided, where the users search the
best scenic route to a specified destination by viewing short videos along the
searched route. 4: sharing information (cherry intensity and videos) of cherry-lined
roads by using car-mounted smartphones; teilweise M1.14ohne Gesamtwert).

                                      - 14 -

Hierfür baut das Navigationssystem eines Fahrzeugs und die Recheneinrichtung
eine Kommunikationsverbindung auf (vgl. Fig. 1; M1.15) und das Fahrzeug bezieht
die extrahierten Bilder und die Werte aus der Recheneinrichtung (vgl. Fig. 1;
4: sharing information (cherry intensity and videos) of cherry-lined roads M1.16),
welche sie als Routenvorschau und Routenbewertung grafisch an den Fahrer
zurückgibt (vgl. Fig. 1b; 1: where the users search the best scenic route to a
specified destination by viewing short videos along the searched route. M1.17).
Dem Verfahren der D8 fehlen somit die Merkmale, die für die Auswahl der zu
übermittelnden Videos nötig sind (M1.6 - M1.12), die Analyse der Videodaten auf
der Rechenvorrichtung (M1.3Rest) und die Routenbewertung (M1.13, M1.14Rest).
Insbesondere wird keine Abspieldauer ermittelt, anhand der entschieden wird, ob
ein Videosignal oder nur ein einzelnes Bild ausgegeben wird.

Auch die Druckschrift D9, die im Zusammenhang mit Druckschrift D8 hinsichtlich
der dort genannten „OpenCV library“ in das Verfahren eingeführt wurde, offenbart
nicht mehr Merkmale.

Die Druckschrift D1 aus dem Jahr 1934 liegt aufgrund der fehlenden Details zur
automatischen Bildauswertung fern ab.

Die Druckschrift D2, auf die sich der Zurückweisungsbeschluss im Wesentlichen
stützt, beschäftigt sich zwar mit einem Verfahren zum Auswerten einer Fahrstrecke
(M1.1), allerdings anhand von über Kommunikationsverbindungen zu einer
Rechnereinrichtung empfangenen Bewertungen (wie zum Beispiel landschaftlich,
geschichtlich oder touristisch interessante Strecken). Videodaten werden weder
aufgenommen noch analysiert.

Die Druckschrift D3 befasst sich mit einem Verfahren zur rechnergestützten
Optimierung für mehrere Kriterien bei der Auswahl einer Route eines
Kraftfahrzeugs. Ein Auswerten eines optischen Erscheinungsbildes einer Fahrstrecke anhand von Videobildern wird nicht beschrieben. Dies trifft auch auf die
Schrift D4 zu, welche eine optimale Fahrroute bezüglich des Energieverbrauchs
bestimmt.

                                      - 15 -

Die Klassifizierung von aufgenommenen Straßenszenen mittels neuronalen Netzen
ist Inhalt der Publikation D5. Eine Anwendung für die Navigation ist nicht
angegeben.

Die Dissertation D6 beschäftigt sich mit der automatischen Bereitstellung von
auffälligen Landmarken, um die Wegbeschreibungen eines Navigationssystems an
eine menschliche Wegbeschreibung anzupassen. Hierfür werden bestehende
Geodatenbestände verwendet und aus diesen die Landmarken extrahiert (M1.3tw).
Es fehlen zumindest die aufgenommenen Videodaten (M1.2) und die daraus
generierte Routenvorschau (M1.6 – M1.17).

Der Artikel D7 befasst sich mit demselben Problem, nämlich ein Navigationssystem
bereitzustellen, bei dem beim Routenvorschlag auch deren landschaftlicher Aspekt
berücksichtigt wird (M1.1). Hierzu werden im Internet hochgeladene Fotos mit
Positionsangaben ausgewertet – unter anderem bezüglich Häufungen von Fotos an
einem bestimmten Ort. Es werden jedoch keine ausgewählten Videos dem
Navigationssystem zur Verfügung gestellt.

Auch die übrigen, in der Beschreibungseinleitung der Anmeldeunterlagen
genannten Druckschriften (US 2006/0271286 A1, WO 2014/054288 A1, US
2009/0171568 A1) offenbaren in Bezug auf den Patentanspruch 1 nicht mehr als
die vorgenannten Entgegenhaltungen.



8.   Der Gegenstand des Patentanspruchs 1 beruht gegenüber dem im Verfahren
befindlichen Stand der Technik auch auf einer erfinderischen Tätigkeit (§ 4 PatG).

Ausgehend vom Verfahren der wissenschaftlichen Publikation D8, die sich hauptsächlich mit der Auswertung der Videoframes über die Kirschblüte entlang einer
Fahrroute und dem Übertragen der Videos auf den zentralen Server beschäftigt, hat
der Fachmann mehrere Veranlassungen zur Weiterentwicklung des Verfahrens.

In der „Introduction“ wird darauf hingewiesen, dass ein verbesserter „scenic route
recommandation service“ angeboten werden kann. In Kenntnis der üblichen
Auswahl zwischen mehreren Routen in gängigen Navigationsystemen (vgl. zum

                                        - 16 -

Beleg des Fachwissens z.B. D2) ist es für den Fachmann naheliegend, dem Fahrer
verschiedene Routen in einer nach Kirschblütenintensität geordneten Reihenfolge
vorzuschlagen. Bei mehreren Kirschblütenorten an einer Strecke, ist die Mittelwertbildung für die Bildung einer Rangfolge verschiedener Strecken ein fachübliches
Mittel (M1.13, M1.14Rest). Die Kirschblütenintensität-anzeigenden Zahlen der Fig.
1b zusammen mit dem Ziel, dem Fahrer eine Route mit blühenden Kirschbäumen
vorzuschlagen (vgl. 1.: to collect information about cherry-lined routes), legen dem
Fachmann einen Schwellenwert nahe, ab welchem ein Kirschbaum in Blüte steht
(M1.6).

Weiterhin   weist   die   E8   darauf   hin, dass   die   Kommunikation mit      der
Recheneinrichtung durch Bandbreite oder Vertragslimits begrenzt ist (vgl. 2.: for the
recorded videos, it would not be possible to continuously transfer them to the server
due to the limitation on the communication bandwidth of 3G/4G network or monthly
available communication amount limitation posed to users.). Dieser Aspekt spielt
beim Übertragen der Videos auf den Server ebenso eine Rolle, wie auch beim
Übertragen der Videos auf das Navigationssystem (vgl. 1.: where the users search
the best scenic route to a specified destination by viewing short videos along the
searched route). Daher wird sich der Fachmann mit der Frage auseinandersetzen,
wie er die auf das Navigationssystem zu übertragenden Videos auf die
aussagekräftigsten Videosequenzen reduziert. Hieraus folgt direkt, dass nur Videosequenzen mit Kirschbäumen, die zu einem Großteil in Blüte sind (Schwellenwert),
ausgewählt werden (M1.6, M1.7).

Ob es aufgrund der Bandbreitenbegrenzung nahegelegen haben mag, zudem die
zu übertragenden Videos anhand der Bildqualität auszuwählen, kann dahin stehen
(M1.8 – M1.10). Denn anhand der Abspieldauer zu entscheiden, ob ein einzelnes
Bild oder ein Videosignal ausgegeben wird, ist weder aus der D8 bekannt, noch für
den Fachmann naheliegend.

Zudem unterscheidet sich das Verfahren der D8 vom Verfahren der Anmeldung in
dem Ort, an dem die aufgenommenen Videodaten analysiert werden. Während in
der Anmeldung die gesamte Analyse auf der externen Recheneinrichtung vorgenommen wird, übernimmt dies in der D8 die Sakura-Sensor Applikation auf den

                                      - 17 -

Smartphones. Nur die Ergebnisse sowie die kurzen Videos werden auf die Recheneinrichtung („server“) übertragen. Eine Veranlassung für die Auswertung der
Videodaten auf der externen Recheneinrichtung ist durch die Bandbreitenbegrenzung nicht gegeben.

Die übrigen im Verfahren befindlichen Druckschriften bilden für die Beurteilung der
erfinderischen Tätigkeit ebenfalls keinen geeigneten Ausgangspunkt .

Damit steht fest, dass der Gegenstand des Patentanspruchs 1 gegenüber dem im
Verfahren befindlichen Stand der Technik auch auf einer erfinderischen Tätigkeit
beruht und damit patentfähig ist.



9.   Die abhängigen Ansprüche 2 bis 7 sind mit dem gewährbaren Patentanspruch 1 ebenfalls patentfähig.



10. Da die vorgelegten geltenden Unterlagen auch den weiteren Voraussetzungen
zur Patenterteilung (§§ 1, 2, 5, 34 PatG) genügen, war auf die Beschwerde der
Anmelderin der Zurückweisungsbeschluss der Prüfungsstelle für Klasse G 06 V des
Deutschen Patent- und Markenamts aufzuheben und ein Patent zu erteilen.

                                           - 18 -

                                            III.


                                   Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
       Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
       Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
       sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
       zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
       die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind,
       oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek               Kätker            Dr. Flaschke        Dr. Schenkl

                                  - 19 -

Bundespatentgericht

     18 W (pat) 22/23
         (Aktenzeichen)




Verkündet am

22. Oktober 2024

…
Justizbeschäftigter
als Urkundsbeamter der Geschäftsstelle
