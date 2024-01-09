---
ecli: "ECLI:DE:BPatG:2024:090124B17Wpat13.22.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 13/22"
decided: "2024-01-09"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=0&nr=43976&anz=391&pos=6&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2024-01-09_17_W-pat_13_22_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0037.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 17 W (pat) 13/22 vom 2024-01-09

## Entscheidung

BUNDESPATENTGERICHT


    17 W (pat) 13/22                                                   Verkündet am
 _______________________
                                                                       9. Januar 2024
     (Aktenzeichen)
                                                                             …




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2021 210 356.1
…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 9. Januar 2024 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, der Richterin Akintche, des Richters Dipl.-Phys.
Univ. Dr. Städele und des Richters Hofmeister


beschlossen:


    Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für
    Klasse G06T des Deutschen Patent- und Markenamts vom 18. Juli 2022
    aufgehoben und das Patent wird mit folgenden Unterlagen erteilt:




ECLI:DE:BPatG:2024:090124B17Wpat13.22.0

                                             -2-



         -       Patentansprüche 1 bis 12, wie am Anmeldetag eingereicht,
         -       Beschreibung Seiten 1 bis 26, eingegangen am 12. Juli 2022 und
         -       3 Blatt Zeichnungen mit Figuren 1 bis 5, wie am Anmeldetag eingereicht.




                                           Gründe


                                              I.


Die vorliegende Patentanmeldung ist am 17. September 2021 beim Deutschen
Patent- und Markenamt eingereicht worden. Sie trägt die Bezeichnung „Verfahren
und Einrichtung zur Segmentierung von Hochkontrastobjekten in Röntgenbildern“.


Die Patentanmeldung wurde am 18. Juli 2022 von der Prüfungsstelle für Klasse
G06T mit der Begründung zurückgewiesen, dass der Gegenstand des
Patentanspruchs 1 nicht als auf einer erfinderischen Tätigkeit (§ 4 PatG) beruhend
gelte.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Die Anmelderin stellt den Antrag,


     den Beschluss der Prüfungsstelle für Klasse G06T des Deutschen Patent- und
     Markenamts vom 18. Juli 2022 aufzuheben und das Patent auf Grundlage
     folgender Unterlagen zu erteilen:


             -     Patentansprüche 1 bis 12, wie am Anmeldetag eingereicht,
             -     Beschreibung Seiten 1 bis 26, eingegangen am 12. Juli 2022 und
             -     3 Blatt Zeichnungen mit Figuren 1 bis 5, wie am Anmeldetag
                   eingereicht.

                                          -3-




Das geltende Patentbegehren – hier bzgl. der Ansprüche 1 bis 6 mit
Merkmalsgliederungen versehen – lautet:


   M0     1. Computer-implementiertes Verfahren zur Segmentierung eines
          Hochkontrastobjekts in einem Röntgenbild, umfassend die Schritte:


   M1     durch eine Schnittstelle (2) empfangen eines Röntgenprojektionsbildes,
          wobei das Röntgenprojektionsbild eine Vielzahl von Pixeln umfasst,


   M2     durch einen Bildverarbeitungsprozessor (3) bestimmen für ein oder
          mehrere Pixel des empfangenen Röntgenprojektionsbildes, ob das
          jeweilige Pixel ein Schattenpixel ist, welches eine Projektionsabbildung
          eines Hochkontrast-Objekts darstellt,


   M3     erzeugen einer Hochkontrastobjekt-Segmentierung eines oder mehrerer
          Hochkontrastobjekte für das Röntgenprojektionsbild auf Grundlage der
          Schattenpixel,


   M4     wobei das Bestimmen von Schattenpixeln die folgenden Schritte umfasst:


        M4.1 für das jeweilige Pixel des empfangenen Röntgenprojektionsbildes
           bestimmen     eines   Verhältnisses    der    dem   Pixel   zuzuordnenden
           Streustrahlungs-Intensität     zu    der     dem    Pixel   zuzuordnenden
           Primärstrahlungs-Intensität,


        M4.2 vergleichen des Verhältnisses mit einem Streu-Primär-Schwellwert,


        M4.3 klassifizieren des Pixels, wobei das Pixel als Schattenpixel klassifiziert
           wird, falls das Verhältnis größer als der Streu-Primär-Schwellwert ist.

                                      -4-



