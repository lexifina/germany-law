---
ecli: "ECLI:DE:BPatG:2014:070514U5Ni51.11EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 51/11"
decided: "2014-05-07"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=26&nr=26205&anz=1119&pos=398&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2014-05-07_5_Ni_51_11_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 51/11 vom 2014-05-07

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      Verkündet am
                                                       7. Mai 2014
5 Ni 51/11 (EP)                                            …

(Aktenzeichen)


                     In der Patentnichtigkeitssache

 …




 BPatG 253
 08.05

                                           -2-



                    betreffend das europäische Patent 1 114 528
                                   (DE 600 28 525)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 7. Mai 2014 durch den Vorsitzenden Richter
Gutermuth,    die    Richterin   Martens   sowie    die   Richter   Dipl.-Ing. Gottstein,
Dipl.-Ing. Kleinschmidt und Dipl.-Geophys. Dr. Wollny


für Recht erkannt:


        I.   Das europäische Patent 1 114 528 wird mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt, soweit es über folgende Fassung der Patentansprüche 1
             bis 9 und 11 hinausgeht:


             1. A uplink transmitting device for a mobile communication
                system, comprising:
                      an encoder (110) for receiving an information bit
                      stream and for outputting three streams, a systematic
                      symbol stream (Xk), a first parity symbol stream (Yk),
                      and a second parity symbol stream (Zk) by encoding
                      the information bit stream;
                      an interleaver (120) for interleaving the three streams
                      of encoded symbols with each other by a predetermined interleaving rule and for outputting an interleaved stream;
                      wherein the interleaver is adapted to interleave the encoded streams at a transmission time interval after inserting filler bits into the encoded streams in order to
                      equalize the size of the at least one radio frame;

                           -3-



       a radio frame segmenter (130) for receiving the interleaved stream and mapping the received stream onto
       at least one radio frame;
       a demultiplexer (141); and
       a rate matcher (143, 144) adapted to puncture a part
       of the first and second parity symbols according to a
       given rate matching rule.


2. The transmitting device of claim 1, wherein when a transmission time interval is longer than 10 ms, the interleaved
   stream is mapped onto at least one radio frame.


3. The transmitting device of claim 1, wherein the transmission time interval is one of 10, 20, 40 and 80 ms.


4. The transmitting device of any of claims 1 to 3, wherein
   the interleaving rule is a bit reverse method.


5. The transmitting device of any of claims 1 to 4, wherein an
   arrangement of systematic symbols and parity symbols in
   each of the at least one radio frames has a regular pattern.


6. The transmitting device of any of claims 1 to 5, wherein
   the at least one radio frame has an initial symbol determined by the transmission time interval.

                               -4-



   7. The transmitting device of claim 1, wherein the demultiplexer is further adapted to separate symbols of the radio
       frame into the systematic symbols, the first parity symbols
       and the second parity symbols according to a regular pattern corresponding to the at least one radio frame.


   8. The transmitting device of claim 1, further comprising:
           a memory for storing initial symbols of the at least one
           radio frame, and
           a controller for controlling the demultiplexer according
           to the regular pattern and the stored initial symbol of
           the at least one radio frame.


   9. The transmitting device of claim 8, further comprising:
           a multiplexer for multiplexing the outputs of the rate
           matcher under control of the controller.


   11. The transmitting device of any of claims 1 to 9, wherein
       the rate matcher comprises:
           a first component rate matcher for rate-matching the
           systematic symbols;
           a second component rate matcher for rate-matching
           the first parity symbols; and
           a third component rate matcher for rate-matching the
           second parity symbols.


II. Im Übrigen wird die Klage abgewiesen.


III. Von den Kosten des Rechtsstreits tragen die Klägerin 1/3 und
   die Beklagte 2/3.

                                       -5-



        IV. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
            des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.


                                 Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 1 114 528
(Streitpatent), das am 8. Juli 2000 angemeldet wurde und in der Verfahrenssprache die Bezeichnung „APPARATUS AND METHOD FOR CONTROLLING A DE-MULTIPLEXER AND A MULTIPLEXER USED FOR RATE MATCHING IN A MO-BILE COMMUNICATION SYSTEM“ trägt. Das Streitpatent nimmt die Prioritäten
dreier koreanischer Anmeldungen (KR 9927407 vom 8. Juli 1999, KR 9930095
vom 23. Juli 1999 sowie KR 9937496 vom 30. August 1999) in Anspruch. Es wird
vom Deutschen Patent- und Markenamt unter dem Aktenzeichen 600 28 525.1 geführt und umfasst 48 Patentansprüche, die alle mit der Nichtigkeitsklage angegriffen sind.


Die unabhängigen Patentansprüche 1, 12, 23, 31 und 42 haben nach der Streitpatentschrift EP 1 114 528 B1 in der Verfahrenssprache folgenden Wortlaut:

                                         -6-



Patentanspruch 1:


       „1. A uplink transmitting device for a mobile communication system, comprising:
             an encoder (110) for receiving an information bit stream and
             for    outputting   three   streams,   a   systematic   symbol
             stream (Xk), a first parity symbol stream (Yk), and a second
             parity symbol stream (Zk) by encoding the information bit
             stream;
             an interleaver (120) for interleaving the three streams of encoded symbols with each other by a predetermined interleaving rule and for outputting an interleaved stream;
             a radio frame segmenter (130) for receiving the interleaved
             stream and mapping the received stream onto at least one
             radio frame;
             a demultiplexer (141); and
             a rate matcher (143, 144) adapted to puncture a part of the
             first and second parity symbols according to a given rate
             matching rule.“


Patentanspruch 12:


       „12. A transmitting device for a mobile communication system,
            comprising:
             an encoder (110) for receiving an information bit stream with
             a predetermined transmission time interval and for outputting a systematic symbol stream and at least one kind of
             parity symbol stream by encoding the information bit stream
             in accordance with a coding rate of said encoder;
             an interleaver (120) for receiving the stream of systematic
             symbols and the stream of parity symbols from the encoder,
             interleaving the stream of systematic symbols and the

                                        -7-



             stream of parity symbols with each other and outputting an
             interleaved stream;
             a radio frame segmenter (130) for receiving the interleaved
             stream from the interleaver, dividing the received stream
             into at least one radio frame and outputting the at least one
             radio frame;
             a demultiplexer (141) for receiving the at least one radio
             frame and for demultiplexing the received at least one radio
             frame into systematic symbol stream and at least one kind
             of parity symbol stream; and
             a rate matcher (143, 144) for rate matching said streams received from the demultiplexer an outputting rate matched
             streams, said rate matcher having at least one component
             rate matcher for rate matching a part of the parity symbol
             stream, the number of the component rate matcher being
             equal to the number of the parity symbol streams,
             wherein the demultiplexer switches each of the parity symbols in the radio frames to said component rate matcher
             corresponding to each parity symbol stream.“


Patentanspruch 23:


       „23. A method of transmitting for a mobile communication system,
            the method comprising the steps of:
             receiving an information bit stream transmitted at a predetermined transmission time interval;
             encoding the information bit stream and outputting a systematic symbol stream and at least one kind of parity symbol
             stream corresponding to the information bit stream, the
             number of the parity symbol streams corresponding to a coding rate of an encoder;

                                      -8-



             interleaving the systematic symbol stream and the at least
             one parity symbol stream with each other and outputting an
             interleaved stream;
             dividing the interleaved stream into at least one radio frame
             and outputting the at least one frame, each of the at least
             one radio frames having a predetermined time frame,
             demultiplexing the received at least one radio frame into a
             systematic symbol stream and at least one kind of parity
             symbol stream; and
             rate matching the demultiplexed streams by a rate matcher,
             wherein each of parity symbols in the at least one radio
             frame are switched to a component rate matcher corresponding to each parity symbol stream, said rate matcher having
             at least one component rate matcher for rate matching a
             part of said parity symbol stream, the number of component
             rate matcher being equal to the number of the parity symbol
             streams.“


Patentanspruch 31:


       „31. A transmitting device for a mobile communication system,
            comprising:
             an encoder (110) for receiving an information bit stream at a
             predetermined transmission time interval and for encoding
             and outputting a systematic symbol stream and at least one
             kind of parity symbol stream corresponding to the information bit stream in accordance with a coding rate of said encoder;
             an interleaver (120) for interleaving the systematic symbol
             stream and the parity symbol stream with each other and
             outputting an interleaved stream;

                                      -9-



             a demultiplexer (141) for receiving the interleaved stream
             and demultiplexing the received stream into a systematic
             stream and at least one kind of parity stream; and
             a rate matcher (143,144) for rate matching said streams,
             said rate matcher having at least one component rate matcher for rate matching a part of the parity stream and the
             number of the component rate matches being equal to the
             number of the parity streams,
             wherein the demultiplexer switches each of the symbols in
             the interleaved stream to a component rate matcher corresponding to each parity stream.“


Patentanspruch 42:


       „42. A method of transmitting for a mobile communication system,
            the method comprising the steps of:
             receiving an information bit stream at a predetermined
             transmission time interval;
             encoding the information bit stream and outputting a systematic symbol stream and at least one kind of parity symbol
             stream corresponding to the information bit stream in accordance with a coding rate of an encoder;
             interleaving the systematic symbol stream and the parity
             symbol stream with each other and outputting an interleaved stream;
             demultiplexing the interleaved stream into the systematic
             symbol stream and at least one kind of parity symbol
             stream; and
             rate matching the demultiplexed streams by a rate matcher,
             wherein each of parity symbols in the interleaved stream are
             switched to a component rate matcher corresponding to
             each kind of parity symbol stream, the number of compo-

                                       - 10 -



              nent rate matchers being equal to the number of the parity
              symbol streams.“


In der deutschen Übersetzung der Streitpatentschrift (EP 1 114 528 B1) lauten die
nebengeordneten Ansprüche wie folgt:


Patentanspruch 1:


       „1.   Vorrichtung zur Übertragung in Aufwärtsrichtung für ein mobiles Kommunikationssystem mit:
              einem Codierer (110) zum Empfangen eines Informationsbitstroms und zum Ausgeben von drei Strömen, einem
              systematischen Symbolstrom (Xk), einem ersten Paritätssymbolstrom (Yk)   und     einem   zweiten   Paritätssymbolstrom (Zk) durch Codieren des Informationsbitstroms;
              einem Verschachteler (120) zum Verschachteln der drei
              Ströme von codierten Symbolen miteinander mittels einer
              vorbestimmten Verschachtelungsregel und zum Ausgeben
              eines verschachtelten Stromes;
              einem Funkrahmensegmentierer (130) zum Empfangen des
              verschachtelten Stromes und zum Abbilden des empfangenen Stromes auf mindestens einen Funkrahmen;
              einem Demultiplexer (141); und
              einem Ratenabstimmer (143, 144) zum Punktieren von einem Teil der ersten und zweiten Paritätssymbole entsprechend einer vorgegebenen Ratenabstimmungsregel.“

                                    - 11 -



Patentanspruch 12:


       „12. Eine Übertragungsvorrichtung für ein mobiles Kommunikationssystem mit:
             einem Codierer (110) zum Empfangen eines Informationsbitstroms mit einem vorbestimmten Übertragungszeitintervall und zum Ausgeben eines systematischen Symbolstroms und mindestens einer Art von Paritätssymbolstrom
             mittels Codieren des Informationsbitstroms in Übereinstimmung mit einer Codierrate des Codierers;
             einem Verschachteler (120) zum Empfangen des Stroms
             von systematischen Symbolen und des Stroms von Paritätssymbolen vom Codierer, Verschachteln des Stroms von
             systematischen Symbolen und des Stroms von Paritätssymbolen miteinander und Ausgeben eines verschachtelten
             Stroms;
             einem Funkrahmensegmentierer (130) zum Empfangen des
             verschachtelten Stroms von dem Verschachteler, Teilen des
             empfangenen Stroms in mindestens einen Funkrahmen und
             Ausgeben des mindestens einen Funkrahmens;
             einem Demultiplexer (141) zum Empfangen des mindestens
             einen Funkrahmens und zum Demultiplexen des empfangenen mindestens einen Funkrahmens in einen systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom; und
             einem Ratenabstimmer (143, 144) zum Ratenabstimmen
             der von dem Demultiplexer empfangenen Ströme und zum
             Ausgeben der ratenabgestimmten Ströme, wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer zum Ratenabstimmen eines Teils des Paritätssymbolstroms aufweist, und die Anzahl des Komponentenratenabstimmers gleich der Anzahl von Paritätssymbolströmen ist,

                                     - 12 -



             wobei der Demultiplexer jeden der Paritätssymbolströme in
             den Funkrahmen zu dem Komponentenratenabstimmer
             schaltet, der jedem Paritätssymbolstrom entspricht.“


