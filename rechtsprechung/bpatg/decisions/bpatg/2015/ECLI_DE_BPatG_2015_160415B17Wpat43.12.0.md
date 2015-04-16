---
ecli: "ECLI:DE:BPatG:2015:160415B17Wpat43.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 43/12"
decided: "2015-04-16"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=16&nr=27224&anz=851&pos=254&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-04-16_17_W-pat_43_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 43/12 vom 2015-04-16

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 43/12                                                       Verkündet am
_______________                                                         16. April 2015
    (Aktenzeichen)                                                            …




                              BESCHLUSS

                            In der Beschwerdesache


              betreffend die Patentanmeldung 10 2010 019 147.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 16. April 2015 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder   sowie   der   Richter
Dipl.-Ing. Baumgardt und Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                       -2-



beschlossen:


        Die Beschwerde wird zurückgewiesen.


        Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 3. Mai 2010 beim Deutschen Patentund Markenamt eingereicht. Sie trägt die Bezeichnung


    „Verfahren und Vorrichtung zur Verfolgung der Bewegungsbahn eines sich
       bewegenden Objekts sowie Computerprogramm und Datenträger“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 10. Januar 2012 mit der Begründung zurückgewiesen, dass der Gegenstand des Patentanspruchs 1 von einem
universell anwendbaren Verfahren zur Verfolgung der Bewegungsbahn eines sich
bewegenden Objektes bestimmt werde, dessen einzelne Schritte einen Algorithmus und somit eine mathematische Methode als solche darstellten, und er damit
unter das Patentierungsverbot des § 1 PatG falle.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellt den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                        -3-



        gemäß Hauptantrag mit
        Patentansprüchen 1-13,
        Beschreibung Seiten 1-17 und
        3 Blatt Zeichnungen mit Figuren 1-4B, jeweils vom Anmeldetag;


        gemäß Hilfsantrag 1 mit
        Patentansprüchen 1-13, überreicht in der mündlichen Verhandlung,
        Beschreibung und
        Zeichnungen mit Figuren, jeweils wie Hauptantrag;


        gemäß Hilfsantrag 2 mit
        Patentansprüchen 1-12, überreicht in der mündlichen Verhandlung,
        im Übrigen wie Hilfsantrag 1;


        gemäß Hilfsantrag 3 mit
        Patentansprüchen 1-10, überreicht in der mündlichen Verhandlung,
        im Übrigen wie Hilfsantrag 1;


        gemäß Hilfsantrag 4 mit
        Patentansprüchen 1-10, überreicht in der mündlichen Verhandlung,
        im Übrigen wie Hilfsantrag 1.


Sie regt ferner die Zurückverweisung an das Patentamt und die Rückzahlung der
Beschwerdegebühr an.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind die Druckschriften

                                      -4-



D1: ZHANG, H.; LANEUVILLE, D.: Grid Based Solution of Zakai Equation
with Adaptive Local Refinement for Bearings-only Tracking. In: IEEE Aerospace Conference 2008, 2008, S. 1-8

und


D2: FEUERSÄNGER, C.: An efficient Sparse Grid Method for the high
dimensional Fokker Planck Equation. In: Second Workshop on High-dimensional Approximation, 2007. URL:<
http://wwwmaths.anu.edu.au/events/hda07/talks/feuersaenger.pdf>
[recherchiert am 23.12.2010]

genannt worden. Vom Senat wurde zusätzlich die Druckschrift


D3: Balaji, B.: Efficient target tracking using adaptive grid and sparse
tensors. In: SPIE Proceedings Vol. 7336: Signal Processing, Sensor Fusion,
and Target Recognition XVIII, May 2009

eingeführt. In der mündlichen Verhandlung überreichte die Anmelderin noch die in
der Anmeldung in Absatz [0020] genannte Druckschrift


D4:   ZENGER, C.: Sparse Grids. In: W. Hackbusch (Hrsg.): Parallel Algorithms for Partial Differential Equations. Braunschweig: Vieweg, 1991 (Notes
on Numerical Fluid Mechanics 31), Seiten 241 bis 251.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


       „Verfahren zur Verfolgung der Bewegungsbahn eines sich bewegenden
       Objekts mit den folgenden Schritten:

                                -5-



a) Bereitstellung von Daten von zumindest einer die Bewegung beeinflussenden, zu bestimmenden Zustandsgröße des sich bewegenden Objekts zu einem ersten Zeitpunkt;


b) Initialisierung der Wahrscheinlichkeitsdichte ( p) der zumindest einen
     zu bestimmenden Zustandsgröße zum ersten Zeitpunkt;


c) Prädiktion der Wahrscheinlichkeitsdichte ( p) der zumindest einen zu
     bestimmenden Zustandsgröße zu einem nach dem ersten Zeitpunkt
     gelegenen nächsten Zeitpunkt;


d) Überprüfen, ob Messdaten vorliegen, die zu einer Berechnung der
     Wahrscheinlichkeitsdichte ( p) der zumindest einen zu bestimmenden
     Zustandsgröße herangezogen werden können, und,


d´) falls derartige Messdaten vorliegen, Neuberechnung der Wahrscheinlichkeitsdichte ( p) mit diesen Messdaten;


e) Berechnen der Vorhersagewerte der zu bestimmenden Zustandsgröße(n) aus der Wahrscheinlichkeitsdichte ( p) ;


f)   Ausgabe der berechneten Vorhersagewerte an eine nachgeordnete
     Datenverarbeitungseinrichtung;


g) Wiederholen der Schritte c) bis f);


