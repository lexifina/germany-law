---
ecli: "ECLI:DE:BPatG:2021:150621B17Wpat20.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 20/20"
decided: "2021-06-15"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=19&nr=42105&anz=599&pos=286&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2021-06-15_17_W-pat_20_20_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 17 W (pat) 20/20 vom 2021-06-15

## Entscheidung

BUNDESPATENTGERICHT


    17 W (pat) 20/20                                                 Verkündet am
 _______________________
                                                                     15. Juni 2021
     (Aktenzeichen)




                                  BESCHLUSS

                                In der Beschwerdesache


                betreffend die Patentanmeldung 10 2014 119 048.3
…
hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 15. Juni 2021 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Merzbach, des Richters Dipl.-Phys.
Dr. Forkel und des Richters Dipl.-Phys. Dr. Städele


beschlossen:


                           Die Beschwerde wird zurückgewiesen.




                                       Gründe


                                           I.




ECLI:DE:BPatG:2021:150621B17Wpat20.20.0

                                        -2-



Die vorliegende Patentanmeldung wurde am 18. Dezember 2014 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


 „ Ausführung von Verarbeitungsvorgängen in einer SIMD-Verarbeitungseinheit “.


Die Patentanmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F
des Deutschen Patent- und Markenamts vom 20. Januar 2020 aus Gründen des
Bescheids vom 24. September 2019 zurückgewiesen. In dem in Bezug
genommenen Bescheid ist sinngemäß ausgeführt, mangels einer ausreichenden
Definition des unter Schutz zu stellenden Gegenstands erfülle der (damalige)
Patentanspruch 1 nicht die Anforderungen nach §34 Abs. 3 Nr. 3 PatG und sei aus
diesem Grund nicht gewährbar. Selbst wenn dieser Mangel keine Berücksichtigung
fände, sei der Gegenstand des Patentanspruchs 1 mit Rücksicht auf den der
Druckschrift D1 entnehmbaren Stand der Technik nicht neu und beruhe gegenüber
der Druckschrift D2 nicht auf einer erfinderischen Tätigkeit.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin beantragt,


      den Beschluss der Prüfungsstelle für Klasse G06F vom 20. Januar 2020
      aufzuheben und das nachgesuchte Patent auf der Grundlage folgender
      Unterlagen zu erteilen:


             durch die Merkmale der Patentansprüche 1 bis 20 vom 23. Dezember
             2020 gemäß Hauptantrag,

             Beschreibung und Zeichnungen wie Offenlegungsschrift,

             hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 18 vom 23.
             Dezember 2020 gemäß Hilfsantrag 1,

                                      -3-



             Beschreibung und Zeichnungen wie Offenlegungsschrift,


             weiter hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 17 vom 23. Dezember
             2020 gemäß Hilfsantrag 2,
             Beschreibung und Zeichnungen wie Offenlegungsschrift,


             weiter hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 16 vom 23. Dezember
             2020 gemäß Hilfsantrag 3,
             Beschreibung und Zeichnungen wie Offenlegungsschrift,


             weiter hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 14 vom 23. Dezember
             2020 gemäß Hilfsantrag 4,
             Beschreibung und Zeichnungen wie Offenlegungsschrift,


             weiter hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 12 vom 23. Dezember
             2020 gemäß Hilfsantrag 5,
             Beschreibung und Zeichnungen wie Offenlegungsschrift,


             weiter hilfsweise
             durch die Merkmale der Patentansprüche 1 bis 10 gemäß Hilfsantrag
             6, überreicht in der mündlichen Verhandlung,
             Beschreibung und Zeichnungen wie Offenlegungsschrift.


Der geltende Patentanspruch 1 gemäß Hauptantrag, mit einer möglichen
Gliederung versehen, lautet:

                                -4-



M1    SIMD(Single Instruction Multiple Data)-Verarbeitungseinheit, die
      ausgelegt ist,

M2    eine Mehrzahl von Verarbeitungsvorgängen zu verarbeiten,

M2a die jeweils Arbeitselemente bis zu einer vorbestimmten Höchstanzahl
      umfassen,

M3    wobei die Arbeitselemente eines Verarbeitungsvorgangs ausgelegt
      sind, eine gemeinsame Sequenz von Befehlen an entsprechenden
      Datenelementen auszuführen, wobei

M4    die Datenelemente in Blöcken von Datenelementen angeordnet sind,
      wobei

M5    Blöcke von Arbeitselementen in einem Verarbeitungsvorgang sich auf
      jeweilige Blöcke von Datenelementen beziehen, wobei,

M6    falls eines oder mehrere der Datenelemente in einem Block von
      Datenelementen verarbeitet werden sollen, dann alle Datenelemente
      in diesem Block von Datenelementen zur Verarbeitung durch die
      SIMD-Verarbeitungseinheit eingeplant werden, und wobei

M7    einige der Blöcke wenigstens ein ungültiges Arbeitselement umfassen,

M8    wobei die SIMD-Verarbeitungseinheit umfasst:

      eine Gruppe von Verarbeitungsbahnen, die ausgelegt sind, Befehle
      von Arbeitselementen eines bestimmten Verarbeitungsvorgangs über
      eine Mehrzahl von Verarbeitungszyklen auszuführen,

M9    wobei jede der Verarbeitungsbahnen der Gruppe ausgelegt ist,
      Befehle eines jeweiligen Blocks von Arbeitselementen über eine
      Mehrzahl         von   aufeinanderfolgenden    Verarbeitungszyklen
      auszuführen; und

                                       -5-



      M10‘ ein Steuermodul, das ausgelegt ist, basierend auf der Gültigkeit der
              Arbeitselemente die Arbeitselemente zu den Verarbeitungsvorgängen
              zusammenzustellen,

              sodass      ungültige     Arbeitselemente      des      bestimmten
              Verarbeitungsvorgangs über die Gruppe von Verarbeitungsbahnen
              hinweg vorübergehend in Linie gebracht sind.


Patentanspruch 1 nach Hilfsantrag 1 beruht auf Patentanspruch 1 nach
Hauptantrag, wobei sich an Merkmal M10‘ das Merkmal

      M12 ferner umfassend Logik, die mit der Gruppe von Verarbeitungsbahnen
              gekoppelt ist, die ausgelegt ist, die Gruppe von Verarbeitungsbahnen
              zu veranlassen, die Ausführung einer Gruppe von ungültigen
              Arbeitselementen zu überspringen, falls die Gruppe von ungültigen
              Arbeitselementen die einzigen Arbeitselemente sind, die für die
              Ausführung in der Gruppe von Verarbeitungsbahnen in einem
              Verarbeitungszyklus geplant sind.

