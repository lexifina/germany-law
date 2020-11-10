---
ecli: "ECLI:DE:BPatG:2020:101120B17Wpat14.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 14/20"
decided: "2020-11-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=38&nr=40172&anz=666&pos=584&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2020-11-10_17_W-pat_14_20_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 17 W (pat) 14/20 vom 2020-11-10

## Entscheidung

BUNDESPATENTGERICHT



    17 W (pat) 14/20
 ________________________

    (Aktenzeichen)




                                    BESCHLUSS

                               In der Beschwerdesache


                 betreffend die Patentanmeldung 10 2018 200 555.9
…
hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
10. November 2020           unter    Mitwirkung   des    Vorsitzenden      Richters
Dipl.-Phys. Dr. Morawek, der Richterin Bayer, des Richters Dipl.-Phys. Dr. Forkel
und des Richters Dipl.-Phys. Dr. Städele


beschlossen:


      Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom
      4. Juni 2019 aufgehoben und das Patent mit folgenden Unterlagen erteilt:




ECLI:DE:BPatG:2020:101120B17Wpat14.20.0

                                        -2-



     Patentansprüche 1 bis 8 sowie
     Beschreibung Seiten 1 bis 20,
                    jeweils eingegangen am 25. September 2020,
     4 Blatt Zeichnungen mit Figuren 1 bis 5 vom 15. Januar 2018.




                                     Gründe


                                          I.


Die vorliegende Patentanmeldung ist am 15. Januar 2018 beim Deutschen Patentund Markenamt eingereicht worden. Sie trägt die Bezeichnung


  „Fahrzeugelektronikeinheit mit einer physikalischen Netzwerk-Schnittstelle und
  mehreren virtuelle Netzwerk-Schnittstellen aufweisenden virtuellen Maschinen
sowie Datenkommunikationsverfahren zwischen den virtuellen Maschinen und der
  Netzwerk-Schnittstelle zu einem lokalen Fahrzeugnetzwerk eines Fahrzeugs“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F des
Deutschen Patent- und Markenamts in der Anhörung vom 4. Juni 2019 zurückgewiesen. Zur Begründung führte die Prüfungsstelle sinngemäß aus, dass die
Gegenstände der (damaligen) Patentansprüche 1 nach dem Hauptantrag sowie den
Hilfsanträgen 1 bis 2 nicht auf einer erfinderischen Tätigkeit beruhten.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Anmelderin beantragt sinngemäß,


     den Zurückweisungsbeschluss der Prüfungsstelle vom 4. Juni 2019 aufzuheben und das nachgesuchte Patent auf der Grundlage der folgenden Unterlagen zu erteilen:

                                       -3-



     Patentansprüche 1 bis 8 sowie
     Beschreibung Seiten 1 bis 20,
                   jeweils eingegangen am 25. September 2020,
     4 Blatt Zeichnungen mit Figuren 1 bis 5 vom 15. Januar 2018.


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 lautet:

     1.        Fahrzeugelektronikeinheit (10) mit


     M1     - wenigstens zwei virtuellen Maschinen (P1, P2) mit jeweils einer virtuellen Netzwerk-Schnittstelle (5.1, 5.2),


     M2     - einem Hypervisor (1), welcher zur Trennung der virtuellen Maschinen (P1, P2) ausgebildet ist,


     M3     - einem Speicher (3) mit jeweils einer der virtuellen Maschinen (P1,
               P2) exklusiv zugeordneten Speicherabschnitten (3.1, 3.2),


     M3.1      wobei jeder Speicherabschnitt (3.1, 3.2) direkte Speicherbereiche (3.10, 3.11, 3.20, 3.21) für die direkte Kommunikation der virtuellen Maschine (P1, P2) mit deren zugeordneter virtueller Netzwerk-Schnittstelle (5.1, 5.2) aufweist, und


     M4     - einer physikalischen Netzwerk-Schnittstelle (2.1) einer Netzwerkkarte (2) zur Herstellung einer Kommunikationsverbindung zwischen jeweils einer virtuellen Netzwerk-Schnittstelle (5.1, 5.2) einer
               virtuellen Maschine (P1, P2) und einem Fahrzeugnetzwerk (B1),


               dadurch gekennzeichnet, dass

                                  -4-



M3.2   - in dem jeweiligen Speicherabschnitt (3.1, 3.2) der virtuellen
         Maschine (P1, P2) jeweils mehrere unterschiedliche Applikationen
         implementiert sind, und


M3.3   - für jede der von der jeweiligen virtuellen Maschine (P1, P2) ausgeführten Applikationen jeweils ein RX-Pufferbereich sowie ein TX-Pufferbereich als Speicherbereich (3.10, 3.11, 3.20, 3.21) bereitgestellt sind und


