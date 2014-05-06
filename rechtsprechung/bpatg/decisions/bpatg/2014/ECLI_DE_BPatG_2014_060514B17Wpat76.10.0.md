---
ecli: "ECLI:DE:BPatG:2014:060514B17Wpat76.10.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 76/10"
decided: "2014-05-06"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=25&nr=26193&anz=1119&pos=385&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-05-06_17_W-pat_76_10_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 76/10 vom 2014-05-06

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 76/10                                                  Verkündet am
_______________                                                     6. Mai 2014
    (Aktenzeichen)                                                      …




                            BESCHLUSS

                          In der Beschwerdesache


             betreffend die Patentanmeldung 10 2008 050 049.6-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 6. Mai 2014 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin Dipl.-Phys.
Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                        -2-



beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der
        Prüfungsstelle für Klasse G06T des Deutschen Patent- und
        Markenamts vom 6. Mai 2010 aufgehoben und das Patent mit
        folgenden Unterlagen erteilt:


        Patentansprüche 1 bis 6 und
        Beschreibung Seiten 1, 1a, 2, 2a, 3 bis 16,
        jeweils überreicht in der mündlichen Verhandlung,
        5 Blatt Zeichnungen mit Figuren 1 bis 5B vom Anmeldetag.




                                    Gründe:


                                         I.


Die vorliegende Patentanmeldung ist am 1. Oktober 2008 beim Deutschen Patentund Markenamt unter der Bezeichnung


    „Verfahren zur Bestimmung einer die Objektgrenze eines Objekts in einem
               digitalen 3D-Datensatz annähernden 3D-Oberfläche“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat am 6. Mai 2010 die Anmeldung zurückgewiesen, da der Gegenstand des Patentanspruchs 1 nicht auf erfinderischer
Tätigkeit beruhe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.

                                       -3-



Die Beschwerdeführerin beantragt,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        Patentansprüche 1 bis 6 und
        Beschreibung Seiten 1, 1a, 2, 2a, 3 bis 16, jeweils überreicht in
        der mündlichen Verhandlung,
        5 Blatt Zeichnungen mit Figuren 1 bis 5B vom Anmeldetag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist folgende
Druckschrift genannt worden:


        D1: W.E.Lorensen, H.E.Cline: „Marching Cubes: A High Resolution 3D
             Surface Construction Algorithm“, ACM SIGGRAPH Computer
             Graphics, Vol. 21, Issue 4, July 1987, pp. 163 bis 169.


Der Senat hat zusätzlich die Druckschriften


        D2: DE 199 29 779 A1


        D3: L. Wang, J. Bai, K. Ying: "Adaptive approximation of the boundary
             surface of a neuron in confocal Microscopy volumetric images”, in:
             Medical & Biological Engineering & Computing 2003, Volume 41,
             Seiten 601-607


in das Verfahren eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.

                                       -4-



                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat auch Erfolg, da ein Patent nach dem nunmehr geltenden Antrag erteilt werden
kann.


1.      Gegenstand der Patentanmeldung ist ein Verfahren zur Bestimmung einer
die Objektgrenze eines Objekts in einem digitalen 3D-Datensatz annähernden 3D-Oberfläche.


Gemäß der Beschreibungseinleitung auf S. 1 Abs. 2 der ursprünglich eingereichten Unterlagen ist es auf vielen Gebieten der zerstörungsfreien nichtinvasiven
Mess- und Prüftechnik, z. B. auch der medizinischen Bildgebung im Rahmen einer
Diagnostik heute üblich, von zu untersuchenden Objekten, z. B. einem Patienten
einen digitalen dreidimensionalen Bilddatensatz, d. h. einen vollständig mit Voxeln
ausgefüllten dreidimensionalen Voxelblock zu erzeugen.