anschließt.


Patentanspruch 1 nach Hilfsantrag 2 unterscheidet sich von Patentanspruch 1
nach Hilfsantrag 1 dadurch, dass Merkmal M10‘ durch Merkmal

      M10 ein Steuermodul, das ausgelegt ist, basierend auf der Gültigkeit der
              Arbeitselemente die Arbeitselemente zu den Verarbeitungsvorgängen
              zusammenzustellen,

              wobei Arbeitselemente in einem Block von Arbeitselementen
              umgeordnet werden, um dadurch die ungültigen Arbeitselemente aus
              verschiedenen Blöcken von Arbeitselementen innerhalb eines
              Verarbeitungsvorgangs über die Gruppe von Verarbeitungsbahnen
              hinweg vorübergehend in Linie zu bringen,

                                        -6-



ersetzt ist.


Patentanspruch 1 nach Hilfsantrag 3 geht aus Patentanspruch 1 nach Hilfsantrag
2 hervor, indem zwischen den Merkmalen M10 und M12 das Merkmal

         M11 wobei das Steuermodul ausgelegt ist, Arbeitselemente in einem Block
               von Arbeitselementen umzuordnen, indem wenigstens eines von
               einem    Rotationsvorgang      und   einem   Tauschvorgang     der
               Arbeitselemente im Block von Arbeitselementen durchgeführt wird,

eingefügt wird.


Bei Patentanspruch 1 nach Hilfsantrag 4 wird gegenüber Patentanspruch 1 nach
Hilfsantrag 3 nach Merkmal M12 noch Merkmal

         M13 wobei das Steuermodul ferner ausgelegt ist, einen entsprechenden
               Indikator für eine Mehrzahl der Blöcke von Arbeitselementen zu
               setzen, um die Reihenfolge der Arbeitselemente innerhalb der
               Mehrzahl von Blöcken von Arbeitselementen anzuzeigen.

angehängt.


Patentanspruch 1 nach Hilfsantrag 5 beruht auf Patentanspruch 1 nach
Hilfsantrag 4, wobei auf Merkmal M13 noch Merkmal




         M14 wobei die Datenelemente Pixelwerte sind und wobei die Blöcke von
               Datenelementen Pixelquads sind.

folgt.


Schließlich unterscheidet sich Patentanspruch 1 nach Hilfsantrag 6 von
Patentanspruch 1 nach Hilfsantrag 5 darin, dass nach Merkmal M14 noch Merkmal

                                         -7-



       M15 und wobei Befehle eines jeweiligen Blocks von Arbeitselementen, die
               sich auf einen jeweiligen Pixelquad beziehen, eingeplant sind, in einer
               jeweiligen Verarbeitungsbahn ausgeführt zu werden.

ergänzt ist.


Zu den nebengeordneten Patentansprüchen sowie zu den Unteransprüchen wird
auf die Akte verwiesen.


Im Prüfungsverfahren vor dem deutschen Patent- und Markenamt sind u.a. die
Druckschriften


G9     Giesen, Fabian: A trip through the Graphics Pipeline 2011, part 8,
       10.07.2011. URL: https://fgiesen.wordpress.com/2011/07/10/a-trip-throughthe-graphics-pipeline-2011-part-8/, [abgerufen am 10.09.2019]


und


D2     Rhu, Minsoo; Erez, Mattan: Maximizing SIMD Resource Utilization in
       GPGPUs with SIMD Lane Permutation. In: SIGARCH Comput. Archit. News,
       Volume 41, June 2013, Issue 3, S. 356-367. - ISSN 0163-5964.
       http://doi.acm.org/10.1145/2508148.2485953, [abgerufen am 18.04.2016]


genannt worden.



                                          II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da der Gegenstand des jeweiligen Patentanspruchs 1 nach

                                         -8-



Hauptantrag sowie nach den Hilfsanträgen 1 bis 6 nicht auf einer erfinderischen
Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung betrifft die Datenverarbeitung in SIMD-Verarbeitungseinheiten („SIMD“ = „single instruction multiple data“).


Der Beschreibungseinleitung der Anmeldung ist zu entnehmen, dass SIMD-Verarbeitungseinheiten Datenelemente parallel verarbeiten können und daher
besonders nützlich sind, wenn derselbe Befehl an einer großen Anzahl von
Datenelementen        auszuführen        ist.   Beispielsweise      könne         eine
Grafikverarbeitungseinheit (GPU) eine SIMD-Verarbeitungseinheit verwenden, um
Verarbeitungsvorgänge      an    einer    großen    Anzahl    von       Pixeln   eines
computergenerierten Bilds durchzuführen (Offenlegungsschrift, Absatz [0001]).


Ein Verarbeitungsvorgang könne aus einer Mehrzahl von Arbeitselementen
bestehen, bei deren Ausführung eine gemeinsame Sequenz von Befehlen an
entsprechenden      Datenelementen         ausgeführt    werde.     Eine         SIMD-Verarbeitungseinheit könne Verarbeitungsbahnen umfassen, die jeweils ausgelegt
sind, einen Befehl eines Arbeitselements in mehreren Verarbeitungszyklen
auszuführen (Offenlegungsschrift, Absätze [0002], [0003] sowie Figuren 1 und 2;
der in Figur 1 dargestellte Verarbeitungsvorgang 100 mit 32 Arbeitselementen wird
gemäß Figur 2 auf 16 Verarbeitungsbahnen in zwei Verarbeitungszyklen
ausgeführt). Falls ein Verarbeitungsvorgang nur teilweise belegt sei oder ungültige
Arbeitselemente umfasse, blieben einige „Verarbeitungsschlitze“ - d.h. Zeitfenster,
in denen jeweils ein Befehl in einer bestimmten Verarbeitungsbahn abgearbeitet
werden kann - ungenutzt (vgl. Offenlegungsschrift, Absätze [0003], [0004]).


Moderne Grafikschnittstellen zur Anwendungsprogrammierung wie OpenGL und
DirectX definierten Befehle, die mit Pixeln in einem 2x2-Pixelquad arbeiten. Es sei
z.B. häufig erforderlich, die Änderungsrate einer variierenden Menge von
verschiedenen Pixeln mittels eines „Gradienten“-Vorgangs zu bestimmen. Die

                                               -9-



