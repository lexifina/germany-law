---
ecli: "ECLI:DE:BPatG:2014:010414B17Wpat2.10.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 2/10"
decided: "2014-04-01"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=18&nr=26032&anz=1119&pos=280&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-04-01_17_W-pat_2_10_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 2/10 vom 2014-04-01

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 2/10                                                     Verkündet am
_______________                                                       1. April 2014
    (Aktenzeichen)                                                          …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 10 2007 034 480.7


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 1. April 2014 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,      der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel


beschlossen:


                      Die Beschwerde wird zurückgewiesen.




BPatG 154
05.11

                                       -2-



                                     Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 20. Juli 2007 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


       „Verfahren zur Steuerung von datenbankübergreifenden Routinen.“


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 29. Juni 2009 mit der Begründung
zurückgewiesen, dass im Gegenstand des Patentanspruchs 1 nur ein Programm
für eine Datenverarbeitungsanlage als solches gesehen werden könne, das
gemäß den Ausschlusskriterien des § 1 Abs. 3 Nr. 3 i. V. m. Abs. 4 PatG dem
Patentschutz nicht zugänglich sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellt den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        gemäß Hauptantrag mit
        Patentansprüchen 1-14 vom 02.06.2010,
        Beschreibung Seiten 1-15 und
        3 Blatt Zeichnungen mit 3 Figuren, jeweils vom Anmeldetag;


        gemäß Hilfsantrag 1 mit
        Patentansprüchen 1-4, überreicht in der mündlichen Verhandlung,
        im Übrigen wie Hauptantrag, mit anzupassender Beschreibung.

                                           -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind die
Druckschriften


D1: Wikipedia: “Simple Network Management Protocol” vom 26.07.2007,
08:03


und


D2: ROSE, M.: “SNMP MUX Protocol and MIB”, Network Working Group,
Request       for   Comments       (RFC)    1227,   May    1991,   <Im    Internet:
http://www.faqs.org/ftp/rfc/pdf/rfc1227.txt.pdf>


genannt worden. Vom Senat wurden zusätzlich die Druckschriften


D3: WO 96/21190 A1


und


D4: US 6 510 421 B1


eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet (mit markierten redaktionellen Änderungen):


      (a)     „Verfahren zur Steuerung von datenbankübergreifenden Routinen, um
              Daten in einer Mehrzahl von Datenbankeinheiten (30, 30´, 30´´, 30´´´)
              quasi parallel zu manipulieren,
      wobei

                                  -4-



(b)    an einer Zentraleinheit (10) eine Mehrzahl von Eingabesystemen
        (20) angeschlossen ist,


(c)    jede Datenbankeinheit (30, 30´, 30´´, 30´´´) eine Datenbank (31, 31´,
        31´´, 31´´´), ein Applikationselement (32, 32´, 32´´r, 32´´´) und eine
        auf dem Applikationselement (32, 32´, 32´´, 32´´´) ausführbare
        Applikationsroutine (33) aufweist,


(d)    jeder Datenbankeinheit (30, 30´, 30´´, 30´´´) eine eindeutige
        Informationsklasse (40, 40´, 40´´, 40´´´) zugeordnet ist,


(e)    in jeder Datenbankeinheit (30, 30´, 30´´, 30´´´) Informationselemente
        (41, 41´) einer eindeutigen Informationsklasse (40, 40´, 40´´, 40´´´)
        hinterlegt sind,


wobei das Verfahren die folgenden Schritte umfasst:


(f)    mittels eines Eingabesystems (20) wird eine Informationsgruppe (35)
        in die Zentraleinheit (10) eingegeben, wobei die Informationsgruppe
        (35) mehrere Informationselemente (41, 41´) beinhaltet und jedes
        Informationselement (41, 41´) einer Informationsklasse (40, 40´, 40´´,
        40´´´) zugeordnet ist.,


(g)    in einer Zuordnungsroutine (11) in der Zentraleinheit (10) wird die
        Informationsgruppe (35) in die Informationselemente (41, 41´)
        zerlegt,


