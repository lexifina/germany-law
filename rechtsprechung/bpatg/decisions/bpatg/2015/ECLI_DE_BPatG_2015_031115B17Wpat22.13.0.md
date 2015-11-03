---
ecli: "ECLI:DE:BPatG:2015:031115B17Wpat22.13.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 22/13"
decided: "2015-11-03"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=47&nr=27582&anz=851&pos=707&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-11-03_17_W-pat_22_13_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 22/13 vom 2015-11-03

## Entscheidung

BUNDESPATENTGERICHT



 17 W (pat) 22/13
_______________________

    (Aktenzeichen)




                             BESCHLUSS

                            In der Beschwerdesache


                 betreffend die Patentanmeldung 103 35 601.0-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts in
der Sitzung vom 3. November 2015 unter Mitwirkung des Vorsitzenden Richters
Dipl.-Phys. Dr. Morawek,      der     Richterin     Eder,      der    Richterin
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel




BPatG 152
08.05

                                     -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und Markenamts vom 4. März 2013 aufgehoben und das Patent mit folgenden
       Unterlagen erteilt:


       Patentansprüche 1 bis 12 vom 24. September 2015, eingegangen
       am 2. Oktober 2015,
       Beschreibung Seiten 4, 4a, 4b, 5, 6, 6a, 9 und 18 vom 24. September 2015, eingegangen am 2. Oktober 2015,
       Beschreibung Seiten 1 bis 3, 7, 8 und 10 bis 17 und
       5 Blatt Zeichnungen mit Figuren 1 bis 5 vom Anmeldetag.




                                  Gründe


                                       I.


Die vorliegende Patentanmeldung ist am 4. August 2003 beim Deutschen Patentund Markenamt eingereicht worden. Sie trägt die Bezeichnung


          „Verfahren zur Objektklassifizierung unter Verwendung einer
                             3D-Modelldatenbank“.


Die Prüfungsstelle für Klasse G06T hat am 4. März 2013 die Anmeldung zurückgewiesen, da der Anspruch 1 mangels erfinderischer Tätigkeit seines Gegenstandes nicht gewährbar sei.


Gegen diesen Beschluss wendet sich die am 5. April 2013 eingegangene
Beschwerde der Anmelderin.

                                      -3-



