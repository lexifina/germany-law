---
ecli: "ECLI:DE:BPatG:2005:011205B17Wpat42.03.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 42/03"
decided: "2005-12-01"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2005&Sort=1&Seite=121&nr=18491&anz=1972&pos=1818&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2005-12-01_17_W-pat_42_03_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 42/03 vom 2005-12-01

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 42/03                                                    Verkündet am
 _______________                                                  1. Dezember 2005
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 198 42 944.4-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 1. Dezember 2005 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch sowie des Richters Dipl.-Ing. Prasch, der
Richterin Eder und des Richters Dipl.-Ing. Baumgardt


beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und




BPatG 154
08.05

                                        -2-



       Markenamts vom 2. Dezember 2002 aufgehoben und das Patent
       erteilt.


       Der Erteilung liegen folgende Unterlagen zugrunde:


       Patentansprüche 1 bis 23 gemäß Hilfsantrag 1, überreicht in der
       mündlichen Verhandlung, Beschreibung Seiten 1-7, 7a, 8-9, überreicht in der mündlichen Verhandlung, Seiten 10-41 vom Anmeldetag,
       9 Blatt Zeichnungen mit Figuren 1-14 vom Anmeldetag.

                                   Gründe


                                         I.

Die vorliegende Patentanmeldung mit der nunmehrigen Bezeichnung:


       "Verfahren zur Rekonstruktion eines dreidimensionalen Bildes eines im Rahmen einer Tomosynthese abgetasteten Objekts"


ist am 18. September 1998 beim Deutschen Patent- und Markenamt unter Inanspruchnahme     der   Priorität   der   Voranmeldung   DE 197 56 246.9    vom
17. Dezember 1997 eingereicht worden.


Sie wurde von der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und
Markenamts durch Beschluss vom 2. Dezember 2002 zurückgewiesen. Zu den
Gründen für die Zurückweisung wird auf den Bescheid vom 18. Februar 2002 verwiesen. Dort ist ausgeführt, dass die Gegenstände der nebengeordneten Patentansprüche 1 und 2 gegenüber dem Stand der Technik nicht auf einer erfinderischen Tätigkeit beruhen.

                                      -3-



Die Anmelderin hat Beschwerde eingelegt und stellt den Antrag,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:
       gemäß Hauptantrag mit Patentansprüchen 1 bis 23, überreicht in
       der mündlichen Verhandlung, Beschreibung Seiten 1-7, 7a, 8-9,
       überreicht in der mündlichen Verhandlung, Seiten 10 - 41 vom
       Anmeldetag, 9 Blatt Zeichnungen mit Figuren 1 - 14 vom Anmeldetag;
       gemäß Hilfsantrag 1 mit Patentansprüchen 1 - 23, überreicht in
       der mündlichen Verhandlung, Beschreibung und Zeichnungen mit
       Figuren wie Hauptantrag;
       gemäß Hilfsantrag 2 mit Patentansprüchen 1 - 19, überreicht in
       der mündlichen Verhandlung, Beschreibung und Zeichnungen mit
       Figuren wie Hauptantrag.


Der Anspruch 1 gemäß Hauptantrag lautet:


       „Verfahren zur Rekonstruktion eines dreidimensionalen Bildes eines im Rahmen einer Tomosynthese abgetasteten Objekts, wobei
       während der Abtastung mehrere in einem 2D-Projektionsbildraum
       liegende Einzelprojektionsbilder in Form digitaler Projektionsbilddaten des in einem 3D-Objektraum liegenden Objekts aufgenommen werden, welche zur Erzeugung des Rekonstruktionsbildes in
       ein 3D-Rekonstruktionsbildvolumen rückprojiziert werden, wobei
       das Objekt zur Aufnahme der Projektionsbilder unter verschiedenen Projektionswinkeln φ mittels Röntgenstrahlung durchstrahlt
       und die aus dem Objekt austretende Strahlung mittels eines digitale Ausgangsbildsignale liefernden Detektormittel aufgenommen
       wird, wobei die die Projektionsbilddaten darstellenden Ausgangsbildsignale einem Rechenmittel zur Bildrekonstruktion zugeführt

                                      -4-



