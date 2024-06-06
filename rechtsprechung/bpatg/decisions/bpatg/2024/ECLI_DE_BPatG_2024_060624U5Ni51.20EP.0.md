---
ecli: "ECLI:DE:BPatG:2024:060624U5Ni51.20EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 51/20"
decided: "2024-06-06"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=11&nr=44273&anz=391&pos=169&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-06-06_5_Ni_51_20_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 51/20 vom 2024-06-06

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                       Verkündet am
                                                        6. Juni 2024
5 Ni 51/20 (EP)                                              …
   verb. mit
5 Ni 56/21 (EP)

(Aktenzeichen)

                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2024:060624U5Ni51.20EP.0

                                        -2-




                 betreffend das europäische Patent 3 132 587
                              (DE 60 2015 031 814)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 6. Juni 2024 durch den Richter Heimen als
Vorsitzenden sowie die Richter Dipl.-Phys. Univ. Bieringer, Schödel, Dr.-Ing. Ball
und Dipl.-Phys. Christoph


für Recht erkannt:


I.    Das europäische Patent EP 3 132 587 wird für das Hoheitsgebiet der
      Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt, dass
      seine Patentansprüche folgende Fassung erhalten:


      1. A method, comprising:
             receiving, by each of a plurality of packet security gateways
             associated with a security policy management server and from the
             security policy management server, a dynamic security policy that
             includes at least one rule specifying packet-identification criteria and
             a packet transformation function comprising a packet digest logging

                                  -3-



      function to be performed on packets corresponding to the packetidentification criteria;


      receiving, by a packet security gateway of the plurality of packet
      security gateways, packets associated with a network protected by
      the packet security gateway;


      identifying, by the packet security gateway, from amongst the
      packets associated with the network protected by the packet security
      gateway, and on a packet-by-packet basis, one or more packets
      corresponding to the packet-identification criteria;


      performing, by the packet security gateway and on a packet-bypacket basis, the packet digest logging function on each of the one or
      more packets corresponding to the packet-identification criteria; and


      routing, by the packet security gateway and on a packet-by-packet
      basis, each of the one or more packets corresponding to the packetidentification criteria to a monitoring device in response to the
      performing the packet digest logging function,


wherein the performing the packet digest logging function on each of the
one or more packets corresponding to the packet-identification criteria
comprises:


      identifying a subset of information specified by the packet digest
      logging function for each of the one or more packets corresponding
      to the packet-identification criteria; and

                                   -4-



       generating, for each of the one or more packets corresponding to the
       packet-identification criteria, a record comprising the subset of
       information specified by the packet digest logging function, and


wherein the method further comprises:


       encapsulating each of the one or more packets corresponding to the
       packet-identification criteria with an Internet Protocol header
       specifying a network address corresponding to the monitoring device;


       stripping, by the monitoring device on a packet-by-packet basis, the
       Internet Protocol header specifying the network address
       corresponding to the monitoring device encapsulating the one or
       more packets comprising the packet-identification criteria; and


       forwarding, by the monitoring device on a packet-by-packet basis,
       one or more packets corresponding to the packet-identification
       criteria toward their respective destinations without the Internet
       Protocol header specifying the network address corresponding to the
       monitoring device.


2. The method of claim 1, wherein the subset of information comprises at
least one of a portion of data from the packet, a source address of the
packet, a source port of the packet, a destination address of the packet, a
destination port of the packet, a transport-protocol type of the packet, a
uniform resource identifier from the packet, an arrival time of the packet, a
size of the packet, a flow direction of the packet, an identifier of an interface
of the packet security gateway that received the packet, or one or more
media access control addresses associated with the packet.

                                  -5-



3. The method of claim 1, comprising:


       temporarily storing data in a memory of the packet security gateway,
       the data comprising the subset of information specified by the packet
       digest logging function for each of the one or more packets
       corresponding to the packet-identification criteria; and


       utilizing, by the packet security gateway, the data to generate a
       message comprising the subset of information specified by the
       packet digest logging function for each of the one or more packets
       corresponding to the packet-identification criteria.


4. The method of claim 3 comprising communicating, by the packet security
gateway and to the security policy management server, the message
comprising the subset of information specified by the packet digest logging
function for each of the one or more packets corresponding to the packetidentification criteria.


5. The method of claim 1, comprising reformatting, for each of the one or
more packets corresponding to the packet-identification criteria, the subset
of information specified by the packet digest logging function in accordance
with a logging system standard.


6. The method of claim 5, wherein reformatting the subset of information
specified by the packet digest logging function in accordance with the
logging system standard comprises reformatting the subset of information
specified by the packet digest logging function in accordance with a syslog
logging system standard.

                                   -6-



7. The method of claim 1, wherein the packet-identification criteria
comprises a five-tuple specifying one or more transport-layer protocols, a
range of source addresses, a range of source ports, a range of destination
addresses, and a range of destination ports, and wherein identifying the one
or more packets corresponding to the packet-identification criteria
comprises determining by the packet security gateway that each of the one
or more packets corresponding to the packet-identification criteria
corresponds to at least one of the one or more transport-layer protocols,
has a source address within the range of source addresses, a source port
within the range of source ports, a destination address within the range of
destination addresses, and a destination port within the range of destination
ports.


8. The method of claim 1, wherein the packet-identification criteria
comprises application-layer packet-header information, and wherein
identifying the one or more packets corresponding to the packetidentification criteria comprises determining by the packet security gateway
that each of the one or more packets corresponding to the packetidentification criteria comprises at least a portion of the application-layer
packet-header information.


9. The method of claim 8, wherein the application-layer packet-header
information identifies one or more hypertext transfer protocol packets, and
wherein identifying the one or more packets comprising the applicationlayer packet-header information comprises determining by the packet
security gateway that the one or more packets comprising the applicationlayer packet-header information comprises a particular hypertext transfer
protocol method call.

                                        -7-



       10. The method of claim 1, wherein the packet-identification criteria
       comprise a Differentiated Service Code Point, DSCP, descriptor.


       11. A system comprising at least one processor and a memory storing
       instructions that, when executed by the at least one processor, cause the
       system to perform one or more of the methods of claims 1 to 10.


       12. A computer program comprising computer-executable instructions that,
       when executed by one or more processors, cause the one or more
       processors to perform one or more of the methods of claim 1 to 10.


       Im Übrigen wird die Klage abgewiesen.


II.    Die Kosten des Rechtstreits werden gegeneinander aufgehoben.


III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des jeweils zu
       vollstreckenden Betrages vorläufig vollstreckbar.




                                    Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 3 132 587 (Streitpatent – SP),
das – unter Inanspruchnahme der Priorität der US 201414253992 vom 16. April
2014 – am 7. April 2015 angemeldet worden ist. Die Erteilung des europäischen
Patents ist am 12. Juni 2019 veröffentlicht worden. Das in englischer Sprache
gefasste Streitpatent trägt die Bezeichnung “METHODS AND SYSTEMS FOR
PROTECTING A SECURED NETWORK“, ins Deutsche übersetzt “SYSTEM UND
VERFAHREN ZUM SCHUTZ EINES GESICHERTEN NETZWERKS”. Es ist in Kraft
und umfasst in der erteilten Fassung insgesamt 15 Ansprüche, und zwar den auf
ein Verfahren gerichteten Anspruch 1 und die auf diesen unmittelbar oder mittelbar

                                           -8-



rückbezogenen Unteransprüche 2 bis 13, den auf eine Vorrichtung gerichteten
Anspruch 14 und den auf ein Computerprogramm gerichteten Anspruch 15.
Die nebengeordneten Patentansprüche 1, 14 und 15 lauten in der erteilten Fassung
in englischer Originalsprache wie folgt:


Patentanspruch 1:


      A method, comprising:
      receiving, by each of a plurality of packet security gateways associated with
      a security policy management server and from the security policy
      management server, a dynamic security policy that includes at least one rule
      specifying packet-identification criteria and a packet transformation function
      comprising a packet digest logging function to be performed on packets
      corresponding to the packet-identification criteria;
      receiving, by a packet security gateway of the plurality of packet security
      gateways, packets associated with a network protected by the packet security
      gateway;
      identifying, by the packet security gateway, from amongst the packets
      associated with the network protected by the packet security gateway, and
      on a packet-by-packet basis, one or more packets corresponding to the
      packet-identification criteria;
      performing, by the packet security gateway and on a packet-by-packet basis,
      the packet digest logging function on each of the one or more packets
      corresponding to the packet-identification criteria; and
      routing, by the packet security gateway and on a packet-by-packet basis,
      each of the one or more packets corresponding to the packet-identification
      criteria to a monitoring device in response to the performing the packet digest
      logging function, wherein the performing the packet digest logging function
      on each of the one or more packets corresponding to the packet-identification
      criteria comprises:

                                        -9-



      identifying a subset of information specified by the packet digest logging
      function for each of the one or more packets corresponding to the packetidentification criteria; and
      generating, for each of the one or more packets corresponding to the packetidentification criteria, a record comprising the subset of information specified
      by the packet digest logging function.


Patentanspruch 14:


      A system comprising at least one processor and a memory storing
      instructions that, when executed by the at least one processor, cause the
      system to perform one or more of the methods of claims 1 to 13.


Patentanspruch 15:


      A computer program comprising computer-executable instructions that, when
      executed by one or more processors, cause the one or more processors to
      perform one or more of the methods of claim 1-13.


Wegen des Wortlauts der auf Anspruch 1 unmittelbar oder mittelbar rückbezogenen
Ansprüche 2 bis 13 wird auf das Streitpatent verwiesen.


Mit ihren Klagen begehren die Klägerinnen die vollständige Nichtigerklärung des
Streitpatents, auch in der beschränkten Fassung gemäß Hauptantrag vom 6. Juni
2024. Sie machen die Nichtigkeitsgründe der fehlenden Patentfähigkeit, nämlich
mangelnde Neuheit und mangelnde erfinderische Tätigkeit (Art. 138 Abs. 1
Buchst. a) i.V.m. Art. 54, 56 EPÜ), sowie der unzulässigen Erweiterung (Art. 138
Abs. 1 Buchst. c) EPÜ) geltend und stützen ihren Vortrag u. a. auf die nachfolgenden Druckschriften:

                          - 10 -



NK1          Streitpatent EP 3 132 587 B1 (SP)
NK1a         ursprüngliche Anmeldeunterlagen
NK4          US 8,204,082 B2
NK5          US 2010/0162036 A1

NK6          EP 2 175 603 A1
NK7          US 2011/0314177 A1
NK8          US 8,347,384 B1
NK9          US 2004/0123220 A1
NK11         US 2008/0229415 A1
NK12                 RFC 2003
NK12a                Document History RFC 2003
NK13                 RFC 3164
NK13a                Document History RFC 3164
NK14                 RFC 2475
NK14a                Document History RFC 2475
NK15                 US 8,159,941 B2
NK18                 Benutzerhandbuch "Sourcefire 3D System",
             Version 4.10
NK19/NK19a           Eidesstattliche Versicherung X … zur NK18 mit
             deutscher Übersetzung
NK20/NK20a           Erklärung Y … zur NK18 im Inter Partes Review
             des USPTO mit deutscher Übersetzung
NK21         A. S. Tanenbaum: „Computernetzwerke“,
             Inhaltsverzeichnis und S. 33 – 37, S. 45 – 48, S. 52 -
             54, S. 443, S. 446 - 447, Prentice Hall, 2000.
NK26         Benutzerhandbuch „Sourcefire 3D System“, Version
             5.1.1
NK27/NK27a   Eidesstattliche Versicherung X … mit deutscher
             Übersetzung

                                       - 11 -



     NK28/NK28a           Eidesstattliche Versicherung Y … mit deutscher
                          Übersetzung
     NK29                 Sonia Fahmy, Vulnerabilities and Safe-guards in
                          Networks with QoS Support, Purdue e-Pubs, 2003
     HLNK1                Juniper, Concepts & Examples ScreenOS Reference
                          Guide, 2012-12-10
     HLNK1a               Juniper, Network and Security Manager Administration
                          Guide, 2011-04-01
     HLNK5                WO 2012/164336 A1


Die Beklagte verteidigt das Streitpatent nur noch in beschränkter Fassung gemäß
neuem Hauptantrag vom 6. Juni 2024. Auf den qualifizierten Hinweis des Senats
vom 4. Mai 2023 hin hat die Beklagte zur hilfsweisen Verteidigung des Streitpatents
mit Schriftsatz vom 19. Juni 2023 ferner sieben Hilfsanträge (1 bis 7, wobei sie
Hilfsantrag 7 in der mündlichen Verhandlung modifiziert hat) sowie mit Schriftsatz
vom 27. März 2024 einen weiteren Hilfsantrag 8 eingereicht.


Der neue Hauptantrag und vormalige Hilfsantrag 1 unterscheidet sich von der
erteilten Fassung des Streitpatents lediglich dadurch, dass die Unteransprüche 12
und 13 gestrichen worden sind und die Nummerierung der nebengeordneten
Ansprüche angepasst wurde.


Der Patentanspruch 1 gemäß Hilfsantrag 7 lautet:


      1.     A method, comprising:
             receiving, by each of a plurality of packet security gateways associated
      with a security policy management server and from the security policy
      management server, a dynamic security policy that includes at least one rule
      specifying packet-identification criteria and a packet transformation function
      comprising a packet digest logging function to be performed on packets
      corresponding to the packet-identification criteria, wherein the plurality of

                                  - 12 -



packet security gateways collectively provide an entire interface across each
boundary between a network protected by the plurality of packet security
gateways and a network other than the protected network, and wherein the
at least one rule is to be applied to all network traffic traversing the
boundaries;
       receiving, by a packet security gateway of the plurality of packet
security gateways, packets associated with a the network protected by the
plurality of packet security gateways and traversing the boundary;
       identifying, by the packet security gateway, from amongst the packets
associated with the network protected by the packet security gateway, and
on a packet-by-packet basis, one or more packets corresponding to the
packet-identification criteria;
       performing, by the packet security gateway and on a packet-by-packet
basis, the packet digest logging function on each of the one or more packets
corresponding to the packet-identification criteria; and
       routing, by the packet security gateway and on a packet-by-packet
basis, each of the one or more packets corresponding to the packetidentification criteria to a monitoring device in response to the performing the
packet digest logging function, wherein the performing the packet digest
logging function on each of the one or more packets corresponding to the
packet-identification criteria comprises:
       identifying a subset of information specified by the packet digest
logging function for each of the one or more packets corresponding to the
packet-identification criteria; and
       generating, for each of the one or more packets corresponding to the
packet-identification criteria, a record comprising the subset of information
specified by the packet digest logging function.




(Änderungen gegenüber dem erteilten Anspruch sind durch Unterstreichung
hervorgehoben.)

                                    - 13 -



Der Patentanspruch 1 gemäß Hilfsantrag 8 lautet:

                                      - 14 -



      (Änderungen gegenüber dem erteilten Anspruch sind durch Unterstreichung
      hervorgehoben.)


Der Patentanspruch 1 gemäß Hilfsantrag 6 stellt eine Kombination der erteilten
Patentansprüche 1 und 2 dar und lautet wie folgt:

                                      - 15 -




      (Änderungen gegenüber den beiden erteilten Ansprüchen 1 und 2 sind durch
      Streichung und Unterstreichung hervorgehoben.)