Die Beschwerdeführerin beantragt sinngemäß,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 12 vom 24. September 2015, eingegangen
       am 2. Oktober 2015,

       Beschreibung Seiten 4, 4a, 4b, 5, 6, 6a, 9, 18 vom 24. September 2015, eingegangen am 2. Oktober 2015,

       Beschreibung Seiten 1 bis 3, 7, 8 und 10 bis 17 vom Anmeldetag,

       5 Blatt Zeichnungen mit Figuren 1 bis 5 vom Anmeldetag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


       D1: US 6 259 815 B1

       D2: US 2003/0114964 A1

       D3: Edwars, J.; Murase, H.: “Appearance Matching of Occluded Objects
       Using Coarse-to-fine Adaptive Masks”, Proc. IEEE Conference on Computer Vision and Pattern Recognition 1997, ISSN 1063-6919/97, S. 533 –
       539

       D4: DeCarlo, D.; Metaxas, D.: “Blended Deformable Models”, IEEE
       Transactions on Pattern Analysis and Machine Intelligence, Vol. 18, No. 4,
       April 1996, S. 443 – 446

       D5: DE 100 25 678 A1

       D6: US 6 498 972 B1.

                                       -4-



Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft
ein


       „1.    Verfahren zur computergestützten Klassifizierung von dreidimensionalen Objekten zu einer oder mehreren vorgegebenen Klassen (20, 22,
       24),

       (A)    bei dem ein Objekt messtechnisch erfasst wird,

       (B)    wobei von mindestens einem Sensor ein Satz von Messdaten (50)
       erzeugt wird,

       (C)    und das Objekt mit einem oder mehreren Modellen als Repräsentant einer jeweiligen Klasse von Objekten verglichen wird,

       (D)    wobei ein Modell aus einer vorgegebenen Menge von Modelldatenpunkten berechenbar ist,

       mit folgenden Schritten:

       a)     die Messdaten (50) Informationen über alle drei Raumrichtungen
       enthalten,

       b)     Vergleichen (130) der dreidimensionalen Form, die sich aus einer
       Messdatenpunktwolke (50) ergibt, mit einer dreidimensionalen Modellform (300), wobei ein Vergleichsresultat für die Kongruenz der Formen
       aus Messdaten (50) und Modelldaten (26, 28, 30, 32, 34, 36) erzeugt wird,

       c)     Variieren (140) der geometrischen Beziehung zwischen beiden Formen,

       d)     Wiederholen der Schritte b) und c), solange bis eine Kongruenz
       erreicht ist, die ein vorbestimmtes Qualitätskriterium erfüllt (160), oder ein
       anderes, vorgewähltes Abbruchkriterium erfüllt (170) ist,

                                       -5-



       e)     Durchführen der Schritte b), c) und d) für die Modellformen aller zur
       Auswahl stehenden Klassen,

       f)     Klassifizieren (190) des 3D-Objekts in die demjenigen Modell zugeordnete Klasse, bei dem das beste Vergleichsresultat erzielt wurde,

       dadurch gekennzeichnet, dass

       (g1)   im Schritt a) als weitere Sensordaten (52) eine Geschwindigkeit des
       Objekts erfasst wird,

       (g1a) wobei ein typischer Geschwindigkeitsbereich (38) der Klasse des
       Objekts mit in die Klassifizierung (190) für eine Plausibilitätsprüfung einbezogen wird,

       und/oder

       (g2)   im Schritt a) als weitere Sensordaten (52) eine Beschleunigung des
       Objekts erfasst wird, wobei ein typisches Beschleunigungsvermögen (40)
       der Klasse des Objekts mit in die Klassifizierung (190) für eine Plausibilitätsprüfung einbezogen wird,

       (h)    wobei durch einen Vergleich der weiteren Sensordaten (52) mit
       Zusatzinformationsdaten (38, 40) eine Vorauswahl der in Frage kommenden 3D-Modelldaten getroffen wird.“


Der nebengeordnete Patentanspruch 12 lautet:


       „12. Computergestütztes Fahrzeuginformationssystem (3) enthaltend

       wirksame Verbindungen zu Fahrzeugsensoreinrichtungen (5) zur Erfassung von Objekten aus dem Umfeld des Fahrzeugs (1),

                                        -6-



       wobei als weitere Sensordaten (52) die Geschwindigkeit und/oder die
       Beschleunigung eines Objekts messtechnisch erfassbar sind,

       eine computergestützte Datenbank (9), enthaltend Daten dreidimensional
       abbildender Modelle (26, 28, 30, 32, 34, 36) von Objekten und Zusatzinformationen mit wenigstens

       a)   einem Geschwindigkeitsbereich eines Objekts, oder

       b)   einem Beschleunigungsbereich eines Objekts,

       einen Steuerkreis (11) zur Analyse (130, 140, 150, 160, 170) und Klassifizierung (190) der erfassten Objekte mit Hilfe der Daten der dreidimensional abbildenden Modelle und der Zusatzdaten,

       wobei ein typischer Geschwindigkeitsbereich (38) einer Klasse eines
       Objekts mit in die Klassifizierung (190) für eine Plausibilitätsprüfung

       und/oder ein typisches Beschleunigungsvermögen (40) einer Klasse eines
       Objekts mit in die Klassifizierung (190) für eine Plausibilitätsprüfung einbezogen wird,

       wobei durch einen Vergleich der weiteren Sensordaten (52) mit Zusatzinformationsdaten (38, 40) eine Vorauswahl in Frage kommender 3D-Modelldaten getroffen wird,

       sowie wirksame Verbindungen zu Aktuatoreinrichtungen (13) am Fahrzeug (1), die je nach Klassifizierungsergebnis selektiv betätigbar sind.“