M4.1     die physikalische Netzwerk-Schnittstelle (2.1) dazu eingerichtet ist,
         ein jeweiliges empfangenes Datenpaket in einen RX-Puffer (2.2)
         der Netzwerkkarte (2) zu schreiben


M4.2     und gleichzeitig eine Eingangsmeldung einem Ethernet-Treiber (2.5) zu übermitteln, welcher ein Triggersignal an eine Filterund Routingeinheit (2.3) sendet, und


M2.1   - der Hypervisor (1) dazu eingerichtet ist, der Filter- und Routingeinheit (2.3) Filter- und Routing-Regeln bereitzustellen, und


M4.3   - der RX-Puffer (2.2) dazu eingerichtet ist, einen Header des Datenpakets zur Analyse von dessen Header-Information von dem RX-Puffer (2.2) an die Filter- und Routingeinheit (2.3) zu senden, und


M5     - die Filter- und Routingeinheit (2.3) dazu eingerichtet ist, den Header
         hinsichtlich der der Header-Information entsprechenden Zuordnung
         zu einer der virtuellen Maschinen (P1, P2) auszuwerten und


M5.1     mittels eines Triggersignals einen PCIe-Treiber (2.4) der Netzwerkkarte (2) zu veranlassen,

                                      -5-



     M5.2      mittels einer Speicherdirektzugriffs (DMA)-Funktion das Datenpaket aus dem RX-Puffer (2.2) über DMA-Ausgänge (2.30) der Filterund Routingeinheit (2.3) und eine PCIe-Schnittstelle (7) in den der
               Header-Information entsprechenden Speicherbereich (3.10, 3.11,
               3.20, 3.21) der jeweiligen virtuellen Maschine (P1, P2) zu kopieren.



Die geltenden Patentansprüche 2 bis 8 lauten:


      „2.      Fahrzeugelektronikeinheit (10) nach Anspruch 1, bei welcher


            - ein erster Speicherabschnitt (3.1) einer ersten virtuellen Maschine (P1) wenigstens einen Speicherbereich (3.10) aufweist,
               wobei dieser Speicherbereich (3.10) mit

            - einem Signalisierungsbereich (3.01) zum Signalisieren, ob RX-
               oder TX-Daten übermittelt werden,

            - einem RX-Puffer zum Speichern von empfangenen Daten, und

            - einem TX-Puffer zum Speichern von zu sendenden Daten

               ausgebildet ist, und

            - ein zweiter Speicherabschnitt (3.2) einer zweiten virtuellen Maschine (P2) wenigstens einen Speicherbereich (3.20) aufweist,
               wobei dieser Speicherbereich (3.20) mit

            - einem Signalisierungsbereich (3.02) zum Signalisieren, ob RX-
               oder TX-Daten übermittelt werden,

            - einem RX-Puffer zum Speichern von empfangenen Daten, und

            - einem TX-Puffer zum Speichern von zu sendenden Daten

               ausgebildet ist.

                                 -6-



3.     Fahrzeugelektronikeinheit (10) nach Anspruch 1, bei welcher die
       Fahrzeugelektronikeinheit (10) zum Signalisieren, ob RX- oder TX-Daten übermittelt werden, zur Durchführung von definierten Interrupts konfiguriert ist.


4.     Fahrzeugelektronikeinheit (10) nach einem der vorhergehenden
       Ansprüche, bei welcher jeweils ein Speicherabschnitt (3.1, 3.2)
       einen Speicherbereich (3.10, 3.20) für IP-Steuerdaten und einen
       Speicherbereich (3.11, 3.21) für Video- und/oder Grafikdaten aufweist.


5.     Fahrzeugelektronikeinheit (10) nach einem der vorhergehenden
       Ansprüche, bei welcher wenigstens eine virtuelle Maschine (P1, P2)
       mit einer PCIe-Schnittstelle (6) zum Empfangen von in dem zugeordneten Speicherabschnitt (3.1, 3.2) zu speichernden Daten und
       zum Senden von Daten aus dem zugeordneten Speicherabschnitt (3.1, 3.2) konfiguriert ist.


6.     Fahrzeugelektronikeinheit (10) nach einem der vorhergehenden
       Ansprüche, bei welcher die wenigstens zwei virtuellen Maschinen (P1, P2)

     - auf wenigstens zwei Prozessoren ausgeführt werden,

     - den beiden Prozessoren jeweils wenigstens ein Speicher zugeordnet ist, und

     - die beiden Speicher jeweils eine PCIe-Schnittstelle zum Empfangen von zu speichernden Daten und zum Senden von Daten über
       die physikalische Netzwerk-Schnittstelle (2.1) aufweisen.


