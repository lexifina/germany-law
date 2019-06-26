---
ecli: "ECLI:DE:BPatG:2019:260619U6Ni2.17EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 2/17"
decided: "2019-06-26"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=28&nr=36770&anz=817&pos=426&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2019-06-26_6_Ni_2_17_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0082.md", "germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0132.md", "germany/bund/acts/zpo/0138.md", "germany/bund/acts/zpo/0217.md", "germany/bund/acts/zpo/0227.md", "germany/bund/acts/zpo/0274.md", "germany/bund/acts/zpo/0283.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 2/17 vom 2019-06-26

## Entscheidung

BUNDESPATENTGERICHT

                    IM NAMEN DES VOLKES

                              URTEIL
                                                     Verkündet am
                                                     26. Juni 2019
6 Ni 2/17 (EP)                                             …

(Aktenzeichen)


                    In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2019:260619U6Ni2.17EP.0

                                           -2-



                     betreffend das europäische Patent 1 990 926
                                   (DE 60 2007 032 340)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts am 26. Juni 2019
durch     die        Vorsitzende      Richterin   Friehe     sowie     die       Richter
Dipl.-Phys. Dr. Schwengelbeck, Jacobi, Dipl.-Ing. Altvater und Dr. Ing. Flaschke


für Recht erkannt:


   I.     Das europäische Patent 1 990 926 wird teilweise für nichtig erklärt, soweit es über folgende Fassung hinausgeht:


                1.     A method for a network device of a LTE network system comprising:


                allocating control channels represented by nodes of a tree
                structure, wherein nodes of the tree structure at a highest
                level of the tree structure represent control channel elements, and wherein each control channel of the control
                channels comprises at least one of the control channel elements carrying information for a respective identifier used to
                detect the control channel,


                characterized in that
                the allocation is performed by limiting allocation of highest
                level control channels, the highest level control channels being represented by the nodes of the tree structure at the
                highest level of the tree structure, the method further comprising increasing allocation of lower level control channels,
                the lower level control channels being represented by nodes
                of the tree structure at lower levels of the tree structure,

                           -3-



wherein the allocation is increased more the lower the level
of the tree structure.


2.      The method of claim 1, comprising:
transmitting the allocated control channels to user equipments by distributing the allocated control channels to subcarriers over a system bandwidth.


3.      The method of claim 1, wherein the higher level control channels are combined to the lower level control channels.


7.      A network device in a LTE network system (20) comprising:
an allocation unit (22) configured to allocate control channels
represented by nodes of a tree structure, wherein nodes of
the tree structure at a highest level of the tree structure represent control channel elements, and wherein each control
channel of the control channels comprises at least one of the
control channel elements carrying information for a respective identifier used to detect the control channel,


characterized in that
the allocation unit (22) is configured to limit allocation of
highest level control channels, the highest level control
channels being represented by the nodes of the tree structure at the highest level of the tree structure, and to increase
allocation of lower level control channels, the lower level
control channels being represented by nodes of the tree
structure at lower levels of the tree structure, wherein the allocation is increased more the lower the level of the tree
structure.

                                         -4-



             8.       The device of claim 7, comprising:
             a transmitting unit (21) configured to transmit the allocated
             control channels to user equipments by distributing the allocated control channels to sub-carriers over a system bandwidth.


             9.       The device of claim 7 or 8, wherein the device comprises an evolved node B.


II.    Die weitergehende Klage wird abgewiesen.


III.   Von den Kosten des Rechtsstreits trägt die Klägerin 10 % und die
Beklagte 90 %.


IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 % des zu
vollstreckenden Betrages vorläufig vollstreckbar.




                                    I. Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 1 990 926
(Streitpatent). Das am 7. Mai 2007 angemeldete Streitpatent ist in Kraft und wird
beim    Deutschen      Patent-    und    Markenamt     unter   dem   Aktenzeichen
60 2007 032 340 geführt.


Das Streitpatent trägt die Bezeichnung


              „Control channels in communication network systems“
                  (in deutscher Sprache laut Streitpatentschrift:
              „Steuerkanäle in Kommunikationsnetzwerksystemen“)

                                       -5-



und umfasst in der erteilten Fassung sechzehn Patentansprüche, die mit der am
22. Dezember 2016 eingereichten Nichtigkeitsklage in vollem Umfang angegriffen
werden.


Die angegriffenen nebengeordneten Patentansprüche 1, 5, 8, 11 und 14 lauten in
der Verfahrenssprache Englisch:


            1.     A method for a network device of a LTE network system comprising:
            allocating control channels represented by nodes of a tree
            structure, wherein nodes of the tree structure at a highest
            level of the tree structure represent control channel elements, and wherein each control channel of the control
            channels comprises at least one of the control channel elements carrying information for a respective identifier used to
            detect the control channel,


            characterized in that
            the allocation is performed by limiting allocation of highest
            level control channels, the highest level control channels being represented by the nodes of the tree structure at the
            highest level of the tree structure, thereby allowing allocation
            of lower level control channels, the lower level control channels being represented by nodes of the tree structure at
            lower levels of the tree structure.


            5.     A method in a user device of a LTE network system
            comprising:
            searching for a control channel by decoding control channels
            represented by nodes of a tree structure, by using an identifier, wherein nodes of the tree structure at a highest level of
            the tree structure represent control channel elements, and

                            -6-



wherein each control channel of the control channels comprises at least one of the control channel elements carrying
information for a respective identifier used to detect the control channel,


characterized in that
the searching is limited for highest level control channels, the
highest level control channels being represented by the
nodes of the tree structure at the highest level of the tree
structure, thereby allowing searching for lower level control
channels, the lower level control channels being represented
by nodes of the tree structure at lower levels of the tree
structure.


8.     A network device in a LTE network system (20) comprising:
an allocation unit (22) configured to allocate control channels
represented by nodes of a tree structure, wherein nodes of
the tree structure at a highest level of the tree structure represent control channel elements, and wherein each control
channel of the control channels comprises at least one of the
control channel elements carrying information for a respective identifier used to detect the control channel,


characterized in that
the allocation unit (22) is configured to limit allocation of
highest level control channels, the highest level control
channels being represented by the nodes of the tree structure at the highest level of the tree structure, thereby allowing
allocation of lower level control channels, the lower level
control channels being represented by nodes of the tree
structure at lower levels of the tree structure.

                                         -7-



             11.    A user device in a LTE network system (10) comprising:
             a decoding unit (12) configured to search for a control channel by decoding control channels represented by nodes of a
             tree structure, by using an identifier, wherein nodes of the
             tree structure at a highest level of the tree structure represent
             control channel elements, and wherein each control channel
             of the control channels comprises at least one of the control
             channel elements carrying information for a respective identifier used to detect the control channel,


             characterized in that
             the decoding unit (12) is configured to limit searching for
             highest level control channels, the highest level control
             channels being represented by the nodes of the tree structure at the highest level of the tree structure, thereby allowing
             searching for lower level control channels, the lower level
             control channels being represented by nodes of the tree
             structure at lower levels of the tree structure.


             14.    A computer program product including a program for a
             processing device, comprising executable instructions for
             performing the steps of any one of claims 1 to 7 when the
             program is run on the processing device.


In der Fassung der Streitpatentschrift lauten sie in deutscher Sprache:



             1.     Verfahren für eine Netzwerkkomponente eines LTG-Netzwerksystems, wobei das Verfahren Folgendes umfasst:
             Zuordnen von Steuerkanälen, die durch Knoten einer
             Baumstruktur     dargestellt    werden,      wobei Knoten    der
             Baumstruktur auf einer höchsten Ebene der Baumstruktur

                          -8-



Steuerkanalelemente darstellen, und wobei jeder Steuerkanal der Steuerkanäle mindestens eines der Steuerkanalelemente umfasst, das Informationen für einen jeweiligen Identifikator transportiert, der zum Detektieren des Steuerkanals
verwendet wird,


dadurch gekennzeichnet, dass
die Zuordnung ausgeführt wird, indem die Zuordnung von
Steuerkanälen der höchsten Ebene begrenzt wird, wobei die
Steuerkanäle der höchsten Ebene durch die Knoten der
Baumstruktur auf der höchsten Ebene der Baumstruktur dargestellt werden, wodurch die Zuordnung von Steuerkanälen
niedrigerer Ebenen ermöglicht wird, wobei die Steuerkanäle
niedrigerer Ebenen durch Knoten der Baumstruktur auf niedrigeren Ebenen der Baumstruktur dargestellt werden.


5.    Verfahren in einer Nutzerkomponente eines LTG-Netzwerksystems, das Folgendes umfasst:
Suchen nach einem Steuerkanal durch Decodieren von
Steuerkanälen, die durch Knoten einer Baumstruktur dargestellt werden, unter Verwendung eines Identifikators, wobei
Knoten der Baumstruktur auf einer höchsten Ebene der
Baumstruktur Steuerkanalelemente darstellen, und wobei jeder Steuerkanal der Steuerkanäle mindestens eines der
Steuerkanalelemente umfasst, das Informationen für einen
jeweiligen Identifikator transportiert, der zum Detektieren des
Steuerkanals verwendet wird,


dadurch gekennzeichnet, dass
das Suchen nach Steuerkanälen der höchsten Ebene begrenzt ist, wobei die Steuerkanäle der höchsten Ebene durch
die Knoten der Baumstruktur auf der höchsten Ebene der

                          -9-



Baumstruktur dargestellt werden, wodurch das Suchen nach
Steuerkanälen niedrigerer Ebenen ermöglicht wird, wobei die
Steuerkanäle niedrigerer Ebenen durch Knoten der Baumstruktur auf niedrigeren Ebenen der Baumstruktur dargestellt
werden.


8.    Netzwerkkomponente in einem LTG-Netzwerksystem
(20), die Folgendes umfasst:
eine Zuordnungseinheit (22), die dafür konfiguriert ist,
Steuerkanäle zuzuordnen, die durch Knoten einer Baumstruktur dargestellt werden, wobei Knoten der Baumstruktur
auf einer höchsten Ebene der Baumstruktur Steuerkanalelemente darstellen, und wobei jeder Steuerkanal der Steuerkanäle mindestens eines der Steuerkanalelemente umfasst,
das Informationen für einen jeweiligen Identifikator transportiert, der zum Detektieren des Steuerkanals verwendet wird,


dadurch gekennzeichnet, dass
die Zuordnungseinheit (22) dafür konfiguriert ist, die Zuordnung von Steuerkanälen der höchsten Ebene zu begrenzen,
wobei die Steuerkanäle der höchsten Ebene durch die Knoten der Baumstruktur auf der höchsten Ebene der Baumstruktur dargestellt werden, wodurch die Zuordnung von
Steuerkanälen niedrigerer Ebenen ermöglicht wird, wobei die
Steuerkanäle niedrigerer Ebenen durch Knoten der Baumstruktur auf niedrigeren Ebenen der Baumstruktur dargestellt
werden.


11.   Nutzerkomponente in einem LTG-Netzwerksystem
(10), die Folgendes umfasst:
eine Decodiereinheit (12), die dafür konfiguriert ist, durch
Decodieren von Steuerkanälen, die durch Knoten einer

                                       - 10 -



             Baumstruktur dargestellt werden, unter Verwendung eines
             Identifikators nach einem Steuerkanal zu suchen, wobei
             Knoten der Baumstruktur auf einer höchsten Ebene der
             Baumstruktur Steuerkanalelemente darstellen, und wobei jeder Steuerkanal der Steuerkanäle mindestens eines der
             Steuerkanalelemente umfasst, das Informationen für einen
             jeweiligen Identifikator transportiert, der zum Detektieren des
             Steuerkanals verwendet wird,


             dadurch gekennzeichnet, dass
             die Decodiereinheit (12) dafür konfiguriert ist, das Suchen
             nach Steuerkanälen der höchsten Ebene zu begrenzen, wobei die Steuerkanäle der höchsten Ebene durch die Knoten
             der Baumstruktur auf der höchsten Ebene der Baumstruktur
             dargestellt werden, wodurch das Suchen nach Steuerkanälen niedrigerer Ebenen ermöglicht wird, wobei die Steuerkanäle niedrigerer Ebenen durch Knoten der Baumstruktur auf
             niedrigeren Ebenen der Baumstruktur dargestellt werden.


             14.     Computerprogrammprodukt, das ein Programm für ein
             Verarbeitungsgerät enthält und ausführbare Instruktionen
             umfasst, um die Schritte nach einem der Ansprüche 1 bis 7
             auszuführen, wenn das Programm auf dem Verarbeitungsgerät läuft.


Die ebenfalls angegriffenen übrigen Patentansprüche sind jeweils auf die vorgenannten nebengeordneten Ansprüche unmittelbar oder mittelbar rückbezogen.


Die Klägerin ist der Ansicht, dass das Streitpatent wegen des Nichtigkeitsgrunds
der mangelnden Patentfähigkeit, und zwar wegen mangelnder Neuheit, jedenfalls
aber wegen mangelnder erfinderischer Tätigkeit, für nichtig zu erklären sei. Dies

                                          - 11 -



stützt sie auf die Druckschriften (Nummerierung und Kurzzeichen nach Klageschriftsatz):


K4       3GPP Dokument R1-072220: „Restriction on PDCCH monitoring set“
K4e      3GPP TS 36.300 v8.0.0
K5       EP 1 988 667 A2
K6       WO 2008/084422 A2
K7       WO 2008/081004 A1
K8       3GPP Dokument R1-071003: „Structure and transport of the Downlink
         Control Channels“
