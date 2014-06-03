---
ecli: "ECLI:DE:BPatG:2014:030614B17Wpat3.11.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 3/11"
decided: "2014-06-03"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=33&nr=26148&anz=1119&pos=504&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-06-03_17_W-pat_3_11_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 3/11 vom 2014-06-03

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 3/11                                                     Verkündet am
_______________                                                        3. Juni 2014
    (Aktenzeichen)                                                          …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 11 2005 000 205.5-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 3. Juni 2014 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,      der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                      -2-



beschlossen:


                    Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                       I.


Die vorliegende Patentanmeldung geht hervor aus einer PCT-Anmeldung (Veröffentlichungsnummer WO 2005/073918 A2), die am 18. Januar 2005 unter Inanspruchnahme der Prioritäten zweier US-Anmeldungen (die früheste vom 26. Januar 2004) eingereicht worden ist. Sie trägt in der deutschen Übersetzung die
Bezeichnung


    „System und Verfahren zur automatischen Knochenextraktion von einem
                              medizinischen Bild“.


Die Prüfungsstelle für Klasse G06T hat in der Anhörung am 15. September 2010
die Anmeldung zurückgewiesen, da der Patentanspruch 1 mangels Erfindungshöhe seines Gegenstands nicht gewährbar sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 10 vom 29. August 2010, eingegangen am
       31. August 2010,

                                         -3-



          noch anzupassende Beschreibung Seiten 1 bis 18 und
          6 Blatt   Zeichnungen   mit   Figuren 1   bis   6B,   jeweils   vom
          18. Juli 2006.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


          D1: J.S. Silva, A. Silva, B.S. Santos: „Lung Segmentation Methods in X-
          ray CT Images“, Proc. of the SIARP 2000 (5th Iberoamerican Symposium
          on Pattern Recognition), Seiten 583 bis 598

          D2: M. Fiebich et al: „Automatic Bone Segmentation Technique for CT
          Angiographic Studies“, Journal of Computer Assisted Tomography 23 (1),
          1999, Seiten 155 bis 161

          D3: US 2003/0142857 A1.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da der Gegenstand des Patentanspruchs 1
nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1
PatG).


1.       Die Patentanmeldung betrifft ein System und ein Verfahren zum automatischen Extrahieren einer Knochenstruktur aus einem medizinischen Bild.


Eine der Patentanmeldung zugrunde liegende Aufgabe ist nicht direkt angegeben.
Gemäß Abs. [0006] der DE 11 2005 000 205 T5 seien die automatischen Bildseg-

                                          -4-



mentierungstechniken, die bisher entwickelt worden sind, um Verbindungen zwischen Knochen und Blutgefäßen zu entfernen, für große Datenmengen oder eine
Hochgeschwindigkeitsanalyse nicht geeignet. Demgemäß bestehe ein Bedarf
nach einer Bildanalysetechnik, die ungewollte Objekte aus medizinischen Bilddaten ohne manuelle Interaktion extrahieren könne und die mit Hochgeschwindigkeit
arbeite.


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft
ein


           1. Verfahren zum automatischen Extrahieren einer Knochenstruktur aus
           einem medizinischen Bild mit folgenden Schritten:

           a) Durchführen einer Schwellwertberechnung auf jedem Voxel des medizinischen Bildes in einem Intensitätsbereich der Knochenstruktur, um eine
           erste Bitmaske zu erzeugen;

           b) Erodieren der ersten Bitmaske, um Verbindungen zwischen Blutgefäßen und der Knochenstruktur zu entfernen, um eine zweite Bitmaske zu
           erzeugen, wobei die Verbindungen innerhalb des Intensitätsbereichs liegen;

           c) Durchführen eines Bereichswachstums innerhalb der zweiten Bitmaske beginnend von einem Anfangspunkt (seed point) durch Anwachsen
           der Voxel in benachbarte Voxel innerhalb des Intensitätsbereichs, um die
           Knochenstruktur von unverbundenen Blutgefäßen zu trennen und um eine
           dritte Bitmaske zu erzeugen;

           d) Dilatation der dritten Bitmaske, um einen Oberflächenbereich der dritten Bitmaske wiederherzustellen, um eine vierte Bitmaske zu erzeugen;
           und

                                        -5-



        e) Durchführen eines Bereichswachstums innerhalb der vierten Bitmaske
        beginnend von dem Anfangspunkt durch Anwachsen in benachbarte Voxel
        innerhalb des Intensitätsbereichs, um eine fünfte Bitmaske zu erzeugen,
        die die Knochenstruktur darstellt.


