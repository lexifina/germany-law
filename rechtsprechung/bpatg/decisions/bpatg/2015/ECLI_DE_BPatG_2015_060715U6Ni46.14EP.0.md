---
ecli: "ECLI:DE:BPatG:2015:060715U6Ni46.14EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 46/14"
decided: "2015-07-06"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=29&nr=27750&anz=851&pos=439&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2015-07-06_6_Ni_46_14_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 46/14 vom 2015-07-06

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      An Verkündungs Statt
                                                          zugestellt am
6 Ni 46/14 (EP)                                            6. Juli 2015
                                                                …
(Aktenzeichen)




                     In der Patentnichtigkeitssache

 …




 BPatG 253
 08.05

                                             -2-



                  betreffend das europäische Patent 1 212 919
                                        (DE 600 44 939)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 4. März 2015 durch die Richterin Martens als Vorsitzende, die Richterin Bayer sowie die Richter Dr.-Ing. Scholz, Dipl.-Ing. J. Müller
und Dipl.-Phys. Univ. Bieringer


für Recht erkannt:


I.   Das europäische Patent 1 212 919 wird mit Wirkung für das
     Hoheitsgebiet der Bundesrepublik Deutschland insoweit teilweise für
     nichtig erklärt, als seine Ansprüche über folgende Fassung hinausgehen:


     1. A method in a communication system for relocating a protocol
         termination point,
         characterised in the steps of:


            using a first protocol to define a protocol initialization unit (20)
            at a first termination point of a first protocol (34), said protocol
            initialization unit containing predefined information pertaining
            to initialization of a second termination point (36) of said first
            protocol, wherein the first protocol is a radio resource
            control (RRC) protocol;
            transferring the protocol initialization unit from the first
            termination point to a second termination point by a second
            protocol, wherein the protocol initialization unit (20) is
            transparent for the second protocol; and
            initializing the second termination point based on the protocol
            initialization unit (38);
            wherein

                                   -3-




      -   the protocol initialization unit is transmitted via a third
          network element between the termination points and the
          transmission by the second protocol is based on a radio
          access network application part (RANAP) protocol or
      -   the protocol initialization unit (20) is transmitted by a
          direct connection between the termination points and the
          transmission by the second protocol is based on a radio
          network subsystem application part (RNSAP) protocol.

2.   A method according to claim 1, wherein the protocol
     initialization unit (20) contains state information of the first
     protocol termination point.


3.   A method according to claim 1 or 2, wherein the first
     termination point is located at a first network element (10) of
     the communication system and the second termination point is
     located   at   a   second      network (11)   element   of   the
     communication system.


4.   A method according to claim 3, wherein the second network
     element (11), upon receiving the protocol information unit (20),
     generates and transmits a response to the first network
     element by means of the second protocol.


5.   A method according to any of the preceding claims, wherein
     the protocol initialization unit (20) is encapsulated in a
     message transmitted between the first termination point and
     the second termination point by the second protocol.


6.   A method according to any of the preceding claims, wherein
     the predefined information of the first protocol comprise one or
     several parameters of a radio resource control protocol (RRC),
     medium access control protocol (MAC), radio link control

                                    -4-



      protocol (RLC),      and/or     packet      data     convergence
      protocol (PDCP).


7.    A method according to any of the preceding claims, wherein
      the protocol initialization unit contains information of at least
      one further protocol.


8.    A method according to any of the preceding claims,
      comprising steps of:
      defining at least one further protocol initialization unit
      containing predefined information of a further protocol by the
      further protocol; and
      transferring the further protocol initialization unit from the first
      termination point to the second termination point.


9.    A method according to claim 8, wherein the further protocol
      initialization unit is transferred between the termination points
      by a protocol that is different to the second protocol.


10.   A method according to any of the preceding claims, wherein at
      least one of the termination points is located at one of the
      following: a base station controller, a radio network controller,
      a base station, a gateway.


11.   A method according to any of the preceding claims, wherein
      the step of initializing the second termination point comprises
      setting the parameters of the second termination point into a
      state that is similar to the parameters of the first termination
      point before or at the time the relocation procedure was
      initiated.


12.   A communication system, characterized in comprising:

                                   -5-



      a first protocol termination point (10);
      a second protocol termination point (11);
      control means for relocating a first protocol from the first
      protocol termination point to the second protocol termination
      point, said control means being arranged to form a protocol
      initialization unit (20) containing predefined information of the
      first protocol at the first protocol termination point by using the
      first protocol to define the protocol initialization unit (20),
      wherein the first protocol is a radio resource control (RRC)
      protocol;
      communication path (18) based on a second protocol between
      the first and the second termination points for transferring the
      protocol initialization unit, wherein the protocol initialization
      unit (20) is transparent for the second protocol; and
      control means for initializing the second protocol termination
      point based on the protocol initialization unit;
      wherein

       -   the protocol initialization unit is transmitted via a third
           network element between the termination points and the
           transmission by the second protocol is based on a radio
           access network application part (RANAP) protocol or
       -   the protocol initialization unit (20) is transmitted by a
           direct connection between the termination points and the
           transmission by the second protocol is based on a radio
           network subsystem application part (RNSAP) protocol.

13.   A communication system according to claim 12, wherein the
      protocol initialization unit (20) contains state information of the
      first protocol termination point.


14.   A communication system according to claim 12 or 13, wherein
      the control means for relocating are arranged to encapsulate
      the protocol initialization unit (20) into a message to be

                                   -6-



      transmitted from the first termination point to the second
      termination point.


15.   A communication system according to any of claims 12 to 14,
      wherein the first termination point is located at a first network
      element (10) of the communication system and the control
      means for relocating are arranged in connection with the first
      network element.


16.   A communication system according to any of claims 12 to 15,
      wherein the second termination point is located at a second
      network element (11) of the communication system and the
      control means for initializing are arranged in connection with
      the second network element.


17.   A communication system according to any of the claims 12 to
      16, wherein the protocol initialization unit contains information
      of at least one further protocol.


18.   A network element for use in a communication network,
      comprising:


      a protocol termination point;
      control means for relocating a first protocol from the protocol
      termination point to another protocol termination point,
      characterized in said control means being arranged to form a
      protocol    initialization   unit (20)   containing    predefined
      information of the first protocol at the protocol termination point
      by using the first protocol to define the protocol initialization
      unit (20), wherein the first protocol is a radio resource
      control (RRC) protocol; and

                                          -7-



             an interface to said other protocol termination point based on a
             second protocol for transferring the protocol initialization unit
             from the first termination point by means of the second
             protocol, wherein the protocol initialization unit (20) is
             transparent for the second protocol;
             wherein

              -   the protocol initialization unit is transmitted via a third
                  network element between the termination points and the
                  transmission by the second protocol is based on a radio
                  access network application part (RANAP) protocol or
              -   the protocol initialization unit (20) is transmitted by a
                  direct connection between the termination points and the
                  transmission by the second protocol is based on a radio
                  network subsystem application part (RNSAP) protocol.

       19.   A network element according to claim 18, wherein the network
             element comprises a controller of a cellular communication
             network.


       20.   A network element according to claim 18 or 19, wherein the
             control means for relocating are arranged to encapsulate the
             protocol initialization unit into a message to be transmitted
             from the first termination point by means of the second
             protocol.


       21.   A network element according to any of claims 18 to 20,
             wherein the protocol initialization unit contains information of
             at least one further protocol.


II.    Im Übrigen wird die Klage abgewiesen.


III.   Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.

                                           -8-



IV.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.



                                        Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents EP 1 212 919
(Streitpatent), das am 13. September 2000 unter Inanspruchnahme der Priorität
der britischen Patentanmeldung GB 99 21 706 vom 14. September 1999 angemeldet worden ist. Das in englischer Verfahrenssprache veröffentlichte Streitpatent trägt die Bezeichnung: „RELOCATION IN A COMMUNICATION SYSTEM“
(Umlenkung in einem Kommunikationssystem) und wird beim Deutschen Patentund Markenamt unter dem Aktenzeichen 600 44 939.4 geführt. Es umfasst in der
erteilten Fassung 28 Patentansprüche, von denen die Ansprüche 1, 17, 23 und 27
einander nebengeordnet sind und in der Verfahrenssprache nach der Streitpatentschrift (EP 1 212 919 B1) folgenden Wortlaut haben:


      “1.   A method in a communication system for relocating a protocol
            termination point, characterised in the steps of:


            using a first protocol to define a protocol initialization unit (20) at a first
            termination point of a first protocol (34), said protocol initialization unit
            containing predefined information pertaining to initialization of a second
            termination point (36) of said first protocol;


            transferring the protocol initialization unit from the first termination point
            to a second termination point by a second protocol; and


            initializing the second termination point based on the protocol
            initialization unit (38).


      17. A communication system, characterized in comprising:

                                     -9-



     a first protocol termination point (10);
     a second protocol termination point (11);
     control means for relocating a first protocol from the first protocol
     termination point to the second protocol termination point, said control
     means being arranged to form a protocol initialization unit (20)
     containing predefined information of the first protocol at the first protocol
     termination point;
     communication path (18) based on a second protocol between the first
     and the second termination points for transferring the protocol
     initialization unit; and
     control means for initializing the second protocol termination point
     based on the protocol initialization unit.


23. A network element for use in a communication network, comprising:
     a protocol termination point;
     control means for relocating a ﬁrst protocol from the protocol
     termination point to another protocol termination point, characterized in
     said control means being arranged to form a protocol initialization
     unit (20) containing predefined information of the first protocol at the
     protocol termination point; and
     interface to said other protocol termination point based on a second
     protocol for transferring the protocol initialization unit from the first
     termination point by means of the second protocol.


27. A network element for use in a communication network, comprising:
     a protocol termination point of a first protocol;
     interface to another protocol termination point characterise in being
     adapted to receive a protocol initialization unit containing predefined
     information of the first protocol at said other termination point, wherein
     the interface is based on a second protocol; and
     control means for initializing the protocol termination point based on the
     received protocol initialization unit.”

                                            - 10 -