dadurch gekennzeichnet,

                                          -6-



        h) dass die Schritte


            h1) der Initialisierung der Wahrscheinlichkeitsdichte [Schritt b)],


            h2) der Prädiktion der Wahrscheinlichkeitsdichte [Schritt c)],


            h3) der Neuberechnung der Wahrscheinlichkeitsdichte [Schritt d´)]
                    und


            h4) der Berechnung der Vorhersagewerte [Schritt e)]


            h5´) durch Diskretisierung der Wahrscheinlichkeitsdichte ( p) auf dünnen Gittern durchgeführt werden.“


In Hinblick auf die jeweils nebengeordneten auf ein „Computerprogramm“, ein
„Computerprogrammprodukt“, einen „Datenträger“ und eine „Vorrichtung“ gerichteten Patentansprüche 10 bis 13 sowie die Unteransprüche 2 bis 9 wird auf den
Akteninhalt verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag 1 enthält neben den Merkmalen a) bis
h4) gemäß Hauptantrag zusätzlich das Merkmal h5), welches das Merkmal h5´)
ersetzen soll:


        h5) „durch Diskretisierung der Wahrscheinlichkeitsdichte (p) auf dünnen
                 Gittern gemäß der Vorschrift von Zenger [Zenger, C.: Sparse Grids.
                 In W. Hackbusch (Hrsg.): Parallel Algorithms for Partial Differential
                 Equations. Braunschweig: Vieweg, 1991 (Notes on Numerical Fluid
                 Mechanics 31), Seiten 241 bis 251] durchgeführt werden.“


Die Patentansprüche 2 bis 13 sind mit den Patentansprüchen 2 bis 13 gemäß
Hauptantrag identisch.

                                         -7-



Der Patentanspruch 1 gemäß Hilfsantrag 2 unterscheidet sich vom Patentanspruch 1 gemäß Hilfsantrag 1 durch die Merkmale i) und j), die nach Merkmal h5)
angefügt werden sollen:


        i)   „und dass im Schritt b) vor der ersten Diskretisierung der Wahrscheinlichkeitsdichte Daten bereitgestellt werden, die die Anzahl der
             Gitterstellen und die Abstände zwischen den Gitterstellen für jede
             Dimension des dünnen Gitters definieren und so eine Dünngittereinheit bestimmen und dass ein zumindest eine Dünngittereinheit aufweisendes Dünngittergebiet definiert wird,


        j)   wobei am Rand der Dünngittereinheit keine Gitterstellen vorgesehen
             sind.“


In Hinblick auf die Patentansprüche 2 bis 12 wird auf die Akte verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag 3 enthält neben den Merkmalen des
Patentanspruchs 1 gemäß Hilfsantrag 2 noch die Merkmale k), l), e1), e2) und m),
n), e3), e4), die auf das Merkmal j) folgen sollen:


        k)   „dass vor Schritt c), vorzugsweise im Schritt b), die Definition einer
             von der Wahrscheinlichkeitsdichte abhängigen ersten Entscheidungsgröße erfolgt und


        l)   dass nach dem Schritt e) die folgenden Schritte durchgeführt werden:


        e1) Überprüfen, ob die erste Entscheidungsgröße auf einer Dünngittereinheit unter einem vorgegebenen Schwellenwert liegt und

                                      -8-



       e2) falls dies der Fall ist, Entfernen der überprüften Dünngittereinheit aus
             dem Dünngittergebiet,


       m)    dass vor Schritt c), vorzugsweise im Schritt b), die Definition einer
             von der Wahrscheinlichkeitsdichte abhängigen zweiten Entscheidungsgröße erfolgt und


       n)    dass nach dem Schritt e) beziehungsweise Schritt e2) die folgenden
             Schritte durchgeführt werden:


       e3) Überprüfen, ob die zweite Entscheidungsgröße in einem vorgegebenen Abstand zu einem Rand des Dünngittergebiets über einem vorgegebenen Schwellenwert liegt und


       e4) falls dies der Fall ist, Erweitern des Dünngittergebiets um zumindest
             eine Dünngittereinheit angrenzend an den betreffenden Rand des
             Dünngittergebiets.“


Der Patentanspruch 1 gemäß Hilfsantrag 4 enthält neben den Merkmalen des
Patentanspruchs 1 gemäß Hilfsantrag 3 noch das Merkmal o), das sich an Merkmal e4) anschließt:


       o)    „wobei bei der Erweiterung des Dünngittergebiets am Rand der
             Dünngittereinheit(en), an den eine weitere Dünngittereinheit angefügt
             wird, Gitter-Ergänzungsstellen eingefügt werden.“


Hinsichtlich der Patentansprüche 2 bis 10 gemäß Hilfsantrag 3 bzw. 4 wird wieder
auf den Akteninhalt verwiesen.


Die Anmelderin trägt vor, dass die Bedeutung der vorliegenden Erfindung darin
bestehe, militärische Flugkörper abfangen zu können. Solche Flugkörper führten

                                       -9-



oftmals nicht-lineare Bewegungen aus, um einer Berechenbarkeit ihrer Bahnbewegung zu entgehen. Um ihre Koordinaten zu bestimmen, müssten hochkomplexe
Berechnungen in einem vieldimensionalen Zustandsraum ausgeführt werden.
Damit die Berechnungen dennoch in Echtzeit bewerkstelligt werden könnten, sehe
die beanspruchte Lehre im Wesentlichen die Anwendung eines Dünngitterverfahrens vor, um die Rechenzeiten deutlich zu verkürzen.


