---
ecli: "ECLI:DE:BPatG:2004:280904B17Wpat31.03.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 31/03"
decided: "2004-09-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=98&nr=19451&anz=2061&pos=1481&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-09-28_17_W-pat_31_03_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 31/03 vom 2004-09-28

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 31/03                                               Verkündet am
 _______________                                             28. September 2004
    (Aktenzeichen)                                                    …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 199 54 019.5-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. September 2004 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch und der Richter Dr. Schmitt,
Dipl.-Phys. Dr. Kraus und Dipl.-Ing. Prasch




BPatG 154
6.70

                                       -2-



beschlossen:


          Auf die Beschwerde wird der Beschluss der Prüfungsstelle
          für Klasse G 06 T des Deutschen Patent- und Markenamts
          vom 18. Dezember 2002 aufgehoben und die Sache unter
          Zugrundelegung der in der mündlichen Verhandlung am
          28. September 2004 überreichten und mit Hilfsantrag 5
          bezeichneten Patentansprüche 1 - 7 zur weiteren Prüfung an
          das Deutsche Patent- und Markenamt zurückverwiesen.


          Die weitergehende Beschwerde wird zurückgewiesen.
          Insoweit wird die Rechtsbeschwerde zugelassen.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung mit der Bezeichnung


               "Verfahren zur Durchwanderung eines Partitionsbaums“


ist am 10. November 1999 beim Deutschen Patent- und Markenamt eingereicht
worden.


Sie wurde von der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und
Markenamts mit Beschluss vom 18. Dezember 2002 zurückgewiesen. In diesem
Beschluss ist ausgeführt, dass die Gegenstände der Patentansprüche 1 gemäß
Hauptantrag, drittem und sechstem Hilfsantrag keine vollständige Lehre zur
Lösung der gestellten Aufgabe vermittelten und die Gegenstände der Patentan-

                                        -3-



sprüche 1 gemäß erstem, zweitem, vierten, fünften und siebten bis neunten Hilfsantrag nicht auf erfinderischer Tätigkeit beruhten.


Der Anmelder hat Beschwerde eingelegt und stellt den Antrag,


           den angefochtenen Beschluss aufzuheben und das nachgesuchte Patent mit folgenden Unterlagen zu erteilen:
           Patentansprüche 1 - 28 gemäß Hauptantrag,
           hilfsweise
           Patentansprüche 1 - 28 gemäß Hilfsantrag 1,
           weiter hilfsweise
           Patentansprüche 1 - 8 gemäß Hilfsantrag 2,
           zudem hilfsweise
           Patentansprüche 1 - 8 gemäß Hilfsantrag 3,
           ferner hilfsweise
           Patentansprüche 1 - 7 gemäß Hilfsantrag 4,
           und schließlich hilfsweise
           Patentansprüche 1 - 7 gemäß Hilfsantrag 5,
           sämtliche Anspruchsfassungen überreicht in der mündlichen
           Verhandlung am 28. September 2004, einer noch anzupassenden Beschreibung und 10 Blatt Zeichnungen mit Figuren 1 - 18 vom 13. November 2000.


Der Anspruch 1 gemäß Hauptantrag lautet:


           "Verfahren zur Durchquerung eines Partitionsbaums in Richtung einer Halbgeraden zur Anwendung bei der computergestützten strahlbasierten Generierung von digitalen Bildern
           (Ray Tracing), wobei der Parameter "Maximaltiefe" die Tiefe
           der Raumpartition bezeichnet, wobei 2Maximaltiefe die Kantenlänge des gesamten partitionierten Bereichs ist, wobei die

                            -4-



Halbgerade durch einen Startpunkt sowie einen Richtungsvektor gegeben ist, wobei der Richtungsvektor eine Hauptkomponente sowie Nebenkomponenten aufweist, und wobei
der Betrag jeder Nebenkomponente kleiner oder gleich dem
Betrag der Hauptkomponente ist,


gekennzeichnet durch folgende Schritte:


d)   Bestimmen der Abstände des Eintrittspunkts der Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;


f)   Dekrementieren der Abstände in Richtung der Hauptkomponente um 2n sowie der Abstände in Richtung der
     Nebenkomponenten um 2n x (Steigung m der jeweiligen
     Nebenkomponente), wobei n eine natürliche Zahl ist,
     wobei 2n nacheinander in absteigender Reihenfolge die
     Werte "Kantenlänge der terminalen Zelle", ... 2, 1
     annimmt, wobei ein Dekrementierungsschritt nur dann
     ausgeführt wird, wenn sowohl der ganzzahlige Anteil
     des Abstands in der Hauptkomponente als auch die
     ganzzahligen Anteile der Abstände in den Nebenkomponenten sämtlich nichtnegativ sind, und wobei die
     Dekremente in absteigender Folge abgearbeitet werden, bis folgende Abbruchbedingung erfüllt ist: der
     ganzzahlige Anteil des dekrementierten Abstands in
     Richtung der Hauptkomponente und/oder der ganzzahlige Anteil des dekrementierten Abstands in Richtung
     mindestens einer Nebenkomponenten ist Null; wobei für

                                       -5-



               den Fall, daß die Abbruchbedingung dadurch erfüllt ist,
               daß der ganzzahlige Teil des dekrementierten Abstands
               in Richtung einer Nebenkomponente Null ist, geprüft
               wird, ob dieselbe Abbruchbedingung auch durch mindestens ein nachfolgendes, kleineres Dekrement erfüllbar ist, und, falls dies so ist, Verwerfen des ursprünglichen größeren Dekrements;


          g)   Bestimmen der den Austrittspunkt der Halbgeraden aus
               der terminalen Zelle enthaltenden, sich anschließenden
               Einheitszelle aus den bei Abbruch der Dekrementierung
               vorliegenden dekrementierten Abständen;


          h)   Bestimmen der terminalen Zelle, welche die sich
               anschließende Einheitszelle umschließt."


Der Anspruch 1 gemäß Hilfsantrag 1 lautet:


          "Verfahren   zur   Durchquerung     einer   dreidimensionalen
          Octree-Struktur entlang einer Halbgeraden und zur Berechnung des Strahlverlaufs von auf einer Bildebene Pixel für
          Pixel eintreffenden Strahlen, wobei der Parameter "Maximaltiefe" die Tiefe der Raumpartition bezeichnet, wobei
          2Maximaltiefe die Kantenlänge des gesamten partitionierten
          Bereichs ist, wobei die Halbgerade durch einen Startpunkt
          sowie einen Richtungsvektor gegeben ist, wobei der Richtungsvektor eine Hauptkomponente sowie Nebenkomponenten aufweist, und wobei der Betrag jeder Nebenkomponente
          kleiner oder gleich dem Betrag der Hauptkomponente ist,


          gekennzeichnet durch folgende Schritte:

                             -6-



