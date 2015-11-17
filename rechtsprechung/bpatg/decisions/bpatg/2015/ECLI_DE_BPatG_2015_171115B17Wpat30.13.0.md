---
ecli: "ECLI:DE:BPatG:2015:171115B17Wpat30.13.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 30/13"
decided: "2015-11-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=49&nr=27806&anz=851&pos=737&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-11-17_17_W-pat_30_13_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 30/13 vom 2015-11-17

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 30/13                                                Verkündet am
_______________                                               17. November 2015
    (Aktenzeichen)                                                   …




                              BESCHLUSS

                            In der Beschwerdesache


              betreffend die Patentanmeldung 10 2010 028 364.9


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 17. November 2015 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, des Richters
Dipl.-Phys. Dr. Forkel und des Richters Dipl.-Ing. Hoffmann




BPatG 154
05.11

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung, welche die Priorität einer Voranmeldung in den
USA vom 29. April 2009 in Anspruch nimmt, wurde am 29. April 2010 in englischer
Sprache beim Deutschen Patent- und Markenamt eingereicht. Sie trägt in der
deutschen Übersetzung die Bezeichnung


     „System, Verfahren und Computerprogrammprodukt zum Zerlegen einer
         Stichprobenentnahme-Aufgabe in eine Mehrzahl von Aufträgen“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F des
Deutschen Patent- und Markenamtes in der Anhörung vom 9. April 2013 zurückgewiesen. Zur Begründung führt die Prüfungsstelle aus, dass die jeweiligen
Gegenstände des (damaligen) Hauptanspruchs gemäß Haupt- und 1. Hilfsantrag
unter das Patentierungsverbot des § 1 PatG fielen, da die betreffenden, die parallele Verarbeitung ermöglichenden Programme für Datenverarbeitungsanlagen als
solche beansprucht würden und somit kein technisches Mittel darstellten. Darüber
hinaus falle auch der Gegenstand des Hauptanspruchs gemäß 2. Hilfsantrag unter
das Patentierungsverbot des § 1 PatG, weil er ein Programm für Datenverarbeitungsanlagen als solche betreffe, welches wiederum mathematische Methoden als
solche zum Inhalt habe. Die jeweiligen Hauptansprüche gemäß Haupt-, 1. und
2. Hilfsantrag seien daher nicht gewährbar.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.

                                       -3-



Die ordnungsgemäß geladene Anmelderin ist zur mündlichen Verhandlung - wie
angekündigt - nicht erschienen.


Sie hat mit Eingabe vom 9. August 2013 sinngemäß beantragt,


        den angefochtenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        gemäß Hauptantrag mit
        Patentansprüchen 1 bis 20 vom 09.08.2013,
        Beschreibung Seiten 1 bis 25 vom 16.03.2011 (unter Berücksichtigung der mit Eingabe vom 06.02.2012 beantragten Änderungen),
        4 Blatt Zeichnungen mit Figuren 1 bis 4 vom 29.07.2010;


        gemäß Hilfsantrag I mit
        Patentansprüchen 1 bis 17 vom 09.08.2013,
        im Übrigen wie Hauptantrag;


        gemäß Hilfsantrag II mit
        Patentansprüchen 1 bis 12 vom 09.08.2013,
        im Übrigen wie Hauptantrag;


        gemäß Hilfsantrag III mit
        Patentansprüchen 1 bis 11 vom 09.08.2013,
        im Übrigen wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt wurde auf die
Druckschrift

                                         -4-



D1: WO 2007/022439 A2


hingewiesen.


Vom Senat wurden zusätzlich die Druckschriften


D2: LINDHOLM, E.; NICKOLLS, J.; OBERMAN, S.; MONTRYM, J.: NVIDIA
Tesla: A Unified Graphics and Computing Architecture, IEEE Computer
Society, 2008


und


D3: EP 1 397 782 B1


eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


        (a)    In einem System (400), welches einen Graphikprozessor
               (406), welcher operable ist, ein Computer-erzeugtes Bild bereitzustellen,


        (b)    und eine Anzeige (408) hat, welche mit dem Graphikprozessor (406) gekoppelt ist und operable ist, das Computer-erzeugte Bild anzuzeigen,


        (c)    wobei der Graphikprozessor konfiguriert ist, die Helligkeit von
               Pixeln des Computer-erzeugten Bildes zu bestimmen,

                                        -5-



        (d)   wobei der Graphikprozessor (406) konfiguriert ist, die Operation von parallel Verarbeiten einer Stichprobenprüfungsaufgabe, die mit dem Verarbeiten einer Gruppe von Strahlen zum
              Rendern des computererzeugten Bilds assoziiert ist, durchzuführen, wobei das Verfahren zum parallel Verarbeiten einer
              Stichprobenprüfungsaufgabe aufweist:


        (e)   Identifizieren einer Stichprobenprüfungsaufgabe, die mit einer
              Gruppe von Strahlen zum Rendern eines computererzeugten
              Bilds assoziiert ist;


        (f)   Zerlegen der Stichprobenprüfungsaufgabe in eine Mehrzahl
              von Aufträgen;


        (g)   Verarbeiten jedes der Mehrzahl von Aufträgen parallel unter
              Verwendung einer parallelen Verarbeitungsarchitektur; und


        (h)   Beenden jedes der Mehrzahl von Aufträgen unabhängig von
              der anderen Mehrzahl von Aufträgen.


In Hinblick auf die nebengeordneten Patentansprüche 18 und 19 sowie die Unteransprüche 2 bis 17 und 20 gemäß Hauptantrag wird auf den Akteninhalt verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag I, hier mit einer denkbaren Gliederung
versehen, lautet:


        (a´) System (400), aufweisend: einen Graphikprozessor (406),
              welcher operable ist, ein Computer-erzeugtes Bild bereitzustellen;

                                         -6-



       (b´) und eine Anzeige (408), welche mit dem Graphikprozessor
              (406) gekoppelt ist und operable ist, das Computer-erzeugte
              Bild anzuzeigen,


       (c´) wobei der Graphikprozessor konfiguriert ist, die Helligkeit von
              Pixeln des Computer-erzeugten Bildes zu bestimmen,


       (d´) wobei der Graphikprozessor (406) konfiguriert ist, die Operation von parallel Verarbeiten einer Stichprobenprüfungsaufgabe, die mit dem Verarbeiten einer Gruppe von Strahlen zum
              Rendern des computererzeugten Bilds assoziiert ist, durchzuführen, wobei der Graphikprozessor operiert, um:


       (e´) eine Stichprobenprüfungsaufgabe zu identifizieren, die mit
              einer Gruppe von Strahlen zum Rendern des computererzeugten Bilds assoziiert ist;


       (f´)   die Stichprobenprüfungsaufgabe in eine Mehrzahl von Aufträgen zu zerlegen;


       (g´) jeden der Mehrzahl von Aufträgen parallel unter Verwendung
              einer parallelen Verarbeitungsarchitektur zu verarbeiten; und


       (h´) jeden der Mehrzahl von Aufträgen unabhängig von der anderen Mehrzahl von Aufträgen zu beenden.


In Hinblick auf die abhängigen Patentansprüche 2 bis 17 gemäß Hilfsantrag I wird
auf die Akte verwiesen.

                                              -7-



Der mit einer denkbaren Gliederung versehene Patentanspruch 1 gemäß Hilfsantrag II lautet:


         (a1) In einem System (400), welches einen Graphikprozessor
                  (406), welcher operable ist, ein Computer-erzeugtes Bild aus
                  Daten, die einem Graphikprozessor zugeführt sind, bereitzustellen,


         (b)      und eine Anzeige (408) hat, welche mit dem Graphikprozessor (406) gekoppelt ist und operable ist, das Computererzeugte Bild anzuzeigen,


         (c)      wobei der Graphikprozessor konfiguriert ist, die Helligkeit von
                  Pixeln des Computer-erzeugten Bildes zu bestimmen,


         (d)      wobei der Graphikprozessor (406) konfiguriert ist, die Operation von parallel Verarbeiten einer Stichprobenprüfungsaufgabe, die mit dem Verarbeiten einer Gruppe von Strahlen zum
                  Rendern des computererzeugten Bilds assoziiert ist, durchzuführen, wobei das Verfahren zum parallel Verarbeiten einer
                  Stichprobenprüfungsaufgabe aufweist:


         (e)      Identifizieren einer Stichprobenprüfungsaufgabe, die mit einer
                  Gruppe von Strahlen zum Rendern eines computererzeugten
                  Bilds assoziiert ist,


         (e1) wobei die Stichprobenprüfungsaufgabe mit einer (t , s) - Sequenz oder einer Rang-1-Gitter-Sequenz assoziiert ist;


         (f)      Zerlegen der Stichprobenprüfungsaufgabe in eine Mehrzahl
                  von Aufträgen,

                                       -8-



       (f1) was Zerlegen der Stichprobenprüfungsaufgabe in s - dimensionale Stichproben umfasst, wobei s eine ganze Zahl ist;


       (g)   Verarbeiten jedes der Mehrzahl von Aufträgen parallel unter
             Verwendung einer parallelen Verarbeitungsarchitektur; und


       (h)   Beenden jedes der Mehrzahl von Aufträgen unabhängig von
             der anderen Mehrzahl von Aufträgen,


       (h1) wobei die Anzahl von Stichproben ein Vielfaches von N  b m
             ist, wobei N eine Anzahl der Mehrzahl von Aufträgen ist, b
             eine Basis der (t , s) - Sequenz oder der Rang-1-Gitter-Sequenz ist, und m eine Zahl von niedrigstwertigen Bits ist, welche zum Verarbeiten der Mehrzahl von Aufträgen benützt
             werden.