Um Objektgrenzen (etwa Oberflächen von Knochen) in einem derartigen Voxelblock darstellen zu können, müssten die Oberflächenpunkte innerhalb eines
Volumenblocks ermittelt werden (Segmentierung, S. 1 Abs. 3), etwa durch Bestimmung zusammengehöriger Volumenelemente oder durch Bestimmung von Randpunkten, z. B. durch Anwendung eines Gradientenoperators in Verbindung mit
einem Schwellwert (S. 2 Abs. 1 und 2). Mit Hilfe der segmentierten Oberflächenpunkte könne dann eine Oberflächendarstellung gebildet werden, etwa als Netz
aus Polygonen (Dreiecken, Vierecken usw.), welche sich an die segmentierten
Oberflächenvoxel anschmiegten (S. 2 le. Abs. bis S. 3 Abs. 2).


Bekannte Segmentierungsverfahren orientierten sich an einzelnen 3D-Schichten
oder an 3D-Voxelblöcken, etwa in einer hierarchischen Strukturierung des Volumens (S. 4 Abs. 1 bis 3).

                                         -5-



Bei vielen bekannten Methoden würden die Objekte oder Oberflächen bzw. die
hierzu gehörigen Voxel anhand von Schwellwerten ermittelt. Dies sei problematisch, da oft der Signalpegel innerhalb eines Objektes nicht konstant sei; z. B.
änderten sich die Voxelwerte bei der Magnetresonanztomographie mit zunehmendem Abstand von der Empfangsspule. Des Weiteren seien sämtliche Schwellwertverfahren anfällig für Störungen bzw. Rauschen in den Volumendaten, die insbesondere bei medizinischen Datensätzen z. B. aufgrund des Röntgenrauschens
oder allgemein des Signalrauschens häufig aufträten; dies führe zu Lücken in den
ermittelten Oberflächen (S. 4 le. Abs. bis S. 5 Abs. 1).


Durch die Lehre der Anmeldung soll die Aufgabe gelöst werden, ein verbessertes
Verfahren zur Bestimmung von 3D-Oberflächen anzugeben, welche die Objektgrenzen von Objekten in einem digitalen 3D-Datensatz annähern (S. 5 Abs. 2 der
ursprünglichen und der geltenden Unterlagen).


Der geltende Patentanspruch 1 lautet:


        „1.   Verfahren zur Bestimmung einer die Objektgrenze (6) eines
              Objekts (4) in einem digitalen 3D-Datensatz (2) annähernden
              3D-Oberfläche (14), mit folgenden Schritten:


              a) der 3D-Datensatz (2) wird in zusammenhängende 3D-Teilbereiche (10) von mindestens zwei Voxeln (8) in jeder
              der drei Raumrichtungen zerlegt,


              b) in jedem 3D-Teilbereich (10) wird unter Verwendung aller
              Voxel (8) des Teilbereiches (10) ein 3D-Gradient (g→ ) als
              Wahrscheinlichkeitsmaß (21) für das Vorhandensein der
              Objektgrenze (6) in diesem 3D-Teilbereich (10) sowie eine
              potentielle Lage (26) und Orientierung (24) der Objektgrenze
              (6) berechnet, wobei im 3D-Bereich (10) in jeder der drei

                                         -6-



              Raumrichtungen (x, y, z) für jede Voxelebene (20a-c) quer
              zur jeweiligen Raumrichtung (x, y, z) ein Mittelwert (Mx, y, z)
              der Werte der Voxel (8) gebildet wird und der 3D-Gradient
              (g→ ) aus den Mittelwerten (Mx, y, z) gebildet wird, und die
              Orientierung (24) der Objektgrenze (6) als Richtung des 3D-Gradienten (g→ ) ermittelt wird,


              c)   in jedem 3D-Teilbereich (10) wird anhand des Wahrscheinlichkeitsmaßes (21) und eines Kantenkriteriums (22)
              entschieden, ob die Objektgrenze (6) im 3D-Teilbereich (10)
              verläuft, wobei das Kantenkriterium (22) auf den 3D-Gradienten (g→ ) angewendet wird,


              d) aus einem Satz von für den 3D-Teilbereich (10) gegebenen Flächenstücken (F1-9) wird dasjenige ausgewählt,
              dessen Lage (26) und Orientierung (24) der ermittelten Lage
              (26) und Orientierung (24) der Objektgrenze (6) am nächsten
              kommt,


              e) die 3D-Oberfläche (14) wird als Vereinigungsmenge der
              ausgewählten Flächenstücke (F1-9) gebildet.“


