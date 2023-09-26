---
ecli: "ECLI:DE:BPatG:2023:260923U5Ni2.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 2/22"
decided: "2023-09-26"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=26&nr=44171&anz=529&pos=390&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-09-26_5_Ni_2_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 2/22 vom 2023-09-26

## Entscheidung

BUNDESPATENTGERICHT

                    IM NAMEN DES VOLKES

                              URTEIL
                                                        Verkündet am
                                                     26. September 2023
5 Ni 2/22 (EP)                                                …

(Aktenzeichen)



                    In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:260923U5Ni2.22EP.0

                                        -2-



                 betreffend das europäische Patent EP 2 433 414
                                (DE 60 2010 059 822)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 26. September 2023 durch den Richter Heimen als
Vorsitzenden sowie die Richter Dr. Meiser, Dipl.-Geophys. Univ. Dr. Wollny, Dr.-Ing.
Ball und den Richter kraft Auftrags Dipl.-Ing. Jürgensen




für Recht erkannt:


I.    Das europäische Patent EP 2 433 414 wird für das Hoheitsgebiet
      der Bundesrepublik Deutschland dadurch teilweise für nichtig
      erklärt, dass seine Patentansprüche folgende Fassung erhalten:


      1.     A system (40, 50) for identifying proximate devices (1, 2)
      arranged for detecting a sensory identifier (ID) and transmitting
      request messages (RQ1, RQ2) comprising representations of the
      detected sensory identifier, the system comprising:


             •    means for correlating representations of the detected
             sensory identifiers from the request messages received from
             the devices (1, 2) so as to match two or more of those devices,
             and
             • means for carrying out an application involving devices that
             have    been   matched    by     said   means   for   correlating
             representations,


        wherein said means for correlating are at least one correlation
      server (5) and said means for carrying out the application are at least

                                  -3-



one application server (6), the at least one correlation server (5) and
the at least one application server (6) being distinct servers,
 wherein the proximate devices (1, 2) are arranged to include, in the
request messages (RQ1, RQ2), an indication of an application to be
executed, the at least one correlation server (5) being configured to
compare the applications indicated by the request messages, and
causing a transmitter (88) to transmit the match message based on
the match to an application server identified by the matching
indications of the application in the matched request messages,
 wherein the match message is transmitted from the at least one
correlation server to the application server through one of the
proximate devices.


2. The system according to claim 1, wherein the correlation server is
configured to generate a session identifier in response to the
detected match and to transmit the session identifier back to the
proximate devices involved in the match, and to generate a further
message specifying the session identifier and identifiers of the
matched devices to the application server.


3. The system according to claim 1, wherein the at least one
application server (6) is arranged for communicating with the devices
(1, 2) through the correlation server (5).


4. The system according to claim 1, comprising a plurality of
application servers for performing mutually different applications, the
request messages each indicating at least one of said applications,
the at least one correlation server (5) being configured to determine
whether the request messages with correlated representations
received from the devices (1, 2) indicate a same one of the
applications and to match the devices (1, 2) only if this is the case.

                                  -4-




5. The system according to claim 4, wherein the correlation server
(5) is configured to transmit a match message to a selected one of
the application servers in response to detection that the request
messages received from the devices (1, 2) contain correlated
representations and indicate a same one of the applications, a
selected one of the application servers being selected according to
whether it performs said same one of the applications.


6. The system according to any one of the preceding claims, wherein
the at least one application server (6) is arranged for communicating
with the devices (1, 2) directly, at least after receiving a match
message indicating the devices based on detection of said
correlation from the correlation server.


7. The system according to any of the preceding claims, wherein the
request messages (RQ1, RQ2) further comprise environmental
information, such as temperature, air pressure, scent and/or location,
and wherein the correlation server (5) is arranged for additionally
correlating the environmental information.


8. The system according to any of the preceding claims, wherein the
sensory identifier (ID) comprises a sound, preferably a sound
produced by tapping the devices (1, 2) together, and/or an image,
preferably a symbol.


9. The system according to any of the preceding claims, wherein the
devices (1, 2) are mobile devices, preferably mobile telephone
devices.

                                    -5-



10. The system according to any of the preceding claims, comprising
at least two correlation servers (5), further comprising at least one
proxy server for routing request messages (RQ1, RQ2) from the
devices (1, 2) to a correlation server (5), the at least one proxy server
preferably being arranged for routing in dependence of the sensory
identifier (ID).


11. The system according to claim 10, wherein the at least one proxy
server is configured to associate each correlation server with a
predetermined range of values of the sensory identifier, a base
station through which the request message is transmitted, a type of
the sensory identifier and/or a combination of part or all of these
properties, and to route each respective request messages (RQ1,
RQ2) from the devices (1, 2) to a selected one or a selected plurality
of correlation servers (5), associated with the range or ranges in
which a value of the sensory identifier, the source cell through which
the respective request message is transmitted, a type of the sensory
identifier and/or a combination of part or all of these properties lies.


12. The system according to claim 10, wherein the at least one proxy
server is arranged for routing an acknowledgement message (AC1)
from a correlation server (5) to a device (1, 2).


13. The system according to any one of the preceding claims,
wherein the request messages (RQ1, RQ2) each comprise at least
one of:


       • a client identity indicating a client device,
       -   an application handle indicating an application program to
           be executed,
       -   a fingerprint vector indicating event data,

                                  -6-



       -   a handling policy indicating a correlation algorithm and/or
           handling instructions, and
       -   a payload containing data to be exchanged.


14. A correlation server for use in the system (1) according to any of
the preceding claims, comprising


  -   a receiver, a memory, a match detector and
  -   a message processor coupled to a receiver, the message
      processor being configured to store data derived from request
      messages received by the receiver in the memory and to cause
      the match detector to compare first representations of a sensory
      identifier in the stored data of the received request messages
      with a second representation of a sensory identifier from a
      subsequently    received    request   message,     wherein    the
      correlation server is configured to compare applications
      indicated by the request     messages, the correlation server
      comprising a transmitter and the message processor is
      configured to cause the transmitter to transmit a match
      message through one of the devices to an application server
      that is distinct from the correlation server and identified by the
      indications of the application in the matched request messages,
      in response to detection of a match between one of the first
      representations and the       second representation and the
      indicated applications, the match message identifying         the
      devices that transmitted said one of the first representations
      and the second        representation, or a session identifier
      associated with these devices.


15. A method of identifying proximate devices (1, 2) arranged for
detecting a sensory identifier (ID) and transmitting request messages

                                   -7-



(RQ1, RQ2) comprising representations of the detected sensory
identifier, the method comprising the steps of:


   •   correlating representations of the detected sensory identifiers
       from the request messages received from the devices (1, 2)
       so as to match two or more of those devices, and
   •   carrying out an application involving matching devices,


wherein said matching is performed by at least one correlation server
(5) and said carrying out the application is performed by at least one
application server (6) the at least one correlation server (5) and the
at least one application server (6) being distinct servers, the least one
correlation server (5) comparing applications indicated by the request
messages, the least one correlation server (5) transmitting the match
message to an application server identified by the matching of the
application in the matched request messages, wherein the match
message is transmitted to the application server through one of the
devices.


16. The method according to claim 15, wherein the request
messages (RQ1, RQ2) further comprise environmental information
from the devices (1, 2), such as temperature, air pressure, scent
and/or location, and wherein the method comprises the further step
of the correlation server (5) correlating the environmental information
in addition to the representations.


17. The method according to claim 15 or 16, wherein the step of
correlating takes previous matches into account.


18. The method according to claim 15, 16 or 17, wherein the sensory
identifier (ID) comprises a sound, preferably a sound produced by

                                        -8-



       tapping the devices (1, 2) together, and/or an image, preferably a
       symbol.


       19. A computer program product for carrying out the method
       according to any of claims 15-18.


       Im Übrigen wird die Klage abgewiesen.


II.    Von den Kosten des Rechtsstreits tragen die Klägerin 1/3 und die
       Beklagte 2/3.


III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des
       jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.




                                    Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents EP 2 433 414 (Streitpatent),
das – unter Inanspruchnahme der Prioritäten der EP 09160930 vom 22. Mai 2009,
der EP 09174329 vom 28. Oktober 2009 und der EP 09179966 vom 18. Dezember
2009 – am 25. Mai 2010 angemeldet worden ist. Die Erteilung des europäischen
Patents ist am 3. Juli 2019 veröffentlicht worden. Das in englischer Sprache
verfasste Streitpatent trägt die Bezeichnung “Servers for device identification
services“, ins Deutsche übersetzt “Server für Vorrichtungsidentifizierungsdienste”.
Es ist in Kraft und umfasst in der geltenden Fassung insgesamt 19 Patentansprüche
mit dem Vorrichtungsanspruch 1 und auf diesen unmittelbar und mittelbar zurückbezogenen Unteransprüchen 2 bis 13, den Vorrichtungsanspruch 14, den nebengeordneten Verfahrensanspruch 15 und auf diesen unmittelbar und mittelbar
zurückbezogenen Unteransprüchen 16 bis 18 sowie den nebengeordneten
Anspruch 19 betreffend ein Computerprogrammprodukt.

                                        -9-




Mit ihrer Klage begehrt die Klägerin die vollständige Nichtigerklärung des
Streitpatents.


Die geltenden Patentansprüche 1, 14 und 15 haben folgenden Wortlaut:


Verfahrenssprache Englisch              Dt.-Übersetzung lt. SP (inkl. Korrektur)
1. A system for identifying proximate   1. System zum Identifizieren
devices,                                benachbarter Vorrichtungen,
arranged for detecting a sensory        die zum Erfassen eines sensorischen
identifier and                          Identifikators und
transmitting request messages,          zum Senden von Anfragemeldungen
comprising representations of the       mit Darstellungen des erfassten
detected sensory identifier,            sensorischen Identifikators eingerichtet
                                        sind,
the system comprising:                  wobei das System Folgendes umfasst:
means for correlating representations   Mittel zum Korrelieren von
of the detected sensory identifiers     Darstellungen der erfassten
from the request messages received      sensorischen Identifikatoren aus den
from the devices so as to match two     von den Vorrichtungen empfangenen
or more of those devices, and           Anfragemeldungen, um zwei oder mehr
                                        dieser Vorrichtungen abzugleichen, und
means for carrying out an application   Mittel zum Ausführen einer Anwendung
involving devices that have been        mit Vorrichtungen, die durch die Mittel
matched by said means for               zum Korrelieren von Darstellungen
correlating representations,            abgeglichen wurden,
wherein said means for correlating      wobei die Mittel zum Korrelieren
are at least one correlation server     mindestens ein Korrelationsserver sind
and                                     und

                                          - 10 -



said means for carrying out the            die Mittel zum Ausführen der
application are at least one               Anwendung mindestens ein
application server,                        Anwendungsserver sind,
the at least one correlation server        wobei der mindestens eine
and the at least one application           Korrelationsserver und der mindestens
server being distinct servers,             eine Anwendungsserver verschiedene
                                           Server sind,
wherein the proximate devices are          wobei die benachbarten Vorrichtungen
arranged to include, in the request        dazu eingerichtet sind, um in den
messages, an indication of an              Anfragemeldungen eine Angabe einer
application to be executed,                auszuführenden Anwendung zu
                                           enthalten,
the at least one correlation server        wobei der mindestens eine der
being configured to compare the            Korrelationsserver dazu konfiguriert ist,
applications indicated by the request      um die durch die Anfragemeldungen
messages,                                  angezeigten Anwendungen zu
                                           vergleichen,
and causing a transmitter to transmit      dass ein Sender die Abgleichsmeldung
the match message based on the             auf der Grundlage des Abgleichs an
match to an application server             einen Anwendungsserver sendet, der
identified by the matching indications     durch die abgleichenden Angaben der
of the application in the matched          Anwendung in den abgleichenden
request messages.                          Anfragemeldungen identifiziert wird.




14. A correlation server for use in the     14. Korrelationsserver zur Verwendung
system according to any of the              in dem System nach einem der
preceding claims, comprising                vorhergehenden Ansprüche,
                                            umfassend:
a receiver, a memory, a match               einen Empfänger, einen Speicher,
detector and                                einen Abgleichsdetektor und

                                           - 11 -



