---
ecli: "ECLI:DE:BPatG:2012:061112B17Wpat20.09.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 20/09"
decided: "2012-11-06"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2012&Sort=1&Seite=80&nr=24261&anz=1451&pos=1212&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2012-11-06_17_W-pat_20_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 20/09 vom 2012-11-06

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 20/09                                                       Verkündet am
_______________                                                      6. November 2012
    (Aktenzeichen)                                                           …




                              BESCHLUSS

                             In der Beschwerdesache


             betreffend die Patentanmeldung 10 2005 023 964.1-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 6. November 2012 unter Mitwirkung des Richters
Dipl.-Ing. Baumgardt   als    Vorsitzendem,   der     Richterinnen     Eder   und
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
08.05

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                         I.


Die vorliegende Patentanmeldung ist am 20. Mai 2005 beim Deutschen Patentund Markenamt in englischer Sprache unter Inanspruchnahme der Prioritäten
zweier US-amerikanischer Patentanmeldungen (die früheste vom 25. Mai 2004)
eingereicht worden. Die Bezeichnung lautet in der deutschen Übersetzung


               „Volumenvisualisierung mittels Texturverschiebung“.


Die Prüfungsstelle für Klasse G06T hat die Anmeldung zurückgewiesen, da der
jeweilige Gegenstand des nachgesuchten Patents nach dem damals geltenden
Hauptantrag und Hilfsantrag nicht auf erfinderischer Tätigkeit beruhe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        Patentansprüche 1 bis 9 vom 29. Oktober 2012,
        noch anzupassende Beschreibung
        und Zeichnungen mit 4 Figuren, jeweils wie Offenlegungsschrift.

                                        -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist folgende
Druckschrift genannt worden:


         D1: C. Rezk-Salama, K. Engel, M. Bauer, G. Greiner, T. Ertl: „Interactive
              Volume Rendering on Standard PC Graphics Hardware Using Multi-Textures and Multi-Stage Rasterization“, ACM-Press, 2000; Proceedings of the ACM SIGGRAPH/EUROGRAPHICS workshop on
              Graphics hardware, 2000, pages 109-118, ISBN 1-58113-257-3.


Der Senat hat mit Ladungszusatz zusätzlich die Frage aufgeworfen, ob das beanspruchte Verfahren gemäß § 1 Abs. 3 und 4 PatG vom Patentschutz ausgeschlossen ist, und ob bei der Prüfung auf erfinderische Tätigkeit möglicherweise nicht
alle Anspruchsmerkmale zu berücksichtigen sind.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                         II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da das Verfahren des Patentanspruchs 1 nicht
auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.      Die Patentanmeldung betrifft Volumenvisualisierung mittels Texturverschiebung.


Gemäß der Beschreibungseinleitung in Abs. [0002] bis [0008] der Offenlegungsschrift ist bei der Volumenvisualisierung das unterschiedliche Verfahren gemeinsame Prinzip die Integration von Daten entlang von Sichtstrahlen innerhalb eines
Volumens für jedes Pixel einer dreidimensionalen Darstellung. Bei medizinischen
oder seismischen Daten fielen sehr große Datenmengen an.

                                     -4-