Patentanspruch 23:


       „23. Übertragungsverfahren für ein mobiles Kommunikationssystem mit den Schritten:
             Empfangen eines Informationsbitstroms, der zu einem bestimmten Übertragungszeitintervall gesendet wird;
             Codieren des Informationsbitstroms und Ausgeben eines
             systematischen Symbolstroms und mindestens einer Art
             von Paritätssymbolstrom entsprechend dem Informationsbitstroms, wobei die Anzahl der Paritätssymbolströme einer
             Codierrate eines Codierers entspricht;
             Verschachteln des systematischen Symbolstroms und des
             mindestens einen Paritätssymbolstroms miteinander und
             Ausgeben eines verschachtelten Stromes;
             Teilen des verschachtelten Stroms in mindestens einen
             Funkrahmen und Ausgabe des mindestens einen Funkrahmens, wobei jeder der mindestens einen Funkrahmen einen
             vorbestimmten Zeitrahmen aufweist;
             Demultiplexen des empfangenen mindestens einen Funkrahmens in einen systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom; und
             Ratenabstimmen der demultiplexten Ströme mittels eines
             Ratenabstimmers,
             wobei jeder der Paritätssymbole in dem mindestens einen
             Funkrahmen zu einem Komponentenratenabstimmer geschaltet wird, entsprechend jedem Paritätssymbolstrom, wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer zum Ratenabstimmen eines Teils des Pari-

                                    - 13 -



             tätssymbolstroms aufweist, und die Anzahl des Komponentenratenabstimmers gleich der Anzahl der Paritätssymbolströme ist.“


Patentanspruch 31:


       „31. Übertragungsvorrichtung für ein mobiles Kommunikationssystem mit:
             einem Codierer (110) zum Empfangen eines Informationsbitstroms zu einem vorbestimmten Übertragungszeitintervall
             und zum Codieren und Ausgeben eines systematischen
             Symbolstroms und mindestens einer Art von Paritätssymbolstrom entsprechend dem Informationsbitstroms in Übereinstimmung mit einer Codierrate des Codierers;
             einem Verschachteler (120) zum Verschachteln des systematischen Symbolstroms und des Paritätssymbolstroms
             miteinander und Ausgeben eines Verschachtelten Stroms;
             einem Demultiplexer (141) zum Empfangen des verschachtelten Stroms und Demultiplexen des empfangenen Stroms
             in einen systematischen Strom und mindestens eine Art von
             Paritätssymbolstrom; und
             einem Ratenabstimmer (143, 144) zum Ratenabstimmen
             der Ströme, wobei der Ratenabstimmer mindestens einen
             Komponentenratenabstimmer zum Ratenabstimmen eines
             Teils des Paritätsstroms aufweist, und die Anzahl der Komponentenratenabstimmer gleich der Anzahl der Paritätsströme ist,
             wobei der Demultiplexer jedes der Symbole in dem verschachtelten Strom zu einem Komponentenratenabstimmer
             schaltet, entsprechend jedem Paritätsstrom.“

                                     - 14 -



Patentanspruch 42:


       „42. Übertragungsverfahren für ein mobiles Kommunikationssystem mit den Schritten:
             Empfangen eines Informationsbitstroms zu einem vorbestimmten Übertragungszeitintervalls;
             Codieren des Informationsbitstroms und Ausgeben eines
             systematischen Symbolstroms und mindestens einer Art
             von Paritätssymbolstroms, entsprechend dem Informationsbitstroms in Übereinstimmung mit einer Codierrate eines
             Codierers;
             Verschachteln des systematischen Symbolstroms und des
             Paritätssymbolstroms miteinander und Ausgeben eines verschachtelten Stroms;
             Demultiplexen des verschachtelten Stroms in den systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom; und
             Ratenabstimmen der demultiplexten Ströme mittels eines
             Ratenabstimmers,
             wobei jeder der Paritätssymbole in dem verschachtelten
             Strom zu einem Komponentenratenabstimmer geschaltet
             wird, entsprechend jeder Art von Paritätssymbolstrom, und
             die Anzahl der Komponentenratenabstimmer gleich der Anzahl der Paritätssymbolströme ist.“


Wegen der auf die nebengeordneten Ansprüche jeweils direkt oder indirekt rückbezogenen Unteransprüche 2 bis 11, 13 bis 22, 24 bis 30, 32 bis 41 sowie 43 bis
48 wird auf die Streitpatentschrift (EP 1 114 528 B1) Bezug genommen.

                                        - 15 -



Die Klägerin macht mit der Nichtigkeitsklage geltend, die Gegenstände des Streitpatents    seien   gegenüber      den    ursprünglich   eingereichten     Unterlagen
(WO 01/05059 A1, vorgelegt als NK9) in mehrerer Hinsicht unzulässig erweitert
bzw. unzureichend offenbart. Dem Streitpatent, das nach Auffassung der Klägerin
die Priorität der koreanischen Anmeldung 9927407 nicht wirksam beanspruchen
könne, fehle gegenüber den Druckschriften NK6 und NK7 die Neuheit. Es sei
auch für den Fall der wirksamen Inanspruchnahme der koreanischen Priorität wegen mangelnder Patentfähigkeit zu widerrufen, da seine Gegenstände durch den
weiteren Stand der Technik dem Fachmann im maßgeblichen Zeitpunkt nahegelegt seien und somit nicht auf einer erfinderischen Tätigkeit beruhten.


Die Klägerin stützt ihr Vorbringen auf folgende Unterlagen:


          NK1        EP 1 114 528 B1 (EP-Streitpatent (SP) mit EPA-Registerauszug)
          NK2        DE 600 28 525 T2 (Dt. Übersetzung des SP mit
                     DPMA-Registerauszug)
          NK3        Merkmalstabelle der unabhängigen Ansprüche 1, 12,
                     23, 31, 42
          NK4        3GPP TS 25.212 V2.0.0 (1999-06), Technical Specification; 3rd Generation Partnership Project (3GPP);
                     Technical Specification Group (TSG) Radio Access
                     Network (RAN); Working Group 1 (WG1); Multiplexing and channel coding (FDD)
          NK5        TSGR1#4(99)467; Title: Proposal for rate matching
                     of Turbo Codes, Source: Nortel Networks,
          NK6        TSGR1#6(99)919; TSG-RAN Working Group1 meeting #6; Espoo, Finland, 13-16, July 1999, Title: Unified rate matching scheme for Turbo/ convolutional
                     codes and up/down links; Source: SAMSUNG Electronics Co, Document for: discussion & decision,

                          - 16 -



NK7      TSGR1#6(99)948; TSG-RAN Working Group1 meeting #6; Espoo, Finland, 13-16 July 1999, Title: A method to classify the interleaved symbols of 1st MIL interleaver using some property; Source: SAMSUNG
         Electronics Co, Document for: Discussion,
NK8      Beglaubigte   englischsprachige    Übersetzung     des
         Prioritätsdokuments KR 9927407
NK8E     beglaubigte vollständige deutsche Übersetzung des
         koreanischen Prioritätsdokuments,
NK9      WO 01/05 059 A1 der Anmeldung PCT/KR00/00739,
         mit markierter Version (NK9a)
NK10     US 4 317 198 A
NK11     US 5 365 519 A
NK12     F. Jordan, K.-D. Kammeyer: A Study on Iterative Decoding Techniques Applied to GSM-Full-Rate Channels, PIMRC98, vol. 3, pp. 1066-1070, 8-11 September 1998
NK13-1   ETS 300 909: Digital cellular telecommunications
         system (Phase 2+) Channel coding. GSM Recommendation 05.03, Version 5.5.1, October 1998
NK13-2   GSM full rate speech transcoding. GSM Recommendatio 06.10, January 1991
NK14     M. Sajadieh, F. R. Kschischang, A. Leon-Garcia: Modulation-Assisted Unequal Error Protection over the
         Fading Channel. IEEE Transactions on Vehicular
         Technology, vol. 47 (1998) no. 3, pp. 900-908
NK15     Deepen Sinha, Carl-Erik W. Sundberg: Unequal Error Protection (UEP) for Perceptual Audio Coders,
         presented at the 104th Convention 1998 May 16-19
         Amsterdam

                              - 17 -



NK16        Frank Burkert, Guisepp Caire, Joachim Hagenauer,
            Thomas Hindelang and Guenther Lechner: „Turbo”
            Decoding with Unequal Error Protection applied to
            GSM       speech       coding,      GLOBECOM1996,
            pages 2044-2048
NK17        A. S. Barbulescu and S. S. Pietrobon: Rate compatible turbo codes, Electronic Letters, 30th March 1995,
            Vol. 31, No. 7, pages 535-536
NK18        G. Caire and G. Lechner: Turbo codes with unequal
            error protection, Electronic Letters, 28th March 1996,
            Vol. 32, No. 7, pages 629-631
NK19        TSG S4 '3(99)71: Layer one considerations for the
            Speech services, TSG-SA Working Group 4 meeting
            #3, Yokosuka, Japan, 24thth March 1999
NK20        Berufungsbegründung vom 6. August 2012 der Patentinhaberin im parallelen Verletzungsverfahren
NK21-1      TSGR1#6(99)XXX: Fujitsu & Siemens: Universal rate
            matching algorithm for up/down-link and Turbo/convolutional coding, TSG-RAN Working Group 1 (Radio) meeting #6, Espoo, Finland, 13-16 July 1999
NK21-2      http_list.etsi.org_scripts_wa / email von
            Herrn T… an A… Gruppen 4 und 5 vom
            5. Juli 1999
NK21-3      Mailing-Liste „3GPP_TSG_RAN_WG1”
NK21-4a-e   Anlagenkonvolut dazu
NK22        R. J. Polge, B. K. Bhagavan, J. M. Carswell: Fast
            Computational Algorithms for Bit Reversal. IEEE
            Transactions on Computers, vol. C-23 (1974) no. 1,
            pp. 1-9

                        - 18 -



NK23   J. S. Walker: A New Bit Reversal Algorithm. IEEE
       Transactions on Acoustics, Speech, and Signal Processing, vol. 38 (1990) no. 8, pp. 1472-1473
NK24   P. Jung, J. Blanz: Realization of a soft output Viterbi
       equalizer using field programmable gate arrays. Proceedings of the 43rd IEEE Vehicular Technology Conference (VTC93), pp. 625-628, 18-20 May 1993
NK26   C. Berrou, A. Glavieux, P. Thitimajshima: Near Shannon limit error-correcting coding and decoding: Turbo-codes (1). Proceedings of the IEEE International
       Conference on Communications (ICC93), vol. 2,
       pp. 1064-1070, 23-26 May 1993
NK27   A. A. Barbulescu, S. S. Pietrobon: Rate compatible
       turbo codes. Electronics Letters, vol. 31 (1995),
       No. 7, pp 535-536
NK28   P. Jung, J. Plechinger, M. Doetsch, F. M. Berens: A
       pragmatic approach to rate compatible punctured
       Turbo-Codes for mobile radio applications. Proceedings of the Sixth International Conference on
       Advances in Communications and Control: Telecommunications/Signal          Processing,         Corfu,
       23-27 June 1997, pp. 545-554
