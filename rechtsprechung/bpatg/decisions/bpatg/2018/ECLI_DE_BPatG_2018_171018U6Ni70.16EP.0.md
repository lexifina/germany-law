---
ecli: "ECLI:DE:BPatG:2018:171018U6Ni70.16EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 70/16"
decided: "2018-10-17"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=43&nr=34383&anz=825&pos=653&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2018-10-17_6_Ni_70_16_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 70/16 vom 2018-10-17

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                       Verkündet am
                                                      17. Oktober 2018
6 Ni 70/16 (EP)                                              …

(Aktenzeichen)


                     In der Patentnichtigkeitssache

 …




 ECLI:DE:BPatG:2018:171018U6Ni70.16EP.0

                                         -2-



                 betreffend das europäische Patent EP 1 119 997
                                  (DE 699 24 130)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 17. Oktober 2018 durch die Vorsitzende Richterin Friehe sowie
die    Richter     Schwarz,      Dipl.-Phys. Dr. Schwengelbeck,       die    Richterin
Dipl.-Phys. Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater


für Recht erkannt:


  I.   Das europäische Patent 1 119 997 wird mit Wirkung für das Hoheitsgebiet
       der Bundesrepublik Deutschland teilweise für nichtig erklärt, soweit es über
       folgende Fassung hinausgeht:


          1.     A method of allocating a temporary identity (TLLI) in a cellular network to a mobile station (MS) by a first network element (SGSN,
                 BSC, RNC) which has an identifier (NEI) of its own, characterized
                 in that the temporary identity (TLLI) comprises at least part of an
                 identifier (NEI) indicating the first network element and that said
                 temporary identity (TLLI) also comprises a paging identity which is
                 unique to each mobile station (MS) in the paging area in question,
                 and further characterized by using only part of said temporary
                 identity (TLLI) in connection with paging.


          2.     A method according to claim 1, characterized in that the cellular
                 network comprises a plurality of paging areas.


          3.     A method according to claim 1 or 2, characterized in that the
                 identifier (NEI) of the first network element together with an identifier (RAI) of the paging area where said temporary identity (TLLI)
                 was allocated uniquely identifies the first network element.

                               -3-



4.   A method according to any one of the claims 2 to 3, characterized
     in that
                   each paging area has an associated master network
     element for allocating a paging identity to each of several mobile
     stations in the paging area; and
                   the first network element, before allocating the temporary identity (TLLI) to a paging area, requests a paging identity for
     the mobile station from said master network element in the paging
     area in question.


5.   A method according to any one of the claims 2 to 4, characterized
     in that each paging area is connected to a plurality of network elements, and that the cellular network uses said temporary identity
     (TLLI) for routing uplink traffic to the network element currently
     serving the mobile station (MS).


6.   A method according to any one of the preceding claims, characterized in that after a change to a new paging area by the mobile station (MS), a network element to which the mobile station is registered uses said temporary identity (TLLI) and the identifier of the
     new paging area for deriving an identifier of a network element
     which served the mobile station before said change.


7.   A method according to any one of claims 3 to 6, characterized in
     that only said paging identity is used at first for paging the mobile
     station, and that the entire temporary identity (TLLI) is used for
     signalling.


8.   A network element adapted to allocate a temporary identity (TLLI)
     to a mobile station (MS), characterized in that said temporary
     identity (TLLI) comprises at least a part of an identifier (NEI) indicating said network element and that said temporary identity

                             -4-



     (TLLI) also comprises a paging identity which is unique to each
     mobile station (MS) in the paging area in question, and further
     characterized by said network element being adapted to use only
     part of said temporary identity (TLLI) in connection with paging.


9.   A network element according to claim 8, characterized by being
     adapted to use said temporary identity (TLLI) and the identifier of
     the paging area where the mobile station (MS) is located to derive
     an identifier of another network element which served the mobile
     station prior to the current network element.


10. A cellular network comprising a mobile station (MS) and a first network element adapted to allocate a temporary identity (TLLI) to the
     mobile station, characterized in that the first network element is a
     network element according to any one of claims 8 and 9.


11. A cellular network according to claim 10, characterized by a database element, which is adapted to:
     - receive an inquiry comprising said at least part of the identifier of
     the network element that allocates the temporary identity (TLLI)
     and information relating to the location where the temporary identity (TLLI) was allocated, such as a paging area identifier; and to
     - unambiguously determine, on the basis of said inquiry, an address of the network element which allocated the temporary identity (TLLI).


12. A cellular network according to claim 11, characterized in that the
     database element (DNS) is also adapted to send an inquiry to another network element currently storing a context for the mobile
     station (MS) in question.

                                -5-



13. A mobile station (MS) for a cellular network, being adapted to use
      a temporary identity (TLLI) allocated by a network element, characterized in that said temporary identity (TLLI) comprises at least a
      part of the identifier of the network element (SGSN) that has allocated the temporary identity (TLLI) and that said temporary identity
      (TLLI) also comprises a paging identity which is unique to each
      mobile station (MS) in the paging area in question, and further
      characterized by said mobile station (MS) being adapted to use
      only part of said temporary identity (TLLI) in connection with paging.


14.   A mobile station (MS) according to claim 13, characterized by being adapted to use the temporary identity (TLLI) in connection with
      at least one of the following procedures:
      - cell update,
      - routing area update,
      - location area update,
      - paging area update, and
      - paging response.


15.   A mobile station (MS) according to claim 13 or 14, characterized
      by being adapted to:
      use a part of the identifier of the network element (SGSN) that
      allocates the temporary identity (TLLI) for data transfer; and to
      use the identifier in full for signalling.


16.   A radio station controller for a cellular network, adapted to route
      data packets comprising a temporary identity (TLLI) allocated to a
      mobile station (MS), characterized in that
             the temporary identity (TLLI) comprises at least part of an
      identifier (NEI) indicating a first network element which allocated
      the temporary identity (TLLI); and that said temporary identity

                                         -6-



               (TLLI) also comprises a paging identity which is unique to each
               mobile station (MS) in the paging area in question, and
                   the radio station controller is adapted to use said at least part
               of the identifier for routing data packets to said first network element currently serving the mobile station, wherein said radio station is adapted to use only part of said temporary identity (TLLI) in
               connection with paging.


          17. A radio station controller according to claim 16, characterized by
               comprising, for each of several mobile stations, a context for temporarily storing an identifier of the network element currently serving the mobile station.


II. Die weitergehende Klage wird abgewiesen.


III. Die Kosten des Rechtsstreits trägt die Klägerin zu 1/3 und die Beklagte zu
   2/3.


IV. Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 % des zu
   vollstreckenden Betrages vorläufig vollstreckbar.

                                         -7-



                                    Tatbestand


Die Beklagte ist seit 1. Oktober 2012 eingetragene Inhaberin des europäischen
Patents 1 119 997 (Streitpatent). Die ursprünglich von der Fa. N…
…OY, H… (F…), die zum 1. Dezember 1999 in N…
OY umfirmiert worden war, am 5. Oktober 1999 unter Inanspruchnahme der Priorität aus der finnischen Anmeldung FI 982 166 vom 6. Oktober 1998 eingereichte
internationale Anmeldung PCT/FI1999/00825 wurde als WO 00/21319 am
13. April 2000 veröffentlicht. Das Streitpatent wurde in der Verfahrenssprache
Englisch am 9. März 2005 veröffentlicht.


Das Streitpatent trägt die Bezeichnung


     „IDENTIFYING A MOBILE STATION IN A PACKET RADIO NETWORK“


(in Deutsch laut Streitpatentschrift: „IDENTIFlZIERUNG EINER MOBILSTATION
IN EINEM PAKETFUNKNETZ“)


und umfasst in der erteilten Fassung 19 Patentansprüche, die mit der am
10. November 2016 erhobenen Nichtigkeitsklage in vollem Umfang angegriffen
werden.


