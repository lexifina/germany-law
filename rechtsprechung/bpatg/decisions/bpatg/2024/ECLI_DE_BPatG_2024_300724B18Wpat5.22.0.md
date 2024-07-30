---
ecli: "ECLI:DE:BPatG:2024:300724B18Wpat5.22.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 5/22"
decided: "2024-07-30"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=15&nr=44216&anz=391&pos=238&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2024-07-30_18_W-pat_5_22_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 5/22 vom 2024-07-30

## Entscheidung

BUNDESPATENTGERICHT


    18 W (pat) 5/22                                                  Verkündet am
 _______________________
                                                                     30. Juli 2024
    (Aktenzeichen)
                                                                           …




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 11 2019 001 310.6
…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 30. Juli 2024 durch den Vorsitzenden Richter Dipl.-
Phys. Dr. Morawek sowie die Richter Dr.-Ing. Flaschke, Dr. Nielsen und der
Richterin kraft Auftrags Dipl.-Phys. Dr. Schenkl




ECLI:DE:BPatG:2024:300724B18Wpat5.22.0

                                           -2-



beschlossen:

       Auf die Beschwerde der Anmelderin wird der Beschluss der
       Prüfungsstelle für Klasse G 06 V des Deutschen Patent- und
       Markenamts vom 20. Juli 2022 aufgehoben und das Patent mit der
       Bezeichnung „Systeme und Verfahren zum Reduzieren der Menge
       an Datenspeicher beim maschinellen Lernen“ auf der Grundlage
       folgender Unterlagen erteilt:

        - Patentansprüche 1 bis 14, übergeben in der heutigen
           mündlichen Verhandlung,

        - Beschreibungsseiten          1     bis   25,   eingegangen   am
           27. Oktober 2022,

        - 5 Seiten Zeichnungen mit Figuren 1 bis 4D, eingegangen am
           27. Oktober 2022.



                                       Gründe


                                            I.



Die vorliegende Patentanmeldung 11 2019 001 310.6 trägt die Bezeichnung

  „Systeme und Verfahren zum Reduzieren der Menge an Datenspeicher beim
                               maschinellen Lernen“

und geht aus einer PCT-Anmeldung hervor, die am 14. Februar 2019 unter
Inanspruchnahme einer US-amerikanischen Priorität vom 13. März 2018 (US
15/919,376) eingereicht und in englischer Sprache als WO 2019/177738 A1 und in
deutscher Sprache als DE 11 2019 001 310 T5 veröffentlicht worden ist. Die
Patentanmeldung, die das maschinelle Lernen im Fahrzeugbereich betrifft, wurde
mit Beschluss vom 20. Juli 2022 von der Prüfungsstelle für Klasse G 06 V des
Deutschen Patent- und Markenamts in der Anhörung zurückgewiesen. Die

                                         -3-



Prüfungsstelle hat ihren Zurückweisungsbeschluss sinngemäß damit begründet,
dass die Gegenstände der damals geltenden jeweiligen Patentansprüche 1 nach
Haupt- und Hilfsanträgen 1 bis 7 nicht auf einer erfinderischen Tätigkeit beruhten.



Dabei wurde auf die folgenden Druckschriften verwiesen:

  D1 Rozantsev, Artem; Lepetit, Vincent; Fua, Pascal: On Rendering Synthetic
      Images for Training an Object Detector. In: arXiv, 28. November 2014, URL:
      https://arxiv.org/abs/1411.7911v1

  D2 Alhaija, Hassan Abu, [et al.]: Augmented Reality Meets Deep Learning for
      Car Instance Segmentation in Urban Scenes. In: British machine vision
      conference. 2017.



Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.



Die Anmelderin beantragt zuletzt in der Verhandlung vom 30. Juli 2024

        den Beschluss der Prüfungsstelle für Klasse G 06 V des Deutschen Patentund Markenamts vom 20. Juli 2022 aufzuheben und ein Patent zu erteilen
        mit der Bezeichnung „Systeme und Verfahren zum Reduzieren der Menge
        an Datenspeicher beim maschinellen Lernen“ auf der Grundlage folgender
        Unterlagen:

         -   Patentansprüche 1 bis 14, übergeben in der heutigen
             mündlichen Verhandlung,

         -   Beschreibungsseiten     1    bis    25,   eingegangen      am
             27. Oktober 2022,

         -   5 Seiten Zeichnungen mit Figuren 1 bis 4D, eingegangen am
             27. Oktober 2022.

                                            -4-