7.     Datenkommunikationsverfahren zwischen den virtuellen Maschinen (P1, P2) der Fahrzeugelektronikeinheit (10) nach einem der

                          -7-



  vorhergehenden Ansprüche und der physikalischen Netzwerk-Schnittstelle (2.1) der Netzwerkkarte (2) der Fahrzeugelektronikeinheit (10), wobei zum Empfangen wenigstens einer ein Datenpaket
  mit einem Header und einen Nachrichtensignalisierungs-Interrupt
  (MSI = Message Signaled Interrupt) aufweisenden Datennachricht
  entsprechend einem Netzwerkprotokoll folgende Verfahrensschritte
  durchgeführt werden:


- Betreiben der mehreren durch einen Hypervisor (1) getrennten virtuellen Maschinen (P1, P2), wobei in einem jeweiligen Speicherabschnitt (3.1, 3.2) der virtuellen Maschinen (P1, P2) jeweils mehrere
  unterschiedliche Applikationen implementiert sind und für jede der
  von der jeweiligen virtuellen Maschine (P1, P2) ausgeführten Applikationen jeweils ein RX-Pufferbereich sowie ein TX-Pufferbereich
  als direkter Speicherbereich (3.10, 3.11, 3.20, 3.21) bereitgestellt
  ist,


- Speichern des Datenpaketes der Datennachricht in einem RX-Puffer (2.2) der Netzwerkkarte (2),


- Auswerten des Headers der Datennachricht mittels einer Filter- und
  Routingeinheit (2.3) hinsichtlich der das Datenpaket zuzuweisenden Partition, wobei die Header-Information und der Nachrichtensignalisierungs-Interrupt über einen PCIe-Treiber (2.4) einer Speicherdirektzugriffs   (DMA)-Funktion        und   einer   MSI-Interrupt-Steuerungsfunktion (MSI-Handler) zur Verfügung gestellt werden
  und wobei der Hypervisor (1) der Filter- und Routingeinheit (2.3)
  Filter- und Routing-Regeln bereitstellt,


- Kopieren des Datenpaketes mittels der Speicherdirektzugriffs
  (DMA)-Funktion in den der Header-Information entsprechenden

                               -8-



       Speicherabschnitt    (3.1,   3.2)   der   entsprechenden   virtuellen
       Maschine (P1, P2), indem die Filter- und Routingeinheit (2.3) mittels
       eines Triggersignals den PCIe-Treiber (2.4) veranlasst, mittels der
       Speicherdirektzugriffs (DMA)-Funktion das Datenpaket aus dem
       RX-Puffer (2.2) über DMA-Ausgänge (2.30) der Filter- und Routingeinheit (2.3) und eine PCIe-Schnittstelle (7) in den der Header-Information entsprechenden Speicherbereich (3.10, 3.11, 3.20,
       3.21) der jeweiligen virtuellen Maschine (P1, P2) zu kopieren, und


     - Bereitstellen eines virtuellen Interrupts mittels der MSI-Interrupt-Steuerungsfunktion für die der Header-Information entsprechende
       virtuelle Maschine (P1, P2), und


     - Verarbeiten des Datenpaketes durch die der Header-Information
       entsprechende virtuelle Maschine (P1, P2).


8.     Datenkommunikationsverfahren zwischen den virtuellen Maschinen (P1, P2) der Fahrzeugelektronikeinheit (10) nach Anspruch 7
       und der physikalischen Netzwerk-Schnittstelle (2.1), wobei zum
       Senden wenigstens einer ein Datenpaket mit einem Header und
       einen Nachrichtensignalisierungs-Interrupt (MSI = Message Signaled Interrupt) aufweisenden Datennachricht entsprechend einem
       Netzwerkprotokoll folgende Verfahrensschritte durchgeführt werden:


     - Erzeugen des an die Netzwerk-Schnittstelle (2.1) weiterzuleitenden
       Datenpaketes durch eine virtuelle Maschine (P1, P2) und Speichern
       des Datenpaketes in dem zugehörigen Speicherabschnitt (3.1, 3.2),


     - Erzeugen einer die Bereitstellung des weiterzuleitenden Datenpaketes anzeigenden Nachricht für einen PCIe-Treiber (6),

                                         -9-



              - Kopieren des Datenpaketes in einen TX-Puffer (2.20) mittels der
                 durch den PCIe-Treiber (6) ausgeführten Speicherdirektzugriffs
                 (DMA)-Funktion,


              - Ergänzen des Datenpaketes mit einer einer Header-Information
                 entsprechenden Information des PCIe-Treibers (6) mittels der Netzwerk-Schnittstelle (2.1),


              - Erstellen einer Datennachricht aus dem Datenpaket mit Header entsprechend dem Netzwerkprotokoll mittels der physikalischen Netzwerk-Schnittstelle (2.1), und


              - Senden der Datennachricht mittels der physikalischen Netzwerk-Schnittstelle (2.1).“