Die direkte Volumenvisualisierung könne einen wahlfreien Zugriff auf die Datenwerte des dreidimensionalen Arrays erfordern und deshalb werde das gesamte
Array im RAM oder im Speicher der grafischen Verarbeitungseinheit (GPU)
gespeichert. Solch eine enorme Datenmenge sei oft größer als die auf modernen
Computern verfügbare Speicherkapazität von Direktzugriffsspeichern (RAM). Um
direkte Volumenvisualisierungen von sehr großen Volumina zu berechnen, werde
eine kostenintensive Vorrichtung mit sehr großen RAM-Mengen verwendet.
Bei der Verwendung einer 32-Bit CPU sei die Größe des Arrays, das für die
direkte Volumenvisualisierung verwendet werde, auf die durch die CPU adressierbare maximale Anzahl von Datenelementen begrenzt. Einige dreidimensionale
Arrays könnten so groß sein, dass ihre Größe die Speicheradressiereigenschaft
von 32-Bit CPUs überschreite, die man in vielen PCs und Grafikarbeitsstationen
finde.
Volumenvisualisierungsverfahren   könnten    auch    das    erneute   Abtasten
(Resampling) der Volumendaten in ein gleichmäßiges kartesisches Raster erfordern. Die Bilder wiesen alle die gleiche Auflösung und Abmessungen auf und der
Abstand zwischen angrenzenden Bildern sei für den kompletten Satz von Volumendaten konstant.
Die Daten für das Volumen könnten in einer einzigen 3D-Textur gespeichert werden und die drei Texturkoordinaten von den Eckpunkten der Schnitte würden über
das Innere der Schnittpolygone interpoliert. Die drei Texturkoordinaten würden
während der Rasterung zum Abrufen von gefilterten Pixels aus der 3D-Texturabbildung verwendet. Je nach Größe der 3D-Textur sei die Cache-Leistung der CPU
oder GPU ausreichend. Es sei ebenfalls möglich, das Volumen in mehrere kleinere 3D-Texturen (Bausteine; bricks) zu zerlegen, um die Cache-Leistung zu
erhöhen. Um jedoch eine zusammenhängende Interpolation zwischen den Bausteinen zu gewährleisten, müssten die Volumendaten auf den Bausteingrenzen
repliziert werden.
Da die Cache-Speicher in CPUs und GPUs relativ klein seien, würden die Volumendaten in eine große Anzahl von Bausteinen zerlegt, um eine optimale Cache-Leistung zu gewährleisten. Viele Volumendaten würden auf den Bausteingrenzen

                                       -5-



repliziert, was bei großen Volumendaten keine praktische Lösung darstelle.
Zusätzlich müssten die Daten im Speicher von der ursprünglichen Darstellung als
ein Stapel von Schnitten neu angeordnet werden.
Ein alternativer Ansatz sei es, Volumendaten als eine Anzahl von zweidimensionalen Bildern (2D-Texturen) zu speichern. Ein einzelnes Bild der Volumendaten
sei verglichen mit dem gesamten Volumen eher klein. Die Visualisierung von
jeweils einer einzelnen zweidimensionalen Textur ergebe eine gute Cache-Leistung. Dieser Ansatz erfordere jedoch, dass drei Kopien der Volumendaten im
Speicher abgelegt würden, wobei jede Kopie in einer der drei Hauptachsen der
Volumendaten orientiert sei. Die Kopie der Volumendaten mit einer Hauptachse,
die am stärksten senkrecht zur Sichtlinie des Betrachters liege, werde zur Visualisierung verwendet, um gute Speicherzugriffsmuster und eine Cache-Kohärenz zu
gewährleisten.


Der geltende Patentanspruch 1 betrifft (mit eingefügten Gliederungszeichen) ein


        a) Verfahren zur direkten Visualisierung medizinischer oder tomografischer Bilddaten aus zweidimensionalen Texturen mit einem System (10), das eine Datenquelle (12), einen Speicher (14), einen Prozessor (16) und eine Anzeige (18) umfasst,

        b) bei dem die Datenquelle (12) zweidimensionale Bilder (50) und zugehörige räumliche Beziehungsdaten zur Verfügung stellt, die einen ein
            Volumen darstellenden Datensatz von MRI- , CT- , Röntgen- , PET-
            oder Ultraschalldaten bilden,

        c) bei dem in den Speicher (14) oder Prozessor (16) sequentiell unterschiedliche Untermengen von aneinander angrenzenden Bildern (50)
            geladen werden,

                                      -6-



       d) bei dem der Prozessor (16) durch sequentielles Ausführen einer trilinearen Interpolation für unterschiedliche Untermengen der Volumendaten eine dreidimensionale Darstellung erzeugt,

       da) indem für jede Untermenge von Bildern (50) der Raum zwischen den
           aktuellen angrenzenden Bildern (50) gerastert wird, wobei

       db) beim objektausgerichteten Schneiden und bei einer Hauptblickrichtung
           entlang der z-Achse die Bilder (50) verwendet werden, um den Raum
           zu rastern und wobei

       dc) für die Wiedergabe entlang der x- oder y- Achse basierend auf der
           Umgebungsgeometrie, die aus dem objektausgerichteten oder bildausgerichteten Schnitt bekannt ist, Polygone (56) oder Bereiche festgelegt werden, die sich als Streifen zwischen angrenzenden zweidimensionalen Texturen erstrecken und Texturdaten aus Daten der
           zweidimensionalen Texturen, die das Polygon (56) schneidet, erzeugt
           werden,

       e) und bei dem die Anzeige (18) ein durch trilineare Interpolation unter
           Verwendung der Texturdaten für die Polygone (56) erzeugtes Bild darstellt.


