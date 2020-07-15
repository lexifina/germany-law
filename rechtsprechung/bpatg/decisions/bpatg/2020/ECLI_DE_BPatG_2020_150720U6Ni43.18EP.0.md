---
ecli: "ECLI:DE:BPatG:2020:150720U6Ni43.18EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 43/18"
decided: "2020-07-15"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=24&nr=39969&anz=666&pos=373&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2020-07-15_6_Ni_43_18_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 43/18 vom 2020-07-15

## Entscheidung

BUNDESPATENTGERICHT

                               IM NAMEN DES VOLKES
 6 Ni 43/18 (EP)
     verbunden mit                        URTEIL
 6 Ni 44/18 (EP)                                                           Verkündet am
     verbunden mit                                                         15. Juli 2020
 6 Ni 52/18 (EP)                                                                …
_______________________

  (Aktenzeichen)


                               In der Patentnichtigkeitssache

 …


                       betreffend das europäische Patent 1 173 986
                                     (DE 600 06 514)


 hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts am 15. Juli 2020
 durch die Vorsitzende Richterin Friehe, die Richterin Werner sowie die Richter Dipl.-
 Phys. Dr. Schwengelbeck, Dipl.-Ing. Altvater und Dr.-Ing. Flaschke,


 für Recht erkannt:


        I.
        Das europäische Patent 1 173 986 wird mit Wirkung für das Hoheitsgebiet
        der Bundesrepublik Deutschland teilweise für nichtig erklärt, soweit es über
        folgende Fassung hinausgeht:

             „1. A method for transferring packet data in the uplink direction from a
                 mobile station to a system in such a manner that

                 ‐ a common channel (RACH) or a dedicated channel (DCH) is
                     selected for the sending of a data packet, and




 ECLI:DE:BPatG:2020:150720U6Ni43.18EP.0

                                  -2-


    ‐ the data packet is sent using the channel selected,

    characterized in that

    ‐ a threshold value of a channel selection parameter is defined (620),

    ‐ said threshold value of the channel selection parameter is sent to
      the mobile station (630),

    ‐ a current value of the channel selection parameter is compared
      to said threshold value of the channel selection parameter by
      the mobile station (650), and

    ‐ said selection is performed on the basis of said comparison (660).


2. A method according to claim 1, characterised in that said current value
    corresponding to the channel selection parameter is calculated at the
    mobile station on the basis of the parameters of the data packet to be
    transferred.


3. A method according to any one of claims 1 to 2, characterized in that if
    the channel selected for the data packet transfer is a dedicated channel
    (DCH), a channel (DCH) is allocated after the selection, whereafter the
    data packet is transferred on the allocated channel (DCH).


4. A method according to any one of claims 1 to 3, characterized in that
    said channel selection parameter value is sent on a common channel.


5. A method according to claim 4, characterized in that the channel selection
    parameter value is sent on one of the following common channels: BCH,
    FACH, PCH.


6. A method according to any one of claims 1 to 2, characterized in that
    said channel selection parameter value is sent on a DCH.

                                 -3-


7. A method according to any one of the preceding claims, characterized in
    that one or more of the following parameters are used in the channel
    selection:

     ‐ size of data packet,

     ‐ maximum allowed data packet size on the RACH,

     ‐ bit rate required,

     ‐ allowed transfer delay,

     ‐ priority of data to be transferred,

     ‐ load on the transfer channel, and

     ‐ transmit power level required on the RACH.


8. A method according to claim 7, characterized in that the size of data
    packet is determined on the basis of amount of data in RLC buffers.


9. A method according to any one of the preceding claims, characterized in
    that, the channel selection parameter value sent to the mobile station is
    one or several of the following:

     ‐ maximum allowed data packet size on the RACH,

     ‐ load on the transfer channel, and

     ‐ maximum allowed power level on the RACH.


10. A method according to claim 8, characterized in that the channel
    selection parameter value sent to the mobile station is a threshold
    value for the data in the RLC buffer(s).


11. A method according to any one of the preceding claims, characterized
    in that the channel selection parameters are defined so as to concern
    all mobile stations in the area in which the parameters are sent.

                                 -4-


12. A method according to any one of claims 1 to 10, characterized in
      that the channel selection parameters are defined so as to concern a
      subset of all mobile stations in the area in which the parameters are
      sent.


13. A method according to any one of claims 1 to 10, characterized in that
      the channel selection parameters are defined so as to concern a single
      mobile station.


14.


15. A mobile station connected with a cellular system, comprising

      means for sending uplink packet data to the system using a selected
      channel, wherein the selected channel is either a common channel (RACH) or a dedicated channel (DCH),

      characterized in that

      it also comprises

       ‐ means for receiving a threshold value of a channel selection
          parameter from the system,

       ‐ means for storing said threshold value of the channel selection
          parameter,

       ‐ means for comparing said threshold value of the channel selection
          parameter to a current value of the channel selection parameter
          for basis of said channel selection, and

       ‐ means for making said channel selection on the basis of the result
          of said comparison.


16.


17. A mobile station according to claim 15, characterized in that it comprises

                                          -5-


        ‐ means for calculating a value corresponding to the channel selection
             parameter on the basis of the parameters of the data packet to be
             sent,
        ‐ means for comparing a current value of the last channel selection
             parameter sent to the mobile station to said calculated value of the
             channel selection parameter, and
        ‐ means for making said channel selection on the basis of said comparison.


       18. A mobile station according to claim 17, characterized in that said value
             corresponding to the channel selection parameter is the amount of
             data in the radio link control (RLC) buffer(s) said last current value of
             the last channel selection parameter is a threshold value for the
             amount of data in the radio link control (RLC) buffer(s).


       19. The use of the method of any one of claims 1 to 13 in a UMTS system.


       20.


       21. The use of the mobile station of any one of claims 15 to 18 in a UMTS
             system.“



II.
Im Übrigen werden die Klagen abgewiesen.



III.
Die Kosten des Rechtsstreits werden wie folgt verteilt:

        Die Gerichtskosten tragen die Beklagte zu 1/3 und die Klägerinnen gesamtschuldnerisch zu 2/3.

        Die außergerichtlichen Kosten der Klägerinnen trägt die Beklagte jeweils zu 1/3 und die außergerichtlichen Kosten der
        Beklagten tragen die Klägerinnen jeweils zu 2/9.

                                         -6-


           Im Übrigen tragen die Parteien ihre Kosten jeweils selbst.


     IV.
     Das Urteil ist gegen Sicherheitsleistung in Höhe von 110% des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.




                                  Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 1 173 986 (Streitpatent), das
auf die internationale Anmeldung PCT/FI00/00137 vom 22. Februar 2000 zurückgeht. Das Streitpatent nimmt die Priorität aus der Anmeldung FI 990384 vom 23.
Februar 1999 in Anspruch. Die Anmeldung ist als WO 00/051245 A2 veröffentlicht
worden.


Das Streitpatent ist in Kraft und wird beim Deutschen Patent- und Markenamt unter
dem Aktenzeichen 600 06 514 geführt. Es trägt die Bezeichnung

      „Method and Arrangement for Managing Packet Data Transfer in a
                                 Cellular System“
                       (auf Deutsch laut Streitpatentschrift:
       „Verfahren und Vorrichtung zur Verwaltung von Paketübertragung
                             in einem Zellularsystem“)

und umfasst in der erteilten Fassung einundzwanzig Patentansprüche, die mit den
drei Nichtigkeitsklagen, die eingereicht wurden am 2. November 2018 [6 Ni 43/18
(EP)], am 5. November 2018 [6 Ni 44/18 (EP)] und am 12. Dezember 2018 [6 Ni
52/18 (EP)], jeweils in vollem Umfang angegriffen werden.


Die angegriffenen erteilten nebengeordneten Patentansprüche 1, 14, 15, 19, 20 und
21 lauten:

                            -7-


in der Verfahrenssprache:    auf Deutsch laut Streitpatentschrift EP 1
                             173 986 B1

                                        -8-




Die ebenfalls angegriffenen Patentansprüche 2 bis 13 und 16 bis 18 sind auf diese
Patentansprüche unmittelbar oder mittelbar rückbezogen.


Die Klägerinnen zu 1) bis 3) sind der Ansicht, dass das Streitpatent wegen des
Nichtigkeitsgrunds der mangelnden Patentfähigkeit, nämlich mangelnder Neuheit
und mangelnder erfinderischer Tätigkeit, für nichtig zu erklären sei. Die Klägerinnen
zu 1) und 2) sind darüber hinaus der Auffassung, dass das Streitpatent auch wegen
der Nichtigkeitsgründe der mangelnden Ausführbarkeit bzw. Offenbarung sowie der
unzulässigen Erweiterung für nichtig zu erklären sei. Den Einwand der fehlenden
Patentfähigkeit stützen die Klägerinnen auf die Druckschriften (Nummerierung und
Kurzzeichen nach Klageverfahren, wobei im Weiteren die an der Kurzbezeichnung
hochgestellte Ziffer auf die Verwendung durch die jeweilige Klägerin hinweist):

                                            -9-


6 Ni 43/18   6 Ni 44/18 6 Ni 52/18   Bezeichnung

NK7                     D4           US 5,673,259
                        D4a          Eingabe der Beklagten im Anmeldeverfahren zum
                                     Streitpatent vom 27. Januar 2003
             NK4        D3           WO 99/66748 A1
