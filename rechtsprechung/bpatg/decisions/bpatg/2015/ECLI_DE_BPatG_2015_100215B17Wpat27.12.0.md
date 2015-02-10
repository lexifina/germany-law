---
ecli: "ECLI:DE:BPatG:2015:100215B17Wpat27.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 27/12"
decided: "2015-02-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=6&nr=26936&anz=851&pos=95&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-02-10_17_W-pat_27_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 27/12 vom 2015-02-10

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 27/12                                                    Verkündet am
_______________                                                     10. Februar 2015
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2010 028 382.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 10. Februar 2015 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                     -2-



beschlossen:


        Die Beschwerde wird zurückgewiesen.


        Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                 Gründe:


                                      I.


Die vorliegende Patentanmeldung ist am 29. April 2010 beim Deutschen Patentund Markenamt eingereicht worden. Sie trägt die Bezeichnung


„Verfahren und Computersystem zur Bearbeitung tomographischer Bilddaten aus
         einer Röntgen-CT-Untersuchung eines Untersuchungsobjektes“.


Die Prüfungsstelle für Klasse G06T hat am 12. Dezember 2011 die Anmeldung
zurückgewiesen, da der Gegenstand des Patentanspruchs 1 nicht auf erfinderischer Tätigkeit beruhe.


Gegen den Beschluss wendet sich die am 9. Januar 2012 eingegangene
Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt sinngemäß,


        - den Beschluss über die Zurückweisung der Patentanmeldung
        aufzuheben und das nachgesuchte Patent mit folgenden Unterlagen zu erteilen:

                                      -3-



            Patentansprüche 1 bis 16 vom 20. Juni 2011, eingegangen
            am 22. Juni 2011,
            Beschreibung Seite 1 vom 7. Dezember 2012, eingegangen
            am 12. Dezember 2012,
            Beschreibung Seiten 3, 3a, 4, 4a, 5 vom 20. Juni 2011, eingegangen am 22. Juni 2011,
            Beschreibung Seiten 2, 6 bis 15, wie ursprünglich eingereicht,
            3 Blatt Zeichnungen mit Figuren 1 bis 3, wie ursprünglich eingereicht;


       - oder alternativ, die Angelegenheit zur weiteren Prüfung mit der
       Maßgabe der Durchführung einer Anhörung an die Prüfungsstelle
       des DPMA zurückzuverweisen.


Zudem regt sie an, die Beschwerdegebühr zurückzuzahlen.


Zur mündlichen Verhandlung ist die Anmelderin - wie angekündigt - nicht erschienen.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


       D1: Arne Militzer et al: "Probabilistic Boosting Trees for Automatic Bone
       Removal from CT Angiography Images". Proc. of SPIE, Vol. 7259, doi:
       10.1117/12.811886, Online Publication Date: 27 March 2009


       D2: Shai Avidan: "SpatialBoost: Adding Spatial Reasoning to AdaBoost".
       Springer-Verlag, 2006, Computer Vision – ECCV 2006, Lecture Notes in
       Computer Science, Vol. 3954, pp. 386-396, doi: 10.1007/11744085_30

                                       -4-



        D3: Shimizu, A. et al: "Ensemble segmentation using AdaBoost with
        application to liver lesion extraction from a CT volume". Published in The
        MIDAS Journal - Grand Challenge Liver Tumor Segmentation (2008
        MICCAI Workshop), herunterladbar über http://hdl.handle.net/10380/1411


        D4: F. Jäger, J. Hornegger: "Nonrigid Registration of Joint Histograms for
        Intensity Standardization in Magnetic Resonance Imaging", IEEE Trans.
        Medical Imaging, vol. 28, no. 1, pp. 137-150, Jan. 2009.


Der Senat hat zusätzlich die Druckschriften


        D5: Jonathan H. Morra et al: "Automatic Subcortical Segmentation Using
        a Novel Contextual Model"; Medical Image Computing and Computer-Assisted Intervention – MICCAI 2008, Springer Lecture Notes in Computer
        Science, Vol. 5241, 2008, pp. 194 - 201


        D6    Geoff Dougherty: Digital Image Processing for Medical Applications,
        Cambridge University Press 2009, ISBN 978-0-521-86085-7, Kap. 5.2
        "Histogram transformations and look-up tables", pp. 135 - 147


