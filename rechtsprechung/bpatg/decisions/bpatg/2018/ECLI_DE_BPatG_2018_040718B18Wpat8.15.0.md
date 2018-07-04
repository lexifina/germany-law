---
ecli: "ECLI:DE:BPatG:2018:040718B18Wpat8.15.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 8/15"
decided: "2018-07-04"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=28&nr=32077&anz=825&pos=430&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2018-07-04_18_W-pat_8_15_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 18 W (pat) 8/15 vom 2018-07-04

## Entscheidung

BUNDESPATENTGERICHT


  18 W (pat) 8/15                                                 Verkündet am
_______________                                                    4. Juli 2018
    (Aktenzeichen)                                                      …




                            BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 10 2013 020 967.6


…




hat der 18. Senat (Techn. Beschwerdesenat) des Bundespatentgerichts auf die
mündliche Verhandlung vom 4. Juli 2018 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, Dipl.-Phys. Dr. Schwengelbeck und
Dipl.-Ing. Altvater




ECLI:DE:BPatG:2018:040717B18Wpat8.15.0

                                       -2-



beschlossen:


          Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 7. April 2015 aufgehoben und die Sache wird an das
          Deutsche Patent- und Markenamt zurückverwiesen.



                                    Gründe


                                        I.


Die am 11. Dezember 2013 beim Deutschen Patent- und Markenamt unter
Inanspruchnahme einer US-amerikanischen Priorität vom 19. Dezember 2012
(US 13/720 745) eingereichte Patentanmeldung 10 2013 020 967.6 mit der
Bezeichnung


       „Technik zur Ausführung von Speicherzugriffsoperationen über eine
                                 Textur-Hardware“


ist durch die Prüfungsstelle für Klasse G06F mit einem am 7. April 2015 signierten
Beschluss zurückgewiesen worden. Die Zurückweisung ist damit begründet
worden, dass die Gegenstände der jeweiligen Ansprüche 1 nach Hauptantrag
bzw. Hilfsanträgen 1 und 2 nicht so deutlich und vollständig offenbart seien, dass
ein Fachmann sie ausführen könne, sowie dass der Gegenstand des Anspruchs 1
nach Hilfsantrag 3 nicht auf einer erfinderischen Tätigkeit gegenüber dem Stand
der Technik gemäß


               D1: US 2007 / 0 091 089 A1


beruhe.

                                             -3-



Im Prüfungsverfahren ist zudem folgender Stand der Technik genannt worden:


              D2: GPU Gems 2: Chapter 32. Taking the Plunge into GPU
                    Computing.
                    </http://http.developer.nvidia.com/GPUGems2/gpugems2_chap
                    ter32.html>       In:    <web.archive.org>           mit      Datum   vom
                    25. April 2009.


Die Beschwerde der Anmelderin richtet sich gegen den vorstehend genannten
Beschluss.


Mit Ladungszusatz vom 23. März 2018 hat der Senat auf folgende Druckschrift als
möglicherweise relevanten Stand der Technik hingewiesen:


              D3:    US 7 002 591 B1.


Die Anmelderin beantragt,


       den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 7. April 2015 aufzuheben und
       das Patent auf der Grundlage der folgenden Unterlagen zu erteilen:


       -      Patentansprüche 1 bis 9, eingereicht in der mündlichen Verhandlung,
       -      Beschreibung        Seiten 1       bis     43,        eingegangen     am
              9. März 2014,
       -      Figuren 1,   2,     3A-C,     4,   7     und     8,   eingegangen     am
              9. März 2014,       Figuren 5      und         6,     eingegangen     am
              23. März 2015.

                                       -4-