In deutscher Übersetzung der Streitpatentschrift lauten die einander nebengeordneten Ansprüche der erteilten Fassung wie folgt:


     „1.   Verfahren in einem Kommunikationssystem zum \/erlagern eines
           Protokollendpunkts, gekennzeichnet durch:


           \/erwenden eines ersten Protokolls, um eine Protokollinitialisierungseinheit (20) an einem ersten Endpunkt von einem ersten Protokoll (34) zu bestimmen, wobei die Protokollinitialisierungseinheit eine
           vorbestimmte Information enthält, die eine lnitialisierung eines zweiten
           Endpunkts (36) des ersten Protokolls betrifft;
           Übertragen der Protokollinitialisierungseinheit von dem ersten Endpunkt
           zu einem zweiten Endpunkt durch ein zweites Protokoll; und
           lnitialisieren des zweiten Endpunkts basierend auf der Protokollinitialisierungseinheit (38).


     17. Kommunikationssystem, gekennzeichnet durch Umfassen von:


           einem ersten Protokollendpunkt (10);
           einem zweiten Protokollendpunkt (11):
           Steuermittel zum Verlagern eines ersten Protokolls von dem ersten
           Protokollendpunkt zu dem zweiten Protokollendpunkt, wobei die Steuermittel   so   eingerichtet      sind,     dass   sie   eine   Protokollinitialisierungseinheit (20), die eine vorbestimmte Information des ersten Protokolls enthält, an dem ersten Protokollendpunkt bilden;
           einem Kommunikationspfad (18), der auf einem zweiten Protokoll
           zwischen dem ersten und dem zweiten Endpunkt basiert, zum Übertragen der Protokollinitialisierungseinheit; und
           Steuermittel zum lnitialisieren des zweiten Protokollendpunkts basierend auf der Protokollinitialisierungseinheit.

                                       - 11 -



     23. Netzwerkelement zur Verwendung in einem Kommunikationsnetzwerk,
          umfassend:
          einen Protokollendpunkt;
          Steuermittel   zum    Verlagern    eines   ersten    Protokolls   von   dem
          Protokollendpunkt zu einem anderen Protokollendpunkt, dadurch
          gekennzeichnet, dass die Steuermittel so eingerichtet sind, dass sie
          eine Protokollinitialisierungseinheit (20), die eine vorbestimmte Information des ersten Protokolls enthält, an dem Protokollendpunkt bilden; und
          eine Schnittstelle zu dem anderen Protokollendpunkt, die auf einem
          zweiten   Protokoll   basiert,    zum   Übertragen    der   Protokollinitialisierungseinheit von dem ersten Endpunkt mittels des zweiten Protokolls.


     27. Netzwerkelement zur Verwendung in einem Kommunikationsnetzwerk,
          umfassend:
          einen Protokollendpunkt von einem ersten Protokoll;
          eine Schnittstelle zu einem anderen Protokollendpunkt, dadurch
          gekennzeichnet, dass es ausgelegt ist, eine Protokollinitialisierungseinheit zu empfangen, die eine vorbestimmte Information des ersten
          Protokolls an dem anderen Endpunkt enthält, wobei die Schnittstelle auf
          einem zweiten Protokoll basiert; und
          ein Steuermittel zum lnitialisieren des Protokollendpunkts basierend auf
          der empfangenen Protokollinitialisierungseinheit.“


Wegen des Wortlauts der weiteren angegriffenen, mittelbar oder unmittelbar auf
die nebengeordneten Ansprüche rückbezogenen Ansprüche 2 bis 16, 18 bis 22,
24 bis 26 und 28 wird auf die Streitpatentschrift Bezug genommen.



Die Klägerin, die das Streitpatent in vollem Umfang angreift, macht geltend, das
Streitpatent sei nicht bestandsfähig, da sein Gegenstand weder neu sei noch auf
einer erfinderischen Tätigkeit beruhe (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.

                                      - 12 -



Art. 138 Nr. 1a, Art. 52 bis 57 EPÜ). Soweit sie die Nichtigkeitsklage zusätzlich
damit begründet hatte, das Streitpatent offenbare die Erfindung nicht so deutlich
und vollständig, dass ein Fachmann sie ausführen könne, verfolgt sie diesen
Nichtigkeitsgrund nicht weiter.


Die Klägerin stützt ihren Vortrag zur fehlenden Patentfähigkeit auf folgende Unterlagen:


     NK6     WO 99/51051 A2

     NK7     CH 682 867 A5

     NK8     ETSI/3GPP-Dokument TSGR3#6(99)A61

     NK8a, NK8b, NK8c Screenshots zum Abrufen und Auffinden von NK8 über
             die Webseite www.3gpp.org

     NK8d ETSI Directives, Juni 1999

     NK8e    Kopie einer E-Mail an die Mitglieder der 3GPP TSG-RAN Working
             Group 3          vom     30. August 1999.       Abrufbar        über
             http://list.etsi.orglscriptslwa.exe?A2=ind9908&L=3gpp_tsg_ran_wg3&
             T=0&P=21 094)

     NK8f    Bericht über das Treffen #6 der 3GPP TSG-RAN Working Group 3
             vom 23. bis 27. August 1999 in Sophia Antipolis (in Auszügen)

     NK8g Bericht über das Treffen #7 der 3GPP TSG-RAN Working Group 3
             vom 20. bis 24. September 1999 in Sophia Antipolis

     NK8h Kopie       eines   Schreibens   vom   28. Januar 2014   aus   dem      in
             Großbritannien geführten Verletzungsprozess betr. das Streitpatent

     NK8i    E-mail-Korrespondenz zwischen M…3 GPP
             Specifications Manager, Director, ETSI Mobile Competence Centre
             und C…, Director of Patent Prosecution, O… LLP
             vom 13/14. März 2014

     NK9     Technische Spezifikation 3Gpp TS 25.413 Version 1.0.0

                               - 13 -



NK10 ETSI/3GPP-Dokument TSGR3#3(99)359

NK11 ETSI/3GPP-Dokument TSGR3#4(99)455

NK12 ETSI/3GPP-Dokument TSGR3#3(99)328

NK13 ETSI/3GPP-Dokument TSGR3#3(99)385

NK14 ETSI/3GPP-Dokument TSGR3#5(99)678

NK18 TIA/EIA     Standard,   MSC-BS     Interface   for   Public   Wireless
       Communications Systems, TIA/EIA-634-B, April 1999 sowie Auszüge
       daraus als Anlage NK18a

NK18b TIA-2000.000, CDMA, List of Standards,

NK19 TIA/EIA Telecommunications Systems Bulletin, Support for 14.4 kbps
       Data Rate and PCS Interaction for Wideband Spread Spectrum
       Cellular Systems, TSB 74, Dezember 1995 sowie Auszüge daraus
       als Anlage NK19a

NK20 ANSI, Personal Station-Base Station Compatibility Requirements for
       1.8 to 2.0 GHz CDMA Personal Communications Systems mit
       Auszügen daraus als Anlage NK20a

NK21 Auszug aus dem Protokoll zum Rechtsstreit zwischen Z… (UK) Ltd.
       und V… Inc. betreffend das Streitpatent vor dem High
       Court of Justice in London zu Aktenzeichen HC 12 D 03895, am
       29. Oktober 2014 (2. Verhandlungstag)

NK22 “First expert report of B…” vom 29. August 2014,
       Gutachten des … vor dem High Court of Justice zu
       Aktenzeichen HC 12 D 03895.

                                         - 14 -



Die Klägerin beantragt,

        das europäische Patent 1 212 919 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,

        die Klage insoweit abzuweisen, als sie sich gegen die mit
        Hauptantrag verteidigte Fassung der Patentansprüche 1 - 28,
        eingegangen mit Schriftsatz vom 16. Januar 2015, richtet.

Hilfsweise verteidigt sie das Streitpatent mit den Fassungen der Hilfsanträge 1 bis
5, eingegangen mit Schriftsatz vom 16. Januar 2015.



Die in erster Linie verteidigte Fassung des Streitpatents - Hauptantrag- weist
gegenüber der erteilten Fassung in den Ansprüchen 17, 23 und 27 folgende
hervorgehobenen Änderungen auf:

“17. A communication system, characterized in comprising:

    a first protocol termination point (10);
    a second protocol termination point (11);
    control means for relocating a first protocol from the first protocol termination
    point to the second protocol termination point, said control means being
    arranged to form a protocol initialization unit (20) containing predefined
    information of the first protocol at the first protocol termination point by using
    the first protocol to define the protocol initialization unit (20);
    communication path (18) based on a second protocol between the first and the
    second termination points for transferring the protocol initialization unit; and
    control means for initializing the second protocol termination point based on
    the protocol initialization unit.

                                          - 15 -



23. A network element for use in a communication network, comprising:


    a protocol termination point;
    control means for relocating a first protocol from the protocol termination point
    to another protocol termination point, characterized in said control means
    being arranged to form a protocol initialization unit (20) containing predefined
    information of the first protocol at the protocol termination point by using the
    first protocol to define the protocol initialization unit (20); and
    an interface to said other protocol termination point based on a second
    protocol for transferring the protocol initialization unit from the first termination
    point by means of the second protocol.


27. A network element for use in a communication network, comprising:


    a protocol termination point of a first protocol;
    an interface to another protocol termination point characterised in being
    adapted to receive a protocol initialization unit for relocating the other protocol
    termination point, wherein the protocol initialization unit is defined by using the
    first protocol and containing contains predefined information of the first
    protocol at said other termination point, wherein the interface is based on a
    second protocol; and
    control means for initializing the protocol termination point based on the
    received protocol initialization unit.”


In der Fassung nach den Hilfsanträgen 1 bis 4 lauten die einander nebengeordneten Ansprüche mit gegenüber der erteilten Fassung hervorgehobenen Änderungen jeweils wie folgt:

                                           - 16 -



Hilfsantrag 1:


 “1. A method in a communication system for relocating a protocol termination
     point, characterised in the steps of:
     using a first protocol to define a protocol initialization unit (20) at a first
     termination point of a first protocol (34), said protocol initialization unit
     containing predefined information pertaining to initialization of a second
     termination point (36) of said first protocol;
     transferring the protocol initialization unit from the first termination point to a
     second termination point by a second protocol, wherein the protocol
     initialization unit (20) is transparent for the second protocol; and
     initializing the second termination point based on the protocol initialization
     unit (38).


17 16. A communication system, characterized in comprising:


       a first protocol termination point (10);
       a second protocol termination point (11);
       control means for relocating a first protocol from the first protocol
       termination point to the second protocol termination point, said control
       means being arranged to form a protocol initialization unit (20) containing
       predefined information of the first protocol at the first protocol termination
       point by using the first protocol to define the protocol initialization unit (20);
       communication path (18) based on a second protocol between the first and
       the second termination points for transferring the protocol initialization unit,
       wherein the protocol initialization unit (20) is transparent for the second
       protocol; and
       control means for initializing the second protocol termination point based on
       the protocol initialization unit.

                                          - 17 -



23 22. A network element for use in a communication network, comprising:


       a protocol termination point;
       control means for relocating a first protocol from the protocol termination
       point to another protocol termination point, characterized in said control
       means being arranged to form a protocol initialization unit (20) containing
       predefined information of the first protocol at the protocol termination point
       by using the first protocol to define the protocol initialization unit (20); and
       an interface to said other protocol termination point based on a second
       protocol for transferring the protocol initialization unit from the first
       termination point by means of the second protocol, wherein the protocol
       initialization unit (20) is transparent for the second protocol.”




