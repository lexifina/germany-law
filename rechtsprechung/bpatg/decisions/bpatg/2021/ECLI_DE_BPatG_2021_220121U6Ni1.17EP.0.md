---
ecli: "ECLI:DE:BPatG:2021:220121U6Ni1.17EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 1/17"
decided: "2021-01-22"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=1&nr=40429&anz=599&pos=18&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2021-01-22_6_Ni_1_17_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091a.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 1/17 vom 2021-01-22

## Entscheidung

BUNDESPATENTGERICHT

                         IM NAMEN DES VOLKES

                                     URTEIL
                                                                       Zugestellt an
                                                                   Verkündungs Statt am:
 6 Ni 1/17 (EP)
verbunden mit                                                           22.01.2021
6 Ni 12/17 (EP)
verbunden mit
6 Ni 27/18 (EP)




(Aktenzeichen)

                          In der Patentnichtigkeitssache
…


                  betreffend das europäische Patent 0 957 594
                                  (DE 699 24 914)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts aufgrund der
mündlichen Verhandlung vom 28. Oktober 2020 durch die Vorsitzende Richterin
Friehe,   die     Richterin   Werner     sowie     die   Richter    Dipl.-Ing. Müller,
Dipl.-Phys. Univ. Dipl.-Wirtsch.-Phys. Arnoldi und Dipl.-Ing. Matter,


für Recht erkannt:




ECLI:DE:BPatG:2021:220121U6Ni1.17EP.0

                                   -2-



                                         I.


Das europäische Patent 0 957 594 wird mit Wirkung für das Hoheitsgebiet der
Bundesrepublik    Deutschland     teilweise   hinsichtlich   der   angegriffenen
Patentansprüche 3, 7 und 9 für nichtig erklärt, und hinsichtlich der
angegriffenen Patentansprüche 1 und 8 soweit es über folgende Fassung
hinausgeht:

1. A slot timing synchronization method in a code division multiple
   access mobile communication system, said slot timing synchronizing
   method comprising the steps of:

   transmitting from a base station a control signal via perch channels
   (106, 107),

   said perch channels being formed such that a long period code
   assigned to said base station and a first short period code spread a
   first section (102) of one slot of said perch channel and a
   predetermined short period code spreads a second section (131) of
   said one slot; and

   in a mobile terminal, despreading said second section of said one
   slot by using said predetermined short period code, and

   conducting slot timing synchronization by using a correlation value
   obtained as a result of despreading,

   characterized in that

   a spreading factor of said predetermined short period code

         is set to a value lower than a spreading factor of said first short
         period code of said first section and

         is less than 256.

                                   -3-




8. A mobile terminal used in a code division multiple access mobile
   communication system

   in which a base station transmits a control signal via perch channels
   (106, 107) formed such that a long period code assigned to said base
   station and a first short period code spread a first section (102) of one
   slot of said perch channel and a predetermined short period code
   spreads a second section (131) of said one slot,

   said mobile terminal comprising:

   an RF unit (801) for converting a received signal of a carrier
   frequency received from an antenna to a baseband signal; and

   a matched filter (901) for receiving input of said baseband signal,
   despreading said baseband signal by using said second short period
   code (CSC), and outputting a correlation value to establish slot timing
   synchronization,

   characterized in that

   a spreading factor of said predetermined short period code

        has a lower value than a spreading factor of said first short
        period code and

        is less than 256.

                                            -4-




                                                   II.


     Im Übrigen werden die Klagen abgewiesen.



                                                   III.


     Die Kosten des Rechtsstreits tragen die Beteiligten wie folgt:

          Die Gerichtskosten tragen die Klägerinnen gesamtschuldnerisch.

          Die     außergerichtlichen    Kosten           der   Beklagten   tragen    die
          Klägerinnen jeweils zu 1/3.

          Im Übrigen tragen die Parteien ihre Kosten jeweils selbst.


                                                   IV.


     Das Urteil ist gegen Sicherheitsleistung in Höhe von 110% des jeweils zu
     vollstreckenden Betrages vorläufig vollstreckbar.




                                     Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für das Hoheitsgebiet der
Bundesrepublik       Deutschland       erteilten          europäischen     Patents   0 957 594
(Streitpatent),    das   auf   die     europäische             Anmeldung    99102816.8     vom
26. Februar 1999 zurückgeht. Das Streitpatent nimmt die Priorität aus JP 12999598
vom 13. Mai 1998 in Anspruch. Die Anmeldung ist am 17. November 1999 als
EP 0 957 594 A2 veröffentlicht worden.


Das Streitpatent ist am 26. Februar 2019 durch Zeitablauf erloschen.

                                       -5-



Das beim Deutschen Patent- und Markenamt unter dem Aktenzeichen 699 24 914
geführte Streitpatent trägt die Bezeichnung


           Code division multiple access mobile communication system
                       (auf Deutsch laut Streitpatentschrift:
Mobile Kommunikationsanordnung mit Kodeverteilung Mehrfachzugriffsverfahren)


und umfasst in der erteilten Fassung dreizehn Patentansprüche.

                                        -6-



Die angegriffenen unabhängigen Patentansprüche 1 und 8 lauten in der
Verfahrenssprache Englisch laut Streitpatentschrift EP 0 957 594 B1:

     1. A slot timing synchronization method in a code division multiple
         access mobile communication system, said slot timing synchronizing
         method comprising the steps of:
               transmitting from a base station a control signal via perch
               channels (106, 107), said perch channels being formed such
               that a long period code assigned to said base station and a first
               short period code is mapped in a first section (102) of one slot
               of said perch channel and a predetermined short period code is
               mapped in a second section (131) of said one slot; and
               in a mobile terminal, calculating a correlation value for said
               second section of said one slot by using said predetermined
               short period code, and conducting slot timing synchronization
               by using said calculated correlation value,
         characterized in that
         a spreading factor of said predetermined short period code is set to a
         value lower than a spreading factor of said first short period code of
         said first section.


     8. A mobile terminal used in a code division multiple access mobile
         communication system in which a base station transmits a control
         signal via perch channels (106, 107) formed such that a long period
         code assigned to said base station and a first short period code is
         mapped in a first section (102) of one slot of said perch channel and
         a predetermined short period code is mapped in a second section
         (131) of said one slot, said mobile terminal comprising:
                an RF unit (801) for converting a received signal of a carrier
                frequency received from an antenna to a baseband signal; and

                                           -7-



                a matched filter (901) for receiving input of said baseband
                signal and calculating a correlation value for said baseband
                signal by using said second short period code (CSC) to
                establish slot timing synchronization,
         characterized in that
         a spreading factor of said predetermined short period code has a lower
         value than a spreading factor of said first short period code.


In deutscher Sprache lauten sie gemäß Streitpatentschrift EP 0 957 594 B1:

     1. Zeitfenstersynchronisationsverfahren          für      ein        mobiles
         Kommunikationssystem mit Codeverteilung und Mehrfachzugriff, das
         die Schritte des Sendens eines Steuersignals von einer Basisstation
         über Festkanäle (106, 107), die so beschaffen sind, daß ein der
         Basisstation zugeordneter Langcode und ein erster Kurzcode in
         einem ersten Abschnitt (102) eines Fensters des Festkanals und ein
         vorgegebener Kurzcode in einem zweiten Abschnitt (131) des einen
         Fensters    enthalten     sind,     und    der     Berechnung      eines
         Korrelationswerts für den zweiten Abschnitt des einen Fensters unter
         Verwendung des vorgegebenen Kurzcodes durch einen mobilen
         Anschluß sowie der Ausführung einer Zeitfenstersynchronisation
         unter Verwendung des berechneten Korrelationswerts umfaßt;
         dadurch gekennzeichnet, daß
         der Ausbreitungsfaktor des vorgegebenen Kurzcodes auf einen
         geringeren Wert als der Ausbreitungsfaktor des ersten Kurzcodes
         des ersten Abschnitts eingestellt ist.


     8. Mobilanschluß      für   ein   mobiles     Kommunikationssystem       mit
         Codeverteilung und Mehrfachzugriff, bei dem eine Basisstation ein
         Steuersignal über Festkanäle (106, 107) überträgt, die so beschaffen
         sind, daß ein der Basisstation zugeordneter Langcode und ein erster

                                        -8-



         Kurzcode in einem ersten Abschnitt (102) eines Fensters des
         Festkanals und ein vorgegebener Kurzcode in einem zweiten
         Abschnitt (131) des einen Fensters enthalten sind, wobei der mobile
         Anschluß
         eine RF-Einheit (801) zum Umwandeln eines von einer Antenne
         empfangenen        Signals   aus   einer   Trägerfrequenz   in    ein
         Basisbandsignal und
         ein angepaßtes Filter (901) zum Empfangen eines Eingangs des
         Basisbandsignals und zum Berechnen eines Korrelationswerts für
         das Basisbandsignal unter Verwendung des zweiten Kurzcodes
         (CSC) zur Herstellung einer Zeitfenstersynchronisation umfaßt,
         dadurch gekennzeichnet, daß
         der   Ausbreitungsfaktor     des   vorgegebenen   Kurzcodes      einen
         niedrigeren Wert als der Ausbreitungsfaktor des ersten Kurzcodes
         aufweist.


Die weiteren angegriffenen Patentansprüche sind auf diese Patentansprüche
unmittelbar oder mittelbar rückbezogen.


Die Klägerinnen sind der Ansicht, dass das Streitpatent jeweils im Umfang ihres
Angriffs wegen der Nichtigkeitsgründe der mangelnden Patentfähigkeit und der
unzulässigen Erweiterung für nichtig zu erklären sei.


Den Einwand der fehlenden Patentfähigkeit stützen die Klägerinnen u.a. auf die
folgenden Druckschriften:

                                         -9-



Bezeichnung     Veröffentlichungsnum-           Bezeich-   Bezeich-   Bezeichdes Senats      mer bzw. Titel                  nung der   nung der   nung der
                                                Klägerin   Klägerin   Klägerin
                                                zu 1       zu 2       zu 3
WO 246          WO 98/47246 A1                  ZP10                  D1
EP 211          EP 1 011 211 A1                 ZP10A      D5         D1a
ARIB V. 0       (Draft) Volume 1                ZP14
                Requirements and
                Objectives for a 3G Mobile
                Services and System Ver.0
                Issued. Association or
                Radio Industries and
                Businesses (ARIB). S. I –
                VII, 1 – 204.
                Volume 3 Specification of
                Air-Interface for the 3G
                mobile system. S. i, 1 – 71,
                i, ii, 72 – 111, i, ii, 112 –
                135, 1 – 33, Annex
ARIB V. 0-1.0   enthält u. a. SWG2: Volume ZP14g
                3 Specifications Ver. 0-4.0
                July 25, 1997, S. 169 - 292
ARIB V. 0-4.0   enthält u. a. SWG2:             ZP14h
= ARIB-         Volume 3 Specifications of
Standard        Air-Interface for 3G Mobile
                System Ver. 0-4.0
                December 18, 1997, S.
                174 - 363

                                     - 10 -



ARIB V. 0.5     Volume 3 Specifications of    ZP14A
                Air-Interface for 3G Mobile
                System Ver.0.5 Issued 0.0
                December 18th, 1997;
                Revision 0.5 July 21th,
                1998. Inhaltsverzeichnis,
                S. 1 – 126, Annex
ARIB Articles   Articles of Association of    ZP14m
                the Telecommunications
                Technology Association of
                Korea (TTA), July 6, 2000;
                S. 1 - 11
Higuchi_IEICE   HIGUCHI, K.; et al: Fast      ZP9     D1   D13
                Cell Search Algorithm                      MN8
                using Long Code Masking
                in DS-CDMA
                Asynchronous Cellular
                Systems, The Institute of
                Electronics, Information
                and Communication
                Engineers, Technical
                Report of IEICE, DSP96-
                116, SAT96-111, RCS96-
                112 (1997-01), S. 57 - 63

                                      - 11 -



Higuchi_IEICE   Übersetzung von                       D1a
deutsch         Higuchi_IEICE: Schneller
                Zellsuchalgorithmus unter
                Verwendung einer
                Langcodemaskierung in
                einem asynchronen
                zellularen DS-CDMA-System, S. 1 - 17
Higuchi_IEEE    Higuchi et al.: Fast Cell      ZP8    D2    D12
                Search Algorithm in DS-CDMA mobile radio using
                long spreading codes,
                IEEE 47th Vehicular
                Technology Conference, 4.
                - 7. Mai 1997, ISBN 0-
                7803-3659-3, S. 1430 -
                1434
Nakamura_       NAKAMURA, T; et al:            ZP12         D3
IEEE            Configuration and
                Characteristics Estimation
                of a W-CDMA experimental
                System for third generation
                mobile communications,
                IEEE Vehicular Technology
                Conference VTC’98, 18. -
                21. Mai 1998, Ottawa,
                Ontario, Kanada, S. 973 -
                977

                                      - 12 -



 Ireland –       Concept Group Alpha -         ZP11     D3          D2
 WCDMA           Wideband Direct-Sequence CDMA (WCDMA)
                 EVALUATION
                 DOCUMENT (3.0) Part 1:
                 System Description
                 Performance Evaluation.
                 ETSI SMG 2 Meeting no
                 24, Cork, Ireland 1 - 5
                 December 1997. Tdoc
                 SMG2 359/97. S. 1 - 52
 TR 146          TR 101 146 V3.0.0 (1997-                           D6
                 12) Technical Report
                 Universal Mobile
                 Telecommunications
                 System (UMTS);
                 UMTS Terrestrial Radio
                 Access (UTRA); Concept
                 evaluation
                 (UMTS 30.06 version
                 3.0.0), ETSI, Deckblatt, S.
                 1 bis 689
 EP 315          EP 0 797 315 A2                        D4          D5
 EP 737          EP 0 825 737 A1               ZP5                  D9


Die Klägerin   zu 1 hat       mit ihrer am 20. Dezember 2016 eingereichten
Nichtigkeitsklage [6 Ni 1/17 (EP)] das Streitpatent zunächst im Umfang der
Patentansprüche 1, 8 und 12, die Klägerin zu 2 mit ihrer am 8. Februar 2017
eingereichten Nichtigkeitsklage [6 Ni 12/17 (EP)] zunächst im Umfang der
Patentansprüche 1 und 8 und die Klägerin zu 3 mit ihrer am 18. April 2018
eingereichten Nichtigkeitsklage [6 Ni 27/18 (EP)] im Umfang der Patentansprüche

                                       - 13 -



1 und 8 angegriffen. Mit Schriftsatz vom 20. Januar 2020 hat die Klägerin zu 1 ihren
Angriff auf die Patentansprüche 3, 4, 7 und 9 erweitert und ihren Angriff auf den
Patentanspruch 12 für erledigt erklärt. Mit Schriftsatz vom 20. Januar 2020 hat die
Klägerin zu 2 ihren Angriff auf die Patentansprüche 3, 7 und 9 erweitert. Die
Beklagte    hat   den     Erweiterungen     der   Nichtigkeitsklagen   sowie    der
Teilerledigterklärung zugestimmt.


