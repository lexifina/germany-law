---
ecli: "ECLI:DE:BPatG:2014:270514B17Wpat93.10.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 93/10"
decided: "2014-05-27"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=32&nr=26171&anz=1119&pos=481&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-05-27_17_W-pat_93_10_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 93/10 vom 2014-05-27

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 93/10                                                     Verkündet am
_______________                                                       27. Mai 2014
    (Aktenzeichen)                                                          …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2008 013 909.2-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 27. Mai 2014 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,      der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                          -2-



beschlossen:


                       Die Beschwerde wird zurückgewiesen.




                                     Gründe:


                                           I.


Die vorliegende Patentanmeldung ist am 12. März 2008 beim Deutschen Patentund Markenamt unter der Bezeichnung


     „Verfahren und Bildsegmentierungseinrichtung zur Segmentierung von
          Bilddaten, bildgebendes System und Computerprogrammprodukt“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat in der Anhörung am 22. Juni 2010 die
Anmeldung zurückgewiesen, da der Gegenstand des Patentanspruchs 1 nach
dem (damals geltenden) Haupt- und Hilfsantrag nicht auf erfinderischer Tätigkeit
beruhe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


          den angegriffenen Beschluss aufzuheben und das nachgesuchte
          Patent mit folgenden Unterlagen zu erteilen:


          gemäß Hauptantrag mit
          Patentansprüchen 1 bis 20 und

                                        -3-



        Beschreibung Seiten 1 bis 27, jeweils vom 26. Mai 2014,
        5 Blatt Zeichnungen mit Figuren 1 bis 13 vom Anmeldetag;


        gemäß 1. Hilfsantrag mit
        Patentansprüchen 1 bis 20 und
        Beschreibung Seiten 1 bis 27, jeweils vom 26. Mai 2014,
        im Übrigen wie Hauptantrag;


        gemäß 2. Hilfsantrag mit
        Patentansprüchen 1 bis 18 und
        Beschreibung Seiten 1 bis 29, jeweils vom 26. Mai 2014,
        im Übrigen wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: US 2004/0008886 A1

        D2: Yuri Boykov, Vladimir Kolmogorov: “An Experimental Comparison of
        Min-Cut/Max-Flow Algorithms for Energy Minimization in Vision”, IEEE
        Transactions on Pattern Analysis and Machine Intelligence, Vol. 26, No. 9,
        Sept. 2004, pp 1124 bis 1137

        D3    Nobuyuki Otsu: “A Threshold Selection Method from Gray-Level
        Histograms”, IEEE Transactions on Systems, Man and Cybernetics 9
        (1979), No. 1, pp.62-66.


Vom Senat wurde zusätzlich die Druckschrift


        D4: US 2003/0152262 A1


eingeführt.

                                       -4-



Zu den Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da der Gegenstand des Patentanspruchs 1
nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1
PatG).


1.       Die Patentanmeldung betrifft ein Verfahren zur Segmentierung von Bilddaten, insbesondere von mittels eines medizintechnischen bildgebenden Geräts
erzeugten Bilddaten vom Inneren eines Untersuchungsobjekts, zur Separation
zumindest einer Zielstruktur. Darüber hinaus betrifft die Anmeldung eine hierfür
nutzbare Bilddatensegmentierungseinrichtung sowie ein bildgebendes System mit
einer solchen Bilddatensegmentierungseinrichtung und ein Computerprogrammprodukt, mit dem das Verfahren durchführbar ist.


Zum Hintergrund der Anmeldung ist auf S. 1 le. Abs. bis S. 4 Abs. 1 der ursprünglich eingereichten Beschreibung ausgeführt, dass bei der zeitnah mit einer medizinischen Untersuchung stattfindenden Weiterverarbeitung von medizinischen Bilddaten (Serien mit einer Vielzahl von Schnittbildern oder mit dreidimensionalen
Volumenbilddaten, die etwa mittels Computertomografie erzeugt wurden) die Segmentierung von bestimmten Zielstrukturen eine wesentliche Rolle spiele. Hierbei
würden Teilobjekte eines Untersuchungsobjekts, etwa ein Herz oder eine Herzkammer von den übrigen Bilddaten separiert. Dies sei z. B. bei der Operationsplanung wichtig.
Zur Segmentierung von Bilddaten würden im medizinischen Bereich oft Regionenwachstumsverfahren eingesetzt. Hierbei werde versucht, die Umgebung eines
Bildpunkts in die Beurteilung mit einzubeziehen, ob der betreffende Bildpunkt zu
einer bestimmten Struktur gehöre. Dabei werde zunächst ein Startpunkt ermittelt.

                                       -5-