Hilfsantrag 2:


 “1. A method in a communication system for relocating a protocol termination
     point, characterised in the steps of:


     using a first protocol to define a protocol initialization unit (20) at a first
     termination point of a first protocol (34), said protocol initialization unit
     containing predefined information pertaining to initialization of a second
     termination point (36) of said first protocol, wherein the first protocol is a radio
     resource control (RRC) protocol;
     transferring the protocol initialization unit from the first termination point to a
     second termination point by a second protocol, wherein the protocol
     initialization unit (20) is transparent for the second protocol; and
     initializing the second termination point based on the protocol initialization
     unit (38).

                                          - 18 -



17 16. A communication system, characterized in comprising:


      a first protocol termination point (10);
      a second protocol termination point (11);
      control means for relocating a first protocol from the first protocol
      termination point to the second protocol termination point, said control
      means being arranged to form a protocol initialization unit (20) containing
      predefined information of the first protocol at the first protocol termination
      point by using the first protocol to define the protocol_initialization unit (20),
      wherein the first protocol is a radio resource control (RRC) protocol;
      communication path (18) based on a second protocol between the first and
      the second termination points for transferring the protocol initialization unit,
      wherein the protocol initialization unit (20) is transparent for the second
      protocol; and
      control means for initializing the second protocol termination point based on
      the protocol initialization unit.


23 22. A network element for use in a communication network, comprising:


      a protocol termination point;
      control means for relocating a first protocol from the protocol termination
      point to another protocol termination point, characterized in said control
      means being arranged to form a protocol initialization unit (20) containing
      predefined information of the first protocol at the protocol termination point
      by using the first protocol to define the protocol initialization unit (20),
      wherein the first protocol is a radio resource control (RRC) protocol; and
      an interface to said other protocol termination point based on a second
      protocol for transferring the protocol initialization unit from the first
      termination point by means of the second protocol, wherein the protocol
      initialization unit (20) is transparent for the second protocol.”

                                         - 19 -



Hilfsantrag 3:


 “1. A method in a communication system for relocating a protocol termination
     point, characterised in the steps of:


     using a first protocol to define a protocol initialization unit (20) at a first
     termination point of a first protocol (34), said protocol initialization unit
     containing predefined information pertaining to initialization of a second
     termination point (36) of said first protocol, wherein the first protocol is a radio
     resource control (RRC) protocol;
     transferring the protocol initialization unit from the first termination point to a
     second termination point by a second protocol, wherein the protocol
     initialization unit (20) is transparent for the second protocol; and
     initializing the second termination point based on the protocol initialization
     unit (38),
     so that a single protocol defines the information to be transferred thereby
     avoiding a need for defining parameters of one protocol in another protocol.


17 16. A communication system, characterized in comprising:


       a first protocol termination point (10);
       a second protocol termination point (11);
       control means for relocating a first protocol from the first protocol
       termination point to the second protocol termination point, said control
       means being arranged to form a protocol initialization unit (20) containing
       predefined information of the first protocol at the first protocol termination
       point by using the first protocol to define the protocol_initialization unit (20),
       wherein the first protocol is a radio resource control (RRC) protocol;
       communication path (18) based on a second protocol between the first and
       the second termination points for transferring the protocol initialization unit,
       wherein the protocol initialization unit (20) is transparent for the second
       protocol; and

                                           - 20 -



       control means for initializing the second protocol termination point based on
       the protocol initialization unit,
       so that a single protocol defines the information to be transferred thereby
       avoiding a need for defining parameters of one protocol in another protocol.


23 22. A network element for use in a communication network, comprising:


       a protocol termination point;
       control means for relocating a first protocol from the protocol termination
       point to another protocol termination point, characterized in said control
       means being arranged to form a protocol initialization unit (20) containing
       predefined information of the first protocol at the protocol termination point
       by using the first protocol to define the protocol initialization unit (20),
       wherein the first protocol is a radio resource control (RRC) protocol; and
       an interface to said other protocol termination point based on a second
       protocol for transferring the protocol initialization unit from the first
       termination point by means of the second protocol, wherein the protocol
       initialization unit (20) is transparent for the second protocol,
       so that a single protocol defines the information to be transferred thereby
       avoiding a need for defining parameters of one protocol in another
       protocol.”




Hilfsantrag 4:


“1. A method in a communication system for relocating a protocol termination
    point, characterised in the steps of:


    using a first protocol to define a protocol initialization unit (20) at a first
    termination point of a first protocol (34), said protocol initialization unit
    containing predefined information pertaining to initialization of a second

                                           - 21 -



   termination point (36) of said first protocol, wherein the first protocol is a radio
   resource control (RRC) protocol;
   transferring the protocol initialization unit from the first termination point to a
   second termination point by a second protocol, wherein the protocol
   initialization unit (20) is transparent for the second protocol; and
   initializing the second termination point based on the protocol initialization
   unit (38);
   wherein
     -     the protocol initialization unit is transmitted via a third network element
           between the termination points and the transmission by the second
           protocol is based on a radio access network application part (RANAP)
           protocol or
     -     the protocol initialization unit (20) is transmitted by a direct connection
           between the termination points and the transmission by the second
           protocol is based on a radio network subsystem application part
           (RNSAP) protocol.


1712. A communication system, characterized in comprising:


         a first protocol termination point (10);
         a second protocol termination point (11);
         control means for relocating a first protocol from the first protocol
         termination point to the second protocol termination point, said control
         means being arranged to form a protocol initialization unit (20) containing
         predefined information of the first protocol at the first protocol termination
         point by using the first protocol to define the protocol initialization unit (20),
         wherein the first protocol is a radio resource control (RRC) protocol;
         communication path (18) based on a second protocol between the first and
         the second termination points for transferring the protocol initialization unit,
         wherein the protocol initialization unit (20) is transparent for the second
         protocol; and

                                             - 22 -



         control means for initializing the second protocol termination point based on
         the protocol initialization unit;
         wherein

         - the protocol initialization unit is transmitted via a third network element
           between the termination points and the transmission by the second
           protocol is based on a radio access network application part (RANAP)
           protocol or
         - the protocol initialization unit (20) is transmitted by a direct connection
           between the termination points and the transmission by the second
           protocol is based on a radio network subsystem application part
           (RNSAP) protocol.

2318. A network element for use in a communication network, comprising:


     a protocol termination point;
     control means for relocating a first protocol from the protocol termination
     point to another protocol termination point, characterized in said control
     means being arranged to form a protocol initialization unit (20) containing
     predefined information of the first protocol at the protocol termination point by
     using the first protocol to define the protocol initialization unit (20), wherein
     the first protocol is a radio resource control (RRC) protocol; and
     an interface to said other protocol termination point based on a second
     protocol for transferring the protocol initialization unit from the first termination
     point by means of the second protocol, wherein the protocol initialization
     unit (20) is transparent for the second protocol;
     wherein

     -      the protocol initialization unit is transmitted via a third network element
            between the termination points and the transmission by the second
            protocol is based on a radio access network application part (RANAP)
            protocol or
     -      the protocol initialization unit (20) is transmitted by a direct connection
            between the termination points and the transmission by the second
            protocol is based on a radio network subsystem application
            part (RNSAP) protocol.”

                                       - 23 -



Die Beklagte tritt dem Vorbringen der Klägerin in allen Punkten entgegen. Die Gegenstände des Streitpatents seien gegenüber dem im Verfahren befindlichen
Stand der Technik neu und beruhten auf einer erfinderischen Tätigkeit. Jedenfalls
in einer der hilfsweise zur Entscheidung gestellten Fassungen sei das Streitpatent
daher bestandsfähig.
Zum Wissen des Fachmanns am Prioritätstag nimmt die Beklagte Bezug auf
folgende Druckschriften:


     MN4     Technische Spezifikation 3GPP TS 25.423, „UTRAN Iur Interface
             RNSAP Signalling“, Version 1.1.1, Juni 1999

     MN8     Mouly,    M.,   Pautet,   M.:      „The   GSM-System     for    Mobile
             Communications” 1992, ISBN 2-9507190-0-7, Auszüge: Seiten 11-
             15, 118-122, 166-170, 260-266

     MN9     Technische Spezifikation, ETSI, TS 100 590, „Digital cellular
             telecommunications system (Phase 2+); Mobile-services Switching
             Centre -Base Station System (MSC - BSS) interface; Layer 3
             specification (GSM 08.08 version 7.2.0 Release 1998)“, Juli 1999,
             Auszüge: Seiten 1-30, 71-75, 114-118

     MN10 Technische Spezifikation 3GPP TS 25.413, „UTRAN Iu Interface
             RANAP Signalling“, Version 1.0.2, Juni 1999

     MN11 ETSI/3GPP-Dokument:           TSGR3#3(99)325,     TSG-RAN         Working
             Group 3 meeting #3, “Updated proposed new presentation for Iu
             RANAP procedure ‘Servicing RNS relocation”, April 1999

     MN12 ETSI/3GPP-Dokument:           TSGR3#3(99)438,     TSG-RAN         Working
             Group 3 meeting #4, “Sequence charts of User Data Retrieve at
             SRNS Relocation for IP domain”, Juni 1999

     MN13 ETSI/3GPP-Dokument:           TSGR3#3(99)441,     TSG-RAN         Working
             Group 3 meeting #4, “Draft Minutes of Meeting #3”, Juni 1999

                                       - 24 -



     MN14 ETSI/3GPP-Dokument:           TSGR3#8(99)e44,       TSG-RAN      Working
             Group 3 meeting #8, “Response to RAN WG3 LS regarding
             Relocation and GSM-UMTS handover” , 20. bis 24. September 1999

     MN15 Technische       Spezifikation   3GPP    TS    25.331,   „RRC    Protocol
             Specification“, Version 3.0.0, Oktober 1999 , Auszüge: Seiten 1-19,
             245-250.


Wegen des Vorbringens der Parteien im Übrigen einschließlich der vorgelegten
Unterlagen wird auf die gewechselten Schriftsätze Bezug genommen.
Der Senat hat den Parteien zur Vorbereitung der mündlichen Verhandlung einen
qualifizierten Hinweis vom 15. Dezember 2014 zugestellt.




                          Entscheidungsgründe