Um aus medizinischen Bilddaten, die Knochen und Blutgefäße repräsentieren, die
Knochenstruktur zu extrahieren, werden gemäß der Lehre der Anmeldung folgende Schritte durchgeführt:


Zunächst wird auf dem Bild eine Schwellwertoperation ausgeführt, wobei die Bildpunkte, deren Intensitätswerte oberhalb des Schwellwerts liegen, markiert werden
(erste Bitmaske, Fig. 3A) – Merkmal a). In dem derart grob segmentierten Bild sind
außer Knochen auch andere Gewebebereiche markiert. Durch Erosion wird die
Markierung aller Bildpunkte entfernt, die nicht vollständig von markierten Bildpunkten umgeben sind (zweite Bitmaske, Fig. 3B), d. h. es werden die äußeren, an den
nicht segmentierten Bereich angrenzenden Punkte entfernt - Merkmal b). Danach
erfolgt ausgehend von einem Saatpunkt im Knochenbereich ein Bereichswachstum („region growing“); hierbei werden im Wesentlichen nur die zum Knochen
gehörigen Punkte erfasst, außerhalb des Knochens gelegene und nicht mit diesem verbundene markierte Bereiche werden entfernt (dritte Bitmaske) – Merkmal c). Durch Dilatation wird die bisher gefundene Struktur in ihren Randbereichen
expandiert (vierte Bitmaske), wobei die im Erosionsschritt verlorenen gegangenen
Außenbereiche des Knochens wieder hergestellt werden – Merkmal d). Durch die
Dilatation können an den Knochen angrenzende, zur Umgebung gehörende
Punkte fälschlicherweise als zum Knochen gehörig markiert werden (Abs. [0044]
letzter Satz in DE 11 2005 000 205 T5). Daher wird anschließend ein zweites, von
dem Knochen-Saatpunkt ausgehendes Bereichswachstum durchgeführt, wodurch
die Markierung nicht zum Knochen gehöriger Randpunkte entfernt wird (fünfte Bitmaske, Fig. 4A, 4B, 5B) – Merkmal e).

                                          -6-



Als Fachmann sieht der Senat hier einen Informatiker oder Physiker der Fachrichtung Bildverarbeitung an, der Erfahrung auf dem Gebiet der Segmentierung von
(insbesondere medizinischen) Bilddaten besitzt und dem die hierbei üblicherweise
eingesetzten Verfahren, etwa morphologische Operationen wie Erosion und Dilatation und ebenso Regionenwachstumsverfahren (englisch „region growing“) in
ihrem Ablauf und ihrer Wirkungsweise geläufig sind.


2.     Das Verfahren des Patentanspruchs 1 ist nicht patentfähig, da es nicht auf
erfinderischer Tätigkeit beruht.


2.1.   Als im Stand der Technik besonders relevant sieht der Senat die Druckschrift D3 an.


D3 beschreibt ein Verfahren zur schnellen und genauen Segmentierung von medizinischen Bildern (Abs. [0004], [0005]). Aus mittels Magnetresonanz gewonnenen
Bilddatensätzen (Wertepaare dualer Echo-Bilder) sollen bestimmte Strukturen
(Hirnflüssigkeit CSF, Gehirn, oder eine dieses umgebende Gesichtsstruktur) extrahiert werden. Fig. 2 zeigt den Verfahrensablauf: Für eine zu extrahierende Struktur
wird zunächst über eine Abfolge verschiedener Operationen (Medianfilter, Maximum-Intensity-Projektion MIP       der   beiden   Echobilder,   Histogrammerstellung
und -auswertung; Fig. 2 Schritte 220 bis 320, Fig. 3 bis 6 mit Beschreibung) ein
kreisringsegmentförmiger Wertebereich für die Bilddatenpaare bestimmt („annulus
region for tissue cluster (T2 window)“, Schritt 320). Anhand dieses durch mehrere
Parameter beschriebenen Wertebereichs (Abs. [0033] „four parameters“; Fig. 8,
10, 12) wird eine grobe Segmentierung durchgeführt (Abs. [0034]). Zur feineren
Segmentierung kann hierauf eine Kombination der Verfahrensschritte Erosion,
Regionenwachstum ausgehend von einem Saatpunkt in der Mitte der zu extrahierenden Struktur, sowie Dilatation (Schritte 330, 340, 350) angewendet werden.
Dadurch werden falsch klassifizierte Voxel entfernt, die ähnliche Werte wie die
gesuchte Struktur aufweisen, sich jedoch außerhalb der gesuchten Struktur befin-

                                      -7-