Zu den weiteren Einzelheiten wird auf die Akte verwiesen.




                                             II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
hat auch Erfolg, da ein Patent nach dem nunmehr geltenden Antrag erteilt werden
kann.


1.      Die vorliegende Patentanmeldung betrifft eine Fahrzeugelektronikeinheit mit
einer physikalischen Netzwerk-Schnittstelle und wenigstens zwei virtuellen Maschinen sowie ein Datenkommunikationsverfahren zwischen den virtuellen Maschinen
und der Netzwerk-Schnittstelle zu einem lokalen Fahrzeugnetzwerk eines Fahrzeugs (Offenlegungsschrift, Absatz [0001]).

                                       - 10 -



Gemäß der Beschreibungseinleitung böten Cockpit- und Infotainmentsysteme in
Fahrzeugen beispielsweise Zugriff auf Betriebs- und Fahrzeugdatenanzeigen,
Navigation, Servicefunktionen, Mobiltelefon, Internet und Audio/Video. Um Nutzdaten und Steuerdaten zwischen diesen unterschiedlichen Komponenten austauschen zu können, werde das Konzept der Virtualisierung mit mehreren Betriebssystemen durch einen Hypervisor realisiert. Mittels solcher Hypervisoren werde eine
virtuelle Umgebung definiert, die es erlaube, mehrere Betriebssysteme parallel auf
einer gemeinsamen Hardware zu betreiben (Offenlegungsschrift, Absatz [0003]; der
Verweis auf das Konzept der „Visualisierung“ meint offensichtlich eine „Virtualisierung“).


Ferner sei es bekannt, dass zur Übertragung von Daten innerhalb einer Hypervisor-Architektur ein Datenübertragungsverfahren verwendet werde, welches zu einer
unerwünschten erhöhten CPU-Last führe und nachteilige Eigenschaften hinsichtlich
von Sicherheitsaspekten aufweise. Bei diesem Datenübertragungsverfahren würden Ethernet-Datenpakete zwischen einer Partition und einer Netzwerkschnittstelle
eines Fahrzeugnetzwerkes übertragen, wobei Daten einer weiteren zweiten Partition nicht direkt an die Netzwerkschnittstelle übergeben würden, sondern zunächst
über ein virtuelles Netzwerk zur ersten Partition und erst anschließend zur Netzwerkschnittstelle (Offenlegungsschrift, Absatz [0004]).


Der Anmeldung soll die Aufgabe zugrunde liegen, eine Fahrzeugelektronikeinheit
mit wenigstens zwei virtuellen Maschinen, mit welcher eine leistungsstarke, sichere
und zuverlässige Datenkommunikation innerhalb der Architektur der Fahrzeugelektronikeinheit erzielt wird, und ein entsprechendes Datenkommunikationsverfahren
anzugeben (Offenlegungsschrift, Absatz [0008]).


Als Fachmann, der mit der Lösung der oben genannten Aufgabe betraut wird, ist
ein Elektrotechnikingenieur oder ein Informatiker mit mehrjähriger Berufserfahrung

                                       - 11 -



in der Entwicklung von Virtualisierungslösungen für Fahrzeugkommunikationssysteme anzusehen.


2.     Zur Lösung der oben genannten Aufgabe schlägt die Anmeldung eine Fahrzeugelektronikeinheit gemäß dem geltenden Patentanspruch 1 und ein Datenkommunikationsverfahren nach dem geltenden Patentanspruch 7 vor.


2.1    Der als Vorrichtungsanspruch formulierte Patentanspruch 1 beschreibt das
spezielle Zusammenwirken verschiedener Hard- und Softwarekomponenten einer
Fahrzeugelektronikeinheit, um von einer Netzwerkkarte empfangene Datenpakete
in applikationsspezifische Speicherbereiche virtueller Maschinen einer Fahrzeugelektronikeinheit zu transferieren.


Dementsprechend weist die beanspruchte Fahrzeugelektronikeinheit wenigstens
zwei virtuelle Maschinen, einen Hypervisor, einen Speicher mit jeweils einer der virtuellen Maschinen exklusiv zugeordneten Speicherabschnitten und eine physikalische Netzwerk-Schnittstelle zur Herstellung einer Kommunikationsverbindung
zwischen jeweils einer virtuellen Netzwerk-Schnittstelle einer virtuellen Maschine
und einem Fahrzeugnetzwerk auf (vgl. Merkmale M1, M2, M3 und M4). Die in den
virtuellen Maschinen implementierten Applikationen verarbeiten beispielsweise
Steuerdaten für den IP-Datenverkehr oder Video- und/oder Grafikdaten (vgl. Offenlegungsschrift, Absätze [0021], [0030], [0031]).