Die Klage ist zulässig, aber nur zum Teil begründet. Soweit die Beklagte die erteilte Fassung nicht mehr verteidigt, war das Streitpatent mit Wirkung für die Bundesrepublik Deutschland ohne Sachprüfung für nichtig zu erklären (zur st. Rspr. im
Nichtigkeitsverfahren vgl. z. B. BGH GRUR 2007, 404, 405 - Carvedilol II;
Busse/Keukenschrijver, PatG, 7. Aufl., § 82 Rdn. 90 m. w. Nachw.; Schulte/Voit,
PatG, 9. Aufl., § 81 Rdn. 128). Mit der in erster Linie verteidigten Fassung (Hauptantrag) kann das Streitpatent mangels Patentfähigkeit jedoch keinen Bestand haben (Artikel II § 6 Absatz 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m.
Art. 56 EPÜ). Dies gilt auch für die Fassungen der Patentansprüche nach den
Hilfsanträgen 1 bis 3. Soweit die Beklagte das Streitpatent mit der Fassung nach
Hilfsantrag 4 zulässigerweise verteidigt, ist sein Gegenstand gegenüber dem
Stand der Technik am Prioritätstag neu und beruht demgegenüber auch auf einer
erfinderischen Tätigkeit. Insoweit war die Nichtigkeitsklage daher abzuweisen.

                                          - 25 -



                         I. Gegenstand des Streitpatents


1. Das   Streitpatent   betrifft   nach   seiner   Bezeichnung   „Relocation   in   a
communication system“ die Verlagerung einer bestehenden Mobilfunkverbindung
in einem Kommunikationssystem. Nach den erteilten Ansprüchen betrifft die
Verlagerung diejenige eines Protokollendpunktes.
Zum allgemeinen technischen Hintergrund führt das Streitpatent aus, Protokolle
stellten die Regeln dar, nach denen im Netzwerk die Kommunikation erfolge; diese
Regeln/Protokolle ergäben sich aus den zugehörigen Standards. Während einer
aktiven Verbindung im Netzwerk habe ein Protokoll einen Endpunkt in einem
Netzwerkelement, das die Verbindung steuere (vgl. Streitpatent [0002]).
In den darauf folgenden Absätzen stellt das Streitpatent auf ein zelluläres
Funknetzwerk ab und hebt hervor, dass sich die Zuständigkeit für das Steuern
einer Verbindung zwischen Mobilstation und Netzwerk während der laufenden
Verbindung ändern könne. Daher sei es nötig, zumindest einen Teil der
Funktionalitäten, die mit der Verbindung assoziiert würden, zu verlagern, um z. B.
die Verbindung nicht zu verlieren oder um die Qualität der Verbindung zu erhalten
(vgl. Streitpatent [0005]). Eines der Merkmale, das verlagert werden soll, sei der
Zustand eines Protokollendpunktes. Als Stand der Technik schildert das
Streitpatent, dass die zu übermittelnden Parameter in den beiden Protokollen
definiert werden müssten, die verwendet würden, um die Informationen vom alten
Endpunkt auf den neuen Endpunkt zu übertragen. Das erfordere die Verlagerung
sehr vieler zusätzlicher Parameter und erhöhe die Komplexität der Steuerung.


Nach Absatz [0008] der Streitpatentschrift sei es Aufgabe der Erfindung,
zumindest eines der geschilderten Probleme zu lösen.


Demgemäß schlägt das Streitpatent in der erteilten Fassung ein Verfahren zum
Verlagern eines der Protokollendpunkte gemäß Patentanspruch 1 sowie ein
Kommunikationssystem gemäß Patentanspruch 17 und Netzwerkelemente gemäß
den Patentansprüchen 23 und 27 vor.

                                      - 26 -



In den Ausführungsbeispielen beschreibt das Streitpatent das Verlagern
(„relocation“) einer bestehenden Mobilfunkverbindung im Einzelnen unter Verwendung der Terminologie des vorgeschlagenen Universal Mobile Telecommunication
Systems (UMTS), wobei die Erfindung nicht darauf beschränkt sein solle (vgl.
Streitpatent [0022]).
Die Kernidee der erfindungsgemäßen Lehre beschreibt das Streitpatent im
Ausführungsbeispiel der Absätze [0030] bis [0038]. Demgemäß wird eine „protocol
initialization unit“ (i. W. von Senat und Parteien als PIU bezeichnet) entsprechend
einer speziellen PDU des RRC-Protokolls zwischen den beiden Endpunkten
„serving RNC“ und Mobilstation erzeugt und diese transparent in das RANAP-Protokoll (alternativ RNSAP) eingefügt, um einen zweiten RNC (den „drift RNC“)
zum neuen serving RNC zu machen. Damit wird die Verbindung der Mobilstation
mit dem serving RNC gemäß RRC-Protokoll zum zweiten RNC, der nun die
Funktionalität des serving RNC übernimmt, verlagert („relocation“). Die Protokolle
und entsprechenden Schnittstellen (Iu, Iur) veranschaulicht die Streitpatentschrift
in Fig. 3:




2. Das Streitpatent wendet sich somit an einen Ingenieur der Nachrichtentechnik
mit Universitätsabschluss oder vergleichbaren in der Entwicklung erworbenen
Kenntnissen, der an der Erarbeitung von Standards für Mobilfunkkommunikations-

                                         - 27 -



systeme (RAN - „Radio Access Network“) beteiligt ist oder zumindest deren
Erstellung verfolgt und fundierte Kenntnisse der einschlägigen Übertragungsprotokolle sowie der zugehörigen Netzwerkkomponenten besitzt. Zum Zeitrang
des Streitpatents (14. September 1999) gehören zum Fachwissen insbesondere
die Diskussionen der einschlägigen Arbeitsgruppen (insbesondere „TSG-RAN
working Group 3“) und deren Arbeitspapiere, soweit sie allgemein zugänglich auf
dem Server des Europäischen Institut für Telekommunikationsnormen (ETSI:
European Telekommunications Standards Institute) abgelegt sind. Zur Standardisierung von UMTS und der Weiterentwicklung von GSM haben sich mehrere
Standardisierungsgremien – darunter ETSI – zum 3rd Generation Partnership
Project (3GPP) zusammengeschlossen, so dass sich der Fachmann vorliegend
gleichfalls über den 3GPP-Server über das am Prioritätstag zur Verfügung
stehende Wissen informiert. Dies betrifft insbesondere die technische Lehre der
von der Klägerin eingereichten Dokumente NK8 und NK9 bis NK14 sowie der von
der Beklagten eingereichten Dokumente MN10 bis MN13.




                      II. Zur Fassung gemäß Hauptantrag


1. Zur Lösung des genannten Aufgabenkomplexes wird mit dem Patentanspruch 1, in der Fassung nach Hauptantrag, der mit dem erteilten Patentanspruch 1 identisch ist, ein Verfahren vorgeschlagen, das sich in folgende Merkmale gliedern lässt (Übersetzung gemäß Patentschrift kursiv hinzugefügt):


     M1       A method in a communication system for relocating a
              protocol termination point, characterised in the steps of:
              Verfahren in einem Kommunikationssystem zum Verlagern eines
              Protokollendpunkts, gekennzeichnet durch

     M1.1     using a first protocol to define a protocol initialization
              unit (20) at a first termination point of a first protocol (34),
              Verwenden           eines      ersten     Protokolls,  um      eine
              Protokollinitialisierungseinheit (20) an einem ersten Endpunkt von
              einem ersten Protokoll (34) zu bestimmen,

                                            - 28 -



     M1.1.1    said protocol initialization unit containing predefined
               information     pertaining     to     initialization   of    a    second
               termination point (36) of said first protocol;
               wobei die Protokollinitialisierungseinheit eine vorbestimmte Information
               enthält, die eine Initialisierung eines zweiten Endpunkts (36) des ersten
               Protokolls betrifft;

     M1.2      transferring the protocol initialization unit from the first
               termination point to a second termination point by a second
               protocol; and
               Übertragen der Protokollinitialisierungseinheit von dem ersten
               Endpunkt zu einem zweiten Endpunkt durch ein zweites Protokoll; und

     M1.3      initializing the second termination point based on the
               protocol initialization unit (38).
               lnitialisieren    des    zweiten    Endpunkts    basierend       auf   der
               Protokollinitialisierungseinheit (38).



2. Einige Begriffe in den vorgenannten Ansprüchen des Streitpatents (in der
Fassung gemäß Hauptantrag) bedürfen einer Erläuterung. Nach Ansicht des
Senats versteht der Fachmann die Gegenstände der unabhängigen Patentansprüche und die verwendeten Begriffe unter Heranziehen der Beschreibung und
der Figuren des Streitpatents wie folgt:


Begriff „relocation“ in Abgrenzung zu „handover/handoff“


Aus dem GSM-System ist dem Fachmann der Fachbegriff „handover“ (manchmal
auch als „handoff“ bezeichnet) bekannt. Er versteht darunter das Übernehmen
einer Mobilfunkverbindung zwischen mobilem Endgerät (MS) und einer ersten
Basisstation (BTS) durch eine zweite Basisstation. Dabei wird die Verbindung
zwischen dem mobilen Endgerät und der ersten Basisstation (BTS) beendet und
danach eine neue Verbindung auf einem anderen Kanal zwischen dem mobilen
Endgerät und der zweiten Basisstation aufgebaut („hard handover“). Dies führt zu
einer (in der Regel kurzen) Unterbrechung der Verbindung. Der „hard handover“
erfolgt, wenn sich ein Benutzer mit seinem mobilen Endgerät von einer Funkzelle
in eine benachbarte Funkzelle bewegt.

                                            - 29 -



Dem Fachmann ist darüber hinaus auch die Technik des „soft handovers“ bekannt
(vgl.   Streitpatentschrift,    Abs. [0005]),    wobei   das   mobile   Endgerät    im
Überlappungsbereich benachbarter Mobilfunkzellen mit zwei Basisstationen
zugleich verbunden ist („macrodiversity“ bzw. „Makrodiversität“) und die Übergabe
der Mobilfunkverbindung von der ersten Basisstation an die zweite Basisstation
erst nach Herstellen einer entsprechenden Verbindung erfolgt.


Der Fachmann unterscheidet darüber hinaus zwischen „internal handover“ und
„external handover“, wobei die am Handover beteiligten Basisstationen (BTS) von
einem     gemeinsamen          (internal)   Controller (BSC/RNC)   bzw.   von      zwei
verschiedenen Controllern gesteuert werden und außerdem eine Übergabe der
Kommunikationsparameter zwischen den beiden Controllern erfolgt (external).


„Relocation“ hat sich während der Standardisierungsphase für UMTS als
Fachbegriff herausgebildet und betrifft im Zusammenhang mit UMTS die
Verlagerung einer Mobilfunkverbindung zwischen einem Endgerät und dem
serving RNC zu einem anderen RNC. Dabei wird die Verbindung zwischen
Endgerät (Mobiltelefon) und RNC (radio network controller) nicht unterbrochen.
Der Fachmann unterscheidet zwischen serving RNC (SRNC) und einem drift RNC
(DRNC), wobei am serving RNC ein Protokollendpunkt des RRC-Protokolls (radio
resource control-Protokoll) implementiert ist (der andere Protokollendpunkt
befindet sich im Endgerät), wobei der Drift RNC aber bereits Daten empfängt und
weiterleitet. Jedes Endgerät (UE) hat genau einen serving RNC. „Relocation“
betrifft das Umziehen des einen Protokollendpunkts am serving RNC zu einem
anderen RNC, d. h. der drift RNC wird zum serving RNC.