Zu den übrigen Patentansprüchen sowie zu den weiteren Einzelheiten wird auf die
Akte verwiesen.

                                       -7-



                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat auch Erfolg, da ein Patent nach dem nunmehr geltenden Antrag erteilt werden
kann.


1.      Gegenstand der Patentanmeldung ist ein Verfahren zur computergestützten
Klassifizierung von dreidimensionalen Objekten zu einer oder mehrerer vorgegebenen Objektklassen, bei dem ein Objekt messtechnisch erfasst wird (Offenlegungsschrift Abs. [0001]).


In der Offenlegungsschrift Abs. [0002] bis [0009] ist zum Stand der Technik Folgendes ausgeführt:


In vielen Anwendungsgebieten würden heute Objektdaten wie z. B. Position, Ausmaß, Geschwindigkeit und Beschleunigung aus einer 3D-Umgebung erfasst, unter
anderem in der Umfelderfassung von Fahrzeugen. Diese Objektdaten würden von
Messeinrichtungen geliefert, welche aus einem oder mehreren Sensoren bestehen
könnten (Radar, Video, Lidar, ...).


Eine Zielsetzung in der Verarbeitung von Objektdaten sei die Klassifizierung, d. h.
die Zuordnung von Objekten zu bestimmten Objektklassen, wobei jede Klasse
eine Menge von zusammengehörigen Objekten repräsentiere. Bei der Umfelderfassung von Fahrzeugen könnten beispielsweise Fußgänger, Radfahrer, Personenkraftwagen (PKW) und Lastkraftwagen (LKW) wesentliche Objektklassen sein.


Zur Objektklassifizierung seien unterschiedliche Verfahren bekannt.


Bei einem datenbasierten Ansatz werde das vorhandene Datenmaterial selbst
untersucht, um geeignete Unterscheidungsmerkmale zu finden und damit die
Objekte den verschiedenen Klassen zuzuordnen. Dies sei meist mit einem hohen

                                        -8-



Aufwand hinsichtlich der erforderlichen Trainingsprozesse und der Datenanalyse
verbunden; insbesondere sei bei Veränderung der Objektklassen eine erneute
Analyse des Datenmaterials zur Ermittlung der Unterscheidungsmerkmale notwendig.


Im Gegensatz zum datenbasierten Ansatz werde beim modellbasierten Ansatz
Vorwissen über die Elemente einer Klasse in Form von Modellen eingebracht. Ziel
sei es, die unterschiedlichen Erscheinungsformen möglichst aller in der Praxis
häufig auftretenden Objekte durch die Verwendung solcher Modelle nachzubilden.
Die Klassifizierung, also die Zuweisung der Objekte zu den Objektklassen,
geschehe im Stand der Technik durch einen Vergleich der Objektdaten mit den
vorher festgelegten Modellen.


So würden etwa bei dem modellbasierten 2D-Klassifizierungsverfahren „2D-Template-Matching“ zweidimensionale Schablonen verwendet, um beispielsweise
in einem Videobild charakteristische Muster zur Klassifizierung eines aufgenommenen Objektes wiederzuerkennen. Diese Schablonen könnten sich je nach
Anwendung z. B. auf Form, Helligkeit, Farbe oder Kanten beziehen. Da Objekte in
Abhängigkeit von ihrer Orientierung und Lage zum Sensor unterschiedliche
Erscheinungsformen haben könnten - ein Fahrzeug sehe ja von vorn betrachtet
anders aus als von der Seite betrachtet -, würden je nach Qualitätsanforderungen
zumindest einige bis hin zu sehr vielen solcher Schablonen zur Repräsentation
eines Objektes benötigt. Ein weiteres Problem sei die Oberflächenbeschaffenheit
eines Objekts, also Texturierung und Farbe. So könnten Objekte gleichen Typs je
nach Oberfläche, Farbe und Beleuchtung von einem Sensor unterschiedlich wahrgenommen werden. Diese Einflüsse seien bei 2D-Klassifizierungsverfahren wie
dem „Template-Matching“ zu berücksichtigen; sie machten die Auswertung der
erfassten Daten und die Klassifizierung sehr komplex und erforderten gegebenenfalls eine zu lange Rechenzeit, was insbesondere bei gefordertem schnellen Echtzeitverhalten eines Systems nicht tolerierbar sei.

                                       -9-