Die jeweiligen Gegenstände nach Patentanspruch 1 gemäß Hauptantrag und
Hilfsantrag 1 bis 4 riefen somit einen technischen Effekt hervor und seien daher
dem Patentschutz grundsätzlich zugänglich. Sie seien außerdem nicht nur neu,
sondern beruhten auch auf erfinderischer Tätigkeit.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da die jeweiligen Gegenstände des Patentanspruchs 1 nach
Hauptantrag und Hilfsantrag 1 bis 4 nicht auf erfinderischer Tätigkeit beruhen (§ 1
Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung bezieht sich auf ein Verfahren und eine
Vorrichtung zur Verfolgung der Bewegungsbahn eines sich bewegenden Objekts.
Sie betrifft weiterhin ein Computerprogramm, welches dieses Verfahren implementiert sowie einen Datenträger mit einem derartigen Computerprogramm (Offenlegungsschrift, [0001]).


Wie in der Anmeldung ausgeführt, wird ein solches Verfahren, welches auch als
„Tracking“-Verfahren bezeichnet wird, dazu eingesetzt, um die Bewegungsbahn
von Flugkörpern selbst dann noch mit verhältnismäßig großer Genauigkeit bestimmen und die Bewegung des Flugkörpers vorhersagen zu können, wenn nur wenige und möglicherweise fehlerbehaftete Ortungen des Flugkörpers vorliegen. Sol-

                                      - 10 -



che Ortungen könnten beispielsweise mittels Radarmessungen von einer oder
mehreren Messeinrichtungen durchgeführt werden (Offenlegungsschrift, [0002]).
Laut Beschreibung sei unter Verwendung aller bis zu einem gegebenen Zeitpunkt
verfügbaren Messdaten zuallererst die aktuelle Position des Objekts zu bestimmen. Dies solle möglichst in Echtzeit erfolgen, da es zum Beispiel für die Bekämpfung eines anfliegenden Flugkörpers erforderlich sei, zumindest die aktuelle Position des Flugkörpers zu kennen und möglicherweise sogar die weitere Bewegungsbahn des Flugkörpers vorauszusagen (Offenlegungsschrift, [0003]). Neben
der Position des Flugkörpers sei man in der Regel aber auch an anderen Zustandsgrößen, wie z. B. dem Geschwindigkeitsvektor, den Parametern von Manövermodellen oder dem ballistischen Koeffizienten interessiert, denn ein anfliegender Flugkörper bewege sich nicht entlang einer linearen Bewegungsbahn mit
gleichmäßiger Geschwindigkeit, sondern werde in der Regel so gesteuert, dass er
taktische Manöver fliege. Würde das Objekt lediglich eine lineare Bewegung
beschreiben oder würden sich die Zustandsgrößen des Objekts in linearer Weise
ändern, so wäre bei normal verteilter Anfangsverteilung und normal verteilten
Messfehlern eine Berechnung mit relativ geringem Aufwand mittels Kalman-Filtern
durchführbar. In der Praxis würden sich die Zustände des Objekts jedoch in nichtlinearer Weise ändern. Ein Flugkörper könne etwa in einem Täuschungsmanöver
verzögern, beschleunigen oder abrupt die Richtung ändern, so dass eine Bahnbestimmung mit einer Kalman-Filterung nicht oder nur sehr ungenau möglich sei.
Würden dementsprechend die interessierenden Bewegungen und Zustandsgrößen des sich bewegenden Objekts durch nichtlineare Gleichungen beschrieben,
sei eine optimale Bestimmung des Schätzwerts in einer geschlossenen Form oftmals nicht möglich (Offenlegungsschrift, [0004]-[0006]). Eine exakte Behandlung
des Problems erfolge durch Betrachtung der bedingten Wahrscheinlichkeitsdichtefunktion, die die vollständige Information über die Bewegung des Objekts zu
einem Zeitpunkt enthalte. Die Dichtefunktion ergebe sich als Lösung einer stochastischen partiellen Differentialgleichung, die sowohl eine Komponente zur Vorhersage des Systemverhaltens ohne Verwendung von Messungen als auch eine
Komponente für den durch die Verwendung von Messungen erzielten Informati-

                                        - 11 -



onsgewinn beinhalte. Die Lösung einer derartigen Gleichung durch numerische
Verfahren auf regulären Gittern von Stützstellen habe aber den Nachteil, dass die
für mehrdimensionale Probleme (d. h. ab vier Dimensionen im Zustandsraum) benötigte Rechenzeit schnell anwachse, weil der Rechenaufwand mit der Anzahl der
Dimensionen exponentiell ansteige (Offenlegungsschrift, [0010]-[0020]).


Die der Anmeldung zugrundeliegende Aufgabe sieht der Senat darin, ein Verfahren anzugeben, welches die Werte von Zustandsgrößen, die die Bewegung eines
Objekts, z. B. eines Flugkörpers, zu verschiedenen Zeitpunkten beschreiben,
selbst für höhere Dimensionen in Echtzeit rechnerisch voraussagt.


Als Fachmann, der mit der Aufgabe betraut wird, ein Tracking-Verfahren für sich
bewegende Objekte, z. B. Flugkörper zu verbessern, ist ein berufserfahrener Ingenieur der Fachrichtung Elektrotechnik anzusehen, welcher nicht nur über fundierte
Kenntnisse in der funkbasierten Flugzeugortung und -abstandsmessung verfügt,
sondern auch mit der Anwendung numerischer Lösungsmethoden zur Bestimmung von Bahnbewegungen vertraut ist.


2.    Die jeweiligen Gegenstände des Patentanspruchs 1 gemäß Hauptantrag
sowie Hilfsantrag 1 und 2 beruhen nicht auf erfinderischer Tätigkeit.


2.1   Zur Lehre des Patentanspruchs 1


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hauptantrag ein Verfahren zur Verfolgung der Bewegungsbahn eines sich bewegenden Objekts vor. Bei dem bewegten Objekt kann es sich insbesondere um
einen Flugkörper handeln, der geortet und dessen Bahn nachverfolgt werden soll.
Das Verfahren ist als Software implementiert und läuft auf einer Recheneinrichtung ab (Offenlegungsschrift, [0050]; Fig. 2).

                                      - 12 -



Laut Beschreibung werden die für die Berechnung nötigen Eingabedaten in einem
Speicher abgelegt. Außerdem werden alle erforderlichen Initialisierungen vorgenommen (Offenlegungsschrift, [0051]). Merkmal a) besagt hierzu konkret, dass
Daten bereitgestellt werden sollen, die wenigstens eine Zustandsgröße des sich
bewegenden Objekts zu einem ersten Zeitpunkt beschreiben. Die zumindest eine
zu bestimmende Zustandsgröße soll die Bewegung des Objekts beeinflussen.
Laut Merkmal b) soll die Wahrscheinlichkeitsdichte der zumindest einen Zustandsgröße initialisiert werden.