Zur Begrifflichkeit „protocol initialization unit“


Nach Überzeugung des Senats ist „protocol initialization unit“ (i. W. mit PIU
abgekürzt) kein Fachbegriff zum Zeitrang des Streitpatents, sondern ist aus der
Streitpatentschrift heraus zu verstehen. Die Beschreibung, Sp. 7, Z. 28-33,
vermittelt dem Fachmann, dass eine spezielle PDU („protocol data unit“) mit
vordefinierten Parametern für die Initialisierung des zweiten Protokollendpunkts

                                             - 30 -



erzeugt wird. Aus Abs. [0038] entnimmt der Fachmann, dass verschiedene PIUs
aus verschiedenen Protokollen erzeugt werden können. Der Fachmann versteht
also unter einer „protocol initialization unit“, eine PDU, die durch ein (erstes)
Protokoll erzeugt wurde. Abs. [0034] der Streitpatentschrift vermittelt dem
Fachmann in einem Ausführungsbeispiel, dass eine „special protocol initialization
unit“ durch die „control unit 20“ des source RNCs erzeugt wird, wobei sie eine
RRC PDU ist. Der Inhalt dieser RRC PDU betrifft vordefinierte RRC Parameter,
welche am neuen Protokollendpunkt (target RNC) benötigt werden.
Dem Fachmann ist der Begriff „PDU“ als solcher bekannt. Er bezeichnet die
Gesamtheit aller Nutz- und Steuerdaten einer Übertragung gemäß einem
Protokoll. Zum Basiswissen des Fachmanns zählt das OSI-Schichtenmodell,
gemäß        dem   Protokolle     zwischen     Kommunikationspartnern   (physikalisch)
schichtweise gestapelt sind
(„protocol     stack“).    Sie
korrespondieren mit ihrem
Kommunikationspartner (logisch) innerhalb derselben
Schicht („layer“). Die anfallenden Daten werden auf
der     sendenden         Seite
schichtweise verpackt (Prinzip der russischen Matroschka) und auf der
empfangenden Seite entsprechend entpackt. Die Beklagte hat in der mündlichen
Verhandlung aus NK22, S. 13 vorgetragen und die dortige Fig. 4 detailliert
erläutert. Insoweit stimmt die Erläuterung der Beklagten zum OSI-Schichtenmodell
mit dem Wissen des Fachmanns überein. Eine PDU besteht aus einem
protokollspezifischen Header mit Steuerinformationen und einer Service Data
Unit (SDU) mit Nutzdaten, die zusammen der PDU der nächst höheren Schicht
(Layer) entspricht (= Prinzip der Verkapselung).

                                                   - 31 -



Sofern die Beklagte vorträgt, die RRC-PDU enthalte keine Header, kann der Senat
dieser        Auslegung       nicht      folgen.   Denn     eine   PDU   besteht   aus   einem
protokollspezifischen Header und einer Service Data Unit (SDU). Daher kann der
Fachmann          die        „protocol
initialization unit“ (PIU) nur
als PDU inklusive einem
RRC-Header verstehen. Die
Beklagte        hat     in    diesem
Kontext        argumentiert,      die
RRC-PDU werde in das
RANAP-Protkoll                  (radio
access network application
part-Protokoll) eingefügt und
dies     in     der     mündlichen
Verhandlung durch folgende Skizze unterstützt: In der Mitte der Skizze ist der OSI-Layer 3 mit dem RANAP-Protokoll dargestellt. Es ist zu erkennen und wurde von
der Beklagten erläutert, dass die PIU als Protokoll-PDU („PIU=PDU“) anstelle der
PDU des darüber liegenden OSI-Layers eingefügt wird.


Der weitere Vortrag der Klägerin, die PIU sei im Sinne einer Copy mit der PDU
identisch, stützt die Auslegung des Senats, dass die „protocol initialization unit“
(PIU) mit einer Protokoll-PDU identisch ist und als SDU mit dem RANAP-Protokoll
transportiert werde. Dies entnimmt der Fachmann auch dem Ausführungsbeispiel
der Beschreibung gemäß Streitpatentschrift, wonach die RRC PDU im zweiten
Protokoll (Merkmal M1.2), beispielsweise RANAP oder RNSAP (radio network
subsystem application part), verkapselt werden könne, vgl. Abs. [0037].

Dieses Verständnis kann jedoch den Ansprüchen nach Hauptantrag und
Hilfsanträgen nur teilweise zugebilligt werden. So wird das RRC-Protokoll und
somit die Festlegung der PIU als RRC-PDU erst im Hilfsantrag 2, das RANAP
bzw. RSNAP-Protokoll erst im Hilfsantrag 4 festgelegt. Die Verfahren nach
Hauptantrag und Hilfsantrag 1 bis 3 lassen somit auch die Erstellung einer PDU,

                                       - 32 -



wie sie beim Übergang von einer Schicht des OSI-Modells in eine tiefere Schicht
üblich ist, zu.
Den Unterschied zwischen PDU und PIU sieht der Fachmann nach Überzeugung
des Senats in ihrer Zweckbestimmung, bei der PDU zum Datentransport
allgemein, bei der PIU dagegen speziell zur Initialisierung des RNC.


3. Der Gegenstand in der verteidigten Fassung des Streitpatents nach
Hauptantrag ist zwar gegenüber den von der Nichtigkeitsklägerin in das Verfahren
eingeführten Druckschriften neu, beruht aber weder in der verteidigten Fassung
nach Hauptantrag noch nach einem der Hilfsanträge 1, 2 oder 3 gegenüber dem
Stand der Technik auf einer erfinderischen Tätigkeit.


Der Gegenstand des Patentanspruchs 1 der verteidigten              Fassung nach
Hauptantrag ist dem Fachmann aus der NK8 nahegelegt. Der Hauptantrag ist
mangels Patentfähigkeit (Art. 56 EPÜ i. V. m. mit Art. 54 Abs. 2 EPÜ) zur
Selbstbeschränkung nicht geeignet.


Die NK8 (=TSGR3#6(99)A61) betrifft ein Arbeitspapier zur Diskussion unter
Fachleuten        der TSG-RAN Working     Group 3       (i.W. WG3), die   sich   am
Standardisierungsprozess für UMTS beteiligen. Es betrifft die Verlagerung eines
Protokollendpunktes für den Handover zwischen GSM und UMTS (Titel: „LS
regarding Relocation and GSM-UMTS handover“). Aus der NK8 geht hervor, dass
sich die Arbeitsgruppe WG3 bereits auf die unter Ziffern 1) bis 3) genannten
Verfahrensmerkmale geeinigt hat (vgl. 4. Abs: „Currently RAN WG3 has adopted
following assumptions:“). Aus Ziff. 1) entnimmt der Fachmann, dass der alte RNC
(„source RNC“) grundsätzlich alle notwendigen Informationen bereitstellt, die für
das Starten (entspricht einem Initialisieren) der Verbindung zwischen einem
RNC/Node-B/BTS mit dem mobilen Endgerät benötigt werden („UTRAN-UE
connection that is required by target RNC to start the Serving RNC operation“).
Diese Information soll vom alten RNC zum neuen RNC übertragen werden und
sich in einer als „Source RNC to target RNC Transparent Field“ bezeichneten

                                        - 33 -



Entität befinden. Die gemäß NK8 bereitgestellten Daten werden über das Iu-Interface mit RANAP an den neuen RNC übertragen.


Im Einzelnen ist mit den Worten des Patentanspruchs 1 aus der NK8 bekannt:



     M1     A method in a communication system (NK8, Titel: „...GSM-UMTS
            handover”) for relocating (NK8, Titel: „...regarding Relocation...”) a
            protocol termination point (NK8, S. 1, Z. 37-38: Serving RNC wird
            vom source RNC zum target RNC verlagert), characterised in the
            steps of:
     M1.1   using a first protocol (gemäß NK8, S. 1, Z. 37-38, besteht eine
            Verbindung zwischen UTRAN und UE. Die Informationen dieser
            Verbindung sollen von einem RNC (“source”) zu einem anderen
            (“target”) übermittelt werden. Daher müssen die Informationen des
            Protokolls zwischen den beiden Endpunkten UTRAN und UE
            verwendet werden, um diese Informationen bereitzustellen) to define
            a protocol initialization unit at a first termination point of a first
            protocol (keine PDU, jedoch „Source RNC to target RNC Transparent
            Field“, welche die Informationen zum Starten des target RNCs als
            SRNC aufweist, vgl. NK8, S. 1, Z. 37 ff.).
     M1.1.1 said protocol initialization unit containing predefined information
            pertaining to initialization of a second termination point of said first
            protocol (vgl. NK8, S. 1, Z. 37 ff.);
     M1.2   transferring the protocol initialization unit from the first termination
            point to a second termination point by a second protocol; and
            („Source RNC to target RNC Transparent Field“ wird über die Iu-Schnittstelle mit RANAP-Protokoll übertragen, vgl. NK8, S. 1, Z. 39-
            41).
     M1.3   initializing the second termination point based on the protocol
            initialization unit.

                                       - 34 -



Somit ist der NK8 zumindest das Merkmal M1.3 nicht zu entnehmen. Soweit die
Klägerin in der mündlichen Verhandlung vorgetragen hat, die NK8 stehe dem
Patentanspruch 1 neuheitsschädlich entgegen, da das Merkmal M1.3 durch „to
start“ aus der NK8, Ziffer 1) bekannt sei, kann der Senat darin noch nicht
unmittelbar das Initialisieren des zweiten Protokollendpunkts erkennen. Jedoch
entnimmt der Fachmann der NK8, dass die Übertragung des „Source RNC to
target RNC Transparent Field“ mit der Intention erfolgt, den target RNC zum neuen
serving RNC zu machen. An die Übertragung noch den Verfahrensschritt der
Initialisierung des target RNCs zum SNRC anzuschließen, ist dann aus
fachmännischer Sicht eine naheliegende Konsequenz.

Der Patentanspruch 1 unterscheidet sich teilweise auch im Merkmal M1.1 von der
NK8, insoweit als nach der NK8 ein transparentes Feld, das die gewünschte
Information enthalten soll, übermittelt wird. Dieses Feld wird jedoch beim
regelmäßig nötigen Übergang in eine tiefere Schicht des OSI-Modells ggf. mit
weiteren Daten in einer PDU dieser Schicht verkapselt. Da diese PDU mit dem
transparenten Feld ebenfalls der Initialisierung dient, ist sie als PIU im Sinne des
Anspruchs anzusehen.

