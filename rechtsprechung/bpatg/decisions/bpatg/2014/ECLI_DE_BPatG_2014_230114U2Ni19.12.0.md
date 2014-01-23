---
ecli: "ECLI:DE:BPatG:2014:230114U2Ni19.12.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 19/12"
decided: "2014-01-23"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=3&nr=26102&anz=1119&pos=57&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2014-01-23_2_Ni_19_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0021.md", "germany/bund/acts/patg/0022.md", "germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0263.md", "germany/bund/acts/zpo/0267.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 19/12 vom 2014-01-23

## Entscheidung

BUNDESPATENTGERICHT

                    IM NAMEN DES VOLKES

                              URTEIL
                                                      Verkündet am
                                                     23. Januar 2014
  2 Ni 19/12                                                …

(Aktenzeichen)


                    In der Patentnichtigkeitssache

…




BPatG 253
08.05

                                         -2-



                     betreffend das deutsche Patent 41 03 173


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 23. Januar 2014 unter Mitwirkung der Vorsitzenden
Richterin Sredl sowie der Richter Merzbach, Dipl.-Ing. Baumgardt, Dr. Forkel und
Dipl.-Ing. Hoffmann


für Recht erkannt:


        I.    Das deutsche Patent 41 03 173 wird dadurch teilweise für
              nichtig erklärt, dass es im Umfang der angegriffenen Patentansprüche 1, 3, 4, 5 sowie 8 bis 13 folgende Fassung
              erhält:


                        Vorrichtung zum Schutz gegen unautorisierte
                        Benutzung von Software, bei der mindestens
                        ein mit einem Signaleingang eines Rechensystems (10) verbindbarer externer Datengenerator (11) Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen Daten von empfangenen Daten aus dem Rechensystem (10)
                        abhängig sind und das Rechensystem in einen
                        Fehlerzustand gebracht wird oder die Software
                        im Rechensystem nicht zweckmäßig arbeitet,
                        wenn das Rechensystem keine oder fehlerhafte
                        Daten über den Signaleingang (13) empfängt,


                        dadurch gekennzeichnet, dass der Datengenerator (11) Manipulationsversuche an den empfangenen Daten erkennt, wobei

                                        -3-



                      der Datengenerator (11) nicht vorgesehene
                      Daten oder Datenfolgen und/oder zeitlich nicht
                      vorgesehene Daten oder Datenfolgen als Manipulationsversuche erkennt und bei erkanntem
                      Manipulationsversuch den Inhalt eines Speichers im Datengenerator ändert und infolgedessen beim Empfang weiterer Daten zeitlich
                      begrenzt nur fehlerhafte Daten ausgibt, wobei
                      die vom Datengenerator (11) generierten Daten
                      eine nicht-deterministisch erzeugte Redundanz
                      aufweisen, wobei der Datengenerator (11) zwei
                      Zustände A und B besitzt, von deren Annahme
                      die vom Datengenerator ausgegebenen Daten
                      abhängen, der Datengenerator aus dem Zustand A in den Zustand B nur durch mindestens
                      fünf aufeinanderfolgende weitere Zustände C
                      gebracht werden kann, die aufgrund empfangener Daten angenommen werden, und die
                      vom   Datengenerator    ausgegebenen       Daten
                      nicht von den Zuständen C abhängen.


       Im Übrigen wird die Klage abgewiesen.


       II.    Die Kosten des Rechtsstreits trägt die Beklagte.


       III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
              des zu vollstreckenden Betrages vorläufig vollstreckbar.



                                 Tatbestand


Die Beklagte war eingetragene Inhaberin des durch Zeitablauf erloschenen deutschen Patents 41 03 173 (Streitpatent) mit der Bezeichnung „Vorrichtung zum

                                        -4-



Schutz gegen unautorisierte Benutzung von Software“, das am 2. Februar 1991
beim Deutschen Patent- und Markenamt angemeldet und in einer gegenüber der
ursprünglich erteilten Fassung eingeschränkten Form am 13. März 1997 unter der
Nummer DE 41 03 173 C3 veröffentlicht wurde.


Das Streitpatent umfasst 15 Patentansprüche. Der Patentanspruch 1 ist auf eine
„Vorrichtung zum Schutz gegen unautorisierte Benutzung von Software“ gerichtet.
Die auf den Oberbegriff des Patentanspruchs 1 zurückbezogenen Ansprüche 3, 4
und 14 sind nebengeordnete Ansprüche und die Ansprüche 2, 5 bis 13 und 15
sind Unteransprüche.


Patentanspruch 1 lautet in der erteilten Fassung wie folgt:


        „Vorrichtung zum Schutz gegen unautorisierte Benutzung von
        Software, bei der mindestens ein mit einem Signaleingang eines
        Rechensystems (10) verbindbarer externer Datengenerator (11)
        Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen
        Daten von empfangenen Daten aus dem Rechensystem (10)
        abhängig sind und das Rechensystem in einen Fehlerzustand
        gebracht wird oder die Software im Rechensystem nicht
        zweckmäßig arbeitet, wenn das Rechensystem keine oder
        fehlerhafte Daten über den Signaleingang (13) empfängt, dadurch
        gekennzeichnet, dass der Datengenerator (11) nicht vorgesehene
        Daten oder Datenfolgen und/oder zeitlich nicht vorgesehene
        Daten oder Datenfolgen als Manipulationsversuche erkennt und
        bei erkanntem Manipulationsversuch den Inhalt eines Speichers
        im Datengenerator ändert und infolgedessen beim Empfang
        weiterer Daten keine oder fehlerhafte Daten ausgibt und/oder eine
        Benutzerautorisierung verändert.“

                                        -5-



Der nebengeordnete Patentanspruch 3 lautet in der erteilten Fassung wie folgt:


          „Vorrichtung nach dem Oberbegriff des Anspruchs 1, insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1
          und/oder 2, dadurch gekennzeichnet, dass die vom Datengenerator (11) generierten Daten eine nicht-deterministisch erzeugte
          Redundanz aufweisen.“


Der nebengeordnete Patentanspruch 4 lautet in der erteilten Fassung wie folgt:


          „Vorrichtung nach dem Oberbegriff des Anspruchs 1, insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1, 2
          und/oder 3, dadurch gekennzeichnet, dass der Datengenerator
          (11) zwei Zustände A und B besitzt, von deren Annahme die vom
          Datengenerator ausgegebenen Daten abhängen, der Datengenerator aus dem Zustand A in den Zustand B nur durch mindestens
          fünf aufeinanderfolgende weitere Zustände C gebracht werden
          kann, die aufgrund empfangener Daten angenommen werden,
          und die vom Datengenerator ausgegebenen Daten nicht von den
          Zuständen C abhängen.“


Zum Wortlaut der übrigen Ansprüche wird auf die Streitpatentschrift Bezug genommen.


Die Klägerin wendet sich mit ihrer Nichtigkeitsklage gegen die erteilten Patentansprüche 1, 3, 4, 5 sowie 8 bis 13. Die Beklagte verteidigt das Streitpatent im angegriffenen Umfang in der erteilten Fassung, hilfsweise auf Grundlage der in der
mündlichen Verhandlung überreichten Hilfsanträge 1 bis 5, welche die zuvor mit
Schriftsatz vom 28. Juni 2013 eingereichten Hilfsanträge 1 bis 3 sowie die mit
weiterem Schriftsatz vom 15. Januar 2014 eingereichten Hilfsanträge 4 bis 7 ersetzen.

                                        -6-




Die Klägerin macht geltend, der Gegenstand des Streitpatents sei im angegriffenen Umfang gegenüber dem Stand der Technik nicht patentfähig. Er sei nicht neu
(§ 3 Abs. 1 PatG), beruhe aber jedenfalls nicht auf einer erfinderischen Tätigkeit (§
4 Satz 1 PatG). Zudem offenbare das Streitpatent die Erfindung nicht so deutlich
und vollständig, dass ein Fachmann sie ausführen könne, §§ 22 Abs. 1, 21 Abs. 1
Nr. 2 PatG. Der Gegenstand des Streitpatents gehe ferner auch über den Inhalt
der Patentanmeldung in der ursprünglich eingereichten Fassung hinaus, §§ 22
Abs. 1, 21 Abs. 1 Nr. 4 PatG. Schließlich sei auch der Schutzbereich des Streitpatents in unzulässiger Weise erweitert worden, § 22 Abs. 1, 2. Alt. PatG.
Dazu beruft sich die Klägerin auf die Druckschriften



            NK1     WO 92/09160 A1, Zeitrang 7. November 1990, veröffentlicht
                    am 29. Mai 1992,

            NK1a    DE 691 30 175 T2, deutsche Übersetzung des aus der NK1
                    hervorgegangenen europäischen Patents 0 556 305,

           NK2      US 4,740,890,

           NK3      DE 33 15 992 A1,

           NK4      B. Yannicos „Softguard schützt Programme", Artikel in der
                    Zeitschrift „MC", Ausgabe 1/1986,

           NK5      W. Watts „The Protection Racket", .EXE Magazine, Vol. 5, Issue 5, Oktober 1990, Seiten 12/13,15/16 und 18,

           NK6      US 4,584,641,

           NK7      US 4,683,553,

           NK8      US 4,816,654,

           NK9      US 4,932,054,

           NK10     DE 33 18 101 A1,

           NK11     US 4,634,807,

           NK12     US 4,791,565,

                                          -7-




              NK13     US 4,747,139,

              NK14     DE 35 26 130 C2,

              NK15     US 4,562,306,

              NK16     US 4,658,093.


Die Klägerin stellt den Antrag,


        das deutsche Patent 41 03 173 im Umfang der Patentansprüche 1, 3, 4, 5 sowie 8 bis 13 einschließlich der mittelbaren und
        unmittelbaren Rückbezüge für nichtig zu erklären.


Die Beklagte stellt den Antrag,


        die    Klage    abzuweisen,    soweit   sie   sich   gegen   das   Patent 41 03 173 im angegriffenen Umfang richtet.


        Hilfsweise beantragt sie, dem angegriffenen Teil des Streitpatents
        eine der Fassungen der Hilfsanträge 1 bis 5 zu geben.


Hilfsantrag 1


