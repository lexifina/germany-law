---
ecli: "ECLI:DE:BPatG:2012:260412B17Wpat102.08.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 102/08"
decided: "2012-04-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2012&Sort=1&Seite=34&nr=23669&anz=1451&pos=519&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2012-04-26_17_W-pat_102_08_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0021.md"]
---

# Bundespatentgericht, 17 W (pat) 102/08 vom 2012-04-26

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 102/08                                                    Verkündet am
_______________                                                       26. April 2012
    (Aktenzeichen)                                                         …




                               BESCHLUSS

                             In der Beschwerdesache


             betreffend die Patentanmeldung 11 2004 001 486.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. April 2012 unter Mitwirkung des Vorsitzenden
Richters      Dipl.-Phys. Dr. Fritsch,   der     Richterinnen     Eder        und
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                     -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und Markenamts vom 5. August 2008 aufgehoben und das Patent mit folgenden Unterlagen erteilt:


       Patentansprüche 1-4,
       Beschreibung Seiten 2-6 und
       6 Blatt Zeichnungen mit Figuren 1-6,


       jeweils überreicht in der mündlichen Verhandlung.




                                  Gründe:


                                       I.


Die vorliegende Patentanmeldung geht hervor aus der internationalen Anmeldung
PCT/US2004/026577, die am 16. August 2004 eingereicht wurde und zwei US-
amerikanische Prioritäten (die früheste vom 14. August 2003) beansprucht. Sie
trägt die Bezeichnung


     „System und Verfahren zur Ortung von kompakten Objekten in Bildern“.


Die Prüfungsstelle für Klasse G06T hat am 5. August 2008 die Anmeldung durch
Beschluss zurückgewiesen unter Bezugnahme auf den Amtsbescheid vom 7. Februar 2008, nach dem den gesamten Anmeldeunterlagen keine klare Lehre zum
technischen Handeln entnehmbar sei und die Ansprüche 1 bis 5 daher mangels
einer klaren nacharbeitbaren Lehre nicht gewährbar seien; soweit erkennbar, sei

                                       -3-



der Anmeldungsgegenstand auch aufgrund § 1 Abs. 3 und 4 PatG von der Patentierbarkeit ausgeschlossen.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       - den angegriffenen Beschluss aufzuheben und das nachgesuchte Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 4,
       Beschreibung Seiten 2 bis 6 und
       6 Blatt Zeichnungen mit Figuren 1 bis 6,
       jeweils überreicht in der mündlichen Verhandlung.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist folgende
Druckschrift genannt worden:


       D1: B. Zhao et al: Automatic detection of small lung nodules on CT
       utilizing a local density maximum algorithm, Journal of Applied Clinical
       Medical Physics, Vol. 4, Nr. 3, Sommer 2003, Seiten 248 bis 260.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat auch Erfolg, da ein Patent nach dem nunmehr geltenden Antrag erteilt wird.

                                        -4-



1.       Gegenstand der Patentanmeldung ist ein System und ein Verfahren zur
Ortung von kompakten Objekten in Bildern. Insbesondere sollen in medizinischen
Bilddaten medizinisch signifikante Objekte erkannt werden, etwa Lungenknötchen
in CT-Lungenscans, vgl. Abs. [0006] der Beschreibung.


Gemäß Abs. [0007] der Beschreibung sind existierende Vorgehensweisen mit
hohem Rechenzeitaufwand verbunden. Es bestehe Bedarf an einem schnellen
Algorithmus, der von einem System für medizinische Bildverarbeitung angewendet
wird, um spezifische Strukturen und/oder Objekte in Bildern zu erkennen (Aufgabe).