in das Verfahren eingeführt.


Der geltende Patentanspruch 1 betrifft (nach Korrektur eines offensichtlichen Fehlers) ein


        1.   Verfahren zur Bearbeitung tomographischer Bilddaten (B) aus einer
        Röntgen-CT-Untersuchung eines Untersuchungsobjektes (C7), aufweisend die folgenden Verfahrensschritte:

        1.1 Laden eines ersten Bilddatensatzes, bestehend aus einer Vielzahl
        von Bildpixeln mit ersten Bildwerten,

                                -5-



1.2 Normierung der ersten Bildwerte durch Transformation der Bildwerte
derart, dass danach das Histogramm der transformierten Bildwerte einem
vorgegebenen Standardhistogramm entspricht,

1.3 Berechnung eines Merkmalsvektors für jedes Bildpixel mit Bildmerkmalen auf der Basis der Eigenschaften der Bildpixel und/oder deren Umgebung,

1.4 erste Klassifikation der Bildpixel in Form eines Wahrscheinlichkeitsbildes auf der Basis der Merkmalsvektoren mit Berechnung der Wahrscheinlichkeit der Zugehörigkeit des jeweiligen Bildpixels zu einer Klasse
von Bildpixeln aus mindestens zwei unterschiedlichen Klassen durch ein
zuvor trainiertes und auf Wahrscheinlichkeitswerten basierendes Klassifikationsverfahrens mit den gleichen Merkmalsvektoren und Erstellung
eines Wahrscheinlichkeitsbildes aus den bildpixelbezogenen Wahrscheinlichkeitswerten,

1.5 iterative Klassifikation durch:


     1.5.1.   Ergänzung der Merkmalsvektoren jedes Bildpixels mit Wahrscheinlichkeitsmerkmalen auf der Basis der Wahrscheinlichkeitswerte der Bildpixel und/oder deren Umgebung mit dem zuletzt ermittelten Wahrscheinlichkeitsbild (W1, W2),

     1.5.2.   Durchführung mindestens einer weiteren Klassifikation durch
     Bewertung der ergänzten Merkmalsvektoren und

     1.5.3.   Ausgabe eines neuen Wahrscheinlichkeitsbildes (W1, W2)
     mit Wahrscheinlichkeitswerten für die Zugehörigkeit der Bildpixel zu
     mindestens einer Klasse,

                                        -6-



         1.6 Abbruch der iterativen Klassifikation nach einem vorgegebenen Abbruchkriterium und Ausgabe des letzten Wahrscheinlichkeitsbildes (W3)
         als Ergebnis, und

         1.7 Berechnung einer Kandidatenbildmaske aus dem letzten Wahrscheinlichkeitsbild (W3), wobei jedes Bildpixel eindeutig einer bestimmten
         Klasse zugeordnet wird.


Der nebengeordnete Patentanspruch 13 lautet (ebenfalls mit Korrektur eines
offensichtlichen Fehlers):


         „13. Computersystem (C10) mit einem Speicher zur Aufnahmen von
         Computerprogrammen, insbesondere in Verbindung mit einem CT-System (C1),
         dadurch gekennzeichnet, dass im Speicher des Computersystems (C10)
         Computerprogramme (Prg1 bis Prgn) gespeichert sind, welche im Betrieb
         das Verfahren gemäß einem der Verfahrensansprüche 1 bis 12 durchführen.“


Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.




                                         II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da der Gegenstand des Patentanspruchs 1
nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1
PatG).

                                       -7-



1.    Die Patentanmeldung betrifft ein Verfahren und ein Computersystem zur
Bearbeitung tomographischer Bilddaten aus einer Röntgen-CT-Untersuchung
eines Untersuchungsobjektes durch Berechnung von Merkmalsvektoren für die
Bildpixel, welche Eigenschaften der Pixel und/oder deren Umgebung enthalten,
Klassifikation der Pixel auf der Basis der berechneten Merkmalsvektoren durch
Wahrscheinlichkeitsbetrachtungen und Bestimmung einer Kandidatenbildmaske,
die jedes Pixel eindeutig einer bestimmten Klasse zuordnet (Offenlegungsschrift
Abs. [0001]).