a message processor coupled to a             einen Meldungenprozessor, der mit
receiver,                                    einem Empfänger gekoppelt ist,
the message processor being                  wobei der Meldungenprozessor dazu
configured to store data derived from        konfiguriert ist, Daten zu speichern, die
request messages received by the             aus den vom Empfänger empfangenen
receiver in the memory                       Anfragemeldungen stammen,
and to cause the match detector to           und zu bewirken, dass der
compare first representations of a           Abgleichsdetektor erste Darstellungen
sensory identifier in the stored data of     eines sensorischen Identifikators in
the received request messages with a         den gespeicherten Daten der
second representation of a sensory           empfangenen Anfragemeldungen mit
identifier from a subsequently               einer zweiten Darstellung eines
received request message,                    sensorischen Identifikators aus einer
                                             anschließend empfangenen
                                             Anfragemeldung vergleicht,
wherein the correlation server is            wobei der Korrelationsserver dazu
configured to compare applications           konfiguriert ist, durch die
indicated by the request messages,           Anfragemeldungen angegebene
                                             Anwendungen zu vergleichen,
the correlation server comprising a          wobei der Korrelationsserver einen
transmitter and                              Sender umfasst und
the message processor is configured          der Meldungenprozessor dazu
to cause the transmitter to transmit a       konfiguriert ist, zu bewirken, dass der
match message to an application              Sender eine Abgleichsmeldung an
server that is distinct from the             einen Anwendungsserver sendet, der
correlation server                           sich vom Korrelationsserver
                                             unterscheidet
and identified by the indications of the     und durch die Angaben der
application in the matched request           Anwendung in den abgeglichenen
messages, in response to detection of        Anfragemeldungen identifiziert wird,
a match between one of the first rep-        als Reaktion auf das Erfassen eines

                                        - 12 -



resentations and the second               Abgleichens zwischen einer der ersten
representation and the indicated          Darstellungen und der zweiten
applications,                             Darstellung und den angegebenen
                                          Anwendungen,
the match message identifying the         die Abgleichsmeldung, die die
devices that transmitted said one of      Vorrichtungen identifiziert, die die eine
the first representations and the         der ersten Darstellungen und die
second representation, or a session       zweite Darstellung gesendet haben,
identifier associated with these          oder einen Sitzungsidentifikator, der
devices.                                  diesen Geräten zugeordnet ist.




15. A method of identifying proximate     15. Verfahren zum Identifizieren von
devices                                   benachbarten Vorrichtungen,
arranged for detecting a sensory          die zum Erfassen eines sensorischen
identifier and                            Identifikators und
transmitting request messages,            zum Senden von Anfragemeldungen
comprising representations of the         mit Darstellungen des erfassten
detected sensory identifier,              sensorischen Identifikators eingerichtet
                                          sind,
the method comprising the steps of:       wobei das Verfahren die folgenden
correlating representations of the        Schritte umfasst:
detected sensory identifiers from the     Korrelieren von Darstellungen der
request messages received from the        erfassten sensorischen Identifikatoren
devices so as to match two or more of     aus den von den Vorrichtungen
those devices, and                        empfangenen Anfragemeldungen, um
                                          zwei oder mehr dieser Vorrichtungen
                                          abzugleichen, und
carrying out an application involving     Ausführen einer Anwendung mit
matching devices,                         abgestimmten Vorrichtungen

                                          - 13 -



wherein said matching is performed          wobei das Abgleichen von mindestens
by at least one correlation server and      einem Korrelationsserver ausgeführt
                                            wird und
said carrying out the application is        das Ausführen der Anwendung von
performed by at least one application       mindestens einem Anwendungsserver,
server                                      ausgeführt wird,
the at least one correlation server and     wobei der mindestens eine
the at least one application server         Korrelationsserver und der mindestens
being distinct servers,                     eine Anwendungsserver
                                            unterschiedliche Server sind,
the least one correlation server            wobei der mindestens eine
comparing applications indicated by         Korrelationsserver durch die
the request messages,                       Anfragemeldungen angegebene
                                            Anwendungen vergleicht,
the least one correlation server            wobei der mindestens eine
transmitting the match message to an        Korrelationsserver die
application server identified by the        Abgleichsmeldung an einen durch das
matching of the application in the          Abgleichen identifizierten
matched request messages                    Anwendungsserver die Anwendung in
                                            den abgleichenden Anfragemeldungen
                                            sendet.


Wegen des Wortlauts der abhängigen Unteransprüche 2 bis 13 und 16 bis 18 sowie
des nebengeordneten Anspruchs 19 wird auf die Streitpatentschrift EP 2 433 414
B1 verwiesen.


Die Klägerin macht gegen die geltende Fassung die Nichtigkeitsgründe der
unzulässigen Erweiterung (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 c) EPÜ)
sowie der mangelnden Neuheit und der mangelnden erfinderischen Tätigkeit (Art. II
§ 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 a) i. V. m. Art. 54, 56 EPÜ) geltend.

                                        - 14 -



Sie stützt ihre Klage u. a. auf folgende Unterlagen:


NK4    WO 2010 / 134 817 A2 (Offenlegungsschrift der PCT-Anmeldung),
D1     US 2007 / 0 093 258 A1,
D2     US 2005 / 0 277 472 A1,
D3     US 6,128,660 A,
D4     EP 1 471 710 B1,
D5     US 2007 / 0 174 243 A1,
D6     JOINES, S. et al.: Performance Analysis for Java Websites. Addison Wesley,
       Boston: San Francisco, 2003, ISBN 0-201-84454-0; S. i – vi, 83, 85 - 87, 102,
       103,
D7     WO 03 / 091 894 A1,
D8     US 2006 / 0 206 614 A1,
D9     US 2009 / 0 070 412 A1,
D10    EP 1 374 959 A2,
D11    WO 2009 / 014 438 A1,
D12    EP 2 073 515 A1.


Auf den qualifizierten Hinweis des Senats vom 10. Juli 2023 hat die Beklagte zur
hilfsweisen Verteidigung des Streitpatents in mehreren Schritten insgesamt 20
Hilfsanträge (0a bis 5c) eingereicht, nämlich mit Schriftsatz vom 11. August 2023
die Hilfsanträge 0a, 0b, 1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c, 4a, 4b, 4c, 5a, 5b, 5c und
in der mündlichen Verhandlung vom 26. September 2023 die zusätzlichen Hilfsanträge 1a´, 1b1´, und 1b2´. Der vormalige Hilfsantrag 1 wurde von der Beklagten
durch Hilfsantrag 0a ersetzt.


Der Vorrichtungsanspruch 1 nach Hilfsantrag 0a enthält gegenüber der erteilten
Fassung folgende Änderung (Änderung gegenüber erteiltem Anspruch 1 fettgedruckt bzw. gestrichen):

                                       - 15 -



   „1. A system (40, 50) for identifying proximate devices (1, 2), arranged for
   detecting a sensory identifier (ID) and transmitting request messages (RQ1,
   RQ2), comprising representations of the detected sensory identifier, the system
   comprising:


       •   said devices, wherein said proximate devices are arranged for
           detecting a sensory identifier (ID) and transmitting request
           messages (RQ1, RQ2) comprising representations of the detected
           sensory identifier;
       •   means for correlating representations of the detected sensory identifiers
           from the request messages received from the devices (1, 2) so as to
           match two or more of those devices, and […]“


Der Verfahrensanspruch 15 gemäß Hilfsantrag 0a wird wie folgt geändert:


   „15. A method of identifying proximate devices (1, 2) arranged for detecting a
   sensory identifier (ID) and transmitting request messages (RQ1, RQ2),
   comprising representations of the detected sensory identifier, the method
   comprising the steps of:


   •   detecting a sensory identifier (ID) by said devices and transmitting
       request messages (RQ1, RQ2) comprising representations of the
       detected sensory identifier by said devices;


   •   correlating representations of the detected sensory identifiers from the
       request messages received from the devices (1, 2) so as to match two or
       more of those devices, and […]“


Der Hilfsantrag 0b enthält nur die Änderung in Anspruch 15 gemäß Hilfsantrag 0a,
der Anspruch 1 bleibt – wie die übrigen Ansprüche - gegenüber der erteilten
Fassung unverändert.

                                       - 16 -



Die nächstrangig hilfsweise verteidigte Fassung gemäß Hilfsantrag 1a´ enthält die
identischen Ergänzungen aus Hilfsantrag 0a, jedoch ohne die Streichungen in
Anspruch 1 und 15. Darüber hinaus enthält der Gegenstand nach Hilfsantrag 1a´
jeweils am Ende die folgenden zusätzlichen Merkmale in Anspruch 1


      „wherein the match message is transmitted from the at least one correlation
      server to the application server through one of the proximate devices.“


und in Anspruch 15


      „wherein the match message is transmitted to the application server through
      one of the devices.“.


Ferner enthält der Hilfsantrag 1a´ ein zusätzliches Merkmal in Anspruch 14. Der
Anspruch lautet (Änderung gegenüber erteiltem Anspruch 14 fettgedruckt):


      “14. A correlation server for use in the system (1) according to any of the
      preceding claims, comprising


         -   a receiver, a memory, a match detector and
         -   a message processor coupled to a receiver, the message processor
             being configured to store data derived from request messages
             received by the receiver in the memory and to cause the match
             detector to compare first representations of a sensory identifier in the
             stored data of the received request messages with a second
             representation of a sensory identifier from a subsequently received
             request message, wherein the correlation server is configured to
             compare applications indicated by the request          messages, the
             correlation server comprising a transmitter and the message
             processor is configured to cause the transmitter to transmit a match
             message through one of the devices to an application server that is

                                         - 17 -



               distinct from the correlation server and identified by the indications of
               the application in the matched request messages, in response to
               detection of a match between one of the first representations and the
               second representation and the indicated applications, the match
               message identifying the devices that transmitted said one of the first
               representations and the second representation, or a session identifier
               associated with these devices.”


Gemäß Hilfsantrag 1b1´ entfällt in Anspruch 15 die Änderung aus Hilfsantrag 0a,
während das zusätzliche Merkmal aus Hilfsantrag 1a´ gleich bleibt. Die Ansprüche
1 und 14 sind gegenüber Hilfsantrag 1a´ unverändert.


Gemäß Hilfsantrag 1b2´ entfällt in Anspruch 1 die Änderung aus Hilfsantrag 0a,
während das zusätzliche Merkmal aus Hilfsantrag 1a´ gleich bleibt. Die Ansprüche
14 und 15 sind gegenüber Hilfsantrag 1a´ unverändert.


Gemäß Hilfsantrag 1c enthalten der Anspruch 1 und Anspruch 15 jeweils am Ende
das zusätzliche Merkmal aus Hilfsantrag 1a´ und entsprechen im Übrigen der
geltenden Fassung. Anspruch 14 enthält ebenfalls das zusätzliche Merkmal aus
Hilfsantrag 1a´. Alle sonstigen Ansprüche sind gegenüber der geltenden Fassung
unverändert.


Die nachrangig verteidigte Fassung nach Hilfsantrag 1a entspricht der Fassung des
Hilfsantrags 0a, enthält jedoch die zusätzlichen Merkmale in den Ansprüchen 1, 14
und 15 gemäß Hilfsantrag 1a´.
Die verteidigte Fassung nach Hilfsantrag 1b entspricht der Fassung des
Hilfsantrages 0b, enthält jedoch die zusätzlichen Merkmale gemäß Hilfsantrag 1a´
in den Ansprüchen 1, 14 und 15.

                                      - 18 -



Wegen des Wortlauts der weiteren nachrangig verteidigten Fassungen nach den
Hilfsanträgen 2a bis 5c wird auf die Anlagen zum Schriftsatz der Beklagten vom 11.
August 2023 verwiesen.


Die Klägerin ist der Ansicht, dass die Gegenstände der geltenden Ansprüche 1 und
15 jeweils unzulässig erweitert seien, da sie über den Inhalt der Anmeldung in der
ursprünglich eingereichten Fassung hinausgingen.
Den Gegenständen sämtlicher Ansprüche fehle es an der Patentfähigkeit. Sie führt
dazu aus, der Gegenstand des Anspruchs 1 sei nicht neu gegenüber jeder der
Druckschriften D1 bis D4. Die Klägerin ist dazu u. a. der Meinung, das beanspruchte
System gemäß Anspruch 1 müsse nur dazu geeignet sein, benachbarte Vorrichtungen zu identifizieren, die Vorrichtungen charakterisierten aber nicht das System.
Ferner seien im Stand der Technik bereits ein „sensory identifier“ und
„representations“ gezeigt. Es fehle ferner ausgehend von der Druckschrift D5 bzw.
D11 auch an erfinderischer Tätigkeit. Insbesondere zähle es zum Wissen und
Können des Fachmanns, eine aufgeteilte Serverarchitektur zu verwenden. Dies
gelte auf gleicher Grundlage auch für den Anspruch 15.


