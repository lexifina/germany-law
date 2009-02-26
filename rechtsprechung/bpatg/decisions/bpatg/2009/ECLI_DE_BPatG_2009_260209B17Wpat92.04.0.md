---
ecli: "ECLI:DE:BPatG:2009:260209B17Wpat92.04.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 92/04"
decided: "2009-02-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2009&Sort=1&Seite=14&nr=11995&anz=1436&pos=220&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2009-02-26_17_W-pat_92_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0014.md"]
---

# Bundespatentgericht, 17 W (pat) 92/04 vom 2009-02-26

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 92/04                                                    Verkündet am
_______________                                                     26. Februar 2009
    (Aktenzeichen)                                                         …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 196 00 431.4-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. Februar 2009 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch, des Richters Dipl.-Ing. Prasch sowie
der Richterin Eder und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
08.05

                                      -2-



beschlossen:


                       Die Beschwerde wird zurückgewiesen.




                                   Gründe:


                                       I.


Die vorliegende Patentanmeldung ist am 8. Januar 1996 unter Beanspruchung der
US-amerikanischen Priorität 08/370669 vom 10. Januar 1995 beim Deutschen
Patent- und Markenamt unter der Bezeichnung


        „Computergraphik-Pixel-Wiedergabesystem mit Cache-Speichern“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 4. Juni 2004 die
Anmeldung zurückgewiesen, da der Gegenstand des Patentanspruchs 1 durch
Aufnahme eines bestimmten Merkmals unzulässig erweitert worden sei. Auf S. 4
le. Abs. bis S. 5 Abs. 1 dieses Beschlusses hat sie zudem sinngemäß ausgeführt,
dass im Falle einer Interpretation des besagten Merkmals im ursprünglich offenbarten Sinne dieses Merkmal die Patentfähigkeit des Patentanspruchs 1 nicht
begründen könne, da es bereits aus dem im Verfahren befindlichen Stand der
Technik bekannt sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.

                                          -3-



Die Beschwerdeführerin beantragt mit Eingabe vom 16. Januar 2009,


       den Beschluss der Prüfungsstelle vom 4. Juni 2004 aufzuheben und ein
             Patent auf Grundlage des mit Eingabe vom 16. Januar 2009 eingereichten Satzes von Ansprüchen 1 bis 12 gemäß Hauptantrag, den
             ursprünglich eingereichten Beschreibungsseiten 1 bis 19 und den
             ursprünglich eingereichten Figuren 1 bis 8 zu erteilen,


       hilfsweise, den Beschluss der Prüfungsstelle vom 4. Juni 2004 aufzuheben und ein Patent auf Grundlage des mit Eingabe vom 16. Januar 2009 eingereichten Satzes von Ansprüchen 1 bis 10 gemäß Hilfsantrag, den ursprünglich eingereichten Beschreibungsseiten 1 bis 19
             und den ursprünglich eingereichten Figuren 1 bis 8 zu erteilen.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden, die bereits von der Anmelderin in den Anmeldeunterlagen aufgeführt wurden:


       D1: Pineda, J.: A Parallel Algorithm for Polygon Rasterization, Computer
       Graphics, Vol. 22, No. 4, August 1988, S. 17 bis 20


       D2: Computer Graphics: Principles and Practice, Hrsg. James D. Foley,
       2. Ausgabe, Addison-Wesley 1990, S. 883 bis 886 und 887 bis 907.