Der Patentanspruch 1 lautet:


          „Bildverarbeitungssystem zum Erkennen von medizinischen Objekten in
          dreidimensionalen Bildern, umfassend:

          a) ein Bilderfassungsmodul zum Erfassen eines dreidimensionalen Bildes;

          b) ein Bildsegmentierungsmodul zum Segmentieren des erfassten dreidimensionalen Bildes in ein Vordergrundbild und ein Hintergrundbild;

          c) einen Maskengenerator zum Erzeugen wenigstens einer Maske,
             wobei die Maske ein dreidimensionales Bild umfasst, das eine Vielzahl
             von Voxeln enthält und eine Vielzahl von Seitenflächen aufweist,
             wobei alle auf den Seitenflächen liegenden Voxel einen von Null verschiedenen Wert haben;

          d) einen Kandidatensucher zum Suchen wenigstens eines als Kandidat
             in Frage kommenden Objektes, das wenigstens einem vorgegebenen
             Objekt in wenigstens einem dreidimensionalen Bild ähnlich ist, wobei
             der Kandidatensucher die Maske auf eine vorgegebene Region des

                                         -5-



            Vordergrundbildes anwendet, indem er die Maske auf die vorgegebene Region auflegt, um die Anzahl der Seitenflächen der Maske zu
            bestimmen, welche von der vorgegebenen Region geschnitten werden, wobei der Kandidatensucher das Vorhandensein wenigstens
            eines Kandidaten feststellt, wenn diese Anzahl kleiner als zwei ist;

       e) ein Ausgabemodul zum Ausgeben einer Liste von Kandidaten, die von
            dem Kandidatensucher gefunden wurden.“


Der nebengeordnete Patentanspruch 4 lautet:


       „Verfahren zum Erkennen von Objekten in einem dreidimensionalen Bild,
       umfassend die folgenden Schritte:

       a) Erfassen des dreidimensionalen Bildes unter Verwendung eines Bilderfassungsgerätes; und

       b) Zerlegen des dreidimensionalen Bildes in eine Vordergrundregion und
            eine Hintergrundregion.

       c) Erzeugen wenigstens einer dreidimensionalen Maske; und Suchen
            nach Kandidaten in der Vordergrundregion des dreidimensionalen Bildes durch Verwenden der dreidimensionalen Maske, wobei der Schritt
            des Suchens ferner umfasst:

       d) Auflegen der Maske auf einen vorgegebenen Teil der Vordergrundregion des dreidimensionalen Bildes;

       e) Zählen der Anzahl der Seitenflächen der Maske, welche von dem vorgegebenen Teil der Vordergrundregion geschnitten werden; und

       f)   Feststellen des Vorhandenseins des Objektes, nach welchem gesucht
            wird, falls diese Anzahl kleiner als zwei ist.“

                                       -6-



2.       Die Erfindung ist in den Anmeldeunterlagen so deutlich und vollständig
offenbart, dass ein Fachmann (hier ein Hochschul-Ingenieur der Fachrichtung
Informatik oder Informationstechnik mit Erfahrung in der insbesondere medizinischen Bildverarbeitung) sie ausführen kann (§ 34 Abs. 4 und § 21 Abs. 1 Nr. 2
PatG).


Den ursprünglich eingereichten englischen Unterlagen gemäß WO 2005/017837
A1 ist folgende Lehre zu entnehmen (entsprechende Stellen in der Veröffentlichung der deutschen Übersetzung DE 11 2004 001 486 T5 sind jeweils in Klammern angegeben):


Dreidimensionale Bilddaten werden in einem medizinischen Bildaufnahmesystem
erfasst, wobei das dreidimensionale Bild aus einzelnen Bildpunkten (Voxel, an
manchen Stellen auch als Pixel bezeichnet) besteht. Es kann sich z. B. um Bilder
einer Lunge handeln, aus denen Kandidaten für Knötchen extrahiert werden sollen. Die Bilddaten werden zunächst in eine Vordergrund- und eine Hintergrundregion segmentiert; danach haben alle Hintergrundvoxel einen einheitlichen Wert
(z. B. Null), während die Vordergrundvoxel entweder einheitliche oder unterschiedliche Werte aufweisen können, vgl. S. 6 Abs. 1 (DE 11 2004 001 486 T5
Abs. [0025]).
Sodann wird eine dreidimensionale Maske mit mehreren Seitenflächen definiert,
etwa ein Quader oder Würfel mit sechs Seitenflächen. Den Voxeln der Maske werden Werte zugeordnet, wobei die Werte der Voxel im Maskeninneren auf Null
gesetzt werden, während die Voxel auf den Seitenflächen einen von Null verschiedenen Wert (insbesondere den Wert 1) haben, vgl. S. 6 le. Abs. bis S. 7 Abs. 1
(DE 11 2004 001 486 T5 Abs. [0028]). Der Mittelpunkt der Maske wird über ein
Vordergrundvoxel gelegt, und der unter der Maske liegende Vordergrundbereich
wird in Bezug auf die „Anzahl der Schnittmengen“ zwischen der Maske und der
vorgegebenen Region des Vordergrundbildes untersucht (Fig. 3 Schritt 42 und
44). Falls die „Anzahl der Schnittmengen“ kleiner als zwei ist, wird der untersuchte
Bereich als knötchenverdächtiger Kandidat angesehen (Fig. 3 Schritt 46 und 48).

                                         -7-



