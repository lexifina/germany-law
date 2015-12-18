---
ecli: "ECLI:DE:BPatG:2015:181215B18Wpat67.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 67/14"
decided: "2015-12-18"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=56&nr=27919&anz=851&pos=845&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-12-18_18_W-pat_67_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0038.md", "germany/bund/acts/patg/0042.md", "germany/bund/acts/patg/0045.md", "germany/bund/acts/patg/0048.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 18 W (pat) 67/14 vom 2015-12-18

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 67/14                                                   Verkündet am
_______________                                                  18. Dezember 2015
    (Aktenzeichen)                                                       …




                              BESCHLUSS

                            In der Beschwerdesache


              betreffend die Patentanmeldung 11 2005 002 360.5-53

…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 18. Dezember 2015 durch die Vorsitzende
Richterin Dipl.-Ing. Wickborn sowie den Richter Kruppa, die Richterin Dipl.-Phys.
Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater

beschlossen:

        1.   Die Beschwerde wird zurückgewiesen.

        2.   Die Rückzahlung der Beschwerdegebühr wird angeordnet.




BPatG 154
05.11

                                        -2-



                                     Gründe


                                          I.



Die vorliegende Patentanmeldung 11 2005 002 360.5 geht hervor aus einer PCT-Anmeldung      (Veröffentlichungsnummer        WO 2006/039202 A2),         die   am
21. September 2005 unter Inanspruchnahme einer US-amerikanischen Priorität
10/956239 vom 30. September 2004 eingereicht worden ist. Sie trägt in der
deutschen Übersetzung die Bezeichnung


            „Bereitstellung einer Unterstützung für einen Zeitgeber, der
                  einem Virtual-Machine-Monitor zugeordnet ist“.


Die Anmeldung wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts mit Beschluss vom 25. Januar 2010 zurückgewiesen,
weil der Gegenstand des (damals geltenden) jeweiligen Anspruchs 1 nach Hauptund Hilfsantrag im Hinblick auf die im Prüfungsverfahren ermittelten Druckschriften


             D2: US 2004 / 0117532 A1 und
             D3: US 6 401 156 B1


nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Im Prüfungsverfahren war bereits die folgende Druckschrift genannt:


             D1: YOUNIS, M. u. a.: An approach for supporting temporal
                   partitioning and software reuse in integrated modular
                   avionics. In : Proceedings of the Sixth IEEE Real Time

                                        -3-



                     Technology and Applications Symposium, 2000. RTAS
                     2000, Seiten 56 bis 66.


Mit Anlage zur Ladung vom 15. Oktober 2015 hat der Senat auf die Druckschrift


               D4: US 5 023 771 A


hingewiesen.


Die Anmelderin beantragt,


      den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 25. Januar 2010 aufzuheben und das Patent auf der Grundlage der folgenden Unterlagen
      zu erteilen:


      - Patentansprüche 1 bis 21, eingegangen am
       17. Dezember 2015,
       hilfsweise gemäß Hilfsantrag 1
       Patentansprüche 1 bis 21, eingereicht in der mündlichen
       Verhandlung,
       hilfsweise gemäß Hilfsantrag 2
       Patentansprüche 1 bis 21, eingegangen am
       17. Dezember 2015,
       hilfsweise gemäß Hilfsantrag 3
       Patentansprüche 1 bis 21, eingereicht in der mündlichen
       Verhandlung,
       hilfsweise gemäß Hilfsantrag 4
       Patentansprüche 1 bis 21, eingereicht in der mündlichen
       Verhandlung,
       hilfsweise gemäß Hilfsantrag 5

                                        -4-



       Patentansprüche 1 bis 11, eingereicht in der mündlichen
       Verhandlung,


      - Beschreibung   Seite 1,   eingegangen     am     30. März 2009,
       Seite 1a, eingereicht in der mündlichen Verhandlung, Seiten 2
       bis 18, eingegangen am 28. März 2007,


      - Figuren 1 bis 5, eingegangen am 28. März 2007.




Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hauptantrag lautet:


      M1     „Verfahren zum Ausführen eines Virtual-Machine-Monitors auf einer
             Vorrichtung nach Anspruch 8, wobei der Virtual-Machine-Monitor eine
             oder mehrere virtuelle Maschinen (VMs) unterstützt, welche mit
             einem jeweiligen Gast-Standardbetriebssystem assoziiert sind,
      M2     umfassend in der VMM-Zeitgeber-Stützlogik:
      M3     Übergeben (210) der Kontrolle von dem VMM an die VM;
      M4     Feststellen (204), daß eine VMM-Zeitgeberanzeige auf einen freigebenden Wert gesetzt ist;
      M5     Identiﬁzieren (206) eines VMM-Zeitgeberwertes, der von dem VMM
             konfiguriert ist, wobei der VMM-Zeitgeberwert eine Zeit festlegt, zu
             der die Kontrolle an den VMM zurückgegeben werden soll;
      M6     periodisches Vergleichen während des Betriebs der VM eines aktuellen Wertes einer Zeitgeberquelle mit dem VMM-Zeitgeberwert, um
             festzustellen, ob die Zeit erreicht ist, zu der die Kontrolle an den VMM
             zurückgegeben werden soll;
      M7     Erzeugen eines internen Ereignisses, wenn der aktuelle Wert der
             Zeitgeberquelle den VMM-Zeitgeberwert erreicht hat; und

                                      -5-



      M8     Übergeben (220) der Kontrolle an den VMM als Reaktion auf das
             interne Ereignis, ohne eine Ereignishandhabungsprozedur in entweder dem VMM oder dem VM durchzuführen.“




Patentanspruch 5 nach Hauptantrag lautet:


             „Verfahren zum Ausführen eines Virtual-Machine-Monitors auf einer Vorrichtung nach Anspruch 11, wobei der Virtual-Machine-Monitor eine oder
             mehrere virtuelle Maschinen (VMs) unterstützt, welche mit einem jeweiligen Gast-Standardbetriebssystem assoziiert sind, umfassend in der
             VMM-Zeitgeber-Stützlogik:
             Übergeben (210) der Kontrolle dem VMM an die VM;
             Feststellen (204), daß eine VMM-Zeitgeberanzeige auf einen freigebenden Wert gesetzt ist;
             Dekrementieren eines VMM-Zeitgeberwertes nach jeder vordefinierten
             Zahl von Zeitsteuertakten einer Zeitgeberquelle während die VM ausgeführt wird, wobei der VMM-Zeitgeberwert ein Zeitintervall festlegt, an
             dessen Ende die Kontrolle an den VMM zurückgegeben werden soll;
             Erzeugen eines internen Ereignisses, wenn festgestellt ist, daß der VMM-Zeitgeberwert Null erreicht hat; und
             Übergeben (220) der Kontrolle an den VMM als Reaktion auf das interne
             Ereignis, ohne eine Ereignishandhabungsprozedur in entweder dem VMM
             oder dem VM durchzuführen.“

                                       -6-



Patentanspruch 8 nach Hauptantrag lautet:


            „Vorrichtung, umfassend:
            eine Rechenplattform (118) mit einem Speicher (120) und einem Prozessor (118) zur Ausführung eines Virtual-Machine-Monitors (VMM) (112),
            der eine oder mehrere virtuelle Maschinen (VMs) (102, 114) unterstützt,
            welche mit einem jeweiligen Gast-Standardbetriebssystem (104, 106)
            assoziiert sind;
            eine Datenstruktur (124) in dem Speicher, die vom VMM (112) gesteuert
            wird, wobei die Datenstruktur eine VMM-Zeitgeberanzeige und einen
            VMM-Zeitgeberwert speichert, der vom VMM (112) konfiguriert ist wobei
            der VMM-Zeitgeberwert eine Zeit festlegt, zu der die Kontrolle an den
            VMM (112) zurückgegeben werden soll; und wobei
            der Prozessor (118) eine VMM-Zeitgeber-Stützlogik (122) umfasst zum
            Übergeben der Kontrolle vom VMM (122) an eine virtuelle Maschine (VM)
            (102, 114), zum Feststellen, daß die VMM-Zeitgeberanzeige auf einen
            freigebenden Wert gesetzt ist, um periodisch einen aktuellen Wert einer
            Zeitgeberquelle mit dem VMM-Zeitgeberwert zu vergleichen, um festzustellen, ob die Zeit erreicht ist, zu der die Kontrolle an den VMM (112) zurückgegeben werden soll, um ein internes Ereignis zu erzeugen, wenn
            der aktuelle Wert der Zeitgeberquelle den VMM-Zeitgeberwert erreicht
            hat, und um die Kontrolle als Reaktion auf das interne Ereignis an den
            VMM (112) zu übergeben, ohne eine Ereignishandhabungsprozedur in
            entweder dem VMM (112) oder dem VM (102, 114) durchzuführen.“

                                       -7-