NK8                                  Veröffentlichung Christiaan Roobol et al., „A proposal
                                     for an RLC/MAC Protocol for Wideband CDMA Capable of Handling Real Time and Non Real Time Services", VTC '98, Seiten 107 bis 111
NK9                                  Masterarbeit (Master's Thesis) …
                        D5           Technische Spezifikation 3G TS 25.321, V3.2.0
                                     (1999-12)
                        D6           Technische Spezifikation 3G TS 25.303 V3.2.0 (1999-
                                     12)
             NK1                     ETSI TS 125.331 V3.1.0 (2000-01), "RRC Protocol
                                     Specification"
                        D1           Technische Spezifikation 3G TS 25.331 V3.1.0 (2000-
                                     01)
                        D1a          Sitzungsbericht …
             NK2                     Association of Radio Industries and Businesses
                                     (ARIB), MAC Sublayer Specification for 3G Mobile
                                     System (Ver.1.0), veröffentlicht als 3GPP Tdoc TSG-RAN WG2 09/99 auf dem RAN WG2 Meeting #1, 20 -
                                     22 Januar 1999, Helsinki, Finnland
             NK3                     Telecommunication Technology Committee (TTC),
                                     Association of Radio Industries and Businesses
                                     (ARIB), UE-UTRAN L3 RRC Signaling Protocol, Vol 9,
                                     Ver. 1.0.0, January 18.1999, veröffentlicht als 3GPP
                                     Tdoc TSG-RAN WG2 10/99 auf dem RAN WG2 Meeting #1, 20 - 22 Januar 1999, Helsinki, Finnland
             NK3a                    3GPP Working group …
                        D2           Technische Spezifikation UMTS YY.03, V0.5.0 1999-
                                     1
                        D2a          Tdoc RAN WG2 052/99, Sitzungsbericht …
                        D7           Tdoc SMG2 UMTS-L23 477/98 …
                        D7a          UMTS-Spezifikation XX.03, Version 0.1.0 (September
                                     1998)
                        D7b          UMTS-Spezifikation XX.05, Version 0.1.0 (September
                                     1998)
                        D7c          Tdoc SMG2 UMTS-L23 002/99, …
                        D7d          Tdoc SMG2 UMTS-L23 582/98, …
                        D7e          Tdoc SMG2 UMTS-L23 480/98, …
                        D7f          Tdoc SMG2 UMTS-L1 596/98, …
                        D8           Tdoc SMG2 UMTS-L23 427/98, …




Die Klägerinnen beantragen,

                                     - 10 -


      das europäische Patent 1 173 986 mit Wirkung für das Hoheitsgebiet der
      Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,

      die Klage abzuweisen,

      hilfsweise Teilabweisung der Klage nach Maßgabe der Hilfsanträge im
      Schriftsatz vom 06.07.2020, wobei in den Anträgen A.2 und B.2 der Patentanspruch 20 ebenfalls gestrichen wird.


Die Ansprüche nach dem in der Verfahrenssprache eingereichten Hilfsantrag A.1
lauten wie folgt (Änderungen gegenüber der erteilten Fassung sind jeweils gekennzeichnet):

- 11 -

- 12 -

- 13 -

                                       - 14 -


Wegen des Wortlauts der Ansprüche nach Hilfsantrag A.2 wird auf den Urteilstenor
und wegen des Wortlauts der Ansprüche nach den Hilfsanträgen B.1 und B.2 wird
auf die Akte verwiesen.


Die Beklagte tritt der Argumentation der Klägerinnen entgegen und hält den Gegenstand des Streitpatents in der erteilten Fassung, wenigstens in der verteidigten Fassung, für schutzfähig.



Der Senat hat den Parteien einen qualifizierten Hinweis vom 16. April 2020 zugeleitet und hierin Fristen zur Stellungnahme auf den Hinweis und auf etwaiges Vorbringen der jeweiligen Gegenpartei gesetzt.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                          Entscheidungsgründe


                                          A.


Die Klagen sind zulässig, haben in der Sache aber nur teilweise Erfolg, und zwar
hinsichtlich der erteilten Fassung und der verteidigten Fassung nach Hilfsantrag
A.1. Denn insoweit steht, ungeachtet der Frage, ob auch die weiteren geltend gemachten Nichtigkeitsgründe bestehen, jedenfalls der Nichtigkeitsgrund der unzulässigen Erweiterung entgegen gemäß Artikel II § 6 Abs.1 Nr.3 IntPatÜG, Artikel 138
Abs.1 Buchst.c) EPÜ i. V. m. Art. 52, 56 EPÜ.


In der ebenfalls verteidigten Fassung nach Hilfsantrag A.2 erweist sich das Streitpatent dagegen insgesamt als schutzfähig, so dass die Klagen, soweit sie sich auch
gegen diese Fassung richten, teilweise abzuweisen sind. Auf die weitere Frage, ob

                                      - 15 -


das Streitpatent auch in der Fassung nach Hilfsanträgen B.1 und B.2 Bestand hätte,
kam es bei dieser Sachlage nicht mehr an.




                     I. Zum Gegenstand des Streitpatents


1. Das Streitpatent betrifft gemäß Beschreibungseinleitung ein Verfahren und eine
   Anordnung für das Management der Übertragung von Paketdaten in einem Zellenfunksystem (cellular system). Die Erfindung werde vorteilhaft in einem auf
   WCDMA (Wideband Code Division Multiple Access) gestützten Mobilkommunikationssystem verwendet, wie beispielsweise dem UMTS (Universal Mobile Telecommunications System), das die Betriebsarten TDD (Time Division Duplex)
   und FDD (Frequency Division Duplex) verwende (vgl. Streitpatentschrift, Abs. 1
   bzw. entsprechende deutsche Übersetzung gemäß DE 600 06 514 T2).


   Das Problem bei der Paketdatenübertragung auf einer Aufwärtsstrecke (uplink
   packet data transfer) sei, dass das System keine Informationen über die zu sendenden Pakete besitze, um auf diese ihre Kanalauswahlentscheidung zu stützen. Folglich würden die Informationen über die zu übertragenden Datenpakete
   zum System gesendet werden müssen, woraufhin das System die Informationen über die Entscheidung über die Verwendung eines gemeinsamen oder eines zweckgebundenen Kanals zur Mobilstation senden müsse. Diese Informationsübertragung beanspruche Kapazität (trafﬁc capacity) und verlangsame die
   Übertragung der Paketdaten (vgl. Streitpatentschrift, Abs. 21 und deutsche
   Übersetzung).


   Im Stand der Technik gemäß US 5 673 259 A (NK71 / D43) werde ein digitales
   Kommunikationssystem mit einer Vorwärts-/Aufwärtsstrecke (uplink) und einer
   Rückwärtsstrecke zur Übertragung eines Datenpakets beschrieben. Das System umfasse einen Sender/Empfänger für das Senden des Datenpakets in einem Direktzugriffskanal über die Rückwärtsstrecke. Dieses System könne einen zweckgebundenen Kanal für die Übertragung des Datenpakets zwischen

                                       - 16 -


   dem Sender/Empfänger und der Basisstation enthalten sowie einen Prozessor
   für das Umschalten vom Direktzugriffskanal zum zweckgebundenen Kanal,
   wenn der Bandbreitenbedarf eine erste Schwelle überschreite, und für das Umschalten vom zweckgebundenen Kanal zum Direktzugriffskanal, wenn der
   Bandbreitenbedarf unter eine zweite Schwelle falle (vgl. Streitpatentschrift, Abs.
   22 sowie deutsche Übersetzung).


2. Entsprechend den Angaben in der Beschreibungseinleitung des Streitpatents
   ist die Aufgabe darin zu sehen, eine Lösung für das Management der Aufwärtsstrecken-Paketdaten zu schaffen, die die zuvor erwähnten Probleme vermeide.
   Dementsprechend ist die dem Streitpatent zugrundeliegende technische Problemstellung darin zu sehen, das Beanspruchen bzw. Aufbrauchen von Kapazität
   (trafﬁc capacity) durch die (zusätzliche) Informationsübertragung und die damit
   verbundene Verlangsamung der Übertragung von Datenpaketen von einer Mobilstation zu einem zellularen System bzw. Mobilfunknetz in der sogenannten
   Aufwärtsstrecken-Richtung (uplink direction) zu vermeiden (vgl. Streitpatentschrift, Abs. 23 i. V. m. Abs. 21 und Abs. 22).


3. Die Aufgabe bzw. die technische Problemstellung soll nach Hauptantrag sowie
   nach Hilfsantrag A.1 unter anderem durch ein zellulares System bzw. Zellenfunksystem (cellular system) gemäß Patentanspruch 14 gelöst werden, wobei
   dieses zur Übermittlung von Datenpaketen / Paketdaten (packet data) im Zusammenhang mit der sogenannten Aufwärtsstrecken-Richtung (uplink direction) von einer Mobilstation (mobile station) zum System eingerichtet ist und das
   zellulare System dabei Mittel (means) aufweist, um eine Kanalauswahl auf Basis eines Vergleiches zwischen einem Schwellenwert eines Parameters zur Kanalauswahl und einem aktuellen Wert des Parameters zur Kanalauswahl durchzuführen. In der beschränkten Fassung nach Hilfsantrag A.2 beansprucht das
   Streitpatent nach Patentanspruch 1 ein Verfahren zur Übermittlung von Datenpaketen bzw. Paketdaten in der Aufwärtsstrecken-Richtung sowie nach Patentanspruch 15 eine Mobilstation, welche Mittel aufweist, um eine Kanalaus-

                                      - 17 -


   wahl auf Basis eines Vergleiches zwischen einem Schwellenwert eines Parameters zur Kanalauswahl und einem aktuellen Wert des Parameters zur Kanalauswahl durchzuführen. Des Weiteren wird die Verwendung des Verfahrens gemäß Anspruch 1 und der Mobilstation gemäß Anspruch 15 in einem UMTS-System beansprucht (Patentansprüche 19 und 21).




       II. Zur Verteidigung nach Hauptantrag und nach Hilfsantrag A.1


