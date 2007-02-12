---
ecli: "ECLI:DE:BPatG:2007:120207B20Wpat352.03.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 352/03"
decided: "2007-02-12"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2007&Sort=1&Seite=10&nr=1980&anz=1511&pos=164&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2007-02-12_20_W-pat_352_03_NA_0.txt"
---

# Bundespatentgericht, 20 W (pat) 352/03 vom 2007-02-12

## Entscheidung

BUNDESPATENTGERICHT

 20 W (pat) 352/03                                       Verkündet am
 _______________                                        12. Februar 2007
    (Aktenzeichen)                                             …




                          BESCHLUSS

                         In der Einspruchssache


…




                     betreffend das Patent 197 56 210


                                 gegen


…




BPatG 154
08.05

                                      -2-



…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 12. Februar 2007 unter Mitwirkung …




beschlossen:


                          Das Patent wird widerrufen.


                                   Gründe


                                        I.


Im Einspruch ist fehlende Patentfähigkeit geltend gemacht worden.


Die Einsprechende beantragte mit Einspruchsschriftsatz,


       das Patent zu widerrufen.


Die Patentinhaberin beantragt,


       das Patent wie erteilt aufrechtzuerhalten, hilfsweise mit den Hilfsanträgen 1-3, eingegangen am 6. Februar 2007.

                                      -3-



In der mündlichen Verhandlung wurden u. a. folgende Druckschriften erörtert:


       (D1) c´t magazin für computer technik: „Kinokarten, PC-Grafikadapter mit
             integrierter Videobeschleunigung“, 1995, Heft 7, Seiten 116-124,
       (D2) FERNSEH- und KINOTECHNIK: „Der MPEG-2-Standard, Generische Codierung für Bewegtbilder und zugehöriger Audio-Information,
             Main Profile: Kern des MPEG-2-Video-Standards (Teil 2)“, 48. Jahrgang, Heft Nr. 5/1994 und die
       (D3) IEEE Journal of Solid-State Circuits 29 (1994), December, No. 12,
             New York, US, Seiten 1474-1481: „A VIDEO DSP with a Macroblock-Level-Pipeline and a SIMD Type Vector-Pipeline Architecture for
             MPEG2 CODEC.”


Der Patentanspruch 1 nach Hauptantrag lautet (Nummerierung hinzugefügt):


       „Verfahren zum Decodieren eines codierten MPEG-Videodatenstroms mit folgenden Verfahrensschritten:


 1.
       Aufteilen der Decodierung des codierten MPEG-Videodatenstroms
       in speicher-rechenintensive Aufgaben, die umfangreiche Speicherund Rechenresourcen benötigen, und wenig speicher-rechenintensive Aufgaben, die keine umfangreichen Speicher- oder Rechenresourcen benötigen;


 2.
       a) Ausführen der wenig speicher-rechenintensiven Aufgaben mittels Softwaremodulen, die auf einem Prozessor (190) laufen,


       b) um vorverarbeitete Symbolstrom-Datenstrukturen für jedes Videobild zu erzeugen, wobei

                                     -4-



3.
     das Ausführen der wenig speicher-rechenintensiven Aufgabe die
     folgenden Schritte umfasst:
     a) Parsen des codierten MPEG-Videodatenstroms mittels einer
        variablen Längendecodierung, um einen geparsten Videodatenstrom zu erzeugen;


     b) Ausführen einer inversen Quantisierung des geparsten Videodatenstroms, um einen quantisierten Videodatenstrom zu erzeugen;


     c) Formatieren des quantisierten Videodatenstroms als die vorverarbeitete Symbolstrom-Datenstruktur; und


     d) Schreiben der vorverarbeiteten Symbolstrom-Datenstruktur in
        den Speicherpuffer;


4.
     Speichern der vorverarbeiteten Symbolstrom-Datenstruktur in einem Speicherpuffer (192,194);


5.
     Ausführen der speicher-rechenintensiven Aufgaben in einer speziellen Videohardware (118b), um ein decodiertes Videobild zu erzeugen;