K11      3GPP TS 36.212 V1.0.0
K12      3GPP Dokument R1-071296: „Signaling Choices for UL ACK/NAK”


Die Klägerin beantragt,


       das europäische Patent 1 990 926 mit Wirkung für das Hoheitsgebiet der
       Bundesrepublik Deutschland in vollem Umfang für nichtig zu erklären.


Die Beklagte beantragt,

       die Klage abzuweisen;

       hilfsweise, die Klage abzuweisen, soweit sie sich auch gegen eine der Fassungen des Streitpatents nach den Hilfsanträgen

            -   1 und 2 vom 23. Juli 2018,
            -   2‘ vom 26. Juni 2019,
            -   2a vom 24. Mai 2019,
            -   2a‘ vom 26. Juni 2019,
            -   3 vom 23. Juli 2018,
            -   4 und 5 vom 24. Mai 2019 und
            -   6 vom 26. Juni 2019

       (in dieser Reihenfolge) richtet.

                                     - 12 -



Die neun Hilfsanträge, aufgeführt in der beantragten Reihenfolge, haben folgenden Inhalt:


   -   Hilfsantrag 1 vom 23. Juli 2018 ändert gegenüber der erteilten Fassung
       die Fassung der unabhängigen Ansprüche 1, 5, 8 und 11 wie folgt:

- 13 -

                                   - 14 -



-   Hilfsantrag 2 vom 23. Juli 2018 ändert gegenüber der erteilten Fassung
    die Fassung des Anspruchs 1 wie folgt:




    Anspruch 4 der erteilten Fassung ist gestrichen. Aus den Ansprüchen 5 bis
    16 werden die Ansprüche 4 (neu) bis 15 (neu), unter Anpassung der Rückbezüge in den Ansprüchen 5 (neu), 6 (neu), 8 (neu), 9 (neu) und 11 bis 15
    (neu). Gegenüber der erteilten Fassung wird die Fassung der unabhängigen Ansprüche 4 (neu), 7 (neu) und 10 (neu) wie folgt geändert:

- 15 -

                                    - 16 -



-   Hilfsantrag 2‘ vom 26. Juni 2019 ändert gegenüber der erteilten Fassung
    die Fassung des Anspruchs 1 wie folgt:




    Die Ansprüche 4, 6 und 12 der erteilten Fassung sind gestrichen. Aus dem
    Anspruch 5 wird der Anspruch 4 (neu), aus den Ansprüchen 7 bis 11 werden die Ansprüche 5 bis 9 (neu), aus den Ansprüchen 13 bis 16 werden die
    Ansprüche 10 bis 13 (neu), unter Anpassung der Rückbezüge in den Ansprüchen 5 (neu), 7 (neu), 8 (neu) sowie 10 (neu) bis 13 (neu). Gegenüber
    der erteilten Fassung wird die Fassung der unabhängigen Ansprüche 4
    (neu), 6 (neu) und 9 (neu) wie folgt geändert:

- 17 -

                                   - 18 -




-   Hilfsantrag 2a vom 24. Mai 2019 ändert gegenüber der erteilten Fassung
    die Fassung des Anspruchs 1 wie folgt:




    Anspruch 4 gemäß erteilter Fassung ist gestrichen. Aus den Ansprüchen 5
    bis 16 werden die Ansprüche 4 (neu) bis 15 (neu) unter Anpassung der
    Rückbezüge in den Ansprüchen 5 (neu), 6 (neu), 8 (neu), 9 (neu) und 11
    bis 15 (neu). Gegenüber der erteilten Fassung wird die Fassung der unabhängigen Ansprüche 4 (neu), 7 (neu) und 10 (neu) wie folgt geändert:

- 19 -

                                  - 20 -




-   Hilfsantrag 2a‘ vom 26. Juni 2019 entspricht Hilfsantrag 2a vom 24. Mai
    2019 mit dieser ergänzenden Maßgabe in den Ansprüchen 4 (neu) und 10
    (neu):

                                  - 21 -




-   Hilfsantrag 3 vom 23. Juli 2018 ändert gegenüber der erteilten Fassung
    die Fassung der unabhängigen Ansprüche 1, 5, 8 und 11 wie folgt:

- 22 -

                                  - 23 -




-   Hilfsantrag 4 vom 24. Mai 2019 ändert gegenüber der erteilten Fassung
    die Fassung der unabhängigen Ansprüche 1, 5, 8 und 11 wie folgt:

- 24 -

                                  - 25 -




-   Hilfsantrag 5 vom 24. Mai 2019 :ändert gegenüber der erteilten Fassung
    die Fassung des Anspruchs 1 wie folgt:




    Anspruch 4 gemäß erteilter Fassung ist gestrichen. Aus den Ansprüchen 5
    bis 16 werden die Ansprüche 4 (neu) bis 15 (neu) unter Anpassung der
    Rückbezüge in den Ansprüchen 5 (neu), 6 (neu), 8 (neu), 9 (neu) und 11

                               - 26 -



bis 15 (neu). Gegenüber der erteilten Fassung wird die Fassung der unabhängigen Ansprüche 4 (neu), 7 (neu) und 10 (neu) wie folgt geändert:

                                       - 27 -




   -   Hilfsantrag 6 vom 26. Juni 2019 lautet wie aus dem Tenor ersichtlich.


Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den Gegenstand des Streitpatents in der erteilten Fassung, wenigstens in einer der verteidigten Fassungen für schutzfähig.


Die Klägerin hält die Hilfsanträge 1, 2, 2a und 5 bereits für unzulässig sowie den
Gegenstand der Hilfsanträge 1, 2, 3 und 6 für nicht ausführbar offenbart. Hilfsantrag 2‘ vom 26. Juni 2019 sei als verspätet zurückzuweisen. Dieser Hilfsantrag
beruhe nicht auf dem Ergebnis der Diskussion in der mündlichen Verhandlung, sei
vielmehr bereits vor dem Termin vorbereitet worden.


Die Beklagte bestätigt, dass Hilfsantrag 2‘ bereits vor dem Termin vorbereitet worden sei. Die Frist nach dem qualifizierten Hinweis vom 26. April 2019 sei allerdings
zu kurz bemessen gewesen.


In dem qualifizierten Hinweis vom 26. April 2019, zu dessen Wortlaut auf die Akte
verwiesen wird, war den Parteien eine Äußerungsfrist zum Hinweis bis zum
24. Mai 2019 und eine Stellungnahmefrist auf das jeweilige Vorbringen der

                                       - 28 -



Gegenseite bis zum 14. Juni 2019 gesetzt worden, wobei sie über die Folgen
einer Fristversäumung nach § 83 Abs. 4 PatG belehrt wurden.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                            II. Entscheidungsgründe


Die zulässige Klage ist überwiegend, wie aus dem Tenor ersichtlich, begründet.


Während das Streitpatent in der erteilten Fassung für nichtig zu erklären ist, weil
insoweit der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Artikel II
§ 6 Absatz 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54
EPÜ besteht, und die Beklagte es auch nicht in den beschränkten Fassungen
nach den Hilfsanträgen 1, 2, 2‘, 2a, 2a‘ und 3 bis 5 erfolgreich verteidigen kann,
weil diese Hilfsanträge entweder als unzulässig bzw. als verspätet zurückzuweisen sind oder derselbe Nichtigkeitsgrund wie bei der erteilten Fassung besteht, ist
die Klage abzuweisen, soweit sie sich auch gegen die beschränkte Fassung nach
Hilfsantrag 6 richtet, weil dieser keine Nichtigkeitsgründe entgegenstehen.




                                        A.


                   I.     Zum Gegenstand des Streitpatents


1.    Die Erfindung betrifft ausweislich seines Titels Steuerkanäle (control
channels)    in    Kommunikationssystemen, insbesondere deren Zuweisung
(allocation) und Dekodierung (decoding), beispielsweise in 3GPP (3rd Generation
Partnership Project) LTE-Netzwerksystemen (Absatz 0001 der Streitpatentschrift).


Die Streitpatentschrift geht nach Absatz 0002 davon aus, dass beispielsweise in
einem LTE-System alle Kanalzuweisungen in einem sehr kurzen Zeitraum, der

                                        - 29 -



Dauer    der   sogenannten   Teilrahmen     (subframes)   erfolgen   müssten.   Die
Kanalzuweisungen würden über gemeinsame Steuerkanäle (shared control
channels) signalisiert, die in den ersten Multi-Carrier-Symbolen eines Teilrahmens
enthalten seien und den Multi-Carrier-Symbolen für Datenkanäle (data channels)
vorausgingen. Jeder Kanal, egal ob für den Downlink oder für den Uplink, sei
daher in zwei separate Teile aufgeteilt, nämlich in einen Teil für Steuerdaten
(control part) und in einen Teil für Nutzdaten (data part). Der als PDSCH (physical
downlink shared channel) bezeichnete Teil für Nutzdaten enthalte Daten für die
Nutzer, während der als PDCCH (physical downlink control channel) bezeichnete
Teil für Steuerdaten (unter anderem) die Allokations- bzw. Zuweisungsinformation
für die vorgesehenen Nutzer enthalte.


Dabei ist dem Streitpatent als Aufgabe zu entnehmen, Verfahren und
Vorrichtungen zum Reduzieren der Komplexität der Steuerkanal-Dekodierung
anzugeben (vgl. Absatz 0007 der Streitpatentschrift).


Diese Aufgabe soll ausweislich von Absatz 0008 der Streitpatentschrift mittels
einer Strukturierung der Suche nach aggregierten Steuerkanälen in der Weise
gelöst werden, dass die aggregierten Steuerkanäle logisch in einer Baumstruktur
angeordnet werden, die dann auf systematische Art und Weise reduziert bzw.
verkleinert werde.


Gelöst werden soll dies netzwerkseitig durch ein Verfahren für eine Netzwerkkomponente (a method for a network device) und eine Netzwerkkomponente in einem
LTE-Netzwerksystem (network device in a LTE network system) mit den Merkmalen der Patentansprüche 1 und 8, nutzerseitig durch ein Verfahren in einer Nutzerkomponente (a method in a user device) und eine Nutzerkomponente (a user device) in einem LTE-Netzwerksystem mit den Merkmalen nach den Patentansprüchen 5 und 11 sowie ein Computerprogrammprodukt (a computer program product) mit den Merkmalen des Patentanspruchs 14.


2.      Die erteilten unabhängigen Ansprüche können wie folgt gegliedert werden:

                                  - 30 -



Anspruch 1
     1.1      A method for a network device of a LTE network system comprising:
     1.2      allocating control channels
     1.2.1b          represented by nodes of a tree structure,
     1.3      wherein nodes of the tree structure at a highest level of the
              tree structure represent control channel elements,
     1.4.1    and wherein each control channel of the control channels
              comprises at least one of the control channel elements
     1.4.2    carrying information for a respective identifier used to detect
              the control channel,
              characterized in that
     1.5      the allocation is performed by limiting allocation of highest
              level control channels,
     1.5.1           the highest level control channels being represented by
                     the nodes of the tree structure at the highest level of the
                     tree structure,
     1.6      thereby allowing allocation of lower level control channels,
     1.6.1           the lower level control channels being represented by
                     nodes of the tree structure at lower levels of the tree
                     structure.


Anspruch 5
      5.1     A method in a user device of a LTE network system comprising:
     5.2      searching for a control channel
     5.2.1a          by decoding control channels
     5.2.1b          represented by nodes of a tree structure,
     5.2.2           by using an identifier,
     5.3      wherein nodes of the tree structure at a highest level of the
              tree structure represent control channel elements,
     5.4.1    and wherein each control channel of the control channels
              comprises at least one of the control channel elements

                                  - 31 -



     5.4.2    carrying information for a respective identifier used to detect
              the control channel,
              characterized in that
     5.5      the searching is limited for highest level control channels,
     5.5.1           the highest level control channels being represented by
                     the nodes of the tree structure at the highest level of the
                     tree structure,
     5.6      thereby allowing searching for lower level control channels,
     5.6.1           the lower level control channels being represented by
                     nodes of the tree structure at lower levels of the tree
                     structure.


Anspruch 8
      8.1     A network device in a LTE network system (20) comprising:
     8.2      an allocation unit (22) configured to allocate control channels
     8.2.1b          represented by nodes of a tree structure,
     8.3      wherein nodes of the tree structure at a highest level of the
              tree structure represent control channel elements,
     8.4.1    and wherein each control channel of the control channels
              comprises at least one of the control channel elements
     8.4.2    carrying information for a respective identifier used to detect
              the control channel,
              characterized in that
     8.5      the allocation unit (22) is configured to limit allocation of highest level control channels,
     8.5.1           the highest level control channels being represented by
                     the nodes of the tree structure at the highest level of the
                     tree structure,
     8.6      thereby allowing allocation of lower level control channels,
     8.6.1           the lower level control channels being represented by
                     nodes of the tree structure at lower levels of the tree
                     structure.

                                         - 32 -



Anspruch 11
      11.1           A user device in a LTE network system (10) comprising:
      11.2           a decoding unit (12) configured to search for a control channel
      11.2.1a               by decoding control channels
      11.2.1b               represented by nodes of a tree structure,
      11.2.2                by using an identifier,
      11.3           wherein nodes of the tree structure at a highest level of the
                     tree structure represent control channel elements,
      11.4.1         and wherein each control channel of the control channels
                     comprises at least one of the control channel elements
      11.4.2         carrying information for a respective identifier used to detect
                     the control channel,
                     characterized in that
      11.5           the decoding unit (12) is configured to limit searching for highest level control channels,
      11.5.1                the highest level control channels being represented by
                            the nodes of the tree structure at the highest level of the
                            tree structure,
      11.6           thereby allowing searching for lower level control channels,
      11.6.1                the lower level control channels being represented by
                            nodes of the tree structure at lower levels of the tree
                            structure.