Patentanspruch 1 in der Fassung des Hilfsantrags 1 lautet (Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind unterstrichen):


        „Vorrichtung zum Schutz gegen unautorisierte Benutzung von
        Software, bei der mindestens ein mit einem Signaleingang eines
        Rechensystems (10) verbindbarer externer Datengenerator (11)
        Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen
        Daten von empfangenen Daten aus dem Rechensystem (10)
        abhängig sind und das Rechensystem in einen Fehlerzustand

                                      -8-



        gebracht wird oder die Software im Rechensystem nicht
        zweckmäßig arbeitet, wenn das Rechensystem keine oder
        fehlerhafte Daten über den Signaleingang (13) empfängt,



        dadurch gekennzeichnet, dass der Datengenerator (11) Manipulations-versuche an den empfangenen Daten erkennt, wobei der
        Datengenerator (11) nicht vorgesehene Daten oder Datenfolgen
        und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als
        Manipulationsversuche      erkennt       und      bei   erkanntem
        Manipulationsversuch    den     Inhalt    eines     Speichers   im
        Datengenerator ändert und infolgedessen beim Empfang weiterer
        Daten keine oder fehlerhafte Daten ausgibt und/oder eine
        Benutzerautorisierung verändert.“



Der nebengeordnete Patentanspruch 3 in der Fassung des Hilfsantrags 1 lautet
(Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind gekennzeichnet):


        „Vorrichtung nach dem Oberbegriff des Anspruchs 1, insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1
        und/oder 2, dadurch gekennzeichnet, dass die vom Datengenerator (11) generierten Daten eine nicht-deterministisch erzeugte
        Redundanz aufweisen.“


Der nebengeordnete Patentanspruch 4 in der Fassung des Hilfsantrags 1 lautet
(Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind gekennzeichnet):


        „Vorrichtung nach dem Oberbegriff des Anspruchs 1, insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1, 2

                                       -9-



       und/oder 3, dadurch gekennzeichnet, dass der Datengenerator
       (11) zwei Zustände A und B besitzt, von deren Annahme die vom
       Datengenerator ausgegebenen Daten abhängen, der Datengenerator aus dem Zustand A in den Zustand B nur durch mindestens
       fünf aufeinanderfolgende weitere Zustände C gebracht werden
       kann, die aufgrund empfangener Daten angenommen werden,
       und die vom Datengenerator ausgegebenen Daten nicht von den
       Zuständen C abhängen.“


Die Unteransprüche gemäß Hilfsantrag 1 entsprechen den erteilten angegriffenen
Unteransprüchen 5 sowie 8 bis 13, wobei jeweils die Rückbezüge angepasst wurden.


Hilfsantrag 2


Patentanspruch 1 in der Fassung des Hilfsantrags 2 lautet (Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind durch- bzw. unterstrichen):


       „Vorrichtung zum Schutz gegen unautorisierte Benutzung von
       Software, bei der mindestens ein mit einem Signaleingang eines
       Rechensystems (10) verbindbarer externer Datengenerator (11)
       Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen
       Daten von empfangenen Daten aus dem Rechensystem (10)
       abhängig sind und das Rechensystem in einen Fehlerzustand
       gebracht wird oder die Software im Rechensystem nicht
       zweckmäßig arbeitet, wenn das Rechensystem keine oder
       fehlerhafte Daten über den Signaleingang (13) empfängt,


       dadurch gekennzeichnet, dass der Datengenerator (11) Manipulations-versuche an den empfangenen Daten erkennt, wobei der
       Datengenerator (11) nicht vorgesehene Daten oder Datenfolgen
       und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als

                                       - 10 -



        Manipulationsversuche      erkennt        und      bei   erkanntem
        Manipulationsversuch     den     Inhalt    eines     Speichers   im
        Datengenerator ändert und infolgedessen beim Empfang weiterer
        Daten keine oder zeitlich begrenzt nur fehlerhafte Daten ausgibt
        und/oder eine Benutzerautorisierung verändert.“



Die angegriffenen Ansprüche 3, 5 sowie 8 bis 13 wurden gestrichen. Der nebengeordnete Patentanspruch 4 gemäß Hilfsantrag 2 entspricht dem erteilten angegriffenen nebengeordneten Anspruch 4 mit entsprechend geändertem Rückbezug
(allein auf Anspruch 1).


Hilfsantrag 3


Patentanspruch 1 in der Fassung des Hilfsantrags 3 lautet (Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind durch- bzw. unterstrichen):


        „Vorrichtung zum Schutz gegen unautorisierte Benutzung von
        Software, bei der mindestens ein mit einem Signaleingang eines
        Rechensystems (10) verbindbarer externer Datengenerator (11)
        Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen
        Daten von empfangenen Daten aus dem Rechensystem (10)
        abhängig sind und das Rechensystem in einen Fehlerzustand
        gebracht wird oder die Software im Rechensystem nicht
        zweckmäßig arbeitet, wenn das Rechensystem keine oder
        fehlerhafte Daten über den Signaleingang (13) empfängt,


        dadurch gekennzeichnet, dass der Datengenerator (11) Manipulations-versuche an den empfangenen Daten erkennt, wobei der
        Datengenerator (11) nicht vorgesehene Daten oder Datenfolgen
        und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als
        Manipulationsversuche      erkennt        und      bei   erkanntem
        Manipulationsversuch     den     Inhalt    eines     Speichers   im

                                      - 11 -



         Datengenerator ändert und infolgedessen beim Empfang weiterer
         Daten keine oder fehlerhafte Daten ausgibt und/oder eine
         Benutzerautorisierung verändert, wobei die vom Datengenerator
         (11) generierten Daten eine nicht-deterministisch erzeugte Redundanz aufweisen.“



Der nebengeordnete Patentanspruch 4 gemäß Hilfsantrag 3 lautet (Änderungen
gegenüber Patentanspruch 4 in der erteilten Fassung sind durch- bzw. unterstrichen):


         „Vorrichtung nach dem Oberbegriff des Anspruchs 1, insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1, 2
         und/oder 3 dergestalt, dass der Datengenerator (11) nicht vorgesehene Daten oder Datenfolgen und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als Manipulationsversuche erkennt
         und bei erkanntem Manipulationsversuch den Inhalt eines Speichers im Datengenerator ändert und infolgedessen beim Empfang
         weiterer Daten keine oder fehlerhafte Daten ausgibt und/oder eine
         Benutzerautorisierung verändert,


         dadurch gekennzeichnet,


         dass der Datengenerator (11) zwei Zustände A und B besitzt, von
         deren Annahme die vom Datengenerator ausgegebenen Daten
         abhängen, der Datengenerator aus dem Zustand A in den Zustand
         B nur durch mindestens fünf aufeinanderfolgende weitere Zustände C gebracht werden kann, die aufgrund empfangener Daten
         angenommen werden, und die vom Datengenerator ausgegebenen Daten nicht von den Zuständen C abhängen.“



Die angegriffenen Ansprüche 3, 5 sowie 8 bis 13 wurden gestrichen.

                                       - 12 -




Hilfsantrag 4


Patentanspruch 1 in der Fassung des Hilfsantrags 4 lautet (Änderungen gegenüber Patentanspruch 1 in der erteilten Fassung sind durch- bzw. unterstrichen):


        „Vorrichtung zum Schutz gegen unautorisierte Benutzung von
        Software, bei der mindestens ein mit einem Signaleingang eines
        Rechensystems (10) verbindbarer externer Datengenerator (11)
        Daten erzeugt, wobei die vom Datengenerator (11) ausgegebenen
        Daten von empfangenen Daten aus dem Rechensystem (10)
        abhängig sind und das Rechensystem in einen Fehlerzustand
        gebracht wird oder die Software im Rechensystem nicht
        zweckmäßig arbeitet, wenn das Rechensystem keine oder
        fehlerhafte Daten über den Signaleingang (13) empfängt,


        dadurch gekennzeichnet, dass der Datengenerator (11) Manipulations-versuche an den empfangenen Daten erkennt, wobei der
        Datengenerator (11) nicht vorgesehene Daten oder Datenfolgen
        und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als
        Manipulationsversuche      erkennt        und      bei   erkanntem
        Manipulationsversuch     den     Inhalt    eines     Speichers   im
        Datengenerator ändert und infolgedessen beim Empfang weiterer
        Daten keine oder fehlerhafte Daten ausgibt und/oder eine
        Benutzerautorisierung verändert, wobei die vom Datengenerator
        (11) generierten Daten eine nicht-deterministisch erzeugte Redundanz aufweisen.“



Die angegriffenen Ansprüche 3, 5 sowie 8 bis 13 wurden gestrichen. Der nebengeordnete Patentanspruch 4 gemäß Hilfsantrag 4 entspricht Anspruch 4 gemäß
Hilfsantrag 3.

                                      - 13 -



Hilfsantrag 5


Hinsichtlich des Wortlauts von Patentanspruch 1 gemäß Hilfsantrag 5 wird auf
den Tenor der Entscheidung Bezug genommen. Die weiteren angegriffenen Ansprüche 3, 4, 5 sowie 8 bis 13 wurden gestrichen.


Die Beklagte tritt den Ausführungen der Klägerin in allen Punkten entgegen. Sie
hält den Gegenstand des Streitpatents für ursprünglich offenbart bzw. durch den
ursprünglichen Schutzbereich gedeckt. Das Streitpatent sei auch im Übrigen patentfähig; jedenfalls in einer der Fassungen der Hilfsanträge. Es mangele ihm
gegenüber dem Stand der Technik weder an Neuheit noch an erfinderischer Tätigkeit; eine unzulässige Erweiterung sei nicht gegeben.


Dazu hat sie u.a. auf die folgenden Dokumente verwiesen:


   A2     ursprüngliche Anmeldeunterlagen zum Streitpatent
   A3     Zwischenbescheid der Patentabteilung vom 31. Juli 1995
   A4     Beschluss der Patentabteilung vom 23. Juli 1996
   A5     NK1-P1 (US 5,103,476), Anmeldetag 7. November 1990
   A6     NK1-P2 (US 5,222,134), Anmeldetag 9. April 1991
   A7     Prioritätsdokument zu NK1
   A8     Vergleich zwischen NK1 und Prioritätsschrift NK1 -P1
   A9     Offenlegungsschrift
   A10    Auszug aus einer Online-Enzyklopädie, Seitenkanalattacke
   A11    Auszug aus einer Online-Enzyklopädie, Diskretes Bauelement
   A12    Auszug aus einer Online-Enzyklopädie, Integrierter Schaltkreis
   A20    Auszug aus einer Online-Enzyklopädie, Endlicher Automat