Das beanspruchte Visualisierungsverfahren wird auf einem Datenverarbeitungssystem mit Datenquelle, Speicher, Prozessor und Anzeige durchgeführt, wobei die
Datenquelle einen Volumendatensatz (z. B. einen CT-Datensatz) liefert in Form
einer Mehrzahl von zweidimensionalen Bildern (einschließlich Informationen bzgl.
deren Anordnung im Raum), etwa als parallel zueinander und zur (x,y)-Ebene
angeordnete, objektausgerichtete Schnitte bzw. Texturen 50, vgl. Fig. 3 (Merkmale a), b)). Sequentiell werden Untermengen der Volumendaten in Form von
jeweils benachbarten Bildern (Texturen) 50 ausgewählt und in den Speicher geladen (Merkmal c)).

                                          -7-



Um eine Visualisierung der Volumendaten in einer Blickrichtung parallel zu den
Texturen (etwa entlang der x- oder y-Achse) zu erzeugen, werden in der Schicht
zwischen den beiden Texturen 50 Polygonstreifen 56 festgelegt, die sich etwa
senkrecht zur Blickrichtung (parallel zur z-Achse) erstrecken (Fig. 4). Auf den Polygonstreifen werden Texturwerte interpoliert, und zwar aus den Werten auf den
Schnittlinien der Polygone 56 mit den Texturen 50; dadurch wird der Raum zwischen den benachbarten Texturen gerastert (Merkmal da) in Verbindung mit dc)).
Hierbei wird für die jeweilige Schnittlinie innerhalb der Textur 50 interpoliert und
zusätzlich auf den Polygonen zwischen den beiden Schnittlinien, also insgesamt
trilinear, vgl. Offenlegungsschrift Abs. [0029] drittletzter und vorletzter Satz. Die trilinear interpolierten Daten auf den Polygonen liefern Beiträge zur Bildwiedergabe;
die sich aus der sequentiellen Verarbeitung jeweils benachbarter Texturen ergebenden Beiträge für die Bildwiedergabe werden kombiniert und dargestellt (Merkmale d), e)).
Für eine Blickrichtung entlang der z-Achse (senkrecht zu den vorgegebenen Texturen 50) wird dagegen, ebenfalls in sequentieller Verarbeitung, die Rasterung aus
den jeweiligen benachbarten Bildern bzw. Texturen 50 unter Verwendung von trilinear    interpolierten   Zwischenschnitten     erzeugt,    vgl.   Offenlegungsschrift
Abs. [0038] (Merkmale d) und da) in Verbindung mit db)).


Als Fachmann sieht der Senat hier einen Hochschul-Ingenieur der Fachrichtung
Informatik mit Erfahrung in der Verarbeitung und Darstellung von dreidimensionalen Bilddaten an.


2.       Das Verfahren des Patentanspruchs 1 beruht nicht auf erfinderischer Tätigkeit. Es war dem Fachmann nämlich durch die Druckschrift D1 nahegelegt. Dies
gilt selbst dann, wenn der Prüfung der gesamte Patentanspruch mit allen seinen
Merkmalen zugrunde gelegt wird. Damit kann dahingestellt bleiben, ob das beanspruchte Verfahren gemäß § 1 Abs. 3 und 4 PatG vom Patentschutz ausgeschlossen ist, und ob der Anspruch 1 Merkmale enthält, die nicht die Lösung eines technischen Problems mit technischen Mitteln bestimmen oder beeinflussen und somit

                                          -8-



bei der Prüfung der erfinderischen Tätigkeit nicht zu berücksichtigen sind (BGH in
GRUR 2011, 125-128 - „Wiedergabe topografischer Informationen“).


