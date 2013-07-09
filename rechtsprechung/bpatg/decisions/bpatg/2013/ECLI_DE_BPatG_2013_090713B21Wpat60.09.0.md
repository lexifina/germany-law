---
ecli: "ECLI:DE:BPatG:2013:090713B21Wpat60.09.0"
court: "Bundespatentgericht"
spruchkoerper: "21"
aktenzeichen: "21 W (pat) 60/09"
decided: "2013-07-09"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=41&nr=25078&anz=1167&pos=628&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-07-09_21_W-pat_60_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0046.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 21 W (pat) 60/09 vom 2013-07-09

## Entscheidung

BUNDESPATENTGERICHT



 21 W (pat) 60/09
_______________________

    (Aktenzeichen)




                             BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2007 028 270.4


…




hat der 21. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
9. Juli 2013 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Häußler
sowie der Richterin Hartlieb und der Richter Dipl.-Ing. Veit und Dipl.-Ing. Univ.
Schmidt-Bilkenroth




BPatG 152
08.05

                                        -2-



beschlossen:


    1. Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse A 61 B des Deutschen Patent- und Markenamts    vom    23. Januar 2009    aufgehoben       und   das      Patent
       10 2007 028 270 erteilt.


       Bezeichnung:    "Verfahren zur Segmentierung von Bilddaten zur
                       Erkennung einer Leber"


       Anmeldetag:     15. Juni 2007.


       Der Erteilung liegen folgende Unterlagen zugrunde:


       Patentansprüche 1 bis 23,         in   der   mit    Schriftsatz     vom
                                         12. Juni 2013 eingereichten Fassung


       Beschreibung, Seiten 1 bis 26,    in   der   mit    Schriftsatz     vom
                                         12. Juni 2013 eingereichten Fassung


       6 Blatt Zeichnungen, Figuren 1 bis 9, in der mit Eingabe vom
                                         29. Juni 2007 eingereichten Fassung


       1 Blatt Zeichnungen, Figur 10,    in der mit Schriftsatz vom 7. Juni
                                         2013 eingereichten Fassung.


    2. Die Rückzahlung der Beschwerdegebühr wird angeordnet.

                                       -3-



                                    Gründe


                                         I


Die Patentanmeldung mit dem Aktenzeichen 10 2007 028 270.4 ist am 15. Juni 2007 mit der Bezeichnung „Verfahren zur Segmentierung von Bilddaten zur Erkennung einer Leber“ beim Deutschen Patent- und Markenamt eingereicht und am
18. Dezember 2008 offengelegt worden.


Im Prüfungsverfahren sind die Druckschriften


      D1     US 2006/0147126 A1
      D2     GRADY, L.: Random Walks for Image Segmentation.
             In: IEEE Trans. on Pattern Analysis and Machine Intelligence,
             Vol. 28, Nr. 11, Nov. 2006, S. 1768-1783
      D3     DE 10 2006 047 373 A1
      D4     EP 1 750 226 A2


in Betracht gezogen worden.


Mit Beschluss vom 23. Januar 2009 hat die Prüfungsstelle für Klasse A 61 B die
Anmeldung zurückgewiesen. Dem Beschluss lagen die mit Eingabe vom 5. September 2008 eingereichten Patentansprüche 1 bis 28 zugrunde. In der Begründung ist ausgeführt, dass der Gegenstand des neu eingereichten Patentanspruchs 1 ebenso wie der des vorbeschiedenen ursprünglichen Patentanspruchs 1 nach wie vor nicht neu gegenüber der Druckschrift D2 sei. Im Übrigen
sei die hilfsweise beantragte Anhörung nicht sachdienlich.


Hiergegen richtet sich die Beschwerde der Anmelderin.

                                        -4-