Wegen der weiteren Einzelheiten des Vorbringens der Beteiligten wird auf den
Akteninhalt verwiesen.

                                       - 14 -



                        Entscheidungsgründe


                                        A


Die Klage ist im geltenden Umfang zulässig. Ferner können die geltenden Hilfsanträge 1 bis 5 berücksichtigt werden.


1. Dies gilt insbesondere auch insoweit, als die Klägerin die Nichtigkeitsklage
über die zunächst mit der Klageschrift angegriffenen Patentansprüche 1 und 8 bis
13 des Streitpatents hinaus mit Schriftsatz vom 21. März 2013 auf die Patentansprüche 4 und 5 des Streitpatents sowie in der mündlichen Verhandlung vom
23. Januar 2014 auf den Patentanspruch 3 des Streitpatents erweitert hat. Die
darin liegende Klageänderung ist bereits aufgrund der rügelosen Einlassung der
Beklagten nach § 99 Abs. 1 PatG i. V. m. §§ 263 Abs. 1, 267 ZPO zulässig (vgl.
dazu Busse/Keukenschrijver, Patentgesetz, 7. Auflage, § 82 Rdnr. 23) und im Übrigen auch sachdienlich. Insoweit wurden auch keine Fragen in tatsachlicher und
rechtlicher Hinsicht aufgeworfen, welche in der Verhandlung nicht oder nur mit
unverhältnismäßigem Aufwand zu klären gewesen wären und dementsprechend
eine Vertagung erforderlich gemacht hätten. Vielmehr konnte die Erörterung und
Beurteilung der Patentfähigkeit ohne weiteres in die mündliche Verhandlung einbezogen werden, zumal die Beklagte das kennzeichnende Merkmal des erteilten
Patentanspruchs 3 mittels der Formulierung „…insbesondere in Verbindung mit
dem Kennzeichen des Anspruchs 1, 2 und/oder 3“ Gegenstand des erteilten Patentanspruchs 4 geworden ist. Die Beklagte hat dementsprechend auch sachlich
zu diesem Patentanspruch Stellung genommen. Für den Senat bestand daher
keine Veranlassung, die Erweiterung der Klage auf Patentanspruch 3 nach § 83
Abs. 4 PatG – welcher auch bei einer Klageänderung Anwendung findet (aA insoweit Schulte, PatG, 10. Aufl., § 83 Rdnr. 20) – als verspätet zurückzuweisen.


2. Einer Zulässigkeit der Klage steht auch nicht das Erlöschen des Streitpatents
wegen Zeitablaufs entgegen. Das insoweit erforderliche Rechtsschutzbedürfnis
ergibt sich daraus, dass die Klägerin von der Beklagten wegen Verletzung des

                                       - 15 -



Streitpatents gerichtlich in Anspruch genommen wird. Dies gilt auch in Bezug auf
die erst mit Schriftsatz vom 21. März 2013 bzw. in der mündlichen Verhandlung
vom 23. Januar 2014 angegriffenen Patentansprüche 3, 4 und 5.


3. Die von der Beklagten in der mündlichen Verhandlung am 23. Januar 2014 zur
hilfsweisen Verteidigung des Streitpatents gestellten Hilfsanträge 1 bis 5 sind nicht
gemäß § 83 Abs. 4 PatG als verspätet zurückzuweisen.


Die durch das 2009 in Kraft getretene Patentrechtsmodernisierungsgesetz (PatR-ModG) erfolgte Neufassung des § 83 PatG und die damit in das Nichtigkeitsverfahren eingeführten Präklusionsregeln sehen zwar grundsätzlich die Möglichkeit
vor, verspätetes Vorbringen zurückzuweisen. Hierfür ist es aber stets erforderlich,
dass dieser Vortrag tatsächliche oder rechtliche Fragen aufkommen lässt, die in
der mündlichen Verhandlung nicht oder nur mit unverhältnismäßigem Aufwand zu
klären sind (vgl. Begründung zum Entwurf eines Gesetzes zur Vereinfachung und
Modernisierung des Patentrechts, BlPMZ 2009, 307, 315). Kann das an sich verspätete Vorbringen dagegen noch ohne Weiteres in die mündliche Verhandlung
einbezogen werden, ohne dass es zu einer Verfahrensverzögerung kommt, liegen
die Voraussetzungen für eine Zurückweisung nach § 83 Abs. 4 PatG nicht vor (vgl.
BPatG Urt. v. 15. 11. 2011 – 3 NI 27/10; Busse/Keukenschrijver PatG 7. Aufl.,
§ 83 Rn. 15 a. E.).



So liegt der Fall hier. Die Ansprüche gemäß den Hilfsanträgen enthalten keine
grundlegenden Änderungen gegenüber den weitgehend bereits (schriftsätzlich)
erörterten, fristgerecht eingereichten Hilfsanträgen, so dass nach Überzeugung
des Senats eine Stellungnahme der Klägerin und eine abschließende Beurteilung
ohne Vertagung möglich war. Dementsprechend hat sich die Klägerin bezüglich
der Hilfsanträge der Beklagten zur Sache eingelassen und zu deren, ihrer Auffassung nach, fehlenden Patentfähigkeit ausdrücklich vorgetragen. Eine Vertagung
wurde von der Klägerin auch nicht beantragt.

                                      - 16 -



                                           B


In der Sache erweist sich die Klage, mit der in Bezug auf die angegriffenen Ansprüche sowie die Hilfsanträge neben dem Nichtigkeitsgrund mangelnder Patentfähigkeit nach den §§ 1 bis 5 PatG auch die Nichtigkeitsgründe der unzureichenden Offenbarung (§§ 22 Abs. 1, 21 Abs. 1 Nr. 2 PatG), der unzulässigen Erweiterung gegenüber den ursprünglichen Anmeldeunterlagen (§§ 22 Abs. 1, 21 Abs. 1
Nr. 4 PatG) sowie der Erweiterung des Schutzbereiches gemäß § 22 Abs. 1, 2.
Alt. PatG geltend gemacht werden, überwiegend als begründet.




                                           I.


1. Gemäß der Beschreibungseinleitung des Streitpatents besteht bei Software
das Problem, dass diese unautorisiert benutzt werden kann. Aus dem Stand der
Technik ist gemäß dem Streitpatent bekannt, dass zur Vermeidung dieser
unautorisierten Benutzung der Rechner, auf dem die Software installiert ist, mit
einem Datengenerator verbunden wird. Der Datengenerator empfängt beim
Ausführen der Software Signale des Rechners und gibt definierte Antwortsignale
zurück. Stimmen die Antwortsignale mit den erwarteten Signalen überein, so kann
die Software ausgeführt werden. Werden jedoch falsche Signale zurückgegeben,
so wird die Ausführung der Software gesperrt. Dieses Schutzverfahren kann jedoch durch eine Analyse der Ein- und Ausgabedaten des Datengenerators umgangen werden. Mittels einer solchen Analyse könnte sich das messtechnisch erfasste Ein-/Ausgabeverhalten des Datengenerators mit Hilfe von Logik-Minimierungsverfahren auf einfache Logikfunktionen reduzieren lassen, oder ein Modell
des Datengenerators entwickelt werden, so dass sich der Datengenerator simulieren oder nachbauen lässt (Streitpatent Sp. 1 Z. 16-38). Weiterhin ist im Stand der
Technik auch angegeben, dass ein Öffnen des Gehäuses als Manipulationsversuch erkannt wird (Streitpatent Sp. 2 Z. 5-9); in diesen Fällen gibt der Datengenerator keine oder gefälschte Signale aus.

                                        - 17 -




2. Das Streitpatent nennt Nachteile dieser bekannten Lösungen und stellt sich
die Aufgabe, eine Vorrichtung zum Schutz gegen eine unautorisierte Benutzung
von Software zu schaffen, die eine Analyse der Funktion des Datengenerators
anhand seiner Ein- und Ausgaben bzw. nur seiner Ausgaben äußerst erschwert
(Streitpatent Sp .2 Z. 36-40).



3. Die beanspruchte Lösung besteht i.W. darin, dass der Datengenerator eine
Analyse seiner Funktionen (Manipulationsversuche) erkennt und daraufhin keine
oder fehlerhafte Daten ausgibt (Sp. 2 Z. 46-50), oder die Daten durch andere
Maßnahmen im zurückgesendeten Datenstrom „versteckt“ (Sp. 3 Z. 16 ff., Z. 27
ff.).



Konkret gelöst wird diese Aufgabe u. a. durch die Gegenstände der mit der Nichtigkeitsklage angegriffenen, erteilten nebengeordneten Patentansprüche 1, 3 und
4.


Patentanspruch 1 beschreibt danach eine


        (M1)   Vorrichtung zum Schutz gegen unautorisierte Benutzung
               von Software,


        (M2)   bei der mindestens ein mit einem Signaleingang eines
               Rechensystems (10) verbindbarer


        (M3)   externer Datengenerator (11) Daten erzeugt,


        (M4)   wobei die vom Datengenerator (11) ausgegebenen
               Daten von empfangenen Daten aus dem Rechensystem
               (10) abhängig sind und

                                     - 18 -



    (M5)    das Rechensystem in einen Fehlerzustand gebracht wird
            oder die Software im Rechensystem nicht zweckmäßig
            arbeitet, wenn das Rechensystem keine oder fehlerhafte
            Daten über den Signaleingang (13) empfängt,


    dadurch gekennzeichnet, dass


    (M5a)   der Datengenerator (11) nicht vorgesehene Daten oder
            Datenfolgen und/oder zeitlich nicht vorgesehene Daten
            oder Datenfolgen als Manipulationsversuche erkennt und


    (M5b) bei erkanntem Manipulationsversuch den Inhalt eines
            Speichers im Datengenerator ändert und


    (M5c)   infolgedessen beim Empfang weiterer Daten keine oder
            fehlerhafte     Daten     ausgibt    und/oder     eine
            Benutzerautorisierung verändert.