Zu den Hilfsanträgen vertritt die Klägerin die Auffassung, die Änderungen gemäß
der Fassung nach den Hilfsanträgen 0a und 0b stellten eine Schutzbereichserweiterung dar, dies gelte auch für die Hilfsanträge 1a´, 1b1´, 1b2´ sowie
1a, 1b und 1c. Der geänderte Gegenstand sei jeweils auch nicht ursprungsoffenbart.
Gegen die Fassung gemäß den Hilfsanträge 1a´, 1b1´und 1b2´ erhebt die Klägerin
den Einwand der Unklarheit. Des Weiteren vertritt die Klägerin die Auffassung, der
jeweilige Gegenstand nach den Hilfsanträgen sei ebenfalls nicht patentfähig.




Die Klägerin beantragt,


      das europäische Patent EP 2 433 414 B1 mit Wirkung für das Hoheitsgebiet
      der Bundesrepublik Deutschland für nichtig zu erklären.

                                         - 19 -




Die Beklagte beantragt,


       die Klage abzuweisen,


       hilfsweise die Klage abzuweisen, soweit sie sich gegen das Streitpatent in
       seiner verteidigten Fassung gemäß einem der Hilfsanträge 0a, 0b, 1a‘, 1b1‘,
       1b2‘, 1c, 1a, 1b, 2a, 2b, 2c, 3a, 3b, 3c, 4a, 4b, 4c, 5a, 5b, 5c, eingereicht mit
       Schriftsatz vom 11. August 2023 und in der mündlichen Verhandlung vom
       26. September 2023 (Anträge 1a‘, 1b1‘ und 1b2‘), richtet.




Die Beklagte verteidigt das Streitpatent in der erteilten Fassung und tritt der Klage
in allen Punkten entgegen. Sie hält die Gegenstände des Streitpatents in der
erteilten Fassung, jedenfalls aber in der Fassung nach einem der Hilfsanträge für
schutzfähig. Alle verteidigten Fassungen seien in den ursprünglichen Anmeldeunterlagen offenbart, eine unzulässige Erweiterung liege nicht vor.
Der Gegenstand des Streitpatents sei gegenüber dem Stand der Technik neu und
erfinderisch. Dem im Verfahren befindlichen Stand der Technik fehlten die
wesentlichen Merkmale der Lehre des Streitpatents, es liege auch von den
vorgetragenen Ausgangspunkten nicht nahe, die vorveröffentlichten Lehren zur
Lösung der erfindungsgemäßen Aufgabe zu kombinieren. Auch entsprechendes
Können und Wissen des Fachmanns, auf welches er zurückgreifen könne, sei
weder belegt noch ersichtlich.
Hilfsweise verteidigt die Beklagte das Streitpatent mit den Hilfsanträge 0a bis 5c (in
der beantragten Reihenfolge). Jede der verteidigten Fassungen sei zulässig, insbesondere sei der jeweilige Gegenstand ursprünglich offenbart und auch patentfähig.
Die Beklagte rügt den Einwand der Unklarheit als verspätet, Unklarheit liege auch
nicht vor.

                                       - 20 -



Wegen der weiteren Einzelheiten des Vorbringens der Parteien wird auf die
zwischen den Parteien gewechselten Schriftsätze nebst Anlagen und den weiteren
Inhalt der Akte Bezug genommen.




                              Entscheidungsgründe


                                          I.


Die Klage ist im tenorierten Umfang begründet, da dem Streitpatent insoweit der
Nichtigkeitsgrund der mangelnden Patentfähigkeit entgegensteht, Art. II § 6 Abs. 1
Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54, 56 EPÜ. In der
beschränkt verteidigten Fassung gemäß Hilfsantrag 1c ist das Streitpatent
rechtsbeständig und die weitergehende Klage abzuweisen.




1.     Zum Streitpatent


1.1.   Das Streitpatent (SP), befasst sich laut Absatz [0001] mit Servern, die Geräte
identifizieren können. Insbesondere befasst es sich mit einem System, das
nahegelegene Geräte identifizieren kann, wobei dieses mindestens einen
Korrelationsserver aufweist, der zu ihm gesandte Geräteidentifikationsdaten
korreliert und mindestens einen Anwendungsserver, der als Folge einer korrelierten
Identifikation eine Anwendung ausführt.


Mobilgeräte, wie Mobiltelefone, PDAs, Laptops und Spielkonsolen besäßen immer
mehr Funktionen. Mobiltelefone ermöglichten nicht nur das Telefonieren, sondern
schlössen einen Taschenrechner, einen Kalender oder Spiele mit ein. Mobiltelefon-Spiele seien typischerweise für einen Spieler ausgelegt und umfassten nur das
Mobiltelefon des Spielers selbst. Jedoch erforderten andere Spiele mehrere
Mitspieler, wobei jeder Spieler sein eigenes Gerät nutze. Bevor ein Multi-Player

                                          - 21 -



Spiel starten könne, müssten die Spieler ausgewählt und ihre jeweiligen Geräte
identifiziert werden (SP, Abs. [0002]).
Es sei möglich, andere mobile / nicht mobile Geräte zu identifizieren, indem eine
Telefonliste genutzt werde, die die Telefonnummern aller anderen Mobilgeräte und
die Namen ihrer Besitzer enthalte. Eine Telefonnummernliste sage jedoch nichts
über die Verfügbarkeit und räumliche Nähe anderer Mobilgeräte aus. Wenn ein
Multi-Player Spiel mit einer Gruppe von Mitspielern gespielt werden solle, die sich
alle in einer gewissen Nähe zueinander befänden (z.B. in Sichtweite), müssten die
Geräte dieser Gruppe auf andere Weise identifiziert werden. Natürlich sei es
möglich, die Nummern der Teilnehmer händisch einzugeben, wenn diese bekannt
seien. Dies sei jedoch aufwändig und fehleranfällig, v.a. wenn die Telefonnummern
dafür laut vorgelesen werden müssten (SP, Abs. [0003]).
Die Nutzung von Bluetooth© zur Identifizierung der Geräte sei auch schwerfällig, da
eine komplizierte Prozedur für die Auswahl eines anderen Gerätes aus einer sog.
„device discovery list“ und ggf. ein Passwort für die Bluetooth-Paarung notwendig
sei. Daher bestehe Bedarf an einem einfachen und effektiven Mechanismus, um
benachbarte Geräte zu identifizieren (SP, Abs. [0004] und [0005]).
Solch ein Identifikationsmechanismus könne auch in anderen Mobilgeräten außer
Mobiltelefonen genutzt werden. Er mag auch nicht nur für Spieleanwendungen zum
Einsatz kommen, weil z. B. PDAs o. ä. für einen Datentransfer (z.B. von Datenfiles,
Kalendereinträgen, etc.) mit anderen Geräten diese zunächst einmal identifizieren
müssten. Der Identifikationsmechanismus werde für Geräte verwendet, die sich
gegenseitig in räumlicher Nähe zueinander befänden, da entfernte Geräte mit
geringer Wahrscheinlichkeit weder in ein Multi-Player Spiel noch in einen Datentransfer eingebunden seien. Insbesondere sei es oft gewünscht, dass u. a. ein
Mitspieler/Gerät zu einem Spiel eingeladen werde, eine elektronische Business-Card ausgetauscht oder eine finanzielle Transaktion ausgeführt werden solle, wenn
das Gerät sich in Sichtweite zu einem anderen Gerät befinde. Damit das
eingeladene Gerät hierfür in Aktion treten könne, müsse es erst identifiziert werden.
Es bestehe Bedarf, dass dies automatisch geschehe und in Folge eine Anwendung/

                                         - 22 -



Dienst (z.B. ein Spiel) für alle identifizierten Geräte aktiviert werde (SP, Abs. [0005]
und [0006]).
Aus der WO 2009 / 014438 (TNO / KPN) sei ein Anwendungsserver bekannt, der
ein Identifikationsverfahren für benachbarte Mobilgeräte nutze. Ein detektierter
Sensor-Identifikator, wie ein bestimmter Klang oder ein bestimmtes Bild, werde
hierzu im Server verifiziert. Solch eine Verifizierung erübrige auf den Mobilgeräten
das Vorhandensein entsprechender Verifikations-Hardware und –Software, was die
Mobilgeräte einfach und kostengünstig halte. Die wechselseitige Identifizierung
ausgehend von diesem bekannten Verfahren werde z. B. für das Initiieren eines
Spiels, einer Transaktion, o. ä. eingesetzt. Diese weiteren Aktivitäten erforderten
das Ausführen bzw. den Betrieb entsprechender Software auf einem Server, der
sinnvollerweise derjenige sein könne, durch den auch die Identifikation durchgeführt
werde. Dies könne jedoch teuer werden, da die entsprechenden Ressourcen dort
vorgehalten werden müssten (SP, Abs. [0007], [0008]).


Als Aufgabe der vorliegenden Erfindung wird in den Absätzen [0009] bis [0011] die
Überwindung der eben genannten Nachteile genannt. Dazu soll ein System und
eine Methode zur Verarbeitung der Identifizierung von Geräten zur Verfügung
gestellt werden, welche/s Server nutzt, die eine verringerte Komplexität aufweisen.
Somit könnten ausgewählte aus einer Vielzahl von Servern unterschiedliche
Anwendungen aufsetzen, die wiederum Geräte entsprechend einer Sensorinformation an den Geräten auswählten, wobei die paarweise Identifizierung von
Geräten, die an einer Anwendung teilnehmen, von einem Anwendungsserver auf
mehrere Server aufgeteilt werden kann.


1.2.   Der erteilte Anspruch 1 hat in englischer Verfahrenssprache mit der
Merkmalsgliederung des Senats, folgenden Wortlaut:


1      A system (40, 50) for identifying proximate devices (1, 2),
1.a    arranged for detecting a sensory identifier (ID) and

                                          - 23 -



1.b    transmitting request messages (RQ1, RQ2), comprising representations of
       the detected sensory identifier,
1.c    the system comprising:
       means for correlating representations of the detected sensory identifiers
       from the request messages received from the devices (1, 2) so as to match
       two or more of those devices, and
1.d    means for carrying out an application involving devices that have been
       matched by said means for correlating representations,
1.e    wherein said means for correlating are at least one correlation server (5)
       and
1.f    said means for carrying out the application are at least one application
       server (6),
1.g    the at least one correlation server (5) and the at least one application server
       (6) being distinct servers,
1.h    wherein the proximate devices (1, 2) are arranged to include, in the request
       messages (RQ1, RQ2), an indication of an application to be executed,
1.i    the at least one correlation server (5) being configured to compare the
       applications indicated by the request messages,
1.j    and causing a transmitter (88) to transmit the match message based on the
       match to an application server identified by the matching indications of the
       application in the matched request messages.



1.3    Als zuständigen Fachmann sieht der Senat einen Informatiker mit
Universitätsabschluss, der über mehrjährige Erfahrung in der Konzeption und
praktischen Umsetzung von Diensten für Clients in einer Client-Server-Architektur
verfügt.


1.4    Der Senat legt den Merkmalen nach Anspruch 1 folgendes Verständnis
zugrunde:

                                         - 24 -



Mit dem Anspruch 1 wird allgemein eine Vorrichtung („system“) beansprucht, um
nahe beieinanderliegende bzw. räumlich „benachbarte“ („proximate“) Geräte bzw.
Vorrichtungen („devices“) zu identifizieren („identify“), ohne dabei zu spezifizieren,
welche Abstände als „benachbart“ („proximate“) gelten (Merkmal 1) und welche Art
der Identifizierung hiermit verbunden ist. Ebenso wenig beinhaltet das Identifizieren
unmittelbar eine Bestimmung des genannten Abstands. Vielmehr geht das
Streitpatent davon aus, dass zu paarende „devices“ bereits benachbart sind (SP,
Abs. [0042], insb.: „to identify the devices, when they are located in each other's
proximity.“). Das Streitpatent führt in Absatz [0016] zum entsprechenden
Verständnis aus, dass hierunter der Vergleich zweier Geräte fällt, die auf eine
bestimmte Weise ähnlich sind, wenn man bestimmte diesen zugeordnete
Kennung(en) o.ä. miteinander in Beziehung setzt. Diese Formulierungen stellen
letztlich darauf ab, z.B. bereits in einer gewissen räumlichen Nähe zueinander
befindliche Geräte zweier Nutzer für eine gemeinsame Applikation wie bspw. ein
Multi-Player-Online-Spiel miteinander zu verbinden bzw. zu paaren (SP, Abs.
[0042]), um so - rein apparativ betrachtet – das gemeinsame Spielen zu
ermöglichen (SP, Abs. [0002], [0003] und [0007]). Die von den gepaarten „devices“
genutzte Applikation lässt der Anspruch 1 jedoch offen, wobei das Streitpatent mit
Musik, Videos, Datenaustausch und Transaktionen weitere Alternativen nennt (SP,
Abs. [0029]).