Die auf den Anspruch 1 rückbezogenen Unteransprüche 2 bis 6 lauten (mit
markierter Korrektur eines offensichtlichen Schreibfehlers in Unteranspruch 3):


        „2.   Verfahren nach Anspruch 1, bei dem in Schritt c) als
              Kantenkriterium (22) der Betrag des 3D-Gradienten (|g→ |)
              anhand eines Schwellwertes (S1) geprüft wird.

                                       -7-



       3.    Verfahren nach Anspruch 2, bei dem in Schritt a) sich
             benachbarte 3D-Bereiche (10) in jeder der drei Raumrichtungen (x,y,z) um jeweils mindestens eine Voxelebene
             (20a-c) überlagern.


       4.    Verfahren nach einem der vorhergehenden Ansprüche, bei
             dem nach Schritt e) nicht aneinander schließende Flächenstücke (Fi, j) benachbarter 3D-Bereiche (10) durch Interpolation aneinander angepasst werden.


       5.    Verfahren nach einem der vorhergehenden Ansprüche, bei
             dem nach Schritt e) eine Lücke (18) in der 3D-Oberfläche
             (14) durch ein zusätzlich eingesetztes und interpoliertes
             Flächenstück (Fk) geschlossen wird.


       6.    Verfahren nach einem der vorhergehenden Ansprüche, bei
             dem nach Schritt e) eine Lücke in der 3D-Oberfläche (14)
             durch Austausch von Flächenstücken (Fi, j) gemäß einer
             Tabelle zulässiger Nachbarschaften von Flächenstücken (Fi)
             mit anderen Flächenstücken (Fj) aus der Menge der zulässigen Nachbarn geschlossen wird.“


Dem Verfahren des Anspruchs 1 liegt folgende Lehre zugrunde:


Der Volumendatensatz wird in zusammenhängende, mindestens 2x2x2 Voxel
umfassende 3D-Teilbereiche (Würfel 10 in Fig. 1) eingeteilt – Merkmal a). Innerhalb jedes Teilbereiches wird durch eine spezielle Mittelwertbildung unter
Verwendung aller Voxel des Teilbereichs ein Gradient (Fig. 3a) als Maß für die
Wahrscheinlichkeit bestimmt, dass in diesem Teilbereich eine Objektgrenze (Teil
einer Objektoberfläche) vorhanden ist; hierbei gibt die Richtung des 3D-Gradienten die potentielle Orientierung der Objektgrenze an, und die potentielle Lage der

                                        -8-



Objektgrenze ergibt sich aus der Lage des 3D-Teilbereichs (S. 14 Z. 18 bis 22) –
Merkmal b). Anhand eines auf den 3D-Gradienten angewendeten Kantenkriteriums wird entschieden, ob sich im Teilbereich tatsächlich eine Objektgrenze
befindet; eine Objektgrenze ist z. B. dann vorhanden, wenn der Betrag des
Gradienten größer ist als ein Schwellwert – Merkmal c). Wurde eine Objektgrenze
festgestellt, so wird aus einem Satz von vorgegebenen Flächenstücken mit
unterschiedlichen Lagen im Teilbereich (schraffierte Bereiche in Fig. 4) dasjenige
ausgewählt, dessen Lage und Orientierung der potentiellen Lage und Orientierung
der Objektgrenze am nächsten kommt – Merkmal d). Schließlich werden alle
derart ausgewählten Flächenstücke vereinigt und daraus die Objektoberfläche (in
Netzform) gebildet – Merkmal e). Hierbei können einzelne Flächenelemente
geändert oder hinzugefügt werden (Fig. 5A, 5B).


Als Fachmann für eine solche Lehre sieht der Senat hier einen Informatiker oder
Physiker mit Erfahrung in der dreidimensionalen Bildverarbeitung, insbesondere
der Segmentierung von (z.B. medizinischen) Volumendaten an.