2. Verfahren nach Anspruch 1, umfassend die folgenden zusätzlichen Schritte:
   ·   für mindestens zwei Pixel des empfangenen Röntgenprojektionsbildes
       oder eines Teilbereichs des empfangenen Röntgenprojektionsbildes
       bestimmen des Verhältnisses der dem jeweiligen Pixel zuzuordnenden
       Streustrahlungs-Intensität     zu    der   dem     Pixel     zuzuordnenden
       Primärstrahlungs-Intensität,
   ·   bestimmen eines Mittelwertes der für die mindestens zwei Pixel
       berechneten Verhältnisse,
   ·   bestimmen des Streu-Primär-Schwellwertes in Abhängigkeit von dem
       Mittelwert.


3. Verfahren nach einem der vorhergehenden Ansprüche, umfassend die
folgenden zusätzlichen Schritte:
   ·   für ein oder mehrere Pixel des empfangenen Röntgenprojektionsbildes
       bestimmen eines dem jeweiligen Pixel zuzuordnenden Primärstrahlungs-Linienintegrals,
   ·   bestimmen     eines      der   Bildumgebung      des    jeweiligen    Pixels
       zuzuordnenden Primärstrahlungs-Linienintegral-Mittelwerts,
   ·   bestimmen      einer     dem    Primärstrahlungs-Linienintegral-Mittelwert
       zuzuordnenden Standard-Abweichung,
   ·   bestimmen eines Bildumgebungs-Schwellwerts durch Summieren von
       Primärstrahlungs-Linienintegral-Mittelwert und Standard-Abweichung,
   ·   vergleichen        des    Primärstrahlungs-Linienintegrals      mit    dem
       Bildumgebungs-Schwellwert,
   ·   klassifizieren des jeweiligen Pixels, wobei das Pixel als Schattenpixel
       klassifiziert wird, falls das Primärstrahlungs-Linienintegral größer als der
       Bildumgebungs-Schwellwert und
   ·   das Verhältnis der dem Pixel zuzuordnenden Streustrahlungs-Intensität
       zu der dem Pixel zuzuordnenden Primärstrahlungs-Intensität größer als
       der Streu-Primär-Schwellwert ist.

                                       -5-



4. Verfahren nach einem der vorangehenden Ansprüche, umfassend die
folgenden zusätzlichen Schritte:
   ·   für ein oder mehrere Pixel des empfangenen Röntgenprojektionsbildes
       bestimmen eines dem jeweiligen Pixel zuzuordnenden Gesamt-Linienintegrals,
   ·   Vergleichen       des   Gesamt-Linienintegrals   mit   einem     Gesamt-Linienintegral-Schwellwert,
   ·   klassifizieren des jeweiligen Pixels als Schattenpixel nur, falls das
       Gesamt-Linienintegral größer als der Gesamt-Linienintegral-Schwellwert
       und
   ·   das Verhältnis der dem Pixel zuzuordnenden Streustrahlungs-Intensität
       zu der dem Pixel zuzuordnenden Primärstrahlungs-Intensität größer als
       der Streu-Primär-Schwellwert ist.


