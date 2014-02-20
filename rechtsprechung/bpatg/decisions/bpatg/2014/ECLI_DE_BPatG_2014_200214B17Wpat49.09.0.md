---
ecli: "ECLI:DE:BPatG:2014:200214B17Wpat49.09.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 49/09"
decided: "2014-02-20"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=10&nr=25965&anz=1119&pos=163&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-02-20_17_W-pat_49_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 49/09 vom 2014-02-20

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 49/09                                                 Verkündet am
_______________                                                  20. Februar 2014
    (Aktenzeichen)                                                      …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2005 007 630.0-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 20. Februar 2014 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, des Richters
Dipl.-Ing. Baumgardt und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                        -2-



beschlossen:


        Die Beschwerde wird zurückgewiesen.


        Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                       Gründe


                                         I.


Die vorliegende Patentanmeldung, die eine japanische Priorität vom 18. Februar 2004 in Anspruch nimmt, wurde am 18. Februar 2005 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


    „Berechnungsverfahren, Berechnungsvorrichtung und Computer-lesbares
          Aufzeichnungsmedium für das Packen von Drahtmaterialien“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 7. April 2009 mit der Begründung
zurückgewiesen, dass der Gegenstand des Patentanspruchs 1 unter das Patentierungsverbot des § 1 PatG falle, da die einzelnen Schritte des (beanspruchten)
Verfahrens einen Algorithmus darstellten und das Verfahren somit eine mathematische Methode als solche darstelle.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellt den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                        -3-



          gemäß Hauptantrag mit
          Patentansprüchen 1-5 vom 18.08.2009,
          noch anzupassender Beschreibung Seiten 1-3, 12-41 und
          19 Blatt Zeichnungen mit Figuren 1-19, jeweils vom Anmeldetag,
          Beschreibung Seiten 4, 8, 10, 11 vom 19.09.2007;


          gemäß Hilfsantrag mit
          Patentanspruch 4 gemäß Hauptantrag,
          im Übrigen ebenfalls wie Hauptantrag.


Ferner regte die Anmelderin die Rückzahlung der Beschwerdegebühr an.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist die Druckschrift


D1: WO 2004/013778 A2


genannt worden.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet (nach Korrektur eines offensichtlichen Schreibfehlers):


          (A) „Berechnungsverfahren, welches auf einem Computer ausgeführt wird, für den Entwurf einer Anordnung einer Vielzahl
               von Drähten für das Packen zu einem Drahtbündel, wobei
               die Querschnittformen der Vielzahl von Drähten durch eine
               Vielzahl von Kreisen (ci, mi) mit entsprechenden Durchmessern repräsentiert werden, und wobei der Computer folgende
               Schritte ausführt:

                                 -4-



(B) Anordnen der Vielzahl von Kreisen (ci, mi) in einer Ebene,
      ohne einander zu überlappen,


(C) Erzeugen (S3) eines anfänglichen Umfassungskreises (C),
      der die Vielzahl von Kreisen (ci, mi) umfasst,


(D) Erzeugen (S4) eines Zielkreises (D), der kleiner ist als der
      Umfassungskreis (C), mit demselben Mittelpunkt (x1, y1) wie
      der Umfassungskreis (C), derart, dass wenigstens einer (cn)
      aus der Vielzahl von Kreisen (ci, mi) aus dem Zielkreis (D)
      herausragt (S5: JA),


(E)   Berechnen (S7, S8) einer Anordnung für die Vielzahl von
      Kreisen (ci, mi) durch Bestimmen von Zielpositionen für die
      Vielzahl von Kreisen (ci, mi), zu denen die Kreise (ci, mi) mit
      Ausnahme des herausragenden Kreises (cn) innerhalb des
      Zielkreises (D) verschoben werden, ohne einander zu überlappen, um innerhalb des Zielkreises (D) einen Raum für den
      herausragenden Kreis (cn) zu schaffen, und Verschieben des
      herausragenden Kreises (cn) in den Raum innerhalb des Zielkreises (D), so dass der Zielkreis (D) zu einem Umfassungskreis für die berechnete Anordnung wird,


(F)   Erzeugen (S4) eines neuen Zielkreises, der kleiner als der
      aktuelle Zielkreis (D) ist und den bisher herausragenden
      Kreis (cn) umfasst, wenn der gesamte herausragende
      Kreis (cn) in den Zielkreis (D) eingefügt werden kann, und