Die Druckschrift D1 betrifft interaktive Volumendarstellung auf der Grafik-Hardware
eines Standard-PC. In S. 111 Kap. „Texture Based Volume Rendering“ ist im
ersten Satz die übliche Aufteilung eines Volumendatensatzes in benachbarte Bildebenen bzw. Schnitte („slices“) beschrieben. Fig. 4 zeigt zwei bekannte Möglichkeiten der Orientierung der Schnitte, nämlich angepasst an die Kameraposition
bzw. Blickrichtung („viewport-aligned“, Fig. 4 links, wird für spezielle, auf trilineare
Texturinterpolation zugeschnittene Hardware verwendet) oder objektangepasst
(Fig. 4 rechts, wird für Hardware verwendet, die nur 2D-Texturen unterstützt); letzteres erlaubt die Ersetzung der trilinearen durch bilineare Interpolation. Gemäß
S. 111 re. Sp. Abs. 2 ist es (bisher) im Fall objektangepasster Orientierung der
Schnitte nötig, drei Kopien des Datensatzes bereitzustellen (dies entspricht dem in
der Offenlegungsschrift der vorliegenden Anmeldung Abs. [0008] dargestellten
Stand der Technik). Durch die fehlende räumliche Interpolation ergeben sich hier
starke visuelle Artefakte, vgl. auch die Zusammenfassung sowie S. 109 li. Sp. letzter Absatz. Diese können durch die Berechnung von Zwischenschnitten („intermediate slices“) vermindert werden, wobei von einer Schnittfläche zum nächsten trilinear interpoliert wird, vgl. S. 111 re. Sp. Kap. 5 Abs. 1, insbesondere Gl. (1).
Kap. 9 auf S. 114 und 115 i. V. m. Fig. 11 mit Beschreibung zeigt, wie ein Schnitt in
beliebiger Richtung (senkrecht zur jeweiligen Betrachtungsrichtung) durch den 3D-Datensatz interpoliert werden kann. Ein Schnittpolygon der darzustellenden
Schnittebene mit der Hülle („bounding box“) des Volumens wird berechnet (Fig. 11
links). Die Hülle und mit ihr das Schnittpolygon wird durch die vorgegebenen
Schnitte (Bildebenen) des Volumendatensatzes in Streifen geschnitten (Fig. 11, 2.
von links). Für jeden der Polygonstreifen wird Bildinformation aus den zwei
benachbarten Texturbildern interpoliert. Fig. 11 zeigt im dritten Bild von links die
zur Interpolation verwendeten Gewichtsfaktoren, im rechten Bild das aus den interpolierten Streifen zusammengesetzte Bild auf dem Schnittpolygon. Zur Realisierung der Interpolation mittels Hardware werden Daten aus den beiden benachbar-

                                        -9-



ten Texturbildern („slice i“ und „slice (i+1)“) in Register geladen und zwischen diesen mit Hilfe eines ebenfalls geladenen Faktors                          12. Gemäß
S. 115 li. Sp. le. Abs. bis re. Sp. Abs. 1 kann dieses Verfahren nicht nur zur Interpolation einzelner Schnittbilder, sondern auch zur Volumendarstellung mit kamerapositions- bzw. blickrichtungs-orientierten („viewport-aligned“) Schnitten verwendet
werden. Dieses Verfahren sei jedoch sehr rechenintensiv und habe daher eine
schlechte Effizienz („the significant computational overhead for intersection calculation in combination with the large number of texture binding operations results in
a poor rendering performance“).


Im Gegensatz zur Ansicht der Anmelderin lag es trotz der in D1 beschriebenen
Nachteile für den in der Datenverarbeitung bewanderten Fachmann, dem die
raschen Fortschritte der Datenverarbeitungstechnik im Hinblick auf Speicher- und
Prozessorleistung bekannt waren und der ein Verfahren zur Volumendarstellung
(weiter-) entwickeln wollte, durchaus nahe, mehrere Jahre nach der Veröffentlichung der Druckschrift D1 (D1 wurde im Jahre 2000 veröffentlicht, Prioritätsjahr
der vorliegenden Patentanmeldung ist 2004) auf diese zurückzugreifen und ein
solches Verfahren mit Blick auf die inzwischen verfügbare Hardware zu implementieren. Beim aus D1 Kap. 9, insbesondere Fig. 11 mit Beschreibung bekannten
Visualisierungsverfahren, das auf einem üblichen PC (mit Speicher für Volumendaten und Anzeige) mit Standard-Graphikprozessor (siehe Titel) durchgeführt wird,
sind Volumendaten in Form mehrerer zweidimensionaler Bilder (einschließlich
Informationen bzgl. deren Anordnung im Raum) vorhanden, wobei der Fachmann
aus den auf S. 109 li. Sp. le. Satz angesprochenen medizinischen Anwendungen
die Möglichkeit der Verwendung von MRI- , CT- , Röntgen- , PET- oder Ultraschalldaten mitliest - Merkmale a), b). Zur Interpolation einer in beliebiger Richtung
orientierten Schnittebene (die jeweils senkrecht zur Blickrichtung liegt, also beispielsweise in (y,z)- bzw. (x,z)- Orientierung für eine Wiedergabe entlang einer zu
den vorgegebenen objektorientierten Schnitten parallelen x- bzw. y-Richtung) wird
die gewünschte Schnittebene durch die vorgegebenen Bildebenen des Volumendatensatzes in Polygonstreifen geschnitten. Für eine Volumendarstellung mit meh-

                                       - 10 -