Anspruch 1 lautet unter senatsseitiger Hinzufügung einer Merkmalsgliederung
(Änderungen gegenüber dem ursprünglich eingereichten Anspruch 1 hervorgehoben):


        M1        „Ein computerimplementiertes Verfahren zur Ausführung einer
                  Datenzugriffsoperation, wobei das Verfahren umfasst:


        M2        Empfangen einer ersten Speicherzugriffsanforderung;


        M3        Ermitteln, dass die erste Speicherzugriffsanforderung eine Zugriffsoperation für allgemeine Daten repräsentiert, die nicht
                  speziell mit Texturdaten verknüpft sind;


        M4        Konfigurieren einer Textur-Verarbeitungs-Pipeline, um Zugriffsoperationen für allgemeine Daten anstelle von Zugriffsoperationen für Texturdaten auszuführen,


        M5        wobei das Konfigurieren der Textur-Verarbeitungs-Pipeline
                  umfasst:       Konfigurieren        einer         Textur-orientierten
                  Verarbeitungseinheit    innerhalb    der    Textur-Verarbeitungs-Pipeline, um die erste Speicherzugriffsanforderung an eine
                  nachfolgende       Verarbeitungseinheit      in       der    Textur-Verarbeitungs-Pipeline weiterzuleiten, ohne Textur-bezogene
                  Operationen    mit   der   ersten   Speicherzugriffsanforderung
                  auszuführen; und


        M6        Ausführen der Zugriffsoperation für allgemeine Daten durch
                  Abrufen eines Teils von allgemeinen Daten aus einer Stelle,
                  die aus der ersten Speicherzugriffsanforderung abgeleitet ist.“

                                    -5-



Der nebengeordnete Anspruch 8 lautet:


               „Eine Recheneinrichtung, die ausgebildet ist, eine Datenzugriffsoperation auszuführen, mit:


    N1         einer Verarbeitungseinheit, die ausgebildet ist, um:


    N2         eine erste Speicherzugriffsanforderung zu empfangen;


    N3         zu ermitteln, dass die erste Speicherzugriffsanforderung eine
               Zugriffsoperation für allgemeine Daten repräsentiert, die nicht
               speziell mit Texturdaten verknüpft sind;


    N4         eine Textur-Verarbeitungs-Pipeline zur Ausführung von Zugriffsoperationen für allgemeine Daten anstelle von Zugriffsoperationen für Texturdaten zu konfigurieren,


    N5         wobei das Konfigurieren der Textur-Verarbeitungs-Pipeline
               umfasst:       Konfigurieren        einer         Textur-orientierten
               Verarbeitungseinheit    innerhalb    der    Textur-Verarbeitungs-Pipeline, um die erste Speicherzugriffsanforderung an eine
               nachfolgende       Verarbeitungseinheit      in       der    Textur-Verarbeitungs-Pipeline weiterzuleiten, ohne Textur-bezogene
               Operationen    mit   der   ersten   Speicherzugriffsanforderung
               auszuführen; und


    N6         die Zugriffsoperation für allgemeine Daten auszuführen, indem
               ein Teil von allgemeinen Daten aus einer Stelle abgerufen
               wird, die aus der ersten Speicherzugriffsanforderung abgeleitet ist.“

                                      -6-



Wegen des Wortlauts der Unteransprüche 2 bis 7 und 9 wird auf den Akteninhalt
verwiesen.


Die Beschwerdeführerin vertritt die Auffassung, dass die Ausführbarkeit der beanspruchten Gegenstände für den Fachmann gegeben ist und dass die geltenden
Ansprüche zulässig und patentfähig sind.


Wegen der weiteren Einzelheiten wird auf die Akte verwiesen.




                                    II.


Die zulässige Beschwerde führt zur Aufhebung des angefochtenen Beschlusses
der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts und
zur Zurückverweisung in der Sache an das Deutsche Patent- und Markenamt gemäß § 79 Abs. 3 Satz 1 Nr. 1 und 3 PatG.