Wie im Hauptantrag wurden in den Hilfsanträgen jeweils die Unteransprüche 12 und
13 gestrichen und die Nummerierung der Ansprüche entsprechend angepasst.
Ebenso wurde die Nummerierung der Ansprüche im Hilfsantrag 6 aufgrund der
Kombination der Ansprüche 1 und 2 angeglichen. Wegen des Wortlauts der
Ansprüche im Übrigen sowie hinsichtlich der weiteren Hilfsanträge 2 bis 5 wird auf
die Akte verwiesen.


Die Klägerinnen vertreten zu den Nichtigkeitsgründen die Auffassung, der Gegenstand des erteilten Patentanspruchs 1 sei gegenüber den Anmeldeunterlagen aus
mehreren Gründen unzulässig erweitert. Die Gegenstände der Ansprüche 1, 14 und
15 seien auch nicht patentfähig, insbesondere mangele es ihnen an der Neuheit,
zumindest beruhten sie nicht auf einer erfinderischen Tätigkeit. Das gelte auch für
die Unteransprüche. Die mangelnde Neuheit dieser Ansprüche ergebe sich
insbesondere aus den Druckschriften NK4, NK5, NK18, NK26 sowie der
Kombination aus HLNK1 und HLNK1a. Ebenso sei Patentanspruch 1 nach allen

                                       - 16 -



Hilfsanträgen unzulässig erweitert, da diese Fassungen jeweils auf dem erteilten
Anspruch 1 beruhten. Im Übrigen mangele es diesen Fassungen jeweils aus den
gleichen Gründen wie dem erteilten Anspruch 1 an der Patentfähigkeit.


Die Klägerinnen beantragen,


        das europäische Patent EP 3 132 587 mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland in vollem
        Umfang für nichtig zu erklären.


Die Beklagte beantragt,


        die Klage mit der Maßgabe abzuweisen, dass das Streitpatent die
        Fassung gemäß Hilfsantrag 1, eingereicht mit Schriftsatz vom 19. Juni
        2023, erhält,


        hilfsweise die Klage mit der Maßgabe abzuweisen, dass das Streitpatent
        die Fassung des Hilfsantrags 7, eingereicht in der mündlichen
        Verhandlung, oder des Hilfsantrags 8, eingereicht mit Schriftsatz vom 27.
        März 2024, oder eines der Hilfsanträge 6, 2, 3, 4 oder 5, eingereicht mit
        Schriftsatz vom 19. Juni 2023, erhält.


Die Beklagte erklärt, dass der neue Hauptantrag vom 6. Juni 2024 (ehemals
Hilfsantrag 1 vom 19. Juni 2023) und die weiteren Hilfsanträge jeweils als geschlossene Anspruchssätze zu verstehen seien und die Hilfsanträge in der angegebenen
Reihenfolge gestellt seien.


Sie verteidigt das Streitpatent in der Fassung gemäß neuem Hauptantrag und tritt
der Klage in allen Punkten entgegen. Die geltenden Ansprüche gingen nicht über
die ursprünglich eingereichten Unterlagen hinaus und seien neu und erfinderisch.
Dies gelte auch für die Ansprüche nach den Hilfsanträgen. Jedenfalls in diesen

                                        - 17 -



hilfsweise verteidigten Fassungen seien die Ansprüche neu und beruhten auf einer
erfinderischen Tätigkeit. Die Handbücher NK18, NK26, HLNK1 und HLNK1a
gehörten nicht zum Stand der Technik, da sie zum Anmeldezeitpunkt nicht öffentlich
verfügbar gewesen seien.


In seinem qualifizierten Hinweis vom 4. Mai 2023 hat der Senat den Parteien die
Beschreibung des Betriebssystems CPOS (CloudShield Packet Operating System)
„CloudShield CS-2000 with CPOS 3.0.3 Security Target Version 1.0“ (im Folgenden
als NK4a bezeichnet) zum fachmännischen Verständnis der Lehre der NK4
übermittelt.


Wegen der weiteren Einzelheiten des Vorbringens der Parteien wird auf die
zwischen den Parteien gewechselten Schriftsätze nebst Anlagen und den weiteren
Inhalt der Akte Bezug genommen.




                              Entscheidungsgründe


Die Klagen sind zulässig und haben in der Sache teilweise Erfolg. Soweit die
Fassung des Streitpatents über die von der Beklagten noch gemäß geltendem
Hauptantrag verteidigte beschränkte Fassung hinausgeht, war diese ohne weitere
Sachprüfung für nichtig zu erklären. Das Streitpatent erweist sich ebenfalls als nicht
rechtsbeständig, soweit es über die mit Hilfsantrag 6 verteidigte Fassung
hinausgeht. Es ist daher im tenorierten Umfang wegen mangelnder Patentfähigkeit
gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i.V.m. Art.
56 EPÜ für nichtig zu erklären.

                                       - 18 -



                                         I.


1.     Zum Streitpatent


1.1    Das Streitpatent (EP 3 132 587) mit dem Titel „SYSTEM UND VERFAHREN
ZUM SCHUTZ EINES GESICHERTEN NETZWERKS“ betrifft „Packet Security
Gateways“ (PSGs), wobei diese Netzwerkschutzvorrichtungen von einem
zugeordneten „Security Policy Management Server“ dynamische „Security Policies“
übermittelt bekämen (Streitpatentschrift (SP), Abs. [0005]).


Nach der Beschreibung seien Netzwerkprotokolle trotz der fortlaufenden
Entwicklung in Richtung einer sicheren Kommunikation immer noch anfällig für
Angriffe wie bspw. DDoS-Angriffe („Distributed Denial of Service“; SP, Abs. [0001]).


Die meisten existierenden Ansätze zum Schutz von Netzwerken seien jedoch
reaktiv, d. h. sie könnten nur bereits erfolgreich gestartete Angriffe im Netzwerk
detektieren, die Quelle des Angriffs identifizieren und sukzessive gegensteuern.
Proaktive Lösungen könnten derzeit nicht bei größeren Netzwerken und deren
enormen Datenmengen eingesetzt werden, da diese zu viel Zeit benötigten, um den
nahezu kompletten Netzwerkverkehr mit hoher Auflösung zu filtern (SP, Abs. [0002]
u. [0003]).


Die Aufgabe des vorliegenden Streitpatents sei – im vorliegenden technischen
Kontext – somit die Verbesserung der Netzwerksicherheit mittels eines proaktiven
Ansatzes (SP, Abs. [0003]).


1.2    Der Anspruch 1 gemäß Hauptantrag vom 6. Juni 2024 (ehemals
Hilfsantrag 1) ist identisch zum erteilten Anspruch 1 und hat mit der Merkmalsgliederung des Senats in englischer Verfahrenssprache sowie der deutschen
Übersetzung folgenden Wortlaut:

                                          - 19 -



Merkmal   Patentanspruch 1                         Deutsche Übersetzung
M         lt. Streitpatentschrift                  lt. Streitpatentschrift
1         A method, comprising:                    Verfahren, das folgendes umfasst:

2         receiving, by each of a plurality of Empfangen,            durch     jeden    einer
          packet       security         gateways Mehrzahl       von      Paket      Securityassociated with a security policy Gateways,             die    einem       Security
          management server and from the Policy                       Management-Server
          security     policy       management zugeordnet sind, und von dem
          server, a dynamic security policy        Security     Policy        Management-Server, einer dynamischen Security
                                                   Policy,
3         that includes at least one rule die              mindestens         ein      Regeln
          specifying      packet-identification spezifizierendes
          criteria     and          a      packet Paketidentifizierungsmerkmal und
          transformation                  function eine Pakettransformationsfunktion
          comprising      a      packet     digest aufweist, die eine Paket Digest
          logging function to be performed Logging-Funktion zur Ausführung
          on packets corresponding to the an               Paketen      umfasst,       welche
          packet-identification criteria;          dem/den                     Merkmal(en)
                                                   entsprechen;
4         receiving, by a packet security Empfangen, durch einen Paket
          gateway of the plurality of packet Security-Gateway                der    Mehrzahl
          security     gateways,          packets von Paket Security-Gateways, von
          associated      with      a     network Paketen,      die     einem       Netzwerk
          protected by the packet security zugeordnet sind, das durch den
          gateway;                                 Paket Security-Gateway geschützt
                                                   wird;

                                       - 20 -



5   identifying, by the packet security ldentifizieren,           durch       den   Paket
    gateway,        from        amongst       the Security-Gateway, aus den dem
    packets     associated         with       the durch den Paket Security-Gateway
    network protected by the packet geschützten Netzwerk und Paket
    security    gateway,         and     on     a für Paket, eines oder mehrerer
    packet-by-packet basis, one or Pakete,                        die           dem/den
    more packets corresponding to Paketidentifizierungsmerkmal(en)
    the packet-identification criteria;           entsprechen;

6   performing, by the packet security Ausführen,                durch    den       Paket
    gateway and on a packet-by- Security-Gateway und Paket für
    packet basis, the packet digest Paket, der Paket Digest Logginglogging function on each of the Funktion an jedem des einen oder
    one        or      more            packets der mehreren Pakete, die dem/den
    corresponding          to    the   packet- Paketidentifizierungsmerkmal(en)
    identification criteria; and                  entsprechen; und



7   routing, by the packet security Routen, durch den Paket Securitygateway and on a packet-by- Gateway und Paket für Paket, jedes
    packet basis, each of the one or des einen oder der mehreren
    more packets corresponding to Pakete,                         die           dem/den
    the packet-identification criteria to Paketidentifizierungsmerkmal(en)
    a monitoring device in response to entsprechen,                      zu         einer
    the performing the packet digest Überwachungsvorrichtung                          als
    logging function,                             Reaktion auf das Ausführen der
                                                  Paket Digest Logging-Funktion;

                                           - 21 -



8           wherein the performing the packet wobei das Ausführen der Paket
            digest logging function on each of Digest Logging-Funktion an jedem
            the   one     or    more       packets des einen oder der mehreren
            corresponding      to   the    packet- Pakete,         die       dem/den
            identification criteria comprises:      Paketidentifizierungsmerkmal(en)
                                                    entsprechen, folgendes umfasst:


8.1         identifying a subset of information Identifizieren einer durch die Paket
            specified by the packet digest Digest Logging-Funktion für jedes
            logging function for each of the des einen oder der mehreren
            one      or        more        packets Pakete,         die       dem/den
            corresponding      to   the    packet- Paketidentifizierungsmerkmal(en)
            identification criteria; and            entsprechen,         spezifizierter
                                                    Informationsteilmenge; und

8.2         generating, for each of the one or Erzeugen, für jedes des einen oder
            more packets corresponding to der mehreren Pakete, die dem/den
            the packet-identification criteria, a Paketidentifizierungsmerkmal(en)
            record comprising the subset of entsprechen, eines Datensatzes,
            information    specified       by   the der die durch die Paket Digest
            packet digest logging function.         Logging-Funktion      spezifizierte
                                                    Informationsteilmenge umfasst.



1.3   Der Gegenstand des Streitpatents richtet sich an einen Ingenieur der
Elektrotechnik bzw. Nachrichtentechnik/Informationstechnik mit abgeschlossenem
Universitätsstudium und mit mehrjähriger Berufserfahrung in der Entwicklung
vernetzter, paketvermittelnder Datenübertragungs- und Kommunikationssysteme,
wobei der Fachmann insbesondere detaillierte Kenntnisse hinsichtlich der einschlägigen Netzwerkgeräte, Netzwerkprotokolle sowie der Netzwerksicherheit hat.

                                        - 22 -



1.4    Der Senat legt den Merkmalen nach Anspruch 1 folgendes Verständnis
zugrunde:


Mit dem Merkmal M1 ist ein Verfahren beansprucht, welches folgende räumlichkörperliche Vorrichtungen verwendet:
•     eine Vielzahl von Packet Security Gateways (PSGs), d. h. mindestens zwei
      PSGs (Merkmal M2),
•     einen Security Policy Management-Server (Merkmal M2),
•     ein Netzwerk, welches durch einen der Packet Security Gateways geschützt
      wird (Merkmale M4 und M5) und
•     eine Überwachungs-/Anzeigevorrichtung bzw. -gerät („monitoring device“,
      Merkmal M7),
wobei ein Packet Security Gateway jede Recheneinheit sein kann, die dazu
konfiguriert ist, Pakete zu empfangen und auf diesen eine Pakettransformationsfunktion (PTF) durchzuführen („…any computing device configured to
receive packets and perform a packet transformation function on the packets“, SP,
Abs. [0023]) und wobei ein Security Policy Management-Server jede Recheneinheit
sein kann, die dazu konfiguriert ist, ein dynamisches Regelwerk, das
Sicherheitsaspekte betrifft, an ein Packet Security Gateway zu kommunizieren
(„…any computing device configured to communicate a dynamic security policy to
a packet security gateway“, SP, Abs. [0023]).


Gemäß den Merkmalen M4 bis M7 ist ein Packet Security Gateway weiterhin dazu
geeignet, ein Netzwerk zu schützen (Merkmal M4), wobei das Gateway gemäß der
Beschreibung an der Grenze zwischen einem sicheren und einem unsicheren
Netzwerk angeordnet sein kann (vgl. SP, Fig. 1, 2, 6 bis 9 i.V.m. Abs. [0016], [0024],
[0066]), Pakete zu identifizieren (Merkmal M5), eine sog. „Packet Digest Logging
Function“ (PDLF) auszuführen (Merkmal M6) und Pakete, die einem Paketidentifikationskriterium entsprechen, zu routen (Merkmal M7). Insofern versteht der
Fachmann, dass das Packet Security Gateway ein so konfiguriertes Gateway ist.

                                        - 23 -



Somit fällt bspw. ein dementsprechend konfigurierter Router (ISO/OSI Layer 3) an
einer Netzwerkgrenze unter den im beanspruchten Verfahren verwendeten Packet
Security Gateway. Gleiches gilt für ein zumindest mit einem solchen Router
assoziiertes Packet Security Gateway (vgl. SP, Abs. [0065] – [0066]).


Gemäß Merkmal M2 überträgt der Security Policy Management-Server eine
dynamische Security Policy an die Packet Security Gateways, wobei „dynamisch“
hier lediglich als nicht statisch zu verstehen ist. Das Streitpatent beschreibt in
Figur 5 i.V.m. Absätzen [0047] bis [0051] sowie in Figur 13 i.V.m. Absatz [0073] für
die dynamische Security Policy einen manuellen Update-Prozess durch einen
Administrator sowie einen automatischen Update-Prozess, bspw. angestoßen
durch einen „malicious host tracker service“. Darüber hinaus wird der Security Policy
Management-Server auch vom Packet Security Gateway über den Datenverkehr
informiert, wobei der Packet Security Gateway die PDLFs der identifizierten Pakete
bspw. mittels einer Nachricht überträgt (vgl. SP, Abs. [0072]).


Merkmal M3 spezifiziert die Security Policy gemäß Merkmal M2 dahingehend, dass
diese mindestens eine Regel, zumindest Paketidentifizierungskriterien und eine
Pakettransformationsfunktion umfasst. Im vorliegenden technischen Kontext mit
Security Gateways und Firewalls handelt es sich bei der Security Policy also um ein
Regelwerk, das unter Sicherheitsaspekten gilt.