Patentanspruch 3 beschreibt eine


    (M1)    Vorrichtung zum Schutz gegen unautorisierte Benutzung
            von Software,


    (M2)    bei der mindestens ein mit einem Signaleingang eines
            Rechensystems (10) verbindbarer


    (M3)    externer Datengenerator (11) Daten erzeugt,


    (M4)    wobei die vom Datengenerator (11) ausgegebenen
            Daten von empfangenen Daten aus dem Rechensystem
            (10) abhängig sind und

                                     - 19 -



    (M5)    das Rechensystem in einen Fehlerzustand gebracht wird
            oder die Software im Rechensystem nicht zweckmäßig
            arbeitet, wenn das Rechensystem keine oder fehlerhafte
            Daten über den Signaleingang (13) empfängt,


    insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1 und/oder 2,


    dadurch gekennzeichnet, dass


    (M6)    die vom Datengenerator (11) generierten Daten eine
            nicht-deterministisch erzeugte Redundanz aufweisen.


Patentanspruch 4 beschreibt eine


    (M1)    Vorrichtung zum Schutz gegen unautorisierte Benutzung
            von Software,


    (M2)    bei der mindestens ein mit einem Signaleingang eines
            Rechensystems (10) verbindbarer


    (M3)    externer Datengenerator (11) Daten erzeugt,


    (M4)    wobei die vom Datengenerator (11) ausgegebenen
            Daten von empfangenen Daten aus dem Rechensystem
            (10) abhängig sind und


    (M5)    das Rechensystem in einen Fehlerzustand gebracht wird
            oder die Software im Rechensystem nicht zweckmäßig
            arbeitet, wenn das Rechensystem keine oder fehlerhafte
            Daten über den Signaleingang (13) empfängt,

                                        - 20 -



     insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1, 2 und/oder 3,


     dadurch gekennzeichnet, dass


     (M7a)   der Datengenerator (11) zwei Zustände A und B besitzt,
             von deren Annahme die vom Datengenerator ausgegebenen Daten abhängen,


     (M7b) der Datengenerator aus dem Zustand A in den Zustand
             B nur durch mindestens fünf aufeinanderfolgende weitere
             Zustände C gebracht werden kann, die aufgrund empfangener Daten angenommen werden, und


     (M7c)   die vom Datengenerator ausgegebenen Daten nicht von
             den Zuständen C abhängen.


Die Angabe in den Patentansprüchen 3 und 4, dass der Oberbegriff des Hauptanspruchs insbesondere in Verbindung mit dem Kennzeichen des Anspruchs 1, 2
und/oder 3 zu betrachten sei, stellt ein fakultatives Merkmal dar. Fakultative
Merkmale beschränken den Schutzbereich eines Patentanspruchs nicht und sind
daher nicht weiter zu berücksichtigen (vgl. Schulte PatG, 9. Aufl. (2013), § 34
Rdn. 128).


4. Als Fachmann, der mit der Aufgabe betraut wird, die Analyse einer
Schutzfunktion für Software zu erschweren und damit einen unautorisierten Zugriff
zu verhindern, ist ein Diplomingenieur oder Informatiker mit Erfahrung im
Bereich der Autorisierungsverfahren zur Benutzung von Software anzusehen.


5. Im Lichte der Streitpatentschrift versteht ein solcher Fachmann die beanspruchte Lehre wie folgt:

                                      - 21 -



Gemäß Merkmal (M1) ist eine Vorrichtung zum Schutz gegen unautorisierte Benutzung von Software beansprucht. Hierzu verfügt die Vorrichtung über einen externen Datengenerator, der Daten erzeugt (Merkmal (M3)), und der mit einem Signaleingang eines Rechners verbunden wird (Merkmal (M2)). Im Betrieb empfängt
der Datengenerator Daten von dem Rechensystem und sendet daraufhin Daten
an das Rechensystem zurück, die in Abhängigkeit von den empfangenen Daten
erzeugt werden (Merkmale (M4)). Falls keine Daten zurückgesendet werden oder
die zurückgesendeten Daten nicht den erwarteten Wert haben, d. h. fehlerhaft
sind, wird durch das Rechensystem die weitere Ausführung der Software verhindert (Merkmal (M5)).



Für die Beurteilung der Patentfähigkeit des erteilten Patentanspruchs 1 ist hervorzuheben, dass der Datengenerator Eingabedaten als nicht vorgesehene Daten
/ Datenfolgen bzw. zeitlich nicht vorgesehene Daten / Datenfolgen erkennt. D. h.
die verbesserte Schutzmaßnahme besteht darin, dass – gegebenenfalls zeitlich
beschränkt – nur bestimmte Daten als Eingabedaten für den Datengenerator zulässig sind. Der Datengenerator überprüft die Eingabedaten auf ihre Zulässigkeit
(Merkmal (M5a)) (und sendet nicht nur, wie aus dem Stand der Technik bekannt,
von den Eingabedaten abgeleitete Ausgabedaten zurück). Wenn unzulässige Eingabedaten empfangen werden, wird der Speicher des Datengenerators verändert
(Merkmal (M5b)) und beim Empfang weiterer Daten werden keine bzw. fehlerhafte
Daten ausgegeben und/oder die Benutzerautorisierung wird verändert (Merkmal
(M5c)).


Zur Erläuterung des Begriffes „Manipulationsversuch“ ist noch darauf hinzuweisen,
dass gemäß der Streitpatentschrift bei der Überprüfung der Daten in dem Datengenerator – fälschlicherweise - auch fehlerhafte Übertragungen als „Manipulationsversuch“ gewertet werden (s. Streitpatent Sp. 3 Z. 65-67). D. h. im Mittelpunkt
steht nicht die tatsächliche Erkennung von Manipulationsversuchen, sondern allein
die Überprüfung, ob die (empfangenen) Daten zulässig sind.

                                        - 22 -



Mit dem nebengeordneten Patentanspruch 3 ist als Lösungsalternative beansprucht, dass in einer Vorrichtung mit den Merkmalen (M1) bis (M5) die vom Datengenerator erzeugten Daten eine nicht-deterministisch erzeugte Redundanz
aufweisen (Merkmal (M6)). Von einer Erkennung eines Manipulationsversuchs ist
hier somit keine Rede mehr. Statt dessen sollen die vom Datengenerator an das
Rechensystem zurückgesendeten Daten zunächst die nach Merkmal (M4) auszugebenden Daten umfassen, welche von den aus dem Rechensystem empfangenen Daten abhängig sind, und darüber hinaus weitere Daten, welche eigentlich
„überflüssig“ sind (Redundanz) und zufällige Werte ( = nicht-deterministisch erzeugt) annehmen. Damit werden die „Nutzdaten“ des Merkmals (M4) mit Zufallsdaten erweitert, was eine Analyse erheblich erschwert. Denn ein potentieller Angreifer kann in dem Antwort-Datenblock die zufälligen Daten von den „Nutzdaten“
nicht unterscheiden.


Auf eine weitere Lösungsalternative ist der nebengeordnete Patentanspruch 4
gerichtet. In einer Vorrichtung mit den Merkmalen (M1) bis (M5) soll der Datengenerator als Zustandsautomat ausgelegt sein, welcher Daten in Antwort auf empfangene Daten vom Rechensystem und in Abhängigkeit von diesen (Merkmal
(M4)) in zwei Zuständen A und B erzeugt (Merkmal (M7a)). Diese Zustände A und
B folgen jedoch nicht unmittelbar aufeinander, sondern der Übergang erfolgt über
mindestens fünf Zustände C, die nacheinander jeweils durch den Empfang von
Daten vom Rechensystem eingenommen werden (Merkmal (M7b)). Dabei sollen
die ausgegebenen Daten in den Zuständen C nicht vom Zustand abhängen
(Merkmal (M7c)), d.h. für einen potentiellen Angreifer nicht interpretierbar sein und
so eine Analyse erheblich erschweren, da nur höchstens jeder sechste übermittelte Datenblock „gültige“ Daten enthält.




                                            II.


Die mit der Nichtigkeitsklage angegriffenen Patentansprüche 1, 3, 4, 5 und 8 bis
13 des Streitpatents sind in der erteilten Fassung, sowie in der Fassung der Hilfs-

                                      - 23 -



anträge 1 bis 4 nicht schutzfähig. Die mit Hilfsantrag 5 verteidigte Fassung der
Patentansprüche ist dagegen zulässig und wird dem Fachmann durch den Stand
der Technik nicht nahegelegt. In dieser Fassung ist das Streitpatent somit patentfähig.


1. In der erteilten Fassung (Hauptantrag) hat das Streitpatent keinen Bestand,
weil der Gegenstand des angegriffenen unabhängigen Patentanspruchs 1 Änderungen umfasst, die den Schutzbereich des Patents erweitern (§ 22 (1) PatG).


1.1. In dem ursprünglich erteilten Patent (DE 41 03 173 C2) ist in Anspruch 1
beansprucht, dass „…die vom Datengenerator (11) ausgegebenen Daten von
empfangenen Daten aus dem Rechensystem (10) abhängig sind“ und „dass der
Datengenerator (11) Manipulationsversuche an den empfangenen Daten erkennt…“.
Weiter wird in Unteranspruch 2 des ursprünglich erteilten Patents konkretisiert,
dass „der Datengenerator (11) einen Manipulationsversuch an nicht vorgesehenen
Daten oder Datenfolgen und/oder zeitlich nicht vorgesehenen Daten oder Datenfolgen erkennt“.


1.2.     Dem Patentanspruch 1 des Streitpatents (DE 41 03 173 C3) ist demgegenüber zu entnehmen, dass „der Datengenerator (11) nicht vorgesehene Daten oder
Datenfolgen und/oder zeitlich nicht vorgesehene Daten oder Datenfolgen als Manipulationsversuche erkennt“ (Merkmal (M5a)).


1.3.     Patentanspruch 1 des Streitpatents kann keinen Bestand haben, da sein
Schutzbereich über den Schutzbereich des ursprünglich erteilten Patents hinausgeht (§ 22 (1) PatG).