Patentanspruch 11 nach Hauptantrag lautet:


             „Vorrichtung, umfassend:
             eine Rechenplattform (118) mit einem Speicher (120) und einem
             Prozessor (118) zur Ausführung eines Virtual-Machine-Monitors (VMM)
             (112), der eine oder mehrere virtuelle Maschinen (VMs) (102, 114)
             unterstützt, welche mit einem jeweiligen Gast-Standardbetriebssystem
             (104, 106) assoziiert sind;
             eine Datenstruktur (124) in dem Speicher, die vom VMM (112) gesteuert
             wird, wobei die Datenstruktur eine VMM-Zeitgeberanzeige speichert; und
             wobei
             der Prozessor (118) eine VMM-Zeitgeber-Stützlogik (122) umfasst zum
             Übergeben der Kontrolle vom VMM an eine virtuelle Maschine (VM) (102,
             114), zum Feststellen, daß die VMM-Zeitgeberanzeige auf einen freigebenden Wert gesetzt ist, um einen VMM-Zeitgeberwert nach jeder vordefinierten Zahl von Zeitsteuertakten einer Zeitgeberquelle zu dekrementieren, während die VM ausgeführt wird, wobei der VMM-Zeitgeberwert
             ein Zeitintervall festlegt, an dessen Ende die Kontrolle an den VMM (112)
             zurückgegeben werden soll, um ein internes Ereignis zu erzeugen, wenn
             festgestellt ist, daß der Zeitgeberwert null erreicht hat, und um die Kontrolle als Reaktion auf das interne Ereignis an den VMM (112) zu übergeben, ohne eine Ereignishandhabungsprozedur in entweder dem VMM
             (112) oder dem VM (102, 114) durchzuführen.“




Patentanspruch 14 nach Hauptantrag lautet:


            „System, umfassend:

            einen Speicher (120) zum Speichern einer Zeitgeberanzeige und
            eines Zeitgeberwertes; und

                                      -8-



            einen Prozessor (118), der mit dem Speicher (120) verbunden ist,
            um die Zeitgeberanzeige zum Feststellen während des Betriebs
            einer virtuellen Maschine (VM) (102, 114) zu verwenden, daß der
            Zeitgeber eines Virtual-Machine-Monitors (VMM) (112) freigegeben
            ist, um periodisch einen aktuellen Wert einer Zeitgeberquelle mit dem
            Zeitgeberwert zu vergleichen und um ein internes Ereignis zu erzeugen, wenn der aktuelle Wert der Zeitgeberquelle den Zeitgeberwert erreicht hat, und um die Kontrolle als Reaktion auf das interne
            Ereignis an den VMM (112) zu übergeben, ohne eine Ereignishandhabungsprozedur in entweder dem VMM (112) oder dem VM (102,
            114) durchzuführen.“




Patentanspruch 17 nach Hauptantrag lautet:


            „System, umfassend:

            einen Speicher (120) zum Speichern einer Zeitgeberanzeige; und

            einen Prozessor (118), der mit dem Speicher (120) verbunden ist,
            um die Zeitgeberanzeige zum Feststellen während des Betriebs
            einer virtuellen Maschine (VM) (102, 114) zu verwenden, daß der
            Zeitgeber eines Virtual-Machine-Monitors (VMM) (112) freigegeben
            ist, um einen VMM-Zeitgeberwert nach jeder festgelegten Zahl von
            Zeitsteuertakten einer Zeitgeberquelle zu dekrementieren, während
            die VM (102, 114) ausgeführt wird, um ein internes Ereignis zu
            erzeugen, wenn festgestellt wird, daß der VMM-Zeitgeberwert null erreicht hat, und um die Kontrolle als Reaktion auf das interne Ereignis
            an den VMM (112) zu übergeben, ohne eine Ereignishandhabungsprozedur in entweder dem VMM (112) oder dem VM (102, 114)
            durchzuführen.“

                                     -9-



Patentanspruch 20 nach Hauptantrag lautet:


             „Maschinenlesbares Medium, das Befehle umfaßt, die bei Ausführung durch ein Verarbeitungssystem bewirken, daß das Verarbeitungssystem ein Verfahren nach Anspruch 1 ausführt.“




Patentanspruch 21 nach Hauptantrag lautet:


             „Maschinenlesbares Medium, das Befehle umfaßt, die bei Ausführung durch ein Verarbeitungssystem bewirken, daß das Verarbeitungssystem ein Verfahren nach Anspruch 11 ausführt.“


Wegen der abhängigen Ansprüche 2 bis 4, 6, 7, 9, 10, 12, 13, 15, 16, 18 und 19
nach Hauptantrag wird auf den Akteninhalt verwiesen.




Der Patentanspruch 1 nach Hilfsantrag 1 entspricht dem Anspruch 1 nach Hauptantrag unter Ersetzung des Merkmals M7 durch das folgende Merkmal (Änderungen gegenüber Merkmal M7 nach Hauptantrag hervorgehoben):


      M7.1   „Erzeugen eines internen Ereignisses, wenn der aktuelle Wert der
             Zeitgeberquelle den VMM-Zeitgeberwert erreicht hat, wobei das
             interne Ereignis keine Durchführung einer Ereignishandhabungsprozedur durch den VMM oder den VM erfordert; und“


Eine entsprechende Ergänzung wurde in den nebengeordneten Ansprüchen 5, 8,
11, 14 und 17 nach Hilfsantrag 1 vorgenommen. Die nebengeordneten Ansprüche
20 und 21 nach Hilfsantrag 1 entsprechen denen des Hauptantrags.

                                        - 10 -



Wegen der abhängigen Ansprüche 2 bis 4, 6, 7, 9, 10, 12, 13, 15, 16, 18 und 19
nach Hilfsantrag 1 wird auf den Akteninhalt verwiesen.




Der Patentanspruch 1 nach Hilfsantrag 2 entspricht dem Anspruch 1 nach Hauptantrag unter Ersetzung der Merkmale M7 und M8 durch die nachfolgend aufgeführten Merkmale (Änderungen gegenüber den Merkmalen M7 und M8 nach
Hauptantrag hervorgehoben):


        M7.2   „Erzeugen eines internen Ereignisses, wenn der aktuelle Wert der
               Zeitgeberquelle den VMM-Zeitgeberwert erreicht hat, wobei das interne Ereignis ein Seitenfehler ist; und
        M8.2   Übergeben (220) der Kontrolle an den VMM als Reaktion auf das
               interne Ereignis, ohne eine Ereignishandhabungsprozedur in entweder dem VMM oder dem VM durchzuführen und durch Durchführen
               eines VM-Austritts und Speichern des VM-Zustands.“


Eine entsprechende Änderung wurde in den nebengeordneten Ansprüchen 5, 8,
11, 14 und 17 nach Hilfsantrag 2 vorgenommen. Die nebengeordneten Ansprüche
20 und 21 nach Hilfsantrag 2 entsprechen denen des Hauptantrags.


