---
ecli: "ECLI:DE:BPatG:2004:171104B20Wpat16.03.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 16/03"
decided: "2004-11-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=121&nr=19595&anz=2061&pos=1820&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-11-17_20_W-pat_16_03_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 20 W (pat) 16/03 vom 2004-11-17

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 16/03                                                    Verkündet am
 _______________                                                  17. November 2004
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 100 43 318.9-42


…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 17. November 2004 durch den Richter
Dipl.-Phys. Dr. Hartung als Vorsitzenden sowie den Richter Dipl.-Ing. Obermayer,
die Richterin Martens und den Richter Dipl.-Phys. Dr. Zehendner




BPatG 154
6.70

                                          -2-



beschlossen:




         Der Beschluss des Patentamts vom 22. Februar 2002 wird aufgehoben und das Patent erteilt.


         Bezeichnung:     Verfahren zum automatischen Beschneiden eines
                          abgetasteten Bildes im Echtzeitbetrieb.


         Anmeldetag:      18. August 2000


         Der Erteilung liegen folgende Unterlagen zugrunde:


         Patentansprüche 1-15, überreicht in der mündlichen Verhandlung,
         Beschreibung Spalten 1-9, überreicht in der mündlichen Verhandlung,
         4 Blatt Zeichnungen, Figuren 1-6E (Seiten 1-7) wie Offenlegungsschrift.


                                         Gründe


                                            I.


Die Patentanmeldung wurde vom Patentamt aus den Gründen des Bescheids vom
18. Juni 2001 zurückgewiesen. Im Bescheid vom 18. Juni 2001 sind folgende
Druckschriften genannt:


   (1)       EP 703 696 A2
   (2)       EP 800 148 A2
   (3)       EP 949 802 A2

                                        -3-



Im Bescheid wird ausgeführt, dass diese Druckschriften zwar einzelne Merkmale
des Anmeldungsgegenstands offenbarten, der vollständige Anmeldungsgegenstand im Umfang des Patentanspruchs 1 aus (1) bis (3) jedoch nicht nahegelegt
erscheine. Der Patentanspruch 1 sei daher voraussichtlich gewährbar. Der nebengeordnete Patentanspruch 9 sei jedoch nicht gewährbar, da er keine vom Patentanspruch 1 verschiedene Lösung der gestellten Aufgabe erkennen lasse,
vielmehr seien seine Merkmale sinngemäße Wiederholungen der entsprechenden
Merkmale des Patentanspruchs 1. Außerdem sei der Stand der Technik in die Beschreibung aufzunehmen, die Aufgabenstellung zu überarbeiten und der letzte
Absatz der Beschreibung zu entfernen.


Die Anmelderin beantragt,


      den angefochtenen Beschluss aufzuheben und das Patent mit den
      in der mündlichen Verhandlung überreichten Unterlagen zu erteilen.


Der geltende Patentanspruch 1 lautet:


      "Verfahren zum automatischen Beschneiden eines abgetasteten
      Bildes im Echtzeitbetrieb, das folgende Schritte umfaßt:


      (a) sequentielles Lesen eines ersten sowie weiterer Teilbildblöcke
      aus einem Scanner, bis eine erste bedeutungstragende Bildregion
      aufgefunden wurde und anschließendes Speichern eines jeden
      Teilbildblocks in einer Speichereinrichtung des Scanners;


      (b) Aufzeichnen eines Attributs eines jeden Bildelements eines jeden Teilbildblocks in einem Speicherraum, bis die bedeutungstragende Bildregion aufgefunden wurde, wobei das Attribut anzeigt, ob
      ein Bildelement bedeutungstragend oder bedeutungslos ist;

                                 -4-



(c) Berechnen einer Position eines am weitesten links liegenden
Startbildelements und einer Position eines am weitesten rechts liegenden Endebildelements der ersten bedeutungstragenden Bildregion, nachdem die erste bedeutungstragende Bildregion aufgefunden wurde;


(d) Stichprobenentnahme einer Vielzahl von Zeilenbereichen innerhalb einer jeden bedeutungstragenden Bildregion, um die Position
einer Basiszeile des abgetasteten Bildes zu bestimmen;


(e) Berechnen der Breite der ersten bedeutungstragenden Bildregion auf Grundlage der Position des am weitesten links liegenden
Startbildelements und der Position des am weitesten rechts liegenden Endebildelements;


(f) Zurücksetzen der Abtastbreite des Scanners, um nachfolgende
Bilddaten in Antwort auf die in Schritt (e) berechnete Breite einzulesen;


(g) Einlesen aller nachfolgenden bedeutungstragenden Bildregionen, bis eine Basiszeile aufgefunden wurde, und direktes Einschreiben der gültigen Bilddaten eines jeden nachfolgenden Teilbildblocks in eine bitweise orientierte Datei und Aufsummieren der
Gesamtanzahl von Bildzeilen mit gültigen Bilddaten in einer jeden
nachfolgenden bedeutungstragenden Bildregion, oder Übertragen
der gültigen Bilddaten in ein übergeordnetes Bildverarbeitungsprogramm; und


