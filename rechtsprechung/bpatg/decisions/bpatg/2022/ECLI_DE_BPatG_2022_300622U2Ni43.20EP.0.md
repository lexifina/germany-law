---
ecli: "ECLI:DE:BPatG:2022:300622U2Ni43.20EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 43/20"
decided: "2022-06-30"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2022&Sort=1&Seite=18&nr=43210&anz=542&pos=280&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2022-06-30_2_Ni_43_20_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0269.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 43/20 vom 2022-06-30

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                       Verkündet am
                                                       30. Juni 2022
2 Ni 43/20 (EP)                                              …
verbunden mit
2 Ni 44/20 (EP)

(Aktenzeichen)



                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2022:300622U2Ni43.20EP.0

                                        -2-




              betreffend das europäische Patent EP 2 286 629
                              (DE 60 2009 025 963)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 30. Juni 2022 unter Mitwirkung des Richters
Dr. Himmelmann als Vorsitzenden sowie der Richter Dipl.-Phys. Dr. rer. nat.
Friedrich, Dipl.-Phys. Dr. rer. nat. Zebisch, Dr. Söchtig und Dr.-Ing. Kapels

                                            -3-



für Recht erkannt:


      I.      Das europäische Patent EP 2 286 629 wird mit Wirkung für
              das Hoheitsgebiet der Bundesrepublik Deutschland für
              nichtig erklärt.


      II.     Von den Gerichtskosten haben die Klägerin zu 1) 1/3 und die
              Beklagte 2/3 zu tragen. Von den außergerichtlichen Kosten
              der Beklagten hat die Klägerin zu 1) 1/3 zu tragen. Die
              Beklagte hat die außergerichtlichen Kosten der Klägerinnen
              zu 2) und zu 3) zu tragen. Im Übrigen haben die Parteien ihre
              außergerichtlichen Kosten selbst zu tragen.


      III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
              des zu vollstreckenden Betrages vorläufig vollstreckbar.




                                    Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
erteilten europäischen Patents EP 2 286 629, das am 28. April 2009 unter
Beanspruchung        der   US-Prioritäten   US 125961 P   vom   28. April 2008   und
US 48554 P und US 48908 P jeweils vom 29. April 2008 angemeldet worden ist.
Der Hinweis auf die Erteilung des Patents wurde am 13. August 2014 veröffentlicht.
Im Rahmen eines gegen das Patent gerichteten Einspruchsverfahrens wurde
dieses beschränkt aufrechterhalten und als EP 2 286 629 B2 veröffentlicht (im
Folgenden: Streitpatent). Das Streitpatent mit der Bezeichnung „Method and
apparatus to link modulating and coding scheme to amount of resources (Verfahren
und Vorrichtung zur Verknüpfung des Modulations- und Codierungsverfahrens mit
der Betriebsmittelmenge)“ wird vom Deutschen Patent- und Markenamt unter dem
Aktenzeichen 60 2009 025 963 geführt.

                                        -4-



Das Streitpatent umfasst sieben Patentansprüche, davon den unabhängigen
Verfahrensanspruch 1, den unabhängigen Vorrichtungsanspruch 5 und den formal
nebengeordneten Erzeugnisanspruch 7 sowie die unmittelbar auf Patentanspruch
1 rückbezogenen Unteransprüche 2 bis 4 sowie den unmittelbar auf Patentanspruch
5 rückbezogenen Unteranspruch 6.


Der geltende Patentanspruch 1 lautet in der Verfahrenssprache Englisch gemäß
EP 2 286 629 B2 mit hinzugefügter Merkmalsgliederung des Senats:


  1.   A method for linking modulating and coding scheme to amount of resources,
       comprising:
       1.1     - providing a plurality of static input parameters;
       1.2     - providing a plurality of signaled input parameters; and
       1.3     - determining from said static input parameters and said plurality of
               signalled input parameters an output parameter indicative of a
               number of control symbols per transmission time interval for an
               amount of control signaling bits,
       1.3.1   - wherein said output parameter relates to a physical resource with
               given modulation and coding scheme for an uplink,
       1.3.2   - characterized in that said determining of the output parameter
               employs a ceil operation on a quantity that includes a product of a
               number of control signalling bits multiplied by a coding rate divided
               by a number of uncoded bits per symbol and an offset parameter
               according to
                           ⋅
       1.3.3         =          _   , wherein

                     is the output parameter,
                 is the number of control signalling bits transmitted with uplink data
               on the Physical Uplink Shared Channel, PUSCH,
                  is the coding rate of the given Modulation and Coding Scheme
               of the PUSCH data channel,

                                             -5-



                     is the number of uncoded bits per symbol for the given uplink
               data Modulation and Coding Scheme,
                      _   is the offset parameter, wherein the offset parameter is
               the quality difference between a given control channel carrying the
               control signalling bits and the PUSCH data channel,
               ⌈ ⌉ denotes the ceil operation.


In deutscher Übersetzung gemäß der Streitpatentschrift EP 2 286 629 B2 lautet der
geltende Patentanspruch 1 wie folgt (mit Merkmalsgliederung):


  1.   Verfahren zum Verbinden eines Modulations- und Codierungsschemas mit
       einer Menge von Betriebsmitteln, das Folgendes umfasst:
       1.1     Bereitstellen von mehreren statischen Eingabeparametern;
       1.2     Bereitstellen von mehreren signalisierten Eingabeparametern; und
       1.3     Bestimmen aus den statischen Eingabeparametern und den
               mehreren          signalisierten            Eingabeparametern        eines
               Ausgabeparameters, der eine Anzahl von Steuersymbolen pro
               Übertragungszeitintervall             für      eine      Menge        von
               Steuersignalisierungsbits angibt,
       1.3.1   wobei sich       der        Ausgabeparameter auf ein      physikalisches
               Betriebsmittel        mit     einem    gegebenen      Modulations-    und
               Codierungsschema für eine Aufwärtsstrecke bezieht,
       1.3.2   dadurch     gekennzeichnet,            dass     das    Bestimmen      des
               Ausgabeparameters eine Nächste-obere-Ganzzahl-Operation auf
               einer Quantität einsetzt, die ein Produkt einer Anzahl von
               Steuersignalisierungsbits multipliziert mit einer Codierungsrate
               dividiert durch eine Anzahl uncodierter Bits pro Symbol und einen
               Versatzparameter enthält, gemäß:
                           ⋅
       1.3.3         =           _     , wobei

                     der Ausgabeparameter ist,

                                             -6-



                        die   Anzahl   von    mit    Aufwärtsstreckendaten       auf   dem
                  gemeinsamen physikalischen Aufwärtsstreckenkanal, PUSCH,
                  übertragenen Steuersignalisierungsbits ist,
                        die   Codierungsrate       des   gegebenen      Modulations-   und
                  Codierungsschemas des PUSCH-Datenkanals ist,
                          die Anzahl uncodierter Bits pro Symbol für das gegebene
                  Aufwärtsstreckendaten-Modulations- und -Codierungsschema ist,
                          _    der Versatzparameter ist, wobei der Versatzparameter
                  der    Qualitätsunterschied       zwischen    einem     gegebenen     die
                  Steuersignalisierungsbits führenden Steuerkanal und dem PUSCH-Datenkanal ist,
                  ⌈ ⌉ die Nächste-obere-Ganzzahl-Operation bezeichnet.


Der    geltende    unabhängige      Patentanspruch        5    lautet   mit   hinzugefügter
Merkmalsgliederung des Senats wie folgt:


  5.    An apparatus for linking modulating and coding scheme to amount of
        resources, comprising:
        5.1       - an uplinking module configured to provide a plurality of - static
                  input parameters;
        5.2       the apparatus being configured for providing a plurality of signalled
                  input parameters; and
        5.3       - a processor configured to determine from said static input
                  parameters and said plurality of signalled input parameters an
                  output parameter indicative of a number of control symbols per
                  transmission time interval for an amount of control signalling bits,
        5.3.1     - wherein said output parameter relates to a modulation and coding
                  scheme for an uplink,
        5.3.2     - characterized in that said processor employs a ceil operation on a
                  quantity that includes a product of a number of control signalling bits
                  multiplied by a coding rate divided by a number of uncoded bits per
                  symbol and an offset parameter according to

                                           -7-



                              ⋅
          5.3.3        =           _    , wherein

                       is the output parameter,
                    is the number of control signalling bits transmitted with uplink data
                  on the Physical Uplink Shared Channel, PUSCH,
                     is the coding rate of the given Modulation and Coding Scheme
                  of the PUSCH data channel,
                        is the number of uncoded bits per symbol for the given uplink
                  data Modulation and Coding Scheme,
                         _   is the offset parameter, wherein the offset parameter is
                  the quality difference between a given control channel carrying the
                  control signalling bits and the PUSCH data channel,
                  ⌈ ⌉ denotes the ceil operation.