Hinsichtlich der nebengeordneten Patentansprüche 10 und 11 sowie der Unteransprüche 2 bis 9 und 12 gemäß Hilfsantrag II wird auf die Akte verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag III unterscheidet sich von Patentanspruch 1 gemäß Hilfsantrag II durch das Merkmal (i), welches nach Merkmal (h1)
angefügt werden soll:


       (i)   „wobei das Zerlegen der Stichprobenprüfungsaufgabe in die
             Mehrzahl von Aufträgen das Aufteilen einer Niedrigdiskrepanz-Punktsequenz in eine Mehrzahl von Niedrigdiskrepanz-Sequenzen aufweist.“


In Hinblick auf die nebengeordneten Patentansprüche 9 und 10 sowie die Unteransprüche 2 bis 8 und 11 wird wieder auf die Akte hingewiesen.

                                       -9-



                                         II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da die jeweiligen Gegenstände des Patentanspruchs 1
gemäß Hauptantrag sowie gemäß den Hilfsanträgen I bis III nicht auf erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung bezieht sich auf ein System, ein Verfahren und ein Computerprogrammprodukt zum Zerlegen einer Stichprobenentnahme-Aufgabe     in   eine   Mehrzahl         von   Aufträgen   (Offenlegungsschrift
DE 10 2010 028 364 A9, [0001]).


Ausweislich der Anmeldung kann das Photon Mapping dadurch beschleunigt werden, dass die zum Aufbau von Photonenkarten („photon maps“) notwendigen
Rechenprozesse parallel abgearbeitet werden. Eine hierzu angewandte Technik
beruht im Wesentlichen auf zahlentheoretischen Erkenntnissen, die die Zerlegung
einer Halton-Sequenz, also einer deterministischen Punktsequenz in eine Mehrzahl von Untersequenzen vorsieht. Da alle diese Subsequenzen eine niedrige Diskrepanz bzw. eine geringe Abweichung von der Gleichverteilung haben, verbraucht jeder Rechenauftrag bzw. Job, der eine solche Subsequenz verwendet,
eine ungefähr gleich große Anzahl von Stichproben. Die Rechenaufträge können
dann ohne miteinander synchronisiert zu werden unabhängig voneinander terminieren. Eine direkte Übertragung dieses aus dem Stand der Technik bekannten
Ansatzes zur parallelen Erzeugung von Photonenkarten auf andere Punktsequenzen niedriger Diskrepanz, wie z. B. (t , s) - Sequenzen oder Rang-1-Gittersequenzen ist aber laut Beschreibung nicht möglich (Offenlegungsschrift, [0001]-[0007],
[0032]-[0034]).


Die der Anmeldung zugrundeliegende objektive technische Aufgabe sieht der
Senat darin, die Verarbeitung von Rechenaufträgen, die sich auf die Bildverarbei-

                                         - 10 -



tung oder Bildsynthese und hier insbesondere auf das Rendering beziehen, in effizienter Weise zu parallelisieren.


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren bzw. System zur
Erzeugung von Computergrafiken zu verbessern, ist ein Diplom-Informatiker oder
ein Ingenieur der Fachrichtung Elektrotechnik mit langjähriger Berufserfahrung in
der Bildverarbeitung und Bildsynthese anzusehen, der insbesondere über fundierte Kenntnisse auf dem Gebiet der der Grafik-Pipeline zugrundeliegenden Algorithmen verfügt.