Auf diese Weise werden knötchenverdächtige Bereiche identifiziert, die entweder
von ihrer Umgebung isoliert sind oder mit einem Gefäß oder einer Wand verbunden sind; ist dagegen mehr als eine Schnittmenge vorhanden, so ist der untersuchte Bildabschnitt kein Kandidat, vgl. S. 7 le. Abs. bis S. 8 Abs. 1
(DE 11 2004 001 486 T5 Abs. [0031]) in Verbindung mit Fig. 1, vgl. auch S. 3 le.
Abs., S. 9 Abs. 2 und S. 12 le. Abs. bis S. 13 Abs. 1 (DE 11 2004 001 486 T5
Abs. [0009], [0035] und [0045]).
Das Verfahren kann mit unterschiedlich angeordneter Maske und unterschiedlichen Maskengrößen wiederholt werden, vgl. S. 7 Abs. 1 und S. 8 Abs. 2
(DE 11 2004 001 486 T5 Abs. [0028] und [0032]). Schließlich wird die Liste der
ermittelten Kandidaten ausgegeben.


Einzelheiten zur Definition und Bestimmung der „Anzahl der Schnittmengen“ zwischen der Maske und der vorgegebenen Region des Vordergrunds lassen sich
Fig. 4 mit Beschreibung entnehmen:
Fig. 4 zeigt in den Schritten 58 bis 68 die Operationen, welche für eine mit ihrem
Mittelpunkt auf einem Vordergrundvoxel platzierte Maske durchgeführt werden
(vgl. auch Fig. 1 mit den Knötchen 12, 14 und 16 und den um diese herum platzierten Masken 18, 20 und 22). Die hierbei verwendeten Variablen sind unter dem
Bezugszeichen 56 erklärt, insbesondere eine logische Variable „Intersect“, welche
verfolgt, ob ein Schnitt mit einer bestimmten Seite der Maske vorhanden war.
Gemäß Fig. 4 werden nur die auf den Seitenflächen f der Maske liegenden Voxel
(mit Werten ungleich Null) untersucht (Schritte 58, 60). Für jedes dieser Voxel wird
ermittelt, auf welcher Seitenfläche f der Maske das Voxel liegt (Schritt 62), und es
wird abgefragt, ob das entsprechende Voxel des Bildes (auf dem die Maske liegt)
ein Vordergrundvoxel ist (mit Wert ungleich Null, Schritt 64). Wenn dies der Fall ist,
wird festgestellt, dass der betrachtete Vordergrundbereich die zugehörige Seitenfläche f der Maske schneidet (Intersect[f]: = true, Schritt 66).
Wie der Fachmann erkennt, liefert dieses Verfahren für jede Seitenfläche f der
Maske einen Wert der logischen Variablen Intersect[f], welcher angibt, ob diese
Seitenfläche den betrachteten Vordergrundbereich schneidet oder nicht (dass der

                                       -8-



Wert der logischen Variablen anfänglich auf „false“ gesetzt wird und damit im Fall
fehlender Schnitte auf diesem Wert bleibt, liest der Fachmann mit). Es wird nicht
ermittelt, ob die Seitenfläche in einem oder mehreren Voxeln geschnitten wird.
Gemäß der Beschreibung zu Fig. 4 in S. 10 Abs. 2 (DE 11 2004 001 486 T5
Abs. [0038]) werden nur die Schnitte bzw. Schnittmengen (im englischen Original:
„intersections“) mit den Seitenflächen der „Box“, d. h. der Maske gezählt. Dies
weist darauf hin, dass festgestellt werden soll, wie viele Seitenflächen der Maske
von der betrachteten Vordergrundregion geschnitten werden (Anzahl der Schnittmengen).