Der Patentanspruch 1 lautet:

1.    Verfahren zum Reduzieren einer Größe von Maschinenlerndaten, die in einer
Fahrzeugspeichervorrichtung gespeichert sind, wobei das Verfahren aufweist:

Empfangen, durch einen Prozessor, von Daten, die ein dreidimensionales Modell
aufweisen; wobei das dreidimensionale Modell 3D-Daten sind, die durch einen oder
mehrere Sensoren erfasst werden,

Analysieren, durch den Prozessor, einer Szene innerhalb des dreidimensionalen
Modells, um ein interessierendes Objekt und ein oder mehrere zusätzliche Objekte
zu identifizieren;

Aufnehmen, durch den Prozessor, des interessierenden Objekts und des einen oder
der mehreren zusätzlichen Objekte als mehrere zweidimensionale Bilder;

Entfernen, durch den Prozessor, des einen oder der mehreren zusätzlichen Objekte
aus     den    mehreren      zweidimensionalen      Bildern,   um   mehrere    gecroppte
zweidimensionale Bilder des interessierenden Objekts zu erhalten;

Speichern, durch den Prozessor, der mehreren gecroppten zweidimensionalen
Bilder des interessierenden Objekts in der Fahrzeugspeichervorrichtung;

Empfangen, durch den Prozessor, eines Hintergrundbildes von einem Bildsensor,
wobei das Hintergrundbild einen Hintergrund aufweist, der das interessierende
Objekt in späteren Verfahrensschritten umgeben soll;

Kategorisieren, durch den Prozessor, des Hintergrundbildes anhand eines oder
mehrerer Attribute des Hintergrundes;

Hinzufügen, durch den Prozessor, eines ausgewählten Attributs zu den mehreren
gecroppten zweidimensionalen Bildern, wobei das ausgewählte Attribut zumindest
eines    von    einem     Wetterattribut,   einem    Beleuchtungsattribut     und   einem
Schattierungsattribut ist;

Synthetisieren, durch den Prozessor, eines oder mehrerer synthetisierter Bilder aus
den mehreren gecroppten zweidimensionalen Bildern mit hinzugefügtem Attribut
und dem Hintergrundbild; und

                                       -5-



Annotieren, durch den Prozessor, des einen oder der mehreren synthetisierten
Bilder mit der genauen Position des interessierenden Objekts.



Der nebengeordnete Patentanspruch 6 lautet:

6.    System zum Verringern einer Menge an Datenspeicher, der zum Beinhalten
von Trainingsdaten beim maschinellen Lernen verwendet wird, wobei das System
aufweist: einen Prozessor;

einen Bildsensor, der kommunikativ mit dem Prozessor gekoppelt ist, wobei der
Bildsensor mehrere Hintergrundbilder aufnimmt; und

ein nicht-flüchtiges, prozessorlesbares Speichermedium, wobei das nicht-flüchtige,
prozessorlesbare Speichermedium eine oder mehrere Programmierinstruktionen
aufweist, die, wenn sie ausgeführt werden, den Prozessor veranlassen zum:

Empfangen, durch den Prozessor, von Daten, die ein dreidimensionales Modell
aufweisen, wobei das dreidimensionale Modell 3D-Daten sind, die durch einen oder
mehrere Sensoren erfasst werden;

Analysieren, durch den Prozessor, einer Szene innerhalb des dreidimensionalen
Modells, um ein interessierendes Objekt und ein oder mehrere zusätzliche Objekte
zu identifizieren;

Aufnehmen, durch den Prozessor, des interessierenden Objekts und des einen oder
der mehreren zusätzlichen Objekte als mehrere zweidimensionale Bilder;

Entfernen, durch den Prozessor, des einen oder mehreren zusätzliche Objekte aus
den     mehreren     zweidimensionalen    Bildern,   um     mehrere     gecroppte
zweidimensionale Bilder des interessierenden Objekts zu erhalten;

Speichern, durch den Prozessor, der mehreren gecroppten zweidimensionalen
Bilder des interessierenden Objekts in einer Fahrzeugspeichervorrichtung;