Befehle        der     Grafikschnittstellen    ließen    die   Entfernung     von   „leeren“
Pixelverarbeitungsschlitzen (die ungültigen Arbeitselementen entsprechen) nicht
zu, wenn Arbeitselemente in Verarbeitungsvorgängen verpackt werden (vgl.
Offenlegungsschrift, Absatz [0005]).


Eine Aufgabe wird in der vorliegenden Patentanmeldung nicht ausdrücklich
genannt. Jedoch lässt Absatz [0025] der Offenlegungsschrift aus Sicht des Senats
auf      die     Aufgabenstellung        schließen,     eine      SIMD-Verarbeitungseinheit
bereitzustellen, die ausgelegt ist, die Anzahl ungenutzter Verarbeitungsschlitze
aufgrund ungültiger Arbeitselemente in Verarbeitungsvorgängen zu verringern.


Als Fachmann, der mit der Lösung dieser Aufgabe betraut wird, ist ein Informatiker
oder Ingenieur der Fachrichtung Elektrotechnik mit mehrjähriger Erfahrung in der
Entwicklung          paralleler   Datenverarbeitungsarchitekturen      -   insbesondere   für
Grafikanwendungen - anzusehen.


2.       Zur Lehre von Patentanspruch 1


Patentanspruch 1 nach Hilfsantrag 6, der inhaltlich sämtliche Merkmale des
jeweiligen Patentanspruchs 1 gemäß Hauptantrag und Hilfsantrag 1 bis 5 enthält,
sieht eine SIMD-Verarbeitungseinheit vor (Merkmal M1), d.h. eine Recheneinheit,
die es gestattet, denselben Befehl gleichzeitig auf mehrere unterschiedliche Daten
anzuwenden (Offenlegungsschrift, Absatz [0001]).


Die      SIMD-Verarbeitungseinheit            ist    ausgelegt,     eine    Mehrzahl      von
Verarbeitungsvorgängen zu verarbeiten, die jeweils Arbeitselemente bis zu einer
vorbestimmten Höchstanzahl umfassen (Merkmale M2, M2a). Ein Arbeitselement
kann einen Teilvorgang eines Verarbeitungsvorgangs und insbesondere eine
Sequenz von Befehlen umfassen (vgl. Offenlegungsschrift, Absatz [0002], erster
Satz).

                                       - 10 -



Die Arbeitselemente eines Verarbeitungsvorgangs sollen ausgelegt sein, eine
„gemeinsame“ Sequenz von Befehlen an entsprechenden Datenelementen
auszuführen (Merkmal M3). Dies soll bedeuten, dass eine Gruppe von
Arbeitselementen des Verarbeitungsvorgangs dieselbe Sequenz von Befehlen
umfasst,   die   auf   entsprechende   Datenelemente     anzuwenden      sind   (vgl.
Offenlegungsschrift, Absatz [0002]).


Gemäß den Merkmalen M4 und M14 sind die Datenelemente Pixelwerte, die in
Pixelquads angeordnet sind, d.h. in quadratischen 2x2-Pixelblöcken (vgl.
Offenlegungsschrift, Absatz [0035], [0057], [0067]; Figur 4 i. V. m. Absatz [0028]).
Aus Sicht des Fachmanns umfasst der Sinngehalt des Begriffs „Pixelquad“
allerdings nicht nur 2x2-Pixelblöcke, sondern auch größere Blöcke (z.B. 4x4-
Pixelblöcke).


Ferner sollen sich Blöcke von Arbeitselementen in einem Verarbeitungsvorgang auf
jeweilige Pixelquads beziehen (Merkmale M5 und M14). Ein Block von
Arbeitselementen stellt eine zusammenhängende Menge von Arbeitselementen
dar, die in einer oder mehreren Dimensionen angeordnet sind (vgl. etwa die Figuren
1 und 2 der Offenlegungsschrift). Aus Sicht des Fachmanns liegt ein Bezug
zwischen Blöcken von Arbeitselementen und jeweiligen Pixelquads im Sinne von
Merkmal M5 bereits dann vor, wenn Blöcke von Arbeitselementen des
Verarbeitungsvorgangs Pixelwerte einer Menge von Pixelquads verarbeiten.

Gemäß den Merkmalen M6 und M14 werden alle Pixelwerte in einem Pixelquad zur
Verarbeitung durch die SIMD-Verarbeitungseinheit eingeplant, falls einer oder
mehrere dieser Pixelwerte verarbeitet werden sollen. Dies bedeutet, dass alle
Pixelwerte des Pixelquads zur Verarbeitung in der SIMD-Verarbeitungseinheit
vorgesehen werden, wenn zumindest an einem dieser Pixelwerte Berechnungen
durchgeführt werden sollen.

                                       - 11 -



Nach Merkmal M7 umfassen einige der Blöcke von Arbeitselementen wenigstens
ein ungültiges Arbeitselement. Der Beschreibung ist zu entnehmen, dass ein
Arbeitselement dann ungültig ist, wenn es sich auf ein ungültiges Datenelement
bzw. einen ungültigen Pixelwert bezieht (Offenlegungsschrift, Absätze [0007],
[0009]). Ein Pixelwert eines Pixelquads kann ungültig sein, wenn an dem Pixelwert
keine oder nur sehr wenige Befehle auszuführen sind (Offenlegungsschrift, Absätze
[0028], [0054]). Aus Sicht des Fachmanns stellen aber auch maskierte oder
ausgeblendete      Arbeitselemente,      deren   Ausführungsergebnisse       nicht
weiterverwendet werden, ungültige Arbeitselemente im Sinne des Merkmals M7 dar
(vgl. Offenlegungsschrift, Absatz [0061]).


Die    SIMD-Verarbeitungseinheit       umfasst   ferner    eine    Gruppe     von
Verarbeitungsbahnen, die ausgelegt sind, Befehle von Arbeitselementen eines
bestimmten Verarbeitungsvorgangs über eine Mehrzahl von Verarbeitungszyklen
auszuführen (Merkmal M8). Jede dieser Verarbeitungsbahnen ist ferner ausgelegt,
Befehle eines jeweiligen Blocks von Arbeitselementen über eine Mehrzahl von
aufeinanderfolgenden Verarbeitungszyklen auszuführen (Merkmal M9).