Wegen der abhängigen Ansprüche 2 bis 4, 6, 7, 9, 10, 12, 13, 15, 16, 18 und 19
nach Hilfsantrag 2 wird auf den Akteninhalt verwiesen.




Der Patentanspruch 1 nach Hilfsantrag 3 entspricht dem Anspruch 1 nach Hilfsantrag 1 unter Ersetzung des Merkmals M8 durch das nachfolgend aufgeführte
Merkmal (Änderungen gegenüber Merkmal M8 nach Hilfsantrag 1 hervorgehoben):

                                      - 11 -



      M8.3    „Übergeben (220) der Kontrolle an den VMM als Reaktion auf das
              interne Ereignis, ohne eine Ereignishandhabungsprozedur in entweder dem VMM oder dem VM durchzuführen, wodurch ein Lokalisieren
              eines Unterbrechungsvektors durch Durchqueren einer Umleitungsstruktur, Laden eines Status eines Ereignishandhabungsprogramms
              und Beginnen einer Ausführung in einem neuen Code vermieden
              werden.“


Eine entsprechende Ergänzung wurde in den nebengeordneten Ansprüchen 5, 8,
11, 14 und 17 nach Hilfsantrag 3 vorgenommen. Die nebengeordneten Ansprüche
20 und 21 nach Hilfsantrag 3 entsprechen denen des Hauptantrags.


Wegen der abhängigen Ansprüche 2 bis 4, 6, 7, 9, 10, 12, 13, 15, 16, 18 und 19
nach Hilfsantrag 3 wird auf den Akteninhalt verwiesen.




Der Patentanspruch 1 nach Hilfsantrag 4 entspricht dem Anspruch 1 nach Hilfsantrag 3 unter Ersetzung des Merkmals M8.3 durch das nachfolgend aufgeführte
Merkmal (Änderungen gegenüber Merkmal M8.3 nach Hilfsantrag 3 hervorgehoben):


      M8.4    „Übergeben (220) der Kontrolle an den VMM als Reaktion auf das interne Ereignis, ohne eine Ereignishandhabungsprozedur in entweder
              dem VMM oder dem VM durchzuführen, wodurch umfassend ein Lokalisieren eines Unterbrechungsvektors durch Durchqueren einer
              Umleitungsstruktur, Laden eines des Status eines Ereignishandhabungsprogramms und Beginnen einer mit der Ausführung in einem im
              neuen Code vermieden werden, wobei das interne Ereignis durch
              einen VM-Austritt, eine VM-Zustandsspeicherung und Behandlung
              des internen Ereignisses durch den VMM verarbeitet wird.“

                                        - 12 -



Eine entsprechende Änderung wurde in den nebengeordneten Ansprüchen 5, 8,
11, 14 und 17 nach Hilfsantrag 4 vorgenommen. Die nebengeordneten Ansprüche
20 und 21 nach Hilfsantrag 4 entsprechen denen des Hauptantrags.


Wegen der abhängigen Ansprüche 2 bis 4, 6, 7, 9, 10, 12, 13, 15, 16, 18 und 19
nach Hilfsantrag 4 wird auf den Akteninhalt verwiesen.




Anspruch 1 nach Hilfsantrag 5 basiert auf dem Anspruch 8 nach Hauptantrag und
lautet (Änderungen gegenüber dem Anspruch 8 nach Hauptantrag hervorgehoben):


             „Vorrichtung, umfassend:
             eine Rechenplattform (118) mit einem Speicher (120) und einem
             Prozessor (118) zur Ausführung eines Virtual-Machine-Monitors
             (VMM) (112), der eine oder mehrere virtuelle Maschinen (VMs) (102,
             114) unterstützt, welche mit einem jeweiligen Gast-Standardbetriebssystem (104, 106) assoziiert sind;
             eine Datenstruktur (124) in dem Speicher, die vom VMM (112) gesteuert wird, wobei die Datenstruktur eine VMM-Zeitgeberanzeige
             und einen VMM-Zeitgeberwert speichert, der vom VMM (112) konfiguriert ist wobei der VMM-Zeitgeberwert eine Zeit festlegt, zu der die
             Kontrolle an den VMM (112) zurückgegeben werden soll; und wobei
             der Prozessor (118) eine VMM-Zeitgeber-Stützlogik (122) umfasst
             zum Übergeben der Kontrolle vom VMM (112) an eine virtuelle Maschine (VM) (102, 114), zum Feststellen, daß die VMM-Zeitgeberanzeige auf einen freigebenden Wert gesetzt ist, um periodisch einen
             aktuellen Wert einer Zeitgeberquelle mit dem VMM-Zeitgeberwert zu
             vergleichen, um festzustellen, ob die Zeit erreicht ist, zu der die Kontrolle an den VMM (112) zurückgegeben werden soll, um ein internes

                                      - 13 -



            Ereignis zu erzeugen, wenn der aktuelle Wert der Zeitgeberquelle
            den VMM-Zeitgeberwert erreicht hat, wobei das interne Ereignis
            keine Durchführung einer Ereignishandhabungsprozedur durch den
            VMM (112) oder den VM (102, 114) umfassend ein Lokalisieren eines
            Unterbrechungsvektors durch Durchqueren einer Umleitungsstruktur,
            Laden des Status eines Ereignishandhabungsprogramms und
            Beginnen mit der Ausführung im neuen Code erfordert, und um die
            Kontrolle als Reaktion auf das interne Ereignis an den VMM (112) zu
            übergeben, ohne eine Ereignishandhabungsprozedur in entweder
            dem VMM (112) oder dem VM (102, 114) durchzuführen, wobei das
            interne Ereignis durch einen VM-Austritt, eine VM-Zustandsspeicherung und Behandlung des internen Ereignisses durch den VMM
            (112) verarbeitet wird,
            wobei der Prozessor (118) ferner dazu vorgesehen ist, einen Fehler
            zu erfassen, der mit einem Übergang der Kontrolle auf den VMM
            (112) verbunden ist, bevor festgestellt wird, daß der VMM-Zeitgeber
            null erreicht hat, den verringerten VMM-Zeitgeberwert in der Datenstruktur zu speichern, die vom VMM (112) gesteuert ist, und die Kontrolle an den VMM (112) zu übergeben.“


Dieselbe Änderung wurde in dem nebengeordneten Anspruch 4, welcher auf dem
Anspruch 11 nach Hauptantrag basiert, sowie in den nebengeordneten Ansprüchen 7 und 10, welche auf den Ansprüchen 14 und 17 des Hauptantrags basieren,
vorgenommen. Der Anspruchssatz nach Hilfsantrag 5 enthält ferner die abhängigen Ansprüche 2, 3, 5, 6, 8, 9 und 11, zu denen auf den Akteninhalt verwiesen
wird.


Die Beschwerdeführerin macht hierzu geltend, dass die geänderten Anspruchsfassungen zulässig seien und die Gegenstände der Ansprüche neu und erfinderisch
seien.

                                      - 14 -



Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                       II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn die Gegenstände
der jeweiligen Ansprüche 1 nach Hauptantrag sowie nach den Hilfsanträgen 1, 3,
4 und 5 beruhen nicht auf einer erfinderischen Tätigkeit (§ 4 PatG). Der Gegenstand des Anspruchs 1 nach Hilfsantrag 2 wurde gegenüber dem Inhalt der
Anmeldung in der ursprünglich eingereichten Fassung unzulässig erweitert
(§ 38 Satz 1 PatG). Die Fragen der Zulässigkeit der geltenden Ansprüche nach
Hauptantrag und nach den Hilfsanträgen 1, 3, 4 und 5 sowie der Neuheit der Anspruchsgegenstände können somit dahinstehen (vgl. BGH GRUR 1991, 120, 121
li. Sp. Abs. 3 - „Elastische Bandage“). Ebenso kann dahingestellt bleiben, ob die
Gegenstände der geltenden Ansprüche nach Hilfsantrag 2 im Hinblick auf die §§ 1
bis 5 PatG patentfähig sind.