Empfangen, durch den Prozessor, eines Hintergrundbildes von dem Bildsensor,
wobei das Hintergrundbild einen Hintergrund aufweist, der das interessierende
Objekt später umgeben soll;

                                         -6-



Kategorisieren, durch den Prozessor, des Hintergrundbildes anhand eines oder
mehrerer Attribute des Hintergrundes;

Hinzufügen, durch den Prozessor, eines ausgewählten Attributs zu den mehreren
gecroppten zweidimensionalen Bildern, wobei das ausgewählte Attribut zumindest
eines   von   einem    Wetterattribut,   einem   Beleuchtungsattribut   und   einem
Schattierungsattribut ist;

Synthetisieren, durch den Prozessor, eines oder mehrerer synthetisierter Bilder aus
den mehreren gecroppten zweidimensionalen Bildern mit hinzugefügtem Attribut
und dem Hintergrundbild; und

Annotieren, durch den Prozessor, des einen oder der mehreren synthetisierten
Bilder mit der genauen Position des interessierenden Objekts.



Der nebengeordnete Patentanspruch 11 lautet:

11. System zum Verringern einer Menge an Datenspeicher, der zum Beinhalten
von Trainingsdaten beim maschinellen Lernen verwendet wird, wobei das System
aufweist:

einen ersten Prozessor;

einen Bildsensor, der kommunikativ mit dem ersten Prozessor gekoppelt ist;

einen zweiten Prozessor, der extern von dem ersten Prozessor ist und
kommunikativ mit dem ersten Prozessor gekoppelt ist;

ein nicht-flüchtiges, prozessorlesbares Speichermedium, wobei das nicht-flüchtige,
prozessorlesbare Speichermedium eine oder mehrere Programmierinstruktionen
aufweist, die, wenn sie ausgeführt werden, den ersten Prozessor veranlassen zum:

Empfangen von Daten, die ein dreidimensionales Modell aufweisen, wobei das
dreidimensionale Modell 3D-Daten sind, die durch einen oder mehrere Sensoren
erfasst werden;

                                         -7-



Analysieren einer Szene innerhalb des dreidimensionalen Modells, um ein
interessierendes Objekt und ein oder mehrere zusätzliche Objekte zu identifizieren;
Aufnehmen des interessierenden Objekts und des einen oder der mehreren
zusätzlichen Objekte als mehrere zweidimensionale Bilder;

Senden der mehreren zweidimensionalen Bilder an den zweiten Prozessor;

Empfangen eines Signals von dem zweiten Prozessor, das anzeigt, dass die
mehreren zweidimensionalen Bilder realistische Bilder sind;

Entfernen des einen oder der mehreren zusätzlichen Objekte aus den mehreren
zweidimensionalen Bildern, um mehrere gecroppte zweidimensionale Bilder des
interessierenden Objekts zu erhalten;

Speichern    der     mehreren    gecroppten         zweidimensionalen     Bilder   des
interessierenden Objekts in einer Fahrzeugspeichervorrichtung;

Empfangen eines Hintergrundbildes von dem Bildsensor, wobei das Hintergrundbild
einen Hintergrund aufweist, der das interessierende Objekt später umgeben soll;

Kategorisieren des Hintergrundbildes anhand eines oder mehrerer Attribute des
Hintergrundes;

Hinzufügen   eines     ausgewählten     Attributs   zu   den   mehreren    gecroppten
zweidimensionalen Bildern, wobei das ausgewählte Attribut zumindest eines von
einem Wetterattribut, einem Beleuchtungsattribut und einem Schattierungsattribut
ist;

Synthetisieren eines oder mehrerer synthetisierter Bilder aus den mehreren
gecroppten zweidimensionalen Bildern mit hinzugefügtem Attribut und dem
Hintergrundbild; und

Annotieren des einen oder der mehreren synthetisierten Bilder mit der genauen
Position des interessierenden Objekts.



Wegen des Wortlauts der abhängigen Ansprüche 2 bis 5, 7 bis 10 und 12 bis 14
wird auf die Akte verwiesen.

                                               -8-




Die Beschwerdeführerin vertritt die Auffassung, dass die geltenden Ansprüche
zulässig und patentfähig sind.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                                II.