Gemäß Merkmal M10 soll die SIMD-Verarbeitungseinheit ein Steuermodul
umfassen, das ausgelegt ist, basierend auf der Gültigkeit der Arbeitselemente die
Arbeitselemente zu den Verarbeitungsvorgängen zusammenzustellen, wobei
Arbeitselemente in einem Block von Arbeitselementen umgeordnet werden, um
dadurch die ungültigen Arbeitselemente aus verschiedenen Blöcken von
Arbeitselementen innerhalb eines Verarbeitungsvorgangs über die Gruppe von
Verarbeitungsbahnen hinweg „vorübergehend in Linie zu bringen“.


Dies bedeutet insbesondere, dass die Arbeitselemente jeweils innerhalb der
verschiedenen Blöcke mit der Zielsetzung umsortiert werden, die ungültigen
Arbeitselemente aus verschiedenen Blöcken so zu Verarbeitungsvorgängen
zusammenzustellen, dass in möglichst vielen Verarbeitungszyklen ausschließlich
ungültige Arbeitselemente enthalten sind. Diese Arbeitselemente sind in zeitlicher

                                          - 12 -



Hinsicht „in Linie gebracht“, da sie in demselben Verarbeitungszyklus verarbeitet
werden sollen (vgl. Offenlegungsschrift, z.B. Figur 7 - die Arbeitselemente werden
jeweils innerhalb der einzelnen Spalten von Arbeitselementen derart umgeordnet,
dass die vier ungültigen Arbeitselemente 0, 6, 9 und 15 zur Ausführung in
demselben Verarbeitungszyklus „clk 3“ vorgesehen sind).


Das im jeweiligen Patentanspruch 1 nach Haupt- und Hilfsantrag 1 anstelle von
Merkmal M10 enthaltene Merkmal M10‘ geht inhaltlich nicht über Merkmal M10
hinaus.


Das Steuermodul soll ferner ausgelegt sein, Arbeitselemente in einem Block von
Arbeitselementen umzuordnen, indem zumindest ein Rotations- oder ein
Tauschvorgang durchgeführt wird (Merkmal M11).


Ferner soll dieses Modul mit der Gruppe von Verarbeitungsbahnen eine gekoppelte
„Logik“ - also logische Schaltungen - umfassen, die ausgelegt sind, die Gruppe von
Verarbeitungsbahnen zu veranlassen, die Ausführung einer Gruppe von ungültigen
Arbeitselementen    zu    überspringen,       falls   die   Gruppe    von    ungültigen
Arbeitselementen die einzigen Arbeitselemente sind, die für die Ausführung in der
Gruppe von Verarbeitungsbahnen in einem Verarbeitungszyklus eingeplant sind
(Merkmal M12). Damit wird zum Ausdruck gebracht, dass ein Verarbeitungszyklus,
in   dem   ausschließlich    ungültige,     „vorübergehend     in    Linie   gebrachte“
Arbeitselemente ausgeführt werden sollen, übergangen werden kann. Dadurch
verringert sich die Anzahl ungenutzter „Verarbeitungsschlitze“ (Offenlegungsschrift,
Absatz [0044]), d.h. die Anzahl von Zeitfenstern, in denen keine Befehle zur
Ausführung vorgesehen sind.


Merkmal M13 zufolge soll das Steuermodul ausgelegt sein, einen entsprechenden
Indikator für eine Mehrzahl der Blöcke von Arbeitselementen zu setzen, um die
Reihenfolge der Arbeitselemente innerhalb der Mehrzahl von Blöcken von

                                         - 13 -



Arbeitselementen anzuzeigen. Ein solcher Indikator kann mehrere Bits umfassen
(Offenlegungsschrift, Absatz [0046]; ursprüngliche Patentansprüche 10, 11).


Schließlich sollen Befehle eines jeweiligen Blocks von Arbeitselementen, die sich
auf einen jeweiligen Pixelquad beziehen, eingeplant sein, in einer jeweiligen
Verarbeitungsbahn ausgeführt zu werden (Merkmal M15). Vor dem Hintergrund der
Offenlegungsschrift (vgl. Absatz [0037] mit Figur 6) kann dies bedeuten, dass die
die einzelnen Pixelwerte eines Pixelquads ausschließlich in einer einzigen
Verarbeitungsbahn verarbeitet werden (im Beispiel der Figur 6 sollen die
Arbeitselemente 0 bis 3, mit denen offensichtlich Berechnungen an den Pixeln eines
ersten Pixelquads vorgenommen werden, ausschließlich in der ganz linken
Verarbeitungsbahn ausgeführt werden, die Arbeitselemente 4 bis 7 in der zweiten
Verarbeitungsbahn    von    links   usw.).   Diese    Anordnung       der    Blöcke   von
Arbeitselementen ist in der Anmeldung auch als „Spalte-zuerst-Ordnung“
bezeichnet (vgl. Offenlegungsschrift, Absatz [0035]).


Jedoch ist zu beachten, dass sich Merkmal M15 auf die Ausführung von Befehlen
eines Blocks von Arbeitselementen bezieht; es beschreibt damit auch eine
Zuordnung zwischen den einzelnen Befehlen, die auf mindestens ein Pixel eines
Pixelquads angewendet werden sollen, und den „jeweiligen“ Verarbeitungsbahnen,
in denen diese Befehle ausgeführt werden sollen. Merkmal M15 ist somit auch dann
erfüllt, wenn ein einzelner SIMD-Befehl, der auf mindestens ein Pixel eines
Pixelquads    angewendet     werden      soll,    gleichzeitig   in   unterschiedlichen
Verarbeitungsbahnen ausgeführt werden soll - d.h. in Form mehrerer, von der
SIMD-Verarbeitungseinheit     parallel    verarbeiteter    Befehle,    die    in   einem
entsprechenden Block von Arbeitselementen enthalten sind.


Zudem kann aus Merkmal M15 nicht abgeleitet werden, dass „Befehle eines
jeweiligen Blocks von Arbeitselementen, die sich auf einen jeweiligen Pixelquad
beziehen“ ausschließlich auf das in Merkmal M15 genannte Pixelquad angewendet
werden sollen, wenn sie eingeplant sind, in einer „jeweiligen Verarbeitungsbahn

                                         - 14 -



ausgeführt“ zu werden. So kann z.B. der Befehl „Addiere X zum jeweiligen
Pixelwert“ zunächst auf einen Pixelwert eines Pixelquads in einer bestimmten
Verarbeitungsbahn       angewendet       werden,     und     später    in    derselben
Verarbeitungsbahn auf einen Pixelwert eines anderen Pixelquads. Auch dieser Fall
fällt unter den Wortlaut von Merkmal M15. Im Ergebnis ist Merkmal M15 also auch
dann erfüllt, wenn dieselben Befehle, die in einer bestimmten Verarbeitungsbahn
auf mindestens ein Pixel eines Pixelquads angewendet werden sollen, in derselben
Verarbeitungsbahn auch auf andere Pixelquads angewendet werden sollen.