Die angegriffenen erteilten unabhängigen Patentansprüche 1, 9, 15 und 18 lauteten wie folgt:


       1. A method of allocating a temporary identity (TLLI) in a cellular network
           to a mobile station (MS) by a first network element (SGSN, BSC, RNC)
           which has an identifier of its own, characterized in that the temporary
           identity (TLLI) comprises at least part of an identifier (NEI) indicating the
           first network element.

                                        -8-



      9. A network element adapted to allocate a temporary identity (TLLI) to a
          mobile station (MS), characterized in that said temporary identity
          comprises at least a part of an identifier (NEI) indicating said network
          element.


      15. A mobile station (MS) for a cellular network, being adapted to use a
          temporary identity (TLLI) allocated by a network element, characterized in that said temporary identity comprises at least a part of the
          identifier of the network element (SGSN) that has allocated the temporary identity.


      18. A radio station controller for a cellular network, adapted to route data
          packets comprising a temporary identity allocated to a mobile station
          (MS), characterized in that
             the temporary identity comprises at least part of an identifier (NEI)
          indicating a first network element which allocated the temporary identity;
          and
              the radio station controller is adapted to use said at least part of the
          identifier for routing datapackets to said first network element currently
          serving the mobile station.


In deutscher Übersetzung laut Streitpatentschrift lauten sie:


      1. Verfahren zum Zuweisen einer vorübergehenden Identität (TLLI) in einem zellularen Netzwerk an eine Mobilstation (MS) durch ein erstes
          Netzwerkelement (SGSN, BSC, RNC), welches einen eigenen Identifikator aufweist, dadurch gekennzeichnet, dass die vorübergehende
          Identität (TLLI) mindestens einen Teil eines Identifikators (NEI) aufweist, der das erste Netzwerkelement anzeigt.


      9. Netzwerkelement, angepasst eine vorübergehende Identität (TLLI) an
          eine Mobilstation zuzuweisen, dadurch gekennzeichnet, dass die vo-

                                          -9-



            rübergehende Identität mindestens einen Teil eines Identifikators (NEI)
            umfasst, der das Netzwerkelement anzeigt.


       15. Mobilstation (MS) für ein zellulares Netzwerk, die ausgelegt ist, eine vorübergehende Identität (TLLI), die einem Netzwerk zugewiesen wurde,
            zu verwenden, dadurch gekennzeichnet, dass die vorübergehende
            Identität mindestens einen Teil des Identifikators des Netzwerkelements
            (SGSN) umfasst, der die vorübergehende Identität zugewiesen hat.


       18. Funkstations-Steuerung für ein zellulares Netzwerk, die angepasst ist,
            Datenpakete zu routen, umfassend eine vorübergehende Identität, die
            einer Mobilstation (MS) zugewiesen wurde, dadurch gekennzeichnet,
            dass die vorübergehende Identität mindestens einen Teil eines Identifikators (NEI) umfasst, der ein erstes Netzwerkelement anzeigt, welches
            die vorübergehende Identität zuwies; und die Funkstations-Steuerung
            angepasst ist, um mindestens einen Teil des Identifikators zum Routen
            von Datenpaketen zu dem ersten Netzwerkelement, das gegenwärtig
            die Mobilstation bedient, zu verwenden.


Bei den übrigen ebenfalls angegriffenen Patentansprüchen handelt es sich um
jeweils   auf     einen   oder      mehrere   der   vorgenannten   nebengeordneten
Patentansprüche unmittelbar oder mittelbar rückbezogene Ansprüche.


Die Klägerin ist der Ansicht, dass das Streitpatent wegen unzulässiger Erweiterung der erteilten Ansprüche 3 und 11, mangelnder Ausführbarkeit der Gegenstände der Ansprüche 1, 5, 13 bis 15 und 17 sowie wegen fehlender Patentfähigkeit für nichtig zu erklären ist.


Dies stützt sie auf die Druckschriften (Nummerierung und Kurzzeichen nach Klageschriftsatz):

                               - 10 -



NK1     EP 0 920 761 A2, angemeldet am 24. Juni 1998 mit Priorität vom
        24. Juni 1997, veröffentlicht als WO 98/59468 A2 am 30. Dezember 1998


NK1-a   Registerauszug zu NK1


NK2     EP 1 116 396 A0, angemeldet am 20. September 1999 mit Priorität
        vom 21. September 1998, veröffentlicht als WO 00/18155 A2 am
        30. März 2000


NK2-0   Prioritätsschrift FI 982027 zur NK2


NK2-a   Registerauszug zu NK2


NK3     EP 0 859 531 A2, veröffentlicht am 19. August 1998


NK4     WO 98/48528 A1, angemeldet am 24. April 1998 mit Priorität vom
        24. April 1997, veröffentlicht am 29. Oktober 1998


NK4a    Registerauszug zu EP 0 978 958 (Familienmitglied der NK4)
        englische Übersetzung der ursprünglich in japanischer Sprache
        veröffentlichten WO 98/48528 A1


NK5     Network Working Group; C. Perkins, Editor, Request for Comments: 2002 (rfc2002); IBM; Category: Standard Tracks; Oktober
        1996


NK6     WO 97/33403 A1, veröffentlicht am 12. September 1997


NK7     WO 98/32304 A2, veröffentlicht am 23. Juli 1998


NK8     US 5 729 537, veröffentlicht am 17. März 1998

                                        - 11 -




     NK9        ETSI GSM 03.60 v2.0.0; Digital cellular telecommunications system (Phase 2+); General Packet Radio Service (GPRS); Service
                description; Stage 2; Mai 1997


     NK10       ETSI GSM 03.03 v6.1.0; TS 100 927; Digital cellular telecommunications system (Phase 2+); Numbering, addressing and identification; Juli 1998


     NK11       ETSI GSM 03.60 version 6.1.1 Release 1997; Draft EN 301 344;
                Digital cellular telecommunications system (Phase 2+); General
                Packet Radio Service (GPRS); Service description; Stage 2; August 1998


     NK12       ETSI GSM 01.04 version 5.0.1; ETSI Technical Report 350; Digital
                cellular telecommunications system (Phase 2+); Abbreviations and
                acronyms; Dezember 1996




Die Klägerin beantragt,




        das   europäische     Patent   1 119 997   mit   Wirkung   für   das
        Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu
        erklären.


Die Beklagte, welche das Streitpatent nur noch beschränkt verteidigt, beantragt,


        die Klage abzuweisen, soweit das Patent mit dem nunmehrigen
        Hauptantrag und den jetzigen Hilfsanträgen vom 9. Juli 2018 verteidigt wird.

                                        - 12 -



Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den Gegenstand des Streitpatents in wenigstens in einer der verteidigten Fassungen für
schutzfähig. Zur Begriffsdefinition verweist sie auf die im Streitpatent aufgeführten
Druckschriften


     B1          ETSI GSM 03.60 v6.0.0 (1998-03); Digital cellular telecommunications system (Phase 2+); General Packet Radio Service (GPRS);
                 Service description; Stage 2,


     B2          ETSI GSM 03.03 v6.0.0 (1998-04); Digital cellular telecommunications system (Phase 2+); Numbering, addressing and identification.




Die unabhängigen nebengeordneten Ansprüche nach Hauptantrag lauten wie
folgt (Änderungen gegenüber der erteilten Fassung unterstrichen):


      1. A method of allocating a temporary identity (TLLI) in a cellular network
          to a mobile station (MS) by a first networkelement (SGSN, BSC, RNC)
          which has an identifier of its own, characterized in that the temporary
          identity (TLLI) comprises at least part of an identifier (NEI) indicating the
          first network element, wherein the temporary identity (TLLI) is used by
          the mobile station (MS) in connection with a paging response procedure.


      8. A network element adapted to allocate a temporary identity (TLLI) to a
          mobile station (MS), characterized in that said temporary identity (TLLI)
          comprises at least a part of an identifier (NEI) indicating said network
          element wherein the temporary identity (TLLI) is used in connection with
          a paging response procedure.

                                        - 13 -



      13. A mobile station (MS) for a cellular network, being adapted to use a
          temporary identity (TLLI) allocated by a network element, in connection
          with a paging response procedure, characterized in that said temporary
          identity (TLLI) comprises at least a part of the identifier of the network
          element (SGSN) that has allocated the temporary identity (TLLI).


      16. A radio station controller for a cellular network, adapted to route data
          packets comprising a temporary identity (TLLI) allocated to a mobile
          station (MS), characterized in that
             the temporary identity (TLLI) comprises at least part of an identifier
          (NEI) indicating a first network element which allocated the temporary
          identity (TLLI); and
              the radio station controller is adapted to use said at least part of the
          identifier for routing data packets to said first networkelement currently
          serving the mobile station in connection with a paging response procedure.


Wegen des Wortlauts der Ansprüche nach Hilfsantrag I wird auf den Urteilstenor,
wegen des Wortlauts der abhängigen Ansprüche nach Hauptantrag sowie der Ansprüche nach Hilfsantrag II wird auf die Akte Bezug genommen.