(G) Zurückkehren zu dem Schritt des Berechnens (S7, S8) der
      Anordnung, um den Umfassungskreis zu reduzieren, und

                                        -5-



              Ausgeben (S12) der berechneten Anordnung als Berechnungsergebnis für das Packen der Drähte,


        dadurch gekennzeichnet, dass


        (H) der Berechnungsschritt (S7, S8) unter Berücksichtigung
              einer vordefinierten Verschiebungsbedingung für die den
              Drähten entsprechenden Kreise (ci, mi) erfolgt, wobei die
              Verschiebungsbedingung auf vorgegebenen Beschränkungen der Anordnung der zu packenden Drähte beruht,


        (I)   die Verschiebungsbedingung eine Verbindungsbeziehung
              von bestimmten Drähten (81, 91, 81', 91'), die zu einem
              zusammengesetzten Draht (8, 9) gehören, enthält, wenn die
              Vielzahl von Drähten einen durch bestimmte Drähten gebildeten zusammengesetzten Draht (8, 9) umfassen, und


        (J)   bestimmte Kreise (c11, c12; c1, c2, c3, c4), die dem zusammengesetzten Draht (8; 9) entsprechen, in Übereinstimmung mit
              der Verbindungsbeziehung für den zusammengesetzten
              Draht (8; 9) verschoben werden, wobei der ganze zusammengesetzte Draht (8; 9) nur dann verschoben wird, wenn
              alle die bestimmten Kreise (c11, c12; c1, c2, c3, c4), die dem
              zusammengesetzten Draht (8; 9) entsprechen, verschoben
              werden können.“


Zu den nebengeordneten Patentansprüchen 4 und 5 sowie zu den Unteransprüchen 2 und 3 wird auf die Akte verwiesen.


Der (einzige) Patentanspruch gemäß Hilfsantrag, hier mit einer möglichen Gliederung versehen, lautet (nach Korrektur eines offensichtlichen Schreibfehlers):

                                -6-



(a)   „Berechnungsvorrichtung für den Entwurf einer Anordnung
      einer Vielzahl von Drähten für das Packen zu einem Drahtbündel, wobei die Querschnittformen der Vielzahl von Drähten als eine Vielzahl von Kreisen (ci, mi) mit entsprechenden
      Durchmessern repräsentiert werden, und wobei die Berechnungsvorrichtung umfasst:


(b)   eine Umfassungskreis-Zieheinheit (3B) zum Erzeugen eines
      anfänglichen Umfassungskreises (C), der die Vielzahl von
      Kreisen (ci, mi) umfasst, die in einer Ebene angeordnet sind,
      ohne einander zu überlappen,


(c)   eine Zielkreis-Definitionseinheit (3C) zum Erzeugen eines
      Zielkreises (D), der kleiner ist als der Umfassungskreis (C)
      mit demselben Mittelpunkt (x1, y1) wie der Umfassungskreis (C) derart, dass wenigstens einer (cn) aus der Vielzahl
      von Kreisen (ci, mi) aus dem Zielkreis (D) herausragt,


(d)   eine Berechnungseinheit (3D, 3E) zum Berechnen einer
      Anordnung für die Vielzahl von Kreisen (ci, mi) durch Bestimmen von Zielpositionen für die Vielzahl von Kreisen (ci, mi),
      zu denen die Kreise (ci, mi) mit Ausnahme des herausragenden Kreises (cn) innerhalb des Zielkreises (D) verschoben
      werden, ohne einander zu überlappen, um innerhalb des
      Zielkreises (D)   einen   Raum    für   den   herausragenden
      Kreis (cn) zu schaffen, und Verschieben des herausragenden
      Kreises (cn) in den Raum innerhalb des Zielkreises (D), so
      dass der Zielkreis (D) zu einem Umfassungskreis für die
      berechnete Anordnung wird,

                                 -7-



(e)   eine Steuereinheit (3F) zum Erzeugen eines neuen Zielkreises, der kleiner als der aktuelle Zielkreis (D) ist und den bisher herausragenden Kreis (cn) umfasst, wenn der gesamte
      herausragende Kreis (cn) in den Zielkreis (D) eingefügt werden kann, wobei


(f)   die Berechnungseinheit (3D, 3E) eingerichtet ist, das Berechnen der Anordnung mit dem neuen Zielkreis zu wiederholen,
      um den Umfassungskreis zu reduzieren, und


