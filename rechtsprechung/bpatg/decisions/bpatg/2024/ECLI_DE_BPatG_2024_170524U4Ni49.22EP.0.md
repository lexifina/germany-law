---
ecli: "ECLI:DE:BPatG:2024:170524U4Ni49.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 49/22"
decided: "2024-05-17"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=10&nr=44138&anz=391&pos=160&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-05-17_4_Ni_49_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0130a.md", "germany/bund/acts/zpo/0156.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 49/22 vom 2024-05-17

## Entscheidung

BUNDESPATENTGERICHT
                         IM NAMEN DES VOLKES

                                         URTEIL

4 Ni 49/22 (EP)                                            An Verkündungs Statt
                                                               zugestellt am
 verbunden mit                                                17.05.2024
4 Ni 53/22 (EP)                                                     …

(Aktenzeichen)



                          In der Patentnichtigkeitssache
…




ECLI:DE:BPatG:2024:170524U4Ni49.22EP.0

                  betreffend das europäische Patent 2 940 685
                              (DE 60 2013 070 229)



hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 26. Januar 2024 durch die Richterin Werner M. A. als Vorsitzende
und die Richter Schwarz, Dipl.-Ing. Altvater, Dipl.-Ing. Matter und Dipl.-Phys.
Univ. Dr. Haupt


für Recht erkannt:

     I.     Das europäische Patent 2 940 685 wird mit Wirkung für das
            Hoheitsgebiet der Bundesrepublik Deutschland für nichtig
            erklärt.


     II.    Die Beklagte trägt die Kosten des Rechtsstreits.


     III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
            des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.




                                                                               2/120

                                 Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet
der Bundesrepublik Deutschland in englischer Sprache erteilten Europäischen Patents 2 940 685 (Streitpatent), das unter Inanspruchnahme der Priorität der chinesischen Anmeldung CN 201310034240 vom 29. Januar 2013 am 23. Juli 2013 als
PCT/CN2013/079883 international angemeldet worden ist. Die Anmeldung ist am
7. August 2014 als WO 2014/117484 A1 und die Erteilung des Streitpatents am
24. Juni 2020 als EP 2 940 685 B1 veröffentlicht worden.

Das Deutsche Patent- und Markenamt führt das Streitpatent unter dem Aktenzeichen 60 2013 070 229.2. Es trägt die Bezeichnung

     „PREDICTION METHOD AND DECODING DEVICE FOR BANDWIDTH
                           EXPANSION BAND SIGNAL”

                        und in der deutschen Übersetzung:
            „Vorhersageverfahren und Decodierungsvorrichtung für ein
                      Bandbreitenerweiterungs-Bandsignal“.

Das Patent umfasst in der erteilten Fassung zehn Patentansprüche, die die Klägerin
zu 1 mit ihrer Nichtigkeitsklage vom 12. April 2022 im Umfang der Patentansprüche
1, 3, 4, 5 (zweite Alternative), 6, 8, 9 und 10 (zweite Alternative) und die Klägerin
zu 2 mit ihrer Nichtigkeitsklage vom 1. Mai 2022 in vollem Umfang angreift.


Der das Verfahren zur Vorhersage eines Bandbreiterweiterungs-Frequenzbandsignals betreffende unabhängige Patentanspruch 1 und der die Dekodiervorrichtung
betreffende unabhängige Patentanspruch 6 lauten in der erteilten Fassung in der
Verfahrenssprache Englisch laut Streitpatentschrift:

  1. A method for predicting a bandwidth extension frequency band signal, comprising:




                                                                               3/120

demultiplexing (100) a received bitstream, and
decoding the demultiplexed bitstream to obtain
a frequency domain signal;
determining (101) whether a highest frequency
bin, to which a bit is allocated, of the frequency
domain signal is less than a preset start frequency bin of a bandwidth extension frequency
band;
predicting (102) an excitation signal of the bandwidth extension frequency band according to an
excitation signal within a predetermined frequency band range of the frequency domain signal and the preset start frequency bin of the
bandwidth extension frequency band when the
highest frequency bin to which a bit is allocated
is less than the preset start frequency bin of the
bandwidth extension frequency band;
predicting (103) the excitation signal of the bandwidth extension frequency band according to the
excitation signal within the predetermined frequency band range of the frequency domain signal, the preset start frequency bin of the bandwidth extension frequency band, and the highest
frequency bin to which a bit is allocated when the
highest frequency bin to which a bit is allocated
is no less than the preset start frequency bin of
the bandwidth extension frequency band;
and
predicting (104) the bandwidth extension frequency band signal according to the predicted
excitation signal of the bandwidth extension frequency band and a frequency envelope of the
bandwidth extension frequency band;


                                                      4/120

wherein the predicting an excitation signal of the
bandwidth extension frequency band according
to an excitation signal within a predetermined
frequency band range of the frequency domain
signal and the preset start frequency bin of the
bandwidth extension frequency band comprises:
    making n copies of the excitation signal
    within the predetermined frequency band
    range of the frequency domain signal, and
    using the n copies of the excitation signal
    as an excitation signal between the preset
    start frequency bin of the bandwidth extension frequency band and a highest frequency bin of the bandwidth extension frequency band, wherein n is an integer or a
    non-integer greater than 0, and n is equal to
    a ratio of a quantity of frequency bins between the preset start frequency bin of the
    bandwidth extension frequency band and
    the highest frequency bin of the bandwidth
    extension frequency band to a quantity of
    frequency bins within the predetermined
    frequency band range of the frequency domain signal;
    where n is an integer or a non-integer
    greater than 0; and
    wherein the predicting the excitation signal
    of the bandwidth extension frequency band
    according to the excitation signal within the
    predetermined frequency band range of the
    frequency domain signal, the preset start
    frequency bin of the bandwidth extension


                                                     5/120

           frequency band, and the highest frequency
           bin, to which a bit is allocated comprises:
           making a copy of an excitation signal from
           the mth frequency bin fexc_start+ above a start
           frequency bin fexc_start of the predetermined
           frequency band range of the frequency domain signal to an end frequency bin fexc_end
           of the predetermined frequency band
           range of the frequency domain signal and
           n copies of the excitation signal within the
           predetermined frequency band range of
           the frequency domain signal, and using the
           two parts of excitation signals as an excitation signal between the highest frequency
           bin, to which a bit is allocated, of the frequency domain signal and the highest frequency bin of the bandwidth extension frequency band, wherein n is 0 or an integer
           or a non-integer greater than 0, m is a positive integer, and m is equal to a value of a
           quantity of frequency bins between the
           highest frequency bin to which a bit is allocated and the preset start frequency bin of
           the bandwidth extension frequency band.


6. A decoding device, comprising:

       a decoding module (30), configured to: demultiplex a received bitstream, and decode the demultiplexed bitstream to obtain a frequency domain signal;
       a determining module (31), configured to determine whether a highest frequency bin, to which




                                                             6/120

a bit is allocated, of the frequency domain signal
is less than a preset start frequency bin of a
bandwidth extension frequency band;
a first processing module (32), configured to:
when the determining module (31) determines
that the highest frequency bin to which a bit is
allocated is less than the preset start frequency
bin of the bandwidth extension frequency band,
predict an excitation signal of the bandwidth extension frequency band according to an excitation signal within a predetermined frequency
band range of the frequency domain signal and
the preset start frequency bin of the bandwidth
extension frequency band;
a second processing module (33), configured to:
when the determining module (31) determines
that the highest frequency bin to which a bit is
allocated is greater than or equal to the preset
start frequency bin of the bandwidth extension
frequency band, predict the excitation signal of
the bandwidth extension frequency band according to the excitation signal within the predetermined frequency band range of the frequency
domain signal, the preset start frequency bin of
the bandwidth extension frequency band, and
the highest frequency bin to which a bit is allocated; and
a predicting module (34), configured to predict a
bandwidth extension frequency band signal according to the predicted excitation signal of the
bandwidth extension frequency band and a frequency envelope of the bandwidth extension
frequency band;


                                                     7/120

wherein the first processing module (32) is specifically configured to: make n copies of the excitation signal within the predetermined frequency
band range of the frequency domain signal, and
use the n copies of the excitation signal as an
excitation signal between the preset start frequency bin of the bandwidth extension frequency band and a highest frequency bin of the
bandwidth extension frequency band, wherein n
is an integer or a non-integer greater than 0, and
n is equal to a ratio of a quantity of frequency
bins between the preset start frequency bin of
the bandwidth extension frequency band and the
highest frequency bin of the bandwidth extension frequency band to a quantity of frequency
bins within the predetermined frequency band
range of the frequency domain signal; where n is
an integer or a non-integer greater than 0; and
wherein the second processing module (33) is
specifically configured to: make a copy of an excitation signal from the mth frequency bin fexc_start+
above a start frequency bin fexc_start of the predetermined frequency band range of the frequency
domain signal to an end frequency bin fexc_end of
the predetermined frequency band range of the
frequency domain signal and n copies of the excitation signal within the predetermined frequency band range of the frequency domain signal, and use the two parts of excitation signals
as an excitation signal between the highest frequency bin, to which a bit is allocated, of the frequency domain signal and the highest frequency
bin of the bandwidth extension frequency band,


                                                         8/120

          wherein n is 0 or an integer or a non-integer
          greater than 0, m is a positive integer, and m is
          equal to a value of a quantity of frequency bins
          between the highest frequency bin to which a bit
          is allocated and the preset start frequency bin of
          the bandwidth extension frequency band.



In deutscher Übersetzung gemäß Streitpatentschrift:

  1. Verfahren zur Vorhersage eines Bandbreitenerweiterungs-Frequenzbandsignals, umfassend:

          Entmultiplexen (100) eines empfangenen Bitstroms und Dekodieren des entmultiplexten Bitstroms, um ein Frequenzdomänensignal zu erhalten;
          Bestimmen (101), ob ein höchstes Frequenzbin,
          dem ein Bit zugeordnet ist, des Frequenzdomänensignals kleiner ist als ein voreingestelltes
          Anfangs-Frequenzbin eines Bandbreitenerweiterungs-Frequenzbandes;
          Vorhersagen (102) eines Erregungssignals des
          Bandbreitenerweiterungs-Frequenzbandes gemäß einem Erregungssignal in einem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals und dem voreingestellten Anfangs-Frequenzbin     des   Bandbreitenerweiterungs-Frequenzbandes, wenn das höchste Frequenzbin, dem ein Bit zugeordnet ist, kleiner ist
          als das voreingestellte Anfangs-Frequenzbin
          des       Bandbreitenerweiterungs-Frequenzbandes;




                                                               9/120

Vorhersagen (103) des Erregungssignals des
Bandbreitenerweiterungs-Frequenzbandes gemäß einem Erregungssignal in dem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals, dem voreingestellten Anfangs-Frequenzbin     des   Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin, dem ein Bit zugeordnet ist, wenn das
höchste Frequenzbin, dem ein Bit zugeordnet
ist, nicht kleiner ist als das voreingestellte Anfangs-Frequenzbin     des   Bandbreitenerweiterungs-Frequenzbandes; und
Vorhersagen (104) des Bandbreitenerweiterungs-Frequenzbandsignals gemäß dem vorhergesagten Erregungssignal des Bandbreitenerweiterungs-Frequenzbandes und einer Frequenzhüllkurve des Bandbreitenerweiterungs-Frequenzbandes;
wobei das Vorhersagen eines Erregungssignals
des      Bandbreitenerweiterungs-Frequenzbandes gemäß einem Erregungssignal in einem
vorbestimmten Frequenzbandbereich des Frequenzdomänensignals und dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes umfasst:
      Erzeugen von n Kopien des Erregungssignals in dem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals und
      Verwenden der n Kopien des Erregungssignals als Erregungssignal zwischen dem
      voreingestellten Anfangs-Frequenzbin des
      Bandbreitenerweiterungs-Frequenzbandes und einem höchsten Frequenzbin des


                                                     10/120

Bandbreitenerweiterungs-Frequenzbandes, wobei n eine ganze Zahl oder eine
nicht ganze Zahl größer als 0 ist und n
gleich einem Verhältnis einer Menge von
Frequenzbins zwischen dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und dem
höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes      zu    einer
Menge von Frequenzbins in dem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals ist; wobei n eine
ganze Zahl oder eine nicht ganze Zahl größer als 0 ist; und wobei das Vorhersagen
des Erregungssignals des Bandbreitenerweiterungs-Frequenzbandes gemäß dem
Erregungssignal in dem vorbestimmten
Frequenzbandbereich des Frequenzdomänensignals, dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin, dem ein Bit zugeordnet ist, umfasst:
Erzeugen einer Kopie des Erregungssignals von dem m-ten Frequenzbin fexc_start+
über einem Anfangs-Frequenzbin fexc_start
des vorbestimmten Frequenzbandbereichs
des Frequenzdomänensignals bis zu einem
End-Frequenzbin fexc_end des vorbestimmten Frequenzbandbereichs des Frequenzdomänensignals und n Kopien des Erregungssignals in dem vorbestimmten Fre-




                                             11/120

              quenzbandbereich des Frequenzdomänensignals und Verwenden der beiden Teile
              der Erregungssignale als Erregungssignal
              zwischen dem höchsten Frequenzbin, dem
              ein Bit zugeordnet ist, des Frequenzdomänensignals und dem höchsten Frequenzbin
              des    Bandbreitenerweiterungs-Frequenzbandes, wobei n 0 oder eine ganze Zahl oder eine nicht ganze Zahl größer als 0 ist, m
              eine positive ganze Zahl ist und m gleich einem Wert einer Menge von Frequenzbins
              zwischen dem höchsten Frequenzbin, dem
              ein Bit zugeordnet ist, und dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes ist.


6. Dekodiervorrichtung, umfassend:

       ein Dekodiermodul (30), das dafür ausgelegt ist:
       einen empfangenen Bitstrom zu entmultiplexen
       und den entmultiplexten Bitstrom zu dekodieren, um ein Frequenzdomänensignal zu erhalten;
       ein Bestimmungsmodul (31), das dafür ausgelegt ist zu bestimmen, ob ein höchstes Frequenzbin, dem ein Bit zugeordnet ist, des Frequenzdomänensignals kleiner ist als ein voreingestelltes Anfangs-Frequenzbin eines Bandbreitenerweiterungs-Frequenzbandes;
       ein erstes Verarbeitungsmodul (32), das ausgelegt ist zum: wenn das Bestimmungsmodul (31)
       bestimmt, dass das höchste Frequenzbin, dem




                                                              12/120

ein Bit zugeordnet ist, kleiner als das voreingestellte Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes ist, Vorhersagen
eines Erregungssignals des Bandbreitenerweiterungs-Frequenzbandes gemäß einem Erregungssignal in einem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals und
dem voreingestellten Anfangs-Frequenzbin des
Bandbreitenerweiterungs-Frequenzbandes;
ein zweites Verarbeitungsmodul (33), das ausgelegt ist zum: wenn das Bestimmungsmodul
(31) bestimmt, dass das höchste Frequenzbin,
dem ein Bit zugeordnet ist, größer oder gleich
dem voreingestellten Anfangs-Frequenzbin des
Bandbreitenerweiterungs-Frequenzbandes ist,
Vorhersagen des Erregungssignals des Bandbreitenerweiterungs-Frequenzbandes       gemäß
dem Erregungssignal in dem vorbestimmten
Frequenzbandbereich des Frequenzdomänensignals, dem voreingestellten Anfangs-Frequenzbin     des   Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin,
dem ein Bit zugeordnet ist; und
ein Vorhersagemodul (34), das dafür ausgelegt
ist,   ein   Bandbreitenerweiterungs-Frequenzbandsignal gemäß dem vorhergesagten Erregungssignal des Bandbreitenerweiterungs-Frequenzbandes und einer Frequenzhüllkurve des
Bandbreitenerweiterungs-Frequenzbandes vorherzusagen;
wobei das erste Verarbeitungsmodul (32) speziell ausgelegt ist zum: Erzeugen von n Kopien
des Erregungssignals in dem vorbestimmten


                                                    13/120

Frequenzbandbereich des Frequenzdomänensignals und Verwenden der n Kopien des Erregungssignals als Erregungssignal zwischen
dem voreingestellten Anfangs-Frequenzbin des
Bandbreitenerweiterungs-Frequenzbandes und
einem höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes, wobei n eine
ganze Zahl oder eine nicht ganze Zahl größer
als 0 ist und n gleich einem Verhältnis einer
Menge von Frequenzbins zwischen dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes      und    dem
höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes zu einer Menge von
Frequenzbins in dem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals ist;
wobei n eine ganze Zahl oder eine nicht ganze
Zahl größer als 0 ist; und
wobei das zweite Verarbeitungsmodul (33) speziell ausgelegt ist zum: Erzeugen einer Kopie
des Erregungssignals von dem m-ten Frequenzbin fexc_start+ über einem Anfangs-Frequenzbin fexc_start des vorbestimmten Frequenzbandbereichs des Frequenzdomänensignals
bis zu einem End-Frequenzbin fexc_end des vorbestimmten Frequenzbandbereichs des Frequenzdomänensignals und n Kopien des Erregungssignals in dem vorbestimmten Frequenzbandbereich des Frequenzdomänensignals und
Verwenden der beiden Teile von Erregungssignalen   als   Erregungssignal   zwischen   dem
höchsten Frequenzbin, dem ein Bit zugeordnet
ist, des Frequenzdomänensignals und dem


                                                  14/120

          höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes, wobei n 0 oder eine
          ganze Zahl oder eine nicht ganze Zahl größer
          als 0 ist, m eine positive ganze Zahl ist und m
          gleich einem Wert einer Menge von Frequenzbins zwischen dem höchsten Frequenzbin, dem
          ein Bit zugeordnet ist, und dem voreingestellten
          Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes ist.


Die Patentansprüche 2 bis 5 sind unmittelbar oder mittelbar auf Patentanspruch 1
und die Patentansprüche 7 bis 10 sind unmittelbar oder mittelbar auf Patentanspruch 6 rückbezogen; wegen ihres Wortlauts wird auf die Akte verwiesen.


Die Klägerinnen sind der Ansicht, der jeweilige Gegenstand gemäß den Patentansprüchen 1 und 6 sei nicht patentfähig.

Die Klägerinnen stützen ihr Vorbringen u. a. auf folgende Dokumente:

     CHAN             MFG10               YAO, S.;   CHAN, Ch.-F.:     Block-based
                                          speech bandwidth extension system with
                                          separated envelope energy ratio estimation. In: 13th European Signal Processing
                                          Conference, 2005 September 4-8, Antalya, Turkey. January 2008, 4 Seiten

     CN‘072           MFG16               CN 101471072 B mit englischer Übersetzung als Anlage MFG16a

     CN‘664           MFG17               CN 101853664 A mit englischer Übersetzung als Anlage MFG17a

     DEN BRINKER MFG20 / NK10             DEN BRINKER, A. C. et. al.: An Overview
                                          of the Coding Standard MPEG-4 Audio
                                          Amendments 1 and 2: HE-AAC, SSC, and




                                                                             15/120

                         HE-AAC v2. In: EURASIP Journal on Audio, Speech, and Music Processing 2009,
                         Published on: 3 June 2009, S. 1 - 21

DIETZ      MFG9          DIETZ, M. et. al.: Spectral Band Replication, a novel approach in audio coding. In:
                         Audio Engineering Society Convention
                         Paper 5553, Presented at the 112th Convention, 2002 May 10-13, Munich. S. 1 - 8

GAO        NK3           US 2012/0016667 A1

…          MFG25         Technisches          Gutachten           zu
                         EP 2 940 685 B1, 12. Januar 2024, …

HOEG       NK8           Hoeg, W.; Lauterbach, Th.: Digital Audio
                         Broadcasting, Principles and Applications
                         of DAB, DAB+ and DMB, Third Edition,
                         John Wiley and Sons, Ltd., Copyright
                         2009, ISBN 978-0-470-51037-7, S. v – xi,
                         107 - 109