In    deutscher   Übersetzung     gemäß      Streitpatentschrift   lautet   der   geltende
Patentanspruch 5 wie folgt (mit Merkmalsgliederung):


     5.   Vorrichtung zum Verbinden eines Modulations- und Codierungsschemas
          mit einer Menge von Betriebsmitteln, die Folgendes umfasst:
          5.1     ein Aufwärtsverbindungsmodul, das konfiguriert ist, mehrere
                  statische Eingabeparameter bereitzustellen;
          5.2     wobei die Vorrichtung konfiguriert ist, mehrere signalisierte
                  Eingabeparameter bereitzustellen; und
          5.3     einen Prozessor, der konfiguriert ist, aus den statischen
                  Eingabeparametern         und     den      mehreren        signalisierten
                  Eingabeparametern einen Ausgabeparameters zu bestimmen, der
                  eine Anzahl von Steuersymbolen pro Übertragungszeitintervall für
                  eine Menge von Steuersignalisierungsbits angibt,
          5.3.1   wobei sich      der   Ausgabeparameter auf ein            physikalisches
                  Betriebsmittel für eine Aufwärtsstrecke bezieht,

                                                -8-



        5.3.2     dadurch gekennzeichnet, dass der Prozessor eine Nächste-obere-Ganzzahl-Operation auf einer Quantität einsetzt, die ein Produkt
                  einer Anzahl von Steuersignalisierungsbits multipliziert mit einer
                  Codierungsrate dividiert durch eine Anzahl uncodierter Bits pro
                  Symbol und einen Versatzparameter enthält, gemäß:
                               ⋅
        5.3.3            =          _     , wobei

                         der Ausgabeparameter ist,
                        die   Anzahl      von    mit    Aufwärtsstreckendaten       auf   dem
                  gemeinsamen physikalischen Aufwärtsstreckenkanal, PUSCH,
                  übertragenen Steuersignalisierungsbits ist,
                        die   Codierungsrate          des   gegebenen      Modulations-   und
                  Codierungsschemas des PUSCH-Datenkanals ist,
                          die Anzahl uncodierter Bits pro Symbol für das gegebene
                  Aufwärtsstreckendaten-Modulations- und -Codierungsschema ist,
                          _    der Versatzparameter ist, wobei der Versatzparameter
                  der    Qualitätsunterschied          zwischen    einem     gegebenen     die
                  Steuersignalisierungsbits führenden Steuerkanal und dem PUSCH-Datenkanal ist,
                  ⌈ ⌉ die Nächste-obere-Ganzzahl-Operation bezeichnet.


Der    geltende    unabhängige          Patentanspruch       7    lautet   mit   hinzugefügter
Merkmalsgliederung des Senats wie folgt:


  7.    A computer program product comprising
        7.1       a computer readable medium having executable code stored
                  therein;
        7.2       the code, when executed by a processor, adapted to carry out the
                  method of claims 1 to 4.

                                         -9-



In deutscher Übersetzung gemäß Streitpatentschrift lautet der Patentanspruch 7
wie folgt (mit Merkmalsgliederung):


  7.    Computerprogrammprodukt,
        7.1      das ein computerlesbares Medium umfasst, das darin gespeichert
                 ausführbaren Code aufweist;
        7.2      wobei der Code, wenn er durch einen Prozessor ausgeführt wird,
                 ausgelegt ist, das Verfahren nach den Ansprüchen 1 bis 4
                 auszuführen.


Wegen des Wortlauts der abhängigen Unteransprüche 2 bis 4 sowie 6 wird auf die
Streitpatentschrift verwiesen.


Mit Schriftsatz vom 27. August 2019 ist die Klägerin zu 2) dem Rechtsstreit auf
Seiten der Klägerin zu 1) beigetreten.


Mit Beschluss vom 7. November 2019 hat der damals zuständige 4. Senat die
Verfahren     4 Ni 58/19 (EP)    (2 Ni 43/20 (EP)     (neu))    und    4 Ni 59/19 (EP)
(2 Ni 44/20 (EP) (neu))   zum    Zwecke     der   gemeinsamen       Verhandlung   und
Entscheidung miteinander verbunden und unter dem führenden Aktenzeichen
4 Ni 58/19 (EP) (2 Ni 43/20 (EP) (neu)) weitergeführt.


Mit Schriftsatz vom 2. Juni 2021 hat die Klägerin zu 1) ihre Klage zurückgenommen.


Die Klägerinnen zu 2) und 3) machen hinsichtlich der geltenden Fassung des
Streitpatents den Nichtigkeitsgrund der fehlenden Patentfähigkeit in Form
mangelnder Neuheit und fehlender erfinderischer Tätigkeit geltend (Art. II § 6 Abs. 1
Satz 1 Nr. 1 i. V. m. Art. 138 Abs. 1 lit. a) EPÜ i. V. m. Art. 54, 56 EPÜ).


Zur Stützung ihres Vorbringens haben die Klägerinnen zu 2 und 3 insbesondere die
folgenden Dokumente genannt:

                                    - 10 -



QE D 1   Nokia Siemens Networks, Nokia: „Linkage between PUSCH MCS and
         amount of resources for control on PUSCH”, 3GPP TSG RAN WG1
         Meeting #53, Kansas City, MO, USA, 5.-9. Mai 2008, R1-081852,
         veröffentlicht am 14. Mai 2008 (entspr. Anlage BP 6 der Klägerin zu
         3))
QE D 2   Freescale Semiconductor: “Control Region on the PUSCH”, 3GPP
         TSG-RAN WG1 Meeting #52bis, Shenzhen, China, March 31 – April 4,
         2008, R1-081331, veröffentlicht am 26. März 2008 (entspr. Anlage
         BP 7 der Klägerin zu 3))
QE D 3   Motorola: “Resource Provision for UL Control in PUSCH”, 3GPP TSG
         RAN WG1 Meeting #52bis, Shenzhen, China, March 31 – April 4,
         2008, R1-081295, veröffentlicht am 26. März 2008 (entspr. Anlage
         BP 10 der Klägerin zu 3))
QE D 4   Samsung: “Results for the linkage between PUSCH MCS and
         ACK/NACK resource amount on PUSCH”, 3GPP TSG RAN WG1
         Meeting #52bis, Shenzhen, China, March 31 –April 4, 2008, R1-
         081218, veröffentlicht am 26. März 2008 (entspr. Anlage BP 8 der
         Klägerin zu 3))
QE D 5   Samsung: “Multiplexing Control and Data in the PUSCH”, 3GPP TSG
         RAN WG1 Meeting #52bis, Shenzhen, China, March 31 – April 4,
         2008, R1-081223, veröffentlicht am 26. März 2008 (entspr. Anlage
         BP 9 der Klägerin zu 3))
QE D 6   WO 2007/148583 A1, angemeldet am 13. Juni 2007, offengelegt am
         27. Dezember 2007 (entspr. Anlage BP 11 der Klägerin zu 3))
QE D 7   EP 2 031 888 A1, angemeldet am 13. Juni 2007, offengelegt am
         4. März 2009 (entspr. Anlage BP 12 der Klägerin zu 3))
QE D 8   NTT DoCoMo et al: „Implicit Resource Allocation of ACK/NACK Signal
         in E-UTRA Uplink“, 3GPP TSG RAN WG1 Meeting #48bis St. Julians,
         Malta, March 26 - 30, 2007, R1-071650, veröffentlicht am 3. April 2007
         (entspr. Anlage BP 13 der Klägerin zu 3))

                                        - 11 -



QE D 9       Nokia: “Uplink Scheduling for VoIP”, 3GPP TSG-RAN WG2 Meeting
             #57, St. Louis, Missouri, February 12 - 16, 2007, R2-070476,
             veröffentlicht am 10. Januar 2007 (entspr. Anlage BP 14 der Klägerin
             zu 3))
QE D 10      3GPP: TS 36.212 V8.2.0 (2008-03), 3rd Generation Partnership
             Project; Technical specification group radio access network; Evolved
             universal terrestrial radio access (E-UTRA); Multiplexing and channel
             coding (Release 8), veröffentlicht am 20. März 2008 (entspr. Anlage
             BP 15 der Klägerin zu 3))
QE D 11      3GPP: TS 36.213 V8.2.0 (2008-03), 3rd Generation Partnership
             Project; Technical specification group radio access network; Evolved
             universal terrestrial radio access (E-UTRA); Physical layer procedures
             (Release 8), veröffentlicht am 20. März 2008 (entspr. Anlage BP 16
             der Klägerin zu 3))


Die Klägerin zu 2) stützt ihr Vorbringen darüber hinaus noch insbesondere auf die
folgenden Dokumente:


NK2                   Gutachten zum Streitpatent des Herrn Prof. Dr. B…, Leiter
                      des Instituts für Nachrichtentechnik an der Technischen
                      Universität H…, vom 15. August 2019
Anlage 1 zur NK2 S. Le Goff, A. Glavieux, C. Berrou: Turbo-codes and high
                      spectral efficiency modulation. IEEE International Conference
                      on Communications (ICC), 1994, S. 645-649


Die Klägerin zu 2) und die Klägerin zu 3) sind der Auffassung, das Streitpatent sei
nicht patentfähig, da die Lehre der unabhängigen Patentansprüche 1, 5 und 7
jedenfalls durch die Entgegenhaltungen QE D 1 (BP 6), QE D 2 (BP 7) und QE D 3
(BP 10) neuheitsschädlich vorweggenommen werde. Die Schrift QE D 1 (BP 6)
gehöre zum vorveröffentlichten Stand der Technik, denn das Streitpatent nehme die
von ihm benannten Prioritäten nicht wirksam in Anspruch. Die Klägerin zu 2) meint
darüber hinaus, dass das Verfahren des Anspruchs 1 des Streitpatents auch nicht

                                        - 12 -



neu gegenüber der QE D 4 (BP 8) sei. Beide Klägerinnen sind darüber hinaus
übereinstimmend der Auffassung, dass es dem Gegenstand der Ansprüche 1, 5 und
7 jedenfalls aber an der erfinderischen Tätigkeit mangele. Auch die zusätzlichen
Merkmale der rückbezogenen Unteransprüche enthielten nach Auffassung der
Klägerin zu 2 nichts Patentfähiges.