Der erteilte nebengeordnete Patentanspruch 14 hat folgenden Wortlaut:


               A computer program product including a program for a processing
               device, comprising executable instructions for performing the steps of
               any one of claims 1 to 7 when the program is run on the processing
               device.

                                       - 33 -



3.    Die Merkmale in diesen Ansprüchen bedürfen der Auslegung. Der zuständige Fachmann, ein Ingenieur der Nachrichtentechnik, Elektrotechnik oder Informationstechnik mit Hochschulabschluss und mehrjähriger Erfahrung auf dem Gebiet der Datenübertragung in mobilen Kommunikationssystemen, der mit den relevanten Mobilfunkstandards auf diesem Gebiet vertraut ist und die aktuellen Standardisierungsbemühungen auf diesem Gebiet verfolgt, versteht sie wie folgt:


3.1   Der erteilte Anspruch 1 ist gemäß Merkmal 1.1 auf ein Verfahren für eine
Netzwerkkomponente (engl. network device) in einem LTE-Netzwerksystem
gerichtet (LTE network system). Das Streitpatent bezieht sich hierbei gemäß
Absatz 0001 auf LTE (Long Term Evolution) Netzwerksysteme im Sinne des
3GPP (3rd Generation Partnership Project). Das Streitpatent nennt „eNB“ (evolved
Node B) als Beispiel für eine solche Netzwerkkomponente (vgl. Streitpatent, Abs.
0033), was die Weiterentwicklung von Basisstationen in älteren Mobilfunk-Generationen darstellt.


Das Verfahren nach Anspruch 1 umfasst gemäß Merkmal 1.2 das Allokieren bzw.
Zuordnen von Steuerkanälen (allocating control channels). Dabei werden einem
Nutzer Ressourcen in einer Zelle eines LTE Netzwerksystems zugeordnet, wobei
es sich bei den hier genannten Steuerkanälen jeweils um den Physical Downlink
Shared Control Channel (PDSCCH) handelt, mit dem unter anderem Schedulingbzw. Zuweisungsdaten für die Nutzerkomponenten übertragen werden (vgl. Streitpatent, Abs. 0014).


Vor dem Hintergrund einer erforderlichen Flexibilität seitens der Basisstation (eNb)
in der Bereitstellung geeigneter Steuerkanäle für Nutzerkomponenten (vgl. Streitpatent, Absatz 0008) erläutert das Streitpatent im Zusammenhang mit Figur 3,
dass beispielsweise das Vorsehen von sechs Steuerkanalelementen (control
channel elements) zu einem Satz von 10 Steuerkanalkandidaten (control channel
candidate bzw. CCH candidate) führen kann, welche die Nutzerkomponente alle
als für sie in Frage kommende Steuerkanäle demodulieren, decodieren und überprüfen müsste (vgl. Absatz 0019, 0024).

                                      - 34 -




                                                              Fig. 3


Die Steuerkanalkandidaten sind entweder einem einzelnen Steuerkanalelement
zugeordnet (im Beispiel CCH candidates 1 - 6), oder einer Aggregation von Steuerkanalelementen (im Beispiel CCH candidates 7 - 10; vgl. auch Streitpatent, Abs.
0014). So wird im Beispiel der Figur 3 der Steuerkanalkandidat 7 durch eine Aggregation der Steuerkanalelemente 0 und 1 gebildet, während der Steuerkanalkandidat 10 eine Aggregation der Steuerkanalelemente 0 bis 3 darstellt. Ein Steuerkanalkandidat wird im Streitpatent auch als ein „Code Block“ (CB) bezeichnet
(vgl. Streitpatent, Abs. 0014). Die Steuerkanalkandidaten bzw. Code-Blocks können als Knoten (nodes) einer Baumstruktur (tree structure) dargestellt werden
(Merkmal 1.2.1b). Ein Beispiel einer solchen Baumstruktur zeigt Figur 1 des
Streitpatents:




                                                              Fig. 1


Gemäß Merkmal 1.5.1 werden die Steuerkanäle der höchsten Ebene durch die
Knoten der Baumstruktur auf der höchsten Ebene der Baumstruktur dargestellt
(vgl. Streitpatent: Level 3 in Figur 1 und Abs. 0022). Die Steuerkanäle niedrigerer
Ebenen werden nach Merkmal 1.6.1 durch Knoten der Baumstruktur auf den niedrigeren Ebenen der Baumstruktur dargestellt. Dabei stellen gemäß Merkmal 1.3

                                       - 35 -



Knoten der Baumstruktur auf einer höchsten Ebene der Baumstruktur Steuerkanalelemente dar (control channel element / CCE). Aus dieser Struktur ergibt sich
auch, dass jeder der Steuerkanäle entsprechend Merkmal 1.4.1 dabei mindestens
ein Steuerkanalelement umfasst (Control Channel Element; vgl. beispielsweise
Fig. 3). Dieses Steuerkanalelement transportiert Informationen für einen (entsprechenden) Identifikator (…carrying information for a respective identifier), der von
der jeweiligen Nutzerkomponente (user device) zum Detektieren des Steuerkanals
verwendet wird (used to detect…) (Merkmal 1.4.2). Das anspruchsgemäße
Steuerelement muss dabei jedoch nicht zwingend den Identifikator selbst enthalten. Anspruch 1 legt zudem die Art des Identifikators nicht fest, wobei das Streitpatent in den Ausführungsbeispielen davon ausgeht, dass es sich um einen Identifikator der Nutzerkomponente handelt („MAC ID“, Abs. 0018, 0040; „a receiver
specific c-RNTI identity“, Abs. 0019, 0040).


Das Verfahren nach Anspruch 1 ist dadurch gekennzeichnet, dass ein Allokieren
(„allocating“, in der deutschen Übersetzung des Streitpatents auch als „Zuordnen“
bezeichnet) erfolgt, indem die Zuordnung der Steuerkanäle auf der obersten
Ebene der Baumstruktur begrenzt wird (Merkmal 1.5), was so zu verstehen ist,
dass nicht alle Steuerkanalelemente der höchsten Ebene, die nach Merkmal 1.5.1
durch die Knoten der höchsten Ebene der Baustruktur repräsentiert werden,
durchsucht werden (vgl. Abs. 0038, 0040 i. V. m. Abs. 0027, 0031). Nähere Angaben zur Auswahl der nicht zu durchsuchenden Elemente der höchsten Ebene
macht der Anspruch nicht.


Durch die Begrenzung nach Merkmal 1.5 soll gemäß Merkmal 1.6 das Zuordnen
von Steuerkanälen niedrigerer Ebenen ermöglicht werden (thereby allowing allocation…), welche nach Merkmal 1.6.1 durch die Knoten der Baumstruktur auf den
niedrigeren Ebenen repräsentiert werden. Ein Allokieren in höheren Ebenen der
Baumstruktur schließt allerdings ein Allokieren in niedrigeren Ebenen der Baumstruktur nicht grundsätzlich aus, da es sich bei allen Knoten der Baumstruktur um
allokier- bzw. zuordenbare Steuerkanäle handelt (vgl. Streitpatent, Abs. 0020 bis
0024). Damit stellt Merkmal 1.6 für die beanspruchte Komponente weder eine Be-

                                     - 36 -



schränkung noch eine Besonderheit dar. Die Aussage des Merkmals ist vielmehr
im Zusammenhang mit der in LTE-Netzwerksystemen durch die Länge der sogenannten Subframes begrenzten Zeit für das Verarbeiten von Steuerkanälen innerhalb des jeweiligen Subframes zu sehen (vgl. Streitpatent Abs. 0002). Betrachtet
man das Allokieren unter dieser zeitlichen Randbedingung, steht bei einer Begrenzung der Zahl der Steuerkanäle auf der höchsten Ebene (also bei einer Reduzierung der zu verwendenden Code-Blocks auf der höchsten Ebene) systembedingt mehr Zeit zur Verarbeitung von Steuerkanälen auf den niedrigeren Ebenen
der Baumstruktur zur Verfügung.


3.2   Korrespondierend zum Verfahren für eine Netzwerkkomponente (network
device) nach Anspruch 1 gibt der erteilte Anspruch 5 das Verfahren in einer Nutzerkomponente (user device) eines LTE Netzwerksystems wieder (Merkmal 5.1)
und betrifft gemäß Merkmal 5.2 das Suchen nach einem Steuerkanal (searching
for a control channel). Unter einer Nutzerkomponente (user device) versteht das
Streitpatent jedes Gerät, mit dem ein Nutzer mit dem Netzwerk kommunizieren
kann, und das im Netzwerk als Client oder Server oder beides auftreten kann (vgl.
Streitpatent, Abs. 0011). Das Suchen eines Steuerkanals bedeutet für die Nutzerkomponente, dass sie aus allen in der Netzwerk-Zelle übermittelten Steuerdaten
die für sie relevanten Steuerdaten bestimmen muss. Die Suche erfolgt durch Decodieren von Steuerkanälen (Merkmal 5.2.1a), die durch Knoten einer Baumstruktur dargestellt werden (Merkmal 5.2.1b), unter Verwendung eines Identifikators (Merkmal 5.2.2). Aus der Formulierung „unter Verwendung eines Identifikators“ in der Merkmalsgruppe 5.2 geht nicht eindeutig hervor, ob sich der Rückbezug auf das „Suchen nach einem Steuerkanal“ oder das „Decodieren von Steuerkanälen“ bezieht (vgl. Merkmal in der englischsprachigen Version: searching for a
control channel by decoding control channels represented by nodes of a treestructure, by using an identifier). Ausgehend von der Beschreibung des Streitpatents, das sich in den Absätzen 0014, 0018, 0019 und 0040 näher mit dem Identifizieren eines Steuerkanals für die Nutzerkomponente befasst, versteht der Fachmann die Merkmalsgruppe 5.2 so, dass die Suche nach einem Steuerkanal unter
Verwendung des Identifikators erfolgt. Für ein Verständnis im Sinne eines nutzer-

                                      - 37 -



seitigen Decodierens der Steuerkanäle unter Verwendung des Identifikators, mithin einer Doppelfunktion des Identifikators zum Decodieren und Detektieren (vgl.
Merkmale 5.2.1a i.V.m. 5.2.2 und 5.4.2), findet sich im Streitpatent dagegen kein
Hinweis. Der Empfänger, im vorliegenden Fall die Nutzerkomponente, demoduliert
und decodiert die sogenannten Subcarrierer der OFDM-Symbole, ohne dass das
Streitpatent hierzu auf eine Verwendung des Identifikators verweist. Da die Systembandbreite und die Größe des Code-Blocks (d. h. des Steuerkanalkandidaten,
vgl. Abs. 0014) bekannt sind, kennt der Empfänger die Subcarrierer, die als Kandidaten für einen Code-Block in Frage kommen. Ob das Demodulieren und Decodieren des Steuerkanalkandidaten fehlerfrei erfolgt ist, wird beispielsweise anhand
einer CRC-Prüfung (cyclic reduncancy check) festgestellt; ob dieser als Steuerkanal für den Empfänger bzw. die Nutzerkomponente erkannt wurde, kann dabei
zusammen mit der CRC-Prüfung anhand einer empfängerspezifischen c-RNTI ID
(d. h. anhand des Identifikators) gefiltert werden (vgl. Streitpatent, Abs. 0019).
Auch ein netzwerkseitiges Codieren unter Verwendung des Identifikators, das die
Voraussetzung für ein entsprechendes nutzerseitiges Decodieren und damit eine
Hinweis auf eine Doppelfunktion des Identifikators wäre, ist weder der Beschreibung des Streitpatents noch den weiteren Patentansprüchen zu entnehmen.


Die Baumstruktur zur Beschreibung der Steuerkanäle ist nutzerseitig in den
Merkmalen 5.3, 5.4.1, 5.4.2, 5.5.1 und 5.6.1 des Anspruchs 5 in gleicher Weise
wie netzwerkseitig in Anspruch 1 definiert (vgl. Merkmale 1.3, 1.4.1, 1.4.2, 1.5.1
und 1.6.1).


Das Verfahren nach Anspruch 5 ist dadurch gekennzeichnet, dass das Suchen
für Steuerkanäle auf der obersten Ebene der Baumstruktur begrenzt ist
(Merkmal 5.5), was analog zum netzwerkseitigen Allokieren (vgl. Anspruch 1) so
zu verstehen ist, dass nicht alle Steuerkanalelemente der höchsten Ebene
durchsucht werden müssen (vgl. Abs. 0040 i. V. m. Abs. 0027, 0031). Durch die
Begrenzung nach Merkmal 5.5 soll gemäß Merkmal 5.6 das Suchen von
Steuerkanälen niedrigerer Ebenen ermöglicht werden. Wie beim netzwerkseitigen
Allokieren ist ein solches Durchsuchen weder grundsätzlich durch den LTE-

                                          - 38 -