Der zentrale Teil des Regionenwachstumsverfahrens bestehe dann darin, die umliegenden Bildpunkte zu untersuchen und bei Erfüllung eines bestimmten Kriteriums den Bildpunkt der Struktur des Startpunkts zuzuordnen. Dieses Verfahren
werde für jeden neuen Bildpunkt wiederholt, so dass nach und nach eine Region
aus zusammenhängenden Bildpunkten, ein sogenannter „Cluster“, anwachse.
Könne die Zielstruktur nicht erweitert werden, weil z. B. kein Bildpunkt in der Umgebung des Clusters die Bedingung erfüllt, so sei das Verfahren beendet oder es
müsse ein neuer Startpunkt gesetzt werden.
In der Regel werde als Kriterium, ob ein bestimmter untersuchter Bildpunkt zum
Cluster hinzugenommen wird, eine Differenz der Intensitätswerte der benachbarten Bildpunkte herangezogen. In der Praxis neigten bei den bisher verwendeten
üblichen Regionenwachstumsverfahren die Cluster dazu, auch in Regionen einzufließen, die eigentlich nicht Teil der Zielstruktur seien. Um ein unerwünschtes Einfließen in andere Strukturen zu unterbinden, müssten wachstumsbegrenzende
Prozeduren angewendet werden. Diese seien jedoch an die jeweilige besondere
Problemstellung anzupassen und nicht generell anwendbar.
Um allgemein verwendbare Werkzeuge zur Generierung oder zumindest zur Korrektur von Segmentierungsmasken zu bieten, könnten halbautomatische Verfahren eingesetzt werden, die auf Bedienereingaben zurückgriffen, wobei anhand von
Angaben des Benutzers die Konturen der Zielregion lokalisiert würden. Beispielsweise könne der Bediener zuvor Grenzen um die Zielstruktur legen bzw. bestimmte Teilstrukturen durch geeignete Grenzlinieneingaben ausgrenzen. Solche
Methoden seien besser geeignet, um Regionen in zwei Dimensionen, z. B. in
zweidimensionalen Schnittbildern, voneinander abzugrenzen. Zwar sei es grundsätzlich möglich, solche Verfahren auch auf Verfahren zur dreidimensionalen Bilddatensegmentierungen zu übertragen, indem dreidimensionale Konturen aus mehreren in zweidimensionalen Bildern erzeugten Konturen zusammengesetzt würden. Jedoch sei es für unerfahrene Benutzer äußerst schwierig, intuitiv zu erkennen, in welchem Verhältnis eine bestimmte Grenzziehung in einem zweidimensionalen Bild letztlich zu welchen Segmentierungsergebnissen im dreidimensionalen
Volumen führe. Darüber hinaus könne in Abhängigkeit von der Komplexität des

                                         -6-



segmentierten Objekts die Anzahl der benötigten Konturverläufe und somit auch
der einzelnen Eingabeschritte sehr hoch sein, was letztlich zu sehr langen Untersuchungs- und Auswertezeiten führen könne.