Mit Schriftsatz vom 7. Juni 2013 reicht die Anmelderin u. a. eine neue Zeichnungsseite 7 mit der Figur 10 sowie Schriftsatz vom 12. Juni 2013 neue Patentansprüche 1 bis 23 und neue Beschreibungsseiten 1 bis 26 ein und beantragt,


         den angegriffenen Beschluss vom 23. Januar 2009 aufzuheben
         und das Patent zu erteilen auf der Grundlage der vorliegenden geänderten Unterlagen.


Der mit Schriftsatz vom 12. Juni 2013 eingereichte Patentanspruch 1 lautet gegliedert:


M1      Verfahren zur automatischen Segmentierung von Bilddaten zur Erkennung
        einer Leber von einem Untersuchungsobjekt, wobei die Bilddaten mehrere
        Bildpunkte umfassen, denen jeweils ein Signalwert zugeordnet ist, wobei
        das Verfahren umfasst:


M2      - automatisches Bestimmen von Bildpunkten (26-29), welche eine Rippe (25) darstellen, als Rippenbildpunkte (26-29),


M3      - automatisches Bestimmen von Bildpunkten (30), welche einen Bereich
          innerhalb eines Brustkorbs (38) eingrenzen, mit Hilfe der Rippenbildpunkte (26-29),


M4      - automatisches Bestimmen mindestens eines Bildpunkts (34), welcher einen Bildpunkt der Leber darstellt, als einen Leberbildpunkt innerhalb von
          Bildpunkten, welche sich in dem Bereich innerhalb des Brustkorbs (38)
          befinden,

                                            -5-



M5     - automatisches Definieren der Rippenbildpunkte (26-29) und der Bildpunkte (30), welche den Bereich innerhalb des Brustkorbs (38) eingrenzen, als Hintergrundsaatpunkte (26-30),


M6     - automatisches Definieren des mindestens einen Leberbildpunkts (34) als
            Lebersaatpunkte (34) und


M7     - Bestimmen einer Wahrscheinlichkeit für jeden Bildpunkt eines Bereichs
            innerhalb des Brustkorbs (38), ob der Bildpunkt zu der Leber gehört oder
            nicht, mit Hilfe eines Random Walker Verfahrens und der Lebersaatpunkte (34) und der Hintergrundsaatpunkte (26-30).


Der mit Schriftsatz vom 12. Juni 2013 eingereichte Patentanspruch 22 lautet gegliedert:


N1     Vorrichtung zur automatischen Segmentierung von Bilddaten zur Erkennung einer Leber von einem Untersuchungsobjekt, wobei die Bilddaten
       mehrere Bildpunkte umfassen, denen jeweils ein Signalwert zugeordnet ist,
       wobei die Vorrichtung umfasst:


N2     - ein Element zum automatischen Bestimmen von Bildpunkten (26-29),
            welche eine Rippe (25) darstellen, als Rippenbildpunkte (26-29),


N3     - ein Element zum automatischen Bestimmen von Bildpunkten (30), welche einen Bereich innerhalb eines Brustkorbs (38) eingrenzen, mit Hilfe
            der Rippenbildpunkte (26-29),


N4     - ein Element zum automatischen Bestimmen mindestens eines Bildpunkts
            (34), welcher einen Bildpunkt der Leber darstellt, als einen Leberbildpunkt (34) innerhalb von Bildpunkten, welche sich in dem Bereich innerhalb des Brustkorbs (38) befinden,

                                      -6-



N5    - ein Element zum automatischen Definieren der Rippenbildpunkte (26-29)
         und der Bildpunkte (30), welche den Bereich innerhalb des Brustkorbs
         (38) eingrenzen, als Hintergrundsaatpunkte (26-30),


N6    - ein Element zum automatischen Definieren des mindestens einen Leberbildpunkts (34) als Lebersaatpunkte (34), und


N7    - ein Element zum Bestimmen einer Wahrscheinlichkeit für jeden Bildpunkt
         eines Bereichs innerhalb des Brustkorbs, ob der Bildpunkt zu der Leber
         gehört oder nicht, mit Hilfe eines Random Walker Verfahrens und der Lebersaatpunkte (34) und der Hintergrundsaatpunkte (26-30).


