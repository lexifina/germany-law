---
ecli: "ECLI:DE:BPatG:2011:150311B17Wpat93.06.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 93/06"
decided: "2011-03-15"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=18&nr=19056&anz=1310&pos=276&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-03-15_17_W-pat_93_06_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 93/06 vom 2011-03-15

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 93/06                                                    Verkündet am
_______________                                                      15. März 2011
    (Aktenzeichen)                                                        …




                               BESCHLUSS

                             In der Beschwerdesache


               betreffend die Patentanmeldung 103 44 805.5-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 15. März 2011 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Fritsch,   der   Richterin   Eder,     des   Richters
Dipl.-Ing. Baumgardt und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
08.05

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                        I.


Die vorliegende Patentanmeldung ist am 26. September 2003 beim Deutschen
Patent- und Markenamt unter der Bezeichnung


               „Verfahren zur automatischen Objektmarkierung in der
                            medizinischen Bildgebung“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 25. April 2006 die
Anmeldung zurückgewiesen, da der Patentanspruch 1 mangels Erfindungshöhe
seines Gegenstandes nicht gewährbar sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:

                                        -3-



        gemäß Hauptantrag mit Patentansprüchen 1 bis 18 vom Anmeldetag,
        Beschreibung Seiten 1 bis 14 vom 13. August 2004, eingegangen
        am 17. August 2004, 2 Blatt Zeichnungen mit 2 Figuren vom Anmeldetag,


        gemäß Hilfsantrag I mit Patentansprüchen 1 bis 17 vom 22. November 2006, eingegangen am 27. November 2006, noch anzupassender Beschreibung und Zeichnungen mit Figuren, jeweils
        wie Hauptantrag,


        gemäß Hilfsantrag II mit Patentanspruch 1, überreicht in der
        mündlichen Verhandlung, Patentansprüchen 2 bis 18 vom Anmeldetag, im Übrigen wie Hilfsantrag I,


        gemäß Hilfsantrag III mit Patentansprüchen 1 bis 15, überreicht in
        der mündlichen Verhandlung, im Übrigen wie Hilfsantrag I.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: US 2002/028006 A1
        D2: US 6 246 784 B1.


Vom Senat wurde zusätzlich die von der Anmelderin selbst genannte Druckschrift


        D3: Jendrysiak, U: Segmentierung von Schnittbildern. Spektrum der Wissenschaft, 1/1999, S. 24-29


eingeführt.

                                       -4-



Zu den Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie konnte jedoch keinen
Erfolg haben, da die Gegenstände des Patentanspruchs 1, des nebengeordneten
Patentanspruchs 17 und des nebengeordneten Patentanspruchs 18 nach Hauptantrag sowie des jeweiligen Patentanspruchs 1 nach den Hilfsanträgen I, II und III,
der nebengeordneten Patentansprüche 16 und 17 nach Hilfsantrag I, der nebengeordneten Patentansprüche 17 und 18 nach Hilfsantrag II und der nebengeordneten Patentansprüche 14 und 15 nach Hilfsantrag III nicht auf erfinderischer
Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.   Die Patentanmeldung betrifft ein Verfahren zur automatischen Objektmarkierung in der medizinischen Bildgebung sowie ein entsprechendes System, außerdem ein Computersoftwareprodukt.
In der Beschreibungseinleitung ist das Problem der Segmentierung verschiedener
Gewebe in medizinischen Bilddatensätzen angesprochen. Insbesondere sei es
schwierig, Tumore und andere pathologische Veränderungen, die im Rahmen gängiger bildgebender Verfahren zu gesundem Gewebe kaum kontrastieren, gut differenzierbar darzustellen. Es werden verschiedene in der Medizintechnik bekannte
Darstellungsverfahren erläutert. Hinsichtlich der Segmentierung wird auf die
Druckschrift D3 hingewiesen, gemäß der die Segmentierung schwer differenzierbarer Objekte wie etwa Tumore über Texturmaße einer Fläche (etwa über Eigenschaften der Häufigkeitsverteilung der Grauwerte in der Fläche, z. B. mittlerer
Grauwert, Standardabweichung) erfolge. In einem ersten Schritt werde von einer
Startregion (Polygonzug) ausgegangen und über die Texturmaße innerhalb und
außerhalb der Startregion eine grobe Eingrenzung des Tumors ermittelt. In einem
zweiten Schritt werde die Umgebung abgesucht und das Ergebnis im Randbereich
optimiert. Die Genauigkeit an den Rändern lasse oft noch zu wünschen übrig.

                                      -5-