(h)    die Zuordnungsroutine (11) übermittelt die Informationselemente (41,
        41´) in Abhängigkeit von der Informationsklasse (40, 40´, 40´´, 40´´´)
        an die der Informationsklasse (40, 40´, 40´´, 40´´´) zugeordnete
        Datenbankeinheit (30, 30´, 30´´, 30´´´),

                                         -5-



     (i)     die Applikationsroutinen (33) in den Datenbankeinheiten (30, 30´,
             30´´,   30´´´)   zerlegen   die   Informationselemente     (41,   41´)    in
             Subelemente (42, 42´),


     (j)     die Subelemente (42, 42´) werden quasi parallel in den Datenbanken
             (31, 31´, 31´´, 31´´´) verarbeitet.“


In Hinblick auf die Patentansprüche 2 bis 14 wird auf die Akte verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag 1 (im Folgenden einfach als Hilfsantrag
bezeichnet) enthält neben den Merkmalen (a) bis (j) gemäß Hauptantrag noch die
folgenden, mit einer möglichen Gliederung versehenen Merkmale (mit markierten
redaktionellen Änderungen):


     (k)     „wobei ein Subelement (42, 42´) eine Abfrage oder eine Angabe
             enthält, derart, daß eine Verarbeitung eines Subelementes (42, 42´)
             zu einer Veränderung eines in der Datenbank (31, 31´, 31´´, 31´´´)
             hinterlegten Datensatzes führt,


     (l)     eine Koordinatorroutine (15) überwacht, daß alle oder keines der
             Subelemente (42, 42´) in den Datenbanken (31, 31´, 31´´, 31´´´)
             quasi    parallel   verarbeitet    werden   bzw.   wird,     wobei       die
             Koordinatorroutine in der Zentraleinheit (10) ausgeführt wird,


     (m)     vor einer Verarbeitung der Subelemente (42, 42´). die Subelemente
             (42, 42´) sowie der hinterlegte Datensatz gespeichert werden,


     (n)     die Subelemente (42, 42´) verarbeitet werden,

                                        -6-



     (o)     die Koordinatorroutine eine Zustimmung oder eine Ablehnung zu
             einer Festschreibung der Verarbeitung der Subelemente (42, 42´)
             von allen Datenbanken (31, 31´,31´´, 31´´´) einholt,


     (p)     nur bei einer einheitlichen Zustimmung jede Datenbank (31, 31´,
             31´´, 31´´´) von der Koordinatorroutine informiert wird, daß die
             Verarbeitung der Subelemente (42, 42´) durchgeführt wird, und


     (q)     der hinterlegte Datensatz gelöscht wird,


     (r)     bei einer nicht einheitlichen Zustimmung der Datenbank (31, 31´,
             31´´, 31´´´) die Verarbeitung der Subelemente (42, 42´) als nicht
             durchgeführt gilt und keine Verarbeitung der Subelemente (42, 42´)
             und/oder keine Übermittlung der Informationselemente (41, 41´)
             ausgeführt wird und


     (s)     eine Dispatcherroutine (36) für eine Übermittlung der Subelemente
             (42, 42´) an die Datenbank (31, 31´, 31´´, 31´´´) genutzt wird, wobei
             die Dispatcherroutine (36) die Subelemente (42, 42´) in eine
             Übermittlungswarteschlange einordnet wobei eine Mehrzahl von
             Datenbankroutinen (34, 34´) auf jeder Datenbank (31, 31´, 31´´,
             31´´´) ausgeführt wird.“


In Hinblick auf die Patentansprüche 2 bis 4 wird auf die Akte verwiesen.


Die Anmelderin trägt vor, dass der Gegenstand der Anmeldung eine datenbankübergreifende quasi parallele Verarbeitung von Informationsgruppen ermögliche. Dies geschehe durch eine Aufspaltung in unterschiedliche Informationselemente. Die Verwendung einer Dispatcherroutine erlaube zudem eine quasi
parallele und sichere Verarbeitung von Informationsgruppen auf einer Mehrzahl

                                       -7-



von Datenbankeinheiten. Darüber hinaus sichere eine zentrale Koordinatorroutine
eine fehlerfreie Bearbeitung der Informationselemente.


Der Gegenstand nach Patentanspruch 1 sei nicht nur dem Patentschutz grundsätzlich zugänglich, er sei darüber hinaus neu und beruhe auch auf erfinderischer
Tätigkeit.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da die jeweiligen Verfahren des Patentanspruchs 1 gemäß
Haupt- und Hilfsantrag nicht auf erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in
Verbindung mit § 4 Satz 1 PatG).


