---
ecli: "ECLI:DE:BPatG:2019:071119U2Ni7.17EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 7/17"
decided: "2019-11-07"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=47&nr=39602&anz=817&pos=717&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2019-11-07_2_Ni_7_17_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0064.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0066.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0101.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 7/17 vom 2019-11-07

## Entscheidung

Zu diesem Urteil ist ein Berichtigungsbeschluss ergangen
                                                 am 22. Juni 2020




                 BUNDESPATENTGERICHT

                    IM NAMEN DES VOLKES

                              URTEIL
                                                              Verkündet am
                                                           7. November 2019
2 Ni 7/17 (EP)                                                     …
verbunden mit
2 Ni 8/17 (EP)
2 Ni 9/17 (EP)

(Aktenzeichen)



                    In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2019:071119U2Ni7.17EP.0

    -2-



…

                                       -3-



     …




                 betreffend das europäische Patent 1 362 446
                                (DE 602 18 431)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der mündlichen Verhandlung vom 7. November 2019 unter Mitwirkung der Richterin Hartlieb
als Vorsitzende sowie der Richter Dipl.-Phys. Dr. rer. nat. Friedrich, Dipl.-Phys.
Dr. rer. nat. Zebisch, Dr. Himmelmann und Dr.-Ing. Kapels für Recht erkannt:


   I. Die Nebenintervention der Z… GmbH in D…, wird zugelassen.
   II. Das europäische Patent 1 362 446 B1 wird im Umfang seines Anspruchs 1
      mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch
      teilweise für nichtig erklärt, dass sein Anspruch 1 folgende Fassung erhält:

      A method for transferring IP data comprising payload and header fields over
      a radio interface between a mobile station and a packet radio network, in
      which method IP packet header fields are compressed (506) and decompressed (508) according to ROHC, characterized by comprising the steps of

                                       -4-



      allocating (503) at least two logical connections for the transfer of header
      fields compressed on the basis of different contexts, wherein a context represents the current properties of the compression,
      wherein each logical connection is a data link layer, L2, connection used for
      transferring IP data between the mobile station and the packet radio network,
      and
      wherein the allocating the at least two logical connections comprises allocating separate logical connections to the header fields of different compress
      states, transferring (507) the header fields compressed on the basis of the
      different contexts on separate logical connections,
      wherein the transferring the compressed header fields includes transferring
      each compressed header field on one of the at least two logical connections
      conforming to the compress state of the compressed header field.

      Im Übrigen wird die Klage abgewiesen.


  III. Von den Kosten des Rechtsstreits trägt die Beklagte 3/4, die Klägerinnen und
      die Nebenintervenientin jeweils 1/20.


  IV. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu
      vollstreckenden Betrages vorläufig vollstreckbar.




                                 Tatbestand



Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
erteilten, europäischen Patents 1 362 446 (Streitpatent), das unter Inanspruchnahme der finnischen Priorität FI 20010099 vom 16. Januar 2001 am 15. Januar
2002 international unter der Nummer PCT/FI2002/000030 mit der Benennung EP
unter Nennung der Bundesrepublik Deutschland als Bestimmungsland von der N…
Corporation in E…, Finnland, angemeldet und mit der WO 2002/056
532 A1 am 18. Juli 2002 offengelegt wurde. Das in der Verfahrenssprache Englisch
am 28. Februar 2007 mit der Bezeichnung „Transfer of IP data in communications
system, using several logical connections for compressed fields on the basis of different contexts“ mit der EP 1 362 446 B1 veröffentlichte Patent wird vom Deutschen

                                         -5-



Patent- und Markenamt unter der Nummer 602 18 431.2 geführt und umfasst 3
selbständige und 9 auf diese selbständigen Ansprüche direkt oder indirekt rückbezogene Patentansprüche. Eine deutsche Übersetzung des Patents wurde mit der
DE 602 18 431 T2 am 21. Juni 2007 veröffentlicht.


Patentanspruch 1 lautet in der englischen Fassung gemäß EP 1 362 446 B1 (mit
eingefügter Merkmalsgliederung entsprechend der Anlage N5):


  „M1 A method for transferring IP data comprising payload and header fields, in
      which method IP packet header fields are compressed (506) and decompressed (508), characterized by comprising the steps of
  M2 allocating (503) at least two logical connections for the transfer of headerfields compressed on the basis of different contexts, and
  M3 transferring (507) the header fields compressed on the basis of the different
      contexts on separate logical connections.”

Patentanspruch 1 lautet in der deutschen Fassung gemäß EP 1 362 446 B1 (mit
eingefügter Merkmalsgliederung):


  „M1 Verfahren für den Transfer von IP-Daten, die Nutzlast und Kopffelder umfassen, bei dem IP-Paketkopffelder komprimiert (506) und dekomprimiert
      (508) werden, dadurch gekennzeichnet, dass es die folgenden Schritte umfasst:
  M2 Zuweisen (503) mindestens zweier logischer Verbindungen für den Transfer von auf Basis unterschiedlicher Kontexte komprimierter Kopffelder, und
  M3 Übertragung (507) der auf Basis unterschiedlicher Kontexte komprimierten
      Kopffelder auf getrennten logischen Verbindungen.“



Mit ihren Klagen begehren die Klägerinnen jeweils die Nichtigerklärung des deutschen Teils des Streitpatents im Umfang des Patentanspruchs 1.
Die Nebenintervenientin hat mit Schriftsatz vom 8. Juni 2016 ihren Beitritt auf der
Seite der Klägerin zu 4. erklärt.


Die Klägerinnen und die Nebenintervenientin stützen sich auf den Nichtigkeitsgrund
der mangelnden Patentfähigkeit wegen fehlender Neuheit und mangelnder erfinderischer Tätigkeit (Art. 54 und 56 EPÜ i. V. m. Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG

                                       -6-



und Art. 138 Abs. 1 lit. a) EPÜ) und den Nichtigkeitsgrund der mangelnden Ausführbarkeit der beanspruchten Lehre (Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜG und Art.
138 Abs. 1 lit. b) EPÜ). Zudem ist nach Ansicht der Klägerinnen die Priorität zu Unrecht in Anspruch genommen worden.


Zur Stützung ihres Vorbringens haben die Klägerinnen und die Nebenintervenientin
die folgenden Dokumente genannt (es wird die Nummerierung der Klägerinnen 2
und 3 verwendet, die auch die Klägerin 4 und die Beklagte benutzen. Dabei sind
zusätzliche Dokumente der Klägerin 1 passend in die Nummerierung eingefügt):

N1       EP 1 362 446 B1 (Streitpatentschrift);
N2       Auszug aus dem Register des Deutschen Patent- und Markenamts zum
         Aktenzeichen 602 18 431.2;
N3       WO 02/056 532 A1 (Offenlegungsschrift);
N4       Prioritätsbeleg zur Fl 20010099;
N5       Merkmalsgliederung zu Verfahrensanspruch 1 des Streitpatents;
N6       Klageschrift der parallelen Patentverletzungsklage gegen die V…
         GmbH vor dem Landgericht München I (Az. …);
N7       Eingabe der Anmelderin auf einen Prüfungsbescheid des USPTO;
N8       Streitwertbeschluss des Landgerichts München I im Verfahren der I…
         LLC gegen die V… GmbH (Az. …) vom
         12.Oktober 2015;
N9       Urteil des Landgerichts München I im parallelen Verletzungsverfahren (Az.
         …) vom 22. Juli 2016 (in Auszügen);
N10      Berufungsbegründung im parallelen Verletzungsverfahren der I…
         LLC gegen die T… GmbH u.a. vor dem Oberlandesgericht München (Az. …) vom 28. November 2016 (in
         Auszügen);
N11      Klageschrift der parallelen Patentverletzungsklage gegen die D1…
         GmbH, die D2… GmbH und die
         T1… GmbH vor dem Landgericht München I (Az. …
         );
N11a     ROHC Standardvorschlag RFC3095
N11b     Vergleich zwischen <draft-ietf-rohc-rtp-04.txt> und RFC3095, wie durch
         IETF erstellt;
N11c     Historie von RFC3095 auf der IETF-Webseite;
N12      Klageschrift der parallelen Patentverletzungsklage gegen die T2…
         GmbH & Co. OHG und die T3… AG
         vor dem Landgericht München I (Az. …);
N12a     Entscheidung der Beschwerdekammer des Europäischen Patentamts vom
         21. Mai 2014 T0286/10, zusammen mit einer deutschen Übersetzung in
         Auszügen;
N12b     Entscheidung der Beschwerdekammer des Europäischen Patentamts vom
         18. Februar 2016 T2227/11

                                      -7-




HL1      Streitverkündung der T2… GmbH & Co. OHG und der T3…
         AG an die Z… GmbH und die
         Z1… Corporation.;
HL2      Presseerklärung der Z…GmbH vom 21. Februar 2013: „E1…
         plant LTE-Ausbau des Netzes mit Z2…“.
HL3      Eidesstattliche Versicherung von Herrn K…, Senior Legal
         Manager bei der Z… GmbH.

NK1    WO 01/35598 A1;
NK2    L.-E. Jonsson et al.: "RObust Checksum-based header COmpression“
       (ROCCO), ROCCO Version: 06, 15. Juni 2000;
NK2a   The Internet Standards Process – Revision 3, veröffentlicht im Oktober
       1996;
NK2a1 Auszüge aus der Webseite des IETF vom 8. Dezember 2000;
NK2b   Kopie der bei IETF archivierten E-Mail vom 16. Juni 2000;
NK2c   Webseite-Auszug, http://web.archive.org/web/20000815232824/httpzl/www.ietf.org:80/ids.by.wg/rohc.html;
NK2d   Webseite-Auszug, http://web.archive.org/web/20000815231439/http://www.ietf.org280/internetdrafts/draft-ietf-rohc-rtp-rocco-01.txt;
NK2e   FAQ der Non-Profit-Organisation Internet Archive;
NK2f   Anlagenkonvolut für weitere Veröffentlichungsnachweise der Druckschrift
       NK2, umfassend:
     NK2f1 Auszug aus Tagungsberichten von IETF für die 47. lETF Tagung
     NK2f2 Auszug aus Tagungsberichten von IETF für die 48. lETF-Tagung
     NK2f3 Zwei Forschungspapers, jeweils veröffentlicht am 15. Dezember
              2000 und im Jahr 2000, "Larzon et al.: Requirements on the TCP/IP
              Protocol Stack for Real-Time Communication in Wireless Environments" und im Jahr 2000, "Svanbro et al.: Voice-over-IP-over-Wireless", die die Druckschrift NK2 zitieren;
     NK2f4 Auszug aus der Webseite, "The ROCCO Homepage", auf der die
              Druckschrift NK2 veröffentlicht ist;
     NK2f5 PowerPoint-Folie von Lars-Erik Jonsson in der 47. lETF-Tagung;
