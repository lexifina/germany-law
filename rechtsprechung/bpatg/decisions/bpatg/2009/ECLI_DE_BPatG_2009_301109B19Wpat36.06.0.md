---
ecli: "ECLI:DE:BPatG:2009:301109B19Wpat36.06.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 36/06"
decided: "2009-11-30"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2009&Sort=1&Seite=87&nr=15691&anz=1436&pos=1315&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2009-11-30_19_W-pat_36_06_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 19 W (pat) 36/06 vom 2009-11-30

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 36/06                                                   Verkündet am
_______________                                                  30. November 2009
    (Aktenzeichen)                                                       …




                               BESCHLUSS

                             In der Beschwerdesache


…




                betreffend die Patentanmeldung 197 40 550.9-55


hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 30. November 2009 unter Mitwirkung des Vorsitzenden Richters Dipl.-Ing. Bertl, der Richterin Kirschneck sowie der Richter
Dr.-Ing. Scholz und Dipl.-Ing. J. Müller




BPatG 154
08.05

                                     -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                  Gründe


                                      I.
Die am 15. September 1997 beim Deutschen Patent- und Markenamt eingegangene Patentanmeldung mit der Bezeichnung „Steuerung“, die die Priorität der
deutschen Gebrauchsmusteranmeldung DE 296 17 837 vom 14. Oktober 1996 in
Anspruch nimmt, wurde von der Prüfungsstelle für Klasse G05B durch am
18. Mai 2006 verkündeten Beschluss mit Datum vom 19. Mai 2006 mit der Begründung zurückgewiesen, der Anmeldegegenstand betreffe keine Erfindung im
Sinne des § 1 PatG.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Sie beantragt,


       den angefochtenen Beschluss der Prüfungsstelle für Klasse G05B
       des Deutschen Patent- und Markenamtes vom 19. Mai 2006 aufzuheben und das nachgesuchte Patent mit folgenden Unterlagen
       zu erteilen:
       - Patentansprüche 1 bis 3 gemäß Hauptantrag, überreicht in der
       mündlichen Verhandlung,
       - Beschreibung und 20 Blatt Zeichnungen, Figuren 1 bis 18, vom
       Anmeldetag 15. September 1997.

                                          -3-



Der geltende Patentanspruch 1 lautet unter Einfügung einer Merkmalsgliederung:


       F1   Steuerung (ST) mit Mitteln zum Steuern eines technischen
            Prozesses und Mitteln zur Steuerung einer Bewegung einer
            Verarbeitungsmaschine,
       F2   mit einem während eines Steuerbetriebs durch eine von der
            Steuerung (ST)
            umfasste CPU-Einheit ausführbaren,
            Softwaremodule umfassenden Steuerprogramm,


       dadurch gekennzeichnet, dass


       F3   das Steuerprogramm zum Steuern des technischen Prozesses eine Prozesssteuerungsfunktionalität und zur Steuerung
            der Bewegung der Verarbeitungsmaschine eine Bewegungssteuerungsfunktionalität vereint,
       F4   indem es zumindest zwei Softwaremodule (1) umfasst,
       F4.1 die ihrerseits
       F4.2 mindestens ein zur Bewegungssteuerung vorgesehenes sequentielles Programm (4a, 4b) und
       F4.3 mindestens       ein    einerseits    zur   Prozesssteuerung    und
            andererseits zum Aufruf wie auch zur Koordination des oder
            jedes sequentiellen Programms (4a, 4b) vorgesehenes zyklisches Programm (3a, 3b) umfassen,
       F5   wobei jedes sequentielle Programm (4a, 4b) und jedes zyklische Programm (3a, 3b) einen Variablen- und Konstantendeklarationsteil (5) umfasst,
       F6   wobei die Softwaremodule jeweils einen Deklarationsteil (2)
            umfassen, auf welchen die Programme des jeweiligen Softwaremoduls (1)         zugreifen     und    in   welchem   Variablen

                                       -4-



             und/oder Datenstrukturen und/oder Bewegungsprofile hinterlegt sind.


Als Aufgabenstellung nennt die Anmelderin (Seite 2, Zeilen 19 bis 26 der ursprünglichen Unterlagen):


       „eine Steuerung der eingangs genannten Art anzugeben, welche
       die Verwirklichung von Prozessfunktionalitäten sowie von technologischen Bewegungsabläufen von Verarbeitungsmaschinen vereinfacht.
       Darüber hinaus ist ein Programmiergerät zu schaffen, das die Erstellung für eine derartige Steuerung vereinfacht.“


Die Patentanmelderin ist der Auffassung, bei der von ihr angemeldeten Steuerung
sei erstmals vorgesehen, ein vollständig modulares Steuerprogramm für Verarbeitungsmaschinen anzugeben, bei dem aus einem zyklischen Programmteil heraus ein oder mehrere sequentielle Programmteile aufgerufen würden.


Diese Modularität werde dadurch erreicht, dass sowohl das Softwaremodul in einem Kopfteil als auch die einzelnen zyklischen und sequentiellen Programmteile
jeweils separate Konstantendeklarationsteile hätten.


Hierzu gebe es keinerlei Anregung aus dem bekannt gewordenen Stand der
Technik.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt Bezug genommen.

                                        -5-



                                          II.