1.     Die vorliegende Patentanmeldung betrifft ein Verfahren zur Steuerung von
datenbankübergreifenden Routinen.


Ausweislich der Patentanmeldung würden heutzutage für individuelle Informationsklassen, z. B. unterschiedliche Kundenarten, häufig separate und eigenständige Datenbankeinheiten aufgebaut. Dabei könnten mittels eines Eingabesystems Informationen in die verschiedenen Datenbankeinheiten eingegeben
werden, wobei im Allgemeinen jede der Informationsklassen ein individualisierendes Attribut aufweise. Bei einem solchen Attribut könne es sich z. B. um den
Typ eines Vertrages eines Kunden mit einem Telekommunikationsunternehmen
handeln. Mittlerweile würden moderne Telekommunikationsunternehmen eine
Vielzahl von unterschiedlichen Vertragstypen anbieten. So könne z. B. ein
Gesprächsguthaben im Vorhinein käuflich erworben und danach verbraucht
werden. Von einem solchen Prepaid Vertrag unterscheide sich die Möglichkeit, mit
dem Telekommunikationsunternehmen eine feste Vereinbarung abzuschließen
und die in Anspruch genommene Dienstleistung im Nachhinein zu bezahlen. Für

                                        -8-



jeden Vertragstyp eines Kunden sei eine individuelle Datenbankeinheit zur
Speicherung der Kundendaten aufgebaut worden. Dabei sei es bislang unmöglich,
die unterschiedlichen Datenbankeinheiten synchron/zeitnah zu betreiben (Offenlegungsschrift, [0002]).


Die der Anmeldung zugrundeliegende objektive Aufgabe sieht der Senat darin, in
einem aus mehreren Datenbanken bestehenden Datenbanksystem unter Berücksichtigung komplizierter Datenzusammenhänge Datenbestände, z. B. Kundendaten von Mobilfunknetzbetreibern, ressourcensparend und schnell zu bearbeiten,
ohne dass auf Datenbanksynchronisierungen gewartet werden muss.


Als Fachmann, der mit der Aufgabe betraut wird, ein System zur Verwaltung von
Kundendaten zu verbessern, ist ein Systemprogrammierer anzusehen, welcher
über eine langjährige Berufserfahrung in der Entwicklung von Informationssystemen, insbesondere relationalen Datenbanksystemen, verfügt.


2.    Zu Haupt- und Hilfsantrag


Die jeweiligen Gegenstände des Patentanspruchs 1 gemäß Haupt- und Hilfsantrag beruhen bei Berücksichtigung nur derjenigen Merkmale, die die Lösung
eines konkreten technischen Problems mit technischen Mitteln bestimmen oder
zumindest beeinflussen (BGH GRUR 2011, 125 – Wiedergabe topografischer
Informationen), nicht auf erfinderischer Tätigkeit (§ 4 Satz 1 PatG).


2.1   Zur Lehre des Patentanspruchs 1.


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hauptantrag ein Verfahren zur Steuerung von datenbankübergreifenden Routinen
mit den Merkmalen (a) bis (j) vor.

                                       -9-



Das beanspruchte Verfahren dient dazu, eine datenbankübergreifende Koordinatorroutine, also eine Software, so bereitzustellen und zu steuern, dass die in
einer Mehrzahl von Datenbankeinheiten gespeicherten Daten „quasi parallel“
manipuliert, d. h. verarbeitet werden können. Laut Beschreibung weist jede
Datenbankeinheit eine Datenbank, d. h. die eigentliche Datenbasis, sowie ein
Applikationselement auf. Bei dem Applikationselement handelt es sich um eine
Systemkomponente, auf der eine Applikationsroutine in Form einer Softwareroutine ausgeführt wird (Offenlegungsschrift, [0005]). Eine „quasi parallele“
Verarbeitung bzw. ein „quasi paralleler“ Datenbankzugriff i. S. d. Anmeldung
bedeutet nichts Anderes, als dass die für den Zugriff zuständigen Routinen
innerhalb einer für ein Datenverarbeitungssystem geringen Zeitspanne annähernd
gleichzeitig bearbeitet werden (Offenlegungsschrift, [0006] – Merkmal (a)). Aus der
Beschreibung geht implizit hervor, dass der Begriff „quasi parallele“ Verarbeitung
keine Verarbeitung in Echtzeit bedeutet; vielmehr ist damit gemeint, dass eine
Datenbankoperation auf einer zweiten Datenbankeinheit gestartet werden kann,
noch bevor die Datenbankoperation auf einer ersten Datenbankeinheit komplett
abgeschlossen ist (Offenlegungsschrift, [0007]).