In diesem Patentanspruch ist nicht mehr spezifiziert, welche Daten vom Datengenerator überprüft werden sollen, bzw. woher diese eigentlich stammen sollen.
Aus dem Patentanspruch 1 in der Fassung des ursprünglich erteilten Patents geht
aber hervor, dass die Daten vom Rechensystem stammen müssen und daher

                                     - 24 -



eben nicht beliebigen Ursprungs sind. Hingegen umfasst der geltende Patentanspruch 1 auch die Möglichkeit, Daten bzw. Datenfolgen auf einem beliebigen anderen Weg in den Datengenerator einzugeben. Dies wäre beispielsweise auch
durch ein Öffnen des Gehäuses des Datengenerators und ein anschließendes
Anlegen von Daten direkt an den internen Signalleitungen des Datengenerators
möglich. Damit fallen in den Schutzbereich des erteilten Patentanspruchs 1 auch
Ausführungsformen, die vom ursprünglich erteilten Patent (DE 41 03 173 C2) nicht
erfasst waren.


1.4.   Die dagegen gerichtete Argumentation der Beklagten vermochte nicht zu
überzeugen.


Die Beklagte führt hierzu aus, dass es sich bei den Daten des Merkmals (M5a)
nach wie vor nur um „empfangene“ Daten (aus dem Rechensystem) handeln
könne. Dies ergebe sich aus dem Kontext der Merkmale (M4) und (M5c) sowie
aus der Beschreibung des Streitpatents, insbesondere Spalte 2 Zeile 51-54,
Spalte 3 Zeile 1-5.


Beispielhafte Angaben aus der Beschreibung rechtfertigen jedoch keine einengende Auslegung eines Patentanspruchs. Und auch der Wortlaut der Merkmale
(M4), (M5a) und (M5c) erlaubt im gegebenen Kontext keine Beschränkung des
Merkmals (M5a) auf empfangene Daten. So wird zwar in Merkmal (M4) spezifiziert, dass die ausgegebenen Daten des Datengenerators von empfangenen Daten des Rechensystems abhängig sind; dieses Merkmal betrifft aber nicht die Erkennung eines Manipulationsversuchs, sondern eine Eigenschaft der ausgegebenen Daten. Merkmal (M5c) beschreibt eine Folge der Erkennung eines Manipulationsversuchs, nämlich im Kontext des Merkmals (M4), dass die Daten des Datengenerators, die als Reaktion auf den Empfang von weiteren Daten des Rechensystems ausgegeben werden, bewusst fehlerhaft ausgelegt werden sollen. Demgegenüber ist nirgendwo spezifiziert, dass die als Manipulationsversuch erkannten
Daten des Merkmals (M5a) explizit „vom Rechensystem empfangene Daten“ sein
müssten. Gerade die von der Beklagten zitierte Spalte 2 Zeile 51-54 des Streitpa-

                                        - 25 -



tents nennt als mögliche Manipulation auch eine Öffnung des Gehäuses des Datengenerators. Damit fällt auch ein Manipulationsversuch durch direktes Einbringen von Daten auf die internen Signalleitungen mit unter den Wortlaut des Merkmals (M5a), was beim ursprünglich erteilten Patent aber nicht der Fall war.


1.5.    Mit dem Patentanspruch 1 fällt der gesamte Hauptantrag. Beantragt der
Patentinhaber, das Patent in beschränktem Umfang mit einem bestimmten Anspruchssatz oder bestimmten Anspruchssätzen aufrechtzuerhalten, rechtfertigt es
grundsätzlich den Widerruf des Patents, wenn sich auch nur der Gegenstand eines Patenanspruchs aus dem vom Patentinhaber verteidigten Anspruchssatz als
nicht patentfähig erweist (vgl. für das Einspruchsbeschwerdeverfahren BGH
GRUR 2007, 862 – Informationsübermittlungsverfahren II, bei Verteidigung des
Patents durch Hilfsanträge auf das Nichtigkeitsverfahren zu übertragen).


2. Die Hilfsanträge 1 bis 4 haben keinen Bestand, da insbesondere der Gegenstand des jeweiligen nebengeordneten Patentanspruchs 4 nicht auf einer erfinderischen Tätigkeit beruht (§ 4 PatG).


2.1.    Patentanspruch 4 des Hilfsantrags 1 hat keinen Bestand, da sein Gegenstand nicht auf einer erfinderischen Tätigkeit beruht.


2.1.1. Für die Beurteilung der erfinderischen Tätigkeit des Patentanspruchs 4, bei
der die fakultativen Merkmale nicht zu berücksichtigen sind, wird von folgender
Gliederung des Anspruchs ausgegangen:


       (M1)   Vorrichtung zum Schutz gegen unautorisierte Benutzung
              von Software,


       (M2)   bei der mindestens ein mit einem Signaleingang eines
              Rechensystems (10) verbindbarer


       (M3)   externer Datengenerator (11) Daten erzeugt,

                                      - 26 -




     (M4)    wobei die vom Datengenerator (11) ausgegebenen
             Daten von empfangenen Daten aus dem Rechensystem
             (10) abhängig sind und


     (M5)    das Rechensystem in einen Fehlerzustand gebracht wird
             oder die Software im Rechensystem nicht zweckmäßig
             arbeitet, wenn das Rechensystem keine oder fehlerhafte
             Daten über den Signaleingang (13) empfängt,


     dadurch gekennzeichnet, dass


     (M7a)   der Datengenerator (11) zwei Zustände A und B besitzt,
             von deren Annahme die vom Datengenerator ausgegebenen Daten abhängen,


     (M7b) der Datengenerator aus dem Zustand A in den Zustand
             B nur durch mindestens fünf aufeinanderfolgende weitere
             Zustände C gebracht werden kann, die aufgrund empfangener Daten angenommen werden, und


     (M7c)   die vom Datengenerator ausgegebenen Daten nicht von
             den Zuständen C abhängen.


2.1.2. Die Merkmale des Patentanspruchs 4 ergeben sich in naheliegender Weise
für den Fachmann aus der Druckschrift NK13.
Denn aus dieser ist eine Vorrichtung zum Schutz von Software gegen unautorisierte Benutzung (Sp. 1 Z. 12-14) zu entnehmen, die einen externen Datengenerator („key generator“ 28) verwendet, der mit dem Rechner („CPU“ 50) über einen
Signaleingang („I/O Port“ 60) verbunden ist (Fig. 3, Sp. 6 Z. 67 – Sp. 7 Z. 12).
Damit sind die Merkmale (M1), (M2) und (M3) bereits bekannt. Weiter wird in der
Druckschrift NK13 beschrieben (Sp. 2 Z. 36-43, Sp. 7 Z. 15-18), dass die vom

                                     - 27 -



Datengenerator ausgegebenen Daten von den empfangenen Daten abhängig sind
(Sp. 2 Z. 36-43, Sp. 4 Z. 40-46 - Merkmal (M4)) und dass die Software im
Rechensystem nicht zweckmäßig arbeitet (Sp. 3 Z. 27-41 - Merkmal (M5)), wenn
das Rechensystem keine oder fehlerhafte Daten von dem Datengenerator über
den Signaleingang empfängt.


Darüber hinaus ist in Druckschrift NK13 ein Zustandsautomat gezeigt (Fig. 2), der
in dem Datengenerator die auszugebenden Daten generiert, wobei der Zustandsautomat einen ersten Zustand, im Folgenden (A) genannt (z. B. Fig. 2 oben links,
Ausgabewert 6), und einen zweiten Zustand, im Folgenden (B) genannt (z. B.
Fig. 2 oben rechts, Ausgabewert 9), annehmen kann. Dabei generiert der Zustandsautomat in beiden Zuständen eine Ausgabe, die vom eingenommenen Zustand abhängig ist (Fig. 2, Sp. 5 Z. 60 – Sp. 6 Z. 8, Sp. 6 Z. 33-64) (Merkmal
(M7a)). Für einen Übergang von Zustand (A) nach Zustand (B) sind mehrere
Wege angegeben. Ein möglicher Übergang von Zustand (A) nach Zustand (B)
führt über einen oder zwei Zwischenzustände, im Folgenden als (C 1), (C2) bezeichnet, die aufgrund empfangener Daten angenommen werden. Empfängt
bspw. der Zustandsautomat in Zustand (A) den Wert „7“ erfolgt ein Übergang nach
Zustand (C1) (Ausgabewert 3), und beim darauffolgenden Empfang des Wertes „9“
wird Zustand (C2) (Ausgabewert 2) erreicht. Von diesem Zustand wechselt der
Zustandsautomat nach Empfang des Wertes „3“ in den Zustand (B). Somit offenbart die Druckschrift NK13 (Sp. 5 Z. 60 – Sp. 6 Z. 8) den Übergang von einem Zustand (A) nach einem Zustand (B) durch mehrere aufeinanderfolgende Zustände
(C), die abhängig von den empfangenen Daten angenommen werden (Fig. 2,
Sp. 5 Z. 48 – Sp. 6 Z. 8).
Die in den Zuständen (C1) und (C2) ausgegebenen Daten haben in diesem Beispiel der Figur 2 einen definierten Wert (3 bzw. 2). Jedoch gibt die Druckschrift
NK13 noch zusätzlich die Lehre, beim Empfang nicht vorgesehener (d. h. unzulässiger) Daten zufällige Daten auszugeben (Sp. 6 Z. 3-5, „…the finite state machine would sense an improper input and would generate some random output“).
Es liegt für den Fachmann nahe, hierfür bestimmte Zustände des Zustandsautomaten vorzusehen, so wie im Beispiel die Zustände (C1) und (C2) (dort für zuläs-

                                       - 28 -



sige Eingabedaten). Wenn der Fachmann aber auch für die Behandlung unzulässiger Eingabedaten solche eigenen Zustände vorsieht, gelangt er zu einem Zustandsautomaten nach Patentanspruch 4, der – im Falle des Empfangs einer bestimmten Kombination von zulässigen und unzulässigen Eingabedaten – von Zustand (A) auch z. B. über fünf Zustände (C) (in denen zufällige Daten ausgegeben
werden) in den Zustand (B) gelangt (Merkmale (M7b) und (M7c)).