1. Die Patentanmeldung betrifft gemäß Absatz 0001 der geltenden Beschreibung
   Speicherzugriffsoperationen und eine Technik zur Ausführung von Speicherzugriffsoperationen über eine Textur-Hardware. Eine konventionelle grafische
   Verarbeitungseinheit (GPU) enthalte eine Textur-Verarbeitungshardware, die
   ausgebildet sei, eine Vielzahl von Textur-bezogenen Operationen auszuführen,
   wozu Textur-Ladeoperationen und Textur-Cache-Operationen gehörten. Ein
   Entwickler eines Grafikprogramms könne Schattierungsprogramme erzeugen,
   die von dieser Textur-Verarbeitungshardware Gebrauch machen, um eine
   zweidimensionale graphische Szene zu erzeugen (vgl. Abs. 0002 der geltenden Beschreibung). In jüngerer Zeit hätten Entwickler von Programmen damit
   begonnen, Schattierungsprogramme zu erzeugen, die willkürliche Operationen
   ausführten, welche eine Grafik betreffen würden, wobei die Parallelverarbeitungs-Architektur der GPU vorteilhaft genutzt würde. Jedoch müssten diese
   Speicherzugriffsoperationen unter Berücksichtigung der Architektur der Textur-

                                   -7-



Verarbeitungshardware sehr sorgfältig gestaltet werden, um Textur-Verarbeitungsoperationen nachzubilden. Beispielsweise lese eine typische Textur-Zugriffsoperation zweidimensionale (2D) Texturdaten aus einem Speicher auf der
Grundlage von 2D-Koordinaten und Dimensionen aus, die mit der Textur verknüpft seien. Um ein Schattierungsprogramm zu erzeugen, das in der Lage
sei, Nicht-Texturdaten zu laden, müsse ein Programmentwickler explizit alle
Datenelemente so deklarieren, dass diese 2D-Koordinaten und Abmessungen
besitzen, die eine 2D-Datenstruktur ähnlich zu einer Textur wiedergäben (vgl.
Abs. 0003 der geltenden Beschreibung). Die oben genannte Vorgehensweise
sei problematisch dahingehend, dass eine Erzeugung eines Schattierungsprogramms, das beliebige Berechnungen ausführe, eine extensive Kenntnis der
Textur-Verarbeitungsoperationen benötige und viele Programmentwickler, die
die Parallelverarbeitungsarchitektur der GPUs vorteilhaft ausnutzen wollten,
keine derartige Kenntnis hätten. Diese Anforderungen stellten eine beträchtliche Hürde für viele Programmentwickler dar (vgl. Abs. 0004 der geltenden Beschreibung). Eine Lösung für dieses Problem bestehe darin, einen separaten
Datenpfad für allgemeine Speicherzugriffsoperationen zusätzlich zu der bestehenden Textur-Verarbeitungshardware zu schaffen. Mit dieser Vorgehensweise könnten Programmentwickler, die Verarbeitungsoperationen mit beliebigen Nicht-Texturdaten ausführen wollten, einfach Programme schreiben, die
vollständig auf diesem separaten Pfad beruhen. Jedoch sei diese Vorgehensweise problematisch, da konventionelle GPUs nicht den erforderlichen Platz
hätten, um weitere Datenpfade zu integrieren. Eine Vergrößerung der GPU sei
dagegen kostenaufwändig (vgl. Abs. 0005 der geltenden Beschreibung).


Als Aufgabe wird dazu sinngemäß aufgeführt, eine effizientere Technik zur
Ausführung allgemeiner Datenzugriffsoperationen über eine Textur-Verarbeitungshardware zu schaffen (vgl. Absatz 0006 der geltenden Beschreibung).