Der geltende Patentanspruch 1 nach Hauptantrag lautet:


       „1.     Computergraphikverfahren zur Abtastverarbeitung von Grundformen
       zwecks Generierung von Anzeige-Pixeln, wie sie z.B. in einem Vollbild-Puffer vorliegen, wobei die Lage der Pixel in einem Bildschirmraum eine
       definierte Beziehung zu einem Anzeige-Bildraum aufweist, umfassend folgende Schritte:

                                      -4-



       Definieren von Grundformen in Relation zu einer Mehrzahl von Tafeln (A-H), die jeweils mehrere Spannen enthalten, wobei jede Spanne (120, 122)
       zweidimensional ist und eine Mehrzahl von aneinander angrenzenden
       Pixeln des Anzeige-Bildraums enthält;


       Abtasten der Tafeln (A-H), um Spannen ausfindig zu machen;


       reihenweises Abtasten der Spannen, um überlappte Spannen mit überlappten Pixeln innerhalb einer Grundform ausfindig zu machen, indem die
       Reihen der einzelnen Spannen nacheinander in wechselnden Richtungen
       abgetastet werden;


       Abtasten von Pixeln im Inneren der überlappten Spannen, um überlappte
       Pixel für die Verarbeitung ausfindig zu machen, und


       Verarbeiten der abgetasteten überlappten Pixel, Pixel für Pixel und
       Spanne für Spanne, um Pixeldaten für den Vollbildpuffer bereitzustellen.“


Der nebengeordnete Patentanspruch 8 nach Hauptantrag lautet:


       „8.   Computergraphiksystem zur Abtast-Verarbeitung von Grundformen
       zwecks Generierung von Pixeldaten für eine einen Bildraum aufweisende
       Anzeigeeinheit, umfassend:


       einen Vollbildpuffer, der so organisiert ist, daß er eine vorbestimmte
       Raumbeziehung zu dem Bildraum der Anzeigeeinheit aufweist;


       eine Einrichtung, die den Vollbildpuffer in eine Mehrzahl von Tafeln unterteilt, die jeweils mehrere Spannen enthalten, von denen jede Spanne zweidimensional ist und eine Mehrzahl von Pixeln beinhaltet;

                                      -5-



       einen Abtaster zum Abtasten der Tafeln (A-H), um Spannen innerhalb
       einer Grundform und innerhalb einer Tafel ausfindig zu machen, zum reihenweisen Abtasten der Spannen in abwechselnder Reihen-Richtung, um
       Pixel in einer Grundform und einer Spanne und somit Pixel für die Verarbeitung zu lokalisieren, und


       einen Prozessor zum Verarbeiten der Pixel in einer Grundform, einer Tafel
       und einer Spanne, um Pixeldaten in dem Vollbildpuffer bereitzustellen.“


Der Patentanspruch 1 nach Hilfsantrag lautet:


       „1.   Computergraphikverfahren zur Abtastverarbeitung von Grundformen
       zwecks Generierung von Anzeige-Pixeln, wie sie z.B. in einem Vollbild-Puffer vorliegen, wobei die Lage der Pixel in einem Bildschirmraum eine
       definierte Beziehung zu einem Anzeige-Bildraum aufweist, umfassend folgende Schritte:


       Definieren von Grundformen in Relation zu einer Mehrzahl von Tafeln (A-H), die jeweils mehrere Spannen enthalten, wobei jede Spanne (120, 122)
       zweidimensional ist und eine Mehrzahl von aneinander angrenzenden
       Pixeln des Anzeige-Bildraums enthält;


       Abtasten der Tafeln (A-H), um Spannen ausfindig zu machen;


       reihenweises Abtasten der Spannen, um überlappte Spannen mit überlappten Pixeln innerhalb einer Grundform ausfindig zu machen, indem die
       Reihen der einzelnen Spannen nacheinander in wechselnden Richtungen
       abgetastet werden;


       Abtasten von Pixeln im Inneren der überlappten Spannen, um überlappte
       Pixel für die Verarbeitung ausfindig zu machen, und

                                         -6-



       Verarbeiten der abgetasteten überlappten Pixel, Pixel für Pixel und
       Spanne für Spanne, um Pixeldaten für den Vollbildpuffer bereitzustellen,


       bei dem der Verarbeitungsschritt durch mehrere Wiedergabeprozessoren (P1-P8) durchgeführt wird.“