Der Senat hat den Parteien einen qualifizierten Hinweis vom 6. April 2018 zukommen lassen.




                          Entscheidungsgründe


                                          A.
Die Klage ist zulässig, hat aber nur teilweise Erfolg. In der erteilten Fassung ist
das Streitpatent ohne Sachprüfung für nichtig zu erklären, nachdem diese Fassung von der Beklagten nicht mehr verteidigt wird. Aber auch in der Fassung nach
dem (neuen) Hauptantrag ist das Streitpatent nach Art. II § 6 Abs. 1 Nr. 1

                                      - 14 -



IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52 bis 57 EPÜ für nichtig zu erklären, weil dieser Fassung der Nichtigkeitsgrund mangelnder Patentfähigkeit entgegensteht. Demgegenüber ist die Klage abzuweisen, soweit sie sich auch gegen
die Fassung des Streitpatents nach Hilfsantrag I richtet, denn einer solchen Fassung des Streitpatents stehen keine Nichtigkeitsgründe entgegen. Auf die weitere
Frage, ob das Streitpatent auch in der Fassung nach Hilfsantrag II Bestand hätte,
kam es bei dieser Sachlage nicht mehr an.


                     I. Zum Gegenstand des Streitpatents


1.    Das Patent betrifft gemäß der Beschreibungseinleitung des Streitpatents
„Paketfunk-Netzwerke“ (packet radio networks) und insbesondere eine Mobilitätsunterstützung in solchen Netzwerken (vgl. Abs. 0001 der Streitpatentschrift (SP)
bzw. deutsche Übersetzung der europäischen Patentschrift des Streitpatents
DE 699 24 130 T2, Abs. 0001). Dies wird anhand der Implementierung eines allgemeinen paketorientierten Funkdiensts GPRS (General Packet Radio Service) in
einem GSM Mobilfunksystem näher erläutert (vgl. SP, Abs. 0002 ff). Unter einem
paketorientierten Dienst ist ein Dienst zu verstehen, bei dem Daten bei einem
Sender in einzelne Pakete umgewandelt und beim Empfänger wieder zusammengesetzt werden.


Ein allgemeiner Paketfunkdienst GPRS (General Packet Radio Service) ist gemäß
Beschreibungseinleitung der Patentschrift ein Dienst in dem GSM-System und
eines der Ziele der Standardisierungsarbeiten der GSM-Phase 2+ beim ETSI (Europäisches Telekommunikationsstandard-Institut). Die GPRS-betriebsfähige Umgebung umfasse einen oder mehrere Sub-Netzwerk-Dienstbereiche, welche untereinander durch ein GPRS-Basisnetzwerk (GPRS backbone network) verbunden
seien. Ein Sub-Netzwerk umfasse eine Zahl von Paketdaten-Dienstknoten (SN),
welche in der Patentschrift als bedienende GPRS-Unterstützungsknoten (SGSN)
bezeichnet werden, wobei jeder dieser mit dem GSM-Mobilkommunikations-Netzwerk (typischerweise mit Basisstationssystemen) derart verbunden sein soll, dass
es einen Paketdienst für mobile Datenendgeräte mittels mehrerer Basisstationen

                                      - 15 -



(d. h. Zellen) bereitstellen könne. Das dazwischen liegende Mobilkommunikations-Netzwerk liefere paketvermittelte Datenübertragung zwischen einem Unterstützungsknoten und mobilen Datenendgeräten. Unterschiedliche Sub-Netzwerke
seien ihrerseits mit einem externen Datennetzwerk, beispielsweise mit einem öffentlichen Vermittlungs-Datennetzwerk (PSPDN) mittels GPRS-Gateway-Unterstützungsknoten (GGSN) verbunden. Der GPRS-Dienst erlaube somit eine Paketdatenübertragung zwischen mobilen Datenendgeräten und externen Datennetzwerken, wenn das GSM-Netzwerk als ein Zugangsnetzwerk funktioniere (vgl.
Abs. 0002 der Streitpatentschrift).


2.    Als Problem wird in der Streitpatentschrift aufgeführt, dass in dem Fall,
wenn die Mobilstation ihren Funkrufbereich (paging area) wechselt, das neue Unterstützungsnetzwerk-Element Schwierigkeiten beim Bestimmen des alten Unterstützungs-Netzwerkelements auf der Basis des Funkrufbereichs-ldentifikators haben könne. Es gäbe auch ein Risiko von zwei Unterstützungsnetzwerk-Elementen,
welche die gleiche temporäre Identität (TLLI) an zwei unterschiedliche Mobilstationen zuweisen (vgl. SP, Abs. 0037). Im Streitpatent wird dazu als Aufgabe genannt, die Probleme und Nachteile zu verringern, welche sich aus dem herkömmlichen Verfahren zum Zuweisen einer temporären Identität ergeben (vgl. SP,
Abs. 0038).


3.    Die Aufgabe soll u. a. dadurch gelöst werden, dass im Zusammenhang mit
einem Verfahren zum Zuweisen einer temporären Identität, einem Netzwerkelement, einer Mobilstation sowie einer Funkstationssteuerung jeweils ein Netzwerkelement, welches eine temporäre / vorübergehende Identität (TLLI) an eine Mobilstation (MS) zuweist, seinen eigenen Identifikator oder zumindest einen Teil davon
in die temporäre Identität (TLLI) kodiert (vgl. SP, Abs. 0039 und 0040 bzw. deutsche Übersetzung, Abs. 0028 und 0029). Dementsprechend beansprucht das
Streitpatent in der beschränkten Fassung nach Hauptantrag ein Verfahren, ein
Netzwerkelement, eine Mobilstation und eine Funkstations-Steuerung für ein zellulares Netzwerk jeweils mit den Merkmalen nach den neuen unabhängigen An-

                                         - 16 -



sprüchen 1, 8, 13 und 16, die auf den erteilten Ansprüchen 1, 9, 15 und 18 beruhen.


       II. Zur beschränkten Verteidigung nach dem neuen Hauptantrag


In der Fassung des neuen Hauptantrags kann die Beklagte ihr Patent nicht erfolgreich verteidigen, weil dieser Fassung zumindest der Nichtigkeitsgrund der fehlenden Patentfähigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1
Buchst. a), Art. 52 bis 57 EPÜ) entgegensteht.


1.     Der unabhängige nebengeordnete Anspruch 13 nach Hauptantrag lässt
sich in der Verfahrenssprache, die der beschränkten Verteidigung zugrunde liegt,
wie folgt gliedern:


       Anspruch 13
       13.1           A mobile station (MS) for a cellular network, being adapted to
                      use a temporary identity (TLLI) allocated by a network element, in connection with a paging response procedure,
                      characterized in that
       13.2           said temporary identity (TLLI) comprises at least a part of the
                      identifier of the network element (SGSN) that has allocated the
                      temporary identity (TLLI).


2.     Der zuständige Fachmann, ein Ingenieur der Elektrotechnik, der über eine
mehrjährige Erfahrung auf dem Gebiet des Mobilfunks im Zusammenhang mit der
Datenübertragung in GSM-Mobilnetzen verfügt, versteht das Streitpatent und die
in den vorgenannten beschränkt verteidigten Ansprüchen nach neuem Hauptantrag verwendeten Begriffe wie folgt:


Die jeweiligen unabhängigen Patentansprüche nach Hauptantrag betreffen ein
Verfahren, ein Netzwerkelement (network element), eine Mobilstation (mobile station / MS) und eine Funkstations-Steuerung (radio station controller), wobei in ei-

                                      - 17 -



nem solchen Netzwerk eine vorübergehende Identität (TLLI / Temporary Logical
Link Identity) an die Mobilstation (MS) zugewiesen wird (vgl. SP, Abs. 0014). Die
Zuweisung soll durch ein Netzwerkelement (Unterstützungsknotenpunkt SGSN,
Basisstationssteuerung BSC, Funknetzwerksteuerung RNC) geschehen, welches
einen eigenen Identifikator aufweist, wobei die vorübergehende Identität (TLLI)
mindestens einen Teil eines Identifikators (Netzwerkelement-ldentifikator NEI)
aufweist, der dieses Netzwerkelement anzeigt (vgl. SP, Fig. 1A). Dabei geht das
Streitpatent davon aus, dass der Identifikator (NEI) (bzw. ein Teil davon) einigen
Bits innerhalb einer herkömmlichen vorübergehenden Identität (TLLI) zugewiesen
wird, bspw. ohne dabei die Länge des TLLI zu verändern (vgl. SP, Abs. 0040). Der
auf eine Mobilstation (mobile station) gerichtete Anspruch 13 des Hauptantrags
setzt in diesem Zusammenhang keine „extended temporary identity“ voraus, wie
sie das Streitpatent in einem weiteren Ausführungsbeispiel beschreibt (vgl. SP,
Abs. 0057 ff).