Die Klägerin zu 1 beantragt nun,


        das europäische Patent 0 957 594 mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der
        Patentansprüche 1, 3, 7, 8, und 9 für nichtig zu erklären.


Die Klägerin zu 2 beantragt nun,


        das europäische Patent 0 957 594 mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der
        Patentansprüche 1, 3, 7, 8 und 9 für nichtig zu erklären.


Die Klägerin zu 3 beantragt,


        das europäische Patent 0 957 594 mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der
        Patentansprüche 1 und 8 für nichtig zu erklären.


Die Beklagte beantragt,

        die Klagen abzuweisen,

        hilfsweise die Klagen abzuweisen,
        soweit sie sich auch gegen eine der Fassungen des Streitpatents
        nach den (geschlossenen) Hilfsanträgen A.1, A.2, A.3, A.4, A.5,

                                         - 14 -



        B.1, B.2, B.3, B.4, B.5, B.6, B.7, C.1, C.2 und C.3 vom
        10. Februar 2020 (in dieser Reihenfolge), nach dem Hilfsantrag
        B.6‘ aus der mündlichen Verhandlung vom 19. Februar 2020 mit
        den entsprechenden Maßgaben aus der mündlichen Verhandlung
        vom 19. Februar 2020, sowie nach den Hilfsanträgen D.1, D.2 und
        C.4 aus dem Schriftsatz vom 16. Oktober 2020, die nachrangig zu
        dem Hilfsantrag B.6 und vor Hilfsantrag B.7 und Folgende gestellt
        sein sollen, richten, wobei der Hilfsantrag B.6‘ als allererster
        Hilfsantrag nach dem Hauptantrag gestellt sein soll.


Wegen des Wortlauts der Ansprüche 1 und 8 nach Hilfsantrags B.6‘ wird auf den
Tenor verwiesen.


Von der zunächst beschränkten Verteidigung der Patentansprüche 3, 7 und 9 im
Hilfsantrag B.6‘ hat die Beklagte in der mündlichen Verhandlung letztlich ganz
abgesehen.


Wegen des Wortlauts der Ansprüche nach den Hilfsanträgen A.1, A.2, A.3, A.4, A.5,
B.1, B.2, B.3, B.4, B.5, B.6, B.7, C.1, C.2 und C.3 sowie D.1, D.2 und C.4 wird auf
die Akte und dabei auch auf das Protokoll der mündlichen Verhandlung vom
19. Februar 2020 verwiesen.


Die Beklagte tritt der Argumentation der Klägerinnen entgegen und hält den
Gegenstand des Streitpatents in der erteilten Fassung, wenigstens in einer der
verteidigten Fassung, für schutzfähig.


Zur Stützung ihres Vorbringens beruft sie sich u. a. auf folgende Druckschriften:

                                           - 15 -



 Bezeichnung       Veröffentlichungsnummer bzw. Titel         Bezeichnung der
 des Senats                                                   Beklagten
 Glisic            GLISIC, S.; VUCETIC, B.: Spread            D…4
                   spectrum CDMA systems for wireless
                   communications. Artech House. 1997.
                   ISBN 0-89006-858-5. S. iii – xvi, 1 - 47
 Kaaranen          KAARANEN, H.; et. al.: UMTS                D…8
                   Networks Architecture, Mobility and
                   Services. Second Edition. John Wiley
                   & Sons, Ltd. 2005. ISBN 0-470-01103-
                   3. S. v – ix, 59 - 75


Die Klägerinnen rügen den in der mündlichen Verhandlung am 19. Februar 2020
gestellten Hilfsantrag B.6‘ als verspätet.


Die Beklagte rügt die Angriffe der Klägerin zu 1 in der mündlichen Verhandlung vom
19. Februar 2020 zur fehlenden Patentfähigkeit gestützt auf den im ARIB-Standard
(ZP14 und ZP14a) dargestellten TDD-Modus bzw. gestützt auf den ARIB TDD-Modus in Kombination mit der Druckschrift „Higuchi_IEEE“ (= ZP8) als verspätet.


Der Senat hat den Parteien einen qualifizierten Hinweis vom 13. September 2019
zugeleitet und hierin Fristen zur Stellungnahme auf den Hinweis und auf etwaiges
Vorbringen der jeweiligen Gegenpartei gesetzt.


Die Beklagte hat aus den Patentansprüchen 1 und 8 des Streitpatents
Verletzungsklagen gegen die Klägerinnen geführt. Die Klage vom 5. Juli 2016
gegen die Klägerin zu 1 hat das Landgericht … abgewiesen und die Berufung ist
beim Oberlandesgericht … anhängig. Die Klage gegen die Klägerin zu 2 hat das
Landgericht … ebenfalls abgewiesen und auch die dagegen eingelegte Berufung
ist beim Oberlandesgericht München … anhängig. Der Klage vom 24. Oktober 2017
gegen die Klägerin zu 3 hat das Landgericht … mit Urteil vom 28. Januar 2020

                                       - 16 -



stattgegeben und die dagegen erhobene Berufung ist beim Oberlandesgericht …
anhängig.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                          Entscheidungsgründe


                                        A.


Die Klagen sind zulässig, haben in der Sache aber nur teilweise Erfolg, und zwar
hinsichtlich der angegriffenen Patentansprüche in der erteilten Fassung. Denn der
erteilten Fassung stehen die Nichtigkeitsgründe der unzulässigen Erweiterung
gemäß Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 Buchst. c) EPÜ und auch
der fehlenden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138
Abs. 1 Buchst. a) i. V. m. Art. 52, 54 EPÜ entgegen.


In der ebenfalls verteidigten Fassung nach Hilfsantrag B.6‘ erweist sich das Streitpatent dagegen im Umfang der beschränkt verteidigten Patentansprüche 1 und 8
als schutzfähig, so dass die Klagen, soweit sie sich auch gegen diese Fassung
richten, teilweise abzuweisen sind. Da die Beklagte in dem geschlossen gestellten
Hilfsantrag B.6‘ die Patentansprüche 3, 7 und 9 nicht (mehr) verteidigt, sind die
Klagen der Klägerinnen zu 1 und 2 allerdings auch insoweit erfolgreich.


                          I. Zur Zulässigkeit der Klagen


Die Klagen sind trotz Erlöschen des Streitpatents mit Zeitablauf am 26. Februar
2019 zulässig; durch das Erlöschen des Streitpatents ist das Rechtsschutzbedürfnis
der Klägerinnen nicht entfallen.
Die Frage, ob ein eigenes Rechtsschutzinteresse vorliegt, darf nicht nach allzu
strengen Maßstäben beurteilt werden. Soll eine Nichtigkeitsklage der vorbeugenden

                                        - 17 -



Abwehr von Ansprüchen dienen, ist nicht ausschlaggebend, ob diese bereits
geltend gemacht oder auch nur angekündigt sind. Hinreichender Anlass,
gerichtlichen Rechtsschutz in Anspruch zu nehmen, besteht vielmehr schon dann,
wenn der Kläger Anlass zu der Besorgnis hat, er könne auch nach Ablauf der
Schutzdauer noch Ansprüchen wegen zurückliegender Handlungen ausgesetzt
sein. Ein Rechtsschutzinteresse darf in solchen Fällen nur dann verneint werden,
wenn eine solche Inanspruchnahme ernstlich nicht mehr in Betracht kommt (BGH,
Urteil vom 13. Juli 2020 – X ZR 90/18 – Signalübertragungssystem Rn. 28 ff.;
Beschluss vom 14. Februar 1995 - X ZB 19/94, GRUR 1995, 342 f. -Tafelförmige
Elemente).


Ausgehend     von    diesen    Grundsätzen       hat   der   Bundesgerichtshof   ein
Rechtsschutzinteresse zum Beispiel für den Fall bejaht, dass der Patentinhaber
eine bereits erhobene Verletzungsklage zurücknimmt, einen Verzicht auf eventuelle
Ansprüche aus dem Streitpatent aber ablehnt (BGH, Urteil vom 9. September 2010
- Xa ZR 14/10, GRUR 2010, 1084 Rn. 10 - Windenergiekonverter).


Eine damit vergleichbare Konstellation liegt auch im Streitfall vor.
Die Beklagte nimmt die Klägerinnen zu 1 und 2 vor dem Landgericht … bzw.
inzwischen in den vor dem Oberlandesgericht … anhängigen Berufungen und die
Klägerin zu 3 vor dem Landgericht … bzw. inzwischen in der vor dem
Oberlandesgericht … anhängigen Berufung jeweils wegen Verletzung des
Streitpatents hinsichtlich der Patentansprüche 1 und 8 in Anspruch. Zudem hat die
Beklagte keine Erklärung dahingehend abgegeben, sich gegenüber den
Klägerinnen keiner Ansprüche aus einem unabhängigen Patentanspruch mehr zu
berühmen. Auch von einer Freistellung der Klägerinnen durch die Beklagte für die
Vergangenheit ist nichts ersichtlich.

                                        - 18 -




                     II. Zum Gegenstand des Streitpatents


1.     Das Streitpatent betrifft die Synchronisation eines mobilen Endgeräts mit
einer Basisstation eines CDMA-Mobilfunksystems. Im Streitpatent ist ausgeführt, zu
Beginn einer Kommunikation oder bei einem Wechsel in eine andere Funkzelle
(hand over) führe das mobile Endgerät eine dreistufige Zellensuche durch, wobei
eine Zeitschlitz- und Rahmensynchronisation sowie eine Erfassung eines
basisstationsspezifischen     Spreizcodes        ausgeführt    werde.   Gemäß     der
Veröffentlichung „Higuchi_IEICE“ spreize eine Basisstation auf einem ersten von
zwei    Steuerkanälen       die   zu   übertragenden          Symbole   durch   einen
basisstationsspezifischen     Lang-    und   einen     kanalspezifischen   Kurzcode,
wohingegen ein sich am Ende eines jeden Zeitschlitzes befindliches Symbol nur
durch den „gemeinsamen Kurzcode“ CSC (common short code) gespreizt werde.
Der CSC sei spezifisch für das Mobilfunksystem und den mobilen Endgeräten
bekannt. Im ersten Schritt der Zellensuche ermittle ein mobiles Endgerät die
Zeitschlitzsynchronisation auf der Basis der Größe eines Korrelationswertes, den
es durch Entspreizen des ersten Steuerkanals unter Verwendung des ihm
bekannten CSC erhalte. Im zweiten Schritt detektiere das mobile Endgerät den
sogenannten Gruppenidentifizierungskurzcode GISC (group identification short
code), der eine Gruppe von Langcodes kennzeichne und auf dem zweiten
Steuerkanal übertragen werde. Dazu entspreize das mobile Endgerät den zweiten
Steuerkanal mit allen ihm bekannten GISCs unter Beachtung der zuvor erhaltenen
Zeitschlitzsynchronisation. Im dritten Schritt der Zellensuche entspreize das mobile
Endgerät die Steuerkanäle mit denjenigen Langcodes, die zu der im zweiten Schritt
ermittelten Langcodegruppe gehören, und detektiere somit den gesuchten
basisstationsspezifischen Langcode.

                                           - 19 -



Der erste Schritt, die Zeitschlitzsynchronisation, nehme die meiste Zeit in Anspruch,
da bei einem CSC der Länge 256 (Chips) und einem signalangepassten Filter
(matched filter) mit 64 Koeffizienten bzw. Anschlüssen (taps) die Koeffizienten
viermal umzuschalten seien. Ein Filter mit 256 statt 64 Anschlüssen vermeide zwar
diese Umschaltung und verkürze damit die Zeitschlitzsynchronisation, habe jedoch
eine sehr große Gatterzahl und einen hohen Stromverbrauch (Streitpatentschrift,
i. F. mit SPS bezeichnet, Abs. 0001 – 0003, 0007 – 0013).


2.       Um eine schnelle Zellensuche trotz eines Filters mit geringer Gatterzahl und
niedrigem Stromverbrauch zu ermöglichen (SPS, Abs. 0014) schlägt das
Streitpatent nach dem Anspruch 1 in der erteilten Fassung ein Verfahren vor, das
sich wie folgt gliedern lässt (Merkmale in Deutsch weichen von der fehlerhaften
Fassung der Streitpatentschrift ab):


     1.          Zeitschlitzsynchronisationsverfahren für ein mobiles CDMA-Kommunikationssystem, umfassend die Schritte:
                     A slot timing synchronization method in a code
                     division   multiple   access   mobile   communication
                     system, said slot timing synchronizing method
                     comprising the steps of:
     2           Senden eines SteuersignaIs von einer Basisstation über
                 Festkanäle (106, 107), die so beschaffen sind, dass
                     transmitting from a base station a control signal via
                     perch channels (106, 107), said perch channels being
                     formed such that
     2.1         ein der Basisstation zugeordneter Langcode und
                     a long period code assigned to said base station and
     2.2         ein erster Kurzcode auf einen ersten Abschnitt (102) eines
                 Zeitschlitzes des Festkanals abgebildet sind und
                     a first short period code is mapped in a first section
                     (102) of one slot of said perch channel and

                                         - 20 -



     2.3      ein vorgegebener Kurzcode auf einen zweiten Abschnitt (131)
              des einen Zeitschlitzes abgebildet ist, und
                  a predetermined short period code is mapped in a
                  second section (131) of said one slot; and
     3        in einem mobilen Endgerät,
                  in a mobile terminal
     3.1      Berechnung eines Korrelationswerts für den zweiten Abschnitt
              des einen Zeitschlitzes unter Verwendung des vorgegebenen
              Kurzcodes und
                  calculating a correlation value for said second section
                  of said one slot by using said predetermined short
                  period code, and
     3.2      Ausführen einer Zeitschlitzsynchronisation unter Verwendung
              des berechneten Korrelationswerts
                  conducting slot timing synchronization by using said
                  calculated correlation value,
     4        dadurch     gekennzeichnet,         dass     ein    Spreizfaktor   des
              vorgegebenen Kurzcodes auf einen niedrigeren Wert als ein
              Spreizfaktor des ersten Kurzcodes des ersten Abschnitts
              eingestellt ist.
                  characterized in that a spreading factor of said
                  predetermined short period code is set to a value
                  lower than a spreading factor of said first short period
                  code of said first section.


Der auf ein mobiles Endgerät gerichtete Anspruch 8 lautet gegliedert:


     3        Mobiles       Endgerät        für      ein         mobiles     CDMA-Kommunikationssystem, bei dem
                  A mobile terminal used in a code division multiple
                  access mobile communication system in which

                                - 21 -



2      eine Basisstation ein Steuersignal über Festkanäle(106, 107)
       überträgt, die so beschaffen sind, dass
           a base station transmits a control signal via perch
           channels (106, 107) formed such that
2.1    ein der Basisstation zugeordneter Langcode und
           a long period code assigned to said base station and
2.2    ein erster Kurzcode auf einen ersten Abschnitt (102) eines
       Zeitschlitzes des Festkanals abgebildet sind und
           a first short period code is mapped in a first section
           (102) of one slot of said perch channel and