Aufgabe der vorliegenden Anmeldung sei es daher, ein Verfahren, ein System
sowie ein Computersoftwareprodukt bereitzustellen, mit welchem schwach kontrastierende, aber doch in sich geschlossene zusammengehörige Objekte in medizinischen 2D- bzw. 3D-Bilddatensätzen selektiv hervorgehoben und dadurch direkt
und gut differenzierbar in ihrer entsprechenden Umgebung dargestellt werden können, vgl. S. 5 Abs. 2 der geltenden Beschreibung.


Der Patentanspruch 1 nach Hauptantrag betrifft ein


       Verfahren zur automatischen Objektmarkierung in der medizinischen Bildgebung,

       aufweisend die folgenden Schritte:

       - (S1)    gekoppeltes Darstellen unterschiedlicher Darstellungsweisen zumindest eines Bilddatensatzes, welcher zumindest ein zu markierendes
       Objekt enthält, in jeweils unterschiedlichen Displayfenstern auf zumindest
       einem Bildschirm eines Rechners,

       - (S2)    Übergeben der Position eines im Rahmen einer objektbestimmenden Erstmarkierung durch einen Anwender angewählten Initialpunktes
       an den Rechner,

       - (S3)    Anwenden von Techniken der Mustererkennung auf die Umgebung des Initialpunktes der Erstmarkierung mit dem Ergebnis einer detaillierten hochaufgelösten Zweitmarkierung des Objektes,

       - (S4)    reversibles Codieren der Zweitmarkierung der im Rechner vorliegenden Bilddatensätze, und

       - (S5)    Hervorheben des markierten Objektes relativ zu seiner Umgebung in den Bilddatensätzen auf dem Bildschirm.

                                      -6-



Zudem betrifft die Anmeldung gemäß dem Patentanspruch 17 nach Hauptantrag
ein


       System, das zur Durchführung des Verfahrens nach den Ansprüchen 1 bis
       16 geeignet ist


und gemäß dem nebengeordneten Patentanspruch 18 nach Hauptantrag ein


       Computersoftwareprodukt

       dadurch gekennzeichnet,

       dass es ein Verfahren nach einem der Ansprüche 1 bis 16 implementiert,
       wenn es auf einer mit einem gemäß Anspruch 17 ausgeführten System
       verbundenen Recheneinrichtung läuft.


Der Patentanspruch 1 gemäß Hilfsantrag I ist auf ein Verfahren zur automatischen
Objektmarkierung in der medizinischen Bildgebung mit den Schritten (S1) bis (S5)
des Anspruchs 1 nach Hauptantrag gerichtet und enthält das zusätzliche Merkmal


       a) dass das Markieren und Hervorheben des zu markierenden Objektes
       insofern komplementär erfolgt, als dass zunächst identifizierbares Gewebe
       entsprechend der Schritte (S1) bis (S3) identifiziert und vormarkiert wird
       und anschließend alle nicht vormarkierten eingeschlossenen Voxelbereiche markiert werden und die Vormarkierung aufgehoben wird.


Im Patentanspruch 1 gemäß Hilfsantrag II sind gegenüber dem Patentanspruch 1
nach Hauptantrag die Schritte (S4) und (S5) ersetzt durch


       - (S4*) reversibles Codieren der Zweitmarkierung der im Rechner vorliegenden Bilddatensätze, wobei den Voxeln des Bilddatensatz jeweils Grauwerte mit einer geringen Farbtiefe von 12 Bit zugeordnet sind und mit Hilfe

                                        -7-



        einer Transferfunktion die Grauwerte eines jeden Voxels auf eine Farbund Helligkeitsskala verschoben werden und dabei jedem Voxel eine
        erhöhte Farbtiefe von 16 Bit zugewiesen wird, und wobei dem Anwender
        ein Hin- und Herschalten zwischen der Farb- und Helligkeitsskala und den
        ursprünglichen Grauwerten ermöglicht ist und

        - (S5*) Hervorheben des markierten Objektes relativ zu seiner Umgebung in den Bilddatensätzen auf dem Bildschirm, indem die Farb- und Helligkeitszuordnung mittels der Transferfunktion durch eine anwenderbasierende Parameterkonfiguration der Transferfunktion erfolgt

(Änderungen gegenüber den Schritten S4 und S5 sind hervorgehoben).