Wegen der rückbezogenen Patentansprüche 2 bis 21 und 23 sowie der weiteren
Einzelheiten wird auf den Akteninhalt verwiesen.




                                        II


1. Die Beschwerde der Anmelderin ist zulässig und hat mit dem geänderten Patentbegehren Erfolg. Sie führt zur Aufhebung des angefochtenen Beschlusses und
zur Erteilung des Patents, denn das Verfahren mit den im Patentanspruch 1 angegebenen Merkmalen sowie die Vorrichtung nach dem nebengeordneten Anspruch 22 sind gegenüber dem Stand der Technik neu und ergeben sich für den
Fachmann aus diesem nicht in naheliegender Weise.


2. Die Anmeldung betrifft gemäß Beschreibung (siehe Offenlegungsschrift,
Abs. [0001]) ein Verfahren und eine Vorrichtung zur Segmentierung von Bilddaten
zur Erkennung einer Leber und insbesondere zur Segmentierung von Bilddaten
mit Hilfe eines Random-Walker-Verfahrens, wobei das Verfahren und die Vorrichtung als Zwischenschritt Bildpunkte der Bilddaten als Lebersaatpunkte (Liver Seed
Points) und Hintergrundsaatpunkte (Background Seed Points) bestimmt.

                                       -7-



Die Segmentierung von Bilddaten, beispielsweise von einem Computertomographen, zur Erkennung der Leber in einem Menschen, stellt einen grundlegenden
Vorverarbeitungsschritt für eine Reihe von medizinischen Anwendungen dar, beispielsweise bei einer Planung eines chirurgischen Eingriffs oder bei einer bildgeführten Leberbehandlung (siehe Offenlegungsschrift Abs. [0002]).
Eine automatische und genaue Segmentierung von Bilddaten zur Lebererkennung
bereitet jedoch eine Reihe von Problemen. So können Größe und Form der Leber
sehr unterschiedlich sein. Darüber hinaus können die Signalwerte, welche beispielsweise von einem Computertomographen erfasst werden, innerhalb der Leber und dem umgebenden Bereich in Abhängigkeit von zugrunde liegenden Abtastparametern und der Menge eines verabreichten Kontrastmittels über einen
großen Bereich variieren. Insbesondere an dem Übergang zwischen Lebergewebe
und Muskelgewebe zwischen den Rippen ist eine Segmentierung der Bilddaten
aufgrund der ähnlichen Röntgenabsorption des Lebergewebes und der Muskulatur
sehr schwierig. Darüber hinaus führen Tumore oder eine Fettlebererkrankung zu
stark unterschiedlichen Signalwerten von Computertomographiebilddaten innerhalb der Leber (siehe Offenlegungsschrift Abs. [0003]).
Ein allgemeines Verfahren zur Segmentierung von Bilddaten ist in der US
2006/0147126 A1 (= D1) offenbart, welches basierend auf einer Graphentheorie
eine Bilddatensegmentierung mit Hilfe des so genannten Random-Walker-Verfahrens durchführt. Das Random-Walker-Verfahren arbeitet derart, dass ein
Benutzer zunächst einige Bildpunkte mit Markierungen versieht. Mindestens ein
Bildpunkt, welcher sich innerhalb der Leber befindet, wird als ein Leberbildpunkt
(Liver Seed Point, Lebersaatpunkt) markiert und mindestens ein weiterer Bildpunkt, welcher nicht zur Leber gehört, wird als Hintergrundsaatpunkt (Background
Seed Point) markiert.
Eine Segmentierung der Bilddaten wird von dem Random-Walker-Verfahren dann
folgendermaßen bestimmt: Für einen jeden Bildpunkt wird die Wahrscheinlichkeit
berechnet, dass ein Random Walker (Zufallswanderer), welcher an diesem Bildpunkt startet, einen Bildpunkt mit einer Markierung erreicht. Die Richtung, in welcher sich der Random Walker bewegt, ist zufällig, wobei jedoch die Wahrschein-

                                       -8-