Merkmal (b) besagt, dass an einer Zentraleinheit eine Mehrzahl von Eingabesystemen angeschlossen sein soll. Aus der Beschreibung geht hierzu hervor, dass
es sich bei der Zentraleinheit entweder um eine einzelne Hardwarekomponente
oder um mehrere untereinander synchronisierte, dezentral verteilte Subkomponenten handeln kann (Offenlegungsschrift, [0010]). Eingabesysteme sind
gemäß Beschreibung Terminals bzw. Rechner, die bei einem Einzelhändler
aufgestellt sind und mit dem Zentralrechner eines Herstellers oder Dienstleistungsanbieters verbunden sind. Alternativ kommen als Eingabesysteme
Notebooks, PDAs oder Handys in Frage, welche mittels drahtloser Kommunikation
Information an die Zentraleinheit übersenden können (Offenlegungsschrift, [0008],
[0009]).

                                       - 10 -



Wie bereits oben ausgeführt, soll jede Datenbankeinheit eine Datenbank und ein
Applikationselement aufweisen. Auf dem Applikationselement wird eine Applikationsroutine, also Software ausgeführt (Offenlegungsschrift, [0005] – Merkmal (c)).


Gemäß Merkmal (d) ist jeder Datenbankeinheit eine eindeutige Informationsklasse
zugeordnet. Damit ist gemeint, dass jede Datenbankeinheit für eine Informationsklasse, wie z. B. einen Vertragstyp eines Mobilfunknetzbetreibers, erstellt ist
und die für diese Informationsklasse hinterlegten Informationen speichert (Offenlegungsschrift, [0006]).


Die einer Informationsklasse zugeordneten Informationen sind als sogenannte
Informationselemente in einer Datenbankeinheit abgelegt (Merkmal (e)).


Nach Merkmal (f) wird von einem Benutzer mit Hilfe eines Eingabesystems eine
Informationsgruppe in die Zentraleinheit eingegeben. Die Informationsgruppe
zeichnet sich im Wesentlichen dadurch aus, dass sie mehrere Informationselemente umfasst und jedes Informationselement zu einer Informationsklasse
(z. B. Prepaid Vertrag) gehört.


Die eingegebene Informationsgruppe wird in der Zentraleinheit mit Hilfe der
Zuordnungsroutine in die einzelnen Informationselemente zerlegt (Merkmal (g)).


Die Informationselemente werden dann entsprechend ihrer Zugehörigkeit zu den
Informationsklassen an die zuständigen Datenbankeinheiten und dort an deren
Applikationselemente übermittelt (Offenlegungsschrift, [0010] – Merkmal (h)).


In der einer Informationsklasse zugeordneten Datenbankeinheit findet eine weitere
Aufteilung der Informationselemente in Subelemente statt, und zwar mittels der
auf dem Applikationselement gespeicherten Applikationsroutine (Offenlegungsschrift, [0007], [0011] – Merkmal (i)). Die Subelemente enthalten hierbei eine

                                       - 11 -



Abfrage oder eine Angabe und werden im Wesentlichen synchron, also „quasi
parallel“ in den Datenbanken verarbeitet (Offenlegungsschrift, [0007], [0011] –
Merkmal (j)).


Der Patentanspruch 1 gemäß Hilfsantrag unterscheidet sich vom Hauptantrag
durch die Merkmale (k) bis (s), wonach die beanspruchten Datenbankeinheiten im
Wesentlichen über ein „Two-Phase-Commit“ Protokoll gesteuert werden (Offenlegungsschrift, [0023]), und an jeder Datenbankeinheit eine Dispatcherroutine zur
Übermittlung von Subelementen an die Datenbank vorgesehen ist, die die
Subelemente in eine Übermittlungswarteschlange einordnet, wobei mehrere
Datenbankroutinen auf jeder Datenbank ausgeführt werden (Offenlegungsschrift,
[0022]).


2.2   Zur Beurteilung der beanspruchten Lehre sind die Druckschriften D3 und
D4 von besonderer Bedeutung.