1.    Die Patentanmeldung betrifft virtuelle Maschinen (VM) und die Bereitstellung einer Unterstützung für einen Zeitgeber, der einem Virtual-Machine-Monitor (VMM) zugeordnet ist (vgl. Offenlegungsschrift, Abs. [0001]). Betriebssysteme
und Anwendungssoftware verwendeten normalerweise Zeitgeber, um Aktivitäten
zeitlich einzuordnen und zu optimieren. In einem virtuellen Maschinensystem könne ein Virtual-Machine-Monitor möglicherweise Zeitgeber auf Plattformbasis in
ähnlicher Weise verwenden wie ein herkömmliches Betriebssystem. Ein VMM
könne zum Beispiel Zeitgeber verwenden, um Ressourcen zeitlich zu planen, Sicherheit zu gewährleisten oder für Betriebsqualität zu sorgen (vgl. Offenlegungsschrift, Abs. [0002], [0004]).


Eine Aufgabe ist in der Anmeldung nicht angegeben. Die anhand des jeweiligen
Anspruchs 1 nach Hauptantrag und nach den Hilfsanträgen sich ergebende objek-

                                       - 15 -



tive Aufgabe ist darin zu sehen, für eine Rechenplattform, auf der ein Virtual-Machine-Monitor ausgeführt wird, der eine oder mehrere virtuelle Maschinen
unterstützt, sicherzustellen, dass der Virtual-Machine-Monitor nach einer festgelegten Zeit die Kontrolle von der jeweils aktiven virtuellen Maschine zurückerlangt.


Die Aufgabe soll u. a. durch ein Verfahren mit den Merkmalen des Anspruchs 1
nach Hauptantrag und nach den Hilfsanträgen 1 bis 4 gelöst werden, das zum
Ausführen eines Virtual-Machine-Monitors auf einer Vorrichtung mit einer Rechenplattform mit einem Speicher und einem Prozessor dient, sowie durch eine
Vorrichtung mit den Merkmalen des Anspruchs 1 nach Hilfsantrag 5.


Als Fachmann sieht der Senat einen Ingenieur der Informationstechnik an, der mit
der Programmierung der Prozessoransteuerung in einem System mit virtuellen
Maschinen vertraut ist.




2.    Einige der im jeweiligen Anspruch 1 nach Hauptantrag und nach den Hilfsanträgen 1 bis 5 aufgeführten Merkmale bedürfen der Auslegung.


Unter einem Monitor für virtuelle Maschinen (VMM) wird in der Regel ein Computerprogramm verstanden, das anderen Computerprogrammen (der Gast-Software)
die Abstraktion einer virtuellen Maschine (VM), d. h. eine Emulation von Rechner-Hardware und Betriebssystemen, zur Verfügung stellt und das die Hardwareressourcen des Rechners an die verschiedenen virtuellen Maschinen verteilt (vgl.
auch Abs. [0019] und [0023] der Offenlegungsschrift). In der Anmeldung wird offen
gelassen, ob der VMM als eine Softwareschicht oberhalb des Host-Betriebssystems läuft oder etwa als Hardware implementiert ist, es können auch zwei VMMs
übereinander laufen (vgl. Abs. [0019] der Offenlegungsschrift). Die virtuellen Maschinen sind gemäß Merkmal M1 mit einem jeweiligen Gast-Standardbetriebssystem assoziiert; auf den virtuellen Maschinen läuft weitere Gast-Software, welche

                                        - 16 -



verschiedene Gast-Softwareanwendungen umfasst (vgl. Abs. [0023] und Fig. 1
der Offenlegungsschrift). In der vorliegenden Anmeldung wird als VM-Austritt oder
VM-Ausgang die Übertragung der Steuerung von der Gastsoftware auf den
Monitor für virtuelle Maschinen bezeichnet, während der Übergang der Steuerung
von dem VMM an die Gastsoftware als VM-Eingang oder VM-Eintritt bezeichnet
wird (vgl. Offenlegungsschrift, Abs. [0025] u. [0065], Fig. 3).


Wegen der Bezugnahme auf die Vorrichtung nach Anspruch 8 im jeweiligen
Patentanspruch 1 nach Hauptantrag und nach den Hilfsanträgen 1 bis 4 umfasst
Merkmal M1 auch die im jeweiligen Anspruch 8 beanspruchte Rechnerplattform
mit Speicher und Prozessor zur Ausführung eines VMMs. Aus dem gleichen
Grund umfasst das Merkmal M2, dass die VMM-Zeitgeber-Stützlogik Bestandteil
des Prozessors ist.


Als ein erster Verfahrensschritt erfolgt das Übergeben der Kontrolle von dem Virtual-Machine-Monitor an die virtuelle Maschine, d. h. ein VM-Eingang (vgl. Merkmal M3, Fig. 2 u. 4). Es folgt das Identifizieren eines VMM-Zeitgeberwerts (vgl.
Merkmal M5), worunter ein Wert verstanden wird, der angibt, nach welcher gewünschten Zeit der Monitor für virtuelle Maschinen die Rückgewinnung der
Kontrolle über den Prozessor erhält, d. h. nach welcher Zeit ein VM-Austritt erzeugt werden soll (vgl. Offenlegungsschrift, Abs. [0030]). Eine VMM-Zeitgeberanzeige (vgl. Merkmal M4) soll dagegen festlegen, ob ein VMM-Zeitgeber freigegeben werden soll, d. h. diese Anzeige stellt lediglich einen Ja/Nein-Wert dar, der
es der Verarbeitungslogik erlaubt, festzustellen, ob der Monitor für virtuelle Maschinen einen VMM-Zeitgebermechanismus wünscht oder nicht. Dementsprechend werden in dem in Figur 2 dargestellten Ablauf die den VMM-Zeitgeber betreffenden Verarbeitungsblöcke (Schritte 206, 208, 214) übersprungen, wenn der
Wert der VMM-Zeitgeberanzeige „Nein“ ist (vgl. Offenlegungsschrift, Fig. 2,
Abs. [0039] - [0041], [0044]). Der in den Merkmalen M5 bis M8 festgelegte Verfahrensablauf des Anspruchs 1 erfolgt somit nur, wenn die VMM-Zeitgeberanzeige,
wie in Merkmal M4 ausgedrückt „auf einen freigebenden Wert gesetzt ist“, das

                                      - 17 -



heißt wenn die VMM-Zeitgeberanzeige mit „Ja“ belegt ist. Da der Fall, dass die
VMM-Zeitgeberanzeige nicht auf einen freigebenden Wert gesetzt ist, also mit
„Nein“ belegt ist, in den beanspruchten Verfahren nicht vorgesehen ist, wirkt das
Merkmal M4 in Anspruch 1 nicht beschränkend für das Verfahren.


Als ein internes Ereignis wird in der Anmeldung ein Ereignis bezeichnet, welches
nicht erfordert, dass eine Ereignishandhabungsprozedur – ob vom Monitor oder
alternativ dazu von der virtuellen Maschine – ausgeführt wird (vgl. Offenlegungsschrift, Abs. [0028], [0029]). Mit der in Merkmal M7 gewählten Formulierung des
Erzeugens eines internen Ereignisses, wenn der aktuelle Wert der Zeitgeberquelle
den VMM-Zeitgeberwert erreicht hat, wird somit lediglich besagt, dass innerhalb
der VMM-Zeitgeber-Stützlogik ein Ereignis erzeugt wird (vgl. Merkmal M2 i. V. m.
Merkmal M7), welches dann gemäß Merkmal M8 dazu führt, dass die Kontrolle
(wieder) an den Virtual-Machine-Monitor übergeben wird, welches also zu einem
VM-Austritt führt. Jedes Verfahren, bei dem beim VM-Austritt in der virtuellen Maschine keine weiteren Arbeitsschritte erfolgen, erfüllt somit die als zweite Oder-Variante in Merkmal M8 sowie in Merkmal M7.1 des Hilfsantrags 1 aufgeführte
Bedingung, dass die Kontrolle an den Monitor übergeben wird, ohne eine Ereignishandhabungsprozedur in der virtuellen Maschine durchzuführen.


