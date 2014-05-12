---
ecli: "ECLI:DE:BPatG:2014:120514U5Ni55.11EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 55/11"
decided: "2014-05-12"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=27&nr=26061&anz=1119&pos=412&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2014-05-12_5_Ni_55_11_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 55/11 vom 2014-05-12

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      An Verkündungs Statt
                                                          zugestellt am
5 Ni 55/11 (EP)                                           12. Mai 2014
                                                               …
(Aktenzeichen)



                     In der Patentnichtigkeitssache

 …




 BPatG 253
 08.05

                                           -2-



                    betreffend das europäische Patent 1 188 269
                                   (DE 600 14 897)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 29. Januar 2014 durch den Vorsitzenden Richter
Gutermuth,    die    Richterin   Martens   sowie   die   Richter   Dipl.-Ing. Gottstein,
Dipl.-Ing. Kleinschmidt und Dipl.-Geophys. Dr. Wollny


für Recht erkannt:


        I.   Das europäische Patent 1 188 269 wird mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt, soweit es über folgende Fassung hinausgeht:


             „1. A Transport Format Combination Indicator TFCI encoding apparatus for a CDMA communication system,
                 the apparatus comprising:


             an orthogonal sequence generator for generating a plurality of basis biorthogonal sequences according to a first
             part of information bits, the orthogonal sequence generator
             including a one-bit generator (800) for generating the sequence “11111111111111111111111111111111” and a
             Walsh code generator (810) for generating the basis
             Walsh sequences
              “01010101010101010101010101010101” named W1,
              “00110011001100110011001100110011” named W2,
              “00001111000011110000111100001111” named W4,
              “00000000111111110000000011111111” named W8,
              “00000000000000001111111111111111” named W16;

                           -3-



a mask sequence generator (820) for generating a plurality
of basis mask sequences according to a second part of information bits,
wherein the basis mask sequences are
“00101000011000111111000001110111” named M1,
“00000001110011010110110111000111” named M2,
“00001010111110010001101100101011” named M4,
“00011100001101110010111101010001” named M8; and


an adder (860), for summing the basis biorthogonal sequences and the basis mask sequences generated from
the orthogonal sequence generator and the mask sequence generator.


2. A Transport Format Combination Indicator TFCI encoding apparatus for a CDMA communication system,
    the apparatus comprising:


an orthogonal sequence generator for generating a plurality of punctured basis biorthogonal sequences according
to a first part of information bits, the orthogonal sequence
generator including a one-bit generator (800) for generating the sequence “111111111111111111111111111111”
and a Walsh code generator (810) for generating the punctured basis Walsh sequences
   “101010101010101101010101010101” named W1,
   “011001100110011011001100110011” named W2,
   “000111100001111000111100001111” named W4,
   “000000011111111000000011111111” named W8,
   “000000000000000111111111111111” named W16;

                            -4-



a mask sequence generator (820) for generating a plurality
of punctured basis mask sequences according to a second
part of information bits,
wherein the punctured basis mask sequences are
 “010100001100011111000001110111” named M1,
 “000000111001101110110111000111” named M2,
 “000101011111001001101100101011” named M4,
 “001110000110111010111101010001” named M8; and


an adder (860), for summing the punctured basis biorthogonal sequences and the punctured basis mask sequences generated from the orthogonal sequence generator
and the mask sequence generator.


3. The encoding apparatus of claim 1, wherein the mask
    sequence generator is adapted to generate a ﬁrst msequence and a second m-sequence which can be added together to form a Gold code, is further adapted to
    form a ﬁrst sequence group having sequences formed
    by cyclically shifting the ﬁrst m-sequence and a second sequence group having sequences formed by cyclically shifting the second m-sequence is further
    adapted to generate and apply a column transposition
    function to the sequences in the ﬁrst group to convert
    the sequences in the ﬁrst group to orthogonal sequences, is further adapted to insert a column of „0“ in the
    front of the sequences in the second group, and is further adapted to generate and apply a reverse column
    transposition function to the sequences in the second
    group to convert the sequences in the second group to
    mask sequences.

                               -5-



   4. The TFCI encoding apparatus of any of claims 1 or 3,
       wherein the encoding apparatus comprises a plurality
       of ﬁrst multipliers (840 to 845) for multiplying the basis
       biorthogonal sequences by the ﬁrst part of the information bits, a plurality of second multipliers (846 to 849)
       for multiplying the basis mask sequences by the second part of the information bits and wherein the adder
       is adapted to sum the outputs of the ﬁrst and second
       multipliers.


   5. The encoding apparatus of any of claims 1, 3 or 4,
       wherein the orthogonal sequence generator (810) is
       adapted to output sequences of length 30 in which #0
       and #16 symbols are excluded from length 32 Walsh
       codes.


   6. The encoding apparatus of any of claims 1, 3, 4 or 5,
       wherein the mask sequence generator (820) is adapted to output sequences of length 30 in which #0 and
       #16 symbols are excluded from length 32 basis mask
       sequences.


   7. The encoding apparatus of any of claims 1, 3 or 4,
       wherein the encoding apparatus comprises means
       adapted to output a sequence of length 30 in which #0
       and #16 symbols are excluded from a sequence made
       by summing the basis biorthogonal sequences and the
       basis mask sequences.”


II. Im Übrigen wird die Klage abgewiesen.

                                       -6-



        III. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.


        IV. Das Urteil ist im Kostenpunkt in Höhe von 120 % des jeweils
            zu vollstreckenden Betrages vorläufig vollstreckbar.


                                   Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 1 188 269 (Streitpatent), das am
6. Juli 2000 angemeldet wurde und die Priorität der koreanischen Anmeldung
99/27932 vom 6. Juli 1999 in Anspruch nimmt. Das Streitpatent, das beim Deutschen Patent- und Markenamt unter dem Aktenzeichen 600 14 897.1 geführt wird,
betrifft eine Vorrichtung zur Kodierung eines Transport-Format-Kombinationsindikators (TFCI) für ein Kommunikationssystem. Es umfasst in der erteilten Fassung
(EP 1 188 269 B1) 10 Patentansprüche, die alle mit der Nichtigkeitsklage angegriffen sind.


Patentanspruch 1 hat in der Verfahrenssprache Englisch in dieser Fassung folgenden Wortlaut:


        „1. A Transport Format Combination Indicator TFCI encoding apparatus for a communication system, comprising:


            an orthogonal sequence generator (810) for generating a plurality of basis biorthogonal sequences according to a first part
            of Information bits;


            a mask sequence generator (820) for generating a, plurality of
            basis mask sequences according to a second part of information bits, and

                                       -7-



             an adder (860) for summing the basis biorthogonal sequences
             and the basis mask sequences generated from the sequence
             generator and the mask sequence generator.“


Die deutsche Übersetzung von Patentanspruch 1 lautet nach der Streitpatentschrift wie folgt:


         „1. Transport-Format-Kombinationsindikator-Kodierungsvorrichtung (TFCI) für ein Kommunikationssystem, umfassend:


             eine Orthogonal-Sequenz-Erzeugungsvorrichtung (810) zum
             Erzeugen einer Vielzahl von biorthogonalen Basissequenzen
             entsprechend einem ersten Teil von Informationsbits;


             eine Maskiersequenzerzeugungsvorrichtung (820) zum Erzeugen einer Vielzahl von Basismaskiersequenzen entsprechend
             einem zweiten Teil von Informationsbits; und


             einem Addierer (860) zum Addieren der von der Sequenzerzeugungsvorrichtung und von der Maskiersequenzerzeugungsvorrichtung erzeugten biorthogonalen Basissequenzen
             und der Basismaskiersequenzen.“


Wegen des Wortlauts der auf Patentanspruch 1 direkt oder indirekt rückbezogenen Patentansprüche 2 bis 10 wird auf die Streitpatentschrift Bezug genommen.

                                          -8-



