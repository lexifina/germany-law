---
ecli: "ECLI:DE:BPatG:2018:120718U2Ni26.16EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 26/16"
decided: "2018-07-12"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=30&nr=34776&anz=825&pos=459&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2018-07-12_2_Ni_26_16_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 26/16 vom 2018-07-12

## Entscheidung

BUNDESPATENTGERICHT

                         IM NAMEN DES VOLKES

                                     URTEIL
2 Ni 26/16 (EP)                                            Verkündet am
verbunden mit                                              12. Juli 2018
2 Ni 46/16 (EP)                                                 …


(Aktenzeichen)




                          In der Patentnichtigkeitssache

 …




 ECLI:DE:BPatG:2018:120718U2Ni26.16EP.0

                                      -2-


…




                  betreffend das europäische Patent 1 196 856
                                (DE 600 45 552)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 12. Juli 2018 unter Mitwirkung des Vorsitzenden
Richters   Guth   sowie   des   Richters    Dipl.-Ing. Baumgardt,   der   Richterin
Dipl.-Phys. Dr. Thum-Rung    und    der     Richter   Dipl.-Phys. Dr. Forkel   und
Dr. Himmelmann

                                         -3-


für Recht erkannt:


        I.     Das europäische Patent 1 196 856 wird mit Wirkung für das
               Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


        II.    Die Kosten des Rechtsstreits trägt die Beklagte.


        III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120%
               des zu vollstreckenden Betrages vorläufig vollstreckbar.




                                     Tatbestand


Die Beklagte ist Inhaberin des am 30. Juni 2000 angemeldeten und am
19. Januar 2011 veröffentlichten Patents EP 1 196 856 B1 (im Folgenden: Streitpatent) mit der Bezeichnung „METHOD AND APPARATUS FOR MONITORING
TRAFFIC IN A NETWORK“ (deutsch: „Verfahren und Gerät um den Netzwerkverkehr zu überwachen“), das auf die internationale Anmeldung mit der Veröffentlichungsnummer WO 2001 / 1 272 A1 zurückgeht und für das die Priorität der US-Anmeldung 60 / 141 903 vom 30. Juni 1999 in Anspruch genommen wird. Das in
der Verfahrenssprache Englisch abgefasste Streitpatent wird vom Deutschen Patent- und Markenamt unter der Nummer DE 600 45 552.1 geführt.


Mit ihren Klagen begehren die Klägerinnen jeweils die Nichtigerklärung des deutschen Teils des europäischen Patents in vollem Umfang.


Die Beklagte verteidigt ihr Streitpatent mit dem Hauptantrag in vollem Umfang und
hilfsweise beschränkt mit den Hilfsanträgen 1, 2a bis 2d und 4 jeweils vom
8. Januar 2018 sowie den Hilfsanträgen 2e, 3 und 5 bis 9 jeweils vom
28. Mai 2018.

                                         -4-


Das Streitpatent umfasst 92 Patentansprüche, mit einem auf ein „Verfahren zum
Erkennen eines oder mehrerer Gesprächsflüsse für Pakete, die durch einen Verbindungspunkt in einem Computernetz gehen“ gerichteten Hauptanspruch und 39
darauf rückbezogenen Unteransprüchen, sowie mit einem nebengeordneten, auf
einen dafür eingerichteten „Paketmonitor“ gerichteten Anspruch 41 und 51 darauf
rückbezogenen Unteransprüchen.


In der Verfahrenssprache Englisch lauten die erteilten unabhängigen Patentansprüche 1 und 41 gemäß der Streitpatentschrift EP 1 196 856 B1:


       „1.   A method of recognizing one or more conversational flows
       for packets passing through a connection point (121) on a computer network (102), each packet conforming to at least one
       protocol, wherein at least one said protocol defines one or more
       conversational flows that each includes a plurality of states of the
       flow including an initial state, and transitions from the initial state
       to at least one of the plurality of states of the flow, the method
       comprising:


             receiving a packet (302) from a packet acquisition device;


             performing at least one parsing operation (304) and/or at
             least one extraction operation (306) on the packet to create
             a parser record comprising a function (312) of selected portions of the packet; wherein at least one of the parsing
             and/or extraction operations depend on one or more of the
             protocols to which the packet conforms; looking up (314) in
             a flow-entry database (324) comprising flow entries for any
             previously encountered conversational flows, the look up
             using at least some of the selected packet portions and
             determining (316) if the packet is of an existing conversational flow;

                                  -5-


     if the packet is of an existing conversational flow, classifying
     the packet as belonging to the found existing conversational
     flow and performing (328, 330) any state operation or
     operations specified in a database (326) for the state of the
     conversational flow; and


     if the packet is of a new conversational flow, storing (322) a
     new flow-entry for the new conversational flow in the flowentry database, including identifying information for future
     packets to be identified with the new flow-entry, determining
     the state of the flow (318) using the database (326) and
     performing (328, 330) any state operation or operations
     specified in the database (326) for the state of the flow;


     wherein each conversational flow that includes a plurality of
     states is recognized by transitioning through a plurality of
     states of the conversational flow, and at each state, carrying
     out one or more state operations specified in the database
     (326) for the state of the flow.“


„41. A packet monitor (108) for recognizing one or more
conversational flows for packets passing through a connection
point (121) on a computer network (102), each packet
conforming to at least one protocol, wherein at least one said
protocol defines one or more conversational flows that each
includes a plurality of states of the flow including an initial state,
and transitions from the initial state to at least one of the plurality
of states of the flow, the packet monitor comprising:


     a packet acquisition device (1502) for coupling to the
     connection point and configured to receive packets passing
     through the connection point, including an input buffer

                           -6-


memory (1008) coupled to and configured to accept a
packet;


a parser subsystem (301) coupled to the input buffer
memory and including a slicer (1007), the parsing
subsystem configured to extract selected portions of the
received packet and to output a parser record containing
the selected portions, wherein the operation of the parser
subsystem depends on one or more of the protocols to
which the packet conforms;


a memory (324) for storing a database comprising flowentries for any previously encountered conversational flows,
each flow-entry identified by identifying information stored in
the flow-entry, conversational flows having one or more
states;


a lookup engine (1107) coupled to the output of the parser
subsystem and to the memory and configured to lookup
whether the particular packet whose parser record is output
by the parser subsystem has a matching flow-entry in the
flow-entry database, the looking up using at least some of
the selected packet portions and determining if the packet is
of an existing conversational flow;


a flow insertion engine (1110) coupled to the memory and
to the lookup engine and configured to create a flow-entry in
the flow-entry database, the flow-entry including identifying
information for future packets to be identified with the new
flow-entry;


a database (326, 1109) specifying state operations and
patterns for conversational flows; and

                                        -7-


             a state processor (1108) configured to perform any state
             operations specified in the database (326, 1109) for the
             state of the flow and to determine the state of the flow if the
             packet is of a new conversational flow;


             wherein the lookup engine is configured to classify the
             packet as belonging to the found existing conversational
             flow if the packet is of an existing conversational flow;


             and the flow insertion engine is configured to store a new
             flow-entry for the new conversational flow in the flow-entry
             database if the packet is of a new conversational flow, the
             new flow entry including identifying information for future
             packets to be identified with the new flow-entry.“


Wegen des Wortlautes der auf Patentanspruch 1 unmittelbar oder mittelbar rückbezogenen Unteransprüche 2 bis 40 und der auf Patentanspruch 41 unmittelbar
oder mittelbar rückbezogenen Unteransprüche 42 bis 92 wird auf die Streitpatentschrift verwiesen.


Zum Wortlaut der jeweiligen Patentansprüche 1 in der Fassung der Hilfsanträge 1,
2a bis 2e und 3 bis 9 und insbesondere zu den Unterschieden gegenüber dem
Patentanspruch 1 der erteilten Fassung wird auf die Entscheidungsgründe und die
dortigen Erläuterungen verwiesen.


Die Klägerinnen machen Nichtigkeitsgründe gemäß Art. II § 6 Abs. 1 IntPatÜG
geltend, nämlich dass


1. der Gegenstand des Streitpatents nicht patentfähig sei, Art. II § 6 Abs. 1
   Nr. 1 IntPatÜG in Verbindung mit Art. 54 und Art. 56 EPÜ,


2. das Streitpatent die Erfindung nicht so deutlich und vollständig offenbare, dass
   ein Fachmann sie ausführen könne, Art. II § 6 Abs. 1 Nr. 2 IntPatÜG, und dass

                                         -8-


3. der Gegenstand des Streitpatents über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinausgehe, Art. II § 6 Abs. 1 Nr. 3
   IntPatÜG.


Zur Stützung ihres Vorbringens nennen die Klägerinnen u.a. folgende Druckschriften und Unterlagen:


Betreffend das Streitpatent
     N1        EP 1 196 856 B1 (Streitpatentschrift)
     N2        Registerauszug (Az. 600 45 552.1)
     N3        US 60/141,903 (Prioritätsanmeldung)
     N4        Übersicht Rechtsübergänge an Prioritätsanmeldung (USPTO Public
               PAIR)
     N5        Merkmalsgliederung der Ansprüche 1 und 41 (Verfahrenssprache
               Englisch)
     N6        Merkmalsgliederung der Ansprüche 1 und 41 (Deutsche Übersetzung)
     N7        Merkmalszuordnung zwischen den Ansprüchen 1 und 41
     N8        WO 01/01272 A2 (Anmeldefassung des Streitpatents)
     N9        Übersicht der Änderungen der Ansprüche 1 und 41 im Verlauf des
               europäischen Prüfungsverfahrens
     N10       Zuordnungstabelle der Anmelderin
     N11       Berufungsbegründung      der    Nichtigkeitsbeklagten   im   parallelen
               Verletzungsverfahren (Az. 6 U 186/16)
     N12       Eidesstattliche Versicherung von Herrn Z… vom
               12. März 2017
     N13       RFC 959: File Transfer Protocol (October 1985)
     N14       Vergleich der neuen Merkmale (2.1) und (3.3) des (jetzigen)
               Hilfsantrags 9 mit den ursprünglichen Ansprüchen 60 bis 63
     N15       Auszug aus „TCP/IP Illustrated“ Vol.1 (1994) – Kapitel 29
     N16       Gutachten Dr. B…
     N17       Gutachten Prof. Dr. B1… zur Frage des Übergangs des
               patentrechtlichen Prioritätsrechts nach Art. 87 EPÜ

                                      -9-


Entgegenhaltungen
    E1     Paxson: „Bro: A System for Detecting Network Intruders in Real-Time“, Proceedings of the 7th USENIX Security Symposium, 1998
           (dazu weitere Erläuterungen E1a, BROa – BROe)
    E2     WO 92/19054 A1
    E3     US 5,862,335
    E4     US 5,802,320
    E5     Musial: „Neue Verfahren zur maschinellen Analyse des Verhaltens
           von Protokollmaschinen anhand passiver Beobachtung“, Dissertation
           TU Berlin, 20. Juli 1999
    E6     WO 00/52869 A2
    E7     Brownlee et al.: „Traffic Flow Measurement: Architecture“, RFC 2722,
           Mai 1999
    E8     Check Point FireWall-I™ White Paper (Version 3.0), 1997
    E8a    Check Point™ VPN-1 / FireWall-1® Administration Guide, Jan. 2000
    E8b    Check Point™ VPN-1 / FireWall-1® Reference Guide, Jan. 2000
    E8c    Check Point™ VPN-1 / FireWall-1® User Guide (auf CD)
    E9     Ptacek et al.: „Insertion, Evasion, and Denial of Service: Eluding
           Network Intrusion Detection“, Secure Networks Inc., 1998
    E10    US 5,430,709
    E11    Decasper et al.: „Router Plugins - A Software Architecture for Next
           Generation Routers“, ACM SIGCOMM Conference, 1998
    E12    WO 99/53648 A2
    E13    US 5,347,524
    E14    Goncalves et al.: „Check Point Firewall-1 Administration Guide“,
           Seiten 28-35 und 258-259, McGraw-Hill, 1. Sept. 1999
    E15    Schobert: „Protokollanalyse in lokalen Netzen: Messtechnik und
           Interpretation von Datenübertragungsprotokollen in lokalen Netzen“,
           Seiten 247-249, Expert-Verlag, 1994
    E16    WO 01/65343 A1
    E17    Malan et al.: „An Extensible Probe Architecture for Network Protocol
           Performance Measurement“, ACM SIGCOMM Conference, 1998
    E18    NetFlow Services and Applications Whitepaper, Cisco Systems, 1999

                                     - 10 -


     E19    US 6,006,268
     E20    EP 0 909 073 A2
     E21    DE 196 40 346 C2
     E22    Claffy et al.: „A Parameterizable Methodology for Internet Traffic Flow
            Profiling“, IEEE Journal on Selected Areas in Communications, 13 (8):
            S. 1481-1494; 1995
     E23    Che et al.: „Adaptive Resource Management for Flow-based IP/ATM
            Hybride Switching Systems“, IEEE Transactions on Networking, 6 (5):
            S. 544-557; 1998
     E24    US 5,351,243
     E25    WO 98/28938 A1
     E26    WO 00/31963 A1
     E27    US 5,101,402
     E28    WO 00/02114 A2
     E29    Naylor: „The Re-Analysis and Re-Implementation of X.25“, B.Sc.
            Thesis, University of Nottingham, 1997
     E30    US 5,793,954
     E31    WO 98/26510 A2
     E32    US 5,892,924
     E33    MeterFlow™ C-Code 5.5, Frequently Asked Questions, 1999
     E33a   Eidesstattliche Versicherung von Herrn B2…,
            17. März 2017
     E33b   Webseite-Auszug
            „http://web.archive.org/web/20000301200951/http://www.apptitude.
            com/products/meterflow.htm“ (Stand vom 1. März 2000)


Die Klägerinnen sind der Ansicht, die Ergänzung der Patentansprüche 1 und 41
gemäß den Hilfsanträgen 1 und 2a bis 2e durch das Merkmal „a conversational
flow comprising more than one connection“ sei unzulässig, weil bereits der
auch in der geltenden Fassung verwendete Begriff „connection“ unklar sei. Mangelnde Klarheit erteilter Ansprüche sei zwar kein Nichtigkeitsgrund, aber geänderte Ansprüche müssten auch im Nichtigkeitsverfahren sachlich geprüft werden

                                         - 11 -


und den Klarheitserfordernissen nach § 34 Abs. 3 Nr. 3 PatG / Art. 84 EPÜ genügen.


Die Klägerinnen machen insbesondere geltend:


a)     das Streitpatent beschreibe an keiner Stelle, wie die „parser records“ und deren „selected portions“ für das Merkmal (3.1) aussehen sollten bzw. auszuwählen seien;


b)     auch    wie   der   neue   Flusseintrag    gemäß       Merkmal   (6.1)   und   die
       Identifizierungsinformation des Merkmals (6.2) aussehen solle, sei an keiner
       Stelle erläutert;


c)     und ferner widersprächen die Anweisungen der Merkmalsgruppe 7, die lautet:


       „(7)   wherein each conversational flow that includes a plurality of states is
              recognized


       (7.1) by transitioning through a plurality of states of the conversational flow,
              and


       (7.2) at each state, carrying out one or more state operations specified in
              the database (326) for the state of the flow”


       denjenigen der Merkmalsgruppe 4, die lautet:


       „(4)   looking up (314) in a flow-entry database (324) comprising flow entries
              for any previously encountered conversational flows,


       (4.1) the look up using at least some of the selected packet portions and


       (4.2) determining (316) if the packet is of an existing conversational flow”.

                                      - 12 -


Die Klägerinnen sind weiter der Meinung, der als Beispiel herangezogene Ethernet-Frame enthalte die MAC-Adressen und diese hätten mit der Erkennung von
FTP-Verbindungen nichts zu tun. Sie bemängeln die ursprüngliche Offenbarung
des Merkmals „wherein at least one said protocol defines one or more conversational flows”.


Die Klägerinnen machen weiter geltend, da das Streitpatent gegenüber der Nachanmeldung (N8) unzulässig erweitert sei, gehe es zwangsläufig auch über die Prioritätsanmeldung (N3) hinaus und könne deshalb deren Priorität nicht in Anspruch
nehmen. Auch habe eine rechtswirksame Übertragung der Priorität der US
60/141,903 nicht stattgefunden.