In den Fassungen des Hauptantrags und des Hilfsantrags A.1 kann die Beklagte ihr
Patent nicht erfolgreich verteidigen, weil diesen Fassungen der Nichtigkeitsgrund
der unzulässigen Erweiterung entgegensteht (Artikel II § 6 Abs.1 Nr.3 IntPatÜG,
Artikel 138 Abs.1 Buchst.c) EPÜ).


1. Der vom Europäischen Patentamt in der Verfahrenssprache Englisch erteilte
   Patentanspruch 14 (Hauptantrag) bzw. der identische Patentanspruch 14
   nach Hilfsantrag A.1 lässt sich wie folgt gliedern:


          14.      A cellular system comprising


          14.1     -   means for sending packet data in the uplink direction from
                       a mobile station to the system using a selected channel,


          14.2     -   means for selecting a common channel (RACH) or a dedicated channel (DCH) for the sending of a data packet,


             characterized in that it also comprises


          14.3     -   means for defining a threshold value of a channel selection
                       parameter,

                                       - 18 -


          14.4     -   means for sending said threshold value of the channel selection parameter from the system to the mobile station in
                       order to compare said threshold value of the channel selection parameter to a current value of the channel selection
                       parameter, and


          14.5     -   means for making said channel selection on the basis of
                       said comparison.


2. Der zuständige Fachmann, der als ein Ingenieur der Elektrotechnik mit Fachrichtung Nachrichtentechnik anzusehen ist und über eine mehrjährige Erfahrung auf dem Gebiet der Mobilfunksysteme im Zusammenhang mit Mobilfunkstandards und Übertragungstechnik in Mobilfunknetzen verfügt, versteht den
   nach Hauptantrag wie auch nach Hilfsantrag A.1 verteidigten Patentanspruch
   14 wie folgt:


   Anspruch 14 betrifft ein Zellenfunksystem bzw. zellulares System (cellular system) und eine Kanalauswahl im Rahmen des sogenannten „Hochladens“ von
   Daten von einer Mobilstation zum zellularen System (vgl. Streitpatentschrift, Fig.
   1 sowie Abs. 1, 3, 4 und 19). Dieses System beinhaltet gemäß der Beschreibung des Streitpatents einzelne Basisstationen (BS) sowie Funknetzwerkeinrichtungen (RNC) im Rahmen eines hierarchisch aufgebauten Funkzugangsnetzes (UTRAN = UMTS Terrestrial Radio Access Network), nicht jedoch eine
   Mobilstation (MS), die per Funk mit dem zellularen System verbunden ist (vgl.
   Streitpatentschrift, Titel und Fig. 1, Abs. 1 sowie Abs. 3, 4, 19 und 46: mobile
   station 800 according to the invention and its connection to a cellular system).
   Zum Senden eines Datenpakets sind entsprechend den Merkmalen 14.1 und
   14.2 Mittel im zellularen System vorgesehen, mit denen ein gemeinsamer Kanal
   (RACH = Random Access Channel) oder ein zweckgebundener Kanal (DCH =
   Dedicated Channel) ausgewählt wird, welcher dann zum Übertragen bzw. Senden des Datenpaketes von der Mobilstation an das zellulare System dient. Des

                                      - 19 -


   Weiteren weist das zellulare System gemäß Merkmal 14.3 ein Mittel zur Definition eines Schwellenwerts (threshold value) eines Parameters zur Kanalauswahl (channel selection parameter) auf. Dieser Schwellenwert des Parameters
   zur Kanalauswahl wird an die Mobilstation gesendet, um einen Vergleich des
   Schwellenwerts des Kanalauswahlparameters mit einem momentanen Wert
   des Kanalauswahlparameters (current value) zu ermöglichen (Merkmale 14.4).
   Das zellulare System soll gemäß Merkmal 14.5 zudem Mittel aufweisen, um die
   Kanalauswahl (channel selection) auf Basis des zuvor genannten Vergleichs
   durchzuführen (A cellular system comprising […] means for making said channel selection on the basis of said comparison).


3. Der auf ein Zellenfunksystem bzw. zellulares System (cellular system) gerichtete Patentanspruch 14 geht über den Inhalt der Anmeldung in der ursprünglichen Fassung hinaus und weist damit eine unzulässige Erweiterung auf.


   Entgegen der von der Beklagten vertretenen Auffassung kann der Fachmann
   der ursprünglichen Anmeldung gemäß WO 00/51245 A2 – wie auch dem inhaltsgleichen Prioritätsdokument – nicht entnehmen, dass das zellulare System
   selbst die Mittel aufweist, um die Kanalauswahl auf Basis des Vergleichs des
   Schwellenwerts eines Parameters zur Kanalauswahl mit einem momentanen
   Wert des Parameters zur Kanalauswahl durchzuführen (vgl. Merkmal 14.5
   i.V.m. Merkmal 14.4). Vielmehr ist in der ursprünglichen Anmeldung offenbart,
   dass ein Parameterwert zur Kanalauswahl vom zellularen System an die Mobilstation gesendet wird und die Mobilstation die Mittel (means) zu Kanalauswahl
   aufweist, bzw. dass die Auswahl des Kanals von der Mobilstation getroffen wird
   (vgl. die ursprünglichen Ansprüche 15 und 16, sowie die ursprüngliche Beschreibung, S. 7, Z. 4-11, insbesondere Z. 7-11: […] mobile station […] comprises: […] means for making said selection […]; vgl. auch Fig. 6 und 8 mitsamt
   zugehörigen Text auf S. 8, Z. 14-17, und S. 10, Z. 10-14: […] channel selected
   by the mobile station). Darüber hinaus wird hinsichtlich der Kanalauswahl in der
   Beschreibungseinleitung der ursprünglichen Anmeldung vor der Beschreibung
   der Erfindung lediglich darauf hingewiesen, dass es ein Problem sei, dass das

                                     - 20 -


   System keine Information über zu sendende Datenpaket für die Paketdatenübertragung auf der Aufwärtsstrecke (uplink packet data transfer) habe. Denn
   folglich müsse die Information über zu übertragende Datenpakete erst an das
   System übermittelt werden, woraufhin das System seine Entscheidung der Kanalauswahl an die Mobilstation senden müsse. Dies beanspruche Kapazitäten
   und verlangsame den Transfer der Datenpakete (vgl. urspr. Anmeldung gemäß
   WO 00/51245 A2, S. 4, Z. 25-31). Im Anschluss daran wird dann die Lösung
   des Problems im Rahmen von Mitteln zur Kanalauswahl in der Mobilstation beschrieben, wie vorstehend ausgeführt (vgl. urspr. Anmeldung gemäß
   WO 00/51245 A2 ab S. 4, Z. 32, insbes. S. 7, Z. 4-11, und S. 10, Z. 10-14).
   Damit ist der Gegenstand des Anspruchs 14 nach Haupt- bzw. Hilfsantrag A.1,
   der Mittel zur Kanalauswahl im zellularen System beinhaltet, in dieser Form
   nicht in der ursprünglichen Anmeldung offenbart und geht folglich über den Inhalt Anmeldung in der ursprünglichen Fassung hinaus.


4. Die weiteren Patentansprüche des Hauptantrags und des Hilfsantrags A.1 bedürfen keiner weiteren isolierten Prüfung, weil die Beklagte in der mündlichen
   Verhandlung erklärt hat, dass sie den Hauptantrag und den Hilfsantrag A.1 jeweils als geschlossenen Anspruchssatz versteht und das Streitpatent in der Reihenfolge des Hauptantrags und der Hilfsanträge jeweils als Ganzes verteidigt
   (vgl. BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 –
   Datengenerator).




              III. Zur beschränkten Verteidigung nach Hilfsantrag A.2


Demgegenüber kann die Beklagte ihr Patent mit der Fassung nach Hilfsantrag A.2
beschränkt verteidigen, weil dieser Fassung des Streitpatents keine Nichtigkeitsgründe entgegenstehen.

                                         - 21 -