(g)   eine Ausgabeeinheit (5) für das Ausgeben der berechneten
      Anordnung als Berechnungsergebnis für das Packen der
      Drähte,


dadurch gekennzeichnet dass


(h)   die Berechnungsvorrichtung eingerichtet ist, die Berechnung
      unter Berücksichtigung einer vordefinierten Verschiebungsbedingung für die den Drähten entsprechenden Kreise (ci,
      mi) auszuführen, wobei die Verschiebungsbedingung auf vorgegebenen Beschränkungen der Anordnung der zu packenden Drähte beruht,


(i)   die Verschiebungsbedingung eine Verbindungsbeziehung
      von bestimmten Drähten (81, 91, 81', 91'), die zu einem
      zusammengesetzten Draht (8, 9) gehören, enthält, wenn die
      Vielzahl von Drähten einen durch bestimmte Drähten gebildeten zusammengesetzten Draht (8, 9) umfassen, und


(j)   bestimmte Kreise (c11, c12; c1, c2, c3, c4), die dem zusammengesetzten Draht (8; 9) entsprechen, in Übereinstimmung mit

                                       -8-



             der Verbindungsbeziehung für den zusammengesetzten
             Draht (8; 9) verschoben werden, wobei der ganze zusammengesetzte Draht (8; 9) nur dann verschoben wird, wenn
             alle die bestimmten Kreise (c11, c12; c1, c2, c3, c4), die dem
             zusammengesetzten Draht (8; 9) entsprechen, verschoben
             werden können.“


Die Anmelderin trägt vor, dass der Gegenstand der Anmeldung ein allgemeines
Berechnungsverfahren für das kompakte Packen einer Mehrzahl von Drähten darstelle, welches unterschiedliche Konfigurationen von Einzel- oder zusammengesetzten Drähten berücksichtigen könne. Gegenüber aus dem Stand der Technik
bekannten Verfahren bestehe der Vorteil der vorliegenden Erfindung darin, dass
unter Anwendung von Verschiebungsbedingungen und Verbindungsbeziehungen
kompakte Anordnungen von Drähten beliebiger Art ermittelt werden könnten. Insbesondere gebe das beanspruchte Verfahren eine effiziente Datenverarbeitung
auch für zusammengesetzte Drähte und löse daher ein konkretes technisches
Problem.


Der Gegenstand nach Patentanspruch 1 sei nicht nur dem Patentschutz grundsätzlich zugänglich, er sei darüber hinaus neu und beruhe auch auf erfinderischer
Tätigkeit.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da das Verfahren des Patentanspruchs 1 nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.     Die vorliegende Patentanmeldung betrifft ein Berechnungsverfahren für das
Packen von mehreren Drahtmaterialien unter Erfüllung von Bedingungen für das

                                        -9-



Verschieben von Drahtmaterialien, eine entsprechende Berechnungsvorrichtung
und ein computerlesbares Aufzeichnungsmedium (Offenlegungsschrift, [0001]).


In der Beschreibungseinleitung wird ausgeführt, dass sowohl in Fahrzeugen als
auch Häusern Drahtbündel vorgesehen seien, die durch ein Zusammenbinden
mehrerer Drahtmaterialien wie z. B. mehrerer elektrischer Drähte hergestellt seien.
Die Drahtbündel dienten dazu, elektrische Geräte, elektronische Komponenten
usw. miteinander zu verbinden. Mittlerweile sei ein Bedarf an möglichst kompakten
Drahtbündeln entstanden. Dabei sei allerdings zu beachten, dass eine Verbesserung der Raumeffizienz nicht dazu führen dürfe, dass die elektrischen Eigenschaften der Drähte beeinträchtigt würden. Aus diesem Grunde müsse während des
Entwurfs einer Verkabelung ein möglichst kompaktes Drahtbündel berechnet werden (Offenlegungsschrift, [0002]).


Ein spezifisches und effizientes Berechnungsverfahren, welches den genannten
Zweck erfülle, sei bislang nicht bekannt.


Die der Anmeldung zugrunde liegende objektive Aufgabe sieht der Senat darin,
die Geometrie einer möglichst kompakten Anordnung eines Drahtbündels zu
ermitteln, welches nicht nur aus elektrischen Einfachdrähten sondern auch aus
zusammengesetzten Drähten, wie etwa verdrillten Drähten oder Flachdrähten,
aufgebaut ist.