Zudem vermissen die Klägerinnen jegliche Offenbarung, dass „mindestens ein
Protokoll einen oder mehrere Gesprächsflüsse definiert“. Weil außerdem nicht alle
Details in die Merkmalsgruppe 7 aufgenommen seien, beurteilen sie die Merkmalsgruppe 7 als eine unzulässige Verallgemeinerung. Das zusätzliche Merkmal
„in real time“ des Hilfsantrags 3 sei unklar und rein aufgabenhaft formuliert, da
nicht spezifiziert werde, wie und aufgrund welcher Merkmale die gewünschte
Echtzeitfähigkeit erreicht werde. Ferner fehle es an der Ausführbarkeit und der ursprünglichen Offenbarung. Dieselben Mängel würden im Blick auf das Merkmal
“the carrying out of the state operations furthering the process of identifying the
application content of a conversational ﬂow” bestehen. Auch hinsichtlich des
Merkmals “and the state operations comprising building a new signature for future
recognition of packets of the next state” machen die Klägerinnen fehlende Ausführbarkeit und fehlende Offenbarung geltend.


Die Klägerinnen sind ferner der Auffassung, dass der Fachmann in der Lage gewesen sei, die detaillierte Arbeitsweise des in der Druckschrift E1 beschriebenen
Paketmonitors aus dem (ihrer Auffassung nach öffentlich zugänglichen) Source-Code abzuleiten, so dass die E1 die technische Lehre des Streitpatents vorweg
nehme. Die Klägerinnen weisen zudem darauf hin, dass der Patentanspruch 1 des
Streitpatents den Begriff „Gesprächsfluss“ nicht darauf beschränke, dass dieser
mehrere „Verbindungsflüsse“ (connection flows) umfassen müsse. Haupt- und

                                       - 13 -


Hilfsanträge der Patentinhaberin würden zudem an formalen Mängeln leiden, namentlich an mangelnder Klarheit, unzulässiger Erweiterung und fehlender Ausführbarkeit.


Im Übrigen halten die Klägerinnen die Einreichung von Hilfsantrag 8, der einen
gänzlich neuen Gegenstand betreffe, für verspätet und beantragen daher seine
Zurückweisung.


Die Klägerinnen stellen die Anträge,


        das europäische Patent 1 196 856 in vollem Umfang mit Wirkung
        für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig
        zu erklären.


Die Beklagte stellt den Antrag,


        die Klage abzuweisen,
        hilfsweise
        unter Klageabweisung im Übrigen das europäische Patent
        1 196 856 dadurch teilweise für nichtig zu erklären, dass seine
        Patentansprüche die Fassung eines der Hilfsanträge 1, 2a bis 2d
        sowie 4 vom 8. Januar 2018, weiter hilfsweise eines der Hilfsanträge 2e, 3, 5 bis 9 vom 28. Mai 2018, in der Reihenfolge ihrer
        Nummerierung, erhalten.


Die Beklagte erklärt, dass sie die Ansprüche gemäß Haupt- und Hilfsanträgen jeweils als geschlossene Anspruchssätze ansieht, die sie jeweils in ihrer Gesamtheit
beansprucht.


Die Beklagte verteidigt das Streitpatent mit dem Hauptantrag in vollem Umfang
und mit den genannten Hilfsanträgen beschränkt und tritt dem Vortrag der Klägerinnen in allen Punkten entgegen. Sie ist insbesondere der Auffassung, sie habe
die Priorität der US 60/141,903 wirksam in Anspruch genommen.

                                       - 14 -


Zur Unterstützung ihrer Argumentation reicht sie u. a. folgende Dokumente bzw.
Ausdrucke ein:


     MFG1         BGH-Entscheidung X ZR 49/12 – Fahrzeugscheibe
     MFG2/1 bis MFG2/6           Eidesstattliche Versicherungen der sechs auf der
                  Streitpatentschrift genannten Erfinder zur Übertragung des Prioritätsrechts
     MFG3         Entscheidung USPTO Patent Trial and Appeals Board
                  betreffend das Patent US 6,771,646 B1
     MFG4         US 6,771,646 B1
     MFG5         US 6,115,393
     MFG7         Dokumentation der Wayback Machine betreffend die Internet-Seite http://www.apptitude.com/pdfs/mflowfaq.pdf
     MFG8         Wikipedia: Connection-oriented communication (15.12.2017)
     MFG9         https://www.lifewire.com/definition-of-protocol-network-817949?print „Network Protocols“ (Ausdruck vom 20.12.2017)
     MFG10        RFC 783: TFTP Protocol Rev. 2 (1981)
     MFG11        Wikipedia: File Transfer Protocol (18.12.2017)
     MFG12        Wikipedia: Transport Layer (30.12.2017)
     MFG16        RFC 2074: Remote Network Monitoring MIB Protocol Identifiers
                  (1997) – zur Erläuterung der Begriffe “child protocol” und “parent
                  protocol”
     MFG17        Wikipedia: Transmission Control Protocol (21.6.2018)
     MFG18        Email-Verkehr betr. Dokumentation zu „Bro”, 1998


Die Beklagte erläutert, das Streitpatent offenbare den ersten funktionsfähigen Paketmonitor, der durch einen progressiven Erkennungsprozess das Anwendungsschicht-Protokoll bzw. die Anwendung erkennen könne, und erkennen könne,
dass Verbindungsflüsse in einem gemeinsamen Kontext stünden und somit einem
Gesprächsfluss zugeordnet werden könnten.


Ein „Gesprächsfluss“ („conversational flow“) sei eine Reihe oder ein Fluss von Paketen, die zusammengehörten, da sie eine gemeinsame Aktivität (Kontext) zwi-

                                      - 15 -


schen zwei oder mehr Geräten innerhalb des Computernetzes repräsentierten.
Der Netzwerkmonitor „Bro“ aus PAXSON (gemäß der Druckschrift E1 und den zusätzlichen Erläuterungen) führe eine Verarbeitung von Verbindungsflüssen auf der
Transportschicht aus, nicht jedoch eine Zustandsverarbeitung bezüglich Gesprächsflüssen   auf   der    Anwendungsschicht.    Verbindungen     der   vierten
OSI-Schicht (TCP-Verbindungen) seien keine Gesprächsflüsse, sondern Verbindungsflüsse im Sinne des Streitpatents. Darüber hinaus werde die Vorveröffentlichung der zusätzlichen Erläuterungen und die öffentliche Zugänglichkeit des
Quellcodes bestritten; insbesondere auch, dass der Fachmann in der Lage gewesen sei, diesen zu verstehen und die Details der beanspruchten Lehre unmittelbar
und eindeutig zu entnehmen.


Die Beklagte macht geltend, das Streitpatent führe eine progressive Analyse von
Paketen eines Gesprächsflusses zur Identifizierung eines Anwendungsschicht-Protokolls durch, indem es sich an den „Zustand“ des Gesprächsflusses von einem Paket zum nächsten erinnere. Der Unterschied zwischen der Lehre des
Streitpatents und der Druckschrift E2 liege vor allem darin, dass die Druckschrift
E2 „nur“ Dialog-Erkennungen auf niedrigeren Protokoll-Ebenen (insbes. TCP) betreffe, welche nach Auslegung der Beklagten „Verbindungsflüsse“ seien. Die Beklagte verweist hierzu auf eine Entscheidung des „Patent Trial & Appeal Board“
des United States Patent and Trademark Office (USPTO) betreffend das Patent
US 6 771 646 B1, welches auf dieselbe Voranmeldung zurückgehe wie das Streitpatent.


Der in der Druckschrift E2 beschriebene Netzwerkmonitor, der lediglich einzelne
TCP-Verbindungen erkennen könne, sei noch kein Paketmonitor zur Erkennung
von Gesprächsflüssen im Sinne des Streitpatents, denn Gesprächsflüsse müssten
solche Gesprächsflüsse umfassen, die aus mehreren Verbindungsflüssen auf
Netzwerk-Ebene bestehen würden. Eine TCP-Verbindung sei nur als „connection“
zu verstehen und erst mehrere TCP-Verbindungen könnten als Gesprächsfluss
verstanden werden. Der Begriff „connection“ sei im Streitpatent und Fachgebiet
ein definierter und stehender Begriff. Die Verbindungen und die Verbindungszustände, die aus den einzelnen Phasen einer einzigen TCP-Verbindung resultier-

                                       - 16 -


ten, seien nach der Definition in Absatz [0010] des Streitpatents ein einzelner Verbindungsfluss, stellten jedoch nicht mehrere Verbindungsflüsse dar.


Zumindest sei das Streitpatent in der Fassung eines der eingereichten Hilfsanträge bestandsfähig, die zulässig und patentfähig seien, insbesondere auch technische Probleme mit technischen Mitteln lösten, so die „Ausgestaltung eines
Compiler-Prozesses“ gemäß Hilfsantrag 9.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                        Entscheidungsgründe


Die Klage, mit der u. a. der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Artikel II § 6 Absatz 1 Nr. 1 IntPatÜG, Artikel 138 Abs. 1 lit a EPÜ i. V. m. Artikel 54 Absatz 1, 2 und Artikel 56 EPÜ geltend gemacht wird, ist zulässig und begründet. Das Streitpatent erweist sich sowohl in der erteilten Fassung als auch in
der Fassung der Hilfsanträge 1, 2a bis 2e und 3 bis 8 als nicht patentfähig, weil die
mit den unabhängigen Patentansprüchen 1 und 41 beanspruchte Lehre aus dem
Stand der Technik vorbekannt oder (im Falle der Hilfsanträge 1 bis 8) durch ihn
nahegelegt war (Art. 54, Art. 56 EPÜ); beim Hilfsantrag 8 (und ggf. auch beim
Hilfsantrag 9) sind zudem Merkmale, welche nicht zur Lösung eines technischen
Problems mit technischen Mitteln beitragen, bei der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen (vgl. BGH GRUR 2011, 125 – Wiedergabe topografischer Informationen).


Die Anspruchsfassung gemäß Hilfsantrag 9 führt bereits deshalb nicht zum Erfolg,
weil der Gegenstand seines Patentanspruchs 1 den Schutzbereich des europäischen Patents erweitern würde, Artikel II § 6 Absatz 1 Nr. 4 IntPatÜG, Artikel 138
Abs. 1 lit d EPÜ.


Ob unabhängig davon auch noch weitere von den Klägerinnen geltend gemachte
Nichtigkeitsgründe vorliegen (wie insbesondere die behauptete fehlende Ausführ-

                                         - 17 -


barkeit bzw. unzureichende Offenbarung oder ein Hinausgehen über den Inhalt
der Patentanmeldung in ihrer ursprünglich eingereichten Fassung), oder ob einzelnen Hilfsanträgen eine mangelnde Klarheit neu formulierter Ansprüche entgegensteht, kann offen bleiben.




                                           I.


1.     Gegenstand des Streitpatents ist ein Verfahren und eine Vorrichtung zur
Analyse, Erkennung und Klassifizierung von übertragenen Datenpaketen bei der
Datenübertragung in Computernetzwerken (bekannt unter den englischsprachigen
Fachbegriffen „network monitor“ bzw. „packet monitor“), umfassend auch eine
Klassifizierung der Datenpakete nach verwendetem Protokoll und „application“
(s. u. Abschnitt 7.3) – vgl. Streitpatent Abs. [0001], [0003], [0013], [0040]).


Damit soll eine Netzwerk-Aktivitätsüberwachung in Echtzeit ermöglicht werden,
z. B. für Instandhaltung und Betrieb des Netzwerks („maintenance and … operation"), um ausgewählte Nutzer (Administratoren) rechtzeitig auf Probleme aufmerksam zu machen (siehe Abs. [0003], [0013]), aber z.B. auch um bestimmte Verbindungen gezielt abhören zu können („Eavesdropping“, siehe Absatz [0086]).


Das Streitpatent geht dabei aus von den bekannten Netzwerk-Protokollen, insbesondere nach dem ISO-Schichtenmodell (ISO layered network model, siehe
Abs. [0075] bis [0078]), und untersucht die einzelnen Datenpakete an einem bestimmten Punkt im Netzwerk (connection point 121) auf vom jeweiligen Übertragungsprotokoll abgeleitete Erkennungs-Muster, um Übertragungs-Verbindungen
zu erkennen und zu klassifizieren und letztlich eine Zuordnung der Pakete zu einer
auf einer höheren Protokoll-Ebene hergestellten Datenverbindung (durch eine
„application“, einen Netzwerk-Dienst) treffen zu können (vgl. Abs. [0041] bis
[0045]).


Ähnliche Verfahren zur Netzwerk-Überwachung waren vorbekannt, wurden aber
laut den Ausführungen im Streitpatent entweder im Nachhinein auf der Basis von

                                         - 18 -


Log-Dateien eingesetzt oder konnten lediglich einzelne Verbindungen („connection
flow“) erkennen (siehe Abs. [0004]) bis [0012]). Das sei jedoch nicht ausreichend,
um im laufenden Betrieb eine Zuordnung unterschiedlicher Einzelverbindungen zu
einzelnen Nutzungsarten oder Netzwerk-Diensten zu ermöglichen. Die Besonderheit der Lehre des Streitpatents soll darin liegen, dass ein vollständiger „Gesprächsfluss“ („conversational flow“) erkannt werden könne, unter Zuordnung der
zugehörigen Einzelverbindungen, in jeder Schicht bis hin zur Anwendungsschicht
des OSI-Modells (siehe Abs. [0013], [0014], [0015], [0077]).




2.       Davon ausgehend nennt das Streitpatent in Absatz [0041] verschiedene
Aufgaben, die durch die beanspruchte Lehre gelöst würden:


     –    Erkennen und Klassifizieren aller Pakete, die in jeweiligen Client /
          Server-Anwendungen zwischen einem Client und einem Server
          ausgetauscht werden;


     –    Erkennen und Klassifizieren von Gesprächsflüssen ("conversational flows"), die einen Punkt in einem Netzwerk in beiden Richtungen passieren, auf allen Protokoll-Ebenen;


     –    Bestimmen der Verbindung und des (Gesprächs-) Fluss-Fortschritts zwischen Clients und Servern anhand der einzelnen Pakete, die über ein Netzwerk ausgetauscht werden;


     –    Beitragen zur Steigerung der Leistung eines Netzwerks abhängig
          von der aktuellen Mischung von Client / Server-Anwendungen, die
          Netzwerkressourcen benötigen;


     –    Führen von Statistiken, die relevant sind für den Mix von Client /
          Server-Anwendungen, die Netzwerkressourcen benötigen;

                                      - 19 -


     –    Erzeugen von Berichten über das Auftreten von bestimmten Paket-Sequenzen, die von bestimmten Anwendungen für Client /
          Server-Netzwerk-Gesprächsflüsse verwendet werden.


Die Beklagte hat im Laufe des Verfahrens den Schwerpunkt darauf gelegt, dass
das beanspruchte Verfahren bzw. der Paketmonitor einen oder mehrere sogenannte Gesprächsflüsse („conversational flows“) aus Paketen, die einen Verbindungspunkt in einem Computernetzwerk passieren, erkennen solle, und Pakete
als zu einem bestimmten Gesprächsfluss gehörend klassifizieren und den sogenannten Zustand eines Gesprächsflusses von Paketen bestimmen solle (siehe
die insoweit in beiden Verfahren gleichlautende Widerspruchsbegründung vom
16. September 2016 bzw. vom 10. Februar 2017, Abschnitt B. IV. „Aufgabe und
Lösung“). Damit offenbare das Streitpatent den ersten funktionsfähigen Paketmonitor, der durch einen progressiven Erkennungsprozess das Anwendungsschicht-Protokoll bzw. die Anwendung erkennen könne, und erkennen könne, dass Verbindungsflüsse in einem gemeinsamen Kontext stehen und somit einem Gesprächsfluss zugeordnet werden könnten (Widerspruchsbegründung, letzter Satz
von Abschnitt A. „Vorbemerkung“).