Die Paketidentifizierungskriterien und Pakettransformationsfunktion betreffen
jeweils IP-Pakete gemäß Vermittlungsschicht bzw. Layer 3 des ISO/OSI-Referenzmodells („IP packet“, SP, Abs. [0030]; „gateways may operate in a network
layer transparent manner … perform the packet transformation function at the
network layer“, SP, Abs. [0013]).


Als Paketidentifizierungskriterien nennt das Streitpatent u. a. die Paket-Header-Information des IP-Pakets, wie bspw. den IP-Quint („five tuple“), IP-Adressen für

                                        - 24 -



Quelle bzw. Ziel oder auch den DSCP („differentiated service code point“), sowie
die Paket-Header-Information der Anwendungsschicht, wie bspw. eine URI
(„uniform resource identifier“) bei einer HTTP-Datenübertragung oder einer VoIP-Session (vgl. SP, Fig. 3 i.V.m. Abs. [0030] und Abs. [0037], [0052], [0068] – [0069]).
Gemäß Streitpatent erfolgt die Paketidentifizierung in einem derzeit mit
Patentanspruch 1 nicht beanspruchten Paketfilter, welcher die Pakete hinsichtlich
bestimmter Information untersucht und anschließend an eine oder mehrere
Pakettransformationsfunktionen übergibt/weiterleitet (vgl. SP, Fig. 2 i.V.m. Abs.
[0025]).


Die Pakettransformationsfunktion definiert eine oder mehrere Handlungen
(„action“), welchen das Paket unterzogen wird. Das Streitpatent nennt als Beispiele
für Pakettransformationsfunktionen in Absatz [0033] ein Blockieren oder Verwerfen
identifizierter Pakete, in Absatz [0034] ein Akzeptieren oder Weiterleiten
identifizierter Pakete, in Absatz [0035] eine Firewallfunktionalität, in Absatz [0036]
eine zeitlich gestaffelte Wiederherstellungsfunktionalität nach Netzwerkattacken
sowie in Absatz [0039] ein Routen identifizierter Pakete an ein Überwachungsgerät
(„monitoring device“), um bspw. eine Personenüberwachung oder Strafverfolgung
(„Law Enforcement“) zu ermöglichen.


Die mit Merkmal M3 explizit umfasste „Packet Digest Logging Function“ (PDLF)
gehört ebenfalls zu den Pakettransformationsfunktionen. Im Englischen bezeichnet
ein Digest sprachlich u. a. eine Kurzfassung, einen Auszug bzw. einen Extrakt oder
auch eine Übersicht. Das Streitpatent versteht gemäß den Absätzen [0005], [0040],
[0072] sowie Patentanspruch 3 unter einem Packet Digest Logging ein Abspeichern
einer Untermenge der im Paket (Paketheader und Paketnutzlast) und/oder im
Security Gateway vorhandenen Information oder Metadaten bezüglich eines
identifizierten Pakets in einer Datenstruktur („a record comprising the subset of
information specified by the packet digest logging function“; „produces a digest
version, or log, of the packet. This packet log (or digest) may contain selected packet
information and/or system information (e.g. associated network addresses, ports,

                                        - 25 -



protocol types, URIs, arrival times, packet sizes, directions, interface names, media
access control (MAC) addresses, matching rule IDs, metadata associated with
matching rules, enforced policy names, or the like)“; „wherein the subset of
information comprises at least one of a portion of data from the packet, a source
address of the packet“; Unterstreichungen hinzugefügt). Nach fachmännischem
Verständnis grenzt sich der anspruchsgemäße Packet Digest Log also von einem
konventionellen Log dadurch ab, dass er
•    nur Informationen von identifizierten Paketen,
•    nur eine Teilmenge („subset“) der im Security Gateway vorhandenen
     Gesamtinformation über ein Paket,
•    und insbesondere nur einen Anteil bzw. Teilbereich der Paketdaten (Header
     und Payload)
aufweist. Ein Log umfassend eine (komplette) Paketkopie – also Header plus
Payload – fällt damit nicht unter den Anspruchsgegenstand. Je nach Paketgröße
und vorhandener System-/Metainformation hinsichtlich des Pakets im Security
Gateway kann der Packet Digest Log somit unter Umständen (insbesondere bei
kleinen Paketgrößen) durchaus voluminöser als ein konventioneller Log ausfallen,
so dass sich schon aus diesem Grund eine – wie oben genannte – linguistische
beschränkende Auslegung im Sinn einer Kurzfassung verbietet.


Die multiplen Regeln wie auch die multiplen Pakettransformationsfunktionen der
dynamischen Security Policy können gemäß Streitpatent kaskadiert, zusammengefasst oder in Phasen bzw. nacheinander in sequentieller Reihenfolge, ggf. zu
definierten relativen Zeitpunkten zueinander, ausgeführt werden („PTF1, PTF2,
PTFn“, SP, Fig. 2; „two rules requiring sequential execution“, Abs. [0006]; „the orderof-application of the rules“, Abs. [0032]; „the rules or rule sets should be
implemented in time-shifted phases.“, Abs. [0036]). Eine Regel kann auch parallel
mehrere Pakettransformationsfunktionen umfassen (vgl. SP, Fig. 2 i.V.m. Abs.
[0025] - [0026], [0030], [0040]).

                                       - 26 -



Merkmal M4 betrifft das Empfangen von Paketen durch den Packet Security
Gateway aus dem bzw. in das von diesem zu beschützende Netzwerk.


Merkmal M5 betrifft das Identifizieren von einem oder mehreren Paketen anhand
der Paketidentifizierungskriterien gemäß Merkmal M3. Der Verfahrensschritt des
Identifizierens der Pakete erfolgt auf Paketbasis („packet-by-packet“).


Merkmal M6 betrifft die Durchführung der in Merkmal M3 angegebenen PDLF auf
Paketbasis, wobei ausschließlich die in Merkmal M5 identifizierten Pakete
abgespeichert werden sollen. Was mit dem Paketprotokoll bzw. der damit
abgespeicherten Paketinformation weiter geschehen soll, lässt der Anspruchswortlaut offen. Gemäß den Ausgestaltungen der Unteransprüche 4 und 5 können
diese Informationen im Packet Security Gateway nur temporär gespeichert und
dann mittels einer Nachricht vom Packet Security Gateway an den Management
Server übermittelt werden. Darüber hinaus lehrt das Streitpatent ebenfalls die
Verwendung der PDLF im Zusammenhang mit einem „informational/ awareness
service“ (vgl. SP, Abs. [0040]).


Gemäß Merkmal M7 werden auf Paketbasis die identifizierten Pakete vom Packet
Security Gateway an ein Überwachungs- bzw. ein Anzeigegerät geroutet.
Hinsichtlich des Routings beschreibt das Streitpatent in den Absätzen [0039] und
[0055], dass für die Durchführung eines Überwachungsdienstes ein identifiziertes
Paket nicht an die ursprüngliche Zieladresse des Pakets, sondern an die
Netzwerkadresse des Überwachungsgeräts geroutet wird, wobei die Pakettransformationsfunktion des Routingdienstes dazu das Paket in einen neuen IP-Header mit der Zieladresse des Überwachungsgeräts einkapselt („the packet
transformation function may be configured to encapsulate the packets with an IP
header specifying the network address corresponding to the monitoring device“, SP,
Abs. [0039]). Anspruchsgemäß muss also im Layer 3 das empfangene IP-Paket
vollständig und wie ursprünglich formatiert an das Überwachungsgerät umgeleitet

                                        - 27 -



werden. Ein reines Versenden von dekodierter Paketinformation bzw. dekodierten
Paketdaten fällt somit nicht unter den Anspruch. Gleiches gilt für ein Versenden von
bloßen Teilen des Pakets, insbesondere des Digest Logs.


Darüber hinaus lehrt das Streitpatent in Figur 3 i.V.m. Absatz [0031], dass ein
identifiziertes IP-Paket ebenfalls zunächst akzeptiert und an die Zieladresse
weitergeleitet („forwarding (accepting or allowing)“) werden kann und danach noch
zusätzlich an das Überwachungsgerät geroutet wird („destined for any IP address
that begins with 120, and destined for port 90 should not only have an accept packet
transformation function performed on them, but should also be routed to a
monitoring device“; Unterstreichung hinzugefügt). Ähnliches offenbart das
Streitpatent in Absatz [0056], wonach zwei Pakettransformationsfunktionen
nacheinander angewendet werden. Dabei leitet die erste Pakettransformationsfunktion das Paket an die          Zieladresse   weiter und die zweite         Pakettransformationsfunktion routet das Paket an das Überwachungsgerät. Hierzu fertigt
das Security Gateway bei multiplen Pakettransformationsfunktionen ggf. auch
Paketrepliken (Kopien) an („configured to encapsulate the packets (or a copy of the
packets) with an IP header“, SP, Abs. [0056]).


Hinsichtlich der (nicht beanspruchten) Ausgestaltung des anspruchsgemäßen
Überwachungsgeräts offenbart das Streitpatent lediglich ein Kopieren bzw.
Abspeichern des empfangenen Pakets oder dessen Inhalts, ein Entfernen der
Einkapselung und ggf. ein Weiterleiten des Pakets an die ursprüngliche Zieladresse
(vgl. SP, Unteranspruch 2 sowie Abs. [0039] und [0055]). Gemäß Streitpatent
stehen die im Überwachungsgerät kopierten Pakete bzw. deren Inhalte für eine
nachfolgende Überprüfung oder Analyse, bspw. zur Strafverfolgung, zur Verfügung
(„review or analysis (e.g., by a law enforcement or national security authority)“, SP,
Abs. [0056]).
Im Merkmal M7 kommt es nicht darauf an, ob der Wortlaut „in response to“ temporal
oder kausal zu verstehen ist. Soweit die Klägerinnen die Auffassung vertreten, dass
damit nur ein kausaler Zusammenhang zwischen dem vom Digest geloggten Paket

                                        - 28 -



und dem gerouteten Paket beansprucht werde, vermag der Senat dem nicht zu
folgen. Denn die Patentschrift ist in einem sinnvollen Zusammenhang zu lesen und
ein Patentanspruch ist im Zweifel so zu verstehen, dass sich keine Widersprüche
zur Beschreibung und den Zeichnungen ergeben. Soweit gemäß Streitpatent das
Digest Logging eine oder ein Teil einer Pakettransformationsfunktion bzw. Aktion ist
und auch das Routen an eine Überwachungsvorrichtung eine Aktion darstellt und
beide Aktionen sowohl sequentiell als auch parallel ausgeführt werden können, fällt
ein Routen des Pakets beim Ansprechen bzw. im Anschluss an das Packet Digest
Logging auf jeden Fall unter den Anspruchsgegenstand. Gemäß Streitpatent spielt
die Fragestellung „temporal oder kausal“ auch funktional keine Rolle, da das vom
Packet Digest geloggte Paket und das geroutete Paket letztlich jeweils
unterschiedlichen Adressaten, nämlich zum einen dem Management Server oder
dem „informational/ awareness service“ (nicht beansprucht) und zum anderen dem
Überwachungsgerät zugestellt werden. Eine rein kausale Auslegung hinsichtlich
des Merkmals M7 greift daher zu kurz.


Die beanspruchten Verfahrensmerkmale M8, M8.1 und M8.2 betreffen wiederum
das Packet Digest Logging, wobei sich das diesbezügliche fachmännische
Verständnis mit dem hinsichtlich des Merkmals M3 (s. o.) deckt.


Für die Auslegung der gleichlautenden Merkmale der nebengeordneten Ansprüche
12 und 13 gelten entsprechende Überlegungen.

                                        - 29 -



                                         II.


Der Anspruch 1 in der Fassung gemäß Hauptantrag vom 6. Juni 2024 ist zulässig,
da sein Gegenstand in den ursprünglich eingereichten Anmeldeunterlagen offenbart
ist und er auch nicht über den Schutzbereich des erteilten Streitpatents hinausgeht.
Der Anspruch ist jedoch nicht patentfähig, da sein Gegenstand nicht auf einer
erfinderischen Tätigkeit beruht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 138
Abs. 1 Buchst. a), Art. 56 EPÜ).




1.    Der Anspruch 1 gemäß Hauptantrag vom 6. Juni 2024 ist identisch zum
erteilten Anspruch 1, so dass er nicht über den Schutzbereich des erteilten
Streitpatents hinausgeht und damit nicht unzulässig erweitert ist. Der Fachmann
entnimmt den Gegenstand des Anspruchs 1 den ursprünglichen Anmeldeunterlagen unmittelbar und eindeutig.


1.1   Der erteilte Patentanspruch 1 wird von den Klägerinnen aufgrund ihrer
Auslegung des Wortlauts „in response to“ im Merkmal M7 mit dem Argument der
unzulässigen    Erweiterung        gegenüber     den   ursprünglich   eingereichten
Anmeldeunterlagen angegriffen.


Die Beklagte vertritt dazu die Auffassung, dass das Paket nach dem Versenden aus
dem Gateway nicht mehr verfügbar sei und somit im Anschluss an das Routen nicht
mehr mittels der PDLF geloggt werden könne. Die Beklagte berücksichtigt dabei
jedoch nicht, dass das Gateway gemäß Absatz [70] in der ursprünglichen
Offenbarung, insbesondere bei der Ausführung multipler Pakettransformationsfunktionen (PTFs), ggf. auch Repliken bzw. Paketkopien verwendet („configured to
encapsulate the packets (or a copy of the packets) with an IP header“, NK1a, Abs.
[70]; Unterstreichung hinzugefügt).

                                        - 30 -



In den ursprünglichen Anmeldeunterlagen findet sich zwar explizit kein
Ausführungsbeispiel mit der beanspruchten Kombination von PDLF und Routing an
das Überwachungsgerät. Die NK1a beschreibt zum einen die PDLF in Absatz [54],
in Figur 12 i.V.m. den Absätzen [84] bis [86] sowie in den ursprünglichen
Ansprüchen 10 bis 18, wobei als kausale Aktion der PDLF bspw. das Bereitstellen
eines Logs an einen „awareness application server“ oder das Generieren einer
Message aus den gespeicherten Daten an einen Computer bzw. den Security Policy
Management-Server („computing device“, „security policy management server“)
genannt wird. Die ursprünglichen Anmeldeunterlagen offenbaren zum anderen
ebenfalls nur ein separates Routing des Pakets an ein Überwachungsgerät gemäß
NK1a, Absätzen [45], [53] und [68] bis [70].


Der   zeitliche   Zusammenhang        zwischen    mehreren     kombinierten   Pakettransformationsfunktionen beim Ausführen einer Regel ergibt sich jedoch aus den
Absätzen [07] („two rules requiring sequential execution“), [46] („the order-ofapplication of the rules“) sowie [50] („execution in time-shifted phases“).


Im Übrigen spielt die Fragestellung „temporal oder kausal“ in der Gesamtschau der
Lehre des Streitpatents funktional keine Rolle, da unterschiedliche und voneinander
unabhängige Aktionen bzw. Dienste betroffen sind (vgl. ebenso die Auslegung
gemäß Ziff. I 1.4). Denn der Security Policy Management-Server, der dem Packet
Security Gateway u. a. die dynamische Security Policy bereitstellt, wird bspw. vom
Packet Security Gateway mittels Nachrichten, die jeweils den „Digest Log“
identifizierter Pakete umfassen, regelmäßig systemintern informiert (vgl. NK1a, Abs.
[86], Anspruch 14). Völlig unabhängig davon wird das identifizierte (gleiche) Paket
(oder dessen Replik) zur weiteren Analyse an das Überwachungsgerät geschickt.