Durch die Lehre der Anmeldung soll die Aufgabe gelöst werden, ein verbessertes
Verfahren zur Segmentierung von Bilddaten, insbesondere auch dreidimensionalen Bilddaten, sowie eine geeignete Bilddatensegmentierungseinrichtung zu schaffen, mit der schneller und sicherer eine bessere Separation einer Zielstruktur von
anderen Strukturen in den Bilddaten erreicht wird (S. 5 Abs. 2 der jeweiligen
Beschreibung gemäß Hauptantrag und gemäß dem ersten und zweiten Hilfsantrag).


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 gemäß
Hauptantrag betrifft ein


         1. Verfahren zur Segmentierung von Bilddaten (B) zur Separation zumindest einer Zielstruktur (Z)

         a) mittels eines Regionenwachstumsverfahrens auf Basis eines Graphen (G), der Knoten (K) aufweist, die jeweils einen Bilddatenpunkt oder
         eine Gruppe benachbarter Bilddatenpunkte repräsentieren, und Kannten (E) aufweist, die jeweils eine Konnektivität zwischen benachbarten
         Knoten (K) repräsentieren, bei dem

         b) die Bilddaten (B) und/oder der Graph (G) mittels einer graphischen
         Benutzerschnittstelle (11, 13) visualisiert werden,

         c) zur Gewinnung eines Startpunkts (S1) für das Regionenwachstumsverfahren mittels der graphischen Benutzerschnittstelle (11, 13) eine Markierung eines Knotens (K) erfasst wird, welcher Knoten (K) als Startpunkt (S1) herangezogen wird und

                                        -7-



       d) das Regionenwachstumsverfahren automatisch so lange durchgeführt
       wird, wie eine Betätigung eines bestimmten Bedienelements (11L) einer
       Benutzerschnittstelle (11) detektiert wird, wobei gleichzeitig mittels der graphischen Benutzerschnittstelle durch Markierung von als zur Zielstruktur (Z) gehörig akzeptierten Bilddatenpunkten und/oder Knoten (K) das
       Fortschreiten des Regionenwachstumsverfahrens in diskreten Schritten
       visualisiert wird.


Im Anspruch 1 nach dem 1. Hilfsantrag ist Merkmal d) ersetzt durch


       d‘) das Regionenwachstumsverfahren automatisch so lange durchgeführt
       wird, wie eine Betätigung eines bestimmten Bedienelements (11L) einer
       Benutzerschnittstelle (11) detektiert wird, wobei gleichzeitig mittels der graphischen Benutzerschnittstelle durch Markierung von als zur Zielstruktur (Z) gehörig akzeptierten Bilddatenpunkten und/oder Knoten (K) das
       Fortschreiten des Regionenwachstumsverfahrens in diskreten Schritten
       mit maximal 4 Schritten pro Sekunde visualisiert wird.


Im Anspruch 1 nach dem 2. Hilfsantrag ist zusätzlich hierzu vorgesehen, dass


       e) in einem Schrumpfungsmodus mittels eines inversen Regionenwachstumsverfahrens geprüft wird, ob bereits als zur Zielstruktur (Z) gehörige
       markierte Knoten (K) oder Bilddatenpunkte nicht zur Zielstruktur (Z) gehören und dabei schrittweise von den als nicht zur Zielstruktur gehörig ermittelten Knoten (K) und/oder Bilddatenpunkten die Markierung wieder aufgehoben wird,

       f)   wobei eine Schrittgeschwindigkeit der im Schrumpfungsmodus visualisierten diskreten Schritte geringer ist als die Schrittgeschwindigkeit bei der
       Visualisierung des Regionenwachstumsverfahrens und/oder wobei ein pro

                                        -8-



        Schritt im Schrumpfungsmodus visualisiertes Volumen geringer ist als ein
        pro Schritt im Regionenwachstumsverfahren visualisiertes Volumen.