Der zuständige Fachmann ist vorliegend ein Diplom-Ingenieur der Fachrichtung Elektrotechnik mit Schwerpunkt Informationstechnik, der über eine mehr-

                                       -8-



   jährige Erfahrung auf dem Gebiet der Entwicklung von Hard- und Software für
   Computergrafikverarbeitung verfügt.


   Zur Lösung der Aufgabe sind gemäß den unabhängigen Ansprüchen 1 und 8
   ein Verfahren, welches auf einem Computer bzw. einer Rechnereinrichtung
   implementiert ist (computerimplementiertes Verfahren), sowie eine Rechnereinrichtung zur Ausführung einer Datenzugriffsoperation vorgesehen, bei der
   eine erste Speicherzugriffsanforderung empfangen bzw. ermittelt wird, die eine
   Zugriffsoperation für allgemeine – nicht speziell mit Texturdaten verknüpfte –
   Daten repräsentiert (vgl. Merkmale M1 bis M3 bzw. N1 bis N3). Unter Texturdaten versteht der Fachmann Daten, die dazu dienen, ein computergeneriertes
   Bild detailreicher und realistischer erscheinen lassen. Gemäß Merkmal M4
   bzw. Merkmal N4 soll eine Textur-Verarbeitungs-Pipeline konfiguriert werden,
   um Zugriffsoperationen für allgemeine Daten anstelle von Zugriffsoperationen
   für Texturdaten auszuführen. Des Weiteren ist das Konfigurieren einer Texturorientierten Verarbeitungseinheit innerhalb der Textur-Verarbeitungs-Pipeline
   vorgesehen, um die erste Speicherzugriffsanforderung an eine nachfolgende
   Verarbeitungseinheit in der Textur-Verarbeitungs-Pipeline weiterzuleiten, ohne
   Textur-bezogene Operationen mit der ersten Speicherzugriffsanforderung
   auszuführen (vgl. Merkmal M5 bzw. Merkmal N5). Die Zugriffsoperation für allgemeine Daten wird ausgeführt, indem ein Teil von allgemeinen Daten aus einer Stelle, die aus der ersten Speicherzugriffsanforderung abgeleitet ist, abgerufen wird (vgl. Merkmal M6 bzw. Merkmal N6).


2. Die geltenden Ansprüche und Beschreibungsunterlagen mitsamt Figuren sind
   zulässig (§ 38 PatG).


   Der geltende Verfahrensanspruch 1 beinhaltet die Merkmale der ursprünglichen Ansprüche 1 und 7 (vgl. Merkmale M1 bis M6) unter Präzisierung des
   Merkmals M3 im Rahmen der ursprünglich in englischer Sprache eingereichten
   Beschreibung (vgl. Abs. 0076, erster Satz). Der geltende nebengeordnete Vor-

                                       -9-



   richtungsanspruch 8 beinhaltet die Merkmale des ursprünglichen Anspruchs 9
   im Gesamtzusammenhang mit den Merkmalen der ursprünglichen Ansprüche
   1 und 7 (vgl. Merkmale N1 bis N6) unter Präzisierung des Merkmals N3 im
   Rahmen der ursprünglichen Beschreibung (vgl. Abs. 0076 im Zusammenhang
   mit Fig. 1 und 5 bis 7 sowie Abs. 0007, 0008 und Abs. 0067 bis 0076). Die
   geltenden Unteransprüche 2 bis 7 und 9 beinhalten die Merkmale der ursprünglichen Ansprüche 2 bis 6, 8 und 10, die im Gesamtzusammenhang auch
   in den Absätzen 0069, 0070, 0074, 0075, 0080 und 0083 der ursprünglichen
   Beschreibung offenbart sind.


   Die geltende Beschreibung sowie die geltenden Figuren entsprechen inhaltlich
   der ursprünglich in englischer Sprache eingereichten Beschreibung mitsamt
   den ursprünglichen Figuren; die Änderungen in den Figuren 5 und 6 basieren
   auf den Absätzen 0080 und 0083 dieser ursprünglichen Beschreibung.


3. Das Verfahren gemäß Anspruch 1 ist ausführbar; dies gilt ebenso in Bezug auf
   die Gegenstände der weiteren Ansprüche der vorliegenden Anmeldung
   (§ 34 Abs. 4 PatG).


   Unter dem im Anspruch 1 aufgeführten computerimplementierten Verfahren
   versteht der Fachmann ein Verfahren, welches auf einem Computer bzw. einer
   Rechnereinrichtung implementiert ist bzw. darauf durchgeführt wird. Das in der
   zugehörigen Beschreibung aufgeführte – zweifellos technische – Ausführungsbeispiel, welches auf einer Hardware zur Texturverarbeitung beruht, ist diesbezüglich für den Fachmann hinreichend deutlich und vollständig beschrieben
   (vgl. geltende Beschreibung, u. a. Abs. 0067 ff. i. V. m. Fig. 5). Die in der Anmeldung enthaltenen Angaben vermitteln dem Fachmann dabei so viel an
   technischer Information, dass er mit seinem Fachwissen in der Lage ist, die
   Erfindung bzw. das zweifellos technische Verfahren gemäß Anspruch 1 erfolgreich auszuführen (vgl. BGH, Urteil vom 13. Juli 2010, Xa ZR 126/07, Leitsatz
   – Klammernahtgerät). Dies gilt in gleicher Weise in Bezug auf den geltenden

                                       - 10 -



  Vorrichtungsanspruch 8 sowie die geltenden Unteransprüche, deren Gegenstände ebenfalls ausführbar offenbart sind.