1. Die unabhängigen Patentansprüche 1 und 15 nach Hilfsantrag A.2 lassen sich
   in der Verfahrenssprache, die der beschränkten Verteidigung zugrunde liegt,
   wie folgt gliedern:


   Anspruch 1:

          1.1     A method for transferring packet data in the uplink direction from
                  a mobile station to a system in such a manner that


          1.2     -      a common channel (RACH) or a dedicated channel (DCH) is
                         selected for the sending of a data packet, and


          1.3     -      the data packet is sent using the channel seIected,


                      characterized in that


          1.4     -      a threshold value of a channel selection parameter is defined
                         (620),


          1.5     -      said threshold value of the channel selection parameter is
                         sent to the mobile station (630),


          1.6     -      a current value of the channel selection parameter is compared to said threshold value of the channel selection parameter by the mobile station (650), and


          1.7     -      said selection is performed on the basis of said comparison
                         (660).


      Anspruch 15:

          15.1    A mobile station connected with a cellular system,

                                        - 22 -


          15.2    comprising means for sending uplink packet data to the system using a selected channel,


          15.3    wherein the selected channel is either a common channel
                  (RACH) or a dedicated channel (DCH),


                      characterized in that it also comprises


          15.4    -     means for receiving a threshold value of a channel selection parameter from the system,


          15.5    -     means for storing said threshold value of the channel
                        selection parameter,


          15.6    -     means for comparing said threshold value of the channel selection parameter to a current value of the channel selection parameter for basis of said channel selection, and


          15.7    -     means for making said channel selection on the result
                        of said comparison.”




2. Anspruch 1 nach Hilfsantrag A.2 betrifft ein Verfahren zum Übertragen von Datenpaketen / Paketdaten (packet data) im Zusammenhang mit einer Paketdatenvermittlung auf einer Aufwärtsstrecken-Richtung (uplink direction) von einer
   Mobilstation (MS) an ein System, welches als zellulares System anzusehen ist
   (vgl. Streitpatentschrift, Fig. 8 und Abs. 46 / Merkmal 1.1). Zum Senden eines
   Datenpakets wird entweder ein gemeinsamer Kanal (RACH: Random Access
   Channel) oder ein dedizierter / zweckgebundener Kanal (DCH: Dedicated
   Channel) ausgewählt (Merkmale 1.2 und 1.3). Der gemeinsame Kanal (RACH)
   stellt für den Fachmann einen zufallsgesteuerten Direktzugriffs-/Transportkanal

                                     - 23 -


dar, während der zweckgebundene Kanal (DCH) der Mobilstation für einen gegebenen Dienst zugewiesen wird (vgl. Streitpatentschrift, Abs. 5). Des Weiteren
wird bei dem Verfahren gemäß Patentanspruch 1 nach Hilfsantrag A.2 ein
Schwellenwert (threshold value) eines Parameters zur Kanalauswahl (channel
selection parameter) definiert (vgl. Streitpatentschrift, Fig. 6, Schritt 620, sowie
Abs. 0046 / Merkmal 1.4) und an die Mobilstation gesendet (vgl. Schritt 630 in
Fig. 6 / Merkmal 1.5). Ein momentaner Wert des Parameters zur Kanalauswahl
(current value of the channel selection parameter) wird dann seitens der Mobilstation (by the mobile station (650)) mit dem gesendeten Schwellenwert des
Kanalauswahlparameters verglichen (vgl. Streitpatentschrift, Fig. 6, Schritt 630,
und Abs. 50, letzter Satz / Merkmal 1.6). Das Merkmal 1.7 wird dabei vom
Fachmann so verstanden und ist dementsprechend auch im Einklang mit der
Beschreibung nur so auszulegen, dass die Auswahl des Kanals (selection) von
der Mobilstation (mobile station) auf der Basis des Vergleichs mit dem zugesandten Schwellenwert des Parameters zur Kanalauswahl durchgeführt wird
(vgl. Schritt 660 in Fig. 6 sowie Fig. 8 und den zugehörigen Text in Abs. 0050,
insbes. letzter Satz: […] channel selected by the mobile station).


Gemäß Anspruch 15 nach Hilfsantrag A.2 ist eine Mobilstation (mobile station)
vorgesehen, die mit einem Zellenfunksystem bzw. zellularen System (cellular
system) verbunden ist, wobei die Mobilstation die Mittel zum Senden von Datenpaketen bzw. Paketdaten auf der sogenannten Aufwärtsstrecke (uplink) an
das System unter Verwendung eines ausgewählten Kanals aufweist (Merkmale
15.1 und 15.2). Gemäß Merkmal 15.3 ist der ausgewählte Kanal wiederum entweder ein gemeinsamer Kanal (RACH) oder ein zweckgebundener Kanal
(DCH). Die Mobilstation umfasst dabei auch Mittel zum Empfangen eines
Schwellenwertes eines Parameters zur Kanalauswahl von dem zellularen System (Merkmal 15.4), Mittel zum Speichern des Schwellenwertes des Parameters zur Kanalauswahl (Merkmal 15.5) sowie Mittel zum Vergleichen dieses
Schwellenwertes mit einem momentanen Wert des Kanalauswahlparameters
als Grundlage für die Kanalauswahl (Merkmal 15.6). Darüber hinaus weist die

                                      - 24 -


   Mobilstation Mittel auf, um die Kanalauswahl auf Basis des Ergebnisses des
   vorstehend genannten Vergleichs durchzuführen (Merkmal 15.7).


   Demnach kommt in den unabhängigen Ansprüchen 1 und 15 nach Hilfsantrag
   A.2 zum Ausdruck, dass die Auswahlentscheidung auf Basis des vom zellularen
   System zugesandten Schwellenwertes in der Mobilstation stattfindet und dass
   die Mobilstation die Mittel für eine solche Kanalauswahl aufweist.


   Eine Mitteilung der Auswahlentscheidung der Mobilstation an das zellulare System bzw. Mobilfunknetz ist nicht Gegenstand des Anspruchs 1 oder des Anspruchs 15. So ist eine von der Beklagten in der mündlichen Verhandlung vorgetragene Umsetzung im Zusammenhang mit einer Signalisierung der Auswahl
   im Rahmen eines Requests bzw. mit einem Bit an das zellulare System respektive Mobilfunknetz, um dem System anzuzeigen, dass seitens der Mobilstation
   beispielsweise ein dedizierter Kanal / DCH ausgewählt wurde, nicht Gegenstand der Ansprüche 1 oder 15.


   Die nebengeordneten Patentansprüche 19 und 21 nach Hilfsantrag A.2 sind auf
   die Verwendung des Verfahrens nach Patentanspruch 1 bzw. die Verwendung
   der Mobilstation nach Patentanspruch 15 in einem UMTS-System gerichtet.


   Der auf ein zellulares System gerichtete Patentanspruch 14, der entsprechend
   vorstehenden Ausführungen zum Hauptantrag bzw. Hilfsantrag A.1 eine unzulässige Erweiterung bezüglich des Ortes der Kanalauswahl aufweist, ist in Hilfsantrag A.2 nicht mehr enthalten.


3. Der unabhängige Patentanspruch 1 nach Hilfsantrag A.2, der der Fassung des
   erteilten Anspruchs 1 entspricht, ist zulässig, insbesondere ist sein Gegenstand
   in der ursprünglichen Anmeldung offenbart. Dies gilt auch für den nebengeordneten Anspruch 15 nach Hilfsantrag A.2, der auf den erteilten Ansprüchen 15
   und 16 basiert.

                                   - 25 -


Die Merkmale 1.1 bis 1.3 des Patentanspruchs 1 nach Hilfsantrag A.2 sowie die
Merkmale 15.1 bis 15.3 des Patentanspruchs 15 nach Hilfsantrag A.2 sind in
den ursprünglichen Ansprüchen 1 und 15 sowie der ursprünglichen Beschreibung gemäß der Offenlegungsschrift WO 00/51245 A2 offenbart (vgl. u. a. S. 4,
letzter Abs. und S. 5, erster Abs. sowie S. 6, zweiter Abs., S. 7, zweiter Abs.
und Fig. 6 mitsamt zugehörigem Text ab S. 7, letzter Abs.). Entgegen der seitens der Klägerinnen vertretenen Auffassung ist das Merkmal 1.4 des Patentanspruchs 1 bezüglich der Definition eines Schwellenwertes eines Parameters zur
Kanalauswahl (a threshold value of a channel selection parameter is defined) in
der ursprünglichen Figur 6 offenbart (vgl. Schritt 620: DEFINE THRESHOLD
VALUES OF CHANNEL SELECTION PARAMETER) und umfasst auch dessen
Einzahl (threshold value). Als ein Beispiel für einen Parameter zur Kanalauswahl ist in der Beschreibung die zu übertragene Datenmenge (amount of data
to be transferred) offenbart (vgl. WO 00/51245 A2, S. 8, Z. 18-19). Auch das
Senden des Schwellenwertes des Kanalauswahlparameters an die Mobilstation
gemäß Merkmal 1.5 ist in der ursprünglichen Anmeldung beschrieben. Entsprechend vorstehenden Ausführungen offenbart die ursprüngliche Figur 6 auch,
dass im Schritt 620 ein Kanalauswahlparameter bzw. ein Schwellenwert des
Kanalauswahlparameters definiert wird. Dieser Schritt 620 geschieht vor dem
Sendevorgang im Ablaufdiagramm der Figur 6 (vgl. Schritt 630 und ebenso den
ursprünglichen Anspruch 1). Nach dem Sendevorgang mit Parameterwerten
(Schritt 630 in Fig. 6 der ursprünglichen Anmeldung) wird der definierte Schwellenwert (said threshold value of the channel selection parameter) in Schritt 650
mit einem momentanen bzw.aktuellen Wert (current value) des Kanalauswahlparameters verglichen, um den Kanal in der Mobilstation entsprechend den
Merkmalen 1.6 und 1.7 auszuwählen (vgl. ursprüngliche Anmeldung gemäß
WO 00/51245 A2, Anspruch 2 auf S. 11: the current value of the channel selection parameter sent to the mobile station is compared to said threshold value of
the channel selection parameter; vgl. Fig. 6, Schritt 650: COMPARE CHANNEL
SELECTION PARAMETERS AND PACKET DATA INFORMATION TO
THRESHOLD VALUES). Demnach offenbart die ursprüngliche Anmeldung,

                                      - 26 -


   dass der in Schritt 620 definierte Schwellenwert in Schritt 630 mit anderen Parametern, wie dem Wert des aktuellen Kanalauswahlparameters, an die Mobilstation gesendet wird, um dort im Vergleichsschritt 650 zur Entscheidung der
   Kanalauswahl genutzt zu werden (vgl. Merkmale 1.6 und 1.7). Dies wird durch
   den ursprünglichen Unteranspruch 11 bestätigt, in dem in einer konkreten Ausgestaltung in beispielhafter Weise aufgeführt wird, dass der an die Mobilstation
   gesendete Wert des Kanalauswahlparameters ein Schwellenwert für Daten in
   RLC-Puffern ist (the channel selection parameter value sent to the mobile station is a threshold value for the data in the RLC buffer(s)). Das Verfahren gemäß
   Anspruch 1 ist damit in der ursprünglichen Anmeldung offenbart und geht nicht
   über dessen Inhalt hinaus. Vorstehende Ausführungen gelten ebenso für den
   auf eine Mobilstation gerichteten und ebenfalls als zulässig anzusehenden Patentanspruch 15 mit den entsprechenden Merkmalen 15.4 bis 15.7 bezüglich
   Mitteln zum Empfangen und Speichern des vorstehend genannten Schwellenwertes sowie Mitteln zur Kanalauswahl auf Basis eines Vergleichs zwischen
   dem Schwellenwert und einem aktuellen Wert eines Parameters zur Kanalauswahl.


   Die auf eine Verwendung in einem UMTS-System gerichteten Patenansprüche
   19 und 21 nach Hilfsantrag A.2, die auf die Ansprüche 1 und 15 rückbezogen
   sind, basieren auf den ursprünglichen Ansprüchen 20 und 21.


   Bezüglich der Merkmale der von den Patentansprüchen 1 und 15 nach Hilfsantrag A.2 abhängigen Ansprüche ist ebenfalls keine unzulässige Erweiterung ersichtlich.