werden, bei welchem Verfahren zunächst anhand folgender
Schritte ein im Rahmen der Rekonstruktion anzuwendendes Filter
erzeugt wird:


1.    Berechnung einer 3D-Übertragungsfunktion Hproj (ωx, ωy, ωz)
aus der Aufnahmegeometrie für die Einzelprojektionsbildaufnahme
und die Rückprojektion der Einzelprojektionsbilder in das 3D-Rekonstruktionsbildvolumen,


2.    Näherungsweise           Inversion    der    3D-Übertragungsfunktion
Hproj (ωx, ωy, ωz)      zur      Ermittlung       einer     Inversionsfunktion
Hinv (ωx, ωy, ωz),


3.    Erstellung       einer     3D-Filterfunktion        Hopt (ωx, ωy, ωz)   in
Abhängigkeit einer oder mehrerer gewünschter Bildeigenschaften
des Rekonstruktionsbildes,


4.    Ermittlung         einer       resultierenden           3D-Filterfunktion
Hfilter (ωx, ωy, ωz)   durch      Multiplikation     der      3D-Filterfunktion
Hopt (ωx, ωy, ωz) und der Inversionsfunktion Hinv (ωx, ωy, ωz),


5.    Ermittlung einer 2D-Filterfunktion H2Dfilter, φ (ωu, ωv) aus der
resultierenden 3D-Filterfunktion Hfilter, (ωx, ωy, ωz) durch Koordinatentransformation des 3D-Objektraums in den 2D-Projektionsbildraum der jeweiligen Einzelprojektionsbilder unter Projektionswinkel φ,
wonach die Rekonstruktion des Bildes im Rechenmittel mit folgenden Schritten erfolgt:

                                      -5-



       6.   Anwendung der 2D-Filterfunktion H2Dfilter, φ (ωu, ωv), auf die
       zugehörigen Einzelprojektionsbilddaten,


       7.   Erzeugung des Rekonstruktionsbildes durch Rückprojektion
       der nach 6. gefilterten Einzelprojektionsbilddaten in das 3D-Rekonstruktionsbildvolumen.“


Der Anspruch 1 gemäß Hilfsantrag 1 lautet:


       „Verfahren zur Rekonstruktion eines dreidimensionalen Bildes eines im Rahmen einer Tomosynthese abgetasteten Objekts, wobei
       während der Abtastung mehrere in einem 2D-Projektionsbildraum
       liegende Einzelprojektionsbilder in Form digitaler Projektionsbilddaten des in einem 3D-Objektraum liegenden Objekts aufgenommen werden, welche zur Erzeugung des Rekonstruktionsbildes in
       ein 3D-Rekonstruktionsbildvolumen rückprojiziert werden, wobei
       das Objekt zur Aufnahme der Projektionsbilder unter verschiedenen Projektionswinkeln φ mittels Röntgenstrahlung durchstrahlt
       und die aus dem Objekt austretende Strahlung mittels eines digitale Ausgangsbildsignale liefernden Detektormittel aufgenommen
       wird, wobei die die Projektionsbilddaten darstellenden Ausgangsbildsignale einem Rechenmittel zur Bildrekonstruktion durch rekonstruktive Verrechnung der Projektionsbilder in einen Satz von
       Schichtbildern durch gefilterte Rückprojektion zugeführt werden,
       bei welchem Verfahren zunächst anhand folgender Schritte das im
       Rahmen der Rekonstruktion anzuwendende Filter erzeugt wird:


       1.   Berechnung einer 3D-Übertragungsfunktion Hproj (ωx, ωy, ωz)
       aus der Aufnahmegeometrie für die Einzelprojektionsbildaufnahme
       und die Rückprojektion der Einzelprojektionsbilder in das 3D-Rekonstruktionsbildvolumen,

                                      -6-