3.     Der jeweilige Patentanspruch 1 in der Fassung des Hauptantrags und der
Hilfsanträge 1 bis 6 ist so klar und deutlich gefasst, dass sein Schutzbereich
hinreichend sicher vorhersehbar ist. Außerdem ist die damit beanspruchte Lehre in
der Anmeldung so deutlich und vollständig offenbart, dass ein Fachmann sie
ausführen kann.


4.     Der Gegenstand des jeweiligen Patentanspruchs 1 nach Hauptantrag sowie
nach den Hilfsanträgen 1 bis 6 beruht jedoch nicht auf einer erfinderischen Tätigkeit.


4.1    Für die Beurteilung der beanspruchten Lehre sind die Druckschriften G9 und
D2 von besonderer Bedeutung.


4.1.1 Die Druckschrift G9 ist ein Teil einer einführenden Textreihe zur parallelen
Datenverarbeitung in einer Grafikpipeline (Seite 1, erster Absatz sowie zweiter
Absatz, erster Satz), in dem die Parallelisierung von Rasterungs- und
Shadingoperationen (vgl. die Abschnitte „Going wide during rasterization“, „You
need to go wider!“), die Interpolation von Pixelattributen (vgl. die Abschnitte
„Attribute interpolation“, „“Centroid“ interpolation is tricky“) und weitere Teilaspekte
des Shadings (vgl. Abschnitt „The actual shader body“) diskutiert werden.


Dieser Druckschrift ist insbesondere zu entnehmen, dass bei der Grafikarchitektur
„Fermi“ der Firma NVidia Threads in Einheiten von Warps an die Shader-Einheiten

                                       - 15 -



einer GPU geschickt werden, wobei ein Warp 32 Threads umfasst (vgl. Abschnitt
„You need to go wider!“ – „for NVidia, the unit of dispatch to shader units is 32
threads, which they call a „Warp“.“). Für den Fachmann ist selbstverständlich, dass
die Anzahl der Threads pro Warp (diese wird im Folgenden als „NThW“ bezeichnet)
von der gewählten Grafikarchitektur abhängig ist.


Da alle Threads in einem Warp denselben Code ausführen (vgl. Seite 5, letzter
Absatz – „[…] work on all elements of each batch usually proceeds in lockstep. All
„threads“ run the same code, at the same time.“ i. V. m. Seite 5, vorletzter Absatz –
„multiple batches (or „Warps“ on NVidia hardware […])“), stellt die in Druckschrift
G9 beschriebene GPU eine SIMD-Verarbeitungseinheit im Sinne des Merkmals M1
dar.


Eine Menge von 2n aufeinanderfolgender Warps (mit n = 1, 2, 3, …) kann als ein
Verarbeitungsvorgang angesehen werden, der die Höchstzahl von 2n • NThW
Threads - d.h. von Arbeitselementen im Sinne des Patentanspruchs 1 - umfasst
(Merkmale M2, M2a).


Die verarbeiteten Pixelwerte sind ferner in Pixelquads angeordnet, d.h. in 2x2-
Blöcken von Pixelwerten (vgl. Figur auf Seite 3; Merkmale M4 und M14).


Da bei der Ausführung eines Threads solche Pixelwerte verarbeitet werden (vgl.
Seite 2, erster vollständiger Absatz – „Each Pixelquad has 4 pixels (each of which
in turn can be handled as one thread)“), ist auch Merkmal M3 erfüllt.


Ferner setzt sich ein aus 2n Warps bestehender Verarbeitungsvorgang aus zwei
nacheinander ausgeführten Blöcken mit jeweils n • NThW Threads zusammen. Diese
Blöcke beziehen sich selbstverständlich auf all diejenigen Pixelquads, die im
Rahmen des Verarbeitungsvorgangs verarbeitet werden sollen (Merkmal M5).


Weiterhin zeigt die Druckschrift G9, dass einige der Pixel eines Pixelquads, die an
die Shader-Einheiten der GPU geschickt werden, unsichtbar sind, so dass an ihnen

                                         - 16 -



kein Shading durchgeführt werden muss (vgl. Seite 2, letzter Absatz und Seite 3,
erster Absatz i. V. m. der Figur auf Seite 3 - die Werte der hellgrau hinterlegten
unsichtbaren      Pixel    werden      weder      für   ein    Shading           noch    für
Gradientenberechnungen verwendet, die Werte der mittelgrau hinterlegten,
ebenfalls      unsichtbaren       Helferpixel     („helper      pixels“)         nur     für
Gradientenberechnungen, die Werte der dunkelgrau hinterlegten sichtbaren Pixel
sowohl für ein Shading als auch für Gradientenberechnungen). Die unsichtbaren
Pixel sind zwar maskiert, jedoch wird auch an ihnen zwangsläufig ein Shading
durchgeführt (vgl. Seite 2, erster vollständiger Absatz – „[…] all pixels in a Pixelquad,
even the masked ones, get shaded“), was selbstverständlich voraussetzt, dass alle
Pixelwerte des Pixelquads auch für das Shading vorgesehen werden (Merkmal M6).


Die Werte der unsichtbaren Pixel stellen „ungültige“ Pixelwerte im Sinne des
Patentanspruchs 1 dar, da an ihnen selbstverständlich weniger Befehle als an den
Werten der sichtbaren Pixel auszuführen sind. Dementsprechend sind die
maskierten Threads, die der Verarbeitung der Werte der unsichtbaren Pixel dienen,
ungültige Arbeitselemente im Sinne von Patentanspruch 1.


Somit ist auch Merkmal M7 erfüllt.


Allerdings gehen die Merkmale M8 bis M13 und M15 nicht unmittelbar aus der
Druckschrift G9 hervor.