NK29   P. Jung, J. Plechinger, M. Doetsch, F. Berens: Advances on the application of turbo-codes to data services in third generation mobile networks. Proceedings of the First Symposium on Turbo Codes, Brest,
       3-5 Sept. 1997, pp. 135-142
NK30   P. Jung, J. Plechinger: Performance of rate compatible punctured Turbo-codes for mobile radio applications. Electronics Letters, vol. 33 (1997), no. 25,
       pp. 2102-2103

                                     - 19 -



       NK31          G. Caire, E. Biglieri: Parallel Concatenated Codes
                     with Unequal Error Protection, IEEE Transactions on
                     Communications, vol. 46 (1998), no. 5, pp. 565-567
       NK32-1        Hann F. Najjar: Multiplexing Asynchronous Signals
                     Using Bit Stuffingand Retiming Techniques, IEEE
                     Transactions on Aerospace and Electronic Systems,
                     vol. AES-5, pp. 661-671,
       NK32-2        M. Bossert, M. Breitbach: Digitale Netze, Stuttgart,
                     B.G. Teubner 1999, Seiten 67-70
       NK32-3        A. Artom: Choice of Prefix in Self-Synchronizing
                     Codes, Paper approved by the CT-Committee of the
                     IEEE   Communications      society   for   publication,
                     received July 21. 1971
       NK33          TSGR1#6(99)yyy: Detailed descriptions of Radio
                     frame segmentation to 2nd interleaver, TSG-RAN
                     Working Group 1 meeting #6, Espoo, Finland, 13-16,
                     July 1999
       NK34          S. Le Goff, A. Glavieux, C. Berrou: TURBO-CODES
                     AND HIGH SPECTRAL EFFICIENCY MODULA-TION, IEEE 1994
       NK35          englische Übersetzung der koreanischen Anmeldung
                     9930095
       NK36          englische Übersetzung der koreanischen Anmeldung
                     9837469.


Die Klägerin beantragt,


       das europäische Patent 1 114 528 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.

                                          - 20 -



Die Beklagte beantragt,


        die Klage abzuweisen.


Hilfsweise verteidigt sie das Streitpatent in den in der mündlichen Verhandlung
vom 7. Mai 2014 überreichten Fassungen der Hilfsanträge 1 bis 3 sowie 4 und 4‘.


Mit Hilfsantrag 1 beantragt die Beklagte die Aufrechterhaltung des Streitpatents im
Umfang der Ansprüche 1 bis 5 wie erteilt, bei Streichung der Ansprüche 6 bis 48,
der Absätze [0043] bis [0046] und [0054] bis [0090] sowie der Zeichnungen 8a bis
15 der Streitpatentschrift EP 1 114 528 B1.


Patentanspruch 1 gemäß Hilfsantrag 2 lautet wie folgt (Ergänzungen gegenüber
Anspruch 1 in der erteilten Fassung sind unterstrichen):


        „1.   A uplink transmitting device for a mobile communication System, comprising:
               an encoder (110) for receiving an information bit stream and
               for   outputting   three      streams,   a   systematic   symbol
               stream (Xk), a first parity symbol stream (Yk), and a second
               parity symbol stream (Zk) by encoding the information bit
               stream;
               an interleaver (120) for interleaving the three streams of encoded symbols with each other by a predetermined interleaving rule at a transmission time interval (TTI) and for outputting an interleaved stream, in a symbol pattern of „systematic symbol – first parity symbol – second parity symbol” or in
               a symbol pattern of „systematic symbol - second parity symbol – first parity symbol”,
               wherein the transmission time interval ist TTI = 10ms,
               TT1=20ms 0r TTI = 80 ms, and

                                       - 21 -



              a radio frame segmenter (130) for receiving the interleaved
              stream and mapping the received stream onto at least one
              radio frame;
              a demultiplexer (141); for demultiplexing the at least one radio frame to the systematic symbols, the first parity symbols,
              and the second parity symbols of the radio frame; and
              a rate matcher (143,144) adapted to puncture a part of the
              first and second parity symbols according to a given rate
              matching rule.“


Diesem schließen sich die Unteransprüche 2, 4 und 5 der erteilten Fassung mit
entsprechenden Rückbezügen an; die Ansprüche 3 sowie 6 bis 48 sind ebenso
gestrichen wie die zu Hilfsantrag 1 genannten Absätze und Zeichnungen gemäß
Beschreibung. Auf den Hinweis des Vorsitzenden, dass gegen die Streichung von
Teilen der Beschreibung grundsätzliche Bedenken bestehen, hat die Beklagte erklärt, sie verteidige das Streitpatent weiter hilfsweise in einer Fassung nach Hilfsantrag 2, jedoch ohne diese Streichungen.


Hilfsantrag 3 unterscheidet sich von der zur Entscheidung gestellten Fassung
nach Hilfsantrag 2 lediglich durch die folgende Ergänzung bezüglich des interleavers (120): „wherein the interleaver is 160 bits“. Wie zu Hilfsantrag 2 ausgeführt
verteidigt die Beklagte auch hier das Streitpatent weiter hilfsweise in einer Fassung ohne Streichung von Teilen der Beschreibung.


Hilfsantrag 4 entspricht der im Tenor wiedergegebenen Fassung des Streitpatents.


Wegen des Wortlauts der mit Hilfsantrag 4‘ verteidigten Fassung des Streitpatents
wird auf das Sitzungsprotokoll Bezug genommen.

                                       - 22 -



Die Beklagte hat die Vertagung der mündlichen Verhandlung vom 7. Mai 2014 mit
der Begründung beantragt, ihr sei Gelegenheit zu geben, die Eigenschaften eines
Funkrahmensegmentierers weiter zu klären, auf die das Gericht bei seiner Entscheidung offensichtlich abstellen wolle.


Die Klägerin ist diesem Antrag der Beklagten entgegengetreten. Sie hat zudem die
Verspätung der Hilfsanträge 1 bis 3 mit der Begründung gerügt, sie könne hinsichtlich dieser geänderten Fassungen die Auswirkung auf das Verletzungsverfahren nicht absehen. Auch könne sie in der mündlichen Verhandlung zur Zulässigkeit und Patentfähigkeit dieser Fassungen nicht Stellung nehmen. Zur Aufnahme
des Unteranspruchs 10 in den Hilfsantrag 4 könne sie sich jedoch einlassen.


Die Beklagte tritt den Ausführungen der Klägerin in allen Punkten entgegen. Das
Streitpatent sei gegenüber der Anmeldung in ihrer ursprünglich eingereichten Fassung nicht unzulässig erweitert. Es offenbare die Erfindung so deutlich, dass ein
Fachmann sie ausführen könne.


Das Streitpatent könne in der erteilten Fassung wie auch in den Fassungen der
Hilfsanträge 1 bis 3 die Priorität der koreanischen Voranmeldung 9927407 vom
8. Juli 1999 wirksam beanspruchen. In allen verteidigten Fassungen gelte das
Streitpatent gegenüber dem jeweils zu berücksichtigenden Stand der Technik als
neu und sei dem Fachmann auch nicht nahe gelegt.

                                         - 23 -



Bezüglich der wirksamen Inanspruchnahme der Priorität der koreanischen Voranmeldung 9927407 stützt die Beklagte ihr Vorbringen auf folgende Unterlagen:


        NK8A koreanische Prioritätsanmeldung KR 1999-27407
        NK8B auszugsweise beglaubigte deutsche Übersetzung aus der
                koreanischen Sprache
        NK8C weitere Korrekturen zur Prioritätsanmeldung NK8 in englischer Sprache
        NK8D nach US-Recht zertifizierte Übersetzung der Prioritätsschrift ins Englische.


Der Senat hat den Antrag der Beklagten, die mündliche Verhandlung wegen der
Klärung der Eigenschaften eines Funkrahmensegmentierers zu vertagen, durch
Beschluss zurückgewiesen. Die Verteidigung des Streitpatents mit den Fassungen
der Hilfsanträge 1 bis 3 hat der Senat gemäß § 83 Abs. 4 PatG nicht zugelassen
und durch Beschluss zurückgewiesen.


Im Termin vom 5. Juni 2013 hatte der Senat beschlossen, eine vollständige
schriftliche Übersetzung der Prioritätsschrift, der koreanischen Voranmeldung 9927407 vom 8. Juli 1999, in die deutsche Sprache durch eine/n öffentlich
bestellte/n und allgemein beeidigte/n Übersetzer/in einzuholen. Daraufhin hat die
Klägerin eine entsprechende Übersetzung als Anlage NK8E (Blatt 631 der Gerichtsakte) vorgelegt, zu der die Beklagte mit Schriftsatz vom 18. März 2014 lediglich Korrekturen offensichtlicher Schreibfehler oder Ungenauigkeiten angebracht
hat.


Wegen des Vorbringens der Parteien im Übrigen wird auf die Sitzungsprotokolle
vom 5. Juni 2013 und vom 7. Mai 2014 sowie auf die gewechselten Schriftsätze
Bezug genommen.

                                        - 24 -



Der Senat hat den Parteien einen Hinweis nach § 83 PatG vom 7. März 2013
übermittelt. In seiner Einführung in den Sach- und Streitstand in der mündlichen
Verhandlung vom 7. Mai 2014 hatte der Vorsitzende u. a. darauf hingewiesen,
dass die nebengeordneten Ansprüche 31 und 42, da sie keinen Funkrahmensegmentierer beanspruchten, möglicherweise gegenüber den ursprünglichen Unterlagen (veröffentlicht als WO 01/05059 A1, vorgelegt als NK9) unzulässig erweitert
sein könnten. Die Klägerin hat hierzu auf ihren schriftsätzlichen Vortrag verwiesen;
die Beklagte hat erklärt, sie verzichte diesbezüglich ebenfalls auf weiteren Vortrag.


                          Entscheidungsgründe


Die zulässige Nichtigkeitsklage ist teilweise begründet.


In der erteilten Fassung kann das Streitpatent keinen Bestand haben. Die Gegenstände der nebengeordneten Ansprüche 1, 12 und 23 sind durch die Druckschriften NK6 bzw. NK7 neuheitsschädlich vorweggenommen (Art. 138 Abs. 1a i. V. m.,
Art. 54 EPÜ), da das Streitpatent die Priorität der koreanischen Anmeldung
9927407 nicht wirksam beansprucht. Die Gegenstände der weiteren nebengeordneten Ansprüche 31 und 42 gehen über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus und sind somit unzulässig erweitert
(Art. 138 Abs. 1c EPÜ).


Die Verteidigung des Streitpatents in den Fassungen der Hilfsanträge 1, 2 und 3
hat der Senat gemäß § 83 Abs. 4 PatG bei der Entscheidung nicht berücksichtigt.
In der Fassung nach Hilfsantrag 4 hat das Streitpatent jedoch Bestand. Insoweit
war die Nichtigkeitsklage abzuweisen.

                                     - 25 -



                   I. Das Streitpatent und seine Auslegung


1. Das Streitpatent EP 1 114 528 B1 (NK1) befasst sich mit der Ratenabstimmung
eines kanalcodierten Signals und insbesondere mit einer Vorrichtung zum Steuern
eines Demultiplexers (DEMUX) und eines Multiplexers (MUX) im Rahmen einer
Ratenabstimmung im Mobilfunkkontext (NK1, Absätze [0001] bis [0003]).


Allgemein nähmen Funkkommunikationssysteme eine Kanalcodierung der Quellbenutzerdaten mit einem Fehlerkorrekturcode vor der Übertragung vor, um die
Systemzuverlässigkeit zu erhöhen. Typische für die Kanalcodierung verwendete
Codes seien Faltungs- und Linearblockcodes, für die ein einzelner Decodierer verwendet werde. Auch so genannte Turbocodes seien hierfür vorgeschlagen. Ein
Kommunikationssystem mit mehrfachen Zugriffen und mehrfachen Kanälen stimme die Anzahl der kanalcodierten Symbole auf eine bestimmte Anzahl von Übertragungsdatensymbolen ab, um die Effizienz und die Systemleistung der Datenübertragung zu erhöhen. Diese Operation werde als Ratenabstimmung bezeichnet. Als Abstimmungsmaßnahmen kämen häufig Punktierung und Wiederholung
von Bits zum Einsatz.


