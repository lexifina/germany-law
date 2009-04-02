---
ecli: "ECLI:DE:BPatG:2009:020409B17Wpat5.05.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 5/05"
decided: "2009-04-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2009&Sort=1&Seite=26&nr=14571&anz=1436&pos=390&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2009-04-02_17_W-pat_5_05_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 5/05 vom 2009-04-02

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 5/05                                                      Verkündet am
_______________                                                        2. April 2009
    (Aktenzeichen)                                                          …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 198 28 317.2-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 2. April 2009 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Fritsch, der Richterin Eder, des Richters Dipl.-Ing. Prasch
und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
08.05

                                        -2-



beschlossen:


        1. Die Beschwerde wird zurückgewiesen.


        2. Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                     Gründe


                                         I.


Die vorliegende Patentanmeldung ist am 25. Juni 1998 beim Deutschen Patentund Markenamt unter der Bezeichnung


        „Farbschema für Hinderniswarnung“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 20. September 2004
die Anmeldung zurückgewiesen, da der Gegenstand des Patentbegehrens nicht
auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


        den angefochtenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                      -3-



       gemäß Hauptantrag mit Patentansprüchen 1 bis 9 vom 12. November 2004,
       Beschreibung Seiten 1, 1a vom 17. März 2009, eingegangen am
       18. März 2009,
       Beschreibung Seiten 2 bis 5 vom Anmeldetag,


       gemäß Hilfsantrag mit Patentansprüchen 1 bis 7 vom 12. November 2004,
       Beschreibung wie Hauptantrag.


Zudem regt sie die Rückzahlung der Beschwerdegebühr an.
Als Grund für die angeregte Rückzahlung der Beschwerdegebühr macht die
Anmelderin Verletzung rechtlichen Gehörs sowie Verstoß gegen die Verfahrensökonomie und die Pflicht zur Verfahrensförderung geltend.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


       D1: DE 31 06 100 A1


       D2: Computer Graphics: Principles and Practice, Hrsg. James D. Foley
       et al, 2nd ed. in C, Addison-Wesley Systems Programming Series, 1996,
       S. 610, 611, 727, 728.


Der geltende Patentanspruch 1 nach Hauptantrag lautet:


       „1. Vorrichtung zur Farbkodierung von Umgebungsdarstellungen auf
       Anzeigeschirmen in Fluggeräten, insbesondere in Hubschraubern, mit:


           einem Sensor zur Erfassung von Abstandsdaten zu umgebenden Elementen oder Objekten,

                                      -4-



           einer Einrichtung zur Verarbeitung der vom Sensor erfassten
           Abstandsdaten, die den Abstandsdaten entsprechend vorher festgelegten Abstandsbereichen verschiedene farbkodierte Farbbereiche
           zuweist und diese Farben auf dem gesamten Anzeigeschirm darstellt,
           wobei jeder Farbbereich durch RGB-Werte bei seinem Anfangs- und
           Endabstand definiert ist, und


           einer Einrichtung zum Interpolieren der RGB-Werte für die Abstände
           zwischen Anfangs- und Endabstand jedes Farbbereichs.“


Der nebengeordnete Patentanspruch 6 nach Hauptantrag lautet:


       „6. Verfahren zur Farbkodierung von Umgebungsdarstellungen auf Anzeigeschirmen in Fluggeräten, insbesondere in Hubschraubern, mit den
       Schritten:


           Erfassen von Abstandsdaten zu umgebenden Elementen oder Objekten durch einen Sensor,


           Verarbeiten der vom Sensor erfassten Abstandsdaten, wobei den
           Abstandsdaten entsprechend vorher festgelegten Abstandsbereichen
           verschiedene farbkodierte Farbbereiche zugewiesen werden und
           diese Farben auf einem gesamten Anzeigeschirm dargestellt werden,
           wobei jeder Farbbereich durch RGB-Werte bei seinem Anfangs- und
           Endabstand definiert ist, und wobei


           für die Abstände zwischen Anfangs- und Endabstand die RGB-Werte
           jedes Farbbereichs interpoliert werden.“

                                               -5-