Bei der konkreten Umsetzung des Transfers der Datenpakete spielt eine Filter- und
Routingeinheit eine zentrale Rolle. Nachdem die physikalische Netzwerk-Schnittstelle ein Datenpaket in einen RX-Puffer der Netzwerkkarte geschrieben hat (Merkmal M4.1), wird der Filter- und Routingeinheit durch einen Ethernet-Treiber ein Triggersignal übermittelt; sie wertet den ihr von dem RX-Puffer gesendeten Header des
Datenpakets hinsichtlich der der Header-Information entsprechenden Zuordnung zu
einer der virtuellen Maschinen aus, wozu ihr von einem Hypervisor Filter- und Routing-Regeln bereitgestellt werden (vgl. Merkmale M2.1, M4.2, M4.3, M5). Auf der

                                       - 12 -



Grundlage dieser Auswertung triggert die Filter- und Routingeinheit ihrerseits einen
PCIe-Treiber der Netzwerkkarte, so dass das Paket über eine Speicherdirektzugriffs-(„DMA“)-Funktion aus einem RX-Puffer der Netzwerkkarte über entsprechende Ausgänge der Filter- und Routingeinheit und eine PCIe-Schnittstelle in den
Speicherbereich einer Applikation geschrieben werden kann (Merkmale M5.1 und
M5.2; die Abkürzung „DMA“ - engl. „direct memory access“ - weist dabei auf einen
Datentransfer hin, der nicht durch eine CPU vorgenommen wird). Für jede Applikation ist jeweils ein RX-Pufferbereich sowie ein TX-Pufferbereich als direkter Speicherbereich für die direkte Kommunikation der virtuellen Maschine mit deren zugeordneter virtueller Netzwerk-Schnittstelle bereitgestellt (Merkmale M3.1, M3.2 und
M3.3).


Laut Beschreibung besitzt die damit realisierte Fahrzeugelektronik-Architektur den
Vorteil einer klaren Trennung der zwischen jeweils einer virtuellen Maschine und
der physikalischen Netzwerk-Schnittstelle eines lokalen Fahrzeugnetzwerks zu
kommunizierenden Datenpakete, so dass weder negative Auswirkungen auf die
Sicherheit dieser Architektur noch auf die Leistungsfähigkeit und Zuverlässigkeit
eintreten könnten (Offenlegungsschrift, Absatz [0011]).


2.2      Der auf ein Datenkommunikationsverfahren gerichtete Patentanspruch 7 enthält zusätzlich zu den Merkmalen des Patentanspruchs 1 weitere Merkmale, gemäß
denen das empfangene Datenpaket Teil einer Datennachricht ist, die neben dem
Header auch noch einen Nachrichtensignalisierungs-Interrupt aufweist, welcher
einer Message-Signalled-Interrupt-Steuerungsfunktion (einem „MSI-Handler“) zur
Verfügung gestellt wird, welche der virtuellen Maschine einen virtuellen Interrupt
bereitstellt.


3.       Das geltende Patentbegehren ist zulässig. Die Gegenstände der Patentansprüche 1 und 7 genügen dem Erfordernis einer deutlichen und vollständigen Offenbarung und sind durch den Stand der Technik weder neuheitsschädlich vorweggenommen noch dem Fachmann nahegelegt.

                                         - 13 -



3.1        Das geltende Patentbegehren geht nicht über den Inhalt der am Anmeldetag
eingereichten Unterlagen hinaus (§ 38 PatG).


So folgt die Lehre des Patentanspruchs 1 aus den ursprünglichen Patentansprüchen 1 und 2, den Figuren 1 bis 4 sowie den Absätzen [0021], [0027], [0030], [0031],
[0053], [0054] und [0060] der Offenlegungsschrift. Der Gegenstand des nebengeordneten Patentanspruchs 7 basiert auf dem ursprünglichen Patentanspruch 8
sowie ebenfalls auf den zuvor genannten Textstellen und Figuren der Offenlegungsschrift.


Die abhängigen Ansprüche 2 bis 6 bzw. 8 gehen auf die ursprünglichen Ansprüche 3 bis 7 bzw. 10 sowie die Absätze [0013] bis [0015] der Offenlegungsschrift
zurück.


Auch die an den ursprünglich eingereichten Beschreibungsseiten vorgenommenen
Änderungen sind zulässig.


Die geltenden Figurenseiten mit den Figuren 1 bis 5 entsprechen den ursprünglichen Figurenseiten 1 bis 4 mit den Figuren 1 bis 5.


3.2        Die Lehren der Patentansprüche 1 und 7 sind in der Anmeldung so deutlich
und vollständig offenbart, dass ein Fachmann sie ausführen kann (§ 34 Abs. 4
PatG).