Merkmal c) besagt, dass die Wahrscheinlichkeitsdichte der wenigstens einen Zustandsgröße für einen nächstfolgenden Zeitpunkt vorhergesagt wird („Prädiktion“).
In der Beschreibung wird hierzu ausgeführt, dass die Vorhersage der Bewegung
jeweils zu diskreten Zeitpunkten berechnet wird. Die Vorhersage des Systemverhaltens erfolgt an dieser Stelle ohne Verwendung von Messungen durch Lösung
der Fokker-Planck-Gleichung (Offenlegungsschrift, [0017]).


In Merkmal d) wird überprüft, ob Messdaten vorliegen, die noch zur Berechnung
der Wahrscheinlichkeitsdichte herangezogen werden können.


Falls solche Messdaten vorliegen, wird die Wahrscheinlichkeitsdichte unter Verwendung dieser Daten neu berechnet bzw. korrigiert (Merkmal d´)). Das Merkmal
trägt im Wesentlichen dem Mess-Term aus der in der Beschreibung genannten
stochastischen partiellen Differentialgleichung Rechnung (Offenlegungsschrift,
[0016], [0018]).


Auf Grundlage der (mit oder ohne Messwertkorrektur) berechneten Wahrscheinlichkeitsdichte werden Werte für die zu bestimmenden Zustandsgrößen vorhergesagt (Merkmal e)).


Die berechneten Vorhersagewerte werden noch an eine Datenverarbeitungseinrichtung ausgegeben (Merkmal f)).

                                        - 13 -



Die in den Merkmalen c) bis f) genannten Verfahrensschritte werden wiederholt
(Merkmal g)), und zwar über die jeweils betrachtete Zeit im Zustandsraum, d. h.
über den gesamten Lösungszeitraum hinweg.


Die Merkmalsgruppe h) besagt, dass Initialisierung, Prädiktion und Neuberechnung der Wahrscheinlichkeitsdichte sowie die Berechnung der Vorhersagewerte
der Zustandsgrößen mittels eines Dünngitterverfahrens durchgeführt werden sollen (Merkmale h1) bis h5´)). Damit ist gemeint, die relevanten stochastischen partiellen Differentialgleichungen nicht auf regulären, sondern auf dünnen Gittern zu
lösen. Solche dünnen Gitter weisen laut Beschreibung eine deutlich geringere
Komplexität auf, wodurch für einen mehrdimensionalen Zustandsraum deutlich
kürzere Rechenzeiten als für gewöhnliche Gitter erzielt werden können (Offenlegungsschrift, [0025]).


In Patentanspruch 1 gemäß Hilfsantrag 1 wurde das Merkmal h5´) gegen das
Merkmal h5) ausgetauscht. Demnach soll die Wahrscheinlichkeitsdichte auf einem
speziellen Typ von dünnen Gittern diskretisiert werden, wie er in dem Fachartikel
„Sparse Grids“ von C. Zenger konkretisiert und mathematisch beschrieben wird.
Während in Figur 1 der Offenlegungsschrift ein Beispiel eines einzelnen zweidimensionalen dünnen Gitters, das eine Dünngittereinheit repräsentiert, wiedergegeben ist, zeigt Figur 3 ein aus mehreren Dünngittereinheiten aufgebautes Dünngittergebiet.


Das im Patentanspruch 1 gemäß Hilfsantrag 2 neu hinzugekommene Merkmal i)
sieht vor, dass vor der ersten Diskretisierung der Wahrscheinlichkeitsdichte zunächst eine Dünngittereinheit bestimmt werden soll. Zu diesem Zweck werden für
jede Dimension des dünnen Gitters sowohl eine Anzahl von Gitterstellen als auch
die Abstände zwischen den Gitterstellen festgelegt. Außerdem wird für die Berechnung ein ganzes Dünngittergebiet definiert, das wenigstens eine Dünngittereinheit
umfassen soll. Das neue Merkmal j) besagt, dass sich am Rand der Dünngittereinheit keine Gitterstellen befinden sollen.

                                      - 14 -



2.2   Die Würdigung des eingeführten Standes der Technik ergibt, dass die mit
dem jeweiligen Patentanspruch 1 gemäß Hauptantrag sowie Hilfsantrag 1 und 2
beanspruchten Gegenstände für den Fachmann nahegelegen haben. Dies gilt
selbst dann, wenn der Prüfung der gesamte Patentanspruch mit allen seinen
Merkmalen zugrunde gelegt wird. Damit kann dahingestellt bleiben, ob die beanspruchten Gegenstände gemäß § 1 Abs. 3 i. V. m. Abs. 4 PatG vom Patentschutz
ausgeschlossen sind, und ob der jeweilige Patentanspruch 1 Merkmale enthält,
die nicht die Lösung eines technischen Problems mit technischen Mitteln bestimmen oder beeinflussen und somit bei der Prüfung der erfinderischen Tätigkeit nicht
zu berücksichtigen sind (BGH GRUR 2011, 125 - Wiedergabe topografischer
Informationen).