NK3    C. Bormann et al.: "RObust Header Compression” Version 4 (ROHC), 11.
       Oktober 2000;
NK3a   Kopie der bei IETF archivierten E-Mail vom 13. Oktober 2000;
NK3b   Anlagenkonvolut für weitere Veröffentlichungsnachweise der Druckschrift
       NK3, umfassend:
     NK3b1 Ein Forschungspaper, veröffentlicht am 15. November 2000 "Bonjour et al.: IP convergence layer for HIPERLAN/2" und eine Patenanmeldung, "US 7,290,063 B2", angemeldet am 10. Januar 2001,
              die die NK3 zitieren;
NK4    WO 00/48374 A1
NK5    K. Svanbro: "Lower Layer Guidelines for Robust Header Compression"
       (SVANBRO), 10. März 2000;
NK5a   Kopie der bei IETF archivierten E-Mail vom 14. März 2000;

                                     -8-



NK5b   Anlagenkonvolut für weitere Veröffentlichungsnachweise der Druckschrift
       NK5, umfassend:
     NK5b1 PowerPoint-Folie von Krister Svanbro in der 47. lETF-Tagung;
     NK5b2 Auszug aus der Webseite, "The ROCCO Homepage", auf der die
               PowerPoint-Folie gemäß Anlage NK5b1 veröffentlicht ist;
     NK5b3 Ein Bericht von einem Teilnehmer der Tagung, Colin Perkins, veröffentlicht auf der Webseite einer Forschungsgruppe der Europäischen Kommission;
     NK5b4 Veröffentlichungsnachweis des Berichts gemäß Anlage NK5b3
NK6    M. Degermark: "lP Header Compression" (RFC 2507), veröffentlicht im
       Februar 1999;
NK7    3GPP Standard Dokument TS 25.323 V.3.3.0 (2000-09) (PDCP), veröffentlicht im September 2000;
NK7a   3GPP Standard Dokument TS 25.301 V.3.6.0 (2000-09) Radio Interface
       Protocol Architecture, veröffentlicht im September 2000;
NK7b   UMTS-Standardspezifikation ETSI TS 125 322 V3.1.2 (2000-01) RLC Protocol Specification, veröffentlicht im Januar 2000
NK8    US 5,987,022 A;
NK9    WO 99/66736 A2;
NK10   WO 00/76112 A1;
NK11   J. Kalliokulju, TSG Working Group 2 (Radio L2 and Radio L3), Paris,
       Frankreich, 3.-7. Juli 2000, R2-001533, “Response to LS (R3-001581) on
       SRNS Relocation of RT RABs and interaction with PDCP;”
NK11a Directory-Auszug zu NK11;
NK12   3GPP Standard Dokument TS 25.323 V.3.2.0 (2000-06) (PDCP);
NK12a Directory-Auszug zu NK12;
NK13   3GPP Standard Dokument TS 25.322 V.3.5.0 (2000-12) RCL protocol
       specification;
NK14   3GPP Standard Dokument TS 25.321 V.3.5.0 (2000-09) MAC protocol
       specification;
NK15   3GPP Standard Dokument TS 25.331 V.3.5.0 (2000-12) RRC protocol
       specification;

Die Klägerinnen und die Nebenintervenientin machen geltend, dass


-   die Nebenintervention der Z… GmbH zulässig sei;


-   das Verfahren des Anspruchs 1 nicht neu sei gegenüber den Druckschriften
    NK1, NK2, NK3, NK4, NK 5, NK7, NK8, NK9 und NK10;


-   das Verfahren des Anspruchs 1 gegenüber der Lehre der Druckschrift NK6 auf
    keiner erfinderischen Tätigkeit des Fachmanns beruhe;

                                        -9-



-   die Lehre des Anspruchs 1 nicht ausführbar sei, da sie nicht im gesamten beanspruchten Bereich für den Fachmann nacharbeitbar sei; und


-   die Priorität zu Unrecht in Anspruch genommen werde, da zum einen nicht nachgewiesen sei, dass zum Zeitpunkt der Anmeldung der Anmelder mit dem Anmelder der prioritätsbegründenden Anmeldung identisch war und zudem die Prioritätsanmeldung nicht die erste Anmeldung der Anmelderin gewesen sei, die das
    beanspruchte Verfahren offenbare;


-   die Ansprüche 1 nach den von der Beklagten vorgelegten Hilfsanträgen 1 bis 10
    teilweise unzulässig seien, ihre Lehren teilweise nicht ausführbar und zudem
    nicht patentfähig seien.



Die Nebenintervenientin stützt ihr berechtigtes Interesse am Streitbeitritt darauf,
dass sie in Deutschland LTE Basisstationen anbiete und vertreibe und auch die
Firma E2… GmbH mit LTE Basisstationen beliefert habe, die von der
Beklagten auf der Grundlage des Streitpatents auf Verletzung verklagt worden sei.
Die Lieferverträge enthielten keinen Verzicht auf Regressansprüche. Dazu legt sie
eidesstattliche Versicherungen vor. Das Streitpatent hindere die Nebenintervenientin darin, von ihr in Deutschland angebotene und gelieferte LT-Basisstationen mit
einer VolTE-Funktionalität auszustatten und schränke damit die geschäftlichen Aktivitäten ein. Damit sei ein berechtigtes Interesse gegeben, da im Patentnichtigkeitsverfahren ein großzügiger Maßstab gelte und bereits die Tätigkeit auf dem betreffenden Marktsegment ausreichen könne.


Die Beklagte hat der Klage der Klägerin 1 mit Schriftsatz vom 21. Juni 2016, der
Klage der Klägerinnen 2 und 3 mit Schriftsatz vom 27. April 2016 und der Klage der
Einsprechenden 4 mit Schriftsatz vom 18. April 2016 jeweils fristgerecht widersprochen und ihre Widersprüche mit Schriftsatz vom 21. November 2016 begründet. Sie
hat als Reaktion auf die Klagen und den qualifizierten Hinweis des Senats vom 26.
Juli 2018 mit Schriftsatz vom 21. September 2018 zehn weitere Ansprüche 1 als
Hilfsanträge 1 bis 10 eingereicht.

                                       - 10 -




Anspruch 1 nach Hilfsantrag 1 enthält ausgehend vom Anspruch 1 des Streitpatents im Merkmal M1 einen Einschub und zwischen den Merkmalen M2 und M3 das
zusätzliche Merkmal M2.1, so dass er lautet (zusätzliche Teile unterstrichen):


  „M1’ A method for transferring IP data comprising payload and header fields
       over a radio interface between a mobile station and a packet radio network,
       in which method IP packet header fields are compressed (506) and decompressed (508), characterized by comprising the steps of
  M2   allocating (503) at least two logical connections for the transfer of headerfields compressed on the basis of different contexts,
  M2.1 wherein each logical connection is a data link layer, L2, connection used
       for transferring IP data between the mobile station and the packet radio
       network, and
  M3   transferring (507) the header fields compressed on the basis of the different contexts on separate logical connections.”

Anspruch 1 nach Hilfsantrag 2 enthält zwischen dem Merkmal M2.1 des Anspruchs
1 nach Hilfsantrag 1 und dem Merkmal M3 das zusätzliche Merkmal


  M2.2 wherein logical connections of different characteristics are allocated to
       header fields compressed on the basis of different contexts,

und am Ende in Merkmal M3 den Zusatz „allocated to them“


In Anspruch 1 des Hilfsantrags 3 ist ausgehend vom Anspruch 1 des Hilfsantrags
1 in das Merkmal M1 nach dem Bezugszeichen (508) die Partizipialkonstruktion
„according to ROHC“ eingefügt und in das Merkmal M2 an dessen Ende der Zusatz
„wherein a context represents the current properties of the compression,“ angefügt.


Anspruch 1 des Hilfsantrags 4 enthält sowohl die Änderungen des Hilfsantrags 2
als auch die des Hilfsantrags 3.


In Anspruch 1 des Hilfsantrags 5 ist ausgehend vom Anspruch 1 des Hilfsantrags 4
noch das weitere Merkmal

                                      - 11 -



  M2.3 wherein at least different radio bearer parameters are reserved for the logical connections,

zwischen die Merkmale M2.2 und M3 eingefügt.


In Anspruch 1 des Hilfsantrags 6 ist ausgehend vom Anspruch 1 des Hilfsantrags
4 noch das weitere Merkmal


  M2.4 wherein a logical connection offering a higher bandwidth and/or a higher
       bit-error-ratio is allocated to uncompressed header fields than to compressed header fields and/or different radio frame sizes are used on the
       different logical connections conforming to different contexts,

zwischen die Merkmale M2.2 und M3 eingefügt.


Anspruch 1 des Hilfsantrags 7 lautet mit eingefügter Gliederung:


  M1’’ A method for transferring IP data comprising payload and header fields
       over a radio interface between a mobile station and a packet radio network,
       in which method IP packet header fields are compressed (506) and decompressed (508) according to ROHC, characterized by comprising the
       steps of
  M2’ allocating (503) at least two logical connections for the transfer of header
       fields compressed on the basis of different contexts, wherein a context
       represents the current properties of the compression,
  M2.1 wherein each logical connection is a data link layer, L2, connection used
       for transferring IP data between the mobile station and the packet radio
       network, and
  M2.5 wherein the allocating the at least two logical connections comprises allocating separate logical connections to the header fields of different compress states,
  M3   transferring (507) the header fields compressed on the basis of the different contexts on separate logical connections,
  M3.1 wherein the transferring the compressed header fields includes transferring each compressed header field on one of the at least two logical connections conforming to the compress state of the compressed header field.

Zu den Hilfsanträgen 8 bis 10 sei auf den Akteninhalt verwiesen.


Die Klägerinnen sind der Auffassung, dass die Ansprüche 1 der Hilfsanträge 1 bis
10 der Beklagten ebenfalls nicht zum Erfolg führen. Die Ansprüche der Hilfsanträge

                                        - 12 -



seien teilweise unzulässig erweitert und ihre Lehren seien teilweise nicht ausführbar. Die mit ihnen beanspruchten Verfahren seien nicht patentfähig, da sie gegenüber dem im Verfahren befindlichen Stand der Technik nicht neu seien oder zumindest nicht auf erfinderischer Tätigkeit beruhten.


Die Klägerinnen und die Nebenintervenientin stellen in der mündlichen Verhandlung
den Antrag,


        das europäische Patent 1 362 446 mit Wirkung für das Hoheitsgebiet der
        Bundesrepublik Deutschland im Umfang seines Patentanspruchs 1 für nichtig zu erklären.