KIM        MFG12 / NK1   Kim, M. et. al.: High-quality scalable audio
                         codec. In: Proceedings of SPIE, Vol.
                         6777, 67770E, 10 September 2007, Seiten 67770E-1 – 67770E-11

KORNAGEL   MFG7 / NK6    KORNAGEL, U.: Spectral Widening of the
                         Excitation Signal for Telephone-Band
                         Speech Enhancement. In: 7th International Workshop on Acoustic Echo and
                         Noise control, Darmstadt University of
                         Technology, 10.-13. September 2001,
                         Proceedings, S. 215-218

LARSEN     NK5           Larsen, E.; Aarts, R. M.: Audio Bandwidth
                         Extension. Applications of Psychoacoustics, Signal Processing and Loudspeaker


                                                               16/120

                           Design. John Wiley & Sons, Ltd., Copyright 2004. ISBN 0-470-85864-8, S. v –
                           xxiii, 1 – 287

LIU         MFG14          Liu, Ch.-M. et. al.: Compression Artifacts
                           in Perceptual Audio Coding. In: IEEE
                           Transactions on Audio, Speech, and Language Processing, Vol. 16, No. 4, Mai
                           2008, S. 681 - 695

MELTZER     MFG21 / NK13   MELTZER, S.; MOSER, G.: MPEG-4 HE-AAC v2 – audio coding for today’s digital
                           media world. In: EBU Technical Review –
                           Januar 2006, S. 1 - 12

MPEG-4      MFG8/ NK2      International Standard ISO/IEC 14496-3
                           Fourth edition 2009-09-1: Information
                           technology – Coding of audio-visual objects – Part 3: Audio. Reference number
                           ISO/IEC 14496-3:2009(E). 1416 Seiten

NAGEL       NK11           NAGEL, F.;       DISCH, S.:   A   Harmonic
                           Bandwidth Extension Method for Audio
                           Codecs. In: IEEE ICASSP 2009, S. 145 -
                           148

NEUENDORF   MFG11          WO 2012/126893 A1

            NK2b           Erläuterungen der Klägerin zu 2 zum
                           MPEG-4 Standard, eine Seite

            NK2c           Erläuterungen der Klägerin zu 2 zum
                           MPEG-4 Standard, zwei Seiten

            NK2d           Fraunhofer FDK AAC Codec Library for
                           Android, Copyright 1995 – 2012 Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e.V., Fraunhofer



                                                                17/120

                     Institute for Integrated Circuits IIS, acht
                     Seiten

            NK2e     Erläuterungen der Klägerin zu 2 zum
                     MPEG-4 Standard: Bestimmung von
                     bs_start_freq in der Fraunhofer-Implementierung des MPEG-4-SBR-Encoderes, fünf Seiten

RAMABADRAN NK4       WO 2010/091013 A1

SAMSUNG     HLNK10   KR 10-2004-0086879 mit englischsprachiger Übersetzung als Anlage HLNK10a

SAMSUNG_1   MFG22    WO 2012/036487 A2

SENG        NK7      SENG, Ch. K. et. al.: Low Power Spectral
                     Band Replication Technology for the
                     MPEG-4 Audio Standard. In: IEEE ICICS-PCM 2003, 15-18 December 2003, Singapore, S. 1408 - 1412

TALEB       HLNK9    US 2010/0241437 A1

TANG        MFG15    Tang,     Sh.-H.:   Efficient   Design   of
                     Time/Frequency Grid in HE-AAC Encoder. Masterarbeit, Juni 2006, Institute
                     of Computer Science and Information Engineering National Chiao Tung University,
                     S. i – ix, 1 - 65

TSUJINO     MFG24    TSUJINO, K.; KIKUIRI, K.: Low-Complexity Bandwidth Extension in MDCT Domain
                     for Low-Bitrate Speech Coding. ICASSP
                     2009, S. 4145 - 4148




                                                          18/120

     VARY              MFG23               VARY, P.; MARTIN, R.: Digital Speech
                                           Transmission. Enhancement, Coding and
                                           Error Concealment, John Wiley & Sons,
                                           Ltd., England. 2006. ISBN 0-471-56018-
                                           9, S. v – xvi, 73 - 117

     VOLBERT           HLNK13              Volbert, K.: Grundlagen der Informatik –
                                           Einführung in Berechenbarkeit und Komplexität, Hochschule für angewandte Wissenschaften Fakultät Informatik und Mathematik, Wintersemester 2010/11, Regensburg, 12./13. Januar 2011, 14 Seiten

     Wolters           NK9                 Wolters, M. et. al.: A closer look into
                                           MPEG-4 High Efficiency AAC. In: Audio
                                           Engineering Society, Convention Paper
                                           5871, Presented at the 115th Convention,
                                           2003 October 10-13, New York, NY, USA,
                                           S. 1 – 16

Die Klägerinnen sind der Ansicht, die Gegenstände nach den Ansprüchen 1 und 6
seien bereits nicht neu, insbesondere aus dem MPEG-4 – Standard, DEN BRIN-KER, KORNAGEL, KIM, TALEB und SAMSUNG bekannt. Zumindest beruhten die
Gegenstände nach den Ansprüchen 1 und 6 nicht auf einer erfinderischen Tätigkeit
gegenüber dem verfahrensgegenständlichen Stand der Technik.


Die Klägerin zu 1 beantragt,

      das europäische Patent 2 940 685 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der Patentansprüche 1, 3, 4, 5 (zweite Alternative), 6, 8, 9 und 10 (zweite Alternative)
      für nichtig zu erklären.




                                                                                 19/120

Die Klägerin zu 2 beantragt,

      das europäische Patent 2 940 685 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für nichtig
      zu erklären.


Die Beklagte beantragt,

      die Klagen abzuweisen,

hilfsweise, die Klagen abzuweisen,

      soweit sie sich auch gegen eine der Fassungen des Streitpatents nach den Hilfsanträgen

      Hilfsantrag 0, eingereicht mit Schriftsatz vom 10. November 2023,

      Hilfsanträgen 1 und 2, jeweils eingereicht mit den Widerspruchsbegründungen vom 13. September 2022 (Verfahren 4 Ni 49/22 (EP)) bzw. vom
      12. Juli 2022 (Verfahren 4 Ni 53/22 (EP)),

      Hilfsantrag 3.0, eingereicht mit Schriftsatz vom 10. November 2023,

      Hilfsantrag „Abhängig 1“, überreicht in der mündlichen Verhandlung am
      26. Januar 2024,

      Hilfsantrag 3.0‘, überreicht in der mündlichen Verhandlung am 26. Januar 2024,

      Hilfsantrag 3.0‘‘, überreicht in der mündlichen Verhandlung am 26. Januar 2024,

      Hilfsantrag 3, eingereicht mit den Widerspruchsbegründungen vom
      13. September 2022 (Verfahren 4 Ni 49/22 (EP)) bzw. vom 12. Juli 2022
      (Verfahren 4 Ni 53/22 (EP))

      Hilfsantrag 3a vom 28. Februar 2023,

      Hilfsanträgen 4 und 5, jeweils eingereicht mit den Widerspruchsbegründungen vom 13. September 2022 (Verfahren 4 Ni 49/22 (EP)) bzw. vom
      12. Juli 2022 (Verfahren 4 Ni 53/22 (EP)), sowie

      Hilfsantrag „Abhängig 2“, überreicht in der mündlichen Verhandlung am
      26. Januar 2024,


                                                                            20/120

         und zwar in dieser angegebenen Reihenfolge, richten, mit der Maßgabe,
         dass die Hilfsanträge jeweils als geschlossener Anspruchssatz gestellt
         werden.


Die Beklagte tritt der Argumentation der Klägerinnen entgegen und ist der Auffassung, der Gegenstand des Streitpatents nach den Patentansprüchen 1 und 6 sei
gegenüber dem Stand der Technik neu und beruhe auch auf einer erfinderischen
Tätigkeit. Der Gegenstand des Streitpatents im angegriffenen Umfang sei wenigstens in einer der verteidigten Fassungen nach den eingereichten Hilfsanträgen
schutzfähig.


Zur Stützung ihrer Argumentation verweist die Beklagte u. a. auf die folgenden Dokumente:

     Kopiervorgang      NB6      Grafische Darstellung zur Erläuterung der Erfindung
     BESSETTE           NB10     Bessette, B. et. al.: The Adaptive Multirate Wideband Speech Codec (AMR-WB). In: IEEE Transactions on Speech and Audio Processing, Vol. 10,
                                 No. 8, November 2002, S. 620 - 636
     …                  NB11     Gutachterliche Stellungnahme zum Europäischen
                                 Patent EP 2 940 685 B1, …



Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 0 lauten (Änderungsfassung):




                                                                             21/120

22/120

23/120

24/120

Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 1 lauten (Änderungsfassung):




                                                                         25/120

26/120

27/120

Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 2 lauten (Änderungsfassung):




                                                                         28/120

29/120

30/120

Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 3.0 lauten (Änderungsfassung):




                                                                        31/120

32/120

33/120

Mit Hilfsantrag „Abhängig 1“ verteidigt die Beklagte ausschließlich die Patentansprüche 4 und 5 sowie 9 und 10 nach erteilter Fassung.


Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 3.0‘ lauten (Änderungsfassung):




                                                                               34/120

35/120

36/120

37/120

In Hilfsantrag 3.0‘‘ ändert die Beklagte gegenüber Hilfsantrag 3.0‘ lediglich die unbestimmten Artikel in Zeile 4 von Patentanspruch 1 in der Ergänzung „obtain a frequency domain signal, a signal type, and a frequency envelope of a bandwidth extension frequency band;“ bzw. in Patentanspruch 6 in dem Einschub „wherein the
frequency envelope of the bandwidth extension frequency band is acquired by an
acquiring module (35) based on a signal type“ in bestimmte Artikel „… the signal
type …“.



Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 3 lauten (Änderungsfassung):




                                                                               38/120

39/120

40/120

Die Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 3a lauten (Änderungsfassung):




                                                                      41/120

42/120

43/120

44/120

Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 4 lauten (Änderungsfassung):




                                                                         45/120

46/120

47/120

Patentansprüche 1 und 6 in der Fassung nach Hilfsantrag 5 lauten (Änderungsfassung):




                                                                         48/120

49/120

50/120

Mit Hilfsantrag „Abhängig 2“ verteidigt die Beklagte ausschließlich die Patentansprüche 5 (2. Alternative) sowie 10 (2. Alternative) nach erteilter Fassung.


Wegen des jeweiligen Wortlauts der abhängigen Ansprüche der Hilfsanträge wird
auf die Akte verwiesen.


Die Klägerinnen treten auch den Hilfsanträgen entgegen und sehen die Gegenstände nach den unabhängigen Patentansprüchen in der Fassung der jeweiligen
Hilfsanträge als nicht schutzfähig an. Die Gegenstände nach den Hilfsanträgen
seien bereits unzulässig erweitert und den ursprünglichen Unterlagen nicht als zur
Erfindung gehörend zu entnehmen. Darüber hinaus seien die Gegenstände der unabhängigen Patentansprüche nach den Hilfsanträgen auch mit den hinzugefügten
Merkmalen nicht neu und nicht erfinderisch. Die in der mündlichen Verhandlung
vom 26. Januar 2024 von der Beklagten überreichten Hilfsanträge 3.0‘ und 3.0‘‘




                                                                               51/120

seien als verspätet zurückzuweisen, soweit der Senat deren Zulässigkeit bejahen
würde.


Der Senat hat den Parteien einen Hinweis vom 2. Dezember 2022 zugeleitet und
hierin Fristen zur Stellungnahme gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, das Protokoll der mündlichen Verhandlung vom 26. Januar 2024 sowie den weiteren Akteninhalt Bezug genommen. Die Beklagte hat nach Schluss der mündlichen Verhandlung mit nicht
nachgelassenen Schriftsatz vom 18. März 2024 weiter vorgetragen. Die Klägerin
zu 1 hat diesen Vortrag mit Schriftsatz vom 19. März 2024 als verspätet gerügt und
mit Schriftsatz vom 7. Mai 2024 erwidert. Die Klägerin zu 2 hat mit Schriftsätzen
vom 20. März 2024 und 15. April 2024 zu den Ausführungen der Beklagten Stellung
genommen.




                          Entscheidungsgründe


                                         A.


Auf die zulässigen Klagen ist das Streitpatent in der erteilten Fassung für nichtig zu
erklären. Denn insoweit ist jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ
i. V. m. Art. 52, 54, 56 EPÜ gegeben. Auch in den Fassungen nach den Hilfsanträgen erweist sich das Streitpatent als nicht patentfähig.




                                                                                52/120

     I.      Zum Streitpatent (in erteilter Fassung), zur Aufgabe, zum Fachmann und zur Auslegung


1.        Das Streitpatent befasst sich mit einem Verfahren zur Vorhersage eines
Bandbreiterweiterungs-Frequenzbandsignals und einer Decodiervorrichtung (Streitpatentschrift, Abs. 0001, Oberbegriff der Ansprüche 1 und 6).


Zur Reduzierung der Speicher- bzw. Übertragungsressourcen und zur Erhöhung
der Qualität von Musiksignalen bei gleichzeitiger Gewährleistung der Qualität von
Sprachsignalen sei es weit verbreitet, Audiosignale vom Zeit- in den Frequenzbereich zu transformieren und danach zu komprimieren und zu kodieren (Abs. 0002,
0003). Auch ein Hochfrequenzbandsignal in einem Audiosignal werde mittels einer
FFT, MDCT oder einer DCT (Fast Fourier, Modified Discrete Cosine, Discrete Cosine Transform) in den Frequenzbereich transformiert und anschließend kodiert
(Abs. 0004). Im Falle einer niedrigen Bitrate würden jedoch die meisten Bits zur
präzisen Quantisierung der Niedrigfrequenzbandsignale verwendet und nur einige
wenige Bits zur groben Quantisierung und Codierung der spektralen Einhüllenden
der Hochfrequenzbandsignale. Die Quantisierungsparameter der Niedrigfrequenzbandsignale, die Anregungssignale und Frequenzeinhüllende umfassen, würden
zusammen mit der Einhüllenden der Hochfrequenzbandsignale in einem Bitstrom
zur einem Dekodierer übertragen (Abs. 0005).


Dieser stelle die Niedrigfrequenzbandsignale gemäß den empfangenen Quantisierungsparametern wieder her und prädiziere Anregungssignale im Hochfrequenzband anhand der Anregungssignale im niedrigen Frequenzbereich unter Verwendung einer Bandbreitenerweiterungs-Technologie (BWE, Band Width Extension).
Die Frequenzeinhüllende des Hochfrequenzbandsignals modifiziere das prädizierte
Anregungssignal des Hochfrequenzbandsignals (Abs. 0006).


Hoch- und Niedrigfrequenzband seien getrennt durch den höchsten Frequenzwert,
dem ein Bit zugeordnet sei. Bei der BWE-Technologie werde ein Anregungssignal
im Niedrigfrequenzband in das Hochfrequenzband kopiert und dort als Anregungssignal verwendet (Abs. 0007).



                                                                               53/120

Ein Nachteil der aus dem Stand der Technik bekannten BWE-Methode zur Vorhersage eines Bandbreitenerweiterungssignals sei, dass in verschiedenen Rahmen
Anregungssignale verschiedener Niedrigfrequenzbandsignale in dasselbe Hochfrequenzbandsignal kopiert werden könnten, was zu Diskontinuitäten der Anregungssignale und verringerter Qualität der vorhergesagten Bandbreitenerweiterungssignale und der Hörqualität führen könne (Abs. 0008, 0019). Zudem würde der Dekodierer bei der Prädiktion des Hochfrequenzbandsignals den Signaltyp (bspw. harmonische / nicht-harmonische Signale) nicht berücksichtigen und immer die gleiche
spektrale Einhüllende verwenden, was das Rauschen erhöhen und zu einem relativ
großen Fehler zwischen dem per BWE erzeugten und dem tatsächlichen Hochfrequenzbandsignal führen könne (Abs. 0019).



2.    Das Streitpatent stellt sich daher die Aufgabe, mit einem Verfahren zur Vorhersage eines bandbreitenerweiterten Frequenzbandsignals nach Anspruch 1 und
einer Dekodiervorrichtung nach Anspruch 6 die vorgenannten technischen Probleme zu lösen, insbesondere für Kontinuität zwischen den prädizierten BWE-Signalen aufeinanderfolgender Rahmen zu sorgen und die Qualität des vorhergesagten
bandbreitenerweiterten Frequenzbandsignals und damit die Hörqualität eines Audiosignals zu verbessern (Abs. 0010, 0019, 0021, 0028, 0056, 0057, 0062, 0074).



3.    Maßgeblicher Fachmann zur Bearbeitung und Lösung der zuvor geschilderten Aufgabe ist ein Ingenieur mit einem universitären Abschluss (Diplom oder Master) im Bereich der Elektro-, Nachrichten-, oder Informationstechnik, der über eine
mehrjährige Berufserfahrung auf dem Gebiet der Audiocodecs verfügt. Er verfolgt
die Sitzungen der einschlägigen Normierungs- und Standardisierungsgremien und
kennt die dort diskutieren Entwicklungsvorschläge.



4.   Das Streitpatent weist insgesamt zehn Patentansprüche auf mit dem unabhängigen Verfahrensanspruch 1 und dem unabhängigen Vorrichtungsanspruch 6




                                                                             54/120

sowie den abhängigen Ansprüchen 2 bis 5 und 7 bis 10, die alle direkt oder indirekt
auf die Ansprüche 1 und 6 rückbezogen sind.


Der Patentanspruch 1 lautet mit einer Gliederung, wobei in der deutschen Übersetzung einige in der Streitpatentschrift verwendete Wörter durch fachübliche Begriffe
ersetzt sind (Änderungen gegenüber der Streitpatentschrift sind durch Unterstreichung gekennzeichnet):

     1       A method for predicting a bandwidth extension frequency band signal,
             comprising:
             Verfahren zur Vorhersage eines Bandbreitenerweiterungs-Frequenzbandsignals, umfassend:
     1.1       demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;
               Demultiplexen (100) eines empfangenen Bitstroms und Dekodieren
               des demultiplexten Bitstroms, um ein Frequenzbereichssignal zu erhalten;
     1.2       determining (101) whether a highest frequency bin, to which a bit is
               allocated, of the frequency domain signal is less than a preset start
               frequency bin of a bandwidth extension frequency band;
               Bestimmen (101), ob ein höchstes Frequenzbin, dem ein Bit zugeordnet ist, des Frequenzbereichssignals kleiner ist als ein voreingestelltes
               Anfangs-Frequenzbin eines Bandbreitenerweiterungs-Frequenzbandes;
     1.3       predicting (102) an excitation signal of the bandwidth extension frequency band
               Vorhersagen (102) eines Anregungssignals des Bandbreitenerweiterungs-Frequenzbandes
     1.3.1        according to an excitation signal within a predetermined frequency
                  band range of the frequency domain signal and the preset start frequency bin of the bandwidth extension frequency band




                                                                                  55/120

          gemäß einem Anregungssignal in einem vorbestimmten Frequenzbandbereich des Frequenzbereichssignals und dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes,
1.3.2     when the highest frequency bin to which a bit is allocated is less
          than the preset start frequency bin of the bandwidth extension frequency band;
          wenn das höchste Frequenzbin, dem ein Bit zugeordnet ist, kleiner
          ist als das voreingestellte Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes;
1.4     predicting (103) the excitation signal of the bandwidth extension frequency band
        Vorhersagen (103) des Anregungssignals des Bandbreitenerweiterungs-Frequenzbandes
1.4.1     according to the excitation signal within the predetermined frequency band range of the frequency domain signal, the preset start
          frequency bin of the bandwidth extension frequency band, and the
          highest frequency bin to which a bit is allocated
          gemäß einem Anregungssignal in dem vorbestimmten Frequenzbandbereich des Frequenzbereichssignals, dem voreingestellten
          Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin, dem ein Bit zugeordnet ist,