Um diese Identifikation zu bewerkstelligen, ist das System befähigt, einen sog.
„sensory identifier (ID)“ zu erfassen, wobei die Art der Erfassung im Anspruch offen
bleibt, jedoch die (menschlichen) Sinne („human senses“) betrifft bzw. durch diese
erfolgt (SP, Abs. [0017]; Merkmal 1.a). Die Art sensorischer Kennungen („identifier“)
wird im Streitpatent in den Absätzen [0008], [0017] und [0055] beschrieben (u.a.
„motion/audio/visual identifier“, der als „string of digits“ ausgeführt sein kann). Davon
zu unterscheiden sind sog. „location identifier“ via GPS, die ausdrücklich nicht dem
ID zugerechnet werden (SP, Abs. [0017]). Eine Bestimmung des Orts („location“)
und damit der Nähe bzw. des Abstands oder der Nachbarschaft multipler „devices“
ist gemäß dem Streitpatent optional, so dass eine reine Orts-ID, bspw. generiert mit

                                            - 25 -



GPS, zwar noch zusätzlich im Identifizierungsschritt hinzugezogen werden kann,
jedoch nicht als sensorische Kennung i.S.d. Streitpatents gilt. Die sensorische
Kennung wird im „device“ mit einem für diese üblichen Sensor gewonnen bzw.
detektiert; dabei handelt es sich bspw. um ein Mikrophon für einen Klang/Ton oder
eine Kamera für ein Symbol bzw. einen Barcode (SP, Abs. [0022]). Die „devices“
weisen damit keine räumlich-körperlichen Eigenschaften auf, die auf das System
zurückzuführen sind, sondern sie nutzen sensorisch lediglich die ohnehin in ihnen
implementierte Technik.


Das System ist zudem in der Lage, Verkörperungen/Darstellungen (z.B. „string of
digits“) des „sensory identifiers“ im Rahmen von Anfragemitteilungen (‚request
messages‘) zu versenden (Merkmal 1.b), was laut den o.g. Absätzen des Streitpatents bspw. die Grundlage für das Miteinander-In-Verbindung-Bringen räumlich
sich nahe beieinander befindender - potentieller Spieler und/oder ihrer – Empfangsgeräte darstellt.


Das System weist laut Anspruch 1 hierfür die folgenden beiden Bestandteile auf:


·   Mittel („means“) zum Korrelieren von Darstellungen der erfassten sensorischen
    Identifikatoren aus den von „devices“ empfangenen Anfragemitteilungen
    („request messages“), um zwei oder mehr dieser „devices“ abzugleichen
    (Merkmal 1.c), was letztlich die „Kompatibilität“ der potentiellen Spieler und ihrer
    Geräte unabhängig von der konkreten Grundlage (außer, dass sie mit dem nicht
    weiter spezifizierten „Identifier“ verknüpft ist) betrifft,
       o wobei die Korrelationsmittel durch mindestens einen „correlation server“
           repräsentiert werden (Merkmal 1.e), also einen als Hard- oder Software
           ausgeführten Dienst im Netzwerk, der beide „identifier“ miteinander in
           eine vergleichende Beziehung zu setzen vermag,
·   Mittel („means“), um eine Anwendung („application“) auszuführen, die diejenigen
    „devices“ betreffen, welche von den genannten Korrelationsmitteln als
    zusammenpassend („matched“) ermittelt wurden (Merkmal 1.d), also eine im

                                              - 26 -



    Netzwerk vorhandene Entität, die die beiden „devices“ miteinander verknüpft,
    sofern sie vom „correlation server“ als zusammenpassend bewertet wurden,
       o wobei die Mittel zur Ausführung einer Applikation durch mindestens einen
          „application server“ repräsentiert werden (Merkmal 1.f), also auch hier
          einen als Hard- oder Software ausgeführten Dienst im Netzwerk, der die
          Anwendung ausführen kann,



·   wobei der mindestens eine Korrelationsserver und der mindestens eine
    Applikationsserver einzelne/individuelle („distinct‘) Server sind (Merkmal 1.g),
    also jeweils als selbständige Entitäten anzusprechen sind,


·   wobei die nahe beieinanderliegenden „devices“ in der Lage sind,
       o in    den     Anfragemitteilungen         (‚request    messages“)    die   Angabe
          („indication“)     einer    auszuführenden           Anwendung     einzuschließen
          („include“; Merkmal 1.h), damit z.B. von den miteinander verknüpften
          „devices“ auch dieselbe Applikation ausgeführt - d.h. zum Beispiel
          dasselbe Spiel gespielt - werden kann,


·   wobei der mindestens eine Korrelationsserver ausgestaltet ist,
       o die durch die Anfragemitteilungen angezeigten Anwendungen zu
          vergleichen („compare“; Merkmal 1.i), also z.B. die in der „request
          message“ unterschiedlicher „devices“ mit dort genannten (gewünschten)
          Spieleanwendungen zu vergleichen,
       o dass     er       einen     Sender      („transmitter“)   dazu    veranlasst,   die
          Übereinstimmungsmeldung, die auf der vorangegangenen Untersuchung
          (vgl. Merkmal 1.d) basiert, an einen Anwendungsserver zu senden, der
          durch die „matching indications“ der Anwendung in den hierauf
          untersuchten Abfragemeldungen als Anbieter identifiziert wurde, damit in
          Folge bspw. der Server - der z.B. für ein Multi-Player-Game die

                                       - 27 -



          entsprechende Anwendung anbietet - die besagte Anwendung für die
          gematchten „devices“ zur Verfügung stellt (Merkmal 1.j).


Für die Auslegung der gleichlautenden Merkmale der nebengeordneten Ansprüche
14 und 15 gelten entsprechende Überlegungen.




1.5   Es kann im Ergebnis dahinstehen, ob die angegebenen drei Prioritätsanmeldungen vom Streitpatent wirksam in Anspruch genommen werden können,
da die zur Bewertung der Patentfähigkeit in diesem Verfahren in Betracht
kommenden Druckschriften (vgl. folgende Abschnitte) jeweils vor dem frühesten
Prioritätsdatum der NK5 veröffentlicht worden sind; damit ist diese Frage nicht entscheidungserheblich. Die Klägerin hat dazu vorgetragen, dass in keiner der für die
Priorität in Anspruch genommenen Patentanmeldungen die Merkmale 1.h, 1.i und
1.j gemäß obiger Gliederung des Anspruchs 1 unmittelbar und eindeutig offenbart
seien. Gleiches gelte für die entsprechenden Merkmale des Anspruchs 14.


Beim jeweiligen Gegenstand der Patentanmeldungen (NK5, NK6 und NK7) handelt
es sich zur Überzeugung des Senats nicht um dieselbe Erfindung wie sie das
Streitpatent beschreibt. In ihnen werden weder ein „message processor 82“ noch
eine „message“ bzw. ein „match detector 86“ erwähnt. Daher wird auch deren
Funktionalität im Bauteilverbund eines Systems an keiner Stelle thematisiert. Diese
Funktionalitäten haben jedoch zusammen mit den o.g. Bestandteilen zumindest
Eingang in den nebengeordneten Anspruch 14 gefunden.


1.6   Eine unzulässige Erweiterung ist mit der erteilten Fassung des Anspruchs 1
zur Überzeugung des Senates nicht verbunden.
Der Anspruch 1 ist in seiner Sachaussage als Ganzes zu betrachten und nicht die
Merkmale 1.h bis 1.j in isolierter Form. Daraus geht hervor, dass bereits in den
Merkmalen 1.c und 1.d das „matching“ der „devices“ anhand des sensorischen
Identifiers erfolgt (vgl. Merkmal 1.d, insb; „… carrying out an application involving

                                        - 28 -



devices that have been matched ...“), und dass das Wort „wherein“ gemäß Merkmal
1.h nurmehr näher spezifiziert, dass die „matching“- Nachricht nur bei Gleichheit der
Applikationsangabe in der Request-Message an den Applikationsserver ausschließlich für die bereits als benachbart identifizierten Geräte gesendet wird.


Somit beansprucht der Anspruch 1 sowohl das Korrelieren der Geräte als auch der
jeweils von den Geräten angeforderten Applikation. Dies ist so auch für ein
separates „device matching“ (NK4, S. 4, Z. 4 - 10; S. 6, Z. 26 ff; Anspruch 14) und
ein separates „application matching“ ursprungsoffenbart (NK4, S. 4, Z. 4 - 10; S. 18,
Z. 1 ff).


Eine unzulässige „Zwischenverallgemeinerung“ liegt ebenfalls nicht vor, da in der
Ursprungsanmeldung kein anderer oder weiterer Bestandteil des Korrelationsservers beschrieben ist, der die beanspruchten Maßnahmen (Vergleichen bzw.
Senden) auszuführen vermag, und der „message detector“ integraler Bestandteil
des Korrelationsservers ist.


1.7     Der Gegenstand des erteilten Anspruchs 1 ist gegenüber der Lehre der
Druckschriften D1 bis D4 neu (Art. 54 EPÜ), denn es fehlt jeder derselben jeweils
mindestens eines der Merkmale, die im Anspruch 1 enthalten sind.


1.7.1 Die Druckschrift D1 (US 2007 / 0 093 258 A1) lehrt ein System, mit dem für
mobile Geräte so genannte „resource matching services“ angeboten werden. Diese
Dienste zeigen einem Nutzer auf Basis bestimmter eigener Eigenschaften
Präferenzen und/oder auf Basis eines aktuellen Aufenthaltsortes einen spezifischen
Inhalt über ein kabelloses Netzwerk an. Ein Nutzer kann dabei mit einer oder
mehreren Ressourcen für den Inhalt „gematcht“ werden. Ressourcen umfassen z.B.
angepasste Werbung, andere in seiner Nähe befindliche Nutzer, Angebote naher
Geschäfte, etc. (D1, Fig. 1 i.V.m. Abstract, Abs. [0002], [0005]).

                                        - 29 -



Somit ist aus dieser Druckschrift prinzipiell ein System zum Identifizieren benachbarter Vorrichtungen bekannt (D1, Fig. 1 und 2 i.V.m. Abs. [0022], insb.:
„…configured to match a user with one or more resources … Such resources include
… (4) locating a nearby service or store.“, (Unterstreichung hinzugefügt); Merkmal
1), jedoch ist dort nirgends davon die Rede, dass es hierfür des Erfassens eines
sensorischen Identifikators i.S.d. Streitpatents bedarf, oder dieses in technisch
sinnvoller Weise eingebunden werden sollte (Merkmal 1.a fehlt).
Es ist aus dem Sachgehalt der dortigen Figuren 1 und 2 auch ein Datenaustausch
zwischen den „Wireless Terminals A-N“, den „Base Stations A-M“ und dem „backend operations system 114“ bekannt, wobei zwangsläufig mit dem Senden von
Datenpaketen auch „messages“ i.S.d. Streitpatents verbunden sind. Da aber in
dieser Druckschrift kein ID offenbart ist, kann hier auch keine „representation“
desselben in dieser „message“ enthalten sein, weshalb dieses Merkmal nicht
vollständig aus der D1 hervorgeht (Merkmal 1.b fehlt teilweise).
Mit derselben Begründung kann in logischer Folge hier auch keine Korrelation
anhand einer bzw. mehrerer IDs vorgenommen werden, wobei jedoch Korrelationsserver i.S.v. Servern, die ein Matchen (eine Basis hierfür ist nicht genannt)
durchführen können, mit der „matching engine 118“ im „back-end operations system
114“ vorhanden sind (D1, Fig.1 i.V.m. Abs. [0046]; Merkmal 1.c fehlt teilweise,
Merkmal 1.e).
Mittel zum Ausführen einer Anwendung auf (jedoch nicht auf Basis einer ID i.S.d.
SP) als zusammenpassend ermittelten („gematchten“) Geräten mittels mindestens
eines Anwendungsservers sind in der D1 in vergleichbarer Form mit den
„application servers 116“ im „back-end operations system 114“ gezeigt (D1, Fig.1;
Merkmal 1.d fehlt teilweise, Merkmal 1.f).
Dass die eben genannten „application servers 116“ und die „matching engine 118“
jeweils als einzelne Entitäten vorgesehen sind, ist aufgrund ihrer Darstellungsweise
in der Figur 1 explizit gezeigt (Merkmal 1.g).
Eine Anwendungskennung („indication of an application to be executed“) als
Bestandteil einer „request message“ i.S.d. Streitpatents ist in dieser Druckschrift
weder explizit benannt noch thematisiert, und ist auch nicht implizit mitzulesen.

                                        - 30 -