Die Klägerin zu 2) stellt den Antrag,


           das europäische Patent 2 286 629 in vollem Umfang mit Wirkung für das
           Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Klägerin zu 3) stellt den Antrag,


           das europäische Patent 2 286 629 im Umfang der Patentansprüche 1, 5
           und 7 für nichtig zu erklären.


Die Beklagte beantragt,


           die Klage abzuweisen,
           hilfsweise
           das europäische Patent 2 286 629 dadurch teilweise für nichtig zu
           erklären,    dass seine Patentansprüche die Fassung eines der
           Hilfsanträge 1 vom 25. April 2022, 1a vom 28. Juni 2022, 1b vom
           30. Juni 2022 und 2 vom 25. April 2022, in dieser Reihenfolge, erhalten.


Der Anspruch 1 des Hilfsantrags 1 lautet mit hinzugefügter Gliederung wie folgt:
(Änderungen zum Hauptantrag sind unterstrichen):


  1.    A method for linking modulating and coding scheme to amount of resources,
        comprising:
        1.1     - providing a plurality of static input parameters;
        1.2     - providing a plurality of signaled input parameters; and

                               - 13 -



1.3     - determining from said static input parameters and said plurality of
        signalled input parameters an output parameter indicative of a
        number of control symbols per transmission time interval for an
        amount of control signaling bits,
1.3.1   - wherein said output parameter relates to a physical resource with
        given modulation and coding scheme for an uplink,
1.3.2   - characterized in that said determining of the output parameter
        employs a ceil operation on a quantity that includes a product of a
        number of control signalling bits multiplied by a coding rate divided
        by a number of uncoded bits per symbol and an offset parameter
        according to
                    ⋅
1.3.3        =          _   , wherein

             is the output parameter,
          is the number of control signalling bits transmitted with uplink data
        on the Physical Uplink Shared Channel, PUSCH,
           is the coding rate of the given Modulation and Coding Scheme
        of the PUSCH data channel,
              is the number of uncoded bits per symbol for the given uplink
        data Modulation and Coding Scheme,
               _    is the offset parameter, wherein the offset parameter is
        the quality difference between a given control channel carrying the
        control signalling bits and the PUSCH data channel,
        ⌈ ⌉ denotes the ceil operation,
1.3.4   and wherein the offset parameter is defined separately for different
        PUSCH bandwidths or for different Modulation and Coding
        Schemes or for different service types or for different control
        channels.

                                         - 14 -



Der Anspruch 1 des Hilfsantrags 1a ergibt sich aus dem Anspruch 1 des Hilfsantrags
1, indem im Merkmal 1.3.4 die Alternative für unterschiedliche Modulations- und
Codierschemata gestrichen wurde (Änderungen zum Merkmal 1.3.4 des Anspruchs
1 von Hilfsantrag 1 sind durchgestrichen):


        1.3.4’   and wherein the offset parameter is defined separately for different
                 PUSCH bandwidths or for different Modulation and Coding
                 Schemes or for different service types or for different control
                 channels.


Der Anspruch 1 des Hilfsantrags 1b stimmt mit Anspruch 1 nach Hilfsantrag 1a
überein, jedoch sind der selbständige Anspruch 5 und der auf diesen rückbezogene
Unteranspruch 6 gestrichen.


Der Anspruch 1 des Hilfsantrags 2 lautet mit hinzugefügter Gliederung wie folgt
(Änderungen zum Anspruch 1 des Hauptantrags sind unterstrichen):


  1.    A method for linking modulating and coding scheme to amount of resources,
        comprising:
        1.1      - providing a plurality of static input parameters;
        1.2      - providing a plurality of signaled input parameters; and
        1.3      - determining from said static input parameters and said plurality of
                 signalled input parameters an output parameter indicative of a
                 number of control symbols per transmission time interval for an
                 amount of control signaling bits,
        1.3.1    - wherein said output parameter relates to a physical resource with
                 given modulation and coding scheme for an uplink,
        1.3.2’   - characterized in that said determining of the output parameter
                 employs a ceil operation on a quantity that includes a product of a
                 number of control signalling bits multiplied by a coding rate divided
                 by a number of uncoded bits per symbol and an offset parameter,
                 and the result of the ceil operation on the quantity is chosen as the

                                             - 15 -



                 output parameter if the result of the ceil operation on the quantity is
                 the maximum value of a group consisting of the result of the ceil
                 operation on the quantity and a predetermined number, according
                 to
                                     ⋅
        1.3.3‘   Mctrl = max (           _    , K), wherein

                         is the output parameter,
                      is the number of control signalling bits transmitted with uplink data
                 on the Physical Uplink Shared Channel, PUSCH,
                       is the coding rate of the given Modulation and Coding Scheme
                 of the PUSCH data channel,
                          is the number of uncoded bits per symbol for the given uplink
                 data Modulation and Coding Scheme,
                           _    is the offset parameter, wherein the offset parameter is
                 the quality difference between a given control channel carrying the
                 control signalling bits and the PUSCH data channel,
                 ⌈ ⌉ denotes the ceil operation,
                 K is the predetermined number.


Im jeweiligen selbstständigen Anspruch 5 der Hilfsanträge 1, 1a und 2 sind die
Merkmale ebenfalls entsprechend dem jeweiligen Anspruch 1 geändert.


Die Beklagte tritt den Ausführungen der Klägerinnen in allen wesentlichen Punkten
entgegen und erachtet das Streitpatent, zumindest in einer der Fassungen der vier
Hilfsanträge vom 25. April 2022, vom 28. Juni 2022 sowie vom 30. Juni 2022 für
patentfähig.


Die   Beklagte        stützt   ihr   Vorbringen       u. a.   auf   folgende   Dokumente:

                                        - 16 -



DFMP 2       Gutachten des Herrn Univ.-Prov. Dr.-Ing. habil. J…, Inhaber
             des Lehrstuhls für Kommunikationstechnik der Universität D…-
             E… vom 24. Oktober 2019 zum Streitpatent
DFMP 3       Notice of Recordation of Assignment Document des USTPO,
             9. September 2008, Nr. 021498/0293
DPMP 4       Notice of Recordation of Assignment Document des USTPO,
             9. September 2008, Nr. 021498/0287
DPMP 5       Übersicht zur Erläuterung der Behauptung der Klägerin 1, dass die
             anspruchsgemäße Formel aus der Offenbarung der QE D3
             mathematisch ableitbar sei
DPMP 6       Übersicht zur Erläuterung der Behauptung der Klägerin 1, dass die
             anspruchsgemäße Formel aus der Offenbarung der QE D5
             mathematisch ableitbar sei


Die Beklagte ist der Auffassung, das Streitpatent nehme die von ihm beanspruchten
Prioritäten wirksam in Anspruch. Auch nehme keines der genannten Dokumente die
Gegenstände der unabhängigen Patentansprüche 1, 5 und 7 neuheitsschädlich
vorweg. Diese beruhten auch auf einer erfinderischen Tätigkeit. Zumindest erweise
sich das Streitpatent aber in einer der Fassungen der Hilfsanträge 1, 1 a, 1b und 2
vom 25. April 2022, vom 28. Juni 2022 sowie vom 30. Juni 2022 als patentfähig.


Die Klägerinnen zu 2) und zu 3) erachten das Streitpatent auch in den Fassungen
der Hilfsanträge 1, 1a und 2 vom 25. April 2022 bzw. vom 28. Juni 2022 für nicht
patentfähig. Das in Anspruch 1 bzw. 5 des Hilfsantrags 1 neu hinzugenommene
Merkmal schränke den Anspruch jeweils nicht ein. Der Hilfsantrag 2 erweitere den
Schutzbereich des Streitpatents in unzulässiger Weise. Im Übrigen seien die
Gegenstände des Streitpatents auch in den Fassungen der drei Hilfsanträge nicht
neu bzw. beruhten zumindest nicht auf einer erfinderischen Tätigkeit. Das
Streitpatent erweise sich auch nicht in der Fassung nach Hilfsantrag 1b als
patentfähig. Die Klägerin zu 3) rügt diesen Hilfsantrag als verspätet.

                                          - 17 -



Der Senat hat den Parteien am 11. Februar 2022 einen gerichtlichen Hinweis gem.
§ 83 PatG sowie in der mündlichen Verhandlung am 30. Juni 2022 einen weiteren
rechtlichen Hinweis erteilt.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                              Entscheidungsgründe


Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6   Abs.   1 Satz    1   Nr.   1 IntPatÜbkG   i. V. m.   Art.   138   Abs.   1
lit. a) EPÜ i. V. m. Art. 54, 56 EPÜ geltend gemacht wird, ist zulässig.


Die Klage ist auch begründet. Das Streitpatent hat weder hinsichtlich des
Hauptantrags noch hinsichtlich der Hilfsanträge Bestand, denn dem Streitpatent
gemäß Hauptantrag und Hilfsanträgen 1, 1a und 1b steht der Nichtigkeitsgrund der
fehlenden Patentfähigkeit, und dem Streitpatent gemäß dem Hilfsantrag 2 der
Nichtigkeitsgrund der unzulässigen Erweiterung des Schutzbereichs entgegen.




                                            I.


Der in der mündlichen Verhandlung am 30. Juni 2022 eingereichte Hilfsantrag 1b
war trotz Rüge der Klägerin zu 3) nach § 83 Abs. 4 Satz 1 PatG nicht als verspätet
zurückzuweisen.


Damit ist über die Verteidigung des Streitpatents nach dem Hilfsantrag 1b in der
Sache zu entscheiden.