In den Hilfsanträgen 3, 4 und 5 ist angegeben, dass aufgrund der nicht durchgeführten Ereignishandhabungsprozedur ein Lokalisieren eines Unterbrechungsvektors, ein Laden eines Status eines Ereignishandhabungsprogramms und ein Beginnen einer Ausführung in einem neuen Code vermieden werden (vgl. die Merkmale M8.3 und M8.4 sowie Hilfsantrag 5), was den Ablauf insoweit präzisiert, als
dass beim durch Erreichen des VMM-Zeitgeberwerts verursachten VM-Austritt als
einziger erforderlicher Schritt eine VM-Zustandsspeicherung erfolgt, wie in Merkmal M8.4 gemäß Hilfsantrag 4 und wie in Hilfsantrag 5 angegeben.

                                           - 18 -



3.     Das Verfahren des Patentanspruchs 1 gemäß Hauptantrag beruht für den
Fachmann in Kenntnis der Druckschriften D1 und D4 nicht auf einer erfinderischen
Tätigkeit.


Druckschrift D1 offenbart ein Verfahren zum Ausführen eines Virtual-Machine-Monitors (System Executive SE) auf einer Vorrichtung, umfassend eine Rechnerplattform (hardware platform) mit einem Speicher und einem Prozessor (vgl.
Fig. 7, S. 64, Abschnitt 4.: PowerPC), wobei der Monitor mehrere virtuelle Maschinen (Application partition; virtual machine) unterstützt, welche mit einem Gast-Standardbetriebssystem (real-time operating system) assoziiert sind (vgl. S. 58, li.
Sp., le. Abs. - re. Sp., Z. 2; S. 59, li. Sp., zw. Abs., dritter u. vierter Satz; S. 60, li.
Sp., zw. Abs., zw. Satz; S. 65, re. Sp., fünfter Abs., erster Satz / Merkmal M1).
Dabei übergibt der Monitor SE die Kontrolle an die virtuellen Maschinen (vgl.
S. 61, li. Sp., dr. Abs., erster Satz / Merkmal M3) und ist auch für das Zeitmanagement verantwortlich, wobei jeder virtuellen Maschine ein Zeitschlitz (time
slice) zugewiesen wird (vgl. S. 60, Abschnitt 3.1 Time Management, erster u. zw.
Abs.; S. 58, re. Sp., dr. Abs. zw. Satz). Diese von dem Monitor konfigurierten Zeitschlitze stellen einen festgelegten VMM-Zeitgeberwert im Sinne des Merkmals
Merkmal M5 dar, zu dem die Kontrolle (über die Ressourcen) von der jeweiligen
virtuellen Maschine an den Monitor zurückgegeben werden soll (vgl. Fig. 4, Block
switch out to SysExec; S. 61, li. Sp., dr. Abs. i. V. m. re. Sp., dr. Abs.). Als eine
Ausgestaltung wird beschrieben, dass der Monitor SE während des Betriebs der
virtuellen Maschine mit einem rückwärts zählenden Zeitgeber (countdown timer)
überwacht, ob der für die Ausführung der virtuellen Maschine vorgesehene Zeitrahmen eingehalten wird, was einem periodisches Vergleichen eines aktuellen
Werts einer Zeitgeberquelle (real-time clock) mit dem festgelegten VMM-Zeitgeberwert gemäß Merkmal M6 entspricht (vgl. S. 60, Abschnitt 3.1, erster Abs.,
vierter Satz, u. zw. Abs. zw. Satz; S. 61, li. Sp., dr. Abs. 3. Satz und re. Sp., zw. u.
dr. Abs.: Nticks, parTick). Wenn die Zeit erreicht ist, zu der die Kontrolle an den
Monitor zurückgegeben werden soll, wird ein Interrupt erzeugt (vgl. Fig. 2 u. 4,
S. 61, re. Sp., dr. Abs., zw. Satz: final interrupt). Da als Reaktion auf den Interrupt

                                           - 19 -



die Kontrolle an den Monitor übergeben wird, ohne eine weitere Prozedur in der
virtuellen Maschine durchzuführen, stellt der Interrupt ein internes Ereignis gemäß
Merkmal M7 und gemäß Merkmal M8 in der zweiten Oder-Variante dar (vgl. Fig. 2,
3 u. 4; S. 58, le. Z. - S. 59, li. Sp., Z. 2; S. 61, li. Sp., vierter Abs., dr. Satz). Druckschrift D1 macht keine Angaben dazu, ob das geschilderte Verfahren von einer
Verarbeitungslogik in Hardware, Software oder einer Kombination davon implementiert ist, während in der vorliegenden Anmeldung das Verfahren von der VMM-Zeitgeber-Stützlogik, welche Teil des Prozessors ist (vgl. Anspruch 8), ausgeführt
wird (Merkmal M2 fehlt).


Ausgehend von dem aus Druckschrift D1 bekannten Verfahren steht der Fachmann daher vor der Frage, wie ein Verfahren mit einem Zeitgeber, der einem
Monitor für virtuelle Maschinen zugeordnet ist, zu implementieren ist. Im Stand der
Technik stößt der Fachmann hierzu auf Druckschrift D4, welche einen das Zeitmanagement betreffenden Controller in einem System mit virtuellen Maschinen
beschreibt (vgl. Abstract).


Druckschrift D4 offenbart ein Verfahren zum Ausführen eines Virtual-Machine-Monitors (virtual machine control program / VMCP) auf einer Vorrichtung gemäß
Merkmal M1 (vgl. Fig. 2a/2b, 3a/3b), wobei der Monitor mehrere virtuelle Maschinen mit jeweiligem Gast-Standardbetriebssystem (guest operating system
GOS) unterstützt (vgl. Fig. 2a/2b und Sp. 3, Z. 37 - 41). Das Übergeben der Kontrolle von dem Monitor für virtuelle Maschinen an die jeweilige virtuelle Maschine
wird in der Druckschrift als Wechsel von verschiedenen Betriebsmodi bezeichnet
(vgl. Sp. 3, Z. 18 - 24, Z. 31 - 41: virtual machine monitoring (VMM) mode; virtual
machine operating system (VMOS) mode / Merkmal M3). Bei dem Betrieb der
mehreren virtuellen Maschinen kommen verschiedene Zeitgeber zum Einsatz, insbesondere läuft ein zweiter Zeitgeber B nur dann, wenn das System sich im
VMOS Modus befindet, d. h. nur während des Betriebs der virtuellen Maschine;
dabei zählt ein zugeordnetes zweites Zeitgeber-Register 82 solange herunter, bis
ein zugeordneter zweiter Komparator (Comparator B) durch Vergleichen feststellt,

                                         - 20 -



dass der aktuelle Wert des Zeitgebers B mit einem vorbestimmten Wert übereinstimmt (vgl. Sp. 6, Z. 47 - 63 / Merkmal M6). Dieser vorbestimmte Wert (second
predetermined value) entspricht dabei einem VMM-Zeitgeberwert, welcher die Zeit
festlegt, zu der die Kontrolle an den Monitor zurückgegeben werden soll. Das Verfahren wird durchgeführt von einem Timer Controller 66, der Teil der CPU ist (vgl.
Sp. 5, Z. 47 - 51); dieser Controller stellt eine VMM-Zeitgeber-Stützlogik gemäß
Merkmal M2 dar. Wenn der aktuelle Wert des Zeitgebers B den vorbestimmten
Wert erreicht hat, wird im Timer Controller 66 ein Interrupt (B timer run out signal
as a second interruption signal) erzeugt, was, da es innerhalb der Zeitgeber-Stützlogik (Timer Controller) erfolgt, als ein internes Ereignis gemäß Merkmal M7
anzusehen ist (vgl. Sp. 2, Z. 46 - 57; Sp. 5, Z. 47 - 51; Sp. 6, Z. 59 - 64).


