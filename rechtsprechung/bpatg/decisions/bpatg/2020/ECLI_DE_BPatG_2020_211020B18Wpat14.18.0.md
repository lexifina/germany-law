---
ecli: "ECLI:DE:BPatG:2020:211020B18Wpat14.18.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 14/18"
decided: "2020-10-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=36&nr=40420&anz=666&pos=550&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2020-10-21_18_W-pat_14_18_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 18 W (pat) 14/18 vom 2020-10-21

## Entscheidung

BUNDESPATENTGERICHT


    18 W (pat) 14/18                                                Verkündet am
 _______________________
                                                                   21. Oktober 2020
     (Aktenzeichen)
                                                                           …




                                  BESCHLUSS

                             In der Beschwerdesache


                betreffend die Patentanmeldung 10 2015 113 434.9


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 21. Oktober 2020 durch den Richter Dipl.-Ing. Veit
als Vorsitzenden sowie den Richter Kruppa, die Richterin Dipl.-Phys. Zimmerer und
den Richter Dipl.-Ing. Altvater




ECLI:DE:BPatG:2020:211020B18Wpat14.18.0

                                        -2-



beschlossen:


                       Die Beschwerde wird zurückgewiesen.


                                     Gründe


                                          I.


Die am 14. August 2015 beim Deutschen Patent- und Markenamt eingereichte
Patentanmeldung 10 2015 113 434.9 nimmt die US-Prioriät 14/811,062 vom
28. Juli 2015 in Anspruch und trägt die Bezeichnung


               „Verfahren zur Objektlokalisierung und Posenschätzung
                          für ein interessierendes Objekt“.


Sie wurde durch Beschluss der Prüfungsstelle für Klasse G06K des Deutschen
Patent- und Markenamts vom 19. Juni 2018 aus Gründen des Prüfungsbescheids
(Ladungszusatz) vom 12. April 2018 zurückgewiesen, wonach sich der Gegenstand
des Anspruchs 1 in naheliegender Weise aus dem Stand der Technik gemäß
Druckschrift


      D1       Wu, Kanzhi et al.: A fast pipeline for textured object recognition in
               clutter using an RGB-D sensor. In: 2014 13th International Conference
               on Control, Automation, Robotics & Vision (ICARCV 2014). IEEE,
               2014. S. 1650-1655
ergebe.

                                        -3-



Gegen den vorstehend genannten Beschluss richtet sich die Beschwerde der
Anmelderin.


Sie beantragt mit Schriftsatz vom 17. Juli 2018 sinngemäß, den Beschluss der
Prüfungsstelle für Klasse G06K des Deutschen Patent- und Markenamts vom
19. Juni 2018 aufzuheben und das Patent gemäß Hauptantrag mit den
Patentansprüchen 1 bis 9, eingegangen am 13. März 2018, hilfsweise gemäß
Hilfsantrag mit den Patentansprüchen 1 bis 7, eingegangen am 17. Juli 2018, zu
erteilen.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 gemäß
Hauptantrag lautet:


       M1     „Verfahren (200) zum Lokalisieren und Schätzen einer Pose (287)
              eines bekannten Objekts (40, 205) im Blickfeld (35) eines
              Sichtsystems, wobei das bekannte Objekt (40, 205) eine strukturelle
              Entität enthält, die vordefinierte Merkmale aufweist, welche räumliche
              Abmessungen umfassen,


              wobei das Verfahren (200) umfasst, dass:


       M2     ein prozessorbasiertes Modell des bekannten Objekts (40, 205)
              entwickelt wird (300);
       M3     eine Bitmap-Bilddatei (25) aufgenommen wird, die ein Bild (15) des
              Blickfelds (35) enthält, das das bekannte Objekt (40, 205) enthält;
       M4     Merkmale (227) aus der Bitmap-Bilddatei (25) extrahiert werden (210);
       M5     die extrahierten Merkmale (227) mit Merkmalen abgeglichen werden
              (220), die dem Modell des bekannten Objekts (40, 205) zugeordnet
              sind;
       M6     anschließend ein Objekt in der Bitmap-Bilddatei (25) auf der
              Grundlage der extrahierten Merkmale (227) lokalisiert wird (230);

                                       -4-



      M7    die extrahierten Merkmale (227) des lokalisierten Objekts gruppiert
            werden (240);
      M8    die gruppierten extrahierten Merkmale (227) zusammengeführt
            werden (260);
      M9    das bekannte Objekt (40, 205) in dem Blickfeld (35) auf der Grundlage
            eines Vergleichs der zusammengeführten gruppierten extrahierten
            Merkmale (227) mit dem prozessorbasierten Modell des bekannten
            Objekts (40, 205) detektiert wird (270); und
      M10   eine Pose (287) des detektierten bekannten Objekts (40, 205) im
            Blickfeld (35) auf der Grundlage des Detektierens (270) des
            bekannten Objekts (40, 205) geschätzt wird (280).“