Der Patentanspruch 1 nach Hilfsantrag lautet:


       „1. Vorrichtung zur Farbkodierung von Umgebungsdarstellungen auf
       Anzeigeschirmen in Fluggeräten, insbesondere in Hubschraubern, mit:


            einem Sensor zur Erfassung von Abstandsdaten zu umgebenden Elementen oder Objekten,


            einer Einrichtung zur Verarbeitung der vom Sensor erfassten
            Abstandsdaten, die den Abstandsdaten entsprechend vorher festgelegten Abstandsbereichen verschiedene farbkodierte Farbbereiche
            zuweist und diese Farben auf dem gesamten Anzeigeschirm darstellt,


            wobei jeder Farbbereich durch RGB-Werte bei seinem Anfangs- und
            Endabstand definiert ist, und


            einer Einrichtung zum Interpolieren der RGB-Werte für die Abstände
            zwischen Anfangs- und Endabstand jedes Farbbereichs, welche die
            RGB-Werte mit dem folgenden linearen Algorithmus interpoliert:


       c = (d - dStart) / (dStop – dStart) * (cStop – cStart) + cStart
       wobei
       c        der berechnete R-, G- oder B-Wert ist,
       d        der aktuelle Abstand zwischen Sensor und Hindernis ist
       dStart   der Anfangsabstand des Farbbereichs ist,
       dStop    der Endabstand des Farbbereichs ist,
       cStart   der R-, G-, B-Wert beim Anfangsabstand ist, und
       cStop    der R-, G-, B-Wert beim Endabstand ist.“

                                               -6-



Der nebengeordnete Patentanspruch 5 nach Hilfsantrag lautet:


       „5. Verfahren zur Farbkodierung von Umgebungsdarstellungen auf Anzeigeschirmen in Fluggeräten, insbesondere in Hubschraubern, mit den
       Schritten:


            Erfassen von Abstandsdaten zu umgebenden Elementen oder Objekten durch einen Sensor,


            Verarbeiten der vom Sensor erfassten Abstandsdaten, wobei den
            Abstandsdaten entsprechend vorher festgelegten Abstandsbereichen
            verschiedene farbkodierte Farbbereiche zugewiesen werden und
            diese Farben auf einem gesamten Anzeigeschirm dargestellt werden,
            wobei


            jeder Farbbereich durch RGB-Werte bei seinem Anfangs- und Endabstand definiert ist und beim Verarbeiten der vom Sensor erfassten
            Abstandsdaten für die Abstände zwischen Anfangs- und Endabstand
            die RGB-Werte mit dem folgenden linearen Algorithmus interpoliert
            werden:


       c = (d - dStart) / (dStop – dStart) * (cStop – cStart) + cStart
       wobei
       c        der berechnete R-, G- oder B-Wert ist,
       d        der aktuelle Abstand zwischen Sensor und Hindernis ist
       dStart   der Anfangsabstand des Farbbereichs ist,
       dStop    der Endabstand des Farbbereichs ist,
       cStart   der R-, G-, B-Wert beim Anfangsabstand ist, und
       cStop    der R-, G-, B-Wert beim Endabstand ist.“

                                       -7-



Der Anmeldung soll gemäß der Beschwerdebegründung Seite 10 vorle. Abs. die
technische Aufgabe zugrunde liegen, eine Vorrichtung und ein Verfahren zur Farbkodierung für Umgebungsdarstellungen auf Anzeigeschirmen in Fluggeräten zu
schaffen, mit der eine einfache, schnelle Erkennung von Hindernissen, insbesondere von dem Fluggerät nächstliegenden Hindernissen, ermöglicht wird.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie konnte jedoch keinen
Erfolg haben, da die Gegenstände des Patentanspruchs 1 und des nebengeordneten Patentanspruchs 6 nach Hauptantrag sowie des Patentanspruchs 1 und des
nebengeordneten Patentanspruchs 5 nach Hilfsantrag nicht auf erfinderischer
Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.     Gemäß dem mit einer möglichen Gliederung versehenen Patentanspruch 1
nach Hauptantrag betrifft die Anmeldung eine


(a)   Vorrichtung zur Farbkodierung von Umgebungsdarstellungen auf Anzeigeschirmen in Fluggeräten, insbesondere in Hubschraubern, mit:
(b)   einem Sensor zur Erfassung von Abstandsdaten zu umgebenden Elementen
      oder Objekten,