2.    Näherungsweise           Inversion    der    3D-Übertragungsfunktion
Hproj (ωx, ωy, ωz)      zur      Ermittlung       einer     Inversionsfunktion
Hinv (ωx, ωy, ωz),


3.    Erstellung       einer     3D-Filterfunktion        Hopt (ωx, ωy, ωz)   in
Abhängigkeit mehrerer gewünschter Bildeigenschaften des Rekonstruktionsbildes, nämlich der Ausbildung eines homogenen
Schichtprofils, und einer spektralen Bildmanipulation zur Anpassung der Bildqualität an die interessierenden Objektcharakteristika
einschließlich der Dämpfung hochfrequenter Bildanteile unter Berücksichtigung der unvollständigen Abtastung in der Tomosynthese, indem ein erster Filteranteil HSpektrum (ωx, ωy) des spektralen Bildgehalts und ein zweiter Filteranteil Hprofil ωz) für die Definition des Schichtprofils zur Bildung von Hopt (ωx, ωy, ωz) miteinander multipliziert werden,


4.    Ermittlung         einer       resultierenden           3D-Filterfunktion
Hfilter (ωx, ωy, ωz)   durch      Multiplikation     der      3D-Filterfunktion
Hopt (ωx, ωy, ωz) und der Inversionsfunktion Hinv (ωx, ωy, ωz),


5.    Ermittlung einer 2D-Filterfunktion H2Dfilter, φ (ωu, ωv) aus der
resultierenden 3D-Filterfunktion Hfilter, (ωx, ωy, ωz) durch Koordinatentransformation des 3D-Objektraums in den 2D-Projektionsbildraum der jeweiligen Einzelprojektionsbilder unter Projektionswinkel φ,
wonach die Rekonstruktion des Bildes im Rechenmittel mit folgenden Schritten erfolgt:


6.    Anwendung der 2D-Filterfunktion H2Dfilter, φ (ωu, ωv), auf die
zugehörigen Einzelprojektionsbilddaten,

                                       -7-



         7.   Erzeugung des Rekonstruktionsbildes durch Rückprojektion
         der nach 6. gefilterten Einzelprojektionsbilddaten in das 3D-Rekonstruktionsbildvolumen.“


Hinsichtlich der weiteren Ansprüche und des Hilfsantrags 2 wird auf die Akten
verwiesen.


Die Anmelderin erläutert, dass mit dem beanspruchten Verfahren aus einer Anzahl
von Einzelprojektionsbildern, die bei der Abtastung eines Objekts mittels Röntgenstrahlen unter verschiedenen Winkeln gewonnen worden seien, ein dreidimensionales Bild des Objekts rekonstruiert werden solle. Hierzu werde gemäß den
Schritten 1 bis 5 des Anspruchs 1 eine 2D-Filterfunktion erzeugt, entsprechend
den Schritten 6 und 7 auf die Einzelprojektionen angewandt, und aus den derart
gefilterten Einzelprojektionen durch Rückprojektion das gewünschte dreidimensionale Bild des Objekts rekonstruiert. Dieses Verfahren, das in seiner Allgemeinheit
mit dem Hauptantrag beansprucht werde, sei dem einschlägigen Fachmann, einem Informatiker, der über Berufserfahrung auf dem Gebiet der medizintechnischen Anwendungen verfüge, durch die Ausführungen im entgegengehaltenen
Stand der Technik nicht nahegelegt. Das Verfahren nach dem Hilfsantrag 1 enthalte darüber hinaus konkrete Anweisungen, wie der Fachmann die Filterfunktion
gezielt in Hinsicht auf mehrere gewünschte Bildeigenschaften verbessern könne.
Das Verfahren nach dem jeweils nebengeordneten Anspruch 2 unterscheide sich
von dem des Anspruchs 1 dadurch, dass die Filterung nicht auf die 2D-Projektionen, sondern auf das rückprojizierte 3D-Bild angewandt werde.


                                        II.


Die in rechter Frist und Form erhobene Beschwerde ist zulässig. Sie hat insoweit
Erfolg, als sie zur Erteilung des nachgesuchten Patents nach dem Hilfsantrag 1
führt.

                                        -8-