Unter einer Mobilstation (MS) ist dabei ein Mobilfunk-Endgerät – beispielsweise
ein Mobiltelefon – zu verstehen (vgl. SP, Figur 1A), wobei ein zellulares Netzwerk
ein Mobilfunknetzwerk mit überlappenden Raumbereichen bzw. Zellen darstellt,
die jeweils so mit Funkwellen versorgt werden, dass bei einer Bewegung einer
Mobilstation über eine Zelle hinweg eine unterbrechungsfreie Übertragung möglich
ist.


Unter der vorstehend genannten temporären / vorübergehenden Identität (TLLI)
versteht der Fachmann eine Übermittlungsadresse zum Adressieren der Mobilstation für die Kommunikation zwischen der Mobilstation und einem Netzwerkelement. Das Zuweisen der vorübergehenden Identität (TLLI) erfolgt beim Aufbau
einer logischen Verbindung zwischen dem zuständigen Netzwerkelement (bspw.
SGSN im GSM-Netz) und der Mobilstation (MS), d. h. beim erstmaligen Anmelden
der Mobilstation bzw. beim Wechsel in den Zuständigkeitsbereich eines anderen
Netzwerkelements (routing area update; vgl. SP, Fig. 3 und Abs. 0024 bis 0034).

                                        - 18 -




Die Formulierung „being adapted to use a temporary identity (TLLI)” im Oberbegriff
des Anspruchs 13 gemäß Hauptantrag (vgl. Merkmal 13.1) ist so zu verstehen,
dass sie sich auf die Mobilstation (mobile station) bezieht. Allerdings ist die Art und
Weise, wie die Mobilstation ausgelegt ist, eine vorübergehende Identität zu verwenden, durch den Anspruchswortlaut nicht weiter beschränkt. Die Bezugnahme
auf den Identifikator des Netzwerkelements als „identifier of the network element
(SGSN) that has allocated the temporary identity" im kennzeichnenden Teil des
Anspruchs 13 gemäß Hauptantrag (vgl. Merkmal 13.2) ist so auszulegen, dass der
Begriff „network element“ respektive „Netzwerkelement“ insgesamt auf all diejenigen netzwerkseitig aktiven Funktionseinheiten gerichtet ist, welche einer Mobilstation eine vorübergehende Identität zuweisen können. Die inhaltliche Bedeutung
des Identifizierers des Netzwerkelements (identifier of the network element), der
gemäß Anspruch 13 in der vom Netzwerkelement vergebenen vorübergehenden
Identität (TLLI) enthalten sein soll, stellt dabei keine Einschränkung hinsichtlich der
im Oberbegriff des Anspruchs aufgeführten Eignung zur Verwendung der vorübergehenden Identität (adapted to use a temporary identity) durch die beanspruchte
Mobilstation (MS) dar. Anspruch 13 des Hauptantrags fordert dabei nicht, dass die
Mobilstation die vorübergehende Identität inhaltlich auswertet und dabei den ent-

                                      - 19 -



haltenen Teil des Identifzierers des Netzwerkelements gezielt verwendet (vgl. SP,
Abs. 0040, 0041, 0046, 0047 und 0051 i. V. m. Fig. 2, 3 und Abs. 0024-0034). So
wird beispielsweise bei dem im Streitpatent gezeigten Routingbereichs-Aktualisierungsverfahren (routing area update procedure) die am Ende einer Zuweisungsprozedur (attach procedure) von einem Netzwerkelement (SGSN) empfangene
vorübergehende Identität (TLLI) durch die Mobilstation unverändert an ein anderes
Netzwerkelement (SGSN) weitergegeben (vgl. SP, Fig. 2 und 3 sowie Abs. 0043,
0046 und 0047 i. V. m. Abs. 0033, 0034). Eine inhaltliche Auswertung der vorübergehenden Identität (TLLI) mitsamt dem genannten Identifizierer des Netzwerkelments, um zu bestimmen, von welchem Netzwerkelement die verwendete
vorübergehende Identität an die Mobilstation vergeben wurde, findet nur im jeweiligen Netzwerkelement statt (vgl. SP, u. a. Abs. 0041: The TLLI according to the
invention is used e.g. by a BSC […]. It is also used by any network element […]).


Mangels weiterer Angaben in Anspruch 13 nach Hauptantrag gilt dies in gleicher
Weise für das „Paging“. Unter dem Begriff „Paging“ ist eine in der deutschen
Übersetzung des Streitpatents als Funkruf bzw. Funkrufdienst bezeichnete Kommunikation zwischen einem Netzelement und der Mobilstation zu verstehen, bei
der die Mobilstation beispielsweise über einen eingehenden Anruf informiert wird,
wobei ein Funkruf mit einer Funkruf-Antwort (paging response) beantwortet wird.
Dabei soll die Mobilstation gemäß Anspruch 13 des Hauptantrags in Verbindung
mit dem Paging geeignet sein, eine vorübergehende Identität (TLLI) zu verwenden
(„adapted to use…“), die einen Identifizierer eines Netzwerkelements enthält. Die
anspruchsgemäße vorübergehende Identität (TLLI) unterscheidet sich auch hierbei von einer herkömmlichen vorübergehenden Identität nur in der zugewiesenen
Bedeutung einiger enthaltener Bits für das Identifizieren eines Netzwerkelements
(vgl. SP, Abs. 0040 i. V. m. Abs. 0036); eine möglicherweise auch im Umfang oder
der Bedeutung für die Mobilstation veränderte „erweiterte vorübergehende Identität“ („extended temporary identity“) entsprechend eines weiteren Ausführungsbeispiels des Streitpatents (vgl. Abs. 0057) ist in Anspruch 13 des Hauptantrags nicht
gefordert. Wie die Klägerin in diesem Zusammenhang zu Recht ausgeführt hat,
sind für die Mobilstation eine herkömmliche vorübergehende Identität wie auch

                                        - 20 -



eine vorübergehende Identität, die gemäß Streitpatent zumindest Teile des Identifizierers eines Netzwerkelements aufweisen, nichts anderes als Bitstrings, die im
Rahmen des Paging – bei der Anfrage des Netzwerkelements wie auch im Rahmen einer Funkruf-Antwort (paging response procedure) – als Ganzes dem eindeutigen Adressieren bzw. Identifizieren der Mobilstation dienen. In der Mobilstation selbst genügt hierbei ein Vergleich mit der ihr zugewiesenen vorübergehenden Identität, um zu erkennen, ob sie angesprochen (d. h. adressiert) wurde, ohne
dass dabei dem enthaltenen Identifizierer des Netzwerkelements eine Bedeutung
zukommt und dieser ausgewertet werden muss.


3.     Es kann dahingestellt bleiben, ob der von der Klägerin geltend gemachte
Nichtigkeitsgrund der fehlenden Neuheit besteht, denn jedenfalls erweist sich das
Streitpatent auch mit den Änderungen nach dem neuen Hauptantrag nicht als patentfähig, da der Gegenstand des auf eine Mobilstation gerichteten nebengeordneten Anspruchs 13 gegenüber dem Stand der Technik gemäß Druckschrift NK9
nicht auf einer erfinderischen Tätigkeit beruht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG
i. V. m. Art. 138 Abs. 1 Nr. 1, Art. 52, 56 EPÜ).


Aus dem im Jahr 1997 zweifellos vorveröffentlichten Stand der Technik gemäß
NK9, einem Standard-Dokument zum General Packet Radio Service (GPRS), ist
eine Mobilstation (mobile station / MS) für ein zellulares Telekommunikations-System (Digital cellular telecommunication system) mit einem entsprechenden
zellularen Netzwerk bekannt, das einzelne Unterstützungsknotenpunkte (SGSN /
Serving GPRS Support Nodes) als Netzwerkelemente aufweist (vgl. bspw. Abschnitt 3.2 Abbreviations, S. 11). Durch eines dieser Netzwerkelemente (SGSN /
Serving GPRS Support Nodes) wird der Mobilstation beispielsweise bei der Anmeldung für GPRS-Dienste eine vorübergehende Identität (TLLI / Temporary Logical Link Identity) zugewiesen (vgl. Abschnitt 6.5 Attach Function auf S. 31 bis 34,
insbesondere erster Absatz auf S. 31 und Punkte 3, 4 und 8 auf S. 33). Diese
dient der Adressierung der Mobilstation (vgl. Abschnitt 12.1.1, S. 59).

                                       - 21 -