4.1.2 Die Druckschrift D2 befasst sich mit Methoden zur Maximierung der
Ressourcenauslastung in Grafikverarbeitungseinheiten, die nach dem SIMD-Prinzip
arbeiten    und   aus     mehreren    Streaming-Multiprozessoren           mit    parallelen
Verarbeitungsbahnen („execution lanes“, „SIMD lanes“) bestehen. In diesen
Bahnen werden Threads (d.h. parallelisierbare Befehlsfolgen) ausgeführt, die ein
Programmierer zu sog. kooperativen Threadfeldern („CTAs“ = „cooperative thread
arrays“) gruppiert hat, welche ihrerseits aus mehreren „Warps“ bestehen - d.h. aus
kleineren Threadgruppen, die denselben Code umfassen (vgl. Druckschriftentitel i.

                                          - 17 -



V. m. Abschnitt 2.1). Die Anzahl gleichzeitig ausführbarer Threads (die „SIMDwidth“,
vgl. Abschnitt 3.3, Gleichung (1) mit darunterstehendem Text - „SIMDwidth
designates the width of the SIMD pipeline“) hängt dabei von der verwendeten
Grafikarchitektur ab; demensprechend sind in den Beispielen der Figuren 7, 8 und
9 jeweils 4, 16 und 8 Verarbeitungsbahnen gezeigt.


Damit sind bereits die Merkmale M1, M2, M2a, M3 und M8 verwirklicht. Denn ein
nach dem SIMD-Prinzip arbeitender Streaming-Multiprozessor ist eine SIMD-Verarbeitungseinheit im Sinne von Merkmal M1. Die Verarbeitungsbahnen eines
solchen Multiprozessors bilden eine Gruppe und sind ausgelegt, die Befehle der
Threads mehrerer CTAs (d.h. die Befehle der Arbeitselemente mehrerer
Verarbeitungsvorgänge)         über   mehrere       Verarbeitungszyklen      auszuführen
(Merkmale M2, M8). Die CTAs umfassen eine Höchstanzahl von Arbeitselementen
(vgl. z.B. Figur 1 mit Bildunterschrift - „each CTA contains 3 warps of 4 threads
each“, d.h. zwölf Arbeitselemente; Merkmal M2a). Da ein Streaming-Multiprozessor
eine   SIMD-Verarbeitungseinheit       darstellt,   wird    ein    CTA    über   mehrere
Verarbeitungsbahnen in mehreren Verarbeitungszyklen ausgeführt, so dass jede
Verarbeitungsbahn      eine     Sequenz     von     Befehlen      (selbstverständlich   an
entsprechenden Datenelementen) ausführt, die sie mit den anderen Bahnen
gemeinsam hat (Merkmal M3).


Ferner ist den einleitenden Abschnitten der Druckschrift D2 zu entnehmen, dass ein
sogenanntes SIMT-Ausführungsmodell („SIMT“ = „single-instruction multiplethread“) es ermöglicht, in Grafikprozessoren („GPUs“) effiziente SIMD-Pipelines zu
verwenden und gleichzeitig in den ausgeführten Threads beliebige Kontrollflüsse
vorzusehen.    Die    GPU-Hardware        würde      auch    bedingte     Verzweigungen
unterstützen, so dass jede SIMD-Verarbeitungsbahn ihren eigenen logischen
Thread ausführen könne (vgl. Abschnitt 1, erster Absatz sowie Abschnitt 2.1 und
Abschnitt 2.2, erster Satz).

                                       - 18 -



Die    unabhängige      Verarbeitung     von    Verzweigungen       würde     durch
hardwaregenerierte Bitmasken ermöglicht, welche kennzeichneten, ob ein Thread
aktiv sei oder nicht. Gemäß dem SIMT-Ausführungsmodell würde die Ausführung
einer divergenten Verzweigung teilweise serialisiert, da der „wahre“ und der
„falsche“ Pfad nacheinander ausgeführt und die Threads auf dem jeweils nicht
aktiven Pfad maskiert werden müssten. Bei jeder Divergenz würden Threads
maskiert und nicht ausgeführt, so dass sich die Anzahl aktiver Threads und damit
die Auslastung der SIMD-Verarbeitungsbahnen weiter reduziere und die Anzahl
„vergeudeter Verarbeitungsschlitze“ („wasted execution slots“) erhöhe (vgl.
Abschnitt 2.2 i. V. m. Figur 1; Abschnitt 2.3, erster Satz; s. auch Abstract und
Abschnitt 1, erster Absatz).


Somit bilden Gruppen aufeinanderfolgender Warps innerhalb eines jeden CTA
Blöcke von Arbeitselementen, die maskierte Threads - und somit ungültige
Arbeitselemente - enthalten und über mehrere Verarbeitungszyklen ausgeführt
werden (Merkmale M7 und M9).


Um die Auslastung der SIMD-Verarbeitungsbahnen zu verbessern, beschreibt die
Druckschrift D2 zunächst die Methode der Threadblock-Verdichtung („Thread block
compaction“ = „TBC“; vgl. Abschnitt 2.3 sowie Figuren 1 und 2). Dabei werden
Threads innerhalb eines CTA unter Beibehaltung ihrer Verarbeitungsbahn (ihrer
„home lane“) umgeordnet (vgl. Abschnitt 2.3 i. V. m. Figuren 1 und 2 - die Warps „-
- - 7“ und „- - A - “ des CTA B und die Warps „4 5 6 -“ und „8 9 - B“ des CTA C
werden umgeordnet, so dass die Warps „- - A 7“ und „- - - -“ bzw. „4 5 6 B“ und „8 9
- -“ entstehen). Die Auslastung der SIMD-Verarbeitungsbahnen erhöht sich genau
dann, wenn sich durch die Umordnung die zur Verarbeitung des CTA erforderliche
Anzahl von Warps verringert, d.h. wenn Warps entstehen, die ausschließlich
maskierte Threads enthalten und daher nicht ausgeführt werden (vgl. Figur 1 - ohne
Verdichtung werden die Warps „- - - 7“ und „- - A - “ des CTA B in zwei
Verarbeitungszyklen ausgeführt, nach der Verdichtung genügt stattdessen die

                                      - 19 -



Ausführung    des   verdichteten    Warps      „-   -   A   7“   in   einem   einzigen
Verarbeitungszyklus).


Die Lehre der Druckschrift D2 geht noch über eine derartige Threadblock-Verdichtung hinaus, indem die Threads vor der Verdichtung innerhalb der Warps -
d.h. über die Verarbeitungsbahnen hinweg - im Rahmen einer „SIMD Lane
Permutation“ („SLP“) permutiert werden (vgl. insbesondere Abschnitte 4.1 und 4.3
i. V. mit den Figuren 7 bis 9 sowie Abschnitt 4.4 – „Implementation of SLP […]
Enabling SLP on top of TBC […]“).