1.    Das Verfahren gemäß dem Hauptantrag ist nicht patentfähig, da es sich für
den Fachmann in naheliegender Weise aus dem Stand der Technik ergibt und
deshalb nicht als auf erfinderischer Tätigkeit beruhend gilt (§§ 1 Abs. 1, 4 PatG).


In der Beschreibungseinleitung werden zunächst einige bekannte Verfahren erläutert, mit denen aus einzelnen, durch Abtastung eines Objektes unter verschiedenen Projektionswinkeln erzeugten zweidimensionalen Projektionsbildern ein
dreidimensionales Bild des Objekts rekonstruiert werden kann. Hierbei werden die
durch Abtastung gewonnenen Bilder einer Filterung unterzogen. Als gemeinsamer
Nachteil der bekannten Filtermethoden wird angeführt, dass die Bildqualität nicht
optimal sei. Entsprechend wird die der Anmeldung zugrunde liegende Aufgabe
darin gesehen, ein Verfahren zur Bildrekonstruktion anzugeben, bei dem die Bildqualität des Rekonstruktionsbildes manipulierbar und gegenüber dem Stand der
Technik verbessert ist (vgl. S. 7, Z. 29 ff. der geltenden Beschreibung).
Der Patentanspruch 1 nach dem Hauptantrag schlägt hierzu in den Schritten 1 bis
5 zunächst die Ermittlung einer 2D-Filterfunktion und in den Schritten 6 und 7 die
Anwendung der ermittelten 2D-Filterfunktion auf die einzelnen Projektionsbilder
zur Erzeugung eines 3D-Rekonstruktionsbildes vor. Die Anmelderin erläutert, dass
es ihr bei den Schritten 1 bis 5 nicht um den Prozess des Auffindens der mathematischen Filterfunktion gehe, sondern nur um die Anwendung der ermittelten
Filterfunktion bei der Rekonstruktion des 3D-Bildes.


Das Verfahren zur Rekonstruktion eines dreidimensionalen Bildes eines im Rahmen einer Tomosynthese abgetasteten Objekts nach dem Anspruch 1 gemäß
Hauptantrag ist dem Fachmann aus dem Aufsatz von Hiroshi Matsuo u. a. "Three-Dimensional Image Reconstruction by Digital Tomo-Synthesis Using Inverse
Filtering", veröffentlicht in IEEE Transactions on Medical Imaging, Vol. 12, No. 2,
Juni 1993, S. 307 - 313 nahegelegt. Als Fachmann für die Bearbeitung und Rekonstruktion von im Rahmen einer Tomosynthese aufgenommenen Bildern ist ein
Informatiker anzusehen, der auf dem Gebiet der medizinischen Bildverarbeitung
über praktische Berufserfahrung verfügt.

                                        -9-



Dieser Fachmann entnimmt dem Aufsatz von Hiroshi Matsuo u. a., dass zur Rekonstruktion eines dreidimensionalen Bildes aus den Projektionsbildern entsprechend den Schritten 1 und 2 des Anspruchs zunächst aus der bei der tomographischen Abtastung verwendeten Aufnahmegeometrie eine (3D-) Übertragungsfunktion und dann deren Inverse Hinv zu berechnen ist (vgl. Abs. 2 des Abstract S. 307,
Darstellung der Projektions- und Rekonstruktionsgeometrie in Figur 1 mit Abschnitt IV: Reconstruction using Inverse Filtering). Er wird aber auch darauf hingewiesen, dass, bedingt durch die Aufnahmegeometrie, der Abbildungsprozess
nur zu einer unvollständigen Information (incompleteness of information, vgl.
S. 308, rechte Sp. unten) führt, also nicht optimal ist. Zur Optimierung wird eine
Modifikation des inversen Filters bzw. der inversen Filterfunktion vorgeschlagen
(vgl. S. 310, linke Sp. unten). Diese Ausführungen veranlassen den Fachmann,
bei dem beanspruchten Rekonstruktionsverfahren die durch Inversion gewonnene
Übertragungsfunktion Hinv durch eine Optimierungsfunktion Hopt zu modifizieren,
und die resultierende Filterfunktion Hfilter zur (optimierten) Filterung zu benutzen,
wie in den Schritten 3 und 4 angegeben.
Die Anmelderin führt hiergegen an, dass die Besonderheit des Schritts 3 in der Art
und Weise der Optimierung der Filterung liege. Diesbezüglich ist Schritt 3 jedoch
lediglich zu entnehmen, dass die Optimierungsfunktion Hopt „in Abhängigkeit von
einer oder mehrerer gewünschter Eigenschaften des Rekonstruktionsbildes“ zu
erstellen sei. Über diesen allgemeinen Hinweis hinaus enthält Schritt 3 keine Anweisung, welche konkreten Modifikationen an der Filterfunktion vorzunehmen sind,
um gezielt eine bestimmte Bildeigenschaft zu verbessern. Die diesbezügliche Anweisung in Schritt 3 geht nicht über die allgemeine Anregung hinaus, die der
Fachmann bereits dem Aufsatz von Hiroshi Matsuo u. a. entnimmt.


