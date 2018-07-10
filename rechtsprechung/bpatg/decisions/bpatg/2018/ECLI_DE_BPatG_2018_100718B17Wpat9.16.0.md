---
ecli: "ECLI:DE:BPatG:2018:100718B17Wpat9.16.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 9/16"
decided: "2018-07-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=29&nr=32800&anz=825&pos=445&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2018-07-10_17_W-pat_9_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 9/16 vom 2018-07-10

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 9/16                                                     Verkündet am
_______________                                                       10. Juli 2018
    (Aktenzeichen)                                                         …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2005 044 653.1


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 10. Juli 2018 unter Mitwirkung des Vorsitzenden
Richters     Dipl.-Phys. Dr. Morawek,     der     Richterinnen        Eder    und
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel




ECLI:DE:BPatG:2018:100718B17Wpat9.16.0

                                        -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                       Gründe


                                         I.


Die vorliegende Patentanmeldung wurde am 19. September 2005 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


     „Verfahren und Vorrichtung zur Rekonstruktion eines dreidimensionalen
            Bildvolumens aus zweidimensionalen Projektionsbildern“.


Die Prüfungsstelle für Klasse G06T des Deutschen Patent- und Markenamts hat in
der Anhörung am 24. November 2015 die Anmeldung zurückgewiesen, da der
Patentanspruch 1 unter Berücksichtigung nur derjenigen Merkmale, die die Lösung eines technischen Problems mit technischen Mitteln bestimmen, nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen den Beschluss wendet sich die am 8. Januar 2016 eingegangene Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                       -3-



       - gemäß Hauptantrag mit
       Patentansprüchen 1 bis 9, überreicht in der mündlichen Verhandlung,
       Beschreibung Seiten 1 bis 10 und
       2 Blatt Zeichnungen mit Figuren 1 bis 4, jeweils vom Anmeldetag;


       - gemäß Hilfsantrag 1 mit
       Patentansprüchen 1 bis 8, überreicht in der mündlichen Verhandlung,
       noch anzupassender Beschreibung und Zeichnungen mit Figuren
       wie Hauptantrag;


       - gemäß Hilfsantrag 2 mit
       Patentansprüchen 1 bis 8, überreicht in der mündlichen Verhandlung,
       im Übrigen wie Hilfsantrag 1;


       - gemäß Hilfsantrag 3 mit
       Patentansprüchen 1 bis 7, überreicht in der mündlichen Verhandlung,
       im Übrigen wie Hilfsantrag 1.


Im Verfahren sind folgende Druckschriften genannt worden:


       D1: Wiesent, K. et al: Enhanced 3-D-Reconstruction Algorithm for C-Arm
       Systems Suitable for Interventional Procedures. IEEE Trans. on Medical
       Imaging, Vol. 19, No. 5, May 2000, Seiten 391 – 403

       D2: DE 100 30 633 A1

       D3: US 2004/0179643 A1.

                                       -4-



Vom Senat wurde zusätzlich die Druckschrift


        D4: US 6 477 221 B1


eingeführt.


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 gemäß
Hauptantrag lautet:


     „Verfahren zur Rekonstruktion eines dreidimensionalen Bildvolumens (12)

        a) aus zweidimensionalen Projektionsbildern (20) eines Objekts,
          die durch Rotation eines Aufnahmesystems (3, 4) um das Objekt (5) aus verschiedenen Projektionsrichtungen aufgenommen
          wurden,

        b) wobei zumindest ein Projektionsbild (20) derart modifiziert wird,
          dass es einem Projektionsbild (24) entspricht, welches mit einem virtuellen Detektor (22) aufgenommen wurde, dessen
          Spalten parallel zur Rotationsachse (18) des Aufnahmesystems
          ausgerichtet sind

        c) und bei welchem die Grauwerte der Voxel des Bildvolumens (12) durch Rückprojektion der Projektionsbilder (20) berechnet werden,

    dadurch gekennzeichnet,

        d) dass die z-Richtung des Koordinatensystems des Bildvolumens (12) parallel zur Rotationsachse (18) des Aufnahmesystems verläuft, und

        e) dass bei der Rückprojektion für jedes modifizierte Projektionsbild (24) die Voxel des Bildvolumens (12) in der x-, y- und z-

                                          -5-



             Richtung in drei Schleifen abgetastet werden und jeweils die
             Projektion des Voxels auf das Projektionsbild (24) berechnet
             und der entsprechende Grauwert des Projektionsbildes (24)
             zum Grauwert des Voxels akkumuliert wird, wobei

          f) die z-Richtung in der innersten Schleife abgetastet wird und dabei jeweils die vertikale Bildkoordinate (v) des Projektionsbildes
             durch Addition eines für die x- und y-Koordinaten dieser Schleife konstanten Inkrements (Δv) berechnet wird,

          g) und dass das modifizierte Projektionsbild (24) während der
             Rückprojektion in einem Datenspeicher gespeichert ist, der so
             eingerichtet ist, dass vertikal benachbarte Pixel aufeinander folgen.“