Wegen des Wortlauts der Patentansprüche 2 bis 9 gemäß Hauptantrag wird auf die
Akte verwiesen.


Patentanspruch 1 gemäß Hilfsantrag konkretisiert die Lokalisierung des Objekts
nach Merkmal M6 mit den Merkmalen M6.1 und M6.2, welche anschließend an
Merkmal M6 zusätzlich in den Patentanspruch 1 des Hauptantrags eingefügt sind:


      M6.1 „was umfasst, dass Merkmale in der Bitmap-Bilddatei (25) identifiziert
            werden, die Merkmalen des bekannten Objekts (40, 205) zugeordnet
            sind;
      M6.2 wobei das Identifizieren von Merkmalen in der Bitmap-Bilddatei (25),
            die Merkmalen des bekannten Objekts (40, 205) zugeordnet sind,
            ferner   umfasst,   dass   ein   digitales   Fenster   (237)    um   eine
            interessierende Region in der Bitmap-Bilddatei (25) eingepasst wird
            und dass Merkmale nur in einem Abschnitt der Bitmap-Bilddatei (25)
            innerhalb des digitalen Fensters (237) identifiziert werden;“


Wegen des Wortlauts der Patentansprüche 2 bis 7 gemäß Hilfsantrag wird auf die
Akte verwiesen.

                                       -5-



Die Beschwerdeführerin macht in ihrem Schriftsatz vom 17. Juli 2018 geltend, dass
die geänderten Anspruchsfassungen nach Haupt- und Hilfsantrag zulässig und die
Gegenstände der Patentansprüche im Lichte des Standes der Technik neu seien
und auf einer erfinderischen Tätigkeit beruhten.


Der Senat hat im Zusatz zur Ladung zur mündlichen Verhandlung vom 24. Juli 2020
unter anderem darauf hingewiesen, dass der Gegenstand des Patentanspruchs 1
nach Haupt- und Hilfsantrag dem Fachmann möglicherweise aus Druckschrift D1
nahegelegt ist.


Die Beschwerdeführerin hat, wie mit Schreiben vom 5. Oktober 2020 angekündigt,
an der mündlichen Verhandlung nicht teilgenommen.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                        II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg, da der jeweilige
Gegenstand des Patentanspruchs 1 nach Haupt- und Hilfsantrag nicht auf einer
erfinderischen Tätigkeit beruht (§ 4 PatG). Die Frage der Zulässigkeit des
Gegenstands der vorstehend genannten Patentansprüche kann daher dahinstehen
(vgl. BGH, Urteil X ZR 29/89 vom 18. September 1990, GRUR 1991, 120,121 li. Sp.
Abs. 3 – Elastische Bandage).


1. Die Anmeldung betrifft ein Sichtsystem und Verfahren zum Lokalisieren eines
   interessierenden Objekts und von dessen Pose (vgl. geltende Beschreibung,
   S. 1, erster Abs.).


   Die Anmeldung geht davon aus, dass bekannte Roboterwahrnehmungssysteme
   eine gewünschte Leistung und Zuverlässigkeit erreichten, indem spezielle

                                      -6-