2.     Die jeweiligen Gegenstände des Patentanspruchs 1 gemäß Hauptantrag
sowie Hilfsantrag I bis III beruhen nicht auf erfinderischer Tätigkeit.


2.1    Der Patentanspruch 1 bedarf der Auslegung.


Im Folgenden geht der Senat davon aus, dass mit den jeweiligen Patentansprüchen 1 gemäß Hauptantrag sowie Hilfsantrag II und III ein Verfahren zum parallelen Verarbeiten einer Stichprobenprüfungsaufgabe beansprucht werden soll, während der Patentanspruch 1 gemäß Hilfsantrag I auf ein System bzw. eine Systemanordnung gerichtet sein soll.


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hilfsantrag III, der inhaltlich sämtliche Merkmale der jeweiligen Patentansprüche 1
gemäß Hauptantrag sowie Hilfsantrag I und II mit umfasst, ein computerimplementiertes Verfahren vor, das auf einem System durchgeführt werden soll, welches über einen Grafikprozessor verfügt, der aus den ihm zugeführten (Roh-)Daten ein Bild bzw. eine Computergrafik erzeugt (Merkmal (a1)).


Das generierte Bild wird auf einer Anzeigevorrichtung, also einem Bildschirm wiedergegeben, der mit dem Grafikprozessor verbunden ist (Merkmal (b)).

                                       - 11 -



Merkmal (c) sieht die Berechnung der Helligkeit von Pixeln des erzeugten Bildes
vor. Laut Beschreibung weist der Grafikprozessor hierzu u. a. eine Mehrzahl von
Schattierermodulen und ein Rasterisierungsmodul auf (Offenlegungsschrift,
[0077]).


Laut Merkmal (d) soll der Grafikprozessor eine Stichprobenprüfungsaufgabe parallel verarbeiten, wobei „die Stichprobenprüfungsaufgabe mit dem Verarbeiten einer
Gruppe von Strahlen zum Rendern des computererzeugten Bildes assoziiert sein
soll“. In Absatz [0009] der Beschreibung wird hierzu ausgeführt, dass es sich bei
einer Stichprobenentnahmeaufgabe um eine beliebige Aufgabe handeln könne,
die in eine Mehrzahl von anderen Aufgaben oder Aufträge zerlegt werden könne.
Der Fachmann wird eine solche Stichprobenentnahmeaufgabe mit der im Patentanspruch genannten Stichprobenprüfungsaufgabe gleichsetzen, in der an den
ausgewählten Punkten einer Punktsequenz die Photonenereignisse, die zur Lichtverteilung im Raum beitragen, ausgewertet und in einer Datenstruktur (einer „photon map“) gespeichert werden. Aus fachmännischer Sicht betrifft Merkmal (d)
damit den Vorgang einer Rasterung bzw. eines Renderings, bei dem jeder Punkt
eines 3D-Objekts in ein Pixel umgewandelt wird. So ist mit dem Assoziieren der
„Stichprobenprüfungsaufgabe mit dem Verarbeiten einer Gruppe von Strahlen
zum Rendern“ ein Photon Mapping bzw. die Anwendung eines Raytracing Algorithmus gemeint (z. B. ein Monte-Carlo-Raytracing), mit dem die Strahldichte an
einem Punkt x und damit auch die Helligkeit des gerenderten Pixels mit Hilfe
einer Rendergleichung berechnet wird.


Nachdem die Stichprobenprüfungsaufgabe bzw. -entnahmeaufgabe identifiziert
ist, wird sie in eine Mehrzahl von (Rechen-)Aufträgen zerlegt (Offenlegungsschrift,
[0010] - Merkmale (e), (f)). Die Stichprobenprüfungsaufgabe soll mit einer (t , s) -
Sequenz oder einer Rang-1-Gitter-Sequenz, also Punktsequenzen niedriger Diskrepanz, verknüpft sein (Merkmal (e1)). Weiterhin soll die Zerlegung der Stichprobenprüfungsaufgabe in s -dimensionale Stichproben erfolgen, wobei die ganze
Zahl s die Dimension der Punkte innerhalb der Sequenz angibt (Merkmal (f1)).

                                       - 12 -



Merkmal (g) gibt an, dass die Mehrzahl von (Rechen-)Aufträgen unter Verwendung einer parallelen Verarbeitungsarchitektur parallel abgearbeitet werden sollen.
Laut Beschreibung weist eine solche Architektur mehrere Prozessoren auf, die
eine Vielzahl von Threads parallel ausführen (Offenlegungsschrift, [0020]).