Druckschrift D4 entnimmt der Fachmann somit, dass ein Verfahren mit einem Zeitgeber, der einem Monitor für virtuelle Maschinen zugeordnet ist und der festlegt,
wann die Kontrolle von der virtuellen Maschine wieder an den Monitor zurückgegeben werden soll, in einer Zeitgeberstützlogik der CPU implementiert werden
kann. Wendet er diese Kenntnis bei der Implementierung des aus Druckschrift D1
bekannten Verfahrens zum Ausführen eines Virtual-Machine-Monitors an, das die
Merkmale M1, M3 und M5 bis M8 aufweist, so wird er die Vorrichtung gemäß
Merkmal M2 mit einer Zeitgeber-Stützlogik zur Ausführung des Verfahrens ausstatten. Da das Merkmal M4 für das Verfahren nicht beschränkend wirkt – wie in
Kapitel II. Abschnitt 2. ausgeführt –, ist der Fachmann somit zu einem Verfahren
mit sämtlichen zu berücksichtigenden Merkmalen einer der beanspruchten Alternativen des Anspruchs 1 nach Hauptantrag gelangt.


Die Argumentation der Anmelderin, Druckschrift D1 offenbare weder einen Monitor
für virtuelle Maschinen noch eine virtuelle Maschine, kann nicht überzeugen. Es ist
zwar zutreffend, dass Druckschrift D1 das Problem betrifft, dass aus Sicherheitsgründen verschiedene Anwendungen in einem Flugzeugcomputer nicht miteinander interferieren dürfen. Die hierzu vorgeschlagene Zweischicht-Software-Architektur stellt aber nichts anderes dar als ein virtuelles Maschinensystem, bei dem

                                           - 21 -



die System Executive Schicht den Monitor für virtuelle Maschinen bildet, welcher
den Anwendungsmodulen jeweils eine virtuelle Maschine zur Verfügung stellt (vgl.
S. 58, li. Sp., le. Abs.; S. 60, li. Sp., zw. Abs., zw. Satz; S. 65, re. Sp., fünfter Abs.).
Auch den Ausführungen der Anmelderin in Bezug zu Figur 3 in Druckschrift D1,
dass zwischen den Applikationen ohne Steuerung durch einen Monitor für virtuelle
Maschinen umgeschaltet wird, vermag der Senat nicht zu folgen, denn Druckschrift D1 beschreibt durchgängig ein Verfahren, bei dem die den Monitor für
virtuelle Maschinen darstellende Softwareschicht SE die Herrschaft über das Zeitmanagement und die Vergabe der Ressourcen hat (vgl. S. 61, li. Sp., dr. bis
fünfter Abs.).
Die Anmelderin verweist zwar zutreffend darauf, dass nicht jeder Timer-Interrupt
nach Figur 2 der Druckschrift D1 zu einem VM-Austritt führt, da der Timer-Interrupt
auch in der Virtuellen Maschine (Application Executive) als Zeitgeber Verwendung
findet. Der Fachmann, der bereits zur technischen Umsetzung der Zeitüberwachung Druckschrift D4 heranzieht, entnimmt Druckschrift D4 (vgl. Sp. 6, Z. 47 - 63)
auch die Möglichkeit der exklusiven Zuordnung eines bestimmten Timers in der
Zeitgebelogik zur Überwachung des Zeitgeberwerts. Dadurch wird zudem die
Anforderung eines sofortigen Wechsels nach Erreichen des VMM-Zeitgeberwerts
(Time Slice) in Druckschrift D1 erfüllt und damit eine Reaktion auf das interne
Ereignis ohne Ereignishandhabungsprozedur in der virtuellen Maschine realisiert
(vgl. S. 61, li. Sp. vierter Abs, vierter Satz).


Eine der beanspruchten Alternativen des Verfahrens des Anspruchs 1 nach
Hauptantrag ist für den Fachmann daher in Kenntnis von Druckschrift D1 i. V. m.
Druckschrift D4 nahegelegt, so dass es nicht auf einer erfinderischen Tätigkeit
beruht.


Der Patentanspruch 1 nach Hauptantrag ist somit nicht patentfähig.



4.     Auch die Präzisierung gemäß Anspruch 1 nach Hilfsantrag 1 kann eine
erfinderische Tätigkeit nicht begründen.

                                         - 22 -



Der Patentanspruch 1 nach Hilfsantrag 1 unterscheidet sich von Anspruch 1 nach
Hauptantrag darin, dass in Merkmal M7.1 klargestellt ist, dass ein internes Ereignis eines ist, das keine Durchführung einer Ereignishandhabungsprozedur durch
den VMM oder die VM erfordert.


Ein solches Verständnis des Begriffs „internes Ereignis“ wurde, wie in Kapitel II.
Abschnitt 2. ausgeführt, bereits bei der Auslegung der Merkmale M7 und M8 des
Anspruchs 1 nach Hauptantrag zugrunde gelegt. Somit gilt die zum Anspruch 1
nach Hauptantrag ausgeführte Argumentation (vgl. Kapitel II. Abschnitt 3.) in gleicher Weise für das Verfahren gemäß Anspruch 1 nach Hilfsantrag 1, denn bei
dem in Druckschrift D1 offenbarten Verfahren erfordert der als internes Ereignis
anzusehende Interrupt keine Durchführung einer weiteren Prozedur in der virtuellen Maschine (Merkmal M7.1). Das Verfahren des Anspruchs 1 nach Hilfsantrag 1
ist für den Fachmann daher in Kenntnis von Druckschrift D1 i. V. m. Druckschrift
D4 nahegelegt, so dass es nicht auf einer erfinderischen Tätigkeit beruht.


Der Patentanspruch 1 nach Hilfsantrag 1 ist daher ebenfalls nicht patentfähig.




5.     Der Gegenstand des geltenden Anspruchs 1 nach Hilfsantrag 2 geht über
den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus.


Patentanspruch 1 nach Hilfsantrag 2 gibt in Merkmal M7.2 vor, dass ein internes
Ereignis erzeugt wird, wenn der aktuelle Wert der Zeitgeberquelle den VMM-Zeitgeberwert erreicht hat, wobei – im Unterschied zu Anspruch 1 nach Hauptantrag –
„das interne Ereignis ein Seitenfehler ist“.


Laut ursprünglicher Beschreibung wird in Übereinstimmung mit Merkmal M8 des
Anspruchs 1 nach Hauptantrag und mit Merkmal M8.2 des Anspruchs 1 nach
Hilfsantrag 2 als internes Ereignis ein Ereignis bezeichnet, das keine Durch-

                                      - 23 -



führung einer Ereignishandhabungsprozedur durch den Monitor für virtuelle
Maschinen oder durch die virtuelle Maschine erfordert (vgl. Anmeldeunterlagen,
Abs. [0028]). Zur Erläuterung von internen Ereignissen nennt die Anmeldung als
ein Beispiel einen Seitenfehler, der während der Ausführung einer virtuellen
Maschine auftreten kann (vgl. a. a. O.). Offenbart ist, dass die Verarbeitungslogik
bei Zeitablauf ein internes Ereignis erzeugt und einen VM-Austritt; anschließend
wird die Ausführung im VMM wieder aufgenommen, ohne die Ereignishandhabungsprozedur auszuführen (vgl. Anmeldeunterlagen, Abs. [0028], [0052], [0053]
u. [0057]); damit ist aber nicht offenbart, dass bei Erreichen des VMM-Zeitgeberwerts, d. h. bei einem Zeitablauf, von der VMM-Zeitgeber-Stützlogik zwingend ein
Seitenfehler erzeugt wird (vgl. Merkmal M2 i. V. m. Merkmal M7.2). In der Verallgemeinerung in Merkmal M7.2, dass sämtliche internen Ereignisse einen Seitenfehler darstellen, ist daher eine unzulässige Verallgemeinerung eines Ausführungsbeispiels zu sehen.