Somit ist der Gegenstand des Patentanspruchs 1 nach Hauptantrag zwar neu
gegenüber NK8 (da M1.3 und M1.1 teilweise fehlen), jedoch beruht er nicht auf
einer erfinderischen Tätigkeit. Dies gilt in gleicher Weise für die das
Kommunikationssystem bzw. die entsprechenden Netzwerkelemente betreffenden
nebengeordneten Ansprüche 17, 23 und 27, die lediglich um ein Teil des
Merkmals M1.1 ergänzt wurden.

                                        - 35 -



                             III. Zu den Hilfsanträgen


1. Fassung nach Hilfsantrag 1 (Komplex Transparenz)

Das Verfahren des Hauptanspruchs gemäß Hilfsantrag 1 beruht nicht auf einer
erfinderischen Tätigkeit. Der Hilfsantrag 1 ist mangels Patentfähigkeit (Art. 56 EPÜ
i. V. m. mit Art. 54 Abs. 2 EPÜ) zur Selbstbeschränkung nicht geeignet.


Der Patentanspruch 1 in der Fassung nach Hilfsantrag 1 weist gegenüber der
erteilten Fassung zwischen den Merkmalen M1.2 und M1.3 zusätzlich das
folgende Merkmal auf (Unterstreichen hinzugefügt):


     M.Transp       „wherein the protocol initialization unit (20) is transparent
                    for the second protocol;“


Hinsichtlich der Zulässigkeit dieser Änderung hat der Senat keine Bedenken, denn
dieses Merkmal entspricht dem kennzeichnenden Merkmal des erteilten
Unteranspruchs 6.


Die Eigenschaft „transparent“ verwendet der Fachmann im Kontext mit Netzwerken und Nachrichten gemäß dem Bild (i. S. von Vorstellung) vom Glas, das für
Licht durchlässig ist, vgl. MN8 („Mouly“). Sie betrifft die Wechselwirkung zwischen
Protokollen, Nachrichten und Netzwerkkomponenten (i. S. von Geräten). Eine
Nachricht wird als transparent bezeichnet, wenn sie durch die Netzwerkkomponente hindurchgeleitet wird und dabei nicht gelesen und/oder verändert
wird. Im Bild von lichtdurchlässigem Glas ist strenggenommen die Netzwerkkomponente (bzw. das Gerät) transparent für das Protokoll oder die Nachricht, vgl.
MN8, S. 265. Die Parteien bezeichnen diesen Sachverhalt als „Netzwerktransparenz“. Eine Nachricht wird auch als transparent bezeichnet, wenn sie von
einem Protokoll unverändert und ungelesen transportiert wird. d. h. das Protokoll
kennt die Nachricht, die es transportiert, nicht. Dies ist grundsätzlich bei jedem
Protokoll der Fall, das nach dem OSI-Schichten-Modell in das nächst tiefere

                                        - 36 -



Protokoll verkapselt wird (siehe Ausführungen zum OSI-Modell unter Ziffer II.2.).
Diesen Sachverhalt bezeichnen die Parteien als „Protokoll-transparenz“.

Der   Fachmann      versteht    den   Satz   (vgl.   Streitpatentschrift [0037])   „The
encapsulation of protocol messages transparently to a message of another
protocol is a known technique and will thus not be discussed in more detail.“ im
Sinne der „Protokolltransparenz“. Der Senat hat keinen Zweifel daran, dass dieses
Verständnis zum Basiswissen des Fachmanns zählt. Der Fachmann entnimmt
dem Abs. [0015] ebenfalls, dass die PIU in der Nachricht eines zweiten Protokolls
verkapselt ist und transparent für das zweite Protokoll ist, was er im Sinne von
„Protokolltransparenz“ versteht.


Das Merkmal M.Transp versteht der Fachmann also dahingehend, dass die PIU
durch das zweite Protokoll nicht gelesen und verändert werden soll. Mit dem
Merkmal M1.2 und dem oben beschriebenen Verständnis des Fachmanns der PIU
(siehe Ziffer II.2.) als eine spezielle PDU lässt sich das Merkmal M.Transp nur als
ein Verkapseln der PIU in das zweite Protokoll verstehen.


Das Merkmal M.Transp spezifiziert nicht, welche PDU für welches Protokoll
transparent sein soll. Somit umfasst der Gegenstand des Patentanspruchs 1
gemäß Hilfsantrag 1 wortsinngemäß alle Protokollkombinationen, die an einem
Handover mit Relocation beteiligt sein können, insbesondere auch Protokolle
verschiedener OSI-Layer. Ein Verkapseln einer speziellen PDU in ein Protokoll der
nächst tieferen Schicht ist jedoch aus dem OSI-Schichtenmodell bekannt, siehe
Ziffer II.2. Dies betrifft rein fachmännisches Handeln und trägt nichts zur
erfinderischen Tätigkeit bei.
Da die weiteren nebengeordneten Ansprüche 16 und 22 ebenfalls lediglich um
M.Transp ergänzt wurden, ergeben sich bezüglich der Beurteilung der
Patentfähigkeit keine Unterschiede. In der Fassung nach Hilfsantrag 1 kann das
Streitpatent daher nicht aufrechterhalten werden.

                                       - 37 -



2. Fassung nach Hilfsantrag 2 (RRC-Protokoll)


Das Verfahren des Hauptanspruchs gemäß Hilfsantrag 2 beruht nicht auf einer
erfinderischen Tätigkeit. Der Hilfsantrag 2 ist mangels Patentfähigkeit (Art. 56 EPÜ
i. V. m. mit Art. 54 Abs. 2 EPÜ) zur Selbstbeschränkung nicht geeignet.

Der Patentanspruch 1 in der Fassung nach Hilfsantrag 2 weist gegenüber der
erteilten Fassung zusätzlich das Merkmal M.Transp (wie gemäß Hilfsantrag 1)
und zwischen den Merkmalen M1.1.1 und M1.2 zusätzlich folgendes Merkmal auf
(Unterstreichen hinzugefügt):


     M.RRC          „wherein the first protocol is a radio resource control
                    (RRC) protocol;“


An der Zulässigkeit dieser Änderung hat der Senat keine Zweifel, denn dieses
Merkmal ist dem Ausführungsbeispiel nach Abs. [0028] der Streitpatentschrift
sowie der Figur 3 entnommen.


Dem Fachmann ist klar, was unter einem RRC-Protokoll zu verstehen ist. Es
betrifft das Radio Resource Control Protokoll, das zwischen dem RNC und einer
Mobilstation (UE für „user equipment“ in UMTS) besteht. Den Merkmalen
M.Transp und M1.2 zusammen mit dem oben beschriebenen Verständnis der PIU
(siehe Ziffer II.2.) als eine spezielle PDU entnimmt der Fachmann, dass die RRC-PDU der Verbindung zwischen der betreffenden Mobilstation und dem Serving
RNC in ein anderes Protokoll verkapselt werden soll.


Somit umfasst der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2
wortsinngemäß alle Protokolle, die an einem Handover mit Relocation beteiligt
sein können, die ein RRC-Protokoll verkapseln, was insbesondere alle Protokolle
des darunter liegenden OSI-Layers 2 („data link layer“) betrifft. Da das RRC-Protokoll (ISO-OSI-Layer 3, „Network layer“) grundsätzlich in ein Protokoll des
Data Link Layers (ISO-OSI-Layer 2) verkapselt wird, vermittelt dieses Merkmal

                                       - 38 -



dem Fachmann keine neue Lehre. Vielmehr betrifft es rein fachmännisches
Handeln und trägt nichts zur erfinderischen Tätigkeit bei.
Die nebengeordneten Ansprüche 16 und 22 dieser Fassung, die um dieselben
Merkmale ergänzt sind, teilen das Schicksal des Anspruchs 1. Somit kann das
Streitpatent in der Fassung nach Hilfsantrag 2 keinen Bestand haben.

3. Fassung nach Hilfsantrag 3 (Avoid-Formulierung)


Das Verfahren des Hauptanspruchs gemäß Hilfsantrag 3 beruht nicht auf einer
erfinderischen Tätigkeit. Der Hilfsantrag 3 ist mangels Patentfähigkeit (Art. 56 EPÜ
i. V. m. mit Art. 54 Abs. 2 EPÜ) zur Selbstbeschränkung nicht geeignet.


Der Patentanspruch 1 in der Fassung nach Hilfsantrag 3 weist gegenüber der
erteilten Fassung zusätzlich die Merkmale M.Transp, M.RRC und nach dem
Merkmal M1.3 zusätzlich folgendes Merkmal auf (Unterstreichen hinzugefügt):


     M.Avoid        „so that a single protocol defines the information to be
                    transferred   thereby   avoiding   a     need   for   defining
                    parameters of one protocol in another protocol“.


Das Merkmal M.Avoid betrifft eine Zweckbestimmung, dahingehend, dass auf das
Definieren weiterer Parameter verzichtet werden kann. Es ist somit nicht geeignet,
den Gegenstand des Patentanspruchs zu beschränken. Daher gilt das zu
Hilfsantrag 2 Gesagte entsprechend. Die Parteien haben sich in der mündlichen
Verhandlung zum Hilfsantrag 3 im Übrigen nicht mehr geäußert.


Mit der Fassung nach Hilfsantrag 3 kann das Streitpatent daher nicht aufrechterhalten werden.

4. Fassung nach Hilfsantrag 4


In der Fassung nach Hilfsantrag 4 verteidigt die Beklagte das Streitpatent mit
Erfolg.

                                          - 39 -



Der Patentanspruch 1 in der Fassung nach Hilfsantrag 4 weist gegenüber der
erteilten Fassung zusätzlich die Merkmale M.Transp, M.RRC und nach dem
Merkmal M1.3 zusätzlich folgende durch „oder“ verknüpfte Merkmale auf
(Unterstreichen hinzugefügt):

     M.Iu            wherein
                     - the protocol initialization unit is transmitted via a third
                     network element between the termination points and the
                     transmission by the second protocol is based on a radio
                     access network application part (RANAP) protocol
                     or
     M.Iur           - the protocol initialization unit (20) is transmitted by a
                     direct connection between the termination points and the
                     transmission by the second protocol is based on a radio
                     network subsystem application part (RNSAP) protocol.


Mit Hilfsantrag 4 wird die erfindungsgemäße Lehre auf das Verkapseln einer PDU
des RRC-Protokolls als SDU eines RANAP (oder des RNSAP) Protokolls
beschränkt. Das RANAP-Protokoll und die Iu-Schnittstelle sind dem Fachmann
aus MN10 (einer jüngeren - aber noch vor dem Prioritätstag veröffentlichten –
Version (V1.0.2) der Spezifikation gemäß NK9 (V1.0.0)) bekannt. Das RNSAP-Protokoll und die Iur-Schnittstelle sind dem Fachmann aus MN4 bekannt. Sowohl
das RRC-Protokoll als auch das RANAP bzw. RNSAP-Protokoll sind Protokolle
des OSI-Layers 3. Das Verfahren nach Patentspruch 1 ist damit auf spezielle
Protokolle des Network-Layers beschränkt.