3.       Die beanspruchte Lösung besteht i. W. darin, jedes einzelne Datenpaket
zu analysieren und in eine Verbindungsfluss-Datenbank so einzutragen, dass
spätere zu demselben Verbindungs- bzw. übergeordneten Gesprächsfluss gehörende Datenpakete wiedererkannt und zugeordnet werden können, unter Zuhilfenahme einer „state machine“ (Zustandsautomat) und einer Datenbank für Zustandsoperationen, welche die aufeinanderfolgenden Zustände der Übertragungsflüsse abspeichert und mitverfolgt. Eine Besonderheit soll darin liegen (siehe
Hilfsanträge), dass aus der Analyse bestimmter Verbindungen im Vorhinein ein
Erkennungsmuster generiert werden kann, welches eine spätere, für sich betrachtet unterschiedliche Verbindung als zu der ersteren Verbindung zugehörig
identifiziert, d. h. aus unzusammenhängenden („disjointed“) Einzelverbindungen
den übergeordneten „Gesprächsfluss“ zu erkennen erlaubt.

                                          - 20 -


4.      Als hier zuständigen Fachmann sieht der Senat einen Hochschulabsolvent
der Informatik oder der Netzwerk-Technik mit praktischen Kenntnissen in der
Kommunikationstechnik und der digitalen Informationsverarbeitung an, insbesondere betreffend die OSI- und TCP/IP-Referenzmodelle und deren Protokollfamilien
sowie die technischen Möglichkeiten, den Netzwerkverkehr mittels bekannter
Firewall-Techniken protokollabhängig zu überwachen; ferner sind ihm der Ansatz
der Endlichen Automaten oder Zustandsautomaten (engl.: „finite-state machines")
sowie die entsprechenden Konzepte zur Zustandsmodellierung von Kommunikationsprozessen vertraut, hier insbesondere in Form von TCP- oder IP-Zustandsautomaten.


5.1     Für den Patentanspruch 1 des Streitpatents wurde im Verfahren die folgende Merkmalsgliederung verwendet:


(1)      A method of recognizing one or more conversational flows for packets
         passing through a connection point (121) on a computer network (102)


(1.1)    each packet conforming to at least one protocol,


(1.2)    wherein at least one said protocol defines one or more conversational
         flows that each includes a plurality of states of the flow including an initial
         state, and transitions from the initial state to at least one of the plurality of
         states of the flow,


the method comprising:


(2)      receiving a packet (302) from a packet acquisition device;


(3)      performing at least one parsing operation (304) and/or at least one
         extraction operation (306) on the packet


(3.1)    to create a parser record comprising a function (312) of selected portions
         of the packet;

                                          - 21 -


(3.2)    wherein at least one of the parsing and/or extraction operations depend on
         one or more of the protocols to which the packet conforms;


(4)     looking up (314) in a flow-entry database (324) comprising flow entries for
        any previously encountered conversational flows,


(4.1) the look up using at least some of the selected packet portions and


(4.2) determining (316) if the packet is of an existing conversational flow;


(5)     if the packet is of an existing conversational flow,


(5.1) classifying the packet as belonging to the found existing conversational flow
        and


(5.2) performing (328, 330) any state operation or operations specified in a
        database (326) for the state of the conversational flow; and


(6)     if the packet is of a new conversational flow,


(6.1) storing (322) a new flow-entry for the new conversational flow in the flowentry database, including


(6.2) identifying information for future packets to be identified with the new flowentry,


(6.3) determining the state of the flow (318) using the database (326) and


(6.4) performing (328, 330) any state operation or operations specified in the
        database (326) for the state of the flow;


(7)     wherein each conversational flow that includes a plurality of states is
        recognized

                                        - 22 -




(7.1) by transitioning through a plurality of states of the conversational flow, and


(7.2) at each state, carrying out one or more state operations specified in the
       database (326) for the state of the flow.


Der Senat bezieht sich zur Vermeidung von Fehl-Interpretationen auf die Anspruchsformulierung in der Verfahrenssprache Englisch. Zur deutschen Übersetzung siehe die Streitpatentschrift (z. T. missverständlich) und die folgenden Erläuterungen (Abschnitt 6. / 7.).


5.2    Der nebengeordnete, auf einen entsprechend arbeitenden „Paketmonitor“
gerichtete Patentanspruch 41 ist oben im Tatbestand wiedergegeben. Wie die
Parteien ist auch der Senat der Auffassung, dass seine technische Lehre hinsichtlich Neuheit und erfinderischer Tätigkeit nicht anders zu beurteilen ist als beim
Patentanspruch 1.


6.     Mit dem Anspruch 1 unter Schutz gestellt ist sonach ein Verfahren zum Erkennen von Gesprächsflüssen an einem Netzwerk-Knoten (121) durch Untersuchung der vorbeilaufenden Datenpakete, wobei ganz selbstverständlich jedes dieser Pakete in Übereinstimmung mit mindestens einem, i. d. R. mit mehreren (unterschiedliche Schichten betreffenden) Protokollen aufgebaut ist (Merkmale (1),
(1.1)). Zum besseren Verständnis, wie ein Datenpaket für mehrere Protokolle unterschiedlicher Schichten ausgelegt ist, verweist der Senat rein beispielhaft auf
folgende Figur (aus der deutschsprachigen Wikipedia, Stichwort „OSI-Modell“):

                                       - 23 -


D. h. die „Nutzlast“ einer tieferen Schicht ist jeweils entsprechend dem Protokoll
der nächsthöheren Schicht aufgebaut (vgl. auch Druckschrift E2 Figur 3).


Mit dem Merkmal (1.2) sollen der Begriff „Gesprächsfluss“ und die mehreren möglichen Zustände, die ein solcher Fluss durchläuft, verdeutlicht werden (s. u. Abschnitt 7.1 / 7.2).


Jedes empfangene Paket (Merkmal (2)) soll untersucht werden (parsing operation), wobei Teile des Paketes extrahiert werden können, um daraus einen Datensatz als „parser record“ zu erzeugen; dies natürlich abhängig von den Protokollen,
die das Datenpaket verwendet (Merkmale (3), (3.1), (3.2)).


Dann wird überprüft, ob das aktuelle Paket zu einem bereits registrierten Gesprächsfluss gehört. In einer Datenbank für „flow entries“ (324) sind Signaturschlüssel von bisherigen Gesprächsflüssen gespeichert (Merkmal (4)). Teile des
extrahierten „parser record“ werden mit diesen Signaturschlüsseln verglichen (vgl.
Figur 2 und zugehörige Beschreibung). Bei Übereinstimmung kann das Paket dem
bestehenden Gesprächsfluss zugeordnet werden (Merkmale (4.1), (4.2)).


Wenn das aktuelle Paket zu einem bestehenden Gesprächsfluss gehört, wird es
als zu diesem gehörig klassifiziert, und ggf. wird der Zustand innerhalb des Gesprächsflusses bestimmt (s. u. Abschnitt 7.2) und davon abhängig werden vorbestimmte weitere Operationen („any state operation“) durchgeführt, die nötig sind
für die Erkennung des Fortschritts des Gesprächsflusses und die weitere Zuordnung (Merkmale (5), (5.1), (5.2) – zur Datenbank (326) s. u. Abschnitt 7.2).


Für Pakete, die keinem bestehenden Gesprächsfluss zugeordnet werden können,
wird ein neuer Eintrag in der Datenbank für „flow entries“ (324) angelegt, mit einem Signaturschlüssel („identifying information“) ausgehend von dem o.g. „parser
record“, so dass spätere Pakete als diesem neuen Gesprächsfluss zugehörig
identifiziert werden können (Merkmale (6), (6.1), (6.2)). Dann wird auch hier der
Zustand innerhalb des Gesprächsflusses bestimmt (s. u. Abschnitt 7.2) und davon
abhängig werden die vorbestimmten weiteren Operationen („any state operation“)

                                        - 24 -


durchgeführt, wie es die Datenbank (326) vorgibt (Merkmale (6.3), (6.4) – vgl.
Merkmal (5.2)).


Dadurch soll es ermöglicht werden, solche Gesprächsflüsse zu erkennen, bei denen das Protokoll mehrere zu durchlaufende Zustände vorgibt. Erst durch das
Durchlaufen mehrerer Zustände des Gesprächsflusses, unter Abarbeitung der in
der Datenbank (326) vorgegebenen Zustandsoperationen, soll eine Erkennung
möglich werden (Merkmale (7), (7.1), (7.2)).


7.    Einige Begriffe bedürfen einer Erläuterung.


7.1   Gesprächsfluss („conversational flow“) / Verbindungsfluss („connection
      flow“) / disjunkte Teil-Flüsse („disjointed sub-flows“)


Von wesentlicher Bedeutung ist die Frage, was genau der Begriff „Gesprächsfluss“ bezeichnet. Das Ziel der beanspruchten Lehre, „Gesprächsflüsse“ („conversational flows“) zu erkennen, will die Beklagte bei den Hilfsanträgen 1 bis 4
dadurch noch klarstellen, dass ein solcher Gesprächsfluss ausdrücklich „mehr als
eine Verbindung“ („more than one connection“) umfassen soll. Anstelle der „more
than one connection“ beziehen sich die Hilfsanträge 5 bis 9 auf „more than one
disjointed sub-flows“.


7.1.1 Das Streitpatent unterscheidet begrifflich zwischen „Verbindungsfluss“
(„connection flow” – siehe Abs. [0010]: all the packets involved with a single
connection) und „Gesprächsfluss“ („conversational flow“ - Abs. [0010]: the
sequence of packets that are exchanged in any direction as a result of an activity -
for instance, the running of an application on a server as requested by a client…
some conversational flows involve more than one connection, and some even
involve more than one exchange of packets between a client and server). Der
Unterschied soll darin liegen, dass ein Gesprächsfluss eben mehrere unterschiedliche Verbindungen (auf einer niedrigeren Protokoll-Schicht) umfassen kann (vgl.
Abs. [0011] / [0012]).

                                       - 25 -


Beim Vergleich der Argumentationen von den Klägerinnen und der Beklagten ist
erkennbar, dass der Begriff „Gesprächsfluss" ausgehend von der Lehre des
Streitpatents nicht eindeutig zu bestimmen ist. Die Merkmale (1), (1.1) und (1.2)
legen lediglich fest, dass es sich hierbei um eine Datenübertragungs-Verbindung
in einem Computer-Netzwerk für Daten-Pakete handeln soll, basierend auf mindestens einem der bekannten Protokolle. Die einzige weitere im Anspruch getroffene Definition (im Merkmal (1.2)) besteht darin, dass mehrere Gesprächsfluss-Zustände vorgesehen sein sollen mit Übergängen von einem Initialzustand zu
späteren Zuständen – und nur auf solche Gesprächsflüsse bezieht sich die Lehre
der übrigen Merkmale.


7.1.2 Ein sog. „Verbindungsfluss" („connection flow") soll eine einzelne Verbindung auf einer niedrigeren Protokoll-Schicht als der anspruchsgemäße „Gesprächsfluss“ darstellen. In dem Ausführungsbeispiel des Absatzes [0209], das
sich auf TFTP-Verbindungen bezieht, ist die TFTP-Verbindung (Application Layer
= Schicht 7, siehe Entgegenhaltung E2 Figur 2) als „Gesprächsfluss" zu betrachten, der zwei „Verbindungsflüsse" auf UDP-Ebene (Transport Layer = Schicht 4,
siehe Abs. [0077] und E2 Figur 2) umfasst, nämlich den Fluss auf dem Steuerkanal (UDP Port 69) für den Aufbau der TFTP-Verbindung und den Fluss auf dem
dynamisch ausgehandelten Datenkanal („new port“) für den eigentlichen Dateitransfer (siehe die detaillierte Erläuterung in Abs. [0209]). In entsprechender Weise
bestehen FTP-Gesprächsflüsse (ebenfalls Application Layer = Schicht 7) aus zwei
Verbindungsflüssen auf TCP-Ebene (Transport Layer = Schicht 4).


Die beiden Verbindungsflüsse unterscheiden sich durch den verwendeten Port
und sind „aus sich heraus“ nicht als zusammengehörig erkennbar; dies gelingt nur,
wenn bereits bei der ersten Verbindung erkannt wird, dass die Antwort des Servers die Port-Nummer („new port“) für die zugehörige spätere Verbindung enthält,
und wenn diese Port-Nummer vorab registriert wird. Das ist in den Abs. [0223] bis
[0234] des Streitpatents in Verbindung mit Figur 2 erläutert: Der Paketmonitor erkennt ein Paket (206) eines ersten Verbindungsflusses (Steuerkanal) und legt eine
Signatur KEY-1 für diesen an. Durch Analyse des Datenflusses vom ersten Verbindungsfluss auf diesem Steuerkanal wird das Antwortpaket 207 erkannt, wel-

                                       - 26 -