d)   Bestimmen der Abstände des Eintrittspunkts der Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;


f)   Dekrementieren der Abstände in Richtung der Hauptkomponente um 2n sowie der Abstände in Richtung der
     Nebenkomponenten um 2n x (Steigung m der jeweiligen
     Nebenkomponente), wobei n eine natürliche Zahl ist,
     wobei 2n nacheinander in absteigender Reihenfolge die
     Werte "Kantenlänge der terminalen Zelle", ... 2, 1
     annimmt, wobei ein Dekrementierungsschritt nur dann
     ausgeführt wird, wenn sowohl der ganzzahlige Anteil
     des Abstands in der Hauptkomponente als auch die
     ganzzahligen Anteile der Abstände in den Nebenkomponenten sämtlich nichtnegativ sind, und wobei die
     Dekremente in absteigender Folge abgearbeitet werden, bis folgende Abbruchbedingung erfüllt ist: der
     ganzzahlige Anteil des dekrementierten Abstands in
     Richtung der Hauptkomponente und/oder der ganzzahlige Anteil des dekrementierten Abstands in Richtung
     mindestens einer Nebenkomponenten ist Null; wobei für
     den Fall, daß die Abbruchbedingung dadurch erfüllt ist,
     daß der ganzzahlige Teil des dekrementierten Abstands
     in Richtung einer Nebenkomponente Null ist, geprüft
     wird, ob dieselbe Abbruchbedingung auch durch mindestens ein nachfolgendes, kleineres Dekrement erfüllbar ist, und, falls dies so ist, Verwerfen des ursprünglichen größeren Dekrements;

                                       -7-



          g)   Bestimmen der den Austrittspunkt der Halbgeraden aus
               der terminalen Zelle enthaltenden, sich anschließenden
               Einheitszelle aus den bei Abbruch der Dekrementierung
               vorliegenden dekrementierten Abständen;


          h)   Bestimmen der terminalen Zelle, welche die sich
               anschließende Einheitszelle umschließt."


Der Patentanspruch 1 gemäß Hilfsantrag 2 lautet:


          "Bildprozessor zur strahlbasierten Generierung von digitalen
          Bildern (Ray Tracing), wobei zur Strahlverlaufsberechnung
          eine vollständige, disjunkte Raumpartition in Richtung einer
          Halbgeraden durchquert wird, wobei die Halbgerade durch
          einen Startpunkt sowie einen Richtungsvektor gegeben ist,
          wobei der Richtungsvektor eine Hauptkomponente sowie
          Nebenkomponenten aufweist, und wobei der Betrag jeder
          Nebenkomponente kleiner oder gleich dem Betrag der
          Hauptkomponente ist, wobei der Parameter "Maximaltiefe"
          die Tiefe der Raumpartition bezeichnet, und wobei 2Maximaltiefe
          die Kantenlänge des gesamten partitionierten Bereichs ist,


          gekennzeichnet durch


          Mittel zum Bestimmen der Abstände des Eintrittspunkts der
          Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;


          Mittel zum Dekrementieren der Abstände in Richtung der
          Hauptkomponente um 2n sowie der Abstände in Richtung der

                            -8-



Nebenkomponenten um 2n x (Steigung m der jeweiligen
Nebenkomponente), wobei n eine natürliche Zahl ist, wobei
2n nacheinander in absteigender Reihenfolge die Werte
"Kantenlänge der terminalen Zelle", ... 2, 1 annimmt, wobei
ein Dekrementierungsschritt nur dann ausgeführt wird, wenn
sowohl der ganzzahlige Anteil des Abstands in der Hauptkomponente als auch die ganzzahligen Anteile der Abstände
in den Nebenkomponenten sämtlich nichtnegativ sind, und
wobei die Dekremente in absteigender Folge abgearbeitet
werden, bis folgende Abbruchbedingung erfüllt ist: der ganzzahlige Anteil des dekrementierten Abstands in Richtung der
Hauptkomponente und/oder der ganzzahlige Anteil des
dekrementierten Abstands in Richtung mindestens einer
Nebenkomponenten ist Null; wobei für den Fall, daß die
Abbruchbedingung dadurch erfüllt ist, daß der ganzzahlige
Teil des dekrementierten Abstands in Richtung einer Nebenkomponente Null ist, geprüft wird, ob dieselbe Abbruchbedingung auch durch mindestens ein nachfolgendes, kleineres
Dekrement erfüllbar ist, und, falls dies so ist, Verwerfen des
ursprünglichen größeren Dekrements;


Mittel zum Bestimmen der den Austrittspunkt der Halbgeraden aus der terminalen Zelle enthaltenden, sich anschließenden Einheitszelle aus den bei Abbruch der Dekrementierung
vorliegenden dekrementierten Abständen;


Mittel zum Bestimmen der terminalen Zelle, welche die sich
anschließende Einheitszelle umschließt."

                                       -9-



Der Patentanspruch 1 gemäß Hilfsantrag 3 lautet:


          "Bildprozessor zur strahlbasierten Generierung von digitalen
          Bildern (Ray Tracing), wobei zur Strahlverlaufsberechnung
          dreidimensionale Octree-Struktur in Richtung einer Halbgeraden durchquert wird und der Strahlverlauf von auf einer
          Bildebene Pixel für Pixel eintreffenden Strahlen berechnet
          wird, wobei die Halbgerade durch einen Startpunkt sowie
          einen Richtungsvektor gegeben ist, wobei der Richtungsvektor eine Hauptkomponente sowie Nebenkomponenten
          aufweist, und wobei der Betrag jeder Nebenkomponente kleiner oder gleich dem Betrag der Hauptkomponente ist, wobei
          der Parameter "Maximaltiefe" die Tiefe der Raumpartition
          bezeichnet, und wobei 2Maximaltiefe die Kantenlänge des
          gesamten partitionierten Bereichs ist,


          gekennzeichnet durch


          Mittel zum Bestimmen der Abstände des Eintrittspunkts der
          Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;


          Mittel zum Dekrementieren der Abstände in Richtung der
          Hauptkomponente um 2n sowie der Abstände in Richtung der
          Nebenkomponenten um 2n x (Steigung m der jeweiligen
          Nebenkomponente), wobei n eine natürliche Zahl ist, wobei
          2n nacheinander in absteigender Reihenfolge die Werte
          "Kantenlänge der terminalen Zelle", ... 2, 1 annimmt, wobei
          ein Dekrementierungsschritt nur dann ausgeführt wird, wenn
          sowohl der ganzzahlige Anteil des Abstands in der Haupt-

                                      - 10 -



          komponente als auch die ganzzahligen Anteile der Abstände
          in den Nebenkomponenten sämtlich nichtnegativ sind, und
          wobei die Dekremente in absteigender Folge abgearbeitet
          werden, bis folgende Abbruchbedingung erfüllt ist: der ganzzahlige Anteil des dekrementierten Abstands in Richtung der
          Hauptkomponente und/oder der ganzzahlige Anteil des
          dekrementierten Abstands in Richtung mindestens einer
          Nebenkomponenten ist Null;


          Mittel zum Bestimmen der den Austrittspunkt der Halbgeraden aus der terminalen Zelle enthaltenden, sich anschließenden Einheitszelle aus den bei Abbruch der Dekrementierung
          vorliegenden dekrementierten Abständen;


          Mittel zum Bestimmen der terminalen Zelle, welche die sich
          anschließende Einheitszelle umschließt."