lichkeit für eine Bewegungsrichtung über Gewichte zwischen zwei benachbarten
Bildpunkten beeinflusst werden kann. Je ähnlicher sich zwei Bildpunkte sind (zum
Beispiel je ähnlicher die Signalwerte von zwei benachbarten Bildpunkten sind),
umso größer ist die Wahrscheinlichkeit, dass der Random Walker diesen Übergang wählt. Dem Bildpunkt wird dann die Markierung zugeordnet, welche die
größte Wahrscheinlichkeit aufweist (siehe Offenlegungsschrift Abs. [0004]).
Probleme des zuvor genannten Random-Walker-Verfahrens sind einerseits eine
geeignete Auswahl von Bildpunkten, welche mit höchster Wahrscheinlichkeit beispielsweise der Leber bzw. dem Hintergrund zugeordnet sind, automatisch zu bestimmen sowie eine geeignete Gewichtsfunktion bereitzustellen (siehe Offenlegungsschrift Abs. [0005]).


Der Anmeldung liegt daher die Aufgabe (siehe Offenlegungsschrift Abs. [0006])
zugrunde, ein Verfahren und eine Vorrichtung zur Segmentierung der Bilddaten
zur Erkennung einer Leber von einem Untersuchungsobjekt bereitzustellen, welche zuverlässig und automatisch Bildpunkte bestimmen, die entweder zur Leber
gehören oder zum Hintergrund gehören, und die mit Hilfe eines Random-Walker-Verfahrens und der Bildpunkte, die entweder zur Leber gehören (Lebersaatpunkte) oder die zum Hintergrund gehören (Hintergrundsaatpunkte) die Bilddaten segmentieren.


Als hier zuständigen Fachmann sieht der Senat einen Informatiker oder einen Ingenieur der Medizintechnik mit Universitätsstudium an, der über mehrjährige Berufserfahrung auf dem Gebiet der Bildverarbeitung und -analyse bei bildgebenden
medizinischen Systemen, insbesondere Computertomographen, verfügt.


3. Die Patentansprüche 1 bis 23 sind zulässig, da ihre Merkmale in den ursprünglichen Anmeldeunterlagen als zur Erfindung gehörend offenbart sind.

                                        -9-



Der Patentanspruch 1 geht aus dem ursprünglichen Anspruch 1 hervor und ist
demgegenüber dadurch geändert, dass das Wort „automatisch“ in den Merkmalen
M1 bis M6 eingefügt worden ist. Damit werden die zugehörigen Verfahrensschritte, die letztendlich zur automatischen Ermittlung von Leber- und Hintergrundsaatpunkt dienen, als Kern der Erfindung hervorgehoben. Als Stütze für die ursprüngliche Offenbarung wird auf die ursprüngliche Beschreibung, Seite 17 Zeile 22f. und
Seite 29 Zeile 30 (M1), Seite 20 Zeilen 11 bis 17 (M2), Seite 18 Zeile 30 bis Seite 21 Zeile 24 i. V. m. Fig. 2-6 (M3, M5) und Seite 21 Zeile 36 bis Seite 23 Zeile 12 i. V. m. Fig. 7-9 (M4, M6) verwiesen.


Entsprechend dieser Änderungen ist auch der nebengeordnete Patentanspruch 22, der aus dem ursprünglichen Anspruch 26 hervorgegangen ist, geändert
worden, wobei noch einzelne Bezugszeichen korrigiert worden sind.