Jeder Rechenauftrag kann unabhängig von den anderen Rechenaufträgen beendet werden (Merkmal (h)). Der Grund hierfür liegt in der Anwendung von Quasi-Monte-Carlo-Verfahren, was eine adaptive parallele Verarbeitung ohne Synchronisation ermöglicht (Offenlegungsschrift, [0031]).


Merkmal (h1) legt fest, dass die Anzahl der Stichproben ein Vielfaches der Anzahl
von (Rechen-)Aufträgen N  b m sein soll; b stellt hierbei eine Basis der verwendeten (t , s) - Sequenz oder Rang-1-Gittersequenz dar, während m die Zahl der niedrigstwertigen Bits, also derjenigen Bits mit dem niedrigsten Stellenwert angibt, die
zur Verarbeitung der Rechenaufträge verwendet werden.


Wird die Stichprobenprüfungsaufgabe in mehrere (Rechen-)Aufträge zerlegt, so ist
dies mit der Aufteilung einer Punktsequenz niedriger Diskrepanz in eine Mehrzahl
von (Unter-)Sequenzen niedriger Diskrepanz verknüpft (Merkmal (i)).


Die jeweiligen Patentansprüche 1 gemäß Hauptantrag sowie Hilfsanträgen I und II
gehen inhaltlich nicht über den Patentanspruch 1 gemäß Hilfsantrag III hinaus.


2.2   Zur Beurteilung der beanspruchten Lehre sind die Druckschriften D2 und
D3 von besonderer Bedeutung.


Bei der Druckschrift D2 handelt es sich um einen Fachartikel über die Beschleunigung von Aufgaben der parallelen Bildverarbeitung durch Benutzung von NVIDIA-Grafikkarten. Die Druckschrift beschreibt die Hardware-Architektur der Grafikkarten, die sogenannte Tesla-Architektur, sowie CUDA („Compute Unified Device
Architecture“), eine Programmiertechnik, mit der Programmteile durch einen Gra-

                                       - 13 -



fikprozessor (GPU) abgearbeitet werden können (Seite 39, Abstract; Seite 39,
linke Spalte).


Sie offenbart damit ein Verfahren zum parallelen Abarbeiten von Rechenaufträgen
bzw. Tasks (Seite 39, Abstract; Seite 41, Figur 1), wobei ein Grafikprozessor aus
ihm zugeführten Rohdaten ein Bild erzeugt (Seite 39, linke Spalte, zweiter Absatz;
Seite 49, rechte Spalte, Abschnitt „Parallel computing architecture“). Bei dem Grafikprozessor handelt es sich um eine GeForce 8800 GPU mit Tesla-Architektur
(Seite 40, rechte Spalte, Abschnitt „Tesla architecture“; Figur 1 – Merkmale (a),
(a´), (a1)).


Die aus der Druckschrift D2 bekannte GPU mit Tesla-Architektur ist mittlerweile in
Laptops, Desktops und Workstations enthalten, d. i. in Systemen, die über Displays bzw. Anzeigen verfügen, auf denen die gerenderten Bilder wiedergegeben
werden können (Seite 49, rechte Spalte, letzter Absatz - Seite 50, linke Spalte,
erster Absatz - Merkmale (b), (b´)).


Auf dem Graphikprozessor der Druckschrift D2 werden u. a. Vertex-Shader, Geometrie-Shader und Pixel-Fragment-Shader Programme ausgeführt (Seite 43, linke
Spalte, Abschnitt „Streaming multiprocessor“). Für den Fachmann ist in diesem
Zusammenhang selbstverständlich, dass die genannten Programme u. a. für die
durch Lichtquellen hervorgerufene Beleuchtung im Bild, aber auch für die Berechnung von Farbe, Transparenz, Reflektivität oder Struktur jedes einzelnen Pixels
zuständig sind und damit auch die Helligkeit des Pixels bestimmen (Merkmale (c),
(c´)).