(h) Einsetzen der Summe der Gesamtanzahl von Bildzeilen mit gültigen Bilddaten in einer jeden bedeutungstragenden Bildregion, als
Länge des abgetasteten Bildes und Einschreiben der Länge und

                                       -5-



      der Breite in den Anfangskennsatz der bitweise orientierten Datei,
      oder Senden eines Dateiendesignals an ein übergeordnetes Bildverarbeitungsprogramm, um das Einlesen der gültigen Bilddaten zu
      beenden."


Der nebengeordnete Patentanspruch 9 hat folgende Fassung:


      "Verfahren zum automatischen Beschneiden eines abgetasteten
      Bildes im Echtzeitbetrieb, das die Schritte umfaßt:


      (a) Suchen einer ersten bedeutungstragenden Bildregion innerhalb
      eines Teilbildblocks und Einschreiben der Bilddaten der ersten bedeutungstragenden Bildregion in eine bitweise orientierte Datei und
      Aufsummieren der Gesamtanzahl der Bildzeilen der ersten bedeutungstragenden Bildregion;


      (b) Berechnen der Breite der ersten bedeutungstragenden Bildregion;


      (c) Rücksetzen einer Abtastbreite für einen Scanner, um nachfolgende Bilddaten zu lesen;


      (d) Probenahme einer Vielzahl von Zeilenbereichen in jedem Teilbildblock, um die Lage einer Basiszeile für das abgetastete Bild zu
      bestimmen;


      (e) Einlesen einer jeden nachfolgenden bedeutungstragenden Bildregion, bis eine Basiszeile aufgefunden wurde und direktes Einschreiben der Bilddaten einer jeden nachfolgenden bedeutungstragenden Bildregion in die bitweise orientierte Datei und Aufsummie-

                                         -6-



          ren der Gesamtanzahl der Bildzeilen für jede nachfolgende bedeutungstragende Bildregion;


          (f) Einsetzen der Summe der Gesamtanzahl der Bildzeilen als die
          Länge des abgetasteten Bildes und Einschreiben der Breite und der
          Länge in den Anfangskennsatz der bitweise orientierten Datei, oder
          Übertragen der gültigen Bilddaten an ein übergeordnetes Bildverarbeitungsprogramm; und


          (g) Schließen der bitweise orientierten Datei und Übergeben des
          Dateinamens der bitweise orientierten Datei als ein Parameter an
          ein übergeordnetes Bildverarbeitungsprogramm oder an eine Datenquelle, oder Senden eines Dateiendesignals an ein übergeordnetes Bildverarbeitungsprogramm, um das Einlesen der gültigen
          Bilddaten zu beenden; und


          (h) Senden eines Steuersignals an den Scanner, um den Abtastvorgang zu beenden."


Zum Wortlaut der Patentansprüche 2 bis 8 und 10 bis 15 wird auf die Akte verwiesen.


                                          II.


Die Beschwerde ist zulässig und führt mit dem neuen Patentbegehren auch zum
Erfolg.


1. Die geltenden Patentansprüche sind zulässig. Das im Patentanspruch 1 geänderte Merkmal, das das sequentielle Lesen eines ersten sowie weiterer Teilbildblöcke aus einem Scanner betrifft, ist in der ursprünglichen Beschreibung offenbart (Offenlegungsschrift Sp 4 Z 48 – 52).

                                       -7-




2. Stand der Technik


Aus Druckschrift (1) ist ein Verfahren zum Korrigieren des Schrägwinkels von
schräg durch einen Scanner erfassten Bildern bekannt (Fig 3). Hierzu wird für einzelne Zeilen des Bildes jeweils das am weitesten links liegende Pixel mit Bildinformation festgestellt (Abstract). Durch die so gefundenen Punkte wird eine Gerade gelegt (Fig 2: 109, 111), deren Winkel zu den Abtastlinien bestimmt wird (Fig
2: 113). Anschließend wird das Bild um diesen Winkel gedreht (Fig 2: 115). Im
Unterschied zu den Gegenständen der Patentansprüche 1 und 9 wird das Bild
nicht im Echtzeitbetrieb beschnitten. Das Verfahren wird vielmehr an vollständig
eingescannten Bildern vorgenommen.