Laut Stand der Technik empfange ein Kanalcodierer im Vorfeld der Ratenabstimmung zunächst Rahmendaten mit vorbestimmten TTIs (Transmission Time Intervals = Übertragungszeitintervalle) und codiere diese. Die codierten Symbole gebe
er dann in Übereinstimmung mit einer vorbestimmten Codierrate aus. Die Größe
der Rahmendaten entspreche der Anzahl der Informationsbits. Ein erster Verschachteler verschachtele dann die Ausgabe des Kanalcodierers, bevor ein Funkrahmen-Segmentierer die verschachtelten Symbole zu Funkrahmenblöcken segmentiere. Anschließend stimme ein Ratenabstimmer die Datenrate eines Funkrahmens dergestalt auf eine vorbestimmte Datenrate ab, dass er die Symbole des
Funkrahmens punktiere oder wiederhole. Ein MUX multiplexe in Folge die ratenabgestimmten Funkrahmen. Ein physikalischer Kanal-Segmentierer segmentiere
die nun gemultiplexten Funkrahmen zu physikalischen Kanalblöcken. Ein zweiter
Verschachteler verschachtele in Folge die physikalischen Kanalblöcke und ein

                                       - 26 -



physikalischer Kanal-Abbilder bilde die zum zweiten Mal verschachtelten Blöcke
auf physikalischen Kanälen für die Übertragung ab. Eine UMTS-Aufwärtsverbindungs-Übertragungsvorrichtung beinhalte Ratenabstimmer, die in ihrer Konfiguration in Abhängigkeit davon variierten, ob der Kanalcodierer ein Faltungscodierer
oder ein Turbocodierer sei, wofür verschiedene Vorschläge zur Umsetzung existierten (NK1, Absatz [0005] bis Absatz [0007]).


Hierbei sei es wesentlich, zwischen den Informationssymbolen und den Paritätssymbolen in den codierten Symbolen zu unterscheiden, um eine optimale Ratenabstimmung zu erreichen. Eine Verarbeitung wie etwa eine Kanalverschachtelung
könne zwischen dem Turbocodierer und einem Ratenabstimmer eingefügt werden. Trotzdem sollte die Unterscheidung zwischen Informationssymbolen und Paritätssymbolen aufrechterhalten werden. Dies sei bisher jedoch unmöglich, weil alle kanalcodierten Symbole nach der Kanal-Verschachtelung bisher willkürlich gemischt würden (NK1, Absatz [0009] bis Absatz [0012]).


Aus dieser Sachlage ergäbe sich die Aufgabe, eine Vorrichtung und ein Verfahren
für eine verbesserte Ratenabstimmung in einer Multiplex- und Kanalcodierungskette eines mobilen Kommunikationssystems anzugeben, das auch eine verbesserte Leistungsfähigkeit des Verschachtelers aufweise. Auch würden eine Vorrichtung und ein Verfahren zum Anordnen eines DEMUX vor einem Ratenabstimmer
angegeben, um die Symboldaten in Informationssymbole und Paritätssymbole zu
trennen, ferner eine weitere Vorrichtung und ein weiteres Verfahren zum Steuern
eines DEMUX und eines MUX für die Verwendung bei der Ratenabstimmung in einer Aufwärtsverbindungs-Übertragungsvorrichtung, sowie eine Vorrichtung und
ein Verfahren zum Steuern eines DEMUX und eines MUX für die Verwendung bei
der Ratenabstimmung eines turbocodierten Signals in einer Aufwärtsverbindungs-Übertragungsvorrichtung (NK1, Absatz [0013] bis Absatz [0017]).

                                          - 27 -



Die Vorrichtung zur Übertragung in Aufwärtsrichtung für ein mobiles Kommunikationssystem, gemäß erteiltem Patentanspruch 1, lässt sich in folgende Merkmale
gliedern:


Englische Version:


        1.1 A[n] uplink transmitting device for a mobile communication
             system, comprising.
        1.2 an encoder (110)
             1.2.1 for receiving an information bit stream and
             1.2.2 for outputting three streams, a systematic symbol
                     stream (Xk), a first parity symbol stream (Yk), and a second parity symbol stream (Zk) by encoding the information bit stream,
        1.3 an interleaver (120)
             1.3.1 for interleaving the three streams of encoded symbols
                     with each other by a predetermined interleaving rule
                     and
             1.3.2 for outputting an interleaved stream,
        1.4 a radio frame segmenter (130)
             1.4.1 for receiving the interleaved stream and
             1.4.2 mapping the received stream onto at least one radio
                     frame,
        1.5 a demultiplexer (141), and
        1.6 a rate matcher (143,144)
             1.6.1 adapted to puncture a part of the first and second parity symbols
             1.6.2 according to a given rate matching rule.

                                        - 28 -



Deutsche Version:


       1.1 Vorrichtung zur Übertragung in Aufwärtsrichtung für ein mobiles Kommunikationssystem mit.
       1.2 einem Codierer (110)
            1.2.1 zum Empfangen eines Informationsbitstroms und
            1.2.2 zum Ausgeben von drei Strömen, einem systematischen Symbolstrom (Xk), einem ersten Paritätssymbolstrom (Yk) und einem zweiten Paritätssymbolstrom (Zk) durch Codieren des Informationsbitstroms,
       1.3 einem Verschachteler (120)
            1.3.1 zum Verschachteln der drei Ströme von codierten
                    Symbolen miteinander mittels einer vorbestimmten
                    Verschachtelungsregel und
            1.3.2 zum Ausgeben eines verschachtelten Stromes,
       1.4 einem Funkrahmensegmentierer (130)
            1.4.1 zum Empfangen des verschachtelten Stromes und
            1.4.2 zum Abbilden des empfangenen Stromes auf mindestens einen Funkrahmen,
       1.5 einem Demultiplexer (141), und
       1.6 einem Ratenabstimmer (143,144)
            1.6.1 zum Punktieren von einem Teil der ersten und zweiten
                    Paritätssymbole
            1.6.2 entsprechend        einer      vorgegebenen   Ratenabstimmungsregel.

                                      - 29 -



Die Übertragungsvorrichtung für ein mobiles Kommunikationssystem, gemäß erteiltem Patentanspruch 12, lässt sich in folgende Merkmale gliedern:


Englische Version:


       12.1 A transmitting device for a mobile communication system,
             comprising.
       12.2 an encoder (110)
             12.2.1 for receiving an information bit stream with a predetermined transmission time interval and
             12.2.2 for outputting a systematic symbol stream and
             12.2.3 at least one kind of parity symbol stream by encoding
                     the information bit stream in accordance with a coding rate of said encoder,
       12.3 an interleaver (120)
             12.3.1 for receiving the stream of systematic symbols and
                     the stream of parity symbols from the encoder,
             12.3.2 interleaving the stream of systematic symbols and
                     the stream of parity symbols with each other, and
             12.3.3 outputting an interleaved stream,
       12.4 a radio frame segmenter (130)
             12.4.1 for receiving the interleaved stream from the interleaver,
             12.4.2 dividing the received stream into at least one radio
                     frame
             12.4.3 and outputting the at least one radio frame,
       12.5 a demultiplexer (141),
             12.5.1 for receiving the at least one radio frame and
             12.5.2 for demultiplexing the received at least one radio
                     frame into systematic symbol stream and at least
                     one kind of parity symbol stream

                                       - 30 -



       12.6 a rate matcher (143,144)
            12.6.1 for rate matching said streams received from the demultiplexer and
            12.6.2 outputting rate matched streams
            12.6.3 said rate matcher having at least one component
                    rate matcher for rate matching a part of the parity
                    symbol stream.
            12.6.4 the number of the component rate matcher being
                    equal to the number of the parity symbol streams,
            12.6.5 wherein the demultiplexer switches each of the parity
                    symbols in the radio frames to said component rate
                    matcher corresponding to each parity symbol stream.


Deutsche Version:


       12.1 Eine Übertragungsvorrichtung für ein mobiles Kommunikationssystem mit.
       12.2 einem Codierer (110)
            12.2.1 zum Empfangen eines Informationsbitstroms mit einem vorbestimmten Übertragungszeitintervall und
            12.2.2 zum Ausgeben eines systematischen Symbolstroms
                    und
            12.2.3 mindestens einer Art von Paritätssymbolstrom mittels
                    Codieren des Informationsbitstroms in Übereinstimmung mit einer Codierrate des Codierers,

                             - 31 -



12.3 einem Verschachteler (120)
     12.3.1 zum Empfangen des Stroms von systematischen
            Symbolen und des Stroms von Paritätssymbolen
            vom Codierer,
     12.3.2 Verschachteln des Stroms von systematischen Symbolen und des Stroms von Paritätssymbolen miteinander und
     12.3.3 Ausgeben eines verschachtelten Stroms,
12.4 einem Funkrahmensegmentierer (130)
     12.4.1 zum Empfangen des verschachtelten Stroms von
            dem Verschachteler,
     12.4.2 Teilen des empfangenen Stroms in mindestens einen Funkrahmen und
     12.4.3 Ausgeben des mindestens einen Funkrahmens,
12.5 einem Demultiplexer (141),
     12.5.1 zum Empfangen des mindestens einen Funkrahmens und
     12.5.2 zum Demultiplexen des empfangenen mindestens einen Funkrahmens in einen systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom, und
12.6 einem Ratenabstimmer (143,144)
     12.6.1 zum Ratenabstimmen der von dem Demultiplexer
            empfangenen Ströme und
     12.6.2 zum Ausgeben der ratenabgestimmten Ströme
     12.6.3 wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer zum Ratenabstimmen eines Teils des Paritätssymbolstroms aufweist, und
     12.6.4 die Anzahl des Komponentenratenabstimmers gleich
            der Anzahl von Paritätssymbolströmen ist,

                                         - 32 -



              12.6.5 wobei der Demultiplexer jeden der Paritätssymbolströme in den Funkrahmen zu dem Komponentenratenabstimmer schaltet, der jedem Paritätssymbolstrom entspricht.


Das Übertragungsverfahren für ein mobiles Kommunikationssystem gemäß erteiltem Patentanspruch 23, lässt sich in folgende Merkmale gliedern:


Englische Version:


       23.1     A method of transmitting for a mobile communication system, the method comprising the steps of.
       23.2     receiving an information bit stream transmitted at a predetermined transmission time interval,
       23.3     encoding the information bit stream
       23.4     and outputting a systematic symbol stream and
       23.5     at least one kind of parity symbol stream corresponding to
                the information bit stream,
       23.6     the number of the parity symbol streams corresponding to
                a coding rate of an encoder,
       23.7     interleaving the systematic symbol stream and the at least
                one parity symbol stream with each other and
       23.8     outputting an interleaved stream,
       23.9     dividing the interleaved stream into at least one radio
                frame and
       23.10    outputting the at least one frame,
       23.11    each of the at least one radio frames having a predetermined time frame,
       23.12    demultiplexing the received at least one radio frame into a
                systematic symbol stream and at least one kind of parity
                symbol stream,

                                      - 33 -



       23.13   and rate matching the demultiplexed streams by a rate
               matcher,
       23.14   wherein each of parity symbols in the at least one radio
               frame are switched to a component rate matcher corresponding to each parity symbol stream,
       23.15   said rate matcher having at least one component rate
               matcher for rate matching a part of said parity symbol
               stream,
       23.16   the number of component rate matcher being equal to the
               number of the parity symbol streams.