6.
     a) Synchronisieren der wenig speicher-rechenintensiven Aufgaben, die von den Softwaremodulen erledigt werden, und der
        speicher-rechenintensiven Aufgaben, die von der speziellen
        Videohardware ausgeführt werden; und

                                       -5-



        b) Anzeigen des decodierten Videobildes auf einem Anzeigegerät.“


Der Patentanspruch 1 gemäß Hilfsantrag 1 unterscheidet sich von dem erteilten
Patentanspruch 1 durch Ersetzen des Bindestriches in dem Merkmal „speicher-rechenintensive“ und den Merkmalen „speicher-rechenintensiven“ durch jeweils einen Schrägstrich, der als und/oder auslegbar ist.


Der Patentanspruch 1 gemäß Hilfsantrag 2 unterscheidet sich von dem erteilten
Patentanspruch 1 durch


        Ersetzen des Bindestriches in dem Merkmal „speicher-rechenintensive“ und den Merkmalen „speicher-rechenintensiven“ durch jeweils einen Schrägstrich und


        durch Ersetzen des Merkmals „einem Prozessor“ durch „einer
        CPU“ in der Merkmalsgruppe 2a) sowie durch Anfügung des nachstehenden Merkmals c) an die Merkmalsgruppe 6 (Nummerierung
        hinzugefügt):


        „c) wobei die Aufteilung der Decodieraufgaben in Software- und
            Hardwareaufgaben auch abhängig von den Rechenressourcen der CPU (190) vorgenommen wird.“


Der Patentanspruch 1 gemäß Hilfsantrag 3 unterscheidet sich von dem erteilten Patentanspruch 1 durch


        Ersetzen des Bindestriches in dem Merkmal „speicher-rechenintensive“ und den Merkmalen „speicher-rechenintensiven“ durch jeweils einen Schrägstrich sowie durch Anfügung folgender Merkmale an die Merkmalsgruppe 6 (Nummerierung hinzugefügt):

                                       -6-



        „d) wobei der Schritt des Synchronisierens die Verwaltung eines
             Aufgaben-FIFOs umfasst und


        e) die Anzahl der Einträge des Aufgaben-FIFOs der Anzahl der
             von den Softwaremodulen ausgeführten Aufgaben entspricht,
             und wobei


        f)   Einträge zum Aufgaben-FIFO hinzugefügt werden, wenn die
             Softwaremodule eine Vorverarbeitungsaufgabe beendet haben, und


        g) Einträge aus dem Aufgaben-FIFO entfernt werden, wenn die
             spezielle Videohardware ein Aufgabenende signalisiert.“


Die Einsprechende, die ihrer Ankündigung folgend an der mündlichen Verhandlung nicht teilgenommen hat, führt schriftsätzlich aus, das Verfahren des Patentanspruches 1 gemäß Hauptantrag bzw. der Hilfsanträge 1-3 beruhe nicht auf einer
erfinderischen Tätigkeit.


Die Patentinhaberin ist der Auffassung, die Gegenstände des Patentanspruchs 1
nach Hauptantrag und nach den Hilfsanträgen seien gegenüber dem Stand der
Technik nicht nur neu, sondern beruhten auch auf erfinderischer Tätigkeit. Keine
der im Verfahren befindlichen Druckschriften gebe einen Hinweis darauf, bei einer
MPEG-Decodierung zwischen speicher- und rechenintensiven Aufgaben und wenig speicher- bzw. rechenintensiven Aufgaben zu unterscheiden und diese einer
speziellen Videohardware bzw. Softwaremodulen zuzuweisen. Insbesondere könne der Fachmann dem Stand der Technik keine Anregung dazu entnehmen, bei
einer MPEG-Decodierung die variable Längendecodierung und die inverse Quantisierung mittels Softwaremodulen auszuführen und die mittels Software vorverarbeiteten Daten in einem Speicherpuffer zu speichern, um ihn von dort an eine spezielle Videohardware zu übergeben.

                                       -7-



                                         II.


Der rechtzeitig am 24. Oktober 2003 beim Deutschen Patent- und Markenamt eingegangene Einspruch ist zulässig, er führt zum Widerruf des Patents.


