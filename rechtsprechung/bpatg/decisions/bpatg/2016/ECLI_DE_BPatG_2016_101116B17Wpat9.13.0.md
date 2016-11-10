---
ecli: "ECLI:DE:BPatG:2016:101116B17Wpat9.13.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 9/13"
decided: "2016-11-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2016&Sort=1&Seite=51&nr=28534&anz=906&pos=767&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2016-11-10_17_W-pat_9_13_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 17 W (pat) 9/13 vom 2016-11-10

## Entscheidung

BUNDESPATENTGERICHT



    17 W (pat) 9/13
_______________________

    (Aktenzeichen)




                             BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2009 018 928.9


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts
in der Sitzung am 10. November 2016 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek,   der    Richterin   Eder,    der   Richterin
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel




BPatG 152
08.05

                                          -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und Markenamts vom 14. September 2012 aufgehoben und das Patent mit folgenden Unterlagen erteilt:


       Patentansprüchen 1 bis 8 vom 20. September 2016, wobei im
       Patentanspruch 1 in Merkmal c) „der der Hauptachse“ in „der
       Hauptachse“ geändert wird und im Patentanspruch 7 der Ausdruck „der Nebenachsen-Koordinatenwert nicht korrigiert wird“
       geändert wird in „der Nebenachsen-Koordinatenwert des Startpunkts nicht korrigiert wird“,

       Beschreibung Seiten 1 und 2 vom 18. Juli 2016, eingegangen am
       20. Juli 2016,

       Beschreibung Seiten 3 bis 39, eingegangen am 12. Juni 2009,

       18 Blatt Zeichnungen mit Figuren 1, 2, 6, 18 bis 32, eingegangen
       am 12. Juni 2009,

       15 Blatt Zeichnungen mit Figuren 3 bis 5, 7 bis 17, 33 vom
       11. November 2009.




                                        Gründe:


                                           I.


Die vorliegende Patentanmeldung ist am 28. April 2009 beim Deutschen Patentund Markenamt in englischer Sprache eingereicht worden. Sie beansprucht die

                                          -3-



Priorität einer japanischen Voranmeldung vom 27. Juni 2008 und trägt in der deutschen Übersetzung die Bezeichnung


                                „Linienzeichenverfahren“.


Die Prüfungsstelle für Klasse G06T hat in der Anhörung vom 14. September 2012
die Anmeldung zurückgewiesen, da der jeweilige Anspruch 1 des damals geltenden Hauptantrags und der damals geltenden Hilfsanträge 1 und 2 nicht klar, eindeutig und präzise erkennen ließen, was als patentfähig unter Schutz gestellt werden soll (§ 34 Abs. 3 Nr. 3 PatG).


Gegen diesen Beschluss wendet sich die am 17. November 2012 eingegangene
Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt sinngemäß,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        -   Patentansprüchen 1 bis 8 vom 20. September 2016,

        -   Beschreibung Seiten 1 und 2 vom 18. Juli 2016, eingegangen
            am 20. Juli 2016,

        -   Beschreibung Seiten 3 bis 39, eingegangen am 12. Juni 2009,

        -   18 Blatt Zeichnungen mit Figuren 1, 2, 6, 18 bis 32, eingegangen am 12. Juni 2009,

        -   15 Blatt Zeichnungen mit Figuren 3 bis 5, 7 bis 17, 33 vom
            11. November 2009.

                                       -4-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: US 7 307 628 B1

        D2: US 5 729 750 A

        D3: OpenGL SuperBible: „14 Rasterization and Operations on the
        Framebuffer”, 22. Juni 2008, S. 1 bis 5; mit Altersnachweis gemäß Internet
        Archive WayBack,
        http://www.opengl.org/resources/faq/technical/rasterization.htm

        D4: Segal, M. et al.: The Open GL Graphics System: A Specification.
        Version 1.1 vom 4.3.1997, URL:
        http://www.graphics.stanford.edu/courses/cs448a-01-fall/GLspec1.1.pdf

        D5: Sun, C. et al.: Hardware Acceleration for Spatial Selections and
        Joins; Proc. ACM SIGMOD International Conference on Management of
        Data, 2003, S. 455 bis 466

        D6: US 2004/0139080 A1

        D7: US 2008/0062204 A1

        D8: OpenGL-Forumseintrag vom September 2003, URL:
        http://www.opengl.org/discussion_boards/showthread.php/147055-2D-
        linerendering?p=1054333#post1054333

        D9: „Processing“-Forumseintrag von 2007, URL:
        http://processing.org/bugs/bugzilla/501.html