Die Diskussion „temporal oder kausal“ kann letztlich auch deshalb dahingestellt
bleiben, da der genannte Stand der Technik bspw. mit der Druckschrift NK4 bzw.
der Druckschrift HLNK1 das Merkmal M7 sowohl hinsichtlich einer temporalen als

                                       - 31 -



auch hinsichtlich einer kausalen Ausführung von Regeln und Aktionen bzw.
Pakettransformationsfunktionen aufzeigt.


1.2   Auch die Argumentation der Klägerinnen, dass ein Anwenden mehrerer
PTFs auf das gleiche Paket nicht ursprungsoffenbart sei, ist unzutreffend. Denn die
NK1a, Absatz [80], offenbart zusätzlich zu den bereits oben unter Ziff. II 1.1
genannten Textstellen betreffend das parallele bzw. sequentielle Anwenden von
PTFs explizit das Spezifizieren multipler PTFs, mittels derer identifizierte Pakete
weiterverarbeitet werden sollen („and may further specify one or more packet
transformation functions to be performed on packets matching the specified criteria.
Packet security gateway 910 may identify packets matching one or more of the
criteria specified by the rules and may perform the associated packet transformation
functions on the identified packets“, Unterstreichungen hinzugefügt).


1.3   Ebenso greift auch die Argumentation der Klägerinnen, dass die beanspruchte Kombination aus PDLF und Routing lediglich eine beliebige Auswahlentscheidung mit Merkmalen aus einem Reservoir verschiedener Ausführungsbeispiele darstelle, nicht durch. Denn die ursprüngliche Offenbarung NK1a, Figur 2
i.V.m. Absätze [39] bis [41], lehrt multiple parallele PTFs („For example, dynamic
security policy 212 may include one or more rules specifying that packets having
specified information should be forwarded to packet transformation function 216,
while all other packets should be forwarded to packet transformation function 218.
Packet transformation functions 1 – N 216, 218, and 220 may be configured to
perform one or more functions on packets they receive from packet filter 214.“).


Insbesondere lehrt die ursprüngliche Anmeldung den Fachmann an mehreren
Stellen multiple Services bzw. PTFs gemäß den Ausführungsbeispielen in den
Absätzen [47] ff. zu implementieren, wobei vorzugsweise ebenso das anspruchsgemäße „Routing zum Monitor“ umfasst sein sollte („effectuating one or more
services within a network environment.“, NK1a Abs. [47]; „By utilizing packet
security gateway 910 within network environment 900, an operator of network

                                         - 32 -



environment 900 may be able to protect network environment 900 from network
attacks, as well as implement one or more services (e.g., blocklist service, allowlist
service, VoIP firewall service, phased restoration service, enqueueing service, multidimensional routing service, or monitoring service) within network environment
900.“, NK1a, Abs. [80]; „… specify a packet transformation function other than
forwarding (accepting or allowing) or dropping (denying) a packet. … but should also
be routed to a monitoring device“, NK1a, Abs. [45]; Unterstreichungen hinzugefügt).


Das „Routing zum Monitor“ ist also gemäß NK1a ein erfindungswesentliches
Merkmal, das an vielen Stellen der ursprünglichen Anmeldung ausgestaltet wird
(vgl. NK1a, Fig. 3 BZ 306 und Abs. [11], [52], [53], [66], [68], [71], [80]). In diesem
technischen Kontext ist das „Digest Logging“ ebenfalls ein essentieller Kerngedanke, der bereits ursprünglich beansprucht wurde und ebenfalls an mehreren
Stellen in den ursprünglichen Unterlagen vorkommt (vgl. NK1a, Ansprüche 10-18,
Fig. 12, Abs. [54], [84] – [86]). Die fraglichen Merkmale PDLF und Routing werden
somit in den ursprünglichen Anmeldeunterlagen als „bevorzugt“ hervorgehoben.
Insbesondere beschreiben die NK1a, Absätze [47] und [80], ein Packet Security
Gateway zum Schutz einer Netzwerkumgebung vor Netzwerkattacken, welches
mittels der „dynamic security policy“ die genannten multiple Dienste bereitstellt,
wozu ein „blocklist service“ (Absatz [47]), ein „allowlist service“ (Absatz [48]), ein
„firewall service“ (Absatz [49]), ein „restoration service“ (Absatz [50]), ein „enqueuing
service“ (Absatz [51]), ein „routing service“ sowie ein „monitoring service“ mit dem
beanspruchten Routen des Pakets an ein Überwachungsgerät (Absätze [52] und
[53]) und ein „informational/awareness service“ umfassend die PDLF (Absatz [54])
zählen.


Die ursprüngliche Anmeldung offenbart demnach gemäß NK1a, Absätze [47] ff. und
[80], eine einstellige, für den Fachmann durchaus überschaubare Anzahl von
Diensten sowie den mit diesen assoziierten PTFs zur Auswahl, von denen in der
Anmeldung – wie oben ausgeführt – dem „Routing zum Monitor“ und dem „Digest
Logging“ jeweils eine zentrale Bedeutung zukommt, und wobei gemäß Absatz [45]

                                        - 33 -



„accept/allow“ bzw. „drop/deny“ bereits als unwesentliche und gängige PTFs
identifiziert wurden. Eine übermäßige Komplexität aufgrund einer unüberschaubaren Vielzahl optionaler Merkmale liegt entgegen der Auffassung der Klägerinnen
nicht vor, da mit der Kombination „Routing zum Monitor“ und „Digest Logging“/PDLF
gerade die zwei wesentlichen Kerngedanken der Erfindung Eingang in den
Anspruch 1 gefunden haben. Die von den Klägerinnen in dem Zusammenhang
zitierte höchstrichterliche Rechtsprechung (BGH, Xa ZR 148/05, Urteil vom
14.05.2009 – Heizer; X ZR 4/22, Urteil vom 20.07.2023 - Funktionstaste) gibt nicht
Anlass für eine andere Beurteilung, weil diese die Kombination verschiedener
Offenbarungsstellen der Beschreibung betrifft, die in keinem erkennbaren Zusammenhang miteinander stehen. Dies ist hier, wie ausgeführt, nicht der Fall.


2.    Der Gegenstand des Anspruchs 1 gemäß Hauptantrag ist gegenüber der
Lehre der Druckschriften NK4 bis NK9, NK11 bis NK15, NK18, NK21, NK26, NK29
sowie HLNK1/1a und HLNK5 neu (Art. 54 EPÜ), denn es fehlt jeder dieser Druckschriften jeweils mindestens eines der Merkmale, die im Anspruch 1 enthalten sind.


2.1   Der Beklagten ist nicht darin zu folgen, dass die „Sourcefire“-Benutzerhandbücher (NK18, NK26) sowie die „Juniper“-Benutzerhandbücher (HLNK1,
HLNK1a) zum Anmeldezeitpunkt nicht öffentlich zugänglich gewesen seien. Ein
vorveröffentlichtes Benutzerhandbuch gilt stets als Stand der Technik. Der
Umstand, dass nur derjenige Zugriff auf das Handbuch hat, der es erwirbt, steht
dem nicht entgegen (vgl. BGH, X ZR 41/11, Urteil vom 15.10.2013 – Bildanzeigegerät; BGH, X ZR 113/15).




2.2   Aus der Druckschrift NK4 (US 8,204,082 B2) sind nicht sämtliche Merkmale
des Gegenstands des Anspruchs 1 bekannt. Diese betrifft eine hinsichtlich Zuverlässigkeit, Sicherheit und Fehlertoleranz verbesserte Internet-Infrastruktur für einen
Service-Provider mit einem „edge adapter“ bzw. „packet interceptor“, welcher bspw.

                                         - 34 -



aus einem Cisco 12000 Series GSR (Gigabit Switch Router) in Kombination mit
einer CloudShield CS-2000 „intelligent packet architecture“ besteht (vgl. NK4, Fig.
6 - 7 i.V.m. Sp. 1, Z. 53 – 56, Sp. 33, Z. 35 – Sp. 34, Z. 67).


Die NK4 hat ein Verfahren ( „a method“; Merkmal M1) mit multiplen Edge Servern
in einem Internet Service Provider (ISP) Netzwerk zum Gegenstand, wobei Figur 6
exemplarisch zwar nur einen Edge Server pro ISP zeigt, jedoch aus dem folgenden
Kontext hervorgeht, dass jeder ISP mehrere Edge Server in seinem Netzwerk
installiert hat („… additional upstream edge servers and edge caches can be
provided at major peering points … a hierarchy of edge servers and edge caches
can be used to handle any overload of one or more downstream edge servers and
edge caches …“, vgl. NK4, Fig. 6 i.V.m. Sp. 28, Z. 54 – 58 und Sp. 29, Z. 35 – 45).
Jeder Edge Server umfasst einen Router und einen Packet Analyzer, welchem über
ein Management Interface oder von externen Geräten eine Security Policy mit
Regeln zugeführt wird (vgl. NK4, Fig. 7 i.V.m. Sp. 35, Z. 14 – 20, Sp. 40, Z. 39 – 62).
Bei der Security Policy der NK4 handelt es sich um eine dynamische Security Policy
mit einem sich über der Zeit verändernden Regelsatz (vgl. NK4, Sp. 40, Z. 59 – 62;
Sp. 59, Z. 26 – 59). Die NK4 offenbart zwar neben dem Management Interface in
Figur 7, Bezugszeichen 722, noch ein IBM IPMI Interface (vgl. NK4, Sp. 51, Z. 57 –
67) sowie ein externes Managementgerät oder einen Desktopcomputer („external
management device“, „desktop computer“, vgl. NK4, Sp. 41, Z. 47 – 59, Sp. 67, Z.
27 – 58), schweigt jedoch hinsichtlich des Security Policy Management Servers
(Merkmal M2 nur teilweise).


Gemäß NK4, Spalte 44, Zeilen 8 bis 30, besteht ein Regelsatz aus einem verlinkten
Baum logisch verknüpfter Knoten, die Informationen über ein Paket sammeln („data
gathering“), anhand der identifizierten Paketmerkmale entscheiden („decision“) und
eine Aktion („action“), d. h. eine Operation mit dem Paket, durchführen. Die NK4
lehrt auch explizit eine Paket Digest Logging-Funktion („If the packet 704 is to be
intercepted, it is stored in the buffer 714 for further processing and analysis by the
rules processor 716 and interceptor/analyzer 712 or one or more of the external

                                        - 35 -



devices 724“, NK4, Sp. 35, Z. 43 – 46; „the packet analyzer 720 may log or otherwise
store information about the packet, including storing a copy of the packet itself“, Sp.
39, Z. 29 – 32; „data about the packet 704 may be stored in a memory for use by
other rules, for processing the current or future packets 704“, Sp. 39, Z. 49 – 51; „An
additional basic operation of the packet analyzer 720 is provided for storing a one
or more attributes or an entire copy, of the captured packet(s) in a state memory“,
Sp. 56 – 58; Unterstreichungen hinzugefügt; Merkmal M3).


Die NK4 zeigt weiter ein Empfangen von Paketen durch den Packet Security
Gateway („The adapter 720 is coupled with the router 702 so as to be able to
intercept packets 704 before they are routed by the router 702 over the network
100“, NK4, Fig. 7 i.V.m. Sp. 34, Z. 60 – 62; Merkmal M4).


Sie beschreibt ein paketweises Identifizieren von einzelnen Paketen anhand der
Identifizierungsmerkmale („As packets 704 enter the router 702, they are
temporarily diverted to the packet analyzer 712 which determines whether or not the
packet is to be intercepted. This determination is made in conjunction with the rules
processor 716 by analyzing the header data 706 and application data 707 contained
with the packet 704 according to pre-defined rules contained within the rules
processor“, NK4, Sp. 35, Z. 34 – 40; „Interception and subsequent processing of
packets 704 is based on the application of rules to any of the various layers of data
contained with the packet 704“, Sp. 35, Z. 47 - 49; Merkmal M5).


Die obigen Ausführungen zu Merkmal M3 gelten entsprechend auch für Merkmal
M6.
Die NK4 lehrt ferner ein sequentielles bzw. temporales sowie ein bedingtes
Abarbeiten von Regeln sowie zusammengesetzte Pakettransformationsfunktionen
pro Regel („the packet analyzer 720 will take the desired course of action or actions
as dictated by the rule 732. The packet analyzer 720 is capable of taking several
basic actions independently or in combination“, NK4, Sp. 39, Z. 5 – 8, Sp. 39, Z. 13

                                        - 36 -



– 17; „compound actions to be taken on a given packet“, Sp. 39, Z. 34 – 40). Zwar
beschreibt die NK4 explizit kein Routen von Paketen, jedoch ein Weiterleiten
(„forward“) einer Kopie des Pakets an ein externes Gerät („external device“), wobei
das externe Gerät das Paket weiterverarbeitet oder ein Überwachen des Pakets
durchführt („Further the data can include copies of buffered packets 704 from the
packet analyzer 712 sent to one or more of the external devices 724 in response to
the action of one or more rules 732“, vgl. NK4, Sp. 39, Z. 24 – 25, Sp. 40, Z. 45 –
46 und Sp. 40, Z. 63 - Sp. 41, Z. 10; Unterstreichungen hinzugefügt; Merkmal M7
nur teilweise).


Allerdings offenbart die NK4 ein Paket Digest Logging umfassend ein Abspeichern
von Information über das Paket, Daten über das Paket bzw. ein oder mehrere
Attribute des Pakets, vgl. obige Ausführungen zu M3 (Merkmal M8, M8.1, M8.2).
Alternativ kann darüber hinaus aber auch eine komplette Kopie des Pakets
abgespeichert oder gelogged werden („including storing a copy of the packet itself“,
NK4, Sp. 39, Z. 29 – 32; „or an entire copy“, Sp. 39, Z. 56 – 58).


2.3 Die Druckschrift NK5 (US 2010/0162036 A1) betrifft einen Cluster aus einer
Vielzahl von „computing devices“, welcher mittels der verteilten Rechnerarchitektur
anhand einer „security policy“ Sicherheitsdienste wie bspw. Firewall, VPN,
Paketfilterung usw. bereitstellt, wobei der Cluster einen Master zur Konfiguration
und Organisation umfasst, und wobei die „security policy“ aus Regeln besteht, die
von einem „policy server“ empfangen und ggf. mittels Updates dynamisch
modifiziert werden (vgl. NK5, Fig. 1 i.V.m. Abs. [0031], [0037], [0087], [0090],
[0146]).


Die NK5 beschreibt in Absatz [0097] das Senden von Daten an einen Quarantäneserver sowie das Senden von Logging-Information an einen Log-Server, ohne zu
Details hinsichtlich einer potentiellen Paketidentifizierung, der Art und dem Format
der Daten bzw. der Logging-Information und dem Senden auszuführen.

                                      - 37 -