Allerdings enthalten die Anmeldeunterlagen Widersprüche zu obiger Interpretation
der „Anzahl der Schnittmengen“:
Gemäß S. 7 Z. 5 bis 9 (DE 11 2004 001 486 T5 Abs. [0028] vorle. und le. Satz) soll
die Anzahl der Maskenpixel gezählt werden, die die Vordergrundpunkte schneiden
(eine solche Bestimmung findet in Fig. 4 nicht statt); danach soll bestimmt werden,
wie viele Seitenflächen des Knötchens (Vordergrundbereichs) die Maske schneiden. Außerdem soll gemäß der Beschreibung zu Fig. 5A und 5C auf S. 10 le. Abs.
bis S. 11 Abs. 2 (DE 11 2004 001 486 T5 Abs. [0040] und [0041] dort die Maske
das Knötchen nur an einer Stelle bzw. nur in einem Schnitt (in der obigen Interpretation: nur an einer Seitenfläche der Maske) schneiden, wogegen Fig. 5A und 5C
Schnitte mit drei Seitenflächen der Maske zeigen.


Zur Interpretation der Anmeldung berücksichtigte der Fachmann zum Einen die in
der Beschreibung mehrfach wiederholte Angabe, dass ein Knötchen-Kandidat
gefunden ist, wenn keine Schnittmenge oder nur eine Schnittmenge vorhanden ist,
wobei eine Schnittmenge auf ein an einer Wand oder einem Gefäß (einseitig)
anhaftendes Knötchen hindeutet (vgl. etwa in Fig. 1 das Knötchen 14, welches
von einer Seitenfläche der Maske 20 geschnitten wird), und zum Anderen insbesondere Fig. 4 mit der zugehörigen Beschreibung, welche ein Verfahren zur
Bestimmung der Schnitte bzw. Schnittmengen im Einzelnen zeigt. Im vorliegenden
Fall waren diese Angaben in den ursprünglichen Unterlagen ausreichend, um dem

                                        -9-



Fachmann eine Lehre hinsichtlich der Bestimmung der Schnittmengen und deren
Anzahl zu vermitteln, die er als sinnvoll und tatsächlich gemeint erkennen konnte.
Auf dieser Grundlage mussten dem Fachmann Fig. 5 und die zugehörigen Beschreibungsteile und ebenso die der entnehmbaren Lehre widersprechenden Angaben in S. 7 Z. 5 bis 9 als offensichtlich fehlerhaft und nicht berücksichtigenswert
erscheinen.


3.    Die nunmehr geltenden Unterlagen liegen im Rahmen der ursprünglichen
Offenbarung.


Anspruch 1 ist gestützt auf die ursprünglichen Ansprüche 1, 2, 3, 7, 10 und 11,
S. 6 le. Abs. bis S. 7 Z. 2 und Abs. 2 letzter Satz (DE 11 2004 001 486 T5
Abs. [0028] Satz 1 und 2 und Abs. [0030]) sowie Fig. 4 mit der zugehörigen
Beschreibung, insbesondere auf S. 10 Abs. 2 Satz 1 (DE 11 2004 001 486 T5
Abs. [0038] Satz 1).


Die Unteransprüche 2 und 3 gehen zurück auf die ursprünglichen Unteransprüche 8 und 9.


Der nebengeordnete Patentanspruch 4 geht hervor aus den ursprünglichen Ansprüchen 17, 18, 19 und 20 sowie Fig. 4 mit Beschreibung.


Zudem wurden diejenigen Teile der Beschreibung und der Zeichnungen gestrichen, welche der Fachmann wie oben unter Gliederungspunkt 2. ausgeführt als
offensichtlich fehlerhaft erkannte und daher nicht berücksichtigte. Durch diese
Änderungen wird der Gegenstand der Anmeldung nicht erweitert.


4.    Die Erfindung liegt auf technischem Gebiet (§ 1 Abs. 1 PatG). Es liegt auch
kein Ausschlusstatbestand nach § 1 Abs. 3 und 4 PatG vor.

                                      - 10 -



Bei der Prüfung, ob ein Ausschlusstatbestand gemäß § 1 Abs. 3 und 4 PatG vorliegt, ist darauf abzustellen, ob ein konkretes technisches Problem mit technischen
Mitteln gelöst wird, vgl. BGH Xa ZB 20/08, GRUR 2010, 613 - Dynamische Dokumentengenerierung, BGH X ZR 121/09, GRUR 2011, 610 - Webseitenanzeige.


Durch die Lehre der Anmeldung wird die technische Aufgabe gelöst, in Bilddaten
(von einem physikalischen Objekt aufgenommenen Messdaten) bestimmte Muster
(Knötchen) automatisch zu erkennen. In die Lösung dieser Aufgabe fließen technische Überlegungen über die Strukturen in den Bildern und die diesen zugrunde
liegenden physikalischen Objekte ein (die zu extrahierenden Knötchen sind entweder isoliert oder nur einseitig mit anderen Mustern, etwa Gefäßen verbunden, sie
können daher durch Schnitte mit geeigneten Masken identifiziert werden).


5.    Das System gemäß Anspruch 1 und ebenso das Verfahren gemäß dem
nebengeordneten Anspruch 4 sind neu gegenüber dem durch die Druckschrift D1
belegten Stand der Technik und beruhen auf erfinderischer Tätigkeit.


D1 betrifft die automatische Detektion kleiner Lungenknötchen in CT-Bilddaten. In
einem ersten Schritt wird das Lungengewebe extrahiert, vgl. Kapitel A auf S. 250f.
In einem zweiten Schritt werden hieraus über lokale Schwellenwerte Kandidaten
für Knötchen gewonnen (Knötchen haben dichteres Gewebe als normales Lungengewebe), vgl. Kapitel B auf S. 251f. Die hierdurch gewonnenen Kandidaten
umfassen nicht nur Knötchen, sondern beispielsweise auch Gefäße. Knötchen
und Gefäße werden in einem dritten Schritt identifiziert und die Gefäße aus der
Kandidatenliste entfernt, vgl. Kapitel C auf S. 252f. Hierbei wird ausgenutzt, dass
sich Knötchen und Gefäße in ihrer Form stark voneinander unterscheiden; Knötchen sind ungefähr kugelförmig, während Gefäße röhrenförmig („tubular“) sind,
vgl. S. 252 Kap. C Abs. 1 drittle. und vorle. Satz. Zur Unterscheidung werden Abmessungen des Kandidatenobjekts und eines dieses umgebenden quaderförmigen Körpers („bounding box“) herangezogen, unter Anderem ein Volumenmaß,

                                       - 11 -



vgl. unter Kapitel C auf S. 252 und 253 Gl. (1) bis (4) mit der zugehörigen Beschreibung in Verbindung mit Fig. 4.


Somit ist in D1 (ebenso wie der vorliegenden Anmeldung) ein Verfahren beschrieben, um in 3D-Bilddaten Lungenknötchen zu finden, wobei anfängliche Kandidaten für Knötchen (entsprechend dem Vordergrundbild in der vorliegenden Anmeldung) über Schwellenwerte vom Hintergrund separiert werden. D1 zeigt jedoch in
eine andere Richtung als die vorliegende Anmeldung: Der in D1 zur Unterscheidung von Knötchen und Gefäßen verwendete Algorithmus beinhaltet die Abmessungen von Kandidatenobjekten und von diese umgebenden, individuell an das
jeweilige Kandidatenobjekt angepassten quaderförmigen Körpern bzw. Masken.
Irgendein Hinweis auf die Erstellung von Schnitten mit einer Maske und deren
Auswertung ist D1 nicht zu entnehmen.


Das System gemäß Anspruch 1 war somit aus der Druckschrift D1 weder vorbekannt, noch war es durch diese nahegelegt. Ohne Hinweis und Anregung im Stand
der Technik war dies auch für den Fachmann nicht von sich aus naheliegend.


Durch die vorliegende Patentanmeldung werden vorteilhaft ein System und ein
Verfahren bereitgestellt, die eine einfache und schnelle Erkennung von Kandidaten für Knötchen in medizinischen Bilddaten erlauben.


Es ist daher anzuerkennen, dass das System nach Patentanspruch 1 nicht nur
neu ist, sondern auch auf erfinderischer Tätigkeit beruht.


Entsprechendes gilt für den nebengeordneten Anspruch 4.


6.     Der Anspruch 1 und ebenso der nebengeordnete Anspruch 4 sind gewährbar.

                                      - 12 -



Die abhängigen Ansprüche 2 und 3 beinhalten zweckmäßige, nicht selbstverständliche Ausgestaltungen des Systems nach Patentanspruch 1 und sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.




Dr. Fritsch              Eder              Dr. Thum-Rung                  Dr. Forkel




                                                                                 Fa