3.3        Die Gegenstände der Patentansprüche 1 und 7 sind nicht aus dem Stand der
Technik bekannt und beruhen demgegenüber auch auf einer erfinderischen Tätigkeit. Insbesondere leitet der Fachmann die eine Filter- und Routingeinheit betreffenden, durch die Merkmale M2.1, M4.2, M4.3, M5.1 und M5.2 beschriebenen Datenverarbeitungsmaßnahmen nicht aus dem Stand der Technik ab.

                                        - 14 -



3.3.1 Zum Stand der Technik wurden im Prüfungsverfahren vor dem Deutschen
Patent- und Markenamt die Druckschriften


      P1)    William, P. et al.: Concurrent Direct Network Access for Virtual
             Machine Monitors. In: Proceedings of the 2007 IEEE 13th International
             Symposium on High Performance Computer Architecture. Scottsdale,
             AZ, USA, 10 - 14 Feb. 2007. pp 306 - 317,


      P2)    US 7 620 955 B1,


      P3)    US 2005 / 0 207 407 A1


und


      P4)    Mustacchi, R.: Turtles on the wire: understanding how the OS uses the
             modern NIC. 15.9.2016 <https://www.joyent.com/blog/virtualizingnics> In: <https://web.archive.org> am 14.3.2017 (recherchiert am
             30.4.2019)


ermittelt.


3.3.2 Die als „nächstliegender“ Stand der Technik anzusehende Druckschrift P1
beschreibt Hard- und Softwaremechanismen, die mehreren von einem „virtual
machine monitor“ - also einem Hypervisor - verwalteten, voneinander isolierten virtuellen Maschinen einen gleichzeitigen direkten Netzwerkzugang ermöglichen (vgl.
Abstract, Abschnitt 1, erster bis dritter Absatz; Abschnitt 2.1, erster Absatz). Daneben besitzt jede virtuelle Maschine einen nur ihr zugeordneten Speicherabschnitt
(„context“) auf einer Netzwerkkarte, über den die Kommunikation geleitet wird (vgl.
Abschnitt 1, vierter Absatz; Abschnitte 3 und 3.1, jeweils erster Absatz; Abschnitt 4,
dritter und sechster Absatz). Zum Transferieren der auf der Netzwerkkarte eingehenden Datenpakete zur entsprechenden virtuellen Maschine bzw. zum in der virtuellen Maschine ablaufenden „guest operating system“ wird eine dem jeweiligen

                                         - 15 -



„context“ zugeordnete MAC-Adresse verwendet (Abschnitt 3.1, insbesondere letzter
Satz). Dabei ist es für den Fachmann zum einen selbstverständlich, dass eine virtuelle Maschine auch eine virtuelle Schnittstelle zum Datenaustausch mit dem ihr
zugeordneten „context“ auf der Netzwerkkarte besitzt, und zum anderen, dass ein
einer virtuellen Maschine zugeordneter Speicherabschnitt jeweils aus Speicherbereichen - z.B. aus Blöcken einzelner Speicherzellen - besteht.


Bis auf den Umstand, dass die physikalische Netzwerkschnittstelle der Herstellung
einer Kommunikationsverbindung zu einem speziellen Netzwerk - nämlich einem
Fahrzeugnetzwerk - dienen soll (Teilaspekt von Merkmal M4), verwirklicht die Lehre
der Druckschrift P1 damit die Merkmale M1, M2, M3, M3.1 und M4.


Auch das Merkmal M3.2 ist der Druckschrift P1 zu entnehmen, da in jeder virtuellen
Maschine mehrere Dienste - also Applikationen - voneinander isoliert betrieben werden können (vgl. Abschnitt 1 Satz 3 – „[…] multiple virtual machines, each encapsulating one or more services, […]“).


Das Merkmal M4.1 ist ebenfalls aus der Druckschrift P1 bekannt, da die Netzwerkkarte („NIC“) „receive packet buffers“ besitzt (vgl. Abschnitt 4, vorletzter Absatz).


Da die eingehenden Datenpakete anhand einer MAC-Adresse an die einzelnen
„guests“ verteilt werden (vgl. Abschnitt 3.1 – „When network packets are received
by the NIC, it uses the Ethernet MAC address to demultiplex the traffic, and transfers
each packet to the appropriate guest“), muss auch eine entsprechende „Filter- und
Routingeinheit“ auf der Netzwerkkarte vorhanden sein, die die MAC-Adressen aus
den Headers der Datenpakete extrahiert („herausfiltert“) und auswertet, um die
Pakete an die richtige virtuelle Maschine weiterzuleiten (zu „routen“), für die das
jeweilige Paket bestimmt ist (Merkmal M5).