Die vorübergehende Identität (TLLI) wird von der Mobilstation und den Netzwerkelementen (SGSN / Serving GPRS Support Nodes) in Verbindung mit einem
Funkruf- bzw. Paging-Verfahren für einen sogenannten Downlink-Transfer (Paging
for GPRS Downlink Transfer) verwendet, wobei das Funkruf- bzw. Paging-Verfahren sowohl eine Paging-Anfrage (paging request) als auch eine Paging-Antwort
(paging response message) und damit eine Funkruf-Antwort-Prozedur entsprechend dem Oberbegriff des Anspruchs 13 beinhaltet (vgl. Figur 25 und Abschnitt
8.4, S. 48 bis S. 49, insbes. zw. Abs. le. Satz: The SGSN shall then consider the
LLC frame to be an implicit paging response message […] / Merkmal 13.1).




Da die aus dem Stand der Technik gemäß NK9 bekannte Mobilstation (MS) im
Rahmen des Paging eine vorübergehende Identität (TLLI) von einem Netzwerkelement (SGSN) in der Funkruf-Anfrage (paging request) empfängt und die vorübergehende Identität (TLLI) dann unverändert als Teil der Antwort (paging
response) in einem LLC Frame als eigene Adresse zurückgegeben wird (vgl. Abschnitt 8.4, S. 48, insbes. Punkte 2 bis 4; i. V. m. Abschnitt 12.1.1, S. 59 und LLC
Header: Fig. 36, S. 61), ist eine solche Mobilstation für den Fachmann offensichtlich auch bereits eingerichtet, eine vorübergehende Identität (TLLI) zu verwenden,
wie es in der Beschreibung des Streitpatents im Zusammenhang mit einer Funkruf- bzw. Paging-Antwort aufgeführt ist (vgl. SP, Abs. 0040, 0046 und 0047 sowie
die vorstehende Auslegung unter Ziffer 2). Der Fachmann geht dabei aufgrund
seines Fachwissens davon aus, dass die aus NK9 bekannte vorübergehende
Identität bzw. TLLI von der Mobilstation (MS) nur als die Adresse verwendet wird,
ohne dass Teilen der vorübergehenden Identität für die Mobilstation eine darüber

                                       - 22 -



hinausgehende Bedeutung zukommt, die deren inhaltliche Auswertung erfordert.
Denn auch beim Paging gemäß Anspruch 13 ist von einer vorübergehenden Identität (TLLI) auszugehen, die sich von einer herkömmlichen vorübergehenden Identität nur in der zugewiesenen Bedeutung einiger enthaltener Bits für die Netzwerkelemente unterscheidet, aber in unveränderter Weise als Adresse der Mobilstation
dient (vgl. SP, Abs. 0040 i. V. m. Abs. 0036). Eine möglicherweise auch in der Bedeutung für die Mobilstation veränderte „erweiterte vorübergehende Identität“
(„extended temporary identity“) entsprechend eines weiteren Ausführungsbeispiels
des Streitpatents (vgl. Abs. 0057) ist in Anspruch 13 des Hauptantrags nicht gefordert.


Die Mobilstation gemäß Anspruch 13 nach Hauptantrag ergibt sich damit für den
Fachmann in naheliegender Weise aus der Kenntnis des Stands der Technik gemäß Dokument NK9 unter Zuhilfenahme seines Fachwissens, ohne dabei erfinderisch werden zu müssen.


4.     Die weiteren Patentansprüche des Hauptantrags bedürfen keiner weiteren,
isolierten Prüfung, weil die Beklagte sowohl schriftsätzlich als auch in der mündlichen Verhandlung zu erkennen gegeben hat, dass sie den Hauptantrag als geschlossenen Anspruchssatz versteht und das Streitpatent nur in der Reihenfolge
des Hauptantrags und der Hilfsanträge jeweils als Ganzes verteidigt (vgl. BGH –
Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator).


       III. Zur beschränkten Verteidigung nach Hilfsantrag I


Demgegenüber kann die Beklagte ihr Patent aber mit der Fassung nach Hilfsantrag I beschränkt verteidigen, weil dieser Fassung des Streitpatents keine Nichtigkeitsgründe entgegen stehen.


1.     Die unabhängigen Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I lassen sich
in der Verfahrenssprache, die der beschränkten Verteidigung zugrunde liegt, wie

                                       - 23 -



folgt gliedern (Änderungen gegenüber der erteilten Fassung der entsprechenden
Ansprüche unterstrichen):


      Anspruch 1:
      1.1           A method of allocating a temporary identity (TLLI) in a cellular
                    network to a mobile station (MS) by a first network element
                    (SGSN, BSC, RNC) which has an identifier (NEI) of its own,
                    characterized in that
      1.2           the temporary identity (TLLI) comprises at least part of an
                    identifier (NEI) indicating the first network element
      1.3           and that said temporary identity (TLLI) also comprises a paging identity which is unique to each mobile station (MS) in the
                    paging area in question, and further characterized by using
                    only part of said temporary identity (TLLI) in connection with
                    paging.


      Anspruch 8
      8.1           „A network element adapted to allocate a temporary identity
                    (TLLI) to a mobile station (MS),
                    characterized in that
      8.2           said temporary identity (TLLI) comprises at least a part of an
                    identifier (NEI) indicating said network element
      8.3           and that said temporary identity (TLLI) also comprises a paging identity which is unique to each mobile station (MS) in the
                    paging area in question, and further characterized by said
                    network element being adapted to use only part of said temporary identity (TLLI) in connection with paging.


      Anspruch 13
      13.1          A mobile station (MS) for a cellular network, being adapted to
                    use a temporary identity (TLLI) allocated by a network element,

                                       - 24 -



                    characterized in that
      13.2          said temporary identity (TLLI) comprises at least a part of the
                    identifier of the network element (SGSN) that has allocated the
                    temporary identity (TLLI)
      13.3          and that said temporary identity (TLLI) also comprises a paging identity which is unique to each mobile station (MS) in the
                    paging area in question, and further characterized by said mobile station (MS) being adapted to use only part of said temporary identity (TLLI) in connection with paging.


      Anspruch 16
      16.1          A radio station controller for a cellular network, adapted to
                    route data packets comprising a temporary identity (TLLI) allocated to a mobile station (MS),
                    characterized in that
      16.2          the temporary identity (TLLI) comprises at least part of an
                    identifier (NEI) indicating a first network element which allocated the temporary identity (TLLI); and that said temporary
                    identity (TLLI) also comprises a paging identity which is unique
                    to each mobile station (MS) in the paging area in question,
                    and
      16.3          the radio station controller is adapted to use said at least part
                    of the identifier for routing data packets to said first network
                    element currently serving the mobile station, wherein said radio station is adapted to use only part of said temporary identity (TLLI) in connection with paging.


2.    In den unabhängigen Ansprüchen nach Hilfsantrag I kommt gegenüber dem
Streitpatent in der erteilten Fassung zusätzlich zum Ausdruck, dass die vorübergehende Identität eine Funkruf-Identität (paging identity) umfasst, die für jede Mobilstation eindeutig innerhalb des jeweiligen Funkruf-Bereichs (in the paging area
in question) ist und dabei sowohl das Netzwerkelement (network element) des

                                        - 25 -



Mobilfunk-Netzwerks (vgl. Merkmale 1.3, 8.3 sowie 16.2 und 16.3) als auch die
Mobilstation (vgl. Merkmal 13.3) so angepasst sind, dass alleinig bzw. nur ein Teil
der vorübergehenden Identität (TLLI) in Verbindung mit einem Funkruf (paging)
verwendet wird (to use only part of said temporary identity), wobei im Anspruch 13
zum Ausdruck kommt, dass der zuvor genannte Teil der vorübergehenden Identität auch von der Mobilstation benutzt wird. Durch die vorstehend genannte Verwendung der so erweiterten vorübergehenden Identität TLLI und einer für jede
Mobilstation eindeutigen Funkruf-Identität (paging identity) innerhalb eines Funkruf-Bereichs (paging area) soll gemäß Streitpatentschrift bei einem Funkruf an
eine Mobilstation, die noch nicht in einem Funkrufbereich registriert ist, ein Kollisionsrisiko verringert werden (vgl. SP, Abs. 0058, insbes. Sp. 12, Z. 5-10 u. Z. 12-
15, i. V. m. Abs. 0055).