Der nebengeordnete Patentanspruch 7 nach Hilfsantrag lautet:


       „7.   Computergraphiksystem zur Abtast-Verarbeitung von Grundformen
       zwecks Generierung von Pixeldaten für eine einen Bildraum aufweisende
       Anzeigeeinheit, umfassend:


       einen Vollbildpuffer, der so organisiert ist, daß er eine vorbestimmte
       Raumbeziehung zu dem Bildraum der Anzeigeeinheit aufweist;


       eine Einrichtung, die den Vollbildpuffer in eine Mehrzahl von Tafeln unterteilt, die jeweils mehrere Spannen enthalten, von denen jede Spanne zweidimensional ist und eine Mehrzahl von Pixeln beinhaltet;


       einen Abtaster zum Abtasten der Tafeln (A-H), um Spannen innerhalb
       einer Grundform und innerhalb einer Tafel ausfindig zu machen, zum reihenweisen Abtasten der Spannen in abwechselnder Reihen-Richtung, um
       Pixel in einer Grundform und einer Spanne und somit Pixel für die Verarbeitung zu lokalisieren,


       einen Prozessor zum Verarbeiten der Pixel in einer Grundform, einer Tafel
       und einer Spanne, um Pixeldaten in dem Vollbildpuffer bereitzustellen, und


       mehrere Wiedergabeprozessoren (P1, P2, ...) zum Verarbeiten der Pixel.“

                                       -7-



Der Anmeldung soll gemäß der Eingabe vom 8. Juni 1998 Seite 3 vorle. Abs. die
Aufgabe zugrunde liegen, ein Computergraphikverfahren und -system zu schaffen,
die es ermöglichen, Grundformen in einer Art und Weise zu verarbeiten, die einer
bestimmten Vollbildpuffer-Organisation am besten Rechung trägt.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                         II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie hat jedoch keinen
Erfolg, da die Gegenstände des jeweiligen Patentanspruchs 1 und ebenso die
Gegenstände des jeweils nebengeordneten Patentanspruchs nach Haupt- und
Hilfsantrag nicht auf erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit
§ 4 Satz 1 PatG).


1.    Die Anmeldung betrifft ein Computergraphikverfahren.
Wie in der Beschreibung ausgeführt, werden bei Computergraphikverfahren die
Oberflächen von darzustellenden Gegenständen üblicherweise aus einer Vielzahl
von definiert im Raum angeordneten Grundformen (z. B. Dreiecken) zusammengesetzt. Für die Darstellung werden mit Hilfe der Grundformdaten Helligkeitswerte
von zeilen- und spaltenweise angeordneten Bildpunkten (Pixel) berechnet, in
einem Vollbild-Pufferspeicher abgelegt und für die Bildschirmanzeige verwendet.
Bei der Berechnung werden für jede Grundform die zugehörigen Pixel abgetastet
und mit Helligkeitswerten versehen. In der Anmeldung geht es im Wesentlichen
um die Reihenfolge der Abarbeitung der Pixel in einer Grundform, die mit Hilfe
eines oder mehrerer Prozessoren durchgeführt wird.


Der mit einer möglichen Gliederung versehene Patentanspruch 1 nach Hauptantrag betrifft (nach Weglassen der Bezugszeichen) ein

                                      -8-



       a) Computergraphikverfahren zur Abtastverarbeitung von Grundformen
       zwecks Generierung von Anzeige-Pixeln, wie sie z. B. in einem Vollbild-Puffer vorliegen, wobei die Lage der Pixel in einem Bildschirmraum eine
       definierte Beziehung zu einem Anzeige-Bildraum aufweist, umfassend folgende Schritte:


       b) Definieren von Grundformen in Relation zu einer Mehrzahl von Tafeln,
       die jeweils mehrere Spannen enthalten, wobei jede Spanne zweidimensional ist und eine Mehrzahl von aneinander angrenzenden Pixeln des
       Anzeige-Bildraums enthält;


       c) Abtasten der Tafeln, um Spannen ausfindig zu machen;


       d) reihenweises Abtasten der Spannen, um überlappte Spannen mit
       überlappten Pixeln innerhalb einer Grundform ausfindig zu machen, indem
       die Reihen der einzelnen Spannen nacheinander in wechselnden Richtungen abgetastet werden;


       e) Abtasten von Pixeln im Inneren der überlappten Spannen, um überlappte Pixel für die Verarbeitung ausfindig zu machen, und


       f)   Verarbeiten der abgetasteten überlappten Pixel, Pixel für Pixel und
       Spanne für Spanne, um Pixeldaten für den Vollbildpuffer bereitzustellen.