1.4.2     when the highest frequency bin to which a bit is allocated is no less
          than the preset start frequency bin of the bandwidth extension frequency band; and
          wenn das höchste Frequenzbin, dem ein Bit zugeordnet ist, nicht
          kleiner ist als das voreingestellte Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes; und
1.5     predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
        frequency band and a frequency envelope of the bandwidth extension
        frequency band;




                                                                         56/120

        Vorhersagen (104) des Bandbreitenerweiterungs-Frequenzbandsignals gemäß dem vorhergesagten Anregungssignal des Bandbreitenerweiterungs-Frequenzbandes und einer Frequenzhüllkurve des
        Bandbreitenerweiterungs-Frequenzbandes;
1.6     wherein the predicting an excitation signal of the bandwidth extension
        frequency band according to an excitation signal within a predetermined frequency band range of the frequency domain signal and the
        preset start frequency bin of the bandwidth extension frequency band
        comprises:
        wobei das Vorhersagen eines Anregungssignals des Bandbreitenerweiterungs-Frequenzbandes gemäß einem Anregungssignal in einem
        vorbestimmten Frequenzbandbereich des Frequenzbereichssignals
        und dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes umfasst:
1.6.1     making n copies of the excitation signal within the predetermined
          frequency band range of the frequency domain signal, and
          Erzeugen von n Kopien des Anregungssignals in dem vorbestimmten Frequenzbandbereich des Frequenzbereichssignals und
1.6.2     using the n copies of the excitation signal as an excitation signal
          between the preset start frequency bin of the bandwidth extension
          frequency band and a highest frequency bin of the bandwidth extension frequency band,
          Verwenden der n Kopien des Anregungssignals als Anregungssignal zwischen dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und einem höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes,
1.6.3     wherein n is an integer or a non-integer greater than 0, and n is
          equal to a ratio of a quantity of frequency bins between the preset
          start frequency bin of the bandwidth extension frequency band and
          the highest frequency bin of the bandwidth extension frequency
          band to a quantity of frequency bins within the predetermined frequency band range of the frequency domain signal; where n is an
          integer or a non-integer greater than 0; and


                                                                        57/120

          wobei n eine ganze Zahl oder eine nicht ganze Zahl größer als 0 ist
          und n gleich einem Verhältnis einer Anzahl von Frequenzbins zwischen dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin
          des Bandbreitenerweiterungs-Frequenzbandes zu einer Anzahl
          von Frequenzbins in dem vorbestimmten Frequenzbandbereich
          des Frequenzbereichssignals ist; wobei n eine ganze Zahl oder eine
          nicht ganze Zahl größer als 0 ist; und
1.7     wherein the predicting the excitation signal of the bandwidth extension
        frequency band according to the excitation signal within the predetermined frequency band range of the frequency domain signal, the preset start frequency bin of the bandwidth extension frequency band,
        and the highest frequency bin, to which a bit is allocated comprises:
        wobei das Vorhersagen des Anregungssignals des Bandbreitenerweiterungs-Frequenzbandes gemäß dem Anregungssignal in dem vorbestimmten Frequenzbandbereich des Frequenzbereichssignals, dem
        voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes und dem höchsten Frequenzbin, dem ein Bit zugeordnet ist, umfasst:
1.7.1     making a copy of an excitation signal from the mth frequency bin
          fexc_start+ above a start frequency bin fexc_start of the predetermined
          frequency band range of the frequency domain signal to an end frequency bin fexc_end of the predetermined frequency band range of
          the frequency domain signal and
          Erzeugen einer Kopie des Anregungssignals von dem m-ten Frequenzbin fexc_start+ über einem Anfangs-Frequenzbin fexc_start des vorbestimmten Frequenzbandbereichs des Frequenzbereichssignals
          bis zu einem End-Frequenzbin fexc_end des vorbestimmten Frequenzbandbereichs des Frequenzbereichssignals und
1.7.2     [making] n copies of the excitation signal within the predetermined
          frequency band range of the frequency domain signal, and
          [Erzeugen von] n Kopien des Anregungssignals in dem vorbestimmten Frequenzbandbereich des Frequenzbereichssignals und


                                                                           58/120

     1.7.3      using the two parts of excitation signals as an excitation signal between the highest frequency bin, to which a bit is allocated, of the
                frequency domain signal and the highest frequency bin of the bandwidth extension frequency band,
                Verwenden der beiden Teile der Anregungssignale als Anregungssignal zwischen dem höchsten Frequenzbin, dem ein Bit zugeordnet ist, des Frequenzbereichssignals und dem höchsten Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes,
     1.7.4      wherein n is 0 or an integer or a non-integer greater than 0, m is a
                positive integer, and m is equal to a value of a quantity of frequency
                bins between the highest frequency bin to which a bit is allocated
                and the preset start frequency bin of the bandwidth extension frequency band.
                wobei n gleich 0 ist oder eine ganze Zahl oder eine nicht ganze Zahl
                größer als 0 ist, m eine positive ganze Zahl ist und m gleich einem
                Wert einer Anzahl von Frequenzbins zwischen dem höchsten Frequenzbin, dem ein Bit zugeordnet ist, und dem voreingestellten Anfangs-Frequenzbin des Bandbreitenerweiterungs-Frequenzbandes
                ist.



5.   Der Gegenstand des Streitpatents bedarf hinsichtlich der Merkmale der angegriffenen Patentansprüche der Erläuterung.


Die inhaltliche Beurteilung des dekodiererseitigen Verfahrens (Merkmal 1.1: decoding the demultiplexed bitstream) nach Patentanspruch 1 ist auf die Dekodiervorrichtung (decoding device) nach Patentanspruch 6 in entsprechender Weise übertragbar; daher wird im Folgenden nur Patentanspruch 1 betrachtet. Im Zusammenhang mit der in Figur 8 gezeigten Ausführungsform der Dekodiervorrichtung (decoding device 80) ist angegeben, dass das beanspruchte Verfahren ganz oder teilweise in einem Dekodierprozessor (decoding processor 803) oder in einer Betriebseinheit (processing unit 804) realisiert sein kann (Abs. 0077 – 0081).




                                                                                59/120

5.1    Der Anspruch 1 ist auf ein Verfahren zur Prädiktion eines Bandbreitenerweiterungsfrequenzbandsignals (A method for predicting a bandwidth extension frequency band signal) gerichtet (Merkmal 1). Auch wenn das Streitpatent sich durchgängig mit Audiosignalen beschäftigt, sind die Ansprüche in der erteilten Fassung
nicht darauf beschränkt.


Als ersten Verfahrensschritt umfasst das beanspruchte Verfahren das Demultiplexen, d. h. das Aufteilen oder Entflechten eines empfangenen Bitstroms und Dedodieren des demultiplexten Bitstroms, um ein Frequenzbereichssignal (frequency domain signal) zu erhalten (Merkmal 1.1). Hier entnimmt der Fachmann, dass der
empfangene Bitstrom nicht nur das kodierte niederfrequente Frequenzbereichssignal, sondern auch weitere, typischerweise ebenfalls kodierte, Informationen enthält,
insbesondere die im Merkmal 1.5 genannte spektrale Einhüllende des Bandbreitenerweiterungsfrequenzbands (frequency envelope of the bandwidth extension frequency band), d. h. die Einhüllende für den hohen, in der Dekodiervorrichtung
künstlich zu erzeugenden Frequenzbereich. Zudem können – fachüblich – Hilfsinformationen vom Kodierer an den Dekodierer übertragen werden, etwa welcher Signaltyp gerade vorliegt (Anspruch 4 erteilter Fassung: decoding the bitstream to obtain a signal type).


Dem Fachmann ist bekannt, dass viele Audio-Kodierer eine Transformation der zu
übertragenen Audiosignale vom Zeit- in den Frequenzbereich durchführen und
quantisierte Spektralkomponenten des so erzeugten frequenzdiskreten Spektrums
kodieren und als Bitstrom an den Dekodierer übertragen (Absätze 0002 bis 0005).
Insofern versteht der Fachmann unter dem in Merkmal 1.1 genannten Frequenzbereichssignal insbesondere quantisierte Spektralkoeffizienten (frequency domain coefficients) eines frequenzdiskreten (Amplituden-)Spektrums für den niedrigen Frequenzbereich (Abs. 0024).


Nach den Ausführungsbeispielen gemäß den Figuren 6 und 7 führt ein Dekodierungsmodul (decoding module 30) als Teil der Dekodiervorrichtung die in Merkmal
1.1 genannten Verfahrensschritte durch (Abs. 0060, 0068). Merkmal 1.1 verlangt,




                                                                              60/120

dass der empfangene Bitstrom demultiplexiert und dekodiert wird, um ein Frequenzbereichssignal zu erhalten. Es ist nach Anspruch 1 des Streitpatents nicht ausgeschlossen, dass in weiteren Verfahrens(zwischen)schritten eine Transformation in
einen anderen Bereich, z. B. den Zeitbereich, stattfindet, solange die Anforderungen der einzelnen Merkmale erfüllt sind. Das Streitpatent verhält sich zu den Implementierungsdetails des Verfahrens bzw. der entsprechenden Vorrichtungen (Fig. 6:
30 - 34; Fig. 7: 33 – 35) nicht.


5.2    Dem Fachmann ist bekannt, dass Audio-Codecs, insbesondere im Mobilfunkbereich, Signale in als Rahmen (frames) bezeichneten Zeitabschnitten verarbeiten, wobei eine typische Rahmenlänge 20 ms beträgt (Abs. 0014).


Das höchste vom Kodierer kodierte und an den Dekodierer übertragene Frequenzbin (Merkmal 1.2: decoding … to obtain a frequency domain signal … highest frequency bin, to which a bit is allocated) kann sich im Laufe der Zeit, somit auch von
Rahmen zu Rahmen, ändern (Abs. 0008, 0019, 0021, 0028 und 0056), was nach
den Angaben im Streitpatent bei aus dem Stand der Technik bekannten Bandbreitenerweiterungsverfahren zu Qualitätsproblemen des im Dekodierer erzeugten Audiosignals führen kann. Unter einem Frequenzbin versteht der Fachmann eine Frequenzlinie, wie sie typischerweise durch eine Transformation eines abgetasteten
Signals in den Frequenzbereich entsteht. Bei jedem Frequenzbin liegt ein Spektralkoeffizient vor.


5.3    Der Fachmann kann dem Streitpatent nicht unmittelbar und eindeutig entnehmen, ob nicht nur die höchste, sondern auch die niedrigste Frequenz, die vom
Dekodierer empfangen und dekodiert wird, (rahmenweise) variabel ist.


Jedenfalls bedient sich die streitpatentgemäße dekodiererseitige Vorhersage des
Anregungssignals des Bandbreitenerweiterungsfrequenzbandes (Merkmale 1.3,
1.4: predicting (102) an excitation signal of the bandwidth extension frequency band)
eines Anregungssignals, das innerhalb eines vorbestimmten Teils des (niederfrequenten) vom Kodierer empfangenen Frequenzbereichssignals liegt (Merkmale




                                                                               61/120

1.3.1, 1.4.1, 1.6, 1.6.1, 1.7: an excitation signal within a predetermined frequency
band range of the frequency domain signal).

Nach den Ausführungsbeispielen kann die Frequenzuntergrenze fexc_start des vorbestimmten Teils des in den oberen Frequenzbereich zu kopierenden Anregungssignals bei 0 kHz bzw. bei 1,6 kHz liegen, während die Frequenzobergrenze fexc_end in
beiden Ausführungsbeispielen 4 kHz beträgt (Abs. 0040, 0053).

Dem Fachmann ist vor dem Hintergrund der gesamten Offenbarung des Streitpatents bewusst, dass sich – im Vergleich zur variablen, insbesondere rahmenweise
variablen, höchsten dekodierten Frequenz – der zu kopierende Teil des (niederfrequenten) Frequenzbereichssignals insofern „vorbestimmt“ und damit konstant ist,
als dass er vom System nur dann verändert wird, wenn sich Systemparameter, wie
die Kodierungs-Bitrate und der Signaltyp (harmonic; non-harmonic), ändern (Abs.
0035: Selection of the predetermined frequency band range from the fexc_start to the
fexc_end of the frequency domain signal is related to a signal type and an encoding
rate).

Solche Änderungen finden regelmäßig nicht an jeder Rahmengrenze, sondern seltener statt, weil anderenfalls die erfindungsgemäß angestrebte Lösung – die Vermeidung von Diskontinuitäten zwischen aufeinanderfolgenden Rahmen beim Kopieren des vorbestimmten niederfrequenten Frequenzbands in gleiche hochfrequente Frequenzbänder – nicht erreicht werden würde.


Nach der erteilten Fassung des Anspruchs 1 ist umfasst, dass der Kodierer dem
Dekodierer die (veränderte) Kodierrate und/oder den (neuen) Signaltyp signalisiert
und der Dekodierer basierend auf diesen Informationen den für die Erzeugung des
BWE-Signals zu verwendenden Frequenzbereich selbst bestimmt, dieser somit basierend auf dieser Information „vorbestimmt“ ist. Ebenso ist nach der erteilten Fassung des Anspruchs 1 nicht ausgeschlossen, dass der Kodierer dem Dekodierer
unmittelbar die Werte der Start- und Stoppfrequenz des vom Dekodierer zu verwendenden niederfrequenten Frequenzbereichs signalisiert und dieser damit insofern –
vor dem Beginn des Kopiervorgangs im Dekodierer - „vorbestimmt“ ist.




                                                                              62/120

5.4   Die Bandbreite und damit die untere (Merkmal 1.2: preset start frequency bin
of a bandwidth extension frequency band) und obere (Merkmale 1.6.2, 1.7.3: highest frequency bin of the bandwidth extension frequency band) Grenzfrequenz des
vorherzusagenden bandbreitenerweiterten Frequenzband-Signals hängen gemäß
den Angaben zu den Ausführungsbeispielen ebenfalls u. a. von der Kodierrate ab.
Für ein mit 24 bzw. 32 kbps kodiertes UWB-Signal (Ultra Wide Band) betrage die
untere Grenzfrequenz fbwe_start 6,4 kHz bzw. 8 kHz (Abs. 0031, 0053). Die im Streitpatent mit ftop_sfm bezeichnete obere Grenzfrequenz des vorherzusagenden Signals
betrage für ein WB-Signal (Wide Band) 7 kHz oder 8 kHz und für ein UWB-Signal
14 kHz oder 16 kHz (Abs. 0036, 0054), wobei die 14 kHz bei einer Kodierrate von
24 kbps gewählt würden (Abs. 0053). Für ein mit 24 kbps kodiertes UWB-Signal
ergibt somit ein (maximal) vorherzusagender Frequenzbereich von 6,4 kHz bis
14 kHz.

Der Fachmann entnimmt dem Streitpatent auch bezüglich des vorherzusagenden
oberen Frequenzbereichs, dass dieser zwar möglicherweise von Systemparametern, wie der Kodierrate, abhängig ist, die sich grundsätzlich im Betrieb ändern können, jedoch im Vergleich zu der sich häufig von Rahmen zu Rahmen verändernden
höchsten dekodierten Frequenz (Merkmal 1.2: decoding … to obtain a frequency
domain signal … highest frequency bin, to which a bit is allocated) als vorbestimmt
bzw. voreingestellt (preset start frequency bin of a bandwidth extension frequency
band) angesehen werden können.


Nach der erteilten Fassung des Anspruchs 1 ist es möglich, dass die Frequenzgrenzen des BWE-Bereichs, insbesondere dessen voreingestellte Startfrequenz, unmittelbar vom Kodierer an den Dekodierer signalisiert werden oder dass der Dekodierer
sich diese Werte aus vom Kodierer empfangenen Parameterwerten, etwa hinsichtlich der Kodierrate, selber errechnet. In beiden Varianten sind die Frequenzgrenzen
vor dem Beginn des Kopiervorgangs voreingestellt im Sinne des Merkmals 1.2.


5.5   In welcher Weise und wie oft der vorbestimmte Teil des niederfrequenten
Anregungssignals kopiert wird, um den vorherzusagenden oberen Frequenzbereich




                                                                               63/120

vollständig zu füllen, wird im Streitpatent detailliert beschrieben, wobei es sich um
eine prinzipiell einfache Kopiervorschrift handelt.

Zunächst wird gemäß Merkmal 1.2 (determining (101) whether a highest frequency
bin, to which a bit is allocated, of the frequency domain signal is less than a preset
start frequency bin of a bandwidth extension frequency band) unterschieden, ob die
höchste Frequenz flast_sfm des im Dekodierer dekodierten niederfrequenten Frequenzbereichssignals kleiner ist als die voreingestellte untere Frequenz fbwe_start des
vorherzusagenden Bandbreitenerweiterungsfrequenzbandes (Fig. 4, Schritt 203:
flast_sfm < fbwe_start ?).


Merkmal 1.2 gibt zwar nicht an, wie die Prüfung genau ausgeführt wird, jedoch erkennt der Fachmann anhand der Reihenfolge der Merkmale 1.1 und 1.2 und der
Gesamtoffenbarung des Streitpatents, dass der Dekodierer selbst diese Bestimmung bzw. Prüfung durchführt (Abs. 0020, Schritt 101; Abs. 0029, Schritte 202, 203;
Figuren 6, 7: Determining module 31)


a)       Wenn die in Merkmal 1.2 genannte Abfrage mit JA beantwortet wird (Merkmal 1.3.2: when the highest frequency bin to which a bit is allocated is less than
the preset start frequency bin of the bandwidth extension frequency band), d. h
wenn flast_sfm < fbwe_start gilt, hängt die in Merkmal 1.3 genannte Vorhersage gemäß
den Angaben in den Merkmalen 1.3.1 und 1.6 von dem niederfrequenten Anregungssignal in einem vorbestimmten Frequenzband (            _    ,   _   ) und der voreingestellten Startfrequenz des vorherzusagenden Bandbreitenerweiterungsfrequenzbereichs (              _   ) ab. Gemäß den Angaben in den Merkmalen 1.6.1, 1.6.2
und 1.6.3 verläuft der Kopiervorgang dann wie folgt:

     ·   Bestimmen einer Zahl n (ganzzahlig oder nicht-ganzzahlig und größer als
         Null) mittels Teilen der Anzahl der Frequenzwerte im vorherzusagenden Frequenzbereich (Merkmal 1.6.3: quantity of frequency bins between the preset
         start frequency bin of the bandwidth extension frequency band and the highest frequency bin of the bandwidth extension frequency band) durch die
         Anzahl der Frequenzwerte des vorbestimmten Teils des (niederfrequenten)



                                                                                  64/120

       Frequenzbereichssignals (Merkmal 1.6.3: quantity of frequency bins within
       the predetermined frequency band range of the frequency domain signal);
       unter der Voraussetzung eines konstanten Frequenzabstandes zwischen
       den Frequenzwerten jeweils benachbarter Frequenzbins können statt der
       Anzahl der Bins auch die entsprechenden Frequenzdifferenzen durcheinan-
                                                        _               _
       der geteilt werden (Abs. 0042), d. h.:   =                            ,
                                                        _           _

   ·   Erzeugen (making) von n Kopien des Anregungssignals in dem vorbestimmten Frequenzbandbereich (       _    ,       _       ) des (niederfrequenten) Frequenzbereichssignals (Merkmal 1.6.1),
   ·   Verwenden (using) der erzeugten n Kopien des niederfrequenten Anregungssignals als Anregungssignal zwischen der vorbestimmten Startfrequenz des Bandbreitenerweiterungsbandes (                _           ) und der höchsten
       Frequenz des Bandbreitenerweiterungsbandes (                 _       ) (Merkmal 1.6.2).


Dabei kann gemäß den Ausführungsbeispielen das Kopieren der n Kopien als sequentielles Kopieren des Anregungssignals gemäß dem ganzzahligen Anteil der
Zahl n (sofern n > 1) und Einfügen in den vorherzusagenden Frequenzbereich beginnend an dessen unterer Grenzfrequenz (fbwe_start) und anschließendes Kopieren
des Anregungssignals gemäß dem nicht-ganzzahligen Anteil der Zahl n und entsprechendes Einfügen in den oberen Frequenzbereich ausgeführt sein.