3.     Die Beschränkung der unabhängigen Ansprüche 1, 8, 13 und 16 gegenüber
der erteilten Fassung ist zulässig. Die Merkmale der Ansprüche 1 bzw. 8, 13 und
16 nach Hilfsantrag I basieren auf den nebengeordneten Ansprüchen 1, 8, 10 und
15 im Zusammenhang mit den Ansprüchen 2 und 10 sowie der Beschreibung der
ursprünglichen Anmeldung (vgl. Offenlegungsschrift WO 00/21319 A1, S. 13,
Z. 18, bis S. 14, Z. 11). Im Streitpatent finden sich die Merkmale in den Ansprüchen 1, 8, 15 und 18 im Zusammenhang mit der Beschreibung (vgl. SP, Abs. 0058
i. V. m. Abs. 0055). Bezüglich der Merkmale der von den Ansprüchen 1, 8, 13 und
16 abhängigen Ansprüche 2 bis 7, 9 bis 12, 14, 15 und 17 ist keine unzulässige
Erweiterung geltend gemacht worden und auch nicht ersichtlich. Dies gilt in gleicher Weise für die zum Hilfsantrag I zugehörige Fassung der Beschreibung und
Figuren.


4.     Der von der Klägerin vertretenen Auffassung bezüglich einer mangelnden
Ausführbarkeit und Klarheit der jeweiligen Anspruchsgegenstände ist nicht zuzustimmen. Für den Fall, dass die vorübergehende Identität lediglich einen Teil des
Identifikators des Netzwerkelements umfasse, sei gemäß den Ausführungen der
Klägerin nicht hinreichend deutlich und vollständig offenbart bzw. nicht hinreichend
klar, wie ein eindeutiger und vollständiger Identifikator des Netzwerkelements ge-

                                      - 26 -



bildet werden könne. Die Klägerin hat diesbezüglich ausgeführt, dass zwar drei
Bits gemäß Beschreibung des Streitpatents ausreichten, um acht Unterstützungsknotenpunkte bzw. SGSN, die einer „Routing area 1" zugeordnet sind, innerhalb
dieser „Routing area 1" eindeutig zu unterscheiden – jedoch ein SGSN in einer
„Routing area 2“, der diese drei Bits in der „vorübergehenden Identität“ lese, wenn
sich eine Mobilstation, ausgehend von der „Routing area 1“ in die „Routing area 2"
bewege, keinerlei Rückschluss darauf ziehen könne, ob die Mobilstation aus
„Routing area 1“ oder einer beliebigen anderen „Routing area“ komme, der beispielsweise auch acht SGSN (codiert über drei Bits) zugeordnet seien. Diese Annahme der Klägerin (mit drei Bits) steht jedoch nicht generell einer Ausführbarkeit
(mit mehr Bits) entgegen, wobei die Codierung in den unabhängigen Ansprüchen
nicht auf drei Bits beschränkt ist, sondern die Wahl einer geeigneten Codierung
dem Fachmann überlassen bleibt. Insofern ist vorliegend die Ausführbarkeit für
den Fachmann grundsätzlich gegeben, selbst wenn sich unter dem Anspruchswortlaut auch ein einzelnes Beispiel konstruieren ließe, bei dem die Funktion fraglich sein könnte (vgl. u. a. BGH, Urteil vom 13. Juli 2010 – Xa ZR 126/07, GRUR
2010, 916, Leitsatz – Klammernahtgerät).


5.    In der beschränkten Fassung nach Hilfsantrag I sind die jeweiligen Gegenstände der unabhängigen Ansprüche 1, 8, 13 und 16 neu und beruhen auf einer
erfinderischen Tätigkeit.


a)    Neuheit


aa)   NK9


Aus dem Stand der Technik gemäß NK9 ist entsprechend den vorstehenden
Ausführungen zu einer Mobilstation gemäß Anspruch 13 nach Hauptantrag unter
Ziffer II. 3. ein Verfahren zum Zuweisen einer vorübergehenden Identität (TLLI /
Temporary Logical Link Identity) an eine Mobilstation bekannt. Die Identität (TLLI)
wird in einem zellularen Netzwerk zugewiesen, das Netzwerkelemente in Form
von Unterstützungsknotenpunkten (SGSN / Serving GPRS Support Node) und

                                      - 27 -



mehrere Zellen aufweist (vgl. Ausführungen zum Hauptantrag). Der Fachmann
liest dabei im Hinblick auf Merkmal 1.1 bzw. die Merkmale 8.1, 13.1 und 16.1 mit,
dass ein Netzwerkelement zu seiner Identifizierung einen eigenen Identifikator
aufweist. Aufgrund seines Fachwissens geht der Fachmann dabei auch davon
aus, dass die temporäre Identität (TLLI) entsprechend Merkmal 1.3 bzw. entsprechend den Merkmalen 8.3, 13.3 und 16.3 im Rahmen des Funkrufs (paging) als
Adresse der Mobilstation verwendet wird (vgl. Fig. 25 und S. 48, drittletzter Abs.:
TLLI is the identifier by which the MS is paged). Des Weiteren ist dem Stand der
Technik gemäß NK9 zu entnehmen, dass eine Mobilstation im Rahmen einer
Funkruf- bzw. Paging-Antwort eine vorübergehende Identität (TLLI) im Zusammenhang mit einer logischen Verbindungssteuerung (LLC) über die Basisstation
(BSS) an ein Netzwerkelement (SGSN) sendet (vgl. S. 48 und Fig. 25 mitsamt
zugeh. Text). Dass bei dem Verfahren jedoch eine Funkruf-Identität in einem definierten Funkruf-Bereich (paging area) verwendet wird, die eindeutig für eine Mobilstation ist und dabei – insbesondere auch durch die Mobilstation nach Anspruch 13 – alleinig ein Teil einer vorübergehenden Identität im Netzwerk im Zusammenhang mit einem Funkruf- bzw. Paging-Verfahren verwendet wird, wie es in
Merkmal 1.3 des Anspruchs 1 bzw. den Merkmalen 8.3, 13.3 und 16.3 der Ansprüche 8, 13 und 16 nach Hilfsantrag I aufgeführt ist, ist dem Stand der Technik
gemäß NK9 nicht zu entnehmen.


Den Ausführungen der Klägerin bezüglich der im Anspruch 13 aufgeführten Mobilstation und Merkmal 13.3, dass der Schluss gezogen werden könne, dass bereits
eine in der NK9 beschriebene Mobilstation eingerichtet sei, einen erfindungsgemäßen TLLI im Zusammenhang mit einer „Attach“- oder „Routing Area Update“-
Prozedur gemäß dem im Streitpatent in den Absätzen [0046] und [0047] beschriebenen Verfahren zu verwenden, kann nicht zugestimmt werden. Vielmehr kann
der Fachmann dem Stand der Technik gemäß NK9 auch unter Zuhilfenahme seines Fachwissens keinen Hinweis darauf entnehmen, dass eine Mobilstation in
Verbindung mit einer für die Mobilstation eindeutigen Paging-Identität so angepasst ist, dass die Mobilstation alleinig bzw. nur einen Teil einer vorübergehenden
Identität (TLLI) im Zusammenhang mit einem Funkruf/Paging – also auch in der

                                        - 28 -



Funkruf-Antwort – verwendet, wie es in Anspruch 13 nach Hilfsantrag I in dem Zusatz „to use only part of said temporary identity“ im Merkmal 13.3 enthalten ist.
Dies gilt in gleicher Weise in Bezug auf die Verwendung nur eines Teils einer vorübergehenden Identität bei einem Verfahren zur Zuweisung einer Identität gemäß
Merkmal 1.3 des Anspruch 1 nach Hilfsantrag I bzw. einer Verwendung nur eines
Teils einer solchen Identität durch ein Netzwerkelement bzw. eine Funkstation
gemäß den Merkmalen 8.3 und 16.3 der Ansprüche 8 und 16 nach Hilfsantrag I.