In der NK5 fehlen eine Vielzahl von Packet Security Gateways (Merkmal M2
teilweise), ein Packet Digest Logging identifizierter Pakete (Merkmale M3
teilweise, M6, M8, M8.1, M8.2) sowie ein Routen identifizierter Pakete an das
Überwachungsgerät bzw. den Quarantäneserver im Anschluss an das Logging
(Merkmal M7 teilweise).


2.4 Die Druckschrift NK18 ist das Benutzerhandbuch („user guide“) für das
„Sourcefire 3D-System“ (Version V4.10), das eine Echtzeit-Netzwerkintelligenz für
den Netzwerkschutz bereitstellt, wobei im Netzwerk verteilte 3D-Sensoren den
Netzwerkverkehr erfassen und Daten bzw. Pakete loggen, im Rahmen eines
„intrusion prevention systems (IPS)“ Ereignisse wie bspw. „intrusion events“
feststellen und die gesammelten Informationen an ein zentrales „defence center“
bzw. übergeordnetes „master defence center“ zur Auswertung und Abspeicherung
in Datenbanken schicken, wobei das „defence center“ die 3D-Sensoren mit
dynamischen „Security Policies“ konfiguriert und verwaltet (vgl. NK18, Figur S. 107
sowie S. 32 – 36 und S. 267).


Sourcefire basiert u. a. ebenfalls auf Cisco NetFlow, das in der RFC 3954 beschrieben ist und den Export von im Netzwerk durch „observation points“ anhand
von definierbaren „templates“ gesammelten Flow-Daten an Kollektoren bspw. eines
Überwachungssystems spezifiziert (vgl. NK18, S. 884 – 885 und Kapitel 26, S. 1140
ff.).




In der NK18 fehlt bereits Merkmal M2 teilweise, da der NK18 eine Konkordanz
bzw. eine Assoziierung von unabhängigen bzw. eigenständigen („standalone“) 3D-Sensoren mit anspruchsgemäßen Security Gateways nicht zu entnehmen ist. Bei
den 3D-Sensoren handelt es sich einerseits um passive Datenerfassungsvorrichtungen mit einer Alarmfunktion bzw. Exportfunktion zum Versenden von

                                       - 38 -



Eventdaten und andererseits um „inline“ Sensoren, d. h. im Leitungsweg eines
Netzwerksegments eingebaute Datenerfassungsvorrichtungen mit einer zusätzlichen Filterfunktion („configure rules to drop suspicious packets“, „modify or drop
packets“), jedoch in beiden Fällen ohne die anspruchsgemäße Routingfunktionalität
eines Gateways bzw. ohne Assoziierung mit einem verbundenen Router oder
Switch (vgl. NK18, S. 262 – 264). Die NK18 zeigt in der Figur auf S. 1149 eine
beispielhafte Sourcefire 3D-Installation mit passiver Datenerfassung, wobei der 3D-Sensor an ein Tap zwischen Firewall und DMZ angeschlossen ist. Das eigentliche
Gateway dieses Netzwerks, d. h. der Router zum Internet, wird überhaupt nicht
überwacht. Der zweite Router zum „Engineering Network“ und zum „Sales Network“
wird mit NetFlow freigegeben und sendet seine NetFlow-Exportdaten in einem
Rundstrahlmodus („broadcast“) erst zum 3D-Sensor zur Weiterleitung an das
„defence center“. Die Kommunikation zwischen 3D-Sensor und „defence center“
wird gemäß obiger Figur zudem ausschließlich über das Management-Interface
durchgeführt.


Darüber hinaus zeigt die NK18 im Standardbetrieb auch kein Packet Digest Logging
gemäß den Merkmalen M3 (teilweise), M6, M8, M8.1, M8.2, sondern einen
konventionellen Packet Log, da bei einem „packet-based event“ zusammen mit dem
„intrusion event“ stets eine komplette Paketkopie und kein anspruchsgemäßes
Subset bzw. Extrakt der Paketinformation im 3D-Sensor abgespeichert bzw.
protokolliert wird (vgl. NK18, S. 267). Der Senat vermag sich insoweit nicht der
Ansicht der Klägerin anzuschließen, dass der „intrusion event“ exklusiv als Digest
Log identifiziert wird, da hierbei der eigentliche Packet Log des kompletten Pakets
ausgeblendet wird („Each event in the database includes two types of information
about the potential attack. The first is called an event header and contains
information about the event name and classification, the source and destination IP
addresses and ports, the process that generated the event, and the date and time
of the event. The second is the packet log and includes a copy of the decoded
packet header and packet payload“, NK18, S. 260; Unterstreichungen hinzugefügt).

                                       - 39 -



Schließlich fehlt in der NK18 auch das Routen des Pakets an das Überwachungsgerät gemäß Merkmal M7. Stattdessen sendet der 3D-Sensor die Eventdaten
umfassend den Packet Log an das Defence Center, wobei der Packet Log eine
Kopie des dekodierten Paketheaders und der dekodierten Payload umfasst und
eben nicht das unkodierte bzw. originale Paket oder dessen (unveränderte) Replik
(„The second is the packet log and includes a copy of the decoded packet header
and packet payload“, NK18, S. 260, letzter Absatz; Unterstreichung hinzugefügt).
Die NK18 führt auf Seite 218 zudem aus, dass durch das Dekodieren bspw. das
Format des Pakets geändert wird. Zur Kommunikation zwischen 3D-Sensor und
Defence Center dient ein dedizierter, bidirektionaler und SSL-verschlüsselter
Kommunikationskanal, über welchen das Defence Center die 3D-Sensoren
verwaltet („management“) und Policies verschickt sowie die Sensoren die
gesammelten Eventdaten an das Defence Center übermitteln (vgl. NK18,
S. 118 – 126).


Zwar kann das automatische Loggen des kompletten Pakets in einem Sensor
optional ausgeschaltet werden („Prohibit Packet Transfer to the Defense Center“,
NK18, S. 125 – 126), d. h. mit dem „event“ wäre zumindest ein Digest Log im Sinne
des Streitpatents verfügbar, allerdings würde auch dann immer noch das Routen
des Pakets zum Überwachungsgerät gemäß Merkmal M7 fehlen.


2.5   Die Druckschrift NK26 ist das Benutzerhandbuch zur Nachfolgeversion
(Version V5.1.1) des unter Ziff. 2.4 beschriebenen Sourcefire3D-Systems.
Hinsichtlich der Neuheitsbetrachtung des Anspruchs 1 gilt für die NK26 im
Wesentlichen die gleiche Argumentation wie für die Vorgängerversion NK18.
Gemäß NK26 wird zu jedem Event neben dem Event Header ein komplettes Paket
geloggt, womit kein Digest Log (PDLF) vorliegt („For packet-based events, a copy
of the packet or packets that triggered the event is also recorded“, NK26, S. 458;
„Each event in the database includes two sources of information about the potential
attack. The first is called an event header and contains information about the event
name and classification, the source and destination IP addresses and ports, the

                                      - 40 -



process that generated the event, and the date and time of the event. The second
is the packet log and includes a copy of the decoded packet header and packet
payload“, S. 463; „logging is automatic“, S. 486; Merkmal M6, Merkmalsgruppe
M8 fehlen). Das automatische Loggen kann allerdings analog zur NK18 optional
ausgeschaltet werden (vgl. NK26, S. 317 – 318).


Darüber hinaus wird – sofern nicht ausgeschaltet – neben dem Event Header stets
das geloggte Paket an das Defence Center gesendet („To send connection events
to the Defence Center“, NK26, S. 318), wobei das geloggte Paket im Defence
Center zum Download lediglich umformatiert im libpcap-Format vorliegt (vgl. NK26,
S. 491, S. 494, S. 498, S. 500), so dass das Paket nicht zum Überwachungsgerät
geroutet wird (Merkmal M7 fehlt).


Schließlich wird zur Kommunikation zwischen gemanagtem Objekt bzw. Sensor und
dem Defence Center der SSL-verschlüsselte bidirektionale Kommunikationskanal
verwendet (vgl. NK26, S. 49 – 50, S. 177) oder eine Cloud Communication (vgl.
NK26, S. 1071), was ebenfalls kein Routen eines Pakets an ein Überwachungsgerät
darstellt.


Zwar erwähnt die NK26 (Seite 2145) für ein „inline deployment“ eines Sensors die
Möglichkeit, einen Verkehrsdatenfluss mittels Routen zu beeinflussen, allerdings
fehlt dort jegliche technische Ausgestaltung des Routens insbesondere hinsichtlich
des anspruchsgemäßen Routens des Pakets zu einem Überwachungsgerät gemäß
Merkmal M7.
2.6    Die Druckschrift HLNK1 (Juniper Networks Concepts & Examples Screen
OS Reference Guide Release 6.3.0) sowie die Druckschrift HLNK1a (Juniper
Networks Network and Security Manager Administration Guide), auf die auf Seite
313 in der HLNK1 verwiesen wird, betreffen jeweils ein anspruchsgemäßes
Verfahren mit multiplen, von einem Management-Server verwalteten Security
Gateways (PSGs), das auf einer dynamischen Security Policy basiert und bspw.

                                      - 41 -



zum Schutz eines Netzwerks eingesetzt werden kann, wobei u. a. zur Abwehr von
Netzwerkattacken Virenscans an identifizierten Datenpaketen durchgeführt werden
oder eine Überwachung von Zielpersonen durch Behörden mittels „Lawful Intercept“
vorgeschlagen wird.


Die Zusammenschau der HLNK1 mit der HLNK1a umfasst die folgenden Merkmale
des Anspruchs 1 gemäß Hauptantrag, wobei sowohl die HLNK1 als auch die
HLNK1a ein entsprechendes Verfahren betreffen, das zum o. g. Schutz von Netzwerken dient („traffic alarms …. the following methods“, HLNK1, S. 360; „detection
methods“, S. 406; „packet-filering method“, S. 407; „Unlike an IPS alone, IDP uses
multiple methods to detect attacks against your network and prevent attackers from
gaining access and doing damage“, S. 577; „a robust method for managing multiple
objects“, HLNK1a, S. 21; „Unlike IDS, IDP uses multiple methods to detect attacks
against your network and prevent attackers from gaining access and doing
damage“, S. 45; Merkmal M1).


Die HLNK1/1a zeigen ebenfalls eine Vielzahl von PSGs, die mit einem Security
Policy Management-Server assoziiert sind und von diesem eine dynamische
Security Policy empfangen („Management with the Network and Security Manager
… configures and monitors multiple Juniper Networks security devices … GUI
server … Device Server“, HLNK1, Fig. 92 i.V.m. S. 312 – 313; „You can install the
same security policy on multiple devices“, S. 588; „loading a policy on the ISG-IDP
device“, Fig. 186 i.V.m. S. 650 – 651; „policy manager ... centralized policy
management … create and deploy new policies“, HLNK1a, S. 10 – 11 mit Fig.1 – 2,
S. 28; Merkmal M2).
Die HLNK1/1a lehren Regeln zum Identifizieren von empfangenen Paketen (bspw.
basierend auf einem „Five Tuple“) und darauf anzuwendende Pakettransformationsfunktionen (PTFs) u. a. zum Schutz vom Netzwerken mittels Firewall
und/oder „Deep Inspection (DI)“ („separate a set policy command into two parts—
the core section and the DI component: - The core section contains the source and
destination zones, source and destination addresses, one or more services, and an

                                        - 42 -



action.- The DI component instructs the security device to inspect traffic permitted
by the core section of the policy for patterns matching the attack objects contained
in one or more attack object groups. If the security device detects an attack object,
it then performs the action defined for the corresponding group“, HLNK1, Fig. 141
i.V.m. S. 527; Merkmal M3 erster Teil, Merkmale M4, M5).


Ebenso offenbaren die HLNK1/1a Pakettransformationsfunktionen, die ein Loggen
eines Pakets insbesondere in der Form eines Digest Logs (PDLF) durchführen,
bspw. in der Form eines „Traffic Logs“ oder eines „Event Logs“, wobei bei „Traffic
Logs“ das Protokollieren der Paketinformation abgeschaltet und insbesondere bei
GTP-Verkehr die Menge des zu protokollierenden Payloads konfiguriert werden
kann („Traffic Log … monitor and record traffic that it permits or denies based on
previously configured policies … To log specific traffic, enable logging only on
policies that apply for that traffic“, HLNK1, S. 352; „IDP alarm log entries appear in
the Log Viewer and display the following columns of information“, S. 650; „GTP
Traffic Monitoring … Traffic Logging … specify how much information, basic or
extended, you want about each packet“, S. 1948; „For GTP packets containing user
data, you can specify the number of bytes to log“, S. 1950; „GTP objects“, „lawful
interception“, HLNK1a, S. 381 ff.; „Traffic Logging A security device creates log
entries for GTP events based on the status of the GTP packet. For each event type,
you can also specify how much information (basic or extended) you want about each
packet. To configure GTP logging, select basic or extended for each GTP packet
status: • Log Forwarded Packets—When enabled, the device creates a log entry for
each GTP packet that was transmitted because it was permitted by the security
policy“, S. 384; „Configuring Subscriber Tracing (Lawful Interception) You can
configure a security device to identify subscribers“, S. 386; „Managing Packet Data
in Logs … To store the packet data on the IDP sensor, double-click an IDP sensor,
select Report Settings in the navigation tree, and then uncheck Include packet data
in log. To send the packet data to NSM with the log data, double-click an IDP sensor,
select Report Settings in the navigation tree, and then select Include packet data in

                                        - 43 -



log if it is not already selected“, S. 733 – 734; Unterstreichung hinzugefügt; Merkmal
M3 zweiter Teil, Merkmale M6 und M8 bis M8.2).


Schließlich umfassen die HLNK1/1a mit dem „Policy-Based Routing (PBR)“
ebenfalls ein Routen eines Pakets an ein Überwachungsgerät, wobei als Ausführungsbeispiel eines Überwachungsgeräts bspw. ein Anti-Viren-Scanner (AV)
beschrieben wird („the security device redirects traffic to an external ICAP AV scan
server … Encapsulation of http and SMTP traffic“, HLNK1, S. 467 – 468; „the
complete message is sent to the AV scan engine for virus scanning“, S. 473; „Policy-Based Routing … such as for antivirus (AV), deep inspection (DI) or Web filtering“,
S. 1287 ff.; „selective routing by traffic type“, Fig. 338 i.V.m. S. 1297 – 1298;
„Routing configuration … policy based routing (PBR)“, HLNK1a, S. 89; Merkmal
M7).


Die beiden getrennt veröffentlichten Dokumente HLNK1 und HLNK1a stellen jedoch
keine neuheitsschädliche Offenbarung des Gegenstands des Anspruchs 1 dar. Der
Gegenstand eines Patents ist durch eine Vorveröffentlichung nur dann neuheitsschädlich getroffen, wenn diese ihn aus fachmännischer Sicht unmittelbar und
eindeutig zeigt (st. Rspr., vgl. BGH, Urteil vom 16. Dezember 2008 - X ZR 89/07,
BGHZ 179, 168 Rn. 25 - Olanzapin). Nicht in diesem Sinne Stand der Technik ist
das, was der Fachmann erst aus der Verknüpfung unterschiedlicher Schriften oder
Benutzungen oder durch weiterführende, durch die Quelle lediglich veranlasste
Überlegungen ableiten kann.
Da die Merkmale gemäß Anspruch 1 von den Klägerinnen aus zwei unterschiedlichen Dokumenten entnommen werden, wobei sich u. a. das Routing der
identifizierten Pakete im Speziellen an den Monitor lediglich aus der HLNK1 und die
vom Management-Server empfangene, dynamische Security Policy lediglich aus
der HLNK1a herleiten lassen, fehlt es an dieser Voraussetzung. Daran ändert es
auch nichts, dass die HLNK1 einen Link zur HLNK1a enthält, durch den deren Inhalt
nicht zum Offenbarungsgehalt der HLNK1 wird. Ob es der Neuheit entgegensteht,
dass die anspruchsgemäßen Merkmale, bspw. das Packet Digest Logging (PDLF)

                                      - 44 -