Als Fachmann, der mit der Aufgabe betraut wird, ein Berechnungsverfahren zur
Ermittlung der Geometrie eines Drahtbündels zu verbessern, sieht der Senat
einen Planungsingenieur der Fachrichtung Elektrotechnik an, der sich mit der Verkabelung in Hausinstallationen und Kraftfahrzeugen befasst und über Kenntnisse
aus der algorithmischen Geometrie verfügt.

                                       - 10 -



2.    Zum Hauptantrag


Der Hauptantrag ist nicht gewährbar, weil der Gegenstand seines Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruht (§ 4 Satz 1 PatG).


2.1   Der Patentanspruch 1 bedarf der Auslegung.


Zur Lösung der genannten Aufgabe schlägt der Anspruch 1 ein Berechnungsverfahren mit den Merkmalen (A) bis (J) vor.


Der Patentanspruch 1 betrifft ganz allgemein ein Verfahren, welches auf einem
Computer ausgeführt wird und dazu dient, eine (geometrische) Anordnung einer
Vielzahl von Drähten zu entwerfen, wenn diese zu einem Drahtbündel gepackt
werden sollen. Die einzelnen Querschnitte der Drähte werden für die Berechnung
durch Kreise (ci, mi) mit entsprechenden Durchmessern dargestellt (Merkmal (A)).
In der Beschreibung wird hierzu ausgeführt, dass mit Hilfe des vorgeschlagenen
Berechnungsverfahrens der Außendurchmesser eines Drahtbündels bestimmt
wird, wobei das Drahtbündel durch das Binden und Packen von mehreren elektrischen Drähten zu einer kreisrunden Form mit minimaler Größe gebildet wird (Offenlegungsschrift, [0054]).


Laut Merkmal (B) werden in der Berechnung die Kreise in einer Ebene angeordnet, ohne dass sie einander überlappen.


Ein die Kreise umgebender großer Kreis, ein sog. „Umfassungskreis“, wird gezogen (Merkmal (C)).


Merkmal (D) besagt, dass ein sog. „Zielkreis“ ermittelt wird, der kleiner als der
„Umfassungskreis“ sein soll, aber denselben Mittelpunkt wie dieser haben soll.
Weiterhin soll der „Zielkreis“ so angelegt sein, dass wenigstens ein Kreis (cn) aus

                                      - 11 -



der Vielzahl der Kreise (ci, mi) aus dem „Zielkreis“ vorsteht bzw. herausragt (Offenlegungsschrift, [0060]).


Danach soll für die Vielzahl von Kreisen (ci, mi) eine neue Anordnung errechnet
werden, indem Zielpositionen bestimmt werden, zu denen diese Kreise (ci, mi) mit
Ausnahme des herausragenden Kreises (cn) innerhalb des „Zielkreises“ hin verschoben werden, ohne einander zu überlappen. Laut Beschreibung werden die
Kreise in der Reihenfolge der abnehmenden Distanz von dem vorstehenden
Kreis (cn) verschoben. Jeder Kreis soll dabei zu einer möglichst weit entfernten
Position verschoben werden. Falls keine Verschiebung möglich ist, bleibt der Kreis
an seiner Position (Offenlegungsschrift, [0062]). Der Kreis (cn) wird in den durch
die Verschiebung geschaffenen Raum innerhalb des „Zielkreises“ eingefügt, so
dass der „Zielkreis“ zum „Umfassungskreis“ für die berechnete Anordnung wird
(Merkmal (E)).


Gemäß Merkmal (F) wird ein neuer „Zielkreis“ gewählt, der kleiner als der aktuelle
„Zielkreis“ ist und den vormals herausragenden Kreis (cn) mit umfasst.


Die berechnete Anordnung mit „Umfassungskreis“ und „Zielkreis“ wird als Resultat
der beschriebenen Verarbeitungsprozedur für das Packen der Drähte z. B. in
Form einer Tabelle dem Benutzer ausgegeben. Laut Beschreibung enthält eine
solche Tabelle u. a. Positionen, Radien und Typen der elektrischen Drähte (Offenlegungsschrift, [0066]). Die ermittelte Anordnung bildet den Ausgangspunkt für
eine neue Berechnung des „Umfassungskreises“, mit dem Ziel eine noch kompaktere Anordnung des Drahtbündels zu erreichen (Merkmal (G)).