Gemäß dem Patentanspruch 1 nach Hilfsantrag ist zusätzlich vorgesehen, dass


       g) der Verarbeitungsschritt durch mehrere Wiedergabeprozessoren
       durchgeführt wird.


Der ebenfalls mit einer möglichen Gliederung versehene nebengeordnete
Anspruch 8 nach Hauptantrag betrifft ein

                                      -9-



       A) Computergraphiksystem zur Abtast-Verarbeitung von Grundformen
       zwecks Generierung von Pixeldaten für eine einen Bildraum aufweisende
       Anzeigeeinheit, umfassend:


       B) einen Vollbildpuffer, der so organisiert ist, daß er eine vorbestimmte
       Raumbeziehung zu dem Bildraum der Anzeigeeinheit aufweist;


       C) eine Einrichtung, die den Vollbildpuffer in eine Mehrzahl von Tafeln
       unterteilt, die jeweils mehrere Spannen enthalten, von denen jede Spanne
       zweidimensional ist und eine Mehrzahl von Pixeln beinhaltet;


       D) einen Abtaster zum Abtasten der Tafeln, um Spannen innerhalb einer
       Grundform und innerhalb einer Tafel ausfindig zu machen, zum reihenweisen Abtasten der Spannen in abwechselnder Reihen-Richtung, um Pixel in
       einer Grundform und einer Spanne und somit Pixel für die Verarbeitung zu
       lokalisieren, und


       E) einen Prozessor zum Verarbeiten der Pixel in einer Grundform, einer
       Tafel und einer Spanne, um Pixeldaten in dem Vollbildpuffer bereitzustellen.


Gemäß dem nebengeordneten Patentanspruch 7 nach Hilfsantrag enthält das
System zusätzlich


       F) mehrere Wiedergabeprozessoren zum Verarbeiten der Pixel.


Gemäß den geltenden Ansprüchen nach Haupt- und Hilfsantrag ist somit eine
dreistufige Abtastung einer Grundform (Tafel - Spanne - Pixel) vorgesehen.


Zur Auslegung der Patentansprüche ist zu ermitteln, was sich aus der Sicht des
angesprochenen Fachmanns aus den Merkmalen des Patentanspruchs im Einzel-

                                       - 10 -



nen und in ihrer Gesamtheit als unter Schutz gestellte technische Lehre ergibt, vgl.
BGH X ZB 9/06 17. April 2007 - Informationsübermittlungsverfahren (Leitsatz 2).
Zur Auslegung sind die Beschreibung und die Zeichnungen heranzuziehen, vgl.
§ 14 S. 2 PatG alg. Subjektive Vorstellungen des Anmelders sind nicht mitbestimmend für den geschützten (analog für den zu schützenden) Gegenstand, vgl. BGH
X ZR 23/97 vom 13. April 1999 (Kap. III. 4, m. w. N.).


Wie der Fachmann, hier ein Ingenieur der Fachrichtung Informatik mit Erfahrung
auf dem Gebiet der Computergraphikverfahren und der entsprechenden Systeme
erkennt, beziehen sich im vorliegenden Fall die Ansprüche 1 und 8 nach Hauptantrag auf die Abtastung gemäß Fig. 5 bis 7 mit der zugehörigen Beschreibung (zum
Anspruch 1 nach Hilfsantrag ist zusätzlich Fig. 8 und die zugehörige Beschreibung
heranzuziehen). Aus diesen Offenbarungsstellen entnimmt der Fachmann, dass
zur Abtastung einer Grundform zunächst die Tafeln ermittelt werden, die zumindest
teilweise mit der Grundform überlappen. In jeder Tafel werden die Spannen abgetastet und ermittelt, welche zumindest teilweise mit der Grundform überlappen
(überlappte Spannen); hierbei werden die Spannen nacheinander reihenweise in
wechselnden Richtungen abgetastet, vgl. die die Abtastung mehrerer Spannen
hintereinander zeigende mäanderförmige Linie in Fig. 5. Durch Abtasten der Pixel
im Inneren dieser überlappten Spannen werden die mit der Grundform überlappten Pixel ermittelt.
Dieser Sachverhalt wird im Anspruch 1 nach Hauptantrag und Hilfsantrag durch
die Merkmale c) bis e) und ebenso im jeweiligen nebengeordneten Anspruch
durch das Merkmal D) ausgedrückt.