Demgegenüber ist im Patentanspruch 1 des Hilfsantrags 1 vor dem Merkmal d)
eingefügt:


          h) dass das modifizierte Projektionsbild (24) durch Anwendung einer projektiven Transformation (Homographie) aus dem ursprünglichen Projektionsbild (20) gewonnen wird,


Ausgehend vom Patentanspruch 1 des Hauptantrags ist im Patentanspruch 1 des
Hilfsantrags 2 nach dem Merkmal f) eingefügt:


          i) dass bei der Akkumulation des Grauwerts des Projektionsbildes (24) jeweils der nächstliegende Pixel des Projektionsbildes
             verwendet wird,


Der Patentanspruch 1 des Hilfsantrags 3 geht aus vom Patentanspruch 1 des
Hauptantrags und enthält zusätzlich sowohl das Merkmal h) als auch das Merkmal i).

                                        -6-



Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.




                                         II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da der Gegenstand des Patentanspruchs 1
nach Hauptantrag und der jeweilige Gegenstand des Patentanspruchs 1 nach
Hilfsantrag 1, 2 und 3 nicht auf erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.   Die Patentanmeldung betrifft ein Verfahren und eine Vorrichtung zur Rekonstruktion eines dreidimensionalen Bildvolumens aus zweidimensionalen Projektionsbildern, sowie ein digitales Speichermedium mit einem Programmcode zur
Durchführung des Verfahrens. Insbesondere ist die Erfindung auf ein Verfahren
bzw. eine Vorrichtung gerichtet, bei welchem die Projektionsbilder durch Rotation
eines Aufnahmesystems um ein Objekt aus verschiedenen Projektionsrichtungen
aufgenommen werden, wobei die Voxel des Bildvolumens durch Rückprojektion
der Projektionsbilder berechnet werden (Offenlegungsschrift Abs. [0001]).


In der Radiologie besteht oft das Bedürfnis, für die Diagnose, die Therapieplanung
und während interventioneller Eingriffe aus zweidimensionalen (2-D) Bildern ein
dreidimensionales (3-D) Bild zu rekonstruieren. Insbesondere bei C-Arm-Röntgensystemen, bei welchen Röntgenröhre und -detektor an einem frei um den Patienten verfahrbaren C-Arm befestigt sind, möchte man oft aus den so erhaltenen
zweidimensionalen Röntgenbildern bzw. Projektionsbildern ein dreidimensionales
Bildvolumen rekonstruieren. Probleme entstehen durch die komplexe Projektionsgeometrie mit konusförmigem Strahl sowie durch die mechanische Instabilität von

                                      -7-



C-Arm-Systemen, die sich nicht exakt auf einer Kreisbahn um das Objekt bewegen, sondern zum Beispiel leichte Schwingungen ausführen (Offenlegungsschrift
Abs. [0002]).


Zur Rekonstruktion von Strukturen mit niedrigem Röntgenkontrast (z. B. Weichteilen in medizinischen Daten) werden sehr viele Projektionsbilder benötigt, was
den Berechnungsaufwand stark erhöht und daher negative Auswirkungen auf die
Anwendbarkeit des Verfahrens haben kann. Während einer interventionellen
Katheterbehandlung muss die Rekonstruktion beispielsweise möglichst innerhalb
weniger Sekunden, maximal weniger Minuten, beendet sein (Offenlegungsschrift
Abs. [0003])