Die zulässige Beschwerde hat in der Sache Erfolg. Sie führt zur Aufhebung des
angefochtenen Beschlusses und zur Erteilung des nachgesuchten Patents. Denn
der zweifelsfrei gewerblich anwendbare Gegenstand des nunmehr geltenden
Patentbegehrens ist gegenüber dem im Verfahren befindlichen Stand der Technik
neu   und    beruht   auf   einer     erfinderischen     Tätigkeit.   Auch   die   weiteren
Voraussetzungen zur Patenterteilung sind erfüllt (§§ 1 bis 5, § 34 und § 38 PatG).



1.    Die   Patentanmeldung         betrifft    ein   Verfahren   zum   Reduzieren     des
Speicherplatzes, der für Trainingsdaten benötigt wird, die für maschinelles Lernen
verwendet werden, und betrifft im besonderen Systeme und Verfahren zum
Generieren zweidimensionaler Bilder aus dreidimensionalen Modellen, wobei die
zweidimensionalen Bilder als Trainingsdaten verwendet werden (vgl. DE 11 2019
001 310 T5, Abs. [0002]).

Üblicherweise     werden     in     den        bordeigenen   Computervorrichtungen      im
Zusammenhang mit maschinellem Lernen für autonome oder halbautonome
Fahrzeuge dreidimensionale Modelle gespeichert. Diese Art von Trainingsdaten
benötigen viel Speicherplatz und die Verarbeitung ist sehr rechenintensiv, was eine
effektive Nutzung für die bordeigenen Fahrzeugprozessoren schwierig gestaltet
(vgl. T5-Schrift, Abs. [0003]).

                                         -9-



2.    Ausgehend von diesem Hintergrund besteht das technische Problem darin,
Trainingsdaten zu generieren, welche einerseits weniger Speicherplatz benötigen
und andererseits eine effektivere Nutzung von bordeigenen Fahrzeugprozessoren
ermöglichen.



Diese Aufgabe wird gelöst durch das Verfahren gemäß Patentanspruch 1 und die
Systeme gemäß den Patentansprüchen 6 und 11. Der seitens des Senats mit einer
Merkmalgliederung versehene Patentanspruch 1 lautet wie folgt:

     M1.0   Verfahren zum Reduzieren einer Größe von Maschinenlerndaten, die in
            einer Fahrzeugspeichervorrichtung gespeichert sind, wobei das
            Verfahren aufweist:

     M1.1   Empfangen,     durch    einen      Prozessor,    von   Daten,     die   ein
            dreidimensionales Modell aufweisen; wobei das dreidimensionale
            Modell 3D-Daten sind, die durch einen oder mehrere Sensoren erfasst
            werden,

     M1.2   Analysieren, durch den Prozessor, einer Szene innerhalb des
            dreidimensionalen Modells, um ein interessierendes Objekt und ein
            oder mehrere zusätzliche Objekte zu identifizieren;

     M1.3   Aufnehmen, durch den Prozessor, des interessierenden Objekts und
            des einen oder der mehreren zusätzlichen Objekte als mehrere
            zweidimensionale Bilder;

     M1.4   Entfernen, durch den Prozessor, des einen oder der mehreren
            zusätzlichen Objekte aus den mehreren zweidimensionalen Bildern, um
            mehrere gecroppte zweidimensionale Bilder des interessierenden
            Objekts zu erhalten;

     M1.5   Speichern,   durch     den   Prozessor,    der    mehreren      gecroppten
            zweidimensionalen Bilder des interessierenden Objekts in der
            Fahrzeugspeichervorrichtung;

                                      - 10 -



     M1.6   Empfangen, durch den Prozessor, eines Hintergrundbildes von einem
            Bildsensor, wobei das Hintergrundbild einen Hintergrund aufweist, der
            das interessierende Objekt in späteren Verfahrensschritten umgeben
            soll;

     M1.7   Kategorisieren, durch den Prozessor, des Hintergrundbildes anhand
            eines oder mehrerer Attribute des Hintergrundes;

     M1.8   Hinzufügen, durch den Prozessor, eines ausgewählten Attributs zu den
            mehreren    gecroppten    zweidimensionalen      Bildern,   wobei   das
            ausgewählte Attribut zumindest eines von einem Wetterattribut, einem
            Beleuchtungsattribut und einem Schattierungsattribut ist;

     M1.9   Synthetisieren,   durch   den      Prozessor,   eines   oder   mehrerer
            synthetisierter Bilder aus den mehreren gecroppten zweidimensionalen
            Bildern mit hinzugefügtem Attribut und dem Hintergrundbild; und

     M1.10 Annotieren, durch den Prozessor, des einen oder der mehreren
            synthetisierten Bilder mit der genauen Position des interessierenden
            Objekts.