Der Patentanspruch 1 gemäß Hilfsantrag 4 lautet:


          "Bildprozessor zur strahlbasierten Generierung von digitalen
          Bildern (Ray Tracing), wobei zur Strahlverlaufsberechnung
          eine vollständige, disjunkte Raumpartition in Richtung einer
          Halbgeraden durchquert wird, wobei die Halbgerade durch
          einen Startpunkt sowie einen Richtungsvektor gegeben ist,
          wobei der Richtungsvektor eine Hauptkomponente sowie
          Nebenkomponenten aufweist, und wobei der Betrag jeder
          Nebenkomponente kleiner oder gleich dem Betrag der
          Hauptkomponente ist, wobei der Parameter "Maximaltiefe"
          die Tiefe der Raumpartition bezeichnet, und wobei 2Maximaltiefe
          die Kantenlänge des gesamten partitionierten Bereichs ist,

                            - 11 -



gekennzeichnet durch


Mittel zum Bestimmen der Abstände des Eintrittspunkts der
Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;


Mittel zum Dekrementieren der Abstände in Richtung der
Hauptkomponente um 2n sowie der Abstände in Richtung der
Nebenkomponenten um 2n x (Steigung m der jeweiligen
Nebenkomponente), wobei n eine natürliche Zahl ist, wobei
2n nacheinander in absteigender Reihenfolge die Werte
"Kantenlänge der terminalen Zelle", ... 2, 1 annimmt, wobei
ein Dekrementierungsschritt nur dann ausgeführt wird, wenn
sowohl der ganzzahlige Anteil des Abstands in der Hauptkomponente als auch die ganzzahligen Anteile der Abstände
in den Nebenkomponenten sämtlich nichtnegativ sind, und
wobei die Dekremente in absteigender Folge abgearbeitet
werden, bis folgende Abbruchbedingung erfüllt ist: der ganzzahlige Anteil des dekrementierten Abstands in Richtung der
Hauptkomponente und/oder der ganzzahlige Anteil des
dekrementierten Abstands in Richtung mindestens einer
Nebenkomponenten ist Null; wobei für den Fall, daß die
Abbruchbedingung dadurch erfüllt ist, daß der ganzzahlige
Teil des dekrementierten Abstands in Richtung einer Nebenkomponente Null ist, geprüft wird, ob dieselbe Abbruchbedingung auch durch mindestens ein nachfolgendes, kleineres
Dekrement erfüllbar ist, und, falls dies so ist, Verwerfen des
ursprünglichen größeren Dekrements; wobei die gesamten
Folgen der Dekremente der Hauptkomponente sowie der

                                      - 12 -



          zugehörigen Dekremente der Nebenkomponenten mittels
          Schieberegistern erzeugt werden;


          Mittel zum Bestimmen der den Austrittspunkt der Halbgeraden aus der terminalen Zelle enthaltenden, sich anschließenden Einheitszelle aus den bei Abbruch der Dekrementierung
          vorliegenden dekrementierten Abständen;


          Mittel zum Bestimmen der terminalen Zelle, welche die sich
          anschließende Einheitszelle umschließt."


Der Patentanspruch 1 gemäß Hilfsantrag 5 lautet:


          "Bildprozessor zur strahlbasierten Generierung von digitalen
          Bildern (Ray Tracing), wobei zur Strahlverlaufsberechnung
          eine vollständige, disjunkte Raumpartition in Richtung einer
          Halbgeraden durchquert wird, wobei die Halbgerade durch
          einen Startpunkt sowie einen Richtungsvektor gegeben ist,
          wobei der Richtungsvektor eine Hauptkomponente sowie
          Nebenkomponenten aufweist, und wobei der Betrag jeder
          Nebenkomponente kleiner oder gleich dem Betrag der
          Hauptkomponente ist, wobei der Parameter "Maximaltiefe"
          die Tiefe der Raumpartition bezeichnet, und wobei 2Maximaltiefe
          die Kantenlänge des gesamten partitionierten Bereichs ist,


          gekennzeichnet durch


          Mittel zum Bestimmen der Abstände des Eintrittspunkts der
          Halbgerade in die terminale Zelle in der Richtung der Hauptkomponente sowie in den Richtungen der Nebenkomponenten von den Wänden der umschließenden terminalen Zelle;

                                      - 13 -



          Mittel zum Dekrementieren der Abstände in Richtung der
          Hauptkomponente um 2n sowie der Abstände in Richtung der
          Nebenkomponenten um 2n x (Steigung m der jeweiligen
          Nebenkomponente), wobei n eine natürliche Zahl ist, wobei
          2n nacheinander in absteigender Reihenfolge die Werte
          "Kantenlänge der terminalen Zelle", ... 2, 1 annimmt, wobei
          ein Dekrementierungsschritt nur dann ausgeführt wird, wenn
          sowohl der ganzzahlige Anteil des Abstands in der Hauptkomponente als auch die ganzzahligen Anteile der Abstände
          in den Nebenkomponenten sämtlich nichtnegativ sind, und
          wobei die Dekremente in absteigender Folge abgearbeitet
          werden, bis folgende Abbruchbedingung erfüllt ist: der ganzzahlige Anteil des dekrementierten Abstands in Richtung der
          Hauptkomponente und/oder der ganzzahlige Anteil des
          dekrementierten Abstands in Richtung mindestens einer
          Nebenkomponenten ist Null; wobei die gesamte Folge der
          Dekremente der Hauptkomponente sowie der zugehörigen
          Dekremente der Nebenkomponenten mittels einer Mehrzahl
          von jeweils um ein Bit gegeneinander verschobenen Ausleseports erzeugt werden;


          Mittel zum Bestimmen der den Austrittspunkt der Halbgeraden aus der terminalen Zelle enthaltenden, sich anschließenden Einheitszelle aus den bei Abbruch der Dekrementierung
          vorliegenden dekrementierten Abständen;


          Mittel zum Bestimmen der terminalen Zelle, welche die sich
          anschließende Einheitszelle umschließt."