2.1.3. Die dagegen gerichtete Argumentation der Beklagten konnte nicht überzeugen.
Nach den Ausführungen der Beklagten ist die Einschränkung auf zwei Zustände
(A) und (B) und die Einnahme von fünf Zuständen (C), sowie der Übergang „nur“
durch mindestens fünf Zustände (C), nicht aus der Druckschrift NK13 zu entnehmen.
Jedoch wird in Druckschrift NK13 der dort gezeigte Zustandsautomat lediglich als
beispielhafte Ausführung beschrieben. Einfache Änderungen des beschriebenen
Zustandsautomaten, insbesondere im Hinblick auf die Anzahl der möglichen Zustände, die Zustandsübergänge bzw. deren Häufigkeit sowie die Art der generierten Daten verlassen nicht den Rahmen des rein fachmännischen Denkens und
Handelns. Auch die Festlegung, dass der Datengenerator nicht anders als („nur“)
durch mindestens fünf Zustände (C) in den Zustand (B) gebracht werden kann,
stellt nicht mehr als eine fachmännische Maßnahme dar.


2.2.     Der Patentanspruch 4 des Hilfsantrags 2 hat ebenso keinen Bestand.
Sein Gegenstand beruht nicht auf einer erfinderischen Tätigkeit, da er mit dem
Patentanspruch 4 des Hilfsantrags 1 übereinstimmt.


2.3.     Die jeweiligen Patentansprüche 4 gemäß Hilfsantrag 3 und 4 sind identisch.
Bei beiden Anträgen hat Patentanspruch 4 keinen Bestand, da sein jeweiliger Gegenstand nicht auf einer erfinderischen Tätigkeit beruht.

                                      - 29 -



Der Patentanspruch 4 unterscheidet sich in beiden Anträgen nur durch die Aufnahme eines fakultativen Merkmals („insbesondere dergestalt …“) von Patentanspruch 4 des Hilfsantrags 1. Wie bereits ausgeführt sind fakultative Merkmale bei
der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen. Damit gilt
aber für den Patentanspruch 4 nach den Hilfsanträgen 3 und 4 nichts anderes als
für den Patentanspruch 4 nach Hilfsantrag 1.


2.4.    Es kann dahingestellt bleiben, ob auch der jeweilige Gegenstand des Patentanspruchs 1 bzw. der jeweilige Gegenstand des Patentanspruchs 3 gemäß
den Hilfsanträgen 1 bis 4 aus dem Stand der Technik nahegelegt ist. Denn mit
dem nebengeordneten Patentanspruch 4 fällt jeweils der gesamte Hilfsantrag (vgl.
oben, Abschnitt 1.5.).


3.      Der einzige Patentanspruch des Hilfsantrags 5 hat Bestand. Die Lehre des
Patentanspruchs ist ausführbar, sein Gegenstand geht nicht über den Inhalt der
ursprünglichen Offenbarung hinaus, und es liegt auch keine unzulässige Erweiterung des Schutzbereichs vor. Ferner ist sein Gegenstand weder durch den Stand
der Technik vorweggenommen noch durch diesen nahegelegt.


3.1.    Der (einzige) Patentanspruch 1 des Hilfsantrags 5, unter Verwendung der
bisherigen Gliederung, lautet:


       (M1)   Vorrichtung zum Schutz gegen unautorisierte Benutzung
              von Software,


       (M2)   bei der mindestens ein mit einem Signaleingang eines
              Rechensystems (10) verbindbarer


       (M3)   externer Datengenerator (11) Daten erzeugt,

                                 - 30 -



(M4)    wobei die vom Datengenerator (11) ausgegebenen
        Daten von empfangenen Daten aus dem Rechensystem
        (10) abhängig sind und


(M5)    das Rechensystem in einen Fehlerzustand gebracht wird
        oder die Software im Rechensystem nicht zweckmäßig
        arbeitet, wenn das Rechensystem keine oder fehlerhafte
        Daten über den Signaleingang (13) empfängt,


dadurch gekennzeichnet, dass


(M5a*) der Datengenerator (11) Manipulationsversuche an den
        empfangenen Daten erkennt, wobei


(M5a)   der Datengenerator (11) nicht vorgesehene Daten oder
        Datenfolgen und/oder zeitlich nicht vorgesehene Daten
        oder Datenfolgen als Manipulationsversuche erkennt und


(M5b) bei erkanntem Manipulationsversuch den Inhalt eines
        Speichers im Datengenerator ändert und


(M5c*) infolgedessen beim Empfang weiterer Daten zeitlich begrenzt nur fehlerhafte Daten ausgibt, wobei


(M6)    die vom Datengenerator (11) generierten Daten eine
        nicht-deterministisch erzeugte Redundanz aufweisen,
        wobei


(M7a)   der Datengenerator (11) zwei Zustände A und B besitzt,
        von deren Annahme die vom Datengenerator ausgegebenen Daten abhängen,

                                       - 31 -



     (M7b) der Datengenerator aus dem Zustand A in den Zustand
             B nur durch mindestens fünf aufeinanderfolgende weitere
             Zustände C gebracht werden kann, die aufgrund empfangener Daten angenommen werden, und


     (M7c)   die vom Datengenerator ausgegebenen Daten nicht von
             den Zuständen C abhängen.


3.2. Die Erfindung nach Patentanspruch 1 des Hilfsantrags 5 ist im Streitpatent so
deutlich und vollständig offenbart, dass ein Fachmann sie ausführen kann (§ 21
Abs. 1 Nr. 2 PatG).


3.2.1. Die   Klägerin    macht    diesbezüglich     geltend,   dass    der    Begriff
„Manipulationsversuch“ in der Beschreibung des Streitpatents als „Analyse der
Funktion des Datengenerators“ definiert sei (Spalte 2 Zeile 43-45); dem Fachmann
sei aber weder die genaue Funktion des Datengenerators bekannt, noch könne er
aus dem Streitpatent eine geeignete Art der Funktionsanalyse entnehmen. Ferner
sei nicht erläutert, wie die Erkennung von „nicht vorgesehenen Daten“ erfolge.
Schließlich werde im Streitpatent auch nicht beschrieben, wie die Daten von dem
Datengenerator „in Abhängigkeit von den empfangenen Daten“ erzeugt würden.


3.2.2. Eine mangelnde Ausführbarkeit der Erfindung lässt sich mit diesen
Argumenten jedoch nicht begründen.


Denn gemäß Patentgesetz muss die Erfindung im Streitpatent deutlich und vollständig offenbart sein, nicht allein in den Patentansprüchen. Ferner richtet sich die
Lehre des Streitpatents an den Fachmann, dessen Fachwissen mit einbezogen
werden kann (vgl. § 21 Abs. 1 Nr. 2 PatG).


Wie der Datengenerator auszugebende Daten derart erzeugt, dass sie „von empfangenen Daten aus dem Rechensystem abhängig sind“, war dem Fachmann aus
dem Stand der Technik geläufig, vgl. etwa Streitpatent Spalte 1 Zeile 16-27 („…

                                        - 32 -



mit einer Rechengröße des Programms und den Daten … eine erste Verknüpfungsfunktion…“) oder die Druckschrift NK13 Zusammenfassung (insbesondere
„… generated as a function of a plurality of words of the input key sequence…“).


Unter einer Analyse der Funktion des Datengenerators ist die Bestimmung seines
Ein-Ausgabeverhaltens zu verstehen, d.h. die Eingabe von Testdaten und die
Auswertung der daraus generierten Ausgabedaten (siehe Streitpatent Spalte 1
Zeile 34-53 – dort sind zwei konkrete Möglichkeiten zur Funktionsanalyse beschrieben).


Wie bereits ausgeführt (s. o. Abschnitt I.5.), beruht nach der Lehre des Streitpatents das Erkennen eines „Manipulationsversuchs“ auf einer Überprüfung, ob es
sich bei den vom Rechensystem empfangenen Daten um „vorgesehene Daten
oder Datenfolgen oder um zeitlich vorgesehene Daten oder Datenfolgen“ handelt;
wenn solche Daten nicht vorliegen, wird dies als „Manipulationsversuch“ gewertet.
Das Streitpatent führt dazu aus (siehe Spalte 2 Zeile 65 – Spalte 3 Zeile 1), dass
nur bestimmte Daten oder Datenfolgen zugelassen sind, oder dass diese nur in
bestimmten Zeitintervallen zugelassen sind. Davon ausgehend ist dem Fachmann
klar, dass es für die vom Rechensystem empfangenen Daten bestimmte Gültigkeitsregeln geben muss, die der Datengenerator kennt und die er überprüfen
kann. Dies genügt für eine Ausführbarkeit der Erfindung. Um welche konkreten
Regeln es sich handelt und nach welcher genauen Funktion der Datengenerator
arbeitet, ist nicht Gegenstand des Streitpatents, sondern bleibt dem Fachmann
überlassen (verlässt auch nicht den Rahmen seines Wissens und Könnens, vgl.
dazu etwa den Zustandsgenerator der Druckschrift NK13 Figur 2, der nur vier erlaubte Datenwerte kennt).


3.3.   Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 5 geht nicht über
den Inhalt der ursprünglichen Offenbarung hinaus (PatG § 21 Abs. 1 Nr. 4) und der
Schutzbereich ist gegenüber dem ursprünglich erteilten Patent (DE 41 03 173 C2)
nicht erweitert (PatG § 22 Abs. 1, 2. Alternative).

                                     - 33 -



3.3.1. Die Klägerin sieht in der Formulierung in Patentanspruch 1 des Streitpatents, wonach „nicht vorgesehene Daten oder Datenfolgen als Manipulationsversuch“ erkannt werden, eine unzulässige Erweiterung, weil nach dem ursprünglich
erteilten Patent diese Erkennung auf „empfangene Daten“ beschränkt gewesen sei
(s. o. II.1.). Weiter führt die Klägerin aus, dass die Verwendung der Bezeichnung
„Manipulationsversuch“ über die Offenbarung der ursprünglich gewählten Bezeichnung „Manipulation“ hinausgeht. Schließlich trägt die Klägerin vor, dass die
Formulierung „beim Empfang weiterer Daten“ in Merkmal (M5c) des Patentanspruchs 1 des Streitpatents (bzw. in Merkmal (M5c**) des Hilfsantrags 5) aus der
ursprünglichen Offenbarung nicht hervorgehe.