5. Verfahren nach einem der vorangehenden Ansprüche, umfassend die
folgenden zusätzlichen Schritte:
   ·   für ein oder mehrere Pixel des empfangenen Röntgenprojektionsbildes
       bestimmen eines dem Pixel zuzuordnenden Gesamt-Linienintegrals,
   ·   für das jeweilige Pixel des empfangenen Röntgenprojektionsbildes
       bestimmen      eines    dem    Pixel   zuzuordnenden   Primärstrahlungs-Linienintegrals,
   ·   Subtraktion       des   Gesamt-Linienintegrals   vom   Primärstrahlungs-Linienintegral,
   ·   Vergleichen des Ergebnisses der Subtraktion mit einem Differenz-Schwellwert,
   ·   klassifizieren des Pixels, wobei das Pixel als Schattenpixel klassifiziert
       wird, falls die Differenz größer als der Differenz-Schwellwert und das
       Verhältnis der dem Pixel zuzuordnenden Streustrahlungs-Intensität zu
       der dem Pixel zuzuordnenden Primärstrahlungs-Intensität größer als der
       Streu-Primär-Schwellwert ist.

                                      -6-



6. Verfahren nach einem der vorangehenden Ansprüche, umfassend einen oder
mehrere der folgenden zusätzlichen Schritte:
   ·   klassifizieren oder umklassifizieren eines Pixels des empfangenen
       Röntgenbildes als Schattenpixel, falls mehrere Pixel in der Bildumgebung
       des      Pixels   als   Schattenpixel    klassifiziert    sind   und   einen
       zusammenhängenden Bildbereich von Schattenpixeln bilden, der durch
       das Pixel unterbrochen wird,
   ·   klassifizieren oder umklassifizieren eines Pixels als kein Schattenpixel,
       falls mehrere Pixel in der Bildumgebung des Pixels nicht als Schattenpixel
       klassifiziert sind und einen zusammenhängenden Bildbereich von Nicht-Schattenpixeln bilden, der durch das Pixel unterbrochen wird,
   ·   vergrößern eines Bildbereiches von Pixeln, die als Schattenpixel
       klassifiziert sind und einen zusammenhängenden Bildbereich von
       Schattenpixeln bilden, oder verkleinern eines Bildbereiches von Pixeln,
       die als Schattenpixel klassifiziert sind und einen zusammenhängenden
       Bildbereich von Schattenpixeln bilden.


7. Verfahren nach einem der vorangehenden Ansprüche, wobei in Abhängigkeit
von einem Röntgenprojektionsbild und einer Klassifizierung von einem oder
mehreren Pixeln als Schattenpixel ein hinsichtlich von durch ein oder mehrere
Hochkontrastobjekte verursachten Bildfehlern verbessertes Projektionsbild
erzeugt wird.


8. Verfahren nach Anspruch 7, wobei ein Bilddatensatz umfassend eine Vielzahl
von      Röntgenprojektionsbildern          empfangen           wird,   für     die
Röntgenprojektionsbilder des Bilddatensatzes verbesserte Projektionsbilder
erzeugt werden, und in Abhängigkeit von den verbesserten Projektionsbildern
ein 3D Ergebnisbild rekonstruiert wird.

                                      -7-



   9. Computerprogramm-Produkt ausgebildet dazu, bei Ausführung auf einem
   Computer das Verfahren nach einem der vorangehenden Ansprüche
   durchzuführen.


   10. Computerlesbares Medium, auf dem ein Computerprogramm-Produkt nach
   Anspruch 9 gespeichert ist.


   11. Einrichtung zur Segmentierung eines Hochkontrastobjekts in einem
   Röntgenbild, eingerichtet zur Durchführung des Verfahrens nach einem der
   Ansprüche 1 bis 7, umfassend eine Schnittstelle (2) zum Empfangen eines
   Röntgenprojektionsbildes und einen Bildverarbeitungsprozessor (3) zum
   Bestimmen für Pixel des empfangenen Röntgenprojektionsbildes, ob das
   jeweilige Pixel ein Schattenpixel ist, welches eine Projektionsabbildung eines
   Hochkontrast-Objekts darstellt.


   12. Einrichtung nach Anspruch 11 eingerichtet zur Durchführung des Verfahrens
   nach Anspruch 8 zur Erzeugung eines hinsichtlich von durch ein oder mehrere
   Hochkontrastobjekte verursachten Bildfehlern verbesserten 3D Ergebnisbildes.




Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt wurden folgende
Druckschriften eingeführt:


   D1:       GJESTEBY, Lars, et al. Metal artifact reduction in CT: where are we
       after four decades?. IEEE Access, 2016, 4. Jg., S. 5826-5849.


   D2:       GLOVER, G. H.: Compton scatter in CT reconstructions. In: Medical
       Physics, Vol. 9, 1982, No. 6, S. 860-867. - ISSN 0094-2405.


   D3:       PRELL, D.; KALENDER, W. A.; KYRIAKOU, Y. Development,
       implementation and evaluation of a dedicated metal artefact reduction

                                       -8-



      method for interventional flat-detector CT. The British journal of radiology,
      2010, 83. Jg., Nr. 996, S. 1052-1062.