Die Gegenstände der nebengeordneten Ansprüche 1, 8, 13 und 16 sind damit neu
gegenüber dem Stand der Technik gemäß NK9.


bb)    NK1


Druckschrift NK1, die vor dem Prioritätstag des Streitpatents angemeldet, aber
erst danach veröffentlicht wurde, beschreibt im Hinblick auf die jeweiligen Merkmale 1.1, 8.1, 13.1 und 16.1 sowie die Merkmale 1.2, 8.2 und 13.2 der Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I ein Verfahren zum Zuweisen einer temporären / vorübergehenden Identität (TLLI Temporary Logical Link Identity) an eine
Mobilstation (mobile station MS) in Form eines Mobilfunk-Endgerätes bzw. Mobiltelefons (vgl. S. 3 zweiter Abs. i. V. m. S. 2 vorletzter und letzter Abs. sowie Fig. 4
und 6 bis 8). Die vorübergehende Identität (TLLI) wird in einem zellularen Netzwerk zugewiesen, welches Unterstützungsknotenpunkte (SGSN) als Netzwerkelemente und mehrere Zellen (several cells) aufweist (vgl. a. a. O.). Dabei wird
auch darauf hingewiesen, dass die genannten vorübergehenden Identitäten (TLLI)
ebenfalls einen Identifikator enthalten, um das Netzwerkelement (SGSN / Serving
GPRS Support Node) zu identifizieren, das die vorübergehende Identität (TLLI)
vergeben hat (vgl. S. 13 Z. 26-28 und S. 14 Z. 5-7).


Es kann NK1 jedoch nicht entnommen werden, dass bei dem aus Druckschrift
NK1 bekannten Verfahren bzw. zellularen Netzwerk bzw. Mobilstation eine Funkruf-Identität (paging identity) verwendet wird, die eindeutig für eine Mobilstation in
einem bestimmten Funkruf-Gebiet (paging area) ist und wobei nur ein Teil der vo-

                                       - 29 -



rübergehenden Identität (TLLI) im Netzwerk in Verbindung mit einem Funkrufbzw. Paging-Verfahren verwendet wird, wie es in den Merkmalen 1.3, 8.3, 13.3
bzw. 16.2 und 16.3 der Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I aufgeführt
wird.


cc)     NK2


Druckschrift NK2, die vor dem Anmeldetag des Streitpatents angemeldet, aber
erst danach veröffentlicht wurde, beschreibt in Bezug auf die jeweiligen Merkmale
1.1, 8.1, 13.1 und 16.1 sowie die Merkmale 1.2, 8.2 und 13.2 der Ansprüche 1, 8,
13 und 16 nach Hilfsantrag I eine Routing-Einheit (foreign agent) eines (ersten)
Netzwerkelements in Form eines GPRS-Unterstützungsknotens (SGSN, GGSN) in
einem zellularen Netzwerk (GPRS, UMTS; vgl. S. 1, erster Satz und S. 4, letzter
Abs.), wobei die Routing-Einheit einer Mobilstation anbietet, die Adresse der Routing-Einheit (foreign agent) als eine temporäre COA-Adresse (COA / care of
address) zu verwenden. Diese temporäre Adresse (COA / care of address) ist als
eine Art Endpunkt eines Tunnels zu der Mobilstation für Daten bzw. Datenpakete
(datagrams) zu verstehen, die an Mobilstationen weitergeleitet werden, während
diese sich nicht in einem Heimnetzwerk (Home Network) aufhalten. Auf diese
Weise kann der Verbrauch zusätzlicher IP-Adressen vermieden werden (vgl. S. 1
le. Abs. und S. 2 Z. 4-12 und S. 4, Z. 28, bis S. 5, Z. 2 und S. 6, Z. 24-25). Damit
kann die genannte COA-Adresse eines Netzwerkelements (SGSN, GGSN) auch
als eine zugewiesene vorübergehende Identität in einem zellularen Mobilfunknetz
angesehen werden, wobei die COA-Adresse auch einen eigenen Identifikator des
Netzwerkelements darstellt.


Dass ein Verfahren bzw. ein zellulares Netzwerk bzw. eine Mobilstation eine Funkruf-Identität (paging identity) verwendet, die eindeutig für eine Mobilstation in einem bestimmten Funkruf-Gebiet (paging area) ist, wobei nur ein Teil einer vorübergehenden Identität im Netzwerk im Zusammenhang mit einem Funkruf- bzw.
Paging-Verfahren verwendet wird, wie es in den Merkmalen 1.3, 8.3, 13.3 bzw.

                                         - 30 -



16.2 und 16.3 der Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I gefordert ist, kann
Druckschrift NK2 jedoch nicht entnommen werden.


dd)    NK3


Die vorveröffentlichte Druckschrift NK3 beschreibt im Hinblick auf die nebengeordneten Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I und die zugehörigen
Merkmale 1.1, 8.1, 13.1 und 16.1 sowie 1.2, 8.2 und 13.2 ein Verfahren zum Zuweisen einer temporären / vorübergehenden Identität (TLLI / temporary logical link
identifier bzw. ILSI / international link set-up identity) an eine Mobilstation (mobile
station), wobei ein Netzwerkelement (SGSN) einen zugehörigen Identifikator des
Netzwerks (PLNM / public land mobile network) aufweist (vgl. Sp. 1, Z. 5-10). Dabei liest der Fachmann mit, dass eine neue vorübergehende Identität (TLLI bzw.
ILSI / international link set-up identity) gebildet werden kann, die eine zusätzliche
Information beinhaltet, die eine Ermittlung des alten Netzwerkelements (SGSN)
ermöglicht. Dementsprechend weist die vorübergehende Identität (TLLI bzw. ILSI /
international link set-up identity) auch mindestens einen Teil eines Identifikators
des vorstehend genannten Netzwerks (PLNM / publik land mobile network) auf,
welcher das vorstehend genannte Netzwerkelement (SGNS) anzeigt (vgl. Sp. 2,
Z. 54, bis Sp. 3, Z. 6).


Wie die Beklagte jedoch zu Recht ausgeführt hat, wird in Druckschrift NK3 weder
ein Paging-Verfahren thematisiert noch die Verwendung eines Identifizierers im
Zusammenhang mit einer Paging-Antwort. Im Stand der Technik gemäß NK3 wird
davon ausgegangen, dass ein Netzwerkelement (SGSN) innerhalb eines Routing-Bereichs (RA) bereits eindeutig bestimmbar ist. Ein globaler Identifizierer wird dabei mit einem Ländercode und einem Heimnetzidentifizierer versehen, wobei das
Netzwerkelement weiterhin über die alte Angabe zum Routing-Bereich (RA) identifiziert wird (vgl. Zitatstellen a. a. O., Sp. 2, Z. 54, bis Sp. 3, Z. 6). Dass bei dem
aus Druckschrift NK3 bekannten Verfahren bzw. zellularen Netzwerk bzw. einer
Mobilstation oder einer Funkstations-Steuerung eine Funkruf-Identität (paging
identity) verwendet wird, wobei nur ein Teil einer vorübergehenden Identität, wel-

                                       - 31 -



che eine Funkruf-Identität und zumindest einen Teil des Identifizierers eines Netzwerk-Elements umfasst, im Netzwerk in Verbindung mit einem Paging-Verfahren
verwendet wird, wie es in den jeweiligen Merkmalen 1.3, 8.3, 13.3 bzw. 16.2 und
16.3 der Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I aufgeführt wird, liest der
Fachmann entgegen der von der Klägerin vertretenen Auffassung weder mit, noch
entnimmt der Fachmann Druckschrift NK3 einen entsprechenden Hinweis.


ee)   NK4