Der Grafikprozessor unterstützt die Parallelisierbarkeit von Programmen auf der
Grafikkarte. Um dies zu ermöglichen implementiert die Tesla-Architektur ein Konzept der kooperierenden Arrays von Threads (Cooperating Thread Arrays, CTA).
CTAs werden parallel und unabhängig voneinander abgearbeitet (Seite 50, rechte
Spalte, Abschnitt „Cooperative thread array or thread block“; Seite 51, linke

                                        - 14 -



Spalte, Abschnitt „CTA grids“). Ein CTA besteht aus einer Menge von Threads, die
dasselbe Programm berechnen und miteinander kooperieren können. Das Streaming Prozessor Array der Tesla-Architektur führt Grafik-Shader-Thread Programme aus, um Bilder zu rendern (Seite 42, linke Spalte - teilweise Merkmal (d),
(d´)). Das „Verarbeiten einer Stichprobenprüfungsaufgabe, die mit dem Verarbeiten einer Gruppe von Strahlen“ verbunden sein soll, d. h. eine Verarbeitung von
Rechenaufträgen für ein Photon Mapping oder Ray Tracing unter Anwendung von
Punktmengen, geht aus der Druckschrift D2 allerdings nicht hervor (restlicher Teil
von Merkmal (d) bzw. (d´)).


Entsprechend dem CTA-Konzept der Druckschrift D2 werden Rechenaufträge
parallel und unabhängig voneinander auf den Streaming Prozessoren ausgeführt
(Seite 50, rechte Spalte, zweiter Absatz; Seite 51, linke Spalte, Abschnitt „CTA
grids“). Die Unabhängigkeit der Verarbeitung der Rechenaufträge bedeutet aber
auch, dass jeder Auftrag unabhängig von den anderen Aufträgen terminieren
kann. Die Merkmale (g), (g´) und (h), (h´) sind demnach in der Tesla Architektur
verwirklicht.


Die Druckschrift D3 befasst sich mit einem Verfahren zum Rendern von Bildern
auf der Grundlage von deterministischen Punktsequenzen niedriger Diskrepanz.
Anhand einer Auswahl endlicher Punktmengen aus den erzeugten Sequenzen,
d. h. anhand von Stichproben, werden Rechenaufträge zur Lösung von Integralgleichungen für Pixelwerte abgearbeitet ([0018], [0019]). Dabei werden Lösungsansätze aus der Strahlenoptik, wie etwa das Photon Mapping angewendet, die
das Aussenden und Speichern von Lichtpartikeln ([0028], [0029], [0032]) sowie die
für die gerenderten Pixel aus Sicht des Fachmannes selbstverständliche Berechnung von Strahldichten umfassen ([0032], siehe „Keller application“; [0012]). Das
in Merkmal (d) bzw. (d´) angegebene Teilmerkmal eines parallel Verarbeitens
einer „Stichprobenprüfungsaufgabe, die mit dem Verarbeiten einer Gruppe von
Strahlen zum Rendern des computererzeugten Bilds assoziiert ist“, ist demnach in
der Druckschrift D3 verwirklicht (restlicher Teil von Merkmal (d) bzw. (d´)).

                                        - 15 -



Im bekannten Verfahren der Druckschrift D3 wird eine Auswahl von Punktmengen
aus einer „grobkörnigen“ Halton-Sequenz getroffen ([0025], Gleichungen (13),
(14)). Eine solche Auswahl bzw. Stichprobe wird konkret im Code Segment 1
([0028], Gleichungen (13a), (13b)) formuliert und daher auch bei Ablaufen des
betreffenden Programms „erkannt“. Das in Absatz [0028] gezeigte Code Segment
dient der Bestimmung und Speicherung von Photonenereignissen, die für Rendering Operationen benötigt werden ([0029] - Merkmal (e), (e´)).


Die auf der „grobkörnigen“ Halton-Sequenz basierende Stichprobe der Druckschrift D3 wird in eine Mehrzahl von Rechenaufträgen zerlegt ([0029] - Merkmal (f), (f´)), wobei jeder Rechenauftrag einer mehrdimensionalen Subsequenz
zugeordnet wird ([0027] - Merkmal (f1)).


In der Druckschrift D3 wird ausgeführt, dass die Rechenaufträge für das Photon
Mapping bzw. das Aussenden der Lichtpartikel („photons emission“) parallel abgearbeitet werden können ([0027], [0029]), und zwar auf einem Multiprozessorsystem, wie es in Absatz [0022] erläutert wird („processor module“ - Merkmale (g),
(g´)).


Gerade weil die den einzelnen Rechenaufträgen zugrundeliegenden Subsequenzen (beschrieben durch Index i ) deterministisch und von niedriger Diskrepanz
sind, können die Aufträge bzw. Jobs nicht nur parallel, sondern auch unabhängig
voneinander auf verschiedene Prozessoren verteilt und ohne Synchronisation ausgeführt werden, so dass die Jobs insbesondere unabhängig voneinander enden
können ([0029] - Merkmale (h), (h´)).