Standard noch durch andere Anspruchsmerkmale ausgeschlossen; vielmehr
handelt es sich bei allen Knoten auf allen Ebenen der Baumstruktur um
Steuerkanalkandidaten, die Informationen für die Nutzerkomponente enthalten
können und daher durchsucht werden müssen. Die LTE-Technologie definiert
jedoch, wie das Streitpatent in Absatz 0002 ausführt, ein Paket-Funk-System
(packet radio system), in dem alle Kanalzuweisungen (channel allocation) in sehr
kurzen Zeitabständen erfolgen müssen, die durch die Dauer der Subframes des
Systems vorgegeben sind. Hieraus folgt, dass auch für ein nutzerseitiges
Durchsuchen (searching) der Steuerkanäle nur eine begrenzte Zeit zur Verfügung
steht. Dies wird im Streitpatent bei der Betrachtung des Aufwands zum
netzwerkseitigen      Allokieren   wie   auch      zum   nutzerseitigen   Suchen   nach
Steuerkanälen für eine Nutzerkomponente vorausgesetzt. Bei einer solchen
systembedingten zeitlichen Begrenzung, die ein Durchsuchen aller Kandidaten in
einem Schritt – d. h. ein Durchsuchen der gesamten Baumstruktur innerhalb eines
zeitlich begrenzten Subframes – nicht zulässt, führt eine Begrenzung der Anzahl
der zu durchsuchenden Kandidaten auf der höchsten Ebene (d. h. auf der Ebene
mit der größten Anzahl an Steuerkanal-Kandidaten) dazu, dass mehr Steuerkanal-Kandidaten auf den niedrigeren Ebenen durchsucht werden können.


Allgemein geht das Streitpatent davon aus, dass die Richtung, in der der Baum
durchsucht wird, beliebig ist (vgl. Abs. 0021); eine Richtung ist auch in Anspruch 5
nicht vorgegeben.


3.3   Der erteilte Anspruch 8 ist auf eine Netzwerkkomponente (network device)
in einem LTE-Netzwerksystem gerichtet (Merkmal 8.1). Diese weist nach den
Merkmalen 8.2 und 8.2.1b eine Zuordnungseinheit (allocation unit) auf, die dafür
konfiguriert ist, Steuerkanäle zuzuordnen, die durch Knoten einer Baumstruktur
dargestellt werden.


Die Definition der Baumstruktur zur Beschreibung der Steuerkanäle in den Merkmalen 8.3, 8.4.1, 8.4.2, 8.5.1 und 8.6.1 des Anspruchs 8 entspricht der Definition

                                       - 39 -



im Verfahren für eine Netzwerkkomponente in Anspruch 1 (vgl. Merkmale 1.3,
1.4.1, 1.4.2, 1.5.1 und 1.6.1).


Die Netzwerkkomponente (network device) nach Anspruch 8 ist dadurch gekennzeichnet, dass die Zuordnungseinheit dafür konfiguriert ist, die Zuordnung von
Steuerkanälen – wiederum entsprechend den Verfahrensmerkmalen nach Anspruch 1 – auf der obersten Ebene der Baumstruktur zu begrenzen (Merkmal
8.5), wodurch gemäß Merkmal 8.6 das Suchen von Steuerkanälen niedrigerer
Ebenen ermöglicht werden soll.


3.4    Anspruch 11 ist auf eine Nutzerkomponente (user device) in einem LTE-Netzwerksystem gerichtet (Merkmal 11.1). Diese weist eine Decodiereinheit auf,
die zum Suchen eines Steuerkanals (control channel) konfiguriert ist (Merkmal
11.2), wobei die Steuerkanäle durch Knoten einer Baumstruktur dargestellt werden (Merkmal 11.2.1.b). Die Decodiereinheit ist konfiguriert, durch Decodieren
von Steuerkanälen (by decoding control channels) und durch Verwendung eines
Identifikators (by using an identifier) nach einem Steuerkanal zu suchen (Merkmale 11.2.2, 11.2.1a). Für eine von der Beklagten / Patentinhaberin genannte
Doppelfunktion des Identifikators im Sinne eines Decodierens und Detektierens
findet sich, wie zu Anspruch 5 näher erläutert, kein Hinweis im Streitpatent.


Die Definition der Baumstruktur zur Beschreibung der Steuerkanäle in den Merkmalen 11.3, 11.4.1, 11.4.2, 11.5.1 und 11.6.1 des Anspruchs 11 entspricht der
Definition im Verfahren für eine Nutzerkomponente in Anspruch 5 (vgl. Merkmale
5.3, 5.4.1, 5.4.2, 5.5.1 und 5.6.1).


Die Nutzerkomponente (user device) nach Anspruch 11 ist dadurch gekennzeichnet, dass die Decodiereinheit dafür konfiguriert ist, auf der obersten Ebene der
Baumstruktur die Suche von Steuerkanälen zu begrenzen (Merkmal 11.5),
wodurch gemäß Merkmal 11.6 das Suchen von Steuerkanälen niedrigerer Ebenen ermöglicht werden soll.

                                         - 40 -



3.5     Der erteilte Anspruch 14 ist auf ein Computerprogrammprodukt gerichtet,
das Anweisungen zu Ausführen der Verfahrensschritte nach einem der Ansprüche
1 bis 7 enthält, wenn das Programm auf der entsprechenden Komponente ausgeführt wird.




                II.     Zum Hauptantrag (erteilte Anspruchsfassung)


In der erteilten Fassung ist das Streitpatent für nichtig zu erklären, weil es
gegenüber dem im Verfahren befindlichen Stand der Technik nicht patentfähig ist
(Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a), Art. 52 bis 57
EPÜ).


1.      Entgegen der Auffassung der Beklagten gehört die nachveröffentlichte
Patentanmeldung WO 2008/081004 A1 (Druckschrift K7) zum für die Beurteilung
der Neuheit relevanten Stand der Technik. Diese Anmeldung der NOKIA
CORPORATION vom 3. Januar 2008 ist zwar erst am 10. Juli 2008 veröffentlicht
worden. Die Anmeldung nimmt jedoch die Priorität US 60/878,079 vom
3. Januar 2007 in Anspruch, so dass diese Anmeldung nach Art. 89, 54 Abs. 3
EPÜ eine nachveröffentlichte ältere Anmeldung darstellt und hinsichtlich der
erforderlichen        Neuheit   der   Anspruchsgegenstände    relevant    ist.   Die
Nachanmelderin war dabei insbesondere zur Beanspruchung der Priorität der
Voranmeldung berechtigt. Die Prioritätsanmeldung (NB6) stammt zwar nicht von
der Nachanmelderin, der NOKIA CORPORATION, sondern von den Anmeldern
Mika Rinne, Olav E. Tirkkonen, Frank Frederiksen und Samuli Visuri. Mit dem als
Dokument K10 vorgelegten Auszug aus der Anmeldeakte hat die Klägerin jedoch
ein Assignment vom 7. März 2007 vorgelegt, mit dem die genannten Anmelder die
Anmeldung US 60/878,079 auf die Nokia Corporation übertragen haben.


2.      Der Gegenstand des Anspruchs 11 in der erteilten Fassung (Hauptantrag)
ist gegenüber Druckschrift K7 nicht neu (Art. 56 EPÜ).

                                        - 41 -



Der Fachmann entnimmt Druckschrift K7 eine Nutzerkomponente („user
equipment“, „UE“) in einem LTE-Netzwerksystem (vgl. „LTE“, S. 1, Z. 18-26; „E-UTRA“, „4G“, S. 8, Z. 16-22, „eNB“, S. 5, Z. 25-28; sowie S. 9, Z. 6-10 / Merkmal
11.1) gemäß Patentanspruch 11 in der erteilten Fassung. Die Nutzerkomponente
ist eingerichtet, um nach einem Steuerkanal (hier auch: „code block“) zu suchen,
indem Steuerkanäle („control channels“, „PDCCH“) decodiert werden (decoding
process), wobei der Fachmann mitliest, dass dies auch eine dazu geeignete Decodiereinheit in der Nutzerkomponente voraussetzt bzw. beinhaltet (vgl. S. 5, Z.
25-28 und S. 6, Z. 7-13 / Merkmale 11.2 und 11.2.1a). Die Suche nach einem
Steuerkanal erfolgt dabei unter Verwendung einer Geräteadresse in Form einer
Media-Access-Control-Adresse (MAC ID) als Identifikator („search for a UE specific MAC ID“, vgl. S: 5, Z. 25-28 sowie S. 12, Z. 10-12 und 27-29 / Merkmal
11.2.2).


Druckschrift K7 geht davon aus, dass die kleinsten Steuerkanäle in Form von sogenannten „Code Blocks“ auf einer ersten, höchsten Ebene vorliegen, aus denen
alle Steuerkanäle der niedrigeren Ebenen aufgebaut sind (vgl. S. 13, Z. 7-17; S.
12, Z. 29 bis S. 13, Z. 1; sowie Fig. 4 und S. 12, Z. 14-20). Hieraus folgt, dass jeder Steuerkanal gemäß Druckschrift K7 mindestens einen als Steuerkanalelement
anzusehenden „Code Block“ der höchsten Ebene umfasst (Merkmale 11.3 und
11.4.1). Ein solches Steuerkanalelement transportiert als Teil des Steuerkanals
Informationen für den jeweiligen Identifikator („…carries information for one MAC
ID“; vgl. S. 12, Z. 10-12; sowie S. 14, Z. 22-30), wobei der Identifikator zum Detektieren des Steuerkanals verwendet wird („The MAC ID is used by a UE … to detect the channel“; S. 12, Z. 27-29) (Merkmal 11.4.2).


Jeder Steuerkanal („code block“) wird als Knoten („node“) einer Baumstruktur
(„tree“) dargestellt (vgl. Fig. 5 und 6; S. 12, Z. 25 bis S. 13, Z. 6 und S. 13, Z. 18-
20 / Merkmal 11.2.1b), wobei die Steuerkanäle der höchsten Ebene durch Knoten
auf der höchsten Ebene und Steuerkanäle der niedrigsten Ebene durch Knoten
auf der niedrigsten Ebene der Baumstruktur dargestellt sind (S. 13, Z. 7-17 i. V. m.
S. 20, Z. 5-9 / Merkmale 11.5.1 und 11.6.1).

                                       - 42 -



Gemäß Druckschrift K7 wird das Suchen nach Steuerkanälen in einer Baumstruktur beschränkt, indem der Baum auf allen Ebenen „beschnitten“ wird (vgl. S.
19, Z. 21-23: „pruned tree“). Dies bedeutet, dass unter anderem die Suche nach
Steuerkanälen auf der höchsten Ebene der Baumstruktur begrenzt wird, da ein
Beschneiden („pruning“) nach Druckschrift K7 einen Zweig der Baumstruktur und
damit Knoten auf allen Ebenen der Baumstruktur vom Durchsuchen ausnimmt
(vgl. S. 19, Z. 26-29 und Figuren 5, 6 / Merkmal 11.5). Diese Begrenzung der
Baumstruktur auf der höchsten Ebene nach Merkmal 11.5 ermöglicht damit das
Suchen nach Steuerkanälen der niedrigeren Ebenen, da dadurch weniger Steuerkanäle auf höchster Ebene durch die Nutzerkomponente durchsucht werden müssen (vgl. S. 19, Z. 22-23 / Merkmal 11.6).


Der Senat vermag der Beklagten nicht darin zu folgen, dass in der Verwendung
des Identifikators gemäß den Merkmalen 11.2.1a i.V.m. 11.2.2 und 11.4.2 eine
Doppelfunktion zu erkennen sei. Wie vorstehend im Zusammenhang mit der Auslegung der Ansprüche 5 und 11 näher ausgeführt, findet sich für dieses Verständnis keine Stütze in der Beschreibung des Patents.


Das Argument der Beklagten, dass Druckschrift K7 keine „Steuerkanalelemente“
(control channel elements; vgl. Merkmale 11.3 und 11.4.1) kenne, kann ebenfalls
nicht überzeugen. Es ist zwar zutreffend, dass Druckschrift K7 den Begriff „control
channel element“ nicht verwendet, jedoch weisen die kleinsten Steuerkanäle
(„code blocks“) auf der obersten Ebene der Baumstruktur gemäß Druckschrift K7
genau die Eigenschaften auf, mit denen das Streitpatent die „Steuerkanalelemente“ beschreibt. So legt das Streitpatent fest, dass es sich bei den als Steuerkanalelemente (control channel elements) bezeichneten Steuerkanälen um die
Steuerkanäle der höchsten Ebene der Baumstruktur handelt und dass Steuerkanäle bzw. „Code Blocks“ der niedrigeren Ebenen immer aus den Elementen der
höchsten Ebene aufgebaut bzw. aggregiert sind (vgl. Streitpatent, Abs. 0014,
Abs. 0022). Eine Anforderung, nach der es sich bei Steuerkanalelementen der
höchsten Baumebene um nicht weiter teilbare Steuerkanäle handele, wie die Beklagte geltend gemacht hat, ist dagegen auch dem Streitpatent nicht zu entneh-

                                          - 43 -



men. Zusätzlich sind bei der aus Druckschrift K7 bekannten Nutzerkomponente
auch die Bedingung der gleichen Größe aller Elemente der höchsten Ebene und
deren Abhängigkeit von der verfügbaren Bandbreite (vgl. Streitpatent, Abs. 0022)
erfüllt (vgl. S. 12, Z. 25 bis S. 13, Z. 20 mit Fig. 5, 6). Die Steuerkanäle der
höchsten Ebene der Baumstruktur gemäß Druckschrift K7 (vgl. Fig. 5, 6 und 13
mit Beschreibung a.a.O.) entsprechen daher der Definition von Steuerkanalelementen im Streitpatent (vgl. Abs. 0022 i.V.m. 0014).