4. Der zweifellos technische Gegenstand des geltenden Anspruchs 1 ist neu
  gegenüber dem im Verfahren befindlichen Stand der Technik gemäß den
  Druckschriften D1 bis D3 (§ 3 PatG).


  Druckschrift D3, die als nächstliegender im Verfahren befindlicher Stand der
  Technik anzusehen ist, beschreibt ein Verfahren zur Ausführung einer Datenzugriffsoperation in einem Computergrafik-System mit einer Textur-Verarbeitungs-Pipeline (texturing pipeline arrangement) für die Darstellung von 2D- und
  3D-Grafiken (vgl. Abstract / Merkmal M1). Das Verfahren beinhaltet das
  Empfangen von Speicherzugriffsanforderungen bezüglich Daten für eine Textur-Verarbeitungs-Pipeline (texturing pipeline) eines Grafik-Prozessors (vgl.
  Fig. 4 und Fig. 5 sowie Sp. 8, Z. 62, bis Sp. 9 Z. 43 und Fig. 10A-D mitsamt
  zugh. Text in Sp. 14, Z. 20-42 / Merkmal M2). Vor einer Verarbeitung von
  Texturkoordinaten wird ermittelt, ob eine Speicherzugriffsanforderung indirekte
  Texturdaten (retrieved indirect texture lookup data) betrifft, welche – im Gegensatz zu Merkmal M3 – lediglich Daten repräsentieren, die speziell mit den
  zugehörigen Texturdaten verknüpft sind (vgl. Fig. 10A und Fig. 10B-D sowie
  Sp. 14, Z. 26-42 und Sp. 15, Z. 61, bis Sp. 16, Z. 2). Die in Figur 5 und den Figuren 10A bis 10D dargestellte Textur-Verarbeitungs-Pipeline (texturing pipeline) weist eine Schleife auf (vgl. u. a. Fig. 5: loop 500d), die für die indirekten
  Texturdaten vorgesehen ist – nicht jedoch für allgemeine Daten, die nicht speziell mit Texturdaten verknüpft sind. Dabei ist die Textur-Verarbeitungs-Pipeline
  im Hinblick auf Merkmal M4 auch nur so konfiguriert, dass Zugriffsoperationen
  für die vorstehend genannten indirekten Texturdaten anstelle von Zugriffsoperationen bezüglich direkter Texturdaten (texture data lookup retrieval / direct
  texture coordinates) ausgeführt werden (vgl. Fig. 5 und Sp. 10, Z. 17-27 sowie
  Fig. 10A-D und die Zitatstellen a. a. O.). Im Hinblick auf eine nachfolgende
  Verarbeitungseinheit, wie sie in Merkmal M5 genannt wird, ist auch nur be-

                                    - 11 -



kannt, dass eine Textur-orientierte Verarbeitungseinheit innerhalb der Textur-Verarbeitungs-Pipeline so konfiguriert wird, dass Daten, die mit den
Texturdaten verknüpft sind (indirect texture data), an eine nachfolgende
Verarbeitungseinheit (indirect texture data processing / processing circuitry […]
500c) in der Textur-Verarbeitungs-Pipeline weitergeleitet werden (vgl. Fig. 4, 5
und 11 sowie Sp. 10, Z. 32-39, Sp. 15, Z. 61 bis Sp. 16, Z. 31 und Sp. 25,
Z. 25 ff: sowie Fig. 7B und Fig. 10A-D). Wie vorstehend bezüglich Merkmal M3
ausgeführt, handelt es sich bei den indirekten Texturdaten gerade nicht um
allgemeine Daten, die keine spezielle Verknüpfung mit den Texturdaten
aufweisen (Merkmal M5 fehlt). Dies gilt auch in Bezug auf das in Merkmal M6
aufgeführte Ausführen einer Zugriffsoperation für allgemeine Daten durch Abrufen eines Teils von allgemeinen Daten – eine solche Maßnahme bezüglich
allgemeiner Daten, die nicht mit Texturdaten verknüpft sind, ist Druckschrift D3
nicht entnehmbar.