2.2.1 Zur Beurteilung der beanspruchten Lehre sind die Druckschriften D3 und
D4 von besonderer Bedeutung.


Die Druckschrift D3 beschreibt ein Verfahren zur Verfolgung eines Zielobjekts,
welches insbesondere auf der Anwendung anpassungsfähiger Gitter und dünn besetzter Tensoren im Zustandsraum beruht (Abstract). Das bekannte Verfahren ist
geeignet für Objektverfolgung mittels Radar, d. h. funkbasierte Flugzeugortung
und -abstandsmessung, und umfasst die rechnerische Vorhersage von Wahrscheinlichkeitsdichten und deren Korrektur durch Berücksichtigung von Messwerten für jeweils aufeinanderfolgende Zeitpunkte (Seite 4 Abschnitt 4.2 - „Sparse
Grid Solution based on Transition Probability Tensor Pre-Computation“, vgl. insbesondere Gleichungen (5) und (6)).


Somit offenbart die Druckschrift D3 ein computerimplementiertes Verfahren, welches der Verfolgung der Bewegungsbahn eines Objekts dient (Abstract; Seite 1,
Abschnitt 1 - Introduction, z. B. letzter Absatz, siehe „… solving a radar tracking
problem in Section 4“).

                                        - 15 -



Zur Bestimmung von Zustandsgrößen des Objekts, wie z. B. Ort, Geschwindigkeit
wird in der Druckschrift D3 ein Modell für eine radargestützte Zielverfolgung aufgestellt (Seite 3, Abschnitt 4.1 - „A Standard Radar Tracking Model“). Das Modell
erlaubt die näherungsweise Berechnung einer Zustandsgröße x i zu einem Zeit-

punkt t  T aus dem Wert derselben Größe zum vorangegangenen Zeitpunkt t .
Dass zum vorhergehenden Zeitpunkt t überhaupt Daten der Zustandsgröße vorhanden sein müssen, wird vom Fachmann mitgelesen (Merkmal a)).


Ausgehend von dem aufgestellten Modell wird eine Wahrscheinlichkeitsdichte in
Form eines Tensors P mit Übergangswahrscheinlichkeiten aus einem vergangenen Zustand in einen Zustand zu einem nächsten Zeitpunkt vorhergesagt. Der
Tensor und damit auch die Wahrscheinlichkeitsdichte sind dabei zeitunabhängig
(Seite 4, Abschnitt 4.2 - Sparse Grid Solution based on Transition Probability Tensor Pre-Computation, siehe „prediction step“ und Gleichung (5) – Merkmal c)).


Mit Hilfe von Messergebnissen wird eine bedingte Übergangswahrscheinlichkeit p
berechnet, die die vorhergesagten Übergangswahrscheinlichkeiten korrigiert (Seite 4, Abschnitt 4.2, siehe „measurement correction step“ - Merkmal d´)).


Die Größe u k 1 repräsentiert die Vorhersagewerte der zu bestimmenden Zu-

standsgrößen aus den geänderten Übergangswahrscheinlichkeiten bzw. Wahrscheinlichkeitsdichten (Seite 4, Gleichung (6)). Merkmal e) ist damit verwirklicht.


Die numerischen Resultate des in der Druckschrift D3 vorgestellten, und auf einer
Datenverarbeitungsanlage durchgeführten Rechenverfahrens werden in Diagrammen ausgegeben bzw. dargestellt (Seiten 9-10, Figuren 6, 7). Somit ergibt sich
auch Merkmal f) aus der Druckschrift D3.


Vorhersage und Korrektur von Übergangswahrscheinlichkeiten bzw. Zustandsgrößen für viele aufeinanderfolgende Zeitpunkte rekursiv zu wiederholen, stellt einen

                                         - 16 -



grundlegenden Bestandteil des in der Druckschrift D3 verwendeten „Prediction-Correction“ Algorithmus dar (Seite 2, Abschnitt 2 - Discrete-Time Nonlinear Filtering: A Review; Seite 4, Abschnitt 4.2, siehe „prediction step“ und „measurement
correction step“ - Merkmal g)).


Die Vorhersage („prediction step“) der zeitunabhängigen Übergangswahrscheinlichkeit („transition probability tensor“), d. h. einer Wahrscheinlichkeitsdichte (Seite 4, Gleichung (5)), deren Korrektur bzw. Neuberechnung („measurement correction step“; Seite 4, Gleichung (6)) sowie die Berechnung der Vorhersagewerte für
die relevanten Zustandsgrößen (Seite 4, Gleichung (6); siehe u k 1 ) erfolgt mittels

eines Dünngitterverfahrens, das auf der Verwendung anpassungsfähiger Gitter in
Polarkoordinaten basiert (Seiten 7-8, Abschnitt 6 - „Adaptive Uniform Polar Grid“;
Seite 10, Abschnitt 8 - „Conclusions and Future Work“, erster Absatz - Merkmalsgruppe h) mit h2), h3), h4) und h5´)).


Einem Objekt oder einer Variablen innerhalb eines Programmablaufs einen Initialoder Anfangswert zuzuweisen, ist aus Sicht des Fachmannes ein notwendiger
Schritt, um für diese einen definierten Ausgangszustand schaffen zu können.
Dementsprechend stellt es für ihn eine selbstverständliche Maßnahme dar, im
Sparse Grid Filter der Druckschrift D3 die Übergangswahrscheinlichkeit P (Seite 4, Gleichung (5)) mit Anfangswerten vorzubelegen, und zwar sinnvollerweise in
Übereinstimmung mit der diskreten Aufteilung der Stützstellen des jeweils gewählten dünnen Gitters (Merkmal b) und Merkmalsgruppe h) mit h1) und h5´)).