Der Fachmann entnimmt somit der Druckschrift K7 alle Merkmale der Nutzerkomponente in einem LTE-Netzwerk gemäß Anspruch 11 in der erteilten Fassung. Der
Gegenstand des erteilten Patentanspruchs 11 ist daher nicht neu.


3.     Die weiteren Patentansprüche des Hauptantrags bedürfen keiner weiteren,
isolierten Prüfung, weil die Beklagte in der mündlichen Verhandlung zu erkennen
gegeben hat, dass sie den Hauptantrag als geschlossenen Anspruchssatz
versteht und das Streitpatent nur in der Reihenfolge des Hauptantrags und der
Hilfsanträge in der gemäß der in der mündlichen Verhandlung benannten
Reihenfolge jeweils als Ganzes verteidigt (vgl. BGH, Urteil vom 13. September
2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator).




              III.   Zu den Hilfsanträgen 1, 2, 2‘, 2a, 2a‘, 3, 4 und 5


Die Beklagte kann das Streitpatent auch nicht erfolgreich mit den Hilfsanträgen 1,
2, 2‘, 2a, 2a‘, 3, 4 und 5 verteidigen.


Im Einzelnen:


1.     Zum Hilfsantrag 1
Dem Gegenstand des Anspruchs 11 nach Hilfsantrag 1 steht ebenfalls der
Nichtigkeitsgrund der mangelnden Patentfähigkeit, nämlich der mangelnden

                                     - 44 -



Neuheit gegenüber Druckschrift K7 (Art. 138 Abs. 1 Buchstabe a) EPÜ, Art. II § 6
Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 54 EPÜ) entgegen.


Der unabhängige Anspruch 11 gemäß Hilfsantrag 1, der eine Nutzerkomponente
(user device) betrifft, basiert auf Anspruch 11 des Hauptantrags unter Änderung
des Merkmals 11.6:


       11.6’ thereby allowing and to increase searching for lower level control
             channels,


Auch   das   geänderte    Merkmal   11.6‘   ergibt   sich   zwangsläufig   aus   der
Beschränkung der Suche auf der höchsten Ebene der Baumstruktur nach
Merkmal 11.5. Denn aus dieser Beschränkung folgt implizit, dass für die Suche auf
den niedrigeren Ebenen mehr Zeit zur Verfügung steht, wenn auf der obersten
Ebene (d. h. der Ebene mit der größten Zahl an Steuerkanal-Kandidaten) nicht alle
Elemente durchsucht werden müssen. Da es sich auch bei den Knoten der
Baumstruktur auf den weiteren, niedrigeren Ebenen um Steuerkanalkandidaten
handelt, deren Durchsuchen daher ebenso angezeigt ist wie auf der höchsten
Ebene, folgt ein Durchsuchen von mehr Steuerkanälen auf den niedrigeren
Ebenen aus Druckschrift K7 damit bereits implizit daraus, dass weniger
Steuerkanal-Kandidaten auf der höchsten Ebene der Baumstruktur durchsucht
werden (Merkmal 11.6‘).


Bezüglich der weiteren, gegenüber der erteilten Fassung unveränderten Merkmale
wird auf die Ausführungen zum Hauptantrag verwiesen, die für den Hilfsantrag 1 in
gleicher Weise gelten.


Der Fachmann entnimmt der Druckschrift K7 somit auch eine Nutzerkomponente
mit allen Merkmalen des Anspruchs 11 nach Hilfsantrag 1. Der Gegenstand des
Anspruchs 11 gemäß Hilfsantrag 1 ist daher nicht neu.

                                         - 45 -



2.    Zu Hilfsantrag 2


Die unabhängigen Ansprüche 4 und 10 des Hilfsantrags 2 sind nicht zulässig.


Hilfsantrag 2 unterscheidet sich in den auf die Nutzerkomponente gerichteten Vorrichtungs- und Verfahrensansprüchen 4 und 10 von den entsprechenden Ansprüchen 5 und 11 gemäß Hilfsantrag 1 in der Ergänzung eines Merkmals 4.7 bzw.
10.7 am Ende des jeweiligen Anspruchs:


      4.7 / 10.7   wherein the searching is increased more the lower the level of
                   the tree structure.


Somit soll gemäß Anspruch 4 bzw. Anspruch 10 des Hilfsantrags 2 ein Suchen
von Kanälen in der Nutzerkomponente (user device) mehr bzw. weiter erhöht werden, je niedriger die Ebene der Baumstruktur ist (…is increased more the lower
the level). Dies bedeutet für den Fachmann, dass verstärkt Kanäle auf möglichst
niedriger Ebene durchsucht werden sollen.


Ein verstärktes Suchen von Steuerkanälen je niedriger die Ebene der Baumstruktur auf Seiten der Nutzerkomponente (user device) ist den ursprünglich eingereichten Unterlagen jedoch nicht zu entnehmen. Zwar ist gemäß den ursprünglichen Anmeldeunterlagen im Hinblick auf die Netzwerkkomponente (network device) ein verstärktes Zuordnen bzw. Allokieren von Steuerkanälen vorgesehen, je
niedriger die Ebene der Baumstruktur ist (vgl. EP 1 990 926 A1, Absatz 0036 und
Anspruch 5). Aus dem verstärkten Allokieren von Steuerkanälen je niedriger die
Ebene der Baumstruktur ist, folgt jedoch – entgegen den Ausführungen der Beklagten in der mündlichen Verhandlung – nicht zwangsläufig ein verstärktes Suchen auf den niedrigeren Ebenen. Der Ursprungsoffenbarung in Absatz 0042 der
EP 1 990 926 A1, auf welche die Beklagte in diesem Zusammenhang verweist, ist
kein Hinweis darauf zu entnehmen. Aus der Angabe, dass die Suche und das Allokieren auf der höchsten Ebene der Baumstruktur begrenzt ist, folgt nicht
zwangsläufig eine identische Vorgehensweise von Nutzer- und Netzwerkkompo-

                                      - 46 -



nente beim Suchen und Zuordnen bzw. Allokieren von Steuerkanälen auf den
weiteren, niedrigeren Ebenen. Vielmehr gibt das Streitpatent die Richtung, in der
der Baum nutzerseitig durchsucht wird, als beliebig an (vgl. Abs. 0021) und legt
diese auch in den Ansprüchen 4 bzw. 10 nicht fest. Außerdem sind grundsätzlich
alle Knoten der Baumstruktur mögliche Steuerkanalkandidaten, welche die Nutzerkomponente durchsuchen müsste. Somit ist der Ablauf beim Durchsuchen der
Steuerkanäle in Bezug auf die Baumstruktur nicht zwangsläufig der gleiche wie
beim netzwerkseitigen Allokieren von Steuerkanälen.


Die Merkmale 4.7 und 10.7 der Ansprüche 4 und 10 sind daher der
Ursprungsoffenbarung jeweils nicht unmittelbar und eindeutig zu entnehmen. Die
Gegenstände der Ansprüche 4 und 10 gemäß Hilfsantrag 2 gehen damit über den
Inhalt der Anmeldung in der ursprünglichen Fassung hinaus. Die Ansprüche 4 und
10 gemäß Hilfsantrag 2 sind daher nicht zulässig.


3.    Zum Hilfsantrag 2‘
Der erst in der mündlichen Verhandlung eingereichte Hilfsantrag 2‘ ist auf den
Antrag der Klägerin nach § 83 Abs. 4 PatG als verspätet zurückzuweisen.


Die Beklagte hat Hilfsantrag 2‘ über einen Monat nach Ablauf der im Hinweis
gesetzten Stellungnahmefrist (24. Mai 2019) vorgelegt. Soweit die Beklagte die
Dauer der Stellungnahmefrist als zu kurz beanstandet hat, ändert dies nichts an
der Fristversäumnis. Entgegen dem Vorbringen der Beklagten sind die gesetzten
Stellungnahmefristen nicht unbillig kurz gewählt. Denn soweit das Verfahrensrecht
überhaupt Mindestfristen für Stellungnahmen vorsieht (vgl. etwa § 82 Abs. 3 PatG;
§§ 132, 217, 274 Abs. 3 ZPO), belaufen sich diese in der Regel auf ein bis zwei
Wochen und höchstens auf einen Monat. Da die gesetzten Fristen diese
gesetzlichen Mindestfristen übersteigen, bestehen gegen die vorliegenden
Fristsetzungen – entgegen der Auffassung der Beklagten – keine Bedenken.


Die Beklagte hat die verspätete Vorlegung dieses Hilfsantrags auch nicht
hinreichend entschuldigt (§ 83 Abs. 4 Satz 1 Nr. 2 PatG), geschweige denn

                                           - 47 -



glaubhaft gemacht (§ 83 Abs. 4 Satz 2 PatG). Ihr mündlicher Hinweis auf
innerhalb     der   Frist   liegende   Feiertage    und   einen   nicht   verschiebbaren
Erholungsurlaub des Prozessbevollmächtigten der Beklagten reicht hierfür nicht
aus.


Die Parteien sind gehalten, sich vollständig zu allen verfahrensrelevanten
Tatsachen zu erklären (§ 99 Abs. 1 PatG i. V. m. § 138 Abs. 1 und 2 ZPO). Dazu
gehört auf Seiten der Beklagten auch die Vorlage möglicher Hilfsanträge. Dass sie
sich dessen bewusst war, belegen ihre mit Schriftsatz vom 24. Mai 2019
vorgelegten Hilfsanträge 2a, 4 und 5. Die Beklagte selbst hat im Termin
eingeräumt, dass Hilfsantrag 2‘ bereits vor dem Termin vorbereitet worden sei und
keine Reaktion auf den Verlauf der mündlichen Verhandlung war.


Eine Berücksichtigung des Hilfsantrags 2‘ hätte auch die Vertagung der bereits
begonnenen mündlichen Verhandlung erforderlich gemacht (§ 83 Abs. 4 Satz 1
Nr. 1 PatG). Ein weiterer Termin nach § 99 Abs. 1 PatG i. V. m. § 227 Abs. 1 ZPO
wäre erforderlich gewesen, weil der Senat der Klägerin hätte Gelegenheit geben
müssen, nach einschlägigem Stand der Technik bezüglich Hilfsantrag 2‘ zu
recherchieren, zumal Hilfsantrag 2‘ im geänderten Patentanspruch 4 erstmals die
Funktion der Nutzerkomponente (user device) direkt mit der Allokation von
Steuerkanälen in der Netzwerkkomponente (network device) verknüpft. Es handelt
sich insoweit nicht um eine ganz geringfügige Änderung in den verteidigten
Patentansprüchen (BPatG, Urteil vom 30. Dezember 2012, 10 Ni 6/11 –
Wiedergabeschutzverfahren).


Hilfsantrag 2‘ ist eine neue „Verteidigungslinie“ und konfrontiert die Klägerin mit
neuen Tatsachen. Es war ihr nicht zuzumuten, sich hiermit aus dem Stand
auseinanderzusetzen. Die für eine sachgerechte Auseinandersetzung mit
Hilfsantrag    2‘   erforderliche   Zeit   konnte   der   Klägerin   nicht   durch   eine
Unterbrechung der mündlichen Verhandlung am 26. Juni 2019 in ausreichender
Weise zur Verfügung gestellt werden (BGH, Urteil vom 13. Januar 2004, X ZR
212/02 - Crimpwerkzeug I). Auch war die Einräumung einer nachträglichen
Schriftsatzfrist nach § 283 ZPO kein geeignetes Mittel, eine Fortsetzung der

                                        - 48 -



mündlichen Verhandlung zu vermeiden, weil der Schriftsatznachlass nur eine
einseitige Stellungnahme ermöglicht (Busse, PatG, 8. Aufl., § 83 Rn. 32 m.w.N.).


Die Beklagte ist in dem qualifizierten Hinweis vom 26. April 2019 auch über die
Folgen einer Fristversäumung belehrt worden, so dass die Voraussetzungen für
eine Zurückweisung von Hilfsantrag 2‘ als verspätet vorliegen.


4.    Zum Hilfsantrag 2a


Die Ansprüche 4 und 10 des Hilfsantrags 2a sind nicht zulässig.


Hilfsantrag 2a unterscheidet sich in den eine Nutzerkomponente (user device) betreffenden Ansprüchen 4 und 10 von den entsprechenden Ansprüchen 4 und 10
gemäß Hilfsantrag 2 unter Ersetzung des Merkmals 7 durch die nachfolgenden
Merkmale 4.8 und 4.9 bzw. 10.8 und 10.9 am Ende des jeweiligen Anspruchs:


      4.8 / 10.8    wherein the identifier is a C-RNTI and
      4.9 / 10.9    wherein correct detection of the control channel is recognized
                    by a Cyclic Redundancy Check detector filtered by the C-RNTI.


Merkmal 4.9 bzw. 10.9 der unabhängigen Ansprüche 4 und 10 des Hilfsantrags 2a
ist den Anmeldunterlagen nicht in Verbindung mit einem beliebigen C-RNTI
Identifikator gemäß dem jeweiligen Merkmal 4.8 bzw. 10.8 zu entnehmen. Denn
die   dem   Merkmal     4.9   bzw.    10.9    zugrunde    liegende    Textstelle   (vgl.
EP 1 990 926 A1,    Absatz    0016)    geht      diesbezüglich   lediglich   von   einer
empfängerspezifischen c-RNTI Identität („receiver specific c-RNTI identity“) aus,
also von einem empfängerspezifischen Identifikator. Damit ist das Merkmal 4.9
bzw. 10.9 in Verbindung mit Merkmal 4.8 bzw. 10.8 gegenüber dem Inhalt der
Ursprungsoffenbarung verallgemeinert und dabei der Ursprungsoffenbarung nicht
unmittelbar und eindeutig zu entnehmen. Die Ansprüche 4 und 10 gemäß
Hilfsantrag 2a sind daher nicht zulässig.

                                           - 49 -