Ähnliche, im Rahmen der Bildbearbeitung allgemein bekannte Verfahren nutzten
beispielsweise einen Probabilistic Boost Tree (PBT), der in einer Lernphase trainiert werde und in einer Erkennungsphase jedem Gebiet eines Bildes eine bestimmte Klasse zuweise (Offenlegungsschrift Abs. [0002]).
Solche Verfahren könnten u. a. im medizinischen Bereich eingesetzt werden. Beispielsweise würden zur Diagnose und Verlaufskontrolle von Lebertumoren sowie
zur Planung entsprechender Interventionen Kontrastmittelaufnahmen von CT-Volumina ausgewertet, in denen Tumore und andere Läsionen ein spezifisches
und vom Parenchym unterschiedliches Anreicherungsverhalten zeigten. Hierbei
sei eine genaue Segmentierung der fraglichen Läsionen, also eine punktweise
Unterteilung des Bildes in Läsionen und Hintergrund unerlässlich. Da eine manuelle Segmentierung aus Zeitgründen nicht praktikabel sei, werde ein automatisches, auf einem Computersystem ausführbares Verfahren benötigt (Offenlegungsschrift Abs. [0003]).
Ein dem erfindungsgemäßen Verfahren nahekommender Ansatz (siehe D3) benutze das maschinelle Lernverfahren AdaBoost, um Punkte in der Leber als zu
einer Läsion oder zum Hintergrund gehörend zu klassifizieren. Hierbei würden
zwei Klassifikatoren trainiert, einer zur Erkennung großer, der andere zur Erkennung kleiner Läsionen. Zur Verarbeitung eines neuen Bildes würden beide angewendet und ihre Ergebnisse fusioniert. Die hierbei vorgenommene willkürliche
Trennung der Punkte sei jedoch nachteilig (Offenlegungsschrift Abs. [0005]).

                                         -8-



Ein weiterer Schwachpunkt bisheriger Verfahren sei die mangelnde Berücksichtigung unterschiedlicher Kontrastierung der Daten. Teils werde eine Histogramm-Equalisierung durchgeführt, die aber nur visuell einen verbesserten Kontrast bringe, während gleichzeitig die Form der Intensitätsverteilung zerstört werde. Teils
würden Bilder auch normiert, indem von allen Intensitäten ihr Mittelwert abgezogen und durch ihre Standardabweichung geteilt werde. Da aber insbesondere bei
hypodensen Läsionen die Intensität des Parenchyms deutlich stärker durch das
Kontrastmittel beeinflusst werde als die der Läsion, werde durch die Normierung
der Grauwertbereich der Läsion unter Umständen weiter als erwünscht verschoben (Offenlegungsschrift Abs. [0006]).


Der Patentanmeldung soll demgegenüber die Aufgabe zu Grunde liegen, ein verbessertes Verfahren zur Bearbeitung tomographischer Bilddaten aus einer Röntgen-CT-Untersuchung eines Untersuchungsobjektes und Erkennung vorgegebener klassifizierter Objekte zu finden. Außerdem soll ein dieses Verfahren ausführendes Computersystem, insbesondere zur Anwendung für den diagnostischen
Bereich, vorgeschlagen werden (Offenlegungsschrift Abs. [0007] und ebenso geltende Beschreibung S. 3 le. Abs. bis S. 3a Abs. 1).


Durch den geltenden Anspruch 1 soll folgendes Verfahren unter Schutz gestellt
werden:


Ein aufgenommener und geladener Bilddatensatz, der aus Pixeln mit zugeordneten Bildwerten (Grau- bzw. Intensitätswerten) besteht, wird zunächst standardisiert, indem durch Transformation der Bildwerte sein Histogramm (Häufigkeitsverteilung der Bildwerte) an ein vorgegebenes Standardhistogramm angeglichen
wird - Merkmale 1.1, 1.2. Die Merkmalsformulierung schließt auch eine Histogramm-Equalisierung ein, selbst wenn diese in der Beschreibung als nachteilig
dargestellt ist (vgl. Offenlegungsschrift Abs. [0006], [0012], [0032]).

                                         -9-



Für jedes Pixel wird ein Merkmalsvektor mit Bildmerkmalen berechnet, auf der
Basis der Eigenschaften des Pixels und/oder seiner Umgebung - Merkmal 1.3.
Solche Bildmerkmale können der Grauwert des Pixels, der minimale, maximale
oder mittlere Grauwert der Pixel seiner Umgebung, Grauwertgradienten der Umgebung des Pixels usw. sein (Abs. [0014], [0033]).


Zur ersten Klassifikation der Pixel wird ein Klassifikationsverfahren verwendet, das
vorher (anhand von Beispielbildern bzw. Lerndatensätzen) mit den gleichen Merkmalsvektoren trainiert worden ist, und das für jedes Pixel eine Wahrscheinlichkeit
dafür liefert, dass das Pixel zu einer bestimmten, gesuchten Klasse (aus mindestens zwei unterschiedlichen Klassen) gehört; hieraus wird ein Wahrscheinlichkeitsbild erstellt (Abs. [0035]) - Merkmal 1.4. Ein solches Klassifikationsverfahren kann
beispielsweise ein PBT (probabilistic boosting tree) - Verfahren, ein AdaBoost -
Verfahren oder ein Support Vector Machine - Verfahren sein (Abs. [0016], [0034]).


Sodann wird eine iterative Klassifikation mit folgenden Schritten durchgeführt - Merkmal 1.5:


        - die Merkmalsvektoren jedes Pixels werden durch Wahrscheinlichkeitsmerkmale ergänzt, die aus den Wahrscheinlichkeitsmerkmalen des
          Pixels und/oder seiner Umgebung berechnet werden - Merkmal 1.5.1;
          solche Wahrscheinlichkeitsmerkmale können z. B. der Wahrscheinlichkeitswert des betrachteten Pixels, ein mittlerer Wahrscheinlichkeitswert
          der Umgebungspixel usw. sein (Abs. [0015], [0036]);

        - anhand der ergänzten Merkmalsvektoren wird mindestens eine weitere
          Klassifikation durchgeführt - Merkmal 1.5.2; hierfür muss (vorher) eine
          Lernphase durchlaufen werden, etwa zum Trainieren eines weiteren
          PBTs (Abs. [0036] le. Satz);

                                      - 10 -



        - die damit für jedes Pixel erhaltenen Wahrscheinlichkeitswerte für die
           Zugehörigkeit zu einer Klasse werden in Form eines neuen Wahrscheinlichkeitsbildes ausgegeben - Merkmal 1.5.3.


Die iterative Klassifikation wird nach einem vorgegebenen Abbruchkriterium abgebrochen und das letzte Wahrscheinlichkeitsbild als Ergebnis ausgegeben - Merkmal 1.6.


Aus dem letzten Wahrscheinlichkeitsbild wird eine „Kandidatenbildmaske“ berechnet, wobei jedes Pixel eindeutig einer bestimmten Klasse zugeordnet wird - Merkmal 1.7. D. h. den Pixeln wird anhand der letzten Wahrscheinlichkeitswerte eine
Klassenzugehörigkeit zugewiesen. Dies kann anhand einer Schwellwertoperation
erfolgen, evtl. nach vorgeschalteten Filteroperationen des Wahrscheinlichkeitsbildes zur Glättung (Abs. [0038]).


Unter „Pixel“ sind in der vorliegenden Anmeldung Elemente eines zwei- oder dreidimensionalen Bilddatensatzes (Pixel oder Voxel) zu verstehen, vgl. die ursprünglichen Unteransprüche 11 und 12.


Als Fachmann sieht der Senat hier einen in der Bildverarbeitung, insbesondere
der Analyse medizinischer Bilddaten bewanderten Naturwissenschaftler oder Ingenieur (Physiker, Elektrotechniker oder Informatiker) an, der mit Anwendern (Ärzten) zusammenarbeitet.