3.    Der zuständige Fachmann weist ein abgeschlossenes Hochschulstudium der
Fachrichtung Informatik oder Physik auf und verfügt über eine mehrjährige
Berufserfahrung auf dem Gebiet des maschinellen Lernens im Bereich des
autonomen Fahrens.

                                           - 11 -



4.   Die Merkmale des Patentanspruchs 1 bedürfen der Auslegung.

Das Verfahren zum Reduzieren der Größe von Maschinenlerndaten, die in einer
Fahrzeugspeichervorrichtung gespeichert sind (M1.0), weist mehrere Schritte auf:
Beim Empfangen des dreidimensionalen Modells (M1.1) handelt es sich um 3D-Daten, die durch ein oder mehrere Sensoren erfasst werden. Entsprechend dem
Merkmal M1.2 wird eine Szene analysiert. Beispielsweise ist dies eine
Straßenszene, welche von den Sensoren von autonom fahrenden Fahrzeugen
empfangen wird (vgl. T5-Schrift, Abs. [0035]).

Anschließend werden (virtuelle) zweidimensionale Bilder von dem interessierenden
Objekt mit den mehreren Objekten aus verschiedenen Winkeln und Zoom-Stufen
aufgenommen (vgl. Abs. [0009], M1.3), wobei im folgenden Cropping-Schritt
nurmehr Bilder des interessierenden Objekts übrigbleiben und gespeichert werden
(vgl. Fig. 4A, Abs. [0009], M1.4, M1.5).

                                       - 12 -



Die weiteren Verfahrensschritte betreffen das Hintergrundbild, welches empfangen
(M1.6) und anhand von einem oder mehreren Attributen des Hintergrundes
(Gebäude, Ampel, Straße, Wetter…) kategorisiert wird (vgl. Fig. 4B, [0044], M1.7).

Beim Hinzufügen des Attributs wird das gecroppte 2D-Bild in seinen Eigenschaften
wie Schattierungen oder Spiegelungen verändert (vgl. Fig. 4C, [0044], M1.8).

Ein synthetisiertes Bild entsteht durch die Fusion des gecroppten 2D-Bilds mit
hinzugefügtem Attribut (z.B. Regen) mit dem Hintergrundbild (vgl. Fig. 4D, [0049],
M1.9).

Die synthetisierten Bilder werden zuletzt mit der genauen Position des
interessierenden Objekts annotiert (vgl. Fig. 4D: BZ 422, Abs. [0050], M1.10).



5.   Die Änderungen in den zuletzt beantragten Patentansprüchen 1 bis 14 sind
zulässig (§38 PatG).

Die Merkmale des geltenden Patentanspruchs 1 sind durch die ursprünglichen
Patentansprüche 1 bis 6 sowie der ursprünglich eingereichten Beschreibung (vgl.
WO 2019/177738 A1, Abs. [0018], [0058], [0059]) in Verbindung mit den Figuren 4A
bis 4D als zur Erfindung zugehörend offenbart.

Die nebengeordneten Systemansprüche 6 und 11 wurden an den geänderten
Patentanspruch 1 angepasst.

Bezüglich der Änderungen in den abhängigen Ansprüchen 4, 9 und 13 wird auf die
ursprüngliche Offenbarung in Abs. [0046] der WO-Schrift hingewiesen.



6.   Der Gegenstand des Patentanspruchs 1 ist gegenüber dem im Verfahren
befindlichen Stand der Technik neu (§ 3 PatG).

Die Fachpublikation D1 (Rozantsev, Artem; Lepetit, Vincent; Fua, Pascal: On
Rendering Synthetic Images for Training an Object Detector) befasst sich mit einem
Verfahren zum Generieren von Maschinenlerndaten (vgl. Titel), welche durch die
Verwendung von 2D-Bilder (vgl. Fig. 1: background image) automatisch in der

                                       - 13 -