4. Die Priorität der Voranmeldung vom 23. Februar 1999 (PCT/FI 00/00137, Anmeldung Nr. 990384) wird in Bezug auf den Gegenstand des erteilten Patentanspruchs 1, der mit dem Patentanspruch 1 nach Hilfsantrag A.2 übereinstimmt,
   zu Recht in Anspruch genommen.

                                     - 27 -


   Dies gilt ebenfalls für den Gegenstand des Patentanspruchs 15 nach Hilfsantrag
   A.2. Entgegen der von Seiten der Klägerinnen vertretenen Auffassung wird die
   Kanalauswahl gemäß der eingeschränkten Anspruchsfassung nach Hilfsantrag
   A.2 ohne Zweifel in der Mobilstation durchgeführt, an die das zellulare System
   den Schwellenwert eines Parameters zur Kanalauswahl sendet – in Übereinstimmung mit dem unstreitigen Inhalt der Prioritätsanmeldung bezüglich der Kanalauswahl in der Mobilstation (vgl. hierzu auch vorstehende Ausführungen unter Ziffer III.2. zur Auslegung der Patentansprüche 1 und 15 nach Hilfsantrag
   A.2). Da die Identität der in der Voranmeldung vom 23. Februar 1999 enthaltenen Erfindung und der Erfindung in der Fassung des Streitpatents mit den mit
   den Patentansprüchen 1 und 15 nach Hilfsantrag A.2 gegeben ist, ist die materiell wirksame Inanspruchnahme der Priorität auch diesbezüglich anzuerkennen.


5. Soweit die Klägerinnen die mangelnde Ausführbarkeit des Gegenstands des
   Anspruchs 1 des Streitpatents, der in der erteilten Fassung mit der Fassung
   nach Hilfsantrag A.2 übereinstimmt, geltend machen, vermag sich der Senat
   dem nicht anzuschließen.


   Die Klägerinnen behaupten insoweit, dass der Anspruch 1 Merkmale bezüglich
   nicht weiter bestimmten Parametern zur Kanalauswahl beinhalte, wobei für den
   Fachmann nicht erkennbar sei, woher diese Parameter stammten und was ein
   momentaner Wert sei, so dass er nicht in der Lage sei, die Erfindung auszuführen. Dieser Auffassung kann sich der Senat nicht anschließen. Vielmehr ist der
   Beklagten zuzustimmen, dass der Fachmann den Ansprüchen sowie der Beschreibung mitsamt zugehörigen Figuren diesbezüglich auch konkretere Ausgestaltungen entnehmen kann, wobei es sich bei den zum Einsatz kommenden
   Parametern zur Kanalauswahl u. a. um die Größe eines Datenpakets (data packet size) handelt (vgl. Unteranspruch 7, erster Spiegelstrich, sowie Beschreibung des Streitpatents, Abs. 38). Des Weiteren ist dazu für den Fachmann im
   Streitpatent in hinreichender Weise als Ausführungsbeispiel offenbart, dass die
   Mobilstation den momentanen Wert dieses Kanalauswahlparameters anhand

                                  - 28 -


des Füllstands eines RLC-Zwischenspeichers berechnet und dass es sich bei
dem an die Mobilstation gesandten Schwellenwert eines Parameters zur Kanalauswahl um einen Schwellenwert für die Daten in dem RLC-Zwischenspeicher
handelt (vgl. u.a. Unteransprüche 2, 8 und 10 sowie Beschreibung des Streitpatents, Abs. 25 und 32). Dies gilt in gleicher Weise für den Gegenstand des
nebengeordneten Anspruchs 15 nach Hilfsantrag A.2.


Entgegen den Ausführungen seitens der Klägerinnen besteht nach Ansicht des
Senats auch kein Widerspruch zwischen den nebengeordneten Ansprüchen
und der Beschreibung, dass anspruchsgemäß ein Schwellenwert für den Kanalauswahlparameter an die Mobilstation gesendet werde, aber nach Absatz 26
der Beschreibung bestimmte Kanalauswahlparameter der Mobilstation vorlägen. Vielmehr wird in der Mobilstation ein ihr bekannter momentaner Wert eines
Parameters zur Kanalauswahl mit einem ihr zugesandten Schwellenwert verglichen (vgl. Ansprüche 1 und 15 sowie Fig. 6 und Abs. 38, 39 und 43 der Beschreibung). Für den Fachmann liegt damit kein Widerspruch zwischen den Ansprüchen und der Beschreibung vor, welcher einer Ausführbarkeit entgegenstehen könnte.


Auch die von Seiten der Klägerinnen vertretene Auffassung, dass das Streitpatent nur eine Ausführungsform beschreibe, gemäß der die Mobilstation die Kanalauswahlentscheidung treffe und der Fachmann nicht wisse, wie die Mobilstation unter Beibehaltung einer Verbindung einen Kanal auswählen und verwenden könne, weil aus dem Stand der Technik nur bekannt sei, dass das Netz
die Kanalauswahlentscheidung treffe, ist nicht zuzustimmen. Denn in Absatz 43
der Beschreibung wird im Zusammenhang mit der Figur 6 ein Ausführungsbeispiel zu einer Kanalauswahl in Bezug auf einen RACH- bzw. DCH-Zustand beschrieben, so dass eine Ausführbarkeit auch in dieser Hinsicht gegeben ist.


Ein Mangel bezüglich der Ausführbarkeit liegt damit nicht vor (vgl. u. a. BGH,
Urteil vom 13. Juli 2010 - Xa ZR 126/07, GRUR 2010, 916, Leitsatz – Klammernahtgerät).

                                       - 29 -




6. Die Gegenstände der unabhängigen Ansprüche 1 und 15 in der Anspruchsfassung nach Hilfsantrag A.2 sind neu und beruhen auf einer erfinderischen Tätigkeit.


   a) Neuheit

   Aus dem von der Klägerin zu 1 angeführten Stand der Technik gemäß NK71
   bzw. der inhaltsgleichen Druckschrift D43 der Klägerin zu 3 ist ein Verfahren
   zum Senden von Paketdaten bzw. zum Senden eines Datenpakets (digital data
   packet) in der sogenannten Aufwärtsstreckenrichtung (reverse link) von einer
   Mobilstation (digital transceiver / mobile cellular telephones / user (or mobile
   unit) / user 202) in Richtung eines zellularen Systems bzw. Mobilfunksystems
   (cellular telephone communications system) entsprechend Merkmal 1.1 bekannt (vgl. Sp. 6, Z. 3-12, Sp. 7, Z. 27-32, und Sp. 11, Z. 20-33 sowie Fig. 2 und
   3). Dazu wird entweder ein gemeinsamer Kanal (Random Access Channel 208)
   oder ein zweckgebundener Kanal (Dedicated Channel 214) entsprechend der
   Merkmale 1.2 und 1.3 ausgewählt (vgl. a.a.O.). Des Weiteren sind Schwellenwerte (first threshold level / second threshold level) bezüglich eines Kanalauswahlparameters definiert, welche in einem Prozessor einer Umschalteinrichtung
   (processor 302, switching station 110) des zellularen Systems bzw. Netzes zur
   Kanalauswahl dienen (vgl. Fig. 3 und Sp. 11, Z. 20-53 / Merkmal 1.4). Der Beklagten ist dabei zuzustimmen, dass die Druckschrift weder offenbart, dass der
   Mobilstation ein Schwellenwert zugesandt wird, noch dass die Mobilstation einen Vergleich eines Kanalauswahlparameters mit einem Schwellenwert durchführt, wie es in den Merkmalen 1.5 und 1.6 angeben ist. Die seitens der Klägerinnen diesbezüglich zitierte Passage (Sp. 27, Z. 9-13) weist lediglich darauf
   hin, dass die Mobilstation auch eigene Kriterien zur Kanalauswahl haben kann,
   solange dies nicht zu einem Konflikt mit den Prozeduren einer Basisstation
   führt. Dies bedeutet aber nicht den Empfang eines Schwellenwertes durch die
   Mobilstation oder eine Kanalwahl seitens der Mobilstation auf der Basis eines
   zugesandten Schwellenwertes eines Parameters zur Kanalauswahl gemäß

                                   - 30 -