2.    Das Verfahren des Anspruchs 1 ist nicht patentfähig, da es nicht auf erfinderischer Tätigkeit beruht.


Dieses Verfahren war nämlich für den Fachmann angesichts des aus der Druckschrift D5 Bekannten und im Lichte seines Fachwissens, wie es etwa in D6 ausgewiesen ist, naheliegend.

                                        - 11 -



D5 beschreibt ein Verfahren zur automatischen Segmentierung von subkortikalen
Strukturen in Magnetresonanzbildern (MRI). Dass der Bilddatensatz vor seiner
Verarbeitung in das zur Segmentierung verwendete Computersystem geladen
werden muss, las der Fachmann mit - Merkmal 1.1. Gemäß Kap. 2 „Methods“ auf
S. 195 bis 197, insbesondere S. 195 unten bis S. 196 Mitte des Kap. 2.2 „Auto
Context Model“ wird ein Klassifikationsmodell gelernt. Zunächst wird ein erstes
Klassifikationsmodell auf der Basis von lokalen Bildbereichen („local image patches“) trainiert, wobei (anhand von Merkmalen des Grauwertbildes) für jedes
Voxel i eine erste Wahrscheinlichkeit Pk(0)(i) dafür berechnet wird, dass dieses
Voxel zu einer bestimmten Klasse k („label k“) gehört; die Klassifikatoren hierfür
werden etwa durch boosting oder SVM (Support Vector Machine) trainiert (S. 196
oben) - auf die Trainingsphase bezogener Teil der Merkmale 1.3 und 1.4. Sodann
werden in aufeinander folgenden Iterationsschritten jeweils neue Klassifikatoren
gelernt. Die verwendeten Merkmale sind unter anderem Nachbarschaftsmerkmale,
etwa Mittelwerte, Standardabweichungen und Gradienten (S. 196 Abs. 2). Die im
lernenden AdaBoost-Verfahren eingesetzten (zu einem starken Klassifikator kombinierten) schwachen Klassifikatoren sind „decision stumps“, die jeweils auf Basis
eines einzigen Merkmals entscheiden und sowohl auf dem Grauwertbild („image
map“) als auch auf dem Wahrscheinlichkeitsbild („probability map“) arbeiten. Folglich werden Nachbarschaftsmerkmale sowohl des Grauwertbildes als auch des
Wahrscheinlichkeitsbildes für die iterative Klassifikation verwendet. Der Algorithmus wird iteriert, bis er konvergiert, wobei in jedem Schritt ein neues Wahrscheinlichkeitsbild berechnet wird, vgl. auf S. 196 unten den eingerahmten Kasten -
Merkmale 1.5, 1.5.1, 1.5.2, 1.5.3 für die Trainingsphase. Beim Testen neuer Bilddaten werden im Wesentlichen dieselben Prozeduren verwendet wie in der Lernphase (S. 195 Abs. 1 Z. 9 und 10) - restlicher, auf die Testphase (Klassifikation
neuer Bilddaten anhand vorher trainierter Klassifikationsmodelle) bezogener Teil
der Merkmale 1.3, 1.4, 1.5, 1.5.1, 1.5.2, 1.5.3.
Gemäß S. 201 Abs. 1 kann auch ein Abbruchkriterium („stopping criterion“) eingesetzt werden; das Ergebnis des Verfahrens (Wahrscheinlichkeitsbild) muss dann
selbstverständlich ausgegeben werden - Merkmal 1.6.

                                      - 12 -



In D5 las der Fachmann außerdem mit, dass zur Information des Benutzers letztendlich aus den Wahrscheinlichkeiten eine eindeutige Zuordnung der Bildpunkte
zur gesuchten Klasse berechnet und angezeigt wird, vgl. D5 Fig. 3 mit den dort
eingerahmt hervorgehobenen gefundenen Strukturen - Merkmal 1.7.