Größe reduziert sind. Da diese Maschinenlerndaten durch ihre reduzierte Größe
auch in einer Fahrzeugspeichervorrichtung gespeichert werden können, ist das
Merkmal M1.0 aus der Schrift D1 bekannt. Ebenso werden Daten, die ein
dreidimensionales Modell aufweisen, empfangen (vgl. Abstract: a coarse 3D model
of the target object; M1.1tw) und mehrere zweidimensionale 2D Bilder davon
aufgenommen und gespeichert (vgl. S. 4, oben: we can then change the position
and the orientation of the object in the images to generate arbitrary large synthetic
datasets with realistic imaging artifacts; M1.3tw, M1.5tw). Weiter werden
Hintergrundbilder empfangen (vgl. Fig. 1: background image; S. 8: Starting from a
background image; M1.6), welche unterschiedliche Attribute aufweisen (vgl. S. 12:
This dataset contains images of different planes seen against changing
backgrounds and under a variety of weather and lighting conditions; M1.7tw). Dem
gecroppten 2D-Bild werden Wetter und Beleuchtungsattribute hinzugefügt (vgl. S.
8: To find the set of parameters Θ that best corresponds to real image Xi, we look
for Θ(i) = argminΘ d(Xi, S(Θ, Bi)) … The capture parameters in Θ depend on viewing
conditions, such as lighting and weather conditions, M1.8). Anschließend wird ein
synthetisches Bild erstellt (vgl. Abstract: to generate an unlimited line of training
images of the object of interest in arbitrary 3D poses, which can then be used to
increase classification performances.A key insight of our approach is that the
synthetically generated images should be similar to real images, not in terms of
image quality, but rather in terms of features used during the detector training;
M1.9). Ein Annotieren der exakten Position des interessierenden Objekts liest der
Fachmann bei dem Verfahren mit (vgl. S. 4, unten: Given the prevalence of Machine
Learning based algorithms, capturing and annotating training images has become
a major issue, and sometimes a severe bottleneck when such images are hard to
acquire. M1.10).

Somit fehlen dem aus der D1 bekannten Gegenstand mehrere Merkmale: Die
gecroppten 2D-Bilder des interessierenden Objekts entstehen nicht aus 3D-Daten,
die durch Sensoren erfasst werden und eine Szene mit dem interessierenden
Objekt und ein oder mehreren zusätzlichen Objekten umfassen (M1.1Rest, M1.2).
Ebenso sind auf den zweidimensionalen Bilder keine zusätzlichen Objekte

                                         - 14 -



enthalten (M1.3Rest), welche im nachfolgenden Schritt entfernt werden (M1.4).
Zudem werden die Bilder nicht explizit in einer Fahrzeugspeichervorrichtung
gespeichert (M1.5Rest) und eine Kategorisierung der Hintergrundbilder anhand
verschiedener Attribute durchgeführt (M1.7Rest).

Der Gegenstand des Anspruchs 1 ist damit neu gegenüber der Druckschrift D1.



In der wissenschaftlichen Veröffentlichung D2 (Alhaija, H. A. et al.: Augmented
Reality Meets Deep Learning for Car Instance Segmentation in Urban Scenes) geht
es um ein Verfahren zum Generieren von Maschinenlerndaten (vgl. Fig. 1:
Obtaining synthetic training data). Durch die Reduzierung der 3D-Modelle in 2D-Bilder wird ebenfalls die Größe der Maschinenlerndaten reduziert. Da es sich um
ein Verfahren zur Fahrerunterstützung handelt, liest der Fachmann mit, dass die
Maschinenlerndaten in einer Fahrzeugspeichervorrichtung gespeichert sind (vgl.
Titel: Augmented Reality Meets Deep Learning for Car Instance Segmentation in
Urban Scenes; M1.0). Es wird ein 3D Modell empfangen (vgl. Fig. 2: Given a set of
3D car models; M1.1tw), das interessierende Objekt wird allerdings ohne weitere
Objekte aufgenommen und gespeichert (vgl. Fig. 2: Rendering, Rendered Image;
M1.3tw, M1.5). Ebenso werden Hintergrundbilder empfangen (vgl. Fig. 2:
Background Image; M1.6) und mit den 2D Bildern synthetisiert (vgl. Fig. 2:
Augmented Image; M1.9), wobei eine Annotation der Position des interessierenden
Objekts vorgenommen wird (vgl. S. 3: we believe that it constitutes an important
milestone towards the ultimate task of creating virtually infinite, diverse and realistic
datasets with ground truth annotations; M1.10).