den (im Fall des zu segmentierenden Gehirns typischerweise im unteren Gesichtsbereich), vgl. Abs. [0035].


2.2.   Das Verfahren des Anspruchs 1 war angesichts des Standes der Technik
und im Lichte seines Fachwissens für den Fachmann naheliegend.


Welches technische Problem durch eine Erfindung gelöst wird, ist objektiv danach
zu bestimmen, was die Erfindung tatsächlich leistet (BGH GRUR 2005, 141 – Anbieten interaktiver Hilfe).
Die dem Patentanspruch 1 zugrunde liegende Lehre leistet es, aus medizinischen
Bilddaten, die eine Knochenstruktur und Blutgefäße darstellen, welche die Knochenstruktur zumindest teilweise eng umgeben können, die Knochenstruktur auf
relativ einfache und schnelle Weise zu extrahieren und sie dabei von den umgebenden Blutgefäßen im Wesentlichen vollständig zu trennen, und löst somit eine
entsprechende Aufgabe. Die medizinischen Bilddaten, welche dem Fachmann von
seinen Auftraggebern vorgegeben sind, sind hierbei der Aufgabe bzw. dem Problem selbst, nicht der Problemlösung zuzurechnen, vgl. BGH GRUR 2010,
44 - Dreinahtfolienschlauchbeutel.


Ein Fachmann, der vor die Aufgabe gestellt wird, in vorgegebenen medizinischen
Bilddaten bestimmte Strukturen zu extrahieren bzw. zu segmentieren, und der
hierfür ein einfaches und schnelles, aber dennoch genaues Verfahren entwickeln
will, sieht sich zu diesem Zweck im Segmentierungsverfahren betreffenden Stand
der Technik um. Als Ausgangspunkt wählt er ein ihm prinzipiell geeignet erscheinendes Verfahren aus, das er entsprechend seinen vorgegebenen Bilddaten anpasst bzw. abwandelt.
Im vorliegenden Fall, in welchem eine gesuchte Struktur (hier: Knochen) von einer
umgebenden, teilweise ähnliche Werte aufweisenden Struktur (hier: Blutgefäße)
getrennt werden soll, bot sich als möglicher Ausgangspunkt das Verfahren der D3
an, welches ebenfalls eine solche Trennung beinhaltet; diese Trennung erfolgt
durch eine Grobsegmentierung der Bilddaten anhand eines ermittelten Wertebe-

                                       -8-