Die Druckschrift D3 beschreibt ein System und ein Verfahren zur parallelen
Verarbeitung von Datenbankabfragen in einem verteilten Datenbanksystem. Das
bekannte System umfasst im Wesentlichen Client Applikationen auf Client
Computern sowie eine Mehrzahl von Datenbankservern, die Datenbanken vorhalten. Außerdem werden Speichermittel beschrieben, die Informationen darüber
bereitstellen, wie die Datenbestände auf die einzelnen Datenbankserver verteilt
sind. Mit dem beschriebenen System ist es möglich, komplexe Datenbankanfragen in SQL in Unteranfragen aufzuteilen, die dann auf den Servern parallel
abgearbeitet werden können (Seite 4 Zeile 18 – Seite 5 Zeile 2).


Damit offenbart die Druckschrift D3, die als nächstliegender Stand der Technik
anzusehen ist, ein Verfahren zur Steuerung von datenbankübergreifenden Softwareroutinen, um Datenbankanfragen an eine Mehrzahl von Datenbankeinheiten
quasi parallel, d. h. näherungsweise zeitgleich zu verarbeiten (Seite 1, Zeilen 4-14
– teilweise Merkmal (a)).

                                         - 12 -



Im Verfahren der Druckschrift D3 findet eine Systemanordnung Verwendung, in
der an einer Zentraleinheit (server 400; device 440) eine Mehrzahl von Eingabesystemen (client computer 300) angeschlossen ist (Seite 6, Zeilen 42-44;
Seite 7, Zeilen 23-25; Figur 4A, 4B – Merkmal (b)).


Das System enthält Datenbankeinheiten mit Datenbanken (Seite 6 Zeile 45 –
Seite 7 Zeile 7; siehe IBM DB2 DBMS sowie Oracle 7 DBMS) und Applikationselemente in Form von Server-Hardwarekomponenten (Figur 4A – 4C; siehe
Server 330-350, 450). Auf den Applikationselementen werden Applikationen
ausgeführt, z. B. ein Optimierer (Seite 7, erster Absatz; siehe „optimiser“ 365 –
385 – Merkmal (c))


Jeder Datenbankeinheit werden in eindeutiger Weise Tabellen, Partitionen und
Server zugeordnet; die Verknüpfungen werden als Metadaten für die Datenbankanfragen gespeichert (Seite 15, Zeilen 7-17). Die Gesamtheit der in einer
Datenbankeinheit vorgehaltenen Tabellen bildet eine Menge von Datenstrukturen
(also eine „Informationsklasse“), die den Servern bzw. dem Server der jeweiligen
Datenbankeinheit zugeordnet wird (Seite 13, Table 5; Figur 4B; Seite 7, erster
Absatz; siehe IBM DB2 DBMS mit Servern 330-350 sowie ORACLE 7 DBMS mit
Server 450 – teilweise Merkmal (d)).


Die Tabellen der aus der Druckschrift D3 bekannten Datenbankeinheiten bilden
die einzelnen Elemente der Menge von Datenstrukturen (also „Informationselemente“), die eindeutig auf die Datenbankserver einer Datenbankeinheit
abgebildet sind (teilweise Merkmal (e)).


Im Verfahren der Druckschrift D3 wird mit Hilfe eines Eingabesystems eine
Datenbankanfrage in eine Zentraleinheit (PQD server) eingegeben (Seite 13,
unten „Query“; Seite 15, Zeilen 7-17), die verschiedene Datenbanktabellen
(„Informationselemente“) auf verschiedenen Servern und Datenbankeinheiten
betrifft (Seite 14, Zeilen 1-5; Seite 15, Zeilen 7-17 – teilweise Merkmal (f)).

                                      - 13 -



In der Zentraleinheit (PQD server) wird die Datenbankanfrage (als „Informationsgruppe“) mittels einer Zuordnungsroutine in Unteranfragen zerlegt, die dann
an die zuständigen Datenbankeinheiten mit den zugehörigen Tabellen weitergeleitet werden (Seite 15, Zeilen 19-30; siehe „subqueries“, aber auch Seite 8,
Zeile 42 – Seite 9, Zeile 14, siehe „two sub-tasks, one to be sent to the optimiser
of database server 330 and one to be sent to the non-DB2 database server 450 –
teilweise Merkmale (g) und (h)).