Die geltenden Patentansprüche 1 bis 8 lauten (mit markierten Korrekturen von
offensichtlichen Fehlern):

                              -5-



„1.   Linienzeichenverfahren zum Zeichnen einer Linie, deren Koordinaten
gegeben sind, auf einem Bildschirm, auf dem Pixel angeordnet sind, gemäß einer Diamond-Exit-Regel, welches Verfahren die Schritte umfasst:

a)    Bestimmen einer horizontalen oder vertikalen Achse als Hauptachse,
je nachdem, ob der Betrag der Differenz zwischen den x-Koordinatenwerten des Endpunkts und des Startpunkts der Linie größer oder kleiner ist
als der Betrag der Differenz zwischen den y-Koordinatenwerten des Endpunkts und des Startpunkts,

b)    Korrigieren der Koordinatenwerte des Startpunkts und/oder des Endpunkts der Linie,

b1) wobei der Hauptachsen-Koordinatenwert des Startpunkts nur dann
korrigiert wird, wenn dieser im Äußeren des Rautenrahmens eines Pixels
liegt, wobei der Hauptachsen-Koordinatenwert des Startpunkts zum
Hauptachsen-Koordinatenwert des Mittelpunkts desjenigen Pixels korrigiert wird, in dem ein vom Startpunkt ausgehendes Liniensegment zum
ersten Mal einen Rautenrahmen von innen nach außen kreuzt, und

b2) was den Endpunkt anbelangt, dessen Hauptachsen-Koordinatenwert
zum Hauptachsen-Koordinatenwert des Mittelpunkts desjenigen Pixels
korrigiert wird, in dem ein zum Endpunkt hinlaufendes Liniensegment zum
letzten Mal einen Rautenrahmen von innen nach außen kreuzt,

c)    Ermitteln, ob eine Richtung entlang der der Hauptachse von dem
Startpunkt zu dem Endpunkt der Linie nach der Korrektur dieselbe wie vor
der Korrektur ist;

d)    wenn die Richtungen entlang der Hauptachse vor und nach der Korrektur nicht übereinstimmen, ermitteln, ob ganzzahlige Werte der Hauptachsen-Koordinaten des Startpunktes und des Endpunktes nach der Korrektur dieselben sind; und

                                -6-



e)      Zeichnen mindestens eines Pixels,

e1) wenn die Richtungen entlang der Hauptachse vor und nach der Korrektur dieselben sind oder

e2) die Richtungen entlang der Hauptachse vor und nach der Korrektur
verschieden sind, und ferner ganzzahlige Werte der Hauptachsen-Koordinaten des Startpunkts und des Endpunkts nach der Korrektur dieselben
sind.

2.      Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird und, was die
Koordinaten des Endpunkts anbelangt, der Hauptachsen-Koordinatenwert
korrigiert wird und der Nebenachsen-Koordinatenwert nicht korrigiert wird.

3.      Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird, und was die
Koordinaten des Endpunkts anbelangt, der Hauptachsen-Koordinatenwert
korrigiert wird, und zur Korrektur des Nebenachsen-Koordinatenwerts das
Produkt aus der Bewegungsdistanz der Hauptachsenkoordinate und dem
Neigungswert der Linie zum Nebenachsen-Koordinatenwert addiert wird.

4.      Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird und, was die
Koordinaten des Endpunkts anbelangt sowohl der Hauptachsen-Koordinatenwert als auch der Nebenachsen-Koordinatenwert bis an den Mittelpunkt desjenigen Pixels korrigiert werden, in dem ein zum Endpunkt hinlaufendes Liniensegment zum letzten Mal einen Rautenrahmen von innen
nach außen kreuzt.