Beleuchtungsbedingungen konstruiert würden, Sichtbedingungen strukturiert
würden und die Prozesskonfiguration ausgenutzt werde. Sie seien in einem
schmalen Bereich von Bedingungen flexibel, die nur in einer Teilmenge von
Bedingungen der realen Welt arbeiteten und sie könnten bei kleineren
Veränderungen in der sie umgebenden Umwelt versagen. Zudem reiche die
Verarbeitungsgeschwindigkeit     von    bekannten      Systemen   und   ähnlichen
Techniken für eine effiziente Verarbeitung in Echtzeit nicht aus. Schlüsselfertige
kommerzielle Sichtsysteme könnten langsam sein, wenn eine größere
Flexibilität eingeführt werde, und deren robustes Arbeiten werde erreicht, indem
der Arbeitsbereich rigoros strukturiert werde. Beispielsweise könne das
Verarbeiten eines großen Blickfelds (in englischer Sprache: field-of-view bzw.
FOV), um nach Objekten in nicht erwarteten Orientierungen zu suchen, die 5-
10% des Blickfelds belegen, mehrere Sekunden oder länger dauern. Dies werde
weiter   erschwert,    wenn    nach    Vorderansichten     /   Hinteransichten    /
Seitenansichten gesucht werde, um den Aufenthaltsort und die Pose eines
Objekts präzise zu finden. Darüber hinaus könnten Kosten, die mit dem
Strukturieren der Umgebungen für bekannte Automatisierungslösungen für
Robotermaterialtransfer- und Handhabungsanwendungen verbunden seien, das
Drei- bis Zehnfache der Kosten betragen, die mit der Robotervorrichtung
verbunden seien.


Der Bereich der Produkte, die effizient gehandhabt werden können, könne in
bekannten Automatisierungssystemen begrenzt sein und er sei oft auf nur eine
Handvoll von Typen eingeschränkt. Darüber hinaus seien derartige Systeme in
der Umrüstung mühsam und langsam beim Umkonfigurieren für eine andere
Klasse von Produkten. Folglich seien existierende Automatisierungslösungen
nicht einfach in Montageoperationen anwendbar, die sich mit einer großen
Diversität von Teilen beschäftigten, aufgrund von Problemen mit Bezug auf
Investitionen, Betriebskosten, Flexibilität und Umkonfigurierbarkeit (vgl. geltende
Beschreibung, S. 1, zw. Abs., bis S. 2, erster Abs).

                                       -7-



  Dem beanspruchten Verfahren nach Haupt- und Hilfsantrag liegt die Aufgabe
  zugrunde,   ein   Verfahren    zum    Identifizieren   und   Lokalisieren   eines
  interessierenden Objekts und von dessen Pose im Blickfeld eines Sichtsystems
  anzugeben (vgl. geltende Beschreibung, S. 2, Z. 7-10 i. V. m. S. 1, Z. 7-8).


  Der zuständige Fachmann weist ein abgeschlossenes Hochschulstudium der
  Fachrichtung Elektrotechnik oder Informationstechnik und eine mehrjährige
  Berufserfahrung auf dem Gebiet des maschinellen Sehens auf.


  Die vorstehend genannte Aufgabe soll nach Patentanspruch 1 des Haupt- und
  Hilfsantrags jeweils durch ein Verfahren zum Lokalisieren und Schätzen einer
  Pose eines bekannten Objekts im Blickfeld eines Sichtsystems gelöst werden.


2. Der Fachmann legt dem Anspruchsgegenstand des Patentanspruchs 1 nach
  Haupt- und Hilfsantrag das folgende Verständnis zugrunde:


  Der Patentanspruch 1 gemäß Hauptantrag sieht ein Verfahren zum Lokalisieren
  und Schätzen einer Pose eines bekannten Objekts im Blickfeld eines
  Sichtsystems vor, wobei das bekannte Objekt eine strukturelle Entität enthält,
  die vordefinierte Merkmale aufweist, welche räumliche Abmessungen umfassen
  (vgl.   Merkmal   M1).   Weitere     mögliche   physikalische   Merkmale       sind
  beispielsweise Materialien und Oberflächenbehandlungen (vgl. geltende
  Beschreibung S. 5, erster Abs., le. Satz).
  Das Verfahren umfasst nach Merkmal M2, dass ein prozessorbasiertes Modell
  des bekannten Objekts entwickelt wird. Die Anmeldung definiert den Begriff
  „Modell“ als einen auf einem Prozessor basierenden oder von einem Prozessor
  ausführbaren Code, der eine physikalische Existenz oder einen physikalischen
  Prozess simuliert (vgl. S. 6, zw. Abs., le. Satz). Der Modellaufbauprozess, der
  zu Figur 3 beschrieben ist, stellt ein Beispiel für das Entwickeln eines solchen
  Modells nach Merkmal M2 dar. Dieses Modell bildet die Grundlage, um ein
  bekanntes Objekt in einem aufgenommenen Bild zu erkennen.

                                     -8-