In Druckschrift D3 ist die Anzahl der Rechenaufträge bzw. Jobs durch die Größe
M _ act gegeben (Jobindex i läuft von 0 bis M _ act  1 ; [0028]), wobei M _ act
gemäß Absatz [0030] durch die Anwendung von Primzahlen berechnet wird. Für
den Fachmann ist selbstverständlich, dass die Anzahl von Stichproben deutlich
größer als die Anzahl der auf den Prozessoren parallel abzuarbeitenden Rechen-

                                       - 16 -



aufträge gewählt werden muss, um repräsentative Punktmengen für die Subsequenzen zu erhalten (teilweise Merkmal (h1)). Der in Merkmal (h1) angegebene
Zusammenhang zwischen Auftragsanzahl, Basis der Sequenz und Zahl von niedrigstwertigen Bits geht aus der Druckschrift D3 aber nicht hervor.


Weiterhin lehrt die Druckschrift D3, dass zur Berechnung von Strahldichten
([0021]) die Verteilung der Rechenaufträge auf mehrere Prozessoren mit der Zerlegung einer Punktsequenz niedriger Diskrepanz (hier einer „grobkörnigen“
Halton-Sequenz) in mehrere Subsequenzen niedriger Diskrepanz (jeweils gekennzeichnet durch einen Jobindex i , [0027]) einhergeht. Merkmal (i) ist demnach im
Verfahren der Druckschrift D3 verwirklicht.


2.3   Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
die mit dem jeweiligen Patentanspruch 1 gemäß Hauptantrag und Hilfsantrag I bis
III beanspruchten Gegenstände mit all ihren Merkmalen für den Fachmann nahegelegen haben. Dies gilt selbst dann, wenn der Prüfung der gesamte Patentanspruch mit allen seinen Merkmalen zugrunde gelegt wird. Damit kann dahingestellt
bleiben, ob die beanspruchten Gegenstände gemäß § 1 Abs. 3 i. V. m. Abs. 4
PatG vom Patentschutz ausgeschlossen sind, und ob der jeweilige Patentanspruch 1 Merkmale enthält, die nicht die Lösung eines technischen Problems mit
technischen Mitteln bestimmen oder beeinflussen und somit bei der Prüfung der
erfinderischen Tätigkeit nicht zu berücksichtigen sind (BGH GRUR 2011, 125
- Wiedergabe topografischer Informationen).


Zu den routinemäßigen Aufgaben, die sich dem Fachmann stellen, der sich insbesondere mit Problemen bei der Bildsynthese befasst, gehört es, die Performance
der zugrundeliegenden Rechenverfahren und Programmsysteme, wie den aus der
Druckschrift D2 entnehmbaren CUDA C Programmen, ständig zu verbessern. Für
den Fachmann lag es daher nahe, sich zu diesem Zweck überall dort nach Anregungen umzusehen, wo effektive Algorithmen zur Bildsynthese zum Einsatz kommen. Hierbei konnte der Fachmann auf die Druckschrift D3 stoßen, welche lehrt,

                                          - 17 -



Rechenaufträge für ein Photon Mapping in einem Multiprozessorsystem zu parallelisieren und zu diesem Zweck Punktsequenzen niedriger Diskrepanz in geeignete Subsequenzen aufzuteilen. Angesichts des in der Druckschrift D2 gegebenen
Hinweises, die unterschiedliche Last verschiedener Programme dadurch dynamisch zu verteilen, dass der Streaming Multiprozessor gleichzeitig unterschiedliche Thread Programme und verschiedene Typen von Shadern ausführt (Seite 43,
rechte Spalte, Abschnitt „SM multithreading“) bot es sich für den Fachmann an,
das aus der Druckschrift D2 bekannte Verfahren um das auf deterministischen
Punktsequenzen basierende Verfahren zum Rendern von Bildern nach dem Vorbild der Druckschrift D3 zu erweitern.


Von einer solchen kombinierten Lehre unterscheidet sich die Lehre nach dem
Patentanspruch 1 gemäß Hilfsantrag III im Wesentlichen nur noch dadurch, dass
die Stichprobenprüfungsaufgabe mit einer (t , s) - Sequenz oder einer Rang-1-Gitter-Sequenz (anstelle einer Halton-Sequenz) assoziiert ist (Merkmal (e1)) und dass die
Anzahl der (parallelisierten) Rechenaufträge N  b m ist, wobei b eine Basis der
(t , s) - Sequenz oder der Rang-1-Gitter-Sequenz ist, und m eine Zahl von niedrigstwertigen Bits ist, welche zum Verarbeiten der Mehrzahl von Aufträgen benützt werden (restlicher Teil von Merkmal (h1)).


