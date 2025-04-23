---
ecli: "ECLI:DE:BPatG:2025:230425U4Ni15.23EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 15/23"
decided: "2025-04-23"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2025&Sort=1&Seite=5&nr=44543&anz=77&pos=75&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2025-04-23_4_Ni_15_23_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 15/23 vom 2025-04-23

## Entscheidung

BUNDESPATENTGERICHT
                                          IM NAMEN DES VOLKES

                                                     URTEIL


     4 Ni 15/23 (EP)
 ______________________________________

     (Aktenzeichen)



                                          In der Patentnichtigkeitssache



…




ECLI:DE:BPatG:2025:23042025U4Ni15.23EP.0

                                                  2

                      betreffend das europäische Patent 2 181 559

                                     (DE 60 2008 005 465)




hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 22. Januar 2025 durch die Richterin Werner M. A. als Vorsitzende
und die Richter Dipl.-Ing. Altvater, Dipl.-Ing. Matter, Dr. von Hartz und Dipl.-Ing.
Tischler


für Recht erkannt:


 I. Das europäische Patent 2 181 559 wird mit Wirkung für die Bundesrepublik
    Deutschland im Umfang der angegriffenen Patentansprüche 1, 5, 6, 7, 10 und
    11 dadurch teilweise für nichtig erklärt, dass die Patentansprüche 1 und 11 unter Wegfall der Patentansprüche 5, 6, 7 und 10 die nachfolgende Fassung erhalten:

    1.     A method for handing over a User Equipment (180) from a first base station (110) to
           a second base station (120) of a cellular telecommunication network (100), in
           particularwherein the first base station (110) is from a first eNodeB (110) to-and the
           second base station (120) is a second eNodeB (120) of a Long Term Evolution network
           (100), the method comprising

           •   establishing a first connection (110a) between the User Equipment (180) and the
               first base station (110),
           •   arranging a current configuration of the User Equipment (180) with the first base
               station (110),
           •   forwarding the current configuration of the User Equipment (180) from the first
               base station (110) to the second base station (120) via a terrestrial interface (115),
           •   establishing a second connection (120a) between the User Equipment (110) and
               the second base station (120), and
           •   reusing the forwarded configuration of the User Equipment (180) at least partially
               for the operation of the User Equipment (180), when the User Equipment (180) is
               served by the second base station (120),

                                           3

    characterized by

    -    a set of configuration parameters of the User Equipment (180) is known by the first
         base station (110) and the second base station (120) as a default configuration and
    -    the current configuration of the User Equipment (180) is forwarded from the first
         base station (110) to the second base station (120) by solely forwarding
         configuration parameters, which deviate from the default configuration
    -    wherein the current configuration is forwarded via an X2 interface (115),
    -    wherein the current configuration is a measurement configuration of the User
         Equipment (180) characterizing measurement procedures which are performed by
         the User Equipment (180), and
    -    wherein the current configuration comprises activity data of the User Equipment
         (180), which activity data determine activity times of the User Equipment (180),
         wherein the activity times are used by the User Equipment (180) as a time reference
         for performing measurements.


5. (entfällt)


6. (entfällt)


7. (entfällt)


10. (entfällt)