Gemäß § 83 Abs. 4 Satz 1 PatG kann das Patentgericht zwar eine Verteidigung des
Beklagten mit einer geänderten Fassung des Patents zurückweisen und bei seiner
Entscheidung unberücksichtigt lassen.

                                             - 18 -



Hierfür ist es aber stets erforderlich, dass dieser Vortrag tatsächliche oder rechtliche
Fragen aufkommen lässt, die in der mündlichen Verhandlung nicht oder nur mit
unverhältnismäßigem Aufwand zu klären sind (vgl. Begründung zum Entwurf eines
Gesetzes zur Vereinfachung und Modernisierung des Patentrechts, BlPMZ 2009,
307, 315). Kann das an sich verspätete Vorbringen dagegen noch ohne Weiteres in
die mündliche Verhandlung einbezogen werden, ohne dass es zu einer
Verfahrensverzögerung kommt, liegen die Voraussetzungen für eine Zurückweisung
nach § 83 Abs. 4 PatG nicht vor. So liegt der Fall hier, weil die Berücksichtigung des
Hilfsantrags 1b zu keiner Verzögerung des Rechtsstreits geführt hat. Hinzu tritt, dass
nach der Rechtsprechung des Senats die Voraussetzungen für eine Zurückweisung
dann   nicht   vorliegen,      wenn    die    geänderte       Anspruchsfassung   nicht   zur
Bestandsfähigkeit        des          Patents         führt      (vgl.    Keukenschrijver,
Patentnichtigkeitsverfahren, 7. Aufl. 2021, Rn. 223 mit umfangreichen Nachweisen
zur Rechtsprechung des BPatG, zum letztgenannten Aspekt in Fn. 127).




                                              II.


1. Das Streitpatent betrifft die drahtlose Telekommunikation, insbesondere die
Ressourcenzuweisung in der drahtlosen Telekommunikation (vgl. Abs. [0001] der
Streitpatentschrift (NK 4)).


In UMTS-Funknetzen kann ein Benutzergerät (UE) mehrere gleichzeitig laufende
Anwendungen unterschiedlicher Dienstqualitäten unterstützen. In der MAC-Schicht
können mehrere logische Kanäle zu einem einzigen Transportkanal gemultiplext
werden. Der Transportkanal kann dabei definieren, wie der Verkehr von logischen
Kanälen verarbeitet und an die physikalische Schicht gesendet wird. Die
grundlegende Dateneinheit, die zwischen MAC und Bitübertragungsschicht
ausgetauscht wird, wird als Transportblock (TB) bezeichnet. Es besteht aus einer
RLC-PDU und einem MAC-Header. Während eines als Übertragungszeitintervall
(TTI) bezeichneten Zeitraums werden mehrere Transportblöcke und einige andere
Parameter an die physikalische Schicht geliefert (vgl. Abs. [0009]).

                                      - 19 -



Um den UMTS-Mobilfunkstandard zu verbessern und beispielsweise eine effiziente
Übertragung von IP-Daten zu ermöglichen, wird der LTE-Standard (E-UTRAN)
entwickelt (vgl. Abs. [0006]). Im LTE können Steuer- und Nutzdaten im Uplink von
der Mobil- zur Basisstation gemeinsam auf einem physikalischen Kanal PUSCH
(Physical Uplink Shared Channel) gemultiplext übertragen werden (vgl. Abs. [0014]
- [0016]).


Aus dem Stand der Technik (R1-073842) ist beispielsweise bekannt, für die
Steuersignalisierung auf dem PUSCH verschiedene Annahmen vorzusehen. So
wird die für die Steuersignalisierung zu verwendende Codierrate vom PUSCH MCS
(Modulations- und Codierschema) vorgegeben. Diese Beziehung wird in einer
Tabelle ausgedrückt, in der jedes PUSCH MCS mit einer gegebenen Codierrate für
die Steuersignalisierung, d.h. der Anzahl der Symbole, die für ein ACK/NAK oder
eine bestimmte CQI/PMI-Größe zu verwenden sind, verknüpft ist. Steuerdaten wie
CQI/PMI verwenden auf dem PUSCH das gleiche Modulationsschema wie
Nutzdaten auf dem PUSCH. Zwischen dem Daten-MCS und der Codierrate der
Steuersignalisierung wird ein semistatisch konfigurierter Offset angewendet (A/N
und CQI) (vgl. Abs. [0014]).


Die bisherige Entwicklung befasste sich jedoch nicht damit, wie das PUSCH MCS
und die Ressourcenmenge für die Steuerdaten auf dem PUSCH verknüpft werden,
oder wie eine ausreichende Qualität für Uplink-(UL)-Steuersignale garantiert
werden kann, wenn sie mit UL-Daten gemultiplext werden. Bei der Zuweisung von
Ressourcen für Steuersignale muss beispielsweise berücksichtigt werden, dass
aufgrund von Verzögerungsanforderungen eine Wiederholungsübertragung von
Steuersignalen nicht möglich ist und der Steuerkanal nur eine relativ kleine
Codeblockgröße und einen kleineren Codierungsgewinn hat (vgl. Abs. [0016]).


Aus dem Stand der Technik (R1-081295; QE D 3) ist zwar eine Formel bekannt, um
die Größe der Steuerregion basierend auf dem Daten-MCS-Niveau zu bestimmen,
jedoch weist diese mehrere Nachteile auf (vgl. Abs. [0017]).

                                         - 20 -



1.1 Vor diesem Hintergrund liegt dem Streitpatent als technisches Problem gemäß
der Angabe in der Patentschrift die Aufgabe zugrunde, eine ausreichende Qualität
für UL-Steuersignale zu gewährleisten, wenn sie mit UL-Daten gemultiplext werden
(vgl. Abs. [0018] der Streitpatentschrift).


1.2 Gelöst wird diese Aufgabe durch das Verfahren des erteilten Anspruchs 1, die
Vorrichtung des erteilten Anspruchs 5 und das Computerprogrammprodukt des
erteilten Anspruchs 7, sowie durch die Gegenstände und Verfahren der
selbstständigen Ansprüche der Hilfsanträge.




2. Als hier zuständiger Fachmann ist ein Ingenieur der Fachrichtung
Nachrichtentechnik mit Universitätsabschluss zu definieren, der über eine
mehrjährige Erfahrung in der Entwicklung drahtloser Telekommunikationssysteme
verfügt.




3. Die Anspruchsmerkmale bedürfen der Auslegung.




Das Streitpatent (NK 4) zeigt in seiner hier wiedergegebenen Figur 3 Eingabe- und
Ausgabeparameter des vorgeschlagenen Ressourcenzuweisungsschemas (vgl.
Streitpatent, Seite 4, Zeile 28 und Figur 3). Das Verfahren gemäß Anspruch 1 dient
zum Verbinden eines Modulations- und Codierungsschemas (MCS) mit einer
Menge von Betriebsmitteln (Merkmal 1). Bei der Menge von Betriebsmitteln bzw.
dem Umfang der benötigten Ressourcen handelt es sich um die Anzahl von
Steuersymbolen pro Übertragungszeitintervall (TTI) (vgl. Merkmal 1.3, sowie

                                       - 21 -



Abs. [0025] und Figuren 3, 5 und 7). Es wird somit eine Verbindung zwischen einem
MCS und einer Anzahl von Steuersymbolen pro TTI hergestellt. Das Verfahren
umfasst ein Bereitstellen von mehreren statischen Eingabeparametern (Merkmal
1.1), bei denen es sich beispielsweise um die Codierungsrate (CR) des gegebenen
MCS des PUSCH-UL-Datenkanals (z. B. 3/1) und MMod, die Anzahl uncodierter
Bits/Symbol [2, 4 oder 6 mit QPSK, 16QAM, 64QAM] für das gegebene UL-Daten
MCS, handelt. Die Anzahl Bits/Symbol versteht der Fachmann als die Übertragung
des     Modulationsverfahrens        bzw.       die        Modulationsordnung          des
Modulationsverfahrens und die Anzahl uncodierte Bits als die Anzahl an Bits, die
mit einem Symbol codiert werden. Überdies werden mehrere - beispielsweise von
höheren Schichten - signalisierte Eingabeparameter bereitgestellt (Merkmal 1.2),
bei denen es sich beispielsweise um den Qualitätsunterschied (offset_dB) zwischen
dem gegebenen die Steuersignalisierungsbits führenden Steuerkanal und dem
PUSCH-Datenkanal      und    beispielweise      um     die       Anzahl    (N)   von   mit
Aufwärtsstreckendaten       auf       dem           gemeinsamen            physikalischen
Aufwärtsstreckenkanal, PUSCH, übertragenen Steuersignalisierungsbits (für den
gegebenen Steuersignalisierungstyp) handelt (vgl. Abs. [0025], Figur 3 und
Merkmal    1.3.3).   Aus    diesen   mehreren         statischen     und     signalisierten
Eingabeparametern wird ein Ausgabeparameter bestimmt, der, wie bereits
dargelegt, eine Anzahl von Steuersymbolen pro Übertragungszeitintervall für eine
Menge von Steuersignalisierungsbits angibt (Merkmal 1.3), wobei sich der
Ausgabeparameter auf ein physikalisches Betriebsmittel, also Ressourcen der
physikalischen Schicht, mit einem gegebenen MCS für eine Aufwärtsstrecke bezieht
(Merkmal 1.3.1). Die Merkmale 1.3.2 und 1.3.3 definieren, dass das Bestimmen
                                                       ⋅
des Ausgabeparameters Mctrl gemäß               =            _     erfolgt. Zunächst wird