Nach der Lehre der Anmeldung werden Bilddaten eines Untersuchungsobjekts als
Knoten eines Graphen repräsentiert, wobei jedem Knoten ein Bildpunkt oder eine
Gruppe von benachbarten Bildpunkten (mit den zugehörigen Intensitätswerten, im
Fall mehrerer Bildpunkte mit dem Mittelwert der Intensitätswerte) entspricht.
Benachbarte Knoten sind durch Kanten verbunden, welche die Konnektivität zwischen den Knoten angeben. Beispielsweise kann als Maß für die Konnektivität
zwischen benachbarten Knoten der Gradient herangezogen werden, wobei
benachbarte Knoten dann als zusammenhängend klassifiziert werden, wenn der
Betrag des Gradienten zwischen ihren Intensitätswerten unterhalb einer bestimmten Schwelle liegt, vgl. S. 4 Abs. 3 der ursprünglichen Beschreibung.
Die Bilddaten werden auf einem Bildschirm dargestellt, evtl. überlagert von einer
Darstellung des Graphen (Fig. 2). Ein Benutzer wählt über eine grafische Schnittstelle einen Knoten als Saatpunkt (engl. „seed point“) bzw. Startpunkt aus (S. 5
Abs. 2). Hiervon ausgehend wird schrittweise ein Regionenwachstumsverfahren
(engl. „region growing“) durchgeführt, wobei jeweils die als zur Zielstruktur gehörig
erkannten Bildpunkte und/oder Knoten markiert angezeigt werden (Fig. 6 bis 9).
Das Verfahren wird solange schrittweise fortgesetzt, wie der Benutzer ein Bedienelement betätigt. Lässt der Benutzer das Bedienelement los, so wird das Verfahren gestoppt. Auf diese Weise kann der Benutzer das Verfahren anhalten, wenn
nach seiner Ansicht die gewünschte Region in etwa vollständig segmentiert wurde.


Die Visualisierungsgeschwindigkeit soll auf maximal vier Schritte pro Sekunde
begrenzt sein (vgl. das zusätzliche Merkmal des Anspruchs 1 gemäß dem ersten
Hilfsantrag).


Bei derartigen Verfahren kann es vorkommen, dass nach einer Reihe von Schritten die als zur Zielstruktur gehörig markierten Bereiche auch in Regionen einfließen bzw. überlaufen, die nicht Teil der Zielstruktur sind. Um dies zu korrigieren,

                                        -9-



kann ein (durch den Benutzer veranlasster) Schrumpfungsprozess durchgeführt
werden, wobei die vorher gesetzten Markierungen schrittweise aufgehoben werden. Werden die Schrumpfungsschritte mit relativ geringer Geschwindigkeit und/
oder in relativ feinen Abstufungen visualisiert, so erleichtert dies dem Benutzer die
genaue Einstellung der Grenze der gesuchten Zielstruktur (vgl. die zusätzlichen
Merkmale des Anspruchs 1 gemäß Hilfsantrag 2).


Als Fachmann sieht der Senat hier einen Informatiker der Fachrichtung Bildverarbeitung an, der Erfahrung in der Entwicklung von grafischen Benutzerschnittstellen, insbesondere für die Medizintechnik besitzt.


2.     Das Verfahren des Patentanspruchs 1 gemäß Hauptantrag ist nicht patentfähig, da es dem Fachmann durch das aus der Druckschrift D4 Bekannte nahegelegt war.
Entsprechendes gilt für die Verfahren des jeweiligen Patentanspruchs 1 gemäß
dem ersten und gemäß dem zweiten Hilfsantrag.


D4 beschreibt eine Segmentierung zumindest einer Zielstruktur aus zwei- oder
dreidimensionalen Bilddaten über ein Regionenwachstumsverfahren („region growing“, vgl. Abstract). Ein Benutzer wählt über eine Eingabeeinrichtung einen Saatpunkt aus (Abs. [0038]), d. h. er markiert einen Bilddatenpunkt als Saatpunkt,
wobei diese Markierung von einer grafischen Benutzerschnittstelle erfasst wird
und dieser Saatpunkt als Startpunkt herangezogen wird (vgl. auch Abs. [0044]
Satz 1) - teilweise Merkmal c. Ausgehend von diesem Saatpunkt wird ein iteratives
„region growing“ durchgeführt, wobei für die Zuordnung eines Pixels zu einer
Region die Nachbarschaft der Pixel und ein Homogenitätskriterium berücksichtigt
werden (Abs. [0039], [0040]). Um ein „Einbluten“ oder „Überfließen“ in andere
Regionen zu vermeiden, kann der Benutzer über die Bewegung einer Computermaus oder eines Trackballs (Eingabeeinrichtung) die Anzahl der Iterationen beeinflussen; er kann auch die Segmentierung stoppen, indem er aufhört, die Maus
oder den Trackball zu bewegen (Abs. [0042], [0043]). In jedem Iterationsschritt

                                       - 10 -