Von der aus der Druckschrift D3 bekannten Lehre unterscheidet sich die Lehre
nach Patentanspruch 1 gemäß Hilfsantrag 2, der die jeweiligen Merkmale des
Patentanspruchs 1 gemäß Haupt- und Hilfsantrag 1 mit umfasst, nur noch durch
ein Überprüfen, ob überhaupt Messdaten vorliegen (Merkmal d)), die Anwendung
des Dünngitterverfahrens nach C. Zenger auf die Diskretisierung der Wahrscheinlichkeitsdichte (Merkmal h5)), die Bereitstellung von Daten zur Festlegung von

                                       - 17 -



Dünngittereinheit und -gebiet (Merkmal i)) sowie durch die Verwendung von Dünngittereinheiten, die keine Gitterstellen am Rand besitzen (Merkmal j)).


Der Fachartikel D4 („Sparse Grids“) behandelt eine Methode der dünnen Gitter,
die ein Verfahren zur Lösung mehrdimensionaler Integrale mittels eines Diskretisierungsschemas auf Basis eines besonderen Typs ausgedünnter Gitter darstellt,
wie sie von C. Zenger vorgeschlagen werden. Dabei werden z. B. in zwei Dimensionen die zu integrierenden Funktionen nicht über die gesamte Fläche, sondern
nur mittels derartiger Gitter approximiert. Während ein reguläres Gitter äquidistante Gitterpunkte in Richtung jeder Dimension besitzt, basiert diese Art von dünnen Gittern auf einer hierarchischen Basis (Seite 241, Fig. 1; Seite 244, Fig. 2;
Seite 247, Fig. 3). In der Druckschrift D4 wird die Lösung von Differentialgleichungen am Beispiel der Laplace Gleichung beschrieben (Seite 249). Wahrscheinlichkeitsdichten auf dünnen Gittern gehen aus ihr allerdings nicht hervor (teilweise
Merkmal h5)).


Der Lösung der Differentialgleichung und somit auch der Diskretisierung der jeweils gesuchten Funktion geht die Konstruktion eines dünnen Gitters voraus, dessen Gitterstellen, deren Anzahl und Abstände voneinander für jede Dimension
durch Angabe der Basisfunktionen des Gitters bestimmt werden (Seite 241, Fig. 1;
Fig. 3). Die Druckschrift D4 lehrt somit auch, vor der eigentlichen Integration Daten
bereitzustellen, die Dünngittereinheiten und darauf aufbauende Dünngittergebiete
festlegen (Fig. 3, Fig. 4 - teilweise Merkmal i)), allerdings wiederum ohne auf
Wahrscheinlichkeitsdichten Bezug zu nehmen.


2.2.2 Die jeweiligen Gegenstände des Patentanspruchs 1 gemäß Hauptantrag
sowie Hilfsantrag 1 und 2 ergeben sich durch eine Zusammenschau der Druckschriften D3 und D4.


Aus der Druckschrift D3 entnimmt der Fachmann, dass das dort vorgestellte Tracking-Verfahren durch den Einsatz effektiver Integrationsmethoden weiter be-

                                       - 18 -



schleunigt werden kann (Seite 10, zweiter Absatz, siehe „Finally, the integration
step can be speeded up using Monte Carlo integration methods“).


Aufgrund des gegebenen Hinweises hatte er Veranlassung, sich auf dem Spezialgebiet numerischer Integrationsmethoden kundig zu machen oder entsprechenden
Rat einzuholen, wobei er dann zwangsläufig mit dem aus der Druckschrift D4
bekannten Dünngitterverfahren von C. Zenger konfrontiert wurde, das z. B. zur
Lösung elliptischer Differentialgleichungen gute Resultate liefert (Seiten 248, 249).
Für den Fachmann lag es daher auf der Hand, zur Erhöhung der Rechengeschwindigkeit die aus der Druckschrift D4 bekannten dünnen Gitter in Betracht
zu ziehen und auf die Rechenmethode der Druckschrift D3 anzuwenden, was in
der Folge u. a. zu einer Diskretisierung der Wahrscheinlichkeitsdichte auf Basis
der „Sparse Grids“ gemäß C. Zenger führt (restlicher Teil der Merkmale h5) und
i)).


In Hinblick auf die im Sparse Grid Filter der Druckschrift D3 vorgesehene und auf
Messdaten beruhende Korrektur („measurement correction step“) noch einen
Überprüfungsschritt bzw. eine Abfrage vorzusehen, ob denn überhaupt brauchbare Messdaten vorliegen, um für den Fall, dass keine oder nur fehlerbehaftete
Messdaten vorhanden sind (z. B. infolge von Defekten an Messgeräten), wenigstens mit den unkorrigierten Zustandsgrößen des „Prediction Steps“ weiterrechnen
zu können, stellt für den Fachmann eine naheliegende Maßnahme dar, um unerwünschte Systemunterbrechungen infolge unbrauchbarer Messwerte zu vermeiden (Merkmal d)).


Im Unterschied zu Druckschrift D4 (Fig. 3, Fig. 4) sind gemäß Merkmal j) nicht
Dünngittereinheiten mit, sondern ohne Rand vorgesehen, d. h. am Rand der jeweiligen Dünngittereinheiten sollen gerade keine Gitterstellen vorhanden sein.


Es liegt jedoch im Bereich des Wissens des Fachmannes, dass bei der Konstruktion eines dünnen Gitters Alternativen zur Verfügung stehen, die bekannte Vor-

                                        - 19 -