ches die Port-Information für einen weiteren Verbindungsfluss (Datenkanal) enthält. Der Paketmonitor erzeugt eine entsprechende Signatur KEY-2, die ein Erkennungsmuster („recognition pattern" 253) für diesen zukünftigen Verbindungsfluss umfasst. Mittels dieser Signatur KEY-2 kann der streitpatentgemäße Paketmonitor Pakete (207, 209) des neuen Verbindungsflusses (Datenkanal) erkennen
und zuordnen - wobei der erste Verbindungsfluss und der neue Verbindungsfluss
gemeinsam den anspruchsgemäß zu erkennenden „Gesprächsfluss“ darstellen.


7.1.3 Für den bedeutsamen Begriff der Verbindung („connection“) findet sich im
Streitpatent jedoch ebenfalls keine einheitliche Definition, was u.a. damit zusammenhängt, dass die unterschiedlichen Protokolle, die umfasst sein sollen, unterschiedliche Arten der Datenübertragungs-Verbindung beschreiben (vgl. etwa die
Eingabe der Klägerin 1 vom 18.7.2016, Seite 3 / 4). Festzuhalten ist lediglich, dass
die   anspruchsgemäßen      „Verbindungen“      eine   niedrigere   Protokoll-Ebene
bzw. -Schicht betreffen als der zu erkennende Gesprächsfluss.


7.1.4 Gemäß den Hilfsanträgen 5 bis 9 soll ein Gesprächsfluss (anstelle von
„mehr als eine Verbindung“ der Hilfsanträge 1 bis 4) „mehr als einen disjunkten
Teil-Fluss“ („more than one disjointed sub-flows“) umfassen. „Disjointed“ kann statt
als „disjunkt“ auch als „unzusammenhängend“ übersetzt werden.


Der Begriff „disjointed sub-flow“ geht zurück auf Abs. [0111] des Streitpatents und
wird dort in Bezug zu den in Abs. [0204] ff. beschriebenen „server announcement
type flows“ gesetzt, welche auch in Absatz [0111] genannt sind. Durch die weitere
Einschränkung mit dem Anspruchsmerkmal „each sub-flow being a transport layer
connection“ auf Verbindungen der Transportschicht (Layer 4 - insbesondere TCP
oder UDP) wird klargestellt, dass die beanspruchten „disjointed sub flows“ solche
Teil-Verbindungen sind, die über unterschiedliche Ports laufen (und deshalb nicht
ohne weiteres als zu einem einzigen Gesprächsfluss gehörig zu erkennen sind -
siehe Abs. [0111]: „What may seem to prior art monitors to be some unassociated
flow, may be recognized by the inventive monitor using the flow signature to be a
sub-flow associated with a previously encountered sub-flow”).

                                       - 27 -


7.1.5 Anders als die Beklagte meint, wird jedoch eine bestimmte Protokoll-Ebene
für streitpatentgemäße „Gesprächsflüsse“ in der erteilten Anspruchsfassung
(Hauptantrag) nicht festgelegt. In Abs. [0041] (zweiter Punkt) ist ganz deutlich
festgehalten, dass Gesprächsflüsse ("conversational flows") auf allen Protokoll-Ebenen erkannt und klassifiziert werden sollen. Vgl. auch Abs. [0611]: „Applications and protocols, at any level, are recognized through state analysis, of
sequences of packets“. Die Beispiele für Protokoll-Definitionstabellen (Abs. [0485]
bis [0488]) umfassen ein Protokoll der Anwendungsschicht (HTTP in [0488]), aber
auch Protokolle tieferer Schichten (TCP in [0487], IP in [0486]). Den Ausführungen
der Beklagten (siehe z.B. Widerspruchsbegründung vom 16. September 2016,
Seite 55 drittletzter Absatz): „Verbindungen der vierten OSI-Schicht (TCP-Verbindungen) sind jedoch keine Gesprächsflüsse im Sinne des Streitpatents, sondern
Verbindungsflüsse im Sinne des Streitpatents“ kann daher bezüglich des Hauptantrags nicht gefolgt werden.


7.1.6 Auch eine Beschränkung darauf, dass ein Gesprächsfluss mehrere Verbindungen umfassen müsse, lässt sich dem Streitpatent nicht entnehmen (vgl. Absatz [0010]: „some conversational flows involve more than one connection, and
some even involve more than one exchange of packets between a client and server“ – aus dem Begriff „some“ lässt sich hier auch die umgekehrte Aussage folgern: „some conversational flows involve not more than one connection“). Demnach kann auch eine einzige „connection“ in der erteilen Fassung des Streitpatents einen anspruchsgemäßen Gesprächsfluss darstellen.


7.1.7 Ebensowenig verlangt der erteilte Patentanspruch 1 (Hauptantrag), dass
ein Gesprächsfluss mehrere Pakete in beiden Richtungen umfassen müsse. Die
Anspruchsmerkmale selbst beziehen sich nur auf eine Abfolge von Zuständen der
Paket-Übertragung (Merkmale (1.2), (5.2) / (6.4), (7), (7.1), (7.2)). Zur Anzahl der
Pakete ist wieder auf Absatz [0010] des Streitpatents zu verweisen: „some
conversational flows … even involve more than one exchange of packets between
a client and server“ - d. h. es können also auch weniger sein.

                                         - 28 -


7.2      „states of the flow“ (Merkmal (1.2)) / „database (326) for the state of the
         conversational flow” (Merkmale (5.2), (6.3), (6.4), (7.2))


Hier geht es darum, dass ein Gesprächsfluss einem bestimmten Kommunikationsprotokoll unterliegt und diesem entsprechend verschiedene Zustände durchläuft.


Die verschiedenen möglichen Zustände eines Gesprächsflusses nach einem bestimmten Protokoll sind in einer Datenbank (326) hinterlegt, welche gemäß Streitpatent Abs. [0095] umfasst: “… the different states and state transitions that occur
in different conversational flows, and the state operations that need to be performed (e.g., patterns that need to be examined and new signatures that need to be
built) during any state of a conversational flow to further the task of analyzing the
conversational flow” – d. h. einerseits die möglichen Zustände und Zustandsübergänge aller bekannten bzw. zu erkennenden Gesprächsflüsse, und andererseits
die jeweils zugeordneten Zustandsoperationen, die in einem erkannten Zustand
ausgeführt werden müssen (z. B. Überprüfung bestimmter Muster und Verändern
der Signaturschlüssel, siehe Abs. [0108] / [0109], Abs. [0113] ff., Abs. [0230]).


Wenn ein Datenpaket einem schon bekannten Gesprächsfluss zugeordnet werden
kann (Merkmal (5)), wird (implizit: der Zustand bestimmt bzw. ausgelesen, und davon abhängig) die Zustandsoperation durchgeführt, die für diesen Zustand in der
Datenbank vorgesehen ist (Merkmal (5.2)); oder wenn das Datenpaket als zu einem „neuen“ Gesprächsfluss zugehörig eingestuft wird (Merkmal (6)), wird der
momentane Zustand innerhalb des Gesprächsflusses bestimmt (Merkmal (6.3))
und davon ausgehend ebenfalls die entsprechende Zustandsoperation durchgeführt, die für diesen Zustand in der Datenbank vorgesehen ist (Merkmal
(6.4)) - dabei sollen Gesprächsflüsse, die mehrere Zustände umfassen, durch das
Verfolgen über mehrere Zustände hinweg erkannt werden (Merkmalsgruppe 7).

                                       - 29 -


7.3   „application program“ (Hilfsanträge 4, 5, 7, 8 und 9)


Bereits die Beschreibungseinleitung des Streitpatents (Abs. [0001]) bezieht sich
auf die Klassifizierung der Datenpakete „according to … application program“. Der
Ausdruck „application program“ wird gewöhnlich für Anwendungsprogramme verwendet, wie etwa für einen Internet-Browser oder ein Textverarbeitungsprogramm;
dies entspricht aber nicht dem, was das Streitpatent darunter versteht.


In den Erläuterungen zu Figur 2 (Abs. [0223] ff.) ist beschrieben, dass ein Client
bei einem bestimmten Server (z. B. Portmapper) über einen festgelegten Port
(Abs. [0226]: Port 111 für Sun RPC) die Adresse eines gewünschten Dienstes (eines „application service“, siehe Abs. [0220] u. a.) erfragt. Ein solcher Dienst, der
z. B. mittels RPC Bind Lookup Service (a1) bzw. Sun RPC Service (a2 - siehe
Abs. [0229] / [0230]) zugänglich gemacht wird, wird als „application“ bezeichnet.
Vgl. dazu auch Streitpatent Abs. [0003]: „services (i.e., application programs)“. Insofern ist eine Übersetzung als „Anwendungsprogramm“ missverständlich, richtiger wäre „Dienstprogramm“, oder auch im Deutschen der Begriff „Service“.


Eine besondere Bedeutung kommt dem Verfahren des „server announcement“ zu
(Abs. [0204]), bei welchem ein solcher Service den Teilnehmern im Netzwerk in
einem Rundruf („broadcast or multicast“) mitgeteilt werden kann (s. u. zu Hilfsantrag 5). Auch hier formuliert das Streitpatent: „to announce a server and application“ (Abs. [0204]), wobei „application“ den angebotenen Dienst oder Service bezeichnet (vgl. Abs. [0013] „voice, video …“). Bezüglich möglicher Dienste verweist
das Streitpatent auf eine bei der ICANN hinterlegte Zuordnungsliste (Abs. [0214]).


Hierzu haben beide Parteien in der mündlichen Verhandlung für den Senat überzeugend dargelegt, dass ein streitpatentgemäßer „Gesprächsfluss“ auch darunter
zu verstehen ist, wenn in einer ersten Transport Layer-Verbindung die Adresse eines solchen Services erfragt wird, und diese in einer zweiten Transport Layer-Verbindung dann benutzt wird, um den Dienst in Anspruch zu nehmen. Dabei
handelt es sich um zwei Verbindungen mit unterschiedlichen Adressen, die vom
beanspruchten Paketmonitor als zusammengehörig erkannt werden können.

                                          - 30 -


                                           II.


Das Streitpatent erweist sich sowohl in der erteilten Fassung als auch im Umfang
der Hilfsanträge als nicht patentfähig.


1.    Auf die Frage, ob das Streitpatent die Priorität der US-Anmeldung
60 / 141 903 vom 30. Juni 1999 zu Recht in Anspruch nimmt, insbesondere ob
eine rechtswirksame Übertragung des Prioritätsrechts stattgefunden hat, kommt
es nicht an. Denn die im Folgenden entscheidungserheblichen Dokumente sind
vor dem Prioritätstag veröffentlicht worden.


2.    In der erteilten Fassung (Hauptantrag) hat das Streitpatent keinen Bestand, weil der jeweilige Gegenstand der unabhängigen Patentansprüche 1
und 41 am Prioritätstag des Streitpatents nicht mehr neu war.


2.1   Als nächstliegenden Stand der Technik für die erteilte Anspruchsfassung
sieht der Senat die Druckschrift E2 (WO 92 / 19 054 A1 = CONCORD) an, welche
nach fachmännischem Verständnis die Lehre des Patentanspruchs 1 des Streitpatents vorwegnimmt.


Das Dokument E2 betrifft „network monitoring“ und geht vom OSI-Schichtenmodell
aus (Fig. 2 / 3, Fig. 19; Seiten 13 bis 15). Hier wird ein Netzwerk-Monitor 10 beschrieben, welcher über das Netzwerk verschickte Datenpakete auswertet und
Daten über die verschiedenen Netzwerk-Aktivitäten sammelt, und zwar „in Echtzeit“ und für unterschiedliche Protokolle (siehe Zusammenfassung; Seite 3 ff.;
Fig. 20A bis 20F). Dabei werden „communications“ oder „communication dialogs“
erkannt, wobei jede „communication“ bzw. jeder „communication dialog“ nach einem definierten Verbindungsprotokoll abläuft (Seite 3 Zeile 18 bis 27). Unter
„Dialog“ wird eine Kommunikation zwischen einem Sender und einem Empfänger
verstanden, bei dem ein oder mehrere Pakete übermittelt werden; die meisten
Dialoge umfassen einen Austausch in beiden Richtungen (siehe Seite 17 oben).

                                       - 31 -


Ferner geht die Lehre der E2 davon aus, dass eine einzelne Verbindung
(„connection“) als eine Abfolge verschiedener Zustände („states“) verstanden werden kann (siehe Seite 42 Zeile 20 ff. „The State Machine“, insbesondere Zeile 32
bis 34: „one can identify a beginning and an end of the communication, and
usually some sequence of events which will occur during the course of the
communication“). Deshalb werden die einzelnen Zustände eines Dialogs erkannt,
mitverfolgt und gespeichert (Seite 3 Zeile 28 ff.), entsprechend der anspruchsgemäßen Erkennung von Verbindungen durch das Durchlaufen mehrerer Zustände
(Merkmalsgruppe 7). Damit finden sich hier die Merkmale (1), (1.1), (1.2), (2) sowie (7), (7.1) und (7.2) des Anspruchs 1 des Streitpatents wieder, wobei zunächst
noch der Aspekt offenbleibt, ob durch das Durchlaufen mehrerer Zustände „Gesprächsflüsse“ erkannt werden.


Für die Erkennung einer TCP-Verbindung gibt die Druckschrift E2, in Gegenüberstellung mit den Merkmalen des Patentanspruchs 1 des Streitpatents, die folgende
Lehre: Ein „Real Time Parser“ (Seite 38 Zeile 23 ff.) analysiert vorbeilaufende
Datenpakete (Seite 38 Zeile 25 / 26), d. h. er führt eine „parsing operation“ bzw.
eine „extraction operation“ durch (Merkmal (3)) basierend darauf, dass er - im
Sinne der „selected portions“ des Merkmals (3.1) - die zu untersuchenden Bereiche kennt (Seite 39 Zeile 21 / 22). Selbstverständlich hängt dies vom verwendeten
Protokoll ab (Seite 39 Zeile 24 / 25 - Merkmal (3.2)). Die ab Seite 42 Zeile 20 beschriebene Zustandsmaschine kennt die verschiedenen Zustände einer TCP-Verbindung und trifft daraus eine Zuordnung zu bereits erkannten Verbindungen
(siehe Fig. 8 und Seite 43 Zeile 7 bis 13; Zeile 27 ff.: „When the state machine receives a new event…“, u. a. – insbes. Merkmale (4), (4.1), (4.2)). Hier entspricht
die „history table” gemäß Figur 9 der beanspruchten „flow entry database 324”
(Merkmal (4)), und der „event / state table“ gemäß Figur 8 entspricht der beanspruchten „database for the state of the conversational flow 326“ (insbes. Merkmale (5.2), (6.3), (6.4)). Jedes TCP-Paket wird anhand von Sender und Empfänger identifiziert und sein „Zustand“ innerhalb der Verbindung nachverfolgt, ggf. mit
einem Rückblick auf vorherige Zustände (siehe Figur 8 und zugehörige Beschreibung, z. B. „look at history“). Aus diesem beschriebenen Ablauf ergeben sich für
den Fachmann alle Merkmale der Merkmalsgruppen 4, 5 und 6, insbesondere

                                       - 32 -


auch dass im Fall einer vorher noch nicht bestehenden Verbindung neue Einträge
angelegt werden müssen.


Wie einleitend erläutert (s. o. I. 7.1.5), ist der Patentanspruch 1 des Streitpatents
nicht auf bestimmte Protokoll-Ebenen eingeschränkt, vielmehr sollen Gesprächsflüsse auf allen Protokoll-Ebenen erkannt werden. Dem Fachmann war vertraut,
dass eine vollständige TCP-Verbindung aus einer Abfolge von Einzelverbindungen
(in beiden Richtungen, also vom Sender der TCP-Datenanforderung zum Empfänger und zurück) auf einer tieferen Netzwerk-Schicht (z. B. Ethernet) besteht,
wobei etwa die Zustände „Connecting“, „Data“, „Closing“ durchlaufen werden (E2
Figur 8; zum Verständnis einer TCP-Verbindung siehe auch die Entgegenhaltung
E10 Figur 3 und zugehörige Beschreibung). Wenn man daher eine TCP-Verbindung als den anspruchsgemäßen „Gesprächsfluss“ ansieht, dann entsprechen die
einzelnen Ethernet-Übertragungen den „Verbindungsflüssen“ des Streitpatents.
Der Netzwerk-Monitor der E2 ordnet die einzelnen Ethernet-Pakete der übergeordneten TCP-Verbindung zu und nimmt damit die anspruchsgemäße Erkennung
eines (TCP-) Gesprächsflusses basierend auf der Mitverfolgung der Zustandsübergänge vorweg.


2.2   Der dagegen gerichteten Argumentation der Beklagten kann nicht gefolgt
werden.


2.2.1 Der Unterschied zum Patentanspruch 1 des Streitpatents soll nach der
Argumentation der Beklagten vor allem darin liegen, dass E2 „nur“ Dialog-Erkennungen auf niedrigeren Protokoll-Ebenen (insbes. TCP) betreffe, welche nach
Auslegung der Beklagten „Verbindungsflüsse“ seien.


Eine solche einengende Auslegung des Patentanspruchs 1 ist jedoch nicht zulässig (s. o. I. Abschnitt 7.1.5 und BGH GRUR 2004, 47 - Blasenfreie Gummibahn I:
„Dabei darf im Nichtigkeitsverfahren nicht etwa deshalb eine einengende Auslegung der angegriffenen Patentansprüche zugrunde gelegt werden, weil mit dieser
die Schutzfähigkeit eher bejaht werden könnte.“). Zwar können TCP-Verbindungen „Verbindungsflüsse“ eines Gesprächsflusses auf höherer Protokoll-Ebene

                                        - 33 -


sein (z. B. eines TFTP- oder FTP-Gesprächsflusses). Dies schließt aber nicht aus,
eine einzelne TCP-Verbindung selbst als einen „Gesprächsfluss“ im Sinne des
Streitpatents zu verstehen, welcher wiederum aus mehreren Verbindungsflüssen
auf Ethernet-Ebene besteht und auch für sich allein betrachtet eine Abfolge von
Verbindungszuständen aufweist (und dadurch die nicht auf eine bestimmte Protokoll-Ebene beschränkte Lehre des Patentanspruchs 1 vorwegnimmt).


2.2.2 Die Beklagte ist der Auffassung, der Druckschrift E2 sei nicht die Lehre zu
entnehmen, die Datenpakete von TCP-Verbindungsflüssen mit unterschiedlichen
Adressen (s. o. I. 7.1.2: Steuerkanal / Datenkanal) einem übergeordneten gemeinsamen Gesprächsfluss zuzuordnen.


Darauf kommt es beim erteilten Patentanspruch 1 (Hauptantrag) aber nicht an, da
dieser weder die TCP-Schicht für Verbindungsflüsse fordert noch auf die Zuordnung zweier unterschiedlich adressierter Verbindungen gerichtet ist (s.o. I. 7.1.6).


2.2.3 Der von der Beklagten vorgelegten Argumentation des USPTO (Anlage
MFG3 der Beklagten) betreffend MFG5 „Engel“ (welche Druckschrift mit der
Druckschrift E2 weitgehend übereinzustimmen scheint) kommt für den vorliegenden Fall keine Bedeutung zu, u. a. weil sich die unabhängigen Ansprüche des dort
in Streit stehenden Patents MFG4 vom hiesigen Streitpatent unterscheiden. So
sieht die Argumentation des USPTO den Haupt-Unterschied darin, dass „Engel“
nicht die Lehre gebe, einzelne Datenpakete unterschiedlicher Verbindungsflüsse
einer einzelnen Anwendungs-Aktivität zuzuordnen. Eine Zuordnung zu Anwendungs-Aktivitäten ist aber nicht Gegenstand des Anspruchs 1 des hiesigen Streitpatents.


2.3   Der einzige andere unabhängige, auf einen „Paketmonitor“ gerichtete Patentanspruch 41 ist nicht anders zu beurteilen, weil er lediglich die Merkmale des
Verfahrensanspruchs 1 aufgreift (vgl. oben I. 5.2), und auch die Druckschrift E2
einen „Paketmonitor“ beschreibt (Seite 18 Zeile 25: Monitor 10).

                                          - 34 -


2.4       Mit den Patentansprüchen 1 und 41 fällt der gesamte Hauptantrag - in
Übereinstimmung mit der Erklärung der Beklagten, sie verstehe die Ansprüche
nach Haupt- und Hilfsanträgen jeweils als geschlossene Anspruchssätze, die jeweils in ihrer Gesamtheit beansprucht würden.


3.        Auch den Hilfsanträgen bleibt ein Erfolg verwehrt.


3.1       Der Hilfsantrag 1 kann nicht gewährt werden, weil der Gegenstand seines
Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruht.


3.1.1 Der Patentanspruch 1 des Hilfsantrags 1 unterscheidet sich vom Anspruch 1 des Hauptantrags durch das zusätzliche Merkmal (1.x), welches vor dem
Merkmal (1.1) eingefügt wird, und das gegenüber Merkmal (6.3) ergänzte Merkmal
(6.3x):


          (1.x) a conversational flow comprising more than one connection,


          (6.3x) determining the state and protocol of the flow (318) using the
                database (326) and


Damit wird zum einen festgeschrieben, dass ein Gesprächsfluss mehrere Verbindungen umfassen soll, und zum anderen, dass bei Erkennung eines neuen Gesprächsflusses (Merkmal (6)) nicht nur der Zustand, sondern auch das Protokoll
erkannt werden soll.


3.1.2 Die Ergänzung in Merkmal (6.3x), dass auch das Protokoll erkannt werden
soll, betrifft lediglich die klägerseitig geltend gemachte „fehlende Ausführbarkeit“
der Lehre der erteilten Anspruchsfassung. Der Zustand eines Verbindungsflusses
kann nur festgestellt werden, wenn das verwendete Protokoll bekannt ist, denn
erst aus dem verwendeten Protokoll ergibt sich die Bedeutung der einzelnen Datenbits - das ist „trivial“ und für den Fachmann selbstverständlich, und kommt nun
in der Anspruchsfassung des Hilfsantrags 1 auch zum Ausdruck, ohne dass aber

                                      - 35 -


mit dieser Ergänzung die Neuheit oder das Vorliegen einer erfinderischen Tätigkeit
begründet werden könnte.


3.1.3 Es kann dahinstehen, ob das zusätzliche Merkmal (1.x) geeignet ist, die beanspruchte Lehre von der Lehre der Druckschrift E2 zu unterscheiden. Denn die
beanspruchte Lehre lag zumindest ausgehend von der Druckschrift E1 für den
Fachmann nahe.


a)     Wie oben in I. 7.1.3 festgestellt, liefert das Streitpatent für den Begriff
„connection“ keine einheitliche Definition. Daher neigt der Senat zu der Auffassung, dass auch für den Hilfsantrag 1 die einschränkende Auslegung, unterschiedliche „connections“ müssten unterschiedliche Adressen betreffen, nicht gerechtfertigt ist.