Zu den weiteren Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie führt
zur Aufhebung des angefochtenen          Beschlusses und zur Erteilung des
nachgesuchten Patents. Die Gegenstände der nebengeordneten Patentansprüche
1 und 9 bis 12 sind jeweils patentfähig (§§ 1 bis 5 PatG); die geltenden Unterlagen
genügen auch den Anforderungen der §§ 34, 37 und 38 PatG.


1.    Die Anmeldung betrifft die Segmentierung von Hochkontrastobjekten in
Röntgenbildern (vgl. Abs. [0001] der Offenlegungsschrift, diese wird im Folgenden
„OS“ genannt).


Laut Beschreibung der Anmeldung kann es sich bei den Hochkontrastobjekten um
Metallobjekte handeln, die sog. Metallartefakte in den Röntgenbildern verursachen
(OS, Abs. [0002]).


Obwohl übliche Algorithmen zur Metallartefakt-Reduzierung wirksam seien,
bestehe nichtsdestotrotz der Bedarf, die Bildqualität weiter zu steigern.
Insbesondere     dann,   wenn   Metallobjekte   bei   der   3D-Rekonstruktion   von
Röntgenbildern teilweise oder ganz außerhalb des vollständig rekonstruierbaren
Volumens liegen, könnten die üblichen Algorithmen versagen. Der hauptsächliche
Grund hierfür bestehe darin, dass Pixel im Schatten von Metallobjekten, die
außerhalb des rekonstruierbaren Volumens liegen, nicht durch Segmentierung und
anschließende Vorwärts-Projektion der Metallobjekte bestimmt werden können
(OS, Abs. [0007]).

                                        -9-




Vor diesem Hintergrund stellt sich die Anmeldung die Aufgabe, die Segmentierung
von Hochkontrastobjekten in Röntgenprojektionsbildern (bzw. in Bilddatensätzen
von Röntgenprojektionsbildern für die 3D-Rekonstruktion) zuverlässiger zu machen,
und die Reduzierung von durch Hochkontrastobjekte verursachten Bildfehlern in
dreidimensional rekonstruierten Röntgenbildern zu verbessern (OS, Abs. [0008]).


Der für die Lösung der Aufgabe zuständige Fachmann weist ein Hochschulstudium
der Fachrichtung Elektrotechnik oder Physik auf und verfügt über eine mehrjährige
Berufserfahrung auf dem Gebiet der medizinischen Bildgebung, insbesondere im
Bereich der CT-Rekonstruktion.


2.    Einige der in der Anmeldung verwendeten Begriffe bedürfen der Erläuterung:


Unter Primärstrahlung ist Röntgenstrahlung zu verstehen, die geradlinig von der
Röntgenstrahlungsquelle zum Röntgenbilddetektor verläuft. Primärstrahlung, die
ein Objekt durchläuft, wird durch das Objekt abgeschwächt (OS, Abs. [0011]).


Unter Streustrahlung ist Röntgenstrahlung zu verstehen, die durch ein Objekt
abgelenkt (d.h. gestreut) wird. Streustrahlung verläuft also nicht geradlinig von der
Röntgenstrahlungsquelle zum Röntgenbilddetektor (OS Abs. [0011]).