Als Fachmann ist ein Diplomingenieur der Nachrichtentechnik mit besonderer Erfahrung in der Decodierung von MPEG-Bilddateien anzusetzen.


Zum Hauptantrag und Hilfsantrag 1


Der Gegenstand des Patentanspruches 1 gemäß Hauptantrag und Hilfsantrag 1
umfasst den Gegenstand der enger gefassten Patentansprüche 1 gemäß Hilfsantrag 2 und Hilfsantrag 3. Nachdem letztere - wie die nachfolgenden Ausführungen
zu den Hilfsanträgen 2 und 3 zeigen - nicht auf einer erfinderischen Tätigkeit beruhen, sind auch die Patentansprüche 1 nach Hauptantrag und nach Hilfsantrag 1
nicht rechtsbeständig.


Zum Hilfsantrag 2 und Hilfsantrag 3


Die Druckschrift D1 beschreibt ein Verfahren zum Decodieren eines codierten
AVI- oder MPEG-Videodatenstroms mit Hilfe von speziellen Videokarten. Bei diesen Videokarten werden die beiden letzten Stufen des Decodierungsprozesses,
nämlich die Farbraumkonvertierung und das Skalieren, innerhalb eines auf der Videokarte implementierten Grafikchips ausgeführt. Diese beiden Funktionen sind
dort fest verdrahtet und laufen in dem Grafikchip um ein Vielfaches schneller ab,
als die entsprechenden Softwareroutinen auf dem PC (S. 116 re. Sp. Abs. 2). Anhand eines Blockdiagramms (D1: S. 117 oben) wird gezeigt, dass sich bei der
Wiedergabe von AVI-Sequenzen allein durch Verlagerung der beiden Decodierungsprozesse Farbraumkonvertierung (25 % Rechenleistung) und Skalieren
(25 % Rechenleistung) im Idealfall die CPU- und Busbelastung halbiert (S. 116
re. Sp. Abs. 2 i. V. m. Blockdiagramm auf S. 117). Wie aus dem genannten Block-

                                      -8-



diagramm ohne weiteres ersichtlich, nimmt im Vergleich zur Decodierung von AVI-Sequenzen die Decodierung von MPEG-Sequenzen (MPEG-Videodatenströmen)
die Farbraumkonvertierung und das Skalieren insgesamt nur ca. 15 % Rechenleistung in Anspruch, so dass in diesem Fall die CPU erheblich mehr belastet wäre.
Der Fachmann hat daher bei der Decodierung von MPEG-Videodatenströmen
Veranlassung, von dem Grafikchip noch weitere rechenintensive Aufgaben der
MPEG-Decodierung ausführen zu lassen, um auch im Falle der Decodierung von
MPEG-Videodatenströmen eine Entlastung der CPU in der Größenordnung von
50 % zu erreichen. Dies führt ihn unmittelbar zu einem Verfahren zum Decodieren
eines codierten MPEG-Videodatenstroms mit folgenden Verfahrensschritten:


  -   Aufteilen der Decodierung des codierten MPEG-Videodatenstroms in speicher/rechenintensive Aufgaben, die umfangreiche Speicher- und Rechenressourcen benötigen, und wenig speicher/rechenintensive Aufgaben, die
      keine umfangreichen Speicher- oder Rechenressourcen benötigen (Merkmal 1),
  -   Ausführen der speicher/rechenintensiven Aufgaben in einer speziellen Videohardware (Grafikchip), um ein decodiertes Videobild zu erzeugen
      (Merkmal 5) sowie ein
  -   Ausführen der wenig speicher/rechenintensiven Aufgaben mittels Softwaremodulen, die auf einer CPU (d. h. einem Prozessor) laufen (Merkmal 2a)).


Durch die in dem Blockschaltbild angegebenen prozentualen Rechenleistungen
der einzelnen Verarbeitungsstufen gibt die D1 dem Fachmann weiters eine Anregung, die Aufteilung der Decodieraufgaben in Software- und Hardwareaufgaben
auch abhängig von den Rechenressourcen der CPU vorzunehmen (S. 117 Blockschaltbild oben; Merkmal 6c) gemäß Hilfsantrag 2).

                                       -9-