3.3.2. Diesen Ausführungen kann nicht gefolgt werden. Durch die Aufnahme von
Merkmal (M5a*) in Patentanspruch 1 des Hilfsantrags 5 ist die Beschränkung der
Erkennung auf „empfangene Daten“ wiederhergestellt. Ferner ist bereits in den
ursprünglichen Unterlagen (bspw. Anspruch 1, oder Seite 5 Absatz 2) die Formulierung „Manipulationsversuch“ enthalten. Die Aufnahme der Formulierung in
Merkmal (M5c**), dass als Folge des Empfangs weiterer Daten zeitlich begrenzt
nur fehlerhafte Daten ausgegeben werden, stellt nach Ansicht des Senats lediglich
eine Präzisierung dar, die sich im Kontext des Anspruchsmerkmals, dass die vom
Datengenerator ausgegebenen Daten von empfangenen Daten aus dem Rechnersystem abhängig sind (ursprünglicher Anspruch 1, jetzt Merkmal (M4)), aus Seite 7
Absatz 2 bzw. Seite 11 Absatz 1 der Anmeldeunterlagen (Anlage N2) ableiten
lässt.


3.4.     Eine Vorrichtung gemäß Patentanspruch 1 des Hilfsantrags 5 ist neu
gegenüber dem Stand der Technik (§ 3 PatG) und beruht auf einer erfinderischen
Tätigkeit (§ 4 PatG).


3.4.1. Als nächstkommender Stand der Technik wird die Druckschrift NK13
angesehen.

                                       - 34 -



Wie bereits dargelegt (vgl. oben Abschnitt 2.1.2) ist in der Druckschrift NK13 eine
Vorrichtung beschrieben, die eine Software vor unautorisierter Benutzung schützt
(Sp. 1 Z. 12-14). Dazu verfügt die Vorrichtung über einen externen Datengenerator, der mit dem Rechensystem über einen Signaleingang verbunden ist (Fig. 2,
Fig. 3: „28“, „50“, „60“, Sp. 6 Z. 67 – Sp. 7 Z. 12 – Merkmale (M1), (M2) und (M3)).
Der Datengenerator empfängt von dem Rechensystem Daten, prüft diese Daten
und generiert daraus Antwortdaten, die zurück an das Rechensystem übertragen
werden. Stimmen die Antwortdaten nicht mit erwarteten Antworten überein, wird
die Software im Rechensystem in einen Fehlerzustand gebracht (Sp. 2 Z. 36-43,
Sp. 4 Z. 40-46, Sp. 4 Z. 49-59, Sp. 7 Z. 15-18 – Merkmale (M4), (M5), (M5a*),
(M5a)). Weiter wird die Verwendung eines Zustandsautomaten, der in Abhängigkeit der empfangenen Daten einen Zustandswechsel durchführen kann, wobei
abhängig von dem eingenommenen Zustand „richtige“ Antwortdaten oder „zufällige“ Daten ausgegeben werden (Fig. 2, Sp. 5 Z. 60 – Sp. 6 Z. 8, Sp. 6 Z. 33-64 –
Merkmale (M7a) bis (M7c)), nahegelegt (vgl. oben Abschnitt 2.1.2). Schließlich ist
auch eine Art der Redundanz ausgeführt, bei der die eigentlichen Daten „von zufälligen fehlerhaften Daten umgeben sind“ (Sp 3. Z. 8-12 – Merkmal (M6) teilweise).


Aus der Druckschrift NK13 sind jedoch die Merkmale (M5b) und (M5c*) nicht zu
entnehmen.


Denn beim dort beschriebenen Zustandsautomaten erfolgt der mögliche Wechsel
von einem Zustand (A) nach einem Zustand (B) über die Zwischenzustände (C)
(siehe oben Abschnitt 2.1.2) nur beim Empfang zulässiger Eingabedaten (siehe
Figur 2, z. B. Eingaben „12“, „3“, „7“ Ausgabe „6“). Wenn unzulässige Eingabedaten empfangen werden, erzeugt der Zustandsautomat zufällige Ausgangsdaten,
ohne jedoch seinen momentanen Zustand zu wechseln (Spalte 6 Zeile 2 – 5).
Wenn man das Zustandsregister des Zustandsautomaten als den mit Merkmal
(M5b) beanspruchten „Speicher im Datengenerator“ versteht, dann ändert sich
dessen Inhalt also – im Gegensatz zum Merkmal (M5b) – nur beim Empfang zu-

                                       - 35 -



lässiger Daten. Irgendein anderer Speicher im Datengenerator, der sich gerade
bei unzulässigen Eingabedaten ändern würde, ist nicht beschrieben.


Auch wenn man – der Argumentation in Abschnitt 2.1.2 folgend – das Vorsehen
eigener Zustände für die zufälligen Ausgangsdaten, zu denen dann bei unzulässigen Eingabedaten gewechselt werden würde, als naheliegend betrachtet, folgt
daraus noch nicht eine Änderung des Inhalt eines Speichers im Datengenerator,
um damit einen erkannten Manipulationsversuch anzuzeigen (wie es Merkmal
(M5b) fordert).


Insbesondere ist der Druckschrift NK13 kein Hinweis zu entnehmen, auf den Empfang unzulässiger Daten, d. h. die Erkennung eines Manipulationsversuches hin
„beim Empfang weiterer Daten zeitlich begrenzt nur fehlerhafte Daten auszugeben“ (Merkmal (M5c*)). Die Druckschrift NK13 gibt hier lediglich die Lehre, genau
einmal mit zufälligen (d.h. fehlerhaften) Daten zu reagieren, beim Empfang weiterer Eingabedaten aber wieder richtige Daten auszugeben, falls es sich dabei um
zulässige Eingabedaten handelt.


Die Merkmale des Patentanspruchs 1 nach Hilfsantrag 5 sind somit nicht vollständig aus der Druckschrift NK13 zu entnehmen. Für den Fachmann wären auch
mehrere Schritte notwendig um in Kenntnis dieser Druckschrift zu den Merkmalen
des Anspruchs zu gelangen. Hierzu müsste der Fachmann die Lehre der Druckschrift NK13 verlassen und darüber hinausgehende Überlegungen anstellen, wofür die Druckschrift keinerlei Hinweise und Anregungen liefert.


3.4.2. Eine Erkennung von Manipulationsversuchen ist auch der Druckschrift
NK12 zu entnehmen. Deren Lehre führt aber nicht so weit, dass der Bestand des
Patentanspruchs 1 nach Hilfsantrag 5 gefährdet wäre.


Die Druckschrift NK12 hat eine Vorrichtung zum Schutz von Software gegen unautorisierte Benutzung zum Gegenstand. Hierzu verwendet die Vorrichtung eine
externe Einheit (Datengenerator), die mit dem Rechensystem über eine Schnitt-

                                      - 36 -



stelle verbunden ist und Daten an das Rechensystem überträgt (Fig. 1, Sp. 2
Z. 31-38, Sp. 3 Z. 49-53 – Merkmale (M1) bis (M3)). Weiterhin beschreibt die
Druckschrift NK12, dass auf eine zulässige (autorisierte) Anfrage an den Datengenerator eine Antwort an das Rechensystem zurück gesendet wird (Sp. 5 Z. 12-
17 – Merkmal (M4)). Nicht zulässige Anfragen werden als Manipulationsversuch
(„violation“) erkannt und gezählt (Sp. 5 Z. 19-37 - Merkmale (M5a*) und (M5a)
teilweise).


Für die weiteren Merkmale finden sich in der Druckschrift NK12 keine Hinweise.


Gemäß der Druckschrift findet ein Stoppen des Betriebs der Software (Merkmal
(M5)) erst nach einem Manipulationsversuch der Stufe III statt (Sp. 6 Z. 33-57),
wobei hierfür eine Vielzahl von unzulässigen Zugriffen stattgefunden haben muss.
Da die Merkmale (M5a*) und (M5a) von (M5) direkt abhängig sind, können diese
Merkmale nur teilweise aus der Druckschrift entnommen werden (siehe oben). Die
Änderung des Speichers und die folgende zeitlich begrenzte Ausgabe fehlerhafter
Daten (Merkmale (M5b) und (M5c*)) sind ebenso wenig aus der Druckschrift zu
entnehmen wie die Merkmale (M6) bis (M7c).


Die Druckschrift NK12 kann daher weder allein noch in Verbindung mit der Druckschrift NK13 den Gegenstand des Patentanspruchs 1 nach Hilfsantrag 5 nahelegen.


3.4.3. Die weiteren im Verfahren genannten Druckschriften kommen dem Gegenstand des Anspruchs nicht näher.


3.4.3.1.      In den Druckschriften NK1, NK2 und NK16 wird ein Verfahren für ein
Lizenzmanagement beschrieben.


Dabei lehrt die Druckschrift NK1 und die Druckschrift NK2, dass auf einem Rechensystem eine Demo-Version einer Software installiert wird, die anfänglich in
vollem Umfang funktionsfähig ist und für eine dauerhafte Verwendung freige-

                                      - 37 -



schalten werden muss. Nach der Freischaltung findet aber keine Überprüfung
über ein externes Gerät mehr statt.


In umgekehrter Weise geht aus der Druckschrift NK16 hervor, dass eine Software
nach der Lizensierung nur für eine begrenzte Benutzung voll funktionsfähig ist. Für
die weitere Benutzung ist ein Datengenerator notwendig, der dem Rechensystem,
abhängig von empfangenen Daten, Daten zurück sendet, damit die Software weiterhin ausgeführt werden kann.


Zumindest die Merkmale (M5c*), (M6) und (M7a) bis (M7c) sind aber aus den
Schriften nicht zu entnehmen.


3.4.3.2.     Aus den Druckschriften NK3, NK9, NK11, NK14 und NK15 ist ein
Schutz von Software durch einen Datengenerator zu entnehmen.


Druckschrift NK3 zeigt, dass Programmwörter eine Zusatzinformation enthalten,
mit der eine logisch richtige Folge der Programmwörter wieder hergestellt wird.
Wird die erwartete (falsche) Reihenfolge der Programmwörter empfangen, wird ein
Störwort generiert, wodurch die Ausführung des Programms verhindert wird. Im
Gegensatz zur vorliegenden Anmeldung wird kein externer Datengenerator verwendet.