Die frist- und formgerecht erhobene Beschwerde ist zulässig. Sie hat jedoch keinen Erfolg, da der Gegenstand des Patentanspruchs 1 nach § 1 Abs. 1 PatG in
Verbindung mit § 4 PatG nicht auf einer erfinderischen Tätigkeit beruht.
Aus der bereits im Zurückweisungsbeschluss zitierten Druckschrift (1)
   JONES K.: "IEC 1131-3 programming for motion control" lEE Colloquium on
   Configurable ServoControl Systems, 1994, 6/1 - 6/3
ist Folgendes bekannt: eine


        F1   Steuerung (Seite 6/1, linke Spalte, 3. Absatz: Flexible Machinery Controller) mit Mitteln zum Steuern eines technischen
             Prozesses (Zusammenfassung: applicable to distributed
             multi-tasking motion control systems) und Mitteln zur Steuerung    einer    Bewegung          einer   Verarbeitungsmaschine
             (Seite 6/1, linke Spalte, 3. Absatz, letzter Teilsatz: controlling
             up to 30 tightly co-ordinated axes)
        F2   mit einem während eines Steuerbetriebs durch eine von der
             Steuerung
             umfasste CPU-Einheit (Seite 6/2, linke Spalte, „5. FMC
             Hardware“) ausführbaren,
             Softwaremodule umfassenden Steuerprogramm (Seite 6/1,
             rechte Spalte: 2. Languages),
        wobei
        F3   das Steuerprogramm zum Steuern des technischen Prozesses eine Prozesssteuerungsfunktionalität (Titel PCL - Programming und Seite 6/1, linke Spalte, Absatz 2: Live data
             may then me monitored and displayed … for that application)
             und zur Steuerung der Bewegung der Verarbeitungsmaschine eine Bewegungssteuerungsfunktionalität vereint (motion control),

                                       -6-



       F4    indem es zumindest zwei Softwaremodule (Seite 6/1, linke
             Spalte, Absatz 2: „pre-defined control elements held within
             one or more libraries“) umfasst,
       F4.1 das seinerseits (Seite 6/1, linke Spalte, Absatz 1: „hierarchical programming“)
       F4.2 mindestens ein zur Bewegungssteuerung vorgesehenes sequentielles Programm (Seite 6/1, rechte Spalte, Absatz 3:
             „sequential control algorithms“) und
       F4.3 mindestens     ein   einerseits     zur   Prozesssteuerung   und
             andererseits zum Aufruf wie auch zur Koordination des oder
             jedes sequentiellen Programms vorgesehenes zyklisches
             Programm (Seite 6/1, rechte Spalte, letzter Absatz: „high-level textual language designed for structured programming“)
             umfasst.


Für jeden Fachmann, der hier als Diplom-Ingenieur mit Hochschul- oder zumindest Fachhochschulabschluss der Fachrichtung Elektrotechnik anzunehmen ist,
der mit dem Entwurf von Softwareprodukten für die Prozessleittechnik und die
Maschinensteuerung beauftragt ist und daher die einschlägigen Programmiersprachen beherrscht, ist dabei selbstverständlich, dass sowohl


       F5    jedes sequentielle Programm und jedes zyklische Programm
             einen Variablen- und Konstantendeklarationsteil umfasst, als
             auch
       F6    die Softwaremodule jeweils einen Deklarationsteil umfassen,
             auf welchen die Programme des jeweiligen Softwaremoduls
             zugreifen und in welchem Variablen hinterlegt sind.


Das Wissen des Fachmann bezüglich der Variablen- und Konstantendeklaration
ist beispielsweise durch die der Anmelderin bereits aus dem Prüfungsverfahren
bekannten Druckschrift:

                                       -7-



(4) A. Diepgen: "Einsatz von Hochsprachen in Anpasssteuerungen" in "ZwF" 84
(1989) 9, Seiten 495 bis 499,
belegt.


Dort wird eine Steuerung von Verarbeitungsmaschinen (Seite 495, linke Spalte,
Absatz 3, 1. Zeile: „Werkzeugmachinen“) beschrieben, die einen zyklischen Programmteil (Hochsprache) und daraus heraus aufgerufenen sequentielle Programmteile (SPS-Programmierung) aufweist.


Dabei gibt es sogenannte „Privatdaten“ (Seite 497, rechte Spalte, letzter Absatz),
die nur innerhalb des laufenden Bausteins Gültigkeit haben. Dies sind mit anderen
Worten ausgedrückt, die in Merkmal F5 des Patentanspruchs 1 genannten Variablen- und Konstantendeklarationsteile der sequentiellen und zyklischen Programme.


Daneben gibt es sogenannte „globale Variablen“ (Seite 498, linke Spalte, Satz 2
und 3). Dies entspricht dem im Merkmal F6 des Patentanspruchs 1 genannten
Deklarationsteil, auf welchen die Programme des jeweiligen Softwaremoduls
zugreifen und in welchem Variablen hinterlegt sind.


Somit ist im Patentanspruch 1 lediglich das Grundwissen des Fachmanns wiedergegeben, soweit die darin genannten Merkmale nicht bereits aus der Druckschrift (1) bekannt sind.


Mit dem nicht gewährbaren Patentanspruch 1 fallen auch die auf diesen rückbezogenen Patentansprüche 2 und 3.

                                   -8-



Somit war die Beschwerde zurückzuweisen.




Bertl                 Kirschneck           Dr. Scholz   J. Müller


                                                             prö