Die nachfolgenden Schritte 5 bis 7 beschreiben die Anwendung der resultierenden
Filterfunktion Hfilter auf das durch Abtastung gewonnene Bild, um daraus das (optimierte) 3D-Rekonstruktionsbild des abgetasteten Objekts zu gewinnen. Schritt 7
schlägt hierzu den Einsatz der mathematischen Operation der Rückprojektion vor.

                                         - 10 -



Die Verwendung der Rückprojektion zur Gewinnung des Rekonstruktionsbildes
wird jedoch bereits in dem Aufsatz von Hiroshi Matsuo u. a. vorgeschlagen (vgl.
„backprojection“, S. 308, Abschnitt III i. V. m. Fig. 2). Dabei ist einzuräumen, dass
die Rekonstruktion mit der dort verwendeten optimierten Filterfunktion im
3D-Raum erfolgt, während nach den Schritten 5 und 6 des Anspruchs 1 die Filterung und Rückprojektion im zweidimensionalen Raum stattfindet, was eine
Transformation der 3D-Filterfunktion Hfilter in den 2D-Raum erfordert, um sie
- mathematisch gleichwirkend - auf die Einzelprojektionsbilder anwenden zu können. Dem Fachmann ist eine derartige Transformation, soweit man sie nicht seinen mathematischen Grundkenntnissen zurechnen will, jedenfalls durch die Ausführungen auf S. 307, re. Sp., oben nahegelegt. Dort ist eine Variante eines Rekonstruktionsverfahren (ectomography) beschrieben, bei dem die Filterung und
Rückprojektion zu dem genannten Zweck im zweidimensionalen Raum (twodimensional filtered backprojection) erfolgt.


Das Verfahren nach dem Patentanspruch 1 gemäß Hauptantrag war dem Fachmann sonach durch die Ausführungen in dem Aufsatz von Hiroshi Matsuo u. a.
nahegelegt.


Dem Hauptantrag der Anmelderin ist daher nicht zu folgen.


2.    Die Patentfähigkeit des Verfahrens nach dem Patentanspruch 1 gemäß
Hilfsantrag 1 ist jedoch anzuerkennen.


Die Merkmale des Anspruchs 1 nach dieser Fassung ergeben sich aus den ursprünglichen Patentansprüchen 1, 8 und 11 bzw. den Seiten 15 bis 17 der Voranmeldung. Diese Fassung des Patentanspruchs 1 ist daher zulässig.
Das mit dieser Fassung beanspruchte Verfahren ist auch durch den im Prüfungsverfahren genannten Stand der Technik nicht nahegelegt.

                                        - 11 -