Die Beklagte stellt den Antrag,


        die Klage abzuweisen,
        hilfsweise das europäische Patent 1 362 446 im Umfang seines Patentanspruchs 1 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch für nichtig zu erklären, dass dieser Anspruch die Fassung eines
        der Hilfsanträge 1 bis 10 gemäß Schriftsatz vom 21. September 2018, in dieser Reihenfolge, erhält.

Die Beklagte tritt der Argumentation der Klägerinnen in allen wesentlichen Punkten
entgegen. Sie verteidigt das Streitpatent in vollem Umfang und hilfsweise beschränkt mit den 10 genannten Hilfsanträgen. Sie verweist zur Stützung ihres Vorbringens u.a. auf folgende Dokumente:


NB1.7     Beschluss des Landgerichts München I im Rechtsstreit der I…
          LLC gegen die D1… GmbH, die D2…
          GmbH und die T1…GmbH (Az. …
          );
NB2.7     Kostennachricht der Landesjustizkasse Bamberg zum Az. …
          des Landgerichts München I;
NB1.8     Beschluss des Landgerichts München I im Rechtsstreit der I…
          LLC gegen die V… GmbH (Az. …);
NB2.8     Kostennachricht der Landesjustizkasse Bamberg zum Az. …
          des Landgerichts München I;
NB1.9     Beschluss des Landgerichts München I im Rechtsstreit der I…
          LLC gegen die T2… GmbH & Co. OHG und
          die T3… AG (Az. …);

                                     - 13 -



NB2.9    Kostennachricht der Landesjustizkasse Bamberg zum Az. …
         des Landgerichts München I;
NB3.8    Anlagenkonvolut zum Zusammenschluss der S… LLC
         und der I… LLC zur I… LLC;
NB3.9    Urteil des Landgerichts München I im Rechtsstreit der I…
         LLC gegen die T2… GmbH & Co. OHG und die
         T3… AG (Az. …);
NB5      Urteil des BPatG vom 12. Mai 2014 (Az. 1 Ni 2/13 (EP));
NB6      Beweisbeschluss der Beschwerdekammer 3.4.01 des EPA vom 8. November 2017 (Az. T 0401/12 – 3.4.01);
NB7      Mitteilung der Beschwerdekammer 3.4.01 vom 15. September 2017 (Az.
         T 0401/12 – 3.4.01);
NB8      Englischsprachige Übersetzung des finnischen Handelsregisterauszugs
         vom 4. Dezember 2003 für die N1… Ltd.;
NB8a     Deutsche Übersetzung zu NB8;
NB9      Finnische Handelsregisterinformation über die N1… Ltd.
         vom 7. Februar 2018;
NB9a     Deutsche Übersetzung zu NB9;
NB10     Brief der N… Corporation an das Patenttija rekisterihallitus vom 1. November 2001;
NB10a    Umschreibungsantrag von N2… Property Rights an das finnische Patentamt.
NB10b    Englischsprachige Übersetzung zu NB10;
NB11     Beschluss des 17. Senats des BPatG, Az. 17 W (pat) 01/02 vom 17. Oktober 2002;
NB12     Beschluss des 17. Senats des BPatG, Az. 17 W (pat) 47/00 vom 9. Januar 2003;
NB13     Entscheidung der Beschwerdekammer des Europäischen Patentamts,
         Az. Z 1134/06 vom 3. Februar 2004;
NB14     Beschluss des OLG München, Az. 6 W 1700/16 vom 8. Dezember 2016.
NB15     Metadaten des Files <draft-ietf-rohc-rtp-04.txt>;
NB16     Google Suchergebnis für „header compression rohc rtp 04“

Sie ist der Meinung, dass die Priorität zu Recht in Anspruch genommen werde, da
zum Zeitpunkt der Anmeldung des Streitpatents dessen Anmelder mit dem der prioritätsbegründenden Anmeldung übereingestimmt habe. Außerdem habe es sich
um die erste Anmeldung gehandelt. Die Lehre des Anspruchs 1 sei auch ausführbar. Sie sei zudem neu gegenüber dem von den Klägerinnen eingereichten Stand
der Technik und beruhe gegenüber diesem auch auf einer erfinderischen Tätigkeit.
Bei den Druckschriften NK2, NK3 und NK5 sei nicht nachgewiesen, dass diese vor
dem Anmeldetag der Öffentlichkeit zugänglich gewesen seien. Die Nebeninterven-

                                        - 14 -



tion sei zurückzuweisen, da die Nebenintervenientin keinen Interventionsgrund gemäß § 99 Abs. 1 PatG i.V.m. § 66 Abs. 1 ZPO dargelegt und glaubhaft gemacht
habe.


Jedenfalls aber sei das Streitpatent in der Fassung der Hilfsanträge bestandsfähig,
in denen die geäußerten Bedenken berücksichtigt worden seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                         Entscheidungsgründe



                                          I.


Die Nebenintervention ist zulässig.


Gemäß § 99 Abs. 1 PatG i.V.m. § 66 Abs. 1 ZPO kann jeder, der ein rechtliches
Interesse daran hat, dass in einem zwischen anderen Personen anhängigen
Rechtsstreit die eine Partei obsiege, dieser zum Zwecke ihrer Unterstützung beitreten. Im Falle der Nichtigkeitsklage gegen ein Patent ist einer Firma, die auf dem
Gebiet arbeitet, das das Patent betrifft, das rechtliche Interesse nicht abzusprechen,
da die Herstellung und/oder der Vertrieb eines unter den Schutzbereich fallenden
Gegenstandes oder die Durchführung eines einschlägigen Verfahrens der Firma
zunächst verwehrt ist und bei ähnlichen Patentgegenständen zumindest die Gefahr
einer Unterlassungs- oder Verletzungsklage besteht, was durch Nichtigerklärung
des betreffenden Patents verhindert werden kann.

                                          - 15 -



Im vorliegenden Fall hat die Nebenintervenientin ihr rechtliches Interesse mit der
Streitverkündung der T2… GmbH & Co. OHG und der T3…
AG (HL1) begründet.


Dies ist nach der Rechtsprechung, die einen großzügigen Maßstab anlegt, ausreichend. Der BGH (vgl. Beschluss vom 30. Mai 1967, Ia ZB 24/65, Leitsatz 4, GRUR
1968, 86 – „Ladegerät“) hat das erforderliche rechtliche Interesse im Sinne des § 99
Abs. 1 PatG i.V.m. § 66 Abs. 1 ZPO bejaht, wenn der Nebenintervenient Gegenstände vertreibt, derentwegen der ihn beliefernde Hersteller vom Patentinhaber
bzw. Gebrauchsmusterinhaber wegen Verletzung seines Ausschließlichkeitsrechtes bereits verklagt worden ist (vgl. auch Keukenschrijver, Patentnichtigkeitsverfahren, 6. Aufl. 2016, Rn. 181-182 mit Fußn. 251). Nach neuerer Rechtsprechung des
BGH (vgl. Beschluss vom 17. Januar 2006, X ZR 236/01, GRUR 2006, 438, Leitsatz
– „Carvediol I“) und des BPatG (vgl. Urteil vom 14. November 2011, 1 Ni 3/10 (EU)
juris, Rn. 57 – „Heizleitungsmatte und Verfahren zum Herstellen derselben“) reicht
es für die Zulässigkeit der Nebenintervention im Patentnichtigkeitsverfahren jedenfalls aus, wenn der Nebenintervenient ein Unternehmen ist, das durch das Streitpatent in seinen geschäftlichen Tätigkeiten als Wettbewerber beeinträchtigt werden
kann (vgl. Busse/Keukenschrijver, PatG, 8. Aufl. 2016, § 81 Rn. 127 mit Fußn. 372).
Hat der Nebenintervenient einen Regressanspruch zu befürchten, besteht in seiner
Person ein rechtliches Interesse im Sinne des § 66 Abs. 1 ZPO daran, dem Rechtsstreit beizutreten (vgl. Zöller/Althammer, ZPO, 33. Aufl. 2020, § 66 Rn. 13; MüKo-ZPO/Schultes, 5. Aufl. 2016, § 66 Rn. 17).


Ob und inwieweit der Vortrag im zivilgerichtlichen Verfahren schlüssig und/oder ob
die dort gestellte Forderung begründet ist, ist für den Streitbeitritt im Nichtigkeitsverfahren unerheblich, denn es ist nicht Aufgabe des Senats, zu beurteilen, ob eine
befürchtete Regressforderung nach dem Vortrag im Zivilprozess, wo es etwa auf
das Bestreiten und den Vortrag von Tatsachen maßgeblich ankommt (Verhandlungsgrundsatz bzw. Beibringungsgrundsatz), gerechtfertigt ist.

                                        - 16 -



Es spielt auch keine Rolle, dass gemäß dem Urteil des Landgerichts München I
(NB3) im Verletzungsprozess kein rechtliches Interesse der Nebenintervenientin
angenommen wurde, da - so das Landgericht München I - die von der T4…-
Gruppe von e1… übernommenen, von Z2… gelieferten Mobilfunkstationen vom
Rechtsstreit nicht betroffen seien, weil es sich bei ihnen gemäß dem dortigen Vortrag der Nebenintervenientin um Mobilfunkstationen handle, die nicht in der Lage
seien, das mit der Verletzungsklage angegriffene Verfahren umzusetzen, so dass
in der Folge Regressansprüche an die Nebenintervenientin, selbst wenn die Beklagte den Verletzungsprozess verlieren würde, nicht gerechtfertigt wären. Denn im
Verletzungsprozess ist ein bestimmter angeblich verletzender Gegenstand oder ein
angeblich verletzendes Verfahren Gegenstand des Verfahrens, während im Nichtigkeitsprozess das Patent im Vordergrund steht, das neben dem angeblich verletzenden Gegenstand noch eine Vielzahl weiterer Gegenstände und Verfahren umfasst oder auch in der Zukunft umfassen kann.




                                          II.




Die Klagen, mit denen die Nichtigkeitsgründe der mangelnden Patentfähigkeit wegen fehlender Neuheit und fehlender erfinderischer Tätigkeit (Art. 54, 56 EPÜ
i. V. m. Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG und Art. 138 Abs. 1 lit. a) EPÜ) und
der mangelnden Ausführbarkeit (Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜG und Art.
138 Abs. 1 lit. b) EPÜ) geltend gemacht werden, sind zulässig und teilweise begründet.


Die Klagen sind insofern begründet, als das Streitpatent für nichtig zu erklären ist,
soweit es in seinem Anspruch 1 über die von der Beklagten mit Hilfsantrag 7 beschränkte Fassung hinausgeht, denn die Verfahren des erteilten Anspruchs 1 und
der Ansprüche 1 nach den Hilfsanträgen 1 bis 4 sind gegenüber dem Stand der

                                        - 17 -