werden die Bilddaten und die segmentierte Region auf einem Display in einer
zwei- oder dreidimensionalen Bilddarstellung angezeigt (Fig. 4 bis 7; Fig. 11 bis
16) – Merkmale b), d) in der Alternative „Bilddaten“ bzw. „Bilddatenpunkte“.


Hinsichtlich des im Regionenwachstumsverfahrens verwendeten Homogenitätskriteriums ist in Abs. [0041] angegeben, dass verschiedene, dem Fachmann
bekannte Kriterien für die Zuordnung zur Region berücksichtigt werden können.
Zu derartigen dem Fachmann bekannten Kriterien zählen solche, welche Intensitätsunterschiede und damit die Konnektivität zwischen Bilddatenpunkten berücksichtigen, etwa Unterschiede zwischen jedem betrachteten Bilddatenpunkt und
dem Saatpunkt (Abs. [0039]), oder auch zwischen benachbarten Bilddatenpunkten. Damit waren die wesentlichen Verfahrensschritte des Merkmals a) (Regionenwachstumsverfahren auf Basis von Bilddatenpunkten und der Konnektivität zwischen benachbarten Bilddatenpunkten) für den Fachmann zumindest naheliegend.
Bei der Verwendung eines Graphen mit Knoten, die Bilddatenpunkten entsprechen
können, handelt es sich lediglich um eine mathematische Einkleidung eines bekannten Regionenwachstumsverfahrens, die die Verwendung einer bestimmten
Art von Datenstruktur vorsieht, welche aber an den einzelnen Schritten eines solchen Verfahrens nichts ändert, nicht zur Lösung eines technischen Problems mit
technischen Mitteln beiträgt und daher nach gefestigter Rechtsprechung des Bundesgerichtshofs bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen ist (BGH GRUR 2011, 125 - Wiedergabe topografischer Informationen).
Damit sind die restlichen Teile der Merkmale a) und c) bei der Beurteilung der
erfinderischen Tätigkeit nicht zu berücksichtigen.


Nach alledem beruht das Verfahren des Anspruchs 1 gemäß Hauptantrag nicht
auf erfinderischer Tätigkeit.


Zudem wird im aus D4 bekannten Verfahren das Regionenwachstumsverfahren
automatisch so lange durchgeführt, wie der Benutzer das Bedienelement betätigt,

                                       - 11 -



insbesondere solange er die Computermaus bewegt; hierbei kann in Antwort auf
eine detektierte Bewegung jeweils eine festgelegte Anzahl (z. B. fünf) von Iterationen durchgeführt werden (Abs. [0045]). Die Wahl einer geeigneten Geschwindigkeit für die Anzeige der Iterationsschritte lag dabei vollständig im Bereich fachüblichen Handelns. Insbesondere wählte der Fachmann diese Geschwindigkeit so
aus, dass ein menschlicher Betrachter dem Iterationsverlauf bequem folgen kann,
wobei er bei Bedarf die Ergebnisse mehrerer schnell aufeinander folgender Iterationsschritte für die Visualisierung zusammenfasste. In der Wahl einer Visualisierungsgeschwindigkeit von maximal 4 Schritten pro Sekunde – Merkmal d') - kann
keine erfinderische Tätigkeit erkannt werden.


Auch das Verfahren des Anspruchs 1 gemäß dem 1. Hilfsantrag beruht nicht auf
erfinderischer Tätigkeit.


Des Weiteren kann im Verfahren der D4 eine zu weit ausgedehnte Region wieder
geschrumpft werden, wobei (in umgekehrter Weise zum Regionenwachstum) die
Markierung vorher als zur Region gehörig markierter Bilddatenpunkte schrittweise
aufgehoben wird, und wobei die ermittelte Region dargestellt wird (Abs. [0054],
[0063], Fig. 6 und 7, 15 und 16) – Merkmal e). Wie oben ausgeführt, lag es vollständig im Bereich fachüblichen Handelns, die Geschwindigkeit für die Visualisierung der Iterationen geeignet zu wählen. Insbesondere lag es für den Fachmann
nahe, diese Geschwindigkeit in den Wachstumsschritten relativ hoch zu wählen,
so dass eine schnelle Grobsegmentierung erzielt werden kann, und dann, wenn
das Verfahren sich in der Nähe der gesuchten Regionengrenze befindet, insbesondere wenn das Verfahren (bevor der Benutzer es gestoppt hat) bereits etwas
über die gesuchte Regionengrenze „hinausgeschossen“ ist, zur Feinsegmentierung die Geschwindigkeit beim Schrumpfen herabzusetzen, um dem Benutzer
eine möglichst genaue Bestimmung dieser Grenze zu ermöglichen – Merkmal f).