2.3    ein vorgegebener Kurzcode auf einen zweiten Abschnitt (131)
       des einen Zeitschlitzes abgebildet ist,
           a predetermined short period code is mapped in a
           second section (131) of said one slot,
3      wobei das mobile Endgerät,
           said mobile terminal comprising:
3.3    eine RF-Einheit (801) zum Umwandeln eines von einer Antenne
       empfangenen Signals, das eine Trägerfrequenz hat, in ein
       Basisbandsignal und
           an RF unit (801) for converting a received signal of a
           carrier frequency received from an antenna to a
           baseband signal; and
3.4    ein signalangepasstes Filter (901) zum Empfangen des
       Basisbandsignals und
           a matched filter (901) for receiving input of said
           baseband signal and
3.1_3.2 zum    Berechnen      eines      Korrelationswerts   für    das
       Basisbandsignal unter Verwendung des zweiten Kurzcodes
       (CSC) zur Herstellung einer Zeitschlitzsynchronisation umfaßt

                                             - 22 -



                    calculating a correlation value for said baseband
                    signal by using said second short period code (CSC)
                    to establish slot timing synchronization,
     4          dadurch     gekennzeichnet,           dass   ein   Spreizfaktor   des
                vorgegebenen Kurzcodes einen niedrigeren Wert als ein
                Spreizfaktor des ersten Kurzcodes des ersten Abschnitts hat.
                    characterized in that a spreading factor of said
                    predetermined short period code has a lower value
                    than a spreading factor of said first short period code
                    of said first section.


3.       Fachmann ist ein Ingenieur (Diplom oder Master) der Fachrichtung Elektrooder Nachrichtentechnik, der über eine mehrjährige Berufserfahrung sowie
einschlägige Kenntnisse auf dem Gebiet der Konzeption von Mobilfunksystemen
verfügt, insbesondere im Bereich der Synchronisation und Codierung bei CDMA-Systemen. Bei diesem Fachmann sind Kenntnisse der vor dem Prioritätszeitpunkt
geltenden einschlägigen Normen und Konzeptstudien sowie der dafür zur
Anwendung kommenden Gerätschaften als bekannt vorauszusetzen.


4.       Die Ansprüche 1 und 8 bedürfen teilweise der Erläuterung:


a)       Mobile CDMA-Kommunikationssysteme (code division multiple access; SPS,
Abs. 0001, 0018, 0024; Merkmal 1) waren dem Fachmann bereits vor dem
Prioritätstag bekannt (Higuchi_IEICE_deutsch, Titel; Higuchi_IEEE, Titel; EP 737,
Sp. 1, Z. 5 – 10; TR 146, S. 10, Tab. 1, Z. 1; Ireland-WCDMA, Titel; EP 315, Titel).
Zwischen einer Basisstation und mobilen Endgeräten (Merkmal 3) findet im Downund Uplink jeweils eine Vielzahl von Signalübertragungen, ggfs. zeit- und
frequenzgleich, statt. Die Funkverbindungen sind in Rahmen (frames) mit fester
Länge (z. B. 10 ms) unterteilt, welche jeweils mehrere (z. B. 15 oder 16) Zeitschlitze
(time slots) umfassen (SPS, Abs. 0002; Higuchi_IEEE, S. 1432, li. Sp., letzter Abs.;
TR 146, S. 11, letzter Abs.; Kaaranen, S. 73, Fig. 4.10). Die einzelnen Signale sind

                                       - 23 -



unterschiedlich codiert, so dass ein Empfänger ein an ihn gerichtetes Signal mit
Hilfe „seines“ Codes in dem Signalgemisch detektieren kann. Durch die
Verwendung zueinander orthogonaler Codes mit sehr kleiner Kreuzkorrelation
(Higuchi_IEEE, S. 1430, li. Sp., Kap. I, Abs. 1; TR 146, S. 34, Kap. 2.4.4.1.2,
Abs. 3; EP 737, Sp. 19, Z. 15 - 17) stören sich die Signale gegenseitig nur wenig.

                                           - 24 -



b)    Unter den im Merkmal 2 genannten Festkanälen (perch channels) versteht
der Fachmann physikalische Downlink-Kanäle, über die eine Basisstation
Steuersignale mit regelmäßig konstanter Leistung an die mobilen Endgeräte
aussendet (SPS, Abs. 0007, 0010; Higuchi_IEEE, Abstract; EP 737, Sp. 14, Z. 1).
Nach Figur 1 der Streitpatentschrift werden zwei Festkanäle (106, 107) (code-)
multiplexiert, wobei über den ersten Kanal (106) in einem ersten (Merkmal 2.2) und
in einem zweiten Abschnitt (Merkmal 2.3) jedes Zeitschlitzes Signale übertragen
werden, über den zweiten Kanal (107) jedoch nur im zweiten Abschnitt:




        Streitpatentschrift, Fig. 1 mit Kolorierung und Kommentierung durch den Senat


Vor diesem Hintergrund versteht der Fachmann die Angaben in den Merkmalen 2
bis 2.3 so, dass zwar mehrere Festkanäle vorhanden sind, die Merkmale 2.1 bis 2.3
sich jedoch nur auf einen dieser Festkanäle (nach den Ausführungsbeispielen den
ersten von zweien) beziehen.


c)    Bei einem DS(SS)-CDMA-Mobilfunksystem (direct sequence (spread
spectrum), Higuchi_IEICE_deutsch, Titel; Higuchi_IEEE, Titel; TR 146, S. 8;
EP 737, A. 1) wird jedes Symbol des zu übertragenden Signals, das eine relativ
niedrige Frequenz bzw. Symbolrate fs hat (SPS, Abs. 0024: 16 ksps, kilo symbols
per second), mit einem Vektor multipliziert, der eine Vielzahl von Elementen, „Chips“
genannt, aufweist. Das resultierende Signal hat eine um diese Chipanzahl je

                                           - 25 -



Symbol vergrößerte Frequenz, die als Chiprate fc bezeichnet wird und bei den vor
dem Prioritätszeitpunkt bekannten CDMA-Mobilfunksystemen typischerweise
4,096 Mcps (mega chips per second) beträgt (Higuchi_IEICE, S. 9, Tab. 1;
Higuchi_IEEE, S. 1432, Tab. 1; TR 146, S. 10, Tab. 1).


Das Verhältnis von Chiprate fc zur Symbolrate fs ist der im Merkmal 4 genannte
Spreizfaktor (spreading factor; Kaaranen, S. 63), der die Bandbreitenerhöhung des
Frequenzspektrums des zu übertragenden Signals beschreibt. Es gilt:


             Spreizfaktor SF = fc/fs= Ts/Tc = Anzahl der Chips je Symbol


Während die Chiprate in einem mobilen CDMA-Kommunikationssystem fest
vorgegebenen ist, wird der Spreizfaktor im Betrieb auf den einzelnen
Verkehrskanälen bedarfsweise verändert, womit sich variable Symbolraten
realisieren lassen (Kaaranen, S. 64, Tab. 4.2, 4.3; TR 146, S. 12, Abs. 1). Durch die
spektrale Spreizung der zu übertragenden Signale sind DS(SS)-CDMA-Verbindungen wenig anfällig gegenüber Störsignalen und Fading-Effekten (Glisic,
S. xiii, Abs. 2; EP 315, S. 2, li. Sp., Abs. 1).


d)     Eine Basisstation verwendet für jeden ihrer Downlink-Kanäle einen eigenen
Spreizcode, der als Kanalisierungscode (channelization code) oder Kurzcode (short
code) bezeichnet wird (SPS, Sp. 2, Z. 36 - 39; Higuchi_IEICE_deutsch, S. 3,
Z. 12 - 14; Higuchi_IEEE, S. 1430, re. Sp., Abs. 1; TR 146, S. 12, Abs. 1; Glisic,
S. 10, vorletzter Abs.). Die Länge des Kurzcodes, d. h. die Anzahl seiner Elemente,
ist gleich dem Spreizfaktor und bewegt sich bei einem System mit einer Chiprate
von 4,096 Mcps typischerweise in einem Bereich von 4 bis 256 (TR 146, S. 12,
Abs. 1).


Nach den Ausführungsbeispielen des Streitpatents ist der auf den Festkanälen
(perch channels) der Basisstation verwendete Kurzcode der im Merkmal 2.2
genannte „erste Kurzcode“ (first short period code). Er hat eine Länge von 256

                                          - 26 -



Chips, d. h. einen Spreizfaktor von 256 (SPS, Abs. 0024), womit sich bei einer
Symbolrate von 16 ksps (SPS, Abs. 0024) die aus dem Stand der Technik bekannte
Chiprate von 4,096 Mcps ergibt.


e)     Um die Signale der einzelnen Basisstationen voneinander unterscheidbar zu
machen,    erfolgt   neben       der   Bandspreizung   der   Symbole   mittels   des
kanalspezifischen Kurzcodes eine Verwürfelung (scrambling) des gespreizten
Signals durch eine chipweise Multiplikation mit einem basisstationsspezifischen
Langcode (long code), der bedeutend länger als die Kurzcodes ist (SPS, Abs. 0008;
Higuchi_IEICI_deutsch, S. 9, Tab. 1; TR 146, S. 12, Abs. 2; Kaaranen, S. 64,
Tab. 4.4). Die Anzahl der Chips pro Symbol, d. h. der Spreizfaktor, wird durch die
Multiplikation mit dem Langcode zwar nicht geändert, das Spektrum des
resultierenden Signals jedoch „gleichmäßiger“. Insofern ist auch der Langcode ein
„Spreizcode“ (SPS, Abs. 0007, 0008; A.e 6, 7, 9) und wird vom Fachmann auch so
bezeichnet (Higuchi_IEICE_deutsch, S. 3, Z. 10 - 12; Higuchi_IEEE, Titel; EP 737,
Sp. 12, Z. 55 – Sp. 13, Z. 5).


Nach den Ausführungsbeispielen des Streitpatents ist der basisstationsspezifische
Code der im Merkmal 2.1 genannte Langcode.


f)     Unter „Abbilden“ (is mapped in) (Merkmale 2.1, 2.2) versteht der Fachmann,
dass die Elemente des Langcodes und des ersten Kurzcodes jeweils eine
Definitionsmenge bilden, auf die eine jeweilige beliebige mathematische Funktion
angewendet wird. Die entsprechenden Wertemengen sind im ersten Abschnitt eines
Zeitschlitzes enthalten. Von Symbolen ist im Anspruch 1 keine Rede.


Insofern ist das vorstehend beschriebene Spreizen jedes zu übertragenden
Symbols durch den Langcode und den ersten Kurzcode eine Konkretisierung des
„Abbildens“ dieser Codes.

                                              - 27 -



Das gilt auch für das „Abbilden“ des vorgegebenen Kurzcodes auf den zweiten
Abschnitt des Zeitschlitzes (Merkmal 2.3). Dieser kann somit in beliebig veränderter
Weise im zweiten Abschnitt enthalten sein, beispielsweise durch mehrfaches
Einfügen in den zweiten Abschnitt.


g)     Nach dem Einschalten bzw. bei einem bevorstehenden Wechsel in eine
andere Funkzelle muss ein mobiles Endgerät sich auf die Zeitschlitze der von der
Basisstation ausgesendeten Festkanäle synchronisieren (Merkmale 1, 3.2), wobei
es den basisstationsspezifischen Langcode zunächst nicht kennt. Daher wird am
Ende jedes Zeitschlitzes eines ersten Festkanals, also im „zweiten Abschnitt“, nur
der den mobilen Endgeräten bekannte „vorgegebene Kurzcode“ (predetermined
short code, CSC = common short code) nach Merkmal 2.3 übertragen, wie dies in
der Figur 1 der Streitpatentschrift dargestellt ist. Dabei wird in diesem Abschnitt ein
fiktives,   weil     nicht     informationstragendes           „Symbol          gespreizt“.   Eine
Informationsübertragung mit Hilfe dieses „Symbols“ würde dazu führen, dass der
vorgegebene        Kurzcode    im mobilen         Endgerät      nicht mehr          wunschgemäß
ausgewertet werden könnte.


Dieser zweite Abschnitt des Zeitschlitzes wird als long code masked symbol section
bezeichnet, weil dort der basisstationsspezifische Langcode „maskiert“, d. h. nicht
verwendet wird (SPS, Abs. 0007, 0010, Fig. 2; Higuchi_IEICE_deutsch; S. 4, Fig. 2;
Higuchi_IEEE, S. 1430, re. Sp., Abs. 2):




                      Streitpatentschrift, Fig. 2, mit Kolorierung des Senats

                                           - 28 -



h)    Nach Merkmal 4 ist der Spreizfaktor des vorbestimmten Kurzcodes (CSC)
kleiner als der Spreizfaktor des ersten Kurzcodes, was aufgrund der festen Chiprate
gleichbedeutend mit einer Reduzierung der zeitlichen Länge des CSC ist. Da der
CSC nach den Ausführungsbeispielen des Streitpatents nur einmal in den zweiten
Abschnitt eingefügt ist und zudem der zweite Abschnitt, die long code masked
symbol section, aus Gründen der Rückwärtskompatibilität unverändert lang bleiben
muss (SPS, Abs. 0026), kann der verkürzte CSC an verschiedenen Positionen im
zweiten Abschnitt platziert werden. Nach Figur 3 des Streitpatents wird die Länge
des CSC von 256 auf 64 Chips reduziert, so dass sich vier mögliche Positionen
ergeben:




                   Streitpatentschrift, Fig. 3, mit Kolorierung des Senats


Durch die reduzierte Länge des CSC kann zwar wie gewünscht die
Zeitschlitzsynchronisation schneller ausgeführt werden, jedoch stünde für die
Detektion des CSC weniger Energie zur Verfügung. Zur Kompensation wird die
Sendeleistung der Basisstation während der Übertragung des CSC erhöht (SPS,
Abs. 0027), wie es auch in den Figuren 2 und 3 dargestellt ist.


i)    Das mobile Endgerät empfängt die Festkanäle und berechnet nach
Merkmal 3.1 einen Korrelationswert für den zweiten Abschnitt des einen
Zeitschlitzes unter Verwendung des vorgegebenen Kurzcodes. Der vorgegebene
Kurzcode ist dafür nicht nur – in beliebiger Weise – auf den zweiten Abschnitt des

                                       - 29 -



Zeitschlitzes abgebildet (Merkmal 2.3), sondern auch dem mobilen Endgerät
bekannt, da es anderenfalls keinen Korrelationswert berechnen könnte.


Merkmal 3.1 ist nicht darauf beschränkt, dass ein nur einmal – in nicht veränderter
Form – im zweiten Abschnitt enthaltener vorgegebener Kurzcode empfangen und
anschließend mit dem im mobilen Endgerät vorliegenden CSC korreliert wird.
Vielmehr könnte bei einem mehrfach – auch in modifizierter Weise – in den zweiten
Abschnitt   eingefügten      vorgegebenen   Kurzcode    (vgl.    die   vorstehenden
Ausführungen zum Merkmal 2.3) der Korrelationswert nach Merkmal 3.1 das
Ergebnis einer im zweiten Abschnitt eines Zeitschlitzes mehrfach durchgeführten
Korrelation des CSC mit den empfangenen CSC und beliebiger weiterer
Berechnungen sein.