Im Patentanspruch 1 gemäß Hilfsantrag III sind ausgehend vom Patentanspruch 1
gemäß Hilfsantrag II die Schritte (S1), (S2) und (S3) ersetzt durch


        - (S1*) gekoppeltes Darstellen unterschiedlicher Darstellungsweisen zumindest eines Bilddatensatzes, welcher zumindest ein zu markierendes
        Objekt enthält, in jeweils unterschiedlichen Displayfenstern auf zumindest
        einem Bildschirm eines Rechners, wobei ein erster Bilddatensatz erhalten
        ist mit einer ersten Bildgebungsmodalität

        - (S2*) Übergeben der Position eines im Rahmen einer objektbestimmenden Erstmarkierung durch einen Anwender angewählten Initialpunktes
        an den Rechner, wobei das Finden des Initialpunktes durch den Rechner
        automatisch erfolgt und zum automatischen Finden eines Ausgangsvoxels
        als Initialpunkt Bilder weiterer Bildgebungsmodalitäten herangezogen werden, in welchen der zentrale Bereich des zu markierenden Objekts bestmöglichen Kontrast zeigt

        - (S3*) Anwenden einer Abfolge oder Kombinationen von Techniken der
        Mustererkennung auf die Umgebung des Initialpunktes der Erstmarkierung

                                       -8-



        mit dem Ergebnis einer detaillierten hochaufgelösten Zweitmarkierung des
        Objektes,

(Änderungen gegenüber den Schritten S1, S2 und S3 sind hervorgehoben).


Die nebengeordneten Ansprüche 16 und 17 des Hilfsantrags I, 17 und 18 des
Hilfsantrags II sowie 14 und 15 des Hilfsantrags III entsprechen den nebengeordneten Ansprüchen 17 und 18 des Hauptantrags, jeweils unter Anpassung der
Rückbeziehungen.


Der Anspruch 1 nach Hauptantrag ist in Verbindung mit Fig. 1 und der zugehörigen Beschreibung als Abfolge mehrerer Schritte zu verstehen. Zunächst werden
ein oder mehrere Bilddatensätze in unterschiedlicher Darstellungsweise (z. B.
zwei- und dreidimensional), aber sich entsprechender Ansicht in unterschiedlichen
Displayfenstern dargestellt, wobei die Ansicht in gekoppelter Weise (durch den
Anwender) verändert, z. B. gedreht werden kann (Schritt S1). Ist eine optimale
Ansicht gefunden, so wählt der Anwender einen Punkt (z. B. ein Voxel) aus (Erstmarkierung), dessen Position an den Rechner übergeben wird (Schritt S2). Diese
Position dient als Ausgangspunkt für eine rechnerbasierte Segmentierung, die
gemäß Schritt S3 mittels bekannter Techniken der Mustererkennung (Texturerkennung, Region Growing, Randerkennung, vgl. S. 10 Abs. 2 und 3 der ursprünglichen Beschreibung), insbesondere als Abfolge oder Kombinationen solcher
Techniken (Schritt S3*, Hilfsantrag III) in der Umgebung des Initialpunktes durchgeführt wird, und deren Ergebnis eine „detaillierte hochaufgelöste Zweitmarkierung“ (ein segmentiertes Objekt in den Bilddaten) ist (Schritt S3). Die Zweitmarkierung wird in Schritt S4 reversibel codiert (dem segmentierten Objekt wird z. B. ein
bestimmter Farbbereich reversibel zugewiesen), und das so markierte, segmentierte Objekt wird (relativ zu seiner Umgebung) auf dem Display angezeigt
(Schritt S5).

                                       -9-



Im Anspruch 1 nach Hilfsantrag I ist gemäß Merkmal a) zusätzlich die Möglichkeit
vorgesehen, die Markierung komplementär vorzunehmen, d. h. die vorläufige Markierung eines segmentierten Bereichs zu invertieren (Aufheben der Markierung
der segmentierten Bereiche und Markieren der komplementären Menge der bisher
nicht markierten, eingeschlossenen Umgebungsbereiche). Damit können gemäß
S. 13 Abs. 2 der ursprünglichen Beschreibung schwer zu identifizierende Bereiche
(z. B. schwer von der Nachbarumgebung zu unterscheidendes Tumorgewebe)
hervorgehoben werden, indem in den Schritten S1 bis S3 nicht der Tumor, sondern das umgebende, gesunde Gewebe segmentiert wird und durch Invertieren
die eingeschlossenen, schwer zu identifizierenden Bereiche markiert werden. Aus
der Anmeldung geht nicht hervor, ob und ggfs. wie bei dieser Markierung zwischen
eingeschlossenen und nicht eingeschlossenen Hintergrundbereichen unterschieden werden soll; Merkmal a) ist somit nicht auf eine Markierung lediglich der eingeschlossenen Hintergrundbereiche beschränkt, sondern umfasst auch eine Markierung aller Hintergrundbereiche einschließlich der eingeschlossenen Bereiche.