Merkmal 1.5 und 1.6 bzw. Merkmal 1.7, die damit nicht aus diesem Stand der
Technik bekannt sind. Dies gilt in gleicher Weise in Bezug auf die Merkmale des
Vorrichtungsanspruchs 15 nach Hilfsantrag A.2, wobei die aus NK71 (bzw. der
inhaltsgleichen D43) bekannte Mobilstation keine Mittel entsprechend der Merkmale 15.4 bis 15.7 aufweist, die eine Kanalauswahl in der Mobilstation auf Basis
eines zugesandten Schwellenwertes betreffen.


Die Gegenstände der Ansprüche 1 und 15 nach Hilfsantrag A.2 sind damit neu
gegenüber dem Stand der Technik gemäß NK71 bzw. D43.


Auch der von der Klägerin zu 3 als zusätzliche Information zu Druckschrift D43
eingereichte Auszug D4a aus der Akte zum Prüfungsverfahren vor dem Europäischen Patentamt ändert nichts an der Neuheit der Gegenstände der Ansprüche 1 und 15 nach Hilfsantrag A.2 gegenüber diesem Stand der Technik.




Der Stand der Technik gemäß NK81 offenbart ein Verfahren zum Senden von
Datenpaketen bzw. Paketdaten (packet data) in der sogenannten Aufwärtsstreckenrichtung von einer Mobilstation (MS / mobile station) zum Mobilfunknetzwerk bzw. zum zellularen System entsprechend Merkmal 1.1 (vgl. Kap. 1, zweiter Abs.). Hier wird auch ein gemeinsamer Kanal (Random Access Channel /
RACH) oder ein zweckgebundener Kanal (Dedicated Channel / DCH) entsprechend den Merkmalen 1.2 und 1.3 ausgewählt (vgl. a.a.O. und S. 109, Kap. V,
Abschnitt A). Zudem ist ein Schwellenwert bezüglich einer Ausgangs-Bitrate
(threshold on the output bit rate) definiert, wobei die Ausgangs-Bitrate – entgegen der Auffassung der Beklagten – als Kanalauswahlparameter anzusehen ist,
der zur Kanalauswahl (RACH oder DCH) dient (Kap. V, Abschnitt C, le. Abs.
i.V.m. Kap. IV, S. 108, Mitte re. Sp.: The rate is specified in a Transmission
Format (TF) / Merkmal 1.4). Darüber hinaus ist der Beklagten jedoch zuzustimmen, dass die Druckschrift nicht offenbart, dass der Mobilstation dieser Schwellenwert eines Parameters zur Kanalauswahl zugesendet wird und dass die Mo-

                                   - 31 -


bilstation eine Kanalwahl auf Basis eines Vergleichs eines Kanalauswahlparameters mit einem Schwellenwert durchführt, wie es in den Merkmalen 1.5 bis
1.7 gefordert ist. Dies gilt in gleicher Weise in Bezug auf die Merkmale des Vorrichtungsanspruchs 15 mit den Merkmalen 15.1 bis 15.7, wobei der NK81 nicht
zu entnehmen ist, dass die dort beschriebene Mobilstation auch Mittel gemäß
den Merkmalen 15.4 bis 15.7 aufweist, die einer Kanalauswahl in der Mobilstation auf Basis eines zugesandten Schwellenwertes dienen.




Die Masterarbeit gemäß NK91, welche im Gegensatz zu den Patentansprüchen
1 und 15 eine Übertragung von Datenpaketen in die Abwärtsrichtung betrifft
(vgl. u. a. S. 8, letzter Abs.), wobei auch keine Kanalauswahl in einer Mobilstation im Zusammenhang mit einem Vergleich mit einem der Mobilstation zugesandten Schwellenwert thematisiert wird, ist erst am 17. April 1999 und damit
nach dem 23. Februar 1999 als Prioritätstag des Streitpatents veröffentlicht worden und zählt damit nicht zum relevanten vorveröffentlichten Stand der Technik.




Die – abgesehen von zwei Vorblättern – inhaltsgleichen Dokumente NK12,
(ETSI TS 125 331 V3.1.0 (2000-01)) und D13 (3G TS 25 331 V3.1.0 (2000-01)),
welche von der Klägerin zu 2 bzw. der Klägerin zu 3 genannt worden sind und
im Gegensatz zum Streitpatent auch keine Kanalauswahl in einer Mobilstation
im Zusammenhang mit einem Vergleich mit einem der Mobilstation zugesandten Schwellenwert beinhalten, sind jeweils erst im Jahr 2000 und somit auch
nach dem 23. Februar 1999 als Prioritätstag des Streitpatents veröffentlicht .
Sie zählen daher ebenfalls nicht zum relevanten Stand der Technik. An der
Nachveröffentlichung des ETSI-Dokuments D13 ändert auch die seitens der
Klägerin zu 3 ergänzend eingereichte Schrift D1a3 nichts, hier sind lediglich Daten zu einem Treffen am 3. März 2000, das ebenfalls nach dem Prioritätszeitpunkt stattfand.

                                    - 32 -


Der Stand der Technik gemäß NK22, der von der Klägerin zu 2 in Verbindung
mit einem Protokollentwurf NK32 angeführt wird, offenbart ein Verfahren zum
Senden von Datenpaketen (user packets / Packet data transmission on RACH
and FACH) von einer Mobilstation (mobile station / MS) in einer Aufwärtsstreckenrichtung (reverse link) hin zu einem Mobilfunknetzwerk respektive einem
zellularen System (vgl. NK22, S. 15, Abschnitt 6.2.4.1, i. V. m. S. 30, Abschnitt
9.2.1). Dabei wird ein gemeinsamer Kanal (Random Access Channel / RACH /
common channel) bzw. ein zweckgebundener Kanal (Dedicated Channel /
DCH) entsprechend den Merkmalen 1.1 bis 1.3 ausgewählt (vgl. S. 33, Abschnitt 9.4 und Fig. 9.4.1, i. V. m. S. 35, Abschnitt 9.4.2.1 und Fig. 9.4.3). Zudem wird ein Schwellenwert (threshold […] for triggering a measurement report)
definiert, der mit der Kanalauswahl in dem zellularen System verbunden ist (vgl.
S. 35, Abschnitt 9.4.2.1: selection procedure determines whether the data
should be transmitted on a common channel). Damit wird zwar im Hinblick auf
Merkmal 1.4 ein Schwellenwert in einer Mobilstation (MS) verwendet – dieser
löst jedoch nur einen Messbericht bzw. Report aus (vgl. a. a. O.: […] triggering
a measurement report), um die Basisstation des Systems (BSS) über den Zustand der Mobilstation (MS) zu informieren. Ein Schwellenwert eines Parameters zur Kanalauswahl, der entsprechend Merkmal 1.5 vom System an eine Mobilstation gesendet wird und dann von der Mobilstation mit einem laufenden Parameterwert zur Kanalauswahl in der Mobilstation verglichen wird, wie es in den
Merkmalen 1.6 und 1.7 angegeben ist, kann der Fachmann diesem Stand der
Technik gemäß NK22 jedoch nicht entnehmen.




Auch der Protokollentwurf gemäß NK32, auf den seitens der Klägerin zu 2 im
Zusammenhang mit NK22 verwiesen wird, offenbart keinen Schwellenwert eines
Parameters zur Kanalauswahl. Vielmehr umfassen die dort genannten Parameter Schwellenwert-Niveaus (vgl. S. 16, viertletzter Abs.) für Messungen, die
dazu dienen, Mobilfunkzellen zu überwachen (vgl. u. a. Abschnitt 8.5 auf S. 15
und 16, insbes. S.16, erster und zweiter Abs.: Monitored cells […] 1. Cells that
belong to the active set […]) und um über eine diesbezügliche Übergabe

                                    - 33 -


(handover) zu entscheiden. Dies unterscheidet sich von der im Streitpatent beanspruchten Auswahl eines Kanals in Form eines gemeinsamen Kanals oder
eines dedizierten Kanals, da basierend auf diesen Messungen Mobilfunkzellen
(cells) ausgewählt werden und nicht ein Kanal für die Übertragung eines Datenpakets (vgl. Abschnitt 8.5, a. a. O.). Entscheidet sich das Netz hier für einen
Kanalwechsel, so wird dies der Mobilstation im Wege einer Nachricht bezüglich
einer Kanal-Konfiguration (Physical channel reconfiguration) mitgeteilt (vgl. S.
11, Abschnitt 8.3.7).