Durch die Permutationen werden die Threads automatisch auch innerhalb der
verschiedenen Gruppen aufeinanderfolgender Warps (d.h. in den Blöcken von
Arbeitselementen) mit der Zielsetzung umgeordnet, dass nach der Verdichtung
möglichst viele Warps vorliegen, die ausschließlich maskierte (d.h. ungültige) und
„in Linie gebrachte“ Threads verschiedener Gruppen von Warps enthalten
(Teilmerkmal von Merkmal M10 und M10‘). Diese Threads werden jedoch nicht
ausgeführt, vielmehr wird die Ausführung der maskierten Threads „übersprungen“
(Teilmerkmal von Merkmal M12; vgl. die Teilabbildungen der Abbildungen 7 (b) bis
(h), die mit den Begriffen „Permuted“ und „Compacted“ bezeichnet sind). Bei den
Permutationen tauschen die Arbeitselemente eines Warps im Allgemeinen die
Verarbeitungsbahnen (Teilmerkmal von Merkmal M11).


Es ist selbstverständlich, dass die Ausführung der Permutationen - ebenso wie das
„Überspringen“ der Warps - durch ein entsprechendes Hardware- und/oder
Softwaremodul gesteuert werden muss. Somit verwirklicht die Druckschrift D2 auch
die verbleibenden Teilmerkmale der Merkmale M10, M10‘, M11 und M12.


Die Druckschrift D2 lehrt ferner, dass die Reihenfolge der Threads innerhalb der
einzelnen Warps (die „thread order within a warp“) durch Abbildungsfunktionen
(„mapping functions“) definiert wird, welche die Zuordnung eines Threads zur
jeweiligen Verarbeitungsbahn anzeigen und damit einen Indikator im Sinne des

                                       - 20 -



Merkmals M13 darstellen (vgl. vorletzter Absatz vor Abschnitt 4.2; s. auch Figuren
7 (b) bis (h), in denen Beispiele für Zuordnungen gezeigt sind, die durch die
Abbildungsfunktionen definiert werden).


Somit zeigt die Druckschrift D2 auch Merkmal M13.


Die Druckschrift D2 befasst sich jedoch nicht speziell mit der Verarbeitung von
Pixelquads und offenbart daher die Merkmale des aus den Merkmalen M4 bis M6
sowie M14 und M15 bestehenden Merkmalskomplexes nicht ausdrücklich.


4.2    Der Fachmann gelangte ausgehend von der Druckschrift G9 mit Rücksicht
auf den aus der Druckschritt D2 bekannten Stand der Technik in naheliegender
Weise zum Gegenstand von Patentanspruch 1 nach Hilfsantrag 6.


So ist in Druckschrift G9 beschrieben, dass 25%-75% der für das Shading eines
Pixelquads aufgewendeten Arbeit vergeudet werden, wenn viele kleine Dreiecke zu
rendern sind, da auch für die unsichtbaren Helferpixel ein Shading durchgeführt wird
(vgl. Seite 2 - „[…] between 25-75% of the shading work for Pixelquads generated
for triangle edges is wasted“; Seite 3 - „wasted shading work on pixelquads“; je
nachdem ob ein Pixelquad ein, zwei oder drei Helferpixel besitzt, sind 25%, 50%
oder 75% der Shading-Arbeit überflüssig). Zum Zeitpunkt der Abfassung der
Druckschrift G9 erlaubten weder Programmierschnittstellen noch die Hardware eine
Vereinigung von Pixelquads (Seite 3, erster Absatz, vorletzter Satz).


Der Fachmann hatte somit Veranlassung, im Stand der Technik nach Verfahren zu
suchen, die es erlauben, ein Pixel-Shading zu beschleunigen, wenn eine große Zahl
von Pixeln - und damit auch eine große Zahl der zu diesen Pixeln gehörenden
Threads - ungültig ist.


Hierbei konnte er auf die Druckschrift D2 stoßen, die aufzeigt, wie Warps, die
ungültige Threads aufweisen, durch eine Umordnung von Threads innerhalb von
CTAs beschleunigt verarbeitet werden können (s.o., Abschnitt II.4.1.2).

                                      - 21 -



Für den Fachmann bot es sich daher an, die Lehre der Druckschrift D2 zur
Verarbeitung der in Druckschrift G9 beschriebenen Warps einzusetzen, indem er
zur Verarbeitung von Pixelquads mit unsichtbaren (d.h. ungültigen) Pixeln und somit
ungültigen Threads eine SIMD-Verarbeitungseinheit vorsah, die zunächst CTAs mit
gültigen und ungültigen Threads bereitstellt, diese Threads innerhalb der Warps
über Verarbeitungsbahnen hinweg permutiert und über die Grenzen von Gruppen
aufeinanderfolgender Warps hinweg verdichtet, so dass verdichtete Warps
entstehen, die ausschließlich aus ungültigen Threads bestehen und daher
übersprungen werden können. Dies ist gerade dann von Vorteil, wenn Warps mit
geringen Threadanzahlen NThW verarbeitet werden.


Auf diese Weise gelangte der Fachmann ausgehend von der Druckschrift G9 (diese
zeigt die Merkmale M1 bis M7 und M14, vgl. Abschnitt 4.1.1), unter
Berücksichtigung des aus der Druckschrift D2 Bekannten auch zu den Merkmalen
M8 bis M13.


Das verbleibende Merkmal M15 ergibt sich für den Fachmann wie folgt:


Gemäß Abschnitt 2.1 der Druckschrift D2 wird ein einzelner SIMD-Befehl
ausgeführt, indem er in Form eines Warps an jede der Verarbeitungsbahnen
ausgegeben und dort mehrfach ausgeführt wird. Wenn der Fachmann die Lehre der
Druckschrift D2 auf die parallele Verarbeitung von Pixelquads anwendet, werden
mit dem SIMD-Befehl gleichzeitig verschiedene Pixelwerte eines Pixelquads in
unterschiedlichen Verarbeitungsbahnen verarbeitet. Entsprechend der Auslegung
aus Abschnitt II.2 ergibt sich damit auch Merkmal M15.


Zudem ist es in der Grafikverarbeitung üblich, alle Pixel eines Bildes derselben
Rechenoperation zu unterziehen (z.B. wird ein Bild oft aufgehellt, indem zu einem
Helligkeitswert eines Pixels ein konstanter Wert addiert wird). In diesen Fällen
werden dieselben Befehle für sehr viele Pixelquads in allen Verarbeitungsbahnen

                                        - 22 -



über eine große Anzahl von Verarbeitungszyklen ausgeführt, so dass sich Merkmal
M15 auch aus diesem Grund ergibt (vgl. ebenfalls Abschnitt II.2).