Die Schritte S4* und S5* im Patentanspruch 1 nach Hilfsantrag II sind im Lichte
von Fig. 2 und der zugehörigen Beschreibung in den Anmeldeunterlagen so zu
interpretieren, dass jedes ursprüngliche Voxel des Bilddatensatzes als mit 12 Bit
codierter Grauwert vorliegt, d. h. es können Grauwerte von 0 bis 4096 (oberes
Ende der 12 Bit-Hounsfield-Skala, siehe Fig. 2 linke Hälfte) auftreten. Nach dem
Segmentieren wird jedem Voxel entsprechend seiner Zugehörigkeit zu einem segmentierten, hervorzuhebenden Objekt zusätzlich zu seinem 12 Bit umfassenden
Helligkeits- bzw. Grauwert eine Farbe auf einer 4 Bit umfassenden Farbskala
zugewiesen (mit der insgesamt 16 Farben dargestellt werden können); damit ergeben sich 16 Bit für jedes Voxel in der kombinierten Farb- und Helligkeitsskala. Der
Anwender kann die Zuordnung der Farben zu den segmentierten Objektbereichen
auswählen („anwenderbasierende Parameterkonfiguration“). Entsprechend dieser
Zuordnung erfolgt (über eine Transferfunktion) die Zuweisung der Farben zu den
einzelnen Voxeln; die Helligkeits- bzw. Grauwerte können dabei erhalten bleiben.
Der Anwender hat die Möglichkeit, zwischen der farbcodierten Darstellung (kombi-

                                      - 10 -



nierte Farb- und Helligkeitsskala) und der ursprünglichen Grauwertdarstellung hinund herzuschalten.


Gemäß Schritt S2* des Patentanspruchs 1 nach Hilfsantrag III wird der Initialpunkt
für die Segmentierung nicht durch den Anwender, sondern automatisch bestimmt.
Für diese automatische Bestimmung werden nicht oder nicht nur die von einer ersten Bildgebungsmodalität stammenden, darzustellenden Bilddaten (Schritt S1*)
herangezogen, sondern Bilder weiterer Bildgebungsmodalitäten (z. B. Magnetresonanztomografie MRT, Positronenemissionstomografie PET, Ultraschall US, vgl.
S. 13 Z. 8 der Anmeldeunterlagen), in welchen der zentrale Bereich des zu markierenden Objekts bestmöglichen Kontrast zeigt.


Als Fachmann sieht der Senat hier einen Ingenieur der Fachrichtung Informatik mit
Hochschulabschluss und mehrjähriger Erfahrung in der Entwicklung von Bilddaten
verarbeitenden und darstellenden Systemen für die Medizintechnik an. Ein solcher
Fachmann ist mit den für medizinische Anwendungen geeigneten Segmentierungsalgorithmen und ebenso mit den in der medizinischen Bilddarstellung verwendeten Verfahren und deren Realisierung vertraut und kennt verschiedene
medizinische Bildgebungsmodalitäten und deren Eigenschaften. Er ist somit auch
in der Lage, die in der Anmeldung relativ allgemein beschriebene Lehre im Einzelnen auszuführen.


2.   Als im Stand der Technik besonders relevant sieht der Senat die Druckschriften D1 und D3 an. Diese zeigen Folgendes:


Die Druckschrift D1 betrifft ein interaktives, computergestütztes Diagnoseverfahren
und -system zur Unterstützung der Diagnose von Lungenknoten aus digitalen
medizinischen 3D-Bildern. Fig. 2 zeigt den Verfahrensablauf: Nach dem Laden der
medizinischen Volumendaten und der auswählbaren Darstellung axialer Schnittbilder werden gemäß Abs. [0036] potentielle Kandidaten für Knoten automatisch
oder manuell durch den Anwender ausgewählt (Schritt 115); zur manuellen Aus-

                                        - 11 -