In einem Detektorpixel, das durch seine Koordinaten (x, y) gekennzeichnet werden
kann, summieren sich die Intensitäten von Primärstrahlung (IP) und Streustrahlung
(IS) zur Gesamt-Intensität IT. Daraus ergibt sich die Helligkeit bzw. der Grauwert
des jeweiligen Bildpixels. Es gilt daher: IT(x,y) = IP(x,y) + IS(x,y) (OS, Abs. [0011]
und [0015]).


Das „Streu-zu-Primärstrahlungs-Verhältnis“ oder „Scatter-Primary-Ratio“, im
Folgenden als SPR bezeichnet, ist in der Anmeldung als Quotient IS(x,y) / IP(x,y)
definiert (OS, Abs. [0012] und [0019]). In den Ansprüchen wird für das SPR der

                                        - 10 -



Ausdruck „Verhältnis der dem Pixel zuzuordnenden Streustrahlungs-Intensität zu
der dem Pixel zuzuordnenden Primärstrahlungs-Intensität“ verwendet.


Ein Schattenpixel des Projektionsbilds wird in Merkmal M2 des Anspruchs 1
definiert als ein Pixel, „welches eine Projektionsabbildung eines Hochkontrast-Objekts darstellt“. Wie auch aus dem Kontext der vorliegenden Anmeldung
ersichtlich   (vgl.   OS,    Abs.    [0022]),    sind     Projektionsabbilder   eines
Hochkontrastobjekts bekanntermaßen von verhältnismäßig starker Streustrahlung
betroffen, d.h. der Anteil der Streustrahlungs-Intensität IS an der im Projektionsbild
abgebildeten Gesamt-Intensität IT ist gegenüber dem Anteil der Primärstrahlungs-Intensität IP groß, und zwar insbesondere - aber nicht ausschließlich - im vom
Hochkontrastobjekt abgeschatteten Pixelbereich. Bei der Rekonstruktion führen die
von verhältnismäßig starker Streustrahlung betroffenen Pixel zu Artefakten. Als
Schattenpixel im Sinne der vorliegenden Anmeldung sind somit Pixel eines
Projektionsbildes zu verstehen, deren Werte aufgrund von Streustrahlungseffekten
bei der Rekonstruktion zu Artefakten führen. Wie solche Pixel anspruchsgemäß
bestimmt werden, wird in den Merkmalen M4.1 bis M4.3 konkret definiert; demnach
soll ein Schattenpixel vorliegen, wenn ein SPR in diesem Pixel größer als ein
Schwellwert („Streu-Primär-Schwellwert“) ist.


3.      Der Anspruch 1 beschreibt sonach ein Verfahren, bei dem diejenigen Pixel
eines    Röntgenprojektionsbilds    rechnergestützt     als   ein   Hochkontrastobjekt
darstellende Schattenpixel klassifiziert werden (Merkmale M1, M2), deren SPR über
einem Schwellwert liegt (Merkmalsgruppe M4), wobei auf Basis der klassifizierten
Schattenpixel eines oder mehrere Hochkontrastobjekte segmentiert werden
(Merkmale M0, M3).


4.      Das geltende Patentbegehren ist zulässig gemäß § 38 PatG, da die
Änderungen in den Unterlagen lediglich die Darlegung des Standes der Technik und
offensichtliche Rechtschreibkorrekturen betreffen. Die vorliegenden Unterlagen
genügen auch den Anforderungen der §§ 34 und 37 PatG.

                                          - 11 -




5.     Die Gegenstände der nebengeordneten Patentansprüche 1 sowie 9 bis 12
sind jeweils neu und beruhen auf einer erfinderischen Tätigkeit.


5.1    Der Gegenstand von Anspruch 1 ist neu gegenüber der jeweiligen Lehre der
Druckschriften D1, D2 und D3.