Zwar ist dem Fachmann bekannt, nach dem Schichtenmodell ein Protokoll in ein
anderes      Protokoll    der   nächst   tieferen   Schicht   zu   verkapseln.   Diese
Vorgehensweise wäre vom Fachmann auch dann zu erwarten, wenn beide
Protokolle nicht explizit aus dem Stand der Technik bekannt wären, solange sie
sich auf benachbarten OSI-Schichten (i. S. v. protocol stack) befinden. Zum
Verkapseln zweier Protokolle des Layers 3 ineinander, insbesondere der RRC-PDU in ein RANAP/RNSAP-Protokoll, wie dies mit den Merkmalen M.Iu und M.Iur

                                       - 40 -



erstmals beansprucht wird, kann nicht festgestellt werden, dass diese Maßnahme
zum Fachwissen des einschlägigen Fachmann gehört. Gegenteiliges hat die
Klägerin weder vorgetragen noch hat sie dies druckschriftlich belegt.
Weder die NK8 noch die NK9 initialisieren den neuen Protokollendpunkt
basierend auf der PIU (d. h. Merkmal M1.3 fehlt den Entgegenhaltungen). Der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 4 gilt daher als neu.


Weder die NK8 noch die NK9 zeigen eine PIU, die als eine RRC-PDU transparent
für ein RANAP oder RNSAP-Protokoll übertragen wird, d. h. die Merkmale M1.2,
M.Transp, M.RRC M.Iu und M.Iur fehlen in der Zusammenschau.


Auch der Vortrag der Klägerin zu den weiteren Druckschriften NK18 bis NK20
kann die Merkmale M1, M.Transp und M.RRC nicht nachweisen und deren
Naheliegen nicht plausibel machen.


Vielmehr erkennt der Senat die erfinderische Idee darin, dass die PDU des RRC-Protokolls als SDU in das RANAP-Protokoll (bzw. RNSAP) transparent
aufgenommen wird und diese zum Initialisieren des neuen Protokollendpunktes
der RRC Verbindung verwendet wird, obwohl beide Protokolle auf derselben OSI-Schicht (Layer 3) angeordnet sind.


Der Fachmann, der mit der Aufgabe betraut war, die Zahl der Parameter bei der
Verlagerung eines RRC Protokollendpunktes von einem serving RNC zu einem
anderen serving RNC zu reduzieren, musste von dem langjährig bekanntem GSM-Standard (vgl. MN9) mit „external handover“ (siehe auch Ziffer I.2) ausgehen, bei
dem die Mobilfunkverbindung von einem BSC zu einem anderen BSC übergeben
wird, der in der Struktur dem Relocation der Mobilfunkverbindung von einem RNC
zu einem anderen RNC ähnlich ist.
Der Fachmann würde demgemäß relevante Parameter der RRC-Verbindung
festlegen, die am neuen RNC benötigt werden und diese in einem Protokoll
(RANAP) als IE („information element“) definieren und dazu informationstragende
Felder geeignet zusammenfassen. Diese Vorgehensweise hat auch WG3 gewählt,

                                        - 41 -



was sich anhand der zeitlichen Abfolge der Dokumente NK9 (April 1999), MN10
(Juni 1999) und NK8 (August 1999) erkennen lässt. Die NK9 sieht das „UTRAN
information field“ vor, das wohl (noch unspezifische) Informationen über die
UTRAN-UE-Verbindung enthalten soll und transparent für das Kernnetz zum
neuen RNC übertragen werden soll. Die Version V1.0.2 desselben Standards
TS 25.413 (MN10) konkretisiert dies zu einem „Source RNC to target RNC
transparent field“, das mit „RELOCATION REQUIRED“ und „RELOCATION
REQUEST“ transparent über das Kernnetz (RANSP) an den neuen RNC
übertragen werden soll, vgl. MN10, Abs. 8.1 („Relocation“), Abs. 9.1.1.16, und
9.1.1.17. Mit der NK8 geht die WG3 zum einen davon aus, dass die RANAP-Prozeduren für das Relocation ähnlich der bekannten GSM A-Schnittstelle
BSSMAP (d. h. Protokoll zwischen BSC und MSC)             beim externen Handover
benutzt werden (vgl. NK8, 1. Abs.) und stellt zum anderen Fragen an die WG2,
welche Informationen für ein Relocation im „Source RNC to target RNC
transparent field“ benötigt werden. Dies bedeutet nach Überzeugung des Senats,
dass konkrete Felder für die zu übertragende Information in RANAP spezifiziert
werden sollen und eine Verkapselung nicht vorgesehen ist.
Der Fachmann hatte nach Überzeugung des Senats keine Veranlassung, die
Vorgehensweise der WG3 zu verlassen und statt konkreter Parameter, die RRC-PDU transparent in das RANAP-Protokoll einzufügen (Merkmale M.Transp,
M.RRC, M.Iu). Er musste bei dem Gegenstand des Patentanspruchs 1 nach
Hilfsantrag 4   damit   auch   die   übliche     Vorgehensweise   nach   dem   OSI-Schichtenmodell verlassen.

Zu den Entgegenhaltungen im Einzelnen


4.1 Zur NK8 gelten die Ausführungen unter Ziffer I.3 zum Hauptantrag. Im
Zusammenhang mit Hilfsantrag 4 ist das Verständnis des „Source RNC to Target
RNC transparent Field“ der NK8 bedeutend. Unstrittig ist, dass das „Source RNC
to Target RNC transparent Field“ mittels RANAP-Protokoll über die Iu-Schnittstelle
an den neuen SRNC übertragen wird, vgl. NK8, S. 1, Ziffer 1).
Mit der NK8 stellt die WG3, die sich mit Spezifikationen des Network-Layers (OSI-Layer 3) befasst, an die WG2, die sich mit Spezifikationen des darunter liegenden

                                        - 42 -



Data-Link-Layers (OSI-Layer 2) befasst, die durch die Phrase „3GPP RAN WG2“
eingeleiteten Fragen, vgl. NK8, S. 2.

In der mündlichen Verhandlung haben die Parteien gegensätzliche Auffassungen
über die von der WG3 an die WG2 gestellte Frage (vgl. NK8, S. 2, Ziffer 3))


        „3) 3GPP RAN WG2: What and how much information is
        required to be transmitted from source RNC to target RNC in
        the ‘Source RNC to Target RNC transparent Field‘ in case of
        intra UMTS relocation in order to enable the target RNC to start
        as a Serving RNC?“


vorgetragen. Die Klägerin entnimmt der NK8, dass das „Source RNC to Target
RNC transparent Field“ protokolltransparent sei, also im RANAP-Protokoll
verkapselt sei. Die Beklagte entnimmt der NK8, dass das „Source RNC to Target
RNC transparent Field“ netzwerktransparent sei, also mit der NK8 keine
Verkapselung offenbart sei.


Der Senat entnimmt der Fragestellung, dass die WG3 genaue Angaben über die
an den neuen RNC zu übertragenden Informationen benötigt, um das „Source
RNC to Target RNC transparent Field“ festzulegen. Damit ist das RANAP-Protokoll, das u. a. das „Source RNC to Target RNC transparent Field“ übertragen
soll, von der Definition dieses Feldes abhängig und muss bei jeder Änderung des
Feldes ebenfalls geändert werden. Das „Source RNC to Target RNC transparent
Field“ stellt somit keine RRC-PDU dar, die transparent für das RANAP-Protokoll
ist. Der NK8 ist folglich über das unter Ziffer I.3 bereits Ausgeführte hinaus auch
noch die Merkmalskombination M.Transp, M.RRC nicht zu entnehmen.


4.2 Die NK9 betrifft die Spezifikation (TS 25.413) des RANAP-Protokolls in der
Version 1.0.0. vom April 1999. Das Kapitel 8 der NK9 spezifiziert mehrere
RANAP-Prozeduren, von denen nur die Prozedur „Serving RNS relocation“ gemäß
Abschnitt 8.1 Bezug zum Anspruchsgegenstand des Streitpatents hat. Das
Kapitel 9 der NK9 beschreibt Informationselemente (IE), die für die RANAP-

                                        - 43 -



Kommunikation verwendet werden. Für das Starten der Verlagerung (Relocation)
sind die beiden Informationselemente RELOCATION REQUIRED (vgl. NK9,
Abschn. 9.1.1.19) und RELOCATION REQUEST (vgl. NK9, Abschn. 9.1.1.20)
relevant.


Im Einzelnen entnimmt der Fachmann der NK9, dass


   -   die Funktionalität für eine bestimmte RRC Verbindung (d. h. eine
       Verbindung zwischen einer Mobilstation und einem ersten serving RNC)
       von einem ersten serving RNS (= Radio Network Subsystem, was gemäß
       Fachwissen einen serving RNC aufweist) zu einem anderen RNS verlagert
       („is relocated“) werden soll (vgl. NK9, S. 8, 1. Abs.), was dem Merkmal M1
       entspricht,
   -   die Verlagerung der NK9 eine RRC-Verbindung betrifft, was dem Merkmal
       M.RRC teilweise entspricht,
   -   die Verlagerung mittels RANAP-Protokoll gesteuert wird (vgl. NK9, S. 8,
       2. Abs.), was dem Merkmal M1.2 teilweise und dem Merkmal M.Iu teilweise
       entspricht,
   -   der target RNC initialisiert wird (vgl. NK9, Fig. 1, „SRNS operation start“ auf
       der Zeitlinie des target RNS), was dem Merkmal M1.3 teilweise entspricht.

Sofern die Klägerin das „UTRAN information field“ (vgl. NK9, Abschn. 8.1, 2. Abs.)
als äquivalent zur PIU versteht, kann der Senat dies nach den mündlichen
Vorträgen der Parteien zur PIU nicht nachvollziehen. Zum einen wird das „UTRAN
information field“ der NK9 mit der RELOCATION REQUIRED Nachricht nach dem
RANAP-Protokoll am Kernnetz (CN) nicht gelesen, sondern wird in das „UTRAN
information field“ der RELOCATION REQUEST Nachricht durchgeleitet, also
„netzwerktransparent“, vgl. NK9, 2. Absatz (dort: „transparent to the core network“)
i. V. m NK9, 3. Absatz und Fig. 1. Zum anderen ist der NK9 nicht entnehmbar,
dass das „UTRAN information field“ aus einer RRC-Protokoll-PDU erzeugt würde.
Der NK9 fehlen insofern die Merkmale M1.1, M.Transp und M.RRC teilweise.
Soweit die Klägerin vorgetragen hat, für den Fachmann sei klar, mittels des
„UTRAN information field“ der NK9 würde am neuen RNC eine RRC-Verbindung

                                      - 44 -