b)     Dies kann aber dahinstehen, weil auch eine Erkennung von Gesprächsflüssen, die mehrere Verbindungen zu unterschiedlichen Adressen umfassen, dem
Fachmann jedenfalls durch den Stand der Technik nahegelegt war.


Dem Fachmann war geläufig, dass eine FTP-Kommunikation über eine erste TCP-Verbindung („Steuerkanal“) ausgelöst wird und die zugehörige Nutzdatenübertragung dann über eine zweite TCP-Verbindung („Datenkanal“) erfolgt. D.h. eine übliche FTP-Kommunikation (OSI-Schicht 7) umfasst gewöhnlich zwei TCP-„Verbindungen“ (OSI-Schicht 4), die sich durch die verwendeten Ports unterscheiden (vgl.
oben I 7.1.2). Die Grundidee des Streitpatents besteht darin, dass das beanspruchte Verfahren eine Zuordnung dieser beiden Verbindungen zueinander herstellen soll, d. h. zwei anscheinend unterschiedliche Verbindungen (einer tieferen
Schicht, hier TCP) als zusammengehörend (zu einer einzigen Verbindung der höheren Schicht, hier FTP) erkennt.


Eine solche Zuordnung zweier anscheinend unterschiedlicher TCP-Verbindungen
als zusammengehörig kann der Fachmann jedoch der Druckschrift E1 (PAXSON)
entnehmen.

                                        - 36 -


Die Druckschrift E1 beschreibt einen Echtzeit-Paketmonitor mit dem Ziel, aus der
Beobachtung der einzelnen Pakete Rückschlüsse auf Gesprächsflüsse höherer
Protokoll-Ebenen ziehen zu können (siehe insbesondere Abstract, Figur 1 und
Kapitel 2.1, dort die letzten zwei Absätze „…Thus, by capturing on the order of
only 4 packets (…), we can determine a great deal about a connection“ / „… to
analyze connections at the application level…“). U. a. ist auch die Überwachung
von TCP-Verbindungen anhand der einzelnen Zustände der Verbindung beschrieben (siehe Kapitel 2.2, Abschnitt „TCP processing“).


Der Abschnitt 6 befasst sich mit speziellen „Internet applications“. Im Kapitel 6.2 ist
die Erkennung von FTP-Gesprächsflüssen beschrieben. Im 5. Absatz heißt es:


„A final analysis step for ftp.request events is to parse any PORT request to
extract the hostname and TCP port associated with an upcoming transfer. (The
FTP protocol uses multiple TCP connections, one for the control information such
as user requests, and others, dynamically created, for each data transfer.) This is
an important step, because it enables the script to tell which subsequent
connections belong to this FTP session and which do not.” (Hervorhebung vom
Senat)


D. h. FTP-Datenpakete werden auf das Vorkommen der Zeichenfolge „PORT“
durchsucht, um daraus den TCP-Port für eine zugehörige spätere TCP-Verbindung zu erkennen und deren Zuordnung zum aktuellen Datenfluss („belong to this
FTP session“) zu ermöglichen. Dadurch ist die o. g. Grundidee des Streitpatents
vorweggenommen.


Im konkreten Vergleich mit dem Patentanspruch 1 des Hilfsantrags 1 gibt E1 die
Lehre, Datenpakete an einem Punkt im Netzwerk zu überwachen und FTP-Gesprächsflüsse (welche mehr als eine TCP-Verbindung umfassen) zu erkennen
(Merkmale (1), (1.x) und (2)), wobei jedes Datenpaket mehreren Protokollen (hier
zumindest dem FTP- und dem TCP-Protokoll) entspricht (Merkmal (1.1)), und das
FTP-Protokoll einen Gesprächsfluss definiert, welcher im Sinne des Merkmals
(1.2) eine Abfolge vom Zuständen durchlaufen muss. Dabei werden die einzelnen

                                        - 37 -


Zustände des Gesprächsflusses erkannt, mitverfolgt und gespeichert (vgl.
Kap. 6.2 2. / 3. Absatz „… Bro parses each line … Replies can indicate whether
they continue to … for each line of the reply, the event engine generates …“), so
dass hier eine anspruchsgemäße Erkennung von Gesprächsflüssen durch das
Durchlaufen mehrerer Zustände erfolgt (Merkmale (7), (7.1) und (7.2)).


Die einzelnen Arbeitsschritte nach den anspruchsgemäßen Merkmalsgruppen 3,
4, 5 und 6 sind der E1 nicht unmittelbar zu entnehmen. Der Fachmann kannte
aber derartig arbeitende Paketmonitore beispielsweise aus der Druckschrift E2
(s. o. II. 2.1), und es war daher nicht mehr als übliche handwerkliche Tätigkeit
notwendig, um den Paketmonitor der Druckschrift E2 für die Erkennung von FTP-Gesprächsflüssen anzupassen und so zur Realisierung der Lehre der Druckschrift
E1 einzusetzen. Dies gilt umso mehr, als die Druckschrift E2 die Erkennung von
(Teil-) Verbindungen gemäß FTP-Protokoll bereits konkret beschreibt (siehe E2
Seite 32 Zeile 29, Seite 33 Zeile 3, Seite 40 Zeile 9 / 10, Seite 149 unten / Seite 150 oben).


Damit zeigt das nach dem Vorbild der E2 ergänzte Verfahren der E1 auch die
Merkmale der Merkmalsgruppen 3 bis 6.


c)       Die dagegen gerichtete Argumentation der Beklagten überzeugt den Senat
nicht.


So macht die Beklagte geltend, E1 spreche nicht von einer Zuordnung der FTP-Datenverbindung zum FTP-Steuerkanal, sondern lediglich von „the script keeps
track of pending data transfer connections, and when it encounters them, marks
them as ftp-data applications ...“ (Zitatstelle aus Kapitel 6.2, 5. Absatz). Hier würden also spätere Datenverbindungen nur abstrakt als „ftp-data applications“ gekennzeichnet. Dafür sei es nicht erforderlich, dass sie dem Steuerkanal auch zugeordnet würden, es genüge, wenn die aktuellen FTP-Datenverbindungen festgehalten würden.

                                       - 38 -


Diese Sichtweise greift zu kurz, weil sie sich nur auf einen einzelnen Satz des gesamten Kapitels beschränkt. Wie oben unter b) bereits ausgeführt, geht es in Kapitel 6.2, 5. Absatz, um zukünftige Übertragungen (“upcoming transfer”), und zu
diesem Zweck wird nach der Lehre der E1 der von der Gegenstelle gesendete
TCP-Port extrahiert, um später erkennen zu können, welche nachfolgenden Verbindungen zu dieser FTP-Sitzung gehören („it enables the script to tell which subsequent connections belong to this FTP session“). Die hier genannte „FTP session“ entspricht dem „Gesprächsfluss“, welchen das Streitpatent erkennen will,
und an dieser Stelle spricht die E1 deutlich von Verbindungen, die zu diesem Gesprächsfluss gehören - d. h. die Zusammengehörigkeit soll erkannt werden, nicht
anders als im Streitpatent.


Die Beklagte argumentiert ferner, die „identifying information“ des Merkmals (6.2)
stelle einen komplexen Fingerabdruck der erkannten Verbindung dar, der über
eine simple Speicherung des Ports hinausgehe (vgl. Streitpatent Figur 2, KEY-1
210 und KEY-2 212). Weder E1 noch E2 gäben einen Hinweis, einen solchen
komplexen Fingerabdruck zu verwenden.


Dem ist entgegenzuhalten, dass der Patentanspruch 1 des Hilfsantrags 1 den Begriff „identifying information“ nicht weiter konkretisiert. Auch der in E1 beschriebene Port stellt eine „Identifizierungs-Information“ für spätere Verbindungen dar
und erfüllt damit das Anspruchsmerkmal.


Schließlich wendet die Beklagte noch ein, die Druckschriften E1 und E2 beträfen
völlig unterschiedliche Konzepte zur Paket-Überwachung. Wie die Lehre der E1
durch das, was für den Fachmann aus der E2 entnehmbar ist, realisiert werden
könnte, ließe sich keiner der beiden Druckschriften entnehmen.


Der Senat sieht hier jedoch für den Fachmann, dem die protokollabhängige Überwachung des Netzwerkverkehrs und die Verwendung von Zustandsautomaten bekannt war (s. o. I.4.), keine besondere Schwierigkeit. Entscheidend ist, dass die
E1 dem Fachmann bereits die Anregung gab, unterschiedliche jedoch zusammengehörige TCP-Verbindungen eines FTP-Gesprächsflusses zu erkennen und ein-

                                      - 39 -


ander zuzuordnen. Die Realisierung erforderte dann, etwa ausgehend von dem in
der E2 beschriebenen Beispiel mittels einer Zustands-Verfolgung, vom Fachmann
nur noch handwerkliches Arbeiten.


3.1.4 Mit dem Patentanspruch 1 fällt der gesamte Hilfsantrag 1, in Übereinstimmung mit der Erklärung der Beklagten, sie verstehe die Ansprüche nach Hauptund Hilfsanträgen jeweils als geschlossene Anspruchssätze, die jeweils in ihrer
Gesamtheit beansprucht würden.


3.2   Die Hilfsanträge 2a, 2b, 2c, 2d und 2e bleiben ebenfalls ohne Erfolg, weil
der Gegenstand ihres jeweiligen Patentanspruchs 1 nicht auf einer erfinderischen
Tätigkeit beruht.


3.2.1 Der Patentanspruch 1 der Hilfsanträge 2a bis 2e geht aus vom Patentanspruch 1 nach Hilfsantrag 1, wobei hinter dem zusätzlichen Merkmal (1.x) des
Hilfsantrags 1 jeweils eine der folgenden Ergänzungen eingefügt wird:


      (1.xa) each connection being a transport layer connection, (Hilfsantrag 2a)


      (1.xb) each connection being defined by socket or port numbers,
             (Hilfsantrag 2b)


      (1.xc) each connection being a connection-oriented exchange of packets,
             (Hilfsantrag 2c)


      (1.xd) each connection being defined by a network destination address and
             port, and a network source address and port, (Hilfsantrag 2d)


      (1.xe) each connection being a TCP or UDP connection, (Hilfsantrag 2e)


Die Beklagte hat erklärt, durch diese wahlweisen Einfügungen werde der Begriff
„connection“ weiter differenziert, so dass jedenfalls die verschiedenen Phasen ei-

                                       - 40 -


ner TCP-Verbindung nicht mehr als mehrere „connections“ verstanden werden
könnten.


3.2.2 Die fünf genannten Hilfsanträge sind jedoch nicht günstiger zu beurteilen
als der zugrundeliegende Hilfsantrag 1, weil sich mit keiner der Ergänzungen im
gegebenen Kontext das Vorliegen einer erfinderischen Tätigkeit begründen lässt.


Zwar ist einzuräumen, dass nunmehr die Protokollebene für die Einzelverbindungen (connections) im Patentanspruch 1 auf die Transportschicht (transport layer)
festgelegt ist. Hilfsantrag 2a fordert dies wörtlich. Hilfsantrag 2b bezieht sich auf
die sockets und ports entsprechend dem UDP- bzw. TCP-Protokoll der Transportschicht (vgl. Streitpatent Absatz [0204], [0214]). Hilfsantrag 2c erscheint eher unklar, weil „connection-oriented exchange of packets“ auch nichts anderes aussagt
als „connection“, soll sich aber gemäß den Erläuterungen der Beklagten ebenfalls
auf die Transportschicht beziehen (vgl. Hinweis der Beklagten auf Wikipedia-Artikel in Anlage MFG8). Auch die Netzwerk-Adressen und -Ports des Hilfsantrags 2d
beziehen sich auf Protokolle der Transportschicht. Hilfsantrag 2e schließlich beschränkt sich auf das TCP- und das UDP-Protokoll, welche beide zur Transportschicht gehören. Somit wird mit allen diesen Hilfsanträgen im Grunde das Gleiche
zum Ausdruck gebracht, in etwas unterschiedlicher Anspruchsbreite und mit unterschiedlicher Deutlichkeit. Dadurch fällt die Erkennung einer TCP-Verbindung aus
den einzelnen Verbindungsphasen auf Ethernet-Protokollebene, wie es aus der
Druckschrift E2 als neuheitsschädlich für das erteile Patent zu verstehen war,
nicht mehr unter ein gemäß diesen Hilfsanträgen eingeschränktes Patent.

                                        - 41 -


Die Lehre der Druckschrift E1, welche dem Patentanspruch 1 des Hilfsantrags 1
entgegensteht (in Verbindung mit dem aus der Druckschrift E2 bekannten „Handwerkszeug“, s. o. II. 3.1.3 b)), bezieht sich aber an den zitierten Stellen auf die Erkennung eines FTP-Gesprächsflusses aus unterschiedlichen TCP-Verbindungen
und nimmt dadurch auch die zusätzlichen Merkmale der Hilfsanträge 2a bis 2e
vorweg. So ergeben sich die jeweiligen Merkmale (1.xa), (1.xb) und (1.xe) aus
dem Kapitel 6.2 der E1, 5. Absatz („…to extract the hostname and TCP port …
FTP protocol uses multiple TCP connections”). Eine „verbindungsorientierte“ Datenübertragung gemäß Merkmal (1.xc) ergibt sich in der E1 schon aus der Verwendung von TCP-Verbindungen, bei welchen als erster Schritt jeweils eine „Verbindung“ zwischen zwei Kommunikationsstellen aufgebaut wird; ebenso ist die
Definition einer solchen Verbindung gemäß Merkmal (1.xd) typisch für das TCP-Protokoll (siehe Anlage MFG17, Seite 2). Diese Hilfsanträge können daher nicht
anders als der Hilfsantrag 1 beurteilt werden.