reichs und eine anschließende Feinsegmentierung durch Anwenden der Schritte
Erosion, Regionenwachstum (wie der Fachmann mitlas, innerhalb des bei der Erosion gefundenen Bereichs) und Dilatation.
In D3, in welcher anhand von Wertepaaren mehrere Arten von gesuchten Strukturen voneinander und von einem Hintergrundbereich getrennt werden sollen, wird
zur Grobsegmentierung einer Struktur ein Wertebereich für die Wertepaare der
Struktur verwendet, der als Kreisringsegment in einer Polarkoordinatendarstellung
in Radius und Winkel begrenzt ist (Fig. 8, 10, 12). Wie der Fachmann ohne Weiteres erkannte, können mehrere Schwellwerte aus dem Rand eines solchen Wertebzw. Intensitätsbereichs zur Abtrennung der zugehörigen Struktur eingesetzt werden. Bereits damit ist Merkmal a) teilweise erfüllt. Im Übrigen wandelte der Fachmann dieses Grobsegmentierungsverfahren abhängig von den vorgegebenen
Bilddaten auch ab. War etwa in Bilddaten mit nur einem Intensitätswert pro Voxel
lediglich eine einzige, relativ hohe Werte aufweisende Struktur (Knochen) von
allem Übrigen zu trennen, so bot sich eine einzige Schwellwertoperation zur Einteilung in zwei Wertebereiche (Knochen / Sonstiges) an; dann ist ebenfalls Merkmal a) teilweise erfüllt.
Aus D3 Abs. [0035] ergaben sich die weiteren Schritte Erosion (welche den vorher
grob segmentierten Strukturbereich „schrumpft“ und dadurch schmale Verbindungen zu umgebenden Bereichen trennt sowie kleine isolierte Bereiche entfernt),
Regionenwachstum innerhalb des nach der Erosion vorliegenden Strukturbereichs
(welches ausgehend von einem Voxel im Inneren der bisher gefundenen Struktur
unter Berücksichtigung lokaler Intensitätswerte einen verbundenen Strukturbereich
extrahiert und dadurch isolierte, auch größere äußere Bereiche entfernt) und Dilatation (welche den bisher gefundenen, als gesuchte Struktur klassifizierten Bereich
um einen gewissen Abstand nach außen erweitert und dadurch die im Erosionsschritt verlorengegangenen Randbereiche der Struktur im Wesentlichen wiederherstellt; die Abfolge Erosion und Dilatation bewirkt zudem eine gewisse Glättung
des Strukturrandes) - teilweise Merkmale b), c) und d).

                                           -9-



Für den mit der Entwicklung eines Segmentierungsverfahrens befassten Fachmann lag es im Bereich routinemäßigen Handelns, sein Verfahren anhand mehrerer Bilddatensätze zu testen. Stellte er hierbei fest, dass durch die bisherigen Verfahrensschritte Blutgefäße zwar zum großen Teil entfernt werden, jedoch einige an
den Knochen angrenzende Bereiche fälschlicherweise als Knochen klassifiziert
werden (was offensichtlich auf die Dilatation zurückzuführen ist, welche den in den
vorherigen Schritten gefundenen Knochenbereich ohne Rücksicht auf Intensitätsabstufungen nach außen erweitert, und was der Fachmann zudem beim schrittweisen Testen des Verfahrens erkennen konnte), so trachtete er danach, auch
diese lokal auftretenden Bereiche zu entfernen. Hierfür bot sich als eine einfache
Möglichkeit ein nochmaliges Bereichswachstum an, wie es bereits in einem vorherigen Schritt zum Entfernen falsch klassifizierter Bereiche verwendet wurde (dort
nur innerhalb des vorher erodierten Knochenbereichs). Da hierbei dieselbe Knochenstruktur wie im vorherigen Bereichswachstumsschritt einem Bereichswachstum unterzogen wird, bot es sich an, von demselben, im Inneren dieser Struktur
gelegenen Saatpunkt auszugehen - teilweise Merkmal e).


Die Verwendung von Bitmasken zur Markierung der in den einzelnen Segmentierungsschritten gefundenen Bereiche war hierbei für den Fachmann selbstverständlich - restlicher Teil der Merkmale a), b), c), d), e).


Nach alledem beruht das Verfahren des Anspruchs 1 nicht auf erfinderischer Tätigkeit.


2.3.    Das Vorbringen der Anmelderin konnte nicht zu einer anderen Beurteilung
führen.


Die Anmelderin sieht insbesondere im letzten Verfahrensschritt (zweites Bereichswachstum, ausgehend vom selben Saatpunkt) eine erfinderische Tätigkeit gegeben. Für den Fachmann habe keine Veranlassung für einen solchen weiteren
Schritt bestanden. Im Stand der Technik sei kein Hinweis auf einen weiteren

                                       - 10 -



Bereichswachstumsschritt nach der Dilatation zu erkennen. Dieser Schritt sei nicht
isoliert zu betrachten, sondern vielmehr im technischen Zusammenhang mit den
übrigen Verfahrensschritten. Hierzu weist sie auf die BGH-Entscheidungen
„Papiermaschinengewebe“ (GRUR 2007, 1055) und „Einteilige Öse“ (GRUR 2010,
407) hin.


Dieser Argumentation war nicht zu folgen.