Aus der Druckschrift D2 sind dem Fachmann neben der inversen Cosinustransformation auch das Parsen mittels einer variablen Längendecodierung und die inverse Quantisierung als weitere, für eine Decodierung von normiert codierten MPEG-Videodatenströmen zwingend erforderliche Schritte bekannt (S. 236 Pkt. 4 Abs. 1
i. V. m. Fig. 9).
Es steht im Ermessen des Fachmanns, von der CPU wenigstens die beiden letztgenannten Schritte, das


   -   Parsen des codierten MPEG-Videodatenstroms mittels einer variablen Längendecodierung, um offensichtlich einen geparsten Videodatenstrom zu erzeugen (Merkmal 3a)) und das
   -   Ausführen einer inversen Quantisierung des geparsten Videodatenstroms,
       um offensichtlich einen quantisierten Videodatenstrom zu erzeugen (Merkmal 3b)),


vornehmen zu lassen.


Weiterhin entnimmt der Fachmann der D2, dass der solchermaßen quantisierte Videodatenstrom wieder hergestellt bzw. in eine Blockanordnung überführt, d. h. als
vorverarbeitete Symbolstrom-Datenstruktur formatiert wird (S. 237 Abs. 2 i. V. m.
Fig. 9; Merkmal 3c)). Die so vorverarbeitete Symbolstrom-Datenstruktur wird zudem (nach einer zusätzlich vorgenommenen inversen diskreten Cosinustransformation DCT und einer sich anschließenden Bewegungskompensation) in einen
Bildspeicher bzw. Speicherpuffer geschrieben und dort gespeichert (Fig. 9; Merkmale 3d) und 4). Das im Bildspeicher gespeicherte Bild wird anschließend nachverarbeitet und offensichtlich einem Display zugeführt (Merkmal 6b), Fig. 9).


Ein Synchronisieren der auf die Softwaremodule und den Grafikchip aufgeteilten
Aufgaben ist unumgänglich (Merkmal 6a)). Der Fachmann kann weiter nicht übersehen, dass die Resultate der aufgeteilten Aufgaben in einer bestimmten Reihenfolge zusammengeführt werden müssen, um die ursprünglichen Originalbilder

                                        - 10 -



bzw. Bildfolgen wieder vollständig bzw. wieder in der richtigen zeitlichen Abfolge
herstellen zu können. Für die dazu unerlässliche Verwaltung der für ein bestimmtes Bild abzuarbeitenden Decodierungs-Aufgaben und die zwingende, abfolgemäßig korrekte Zusammenführung der jeweiligen Aufgaben-Resultate bietet sich dem
Fachmann aufgrund seines Fachwissens die Verwendung eines First-In-First-Out-Speicherelements („Aufgaben“-FIFO) als geeignetes Mittel an (Merkmal 6d)). Ein
FIFO ist ihm sowohl als Standard-Speicherbauelement der Informationstechnik als
auch aus der D3 speziell zur Anwendung bei der MPEG-Decodierung bekannt
(D3: S. 1479 Fig. 10b).


Da der CPU die weniger speicher/rechenintensiven Aufgaben zugeordnet sind,
liegt es für den Fachmann nahe, der CPU auch die offensichtlich wenig speicher/rechenintensive Synchronisierung zu übertragen. In diesem Fall gehört es zu
den Routinearbeiten des Fachmanns, dass die Anzahl der Einträge des Aufgaben-FIFOs der Anzahl der auf dem Prozessor bzw. der CPU laufenden, von den Softwaremodulen ausgeführten Aufgaben entspricht (Merkmal 6e)), Einträge zum Aufgaben-FIFO hinzugefügt werden, wenn die Softwaremodule eine Vorverarbeitungsaufgabe beendet haben (Merkmal 6f)) und Einträge aus dem Aufgaben-FIFO
entfernt werden, wenn die spezielle Videohardware ein Aufgabenende signalisiert
(Merkmal 6g)).


In Anbetracht der Sachlage kann die Frage, ob die Patentansprüche 1 nach den
Hilfsanträgen 1 bis 3 zulässig sind, dahingestellt bleiben.


gez.
Unterschriften