Der Erfindung soll nunmehr die Aufgabe zugrunde liegen, eine robuste, genaue
und schnelle Klassifizierung durchzuführen (Eingabe vom 12. September 2011,
Punkt 3. erster Absatz).


Ein Kerngedanke der Erfindung ist, dass eine Messdatenpunktwolke erzeugt wird,
wobei jeder Punkt Informationen über alle drei Raumrichtungen enthält, und dass
zur Klassifizierung die sich hieraus ergebende Form mit einer dreidimensionalen
Modellform verglichen wird. Hierfür müssen die dreidimensionalen Informationen
der Messdatenpunkte, insbesondere auch die Information über die Entfernung
zum Sensor ausreichend genau sein, so dass auch Entfernungsdifferenzen zwischen den einzelnen Messpunkten in Sensorrichtung beim Vergleich berücksichtigt werden können. Eine Information der allgemeinen Form „Abstand des gesamten Messobjekts vom Sensor“ reicht dafür nicht aus.


Als Fachmann ist hier ein Informatiker oder Physiker mit guten Kenntnissen in der
Bildverarbeitung, insbesondere in der Klassifizierung von Objekten anzusehen.


2.    Die nunmehr geltenden Unterlagen liegen im Rahmen der ursprünglichen
Offenbarung.


Der geltende Anspruch 1 geht hervor aus dem ursprünglichen Ansprüchen 1 und 2
sowie der Offenlegungsschrift z. B. Abs. [0038] (Sensoren) sowie [0015] bis
[0017], [0046] und [0047].


Die geltenden Unteransprüche 2 bis 12 entsprechen den ursprünglichen Ansprüchen 3 bis 13.


Der geltende, nebengeordnete Anspruch 12 geht hervor aus dem ursprünglichen
Anspruch 14 sowie den oben zum Anspruch 1 genannten Offenbarungsstellen.


Alle Ansprüche sind somit ursprünglich offenbart.

                                       - 10 -



Die ebenfalls zulässigen Änderungen in der Beschreibung betreffen teilweise die
Darlegung des Standes der Technik, teilweise ergeben sie sich aus den geänderten Ansprüchen.


3.     Das Verfahren gemäß dem Anspruch 1 ist neu gegenüber dem belegten
Stand der Technik und beruht auf erfinderischer Tätigkeit.


Dies ergibt sich aus der Würdigung der zum Stand der Technik genannten Druckschriften und Unterlagen.


3.1.   Aus dem druckschriftlich belegten Stand der Technik war vor dem Anmeldetag der vorliegenden Patentanmeldung Folgendes bekannt:


Die Druckschrift D1 behandelt ein System und Verfahren zur Erkennung abgetasteter Objekte mit Hilfe von deformierbaren Modellen. Ziel ist es, vom Benutzer
selbst geformte Spielzeugmodelle aufzunehmen und so zu repräsentieren, dass
sie in animierter Form eine Welt der virtuellen Realität bevölkern können (Sp. 2
Z. 30 bis 42). Ein auf einem Drehtisch 110 angeordnetes Objekt 101 wird mit Hilfe
einer Kamera 120 und eines Lasersystems 130 dreidimensional abgetastet
(Fig. 1). Die Orientierung des Objekts ist vorzugsweise bekannt, sie kann aber
auch abgeleitet werden (Sp. 2 le. Abs.). Die abgetasteten Bilder des Objekts werden mit parametrisierten Objektmodellen (Fig. 3) verglichen, das Objekt wird dem
zum besten Vergleichsergebnis gehörigen Modell (und damit auch der Klasse, die
das Modell repräsentiert) zugeordnet (Sp. 3 Abs. 3, Fig. 2). Jedes Modell ist in
eine Anzahl von als Rechtecks-Pyramidenstümpfe ausgebildeten Gliedern unterteilt (Fig. 4) und einer Objektklasse (z. B. „Zweifüßer“, „Haus“) eindeutig zugeordnet (Sp. 3 Abs. 4 bis 6). Für jede Objektklasse existieren mehrere Modelle, die
sich in den relativen Abmessungen und Richtungen ihrer Glieder unterscheiden
(Sp. 3 vorle. Abs., Fig. 5). Beim Vergleich von Objekt und Modell wird unter anderem die Anzahl der Voxel berücksichtigt, welche sowohl im abgetasteten Objekt
als auch im Modell besetzt sind (Sp. 4 Abs. 4 „Superposition“). Für den Vergleich

                                       - 11 -



wird jedes Modell größenangepasst, gerastert und mit den abgetasteten volumetrischen Objektdaten verglichen; hierbei werden in mehreren Schritten die Modellparameter (Größen- und Ortsparameter) variiert (Sp. 4 drittle. Abs. bis Sp. 5 Abs. 2).
Eine Vorauswahl von Modelldaten anhand von Geschwindigkeits- oder Beschleunigungsinformation ist in D1 nicht ausgewiesen.


D2 betrifft ein einfaches Klassifikationsschema zur Erkennung von Hindernissen,
nämlich von Fahrzeugen, Masten und Fußgängern (Titel, Abstract, Fig. 1). Mit
Hilfe eines oder mehrerer Sensoren werden Umriss, Geschwindigkeit und Entfernung eines Hindernisses detektiert (Abs. [0025], [0026]). Aus den Höhen- und
Breitendaten wird eine das Hindernis umschließende rechteckige Hülle („bounding
box“ 26) erzeugt (Abs. [0027], Fig. 2). Die Entfernungsdaten werden dazu verwendet, aus den (zweidimensionalen) Pixelabmessungen die tatsächlichen zweidimensionalen Objektabmessungen (Höhe, Breite) zu ermitteln (Abs. [0028]). Der
Fahrzeugtyp wird über die Fahrzeughöhe klassifiziert, der Drehwinkel des Fahrzeugs ergibt sich über dessen sichtbare Breite (Abs. [0030], [0031]); zusätzliche
Genauigkeit lässt sich durch Einbeziehung der Geschwindigkeit erzielen
(Abs. [0037]). Auch andere Objekte (z. B. Fußgänger, Masten oder Bäume) werden anhand ihrer Höhe und Breite klassifiziert (Abs. [0043], Fig. 7). Ein 3D-Modellvergleich mit Hilfe einer dreidimensionalen Punktwolke und eine Vorauswahl von
Modelldaten anhand von Geschwindigkeits- oder Beschleunigungsinformation sind
in D2 nicht ausgewiesen.


D3 zeigt ein Verfahren, um (teilweise) verdeckte Objekte in Szenen Modellen
zuzuordnen. Es wird ein „appearance matching“ - Verfahren verwendet, wobei
Hypothesen über Verdeckungsbereiche aufgestellt werden und mit Hilfe zweidimensionaler adaptiver Masken und deren Vergleich mit der Szene überprüft werden; die Maske mit dem besten Vergleichswert entspricht dann der „richtigen“ Platzierung der verdeckten Bereiche (Abstract, Kap. 3). Hierbei wird hierarchisch von groben zu feinen Masken hin vorgegangen. Das Einbeziehen von

                                      - 12 -



Geschwindigkeits- oder Beschleunigungsinformation zur Modellvorauswahl ist
nicht vorgesehen.