3.2.3 Mit dem jeweiligen Patentanspruch 1 fällt jeweils der gesamte Hilfsantrag
(vgl. oben II. 3.1.4).


3.3    Auch der Hilfsantrag 3 kann keinen Erfolg haben, weil der Gegenstand seines Patentanspruchs 1 nicht günstiger als der Patentanspruch 1 des Hilfsantrags 1 beurteilt werden kann.


3.3.1 Der Patentanspruch 1 des Hilfsantrags 3 geht aus vom Patentanspruch 1
nach einem der Hilfsanträge 2a bis 2e (siehe Eingabe der Beklagten vom
8. Januar 2018, S. 17), wobei vor dem zusätzlichen Merkmal (1.x) des Hilfsantrags 1 das untenstehende Merkmal (1.y) eingefügt wird, das Merkmal (7.2) die
untenstehende Fassung (7.2x) erhält, und am Ende die Merkmale (7.3) und (7.4)
hinzugefügt werden:

                                        - 42 -


       (1.y) in real time,


       (7.2x) at each state of a particular conversational flow, carrying out one or
              more state operations specified in the database (326) for the state of
              the flow,


       (7.3) the carrying out of the state operations furthering the process of
              identifying the application content of the particular conversational
              ﬂow,


       (7.4) and the state operations that involve a state transition to a next state
              comprising building new identification information for recognition of
              packets of the next state of the particular conversational flow.


Damit soll nach den Ausführungen der Beklagten das Patentbegehren noch weiter
klargestellt und an die Lehre der Figur 2 des Streitpatents angepasst werden.


3.3.2 Dieser Patentanspruch 1 nach Hilfsantrag 3 soll wahlweise eine der Ergänzungen aus den Hilfsanträgen 2a bis 2e umfassen. Wie oben dargestellt, haben
die unterschiedlichen Formulierungen des jeweils einzufügenden Merkmals ((1.xa)
bis (1.xe)) jedoch in technischer Hinsicht im Wesentlichen die gleiche Bedeutung
und ergeben sich aus der Lehre der Druckschrift E1, so dass die Maßnahmen im
gegebenen Zusammenhang keine Besonderheit darstellen.


3.3.3 Auch das Merkmal (1.y), dass das beanspruchte Verfahren „in Echtzeit“ ablaufen soll, geht nicht über die Lehre der Druckschrift E1 hinaus (vgl. E1 Seite 1
Abstract Zeile 2).


3.3.4 Die Ergänzung „of a particular conversational flow” in Merkmal (7.2x) hat lediglich eine rein sprachliche, klarstellende Funktion.


3.3.5 Gemäß dem neuen Merkmal (7.3) soll das Ausführen der Zustandsoperationen (in der Zustandsmaschine) den Prozess zur Erkennung des der Einzelverbin-

                                        - 43 -


dung zugrundeliegenden Dienstes (vgl. oben I. 7.3 „application“) „fördern“ oder
„unterstützen“ (vgl. Streitpatent Absatz [0035]).


Dass etwa aus der Verwendung bestimmter Ports auf bestimmte Netzwerk-Dienste geschlossen werden kann, gehörte zum Grundwissen des Durchschnittsfachmanns (vgl. E1 Kapitel 2.1, Kapitel 6.2 5. Absatz „PORT“, Kapitel 6.3). Wie
bereits beschrieben, ist sowohl der E1 (Kapitel 2.1, Kapitel 6.2 2. und 3. Absatz)
als auch der E2 (Figur 8 und zugehörige Beschreibung) zu entnehmen, dass man
durch ein Mit-Verfolgen der Verbindungs-Zustände Rückschlüsse auf den zugrundeliegenden Dienst ziehen kann.


Wenn dadurch nun anspruchsgemäß dieser Erkennungs-Prozess „gefördert“ werden soll, dann stellt das nicht mehr als eine unscharfe Zweckangabe dar, die der
Fachmann im gegebenen Zusammenhang sowieso erwartet hätte. Etwas „Neues“
oder „Erfinderisches“ kann darin nicht gesehen werden.


3.3.6 Gemäß dem zusätzlichen Merkmal (7.4) sollen Zustandsoperationen, bei
welchen ein Übergang zu einem nächsten Zustand erfolgt, eine neue Identifizierungs-Information („identification information“) zur Erkennung von Paketen des
nächsten Zustands des jeweiligen Gesprächsflusses erzeugen. Siehe dazu Streitpatent Abs. [0110], Abs. [0230] (jeweils bezüglich „signature“ anstelle von „identification information“).


a)     Hier ist zunächst festzuhalten, dass der verwendete Ausdruck „identification
information“, im Widerspruch zur Argumentation der Beklagten (siehe Eingabe
vom 8. Januar 2018, Seite 22), im übrigen Patentanspruch nicht vorkommt. In
Übereinstimmung mit der dortigen Argumentation der Beklagten versteht der Senat den Ausdruck als „identifying information“ wie im Merkmal (6.2).


b)     Das zusätzliche Merkmal (7.4) beinhaltet verschiedene Aspekte, ohne dass
aber in diesen eine erfinderische Tätigkeit erkennbar wäre.

                                         - 44 -


Zum einen soll beim Übergang zu einem neuen Zustand eines Gesprächsflusses
von der Zustandsmaschine eine neue Identifizierungs-Information für den nächsten Zustand erzeugt werden. Dem Fachmann war in diesem Kontext geläufig,
dass bei einem Gesprächsfluss, welcher mehrere Verbindungsflüsse umfasst, innerhalb jedes dieser Verbindungsflüsse mehrere Zustände durchlaufen werden
müssen (siehe z. B. Streitpatent Figur 2: im 1. Verbindungsfluss die Anforderung 206 und die Antwort 207, im 2. Verbindungsfluss die Anforderung 208 und
die Antwort 209). Eine Zustandsoperation, welche z. B. die Anforderung 208 erkennt, benötigt keine neue Identifizierungs-Information zur Erkennung der Antwort 209 außer dem Wissen über das Fortschreiten des jeweiligen Flusses, d. h.
nach Beendigung des Zustands „Verbindung 208 mit Signatur KEY-2“ schaltet die
Zustandsmaschine weiter auf „Erkenne Beginn von Folgeverbindung 209 mit gleicher Signatur KEY-2“. Die Information über das Weiterschalten kann man abstrakt
als die merkmalsgemäße „neue Identifizierungs-Information für den nächsten Zustand“ verstehen, aber dieser Schritt ist für Zustandsmaschinen selbstverständlich
und stellt keinerlei Besonderheit dar.


Zum anderen soll am Ende des 1. Verbindungsflusses (gekennzeichnet durch
KEY-1) eine Identifizierungs-Information (KEY-2) zur Erkennung von Paketen des
später folgenden 2. Verbindungsflusses erzeugt werden. Gemäß den Erläuterungen zu Figur 2 des Streitpatents (Abs. [0223] bis [0234]) soll insbesondere die zukünftige Adresse in dieser Signatur enthalten sein.


Eine solche Lehre lässt sich aber bereits aus der Druckschrift E1 ableiten. Wie
schon erläutert, ist in E1 Kapitel 6.2 5. Absatz das Durchsuchen von FTP-Datenpaketen auf das Vorkommen der Zeichenfolge „PORT“ beschrieben, um ggf. den
TCP-Port für eine zugehörige neue TCP-Verbindung zu erkennen und davon ausgehend die Zuordnung zum aktuellen Datenfluss zu ermöglichen. Der Beklagten
ist zuzustimmen, dass E1 nicht ausdrücklich das Erzeugen einer Identifizierungs-Information „im Voraus“ beschreibt. Der anhand der Zeichenfolge „PORT“ erkannte zukünftige Port stellt jedoch in Verbindung mit den genannten Adressen eine
merkmalsgemäße Identifizierungs-Information dar, und auch wenn E1 nicht eine
detaillierte Anweisung dafür gibt, liegt ein Vorab-Speichern von derart wichtigen

                                         - 45 -


Daten für den mit Datenverarbeitung vertrauten Fachmann auf der Hand. Die Formulierung der E1 „to extract the hostname and TCP port“ umfasst zumindest eine
Zwischenspeicherung, und es ist keine vernünftige Alternative erkennbar, was
sonst mit dieser die 1. und die spätere 2. TCP-Übertragungen verknüpfenden Information geschehen sollte, als sie gerade zum Zweck der späteren Identifizierung
des 2. Verbindungsflusses abzuspeichern.


Sonach lässt sich mit dem Merkmal (7.4), auch in Verbindung mit den übrigen
Merkmalen, das Vorliegen einer erfinderischen Tätigkeit nicht begründen.


3.3.7 Mit dem Patentanspruch 1 fällt der gesamte Hilfsantrag 3 (vgl. oben
II. 3.1.4).


3.4     Der Hilfsantrag 4 kann nicht anders beurteilt werden.


3.4.1 Der Patentanspruch 1 des Hilfsantrags 4 geht wiederum aus vom Patentanspruch 1 nach den Hilfsanträgen 2a bis 2e (siehe Eingabe der Beklagten vom
8. Januar 2018, S. 17), wobei nach Merkmal (5.1) das untenstehende Merkmal
(5.1x) eingefügt wird, das Merkmal (5.2) die untenstehende Fassung (5.2x) und
das Merkmal (6.4) die untenstehende Fassung (6.4x) erhält (Unterschiede gekennzeichnet), und am Ende die Merkmale (7.5) und (7.6) hinzugefügt werden:


        (5.1x) obtaining the last encountered state of the flow and


        (5.2x) performing (328, 330) any state operation or operations specified in a
              database (326) for the state of the conversational flow starting from
              the last encountered state of the flow;


        (6.4x) performing (328, 330) any state operation or operations specified in
              the database (326) for the initial state of the flow;

                                         - 46 -


         (7.5) and wherein the state operations for the states of the flow include updating the flow-entry, including storing identifying information for future packets to be identified with the flow-entry,


         (7.6) and wherein the state processing of each received packet of a flow
               furthers the identifying of the application program of the flow.


3.4.2 Mit dem zusätzlichen Merkmal (5.1x) und den Änderungen in den Merkmalen (5.2x) und (6.4x) wird der Kritik der Klägerinnen zur Frage der ursprünglichen
Offenbarung begegnet, dass der zugrundeliegende ursprüngliche Unteranspruch 23 vom „letzten gespeicherten Zustand“ ausging, und dass bei einem neu
erkannten Gesprächsfluss nicht von einem gespeicherten Zustand ausgegangen
werden kann, sondern eine neue Zustandsabfolge mit einem Anfangszustand beginnt.


Insoweit handelt es sich letztlich um Klarstellungen, die die Ablauf-Logik der Verfahrensschritte betreffen, aber nicht irgendwelche neuen oder gar überraschenden
Erkenntnisse beinhalten. Das Vorliegen einer erfinderischen Tätigkeit lässt sich
mit diesen drei Merkmalen nicht begründen.


3.4.3 Auch die Maßnahmen nach den zusätzlichen Merkmalen (7.5) und (7.6) erlauben nicht die Beurteilung, dass der Patentanspruch 1 gemäß Hilfsantrag 4 auf
einer erfinderischen Tätigkeit beruhen könnte.


In der Druckschrift E2 ist die Erkennung eines TCP-Gesprächsflusses anhand der
Zustände einer „State Machine“ insbesondere ab Seite 42 Zeile 20 beschrieben
(„the state machine determines and keeps state for both addresses of all TCP
connections“; S. 43 Z. 11 „For each address of the two parties to the communication, the state machine determines what the current state of the node is. The code
within the state machine determines the state of a connection based upon a set of
rules…”). Die Tabelle in Figur 8 zeigt Übergänge in andere Zustände abhängig
von einem erkannten „Event” (siehe z. B. „State: Unknown“ und „Event: Connect
Req“ -> neuer State „Connecting“), d. h. hier findet ein Update der Flow Entries

                                         - 47 -


statt (Teil von Merkmal (7.5)). Im Falle eines „Data ACK“ soll eine Suche nach
Verbindungen mit „Data State“ erfolgen; dazu ist auf Seite 47 Zeile 3 ff. ausgeführt: „Look_for_Data_state routine 230 searches back through the history one
record at a time … Routine 230 detects the existence of DATA state by determining whether node 1 and node 2 each have had at least two data events or … then
it calls a Look_for_Initiator routine to look for the initiator of the connection” – d.h.
die “history data structure” enthält Informationen über vorangegangene Zustände
zur Identifikation zukünftiger Pakete. Somit wurden „Identifizierungs-Informationen
für zukünftige Pakete“ in Verbindung mit einem Fluss-Eintrag gespeichert (zweiter
Teil von Merkmal (7.5)). Durch das „state processing” jedes einzelnen Paketes
eines Flusses wird, Schritt für Schritt, der Fluss identifiziert (S. 42 Z. 31: „at the
very least, one can identify a beginning and an end of the communication, and
usually some sequence of events which will occur during the course of the
communication“), was natürlich die Erkennung einer Applikation „fördert“ (Merkmal
(7.6)).


Zwar beziehen sich die genannten Fundstellen auf die Erkennung eines TCP-Gesprächsflusses. Sie zeigen aber, dass dem Fachmann das „Handwerkszeug“ zur
Erkennung von zusammenhängenden Datenflüssen bekannt war. Es war naheliegend, dieses auch zur Erkennung von FTP-Gesprächsflüssen einzusetzen, wie es
sich aus der Druckschrift E1 ergibt - zumal dafür keine größeren Änderungen im
Ablauf erforderlich waren (lediglich eine Anpassung an das andere Protokoll).


3.4.4 Mit dem Patentanspruch 1 fällt der gesamte Hilfsantrag 4 (vgl. oben
II. 3.1.4).


3.5       Auch der Hilfsantrag 5 ist nicht gewährbar, weil der Gegenstand seines Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruht.


3.5.1 Für den Patentanspruch 1 des Hilfsantrags 5 sollen gegenüber dem Anspruch 1 des Hilfsantrags 4 die Merkmale (1.x), (1.xa) und (7.6) die folgende
Fassung (Merkmale (1.xx), (1.xax) und (7.6x), Unterschiede gekennzeichnet) erhalten:

                                       - 48 -


       (1.xx) a conversational flow comprising more than one connection
             disjointed sub-flows,


       (1.xax) each connection sub-flow being a transport layer connection,


       (7.6x) and wherein the state processing of each received packet of a flow
             furthers the identifying of the application program of the flow
             recognizes an application program from one or more disjointed subflows that occur in server announcement type flows.


3.5.2 Zum Verständnis der geänderten Merkmale


a)     Zunächst einmal wird der unklare Begriff „connection“ mittels der Merkmale
(1.xx) und (1.xax) zu „(disjointed) sub-flow“ geändert, noch mit dem Zusatz, dass
die beanspruchten Sub-Flows Verbindungen auf „transport layer“-Ebene (OSI
Schicht 4) darstellen.


Damit erfolgt eine Beschränkung (gegenüber der erteilten Anspruchsfassung) auf
die Erkennung von Gesprächsflüssen durch die Verknüpfung zweier unterschiedlicher („disjointed“) Verbindungen („sub-flows“) auf der Transport Layer Ebene
(OSI-Schicht 4), d. h. die Gesprächsflüsse müssen den darüberliegenden Ebenen
(auf den OSI-Schichten 5, 6 oder 7) zugeordnet sein.


Dabei stellen die beanspruchten „transport layer connections“ jeweils komplette
(insbesondere TCP- oder UDP-) Verbindungen dar, die dann als „disjointed“ zu
verstehen sind, wenn sie unterschiedliche Adressen (insbesondere Ports) betreffen.


Bezogen auf Figur 2 des Streitpatents, stellen nach der Erläuterung der Beklagten
die Verbindungen 206 / 207 einerseits und 208 / 209 andererseits jeweils einen
„sub flow“ dar, wobei die Ports sich unterscheiden (siehe Streitpatent Abs. [0225],
[0232]), so dass es sich um „disjointed sub flows“ handelt.

                                      - 49 -


Insoweit unterscheidet sich das Verständnis nicht vom vorherigen Verständnis der
Merkmale der Merkmalsgruppe (1) nach den Hilfsanträgen 1 bis 4, lediglich die
Merkmals-Formulierung ist eine andere.


b)    Eine zweite Einschränkung gegenüber der erteilten Fassung liegt in der Anspruchsbeschränkung auf „server announcement type flows“ (Merkmal (7.6x)).