5.      Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird und, wenn der
Hauptachsen-Koordinatenwert des Startpunkts korrigiert wird, auch der
Nebenachsen-Koordinatenwert des Startpunkts korrigiert wird, indem das

                                -7-



Produkt aus der Bewegungsdistanz der Hauptachsenkoordinate und dem
Neigungswert der Linie zum Nebenachsen-Koordinatenwert addiert wird.

6.   Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird und, wenn der
Hauptachsen-Koordinatenwert des Startpunkts korrigiert wird, auch der
Nebenachsen-Koordinatenwert des Startpunkts korrigiert wird, und zwar
zum Nebenachsen-Koordinatenwert des Mittelpunkts desjenigen Pixels, in
dem ein vom Startpunkt ausgehendes Liniensegment zum ersten Mal
einen Rautenrahmen von innen nach außen kreuzt.

7.   Linienzeichenverfahren nach Anspruch 1, bei dem die zur Hauptachse senkrechte Achse als Nebenachse spezifiziert wird und der Nebenachsen-Koordinatenwert des Startpunkts nicht korrigiert wird.

8.   Vorrichtung zur Durchführung des Linienzeichenverfahrens nach Anspruch 1 umfassend:

einen Korrigierer (10) zum Bestimmen der Hauptachse und zur Durchführung der Korrektur der Koordinatenwerte des Startpunkts und/oder des
Endpunkts einer Linie gemäß den Merkmalen a), b), b1) und b2);

eine erste Sektion (11), die konﬁguriert ist, um zu bestimmen, ob die Richtung entlang der Hauptachse von dem Startpunkt zu dem Endpunkt der
Linie nach Korrektur dieselbe wie vor der Korrektur ist;

eine zweite Sektion (12), die konfiguriert ist, um, wenn die Richtungen entlang der Hauptachse vor und nach der Korrektur nicht übereinstimmen, zu
ermitteln, ob ganzzahlige Werte die Hauptachsen-Koordinaten des Startpunkts und des Endpunkts nach der Korrektur dieselben sind; und

eine Zeichensektion (13), die konﬁguriert ist, um mindestens ein Pixel zu
zeichnen, wenn die Richtungen entlang der Hauptachse vor und nach der
Korrektur verschieden sind und ferner ganzzahlige Werte der Hauptach-

                                       -8-



          sen-Koordinaten des Startpunkts und des Endpunkts nach der Korrektur
          dieselben sind.“


Zu den weiteren Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat auch Erfolg, da ein Patent nach dem nunmehr geltenden Antrag erteilt werden
kann.


1.      Gegenstand der Patentanmeldung ist ein Linienzeichenverfahren zum
Zeichnen von Linien auf einem Bildschirm (Offenlegungsschrift Abs. [0001]).


Die Anmeldung geht aus von der bekannten DiamondExit-Regel zum Zeichnen
von Linien; diese hat den Vorteil, dass kontinuierliche Linien lückenlos gezeichnet
werden, wobei Pixel auch nicht zweimal gezeichnet werden (Offenlegungsschrift
Abs. [0002]). Nach der DiamondExit-Regel wird jedem (rechteckigen) Pixel eine
Raute („diamond“) einbeschrieben (Fig. 3). Jedes von einer zu zeichnenden Linie
getroffene Pixel wird genau dann gezeichnet, wenn die Linie innerhalb des Pixels
die Raute verlässt, d. h. wenn es in Linienrichtung einen Übergang vom Inneren
der Raute zum Außenbereich der Raute gibt. In bestimmten Fällen wird dann zwar
am Startpunkt einer Linie ein Pixel gezeichnet, am Endpunkt aber nicht (Fig. 4
und 5).