Merkmal (H) besagt, dass in obiger Berechnung vordefinierte Verschiebungsbedingungen für die den Drähten entsprechende Kreise berücksichtigt werden sollen, wobei die Verschiebungsbedingungen auf Beschränkungen in der Anordnung
der zu packenden Drähte beruhen. Damit ist gemeint, dass im Verfahren Bedingungen für das Verschieben der Drahtmaterialien beachtet werden sollen (Offen-

                                       - 12 -



legungsschrift, [0005]). Laut Beschreibung ergeben sich die zu beachtenden
Bedingungen aus den jeweiligen Typen der zu bündelnden Drähte, z. B. daraus,
ob es sich bei den Drähten um Einfachdrähte oder zusammengesetzte Drähte
handeln soll (Offenlegungsschrift, [0057]).


Falls die zu bündelnden Drähte einen zusammengesetzten Draht beinhalten, soll
die Verschiebungsbedingung eine Verbindungsbeziehung für diejenigen Drähte
beinhalten bzw. begründen, welche zum zusammengesetzten Draht gehören
(Merkmal (I)). In der Beschreibung wird hierzu ausgeführt, dass die zu einem
zusammengesetzten Draht gehörenden Kreise immer so verschoben werden sollen, dass die Verbindungsbeziehung zwischen den Kreisen aufrechterhalten wird
(Offenlegungsschrift, [0063], [0069], [0070]). Dies bedeutet, dass wenn ein verschobener Kreis zu einem zusammengesetzten Draht gehört, die anderen Kreise
des zusammengesetzten Drahtes unter Beibehaltung der Verbindungsbeziehung
verschoben werden müssen. Deshalb werden die Kreise desselben zusammengesetzten Drahtes aufeinanderfolgend bewegt (Offenlegungsschrift, [0086]). Eine
Variation der Form des zusammengesetzten Drahtes infolge der Verschiebung ist
gemäß den Figuren 10 A bis C erlaubt.


Merkmal (J) besagt im Wesentlichen, dass ein zusammengesetzter Draht immer
nur dann verschoben werden darf, wenn alle die ihn beschreibenden Kreise als
Gesamtheit verschoben werden können (Offenlegungsschrift, [0069], [0070],
[0086]).


2.2   Zur Beurteilung der beanspruchten Lehre ist die Druckschrift D1 von besonderer Bedeutung. Sie beschreibt insbesondere ein Verfahren nach den Merkmalen (A) bis (G) des Patentanspruchs 1 nach Hauptantrag.


Die Druckschrift D1, die auf eine PCT Anmeldung der Anmelderin zurückgeht,
offenbart ein Verfahren und ein System zur numerischen Berechnung einer kompakten Anordnung von Drähten in einem Drahtbündel (Seite 1, Zeilen 7-10;

                                          - 13 -



Seite 12, Zeilen 19ff.) durch iterative Bestimmung des Außendurchmessers eines
gepackten Drahtbündels. Dabei wird das Layout eines Drahtbündels durch Verschieben der Einzeldrähte solange geändert, bis alle Drähte innerhalb eines minimalen Umfassungskreises angeordnet werden können, ohne einander zu überlappen. Die Anwendung des Konzepts von Voronoi Diagrammen unterstützt eine
einfache und schnelle Berechnung des Durchmessers des Drahtbündels (Fig. 2;
Seite 3, Zeile 15 – Seite 5, Zeile 12).


Die Druckschrift D1 lehrt damit ein computerimplementiertes Berechnungsverfahren, das dem Entwurf einer Anordnung von Drähten in einem Drahtbündel dient.
Dabei werden die Drähte im Rahmen eines Modells als Kreise repräsentiert
(Seite 15, Zeilen 1-12 – Merkmal (A)).


Die Kreise sind so angeordnet, dass sie einander nicht überlappen (Seite 16, Zeilen 4-7 - Merkmal (B)).


Um die Kreise wird ein Umfassungskreis gezogen (Seite 16, Zeilen 6-7 – Merkmal (C)).


Danach wird ein gegenüber dem Umfassungskreis kleinerer Zielkreis derart
bestimmt, dass zumindest einer der angeordneten Kreise aus dem Zielkreis hervorragt (Seite 16, Zeilen 9-19 – Merkmal (D)).


Danach werden die Kreise innerhalb des Zielkreises so verschoben, dass auch
der vormals vorstehende Kreis in dem Zielkreis untergebracht werden kann; der
Zielkreis wird zum neuen Umfassungskreis (Seite 16, Zeile 21 – Seite 17, Zeile 6
- Merkmal (E)).