Ein bekanntes Verfahren für eine derartige Rekonstruktion (Feldkamp-Algorithmus), angepasst an C-Arm-Systeme gemäß D1 basiert auf Rückprojektion, d. h.
für jedes Voxel im Bildvolumen werden die Grauwerte der Projektionsbilder an den
entsprechenden Bildpunkten aufsummiert. Hierbei wird für jedes Projektionsbild
das zu rekonstruierende Bildvolumen Voxel für Voxel durchgegangen, die Projektion des Voxels berechnet und der Grauwert des entsprechenden Pixels des Projektionsbildes zu dem Wert des Voxels addiert.
Dieses Verfahren setzt voraus, dass die Projektionsgeometrie des Aufnahmesystems für jede Aufnahmeposition separat durch ein Kalibrierverfahren vorab bestimmt wurde. Dabei werden beliebige Verformungen und dynamische Bewegungen des Aufnahmesystems berücksichtigt, wodurch im Allgemeinen die Hauptachsen des zu rekonstruierenden Volumens in den Projektionsbildern keine einheitliche Ausrichtung besitzen. Daher muss für jede Projektion im Allgemeinen
angenommen werden, dass in keiner Richtung der Hauptachsen die Abstände
benachbarter Voxel in der Projektion einheitlich sind (Offenlegungsschrift
Abs. [0004], [0005]).


[0006] Für die bei C-Arm-Systemen auftretende allgemeine Projektionsgeometrie
müssen für jedes Voxel mindestens drei Additionen und zwei Divisionen durchge-

                                        -8-



führt werden, siehe z. B. Seite 395 des Artikels von K. Wiesent et al. in IEEE
Transactions on Medical Imaging (D1). Bei dem dort angegebenen Algorithmus
ergibt sich ein erheblicher Rechenaufwand. Außerdem ist ein wahlfreier Speicher-Zugriff auf die Projektionsdaten notwendig, der sich negativ auf die notwendigen
Speichertransfers zwischen Hauptspeicher und Cache auswirkt (Offenlegungsschrift Abs. [0006], [0007]).


Der Patentanmeldung soll die Aufgabe zugrunde liegen, ein schnelles Rekonstruktionsverfahren sowie eine entsprechende Vorrichtung bereitzustellen, welches
auch bei mechanisch instabilen Aufnahmesystemen verwendet werden kann
(Offenlegungsschrift Abs. [0008]).


Die Lehre der Patentanmeldung, die insbesondere durch den jeweiligen Patentanspruch 1 des Hauptantrags bzw. der Hilfsanträge 1, 2 und 3 unter Schutz gestellt werden soll, umfasst das Folgende:


Aus zweidimensionalen Projektionsbildern eines Objekts, die durch Rotation eines
Aufnahmesystems um das Objekt aus verschiedenen Projektionsrichtungen aufgenommen wurden, soll ein dreidimensionales Bildvolumen des Objekts rekonstruiert werden (Merkmal a)).
Zumindest eines (oder mehrere) der Projektionsbilder wird derart modifiziert (die
durch Verformungen und dynamische Bewegungen entstandenen Abweichungen
werden zumindest soweit herausgerechnet), dass es einem Projektionsbild entspricht, welches mit einem virtuellen Detektor aufgenommen wurde, dessen Spalten parallel zur Rotationsachse des Aufnahmesystems ausgerichtet sind
(Merkmal b), Fig. 3). Diese Modifikation kann insbesondere durch Anwendung
einer projektiven Transformation (Homographie) auf das ursprünglichen Projektionsbild (20) erfolgen (Merkmal h)).
Wenn benachbarte, äquidistante, auf einer Parallelen zur z-Achse gelegene Voxel
auf den virtuellen Detektor projiziert werden, so sind damit die Projektionen eben

                                       -9-



falls äquidistant, was die Berechnung der Rückprojektion vereinfacht (Abs. [0030],
[0031], Fig. 4).
Letztendlich werden (wie üblich) die Grauwerte der Voxel des Bildvolumens durch
Rückprojektion der Projektionsbilder berechnet (Merkmal c)).