Diese Regel kann zu Problemen führen, insbesondere bei sehr kurzen Linien (mit
einer Länge kleiner als 1 Pixelbreite), wobei abhängig von den Positionen des
Startpunktes und Endpunktes der Linie ein Pixel oder kein Pixel gezeichnet wird
(Offenlegungsschrift Abs. [0003]; Fig. 6 mit Beschreibung).

                                        -9-



Wenn durch eine digitale Schaltung eine Logik realisiert werden soll, die für alle
denkbaren Muster von Start- und Endpunkten einer Linie angibt, wie die Start- und
Endpunkte wiederzugeben sind, führe dies zu einem großen Schaltungsumfang
und zu langsamer Prozessgeschwindigkeit. Deshalb werde eine DiamondExit-Regel gewünscht, die zum Zeichnen von sehr kurzen Linien angewendet werden
könne, und die mit einer einfachen Logik realisiert werden könne (Offenlegungsschrift Abs. [0004]).


Der Erfindung soll daher die Aufgabe zugrunde liegen, ein Linienzeichenverfahren
vorzusehen, bei dem keine Linie unterbrochen wird und das mit einer einfacheren
Logik mit hoher Geschwindigkeit realisiert werden kann (Offenlegungsschrift Abs.
[0005], geltende Beschreibung Seite 2 Abs. 4).


In der Anmeldung wird ein Verfahren beschrieben, mit dessen Hilfe die Diamond
Exit-Regel für den kritischen Fall des Zeichnens von sehr kurzen Linien variiert
wird, nämlich mit Hilfe eines geeigneten, relativ einfachen Algorithmus, der berechnet, ob insbesondere für eine sehr kurze Linie Pixel gezeichnet werden oder
nicht.


Zunächst wird ermittelt, ob die Linie eher horizontal oder eher vertikal ausgerichtet
ist (Hauptachse; Fig. 2 Schritt S2; Merkmal a)).
Sodann werden die Koordinaten des Startpunkts und des Endpunkts der zu zeichnenden Linie verschoben („korrigiert“, Merkmal b)). Diese „Korrektur“ ist für den
Startpunkt und für den Endpunkt unterschiedlich und wird zumindest für den jeweiligen Hauptachsen-Koordinatenwert durchgeführt. Der Hauptachsen-Koordinatenwert des Startpunkts wird nur dann korrigiert, wenn der Startpunkt im Äußeren des
Rautenrahmens eines Pixels liegt, und zwar wird dann der Hauptachsen-Koordinatenwert des Startpunkts zum Hauptachsen-Koordinatenwert des Mittelpunkts
desjenigen Pixels korrigiert, in dem ein vom Startpunkt ausgehendes Liniensegment zum ersten Mal einen Rautenrahmen von innen nach außen kreuzt (Merkmal b1)). Der Hauptachsen-Koordinatenwert des Endpunkts wird dagegen zum

                                           - 10 -



Hauptachsen-Koordinatenwert des Mittelpunkts desjenigen Pixels korrigiert, in
dem ein zum Endpunkt hinlaufendes Liniensegment zum letzten Mal einen Rautenrahmen von innen nach außen kreuzt (Merkmal b2)).
Somit wird im Wesentlichen zumindest die Hauptachsen-Koordinate eines zu korrigierenden Start- bzw. Endpunkts zur Hauptachsen-Koordinate des Mittelpunkts
des zugehörigen Pixels oder eines durch die Linie getroffenen Nachbarpixels verschoben (korrigiert); vgl. Abs. [0070] und [0071] der Offenlegungsschrift sowie die
Ausführungsbeispiele gemäß Fig. 8 ff. mit der zugehörigen Beschreibung.


Das weitere Vorgehen zeigen insbesondere Fig. 24A, 24B und 25 i. V. m. Abs.
[0114] bis [0117]:


Sowohl vor als auch nach der Korrektur wird eine Richtung entlang der Hauptachse vom Start- zum Endpunkt ermittelt (etwa im Fall „horizontal“: von links nach
rechts oder von rechts nach links; die Richtungen vor und nach der Korrektur werden verglichen (Fig. 2 Schritte S3 und S4; Merkmal c)). Ist die Richtung vor und
nach der Korrektur gleich, so wird mindestens ein Pixel gezeichnet (Pixel A in
Fig. 24 A; Fig. 2 Schritt S5; Merkmale e) mit e1)); dies entspricht in etwa dem üblichen DiamondExit-Fall, der bei längeren Linien auftritt.
Im Fall von sehr kurzen Linien kann es vorkommen, dass die Richtung zwischen
Start- und Endpunkt nach der Korrektur zur Richtung vor der Korrektur unterschiedlich   ist,    da   der   Endpunkt    sozusagen   „über   den   Startpunkt   hinaus“ zurückverschoben wird, vgl. Fig. 24B und Fig. 25. Wenn eine Übereinstimmung dieser Richtungen nicht gegeben ist, wird geprüft, ob der Start- und der
Endpunkt nach der Korrektur im selben Pixel liegen (ob ganzzahlige Werte ihrer
Koordinaten dieselben sind; Fig. 2 Schritte S6, S7; Merkmal d)). Ist dies der Fall,
so wird ein Pixel gezeichnet (Pixel A in Fig. 24 B; Merkmale e) mit e2)); wenn
nicht, wird kein Pixel gezeichnet (Fig. 25).

                                      - 11 -



Als Fachmann ist hier ein Informatiker oder Programmierer anzusehen, der Erfahrung in der Entwicklung von Verfahren zur Wiedergabe von Daten auf einem Bildschirm, insbesondere von Linienzeichnungsverfahren besitzt.


2.     Die nunmehr geltenden Unterlagen liegen im Rahmen der ursprünglichen
Offenbarung.


Der geltende Anspruch 1 geht hervor aus dem ursprünglichen Anspruch 1 sowie
den oben unter Punkt 1. genannten Stellen in der Beschreibung und den Figuren.
Entsprechendes gilt für den nebengeordneten Anspruch 8.


Die Merkmale der Unteransprüche 2 bis 7, welche die Korrektur des jeweiligen
Nebenachsen-Koordinatenwerts des Startpunkts und des Endpunkts betreffen,
gehen zurück auf Fig. 8 bis 17 mit der zugehörigen Beschreibung.


Alle Ansprüche sind somit ursprünglich offenbart.


Die ebenfalls zulässigen Änderungen in der Beschreibung betreffen teilweise die
Darlegung des Standes der Technik, teilweise ergeben sie sich aus den geänderten Ansprüchen.


3.     Das Verfahren gemäß dem Anspruch 1 und ebenso die Vorrichtung gemäß
dem nebengeordneten Anspruch 8 sind neu gegenüber dem belegten Stand der
Technik und beruhen auf erfinderischer Tätigkeit.


Dies ergibt sich aus der Würdigung der zum Stand der Technik genannten Druckschriften und Unterlagen.


3.1.   Aus dem druckschriftlich belegten Stand der Technik war vor dem Anmeldetag der vorliegenden Patentanmeldung Folgendes bekannt:

                                      - 12 -



Die Druckschrift D1 behandelt das Entfernen („culling“) von kleinen Primitiven (Linien, Dreiecke), die nicht durch ein Pixel wiedergegeben werden, vor einer Bilddarstellung. Fig. 1 zeigt die in OpenGL angewandte DiamondExit-Regel, nach der
ein von einer Linie getroffenes Pixel nur dann gezeichnet werden soll, wenn die
Linie eine dem Pixel einbeschrieben Raute (diamond) verlässt; vgl. auch Fig. 4.
Um nicht zu zeichnende, kleine Primitive einfach zu entfernen, wird ein Rautenbzw. Diamond-Koordinatensystem mit inneren und äußeren Rauten definiert
(Fig. 5), und die Anfangs- und Endpunkte von Primitiven werden als „innerhalb
einer Raute“, „außerhalb einer Raute“ und „Ecke“ klassifiziert und in dieses Koordinatensystem transformiert (Fig. 5 und 6 mit Beschreibung). Eine Linie wird dann
entfernt (nicht gezeichnet), wenn ihre beiden Endpunkte in derselben Raute liegen, oder wenn ihr Startpunkt in einer äußeren Raute und ihr Endpunkt in einer
benachbarten inneren Raute liegen (Sp. 12 Mitte); dies entspricht im Wesentlichen
der DiamondExit-Regel. Ob eine solche Bedingung erfüllt ist, wird durch Betrachtung der Rautenkoordinaten der Start- und Endpunkte ermittelt (Fig. 7).