Die Unteransprüche 2 bis 20 gehen aus den ursprünglichen Ansprüchen 2 bis 20,
der Unteranspruch 21 aus dem ursprünglichen Anspruch 25 und der Unteranspruch 23 aus dem ursprünglichen Anspruch 27 hervor, wobei neben redaktionellen Korrekturen in den Unteransprüchen 2, 3, 5 und 7 auch das Wort „automatisch“ passend zum Patentanspruch 1 eingefügt worden ist.


4. Das Verfahren nach Patentanspruch 1 ist nach Überzeugung des Senats
zweifelsohne gewerblich anwendbar und im Hinblick auf den vorliegenden Stand
der Technik auch patentfähig.


So ist der Gegenstand des Patentanspruchs 1 jedenfalls neu, denn aus keiner der
im Verfahren befindlichen Druckschriften ist ein Verfahren mit sämtlichen Merkmalen des Patentanspruchs 1 bekannt.


Der Gegenstand des Patentanspruchs 1 ergibt sich für den Fachmann auch nicht
in nahe liegender Weise aus dem vorliegenden Stand der Technik.

                                       - 10 -



Die als dem Gegenstand des Patentanspruchs 1 nächstkommend anzusehende
Druckschrift D2 beschreibt (siehe Abstract) ein interaktives Verfahren zur Segmentierung von Bilddaten (Pixels), wobei unter Pixel das grundlegende Bildelement im Zusammenhang mit seinem Intensitätswert verstanden wird (siehe Seite 1768 rechte Spalte zweiter Abs.) [= M1, abgesehen von der Zweckangabe „zur
Erkennung einer Leber“]. Ausgehend von einer kleinen Zahl von Bildpunkten, denen vom Bediener interaktiv oder vordefiniert Markierungen (Label) zugeordnet
wurden (das sind die sog. Saatpunkte), wird die Wahrscheinlichkeit bestimmt,
dass ein Zufallswanderer an jedem unmarkierten Punkt als erstes einen der markierten Pixel erreicht [= M7]. Dieses Verfahren beruht auf einer Graphentheorie,
wobei ein Graph ein Paar von Knoten und Kanten ist. Es geht von einem Graphen
mit einer festen Anzahl von Knoten und Kanten aus, wobei jeder Kante ein reeller
Wert, das sogenannte Gewicht, zugeordnet ist als die Wahrscheinlichkeit, mit der
ein Zufallswanderer diese Kante überqueren würde (siehe Seite 1768 rechte Spalte zweiter Abs.).
Zwar erwähnt die Druckschrift D2 an manchen Stellen, dass „markierte Bildpunkte“ als Saatpunkte auch automatisiert vorgegeben sein können (siehe z. B. Seite 1774 rechte Spalte letzte Zeile, Seite 1781 rechte Spalte zweiter Absatz), geht
aber darauf überhaupt nicht weiter ein. Vielmehr geht die Druckschrift D2 einfach
davon aus, dass solche Saatpunkte existieren, indem diese insbesondere durch
den Bediener interaktiv vorgegeben wurden (siehe Abstract, Seite 1768 linke Spalte letzter Absatz, Seite 1769 rechte Spalte vorletzter Absatz, Seite 1770 linke
Spalte erster Absatz und rechte Spalte letzter Absatz, Seite 1771 linke Spalte dritte Zeile, Seite 1773 rechte Spalte viertletzter Absatz, Seite 1774 rechte Spalte
letzte Zeile, Seite 1775 linke Spalte letzter Absatz und rechte Spalte erster Absatz), und erläutert im Einzelnen den darauf zugreifenden Random-Walker-Algorithmus.
Ein automatisches Bestimmen im Sinne der Merkmale M5 und M6 von Saatpunkten zeigt die Druckschrift D2 also nicht. Erst recht zeigt die Druckschrift D2 auch
nicht das automatische Bestimmen von Rippenbildpunkten [= M2], das automatische Bestimmen von Bildpunkten eines Bereichs innerhalb des Brustkorbs [M3]

                                       - 11 -