Auch wenn nach Merkmal 3.4 (Anspruch 8) das mobile Endgerät ein
signalangepasstes Filter (matched filter) umfasst, schließt dies nicht aus, dass
mehrere Korrelationen innerhalb des zweiten Abschnitts durchgeführt werden
und/oder dass weitere Schaltungen zur Berechnung des Korrelationswerts
verwendet werden.


Nach dem insofern nicht beschränkenden Ausführungsbeispiel (SPS, Fig. 9) liefert
das signalangepasste Filter im Moment der größten Übereinstimmung des
empfangenen Basisbandsignals mit dem CSC ein großes Ausgangssignal, das
mittels eines Spitzenwertdetektors erfasst und ausgewertet wird, um die
Zeitschlitzsynchronisation    auszuführen   (Merkmal   3.2).    Zur Erhöhung    der
Genauigkeit werden nach den Angaben in der Streitpatentschrift mehrere
aufeinanderfolgende Zeitschlitze ausgewertet (SPS, Abs. 0012).

                                       - 30 -



                     III. Zur Verteidigung nach Hauptantrag


In der erteilten Fassung kann die Beklagte ihr Patent nicht erfolgreich verteidigen,
weil der Gegenstand des Patentanspruchs 1 in der erteilten Fassung über den Inhalt
der europäischen Patentanmeldung in ihrer ursprünglich eingereichten Fassung
hinausgeht und sich im Übrigen auch als nicht patentfähig erweist, Art. II § 6 Abs. 1
Nr. 1 und 3 IntPatÜG, Art. 138 Abs. 1 Buchst. a) und c) i. V. m. Art. 52, 54 EPÜ.


1.      Der Gegenstand des Patentanspruchs 1 in der erteilten Fassung geht über
den Inhalt der Patentanmeldung in der ursprünglich eingereichten Fassung hinaus,
Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 Buchst. c) EPÜ. Im Folgenden wird
auf Fundstellen in der Offenlegungsschrift EP 0 957 594 A2 Bezug genommen.


a)      Der Fachmann entnimmt der Anmeldung, dass der vorgegebene Kurzcode
CSC im zweiten Abschnitt eines Zeitschlitzes nur einmal eingefügt ist, dass er
mithin nur ein fiktives Symbol spreizt, vgl. (Unterstreichungen hinzugefügt):
     - Fig. 3 – 6
     - Abs. 11: the long code masked symbol
     - Abs. 12: the mask symbol
     - Abs. 16: corresponding to one symbol
     - Abs. 23: In the masked symbol section, sections other than those of CSC and
        GISC are provided with no symbols
     - Abs. 28: the long code masked symbol


Ein – wir zur Auslegung erläutert – nach Merkmal 2.3 („Abbilden“) der erteilten
Fassung mögliches mehrfaches Einfügen des CSC in den zweiten Abschnitt kann
der Fachmann der Anmeldung nicht als zur Erfindung gehörend entnehmen. Zwar
ist im Zusammenhang mit dem in der Anmeldung genannten Stand der Technik
davon die Rede, dass der CSC und der GISC auf den zweiten Abschnitt abgebildet
sind (Abs. 4: In a long code masked symbol position […] a CSC […] is mapped. […]
a GISC […] is mapped.). Dabei ist jedoch zu beachten, dass im Stand der Technik

                                        - 31 -



die Spreizfaktoren des ersten Kurzcodes, des CSC und des GISC gleich groß sind
und der zweite Abschnitt ein Symbol lang ist, so dass ein „Abbilden“ des CSC auf
den zweiten Abschnitt in diesem Fall (gleiche Spreizfaktoren) zweifelsfrei mit dem
Spreizen eines fiktiven Symbols gleichzusetzen ist. Durch die streitpatentgemäße
Verkürzung des CSC ergibt sich jedoch die bereits erläuterte Mehrdeutigkeit des
„Abbildens“ des CSC auf den zweiten Abschnitt, die nicht ursprungsoffenbart ist.


Nach Auffassung der Beklagten entnimmt der Fachmann aufgrund der in Figur 5
gezeigten mehrfachen Übertragung des GISC auch eine mehrfache Übertragung
des CSC im zweiten Abschnitt als zur Erfindung gehörend. Dieser Auffassung kann
sich der Senat nicht anschließen. Denn die Bestimmung des GISC funktioniert
anders als die Zeitschlitzsynchronisation mittels des CSC, so dass der Fachmann
eine mehrfache Übertragung des CSC der Anmeldung nicht als zur Erfindung
gehörend entnimmt. Bei der Auswertung des oder der empfangenen GISC im
zweiten Schritt der dreistufigen Zellensuche liegt die streitpatentgemäße Zeitschlitzsynchronisation bereits vor. Damit führt eine mehrfache Übertragung des
(verkürzten) GISC im zweiten Abschnitt zu einer schnelleren und/oder sichereren
Ermittlung des gesuchten GISC, z. B. durch Mittelwertbildung.


Eine mehrfache Übertragung des CSC im zweiten Abschnitt würde hingegen die für
die Zeitschlitzsynchronisation erforderliche eindeutige Bestimmung der zeitlichen
Lage des CSC erschweren. Hinzu kommt, dass ein mobiles Endgerät regelmäßig
die Festkanäle von einer Vielzahl von asynchron sendenden CDMA-Basisstationen
empfängt. Würden diese jeweils mehrere CSC je Zeitschlitz aussenden, wäre es für
ein mobiles Endgerät ersichtlich schwerer, sich auf die Zeitschlitze einer
Basisstation zu synchronisieren.


Danach führt bereits das Merkmal 2.3 dazu, dass der Gegenstand des Streitpatents
in der erteilten Fassung über den Inhalt der ursprünglichen Anmeldeunterlagen
hinausgeht.

                                         - 32 -



b)      Gleiches gilt für das Merkmal 2.2, da der Fachmann den ursprünglichen
Anmeldeunterlagen kein beliebig geartetes „Abbilden“ des Langcodes und des
ersten Kurzcodes auf den ersten Abschnitt eines Zeitschlitzes entnehmen kann.
Vielmehr ist immer nur davon die Rede, dass die beiden Codes die zu
übertragenden Datensymbole spreizen, vgl.
     - Abs. 4: In a data symbol section102 […] a control signal transmitted to the
        mobile terminal is spread by a long code and short code 103
     - Anspruch 1: spreading factor of the long period code and a short period code
        (103) spreading said first section


c)      Der Gegenstand des Streitpatents geht auch insofern über den Inhalt der
ursprünglichen Anmeldung hinaus, dass
     - die Berechnung eines Korrelationswerts für den zweiten Abschnitt des einen
        Zeitschlitzes unter Verwendung des vorgegebenen Kurzcodes und
        Ausführen    einer   Zeitschlitzsynchronisation        unter     Verwendung     des
        berechneten Korrelationswerts (calculating a correlation value for said
        second section of said one slot by using said predetermined short period
        code, and conducting slot timing synchronization by using said calculated
        correlation value) (Merkmale 3.1 und 3.2)
etwas Allgemeineres ist als das ursprünglich offenbarte
     - Entspreizen des Steuersignals unter Verwendung des vorgegebenen
        Kurzcodes     und    Ausführen       einer   Zeitschlitzsynchronisation        unter
        Verwendung      eines    als   Ergebnis      des       Entspreizens     erhaltenen
        Korrelationswerts    (despreading     said   control    signal    by   using   said
        predetermined short period code, and conducting slot timing synchronization
        by using a correlation value obtained as a result of despreading)
        (ursprüngliche Ansprüche 1, 7, 9, 11; Abs. 0010, 0012).
Insbesondere fehlt in den Merkmalen 3.1 und 3.2 der erteilten Fassung, dass ein
Korrelationswert durch Entspreizen des Steuersignals unter Verwendung des CSC
gewonnen wird. Vielmehr wird nun ein Korrelationswert – in beliebiger Weise – unter
Verwendung des CSC berechnet. Eine auf ein Entspreizen des fiktiven Symbols

                                           - 33 -



verzichtende Berechnungsvorschrift kann der Fachmann der ursprünglichen
Anmeldung nicht als zur Erfindung gehörend entnehmen.


2.     Der Gegenstand des Patentanspruchs 1 in der erteilten Fassung ist nicht
patentfähig, Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) i. V. m.
Art. 52, 54 EPÜ. Er ist durch den Inhalt der älteren internationalen Patentanmeldung
PCT/JP98/01786 vorweggenommen, die aufgrund ihrer Nachveröffentlichung als
WO 98/47246 A1 Stand der Technik gemäß Art. 54 Abs. 3 i. V. m. Art. 153 Abs. 5
EPÜ    bildet.   Im     Folgenden   wird    auf     die   zugehörige   englischsprachige
Veröffentlichung EP 1 011 211 A1 (EP 211) Bezug genommen.


a)     Die EP 211 beschreibt ein mobiles DS-CDMA-Kommunikationssystem (Teil
von Merkmal 1), das im 2 GHz Frequenzband eine Informationsübertragungsrate
von bis zu 384 kbps ermöglicht. 16 Zeitschlitze mit einer Länge von jeweils 0,625 ms
bilden einen 10 ms langen Funkrahmen. Neben der Chiprate 4,096 Mcps sind auch
Systemvarianten mit 1,024, 8,192 und 16,384 Mcps möglich (S. 9, 10, Tab. 3; S. 48,
Z. 53 - 58; Fig. 4A).


Die   Basisstationen      übertragen   die     an     alle   Mobilstationen   gerichteten
Systeminformationen über logische Rundsendesteuerkanäle (broadcast control
channels), die auf zwei physikalische Fest-/Steuerkanäle (perch channels) nach
Merkmal 2 abgebildet werden (Fig. 2, 3, 4A, 8; S. 11, Z. 50). Auf den Festkanälen
werden Steuersignale mit einer festen Symbolrate von 16 ksps übertragen (S. 11,
Tab. 4). Der erste Festkanal überträgt kontinuierlich Symbole, der zweite
diskontinuierlich, wie aus der Figur 89 und der nachfolgend wiedergegebenen
Figur 4A ersichtlich:

                                       - 34 -




                                  EP 211, Fig. 4A
Bei der Symbolrate von 16 ksps sind in jedem 0,625 ms langen Zeitschlitz zehn,
jeweils   62,5 µs   lange,   Symbole   enthalten,   von   denen   das    letzte   als
langcodemaskiertes Symbol (long code mask symbol) bezeichnet ist. Denn dieses
fiktive Symbol wird nicht durch den basisstationsspezifischen Langcode, sondern
nur durch den vorgegebenen Kurzcode gespreizt, der im Kommunikationssystem
festgelegt und allen mobilen Endgeräten bekannt ist (Abs. 0077, 0126).


Da das Spreizen von Symbolen mittels eines Codes – wie zur Auslegung dargelegt
– ein Unterfall des „Abbildens“ des Codes ist, zeigt die EP 201 das Merkmal 2.3.


Die in dem ersten Abschnitt jedes Zeitschlitzes auf dem ersten Festkanal
gesendeten neun Symbole (Fig. 4A: 4 pilot symbols, 5 logical channel symbols)
werden durch einen basisstationsspezifischen Langcode und durch einen ersten
(kanalspezifischen) Kurzcode SC gespreizt, was – wie zur Auslegung dargelegt –
ein Unterfall des „Abbildens“ gemäß den Merkmalen 2.1 und 2.2 ist (Abs. 0121,
0123; Fig. 20, 22, 23).


Die Zeitschlitzsynchronisation (Rest von Merkmal 1; Merkmal 3.2) wird in einem
mobilen Endgerät (Merkmal 3) unter Verwendung eines Korrelationswerts
ausgeführt, der für den das langcodemaskierte Symbol enthaltenden zweiten
Abschnitt jedes Zeitschlitzes des ersten Festkanals durch Entspreizen des
empfangenen fiktiven Symbols mittels des vorgegebenen Kurzcodes erhalten wird
(Merkmal 3.1) (Abs. 0061, 0075, 0202, 0203).

                                          - 35 -



Da – wie zur Auslegung dargelegt – das “Entspreizen” des fiktiven Symbols ein
Unterfall des „Berechnens“ ist, sind auch die Merkmale 3.1 und 3.2 aus EP 201
bekannt.


Damit zeigt die EP 201, von der Beklagten auch nicht bestritten, die Merkmale 1 bis
3.2 des Gegenstands des Anspruchs 1 in der erteilten Fassung.


b)     Die EP 201 beschreibt die Funkschnittstelle des DS-CDMA-Kommunikationssystems in der Art einer technischen Spezifikation. Hinsichtlich der Chiprate
hat die 4,096 Mcps Variante zwar eine herausgehobene Stellung (S. 9, Tab. 3: Chip
rate 4.096 Mcps (expandable to 1.024/8.192 /16.384 Mcps); S. 26, Z. 36; S. 48, Z.
54), jedoch werden auch die anderen Varianten – wo erforderlich – behandelt
(S. 28, Z. 17; S. 30, Tab. 16; S. 31, Tab. 17, 18; S. 68, Z. 47).


Da auf den Festkanälen (perch channels) unabhängig von der Chiprate stets eine
Symbolrate von 16 ksps verwendet wird (S. 11, Tab. 4; S. 14, Tab. 5; Fig. 4A, 8,
64B), werden die neun Symbole im ersten Abschnitt jedes Zeitschlitzes des ersten
Festkanals mit einem ersten Kurzcode gespreizt, dessen Spreizfaktor sich aus der
nachfolgend wiedergegebenen Tabelle ergibt:




                  EP 201, S. 31, Tab. 18, mit Kolorierung durch den Senat

                                       - 36 -



Der Spreizfaktor des ersten Kurzcodes im ersten Abschnitt jedes Zeitschlitzes auf
dem ersten Festkanal beträgt somit 64, 256, 512 bzw. 1024 bei den Chipraten
1,024, 4,096, 8,192 bzw. 16,384 Mcps.


Der im zweiten Abschnitt jedes Zeitschlitzes auf dem ersten Festkanal zum
Spreizen des dortigen fiktiven Symbols (long code mask symbol) verwendete,
vorgegebene Kurzcode wird mittels eines Goldcode-Generators erzeugt, der 256
Chips erzeugt, bevor er wieder zurückgesetzt wird:




                               EP 201, S. 32, Z. 1 – 18




                               EP 201, S. 100, Fig. 21


Für die Chiprate 4,096 Mcps entsprechen die 256 Chips der zeitlichen Länge eines
Symbols (256 c / 4,096 Mc *1 s = 62,5 µs), wie dies auch in dem letzten
Aufzählungspunkt des vorstehend wiedergegebenen Absatzes 0122 zum Ausdruck
kommt (The period of the short code is one symbol interval (256 chips) of the perch
channel).

                                      - 37 -