Im Verfahren der Druckschrift D3 erfolgt über die Applikationsroutine (optimiser
365) einer DB2 Datenbankeinheit eine Zerlegung der Unteranfragen („subqueries“
bzw. „sub-tasks“) in weitere Teil- bzw. Unteranfragen („further sub-tasks“, gleichbedeutend mit „Subelementen“), die dann auf den einzelnen DB2 Servern
näherungsweise parallel abgearbeitet werden (Seite 8, Zeile 42 – Seite 9, Zeile 14
– teilweise Merkmale (i) und (j)).


Dass in der Anordnung der Figur 4B neben der DB2 in gleicher Weise eine
Oracle 7 Datenbankeinheit mit mehreren Oracle Servern vorgesehen sein kann,
wobei auch auf einem der Oracle Server eine Applikationsroutine zur Zerlegung
von Datenbankanfragen läuft, wird vom Fachmann in diesem Zusammenhang
mitgelesen.


Nach allem lehrt die Druckschrift D3 damit ein Verfahren, bei dem über verteilten
Datenbankeinheiten komplexe Datenbankanfragen abgesetzt werden, und diese
Datenbankanfragen von Applikationsroutinen, sog. „Optimisern“ zweimal zerlegt
werden, um eine Parallelisierung der so erzeugten Sub-Tasks zu erreichen.


Die Druckschrift D4 betrifft ein Verfahren zur Durchführung eines „Two-Phase-Commits“ bzw. eines „Zwei-Phasen-Commits“ in einem verteilten Datenbanksystem für den Fall verteilter Transaktionen (Spalte 5, Zeilen 10-41). Aus ihr geht
hervor, dass sich in verteilten Systemen eine Transaktion oftmals über mehrere
Prozesse bzw. Datenbanken („participating databases“) erstreckt, welche gemein-

                                        - 14 -



sam und voneinander abhängig Daten verändern. Anstelle – wie üblich - in der
ersten Phase des „Two-Phase-Commits“ die Zustimmung oder Ablehnung zur
Festschreibung der Datenveränderungen aller beteiligten Prozesse bzw. Datenbanken einzuholen, bestimmt ein Koordinator-Datenbanksystem anhand von
Transaktionslogs (Spalte 5, Zeilen 10-19; siehe „external log tracking data“), ob
alle Teiltransaktionen an den Teilnehmer-Datenbanken („participating databases“)
zum erfolgreichen Ende geführt worden sind. In den Transaktionslogs („external
log tracking data“) werden dabei die Zustände der Teilnehmer Datenbanken
protokolliert. Bestimmt die Koordinator-Datenbank, dass alle Transaktionen erfolgreich waren, schickt die Koordinator-Datenbank einen „Commit“ an alle Teilnehmer-Datenbanken, wodurch alle Transaktionen festgeschrieben und die
Ressourcen freigegeben werden (Spalte 6, Zeilen 63-67). Das geschilderte Verfahren hat gegenüber dem typischen „Two-Phase-Commit“ den Vorteil, dass nicht
notwendigerweise „Prepare-Requests“ von der Koordinator-Datenbank an die
Teilnehmer-Datenbanken verschickt werden müssen.


Demnach lehrt die Druckschrift D4 ein Verfahren bzw. System zur Verarbeitung
verteilter Transaktionen in einem System verteilter Datenbanken (Spalte 1
Zeilen 5-25), bei dem die Veränderung der Daten bzw. deren Manipulation im
Wesentlichen nach dem Prinzip eines „Two-Phase-Commits“ erfolgt, das die
Grundlage für eine möglichst zeitgleiche Durchführung einzelner, „atomarer“
Datenbankoperation bildet (Spalte 1, Zeilen 5-25, siehe „providing atomicity of
transactions“ – restlicher Teil von Merkmal (a)).


Die einzelnen Datenbankoperationen, die als Subelemente einer kompletten
Transaktion anzusehen sind, führen zu einer Veränderung wenigstens eines in
einer Datenbank gespeicherten Datensatzes (Spalte 1, Zeilen 14-17; Spalte 2,
Zeilen 31-42; Spalte 5, Zeilen 25-29 – Merkmal (k)).


Die jeweiligen Merkmale (l) bis (r) entsprechen im Wesentlichen den gängigen
Prozessen für „Commit“ und „Rollback“ für Transaktionen in verteilten Daten-

                                        - 15 -