2.     Der Erteilungsantrag liegt im Rahmen der ursprünglichen Offenbarung.


Die geltenden Ansprüche 1 nach Haupt- und Hilfsantrag, die der Fachmann im
oben angegebenen Sinn interpretiert, gehen aus den ursprünglichen Ansprüchen 1, 4 und 7 i. V. m. Fig. 5 und 6 mit der zugehörigen Beschreibung hervor. Die
geltenden nebengeordneten Ansprüche nach Haupt- und Hilfsantrag gehen aus

                                       - 11 -



den ursprünglichen Ansprüchen 10 und 13 i. V. m. Fig. 5 und 6 mit der zugehörigen Beschreibung hervor. Die jeweiligen Unteransprüche gehen aus den noch verbleibenden ursprünglichen Unteransprüchen zu den ursprünglichen Ansprüchen 1
und 10 hervor.


Die Ansprüche nach Haupt- und Hilfsantrag sind somit in den ursprünglichen
Unterlagen offenbart und sind zulässig.


3.   Die Gegenstände des jeweiligen Anspruchs 1 und des jeweiligen nebengeordneten Anspruchs nach Hauptantrag und nach Hilfsantrag beruhen nicht auf
einer erfinderischen Tätigkeit, da sie sich für den Fachmann in naheliegender
Weise aus seinem Fachwissen i. V. m. dem Stand der Technik ergaben.


Das Fachbuch D2 zeigt in Fig. 18.15 auf S. 885 oben einen prinzipiellen Aufbau
zur Abtastverarbeitung für Computergraphik zwecks Generierung von Anzeige-Pixeln, mit einem Prozessor (rasterizer) zur Rasterung von vorgegebenen (vorher
definierten) Grundformen (primitives), einem Bildpuffercache (pixel cache) und
einem Vollbildpuffer (frame buffer) - Merkmale a, A, B und teilweise b. Der Vollbildpuffer ist in mehrere (hier sechzehn) Partitionen unterteilt - teilweise Merkmal C.
Den Partitionen können jeweils Prozessoren zur parallelen Verarbeitung zugeordnet werden, wobei jeder Prozessor Grundformen in seinem Teil des Vollbildpuffers
verarbeitet, vgl. S. 887 vorle. Abs. - Merkmale g, F. Eine Möglichkeit zur Aufteilung
der Pixel auf die Partitionen ist das „contiguous partitioning“, vgl. Fig. 18.17 (a)
i. V. m. Abschnitt „Contiguous partitioning“ auf S. 887 unten bis S. 888 oben; hierbei enthält jede Partition alle Pixel eines ihr zugeordneten Pixelblocks (Region).
Grundformen brauchen nur in den Regionen bearbeitet zu werden, in denen sie
sichtbar sein könnten. Diese (überlappten) Regionen können durch geometrische
Verfahren schnell ermittelt werden.
Nur die in der Grundform liegenden Pixel einer Zeile werden verarbeitet, vgl.
S. 884 „Span processing“ - teilweise Merkmal e. Durch die beschriebene Abtas-

                                       - 12 -



tung und Verarbeitung werden Pixeldaten für den Bildspeicher bereitgestellt - teilweise Merkmale f und E.


Die Druckschrift D1 betrifft das Rastern von Polygonen für Computergraphik. In
den Figuren 3, 4 und 6 ist das pixelweise Abtasten eines Polygons (Dreiecks) in
alternierenden Reihen dargestellt. Fig. 7 und die Beschreibung auf S. 20 li. Sp.
Abs. 2 u. 3 zeigt die Einteilung eines Vollbildpuffers in Blöcke (entsprechend D2
Fig. 18.14), auf die parallel zugegriffen werden kann; als Ergebnis der Verarbeitung können Dreiecke mit Helligkeitsverlauf („shaded triangles“) erzeugt werden.
Somit ist wie in D2 eine zweistufige Abtastung offenbart.