Die Rückprojektion wird folgendermaßen durchgeführt:


Die Richtung der Rotationsachse des Aufnahmesystems wird als z-Richtung des
räumlichen Koordinatensystems definiert (Merkmal d)).
Bei der Rückprojektion für jedes modifizierte Projektionsbild werden die Voxel des
Bildvolumens in den drei Raumrichtungen (x-, y- und z-Richtung) in drei Schleifen
abgetastet, wobei jeweils die Projektion des Voxels auf das Projektionsbild (24)
berechnet und der entsprechende Grauwert des Projektionsbildes (24) zum Grauwert des Voxels akkumuliert wird (Merkmal e)), wobei die z-Richtung in der innersten Schleife abgetastet wird und dabei jeweils die vertikale Bildkoordinate des
Projektionsbildes durch Addition eines für die x- und y-Koordinaten dieser Schleife
konstanten Inkrements (Δv) berechnet wird (Merkmal f)).
Somit wird eine voxelgetriebene Rückprojektion durchgeführt (siehe D1 S. 395
re. Sp. oberes Drittel „voxel driven backprojection“), wobei für jedes Voxel des zu
rekonstruierenden Volumens der Ort (zweidimensionale Koordinaten) auf dem
virtuellen Detektor berechnet wird, an dem ein von der Quelle (3 in Fig. 1) ausgehender Strahl, der das Voxel passiert, auf den virtuellen Detektor trifft. Bei
dieser Berechnung wird die oben erwähnte Äquidistanz der Projektionsorte von
entlang der z-Richtung benachbarten Voxeln ausgenutzt, indem in der innersten
Schleife jeweils die Projektionen der Voxel einer sich in z-Richtung erstreckenden
Voxelspalte berechnet werden, was im virtuellen Projektionsbild zu einer entsprechenden vertikalen Spalte führt, auf der sich die Koordinaten benachbarter Punkte
jeweils nur um einen konstanten Wert unterscheiden. Damit muss jeweils zur
Ermittlung der nächsten Punktkoordinate nur ein für die gesamte vertikale Spalte
konstanter Wert zur vertikalen Koordinate des vorhergehenden Punkts addiert
werden. Die vertikale Richtung im virtuellen Projektionsbild ist offensichtlich als

                                            - 10 -



parallel zur z-Richtung definiert, auch wenn dies im Anspruch nicht direkt angegeben ist; vgl. die v-Richtung in Fig. 4.
Der zu der jeweils berechneten Koordinate des virtuellen Projektionsbilds gehörige
Projektionswert bzw. Grauwert wird für die Akkumulation bei der Rückprojektion
verwendet; insbesondere wird jeweils der Grauwert desjenigen Pixels des Projektionsbildes verwendet, dessen Koordinaten den berechneten Koordinaten am
nächsten liegen (Merkmal i)). Um auf diese Projektionswerte in der benötigten
Reihenfolge (jeweils entlang vertikaler Spalten) schnell zugreifen zu können, ist
das modifizierte Projektionsbild derart in einem Datenspeicher gespeichert, dass
vertikal benachbarte Pixel aufeinander folgen (Merkmal g)).


Als Fachmann sieht der Senat hier einen Physiker oder Informatik-Ingenieur an
mit mehrjähriger Erfahrung auf dem Gebiet der Verarbeitung digitaler radiologischer Bilddaten. Einem solchen Fachmann sind insbesondere die der Rekonstruktion eines dreidimensionalen Bildvolumens aus zweidimensionalen Projektionsbildern zugrunde liegende Projektionsgeometrie sowie die zugehörigen mathematischen Berechnungsmethoden geläufig.


2.   Der Gegenstand des Anspruchs 1 nach Hauptantrag und ebenso der
jeweilige Gegenstand des Anspruchs 1 nach Hilfsantrag 1, 2 und 3 sind nicht
patentfähig, da sie nicht auf erfinderischer Tätigkeit beruhen.


Dies ergibt sich aus den im Verfahren genannten Druckschriften.