Aus der Druckschrift NK9 ist ein Verfahren zu entnehmen, bei dem mit Hilfe eines
mit dem Rechensystem verbundenen externen Gerätes die Sicherheit der
verwendeten Software gewährleistet wird. Das externe Gerät ist aber nur dann in
der Lage Daten an den Rechner zurück zu senden, wenn ein bekannter Datenstrom (stored reference code) empfangen wird.


Das Verfahren gemäß Druckschrift NK11 schützt vor einem unautorisierten
Kopieren von Software, indem während der Ausführung Befehle an den externen
Datengenerator gesendet werden, die dieser entschlüsselt und an den Rechner
zurück überträgt. Erst nach Erhalt dieser Daten kann die Software fehlerfrei aus-

                                     - 38 -



geführt werden. Die Erkennung eines Manipulationsversuchs und insbesondere
die anschließende Reaktion bspw. in Form des Löschens von Daten oder das
zeitlich begrenzte Ausgeben fehlerhafter Daten ist nur in Verbindung mit einem
mechanischen Angriff erläutert.


Für den Schutz der Software wird in der Druckschrift NK14 ein Schlüsselbaustein
(Datengenerator) verwendet, der jedoch nicht extern über eine Schnittstelle mit
dem Rechner verbunden ist, sondern in diesen fest eingebaut ist. Damit ist – im
Sinne der vorliegenden Anmeldung – lediglich eine Vorrichtung zum Schutz von
Software offenbart, die einzelne Details des Streitpatents (wie etwa einen Zustandsautomaten) umfasst, jedoch keine konkretere Übereinstimmung mit der
Lehre des Patentanspruchs 1 aufweist.


Die Lehre der Druckschrift NK15 beruht auf der Verwendung eines Taktsignals für
die Erkennung eines Manipulationsversuchs. Der Datengenerator empfängt zusätzlich zu den Daten ein Taktsignal und sendet die Antwortdaten nach einem
eingestellten Zeitwert zurück. Das Rechensystem wertet die Antwort als zulässig,
wenn der Zeitwert übereinstimmt.
Damit sind aus den genannten Schriften zumindest die Merkmale (M5c*), (M6)
und (M7a) bis (M7c) nicht zu entnehmen.


3.4.3.3.     Die Druckschriften NK4 und NK5 beschreiben die Eigenschaften eines Schutz-Moduls in Form eines Hardware-Dongles.


Das in Druckschrift NK4 gezeigte Kopierschutz-Modul ist als Zwischenstecker für
eine Schnittstelle des Rechners ausgebildet, wobei die Software in einem ersten
Schritt prüft, ob der Stecker verbunden ist und in einem zweiten Schritt
vorgegebene Daten an das Modul sendet und Antwortdaten erhält.


Druckschrift NK5 zeigt den Aufbau und die Funktion mehrerer Schutzmodule, wobei der Kerngedanke die Erkennung eines Ausspähversuchs („attempt to hack it“)
betrifft. Wird ein derartiger Versuch erkannt, werden sogenannte „tamper links“

                                      - 39 -



(Hardwarebrücken) zerstört und das Modul ist nicht mehr benutzbar. Somit ist
aber jede weitere Überprüfung unmöglich.


Aus beiden Schriften sind zumindest die Merkmale (M5c*), (M6) und (M7a) bis
(M7c) nicht zu entnehmen.


3.4.3.4.      In eine gänzlich andere Richtung weist die Lehre der Druckschrift
NK6.


Die Druckschrift NK6 zeigt einen Kopierschutz für einen Datenträger, bei dem eine
Diskette    mit   einem   gespeicherten,   lizensierten   Programm,   mechanisch
beschädigte Speicherbereiche aufweist. Beim Ausführen des Programms versucht
das Programm auf diese Bereiche zu schreiben und die geschriebenen Daten
wieder auszulesen, worauf ein erwarteter Fehler auftritt. Bei einer unrechtmäßig
kopierten Diskette liegt demgegenüber kein defekter Bereich vor, wodurch das
Ausbleiben des erwarteten Fehlers zur Erkennung der falschen Diskette führt.


Dies würde, wenn man den geänderten Aufbau außer Betracht lässt, allenfalls die
Merkmale (M1) bis (M4) und eventuell (M5b) betreffen, alle übrigen Merkmale liegen fern.


3.4.3.5.      Die Druckschriften NK7, NK8 und NK10 sind auf die Verwendung
einer Karte zum Schutz von Software gerichtet.


In Druckschrift NK7 wird die Karte in ein Lesegerät gesteckt, welches mit dem
Rechner des Benutzers der Software verbunden ist. Startet der Benutzer das
Programm, so überprüft dieses, ob die Karte mit dem Rechner verbunden ist,
sendet Daten an die Karte und erhält einen Schlüssel zurück, der die Verwendung
des Programms gestattet.


In ähnlicher Weise beschreibt Druckschrift NK8 ein System mit einem Datenträger
(Karte) zum Schutz gegen unerlaubte Benutzung einer Software, wobei zusätzlich

                                       - 40 -



noch der Schutz der auf der Karte vorhandenen Daten / Programme durch ein
Passwort angegeben ist. Dazu ist ein Zähler für falsche Passwort eingaben vorgesehen (Sp. 8 Z. 34 ff.), wobei beim Überschreiten eines vorgegebenen Wertes die
Karte gelöscht oder gesperrt wird.


Aus der Druckschrift NK10 ist ein Verfahren für einen Zugriffsschutz mit Hilfe einer
Karte zu entnehmen, die mit dem Rechner verbunden wird. Nach Eingabe eines
oder mehrerer Passwörter erfolgt ein Vergleich und nach dem erfolgreichen
Vergleich mit den hinterlegten Passwörtern wird ein Freigabesignal ausgegeben.
Zusätzlich werden fehlerhafte Eingaben erkannt und die Anzahl der fehlerhaften
Eingaben (Manipulationsversuche) wird gespeichert, um nach einer eingestellten
Anzahl die Karte bzw. die Funktion der Karte zu sperren.


Eine Veränderung des Speichers, die Ausgabe fehlerhafter Daten, die Verwendung eines Zustandsautomaten und die Generierung nicht-deterministisch erzeugter Daten gemäß dem Verständnis des Streitpatents ist in keiner dieser
Druckschriften erläutert.


3.4.4. Der dagegen gerichteten Argumentation der Klägerin kann nicht gefolgt
werden.


Die Klägerin führt aus, dass der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 5 weder neu sei noch auf einer erfinderischen Tätigkeit beruhe.


Zu Merkmal (M5b) führt die Klägerin aus, dass aus der Druckschrift NK13 ein Zustandsautomat zu entnehmen sei, dessen Zustände in Registern gespeichert
seien und bei dem folglich bei einem Zustandswechsel eine Änderung des Inhalts
des Registers und somit des Speichers vorliege.


Weiter argumentiert die Klägerin zu Merkmal (M5c*), dass der in Druckschrift
NK13 gezeigte Zustandsautomat ohne erfinderisches Zutun so abgeändert werden könne, dass dieser einer Ausgestaltung mit einer festgelegten Anzahl von Zu-

                                        - 41 -



ständen (C) (beispielsweise 5) entspreche. Diese Anzahl der Zustände (C) sei
gleichzusetzen mit einer zeitlichen Begrenzung der Ausgabe fehlerhafter Daten.


Gemäß der vorliegenden Anmeldung wird der Inhalt eines Speichers nur bei einem erkannten Manipulationsversuch verändert (Merkmal (M5b)). Wie oben dargestellt (siehe Abschnitt 3.4.1.) werden nach der Lehre der Druckschrift NK13 die
Zustandsregister aber nur beim Empfang zulässiger Eingabedaten geändert. Dass
die Erkennung eines Manipulationsversuchs gespeichert würde, ist weder beschrieben, noch liegt es nahe.


Die zeitlich begrenzte Ausgabe fehlerhafter Daten, wie sie in der vorliegenden
Anmeldung angegeben ist, bezieht sich auf eine Zeitvorgabe, die nur nach einem
erkannten Manipulationsversuch und einer daraus resultierenden Speicheränderung wirksam wird (Merkmal (M5c*)). Für eine solche Zeitvorgabe liefert die
Druckschrift NK13 keinerlei Hinweise.


3.4.5. Keine der genannten Druckschriften gibt eine Anregung, eine zeitlich begrenzte Ausgabe fehlerhafter Daten nach einem erkannten Manipulationsversuch
vorzusehen.


Nach allem ist nicht erkennbar, wie der Fachmann in Kenntnis lediglich des aus
den genannten Druckschriften bekannten Standes der Technik zum Gegenstand
nach Patentanspruch 1 gemäß Hilfsantrag 5 hätte gelangen können.

                                     - 42 -



                                       III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 2 Nr. 1
ZPO, die Entscheidung über die vorläufige Vollstreckbarkeit auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                      IV.


Auf die beigefügte Rechtsmittelbelehrung wird verwiesen.




Sredl                 Merzbach    Baumgardt        Dr. Forkel        Hoffmann


                                                                            prö

                                - 43 -




                     Rechtsmittelbelehrung




Gegen dieses Urteil kann das Rechtsmittel der Berufung gemäß
§ 110 PatG eingelegt werden.

Die Berufung ist innerhalb eines Monats nach Zustellung des in
vollständiger Form abgefassten Urteils - spätestens nach Ablauf von
fünf Monaten nach Verkündung - durch einen in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt schriftlich
zum   Bundesgerichtshof,    Herrenstraße    45a,   76133    Karlsruhe,
einzulegen.

Die Berufungsschrift muss

       -   die Bezeichnung des Urteils, gegen das die
           Berufung gerichtet ist, sowie
       -   die Erklärung, dass gegen dieses Urteil Berufung
           eingelegt werde,

enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder
beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit
§ 2 der Verordnung über den elektronischen Rechtsverkehr beim
Bundesgerichtshof und Bundespatentgericht (BGH/BPatGerVV) auf
elektronischem   Weg    zum    Bundesgerichtshof     einzulegen,    wird
hingewiesen (s. www.bundesgerichtshof.de/erv.html)
