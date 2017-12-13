---
ecli: "ECLI:DE:BPatG:2017:131217B18Wpat185.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 185/14"
decided: "2017-12-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=51&nr=29545&anz=809&pos=772&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-12-13_18_W-pat_185_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 185/14 vom 2017-12-13

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 185/14                                                 Verkündet am
_______________                                                 13. Dezember 2017
    (Aktenzeichen)                                                      …




                            BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 11 2004 000 694.5




…




hat der 18. Senat (Techn. Beschwerdesenat) des Bundespatentgerichts auf die
mündliche Verhandlung vom 13. Dezember 2017 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, Dipl.-Phys. Dr. Schwengelbeck und
Dipl.-Ing. Altvater




ECLI:DE:BPatG:2017:131217B18Wpat185.14.0

                                          -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 18. September 2013 aufgehoben und das Patent auf
       der Grundlage der folgenden Unterlagen erteilt:


       -       Patentansprüche 1 und 2, eingereicht in der mündlichen Verhandlung,
       -       Beschreibung   Seiten 1,     3   bis   6,    eingegangen   am
               21. Oktober 2005,     Seite       2,        eingegangen    am
               7. September 2009,
       -       Figuren 1 bis 4, eingegangen am 21. Oktober 2005.



                                    Gründe


                                           I.


Die vorliegende Patentanmeldung 11 2004 000 694.5-53 mit der Bezeichnung


     „Ein Verfahren und eine Vorrichtung zur Verbesserung der Multi-CPU-Systemleistung für Speicherzugriffe“


geht aus einer PCT-Anmeldung (Veröffentlichungsnummer WO 2004/107184 A2)
hervor, die am 12. Mai 2004 unter Inanspruchnahme einer US-amerikanischen
Priorität vom 27. Mai 2003 (US 10/446 986) eingereicht worden ist. Die
Anmeldung ist durch die Prüfungsstelle für Klasse G06 F des Deutschen Patentund Markenamts mit Beschluss vom 18. September 2013 (Verkündung in
Anhörung) zurückgewiesen worden, weil sich die Gegenstände der jeweiligen
Ansprüche 1 gemäß Hauptantrag sowie Hilfsanträgen 1 und 2 in naheliegender

                                         -3-



Weise aus dem Stand der Technik ergeben würden, wobei folgende Druckschrift
zur Begründung der Zurückweisung herangezogen worden ist:


             D6:   US 2003 / 0 070 016 A1.


Im Prüfungsverfahren sind außerdem folgende Druckschriften berücksichtigt worden:


             D1:   US 2003 / 0 065 843 A1,
             D2:   DE 199 83 745 T1,
             D3:   US 4 937 791,
             D4:   US 5 923 857 A und
             D5:   US 2003 / 0 074 504 A1.


Die Beschwerde der Anmelderin richtet sich gegen den vorstehend genannten
Beschluss.


Sie beantragt,


       den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 18. September 2013 aufzuheben und das Patent auf der Grundlage der folgenden Unterlagen zu erteilen:

       -      Patentansprüche 1 und 2, eingereicht in der mündlichen Verhandlung,
       -      Beschreibung   Seiten 1,    3    bis   6,   eingegangen   am
              21. Oktober 2005,        Seite 2,      eingegangen        am
              7. September 2009,
       -      Figuren 1 bis 4, eingegangen am 21. Oktober 2005.

                                        -4-