reren parallelen Schnittebenen im Sinne des „multi-planar reformatting MPR“ (D1
Kap. 9 Satz 1 i. V. m. S. 115 li. Sp. le. Satz) muss dieses Schneiden mehrfach
(einmal für jede Schnittebene) durchgeführt werden, wobei sich in jeder Scheibe
zwischen zwei benachbarten vorgegebenen Bildern mehrere, zu verschiedenen
parallelen Schnittebenen gehörende, zu texturierende Polygonstreifen ergeben.
Fig. 12 deutet auf die Texturierung einer Schnittebene durch sequentielles Laden
benachbarter Texturbilder mit Interpolation jeweils zwischen diesen hin; dieses
sequentielle Vorgehen bot sich dem Fachmann auch für die Erzeugung einer Volumendarstellung an, insbesondere unter dem Aspekt sehr großer Datenmengen
und begrenzter Speicher- und Prozessorleistung - Merkmal c). Um ein aufwändiges wiederholtes Laden der Texturbilder zu vermeiden (wie es bei einer Verarbeitung jeder der parallelen Schnittebenen für sich nötig wäre), lag es für den Fachmann nahe, alle innerhalb einer Scheibe zwischen zwei benachbarten Bildern vorzunehmenden Operationen durchzuführen, während sich das zugehörige Texturbildpaar im Speicher des Prozessors befindet, d. h. jeweils alle Polygonstreifen der
Scheibe anhand der jeweiligen Umgebungsgeometrie festzulegen (beispielsweise
mittels Schneiden aller vorbestimmten Schnittebenen mit dem aktuellen Bildpaar)
und durch trilineare Interpolation zu texturieren - Merkmale d) und da) in Verbindung mit dc).
Aus D1 Fig. 11 erkannte der Fachmann, dass dieses Verfahren sich für solche
Blickrichtungen anbietet, die in etwa parallel zu den ursprünglich vorliegenden Bildern („object-aligned texture slices“) liegen, dies entspricht im geltenden Anspruch 1 den x- und y-Richtungen. Bei der Betrachtung in z-Richtung liegen dagegen die Texturbilder bereits in der gewünschten Orientierung senkrecht zur
Betrachtungsrichtung vor, daher ist eine Reformatierung nicht nötig. Hier kann der
Raum zwischen den Bildern direkt unter Verwendung der ursprünglichen Bilddaten
gerastert werden, wobei sich wie in D1 Kap. 5 Abs. 1 beschrieben zur Vermeidung
von Artefakten die Berechnung von Zwischenschnitten („intermediate slices“) zwischen je zwei Schnitten mit trilinearer Interpolation anbot, die gemäß Gl. (1)
sequentiell (vgl. die Indices i und i+1) durchzuführen ist - Merkmale c), d), da) in
Verbindung mit db).

                                        - 11 -



Aus den jeweils trilinear interpolierten Texturdaten wird schließlich ein Bild erzeugt
und auf der Anzeige dargestellt - Merkmal e).


Durch die geschilderten Überlegungen konnte der Fachmann zum Verfahren
gemäß dem Anspruch 1 gelangen, wozu keine erfinderische Tätigkeit erforderlich
war.


3.     Der Anspruch 1 ist nicht gewährbar.


Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
abhängigen Patentansprüche 2 bis 9 nicht gewährbar (BGH in GRUR 1997, 120
„Elektrisches Speicherheizgerät“).




Baumgardt                Eder                Dr. Thum-Rung                Dr. Forkel




                                                                                   Fa