5.    Zum Hilfsantrag 2a‘


Dem       Gegenstand    des    Anspruchs     11     nach    Hilfsantrag     2a‘    steht    der
Nichtigkeitsgrund der mangelnden Patentfähigkeit, nämlich der mangelnden
erfinderischen Tätigkeit gegenüber dem Stand der Technik der Entgegenhaltung
K4 in Verbindung mit dem allgemeinen Fachwissen entgegen (Art. 138 Abs. 1
Buchstabe a) EPÜ, Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 56 EPÜ).


a)    Entgegen der Auffassung der Beklagten gehört das Dokument „R1-
072220“      des     3GPP-Arbeitsgruppentreffens           „3GPP    TSG       RAN          WG1
#49“ (Dokument K4) zum Stand der Technik. Aus den Anlagen K4a bis K4d und
der Funktion des 3GPP-Portals bzw. –Servers ergibt sich, dass das in den
Veröffentlichungslisten       angegebene       Datum        (2. Mai 2007)         auch     das
Veröffentlichungsdatum ist und somit, dass das Dokument K4 am 7. Mai 2007
bereits vorveröffentlicht war. Dokumente wie K4 dienen der Vorbereitung von
Treffen     der    Arbeitsgruppen   (mit     über     200     Teilnehmern),        hier    des
Arbeitsgruppentreffens „3GG TSG RAN WG1 #49“ in Kobe (Japan), das vom
7. Mai bis 11. Mai 2007 stattgefunden hat. Eine Bereitstellung vor dem Treffen war
nicht nur zu erwarten, sondern ist auch belegt. Nach Überzeugung des Senats war
das Dokument K4 ab dem 2. Mai 2007 auch für die Öffentlichkeit zugänglich, weil
der Server der Fachöffentlichkeit zugänglich war (vgl. BPatG Urteil vom
1. August 2012 – 5 Ni 24/10; BPatG Urteil vom 13. Januar 2010 – 5 Ni 32/09 Rn.
108). Es ist unerheblich, ob das Dokument K4 als pdf-Datei oder, zur Begrenzung
des Speicherplatzbedarfs, als zip-Datei abgelegt wurde. Die Beklagte hat auf den
gerichtlichen Hinweis, in dem auf diese Einschätzung hingewiesen worden war,
keine Tatsachen vorgetragen, die nahelegen, dass Druckschrift K4 auf dem ftp-Server nicht frei zugänglich war oder dass das auf den Servern des 3GPP zur
Verfügung gestellte Dokument K4 nachträglich verändert worden ist.


b)    Die Merkmale 10.1 bis 10.5.1, 10.6‘ und 10.6.1 des Anspruchs 10 nach
Hilfsantrag 2a‘ entsprechen den Merkmalen 11.1 bis 11.5.1, 11.6‘ und 11.6.1 des

                                      - 50 -



Hilfsantrags 1. Anspruch 10 gemäß Hilfsantrag 2a‘ ergänzt die folgenden
Merkmale 10.8‘ und 10.9‘ am Ende des Anspruchs:


      10.8’        wherein the identifier is a receiver specific C-RNTI and
      10.9’        wherein correct detection of the control channel is recognized
                   by a Cyclic Redundancy Check detector filtered by the receiver specific C-RNTI.


c)    Es kann dahinstehen, ob die ergänzten Merkmale 10.8‘ und 10.9‘ bereits
Druckschrift K7 entnehmbar sind. Denn der Gegenstand des Anspruchs 10 nach
Hilfsantrag 2a‘ ist dem Fachmann durch den Stand der Technik gemäß der
Druckschrift K4 in Verbindung mit dem Fachwissen, wie es durch die
Druckschriften K4e und K11 dokumentiert ist, nahegelegt.


Druckschrift K4 ist eine Nutzerkomponente („UE“, vgl. Kap. 1 Introduction) zu entnehmen. Die Verwendung in einem LTE-Netzwerksystem (LTE network system)
wird zwar nicht ausdrücklich genannt, jedoch liest der Fachmann diesen Zusammenhang bereits aufgrund der verwendeten Begriffe („PDCCH“, „CCE“, „subframe“, …) mit (Merkmal 10.1). Die Nutzereinheit („UE“) umfasst eine Decodiereinheit, die konfiguriert ist, nach einem Steuerkanal zu suchen, indem Steuerkanäle decodiert werden („…set of candidate control channels monitored by a UE“,
Kap. 1, erster Spiegelstrich; i. V. m. „blind decoding attempts by a UE“, Kap. 1,
zweiter Spiegelstrich / Merkmale 10.2 und 10.2.1a).


Die Verwendung eines Identifikators bei der Suche nach einem Steuerkanal (vgl.
Merkmal 10.2.2) ist nicht explizit genannt. Das Merkmal ergibt sich entgegen dem
Vortrag der Klägerin auch nicht zwingend aus dem Begriff „blind decoding“, da
dieser sich nur auf den Decodiervorgang der Steuerkanäle selbst (vgl. Merkmal
10.2.1a), nicht aber auf das Identifizieren des Steuerkanals im Rahmen der der
Suche bezieht. Hierbei fordert das „blind decoding“ nur ein Erkennen, ob das Decodieren erfolgreich war, was beispielsweise durch einen CRC (cyclic redundancy
check) erreicht wird. Jedoch dient die in Druckschrift K4 genannte „UE ID“ der

                                       - 51 -



Festlegung des Satzes an Steuerkanal-Kandidaten („candidate control channels“
bzw. „PDCCH candidate“; vgl. Fig. 3 mit Beschreibung), zu der UE und eNb in der
Lage sein sollen („…both eNb and UE can figure out…“; vgl. Kap. 2.3, dritter Abs.,
1. Satz i. V. m. Fig. 3). Seitens der Nutzerkomponente („UE“) werden nur „candidate control channels“ überwacht, welche unter anderem durch diese „UE ID“
festgelegt werden. Damit wird der Identifikator („UE ID“) zumindest indirekt – im
Zusammenhang mit der Festlegung der Teilmenge der zu prüfenden Steuerkanal-Kandidaten – auch zum Suchen sowie dem Detektieren des Steuerkanals verwendet (Merkmale 10.2.2 und 10.4.2).


Jeder der möglichen Steuerkanalkandidaten („PDCCH candidate“) umfasst dabei
zumindest ein Steuerkanalelement („CCE“) (vgl. Fig. 1 / Merkmal 10.4.1). Wenn
man die „UE ID“ als Identifikator selbst identifiziert, ist das Umfassen von Informationen für einen jeweiligen Identifikator durch die Steuerkanalelemente gemäß
Merkmal 10.4.2 in Druckschrift K4 nicht explizit genannt, da der Identifikator nicht
mit dem Inhalt der Steuerkanalelemente gleichzusetzen ist. Jedoch liest der
Fachmann mit, dass ein Steuerkanal, der sich aufgrund des entsprechenden Identifikators an eine bestimmte Nutzerkomponente richtet, auch Informationen für
diese Nutzerkomponente enthält (Merkmal 10.4.2).


Figur 1 der Druckschrift K4:            Figur 3 des Streitpatents:




Bei der Darstellung in Figur 1 der Druckschrift K4 handelt es sich um eine alternative Darstellung einer Baumstruktur, die – ebenso wie Figur 3 des Streitpatents –
auch in Form eines „Baumes“ dargestellt werden kann, wie ihn Figur 1 des Streitpatents zeigt. Denn aus Figur 1 der Druckschrift K4 folgt eine entsprechende Hie-

                                       - 52 -



rarchie der Steuerkanalkandidaten („PDCCH candidates“), bestehend aus einem,
zwei oder vier Steuerkanalementen („control channes elements“, „CCEs“) sowie
eine eindeutige Zuordnung von Kindelementen (einer im Sinne des Streitpatents
höheren Ebene) zu Elternelementen (der jeweils darunterliegenden Ebene), d. h.
es besteht eine feste und eindeutige Zuordnung von Steuerkanalelementen
(„CCE“) der höchsten Ebene zu den Steuerkanalkandidaten („PDCCH candidates“) der darunterliegenden Ebenen. Daher entnimmt der Fachmann Druckschrift K4, dass die Steuerkanalkandidaten („PDCCH candidates“) der Figur 1
sinngemäß Knoten einer Baumstruktur bilden (Merkmal 10.2.1b). Dabei sind die
Elemente auf der höchsten Ebene Steuerkanalelemente („control channel Element“ bzw. „CCE“ / Merkmal 10.3), die als „Knoten“ auf der höchsten Ebene der
Baumstruktur angesehen werden können (Merkmal 10.5.1). Die Steuerkanalkandidaten auf der niedrigsten Ebene entsprechen daher den „Knoten“ auf der niedrigsten Ebene der Baumstruktur (Merkmal 10.6.1).


Die Suche nach Steuerkanälen („PDCCH candidates“) ist gemäß Druckschrift K4
– unter anderem – auf der höchsten Ebene begrenzt, indem auf der höchsten
Ebene mit einzelnen Steuerkanalelementen nur „PDCCH candidates“ 1 und 3
(blaue Schrift in der Originalveröffentlichung) vorgesehen sind (vgl. Figur 1 und
Kap. 2.1, dritter Satz / Merkmal 10.5). Durch das Begrenzen der Suche auf der
obersten Ebene (durch ausschließen der „PDCCH candidates“ 1 und 3 in Figur 1)
erfolgt eine verstärkte Suche auf den niedrigeren Ebenen, da die oberste Ebene in
der systembedingt begrenzten zur Verfügung stehenden Zeit aufgrund der Beschränkung nach Merkmal 10.5 nicht vollständig durchsucht werden muss (vgl.
Figur 1 und Kap. 2.1, dritter Satz / Merkmal 10.6‘).


Dokument K4e (3GPP TS 36.300), eine „Technical Specification“ aus dem LTE/E-UTRA Standardisierungsverfahren, welche in der vorgelegten Version zum
Anmeldezeitpunkt Teil der technischen Grundlagen für LTE Netzwerksysteme war,
dokumentiert das Fachwissens des Fachmanns, der zu diesem Zeitpunkt mit der
Fortentwicklung von LTE Mobilfunksystemen befasst war. Druckschrift K4e
beschreibt, dass in einem standardkonformen LTE Netzwerksystem in der Regel

                                         - 53 -



der C-RNTI als Identifikator für die Nutzerkomponente („UE ID“) dient („The C-RNTI provides a unique UE identification at the cell level identifying RRC
Connection; It is assumed that this identity is used for scheduling unless the cost
would turn out to be too high and the introduction of a separate MAC identity
would be required.“; vgl. S. 37, Abs. 8.1 a) / Merkmal 10.8’).


Dokument K11 (3GPP TS 36.212), eine weitere „Technical Specification“ aus dem
LTE/E-UTRA Standardisierungsverfahren, die wie Druckschrift K4e in der
vorgelegten Version zum Anmeldezeitpunkt Teil der technischen Grundlagen für
LTE-Netzwerksysteme war und ebenfalls das Fachwissen bezüglich LTE-Mobilfunksystemen vor dem Anmeldezeitpunkt dokumentiert, befasst sich unter
anderem mit Aufbau und Codierung des Steuerkanals PDCCH (Physical Downlink
Control Channel). Druckschrift K11 beschreibt, dass für den PDCCH (Physical
Downlink Control Channel) im LTE-Standard vorgesehen ist, zur Fehlererkennung
einen CRC (cyclic redundancy check) zu verwenden, um die korrekte Übermittlung
zu überwachen („Error detection is provided on PDCCH transmissions through a
Cyclic Redundancy Check (CRC).“; vgl. S. 14, Abs. 5.3.2.x, erster Satz). Weiter
sieht der LTE-Standard gemäß Dokument K11 vor, dass der Cyclic Redundancy
Check mit dem Identifikator der Nutzerkomponente (UE Identity) maskiert wird
(„This sequence of bits is then masked with the UE Identity…“; vgl. S. 14,
Abs. 5.3.2.x, letzter Satz), wobei der Fachmann aus Dokument K4e – wie
vorstehend dargelegt – weiß, dass es sich bei diesem Identifikator um den C-RNTI
der Nutzerkomponente handelt (Merkmal 10.9‘).


Die Beklagte hat darauf hingewiesen, dass sich die zum LTE-Standard
gehörenden      Dokumente    K4e   und     K11    noch   in    einem   unvollständigen
Entwurfsstadium befanden, worauf verschiedene Lücken und Hinweise in den
Dokumenten hindeuten. Nach Überzeugung des Senats hindert dies den
Fachmann dennoch nicht daran, die vorveröffentlichten Dokumente K4e und K11
im   Hinblick    auf   grundlegende      Fragen    wie   die     Kanalcodierung   und
Fehlererkennung bei seinen Überlegungen zur Verbesserung der Kanalzuweisung

                                           - 54 -



von Steuerkanälen eines LTE-Netzwerksystems zu berücksichtigen, insbesondere
da diese die Grundlage für die weitere LTE-Standardisierung bilden.


Die Merkmale des Anspruchs 10 nach Hilfsantrag 2a‘ sind damit dem Fachmann
aus der Kenntnis der Druckschrift K4 und dem durch die Druckschriften K4e und
K11 dokumentierten Fachwissen nahegelegt. Der Gegenstand des Anspruchs 10
gemäß Hilfsantrag 2a‘ beruht daher nicht auf einer erfinderischen Tätigkeit.