D4 beschreibt das Erstellen von Modellen, die eine relativ große Anzahl möglicher
Formen beinhalten und mit relativ wenigen Parametern beschreibbar sein sollen.
Hierfür kann zwischen verschiedenen möglichen Formen interpoliert werden
(„blending“); vgl. Abstract, Kap. 1 Abs. 1 sowie Fig. 2 und 3 mit Beschreibung.
Weitere Hinweise auf das beanspruchte Verfahren sind nicht erkennbar.


D5 betrifft ein kamerabasiertes Precrash-Erkennungssystem. Als Stand der Technik zur Interpretation von Bildszenen ist in Abs. [0004] angegeben, mit einem relativ aufwändigen Sensor (Stereo-Sensor oder hochauflösendes Radar oder Lidar)
neben rein zweidimensionaler Bildinformation bereits mehrdimensionale Szeneninformation zu gewinnen. Um hierbei Objekte detektieren zu können, gingen diese
Verfahren von Modellen bzgl. Lage und Ausrichtung potentieller Ziele sowie vorgegebener Ausrichtung bzgl. Sensor und Umgebung aus, was jedoch mit realen
Bedingungen oft nicht übereinstimme und zu Fehlinterpretationen führe. Demgegenüber lehrt D5, zunächst in einem zweidimensionalen Kamerabild mit Hilfe
eines auf zu erkennende Ziele (Verkehrsteilnehmer oder Hindernisse) trainierten
Klassifikators Regionen zu identifizieren, in denen sich solche Ziele befinden.
Diese Regionen werden markiert und mittels eines entfernungsmessenden Sensors bezüglich ihrer Entfernung vom Beobachter vermessen. Abschließend werden ausgewählte Regionen einer Typ-Klassifikation zur exakten Bestimmung der
Art von Verkehrsteilnehmer oder Hindernis zugeführt (Abs. [0008], [0011], Fig. 1).
Aus der wiederholten Vermessung der Entfernung der Verkehrsteilnehmer oder
Hindernisse wird deren Relativgeschwindigkeit in Bezug auf den Beobachter bestimmt (Abs. [0017]). Nach der Identifizierung von Regionen und deren Entfernungsmessung kann die Bildinformation und die Entfernungs- und Geschwindigkeitsinformation einer Auswahleinheit 4 zugeführt werden, welche die endgültig zu
klassifizierenden Bilddaten 40 auswählt und an eine Klassifikationseinheit 5 zur
Typ-Klassifikation weiterleitet. Die Auswahleinheit kann z. B. nur die Bilddaten an

                                       - 13 -



die Klassifikationseinheit weiterleiten, welche bestimmte Kriterien erfüllen, etwa
hinsichtlich der Größe oder der Geschwindigkeit von Objekten (Abs. [0018]). Zur
Entfernungsmessung eignen sich Radarsysteme oder Stereo-Kamera-Systeme.
Da die von den Sensoren gewonnenen Daten rein zur Entfernungsmessung und
nicht zu einer Typ-Klassifikation in Bezug auf die Art von Verkehrsteilnehmer oder
Hindernis herangezogen werden, ist es nicht notwendig, diese Sensoren mit extremen Winkelauflösungen und extrem rechenaufwändigen, robusten Modellen auszustatten; somit kann auf bereits im Fahrzeug vorhandene, auf andere Anwendungen spezialisierte Sensoren zurückgegriffen werden (Abs. [0015]). Alternativ kann
mittels einer Monobildkamera und komplexer Bildauswertung im Bereich der
Regionen (ROI) eine Entfernungsschätzung durchgeführt werden (Abs. [0016]).