2.1 Zusätzlich zu der unten unter 2.2 näher erläuterten Druckschrift D1 sind hierbei insbesondere die Druckschriften D2 und D4 relevant. Diese zeigen Folgendes:


D2 betrifft ein Verfahren und eine Vorrichtung zur dreidimensionalen Rekonstruktion von mit einem C-Arm-Gerät aufgenommenen Röntgenbildern, wobei die im
realen Betrieb auftretende relative Bewegung der Röntgenquelle zur Detektorebene kompensiert wird, indem die Projektionsbilder auf eine virtuelle (ideale)

                                        - 11 -



Detektorebene transformiert werden (Abstract, Sp. 1 Z. 44 bis Sp. 2 Z. 1, Sp. 3
Z. 18 bis 46, Anspruch 1; Fig. 2 bis 6); diese Bilder werden wie üblich rückprojiziert
(Fig. 6). Die Verwindung eines Projektionsbildes auf eine virtuelle Detektorebene
wird über eine planare Transformationsmatrix vorgenommen, welche mit allgemein
bekannten Verfahren berechnet wird (Sp. 2 Z. 28 bis 54).


D4 betrifft ein Verfahren zur schnellen parallelen Konusstrahl-Rekonstruktion
(cone beam reconstruction) für insbesondere medizinische Computertomographie
(CT) – Daten mit Hilfe eines oder mehrerer Mikroprozessoren (Abstract, Sp. 1
Abs. 2 bis 4). Die Rekonstruktion kann auf preisgünstiger, allgemein verfügbarer
Hardware durchgeführt werden; sie basiert auf dem Feldkamp-Algorithmus (Sp. 3
vorle. und le. Abs., insbesondere Z. 48). Hierbei werden im Zuge der Rückprojektion für jedes Projektionsbild die Voxel des Bildvolumens in drei Schleifen
abgetastet (Sp. 7 Z. 43 bis 52), wobei im Stand der Technik in der innersten
Schleife die Abtastung in x-Richtung erfolgt, die senkrecht zur z-Richtung der
Rotationsachse verläuft (Fig. 3 rechts). Um den Rekonstruktionsprozess zu
beschleunigen, lehrt D4 demgegenüber, in der innersten Schleife die z-Richtung
abzutasten und die Projektionsdaten jeweils in z- bzw. u-Richtung (vertikal)
aufeinander folgend im Cache zu speichern, was jeweils einen schnellen Zugriff
für die Berechnung einer z-Linie ermöglicht (Sp. 8 Z. 37 bis 43, Sp. 10 Z. 1 bis 12).


2.2 Ausgehend von dem aus der Druckschrift D1 Bekannten waren das Verfahren des Anspruchs 1 gemäß Hauptantrag und ebenso die Verfahren des jeweiligen Anspruchs 1 gemäß den Hilfsanträgen 1, 2 und 3 für den Fachmann naheliegend.


Die von der Anmelderin selbst genannte Druckschrift D1 zeigt ein Verfahren zur
Rekonstruktion eines dreidimensionalen Bildvolumens aus zweidimensionalen
Projektionsbildern eines Objekts, die durch Rotation eines Aufnahmesystems um
das Objekt aus verschiedenen Projektionsrichtungen aufgenommen wurden
(C-Arm System, vgl. Abstract und Fig. 4) – Merkmal a). Hierbei sollen Abweichun-

                                       - 12 -