Deutsche Version:


       23.1    Übertragungsverfahren für ein mobiles Kommunikationssystem mit den Schritten.
       23.2    Empfangen eines Informationsbitstroms, der zu einem bestimmten Übertragungszeitintervall gesendet wird,
       23.3    Codieren des Informationsbitstroms
       23.4    und Ausgeben eines systematischen Symbolstroms und
       23.5    mindestens einer Art von Paritätssymbolstrom entsprechend dem Informationsbitstroms, [sic!]
       23.6    wobei die Anzahl der Paritätssymbolströme einer Codierrate eines Codierers entspricht,
       23.7    Verschachteln des systematischen Symbolstroms und des
               mindestens einen Paritätssymbolstroms miteinander und
       23.8    Ausgeben eines verschachtelten Stromes,
       23.9    Teilen des verschachtelten Stroms in mindestens einen
               Funkrahmen und
       23.10   Ausgabe des mindestens einen Funkrahmens
       23.11   wobei jeder der mindestens einen Funkrahmen einen vorbestimmten Zeitrahmen aufweist,

                                       - 34 -



       23.12   Demultiplexen des empfangenen mindestens einen Funkrahmens in einen systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom,
       23.13   und Ratenabstimmen der demultiplexten Ströme mittels
               eines Ratenabstimmers,
       23.14   wobei jeder der Paritätssymbole in dem mindestens einen
               Funkrahmen zu einem Komponentenratenabstimmer geschaltet wird, entsprechend jedem Paritätssymbolstrom,
       23.15   wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer zum Ratenabstimmen eines Teils des
               Paritätssymbolstroms aufweist,
       23.16   und die Anzahl des Komponentenratenabstimmers gleich
               der Anzahl der Paritätssymbolströme ist.


Die Übertragungsvorrichtung für ein mobiles Kommunikationssystem, gemäß erteiltem Patentanspruch 31, lässt sich in folgende Merkmale gliedern:


Englische Version:


       31.1 A transmitting device for a mobile communication system,
             comprising.
       31.2 an encoder (110)
             31.2.1 for receiving an information bit stream at a predetermined transmission time interval and
             31.2.2 for encoding and
             31.2.3 outputting a systematic symbol stream and at least
                     one kind of parity symbol stream corresponding to
                     the information bit stream in accordance with a coding rate of said encoder,

                                       - 35 -



       31.3 an interleaver (120)
            31.3.1 for interleaving the systematic symbol stream and
                     the parity symbol stream with each other and
            31.3.2 outputting an interleaved stream,
       31.4 a demultiplexer (141)
            31.4.1 for receiving the interleaved stream and
            31.4.2 demultiplexing the received stream into a systematic
                     stream and at least one kind of parity stream, and
       31.5 a rate matcher (143,144)
            31.5.1 for rate matching said streams,
            31.5.2 said rate matcher having at least one component
                     rate matcher
                     31.5.2.1 for rate matching a part of the parity stream
                     31.5.2.2 and the number of the component rate
                              matches being equal to the number of the
                              parity streams,
            31.5.3 wherein the demultiplexer switches each of the symbols in the interleaved stream to a component rate
                    matcher corresponding to each parity stream.


Deutsche Version:


       31.1 Übertragungsvorrichtung für ein mobiles Kommunikationssystem mit.
       31.2 einem Codierer (110)
            31.2.1 zum Empfangen eines Informationsbitstroms zu einem vorbestimmten Übertragungszeitintervall und
            31.2.2 zum Codieren und
            31.2.3 Ausgeben eines systematischen Symbolstroms und
                     mindestens einer Art von Paritätssymbolstrom entsprechend dem Informationsbitstroms [sic!] in Übereinstimmung mit einer Codierrate des Codierers,

                               - 36 -



31.3 einem Verschachteler (120)
     31.3.1 zum Verschachteln des systematischen Symbolstroms und des Paritätssymbolstroms miteinander
            und
     31.3.2 Ausgeben eines verschachtelten Stroms,
31.4 einem Demultiplexer (141)
     31.4.1 zum Empfangen des verschachtelten Stroms und
     31.4.2 Demultiplexen des empfangenen Stroms in einen
            systematischen Strom und mindestens eine Art von
            Paritätssymbolstrom, und
31.5 einem Ratenabstimmer (143, 144)
     31.5.1 zum Ratenabstimmen der Ströme,
     31.5.2 wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer
            31.5.2.1 zum Ratenabstimmen eines Teils des Paritätsstroms aufweist,
            31.5.2.2 und die Anzahl der Komponentenratenabstimmer gleich der Anzahl der Paritätsströme ist,
     31.5.3 wobei der Demultiplexer jedes der Symbole in dem
            verschachtelten Strom zu einem Komponentenratenabstimmer schaltet, entsprechend jedem Paritätsstrom.

                                      - 37 -



Das Übertragungsverfahren für ein mobiles Kommunikationssystem gemäß erteiltem Patentanspruch 42, lässt sich in folgende Merkmale gliedern:


Englische Version:


       42.1    A method of transmitting for a mobile communication system, the method comprising the steps of.
       42.2    receiving an information bit stream at a predetermined
               transmission time interval,
       42.3    encoding the information bit stream and
       42.4    outputting a systematic symbol stream and
       42.5    at least one kind of parity symbol stream corresponding to
               the information bit stream in accordance with a coding rate
               of an encoder,
       42.6    interleaving the systematic symbol stream and the parity
               symbol stream with each other and
       42.7    outputting an interleaved stream,
       42.8    demultiplexing the interleaved stream into the systematic
               symbol stream and at least one kind of parity symbol
               stream, and
       42.9    rate matching the demultiplexed streams by a rate
               matcher,
       42.10   wherein each of parity symbols in the interleaved stream
               are switched to a component rate matcher
       42.11   corresponding to each kind of parity symbol stream,
       42.12   the number of component rate matchers being equal to
               the number of the parity symbol streams.

                                      - 38 -



Deutsche Version:


       42.1    Übertragungsverfahren für ein mobiles Kommunikationssystem mit den Schritten.
       42.2    Empfangen eines Informationsbitstroms zu einem vorbestimmten Übertragungszeitintervalls [sic!],
       42.3    Codieren des Informationsbitstroms und
       42.4    Ausgeben eines systematischen Symbolstroms und
       42.5    mindestens einer Art von Paritätssymbolstroms, entsprechend dem Informationsbitstroms in Übereinstimmung mit
               einer Codierrate eines Codierers, [sic!]
       42.6    Verschachteln des systematischen Symbolstroms und des
               Paritätssymbolstroms miteinander und
       42.7    Ausgeben eines verschachtelten Stroms,
       42.8    Demultiplexen des verschachtelten Stroms in den systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom, und
       42.9    Ratenabstimmen der demultiplexten Ströme mittels eines
               Ratenabstimmers,
       42.10   wobei jeder der Paritätssymbole [sic!] in dem verschachtelten Strom zu einem Komponentenratenabstimmer geschaltet wird,
       42.11   entsprechend jeder Art von Paritätssymbolstrom, und
       42.12   die Anzahl der Komponentenratenabstimmer gleich der
               Anzahl der Paritätssymbolströme ist.


2. Der Gegenstand des Streitpatents richtet sich nach übereinstimmender Auffassung des Senats und der Parteien an einen Diplomingenieur der Nachrichtentechnik oder Informatik mit Universitätsabschluss, der mehrjährige Erfahrung auf dem
Gebiet der Datenübertragung in digitalen Mobilfunknetzen besitzt.

                                       - 39 -



3. Ausgehend vom Fach- und Erfahrungswissen dieses Fachmanns sind einige
der in den Anspruchsfassungen gemäß Streitpatent enthaltenen Begrifflichkeiten
erläuterungsbedürftig. Der Senat legt den nachfolgenden Begrifflichkeiten folgendes Verständnis zu Grunde:


Ein mobile communication system / mobiles Kommunikationssystem ist im Sinne
des Streitpatents ein Telekommunikationssystem mit mobilen Endgeräten, das in
einem digitalen Telekommunikationsnetz digitale Daten absetzen und empfangen
kann. In einem solchen Telekommunikationsnetz müssen durch ein mobiles Telekommunikationssystem zu versendende Daten im Vorfeld aufbereitet werden, damit sie gültigen Übertragungsstandards und weiteren Randbedingungen genügen.
Dabei kommt eine Vielzahl von Datenverarbeitungsmaßnahmen und/oder –bausteinen zum Einsatz.


So z. B. ein encoder / Codierer, der einen information bit stream / Informationsbitstrom, z. B. ein aus einer Abfolge von digitalen Symbolen/Datenworten bestehendes Nutzsignal, wie das Sprechsignal eines Handy-Nutzers, in ein Datenformat - im Sinne des Streitpatents für einen Übertragungskanal - umwandelt, das
fehlerunempfindlicher ist als das des Informationsbitstroms; dabei arbeitet der Codierer gemäß einer festgelegten Kodiervorschrift, damit der Decodierer auf der
Empfängerseite das Signal in das ursprüngliche Format zurückkonvertieren kann.
Der Ausdruck coding rate / Codierrate wird im Streitpatent in der üblichen fachmännischen Weise verwendet, ebenso wie die Begriffe Multiplexer / Demultiplexer, systematic symbol stream / systematischer Symbolstrom, parity symbol
stream / Paritätssymbolstrom, wie auch interleaver / Verschachteler bzw. dementsprechend interleaving rule / Verschachtelungsregel.

                                      - 40 -



Weiterhin ist ein radio frame segmenter / Funkrahmensegmentierer dahingehend
auszulegen, dass er geeignet ist, einen verschachtelten Datenstrom in Einzelabschnitte (radio frames / Funkrahmen) für den bevorstehenden Sendevorgang aufzuteilen. Hierbei ist die Bitlänge des Funkrahmens direkt mit einem sog. predetermined time frame / vorbestimmten Zeitrahmen korreliert bzw. von diesem abhängig. Dieser Zeitrahmen repräsentiert die Dauer des Zeitintervalls, das für das Senden des/der für die Transmission vorbereiteten Funkrahmen/s zur Verfügung
steht, und wird üblicherweise auch als transmission time interval (TTI) / Übertragungszeitintervall bezeichnet.


Ein rate matcher / Ratenabstimmer – in vergleichbarem Kontext auch unter dem
Begriff Ratenanpasser bekannt - stimmt die Anzahl kodierter Datenworte/-symbole
auf eine bestimmte Anzahl von Übertragungsdatenworten/-symbolen ab, um die
Effizienz und die Systemleistung der Datenübertragung zu erhöhen. Dabei berücksichtigt er Randbedingungen und Systemvorgaben, die in einer rate matching rule
/ Ratenanpassungsregel zusammengefasst sind und im Wesentlichen Regeln für
das Wiederholen und das Punktieren einzelner Bits aus einem Datenwort/-symbol
enthalten. Hierbei wird unter puncturing / Punktieren das Löschen einzelner Paritätsbits nach dem Kodiervorgang eines Datenwortes verstanden, da diese in der
Regel in redundanter Form vorhanden sind. Das Ziel, redundante Information aus
einem Datenwort zu löschen und/oder den Datenstrom damit gemäß den herrschenden Übertragungsbedingungen für den Sendevorgang zu optimieren, kann
durch die Verwendung von mehreren Ratenabstimmern erreicht werden, die jeweils nur auf eine bestimmte Komponente eines Datenpakets oder –stroms wirken
(sog. component rate matcher / Komponentenratenabstimmer); diese wirken, sobald ein kodierter Datenstrom in mehrere einzelne kodierte Datenströme, die jeweils ausschließlich aus Paritätsbits, Informationssymbolen etc. bestehen, zerlegt
worden ist.


Nach Ansicht des Senats wird der eigentliche Signalfluss im Rahmen des mobilen
Kommunikationssystems im Einzelnen durch die sequenzielle Aufzählung gegenständlicher Merkmale in den Ansprüchen charakterisiert.

                                       - 41 -



                             II. Zur erteilten Fassung


1. Über das Streitpatent in seiner erteilten Fassung konnte im Termin vom
7. Mai 2014 entschieden werden, da dem Antrag der Beklagten auf Vertagung der
mündlichen Verhandlung nicht stattzugeben war.