Mit der Nichtigkeitsklage macht die Klägerin geltend, das Streitpatent offenbare
die Erfindung nicht so deutlich und vollständig, dass ein Fachmann sie ausführen
könne. Zudem gehe das Streitpatent über den Inhalt der Anmeldung in der ursprünglichen eingereichten Fassung hinaus und sei daher unzulässig erweitert.
Dem Gegenstand des Streitpatents, das nach Auffassung der Klägerin die Priorität
der koreanischen Voranmeldung nicht in Anspruch nehmen könne, fehle darüber
hinaus die Patentfähigkeit, denn er sei durch den Stand der Technik neuheitsschädlich vorweggenommen, jedenfalls aber diesem gegenüber nicht erfinderisch.


Die Klägerin legt zur Stützung ihres Vorbringens folgende Unterlagen vor:


       NK1           EP 1 188 269 B1 (mit       Rollenauszug   des   EPA,
                     Streitpatent = SP)
       NK2           DE 600 14 897 T2 (mit Rollenauszug des DPMA, dt.
                     Übersetzung des SP)
       NK3           BOSSERT, M.: Kanalcodierung. Stuttgart: Teubner,
                     1998. 2. vollst. neubearb. u. erw. Aufl.; S. 1-119.
                     ISBN 3-519-16143-5.
       NK4           WO 01/03366 A1
       NK5           PLESS, V. S.; HUFFMANN, W. C. [Hrsg.]: Handbook
                     of Coding Theory, Volume II. Amsterdam: Elsevier,
                     1998. S. 2119, 2127, 2128. ISBN 0-444-50087-1
       NK6           MACWILLIAMS, F. J.; SLOANE, N. J. A.: The Theory
                     of Error-Correcting Codes. In: North-Holland Mathematical Library, Vol. 16. New York: North-Holland
                     Publ. Comp., 1977. S. 370-479. ISBN: 0-444-85009-
                     0.
       NK6-1         MACWILLIAMS, F. J.; SLOANE, N. J. A.: The Theory
                     of Error-Correcting Codes. In: North-Holland Mathematical Library, Vol. 16. New York: North-Holland
                     Publ. Comp., 1977. S. 1-369. ISBN: 0-444-85009-0.

                               -9-



NK7      CLARK, George Cyrill: Error-correction coding for digital communications. New York: Plenum Press,
         1982. S. 84-85. ISBN 0-306-40615-2.
NK8      Klageschrift im parallelen Verletzungsstreit (LG
         Mannheim, Az.: 7 O 326/11) vom 21. April 2011.
NK10     Gliederung des Patentanspruchs 1 gemäß Streitpatent
NK11     EP 0 902 574 A2
NK12     Korrespondenztabellen / Diagramme für Gegenüberstellung SP / NK5 / NK11
NK13     BOUWER, A. E.; VERHOEFF, Tom: An Updated Table of Minimum-Distance Bounds for Binary Linear
         Codes. In: IEEE Transactions on Information Theory,
         1993. Vol. 39, No. 2, S. 662-677.
NK14     TSGR(99)913, TSG-RAN Working Group 1 meeting
         #5, Helsinki, Finland, July 13-16, 1999; Source:
         Samsung; Title: Harmonization impact on TFCI and
         New Optimal Coding for extended TFCI with almost
         no Complexity increase; Document for: Proposal,
         9 S.
NK14-2   URL:
         http://www.3gpp.eu/ftp/tsg_ran/WG1_RL1/TSGR1_0
         6/Docs/Pdfs/:                                      Index
         of/ftp/tsg_ran/WG1_RL1/TSGR1_06/Docs/Pdfs, zum
         Nachweis der Veröffentlichung und öffentlichen Zugänglichkeit    von    NK14,   2 S.   [recherchiert   am
         8. Dezember 2011]
NK15     Replik   im    parallelen   Verletzungsverfahren      vom
         14. November 2011.

                             - 10 -



NK16       3GPP TS 125 212 V3.11.0 (2002-09) Technical Specification: 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; Multiplexing and channel coding (FDD), (Release 1999),
           S. 48-49.
NK17       BLAHUT, Richard E.: Theory and Practice of Error
           Control Codes. Addison-Wesley Publ. Comp., 1983.
           6 nicht nummerierte Seiten, ISBN 0-201-10102-5.
NK18       US 5 771 288 A
NK19       Engl. Übersetzung der koreanischen Anmeldung
           27932/1999 vom 6. Juli 1999
NK20       „Vergleich zwischen der Übersetzung der Priorität
           und der Druckversion von EP'269 (basierend auf
           Texterkennung); Druckversion Seiten 9 und 10“,
NK20a      „Vergleich EP [0043] mit Priorität S. 10, Zeilen 7-15“,
NK21       EP 1 104 130 B1
NK22       JUNG, P.: Technical Expert Opinion about Patent EP
           1 188 269 B1, A… GmbH ./. S… E…
           Co., Ltd., 13. Mai 2013, 17 S.
NK22a      Deutsche Übersetzung zu NK22, 13. Mai 2013, 18 S.
NK22-OJ1   FORNEY, G. David: Concatenated codes. Ph.D. dissertation, MIT Press, 1966.
NK22-OJ2   ELIAS, Peter: Error-free coding. In: IRE Trans. Inform. Theory, vol. IT-4 (1954), pp. 29-37
NK22-OJ3   IMAI, Hideki: A Theory of Two-Dimensional Cyclic
           Codes. In: Information and Control, vol. 34 (1977),
           pp. 1-21
NK22-OJ4   BURTON, H. O.; WELDON, E. J.: Cyclic Product
           Codes. In: IEEE Trans. Inf. Theory (1965), pp. 433-
           439

                             - 11 -



NK22-OJ5   GOLDBERG, Morris: Augmentation Techniques for a
           Class of Product Codes. In: IEEE Trans. Inf. Theory
           (1973), pp. 666-672
NK22-OJ6   RAO, Venkat V.; REDDY, Sudhakar M.: A (48,31,8)
           Linear Code. In: IEEE Trans. Inf. Theory (1973),
           pp. 709-711
NK22-OJ7   REED, Irving: A Class of Multiple-Error-Correcting
           Codes and the Decoding Scheme. In: Trans. of the
           IRE Professional Group on Inf. Theory vol. 4 (1954),
           pp. 38-49
NK22-OJ8   3GPP TSG RAN WG1 Multiplexing and channel coding     (FDD)        TS 25.212 v1.0.0      (1999-04),
           23. April 1999
NK23       Berufungsbegründung im parallelen Verletzungsstreit
           (OLG Karlsruhe, Az.: 6 U 33/12)
NK24       JUNG, P.: Supplemental Technical Expert Opinion
           about Patent EP 1 188 269 B1, A… GmbH ./. S…-
           … Electronics Co., Ltd., 15. Juli 2013, 44 S.
NK24a      Deutsche Übersetzung zu NK24, 15. Juli 2013, 44 S.
NK24-OJ1   LIN, Shu; COSTELLO, Jr., Daniel J.: Error Control
           Coding, Intl. Edition, 2nd ed., S. 105
NK24-OJ2   = NK6
NK24-OJ3   TORRIERI, D.: Principles of spread-sprectrum communication. Second Edition, Systems. New York:
           Springer, 2011, S. 98
NK24-OJ4   GOLD, R.: Optimal Binary Sequences for Spread
           Spectrum Multiplexing. In: IEEE Trans. on Information Theory, Oct. 1967, S. 619-621.
NK24-OJ5   = NK26

                              - 12 -



NK24-OJ6    BROUWER, A. E.; VERHOEFF, T.: An Updated Table of Minimum-Distance Bounds for Binary Linear
            Codes. In: IEEE Trans. on Information Theory,
            Band 39, Nr. 2, Mar. 1993, S. 662-677.