Dies gilt in gleicher Weise in Bezug auf die Recheneinrichtung gemäß dem nebengeordneten Anspruch 9, dessen Merkmale N1 bis N6 den Merkmalen des
Anspruchs 1 entsprechen (vgl. insbesondere die Ausführungen zu den Merkmalen M3 bis M6, die den Merkmalen N3 bis N6 des Anspruch 9 entsprechen).


Das Verfahren gemäß Anspruch 1 sowie die Rechnereinrichtung gemäß Anspruch 8 sind damit neu gegenüber dem Stand der Technik gemäß Druckschrift D3.


Druckschrift D1 beschreibt im Hinblick auf die Merkmale M1 bis M3 ein computerimplementiertes Verfahren zur Ausführung einer Datenzugriffsoperation
auf Befehle, Daten und Texturen in einem Computer-Grafik-System (vgl. u. a.
Fig. 2, Abs. 0029 und Abs. 0041: […] fetching of instructions / constants / data /
texture). In Figur 2 wird der Ablauf einer Grafik-Prozessor-Pipeline dargestellt,
wobei die Pipeline bzw. die Abarbeitung von Bildverarbeitungsschritten in einzelnen Grafik-Prozessor-Einrichtungen (vgl. Bezugszeichen 52 bis 62) darge-

                                   - 12 -



stellt ist (vgl. Abs. 0029: pipelined graphics processor). Von einer ersten Komponente (input assembler 52) sowie weiteren Komponenten der Pipeline des
Grafik-Prozessors werden dabei ausschließlich Daten angefordert, die mit
Texturdaten (TEXTURE / texture data) verknüpft sind (vgl. Fig. 2 sowie
Abs. 0029 und Abs. 0041). Im Vergleich zum Verfahren gemäß Anspruch 1 ist
Druckschrift D1 auch kein Konfigurieren der Textur-Verarbeitungs-Pipeline zu
entnehmen, um Zugriffsoperationen für allgemeine Daten – die nicht speziell
mit Texturdaten verknüpft sind – anstelle von Zugriffsoperationen für Texturdaten auszuführen, wie es in Merkmal M4 aufgeführt wird (Merkmal M4 fehlt).
Ein Konfigurieren einer Textur-basierten Verarbeitungseinheit innerhalb einer
Textur-Verarbeitungspipeline ohne Textur-bezogene Operationen entsprechend Merkmal M5 ist Druckschrift D1 ebenfalls nicht zu entnehmen. Auch das
Ausführen einer Zugriffsoperation für allgemeine Daten, die nicht speziell mit
Texturdaten verknüpft sind, durch das Abrufen eines Teils von allgemeinen
Daten aus einer Stelle, die aus der ersten Speicherzugriffsanforderung abgeleitet ist, kann Druckschrift D1 nicht entnommen werden (vgl. insbesondere
Fig. 2 und zugeh. Text sowie Fig. 3 und Abs. 31 bis 33 und 36 / Merkmal M6
fehlt).


Dies gilt wiederum in gleicher Weise in Bezug auf die Recheneinrichtung gemäß dem nebengeordneten Anspruch 9, dessen Merkmale N1 bis N6 den
Merkmalen des Anspruchs 1 entsprechen (vgl. vorstehende Ausführungen).


Das Verfahren gemäß Anspruch 1 sowie die Rechnereinrichtung gemäß Anspruch 8 sind damit auch neu gegenüber dem Stand der Technik gemäß
Druckschrift D1.