oder das automatische Bestimmen von Leberbildpunkten [= M4]. Auch die Seite 1775 mit der Fig. 2 und deren Bildunterschrift und Seite 1774 rechte Spalte letzter Absatz bis Seite 1775 linke Spalte in der Druckschrift D2 haben keinerlei Bezug zu Rippenbildpunkten, Bildpunkten innerhalb des Brustkorbs oder Leberbildpunkten.


Auch die übrigen Druckschriften D1, D3 und D4 führen den Fachmann nicht zum
Gegenstand des Patentanspruchs 1.


Die Druckschrift D1 beschreibt ein Verfahren zur Segmentierung von digitalisierten
Bilddaten auf der Grundlage des Random Walker Verfahrens und geht damit nicht
über das hinaus, was aus der Druckschrift D2 bekannt ist.


Die Druckschrift D3 beschreibt ein System und ein Verfahren zur Segmentierung
eines Objekts von Interesse aus einem medizinischen Bild, insbesondere eine
Segmentierungstechnik, um Zieltumorbereiche aus dreidimensionalen (3-D) Leber-CT-Bildern genau und deutlich zu kennzeichnen [= M1]. Das dort beschriebene Verfahren beruht auf einen Hintergrundmodellbilder und einen Vordergrundmodellbilder, die jedoch nur unter der Mitwirkung eines Benutzers in der Lage sind,
Intensitätsverteilungen der Voxel zur Segmentierung abzuschätzen, siehe Ansprüche 1, 2 und 4.


Die Druckschrift D4 schlägt ein Verfahren vor, das die Segmentierung für ein bereits vorab pre-segmentiertes Bild verbessern will. Dabei werden von einem Benutzer zusätzliche Vordergrund- oder Hintergrundsaatbilder hinzugefügt und weitere Werte als Vertrauensmaß eingegeben, aufgrund dessen unter Nutzung des
Random-Walker-Algorithmus das Segmentierungsergebnis verbessert wird.


Damit sind aus keiner der Druckschriften D1 bis D4 die Merkmale M2, M3, M4, M5
und M6 bekannt. Mangels entsprechender Hinweise werden diese Merkmale vom
vorliegenden Stand der Technik auch in Verbindung mit dem Fachwissen nicht

                                      - 12 -



nahegelegt, so dass nach Überzeugung des Senats der Gegenstand des Patentanspruchs 1 gegenüber den im Verfahren befindlichen Druckschriften als auf erfinderischer Tätigkeit beruhend anzusehen ist.


5. Auch der Gegenstand des Patentanspruchs 22 ist patentfähig.


Die Merkmale der Vorrichtung nach Patentanspruch 22 entsprechen inhaltlich
denjenigen Merkmalen des Verfahrens nach Patentanspruch 1.


Damit treffen die Ausführungen zur Patentfähigkeit des Gegenstands des Patentanspruchs 1 gleichermaßen auch auf die Patentfähigkeit des Gegenstands des
Patentanspruchs 22 zu.


6. Die Unteransprüche 2 bis 21 und der Unteranspruch 23 betreffen vorteilhafte
Ausgestaltungen des Gegenstands des Patentanspruchs 1 bzw. des Patentanspruchs 22.


Schließlich erfüllen auch die übrigen Unterlagen insgesamt die an sie zu stellenden Anforderungen.


7. Die Beschwerdegebühr ist zurückzuzahlen (§ 80 Abs. 3 PatG).


Die Rückzahlung der Beschwerdegebühr entspricht der Billigkeit, wenn bei ordnungsgemäßer und angemessener Sachbehandlung durch das Deutsche Patentund Markenamt die Erhebung der Beschwerde sowie die Einzahlung der Beschwerdegebühr hätten vermieden werden können (vgl. Schulte PatG, 8. Aufl.,
§ 80 Rdn. 110, § 73 Rdn. 124, 125).