NK24-OJ7    GOLD, R.: Maximal Recursive Sequences with 3-Valued Recursive Cross-Correlation Functions. In: IEEE
            Trans. on Information Theory, Jan. 1968, S. 154-156.
NK24-OJ8    = NK25
NK25        STARK,        Wayne E.:         Expert     declaration.
            24. Januar 2012, 10 S.
NK26        MAKS, J.: Expert declaration. 24. Januar 2012, 5 S.
NK27        JUNG, P.: Second Supplemental Technical Expert
            Opinion about Patent EP 1 188 269 B1, A… GmbH
            ./. S… E… Co., Ltd., 31. Juli 2013,
            82 S.
NK27a       Deutsche Übersetzung zu NK27, 31. Juli 2013, 97 S.
NK27-OJ9    CHEN, Yanling; HAN VINCK, A. J.: A Lower Bound
            on the Optimum Distance Profiles of the Second-Order Reed–Muller Codes. In: IEEE Transactions on
            Information Theory, 2010, Band 56, Nr. 9; S. 4309 -
            4320.
NK27-OJ10 BROUWER, A. E.: The [32,10,12] TFCI code. 5 S.
            [aufrufbar                                       unter:
            URL://http://www.win.tue.nl/~aeb/codes/tfci/tfci.pdf]
NK27-OJ11 YANG, Kyeongcheol et. al.: Quasi-Orthogonal Sequences for Code-Division Multiple-Access Systems.
            In: IEEE Transactions on Information Theory, 2000,
            Band 46, Nr. 3, S. 982 – 993.
NK27-OJ12 JERUCHIM, Michel C. et. al.: Simulation of communication systems. New York: Plenum, 1992. S. 500 –
            501; ISBN 0-306-43989-1
NK27-OJ13 = NK17, Seiten ix, 1-2, 130-160

                                       - 13 -



       NK27-OJ14 CLARK, George C.; CAIN, J. Bibb: Error-Correction
                      Coding for Digital Communications. New York: Plenum, 1981. S. 1, 89, 91; ISBN 0-306-40615-2.
       NK27-OJ15 = NK5, Seiten 23, 33, 46, 53-55, 123-124, 141-176
       NK27-OJ16 = NK22-OJ8
       NK27-OJ17 = NK3, Einleitung und Seiten 15, 169, 174
       NK28           Streitwertbeschluss im parallelen Verletzungsstreit
                      LG Mannheim vom 2. März 2012
       NK29           TSGR1#5(99)677, TSG-RAN Working Group 1 meeting #5, Cheju Island, Korea, June 1-4, 1999. Agenda
                      item:   3G     Harmonization;     Source:    Alcatel,
                      CSELT/TIM, DoCoMo, Ericsson, Fujitsu, InterDigital,
                      Japan Telecom, LGIC, Lucent Technologies, Matsushita, Mitsubishi, Motorola, NEC, Nokia, Nortel Networks, Qualcomm, Panasonic, Samsung, Siemens,
                      Telia, Texas Instrument, Toshiba, Vodafone; Title:
                      Impact of OHG harmonization recommendation on
                      UTRA/FDD and UTRA/TDD. 5 S.
       NK30           3GPP_TSG_RAN_WG1 Archives. E-mail Kommunikation und Dokument TSGR1#6(99)791, 3GPP TSG
                      RAN WG1 Meeting #6, 13-16th, July, 1999 Espoo,
                      Finland 1(8); Agenda item: 9.1; Source: Nokia; Title:
                      Encoding of TFCI for 15 slots per frame; Document
                      for:                 Approval                  URL:
                      http://list.etsi.org/scripts/wa.exe?A2=ind9907&L=3G
                      PPJTSG_RAN_WGl&F=&S=&P=2818; 10 S.


Die Klägerin beantragt,


       das europäische Patent 1 188 269 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für nichtig
       zu erklären.

                                         - 14 -



Die Beklagte beantragt,


        die Klage abzuweisen.


Hilfsweise verteidigt die Beklagte das Streitpatent in den Fassungen der Hilfsanträge 0 vom 9. Oktober 2013, 1 vom 17. Juni 2013, 1B vom 9. Oktober 2013, 2
vom 17. Juni 2013 und 3 vom 17. Juni 2013 in dieser Reihenfolge. In der mündlichen Verhandlung hat sie neue Hilfsanträge A und B überreicht, mit denen sie das
Streitpatent vorrangig hilfsweise verteidigt.


Der mit dem Hilfsantrag A verteidigte Hauptanspruch 1 lautet wie folgt:


        „1. A Transport Format Combination Indicator TFCI encoding apparatus for a CDMA communication system, the apparatus
            comprising:


        an orthogonal sequence generator for generating a plurality of basis biorthogonal sequences according to a first part of information
        bits, the orthogonal sequence generator including a one-bit generator (800)        for        generating      the        sequence
        “11111111111111111111111111111111” and a Walsh code generator (810) for generating the basis Walsh sequences
              “01010101010101010101010101010101” named W1,
              “00110011001100110011001100110011” named W2,
              “00001111000011110000111100001111” named W4,
              “00000000111111110000000011111111” named W8,
              “00000000000000001111111111111111” named W16;

                                      - 15 -



        a mask sequence generator (820) for generating a plurality of basis mask sequences according to a second part of information bits,
        wherein the basis mask sequences are
            “00101000011000111111000001110111” named M1,
            “00000001110011010110110111000111” named M2,
            “00001010111110010001101100101011” named M4,
            “00011100001101110010111101010001” named M8; and


        an adder (860), for summing the basis biorthogonal sequences
        and the basis mask sequences generated from the orthogonal sequence generator and the mask sequence generator.”


Wegen des Wortlauts der Patentansprüche 2 bis 7 des Hilfsantrags A wird auf den
Inhalt der Akte verwiesen; bezüglich der Fassung der Hilfsanträge B sowie 0, 1,
1B, 2 und 3 wird auf die genannten Schriftsätze der Beklagten bzw. die Sitzungsniederschrift Bezug genommen.


Die Klägerin, die zunächst vorsorglich die Verspätung der Hilfsanträge A und B mit
der Begründung gerügt hatte, die Änderungen seien der Beschreibung entnommen, hat beantragt,


        die mündliche Verhandlung für den Fall, dass der Senat die Hilfsanträge A und B nicht für unzulässige Fassungen erachte und
        auch nicht wegen Verspätung zurückweisen wolle, zu vertagen.


Die Beklagte hat ausgeführt, sie halte eine Vertagung der mündlichen Verhandlung zwar nicht für erforderlich, wolle sich einer gegensätzlichen Entscheidung des
Senats aber nicht verschließen.

                                        - 16 -



Im Übrigen tritt die Beklagte den Ausführungen der Klägerin in jeder Hinsicht entgegen. Die Lehre des Streitpatents sei ausführbar, sein Gegenstand sei nicht unzulässig erweitert. Dem Streitpatent stehe auch der weitere Nichtigkeitsgrund der
fehlenden Patentfähigkeit nicht entgegen, da es gegenüber dem Stand der Technik am Prioritätstag als neu gelte und auf erfinderischer Tätigkeit beruhe, jedenfalls in einer der hilfsweise verteidigten Fassungen.


Zur Stützung ihres Vorbringens hat die Beklagte folgende Unterlagen eingereicht:


        D1   Merkmalsanalyse des Patentanspruchs 1 des Streitpatents
        D2   TSGR1#7(99)99b60, TSG-RAN Working Group 1 meeting
             #7, Hanover, Germany, August 30 – September 3, 1999;
             Source: Samsung; Title: New Optimal Coding for extended
             TFCI with almost no Complexity increase (rev 2); Document
             for: Proposal. 16 S.
        D3   TSGR1#6(99)865, TSG-RAN Working Group 1 meeting #6;
             Source: Siemens; Title: Simulation results of TFCI coding
             Performance for TDD Document for: Discussion. 9 S.
        D4   SCHOTTEN,        Hans     D.:   Stellungnahme   zum   Patent
             EP 1 188 269 in der Patentnichtigkeitssache 5 Ni 55/11 (EP),
             A… ./. S… vor dem Bundespatentgericht,
             14. Juli 2013, 9 S.
        D5   COURT IN THE HAGUE: Judgment, Civil-Law Division, case
             number / case-list number: 400376 / HA ZA 11-2213 Judgment dated 20. June 2012. 39 S.
        D6   SCHOTTEN, H.D.: Zusätzliche Stellungnahme zum Patent
             EP 1 188 269 in der Patentnichtigkeitssache 5 Ni 55/11 (EP),
             A… ./. S… vor dem Bundespatentgericht. 22 S.
        D7   BGH, Urteil vom 19. Mai 2005 – X ZR 188/01 (BPatG) Aufzeichnungsträger, 11 S.

                                       - 17 -



        D8    ETSI SMG2 UMTS L1 Expert Group Meeting #8, Sophia Antipolis, France, November 9thth, 1998, Tdoc SMG2 UMTS-L1 567/98; Source: Nokia, Title: Extended TFI field, 14 S..


Zur Ergänzung des Tatbestands wird im Übrigen auf die Schriftsätze der Parteien
samt allen Anlagen sowie auf den Hinweis des Senats vom 21. Mai 2013 verwiesen.


                          Entscheidungsgründe


Die zulässige Klage, mit der die Nichtigkeitsgründe der fehlenden Ausführbarkeit
(Art. 138 Nr. 1c EPÜ), der unzulässigen Erweiterung gegenüber der ursprünglichen Anmeldung (Art. 138 Nr. 1b EPÜ) sowie der mangelnden Patentfähigkeit
(Art. 138 Nr. 1a EPÜ) geltend gemacht werden, ist teilweise begründet.


Soweit sich die Klage unbeschadet eines gemäß Art. 105a EPÜ anhängigen, jedoch noch nicht abgeschlossenen Beschränkungsverfahrens weiterhin gegen das
Streitpatent in der erteilten Fassung richtet, hat sie Erfolg, da der Gegenstand des
Streitpatents insoweit nicht patentfähig ist. In der Fassung des in der mündlichen
Verhandlung überreichten Hilfsantrags A liegt jedoch eine zulässige Beschränkung des Streitpatents vor. Insoweit hat das Streitpatent auch Bestand, da dem
Gegenstand des Streitpatents in dieser verteidigten Fassung keiner der geltend
gemachten Nichtigkeitsgründe entgegensteht, so dass die Klage insoweit abzuweisen war.

                                      - 18 -



                                        I.


1. Das Streitpatent EP 1 188 269 B1 (NK1) befasst sich laut dortigen Absätzen [0001] bis [0003] mit einer Vorrichtung und einem Verfahren zum Übertragen
von Daten in einem IMT-2000-System sowie einem Gerät zum Übertragen eines
Transport Format Combination Indicators (TFCI). Ein CDMA-Mobilkommunikationssystem – speziell ein IMT-2000-System - übertrage im Allgemeinen Frames,
die einen sprachbasierten, einen bildbasierten und einen zeichenbasierten Service
mit einer festen oder variablen Datenrate auf einem physikalischen Kanal bereitstellten, wie beispielsweise einen Dedicated Physical Data Channel (DPDCH).
Wenn Daten-Frames, die diese Art von Services enthalten, mit einer festen Datenrate übertragen werden, bestünde keine Notwendigkeit, einen Empfänger über die
Spreizrate jedes Daten-Frames zu unterrichten. Wenn die Daten-Frames andererseits mit einer variablen Datenrate übertragen werden, was impliziere, dass jeder
Daten-Frame eine andere Datenrate aufweist, müsste der Sender den Empfänger
über die Spreizrate jedes Daten-Frames unterrichten, die durch dessen Datenrate
bestimmt werde. Zum Übertragen von Daten-Frames mit variablen Datenraten informiere ein TFCI-Feld eines DPCCH einen Empfänger über die Übertragungsgeschwindigkeit des aktuellen Service-Frames. Das TFCI-Feld umfasse einen TFCI,
der viele Informationen enthalte, einschließlich der Datenrate eines Service-Frames. Der TFCI sei somit die Information, welche die zuverlässige Bereitstellung eines sprach- oder datenbasierten Services unterstütze.


Laut Absatz [0010] des Streitpatents würden TFCIs in einen Basis-TFCI und einen
erweiterten TFCI kategorisiert. Der erweiterte TFCI sei zur Erfüllung der Anforderungen des IMT-2000-Systems für unterschiedliche Serviceleistungen empfohlen
worden. TFCI-Bits seien für einen Empfänger wesentlich, um die von einem Sender erhaltenen Daten-Frames zu empfangen. Aus diesem Grund führe eine unzuverlässige Übertragung von TFCI-Informationsbits aufgrund von Übertragungsfehlern zu einer Fehlinterpretation der Frames im Empfänger. Der Sender codiere daher die TFCI-Bits vor dem Senden mit einem Fehlerkorrekturcode, so dass der
Empfänger eventuell generierte Fehler im TFCI korrigieren könne.

                                         - 19 -



Nach den Absätzen [0024] und [0025] des Streitpatents seien gemäß der herkömmlichen Technologie separate Hardware-Strukturen erforderlich, um den Basis-TFCI und den erweiterten TFCI zu unterstützen. Die Folge davon seien Einschränkungen hinsichtlich der Implementierung eines IMT-2000-Systems in Bezug
auf Kosten und Systemgröße. Es sei daher eine Aufgabe der vorliegenden Erfindung, eine Vorrichtung zum Kodieren eines Transport Format Combination Indicators bereitzustellen, die es ermögliche, TFCI-Codewörter mit unterschiedlicher
Länge zu kodieren, und eine verbesserte Fehlerkorrektur bei reduzierter Komplexität der Hardware bereitzustellen.


Die Kodierungsvorrichtung, die mit dem Patentanspruch 1 der erteilten Fassung
beansprucht wird, lässt sich in folgende Merkmale gliedern:


Englische Version:


        1   A Transport Format Combination Indicator TFCI encoding apparatus for a communication system, comprising:
        2   an orthogonal sequence generator (810) for generating a plurality of basis biorthogonal sequences
            2.1 according to a first part of information bits;
        3   a mask sequence generator (820) for generating a, plurality of
            basis mask sequences
            3.1 according to a second part of Information bits, and
        4   an adder (860) for summing the basis biorthogonal sequences
            and the basis mask sequences generated from the sequence
            generator and the mask sequence generator.

                                      - 20 -



Deutsche Version:


       1   Transport-Format-Kombinationsindikator-Kodierungsvorrichtung (TFCI) für ein Kommunikationssystem, umfassend:
       2   eine Orthogonal-Sequenz-Erzeugungsvorrichtung (810) zum
           Erzeugen einer Vielzahl von biorthogonalen Basissequenzen
           2.1 entsprechend einem ersten Teil von Informationsbits;
       3. eine Maskiersequenzerzeugungsvorrichtung (820) zum Erzeugen einer Vielzahl von Basismaskiersequenzen
           3.1 entsprechend einem zweiten Teil von Informationsbits;
               und
       4   einem Addierer (860) zum Addieren der von der Sequenzerzeugungsvorrichtung und von der Maskiersequenzerzeugungsvorrichtung erzeugten biorthogonalen Basissequenzen
           und der Basismaskiersequenzen.


2. Der Gegenstand des erteilten Anspruchs 1 richtet sich nach Auffassung des Senats an einen Diplomingenieur der Nachrichtentechnik oder Informatik mit universitärer Ausbildung, der mehrjährige Erfahrung auf dem Gebiet der Übertragung
und Verschlüsselung von digitalen Daten in Mobilfunknetzen besitzt.


3. Ausgehend vom Fach- und Erfahrungswissen dieses Fachmanns legt der Senat
den in der Fassung von Anspruch 1 gemäß Streitpatent enthaltenen Begrifflichkeiten jeweils folgendes Verständnis zu Grunde:


Ein TCFI, also ein Transport Format Combination Indicator / Transport-Format-Kombinationsindikator, ist ein digitales Datenwort, besteht aus bis zu 10 Bit und
stellt mit anderen Daten einen Bestandteil/ein Feld eines Funkrahmens dar, der in
einem Mobilfunksystem beim Senden des genannten Funkrahmens mit übertragen wird. Der Begriff TFCI als solcher ist lediglich im Umfeld von CDMA-Mobilfunksystemen definiert. Der TFCI repräsentiert die aktuell gültige Kombination von
Transportformaten der Daten, die im Funkrahmen kodiert und/oder gemultiplext

                                      - 21 -



enthalten sind. Beim Vorhandensein mehrerer nutzbarer Transportkanäle, über die
Datenblöcke transferiert werden, gilt in der Regel für jeden Transportkanal zunächst ein für diesen spezifisches Format, das von den jeweils geltenden Randbedingungen abhängt und jeweils durch einen Indikator, der dieses repräsentiert, kodiert sein kann. Werden mehrere Transportkanäle genutzt, werden die genannten
Indikatoren der einzelnen Transportkanäle so miteinander verknüpft, dass sie den
TFCI ergeben, der eine eindeutige Identifizierung der Transportformatkombination
ermöglicht. Aus dem TCFI geht letztlich für die Empfängerseite hervor, wie die
empfangenen Daten zu dekodieren und zu demultiplexen sowie welchen Transportkanälen sie jeweils zuzuordnen sind.


Ein/e TFCI encoding apparatus / TFCI-Kodierungsvorrichtung ist die Kodiereinheit
(Encoder), die den TFCI vor dem Senden in einem Mobilfunksystem kodiert.


Ein/e orthogonal sequence generator / Orthogonal-Sequenz-Erzeugungsvorrichtung ist im gegebenen Kontext ein Vorrichtungsbestandteil, der für die Kodierung
des TCFI eine Vielzahl von zueinander bi-/orthogonalen Sequenzen zu liefern vermag. Dies bedeutet - nachdem in den Ursprungsunterlagen hierzu nichts weiter
ausgeführt ist - nicht zwangsläufig, dass die hierfür zugrunde zu legende Generatormatrix selbst orthogonal sein muss oder deren Spalten oder Zeilenvektoren zueinander zumindest in Teilen orthogonal sein müssen.


Ein/e a mask sequence generator / Maskiersequenzerzeugungsvorrichtung ist im
gegebenen Kontext ein weiterer Vorrichtungsbestandteil, der zur Kodierung des
TCFI eine Vielzahl von so genannten basis mask sequences / Basismaskiersequenzen zu liefern vermag. Der Begriff der Basismaskiersequenzen stellt jedoch
im gegebenen Zusammenhang keinen Begriff aus dem Fachwortschatz dar. Wie
im Rahmen der mündlichen Verhandlung diskutiert wurde, ist das Präfix „Basis“
hierbei analog zur Bedeutung des Begriffs in der linearen Algebra auszulegen,
nämlich dass die so bezeichneten binären Sequenzen zusammengenommen ein
Erzeugendensystem für Maskiersequenzen darstellen, das heißt: alle entsprechend vorgegebener Randbedingungen / Bildungsvorschriften möglichen Maskier-

                                      - 22 -



sequenzen können aus den Basismaskiersequenzen abgeleitet werden. Hierbei
wird besonders darauf abgestellt, dass die Basismaskiersequenzen für die Gewährleistung einer sehr guten Fehlerkorrekturleistung einen möglichst hohen
Hammingabstand aufweisen. Mangels Zusatzinformationen kann das Wort „mask“
(und seine Ableitungen) im gegebenen technischen Zusammenhang keine den
Patentanspruch in seiner Allgemeinheit einschränkende Wirkung entfalten, sondern ist lediglich als Beschreibung seiner Wirkung anzusehen, nämlich das TCFI
Datenwort mit zu maskieren, also im Ergebnis einen Teil desselben im Verbund
mit anderen genannten Vorrichtungsbestandteilen zu kodieren.


Ein adder / Addierer ist als ein elektronisches Bauteil auszulegen, das eine Addition/Summation zweier binärer Zeichenketten durchführt und in der Regel aus
zwei oder mehreren logischen Gattern aufgebaut ist (wie ein „half-adder“, „full adder“, usw.). Dieses Bauteil weist damit auch eine andere Wahrheitstabelle auf als
ein einziges Gatter (z. B. ein XOR-Gatter), das zwar eine Verknüpfung binärer Zeichenketten vornehmen kann, nicht jedoch eine Addition im o. g. Sinne.


4. Zur erteilten Fassung


In der erteilten Fassung hat das Streitpatent mangels Patentfähigkeit keinen Bestand. Da es die Priorität der koreanischen Voranmeldung, so wie sie im Rahmen
des Nichtigkeitsverfahrens durch ihre englische Übersetzung – die als Druckschrift NK19 eingeführt wurde – repräsentiert wird, nicht beanspruchen kann, ist
sein Gegenstand gegenüber dem Stand der Technik, nämlich der Druckschrift D2,
nicht mehr neu.

                                       - 23 -



4.1.   Zur   Beanspruchung    der   Priorität   der   koreanischen   Voranmeldung
KR 99/27932


Für die wirksame Inanspruchnahme der genannten Priorität ist, wie auch die Einlassungen der Verfahrensbeteiligten in der Verhandlung zeigen, insbesondere der
Vergleich des Absatzes [0043] des Streitpatentes bzw. der Seite 10, Absatz 4 der
der     europäischen     Patentanmeldung        zugrundeliegenden      PCT-Schrift
WO 01/03366 A1 (NK4), mit dem entsprechenden Textabschnitt der Prioritätsschrift NK19 (Seite 10, Zeilen 7 bis 15) entscheidend, wie er seitens der Klägerin
im Rahmen der Druckschrift NK20a in direkter Gegenüberstellung dokumentiert
ist. Die Beklagte führt hierzu insbesondere aus, dass sie die in Absatz [0043] des
Streitpatentes beschriebene Bildungsvorschrift für die so genannten Basismaskiersequenzen als Grundlage für die allgemeinste Form der Auslegung des erteilten
Gegenstandes verstanden wissen will.


Aus dem dem Absatz [0043] des Streitpatents entsprechenden Abschnitt der Prioritätsschrift (NK19, Seite 10, Zeilen 7 bis 15) lässt sich jedoch für den Fachmann
weder die von der Beklagten vertretene Interpretation der für den erteilten Anspruch 1 maßgeblichen so genannten „mask sequences“ noch deren konkrete Bildungsvorschrift aus den so genannten „Walsh codes“ unmittelbar und eindeutig
entnehmen. Wie die Druckschrift NK20a zeigt, wird nämlich durch die im Streitpatent gegenüber der Prioritätsschrift an der Beschreibung vorgenommenen Änderungen überhaupt erst definiert, wie die Maskiersequenzen aus den als Grundlage
für ihre Ableitung dienenden Walsh-Codes durch explizite Operationsangaben gewonnen werden. Erst durch diese Änderungen wird eine konkrete mathematische
Vorschrift angegeben, die operationelle Abhängigkeiten zwischen den Maskiersequenzen und den Walsh-Codes ausformuliert und letztlich zur gewünschten Auslegung seitens der Beklagten führt.

                                        - 24 -



Für die „Walsh codes“ besteht diese Problematik nicht, da sie sowohl in der Prioritätsschrift NK19 (z. B. Figur 5 und 6 i. V. m. Seite 12, Zeilen 8 bis 10) als auch im
Streitpatent NK1 (z. B. Figur 5 und 6, Absatz [0049]) als orthogonale bzw. biorthogonale Sequenzen bekannt sind, die im Sinne der obigen Auslegung des Begriffs
„Basis“ auch ein entsprechendes Erzeugendensystem aufbauen können.


Im Ergebnis ist die Inanspruchnahme der Priorität aus KR 99/27932 durch die europäische Patentanmeldung, wie sie durch die genannte PCT-Anmeldung NK4 repräsentiert ist und in Folge für das Streitpatent gilt, jedoch aufgrund der im Streitpatent vorgenommenen umfangreichen inhaltlichen Änderungen bezogen auf die
Maskiersequenzen nicht zulässig.


Folglich sind für die Prüfung der Patentfähigkeit der mit dem Streitpatent geschützten Gegenstände auch all diejenigen Druckschriften in Betracht zu ziehen, die vor
dem Anmeldetag des Streitpatents – dem 28. Juni 2000 - der Öffentlichkeit bekannt geworden sind. Dies schließt insbesondere die von der Beklagten genannte
Druckschrift D2 mit ein.


4.2. Zur Patentfähigkeit der erteilten Fassung


Die Druckschrift TSGR1#7(99)99b60 (D2) – ein Standard-Dokument der so genannten „Technical Standardisation Group“ für das „UMTS Radio Access Network“ - zeigt sämtliche Merkmale, wie sie im erteilten Anspruch 1 des Streitpatents
unter Schutz gestellt werden und zwar:


Eine Transport-Format-Kombinationsindikator-Kodierungsvorrichtung (TFCI) für
ein Kommunikationssystem (z. B. Seite 1, Kapitel „1. Abstract“, Absatz 1, insbesondere: „TFCI code is very important because decoder depends on the rate information which was carried by TFCI bits. … The current coding scheme for extended TFCI is not optimal. ... the new Extended TFCI coding scheme having an optimal minimum distance … . Moreover, this code can be generated by natural and
simple extension of the current (32,6) TFCI code.“, Merkmal 1), umfassend:

                                         - 25 -



       eine Orthogonal-Sequenz-Erzeugungsvorrichtung zum Erzeugen
       einer Vielzahl von biorthogonalen Basissequenzen (Figur 5: Bereitstellung der Sequenzen „All 1‘s“, „W 32,2“, „W 32,3“, „W 32,5“,
       „W 32,9“, „W 32,17“ und Beschriftung des gestrichelten Kastens:
       „(32,6) Bi-orthogonal Code“ i. V. m. Seite 5, Kapitel 5 „Encoder
       Structure“ [sic!], Absatz 1: „ … encoder structure of the new proposed scheme is described. In fact, all walsh code with Iength 32 is a
       vector space of dimension 5. So, there are 5 basis for vector
       space, for example, W 32,2, W 32,3, W 32,5, W 32,9, W 32,17.“ (Unterstreichung hinzugefügt); Merkmal 2),
       wobei entsprechend ein erster Teil von Informationsbits verarbeitet
       wird (Figur 5: „a0“ bis „a5“, Absatz 1; Merkmal 2.1),
       sowie eine Maskiersequenzerzeugungsvorrichtung zum Erzeugen
       einer Vielzahl von Basismaskiersequenzen (Figur 5: Bereitstellung
       der Sequenzen „Mask 1“ bis „Mask 4“ i. V. m. Seite 4, Kapitel „4.
       Proposed New TFCI Coding scheme“, Absatz 1 und 2, insbesondere: „… we can find a optimal code in … a natural extension of
       the current (32,6) First Order Reed Muller code. Using sub-code of
       Second order Reed Muller code, we can achieve that goal. Second order Reed Muller code consists of codewords by adding
       some masks to the current First Order Reed Muller code. Then,
       the number of mask is decided by the number of TFCI bits exceeding 6bit. …“ (Unterstreichung hinzugefügt), Merkmal 3),
       wobei entsprechend ein zweiter Teil von Informationsbits verarbeitet wird (Figur 5: „a6“ bis „a9“; Merkmal 3.1).


Der diesen nachgeschaltete Addierer („Ʃ“) zum Addieren der von der Maskiersequenzerzeugungsvorrichtung und von der Orthogonal-Sequenz-Erzeugungsvorrichtung zusammen mit den Informationsbits erzeugten binären Ergebnisse, ist
aus der Figur 5 (rechte Seite) zu entnehmen (Merkmal 4).

                                        - 26 -



Somit sind sämtliche Merkmale des erteilten Anspruchs 1 aus der Druckschrift D2
bekannt.


Der Gegenstand des erteilten Anspruchs 1 ist somit mangels Neuheit seines Gegenstandes nicht patentfähig. Folglich kann das Streitpatent in der erteilten Form
auch keinen Bestand haben.


5. Zu Hilfsantrag A


Der Patentanspruch 1 gemäß Hilfsantrag A in seiner in englischer Sprache eingereichten Fassung lässt sich beispielsweise wie folgt gliedern (Änderungen im Vergleich zum Patentanspruch 1 gemäß Hauptantrag fett und durchgestrichen):


        1H A Transport Format Combination Indicator TFCI encoding apparatus for a CDMA communication system, the apparatus
            comprising:
        2   an orthogonal sequence generator (810) for generating a plurality of basis biorthogonal sequences
            2.1 according to a first part of information bits;
            2.2 the orthogonal sequence generator including a
                one-bit generator (800) for generating the sequence “11111111111111111111111111111111”
            2.3 and a Walsh code generator (810) for generating
                the basis Walsh sequences
                “01010101010101010101010101010101” named W1,
                “00110011001100110011001100110011” named W2,
                “00001111000011110000111100001111” named W4,
                “00000000111111110000000011111111” named W8,
                “00000000000000001111111111111111” named W16;

                                       - 27 -



        3   a mask sequence generator (820) for generating a, plurality of
            basis mask sequences
            3.1 according to a second part of information bits, and
            3.2 wherein the basis mask sequences are
                “00101000011000111111000001110111” named M1,
                “00000001110011010110110111000111” named M2,
                “00001010111110010001101100101011” named M4,
                “00011100001101110010111101010001”           named     M8;
                and
        4   an adder (860) for summing the basis biorthogonal sequences
            and the basis mask sequences generated from the sequence
            generator and the mask sequence generator.


5.1. Berücksichtigung des Hilfsantrags A


Den Hilfsantrag A, mit dem die Beklagte das Streitpatent vorrangig hilfsweise verteidigt, hat der Senat entgegen der Auffassung der Klägerin, er sei als verspätet
zurückzuweisen (und/oder aufgrund unzulässiger Inanspruchnahme der bereits
oben genannten koreanischen Priorität als unzulässig anzusehen), bei der Entscheidung berücksichtigt.


Die Fristsetzung nach Hinweis vom 21. Mai 2013 ist insbesondere durch Aufhebung des Termins vom 7. August 2013 zwar nicht wirkungslos geworden. Somit ist
die Verteidigung mit Hilfsantrag A nach Ablauf der dort genannten Fristen eingereicht worden. Mit der Antragstellung reagierte die Beklagte jedoch auf eine geänderte Auffassung des Senats, zu der dieser aufgrund des Vortrags der Beklagten
nach Übersendung des qualifizierten Hinweises gelangt war (vergleiche Seite 4
der Sitzungsniederschrift). Wie mit den Parteien in der mündlichen Verhandlung
ausführlich erörtert und oben unter Ziffer I.3. zusammengefasst, kommt es nämlich
bei der Auslegung des Patentgegenstandes entscheidend auf Absatz [0043] der
Patentschrift an, was jedoch zur Folge hat, dass die Priorität der koreanischen Patentanmeldung, wie oben unter Ziffer I. 4.1. ausgeführt, nicht wirksam beansprucht

                                       - 28 -



werden kann. Somit ist jedenfalls die Verspätung gemäß § 83 Abs. 4 Ziffer 2 PatG
genügend entschuldigt.


Soweit die Klägerin wegen der verspäteten Vorlage die Vertagung der mündlichen
Verhandlung beantragt hatte, ist ihr der Senat nicht gefolgt. Eine Beeinträchtigung
des rechtlichen Gehörs der Klägerin liegt nicht vor. Entgegen ihrer Ansicht sind die
Änderungen in Hilfsantrag A nicht der Beschreibung des Streitpatents entnommen. Sie gehen vielmehr zurück auf die Unteransprüche der erteilten Fassung
bzw. waren bereits Gegenstand des Hilfsantrags 1B, der am 9. Oktober 2013 eingereicht wurde, wobei bis zu diesem Zeitpunkt Frist zur Stellungnahme zum
Schriftsatz der Klägerin vom 31. Juli 2013, der zur Aufhebung des Termins vom
7. August 2013 geführt hatte, gewährt worden war. Insoweit ist die Klägerin somit
durch die Verteidigung der Beklagten nicht überrascht worden. Zur Vorbereitung
auf die mündliche Verhandlung hatte sich die Klägerin neben der Beschäftigung
mit der erteilten Fassung des Streitpatents auch auf die fristgemäß eingereichten
Hilfsanträge einzustellen. In diesem Rahmen bewegen sich ebenfalls die mit Hilfsantrag A vorgenommenen Änderungen. Insoweit war es der Klägerin daher zuzumuten, sich auf die Fragen der Patentfähigkeit der verteidigten Fassung ebenso
einzulassen wie auch auf die Diskussion, ob insoweit eine zulässige Fassung vorliegt. Zu beiden Fragen hat sich die Klageseite auch an der mündlichen Verhandlung beteiligt.


5.2. Prioritätsinanspruchnahme; Zulässigkeit / Ausführbarkeit des Hilfsantrags A


Die Fassung des Streitpatents nach Hilfsantrag A kann entgegen der Auffassung
der Klägerin die Priorität der koreanischen Voranmeldung KR 99/27932 sehr wohl
wirksam beanspruchen. Sie stellt nämlich im Ergebnis auf das in der Voranmeldung in Figur 8 und der entsprechenden Beschreibung Seite 15, Absatz 2 bis Seite 17, Absatz 1 unmittelbar und eindeutig offenbarte Vorsehen von genau drei
Kodegeneratoren für die Kodierung eines 10 bit TCFI-Kodeworts ab.

                                        - 29 -



Im Einzelnen kann dies der englischen Übersetzung der Voranmeldung (NK19),
insbesondere der dortigen Figur 8 an den Stellen entnommen werden, wo die Bezugszeichen „800“, „810“ und „820“ jeweils einem Sequenzgenerator, nämlich
dem so genannten „one-bit generator“, „Walsh code generator“ und „mask sequence generator“ entsprechen (vgl. NK19, Seite 15, Zeile 28 bis Seite 16, Zeile 28), die zusammen mit dem die Kodierung abschließenden Addierer („adder 860“) die für die Kodierung des TCFI-Kodewortes maßgeblichen Vorrichtungsbestandteile darstellen.


Die explizite Nennung der durch diese Kodegeneratoren bereitgestellten Sequenzen ist der Voranmeldung NK19 ebenfalls zu entnehmen, und zwar sowohl für den
„one-bit generator“ („Alwayssymbols are output“; Seite 15, Zeilen 28 und 29),
für den „Walsh code generator“ (Seite 16, Zeilen 3 bis 9) und den „mask sequence
generator“ (Seite 16, Zeilen 24 bis 29). Gleiches gilt auch für die explizite Nennung
der bevorzugten Längen von 32 bit für die Generatorsequenzen (z. B. Seite 16,
Zeilen 9 und 28) und 30 bit (z. B. Seite 30, Zeile 20).


Die entsprechenden Passagen in den Anmeldeunterlagen der dem europäischen
Prüfungsverfahren zugrundeliegenden PCT-Anmeldung geben diesen Sachverhalt
in gleicher Weise wieder, so dass mit dem Hilfsantrag A auch keine unzulässige
Erweiterung gegenüber den Ursprungsunterlagen im europäischen Prüfungsverfahren verbunden ist (NK4, Figur 8 i. V. m. Seite 15, Zeile 5 bis Seite 16, Zeile 21).
Der so beschriebene Gegenstand stellt aufgrund der mit dem Hilfsantrag A vorgenommenen, auch ursprünglich offenbarten Konkretisierungen eine zulässige Beschränkung dar, die der Fachmann auch problemlos ausführen kann, da ihm ausgehend von der Ursprungsoffenbarung alle hierfür notwendigen Informationen zur
Verfügung stehen.


5.3. Der Gegenstand des Streitpatents ist durch den berücksichtigungsfähigen
Stand der Technik auch weder vorweggenommen noch dem Fachmann nahe gelegt und erweist sich insofern als patentfähig.

                                       - 30 -



Als nächstkommender Stand der Technik, wie er sich aufgrund der zulässigen Inanspruchnahme der koreanischen Priorität vom 6. Juli 1999 darstellt, kommen die
Druckschriften NK14 (auf die sich die Klägerin in ihrer Argumentation während der
mündlichen Verhandlung insbesondere gestützt hat), NK21 und D2 nicht mehr in
Betracht. Vielmehr wird er nun durch den Auszug aus dem Lehrbuch PLESS und
HUFFMANN (1998) repräsentiert (Druckschrift NK5).


Dieser Auszug beschreibt – neben der unten ebenfalls aufgeführten Druckschrift NK6 – als einziger in sehr allgemeiner Form eine dem Gegenstand des Anspruchs 1 gemäß Hilfsantrag A strukturell in ihrem Ansatz vergleichbare Kodierungsvorrichtung, jedoch mit dem entscheidenden Unterschied, dass dort lediglich
zwei Kodegeneratoren für die Kodierung des Kodeworts eingesetzt werden. Eine
spezielle Anwendung auf ein TCFI-Datenwort wird dort ohnehin nicht thematisiert.


Im Einzelnen ist aus der NK5 nämlich


       eine Kodierungsvorrichtung für ein Kommunikationssystem bekannt (S. 2127, Kapitel 3.1, Absatz 2, z. B. „Error control was provided by mapping each shade of gray to 1 of the 64 R(1, 5) codewords [44]. The two Mariner '69 spacecraft sent a total of
       201 photographs back to the earth [36].“, Merkmal 1H),
       die eine Orthogonal-Sequenz-Erzeugungsvorrichtung (gleichzusetzen mit einem Teil der Basis „generator matrix“ „G(1,m)“ aus
       S. 2127, Kapitel 3.1, Absatz 3) zum Erzeugen einer Vielzahl von
       biorthogonalen Basissequenzen umfasst (die als Grundlage für die
       folgende Kodierung zu werten sind; in Kenntnis von NK3, Seite 115, Absatz 4, letzter Satz, sind Reed-Müller-Codes (RM-Codes) der Ordnung 1 biorthogonal: „Damit entsprechen biorthogonale Sequenzen den RM-Codes der Ordnung 1“; RM-Codes
       werden auch schon in NK19, Seite 8, Zeile 29 als relevant benannt, daher ist hier deren Referenznahme zulässig; Merkmal 2),

                                         - 31 -



        wobei alle vorhandenen Informationsbits, nämlich die zu kodierende Bitfolge m, unter Verwendung der von ihr erzeugten Sequenzen und einer der genannten Generatormatrix ebenfalls innewohnenden 1-Sequenz verarbeitet werden (S. 2127, Gleichung 3
        i. V. m. Figur 3: „1er“-Quadrat links unten; Merkmal 2.1, 2.2);


Diese Kodiervorrichtung umfasst neben den bereits genannten, wie dem Schema
der Figur 3 zu entnehmen ist, jedoch keine weiteren etwaig separaten Sequenzerzeugungsmittel, insbesondere auch keine zusätzliche Vorrichtung zum Erzeugen
einer Vielzahl von weiteren Sequenzen (vgl. Figur 3; Merkmal 3).


Dies ist auch nicht notwendig, da bereits alle Informationsbits verarbeitet worden
sind (vgl. Figur 3; Merkmal 3.1, 3.2).


Ein nachgeschalteter Addierer zum Addieren der aus der Operation der einzelnen
Sequenzen der Sequenzerzeugungsvorrichtung und der Informationsbits erhaltenen binären Ergebnissen, ist aus der Figur 3 (rechte Seite) jedoch wieder zu entnehmen (Merkmal 4).


Zum selben Resultat gelangt der Fachmann auch bei der Lektüre der Druckschrift NK6, nämlich des Lehrbuchauszuges MACWILLIAMS und SLOANE (1977).


Hier wird in vergleichbarer Weise mit vergleichbaren Ergebnissen wie in der NK5
die Natur von RM-Codes und deren Verwendung thematisiert (vgl. Seite 419, § 4,
Absatz 3 bis 5 und Gleichung (18), Merkmal 1 – Merkmal 2.2, Merkmal 2.3), jedoch fehlt auch hier wiederum (vgl. Seite 420, Figur 14.8) eine neben einer Sequenzerzeugungsvorrichtung für die RM-Codes und einem 1-bit-Generator zur Erzeugung einer 1-Sequenz, weitere separate Sequenzerzeugungsvorrrichtung, die
den Teil eines zu kodierenden Datenwortes kodiert, der von den vorhandenen Sequenzen noch nicht kodiert wurde (vgl. Figur 14.8; Merkmal 3).

                                      - 32 -



Vielmehr wird die Kodierung eines Kodewortes (“u0”, “u1”, “u2”, “u3”) vollständig
durch die vorhandenen beiden für die Kodierung vorgesehen Sequenzen (“1”, “t1”,
“t2”, “t3”) vorgenommen (vgl. Figur 14.8; Merkmal 3.1, 3.2). Abschließend wird für
den Kodiervorgang auch hier noch ein Addierer eingesetzt (Seite 420, Figur 14.8,
rechte Seite i. V. m. Seite 419, Summenterm nach Gleichung (18); Merkmal 4).


Eine Annahme der Klägerin, dass sich der Fachmann zum Anmeldezeitpunkt allein auf Basis dieser beiden Druckschriften und aufgrund seiner Kenntnis, dass
neben den Reed-Müller-Codes 1. Ordnung auch derartige 2. Ordnung existieren
(was er beispielsweise aus der Druckschrift NK3, dem Lehrbuch BOSSERT
(1998), Seite 117 ff., hätte entnehmen können) als Subcodes anzusprechende
Übergangskonstrukte ohne erfinderisches Zutun hätte erarbeiten können, und die
für ein 10 bit Datenwort wohl mathematisch gesehen „zwischen“ den Reed-Müller-Kodes 1. und 2. Ordnung anzusiedeln wären, ist nicht überzeugend, da keiner der
beiden Druckschriften NK5 und NK6 die Anregung entnommen werden kann, von
der bisherigen Praxis abzuweichen und anstatt wie bisher zwei nun drei Kodierer
vorzusehen, um ein von 6 auf 10 bit zu erweiterndes Kodewort - wie es etwa das
TCFI darstellt - unter Beibehaltung der bisherigen Bitlänge der für eine Kodierung
verwendeten Sequenzen zu kodieren, wie sie bisher für ein zu kodierendes Datenwort von 6 bit Länge eingesetzt wurden. Vielmehr weisen die Druckschriften gerade in ihrer Zusammenschau in die entgegengesetzte Richtung, nämlich bei einer
bitmäßigen Verlängerung des zu kodierenden Datenwortes auch die Aufstockung
der Bitlänge der für die Kodierung verwendeten Sequenzen vorzusehen (vgl. beispielsweise NK6, Figur 14.8 i. V. m. Seite 419, Gleichung 18: Sequenzen der Länge 8 (siehe Matrix) zur Kodierung eines 4 bit Datenwortes („u0 u1 u2 u3“) und NK5,
Figur 3 i. V. m. Seite 2127, Gleichung 3: Sequenzen der Länge 16 (siehe Matrix)
zur Kodierung eines 5 bit Datenwortes (dort: „m0 m4 m3 m2 m1“)), so dass der
Fachmann auch keinerlei Veranlassung hatte, in der patentgemäßen Weise vorzugehen.

                                      - 33 -



Auch die übrigen im Verfahren befindlichen Druckschriften sind zur Überzeugung
des Senats nicht geeignet, dem Fachmann den Gegenstand nach dem Patentanspruch 1 gemäß Hilfsantrag A nahe zu legen. Die zu berücksichtigenden Druckschriften zeigen nur Spezialfälle und Teilaspekte von mathematischen Kodierungsvorschriften oder Operationen (NK7, NK17, NK24-OJ4, NK24-OJ7, NK27-
OJ12, NK29, NK30) und Kodierern (NK11, NK13, NK18, NK27-OJ16) in meist
sehr allgemein gehaltener Form, die nicht einmal in Ansätzen der Kodiererstruktur
oder einem Kodierungsablauf gemäß der Druckschriften NK5 oder NK6 ähneln
oder auch Anwendungsgebiete aufzeigen, die einen Fachmann dazu veranlassen
würden, die genannten Strukturen entsprechend - mittels aus diesen gewonnener
neuer Information - wie beansprucht zu modifizieren.


Folglich ist der Gegenstand des Patentanspruchs 1, so wie er mit dem Hilfsantrag A verteidigt wird, sowohl neu als auch erfinderisch gegenüber dem im Verfahren befindlichen Stand der Technik und damit patentfähig.


5.4. Gegen den neuen, nun nebengeordneten, Patentanspruch 2, dessen Nebenordnung sich aus einer notwendigen Aufhebung des bisherigen Rückbezugs auf
einen allgemeiner gehaltenen übergeordneten Anspruch ergibt, und der im Wesentlichen nur dadurch vom Patentanspruch 1 gemäß Hilfsantrag A abweicht,
dass er eine Punktierung von Bits durch die Sequenzgeneratoren in den aus dem
Patentanspruch 1 bekannten Basissequenzen vorsieht, bestehen hinsichtlich Zulässigkeit und Patentfähigkeit - mit gleicher Begründung wie für den Anspruch 1
ausgeführt - ebenfalls keine Bedenken.


Gleiches gilt für die sich hieran anschließenden Unteransprüche.

                                          - 34 -



                                           II.


Es entspricht dem Verhältnis des anteiligen Obsiegens und Unterliegens, dass die
Kosten des Rechtsstreits gegeneinander aufzuheben sind (§ 84 Abs. 2 PatG
i. V. m. § 92 Abs. 1 ZPO). Die Entscheidung über die vorläufige Vollstreckbarkeit
beruht auf § 99 Abs. 1 PatG i. V. m. § 709 ZPO.


                                           III.


                                 Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet und innerhalb     eines    Monats        beim     Bundesgerichtshof,        Herrenstraße 45a,
76133 Karlsruhe eingereicht werden.


Sie kann auch als elektronisches Dokument eingereicht werden (§ 125a Absatz 2
des Patentgesetzes in Verbindung mit der Verordnung über den elektronischen
Rechtsverkehr       beim         Bundesgerichtshof       und     Bundespatentgericht
(BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130). In diesem Fall muss
die Einreichung durch die Übertragung des elektronischen Dokuments in die elektronische   Poststelle     des     Bundesgerichtshofes     erfolgen     (§ 2   Absatz 2
BGH/BPatGERVV).


Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht. Die Frist kann nicht verlängert werden.

                                     - 35 -



Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung
gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteils Berufung
eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Gutermuth         Martens        Gottstein       Kleinschmidt        Dr. Wollny




                                                                              Pü