banken, wie sie in der Druckschrift D4 erläutert werden (Spalte 1, Zeilen 11-54,
Spalte 5, Zeilen 10-41). So bestimmt eine zentrale Koordinatordatenbank
(„coordinating database system“), ob alle oder keine der einzelnen Datenbankoperationen simultan verarbeitet werden können. Die Koordinatordatenbank
der Druckschrift D4 überwacht die Durchführung eines „Two-Phase-Commits“,
dem ein „Alles oder Nichts“ Prinzip zugrundeliegt und nach dem die einzelnen
Datenbankoperationen abgearbeitet werden (Spalte 1, Zeilen 34-65; Spalte 5,
Zeilen 25-41 – Merkmale (l) und (n)).


Dabei holt die Koordinatordatenbank in der ersten Phase („prepare phase“) die
Zustimmung oder Ablehnung zur Festschreibung der Datenveränderungen aller
beteiligten Prozesse bzw. Datenbanken ein (Spalte 1, Zeilen 34-43; Spalte 5,
Zeilen 25-41 – Merkmal (o)).


Nur dann, wenn alle beteiligten Datenbanken zustimmen, entscheidet die
Koordinatordatenbank auf „Commit“ („commit phase“), d. h. auf die Festschreibung der Datenveränderungen bzw. die Verarbeitung der einzelnen Datenbankoperationen (Spalte 1, Zeilen 40-54 – Merkmal (p)), ansonsten gilt die
Verarbeitung der Datenbankoperationen bzw. Subelemente als nicht erfolgt und
die gesamte Transaktion wird zurückgesetzt (Spalte 1, Zeilen 55-62 – Merkmal (r)).


Letzteres bedeutet einen „Rollback“, d. h. eine Wiederherstellung des ursprünglichen Zustandes der beteiligten Datenbanken. Dass für einen solchen Zweck die
ursprünglichen Datensätze sowie die daran vorgenommenen Operationen vorweg
gespeichert werden müssen, ist für den Fachmann in diesem Zusammenhang
selbstverständlich, ergibt sich aber auch schon zumindest teilweise aus der
Druckschrift D4 (Spalte 8, Zeilen 53-58 – Merkmal (m)). Dass darüberhinaus nach
einer erfolgreich durchgeführten Transaktion bei einer Vielzahl weiterer Datenbankanfragen und in der Regel endlichen Speicherkapazitäten – wie sie bei einem
Datenbanksystem nach dem Vorbild der Druckschrift D4 gewöhnlich vor-

                                      - 16 -



liegen - ursprüngliche Datensätze gelöscht werden müssen, wird vom Fachmann
als zwingendes technisches Erfordernis mitgelesen (Merkmal (q)).


Die Durchführung von Datenbankoperationen bzw. die Übermittlung von Subelementen an Datenbanken wird in der Druckschrift D4 im Wesentlichen durch
eine Mehrzahl von Softwareroutinen bewerkstelligt, die eine Interprozesskommunikation unterstützen und die Datenbankanfragen an die einzelnen Datenbanken verteilen, also als Dispatcherroutinen fungieren (Spalte 8, Zeilen 28-43,
siehe „SQLLIB“, „OCI“ und „SQL*Net“ – teilweise Merkmal (s)).


2.3   Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
die jeweiligen mit dem Patentanspruch 1 gemäß Haupt- und Hilfsantrag beanspruchten Gegenstände für den Fachmann nahegelegen haben.


Zu den routinemäßigen Aufgaben, die sich dem Fachmann stellen, der sich
insbesondere mit Problemen in Datenbanksystemen befasst, gehört es, neben der
Performance ebenso die Funktionalität von Datenbanksystemen, wie dem aus der
Druckschrift D3 entnehmbaren System, ständig zu verbessern. Für den Fachmann
lag es nahe, sich zu diesem Zweck überall dort nach Anregungen umzusehen, wo
effektive Informationssysteme zum Einsatz kommen. Hierbei konnte der Fachmann auf die Druckschrift D4 stoßen, welche lehrt, Transaktionen nach einem
„Two-Phase-Commit“ zu organisieren, um performante Zugriffsstrategien zu unterstützen. Angesichts des in der Druckschrift D3 gegebenen Hinweises, für eine
neue Partitionierung der Daten zwischen den Datenbankeinheiten die zugehörige
Partitionierungsinformation in den Metadaten anzupassen (vgl. D3 Seite 10, Zeilen
39-45, siehe „updating the data dictionary“), bot es sich für den Fachmann an, das
aus der Druckschrift D3 bekannte Verfahren bzw. System um die Funktionalität
eines effektiven Schreibzugriffs nach dem Vorbild der Druckschrift D4 zu
erweitern, also neben einem bloßen Datenretrieval auch Transaktionen zuzulassen, die den Zustand einer Datenbank verändern. Eine solche kombinierte
Lehre unterscheidet sich von der Lehre nach Patentanspruch 1 gemäß Hilfs-

                                        - 17 -