Wie das Fachbuch D2 zeigt, waren dem Fachmann bereits Computergraphikverfahren und -systeme mit zweistufiger Abtastung von Grundformen (Block - Pixel)
bekannt, wobei Grundformen nur in den mit ihnen überlappten Pixelblöcken bzw.
Regionen bearbeitet werden. Die zeitaufwendige Abtastung und Verarbeitung der
Pixel (untere Abtaststufe) wird somit vorteilhaft auf relevante, mit der Grundform
überlappte Regionen (obere Abtaststufe) beschränkt, die schnell ermittelt werden
können, vgl. D2 S. 887 letzter Absatz. Bei größeren Regionen, wie sie im Fall des
„contiguous partitioning“ von großen, eine Vielzahl von Pixeln enthaltenden Bildern
und Vollbildspeichern auftreten, vgl. D2 Fig. 18.17 (a) auf S. 887, liegt es für den
Fachmann nahe, die Verarbeitung innerhalb einer Region ebenso zu beschränken,
d. h. zum Zweck der Zeitersparnis die Region in kleinere Einheiten (Spannen) zu
unterteilen und nur die mit der Grundform überlappten Spannen im Hinblick auf
überlappte Pixel zu verarbeiten (wobei die Spannen nacheinander abgetastet werden müssen, um überlappte Spannen zu ermitteln). Hiermit wird das bekannte
zweistufige Verfahren auf ein dreistufiges erweitert, wobei die Regionen den Tafeln
in der vorliegenden Anmeldung entsprechen - Merkmale b, c, C, e, E, f, teilweise
d, D. Hinsichtlich der Abtastreihenfolge ist dem Fachmann eine Abtastung von zeilen- und spaltenförmig angeordneten Einheiten sowohl in jeweils gleicher Zeilenrichtung als auch in abwechselnder Zeilenrichtung bekannt, vgl. zur letztgenannten Alternative die Druckschrift D1 Fig. 3, 4 und 6. Für die Abtastung der Spannen

                                         - 13 -



eine dieser bekannten Alternativen auszuwählen, etwa die letztgenannte, die den
bekannten Vorteil der aufeinanderfolgenden Verarbeitung jeweils benachbarter
Einheiten bietet, stellt eine für den Fachmann naheliegende Maßnahme dar - restlicher Teil der Merkmale d, D.


Durch diese Überlegungen ist der Fachmann bereits beim Verfahren gemäß dem
Anspruch 1 nach Hauptantrag und ebenso beim System gemäß dem nebengeordneten Anspruch 8 nach Hauptantrag angelangt, ohne erfinderisch tätig werden zu
müssen.


Der Anspruch 1 nach Hauptantrag ist nicht gewährbar, ebenso wenig der nebengeordnete Anspruch 8 nach Hauptantrag.


Nachdem gemäß D2 bereits mehrere Prozessoren zum Verarbeiten der Pixel eingesetzt werden, kann auch dieses zusätzliche Merkmal beim Verfahren gemäß
dem Anspruch 1 nach Hilfsantrag und ebenso beim System gemäß dem nebengeordneten Anspruch 7 nach Hilfsantrag keine erfinderische Tätigkeit begründen.


Auch der Anspruch 1 und der nebengeordnete Anspruch 7 nach Hilfsantrag sind
nicht gewährbar.


Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
jeweiligen abhängigen Patentansprüche (2 bis 7 und 9 bis 12 nach Hauptantrag
sowie 2 bis 6 und 8 bis 10 nach Hilfsantrag) nicht gewährbar (BGH in GRUR 1997,
120 „Elektrisches Speicherheizgerät“).




Dr. Fritsch              Eder                     Prasch         Dr. Thum-Rung




                                                                                Fa