Wie der Bundesgerichtshof in der Entscheidung „Installiereinrichtung II“ (GRUR
2012, 378; Leitsatz und Kap. II.4) unter Bezugnahme auf die Entscheidungen
„Betrieb einer Sicherheitseinrichtung“ (GRUR 2009, 746) und              „Einteilige
Öse“ (a. a. O.) ausgeführt hat, ist es für die Beurteilung einer Erfindung als naheliegend erforderlich, dass der Fachmann Grund hatte, den Weg der Erfindung zu
beschreiten. Dazu bedarf es in der Regel über die Erkennbarkeit des technischen
Problems hinausreichender Anstöße, Anregungen, Hinweise oder sonstiger Anlässe. Dabei lässt sich keine allgemeine, vom jeweiligen Streitfall losgelöste Aussage
darüber treffen, in welchem Umfang und mit welcher Konkretisierung der Fachmann Anregungen im Stand der Technik benötigt, um eine bekannte Lösung in
bestimmter Weise weiterzuentwickeln. Es handelt sich vielmehr um eine Frage
des Einzelfalls, deren Beantwortung eine Gesamtbetrachtung aller maßgeblichen
Sachverhaltselemente erfordert. Dabei sind nicht etwa nur ausdrückliche Hinweise
an den Fachmann beachtlich. Vielmehr können Eigenarten des in Rede stehenden
technischen Fachgebiets, insbesondere Ausbildungsgang und Ausbildungsstand
der auf diesem Gebiet tätigen Fachleute zum Prioritätszeitpunkt und die auf dem
technischen Fachgebiet übliche Vorgehensweise von Fachleuten bei der Entwicklung von Neuerungen ebenso eine Rolle spielen wie technische Bedürfnisse, die
sich aus der Konstruktion oder der Anwendung des in Rede stehenden Gegenstands ergeben, nicht-technische Vorgaben, die geeignet sind, die Überlegungen
des Fachmanns in eine bestimmte Richtung zu lenken, und umgekehrt Gesichtspunkte, die dem Fachmann Veranlassung geben könnten, die technische Entwicklung in eine andere, von der Erfindung wegweisende Richtung voranzutreiben.

                                      - 11 -



Diese Ausführungen hat der Bundesgerichtshof in der jüngeren Entscheidung
„Farbversorgungssystem“ (X ZR 139/10 vom 11.03.2014) nochmals bekräftigt.


Wie oben erläutert, konnte der Fachmann im vorliegenden Fall im Rahmen seiner
üblichen Vorgehensweise bei der Entwicklung eines für vorgegebene Bilddaten
geeigneten Segmentierungsverfahrens (Wahl eines geeignet erscheinenden Ausgangsverfahrens und dessen Anpassung/Abwandlung entsprechend den vorgegebenen Bilddaten) zum Verfahren des Anspruchs 1 gelangen. Eine explizite Anregung im Stand der Technik, insbesondere für den auf die Dilatation folgenden
zweiten Bereichswachstumsschritt, war in diesem Fall nicht erforderlich.


Auch war zum Auffinden der anmeldungsgemäßen Lösung nicht notwendig, dass
der Fachmann von bisher beschrittenen Wegen abwich, etwa einen Wechsel des
Blickwinkels vornahm, was für das Vorliegen einer erfinderischen Tätigkeit sprechen könnte, vgl. die BGH-Entscheidung „Betrieb einer Sicherheitseinrichtung“ (a. a. O.).


Der oben dargelegten Beurteilung wurde der gesamte Anspruch 1 im technischen
Zusammenhang aller seiner Merkmale zugrunde gelegt, so dass auch die diesbezüglichen Anforderungen gemäß der BGH-Entscheidung „Papiermaschinengewebe“ (a. a. O.) erfüllt sind.


Der Anspruch 1 ist somit nicht gewährbar.


3.     Auch die übrigen Patentansprüche 2 bis 10 sind nicht gewährbar, da über
einen Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120
„Elektrisches Speicherheizgerät“).

                                            - 12 -



                                  Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


        1.   das beschließende Gericht nicht vorschriftsmäßig besetzt war,
        2.   bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
                Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
                Befangenheit mit Erfolg abgelehnt war,
        3.   einem Beteiligten das rechtliche Gehör versagt war,
        4.   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
                sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
        5.   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
                die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
                sind, oder
        6.   der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                   Eder               Dr. Thum-Rung                 Dr. Forkel




                                                                                        Fa