Bei den Chipraten 8,092 bzw. 16,384 Mcps und der Symbolrate von 16 ksps
umfasst ein Symbol 512 bzw. 1024 Chips. Damit bietet der unverändert ein Symbol
bzw. 62,5 µs lange zweite Abschnitt jedes Zeitschlitzes des ersten Festkanals Platz
für 512 bzw. 1024 Chips. Da der für die Zeitschlitzsynchronisation verwendete
vorgegebene Gold-Code jedoch nur 256 Chips lang ist, nimmt er nur die Hälfte bzw.
ein Viertel der zur Verfügung stehenden Länge des zweiten Abschnitts ein. Damit
hat der Spreizfaktor des im zweiten Abschnitt verwendeten vorgegebenen
Kurzcodes zur Spreizung des fiktiven Symbols auch für die Chipraten 8,192 und
16,384 Mcps den Wert 256.


Damit ist, in Übereinstimmung mit Merkmal 4, für die Chipraten 8,192 Mcps bzw.
16,384 Mcps der Spreizfaktor (256) des vorgegebenen Kurzcodes (Gold-Code der
Länge 256 Chips) geringer als der Spreizfaktor (512 bzw. 1024) des ersten
Kurzcodes (orthogonaler Kurzcode der Länge 512 bzw. 1024).


Nach alledem ist der Gegenstand des Anspruchs 1 in der erteilten Fassung durch
die EP 201 neuheitsschädlich getroffen.


c)    Die weiteren Patentansprüche des Hauptantrags sind hinsichtlich ihre
Patentfähigkeit, weil die Beklagte in der mündlichen Verhandlung erklärt hat, dass
sie den Hauptantrag als geschlossenen Anspruchssatz versteht und das
Streitpatent in der Reihenfolge des Hauptantrags und der Hilfsanträge jeweils als
Ganzes verteidigt (vgl. BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR
2017, 57 – Datengenerator).


                      IV. Zur Verteidigung nach Hilfsantrag B.6‘


Demgegenüber kann die Beklagte ihr Patent hinsichtlich der angegriffenen
Patentansprüche 1 und 8 mit der Fassung nach Hilfsantrag B.6‘ mit Erfolg
beschränkt verteidigen, weil dieser Fassung der Patentansprüche 1 und 8 keine

                                       - 38 -



Nichtigkeitsgründe entgegenstehen, Art. II § 6 Abs. 1 Nr. 1 und 3 IntPatÜG, Art. 138
Abs. 1 Buchst. a) und c) i. V. m. Art. 52, 54, 56 EPÜ.


1.       Hilfsantrag B.6‘, gestellt in der mündlichen Verhandlung am 19. Februar
2020, war trotz Rüge der Klägerinnen nicht als verspätet zurückzuweisen, § 83
Abs. 4 PatG. Dementsprechendes gilt für als verspätet gerügte, erstmals in der
mündlichen Verhandlung am 19. Februar 2020 vorgebrachte Behauptung, der
Gegenstand des Patentanspruchs 1 in erteilter Fassung sei gegenüber dem im
ARIB-Standard (ZP14 und ZP14a) dargestellten TDD-Modus bzw. gegenüber dem
ARIB TDD-Modus in Kombination mit der Druckschrift Higuchi_IEEE (ZP8) nicht
patentfähig.


§ 83 PatG mit den in das Nichtigkeitsverfahren eingeführten Präklusionsregeln sieht
grundsätzlich die Möglichkeit vor, verspätetes Vorbringen zurückzuweisen.
Voraussetzungen hierfür sind aber nach § 83 Abs. 4 PatG, dass das Vorbringen
unter Versäumung der nach § 83 Abs. 2 PatG gesetzten Frist erfolgt, die betroffene
Partei die Verspätung nicht genügend entschuldigt sowie die Berücksichtigung des
neuen Vortrags eine Vertagung des Termins zur mündlichen Verhandlung erfordert
hätte.


Nach Wiedereröffnung der mündlichen Verhandlung und Fortsetzung am
28. Oktober 2020 ist es weder durch Hilfsantrag B.6‘ noch durch die Ausführungen
in der mündlichen Verhandlung am 19. Februar 2020 zur fehlenden Patentfähigkeit
unter Bezugnahme auf den ARIB-Standard zu einer (weiteren) Verzögerung
gekommen und die Klägerinnen haben zudem weiter rügelos zur Sache verhandelt.


2.       Die Patentansprüche 1 und 8 nach Hilfsantrag B.6‘ lassen sich wie folgt
gliedern (Änderungen gegenüber der erteilten Fassung mittels Durch- und
Unterstreichungen gekennzeichnet):

                                         - 39 -



Anspruch 1:
    1         Zeitschlitzsynchronisationsverfahren für ein mobiles CDMA-Kommunikationssystem, umfassend die Schritte:
                  A slot timing synchronization method in a code
                  division   multiple    access   mobile   communication
                  system, said slot timing synchronizing method
                  comprising the steps of:
    2         Senden eines SteuersignaIs von einer Basisstation über
              Festkanäle (106, 107), die so beschaffen sind, dass
                  transmitting from a base station a control signal via
                  perch channels (106, 107), said perch channels being
                  formed such that
    2.1spr    ein der Basisstation zugeordneter Langcode und
                  a long period code assigned to said base station and
    2.2spr    ein erster Kurzcode auf einen ersten Abschnitt (102) eines
              Zeitschlitzes des Festkanals abgebildet sind spreizen und
                  a first short period code is mapped in spread a first
                  section (102) of one slot of said perch channel and
    2.3spr    ein vorgegebener Kurzcode auf einen zweiten Abschnitt (131)
              des einen Zeitschlitzes abgebildet ist spreizt, und
                  a predetermined short period code is mapped in
                  spreads a second section (131) of said one slot; and
    3         in einem mobilen Endgerät,
                  in a mobile terminal
    3.1dspr   Berechnen eines Korrelationswerts für den Entspreizen des
              zweiten Abschnitts des einen Zeitschlitzes unter Verwendung
              des vorgegebenen Kurzcodes und
                  calculating a correlation value for despreading said
                  second section of said one slot by using said
                  predetermined short period code, and

                                       - 40 -



    3.2dspr   Ausführen einer Zeitschlitzsynchronisation unter Verwendung
              des berechneten eines als Ergebnis des Entspreizens
              erhaltenen Korrelationswerts
                  conducting slot timing synchronization by using said
                  calculated a correlation value obtained as a result of
                  despreading,
    4         dadurch     gekennzeichnet,       dass     ein    Spreizfaktor   des
              vorgegebenen Kurzcodes auf einen niedrigeren Wert als ein
              Spreizfaktor des ersten Kurzcodes des ersten Abschnitts
              eingestellt ist
                  characterized in that a spreading factor of said
                  predetermined short period code is set to a value
                  lower than a spreading factor of said first short period
                  code of said first section
    2.3.1     und geringer als 256 ist.
                  and is less then 256.


Anspruch 8:
    3         Mobiles       Endgerät      für      ein         mobiles     CDMA-Kommunikationssystem, bei dem
                  A mobile terminal used in a code division multiple
                  access mobile communication system in which
    2         eine Basisstation ein Steuersignal über Festkanäle(106, 107)
              überträgt, die so beschaffen sind, dass
                  a base station transmits a control signal via perch
                  channels (106, 107) formed such that
    2.1spr    ein der Basisstation zugeordneter Langcode und
                  a long period code assigned to said base station and
    2.2spr    ein erster Kurzcode auf einen ersten Abschnitt (102) eines
              Zeitschlitzes des Festkanals abgebildet sind spreizen und

                                  - 41 -



              a first short period code is mapped in spread a first
              section (102) of one slot of said perch channel and
2.3spr   ein vorgegebener Kurzcode auf einen zweiten Abschnitt (131)
         des einen Zeitschlitzes abgebildet ist spreizt, und
              a predetermined short period code is mapped in
              spreads a second section (131) of said one slot; and
3        wobei das mobile Endgerät umfasst,
              said mobile terminal comprising:
3.3      eine RF-Einheit (801) zum Umwandeln eines von einer Antenne
         empfangenen Signals, das eine Trägerfrequenz hat, in ein
         Basisbandsignal und
              an RF unit (801) for converting a received signal of a
              carrier frequency received from an antenna to a
              baseband signal; and
3.4      ein signalangepasstes Filter (901) zum Empfangen des
         Basisbandsignals und
              a matched filter (901) for receiving input of said
              baseband signal and
3.1_3.2dspr    zum    Berechnen      eines     Korrelationswerts   für    das
         Entspreizen des Basisbandsignals unter Verwendung des
         zweiten     Kurzcodes    (CSC)       und   zum   Ausgeben       eines
         Korrelationswertes            zur          Herstellung          einer
         Zeitschlitzsynchronisation,
              calculating a correlation value for despreading said
              baseband signal by using said second short period
              code (CSC), and outputting a correlation value to
              establish slot timing synchronization,
4        dadurch     gekennzeichnet,         dass   ein   Spreizfaktor    des
         vorgegebenen Kurzcodes einen niedrigeren Wert als ein
         Spreizfaktor des ersten Kurzcodes des ersten Abschnitts hat.

                                            - 42 -



                    characterized in that a spreading factor of said
                    predetermined short period code has a lower value
                    than a spreading factor of said first short period code
                    of said first section
     2.3.1      und geringer als 256 ist.
                    and is less then 256.


3.    Wie zum Hauptantrag erläutert, versteht der Fachmann unter „Spreizen“
gemäß Merkmal 2.2spr die Multiplikation der zu übertragenden Symbole mit dem
ersten Kurzcode, wobei jedes Symbol mit einem Vektor multipliziert wird, dessen
Länge (= Anzahl seiner Elemente) gleich dem Spreizfaktor des ersten Kurzcodes
ist. Werden z. B. bei einer Symbolrate von 16 ksps zehn Symbole mit einem ersten
Kurzcode mit Spreizfaktor 256 gespreizt, so liegt danach ein Signal mit einer Länge
von 2560 Chips und einer Chiprate von 4,096 Mcps vor.


Das „Spreizen“ nach Merkmal 2.1spr betrifft die Multiplikation der bereits mit dem
ersten Kurzcode gespreizten Symbole mit einem Langcode, ohne dabei den
Spreizfaktor zu ändern. Bei den beispielhaft genannten zehn Symbolen, die durch
den ersten Kurzcode auf eine Länge von 2560 Chips gespreizt werden, führt die
anschließende Multiplikation mit einem z. B. 2560 Chips langen Langcode dazu,
dass jedes der zehn 256 Chips langen Symbole mit einem anderen, jeweils 256
Chips langen Abschnitt des Langcodes multipliziert wird. Das resultierende Signal
weist bei einer unveränderten Chiprate von 4,096 Mcps ein verändertes Frequenzspektrum auf.


Das im Merkmal 2.3spr genannte „Spreizen“ des zweiten Abschnitts eines
Zeitschlitzes durch den vorgegebenen Kurzcode versteht der Fachmann – wie zum
Hauptantrag ausgeführt – als einmaliges Einfügen dieses Kurzcodes in den zweiten
Abschnitt. Dabei wird ein „fiktives“, weil keine Information tragendes Symbol durch
den vorgegebenen Kurzcode „gespreizt“.

                                           - 43 -



Die Merkmale 3.1dspr und 3.1_3.2dspr versteht der Fachmann so, dass dieses
„fiktive“ Symbol im mobilen Endgerät „entspreizt“ wird. Wie in Figur 9 der
Streitpatentschrift dargestellt, wird das empfangene Basisbandsignal chipweise in
ein signalangepasstes Filter (matched filter, Merkmal 3.4) eingegeben und dort mit
dem im mobilen Endgerät vorliegenden Kurzcode CSC verglichen. Bei vollständiger
oder zumindest nahezu vollständiger Übereinstimmung gibt das Filter einen großen
Korrelationswert      aus    (Merkmale      3.2dspr,     3.1_3.2dspr),   der   mit   einer
Spitzenwerterfassungsschaltung (peak detector 904) erfasst wird. Dessen
Ausgangssignal wird auf eine Integriererschaltung (accumulator 903) rückgeführt,
um den Vorgang für mehrere aufeinanderfolge Zeitschlitze durchzuführen und damit
die Zeitschlitzsynchronisation genauer bestimmen zu können (Merkmal 3.2dspr).


Nach Merkmal 2.3.1 ist der Spreizfaktor des vorgegebenen Kurzcodes geringer als
256, d. h. er hat eine Länge von weniger als 256 Chips. Die insofern nicht
einschränkenden Ausführungsbeispiele des Streitpatents zeigen Werte von 64 bzw.
16 (Fig. 3, 4).


4.       Die unabhängigen Patentansprüche 1 und 8 nach Hilfsantrag B.6‘ sind
zulässig, insbesondere sind ihre Gegenstände in der ursprünglichen Anmeldung
(EP 0 957 594 A2) wie folgt offenbart:


     1            Zeitschlitzsynchronisationsverfahren für ein mobiles CDMA-Kommunikationssystem, umfassend die Schritte:
                     A. 1: A slot timing synchronization method in a code
                     division   multiple   access      mobile   communication
                     system, said slot timing synchronizing method
                     comprising the steps of:
     2            Senden eines SteuersignaIs von einer Basisstation über
                  Festkanäle (106, 107), die so beschaffen sind, dass
                     A. 1: transmitting from a base station a control signal
                     via perch channels (106, 107)

                                   - 44 -



2.1spr        ein der Basisstation zugeordneter Langcode und
2.2spr    ein erster Kurzcode einen ersten Abschnitt (102) eines
          Zeitschlitzes des Festkanals spreizen und
              A. 1: the long period code and a short period code
              (103) spreading said first section
2.3spr    ein vorgegebener Kurzcode einen zweiten Abschnitt (131) des
          einen Zeitschlitzes spreizt, und
              A. 1: a second section (131) of said one slot being
              spread by a predetermined short period signal
3         in einem mobilen Endgerät,
              A. 1: in a mobile terminal
3.1dspr   Entspreizen des zweiten Abschnitts des einen Zeitschlitzes
          unter Verwendung des vorgegebenen Kurzcodes und
3.2dspr   Ausführen einer Zeitschlitzsynchronisation unter Verwendung
          eines     als     Ergebnis    des        Entspreizens   erhaltenen
          Korrelationswerts
              A. 1: despreading said control signal by using said
              predetermined short period code, and conducting slot
              timing synchronization by using a correlation value
              obtained as a result of despreading; dabei liest der
              Fachmann mit, dass (auch) der zweite Abschnitt des
              einen Zeitschlitzes entspreizt wird