D6 beschreibt ein Pre-Crash-Erkennungssystem. Über verschiedene Sensoren im
Fahrzeug (Kameras, Radar, Lidar) werden in einer vorgegebenen Entscheidungszone das Vorhandensein eines Objekts sowie dessen Parameter wie Größe, Entfernung vom Fahrzeug, Geschwindigkeit und Orientierung bestimmt (Sp. 3 Z. 21
bis 42; Sp. 4 Z. 25 bis Sp. 5 Z. 7), zudem über weitere Sensoren verschiedene
Parameter des Fahrzeugs (Trajektorie, Geschwindigkeit usw.; Sp. 3 Z. 43 bis
Sp. 4 Z. 7). Liegen die Geschwindigkeiten, die Objektentfernung und die Größe
des Objekts in vorgegebenen Bereichen, so wird das Objekt klassifiziert und Gegenmaßnahmen eingeleitet (Fig. 7). Zur Objektklassifizierung können verschiedene Charakteristika des Objekts wie Höhe, Breite und Fläche (auch zeitabhängig
betrachtet) verwendet werden (Sp. 6 Z. 3 bis 26).


3.2.   Das Verfahren des Anspruchs 1 und ebenso das Fahrzeuginformationssystem des nebengeordneten Anspruchs 12 sind gegenüber diesem Stand der Technik neu und beruhen auf erfinderischer Tätigkeit.


Im Zurückweisungsbeschluss wird mit Hinweis auf Abs. [0009], [0011], [0015] und
[0016] der D5 argumentiert, im Verfahren der D5 enthielten die Messdaten Informationen über alle drei Raumrichtungen. Die Druckschrift D5 überlasse ferner die

                                      - 14 -



Wahl des zur „eigentlichen Typ-Klassifikation“ verwendeten Algorithmus dem
Fachmann. Dieser werde daher im Stand der Technik nach geeigneten Typ-Klassifikationsalgorithmen für messtechnisch erfasste Objekte suchen, wobei die
Messdaten Informationen über alle drei Raumrichtungen enthalten, und so auf die
Druckschrift D1 stoßen (und das dort beschriebene Verfahren zur Typ-Klassifikation in D5 anwenden). Da aus D5 bereits bekannt sei, dass dem Klassifikationsalgorithmus Objekte bereits vorausgewählter Klassen (z. B. (langsamer) „Fußgänger“ bzw. „schneller Pkw“ zugeführt werden und daher einige 3D-Modelldaten zur
Typ-Klassifikation a priori gar nicht benötigt würden (z. B. „Pkw“ bzw. „Fußgänger“), liege es für den Fachmann auf der Hand, diese 3D-Modelldaten auch nicht
für die Klassifikation zu verwenden und dadurch die Vorauswahl gemäß Merkmal (h) auch auf die in Frage kommenden 3D-Modelldaten im Rahmen der „eigentlichen Typ-Klassifikation“ auszudehnen. Dies reduziere zudem vorteilhafterweise den Rechenaufwand.


Diese Beurteilung hält der Überprüfung in einem entscheidenden Punkt nicht
stand.


In D5 ist die Entfernungsmessung eine (relativ ungenaue) Entfernungsschätzung,
die nicht zur Typ-Klassifikation in Bezug auf die Art von Verkehrsteilnehmer oder
Hindernis herangezogen wird (Abs. [0015]). Somit steht in D5 keine Messdatenpunktwolke mit genauer Entfernungsinformation für jeden Punkt gemäß Merkmal a) zur Verfügung, sondern eine Angabe, wie weit ein Objekt in einer Region
insgesamt gesehen von der Kamera entfernt ist; vgl. in D5 etwa Abs. [0008] „werden sodann die … Regionen mittels eines entfernungsmessenden Sensors bezüglich ihrer Entfernung vom Beobachter vermessen“. Diese Entfernungsinformation
ist zur Bestimmung der Größe eines Objekts nötig, die zur Abschätzung des Gefährdungspotentials interessant ist (Abs. [0018]; vgl. hierzu auch D2 Abs. [0028]);
sie wird auch zur Bestimmung der Objektgeschwindigkeit verwendet (Abs. [0017]).
Die aus D1 bekannte 3D-Punkt-Auswertung mit 3D-Modellvergleich zur Klassifikation eines Objekts gemäß Merkmal b), was für die einzelnen Punkte des zu analy-

                                       - 15 -



sierenden Objekts eine genaue Kenntnis der 3D-Koordinaten einschließlich einer
Tiefeninformation innerhalb des Objekts erfordert, bot sich jedoch in D5 nicht an.