(c)   einer Einrichtung zur Verarbeitung der vom Sensor erfassten Abstandsdaten,
      die den Abstandsdaten entsprechend vorher festgelegten Abstandsbereichen
      verschiedene farbkodierte Farbbereiche zuweist und
(d)   diese Farben auf dem gesamten Anzeigeschirm darstellt,
(e)   wobei jeder Farbbereich durch RGB-Werte bei seinem Anfangs- und Endabstand definiert ist, und

                                                -8-



(f)   einer Einrichtung zum Interpolieren der RGB-Werte für die Abstände zwischen Anfangs- und Endabstand jedes Farbbereichs.


Zudem betrifft die Anmeldung gemäß dem Patentanspruch 6 nach Hauptantrag ein
entsprechendes Verfahren, wobei die im Anspruch 1 enthaltenen Vorrichtungsmerkmale dort als Verfahrensmerkmale formuliert sind.


Gemäß dem Anspruch 1 nach Hilfsantrag ist zusätzlich zu den Merkmalen des
Anspruchs 1 nach Hauptantrag vorgesehen


(g)   eine Einrichtung zum Interpolieren der RGB-Werte für die Abstände zwischen
      Anfangs- und Endabstand jedes Farbbereichs, welche die RGB-Werte mit
      dem folgenden linearen Algorithmus interpoliert:


          c = (d - dStart) / (dStop – dStart) * (cStop – cStart) + cStart
          wobei
          c        der berechnete R-, G- oder B-Wert ist,
          d        der aktuelle Abstand zwischen Sensor und Hindernis ist
          dStart   der Anfangsabstand des Farbbereichs ist,
          dStop    der Endabstand des Farbbereichs ist,
          cStart   der R-, G-, B-Wert beim Anfangsabstand ist, und
          cStop    der R-, G-, B-Wert beim Endabstand ist.


Ein entsprechendes zusätzliches Verfahrensmerkmal ist im nebengeordneten
Anspruch 5 nach Hilfsantrag enthalten.


Hinsichtlich der Anfangs- und Endwerte der Farbbereiche und der zugehörigen
Abstandsbereiche sind den Ansprüchen 1 und 6 gemäß Hauptantrag und den
Ansprüchen 1 und 5 gemäß Hilfsantrag keine Einschränkungen zu entnehmen;
von diesen Ansprüchen ist somit eine beliebige Einteilung umfasst. Im Ausführungsbeispiel gemäß der Tabelle auf S. 4 der Anmeldeunterlagen, das vom

                                       -9-



Anspruch 1 umfasst ist, werden Entfernungen, die größer als 2000 m sind, als
RGB-Wert Null, also schwarz angezeigt; Entfernungen kleiner als 9 m werden
durch einen einheitlichen RGB-Wert dargestellt. Der Anspruch 1 umfasst demnach
auch Einteilungen, nach denen alle über eine bestimmte Maximalentfernung
hinausgehenden Werte und ebenso alle unterhalb einer Minimalentfernung liegenden Entfernungswerte jeweils in einer einheitlichen Farbe (etwa schwarz für sehr
große Entfernungen, eine bestimmte Signalfarbe für sehr kleine Entfernungen)
angezeigt werden.


Als Fachmann sieht der Senat hier einen Ingenieur der Fachrichtung Informatik
an, der Erfahrung auf dem Gebiet der digitalen Bildverarbeitung besitzt.


2.    Die Gegenstände des geltenden Anspruchs 1 und des nebengeordneten
Anspruchs 6 nach Hauptantrag sowie des Anspruchs 1 und des nebengeordneten
Anspruchs 5 nach Hilfsantrag beruhen nicht auf einer erfinderischen Tätigkeit, da
sie dem Fachmann durch die vorveröffentlichte Druckschrift D1 nahegelegt waren.