D2 betrifft die automatische Dimensionierung im Computer Aided Design (CAD).
Aus gegebenen CAD-Daten werden horizontale und vertikale sowie geneigte oder
gebogene Liniensegmente mit ihren Endpunkten extrahiert, in entsprechenden
Tabellen registriert und zusammen mit der Richtung bzw. Orientierung von x- und
y-Verlängerungslinien gespeichert. Mit Hilfe dieser Daten werden vorläufige x- und
y-Dimensionierungslinien erzeugt; diese werden umgeordnet, so dass kleinere
Dimensionierungslinien näher an dem betrachteten CAD-Teil liegen als größere.
Im Fall von verbundenen geneigten oder gebogenen Segmenten mit horizontalen
oder vertikalen Segmenten werden die gemeinsamen Endpunktkoordinaten angepasst (Kap. „Summary of the Invention“).


D3 betrifft OpenGL. Unter Abschnitt 14.090 ist die DiamondExit-Regel angegeben;
möglicherweise können Linien in OpenGL nicht exakt durch Pixel wiedergegeben
werden. Die DiamondExit-Regel ist auch in Abschnitt 14.120 erwähnt, wobei als

                                       - 13 -



Ausweg     aus   einer   ungenügenden       Rasterung     einer   Linie   ein   „line
loop“ vorgeschlagen wird.


D4 beschreibt in Kap. 3.4 mit 3.4.1 die Rasterung von Liniensegmenten in
OpenGL. Zunächst wird eine horizontale oder vertikale Hauptachse für das Liniensegment ermittelt („x-major or y-major“, Kap. 3.4.1 Abs. 1). Zur Rasterung wird
eine „DiamondExit“-Regel verwendet (Kap. 3.4.1 Abs. 2, Fig. 3.4). Um Schwierigkeiten zu vermeiden, wenn der Endpunkt einer Linie auf dem Diamond-Rahmen
liegt, werden die Koordinaten der Endpunkte um einen sehr kleinen Betrag gestört
(S. 60 le. Abs. bis S. 61 Abs. 2). Es sind auch Variationen des Algorithmus erlaubt,
wobei einige Regeln eingehalten werden müssen; insbesondere besagt Regel 1,
dass die Koordinaten eines (zu zeichnenden) Fragments (Pixels) nicht um mehr
als eine Einheit in x- und y-Koordinaten (d. h. um eine Pixelbreite) von dem durch
die DiamondExit-Regel erzeugten Fragment abweichen darf (S. 61 Abs. 3).


D5 beschreibt in Kap. 2 eine Graphik-Hardware zum Rastern mit OpenGL-Eigenschaften. In Kap. 2.2.2 Abs. 1 i. V. m. Fig. 3(c) ist das Rastern von Liniensegmenten nach der DiamondExit-Regel beschrieben. Es ist auch das Problem angesprochen, dass kleine Liniensegmente verschwinden können, was als äußerst unerwünscht angesehen wird (S. 458 re. Sp. Abs. 2 i. V. m. Fig. 3(d)). Gemäß Kap. 4.1
wird eine Graphikkarte mit einem NVIDIA - Prozessor und Speicher verwendet.
Eine Lösung für das Problem des Verschwindens kleiner Liniensegmente im Sinne
der vorliegenden Anmeldung ist in D5 nicht zu erkennen.