wahl vgl. Abs. [0040] und [0051]. Danach wird automatisch eine relativ einfache
Segmentierung (über eine adaptive Schwelle unter Verwendung des lokalen Histogramms, vgl. Abs. [0038]) und eine Vermessung des segmentierten Objekts durchgeführt (Schritt 121), die Struktur wird automatisch klassifiziert (Schritte 123, 125)
und dreidimensional dargestellt, etwa farbig mit kontrastfarbigen Umgebungsstrukturen (Schritt 126), vgl. Abs. [0044]; die Darstellung kann der Anwender interaktiv
beeinflussen, z. B. drehen, vgl. Abs. [0045] und [0058]. Fig. 5 und 6 mit Beschreibung zeigen die Darstellung der Bilddaten in unterschiedlichen Displayfenstern,
z. B. im „axial image window“ 515, in der „maximum intensity projecion MIP“ 560,
im „spinning/flicker window“ 565 (in diesem Fenster kann das Bild auch vom
Anwender über den „spinning slider“ 580 gedreht werden) und in einem „pop-up
window“ 600 mit „three-dimensional rendering window“ 610 für die Darstellung der
dreidimensionalen Segmentierung, vgl. insbesondere Abs. [0034] und [0035].
Fig. 4 zeigt Möglichkeiten für den Anwender, interaktiv auf die Bilddarstellung Einfluss zu nehmen, z. B. zur Auswahl eines Schnittbilds, eines „Flicker“-Modus, oder
um ein (segmentiertes) 3D-Bild von verschiedenen Seiten zu betrachten, vgl.
Abs. [0075] bis [0079]. Im „Flicker“-Modus wird zwischen zwei unterschiedlichen
Parametersätzen für die Darstellung hin- und hergeschaltet, vgl. Abs. [0043].


Die von der Anmelderin selbst genannte Druckschrift D3 betrifft die Segmentierung
medizinischer Bilddaten. Die Segmentierung dient als Hilfsmittel zur Operationsplanung und soll möglichst genau sein, vgl. S. 24 linke Spalte letzter Satz bis
rechte Spalte Satz 1 („millimetergenaue Planung“) sowie die anschließende Beschreibung bis S. 25 links oben erster vollständiger Absatz („... sind die erforderliche Zeit und die erreichbare Genauigkeit entscheidend.“). Es sind sowohl einfache Schwellenwertverfahren (vgl. S. 25 Kap. „Einfache Ansätze“) als auch fortgeschrittene Verfahren (vgl. S. 25 rechts unten bis S. 27 links oben) erläutert, etwa
über Kanten, Grauwertunterschiede und Texturen, zu letzteren siehe das Kapitel
„Texturbasierte Tumorsegmentierung“ auf den Seiten 27 und 28. Der Anwender
wählt zunächst einen Startpunkt oder eine Startregion aus; im Anschluss wird eine
Segmentierung in einer oder mehreren Phasen durchgeführt, vgl. S. 26 rechte

                                        - 12 -



Spalte letzter Absatz. Hierbei kommt ein Merkmalsvektor (Kombination von mehreren Texturmaßen) zum Einsatz, vgl. S. 27 mittl. Spalte le. Abs. bis S. 28 li. Spalte
Abs. 1. In dem vorgestellten System können Bilder aus CT- und MRT-Verfahren
kombiniert werden, vgl. S. 28 unten mittlere und rechte Spalte. Bild 5 und 6 zeigen
zueinander senkrechte Schnitte eines menschlichen Gehirns in unterschiedlichen
Displayfenstern beim Segmentieren (Bild 6 links), als Segmentierungsergebnis
(Bild 5 rechts) sowie für die Operationsplanung nach der Segmentierung (Bild 6
rechts).


3.   Die Gegenstände des geltenden Anspruchs 1 und der nebengeordneten Ansprüche 17 und 18 nach Hauptantrag und ebenso die Gegenstände des jeweiligen
Anspruchs 1 nach den Hilfsanträgen I, II und III und der nebengeordneten Ansprüche 16 und 17 nach Hilfsantrag I, 17 und 18 nach Hilfsantrag II sowie 14 und 15
nach Hilfsantrag III beruhen nicht auf erfinderischer Tätigkeit.