Hinsichtlich der weiteren Ansprüche wird auf die Akten verwiesen.

                                      - 14 -



Der Anmelder erläutert zunächst die Grundzüge des beanspruchten Verfahrens
zur Durchquerung eines Partitionsbaums. Dieses sei Teil eines "Ray Tracing"-
Verfahrens, das dazu diene, von einer angenommenen räumlichen Szene mit
darin angeordneten Objekten durch Berechnung einer Vielzahl auftretender
(Licht-) Strahlen eine photorealistische zweidimensionale Abbildung in einer Bildebene zu berechnen. Die Berechnung der einzelnen Strahlverläufe sei sehr aufwendig, insbesondere dort, wo mit einem Auftreffen der Strahlen auf die angenommenen Objekte zu rechnen sei. Mit diesen Kollisionsbetrachtungen befasse
sich das beanspruchte Verfahren jedoch nicht, sondern nur mit der Berechnung
der Strahlverläufe in Bereichen, in denen sicher keine Objekte vorhanden seien. In
diesen Bereichen sei die Berechnung der Strahlverläufe relativ einfach, weil die
Strahlen keine Ablenkung erführen. Diese Bereiche würden durch würfelförmige
Raumpartitionen (Zellen) beschrieben, die sicher außerhalb der Objekte lägen und
in ihrer Größe an die Objekte angepasst seien. Diese leeren Raumpartitionen mit
ihren unterschiedlichen Größen seien in einem Partitionsbaum vollständig
beschrieben. Das beanspruchte Verfahren befasse sich mit der Berechnung des
Strahlverlaufs in diesen Raumpartitionen. Die besondere Leistung des Verfahrens
bestehe darin, dass es auf die Fähigkeiten eines Computers zugeschnitten sei und
daher die Berechnung der Strahlverläufe schneller als mit bekannten Verfahren
erfolge.
Den Verfahren nach Hauptantrag und Hilfsantrag 1 sei technischer Charakter
zuzubilligen, weil optische Überlegungen im Vordergrund stünden, es sich um
computergestützte Bildverarbeitung handele, die als Teil der Technik anzusehen
sei und ein Berechnungsalgorithmus vorgeschlagen werde, der auf die Fähigkeiten eines Computers zugeschnitten sei. Ohne Zweifel aber sei den auf einen Bildprozessor gerichteten Fassungen nach den weiteren Hilfsanträgen technischer
Charakter zuzubilligen.

                                        - 15 -



                                          II.


Die in rechter Frist und Form erhobene Beschwerde ist auch sonst zulässig. Sie ist
jedoch nur in Hinsicht auf den Anspruch 1 gemäß dem Hilfsantrag 5 begründet.
Dem Verfahren gemäß Hauptantrag, Hilfsantrag 1 und dem Bildprozessor gemäß
den Hilfsanträgen 2 und 3 mangelt es an einer auf technischem Gebiet liegenden
Erfindung (§ 1 PatG), der Bildprozessor nach dem Anspruch 1 gemäß Hilfsantrag 4 beruht nicht auf einer erfinderischen Tätigkeit (§§ 1, 4 PatG).


1. Zum Hauptantrag:
1.1 Der Anspruch 1 in dieser Fassung betrifft ein Verfahren zur Durchquerung
eines Partitionsbaums in Richtung einer Halbgeraden. Wie vom Anmelder erläutert
und in der Beschreibungseinleitung ausgeführt, ist dieses Verfahren Teil eines
"Ray Tracing"-Verfahrens, das insgesamt dazu dient, von zwei- oder dreidimensionalen Objekten oder Szenen mit mehreren Objekten durch die Berechnung der
Strahlenverläufe einer Vielzahl von Strahlen computergestützt eine dreidimensional (wirkende) Ansicht zu generieren. Damit derart erzeugte Ansichten realistisch
wirken und bspw auch den Schattenwurf von Objekten oder Reflexionen an
Objektoberflächen berücksichtigen, erfordert diese Berechnung den vollständigen
Nachvollzug des Verlaufs einzelner Strahlen. Das hierzu insgesamt verwendete
Modell ist in Figur 1 schematisch dargestellt und auf Seite 10 der Beschreibung
erläutert. Wie vom Anmelder ausgeführt, befasst sich das vorliegende Verfahren
nur mit der Berechnung des Strahlverlaufs in den Raumpartitionen (Teilräumen)
einer Szene, die sicher frei von Objekten sind. In diesen Partitionen ist der Strahlverlauf geradlinig und die Berechnung relativ einfach, da keine Reflexionen an
Objektoberflächen berücksichtigt werden müssen. Die Raumpartitionen sind adaptiv, dh sie weisen in Abhängigkeit von der Form der Objekte, die sie umschließen,
unterschiedliche Größen auf. Ein Beispiel für eine (zweidimensionale) Szene mit
Objekten 11 bis 15 und freien Raumpartitionen (leere Subquadrate zB 17, 22) ist
in Figur 2 dargestellt. Die Raumpartitionen einer Szene werden in einem "Partitionsbaum" nach Größe und Lage aufgelistet. Ein Partitionsbaum stellt sonach eine

                                       - 16 -



nach einem bestimmten Schema geordnete Beschreibung der Größe und Lage
aller leeren Partitionen einer angenommenen Szene dar. In Figur 4 ist beispielhaft
der Partitionsbaum für die Szene von Figur 2 dargestellt.