gen von der idealen Feldkamp-Geometrie berücksichtigt werden, wobei die jeweils
aktuelle Geometrie gemessen wird (S. 392 re. Sp. Kap. B „FG2“ und „FG3“ mit
PDS „pose determination system“). Diese Messungen werden in die Rekonstruktion eingerechnet. Hierfür sind in D1 zwei alternative Möglichkeiten beschrieben:
zum einen die Interpolation der gemessenen Projektionsdaten auf eine ideale
Messgeometrie, die der perfekten Feldkamp-Geometrie entspricht (S. 394 li. Sp.
Kap. E Nr. 1)); hierbei sind die Spalten des (virtuellen) Detektors (v-Richtung)
parallel zur Rotationsachse des Aufnahmesystems (z-Richtung) ausgerichtet
(S. 392 re. Sp. Kap. B. unter „FG1: Ideal Feldkamp Geometry“: „Detector rows-
/columns are orthogonal/parallel to axis of rotation“) – Merkmale b), d). Die zweite,
in D1 näher ausgeführte Möglichkeit betrifft eine Modifizierung des Feldkamp-Algorithmus, wobei Information über die irreguläre Abtast-Geometrie innerhalb des
Rückprojektionsschritts verwendet wird (S. 394 li. Sp. Kap. E Nr. 2) ff., S. 395
Kap. H). In diesem zweiten Fall wird ein voxelgetriebenes Rückprojektionsverfahren eingesetzt, wobei die Voxel des Bildvolumens in drei Raumrichtungen
abgetastet werden und in der innersten Schleife (in der nicht die z-Richtung abgetastet wird) jeweils nicht nur Additionen, sondern auch Divisionen durchgeführt
werden (vgl. den Pseudocode auf S. 395 re. Sp. unten), wie dies in der vorliegenden Anmeldung Abs. [0006] und [0007] als Stand der Technik beschrieben ist.
In jedem Fall werden beim Feldkamp-Algorithmus die Grauwerte der Voxel durch
Rückprojektion der Projektionsbilder berechnet – Merkmal c).


Der Fachmann zog auch die in D1 angegebene Alternative des Kapitels E) Nr. 1)
in Betracht, in der die Projektionsdaten auf eine ideale Feldkamp-Geometrie umgerechnet werden. Aus der Druckschrift D4 konnte er die Lehre entnehmen, die
Rekonstruktion von Daten in einer Feldkamp-Geometrie unter anderem dadurch
zu beschleunigen, dass bei der Drei Schleifen – Abtastung für die Rückprojektion
(in der jeweils die Projektion eines Voxels auf das Projektionsbild berechnet und
der entsprechende Grauwert des Projektsbilds zum entsprechenden Grauwert des
Voxels akkumuliert wird) in der innersten Schleife die z-Richtung (Rotationsachsenrichtung) abgetastet wird und die Projektionsdaten jeweils in z- bzw. u-

                                       - 13 -



Richtung (vertikal) aufeinander folgend im Cache gespeichert werden, was jeweils
einen schnellen Zugriff für die Berechnung einer z-Spalte ermöglicht (D4 Sp. 8
Z. 37 bis 43, Sp. 10 Z. 1 bis 12). Aufgrund der erzielbaren Erhöhung der Berechnungsgeschwindigkeit musste es dem Fachmann vorteilhaft erscheinen, diese
Lehre in der eine ideale Feldkamp-Geometrie verwendenden Alternative der D1
Kapitel E) Nr. 1) anzuwenden. Damit sind die Merkmale e) und g) nahegelegt.
Dass bei der z-Abtastung in der innersten Schleife die vertikalen Koordinaten der
Pixel des Projektionsbildes sich jeweils nur durch ein für die x- und y-Koordinaten
dieser Schleife konstantes Inkrement unterscheiden, das zur jeweils vorherigen
vertikalen Koordinate addiert werden muss, ergibt sich aus der idealen Feldkamp-Geometrie, auf welche das Projektionsbild zuvor umgerechnet wurde, vgl. D1
S. 394 li. Sp. Kap. E Nr. 1) i. V. m. Fig. 2 sowie S. 392 re. Sp. Kap. B. unter
„FG1“ („regular (equidistant) sampling pattern“) – Merkmal f).


Damit beruht das Verfahren des Anspruchs 1 gemäß Hauptantrag nicht auf erfinderischer Tätigkeit.