Das mit dem Anspruch 1 nach Hilfsantrag 2 beanspruchte Verfahren betrifft in der
Gesamtheit seiner Merkmale somit eine technische Lehre, die der Fachmann den
ursprünglichen Unterlagen nicht als mögliche Ausgestaltung der Erfindung entnehmen kann (BGH, Beschluss vom 11. September 2001 – X ZB 18/00, GRUR 2002,
49, Amtlicher Leitsatz – Drehmomentübertragungseinrichtung; BGH, Urteil vom
5. Juli 2005 – X ZR 30/02, GRUR 2005, 1023, Amtlicher Leitsatz – Einkaufswagen II). Der beanspruchte Gegenstand des Anspruchs 1 nach Hilfsantrag 2
geht daher in unzulässiger Weise über den Inhalt der ursprünglichen Anmeldung
hinaus.


Der Anspruch 1 nach Hilfsantrag 2 ist deshalb nicht gewährbar, weil sein Gegenstand über den Offenbarungsgehalt der ursprünglichen Unterlagen hinaus unzulässig erweitert wurde.

                                       - 24 -



6.    Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 3 beruht nicht auf
einer erfinderischen Tätigkeit, da er sich für den Fachmann in naheliegender
Weise aus dem Stand der Technik ergibt.


Anspruch 1 nach Hilfsantrag 3 unterscheidet sich in Merkmal 8 von Anspruch 1
nach Hilfsantrag 1 in der Angabe, welche konkreten Prozesse vermieden werden,
indem in dem Monitor oder in der virtuellen Maschine keine Ereignishandhabungsprozedur durchgeführt wird, nämlich „ein Lokalisieren eines Unterbrechungsvektors durch Durchqueren einer Umleitungsstruktur, Laden eines Status eines
Ereignishandhabungsprogramms und Beginnen einer Ausführung in einem neuen
Code“.


Bei dem aus Druckschrift D1 bekannten Verfahren wird als Reaktion auf den als
internes Ereignis anzusehenden Interrupt die Kontrolle an den Monitor übergeben,
ohne dass in der virtuellen Maschine eine weitere Prozedur durchgeführt wird, wie
zum Hilfsantrag 1 ausgeführt. Dies impliziert, dass in der virtuellen Maschine weder ein Lokalisieren eines Unterbrechungsvektors, noch das Laden eines Status
eines Handhabungsprogramms oder die Ausführung eines neuen Codes erfolgt
(Merkmal M8.3). Dies gilt auch, wenn der Begriffs „Prozedur“ als – wie von der
Anmelderin angeführt – Teil im Ablauf eines Computerprogramms verstanden
wird. Für die weiteren Merkmale des Anspruchs 1 nach Hilfsantrag 3, welche identisch zu den Merkmalen des Anspruchs 1 nach Hilfsantrag 1 sind, gilt das zum
Hauptantrag und zum Hilfsantrag 1 Ausgeführte.


Das Verfahren des Anspruchs 1 nach Hilfsantrag 3 ist dem Fachmann daher in
Kenntnis von Druckschrift D1 und Druckschrift D4 ebenfalls nahegelegt, so dass
der Patentanspruch 1 nach Hilfsantrag 3 nicht patentfähig ist.

                                       - 25 -



7.       Auch die in den Patentanspruch 1 nach Hilfsantrag 4 zusätzlich aufgenommenen Merkmale können eine erfinderische Tätigkeit nicht begründen.


Anspruch 1 nach Hilfsantrag 4 unterscheidet sich von Anspruch 1 nach Hilfsantrag 3 in der Ergänzung in Merkmal M8.4, wonach „das interne Ereignis durch
einen VM-Austritt, eine VM-Zustandsspeicherung und Behandlung des internen
Ereignisses durch den VMM verarbeitet wird“.


Bei dem in Druckschrift D1 offenbarten Verfahren erfolgt als Reaktion auf den als
internes Ereignis anzusehenden Interrupt ein Übergeben der Kontrolle an den
Monitor für virtuelle Maschinen, was einen VM-Austritt bedeutet, und eine Behandlung des internen Ereignisses durch den Monitor für virtuelle Maschinen nach sich
zieht (vgl. Fig. 2 u. 3); dabei startet der Interrupt unverzüglich einen Kontextwechsel, was nichts anderes bedeutet, als dass die Zustandsvariablen der virtuellen Maschine gespeichert werden (vgl. S. 61, re. Sp., dr. Abs., dr.Satz: The ISR
starts the context-switching procedure once the time-slice expires.; S. 61, li. Sp.,
vierter Abs., dr. u. vierter Satz: … the context-switching to the system executive is
immediately started. … the current state of the partition is saved … / Merkmal
M8.4).


Zu den weiteren Merkmalen des Anspruchs 1 nach Hilfsantrag 4, die denen des
Anspruchs 1 nach Hauptantrag bzw. nach Hilfsantrag 1 bzw. Hilfsantrag 3 entsprechen, wird auf die Ausführungen in den Abschnitten 3., 4. und 6. in Kapitel II.
verwiesen, die hier in gleicher Weise gelten.


Das Verfahren des Anspruchs 1 nach Hilfsantrag 4 ergibt sich für den Fachmann
daher in Kenntnis von Druckschrift D1 und Druckschrift D4 in naheliegender
Weise, so dass es nicht auf einer erfinderischen Tätigkeit beruht.


Der Patentanspruch 1 nach Hilfsantrag 4 ist daher ebenfalls nicht patentfähig.

                                       - 26 -



8.    Der auf eine Vorrichtung gerichtete Patentanspruch 1 nach Hilfsantrag 5 ist
ebenfalls nicht patentfähig.


Das in Druckschrift D1 offenbarte Verfahren wird auf einer Vorrichtung ausgeführt,
welche eine Rechnerplattform mit einem Speicher und einem Prozessor umfasst
(vgl. Fig. 1 u. 7, S. 64, Abschnitt 4. Prototype Implementation: … hardware
platform, CPU Board, PowerPC, Memory …). Bei der Implementierung des Verfahrens greift der Fachmann – wie zum Hauptantrag ausgeführt – auf die aus
Druckschrift D4 bekannte Ausgestaltung zurück, welche einen Prozessor mit einer
VMM-Zeitgeber-Stützlogik umfasst (vgl. Fig. 3a/3b u. Sp. 5, Z. 47 - 53) und bei
welcher eine Datenstruktur im Speicher vom Monitor für virtuelle Maschinen gesteuert wird (vgl. Fig. 2a u. Sp. 4, Z. 28 - 35: Memory, virtual machine control program section (VMCP Section) 35). Damit ist dem Fachmann in Kenntnis von
Druckschrift D1 und Druckschrift D4 auch eine Vorrichtung mit den gegenständlichen Merkmalen des Anspruchs 1 nach Hilfsantrag 5 nahegelegt. Ob die in
Anspruch 1 nach Hilfsantrag aufgenommenen weiteren Merkmale, welche Verfahrensmerkmale darstellen, die Vorrichtung charakterisieren, kann dahin gestellt
bleiben, da auch die Verfahrensmerkmale aus dem Stand der Technik bekannt
bzw. nahegelegt sind:


Bis auf die letzte Merkmalsgruppe entsprechen die Verfahrensmerkmale den
Merkmalen des Anspruchs 1 nach Hilfsantrag 4, so dass hierzu auf die Ausführungen in Kapitel II. Abschnitt 7. verwiesen wird. Gemäß der letzten Merkmalsgruppe soll der Prozessor dazu vorgesehen sein, „einen Fehler zu erfassen, der
mit einem Übergang der Kontrolle auf den VMM (112) verbunden ist, bevor festgestellt wird, dass der VMM-Zeitgeber null erreicht hat, den verringerten VMM-Zeitgeberwert in der Datenstruktur zu speichern, die vom VMM (112) gesteuert ist,
und die Kontrolle an den VMM (112) zu übergeben“. Zur Behandlung von Ausnahmen gibt Druckschrift D1 an, dass diese auch Fehler, wie beispielsweise die Division durch null, umfassende Ereignisse vom Prozessor identifiziert werden sollen
und dass in dem Virtual-Machine-System der Monitor für virtuelle Maschinen als

                                        - 27 -



erster auf die Ausnahmen antworten soll (vgl. S. 63, li. Sp., Z. 1 - re. Sp., Z. 1),
was nichts anderes bedeutet, als dass der Prozessor vorgesehen ist, einen
Fehler, der mit einem Übergang der Kontrolle an den Monitor verbunden ist, jederzeit zu erfassen, also auch bevor der VMM-Zeitgeber den Wert null erreicht hat.
Bei Auftreten einer Ausnahme sieht das in Druckschrift D1 offenbarte Verfahren
eine spezielle Routine vor (Exception Handling Routine EHR), zu deren Ausführung die Kontrolle an den Monitor übergeben wird und bei der der Prozessor-Status abgespeichert wird (vgl. S. 63, li. Sp., dritter u. vierter Abs.). Der Fachmann
entnimmt dieser Vorgehensweise, dass dies auch ein Speichern der das Zeitmanagement betreffenden Werte wie etwa des VMM-Zeitgeberwerts beinhaltet (vgl.
auch Druckschrift D1: S. 61, li. Sp., vierter Abs.), insbesondere, wenn man von
einer Realisierung des Zählers als Teil der CPU im Sinne von Druckschrift D4
ausgeht. Damit ist dem Fachmann aus der Zusammenschau der Druckschriften
D1 und D4 auch eine Vorrichtung mit sämtlichen Merkmalen des Anspruchs 1
nach Hilfsantrag 5 nahegelegt, so dass der Gegenstand des Anspruchs 1 nach
Hilfsantrag 5 nicht auf einer erfinderischen Tätigkeit beruht.


Der Patentanspruch 1 nach Hilfsantrag 5 ist damit nicht patentfähig.




9.     Mit den jeweils nicht patentfähigen Ansprüchen 1 nach Hauptantrag und
nach den Hilfsanträgen 1 und 3 bis 5 und mit dem nicht zulässigen Anspruch 1
nach Hilfsantrag 2 sind auch die zu diesen nebengeordneten Ansprüche sowie die
auf diese Ansprüche direkt oder indirekt rückbezogenen Unteransprüche nicht
schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war (vgl. BGH, Beschluss vom 27. Juni 2007 – X ZB 6/05, GRUR 2007, 862
Abschnitt III. 3. a) aa) – Informationsübermittlungsverfahren II).

                                       - 28 -



10.    Nachdem die jeweiligen Anspruchssätze nach Hauptantrag bzw. nach den
Hilfsanträgen 1 bis 5 nicht schutzfähig sind, war die Beschwerde zurückzuweisen.




                                         III.


Die Rückzahlung der Beschwerdegebühr war nach § 80 Abs. 3 PatG anzuordnen.


Nach dieser Vorschrift kann die Rückzahlung der Beschwerdegebühr angeordnet
werden, wenn dies der Billigkeit entspricht. Dies kommt insbesondere bei Verfahrensfehlern oder unsachgemäßer Sachbehandlung in Betracht (vgl. Schulte/Püschel, PatG, 9. Aufl., § 80 Rdn. 111 - 113 und § 73 Rdn. 131 ff.; Busse/Engels,
PatG, 7. Aufl., § 80 Rdn. 90 ff.).


Im angefochtenen Beschluss liegen Verfahrensfehler vor (Schulte/Püschel,
a. a. O., § 73 Rdn. 142, 145; Schulte/Rudloff-Schäffer, a. a. O., § 48, Rdn. 14;
Busse/Engels, a. a. O., § 80 Rdn. 98). Das rechtliche Gehör wurde verletzt, da die
Prüfungsstelle auf die mit Schriftsatz vom 21. Dezember 2009 neu eingereichten
Ansprüche nach (damals geltendem) Hilfsantrag erstmals im Beschluss eingegangen ist.



Der Grundsatz der Gewährung rechtlichen Gehörs beinhaltet, dass sich der Einzelne vor einer Entscheidung, die seine Rechte betrifft, zum Verfahren und seinem
voraussichtlichen Ergebnis äußern kann. Damit darf eine Entscheidung nur auf
Gründen beruhen, zu denen sich der Beteiligte äußern konnte. Dies umfasst denknotwendig, dass sie ihm zuvor mitgeteilt werden müssen. Ausfluss dieses Grundsatzes sind u. a. die Vorschriften der § 42 Abs. 3 Satz 2 PatG, § 45 Abs. 2 PatG
und § 48 Satz 2 PatG (vgl. Schulte/Rudloff-Schäffer, a. a. O., § 48 Rdn. 14 ff.). Die
Anmelderin konnte sich aber im vorliegenden Verfahren nicht zu den Gründen, auf

                                        - 29 -



denen der Zurückweisungsbeschluss in Bezug auf den Hilfsantrag vom
21. Dezember 2009 beruht, äußern.


Die Prüfungsstelle hat in ihrem Beschluss zu dem mit Schriftsatz vom
21. Dezember 2009 neu eingereichten Anspruch 1 nach Hilfsantrag erstmals im
Beschluss Stellung genommen und damit ihre Entscheidung auf Umstände
gestützt, die der Anmelderin noch nicht mitgeteilt waren. Im Zurückweisungsbeschluss hat die Prüfungsstelle ausgeführt, soweit erkennbar handele es sich bei
dem Patentanspruch 1 nach Hilfsantrag lediglich um eine Umformulierung des Anspruchs 1 in Verbindung mit Anspruch 8 des Hauptantrags, die jedenfalls keine
darüberhinausgehende Überlegung zu einem technischen Effekt erkennen lasse.
Ob dies für einzelne Merkmale des Hilfsantrags zutrifft, kann dahingestellt bleiben,
da der Anspruch 1 nach Hilfsantrag sich von dem Anspruch 1 nach Hauptantrag
mindestens in der letzten Merkmalsgruppe unterschied, wonach das Verfahren ein
„Ausführen eines VM-Austritts durch Zurückgeben der Steuerung von der VM an
den VMM als Reaktion auf ein Ereignis, das zu dem VM-Eintritt, der an dem VM
auftritt, in Beziehung steht“ umfasst. Zu diesem Merkmal ist im Prüfungsverfahren
nicht Stellung genommen worden. Ob ein Merkmal eine sinnvolle Einschränkung
des Anspruchsgegenstands darstellt oder einen technischen Effekt erkennen
lässt, ist bei der Prüfung der Verletzung des rechtlichen Gehörs unbeachtlich. Die
Behandlung des Hilfsantrags stellt eine Verletzung des rechtlichen Gehörs dar,
denn die Prüfungsstelle hätte die Anmelderin vor einer endgültigen Zurückweisung
darüber informieren müssen, dass sie die Patentfähigkeit des neuen Hilfsantrags
ebenso bewertet wie die des Hauptantrags, für den sie im vorangegangenen Anhörungsprotokoll vom 27. Mai 2009 das Fehlen einer erfinderischen Tätigkeit bemängelt hatte. Für die Rückzahlung der Gebühr ist unbeachtlich, ob die Begründung zum Hauptantrag und zum Hilfsantrag selbst inhaltlich überhaupt vertretbar
ist (Schulte/Püschel, a. a. O., § 73 Rdn. 137).

                                        - 30 -



                                         IV.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
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

                                     - 31 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen
beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Wickborn              Kruppa       Dr. Otten-Dünnweber                 Altvater


                                                                            Hu