5.1.1 Die D1 gibt einen Überblick über Verfahren zur Reduktion von
Metallartefakten in der Computertomographie (vgl. Titel; MAR = „Metal Artifact
Reduction“). Dabei werden die Verfahren in verschiedene Klassen und
Unterklassen eingeteilt, u.a. in die hier für die Beurteilung der Patentfähigkeit
relevante Klasse „D. Projection Completion“ und darin in die Unterklasse „1)
Interpolation“ (vgl. S. 5834 ff). Aus D1 ist - in Übereinstimmung mit der von der
Anmelderin genannten Aufgabe - bekannt, Metallbereiche in den Projektionsbildern
zuverlässig („reliable“) zu segmentieren (S. 5835 linke Spalte, dritter Absatz: „Unlike
prior methods that segment metal in the sinogram domain …“ bzw. S. 5836, rechte
Spalte oben „… projections [72]. Of course, the success of this technique is
dependent on a reliable segmentation of the metal objects.“). Dem Fachmann ist
klar, dass mit solchen Metallbereichen Bereiche starker Streustrahlung gemeint
sind, die mithin zu Artefakten bei der Rekonstruktion führen können (vgl. D1, S.
5826, rechte Spalte unten „Metal artifacts ... are caused by … most prominently …
scatter …“).


Somit entnimmt der Fachmann der D1 die Merkmale M0 bis M3.


Die D1 offenbart jedoch nicht, ein SPR eines Pixels als Klassifikationskriterium zu
verwenden. Damit fehlt die Merkmalsgruppe M4 in D1.


5.1.2 Die D2 untersucht Streustrahlungs-Effekte in der CT-Rekonstruktion (vgl.
Titel). Dabei wird mittels eines Detektors die Gesamtintensität It(x,y) = Is(x,y) + Ip(x,y)
hinter einem durchstrahlten Phantom gemessen, und mit einem zweiten „off-plane-

                                        - 12 -



measurement“ der Streustrahlungs-Anteil Is (vgl. S. 862, linke Spalte, zweiter
Absatz: „In this fashion, the detector could be positioned either to intercept the
transmitted x-ray beam as usual (to measure primary and scatter) or to measure
only scatter by placing the detector height above the fan beam plane.“ und S. 865,
linke Spalte, zweiter Absatz: „the off-plane measurement of scatter is a good
estimate of the transverse scatter“). In diesem Zusammenhang ist in Fig. 10 die
Größe Is / Ip (= SPR) dargestellt.


Zur Artefaktkorrektur wird in der Projektions-Domäne der Logarithmus der im
Detektor gemessenen Gesamtintensität It um den Wert Is / Ip korrigiert (vgl. Abschnitt
III.A, Überschrift „Scatter projections“ sowie letzter Absatz: „Correction for scatter
may be obtained by adding Is / Ip at each ray position to the corresponding
logarithmic attenuation data Xt“). Mit den derart korrigierten Projektionen wird
anschließend die Rekonstruktion vorgenommen (vgl. ebda. „Fig. 12 shows resulting
reconstructions …“).


Damit liefert die D2 zwar ein projektionsbasiertes MAR-Verfahren unter
Verwendung des SPR und zeigt somit die Merkmale M0, M1 und M4.1. Da aber in
der D2 die Projektionen mit dem SPR korrigiert („adding Is / Ip … to the … attenuation
data“, s.o.), und nicht, wie in der Erfindung, mittels des SPR segmentiert werden,
zeigt die D2 weder das Merkmal M2 noch die eine Segmentierung betreffenden
Merkmale M3, M4.2 und M4.3.


5.1.3 Die D3 stellt ein Verfahren vor, das zur Metallartefaktreduktion die
Rekonstruktions-Domäne verwendet (rekonstruktionsbasierte MAR). Hierzu wird
eine Segmentierung von Metallartefakten in einem - durch eine erste Rekonstruktion
von 2D-Projektionen erzeugten - 3D-Volumen durchgeführt und das 3D-Volumen
vorwärtsprojiziert. Dadurch entstehen Masken, die Metallartefakte in den 2D-Vorwärtsprojektionen anzeigen. Diese werden interpoliert, und die derart
modifizierten 2D-Vorwärtsprojektionen werden wieder rückprojiziert (S. 1053, linke
Spalte, zweiter und dritter Absatz). Da die D3 die Metall-Segmentierung zunächst

                                        - 13 -