Obwohl in der Lehre der D1 zwar seitens der „match engine 516“ der Figur 5 den
Nutzer charakterisierende Daten („criteria“) – z.B. basierend auf „entertainment
preferences“ des Nutzers, die auf geeignete Weise der „engine“ bekannt geworden
sein müssen – zugrunde gelegt werden, schweigt sich die D1 jedoch darüber aus,
wie eine konkrete „message“ seitens des Nutzers zur Ausführung einer „application“
aufgebaut ist (Merkmal 1.h fehlt). Ein Vergleich – wie etwa „entertainment“ zuzurechnende Online-Spiele (auch wenn es auf diese Ausgestaltung – vgl. obige
Auslegung – nicht ankommt) – ist zumindest implizit aus der D1 bekannt oder in
dieser angelegt (D1, Fig.1 i.V.m. Abs. [0046], insb.: „… match the user with other
user based one [sic!] or more criteria (e.g., … entertainment preferences, business
networking opportunities, etc.). The match engine 516 contains a built-in matching
algorithm that supports matching using resource-based and/or location-based data
and provides matches for any user-defined "resource" to another "resource" …“,
(Unterstreichungen hinzugefügt); Merkmal 1.i).
Gemäß Ausführungsbeispiel, wie es der Figur 6 i.V.m. dem Absatz [0060] zugrunde
liegt, ist nach dem Matchen keine „message“ an einen Anwendungsserver i.S.d.
Streitpatents vorgesehen, sondern nur an den dortigen Nutzer (D1, Fig. 6, BZ 608).
Zwar mögen im Ausführungsbeispiel der Figur 5 i.V.m. den Absätzen [0040] bis
[0042] prinzipiell auch andere Kommunikationswege vorgesehen sein, jedoch ist
der D1 für deren explizite Nutzung im Sinne des Anspruchs jedenfalls nichts
unmittelbar und eindeutig zu entnehmen (Merkmal 1.j fehlt).


Damit sind im Ergebnis aus der Druckschrift D1 nicht sämtliche Merkmale des
Gegenstands des Anspruchs 1 bekannt.


1.7.2 Die Druckschrift D2 (US 2005 / 0 277 472 A1) thematisiert über ein spezielles
System u.a. von Servern („gaming servers“, „lobby server“, „billing server“, etc.) das
Generieren von Einkünften seitens eines Online-Spieleanbieters über Nutzer dieser
Spiele, die mit netzwerkfähigen Geräten (bevorzugterweise „mobile devices“) an
diesen teilnehmen. Die „lobby server“ simulieren ein so genanntes „virtual
environment 300“ (D2, Fig. 3), in dem sich potentielle Spieler treffen können.

                                         - 31 -




Somit ist aus dieser Druckschrift zwar prinzipiell ein System zum Identifizieren
benachbarter Vorrichtungen bekannt, wenngleich eine unmittelbare Nähe derselben
nicht konkret thematisiert wird (D2, Fig. 1 und 3 i.V.m. Abs. [0030], insb.: „… As a
matching server, the lobby server 104 can automatically connect a first player with
a second player automatically based upon criteria such as player ranking, …
location, or any other suitable criteria for matching players. …“, (Unterstreichung
hinzugefügt); Merkmal 1), jedoch ist dort nirgends dokumentiert, dass es hierfür des
Erfassens eines wie auch immer gearteten sensorischen Identifikators i.S.d.
Streitpatents bedarf, oder dieses in technisch sinnvoller Weise eingebunden werden
sollte (Merkmal 1.a fehlt).
Es ist dem Sachgehalt der Figuren 1 bis 3 ein nicht weiter konkretisierter
Datenaustausch, z.B. für das „mobile device 108“, über die „game and lobby servers
102, 104“ zu entnehmen, was im gegebenen technischen Kontext mit dem Senden
von als „messages“ zu verstehenden Datenpaketen verbunden sein kann; da aber
aus dieser Druckschrift kein ID i.S.d. Streitpatents bekannt ist, kann hier auch keine
„representation“ desselben in dieser „message“ enthalten sein, weshalb dieses
Merkmal nicht vollständig aus der D2 hervorgeht (Merkmal 1.b fehlt teilweise).
Mit derselben Begründung kann in logischer Folge hier auch keine Korrelation
anhand    einer bzw.    mehrerer IDs vorgenommen werden, wobei jedoch
Korrelationsserver i.S.v. Servern, die ein Matchen (eine Basis hierfür ist nicht
benannt?) durchführen können, mit den „lobby servern 104“ vorhanden sind (D2,
Fig.1 i.V.m. Abs. [0030], [0037]); Merkmal 1.c fehlt teilweise, Merkmal 1.e).
Mittel zum Ausführen einer Anwendung auf (jedoch nicht auf Basis der ID i.S.d. SP)
gematchten Geräten mittels mindestens eines Anwendungsservers, sind in der D2
in vergleichbarer Form mit den dortigen „game servers 102“ gezeigt (D2, Fig.1 i.V.m.
Abs. [0031]; Merkmal 1.d fehlt teilweise, 1.f).
Dass die eben genannten „game server 112“ und „lobby server 114“ als einzelne
Entitäten vorgesehen sein können, ist aufgrund ihrer Darstellungsweise jedenfalls
in der Figur 1 angelegt (Merkmal 1.g).

                                       - 32 -



Eine Anwendungskennung i.S.d. Streitpatents als Bestandteil einer „request
message“ ist der D2 zwar nicht explizit zu entnehmen, ist aber implizit in den
Absätzen [0031] und [0037] (insb.: „… The matching server runs an application that
matches players wanting to play a particular game with other players wanting to play
the same game. ...“, Unterstreichungen hinzugefügt) als funktional notwendig
mitzulesen, da der Server sonst keine Kenntnis von den Wünschen der Spieler
erhalten könnte (Merkmal 1.h).
Damit ist auch deren Vergleich zumindest implizit aus der D2 bekannt oder in dieser
angelegt (D2, Fig. 1 i.V.m. Abs. [0031], [0037]; Merkmal 1.i).
Gemäß dem Ausführungsbeispiel der Figur 1, ist in der D2 auch eine „message“ an
einen Anwendungsserver nach dem Matchen an den dortigen Nutzer zu entnehmen
(D2, Fig. 1 i.V.m. Abs. [0037], insb.: „… Once players are matched up, the host
device addresses are exchanged between either the computers 106 or mobile
devices 108 along with a game instance identification. The computers 106 or mobile
devices 108 then contact the game server 102.“, (Unterstreichung hinzugefügt);
Merkmal 1.j).


Damit sind im Ergebnis aus der Druckschrift D2 ebenfalls nicht alle Merkmale des
Gegenstands des Anspruchs 1 bekannt.


1.7.3 Aus der Druckschrift D3 (US 6,128,660 A), die in der zuvor genannten
Druckschrift D2, Absatz [0006] als Stand der Technik zitiert wird, ist ein so
genanntes    „network   match    making    system“   bekannt,    um   Nutzer   einer
netzwerkbasierten „multi-user application“ aufeinander abzustimmen („to match
users“). Jeder dieser Nutzer ist mit einem Client im Netzwerk assoziiert. Die Clients
werden zum Matchen auf Basis verschiedener Eigenschaften von Nutzern, Clients,
Servern und/oder ihrer Kommunikationsverbindungen ausgewählt. Ein so
genannter „match maker“ empfängt eine Fülle von Anfragen von Clients und
Servern und wählt jeweils passende Clients und Server für die Durchführung einer
„multi-user application“ aus.

                                       - 33 -



Dieser Druckschrift kann ein System zum Identifizieren benachbarter Vorrichtungen
nicht entnommen werden, da die Nähe von Geräten aller Art hier nicht weiter
thematisiert wird, und nur allgemein das Matchen von Vorrichtungen u.a. zum
Durchführen    von    gemeinsamen      Videokonferenzen,      Online-Spielen,      o.ä.
beschrieben wird (D3, Sp. 1, Z. 10 - 20; Sp. 2, Z. 51 - 67); Merkmal 1 fehlt); es ist
in der D3 auch nirgends dokumentiert, dass es hierfür des Erfassens eines
sensorischen Identifikators i.S.d. Streitpatents bedarf, oder dieses in technisch
sinnvoller Weise eingebunden werden sollte; vielmehr werden dort nur allgemein
„user/client/server attributes“ angesprochen (D3, Sp. 2, Z. 51 - 67; Merkmal 1.a).
Den Flussdiagrammen aller Figuren der D3, die lediglich Ausführungsbeispiele,
aber keinen allgemeinen Aufbau des vorgestellten Systems wiedergeben, sind eine
Fülle von Datenwegen zwischen Einzelkomponenten des Systems zu entnehmen,
die „messages“ auch i.S.d. Streitpatents zu übermitteln vermögen (D3, Fig. 8 mit
„CL10“ („client program“) und „MM“ („match maker“), wobei unter BZ 110
beschrieben steht: „REQUEST MM FOR CREATION OF GAME OFFER,
MESSAGE INCLUDES CL10 RELATED ATTRIBUTES“). Da aber aus der D3 kein
ID i.S.d. Streitpatents bekannt ist, kann hier auch keine „representation“ desselben
in dieser „message“ enthalten sein, weshalb dieses Merkmal nicht vollständig aus
der D3 hervorgeht (Merkmal 1.b fehlt teilweise).
Mit derselben Begründung kann in logischer Folge hier auch keine Korrelation
anhand einer bzw. mehrerer IDs vorgenommen werden, wobei jedoch ein
Korrelationsserver i.S.v. einem Server, der ein Matchen (eine Basis hierfür ist nicht
benannt) durchführen kann, mit dem „match maker (MM)“ gegeben ist (D3, Sp. 2,
Z. 51 - 56 i.V.m. Sp. 6, Z. 59 - 65); Merkmal 1.c fehlt teilweise, Merkmal 1.e).
Mittel zum Ausführen einer Anwendung auf (jedoch nicht auf Basis der ID i.S.d. SP)
gematchten Geräten mittels mindestens eines Anwendungsservers, sind in der D3
in vergleichbarer Form mit den dort genannten „game servers“ bzw. dem „multi-user
application server“ gezeigt (D3, Sp. 12, Z. 53 i.V.m. Anspruch 23; Merkmal 1.d fehlt
teilweise, Merkmal 1.f).
Dass die eben genannten Server auch als einzelne Entitäten vorgesehen sein
können, ist explizit dem dortigen Anspruch 23 zu entnehmen (D3, Anspruch 23,

                                         - 34 -



insb.: „A method for a matchmaker server to match a plurality of client computers
and one multi-user application server in a computer network having a plurality of
multi-user application servers …“, (Unterstreichungen hinzugefügt); Merkmal 1.g).
Eine Anwendungskennung i.S.d. Streitpatents als Bestandteil einer „request
message“ ist der D3 zwar nicht explizit, aber der prinzipiellen Lehre der D3 jedoch
zumindest bezüglich der Grundvoraussetzung zum Matchen von Clients bzw.
Nutzern und ihren Geräten und dem letztlichen Ausführen einer Applikation zu
entnehmen (D3, Sp. 2, Z.51 – 67, insb.: „The network match maker matches clients
and a server into matched Sets by comparing the attributes of the user, the client,
the Server and the properties of the network links between them to the requirements
of the application. … Client attributes describe the capabilities of the client computer
System. The performance of the client computer, the type and performance of its
network link and the types and versions of the networked applications that are
installed on it are all reasonable examples of client attributes.“, (Unterstreichungen
hinzugefügt); Merkmal 1.h).
In direkter Folge dieser Vorgehensweise ist auch ein anspruchsgemäßer Vergleich
aus der D3 bekannt (D3, Sp. 6, Z. 46 - 58, insb.: „… A user specifies an application
to run and requests an automatic match. The network match maker looks at the
users requesting an automatic match of the same application and attempts to
organize them into matched sets. …“; Merkmal 1.i).
Gemäß der Lehre der D3 ist dieser zumindest implizit auch eine „message“ an einen
Anwendungsserver nach dem Matchen an den dortigen Nutzer zu entnehmen (D3,
Sp. 7, Z. 7 – 10, insb.: „…When a particular automatic match offer contains enough
clients as required by the attributes, the match maker causes an instance of the
application to be launched. ...“, (Unterstreichung hinzugefügt)), da ein solches
Vorgehen ohne eine entsprechende gesendete Anweisung funktional nicht möglich
ist (Merkmal 1.j).