antrag, welcher die Merkmale (a) bis (j) gemäß Hauptantrag mit umfasst, nur noch
durch die in den Merkmalen (d) bis (j) enthaltenen Teilmerkmale, die das
spezielle, dem beanspruchten Verfahren zugrundeliegende Datenmodell mit Informationsgruppen, -klassen, -elementen und Subelementen betreffen sowie durch
das in Merkmal (s) enthaltene Teilmerkmal, das die Einordnung von Subelementen in eine Übermittlungswarteschlange vorsieht.


Dabei ist dem Fachmann geläufig, dass eine Batchverarbeitung von Datenbankanfragen die Zahl der Datenbank-/Netzwerkzugriffe verringert, indem mehrere
gleichartige Anweisungen in eine Batchdatei geschrieben werden, diese in eine
Warteschlange eingeordnet wird, um dann in einem Aufruf zur Datenbank
geschickt und dort verarbeitet zu werden. Damit dient die Einordnung von
Subelementen bzw. Datenbankanfragen in eine Übermittlungswarteschlange v. a.
dem Zweck eines effektiveren Datenbankzugriffs und ist bereits aus diesem
Grunde für den Fachmann ausgehend von dem in der Druckschrift D4 offenbarten
Stand der Technik nahegelegt (restlicher Teil von Merkmal (s)).


Die das Datenmodell betreffenden Teilmerkmale weisen allerdings keinerlei Teilaspekt auf, der ein technisches Problem bewältigt und sind demnach bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen (BGH a. a. O. –
Wiedergabe topografischer Informationen). Nach Überzeugung des Senats
können weder der Bedeutungsinhalt des Datenmodells (z. B. Vertragstypen,
Tarife, Kundennamen etc.) noch dessen spezielle Einteilung in Informationsgruppen, -klassen, -elementen und Subelementen, welche lediglich auf organisatorischen Erwägungen beruht, zur Lösung eines technischen Problems mit
technischen Mitteln beitragen (restlicher Teil der Merkmale (d) bis (j)).


Der Einwand der Anmelderin, aus dem Stand der Technik sei die Verwendung von
Dispatcherroutinen i. S. d. Anmeldung weder bekannt noch nahegelegt, greift
insoweit nicht durch.

                                        - 18 -



Weiterhin vermochte die Argumentation der Anmelderin, die Druckschriften D3
und D4 zeigten keinerlei Hinweis für eine Koordinatorroutine in einer zentralen
Einheit, nach allem nicht zu überzeugen. Während in der Druckschrift D3 eine
Koordinatorroutine als „Parallel Query Decomposer“ verwirklicht ist, fungiert in der
Druckschrift D4 eine Datenbank („coordinating database system“) als zentraler
Koordinator.


Durch die geschilderten Überlegungen, die keine erfinderische Tätigkeit erforderten, konnte der Fachmann zum Verfahren des jeweiligen Patentanspruchs 1
nach Haupt- bzw. Hilfsantrag gelangen.


2.4      Mit den jeweiligen Patentansprüchen 1 gemäß Haupt- und Hilfsantrag fallen
auch die jeweiligen übrigen Patentansprüche, da über einen Antrag nur einheitlich
entschieden werden kann (BGH GRUR 1997, 120 – Elektrisches Speicherheizgerät).




                                         III.
                               Rechtsmittelbelehrung


      1. Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde
         der Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für
         Klasse G06F des Deutschen Patent- und Markenamtes zurückzuweisen.


      2. Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten
         das   Rechtsmittel   der   Rechtsbeschwerde   zu.   Da   der   Senat   die
         Rechtsbeschwerde nicht zugelassen hat, ist sie nur statthaft, wenn gerügt
         wird, dass

                                         - 19 -



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


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek               Eder                Dr. Thum-Rung            Dr. Forkel




                                                                              Me