Soweit die Beklagte ihren Antrag damit begründet hat, ihr sei Gelegenheit zu geben, die Eigenschaften eines Funkrahmensegmentierers, wie in Anspruch 1 des
Streitpatents enthalten, weiter zu klären, da das Gericht hierauf offensichtlich bei
der Entscheidung abstellen wolle, hat der Senat für eine Vertagung keine Veranlassung gesehen. Denn insoweit handelt es sich nicht um für die Beklagte neue
und damit gegebenenfalls überraschende Überlegungen des Senats. Vielmehr
stand von Beginn des Nichtigkeitsverfahrens an die Frage, über welche Eigenschaften der Demultiplexer nach dem Streitpatent bzw. nach der Lehre des Prioritätsdokuments verfüge, im Mittelpunkt der Erörterungen der Parteien. Auch im
Hinweis des Senats nach § 83 PatG war dieser Komplex unter Ziffer 6a) schwerpunktmäßig problematisiert worden. Die Beurteilung der strittigen Frage der Anordnung des die Symbolklassifzierung durchführenden Demultiplexers hängt auch
nach der dort dargelegten vorläufigen Ansicht des Senats nicht zuletzt davon ab,
welche Eigenschaften der Funkrahmensegmentierer nach der jeweiligen Lehre besitzen muss, damit der Demultiplexer je nach Anordnung seine bestimmungsgemäße Funktion innerhalb der jeweiligen Vorrichtung erfüllen kann. Inwieweit trotz
ausführlicher Diskussion, insbesondere in den Schriftsätzen, weiterer Klärungsbedarf seitens der Beklagten besteht, hat diese im Übrigen nicht näher erläutert.


2. Entgegen der Ansicht der Beklagten kann das Streitpatent die Priorität der koreanischen Voranmeldung KR 9927407 nicht beanspruchen.

                                       - 42 -



Übereinstimmend gehen die Parteien davon aus, dass der Beurteilung der strittigen Frage, ob dem Streitpatent der Zeitrang der koreanischen Voranmeldung KR 9927407 vom 8. Juli 1999 zukommt, die von der Klägerin als Druckschrift NK8E ins Verfahren eingeführte deutsche Übersetzung derselben zugrunde
zu legen ist.


Nach Art. 87, 88 EPÜ kann für eine Anmeldung die Priorität einer Voranmeldung
in Anspruch genommen werden, wenn Anmeldung und Voranmeldung „dieselbe
Erfindung“ betreffen. Dies liegt nach der höchstrichterlichen Rechtsprechung vor,
wenn sich die in der Voranmeldung anhand eines Ausführungsbeispiels oder in
sonstiger Weise beschriebenen technischen Anweisungen für den Fachmann als
Ausgestaltung der in der Nachanmeldung umschriebenen allgemeineren technischen Lehre darstellen und diese Lehre in der in der Nachanmeldung offenbarten
Allgemeinheit bereits der Voranmeldung als zu der angemeldeten Erfindung gehörend    entnehmbar      ist.   (BGH     st. Rspr.,   vgl.       zuletzt   Urteil   vom
11. Februar 2014 - X ZR 107/12 – Kommunikationskanal, Leitsatz und Tz. 20). Ein
Fall der Erfindungsidentität ist vorliegend jedoch nicht gegeben, denn der Fachmann entnimmt die technische Lehre der Gegenstände des Streitpatents gerade
nicht unmittelbar und eindeutig den Ursprungsunterlagen. Das Streitpatent vermittelt ihm auch nicht eine Lehre, die dort zwar gegenüber der Voranmeldung in allgemeinerer Form dargestellt wird, jedoch in ihrer Allgemeinheit bereits der Voranmeldung als zur Erfindung gehörend entnehmbar ist. Vielmehr ist mit dem Streitpatent eine weitere spezielle Ausgestaltungsform unter Schutz gestellt, die sich
dem Fachmann als eine zusätzliche Ausgestaltungsform gegenüber den in der
Voranmeldung KR 9927407 in Form dreier im Detail beschriebener Ausführungsbeispiele darstellt und aus diesem Grund ein Aliud darstellt.

                                     - 43 -



Im Einzelnen ist in der Prioritätsanmeldung allgemein offenbart, dass der Symbolklassifizierer 62 entweder zwischen dem ersten Verschachteler 112 und dem
Funkrahmensegmentierer 113 oder zwischen dem Funkrahmensegmentierer 113
und dem Ratenabstimmer 114 angeordnet sein kann (NK8E, Seite 22-36, Zeilen 6
bis 10: „Hierbei kann der Demultiplexer, der die Daten in das Informationssymbol
und das Paritätssymbol klassifiziert, zwischen dem ersten Verschachteler 112 und
dem Funkrahmen-Segmentierer 113 oder zwischen dem Funkrahmen-Segmentierer 113 und dem Ratenabstimmer 114 in der Kanal-Übertragseinrichtung der
Fig. 1 angeordnet werden.“). Weiter ist in der Prioritätsanmeldung ausgeführt,
dass sich die Ausführungsbeispiele jedoch nur auf die dort beschriebene erste Alternative beziehen, also mit der Anordnung des Symbolklassifizierers unmittelbar
nach dem Verschachteler (NK8E, Seite 22-36, Zeilen 10 bis 13: „Die Ausführungsformen gemäß der vorliegenden Erfindung erläutern über den Demultiplexer, der
für eine Symbolunterteilung verwendet wird, dass er nach dem ersten Verschachteler 112 angeordnet ist.“; Unterstreichung hinzugefügt). Dieses Verständnis der
Voranmeldung stimmt auch mit der zitierten Textstelle vorausgehenden Offenbarungenstellen zu den einzelnen Ausführungsbeispielen überein, in denen lediglich
für den Fall, dass der Symbolklassifizierer zwischen dem ersten Verschachteler
und dem Funkrahmensegmentierer vorgesehen ist, der Symbolklassifizierer als
einfacher n-fach Demultiplexer („n-DEMUX“) ausgebildet sein kann. Bezug genommen wird hierzu insoweit auf die einfache auszuführende Funktion des dort
angeordneten Symbolklassifizierers (NK8E, Seite 20-36, Absatz 2, Zeilen 3 bis 5
unter Bezugnahme auf die Figuren 5, 6 und 7: „Da die Symbolklassifizierungs-Einrichtung eine Modulo-n-Operation für ein Ausgangssymbol ausführt, kann sie
leicht durch Verwendung eines n-DEMUX verwirklicht werden, …“. Unterstreichungen hinzugefügt). Dass ein zwischen dem Funkrahmensegmentierer und dem Ratenabstimmer vorgesehener Symbolklassifizierer ebenso eine Operation auszuführen hätte und deshalb ebenfalls als n-fach Demultiplexer ausgeführt sein kann,
ist der in Rede stehenden Prioritätsanmeldung KR 9927407 hingegen weder konkret zu entnehmen noch stellt sich diese Ausgestaltung dem Fachmann als in allgemeinerer Form zur angemeldeten Erfindung gehörend dar. Ein Symbolklassifizierer ist - auch nach dem Wortlaut der Prioritätsanmeldung – nicht zwingend

                                        - 44 -



durch einen Multiplexer zu realisieren, sondern nur unter ganz bestimmten Voraussetzungen, zu denen die Prioritätsanmeldung jedoch hinsichtlich der speziellen Anordnung zwischen dem Funkrahmensegmentierer und dem Ratenabstimmer keine Ausführungen macht.


Die streitpatentgemäße Ausgestaltung hat im Übrigen auch keinen Eingang in die
Patentansprüche 8 und 10 der Prioritätsanmeldung gefunden, wo ganz allgemein
von dem Symbolklassifizierer die Rede ist und nicht von seiner Ausbildung als Demultiplexer.


Wird im Streitpatent die zweite Alternative der Anordnung eines Multiplexers zwischen dem Funkrahmensegmentierer und dem Ratenabstimmer beansprucht
(Merkmale 1.4 bis 1.6 in ihrer definierten Reihenfolge), so handelt es sich folglich
nicht um dieselbe Erfindung wie in der Prioritätsanmeldung KR 9927407, sondern
um eine andere Realisierungsmöglichkeit, die in der genannten Prioritätsschrift so
aber nicht als zur Erfindung gehörig offenbart ist.


3. Da aus den vorgenannten Gründen das Streitpatent die Priorität der koreanischen Voranmeldung KR 9927407 nicht beanspruchen kann, zählen die beiden
aus einem Standardisierungsverfahren stammenden und in den für dieses Verfahren wesentlichen Punkten inhaltsgleichen Druckschriften TSGR1#6(99)919 (NK6)
und TSGR1#6(99)948 (NK7) folglich zum Stand der Technik.


3.1 Zum erteilten Patentanspruch 1


Aus der Druckschrift NK6 ist eine Vorrichtung zur Übertragung in Aufwärtsrichtung
(„up-link“) für ein mobiles Kommunikationssystem bekannt (vgl. Figur 5; Merkmal 1.1), die einen Codierer aufweist („Turbo Encoder R=1/3”, Figur 5 links), und
zwar zum Empfangen eines Informationsbitstroms („Xk”) und zum Ausgeben von
insgesamt drei Strömen, einem systematischen Symbolstrom („C1k“), einem ersten
Paritätssymbolstrom („C2k“) und einem zweiten Paritätssymbolstrom („C3k“) durch
Codieren des Informationsbitstroms (Figur 5; Merkmal 1.2, Merkmal 1.2.1, Merk-

                                      - 45 -



mal 1.2.2). Ferner weist die Vorrichtung auch einen Verschachteler auf („1st interleaver”, Figur 5, zweiter Kasten von links), und zwar zum Verschachteln der drei
Ströme von codierten Symbolen miteinander mittels einer vorbestimmten Verschachtelungsregel und zum Ausgeben eines verschachtelten Stromes (Figur 5;
Merkmal 1.3, Merkmal 1.3.1, Merkmal 1.3.2), sowie einen Funkrahmensegmentierer („Radio Frame Segmentation”; Figur 5, dritter Kasten von links) zum Empfangen des verschachtelten Stromes und zum Abbilden des empfangenen Stromes auf mindestens einen Funkrahmen (Figur 5; Merkmal 1.4, Merkmal 1.4.1,
Merkmal 1.4.2), einen Demultiplexer (Figur 5, Zeigersymbolik zwischen den drei
vertikalen und den drei horizontalen Kästen; Merkmal 1.5), und einen Ratenabstimmer (Figur 5, „rate matching”, wobei die hier abgebildeten drei Einzelblöcke in
einer einzigen Einheit zusammengefasst sein können, vgl. Figur 6, „rate matching
algorithm block”). Der Ratenabstimmer dient auch hier zum Punktieren von einem
Teil der ersten und zweiten Paritätssymbole (Figur 5, „x“-Symbolik im abgehenden
Binärstrom des zweiten und dritten „rate matching algorithm block“), entsprechend
einer vorgegebenen Ratenabstimmungsregel (vgl. Figur 5 und 6, jeweils rechte Figurenhälfte); Merkmal 1.6, Merkmal 1.6.1, Merkmal 1.6.2).


Folglich sind sämtliche Merkmale des erteilten Anspruchs 1 aus der Druckschrift NK6 bekannt und dieser somit mangels Neuheit seines Gegenstandes nicht
patentfähig.


3.2 Zum erteilten Patentanspruch 12


Aus der Druckschrift NK6 sind auch alle Merkmale des erteilten Anspruchs 12 bekannt und zwar eine Übertragungsvorrichtung für ein mobiles Kommunikationssystem (z. B. Figur 5, Merkmal 12.1), das einen Codierer („Turbo Encoder R=1/3”; Figur 5 links) aufweist (Merkmal 12.2), welcher eingerichtet ist zum Empfangen eines Informationsbitstroms („Xk”) mit einem vorbestimmten Übertragungszeitintervall (z. B. indirekt aus Seite 6, Absatz 1 als Voraussetzung für den folgenden Verarbeitungsbaustein: „interleaver for transmission time interval of 10, 20, 40,
80 msec”, Merkmal 12.2.1), zum Ausgeben eines systematischen Symbolstroms

                                       - 46 -