Die ganzzahligen Kopien des Anregungssignals können auch abwechselnd in „normaler“ und „umgekehrter“ Reihenfolge in den oberen Frequenzbereich eingefügt
werden (Abs. 0038, Sp. 14, Z. 9 bis 17: mirror copy … fold copy … a forward copy
… and a backward copy … are alternately made in sequence).


Die einzelnen Kopien des Anregungssignals können alternativ auch von „oben“ in
den vorherzusagenden Bereich kopiert werden und zwar beginnend mit dem nichtganzzahligen Teil gefolgt von den ganzzahligen Kopien (Abs. 0039, 0040). Im Ergebnis besteht kein Unterschied zu dem Kopieren von „unten“, denn maßgeblich
zur Erreichung des angestrebten Ziels ist, welche niederfrequenten Spektralwerte




                                                                                          65/120

sich nach dem Kopiervorgang an welchem hochfrequenten „Platz“ befinden. Auf die
Reihenfolge des Kopierens kommt es dabei nicht an.


b)       Wenn die in Merkmal 1.2 genannte Abfrage mit NEIN beantwortet wird
(Merkmal 1.4.2: when the highest frequency bin to which a bit is allocated (        _    )
is no less than the preset start frequency bin of the bandwidth extension frequency
band (       _    )), d. h. wenn flast_sfm ≥ fbwe_start gilt, hängt die in Merkmal 1.4 genannte Vorhersage gemäß den Angaben in den Merkmalen 1.4.1 und 1.7 von dem
Anregungssignal in dem vorbestimmten Frequenzbandbereich (                _    ,    _   ),
der voreingestellten niedrigsten Frequenz (         _       ) des vorherzusagenden Bandbreitenerweiterungsbereichs und der höchsten Frequenz (             _   ) des dekodierten
(niederfrequenten) Frequenzbereichssignals ab.


Gemäß den Angaben in den Merkmalen 1.7.1 bis 1.7.4 verläuft der Kopiervorgang
dann wie folgt:

     ·   Berechnen einer Zahl m als Anzahl der Frequenzbins zwischen der höchsten
         dekodierten Frequenz und der voreingestellten Startfrequenz des BWE-Bereichs, wobei m eine positive ganze Zahl ist (Merkmal 1.7.4), damit entspricht m der Frequenzdifferenz zwischen flast_sfm und fbwe_start,
     ·   Erzeugen (making) von einer Kopie (nur) eines Teils des Anregungssignals,
         nämlich nur von dem m-ten Frequenzbin fexc_start+ oberhalb des Startfrequenzbins fexc_start bis zu dem Endfrequenzbin fexc_end des vorbestimmten Frequenzbandbereichs des (niederfrequenten) Frequenzbereichssignals (Merkmal 1.7.1),
     ·   (einmaliges) Verwenden (using) dieser solchermaßen erzeugten Teilkopie
         des niederfrequenten Anregungssignals als Anregungssignal zwischen der
         höchsten dekodierten Frequenz flast_sfm und der höchsten Frequenz ftop_sfm
         des Bandbreitenerweiterungsbandes (Merkmal 1.7.3).
     ·   Erzeugen (making) von n Kopien des Anregungssignals in dem vorbestimmten Frequenzbandbereich (         _    ,       _    ) des niederfrequenten Frequenzbereichssignals (Merkmal 1.7.2), wobei dem Fachmann unmittelbar
         klar ist, wie nun die Zahl n (ganzzahlig oder nicht-ganzzahlig und größer als


                                                                                    66/120

         Null; Merkmal 1.7.4) zu bestimmen ist, um das Bandbreitenerweiterungsfrequenzband nach der einmaligen Verwendung der Teilkopie vollständig zu
         füllen, nämlich analog zu Merkmal 1.6.3, d. h. mittels Teilen der Anzahl der
         Frequenzwerte im restlichen vorherzusagenden Frequenzbereich durch die
         Anzahl der Frequenzwerte des vorbestimmten Teils des niederfrequenten
                                                            _         (   _       _   _      )
         Frequenzbereichssignals, mithin:          =                                         ,
                                                                              _   _

     ·   Verwenden (using) der erzeugten n Kopien des niederfrequenten Anregungssignals als zweiten Teil des Anregungssignals, nun zwischen
         flast_sfm + (flast_sfm – fbwe_start) und der höchsten Frequenz des Bandbreitenerweiterungsbandes (       _    ) (Merkmal 1.7.3 i. V. m. den Merkmalen 1.7.1
         und 1.7.4).


c)       Eine beispielhafte anschauliche Darstellung der streitpatentgemäßen Kopiervorgänge für die beiden möglichen Fälle zeigt folgende Abbildung aus einem abgeschlossenen Nichtigkeitsverfahren zum Streitpatent:




                                Erster Fall: flast_sfm < fbwe_start




                                                                                          67/120

                                  Zweiter Fall: flast_sfm > fbwe_start

Eine von der Beklagten angefertigte Darstellung zeigt den ersten Fall in zwei Rahmen und den zweiten Fall in einem dritten Rahmen:




     Anl. NB6: Rahmen1, 2: flast_sfm < fbwe_start, Rahmen 3: flast_sfm > fbwe_start,



d)    Ein streitpatentgemäßes Verfahren gemäß den Merkmalsgruppen 1.6 und
1.7 und ein anderes Verfahren, welches stets gemäß Merkmalsgruppe 1.6 kopiert


                                                                                       68/120

und nur im Falle einer „Überlappung“ (d. h. von übertragenen, aber im vorgesehenen Erweiterungsbereich liegenden Frequenzbins) die im „Überlappungsbereich“
liegenden, kopierten Frequenzbins durch eine entsprechende Anzahl von „echten“,
also übertragenen Frequenzbins ersetzt, liefern zwar das gleiche Ergebnis, jedoch
unterscheiden sich die beiden Verfahren in einzelnen Verfahrensschritten deutlich
voneinander.


5.6   Der Fachmann versteht die Merkmalsgruppen 1.6 und 1.7 so, dass zunächst die Werte der Zahlen „n“ und „m“ gemäß den Angaben in den Merkmalen
1.6.3 und 1.7.4 bestimmt werden, denn anderenfalls, d. h. ohne Kenntnis der beiden Zahlenwerte, könnten nicht „n Kopien“ (Merkmal 1.6.1: making n copies) bzw.
„eine Kopie“ einer bestimmten Breite (Merkmal 1.7.1: making a copy … mth frequency bin; Merkmal 1.7.4: m is equal to …) erzeugt und anschließend diese Kopien verwendet werden (Merkmal 1.6.2: using the n copies; Merkmal 1.7.3: using
the two parts).


5.7   Der Fachmann erkennt, dass sich durch die vorstehend erläuterte Art und
Weise der Kopiervorgänge für den Fall der Merkmalsgruppe 1.6 eine Situation einstellen kann (aber nicht muss), in der im Frequenzbereich eine „Lücke“ zwischen
der höchsten dekodierten Frequenz flast_sfm und der Startfrequenz fbwe_start des Bandbreitenerweiterungsfrequenzbands ergeben, wie dies in der oben eingeblendeten
Anlage NB6 der Beklagten für die Rahmen 1 und 2 dargestellt ist und wie die nachstehend einkopierte Figur 5a zeigt:




                                                                                69/120

 Fig. 5a, 5b der Streitpatentschrift mit Kolorierung und Kommentierung durch den Senat



Das Streitpatent macht hierzu keine Angaben; offenbar nimmt es diese, möglicherweise nachteilige, „Lücke“ im Frequenzbereich in Kauf, um die angestrebten Vorteile zu erzielen.




                     II.   Zur erteilten Fassung (Hauptantrag)

Auf die zulässigen Klagen ist das Streitpatent in der erteilten Fassung für nichtig zu
erklären. Denn insoweit ist jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ
i. V. m. Art. 52, 54 EPÜ gegeben.


Der Gegenstand gemäß des auf ein Verfahren zur Vorhersage eines Bandbreitenerweiterungs-Frequenzbandsignals gerichteten Patentanspruchs 1 in der erteilten
Fassung – und damit auch der Gegenstand des auf eine entsprechende Dekodiervorrichtung gerichtete Patentanspruchs 6 – ist aus dem MPEG-4 Standard
(MFG8 / NK2) bekannt.




                                                                                 70/120

1.     Der MPEG-4 Audiostandard (Part 3: Audio) integriert viele verschiedene, modular einsetzbare Sprach- und Audio-Codierungswerkzeuge (0 Introduction, Seite v,
0.1 Overview, Seite vii, 0.3 The MPEG-4 Audio tool set, 0.3.1 Speech coding tools;
Seite ix, 0.3.2 Audio coding tools).


Zu den allgemeinen Audio-Codierungswerkzeugen gehören MPEG-4 AAC (Advanced Audio Coding) und MPEG-4 SBR (Spectral Band Replication). Letzteres ist ein
Bandbreitenerweiterungswerkzeug, das zur Verringerung der Bitrate oder zur Erhöhung der Audioqualität verwendet werden kann. Dabei kodiert der Kodierer zwar
die vollständigen Audioinformationen des niedrigen Frequenzbereichs, jedoch nur
eine geringe Datenmenge zur parametrischen Beschreibung des hohen Frequenzbereichs. Der Dekodierer erzeugt aus dieser, im Vergleich zur Kodierung des gesamten Audio-Frequenzbereichs verringerten, Informationsmenge den hohen Frequenzbereich durch Replikation, d. h. durch geeignetes Kopieren niederfrequenter Signalanteile in den hohen Frequenzbereich (0 Introduction, S. ix, 0.3.2.2 General Audio Coding Tools, Abschnitt MPEG-4 SBR).


MPEG-4 AAC und MPEG-4 SBR können in dem High Efficiency AAC Profile kombiniert werden (Subpart 1, S. 26, 1.5.2.1 Profiles … 10. The High Efficiency AAC Profile …; S. 50, 1.6.5.1 Generating and signaling AAC+SBR content; S. 54, Fig. 1.1).



2.     Der für das Streitpatent besonders relevante Teil des MPEG-4 Audiostandards ist der Subpart 4: General Audio Coding (GA) – AAC, TwinVQ, BSAC, der
sich mit den „allgemeinen Audio-Codier-Werkzeugen“ beschäftigt, insbesondere
der Abschnitt 4.6.18 SBR tool (Seiten 220 ff.), der sich mit dem vorstehend genannten SBR-Bandbreitenerweiterungswerkzeug befasst. Die nachfolgende wiedergegebene Figur 4.2 (Seite 5) zeigt den Aufbau eines „allgemeinen, nicht-skalierbaren
Audio-Decodierers“, der auch das SBR-Werkzeug umfasst:




                                                                             71/120

MPEG-4, Subpart 4, S. 5, Fig. 4.2 mit Kolorierung durch den Senat




                                                                    72/120

Aus der Figur 4.2 und der zugehörigen Beschreibung (Subpart 4, S. 6 – 9, 4.1.1.2
Overview of the encoder and decoder tools) entnimmt der Fachmann, dass der
AAC-Dekodierer (AAC; Huffman decoding inverse quantization rescaling) an seinem Ausgang ein Signal im Frequenzbereich abgibt, welches in den mit spectral
processing gekennzeichneten Blöcken M/S, PNS, …, TNS, dependently switched
coupling durchgängig im Frequenzbereich verarbeitet wird. Eine Filterbank (block
switching / filterbank) transformiert vom Frequenz- in den Zeitbereich; Ein- und Ausgangssignale der SBR-Decodierers (SBR decoder) liegen als Zeitbereichssignale
vor; neben dem Zeitbereichssignal des AAC-Decodierers (time domain signal from
the AAC core decoder) erhält der SBR-Dekodierer die quantisierten Einhüllenden-Daten (quantized envelope data) und verschiedene Steuerdaten (Misc. control data)
(Subpart 4, S. 9, vorletzter Absatz: SBR tool) von dem Bitstrom-Nutzlast-Deformatierer (bitstream payload deformatter).


Das genauere Zusammenwirken eines AAC-Kern-Decodierers (AAC Core Decoder) mit dem SBR-Dekodierer sowie dessen Struktur ist in der nachfolgend eingeblendeten Figur 4.46 dargestellt:




MPEG-4, Subpart 4, S. 246, Fig. 4.46 mit Kolorierung und Kommentierung durch den Senat



                                                                               73/120

Der Bitstrom-Nutzlast-Deformatierer (Bitstream Payload Deformatter) teilt den empfangenen kodierten Audiodatenstrom (Coded Audio Stream) in einen AAC Core Decoder-Teil und einen SBR-Teil (Bitstream Parser) auf. Das niederfrequente Zeitbereichssignal am Ausgang des AAC Core Decoder wird von der Analysis QMF Bank
(Quadratur Mirror Filter) in die QMF-Domäne transformiert und als Signal XLow sowohl an den HF-Generator (HF Generator) als auch an die QMF-Synthese-Filterbank (Synthesis QMF Bank) geliefert.


Die Decodierung des SBR-Teils liefert die Einhüllenden-Informationen für den zu
erzeugenden hochfrequenten Signalanteil an den Einhüllenden-Einsteller (Envelope Adjuster), während die zusätzlichen Informationen von dem HF-Generator benötigt werden, damit dieser aus seinem Eingangssignal XLow durch geeignetes Kopieren das Ausgangssignal XHigh erzeugen kann. Die QMF-Synthese-Filterbank fügt
das niederfrequente QMF-Signal XLow und das hochfrequente QMF-Signal Y zusammen und transformiert das QMF-Summensignal in ein – jetzt breitbandiges –
Zeitbereichssignal (Output PCM Samples).



3.    Die vorstehend genannten Einhüllenden-Informationen und Steuerinformationen werden dem SBR-Dekodierer in einem SBR-Erweiterungs-Datenelement
(SBR extension data element) zugeführt, das aus einem Header-Kennzeichen
(Header flag), dem Header und den eigentlichen (Einhüllenden-)Daten (Data; Side
info, Raw data) besteht:




                           MPEG-4, Subpart 4, S. 117, Fig. 4.21




                                                                            74/120

Das SBR-Datenelement wird zumeist ohne Header übertragen, denn grundlegende
Informationen wie der SBR-Frequenzbereich (main) und Steuersignale (tuning) ändern sich nur selten und müssen daher nicht oft übertragen werden, bei bestimmten
Anwendung z. B. nur zweimal pro Sekunde. Das Header-Kennzeichen (Header
flag) ist nur dann gesetzt, wenn der SBR-Header vorhanden sind (Subpart 4,
4.5.2.8.2.1 SBR frame overview, S. 117, zweiter Absatz).


Der SBR-Header umfasst u. a. die Parameter bs_start_freq, bs_stop_freq, und
bs_xover_band (Subpart 4, S. 42, Table 4.63 – Syntax of sbr_header(); S. 112, 113,
4.5.2.8 Payloads for the audio object SBR; S. 224, 4.6.18.3.1 Introduction).



4.    Wie einleitend ausgeführt, erzeugt der SBR-Dekodierer aus den empfangenen Signalen durch mehrfaches Kopieren von empfangenen, niederfrequenten
Subbändern die gewünschten Signale im oberen, dem SBR-Frequenzbereich (Subpart 4, S. 248 (Unterstreichungen hinzugefügt), 4.6.18.6.1 Introduction The objective of the HF generator is to patch, or copy, a number of subband signals obtained
from the analysis filterbank from consecutive subbands of matrix XLow to consecutive subbands of matrix XHigh. The definition of the patching, i.e. the number of
patches and the source ranges for the individual patches, is described by the vectors
patchNumSubbands and patchStartSubband, and the variable numPatches.)


Der SBR-Dekodierer ermittelt aus den im SBR-Header empfangenen Parametern
bs_start_freq, bs_stop_freq und bs_xover_band Frequenzbandtabellen (frequency band tables), von denen in Bezug auf das Streitpatent die sogenannte Masterfrequenztabelle (master frequency table) fMaster und die davon abgeleitete Frequenztabelle mit hoher Frequenzauflösung (high frequency resolution table)
fTableHigh relevant sind. Ein Frequenzband ist ein Frequenzintervall, umfassend eine
Gruppe aufeinanderfolgender QMF-Subbänder (S. 221, 4.6.18.2.1.5 frequency
band). Die Frequenzbandtabellen enthalten die Frequenzgrenzen für jedes Frequenzband, dargestellt als QMF-Subbänder. Jedes Frequenzband wird durch eine
Startfrequenzgrenze und eine Stoppfrequenzgrenze definiert. Das durch die Startfrequenzgrenze angegebene QMF-Subband ist im Frequenzband enthalten, das




                                                                               75/120

durch die Stoppfrequenzgrenze angegebene QMF-Subband ist aus dem Frequenzband ausgeschlossen. Für alle von der Masterfrequenztabelle abgeleiteten Frequenzbandtabellen entspricht die Stoppfrequenzgrenze von Band n der Startfrequenzgrenze von Band n+1, wobei n ein beliebiges Frequenzband in der Tabelle ist
(S. 225, 4.6.18.3.2 Frequency band tables).


4.1   Zunächst werden die Grenzfrequenzen der Masterfrequenztabelle fMaster bestimmt. Die untere bzw. obere Grenzfrequenz werden durch die QMF-Subbänder
k0 bzw. k2 repräsentiert, die sich wie folgt aus den Werten der Parameter
bs_start_freq, bs_stop_freq und dem Wert der SBR-internen Abtastrate FsSBR berechnen (S. 223, 224, 4.6.18.2.6 Variables; S. 225, 226, 4.6.18.3.2.1 Master frequency table):




                                                                           76/120

Aus den vorstehenden Gleichungen und den Angaben in Tabelle 4.63 (Subpart 4,
S. 42, 43) entnimmt der Fachmann, dass die Parameter bs_start_freq und
bs_stop_freq       jeweils   sechzehn     verschiedene      Werte     annehmen     können
(0 ≤ bs_start_freq ≤15; 0 ≤ bs_stop_freq ≤15).


4.2       Der in der Figur 4.39 (Flowchart calculation of fMaster when bs_freq_scale = 0;
S. 227) dargestellte Algorithmus ermittelt aus den QMF-Subbändern der unteren
bzw. oberen Grenzfrequenz, also den Größen k0 und k2, die Anzahl (NMaster = num-Bands) der Frequenzbänder der Masterfrequenztabelle fMaster und deren einzelnen
Einträge (fMaster(k) für k = 0, 1, …, NMaster). Ein Zahlenbeispiel, das auch bestimmte
Nebenbedingungen (S. 237, 4.6.18.3.6 Requirements) einhält, diene der Veranschaulichung. Es sei

      ·   Abtastrate des SBR-Decodierers: FsSBR = 32 kHz,
      ·   bs_start_freq = 5, bs_stop_freq = 15, bs_freq_scale = 0, bs_alter_scale = 0.

Daraus ergibt sich (S. 225 - 227):

      ·   k0 = startmin + offset(bs_start_freq) = 16 + 1 = 17
      ·   k2 = min(64,3*k0) = 51
      ·   numBands = 2*INT((k2 – ko)/2) = 34
      ·   dk = 1; k2Achieved = 17 + 34*1 = 51; k2Diff = 0; vDk(k) = dk = 1 für k =0,
          …, 33
      ·   fMaster(0) = k0 = 17; fMaster(1) = fMaster(0) +vDk(0)= 17 + 1 = 18; …;
          fMaster(34) = fMaster(33) +vDk(33)= 50 + 1 = 51



                                                                                    77/120

          also: fMaster(k) = [17, 18, …, 50, 51]
      ·   NMaster = numBands = 34


4.3       Aus der Masterfrequenztabelle fMaster wird für die SBR-Einhüllenden mit hoher
Frequenzauflösung die Frequenzbandtabelle fTableHigh extrahiert; fTableHigh ist somit eine Teilmenge von fMaster.