Die Druckschrift (2) betrifft ein Verfahren zum automatischen Beschneiden eines
abgetasteten Bildes. Dabei wird zunächst eine Kante des Dokumentbildes innerhalb eines Abtastbildes und daraus der Schrägwinkel des Dokumentbildes ermittelt (Sp 2 Z 35 - 50). Hierfür werden für jede Abtastlinie das erste und das letzte
Dokumentpixel lokalisiert (Sp 7 Z 26 – 33). Die Berechnung des ersten und letzten
Dokumentpixels und des Schrägwinkels werden nach einer Ausführungsform erst
durchgeführt, wenn das Dokument vollständig gescannt ist (Sp 10 Z 25 – 34). Alternativ hierzu kann aber auch die Bestimmung des ersten und letzten Dokumentpixels parallel zum Scannen für jede Zeile sofort dann durchgeführt werden, wenn
die Zeile vollständig gescannt ist. Aber auch bei dieser zweiten Ausführungsform
ist die Berechnung des Schrägwinkels erst möglich, wenn das Scannen abgeschlossen ist (Sp 10 Z 9 – 22). Ein im Echtzeitbetrieb ablaufendes Verfahren, bei
dem nur bedeutungstragende Bildteile vom Scanner eingelesen werden, wird somit in (2) abweichend von den Gegenständen der Patentansprüche 1 und 9 nicht
beschrieben. Außerdem werden keine Teilbildblöcke eingelesen, die Breite der
bedeutungstragenden Bildregion wird nicht bestimmt und die Abtastbreite des
Scanners wird nicht zurückgesetzt.

                                        -8-




Die Druckschrift (3) entspricht in weiten Teilen der Druckschrift (2). Sie bringt hinsichtlich der Beurteilung der Patentfähigkeit keine neuen Gesichtspunkte.




3. Neuheit


Die zweifelsfrei gewerblich anwendbaren Gegenstände der Patentansprüche 1
und 9 sind neu, denn keine der Druckschriften zeigt alle ihre Merkmale, wie sich
aus den vorstehenden Ausführungen zum Stand der Technik ergibt.




4. Erfinderische Tätigkeit


Der Gegenstand des Patentanspruches 1 beruht auf einer erfinderischen Tätigkeit.


Bei dem Verfahren zum automatischen Beschneiden eines abgetasteten Bildes
nach Druckschrift (2) wird zunächst das Bild vollständig vom Scanner abgetastet.
Erst danach wird der Schrägwinkel berechnet (Schritte 506, 507) und das Bild beschnitten. Bei diesem Verfahren besteht ersichtlich der Nachteil, dass das nachträgliche Beschneiden zu Verzögerungen im Verfahrensablauf führt, weil bedeutungsleere Bildanteile ebenfalls eingescannt werden müssen.


Der Fachmann, ein Hochschulingenieur mit mehrjähriger Berufserfahrung in der
Entwicklung von Scannern, erkennt zwar auf Grund seines Fachwissens, dass ein
im Echtzeitbetrieb ablaufendes Verfahren, bei dem das Bild bereits beim Scannen
beschnitten wird, zu einem schnelleren Verfahrensablauf führen würde. Er erhält
jedoch weder aus den Druckschriften (2) und (3) noch aus der weiter abliegenden
Druckschrift (1) einen Hinweis darauf, wie er bei dem aus (2) bekannten Verfahren
den Echtzeitbetrieb verwirklichen kann. Er gelangt daher nur durch erfinderische
Tätigkeit zu den im Patentanspruch 1 im einzelnen angegebenen Merkmalen, wo-

                                       -9-



nach u. a. das Bild in Teilbildblöcke unterteilt wird, dann nach einer ersten bedeutungstragenden Bildregion in einem Teilbildblock gesucht wird, die Breite der ersten bedeutungstragenden Bildregion berechnet wird und dann die Abtastbreite des
Scanners für das Einlesen nachfolgender Bilddaten auf die berechnete Breite zurückgesetzt wird.


Der nebengeordnete Patentanspruch 9 unterscheidet sich vom Patentanspruch 1
unter anderem dadurch, dass die das Aufzeichnen der Attribute und das Berechnen der Position betreffenden Merkmale (b) und (c) des Patentanspruchs 1 nicht
aufgeführt sind. Außerdem enthält er das – verglichen mit dem Patentanspruch 1
– zusätzliche Merkmal des Sendens eines Steuersignals (Merkmal (h)). Die Patentansprüche 1 und 9 beschreiben daher unterschiedliche Verfahren.


Da der Patentanspruch 9 die die Patentfähigkeit tragenden Merkmale des Patentanspruchs 1 umfasst, ist sein Gegenstand ebenfalls patentfähig.


5. Die auf die Patentansprüche 1 und 9 rückbezogenen Patentansprüche 2 bis 8
und 10 bis 15 betreffen über das Selbstverständliche hinausgehende Ausgestaltungen der Gegenstände der Patentansprüche 1 und 9 und sind daher ebenfalls
gewährbar.


6. Die Beschreibung genügt den an sie nach § 34 PatG zu stellenden Anforderungen.




Dr. Hartung               Obermayer               Martens             Dr. Zehendner


                                                                                 Pr