Patentanspruch 1 lautet unter senatsseitiger Hinzufügung einer Merkmalsgliederung wie folgt:
             „Vorrichtung, umfassend:


      M1     mehrere CPUs (102, 104), die über einen Speicher-Controller-Hub (106) mit einem DRAM-Speicher (108, 406) mit mehreren Speicherbänken gekoppelt sind;


      M2     wobei jede der CPUs mehrere DRAM-Verfolgungsregister (204) aufweist;


      M3     wobei jede der CPUs (102, 104) eingerichtet ist, als Antwort auf
             Empfangen (302) einer Snoop-Adresse (202) von einer der anderen
             CPUs (102, 104) oder anderen Agenten die Snoop-Adresse (202)
             mittels eines Bankdekodierers (208) zu dekodieren (304), um eine
             der Speicherbänke, auf die die andere CPU zugreift, zu bestimmen,
             und ferner eingerichtet ist, anhand der bestimmten Speicherbank eines der DRAM-Verfolgungsregister (204) zu bestimmen, mehrere
             Seítenadressenbits der Snoop-Adresse (202) mittels eines Komparators (210) mit dem Inhalt des DRAM-Verfolgungsregisters (204) zu
             vergleichen (306), um zu bestimmen, ob eine der Snoop-Adresse (202) entsprechende Seite des DRAM-Speichers (108, 406)
             geöffnet ist, und, falls keine Übereinstimmung vorliegt, eine geöffnete
             Seite der Speicherbank zu schließen, eine der Snoop-Adresse (202)
             entsprechende Seite zu öffnen und die Snoop-Adresse (202) in das
             DRAM-Verfolgungsregister (204) zu laden; und


      M4     wobei jede der CPUs (102, 104) ferner eingerichtet ist, Adressen
             ausgehender Transaktionen in einer Transaktionswarteschlange in
             DRAM-Verfolgungsregister (204), die den Speicherbänken der Adressen der Transaktionen entsprechen, zu laden und die ausgehen-

                                        -5-



             den Transaktionen in der Transaktionswarteschlange anhand bereits
             geöffneter Seiten zu ordnen.“


Der nebengeordnete Patentanspruch 2 lautet unter senatsseitiger Hinzufügung
einer Merkmalsgliederung wie folgt:


       N1    „Verfahren zur Ausführung in einem System, das mehrere CPUs enthält, wobei jede der CPUs ein oder mehrere DRAM-Verfolgungsregister enthält und folgende Verfahrensschritte ausführen kann:


       N2    als Antwort auf Empfangen (302) einer Snoop-Adresse (202) von einer der CPUs (102, 104) oder anderen Agenten Dekodieren der
             Snoop-Adresse (202), um eine Speicherbank in einem DRAM-Speicher (108, 406) zu bestimmen;


       N3    Bestimmen eines der DRAM-Verfolgungsregister (204) anhand der
             bestimmten Speicherbank;


       N4    Vergleichen (306) mehrerer Seítenadressenbits der Snoop-Adresse (202) mit dem Inhalt des DRAM-Verfolgungsregisters (204),
             um zu bestimmen, ob eine der Snoop-Adresse (202) entsprechende
             Seite des DRAM-Speichers (108, 406) geöffnet ist, und, falls keine
             Übereinstimmung vorliegt, eine geöffnete Seite der Speicherbank zu
             schließen, eine der Snoop-Adresse (202) entsprechende Seite zu
             öffnen und die Snoop-Adresse (202) in das DRAM-Verfolgungsregister (204) zu laden;


       N5    wobei     Adressen       ausgehender    Transaktionen     in     einer
             Transaktionswarteschlange in den DRAM-Verfolgungsregistern, die
             den Speicherbänken der Adressen der Transaktionen entsprechen,
             geladen werden, und die ausgehenden Transaktionen in der Trans-

                                        -6-



             aktionswarteschlange anhand bereits geöffneter Seiten umgeordnet
             werden.“


Die Beschwerdeführerin vertritt die Auffassung, dass die geltenden Ansprüche
zulässig und patentfähig sind.


Wegen der weiteren Einzelheiten wird auf die Akte verwiesen.




                                      II.


Die zulässige Beschwerde hat in der Sache Erfolg. Denn die zweifelsfrei gewerblich anwendbaren Gegenstände der unabhängigen Patentansprüche 1 und 2 sind
im Lichte der im Verfahren befindlichen Druckschriften neu und beruhen auf einer
erfinderischen Tätigkeit; auch die übrigen Kriterien zur Patenterteilung sind erfüllt
(§§ 1 bis 5, 34 und 38 PatG).