Hiervon ausgehend wird iterativ ein minimaler Umfassungskreis ermittelt, in dem
schließlich idealerweise alle Kreise angeordnet werden können. Die Rechnung
basiert im Wesentlichen auf einer wiederholten Verschiebung der Kreise und einer

                                     - 14 -



iterativen Verkleinerung des Umfassungskreises (Seite 17, Zeile 8 – Seite 18,
Zeile 6 – Merkmale (F) und (G)).


Von der Lehre der Druckschrift D1 unterscheidet sich die Lehre nach Patentanspruch 1 gemäß Hauptantrag nur noch durch die Merkmale (H), (I) und (J), die im
Wesentlichen die Berücksichtigung von Verschiebungsbedingungen und Verbindungsbeziehungen zusammengesetzter Drähte betreffen.


2.3   Der Gegenstand des Patentanspruchs 1 ist durch die Druckschrift D1 nahegelegt, da die Merkmale (H), (I) und (J) zu einer technischen Problemlösung nicht
beitragen und daher bei der Beurteilung der erfinderischen Tätigkeit nicht zu
berücksichtigen sind (BGH GRUR 2011, 125 - Wiedergabe topografischer Informationen).


Die Anmeldung geht davon aus, dass es bekannte Verfahren zur Berechnung
möglichst kompakter Anordnungen von mehreren Drahtmaterialien nicht zulassen,
kompakte Drahtbündel mit zusammengesetzten Drähten wie z. B. Flachdrähten
oder verdrillten Drähten zu berücksichtigen. Zur Abhilfe schlägt der Patentanspruch 1 in den kennzeichnenden Merkmalen (H), (I) und (J) im Wesentlichen vor,
bereits vordefinierte Verschiebungsbedingungen für die zu packenden Drähte zu
berücksichtigen, wobei die Verschiebungsbedingungen für zusammengesetzte
Drähte noch Verbindungsbeziehungen enthalten sollen, die den inneren Aufbau
der zusammengesetzten Drähte beschreiben. Der Vorschlag, ein Berechnungsverfahren für kompakte Anordnungen von Drahtbündeln um die Einhaltung solcher
Verschiebungsbedingungen inklusive Verbindungsbeziehungen zu erweitern, setzt
keine auf technischen Überlegungen beruhenden Erkenntnisse voraus, sondern
beruht lediglich auf geometrischen, also mathematischen Überlegungen.


Zwar setzt die Definition von konkreten Verschiebungsbedingungen für bestimmte
zusammengesetzte Drähte zur Beschreibung von deren Eigenschaften im Berechnungsmodell ein technisches Grundwissen voraus. Jedoch wird die Definition

                                       - 15 -



solcher konkreter Bedingungen durch die Merkmale (H) bis (J) gerade nicht
geleistet, sondern ist diesen, aber auch der beanspruchten Lehre insgesamt vorgelagert und daher nicht Bestandteil der Lösung. Entsprechendes gilt für die Festlegung der Verbindungsbeziehungen, die z. B. angeben, ob die aneinandergrenzenden Einzeldrähte eines zusammengesetzten Drahtes geradlinig in Reihe, auf
einer gekrümmten Bahn oder in flächiger Konfiguration angeordnet sind (Offenlegungsschrift, Fig. 10, Fig. 14). Die Anwendung der Verschiebungsbedingungen
und Verbindungsbeziehungen, so dass z. B. die einen zusammengesetzten Draht
repräsentierenden Kreise immer nur als gedankliche Einheit verschoben werden
dürfen, folgt allein den aus der algorithmischen Geometrie bekannten Regeln.
Eine technische Leistung, wie sie möglicherweise für die Umsetzung der Anwendung von Verschiebungsbedingungen und Verbindungsbeziehungen bei Gebrauch von technischen Mitteln zu erbringen war, ist ersichtlich nicht Gegenstand
des Patentanspruchs 1.


Die Merkmale (H) bis (J) haben nach allem keine Lösung eines technischen Problems mit technischen Mitteln zum Gegenstand und müssen bei der Beurteilung der
erfinderischen Tätigkeit unberücksichtigt bleiben.


Nach Überzeugung des Senats kann die Tatsache, dass in den Modellberechnungen für Drahtbündel Angaben zu physikalischen Größen (mit „technischen Daten“)
verarbeitet werden, allein keine Grundlage dafür liefern, den Unterschiedsmerkmalen (H) bis (J) einen Teilaspekt zuzubilligen, der ein technisches Problem
bewältigt (vgl. BGH GRUR 2005, 143 - Rentabilitätsermittlung, III. 4c letzter Absatz).