In der vorveröffentlichten Druckschrift NK4 wird ein Verfahren zum Zuweisen einer
vorübergehenden / temporären Identität (TMUI / temporary mobile user identity)
beschrieben, die einer Mobilstation (mobile station MS) in einem zellularen Mobilfunknetzwerk mit Netzwerkelementen (u. a. M-SCP) zugewiesen wird (vgl. Fig. 1
und Fig. 133 sowie Abs. 0181 und 0182 i. V. m. Abs. 1138 des von der Klägerin
als NK4-0 beigefügten europäischen Familienmitglieds EP 0 978 958 A1 in englischer Sprache). Die vorübergehende / temporäre Identität (TMUI / temporary mobile user identity) weist gemäß Figur 133 und dem zugehörigen Text in den vorstehend genannten Absätzen 1138 und 1139 einen Identifikator in Form einer
Identifikationsnummer für einen Vermittlungspunkt (M-SCP / mobile service control
point) auf, der auch ein Netzwerkelement darstellt. Dass jedoch bei dem aus
Druckschrift NK4 bekannten Verfahren bzw. zellularen Netzwerk oder einer Mobilstation bzw. Funkstations-Steuerung eine Funkruf-Identität (paging identity) verwendet wird, die eindeutig für eine Mobilstation in einem bestimmten Funkruf-Gebiet (paging area) ist und dabei alleinig ein Teil einer vorübergehenden Identität im
Netzwerk in Verbindung mit einem Paging-Verfahren verwendet wird, wie es in
den jeweiligen Merkmalen 1.3, 8.3, 13.3 bzw. 16.2 und 16.3 der nebengeordneten
Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I aufgeführt wird, ist nicht aus NK4
ersichtlich bzw. von der Klägerin vorgebracht worden.

                                      - 32 -



ff)   NK5, NK6, NK7 und NK8


Die vorveröffentlichte Druckschrift NK5 behandelt eine „care-of address“ für einen
Knotenpunkt (mobile node) in einem Mobilfunknetzwerk im Zusammenhang mit
Datagrammen, die an die Mobilstation weitergeleitet werden, während diese sich
nicht in einem Heimnetzwerk (home network) aufhält (vgl. S. 4 letzter Abs.). Darüber hinaus ist NK5 bezüglich der jeweiligen Gegenstände der nebengeordneten
Ansprüche nach Hilfsantrag I nicht weiter relevant und seitens der Klägerin auch
nichts vorgebracht worden. Zu den Druckschriften NK6 und NK7, die neben dem
Stand der Technik gemäß NK3, NK4 und NK5 im Einspruchsverfahren vor dem
Europäischen Patentamt berücksichtigt worden sind, sowie zu NK8 hat die Klägerin nicht weiter ausgeführt. Im Übrigen gehen diese Druckschriften in Bezug auf
die Neuheit der jeweiligen Anspruchsgegenstände gemäß Hilfsantrag I auch nicht
über die vorstehend abgehandelten Druckschriften gemäß NK1 bis NK4 hinaus.


gg)   NK10


Dem vorveröffentlichten ETSI-GSM-Standard gemäß NK10 ist nicht zu entnehmen, dass eine vorübergehende Identität (TLLI / Temporary Logical Link Identity)
einen Teil eines Identifikators aufweist, der ein Netzwerkelement (SGSN) anzeigt,
wie es in den zugehörigen Merkmalen 1.1, 8.1, 13.1 und 16.1 sowie 1.2, 8.2 und
13.2 der nebengeordneten Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I gefordert
ist. Auch dass eine Funkruf-Identität verwendet wird, die eindeutig für eine Mobilstation in einem bestimmten Funkruf-Gebiet (paging area) ist und dabei nur ein
Teil einer vorübergehenden Identität im Netzwerk in Verbindung mit einem Paging-Verfahren verwendet wird, wie es in den jeweiligen Merkmalen 1.3, 8.3, 13.3
bzw. 16.2 und 16.3 der nebengeordneten Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I gefordert ist, ist dem Stand der Technik gemäß NK10 nicht zu entnehmen
und seitens der Klägerin im Übrigen auch nicht vorgebracht worden.

                                       - 33 -



hh)   NK11 und NK12


Druckschrift NK11, welche die Klägerin nur in Bezug auf den erteilten Unteranspruch 17 des Streitpatents angeführt hat (vgl. Abschnitte 9.2.2.1 und 13.1, Tabelle 4 le. Zeile, sowie Abschnitt 14.9), ist im Hinblick auf die Gegenstände der
nebengeordneten Ansprüchen des Hilfsantrags I nicht weiter relevant. Dies gilt in
gleicher Weise für Druckschrift NK12, die seitens der Klägerin lediglich bezüglich
eines PLMN-Netzwerks (PLNM / public land mobile network), wie es in Druckschrift NK3 genannt wird, sowie einer diesbezüglichen Begriffsklärung genannt
worden ist.


b)    Erfinderische Tätigkeit


Wie vorstehend zur Neuheit der Gegenstände der jeweiligen nebengeordneten
Ansprüche 1, 8, 13 und 16 gemäß Hilfsantrag I ausgeführt, sind den im Verfahren
befindlichen Druckschriften die inhaltsgleichen Merkmale 1.3, 8.3, 13.3 sowie 16.2
im Zusammenhang mit Merkmal 16.3 nicht zu entnehmen. Diesbezüglich geben
auch weder der vorveröffentlichte Stand der Technik gemäß Druckschrift NK9 und
Druckschrift NK3 noch die weiteren im Verfahren befindlichen Druckschriften NK1,
NK2, NK4 bis NK8 und NK10 bis NK12 einen Hinweis auf die Benutzung einer für
eine Mobilstation eindeutigen Funkruf-Identität (paging identity) in einem bestimmten Funkruf-Gebiet (paging area) und auf die Verwendung nur eines Teils
einer vorübergehenden Identität von einem Netzwerkelement, einer Mobilstation
oder einer Funkstations-Steuerung in Verbindung mit einem Paging-Verfahren.
Auch eine Zusammenschau des Standes der Technik gemäß NK3 und NK9 oder
eine Kombination der Lehren der übrigen im Verfahren befindlichen Druckschriften
führt damit nicht in naheliegender Weise zu den Gegenständen der nebengeordneten Ansprüche 1, 8, 13 und 16 gemäß Hilfsantrag I. Ein solcher Anspruchsgegenstand ist dem Fachmann auch unter Einbeziehung seines Fachwissens nicht
nahegelegt. Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag I wie auch die
Gegenstände der unabhängigen Ansprüche 8, 13 und 16 gemäß Hilfsantrag I beruhen somit auf einer erfinderischen Tätigkeit und sind daher patentfähig.

                                       - 34 -



c)    Die auf die unabhängigen Patentansprüche in der Fassung nach Hilfsantrag
I rückbezogenen Ansprüche 2 bis 7, 9 bis 12, 14, 15 und 17 genügen ebenfalls
den an sie zu stellenden Anforderungen hinsichtlich Zulässigkeit und Schutzfähigkeit. Gegenteiliges haben auch die Klägerinnen nicht geltend gemacht.


d)    Da die Merkmale 1.3, 8.3, 13.3 bzw. 16.2 und 16.3 der nebengeordneten
Ansprüche 1, 8, 13 und 16 nach Hilfsantrag I aus keiner der im Verfahren befindlichen Druckschriften inklusive Druckschrift NK1 bekannt sind, kann dahinstehen,
ob das Streitpatent – wie von der Klägerin ausgeführt – die beanspruchte Priorität
der finnischen Anmeldung FI 982 166 vom 6. Oktober 1998 tatsächlich zu Unrecht
in Anspruch nimmt und die NK1 damit nicht nur als vor dem Prioritätstag angemeldete, aber erst nach dem Anmeldetag des Streitpatents nachveröffentlichte
Druckschrift nach Art. 54 III EPÜ, sondern auch als Stand der Technik nach
Art. 54 II EPÜ anzusehen wäre.


                                         IV.


Da sich die beschränkte Verteidigung in der Fassung des Hilfsantrags I somit als
zulässig und schutzfähig erweist, war das Streitpatent teilweise nur hinsichtlich der
erteilten Fassung und der Fassung nach dem (neuem) Hauptantrag der Beklagten
für nichtig zu erklären, während die Klage im Hinblick auf die Fassung laut Hilfsantrag I abzuweisen war.


                                         B.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO.
Dabei ist der Senat davon ausgegangen, dass der aufgrund der Fassung nach
Hilfsantrag I verbleibende geschützte Patentgegenstand nur noch ein Drittel des
wirtschaftlichen Wertes ausmacht, der mit dem Patent aufgrund der erteilten Fassung erzielbar gewesen ist. Dementsprechend hat die Beklagte zwei Drittel der
Rechtsstreitkosten zu tragen. Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG i. V. m. § 709 ZPO.

                                         - 35 -



                                          C.

                        Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130)
eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen
elektronischen Signatur versehen sein, die von einer internationalen Organisation
auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich
zur Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die
Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen
Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument     in   die    elektronische      Poststelle   des   Bundesgerichtshofes
(www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens
aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht.



Friehe      Schwarz         Dr. Schwengelbeck     Dr. Otten-Dünnweber      Altvater

                                                                               prö