Im Wesentlichen unterscheidet sich diese Fassung des Patentanspruchs 1 von
der nach dem Hauptantrag durch eine Präzisierung des Schritts 3, der sich mit der
Optimierung der Filterung befasst. Die Filterfunktion soll danach in Hinsicht auf
konkrete Bildeigenschaften, nämlich die Ausbildung eines homogenen Schichtprofils und der Anpassung an interessierende Objektcharakteristika einschließlich der
Dämpfung hochfrequenter Bildanteile, d. h. des Rauschens verbessert werden.
Hierzu schlägt Schritt 3 vor, einen ersten Filteranteil Hspektrum so zu bemessen,
dass Objektcharakteristika hervorgehoben werden und Rauschen reduziert wird
und einen zweiten Filteranteil Hprofil derart, dass das Schichtprofil homogenisiert
wird.
Eine Anregung in Hinsicht auf eine solche Gestaltung des Filters findet sich weder
in dem diskutierten Aufsatz von Hiroshi Matsuo u. a. noch in den weiteren im Prüfungsverfahren entgegengehaltenen Druckschriften:


Der Auszug aus dem "Lexikon der Computergrafik und Bildverarbeitung" Vieweg
Verlag 1994, S. 158 diente lediglich dem Nachweis, dass die Verwendung inverser
Filter bei der Bildrekonstruktion allgemein bekannt ist.
In dem Aufsatz "Practical considerations of the Wiener filtering technique on
Projection data for PET" von Shao, Karp und Countryman, veröffentlicht in IEEE
Transactions on Nuclear Science, Vol. 41, No. 4, August 1994, S. 1560-1565, wird
eine Modifikation des Wiener Filters vorgeschlagen, die gegenüber dem bisherigen Filterverfahren verbesserte Bildeigenschaften haben soll.
Auch der Auszug aus dem Buch von Gonzales und Woods "Digital Image
Processing", Addison-Wesley Publishing Company, 1992, S. 279-282 befasst sich
generell mit den Vorteilen der Wiener Filterung, die geringeres Rauschen gegenüber der inversen Filterung aufweisen soll.
In dem Buch von Morneburg "Bildgebende Systeme für die medizinische Diagnostik", Publicis MCD Verlag, 3. Aufl. 1995, S. 62-67, werden zwar verschiedene Rekonstruktionsverfahren für tomographische Abbildungssysteme erläutert. Auf S. 63
unten, S. 64 wird zur Rückprojektion ausgeführt, dass durch die Wahl der Filterfunktion der Charakter des Bildes gezielt beeinflusst werden kann. Eine Modifika-

                                      - 12 -



tion des Filters in der im Schritt 3 des Anspruchs 1 angegebenen Art kann jedoch
nicht hergeleitet werden.
Eine Anregung in dieser Hinsicht lässt sich auch unter Berücksichtigung der von
der Anmelderin in der ursprünglichen Beschreibungseinleitung genannten Druckschriften nicht erkennen. Es ist daher anzuerkennen, dass das Verfahren nach
dem Patentanspruch 1 gemäß Hilfsantrag 1 auf erfinderischer Tätigkeit beruht und
patentfähig ist.


Das Verfahren nach dem nebengeordneten Patentanspruch 2 unterscheidet sich
von dem Verfahren nach dem Anspruch 1 dadurch, dass die in Schritt 3 erstellte
resultierende Filterfunktion nicht in den zweidimensionalen Raum transformiert
und auf die einzelnen Projektionsbilder angewandt wird, sondern das dreidimensionale Rekonstruktionsbild einer Filterung unterzogen wird. Der Anspruch 2 beschreibt sonach einen anderen Lösungsweg für die gestellte Aufgabe, die jedoch
ebenfalls auf der besonderen Art der Optimierung der Filterfunktion beruht; die
Nebenordnung dieses Anspruch ist daher zulässig.


Die Änderungen in den untergeordneten Ansprüchen und in der Beschreibung
sind durch die ursprüngliche Offenbarung gedeckt bzw. stellen redaktionelle Anpassungen dar.


Bei dieser Sachlage war das Patent gemäß dem Hilfsantrag 1 zu erteilen. Deshalb
erübrigen sich Ausführungen zu Hilfsantrag 2.




Dr. Fritsch                 Prasch              Eder                Baumgardt




                                                                            WA