In Druckschrift D2 wird hinsichtlich der Merkmale M1 und M2 ein computerimplementiertes Verfahren zur Ausführung von Datenzugriffsoperationen im Zusammenhang mit einer Grafik-Prozessoreinheit (GPU) beschrieben, wobei die
beschriebenen Datenzugriffsoperationen nur das Empfangen von Speicherzu-

                                    - 13 -



griffsanforderungen für Texturdaten (texture data / texels) beinhalten (vgl. u. a.
Einleitung zu Kapitel 32 und Abschnitt 32.1.1, vorle. Abs.). Zwar gibt Druckschrift D2 Hinweise auf ein Verarbeiten allgemeiner Daten mit einer GPU (vgl.
Abschnitte 32.1, einleit. Abs., und 32.1.1, le. Abs.). Druckschrift D2 ist dabei
jedoch weder das Ermitteln einer Speicherzugriffsanforderung für allgemeine
Daten zu entnehmen, die nicht speziell mit den Texturdaten verknüpft sind,
noch das Konfigurieren einer Textur-Verarbeitungs-Pipeline, um anstelle von
Zugriffsoperationen für Texturdaten jeweils Zugriffsoperationen für solche allgemeine Daten auszuführen (Merkmale M3 und M4 fehlen). Auch das Konfigurieren einer Textur-basierten Verarbeitungseinheit innerhalb einer Textur-Verarbeitungspipeline ohne Textur-bezogene Operationen ist Druckschrift D2 nicht
zu entnehmen (Merkmal M5 fehlt). Das Ausführen einer Zugriffsoperation für
allgemeine und nicht speziell mit den Texturdaten verknüpfte Daten durch das
Abrufen eines Teils von allgemeinen Daten aus einer Stelle, die aus der ersten
Speicherzugriffsanforderung abgeleitet ist, ist Druckschrift D2 ebenfalls nicht
zu entnehmen (vgl. Kapitel 32, Abschnitte 32.1.1 und 32.1.2 / Merkmal M6
fehlt).


Die vorstehenden Ausführungen zu den Merkmalen M1 bis M6 des Verfahrens
gemäß Anspruch 1 gelten in gleicher Weise in Bezug auf die Recheneinrichtung gemäß dem nebengeordneten Anspruch 9, dessen Merkmale N1 bis N6
den Merkmalen des Anspruchs 1 entsprechen (vgl. insbesondere die Ausführungen zu den fehlenden Merkmalen M4 bis M6, die den Merkmalen N4 bis N6
des Anspruchs 9 inhaltlich entsprechen).


Das Verfahren gemäß Anspruch 1 sowie die Rechnereinrichtung gemäß Anspruch 8 sind damit auch neu gegenüber dem Stand der Technik gemäß
Druckschrift D2.


Keine der im Verfahren befindlichen Druckschriften D1 bis D3 beschreibt damit
ein Verfahren mit sämtlichen Merkmalen des geltenden Anspruchs 1 bzw. eine

                                      - 14 -



   Rechnereinrichtung mit sämtlichen Merkmalen des nebengeordneten Anspruchs 8. Dies gilt insbesondere in Bezug auf die Merkmale M4 bis M6 im Zusammenhang mit Merkmal M3 bzw. die Merkmale N4 bis N6 im Zusammenhang mit Merkmal N3 bezüglich allgemeiner Daten, die nicht speziell mit Texturdaten verknüpft sind, sowie das Konfigurieren der Textur-orientierten Verarbeitungseinheit ohne Textur-bezogene Operationen.