Die Druckschrift D1 betrifft eine Hinderniswarnvorrichtung für Luft-, Raum- oder
Wasserfahrzeuge. Als Stand der Technik ist auf S. 3 le. Abs. bis S. 4 Abs. 1 ein
Flugzeugradarsystem beschrieben, bei dem ein vorgegebener Raumbereich
punktweise abgetastet und zu jedem abgetasteten Punkt die Entfernung zum Flugkörper bestimmt wird, wobei die einzelnen Bildpunkte auf einem Bildschirm koordinatengetreu wiedergegeben und dabei die Entfernung farblich kodiert wird. Hierdurch erhält man ein farbkodiertes Entfernungsbild, welches unter Verwendung
lediglich einer Radarwellenlänge erzeugt wurde. Gemäß S. 4 Abs. 2 erfordert ein
solches System vom Benutzer ein hohes Maß an Erfahrung und Aufmerksamkeit,
um die Objekte eines im Mikrowellenbereich (Radarbereich) aufgenommenen Bildes mit den Objekten im sichtbaren Bereich korrelieren zu können. Mit dem in D1
beschriebenen System soll dem Benutzer ein Bild angeboten werden, in dem
diese Korrelation bereits vorgenommen ist, vgl. S. 4 Abs. 3.

                                       - 10 -



D1 lehrt eine Hinderniswarnvorrichtung mit farbkodierter Entfernungsanzeige,
unter Anderem für Luftfahrzeuge, z. B. Hubschrauber, vgl. den dortigen
Anspruch 1 sowie S. 3 Abs. 1 und Abs. 2 Satz 1 - Merkmal (a) -, mit einem Sensor
(Radargerät), der unter Anderem die Entfernung von Objekten feststellt, vgl.
Anspruch 1 unter a) - Merkmal (b); zusätzlich kann die Geschwindigkeit der
Objekte erfasst werden. Außerdem ist eine Kamera vorgesehen, die ein elektronisches Bild liefert, vgl. Anspruch 1 unter b). Ist die Entfernung von erfassten Objekten kleiner als ein maximaler Abstandswert S1, so werden die zugehörigen Bildpunkte entsprechend der Objektentfernung (Abstand) verschiedenfarbig kodiert
auf einem Farbmonitor dargestellt, d. h. die Bildpunktentfernung wird farbkodiert
wiedergegeben, vgl. Anspruch 1 unter c) sowie S. 8 le. Abs. Satz 1 und 2; beispielsweise geht die Farbe der dargestellten Bildpunkte im Entfernungsbereich
zwischen S1 und einem minimalen Abstandswert S2 in 16 Stufen von grün nach
rot über, vgl. S. 9 Abs. 1 erster und zweiter vollständiger Satz. Geschwindigkeitsdaten können ebenfalls farbkodiert dargestellt werden, beispielsweise durch einen
Übergang von grün nach blau; auf die Geschwindigkeitsdarstellung kann beim
Einsatz als reines Entfernungswarngerät verzichtet werden, vgl. S. 6 le. Satz. Weiter als S1 entfernte Objekte werden einfarbig als von der Kamera geliefertes Bild
dargestellt, vgl. Anspruch 1 unter c). Zusätzlich zur optischen Anzeige kann bei
Unterschreitung der minimalen Entfernung S2 ein akustisches Warnsignal ausgegeben werden, vgl. Anspruch 3, wobei den akustischen Alarm auslösende (im sehr
nahen Bereich befindliche) Objekte auf dem Farbmonitor durch eine eigene Farbe
gekennzeichnet werden, vgl. S. 5 letzter Absatz; dies entspricht der Darstellung
von im extremen Nahbereich liegenden Gegenständen durch eine einheitliche
Farbe, wie sie im Ausführungsbeispiel der vorliegenden Anmeldung vorgenommen
wird, siehe oben.


Wie oben erwähnt, kann gemäß D1 die Farbe der dargestellten Bildpunkte im Entfernungsbereich zwischen S1 und S2 „z. B. in 16 Stufen von grün in rot“ übergehen. Somit werden den Anfangs- und Endabständen S1 und S2 sowie den Zwischenabständen Farbwerte zugeordnet; da die Farben auf einem Bildschirm dar-

                                      - 11 -