Das Verfahren umfasst nach Merkmal M3 das Aufnehmen einer Bitmap-Bilddatei, die ein Bild des Blickfelds (engl.: field-of-view bzw. FOV) enthält, das
das bekannte Objekt enthält. Beispiele für die Art der Bitmap-Bilddatei, welche
im vorliegenden Patentanspruch nicht festgelegt ist, nennt die Anmeldung auf
Seite 5 der geltenden Beschreibung (vgl. geltende Beschreibung, S. 5, zw. Abs.).
Die Bitmap-Bilddatei kann auch mehrere bekannte Objekte enthalten; sie
repräsentiert ein Originalbild des Blickfelds, wie es von der Kamera
aufgenommen wurde (vgl. geltende Beschreibung, S. 5, le. Satz).
Das Verfahren sieht nach Merkmal M4 vor, dass aus der aufgenommenen
Bitmap-Bilddatei Merkmale extrahiert werden. Der vorliegende Patentanspruch
lässt die Art und Anzahl der extrahierten Merkmale und die Maßnahmen zu ihrer
Extrahierung offen. So können in diesem Schritt beispielsweise alle lokalen
Merkmale extrahiert werden (vgl. geltende Beschreibung, S. 7, vorl. Abs.).
Die nach Merkmal M4 extrahierten Merkmale werden in einem Vergleichsschritt
(Merkmalsabgleich 220, vgl. Fig. 2 und geltende Beschreibung, S. 7-8,
seitenüberbr. Abs.) nach Merkmal M5 mit Merkmalen abgeglichen, die dem
Modell des bekannten Objekts zugeordnet sind. Dies bedeutet, dass aus den
extrahierten Merkmalen solche ermittelt werden, die in der Modellbeschreibung
dem bekannten Objekt zugeordnet werden können. Dieser Schritt stellt nicht das
Detektieren des Objekts selbst dar (vgl. Merkmal M9); es werden vielmehr nur
bekannte Merkmale aus der Modellbeschreibung des bekannten Objekts
identifiziert, aber nicht zueinander in Beziehung gesetzt (siehe dazu Merkmale
M6 bis M9). In diesem Verfahrensschritt können beispielsweise aus allen
extrahierten Merkmalen die Merkmale bestimmt werden, die jeweils einem der
bekannten Objekte zugeordnet werden können (vgl. geltende Beschreibung, S.
7-8, seitenüberbr. Abs.).
Auf der Grundlage der nach Merkmal M4 extrahierten Merkmale wird
anschließend nach Merkmal M6 ein Objekt in der Bitmap-Bilddatei lokalisiert.
Patentanspruch 1 stellt keinen Zusammenhang zwischen dem Ergebnis des
Abgleichs nach Merkmal M5 und dem Lokalisieren nach Merkmal M6 her;
Merkmal M6 nimmt vielmehr nur auf die extrahierte Merkmale nach Merkmal M4

                                    -9-



Bezug. Das Lokalisieren (engl.: localizing) ist in der vorliegenden Anmeldung
allgemein als Ortsbestimmung eines Objekts im Blickfeld des Sichtsystems zu
verstehen. Die Anmelderin hat in der Beschwerdebegründung eine engere
Auslegung des Begriffs „Lokalisieren“ verwendet, nach der ein Zusammenhang
zum    Beschränken     des   Bereichs     der    Bilddatei    bei    der     weiteren
Bilddatenverarbeitung herstellt wird, wozu die Anmeldung das Bestimmen einer
interessierenden Region (engl.: region of interest) in der Bilddatei beschreibt
(vgl. Beispiel zur „schnellen Objektlokalisierung“, geltende Beschreibung, S. 8,
zw. Abs.). Patentanspruch 1 des Hauptantrags benennt jedoch keine
entsprechenden Maßnahmen im Rahmen der Lokalisierung, sondern lässt die
dazu erforderlichen Maßnahmen offen. Diese folgen auch nicht zwangsläufig auf
Basis des Ergebnisses des Abgleichs nach Merkmal M5, da gemäß
Patentanspruch 1 nach Hauptantrag nur ein zeitlicher Zusammenhang zwischen
Merkmal M6 und Merkmal M5 besteht. Ungeachtet dessen setzt jede
Lokalisierung bekannter Objekte zwangsläufig einen Abgleich von erfassten
Bildmerkmalen mit bekannten Merkmalen voraus.
Die extrahierten Merkmale des lokalisierten Objekts werden gruppiert (vgl.
Merkmal M7) und zusammengeführt (vgl. Merkmal M8). Dies bedeutet, dass alle
Merkmale, die dem Objekt zugeordnet werden können, in einer nicht weiter
festgelegten   Weise    zusammengefasst         werden.      Im     Rahmen        eines
Anwendungsbeispiels beschreibt die Anmeldung, dass dies die Lockerung einer
Eins-zu-Eins-Übereinstimmung      umfasse,      die    ermögliche,         dass    der
Gruppierungsprozess ein bekanntes Objekt kombiniere und identifiziere,
welches wenige eindeutige Erscheinungsbildmerkmale aufweise (vgl. geltende
Beschreibung, S. 9, zw. Abs.). Der Schritt des Zusammenführens von Gruppen
umfasst das Zusammenführen mehrerer Gruppen, die eines der bekannten
Objekte überspannen, da Daten, die mit einem einzigen bekannten Objekt
verbunden sind, in mehreren Gruppen enthalten sein können (vgl. geltende
Beschreibung, S. 10, zw. Abs.).
Das Verfahren umfasst mit Merkmal M9 den Schritt, das bekannte Objekt
anhand des Vergleichs der zusammengeführten gruppierten extrahierten

                                   - 10 -