Damit sind im Ergebnis aus der Druckschrift D3 ebenfalls nicht alle Merkmale des
Gegenstands des Anspruchs 1 bekannt.

                                          - 35 -



1.7.4 In der Druckschrift D4 (EP 1 471 710 B1) wird auf Basis von sog. „proximity
measures“ zwischen den Geräten bei Onlinespielen das Matchen derselben
thematisiert    (D4,   Abs.   [0001]).   Die   Netzwerklatenz   aufgrund    räumlicher
Entfernungen o.a. limitierender Eigenschaften stellt bei derartigen Spielen einen
beschränkenden Faktor dar, weshalb mit der Lehre der D4 ein verbessertes
„matchmaking system“ zum den jeweiligen Spieleanforderungen angepassten
Matchen von Teilnehmern vorgestellt wird.


In der Lehre dieser Druckschrift wird die Nähe von Geräten aller Art thematisiert und
allgemein das Matchen von Vorrichtungen zum Durchführen von Online-Spielen mit
mehreren Spielern (D4, Abs. [0012], [0020], [0025], [0027]), wobei eines der hierfür
relevanten Attribute die so genannte „proximity measure“ von Geräten darstellt (D4,
Abs. [0032] i.V.m. [0038]; Merkmal 1).
Wie im Rahmen der anderen zur Neuheit abgehandelten Druckschriften wird auch
in dieser kein sensorischer Identifikator i.S.d. Streitpatents thematisiert, sondern nur
ein nicht weiter spezifizierter „request to join the game“ (D4, Abs. [0032]) genannt,
um in den dort beschriebenen Matchingprozess einzusteigen (Merkmal 1.a fehlt).
Es sind dem Sachgehalt der Figuren 1, 2, 6 und 7 zwar verschiedene schematisch
dargestellte Kommunikationswege („LAN“, „System Bus“, etc.) zwischen den jeweils
zusammenwirkenden Komponenten (z.B. „match making system“, „computing
device“) zu entnehmen, was im gegebenen technischen Kontext mit dem Senden
von als „messages“ zu verstehenden Datenpaketen verbunden ist; da aber aus
dieser Druckschrift kein ID i.S.d. Streitpatents bekannt ist, kann hier auch keine
„representation“ desselben in dieser „message“ enthalten sein, weshalb dieses
Merkmal auch nicht vollständig aus der D4 hervorgeht (Merkmal 1.b fehlt
teilweise).
Mit derselben Begründung wird hier auch hier keine Korrelation anhand einer bzw.
mehrerer IDs vorgenommen, wobei jedoch mindestens ein Korrelationsserver (D4,
Fig. 7, „match making system“ mit „match module“), der ein Matchen durchführen
kann, gezeigt ist (D4, Fig.7 i.V.m. [0058], [0063]); Merkmal 1.c fehlt teilweise,
Merkmal 1.e).

                                          - 36 -



Mittel zum Ausführen einer Anwendung auf (jedoch nicht auf Basis der ID i.S.d. SP)
gematchten Geräten mittels mindestens eines Anwendungsservers, sind in der D4
in zum Anspruch vergleichbarer Form aufgeführt (D4, z.B. Abs. [0020], insb.: „… a
game console incorporating additional functionality (e.g., … a server computer, …“);
Merkmal 1.d fehlt teilweise, 1.f).
Dass die eben genannten Komponenten als einzelne Entitäten vorgesehen sein
können, ist ebenfalls bekannt (D4, Abs. [0024]; Merkmal 1.g).
Eine Anwendungskennung i.S.d. Streitpatents als Bestandteil einer „request
message“ ist zwar auch der D4 nicht explizit zu entnehmen, ist aber implizit in den
Absätzen [0032] und [0038] (insb.: „… The matching server runs an application that
matches players wanting to play a particular game with other players wanting to play
the same game. ...“, Unterstreichungen hinzugefügt) als funktional notwendig für die
dortige Lehre angelegt (Merkmal 1.h).
Damit ist auch deren Vergleich zumindest implizit aus dieser Druckschrift bekannt
(D4, Abs. [0058], [0063] i.V.m. Abs. [0027], insb.: „…Additionally, rather than
including the game title, the game title may be inherent in the request (for example,
a different request type may be used for each game title). …“ (Unterstreichung
hinzugefügt); Merkmal 1.i).
Gemäß dem Absatz [0025] der D4 ist implizit auch eine „message“ an einen
Anwendungsserver nach dem Matchen an den dortigen Nutzer zu entnehmen,
zumindest aber dort angelegt, da eine solche Festlegung nur dann erfolgreich
umgesetzt werden kann, wenn entsprechende Nachrichten zwischen den
beteiligten Komponenten ausgetauscht werden (Merkmal 1.j).


Damit sind im Ergebnis aus der Druckschrift D4 ebenfalls nicht alle Merkmale des
Gegenstands des Anspruchs 1 bekannt.


1.8   Der Gegenstand des erteilten Anspruchs 1 beruht jedoch gegenüber der
Lehre der Druckschrift D11 (WO 2009 / 014 438 A1) zusammen mit dem
Fachwissen, wie es durch die D7 (WO 03 / 091 894 A1) belegt wird, nicht auf einer
erfinderischen Tätigkeit (Art. 56 EPÜ).

                                         - 37 -



Aus der Druckschrift D11 ist ein Verfahren bekannt, das die Identifizierung
benachbarter mobiler Geräte („mobile devices“) unterschiedlicher Nutzer mittels so
genannter „sensory identifier information“ erlaubt (D11, S. 1, Z. 3 – 6 i.V.m. S. 4, Z.
6 – 12, insb.: „By letting both (or all) mobile devices detect the same sensory
identifier, it is ensured that these mobile devices are proximate, as the detection of
the sensory identifier typically requires the proximity of the mobile devices to the
sensory identifier, …“ und S. 9, Z. 30 – S.11, Z. 2, insb.: „… the mobile devices 1, 2
are capable of detecting a sensory identifier. …“, (Unterstreichungen hinzugefügt);
Merkmale 1, 1.a).
Das Senden von als „messages“ zu verstehenden Datenpaketen, die eine
„representation“ des ID i.S.d. Streitpatents vorsehen, ist ebenfalls aus dieser
Druckschrift bekannt (D11, S.4, Z.27 – S.5, Z.2, insb.: „Preferably, the request
message comprises sensory identifier information. That is, the request message
may comprise information contained in or represented by the sensory identifier. …“;
Merkmal 1.b).
Um den Matchingprozess zwischen den einzelnen „mobile devices“ durchzuführen,
bedarf es eines Servers (D11, S.5, Z. 9 – 20 i.V.m. S. 8, Z. 20 - 31), der als derartige
Sensoridentifikatoren (ID) z.B. Barcodes nutzt bzw. verarbeitet (D11, S. 5, Z. 27 –
28 und S. 8, Z. 20 - 25 i.V.m. S.15, Z. 11 – 17; Merkmale 1.c, 1.e) und der außerdem
dazu ausgelegt ist, Anwendungen/Applikationen seitens der bzw. für die „devices“
auszuführen, sofern dieser Prozess erfolgreich verlaufen ist (D11, S. 8, Z. 26 – 31
i.V.m. S. 14, Z. 28 – S. 15, Z. 3, Merkmale 1.d, 1.f).
Jedoch ist der Lehre der D11 keines der Merkmale zu entnehmen oder
entsprechend angelegt, die das Ausführen dieser Applikation auf einem separaten
Applikationsserver thematisieren und auch das dafür notwendige Signalisieren
beschreiben (Merkmale 1.g, 1.h, 1.i, 1.j fehlen). Diese Notwendigkeit besteht dort
auch nicht, werden die für die Lehre der D11 relevanten Maßnahmen gemäß D11
doch sämtlich von einem einzigen Server durchgeführt.


Bei Nutzung nur eines Servers, ist es jedoch mit beschränkter Rechnerleistung des
Systems bei steigender Nutzerzahl für den Fachmann zwangsläufig notwendig, die

                                        - 38 -



Leistungsfähigkeit serverseitig durch weitere bauliche, schaltungstechnische oder
programmiertechnische Maßnahmen zu erhöhen, um sein Angebot funktions- und
auf Dauer zukunftsfähig – und damit für ihn letztlich profitabel - zu erhalten.


Es bietet sich für ihn an - wie im Rahmen dieses Nichtigkeitsverfahrens u.a. in dem
Fachbuch D6 mit dem „Horizontal Scaling“ als generelles Fachwissen belegt ist (D6,
S. 102, Fig. 3.13) – dafür Serverfunktionalitäten aufzusplitten oder so zu verteilen,
dass nicht alle Kapazitäten in einem einzigen Server zur Durchführung aller an
diesen gestellten Anfragen vorgehalten werden müssen. Das hätte im Falle
zunehmender      Nutzung    des    Dienstes      der   D11   sonst   zwangsläufig     die
Verlangsamung des Gesamtsystems zur Folge, was insbesondere bei zeitkritischen
Applikationen, wie z. B. Gaming-Applikationen (D11, S.12, Z.24 – 29), äußerst
nachteilig wäre. Zudem bietet ein modularer Aufbau dem Fachmann für zukünftige
Maßnahmen      ohnehin     ein    weniger   fehleranfälliges   sowie    meist     leichter
einzurichtendes, zu wartendes und zu aktualisierendes Umfeld.


Daher würde er die mit den Merkmalen 1.h bis 1.j verbundenen Maßnahmen
aufgrund seines Fachwissens in naheliegender Weise umsetzen, ohne hierfür
eigens erfinderisch tätig werden zu müssen. Als Beleg für das einschlägige Fachwissen auf diesem technischen Gebiet dient die Druckschrift D7, die eine praktisch
ausgereifte Umsetzung aus einem vergleichbaren Umfeld (‚game server“, „online
gaming context“) lehrt. Explizit werden dort Anwendungen wie im Streitpatent auf
mehreren separaten Servern verwirklicht (D7, S. 4, Abs. 1, „…multiple lobby servers
and application servers are provided,…“; S. 6, Abs. 3; Merkmal 1.g) und geeignete
Maßnahmen im Vorfeld zu deren gemeinsamer Einbindung ins Gesamtsystem
vorgenommen, wie sie z.B. entsprechend auszutauschende „messages“ mit die
Anwendungen identifizierendem Inhalt darstellen, sofern Datenwege zwischen den
eingebundenen Einzelkomponenten bestehen; letzteres wird dort etwa in Figur 1
und mittels der Ablaufdiagramme in den Figuren 4 und 5 aufgezeigt (vgl.
Sachaussage der Merkmale 1.h, 1.i, 1.j).

                                         - 39 -



Für den erteilten Anspruch 15, der letztlich nur die entsprechende Umsetzung der
Vorrichtungsmerkmale für ein Verfahren beinhaltet, ergibt sich mit derselben
Begründung wie für den erteilten Anspruch 1 kein erfinderischer Gegenstand.




1.9   Da der erteilte Anspruchssatz als Ganzes verteidigt wird, fallen damit auch
seine übrigen Ansprüche.




2.    Zum Hilfsantrag 0a


2.1   Gliederung der geänderten nebengeordneten Ansprüche 1 und 15


Da mehrere seitens der Parteien in diesem Verfahren aufgeworfene Streitpunkte
unmittelbar mit der Umgestaltung bzw. Umformulierung der einleitenden Merkmale
der Ansprüche 1 und 15 gemäß Hilfsantrag 0a verbunden sind, gibt der Senat diese
im Folgenden aus Gründen der Übersichtlichkeit nochmals in ihren Änderungen
beschrieben, sowie ausformuliert und im Merkmalsverbund an.