gestellt werden sollen, bietet sich die Verwendung von bei der Bildschirmdarstellung üblichen RGB-Werten an. Bei der Auswahl der Anzahl und Einteilung der Stufen, die der Fachmann demnach treffen muss, richtet er sich in naheliegender
Weise nach physiologischen Gesichtspunkten und/oder nach dem Gesichtspunkt
möglichst einfacher Berechnung aus den Anfangs- und Endwerten. Im Rahmen
des in D1 angesprochenen, stufenweisen Übergangs von grün (für weiter entfernte Objekte um S1) nach rot (für nahe Objekte um S2) ist z. B. eine Grobeinteilung nach physiologischen Gesichtspunkten naheliegend, etwa von einem Nahbereich (Gefahrenbereich), der dem Betrachter in roten Farben angezeigt wird, über
einen mittleren Bereich (Bereich einer nicht unmittelbaren, aber möglichen späteren Gefahr) mit gelben Farben zu einem weiter entfernten Bereich (nicht kritischer,
aber dennoch beobachtungswürdiger Entfernungsbereich) mit grünen Farben,
jeweils mit zugehörigen Anfangs- und Endwerten für Farbe und zugeordneten
Abstand - Merkmale (c), (e). Zur farbkodierten Feinabstufung der einzelnen Entfernungen innerhalb dieser Grobbereiche bietet sich in einfacher Weise eine Interpolation zwischen den jeweiligen Anfangs- und Endwerten an - Merkmal (f).


Gemäß der in D1 gegebenen Lehre werden Entfernungen nur bis zu einem (nicht
näher definierten) maximalen Entfernungsbereich farbig kodiert angezeigt; außerhalb dieses Bereichs erfolgt eine einfarbige (Intensitäts-)Darstellung des von der
Kamera gelieferten Bildes. Zudem wird in D1 auf einen Stand der Technik hingewiesen, gemäß dem lediglich die vom Radar gemessenen Entfernungswerte farbkodiert und somit auf dem gesamten Bildschirm angezeigt werden. Zwar ist hierbei
die Zuordnung zu Objekten im sichtbaren Bereich für den Betrachter schwieriger
(aber durchaus möglich); andererseits wird durch ein solches System, wie der
Fachmann ohne Weiteres erkennt, die Kamera und die zugehörige Verarbeitungselektronik eingespart. Für den kostenbewussten Fachmann liegt es somit nahe,
als billigere Grundversion des in D1 beschriebenen Systems ein Gerät vorzusehen, das keine Kamera aufweist und lediglich die über Radar gemessenen
Abstandsdaten farbkodiert auf dem gesamten Bildschirm darstellt (wobei über eine
Grenzentfernung hinausgehende Abstände, auf die es für die im Vordergrund ste-

                                          - 12 -



hende Warnung des Piloten vor nahen oder sich nähernden Objekten nicht
ankommt, einheitlich gefärbt sind, z. B. schwarz) - Merkmal (d).


Durch diese Überlegungen konnte der Fachmann zum Gegenstand des geltenden
Anspruchs 1 gelangen, wozu keine erfinderische Tätigkeit erforderlich war. Ein
über die zu erwartende Wirkung der einzelnen Maßnahmen hinausgehender,
synergistischer Effekt ist nicht ersichtlich.


Die Beschwerdeführerin ist dagegen der Ansicht, dass in D1 die natürliche Darstellung der Umgebung (Kamerabild) im Vordergrund stehe und die Farbkodierung
lediglich einen Zusatz zur Gefahrenerkennung darstelle; dagegen werde in der
vorliegenden Anmeldung ein künstliches Abstandsbild erzeugt, wobei die sich bis
in die Hintergrundsbereiche erstreckende Farbkodierung mit Interpolation eine
Orientierungshilfe biete, ohne dass eine Kamera erforderlich sei.


Dem ist entgegenzuhalten, dass dem Anspruch 1 gemäß Haupt- und Hilfsantrag
keine bestimmten Anfangs- und Endwerte für die Abstandsbereiche (auch nicht für
Hintergrundsbereiche) und ebenso keine bestimmten zugeordneten Farbwerte zu
entnehmen sind, so dass im Hinblick auf die Abstandseinteilung und Farbkodierung sowie die dadurch erzeugten Effekte kein Unterschied zu dem durch D1
Nahegelegten bestehen kann. Das Weglassen der in D1 vorgesehenen Kamera
ergibt sich wie oben dargelegt für den Fachmann aus dem in D1 beschriebenen
Stand der Technik, der bereits ein künstlich erzeugtes Abstandsbild betrifft, unter
Berücksichtigung naheliegender wirtschaftlicher Erwägungen.