1. Die    vorliegende    Anmeldung     betrifft   gemäß    Beschreibungseinleitung
   Mikroprozessorsysteme und insbesondere Mikroprozessorsysteme, die mit einem Speicher-Controller über einen Systembus betrieben werden können (vgl.
   geltende Beschreibung, S. 1, mittlerer Abs.). Dynamische Direktzugriffsspeicher (DRAMs) könnten demgemäß Speichervorlade-, Aktivierungs-Lese- und
   Schreiboperationen aufweisen. Insbesondere müsse ein Speicher-Controller,
   der eine Speicherbank adressiert, zuerst die Speicherbank vorladen; dann
   müsse die adressierte Seite innerhalb der Bank aktiviert werden, bevor auf die
   adressierte Spalte auf dieser Seite zum Lesen oder Schreiben zugegriffen
   werde. Der Zugriff auf eine offene DRAM-Seite („Page Hit") bedeute, dass der
   Speicher, auf den zugegriffen wird, bereits vorgeladen und aktiviert wurde. Es
   sei möglich, Lese- und Schreiboperationen auf der DRAM-Seite durchzuführen, ohne den Speicher während jedes Speicherzugriffs vorladen oder aktivieren zu müssen. Wenn auf Daten auf einer anderen als der offenen Seite im

                                    -7-



Speicher zugegriffen werde („Page Miss"), müsse die aktuell offene Seite geschlossen werden, bevor die neue Speicherseite vorgeladen und aktiviert werden könne, um Zugriff zu ermöglichen. Das Schreiben der alten Seite auf das
DRAM und das Vorladen und Aktivieren der neuen DRAM-Seiten nehme Zeit
und Speicherbefehlbus-Bandbreite in Anspruch, was wiederum die Zugriffslatenz des Speicherzugriffs erhöhe, woraus sich eine ineffiziente Nutzung des
Speicherbusses und ein Leistungsverlust einer Vorrichtung beziehungsweise
eines Computers ergebe (vgl. geltende Beschreibung, S. 1 und 2, seitenübergreifender Abs.).


Die der Erfindung zugrundeliegende objektive Aufgabe bzw. das zugrundeliegende technische Problem ist darin zu sehen, eine Vorrichtung und ein Verfahren anzugeben, bei dem Verzögerungen beim Öffnen von Speicherseiten vermieden werden, die durch die Begrenzung der Anzahl von geöffneten Speicherseiten und das damit verbundene notwendige Schließen von bereits geöffneten Speicherseiten entstehen.


Als zuständiger Fachmann wird vorliegend ein Diplom-Ingenieur der Fachrichtung Elektrotechnik mit Schwerpunkt Informationstechnik angesehen, der über
mehrjährige Erfahrung auf dem Gebiet der Entwicklung von Speichersystemen
verfügt.


Zur Lösung der Aufgabe ist gemäß Anspruch 1 vorgesehen, dass mehrere
CPUs über einen Speicher-Controller-Hub mit einem DRAM-Speicher mit mehreren Speicherbänken gekoppelt sind, wobei jede der CPUs eine Mehrzahl von
DRAM-Verfolgungsregistern aufweist (Merkmale M1 und M2). Dass jede der
CPUs solche DRAM-Verfolgungsregister ausweist, bedeutet, dass es sich um
dezentrale Verfolgungsregister handelt (vgl. Fig. 1 i. V. m. geltender Beschreibung, S. 4 und 5, seitenübergreifender Abs.). Um eine der Speicherbänke zu
bestimmen, auf die die andere CPU zugreift, ist jede der CPUs eingerichtet, als
Antwort auf das Empfangen einer Snoop-Adresse von einer der anderen CPUs

                                   -8-



bzw. anderen Agenten die Snoop-Adresse mittels eines Bankdekodierers zu
dekodieren. Dabei ist vorgesehen, dass jede der CPUs eingerichtet ist, anhand
der bestimmten Speicherbank eines der DRAM-Verfolgungsregister zu bestimmen und mehrere Seítenadressenbits der Snoop-Adresse mittels eines
Komparators mit dem Inhalt des DRAM-Verfolgungsregisters zu vergleichen,
um zu bestimmen, ob eine der Snoop-Adresse entsprechende Seite des
DRAM-Speichers geöffnet ist. Falls keine Übereinstimmung vorliegt, soll eine
geöffnete Seite der Speicherbank geschlossen werden, während eine der
Snoop-Adresse entsprechende Seite geöffnet und die Snoop-Adresse in das
DRAM-Verfolgungsregister geladen werden soll (Merkmal M3). Zur Lösung der
Aufgabe ist gemäß Anspruch 1 außerdem vorgesehen, dass jede der CPUs
eingerichtet ist, die entsprechenden Adressen ausgehender Transaktionen in
einer Transaktionswarteschlange in DRAM-Verfolgungsregister zu laden und
die ausgehenden Transaktionen in der Transaktionswarteschlange anhand bereits geöffneter Seiten zu ordnen (Merkmal M4).


Zur Lösung der Aufgabe ist gemäß Anspruch 2 zudem ein Verfahren vorgesehen, bei dem in einem System mit mehreren CPUs, die jeweils ein oder mehrere DRAM-Verfolgungsregister aufweisen, eine Dekodierung einer Snoop-Adresse als Antwort auf das Empfangen der Snoop-Adresse von einer der CPUs
oder anderen Agenten vorgesehen ist, um eine Speicherbank in einem DRAM-Speicher zu bestimmen (vgl. Merkmale N1 und N2). Dabei soll eines der
DRAM-Verfolgungsregister anhand von Angaben der Speicherbank bestimmt
werden (Merkmal N3). Hierzu ist ein Vergleich mehrerer Seítenadressenbits
der Snoop-Adresse mit dem Inhalt des DRAM-Verfolgungsregisters vorgesehen, um zu bestimmen, ob eine – der Snoop-Adresse entsprechende – Seite
des DRAM-Speichers geöffnet ist. Falls keine Übereinstimmung vorliegt, ist
vorgesehen, eine geöffnete Seite der Speicherbank zu schließen und eine der
Snoop-Adresse entsprechende Seite zu öffnen sowie die Snoop-Adresse in
das DRAM-Verfolgungsregister zu laden (Merkmal N4). Die Adressen ausgehender Transaktionen, die sich in einer Transaktionswarteschlange in den

                                        -9-



   DRAM-Verfolgungsregistern befinden und die den Speicherbänken der Adressen der Transaktionen entsprechen, sollen dabei geladen werden, wobei die
   ausgehenden Transaktionen in der Transaktionswarteschlange anhand bereits
   geöffneter Seiten umgeordnet werden (Merkmal N5).


2. Die   geltenden   Ansprüche     und Beschreibungsunterlagen         sind   zulässig
   (§ 38 PatG).


   Der geltende Anspruch 1 basiert auf den Merkmalen des ursprünglichen Anspruchs 1, wobei die Merkmale M1 und M2 jeweils zulässige Konkretisierungen in Bezug auf die Kopplung von mehreren CPUs mit einem DRAM-Speicher
   sowie in Bezug auf mehrere zugehörige DRAM-Verfolgungsregister darstellen,
   die der ursprünglichen Beschreibung im Zusammenhang mit der ursprünglichen Figur 1 offenbart sind (vgl. deutsche Übersetzung der urspr. Beschreibung, S. 3 le. Abs. und S. 4 erster vollst. Abs.). Des Weiteren stellen die
   Merkmale M3 und M4 des Anspruchs 1 eine zulässige Präzisierung des Anspruchsgegenstands hinsichtlich der jeweiligen DRAM-Verfolgungsregister im
   Zusammenhang mit Snoop-Adressen und Speicher-Transaktionen dar, die in
   der ursprünglichen Beschreibung offenbart sind (vgl. deutsche Übersetzung
   der urspr. Beschreibung a. a. O. und S. 4 dritter Abs. bis S. 5 dritter Abs.).


   Der nebengeordnete Anspruch 2 basiert auf dem ursprünglichen Anspruch 21,
   wobei die Merkmale N1 bis N4 in Bezug auf die CPUs, die Antwort auf den
   Empfang einer Snoop-Adresse sowie die Bestimmung eines der DRAM-Verfolgungsregister und das Vergleichen mehrerer Seitenadressbits der Snoop-Adresse in zulässiger Weise im Rahmen der ursprünglichen Figur 1 sowie den
   Figuren 3 und 4 im Zusammenhang mit der ursprünglichen Beschreibung präzisiert worden sind (vgl. deutsche Übersetzung der urspr. Beschreibung zu
   Fig. 1 sowie S. 5 le. Abs. bis S. 6 zweiter Abs.). Des Weiteren ist der Anspruch
   im Hinblick auf zugehörige Transaktionen und deren Umordnung auf Basis des
   Offenbarungsgehalts der ursprünglichen Beschreibung in zulässiger Weise

                                       - 10 -



  konkretisiert worden (vgl. deutsche Übersetzung der urspr. Beschreibung, S. 4
  dritter Abs. sowie S. 5 erster Abs., zweiter vollst. Satz).


3. Der Gegenstand des geltenden Patentanspruchs 1 ist neu gegenüber dem
  Stand der Technik gemäß den Druckschriften D1 bis D6 (§ 3 PatG).


  Druckschrift D2, die als nächstliegender Stand anzusehen ist, beschreibt eine
  Speichervorrichtung mit einem Speicher mit mehreren Speicherbänken („Zahl
  N von Speicherbänken in einem Mehrbankspeicher 706“), die über einen Bus
  und eine zentrale „Universalsteuerung 104“ an „Anforderungsgeräte 102“ gekoppelt sind, wobei darauf hingewiesen wird, dass die genannten Anforderungsgeräte Mikroprozessoren darstellen (vgl. Fig. 1B und 7A sowie den zugeh. Text auf S. 13 Z. 1-16, S. 14 Z. 13-20 und S. 22 Z. 22-34). Diese Anforderungsgeräte“ bzw. Mikroprozessoren sind dabei als eine Konfiguration von
  Bus-Agenten bzw. CPUs anzusehen, wie sie im Merkmal M1 aufgeführt sind.
  Dabei wird im Zusammenhang mit dem Status von offenen Speicherseiten
  („OPENPAGE, 1000“) gelehrt, dass Speicherbefehle und folglich auch Speichertransaktionen so geordnet werden können, dass aufeinanderfolgende Befehle nicht auf die gleiche Speicherbank zugreifen (vgl. S. 34 le. Abs. und S. 35
  erster Abs. sowie S. 35 le. Abs. bis S. 37 erster Abs. / vgl. Merkmal M4).
  In Druckschrift D2 findet sich jedoch kein Hinweis darauf, dass jeder der Bus-Agenten bzw. jeder der Mikroprozessoren bzw. CPUs mehrere DRAM-Verfolgungsregister entsprechend Merkmal M2 aufweist. Im Zusammenhang mit der
  Bestimmung, ob Speicherseiten offen sind, werden vielmehr „Seitenregister 704“ aufgeführt, die in einer „Seite-Treffer/Fehlschlag-Steuerung 702“ der
  vorstehend genannten zentralen „Universalsteuerung 104“ enthalten sind (vgl.
  Fig. 1A-B und Fig. 7A sowie S. 22 Z. 22-34). Auch die Merkmale M3 und M4,
  die jede der CPUs und jeweils darin enthaltene DRAM-Verfolgungsregister betreffen, kann der Fachmann Druckschrift D2 nicht entnehmen.

                                    - 11 -



Den weiteren im Verfahren befindlichen Druckschriften D1 und D3 bis D6 ist
ebenfalls kein Hinweis zu entnehmen, dass jede von mehreren CPUs jeweils
DRAM-Verfolgungsregister entsprechend Merkmal M2 bzw. entsprechend den
Merkmalen M3 und M4 aufweist.


Druckschrift D1 beschreibt dabei einen Snoop-Filter in einem Multiprozessorsystem (vgl. Titel und Abstract sowie Fig. 1 und Abs. [0021]). Der Snoop-Filter
bzw. ein Snooping-Vorgang dient hier der Verbesserung bzw. der Erhaltung
der Cachespeicher-Kohärenz („cache coherency“) und damit nicht dem Ordnen
einer Zugriffsreihenfolge bzw. einer Transaktionswarteschlange auf einen
Speicher entsprechend Merkmal M4 (vgl. Abstract und Abs. [0026]). Auch dass
jede von mehreren CPUs („CPU 12A-12-H“) entsprechend den Merkmalen M2
bis M4 DRAM-Verfolgungsregister aufweist, ist Druckschrift D1 weder im Hinblick   auf   die   CPUs   noch   hinsichtlich   eines   Kohärenz-Kontrollmoduls
(„coherency control module“) zu entnehmen (vgl. u. a. Titel und Abstract sowie
Fig. 1 mit Abs. [0021] und [0022] und Fig. 2 mit Abs. [0026] und [0027]).


Druckschrift D3 offenbart einen Speicher („memory 28“), der an eine CPU gekoppelt ist, welche als ein Bus-Agent angesehen werden kann (vgl. Fig. 11 und
Sp. 7 le. Abs. sowie Sp. 8 erster Abs.). Diese CPU weist zwar ein Speicherseiten-Register („page register 32“) auf, in dem aktuell offene Speicherseiten
des Speichers („memory 28“) aufgelistet sind (vgl. Sp. 8 Z. 1-12 und Fig. 11).
Dass jede von mehreren CPUs entsprechend Merkmal M2 bzw. entsprechend
den Merkmalen M3 und M4 DRAM-Verfolgungsregister aufweist, kann der
Fachmann Druckschrift D3 jedoch ebenfalls nicht entnehmen, insbesondere da
die Verwendung der Speicherseitenregister nicht dem Ordnen von Transaktionen entsprechend Merkmal M4, sondern der Wahl des Speicherzugriffsmodus
(„static column mode“) dient (vgl. Abstract).


Druckschrift D4 offenbart im Hinblick auf die vorliegende Patentanmeldung lediglich, dass ein Speicher (u. a. „cache memory“) an eine Konfiguration von

                                         - 12 -



  Agenten („cluster 201 and 202 of agents“) gekoppelt ist, welche auch als Bus-Agenten angesehen werden können, da diese Agenten jeweils Anforderungen
  über einen Bus austauschen (vgl. Fig. 2 und Sp. 4 Z. 35-56). In Bezug auf eine
  Ausgestaltung einer Vorrichtung gemäß Merkmal M2 mit mehreren DRAM-Verfolgungsregistern in mehreren CPUs sowie im Hinblick auf die weiteren
  Merkmale des Anspruchs 1 gibt es jedoch keine weiteren Hinweise.


  Druckschrift D5 beschreibt einen Datenbus-Scheduler („DRAM bus scheduler“)
  für einen Speicher, der verfolgt, ob ein Datenbus für einen Lese- oder
  Schreibvorgang auf einem DRAM-Speicher genutzt worden ist (vgl. u. a.
  Abs. [0029] sowie Fig. 5). DRAM-Verfolgungsregister gemäß Merkmal M2 sowie die Auswertung von Snoop-Adressen oder ein Umordnen von Speichertransaktionen entsprechend den Merkmalen M3 und M4 sind Druckschrift D5
  dabei auch nicht zu entnehmen.


  Druckschrift D6, die dem Zurückweisungsbeschluss zugrunde gelegen hat, beschreibt einen Snoop-Filter in einem Multiprozessor-Bussystem mit mehreren
  Prozessoren bzw. CPUs, die an einen Hauptspeicher mit Speichersegmenten
  („segment of main memory designated as 24A-24E“) gekoppelt sind (vgl. Fig. 1
  sowie Abs. [0018] und [0021]). Dass jeder der Prozessoren bzw. jede der
  CPUs DRAM-Verfolgungsregister entsprechend Merkmal M2 umfassen, ist
  Druckschrift D6 ebenfalls nicht zu entnehmen. Dies gilt in gleicher Weise in
  Bezug auf die weiteren Merkmale M3 und M4 des Anspruchs 1, die Druckschrift D6 nicht zu entnehmen sind, zumal diese auf Verbesserungen der
  Cache-Kohärenz und damit nicht auf ein Umordnen von Speicher-Transaktionen im Sinne des Merkmals M4 abzielt (vgl. Abstract und Abs. [0026]).


4. Der Gegenstand des geltenden Patentanspruchs 1 beruht auch auf einer
  erfinderischen Tätigkeit (§ 4 PatG).

                                          - 13 -



   Wie zuvor bereits ausgeführt, kann der Fachmann dem Stand der Technik gemäß den Druckschriften D1 bis D6 keinen Hinweis entnehmen, dass jede von
   mehreren CPUs mit mehreren DRAM-Verfolgungsregistern auszubilden ist
   (vgl. insbesondere die vorstehenden Ausführungen zu Merkmal M2 wie auch
   zu Merkmal M3). Auch eine Zusammenschau der Druckschriften D1 bis D6
   führt damit nicht zu einer Vorrichtung mit den Merkmalen M2 und M3, auf die
   es   im    Stand    der    Technik       keinen   Hinweis   gibt.   Ein   solcher
   Anspruchsgegenstand ist dem Fachmann auch unter Einbeziehung seines
   Fachwissens nicht nahegelegt.


   Der Gegenstand des Patentanspruchs 1 beruht somit auf einer erfinderischen
   Tätigkeit und ist daher patentfähig.


5. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 2 ist ebenfalls neu gegenüber dem Stand der Technik (§ 3 PatG).


   Wie zuvor unter Ziffer 3 bezüglich den Merkmalen M2 und M3 ausgeführt, ist
   keiner der Druckschriften D1 bis D6 ein Hinweis zu entnehmen, mehrere CPUs
   jeweils mit einem oder mehreren DRAM-Verfolgungsregistern auszubilden.
   Dementsprechend ist auch keiner der Druckschriften D1 bis D6 ein Hinweis auf
   ein Verfahren für ein System mit mehreren CPUs entnommen werden, die jeweils ein oder mehrere DRAM-Verfolgungsregister enthalten, wobei jede CPU
   mitsamt den Verfolgungsregistern die Verfahrensschritte N2 bis N5 ausführt
   (vgl. die Ausführungen unter Ziffer 3 und die dort genannten Zitatstellen bzgl.
   den Druckschriften D1 bis D6, die hier in gleicher Weise gelten).


6. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 3 beruht
   ebenfalls auf einer erfinderischen Tätigkeit (§ 4 PatG).


   Wie vorstehend ausgeführt, kann der Fachmann dem Stand der Technik gemäß den Druckschriften D1 bis D6 keinen Hinweis auf ein Verfahren bezüglich

                                       - 14 -



   einem System mit mehreren CPUs entnehmen, die entsprechend Merkmal N1
   jeweils ein oder mehrere DRAM-Verfolgungsregister enthalten, wobei jede
   CPU mitsamt Verfolgungsregistern die Verfahrensschritte N2 bis N5 ausführen
   kann. Auch eine Zusammenschau der Druckschriften D1 bis D6 führt damit
   nicht zu einem Verfahren mit den Merkmalen N1 bis N5 des Anspruchs 2. Ein
   solches Verfahren ist dem Fachmann auch unter Einbeziehung seines Fachwissens nicht nahegelegt.


   Auch der Gegenstand des geltenden Anspruchs 2 beruht damit auf einer erfinderischen Tätigkeit und ist daher patentfähig.


7. Da die vorgelegten Unterlagen auch den Anforderungen des § 34 PatG genügen, war das Patent im Umfang der geltenden Ansprüche 1 und 2, der geltenden Beschreibung sowie der geltenden Figuren zu erteilen.




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

                                         - 15 -



   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
       war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
       stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
       der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
       sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Wickborn              Kruppa                Dr. Schwengelbeck             Altvater


                                                                               Pr