Zudem lag es im Rahmen des Fachkönnens und -wissens eines hier anzunehmenden Fachmanns, die nötigen geometrischen Umformungen zur Rückrechnung
einer verzerrten Geometrie auf eine ideale Feldkamp-Geometrie, insbesondere
eine projektive Transformation bzw. Homographie vorzunehmen – Merkmal h).
Rein beispielhaft wird hierzu auf die Druckschrift D2 hingewiesen, welche ein
Verfahren und eine Vorrichtung zur dreiimensionalen Rekonstruktion von mit einem C-Arm-Gerät aufgenommenen Röntgenbildern mit Hilfe von Rückprojektion
zeigt, wobei die im realen Betrieb auftretende relative Bewegung der Röntgenquelle zur Detektorebene kompensiert wird, indem die Projektionsbilder auf eine
virtuelle (ideale) Detektorebene transformiert (verwunden) werden (Abstract, Sp. 1
Z. 44 bis Sp. 2 Z. 1, Sp. 3 Z. 18 bis 46, Anspruch 1; Fig. 2 bis 6); die hierbei zur
Verwendung eines Projektionsbildes vorgenommenen mathematischen Operationen werden dort unter Hinweis auf mehrere Druckschriften als allgemein bekannt
bezeichnet (D2 Sp. 2 Z. 37 bis 54).

                                        - 14 -



Somit war auch das Verfahren des Anspruchs 1 gemäß Hilfsantrag 1 für den
Fachmann naheliegend.


Des Weiteren wird gemäß D4 Sp. 10 Z. 1 bis bis 9 bei der Berechnung eines für
die Akkumulation bei der Rückprojektion verwendeten Grauwerts zwischen vier
benachbarten Punkten des Projektionsbildes interpoliert („four adjacent points (two
in each of the adjacent u-lines) are used to interpolate the data for one voxel in the
z-line“). Wie dem in der Bildverarbeitung bewanderten Fachmann geläufig war,
erhöht eine Interpolation zwischen mehreren Bildpunkten die Genauigkeit der jeweiligen Berechnung (hier: Berechnung der Grauwerte der Voxel des Bildvolumens), während eine ebenfalls fachüblich bekannte Verwendung nur eines, nämlich des nächstgelegenen Pixels eine etwas geringere Genauigkeit liefert, jedoch
eine schnellere Berechnung ermöglicht. Je nach seinen Prioritäten wählte der
Fachmann aus diesen beiden ihm bekannten Möglichkeiten eine geeignete aus;
kam es ihm vor allem auf eine hohe Geschwindigkeit der Berechnung an, was bei
medizinischen Eingriffen oft erwünscht ist, so bot sich ihm die Verwendung des
jeweils nächstgelegenen Pixels an. Für eine vom Fachmann routinemäßig vorgenommene Auswahl (hier: aus zwei bekannten Möglichkeiten) unter Abwägen der
jeweiligen Vor- und Nachteile, wobei Nachteile um der Vorteile willen in Kauf genommen werden, ist aber kein erfinderisches Zutun erforderlich; vgl. BGH GRUR
2006, 930 – Mikrotom.
Damit war auch Merkmal i) naheliegend.


Somit beruht auch das Verfahren des Anspruchs 1 gemäß Hilfsantrag 2 nicht auf
erfinderischer Tätigkeit.


Entsprechendes gilt für den Anspruch 1 gemäß Hilfsantrag 3, welcher die Merkmale h) und i) enthält. Jedes dieser Merkmale für sich war wie oben erläutert naheliegend. Ein kumulativer Effekt der beiden Maßnahmen „projektive Transformation“ und „Verwendung des nächstliegenden Pixels“, der über das von jeder dieser
Einzelmaßnahmen Erwartbare hinausgeht, ist nicht ersichtlich.

                                      - 15 -



Die Beschwerdeführerin bringt vor, der Fachmann hätte in D1 die zweite, dort näher behandelte Methode (Modifikation des Feldkamp-Algorithmus (S. 394 li. Sp.
Kap. E Nr. 2) ff.) bevorzugt, welche gemäß D1 eine bessere räumliche Auflösung
verspreche; die erste, nicht weiter ausgeführte Methode hätte er nicht berücksichtigt.
Zudem sei gemäß D1 S. 394 li. Sp. Kap. E Möglichkeit 1) zur Umrechnung der
Messdaten auf die ideale Feldkamp-Geometrie nur eine Interpolation vorgesehen,
welche insbesondere in der in D1 in diesem Zusammenhang zitierten Referenz [36] lediglich eine Verschiebung beinhalte, jedoch keine projektive Transformation.
Des Weiteren lehre D4 eine Interpolation der Pixel des Projektionsbildes für die
Akkumulation bei der Rückprojektion, also gerade nicht die Verwendung des
nächstliegenden Pixels wie nunmehr (in den Hilfsanträgen 2 und 3) beansprucht.
Im Zusammenhang mit der Speicherung vertikal benachbarter Pixel werde
dadurch die der Anmeldung zugrunde liegende Aufgabe besonders gut gelöst.