Ausgehend von einem solchen Ray Tracing-Modell mit adaptiven Raumpartitionen
befasst sich das Verfahren gemäß dem Anspruch 1 mit der Ermittlung derjenigen
Partitionen eines Partitionsbaums, die ein angenommener Strahl durchquert.
Gemäß dem Oberbegriff des Anspruchs sind hierzu zunächst Festlegungen zur
Tiefe, dh Größenschachtelung der Partitionen zu treffen, die Kantenlänge der
Szene zu 2Maximaltiefe zu setzen und der Strahl bzw die Halbgerade durch Startpunkt
und Richtungsvektor mit Hauptkomponente und (kleinerer) Nebenkomponente zu
definieren.
Gemäß Merkmal d) werden zur Berechnung des Verlaufs eines angenommenen
Strahls die Abstände des Eintrittspunktes in die "terminale Zelle", dh der momentan betrachteten Raumpartition in Richtung der Haupt- und der Nebenkomponente
bestimmt. Der in Merkmal f) im einzelnen dargestellte Dekrementierungsalgorithmus dient zur Bestimmung der Seite und des engeren Bereichs, an welchem der
Strahl aus der terminalen Zelle (momentan betrachteten Raumpartition) austritt.
Dabei werden alle auftretenden Fälle berücksichtigt, bspw dass der Strahl an der
der Eintrittsseite gegenüberliegenden Seite austritt (vgl Fig 7, Durchstoßpunkt 37)
oder aber an einer der Eintrittsseite angrenzenden Seiten (vgl Fig 7, obere Seite
der Partition 40).
Wie in Merkmal g) dargelegt, wird aus Austrittsseite und -bereich die sich anschließende (kleinste) Einheitszelle ermittelt. Da die im Partitionsbaum anschließende
Raumpartition größer sein kann als eine Einheitszelle, ist gemäß Merkmal h) noch
zu bestimmen, welche terminale Zelle die Einheitszelle umschließt. Diese Zelle
stellt die nächste vom Strahl durchstoßene Raumpartition dar.


Durch eine mehrmalige Anwendung der im Anspruch 1 genannten Verfahrensschritte ist es möglich, gemäß der gestellte Aufgabe (vgl S 3, Abs 5 der Beschrei-

                                       - 17 -



bung) in dem Partitionsbaum nacheinander die Raumpartitionen aufzufinden, die
ein geradliniger Strahl durchläuft.


1.2 Das Verfahren nach dem Patentanspruch 1 gemäß Hauptantrag ist keine
Erfindung iSd § 1 Abs 1 PatG.
1.2.1 Gegenstand des beanspruchten Verfahrens ist im wesentlichen eine mathematische Abbildung einer mehrdimensionalen Szene auf eine Bildebene. Diese
Abbildung erfolgt nicht an Hand real vorhandener Objekte, bspw durch die Aussendung von Lichtstrahlen auf die realen Objekte und Auffangen der reflektierten
Lichtstrahlen durch einen in bestimmter Weise angeordneten Schirm, sondern
allein durch Berechnungen. Der Anspruch 1 lehrt, wie aus einer mathematischen
Beschreibung lediglich mathematisch definierter Objekte mittels einer Abbildungsvorschrift eine andere mathematische Beschreibung gewonnen wird, die dann dargestellt werden kann. Dass der Anspruch 1 sich nur mit einem Teilaspekt einer
vollständigen mathematischen Ray Tracing-Abbildung befasst, nämlich der
Bestimmung, welche Raumpartitionen ein einzelner gedachter Strahl durchläuft,
ändert daran nichts. Wäre der Anspruchsgegenstand allein auf die dargestellten
Berechnungsschritte gerichtet, so läge eine mathematische Methode "als solche"
vor, die bereits nach § 1 Abs 2 Nr 1 und Abs 3 PatG nicht als Erfindung anzusehen wäre.


1.2.2 Gegen eine solche Bewertung des Verfahrens wendet der Anmelder ein,
dass nicht Schutz für das Berechnungsverfahren an sich beansprucht werde, sondern lediglich für die Ausführung des Verfahrens durch eine technische Vorrichtung, nämlich einen Computer, da wie im Anspruch angegeben, die Generierung
von digitalen Bildern "computergestützt" erfolgen soll.


Es ist nicht von der Hand zu weisen, dass der Anspruchswortlaut eindeutig zum
Ausdruck bringt, dass nur die computergestützte Ausführung des Berechnungsverfahrens unter Schutz gestellt sein soll und sonach jedenfalls der Nachvollzug
des Berechnungsverfahrens ohne Einsatz des technischen Mittels "Computer"

                                       - 18 -



nicht vom Anspruch umfasst wird. Insoweit ist der Auffassung des Anmelders beizutreten, dass mit dem Anspruch keine mathematische Methode "als solche", dh
als lediglich auf geistigem Gebiet liegendes Konzept beansprucht wird und der
Ausschlusstatbestand des § 1 Abs 2 Nr 1 und Abs 2 PatG für mathematische
Methoden nicht greift.


Der Umstand, dass nur für die computergestützte Ausführung der Berechnungsschritte Schutz beansprucht wird, also lediglich für deren Ausführung durch eine
festverdrahtete oder geeignet programmierte Datenverarbeitungsanlage, hat allerdings nicht zur Folge, dass der Anspruchsgegenstand ohne weiteres dem Gebiet
der Technik und damit zwangsläufig dem Kreis der in § 1 Abs 1 PatG genannten
"Erfindungen" zuzuordnen ist (andere Auffassung: Beschwerdekammer 3.5.1 des
Europäischen Patentamts, Entscheidung vom 21. April 2004, T 0258/03, Leitsatz I). Einer solchen Zuordnung steht jedenfalls entgegen, dass, wie der Bundesgerichtshof in der Entscheidung "Suche fehlerhafter Zeichenketten" feststellt, "eine
beanspruchte Lehre nicht schon deshalb als patentierbar angesehen werden
kann, weil sie bestimmungsgemäß den Einsatz eines Computers erfordert". ... "Die
prägenden Anweisungen der beanspruchten Lehre müssen vielmehr insoweit der
Lösung eines konkreten technischen Problems dienen. Unter diesen Voraussetzungen ist die beanspruchte Lehre dem Patentschutz auch dann zugänglich, wenn
sie als Computerprogramm oder in einer sonstigen Erscheinungsform [vorliegend:
mathematische Methode] geschützt werden soll, die eine Datenverarbeitungsanlage nutzt" (GRUR 2002, 143, 144 re Sp).


Im vorliegenden Fall sind die prägenden Anweisungen, mit denen letztlich die
schnelle Durchquerung eines Partitionsbaums (auf mathematischem Wege)
gelingt, zweifellos in dem im Anspruch angegebenen Berechnungsverfahren zu
sehen. Eine konkrete, sich mit technischen Umständen auseinandersetzende Problemstellung ist weder der Beschreibung entnehmbar noch ergibt sie sich implizit
aus dem Anspruchsgegenstand. Der vom Anmelder angeführte Vorteil, dass die
Berechnung unter Benutzung des vorgeschlagenen Verfahrens schneller gelingt,

                                       - 19 -