11. A first base station for a cellular telecommunication network (100), wherein the first
    base station (110) is a first eNodeB (110 of a Long Term Evolution network (100), the
    first base station (110, 210) comprising

    •    a connection unit (211) for establishing a first connection to a User Equipment
         (180),
    •    a receiving unit (212) for receiving a current configuration of the User Equipment
         (180) from the User Equipment (180),
    •    a transmission unit (213) for forwarding the current configuration of the User
         Equipment (180) from the first base station (110, 210) to a second base station
         (120) via a terrestrial interface (115), wherein the second base station (120) is a
         second eNodeB (120) of the Long Term Evolution network (100), and

                                             4

        •   a memory unit (214) for storing configuration parameters of the User Equipment
            (180), which configuration parameters represent a default configuration,

        characterized by

        forwarding the current configuration information of the User Equipment by solely
        forwarding configuration parameters which deviate from the default configuration,
        wherein the current configuration is forwarded via an X2 interface (115).




II.    Im Übrigen wird die Klage abgewiesen




III.   Von den Kosten des Rechtsstreits tragen die Klägerin ein Drittel und
       die Beklagte zwei Drittel.




IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils
       zu vollstreckenden Betrages vorläufig vollstreckbar.

                                          5

                                   Tatbestand


Die Klägerin strebt mit ihrer Klage die teilweise Nichtigerklärung des europäischen
Patents 2 181 559 an.


Die Beklagte ist eingetragene Inhaberin des in englischer Sprache auch mit Wirkung
für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 2 181 559 (Streitpatent), das am 21. August 2008 unter Inanspruchnahme der
Priorität der EP 07016382 vom 21. August 2007 angemeldet worden ist. Die Erteilung des Patents ist am 9. März 2011 veröffentlicht worden.
Das Streitpatent ist in Kraft.


Es wird beim Deutschen Patent- und Markenamt unter dem Aktenzeichen
DE 60 2008 005 465 geführt. Es trägt in der englischen Verfahrenssprache die Bezeichnung
         „HANDOVER OF A USER EQUIPMENT WITH FORWARDING
            AND REUSING A USER EQUIPMENT CONFIGURATION“

                          und in der deutschen Übersetzung
           „ÜBERGABE EINES BENUTZERGERÄTES MIT WEITERLEI-TUNG UND WIEDERVERWENDUNG EINER BENUTZERGE-RÄTKONFIGURATION“.


Das Streitpatent umfasst in der erteilten Fassung elf Patentansprüche, die die Klägerin mit ihrer Nichtigkeitsklage vom 6. April 2023 teilweise und zwar im Umfang
der Patentansprüche 1, 5, 6, 7, 10 und 11 angreift. Die Beklagte verteidigt das Streitpatent mit einem gegenüber der erteilten Fassung geänderten Hauptantrag mit
Schriftsatz vom 27. September 2023 (im Weiteren bezeichnet als „geänderter
Hauptantrag“) sowie mit fünf Hilfsanträgen.


Der ein Verfahren zum Übergeben eines Endgeräts betreffende Patentanspruch 1
lautet in der Verfahrenssprache ausweislich der Streitpatentschrift:

                                 6

1. A method for handing over a User Equipment (180)
   from a first base station (110) to a second base station (120) of a cellular telecommunication network
   (100), in particular from a first eNodeB (110) to a
   second eNodeB (120) of a Long Term Evolution network (100), the method comprising

      •   establishing a first connection (110a) between
          the User Equipment (180) and the first base station (110),
      •   arranging a current configuration of the User
          Equipment (180) with the first base station (110),
      •   forwarding the current configuration of the User
          Equipment (180) from the first base station (110)
          to the second base station (120) via a terrestrial
          interface (115),
      •   establishing a second connection (120a) between the User Equipment (110) and the second
          base station (120), and
      •   reusing the forwarded configuration of the User
          Equipment (180) at least partially for the operation of the User Equipment (180), when the User
          Equipment (180) is served by the second base
          station (120),

   characterized by

       - a set of configuration parameters of the User
          Equipment (180) is known by the first base station (110) and the second base station (120) as
          a default configuration and
       - the current configuration of the User Equipment
          (180) is forwarded from the first base station
          (110) to the second base station (120) by solely

                                            7

                     forwarding configuration parameters, which deviate from the default configuration.


In deutscher Übersetzung lautet Patentanspruch 1 entsprechend der Streitpatentschrift wie folgt:

         1. Verfahren zum Übergeben eines Endgeräts (180)
             von einer ersten Basisstation (110) zu einer zweiten
             Basisstation (120) eines zellularen Telekommunikationsnetzes (100), insbesondere von einem ersten
             eNodeB (110) zu einem zweiten eNodeB (120) eines
             Long Term Evolution Netzwerks (100), wobei das
             Verfahren Folgendes umfasst:
                 •   Herstellen einer ersten Verbindung (110a) zwischen dem Endgerät (180) und der ersten Basisstation (110),
                 •   Vorbereiten einer aktuellen Konfiguration des
                     Endgeräts (180) in der ersten Basisstation
                     (110),
                 •   Weiterleiten der aktuellen Konfiguration des
                     Endgeräts (180) von der ersten Basisstation
                     (110) zur zweiten Basisstation (120) über eine
                     terrestrische Schnittstelle (115),
                 •   Herstellen einer zweiten Verbindung (120a)
                     zwischen dem Endgerät (110) und der zweiten
                     Basisstation (120), und
                 •   Wiederverwenden der weitergeleiteten Konfiguration des Endgeräts (180) mindestens teilweise für den Betrieb des Endgeräts (180),
                     wenn das Endgerät (180) durch die zweite Basisstation (120) bedient wird,

             dadurch gekennzeichnet, dass

                                            8

                 - ein Satz Konfigurationsparameter des Endgeräts (180) der ersten Basisstation (110) und der
                     zweiten Basisstation (120) als Standardkonfiguration bekannt ist, und
                 - die aktuelle Konfiguration des Endgeräts (180)
                     von der ersten Basisstation (110) zur zweiten
                     Basisstation (120) dadurch weitergeleitet wird,
                     dass lediglich die Konfigurationsparameter weitergeleitet werden, die von der Standardkonfiguration abweichen.


Die Patentansprüche 5, 6, 7 und 10 nach Streitpatent sind mittelbar bzw. unmittelbar
auf den Patentanspruch 1 rückbezogen. Wegen der konkreten Fassung wird auf die
Streitpatentschrift Bezug genommen.


Der Patentanspruch 11 nach Streitpatent, der eine erste Basisstation für ein zellulares Telekommunikationsnetz zum Gegenstand hat, lautet in der Verfahrenssprache:

       11. A first base station for a cellular telecommunication
           network (100), the first base station (110, 210) comprising
                •    a connection unit (211) for establishing a first
                     connection to a User Equipment (180),
                •    a receiving unit (212) for receiving a current
                     configuration of the User Equipment (180) from
                     the User Equipment (180),
                •    a transmission unit (213) for forwarding the current configuration of the User Equipment (180)
                     from the first base station (110, 210) to a second
                     base station (120) via a terrestrial interface
                     (115), and

                                            9

                 •   a memory unit (214) for storing configuration
                     parameters of the User Equipment (180), which
                     configuration parameters represent a default
                     configuration,

             characterized by

             forwarding the current configuration information of
             the User Equipment by solely forwarding configuration parameters which deviate from the default configuration.


In deutscher Übersetzung lautet Patentanspruch 11 entsprechend der Streitpatentschrift wie folgt:

      11.    Erste Basisstation für ein zellulares Telekommunikationsnetz (100), wobei die erste Basisstation
             (110, 210) Folgendes umfasst:
                 •   eine Verbindungseinheit (211) zum Herstellen
                     einer ersten Verbindung zu einem Endgerät
                     (180),
                 •   eine Empfangseinheit (212) zum Empfangen
                     einer aktuellen Konfiguration des Endgeräts
                     (180) von dem Endgerät (180),
                 •   eine Übertragungseinheit (213) zum Weiterleiten der aktuellen Konfiguration des Endgeräts
                     (180) von der ersten Basisstation (110, 210) zu
                     einer zweiten Basisstation (120) über eine terrestrische Schnittstelle (115), und
                 •   eine Speichereinheit (214) zum Speichern von
                     Konfigurationsparametern      des     Endgeräts
                     (180), die eine Standardkonfiguration darstellen,

             gekennzeichnet durch

                                           10

              das Weiterleiten der aktuellen Konfigurationsinformation des Endgeräts durch das Weiterleiten lediglich der Konfigurationsparameter, die von der Standardkonfiguration abweichen.


Die Klägerin macht den Nichtigkeitsgrund der fehlenden Patentfähigkeit, hier fehlende Neuheit und erfinderische Tätigkeit geltend. Darüber hinaus ist sie der Ansicht, der Patentanspruch 11 sei wegen des Nichtigkeitsgrunds der unzulässigen
Erweiterung für nichtig zu erklären.

Die Klägerin stützt ihr Vorbringen u. a. auf folgende Dokumente:

Kurzzeichen

 N3           WO 2009/024603 A1
              Tdoc R2-062904, „Use of AS-configuration upon handover and connec-NK1          tion establishment“, Samsung, 3GPP TSG-RAN3 Meeting #55, Seoul, Korea, 9.-13. Oktober 2006
              Tdoc R2-062887, „LTE Handover preparation“, Huawei, 3GPP TSG-RAN
 NK2
              WG2 Meeting #55, Seoul, Korea, 9.-13. Oktober 2006
              Tdoc R2-062235, „LTE Handover preparation“, Huawei, 3GPP TSG-RAN
      NK2a
              WG2 Meeting #54, Tallinn, Estland, 28. August bis 1. September 2006
              R3-060038, „Intra-AS handover procedure in LTE-ACTIVE mode with
 NK3          CPS“, CATT, 3GPP TSG RAN WG3 Meeting #50, …, Frankreich, 10.-
              12.1.2006
              Tdoc R2-073416, „Recap of handover procedure, control plane aspects
 NK4          (with TP)“, Samsung, 3GPP TSG-RAN2 #59, Athen, Griechenland, 20.-24.
              August 2007
           Tdoc R2-072629, „Recap of handover procedure, control plane aspects
      NK4d (with TP)“, Samsung, 3GPP TSG-RAN2 Meeting #58bis, Orlando, U.S.A.,
           25.-29. Juni 2007
              R2-073009, „Change Request, 36.300 CR DRAFT, rev -, Current version:
 NK5
              8.1.0“, 3GPP TSG-RAN2 Meeting #58bis, Orlando, USA, 25.-29. Juni 2007
              E-Mail des Autors der NK5 an die Arbeitsgruppe 3GPP TSG RAN WG2, Au-NK5a
              gust 2007

                                            11

             R2-071285, „DRX parameters in LTE“, 3GPP TSG-RAN WG2 Meeting
 NK6
             #57bis, St. Julian’s, Malta, 26.-30. März 2007
             Tdoc R2-072617, „E-UTRA RRC working assumptions & open issues“,
 NK7         Rapporteur (Samsung), 3GPP TSG-RAN2 Meeting #58bis, Orlando, USA,
             25.-29. Juni 2007
             3GPP2 C.S0024-A, Version 2.0, „cdma2000 High Rate Packet Data Air In-NK8
             terface Specification“, 3GPP2, Juli 2005
             3GPP2 SC.R1002-0, Version 1.0, „Publication Numbering Guidelines”, 12.
    NK8b
             Februar 2004
             „CDMA2000 Evolution System Concepts and Design Principles“, Kamran
    NK8c
             Etemad, 2004
             3GPP2 C.S0024-A, Version 3.0, „cdma2000 High Rate Packet Data Air In-NK8d
             terface Specification“, 3GPP2, September 2006
             3GPP2 A.S0008-A v2.0, „Interoperability Specification (IOS) for High Rate
 NK9         Packet Data (HRPD) Radio Access Network Interfaces with Session Control in the Access Network“, 3GPP2, April 2007
 NK10        EP 1 909 521 A1



Die Klägerin beantragt,

        das europäische Patent 2 181 559 mit Wirkung für das Hoheitsgebiet
        der Bundesrepublik Deutschland im Umfang der Patentansprüche 1,
        5, 6, 7, 10 und 11 für nichtig zu erklären.


Die Beklagte beantragt,

        die Klage abzuweisen, soweit sie sich auch gegen die Fassung
        der angegriffenen Patentansprüche des Streitpatents nach dem
        Hauptantrag aus der Widerspruchsbegründung mit Schriftsatz
        vom 27. September 2023 richtet,

        hilfsweise, die Klage abzuweisen,
        soweit sie sich auch gegen eine der Fassungen des Streitpatents
        nach den mit Schriftsatz vom 27. September 2023 eingereichten

                                             12

       Hilfsanträgen 1 und 2 sowie den mit Schriftsatz 11. April 2024 eingereichten Hilfsanträgen 3A und 3 und den in der mündlichen Verhandlung eingereichten Hilfsantrag 2A richtet,

       mit der Maßgabe, dass die Hilfsanträge in der Reihenfolge 2A, 2, 3A,
       3 und 1 geprüft werden sollen und

       alle Anträge jeweils als geschlossener Anspruchssatz gestellt werden.


Die Beklagte tritt dem Vorbringen der Klägerin in allen Punkten entgegen und verteidigt das Streitpatent beschränkt mit dem gegenüber der erteilten Fassung geänderten Hauptantrag vom 27. September 2023. Sie hält die Gegenstände der Patentansprüche 1 und 11 in der gemäß Schriftsatz vom 27. September 2023 mit geändertem Hauptantrag beschränkt verteidigten Fassung, in der zudem der Patentanspruch 10 gestrichen ist, für rechtsbeständig. Gleiches gelte für die verbliebenen
Unteransprüche.


Die Patentansprüche 1 und 11 lauten nach Hauptantrag gemäß Schriftsatz vom
27. September 2023:

 1.   A method for handing over a User Equipment (180) from a first base station (110) to a
      second base station (120) of a cellular telecommunication network (100), in
      particularwherein the first base station (110) is from a first eNodeB (110) to and the
      second base station (120) is a second eNodeB (120) of a Long Term Evolution network
      (100), the method comprising
       • establishing a first connection (110a) between the User Equipment (180) and the
          first base station (110),
       • arranging a current configuration of the User Equipment (180) with the first base
          station (110),
       • forwarding the current configuration of the User Equipment (180) from the first
          base station (110) to the second base station (120) via a terrestrial interface (115),
       • establishing a second connection (120a) between the User Equipment (110) and
          the second base station (120), and
       • reusing the forwarded configuration of the User Equipment (180) at least partially
          for the operation of the User Equipment (180), when the User Equipment (180) is
          served by the second base station (120),

                                            13

     characterized by

     –    a set of configuration parameters of the User Equipment (180) is known by the first
          base station (110) and the second base station (120) as a default configuration, and
     −   the current configuration of the User Equipment (180) is forwarded from the first base
         station (110) to the second base station (120) by solely forwarding configuration parameters, which deviate from the default configuration, and
     −   wherein the current configuration is forwarded via an X2 interface (115).


 11. A first base station for a cellular telecommunication network (100), wherein the first
     base station (110) is a first eNodeB (110 of a Long Term Evolution network (100), the
     first base station (110, 210) comprising
     •   a connection unit (211) for establishing a first connection to a User Equipment
         (180),
     •   a receiving unit (212) for receiving a current configuration of the User Equipment
         (180) from the User Equipment (180),
     •   a transmission unit (213) for forwarding the current configuration of the User
     •   Equipment (180) from the first base station (110, 210) to a second base station
         (120) via a terrestrial interface (115), wherein the second base station (120) is a
         second eNodeB (120) of the Long Term Evolution network (100), and
     •   a memory unit (214) for storing configuration parameters of the User Equipment
         (180), which configuration parameters represent a default configuration,

     characterized by

     forwarding the current configuration information of the User Equipment by solely
     forwarding configuration parameters which deviate from the default configuration,
     wherein the current configuration is forwarded via an X2 interface (115).


Wegen des Wortlauts der Patentansprüche 1 und 11 nach Hilfsantrag 2A wird auf
den Urteilstenor Bezug genommen. Wegen des Wortlauts der Patentansprüche
nach den weiteren Hilfsanträgen wird auf die Akte verwiesen.


Die Klägerin ist der Ansicht, der Patentanspruch 11 gemäß Hauptantrag vom
27. September 2023 sei nicht ursprungsoffenbart und unzulässig erweitert.

                                        14

Patentanspruch 1 in der Fassung des geänderten Hauptantrags sei insbesondere
nicht neu gegenüber den Dokumenten NK4 und NK10. Darüber hinaus beruhe der
Gegenstand des Patentanspruchs 1 nach dem geänderten Hauptantrag ausgehend
von den genannten Schriften zumindest nicht auf einer erfinderischen Tätigkeit. Die
Fachperson werde, ausgehend insbesondere von den Dokumenten NK8 und NK9
in Kombination mit dem Fachwissen, zum angegriffenen Erfindungsgegenstand gelangen. Gleiches gelte für die beschränkte Fassung des Patentanspruchs 11 nach
dem geänderten Hauptantrag.


Die Beklagte tritt der Argumentation der Klägerin entgegen und ist der Auffassung,
der Gegenstand des Streitpatents gemäß den angegriffenen Patentansprüchen in
der eingeschränkt verteidigten Fassung nach dem geänderten Hauptantrag sei zulässig, gegenüber dem Stand der Technik neu und beruhe auch auf einer erfinderischen Tätigkeit. Der Gegenstand des Streitpatents sei auch in den Fassungen nach
den Hilfsanträgen ursprungsoffenbart und wenigstens in einer der verteidigten Fassungen nach den Hilfsanträgen patentfähig.


Die Klägerin tritt auch den Hilfsanträgen entgegen und sieht auch hier die Gegenstände in Bezug auf Patentanspruch 11 jeweils als unzulässig erweitert und insgesamt als nicht patentfähig.


Der Senat hat den Parteien einen qualifizierten Hinweis vom 1. Februar 2024 zugeleitet und hierin Fristen zur Stellungnahme auf den Hinweis und auf etwaiges Vorbringen der jeweiligen Gegenpartei gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, auf das Protokoll der mündlichen Verhandlung vom 22. Januar 2025 sowie den weiteren Akteninhalt Bezug genommen.

                                          15




                           Entscheidungsgründe


                                          A.


Auf die zulässige Klage ist das Streitpatent, soweit angegriffen, teilweise für nichtig
zu erklären.

Das Streitpatent im angegriffenen Umfang der erteilten Patentansprüche 1, 5, 6, 7,
10 und 11 ist, nachdem es jedenfalls auch in einer zulässigerweise eingeschränkten
Fassung verteidigt wird, ohne Sachprüfung für nichtig zu erklären, soweit die Beklagte es nicht mehr verteidigt (vgl. BGH, Urteil vom 19. Dezember 2006 –
X ZR 236/01, GRUR 2007, 404 Rn. 15 – Carvedilol II).

Auch darüber hinaus ist die Klage insoweit begründet, als dem Streitpatent im angegriffenen Umfang in der eingeschränkt verteidigten Fassung nach dem geänderten Hauptantrag vom 27. September 2023 der Nichtigkeitsgrund der mangelnden
Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a)
EPÜ i. V. m. Art. 52, 56 EPÜ entgegensteht.

In der Fassung nach dem Hilfsantrag 2A erweist sich das Patent im angegriffenen
Umfang hingegen als schutzfähig, so dass die Klage, soweit sie sich auch gegen
diese Fassung richtet, abzuweisen ist.

Auf die Frage, ob das Streitpatent auch in der Fassung nach den weiteren Hilfsanträgen Bestand hätte, kommt es bei dieser Sachlage nicht mehr an.




           I.   Zum Streitpatent, zur Aufgabe, zur Fachperson, zur
                    Merkmalsgliederung und zur Auslegung


1.    Gegenstand des Streitpatents ist das Gebiet der Telekommunikationstechnologie, insbesondere die Übergabe eines Endgeräts (auch als Nutzergerät / user

                                          16

equipment / UE bezeichnet) von einer ersten an eine zweite Basisstation (in einem
LTE-System als „eNodeB“ bezeichnet) in einem Mobilfunknetz. Eine solche Übergabe wird als Handover (oder auch als Handoff) bezeichnet (Streitpatent, Abs.
0001, 0003).


Dabei nimmt das Streitpatent auf Long Term Evolution (LTE) Systeme Bezug (Abs.
0002) und geht davon aus, dass in einem LTE-System keine zentrale Steuerung
des Handover vorhanden sei, die sicherstelle, dass die an einem Handover beteiligten Basisstationen die aktuelle Messkonfiguration des Endgeräts kennen. Aus
diesem Grund müsse die aktuelle Messkonfiguration vom Endgerät an die neue
bzw. Ziel-Basisstation über die Funk-Schnittstelle gesendet werden. Nachteilig sei
dabei, dass dadurch die Datenlast der Funk-Schnittstelle erhöht werde (Absatz
0003, 0005).



2.     Dem Streitpatent ist die Aufgabe zu entnehmen, ein effektives Verfahren zur
Verfügung zu stellen, mit dem Konfigurationsparameter von einer ersten (Quellen-)
Basisstation an eine zweite (Ziel-)Basisstation beim Handover eines Nutzergeräts
von der ersten an die zweite Basisstation eines Mobilfunknetzes signalisiert werden
können (Absätze 0006 und 0009).



3.     Die maßgebliche Fachperson verfügt über einen Universitätsabschluss als
Master of Science oder Diplomingenieur der Fachrichtungen Nachrichten- oder Informationstechnik sowie mehrjährige Berufserfahrung auf dem Gebiet der Entwicklung des LTE-Mobilfunksystems. Sie ist mit den Normen und Standards auf diesem
Gebiet vertraut und verfolgt die laufenden Standardisierungsbemühungen.



4.     Das Streitpatent weist auch in der von der Beklagten verteidigten Fassung
nach dem geänderten Hauptantrag die beiden unabhängigen Patentansprüche 1
und 11 auf. Der Patentanspruch 1 ist auf ein Verfahren (method), der Patentanspruch 11 ist auf eine erste Basisstation (first base station) gerichtet.

                                            17

4.1      Der Patentanspruch 1 in der Fassung nach dem gegenüber der erteilten Fassung geänderten Hauptantrag vom 27. September 2023 lautet mit senatsseitig hinzugefügter Gliederung (Änderungen gegenüber der erteilten Fassung hervorgehoben):


 1.1H     A method for handing over a User Equipment (180) from a first base station (110) to a second base station (120) of a cellular telecommunication
          network (100), in particular from wherein the first base station (110) is a
          first eNodeB (110) to and the second base station (120) is a second
          eNodeB (120) of a Long Term Evolution network (100), the method comprising
 1.1.1    • establishing a first connection (110a) between the User Equipment (180)
          and the first base station (110),
 1.1.2    • arranging a current configuration of the User Equipment (180) with the
          first base station (110),
 1.1.3    • forwarding the current configuration of the User Equipment (180) from
          the first base station (110) to the second base station (120) via a terrestrial
          interface (115),
 1.1.4    • establishing a second connection (120a) between the User Equipment
          (110) and the second base station (120), and
 1.1.5    • reusing the forwarded configuration of the User Equipment (180) at least
          partially for the operation of the User Equipment (180), when the User
          Equipment (180) is served by the second base station (120),
          characterized by
 1.2      - a set of configuration parameters of the User Equipment (180) is known
          by the first base station (110) and the second base station (120) as a default configuration, and
 1.3      - the current configuration of the User Equipment (180) is forwarded from
          the first base station (110) to the second base station (120) by solely forwarding configuration parameters, which deviate from the default configuration, and
 1.4H     - wherein the current configuration is forwarded via an X2 interface (115).


4.2      In der Fassung des geänderten Hauptantrags hat die Beklagte die angegriffenen Patentansprüche 5, 6 und 7 unverändert gegenüber der erteilten Fassung
gelassen. Der Patentanspruch 10 nach Streitpatent (dessen Inhalt sie als Merkmal
1.4H in den Patentanspruch 1 in der Fassung des geänderten Hauptantrags aufgenommen hat) entfällt.

                                            18



4.3      Der Patentanspruch 11 lautet in der Fassung nach dem gegenüber der erteilten Fassung geänderten Hauptantrag (Änderungen gegenüber der erteilten Fassung hervorgehoben; Gliederung hinzugefügt):


 11.1H      A first base station for a cellular telecommunication network (100), wherein
            the first base station (110) is a first eNodeB (110[!sic] of a Long Term Evolution network (100), the first base station (110, 210) comprising
 11.1.1     • a connection unit (211) for establishing a first connection to a User Equipment (180),
 11.1.2     • a receiving unit (212) for receiving a current configuration of the User
            Equipment (180) from the User Equipment (180),
 11.1.3H • a transmission unit (213) for forwarding the current configuration of the
         User Equipment (180) from the first base station (110, 210) to a second
         base station (120) via a terrestrial interface (115), wherein the second base
         station (120) is a second eNodeB (120) of the Long Term Evolution network
         (100), and
 11.1.4     • a memory unit (214) for storing configuration parameters of the User
            Equipment (180), which configuration parameters represent a default configuration,
            characterized by
 11.2       forwarding the current configuration information of the User Equipment by
            solely forwarding configuration parameters which deviate from the default
            configuration,
 11.3H      wherein the current configuration is forwarded via an X2 interface (115).




5.       Die Merkmale der Patentansprüche 1 und 11 – in der Fassung des geänderten Hauptantrags vom 27. September 2023 – bedürfen der näheren Erläuterung.


5.1      Patentanspruch 1 gemäß geändertem Hauptantrag ist auf ein Handover-Verfahren gerichtet, bei dem das Endgerät eines Nutzers (user equipment) von einer ersten an eine zweite Basisstation eines Mobilfunknetzes übergeben wird. Bei
der ersten und zweiten Basisstation handelt es sich jeweils um eine als „eNodeB“
bezeichnete Basisstation eines „Long Term Evolution“ (LTE-)Netzwerks (Merkmal
1.1H). Das Streitpatent ist damit in der Fassung des geänderten Hauptantrags vom

                                          19

27. September 2023 gegenüber der erteilten Anspruchsfassung auf ein Verfahren
in einem LTE-Mobilfunksystem beschränkt.

Das Verfahren umfasst das Herstellen einer ersten Verbindung zwischen dem Endgerät und der ersten Basisstation (Merkmal 1.1.1) und das Einrichten einer aktuellen Konfiguration (arranging a current configuration) des Endgeräts (of the User
Equipment) mit der ersten Basisstation (with the first base station) (Merkmal 1.1.2).
Beide Schritte versteht die Fachperson als Schritte zum Aufbau einer ersten Mobilfunkverbindung mit dem Endgerät, die im Zusammenwirken mit der ersten Basisstation des Mobilfunknetzes erfolgen.

Die Formulierung „arranging a current configuration“ in der Verfahrenssprache Englisch ist als das Einrichten einer entsprechenden Konfiguration zu verstehen. Für
ein „Vorbereiten einer aktuellen Konfiguration des Endgeräts in der ersten Basisstation“ (Übersetzung gemäß Streitpatent) finden sich in der Beschreibung keine Anhaltspunkte. Daher versteht die Fachperson die Formulierung „arranging … with the
first base station“ dahingehend, dass neben dem Endgerät auch die erste Basisstation an der Einrichtung der Konfiguration beteiligt ist, ohne dass näher angegeben
ist, worin deren Beitrag liegt.

Der Begriff „arranging“ im Merkmal 1.1.2 ist auch nicht aufgrund der Formulierung
des Patentanspruchs 11 und der Ausführungsbeispiele als „Empfangen“ auszulegen. Unabhängig davon, dass das Streitpatent im Merkmal 1.1.2 im Patentanspruch
1 bewusst eine andere Formulierung als im Patentanspruch 11 wählt, sieht das
Streitpatent auch vor, dass eine neue (zweite) Basisstation Werte der Messkonfiguration des Endgeräts ändern kann (Abs. 0027). Da das Verfahren gemäß dem Absatz 0049 des Streitpatents ausdrücklich für einen (weiteren) Handover zu einer
weiteren (dritten) Basisstation geeignet sein soll, also nicht auf einen einzigen, einmaligen Handover beschränkt ist, ist dem Streitpatent zumindest für diesen Fall zu
entnehmen, dass die Konfiguration nicht allein durch das Endgerät festgelegt wird.
Eine beschränkende Auslegung des Patentanspruchs 1 unter seinem Wortlaut ist
daher auch aufgrund des präsenten Fachwissens der Fachperson zum LTE-Stan-

                                          20

dard nicht geboten, zumal es sich bei dem von den Parteien hierzu diskutierten Dokument NK5 nicht um einen Teil des LTE-Standards, sondern (nur) um einen Änderungsvorschlag zu einer technischen Spezifikation handelt.

Als Beispiele einer aktuellen Konfiguration (current configuration) eines Endgeräts
diskutiert das Streitpatent

-   eine Messkonfiguration, welche die Messverfahren beschreibt, die das Endgerät
    durchführt (Abs. 0019: …the current configuration is a measurement configuration of the User Equipment characterizing measurement procedures which are
    performed by the User Equipment.), sowie

-   Aktivitätsdaten des Endgeräts, welche aktive Perioden des Endgeräts beschreiben (Abs. 0022: …the current configuration comprises activity data of the User
    Equipment, which activity data determine activity times of the User Equipment.
    Thereby, the activity times itself might define time periods, during which the User
    Equipment is deactivated for transmitting radio wave signals to a base station
    and/or for receiving radio wave signals from a base station.),

wobei in einer Ausführungsform die Aktivitätsdaten des Endgeräts einen Teil einer
Messkonfiguration bilden (Abs. 0045).

Der Patentanspruch 1 ist nicht auf die Konfiguration von Messverfahren beschränkt.
Vielmehr spricht bspw. das Merkmal 1.1.5 ganz allgemein von einer Konfiguration
zum Betrieb des Endgeräts (reusing the forwarded configuration of the User Equipment (180) at least partially for the operation of the User Equipment (180)…). Dass
es sich bei der Konfiguration um eine Messkonfiguration handeln soll, ist erst als
Ausgestaltung gemäß dem Unteranspruch 5 beansprucht (…the current configuration is a measurement configuration…). Selbst in diesem Fall, wenn die genannten
Aktivitätsdaten – soweit vorhanden – als Bestandteile der Messkonfiguration vorgesehen sind, sind diese nicht zwingend mit einem bestimmten Messverfahren (bspw.
einer Inter-Frequenz-Messung) verknüpft, da das Streitpatent solche Messverfahren nur beispielgebend nennt (vgl. Abs. 0021: …might also comprise a so called
inter-frequency measurement…; Abs. 0047: …might also be related to… [Unterstreichung ergänzt]).

                                         21

Auch wenn das Streitpatent Aktivitätsdaten, welche die sogenannte „Discontinuous
Reception“ bzw. „Discontinuous Transmission“ anhand von DRX- bzw. DTX-Intervallen beschreiben sollen (Abs. 0022, 0023), nur hinsichtlich ihrer Bedeutung für
Messungen näher betrachtet, sind die DRX/DTX-Intervalle originär kein Teil einer
Messkonfiguration, sondern der Konfiguration des Betriebs des Endgeräts bzw. seiner Kommunikationsschnittstellen. Hierbei bestimmt die Konfiguration der Aktivität
bzw. Inaktivität des Endgeräts (DRX/DTX-Intervalle) ganz allgemein die Sende- und
Empfangseigenschaften des Endgeräts, wie dies das Streitpatent in den Absätzen
0015 und 0023 ebenso allgemein und unabhängig von möglichen Messungen beschreibt. Zeiten der Inaktivität des Endgeräts können zwar Auswirkungen auf die
Messungen gemäß einer Messkonfiguration oder auf die Übertragung von Messberichten haben. Dies macht die Aktivitätsdaten jedoch nicht bereits zu einem Teil
einer „Messkonfiguration“ (die entsprechend Merkmal 1.1.3 zwischen den Basisstationen als aktuelle Konfiguration übertragen wird). Allerdings ist der Patentanspruch
1 weder auf Messverfahren beschränkt, noch ergibt sich aus dem Patentanspruch
1 eine entsprechende zeitliche Abhängigkeit, die ihren Niederschlag in der beim
Handover übermittelten Konfiguration gefunden hätte.

Die nach Merkmal 1.1.2 eingerichtete aktuelle Konfiguration des Endgeräts wird von
der ersten an die zweite Basisstation weitergeleitet, wobei dies über eine „terrestrische“ Schnittstelle erfolgt (Merkmal 1.1.3). Unter einer terrestrischen Schnittstelle
versteht das Streitpatent vorzugsweise eine elektrische oder optische Kabelverbindung zwischen den beiden Basisstationen des Mobilfunknetzes, wobei es sich nach
der Definition in Absatz 0013 des Streitpatents um jegliche Kommunikationsverbindung zwischen zwei räumlich festen Punkten handeln kann, und somit nicht auf eine
kabelgebundene Verbindung beschränkt ist, zumal der Fachperson bekannt ist,
dass Basisstationen eines Mobilfunknetzes oftmals über Richtfunkverbindungen
miteinander verbunden sind (Abs. 0013: The term terrestrial interface refers to any
communication connection between two spatially fixed points. Preferably, a terrestrial interface comprises an electrical and/or an optical cable, which extends between the first base station and the second base station.).

                                         22

Das Verfahren sieht weiter vor, dass eine zweite Verbindung zwischen dem Endgerät und der zweiten Basisstation hergestellt wird (Merkmal 1.1.4), wobei die weitergeleitete Konfiguration des Endgeräts zumindest teilweise für den Betrieb des Endgeräts wiederverwendet wird, wenn das Endgerät durch die zweite Basisstation bedient wird (Merkmal 1.1.5). Diese zweite Verbindung wird im Streitpatent auch als
zweiter Übertragungsweg bezeichnet (second transmission path; vgl. Bezugszeichenliste).

Das Verfahren ist dadurch gekennzeichnet, dass ein Satz Konfigurationsparameter
des Endgeräts beiden Basisstationen, also der ersten und zweiten Basisstation, als
eine Standardkonfiguration (default configuration) bekannt ist (Merkmal 1.2). Die
Fachperson versteht diese Standardkonfiguration als einen Parametersatz, der den
beiden Basisstationen vorab bekannt ist. Der Umfang und Inhalt der Standardkonfiguration ist im Patentanspruch 1 nicht festgelegt. Das Streitpatent beschreibt zur
Standardkonfiguration nur mögliche Ausgestaltungen, nach denen diese von einem
Dienst oder einer Dienstklasse (service or service class) abhängig sein kann, wobei
längere oder kürzere Zeiten der Inaktivität des Endgeräts bspw. abhängig von der
Art der Kommunikation (Sprache oder Internet) gewählt werden können. Die Standardkonfiguration kann bspw. als hierarchische Datenstruktur realisiert werden (hierarchical data structure) (Abs. 0014-0017).

Die aktuelle Konfiguration des Endgeräts, die gemäß dem Merkmal 1.1.3 von der
ersten an die zweite Basisstation weitergeleitet wird, wird gemäß dem Merkmal 1.3
insoweit weitergeleitet, als dass lediglich die von der Standardkonfiguration (default
configuration) abweichenden Konfigurationsparameter weitergeleitet werden („by
solely forwarding configuration parameters, which deviate from the default configuration“ [Unterstreichung ergänzt]). Die Formulierung des Merkmals 1.3 versteht die
Fachperson als ausschließliches Weiterleiten von Parametern, die von der Standardkonfiguration abweichen, was im Umkehrschluss bedeutet, dass keine der
Standardkonfiguration entsprechenden Parameter weitergeleitet werden. Das Weiterleiten eines Konfigurationsparameters, der von einer Standardkonfiguration abweicht, erfüllt nicht alleine bereits Merkmal 1.3. Denn die Weiterleitung dieses Parameters sagt nichts darüber aus, wie mit Konfigurationsparametern verfahren wird,

                                         23

die der Standardkonfiguration entsprechen, d. h. ob diese ebenfalls weitergeleitet
werden oder entsprechend Merkmal 1.3 nicht weitergeleitet werden.

Die Weiterleitung der aktuellen Konfiguration, also das Weiterleiten der Konfigurationsparameter von der ersten an die zweite Basisstation, erfolgt über eine X2-
Schnittstelle (Merkmal 1.4H). Bei der X2-Schnittstelle handelt es sich nach Angabe
des Streitpatents um eine für LTE-Netzwerke standardisierte und bereits bestehende Schnittstelle zwischen benachbarten Basisstationen (Abs. 0029: …the current configuration is forwarded via an X2 interface. This may provide the advantage
that in case the above described method is carried out within an LTE network, a
standardized interface between neighboring eNodeBs, which interface already exists, can be employed.), wobei der Begriff „X2 interface“ nicht einen Anschluss im
Sinne einer Hardware-Komponente, sondern ein Übertragungsprotokoll für die Verbindung zwischen zwei Basisstationen in LTE-Netzwerken bezeichnet.


5.2   Der Patentanspruch 11 gemäß geändertem Hauptantrag ist auf eine erste
Basisstation eines Mobilfunknetzwerks gerichtet, wobei es sich um einen „eNodeB“
eines LTE-Netzwerks, also um eine Basisstation eines „Long Term Evolution“ (LTE-
)Netzwerks handelt (Merkmal 11.1H).

Die erste Basisstation umfasst eine Verbindungseinheit zum Herstellen einer ersten
Verbindung zu einem Endgerät (Merkmal 11.1.1) und eine Empfangseinheit zum
Empfangen einer aktuellen Konfiguration des Endgeräts von dem Endgerät (Merkmal 11.1.2). Hierin besteht ein Unterschied zum Verfahrensanspruch 1, da der Patentanspruch 11 vorsieht, dass Mittel der Basisstation vorgesehen sind, um eine
aktuelle Konfiguration des Endgeräts von diesem Endgerät zu empfangen (receiving a current configuration of the User Equipment from the User Equipment) und
gemäß dem Merkmal 11.1.3H diese aktuelle Konfiguration des Endgeräts weiterzuleiten (…for forwarding the current configuration of the User Equipment…). Diesen
Angaben entnimmt die Fachperson, dass die „aktuelle Konfiguration“ weder ganz
noch teilweise durch die anspruchsgemäße Basisstation festgelegt wird, sondern
durch diese (nur) empfangen und weitergeleitet wird. Ob die „aktuelle Konfiguration“
zwischen dem Endgerät und der Basisstation zu einem früheren Zeitpunkt vorab

                                         24

ausgehandelt wurde, spielt hierbei keine Rolle, da der Patentanspruch 11 nur auf
die Eignung zum Empfangen der weiterzuleitenden aktuellen Konfiguration abstellt,
deren Ursprung dabei im Endgerät und nicht in der Basisstation liegt. Ein Hinweis
darauf, dass sich die nach dem Merkmal 11.1.2 zu empfangende aktuelle Konfiguration von der weiterzuleitenden aktuellen Konfiguration nach dem Merkmal 11.1.3H
in Umfang oder Inhalt unterscheidet, ergibt sich aus dem Anspruchswortlaut oder
der Beschreibung des Streitpatents nicht (bspw. Abs. 0031, 0042, 0051). Selbst im
Hinblick auf mögliche weitere Konfigurationsdaten des Endgeräts spricht das Streitpatent in einer Ausgestaltung nur davon, dass es sich um Daten handelt, die vom
Endgerät abgerufen werden (Abs. 0018: …further configuration data are retrieved
from the User Equipment…), jedoch nicht davon, dass die „aktuelle Konfiguration“
durch die Basisstation festgelegt oder ergänzt wird, oder dass es sich dabei ganz
oder teilweise um Daten handelt, die bereits in der Basisstation vorliegen, da sie zu
einem früheren Zeitpunkt erfasst oder ausgehandelt wurden.

Wie auch der Patentanspruch 1 sieht der Patentanspruch 11 weiter vor, dass die
nach dem Merkmal 11.1.2 vorliegende aktuelle Konfiguration für das Endgerät von
der ersten Basisstation an eine zweite Basisstation weitergeleitet wird, wobei dies
über eine terrestrische Schnittstelle erfolgt (Merkmal 11.1.3H). Nach dem Merkmal
11.1.3H handelt es sich bei der weiterzuleitenden aktuellen Konfiguration um die
nach dem Merkmal 1.1.2. empfangene aktuelle Konfiguration (…forwarding the current configuration…). Dass auch die zweite Basisstation gemäß dem Merkmal
11.1.3H ein „eNodeB“, also Teil eines LTE-Netzwerks ist, charakterisiert dabei die
erste Basisstation nur insoweit, als dass die Übertragungseinheit zur Kommunikation über die terrestrische Verbindung mit einer weiteren Basisstation innerhalb des
LTE-Netzwerks geeignet sein muss.

Weiter ist für die erste Basisstation eine Speichereinheit zum Speichern von Konfigurationsparametern des Endgeräts vorgesehen, die eine Standardkonfiguration
(default configuration) repräsentieren (Merkmal 11.1.4). Das Merkmal ist damit nur
auf das Vorhalten der Konfigurationsparameter gerichtet, welche die Standardkonfiguration bilden.

                                         25

Die erste Basisstation ist dadurch charakterisiert, dass das Weiterleiten der aktuellen Konfigurationsinformation des Endgeräts (an eine zweite Basisstation gemäß
dem Merkmal 11.1.3H) dadurch erfolgt, dass lediglich die Konfigurationsparameter
weitergeleitet werden, die von der Standardkonfiguration abweichen (Merkmal
11.2), wobei das Weiterleiten der aktuellen Konfiguration über eine X2-Schnittstelle
erfolgt (Merkmal 11.3H). Dies entspricht inhaltlich den Merkmalen 1.3 und 1.4H des
Verfahrensanspruchs 1.




        II.   Zum Nichtigkeitsgrund der unzulässigen Erweiterung
                 sowie der fehlenden Ursprungsoffenbarung


Der Gegenstand des Streitpatents soweit angegriffen erweist sich in der Fassung
nach geändertem Hauptantrag vom 27. September 2023 als zulässig.


1.    Die Änderungen in den Patentansprüchen 1 und 11 gemäß der Fassung
nach geändertem Hauptantrag sind den ursprünglichen Unterlagen (PCT-Anmeldung, veröffentlicht als WO 2009/024603 A1, Anlage N3) zu entnehmen.


1.1   Die Beschränkung auf Basisstationen (eNodeB) eines LTE-Netzwerks in der
Fassung nach geändertem Hauptantrag (Merkmale 1.1H, 11.1.1H, 11.1.3H) basiert
auf dem fakultativen Merkmal des ursprünglichen Patentanspruchs 1 der PCT-Anmeldung.


1.2   Die Konkretisierung der Weiterleitung durch die Verwendung einer X2-
Schnittstelle gemäß dem Merkmal 1.4H des Patentanspruchs 1 bzw. 11.3H des Patentanspruchs 11 gemäß geändertem Hauptantrag (wherein the current configuration is forwarded via an X2 interface (115)) basiert auf Seite 8, Zeilen 16 bis 17,
Figur 1 mit Beschreibung auf Seite 10, Zeilen 25 bis 30, und dem Patentanspruch
10 der PCT-Anmeldung.


1.3   Die Streichung des Merkmals „wherein the current configuration is suitable
for to be reused at least partially for the operation of the User Equipment (180),

                                        26

when the User Equipment (180) is served by the second base station (120)“ der
ursprünglichen Fassung des Patentanspruchs 11 stellt keine unzulässige Erweiterung gegenüber der Ursprungsoffenbarung dar.

Das gegenüber der Anmeldung gestrichene Merkmal hat die erste Basisstation –
auf welche der Patentanspruch 11 gerichtet ist – nicht charakterisiert, da es (nur)
die weitere Verwendung der weitergeleiteten Parameter durch das Endgerät in seiner Verbindung mit der zweiten Basisstation beschreibt. Eine Auslegung, nach der
die erste Basisstation nach Streichung dieses Merkmals nunmehr auch eine nicht
zumindest in Teilen wiederverwendbare „aktuelle Konfiguration“ des Endgeräts –
mithin eine vollständig ungeeignete Konfiguration – weiterleiten könne, ist unangebracht, da die Fachperson bei der „aktuellen Konfiguration“ von einer zumindest in
Teilen „geeigneten“ Konfiguration für den Betrieb des Endgeräts ausgeht. Denn bei
dieser „aktuellen Konfiguration“ handelt es sich um eine Konfiguration, die zum Betrieb des Endgeräts in einer ersten Zelle und für eine aktive Verbindung zwischen
dem Endgerät und der ersten Basisstation geeignet ist, wenn das Endgerät von der
ersten Basisstation bedient wird. Da das Endgerät und die erste Basisstation – wie
auch die zweite Basisstation – einem gemeinsamen Standard eines LTE-Netzwerks
genügen, kann die „aktuelle Konfiguration“ auch als Konfiguration für das Endgerät,
wenn es von der zweiten Basisstation bedient wird, nicht vollständig ungeeignet
sein.


1.4     Das Hinzufügen des Merkmals 11.2 „forwarding the current configuration information of the User Equipment by solely forwarding configuration parameters
which deviate from the default configuration“ in den Patentanspruch 11 stellt keine
unzulässige Erweiterung gegenüber der Ursprungsoffenbarung dar.

Grundlage des auf die erste Basisstation gerichteten Patentanspruchs 11 ist Seite
8, Zeile 33 bis Seite 9, Zeile 10 der veröffentlichten PCT-Anmeldung. Die Eignung
der ersten Basisstation zur Weiterleitung der aktuellen Konfiguration an die zweite
Basisstation (Punkt (c)) steht dort in keinem Zusammenhang damit, ob zwischen
dem Endgerät und der zweiten Basisstation bereits eine Verbindung aufgebaut
wurde oder nicht. Dies kann nicht überraschen, da der Aufbau einer Verbindung

                                         27

zwischen Endgerät und zweiter Basisstation keine Eigenschaft oder Fähigkeit der
ersten Basisstation ist.

Der Verweis auf der Seite 13, Zeilen 7 bis 13 der veröffentlichten Anmeldung, wonach das Weiterleiten der aktuellen Konfiguration im Rahmen der Handover-Vorbereitung durchgeführt werde und daher die aktuelle Konfiguration nur als Grundlage
einer solchen Verbindung dienen könne, greift zu kurz, da bereits der ursprüngliche,
auf die erste Basisstation gerichteten Patentanspruch 11 (Seite 18, Zeile 6ff) nicht
auf eine Verwendung der Basisstation im Rahmen der Handover-Vorbereitung beschränkt ist. Wie die erste Basisstation bspw. im Ablauf eines Handover-Verfahrens
verwendet wird, ist außerdem keine Frage der Eigenschaften der Basisstation, sondern des Verfahrens, das sich in den Verfahrensansprüchen widerspiegelt. Zur
Durchführung bzw. zur Teilnahme an diesem Verfahren muss die erste Basisstation
nur geeignet sein (vorliegend bspw. zur Übertragung der Konfiguration eines Endgeräts). Die erste Basisstation ist aber nicht auf die Abfolge von Schritten in diesem
Verfahrensablauf zum Handover beschränkt, insbesondere nicht, wenn diese die
Fähigkeiten der beanspruchten ersten Basisstation nicht berühren. Ob in einem
Handover-Verfahren weitere Anforderungen von den Basisstationen erfüllt werden
müssen, ist hier nicht relevant, da die beanspruchte Basisstation weder in der ursprünglichen Fassung noch gemäß geändertem Hauptantrag auf diesen speziellen
Anwendungsfall beschränkt ist.

Auch, dass für einen fehlerfreien Betrieb zwischen dem Endgerät und der zweiten
Basisstation diese vorab Kenntnis von der (Mess-)Konfiguration des Endgeräts haben müsse (S. 11, Z. 26-30 bzgl. erster Basisstation), stellt keine Beschränkung der
prinzipiellen Eignung der ersten Basisstation dar, die aktuelle Konfiguration vom
Endgerät zu empfangen und an eine zweite Basisstation weiterzuleiten, wie sie ursprünglich im Patentanspruch 11 beschrieben war. Ob die Kenntnis dieser Messkonfiguration für die zweite Basisstation in einem Handover-Verfahren vor dem Verbindungsaufbau sinnvoll oder notwendig ist, oder bspw. die Default-Konfiguration
vorläufig genügen würde, ist hier nicht relevant, da die beanspruchte Basisstation
weder auf diesen speziellen Anwendungsfall des Handover, noch die aktuelle Konfiguration auf eine Messkonfiguration beschränkt ist.

                                        28


Das Merkmal 11.2, nach dem nur Abweichungen von der aktuellen zu einer Standardkonfiguration an eine zweite Basisstation übertragen werden, ist in der Ursprungsoffenbarung ebenfalls nicht vom Bestehen oder Nicht-Bestehen einer Verbindung zwischen dem Endgerät und der zweiten Basisstation abhängig (vgl. veröffentlichte PCT-Anmeldung, S. 12, letzter Absatz bis S. 13, zweiter Absatz).



2.    Die Änderungen in den Patentansprüchen 1 und 11 gemäß der Fassung
nach geändertem Hauptantrag schränken den Schutzbereich gegenüber der erteilten Fassung (Streitpatentschrift, Anlage N1) ein; ihre Gegenstände stellen kein
Aliud dar.


2.1   Die Patentansprüche 1 und 11 sind hier durch die gegenüber der erteilten
Fassung geänderten Merkmale 1.1H bzw. 11.1.1H und 11.1.3H auf Basisstationen
(eNodeB) eines LTE-Netzwerks beschränkt.


2.2   Das gegenüber der erteilten Fassung ergänzte Merkmal 1.4H bzw. 11.3H
(wherein the current configuration is forwarded via an X2 interface (115)) gemäß
geändertem Hauptantrag beschränkt den Schutzbereich des Patentanspruchs 1
bzw. 11.

Denn bei der X2-Schnittstelle (X2 interface) handelt es sich um ein Übertragungsprotokoll für die terrestrische Verbindung zwischen zwei Basisstationen in LTE-Netzwerken. Das Merkmal 11.3H bedeutet, dass die erste Basisstation zur Kommunikation über ein solches „X2 interface“ geeignet eingerichtet sein muss. Da das
Anspruchsmerkmal keine zusätzliche Komponente der Basisstation beschreibt,
sondern die Weiterleitung der aktuellen Konfiguration über eine terrestrische
Schnittstelle (vgl. Merkmal 1.4H bzw. 11.3H gemäß geändertem Hauptantrag) im
Hinblick auf ein bestimmtes Protokoll konkretisiert, ist die beanspruchte erste Basisstation in der Fassung nach geändertem Hauptantrag dahingehend beschränkt,
dass sie mit der zweiten Basisstation unter Verwendung dieses Protokolls kommuniziert. Somit führt das Merkmal 1.4H bzw. 11.3H weder zu einem Aliud, noch handelt

                                        29

es sich um eine nichtbeschränkende Zweckangabe eines Verfahrens, das in einer
anderen Entität des Netzwerks ausgeführt wird.



3.    Die angegriffenen abhängigen Patentansprüche sind im geänderten Hauptantrag vom 27. September 2023 inhaltlich gegenüber der Anmeldung und dem
Streitpatent unverändert. Der im Patentanspruch 1 als Merkmal 1.4H aufgenommene und ebenfalls angegriffene Patentanspruch 10 des Streitpatents entfällt in der
Fassung nach geändertem Hauptantrag.



4.    Die beschränkte Verteidigung des Streitpatents durch Kombination der unabhängigen Patentansprüche 1 und 11 mit den Merkmalen des abhängigen Patentanspruchs 10 der erteilten Fassung ist zulässig, da auch der erteilte Patentanspruch 10 angegriffen ist (vgl. BGH, Urteil vom 1. März 2017, X ZR 10/15 - Ankopplungssystem).




          III. Zur Patentfähigkeit des Streitpatents in der Fassung
                        nach geändertem Hauptantrag


Dem Streitpatent im angegriffenen Umfang nach dem geänderten Hauptantrag vom
27. September 2023 steht jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i.
V. m. Art. 52, 54, 56 EPÜ entgegen.

Der Gegenstand von Patentanspruch 1 in der Fassung nach Hauptantrag vom 27.
September 2023 ist der Fachperson durch den CDMA2000-HRDP-Standard nach
den Dokumenten NK8 und NK9 in Verbindung mit ihrem Fachwissen nahegelegt
und durch das Dokument NK4 (mit NK5) bekannt.

                                        30

1.    Dokument NK8 mit Dokument NK9 (jeweils CDMA2000-HRDP-Standard)

Der jeweilige Gegenstand der unabhängigen Patentansprüche 1 und 11 gemäß geändertem Hauptantrag vom 27. September 2023 ist neu gegenüber dem
CDMA2000-HRDP-Standard nach den Dokumenten NK8 und NK9. Der Gegenstand des Patentanspruchs 1 ist der Fachperson jedoch durch diesen Standard nahegelegt.


1.1   Bei dem Dokument NK8 (3GPP2 C.S0024-A, Version 2.0) handelt es sich
um einen Teil der Spezifikation des Mobilfunkstandards CDMA2000, welcher die
Funkschnittstelle des Endgeräts beschreibt. Das Dokument NK9 (3GPP2 A.S0008-
A, v2.0) ist ebenfalls Teil des Mobilfunkstandards CDMA2000. Beide Dokumente
beziehen sich auf Schnittstellen für „High Rate Packet Data“ (HRPD) in CDMA2000-
Systemen. Während das Dokument NK8 ohne Versionsangabe auf das Standarddokument A.S0008 Bezug nimmt (vgl. NK8, S. lxxxvi, [9]), nimmt das Dokument
NK9 ausdrücklich Bezug auf die Version 2.0 der Spezifikation C.S0024-A v2.0 (vgl.
NK9, S. 1-2, Kap. 1.2.1 Normative References, [10] 3GPP2: C.S0024-A v2.0,…),
also auf das Dokument NK8. Hiervon ausgehend sieht der Senat die beiden Dokumente NK8 und NK9 als gemeinsame Offenbarung des CDMA2000-HRDP-Standards in der Version 2.0 an.


1.2   Die Dokumente NK8 und NK9 offenbaren der Fachperson – ausgedrückt in
den Worten des Patentanspruchs 1 gemäß geändertem Hauptantrag –


 1.1Hteil A method for handing over a User Equipment from a first base station to
          a second base station of a cellular telecommunication network, wherein
          the first base station is a first eNodeB and the second base station is a
          second eNodeB of a Long Term Evolution network, the method comprising

                Die Dokumente NK8 und NK9 umfassen die Beschreibung eines
                Handover-Verfahrens (Handoff) eines Endgeräts (access terminal
                / AT) zwischen zwei Zugangsnetzen (access network / AN) des
                selben Paketdatenknotens (Packet Data Serving Node / PDSN)
                eines CDMA2000-HRDP-Netzwerks, wobei die Zugangsnetze jeweils durch Basisstationen (base station) gebildet werden (vgl.

                                       31

              NK9, S. 3-14, Kap. 3.7 Dormant Handoff of HRPD AT between
              ANs - Served by the Same PDSN; und Fig. 3.7.1-1; i. V. m. NK8,
              S. 1-13, Z. 23, 24, 27, 28, Kap. 1.11: An access network is equivalent to a base station in [2]. … An access terminal is equivalent
              to a mobile station in [2].).

              Den Dokumenten NK8 und NK9 fehlt – als Teile des CDMA2000-
              HRDP-Standards – der Bezug zu LTE-Basisstationen bzw. dem
              Long Term Evolution (LTE) Netzwerk.

1.1.1   • establishing a first connection between the User Equipment and the first
        base station,

              Aus der Abfrage der Sitzungszustandsinformation (HRDP session
              state information) durch das Ziel-Zugangsnetz (target AN) (vgl.
              NK9, S. 3-14 und 3-15, Abschnitte a. bis c.) folgt, dass zum Beginn
              des Handovers (handoff) eine Verbindung zwischen dem Endgerät (AT) und dem Quell-Zugangsnetz (source AN) besteht. Zudem
              bezieht sich der Begriff „HRDP session“ auf einen gemeinsamen
              Zustand von Endgerät (AT) und Zugangsnetz (AN) mit ausgehandeltem und verwendetem Protokoll und Protokollkonfigurationen
              (vgl. NK9, S. 1-6, Kap. 1.3.2 Definitions, HRPD session An HRPD
              session refers to a shared state between the AT and the AN. This
              shared state stores the protocols and protocol configurations that
              were negotiated and are used for communications between the AT
              and the AN…), wobei Basisstationen das jeweilige Zugangsnetz
              bilden (vgl. Merkmal 1.1H).

1.1.2   • arranging a current configuration of the User Equipment with the first
        base station,

              Die vorstehend zum Merkmal 1.1.1 genannte „HRDP session“ bezieht sich auf einen gemeinsamen Zustand von Endgerät (AT) und
              dem (ersten) Zugangsnetz (AN) mit ausgehandeltem und verwendetem Protokoll und Protokollkonfigurationen (vgl. NK9, S. 3-1,
              Kap. 3.1.1, Punkt a.: …Since no session exists between the AT
              and AN, a session is established where protocols and protocol
              configurations are negotiated, stored and used for communications between the AT and the AN…). Eine aktuelle Konfiguration
              ergibt sich auch implizit aus dem Verweis auf zuvor ausgehandelte
              Funkschnittstellenprotokolle zwischen dem (ersten) Zugangsnetz
              (AN) und dem Endgerät (AT) (vgl. NK9, S. Kap. 2.5 A13 (AN-AN)

                                        32

              Interface, dritter Abs., zweiter Listeneintrag „“), wobei Basisstationen das jeweilige Zugangsnetz bilden (vgl. Merkmal 1.1H).

1.1.3   • forwarding the current configuration of the User Equipment from the first
        base station to the second base station via a terrestrial interface,

              Der CDMA2000-HRDP-Standard sieht vor, eine aktuelle Konfiguration des Endgeräts (access terminal / AT) in Form der „Session
              State Information“ von einem ersten Zugangsnetz (access network
              / AN) an ein zweites Zugangsnetz (AN) zu senden, wobei die Zugangsnetze durch die Basisstationen gebildet werden (vgl. NK8,
              S. 14-8, Kap. 14.8 Session State Information Record: The Session
              State Information is to be used in [8][9] for transferring the session
              parameters corresponding to the InUse protocol instances from a
              source access network to a target access network; i. V. m. NK9,
              Kap. 3.7.1, Punkt c. auf Seite 3-15: The source AN validates the
              A13-Session Information Request and sends the requested HRPD
              session information of the AT to the target AN in an A13-Session
              Information Response message; und NK9, S. 5-2, Kap. 5.1.1.2
              A13-Session Information Response: This message is sent from
              the source AN to the target AN and includes the requested session
              control information; i. V. m. dem enthaltenen “Session State Information Record” (vgl. NK9, S. 5-12, Kap. 5.2.1.11 Session State
              Information Record), wobei Basisstationen das jeweilige Zugangsnetz bilden (vgl. Merkmal 1.1H).

              Mit der A13-Schnittstelle erfolgt die Weiterleitung über eine „terrestrische“ Schnittstelle zwischen den Basisstationen (access network / AN) im Sinne des Streitpatents (NK9, S. 1-9, Fig. 1.4-1).

1.1.4   • establishing a second connection between the User Equipment and the
        second base station, and

              Zwischen dem Endgerät (AT) und der Basisstation des Ziel-Zugangsnetzes (target AN) wird eine Verbindung (HRPD session)
              eingerichtet (vgl. NK9, Kap. 3.7.1, S. 3-15, Punkt d.: The AT and
              the target AN complete the establishment of the HRPD session…
              i. V. m. NK9, S. 1-6, Definition „HRDP-Session“), wobei Basisstationen das jeweilige Zugangsnetz bilden (vgl. Merkmal 1.1H).

1.1.5   • reusing the forwarded configuration of the User Equipment at least partially for the operation of the User Equipment, when the User Equipment
        is served by the second base station,

                                     33

            Die zweite Basisstation (target AN) empfängt von der ersten Basisstation (source AN) die aktuelle Konfiguration bezüglich einer
            bestehenden „existing HRPD session“ zwischen erster Basisstation und Endgerät (HRPD session State Information), welche von
            der zweiten Basisstation dieser entsprechend wieder eingerichtet
            wird (vgl. NK9, Kap. 3.7.1, Seiten 3-14 und 3-15, Punkt a.: … During this procedure, the target AN receives the UATI of an existing
            HRPD session … when the target AN attempts to retrieve the existing HRPD session State Information from the source AN; i. V. m.
            NK9, Kap. 3.7.1, Seite 3-15, Punkt d.: … an existing HRPD session may be re-established…), wobei Basisstationen das jeweilige
            Zugangsnetz bilden (vgl. Merkmal 1.1H).

      characterized by

1.2   - a set of configuration parameters of the User Equipment is known by
      the first base station and the second base station as a default configuration,

            Standard-Konfigurationsparameter (default values) sind beiden
            Basisstationen (access network / AN) bekannt (vgl. NK9, S. 5-2,
            Kap. 5.1.1.2 A13-Session Information Response, Punkt d.: Attributes with default values shall not be sent to the target node. If an
            attribute is not contained in the SSIR, the target node shall assume
            that the missing attribute(s) have the default values (specified for
            each attribute in each protocol); i. V. m. “Session State Information
            Record” (vgl. NK9, S. 5-12, Kap. 5.2.1.11 Session State Information Record), und NK9, S. 5-2, Kap. 5.1.1.2 A13-Session Information Response, 1. Satz: This message is sent from the source
            AN to the target AN and includes the requested session control
            information;

            sowie NK8, S. 14-8, Kap. 14.8 Session State Information Record:
            If an attribute is not contained in the Session State Information record, the target access network shall assume that the missing attributes have the default values (specified for each attribute in each
            protocol)).

1.3   - the current configuration of the User Equipment is forwarded from the
      first base station to the second base station by solely forwarding configuration parameters, which deviate from the default configuration, and

            Bei der Weiterleitung der aktuellen Konfiguration dürfen Konfigurationsparameter mit Standardwerten nicht weitergeleitet werden

                                         34

                (vgl. NK9, S. 5-2, Kap. 5.1.1.2 A13-Session Information Response,
                Punkt d.: Attributes with default values shall not be sent to the target node. If an attribute is not contained in the SSIR, the target
                node shall assume that the missing attribute(s) have the default
                values (specified for each attribute in each protocol) [Unterstreichung hinzugefügt] i. V. m. NK9, S. 1-2, Kap. 1.1.3 Document
                Convention: -“Shall” and “shall not” identify requirements to be followed strictly to conform to the standard and from which no deviation is permitted.)

 1.4H     - wherein the current configuration is forwarded via an X2 interface.
                Den Dokumenten NK8 und NK9 fehlt – als Teile des CDMA2000-
                HRDP-Standards – der Bezug zu LTE-Basisstationen und der dort
                verwendeten X2-Schnittstelle; vielmehr dient zur Kommunikation
                zwischen den Basisstationen (access network / AN) im
                CDMA2000-HRDP-Standard eine A13-Schnittstelle als Protokoll
                zur Kommunikation zwischen zwei Basisstationen (AN).

Damit erweist sich der Gegenstand des Patentanspruchs 1 als neu gegenüber dem
CDMA2000-HRDP-Standard (Dokument NK8 mit NK9).


1.3     Der Gegenstand des Patentanspruchs 1 gemäß geändertem Hauptantrag
vom 27. September 2023 ist der Fachperson jedoch durch den CDMA2000-HRDP-Standard nach den Dokumenten NK8 und NK9 nahegelegt und beruht nicht auf
einer erfinderischen Tätigkeit.

Das Merkmal 1.1H, das den Anspruchsgegenstand auf ein LTE-Netzwerk mit entsprechenden Basisstationen (eNodeB) beschränkt, kann eine erfinderische Tätigkeit nicht begründen, da die Fachperson, die sich mit der Aufgabe konfrontiert sieht,
ein effektiveres Signalisierungsverfahren beim Handover (der in den Dokumenten
NK8/NK9 als „Handoff“ bezeichnet ist) eines Endgeräts von einer ersten an eine
zweite Basisstation eines Mobilfunknetzes anzugeben, die Grundprinzipien früherer
Standards, wie sie den Dokumenten NK8 und NK9 des CDMA2000-HRDP-Standards zu entnehmen sind, in Erwägung zieht.

Die Inkompatibilität der Standards von CDMA2000 und LTE ist für die Frage des zu
übertragenden Datenumfangs bei der Signalisierung zur Durchführung eines

                                         35

Handovers – der zum Anmeldetag in beiden Systemen bzw. Standards vorgesehen
war – nicht entscheidend. Weder die orthogonalen Codes noch die Frage, welche
Basisstation den Handover einleitet, betreffen Fragen der Weitergabe von Konfigurationsinformationen für das zu übergebende Endgerät während des Handovers.
Vielmehr gingen beide Standards zum Prioritätstag des Streitpatents davon aus,
dass im Rahmen des Handovers – und unabhängig vom Auslöser des Handovers
– die Übertragung von Konfigurationsinformationen des Endgeräts von der Quell-Basisstation an die Ziel-Basisstation erforderlich war.

Dem naheliegenden Anwenden des Grundprinzips, Standard-Werte nicht zu übertragen, steht auch der Umfang der nach dem CDMA200-HRDP Standard im Falle
des Handovers zu übermittelnden und in den Dokumenten NK8 und NK9 beschriebenen Konfigurationsinformationen nicht entgegen. Ob es zum Anmeldezeitpunkt
identische Informationselemente in LTE gab, ist für das Naheliegen nicht relevant,
da das Dokument NK8 mit NK9 vielmehr das Grundprinzip offenbart, wonach Parameter der Sitzungszustandsinformation mit Standardwerten nicht weitergeleitet werden. Die Fachperson entnimmt dem Dokument NK8 und NK9 ein vom Bedeutungsinhalt der Parameter unabhängiges Grundprinzip zum Umgang mit Default-Parametern bei der Weitergabe von Konfigurationsparametersätzen im Rahmen des
Handovers, welches sie zum Anmeldezeitpunkt des Streitpatents auch ohne weitere
Hinweise ohne Schwierigkeiten auf neue Parametersätze von Konfigurationsinformationen – vorliegend für Komponenten eines LTE-Netzwerks – übertragen hätte.

Das Merkmal 1.4H, welches die Verwendung einer X2-Schnittstelle zur Kommunikation zwischen den am Handover beteiligten Basisstationen festlegt, kann ebenfalls eine erfinderische Tätigkeit nicht begründen. Zwar sieht der Stand der Technik
des CDMA2000-Standards mit der A13-Schnittstelle eine eigene Schnittstelle für
den Handover vor. Jedoch hätte die Fachperson naheliegend aufgrund ihres Fachwissens zu verschiedenen Mobilfunkstandards zum Anmeldezeitpunkt eine bereits
definierte, geeignete Schnittstelle bzw. das damit verbundenen Kommunikationsprotokoll des jeweiligen Standards verwendet – vorliegend das X2-Interface des
LTE-Standards – und nicht für diesen speziellen Anwendungsfall ein zusätzliches

                                        36

Protokoll – hier die A13-Schnittstelle – auf den LTE-Standard übertragen und zusätzlich dort implementiert.

Damit ergeben sich die Unterschiede des Gegenstands des Patentanspruchs 1 gegenüber dem CDMA2000-HRDP-Standard für die Fachperson naheliegend aus diesem Standard (d. h. den Dokumenten NK8 und NK9) und ihrem Fachwissen.



2.      Dokument NK4 (R2-073416) mit Dokument NK5 (R2-073009)
Der Gegenstand des Patentanspruchs 1 nach geändertem Hauptantrag vom 27.
September 2023 ist aus dem Dokument NK4 (in Ergänzung zum darin referenzierten Dokument NK5 aus dem Standardisierungsverfahren) vorbekannt.


2.1     Bei dem Dokument NK4 handelt es sich um einen Diskussionsbeitrag aus
dem Standardisierungsverfahren der 3GPP-Arbeitsgruppe TSG-RAN2 (TSG: Technical Specification Group; RAN: Radio Access Network). Der Beitrag befasst sich
mit der Handover-Prozedur.

Das Dokument NK4 bezieht sich auf den vorausgegangenen Change Request R2-
073009 aus diesem Standardisierungsverfahren (NK4, S. 3, erster Abs.: Please
note that the changes are shown using R2-073009 as a base…), der als Dokument
NK5 in das Verfahren eingeführt ist. Die beiden Dokumente NK4 und NK5 können
als eine gemeinsame Offenbarung angesehen werden, da das Dokument NK4 konkret die Stellen benennt, die im Dokument NK5, auf dem es aufbaut, geändert oder
ergänzt werden sollen. Im folgenden Merkmalsvergleich sind die Dokumente NK4
und NK5 daher gemeinsam berücksichtigt.


2.2     Das Dokument NK4 offenbart der Fachperson – ausgedrückt in den Worten
des Patentanspruchs 1 gemäß geändertem Hauptantrag –


 1.1H    A method for handing over a User Equipment from a first base station to
         a second base station of a cellular telecommunication network, wherein
         the first base station is a first eNodeB and the second base station is a

                                          37

        second eNodeB of a Long Term Evolution network, the method comprising
               Die Dokumente NK4 und NK5 betreffen das Handover-Verfahren
               in LTE (vgl. NK4, Seite 1, 1. Introduction: “LTE handover procedure”; NK4, Seite 4, Figure 10.1.2.1: “Source eNB”; “Target eNB”;
               “3. HO decision”; “4. Handover Request”).
1.1.1   • establishing a first connection between the User Equipment and the first
        base station,
               Eine erste Verbindung folgt in dem Dokument NK4 implizit aus der
               Übertragung von “packet data” zwischen „UE“ und „Source eNB“ in
               Figur 10.1.2.1, sowie aus „serving cell“ in Kapitel 10.2.1 (S. 3) , dritter Absatz, vierter Spiegelstrich.
1.1.2   • arranging a current configuration of the User Equipment with the first
        base station,
               Als Teile einer aktuellen Konfiguration des Endgeräts sind dem Dokument NK4 die AS-Konfiguration (S. 1, Kap. 2. Discussion, II.3.:
               „…currently used AS configuration…“) und die SAE-Bearer-Konfiguration (S. 3, Kap. 10.1.2.1 … Handover: …QoS profiles in use by
               the UE (SAE bearer attributes) …) zu entnehmen.
1.1.3   • forwarding the current configuration of the User Equipment from the first
        base station to the second base station via a terrestrial interface,
               Die aus dem Dokument NK4 bekannte Konfigurationsinformation
               (vgl. Merkmal 1.1.2) wird beim Handover weitergeleitet (vgl. S. 3,
               Kap. 10.1.2.1 Handover, zw. Spiegelstrich: The QoS profiles in use
               by the UE (SAE bearer attributes) are sent to the target eNB by the
               source eNB…; sowie S. 1, Kap. 2. Discussion, II.3.: The source
               eNB provides the currently used AS configuration to the target
               eNB;).
               Eine „terrestrische“ X2 Schnittstelle liest die Fachperson in dem
               Dokument NK4 aufgrund seines Fachwissens bzw. den Angaben

                                         38

              in dem Dokument NK5 zu einer Kommunikation zwischen den Basisstationen (eNB) mit (vgl. NK5, S. 6, Abschnitt 4. Overall architecture und Fig. 4).
1.1.4   • establishing a second connection between the User Equipment and the
        second base station, and
              Eine zweite Verbindung folgt implizit aus Figur 10.1.2.1 des Dokuments NK4 mit der Übertragung von “packet data” zwischen „UE“
              und „Target eNB“, sowie aus NK4, Seite 5, Schritte 8 und 9.
1.1.5   • reusing the forwarded configuration of the User Equipment at least partially for the operation of the User Equipment, when the User Equipment
        is served by the second base station,
              Eine Wiederverwendung der AS-Konfiguration ist in dem Dokument
              NK4 im Rahmen einer “re-configuration” beschrieben: S. 2, Kap. 2.
              Discussion, III.4. i. V. m. S. 5, Nummer 5: The radio resources can
              either be specified … or as a delta compared to the AS-configuration used in the source cell (ie. a ‘re-configuration’); sowie bzgl. der
              SAE-Bearer-Konfiguration (vgl. NK4, S. 5, Nummer 5: The target
              eNB configures the required resources according to the received
              SAE bearer QoS information…).
        characterized by
1.2     - a set of configuration parameters of the User Equipment is known by the
        first base station and the second base station as a default configuration,
              Es ergibt sich zwangsläufig aus dem Vorschlag, nur die Unterschiede zu übertragen (…signalling the delta is considered most
              efficient…), dass beide Basisstationen von der gleichen vorbestimmten Konfiguration (zumindest der AS-Konfiguration) ausgehen müssen, mithin eine „Default-Konfiguration“ existieren muss,
              welche beide Basisstationen kennen (vgl. NK4, S. 2, Kap. 2. Discussion, II.3.: The source eNB provides the currently used AS configuration to the target eNB … It is desirable to keep the handover
              message short. Since normally the configuration should not change

                                           39

                much upon handover, signalling the delta is considered most efficient…).
 1.3     - the current configuration of the User Equipment is forwarded from the
         first base station to the second base station by solely forwarding configuration parameters, which deviate from the default configuration, and
                Das Dokument NK4 schlägt vor, nur ein Delta der Konfiguration,
                mithin nur das Abweichen von einer “default configuration” weiterzuleiten (vgl. S. 2, Kap. 2. Discussion, II.3.: The source eNB provides the currently used AS configuration to the target eNB … It is
                desirable to keep the handover message short. Since normally the
                configuration should not change much upon handover, signalling
                the delta is considered most efficient…; sowie Ausführungen zu
                Merkmal 1.2.)
 1.4H    - wherein the current configuration is forwarded via an X2 interface.
                vgl. Merkmal 1.1.3 zur “terrestrischen” Schnittstelle und X2.


Soweit die Beklagte die Merkmale 1.2 und 1.3 des Patentanspruchs 1 als nicht in
dem Dokument NK4 verwirklicht ansieht, da sich die „handover message“ im diskutierten Absatz auf Seite 2, Kap. 2. Discussion, II.3. (The source eNB provides the
currently used AS configuration to the target eNB … It is desirable to keep the handover message short. Since normally the configuration should not change much upon
handover, signalling the delta is considered most efficient…) auf den „handover
command“ von der Ziel-Basisstation an das Endgerät beziehe (vgl. Seite 2, Punkt
4. unter III. Re-configuration; i. V. m. Seite 4, Fig. 10.1.2.1), überzeugt dies nicht.

Der zitierte Abschnitt II.3. der Diskussion zu „II. AS context transfer“ befasst sich
gemäß dem einleitenden Satz ausdrücklich mit einer Übertragung einer AS-Konfiguration von der Quell- an die Ziel-Basisstation. Daher wird der Leser in den unter
diesem Abschnitt II.3. angeführten Punkten keine Angaben zu Nachrichten von der
Quell-Basisstation an das Endgerät erwarten, sondern weitere Erläuterungen zu der
genannten Übertragung der AS-Konfiguration. Daraus, dass sich das Dokument
NK4 an anderer Stelle (im Abschnitt III. Re-Configuration) mit dem Inhalt des
„handover command“ von der Quell-Basisstation an das Endgerät befasst, lässt sich

                                          40

nicht zwangsläufig schließen, dass sich der Verweis auf eine Handover-Nachricht
in Abschnitt „II. AS context transfer“ auf den „handover command“ an das Endgerät
und nicht auf den „handover request“ an die übernehmende Ziel-Basisstation bezieht. Denn die Änderungsvorschläge (Text proposal) zum Standard, Punkte 4 und
5 auf Seite 5, die sich beide auf die Ziel-Basisstation beziehen (Target eNB in NK4,
Figur 10.1.2.1 auf Seite 4), sehen im Einklang mit Abschnitt „II. AS context transfer“
die Übermittlung der AS-Konfiguration im „HANDOVER REQUST“ vor (vgl. NK4,
Seite 5, Punkt 4: The source eNB issues a HANDOVER REQUEST message to the
target eNB passing necessary information to prepare the HO at the target side ([…]
RRC context including the C-RNTI of the UE in the source eNB and the AS configuration, SAE bearer context)).

Zwar spricht Punkt 5 nur vom Spezifizieren der AS-Konfiguration gegenüber dem
Endgerät als Delta zur AS-Konfiguration in der Quell-Zelle (vgl. NK4, Seite 5, Punkt
5: The target eNB configures the required resources […]. The radio resources can
either be specified independently (i.e. an ‘establishment’) or as a delta compared to
the AS- configuration used in the source cell (ie. a ‘re-configuration’)). Dabei ist der
Fachperson jedoch bewusst, dass im Handover-Request nicht umfangreichere Konfigurationsdaten des Endgeräts von der ersten an die zweite Basisstation (source
eNB an target eNB) übermitteln werden als im (anschließenden) Handover-Command von der zweiten Basisstation an das Endgerät, zumal die Ausführungen auf
Seite 1 zu „II. AS context transfer“, die (ebenfalls) von der Signalisierung des Deltas
sprechen, ausdrücklich – entsprechend dem vorliegenden Patentanspruch 1 – auf
den Datentransfer zwischen Quell- und Ziel-Basisstation Bezug nehmen (vgl. Seite
1, Abschnitt II. AS context transfer: 3. The source eNB provides the currently used
AS configuration to the target eNB; zweiter Aufzählungspunkt: It is desirable to keep
the handover message short. Since normally the configuration should not change
much upon handover, signalling the delta is considered most efficient… [Unterstreichungen ergänzt]).

Der Gegenstand des Patentanspruchs 1 in der Fassung nach dem geänderten
Hauptantrag vom 27. September 2023 ist demnach aus dem Dokument NK4 (mit
dem Dokument NK5 im Sinne einer gemeinsamen Offenbarung) vorbekannt.

                                         41




3.    Die weiteren angegriffenen Patentansprüche 5, 6, 7 und 11 in der Fassung
nach dem geänderten Hauptantrag bedürfen keiner weiteren, isolierten Prüfung,
weil die Beklagte den geänderten Hauptantrag als geschlossenen Anspruchssatz
versteht und das Streitpatent auch insoweit nur als Ganzes verteidigt (der ebenfalls
angegriffene Patentanspruch 10 entfällt nach Aufnahme seiner Merkmale in den
Patentanspruch 1 nach geändertem Hauptantrag); dies rechtfertigt, das Patent in
angegriffenem Umfang in der Fassung nach geändertem Hauptantrag insgesamt
für nicht rechtsbeständig zu erklären, nachdem sich der Gegenstand eines Patentanspruchs aus dem vom Patentinhaber verteidigten Anspruchssatz als nicht patentfähig erweist (vgl. BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR
2017, 57 – Datengenerator).




          IV. Zur Fassung des Streitpatents nach Hilfsantrag 2A


In der Fassung nach Hilfsantrag 2A vom 22. Januar 2025 erweist sich das Streitpatent im angegriffenen Umfang als zulässig und schutzfähig, so dass die Klage, soweit sie sich auch gegen diese Fassung richtet, abzuweisen ist.


1.    Ausgehend von der Anspruchsfassung des geänderten Hauptantrags vom
27. September 2023 wurden in den Patentanspruch 1 nach Hilfsantrag 2A zusätzlich die folgenden Merkmale aufgenommen:
      1.5H2A    wherein the current configuration is a measurement configuration of
                the User Equipment (180) characterizing measurement procedures
                which are performed by the User Equipment (180),
      1.6H2A    wherein the current configuration comprises activity data of the User
                Equipment (180), which activity data determine activity times of the
                User Equipment (180), and
      1.7H2A    wherein the activity times are used by the User Equipment (180) as
                a time reference for performing measurements.

                                         42



Gemäß Patentanspruch 1 des Hilfsantrags 2A soll die aktuelle Konfiguration (current configuration) eine Messkonfiguration des Endgeräts (measurement configuration of the User Equipment) sein, die Messverfahren kennzeichnet, die durch das
Endgerät ausgeführt werden. Solche Messungen sind in den Absätzen 0019 bis
0021 des Streitpatents näher erläutert. Der Hilfsantrag 2A konkretisiert im Patentanspruch 1 außerdem die Inhalte der aktuellen Konfiguration (current configuration) in
Form von Aktivitätsdaten (activity data) des Endgeräts. Solche Aktivitätsdaten sind
in den Absätzen 0022 und 0023 des Streitpatents beschrieben und betreffen demnach die Aktivitätsintervalle DRX und DTX des Endgeräts. Diese beschreiben Aktivitäts- und Ruhezeiten im Rahmen eines als „Discontinuous Reception“ bzw. „Discontinuous Transmission“ bezeichneten Betriebs des Endgeräts.

Das Verfahren nach Hilfsantrag 2A sieht hierzu vor, dass die aktuelle Konfiguration
(current configuration) eine Messkonfiguration ist (Merkmal 1.5H2A: „wherein the
current configuration is a measurement configuration of the User Equipment…“),
somit Messverfahren des Endgeräts beschreibt bzw. berücksichtigt. Das Merkmal
M1.5H2A bezieht sich ausdrücklich auf eine Messkonfiguration, also auf eine Konfiguration zur Durchführung von Messungen. Deren Auswertung oder Übermittlung
an andere Netzwerkkomponenten ist weder im (weiteren) Patentanspruch 1, noch
in den zugrundeliegenden Absätzen 0019 bis 0021 oder 0023 des Streitpatents thematisiert.

Das Merkmal 1.6H2A ergänzt hierzu, dass es sich bei den Aktivitätsdaten um Daten
handelt, die Teil einer aktuellen Konfiguration (current configuration) des Endgeräts
sind, welche gemäß dem Merkmal 1.5H2A die Messkonfiguration des Endgeräts beschreibt. Bei den im Merkmal 1.6H2A genannten Aktivitätsdaten handelt es sich somit
nicht um einen beliebigen Teil der Konfigurationsdaten des Endgeräts, der nur irgendwie im Zusammenhang mit Messungen stehen oder Einfluss auf die Übermittlung von Messberichten haben kann, sondern um Parameter eines Datensatzes von
aktuellen Konfigurationsdaten, welcher gemäß dem Merkmal 1.5H2A eine Messkonfiguration beschreibt, die gemäß dem Merkmal 1.1.2 im Endgerät und der ersten
Basisstation eingerichtet werden und gemäß den Merkmalen 1.1.3, 1.3 und 1.4H

                                        43

von der ersten Basisstation an die zweite Basisstation weitergeleitet werden (vgl.
hierzu auch die Auslegung des Patentanspruchs 1 gemäß geändertem Hauptantrag).

Die in der Messkonfiguration angegebenen Aktivitätsdaten dienen dabei als Referenzzeiten zur Durchführung von Messungen (Merkmal 1.7H2A).

Der Patentanspruch 11 gemäß Hilfsantrag 2A ist gegenüber dem geänderten
Hauptantrag vom 27. September 2023 unverändert.

Die Unteransprüche 5, 6, 7 und 10, deren Merkmale in den Patentanspruch 1 gemäß Hilfsantrag 2A aufgenommen worden sind, entfallen folglich in der Fassung
des Hilfsantrags 2A.



2.       Der Gegenstand des Streitpatents im angegriffenen Umfang gemäß Hilfsantrag 2A geht nicht über den Inhalt der Anmeldung in ihrer ursprünglich eingereichten
Fassung hinaus und ist nicht unzulässig erweitert.

Im Patentanspruch 1 sind die Merkmale der erteilten, ebenfalls angegriffenen und
ursprünglich eingereichten Unteransprüche 5, 6 und 7 ergänzt (vgl. Anlagen N1 und
N3). Diese Merkmale beschränken den Patentanspruch 1 gemäß Hilfsantrag 2A
somit gegenüber der erteilten Anspruchsfassung.

Der Gegenstand des Patentanspruchs 11 gemäß der Fassung nach Hilfsantrag
2A vom 22. Januar 2025 entspricht der Fassung gemäß geändertem Hauptantrag.
Er ist den ursprünglichen Unterlagen zu entnehmen und ist gegenüber der erteilten
Anspruchsfassung beschränkt (vgl. Ausführungen zur Ursprungsoffenbarung und
Zulässigkeit des Patentanspruchs 11 gemäß geändertem Hauptantrag).



3.       Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2A ist neu. Keines der im Verfahren befindlichen Dokumente des Standes der Technik zeigt ein
Verfahren mit allen Merkmalen des Patentanspruchs 1. Der Gegenstand des Patentanspruchs 1 nach gemäß Hilfsantrag 2A beruht auch auf einer erfinderischen

                                        44

Tätigkeit, denn aus keinem der im Verfahren befindlichen Dokumente ergibt sich ein
Verfahren gemäß dem Patentanspruch 1 für die Fachperson in naheliegender
Weise.


3.1   Dokument NK8 mit Dokument NK9 (CDMA2000-HRDP-Standard)
Die Dokumente NK8 und NK9 kennen unter anderem (aktuelle) Konfigurationsinformationen, die beim Handover (der in dem Dokument NK8 bzw. NK9 auch als
„Handoff“ bezeichnet wird) von der Quell- an die Ziel-Basisstation übermittelt werden, wobei deren Default-Werte nach dem Dokument NK9, S. 5-2, Kap. 5.1.1.2 A13-
Session Information Response nicht zur Ziel-Basisstation übertragen werden sollen
(vgl. Ausführungen zum geänderten Hauptantrag).

Den Dokumenten NK8 und NK9 ist allerdings kein direkter Zusammenhang zwischen der Schlaf- und Wachzeitenkonfiguration und der Durchführung von Messverfahren zu entnehmen. Insbesondere fehlt ein Hinweis auf die Aufnahme von Aktivitätsdaten, d. h. von Daten zur Schlaf- und Wachzeitenkonfiguration in dem Messdatensatz, der als Konfigurationsinformation beim Handover (handoff) von der ersten an die zweite Basisstation übermittelt wird. Die Schlaf- und Wachzeitenkonfiguration dient in den Dokumenten NK8 und NK9 nicht der Steuerung der Messverfahren, sondern dem Betrieb des Endgeräts selbst, bspw. dem Aktivieren und Deaktivieren der Funkschnittstelle. Dass aus diesem Grund Aktivitätszeiten des Endgeräts
(DRX/DTX-Intervall) im Zusammenhang mit Messverfahren stehen können, macht
entsprechende Aktivitätsdaten nicht bereits zu Daten einer Messkonfiguration, insbesondere nicht zum Teil eines Datensatzes einer Messkonfiguration, der entsprechend dem Merkmal 1.3 beim Handover übertragen wird.

Zwar sind den Dokumenten NK8 und NK9 im Rahmen eines „Default Route Update
Protocol“ auch Parameter für Messungen zu entnehmen, die im Sinne einer aktuellen Konfiguration nach dem Merkmal 1.3 beim Handover von der (ersten) Basisstation weitergeleitet werden (bspw. Suchfenstergrößenkonfiguration; vgl. NK8, S. 8-
125 ff, 8.7.7 Configuration Attributes). Es sind jedoch im Zusammenhang mit diesen
Parametern für Messverfahren keine Aktivitätszeiten oder -daten als Teil einer entsprechenden Messkonfiguration vorgesehen.

                                        45


Selbst wenn die Fachperson hierbei die mögliche Bedeutung einer Endgerätekonfiguration zur „Discontinuous Transmission (DTX)“ bzw. „Discontinuous Reception
(DRX)“ für solche Messverfahren aufgrund ihres Fachwissens erkennt, führt dies
ausgehend von den in den Dokumenten NK8 und NK9 identifizierten Daten zu
Messverfahren nicht in naheliegender Weise dazu, solche Aktivitätszeiten auch als
Parameter einer Messkonfiguration beim Handover (handoff) von der ersten an die
zweite Basisstation zu übermitteln. Denn weder sind „Discontinuous Transmission
(DTX)“ bzw. „Discontinuous Reception (DRX)“ originär (nur) für Messverfahren relevant, noch ist die Durchführung von Messverfahren zwingend auf aktive Intervalle
des Endgeräts beschränkt oder in inaktiven Intervallen ausgeschlossen.

Die Fachperson erhält daher auch keinen Hinweis, solche Aktivitätsdaten als Parameter der in den Dokumenten NK8 und NK9 identifizierten Messdaten als zusätzliche Parameter dieser Messdaten beim Handover von der ersten an die zweite Basisstation zu übermitteln.

Inwieweit die DRX/DTX-Intervalle einen Versand von Messberichten beeinflussen,
ist für die Beurteilung der Frage der erfinderischen Tätigkeit nicht von Bedeutung,
da sich die unabhängigen Patentansprüche nach Hilfsantrag 2A nur mit einer Messkonfiguration des Endgeräts und deren Weiterleitung befassen, nicht jedoch mit der
Auswertung und Weiterleitung möglicher Messergebnisse.

Die zum CDMA2000-HRDP-Standard offenbarten (aktuellen) Konfigurationsdaten
werden in Form der „Session State Information“ bzw. „A13 Session Information“ von
einem ersten Zugangsnetz (access network / AN) an ein zweites Zugangsnetz (AN)
gesendet, wobei die Zugangsnetze durch Basisstationen gebildet werden (vgl. NK8,
S. 14-8, Kap. 14.8 Session State Information Record: The Session State Information
is to be used in [8][9] for transferring the session parameters corresponding to the
InUse protocol instances from a source access network to a target access network;
i. V. m. NK9, Kap. 3.7.1, Punkt c. auf Seite 3-15: The source AN validates the A13-
Session Information Request and sends the requested HRPD session information
of the AT to the target AN in an A13-Session Information Response message). Soweit hierbei in einem „Enhanced Idle State Protocol“ (NK8, S. 8-46, S. 15-3) auch

                                         46

Aktivitätsdaten umfasst sind, ist kein Hinweis dafür ersichtlich, dass diese Informationen wiederum einen Teil von Messdaten bilden oder die Fachperson den in diesem Kontext übermittelten aktuellen Konfigurationsdaten Messdaten hinzufügen
würde, da das „Enhanced Idle State Protocol“ keine Messungen beschreibt.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 2A vom 22. Januar 2025
erweist sich damit als neu gegenüber dem CDMA2000-Standard gemäß den Dokumenten NK8 und NK9.


Darüber hinaus ist in den Dokumenten NK8 und NK9 keine Veranlassung für die
Fachperson ersichtlich, die vorstehend erläuterten Unterscheidungsmerkmale in
der durch den Hilfsantrag 2A vorgeschlagenen Form abzuwandeln. Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2A vom 22. Januar 2025 ist der
Fachperson daher auch ausgehend von den Dokumenten NK8 und NK9 nicht nahegelegt.


3.2   Dokument NK4 (R2-073416) mit Dokument NK5 (R2-073009)
Bei der Information zur „Discontinuous Reception“ und der AS-Konfiguration gemäß
dem Dokument NK4, in der sie enthalten ist, handelt es sich nicht um eine Messkonfiguration des Endgeräts, die gemäß dem Merkmal 1.5H2A Messverfahren kennzeichnet. Allein daraus, dass „CQI reports“ während der Aus- bzw. Ruhephasen des
DRX-Zyklus nicht erzeugt und gesendet werden können, folgt nicht, dass es sich
bei diesem DRX-Zyklus um einen Aktivierungszeitraum für Messungen handelt, der
das Messverfahren selbst kennzeichnet oder beschreibt (Merkmal 1.5H2A: …characterizing measurement procedures…). Ungeachtet dessen, dass das Streitpatent
bezüglich der Messkonfiguration deren mögliche Auswirkung auf Messberichte
nicht thematisiert, stellt der DRX-Betrieb zwar eine Konfigurationsinformation des
Endgeräts dar, trifft aber nicht zwangsläufig eine Aussage zu einem Messverfahren
und ist insbesondere in der beanspruchten Form in dem Dokument NK4 bzw. NK5
nicht im Rahmen der Übermittlung einer aktuellen Konfiguration zwischen den Basisstationen beim Handover als Parameter eines solchen Parametersatzes zur Konfiguration des Endgeräts vorgesehen.

                                       47

Es ist in dem Dokument NK4 bzw. NK5 bereits nicht erkennbar, dass die DRX-Intervalle als Teil der AS-Konfiguration beim Handover weitergeleitet werden und nähere Angaben zum Inhalt der QoS profiles, SAE bearer attributes bzw. AS-configuration machen. Allein Hinweise auf Abhängigkeiten der Messverfahren von Aktivitätszeiten (aufgrund der Verfügbarkeit bzw. Aktivität bestimmter Übertragungskanäle) geben keinen Anlass dazu, allgemeine Aktivitätsdaten des Endgeräts im Rahmen der QoS profiles bzw. SAE bearer attributes beim Handover mit zu übertragen,
da das Dokument NK4 bzw. NK5 zu diesen Attributen keine näheren Angaben
macht.

Es ist zwar zutreffend, dass eine „Discontinuous Reception“ bzw. „Discontinuous
Transmission“, d. h. das Vorsehen von Aktivitäts- und Ruheintervallen (DRX/DTX-Intervalle), Einfluss auf Messverfahren habe kann, etwa durch das Deaktivieren bestimmter Kommunikationsschnittstellen oder -kanäle. Hierbei sind Messverfahren
jedoch nicht zwangsläufig an die aktive Phase des Endgeräts gebunden, sondern
können auch in Ruhephasen stattfinden (vgl. NK5, Abschnitt 10.1.3.2, S. 42: … UE
may need to perform neighbour cell measurements during DL/UL idle periods that
are provided by DRX/DTX…). Die Bedeutung der DRX-Parameter geht jedoch über
eine mögliche Berücksichtigung in Messverfahren hinaus und bestimmt ganz allgemein den Betrieb des Endgeräts (vgl. Auslegung). In diesem Zusammenhang wird
die Fachperson zwar in dem Dokument NK5 darauf hingewiesen, dass die dem Dokument NK4 bzw. NK5 entnehmbare Messkonfiguration zu den DRX/DTX-Intervallen passen soll (NK5, S. 42, Abs. 10.1.3.1 Note: „…should match the DRX/DTX
cycle…“). Hieraus folgt jedoch nicht, dass die Messkonfiguration selbst Angaben zu
DRX/DTX-Intervallen enthalten muss, sondern lässt offen, ob und wie diese
DRX/DTX-Intervalle tatsächlich berücksichtigt werden. Allein aus der Nennung von
Parametern zur Beschreibung einer „Discontinuous Reception“ bzw. „Discontinuous
Transmission“ folgt daher nicht nahliegend, diese als Parameter einer aktuellen
Messkonfiguration, also als Teil eines Parametersatzes, der eine aktuelle Messkonfiguration des Endgeräts beschreibt, beim Handover weiterzuleiten.

Auch besteht ein Zusammenhang zwischen der Durchführung von Inter-Frequenz-Messungen bzw. Inter-RAT-Messungen und den Ruhephasen des DRX-Betriebs

                                         48

(vgl. NK5, S. 42, Abschnitt 10.1.3.2; S. 48-49, Abschnitt 10.2.3.1). Hieraus folgt jedoch nicht, dass die Parameter des DRX-Betriebs als Teil einer beim Handover weiterzuleitenden Messkonfiguration vorzusehen sind. Vielmehr ist auch hier nur offenbart, dass die allgemein für den Betrieb des Endgeräts geltenden DRX-Intervalle
auch für die Messungen relevant sind. Dies macht die Konfiguration des DRX-Betriebs aber nicht zu einer Messkonfiguration, da die DRX-Konfiguration unabhängig
von Messungen für den allgemeinen Betrieb des Endgeräts erforderlich ist (bspw.
zur Optimierung des Energiebedarfs des Endgeräts; vgl. Abs. 0023, 0046 des Streitpatents). Auch die Anmerkung auf Seite 41/42 des Dokuments NK5 zu Abschnitt
10.1.3.1 („NOTE: To avoid UE activity outside the DRX/DTX cycle, the reporting
criteria for neighbour cell measurements should match the used DRX/DTX cycle“)
sagt nichts Anderes über die DRX-Konfiguration aus, denn die zitierte Anmerkung
besagt nicht, dass das DRX/DTX-Intervall ein Parameter einer (zwischen den Basisinformationen übermittelten) Messkonfiguration ist, sondern nur, dass Kriterien
(d. h. Parameter) für Messungen zu diesem Intervall passen sollen (…should
match…).

Der im Dokument NK5 erkennbare Zusammenhang zwischen Inter-Frequenz-Messungen bzw. Inter-RAT-Messungen und den DRX-Intervallen ist auch nicht Anlass
dazu, Angaben zu DRX-Intervallen als Teil einer beim Handover gemäß dem Dokument NK4 weitergeleiteten AS-Konfiguration zu übertragen. Selbst wenn aus dem
Dokument NK4 bzw. NK5 hervorginge, dass die AS-Konfiguration auch Parameter
zum DRX-Betrieb umfasst, wird diese AS-Konfiguration damit nicht zu einer Messkonfiguration, da die DRX-Intervalle (unabhängig von Messungen oder Messberichten) ganz allgemein den aktiven Betrieb des Endgeräts bestimmen.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 2A vom 14. Januar 2025
erweist sich damit als neu gegenüber dem Dokument NK4 mit NK5.


Darüber hinaus ist in den Dokumenten NK4 und NK5 keine Veranlassung für die
Fachperson ersichtlich, die vorstehend erläuterten Unterscheidungsmerkmale in
der durch den Hilfsantrag 2A vorgeschlagenen Form abzuwandeln. Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2A vom 22. Januar 2025 ist der

                                         49

Fachperson daher auch ausgehend von den Dokumenten NK4 und NK5 nicht nahegelegt.


3.3   Dokument NK10 (EP 1 909 521 A1)
Bei dem Dokument NK10 handelt es sich um eine europäische Patentanmeldung,
die sich mit der Übertragung und Verwaltung von Informationen zur Dienstqualität
(Quality of Service / QoS) während des Handovers von einer Quell- zu einer Ziel-Basisstation in LTE-Kommunikationsnetzwerken befasst. Auf Basis eines übermittelten Buffer-Status und Qualitätsprofilen für die Funkträger (QoS profiles for the
radio bearers) werden dem Endgerät von der (Quell-)Basisstation, mit der das Endgerät verbunden ist, Übertragungsressourcen zugewiesen (vgl. Fig. 7). Die dem
Endgerät hierbei zugeordnete Prioritätsreihenfolge (Priority order), die anhand eines so genannten QoS-Indikators durch die (Quell-)Basisstation dem Endgerät signalisiert wird, kann als eine (von der Quell-Basisstation bestimmte) aktuelle Konfiguration des Endgeräts verstanden werden.

Aus dem Dokument NK10 folgt jedoch nicht zweifelsfrei und eindeutig, ob ein QoS-Indikator 1, der als Standardwert einer aktuellen Konfiguration angesehen werden
kann, bei einem Handover übertragen wird oder nicht und erfüllt damit nicht die Anforderung des Merkmals 1.3 des Patentanspruchs 1 gemäß Hilfsantrag 2A vom
22. Januar 2025.

Ein entsprechender Zusammenhang ergibt sich auch nicht aus Absatz 0116 in Verbindung mit Absatz 0130, denen nur die Übertragung eines QoS-Indikators im Sinne
einer aktuellen Konfiguration des Endgeräts von der ersten an die zweite Basisstation zu entnehmen ist.

Sie ergibt sich auch nicht aus Absatz 0118. Denn dieser betrifft nicht den Fall, dass
sich die Servicequalität tatsächlich verschlechtert, sondern nur die Angabe, dass
die Übermittlung der Servicequalität (einschließend dem QoS-Indikator) in dieser
Ausgestaltung nur für bestimmte Funkträger erfolgt, bei denen eine Verschlechterung der Servicequalität wahrscheinlicher ist (Abs. 0118: …is more likely to undergo
a degradation of the Quality of Service…).

                                         50

Auch aus der Aussage, dass ohne Vorliegen einer Konfiguration die Ziel-Basisstation die Standardkonfiguration verwendet (Absatz 0112), kann nicht abgeleitet werden, dass ausschließlich von der Standardkonfiguration abweichende Parameter
von der ersten Basisstation weitergeleitet werden, denn der zitierte Absatz beschreibt nur die Default-Konfiguration auf Seiten der Ziel-Basisstation und sagt
nichts darüber aus, ob entsprechende Parameter einer Konfiguration beim Handover von der ersten an die zweite Basisstation weitergeleitet werden oder nicht.

Die beschriebene Übertragung des QoS-Indikators 2 (Abs. 0118 i. V. m. Abs. 0106),
der von der Standardkonfiguration (QoS-Indikator 1) abweicht, kann das Merkmal
1.3 ebenfalls nicht erfüllen, da das Merkmal 1.3 ausdrücklich vorsieht, dass lediglich
(solely) die Konfigurationsparameter weitergeleitet werden, die von der Standardkonfiguration abweichen (vgl. auch Auslegung des Merkmals 1.3). Die Übertragung
des QoS-Indikators 2 lässt aber keinen Rückschluss auf die übermittelten Parameter zu, falls die aktuelle Konfiguration der Standardkonfiguration (QoS-Indikator 1)
entspricht.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 2A vom 14. Januar 2025
erweist sich damit als neu gegenüber dem Dokument NK10.


Da das Dokument NK10 im Prioritätsintervall des Streitpatents veröffentlicht wurde,
ist es nur für die Prüfung auf Neuheit gemäß Art. 54 (3) EPÜ und nicht für die Prüfung der erfinderischen Tätigkeit relevant.


3.4    Weitere Dokumente
Die Dokumente NK1, NK2 bzw. NK2a, NK3, NK6 und NK7 hat die Klägerin nur im
Zusammenhang mit einzelnen Merkmalen oder angegriffenen Unteransprüchen in
das Verfahren eingeführt. Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2A vom 22. Januar 2025 ist neu gegenüber diesen weiteren Dokumenten. Eine
mangelnde erfinderische Tätigkeit hat die Klägerin ausgehend von diesen Dokumenten weder geltend gemacht, noch ist sie für den Senat ersichtlich. Ausgehend

                                        51

von den Dokumenten NK1, NK2 bzw. NK2a, NK3, NK6 und NK7 ist der Gegenstand
des Patentanspruchs 1 nach Hilfsantrag 2A der Fachperson nicht nahegelegt.

Bei dem Dokument NK1 (R2-062904) handelt es sich um einen Diskussionsbeitrag
zum 3GPP TSG-RAN3 Meeting #55 in Südkorea mit dem Titel „Use of AS-configuration upon handover and connection establishment“. Das bereits im Streitpatent
zitierte Dokument NK1 wurde außer zum Verständnis des Streitpatents nur als weiterer Beleg für eine Delta-Signalisierung der AS-Konfiguration im Rahmen des
Handover herangezogen (NK1, Kap. 2.2, Seite 3, letzter Spiegelstrich). Dem Dokument NK1 sind darüber hinaus keine Informationen zur Beurteilung der Patentfähigkeit der vorliegenden Anträge zu entnehmen, die über den weiteren Stand der Technik hinausgingen, was auch nicht geltend gemacht wurde.

Beim Dokument NK2a (R2-062235) handelt es sich um einen Diskussionsbeitrag
zum 3GPP TSG-RAN WG2 Meeting #54 mit dem Titel „LTE Handover preparation“,
das ebenfalls bereits im Streitpatent zitiert ist. Bei dem Dokument NK2 (R2-062887)
handelt es sich um ein dem Dokument NK2a inhaltlich entsprechendes Dokument
der gleichen Autorin zum Folgetreffen 3GPP TSG-RAN WG2 Meeting #55. Das im
Streitpatent zitierte Dokument NK2a bzw. NK2 hat die Klägerin nur zum Verständnis
des Streitpatents herangezogen. Das Dokument NK2a bzw. NK2 enthält darüber
hinaus keine Informationen zur Beurteilung der Patentfähigkeit der vorliegenden Anträge, die über den weiteren Stand der Technik hinausgingen, was auch nicht geltend gemacht wurde.

Das Dokument NK3 (R3-060038), ein Diskussionsbeitrag zum 3GPP TSG RAN
WG3 Meeting #50 mit dem Titel „Intra-AS handover procedure in LTE-ACTIVE
mode with CPS“, befasst sich mit Handover-Prozeduren für einen aktiven Betriebszustand in LTE. Das Dokument NK3 enthält keine über den weiteren Stand der
Technik hinausgehenden Informationen zur Beurteilung der Patentfähigkeit der vorliegenden Anträge, was auch nicht geltend gemacht wurde.

                                         52

Das Dokument NK6 (R2-071285) ist ein Diskussionsbeitrag zum 3GPP TSG-RAN
WG2 Meeting #57bis mit dem Titel „DRX parameters in LTE“. Diese Parameter wurden (nur) in Verbindung mit dem Dokument NK4 im Zusammenhang mit dem Unteranspruch 7 in der erteilten Fassung diskutiert.

Zwar beschreiben die in dem Dokument NK6 genannten Parameter die „Discontinuous Reception (DRX)“ in LTE-Netzwerken; sie bilden damit jedoch nicht automatisch einen Bestandteil einer aktuellen Messkonfiguration, insbesondere nicht als
Teil eines Parametersatzes, der eine Messkonfiguration beschreibt und beim
Handover zwischen den Basisstationen ausgetauscht wird, da die Bedeutung der
DRX-Parameter über eine mögliche Berücksichtigung in Messverfahren hinausgeht
(vgl. Auslegung). Zwar wird die Fachperson – wie bereits zum Dokument NK4 dargelegt – in dem Dokument NK5 darauf hingewiesen, dass die dort entnehmbare
Messkonfiguration zu den DRX/DTX-Intervallen passen soll (NK5, Abs. 10.1.3.1
Note: „…should match the DRX/DTX cycle…“). Hieraus folgt jedoch nicht, dass die
Messkonfiguration selbst Angaben zu DRX/DTX-Intervallen enthält. Der Beschreibung von Parametern einer „Discontinuous Reception (DRX)“ in dem Dokument
NK6 ist nicht zu entnehmen, diese als Parameter eines Parametersatzes einer aktuellen Messkonfiguration beim Handover weiterzuleiten. Hierfür liefert weder das
Dokument NK4 noch das Dokument NK6 einen Hinweis.

Das Dokument NK7 (R2-072617), ein Diskussionsbeitrag zum 3GPP TSG-RAN2
Meeting #58bis mit dem Titel „E-UTRA RRC working assumptions & open issues“
befasst sich Annahmen und offenen Fragen des „Radio Resource Control Protocol
(RRC)“ im Rahmen der LTE-Standardisierung.

Das Dokument NK7 wurde nur in Bezug auf Default-Parameter genannt und ihm ist
selbst in diesem Zusammenhang nur zu entnehmen, dass die Verwendung solcher
vorbestimmten Default-Parameter Gegenstand weiterer Untersuchungen ist (NK7,
Abschnitt 2.7, Seite 4: „The use of default and pre-defined configurations is FFS“).
Dies gibt insbesondere auch im Kontext der Dokumente NK4 und NK5 weder Aufschluss über eine Festlegung von Standard-Parametern bei Messkonfigurationen
noch über weitere umfasste Parameter von Messkonfigurationen wie bspw. Angaben zu Aktivitätsphasen des Endgeräts.

                                         53



3.5.   Der Gegenstand des (einzigen weiteren) Patentanspruchs 11 gemäß Hilfsantrag 2A vom 22. Januar 2025 ist ebenfalls neu und beruht auch auf einer erfinderischen Tätigkeit, denn aus den im Verfahren befindlichen Dokumenten ist der Fachperson eine Basisstation gemäß dem Patentanspruch 11 nicht nahegelegt.

Der wesentliche Unterschied des zum Verfahrensanspruch 1 nebengeordneten Patentanspruch 11 gemäß Hilfsantrag 2A liegt in der Empfangseinheit zum Empfangen einer aktuellen Konfiguration des Endgeräts von dem Endgerät (Merkmal
11.1.2), da der Patentanspruch 11 vorsieht, dass Mittel der Basisstation vorgesehen
sind, um eine aktuelle Konfiguration des Endgeräts von diesem Endgerät zu empfangen (receiving a current configuration of the User Equipment from the User
Equipment), die nach dem Merkmal 11.1.3H weitergeleitet werden kann. Somit handelt es sich bei der „aktuellen Konfiguration“, welche die erste Basisstation weiterleiten kann, um eine Konfiguration, die weder ganz noch teilweise durch die Basisstation festgelegt wird, sondern durch diese (nur) empfangen werden kann (vgl.
hierzu auch Auslegung des Patentanspruchs 11 gemäß geändertem Hauptantrag).


3.6    Dokument NK8 mit Dokument NK9 (CDMA2000-HRDP-Standard)
Der Gegenstand des Patentanspruchs 11 nach Hilfsantrag 2A vom 22. Januar 2025 ist neu gegenüber dem Dokument NK8 mit NK9.

Das Merkmal 11.1.2 ist weder aus dem Dokument NK8 noch dem Dokument NK9
bekannt, da nach dem dort beschriebenen Standard die Festlegung der aktuellen
Konfiguration des Endgeräts (access terminal) nicht von der Basisstation (access
network) empfangen wird, sondern zwischen Endgerät und Basisstation ausgehandelt wird.

In den Dokumenten NK8 und NK9 bezieht sich der Begriff „HRDP session“ auf einen
gemeinsamen Zustand von Zugangsterminal AT und Zugangsnetz AN mit ausgehandeltem und verwendetem Protokoll und Protokollkonfigurationen (NK9, S. 1-6,
Kap. 1.3.2 Definitions, HRPD session: An HRPD session refers to a shared state
between the AT and the AN. This shared state stores the protocols and protocol
configurations that were negotiated and are used for communications between the

                                        54

AT and the AN…). Eine entsprechende ausgehandelte aktuelle Konfiguration ergibt
sich auch implizit aus dem Verweis auf zuvor ausgehandelte Funkschnittstellenprotokolle zwischen Zugangsnetz AN und Zugangsterminal AT (NK9, S. 2-5, Kap. 2.5
A13 (AN-AN) Interface, dritter Abs., zw. Listeneintrag); sowie aus NK9, S. 3-1, Kap.
3.1.1, Punkt a.: …Since no session exists between the AT and AN, a session is
established where protocols and protocol configurations are negotiated, stored and
used for communications between the AT and the AN…).

Eine Einrichtung der (ersten) Basisstation zum Empfangen der aktuellen Konfiguration von einem Endgerät ist den Dokumenten NK8 und NK9 dagegen nicht zu entnehmen.

Für die weiteren, inhaltlich dem Verfahren nach dem Patentanspruch 1 entsprechenden Merkmale des Patentanspruchs 11 gelten die Ausführungen zu den entsprechenden Merkmalen des Patentanspruchs 1, d. h. auch die Merkmale 11.1H,
11.1.3H und 11.3H betreffend den LTE-Standard sind weder dem Dokument NK8
noch dem Dokument NK9 zu entnehmen.


Der Gegenstand des nebengeordneten Patentanspruchs 11 gemäß Hilfsantrag 2A
vom 22. Januar 2025 ist der Fachperson durch den CDMA2000-HRDP-Standard
nach den Dokumenten NK8 und NK9 auch nicht nahegelegt.

Zwar liegt es im Rahmen des fachmännischen Handelns, eine Anpassung der Lehre
des Dokuments NK8 bzw. NK9 an ein LTE-Netzwerk (Merkmale 11.1H, 11.1.3H und
11.3H) vorzunehmen (vgl. Ausführungen zur fehlenden Patentfähigkeit des Patentanspruchs 1 gemäß geändertem Hauptantrag).

Aus der Eignung zum Empfangen einer aktuellen Konfiguration des Endgeräts von
dem Endgerät gemäß dem Merkmal 11.1.2 in Verbindung mit dem Weiterleiten dieser aktuellen Konfiguration des Endgeräts nach Merkmal 11.1.3H folgt aus dem Patentanspruch 11, dass die Basisstation nicht nur zum Empfangen von Konfigurationsinformationen des Endgeräts geeignet sein muss. Vielmehr setzt der Patentanspruch 11 voraus, dass die so empfangene „aktuelle Konfiguration“ des Endgeräts
nach dem Merkmal 11.1.3H auch an die zweite Basisstation weitergeleitet wird. Ein

                                          55

solches Empfangen einer aktuellen Konfiguration des Endgeräts, die auch an die
zweite Basisstation weitergeleitet wird, durch die erste Basisstation, ergibt sich nicht
aus den Dokumenten NK8 und NK9 und ist der Fachperson ausgehend von diesen
auch nicht nahegelegt.

Bei einem Übermitteln von Informationen über die Fähigkeiten des Endgeräts auf
eine entsprechende Anfrage der Basisstation hin, welche die Klägerin in ihrer Replik
mit Verweis auf das CDMA2000-HRDP Standard-Dokument NK8 und dessen
Folgeversion NK8d anführt (NK8d, S. 7-79 „Generic Multimode Capability Discovery
Protocol“-Protokoll), ist bereits fraglich, ob es sich bei Informationen zu den Fähigkeiten des Endgeräts um eine „aktuelle Konfiguration“ dieses Endgeräts im Sinne
des Streitpatents handelt. Darüber hinaus ist für eine in diesem Zusammenhang an
die Basisstation gerichtete „ConfigurationResponse“ (NK8d, S. 7-80) ein Zusammenhang mit der Weiterleitung einer empfangenen aktuellen Konfigurationsinformation von der ersten an eine zweite Basisstation im Rahmen des Handovers nicht
ersichtlich.


Ein Hinweis auf das Empfangen einer aktuellen Konfiguration im Sinne des Merkmals 11.1.2 und eine Veranlassung, von der o. g. Weiterleitung der zwischen Endgerät und Basisstation ausgehandelten Konfiguration abzuweichen, ist den Dokumenten NK8 bzw. NK8d und NK9 nicht zu entnehmen. Der Patentanspruch 11 gemäß Hilfsantrag 2A ergibt sich daher für die Fachperson nicht naheliegend aus dem
CDMA2000-HRDP-Standard und seinem Fachwissen.


3.7    Dokument NK4 (R2-073416) mit Dokument NK5 (R2-073009)
Der Gegenstand des Patentanspruchs 11 nach Hilfsantrag 2A vom 22. Januar 2025 ist neu gegenüber den Dokumenten NK4 und NK5.

Der auf die erste Basisstation bezogene Vorrichtungsanspruch 11 unterscheidet
sich inhaltlich von den Verfahrensmerkmalen des Patentanspruchs 1 insbesondere
im Merkmal 11.1.2, wonach die erste Basisstation eine Empfangseinheit zum Empfangen einer aktuellen Konfiguration des Endgeräts von dem Endgerät umfasst. Das
Merkmal 11.1.2 ist in dem Dokument NK4 nicht offenbart, da die Festlegung der

                                        56

AS-Konfiguration, die als aktuelle Konfiguration nach den Merkmalen 11.1.2,
11.1.3H und 11.2 verstanden werden kann, für die jeweilige Zelle des Mobilfunknetzes und damit durch die jeweilige Basisstation erfolgt. Weder aus dem Dokument
NK4 noch den hier relevanten Stellen des Dokuments NK5 ergibt sich ein Hinweis
darauf, dass diese AS-Konfiguration des Endgeräts durch die erste Basisstation
ausgehend von einem solchen Endgerät empfangen wird. Die Tatsache, dass weitere Parameter des Endgeräts, die einen Beitrag zur aktuellen Konfiguration liefern
können (QoS Measurement Reports), durch die Basisstation empfangen werden
können, begründet nicht, dass die aktuelle, nach dem Merkmal 11.1.3H weiterzuleitende Konfiguration – wie von dem Merkmal 11.1.2 gefordert – von der Basisstation
empfangen werden kann, wobei im Hinblick auf die Realisierung der weiteren Merkmale in dem Dokument NK4 vorliegend auf die AS-Konfiguration als „aktuelle Konfiguration“ Bezug genommen wird.

Für die weiteren, inhaltlich dem Verfahren entsprechenden Merkmale des Patentanspruchs 11 gelten die Ausführungen zu den entsprechenden Merkmalen des Patentanspruchs 1.


Darüber hinaus ist keine Veranlassung für die Fachperson ersichtlich, von der Festlegung der AS-Konfiguration, die in dem Dokument NK4 als aktuelle Konfiguration
nach den Merkmalen 11.1.2, 11.1.3H und 11.2 verstanden werden kann, für die jeweilige Zelle des Mobilfunknetzes und damit durch die jeweilige Basisstation abzuweichen, und in der durch den vorliegenden Hilfsantrag 2A vorgeschlagenen Form
abzuwandeln. Der Gegenstand des Patentanspruchs 11 gemäß Hilfsantrag 2A ist
der Fachperson daher ausgehend von dem Dokument NK4 somit auch nicht nahegelegt.


3.8   Dokument NK10 (EP 1 909 521 A1)
Der Gegenstand des Patentanspruchs 11 nach Hilfsantrag 2A vom 22. Januar
2025 ist neu gegenüber dem Dokument NK10. Das Merkmal 11.1.2 ist in dem Dokument NK10 nicht offenbart. Wenn die Fachperson davon ausgeht, dass es sich
bei dem QoS-Indikator bzw. der damit bezeichnete Prioritätsreihenfolge (priority order) um eine aktuelle Konfiguration handelt, ist eine Eignung der (ersten) Basissta-

                                          57

tion zum Empfangen einer entsprechenden aktuellen Konfiguration – wie vom Merkmal 11.1.2 gefordert – nicht vorgesehen. Vielmehr erfolgt die Festlegung des QoS-Indikators durch die Basisstation und wird dem Endgerät mitgeteilt (vgl. Fig. 7).

Für die weiteren, inhaltlich dem Verfahren entsprechenden Merkmale des Patentanspruchs 11 gelten die Ausführungen zu den entsprechenden Merkmalen des Patentanspruchs 1, d. h. auch das Merkmal 11.2 ist dem Dokument NK10 nicht vollständig zu entnehmen, da das Dokument NK10 keine Aussage dazu trifft, wie mit
dem QoS-Indikator 1, der vom Endgerät als Default-Wert genutzt wird, bei der Übertragung der Messkonfiguration zwischen den Basisstationen beim Handover zu verfahren ist.


Da das Dokument NK10 im Prioritätsintervall des Streitpatents veröffentlicht wurde,
ist es nicht für die Prüfung der erfinderischen Tätigkeit relevant.


3.9    Weitere Entgegenhaltungen
Die vorstehenden Ausführungen zu Anspruch 1 des Hilfsantrags 2A vom 22. Januar 2025 hinsichtlich der Dokumente NK1, NK2 bzw. NK2a, NK3, NK6 und NK7
gelten in gleicher Weise für den Patentanspruch 11 gemäß Hilfsantrag 2A vom
22 Januar 2025. Dessen Gegenstand ist ebenfalls jeweils neu gegenüber den Dokumenten NK1, NK2 bzw. NK2a, NK3, NK6 und NK7 und der Fachperson ausgehend von diesen weiteren Dokumenten auch nicht nahegelegt.




                                          B.
                              Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 Satz 1,
2. Var. ZPO.

                                         58

Dabei hat der Senat berücksichtigt, dass der nach Hilfsantrag 2A als schutzfähig
verbleibende Patentgegenstand gegenüber demjenigen der erteilten und angegriffenen Fassung die Übermittlung einer aktuellen Endgerätekonfiguration im Rahmen
des Handover auf Messkonfigurationen in LTE-Mobilfunknetzen einschränkt, die
darüber hinaus Aktivitätsdaten umfassen, welche vom Endgerät als Referenz für die
durchzuführenden Messungen verwendet werden. Diese Einschränkung macht
nach der Einschätzung des Senats zwei Drittel der wirtschaftlichen Verwertbarkeit
des Streitpatents aus, sodass der Beklagten trotz teilweisem Fortbestand des Streitpatents in beschränkter Fassung in diesem Umfang die Kosten des Verfahrens aufzuerlegen waren.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                         C.
                              Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift, die auch als elektronisches Dokument eingereicht werden
kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung nach den hierfür geltenden gesetzlichen Bestimmungen elektronisch signiert sein, d. h. mit einer qualifizierten elektronischen Signatur nach dem
Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur versehen
sein, die von einer internationalen Organisation auf dem Gebiet des gewerblichen
Rechtsschutzes herausgegeben wird und sich zur Bearbeitung durch das jeweilige
Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das
die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil

                                       59

Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.


Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches Dokument in die elektronische Poststelle des Bundesgerichtshofes (Informationen unter
www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt
mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber
mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt,
wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Werner           Altvater            Matter         Dr. von Hartz       Tischler

                                         60

 Bundespatentgericht
       4 Ni 15/23 (EP)
         (Aktenzeichen)




An Verkündungs Statt zugestellt am

23. April 2025

…
Justizbeschäftigte
als Urkundsbeamtin der Geschäftsstelle