dafür ein Produkt gebildet, indem die Anzahl von Steuersignalisierungsbits (N) mit
der Codierrate (CR) multipliziert und durch die Anzahl uncodierter Bits pro Symbol
(MMod) dividiert wird. Anschließend wird dieses Produkt durch einen Korrekturfaktor
dividiert. Der Korrekturfaktor berechnet sich, indem der Versatzparameter
(offset_dB) durch 10 dividiert und das Ergebnis als negativer Exponent zur Basis 10

                                       - 22 -



verwendet wird. Abschließend wird ein Aufrunden des ermittelten Quotienten auf
die nächsthöhere ganze Zahl (⌈ ⌉) vorgenommen.


Somit wird die Anzahl der Steuersymbole pro Übertragungszeitintervall (Mctrl) für die
zu übertragenden Steuerinformationen (N) in Abhängigkeit der Codierrate (CR) und
der Modulationsordnung (MMod) für die auf dem PUSCH-UL-Datenkanal zu
übertragenden Nutzdaten bestimmt. Dies erfolgt, indem die zu übertragenden
Steuersignalisierungsbits mit der Codierrate für die PUSCH-Nutzdaten multipliziert
werden und dann durch die gemäß MCS für die Nutzdaten vorhandene
Modulationsordnung (Anzahl an Bits pro Symbol) dividiert werden. Somit wird das
bereits für die Nutzdaten vorhandene MCS weiterverwendet. Durch den
zusätzlichen Versatzparameter (offset_dB) wird der Qualitätsunterschied zwischen
dem Steuerkanal und dem PUSCH-Datenkanal, z.B. in dB (vgl. Abs. [0060]),
berücksichtigt. Zur Bestimmung nur ganzzahliger Steuersymbolanzahlen wird der
Quotient auf die nächsthöhere ganze Zahl aufgerundet.


Zu beachten ist, dass die Codierrate (CR) im Streitpatent nicht als Verhältnis von
Eingangs- zu Ausgangsbits, z.B. 1/3, definiert ist, sondern umgekehrt. So ist der
Tabelle 2 auf der Seite 10 des Streitpatents in Zeile 15 für QPSK 1/3 eine Codierrate
von 3.0 zu entnehmen.


Die Beklagte argumentiert, dass der Parameter offset_dB einen Gewichtungsfaktor
darstelle, durch den ein Versatz zwischen den zulässigen Blockfehlerraten (BLER)
des PUSCH-Datenkanals und des Steuerkanals vorgegeben werden könne. Er
werde in doppelter Funktion auch zur Anpassung der Anzahl Mctrl von Symbolen pro
Übertragungszeitintervall verwendet. Der Parameter offset_dB werde vom
Qualitätsunterschied zwischen dem Steuer- und dem Datenkanal bestimmt und als
Gewichtungsfaktor im Rahmen der Modulation der codierten Steuersignalisierungsbits N zur Anpassung der Anzahl von Steuersymbolen pro Übertragungszeitintervall
Mctrl verwendet.

                                       - 23 -



Diese Argumentation kann nicht überzeugen. Zwar ist dem Streitpatent ein
Ausführungsbeispiel zu entnehmen, in dem die Blockfehlerquote BLER des UL-Datenkanals und die BLER des Steuerkanals jeweils auf einen bestimmten Wert
(z.B. 40% und 10%) beschränkt werden und ein offset_dB-Wert gefunden wird, der
diese Qualitätskriterien erfüllt (vgl. Streitpatent, Abs. [0035]). Jedoch haben diese
Verfahrensschritte, insbesondere die Bestimmung aus vorgegebenen Ziel-Blockfehlerquoten, keinen Eingang in den erteilten Anspruch 1 gefunden. Das
Merkmal 1.3.3 fordert lediglich einen multiplikativen Offset-Parameter, der der
Qualitätsunterschied zwischen einem gegebenen die Steuersignalisierungsbits
führenden Steuerkanal und dem PUSCH-Datenkanal ist. Dabei ist für den
Fachmann selbstverständlich, dass in der Formel ein größerer multiplikativer Offset-Parameter (offset_dB) zu einer größeren Steuerregion (Mctrl), einer geringeren
Steuerdaten-Fehlerrate und zu einer höheren Qualität der Steuerdaten führt und in
diesem Fall ein größerer Qualitätsunterschied zwischen Steuer- und Nutzdaten,
bzw. zwischen Steuer- und PUSCH-Datenkanal, vorhanden ist. Da somit der Offset-Parameter (offset_dB) einen bestimmten Qualitätsunterschied zwischen Steuerund Nutzdatenkanal erzeugt, ist dieser Parameter auch der Qualitätsunterschied.


Ferner gibt der Anspruch 1 des Streitpatents nicht an, dass der Parameter
„offset_dB“ signalisiert wird. Es kann auch der gesamte Nenner, also ein Teiler, der
gleichbedeutend mit einem zum Teiler inversen Faktor ist, signalisiert werden. Auch
bedeutet das englische Wort „according to“ in der deutschen Übersetzung
„entsprechend“, so dass eine Berechnung einer anderen entspricht, wenn
Ausdrücke zusammengefasst oder auch in einzelne Operationen aufgeteilt werden.


Der unabhängige Anspruch 5 ist auf eine Vorrichtung mit einem Prozessor gerichtet,
der den Algorithmus umsetzt und den Ausgabeparameter bestimmt.


Der unabhängige Anspruch 7 ist auf ein Computerprogrammprodukt mit einem
Code gerichtet, um das Verfahren nach Anspruch 1 auszuführen.

                                        - 24 -



Das Merkmal 1.3.4 des Hilfsantrags 1 gibt an, dass der Offset-Parameter separat
für verschiedene PUSCH-Bandbreiten oder für verschiedene Modulations- und
Codierschemata oder für verschiedene Diensttypen oder für verschiedene
Steuerkanäle definiert wird. Dabei versteht das Streitpatent beispielsweise unter
verschiedenen MCS QPSK, 16QAM, oder 64QAM, unter verschiedenen
Diensttypen verzögerungskritische Dienste oder verzögerungsunkritische Daten,
und unter verschiedenen Steuerkanälen ACK/NACK oder CQI (vgl. NK4, Abs.
[0031], [0032]). Das Merkmal 1.3.4 schränkt den Offset-Parameter somit derart ein,
dass dieser nicht mehr beliebig definiert wird, sondern explizit separat entweder für
verschiedene PUSCH-Bandbreiten oder für verschiedene Modulations- und
Codierschemata oder für verschiedene Diensttypen oder für verschiedene
Steuerkanäle. Dabei kann der Offset-Parameter für verschiedene Fälle auch den
gleichen Wert besitzen, sofern er für jeden Fall separat definiert wird (vgl. Abs.
[0031] und [0032] der Streitpatentschrift).


Im Merkmal 1.3.4‘ des Hilfsantrags 1a ist gegenüber dem Merkmal 1.3.4 des
Hilfsantrags   1   die    Alternative   für   unterschiedliche       Modulations-   und
Codierschemata gestrichen.


Im Merkmal 1.3.2‘ des Hilfsantrags 2 wird gegenüber Merkmal 1.3.2 ergänzt, dass
das Ergebnis der Aufrundungsoperation als Ausgabeparameter gewählt wird, wenn
das Ergebnis der Aufrundungsoperation der Maximalwert von einer Gruppe ist, die
aus dem Ergebnis der Aufrundungsoperation und einer vorbestimmten Zahl besteht.
Gemäß Merkmal 1.3.3‘ des Hilfsantrags 2 erfolgt die Berechnung des
                                                                 ⋅
Ausgabeparameters Mctrl anhand der Formel           = max(             _   , ), wobei K

eine vorbestimmte Zahl ist.


Die Beklagte argumentiert, dass nach Hilfsantrag 2 der Ausgabeparameter Mctrl nur
noch bestimmt würde, wenn das Ergebnis der Aufrundungsoperation größer als die
vorbestimmte Zahl sei.

                                        - 25 -



Diese Argumentation kann nicht überzeugen, da sich zum einen die Ergänzung im
Merkmal 1.3.2‘ nicht darauf bezieht, in welchem Fall der Ausgabeparameter nur
noch bestimmt werden soll, sondern lediglich auf die Frage, welcher Wert als
Ausgabeparameter      verwendet    werden      soll, wenn    bei   der gemeinsamen
Betrachtung der Zahl K und des Ergebnisses der Aufrundungsfunktion dessen
Ergebnis größer als K ist. Dabei legt das Merkmal 1.3.2‘ lediglich fest, dass, wenn
das Ergebnis der Aufrundungsfunktion größer als K ist, dieses Ergebnis als
Ausgabeparameter verwendet werden soll. Für den anderen Fall, wenn das
Ergebnis der Aufrundungsfunktion kleiner als K ist, trifft es keine Aussage. Zum
anderen gibt das Merkmal 1.3.3‘ darüber hinaus dem Fachmann eine explizite
Rechenvorschrift an, wie der Ausgabeparameter Mctrl für alle Fälle zu bestimmen
ist; nämlich als Zahl K für den Fall, dass das Ergebnis der Aufrundungsfunktion
kleiner als K ist. Auch dem Streitpatent entnimmt der Fachmann, dass der
Parameter K gerade dazu dient, immer eine Mindestzahl an reservierten Symbolen
zu garantieren, mithin für die Fälle, in denen die Aufrundungsfunktion ein zu
geringes Ergebnis liefert, sicherzustellen, dass immer mindestens K Symbole zur
Übertragung der Steuerbits mit ausreichender Qualität zur Verfügung stehen (vgl.
NK4, Abs. [0029]: „One way to improve DTX detection is to define the control
signaling size such that a certain number of ACK/NACK symbols are always
reserved“, “K is a predetermined number, e.g., 8-10”, „ The procedure is such that
in the case when ACK/NACK is present, then the number of A/N (i.e. ACK/NACK)
symbols is calculated based e.g., on the equation above. In the case when
ACK/NACK is absent, then K symbols are still reserved.“). Dabei ist K eine
vorbestimmte Zahl, die beispielsweise zwischen 8 und 10 liegt. Das bedeutet, dass
die Bestimmung von Mctrl immer zu beispielsweise 10 führt, solange die Formel in
der Aufrundungsfunktion zu einem kleineren Wert als 10 führt. Die Bestimmung von
Mctrl mittels der Aufrundungsfunktion erfolgt in diesem Beispiel somit erst ab einem
Wert von 10. Somit ergeben sich zwei Alternativen, entweder Alternative A) Mctrl =
                                                    ⋅