Da der Fachmann stets bestrebt ist, die Konvergenz der implementierten Algorithmen zu verbessern, bot es sich für ihn an, auf digitale Punktsequenzen niedriger
Diskrepanz, d. h. Punktsequenzen zur Basis 2 zurückzugreifen, wie die in Quasi-Monte-Carlo-Rechnungen häufig angewandte Sobol-Sequenz (d. i. eine (t , s) -
Sequenz zur Basis 2 ). Dem Fachmann ist geläufig, dass solche Sequenzen durch
binäre Operationen auf binären Zahlenentwicklungen konstruiert werden können
und sich deshalb für eine Implementierung in computergestützten Rechenverfahren
in besonderer Weise anbieten, wohingegen sich die aus der Druckschrift D3 bekannte Halton-Sequenz auf jeweils unterschiedliche Primzahlenbasen für jede
Raumrichtung stützt (vgl. D3 Seite 6, Gleichungen (9) und (10)). Dass die Anwen-

                                      - 18 -



dung einer Sobol-Sequenz in Verbindung mit den Schichtungseigenschaften
deterministischer Punktsequenzen bereits vor dem Prioritätszeitpunkt der Patentanmeldung bekannt war, wird u. a. in der Druckschrift D1 gezeigt (Seite 46, Zeilen 5-14, siehe insbesondere „the convergence can be improved by using the
microstructure …“ - Merkmal (e1)).


Das verbleibende Unterschiedsmerkmal gegenüber dem Stand der Technik, d. i.
die Festlegung der Anzahl der Rechenaufträge auf N  b m , wobei b die Basis der
Punktsequenz darstellen soll und die ganze Zahl m die gemäß dem „least significant bit“ LSB0 nummerierten Bits angibt, die zur Verarbeitung der Rechenaufträge
benutzt werden, beruht allenfalls auf fachgemäßen Überlegungen aus der Zahlentheorie. So sind dem Fachmann die Schichtungseigenschaften digitaler Punktsequenzen durchaus geläufig (siehe oben), die letztlich festlegen, welche und vor
allem wie viele Subsequenzen niedriger Diskrepanz aus einer vorgegebenen
deterministischen Punktsequenz niedriger Diskrepanz überhaupt gebildet werden
können. Insbesondere ist ihm bekannt, dass aus einer Wahl von 2 m Punkten in
einer Raumrichtung immer genauso viel Subsequenzen (abhängig von den jeweils
anderen Raumrichtungen) resultieren, welche als Rechenaufträge unabhängig
voneinander verarbeitet werden können. Die Verwendung der LSB0 Bitnummerierung stellt in diesem Zusammenhang ein elementares zahlentheoretisches Mittel
zur Festlegung der Bitwertigkeit für die zu verarbeitenden Binärzahlen dar und
kann für sich gesehen eine erfinderische Tätigkeit nicht begründen (restlicher Teil
von Merkmal (h1)).


Nach allem waren für den Fachmann lediglich fachgemäße Überlegungen erforderlich, um in Kenntnis der Druckschriften D2 und D3 zu einem Verfahren mit
sämtlichen Merkmalen des Patentanspruchs 1 in der Fassung des Hilfsantrag III
zu gelangen.

                                              - 19 -



Hauptantrag sowie Hilfsantrag I und II können nicht günstiger beurteilt werden, da
ihre jeweiligen Patentansprüche 1 inhaltlich nicht über den Patentanspruch 1
gemäß Hilfsantrag III hinausgehen und die jeweils beanspruchten Gegenstände
damit nicht auf erfinderischer Tätigkeit beruhen.


3.      Mit den jeweiligen Patentansprüchen 1 gemäß Hauptantrag sowie Hilfsanträgen I bis III fallen auch die jeweiligen übrigen Patentansprüche, da über einen
Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120 - Elektrisches Speicherheizgerät).




                                               III.


Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde der
Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamtes zurückzuweisen.




                                   Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
        kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
        nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,

                                            - 20 -



   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek                    Eder                   Dr. Forkel                 Hoffmann




                                                                                          Fa