sowie das Routing eines Pakets an ein Überwachungsgerät, in verschiedenen
Ausführungsbeispielen in verschiedenen Kapiteln der HLNK1/1a beschrieben sind,
kann dahinstehen.


2.7   Der weitere eingeführte Stand der Technik gemäß den Druckschriften NK6
bis NK9, NK11 bis NK15, NK21, NK29 sowie HLNK5 liegt weiter ab und und vermag
die Neuheit des Anspruchs 1 nicht in Frage zu stellen. Dazu wurde von den
Klägerinnen auch nichts Gegenteiliges vorgetragen.




3.    Der Gegenstand des Anspruchs 1 gemäß Hauptantrag beruht jedoch jeweils
gegenüber der Druckschrift NK4 und dem Fachwissen, wie es u. a. durch die NK4a
belegt wird, sowie der Zusammenschau der Druckschriften HLNK1 und HLNK1a
nicht auf einer erfinderischen Tätigkeit (Art. 56 EPÜ). Für die nebengeordneten
Ansprüche 12 und 13, die letztlich nur die entsprechende Umsetzung der Verfahrensmerkmale für eine Vorrichtung oder ein System bzw. ein entsprechendes
Computerprogramm      beinhalten,   gelten     die   nachfolgenden   Ausführungen
entsprechend.


3.1   Die Lehre der NK4 unterscheidet sich vom Verfahren gemäß Anspruch 1
lediglich darin, dass sie keinen anspruchsgemäßen Packet Security Management
Server (Merkmal M2 teilweise) offenbart sowie ein Weiterleiten einer Paketkopie
anstelle eines Routens des Pakets an das Überwachungsgerät (Merkmal M7
teilweise) zeigt.


Dem Fachmann ist bekannt, dass die Vielzahl von Routern, Gateways und Switches
im Netzwerk eines Internet Service Providers (ISP) üblicherweise von einem
zentralen   Netzwerk-Management-System         (NMS)    in   einem   Operations   &
Maintenance Center (OMC), umfassend mindestens einen Management Server,
verwaltet werden (Merkmal M2), obwohl für die im Streitpatent, Absatz [0023],
verwendete Definition des Packet Security Management Servers mit „any

                                      - 45 -



computing device configured to communicate a dynamic security policy to a packet
security gateway“ auch bspw. bereits ein herkömmlicher PC mit einer entsprechenden Management-Software zur Bereitstellung der Security Policies genügt.


Das Routen von originalen sowie von duplizierten Paketen an unterschiedliche
Empfänger oder Zieladressen ist bspw. bei broadcast- und multicast-Paketen eine
in Routern/Switches gängige Praxis.


Das Forwarding und das Routing von Daten sind eng miteinander verzahnt. Das
Routing bestimmt den gesamten Weg eines Nachrichtenstroms durch das
Netzwerk; das Forwarding beschreibt hingegen den Entscheidungsprozess eines
einzelnen Netzknotens, über welchen seiner benachbarten Netzknoten er eine
vorliegende Nachricht weiterleiten soll. Während das Forwarding also den
eigentlichen Vorgang des Weiterleitens von Paketen beschreibt, ist Routing der
Prozess der Entscheidungsfindung, auf welchem Interface und an welchen Next
Hop ein Paket weitergeleitet wird. Es stellt für den Fachmann jedoch keine
Herausforderung dar, in einem Layer-3-Gateway oder -Router ausgehend vom
Forwarding der Paketreplik an den Monitor über die externen Schnittstellen gemäß
NK4 zu einem Routing des Pakets an den Monitor gemäß Patentanspruch 1 zu
gelangen (Merkmal M7).




Die Ansicht der Beklagten, dass der Fachmann keine zweite Routinglogik im Packet
Adapter implementieren würde, um die Pakete direkt an den Monitor zu routen,
überzeugt den Senat nicht. Denn die NK4 (vgl. Sp. 35, Z. 10 bis 12) beschreibt
bereits einen Router mit Routinglogik, Routingtabelle und auf einer Policy
basierendem Routing, wobei der Adapter ein entsprechendes Interface zur
Routingtabelle und der Routinglogik des Routers hat, um dem Router die zu
routenden Pakete zu senden, so dass eine redundante Implementierung der
Routingfunktionalität im Packet Adapter überflüssig ist („Further, the adapter 720

                                           - 46 -



includes an interface 736 with the routing table 728 and routing logic 730 of the
router 702 to send packets to be routed. This arrangement logically places the edge
adapter 720 between the network interface 100 and the routing table 728 and
routing logic 730“, NK4, Sp. 35, Z. 24).


Darüber hinaus schlägt die NK4 in einem Ausführungsbeispiel explizit das
Verwenden einer CloudShield CS-2000-Lösung zur Integration in den Edge Server
vor (vgl. NK4, Sp. 33, Z. 48 – 62). Dabei handelt es sich bei der CS-2000 um eine
Open Network Services Platform (ONSP), umfassend Hardware und Software,
wobei ein entsprechendes API den Entwicklern ein schnelles Entwickeln eigener
Applikationen ermöglicht.


Die NK4a (CloudShield CS-2000 with CPOS 3.0.3 Security Target Version 1.0)
beschreibt das entsprechende Betriebssystem CPOS (CloudShield Packet
Operating System) der CS-2000 (vgl. NK4a, S. 7 erster Absatz), das zum Beleg des
fachmännischen Wissens hinsichtlich des fachmännischen Verständnisses der
Lehre der NK4 herangezogen wird. Die NK4 referenziert das Betriebssystem CPOS
bspw. explizit in Spalte 49, Zeilen 38 bis 44.


Ferner zeigt die NK4a eine Vielzahl von Management-Interfaces zum Importieren
der Policies auf das CS-2000-interne ASM (Application Server Modul), wobei bspw.
der Zugriff über eigene Netzwerk-Interfaces wie ein Web Management-Interface,
ein Command Line-Interface, ein SNMP-Interface zu einer „industry-standard server
management application“ und ein GODYN-Interface genannt werden („The ASM
communicates with remote entities via network interfaces which are independent
from the DPPM“, NK4a, S. 8, letzter Absatz und S. 9, dritter Absatz; S. 15, Illustration
2). Gemäß NK4a werden die Regelsätze von einem Administrator definiert (vgl.
NK4a, S. 7), wobei dem Administrator gemäß NK4a auch ein herkömmlicher PC zur
Konfiguration der CS-2000 mit den Security Policies genügt (vgl. NK4a, S. 11, letzter
Absatz). Die NK4a dokumentiert das in der NK4 vorausgesetzte fachmännische

                                            - 47 -



Wissen, dass u. a. mit dem „management device“ bzw. „desktop computer“ gemäß
NK4, Spalte 41, Zeilen 47 bis 57, die Security Policies eingespielt werden können
(Merkmal M2).


Darüber hinaus beschreibt die NK4a ebenfalls ein Umleiten („re-direction“) sowie
ein Routen von Kopien von Paketen durch den Packet Adapter („simple network
tasks such as switching, routing, filtering, QoS (Quality of Service) and traffic
management can be performed in policies“, NK4a, S. 7, erster Absatz; „… the DPPM
supports a Log Accelerator subsystem for automatic replication, re-direction and
packet encapsulation for sending the packet to the log server.“, S. 38, letzter Absatz
bis S. 39, erster Absatz; Unterstreichung hinzugefügt). Die bestimmungsgemäße
Verwendung des in der NK4 offenbarten CS-2000-Systems betrifft gemäß NK4a
auch das Versenden von Paketen an einen Monitor zur Überwachung („The use of
the TOE for traffic management and control, network monitoring and reporting,
network security, and/or security policy enforcement“, NK4a, S. 9, dritter, vierter und
fünfter Absatz; Unterstreichung hinzugefügt; Merkmal M7).


Ferner zeigt die NK4a ebenfalls explizit die anspruchsgemäße Logging-Funktionalität im Sinne einer PDLF als Aktion auf ein identifiziertes Paket („Storing
of information found within the IP packet or auxiliary information“, NK4a, S. 28,
Absatz FDP_IFF.1.2; „O.DPPM.LOG The TOE provides logging capabilities for IP
packets [FDP_IFF.1]“, S. 32; Merkmal M3).
3.2    Die HLNK1/1a lehren wie das Streitpatent das Ausführen multipler Regeln
und voneinander unabhängiger, multipler Pakettransformationsfunktionen auf ein
identifiziertes Paket. Der Senat legt dabei die Entgegenhaltungen HLNK1/1a wie
das Streitpatent aus (s. o. Ziff. I 1.4).


Der Fachmann entnimmt der Zusammenschau von HLNK1/1a, dass auf ein
identifiziertes Paket zum einen eine PDLF mittels Traffic Log oder Event Log
angewendet wird, und zum anderen das gleiche Paket an ein Überwachungsgerät
wie bspw. den Virenscanner bzw. den Lawful Intercept geschickt wird.

                                        - 48 -




4.     Zum Hilfsantrag 7


Der Anspruch 1 in der Fassung gemäß Hilfsantrag 7 ist zwar zulässig, der Anspruch
ist jedoch nicht patentfähig, da sein Gegenstand nicht auf einer erfinderischen
Tätigkeit beruht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a),
Art. 56 EPÜ).


4.1    Der Verfahrensanspruch 1 nach Hilfsantrag 7 enthält gegenüber der Fassung
gemäß Hauptantrag die geänderten Merkmale M3_Hi7 und M4_Hi7 (Änderungen
hervorgehoben):


      M3_Hi7:       „that includes at least one role specifying packetidentiﬁcation criteria and a packet transformation function comprising a
      packet digest logging function to be performed on packets corresponding
      to the packet-identiﬁcation criteria, wherein the plurality of packet
      security gateways collectively provide an entire interface across
      each boundary between a network protected by the plurality of
      packet security gateways and a network other than the protected
      network, and wherein the at least one rule is to be applied to all
      network traffic traversing the boundaries;“


      M4_Hi7:       „receiving, by a packet security gateway of the plurality of
      packet security gateways, packets associated with the network
      protected. by the plurality of packet security gateways and traversing
      the boundary;“


Die beiden Merkmale gemäß Hilfsantrag 7 bilden das mit Anspruch 1 beanspruchte
Verfahren dahingehend weiter aus, dass nunmehr ein Kollektiv bzw. eine Vielzahl

                                      - 49 -



von PSGs umfasst wird, welche das Netzwerk gemeinsam gegen ein äußeres
Netzwerk schützen sollen, wobei wenigstens eine (identische) Regel in alle PSGs
implementiert werden soll, um sämtlichen Verkehr über alle PSGs bzw. Netzwerkgrenzen hinweg in gleicher Weise zu überwachen, wobei die PSGs somit ein
gemeinsames, kollektives Interface bilden sollen.


Die nebengeordneten Ansprüche 12 und 13 werden aufgrund der jeweiligen
Rückbezüge in analoger Weise modifiziert.


4.2   Die mit dem Hilfsantrag 7 verbundenen Änderungen in den Ansprüchen 1,
12 und 13 sind zulässig.


Der Fachmann entnimmt die geänderten Merkmale mit der Vielzahl von PSGs
zwischen zwei Netzwerken, die das Netzwerk gleichermaßen schützen, sowohl dem
Streitpatent als auch der ursprünglichen Offenbarung (vgl. SP, Fig. 8 und Abs.
[0062] - [0064]; „Security policy management server A 816 may ensure that packet
security gateways 808 and 810 protect each of their respective boundaries with
network C 806 in a uniform manner“, NK1a, Fig. 8 und Abs. [76] - [78];
Unterstreichung hinzugefügt). Die Änderungen sind somit zulässig.


4.3   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 7 ist jedoch nicht
patentfähig, da er sich in naheliegender Weise sowohl aus der Lehre der
Druckschriften NK4/4a als auch aus der HLNK1/1a ergibt.


Die Argumentation der Beklagten, die NK4, Figur 4, zeige nur jeweils einen Edge
Server pro Internet Service Provider (ISP), wie bspw. Telekom oder O2, wobei diese
kein einheitliches Network Management aufwiesen und weitere Sicherheitslücken
über die dort gezeigten Edge Caches beständen, überzeugt nicht.


Zur Überzeugung des Senats weist nach fachmännischem Verständnis ein
Netzwerk eines ISPs nicht nur einen einzigen Edge Server/Cache/Router auf, wobei

                                        - 50 -



die multiplen Edge-Geräte eines ISPs üblicherweise zentral über ein gemeinames
Netzwerkmanagementsystem (NMS) verwaltet werden. Die NK4, Spalte 26, Zeilen
52 bis 62, offenbart einen Edge-Server, welcher mit einem Router und einem Edge
Cache integriert ist, um sämtlichen Netzwerkverkehr zu überwachen („intercept all
network traffic“, „the edge server 602 is integrated with a router“, „the edge server
602 is integrated with the edge cache 604“). Darüber hinaus lehrt die NK4, Spalte
28, Zeilen 54 bis 58, sowie Spalte 31, Zeilen 12 bis 16, eine Vielzahl verteilter Edge
Server und Edge Caches, um eine sichere dezentrale Infrastruktur zu gewährleisten
(„multiple dispersed edge servers 602A, 602B and edge caches 604A, 604B
covering the edge 124 of the network 100“, „the provision of numerous distributed
edge servers and edge caches encircling the core of the network 100 provides a
secure decentralized infrastructure“). Schließlich offenbart die NK4, Spalte 29,
Zeilen 35 bis 45 i.V.m. Figur 6, ebenfalls ein hierarchisches System von multiplen
Edge Servern an wesentlichen Schnittstellen des Netzwerks („provided at major
peering points“, „hierarchy of edge servers and caches“). Die Hierarchie der Edge
Server und Edge Caches eines ISPs soll die Antwortzeiten des Systems verringern,
einer Verkehrsüberlast entgegenwirken sowie die Fehlertoleranz beim Ausfall eines
Edge Servers erhöhen, so dass der Fachmann eine Verwendung der im
Wesentlichen gleichen Policy auf den multiplen Edge Servern im hierarchischen
System mitliest, um die Gleichbehandlung der Pakete an einem gemeinsamen,
kollektiven Interface über die verschiedenen Edge Server der Hierarchie zu
gewährleisten.


Im weiteren Kontext der NK4, Spalte 30, Zeilen 21 bis 40, bilden diese multiplen
Edge Server und Edge Caches kleinere Subnetze aus, um Angriffe auf das Gesamtnetzwerk zu erschweren („The edge servers and edge caches are further located to
minimize the number of downstream clients, thereby forming sub-networks which
can isolate and contain network traffic. This allows security services to be provided
by isolating security threats to the smallest possible portion of the network generally
while leaving the remaining portions of the network fully operational.“). Auch hier
erwartet der Fachmann eine Verwendung der im Wesentlichen gleichen Policy auf

                                        - 51 -