2.    Die nunmehr geltenden Unterlagen liegen im Rahmen der ursprünglichen
Offenbarung.


Anspruch 1 ist gestützt auf die ursprünglichen Ansprüche 1, 2 und 4 sowie S. 6
Z. 4 bis 35, S. 8 le. Abs. bis S. 9 Abs. 1 und Fig. 4 mit Beschreibung.


Die geltenden Unteransprüche 2 bis 6 gehen hervor aus den ursprünglichen
Unteransprüchen 3 und 9 bis 12.


Die ebenfalls zulässigen Änderungen in der Beschreibung betreffen teilweise die
Darlegung des Standes der Technik, teilweise ergeben sie sich aus den geänderten Ansprüchen.

                                       -9-



3.    Das Verfahren gemäß dem Anspruch 1 ist neu gegenüber dem belegten
Stand der Technik und beruht auch auf erfinderischer Tätigkeit.


Die Druckschrift D1 zeigt in Kap. 4 das „Marching Cubes“ - Verfahren zur Ermittlung von Oberflächen in einem Volumendatensatz. Der Volumendatensatz wird in
gleich große Würfel eingeteilt, die nacheinander abgearbeitet werden. In jedem
Würfel werden diejenigen Eckpunkte markiert, deren Voxelwerte oberhalb eines
Schwellwerts liegen. Enthält dann ein Würfel sowohl markierte als auch unmarkierte Eckpunkte, so befindet sich im Würfel mindestens eine Objektgrenze. Je
nach Lage der markierten und der unmarkierten Eckpunkte und der demnach von
der Objektgrenze geschnittenen Würfelkanten wird dem Würfel eine von vierzehn
möglichen Anordnungen zugeordnet, in denen jeweils die Objektgrenzen als
Flächenstücke (Dreiecke) unterschiedlicher Lage und Orientierung im Würfel
verlaufen (Fig. 3 auf S. 165). Nach dieser Zuordnung wird die genaue Lage des
Oberflächenschnittpunkts auf jeder geschnittenen Würfelkante durch Interpolation
bestimmt (S. 165 li. Sp. 6. Abs., S. 166 li. Sp. oben Punkt 5). Mit Hilfe der
ermittelten Flächenstücke (Dreiecke) wird die gesamte Oberfläche dargestellt,
wobei zur Schattierung Gradienten an den einzelnen Ecken der Dreiecke
berechnet werden (S. 165 li. Sp. vorle. Abs. „The final step …“; S. 166 li. Sp. oben
Punkt 6 und 7). Wird die Auflösung einer Schicht des Volumens durch Mittelung
über vier Pixel zu einem reduziert, so reduziert sich die Anzahl der Dreiecke, die
Effizienz der Oberflächenkonstruktion wird verbessert und das Bild wird geglättet
(S. 166 re. Sp. Abs. 1).


In D2 wird eine Segmentierung eines (Ultraschall-) Volumendatensatzes durchgeführt über eine Einteilung des Datensatzes in Würfel (Voxel) und Selektieren der
einem Segmentierkriterium entsprechenden Voxel (Zusammenfassung). Gemäß
Sp. 2 Z. 34 bis 49 kann zur Segmentierung ein auf die Grauwerte der Voxel wirkender Schwellwert herangezogen werden; darüber hinaus wäre es auch möglich,
als Segmentierkriterium den Grauwertgradienten in Selektierrichtung (Richtung, in
der eine Volumenstruktur gesucht wird, vgl. Sp. 1 Z. 65 bis Sp. 2 Z. 15) heranzu-

                                      - 10 -



ziehen, um beispielsweise den Übergang von einer „festeren“ Struktur zu einer
nicht so festen Struktur feststellen zu können. Entsprechend den gefundenen
Übergängen werden die der gesuchten Struktur vorgelagerten Teile in der Darstellung „ausradiert“ (Fig. 4).