(Seite 6, Kapitel 4, Absatz 1 und Kapitel 4.2 i. V. m. Figur 5, „C1k“, Merkmal 12.2.2) und mindestens einer Art von Paritätssymbolstrom (Seite 6, Kapitel 4,
Absatz 1 und Kapitel 4.2 i. V. m. Figur 5, „C2k, C3k“) mittels Codieren des Informationsbitstroms („Xk”) in Übereinstimmung mit einer Codierrate des Codierers (Seite 6, Kapitel 4, Absatz 1 und Kapitel 4.2 i. V. m. Figur 5, “Turbo Encoder R=1/3”;
Merkmal 12.2.3). Ferner weist sie in Folge einen Verschachteler auf („1st interleaver”, Figur 5, zweiter Kasten von links; Merkmal 12.3) zum Empfangen des
Stroms von systematischen Symbolen und des Stroms von Paritätssymbolen vom
Codierer (Figur 5, zweiter Kasten von links; Merkmal 12.3.1), zum Verschachteln
des Stroms von systematischen Symbolen und des Stroms von Paritätssymbolen
miteinander und zum Ausgeben eines verschachtelten Stroms (Figur 5, Pfeilsymbolik zwischen zweitem und drittem Kasten von links; Merkmal 12.3.2, Merkmal 12.3.3), sowie einen Funkrahmensegmentierer („Radio Frame Segmentation”;
Figur 5, dritter Kasten von links; Merkmal 12.4) zum Empfangen des verschachtelten Stroms von dem Verschachteler, zum Teilen des empfangenen Stroms in
mindestens einen Funkrahmen und zum Ausgeben des mindestens einen Funkrahmens (Seite 6, Kapitel 4, Absatz 1 und Kapitel 4.2 i. V. m. Figur 5; Merkmal 12.4.1, Merkmal 12.4.2). Auch ein Demultiplexer (Figur 5, Zeigersymbolik
zwischen den drei vertikalen und den drei horizontalen Kästen; Merkmal 12.5) ist
vorgesehen, und zwar zum Empfangen des mindestens einen Funkrahmens und
zum Demultiplexen des empfangenen mindestens einen Funkrahmens in einen
systematischen Symbolstrom und mindestens eine Art von Paritätssymbolstrom
(Figur 5, Zeigersymbolik s. o.; Merkmal 12.5.1, Merkmal 12.5.2). Diesem folgt ein
Ratenabstimmer (Figur 5, „rate matching”, wobei auch hier die abgebildeten drei
Einzelblöcke in einer einzigen Einheit zusammengefasst sein können, vgl. Figur 6,
„rate matching algorithm block”; Merkmal 12.6) zum Ratenabstimmen der von
dem Demultiplexer empfangenen Ströme und zum Ausgeben der ratenabgestimmten Ströme (Figur 5, „rate matching algorithm block 1-3”; Merkmal 12.6.1,
Merkmal 12.6.2), wobei der Ratenabstimmer mindestens einen Komponentenratenabstimmer zum Ratenabstimmen eines Teils des Paritätssymbolstroms aufweist, und die Anzahl des Komponentenratenabstimmers gleich der Anzahl von
Paritätssymbolströmen ist (Figur 5, „rate matching algorithm block 1” für den „sys-

                                       - 47 -



tematic information symbol” Strom lässt diesen unverändert durch, was dadurch
kenntlich wird, dass keine „x” im Fluss der Nullen und Einsen am Ausgang angezeigt werden; damit ist dieser Block als passiv einzustufen und nur der Block 2
(„parity symbols 1”) und der Block 3 („parity symbols 2”) als aktiv und zu zählen;
folglich beträgt die Anzahl der Komponentenratenabstimmer gleich zwei, entsprechend der Anzahl der Paritätssymbolströme); Merkmal 12.6.3, Merkmal 12.6.4),
und wobei der Demultiplexer jeden der Paritätssymbolströme in den Funkrahmen
zu dem Komponentenratenabstimmer schaltet, der jedem Paritätssymbolstrom
entspricht (Figur 5, „rate matching algorithm block 2,3”; Merkmal 12.6.5).


3.3 Zum erteilten Patentanspruch 23


Der nebengeordnete erteilte Verfahrensanspruch 23 weist gemäß obiger Merkmalsgliederung bis auf das Merkmal 23.11 sinngemäß identische Merkmale auf
wie der erteilte Patentanspruch 12. Bezüglich dieser Merkmale des Anspruchs
wird auf die Ausführungen zum Patentanspruch 12 verwiesen.


Das noch verbleibende Merkmal 23.11, nämlich dass dem Funkrahmen ein vorbestimmter Zeitrahmen zugewiesen wird, wird jedoch vom Fachmann als funktionsnotwendig in der Druckschrift NK6 mitgelesen, da das „travel time interval TTI“ die
Größe ist, die für eine Signalverarbeitung vor der Transmission stets berücksichtigt werden muss (zum Vergleich: Merkmal 12.2.1, in dem das Empfangen mit einem bestimmten Übertragungszeitintervall vorgegeben ist). Der Fachmann ergänzt diese Information als selbstverständlich für die Ausführung der unter Schutz
gestellten Lehre (BGH, Urteil vom 18. März 2014 – X ZR 77/12 - Proteintrennung,
Leitsatz a und Tz. 38-39).


Somit sind auch sämtliche Merkmale des erteilten Patentanspruchs 23 aus der
Druckschrift NK6 bekannt, und dieser daher mangels Neuheit seines Gegenstandes nicht patentfähig.

                                      - 48 -



3.4 Zum erteilten Patentanspruch 31


Der erteilte Vorrichtungsanspruchs 31 unterscheidet sich vom erteilten Vorrichtungsanspruch 12 in der Hauptsache dadurch, dass in ersterem nun kein „radio
frame segmenter“ mehr beansprucht wird. Dies hat zur Folge, dass sich gemäß
Anspruch 31 die bisher gültige sequentielle Anordnung der Vorrichtungsbestandteile ändert, die auch als Definition für den Signalweg bzw. Signalfluss durch die
gesamte beanspruchte Vorrichtung zu lesen ist. Die Merkmalsgruppe 12.5, 12.5.1
und 12.5.2 des erteilten Anspruchs 12 findet nun im Anspruch 31 keine Entsprechung mehr, da mit letzterem beansprucht wird, dass das Signal direkt aus dem
Verschachteler zum Demultiplexer weitergereicht wird, ohne dass zwischen diesen beiden Bauteilen eine Funkrahmensegmentierung stattfindet, oder dass ein
weiterer Baustein, der diese ausführen könnte, an diesem Ort im Signalweg zum
Einsatz kommt. Eine derartige Vorrichtung ist jedoch in der dem Streitpatent zugrundeliegenden PCT-Anmeldung WO 01/05059 A1 (NK9) nicht ursprünglich offenbart.


Der Anmeldung NK9 kann lediglich in deren Anspruch 37 entnommen werden,
dass der Verschachteler („interleaver“) zusätzlich dafür vorgesehen ist, die von
ihm verschachtelten Symbole in eine Vielzahl von Funkrahmen auszugeben, die
für sich jeweils eine festgelegte Anzahl von Symbolen aufnehmen können, also
eine festgelegte Größe aufweisen (NK9, Seite 30, Zeilen 10 bis 13: „an interleaver
for receiving the information symbols and the parity symbols from the encoder,
interleaving the information symbols and the parity symbols and outputting interleaved symbols in a plurality of radio frames, each of the radio frames having a
predetermined number of symbol;“ Unterstreichungen hinzugefügt).

                                      - 49 -



Auch die ursprünglich in der Druckschrift NK9 offenbarten Ausführungsbeispiele
und die diesen zugeordneten Figuren zeigen kein Bild des Signalflusses durch die
Vorrichtung, wie es mit dem erteilten Anspruch 31 beansprucht wird. Vielmehr wird
an den genannten Orten ausdrücklich betont, dass ein Funkrahmensegmentierer
im Signalfluss vorzusehen ist. Zieht man beispielsweise die Figuren 1 und 2 heran, zeigt sich der Funkrahmensegmentierer („radio frame segmenter, 130“) stets
zwischen dem ersten Verschachteler („1st interleaver, 120“) und dem Demultiplexer („DEMUX, 141“) angeordnet, und in den Figuren 13 bis 15 wird davon ausgegangen, dass der Demultiplexer („DEMUX, 141“) einen Signalfluss bearbeitet, der
vorher einer Funkrahmensegmentierung unterworfen war (Figuren 13 bis 15, links
oben „FROM RADIO FRAME SEGMENTATION“), womit die dort gezeigte Abfolge
auch als erfindungserheblich anzusehen ist. An keiner Stelle der ursprünglichen
Anmeldung NK9 ist jedoch davon die Rede, dass die Funkrahmensegmentierung
wie beansprucht im Signalfluss auch komplett entfallen könnte.


Somit geht der Gegenstand des erteilten Anspruchs 31 über die ursprüngliche Offenbarung, wie sie in der Anmeldung NK9 gelehrt wird, hinaus. Er unterfällt aus
diesem Grunde gemäß Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Nr. 1c
EPÜ der Nichtigerklärung.


3.5 Zum erteilten Patentanspruch 42


Der nebengeordnete erteilte Verfahrensanspruch 42 weist gemäß obiger Merkmalsgliederung sämtlich Verfahrensmerkmale auf, die in ihrer Entsprechung als
Vorrichtungsmerkmale bereits aus dem erteilten Anspruch 31 bekannt sind. Folglich geht der erteilte Anspruch 42 aus den gleichen Gründen, wie zu Anspruch 31
ausgeführt, ebenfalls über die Offenbarung der Ursprungsanmeldung hinaus und
ist ebenfalls gemäß Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Nr. 1c EPÜ
für nichtig zu erklären.

                                      - 50 -



                        III. Zu den Hilfsanträgen 1 bis 3


Die Verteidigung des Streitpatents mit den Fassungen gemäß Hilfsanträgen 1 bis
3 sowie gemäß Hilfsanträgen 2 und 3 auch in der Form ohne Streichung von Teilen der Beschreibung hat der Senat in der mündlichen Verhandlung vom
7. Mai 2014 als verspätet zurückgewiesen, da sie eine erneute Vertagung der
mündlichen Verhandlung erforderlich gemacht hätte (§ 83 Abs. 4 PatG).


Die Verteidigung der Beklagten mit diesen Hilfsanträgen erfolgte nach Ablauf der
gemäß § 83 Abs. 2 PatG im Hinweis vom 7. März 2013 nach § 83 Abs. 1 Satz 1
PatG gesetzten Fristen, die am 13. Mai 2013 endeten. Die Vertagung der auf den
5. Juni 2013 angesetzten mündlichen Verhandlung und deren Fortsetzung am
7. Mai 2014 hatten keinen Einfluss auf die im Hinweis gesetzten Fristen, schon gar
nicht konnten sie die bereits abgelaufenen Fristen nachträglich wieder in Lauf setzen. Der Senat hat im Hinblick auf den Fortsetzungstermin den Parteien keinen
weiteren qualifizierten Hinweis übermittelt oder der Beklagten eine erneute Frist
zur Einreichung von Verteidigungsmitteln gesetzt. Auch ist im Übrigen nichts ersichtlich, was eine Hilfsantragsstellung erstmals im Fortsetzungstermin als zulässig hätte erscheinen lassen.


Diesbezüglich hat die Beklagte in der mündlichen Verhandlung lediglich vorgetragen, die Hilfsantragsstellung sei im Hinblick auf die erst am Nachmittag aufgekommene Diskussion über die Rolle des „Funkrahmensegmentierers“ für die Beklagte
erforderlich geworden. Diese Einschätzung ist nicht zutreffend und entschuldigt
daher die verspätete Einreichung im Sinne des § 83 Abs. 4 Nr. 2 PatG nicht.

                                             - 51 -