Technik darstellenden Dokument NK3 nicht neu (Art. 54 EPÜ) und damit nicht patentfähig (Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 lit. a) EPÜ). Die
Ansprüche 1 der Hilfsanträge 5 und 6 sind unzulässig, da sie Beschränkungen nicht
angegriffener Ansprüche sind (Art. 105a, 105b EPÜ, § 64 PatG).


Die weitergehenden Klagen sind hingegen unbegründet, denn in der Fassung nach
Hilfsantrag 7 hat das Patent Bestand.
Anspruch 1 des Hilfsantrags 7 ist zulässig, das mit ihm beanspruchten Verfahren ist
gegenüber dem im Verfahren befindlichen Stand der Technik neu (Art. 54 EPÜ) und
beruht diesem gegenüber auch auf einer erfinderischen Tätigkeit des Fachmanns
(Art. 56 EPÜ), so dass es patentfähig ist (Art. 52 Abs. 1 EPÜ).




1.    Das Streitpatent betrifft den Transfer von IP-(Internet Protocol)-Daten in einem Telekommunikationssystem und insbesondere in einem System, das die Komprimierung von IP-Datenkopffeldern bereitstellt.


Die sich schnell entwickelnde IP-Technologie hat das Einsatzgebiet verschiedener
IP-basierter Anwendungen über den herkömmlichen Internetdatentransfer hinaus
ausgedehnt. Insbesondere kam es zu einer rapiden Entwicklung IP-basierter Telefonanwendungen, die dazu führt, dass ein ständig wachsender Anteil des Transferwegs der Anrufe mit Hilfe von IP-Technologie implementiert werden kann. Insbesondere bilden mobile Kommunikationsnetzwerke einen Bereich, bei dem die IP-Technologie eine Fülle von Vorteilen bietet, da zusätzlich zu herkömmlichen
Sprachdiensten, die mit Hilfe verschiedener IP-basierter Sprachanwendungen bereitgestellt werden, mobile Kommunikationsnetzwerke zunehmend verschiedene
Datendienste, wie beispielsweise Browsen im Internet und elektronische Maildienste anbieten, welche in der Regel vorteilhafterweise als paketvermittelte IP-basierte Dienste hergestellt werden. Daher könnten IP-Schichten, die an die Protokolle
des mobilen Kommunikationssystems angepasst sind, zum Bereitstellen sowohl
von Audio/Videodiensten als auch verschiedener Datendienste verwendet werden.

                                        - 18 -



In mobilen Kommunikationssystemen ist es insbesondere von Bedeutung, dass die
begrenzten Funkressourcen so effizient wie möglich genutzt werden können. Dies
macht die Verwendung von IP-Protokollen auf den Funkschnittstellen andererseits
komplizierter, da der Anteil verschiedener Kopffelder in den zu übertragenden Daten in IP-basierten Protokollen groß ist und in der Folge der Anteil, der für die Nutzlast übrigbleibt, gering ist. Aufgrund der beschränkten Funkressourcen muss dieses
Verhältnis verringert werden. Zu diesem Zweck wurden Kopffeld-Komprimierungsverfahren entwickelt, wie beispielsweise ROHC (Robust Header Compression) von
IETF (Internet Engineering Task Force).


Im Streitpatent wird der Begriff „Nutzlast“ für Daten verwendet, welche für die eingesetzte Anwendung im Wesentlichen nützlich sind, und der Begriff „Kopffelder"
wird für Felder verwendet, die zu der Nutzlast hinzugefügt werden, indem niedrigere
Schichten sich um den Datentransfer der Anwendung kümmern. In Sprachanwendungen umfasst die Nutzlast beispielsweise Sprachproben und Steuerdaten, wobei
es sich bei den Kopffeldern in der Netzwerkschicht beispielsweise um RTP- (Real-Time Transport Protocol), UDP- (User Datagram Protocol) und IP- (Internet Protocol) Kopffelder handelt.


Die vorgeschlagenen Komprimierungsverfahren erfordern das Übertragen unkomprimierter Kopffelder zu Beginn einer Verbindung und möglicherweise auf periodische Weise. ROHC verwendet mehrere Komprimierungszustände, wobei die Effizienz der Komprimierung zunimmt, wenn der Betrieb zu einem höheren Zustand übergeht. Ein grundlegendes Prinzip besteht darin, dass die Komprimierung immer in
dem höchstmöglichen Zustand ausgeführt wird, vorausgesetzt jedoch, dass der
Komprimierer ausreichend Gewissheit darüber hat, dass der Dekomprimierer über
genügend Informationen über das Ausführen der Dekomprimierung in demselben
Zustand verfügt. Eine logische Verbindung ist in der Regel einer Konvergenzeinheit
zugeordnet, die die Übertragung des Anwendungsschichtdatenstroms zu dem mobilen Kommunikationsnetzwerk einerseits und zu der Konvergenzeinheit des RNC
andererseits bereitstellt, wobei die logische Verbindung zur Übertragung von IP-Paketen zu der physikalischen Schicht verwendet wird. Gemäß den Standards des

                                       - 19 -



Mobilkommunikationssystems UMTS (Universal Mobile Telecommunications System) der dritten Generation verwendet die Schicht des Paketdatenkonvergenzprotokolls (PDCP) immer eine Funkstreckensteuer-(RLC)-Schicht-Verbindung zum
Übertragen eines Datenstroms. Wenn die RLC-Verbindung und somit die logische
Verbindung zugewiesen wird, werden Parameter verhandelt, die die Eigenschaften
der logischen Verbindung, wie beispielsweise die Dienstgüte (Quality of Service,
QoS) der Verbindung bestimmen.


Bei der Übertragung insbesondere von Voice-over-IP (VoIP) benötigen Kopffelder
möglicherweise erheblich mehr Bits als die Nutzlast. Einige der zu übertragenden
Kopffelder können komprimiert werden und daher kann die Größe der Kopfteile in
den zu übertragenden IP-Paketen erheblich variieren. Da die Nutzlast der IP-Pakete
und die auf verschiedene Weise komprimierten Kopffelder auf derselben logischen
Verbindung entsprechend den verhandelten Parameter übertragen werden, wird in
der Datenübertragung keine optimale Ausnutzung der Funkressourcen erreicht. Ein
großer Teil der Kapazität muss insbesondere für einen IP-Paketdatenstrom reserviert werden, der von einem für UMTS entwickelten Breitbandsprachcode WB AMR
(Wideband Adaptive Multirate Codec) erzeugt wird, was zu unökonomischer Verwendung des Codebaums führt (vgl. Abs. [0002] bis [0006] der deutschen Übersetzung der Streitpatentschrift).




2.     Vor diesem Hintergrund liegt dem Streitpatent als technisches Problem die
Aufgabe zugrunde, ein Verfahren und ein Gerät bereitzustellen, welche es ermöglichen, IP-Daten effizienter über die Funkschnittstelle zu übertragen (vgl. Abs. [0010]
der deutschen Übersetzung des Streitpatents).




3.     Diese Aufgabe wird u.a. durch das Verfahren für den Transfer von IP-Daten
nach Anspruch 1 des Streitpatents gelöst.

                                         - 20 -



Das Streitpatent beansprucht gemäß Anspruch 1 ein Verfahren, das zur Übertragung von IP-Daten geeignet ist. Diese Daten beinhalten eine Nutzlast, die die eigentlichen zu übertragenden Daten darstellt und Kopffelder. Da das Internetprotokoll ein paketorientiertes Protokoll ist, bedeutet dies, dass das Verfahren zur Übertragung solcher Pakete geeignet sein muss. Die Nutzlast, also die eigentlich zu
übertragenden Daten, ist dann auf eines oder mehrere Pakete verteilt. Die Pakete
weisen alle einen Kopf auf, der mehrere Felder umfasst. Auch diese Köpfe müssen
mit übertragen werden. Alle oder ein Teil davon werden komprimiert und dann wieder dekomprimiert. Dass nicht notwendigerweise alle komprimiert werden müssen,
ergibt sich aus dem Anspruch, der zweimal den Begriff „header fields“ ohne bestimmten Artikel verwendet. Dies wird auch in Abs. [0009] des Streitpatents nochmals angegeben, indem dort hervorgehoben wird, dass auch ein Kontext möglich
ist, bei dem keinerlei Kompression stattfindet (vgl. Abs. [0009]: „It is to be noted that
a compression context according to which the headerfield is not to be compressed
at all is also possible.”).


Das mit Anspruch 1 beanspruchte Verfahren weist nur zwei Verfahrensschritte auf.
Der erste besteht darin, dass zwei oder mehr logische Verbindungen zugewiesen
werden. Diese sind für die Übertragung von auf Basis unterschiedlicher Kontexte
komprimierten Kopffeldern geeignet. Unter logischer Verbindung ist dabei eine Verbindung von einem Sender zu einem Empfänger zu verstehen, die logisch als eine
Verbindung verwaltet wird. Physikalisch können dabei für beide logische Verbindungen eine gemeinsame physikalische Verbindung, zwei physikalische Verbindungen,
also beispielsweise für jede logische Verbindung eine, oder aber auch mehrere physikalische Verbindungen bestehen.


Das Konzept der logischen Verbindung bedeutet, dass es einen Eingang und einen
Ausgang der Verbindung gibt, die jeweils eine Schnittstelle darstellen. An der Eingangsschnittstelle werden Daten in einem bestimmten Format übergeben. An der
Ausgangsschnittstelle verlassen sie die logische Verbindung in derselben Form.
Was mit ihnen dazwischen passiert, ist für die logische Verbindung unerheblich.

                                        - 21 -



Dies bedeutet, dass die beanspruchte logische Verbindung nach der Kopffeldkomprimierung beginnt und vor der Kopffelddekomprimierung endet. Eine logische Verbindung, in deren Verlauf erst die Kopffeldkomprimierung und die Kopffelddekomprimierung erfolgen, ist keine streitpatentgemäße logische Verbindung, denn an ihrem Eingang werden ihr unkomprimierte Kopffelddaten übergeben, die man auch
an ihrem Ende erhält. Ein UMTS-Radio-Bearer ist somit beispielsweise keine streitpatentgemäße logische Verbindung, da erst in seinem Verlauf die Kompression der
Kopffelddaten erfolgt.


Im siebenschichtigen OSI-Modell, das die Klägerinnen 2 bis 4 in ihren Klageschriften darstellen, reicht eine streitpatentgemäße logische Verbindung von der Schicht
2 (Sicherung, Data link) des Senders in die Schicht 2 des Empfängers (vgl. auch
Abs. [0009] der Streitpatentschrift). Die logische Verbindung wird somit durch den
gestrichelten Doppelpfeil „Sicherungs-Protokoll“ repräsentiert, obwohl die Daten eigentlich entlang des dicken Doppelpfeils über eine tiefere Schicht und das Übertragungsmedium laufen.