Jedoch sind zumindest die Anweisungen der Merkmale M2.1, M4.2, M4.3, M5.1 und
M5.2 der Druckschrift P1 nicht zu entnehmen; diese betreffen insbesondere die

                                       - 16 -



Arbeitsweise der beanspruchten Filter- und Routingeinheit und ergeben sich für den
Fachmann auch nicht in naheliegender Weise aus der Lehre der Druckschrift P1.


Hinsichtlich der durch die Merkmale M4.2, M4.3, M5.1 und M5.2 beschriebenen, auf
der Netzwerkkarte nach dem Empfang eines Datenpakets vorgesehenen Datenverarbeitungsmaßnahmen, die zur Kopie des Datenpakets in einen Speicherbereich
einer virtuellen Maschine führen, ist der Druckschrift P1 allenfalls allgemein entnehmbar, dass der Transfer der Datenpakete durch DMA-Zugriffe über ein Ethernet-Netzwerk erfolgt und dazu ein PCI-basiertes System verwendet wird (vgl. Abschnitte 3.1 und 3.4 sowie Abschnitt 4, erster Absatz).


Jedoch liefert die Druckschrift P1 keinen Anlass für die spezielle Vorgehensweise,
gleichzeitig mit dem Schreiben eines Datenpakets in einen RX-Puffer der Netzwerkkarte eine Eingangsmeldung an einen Ethernet-Treiber zu übermitteln, der seinerseits ein Triggersignal an eine Filter- und Routingeinheit sendet, welche mittels
eines weiteren Triggersignals einen PCIe-Treiber veranlasst, das Kopieren des
Datenpakets über ihre eigenen DMA-Ausgänge vorzunehmen (Merkmale M4.2,
M5.1 und M5.2).


Ferner ist es zwar selbstverständlich, dass zumindest die in den „receive packet
buffers“ gespeicherte Header-Information ausgelesen und ausgewertet werden
muss. Das legt aber noch nicht nahe, dass die „receive packet buffers“ per se dazu
eingerichtet sein müssten, den Header im Rahmen eines Sendeschritts quasi „aktiv“
an eine Filter- und Routingeinheit zu übermitteln, wie es das Merkmal M4.3 erfordert. Vielmehr wäre es eine durchaus übliche Vorgehensweise, den Header aus
einem „receive packet buffer“ mittels einer separaten Datenverarbeitungseinheit der
Netzwerkkarte auszulesen, welche auch die aktive Weiterleitung des Headers an
eine Auswerteeinheit übernimmt. Dabei würde der „receive packet buffer“ lediglich
eine passive Rolle spielen.

                                         - 17 -



Zudem beschränken sich die der Druckschrift P1 allenfalls implizit entnehmbaren
Schritte des „Filterns“ und „Routens“ lediglich auf die Extraktion einer MAC-Adresse
und die Weiterleitung eines Datenpakets an eine der MAC-Adresse entsprechende
virtuelle Netzwerk-Schnittstelle, so dass auch für das Bereitstellen spezieller Filterund Routing-Regeln gemäß Merkmal M2.1 keine Veranlassung besteht.


3.3.3 Auch die Druckschriften P2 bis P4 legen die Lehre der Merkmale M2.1, M4.2,
M4.3, M5.1 und M5.2 nicht nahe.


So beschreibt die Druckschrift P2 den Austausch von Datenpaketen zwischen virtuellen Maschinen in Kernel-basierten virtualisierten Systemen, bei denen sowohl
reale physikalische als auch virtuelle Puffer zum Datenaustausch vorgesehen sind
(vgl. Figuren 1 bis 3; Spalte 3, Zeile 29 bis 55; Spalte 12, Zeile 3 bis 61).


Nachdem ein Datenpaket von der Netzwerkkarte empfangen worden ist, bestimmt
ein Kernel die jeweilige virtuelle Netzwerkkarte der virtuellen Maschine, für die das
Datenpaket bestimmt ist und kopiert dieses in den zugehörigen „guest receive
packet data buffer“ der virtuellen „Ziel“-Maschine. Danach wird dem „virtual machine
monitor“ eine „Aktion“ (d.h. eine Anfrage, etwas zu tun) übermittelt, woraufhin dieser
einen Interrupt an die virtuelle Maschine sendet (vgl. insbesondere Spalte 10,
Zeile 18 bis 36; Spalte 18, Zeile 17 bis 39).


Dies unterscheidet sich von der mit dem Patentanspruch 1 beanspruchten Lehre
bereits darin, dass zum Transfer des Datenpakets keine Filter- und Routingeinheit
zum Einsatz kommt, welcher von einem „virtual machine monitor“ Filter- und Routing-Regeln bereitgestellt wurden (Merkmal M2.1).