Merkmale mit dem prozessorbasierten Modell des bekannten Objekts zu
detektieren. Darunter versteht der Fachmann, dass das Objekt, das durch die
zusammengeführten gruppierten extrahierten Merkmale beschrieben ist, durch
Vergleich mit den Merkmalen des prozessorbasierten Modells des bekannten
Objekts identifiziert wird (vgl. Beispiel zur „feinen Objektdetektion“, geltende
Beschreibung, S. 10, zw. Abs.).
Schließlich umfasst das Verfahren nach Merkmal M10 das Schätzen der Pose
des detektierten bekannten Objekts auf der Grundlage des Detektierens dieses
bekannten Objekts nach Merkmal M9. Dieses Schätzen ist in der Anmeldung auf
Basis eines Ausführungsbeispiels im Zusammenhang mit der Modellbildung
näher beschrieben („Posenschätzung“, vgl. geltende Beschreibung, S. 11, zw.
Abs. und S. 12, erster Abs. i. V. m. S. 10, zw. Abs., sowie Beschreibung zu
Fig. 4, ab S. 13, le. Abs).


Der Patentanspruch 1 gemäß Hilfsantrag konkretisiert gegenüber der
Anspruchsfassung des Hauptantrags das Lokalisieren nach Merkmal M6
dahingehend, dass Merkmale in der Bitmap-Bilddatei identifiziert werden, die
den Merkmalen des bekannten Objekts zugeordnet sind (vgl. Merkmal M6.1).
Dabei umfasst dieses Identifizieren, dass ein digitales Fenster um eine
interessierende Region (engl.: region of interest) in der Bitmap-Bilddatei
eingepasst wird und dass Merkmale nur in einem Abschnitt der Bitmap-Bilddatei
innerhalb des digitalen Fensters identifiziert werden (vgl. Merkmal M6.2). Das
Lokalisieren bezieht sich jeweils auf Merkmale eines bekannten Objekts
(Merkmal M6.1), da sonst keine sinnvolle weitere Gruppierung und
Zusammenführung möglich ist (vgl. Ausführungen zu Merkmal M7 und M8 des
Hauptantrags). Das Identifizieren von Merkmalen in der Bitmap-Bilddatei,
welche Merkmalen des bekannten Objekts zugeordnet sind setzt voraus, dass
das digitale Fenster nach Merkmal M6.2 beim Lokalisieren festgelegt wird. Diese
Festlegung erfolgt vor dem Identifizieren, da das Identifizieren nur innerhalb
dieses Fensters erfolgen soll (vgl. Merkmal M6.2, letztes Teilmerkmal). Das
Identifizieren ist daher auch vom Abgleich nach Merkmal M5 zu unterscheiden,

                                          - 11 -



   da gemäß Merkmal M6 dieser Abgleich dem Lokalisieren vorausgeht
   („anschließend…“). Damit stellen auch die Merkmale M6.1 und M6.2 keinen
   inhaltlichen Zusammenhang zwischen Merkmal M6 und dem Ergebnis des
   Merkmalsabgleichs nach Merkmal M5 her.