10 oder Alternative B) Mctrl > 10. Solange   >          _   ist der Ausgabeparameter

                                   ⋅
Mctrl = K anstelle von       =          _    . Somit wird die Gleichung für Mctrl stets

                                        - 26 -



berechnet. Würde der Ausgabeparameter Mctrl erst ab einem bestimmten Wert der
Aufrundungsfunktion überhaupt bestimmt werden, würde nicht nur die explizite
Berechnungsvorschrift des Merkmals 1.3.3‘, sondern auch das im Streitpatent
angegebene Ziel des Parameters K, stets eine Mindestzahl an Symbolen als
Ausgabeparameter Mctrl zu garantieren (vgl. NK4, Abs. [0029]), übergangen. Für die
Auslegung der Beklagten war somit kein Raum.




4. Die Verfahren der Ansprüche 1 nach Hauptantrag und nach den Hilfsanträgen 1,
1a und 1b sind nicht patentfähig, da sie dem Fachmann durch Druckschrift QE D 2
i.V.m. seinem Fachwissen, belegt durch die Anlage 1 der NK 2, QE D 3 und QE D
10 nahegelegt werden (Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG, Art. 138 Abs. 1
lit. a) EPÜ i. V. m. Art. 52 Abs. 1, 56 EPÜ).


Bei dieser Sachlage kann neben der Zulässigkeit dieser Anspruchssätze und der
wirksamen Inanspruchnahme der Priorität auch dahingestellt bleiben, ob die
Merkmale 1.3.2 und 1.3.3 bei der Prüfung auf erfinderische Tätigkeit nicht zu
berücksichtigen sind.


Die Verteidigung des Streitpatents mit dem Hilfsantrag 2 führt wegen Erweiterung
des Schutzbereichs nicht zum Erfolg (Art. II § 6 Abs. 1 Satz 1 Nr. 4 IntPatÜbkG, Art.
138 Abs. 1 lit. d) EPÜ).


4.1 Zum Hauptantrag


Das Dokument QE D 2 ist ein Diskussionsbeitrag der Freescale Semiconductor mit
dem Titel „Control Region on the PUSCH“ für ein Treffen der Arbeitsgruppe 1 (WG1)
der 3GPP Technische Spezifikationsgruppe (3GPP TSG) vom 31. März bis 4. April
2008 in S…, China. Das Dokument wurde am 26. März 2008 auf den ftp-Server der 3GPP hochgeladen und damit vor dem Prioritätstag der Öffentlichkeit
zugänglich gemacht (vgl. Klageschrift der Klägerin zu 1, S. 24; Klageschrift der
Klägerin zu 3), S. 31). Das Dokument betrifft die Modulation der Steuerregion, die

                                       - 27 -



Größe und die MCS-Offsetkonfiguration (vgl. Kap. 1). Nach Festlegung auf das
BPSK-Modulationsschema (bei dem dem Fachmann bekannt ist, dass pro Symbol
ein Bit übertragen wird) für ACK/NACK sei fraglich, wie viele Wiederholungen für die
1- und 2-Bit großen Nachrichten erforderlich sind. Die Autoren schlagen vor, die
Anzahl der Wiederholungen für das ACK/NACK aus dem Quotienten einer
Konstante k1 und dem MCS-Pegel der Modulation SEdata bzw. der spektralen
Effizienz des Datenbereichs zu bestimmen. Die Größe des ACK/NACK-Steuerbereichs bestimmt sich dann durch die folgende Formel (vgl. Kap. 2.1):
                              /     = 1∗            /   /
Des Weiteren wird eine entsprechende Formel für die Berechnung der Größe der
Steuerregion für CQI offenbart:
                                    = 2∗        /
Es sei darüber hinaus allgemein bekannt, dass Nutz- und Steuerdaten auf PUSCH
unterschiedliche MCS-Level haben sollten. Bezüglich der MCS-Offset-Konfiguration
ist die Meinung der Autoren, dass die Modulation zwischen Nutz- und Steuerdaten
nicht identisch sein müsse, um einen geeigneten MCS-Offset zwischen Nutz- und
Steuerdaten aufrechtzuerhalten, die nicht von HARQ profitieren. Wenn die
Konstanten k1 und k2 halbstatisch konfiguriert und eine Funktion von SEdata seien,
müsse die Modulation nicht gleich sein (vgl. Kap. 2.2).


4.1.1 Für den Fachmann ist es selbstverständlich, dass das in der QE D 2 genannte
Modulations- und Codierschema (vgl. QE D 2: „MCS“) ein Modulationsschema
„Anzahl an Bits pro Symbol“ (vgl. QE D 10, S. 17: „Qm is equal to 2 for QPSK, 4 for
16QAM and 6 for 64QAM“; S. 23, Tabelle 5.2.2-1) und ein Codierschema
„Codierrate“ (vgl. QE D 10, S. 22, kap. 5.2.2.6: „coding rate“) beinhaltet. Dabei ist
dem Fachmann aus seinem Fachwissen bekannt, dass sich die spektrale Effizienz
SE als Produkt aus der Codierrate (Rc) und der Anzahl an Bits pro Symbol (b) ergibt
(vgl. Anlage NK 2, Seite 24; sowie S. Le Goff, A. Glavieux, C. Berrou: Turbo-codes
and high spectral efficiency modulation. IEEE International Conference on Communications (ICC), 1994, S. 646, linke Spalte (Anlage 1 zur Anlage NK 2)):
                                         =      ∗

                                          - 28 -



Der Einsatz der durch das Modulations- und Codierschema bereitgestellten
Parameter in der QE D 2 führt den Fachmann somit zu der folgenden Gleichung mit
der Codierrate (Rc; z.B. 1/3) und der Anzahl an Bits pro Symbol bzw.
Modulationsordnung (b; z.B. 2, 4, 6) für die Größe des ACK/NACK-Steuerbereichs:
                                                                1
                              /       =         /       ∗          ∗ 1
                                                                 ∗
Im von der Beklagten vorgelegten Gutachten (DFMP 2, S. 77) wird zwar
argumentiert, dass von der Klägerin für deren Ansicht kein Lehrbuch bzw.
wissenschaftliche Quelle vorgelegt wurde und ein falscher Begriff der spektralen
Effizienz zugrunde gelegt werde, der auf der Annahme basiere, dass es einen
isolierten Sender und einen isolierten Empfänger gebe. Diese Argumentation kann
jedoch nicht überzeugen, da es sich bei dem von der Klägerin zu 1 als Anlage 1 zur
NK 2 vorgelegten Dokument um eine wissenschaftliche Veröffentlichung im
Rahmen einer IEEE-Konferenz, mithin um eine wissenschaftliche Quelle handelt,
die die spektrale Effizienz einer Datenverbindung betrachtet. Da auch die QE D 2
die Größe der Steuerregion einer Datenverbindung („size of the ACK/NACK control
region“) betrachtet, setzt der Fachmann sein durch die Anlage 1 zur NK 2 belegtes
Fachwissen bei der Implementierung der Lösung der QE D 2 auch ein. Da der
Fachmann ausgehend von der QE D 2 eine einzelne Datenverbindung betrachtet,
ist für ihn zugleich unerheblich, ob sich die spektrale Effizienz eines Clusters bzw.
die Cluster-Spektral-Effizienz durch Division durch die Anzahl der Zellen des
Clusters ergibt (Merkmal 1.1).


4.1.2 Dabei ist zu beachten, dass die Codierrate RC in der Anlage 1 der NK 2 als
Verhältnis von Eingangs- zu Ausgangsbits, z.B. 1/3 definiert wird, wohingegen im
Streitpatent die Codierrate CR invers definiert wird (vgl. NK 4, Abs. [0025]: „coding
rate (CR) of given MCS of UL data channel (e.g., 3/1)“, sowie NK 4, Seite 10, Zeile
15: „Data MCS: QPSK 1/3“, „CR: 3.0“). Daraus folgt:
                                                    1
                                            =


                                  /   =             /       ∗    ∗ 1

                                          - 29 -




4.1.3 Da die Anzahl an Steuersymbolen für den PUSCH (z.B. SizeACK/NACK) nur in
ganzen Zahlen vorgegeben und verarbeitet werden kann, wird der Fachmann das
Ergebnis der Berechnung auf- oder abrunden.


Die Beklagte argumentiert, dass der Fachmann zahlreiche andere Möglichkeiten
hätte, um von einer realen Zahl auf eine Ganzzahl zu kommen. Jedenfalls sei in
Anbetracht der zahlreichen alternativen Funktionen kein Grund zu glauben, dass
der Fachmann den oberen Gaußklammer mitlese.