Dem Einwand der Anmelderin, das beanspruchte Verfahren stelle einen Zwischenschritt in einem Vorgang dar, der in der Herstellung von Kabelbäumen resultiere, weswegen die Erfindung entsprechend der BGH Entscheidung „Logikverifikation“ (BGH GRUR 2000, 498) eine technische Aufgabe löse und alle Merkmale
zu berücksichtigen seien, kann nicht gefolgt werden.

                                       - 16 -



Dass dem in der angeführten Entscheidung beschriebenen Verfahren eine Zugänglichkeit zum Patentschutz zugebilligt wurde, war auf den gegenüber bekannten Verifikationsverfahren erzielten, auf einer Reduktion der zu vergleichenden
Daten beruhenden Vorteil zurückzuführen, der allein in Kenntnis der schaltungstechnischen Zusammenhänge durch technisches Fachwissen erbracht werden
konnte. Vergleichbare, auf technischen Überlegungen beruhende Erkenntnisse
sind aber zumindest in den Merkmalen (H) bis (J) des Patentanspruchs 1 nicht zu
entdecken.


Nach allem ist das Verfahren nach dem Patentanspruch 1 gemäß Hauptantrag
durch den Stand der Technik nahegelegt, da die jeweiligen Merkmale (H), (I) und
(J) keinerlei technischen Beitrag liefern können.


2.4   Da über einen Antrag nur einheitlich entschieden werden kann, sind auch
die abhängigen Patentansprüche 2 und 3 sowie die nebengeordneten Patentansprüche 4 und 5 nicht gewährbar (BGH GRUR 1997, 120 - Elektrisches Speicherheizgerät).


3.    Zum Hilfsantrag


Der Hilfsantrag kann nicht günstiger beurteilt werden, da sein beanspruchter
Gegenstand durch den Stand der Technik nahegelegt ist.


Der (einzige) Patentanspruch gemäß Hilfsantrag ist auf eine „Berechnungsvorrichtung“ gerichtet. Er enthält zwar gegenüber dem Patentanspruch 1 gemäß
Hauptantrag zusätzlich ein paar technische Mittel, wie z. B. eine Berechnungseinheit, eine Steuereinheit oder eine Ausgabeeinheit. Diese betreffen jedoch nichts,
was im gegebenen Zusammenhang nicht selbstverständlich wäre.

                                       - 17 -



Daher ist für den Patentanspruch gemäß Hilfsantrag eine andere Beurteilung als
für den Patentanspruch 1 gemäß Hauptantrag nicht gerechtfertigt. Die dortige
Argumentation gilt in gleicher Weise für den Hilfsantrag.


4.    Die Beschwerdegebühr ist zurückzuzahlen.


Die Anmelderin ist in ihrer Eingabe vom 19. September 2007 auf die Argumentation der Prüfungsstelle im vorhergehenden (einzigen) Prüfungsbescheid eingegangen und hat ihre von der Beurteilung der Prüfungsstelle abweichende Sicht der
Dinge erläutert. Hilfsweise hat sie eine Anhörung beantragt. In ihrer Eingabe hat
sie zudem neue Unterlagen mit neuen Patentansprüchen eingereicht. Daraufhin
folgte der Zurückweisungsbeschluss, in welchem die beantragte Anhörung „aus
Gründen der Verfahrensökonomie nicht als sachdienlich“ bezeichnet und damit
abgelehnt wurde.


Wie der Senat in früheren Entscheidungen bereits mehrfach dargelegt hat, war
das Prüfungsverfahren in solchen Fällen regelmäßig mängelbehaftet; es kann
nicht ausgeschlossen werden, dass dieser Mangel ursächlich für die Beschwerdeerhebung war (vgl. etwa 17 W (pat) 74/07, 17 W (pat) 86/07, 17 W (pat) 113/07,
17 W (pat) 76/09).


Es entspricht der Billigkeit, die Beschwerdegebühr zurückzuzahlen.




                                         III.


1.    Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde
der Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamtes zurückzuweisen.

                                            - 18 -



2.      Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
        Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
        sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
        zugestimmt hat,
     5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
        Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
     6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                     Eder                 Baumgardt                  Dr. Forkel




                                                                                         Fa