Der Anspruch 1 nach Hauptantrag ist nach dem oben Ausgeführten nicht gewährbar.
Entsprechendes gilt für den auf ein Verfahren gerichteten, nebengeordneten
Anspruch 6 nach Hauptantrag.

                                        - 13 -



Wie oben bereits dargelegt, bietet sich dem Fachmann als einfache Möglichkeit für
die farbkodierte Feinabstufung von Entfernungen innerhalb grober Bereiche eine
Interpolation zwischen den Anfangs- und Endfarbwerten entsprechend den zugehörigen Abstandswerten an. Die rechnerisch einfachste und damit für den Fachmann naheliegende Lösung hierfür ist eine lineare Interpolation. Zur Berechnung
eines zu einer bestimmten Entfernung gehörigen Farbwerts setzt der Fachmann
die Anfangs- und Endgrößen in die ihm aus seinem mathematischen Grundwissen
bekannte lineare Interpolationsformel ein - Merkmal (g).
Damit beruht auch der Anspruch 1 und ebenso der nebengeordnete Anspruch 5
nach Hilfsantrag nicht auf einer erfinderischen Tätigkeit.


Auch der Anspruch 1 und der nebengeordnete Anspruch 5 nach Hilfsantrag sind
nicht gewährbar.


Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
jeweiligen abhängigen Patentansprüche (2 bis 5 und 7 bis 9 nach Hauptantrag, 2
bis 4, 6 und 7 nach Hilfsantrag) nicht gewährbar (BGH in GRUR 1997, 120 „Elektrisches Speicherheizgerät“).


3.    Die Rückzahlung der Beschwerdegebühr war gemäß § 80 Abs. 3 PatG
anzuordnen. Danach ist die Beschwerdegebühr zurückzuzahlen, wenn dies der
Billigkeit entspricht. Maßgebend dafür sind alle Umstände des Falles. Die Billigkeit
der Rückzahlung kann sich danach aus der Sachbehandlung durch das Deutsche
Patent- und Markenamt ergeben (vgl. Benkard, Patentgesetz Gebrauchsmustergesetz, 10. Auflage (2006), PatG § 80 Rdnr. 21; Schulte, Patentgesetz, 8. Auflage
(2008), § 80 Rdnr. 111, 112 sowie § 73 Rdn. 132 ff.), wenn diese für die Erhebung
der Beschwerde ursächlich war. Dies ist hier der Fall.


Die Prüfungsstelle hat neue, von der Anmelderin eingereichte Patentansprüche
nicht in einem weiteren Prüfungsbescheid gewürdigt; zudem hat sie die Anmeldung 5 Jahre nach Einreichung dieser neuen Ansprüche ohne weiteren Hinweis

                                      - 14 -



zurückgewiesen, obwohl die Anmelderin etwa fünf Wochen vor Erlass dieses
Zurückweisungsbeschlusses eine Sachstandsanfrage an die Prüfungsstelle gerichtet hatte, die mit der Bitte um Erlass eines weiteren Prüfungsbescheides verbunden war. Diese Sachstandsanfrage ist laut Vermerk telefonisch lediglich mit
dem Hinweis auf „Weiterführung“, nicht aber auf Erlass eines Zurückweisungsbeschlusses beantwortet worden. Diese Vorgehensweise stellt in ihrer Gesamtheit
eine unbillige Sachbehandlung dar und war ursächlich für die Beschwerdeerhebung.