den multiplen Edge Servern der jeweiligen Subnetze, um diese bspw. vor einer
Sicherheitsbedrohung zu schützen.


Im Übrigen zeigen die HLNK1/1a ebenfalls multiple PSGs zum Schutz eines
Netzwerks im Sinn des Streitpatents, wobei dort u. a. unter Verwendung von
Templates die identische Policy auf den multiplen Gateways installiert wird („Trust
Zone, Untrust Zone“, HLNK1, Fig. 5 – 6; „Security zones are logical entities to which
one or more interfaces are bound. With many types of Juniper Networks security
devices, you can define multiple security zones, the exact number of which you
determine based on your network needs.“, S. 17; „You can install the same security
policy on multiple devices“, HLNK1, S. 588; „NSM works with networks of all sizes
and complexity. You can add a single device, or create device templates to help you
deploy multiple devices. You can create new policies, or edit existing policies for
security devices.“, HLNK1a, Fig. 1 i.V.m. S. 3; „Centralized Device Configuration:
No matter how large your network, you can use several system management
mechanisms to help you create or modify multiple device configurations quickly and
efficiently at one time: • Templates—A template is a predefined device configuration
that helps you reuse specific information. Create a device template that defines
specific configuration values, and then apply that template to devices to configure
multiple devices at one time. For more flexibility, you can combine and apply multiple
device templates to a single device configuration“, S. 5 – 6; „NSM is a three-tier
management system made up of a user interface (Ul), management system, and
managed devices. The devices process your network traffic and are the
enforcement points that implement your policies“, S. 10; „Devices running JUNOS
Software and managed by NSM … SRX Series Services Gateways … Multiservice
Edge Routers … These routers and gateways offer not only a rich set of routing
protocols and interfaces, but also firewall and IPsec virtual private network
capabilities, providing high levels of security“, S. 16; Unterstreichungen
hinzugefügt).

                                       - 52 -



Darüber hinaus umfasst bspw. ein PSG zumindest zwei virtuelle Router bzw.
virtuelle Systeme („A virtual router (VR) functions as a router …. A security device
supports two predefined virtual routers“, HLNK1, Fig. 4 i.V.m. S. 19 – 20; „vsys“,
HLNK1, Fig. 9 i.V.m. S. 24).


Schließlich umfasst die HLNK1/1a auch Cluster mit multiplen PSGs zu Redundanzzwecken und hoher Verfügbarkeit an einer Netzwerkgrenze, wobei alle PSGs die
gleiche Konfiguration haben („Device Failover … When you configure two security
devices in an NSRP cluster, the primary device device synchronizes all
configuration and state information with the backup device so that the backup device
can become the primary device when necessary“, HLNK1, Fig. 454, S. 1716 ff.;
„Adding Clusters … A cluster consists of multiple devices joined together in a high
availability configuration to ensure continued network uptime. The device
configurations are synchronized, meaning all cluster members share the same
configuration settings, enabling a device to handle traffic for another if one device
fails“, HLNK1a, S. 151 – 152).


Hinsichtlich der unveränderten Merkmale des Anspruchs 1 wird auf die
entsprechenden Ausführungen zum Hauptantrag verwiesen.


4.4   Für die nebengeordneten Ansprüche 12 und 13 gemäß Hilfsantrag 7, welche
die entsprechende Umsetzung der Verfahrensmerkmale in einer Vorrichtung
(„system“) bzw. in einem Computerprogramm („computer program … executed by
one or more processors“) betreffen, gelten die Ausführungen entsprechend.




5.    Zum Hilfsantrag 8


Der Anspruch 1 in der Fassung gemäß Hilfsantrag 8 ist zwar zulässig, der Anspruch
ist jedoch nicht patentfähig, da sein Gegenstand nicht auf einer erfinderischen
Tätigkeit beruht.

                                       - 53 -




5.1    Der Verfahrensanspruch 1 nach Hilfsantrag 8 enthält gegenüber der Fassung
gemäß Hauptantrag die geänderten Merkmale M3_Hi8 und M4_Hi8 (Änderungen
hervorgehoben):


      M3_Hi8:       „that includes at least one role specifying packetidentiﬁcation criteria and a packet transformation function comprising a
      packet digest logging function to be performed on packets corresponding
      to the pacltet-identiﬁcation criteria, wherein one or more packet
      security gateways of the plurality of packet security gateways are
      located at each boundary of a network protected by the plurality of
      packet security gateways and an unprotected network other than
      the protected network, and wherein the at least one rule is
      configured to be applied to all network traffic traversing the
      boundaries via the plurality of packet security gateways;“


      M4_Hi8:       „receiving, by a packet security gateway of the plurality of
      packet security gateways, packets associated with the network protected
      by the plurality of packet security gateways and traversing the
      boundary;“


Der Hilfsantrag 8 mit den geänderten Merkmalen M3_Hi8 und M4_Hi8 basiert im
Wesentlichen auf dem Hilfsantrag 7, wobei M4_Hi8 dem bereits aus dem Hilfsantrag
7 bekannten Merkmal M4_Hi7 entspricht. Im Vergleich mit Hilfsantrag 7 ist in
M3_Hi8 lediglich das Teilmerkmal „collectively provide an entire interface“
gestrichen und durch eine Vielzahl von PSGs platziert an jeder Netzwerkgrenze
ersetzt worden. Die beiden modifizierten Merkmale betreffen hier also eine Vielzahl
von PSGs an jeder Netzwerkgrenze des geschützten Netzwerks, welche an dieser
jeweiligen Netzwerkgrenze das Netzwerk gegen ein äußeres, ungeschütztes
Netzwerk schützen sollen, wobei wenigstens eine Regel in alle PSGs implementiert

                                      - 54 -



werden soll, um sämtlichen Verkehr über diese jeweiligen PSGs an der
Netzwerkgrenze hinweg zu überwachen.


Die nebengeordneten Ansprüche 12 und 13 werden aufgrund der jeweiligen
Rückbezüge in analoger Weise modifiziert.


5.2   Die mit dem Hilfsantrag 8 verbundenen Änderungen in den Ansprüchen 1,
12 und 13 sind zulässig.


Der Fachmann entnimmt die geänderten Merkmale mit der Vielzahl von PSGs
zwischen zwei Netzwerken, welche das Netzwerk gleichermaßen an seiner Außengrenze schützen, sowohl dem Streitpatent als auch der ursprünglichen
Offenbarung. Dort zeigt jeweils die Figur 8 ein Netzwerk A 802, welches mittels den
PSGs 808 und 810 gegenüber dem Netzwerk C 806 geschützt wird, wobei beide
PSGs einen einheitlichen Regelsatz vom Management Server SPM A 816 erhalten
(vgl. SP, Fig. 8 und Abs. [0062] - [0064]; „Security policy management server A 816
may ensure that packet security gateways 808 and 810 protect each of their
respective boundaries with network C 806 in a uniform manner“, NK1a, Fig. 8 und
Abs. [76] - [78]; Unterstreichung hinzugefügt). Die Änderungen sind somit zulässig.


5.3   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 8 ist jedoch nicht
patentfähig, da er sich in naheliegender Weise sowohl aus der Lehre der Druckschriften NK4/4a als auch der HLNK1/1a ergibt.


Insbesondere bedingt das hierarchisches System von multiplen Edge Servern an
wesentlichen Schnittstellen des Netzwerks gemäß NK4, Spalte 29, Zeilen 35 bis 45
i.V.m. Figur 6 ein Verwenden der gleichen Policy auf den multiplen EDGE-Servern,
um im Fehlerfall bzw. bei Überlast die Gleichbehandlung der Pakete an dem
gemeinsamen Interface an der Netzwerkgrenze über die verschiedenen Edge-Server hinweg zu gewährleisten („provided at major peering points“, „hierarchy of
edge servers and caches“, „… handle any overload of one or more downstream

                                        - 55 -



edge servers and edge caches or to handle spill over of capacity or even a complete
failure of one or more edge servers or edge caches.“).


Darüber hinaus zeigen die HLNK1/1a ebenfalls multiple PSGs zum Schutz eines
Netzwerks, wobei dort u. a. unter Verwendung von Templates die identische Policy
auf der Vielzahl von Gateways installiert wird, und wobei zu Redundanzzwecken
und hoher Verfügbarkeit an einer Netzwerkgrenze Cluster mit multiplen PSGs und
jeweils gleicher Konfiguration installiert werden („You can install the same security
policy on multiple devices“, HLNK1, S. 588; „Centralized Device Configuration: …
create or modify multiple device configurations quickly and efficiently at one time: •
Templates - A template is a predefined device configuration that helps you reuse
specific information. Create a device template that defines specific configuration
values, and then apply that template to devices to configure multiple devices at one
time.“, HLNK1a, S. 5 – 6; „Device Failover … When you configure two security
devices in an NSRP cluster, the primary device device synchronizes all
configuration and state information with the backup device so that the backup device
can become the primary device when necessary.“, HLNK1, Fig. 454, S. 1716 ff.;
„Adding Clusters … A cluster consists of multiple devices joined together in a high
availability configuration to ensure continued network uptime. The device
configurations are synchronized, meaning all cluster members share the same
configuration settings, enabling a device to handle traffic for another if one device
fails.“, HLNK1a, S. 151 – 152; Unterstreichungen hinzugefügt).


Im Übrigen gelten die Ausführungen zum Hilfsantrag 7 unter Ziff. 4.3 ebenfalls für
den Hilfsantrag 8.


Hinsichtlich der unveränderten Merkmale des Anspruchs 1 wird zudem auf die
entsprechenden Ausführungen zum Hauptantrag verwiesen.


5.4   Für die nebengeordneten Ansprüche 12 und 13 gemäß Hilfsantrag 8, welche
die entsprechende Umsetzung der Verfahrensmerkmale in einer Vorrichtung

                                       - 56 -



(„system“) bzw. in einem Computerprogramm („computer program … executed by
one or more processors“) betreffen, gelten die Ausführungen entsprechend.


6.     Da der Anspruchssatz gemäß Hauptantrag und den Hilfsanträgen 7 und 8
jeweils als Ganzes verteidigt wird, waren auch seine übrigen Ansprüche für nichtig
zu erklären.




7.     Zum Hilfsantrag 6


Der Gegenstand des mit dem Hilfsantrag 6 zulässig verteidigten Anspruchs 1
erweist sich gegenüber dem im Verfahren befindlichen Stand der Technik als neu
und beruht auch auf einer erfinderischen Tätigkeit.


7.1    Der Verfahrensanspruch 1 nach Hilfsantrag 6 umfasst nunmehr die
Kombination der erteilten Ansprüche 1 und 2 (unter Weglassung der Änderungen
nach den Hilfsanträge 7 und 8), wobei das neue Merkmal M9_Hi6 im Anschluss an
das Merkmal M8.2 hinzugefügt wird (Änderungen hervorgehoben):


      M9_Hi6:       „and   wherein     the      method   further   comprises;
      encapsulating each of the one or more packets corresponding to
      the packet-identification criteria with an Internet Protocol header
      specifying a network address corresponding to the monitoring
      device; stripping, by the monitoring device on a packet-by-packet
      basis, the Internet Protocol header specifying the network address
      corresponding to the monitoring device encapsulating the one or
      more packets comprising the packet-identification criteria; and
      forwarding, by the monitoring device on a packet-by-packet basis,
      one or more packets corresponding to the packet-identification
      criteria toward their respective destinations without the lnternet

                                       - 57 -



      Protocol header specifying the network address corresponding to
      the monitoring device.“


Die identifizierten Pakete sollen demnach vor dem bzw. für das Routen an das
Überwachunsgerät vom PSG unter Verwendung dessen Netzwerkadresse eingekapselt („encapsulating“) werden, wobei das Überwachunsgerät anschließend die
empfangenen Pakete wiederum entpackt („stripping“) und von dort ohne die
Einkapselung direkt an die ursprüngliche Zieladresse weiterleitet („forwarding …
toward their respective destinations“). Nach dem Entfernen der Einkapselung kann
das Paket vom Überwachunsgerät ohne weitere Modifikationen versendet werden,
da im IP-Header des Pakets immer noch die ursprüngliche Zieladresse enthalten
ist. Das Merkmal M9_Hi6 lässt dabei offen, welche Handlungen bzw. Prüfungen das
Überwachungsgerät am Paket durchführt. Im Streitpatent, Absätze [0039], [0052],
[0055] und [0056], wird ein Kopieren oder ein Abspeichern des Pakets bzw. dessen
Inhalts beschrieben, welches dann für eine weitergehende Analyse („subsequent
review or analysis“), für eine Strafverfolgung („law enforcement“) oder für Sicherheitsbehörden („national security authority“) bereitgestellt wird. Mit Merkmal M9_Hi6
wird lediglich eine „Umleitung“ der identifizierten Pakete über das Überwachungsgerät beansprucht, bevor diese von dort letztlich ohne Umweg über den PSG an
ihre ursprüngliche Zieladresse weitergeleitet werden.


7.2    Die mit dem Hilfsantrag 6 verbundenen Änderungen in den Ansprüchen 1,
11 und 12 sind zulässig, denn der Fachmann entnimmt die weitere Ausgestaltung
des Anspruchs 1 mittels Merkmal M9_Hi6 dem Streitpatent, Absätze [0055] und
[0056], Unteranspruch 2 sowie der Offenlegungsschrift NK1a, Absatz [53], wobei
diese Fundstellen jeweils den „multidimensional routing service“ betreffen.


Die Klägerinnen vertreten die Auffassung, dass eine unzulässige Erweiterung
vorliege, da zum einen der Verfahrensschritt des Einkapselns („encapsulating“)
ohne weiteren Bezug zum Routing beansprucht werde und zum anderen die
funktionswesentlichen Merkmale des Speicherns bzw. Kopierens des Pakets im

                                      - 58 -



Überwachungsgerät und ggf. weitere, im „multi-dimensional routing service“
verwendete zusätzliche Parameter nicht umfasst seien. Außerdem ließe der
Anspruchswortlaut offen, dass der entfernte Header immer noch an die ursprüngliche Zieladresse mitgesendet werden könne. Hierbei verkennen die Klägerinnnen
jedoch, dass im vorangehenden Absatz [52] der NK1a der „multi-dimensional
routing service“ ohne ein obligatorisches Speichern/Kopieren des Pakets für ein
beliebiges Netzwerkgerät offenbart wird. Darüber hinaus wird in der NK1a, Absatz
[53] das Kopieren/Speichern im Überwachungsgerät auch lediglich als optional
beschrieben („may be configured to copy the packets“, NK1a, Abs. [53];
Unterstreichung hinzugefügt).