Im Verfahren der D5 werden für die Lernphase und für die nachfolgende Testphase (Segmentierung neuer Daten) insgesamt mehrere Datensätze verwendet.
Dem Fachmann war es geläufig, dass diese unter verschiedenen Bedingungen
(zumindest an verschiedenen Untersuchungsobjekten) aufgenommenen Datensätze soweit möglich standardisiert werden müssen. Ein hierfür übliches Verfahren
war eine Histogramm-Equalisierung oder allgemein eine Anpassung an ein Standard-Histogramm, wie es der Fachbuchauszug D6 zeigt: Durch „histogram equalization“ können demnach z. B. unter unterschiedlichen Bedingungen aufgenommene Bilder standardisiert werden, die miteinander verglichen werden sollen; hierbei werden die Grau- bzw. Intensitätswerte eines Bildes so transformiert, dass sich
ein in etwa gleichverteiltes Histogramm ergibt (Kap. 5.2.2). Das Bild kann auch so
transformiert werden, dass sich ein Histogramm einer gewünschten (im Wesentlichen beliebig wählbaren) Form ergibt („histogram matching“, Kap. 5.2.3). Damit
war Merkmal 1.2 nahegelegt.


Im Verfahren der D5 werden Magnetresonanz-Bilddaten eines Untersuchungsobjekts segmentiert. Für den Fachmann bot es sich an, das Verfahren, das gute Segmentierungsergebnisse liefert (vgl. D5 Abstract le. Satz), und das unabhängig von
der jeweiligen Untersuchungsmodalität ist, auch auf andere dreidimensionale
medizinische Bilddaten von Untersuchungsobjekten anzuwenden, etwa auf Röntgen-CT-Daten - Merkmal 1.


3.    Auch die übrigen Patentansprüche sind nicht gewährbar, da über einen
Antrag nur einheitlich entschieden werden kann (BGH in GRUR 1997, 120 „Elektrisches Speicherheizgerät“).

                                      - 13 -



4.    Für eine Zurückverweisung an das Deutsche Patent- und Markenamt
bestand kein Anlass, da die Sache entscheidungsreif war.


5.    Die Beschwerdegebühr ist zurückzuzahlen.


Im Zurückweisungsbeschluss wurde der Antrag auf eine Anhörung abgelehnt, da
die Anmelderin die Fortführung des Verfahrens in schriftlicher Form vorgezogen
habe, nachdem die Prüfungsstelle im Erstbescheid eine Anhörung angeregt hatte.
Da sodann die Argumente im schriftlichen Verfahren ausgetauscht worden seien,
bestehe kein weiterer Bedarf zur Aufklärung des Sachverhalts.


In der Tatsache, dass die Anmelderin auf die Anregung im Erstbescheid hin nicht
die Prüfungsstelle zur Vereinbarung eines Anhörungstermins kontaktiert hat, sondern schriftlich argumentiert hat, ist jedoch kein Verzicht auf eine Anhörung im
weiteren Verfahren zu sehen, zumal die Anmelderin in jeder ihrer beiden Eingaben
hilfsweise eine Anhörung beantragt hat. Auch hat sie in ihrer ersten Eingabe die
Patentansprüche geändert, und sie hat sich in jeder Eingabe mit den Argumenten
der Prüfungsstelle auseinandergesetzt; damit hat sie ihre Bereitschaft erkennen
lassen, an einer zielgerichteten Fortführung des Prüfungsverfahrens mitzuwirken.


Wie der Senat in früheren Entscheidungen bereits mehrfach dargelegt hat, war
das ohne Anhörung durchgeführte Prüfungsverfahren in solchen Fällen regelmäßig mängelbehaftet; es kann nicht ausgeschlossen werden, dass dieser Mangel
ursächlich für die Beschwerdeerhebung war.


Es entspricht daher der Billigkeit, die Beschwerdegebühr zurückzuzahlen.

                                            - 14 -



                                Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


   das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
       kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg
       abgelehnt war,
   einem Beteiligten das rechtliche Gehör versagt war,
   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
       nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
       hat,
   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                 Eder                 Dr. Thum-Rung                  Dr. Forkel




                                                                                        Fa