Die Prüfungsstelle hat in ihrem einzigen Prüfungsbescheid vom 3. Februar 1999
mangelnde Neuheit gegenüber D1 als Grund für die Nichtgewährung des ursprünglichen Patentanspruchs 1 angegeben; dagegen hat sie im Beschluss vom
20. September 2004 das Patentbegehren mangels erfinderischer Tätigkeit gegenüber D1 und D2 zurückgewiesen, wobei diesem Beschluss ein geänderter Patentanspruch 1 zugrundelag. Zwar hat die Prüfungsstelle im Prüfungsbescheid ergänzend auf die Druckschrift D2 hingewiesen, die (unter anderem) die Merkmale der
ursprünglichen Unteransprüche 2 bis 4 für das allgemein als „depth-cueing“
bekannte Verfahren beschreibe; da auch in den übrigen Unterlagen nicht erkennbar sei, worauf ein gewährbares Patentbegehren gerichtet werden könnte, könne
die Erteilung eines Patents nicht in Aussicht gestellt werden. Zu der Frage, welche
Veranlassung der Fachmann gehabt hätte, die Lehre der Druckschriften D1 und
D2 so zu kombinieren, dass er zum Gegenstand eines aus den ursprünglichen
Ansprüchen 1 bis 4 zusammengesetzten Patentanspruchs gelangt wäre, sind dem
Bescheid jedoch keine Ausführungen zu entnehmen. Es erscheint zudem fraglich,
ob die Anmelderin aus diesem Bescheid den im Beschluss genannten Zurückweisungsgrund hinreichend deutlich entnehmen konnte. Da allerdings im Prüfungsbescheid letztlich auf den zur Zurückweisung führenden Stand der Technik hingewiesen wurde, rechtfertigen diese Mängel allein vorliegend eine Rückzahlung der
Beschwerdegebühr noch nicht.

                                     - 15 -



Jedoch ist zusätzlich eine ungewöhnlich lange Zeit, nämlich über fünf Jahre, zwischen der Vorlage neuer Patentansprüche und dem Zurückweisungsbeschluss
verstrichen. Der Prüfungsstelle ist zugute zu halten, dass diese lange Wartezeit
wohl durch die Überlastung des Deutschen Patent- und Markenamts bedingt war.
Der Erlass des Zurückweisungsbeschlusses erfolgte jedoch als Reaktion auf eine
Sachstandsanfrage der Anmelderin, die mit der Bitte um einen weiteren Prüfungsbescheid verbunden war.


Angesichts dieser Gesamtumstände stellte der Erlass eines Zurückweisungsbeschlusses eine unbillige Sachbehandlung dar.


Die Anmelderin hat ihr Patentbegehren auf den Prüfungsbescheid hin eingeschränkt und eine sachliche Stellungnahme abgegeben. Sie hat somit ihre Bereitschaft erkennen lassen, an einer zielgerichteten Weiterführung des Verfahrens
mitzuwirken und auch auf Einwände der Prüfungsstelle einzugehen. Sie konnte,
nachdem sie über fünf Jahre nach ihrer Eingabe um einen weiteren Prüfungsbescheid gebeten hatte, darauf vertrauen, nicht durch einen Zurückweisungsbeschluss überrascht zu werden, sondern zunächst noch eine weitere Beurteilung
durch die Prüfungsstelle zu erhalten. Dass hinsichtlich der Gründe für die mangelnde Patentfähigkeit der Anmeldung noch Klärungsbedarf bestand, zeigen
sowohl die (im Gegensatz zum Prüfungsbescheid) detaillierten Ausführungen der
Prüfungsstelle zu diesem Punkt im Zurückweisungsbeschluss als auch die ebenfalls ins Einzelne gehenden Ausführungen der Anmelderin in der Beschwerdebegründung, in der diese auf die Argumentation des Zurückweisungsbeschlusses
eingeht.


Es erscheint durchaus denkbar, dass durch einen weiteren Bescheid (mit Erwiderungsmöglichkeit) oder im Rahmen einer Anhörung Einvernehmen über die Sachund Rechtslage erzielt und das Verfahren so weit hätte gefördert werden können,
dass die Anmelderin auf die Einlegung der Beschwerde verzichtet hätte. Diese
Möglichkeit ist der Anmelderin durch den erst nach langer Zeit auf ihre sachliche

                                      - 16 -



Eingabe und damit für die Anmelderin überraschend erfolgten Zurückweisungsbeschluss auf unbillige Weise genommen worden.


Nach alledem war die Sachbehandlung der Anmeldung durch die Prüfungsstelle
mängelbehaftet und ursächlich für die Beschwerdeerhebung, so dass die Rückzahlung der Beschwerdegebühr der Billigkeit entspricht.




Dr. Fritsch               Eder                 Prasch         Dr. Thum-Rung




                                                                          Fa