Schließlich wird gemäß dem Wortlaut des Anspruchs 1 ein Weiterleiten des
ursprünglichen Pakets vom Überwachungsgerät an die ursprüngliche Zieladresse
beansprucht („forward … the packets toward their respective destinations“). Die
Ausführungen der Klägerinnen, der entfernte Header („stripped header“) bzw. die
bereits entfernte Einkapselung könne immer noch zusammen mit dem
ursprünglichen Paket an die ursprüngliche Zieladresse mitgesendet werden, sind
dem Wortlaut des Anspruchs nicht zu entnehmen. Der Fachmann erwartet dies bei
der Studie des Streitpatents und den dort beispielhaft genannten Diensten „lawful
intercept“ bzw. „law enforcement“ auch gar nicht, da dies bspw. bei einem „lawful
intercept service“ eine zu überwachende Person auf die Umleitung des Pakets über
das Überwachungsgerät und somit auf die laufende Observierung erst aufmerksam
machen würde.


7.3   Dem Gegenstand von Patentanspruch 1 in der Fassung gemäß Hilfsantrag
6 steht der Nichtigkeitsgrund der fehlenden Patentfähigkeit nicht entgegen, da das
unter Schutz gestellte Verfahren gegenüber dem im Nichtigkeitsverfahren
entgegengehaltenen Stand der Technik – insbesondere hinsichtlich der Druckschriften NK4/4a sowie HLNK1/1a – auf einer erfinderischen Tätigkeit beruht.

                                        - 59 -



Die NK4/4a beschreibt lediglich ein Forwarding des Pakets bzw. einer Replik des
Pakets an ein externes Gerät, wobei das originale Paket im Packet Security
Gateway solange zurückgehalten wird, bis das Gerät nach dem Bearbeiten des
Pakets ein Kommando („command“) zum Freigeben des Pakets an den Packet
Security Gateway zurücksendet. Erst dann wird das dort festgehaltene Paket in
Abhängigkeit vom Analyseergebnis des Monitors vom Packet Security Gateway an
die ursprüngliche Zieladresse weitergeleitet („in response to a command received
from that external device 724 (as determined by its own processing of the copy of
the packet 704), modifying the IP address and payload of the captured packet 704
and releasing the modified packet 704 to the routing logic 730 of the router 702“,
NK4, Sp. 35, Z. 43 – 46, Sp. 39, Z. 13 – 48; „This data includes commands to the
adapter 720, such as to release a buffered packet 704, … the data includes packets
to be delivered to the routing logic 730 of the router 702 for routing onto the network
100“, Sp. 40, Z. 63 – Sp. 41, Z. 22; Unterstreichungen hinzugefügt). Darüber hinaus
lehrt die NK4 im Kontext der Figur 23 i.V.m. Spalte 59, Zeile 60 ff., im Rahmen einer
Aufzählung eine Vielzahl transparenter Netzwerkdienste, worunter u. a. auch ein
„lawful intercept service“ in Spalte 59, Zeile 66 und Spalte 62 Zeile 65 fällt, ohne
jedoch die aufgezählten Dienste im Speziellen näher auszugestalten. Dazu wird
ferner in Spalte 60, Zeile 40 ff., ausgeführt, dass Pakete in der Nähe eines Egress-Routers des Netzwerks abgefangen („interception“) werden, wobei eine Schnittstelle für eine einfache Übergabe der abgefangenen Pakete an ein Gerät und/oder
eine Anwendung eines „application providers“ bereitgestellt wird. Nähere Details
über den Transport der Pakete zum „application provider“ bleiben offen. Es fehlt
zumindest jeglicher Hinweis auf ein Routen sowie eine Einkapselung der Pakete
(„and/or the intercepted packets may simply be passed to the device and/or
application of the application service provider to be processed“, NK4, Sp. 61, Z. 16
– 22; Unterstreichung hinzugefügt). Nach der Evaluierung der identifizierten und
abgefangenen Pakete soll eine entsprechende Handlung („act“) erfolgen, wie bspw.
ein Löschen, Modifizieren oder Erlauben („allowing“), d.h. ein Weiterleiten des
Pakets an die ursprüngliche Zieladresse. Insbesondere soll hierzu die Applikation
ein Ergebnis („result“) oder eine Anweisung („instruction“) zurückmelden (vgl. NK4,

                                      - 60 -



Sp. 61, Z. 29 – 49). Der Fachmann entnimmt auch diesem Ausführungsbeispiel der
NK4, dass zum Abfangen der Pakete im Egress-Router der „packet interceptor
adapter“ gemäß NK4, Figur 7, BZ 720, angewendet wird und dass das Gerät bzw.
die Applikation des „application providers“ analog zu einem externen Gerät gemäß
NK4, Figur 7, BZ 724, agiert.


In der Zusammenschau von NK4 mit der NK4a fehlt somit das direkte Weiterleiten
des Pakets vom Gerät an die ursprüngliche Zieladresse, ohne den Umweg über das
Packet Security Gateway zu nehmen und ohne eine geeignete Signalisierung,
bspw. ein Feedback-Kommando an den PSG, zu benötigen (Merkmal M9_Hi6
zweiter Teil fehlt).


Zwar umfasst die NK4a im Speziellen noch das Einkapseln eines Pakets zum
Zweck des Routings, das Ausführungsbeispiel betrifft allerdings das Routen an
einen Log Server und nicht an ein Überwachungsgerät („the DPPM supports a Log
Accelerator subsystem for automatic replication, re-direction and packet
encapsulation for sending the packet to the log server. The Log Accelerator subsystem provides a hardware co-processor on CloudShield DPPMs that makes
copies of packets and modifies (encapsulates) them for routing, switching and load
balancing without requiring RAVE software replication overhead. This function
offers improved performance for RAVE applications that use the capture port for
logging data by moving the overhead for these functions to hardware“, NK4a, S. 38
unten – S. 39 oben; Unterstreichungen hinzugefügt; Merkmal M9_Hi6 erster Teil
teilweise).


Die HLNK1/1a beschreibt das „Policy based Routing“ (PBR) durch ein Packet
Security Gateway („Juniper Networks security device“, „ICAP client“) an einen
Virenscanner („AV scanner“, „ICAP-Server“) zur Überprüfung auf enthaltene
Schadsoftware, wobei das Paket eingekapselt wird (Merkmal M9_Hi6 erster Teil).
Anschließend schickt der Virenscanner das Endergebnis – also das auf Viren
geprüfte Paket und das Scanergebnis – wieder an den PSG/ICAP-Client zurück,

                                         - 61 -



anstatt anspruchsgemäß die Pakete selbsttätig an die Zieladresse weiterzuleiten
(Merkmal M9_Hi6 zweiter Teil fehlt). Erst der PSG bzw. ICAP-Client routet dann
die virenfreien Pakete an die ursprüngliche Zieladresse („4. The ICAP client sends
the scan data (in encapsulated ICAP format) to the ICAP server and holds the data
in memory until the ICAP server acknowledges receiving it. 5. The ICAP server
returns the scan results with the entire content to the ICAP client. • If a virus is not
found, the traffic is forwarded to its destination“, HLNK1, Fig. 129 Schritte 4 und 5
i.V.m. S. 467 – 468; Unterstreichungen hinzugefügt).


Darüber hinaus lehrt auch keine der anderen im Verfahren befindlichen
Druckschriften das in den Anspruch 1 gemäß Hilfsantrag 6 aufgenommene Merkmal
M9_Hi6.




Die NK12 (RFC 2003) lehrt lediglich das Einkapseln eines Pakets mit einem „outer
UIP header“ für das Routen des Pakets an eine andere als die ursprüngliche
Zieladresse, wobei ein Monitor exemplarisch nicht genannt wird, und somit nur
teilweise der erste Teil des Merkmals M9_Hi6 (vgl. NK12, Seiten 1 und 3).


Das Gleiche gilt für die NK9 („The packet processor 104 may perform other packet
processing operations such as de/encrypting or de/encapsulating a packet“, NK9,
Abs [0018]).


Gemäß NK5, Absatz [0097], kann ein Paket zwar an einen Quarantäneserver
geschickt werden, die NK5 schweigt jedoch hinsichtlich des anspruchsgemäßen
Einkapselns von Paketen gemäß Merkmal M9_Hi6 ersterTeil und des Weiterleitens
des entkapselten Pakets vom Quarantäneserver an die ursprüngliche Zieladresse
gemäß Merkmal M9_Hi6 zweiter Teil.


Die NK7 betrifft ein „lawful intercept capture system“ zur Aufnahme von Daten,
wobei in einem Router anhand der IP-Adresse identifizierte Pakete von Interesse

                                        - 62 -



für die Behörden ohne Einkapselung an ein Aufnahmesystem umgeleitet
(„redirection“) und die Pakete dann aber im Anschluss an die Aufnahme zur „next
hop entity“ oder ggf. an einen Klienten weitergeleitet bzw. geroutet werden („The
lawful intercept capture system may be configured to receive data packets from the
network router and capture them on a storage device, before forwarding the data
packets to the next hop network entity“, NK7, Abs. [0017]; „The next hop network
entity may be one of the clients 102 or any network entity that lies within the data
path between the origination IP address and the destination IP address of the data
packet“, Abs. [0029]). Zwar werden gemäß NK7 die Pakete zumindest vom „lawful
intercept capture system“ in Richtung des ursprünglichen Ziels weitergeleitet, zum
Weiterleiten an die „next hop entity“ ist jedoch stets noch eine Nachschau („Look-Up“) in einer Routingtabelle erforderlich, so dass sich die Zieladresse nicht
zwanglos nach dem Entfernen der (in der NK7 nicht vorhandenen) Einkapselung
unmittelbar ergibt („the lawful intercept capture device performs a look-up on the
routing table 112 of the lawful intercept capture system 108 to determine the next
hop network entity to which the lawful intercept capture device should forward the
data packet“, NK7, Fig.4, BZ 414 i.V.m. Abs. [0065]; Merkmal M9_Hi6 erster Teil
fehlt komplett und zweiter Teil fehlt teilweise).


Zudem geben weder die NK4/4a noch die HLNK1/1a unter Heranziehung der NK7
dem Fachmann irgendwelche Hinweise bzw. Anregungen für die Implementierung
des Merkmals M9_Hi6, ohne selbst erfinderisch tätig zu werden, denn einem „lawful
intercept service“ basierend auf der Kombination von NK4/4a mit der NK7 fehlte
mindestens das anspruchsgemäße Routen eines eingekapselten Pakets (Merkmal
M9_Hi6 erster Teil fehlt).


Der Fachmann schlösse auch eine Kombination der inkompatiblen Verfahren
gemäß der HLNK1/1a und gemäß der NK7 aus, weil die HLNK1/1a bereits den
„lawful intercept service“ unabhängig von einem auf einer Policy basierenden
Routing (PBR) realisiert, indem ein Protokollieren des GTP-Verkehrs im Security
Device selbst durchgeführt wird, wobei das Security Device die protokollierten

                                        - 63 -



Daten an einen externen „lawful interception“ Server sendet und in diesem
Zusammenhang ein Routen der Pakete nicht offenbart wird (vgl. HLNK1, S. 1950 –
1951).


Die Argumentation der Klägerinnen, dass das Streitpatent in den Absätzen [0055]
und [0056] die beiden wirkungsgleichen Alternativen zeige, dass (1) das entkapselte
Paket vom Monitor direkt an die ursprüngliche Zieladresse weitergeleitet werde oder
(2) das Paket zunächst vom Monitor zum PSG zurückgesendet und anschließend
von dort das Paket dann vom PSG an die ursprüngliche Zieladresse weitergeleitet
werde, wobei beide Optionen im Griffbereich des Fachmanns lägen und jeweils zum
gleichen Ergebnis führten, überzeugt den Senat nicht. Das Gleiche gilt für die
Auffassung der Klägerinnen, dass mit den beiden genannten Alternativen eine
reine,   für    den   Fachmann   naheliegende    Auswahlentscheidung       aus     zwei
verschiedenen zur Verfügung stehenden Möglichkeiten vorliege. Insbesondere ist
die Argumentation der Klägerinnen insoweit rückschauend, dass der Fachmann
eine Auswahlentscheidung für eine von wenigen ihm bekannten Alternativen treffe.
Denn sowohl die NK4/4a als auch die HLNK1/1a umfassen ausschließlich die
zweite der genannten Optionen. Lediglich die NK7 zeigt die erste Option zumindest
ansatzweise, jedoch ohne das anspruchsgemäße Einkapseln und Entkapseln sowie
mit dem obligatorischen Zugriff auf eine Routingtabelle. Ein druckschriftlicher Beleg
für die dem Fachmann angeblich als Fachwissen bekannte erste Option liegt nicht
vor. Die Tatsache, dass das Streitpatent beide Möglichkeiten offenbart, gilt nicht als
Nachweis für das Fachwissen (vgl. BGH, Urteil vom 22.05.2007, X ZR 56/03 –
injizierbarer    Mikroschaum).   Nach    Überzeugung      des   Senats     zeigt    die
anspruchsgemäße erste Option nämlich eine strukturell und funktional von der im
Stand der Technik verwendeten Implementierung nach der zweiten Option deutlich
unterscheidbare Arbeitsteilung, d.h. einen unterschiedlichen „Worksplit“ zwischen
PSG und Monitor. Die erste Option führt zu einer Entlastung des PSGs, da der PSG
weder das Paket zwischenspeichern muss, d. h. auf ein aufwändiges Speichermanagement verzichten kann, noch eine kommunikative Verbindung zum Monitor
zwecks Feedback benötigt, da dieser das Paket ohne Rückmeldung zum PSG ans

                                        - 64 -



ursprüngliche Ziel weiterleitet. Auch der Monitor wird entlastet, da der Monitor keine
Kommunikation zur Koordination mit dem PSG führen muss, sondern der Monitor
kann das Paket direkt an einer Layer-3-Routingfunktion einspeisen, die sich um das
Zustellen an die ursprüngliche Zieladresse kümmert.


7.4   Zu den übrigen im Verfahren genannten Druckschriften haben die
Klägerinnen hinsichtlich der erfinderischen Tätigkeit des Hilfsantrags 6 nicht
vorgetragen. Auch der Senat vermag nicht zu erkennen, wie diese im Einzelnen
oder in Kombination zum Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 6
führen können.


7.5   Entsprechendes gilt für die angegriffenen, nebengeordneten Patentansprüche 11 und 12, welche bereits durch ihren Rückbezug auf den patentfähigen
Patentanspruch 1 rechtsbeständig sind. Gegenteiliges haben die Klägerinnen nicht
geltend gemacht.


7.6   Hinsichtlich der ebenfalls angegriffenen Unteransprüche 2 bis 10, welche
vorteilhafte Ausgestaltungen des Erfindungsgegenstands betreffen, gelten auch die
vorstehenden, den Patentanspruch 1 betreffenden Ausführungen entsprechend.
Die Unteransprüche sind ebenfalls bereits durch ihren unmittelbaren oder
mittelbaren Rückbezug auf den patentfähigen Patentanspruch 1 rechtsbeständig.
Auch diesbezüglich haben die Klägerinnen nichts Gegenteiliges vorgetragen.


8.    Wegen der erfolgreichen Verteidigung des Streitpatents mit Hilfsantrag 6 war
über die weiteren Hilfsanträge sowie die nachrangig verteidigten Unteransprüche
nicht mehr zu entscheiden.

                                     - 65 -




                                       III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i.V.m. § 92 Abs. 1 Satz 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i.V.m. § 709 Satz 1 und 2 ZPO.




                                       IV.

                      Rechtsmittelbelehrung



Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Heimen            Bieringer         Schödel          Dr. Ball         Christoph