Nicht bekannt aus der Publikation D2 sind die Merkmale, die sich durch das
Empfangen der von Sensoren erfassten 3D-Daten (M1.1Rest), welche eine 3D-Szene mit interessierendem Objekt und zusätzlichen Objekten beinhaltet,
entstehen, wie das Analysieren (M1.2) und das Entfernen bzw. Cropping (M1.3Rest,
M1.4). Zudem werden die Hintergrundbilder nicht kategorisiert (M1.7).

                                       - 15 -



Damit ist der Gegenstand des Patentanspruchs 1 auch neu gegenüber der Schrift
D2.



Somit sind keiner der im Verfahren befindlichen Druckschriften alle Merkmale des
Patentanspruchs 1 zu entnehmen. Der Gegenstand des Patentanspruchs 1 ist
daher neu gegenüber dem im Verfahren befindlichen Stand der Technik.



7.    Der Gegenstand des Patentanspruchs 1 beruht gegenüber dem im Verfahren
befindlichen Stand der Technik auch auf einer erfinderischen Tätigkeit (§ 4 PatG).

Im Unterschied zum im Verfahren befindlichen Stand der Technik (D1 und D2) wird
in der vorliegenden Anmeldung nicht allein mit einem 3D Modell des
interessierenden Objekts gearbeitet, sondern mit einer gesamten Szene, aus
welcher das interessierende Objekt und mindestens ein weiteres zusätzliches
Objekt identifiziert wird (M1.2). Anschließend werden vom interessierenden Objekt
inklusive der ein oder der mehreren Objekte mehrere zweidimensionale Bilder
aufgenommen.

Selbst wenn eine Identifizierung eines interessierenden Objekts aus einer realen
Straßenszene    eines   3D-Detektors     eines   autonom     fahrenden   Fahrzeugs,
beispielsweise ausgehend von der Druckschrift D2, noch nahegelegen haben mag,
trifft dies auf den nachfolgenden Schritt der Aufnahme der zweidimensionalen Bilder
nicht mehr zu. Das Aufnehmen der mehreren 2D-Bilder, auf denen das
interessierende Objekt mit den zusätzlichen Objekten abgebildet ist, sowie das
anschließende nötige Cropping der 2D-Bilder erweist sich als sehr aufwändig und
birgt die Problematik von durch zusätzlichen Objekten verdeckten Teilen des
interessierenden Objekts.



Damit steht fest, dass der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag
gegenüber dem im Verfahren befindlichen Stand der Technik auch auf einer
erfinderischen Tätigkeit beruht und damit patentfähig ist.

                                        - 16 -




8.   Die Gegenstände der nebengeordneten Patentansprüche 6 und 11 sind
ebenfalls patentfähig (§ 1 - 5 PatG).

Auch die Systeme der nebengeordneten Patentansprüche 6 und 11 weisen die
Programminstruktionen auf, die zur Patentfähigkeit des Patentanspruchs 1
beigetragen haben. In beiden Systemen werden mehrere zweidimensionale Bilder
vom interessierenden Objekt und ein oder mehreren zusätzlichen Objekten
aufgenommen. Somit sind diese Patentansprüche ebenfalls patentfähig.



9.   Die abhängigen Ansprüche 2 bis 5, 7 bis 10 und 12 bis 14 sind mit den
gewährbaren nebengeordneten Patentansprüche 1, 6 und 11 ebenfalls patentfähig.



10. Da die vorgelegten geltenden Unterlagen auch den weiteren Voraussetzungen
zur Patenterteilung (§§ 1, 2, 5, 34 PatG) genügen, war auf die Beschwerde der
Anmelderin der Zurückweisungsbeschluss der Prüfungsstelle für Klasse G 06 V des
Deutschen Patent- und Markenamts aufzuheben und ein Patent zu erteilen.

                                         - 17 -



                                          III.


                                Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
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
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
       die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind,
       oder
   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek               Dr. Flaschke            Dr. Nielsen      Dr. Schenkl