3. Der Gegenstand des Patentanspruchs 1 nach Haupt- und Hilfsantrag beruht für
   den Fachmann in Kenntnis der Druckschrift D1 jeweils nicht auf einer
   erfinderischen Tätigkeit (§ 4 PatG).


   a) Zum Hauptantrag
   Aus Druckschrift D1 (Wu, Kanzhi et al.) ist ein Verfahren zum Lokalisieren und
   Schätzen einer Pose eines bekannten Objekts im Blickfeld eines Sichtsystems
   bekannt, wobei das bekannte Objekt eine strukturelle Entität enthält, die
   vordefinierte Merkmale aufweist, welche räumliche Abmessungen umfassen
   (…recognizing textured household objects in cluttered environment and
   estimating 6 DOF poses using an RGB-D sensor; vgl. Abstract / Merkmal M1).
   Das Verfahren umfasst das Entwickeln eines prozessorbasierten Modells des
   bekannten Objekts (…recognize objects and estimate related poses using only
   one RGB-D sensor given a set of object models; vgl. S. 1651, Abschnitt III.,
   erster Satz; sowie: Before the recognition procedures, the model for each object
   is created…; vgl. S. 1651, Abschnitt III.A., erster Abs. / Merkmal M2).
   Druckschrift D1 sieht vor, dass eine Bitmap-Bilddatei aufgenommen wird, welche
   ein Bild des Blickfelds enthält, das das bekannte Objekt enthält (The input
   information for each frame consists a color image … captured from Kinect; vgl.
   S. 1651, Abschnitt III.A., erster Abs., sowie Fig. 1 und Table 1 / Merkmal M3).
   Merkmale aus der Bitmap-Bilddatei werden extrahiert (feature extraction; vgl.
   S. 1652, Abschnitt III.B.2, erster Abs., sowie Fig. 1 / Merkmal M4). Die nach
   Merkmal M4 extrahierten Merkmale (features) werden mit Merkmalen
   abgeglichen, die dem Modell des bekannten Objekts zugeordnet sind (ﬁnding
   the matched correspondences … matches between observation and model; vgl.
   S. 1652, Abschnitt III.B.2, zw. Abs.; sowie: We match each type of features

                                      - 12 -



between an image in observation and an image in modeling; vgl. S. 1652,
Abschnitt III.B.2, dr. Abs. und Fig. 1 / Merkmal M5).


Da das Lokalisieren allgemein als Bestimmen des Ortes eines bekannten
Objekts in Bezug auf das in der Bilddatei erfasste Blickfeld des Sichtsystems zu
verstehen ist (vgl. Abschnitt II.2.), ist dies implizit Teil der Gruppierung und
Zusammenführung der Merkmale des extrahierten Objekts. Denn das
Gruppieren basiert auf der Nähe der Merkmale, welche durch Koordinaten – also
Ortsinformationen – beschrieben sind (we group geometrically closer features in
3D camera coordinate system; vgl. S. 1652, Abs. III.B.3, erster Satz, i. V. m.
feature coordinate … and corresponding 3D coordinate; vgl. S. 1652,
Abs. III.B.2, erster Abs.). Somit wird damit auch der Ort des Objekts näher
bestimmt – also das Objekt lokalisiert. Aber auch wenn man von der engeren
Auslegung     des     Merkmals     M6          durch   die   Anmelderin   in   der
Beschwerdebegründung        ausgeht     (vgl.     vorstehende   Ausführungen   zur
Auslegung des Merkmals), liest der Fachmann das Merkmal M6 in Abschnitt
III.B.1 auf Seite 1651 mit, da das Subtrahieren der Ebene (plane subtraction) auf
einem Extrahieren von Merkmalen (hier der Ebene) im Sinne von Merkmal M4
basiert. Dadurch erfolgt auch eine örtliche Bestimmung der Position des
erfassten Objekts in Bezug auf diese Ebene und damit ein Lokalisieren im Sinne
von Merkmal M6 (Merkmal M6).