in der 3D-Domäne durchführt (rekonstruktionsbasierte MAR), die Anmeldung
hingegen in der Projektions-Domäne (projektionsbasierte MAR) mittels eines SPR-Schwellwerts, fehlt in der D3 das Merkmal M3 („Segmentierung … für das
Röntgenprojektionsbild“). Zudem wird nicht anhand eines SPR segmentiert, sodass
der D3 zumindest auch die Merkmalsgruppe M4 nicht zu entnehmen ist.


5.2    Der Gegenstand des Anspruchs 1 wird durch den ermittelten Stand der
Technik auch nicht nahegelegt.


Auch wenn der Fachmann anhand der oben zu D1 genannten Fundstellen es in
Betracht ziehen würde, die Streustrahlung als Segmentierungskriterium zur
Segmentierung der Projektionsbilder zu verwenden, fehlt ihm nämlich ein Anlass,
ein SPR als Segmentierungskriterium (gemäß Merkmalsgruppe M4) zu verwenden.


Die D2 zeigt zwar in Fig. 10 eine SPR-Darstellung in der Projektionsdomäne mit
sichtbar   tiefdunklen   Bereichen,   die   wegen    ihrer   verhältnismäßig    hohen
Streustrahlungs-Werte zu Artefakten führen würden (s. Fig. 10 mit Bildunterschrift),
und damit das Merkmal M4.1. Jedoch beschäftigt sich die D2, wie oben dargelegt,
mit der Korrektur von Pixelwerten mittels des SPR und nicht mit der Segmentierung
von Bereichen mit hohen SPR-Werten. Daher hat der Fachmann keinen Anlass,
das in Figur 10 der D2 gezeigte SPR als Segmentierungskriterium zu verwenden.


Die D3 kann die erfinderische Tätigkeit nicht in Frage stellen, da sie eine andere
MAR-Klasse (rekonstruktionsbasierte MAR) als die Anmeldung (projektionsbasierte
MAR) betrifft, ferner Schwellwerte lehrt, die entweder fix oder von Intensitätswerten
rekonstruierter 3D-Bilddatensätze abgeleitet sind (vgl. S. 1053, Abschnitt „Detection
of metal implants“, erster und zweiter Absatz), und Streustrahlung allenfalls beiläufig
als Ursache für Metallartefakte erwähnt (vgl. u.a. S. 1052, linke Spalte; S. 1056,
rechte Spalte, zweiter Absatz).

                                     - 14 -



Die Druckschriften D1 bis D3 enthalten auch keine sonstigen Hinweise, anhand
derer der Fachmann in naheliegender Weise zum Gegenstand von Patentanspruch
1 gelangen würde.


5.3    Die nebengeordneten Ansprüche 9 bis 12 stützen sich auf den gewährbaren
Anspruch 1. Ihre Gegenstände sind daher ebenfalls neu und beruhen auf einer
erfinderischen Tätigkeit.


5.4    Auch die übrigen Voraussetzungen für die Patentfähigkeit gemäß §§ 1 bis 5
PatG sind erfüllt.

                                       - 15 -



                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1.    das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2.    bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
         Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
         Befangenheit mit Erfolg abgelehnt war,
   3.    einem Beteiligten das rechtliche Gehör versagt war,
   4.    ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
         war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
         stillschweigend zugestimmt hat,
   5.    der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
         der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
         sind, oder
   6.    der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe durch eine
beim Bundesgerichtshof zugelassene Rechtsanwältin oder durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt einzulegen.




 Dr. Morawek                   Akintche            Dr. Städele         Hofmeister