Der Begriff „Kontext“ ist für den Fall der Kopffeldkomprimierung ein feststehender
Fachbegriff. Er wird im Dokument NK3, das sich auf das vom Streitpatent bevorzugt
verwendete Kopffeldkompressionsverfahren, die „Robust Header Compression
(ROHC)“ bezieht, wie folgt definiert (vgl. S. 10, „Context“):

                                       - 22 -




  „The context is the state which the compressor uses to compress a header and
  which the decompressor uses to decompress a header. The context basically
  contains the uncompressed version of the last header sent (compressor) or received (decompressor) over the link, except for fields in the header that are included "as-is" in compressed headers or can be inferred from, e.g., the size of
  the link-level frame. The context can also contain additional information describing the packet stream, for example the typical inter-packet increase in sequence
  numbers or timestamps.”

Der Kontext enthält bei ROHC somit eine unkomprimierte Version des Kopfes, ohne
die Felder, die unverändert, also unkomprimiert übertragen werden, oder die aus
den Eigenschaften des Frames, z.B. seiner Größe abgeleitet werden können. Zusätzlich kann der Kontext weitere Informationen enthalten, die den Paketstrom beschreiben. Dies bedeutet in der Folge, dass sich der Kontext üblicherweise von einem Kopf zum nächsten ändert, indem z.B. ein Wert hoch- oder heruntergezählt
wird. In diesem Fall müssen für eine Komprimierung und eine Dekomprimierung die
Kontexte auf die gleiche Weise verändert werden.


Diese Definition ist im Wesentlichen auch die, die das Streitpatent angibt (vgl. Abs.
[0023]):


  „In the different compression methods, a context is typically defined both for the
  compressor and the decompressor, the context being a state according to which
  the compressor compresses the headerfield to be transmitted and the decompressor decompresses the received headerfield. The context typically also comprises an uncompressed version of the previous header field transmitted (by the
  compressor) or received (by the decompressor) over the data transmission connection. In addition, a context may comprise diverse data identifying the data
  packet flow, such as sequence numbers and time stamps of the data packets.
  The context thus typically comprises both static information, which remains the
  same for the entire data flow, and dynamic information, which changes during the
  data packetflow, although often according to a predetermined pattern. The context comprises information about the compress state and the compress mode.”

Merkmal M2 gibt nicht an, dass eine bestimmte logische Verbindung für einen bestimmten Kontext verwendet wird, oder eine Änderung des Kontextes zu einer Änderung der logischen Verbindung führen muss.

                                       - 23 -



Der weitere Verfahrensschritt M3 des Anspruchs 1 beansprucht, dass eine Übertragung der auf Basis unterschiedlicher Kontexte komprimierten Kopffelder auf getrennten logischen Verbindungen erfolgt. Wörtlich genommen würde dies bedeuten,
dass, von Ausnahmen abgesehen, für jeden Kopf eine eigene logische Verbindung
vorhanden sein muss, denn der Kontext ändert sich üblicherweise von einem Kopf
zum nächsten.


Das Merkmal M3 lässt sich aber auch noch anders interpretieren. So wird in der
Beschreibung ausgeführt, dass bisher in ROHC sechs verschiedene Pakettypen
definiert wurden (vgl. Abs. [0029]). Jeder dieser Pakettypen kann mit einem
„Context Indicator CID“ versehen werden, der den Kontext definiert, der in jedem
der speziellen Fälle verwendet wird, bevor das Paket auf den Übertragungsweg geschickt wird (vgl. Sp. 9, Z. 17 bis 22: „At the moment there are six different data
packet types defined for ROHC, four of which are used for transmission from the
compressor to the decompressor and two as return channel data packets from the
decompressor to the compressor. Although the number of data packets to be used
may change in the future, a common characteristic of all the data packet types is
that each data packet can be provided with a Context Indicator CID defining the
context to be used in each particular case before the packet is sent to the transfer
path.”).


Dies macht eine Interpretation dahingehend möglich, dass zwei Kontexte dann unterschiedlich sind, wenn ihnen eine unterschiedliche CID-Vergabe, nicht notwendigerweise eine unterschiedliche CID, da die gleiche CID auf zwei unterschiedlichen
logischen Verbindungen vorhanden sein kann (vgl. Dokument NK3, S. 36 Abschnitt
5.1.3.: „The CID space is distinct for each channel, i.e., CID 3 over channel A and
CID 3 over channel B do not refer to the same context, even if the endpoints of A
and B are the same nodes. In particular, CIDs for any pairs of forward and reverse
channels are not related (forward and reverse channels need not even have the
same size CID space).”), zugrundeliegt. Damit würde bei der Übertragung von Da-

                                        - 24 -



tenströmen davon ausgegangen, dass den Paketen desselben Datenstroms derselbe Kontext zugrundeliegt, da er auf derselben logischen Verbindung dieselbe
oder als Spezialfall keine CID trägt, der sich jedoch von Paket zu Paket verändert.


Eine weitere Interpretation im Rahmen von ROHC, auf das Anspruch 1 im Übrigen
nicht beschränkt ist, offenbart die Beschreibung des Streitpatents zu Fig. 4 (vgl. Abs.
[0030] bis [0033], insbesondere Abs. [0032]: „According to a preferred embodiment
of the invention, separate logical connections are allocated to the different compress
states. In the preferred embodiment, LC1 is allocated to the header fields of the
initiation/refresh state, LC2 to the payload and LC3 to the FO/SO headerfields of the
first and second states. This allows uncompressed initiation/refresh state headerfields to be separated from the compressed header fields. It is also possible that a
separate connection is allocated for signalling data.”). Dort werden die Pakete eines
Datenstroms in Kopf und Nutzlast zerlegt. Die Nutzlast wird über eine erste logische
Verbindung übertragen, während es eine zweite für nicht komprimierte Köpfe und
eine dritte für Köpfe im ersten und zweiten Kompressionszustand gibt. Dies bedeutet, dass zwei logische Verbindungen den Kopffeldern entsprechend deren Kompressionszustand zugeordnet werden. Der Kontext würde sich demnach dann unterscheiden, wenn im selben Kompressionsalgorithmus unterschiedlich starke Kompressionen der Köpfe gewählt würden. Dabei kann mehreren Kompressionszuständen dieselbe logische Verbindung zugewiesen werden. Die Beklagte gibt hierzu in
der Eingabe vom 26. Februar 2018 anders als in ihren Widerspruchsbegründungen
klarstellend an, dass auf einer logischen Verbindung auch mehrere Kontexte vorliegen können (vgl. Abschnitt A IV: „Auf einer logischen Verbindung dürfen mehrere
Kontexte vorliegen, solange die auf den getrennten logischen Verbindungen vorliegen Kontexte voneinander verschieden sind. Es wird betont, dass die Erfindung
nicht ausschließt, dass auf einer logischen Verbindung nach mehreren Kontexten
komprimierte Kopffelder vorliegen. Zum Beispiel sieht Unteranspruch 2 vor, eine
erste logische Verbindung für nach dem Kontext ”initiation/refresh state“ komprimierte Kopffelder zu verwenden, während auf einer zweiten logischen Verbindung
Kopffelder übertragen werden, die nach zwei Kontexten komprimiert wurden, nämlich „ﬁrst state“ und „second state“. Wichtig ist nur, dass sich - wie in Anspruch 1

                                       - 25 -



deﬁniert - die getrennten logischen Verbindungen hinsichtlich ihrer Kopffeldkomprimierung unterscheiden. Mit anderen Worten: auf den getrennten logischen Verbindungen dürfen streitpatentgemäß nicht die gleichen Kontexte vorliegen.“)


Der Begriff „unterschiedliche Kontexte“ ist somit nicht eindeutig festgelegt und ist
damit relativ breit auszulegen, insbesondere breiter als er in ROHC definiert wird,
solange die Kopffeldkomprimierung nicht auf ROHC festgelegt wird. Eine Beschränkung des Kompressionsverfahrens auf ROHC, wie sie in den Hilfsanträgen 3 bis 10
erfolgt, führt hingegen zu einer eindeutigen Definition des Begriffes „Kontext“, die
hier bereits zitiert wurde.


Insgesamt sind auf Grund dieser vielfältigen Auslegungsmöglichkeiten die Merkmale M2 und M3 so zu verstehen, dass für die Übertragung der Kopffelder zwei
oder mehr logische Verbindungen zur Verfügung gestellt werden, auf denen auf
Grundlage der Kontexte, die sich von Paket zu Paket üblicherweise ändern, komprimierte Kopffelder übertragen werden können, wobei das Nichtkomprimieren einen (leeren) Kontext für die Komprimierung darstellt. Die Kopffelder werden dann
über eine der logischen Verbindungen übertragen, wobei offenbleibt, nach welchen
Gesichtspunkten die logische Verbindung ausgewählt wird, auf der das jeweilige
Kopffeld übertragen wird.


Anspruch 1 beansprucht nicht, dass sich die Kompressionsalgorithmen für unterschiedliche Kontexte unterscheiden oder dass die logischen Verbindungen für den
Transfer von Kopffeldern mit unterschiedlichen Kontexten unterschiedliche Parameter aufweisen. Dies wird vom Anspruch 1 aber auch nicht ausgeschlossen, so dass
die Ausführungsbeispiele unter den Anspruch 1 fallen. Fraglich ist dabei, ob die
Merkmale des Anspruchs 1 ausreichen, um die gestellte Aufgabe zu lösen. Im Übrigen lässt Anspruch 1 auch offen, was mit der Nutzlast geschieht. Auch ist Anspruch 1 nicht auf drahtlose Übertragungsnetzwerke beschränkt. Eine solche Beschränkung erfolgt jedoch in den Hilfsanträgen.

                                        - 26 -



4.      Die Verfahren des erteilten Anspruchs 1 und der Ansprüche 1 nach den
Hilfsanträgen 1 bis 4 sind gegenüber dem Stand der Technik darstellenden Dokument NK3 nicht neu (Art. 54 EPÜ) und damit nicht patentfähig (Art. II § 6 Abs. 1 Satz
1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 lit. a) EPÜ). Die Ansprüche 1 der Hilfsanträge 5
und 6 sind unzulässig, da sie Beschränkungen nicht angegriffener Ansprüche sind
(Art. 105a, 105b EPÜ, § 64 PatG). Anspruch 1 des Hilfsantrags 7 ist hingegen
zulässig, das mit ihm beanspruchten Verfahren ist gegenüber dem im Verfahren
befindlichen Stand der Technik neu (Art. 54 EPÜ) und beruht diesem gegenüber
auch auf einer erfinderischen Tätigkeit des Fachmanns (Art. 56 EPÜ), so dass es
patentfähig ist (Art. 52 Abs. 1 EPÜ).