5. Die Gegenstände der geltenden nebengeordneten Ansprüche 1 und 8 beruhen
   auch auf einer erfinderischen Tätigkeit gegenüber dem bislang im Verfahren
   befindlichen Stand der Technik (§ 4 PatG).


   Wie vorstehend ausgeführt, kann der Fachmann dem Stand der Technik gemäß den im Verfahren befindlichen Druckschriften D1 bis D3 insbesondere
   keinen Hinweis auf die Merkmale M4 bis M6 des Anspruchs 1 im Zusammenhang mit Merkmal M3 bezüglich allgemeiner Daten, die nicht speziell mit Texturdaten verknüpft sind, entnehmen. Auch eine Zusammenschau der Lehren
   der Druckschriften D1 bis D3 führt damit nicht zu dem Gegenstand des Anspruchs 1 mit sämtlichen Merkmalen M3 bis M6, da diese dem im Verfahren
   befindlichen Stand der Technik nicht entnehmbar sind. Ein solcher Anspruchsgegenstand ist dem Fachmann auch unter Einbeziehung seines Fachwissens
   nicht nahegelegt.


   Eine Zusammenschau der Lehren der Druckschriften D1 bis D3 führt damit
   auch nicht zum Gegenstand des Anspruchs 8 mit sämtlichen Merkmalen N3
   bis N6, da diese – in gleicher Weise wie die vorstehend genannten Merkmale
   M3 bis M6 des Anspruchs 1 – dem im Verfahren befindlichen Stand der Technik nicht entnehmbar sind. Auch die im Anspruch 8 aufgeführte Rechnereinrichtung ist dem Fachmann unter Einbeziehung seines Fachwissens nicht nahegelegt.

                                      - 15 -



6. Der Senat hat nach § 79 Abs. 3 Satz 1 Nr. 1 PatG davon abgesehen,
  antragsgemäß in der Sache selbst zu entscheiden und das Patent zu erteilen,
  da in Bezug auf die geltenden Ansprüche 1 und 8 bislang keine Sachentscheidung des Deutschen Patent- und Markenamts vorliegt. Eine solche fehlende
  Sachentscheidung liegt unter anderem vor, wenn das Patentbegehren in zulässiger Weise so geändert wurde, dass es nunmehr an einer Sachentscheidung des DPMA fehlt (vgl. Schulte/Püschel, PatG, 10. Auflage, § 79, Rdn. 20,
  21 Nr. 2 und 5).


   Das vorliegende Patentbegehren genügt den formalen Anforderungen der
   §§ 34 und 38 PatG und erfüllt damit die Voraussetzungen für die Prüfung der
   Patentfähigkeit gemäß §§ 1 bis 5 PatG. Eine solche Prüfung ist bislang nicht
   in Bezug auf die geltenden Ansprüche 1 und 8 erfolgt, so dass es an einer
   Sachentscheidung des DPMA fehlt.


   Ein Zurückverweisungsgrund ergibt sich aus dem Vorliegen neuer Tatsachen
   (§ 79 Abs. 3 Nr. 3 PatG), da das Patentbegehren auf Basis von Unteransprüchen und der Beschreibung präzisiert wurde. Ausweislich der Amtsakte ist im
   bisherigen Prüfungsverfahren keine Recherche des relevanten Standes der
   Technik zu den Unteransprüchen sowie zu Merkmalen aus der Beschreibung
   und somit zum Gegenstand des geltenden Patentbegehrens erfolgt. Es kann
   daher nicht ausgeschlossen werden, dass insbesondere unter dem Gesichtspunkt der §§ 3 und 4 PatG ein einer Patenterteilung möglicherweise entgegenstehender Stand der Technik existiert. Zu deren Ermittlung sind in erster
   Linie die Prüfungsstellen des Deutschen Patent- und Markenamts berufen,
   welche hierzu über geeignete Recherchemittel und Fachkenntnisse verfügen
   (Schulte a. a. O., Rdn. 16, 26).


   Da bislang eine Sachentscheidung des DPMA nicht erfolgt ist, ein auf Basis
   der Beschreibung neu formuliertes Patentbegehren vorliegt und eine sachgerechte Entscheidung nur aufgrund einer vollständigen Recherche des rele-

                                        - 16 -



    vanten Standes der Technik ergehen kann, war die Sache – auch um der Anmelderin keine Tatsacheninstanz zu nehmen – zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückzuverweisen (§ 79
    Abs. 3 Satz 1 Nr. 1 und Nr. 3 PatG).




                                           III.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht der am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
      Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
      Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
      war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
      stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
      der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
      sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.

                                   - 17 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Wickborn             Kruppa          Dr. Schwengelbeck             Altvater


                                                                         Pr