a)   Wie oben erläutert, war dem Fachmann vor dem Anmeldetag der vorliegenden Patentanmeldung aus der Druckschrift D3 ein Verfahren zur automatischen
Objektmarkierung in der medizinischen Bildgebung bekannt mit einer Auswahl
eines Initialpunktes durch den Anmelder (selbstverständlich mit Übergabe der
Position an den Rechner) - Schritt S2. Auf die Umgebung des Initialpunktes werden Techniken der Mustererkennung angewendet mit dem Ergebnis einer Segmentierung des Objekts (Zweitmarkierung), die gemäß S. 24 linke Spalte letzter
Satz bis S. 25 links oben erster vollständiger Absatz möglichst detailgenau und
damit hochaufgelöst durchzuführen ist; hierfür kommen unterschiedliche Mustererkennungstechniken, auch als Abfolge oder in Kombination zum Einsatz, vgl. die in
S. 26 rechte Spalte letzter Absatz angesprochene Segmentierung in mehreren
Phasen, die verschiedenen in D3 erwähnten Mustererkennungstechniken (S. 24
Bild 2 „Keimzellwachstumsverfahren“ sowie S. 25 rechte Spalte letzter Absatz)
sowie den auf S. 27 mittlere Spalte letzter Absatz bis Seite 28 linke Spalte
Absatz 1 angesprochenen Merkmalsvektor - Schritte S3, S3*.

                                      - 13 -



Gemäß D3 Bild 5 und 6 können Bilddaten während und nach der Segmentierung
in unterschiedlichen Querschnittsansichten in verschiedenen Displayfenstern dargestellt werden. Um die Bilddarstellung (auch bereits zur Auswahl des Initialpunktes) für den Anwender möglichst flexibel zu gestalten, lag es für den Fachmann
nahe, zusätzlich oder alternativ weitere Darstellungsarten in Displayfenstern vorzusehen, wie sie beispielsweise aus D1 bekannt waren, etwa ein vom Anwender
drehbares Bild, vgl. in D1 Fig. 5 das „spinning/flicker window 565“ mit dem „spinning slider 580“, sowie eine Projektionsdarstellung, vgl. in D1 Fig. 5 das „maximum
intensity projection window 560“. Um dem Anwender eine gute Orientierung zu
ermöglichen, bot es sich an, unterschiedliche Darstellungen desselben Objektbereichs zu koppeln, etwa gemeinsam drehbar zu gestalten - Schritt S1.
Zudem war es in der medizinischen Bildverarbeitung üblich, ein gefundenes, segmentiertes bzw. markiertes Objekt (relativ zu seiner Umgebung) in der Bildschirmdarstellung hervorzuheben, etwa durch Farbe, vgl. beispielsweise D1 Abs. [0044]
- Schritt S5. Zu diesem Zweck wird üblicherweise den segmentierten Grauwertdaten eine zusätzliche Farbcodierung (etwa über zusätzliche Farbbits) hinzugefügt,
wobei der Anwender die Farbe auswählen und auch ändern kann, d. h. die Codierung ist reversibel - Schritt S4. Eine reversible Codierung drängte sich auch deshalb auf, um es dem Anwender zu ermöglichen, eine vorläufige, als unzureichend
verworfene Markierung bzw. Segmentierung wieder aufzuheben und einen neuen
Segmentierungsversuch zu starten, oder um einen Vergleich mit einer andersartigen Codierung zu erlauben, vgl. den in D1 Abs. [0043] angesprochenen „Flicker“-
Modus.


Durch diese Überlegungen konnte der Fachmann zum Gegenstand des geltenden
Anspruchs 1 nach Hauptantrag gelangen, wozu keine erfinderische Tätigkeit erforderlich war.


Entsprechendes gilt für die nebengeordneten Ansprüche 17 und 18 nach Hauptantrag.

                                       - 14 -



b)    Wie oben erwähnt, setzte der Fachmann beim durch D3 in Verbindung mit
D1 nahegelegten Verfahren ihm bekannte Farbdarstellungen ohne Weiteres zur
Hervorhebung eines segmentierten Bereichs ein. Im einfachsten Fall wird lediglich
das segmentierte Objekt farbig dargestellt; es können auch Objekt und nicht segmentierter Hintergrundbereich in kontrastierenden Farben dargestellt werden, vgl.
D1 Abs. [0044]. Wie dem Fachmann bewusst war, sind in der ersteren Darstellungsart nur das segmentierte Objekt, in der letzteren Darstellungsart sowohl der
segmentierte Objektbereich als auch der kontrastfarbene, nicht segmentierte Hintergrundbereich (der in bestimmten Fällen ebenfalls für den Anwender interessant
sein kann) für eine Betrachtung hervorgehoben. Hiervon ausgehend lag es für den
Fachmann nahe, dem Anwender zusätzlich die Möglichkeit anzubieten, bei Bedarf
lediglich die Hintergrundbereiche farblich hervorzuheben, etwa im Rahmen einer
invertierten Farbdarstellung (Negativ). Zur Durchführung einer solchen Operation
mussten dann die Hintergrundbereiche (einschließlich eingeschlossener Voxelbereiche) farbig markiert und die entsprechende vorherige Farbmarkierung des segmentierten Objektbereichs aufgehoben werden. Durch eine solche Invertierung
werden auch eingeschlossene Hintergrundvoxelbereiche markiert, d. h. Merkmal a) ist erfüllt, vgl. das oben unter II.1. zur Interpretation dieses Merkmals Ausgeführte.