Diese Argumentation kann nicht überzeugen, da es sich für den um eine möglichst
hohe Qualität bemühten Fachmann anbietet, auf- statt abzurunden, um ein
zusätzliches Symbol zur Verfügung zu stellen. Auch dem Dokument QE D 3
entnimmt der Fachmann den Hinweis auf ein Aufrunden der gesamten Formel, so
dass dem Fachmann aus der QE D 2 die folgende Gleichung nahegelegt ist
(Merkmal 1.3.3):

                              /       =        /        ∗       ∗ 1


4.1.4 Darüber hinaus ist dem Fachmann aus seinem Fachwissen bekannt, dass die
Angabe eines Faktors über den eigentlichen Faktor „k1“ oder seine logarithmische
                                                            _
Darstellung in dB „k1_dB“ inhaltsgleich ist: 1 = 10             =     _


Verwendet der Fachmann in der QE D 2 die in der Nachrichtentechnik zur
Verwendung handlicher Zahlenwerte übliche Angabe in Dezibel, ergibt sich für den
Fachmann die folgende inhaltsgleiche Formel zur Berechnung der Größe des
ACK/NACK-Steuerbereichs aus der QE D 2 (Merkmale 1., 1.3 bis 1.3.3):

                                                    /       ∗
                                  /       =             _
                                                   10

                                       - 30 -



4.1.5 Des Weiteren wird im Kapitel 2.2 der QE D 2 angegeben, dass die Modulation
zwischen Nutz- und Steuerdaten nicht identisch sein müsse, um einen geeigneten
MCS-Offset zwischen diesen zu unterstützen. Wenn die Konstanten k1 und k2
halbstatisch konfiguriert und eine Funktion von SEdata seien, müsse die Modulation
nicht gleich sein (vgl. Kap. 2.2: „Regarding the MCS offset configuration, it is our
opinion that the modulation need not be identical between data and control in order
to maintain an appropriate MCS offset between data and control which does not
benefit from HARQ. If the constants, k1 and k2, are configured on a semi-static basis
and are a function of SEdata, there is no need for the modulation to be the same.“).
Damit dienen die Konstanten k1 und k2 der Unterstützung eines geeigneten Offsets
zwischen Nutz- und Steuerdaten, wobei der Fachmann einen größeren Offset als
eine größere Steuerregion, eine geringere Steuerdaten-Fehlerrate und damit eine
höhere Qualität der Steuerdaten und einen größeren Qualitätsunterschied zwischen
Steuer- und Nutzdaten versteht. Die Parameter k1 und k2 sind somit jeweils ein
Parameter      für    den      Qualitätsunterschied     zwischen       einem     die
Steuersignalisierungsbits führenden Steuerkanal und dem PUSCH-Datenkanal
(Merkmal 1.3.3).


4.1.6 Die Beklagte führt aus, dass sich aus der QE D2 keine Lehre bezüglich der
Signalisierung von k1 / k2 ergebe und folglich nicht offenbart sei, dass k1 und k2
signalisierte Eingabeparameter seien. Bezüglich der Bereitstellung von NACK/NACK
schweige QE D2 vollkommen, so dass QE D2 nicht offenbare, dass NACK/NACK ein
signalisierter Eingabeparameter sei.


Dieser Argumentation ist nicht zu folgen, da der QE D 2 zu entnehmen ist, dass die
Konstanten k1 und k2 semi-statisch konfiguriert sein können (vgl. QE D 2, Kap. 2.2:
„If the constants, k1 and k2, are configured on a semi-static basis“). Dem Fachmann
ist aus seinem Fachwissen bekannt, dass semi-statische Parameter von höheren
Schichten signalisiert werden (vgl. QE D 11, S. 17: „In Table 7.2.1-2 the k values
and M1 values are semi-statically configured by higher layers as a function of
system bandwidth.“). Zudem versteht der Fachmann die Variablen NACK/NACK und
NCQI als die Anzahl der ACK/NACK- und CQI-Bits, die selbstverständlich, um eine

                                        - 31 -



Berechnung aus aktuellen Werten überhaupt zu ermöglichen, signalisiert werden
(Merkmal 1.2).


4.1.7 Dass sich das Dokument QE D 2 auf eine Aufwärtsstrecke bezieht, ist für den
Fachmann bei einer Ressourcenberechnung für den PUSCH mit Bezug zu Nutzund Steuerdaten naheliegend (Merkmale 1.3.1, 1.3.3).


4.1.8 Die Beklagte argumentiert, dass der Parameter Mctrl aus dem Parameter
SizeACK/NACK nicht nahegelegt sei, da SizeACK/NACK allenfalls die Anzahl von codierten
Steuersignalisierungsbits bezeichne, jedoch nicht die Anzahl von Steuersymbolen,
insbesondere keine Anzahl von Steuersymbolen pro Übertragungszeitintervall.
Ferner erwähne QE D 2 zwar den PUSCH, lehre den Fachmann aber nicht,
innerhalb wie vieler Übertragungszeitintervalle die von QE D 2 bestimmte Anzahl
von   Steuersignalisierungsbits    SizeACK/NACK   für   eine   ACK/NACK-Nachricht
signalisiert werden solle.


Auch diese Argumentation kann nicht überzeugen. Dem Fachmann ist, wie bereits
ausgeführt, aus seinem Fachwissen bekannt, dass sich die spektrale Effizienz SE
als Produkt aus der Codierrate (Rc) und der Anzahl an Bits pro Symbol (b) ergibt
(vgl. Anlage 1 zur NK 2, Seite 646, linke Spalte). Zudem offenbart die QE D 2, dass
die Konstanten k1 und k2 auf semistatischer Basis konfiguriert werden, um einen
MCS Offset zu erhalten (vgl. QE D 2, Kap. 2.2). Sowohl aus der Betrachtung der
Einheiten (N [Bits] / b [Bits/Symbol]), als auch aus dem expliziten Hinweis auf das
MCS (Modulations- und Codierschema) in der QE D 2 ergibt sich, dass es sich bei
den Variablen SizeACK/NACK und SizeCQI um eine Anzahl Symbole und nicht um eine
Anzahl zwar codierter aber noch nicht modulierter Steuersignalisierungsbits
handelt. Darüber hinaus wird die Anzahl der Symbole fachüblich pro TTI
angegeben.


4.1.9 Weiter argumentiert die Beklagte, dass der Parameter offset_dB aus dem
Parameter k1 nicht nahegelegt sei, da der Parameter k1 zur Berechnung der Anzahl
Rep, mit der die ACK/NACK-Nachrichten wiederholt werden sollen, diene. Die QE

                                      - 32 -



D 2 lehre, dass k1 ausschließlich in Abhängigkeit von der Qualität des Datenkanals
und nicht von einem Qualitätsunterschied zwischen dem Datenkanal und dem
Steuerkanal bestimmt werde.


Auch diese Argumentation kann nicht überzeugen, da, wie bereits ausgeführt, auch
die Konstanten k1 und k2 der Unterstützung eines geeigneten Offsets zwischen
Nutz- und Steuerdaten dienen, wobei der Fachmann ein größeres k1 als eine
größere Steuerregion SizeACK/NACK und einen größeren Qualitätsunterschied
zwischen Steuer- und Nutzdaten versteht. Dem Fachmann ist darüber hinaus aus
seinem Fachwissen bekannt, dass die Steuerdaten keinem HARQ-Schema
unterliegen und somit eine relativ hohe Fehlerrate in Kauf genommen werden
müsste. Daher skaliert die QE D 2 die Größe des Steuerbereichs mit k1 und k2 hoch
und bewirkt so eine höhere Qualität der Steuerdaten und damit einen größeren
Qualitätsunterschied zwischen Steuer- und Nutzdaten. Die Parameter k1 und k2
sind somit jeweils ein Parameter für den Qualitätsunterschied zwischen einem die
Steuersignalisierungsbits führenden Steuerkanal und dem PUSCH-Datenkanal.
Mehr fordert das Merkmal 1.3.3 des Anspruchs 1 nicht.


4.1.10 Die Beklagte ergänzt, dass die Lehre der QE D 2 nicht ausführbar sei, da der
Fachmann für die Ausführung der Lehre keinerlei Information über die zu erzielende
technische Wirkung erhalte. Eine technische Wirkung, wie der vorgegebene Versatz
im Streitpatent zwischen den Blockfehlerraten der Nutzerdaten und der
Steuersignalisierung sei nicht offenbart. Damit sei die QE D 2 kein Bestandteil des
für das Streitpatent maßgeblichen Stands der Technik.


Diese Argumentation kann ebenfalls nicht überzeugen. Eine Erfindung ist
ausführbar offenbart, wenn die in der Patentanmeldung enthaltenen Angaben dem
fachmännischen Leser so viel an technischer Information vermitteln, dass er mit
seinem Fachwissen und seinem Fachkönnen in der Lage ist, die Erfindung
erfolgreich auszuführen. Es ist nicht erforderlich, dass mindestens eine praktisch
brauchbare Ausführungsform als solche unmittelbar und eindeutig offenbart ist

                                        - 33 -



(BGH, Urteil vom 13. Juli 2010, Xa ZR 126/07, GRUR 2010, 916 -
Klammernahtgerät).


Zum einen erfordert der Anspruch, wie bereits im Rahmen der Auslegung dargelegt,
nicht, dass ein Versatz zwischen den Blockfehlerraten der Nutzerdaten und der
Steuersignalisierung durch den Parameter offset_dB vorgegeben wird. Die
Blockfehlerrate bezieht sich lediglich auf ein Ausführungsbeispiel, das keinen
Eingang in den Patentanspruch gefunden hat.