6.    Zum Hilfsantrag 3


Die Ansprüche 1, 5, 8 und 11 des Hilfsantrags 3 sind nicht zulässig.


Hilfsantrag 3 basiert auf der erteilten Anspruchsfassung, wobei die eine Nutzerkomponente betreffenden Ansprüche 1 und 8 um die folgenden Merkmale 1.7‘
bzw. 8.7‘ und 1.8‘‘ bzw. 8.8‘‘ am Ende des jeweiligen Anspruchs ergänzt sind:


      1.7’ / 8.7’     wherein the allocation of control channels is reduced in a systematic way by putting limitations on the tree structure through
                      specifications and
      1.8’’ / 8.8’’   wherein the identifier comprises a C-RNTI.


Die eine Netzwerkkomponente betreffenden Ansprüche 5 und 11 sind in gleicher
Weise um die Merkmale 5.7‘ und 11.7‘ bzw. 5.8‘‘ und 11.8‘‘ am Ende des jeweiligen Anspruchs ergänzt:


      5.7’ / 11.7’    wherein the search for control channels is reduced in a
                      systematic way by putting limitations on the tree structure
                      through specifications and
      5.8’’ / 11.8’’ wherein the identifier comprises a C-RNTI.


Die jeweiligen Merkmale 1.8‘‘ bzw. 8.8‘‘ und 5.8‘‘ bzw. 11.8‘‘ (wherein the identifier
comprises a C-RNTI) beziehen sich auf das jeweilige Merkmal 1.2, 5.2, 8.2 bzw.
11.2 (by using an identifier). Die als Beleg der Ursprungsoffenbarung genannte

                                       - 55 -



Textstellen (vgl. EP 1 990 926 A1, Absatz 0037 bzgl. „searching“; bzw. Abs. 0032
bzgl. „allocation“) besagt, dass es sich bei dem Identifikator um bspw. c-RNTI oder
andere, alternative IDs handelt („by using an identifier such as…“). Das mit Hilfsantrag 3 jeweils ergänzte Merkmal 1.8‘‘ bzw. 8.8‘‘ und 5.8‘‘ bzw. 11.8‘‘ der unabhängigen Ansprüche 1, 5, 8 und 11 sieht dagegen vor, dass der Identifikator
c-RNTI umfasst („comprises…“), was bedeutet, dass der Identifikator neben dem
c-RNTI weitere Parameter zur Identifizierung aufweisen kann. Dies ergibt sich jedoch nicht aus den ursprünglich eingereichten Unterlagen und stellt jeweils eine
unzulässige Verallgemeinerung gegenüber der ursprünglichen Offenbarung dar.


Die Merkmale 1.8‘‘, 5.8‘‘, 8.8‘‘ und 11.8‘‘ der Ansprüche 1, 5, 8 und 11 sind der
Ursprungsoffenbarung im beanspruchten Zusammenhang nicht unmittelbar und
eindeutig zu entnehmen. Die Ansprüche 1, 5, 8 und 11 gemäß Hilfsantrag 3 sind
daher nicht zulässig.


7.    Zum Hilfsantrag 4


In der Fassung gemäß Hilfsantrag 4 kann das Streitpatent ebenfalls keinen
Bestand haben. Dem Gegenstand des Anspruchs 11 nach Hilfsantrag 4 steht
ebenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit, nämlich der
mangelnden Neuheit gegenüber K7 (Art. 138 Abs. 1 Buchstabe a) EPÜ, Art. II § 6
Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 54 EPÜ) entgegen.


Anspruch 11 gemäß Hilfsantrag 4 basiert auf der erteilten Anspruchsfassung, wobei der eine Nutzerkomponente („user device“) betreffende Anspruch 11 um die
Merkmale 11.8 und 11.10 am Ende des Anspruchs ergänzt ist:


      11.8   wherein the identifier is a C-RNTI and
      11.10 wherein only a single size of a node at the highest level of the tree
             structure is defined for a given bandwidth in a cell.

                                       - 56 -



Die gegenüber der erteilten Fassung ergänzten Merkmale sind Druckschrift K7
ebenfalls zu entnehmen.


Druckschrift K7 sieht vor, dass die MAC-ID als Identifikator zum Adressieren der
Nutzerkomponente („UE“) verwendet wird. Jeder Steuerkanal wird dabei eindeutig
durch diesen Identifikator identifiziert (vgl. S. 14, Z. 22-25). Steuerkanäle können
damit von der Nutzerkomponente anhand der entsprechenden MAC-ID gefiltert
und damit als der Nutzerkomponente zugeordnet detektiert werden (vgl. S. 14, Z.
26-28). Da die jeweilige MAC-ID aus dem C-RNTI Adressraum stammt, sieht
Druckschrift K7 vor, dass ein C-RNTI direkt an Stelle einer MAC-ID zum Identifizieren einer individuellen Nutzerkomponente – und damit, wie der Fachmann mitliest, für die entsprechenden für die Nutzerkomponente vorgesehenen Steuerkanäle – verwendet werden kann (vgl. S. 15, Z. 3-4 i.V.m. S. 14, Z. 25-26). Somit ist
Druckschrift K7 zu entnehmen, dass es sich bei dem Identifikator ebenfalls um
einen C-RNTI handelt (Merkmal 11.8).


Weiter ist in Druckschrift K7 vorgesehen, dass auf der höchsten Ebene der Baumstruktur nur Knoten einer einzigen Größe verwendet werden, die durch eine vorgegebene Bandbreite in einer Zelle (des LTE-Netzwerksystems) definiert ist. Wie
Druckschrift K7 zu Figur 5 beschreibt, können die Steuerkanäle, die auf der niedrigsten Ebene die größten Code-Blocks bilden, auf der höchsten Ebene – im gezeigten Ausführungsbeispiel der Figur 5 – jeweils aus vier Steuerkanälen der
kleinsten Code-Blocks bestehen (vgl. S. 13, Z. 7-12 und Fig. 5). Das Ausführungsbeispiel nach Figur 5 geht dabei davon aus, dass alle Steuerkanäle auf der
höchsten Ebene der Baumstruktur die gleiche Größe haben. Da die Steuerkanäle
der niedrigsten Ebenen jeweils die gleiche ganzzahlige Anzahl der Code-Blocks
der höchsten Ebene enthalten und die Zahl der Steuerkanäle auf der niedrigsten
Ebene der Baumstruktur durch die Bandbreites des Systems bestimmt ist („The
number of the control channels at the lowest level of the tree is determined by the
system bandwidth and number of OFDM symbols (n) available for the largest code
blocks“; vgl. S. 13, Z. 1-3 und Fig. 5), sind damit zwangsläufig auch die Steuerka-

                                          - 57 -



näle der höchsten Ebene durch die zur Verfügung stehende Bandbreite in der jeweiligen Netzwerk-Zelle bestimmt (Merkmal 11.10).


Für die weiteren, gegenüber der erteilten Fassung unveränderten Merkmale wird
auf die Ausführungen zu Anspruch 11 des Hauptantrags verwiesen, die für den
Hilfsantrag 4 in gleicher Weise gelten.


Der Fachmann entnimmt der Druckschrift K7 somit auch alle Merkmale des Anspruchs 11. Der Gegenstand des Anspruchs 11 gemäß Hilfsantrag 4 ist daher
nicht neu.


8.     Zum Hilfsantrag 5


Die unabhängigen Ansprüche 4 und 10 des Hilfsantrags 5 sind nicht zulässig.


Die auf eine Nutzerkomponente bezogenen Ansprüche 4 und 10 gemäß Hilfsantrag 5 entsprechen den Ansprüchen 4 und 10 gemäß Hilfsantrag 2a.


Wie vorstehend zu Hilfsantrag 2a ausgeführt, ergeben sich die Merkmale 4.8 und
10.8 der Ansprüche 4 und 10 des Hilfsantrags 2a – und somit der Ansprüche 4
und 10 des Hilfsantrags 5 – in Kombination mit Merkmal 4.9 bzw. 10.9 jeweils
nicht aus den ursprünglich eingereichten Unterlagen, da die ursprüngliche Beschreibung in Bezug auf Merkmal 4.9 bzw. 10.9 einen empfängerspezifischen
Identifikator und nicht einen beliebigen Identifikator vorsieht (vgl. EP 1 990 926 A1,
Abs. 0016).


Merkmal 4.8 bzw. 10.8 der Ansprüche 4 bzw. 10 ist daher jeweils in Verbindung
mit Merkmal 4.9 bzw. 10.9 der Ursprungsoffenbarung nicht unmittelbar und
eindeutig zu entnehmen. Die Ansprüche 4 und 10 gemäß Hilfsantrag 5 sind daher
nicht zulässig.

                                           - 58 -



9.     Die weiteren Patentansprüche der Hilfsanträge 1, 2, 2‘, 2a, 2a‘, 3, 4 und 5
bedürfen keiner weiteren, isolierten Prüfung, weil die Beklagte in der mündlichen
Verhandlung zu erkennen gegeben hat, dass sie das Streitpatent nur in der
Reihenfolge des Hauptantrags und der Hilfsanträge in der gemäß der in der
mündlichen Verhandlung dargelegten Reihenfolge jeweils als Ganzes verteidigt
(vgl. BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 –
Datengenerator).




                                IV.     Zum Hilfsantrag 6


Demgegenüber kann die Beklagte das Streitpatent erfolgreich mit der Fassung
nach Hilfsantrag 6 verteidigen, weil diese Fassung zulässig ist und ihr keine
Nichtigkeitsgründe nach Art. II § 6 Abs. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 EPÜ
entgegenstehen.


1.     Geänderte Ansprüche


Bei den Ansprüchen gemäß Hilfsantrag 6 handelt es sich um die auf eine
Netzwerkkomponente           (network    device)    und   ein   Verfahren   in   einer
Netzwerkkomponente gerichteten Ansprüche 1 bis 3 und 7 bis 9 gemäß
Hilfsantrag 2.


Die unabhängigen Ansprüche 1 und 7 unterscheiden sich von den erteilten
Ansprüchen 1 und 8 im Vorrichtungsanspruch 1 in der folgenden Änderung des
Merkmals 1.6


       1.6’      thereby allowing the method further comprising increasing allocation
                 of lower level control channels,


und im Verfahrensanspruch 7 in der folgenden Änderung des Merkmals 8.6

                                          - 59 -



      7.6’   thereby allowing and to increase allocation of lower level control
             channels,


sowie jeweils im Hinzufügen des folgenden Merkmals am Ende der erteilten Ansprüche 1 und 8:


      1.7 / 7.7     wherein the allocation is increased more the lower the level of
                    the tree structure.


Die Unteransprüche 2 und 3 sowie 8 und 9 entsprechen den Ansprüchen 2 und 3
sowie 9 und 10 der erteilten Fassung.


2.    Zur Auslegung


Die Merkmale 1.7 und 7.7 sehen vor, dass das Allokieren bzw. Zuordnen von
Steuerkanälen mehr bzw. weiter erhöht werden soll, je niedriger die Ebene der
Steuerkanäle in der Baumstruktur ist. Der Fachmann versteht die Merkmale 1.7
und 7.7 so, dass bevorzugt Kanäle auf möglichst niedriger Ebene der
Baumstruktur zugeordnet bzw. allokiert werden sollen.


3.    Zur Zulässigkeit


Diese jeweiligen Änderungen bzw. Einschränkungen der Ansprüche 1 und 7
gemäß Hilfsantrag 6 sind zulässig.


Die Merkmale 1.6‘ und 7.6‘ des Anspruchs 1 nach Hilfsantrag 6 basieren auf den
ursprünglichen Ansprüchen 1 und 2 bzw. den ursprünglichen Ansprüchen 10 und
11. Eine Erweiterung des Schutzbereichs, den die Klägerin in den Änderungen
erkennen will, liegt hierbei nicht vor. Denn auch die erteilte Fassung trifft bereits
keine Aussage über die Art der Äste der Baumstruktur, für die auf den niedrigeren
Ebenen eine Allokation erfolgen kann.

                                       - 60 -



Das Merkmal 1.7 des Anspruchs 1 nach Hilfsantrag 6 entspricht dem
ursprünglichen Anspruch 5 (der auf den urspr. Anspruch 2 rückbezogen war, der
wiederum Merkmal 1.6‘ des Anspruchs 1 entspricht). Aufgrund des Bezugs zur
Netzwerkkomponente (network device) kann dies in gleicher Weise auf Anspruch
7 nach Hilfsantrag 6 übertragen werden, der auf ein Verfahren in einer
Netzwerkkomponente gerichtet ist.


Die Unteransprüche 2 und 3 sowie 8 und 9 basieren auf den ursprünglichen
Ansprüchen mit entsprechenden Rückbezügen. Die Unteransprüche nach
Hilfsantrag 6 sind damit ebenfalls zulässig.


4.    Zur Ausführbarkeit


Entgegen der Ansicht der Klägerinnen ist das Streitpatent im Umfang der Ansprüche des Hilfsantrags 6 nicht schon deshalb für nichtig zu erklären, weil ihre Gegenstände nicht so deutlich und vollständig offenbart wären, dass ein Fachmann
sie ausführen kann (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1
Buchst. b) EPÜ).