Durch diese zusätzlichen Überlegungen, die sich vollständig im fachüblichen Rahmen bewegen, gelangte der Fachmann zum Gegenstand des geltenden Anspruchs 1 nach Hilfsantrag I, wozu ebenfalls keine erfinderische Tätigkeit erforderlich war.


Entsprechendes gilt für die nebengeordneten Ansprüche 16 und 17 nach Hilfsantrag I.


c)    Des Weiteren liegen in einem mit Hilfe einer Bildgebungsmodalität erzeugten
Bilddatensatz, wie er in D3 verwendet wird, die Bilddaten üblicherweise als Grauwerte mit einer bestimmten Grauwerttiefe (Anzahl von Grauwertbits) vor; im Fall

                                        - 15 -



von Magnetresonanzbilddaten können dies beispielsweise 12 Bit-Daten auf einer
Hounsfield-Skala sein. Dies war dem hier anzunehmenden Fachmann geläufig.
Wie oben bereits unter II.3.a) erwähnt, war dem Fachmann zudem aus seinem
Fachwissen als übliche Art der Realisierung einer Farbcodierung darzustellender
Bildbereiche die Verwendung von zusätzlichen Farbbits bekannt, wobei einzelnen
segmentierten Bereichen einzelne Farben zugeordnet werden. Die Anzahl der für
die Farbe zusätzlich bereitzustellenden Bits wählte der Fachmann je nach seinen
Vorgaben (voraussichtliche Anzahl mit unterschiedlichen Farben darzustellender
Bildbereiche, etwa für unterschiedliche Gewebearten) geeignet aus, beispielsweise 4 zusätzliche Farbbits, die eine Darstellung von maximal 16 unterschiedlichen Farben erlauben. Über eine entsprechende Transferfunktion wird demgemäß
jedem Voxel zusätzlich zu seinem Grau- bzw. Helligkeitswert auf der 12 Bit-Helligkeitsskala ein Farbwert auf einer 4 Bit-Farbskala entsprechend seiner Zugehörigkeit zu einem segmentierten Bereich zugewiesen, also insgesamt 16 Bit auf einer
kombinierten Farb- und Helligkeitsskala, wobei die Grau- bzw. Helligkeitswerte
erhalten bleiben. Im Interesse einer für den Anwender möglichst flexibel an seine
Bedürfnisse anpassbaren Darstellung bot es sich für den Fachmann an, die Zuordnung der einzelnen Farben zu den einzelnen Bildbereichen (Parameterkonfiguration der Transferfunktion) vom Anwender auswählbar (anwenderbasierend) zu
gestalten. Im Rahmen der flexiblen Farbauswahl bot es sich ebenfalls an, dem
Anwender einen Vergleich einer von ihm ausgewählten Farbdarstellung mit der ursprünglichen Grauwertdarstellung zu ermöglichen, etwa durch Hin- und Herschalten zwischen der Farb- und Helligkeitsskala und den ursprünglichen Grauwerten;
vgl. den in D1 erwähnten „Flicker“-Modus. Damit ergaben sich die Schritte S4* und
S5*.


Durch diese weiteren Überlegungen, die sich vollständig im Rahmen des in der
medizinischen Bilddarstellung Üblichen bewegen, gelangte der Fachmann zum
Gegenstand des geltenden Anspruchs 1 nach Hilfsantrag II, wozu ebenfalls keine
erfinderische Tätigkeit erforderlich war.

                                         - 16 -



Entsprechendes gilt für die nebengeordneten Ansprüche 17 und 18 nach Hilfsantrag II.