Entsprechend lag auch die Kombination der Druckschriften D2 und D1 oder D6
und D1 nicht nahe. In D2 wird die Entfernungsinformation nur zur Ermittlung der
Objektgröße (Breite, Höhe) herangezogen (Abs. [0028]); eine Differenzierung der
Entfernungskoordinaten innerhalb des Objekts ist nicht zu erkennen. Gleiches gilt
für D6; auch hier werden zur Typ-Klassifikation lediglich zweidimensionale Objektcharakteristika (Höhe, Breite, Fläche) betrachtet, jedoch wird innerhalb des Objekts keine Differenzierung der Entfernungen durchgeführt.


Weder D5 noch D6 noch D2 ist zu entnehmen, dass in den dort beschriebenen
Verfahren nicht nur die zweidimensionalen Bilddaten eines Objekts und die Entfernung des gesamten Objekts vom Sensor, sondern auch für einzelne Punkte des
Objekts unterschiedliche Entfernungsdaten zur Typ-Klassifikation mittels ebenfalls
dreidimensionaler Modelldaten verwendet werden sollen. Damit hatte der Fachmann ausgehend von D2, D5 oder D6 keine Veranlassung, im Stand der Technik
nach einer möglichen Typ-Klassifikation zu suchen, die zusätzlich zu zweidimensionaler Ortsinformation auch innerhalb des Objekts unterschiedliche Entfernungsinformation (also „echte“ 3D-Information einschließlich Tiefeninformation wie in
D1) berücksichtigt. Einzig in D5 Abs. [0004] ist als Stand der Technik die Gewinnung von mehrdimensionaler Information mit Hilfe eines aufwändigen Entfernungssensors und eine nachfolgende Verarbeitung beschrieben. Dies wird jedoch
als nachteilig dargestellt; D5 gab damit dem Fachmann keine Veranlassung, diesen Ansatz weiter zu verfolgen.


Auch ist keine andere Argumentationslinie zu erkennen, die den Fachmann in
naheliegender Weise zum Verfahren des geltenden Anspruchs 1 hätte führen können. Ginge man von D1 aus, welche ein Verfahren mit den oberbegrifflichen Merkmalen des geltenden Anspruchs 1 zeigt, so hätte sich in diesem die Aufnahme
und Klassifikation von lediglich auf einem Drehteller kontrolliert bewegbaren,

                                      - 16 -



ansonsten unbeweglichen Spielzeugmodellen betreffenden Verfahren eine Messung von Geschwindigkeit oder Beschleunigung und deren Berücksichtigung bei
einer Vorauswahl von Modelldaten (Merkmale g1) bis h)) nicht angeboten. D3 und
D4 liegen weiter vom Anmeldungsgegenstand ab und konnten diesen ebenfalls
nicht nahelegen.


Damit ist dem Verfahren des Patentanspruchs 1 neben der (nicht in Zweifel gezogenen) Neuheit auch eine erfinderische Tätigkeit nicht abzusprechen.


Entsprechendes gilt für den nebengeordneten, auf ein Fahrzeuginformationssystem gerichteten Patentanspruch 12, gemäß welchem zur Klassifizierung erfasster
Objekte dreidimensionale Modelle verwendet werden und eine Vorauswahl von
3D-Modelldaten anhand gemessener Geschwindigkeits- oder Beschleunigungsdaten erfolgt.


4.     Der geltende Patentanspruch 1 ist gewährbar.
Entsprechendes gilt für den nebengeordneten Patentanspruch 12.


Die abhängigen Patentansprüche 2 bis 11 sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.

                                            - 17 -



                                Rechtsmittelbelehrung:


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


   das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
       Erfolg abgelehnt war,
   einem Beteiligten das rechtliche Gehör versagt war,
   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern
       er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
       hat,
   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                  Eder                Dr. Thum-Rung                 Dr. Forkel




                                                                                       Fa