Das jeweilige inhaltsgleiche Merkmal 1.7 bzw. 7.7 der Ansprüche 1 und 7 nach
Hilfsantrag 6 gibt vor, Zuordnungen von Steuerkanälen verstärkt durchzuführen, je
niedriger die Ebene in der Baumstruktur ist. Das Merkmal enthält – wie die
Klägerin zutreffend ausführt – keine konkrete Vorgabe an den Fachmann, welche
Steuerkanäle zuerst zu vergeben sind. Dennoch verbleibt der Anspruch für den
Fachmann ausführbar, da er diesen nicht vor unüberwindbare Schwierigkeiten
stellt. Denn das Merkmal lässt dem Fachmann gegenüber einer festen Vorgabe
der zu vergebenden Steuerkanäle selbst oder ihrer Ebene in der Baumstruktur, die
Wahlfreiheit, eine Auswahl zwar vorrangig anhand der Ebene durchzuführen, aber
beispielsweise die mit der Ebene verbundene Größe der Code-Blocks weiterhin zu
berücksichtigen indem die Vergabe (kleinerer) Steuerkanäle einer höheren Ebene
nicht grundsätzlich ausgeschlossen wird. Das Fehlen der Nennung einer
Bezugsgröße, gegenüber der ein verstärktes Allokieren erfolgen soll, stellt den

                                        - 61 -



Fachmann zur Auswahl der zuzuordnenden Steuerkanäle damit nicht vor
Hindernisse, die der Ausführbarkeit des jeweiligen Anspruchs entgegenstehen.
Die Ansprüche 1 und 7 sind damit so deutlich und vollständig offenbart, dass ein
Fachmann sie ausführen kann.


5.     Zur Patentfähigkeit


Entgegen der Auffassung der Klägerinnen steht einer beschränkten Verteidigung
der Ansprüche 1 bis 3 und 7 bis 9 in der Fassung nach Hilfsantrag 6 auch nicht
der Nichtigkeitsgrund mangelnder Patentfähigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG
i. V. m. Art. 138 Abs. 1 Buchst. a) i. V. m. Art. 52 ff. EPÜ) entgegen.


a)     Neuheit


Die Gegenstände der unabhängigen Ansprüche 1 und 7 sind neu, da aus keiner
der im Verfahren befindlichen Druckschriften sämtliche Merkmale des Anspruchs
1 bzw. des nebengeordneten Anspruchs 7 gemäß Hilfsantrag 6 bekannt sind.


Druckschrift K4 sieht einer Beschränkung bei der Suche nach Steuerkanälen in
der Nutzerkomponente („UE“) vor („restricting PDCCH monitoring set of a UE“; vgl.
S. 1, Kap. 1). Dabei wird von einer festen Vorgabe ausgegangen, nach der die
Steuerkanäle auf fest vorgegebene Steuerkanalkandidaten festgelegt sind, wobei
diese Festlegung auch als Festlegung für die Netzwerkkomponente („eNB“) zu
verstehen ist („both eNB and UE can figure out which PDCCH is to be used for the
UE“; vgl. S. 2, Kap. 2.3). In diesem Zusammenhang ist zwar unter anderem eine
Begrenzung der Zuordnung der kleinsten Code-Blocks, also der Steuerkanäle auf
der höchsten Ebene der Baumstruktur vorgesehen (vgl. Merkmal 1.5 bzw. 7.5).
Solche festen Vorgaben der Steuerkanalkandidaten werden nach Druckschrift K4
für die Nutzerkomponente jedoch auch für einzelne oder alle weiteren Ebenen der
Baumstruktur gemacht (vgl. S. 1, Kap. 2.1), so dass das Allokieren von
Steuerkanälen nicht zwangsläufig mehr bzw. weiter erhöht werden kann, je
niedriger die Ebene der Steuerkanäle in der Baumstruktur ist, sondern von diesen

                                      - 62 -



Vorgaben abhängig ist (vgl. Merkmal 1.7 bzw. 7.7). Zudem lässt sich eine
konkrete Strategie zum Zuordnen bzw. Allokieren auf der Netzwerkseite nicht aus
den Vorgaben zum nutzerseitigen Durchsuchen der Baumstruktur ableiten, da
bezüglich einer entsprechenden Signalisierung nur pauschal auf die Festlegung
der Steuerkanalkandidaten für eine bestimmte          Nutzerkomponente     Bezug
genommen wird („higher layer signaling“; vgl. S. 1, Kap. 2.1). Damit sind die
Ansprüche 1 und 7 neu gegenüber Druckschrift K4.


Aufgrund ihres Zeitrangs ist Druckschrift K5 nur für die Neuheitsprüfung relevant.
Ein verstärktes Allokieren von Steuerkanälen, je niedriger die Ebene der
Steuerkanäle in der Baumstruktur ist Druckschrift K5 nicht zu entnehmen, da diese
auch auf den niedrigeren Ebenen eine beschränkte, vorgegebene Auswahl an
Steuerkanal-Kandidaten vorsieht (vgl. Fig. 5A, „PDCCH candidates“ 6 und 7 des
„Monitoring Set“; vgl. Merkmal 10.7 bzw. 4.7). Mit der Vorgehensweise, wie eine
solche beschränkte Auswahl netzwerkseitig festgelegt wird, befasst sich
Druckschrift K5 nicht. Damit sind die Ansprüche 1 und 7 neu gegenüber
Druckschrift K5.


Ob Dokument K6 dem vorliegend relevanten Stand der Technik zuzurechnen ist,
insbesondere ob die Priorität in Druckschrift K6 nicht wirksam in Anspruch
genommen ist (wofür die fehlende Nennung eines der Anmelder in Dokument K9
spricht), kann dahinstehen, da Druckschrift K6 jedenfalls nicht entnommen werden
kann, dass das Zuordnen bzw. Allokieren von Steuerkanälen mehr bzw. weiter
erhöht werden soll, je niedriger die Ebene der Steuerkanäle in der Baumstruktur
ist (vgl. Fig. 2 und 3 mit Beschreibung). Druckschrift K6 zeigt in Figur 3 das
Beispiel einer Baumstruktur, bei der auf der höchsten Ebene nur ein Steuerkanal
belegt ist. Hierzu wird der Nutzerkomponente die Zuordnungsinformation (d. h.
Informationen, welche der Steuerkanäle allokiert sind) für die höchste Ebene
signalisiert. Dies stellt zwar eine Begrenzung der Suche nach Steuerkanälen auf
der höchsten Ebene dar (vgl. Merkmal 1.5 bzw. 7.5), jedoch setzt Druckschrift K6
eine explizite Signalisierung der verwendeten Kanäle (vgl. S. 10, Z. 19-29) bzw.
eine aus der Beschränkung auf der höchsten Ebene der Baumstruktur

                                        - 63 -



abzuleitende Beschränkung auf den weiteren Ebenen voraus (vgl. S. 10, Z. 31 bis
S. 11, Z. 9). Eine Angabe zur Vorgehensweise für eine Auswahl der netzwerkseitig
zu allokierenden Steuerkanäle, insbesondere in Bezug auf die niedrigeren Ebenen
der Baumstruktur, ist weder aus dem Begrenzen der nutzerseitigen Suche
abzuleiten noch Druckschrift K6 sonst zu entnehmen.


Gemäß Druckschrift K7 wird das Allokieren und das Suchen nach Steuerkanälen
in einer Baumstruktur beschränkt, indem der Baum auf allen Ebenen
„beschnitten“ wird („The tree may be pruned so that all the nodes are not possible
to be allocated in all the levels of the tree.“, vgl. S. 19, Z. 21-23). Der Begriff des
Beschneidens („pruning“) weist damit nicht auf eine auf die Ebenen der
Baumstruktur bezogene Beschränkung, sondern auf ein Ausblenden ganzer
Zweige der Baumstruktur hin. Zwar zeigen die in Druckschrift K7 beschriebenen
Beispielen in den Figuren 5 und 6, dass jeweils auch eine Beschränkung auf der
höchsten Ebene der jeweiligen Baumstruktur entsprechend dem Merkmal 1.5 bzw.
7.5 erfolgt. Druckschrift K7 ist aber über das „Beschneiden“ („pruning“), das sich
über mehrere Ebenen erstreckt, keine konkrete Vorgehensweise in Bezug auf ein
Allokieren von Steuerkanälen zu entnehmen; insbesondere gibt es keinen Hinweis
darauf, dass die Zuordnung von Steuerkanälen verstärkt erfolgen soll, je niedriger
die Ebene der Steuerkanäle in der Baumstruktur ist. Damit sind die jeweiligen
Gegenstände Ansprüche 1 und 7 auch neu gegenüber Druckschrift K7.


Druckschrift K8 nennt als mögliches Beispiel für eine Beschränkung des
Suchens von Steuerkanälen das Überwachen bzw. Verfolgen („follow“) von
ausschließlich vier der größten Steuerkanäle („There could e.g. be four (as in
HSDPA) largest PDCCHs each UE will follow instead of all of them“; vgl. Abschnitt
7, Punkt 3), zweiter Abs., zweiter Satz). Dies bedeutet dass keiner der kleinsten
Steuerkanäle, die gemäß Streitpatent auf der höchsten Ebene angeordnet sind,
durchsucht wird. Eine entsprechende netzwerkseitige Vorgehensweise zum
Allokieren erscheint zwar sinnvoll, ist aber nicht gefordert. Selbst wenn eine solche
netzwerkseitige Umsetzung mitgelesen werden kann, folgt aus der festen Vorgabe
von bestimmten zu überwachenden Steuerkanälen keine Angabe dazu, nach

                                       - 64 -



welcher Vorgehensweise netzwerkseitig Steuerkanalkandidaten für die Zuordnung
ausgewählt werden. Die feste Vorgabe bestimmter Steuerkanäle (einzeln oder
pauschal auf eine Ebene bezogen (vgl. a.a.O.) gibt zudem keinen Hinweis darauf,
dass ein Allokieren verstärkt erfolgen, je niedriger die Ebene der Steuerkanäle in
der Baumstruktur ist. Damit sind die jeweiligen Gegenstände der Ansprüche 1 und
7 auch neu gegenüber Druckschrift K8


Die Dokumente K4e, K11 und K12 dienen dem Beleg des Fachwissens und
betreffen keine Strategie zum verbesserten netzwerkseitigen Allokieren von
Steuerkanälen. Insbesondere sind ihnen weder Hinweise auf ein Beschränken von
Steuerkanalkandidaten zu entnehmen, noch darauf, welche Steuerkanäle im Falle
einer solchen Beschränkung bevorzugt zuzuordnen bzw. zu allokieren sind.


b)    Erfinderische Tätigkeit


Die Gegenstände der unabhängigen Ansprüche 1 und 7 beruhen auch auf einer
erfinderischen Tätigkeit, da die Merkmale des Anspruchs 1 bzw. des nebengeordneten Anspruchs 7 gemäß Hilfsantrag 6 dem Fachmann weder einzeln noch in
Zusammenschau der im Verfahren befindlichen Druckschriften und seinem Fachwissen nahegelegt sind.


Die Druckschriften K5 bis K7 sind – ungeachtet der Frage nach einer wirksamen
Inanspruchnahme von Prioritäten – allenfalls als nachveröffentlichter Stand der
Technik für die Neuheitsprüfung relevant.


Die Druckschriften K4 und K8 gehen jeweils von einer festen Vorgabe einzelner
Steuerkanäle selbst oder von der Vorgabe einer bestimmten Ebene einer
Baumstruktur für die Steuerkanalkandidaten aus, die allokiert werden sollen. Diese
Vorgabe wird beispielsweise mit der Größe der jeweiligen Code-Blocks auf dieser
Ebene begründet. Einen Hinweis darauf, die Zuordnung auf der höchsten Ebene
der Baumstruktur, d. h. auf der Ebene der kleinsten Code-Blocks als
Steuerkanalkandidaten zu begrenzen und mehr Steuerkanäle zuzuordnen, je

                                      - 65 -



niedriger die Ebene der Steuerkanäle in der Baumstruktur ist, findet sich im Stand
der Technik nicht.


Auch unter Berücksichtigung des Fachwissens, wie es unter anderem durch die
Druckschriften K4e, K11 und K12 belegt ist, gelangt der Fachmann nicht in
naheliegender Weise zu den jeweiligen Gegenständen der unabhängigen
Ansprüche 1 und 7.


Die Netzwerkkomponente (network device) gemäß Anspruch 1 und das Verfahren
gemäß Anspruch 7 nach Hilfsantrag 6 sind damit dem Fachmann weder durch
einzelne der vorgenannten Druckschriften noch in deren Zusammenschau oder
unter Einbeziehung seines Fachwissens nahegelegt. Die Gegenstände der
Ansprüche 1 und 7 des Hilfsantrags 6 sind somit neu und beruhen auf einer
erfinderischen Tätigkeit.


c)    Die auf die unabhängigen Patentansprüche 1 und 7 rückbezogenen
Ansprüche 2 und 3 sowie 8 und 9 in der Fassung des Hilfsantrags 6 erfüllen
ebenfalls die an sie zu stellenden Anforderungen hinsichtlich Zulässigkeit und
Schutzfähigkeit.




                            B.   Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1
PatG i. V. m. § 709 ZPO.

                                      - 66 -



                         C.     Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument nach Maßgabe der Verordnung über den elektronischen Rechtsverkehr
beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) vom 24.
August 2007 (BGBl. I S. 2130) in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist
beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur versehen sein, die von einer internationalen Organisation auf
dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich zur
Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung
enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils
vorgelegt werden.




Friehe      Dr. Schwengelbeck      Jacobi          Altvater           Dr. Flaschke


                                                                               prö