Auch das Verfahren des Anspruchs 1 gemäß dem 2. Hilfsantrag beruht damit nicht
auf erfinderischer Tätigkeit.

                                      - 12 -



Da das jeweilige Verfahren des Anspruchs 1 gemäß dem ersten und gemäß dem
zweiten Hilfsantrag auch bei Berücksichtigung der die Visualisierung einschließlich
deren Geschwindigkeit betreffenden Teile der Merkmale d') und f) nicht patentfähig
ist, kann es dahinstehen, ob diese Merkmale zur Lösung eines technischen Problems mit technischen Mitteln beitragen und bei der Beurteilung der erfinderischen
Tätigkeit zu berücksichtigen sind.


Die Anmelderin bringt vor, beim Verfahren der D4 müsse der Benutzer durch ständige Bewegung der Computermaus bestimmen, ob das Verfahren fortschreitet, er
müsse die Region quasi „ausmalen“. Im Gegensatz dazu erfordere das Verfahren
der vorliegenden Patentanmeldung lediglich das Drücken auf eine Taste. Zudem
werde beim anmeldungsgemäßen Verfahren durch die langsamere Geschwindigkeit beim Schrumpfen der gesamte Prozess (paradoxerweise) beschleunigt. Dies
stelle einen Paradigmenwechsel dar.


Dieser Argumentation war nicht zu folgen.


Das Bewegen einer Computermaus in D4 stellt (ebenso wie das Drücken auf eine
Taste im Ausführungsbeispiel der vorliegenden Patentanmeldung) eine Betätigung
eines Bedienelements dar und fällt somit unter das Merkmal d) bzw. d') des jeweiligen Anspruchs 1 nach Hauptantrag und nach den Hilfsanträgen 1 und 2. Im Übrigen gibt der Benutzer durch diese Betätigung lediglich vor, dass das Verfahren
fortschreiten soll; die Durchführung der Iterationsschritte erfolgt automatisch
anhand des gewählten Homogenitätskriteriums (ebenso wie in der vorliegenden
Anmeldung) und wird durch die Mausbewegung nicht beeinflusst (kein vom
Benutzer exakt zu steuerndes „Ausmalen“). Zudem lag wie oben erläutert die Auswahl unterschiedlicher Geschwindigkeiten für die Grob- und für die daran anschließende Feinsegmentierung völlig im Bereich fachüblichen Handelns. Es ist kein
über das Erwartbare hinausgehender, überraschender Effekt zu erkennen, der den
Wechsel von einer wissenschaftlich-technischen Grundauffassung zu einer anderen begründen könnte.

                                            - 13 -



Der Anspruch 1 gemäß Hauptantrag ist somit nicht gewährbar. Ebenso ist der
jeweilige Anspruch 1 gemäß dem ersten und gemäß dem zweiten Hilfsantrag nicht
gewährbar.


3.     Auch die übrigen Patentansprüche (2 bis 20 gemäß Hauptantrag, 2 bis 20
gemäß dem ersten Hilfsantrag, 2 bis 18 gemäß dem zweiten Hilfsantrag) sind
nicht gewährbar, da über einen Antrag nur einheitlich entschieden werden kann
(BGH in GRUR 1997, 120 „Elektrisches Speicherheizgerät“).




                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


        1.   das beschließende Gericht nicht vorschriftsmäßig besetzt war,
        2.   bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
                Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
                Befangenheit mit Erfolg abgelehnt war,
        3.   einem Beteiligten das rechtliche Gehör versagt war,
        4.   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
                sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
        5.   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
                die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
                sind, oder
        6.   der Beschluss nicht mit Gründen versehen ist.

                                         - 14 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                Eder              Dr. Thum-Rung                   Dr. Forkel




                                                                                     Fa