Das „server announcement“-Verfahren ist im Streitpatent in den Absätzen [0204],
[0211] und [0217] näher beschrieben. Dabei ist vorgesehen, dass ein Server für
alle Geräte im Netzwerk („broadcast“) oder für bestimmte Geräte („multicast“) ankündigt, auf welchem Port er welchen Service („application“) anbietet. (Siehe noch
den Hinweis in Abs. [0214]: „Each port Mapper … can present the mappings between a unique program number and a specific transport socket through the use of
specific request or a directed announcement”.)


Es gibt bei diesem Verfahren also zwei Verbindungsflüsse (die Ankündigung durch
den Server, und die eventuelle Nutzung der Services durch einen Client unter
Verwendung der angekündigten Ports), welche als „disjointed sub-flows“ auf TCP-Ebene denselben Gesprächsfluss betreffen und deshalb vom beanspruchten Paketmonitor als zusammengehörig erkannt werden sollen.


Dabei könnte die Lehre des Streitpatents so verstanden werden, dass „Server
Announcement“ und „Port Mapper“ zwei unterschiedliche Verfahren beschreiben,
nämlich im Fall des „Server Announcements“ eine einseitige Ankündigung durch
den Server (Figur 2: Anfrage 206 fehlt), im Fall des „Port Mappers“ jedoch eine
Anfrage (206) des Clients und erst darauf folgend eine Antwort (207) des Port
Mapper Servers gemäß Figur 2.


Der Senat hat sich hier von der Darlegung beider Parteien überzeugen lassen,
dass ein solches Verständnis zu eng sei. Schon die Formulierung in Absatz [0211]
„A typical server announcement message is sent to one or more clients…” / „the
announcement is sent to one or more stations” mache deutlich, dass auch die

                                      - 50 -


Antwort des Portmappers auf eine Client-Anfrage als „Server Announcement” verstanden werden könnte.


Somit wird der Anspruch 1 des Hilfsantrags 5 durch das Merkmal (7.6x) nicht auf
eine einseitige 1. Verbindung, die sich von der Darstellung der Figur 2 unterscheiden würde, eingeschränkt. Vielmehr umfasst das Merkmal auch Port Mapper-Datenverkehr, bei welchem der Portmapper in Antwort auf eine Anfrage einen Application-Service bekanntgibt (wie in den Absätzen [0211] bis [0217] beschrieben).


3.5.3 Die so verstandene Lehre lag für den Fachmann jedoch nahe.


Die Merkmale (1.xx) und (1.xax), die letztlich dasselbe wie die Merkmale (1.x) und
(1.xa) … (1.xe) in den höherrangigen Hilfsanträgen nur mit anderen Worten zum
Ausdruck bringen, rechtfertigen keine geänderte Beurteilung.


Ausgehend von der als „naheliegend“ beurteilten Lehre des Anspruchs 1 gemäß
Hilfsantrag 4, unterscheidet sich die mit Hilfsantrag 5 beanspruchte Lehre vor allem durch die Beschränkung auf eine Erkennung von „application programs“ (s. o.
I. 7.3: Dienste, Services), wobei deren Programmnummern mit den zugehörigen
TCP-Portnummern etwa in einer Tabelle eines Port Mappers gespeichert sind und
auf Anfrage oder durch Broadcast bekanntgegeben werden können.


Dieser Unterschied geht nicht über das hinaus, was der Fachmann der Druckschrift E1 entnehmen konnte. Denn ein Portmapper-Service ist in E1 Kapitel 6.3
bereits beschrieben („when clients want access to the service, they first contact
the Portmapper, and it tells them which port they should then contact in order to
reach the service”). Weiter ist dort entnehmbar, dass durch eine Überwachung des
Portmapper-Datenverkehrs auch eine Identifizierung von Verbindungen, die aufgrund der Antwort des Portmappers aufgebaut werden, als zu einem Application
Service gehörig möglich ist („by monitoring Portmapper trafﬁc, we can detect any
attempted access to a number of sensitive RPC services“). Damit geht auch das
Merkmal (7.6x) aus der Druckschrift E1 hervor.

                                      - 51 -


3.5.4 Die Beklagte macht geltend, dem Absatz 6.3 der E1 sei nicht zu entnehmen, dass die Verbindungen zu den Application Services ebenso wie die Portmapper-Verbindungen überwacht würden, insbesondere nicht, dass jedes dieser
Pakete in der beanspruchten Weise mittels der State Machine mitgeführt werde.


Dem kann nur sehr eingeschränkt gefolgt werden.


Zwar ist zuzustimmen, dass die E1 keine solchen Maßnahmen im Detail beschreibt. Für das hingegen beschriebene Erkennen von Zugriffen auf die genannten Dienste („we can detect any attempted access to a number of sensitive RPC
services“) genügt es nach dem Verständnis des Senats nicht, allein den Portmapper-Verkehr zu überwachen; denn dieser zeigt lediglich die Anfragen von potentiellen Angreifern, auf welchem Port ein Service gefunden werden kann, aber nicht
einen konkreten Zugriff (Angriff) auf die Dienste. Dem mitdenkenden Fachmann ist
klar, dass aus der Überwachung des Portmapper-Zugriffs die Adresse eines möglichen Angreifers entnehmbar ist, so dass ein späterer konkreter Angriff auf einen
Dienst anhand der vorhergehenden Portmapper-Anfrage identifiziert werden kann.
Dies setzt aber die weitere Überwachung der vom Portmapper übermittelten
Dienst-Adressen in bekannter Weise (Zustandsmaschine) voraus. Deshalb war
eine anschließende Überwachung dieser Service-Adressen für den Fachmann,
ausgehend von der Lehre der E1, naheliegend.


3.5.5 Mit dem Patentanspruch 1 fällt der gesamte Hilfsantrag 5 (vgl. oben
II. 3.1.4).


3.6     Auch die Hilfsanträge 6 und 7 sind nicht gewährbar, weil der Gegenstand
ihres jeweiligen Patentanspruchs 1 für den hier zuständigen Fachmann nahelag.


3.6.1 Der Patentanspruch 1 gemäß Hilfsantrag 6 weist gegenüber dem Patentanspruch 1 des Hilfsantrags 4 folgende Änderungen und ein neues Merkmal auf:


        (1.xx) a conversational flow comprising more than one connection
              disjointed sub-flows,

                                      - 52 -


      (1.xax) each connection sub-flow being a transport layer connection,


      (5.3) wherein the state operations for the states of the flow include, if the
             packet is related to a first disjointed sub-flow (206, 207) of the
             existing conversational flow and if the packet includes identifying
             information (224 - 233) related to a second sub-flow (208, 209) of the
             existing conversational flow, building a new flow signature (KEY-2)
             for the second sub-flow (208, 209) of the existing conversational flow
             from the identifying information (224 - 233) contained in the packet
             and storing the new flow signature (KEY-2) in the flow-entry
             database (324);


D. h. gegenüber dem Hilfsantrag 5 sind die Merkmale (7.5) und (7.6x) wieder gestrichen (keine Beschränkung auf „Server Announcements“), statt dessen ist nach
Merkmal (5.2x) ein neues Merkmal (5.3) eingefügt, welches nach den Angaben
der Beklagten auf das Ausführungsbeispiel der Figuren 2 und 9 sowie die Absätze [0219] und [0230] des Streitpatents zurückgehen soll.


Hilfsantrag 7 basiert auf diesem Hilfsantrag 6, der Patentanspruch 1 des Hilfsantrags 7 soll nach Merkmal (5.3) noch das folgende zusätzliche Merkmal enthalten:


      (5.4) the identifying information (224 - 233) related to the second sub-flow
             (208, 209) comprising information (s1a) identifying an application
             service requested by a client (202) from a server (204) and the new
             flow signature (KEY-2) comprising information (a2) identifying the
             application service requested by the client (202) from the server
             (204);


Auch dieses Merkmal soll auf das Ausführungsbeispiel der Figuren 2 und 9 sowie
die Absätze [0219] und [0230] des Streitpatents zurückgehen.


3.6.2 Für die Merkmale (1.xx) und (1.xax) gilt unverändert das dazu beim
Hilfsantrag 5 Festgestellte (s.o. 3.5.2 a), 3.5.3), insbesondere dass sich das Ver-

                                       - 53 -


ständnis nicht vom vorherigen Verständnis der Merkmale der Merkmalsgruppe (1)
nach den Hilfsanträgen 1 bis 4 unterscheidet, und die Beurteilung ebensowenig.


3.6.3 Auch die Maßnahmen gemäß den beiden zusätzlichen Merkmalen (5.3)
und (5.4) können das Vorliegen einer erfinderischen Tätigkeit nicht begründen.


a)      Mit dem Merkmal (5.3) soll die Arbeitsweise der Zustandsmaschine
detaillierter beschrieben werden, und zwar, welche konkreten Arbeitsschritte
vorgesehen sind, um einen 2. Teil-Fluss als zugehörig zu einem 1. Teil-Fluss zu
identifizieren.


Hierzu wird beansprucht: Wenn das gerade zu bearbeitende Paket zu einem ersten selbständigen Teil-Fluss eines Gesprächsflusses gehört und Information zur
Identifizierung eines zweiten selbständigen Teil-Flusses enthält (wie es etwa der
Fall ist, wenn ein Portmapper in seiner Antwort auf eine Anfrage die Adresse und
Portnummer des erfragten Dienstes zurückschickt), dann soll aus der Identifizierungs-Information eine neue Signatur „KEY-2“ für den zweiten Teil-Fluss generiert
und in der Datenbank für „flow-entries“ 324 gespeichert werden (wobei diese
Schritte in Form von Zustandsoperationen der Zustandsmaschine bearbeitet werden).


Das dieses noch weiter ergänzende Merkmal (5.4) des Hilfsantrags 7 ist darauf
gerichtet, dass die Identifizierungs-Information für den zweiten Teil-Fluss eine Information (s1a) enthält, welche einen angeforderten Service („application service“,
s. o. I. 7.3) kennzeichnet („identifying an requested application service by a client
(202) from a server (204)“); und dass die neu zu generierende Signatur „KEY-2“
ein Feld (a2) zur Identifizierung dieses Services umfasst.


b)      Der Beklagten ist zuzustimmen, dass weder die Druckschrift E1 noch die
Druckschrift E2 diese Maßnahmen konkret vorwegnimmt. Die Merkmale beschreiben aber nur das, was der Fachmann üblicherweise und ganz selbstverständlich
unternehmen würde, um die in E1 beschriebene Zuordnung zweier scheinbar

                                        - 54 -


selbständiger Teilflüsse (s. o. 3.1.3 b)) durch eine Zustandsmaschine, wie sie die
E2 vorschlägt, zu realisieren.


Hierzu ist zunächst darauf hinzuweisen, dass die in Figur 2 des Streitpatents beschriebenen Datenflüsse 206 bis 209 nicht die Erfindung darstellen, sondern den
Ablauf der einzelnen Teil-Flüsse und den Aufbau der Datenpakete, wie sie dem
verwendeten Protokoll entsprechen und dem Fachmann vertraut sind. Dazu gehört etwa, dass in der Server-Antwort 207 Informationen über den angefragten
Service enthalten sind (Streitpatent Absatz [0228]), die es dem anfragenden Client
ermöglichen, den Service zu nutzen, die es aber auch dem überwachenden Paketmonitor ermöglichen, im Voraus Informationen über einen zu erwartenden
zweiten Teil-Fluss zu entnehmen (zu Feld 230 „s1a“ siehe Absatz [0224]). Dieses
alles ist Stand der Technik.


Das Merkmal (5.3) fordert daher nichts anderes als das beim Hilfsantrag 3 beschriebene Merkmal (7.4) (s. o. 3.3.6 b)), nur jetzt mit einer genaueren, richtigeren
Auswahlbedingung (nicht bei jedem Zustandsübergang, sondern nur bei Antwort-Paketen des ersten Teil-Flusses, welche die benötigte Information enthalten) und
mit der etwas spezielleren Bezeichnung „Fluss-Signatur (KEY-2)“ anstelle von
„buildung new identification information“. An der Beurteilung, dass dafür keine erfinderische Tätigkeit erforderlich ist, ändert das nichts - eine weitere Detaillierung
durch die Benennung spezieller (dem Fachmann aber bekannter) Felder und die
Schaffung einer „Signatur“ betreffen nur das handwerkliche Arbeiten des Fachmanns, der aufgrund seiner fachlichen Ausbildung bereits weiß, wie und woran die
hier wichtigen Felder erkennbar sind und wie er die Datenfelder aufbauen muss,
damit ein Vergleich möglich wird.


Dies gilt genauso für das Merkmal (5.4) des Hilfsantrags 7, welches lediglich auf
ein bekanntes Feld (s1a) verweist und die für den Fachmann selbstverständliche
Feststellung trifft, dessen Information - nicht unbedingt unverändert, sondern im
Form eines Feldes (a2) - zur Identifizierung des Services in die neue Signatur
KEY-2 aufzunehmen. Eine solche Maßnahme geht, im Vergleich mit dem Merkmal
(7.4) des Hilfsantrags 3, nicht über rein handwerkliches Arbeiten des Durch-

                                            - 55 -


schnittsfachmanns hinaus (vgl. dazu - beispielhaft - den Aufbau des Datensatzes
RPC_okay in der Druckschrift E1 Abschnitt 3.2 (rechte Spalte Mitte)).


Der Patentanspruch 1 in der Fassung des Hilfsantrags 6 wie auch in der Fassung
des Hilfsantrags 7 kann daher nicht günstiger als der Patentanspruch 1 des Hilfsantrags 3 beurteilt werden.


3.6.4 Mit dem jeweiligen Patentanspruch 1 fällt jeweils der gesamte Hilfsantrag 6
bzw. Hilfsantrag 7 (vgl. oben II. 3.1.4).


3.7     Der Hilfsantrag 8 ist ebenfalls nicht gewährbar, weil der Gegenstand seines
Patentanspruchs 1 - bei Berücksichtigung nur derjenigen Merkmale, die zu einer
technischen Problemlösung beitragen - nicht auf einer erfinderischen Tätigkeit beruht.


3.7.1 Entgegen dem Vortrag der Klägerinnen ist der (im Übrigen nicht erfolgreiche) Hilfsantrag 8 nicht gem. § 83 Abs. 4 PatG als verspätet zurückzuweisen.
Denn er ist vor Ablauf der vom Senat im 2. Hinweis gesetzten Frist (28. Mai 2018)
eingegangen, und die Klägerinnen hatten außerdem genügend Zeit, hierzu Stellung zu nehmen, was sie auch getan haben.


3.7.2 Der Patentanspruch 1 gemäß Hilfsantrag 8 lautet, mit einer Gliederung ausgehend von der bisherigen Gliederung:


(1)     A method of recognizing one or more conversational flows for packets
        passing through a connection point (121) on a computer network (102)


(1.xx) a conversational flow comprising more than one disjointed sub-flows,


(1.xax) each sub-flow being a transport layer connection,


(1.1) each packet conforming to at least one protocol,

                                         - 56 -


(1.2) wherein at least one said protocol defines one or more conversational flows
       that each includes a plurality of states of the flow including an initial state,
       and transitions from the initial state to at least one of the plurality of states
       of the flow,


the method comprising:


(8.1) receiving commands in a high-level protocol description language that describe the protocols that may be used in packets, and


(8.2) translating the protocol description language commands into a plurality of
       parsing or extraction operations specified in a database (308) of parsing or
       extraction operations, and into a plurality of state operations specified in a
       database (326) of protocol dependent state operations,


(2)    receiving a packet (302) from a packet acquisition device;


(3y)   performing at least one of the parsing operations (304) and/or at least one
       of the extraction operations (306) on the packet


(3.1) to create a parser record comprising a function (312) of selected portions of
       the packet;


(3.2) wherein at least one of the parsing and/or extraction operations depend on
       one or more of the protocols to which the packet conforms;


(4)    looking up (314) in a flow-entry database (324) comprising flow entries for
       any previously encountered conversational flows,


(4.1) the look up using at least some of the selected packet portions and


(4.2) determining (316) if the packet is of an existing conversational flow;

                                        - 57 -


(5)   if the packet is of an existing conversational flow,


(5.1) classifying the packet as belonging to the found existing conversational flow
      and


(5.1x) obtaining the last encountered state of the flow and


(5.2y) performing (328, 330) any state operation or operations specified in a the
      database (326) of protocol dependent state operations for the state of the
      conversational flow starting from the last encountered state of the flow;