und Nachteile aufweisen. Der Fachmann kann am Rand einer Dünngittereinheit
Gitterpunkte anordnen (wie in Druckschrift D4, Seite 247, Fig. 3), um gerade am
Rand definierte Randbedingungen zu schaffen, dies führt jedoch zu einem erhöhten Speicherplatzbedarf. Zum anderen kann am Rand der Dünngittereinheit auf
Gitterstellen verzichtet werden, hierfür wird der Speicherplatzbedarf zwar reduziert, jedoch fehlen dann „Anschlussstellen“ hin zu benachbarten Dünngittereinheiten, die gegebenenfalls später eingefügt werden müssen. Für die Auswahl
einer der beiden ihm bekannten Möglichkeiten unter Abwägen der jeweiligen Vorund Nachteile und unter Inkaufnahme der entsprechenden Nachteile ist kein erfinderisches Zutun erforderlich.


Es waren für den Fachmann somit lediglich fachgemäße Überlegungen erforderlich, um in Kenntnis der Druckschriften D3 und D4 zu einem Verfahren mit sämtlichen Merkmalen des Patentanspruchs 1 in der Fassung des Hauptantrags sowie
der Hilfsanträge 1 und 2 zu gelangen.


3.    Die jeweiligen Gegenstände nach dem Patentanspruch 1 gemäß Hilfsantrag 3 und 4 beruhen nicht auf erfinderischer Tätigkeit.


3.1   Der Patentanspruch 1 gemäß Hilfsantrag 3 ist nicht günstiger zu bewerten
als der Patentanspruch 1 gemäß Hilfsantrag 2, da zumindest die Merkmale l), e1),
e2) sowie n), e3), e4) zu einer technischen Problemlösung nicht beitragen und
daher bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen
sind (BGH a. a. O. - Wiedergabe topografischer Informationen; BGH GRUR 2013,
275 - Routenplanung).


Der Patentanspruch 1 gemäß Hilfsantrag 3 umfasst sämtliche Merkmale des Patentanspruchs 1 gemäß Hilfsantrag 2, unterscheidet sich aber von diesem durch
die jeweiligen Merkmale k) bis e2) sowie m) bis e4).

                                          - 20 -



Merkmal k) besagt, dass vor der Prädiktion der Wahrscheinlichkeitsdichte (Merkmal c)) eine Entscheidungsgröße festgelegt werden soll, die von der Wahrscheinlichkeitsdichte abhängig ist. Nach Vorhersage der zu bestimmenden Zustandsgrößen wird dann überprüft, ob diese Entscheidungsgröße auf einer Dünngittereinheit
unter einem vorgegebenen Schwellenwert liegt (Merkmale l), e1)). Ist dies der Fall
so wird die betroffene Dünngittereinheit aus dem Dünngittergebiet entfernt (Merkmal e2)).


Außerdem soll noch eine weitere von der Wahrscheinlichkeitsdichte abhängige
Entscheidungsgröße definiert werden (Merkmal m)), anhand der entschieden wird,
ob das Dünngittergebiet am Rand erweitert werden soll. Liegt diese zweite Entscheidungsgröße innerhalb eines vorgegebenen Abstands zum Rand des Dünngittergebiets über einem gewissen Schwellenwert, so wird am Rand des Dünngittergebiets eine Dünngittereinheit hinzugefügt (Merkmale n), e3), e4)), das Dünngittergebiet insgesamt also vergrößert.


Die geschilderten Maßnahmen dienen laut Beschreibung dazu, das für die Berechnungen erforderliche Dünngittergebiet klein und damit auch die erforderliche
Gesamtrechenzeit gering zu halten, weil das Dünngittergebiet in seiner Ausdehnung an die Zustandsänderungen des sich bewegenden Objekts angepasst werden kann (Offenlegungsschrift, [0035], [0037]).


Um das den Zustandsberechnungen zugrundeliegende Gitter einzugrenzen und
außerdem an die Bewegungsbahn des Objekts anzupassen, sieht bereits die
Druckschrift D3 die Einführung von Entscheidungsgrößen vor. Bei diesen handelt
es sich zum einen um eine bedingte Wahrscheinlichkeitsdichte, die als auf eine
Gitterscheibe lokalisiert angenommen wird (Seite 5, letzter Absatz, siehe „the conditional probability density function is localized within a domain D(t k ) “; Fig. 2) und

damit deren Lage im Zustandsraum festlegt. Weitere Entscheidungsgrößen sind
die Standardabweichungen der Messwerte für die Entfernung und Richtung zum
Objekt, welche die Ausdehnung der Scheibe bestimmen und Gitterstellen dyna-

                                        - 21 -



misch ein- oder ausschließen (Seite 5, Gleichungen (9) und (10)). Zumindest die
Merkmale k) und m) sind damit im Tracking-Verfahren der Druckschrift D3 verwirklicht.


Die Anmeldung unterscheidet sich hiervon durch den Vorschlag, dass eine erste
bzw. zweite Entscheidungsgröße auf einer Dünngittereinheit bzw. in einem Abstand zum Rand des Dünngittergebiets relativ zu Schwellenwerten bewertet werden und danach entschieden wird, ob eine Dünngittereinheit weggenommen oder
am Rand des Gebiets hinzugefügt wird. Die Unterschiedsmerkmale zeigen, dass
sich die Lehre nach Patentanspruch 1 gemäß Hilfsantrag 3 von dem aus den
Druckschriften D3 und D4 bekannten Stand der Technik lediglich in der Formulierung und Anwendung eines speziellen mathematischen Entscheidungskriteriums
sowie in der hiervon abhängigen geometrischen Anordnung einer besonderen
Form von Gittereinheiten unterscheiden. Die Unterschiedsmerkmale beruhen somit allenfalls auf Überlegungen aus der mathematischen Logik und der Geometrie.
Sie setzen keine auf technischen Überlegungen beruhenden Erkenntnisse voraus
und sind daher bei der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen
(Merkmale l), e1), e2) und n), e3), e4)).