4.3   Der Hauptantrag und die Hilfsanträge 1 bis 5 können nicht günstiger beurteilt
werden, da ihr jeweiliger Patentanspruch 1 inhaltlich nicht über Patentanspruch 1
gemäß Hilfsantrag 6 hinausgeht und ebenfalls durch das aus den Druckschriften G9
und D2 Bekannte nahegelegt ist.


4.4   Die Anmelderin wendet ein, insbesondere die Merkmale M9, M10 und M15
seien nicht aus der Druckschrift D2 ableitbar.


Erfindungsgemäß werde nämlich das jeweils nächste Arbeitselement eines Warps,
welcher jeweils einen Verarbeitungsvorgang im Sinne der Anmeldung darstelle,
derselben Verarbeitungsbahn zugewiesen, bis eine vorgegebene Zahl der
Verarbeitungszyklen erreicht sei, und erst dann die nächste Verarbeitungsbahn
verwendet. Dementsprechend verlangten die Merkmale M9, M10 und M15, dass die
Arbeitselemente eines gegebenen Blocks von Arbeitselementen derselben
Verarbeitungsbahn zugeordnet werden, d.h. eine „Spalte-zuerst-Ordnung“ der
Pixelquads (vgl. die Ausführungen zu Merkmal M15 in Abschnitt II.2). Dies sei von
Vorteil, da von der gleichen Verarbeitungsbahn aus auf die verschiedenen
Pixelwerte eines Pixelquads zugegriffen werde, welche sowohl in räumlicher Nähe
zueinander als auch in räumlicher Nähe zur Verarbeitungsbahn abgespeichert
seien. Hingegen verlange das Grundprinzip der Druckschrift D2, Arbeitselemente
eines Blocks von Arbeitselementen auf unterschiedlichen Verarbeitungsbahnen
auszuführen;   dementsprechend      erfolge      eine   Umordnung   hinsichtlich   der
Verarbeitungsbahn,     aber    gerade     nicht     innerhalb   eines   Blocks     von
Arbeitselementen, so dass von unterschiedlichen Verarbeitungsbahnen aus auf ein
Pixelquad zugegriffen werden müsse.


Zudem orientiere sich die Bildung von Blöcken von Arbeitselementen in der
Druckschrift D2 nicht an Blöcken von Daten, an denen die Arbeitselemente

                                        - 23 -



ausgeführt werden; eine Zuordnung von Blöcken von Datenelementen einerseits
und Blöcken von Arbeitselementen andererseits werde ebenso wie eine gezielte
Zusammenstellung der Pixelwerte in Pixelquads in der Druckschrift D2 nicht
vorgenommen.


Diese Argumente greifen jedoch nicht durch.


So beruht die Argumentation der Anmelderin im Wesentlichen auf der Annahme,
dass ein Verarbeitungsvorgang einem Warp und ein Block von Arbeitselementen
eine Menge von Arbeitselementen entspricht, die ausschließlich von einer einzigen
Verarbeitungsbahn im Sinne einer „Spalte-zuerst-Ordnung“ ausgeführt werden.
Hierfür liefert Patentanspruch 1 jedoch keinen Anhaltspunkt, da in ihm weder der
Umfang eines Verarbeitungsvorgangs noch der Umfang eines Blocks von
Arbeitselementen konkret festgelegt wird. Deshalb ist aus den Merkmalen M9 und
M10 auch nicht zwangsläufig abzuleiten, dass ein Block von Arbeitselementen in
einer einzigen Verarbeitungsbahn liegt und dass eine Umordnung von Threads auf
eine solche Verarbeitungsbahn beschränkt ist (s.o., Abschnitt II.2). Vielmehr können
auch Gruppen aufeinanderfolgender Warps als Blöcke von Arbeitselementen
angesehen werden, so dass in diesem Fall die Merkmale M9 und M10 erfüllt sind
(s.o., Abschnitt II.4.1.2). Außerdem kann - wie bereits unter Abschnitt II.2 ausgeführt
- Merkmal M15 auch so zu verstehen sein, dass eine Zuordnung zwischen Befehlen
und unterschiedlichen Verarbeitungsbahnen existiert, wie es bei der parallelen
Ausführung eines SIMD-Befehls der Fall ist.


Im Übrigen werden bereits dann mehrere Threads, die der Verarbeitung der
Pixelwerte ein und desselben Pixelquads dienen, zur Ausführung in derselben
Verarbeitungsbahn vorgesehen, wenn die Anzahl der Verarbeitungsbahnen gleich
der halben Anzahl der Pixelwerte eines Pixelquads beträgt (d.h. 2 Bahnen, falls 2x2-
Pixelquads verarbeitet werden; 8 Bahnen bei 4x4-Pixelquads). Bei einem solchen
Verständnis sind insbesondere die Merkmale M9, M10 und M15 verwirklicht.

                                       - 24 -



Der Anmelderin ist zwar insoweit zuzustimmen, dass die Druckschrift D2 nichts zur
Beziehung zwischen Pixelquads und den zugehörigen Threads aussagt. Eine
solche Beziehung geht aber aus der Druckschrift G9 hervor, die insbesondere die
Merkmale M4 bis M6 zeigt (s.o., Abschnitt II.4.1.1).


Was den von der Anmelderin angeführten Vorteil anbelangt, ist festzustellen, dass
die vorliegende Patentanmeldung offenlässt, wo die einzelnen Pixelwerte eines
Pixelquads gespeichert sind und welche räumliche Beziehung zwischen dem
Speicherort der Pixelwerte und den Verarbeitungsbahnen besteht, so dass aus
Patentanspruch 1 kein vorteilhaftes Speicherzugriffsverhalten abgeleitet werden
kann. Darüber hinaus zeigt die Druckschrift D2, dass die Reihenfolge von Threads
innerhalb eines Warps das Speicherzugriffsverhalten bestehender Hardware zur
Threadblock-Verdichtung nicht beeinflusst (vgl. Abschnitt 4.1, vorletzter Absatz,
letzter Satz).


5.     Da über einen Antrag jeweils nur einheitlich entschieden werden kann, fallen
mit dem jeweiligen Patentanspruch 1 nach Hauptantrag und den Hilfsanträgen 1 bis
6 auch die übrigen Patentansprüche dieser Anträge (BGH GRUR 1997, 120 –
Elektrisches Speicherheizgerät).

                                              - 25 -




                                  Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft
       Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt
       war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht
       der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften
       über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek                  Merzbach                    Dr. Forkel                  Dr. Städele