Der geänderte Anspruch 1 gemäß Hilfsantrag 0a unterscheidet sich im Vergleich
zur erteilten Fassung darin, dass die bisherigen Merkmale 1.a und 1.b gestrichen
werden und mittels der neuen Merkmale 1.a0a, 1.b0a und dem redaktionell
angepassten Merkmal 1.c0a das „system“ des Anspruchs 1 dahingehend erweitert
wird, dass die „devices“ nun ein integraler Bestandteil des „system“ werden. Der
geänderte Anspruch 1 gemäß Hilfsantrag 0a erhält damit folgende Form
(Änderungen hervorgehoben):


1     A system (40, 50) for identifying proximate devices (1, 2),
1.a   arranged for detecting a sensory identifier (ID) and
1.b   transmitting request messages (RQ1, RQ2), comprising representations of
      the detected sensory identifier,

                                        - 40 -



1.a0a the system comprising:
       said devices, wherein said proximate devices are arranged for detecting
       a sensory identifier (ID)
1.b0a and    transmitting     request    messages      (RQ1,    RQ2)    comprising
       representations of the detected sensory identifier;
1.c0a the system comprising:
       means for correlating representations of the detected sensory identifiers from
       the request messages received from the devices (1, 2) so as to match two or
       more of those devices, and
1.d – 1.j (unverändert)


Der geänderte Anspruch 15 gemäß Hilfsantrag 0a unterscheidet sich im Vergleich
zur erteilten Fassung darin, dass die bisherigen Merkmale 15.a und 15.b gestrichen
werden und mittels der neuen Merkmale 15.a0a, 15.b0a und dem redaktionell
angepassten Merkmal 150a das Verfahren des Anspruchs 15 dahingehend geändert
wird, dass die „devices“ nun ausdrücklich eine aktive Rolle als Bestandteil des
„system“ einnehmen und den so bislang nicht beanspruchten ersten und zweiten
Verfahrensschritt eines „detecting a sensory identifier“ und „transmitting request
messages“ ausführen. Der geänderte Anspruch 15 gemäß Hilfsantrag 0a erhält
damit folgende Form (Änderungen hervorgehoben):


150a   A method of identifying proximate devices (1, 2) the method comprising the
       steps of:
15.a   arranged for detecting a sensory identifier (ID) and
15.b transmitting request messages (RQ1, RQ2), comprising representations of
       the detected sensory identifier, the method comprising the steps of
15.a0a detecting a sensory identifier (ID) by said devices
15.b0a and   transmitting     request    messages      (RQ1,    RQ2)    comprising
       representations of the detected sensory identifier by said devices;
15.c – 15.i (unverändert)

                                      - 41 -



2.2 Die mit dem Hilfsantrag 0a verbundenen Änderungen (Merkmale 1.a0a, 1.b0a,
1.c0a bzw. 15.a0a, 15.b0a, 15.c0a) in den Ansprüchen 1 und 15 sind unzulässig,
da sie zu einer Schutzbereichserweiterung führen. In beiden Fällen sind die
Änderungen nicht von den ursprünglich erteilten Ansprüchen sachlich mit umfasst,
sondern richten sich auf einen anderen technischen Gegenstand, der durch einen
anders gestalteten Aufbau des beanspruchten Systems bzw. durch eine
anderslautende aktive Durchführung des Verfahrensablaufs ausgezeichnet ist. Das
Nichtigkeitsverfahren gibt dem Patentinhaber nur die Möglichkeit, das Schutzrecht
in eingeschränkter Fassung zu verteidigen, nicht aber, dieses darüber hinaus neu
zu gestalten. Letzteres ist vielmehr allein dem Patenterteilungsverfahren vorbehalten. Deshalb darf ein Patentanspruch im Nichtigkeitsverfahren nicht so geändert
werden, dass er einen von der erteilten Fassung nicht umfassten Gegenstand
einbezieht (vgl. BGH, Urteil vom 14. September 2004 - X ZR 149/01 - Elektronisches
Modul). Ein Gegenstand, der durch das erteilte Patent zwar offenbart, von ihm aber
nicht geschützt ist, kann somit auch nicht nachträglich in das Patent einbezogen
und unter Schutz gestellt werden (vgl. BGH, a.a.O.; BGH, Urteil vom 20. Dezember
2018 - X ZR 56/17 - Schaltungsanordnung Ill; BGH, Urteil vom 15. Dezember 2020
- X ZR 120/18 - Nachrichtenübermittlungsdienst).


Die Beklagte tritt dem entgegen. Die explizite Aufnahme der „proximate devices“ in
den Systemanspruch führe nicht zu einer Schutzbereichserweiterung, da hier „ein
gesamtes System“ beansprucht werde, „in dem mehrere Komponenten miteinander
zusammenwirken“. Dieser Auffassung schließt sich der Senat nicht an.


Mit der erteilten Fassung des Anspruchs 1 weist das „system“ die selbständigen
Entitäten mindestens eines „correlation servers“ (CS) und mindestens eines
„application servers“ (AS) auf (vgl. Auslegung im Abschnitt 1.4). Die genannten
„devices“ werden dem „system“ nicht ausdrücklich zugerechnet, wobei das „system“
auf die in ihnen implementierte Technik zurückgreift. Diese Argumentation gilt entsprechend auch bezogen auf die Verfahrensmerkmale des Anspruchs 15 (vgl.

                                        - 42 -



Merkmale 1.a, 1.b, 1.c und 1.a0a, 1.b0a, 1.c0a bzw. 15.a, 15.b, 15.c und 150a, 15.a0a,
15.b0a).


2.2.1 Auch die Beklagte gesteht zu, dass einige dieser Komponenten im erteilten
Systemanspruch 1 als strukturelle Komponenten explizit aufgeführt werden
(nämlich die Server CS und AS), andere jedoch, „speziell die benachbarten
Vorrichtungen“, nicht. Aus dem Gesamtzusammenhang folge ihrer Auffassung nach
aber, dass das Vorhandensein der benachbarten Vorrichtungen für das System
wesentlich sei, und diese – die „devices“ - mit den Servern CS und AS funktional
wechselwirken würden.
Deshalb sei hier auch kein vergleichbarer Fall gegeben, in dem gemäß der
höchstrichterlichen Rechtsprechung eine Erweiterung des Schutzbereiches vorliege
(vgl. BGH, a.a.O. - elektronisches Modul; BGH, a.a.O. - Schaltungsanordnung Ill).
Vielmehr führe die Einfügung eines weiteren Merkmals in den erteilten
Patentanspruch - so jedenfalls auch nach dieser Rechtsprechung - dann nicht zu
einer Schutzbereichserweiterung, wenn dieses in einer funktionalen Wechselwirkung mit dem Gegenstand des erteilten Patentanspruchs stehe. Vorliegend sei
eine solche „funktionale Wechselwirkung“ gegeben, weil der funktionsgemäße
Betrieb des beanspruchten Systems maßgeblich von dem Informationsaustausch
und   der   Wechselwirkung     der   „genannten    Mittel   mit   den   benachbarten
Vorrichtungen“ abhängig sei.
Demnach seien hier die Grundsätze der höchstrichterlichen Rechtsprechung zur
(fehlenden) Schutzbereichserweiterung auf den Systemanspruch des Streitpatents
unmittelbar übertragbar (vgl. BGH, Urteil vom 15. Dezember 2020 - X ZR 120/18 –
Nachrichtenübermittlungsdienst).


2.2.2 Diese Sichtweise der Beklagten, insbesondere ihre Deutung der höchstrichterlichen Rechtsprechung in Bezug auf den Hilfsantrags 0a kann den Senat nicht
überzeugen. Denn die hier vorgenommenen Änderungen im Merkmalswortlaut des
Anspruchs 1 und Anspruchs 15 führen, unabhängig von der Sichtweise, was ein
„funktionelles Wechselwirken“ einzelner durch einen Vorgang miteinander

                                       - 43 -



verknüpfter Entitäten anbelangt, zu keinerlei Beschränkung des jeweils erteilten
Gegenstandes. Der funktionsgemäße Betrieb des Systems in der maßgeblichen
erteilten Fassung wird auch vor der Gesamtoffenbarung der Lehre des Streitpatents
nur vom System selbst – d.h. im erteilten Anspruchssatz repräsentiert durch CS und
AS – übernommen, wogegen für die „devices“ im erteilten Anspruch 1 bzw. 15
hierzu nichts weiter festgelegt ist. Dies steht – anders als die Beklagte meint - im
Gegensatz zu den mit Hilfsantrag 0a beanspruchten Fassungen der genannten
Ansprüche, die nun etwas technisch Anderes beanspruchen als erteilt wurde. Es
findet zwar in der erteilten Fassung ein Datenaustausch zwischen „system“ und
„devices“ statt, auf deren Basis das „system“ weitere Maßnahmen vorsieht, jedoch
ohne dass dabei die „devices“ selbst räumlich-körperlich Teil des erteilten Systems
sind oder werden. Es liegt damit in der erteilten Lehre eine beachtliche Abgrenzung
zwischen System und wechselweisen Nutzern („devices“) vor und keine „funktionale
Wechselwirkung“ im Sinne der zitierten Rechtsprechung.


Im Einzelnen: im erteilten Anspruch 1 stellen ausdrücklich nur – jeweils mindestens
ein - CS und AS die Komponenten des beanspruchten Systems dar, während die
„devices“ nicht explizit als integraler Bestandteil mit funktionalen Aufgaben
innerhalb des Systems („system“) benannt werden. Das erscheint insbesondere vor
dem Hintergrund der technischen Lehre des Streitpatents gegenüber der mit dem
Hilfsantrag 0a beanspruchten Version auch technisch sinnvoll, da die „devices“ dort
beliebig austauschbar sind, nachdem sie jeweils spielwilligen externen Nutzern
gehören, die jederzeit wechseln können, wogegen das System mit CS und AS
selbst in seiner Gestalt, Funktion und softwaretechnischen Umsetzung stets
unverändert bleibt. Diese Lesart ist für den Fachmann auf diesem technischen
Gebiet auch weder fernliegend noch schwer nachvollziehbar, sondern stellt eine für
ihn sinnvolle und praktikable Ausgestaltung dar, deren Umsetzung ihn weder
überfordert, noch vor unüberwindliche Schwierigkeiten stellt. Das in der erteilten
Fassung und dem Hilfsantrag 0a realisierte prinzipielle Interagieren des Systems
(„system“) mit den Endgeräten („devices“) wird vom Senat gesehen. Nur kann allein
ein Zusammenwirken räumlich separierter und prinzipiell unterschiedlicher

                                       - 44 -



technischer Komponenten bzw. Vorrichtungen (Diensteanbieter, wechselnder
Client/Endgerät) nicht automatisch deren zwingende Zusammengehörigkeit in
einem „system“ nach sich ziehen. Gerade im Mobilfunkkontext – der auch vom
Streitpatent zugrunde gelegt wird - würde die Ansicht der Beklagten dazu führen,
dass beispielsweise alle in einem patentrechtlich als System beanspruchten mit
dem Mobilfunknetz verbundenen bzw. potentiell vorhandenen Teilnehmer – vom
Diensteanbieter mit seinen Servern bis zu den Nutzer/Clients und ggf.
nachgeordneter weiterer Teile – automatisch Bestandteil dieses (Gesamt-)Systems
würden. Dadurch würde aber eine technische Abgrenzung einer einzelnen Lehre,
z.B. einer dort auf gewissen Komponenten laufenden Anwendung, sinnlos, da jedes
weitere System automatisch Untersystem dieses Gesamtsystems wäre bzw. würde
und unter dessen Schutzbereich fiele. Daher ist aus Sicht des Senats vorliegend
technisch streng zu unterscheiden, ob permanent vorhandene/vorgehaltene
Entitäten mit weiteren permanent vorhandenen/vorgehaltenen Entitäten eines
Systems kommunizieren (wobei sie - wenn auch zunächst ungenannt - im Rahmen
einer Beschränkung als erstmals genanntes Merkmal auch Teil eines neu
formulierten Anspruchs werden können) oder als von extern für den Bestand und
die Ausgestaltung des Systems selbst nicht wesentliche, weil nur vorübergehend
auf dieses und seine Angebote zugreifende, Komponenten mit diesem zeitweise in
Interaktion stehen. Letztere treten zwar durchaus mit dem System in „funktionale
Wechselwirkung“, können aber aufgrund ihrer technischen Natur nicht echter
Bestandteil des Systems sein, sondern stellen in Kenntnis desselben lediglich
beliebige Nutznießer von dessen Angeboten dar. Daher vermögen sie ein solches
System auch nicht zu beschränken.