Dementsprechend zeigt die Druckschrift P2 auch nicht, dass einzelne Datenverarbeitungseinheiten dazu eingerichtet wären, die genaue Abfolge der zwischen dem
Schreiben eines Datenpakets in einen RX-Puffer der Netzwerkkarte (Merkmal M4.1)

                                       - 18 -



und dem Kopieren des Datenpakets (Merkmal M5.2) erfolgenden Schritte der Merkmale M4.2, M4.3, M5 und M5.1 zu realisieren. Dass eine Filter- und Routingeinheit
einen Header eines Datenpakets auswertet und ein Datenpaket über ihre eigenen
DMA-Ausgänge übermittelt, ist der Druckschrift P2 bereits nicht zu entnehmen.


Es sind auch keine Anregungen erkennbar, die den Fachmann dazu motivieren
könnten, die aus der Druckschrift P2 bekannte spezielle Abfolge der zwischen dem
Empfang eines Datenpakets und dem Kopieren dieses Pakets in einen „guest
receive packet data buffer“ ausgeführten Schritte in die exakte Sequenz der durch
den Patentanspruch 1 beschriebenen Anweisungen zu transformieren.


Die Druckschrift P3 betrifft das Demultiplexen von Datenpaketen in einer Virtuelle-Maschinen-Umgebung (vgl. Abstract). Als nachteilig ist beschrieben, dass ein von
einer Netzwerkkarte empfangenes Datenpaket zunächst in einen verfügbaren DMA-Puffer geschrieben wird, der keiner speziellen virtuellen Maschine zugeordnet ist,
und erst danach in einem zweiten Schritt in den entsprechenden Puffer der virtuellen
„Ziel“-Maschine (Absatz [0010], Figur 1). Stattdessen wird vorgeschlagen, das
Datenpaket zunächst in einem „DMA buffer pool“ zu speichern, der aus „unmapped
pages“ - d.h. Speicherbereichen ohne Zuordnung zu einer bestimmten virtuellen
Maschine - besteht. Anschließend wird die physische Adresse, unter der das Datenpaket gespeichert ist, der virtuellen Netzwerkkarte derjenigen virtuellen Maschine
übermittelt, für die das Paket bestimmt ist. Dadurch wird gerade der Nachteil vermieden, dass eingehende Datenpakete in verschiedene DMA-Puffer geschrieben werden müssen (vgl. Absätze [0011]-[0015]).


Die Druckschrift P3 zeigt zwar noch das Merkmal, dass ein „enhanced demultiplexer 200“ eingehende Datenpakete auf die in ihnen enthaltene MAC- oder IP-Adresse hin untersucht und diese Pakete an eine entsprechende Ziel-Netzwerkkarte weiterleitet (Absatz [0014]). Aber auch die Lehre dieser Druckschrift legt
weder nahe, dass einzelne Datenverarbeitungseinheiten dazu eingerichtet sind, die
genaue Abfolge der durch die Merkmale M4.2, M4.3, M5.1 und M5.2 beschriebenen

                                       - 19 -



Schritte umzusetzen, noch gibt sie einen Anlass dafür, dass ein Hypervisor eine
Filter- und Routingeinheit Filter- und Routing-Regeln gemäß Merkmal M2.1 bereitstellt.


Die Druckschrift P4 schließlich ist ein allgemein gehaltener Blog-Artikel über Netzwerkkarten, dessen Inhalte - soweit sie im Hinblick auf den Gegenstand des Patentanspruchs 1 relevant sind - nicht über das hinausgehen, was der Fachmann bereits
auf Grundlage der Lehre der Druckschrift P1 bis P3 ableitet.


Nach allem ist nicht erkennbar, wie der Fachmann in Kenntnis lediglich des aus den
ermittelten Druckschriften bekannten Standes der Technik zur beanspruchten Lehre
nach Patentanspruch 1 hätte gelangen können.


3.3.4 Entsprechendes gilt für den Patentanspruch 7, dessen Datenkommunikationsverfahren auf die virtuellen Maschinen und die physikalische Netzwerk-Schnittstelle der Fahrzeugelektronikeinheit nach dem Patentanspruch 1 rückbezogen ist
und daher insbesondere auch die die Filter- und Routingeinheit betreffenden Maßnahmen der Merkmale M2.1, M4.2, M5.1 und M5.2 umfasst. Diese Maßnahmen
gehen - wie oben ausgeführt - weder aus dem Stand der Technik hervor noch sind
sie durch diesen nahegelegt.


4.        Die Patentansprüche 1 und 7 sind gewährbar.


Die abhängigen Patentansprüche 2 bis 6 sowie 8 sind ebenfalls gewährbar.


Auch die übrigen Voraussetzungen für eine Patenterteilung sind erfüllt.

                                              - 20 -



                                  Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft
       Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt
       war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht
       der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften
       über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Morawek                        Bayer                         Forkel                       Städele