Daher ist für den Patentanspruch 1 gemäß Hilfsantrag 3 eine andere Beurteilung
als für den Patentanspruch 1 gemäß Hilfsantrag 2 nicht gerechtfertigt.


3.2    Auch der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 4 ist durch
den Stand der Technik nahegelegt.


Der Patentanspruch 1 gemäß Hilfsantrag 4 beinhaltet neben den Merkmalen des
Patentanspruchs 1 gemäß Hilfsantrag 3 noch das Merkmal o).


Dieses sieht vor, dass bei einer Erweiterung des Dünngittergebiets gemäß Merkmal e4) auf dem Rand, an dem eine Dünngittereinheit hinzugefügt wird, Gitter-Ergänzungsstellen angelegt werden. In der Beschreibung wird erläutert, dass sol-

                                         - 22 -



che Ergänzungsstellen null-, ein- oder mehrdimensional sind und Verbindungsbzw. „Klebestellen“ zwischen den Dünngittereinheiten bilden. Das Dünngittergebiet wird dementsprechend kachelartig aus den Dünngittereinheiten zusammengesetzt und bei Bedarf um einzelne Dünngittereinheiten erweitert oder verkleinert
(Offenlegungsschrift, [0058], Fig. 3).


Aus fachmännischer Sicht handelt es sich bei den Ergänzungsstellen um zusätzliche Gitterstellen, die die Stetigkeit der Wahrscheinlichkeitsdichtefunktion zwischen
den einzelnen Dünngittereinheiten garantieren sollen. Die Entscheidung darüber,
ob solche Gitterstellen verwendet werden müssen, orientiert sich in erster Linie an
mathematischen Notwendigkeiten für einen möglichst glatten Funktionenverlauf.
Sie beruht nicht auf technischen Überlegungen.


Nach allem vermochte der Einwand der Anmelderin, durch die Druckschrift D3
werde der Fachmann vom Gegenstand der Anmeldung eher weggeführt, nicht zu
überzeugen. Zwar ist der Anmelderin darin zuzustimmen, dass der aufgezeigte
Stand der Technik keinen direkten Hinweis auf die erfindungsgemäße „Kachelung“
bzw. die Anordnung von Dünngittereinheiten entlang der Bewegungsbahn des Objekts gibt. Jedoch beinhalten die entsprechenden Merkmale l) bis e2) und n) bis o)
keine auf technischen Überlegungen beruhenden Erkenntnisse und somit auch
keinen Teilaspekt, der ein technisches Problem bewältigt. Die genannten Merkmale sind bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen
(BGH a. a. O. - Wiedergabe topografischer Informationen), da ihnen lediglich
Überlegungen aus der Mathematik bzw. Geometrie zugrunde liegen.


Nach allem ist auch der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 4
aus dem aufgezeigten Stand der Technik nahegelegt.


4.     Mit dem jeweils nicht patentfähigen Patentanspruch 1 des Hauptantrages
und der Hilfsanträge 1 bis 4 sind auch die auf diesen rückbezogenen Patentansprüche sowie die auf ein „Computerprogramm“, ein „Computerprogrammprodukt“,

                                      - 23 -



einen „Datenträger“ und eine „Vorrichtung“ gerichteten nebengeordneten Patentansprüche nicht schutzfähig, da über einen Antrag nur einheitlich entschieden
werden kann (BGH GRUR 1997, 120 - Elektrisches Speicherheizgerät; BGH
GRUR 2007, 862 - Informationsübermittlungsverfahren II).


5.    Für eine Zurückverweisung an das Deutsche Patent- und Markenamt bestand kein Anlass, da die Sache entscheidungsreif war.


6.    Die Beschwerdegebühr ist gemäß § 80 Abs. 3 PatG zurückzuzahlen.


In ihrer Eingabe ist die Anmelderin auf die Argumentation der Prüfungsstelle im
vorangegangenen Prüfungsbescheid eingegangen und hat hilfsweise eine Anhörung beantragt. Die Anmeldung wurde mit den ursprünglichen Patentansprüchen
weiterverfolgt. Nach dem ersten Prüfungsbescheid erfolgte der Zurückweisungsbeschluss, in welchem die Durchführung einer Anhörung mit der Begründung
abgelehnt wurde, dass der sachliche Gehalt des Patentbegehrens unstrittig sei
und unterschiedliche Sichtweisen somit lediglich bezüglich des Zutreffens der Ausschlusskriterien des § 1 PatG existierten. Durch den Bescheid der Prüfungsstelle
sei der Anmelderin bereits ausreichend rechtliches Gehör gewährt worden, so
dass eine Anhörung aus Gründen der Verfahrensökonomie als nicht sachdienlich
angesehen werde.


Wie der Senat in früheren Entscheidungen bereits mehrfach dargelegt hat, war
das Prüfungsverfahren in solchen Fällen regelmäßig mängelbehaftet; es kann
nicht ausgeschlossen werden, dass dieser Mangel ursächlich für die Beschwerdeerhebung war (vgl. etwa 17 W (pat) 74/07, 17 W (pat) 86/07, 17 W (pat) 113/07,
17 W (pat) 76/09, 17 W (pat) 83/10, 17 W (pat) 32/12).


Es entspricht daher der Billigkeit, die Beschwerdegebühr zurückzuzahlen.

                                            - 24 -



                                              III.


Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde der Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamtes zurückzuweisen.




                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
      kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.



Dr. Morawek                    Eder                   Baumgardt                   Dr. Forkel



                                                                                       Me/Fa