Der hier zuständige Fachmann ist als berufserfahrener Ingenieur der Fachrichtung
Elektrotechnik oder Nachrichtentechnik oder als berufserfahrener Informatiker zu
definieren, der einen Hochschulstudienabschluss besitzt und über eine mehrjährige
praktische Erfahrung in der Entwicklung von Verfahren und Vorrichtungen der paketorientierten Datenübertragung, zumindest auch in drahtlosen Netzwerken, verfügt.


4.1.    Der Zeitrang des Patents ist der der finnischen Prioritätsanmeldung (16. Januar 2001).


Die Klägerinnen 2 bis 4 machen geltend, dass die finnische Priorität zu Unrecht in
Anspruch genommen werde. Dies sei zum einen der Fall, weil die finnische Prioritätsanmeldung 20010099 (N4) von der N1… Ltd. getätigt wurde,
während die dem Streitpatent zugrundeliegende Anmeldung von der N… Corporation vorgenommen wurde, und somit bei fehlender Übereinstimmung der Anmelderinnen kein Nachweis der Übertragung des Prioritätsrechts vorliege. Zudem sei
die in Anspruch genommene Prioritätsanmeldung vom 16. Januar 2001 nicht die
erste Anmeldung der Anmelderin, die das in Anspruch 1 beanspruchte Verfahren
offenbare, denn dieses sei bereits in der Anmeldung WO 01/35 598 A1 (NK1) offenbart und damit bereits am 30. Oktober 2000 mit einer Priorität vom 5. November
1999 angemeldet worden.

                                      - 27 -




4.1.1. Nach den Prioritätsunterlagen des finnischen Patentamts (N4) ist am 19. November 2001 eine Umschreibung der Anmeldung auf die N… Corporation erfolgt,
wobei lediglich die Adresse nicht übereinstimmt. Während im Fall der finnischen
Prioritätsanmeldung H… als Adresse angegeben wird, findet sich auf der internationalen Anmeldung die Adresse E… Dabei handelt es sich allerdings um zwei
Standorte der N… Corporation, so dass zum Zeitpunkt der Anmeldung der internationalen Patentanmeldung am 15. Januar 2002 eine Identität des Inhabers der
Prioritätsanmeldung mit dem Anmelder der dem Streitpatent zugrundeliegenden internationalen Patentanmeldung vorliegt.


Die Klägerinnen 2 bis 4 geben zusätzlich an, dass es an einem Nachweis des Übergangs des Prioritätsrechts von der ursprünglichen Anmelderin der Prioritätsanmeldung auf die Inhaberin der Prioritätsanmeldung zum Anmeldezeitpunkt der internationalen Patentanmeldung fehle, d.h. sie gehen davon aus, dass mit dem Übergang
der Prioritätsanmeldung von der ursprünglichen Anmelderin auf die Inhaberin der
Anmeldung zum Anmeldezeitpunkt des Streitpatents das Prioritätsrecht nicht mit
übergegangen ist, sondern sich dieses immer noch bei der ursprünglichen Anmelderin befindet.


Diese Annahme ist jedoch unzutreffend, denn Art. 87 Abs. 1 EPÜ gibt an, dass jedermann, der […] eine Anmeldung für ein Patent, ein Gebrauchsmuster oder ein
Gebrauchszertifikat vorschriftsmäßig eingereicht hat, oder sein Rechtsnachfolger
[…] für die Anmeldung derselben Erfindung zum europäischen Patent […] ein Prioritätsrecht genießt. Zwar hat die N… Corporation nicht die Anmeldung eingereicht,
sie genießt jedoch als Rechtsnachfolgerin ebenso ein Prioritätsrecht.


Zum Nachweis der Rechtsnachfolge genügt ohne gegenteilige Hinweise bereits die
Umschreibung der Anmeldung beim finnischen Patentamt. Die Beklagte hat aber
mit den Dokumenten NB8 bis NB10 zudem den Beweis erbracht, dass die N…
Corporation mit der N1… Ltd. fusioniert wurde, so dass die N…

                                       - 28 -



Corporation Rechtsnachfolgerin der nicht mehr bestehenden N1…
Ltd. ist.


4.1.2. Bei der finnischen Prioritätsanmeldung 20010099 (N4) handelt es sich auch
um die erste Anmeldung im Sinne des Art. 87 Abs. 1 EPÜ, denn die mit der WO
01/35 598 A1 (NK1) offenbarte Erfindung geht auf einen anderen Erfindungsakt zurück als die finnische Prioritätsanmeldung und auch das Streitpatent. So wurden die
beiden Anmeldungen von unterschiedlichen Anmeldern vorgenommen, die Prioritätsanmeldung von der N1… Ltd., während die NK1 von der N…
Corporation angemeldet wurde. Auch die Erfinder sind unterschiedlich. So nennen
das Streitpatent und die Prioritätsanmeldung T5…, in E…, Finnland als
Erfinder, während die NK1 L… und B…, beide aus den USA, als
Erfinder nennt. Auch der Inhalt unterscheidet sich in seiner Gesamtheit deutlich.


Im vorliegenden Fall wird deutlich, dass es bei der Feststellung, welche frühere Anmeldung die erste Anmeldung im Sinne des Art. 87 Abs. 1 EPÜ ist, nicht nur darauf
ankommt, ob eine frühere Anmeldung den Gegenstand des Anspruchs 1 neuheitsschädlich vorwegnimmt. Dies ist nur eine notwendige nicht jedoch eine hinreichende
Bedingung. Zusätzlich muss die Anmeldung auf denselben Erfindungsakt zurückgehen. Denn es kann sich keine Änderung des Zeitrangs einer Anmeldung ergeben,
wenn diese von einem Anmelder auf einen anderen übertragen wird. So besteht
kein Zweifel an der rechtmäßigen Inanspruchnahme der Priorität, wenn die Anmeldung bei einem Anmelder verbleibt, der keine ältere Anmeldung mit dem Gegenstand des Anspruchs 1 getätigt hat. Überträgt dieser nun die Anmeldung auf jemanden, der bereits vor der Prioritätsanmeldung eine Anmeldung mit dem Gegenstand
des Anspruchs 1 vorgenommen hat, so würde dieser eine gegenüber der Priorität
noch ältere Anmeldung besitzen, so dass diese die erste Anmeldung wäre. In der
Folge würde sich der Zeitrang der übertragenen Anmeldung bei der Übertragung
ändern. Mit erster Anmeldung kann in Art. 87 Abs. 1 EPÜ somit, um eine Änderung
des Zeitrangs einer Anmeldung bei einer Übertragung zu vermeiden, nur die erste
Anmeldung, die auf denselben Erfindungsakt zurückgeht, gemeint sein.

                                       - 29 -



4.2.   Die Lehre des erteilten Anspruchs 1 des Streitpatents ist ausführbar.


Die Klägerinnen 2 bis 4 bemängeln, dass die Lehre des Anspruchs 1 des Streitpatents nicht ausführbar sei, weil dieser nicht auf ein spezifisches System beschränkt
sei, sondern allgemein für jegliches Netz gelte. Die Anmeldung offenbare aber nur
ein Beispiel für ein bestimmtes Netz, nämlich das UMTS-Netz. Es werde nicht offenbart, wie das Verfahren in den anderen Netzen umgesetzt werden könne. Somit
sei die Ausführbarkeit nicht über den gesamten beanspruchten Bereich gegeben,
was aber gemäß mehreren Entscheidungen der technischen Beschwerdekammern
des EPAs eine notwendige Voraussetzung sei.


Nach der Rechtsprechung des BGH ist es jedoch ausreichend, wenn ein ausführbares Beispiel der beanspruchten Lehre offenbart ist (vgl. BGH GRUR 2001, 813-
819 – „Taxol“; BGH GRUR 1998, 899-901 – „Alpinski“). Dies ist beim Streitpatent
für UMTS der Fall. Dass dem Fachmann nicht für jedes Netz offenbart wird, wie er
das erfindungsgemäße Verfahren umsetzen kann, ist unschädlich. So kann der
Fachmann das in einem verständlichen Wortlaut beanspruchte Verfahren auf Grund
seines Fachwissens und des offenbarten Beispiels bei einer Vielzahl anderer Netze
ebenfalls umsetzen, wenn auch nicht bei allen.


Problematisch könnte in diesem Zusammenhang der Begriff „unterschiedlicher Kontext“ sein. Denn wie bereits ausgeführt ändert sich der Kontext für die Komprimierung des Kopfes bei jedem neuen Kopf, da der Kontext entsprechend dem Kopf
aktualisiert wird. Es wären demnach so viele logische Verbindungen wie Pakete
notwendig, bzw. auf jeder logischen Verbindung würde immer nur genau ein Kopf
übertragen. Für eine derartige Vorgehensweise ist aber kein Ausführungsbeispiel
offenbart.


Dieser Mangel der Ausführbarkeit ist jedoch durch eine nicht wörtliche, andere Auslegung des Anspruchs, die - wie bereits aufgezeigt wurde - möglich ist, zu vermeiden. Gemäß der Rechtsprechung des BGH ist in diesem Fall diese Auslegung des

                                       - 30 -



Anspruchs zu verwenden (vgl. BGH GRUR 2015, 972-976 – „Kreuzgestänge“, BGH
GRUR 2011, 701-705 – „Okklusionsvorrichtung“).


4.3.   Das Verfahren des erteilten Anspruchs 1 ist nicht neu (Art. 54 EPÜ) und
damit nicht patentfähig (Art. 52 Abs. 1 EPÜ).


4.3.1. Entgegen der Ansicht der Beklagten, die durch Nichtwissen bestreitet, dass
die Dokumente NK 2 und NK3 vor dem Zeitrang des Streitpatents öffentlich zugänglich gewesen seien, ist das Dokument NK3 zu berücksichtigender Stand der Technik, da nach freier Überzeugung des Senats davon auszugehen ist, dass es vor
dem Prioritätstag des Streitpatents, dem 16. Januar 2001, der Öffentlichkeit zugänglich gemacht worden ist.