2.3   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 0a ist überdies auch
nicht patentfähig, da er sich in naheliegender Weise aus der Lehre der Druckschrift
D11 zusammen mit dem Fachwissen ergibt, wie es dem Fachmann aus der
Druckschrift D7 bekannt ist (vgl. Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138
Abs. 1 Buchst. a), Art. 52, 56 EPÜ).

                                         - 45 -




Die im Anspruch 1 nunmehr geänderten Merkmale 1.a0a, 1b0a, 1c0a ändern das
„system“ des Anspruchs 1 dahingehend, dass die „devices“ nun einen integralen
Bestandteil des Systems bilden. Diese Änderungen vermögen den Anspruch 1
jedoch nicht gegenüber dem Stand der Technik abzugrenzen, wie er für diese
Merkmale im Rahmen der Druckschrift D11 Relevanz entfaltet. Wie bereits unter
Abschnitt 1.8 ausgeführt, ist aus dieser Druckschrift ein Verfahren bekannt, das die
Identifizierung benachbarter „mobile devices“ unterschiedlicher Nutzer mittels
„sensory identifier information“ erlaubt, wobei die „devices“ jeweils in der Lage sind,
dieselbe mit einer „detection unit“ zu detektieren und in Folge mittels einer
„processor unit“ eine „request message“ zu versenden, die mit der ID assoziiert ist
(D11, S. 1, Z. 3 – 6 i.V.m. S. 4, Z. 6 – 12, S. 8, Z. 7 – 11, S. 9, Z. 30 – S.11, Z. 2).
Damit sind aus den eben genannten Textstellen auch die mit den gemäß Hilfsantrag
0a verbundenen Änderungen sämtlich bekannt (Merkmale 1, 1.a0a, 1b0a, 1c0a).


Hinsichtlich der unveränderten Merkmale des Anspruchs 1 wird zur Begründung auf
die entsprechenden Ausführungen zum Hauptantrag verwiesen.




Für den Anspruch 15 gemäß Hilfsantrag 0a gelten – da es sich um den zum
Anspruch 1 korrespondierenden Verfahrensanspruch handelt - mit derselben
Begründung dieselben Ausführungen.


2.4 Da der Anspruchssatz gemäß Hilfsantrag 0a als Ganzes verteidigt wird, fallen
unabhängig vom jeweiligen Grund damit jeweils auch die übrigen Ansprüche.




3.     Zum Hilfsantrag 0b

                                       - 46 -



3.1   Der Hilfsantrag 0b unterscheidet sich gegenüber dem Hilfsantrag 0a lediglich
darin, dass der Anspruch 1 die erteilte Fassung aufweist und nur der Anspruch 15
die Fassung des vorangegangenen Hilfsantrags 0a erhält.


3.2   Somit sind mit dem Anspruch 15 gemäß Hilfsantrag 0b dieselben
Zulässigkeitsmängel sowie ebenfalls die mangelnde Patentfähigkeit verbunden, wie
bereits im Rahmen des Hilfsantrags 0a ausgeführt. Da der Anspruchssatz dieses
Hilfsantrags geschlossen verteidigt wird, führt diese Verteidigung des Streitpatents
ebenfalls nicht zum Erfolg. Zur Begründung wird auf die obigen Ausführungen unter
den Abschnitten 2.2 und 2.3 verwiesen.




4.    Zum Hilfsantrag 1a‘


Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1a‘ ist ebenfalls nicht zulässig,
da dieser dem Anspruch 1 aus dem Hilfsantrag 0a entspricht.


Zur Begründung wird auf die entsprechenden, obigen Ausführungen im Abschnitt
2.2 verwiesen.




5.    Zum Hilfsantrag 1b1‘


Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1b1‘ ist nicht zulässig, da
dieser ebenfalls die Form des Anspruchs 1 aus dem Hilfsantrag 0a erhält.


Zur Begründung wird gleichfalls auf die entsprechenden Ausführungen im Abschnitt
2.2 verwiesen.




6.    Zum Hilfsantrag 1b2‘

                                       - 47 -



Der Gegenstand des Anspruchs 15 gemäß Hilfsantrag 1b2‘ ist nicht zulässig, da
dieser die Form des Anspruchs 15 aus dem Hilfsantrag 0a erhält.


Zur Begründung wird daher ebenso auf die entsprechenden Ausführungen im
Abschnitt 2.2 verwiesen.




7.    Zum Hilfsantrag 1c


Der Gegenstand der mit dem Hilfsantrag 1c zulässig verteidigten nebengeordneten
Ansprüche 1, 14 und 15 erweist sich gegenüber dem im Verfahren befindlichen
Stand der Technik als neu und beruht auch auf einer erfinderischen Tätigkeit (Art. II
§ 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52, 54, 56 EPÜ).


7.1   Der jeweilige Gegenstand der Ansprüche 1, 14 und 15 gemäß Hilfsantrag 1c
unterscheidet sich im Vergleich zur erteilten Fassung jeweils durch die Ergänzung
eines Merkmals im Anschluss an das bisherige letzte Merkmal (Anspruch 1:
Merkmal 1.k1; Anspruch 15: Merkmal 15.j1) bzw. für den Anspruch 14 um eine
Ergänzung im bisherigen Merkmal 14.e, die jeweils folgendermaßen lauten (vom
Senat gegliedert; Änderungen zur erteilten Fassung hervorgehoben):


Anspruch 1:


1.k1a wherein the match message is transmitted from the at least one
      correlation server to the application server through one of the
      proximate devices.


Anspruch 14:

                                         - 48 -



14.e1 the message processor is configured to cause the transmitter to transmit a
       match message through one of the devices to an application server that is
       distinct from the correlation server.


Anspruch 15:


15.j1a wherein the match message is transmitted to the application server
       through one of the devices.


Mit der Fassung des Hilfsantrags 1c sind keine unzulässigen Erweiterungen
gegenüber den Ursprungsunterlagen verbunden, er ist im Übrigen auch zulässig.


Nach der Rechtsprechung ist es erforderlich, dass der Fachmann die im Anspruch
bezeichnete technische Lehre den Ursprungsunterlagen unmittelbar und eindeutig
als mögliche Ausführungsform der Erfindung entnehmen kann (vgl. Schulte, PatG,
11. Aufl., § 81, Rd. 119 ff. m.w.N.).


Die Ergänzungen sind nach diesen Grundsätzen hier ausreichend in der PCT-Anmeldung ursprungsoffenbart (NK4, Figur 4b i.V.m S. 12, Z. 3 – 8 bzw. im
Streitpatent, Figur 4b i.V.m. Absatz [0052]). Zwar ist der Klägerin zuzustimmen,
dass die Abgleichsmeldung („match message“ enthaltend zumindest repräsentative
Daten zur „ID“ und zur „application“) im Text an den zitierten Stellen nicht
wortwörtlich offenbart ist, sondern nur, dass eine Kommunikation zwischen CS und
AS über CD (also indirekt) möglich ist. Der Fachmann entnimmt den Weg
unmittelbar und eindeutig den in der Figur 4b gezeigten erfindungsgemäßen
Gestaltung im Zusammenhang mit dem Text der Beschreibung, der dies
ausdrücklich als Variante nennt.



7.2    Der Anspruch 1 gemäß Hilfsantrag 1c ist neu gegenüber dem im Verfahren
befindlichen Stand der Technik, da aus keiner der genannten Druckschriften dessen

                                        - 49 -



sämtliche Merkmale bekannt sind. Insbesondere ist das neue Merkmal 1.k1a keiner
der Druckschriften unmittelbar und eindeutig zu entnehmen.


7.3   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1c beruht ausgehend
vom im Verfahren genannten Stand der Technik auch auf einer erfinderischen
Tätigkeit, da er durch diesen nicht nahegelegt ist.


7.3.1 Ausgehend von der Druckschrift D11 vermag der Fachmann das neue
Merkmal 1.k1a nicht in naheliegender Weise aus dem Fachwissen oder in Kenntnis
eines anderen Standes der Technik, wie er im Verfahren genannt ist (etwa der
Druckschrift D7), zu deren Lehre ergänzen, denn dazu fehlt ihm jeglicher Anlass.
Ein solcher wurde seitens der Klägerin auch nicht in überzeugender Weise
vorgetragen und ist für den Senat auch sonst nicht ersichtlich.


Wie in der Merkmalsanalyse (vgl. Abschnitt 1.8) ausgeführt, ist der Druckschrift D11
die Merkmalsgruppe 1 bis 1.f zu entnehmen. Basierend auf der dort ebenfalls
genannten Veranlassung, die D7 als Beleg für das Fachwissen zu nutzen, sind die
weiteren Merkmale 1.g bis 1.j für den Fachmann in naheliegender Weise zu
ergänzen.
Weshalb nun aber ausgehend von dieser Lehre seitens des Fachmanns nur aus
seinem Fachwissen heraus – denn aus D7 und D11 ist nichts Vergleichbares zu
entnehmen - ein Kommunikationsweg zwischen AS und CS mit Umweg über die
„devices“ eingeschlagen werden soll, erschießt sich für den Senat nicht und liegt zu
seiner Überzeugung für den Fachmann auch nicht nahe. Verlängert doch ein
Wegverlauf zusätzlich über die „devices“ die Kommunikation rein laufzeittechnisch
betrachtet   zwischen   den    für   den   reibungslosen   Ablauf   der   Applikation
verantwortlichen Servern im Vergleich zu einer direkten Kommunikation bzw.
Signalisierung und ist damit ggf. fehleranfälliger für äußere Einflüsse. Dies würde
der Fachmann aus Sicht des Senates faktisch als nachteilig ansehen und daher
technisch zu vermeiden suchen.

                                         - 50 -



7.3.2 Auch die diskutierten Druckschriften D1 bis D4 zeigen keinen solchen
Kommunikationsweg für eine „match message“ über die „devices“ (vgl. hierfür
repräsentativ in D1, Fig. 1, D2, Fig. 1 und 3; D3, Fig. 8 i.V.m. Sp. 12, Z. 51 – 61; D4,
Fig. 1, 2, 6 und 7). Auch die Klägerin zeigt hierzu nichts auf.


Die weiteren Druckschriften D5 bis D10, die von den Verfahrensbeteiligten im
Kontext dieses Hilfsantrages gar nicht behandelt wurden, liegen aus Sicht des
Senates im Übrigen ohnehin technisch weiter ab und vermögen zu dieser Thematik
dem Fachmann jedenfalls weder konkrete Ausgestaltungen noch Anregungen zu
vermitteln, die Lehre gemäß dem Merkmal 1.k1a zu ergänzen.


Dies gilt mit derselben Begründung auch für die nebengeordneten Ansprüche 14
und 15 und ihre im Rahmen des Hilfsantrags 1c vorgenommenen, sinngemäß
vergleichbaren Merkmalsergänzungen (Merkmale 14.e1 und 15.j1a).


7.3.3 Die Gegenstände der mit dem Hilfsantrag 1c verteidigten Ansprüche 1, 14
und 15 erweisen sich folglich gegenüber dem im Verfahren befindlichen Stand der
Technik als patentfähig.


Auch die auf den Anspruch 1 und 15 rückbezogenen Unteransprüche 2 bis 13 sowie
16 bis 19 gemäß Hilfsantrag 1c bilden deren Gegenstände, auf die sie jeweils direkt
oder indirekt rückbezogen sind, in nicht selbstverständlicher Weise weiter und
erweisen sich daher ebenfalls als patentfähig.




8.     In Anbetracht der erfolgreichen Verteidigung des Streitpatents mit Hilfsantrag
1c war über die weiteren Hilfsanträge sowie die nachrangig verteidigten
Unteransprüche nicht mehr zu entscheiden.

                                     - 51 -



                                       II.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i.V.m. § 92 Abs. 1 Satz 1 ZPO.
Der Senat hat dabei berücksichtigt, dass der in der Fassung des Hilfsantrages
aufrechterhaltene Teil des Patents gegenüber der erteilten Fassung wesentlich
eingeschränkt ist.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i.V.m. § 709 Satz 1 und 2 ZPO.



                                       III.


                      Rechtsmittelbelehrung



Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Heimen             Dr. Meiser      Dr. Wollny        Dr. Ball        Jürgensen