ist nicht auf eine technische Leistung zurückzuführen, sondern beruht auf dem
vorgeschlagenen Berechnungsverfahren, dem zwar ein vorteilhaftes mathematisches Modell zugrunde liegen mag, das aber jedenfalls auf mathematische Überlegungen gründet.


Auch das weitere Argument des Anmelders, dass die Technizität des Verfahrens
anzuerkennen sei, weil optische Überlegungen im Vordergrund stünden und das
Verfahren auf dem Gebiet der Computergrafik und somit auf einem Gebiet der
Technik liege, vermag nicht zu überzeugen.
Dem Anmelder kann nur insoweit gefolgt werden, als in der herkömmlichen Optik
zur Abbildung einer räumlichen Szene auf einen Bildschirm eine technische Abbildungsvorrichtung und ein entsprechendes technisches Abbildungsverfahren (zB
mit in bestimmter Weise angeordneten Linsen) erforderlich sind. Hierdurch werden
reale Objekte mit optischen Mitteln abgebildet.
Im Unterschied dazu schlägt das beanspruchte Verfahren lediglich eine Berechnung vor, die von einer mathematischen Beschreibung und nicht von real vorhandenen Objekten ausgeht und durch geeignete mathematische Operationen nach
optischen Gesetzen eine Abbildung erzeugt. Der Unterschied zwischen einem real
stattfindenden Prozess und einer bloßen Berechnung - auch wenn sie unter Zuhilfenahme von technischen Hilfsmitteln durchgeführt wird - rechtfertigt es, den vorgenannten real stattfindenden Prozess dem Gebiet der Technik zuzuordnen und
eine bloße Berechnung, auch wenn sie optische Gesetze berücksichtigt, eben
nicht.


Das mit dem Anspruch 1 beanspruchte Verfahren liegt sonach nicht auf technischem Gebiet und ist deshalb keine patentfähige Erfindung (§ 1 Abs 1 PatG).


2. Zum Hilfsantrag 1:
2.1 Der Patentanspruch 1 in dieser Fassung unterscheidet sich vom Anspruch 1
gemäß dem Hauptantrag schon dadurch, dass das Verfahren nicht lediglich auf
die computergestützte Ausführung beschränkt ist, sondern generell beansprucht

                                        - 20 -



wird. Im übrigen ist das Verfahren eingeschränkt auf die Durchquerung einer dreidimensionalen Octree-Struktur entlang einer Halbgeraden. Wie in der Beschreibung ausgeführt, stellt eine Octree-Struktur lediglich den dreidimensionalen Spezialfall einer Raumpartitionierung bzw des im Hauptantrag genannten Partitionsbaums dar (vgl S 3, Abs 2 u 3 iVm Fig 4 und 5B).


2.2 Mit dem Anspruch 1 in dieser Fassung beansprucht der Anmelder somit (jedenfalls auch) Schutz für ein Berechnungsverfahren, das ohne Einsatz technischer Mittel ausgeführt wird. Eine solcher Anspruchsgegenstand ist, wie bereits
zum Hauptantrag erläutert, als mathematische Methode "als solche" anzusehen
und nach § 1 Abs 2 Nr 1 und Abs 3 PatG vom Patentschutz ausgeschlossen.


3. Zum Hilfsantrag 2:
3.1 Der Patentanspruch 1 in dieser Fassung bezieht sich, wie auch die nachfolgenden Fassungen, auf einen Bildprozessor zur strahlbasierten Generierung von
digitalen Bildern, bei genauer Betrachtung lediglich auf die Ermittlung der Raumpartitionen, die ein angenommener Strahl durchquert. Hierzu werden an Stelle der
in der Fassung nach dem Hauptantrag genannten Verfahrensschritte d), f), g) und
h), nämlich des Bestimmens der Abstände, des Dekrementierens dieser Abstände, des Bestimmens der sich anschließenden Einheitszelle und der terminalen
Zelle, welche die sich anschließende Einheitszelle umschließt, dort "Mittel"
genannt, die diese Verfahrenschritte entsprechend ausführen sollen. Eine irgendwie geartete konkrete technische Ausbildung der einzelnen "Mittel" lässt sich dem
Anspruch nicht entnehmen, so dass davon auszugehen ist, dass die genannten
"Mittel" lediglich eine sprachliche Umschreibung der Berechnungsschritte darstellen, die ein beliebiger Bildprozessor ausführen soll.
Mit dem formal auf einen Bildprozessor gerichteten Anspruch 1 beansprucht der
Anmelder inhaltlich sonach nichts anderes als mit dem Verfahrensanspruch
gemäß dem Hauptantrag, nämlich die Ausführung eines bestimmten Berechungsverfahrens mittels eines Computers. Der 20. Senat des Bundespatentgerichts
spricht in einem ähnlich gelagerten Fall von "demselben Erfindungskonzept", das

                                       - 21 -



Verfahren und korrespondierende Vorrichtung prägt, lässt aber die Frage, ob und
ggf in welcher Kategorie eine dem Patentschutz zugängliche technische Erfindung
vorliegt, offen (BPatG, Beschluss vom 10. Mai 2004, 20 W (pat) 314/02, Ende des
Abschnitts II 2.).


3.2 Die strahlbasierte Generierung von digitalen Bildern mittels eines von einem
Bildprozessor ausgeführten Berechnungsverfahrens gemäß dem Anspruch 1 ist
keine Erfindung im Sinne des § 1 Abs 1 PatG.
3.2.1 Der Anmelder führt unter Bezug auf die Entscheidung "Sprachanalyseeinrichtung" des Bundesgerichtshofs (BlPMZ 2000, 276) aus, dass dem vorliegenden
Anspruchsgegenstand schon deshalb technischer Charakter zuzubilligen sei, weil
er auf eine Vorrichtung, nämlich einen Bildprozessor gerichtet sei, der stets technischer Charakter zukomme.
In der vom Anmelder aufgegriffenen Entscheidung führt der Bundesgerichtshof
aus, dass einer Vorrichtung (Datenverarbeitungsanlage), die in bestimmter Weise
programmtechnisch eingerichtet sei, ohne weiteres technischer Charakter
zukomme (aaO, Leitsatz 1 und 277 re Sp). Die Ausführungen des Bundesgerichtshofs in dieser Entscheidung können jedoch nicht ohne Berücksichtigung des tatsächlich beanspruchten Gegenstands auf den vorliegenden Anspruchsgegenstand
übertragen werden. In der jüngeren Entscheidung "Suche fehlerhafter Zeichenketten" hat der Bundesgerichtshof unter Bezug auf die vorgenannte Entscheidung
ausgeführt, dass die Frage, ob ein angemeldeter Patentanspruch die erforderliche
Patentfähigkeit aufweise, nicht allein nach der Kategorie dieses Anspruchs und
unabhängig davon zu beantworten sei, was nach der beanspruchten Lehre im
Vordergrund stehe (GRUR 2002, 143, 145, re Sp).