Hiervon geht auch das Streitpatent aus, denn in ihm wird ROHC in der Version vom
11.10.2000 als Stand der Technik angegeben (vgl. Abs. [0021]: „With regard to a
more detailed description of the compression method in question, reference is made
to an unfinished Internet draft “Robust Header Compression (ROHC)”, version 04,
11.10.2000.”). Dies ist eine Version, deren Datum etwa 3 Monate vor dem Prioritätsdatum liegt und in der NK3 wiedergegeben wird. Die Historie der IETF (Internet
Engineering Task Force) (siehe das Bild aus dem Dokument N11c) zeigt, dass diese
Version 4 nur kurzzeitig im Oktober 2000 gültig war und dann durch einen Nachfolgedraft, die Version 5 vom 23. Oktober 2000, ersetzt wurde. Die zugehörige E-Mail
NK3a der IETF vom 13. Oktober 2000 zeigt, dass der Internet-Draft NK3 spätestens
am 13. Oktober 2000 online gestellt wurde.

                                       - 31 -



Bei dem Dokument NK3 handelt es sich, wie auch beim Dokument NK2, um einen
Internet-Draft der Network Working Group der IETF. Was ein Internet-Draft ist, schildert die IETF folgendermaßen:


  „Internet-Drafts are working documents of the IETF, its areas, and its working
  groups. During the development of a specification, draft versions of the document
  are made available for informal review and comment by placing them in the
  IETF's Internet-Draft format.”

Auf Deutsch:

  „Internet-Drafts sind Arbeitsdokumente der IETF, ihrer Bereiche und ihrer Arbeitsgruppen. Während der Entwicklung einer Spezifikation werden Versionen
  des Dokuments zur informellen Durchsicht und Kommentierung zur Verfügung
  gestellt, indem sie in ein IETF Internet-Draft Format gestellt werden.“

Dies geschieht zeitnah zum angegebenen Datum. Eine Version bleibt höchstens ein
halbes Jahr gültig, kann aber auch früher ersetzt oder für ungültig erklärt werden.
Für jedes Internet-Draft gibt es eine Historie. Für die Dokumente NK2 und NK3 ist
diese unter https://datatracker.ietf.org/doc/rfc3095/ ersichtlich. Man kann erkennen,
dass das Dokument der ROCCO-Version 06, d.h. das Dokument draft-ietf-rohc-rtprocco-01.txt, also NK2 ab Juni 2000 und das Dokument draft-ietf-rohc-rtp-04.txt,
also NK3 ab Oktober 2000 online war.


Zwar ist es richtig, dass ein Internetdokument, das zu einem späteren Zeitpunkt
heruntergeladen wird, nicht mit einem Internetdokument gleichen Namens zu einem
früheren Zeitpunkt übereinstimmen muss, da es während dieser Zeit Veränderungen erfahren kann, die nicht immer nachvollzogen werden können, doch ist dabei
im Einzelfall zu überprüfen, ob eine solche Veränderung mit hinreichender Gewissheit ausgeschlossen werden kann. Nach Überzeugung des Senats wurde jedoch
ausreichend nachgewiesen, dass bei den Druckschriften NK2 und NK3 eine solche
Veränderung nicht erfolgt ist. Denn die Dokumente werden im Archiv einer seriösen
Organisation, der IETF, einem internationalen offenen Zusammenschluss von Netzwerkdesignern, Netzwerkbetreibern, Anbietern und Entwicklern von Netzwerken
und Netzwerkkomponenten, die sich mit der Weiterentwicklung der Internetarchitektur und dem reibungslosen Betrieb des Internets beschäftigen, bereitgestellt. In

                                        - 32 -



diesem Archiv werden verschiedene Dokumente derselben Sache mit unterschiedlichen Versionsnummern angegeben, so dass davon auszugehen ist, dass ein verändertes Dokument auch einen anderen Namen oder zumindest eine andere Versionsnummer erhält, wie dies bei den ROCCO-Versionen oder auch den ROHC-Versionen der Fall ist. Im vorliegenden Fall bestehen keine Anhaltspunkte dafür,
dass entgegen den üblichen Gepflogenheiten gerade an diesen Dokumenten eine
Änderung erfolgt ist.


Soweit die Beklagte hinsichtlich der Frage der Beweiswürdigung die Entscheidung
des BGH vom 26.06.2014 – X ZR 6/11 heranzieht und ausführt, es müsse mit Gewissheit feststehen, dass das Dokument NK3 der Öffentlichkeit vor dem Prioritätszeitpunkt zugänglich gewesen sei, ist festzustellen, dass es sich bei der herangezogenen Entscheidung um eine Einzelfallentscheidung handelt und die Beweiswürdigung in jedem Einzelfall getroffen werden muss. Hierbei muss der Senat einen
bestimmten Sachverhalt für wahr und nicht lediglich für wahrscheinlich halten, allerdings ist ein für das praktische Leben brauchbarer Grad ausreichend, der Zweifeln
Schweigen gebietet, ohne sie völlig auszuschließen (vgl. Busse, Patentgesetz, § 93
Rn. 2).


4.3.2. Dokument NK3 betrifft ein Verfahren zur Kompression von Köpfen bei der
Übertragung von IP-Daten über Funkstrecken, das mit ROHC bezeichnet wird. Es
ist ein Nachfolger des Dokuments NK2, das ebenfalls ein solches Verfahren beschreibt, welches mit ROCCO bezeichnet wurde. Im Rahmen von ROHC ist, wie
bereits erläutert, der Begriff „Kontext“ eindeutig definiert und insbesondere für jedes
zu übertragende Paket unterschiedlich (vgl. S. 10, „Context“). Im Einzelnen offenbart Dokument NK3 in Übereinstimmung mit dem Verfahren des Anspruchs 1 ein:


M1 - Verfahren für den Transfer von IP-Daten, die Nutzlast und Kopffelder umfassen, bei dem IP-Paketkopffelder komprimiert und dekomprimiert werden (vgl. S. 8,
2. Abs.: „Today, IP telephony is gaining momentum thanks to improved technical
solutions. It seems reasonable to believe that in the years to come, IP will become
a commonly used way to carry telephony. Some future cellular telephony links might

                                        - 33 -



also be based on IP and IP telephony. Cellular phones may have become more
general-purpose, and may have IP stacks supporting not only audio and video, but
also web browsing, email, gaming, etc.“ und S. 9, 3. und 4. Abs.: „A problem with IP
over cellular links when used for interactive voice conversations is the large header
overhead. Speech data for IP telephony will most likely be carried by RTP [RTP]. A
packet will then, in addition to link layer framing, have an IP [IPv4] header (20 octets), a UDP [UDP] header (8 octets), and an RTP header (12 octets) for a total of
40 octets. With IPv6 [IPv6], the IP header is 40 octets for a total of 60 octets. The
size of the payload depends on the speech coding and frame sizes being used and
may be as low as 15-20 octets. […] A viable header compression scheme for cellular
links must be able to handle loss on the link between the compression and decompression point as well as loss before the compression point.”), wobei es die folgenden Schritte umfasst:


M2 - Zuweisen mindestens zweier logischer Verbindungen (channels, vgl. S. 18,
2. Abs. „Channels“: „ROHC header-compressed packets flow on channels. Unlike
many fixed links, some cellular radio links can have several channels connecting
the same pair of nodes. Each channel can have different characteristics in terms of
error rate, bandwidth, etc.“) für den Transfer von auf Basis unterschiedlicher Kontexte komprimierter Kopffelder (vgl. S. 18, 3. Abs. „Context identifiers”: „On some
channels, the ability to transport multiple packet streams is required. It can also be
feasible to have channels dedicated to individual packet streams. Therefore, ROHC
uses a distinct context identifier space per channel and can eliminate context identifiers completely in channels where only a single packet stream is compressed.“),
und


M3 - Übertragung der auf Basis unterschiedlicher Kontexte komprimierten Kopffelder auf getrennten logischen Verbindungen (vgl. die bereits zitierten Absätze auf
S.18.).


ROHC umfasst somit eine Ausführungsform, bei der eine logische Verbindung für
mehrere Datenströme, die auch unterschiedliche Kontexte besitzen, verwendet

                                         - 34 -



wird. In diesem Fall werden die Köpfe mit einem „Context Identifier“ (CID) versehen.
ROHC besitzt aber auch eine Ausführungsform, bei der einzelne Datenströme, deren Pakete jeweils denselben CID besitzen, jeweils über eine eigene logische Verbindung übertragen werden. Somit offenbart das Dokument NK3 als eine mögliche
Ausführungsform auch das Verfahren des Anspruchs 1 des Streitpatents und nimmt
damit dieses neuheitsschädlich vorweg. Das Verfahren des erteilten Anspruchs 1
ist somit nicht patentfähig.


4.4.   Das Verfahren des Anspruchs 1 des Hilfsantrags 1 wird vom Dokument NK3
ebenfalls neuheitsschädlich vorweggenommen, so dass es ebenfalls nicht patentfähig ist. Die neu eingeführten Merkmale sind bereits aus der Figur 1.1 und dem
Hinweis auf die IP-Telefonie auf S. 8 der NK3 ersichtlich.


4.5.   Zu den mit Anspruch 1 des Hilfsantrags 2 beanspruchten verschiedenen
Charakteristiken der logischen Verbindungen sei auf den Abschnitt „Channels“ auf
S. 18 des Dokuments NK3 verwiesen. Dort heißt es:


  „Unlike many fixed links, some cellular radio links can have several channels connecting the same pair of nodes. Each channel can have different characteristics…”.

Damit kann auch das neu eingefügte Merkmal M2.2 die Patentfähigkeit des Verfahrens nach Anspruch 1 des Hilfsantrags 2 nicht begründen.


4.6.   Das mit dem Dokument NK3 offenbarte Kopffeldkompressionsverfahren
wurde ROHC genannt und ist auch die im Streitpatent angegebene Version dieses
Vorschlags für einen Standard. Der Kontext, der dort, wie bereits mehrfach ausgeführt, eindeutig definiert ist (vgl. S. 10 „Context“) repräsentiert auch die Eigenschaften der Kompression. Damit ist auch das Verfahren des Anspruchs 1 nach Hilfsantrag 3 gegenüber dem im Dokument NK3 offenbarten nicht neu und damit nicht
patentfähig.

                                       - 35 -



4.7.   Mit Hilfsantrag 4, dessen Anspruch 1 sowohl die Änderungen des Hilfsantrags 2 als auch die des Hilfsantrags 3 enthält, wird ein Zusammenhang zwischen
den verschiedenen logischen Verbindungen und den verschiedenen Kontexten hergestellt. Da aber jedes Paket und damit jeder Header einen anderen Kontext besitzt,
weil sich von einem Header zum anderen Werte nach bestimmten Regeln ändern,
werden logische Verbindungen mit unterschiedlicher Charakteristik auch unterschiedlichen Kontexten zugeordnet. Auch aus der Kombination der neu eingeführten Merkmale ergibt sich somit nichts, was die Patentfähigkeit begründen könnte.