Welcher Teil der Masterfrequenztabelle fMaster die Frequenztabelle fTableHigh bildet,
hängt von dem Parameter bs_xover_band (= cross over band) ab, der ebenfalls
vom Kodierer an den Dekodierer signalisiert wird und acht verschiedene Werte
(0 ≤ bs_xover_band ≤ 7; S. 42, Tab. 4.63) annehmen kann.


Der Parameter bs_xover_band ist ein Index der Masterfrequenztabelle fMaster
(S. 113, dritter Eintrag unter der Tabelle 4.104), der angibt, wo der aktuelle SBR-Frequenzbereich beginnt (S. 43 (Unterstreichungen hinzugefügt), Note 2: Index to
master frequency band table, indicating where the current SBR range begins). Er
wird ebenfalls im SBR-Header übertragen (S. 224, vorletzte Zeile) und muss kleiner
als NMaster sein (S. 238, Zeile 6, 5. Gliederungspunkt).


Der Fachmann entnimmt bereits der Formulierung „indicating where the current
SBR range begins“, dass sich der Parameter bs_xover_band regelmäßig häufiger
ändern wird als die Parameter bs_start_freq und bs_stop_freq. Dafür spricht auch
die Anlage NK2d der Klägerin, die den Quellcode eines Programms der Fraunhofer
FDK AAC Codec Library for Android zum Inhalt hat und sich auf das MPEG-4 Profil
HE AAC bezieht (NK2d, S. 1, Kap. 1, Abs. 1, 2), denn diese bezeichnet den Parameter bs_xover_band als „Start index … used for dynamic crossover frequency“
(Seite 5, Mitte, Kommentar zu UCHAR xover_band).


Die aus der Masterfrequenzbandtabelle fMaster extrahierte Frequenzbandtabelle
fTableHigh bestimmt sich wie folgt:

      ·   Anzahl der Einträge: NHigh = NMaster – bs_xover_band
      ·   Einträge: fTableHigh(k) = fMaster(k + bs_xover_band), 0 ≤ k ≤ NHigh




                                                                                 78/120

      ·   Untere Grenzfrequenz von fTableHigh, repräsentiert durch das QMF-Subband
          kx: kx = fTableHigh(0) = fMaster(bs_xover_band)
      ·   Anzahl der QMF-Subbänder in fTableHigh: M = fTableHigh(NHigh) – fTableHigh(0) bzw.
          M = fMaster(NMaster) – fMaster(bs_xover_band) = k2 – kx


4.4       Wie der Fachmann erkennt, findet eine Fallunterscheidung in Abhängigkeit
vom Wert des Parameters bs_xover_band statt:


a)        Für den Fall, dass bs_xover_band gleich Null ist, ist die Frequenzbandtabelle fTableHigh identisch zur Masterfrequenzbandtabelle fMaster; der nachfolgende Kopieralgorithmus kann somit anhand der Masterfrequenztabelle fMaster und daraus abgeleiteter Größen durchgeführt werden:
      ·   Anzahl der Einträge: NHigh = NMaster
      ·   Einträge: fTableHigh(k) = fMaster(k), 0 ≤ k ≤ NMaster
      ·   Untere Grenzfrequenz von fTableHigh, repräsentiert durch das QMF-Subband
          kx: kx = fTableHigh(0) = fMaster(0) =k0
      ·   Anzahl der QMF-Subbänder in fTableHigh: M = fTableHigh(NMaster) – fTableHigh(0)
          bzw. M = fMaster(NMaster) – fMaster(0) = k2 – k0


b)        Wenn bs_xover_band hingegen ungleich Null ist, findet der Kopiervorgang
anhand der Frequenzbandtabelle fTableHigh und daraus abgeleiteter Größen statt.


Bezugnehmend auf das obige Zahlenbeispiel und unter der Annahme, dass bs_xover_band den Wert 7 hat, ergibt sich das Folgende:
      ·   Unverändert: k0 = 17, k2 = 51; NMaster = 34
      ·   Verändert:
             o NHigh = 34 – 7 = 27
             o fTableHigh(k) = fMaster(k + 7), 0 ≤ k ≤ 27, d. h. fTableHigh = [24, 25, …, 51]
             o kx = fTabelHigh(0) = fMaster(7) = 24
             o M = k2 – kx = 51 – 24 = 27
Die Frequenzbandtabelle fTableHigh umfasst somit nur die oberen 27 Frequenzbänder
der 34 Frequenzbänder umfassenden Masterfrequenzbandtabelle fMaster.




                                                                                         79/120

4.5    Der Kopieralgorithmus zur Erzeugung des hochfrequenten SBR-Frequenzbereichs aus den niederfrequenten Signalen ist im Abschnitt 4.6.18.6.3 HF generator beschrieben (S. 249, 250). In der nachfolgend eingeblendeten Figur 4.48 ist in
Form eines Flussdiagramms die Konstruktion der Kopien (patch construction) erläutert:




                                                                            80/120

MEG-4, Subpart 4, S. 250, Fig. 4.48




                                      81/120

Aus den vorstehend erläuterten Eingangsvariablen k0, kx, Fs, fMaster, NMaster und M
liefert der Algorithmus die Werte der folgenden Variablen:

     ·   numPatches ist ein Maß für die Anzahl der durchzuführenden Kopien, wobei
         bei der ersten Kopie numPatches gleich Null ist, bei der zweiten gleich Eins,
         usw.; der Fachmann erkennt aus Fig. 4.48, dass die Gesamtanzahl der Kopien gleich (numPatches + 1) ist,
     ·   patchStartSubband ist ein Vektor, der numPatches Einträge aufweist und der
         für jede Kopie angibt, mit welchem Subband diese beginnt; die Indexierung
         der Vektoreinträge beginnt gemäß Fig. 4.48 mit Null (patchStartSubband[0] = …; patchStartSubband[1] = …),
     ·   patchNumSubbands ist ein Vektor, der numPatches Einträge aufweist und
         der für jede Kopie angibt, wie viele Subbänder diese umfasst; die Indexierung
         der Vektoreinträge beginnt gemäß Fig. 4.48 mit Null (patchNumSubband[0] = …; patchNumSubband[1] = …).


a)       Basierend auf dem obigen Zahlenbeispiel für den ersten Fall (bs_xover_band = 0), für den gilt:

     ·   FsSBR = 32 kHz, bs_start_freq = 5, bs_stop_freq = 15, bs_freq_scale = 0,
         bs_alter_scale = 0, bs_xover_band = 0, und
     ·   k0 = kx = 17, k2 = 51, NMaster = 34; M = 34, fMaster(k) = [17, 18, …, 50, 51]
liefert der Algorithmus nach Figur 4.48 die folgenden Werte:
     ·   numPatches = 2, d. h. insgesamt drei Kopien,
     ·   patchStartSubband = [1, 1, 15], d. h. die ersten beiden Kopien beginnen beim
         Subband 1, die dritte Kopie beim Subband 15,
     ·   patchNumSubbands [16, 16, 2], d. h. die ersten beiden Kopien umfassen 16
         Subbänder, die dritte Kopie ist eine Teilkopie mit nur zwei Subbändern.


b)       Basierend auf dem obigen Zahlenbeispiel für den zweiten Fall (bs_xover_band = 7), für den gilt:

     ·   FsSBR = 32 kHz, bs_start_freq = 5, bs_stop_freq = 15, bs_freq_scale = 0,
         bs_alter_scale = 0, bs_xover_band = 7, und
     ·   k0 = 17; kx = 24, k2 = 51, NMaster = 34; M = 27, fMaster(k) = [17, 18, …, 50, 51]


                                                                                     82/120

liefert der Algorithmus nach Figur 4.48 die folgenden Werte:
      ·   numPatches = 2, d. h. insgesamt drei Kopien,
      ·   patchStartSubband = [8, 1, 15], d. h. die erste Teilkopie beginnt jetzt erst
          beim Subband 8, die zweite Kopie wie im Fall a) beim Subband 1 und die
          dritte Kopie, ebenfalls wie beim Fall a), beim Subband 15,
      ·   patchNumSubbands = [9, 16, 2], d. h. die erste Teilkopie umfasst nur 9 Subbänder, die zweite Kopie umfasst wie im Fall a) 16 Subbänder und die dritte
          Kopie, ebenfalls wie im Fall a), nur zwei Subbänder.


4.6       Nach der vorstehend erläuterten Ermittlung der Kopierparameter numPatches, patchStartSubband und patchNumSubbands erzeugt der HF-Generator die
entsprechenden Kopien des niederfrequenten Signals XLow, um diese anschließend
als Anregungssignal XHigh im SBR-Frequenzbereich zu verwenden (MPEG-4, Subpart 4, S. 249, 4.6.18.6.3 HF generator):




Die Relationen der obigen Einblendung für den aktuellen Rahmen (l) vereinfachen
sich unter Vernachlässigung des Einflusses der beiden vorherigen Rahmen (l - 1,
l - 2) zu:

              für 0 ≤   <      ℎ              ( ), 0 ≤ <           ℎ   gilt:




                                                                                83/120

                            =    +   +              ℎ                     ( )

                                 =       ℎ                 ( )+
                                             ( )=        ( )


a)       Für das obige Zahlenbeispiel für den ersten Fall (bs_xover_band = 0) ergibt
sich daraus:

     ·   erste Kopie (i = 0):
                                              (     )=         ( );
                                              (     )=         ( )
                                     …
                                              (     )=         (     )
                                              (     )=         (     )
     ·   zweite Kopie (i = 1):
                                              (   )=       ( )
                                              (   )=       ( )
                                     …
                                              (     )=         (      )
                                              (     )=         (      )
     ·   dritte Kopie (i = 2):
                                              (     )=         (     )
                                              (     )=         (     )


b)       Für das obige Zahlenbeispiel für den zweiten Fall (bs_xover_band = 7) ergibt
sich daraus:

     ·   erste Kopie (i = 0):
                                              (     )=         ( );
                                              (     )=         ( )
                                     …
                                              (     )=         (     )




                                                                                84/120

                                        (   )=      (     )
     ·   zweite Kopie (i = 1):
                                        (   )=      ( )
                                        (   )=      ( )
                                  …
                                        (   )=      (     )
                                        (   )=      (     )
     ·   dritte Kopie (i = 2):
                                        (   )=      (     )
                                        (   )=      (     )


c)       Die nachfolgende, vom Senat angefertigte Figur verdeutlicht die Kopiervorgänge für den ersten (bs_xover_band = 0) und den zweiten Fall (bs_xover_band = 7) und zeigt in der Mitte die Bezeichnungen aus dem Streitpatent:




                                                                             85/120

d)    Es gelten die folgenden Entsprechungen:

                            Streitpatent                                        MPEG-4
          Merkmalstext                         Bezeichnung                   Bezeichnung /
                                                                             Zahlenbeispiel
                                                                              nach Fall 2
start frequency bin of the predeter-               fexc_start                     =1
mined frequency band range of
the frequency domain signal
end frequency bin of the predeter-                 fexc_end                    k0 – 1 = 16
mined frequency band range of
the frequency domain signal
highest frequency bin of the fre-                  flast_sfm                   kx – 1 = 23
quency domain signal to which a
bit is allocated,
preset start frequency bin of a                   fbwe_start                     k0 = 17
bandwidth extension frequency
band
highest frequency bin of the band-                 ftop_sfm                    k2 – 1 = 50
width extension frequency band
n is equal to a ratio of a quantity of             _    −        _      (  − )−( − )
                                           =
frequency bins between the preset                  _    −        _         ( − )−
start frequency bin of the band-                                          34
                                                                        =    = 2,125
width extension frequency band                                            16
and the highest frequency bin of
the bandwidth extension frequency band to a quantity of frequency bins within the predetermined frequency band range of
the frequency domain signal
mth frequency bin fexc_start+ above a      fexc_start+ = fexc_start +       1 + ((kx – 1) – k0)
start frequency bin fexc_start of the       (flast_sfm - fbwe_start)               =8
predetermined frequency band
range of the frequency domain
signal and … m is equal to a value
of a quantity of frequency bins between the highest frequency bin to
which a bit is allocated and the
preset start frequency bin of the
bandwidth extension frequency
band.




                                                                                           86/120

4.7       Nach den vorstehenden Erläuterungen ist aus dem MPEG-4 Standard das
Folgende bekannt:

      1      A method for predicting a bandwidth extension frequency band signal (Y),
             comprising
                 0 Introduction, S. ix, 0.3.2.2 General Audio Coding Tools, Abschnitt MPEG-4 SBR: MPEG-4 SBR (Spectral Band Replication) is a bandwidth extension tool used in combination with the
                 AAC general audio codec. […] replicating the highband, i.e. the
                 high frequency part of the spectrum. A small amount of data
                 representing a parametric description of the highband is encoded and used in the decoding process.;
                 Subpart 4, 4.1.1.2 Overview of the encoder and decoder tools,
                 S. 9: The SBR tool regenerates the highband of the audio signal. It is based on replication of the sequences of harmonics,
                 truncated during encoding. It adjusts the spectral envelope of
                 the generated high-band and applies inverse filtering, and adds
                 noise and sinusoidal components in order to recreate the spectral characteristics of the original signal.
                 Subpart 4, 4.6.18.1 Tool description, S. 220: The SBR tool
                 (Spectral Band Replication) extends the audio bandwidth of the
                 decoded bandwidth-limited audio signal. The process is based
                 on replication of the sequences of harmonics, previously truncated in order to reduce data rate, from the available bandwidth
                 limited signal and control data obtained from the encoder.
                 Subpart 4, 4.6.18.5 SBR tool overview, S. 245, dritter
                 Aufzählungspunkt: The envelope adjuster outlined in subclause
                 4.6.18.7 calculates the matrix Y given the matrix XHigh and the
                 SBR envelope data, extracted from the SBR bitstream payload.
                 Subpart 4, S. 246, Fig. 4.46: Die Synthesis QMF Bank kombiniert das niederfrequente Signal XLow und das bandbreitenerweiterte Signal Y zu einem Ausgangsaudiosignal (Output PCM
                 samples), vgl. auch S. 247, Fig. 4.47 (c): output audio signal;



                                                                                   87/120

1.1   demultiplexing a received bitstream (Coded Audio Stream), and decoding the demultiplexed bitstream to obtain a frequency domain signal;
        Bei der aus dem MPEG-4 Standard bekannt Kombination eines AAC-Dekodierers mit einem SBR-Werkzeug wird der
        empfangene Bitstrom (Coded Audio Stream) demultiplexiert
        und vom AAC-Dekodierer dekodiert, um ein Frequenzbereichssignal zu erhalten, wie aus der einleitend zum MPEG-4
        Standard eingeblendeten Figur 4.2 ersichtlich. Im Einzelnen:
        Subpart 4, 4.1.1.2 Overview of the encoder and decoder tools,
        S. 6, Abs. 1: The input to the bitstream payload demultiplexer
        tool is the MPEG-4 GA bitstream payload. The demultiplexer
        separates the bitstream payload into the parts for each tool,
        and provides each of the tools with the bitstream payload information related to that tool; Abs. 2: The AAC noiseless decoding tool takes the information from the payload demultiplexer … decodes the Huffman coded data, and reconstructs
        the quantized spectra … outputs of the noiseless decoding
        tool are … The quantized values for the spectra
        Damit ist das Merkmal 1.1 aus dem MPEG-4 Standard bekannt. Der Anspruch 1 verlangt, wie zur Auslegung dargelegt,
        nicht, dass die Vorhersage des Bandbreitenerweiterungsfrequenzbandsignals durchgängig im Frequenzbereich arbeitet.
        Daher ist es unschädlich, dass beim MPEG-4 Standard das
        Frequenzbereichssignal des AAC-Dekodierers gemäß Figur
        4.2 mit zugehöriger Beschreibung zunächst in ein Zeitbereichssignal umgewandelt und dieses dem SBR-Werkzeug
        zur Verfügung gestellt wird. Davon abgesehen transformiert
        das MPEG-4 SBR-Werkzeug sein im Zeitbereich vorliegendes
        Eingangssignal mittels einer digitalen Filterbank in den komplexwertigen QMF-Bereich (Quadrature Mirror Filter), was einer Frequenztransformation entspricht (vgl. GAO, Abs. 0004,
        0005). Im Einzelnen: Subpart 4: 4.6.18.4.1 Analysis filterbank,


                                                                      88/120

           S. 238; 4.6.18.5 SBR tool overview, S. 246, Fig. 4.46: das
           Ausgangssignal XLow der Analysis QMF Bank liegt in der komplexwertigen QMF-Domäne vor, die Frequenzsubbänder enthält: S. 221, 4.6.18.2.1.5 frequency band … interval in frequency, group of consecutive QMF subbands; S. 221,
           4.6.18.2.1.16 subband … a frequency range represented by
           one row in a QMF matrix, S. 224, 4.6.18.2.6 Variables … XLow
           is the complex input QMF bank subband matrix to the HF generator
1.2     determining whether a highest frequency bin (kx - 1), to which a bit is
        allocated, of the frequency domain signal is less than a preset start
        frequency bin (k0) of a bandwidth extension frequency band (k0 bis
        k2 - 1);
           Wie einleitend zum MPEG-4 Standard dargestellt, hängen die
           Kopiervorgänge davon ab, ob der vom Kodierer zum Dekodierer signalisierte Parameter bs_xover_band gleich Null oder
           größer als Null ist. Im erstgenannten Fall ist die höchste im
           Dekodierer    verfügbare    Frequenz     im    QMF-Subband
           (kx – 1) = (k0 – 1), während die voreingestellte Startfrequenz
           des BWE-Bereichs im Subband k0 liegt. In diesem Fall ist also
           (kx – 1) = (k0 – 1) < k0, d. h. das Ergebnis der Bestimmung
           nach Merkmal 1.2 ist WAHR. Im zweitgenannten Fall ist die
           höchste im Dekodierer verfügbare Frequenz im QMF-Subband (kx – 1), während die voreingestellte Startfrequenz des
           BWE-Bereichs im Subband k0 liegt. In diesem Fall ist also
           (kx – 1) > k0, d. h. das Ergebnis der Bestimmung nach Merkmal 1.2 ist FALSCH.
1.3     predicting an excitation signal (XHigh) of the bandwidth extension frequency band
1.3.1      according to an excitation signal (XLow) within a predetermined frequency band range (1 bis (k0 -1)) of the frequency domain signal




                                                                         89/120

          and the preset start frequency bin (k0) of the bandwidth extension
          frequency band
1.3.2     when the highest frequency bin (kx – 1 = k0 - 1) to which a bit is allocated is less than the preset start frequency bin (k0) of the bandwidth extension frequency band;
             Zu den Merkmalen 1.3 bis 1.3.2 wird auf die einleitenden
             Ausführungen zum MPEG-4 Standard verwiesen.
1.4     predicting the excitation signal (XHigh) of the bandwidth extension frequency band
1.4.1     according to the excitation signal (XLow) within the predetermined
          frequency band range (1 bis (k0 -1)) of the frequency domain signal,
          the preset start frequency bin (k0) of the bandwidth extension frequency band, and the highest frequency bin (kx) to which a bit is
          allocated
1.4.2     when the highest frequency bin (kx) to which a bit is allocated is no
          less than the preset start frequency bin (k0) of the bandwidth extension frequency band; and
             Zu den Merkmalen 1.4 bis 1.4.2 wird auf die einleitenden
             Ausführungen zum MPEG-4 Standard verwiesen.
1.5     predicting the bandwidth extension frequency band signal (Y) according to the predicted excitation signal (XHigh) of the bandwidth extension
        frequency band and a frequency envelope (Eorig) of the bandwidth extension frequency band;
             Im Subpart 4, 4.6.18.7 HF adjustment (mit zugehörigen Unterabschnitten; S. 251 – 256) des MPEG-4 Standards ist im
             Detail beschrieben, wie aus dem vorhergesagten Anregungssignal (XHigh) des Bandbreitenerweiterungsfrequenzbands und einer Frequenzeinhüllenden (EOrig) (4.6.18.2.6
             Variables: Eorig: has LE columns where each column is of
             length NLow or NHigh depending on the frequency resolution
             for each SBR envelope. The elements in EOrig contains the
             envelope scalefactors of the original signal.) das Bandbreitenerweiterungsfrequenzbandsignal (Y) vorhergesagt wird


                                                                           90/120