4         dadurch     gekennzeichnet,       dass     ein   Spreizfaktor   des
          vorgegebenen Kurzcodes auf einen niedrigeren Wert als ein
          Spreizfaktor des ersten Kurzcodes des ersten Abschnitts
          eingestellt ist
              A. 1: a spreading factor of said predetermined short
              period code being set to a value lower than a
              spreading factor of the long period code and a short
              period code (103) spreading said first section; wobei
              der Fachmann in der ursprünglichen Anmeldung

                                   - 45 -



              mitliest, dass der Spreizfaktor des Langcodes und des
              ersten Kurzcodes gleich dem Spreizfaktor des ersten
              Kurzcodes    ist,   weil     der    Langcode   fachüblich
              chipweise mit dem bereits durch den ersten Kurzcode
              gespreizten Signal multipliziert wird und somit durch
              den Langcode der Spreizfaktor nicht verändert wird;
              vgl. auch die Ausführungen zur Auslegung der
              Ansprüche)
2.3.1         und geringer als 256 ist.
                 Abs. 0023, 0025, 0026, 0027


3        Mobiles       Endgerät          für     ein    mobiles       CDMA-Kommunikationssystem, bei dem
              A. 9, A. 11: A mobile terminal used in a code division
              multiple access mobile communication system, said
              mobile terminal comprising:
3.3      eine RF-Einheit (801) zum Umwandeln eines von einer Antenne
         empfangenen Signals, das eine Trägerfrequenz hat, in ein
         Basisbandsignal und
              A. 11: an RF unit (801) for converting a received signal
              of a carrier frequency received from an antenna to a
              received signal of a baseband
3.4      ein signalangepasstes Filter (901) zum Empfangen des
         Basisbandsignals und
              A. 11: a matched filter (901) for receiving input of said
              received signal of the baseband and
3.1_3.2dspr    zum      Entspreizen        des     Basisbandsignals       unter
         Verwendung des zweiten Kurzcodes (CSC) und zum Ausgeben
         eines       Korrelationswertes          zur   Herstellung        einer
         Zeitschlitzsynchronisation,

                                        - 46 -



                   A. 11:   despreading     said   received    signal,   and
                   outputting a correlation value”; A. 9: said matched filter
                   despreads said control signal by using said first short
                   period code (CSC); A. 1: conducting slot timing
                   synchronization by using a correlation value obtained
                   as a result of despreading


Da – wie bereits ausgeführt – die Merkmale 2.1spr, 2.2spr, 2.3spr, 3.1dspr, 3.2dspr und
3.1_3.2dspr die entsprechenden Merkmale der Ansprüche 1 und 8 in der erteilten
Fassung konkretisieren, ist der Schutzbereich des Streitpatents in der Fassung
nach Hilfsantrag B.6‘ kleiner als derjenige der erteilten Fassung.


Das Merkmal 2.3.1 schränkt ebenfalls den Schutzbereich des Streitpatents ein.


5.     Die Gegenstände der unabhängigen Patentansprüche 1 und 8 in der
Anspruchsfassung nach Hilfsantrag B.6‘ gelten als neu und als auf einer
erfinderischen Tätigkeit beruhend.


a)     Die Gegenstände der unabhängigen Patentansprüche 1 und 8 in der
Anspruchsfassung nach Hilfsantrag B.6‘ gelten als neu.


aa)    Der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ ist neu gegenüber
der EP 201.


Wie zum Hauptantrag dargelegt, ist der Gegenstand des Anspruchs 1 erteilter
Fassung aus der EP 201 bekannt. Dort wurde bereits erläutert, dass die EP 201
auch die konkretisierten Merkmale 2.1spr, 2.2spr, 2.3spr, 3.1dspr und 3.2dspr zeigt, so
dass die Merkmale 1 bis 4 des Gegenstands des Anspruchs 1 in der Fassung nach
Hilfsantrag B.6‘ aus der EP 201 bekannt sind.

                                       - 47 -



Wie ebenfalls zum Hauptantrag dargelegt, offenbart die EP 201 für die Chipraten
4,096, 8,192 und 16,384 Mcps jeweils einen vorgegebenen Kurzcode mit der Länge
256 Chips, d. h. sein Spreizfaktor beträgt jeweils 256. Damit zeigt die EP 201 für
diese drei Chipraten das Merkmal 2.3.1 (Spreizfaktor vorgegebener Kurzcode
kleiner als 256) nicht.


Bei der niedrigsten Chiprate von 1,024 Mcps wird der vom Goldcode-Generator
nach Figur 21 der EP 201 erzeugte vorgegebene Kurzcode nach jeweils 64 Chips
gestoppt, weil der zweite Abschnitt, der eine Länge von einem Symbol bzw. 62,5 µs
hat, bei dieser Chiprate nur 64 Chips aufnehmen kann. Damit ist zwar das Merkmal
2.3.1 erfüllt, nicht jedoch das Merkmal 4 (Spreizfaktor vorgegebener Kurzcodes
kleiner als Spreizfaktor erster Kurzcode), denn der Spreizfaktor des ersten
Kurzcodes auf den 16 ksps Festkanälen beträgt bei der Chiprate von 1,024 Mcps
ebenfalls 64 (EP 201, Tab. 18).


Danach ist der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ neu ggü. allen
Varianten der EP 201. Gleiches gilt für den Gegenstand des Anspruchs 8 nach
Hilfsantrag B.6‘, der sich in den Merkmalen 4 und 2.3.1 nicht vom Anspruch 1
unterscheidet.


bb)   Der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ ist auch neu
gegenüber dem ARIB-Standard. Entgegen der Ansicht der Klägerinnen belegt die
mehrfache Erwähnung (inklusive eines Inhaltsverzeichnisses) des japanischen
ARIB-Standards in den Versionen 0, 0-3 und 0-4.0 in einem vorveröffentlichten
Bericht einer europäischen ETSI-Arbeitsgruppe (Anlage ZP14D, S. 115, 122, 130 –
135, 147, 153) nicht, dass der ARIB-Standard vor dem Prioritätszeitpunkt des
Streitpatents der Fachöffentlichkeit zugänglich war.


Nach Ansicht der Klägerinnen war ein Vorschlag der japanischen Organisation
ARIB (Association of Radio Industries and Businesses) für die Funkschnittstelle
eines Mobilfunksystems der dritten Generation vor dem Prioritätstag des

                                      - 48 -



Streitpatents der Fachöffentlichkeit zugänglich. Hierzu haben die Klägerinnen u. a.
die Anlagen ZP14, ZP14g und ZP14h vorgelegt.


Die Anlage ZP14 besteht aus den Abschnitten „(Draft) Volume 1 Requirements and
Objectives for a 3G Mobile Services and System Ver.0 ISSUED“ und “Volume 3
Specification of the Air Interface for the 3G Mobile System”. Ein Hinweis auf den
Zeitpunkt einer Veröffentlichung ist in dem Dokument ZP14 nicht enthalten.


Die Anlagen ZP14g und ZP14h umfassen ebenfalls jeweils einen Teil “Volume 3
Specification of the Air Interface for the 3G Mobile System”, dem ein Deckblatt mit
den Angaben „Version: 0-1.0 […] Date: 25 July 1997“ bzw. „Version: 0-4.0 […] Date:
December 18, 1997“ vorangestellt ist. Die Klägerinnen haben die Anlagen ZP14g
und ZP14h am 30. März 2020 von der Website der Organisation … abgerufen
(ZP14f, ZP14i).


Jedenfalls stimmt das „Volume 3“ der ZP14h inhaltlich mit dem „Volume 3“ der ZP14
überein. Im Folgenden wird daher die Anlage ZP14h, also ARIB Version 0-4.1, als
„ARIB-Standard“ bezeichnet.


Gemäß der Anlage ZP14m gehört es zu den Aufgaben der …, nationale und
internationale technische Standards zu entwickeln und zu veröffentlichen (S. 2,
Art. 4 Nr. 1 und 2).


Die bloße Nennung des Titels und eines Teils des Inhaltsverzeichnisses des ARIB-Standards in dem ETSI-Dokument (ZP14D) lässt allerdings nicht den Schluss zu,
dass der ARIB-Standard in vollem Umfang der Fachöffentlichkeit, z. B. den
Mitgliedern der entsprechenden ETSI-Arbeitsgruppen, zugänglich war.


Der Senat ist nicht davon überzeugt, dass die im März 2020 von der Website der
Organisation … abrufbaren ARIB-Standards (ZP14g = Ver. 0-1.0, ZP14h = Ver. 0-

                                        - 49 -



4.0) auch schon vor dem Prioritätszeitpunkt des Streitpatents dort oder unter einer
anderen Internet-Adresse öffentlich zugänglich waren.


(1)    Auf die Frage der Vorveröffentlichung des ARIB-Standards kommt es letztlich
jedoch nicht an. Denn auch die Veröffentlichung unterstellt, steht der von den
Klägerinnen in das Verfahren eingeführte ARIB-Standard der Patentfähigkeit der
Gegenstände der Patentansprüche 1 und 8 in der Fassung des Hilfsantrags B.6‘
nicht entgegen.


Daher war auch die von den Klägerinnen angebotene Einvernahme der Zeugen zu
der Frage der Vorveröffentlichung entbehrlich. Dabei kann dahinstehen, ob die
Zeugen tatsächlich zu Umständen als Zeugen angeboten worden sind, die in ihre
Wahrnehmung gestellt sind.


Auch    dem       Beweisangebot   der    Klägerinnen     durch   Einholung   eines
Sachverständigengutachtens war nicht nachzugehen. Mit der Antwort auf die Frage,
ob der Fachmann (keine) Probleme damit gehabt hätte, die allgemeine Anweisung
in Abschnitt 3.3.2.1.3 des ARIB-Standards auf die Chipraten 4,096, 8,192 und
16,384 zu beziehen, soll letztlich die Frage nach dem Verständnis des ARIB-Standard beantwortet werden. Dies ist allerdings einem Sachverständigenbeweis
über Tatsachen nicht zugänglich; die Frage der Auslegung ist vielmehr
Schlussfolgerung aufgrund von offenbarten Tatsachen, also eine Rechtsfrage, die
dem Sachverständigenbeweis nicht zugänglich ist.


(2)    Der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ ist neu gegenüber
dem als vorveröffentlicht unterstellten ARIB-Standard.


α)     Der ARIB-Standard (ZP14h) stimmt inhaltlich teilweise mit der zum
Hauptantrag genannten EP 201 (ZP10a) überein. Auch aus dem ARIB-Standard ist
ein     Zeitschlitzsynchronisationsverfahren     für     ein     mobiles     CDMA-Kommunikationssystem nach den Merkmalen 1, 3, 3.1dspr und 3.2dspr bekannt

                                        - 50 -



(S. 174: Title: […] 3G Mobile system; S. 183, Kap. 3.1, Z. 1: W-CDMA; S. 261,
Kap. 3.2.7.1 (b): downlink chip synchronization […] based on the perch channel
synchronization information; S. 277, Kap. 3.2.7.9 (1): mobile station discovers
symbol timing as the time Long Code mask symbol be scanning first perch channel
with unique Short Code in system).


Jede Basisstation des CDMA-Systems sendet über logische Rundsendekanäle
(BCCH1/2), die auf physikalische Festkanäle (perch channels) abgebildet werden,
Steuersignale (system control information) gemäß Merkmal 2 an die mobilen
Endgeräte ihrer Funkzelle (S. 185, Fig. 3.2-1; S. 186, Kap. 3.2.1.1.1.1.1; S. 190,
Fig. 3.2-3; S. 190, Kap. 3.2.1.3.1; S. 294, Kap. 3.3.1.3 u. 3.3.1.3.1).


Der im Downlink verwendete Langcode ist einer Basisstation, insbesondere ihrem
Sektor, zugeordnet und spreizt (verwürfelt) alle physikalischen Kanäle (außer das
im zweiten Abschnitt eines Zeitschlitzes der Festkanäle gesendete long code
masked symbol), also auch den ersten Abschnitt der Zeitschlitze auf den
Festkanälen gemäß Merkmal 2.1spr (S. 184, Tab. 3.1-1: Spreading […] DL […] LC
for sector ID; S. 245, Kap. 3.2.4.2.2: The spreading operation consists of two
operations; Short Code spreading (channelisation) and Long Code spreading
(scrambling); S. 245, Kap. 3.2.4.2.2.1 Downlink Long Code […] Gold Code; S. 300,
Kap. 3.3.4.2.2.1 Downlink Long Code This is the same as FDD mode).


Die Kanalisierungscodes sind als orthogonale geschichtete Codes (layered
orthogonal code) ausgebildete erste Kurzcodes, die alle physikalischen Kanäle
(außer das im zweiten Abschnitt eines Zeitschlitzes der Festkanäle gesendete long
code masked symbol), also auch den ersten Abschnitt eines Zeitschlitzes des
Festkanals gemäß Merkmal 2.2spr, spreizen (S. 248, Kap. 3.2.4.2.2.3.1: Short Code
for Symbols other than Long Code Masked Symbols […] For symbols of all physical
channels other than perch channels, and the symbols other than the long code
masked symbols of perch channels, the layered orthogonal code sequence […] shall
be used; S. 300, Kap. 3.3.4.2.2.3.1: same as FDD mode).

                                              - 51 -



Den zweiten Abschnitt (long code masked symbol) der Zeitschlitze spreizt in
Übereinstimmung mit Merkmal 2.3spr ein vorgegebener Kurzcode (orthogonal Gold
code) (S. 197, Fig. 3.2.2-1, S. 198, Kap. 3.2.2.1.3: Long Code Masked Symbols are
spread only with short codes, and the long codes shall not be used […] orthogonal
Gold codes of code length 256; S. 249, Kap. 3.2.4.2.2.3.2, insbesondere Fig. 3.2.4-
4; S. 295, Fig. 3.3.-2; S. 295, Kap. 3.3.2.1.3 same as FDD mode; S. 300,
Kap. 3.3.4.2.2.3.2: same as FDD mode).


β)       Im Unterschied zur EP 201 beschreibt ARIB nicht nur einen FDD- (frequency
division duplex), sondern auch einen TDD- (time division duplex) Modus des CDMA-Kommunikationssystems. Die Funkschnittstelle unterscheidet sich für die beiden
Modi nur in einigen wenigen Parametern (S. 183, Kap. 3.1, Abs. 1, 2):




     ARIB-Standard (ARIB 0.4-0, ZP14h) S. 183, 184, Tab. 3.1-1 mit Kolorierung durch den Senat


Auf den von einer Basisstation ausgesendeten Festkanälen (perch channels)
beträgt die Symbolrate im TDD-Modus, unabhängig von der Chiprate, 32 ksps.
Damit ist in jedem 0,625 ms langen Zeitschlitz Platz für 20 Symbole, die jeweils
31,25 µs lang sind (S. 293, Tab. 3.3.-1; S. 295, Fig. 3.3.-2), mithin halb so lang wie
im FDD-Modus:

                                          - 52 -




             ARIB-Standard, S. 295, Fig. 3.3.-2 mit Kolorierung durch den Senat


Im TDD-Modus umfasst somit ein Symbol auf dem 32 ksps Festkanal bei den
Chipraten 1,024, 4,096, 8,192 bzw. 16,386 Mcps jeweils 32, 128, 256 bzw. 512
Chips (Anzahl der Chips je Symbol = Chiprate * Symbollänge), d. h. der Spreizfaktor
des ersten Kurzcodes hat den Wert 32, 128, 256 bzw. 512:




            ARIB-Standard, S. 249, Tab. 3.2.4-3 mit Kolorierung durch den Senat