4.8.   Beim Anspruch 1 des Hilfsantrags 5 wurden ausgehend vom Anspruch 1
des Hilfsantrags 4 noch die Merkmale des erteilten Anspruchs 5 in den Anspruch 1
aufgenommen. Damit handelt es sich bei Anspruch 1 nach Hilfsantrag 5 um eine
Beschränkung des Anspruchs 5 des Streitpatents. Anspruch 5 ist aber nicht angegriffen. Der neue Anspruch 1 des Hilfsantrags 5 käme somit wegen seines gegenüber dem erteilten Anspruch 5 geringeren Schutzbereichs gar nicht zur Wirkung, so
dass im Ergebnis den Klagen der Klägerinnen in vollem Umfang stattgegeben
würde und ein weiterer, beschränkter Anspruch in das Patent eingefügt würde. Für
eine solche Änderung, die überhaupt nur möglich ist, wenn sie insgesamt zu einer
Beschränkung eines nicht angegriffenen Patents oder der nicht angegriffenen Ansprüche im Nichtigkeitsverfahren führt, sind das Europäische Patentamt (gemeinsame Beschränkung für alle benannten Staaten, Art. 105a, 105b EPÜ) oder die Patentabteilung des Deutschen Patent- und Markenamts (nur für die Bundesrepublik
Deutschland, § 64 PatG) zuständig und nicht das Bundespatentgericht. Anspruch 1
des Hilfsantrags 5 ist somit unzulässig.


4.9.   Auch Anspruch 1 des Hilfsantrags 6 ist aus den zu Anspruch 1 des Hilfsantrags 5 angegebenen Gründen unzulässig, denn bei ihm handelt es sich sinngemäß
um eine Beschränkung des Verfahrens des ursprünglichen Anspruchs 5, der aber
nicht angegriffen ist. In Bezug auf die Patentfähigkeit sei aber auf den Abschnitt
„Channels“ auf S. 18 der Druckschrift NK3 verwiesen. Dort heißt es weiter:


  „… in terms of error rate, bandwidth, etc.”

                                      - 36 -




Damit kann das zusätzliche Merkmal des Anspruchs 1 des Hilfsantrags 6 auch eine
Patentfähigkeit nicht begründen.


4.10. Das ausführbare (Art. 83 EPÜ), gewerblich anwendbare (Art. 57 EPÜ) Verfahren des Anspruchs 1 nach Hilfsantrag 7 ist ursprünglich offenbart (Art. 123 Abs.
2 EPÜ) und auch patentfähig (Art. 52 EPÜ), da es gegenüber dem im Verfahren
befindlichen Stand der Technik sowohl neu ist (Art. 54 EPÜ), als auch auf einer
erfinderischen Tätigkeit des Fachmanns beruht (Art. 56 EPÜ).


4.10.1. Anspruch 1 nach Hilfsantrag 7 geht aus dem erteilten Anspruch 1, der identisch zum ursprünglichen Anspruch 1 ist (vgl. die Offenlegungsschrift N3), hervor,
indem in ihn eine Anzahl weiterer Merkmale aufgenommen wurde, so dass er ein
gegenüber dem erteilten Patent eingeschränktes Verfahren beansprucht. Diese
weiteren Merkmale sind in der Beschreibung ursprünglich offenbart. So findet sich
der erste Einschub im Merkmal M1‘‘, dass die Übertragung über Funk zwischen
einer Mobilstation und einem paketorientierten Netzwerk erfolgt, im Absatz [0008]
der Offenlegungsschrift N3.


Das Ausführungsbeispiel bezieht sich auf die Kopffeldkompression im Rahmen von
ROHC (vgl. Abs. [0020]), so dass auch der zweite Einschub im Merkmal M1‘‘ ursprünglich offenbart ist.


Bei dem Einschub im Merkmal M2‘, dass der Kontext die laufenden Eigenschaften
der Kompression repräsentiert, handelt es sich um eine Erklärung, die ebenfalls
beispielsweise dem Abs. [0008] der Offenlegungsschrift N3 entnommen werden
kann, genau wie auch das Merkmal M2.1, das in diesem Absatz ebenfalls ursprünglich offenbart ist.


Das Merkmal M2.5, dass die zwei logischen Verbindungen so zugeordnet werden,
dass getrennte logische Verbindungen den Kopffeldern verschiedener Kompressi-

                                        - 37 -



onszustände zugeordnet werden, ist u.a. dem Absatz [0010] der Offenlegungsschrift N3 zu entnehmen und wird im Ausführungsbeispiel weiter ausgeführt. Der
ursprüngliche Anspruch 2 enthält einen speziellen Fall der Zuordnung für ROHC.
Dieses Merkmal ist somit im Absatz [0010], auch in der beanspruchten Breite, ursprünglich offenbart.


Das weitere neu eingeführte Merkmal M3.1 geht aus dem Gesamtzusammenhang
des Ausführungsbeispiels hervor, insbesondere aus Abs. [0030] der Offenlegungsschrift N3, wo angegeben wird, dass die unterschiedlich komprimierten Kopffelder
auf unterschiedlichen logischen Verbindungen übertragen werden („The PDCP entity may be mapped to a plural number of RLC entities which allows a plural number
of logical connections LC1-LC3 to be offered to one PDCP entity. Separate logical
connections LC1-LC3 are allocated to the payload and to the differently compressed
(different context) header fields. The payload and the header fields of the IP packets
to be transmitted are separated, and, after the compression, the differently compressed header fields are transmitted on separate logical connections LC1-LC3.“).
Somit ist auch das Merkmal M3.1 ursprünglich offenbart, so dass insgesamt das
Verfahren des Anspruchs 1 nach Hilfsantrag 1 ursprünglich offenbart ist (Art. 123
Abs. 2 EPÜ). Da es sich bei der Änderung des Patentanspruchs 1, wie bereits dargestellt, um eine Beschränkung des Schutzbereichs des Patents handelt (Art. 123
Abs. 3 EPÜ), ist Anspruch 1 nach Hilfsantrag 7 zulässig.


4.10.2. Das Verfahren des Anspruchs 1 des Hilfsantrags 7 ist gegenüber dem im
Verfahren befindlichen Stand der Technik neu und beruht diesem gegenüber auch
auf einer erfinderischen Tätigkeit.


Dieser Anspruch beansprucht die Zuweisung von zwei logischen Verbindungen zu
verschiedenen Kompressionszuständen. Diese sind in ROHC festgelegt und mit IR
(Initialization and Refresh State), FO (First Order State) und SO (Second Order
State) bezeichnet (vgl. NK3, S. 21, „4.3.1. Compressor states“). NK3 gibt keinerlei

                                       - 38 -



Anregung, diesen unterschiedlichen Kompressionszuständen unterschiedlich logische Verbindungen zuzuordnen und sie auf diesen unterschiedlichen logischen
Verbindungen nach Kompressionszustand getrennt zu übertragen.


Auch die Klägerinnen waren, zuletzt in der mündlichen Verhandlung, nicht in der
Lage, eine entsprechende Stelle im Dokument NK3 aufzuzeigen. Sie haben lediglich argumentiert, dass es naheliegen würde, den unkomprimierten Zustand, dies
ist im Wesentlichen der IR-Zustand, über eine logische Verbindung mit höherer Bitrate zu senden, während die anderen Zustände, die deutlich weniger Information
enthalten, über eine Verbindung mit geringerer Bitrate gesendet werden, wenn
schon solch unterschiedliche logische Kanäle vorhanden sind (vgl. S. 18 „Channels“
der NK3). Dies ist in der Sache zwar richtig, doch benötigt der Fachmann hierzu
zunächst eine Anregung, die ihn in ROHC dazu veranlasst, einen Datenstrom nach
Kompressionszustand aufzuteilen, so dass die verschiedenen Kompressionszustände zumindest auch über verschiedene logische Kanäle übertragen werden können. Als Anregung ist es nicht ausreichend, wenn ihm offenbart wird, dass es logische Kanäle mit verschiedenen Charakteristiken gibt.


Das Verfahren des Anspruchs 1 nach Hilfsantrag 7 ist somit gegenüber dem im
Dokument NK3 offenbarten neu (Art. 54 EPÜ) und beruht diesem gegenüber auch
auf einer erfinderischen Tätigkeit des Fachmanns (Art. 56 EPÜ).


4.10.3. Auch der übrige im Verfahren befindliche Stand der Technik kann die Patentfähigkeit des Verfahrens nach Anspruch 1 des Hilfsantrags 7 nicht in Frage stellen.


Die im Prioritätsintervall veröffentlichte Druckschrift NK1 (WO 01/35 598 A1) mit
älterem Zeitrang vom 5. November 1999 beschäftigt sich nicht mit ROHC, weshalb
sie die Neuheit des Verfahrens nach Anspruch 1 des Hilfsantrags 7 auch nicht in
Frage stellen kann.

                                      - 39 -



Die grundlegende erfinderische Idee, die Kopffelder verschiedener Kompressionszustände über unterschiedliche logische Verbindungen zu übertragen, konnte entgegen der Ansicht der Klägerinnen auch nicht im Dokument NK2, die ROCCO - eine
Vorläuferverfahren von ROHC - beschreibt, nachgewiesen werden. Und auch die
übrigen im Verfahren befindlichen Dokumente lassen dieses Merkmal nicht erkennen.


5.     Bei dieser Sachlage waren die weiteren Hilfsanträge 8 bis 10 somit unbeachtlich, denn das europäische Patent 1 362 446 war mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig zu erklären,
dass sein Anspruch 1 die mit Hilfsantrag 7 eingereichte Fassung erhält.




                                       III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. §§ 91 Abs. 1, 92 Abs.
1, 100 Abs. 1, 101 Abs. 2 ZPO. Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG i.V.m. § 709 Satz 1 und 2 ZPO. Dabei wurde berücksichtigt, dass nur Anspruch 1 angegriffen wurde, und das Verfahren des nicht angegriffenen Anspruchs 2 der für den Fachmann erkennbar sinnvollste Fall von vier
im Rahmen von ROHC möglichen Fällen des Anspruchs 1 nach Hilfsantrag 7 ist, so
dass der Anteil des Obsiegens der Klägerinnen und der Nebenintervenientin gegenüber dem der Beklagten deutlich größer ist.

                                       - 40 -




                                         IV.


                              Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils - spätestens nach Ablauf von fünf Monaten nach Verkündung - durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt
oder Patentanwalt schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133
Karlsruhe, einzulegen.


Die Berufungsschrift muss


- die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
- die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) auf elektronischem Weg beim Bundesgerichtshof einzulegen, wird hingewiesen (www. bundesgerichtshof.de/erv.html).




Hartlieb     Dr. Friedrich      Dr. Zebisch       Dr. Himmelmann          Dr. Kapels