1.6     wherein the predicting an excitation signal (XHigh) of the bandwidth extension frequency band according to an excitation signal (XLow) within
        a predetermined frequency band range (1 bis (k0 -1)) of the frequency
        domain signal and the preset start frequency bin (k0) of the bandwidth
        extension frequency band comprises:
1.6.1     making n copies of the excitation signal (XLow) within the predetermined frequency band range of the frequency domain signal, and
1.6.2     using the n copies of the excitation signal (XLow) as an excitation
          signal (XHigh) between the preset start frequency bin (k0) of the
          bandwidth extension frequency band and a highest frequency bin
          (k2 - 1) of the bandwidth extension frequency band
1.6.3     wherein n is an integer or a non-integer greater than 0, and n is
                                (       )
          equal to a ratio (=                   ) of a quantity of frequency bins ((k2 –
                                    (       )

          1) – k0 – 1) between the preset start frequency bin (k0) of the bandwidth extension frequency band and the highest frequency bin
          (k2 - 1) of the bandwidth extension frequency band to a quantity
          ((k0 – 1) – 1) of frequency bins within the predetermined frequency
          band range of the frequency domain signal;
          where n is an integer or a non-integer greater than 0; and
             Zu den Merkmalen 1.6 bis 1.6.3 wird ergänzend auf die einleitenden Ausführungen zum MPEG-4 Standard verwiesen.
1.7     wherein the predicting the excitation signal (XHigh) of the bandwidth
        extension frequency band according to the excitation signal (XLow)
        within the predetermined frequency band range of the frequency domain signal, the preset start frequency bin (k0) of the bandwidth extension frequency band, and the highest frequency bin (kx), to which a bit
        is allocated comprises:
1.7.1     making a copy of an excitation signal from the mth frequency bin
          fexc_start+ (1 + ((kx – 1) – k0)) above a start frequency bin fexc_start (1)
          of the predetermined frequency band range of the frequency domain signal to an end frequency bin fexc_end (k0 – 1) of the predetermined frequency band range of the frequency domain signal and



                                                                                  91/120

     1.7.2      [making] n copies of the excitation signal (XLow) within the predetermined frequency band range of the frequency domain signal, and
     1.7.3      using the two parts of excitation signals as an excitation signal between the highest frequency bin (kx – 1), to which a bit is allocated,
                of the frequency domain signal and the highest frequency bin
                (k2 - 1) of the bandwidth extension frequency band,
     1.7.4      wherein n is 0 or an integer or a non-integer greater than 0,
                m is a positive integer, and m is equal to a value of a quantity of
                frequency bins (kx – 1 – k0) between the highest frequency bin
                (kx – 1) to which a bit is allocated and the preset start frequency bin
                (k0) of the bandwidth extension frequency band.
                   Zu den Merkmalen 1.7 bis 1.7.4 wird ergänzend auf die einleitenden Ausführungen zum MPEG-4 Standard verwiesen.


Danach ist das Verfahren nach Anspruch 1 der erteilten Fassung aus dem MPEG-4 Standard bekannt. Gleiches gilt für die Vorrichtung nach Anspruch 6.




                         III.   Zur den Hilfsanträgen

Die Beklagte kann das Streitpatent auch in den Fassungen der Hilfsanträge nicht
erfolgreich verteidigen, weil sowohl das danach beanspruchten Verfahren (Anspruch 1 bzw. Anspruch 4 nach Hilfsantrag „Abhängig 1“ bzw. Anspruch 5 nach
Hilfsantrag „Abhängig 2“) als auch die danach beanspruchte Vorrichtung (Anspruch 6 bzw. Anspruch 9 nach Hilfsantrag „Abhängig 1“ bzw. Anspruch 10 nach
Hilfsantrag „Abhängig 2“) nach den Hilfsanträgen 0, 1, 2, 3.0, „Abhängig 1“, 3.0‘,
3.0‘‘, 3, 3a, 4, 5 und „Abhängig 2“ gegenüber dem Stand der Technik nicht neu sind
oder nicht auf einer erfinderischen Tätigkeit beruhen (Art. II § 6 Abs. 1 Nr. 1 Int-PatÜG i. V. m. Art. 138 Abs. 1 lit. a), Art. 52, 54, 56 EPÜ).


1.     Der Gegenstand gemäß dem auf ein Verfahren zur Vorhersage eines Bandbreitenerweiterungs-Frequenzbandsignals gerichteten Patentanspruch 1 in der




                                                                                 92/120

Fassung nach Hilfsantrag 0 vom 10. November 2023 – und damit auch der Gegenstand des auf eine entsprechende Decodiervorrichtung gerichtete Patentanspruchs 6 nach Hilfsantrag 0 – sind nicht patentfähig.


1.1    Anspruch 1 gemäß Hilfsantrag 0 lautet (Änderungen gegenüber der erteilten
Fassung gekennzeichnet)

      1HA1 A method for predicting in a decoding device a bandwidth extension
             frequency band signal, comprising:
      1.1      demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;
      1.1.1HA0    pre-setting a start frequency bin of a bandwidth extension frequency band by the decoding device;
      1.2HA1 determining (101) whether a highest frequency bin, to which a bit is
               allocated, of the frequency domain signal is less than the preset start
               frequency bin of the bandwidth extension frequency band;
      1.3 bis 1.7.4   wie erteilt


Im Hilfsantrag 0 ist im Vergleich zur erteilten Fassung ergänzt, dass das beanspruchte Verfahren in einer Dekodiervorrichtung durchgeführt wird (Merkmal 1HA1),
sowie, dass diese die Startfrequenz des BWE-Bereichs voreinstellt (Merkmal
1.1.1HA0).


1.2    Das Merkmal 1HA1 schränkt den Gegenstand des Anspruchs 1 in der erteilten
Fassung nicht ein, denn, wie im Rahmen der Auslegung zum Hauptantrag dargelegt, versteht der Fachmann bereits die erteilte Fassung so, dass das Verfahren in
einer Dekodiervorrichtung durchgeführt wird.


Dem Merkmal 1.1.1HA0 entnimmt der Fachmann, dass die Dekodiervorrichtung eine
Voreinstellung des Startfrequenzwerts des BWE-Bereichs vornimmt. Damit ist ausgeschlossen, dass der Kodierer dem Dekodierer diesen Wert unmittelbar signalisiert
und der Dekodierer den empfangenen Startfrequenzwert unmittelbar verwendet.




                                                                                93/120

Merkmal 1.1.1HA0 schließt jedoch nicht aus, dass der Kodierer dem Dekodierer bestimmte Parameterwerte, insbesondere den Wert der aktuellen Kodierrate, übermittelt und der Dekodierer daraufhin einen entsprechenden Startfrequenzwert für den
BWE-Bereich bestimmt und diesen – vor Beginn der anspruchsgemäßen Vorhersage des BWE-Signals – voreinstellt. Dabei liest der Fachmann mit, dass der Dekodierer über eine vorbestimmte Zuordnung von Parameterwerten, insbesondere
Kodierraten, zu Startfrequenzwerten verfügt (Streitpatentschrift, Abs. 0031 (Unterstreichungen hinzugefügt): Selection of fbwe_start is related to an encoding rate …. A
higher encoding rate indicates a higher preset start frequency fbwe_start; Abs. 0053:
when the encoding rate ist 24 kpbs, the preset start frequency fbwe_start of the bandwidth extension frequency band is equal to 6.4 kHz).


1.3    Der Gegenstand des Anspruchs 1 nach Hilfsantrag 0 schränkt den Gegenstand des Anspruchs 1 erteilter Fassung jedenfalls durch das Merkmal 1.1.1HA0 ein,
weil damit – wie vorstehend dargelegt – eine Variante ausgeschlossen ist, bei der
der Kodierer eine unmittelbare (direkte) Voreinstellung der Startfrequenz des BWE-Bereichs durchführt, diesen Wert an den Dekodierer überträgt und dieser diesen
Wert dann unmittelbar (direkt) verwendet.


1.4    Die Frage der ursprünglichen Offenbarung des Gegenstands des Anspruchs 1 nach Hilfsantrag 0 (vgl. EP 2 940 685 A1, Abs. 0078) kann dahinstehen
denn jedenfalls erweist sich der Gegenstand des Anspruchs 1 nach Hilfsantrag 0
als nicht patentfähig.


Denn auch im MPEG-4 Standard führt der Dekodierer eine Voreinstellung der Startfrequenz des BWE-Bereichs, der im MPEG-4-Standard durch den SBR (Spectral
Band Replication)-Bereich beschrieben ist, durch, nämlich u. a. durch Bestimmung
des Parameters k0, der, wie zum Hauptantrag im Detail dargelegt, den Beginn des
SBR-Bereichs in MPEG-4 anzeigt. Dabei schließt es das Merkmal 1.1.1HA0 – wie
oben ausgeführt – nicht aus, dass vom Kodierer zum Dekodierer Parameterwerte
signalisiert werden, aus denen der Dekodierer die Startfrequenz ermittelt und entsprechend voreinstellt. So verhält es sich auch im MPEG-4 Standard. Wie zum




                                                                                94/120

Hauptantrag erläutert, hängt die untere Frequenzgrenze k0 der Master-Frequenztabelle, die indikativ für die Startfrequenz des BWE(=SBR)-Bereichs ist, von den Werten der Parameter FsSBR und bs_start_freq ab, die vom Kodierer an den Dekodierer
gesendet werden. Damit führt der Dekodierer – vor Beginn der Prädiktion des BWE-Bereichs – eine Voreinstellung der Startfrequenz des BWE-Bereichs gemäß Merkmal 1.1.1HA0 durch.


Wie weiter zum Hauptantrag ausgeführt, werden die Parameter FsSBR und
bs_start_freq beim MPEG-4 Standard auch nicht regelmäßig von Rahmen zu Rahmen geändert, so dass die vom Streitpatent angestrebte Kontinuität des prädizierten Signals im BWE-Frequenzbereich über Rahmengrenzen hinweg auch beim
MPEG-4 Standard gewährleistet ist. Denn gemäß dem MPEG-4 Standard wird der
Parameter bs_start_freq im SBR-Header übertragen, der unabhängig von einer Änderung nicht bei jedem Rahmen, sondern seltener, z. B. nur zwei Mal je Sekunde
übertragen wird (MPEG-4, Subpart 4, 4.5.2.8.2.1 SBR frame overview, S. 117,
Abs. 2), d. h. nur jeden 50. Rahmen bei einer Rahmenlänge von 20 ms.


Danach ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 0 aus dem MPEG-4
Standard bekannt.



2.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 1
vom 13 September 2022 (Az.: 4 Ni 49/22 (EP); insofern gleichlautend mit dem Anspruch 1    nach    Hilfsantrag 1   vom   12. Juli 2022   im   Verfahren   mit    dem
Az.: 4 Ni 53/22 (EP)) – und damit auch der Gegenstand des Patentanspruchs 6
nach Hilfsantrag 1 – sind nicht patentfähig.


2.1    Anspruch 1 gemäß Hilfsantrag 1 lautet (Änderungen gegenüber der erteilten
Fassung gekennzeichnet):

      1HA1 A method for predicting in a decoding device a bandwidth extension
            frequency band signal, comprising:
      1.1     demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;



                                                                                 95/120

      1.1.1HA1   pre-setting a start frequency bin of a bandwidth extension frequency band and selecting a predetermined frequency band
                 range of the frequency domain signal by the decoding device;
      1.2HA1 determining (101) whether a highest frequency bin, to which a bit is
              allocated, of the frequency domain signal is less than the preset start
              frequency bin of the bandwidth extension frequency band;
      1.3     predicting (102) an excitation signal of the bandwidth extension frequency band
      1.3.1HA1   according to an excitation signal within the predetermined frequency band range of the frequency domain signal and the preset
                 start frequency bin of the bandwidth extension frequency band
      1.3.2 bis 1.7.4 wie erteilt


Im Vergleich zum Hilfsantrag 0 umfasst der Hilfsantrag 1 im Merkmal 1.1.1HA1 zusätzlich das Wählen eines vorbestimmten Frequenzbandbereichs des (niederfrequenten, zu kopierenden) Frequenzbereichssignals durch den Dekodierer.


2.2    Der Fachmann versteht diesen Teil des Merkmals 1.1.1HA1 so, dass der Dekodierer den zu kopierenden niederfrequenten Frequenzbereich anhand eines oder
mehrerer Kriterien auswählt. Damit ist nach Hilfsantrag 1 ausgeschlossen, dass der
Kodierer dem Dekodierer die Frequenzgrenzen unmittelbar signalisiert und der Dekodierer diesen Frequenzbereich unmittelbar zum Kopieren verwendet.


Merkmal 1.1.1HA0 schließt jedoch nicht aus, dass der Kodierer dem Dekodierer bestimmte Parameterwerte, insbesondere den Wert der aktuellen Kodierrate und/oder
den im Kodierer ermittelten Signaltyp (harmonic; non-harmonic), übermittelt und der
Dekodierer daraufhin einen entsprechenden zu kopierenden Frequenzbereich – vor
Beginn der anspruchsgemäßen Vorhersage des BWE-Signals – auswählt und damit
vorbestimmt. Dabei liest der Fachmann mit, dass der Dekodierer über eine vorbestimmte Zuordnung von Parameterwerten, insbesondere Kodierraten und Signaltypen, zu niederfrequenten, zu kopierenden Frequenzbereichen verfügt (Streitpatentschrift, Abs. 0035 (Unterstreichungen hinzugefügt): Selection of the predetermined




                                                                               96/120

frequency band range from the fexc_start to the fexc_end of the frequency domain signal
is related to a signal type and an encoding rate).


2.3    Der Anspruch 1 nach Hilfsantrag 1 schränkt den Gegenstand des Anspruchs 1 erteilter Fassung jedenfalls durch das Merkmal 1.1.1HA1 ein, weil damit –
wie vorstehend dargelegt – eine Variante der erteilten Fassung ausgeschlossen ist,
bei der der Kodierer eine unmittelbare (direkte) Voreinstellung der Startfrequenz des
BWE-Bereichs und des zu kopierenden Frequenzbereichs vornimmt, diese Werte
an den Dekodierer überträgt und dieser diese Werte dann unmittelbar (direkt) verwendet.


2.4    Die Frage der ursprünglichen Offenbarung des Anspruchs 1 nach Hilfsantrag 1 (vgl. EP 2 940 685 A1, Abs. 0053), kann dahinstehen, weil der Gegenstand
des Anspruchs 1 nach Hilfsantrag 1 jedenfalls nicht patentfähig ist.


Denn beim MPEG-4 Standard bestimmt der Dekodierer auf Grundlage der von dem
Kodierer übertragenen Werte der Parameter FsSBR und bs_start_freq den Wert des
Parameters k0 und wählt damit den zu kopierenden Frequenzbereich aus. Dieser
ist damit vorbestimmt, denn er reicht – wie zum Hauptantrag dargelegt – von dem
untersten Subband 1 bis zu dem Subband k0 – 1.


Danach ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 1 aus dem MPEG-4
Standard bekannt.



3.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 2
vom 13. September 2022 (Az.: 4 Ni 49/22 (EP); insofern gleichlautend mit dem Anspruch    1   nach   Hilfsantrag   2   vom    12.07.22    im   Verfahren    mit    dem
Az.: 4 Ni 53/22 (EP)) – und damit auch der Gegenstand des Patentanspruchs 6 –
sind aus dem MPEG-4 Standard bekannt.


3.1    Anspruch 1 gemäß Hilfsantrag 2 basiert auf Anspruch 1 gemäß Hilfsantrag 1
und unterscheidet sich von diesem nur im Merkmal 1.1.1HA2:




                                                                                  97/120

      1.1.1HA2    pre-setting a start frequency bin of a bandwidth extension frequency
                  band depending on an encoding bit-rate and selecting a predetermined frequency band range of the frequency domain signal by
                  the decoding device;


3.2    Nach Merkmal 1.1.1HA2 hängt die Voreinstellung der Startfrequenz des BWE-Bereichs durch den Dekodierer zumindest von der (im Kodierer verwendeten) Kodier-Bitrate ab. Nach den Ausführungsbeispielen des Streitpatents wird für ein mit
24 kbps kodiertes UWB-Signal (Ultra Wide Band) eine Starfrequenz von 6,4 kHz
und für eine Kodierrate von 32 kbps eine Startfrequenz des BWE-Bereichs von
8 kHz gewählt (Streitpatentschrift, Abs. 0031).


3.3    Die Frage der Zulässigkeit des Hilfsantrags 2 (vgl. EP 2 940 685 A1, Abs.
0050, 0070, 0090) kann dahinstehen, denn jedenfalls ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 2 aus dem MPEG-4 Standard bekannt.