Dieses Vorbringen konnte nicht zu einer anderen Beurteilung führen.


Der Fachmann, dem in D1 prinzipiell zwei Alternativen (einerseits Rückrechnung
auf die ideale Feldkamp-Geometrie, andererseits Modifikation des Feldkamp-Algorithmus) aufgezeigt werden, zog ohne Weiteres auch die erste dieser beiden Alternativen in Betracht. Zwar versprach die zweite Alternative eine geringfügig bessere Auflösung, jedoch konnte die erste Alternative möglicherweise andere Vorteile aufweisen, weshalb eine nähere Befassung mit dieser grundsätzlich aussichtsreich erscheinen musste.
Zudem konnte der Fachmann dem im Zusammenhang mit der geometrischen
Umformung zitierten Absatz in D1 (S. 394 li. Sp. Kap. E Möglichkeit 1)) die allgemeine Lehre entnehmen, die Messdaten auf eine ideale Feldkamp-Geometrie hin
umzuformen. Hierfür waren ihm aus seinem Fachwissen verschiedene Möglichkeiten geläufig, etwa eine projektive Transformation; vgl. hierzu das oben mit Hinweis auf D2 Ausgeführte. Selbst wenn man der Anmelderin darin zustimmen

                                      - 16 -



wollte, dass aus D1 i. V. m. der dort zitierten Referenz [0036] nur eine Interpolation mit Verschiebung hervorgeht, so beschränkte sich der Fachmann jedenfalls
nicht allein auf diese, sondern wählte aus den ihm bekannten Transformationsmöglichkeiten eine ihm geeignet erscheinende aus. Hierzu war keine erfinderische
Tätigkeit erforderlich.
Des Weiteren ist der Beschwerdeführerin zwar darin zuzustimmen, dass nach der
Lehre der D4 zur Gewinnung eines Grauwerts für die Rückprojektion zwischen
benachbarten Pixeln des Projektionsbildes interpoliert wird. Jedoch waren dem
Fachmann, der in der Bildverarbeitung bewandert ist, wie oben erläutert sowohl
die Möglichkeit der Interpolation zwischen Pixeln als auch die andere Möglichkeit
der Verwendung des jeweils benachbarten Pixels mit ihren Vor- und Nachteilen
geläufig; je nach seinen Vorgaben wählte er ohne Weiteres eine dieser beiden
Möglichkeiten aus. D4 beschreibt bereits, die Pixel zweier benachbarter Spalten,
zwischen denen interpoliert wird („two adjacent u-lines“ in D4 Sp. 10 Z. 5 bis 11)
sowie die sich ergebenden Interpolationswerte einer Spalte im Cache zu speichern, so dass bei der Berechnung ein schneller Zugriff möglich ist. Verwendet der
Fachmann stattdessen jeweils nur das Nächstliegende Pixel, so ergibt sich entsprechend eine Speicherung der benachbarten Werte einer Spalte (vertikal benachbarte Pixel) im Cache.


Der Patentanspruch 1 gemäß Hauptantrag und ebenso der jeweilige Patentanspruch 1 gemäß den Hilfsanträgen 1, 2 und 3 sind nicht gewährbar.


3.   Auch die übrigen Patentansprüche des Hauptantrags und der Hilfsanträge 1,
2 und 3 sind nicht gewährbar, da über einen Antrag nur einheitlich entschieden
werden kann (BGH GRUR 1997, 120 – „Elektrisches Speicherheizgerät“).

                                            - 17 -



                                Rechtsmittelbelehrung


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




Dr. Morawek                    Eder            Dr. Thum-Rung                   Dr. Forkel


                                                                                       Fi