D6 betrifft ein Navigationssystem mit einem Renderer, der beispielsweise mit
OpenGL arbeiten kann (Abstract, Abs. [0065].


D7 betrifft die Wiedergabe von Linien auf einem Display. Damit durch Pixel dargestellte Linien oder Kurven auf einem Display nicht „gezackt“ aussehen, wird oft ein
„Anti-aliasing“ durchgeführt, wobei Pixel im „gezackten“ Teil der Kurve mehr oder
weniger grau dargestellt werden (Abs. [0001]). Insbesondere im Fall von horizon-

                                        - 14 -



talen oder vertikalen Linien kann dies jedoch zu dem unerwünschten Effekt führen,
dass solche Linien unscharf wirken (Abs. [0002]). Um dies zu vermeiden, lehrt D7,
horizontale und vertikale Führungslinien (202, 208 in Fig. 2 und 3, 210 in Fig. 2
und 4), welche zu zeichnende dünne Linien repräsentieren, zu den nächstgelegenen Pixel-Mittellinien (304, 308 in Fig. 3, 404 in Fig. 4) hin zu verschieben. Durch
dieses „pixel snapping“ werden die Pixel von den verschobenen Linien mittig getroffen und schwarz (oder weiß) gezeichnet, ohne umgebende graue Pixel, was
die gezeichneten Linien scharf und sauber erscheinen lässt. Für geneigte Linien
kann deren Symmetrieachse (212 in Fig. 2 und 4) zu einer Pixelmittellinie (408 in
Fig. 8) hin verschoben werden, was ebenfalls zu einem schärferen, relativ sauberen Seheindruck führt (vgl. in Fig. 4 unten die schrägen Dreieckslinien).


In D8 ist das Problem angesprochen, dass in OpenGL, das nach der DiamondExit-Regel arbeitet, Endpunkte von Linien oft nicht gezeichnet werden. Es wird diskutiert, zur Lösung die Fensterkoordinaten um einen konstanten Wert von etwa
0.375 zu verschieben.


D9 spricht dasselbe Problem an wie D8. Eine konstante Verschiebung wird ebenfalls diskutiert, die jedoch nicht alle (Konsistenz-)Probleme lösen kann.


3.2.   Das Verfahren des Anspruchs 1 und ebenso das System des nebengeordneten Anspruchs 8 sind gegenüber diesem Stand der Technik neu und beruhen
auf erfinderischer Tätigkeit.


Aus dem Stand der Technik sind Linienzeichnungsverfahren nach der Diamond
Exit-Regel bekannt, auch mit einer Korrektur von Endpunkten im Sinne einer Koordinatenverschiebung (D4, D7, D8, D9). Ein Vergleich von Richtungen (entlang
einer Achse) vor und nach der Korrektur, wobei abhängig vom Ergebnis Pixel gezeichnet werden (Merkmale b), c), d)), ist in diesen Druckschriften jedoch nicht
vorgesehen.

                                            - 15 -



Das Verfahren des Anspruchs 1 ist somit neu.


Im bisher bekannt gewordenen Stand der Technik ist auch nicht die Möglichkeit
vorgesehen, dass die Richtung zwischen Start- und Endpunkt entlang einer Achse
vor und nach der Korrektur verschieden ist. Die genannten Druckschriften legen
es damit nicht nahe, die eventuelle Verschiedenheit der beiden Richtungen abzufragen und ergebnisabhängig Pixel zu zeichnen, wobei im Fall von unterschiedlichen Richtungen noch geprüft wird, ob die Start- und Endpunkte nach der Korrektur noch im selben Pixel liegen wie vor der Korrektur.


Damit ist dem Verfahren des Patentanspruchs 1 auch eine erfinderische Tätigkeit
nicht abzusprechen.


Entsprechendes gilt für den nebengeordneten, auf eine Vorrichtung gerichteten
Patentanspruch 8.


4.     Der geltende Patentanspruch 1 und ebenso der nebengeordnete Patentanspruch 8 sind gewährbar.


Die abhängigen Patentansprüche 2 bis 7 sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.




                                Rechtsmittelbelehrung:


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

                                          - 16 -



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




Dr. Morawek                    Eder            Dr. Thum-Rung                   Dr. Forkel




                                                                                       Fa