Wie erläutert, enthält der vorliegende Anspruch 1 keinerlei Hinweise auf eine in
technischer Hinsicht bestimmte Ausbildung des Bildprozessors in seiner Gesamtheit oder der einzeln aufgeführten "Mittel" zur Ausführung der Berechnungsschritte. Aus diesem Umstand ergibt sich, dass eine vorrichtungsmäßige Ausbildung des Bildprozessors objektiv nicht Gegenstand des Anspruchs ist und folglich

                                      - 22 -



auch die beanspruchte Lehre nicht prägen kann. Das wesentliche des formal auf
einen Bildprozessor gerichteten Anspruchs ist - wie beim Gegenstand des
Anspruchs 1 nach Hauptantrag - in dem erläuterten Berechnungsverfahren zu
sehen, das nicht auf technischem Gebiet liegt.


3.2.2 Eine andere Bewertung des technischen Charakters des vorliegenden
Anspruchsgegenstands und ähnlich gelagerter, letztlich auf die computergestützte
Ausführung von Verfahren gerichteter Ansprüche ergäbe sich, wenn der Senat
dem methodischen Vorgehen folgte, das in der unter 1.2.2 dieses Beschlusses
zitierten europäischen Entscheidung T 0258/03 eingeschlagen wurde. Entsprechend dieser Entscheidung wären nicht nur alle Anspruchsgegenstände, die ihrer
patentrechtlichen Kategorie nach auf Vorrichtungen gerichtet sind, sondern auch
jegliche Verfahren "Erfindungen" im Sinne des Art 52 (1) EPÜ bzw § 1 Abs 1
PatG, wenn nur technische Mittel zu ihrer Ausführung verwendet würden (vgl aaO,
Leitsatz I, 3.7).


Eine solche Vorgehensweise führt zwar ebenfalls zu der wünschenswerten patentrechtlichen Gleichbehandlung gleicher technischer Sachverhalte, nämlich dem
eines Computers, der ein (technisches oder nichttechnisches) Verfahren ausführt,
mit dem eines (technischen oder nichttechnischen) Verfahrens, das mittels eines
Computers ausgeführt wird, unabhängig von der gewählten patentrechtlichen
Kategorie. Allerdings erfolgt die Entscheidung darüber, ob der Anspruchsgegenstand auf technischem Gebiet liegt oder nicht, allein an Hand des Umstands, ob
technische Mittel zur Ausführung des Verfahrens verwendet werden, und nicht an
Hand des wesentlichen Inhalts des Anspruchs, ob also das zur Ausführung kommende Verfahren auf technischem Gebiet liegt oder nicht. Eine detaillierte Wertung der einzelnen technischen und nichttechnischen Aspekte des Anspruchsgegenstandes erfolgt erst bei der nachgelagerten Prüfung auf erfinderische Tätigkeit.
Dort werden die einzelnen Merkmale bzw Verfahrensschritte darauf hin überprüft,
ob sie zum technischen Charakter des Anspruchsgegenstandes beitragen oder

                                      - 23 -



nicht (vgl aaO, Leitsatz II) und ggf vollständig aus der Betrachtung ausgeklammert.


Der Senat hat Bedenken, die Entscheidung, ob dem Gegenstand eines Anspruchs
technischer Charakter zukommt oder nicht, letztlich von der isolierten Bewertung
einzelner Anspruchsmerkmale - die für sich durchaus ambivalenten Charakter
haben können - abhängig zu machen. Beispielsweise lässt sich das im Anspruch 1
nach Hauptantrag im Merkmal d) genannte "Bestimmen der Abstände..." bzw das
in der vorliegend diskutierten Anspruchsfassung genannte "Mittel zum Bestimmen
der Abstände des Eintrittspunkts der Halbgeraden in die terminale Zelle ..." nicht
zweifelsfrei als Merkmal identifizieren, das einen Beitrag zum Stand der Technik
enthält oder nicht. Möglicherweise gerät bei einer solchen Vorgehensweise der zu
bewertende Anspruchsgegenstand in seiner Gesamtheit in den Hintergrund und
somit das, wofür der Anmelder letztlich um Schutz nachsucht. Der Senat folgt den
in der Entscheidung "Suche fehlerhafter Zeichenketten" vom Bundesgerichtshof
vorgegebenen Grundsätzen.


Die strahlbasierte Generierung von digitalen Bildern mit einem Bildprozessor nach
dem Anspruch 1 gemäß Hilfsantrag 2 kann sonach nicht als auf technischem
Gebiet liegend erkannt werden.


4. Zum Hilfsantrag 3:
4.1 Der auf einen Bildprozessor gerichtete Anspruch 1 in dieser Fassung unterscheidet sich von dem nach der vorhergehenden Fassung dadurch, dass das vom
Bildprozessor ausgeführte Verfahren auf die Durchquerung einer dreidimensionalen Octree-Struktur entlang einer Halbgeraden, also auf den dreidimensionalen
Spezialfall einer Raumpartitionierung eingeschränkt ist. Nachdem die dem
Anspruch insgesamt entnehmbaren Berechnungsschritte, wie erläutert, nur den
Teil der Berechnung eines gesamten Strahlenverlaufs umfassen, nämlich den, der
durch die leeren Raumpartitionen stattfindet, kann die weiter vorgenommene
Ergänzung, dass "der Strahlverlauf von auf einer Bildebene Pixel für Pixel eintref-

                                      - 24 -



fenden Strahlen berechnet wird", nur als Hinweis auf eine wiederholte Ausführung
dieser Berechnungsschritte verstanden werden.


4.2 Hinsichtlich der Bewertung des technischen Charakters des Gegenstands dieses Anspruchs ergibt sich hierdurch keine Änderung gegenüber der vorhergehend
diskutierten Anspruchsfassung. Auch in der strahlbasierten Generierung von digitalen Bildern mittels eines von einem Bildprozessor ausgeführten Berechnungsverfahren nach Anspruch 1 gemäß Hilfsantrag 3 ist keine auf technischem Gebiet
liegende Erfindung zu erkennen.