Damit ist das Verfahren gemäß Patentanspruch 1 mit den Merkmalen 1.5 bis
1.7 bezüglich einer Kanalauswahl weder aus der NK22 noch aus dem Protokollentwurf NK32 bekannt. Gleiches gilt auch für den Vorrichtungsanspruch 15 nach
Hilfsantrag A.2 mit den Merkmalen 15.4 bis 15.7, die diesem Stand der Technik
nicht zu entnehmen sind.




Die von der Klägerin zu 2 genannte Druckschrift NK42, welche von der Klägerin
zu 3 als Druckschrift D33 benannt worden ist, stellt eine nachveröffentlichte ältere Anmeldung dar, die lediglich die Merkmale 1.1 bis 1.4 sowie 1.6 und 1.7
offenbart. Dabei wird ein Verfahren zum Senden von Paketdaten (data packets)
von einer Mobilstation (mobile station / MS 30) in einer Aufwärtsstreckenrichtung (uplink) zu einem Mobilfunknetzwerk bzw. zellularen System entsprechend
Merkmal 1.1 beschrieben (vgl. S. 3, Z. 15-22 i.V.m. S. 2, Z. 26 – S. 3, Z. 3 sowie
Fig. 2 und 5, Schritt 52). Zu diesem Zweck wird entweder ein gemeinsamer
Kanal (shared channel) oder ein zweckgebundener Kanal (dedicated channel)
entsprechend den Merkmalen 1.2 und 1.3 ausgewählt (vgl. Fig. 5, Schritte 56
und 58 mit S. 11, le. Abs.). Zudem wird ein Schwellenwert (threshold) für die
Menge der Daten in einer Warteschlange (amount of data in queue) im Zusammenhang mit der Kanalauswahl genannt (vgl. S. 4, erster Abs. und Fig. 5, Schritt
54 mit S. 11, le. Abs. / vgl. Merkmale 1.4). Wie die Klägerin zu 2 die in ihrer
Klageschrift selbst angibt, ist das Merkmal 1.5 bezüglich eines von dem zellularen System an die Mobilstation gesendeten Schwellenwertes eines Parameters

                                    - 34 -


zur Kanalauswahl jedoch nicht in der NK42 offenbart – der Gegenstand des Patentanspruchs 1 mit dem Merkmal 1.5 wie auch der Gegenstand des Patentanspruchs 15 nach Hilfsantrag A.2, der mit Merkmal 15.4 entsprechende Mittel
zum Empfangen eines Schwellenwertes eines Parameters zur Kanalauswahl
beinhaltet, sind damit neu gegenüber dem Inhalt der älteren Anmeldung NK42
bzw. D33.


Die Klägerin zu 2 geht in Bezug auf NK42 davon aus, dass ein Schwellenwert,
der nachweislich in der Mobilstation vorliege (Fig. 5, Schritt 58), entweder in der
Mobilstation definiert werde oder vom Mobilfunknetz bzw. einem zellularen System an die Mobilstation gesendet werde, so dass der Fachmann die Auswahl
zwischen zwei Möglichkeiten habe und letztere (entsprechend Merkmal 1.5
bzw. Merkmal 15.4) damit naheliege und keine erfinderische Tätigkeit begründe. Da die Priorität des Streitpatents jedoch zu Recht in Anspruch genommen ist und die NK42 damit eine nachveröffentlichte ältere Anmeldung darstellt,
ist hier jedoch lediglich die Frage der Neuheit relevant, die entsprechend vorstehenden Ausführungen bezüglich Merkmal 1.5 bzw. Merkmal 15.4 gegeben
ist, da der NK42 keine Angabe zum Definieren oder Empfangen des Schwellenwertes zu entnehmen ist.




Druckschrift D23, welche die Klägerin zu 3 neben dem vorstehend in Verbindung
mit NK11 bzw. NK42 abgehandelten Druckschriften D13 und D33 genannt hat,
beschreibt ein Verfahren zum Senden von Datenpaketen für Paketdatendienste
(packet data services) von einer Mobilstation (UE) in einer Aufwärtsstreckenrichtung (transport channel in the uplink) zu einem Mobilfunknetzwerk bzw. zellularen System entsprechend Merkmal 1.1 des Verfahrensanspruchs 1 (vgl. S.
8 erster Abs. und S. 11, mittlerer Abs. über Fig. 2). Hier wird ebenfalls ein gemeinsamer Kanal (common transport channels (RACH/FACH)) oder ein zweckgebundener Kanal (Dedicated transport channels (DCH/FAUSCH)) entsprechend den Merkmalen 1.2 und 1.3 zum Versenden der Datenpakete ausgewählt (vgl. a.a.O. und S. 9, erste Aufzählungspunkte, S. 12, vorle. Abs.). Im

                                    - 35 -


Hinblick auf Merkmal 1.4 ist dabei ein Schwellenwert (thresholds required for
triggering a measurement report) bezüglich der Auslösung eines Messbericht
bzw. Reports zum Verkehrsvolumen im Zusammenhang mit einer Übergabe
(handover) bzw. einem Wechsel der Mobilfunkzelle (cell) offenbart (vgl. a. a. O.,
S. 15 und S. 17, zweiter bis vierter Abs., sowie Fig. 22, S. 55). Ein Schwellenwert zur Kanalauswahl gemäß den Merkmalen 1.4, 1.6 und 1.7, der von dem
zellularen System entsprechend Merkmal 1.5 an die Mobilstation gesendet wird,
ist der Druckschrift D23 entgegen den Ausführungen der Klägerin zu 3 jedoch
nicht zu entnehmen. Des Weiteren gibt es auch keinen Hinweis, dass in der
Mobilstation eine Kanalauswahl entsprechend Merkmal 1.7 vorgesehen ist.
Auch dem von der Klägerin zu 3 hinzugefügten Entwurf einer Sitzungsniederschrift gemäß Dokument D2a (Draft minutes of the 3GPP TSG-RAN WG2 meeting #1) ist ein solcher Zusammenhang nicht zu entnehmen.


Vorstehende Ausführungen gelten in gleicher Weise in Bezug auf den Vorrichtungsanspruch 15 nach Hilfsantrag A.2 mit den Merkmalen 15.4 bis 15.7, die
nicht aus Druckschrift D23 bekannt sind.




Die technische Spezifikation gemäß Druckschrift D53 (3G TS 25.321 V3.2.0
(1999-12)), die von der Klägerin zu 3 in Bezug auf eine geltend gemachte mangelnde erfinderische Tätigkeit und die erteilten Unteransprüche 4 bis 6 genannt
worden, ist erst nach dem Prioritätstag des Streitpatents veröffentlicht worden
und somit nicht relevant hinsichtlich der Beurteilung der Patentfähigkeit der Gegenstände der Patentansprüche 1 und 15 nach Hilfsantrag A.2.




Das Dokument D63 (3G TS 25.303 v3.2.0 (1999-12)), welches sich mit Blick auf
das Streitpatent im Kapitel 7 auf der Seite 82 lediglich mit einer Umkonfiguration
von Kanälen im Zusammenhang mit einer „MEASUREMENT REPORT"-Nachricht einer Mobilstation bzw. User Equipment (UE) befasst, ist erst nach dem

                                   - 36 -


hier maßgeblichen Prioritätstag des Streitpatents veröffentlicht worden und damit hinsichtlich der Merkmale des Verfahrensanspruchs 1 sowie des Vorrichtungsanspruchs 15 nach Hilfsantrag A.2 nicht von Relevanz.




Im Stand der Technik gemäß ETSI-Dokument D73 (UMTS-Spezifikation XX.05,
Version 0.1.0 (September 1998)) wird eine Übertragung von kurzen Datenpaketen in der Aufwärtsstreckenrichtung und im Zusammenhang mit einem physikalischen gemeinsamen Kanal (PRACH) und einem Bedarf für einen reservierten Kanal (reserved channel) thematisiert (vgl. S. 1, Abschnitt Current status
[…] 3.0 Transmission of short (10 ms long) data packets in the uplink; S. 2,
vorletzter Aufzählungspunkt). Ein Hinweis auf einen Schwellenwert zur Kanalauswahl gemäß den Merkmalen 1.4 und 1.6, der von einem zellularen System
entsprechend Merkmal 1.5 an eine Mobilstation gesendet wird, ist der Druckschrift D73 nicht zu entnehmen. Des Weiteren gibt es auch keinen Hinweis, dass
in einer Mobilstation eine Kanalauswahl auf Basis eines von dem zellularen System zur Mobilstation gesendeten Schwellenwertes eines Parameters entsprechend Merkmal 1.7 des Verfahrensanspruchs 1 nach Hilfsantrag A.2 stattfindet.
Dies gilt in gleicher Weise in Bezug auf die entsprechenden Merkmale 15.4 bis
15.7 des Vorrichtungsanspruchs 15 nach Hilfsantrag A.2.




Auch den von der Klägerin zu 3 im Zusammenhang mit D73 genannten Druckschriften D7a bis D7f ist kein Hinweis auf die Merkmale 1.4 bis 1.7 des Patentanspruchs 1 bzw. die Merkmale 15.4 bis 15.7 des Patentanspruchs 15 nach
Hilfsantrag A.2 zu entnehmen. So befasst sich Druckschrift D7a mit der Abhängigkeit von PRACH-Paketgrößen von einem Spreizfaktor (vgl. S. 8, Abschnitt
5.2.2.1, Fig. 3, sowie Abschnitt 5.2.2.1.2). Gemäß Druckschrift D7b kann es seitens des Mobilfunknetzes Vorgaben geben, welcher Spreizfaktor von einer Mobilstation bei Übertragungen auf einem gemeinsamen Kanal (PRACH) zu verwenden ist (vgl. Abschnitt 6.2.3.3, S. 10 unten). Der zugehörige Protokollentwurf
gemäß Druckschrift D7c gibt dabei auch keinen Hinweis auf eine Kanalauswahl

                                    - 37 -


in der Mobilstation auf Basis eines Schwellenwertes entsprechend den Merkmalen 1.4 bis 1.7 bzw. 15.5 bis 15.7. In Druckschrift D7d wird lediglich vorgeschlagen, dass größere Datenmengen mittels dedizierter Kanäle (dedicated
channels) übertragen werden sollen (vgl. S. 2, zweiter Abs.). Die weitere, im
Zusammenhang mit Druckschrift D73 genannte Druckschrift D7e befasst sich
mit einem Fast-Uplink-Signalisierungskanal (FAUSCH), mit dem eine Mobilstation (UE) Anforderungen für einen dedizierten Kanal (DCH) an ein Mobilfunknetz bzw. zellulares System senden kann (vgl. u.a. S. 1, Introduction, S. 2, letzter Abs., und S. 3, erster Abs.). Dabei findet jedoch keine Auswahl eines Kanals
in der Mobilstation im Zusammenhang mit einem Vergleich eines Schwellenwerts eines Parameters zur Kanalauswahl gemäß Merkmal 1.6 bzw. Merkmal
15.6 statt, der entsprechend Merkmal 1.5 vom zellularen System an die Mobilstation gesendet bzw. entsprechend Merkmal 15.4 von Mitteln der Mobilstation
empfangen wird. Die Auswahl des Kanals beruht damit auch nicht auf einem
solchen an die Mobilstation gesendeten bzw. von der Mobilstation empfangenen Schwellenwert, wie es in Merkmal 1.7 bzw. 15.7 im Zusammenhang mit
den vorstehend genannten Merkmalen gefordert ist. Auch Druckschrift D7f, zu
der von Seiten der Klägerinnen nicht weiter ausgeführt worden ist, ist eine solche Merkmalskombination nicht zu entnehmen (vgl. u.a. S. 2, letzter Abs. bzgl.
des Bedarfs an einem für länger Datenpakete reservierten Kanal (reserved
channel)).




Das ETSI-Dokument D83 (Tdoc SMG2 UMTS-L23 477/98) beschreibt in Abschnitt 2.5 eine seitens einer Mobilstation (User Equipment / UE) veranlasste
Umschaltung von einem gemeinsamen zufallsgesteuerten Kanal (RACH) zu einem dedizierten Kanal (DCH) auf Basis einer Nachricht bezüglich eines Messberichts bzw. Reports (measurement report message) und eines internen
Schwellenwerts der Mobilstation (threshold for data buffers in the UE). Die
Nachricht bezüglich des Messberichts wird an ein Mobilfunknetzwerk (network)
bzw. ein zellulares System gesendet (vgl. Abschnitt 2.5 auf S. 6, erster und vor-

                                  - 38 -


letzter Abs.). Das System (network / NW) trifft die Entscheidung, ob ein Kanalwechsel erfolgt (vgl. S. 6, Fig. 5 und vorle. Abs.). Der Fachmann kann diesem
ETSI-Dokument keinen Hinweis auf einen Schwellenwert eines Parameters zur
Kanalauswahl gemäß den Merkmalen 1.4 und 1.6 entnehmen, der entsprechend Merkmal 1.5 von einem zellularen System an eine Mobilstation gesendet
wird. Auch gibt es keinen Hinweis, dass in einer Mobilstation eine Kanalauswahl
auf Basis eines solchen Schwellenwertes entsprechend Merkmal 1.7 stattfindet.
Dies gilt wiederum in gleicher Weise in Bezug auf die entsprechenden Merkmale 15.4 bis 15.7 des Vorrichtungsanspruchs 15 nach Hilfsantrag A.2.




b) Erfinderische Tätigkeit