γ)    Der den zweiten Abschnitt spreizende vorgegebene Kurzcode ist im FDD-Modus ein orthogonaler Gold-Code mit der Länge 256 (S. 198, Kap. 3.2.2.1.3: the
short codes that spread the Long Code Masked Symbols shall be orthogonal Gold
codes of code length 256. Details are described in Chapter 3.2.4.2.2.3.2). In dem
Kapitel 3.2.4.2.2.3.2 sind die den Gold-Code erzeugenden Generator-Polynome mit
einer möglichen Implementierung angegeben:

                                       - 53 -




                      ARIB-Standard, S. 249, Kap. 3.2.4.2.2.3.2




                         ARIB-Standard, S. 249, Fig. 3.2.4-4


Für den FDD-Modus (Symbolrate 16 ksps auf dem Festkanal) und die „Standard-Chiprate“ von 4,096 Mcps weisen sowohl der ersten Kurzcode als auch der
vorgegebene Kurzcode eine Länge und damit einen Spreizfaktor von 256 auf. Damit
ist in diesem Fall weder das Merkmal 4 noch das Merkmal 2.3.1 des Gegenstands
des Anspruchs 1 in der Fassung des Hilfsantrags B.6‘ aus ARIB bekannt.


Dagegen ergeben sich für die größeren Chipraten von 8,192 bzw. 16,384 Mcps im
FDD-Modus – wie bereits zum Hauptantrag zu der Druckschrift EP 201 ausgeführt
– Spreizfaktoren für den ersten Kurzcode von 512 bzw. 1024, während der

                                         - 54 -



Spreizfaktor des vorgegebenen Kurzcodes nach wie vor 256 beträgt. Damit zeigen
diese Varianten zwar jeweils das Merkmal 4, nicht jedoch das Merkmal 2.3.1.


Für den TDD-Modus (Symbolrate 32 ksps statt 16 ksps im FDD-Modus) wird in den
korrespondierenden Kapiteln 3.3.2.1.3 bzw. (die Seiten 295 und 296 übergreifender
Absatz) bzw. 3.3.4.2.2.3.2       (S. 300) des ARIB-Standards folgendes         zum
vorgegebenen Kurzcode und seiner Erzeugung ausgeführt:




                       ARIB-Standard, S. 295, 296, Kap. 3.3.2.1.3




                        ARIB-Standard, S. 300, Kap. 3.3.4.2.2.3.2


Somit soll der vorgegebene Kurzcode im TDD-Modus eine Länge von 128 Chips
haben (code length 128) und mit dem vorgegebenen Kurzcode im FDD-Modus
übereinstimmen (the same as FDD mode), d. h. durch einen Generator erzeugt
werden, der einen 256 Chips langen Gold-Code ausgibt.


Bei der „Standard-Chiprate“ von 4,096 Mcps umfasst ein 32,5 µs langes Symbol
128 Chips. Damit ist auch in dem zweiten Abschnitt eines Zeitschlitzes des
Festkanals, dem long code masked symbol (S. 295, Fig. 3.3.-2) Platz für nur
128 Chips. Der Fachmann versteht daher die vorstehend zitierten Angaben zum
vorgegebenen Kurzcode im TDD-Modus so, dass bei einer Chiprate von
4,096 Mcps zwar der gleiche Gold-Code-Generator wie im FDD-Modus verwendet
wird, jedoch dessen Ausgangssignal entweder nach 128 Chips abgeschnitten oder
– wie die Klägerinnen erläutert haben – das MSB (most significant bit) seines ersten

                                       - 55 -



Schieberegisters (S. 249, Fig. 3.2.4-4) geeignet initialisiert wird, um nur 128 Chips
zu erzeugen. Da im TDD-Modus der Spreizfaktor des ersten Kurzcodes für die
Chiprate von 4,096 Mcps ebenfalls 128 beträgt (S. 249, Tab. 3.2.4-3), ist für diesen
Fall zwar das Merkmal 2.3.1, nicht jedoch das Merkmal 4 erfüllt.


Für die höheren Chipraten von 8,192 bzw. 16,384 Mcps betragen die Spreizfaktoren
des ersten Kurzcodes im TDD-Modus 256 bzw. 512 (S. 249, Tab. 3.2.4-3). Nach
Ansicht   der   Klägerinnen   entnimmt    der   Fachmann     dem    ARIB-Standard,
insbesondere Seiten 295, 296, Kap. 3.3.2.1.3, dass im TDD-Modus der Spreizfaktor
des vorgegebenen Kurzcodes für die Chipraten 4,096, 8,192 und 16,384 Mcps stets
128 beträgt. Der Fachmann würde auch bei den beiden höheren Chipraten, bei
denen ein Symbol 256 bzw. 512 Chips lang ist, den Gold-Code-Generator so
abschneiden oder so initialisieren, dass er nur 128 Chips erzeugt. Damit wären die
Merkmale 4 und 2.3.1 für die beiden höchsten Spreizfaktoren erfüllt.


Diese Sichtweise überzeugt nicht. Der vorgegebene Kurzcode umfasst im TDD-Modus bei der Chiprate von 4,096 Mcps nur deswegen nur 128 Chips, weil wegen
der im Vergleich zum FDD-Modus halb so langen Symbole auf den Festkanälen je
Symbol nicht mehr als 128 Chipplätze zur Verfügung stehen. Die Aussage zum
TDD-Modus „the short codes for long code masked symbols shall use orthogonal
Gold code of code length 128“ (S. 295) steht somit nicht im Widerspruch zu der
Angabe „The cycle is 1 symbol (256 chip) of the perch channel“ (S. 249) im FDD-Modus.


Vor dem Prioritätszeitpunkt des Streitpatents war es üblich, einen vorgegebenen
Kurzcode mit einer Länge von 256 Chips zu verwenden, um eine sichere
Zeitschlitzsynchronisation zu erzielen (TR 146, S. 38, Abs. 1), auch wenn dies bei
einem signalangepassten Filter mit nur 64 Abgriffen Nachteile mit sich bringt, die
(erst) das Streitpatent mit einer Verkürzung des vorgegebenen Kurzcodes auf 64
oder 16 Chips löst. Daher verschlechtert der (bei der Chiprate von 4,096 Mcps) nur
128 Chips lange vorgegebene Kurzcode die Zeitschlitzsynchronisation im TDD-

                                        - 56 -



Modus. Darüber hinaus sendet eine Basisstation auf den Festkanälen im TDD-Modus nur halb so oft Zeitschlitze wie im FDD-Modus (S. 295, Fig. 3.3-1), womit
sich die Synchronisation gegenüber dem FDD-Modus noch weiter verschlechtert.


Vor diesem Hintergrund entnimmt der Fachmann dem Abschnitt 3.3.4.2.2.3.2 des
ARIB-Standards, dass im TDD-Modus – sofern in Abhängigkeit der gewählten
Chiprate im long code masked symbol ausreichend Platz ist – der Gold-Code-Generator des FDD-Modus zu verwenden ist, der einen 256 Chips langen
Kurzcode ausgibt. Damit beträgt der Spreizfaktor des vorgegebenen Kurzcodes
für die beiden höheren Chipraten von 8,192 bzw. 16,384 Mcps jeweils 256, so dass
das Merkmal 2.3.1 (Spreizfaktor kleiner 256) für diese Chipraten nicht erfüllt ist.


Der ARIB-Standard ist, auch wenn es sich um eine frühe, noch nicht endgültig
verabschiedete Version handelt, jedenfalls in seinen wichtigsten Aspekten weder
unvollständig noch widersprüchlich. Daher wäre, falls im TDD-Modus für jede
Chiprate ein Gold-Code mit nur 128 Chips Länge zu verwenden wäre, dies auch
durch einen entsprechenden Eintrag im Kapitel 3.3.4.2.2.3.2 – ggfs. mit Angabe
eines    sich   vom   FDD-Modus       unterscheidenden      Generator-Polynoms        –
dokumentiert. Gerade aufgrund des Fehlens einer solchen speziellen Definition
entnimmt der Fachmann, wie erläutert, dem ARIB-Standard für den TDD-Modus
einen vorgegebenen Kurzcode der Länge 1 Symbol (= 256 Chips) für die beiden
Chipraten 8,192 und 16,384 Mcps


Nach alledem ist der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ durch
keine der im ARIB-Standard offenbarten Varianten neuheitsschädlich getroffen.


δ) Die vorstehende Argumentation gilt auch für den Gegenstand des Anspruchs 8.


cc)     Der Gegenstand des Anspruchs 1 nach Hilfsantrag B.6‘ ist neu gegenüber
dem Dokument „Ireland-WCDMA“.

                                      - 57 -



Vor dem Prioritätstag des Streitpatents befand sich der Mobilfunkstandard UMTS
(Universal Mobile Telecommunications System) in der Evaluationsphase, d. h. es
wurden noch verschiedene Funkschnittstellen diskutiert (TR 146, S. 4, Foreword;
S. 5, Scope). Tdoc SMG2 359/97, im Folgenden „Ireland-WCDMA“ genannt, ist ein
Dokument der ETSI „SMG2 Wideband DS-CDMA concept group (Alpha)“.


(1)   Bei einer Verbindung zwischen Basis- und Mobilstation werden im Downlink
ein Dedicated Physical Data Channel (DPDCH) und ein Dedicated Physical Control
Channel (DPCCH) im zeitlichen Multiplex übertragen (S. 11, Fig 2). Die Nutz- bzw.
Steuersignale werden fachüblich mit einem Kurzcode (channelization code) und mit
einem Langcode (scrambling code) gespreizt bzw. verwürfelt (S. 12, Fig. 3). Der
Langcode ist als Gold-Code der Länge 40960 Chips ausgeführt (S. 12, drittletzer
Abs.). Die Kurzcodes sind als OVSF-Codes (orthogonal variable spreading factor)
ausgebildet (S. 12, Fig. 4), wobei der Wert des Spreizfaktors auf dem
DPDCH/DPCCH zwischen 4 und 256 liegen kann (S. 11, viertletzer Abs.).


Der logische Broadcast Control Channel (BCCH) wird auf den physikalischen
Primary Common Control Physical Channel (Primary CCPCH) abgebildet (S. 10,
Fig. 1), welcher zusammen mit dem Secondary CCPCH den CCPCH bildet. Dieser
Fest- oder Steuerkanal CCPCH unterscheidet sich grundsätzlich bezüglich
Spreizung und Verwürfelung nicht von den Kanälen DPDCH/DPCCH (S. 14,
drittletzter Absatz), wird jedoch im Unterschied zum DPDCH/DPCCH mit konstanter
Symbolrate übertragen, womit sein Spreizfaktor ebenfalls konstant ist. Der Primary
CCPCH wird zellunabhängig und fortlaufend immer mit der gleichen Bitrate von 32
kbps übertragen, der Secondary CCPCH nur bedarfsweise (vgl. S. 14, letzter Abs.).
Dabei entspricht die Bitrate von 32 kbps einer Symbolrate von 16 ksps, denn es
werden jeweils zwei Bits auf ein Symbol abgebildet (S. 12, Abs. 1).


Für die im Rahmen der Zellsuche erforderliche zeitliche Synchronisation der
Mobilstationen   auf   die   Basisstation   sendet   letztere   kontinuierlich   den

                                         - 58 -



Synchronisation Channel (SCH) aus, der einen Primary und einen Secondary SCH
umfasst (S. 15, Kap. 2.4.2.3):




                              Ireland-WCDMA, S. 15, Fig. 8


Dabei besteht der Primary SCH nur aus einem vorgegebenen Kurzcode cp der
Länge 256, der jeweils zu Beginn jedes Zeitschlitzes übertragen wird (S. 15,
Kap. 2.4.2.3, Abs. 3). In der Mobilstation wird für die Zeitschlitzsynchronisation ein
signalangepasstes Filter (matched filter) verwendet, dessen Koeffizienten den
Werten des vorgegebenen Kurzcodes cp entsprechen (S. 24, Kap. 2.6.4.1):


Der Synchronisationskanal SCH (Primary und Secondary SCH) wird mit den
Downlink-Kanälen DPDCH/DPCCH und CCPCH im Codemultiplex übertragen,
wober der SCH nicht verwürfelt, d. h. nicht mit dem basisstationsspezifischen
Langcode multipliziert wird (S. 15, Fig. 9 mit Beschreibung). Aus den Figuren 8 und
9 entnimmt der Fachmann, dass der Primary SCH (oberster Zweig in Figur 9) für
256 Chips je Zeitschlitz die Multiplikation des Symbols „1“ mit dem vorgegebenen
Kurzcode cp überträgt.


(2)   Es kann dahinstehen, ob die Kombination der fortlaufend von der
Basisstation ausgesendeten Kanäle Primary CCPCH und Primary SCH und des
bedarfsweise ausgesendeten Secondary SCH als Festkanäle im Sinne des
Merkmals 2 des Anspruchs 1 des Streitpatents angesehen werden können. Weiter
kann dahinstehen, ob die Kombination von Primary CCPCH und Primary SCH den

                                      - 59 -



einen Steuerkanal im Sinne des Merkmals 2.2 bilden, wogegen spricht, dass die
über den Primary CCPCH zu übertragenden Symbole fortlaufend, also sowohl im
ersten als auch im zweiten Abschnitt jedes Zeitschlitzes, mit dem ersten Kurzcode
und dem Langcode gespreizt und verwürfelt werden, was im Widerspruch zu den
Merkmalen 2.1, 2.2 und 2.3 stehend dürfte.


Jedenfalls erfüllen die Spreizfaktoren nicht Merkmal 4, da der Spreizfaktor auf dem
Primary CCPCH durchgängig, also auch im ersten Abschnitt jedes Zeitschlitzes,
den Wert 256 hat (4,096 Mcps/16 ksps = 256) und der Spreizfaktor des auf dem
Primary SCH gesendeten, vorgegebenen Kurzcodes cp ebenfalls den Wert 256
aufweist (S. 15, unter Figur 8: „The Primary SCH consists of an unmodulated
orthogonal Gold code of length 256 chips“).


Damit ist auch das Merkmal 2.3.1 (Spreizfaktor vorgegebener Kurzcode kleiner als
256) nicht aus Ireland-WCDDMA bekannt.


Danach sind die Gegenstände der Ansprüche 1 und 8 nach Hilfsantrag B.6‘ nicht
aus Ireland-WCDMA bekannt.


dd)   Die weiteren von den Klägerinnen genannten Druckschriften liegen vom
Gegenstand des Streitpatents weiter ab.


b)    Die Gegenstände der unabhängigen Patentansprüche 1 und 8 in der
Anspruchsfassung nach Hilfsantrag B.6‘ gelten auch als auf einer erfinderischen
Tätigkeit beruhend.