Druckschrift D1 sieht weiter vor, dass die extrahierten Merkmale des lokalisierten
Objekts gruppiert (feature clustering; vgl. S. 1652, Abschnitt III.B.3, erster Abs.
und Fig. 1) / Merkmal M7) und zusammengeführt werden (vgl. S. 1652,
Abschnitt III.B.3, erster Abs., le. Satz, i. V. m. S. 1653, Abschnitt III.B.5 zu
method 1) / Merkmal M8). Dabei erfolgt das Detektieren des bekannten Objekts
anhand des Vergleichs der zusammengeführten gruppierten extrahierten
Merkmale mit dem prozessorbasierten Modell des bekannten Objekts (We rerank all the observed features in the cluster G … We verify all the other points
… we calculated the ﬁnal pose [R, t] again using all the correct matches; vgl.

                                    - 13 -



S. 1653, Abschnitt III.c, erster und dritter Abs. i. V. m. The goal of the proposed
system is to recognize objects and estimate related poses…, vgl. S. 1651,
Abschnitt III, erster Satz / Merkmal M9). In diesem Zusammenhang umfasst das
Verfahren auch das Schätzen der Pose des detektierten bekannten Objekts auf
der Grundlage des Detektierens dieses bekannten Objekts (…estimate related
poses, ebd. / Merkmal M10).


Im Unterschied zum beanspruchten Verfahren nach Hauptantrag erfolgt in
Druckschrift D1 eine Lokalisierung im Hinblick auf eine interessierende Region
(Support plane subtraction) im Sinne von Merkmal M6 vor einem Abgleich von
extrahierten Merkmalen (Feature extraction and matching, vgl. S. 1652, zw.
Abs.) mit den Merkmalen des Modells (vgl. Merkmal M5). Das Lokalisieren
erfolgt in Druckschrift D1 also auf Basis einer ermittelten Ebene (support plane)
aus den extrahierten Merkmalen der Bilddatei und nicht im Anschluss an den
Abgleich mit Merkmalen des Objekts nach Merkmal M5. Der Abgleich nach
Merkmal M5 bildet im beanspruchten Verfahren jedoch – wie vorstehend im
Rahmen der Auslegung dargelegt – nicht die Grundlage der Lokalisierung nach
Merkmal M6, da ein Berücksichtigen des Ergebnisses aus Merkmal M5 weder
in Merkmal M6 noch in den weiteren Anspruchsmerkmalen vorgesehen ist. Wie
die Lokalisierung nach Merkmal M6 umgesetzt wird, lässt der Patentanspruch 1
gemäß Hauptantrag offen.
Allein die zeitliche Abfolge von Merkmalslokalisierung im Sinne der Bestimmung
einer interessierenden Bildregion, dem Identifizieren bekannter Objekte und
dem Abgleich von Merkmalen kann eine erfinderische Tätigkeit nicht begründen.
Denn jede Bestimmung einer interessierenden Bildregion setzt ein Auswerten
der extrahierten Merkmale voraus. Ungeachtet, ob der Fachmann dazu
bekannte Objektmerkmale identifiziert oder Bildebenen, die nicht Teil von
Objekten sind, setzt dies zwangsläufig einen Abgleich entsprechender Daten
voraus.    Angesichts    der    Problemstellung,     eine    möglichst    schnelle
Objekterkennung zu ermöglichen, wird der Fachmann den Abgleichs- und
Lokalisierungsschritt abhängig vom Anwendungsfall so wählen, dass der

                                    - 14 -



Rechen- und damit Zeitaufwand minimiert wird. Die Wahl der zeitlichen Abfolge
eines Merkmalsabgleichs nach Merkmal M5 und einem Lokalisieren nach
Merkmal M6 in Anspruch 1 gemäß Hauptantrag, die den einzigen Unterschied
zum Stand der Technik nach Druckschrift D1 bildet, liegt daher im Rahmen des
fachmännischen Handelns und kann eine erfinderische Tätigkeit nicht
begründen.


Das Verfahren nach Anspruch 1 des Hauptantrags ist dem Fachmann daher
aus Druckschrift D1 nahegelegt und beruht nicht auf einer erfinderischen
Tätigkeit.


b) Zum Hilfsantrag
Der Patentanspruch 1 nach Hilfsantrag unterscheidet sich vom Hauptantrag in
der Konkretisierung des Verfahrensschrittes zur Lokalisierung nach Merkmal M6
durch die Merkmale M6.1 und M6.2.