Wie vorstehend zur Neuheit der Gegenstände der jeweiligen unabhängigen Ansprüche 1 und 15 gemäß Hilfsantrag A.2 ausgeführt, sind dem im Verfahren
befindlichen vorveröffentlichten Stand der Technik die Merkmale 1.4 bis 1.6 im
Zusammenhang mit Merkmal 1.7 bezüglich einer Kanalauswahl in der Mobilstation nicht zu entnehmen. Insbesondere sieht keine der im Verfahren befindlichen Druckschriften vor, dass anhand eines durch die Mobilstation durchgeführten Schwellwertvergleichs mit einem vom System versandten Schwellwert eine
Kanalauswahl ausgeführt wird.


Diesbezüglich geben weder der in der mündlichen Verhandlung diskutierte
Stand der Technik gemäß NK91, NK12 , D23 und D7 in Verbindung mit D7a bis
D7f noch die weiteren im Verfahren befindlichen Druckschriften einen Hinweis
auf einen gemäß Merkmal 1.4 definierten Schwellenwert eines Parameters zur
Kanalauswahl, der entsprechend Merkmal 1.5 von einem zellularen System an
eine Mobilstation gesendet wird und dann in der Mobilstation zur Kanalauswahl
auf Basis eines Vergleichs eines solchen Schwellenwertes mit einem aktuellen
Parameter zur Kanalauswahl entsprechend den Merkmalen 1.6 und 1.7 des
Verfahrensanspruchs 1 nach Hilfsantrag A.2 genutzt wird. Allein die Verwendung von Schwellenwerten im Rahmen des Versands von Messberichten oder

                                       - 39 -


    bei der Überwachung von Mobilfunkzellen durch die Mobilstation im Stand der
    Technik gibt zu einer solchen Ausgestaltung der Kanalauswahl keinen Anlass.
    Dementsprechend sind dem Stand der Technik auch keine Mittel gemäß den
    Merkmalen 15.4 bis 15.7 des Vorrichtungsanspruch 15 nach Hilfsantrag A.2 zu
    entnehmen, die zur Kanalauswahl in einer Mobilstation auf Basis eines der Mobilstation zugesandten Schwellenwertes eines Parameters zur Kanalauswahl
    dienen. Auch eine Zusammenschau des im Verfahren befindlichen Stands der
    Technik führt damit nicht in naheliegender Weise zu den Gegenständen der nebengeordneten Ansprüche 1 und 15 gemäß Hilfsantrag A.2.


    Die Gegenstände der Ansprüche 1 und 15 nach Hilfsantrag A.2 sind dem Fachmann auch unter Einbeziehung seines Fachwissens nicht nahegelegt. Sie beruhen somit auf einer erfinderischen Tätigkeit und sind daher patentfähig.




    c) Abhängige Ansprüche in der Fassung nach Hilfsantrag A.2


    Die auf die unabhängigen Patentansprüche 1 und 15 in der Fassung nach Hilfsantrag A.2 rückbezogenen nebengeordneten Verwendungsansprüche 19 und
    21 sowie die auf die Patentansprüche 1 und 15 nach Hilfsantrag A.2 rückbezogenen Unteransprüche genügen ebenfalls den an sie zu stellenden Anforderungen hinsichtlich Zulässigkeit und Patentfähigkeit.




Da sich die beschränkte Verteidigung in der Fassung des Hilfsantrags A.2 somit als
zulässig und patentfähig erweist, war das Streitpatent teilweise nur hinsichtlich der
erteilten Fassung (Hauptantrag) für nichtig zu erklären und konnte auch in der Fassung nach Hauptantrag A.1 der Beklagten nicht aufrechterhalten werden, während
die Klage im Hinblick auf die Fassung nach Hilfsantrag A.2 abzuweisen war.

                                       - 40 -


                                         B.
                              Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO.
Dabei hat der Senat berücksichtigt, dass der nach Hilfsantrag A.2 als schutzfähig
verbleibende Patentgegenstand gegenüber demjenigen der erteilten Fassung eingeschränkt ist. Diese Einschränkung macht nach der Schätzung des Senats ein
Drittel der wirtschaftlichen Verwertbarkeit des Streitpatents aus, sodass der Beklagten trotz teilweisem Fortbestand des Streitpatents in beschränkter Fassung in diesem Umfang die Gerichtskosten, die außergerichtlichen Kosten der Klägerinnen,
welche hinsichtlich der Gerichtskosten und der außergerichtlichen Kosten der Beklagten nach Kopfteilen haften (§ 84 Abs. 2 PatG i.V.m. § 100 Abs. 1 ZPO), sowie
ihre eigenen außergerichtlichen Kosten aufzuerlegen waren.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                         C.
                       Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130) eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen
Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen

                                      - 41 -


Signatur versehen sein, die von einer internationalen Organisation auf dem Gebiet
des gewerblichen Rechtsschutzes herausgegeben wird und sich zur Bearbeitung
durch das jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des
Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass
gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine
Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die
Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Friehe         Werner          Dr. Schwengelbeck         Altvater      Dr. Flaschke