(6)   and if the packet is of a new conversational flow,


(6.1) storing (322) a new flow-entry for the new conversational flow in the flowentry database, including


(6.2) identifying information for future packets to be identified with the new flowentry,


(6.3y) determining the state and protocol of the flow (318) using the database
      (326) of protocol dependent state operations and


(6.4y) performing (328, 330) any state operation or operations specified in the
      database (326) of protocol dependent state operations for the initial state of
      the flow;


(7)   wherein each conversational flow that includes a plurality of states is
      recognized


(7.1) by transitioning through a plurality of states of the conversational flow, and

                                            - 58 -


(7.2y) at each state, carrying out one or more of the state operations specified in
       the database (326) of protocol dependent state operations for the state of
       the flow;


(7.5) and wherein the state operations for the states of the flow include updating
       the flow-entry, including storing identifying information for future packets to
       be identified with the flow-entry,


(7.6x) and wherein the state processing recognizes an application program from
       one or more disjointed sub-flows that occur in server announcement type
       flows.


Ein Vergleich zeigt, dass dieser Anspruch auf dem Anspruch 1 des Hilfsantrags 5
basiert und vor Merkmal (2) um folgende Merkmale ergänzt ist:


       (8.1) receiving commands in a high-level protocol description language
                that describe the protocols that may be used in packets, and


       (8.2) translating the protocol description language commands into a
                plurality of parsing or extraction operations specified in a database
                (308) of parsing or extraction operations, and into a plurality of state
                operations specified in a database (326) of protocol dependent state
                operations,


Ferner sind die Merkmale (3) (jetzt (3y)), (5.2x) (jetzt (5.2y)), (6.3x) (jetzt (6.3y)),
(6.4x) (jetzt (6.4y)) und (7.2) (jetzt (7.2y)) in sprachlicher Hinsicht daran
angepasst, insbesondere durch Bezugnahme auf die in Merkmal (8.2) eingeführte
„database (326) of protocol dependent state operations“, jedoch ohne inhaltlich
eine andere Bedeutung zu enthalten.


Die beiden neuen Merkmale sollen nach den Angaben der Beklagten auf die Figuren 3 und 4 mit zugehöriger Beschreibung und auf den ursprünglichen Anspruch 4

                                      - 59 -


(siehe Druckschrift N8) zurückgehen, ferner auf die Absätze [0093], [0094] sowie
[0402], [0403] des Streitpatents und den erteilten Unteranspruch 45.


3.7.3 Die beiden neuen Merkmale betreffen die Erzeugung zweier Datenbanken
für die Erkennung der einzelnen Protokolle und für die Zustandsmaschine (Datenbank 308 für die Untersuchung der Datenpakete und die Extraktion signifikanter
Bereiche, Datenbank 326 für protokollabhängige Zustandsoperationen). Diese
Datenbank-Erzeugung muss jedoch vorab erfolgen, sie ist kein Teil-Schritt während des Ablaufs der übrigen beanspruchten Arbeitsschritte des Paketmonitors.


Der Fachmann weiß, dass der Erfolg des beschriebenen Paketmonitors mit diesen
Datenbanken steht und fällt, und dass für jedes zu berücksichtigende Protokoll
eine intelligente Aufarbeitung des Protokolls zum Erkennen relevanter Datenabschnitte und zur Festlegung, worin sich das Protokoll von anderen unterscheidet,
sowie für die Beschreibung der durchlaufenen Zustände und Zuordnung jeweils
durchzuführender Operationen erforderlich ist. Wenn diese Arbeit für jedes Protokoll individuell erfolgt, ist die Zusammenstellung der Datenbanken sehr aufwändig
und mühsam.


Zur Verringerung dieses Aufwandes schlagen die beiden zusätzlichen Merkmale
des Hilfsantrags 8 vor, von einer „Protokollbeschreibungssprache“ (protocol
description language, PDL) auszugehen, welche jedes Protokoll mit seinen Eigenheiten abstrakt und maschinenverständlich beschreibt (und wie sie „an sich“ bekannt war, vgl. etwa die Druckschrift E15), und daraus automatisch die erforderlichen Untersuchungs-Operationen („parsing or extraction operations“) und Zustandsoperationen für die Zustandsmaschine („state operations“) abzuleiten.


3.7.4 Durch diese zusätzlichen Maßnahmen wird nach Auffassung des Senats
kein „konkretes technisches Problem“ gelöst.


Das hier gelöste Problem besteht in der Vereinfachung der Erzeugung der beiden
Datenbanken bzw. deren einfacher Erweiterung für neue oder zusätzliche Protokolle. Beansprucht wird damit ein Programm, welches aus einer Protokoll-Be-

                                       - 60 -


schreibung in einer Protokoll-Beschreibungssprache (PDL) automatisch diejenigen
Muster und Arbeitsschritte bestimmt, welche zur Erkennung der Datenpakete des
Protokolls benötigt werden. Dies ist eine reine Maßnahme der Programmierung,
ohne dass „auf technischen Überlegungen beruhende Erkenntnisse“ (BGH GRUR
2000, 498 - Logikverifikation) zugrundeliegen. Der Fachmann dafür ist ein Programmierer, der Protokolle, welche abstrakt anhand einer PDL beschrieben sind,
vergleicht und versucht, für alle Protokolle gültige Extraktionsregeln zu definieren;
irgendwelche technischen Kenntnisse werden dafür nicht benötigt. Auch allein die
Idee, eine solche Automatisierung vorzusehen, erfordert keine „technischen
Überlegungen“, sondern entsteht aus den Kenntnissen und Fähigkeiten des Informatikers betreffend Arbeitsvereinfachungen durch Generalisierung und Strukturierung.


Daher sind die zusätzlichen Merkmale (8.1) und (8.2) bei der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen (vgl. BGH GRUR 2011, 125 - Wiedergabe
topografischer Informationen).


3.7.5 Die Beklagte wendet ein, durch die Merkmale werde eine Schnittstelle für
die automatische Übergabe von Datenübertragungs-Protokollen an den erfindungsgemäßen Paketmonitor geschaffen. „Schnittstellen“ seien dem Patentschutz
aber generell zugänglich. Es dürfe keinen Unterschied machen, ob die Realisierung in Form eines Programmcodes oder durch Hardware erfolge; wenn vorliegend aber eine Hardware-Schnittstelle beansprucht worden wäre, dann würde deren grundsätzliche Patentierbarkeit nicht infrage gestellt werden. Nach der Entscheidungspraxis der Beschwerdekammern des Europäischen Patentamts müsse
der Beitrag der Erfindung auf technischem Gebiet liegen; das sei hier der Fall. Im
Übrigen könnten nur „Verfahren“ einem Ausschlusstatbestand unterliegen, nicht
aber das parallel beanspruchte Gerät (Paketmonitor).


Dieser Argumentation ist nicht zu folgen. Die von der Beklagten angesprochene
Problematik ergibt sich hier nicht, denn der Senat vertritt nicht die Auffassung, der
gesamte Gegenstand des Patentanspruchs sei als nicht technische Lehre vom
Patentschutz ausgeschlossen. Vielmehr berücksichtigt er lediglich bei der Prüfung

                                       - 61 -


der Patentfähigkeit der Lehre des Anspruchs solche Merkmale nicht, die zu einer
technischen Problemlösung nicht beitragen. Insoweit folgt der Senat den Grundsätzen der Rechtsprechung des BGH und der Entscheidungspraxis des EPA. Zwar
ist zuzustimmen, dass es bei der Realisierung einer technischen Problemlösung
nicht darauf ankommen kann, in welcher Weise (Programmcode oder Hardware)
sie erfolgt. Im vorliegenden Fall liefern die zusätzlichen Merkmale (8.1) und (8.2)
nach Verständnis des Senats aber keinen Beitrag zu einer „technischen Problemlösung“ (s. o. 3.7.4). Und schließlich gibt es keinen Grundsatz im Patentrecht,
dass „Schnittstellen“ dem Patentschutz zugänglich seien; allein der Vorschlag,
eine „Schnittstelle“ vorzusehen, kann nicht genügen, wenn ihm keine „auf technischen Überlegungen beruhenden Erkenntnisse“ zugrundeliegen (vgl. etwa die Senatsentscheidung 2 Ni 4/12 (EP) vom 14. November 2013, dort insbes. II. 2.2).


3.7.6 Nachdem die Merkmale (8.1) und (8.2) bei der Prüfung auf erfinderische
Tätigkeit nicht zu berücksichtigen sind, kann der Patentanspruch 1 des Hilfsantrags 8 nicht anders beurteilt werden als der zugrundeliegende Patentanspruch 1
des Hilfsantrags 5.


Mit dem Patentanspruch 1 fällt der gesamte Hilfsantrag 8 (vgl. oben II. 3.1.4).


3.7.7 Angesichts dieser Beurteilung kann es dahinstehen, dass der Einsatz einer
Schnittstelle für Protokolle basierend auf einer Protokoll-Beschreibungssprache
dem Fachmann geläufig war, wie es beispielsweise die Druckschrift E15 (dort
Bild 5.13 und zugehörige Beschreibung) belegt.


Auch dass die Formulierung der beiden neuen Merkmale möglicherweise den
Rahmen der ursprünglichen Offenbarung verlässt, wie die Klägerinnen aufzeigen,
braucht nicht weiter untersucht zu werden.


3.8   Der Hilfsantrag 9 ist bereits deshalb nicht gewährbar, weil die zusätzlichen
Merkmale seines Patentanspruchs 1 im Streitpatent nicht „unmittelbar und eindeutig“ offenbart sind und daher würde der Gegenstand dieses Patentanspruchs 1

                                        - 62 -


den Schutzbereich des europäischen Patents erweitern (Artikel II § 6 Absatz 1
Nr. 4 IntPatÜG, Artikel 138 Abs. 1 lit d EPÜ).


3.8.1 Der Patentanspruch 1 des Hilfsantrags 9 geht wiederum vom Patentanspruch 1 des Hilfsantrags 5 aus. Er soll nach Merkmal (2) bzw. nach Merkmal
(3.2) die folgenden beiden zusätzlichen Merkmale erhalten:


      (2.1) receiving a set of protocol descriptions for a plurality of protocols that
             conform to a layered model, a protocol description for a particular
             protocol at a particular layer level including:


             one or more child protocols of the particular protocol, the packet
             including for any particular child protocol of the particular protocol
             information at one or more locations in the packet related to the particular child protocol,


             one or more locations in the packet where information is stored
             related to any child protocol of the particular protocol, and


             one or more protocol specific operations to be performed on the
             packet for the particular protocol at the particular layer level, wherein
             the protocol specific operations include the state processing
             operation or operations that are a function of the state of the flow of
             the packet;


       (3.3) and wherein the parsing and extraction operations are determined
             from the received set of protocol descriptions, such that the specific
             operations to be performed on the packet are based on the base
             protocol of the packet and the children of the protocols used in the
             packet, and include the at least one parsing and/or extraction
             operation;

                                       - 63 -


Zur Offenbarung verweist die Beklagte auf die ursprünglichen Patentansprüche 60
bis 63 der PCT-Anmeldung (N8), auf die Absätze [0075] und [0076] sowie [0123]
des Streitpatents und auf die Beschreibung zu Figur 3. Eine Erläuterung des Begriffs „child protocol“ soll Absatz [0050] des Streitpatents entnehmbar sein, sowie
der Anlage MFG16.


3.8.2 In der geltenden Formulierung ist ein Ablauf von Verfahrensschritten beansprucht, der mit dem Empfang eines Datenpaketes beginnt (Merkmal (2)). Im folgenden Schritt soll ein Satz von Protokoll-Beschreibungen empfangen werden
(neues Merkmal (2.1)), bevor eine Analyse des Datenpaketes erfolgt (Merkmale
(3) ff.).


Bereits diese Reihenfolge ist schwer nachvollziehbar. Tatsächlich scheinen die
Protokoll-Beschreibungen vorab, also vor der Inbetriebnahme des Paketmonitors,
empfangen und in Analyse-Patterns für das Datenpaket (Figur 3: Datenbank 308)
und in eine protokollabhängige Abfolge von Zuständen und Zustands-Operationen
für die Zustandsmaschine (Figur 3: Datenbank 326) umgewandelt worden zu sein.
Auch die von der Beklagten angeführten Zitat-Stellen geben nichts Anderes her.
Das passt aber nicht zu der nunmehr beanspruchten Abfolge von Arbeitsschritten.


3.8.3 Soweit sich die Beklagte zum Offenbarungsnachweis allein auf die PCT-Anmeldung (N8) bezieht, kann ihr dies nicht weiterhelfen.


Denn nach einer Patenterteilung kann die Patentinhaberin nicht mehr auf den Offenbarungsumfang der ursprünglichen Anmeldung zurückgreifen, sofern dies zu
einer unzulässigen Erweiterung des Schutzbereichs des Patents führt (Art. 138
Abs. 1 lit d EPÜ).


3.8.4 Im erteilten Patent finden sich die gewählten Formulierungen für die neuen
Merkmale aber nicht wieder, wie ein einfacher Textvergleich zeigt. Auch sinngemäß gehen die konkreten Details der genannten Merkmale (2.1) und (3.3) über
das hinaus, was der Fachmann dem Streitpatent, insbesondere den von der Beklagten genannten Fundstellen „unmittelbar und eindeutig“ entnimmt.

                                      - 64 -


Zwar ist dem Fachmann vertraut, dass die in einem Datenpaket eines bestimmten
Protokolls enthaltenen Daten ihrerseits Datenpakete von Protokollen höherer
Ebenen enthalten, wobei diese Protokolle als „child protocols“ bezeichnet werden.
Das führt aber noch nicht zu einer Merkmalsformulierung wie in den Merkmalen
(2.1) und (3.3) gewählt.


Daher hält der Senat die Merkmale (2.1) und (3.3) für unzulässig.


3.8.5 Auch wenn man einräumen würde, dass der Fachmann die Details der
Merkmale (2.1) und (3.3) aufgrund seines Fachwissens ergänzt hätte, führt dies im
Ergebnis nicht weiter. Denn dies hätte zur Folge, dass mit diesen Merkmalen das
Vorliegen einer erfinderischen Tätigkeit aufgrund des darüber vorliegenden Fachwissens des Fachmanns nicht begründet werden könnte.


3.8.6 Deshalb kann dahingestellt bleiben, dass der Fachmann zumindest etwa
der Druckschrift E15 die erforderlichen Details entnehmen konnte, so dass die
Merkmale, im Sinne einer „Aggregation“ mit den übrigen Merkmalen, naheliegend
waren; und dass auch für diese Merkmale nicht erkennbar ist, wie sie zu einer
technischen Problemlösung beitragen (da es sich lediglich um eine Beschreibung
der Protokolle und ihrer bekannten gegenseitige Abhängigkeiten handelt, die bei
der Paket-Analyse berücksichtigt werden sollen, ohne dass irgendwelche „auf
technischen Überlegungen beruhende Erkenntnisse“ zugrundeliegen).


3.8.7 Auch hier fällt mit dem Patentanspruch 1 der gesamte Hilfsantrag 9 (vgl.
oben II. 3.1.4).


4.      Nachdem somit weder der Hauptantrag noch die Hilfsanträge 1 bis 9 Erfolg
haben, kann dahinstehen, ob außerdem - wie die Klägerinnen geltend gemacht
haben - die jeweils beanspruchte Lehre möglicherweise nicht in vollem Umfang
ausführbar ist, und ob sie vielleicht über den Inhalt der Patentanmeldung in ihrer
ursprünglich eingereichten Fassung hinausgeht. Es ist auch nicht mehr entscheidend, ob die Ansprüche der Hilfsanträge genügend klar und eindeutig formuliert
sind.

                                         - 65 -


                                           III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1
Satz 1 ZPO. Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99
Abs. 1 PatG, § 709 Satz 1 und 2 ZPO.




                                           IV.


                          Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufungsfrist beträgt einen Monat. Sie beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf
Monaten nach Verkündung.


Die Berufung ist durch einen in der Bundesrepublik Deutschland zugelassenen
Rechtsanwalt oder Patentanwalt schriftlich oder in elektronischer Form beim
Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


        - die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
        - die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,

                                     - 66 -


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Guth          Baumgardt        Dr. Thum-Rung      Dr. Forkel   Dr. Himmelmann


                                                                            Pr