Nach Ansicht der Anmelderin ermöglicht die anmeldungsgemäße Aufblähung des
Datenvolumens von 12 auf 16 Bit eine Spreizung sowohl der Farben als auch der
Grauwerte innerhalb eines segmentierten Bereichs; dies ermögliche dem Anwender eine bessere Unterscheidung im medizinischen Bild und sei für den Fachmann
nicht nahegelegt.


Dem ist entgegenzuhalten, dass aus den Anmeldeunterlagen eine Spreizung der
Grauwerte und der Farben innerhalb eines segmentierten Bereichs nicht hervorgeht; Fig. 2 und die zugehörige Beschreibung gehen im Gegenteil nicht über eine
Farbzuordnung durch Verschiebung der Daten auf eine kombinierte Farb- und Helligkeitsskala hinaus, wobei jedem segmentierten Bildbereich genau eine Farbe
zugeordnet wird und die Helligkeitswerte beibehalten werden. Durch eine solche
Vorgehensweise, die wie oben ausgeführt in der medizinischen Bilddarstellung
üblich war, sind die Schritte S4* und S5* erfüllt, vgl. auch das oben unter II. 1. hierzu Ausgeführte.


d)    Wie oben unter II.3.a) erläutert, werden beim Verfahren gemäß D3 eine
Abfolge oder Kombinationen von Techniken der Mustererkennung eingesetzt -
Schritt S3*. In einem solchen Verfahren können zudem Daten unterschiedlicher
Bildgebungsmodalitäten kombiniert werden, die jeweils unterschiedliche medizinische Details unterschiedlich gut zeigen, vgl. D3 S. 28 unten mittlere und rechte
Spalte. Je nach der im Segmentierungsverfahren zu lösenden Teilaufgabe verwendete der Fachmann Bilddaten aus hierfür besonders gut geeigneten Bildgebungsmodalitäten.
Im Verfahren gemäß D3 wird der Initialpunkt von Anwender gewählt. Dem Fachmann war jedoch die Möglichkeit bekannt, die Auswahl eines Initialpunkts in einem
Segmentierungsverfahren nicht nur durch den Anwender, sondern alternativ automatisch durch den Rechner vorzunehmen, vgl. etwa D1 Abs. [0036]. Um dem

                                         - 17 -



Anwender im Verfahren gemäß D3 Zeit und Aufwand zu ersparen, bot es ich an,
dort eine solche automatische Auswahl zumindest alternativ vorzusehen. Für die
zu lösende Teilaufgabe „automatisches Finden eines geeigneten Initialpunkts“ verwendete der Fachmann dann Daten aus hierfür geeigneten Bildgebungsmodalitäten, nicht (nur) aus einer ersten, für die Farb- und Grauwertdarstellung verwendeten Bildgebungsmodalität (Schritt S1*), sondern vorzugsweise Daten solcher weiterer Bildgebungsmodalitäten, die entsprechend der Art des zu segmentierenden
(markierenden) Objekts dessen zentralen Bereich, von dem die Segmentierung
ausgehen soll und in dem infolgedessen der Initialpunkt zu wählen ist, besonders
gut zeigen - Schritt S2*.


Diese zusätzlichen Überlegungen, die innerhalb des fachüblichen Rahmens lagen,
konnten den Fachmann zum Verfahren gemäß dem Anspruch 1 des Hilfsantrags III führen; hierzu war keine erfinderische Tätigkeit erforderlich.


Entsprechendes gilt für die nebengeordneten Ansprüche 14 und 15 nach Hilfsantrag III.


Somit waren für den Fachmann aus dem Stand der Technik in Verbindung mit seinem Fachwissen die Gegenstände des jeweiligen Anspruchs 1 und der jeweiligen
nebengeordneten Ansprüche gemäß Hauptantrag und gemäß der Hilfsanträge I, II
und III nahegelegt. Ein über die zu erwartenden Wirkungen der einzelnen Maßnahmen hinausgehender, synergistischer Effekt ist nicht erkennbar.
Keiner dieser Ansprüche ist somit gewährbar.

                                       - 18 -



4.   Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
jeweiligen abhängigen Patentansprüche (2 bis 16 nach Hauptantrag, 2 bis 15 nach
Hilfsantrag I, 2 bis 16 nach Hilfsantrag II, 2 bis 13 nach Hilfsantrag III) nicht gewährbar (BGH in GRUR 1997, 120 „Elektrisches Speicherheizgerät“).




Dr. Fritsch              Eder               Baumgardt               Dr. Thum-Rung




                                                                                  Fa