aa)   Ausgehend vom ARIB-Standard hat der Fachmann keine Veranlassung, im
TDD-Modus bei den Chipraten von 8,192 Mcps bzw. 16,384 Mcps den
vorgegebenen Kurzcode von 256 auf 128 zu kürzen, denn damit wäre – wie bereits
zur Frage der Neuheit dargelegt – jeweils eine             Verschlechterung der

                                      - 60 -



Zeitschlitzsynchronisation verbunden. Gleiches gilt für eine Verringerung des
Spreizfaktors im FDD-Modus für die Chipraten 4,096 Mcps und höher.


Der von der Klägerin zu 3 erhobene Einwand, der ARIB-Standard sei hinsichtlich
des Spreizfaktors des vorgegebenen Kurzcodes bei den verschiedenen Chipraten
widersprüchlich bzw. unvollständig und der Fachmann ziehe daher bei seinem
Bestreben, diese Widersprüche zu beseitigen bzw. diese Lücken zu schließen in
Betracht, bei den höheren Chipraten im TDD-Modus einen Spreizfaktor von 128 zu
verwenden, greift nicht. Denn der ARIB-Standard ist – wie zur Neuheit dargelegt –
jedenfalls in diesen Punkten weder lückenhaft noch widersprüchlich, sondern zeigt
dem Fachmann auf, welche vorgegebenen Codes für die verschiedenen Chipraten
zu verwenden sind. Insofern besteht für den Fachmann keine Veranlassung,
Änderungen an den jeweils in sich geschlossenen Varianten vorzunehmen.


bb)   Die EP 315 gibt dem Fachmann keinen Anlass, bei dem europäischen
UMTS-Vorschlag (Ireland-WCDMA) oder dem japanischen ARIB-Standard den
Spreizfaktor des vorgegebenen Kurzcodes zu verringern.


Die EP 315 möchte bei einem DS-CDMA-System eine vereinfachte, beschleunigte
und stabile Empfängersynchronisation ermöglichen (S. 2, li. Sp. – re. Sp., Abs. 2).
Hierzu wird regelmäßig eine kurze, vorgegebene Synchronisationssequenz (11
Chip Barker Code) ausgesendet, die in einem signalangepassten SAW-Filter
(surface acoustic wave matched filter) des Empfängers einen hohen Korrelationswert erzeugt (Fig. 3 5; Sp. 2, Z. 9, 10). Die zu übertragenden Basisbandsignale
werden mit einem Kurzcode der Länge 1024 gespreizt (Sp. 1, Z. 57 - 59).


Die EP 315 zeigt ein Kommunikationssystem, bei dem es weder die in
Mobilfunksystemen üblichen Festkanäle zur Übertragung von Steuersignalen nach
Merkmal 2 noch einen Langcode zur Unterscheidung mehrerer Basisstationen
gemäß Merkmal 2.1 gibt. Das zur Synchronisation verwendete signalangepasste
SAW-Filter empfängt unmittelbar das Hochfrequenzsignal der Empfangsantenne

                                           - 61 -



(Fig. 1),    was     bei   einem   Mobilfunksystem        zu   einer   nicht    hinnehmbaren
Verschlechterung des Signal-zu-Rausch-Verhältnisses aufgrund der Dämpfung des
SAW-Filters führen würde. Die EP 315 sieht das SAW-Filter zudem als Abkehr von
den bei Mobilfunksystemen üblichen Synchronisationsschaltungen (S. 2, li. Sp.,
drittletzer Abs. – re. Sp., Abs. 1). Daher betrachtet der Fachmann die EP 315 als
eine in sich geschlossene Lösung, die nicht auf die Mobilfunksysteme nach Ireland-WCDMA bzw. ARIB-Standard anwendbar ist.


cc)       Auch unter Hinzunahme des übrigen im Verfahren genannten Standes der
Technik kommt der Fachmann nicht in nahe liegender Weise zu den Gegenständen
der Ansprüche 1 und 8 gemäß Hilfsantrag B.6‘.


Insbesondere steht auch die Druckschrift Nakamura_IEEE der Patentfähigkeit des
Streitpatents in der Fassung nach Hilfsantrag B.6‘ nicht entgegen.


(1)       Sie bildet schon keinen Stand der Technik nach Art. 54 EPÜ, da sie
frühestens am 21. Mai 1998 veröffentlicht wurde und das Streitpatent jedenfalls in
der Fassung nach Hilfsantrag B.6‘ die Priorität vom 13. Mai 1998 aus JP 12999598
wirksam        in   Anspruch    nimmt.   Denn       die   Übersetzung     der     japanischen
Prioritätsanmeldung des Streitpatents zeigt die Merkmale der Ansprüche 1 und 8
nach Hilfsantrag B.6‘ wie folgt:
      1             Zeitschlitzsynchronisationsverfahren für ein mobiles CDMA-Kommunikationssystem, umfassend die Schritte:
                       A. 1: A mobile communication system using the code
                       division multiple access system […] slot timing
                       synchronization (cell search);
      2             Senden eines SteuersignaIs von einer Basisstation über
                    Festkanäle (106, 107), die so beschaffen sind, dass
                       S. 3, 4, Abs. 0004; Fig. 2
      2.1spr           ein der Basisstation zugeordneter Langcode und

                                   - 62 -



2.2spr    ein erster Kurzcode einen ersten Abschnitt (102) eines
          Zeitschlitzes des Festkanals spreizen und
              S. 4, Abs. 0004: In a data symbol section 102 […] a
              control signal transmitted to the mobile terminal is
              spread by a long code and short code 103.
2.3spr    ein vorgegebener Kurzcode einen zweiten Abschnitt (131) des
          einen Zeitschlitzes spreizt, und
              A. 2: long code masked symbol formed of a common
              short code CSC; S. 4, Abs. 0005: The CSC is a short
              period spread code defined common to base stations
              disposed in the mobile communication system; Fig. 3
3         in einem mobilen Endgerät,
3.1dspr   Entspreizen des zweiten Abschnitts des einen Zeitschlitzes
          unter Verwendung des vorgegebenen Kurzcodes und
3.2dspr   Ausführen einer Zeitschlitzsynchronisation unter Verwendung
          eines     als     Ergebnis    des        Entspreizens   erhaltenen
          Korrelationswerts
              S. 5, Z. 1, 2: the mobile terminal despreads the perch
              channels by using the CSC and synchronizes timing
              having a high correlation value as slot timing; S. 8,
              Abs. 0013: In the timing synchronizer 810, it is
              necessary to derive correlation values of timing
              corresponding to one symbol […] to maximize the
              accumulated correlation values, as slot timing
4         dadurch     gekennzeichnet,       dass     ein   Spreizfaktor   des
          vorgegebenen Kurzcodes auf einen niedrigeren Wert als ein
          Spreizfaktor des ersten Kurzcodes des ersten Abschnitts
          eingestellt ist
              A. 1: a spreading factor of the long code masked
              symbol is set to a value lower than that of spreading
              factors of other ordinary symbols

                                    - 63 -



2.3.1         und geringer als 256 ist.
                 S. 7, Z. 15, 16: spreading factor of the mask
                 symbol is 64; Abs. 0018


3        Mobiles       Endgerät           für     ein         mobiles    CDMA-Kommunikationssystem, bei dem
              S. 7, Z. 27, 28: a mobile terminal used in a CDMA
              mobile communication system
3.3      eine RF-Einheit (801) zum Umwandeln eines von einer Antenne
         empfangenen Signals, das eine Trägerfrequenz hat, in ein
         Basisbandsignal und
              S. 8, Z. 2 - 4: A received signal of a carrier frequency
              received from an antenna is lowered in frequency by
              an RF unit 801
3.4      ein signalangepasstes Filter (901) zum Empfangen des
         Basisbandsignals und
              Fig. 9: MF 901
3.1_3.2dspr    zum        Entspreizen       des       Basisbandsignals       unter
         Verwendung des zweiten Kurzcodes (CSC) und zum Ausgeben
         eines       Korrelationswertes           zur     Herstellung        einer
         Zeitschlitzsynchronisation,
              S. 8, Z. 21 – S. 9, Z. 3: In the timing synchronizer 810,
              it is necessary to derive correlation values of timing
              corresponding to one symbol […] MF 901 capable of
              providing     correlation     results     […]    accumulated
              correlation values, as slot timing; S. 5, Z. 1, 2: the
              mobile terminal despreads the perch channels by
              using the CSC and synchronizes timing having a high
              correlation value as slot timing

                                        - 64 -



(2)   Selbst wenn das Streitpatent die Priorität nicht wirksam in Anspruch nähme,
steht Nakamura_IEEE der Patentfähigkeit des Streitpatents in der Fassung nach
Hilfsantrag B.6‘ nicht entgegen.
Das in Nakamura_IEEE vorgeschlagene mobile CDMA-Kommunikationssystem
ähnelt demjenigen des ARIB-Standards (S. 974, Tab. 1, Fig. 2, 3; S. 975, Fig. 4),
insbesondere hinsichtlich der „Standard“-Chiprate von 4,096 Mcps (S. 974, li. Sp.,
Abs. unter Tab. 1). Die Symbolrate auf den Festkanälen (perch channels) beträgt –
ebenfalls wie im ARIB-Standard – 16 ksps (S. 974, re. Sp., Abs. 2), womit sich für
die Chiprate von 4,096 Mcps ein Spreizfaktor des ersten Kurzcodes von 256 ergibt.
Der vorgegebene Kurzcode ist als orthogonaler Gold-Code ausgestaltet (S. 974,
Tab. 1; S. 975, li. Sp., Z. 9 – 12); zu seinem Spreizfaktor finden sich keine Angaben,
womit der Fachmann mitliest, dass der Spreizfaktor des vorgegebenen Kurzcodes
ebenfalls 256 beträgt. Damit sind aus Nakamura_IEEE jedenfalls die Merkmale 4
und 2.3.1 der Gegenstände der Ansprüche 1 und 8 nach Hilfsantrag B.6‘ nicht
bekannt.
Es ist auch nicht ersichtlich, inwiefern weiterer Stand der Technik, etwa die im
Streitpatent genannte Higuchi_IEICE oder die in Nakamura_IEEE zitierte
Higuchi_IEEE,     dem     Fachmann     nahe      legen   könnten,    unterschiedliche
Spreizfaktoren zu verwenden. Higuchi_IEICE und Higuchi_IEEE zeigen jeweils ein
CDMA-System mit einer festen Chiprate von 4,096 Mcps und einer Symbolrate von
64 ksps     auf     den     Festkanälen       (Higuchi_IEEE,     S. 1432,     Tab. 1;
Higuchi_IEICE_deutsch, S. 9, Tab. 1, wobei eine Bitrate von 128 kbps einer
Symbolrate von 64 ksps entspricht). Demgemäß haben die Spreizfaktoren sowohl
des ersten Kurzcodes als auch des vorgegebenen Kurzcodes jeweils den Wert 64.


5.    Da die Beklagte in dem geschlossen gestellten Hilfsantrag B.6‘ die
angegriffenen Patentansprüche 3, 7 und 9 nicht verteidigt, sind diese nicht weiter
zu prüfen und die Klagen der Klägerinnen 1 und 2 bleiben auch insoweit erfolgreich.


Da sich die beschränkte Verteidigung der angegriffenen Patentansprüche 1 und 8
in der Fassung des Hilfsantrags B.6‘ somit als zulässig und die Gegenstände der

                                      - 65 -



Patentansprüche 1 und 8 nach Hilfsantrag B.6‘ als patentfähig erweisen, war das
Streitpatent teilweise im angegriffenen Umfang nur hinsichtlich der erteilten
Fassung (Hauptantrag) und der nicht verteidigten Patentansprüche 3, 7 und 9 für
nichtig zu erklären, während die Klagen im Hinblick auf die Fassung der
Patentansprüche 1 und 8 nach Hilfsantrag B.6‘ abzuweisen waren.


                       V. Zu den weiteren Hilfsanträgen


Da sich das Streitpatent in der Fassung nach Hilfsantrag B.6‘ als schutzfähig
erweist, bedarf es keiner Entscheidung, ob das Streitpatent auch in den Fassungen
der nachrangigen Hilfsanträge schutzfähig wäre.



                                       B.
                            Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. §§ 92 Abs. 2 Nr. 1,
91a Abs. 1 ZPO.


Dabei hat der Senat berücksichtigt, dass der nach Hilfsantrag B.6‘ als schutzfähig
verbleibende Patentgegenstand gegenüber demjenigen der erteilten Fassung
eingeschränkt ist. Diese Einschränkung ist verhältnismäßig geringfügig, fällt nach
der Schätzung des Senats bei der wirtschaftlichen Verwertbarkeit des Streitpatents
kaum ins Gewicht und veranlasst keine höheren Kosten. Dementsprechendes gilt
für die unterschiedlich weiten Angriffe der einzelnen Klägerinnen auf das
Streitpatent. Daher haften die Klägerinnen trotz teilweiser Nichtigerklärung des
Streitpatents für die Gerichtskosten insgesamt gesamtschuldnerisch und für die
gesamten außergerichtlichen Kosten der Beklagten nach Kopfteilen (§ 84 Abs. 2
PatG i.V.m. § 100 Abs. 1 ZPO.

                                       - 66 -



Soweit die Parteien den Rechtsstreit in der Hauptsache übereinstimmend teilweise
hinsichtlich des Angriffs auf Patentanspruch 4 für erledigt erklärt haben, war gemäß
§§ 84 Abs. 2 S. 2, 99 Abs. 1 PatG i.V.m. § 91a Abs. 1 S. 1 ZPO insoweit (nur) noch
über die Kosten unter Berücksichtigung des bisherigen Sach- und Streitstandes
nach billigem Ermessen zu entscheiden. Auf der Grundlage einer summarischen
Prüfung sind dabei die (mutmaßlichen) Erfolgsaussichten der Klage im Zeitpunkt
der Abgabe der Erledigungserklärungen zu beurteilen (vgl. BGH GRUR 2001, 140
Zeittelegramm; Keukenschrijver, Patentnichtigkeitsverfahren, 6. Aufl., Rn. 277).
Somit ist insbesondere das Erlöschen des Streitpatents bei der Entscheidung nicht
zu berücksichtigen. Allerdings erachtet der Senat auch die wirtschaftliche
Verwertbarkeit von Patentanspruch 4 im Verhältnis zu dem als schutzfähig
verbleibenden Patentgegenstand als geringfügig, so dass auch bei unterstelltem
Erfolg des Teilangriffs insoweit keine Kostenauferlegung zu Lasten der Beklagten
in Betracht käme.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.



                                        C.


                       Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130)
eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland
zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der
Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt
unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten

                                          - 67 -



elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen
elektronischen Signatur versehen sein, die von einer internationalen Organisation
auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich
zur Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die
Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die
Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der
Berufungsschrift   soll   eine   Ausfertigung      oder   beglaubigte       Abschrift   des
angefochtenen Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument     in    die    elektronische      Poststelle    des       Bundesgerichtshofes
(www.bundesgerichtshof.de/erv.html)       übertragen      werden.     Die    Berufungsfrist
beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens
aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur
gewahrt, wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht.



 Friehe               Müller          Werner               Arnoldi                 Matter

                                                                                        prö