Da der Fachmann das Lokalisieren nach Merkmal M6 allgemein als Bestimmen
des Ortes eines bekannten Objekts in Bezug auf das in der Bilddatei erfasste
Blickfeld des Sichtsystems versteht, ist dies bereits eine implizite Voraussetzung
für eine Gruppierung und Zusammenführung der Merkmale des extrahierten
Objekts (vgl. vorstehende Ausführungen zum Hauptantrag).
Dabei werden auch nach Druckschrift D1 implizit Merkmale in der Bitmap-Bilddatei identifiziert, die Merkmalen des bekannten Objekts zugeordnet sind
(…denotes the correspondence…; vgl. S. 1652, Abschnitt III.B.2, zw. Abs. /
Merkmal M6.1). Das Definieren einer interessierenden Region (region of
interest) erfolgt nach Druckschrift D1 durch das Subtrahieren der Ebene (plane
subtraction). Abweichend vom Verständnis der Anmelderin erkennt der
Fachmann darin sinngemäß das Festlegen eines digitalen Fensters hinsichtlich
einer verbleibenden, interessierenden Region (plane subtraction, S. 1651,
Abschnitt III.B.1), wobei der dadurch verbleibende Bereich – somit das „Fenster“
– in Druckschrift D1 als Maske bezeichnet wird (…using the generated mask

                                     - 15 -



image; vgl. S. 1652, Abschnitt III.B.2, erster Abs.). Denn aus Anspruch 1 gemäß
Hilfsantrag folgt nicht zwangsläufig, dass das Fenster zur Definition einer
interessierenden Region anhand von Merkmalen bekannter Objekte festgelegt
wird, insbesondere wird zur Definition des digitalen Fensters nach Merkmal M6.2
kein Zusammenhang zum Ergebnis eines Merkmalsabgleichs nach Merkmal M5
hergestellt. Damit lässt Anspruch 1 nach Hilfsantrag aber offen, ob eine
Abgrenzung       der   interessierenden   Region      anhand   von   identifizierten
Objektmerkmalen oder nicht zu den Objekten gehörenden Merkmalen der
Ebene wie in Druckschrift D1 bestimmt wird (Merkmal M6.2).


Dem Subtrahieren der Ebene geht notwendiger Weise wie bei der Festlegung
einer interessierenden Bildregion im beanspruchten Verfahren nach Hilfsantrag
(Merkmalsgruppe M6) das Extrahieren von Merkmalen im Sinne von Merkmal
M4 voraus.


Im Unterschied zu Druckschrift D1 sieht Anspruch 1 gemäß Hilfsantrag bereits
in Merkmal M5 einen Abgleich mit Merkmalen vor, die dem bekannten Objekt
zugeordnet sind, bevor der Schritt des Lokalisierens bzw. des Festlegens eines
digitalen Fensters erfolgt. Diese rein zeitliche Festlegung kann jedoch – wie
vorstehend zum Patentanspruch 1 des Hauptantrags ausgeführt – eine
erfinderische Tätigkeit nicht begründen, da das Ergebnis des Abgleichs nach
Merkmal M5 weder erkennbar die Lokalisierung nach der Merkmalsgruppe M6
bestimmt, noch den weiteren Verfahrensablauf beeinflusst.


Die   weiteren    Anspruchsmerkmale,      die   den    Anspruchsmerkmalen      des
Hauptantrags entsprechen, entnimmt der Fachmann Druckschrift D1. Es wird
hierzu auf die vorstehenden Ausführungen zum Hauptantrag verwiesen, die für
die entsprechenden übereinstimmenden Merkmale nach Anspruch 1 des
Hilfsantrags in gleicher Weise gelten.

                                       - 16 -



   Das Verfahren nach Anspruch 1 des Hilfsantrags ist dem Fachmann daher
   ebenfalls aus Druckschrift D1 nahegelegt und beruht nicht auf einer
   erfinderischen Tätigkeit.


4. Mit dem nicht patentfähigen Patentanspruch 1 nach Haupt- und Hilfsantrag sind
   auch die weiteren jeweiligen Patentansprüche nicht schutzfähig, da auf diese
   Patentansprüche kein eigenständiges Patentbegehren gerichtet ist (vgl. BGH,
   Beschluss vom 27. Juni 2007 – X ZB 6/05, GRUR 2007, 862, III. 3. a) aa)
   – Informationsübermittlungsverfahren II).


5. Nachdem die jeweiligen Anspruchssätze nach Haupt- und Hilfsantrag nicht
   schutzfähig sind, war die Beschwerde zurückzuweisen.




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

                                        - 17 -



   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
        die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind,
        oder
   6. der Beschluss nicht mit Gründen versehen ist.




Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




 Veit                       Kruppa               Zimmerer                   Altvater


                                                                                 prö