Die Frage, welche Funktion der Funkrahmensegmentierer in Anspruch 1 des
Streitpatents im Vergleich zur Offenbarung in der Prioritätsschrift KR 1999-27407
besitzt, durchzieht vielmehr schwerpunktmäßig die gesamte (schriftsätzliche) Diskussion der Parteien zur Auslegung des Streitpatents wie auch zur Frage, ob das
Streitpatent die koreanische Priorität wirksam beanspruchen kann. Grund für die
Anberaumung des Fortsetzungstermins war gerade das zwischen den Parteien
streitige Verständnis der Prioritätsschrift KR 9927407 im Hinblick auf die Stellung
des Funkrahmensegmentierers und seiner Eigenschaften, da mit Hilfe einer vom
Senat    eingeholten     vollständigen       Übersetzung   der   koreanischen   Schrift
KR 9927407 ins Deutsche diese Frage einer abschließend Klärung zugeführt werden sollte. Zu dieser Problematik hatte der Senat im Übrigen im Hinweis vom
7. März 2013 bereits Stellung genommen, so dass für die Beklagte zu diesem frühen Zeitpunkt feststand, dass sie hierauf vorsorglich ihre hilfsweise Verteidigung
ausrichten müsste. Was die Beklagte veranlasst haben könnte, auf diesen Hinweis
nicht zu reagieren, ist nicht ersichtlich.


Die Befassung mit den verspätet und trotz erfolgter Belehrung nach § 83 Abs. 4
Nr. 3 PatG nicht genügend entschuldigten Hilfsanträgen 1 bis 3 einschließlich der
Fassungen, die nicht auch auf die Änderung der Beschreibung gerichtet waren,
hätte nach Auffassung des Senats die erneute Vertagung der mündlichen Verhandlung erforderlich gemacht. Denn die Fassungen, mit denen das Streitpatent
an die Offenbarung in der Prioritätsschrift KR 99-27407 „angepasst“ werden sollte,
erscheinen schon deshalb aus Rechtsgründen höchst problematisch, weil das
Streitpatent in der erteilten Fassung und die koreanische Voranmeldung
KR 9927407 nicht dieselbe Anmeldung betreffen (vgl. oben Ausführungen zur erteilten Fassung). Die Gefahr der Erweiterung des Schutzbereichs (Art. 138
Abs. 1d EPÜ) erscheint unter diesem Gesichtspunkt erheblich. Die Überprüfung
der Zulässigkeit der Fassungen unter Berücksichtigung der Ursprungsoffenbarung
zum Streitpatent war am Verhandlungstag nicht gewährleistet. Erst recht hätte - im
Fall der Zulässigkeit einer der Fassungen – die sich anschließende Prüfung der
Patentfähigkeit an Hand des umfangreichen Standes der Technik den zeitlichen
Rahmen der Verhandlung gesprengt.

                                        - 52 -



                               IV. Zum Hilfsantrag 4


1. Über das Streitpatent in dieser hilfsweise verteidigten Fassung konnte entschieden werden, denn die Änderung betrifft ausschließlich die Aufnahme des über die
Ansprüche 2 bis 9 direkt auf den Anspruch 1 rückbezogenen erteilten Patentanspruch 10 in die Fassung des erteilten Patentanspruchs 1. Die abhängigen Ansprüche 2 bis 9 und 11 sind auf den geänderten Anspruch 1 zurückbezogen. Die
erteilten Ansprüche 12 bis 48 sind gestrichen. Auch die Klägerin hat erklärt, sie
könne sich hierzu uneingeschränkt einlassen.


2. Hilfsantrag 4 ist zulässig, da der in dieser Fassung verteidigte Gegenstand des
Streitpatents in den ursprünglichen Anmeldeunterlagen so offenbart war (NK9, Ansprüche 1 und 11, wobei Anspruch 11 zwei zeitliche Alternativen für das beanspruchte Einbringen von Füllbits angibt), und vom bisherigen Schutzumfang desselben auch mit umfasst war (vergleiche Streitpatent, Ansprüche 1 und 10, wobei
in Anspruch 10 von den oben genannten zwei zeitlichen Alternativen aus den Anmeldeunterlagen für das beanspruchte Einbringen von Füllbits nun nur eine beansprucht wird).


3. Das Streitpatent hat in der Fassung gemäß Hilfsantrag 4 auch Bestand.


Der neue Anspruch 1, der gemäß Hilfsantrag 4 aus einer Kombination der erteilten
Ansprüche 1 und 10 gebildet wurde, kann zwar mit derselben Begründung wie der
erteilte Anspruch 1 nicht die Priorität der koreanischen Voranmeldung 9927407
beanspruchen, jedoch ist sein Gegenstand weder durch den im Verfahren befindlichen, für die Patentfähigkeit zu berücksichtigenden Stand der Technik bekannt,
noch dem Fachmann in Verbindung mit seinem Fachwissen nahe gelegt. Der Gegenstand des Patentanspruchs 1 in der verteidigten Fassung gilt als neu und beruht auch auf einer erfinderischen Tätigkeit.

                                       - 53 -



Der mit dem Hilfsantrag 4 beanspruchte einzige unabhängige Anspruch 1 kann im
Einzelnen wie folgt gegliedert werden (Änderungen zum erteilten Patentanspruch 1 fett):


        1.1 A[n] uplink transmitting device for a mobile communication
              system, comprising:
        1.2 an encoder (110)
              1.2.1 for receiving an information bit stream and
              1.2.2 for outputting three streams, a systematic symbol
                    stream (Xk), a first parity symbol stream (Yk), and a
                    second parity symbol stream (Zk) by encoding the information bit stream,
        1.3 an interleaver (120)
              1.3.1 for interleaving the three streams of encoded symbols
                    with each other by a predetermined interleaving rule
                    and
              1.3.2 for outputting an interleaved stream,
              1.3.3 wherein the interleaver is adapted to interleave the
                    encoded streams at a transmission time interval
                    after inserting filler bits into the encoded streams
                    in order to equalize the size of the at least one radio frame
        1.4 a radio frame segmenter (130)
              1.4.1 for receiving the interleaved stream and
              1.4.2 mapping the received stream onto at least one radio
                    frame,
        1.5 a demultiplexer (141), and
        1.6 a rate matcher (143,144)
              1.6.1 adapted to puncture a part of the first and second parity symbols
              1.6.2 according to a given rate matching rule.

                                      - 54 -



Das neu hinzugetretene Merkmal 1.3.3, nämlich dass der Verschachteler derart
ausgebildet ist, dass er die codierten Ströme für ein bestimmtes Übertragungszeitintervall entsprechend zu verschachteln vermag, nachdem er in den codierten
Strom Füllbits dergestalt eingefügt hat, dass sie an die Größe des mindestens einen Funkrahmens angeglichen sind, kann weder der Druckschrift NK6 noch der
Druckschrift NK7 entnommen werden. Eine derartige Funktionalität des Verschachtelers ist dort nicht vorgesehen, vielmehr wird die Maßnahme des Einfügens von Füllbits dort erst von den einzelnen „Rate Matching Algorithm Block[s]“
(NK6, Figur 5 rechts, ausgehende Bitströme mit den Füllbits „x“) vorgenommen.
Die Druckschriften liefern dem Fachmann zur Überzeugung des Senats auch keinerlei Veranlassung, die mit dem Merkmal 1.3.3 beanspruchte Maßnahme bereits
früher im Signalverarbeitungsablauf vorzunehmen. Auch bei eingehender fachmännischer Analyse der in den Druckschriften vorgestellten Lösung ist kein Nachteil ersichtlich, der den Fachmann anregen könnte, die patentgemäße Lösung aufzugreifen.


Auch die übrigen im Verfahren befindlichen Druckschriften können zur Überzeugung des Senats hierzu weder einen Hinweis liefern noch einen zusätzlichen oder
die bisherigen Maßnahmen ergänzenden technischen Beitrag leisten, da sie das
Einfügen von Füllbits entweder gar nicht (NK5, NK10 bis NK19, NK21-1, NK22 bis
NK26, NK28 bis NK31, NK32-2, NK32-3, NK34) oder an anderen Orten der Signalverarbeitungskette thematisieren (vgl. NK4, Kapitel 4.2.3.2.4, nur im Rahmen
der Kanalkodierung; NK32-1, Fig. 9, nur bildlich dargestellt im so genannten
„OVERALL MULTIPLEX FRAME“, ohne Angabe, wann und wo die Füllbits zu diesem hinzutreten). Der übrige Stand der Technik liegt noch weiter ab.

                                       - 55 -



Auch die von der Beklagten in die bekannte 3GPP Standardisierungsarbeitsgruppe eingebrachte Druckschrift TSGR#6(99)yyy (NK33) offenbart im selben technischen Zusammenhang wie das Streitpatent nur den Einsatz von Füllbits im Rahmen der eigentlichen „Radio Frame Segmentation“ mit anschließendem „Rate
matching“, nicht jedoch unmittelbar die Einbringung der Füllbits direkt am und
durch einen/den Verschachteler (NK33, Seite 1 und 2, Kapitel 2.1.1 i. V. m. Figur 1 obere Hälfte); diese Druckschrift thematisiert auch nicht, wo und in welcher
Beziehung ein etwa vorgesehener DEMUX zum hier gestalteten Signalfluss stünde, so dass eine Kombination der Druckschrift NK33 mit einer der Druckschriften NK6 oder NK7 dem Fachmann ohnehin nicht nahegelegen hätte, um gegebenenfalls unter Einsatz seines Fachwissens auf einen anderen Ort der Einarbeitung
von Füllbits in den Signalstrom hinzuwirken, als er ihm bisher durch die Druckschriften NK6 und NK7 als geeignet vermittelt wurde. Vielmehr hätte er ohne einen dortigen Hinweis auf die Verortung eines funktionstechnisch als DEMUX zu
interpretierenden und in einem Signalfluss bereits als praktikabel verifizierten Bausteins von der Druckschrift NK33 sogar Abstand genommen, wäre doch für ihn damit ein zunächst nicht abschätzbarer zusätzlicher Implementierungsaufwand verbunden, den er in diesem komplexen technischen Zusammenhang aus Zeit- und
Kostengründen vermeiden würde.


Somit hatte der Fachmann weder aus dem im Verfahren befindlichen Stand der
Technik eine dokumentierte Anregung, so vorzugehen wie beansprucht, noch liefert ihm dieser technische Hinweise, die ihn aufgrund seines Fachwissens im gegebenen technischen Kontext auf einen möglichen Vorteil der mit dem Anspruch 1
gemäß Hilfsantrag 4 beanspruchten Vorgehensweise hingewiesen und in naheliegender Weise zum Vorsehen derselben geführt hätten (Merkmal 1.3.3).


Folglich ist der Gegenstand des Patentanspruchs 1, so wie er mit dem Hilfsantrag 4 verteidigt wird, sowohl neu als auch erfinderisch gegenüber dem im Verfahren befindlichen Stand der Technik und dem fachmännischen Wissen. Der Patentanspruch 1 ist damit auch patentfähig, wodurch die Patentfähigkeit der sich hieran
anschließenden Unteransprüche 2 bis 9 und 11 getragen wird.

                                          - 56 -



                                           V.


Die Kostenaufteilung entspricht dem Verhältnis des anteiligen Obsiegens und Unterliegens der Parteien im Rechtsstreit (§ 84 Abs. 2 PatG i. V. m. § 92 Abs. 1
ZPO). Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99
Abs. 1 PatG i. V. m. § 709 ZPO.


                                           VI.


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

                                     - 57 -



Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung
gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteils Berufung
eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Gutermuth         Martens       Gottstein        Kleinschmidt        Dr. Wollny
                  zugleich für
                  den mit
                  Ablauf des
                  Monats
                  Mai 2014 in
                  den Ruhestand eingetretenen Vorsitzenden
                  Richter
                  Gutermuth.



                                                                              Pü