So ist es billig, die Beschwerdegebühr zurückzuzahlen, wenn ein schwerwiegender Verfahrensverstoß vorliegt, wie z. B. die Verletzung rechtlichen Gehörs, insbesondere wenn die angefochtene Entscheidung darauf beruht, sie also möglicher-

                                        - 13 -



weise anders gelautet hätte, wäre das rechtliche Gehör gewährt worden (vgl.
Schulte a. a. O. § 73 Rdn. 132, 135).


Der Anspruch auf rechtliches Gehör umfasst auch das Recht des Anmelders, auf
schriftlichen Antrag im Rahmen einer Anhörung gehört zu werden, wenn dies
sachdienlich ist (§ 46 Abs. 1 Satz 2 und 3 PatG).


Die Rückzahlung der Beschwerdegebühr entspricht hier der Billigkeit, da die
Durchführung der von der Anmelderin beantragten Anhörung sachdienlich gewesen wäre (§ 46 Abs. 1 Satz 2 PatG). Eine einmalige Anhörung ist grundsätzlich in
jedem Verfahren sachdienlich (Schulte, PatG, 8. Aufl., § 46 Rdn. 8 sowie BPatG,
Beschluss vom 28. April 2009 – 21 W (pat) 41/05 m. w. N.). Sie ist immer sachdienlich, wenn sie das Verfahren fördern kann, insbesondere wenn eine mündliche
Erörterung eine schnellere und bessere Klärung als eine schriftliche Auseinandersetzung verspricht. Die Ablehnung eines Antrags auf Anhörung kommt nur in Betracht, wenn triftige Gründe dafür vorliegen (vgl. Schulte a. a. O., § 46, Rdn. 9).


Die Prüfungsstelle hat im Zurückweisungsbeschluss die beantragte Anhörung als
nicht sachdienlich abgelehnt, ohne dafür nähere Gründe zu nennen. Objektive
Gründe, die die Ablehnung eines Antrags auf Anhörung rechtfertigen können, sind
jedoch nicht ersichtlich. Insbesondere gab die Anmelderin keinen Anlass für die
Vermutung, durch die beantragte Anhörung das Verfahren lediglich verzögern zu
wollen. Vielmehr hat die Anmelderin in ihrer Eingabe auf den Erstbescheid einen
neuen Patentanspruch vorgelegt, zur Sache Stellung genommen sowie ihren Bedarf nach weiterer Erörterung für den Fall, dass die Prüfungsstelle weiterhin Bedenken bezüglich der Gewährbarkeit der vorgelegten Unterlagen haben sollte, klar
zum Ausdruck gebracht.


Bei einem solchen Verfahrensstand mit fortbestehenden Meinungsverschiedenheiten ist eine Anhörung sachdienlich, denn sie kann das Verfahren fördern, indem
der Anmelderin und dem Prüfer die Möglichkeit gegeben ist, ihre gegensätzlichen

                                    - 14 -



Auffassungen ausführlich in Rede und Gegenrede zu erörtern, etwa bestehende
Differenzen auszuräumen und so eventuell zu einem Einvernehmen bezüglich einer gewährbaren Anspruchsfassung zu gelangen. Dabei ist eine Anhörung in der
Regel auch dann sachdienlich, wenn der Anmelder unter Angabe von Gründen im
Einzelnen den mit dem einzigen Prüfungsbescheid geäußerten Bedenken der Prüfungsstelle gegen das Patentbegehren widerspricht und keine geänderten Patentansprüche vorgelegt werden (vgl. BPatGE 49, 111 - Anhörung im Prüfungsverfahren).


Damit leidet das Prüfungsverfahren an einem gravierenden Verfahrensfehler, der
auch ursächlich für die Beschwerdeeinlegung war. Denn bei fehlerfreier Sachbehandlung wäre die Beschwerde nicht zwangsläufig erforderlich geworden.




Dr. Häußler              Hartlieb              Veit        Schmidt-Bilkenroth


                                                                           Ko