initialisiert, kann der Senat dieser Auffassung nur teilweise folgen. Zwar geht aus
NK9, Fig. 1 und NK9, S. 8, vorletzter Absatz hervor, dass eine Initialisierung des
neuen RNS (mit RNC) erfolgt, jedoch kann der Senat nicht nachvollziehen, dass
dies zwingend und eindeutig durch das „UTRAN information field“ erfolgen soll.
Insofern fehlt der NK9 auch das Merkmal M1.3 teilweise.


4.3 Es kann dahingestellt bleiben, ob die NK18 mit den zum Verständnis
notwendigen Dokumenten NK19 und NK20, als Stand der Technik gilt - was die
Beklagte bestreitet –, da die NK18 nach Überzeugung des Senats die
Patentfähigkeit des Streitpatents in der Fassung nach Hilfsantrag 4 nicht in Frage
stellt. (Zur leichteren Nachvollziehbarkeit in Hinblick auf den enormen Umfang und
die mehrdeutigen Seitennummern der NK18, NK19 und NK20 wird im Folgenden
zusätzlich die Seitenzahl der von der Klägerin eingereichten elektronischen
Fassung als PDF-Seite angegeben).


Die Klägerin hat in der mündlichen Verhandlung vorgetragen, die NK18 nehme
den Patentanspruch 1 gemäß Hilfsantrag 4 neuheitsschädlich vorweg. Sie hat
dazu ausgeführt, die NK18 zeige einen Handoff (~Handover) zwischen einer
source Basisstation („source BS“) und einer target Basisstation („target BS“), was
dem Relocation eines Protokollendpunktes gemäß Streitpatent entspreche (vgl.
NK18, Teil-200 B, S. 21, Abschnitt 3.5.2.1.1, Fig. 3-1 ~ PDF-S. 337), wobei mit
diesem ein „Service Configuration Record“ (NK18, Teil-400 B, S. 278, Abschnitt
6.2.2.109 ~ PDF-S. 748) entsprechend der „protocol initialization unit“ PIU gemäß
Streitpatent übertragen werde. Die Definition des „Service Configuration Record“
sei wie in der NK19 (vgl. NK19, TSB74, Abschn. 7.7.5.7, S. 7-151 ~ NK19, PDF-S. 357) und NK20 (vgl. NK20, Abs. 3.7.5.7, S. 3-268 ~ NK20, PDF-S. 679)
angegeben zu verstehen (vgl. Verweis in der NK18, Teil 400 B, S. 278,
Abschnitt 6.2.2.109, Zeilen 6-7 ~ NK18, PDF-S. 748). Das „Service Configuration
Record“ sei unabhängig von den Protokollen der NK18 in der NK19 definiert und
bilde somit einen transparenten Container mit RRC-Protokoll. Das RNSAP-Protokoll gemäß Merkmal M.Iur entspreche dem A7-Inferface der NK18, bei dem
Signalisierungsinformation von der „source BS“ (base station) zur „target BS“

                                     - 45 -



übertragen werde (vgl. NK18, Teil 000-B, S. 18, Abschn. 1.7.2, Z. 40-41 ~ NK18,
PDF-S. 47 und vgl. NK18, Teil 100-B, S. 152, Abschn. 3.4.3.1.1, ~ NK18, PDF-S. 213). Das RANAP-Protokoll gemäß Merkmal M.Iu entspreche dem A1-Inferface
der NK18, bei dem Signalisierungsinformation zwischen MSC und BS übertragen
werde, vgl. NK18, Teil 000-B, S. 18, Abschn. 1.7.2, Z. 15-16 ~ NK18, PDF-S. 47.
Die Klägerin hat vorgetragen, der Gegenstand des Patentanspruchs 1 sei dem
Fachmann auch nahegelegt, dies jedoch nicht näher begründet.


Die Beklagte hat dem widersprechend vorgetragen, die NK18 betreffe die
Kommunikation zwischen dem Kernnetz und einer Basisstation (vgl. NK18, Titel:
„MC-BS Interface“) und die NK20 betreffe die Kommunikation zwischen User
Equipment und Basisstation. Gemäß NK18 werde ein Hard Handoff spezifiziert
(vgl. NK18, Teil-200 B, S. 21, Abschnittsüberschrift 3.5.2.1 f. ~ NK18, PDF-S. 337), ein Relocation eines Protokollendpunktes gemäß Merkmal M1 fehle der
NK18. Das „Service Configuration Record“ werde für das TDMA gar nicht und für
CDMA nur optional verwendet. Für eine Initialisierung gemäß Merkmal M1.3
könne das „Service Configuration Record“ der NK18 daher nicht vorgesehen sein.
Das „Service Configuration Record“ könne nicht der PIU gemäß Merkmal
M.Transp entsprechen, da gemäß NK18 (vgl. NK18, Teil 200 B, S. 8, Ziff. c ~
NK18, PDF-S. 324) eine Modifikation des „Service Configuration Record“ durch
die MSC erfolge.


Der Vortrag der Klägerin ist mit den genannten Textstellen nicht geeignet, die
Merkmale M1 (Relocation), M.Transp (Protokolltransparenz der PIU), M.RRC
(PIU = RRC-PDU) und M1.3 (Initialisieren des neuen Protokollendpunkts) einzeln
oder in ihrer Gesamtheit des Anspruchswortlauts aus der NK18 (auch in
Zusammenschau mit NK19 und NK20) als bekannt zu belegen. Der Senat ist
überzeugt, dass die von der Klägerin zitierte Textstelle (vgl. NK18, Teil-200 B,
S. 21, Abschnitt 3.5.2.1.1, Fig. 3-1 ~ PDF-S. 337) einen Hard Handoff und kein
Relocation betrifft. Eine Kommunikation zwischen Mobilstation und RNC bzw. BSC
ist in den von der Klägerin genannten Textstellen der NK18 nicht angesprochen,
vielmehr betrifft die NK18 das Interface zwischen MSC und Basisstation (vgl.

                                       - 46 -



NK18 Titel). Die von der Klägerin zitierte Textstelle der NK19 (vgl. NK19, TSB74,
Abschn. 7.7.5.7, S. 7-151 ~ NK19, PDF-S. 357) besagt, dass ein „Service
Configuration Record“ in einer Service Request Message oder einer Service
Response Message enthalten sein soll. Eine PIU bzw. eine RRC-PDU kann der
Senat darin nicht erkennen. Hinsichtlich der Merkmale M1.3 und M.Transp folgt
der Senat dem Vortrag der Beklagten.


4.4 Zu den weiteren von ihr genannten Druckschriften NK7, NK10 bis NK14 hat
die Klägerin nicht substantiiert vorgetragen, wie diese für sich oder in
Zusammenschau       mit   anderen     Druckschriften    der     Patentfähigkeit   des
Patentanspruchs 1 gemäß Hilfsantrag 4 entgegenstehen könnten. Der Senat hat
keine Veranlassung dazu von Amts wegen zu ermitteln, vgl. BGH, Urteil vom
27. August 2013       – X ZR 19/12,        Tretkurbeleinheit;        Urteil       vom
2. Dezember 2014 - X ZR 151/12, Zwangsmischer, insb. Leitsatz a)).

4.5 Zu den nebengeordneten Patentansprüchen 12 und 18


Die nebengeordneten Patentansprüche gemäß Hilfsantrag 4 wurden analog zum
Patentanspruch 1 beschränkt. Sie weisen gegenüber der mit Hauptantrag
verteidigten Fassung zusätzlich die Merkmale M.Transp, M.RRC, M.Iu und M.Iur
auf. Die Ausführungen zum Hauptanspruch 1 gemäß Hilfsantrag 4 gelten für das
Kommunikationssystem nach Patentanspruch 12 und das Netzwerkelement nach
Patentanspruch 18 entsprechend, denn diese Gegenstände erschöpfen sich in
einer Umsetzung des Verfahrens im entsprechenden Kommunikationssystem und
einem demgemäß hergerichteten Kommunikationselement.
Mit den unabhängigen Patentansprüchen 1, 12 und 18 haben auch die auf diese
rückbezogenen Unteransprüche 2 bis 11, 13 bis 17 und 19 bis 21 Bestand, die
jeweils   vorteilhaften Weiterbildungen    des   sie   tragenden    Patentanspruchs
beschreiben.
Der Senat hat das von der Beklagten in Kopie (MN5) eingereichte Urteil des High
Court of Justice (Aktenzeichen HC-2012-000076) bei seiner Entscheidung
berücksichtigt und kommt in der Sache zum gleichen Ergebnis. Im Lichte der
Beschreibung versteht der High Court of Justice das erste (vgl. MN5, feature (b)

                                               - 47 -



Abs. 80) und das zweite Protokoll (vgl. MN5, feature (c) Abs. 81) wohl als RRC
bzw.    RANAP      Protokoll    und     legt    offensichtlich    dieses     Verständnis    dem
Patentanspruch zugrunde, vgl. MN5, Abs. 77-81. Nach der Rechtsprechung in der
Bundesrepublik Deutschland ist eine Auslegung unterhalb des Wortlauts (im Sinn
einer Auslegung unterhalb des Sinngehalts) der erteilten Patentansprüche jedoch
nicht   zulässig    (vgl.    BGH,       Urt.    v.      12. Dezember 2006         – X ZR 131/02,
„Schussfädentransport“, insb. Leitsatz a).




                                                IV.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO.
Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und Satz 2 ZPO.




                                 Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland
zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der
Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt
unterzeichnet      und      innerhalb     eines         Monats    beim       Bundesgerichtshof,
Herrenstraße 45a, 76133 Karlsruhe eingereicht werden.
Sie kann auch als elektronisches Dokument eingereicht werden (§ 125a Absatz 2
des Patentgesetzes in Verbindung mit der Verordnung über den elektronischen
Rechtsverkehr        beim        Bundesgerichtshof               und       Bundespatentgericht
(BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130). In diesem Fall muss
die Einreichung durch die Übertragung des elektronischen Dokuments in die
elektronische   Poststelle     des      Bundesgerichtshofes            erfolgen   (§ 2   Absatz 2
BGH/BPatGERVV).

                                      - 48 -



Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der
Verkündung. Die Frist ist nur gewahrt, wenn die Berufung vor Fristablauf beim
Bundesgerichtshof eingeht. Die Frist kann nicht verlängert werden.


Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung
gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung
eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Martens         Bayer            Dr. Scholz         J. Müller          Bieringer

                                                                              Bb