5. Zum Hilfsantrag 4:
5.1 Der Anspruch 1 gemäß diesem Antrag ist auf einen Bildprozessor gerichtet,
der das erläuterte (Teil-) Verfahren zur strahlbasierten Generierung von digitalen
Bildern ausführt. Dieser Anspruch unterscheidet sich von den Ansprüchen nach
Hilfsantrag 2 und 3 jedoch dadurch, dass in dieser Fassung eine konkrete technische Ausgestaltung des zum Einsatz kommenden Bildprozessors ergänzt ist,
nämlich dass die gesamten Folgen der Dekremente der Hauptkomponente sowie
der Nebenkomponenten mittels Schieberegister erzeugt werden.
Die Lehre dieses Anspruchs beschränkt sich sonach nicht allein auf die Ausführung einer Berechnungsmethode durch einen Bildprozessor, sondern gibt den Hinweis, den zur Ausführung des Verfahrens verwendeten Bildprozessor durch ein
Schieberegister zu ergänzen.
Der Gegenstand des vorliegenden Anspruchs 1, in seiner Gesamtheit gesehen,
umfasst sonach zwei Aspekte, nämlich das als nichttechnisch bewertete Berechnungsverfahren für die von einem Strahl bzw einer Halbgeraden durchquerten
Raumpartitionen und weiterhin die konkrete schaltungstechnische Ergänzung des
zur Ausführung des Berechnungsverfahrens verwendeten Bildprozessors durch
ein Schieberegister, mit dem die Dekremente der Hauptkomponente und der
Nebenkomponenten erzeugt werden sollen.

                                         - 25 -



5.2 Die im Anspruch (auch) enthaltene konkrete schaltungsmäßige Ausgestaltung
des Bildprozessors liegt zweifelsfrei auf technischem Gebiet. Sie ist auch ausreichend offenbart (vgl S 24, Abs 2 und 3 der Beschreibung) und dient dazu, wie auf
S 3, Abs 5 erläutert, einen Bildprozessor mit hoher Geschwindigkeit zur Verfügung
zu stellen.
Was diesen technischen Aspekt des vorliegenden Anspruchsgegenstands anbelangt, also die Ergänzung des Bildprozessors um ein Schieberegister, so ist diese
Ergänzung jedoch nicht als auf erfinderischer Tätigkeit beruhend anzuerkennen.
Denn dem für den Entwurf von Bildprozessoren zuständigen Fachmann, einem
Datenverarbeitungsingenieur mit praktischer Erfahrung auf dem Gebiet der Bildbearbeitung, war geläufig, dass der Befehlsvorrat üblicher Prozessoren Schiebebefehle umfasst, mit denen Daten um eine binäre Stelle verschoben werden können.
Dem Fachmann war auch die einfachste Möglichkeit geläufig, mit der eine solche
Verschiebung bewerkstelligt werden konnte, nämlich ein Schieberegister.


Die Ergänzung des Bildprozessors um ein Schieberegister zur Ausführung von
Schiebeoperationen war für den Fachmann naheliegend. Der Gegenstand des
Anspruchs 1, soweit er die damit vorgeschlagene technische Ausgestaltung
betrifft, beruht sonach nicht auf erfinderischer Tätigkeit.


Das im Anspruch 1 weiterhin enthaltene Berechnungsverfahren für die von einem
Strahl durchquerten Raumpartitionen, das von dem Bildprozessor ausgeführt wird,
liegt, wie erläutert, nicht auf technischem Gebiet.
Der Anspruch 1 in der Fassung nach Hilfsantrag 4 enthält, insgesamt gesehen,
keine patentfähige Erfindung.


6. Zum Hilfsantrag 5:
6.1 Der Anspruch 1 nach diesem Antrag ist wie der vorhergehende Antrag auf
einen Bildprozessor gerichtet, der ein (Teil-) Verfahren zur strahlbasierten Generierung von digitalen Bildern ausführt, und enthält weiterhin Angaben zu einer konkreten technischen Ausgestaltung des Bildprozessors mit einer Mehrzahl von

                                     - 26 -



jeweils um ein Bit gegeneinander verschobenen Ausleseports zur Erzeugung der
Dekremente. Die diesem Anspruch in seiner Gesamtheit entnehmbare Lehre
umfasst sonach ebenfalls zwei Aspekte, nämlich das nichttechnische Berechnungsverfahren für die von einem angenommenen Strahl durchquerten Raumpartitionen und die schaltungstechnische Ergänzung des Bildprozessors um mehrere
Ausleseports.


6.2 Was die Ergänzung des Bildprozessors durch mehrere, jeweils um ein Bit
verschobene Ausleseports anbelangt, so kann nicht davon ausgegangen werden,
dass eine solche Ausbildung ohne weiteres dem Fachwissen des einschlägigen
Fachmanns zugeschrieben werden konnte. Das Deutsche Patent- und Markenamt
hat hinsichtlich einer solchen schaltungsmäßigen Ausgestaltung eines Bildprozessors im bisherigen Prüfungsverfahren noch keine Ermittlungen durchgeführt.
Der Beschluss der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und
Markenamts war insoweit aufzuheben und die Sache unter Zugrundelegung der
mit Hilfsantrag 5 bezeichneten Patentansprüche 1 - 7 gemäß § 79 Abs 3 Satz 1
Nr 1 PatG zur weiteren Prüfung an das Deutsche Patent- und Markenamt zurückzuverweisen.


Das Deutsche Patent- und Markenamt wird dabei nicht nur den einschlägigen
Stand der Technik ermitteln müssen, sondern, falls die insoweit geltende
Anspruchsfassung beibehalten wird, auch darüber zu befinden haben, ob und in
welcher Form eine gewährbare Anspruchsfassung auch den erläuterten nichttechnischen Aspekt in Form der Berechnungsmethode enthalten kann.


Die weitergehende Beschwerde war zurückzuweisen.


7. Zu einer Fortbildung des Rechts hält der Senat die Zulassung der Rechtsbeschwerde an den Bundesgerichtshof nach § 100 Abs 2 Nr 2 PatG für geboten. Der
Anmelder regt die Zulassung der Rechtsbeschwerde an. Er führt hierzu aus, dass
das beanspruchte Verfahren auf dem Gebiet der Computergrafik liege.

                                      - 27 -



Dieses moderne Gebiet stelle eine Fortentwicklung der herkömmlichen optischen
Technik dar. Deshalb müssten auch die auf diesem Gebiet verwendeten Methoden als technisch anerkannt werden.




Dr. Fritsch             Dr. Schmitt             Dr. Kraus             Prasch




                                                                          Fa