Denn danach hängt die Startfrequenz (Subband k0) des BWE-Bereichs (k0 bis
(k2 – 1)), wie zum Hauptantrag dargelegt, u. a. von der internen Abtastrate FsSBR
des SBR-Werkzeugs ab (MPEG-4, Subpart 4, 4.6.18.3.2.1 Master frequency band
table, S. 225), die wiederum mit der vom Kodierer zum Dekodierer übertragenen
Abtastrate (4.5.1.1 GASpecificConfig(), S. 53: … samplingFrequencyIndex … Table
4.82; 4.5.1.2 Program config element (PCE), S. 55: sampling_frequency_index Indicates the sampling frequency of the program according to the table defined in
subclause 1.6.3.3 (samplingFrequencyIndes); Subbpart 1, 1.6.3.3 samplingFrequency, S. 45: The sampling frequency used for this audio object. Either transmitted
directly, or coded in the form of samplingFrequencylndex; 1.6.3.4 samplingFrequencyIndex, S. 45) des Kern-Codierers verknüpft ist (MPEG-4, Subpart 4, 4.6.18.2.6
Variables, S. 223: FsSBR … twice the sampling frequency of the core coder (after
sampling frequency mapping, Table 4.82).


Darüber hinaus hängt die Kodierrate des Kern-Kodierers von seiner Abtastrate ab
(MPEG-4, Subpart 4, 4.5.3.3 Maximum bit rate, S. 124: … depends on the audio
sampling rate).



                                                                                98/120

Danach hängt die Startfrequenz des BWE-Bereichs in MPEG-4 von der Codierrate
ab. Der Gegenstand des Anspruchs 1 in der Fassung nach Hilfsantrag 2 ist somit
aus dem MPEG-4 Standard bekannt.



4.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 3.0 vom 10. November 2023 – und damit auch der Gegenstand des Patentanspruchs 6 – sind nicht patentfähig.


4.1    Anspruch 1 nach Hilfsantrag 3.0 lautet (Änderungen gegenüber der erteilten
Fassung markiert):

      1HA3 A method for predicting in a decoding device a bandwidth extension
           frequency band signal according to an encoding bit-rate and a signal
           type, comprising
      1.1HA3.0 demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal and a frequency envelope of a bandwidth extension frequency band;
      1.1.1HA3.0 pre-setting a start frequency bin of a bandwidth extension frequency band depending on the encoding bit-rate by the decoding device;
      1.2HA1      determining (101) whether a highest frequency bin, to which a bit is
                  allocated, of the frequency domain signal is less than the preset
                  start frequency bin of the bandwidth extension frequency band;
      …           …
      1.5HA3.0 predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
               frequency band and the frequency envelope of the bandwidth extension frequency band;
      1.5.1HA3    wherein the frequency envelope of the bandwidth extension
                  frequency band is acquired based on the signal type;
      …           …




                                                                                99/120

4.2     Nach Merkmal 1HA3 findet das beanspruchte Verfahren gemäß einer Kodierbitrate und gemäß einem Signaltyp statt, was der Fachmann so versteht, dass diese
Größen – irgendwie – in die Vorhersage des BWE-Signals eingehen. Zudem ist in
Merkmal 1.1HA3.0 ergänzt, dass als Ergebnis des Demultiplexens und Dekodierens
des empfangenen Bitstroms über das (niederfrequente) Frequenzbereichssignal
hinaus auch eine spektrale Einhüllende des BWE-Bereichs erhalten wird. Nach
Merkmal 1.1.1HA3.0 hängt die Voreinstellung der Startfrequenz des BWE-Bereichs
im Dekodierer, wie bei dem Hilfsantrag 2, jedenfalls von der Kodierbitrate ab. Nach
Merkmal 1.5.1HA3 wird die spektrale Einhüllende des BWE-Bereichs basierend auf
dem Signaltyp erworben. Ein Ermitteln des Signaltyps im Kodierer und Übertragen
dieser Information an den Dekodierer, damit dieser basierend auf der Signaltyp-Information den spektrale Einhüllende gewinnt, ist in der Beschreibung des Streitpatents genannt (Abs. 0026, 0070).


Mangels konkreter Angaben wird der Fachmann verstehen, dass der Signaltyp im
Kodierer typischerweise für einen bestimmten Zeitabschnitt, beispielsweise für den
aktuellen Rahmen (d. h. ca. 20 ms) und für den gesamten Frequenzbereich ermittelt
wird.


Hinsichtlich möglicher Varianten des „Signaltyps“ unterscheidet das Streitpatent –
in Übereinstimmung mit dem Wissen des Fachmanns – zwischen einem „harmonischen“ und einem „nicht-harmonischen“ Signal (Abs. 0027, 0071). Unter einem „harmonischen“ Signal versteht der Fachmann ein Signal mit einem vergleichsweise
hohen Anteil sinusförmiger Signale bestimmter, für den Betrachtungszeitraum konstanter, Frequenzen und ggfs. einer gewissen Anzahl entsprechender Oberschwingungen („Harmonische“). Dementsprechend ist ein „nicht-harmonisches“ Signal
dadurch charakterisiert, dass es ein eher rauschartiges, flaches Frequenzspektrum
aufweist und – wenn überhaupt – sinusförmige Anteile nur mit sehr geringen
Amplituden umfasst.


4.3     Die Zulässigkeit des Hilfsantrags 3.0 (vgl. EP 2 940 685 A1, Abs. 0017,
0053, 0086), kann dahinstehen denn der Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0 ist aus dem MPEG-4 Standard bekannt.



                                                                            100/120

Das im Merkmal 1.1HA3.0 genannte Dekodieren der spektralen Einhüllenden des
BWE-Bereichs aus dem empfangenen Bitstrom ist bei Bandbreitenerweiterungs-Werkzeugen fachüblich und auch aus dem MPEG-4 Standard bekannt (Subpart 4,
4.5.2.8 Payloads for the audio object type SBR, 4.5.2.8.1 Definitions, S. 114:
sbr_envelope() … Syntactic element that contains the huffman coded envelope
data; S. 115: bs_num_env … Indicates the number of SBR envelopes in the current
SBR frame; S. 116: bs_data_env … Holds the raw envelope scalefactors for each
channel, SBR envelope and band; S. 117, dritter Absatz: Raw data consists of Huffman coded envelope scalefactors; 4.6.18.2.1.4 envelope scalefactor, S. 220: an element representing the average energy of a signal over a region described by a
frequency band and a time segment; 4.6.18.2.6 Variables, S. 223: EOrig has LE columns where each column is of length NLow or NHigh depending on the frequency
resolution for each SBR envelope. The elements in EOrig contains [sic!] the envelope
scalefactors of the original signal … LE … number of SBR envelopes; 4.6.18.3.3
Time / frequency grid, S. 232, drittletzter Absatz: LE = bs_num_env).


Das Merkmal 1.1.1HA3.0 entspricht inhaltlich dem ersten Teil des Merkmals 1.1.1HA2.
Insofern wird auf die entsprechenden vorstehenden Ausführungen zum Hilfsantrag 2 verwiesen, wonach dieses Merkmal aus dem MPEG-4 Standard bekannt ist.


Auch das Gewinnen der spektralen Einhüllenden des BWE-Frequenzbereichs basierend auf dem Signaltyp gemäß Merkmal 1.5.1HA3 ist aus dem MPEG-4 Standard
bekannt. Denn gemäß Subbpart 4, Abschnitt 4.6.18.7 HF adjustment hängt die im
Dekodierer bestimmte spektrale Einhüllende des BWE-Bereichs auch davon ab, ob
im aktuellen SBR-Rahmen sinusförmige Signalanteile enthalten sind oder nicht.


Hierzu werden vom Kodierer zum Dekodierer die Variable bs_add_harmonic_flag
und der Vektor bs_add_harmonic(i) übertragen (4.5.2.8.1 Definitions, S. 114:
bs_add_harmonic_flag … Indicates if sinusoidal coding information is present;
S. 116: bs_add_harmonic … Indicates if a sinusoidal should be added to a specific
frequency band according to Table 4.119 – bs_add_harmonic vector element), die
angeben, ob und wenn ja, in welchem QMF-Subband (4.6.18.7.2 Mapping, S. 251,
letzter Absatz: 0 ≤ i ≤ NHigh) Harmonische vorliegen.


                                                                             101/120

Basierend auf dieser Information wird die spektrale Einhüllende im Dekodierer bestimmt (4.6.18.7.2 Mapping, S. 251, 252: SIndex -> SIndexmpapped -> SMapped; 4.6.18.7.4
Calculation of levels of additional HF signal component, S. 253: SM = f(EOrig-Mapped, SIndexMapped); 4.6.18.7.5 Calculation of gain, S. 253: The level of additional si-

nusoids, as well as the level of the additional added noise, are taken into account.).


Nach den in den Abschnitten 4.6.18.7.5 Calculation of gain und 4.6.18.7.6 Assembling HF signals angegebenen Formeln geht in das Ausgangssignal Y des „Envelope
Adjuster“ (Subpart 4, S. 246, Fig. 4.46) ein, bei welchen Frequenzen sinusförmige
Signalanteile (Harmonische) vorhanden sind.


Insofern ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0 aus dem MPEG-4 Standard bekannt.



5.        Der Gegenstand des Patentanspruchs 4 in der Fassung nach Hilfsantrag
„Abhängig 1“ vom 26. Januar 2024 – und damit auch der Gegenstand des Patentanspruchs 9 nach Hilfsantrag „Abhängig 1“ – sind nicht patentfähig.


5.1       Der dem erteilten Anspruch 4 entsprechende Anspruch 4 nach Hilfsantrag
“Abhängig 1” lautet in seinem Rückbezug auf den erteilten Anspruch 1 und mit einer
Merkmalsgliederung versehen:

      1      A method for predicting a bandwidth extension frequency band signal,
             comprising
      1.1       demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;
      1.2       determining (101) whether a highest frequency bin, to which a bit is
                allocated, of the frequency domain signal is less than a preset start
                frequency bin of a bandwidth extension frequency band;
      1.3       predicting (102) an excitation signal of the bandwidth extension frequency band




                                                                                   102/120

1.3.1     according to an excitation signal within a predetermined frequency
          band range of the frequency domain signal and the preset start frequency bin of the bandwidth extension frequency band
1.3.2     when the highest frequency bin to which a bit is allocated is less
          than the preset start frequency bin of the bandwidth extension frequency band;
1.4     predicting (103) the excitation signal of the bandwidth extension frequency band
1.4.1     according to the excitation signal within the predetermined frequency band range of the frequency domain signal, the preset start
          frequency bin of the bandwidth extension frequency band, and the
          highest frequency bin to which a bit is allocated
1.4.2     when the highest frequency bin to which a bit is allocated is no less
          than the preset start frequency bin of the bandwidth extension frequency band; and
1.5     predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
        frequency band and a frequency envelope of the bandwidth extension
        frequency band;
1.6     wherein the predicting an excitation signal of the bandwidth extension
        frequency band according to an excitation signal within a predetermined frequency band range of the frequency domain signal and the
        preset start frequency bin of the bandwidth extension frequency band
        comprises:
1.6.1     making n copies of the excitation signal within the predetermined
          frequency band range of the frequency domain signal, and
1.6.2     using the n copies of the excitation signal as an excitation signal
          between the preset start frequency bin of the bandwidth extension
          frequency band and a highest frequency bin of the bandwidth extension frequency band
1.6.3     wherein n is an integer or a non-integer greater than 0, and n is
          equal to a ratio of a quantity of frequency bins between the preset
          start frequency bin of the bandwidth extension frequency band and


                                                                        103/120

           the highest frequency bin of the bandwidth extension frequency
           band to a quantity of frequency bins within the predetermined frequency band range of the frequency domain signal;
           where n is an integer or a non-integer greater than 0; and
1.7      wherein the predicting the excitation signal of the bandwidth extension
         frequency band according to the excitation signal within the predetermined frequency band range of the frequency domain signal, the preset start frequency bin of the bandwidth extension frequency band,
         and the highest frequency bin, to which a bit is allocated comprises:
1.7.1      making a copy of an excitation signal from the mth frequency bin
           fexc_start+ above a start frequency bin fexc_start of the predetermined
           frequency band range of the frequency domain signal to an end frequency bin fexc_end of the predetermined frequency band range of
           the frequency domain signal and
1.7.2      [making] n copies of the excitation signal within the predetermined
           frequency band range of the frequency domain signal, and
1.7.3      using the two parts of excitation signals as an excitation signal between the highest frequency bin, to which a bit is allocated, of the
           frequency domain signal and the highest frequency bin of the bandwidth extension frequency band,
1.7.4      wherein n is 0 or an integer or a non-integer greater than 0,
           m is a positive integer, and m is equal to a value of a quantity of
           frequency bins between the highest frequency bin to which a bit is
           allocated and the preset start frequency bin of the bandwidth extension frequency band,
1.5.2AH1   wherein before the predicting the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension frequency band and a frequency envelope of the bandwidth extension frequency band,
           the method further comprises:
1.1AH1     decoding the bitstream to obtain a signal type; and
1.5.1AH1   acquiring the frequency envelope of the bandwidth extension
           frequency band according to the signal type.


                                                                           104/120

5.2   Der Anspruch 4 nach Hilfsantrag „Abhängig 1“ unterscheidet sich vom Anspruch 1 nach Hilfsantrag 3.0 u. a. dadurch, dass gemäß Merkmal 1.1AH1 die Decodierung des empfangenen Bitstroms auch den Signaltyp liefert. Daraus entnimmt
der Fachmann, dass der Signaltyp – wie es fachüblich ist – im Kodierer bestimmt
und diese Information zum Dekodierer übertragen wird.


Dass die Decodierung des Bitstroms zum Erhalten des Signaltyps (Merkmal 1.1AH1)
und der Erwerb der spektralen Einhüllenden des BWE-Bereichs gemäß dem Signaltyp (Merkmal 1.5.1AH1) vor der Prädiktion des BWE-Signals stattfindet (Merkmal
1.5.2AH1), ist selbstverständlich. In Bezug auf das Merkmal 1.5.1AH1, das inhaltlich
mit dem Merkmal 1.5.1HA3 übereinstimmt, versteht der Fachmann auch den Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0 in diesem Sinn.


5.3   Hinsichtlich der Patentfähigkeit des Gegenstands des Anspruchs 4 nach
Hilfsantrag „Abhängig 1“ gelten die vorstehenden Ausführungen zum Gegenstand
des Anspruchs 1 nach Hilfsantrag 3.0 in entsprechender Weise. Ergänzend wird
darauf hingewiesen, dass beim MPEG-4 Standard die den Signaltyp bestimmenden
Parameter bs_add_harmonic_flag und bs_add_harmonic(i) selbstverständlich zunächst vom Dekodierer dekodiert und danach für die Bestimmung der spektralen
Einhüllenden verwendet werden (Subpart 4, 4.5.2.8 Payloads for the audio object
type SBR, S. 112; 4.5.2.8.1 Definitions, S. 114: bs_add_harmonic_flag … Indicates
if sinusoidal coding information is present; S. 116: bs_add_harmonic … Indicates if
a sinusoidal should be added to a specific frequency band according to Table 4.119
– bs_add_harmonic vector element; 4.5.2.8.2 Decoding process, S. 116; 4.5.2.8.2.1
SBR frame overview).


Danach ist der Gegenstand des Anspruchs 4 nach Hilfsantrag „Abhängig 1“ aus
dem MPEG-4 Standard bekannt.



6.    Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 3.0‘ vom 26. Januar 2024 – und damit auch der Gegenstand des Patentanspruchs 6 nach Hilfsantrag 3.0‘ – sind nicht patentfähig.


                                                                             105/120

Hilfsantrag 3.0’ basiert auf Hilfsantrag 3.0:

     1HA3 A method for predicting in a decoding device a bandwidth extension frequency band signal according to an encoding bit-rate and a signal type,
           comprising
     1.1HA3.0’ demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal, a signal type,
                 and a frequency envelope of a bandwidth extension frequency band;
     1.1.1HA3.0 pre-setting a start frequency bin of a bandwidth extension frequency
                  band depending on the encoding bit-rate by the decoding device;
     1.2HA1       determining (101) whether a highest frequency bin, to which a bit is
                  allocated, of the frequency domain signal is less than the preset
                  start frequency bin of the bandwidth extension frequency band;
     …            …
     1.5HA3.0 predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
                frequency band and the frequency envelope of the bandwidth extension frequency band;
     1.5.1HA3     wherein the frequency envelope of the bandwidth extension frequency band is acquired based on the signal type;
     …            …


Der Hilfsantrag 3.0‘ ergänzt im Vergleich zum Hilfsantrag 3.0, dass die Decodierung
des empfangenen Bitstroms neben dem (niederfrequenten) Frequenzbereichssignal und der spektralen Einhüllenden des BWE-Bereichs auch den Signaltyp liefert,
wie dies auch im Anspruch 4 nach Hilfsantrag „Abhängig 1“ angegeben ist. Der Anspruch 1 nach Hilfsantrag 3.0‘ entspricht inhaltlich im Wesentlichen dem Anspruch 4 nach Hilfsantrag „Abhängig 1“. Insofern wird zur Patentfähigkeit des Gegenstands des Anspruchs 1 nach Hilfsantrag 3.0‘ auf die obigen Ausführungen zum
Hilfsantrag „Abhängig 1“ verwiesen, die hier entsprechend gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0‘ ist somit aus dem MPEG-4
Standard bekannt.


                                                                                106/120

7.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 3.0‘‘ vom 26. Januar 2024 – und damit auch der Gegenstand des Patentanspruchs 6 nach Hilfsantrag 3.0‘‘– sind nicht patentfähig.


Der Anspruch 1 nach Hilfsantrag 3.0’’ unterscheidet sich vom Anspruch 1 nach Hilfsantrag 3.0’ nur in dem Merkmal 1.1HA3.0’’:

     1HA3 A method for predicting in a decoding device a bandwidth extension frequency band signal according to an encoding bit-rate and a signal type,
           comprising
     1.1HA3.0’’ demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal, the signal
               type, and a frequency envelope of a bandwidth extension frequency
               band;


Der Hilfsantrag 3.0‘‘ gibt somit in Merkmal 1.1HA3.0‘‘ explizit an, dass der decodierte
Signaltyp der bereits in dem einleitenden Merkmal 1HA3 genannte Signaltyp ist. Der
Fachmann versteht jedoch bereits den Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0 aufgrund fehlender anderslautender Angaben so, dass in den Merkmalen
1HA3 und 1.5HA3 stets ein und derselbe Signaltyp gemeint ist, insbesondere derjenige, der dem Dekodierer nach Dekodierung des empfangenen Bitstroms zur Verfügung steht, wie dies im Hilfsantrag „Abhängig 1“ und im Hilfsantrag 3.0‘‘ explizit
ausformuliert ist.


Insofern wird zur Patentfähigkeit des Gegenstands des Anspruchs 1 nach Hilfsantrag 3.0‘‘ auf die obigen Ausführungen zum Hilfsantrag 3.0‘ bzw. Hilfsantrag „Abhängig 1“ verwiesen, die hier entsprechend gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 3.0‘‘ ist somit aus dem MPEG-4 Standard bekannt.




                                                                                107/120

8.    Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 3
vom 13. September 2022 (Az.: 4 Ni 49/22 (EP); insofern gleichlautend mit dem Anspruch 1   nach       Hilfsantrag 3   vom   12. Juli 2022   im   Verfahren   mit     dem
Az.: 4 Ni 53/22 (EP)) – und damit auch der Gegenstand des Patentanspruchs 6
nach Hilfsantrag 3 – sind nicht patentfähig.


Der Anspruch 1 nach Hilfsantrag 3 lautet (Änderungen gegenüber der erteilten Fassung gekennzeichnet):

     1HA3 A method for predicting in a decoding device a bandwidth extension
           frequency band signal according to an encoding bit-rate and a signal
           type, comprising
     1.1        demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;
     1.1.1HA3     pre-setting a start frequency bin of a bandwidth extension frequency band depending on the encoding bit-rate and selecting
                  a predetermined frequency band range of the frequency domain signal by the decoding device;
     1.2HA1 determining (101) whether a highest frequency bin, to which a bit is
             allocated, of the frequency domain signal is less than the preset start
             frequency bin of the bandwidth extension frequency band;
     1.3     predicting (102) an excitation signal of the bandwidth extension frequency band
     1.3.1HA1     according to an excitation signal within the predetermined frequency band range of the frequency domain signal and the preset
                  start frequency bin of the bandwidth extension frequency band
     …
     1.5     predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
             frequency band and a frequency envelope of the bandwidth extension
             frequency band;
     1.5.1HA3     wherein the frequency envelope of the bandwidth extension
                  frequency band is acquired based on the signal type;
     …            …



                                                                                   108/120

Der Hilfsantrag 3 kombiniert somit die Hilfsanträge 2 (Merkmal 1.1.1HA3 entspricht
inhaltlich Merkmal 1.1.1HA2) und 3.0 (Merkmale 1HA3 und 1.5.1HA3).


Insofern wird zur Patentfähigkeit des Anspruchs 1 nach Hilfsantrag 3 auf die obigen
Ausführungen zu den Hilfsanträgen 2 und 3.0 verwiesen, die hier entsprechend
gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 3 ist somit aus dem MPEG-4
Standard bekannt.



9.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 3a
vom 28. Februar 2023 – und damit auch der Gegenstand des Patentanspruchs 6
nach Hilfsantrag 3a – sind nicht patentfähig.


Der Anspruch 1 nach Hilfsantrag 3a unterscheidet sich nur im Merkmal 1.1HA3.0 vom
Hilfsantrag 3:

     1HA3 A method for predicting in a decoding device a bandwidth extension frequency band signal according to an encoding bit-rate and a signal type,
           comprising
     1.1HA3.0 demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal and a frequency
                 envelope of a bandwidth extension frequency band;
     1.1.1HA3      pre-setting a start frequency bin of a bandwidth extension frequency
                   band depending on the encoding bit-rate and selecting a predetermined frequency band range of the frequency domain signal by the
                   decoding device;
     …
     1.5.1HA3      wherein the frequency envelope of the bandwidth extension frequency band is acquired based on the signal type;
     …             …




                                                                                109/120

Der Hilfsantrag 3a kombiniert somit die Hilfsanträge 3.0 (Merkmal 1.1HA3.0) und 3
(Merkmale 1HA3, 1.1.1HA3 und 1.5.1HA3).


Insofern wird zur Patentfähigkeit des Gegenstands des Anspruchs 1 nach Hilfsantrag 3a auf die obigen Ausführungen zu den Hilfsanträgen 3.0 und 3 verwiesen, die
hier entsprechend gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 3a ist somit aus dem MPEG-4
Standard bekannt.



10.       Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 4
vom 13. September 2022 (Az.: 4 Ni 49/22 (EP); insofern gleichlautend mit dem Anspruch 1 nach Hilfsantrag 4 vom 12. Juli 2022 im Verfahren mit dem
Az.: 4 Ni 53/22 (EP)) lautet (Änderungen gegenüber der erteilten Fassung gekennzeichnet) – und damit auch der Gegenstand des Patentanspruchs 6 nach Hilfsantrag 4 – sind nicht patentfähig.


Der Anspruch 1 nach Hilfsantrag 4 lautet (Änderungen gegenüber der erteilten Fassung gekennzeichnet):

      1      A method for predicting a bandwidth extension frequency band signal,
             comprising
      1.1       demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal;
      1.1.1HA4    by using decoded frequency domain coefficients of an excitation signal of the frequency domain signal
      …         …;
      1.8HA4      wherein the copies are made by mirror copying.


Das Merkmal 1.1.1HA4 gibt an, dass das Dekodieren des demultiplexten Bitstroms
zum Erhalten eines Frequenzbereichssignals das Verwenden von dekodierten Frequenzbereichskoeffizienten eines Anregungssignals des Frequenzbereichssignals




                                                                             110/120

umfasst. Auch dieses Merkmal verlangt nicht, dass die beanspruchte Prädiktion eines BWE-Signals durchgängig im Frequenzbereich durchgeführt wird. Das Merkmal
1.1.1HA4 bringt nur zum Ausdruck, dass der vom Fachmann im Anspruch 1 mitgelesene Kern-Dekodierer Spektralkomponenten aus dem Bitstrom dekodiert, um das
(niederfrequente) Anregungssignal zu erhalten.


Dies ist beim MPEG-4 Standard der Fall (Subpart 4, 4.1.1.2 Overview of the encoder
and decoder tools, S. 6: The input to the bitstream payload demultiplexer tool is the
MPEG-4 GA bitstream payload. The demultiplexer separates the bitstream payload
into the parts for each tool, and provides each of the tools with the bitstream payload
information related to that tool. The outputs from the bitstream payload demultiplexer tool are: • The quantized (and optionally noiselessly coded) spectra represented by … • the sectioning information and the noiselessly coded spectra (AAC)
… The AAC noiseless decoding tool takes information from the bitstream payload
demultiplexer, parses that information, decodes the Huffman coded data, and reconstructs the quantized spectra and the Huffman and DPCM coded scalefactors.)


Es widerspricht weder der erteilten Fassung des Anspruchs 1 noch der Fassung
nach Hilfsantrag 4, dass beim MPEG-4 Standard, wie zum Hauptantrag dargelegt,
das Frequenzbereichssignal des Kern-Dekodierers in ein Zeitbereichssignal umgewandelt und dem SBR-Werkzeug zur Verfügung gestellt wird, der seinerseits eine
Transformation in den QMF-Bereich durchführt, der dem Frequenzbereich entspricht.


Bei dem im Merkmal 1.8HA4 genannten „spiegelnden Kopieren“ wechseln sich „Vorwärtskopien“ (niederfrequenter Bereich von fexc_start bis fexc_end) und „Rückwärtskopien“ (niederfrequenter Bereich von fexc_start bis fexc_end) ab, jedenfalls bei den ganzzahligen Kopien (Streitpatentschrift, Abs. 0038, 0049).


Diese Art des Kopierens ist dem Fachmann, der sich mit SBR-Bandbreitenerweiterungswerkzeugen bei Audio-Codecs beschäftigt, wohlbekannt, vgl. bspw. die im
Verfahren befindlichen Dokumente:

   ·   TALEB, Fig. 8A, 8B



                                                                                  111/120

      ·    CN‘072, Abs. 0005 i. V. m. Fig. 1, 2
      ·    DEN BRINKER, S. 7, li. Sp., Absatz 1: mirrored or copied
      ·    NAGEL, S. 145, Fig. 1


Der Fachmann hat auch Anlass, diese Variante im MPEG-4 Standard optional vorzusehen, denn ihm ist unmittelbar bewusst, dass sich damit „weichere“ Übergänge
ohne Amplitudensprünge zwischen den einzelnen Kopien im Frequenzspektrum ergeben (NAGEL, Fig. 1 (a)) als beim „normalen“ Kopieren (NAGEL, Fig. 1 (b)):




Der Gegenstand des Anspruchs 1 nach Hilfsantrag 4 ergibt sich somit für den Fachmann in naheliegender Weise aus dem MPEG-4 Standard.



11.        Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag 5
vom 13. September 2022 (Az.: 4 Ni 49/22 (EP); insofern gleichlautend mit dem Anspruch 1       nach     Hilfsantrag 5   vom   12. Juli 2022   im   Verfahren   mit     dem
Az.: 4 Ni 53/22 (EP)) – und damit auch der Gegenstand des Patentanspruchs 6
nach Hilfsantrag 5 – sind nicht patentfähig.


11.1 Der Anspruch 1 nach Hilfsantrag 5 lautet (Änderungen gegenüber der erteilten Fassung gekennzeichnet):

          1HA5 A method for predicting a bandwidth extension frequency band signal for
               a harmonic signal, comprising
          1.1HA5 demultiplexing (100) a received bitstream, and decoding the demultiplexed bitstream to obtain a frequency domain signal and an initial
                 frequency envelope of a bandwidth extension frequency band;
          …         …



                                                                                     112/120

     1.5     predicting (104) the bandwidth extension frequency band signal according to the predicted excitation signal of the bandwidth extension
             frequency band and a frequency envelope of the bandwidth extension
             frequency band;
     1.9HA5 wherein the determination of the frequency envelope of the bandwidth extension frequency band comprises using a value that is
             obtained by performing weighting calculation on the initial frequency envelope and N adjacent initial frequency envelopes,
             wherein N is greater than or equal to 1;
     …          …


11.2 Der Anspruch 1 nach Hilfsantrag 5 schränkt im Merkmal 1HA5 das beanspruchte Verfahren auf die Prädiktion eines BWE-Signals auf den Fall eines harmonischen Signals ein. Damit bleibt offen, welche Verfahrensschritte im Falle eines
nicht-harmonischen Signals ausgeführt werden. Der Anspruch 1 nach Hilfsantrag 5
verlangt somit nicht, dass die Verfahrensschritte ausschließlich dann durchgeführt
werden, wenn ein harmonisches Signal vorliegt.


Unter einem harmonischen Signal versteht der Fachmann ein Signal, das im Wesentlichen aus sinusförmigen Signalen mit – zumindest im betrachteten Zeitabschnitt
– fester Grundfrequenz und gegebenenfalls ein oder mehreren Oberschwingungen
(„Harmonischen“) besteht. Solche Signale bzw. Abschnitte können sowohl bei
menschlicher Sprache („voiced signal“) als auch z. B. bei Musiksignalen auftreten.


Das Merkmal 1.9HA5 bringt zusammen mit dem Merkmal 1.1HA5 zum Ausdruck, dass
die decodierte „anfängliche“ (i. S. v. noch nicht veränderte) spektrale Einhüllende
des zu generierenden BWE-Bereichs (initial frequency envelope of a bandwidth extension frequendy band) dadurch modifiziert wird, dass eine Gewichtungsberechnung zwischen ihr und N benachbarten anfänglichen Einhüllenden stattfindet, wobei
N größer oder gleich Eins sein soll.


Das Streitpatent schweigt dazu, ob die Gewichtungsberechnung im Frequenzund/oder im Zeitbereich stattfinden soll. Eine Gewichtung im Frequenzbereich setzt



                                                                            113/120

voraus, dass die anfängliche spektrale Einhüllende nicht den gesamten BWE-Bereich betrifft, sondern nur einen Teilbereich. Dafür spricht, dass dem Fachmann bekannt ist, dass bei BWE-Verfahren der zu erzeugende BWE-Bereich üblicherweise
in eine Vielzahl von Frequenz-Subbändern aufgeteilt ist und für jeden dieser Teilbereiche jeweils ein Skalenfaktor, d. h. eine Information über die jeweilige Amplitude,
vom Kodierer zum Dekodierer übertragen wird. Weiter spricht für dieses Verständnis, dass in Absatz 0024 der Streitpatentschrift, der sich mit der Normierung des
niederfrequenten Signalanteils im Dekodierer befasst, ebenfalls eine Mittelung über
spektrale Einhüllende frequenzmäßig benachbarter Subbänder stattfindet.


Jedoch umfasst das Merkmal 1.9HA5, auch vor dem Hintergrund der gesamten Offenbarung des Streitpatents und unter Einbeziehung des Fachwissens, auch eine
Mittelung über benachbarte zeitliche Abschnitte, etwa Subrahmen. Denn dem Fachmann ist bekannt, dass Audio-Codecs rahmenbasiert arbeiten (Streitpatentschrift,
Abs. 0014: one frame being 20 ms) und manche Parameter auf Basis von Subrahmen (typische Subrahmenlänge: 4 bzw. 5 ms) bestimmen, insbesondere auch die
Skalenfaktoren für den im Dekodierer künstlich zu erzeugenden BWE-Bereich
(BESSETE, S. 622, re. Sp., letzter Absatz, S. 623, li. Sp.: the higher band gain is
transmitted using 4 bits per subframe; MPEG-4, Subpart 4, 4.6.18.3.6 Requirements, S. 237, vierter Aufzählungspunkt, wonach die Anzahl der zeitlich aufeinanderfolgenden spektralen Einhüllenden eines SBR-Rahmens kleiner als vier oder
fünf sein soll).


Das Streitpatent äußert sich nicht dazu, wie die Gewichtungsberechnung durchgeführt werden soll, insbesondere nicht, mit welcher Auflösung im Zeit- und/oder Frequenzbereich.


11.3 Es kann dahinstehen, ob der Gegenstand des Anspruchs 1 nach Hilfsantrag 5 ursprünglich offenbart ist, denn jedenfalls ist er nicht patentfähig.


Das Merkmal 1HA5 ist aus dem MPEG-4 Standard bekannt, weil dieser selbstverständlich für jede Signalart geeignet ist, jedenfalls auch für harmonische Signale
(MPEG-4, Subpart 4, 4.1.1.2 Overview of the encoder and decoder tools, S. 9: The



                                                                               114/120

SBR tool regenerates the highband of the audio signal. It is based on replication of
the sequences of harmonics, truncated during encoding. It adjusts the spectral envelope of the generated high-band and applies inverse filtering, and adds noise and
sinusoidal components in order to recreate the spectral characteristics of the original
signal.).


Auch die in Merkmal 1.1HA5 genannte Decodierung einer anfänglichen spektralen
Einhüllenden ist aus dem MPEG-4 Standard bekannt. Die Matrix EOrig beinhaltet LE
Spalten (wegen der zeitlichen Unterteilung eines SBR-Rahmens in LE Unterabschnitte) und NHigh Zeilen (Anzahl der Subbänder des SBR-Bereichs bei hoher Frequenzauflösung) mit den dekodierten Skalenfaktoren, d. h. der anfänglichen spektralen Einhüllenden (MPEG-4, Subpart 4, 4.6.18.2.6 Variables, S. 223):




Das Vorsehen einer Glättung der subbandspezifischen spektralen Einhüllenden
durch Berücksichtigung der spektralen Einhüllenden einer gewissen Anzahl benachbarter Subbänder gemäß Merkmal 1.9HA5 geht über fachmännisches Vorgehen
nicht hinaus.


Dementsprechend findet auch beim MPEG-4 Standard eine Gewichtungsberechnung der anfänglichen spektralen Einhüllenden über eine bestimmte Anzahl von
zeitlich bzw. frequenzmäßig benachbarten spektralen Einhüllenden statt (MPEG-4,
Subpart 4, 4.6.18.7.3 Estimation of current envelope, S. 252). In Abhängigkeit des
Werts der Variablen bs_interpol_freq findet eine Interpolation im Zeitbereich oder
im Zeit- und Frequenzbereich statt.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 5 ist somit aus dem MPEG-4
Standard bekannt.




                                                                                115/120

12.    Der Gegenstand des Patentanspruchs 5 in der Fassung nach Hilfsantrag
„Abhängig 2“ vom 26. Januar 2024 – und damit auch der Gegenstand des Patentanspruchs 10 nach Hilfsantrag „Abhängig 2“ – sind nicht patentfähig.


12.1 Der Anspruch 5 nach Hilfsantrag „Abhängig 2“, der den zweiten Teil des Anspruchs 5 der erteilten Fassung umfasst, lautet in seinem Rückbezug auf den Anspruch 4 der erteilten Fassung (Änderungen gegenüber Anspruch 4 nach Hilfsantrag „Abhängig 1“ gekennzeichnet):

      1 – 1.7.4 wie erteilte Fassung
      1.5.2AH1   wherein before the predicting the bandwidth extension frequency
                 band signal according to the predicted excitation signal of the bandwidth extension frequency band and a frequency envelope of the
                 bandwidth extension frequency band, the method further comprises:
      1.1AH1     decoding the bitstream to obtain a signal type; and
      1.5.1AH1   acquiring the frequency envelope of the bandwidth extension frequency band according to the signal type,
      1.5.1AH2   wherein the acquiring the frequency envelope of the bandwidth
                 extension frequency band according to the signal type comprises:
      1.10AH2    when the signal type is a harmonic signal, demultiplexing the
                 received bitstream, decoding the demultiplexed bitstream to
                 obtain an initial frequency envelope of the bandwidth extension frequency band, and using a value that is obtained by performing a weighting calculation on the initial frequency envelope and N adjacent initial frequency envelopes as the frequency envelope of the bandwidth extension frequency band,
                 wherein N is greater than or equal to 1.



12.2 Der Anspruch 1 nach Hilfsantrag „Abhängig 2“ beschreibt in dem Merkmal
1.5.1AH2, welches dem Merkmal 1.5.1HA3 der Hilfsantragsgruppe 3 entspricht, dass




                                                                               116/120

die Gewinnung der spektralen Einhüllenden des BWE-Bereichs auf dem dekodierten Signaltyp basiert. Nach den Merkmalen 1.5.2AH2 und 1.10AH2 wird diese Signaltypabhängigkeit für den Fall eines harmonischen Signals dadurch konkretisiert,
dass die spektrale Einhüllende des BWE-Bereichs durch eine Gewichtungsberechnung aus einer anfänglichen und N benachbarten anfänglichen spektralen Einhüllenden zu ermitteln ist.


Zwar bleibt damit – im Gegensatz zum Anspruch 5 der erteilten Fassung, der sich
auch mit nicht-harmonischen Signalen befasst – offen, welche Verfahrensschritte
im Falle eines nicht-harmonischen Signals zur Gewinnung der spektralen Einhüllenden auszuführen sind. Jedoch verlangt der Anspruch 1 nach Hilfsantrag „Abhängig 2“ eine Decodierung des Signaltyps und, dass der decodierte Signaltyp in die
Bestimmung der spektralen Einhüllenden eingeht, wobei für den Fall des harmonischen Signaltyps genauere Angaben gemacht sind, die jedenfalls zu einem gewissen Teil exklusiv im Fall eines harmonischen Signals auszuführen sind.


Hinsichtlich des fachmännisches Verständnisses der Begriffe „harmonisches Signal“ und „Gewichtungsberechnung“ des Merkmals 1.10AH2 wird auf die vorstehenden Ausführungen zu den Merkmalen 1HA5 und 1.9HA5 verwiesen, die hier entsprechend gelten.


12.3 Der Gegenstand des Anspruchs 5 nach Hilfsantrag „Abhängig 2“ ist nicht patentfähig.

Aus dem MPEG-4 Standard ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 5
bekannt, wie vorstehend dargelegt und begründet.

Der Anspruch 5 nach Hilfsantrag „Abhängig 2“ verlangt darüber hinaus, wie zu Auslegung seines Gegenstands erläutert, dass sich das Verfahren zur Bestimmung der
spektralen Einhüllenden des BWE-Bereichs für ein harmonisches Signal von dem
Verfahren zur Bestimmung der spektralen Einhüllenden des BWE-Bereichs für ein
nicht-harmonisches Signal unterscheidet. Wie zu der Hilfsantragsgruppe 3 dargelegt, zeigt der MPEG-4 Standard auch diese Abhängigkeit der Bestimmung der




                                                                          117/120

spektralen Einhüllenden vom Signaltyp (harmonisch oder nicht-harmonisch), nämlich durch die Berücksichtigung, ob in Subbändern des SBR-Bereichs sinusförmige
Signalkomponenten vorliegen oder nicht.


Danach ist der Gegenstand des Anspruchs 5 nach Hilfsantrag „Abhängig 2“ aus
dem MPEG-4 Standard bekannt.


Sofern der Fachmann den Anspruch 5 des Hilfsantrags „Abhängig 2“ jedoch so versteht, dass sich nicht nur die Bestimmung der spektralen Einhüllenden für harmonische und nicht-harmonische Signaltypen – irgendwie – unterscheiden müssen, sondern darüber hinaus nur für harmonische Signale eine Gewichtungsberechnung zur
Bestimmung der spektralen Einhüllenden durchgeführt wird, nicht jedoch für nichtharmonische Signale, so ergibt sich dieses Vorgehen für den Fachmann in naheliegender Weise aus dem MPEG-4 Standard in Kombination mit seinem Fachwissen.
Denn dem Fachmann ist bewusst, dass eine Mittelung der spektralen Einhüllenden
über benachbarte Subfrequenzbänder insbesondere dann wichtig ist, wenn im betrachteten Subband – aufgrund des harmonischen Signaltyps – eine große
Amplitude vorliegt, während bei nicht-harmonischen, z. B. rauschförmigen, Signalen mit vergleichsweise „flachen“ Frequenzspektren, eine Mittelung keinen großen
Effekt zeigt, so wie dies auch die Klägerinnen vorgetragen haben (z. B. in der Nichtigkeitsklage der Klägerin zu 2, Rn 178, 183). Insofern hat der Fachmann Anlass,
den MPEG-4 Standard insofern abzuwandeln, als dass er die in Abschnitt 4.6.18.7.3
beschriebene Gewichtung bzw. Mittelung im Frequenzbereich nur bei einem harmonischen Signaltyp durchführt und auf diese Weise – jedenfalls im zeitlichen
Durchschnitt betrachtet – Rechenaufwand einspart.


Der wie vorstehend ausgelegte Gegenstand des Anspruchs 5 nach Hilfsantrag „Abhängig 2“ ergibt sich somit für den Fachmann in naheliegender Weise aus dem
MPEG-4 Standard.




                                                                             118/120

13.   Da die Beklagte das Streitpatent jeweils mit geschlossenen Anspruchssätzen verteidigt, bedarf es keiner Erörterung der weiteren Patentansprüche der jeweiligen verteidigten Fassungen, weil im Falle der fehlenden Schutzfähigkeit eines
Patentanspruchs einer Fassung auch deren weitere Patentansprüche und damit
die gesamte Fassung, mit der das Streitpatent verteidigt wird, nicht schutzfähig sind
(vgl. hierzu BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 –
Datengenerator).




                                         B.
                              Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.

Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.

Der nicht nachgelassene Schriftsatz vom 18. März 2024, mit dem die Beklagte nach
eigenen Angeben ihren mündlich vorgebrachten Vortrag lediglich schriftlich zusammenfassend darlegt und an einigen Stellen zu aus ihrer Sicht entscheidungserheblichen Rechtsfragen Stellung nimmt, enthält kein entscheidungserhebliches Vorbringen und macht eine Stellungnahme der Klägerinnen nicht erforderlich. Der nicht
nachgelassene Schriftsatz hat keinen Anlass zur Wiedereröffnung der mündlichen
Verhandlung gegeben (§ 99 Abs. 1 PatG i. V. m. § 156 Abs. 2 ZPO).




                                         C.
                              Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.




                                                                              119/120

Die Berufungsschrift, die auch als elektronisches Dokument gemäß § 130a ZPO eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im
Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur
nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur
versehen sein, die von einer internationalen Organisation auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich zur Bearbeitung durch das
jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung
oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die
Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Werner           Schwarz             Altvater         Matter             Dr. Haupt




                                                                            120/120