D3 betrifft die adaptive Annäherung der Oberfläche eines Neurons in Volumenbildern, die mithilfe konfokaler Mikroskopie erhalten wurden. Zur Bestimmung der
Oberfläche werden die Volumendaten f(x, y, z) zunächst in aneinander angrenzende Würfel („cubes“) von 2x2x2 Voxeln eingeteilt (Fig. 3, S. 606 li. Sp. Abs. 2). In
jedem Würfel werden die Würfelkanten daraufhin untersucht, ob sie von der Oberfläche geschnitten werden, unter Anderem anhand der Gradientenwerte an den
Würfelecken; werden mindestens drei Kanten geschnitten, so handelt es sich um
einen „edge cube“, d. h. einen von der Oberfläche geschnittenen Würfel (S. 604
Kap. 3.1, insbesondere Kriterium (ii)). Sodann werden die Lage und die Grauwerte
der Schnittpunkte der Oberfläche auf den Würfelkanten interpoliert. Im folgenden
Schritt (S. 604 Kap. 3.2) werden jeweils mehrere benachbarte Würfel zu Subbildern („sub-images“) zusammengefasst, welche Oberflächenschnittpunkte enthalten können. Mit Hilfe der Grauwerte der Oberflächenschnittpunkte in den geschnittenen Subbildern wird eine die gesuchte Oberfläche enthaltende dreidimensionale
Funktion in stückweise konstanter Form k(x, y, z) angenähert (vgl. Fig. 4 für den
zweidimensionalen Fall). Die gesuchte Oberfläche wird als Schnitt dieser Funktion
mit den Volumendaten f(x, y, z) über einen „Marching Cubes“ – Algorithmus (vgl.
D1) bestimmt (S. 604 Kap. 3.3).


In den Druckschriften D1 und D3, welche die Bestimmung von zusammengesetzten Oberflächen in Volumendaten über die Betrachtung von Teilbereichen
(Würfeln) zum Inhalt haben, werden somit in jedem Teilbereich über Grauwerte
(D1) oder Gradientenwerte (D3) an den einzelnen Ecken (in Verbindung mit
Schwellwerten) Schnittpunkte der Oberfläche mit den einzelnen Kanten bzw. diese
Kanten schneidende (evtl. mehrere) Flächenstücke ermittelt.

                                       - 11 -



Keiner dieser Druckschriften ist jedoch die Lehre zu entnehmen, pro Teilbereich
einen einzigen, in spezieller Weise gemittelten Gradienten auszuwerten, insbesondere aus dessen Richtung ein einziges Flächenstück der gesuchten Oberfläche zu
bestimmen (Merkmal b). Dies gilt auch für die in D1 S. 166 re. Sp. Abs. 1 angesprochene Glättung durch Mittelung über je vier Pixel in einer Volumenschicht,
welche lediglich zu einer insgesamt geringeren Anzahl von Pixeln bzw. Voxeln,
damit von Teilbereichen und von Flächenstücken führt, jedoch am prinzipiellen
Algorithmus mit Betrachtung der einzelnen Ecken und Kanten in jedem Teilbereich
nichts ändert. Auch D2 liefert keinen Anhaltspunkt auf die spezielle anmeldungsgemäße Oberflächenbestimmung.


Ohne Hinweis und Anregung im Stand der Technik war diese auch für den Fachmann nicht von sich aus naheliegend.


Es ist anzuerkennen, dass das beanspruchte Segmentierungsverfahren eine deutliche Vereinfachung gegenüber dem nachgewiesenen Stand der Technik darstellt
und durch Glättung von in den Volumendaten vorhandenen Störungen bzw.
Rauschen zu einer Reduzierung von Fehlern führen kann.


Das Verfahren gemäß Anspruch 1 ist damit neu und beruht auch auf erfinderischer Tätigkeit.


4.     Der Anspruch 1 ist gewährbar.


Die abhängigen Ansprüche 2 bis 6 beinhalten zweckmäßige Ausgestaltungen des
Verfahrens nach Patentanspruch 1 und sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.

                                           - 12 -



5.      Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
        Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
        Befangenheit mit Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
        sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
        zugestimmt hat,
     5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
        Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
     6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                   Eder                  Dr. Thum-Rung               Dr. Forkel




                                                                                         Me