Zum anderen kann der Fachmann mit den Konstanten k1 und k2, der spektralen
Effizienz SE als Produkt aus der Codierrate (Rc) und der Anzahl an Bits pro Symbol
(b), sowie der Anzahl an Bits (NACK/NACK, NCQI) die Größe der Steuerregion (Kap. 2.1
„Control Region … Size“) bzw. deren Anzahl an Symbolen SizeACK/NACK und SizeCQI
bestimmen. Somit ist der Fachmann mit seinem Fachwissen und Fachkönnen in der
Lage, deren Größe zu berechnen und die Lehre des Dokuments QE D 2 erfolgreich
auszuführen.


4.1.11 Damit ist das Verfahren gemäß Anspruch 1 dem Fachmann aus der QE D 2
i.V.m. seinem Fachwissen, belegt durch die Anlage 1 der NK 2, QE D 3 und QE D
10, nahegelegt.


4.2 Zum Hilfsantrag 1


Die QE D 2 offenbart auch eine separate Definition des Offset-Parameters (k1, k2)
für verschiedene Steuerkanäle (ACK/NACK, CQI) (vgl. dort Kap. 2.1). Darüber
hinaus ist der QE D 2 zu entnehmen, dass k1 und k2 abhängig von der spektralen
Effizienz (vgl. Kap. 2.2: „k1 and k2, … are a function of SEdata“) und somit auch über
SE = MMod / CR für verschiedene Modulations- und Codierschemata definiert sind.
Dem Fachmann ist darüber hinaus auch nahegelegt, die Konfiguration des
Versatzparameters     k   an   den   Bedürfnissen    der   speziellen   Übertragung
auszurichten. Beispielsweise wird er für zeitkritische Dienste eine geringere SE und
ein entsprechend anderes k vorsehen als für weniger zeitkritische Dienste.

                                       - 34 -




Damit ist auch das Verfahren des Anspruchs 1 des Hilfsantrags 1 dem Fachmann
aus der QE D 2 i.V.m. seinem Fachwissen, belegt durch die Anlage 1 der NK 2, QE
D 3 und QE D 10, nahegelegt (Art. 56 EPÜ) und nicht patentfähig (Art. 52 Abs. 1
EPÜ).


4.3 Zum Hilfsantrag 1a


Wie zum Hilfsantrag 1 ausgeführt, entnimmt der Fachmann der QE D 2 eine
separate Definition des Offset-Parameters (k1, k2) für verschiedene Steuerkanäle
und somit eine separate Definition für verschiedene Diensttypen, so dass auch das
Verfahren des Anspruchs 1 gemäß Hilfsantrag 1a nicht auf einer erfinderischen
Tätigkeit beruht (Art. 56 EPÜ) und damit nicht patentfähig ist (Art. 52 Abs. 1 EPÜ).


4.4 Zum Hilfsantrag 1b


Da Anspruch 1 des Hilfsantrags 1b dem Anspruch 1 nach Hilfsantrag 1a entspricht,
ist das Verfahren dieses Anspruchs wie Anspruch 1 des Hilfsantrags 1a zu
beurteilen. Das heißt, sein Verfahren beruht ebenfalls nicht auf einer erfinderischen
Tätigkeit (Art. 56 EPÜ) und ist damit nicht patentfähig (Art. 52 Abs. 1 EPÜ).


4.5 Zum Hilfsantrag 2


Hilfsantrag 2 erweitert den Schutzbereich des Streitpatents entgegen Art II § 6
Abs. 1 Satz 1 Nr. 4 IntPatÜbkG.


Die Beklagte argumentiert, dass die geänderten Ansprüche lediglich den Fall
beträfen,   dass   das   Ergebnis   der   Nächste-obere-Ganzzahl-Operation       der
Maximalwert sei. Die geänderten Ansprüche beträfen hingegen nicht den Fall, dass
die Zahl K der Maximalwert sei. Der Schutzbereich des Streitpatents werde daher
nicht erweitert.

                                       - 35 -



Diese Argumentation kann nicht überzeugen. Nach der Rechtsprechung des BGH
führt die nachträgliche Einbeziehung eines vom Streitpatent in der erteilten Fassung
nicht geschützten Gegenstands in einen Patentanspruch zu einer Erweiterung des
Schutzbereichs. Das Patentnichtigkeitsverfahren eröffnet dem Patentinhaber zwar
die Möglichkeit, das Schutzrecht in eingeschränkter Fassung zu verteidigen. Es
dient aber nicht darüber hinaus der Gestaltung des Patents. Deshalb darf ein
Patentanspruch im Nichtigkeitsverfahren nicht so geändert werden, dass er einen
von der erteilten Fassung nicht umfassten Gegenstand einbezieht (BGH, Urteil vom
15.   Dezember    2020,   X   ZR    120/18,     GRUR   2021,    579   Rn.   102   –
Nachrichtenübermittlungsdienst; BGH, Urteil vom 20. Dezember 2018, X ZR 56/17,
GRUR 2019, 389 Rn. 33 – Schaltungsanordnung III; BGH, Urteil vom
14. September 2004, X ZR 149/01, GRUR 2005, 145 – elektronisches Modul).


                          ⋅
Für den Bereich     ≥          _   (nachfolgend Bereich I) wird nun eine andere

Formel beansprucht als nach dem erteilten Patentanspruch. Die folgende Abbildung
der Klägerin zu 3) zeigt auf der horizontalen Achse die Steuersignalisierungsbits N
und auf der vertikalen Achse den Ausgabeparameter Mctrl. Zwei Graphen wurden
gezeichnet. Mit blau-gestrichelter Linie wird die ursprüngliche Formel aus dem
Patentanspruch wie erteilt gezeigt. Mit orange-durchgezogener Linie wird die neu
beanspruchte Formel nach Hilfsantrag 2 gezeigt, wobei K=5 rein beispielhaft
gewählt wurde.

                                        - 36 -




      Abbildung der Klägerin zu 3: Ursprünglich beanspruchte Formel (blau
         gestrichelt) und nach Hilfsantrag 2 beanspruchte Formel (orange
                                    durchgezogen).


                           ⋅
Für den Bereich      >          _    lehrt der Anspruch 1 des Hilfsantrags 2 einen

anderen Wert des Ausgabeparameters Mctrl als die ursprünglich erteilten
Ansprüche.


Des Weiteren ist es möglich, dass für K eine Größe vorgegeben wird, die unter den
gegebenen Umständen allein mit dem Formalismus nicht erreicht werden kann.
Auch damit ist der Schutzbereich in unzulässiger Weise auf vormals nicht umfasste
Werte von Mctrl ausgedehnt.


Der Vergleich der Merkmale 1.3.3 und 1.3.3‘ zeigt darüber hinaus, dass der erteilte
Anspruch 1 ausschließlich ein Verfahren, bei dem im Merkmal 1.3.3‘ die Variable K
auf null gesetzt wird (K = 0), schützt, wohingegen das Verfahren nach Hilfsantrag 2
nicht mehr auf K = 0 beschränkt, sondern stattdessen auf eine Vielzahl (K)
zusätzlicher Möglichkeiten gerichtet ist.

                                      - 37 -



Somit führt der Ersatz der Merkmale 1.3.2 und 1.3.3 durch die Merkmale 1.3.2‘ und
1.3.3‘ nicht zu einer Einschränkung des Schutzbereichs des erteilten Anspruch 1,
sondern zu dessen Erweiterung.


Soweit die Beklagte vorträgt, dass Anspruch 1 des Hilfsantrags 2 ein Verfahren zum
Gegenstand habe, das gegenüber dem erteilten Anspruch 1 lediglich durch
zusätzliche Verfahrensschritte beschränkt worden sei, weshalb dadurch der
Schutzbereich des erteilten Anspruchs 1 beschränkt werde, kann sich der Senat auf
Grund des Wortlauts des erteilten Anspruchs 1 dieser Auffassung nicht
anschließen. Zwar ist der Beklagten darin zuzustimmen, dass ein erteilter
Verfahrensanspruch i.d.R. durch zusätzliche Verfahrensschritte beschränkt wird,
doch verlangt der erteilte Anspruch 1 explizit, dass der Ausgabeparameter Mctrl das
Ergebnis der Formel nach Merkmal 1.3.3 ist. Durch die geänderte Formel 1.3.3‘ in
Hilfsantrag 2 ist der Ausgabeparameter Mctrl nunmehr entweder das Ergebnis der
Formel nach Merkmal 1.3.3 oder der Wert K. Folglich wird in Hilfsantrag 2 im
Ergebnis    kein    beschränkendes      Merkmal     hinzugefügt,    sondern    ein
Alternativmerkmal, was zu einer Schutzbereichserweiterung führt.


4.6 Patentanspruch 1 des Streitpatents ist somit weder in seiner erteilten Fassung,
noch in einer der Fassungen gemäß den Hilfsanträgen 1, 1a, 1b und 2
bestandsfähig.




                                        III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. §§ 91, 100, 269 Abs. 3 Satz 2 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                       - 38 -



                                         IV.


                               Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt     schriftlich   beim    Bundesgerichtshof,      Herrenstraße     45a,
76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht      (BGH/BPatGERVV)        auf   elektronischem    Weg    beim
Bundesgerichtshof               einzulegen,            wird             hingewiesen
(www.bundesgerichtshof.de/erv.html).




Dr. Himmelmann        Dr. Friedrich    Dr. Zebisch       Dr. Söchtig      Dr. Kapels
