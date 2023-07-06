---
ecli: "ECLI:DE:BPatG:2023:060723U2Ni36.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 36/21"
decided: "2023-07-06"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=19&nr=43863&anz=529&pos=288&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-07-06_2_Ni_36_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0227.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 36/21 vom 2023-07-06

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      Verkündet am
                                                       6. Juli 2023
2 Ni 36/21 (EP)                                             …
(Aktenzeichen)




                     In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:060723U2Ni36.21EP.0

                                       -2-




              betreffend das europäische Patent EP 2 723 078
                             (DE 60 2012 032 040)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 6. Juli 2023 unter Mitwirkung der Vorsitzenden
Richterin Hartlieb sowie der Richter Dipl.-Phys. Univ. Dr. Forkel, Dr. Himmelmann,
Dipl.-Phys. Univ. Dr. Städele und Dr.-Ing. Harth


für Recht erkannt:


I.      Das europäische Patent EP 2 723 078 wird mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


II.     Die Kosten des Rechtsstreits trägt die Beklagte.


III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des zu
        vollstreckenden Betrages vorläufig vollstreckbar.

                                          -3-



                                    Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in englischer Verfahrenssprache erteilten europäischen Patents EP 2 723 078
(deutsches Aktenzeichen DE 60 2012 032 040) (Streitpatent), das am 20. Juni 2012
unter Inanspruchnahme der Prioritäten KR 20110059850 vom 20. Juni 2011,
KR 20110065708 vom 1. Juli 2011, KR 20110119214 vom 15. November 2011 und
KR 20110125353 vom 28. November 2011 angemeldet worden ist und das die
Bezeichnung         „IMAGE     DECODING          APPARATUS“          (Vorrichtung       zur
Bilddekodierung) trägt. Der Hinweis auf die Erteilung des Streitpatents wurde am
3. Mai 2017 veröffentlicht. Die dem Streitpatent zugrundeliegende internationale
Anmeldung wurde am 27. Dezember 2012 unter der Publikationsnummer
WO 2012 / 177 053 A2 veröffentlicht.


Das Streitpatent betrifft eine Vorrichtung zum Decodieren von digital codierten
Videobildern und beschäftigt sich mit der Verbesserung herkömmlicher Codier- und
Decodierverfahren. Zu den zum Anmeldezeitpunkt bekannten Codierverfahren zählt
insbesondere der im Jahr 2003 verabschiedete H.264-Standard (auch AVC-Standard).    Die    Lehre    des    Streitpatents    liegt   auf   dem     Gebiet      der
Bilddatenverarbeitung, befasst sich insbesondere mit dem Decodieren von Videos
und betrifft speziell die Intra-Prädiktion (vgl. Streitpatentschrift, Absatz [0001]).


Das in vollem Umfang angegriffene Streitpatent umfasst 3 Patentansprüche: den
unabhängigen Anspruch 1 sowie die abhängigen Ansprüche 2 und 3.


Der erteilte Patentanspruch 1 lautet gemäß EP 2 723 078 B1 (Streitpatentschrift)
mit an die Anlage NK III der Klägerin angelehnter Merkmalsgliederung und vom
Senat gegenüber der Anlage NK III der Klägerin teilweise veränderten deutschen
Übersetzung:

                                            -4-



1     1. A video decoding apparatus 1. Videodecodierungsvorrichtung (200),
      (200) comprising:                           umfassend:
2     a prediction block generating unit eine                                Vorhersageblockto generate a prediction block              Erzeugungseinheit            für         einen
                                                  Vorhersageblock zum Erzeugen eines
                                                  Vorhersageblockes
2.1   by performing intra prediction on durch Durchführen von Intra-Vorhersage
      a current block,                            auf einem gegenwärtigen Block
2.2   and by performing filtering on a und durch Durchführen von Filterung auf
      filtering    target     pixel   in    the einem        Filterungszielpixel      in    dem
      prediction block                            Vorhersageblock
2.2.1 using a plurality of different filters unter Verwendung einer Mehrzahl von
      for a plurality of different intra unterschiedlichen              Filtern      für    eine
      prediction modes of the current Mehrzahl von unterschiedlichen Intrablock, respectively,                        Vorhersagemodi       des     gegenwärtigen
                                                  Blockes,
2.2.2 the plurality of different intra wobei                    die      Mehrzahl            von
      prediction modes include the DC unterschiedlichen Intra-Vorhersagemodi
      mode, and include at least one den DC-Modus und wenigstens einen
      mode other than the DC mode,                Modus verschieden von dem DC-Modus
                                                  verschiedenen Modus enthält,
2.2.3 wherein           performing         intra wobei    das     Durchführen        von   Intraprediction includes determining Vorhersage das Bestimmen eines Intraan intra prediction mode for the Vorhersagemodus                         für          den
      current block; and                          gegenwärtigen Block enthält; und
3     a reconstructed block generating eine Rekonstruierte-Blöcke-Erzeugungsunit to generate a reconstructed einheit für einen rekonstruierten Block
      block based on the prediction zum Erzeugen eines rekonstruierten
      block       and     a    reconstructed Blockes            basierend          auf      dem
      residual block corresponding to Vorhersageblock                        und           einem
      the current block,                          rekonstruierten        Restblock,          der

                                             -5-



                                                   entsprechend dem gegenwärtigen Block
                                                   entspricht,
4     wherein when the determined wobei,                    wenn      der     bestimmte       Intraintra prediction mode of the Vorhersagemodus des gegenwärtigen
      current block is a DC mode,                  Blockes ein DC-Modus ist,
      the filtering target pixel is a das                        Filterungszielpixel            ein
      prediction pixel on at least one of          Vorhersagepixel von auf einer linken
      a left vertical prediction pixel line vertikalen            Vorhersagepixellinie          ist,
      that is one vertical pixel line welche eine einzige vertikale Pixellinie ist,
      positioned at a leftmost side of the die an einer ganz linken Seite des
      prediction block                             Vorhersageblockes angeordnet ist,
      and      an        upper        horizontal und/oder ein Vorhersagepixel auf einer
      prediction pixel line that is one oberen horizontalen Vorhersagepixellinie
      horizontal pixel line positioned at ist, welche eine einzige horizontale
      an    uppermost          side    of    the Pixellinie ist, die an einer obersten Seite
      prediction block,                            des Vorhersageblockes angeordnet ist,
5     for a plurality of block sizes of the wobei für eine Mehrzahl von Blockgrößen
      current block, same filter shape, des gegenwärtigen Blockes dieselbe
      same filter tap and same filter Filterform,                 dieselben     Filtertaps     und
      coefficients are used for the dieselben                    Filterkoeffizienten    für     die
      filtering of the current block when Filterung des gegenwärtigen Blockes
      the determined intra prediction verwendet werden, wenn der bestimmte
      mode of the current block is the Intra-Vorhersagemodus                                   des
      DC mode,                                     gegenwärtigen Blockes der DC-Modus
                                                   ist,
5.1   the    plurality    of     block      sizes wobei die Mehrzahl von Blockgrößen
      includes 4x4, 8x8 and 16x16,                 4x4, 8x8 und 16x16 enthält,
6.1   when      the      determined         intra wobei,    wenn      der     bestimmte       Intraprediction mode of the current Vorhersagemodus des gegenwärtigen
      block is the DC mode and the Blockes der DC-Modus ist und das
      filtering target pixel is positioned Filterungszielpixel an einer ganz linken

                                       -6-



      at a leftmost upper side of the oberen Seite des Vorhersageblockes
      prediction block, the filtering is angeordnet ist, die Filterung auf dem
      performed on the filtering target Filterungszielpixel              durch        Anwenden
      pixel by applying a first filter using eines ersten Filters unter Verwendung
      a prediction value generated in eines in dem DC-Modus erzeugten
      the DC mode, an upper reference Vorhersage-wertes,                      eines       oberen
      pixel, and a left reference pixel,     Referenzpixels        und         eines          linken
                                             Referenzpixels durchgeführt wird,
6.2   when     the    determined      intra wobei,     wenn       der     bestimmte           Intraprediction mode of the current Vorhersagemodus des gegenwärtigen
      block is the DC mode, the filtering Blockes          der    DC-Modus             ist,     das
      target pixel is positioned at the left Filterungszielpixel         an      der          linken
      vertical prediction pixel line and vertikalen                     Vorhersagepixellinie
      the filtering target pixel is not angeordnet ist und das Filterungszielpixel
      positioned at the upper horizontal nicht       an     der     oberen        horizontalen
      prediction pixel line, the filtering is Vorhersagepixellinie angeord-net ist, die
      performed on the filtering target Filterung auf dem Filterungs-zielpixel
      pixel by applying a second filter durch Anwenden eines zweiten Filters
      using the prediction value and the unter                   Verwendung                     des
      left reference pixel,                  Vorhersagewertes            und     des          linken
                                             Referenzpixels durchgeführt wird,
6.3   when     the    determined      intra wobei,     wenn       der     bestimmte           Intraprediction mode of the current Vorhersagemodus des gegenwärtigen
      block is the DC mode, the filtering Blockes          der    DC-Modus             ist,     das
      target pixel is positioned at the Filterungszielpixel              an      der      oberen
      upper horizontal prediction pixel horizontalen                    Vorhersagepixellinie
      line and the filtering target pixel is angeord-net           ist           und            das
      not positioned at the left vertical Filterungszielpixel nicht an der linken
      prediction pixel line, the filtering is vertikalen                Vorhersagepixellinie
      performed on the filtering target angeordnet ist, die Filterung auf dem
      pixel by applying a third filter Filterungszielpixel               durch        Anwenden

                                            -7-



        using the prediction value and the eines dritten Filters unter Verwendung
        upper reference pixel,                    des Vorhersagewertes und des oberen
                                                  Referenzpixels durchgeführt wird,
 7.1    the upper reference pixel is a wobei das obere Referenzpixel ein
        reconstructed      reference     pixel rekonstruiertes Referenzpixel oberhalb
        above the filtering target pixel,         des Filterungszielpixels ist,
 7.2    the left reference pixel is a wobei                das     linke   Referenzpixel   ein
        reconstructed reference pixel left rekonstruiertes Referenzpixel links von
        of the filtering target pixel,            dem Filterungszielpixel ist,
 8.1    the filtering of the first filter is wobei die Filterung mit dem des ersten
        performed based on 2/4 of the Filters               basierend         auf   2/4    des
        prediction value, 1/4 of a value of Vorhersagewertes, 1/4 eines Wertes des
        the upper reference pixel and 1/4 oberen Referenzpixels und 1/4 eines
        of a value of the left reference Wertes              des     linken     Referenzpixels
        pixel,                                    durchgeführt wird,
 8.2    the filtering of the second filter is wobei die Filterung mit dem des zweiten
        performed based on 3/4 of the Filters               basierend         auf   3/4    des
        prediction value and 1/4 of a value Vorhersagewertes und 1/4 eines Wertes
        of the left reference pixel,              des linken Referenzpixels durchgeführt
                                                  wird,
 8.3    and the filtering of the third filter is und wobei die Filterung mit dem des
        performed based on 3/4 of the dritten Filters basierend auf 3/4 des
        prediction value and 1/4 of a value Vorhersagewertes und 1/4 eines Wertes
        of the upper reference pixel.             des oberen Referenzpixels durchgeführt
                                                  wird.


Die abhängigen Patentansprüche 2 und 3 des Streitpatents lauten in der
Streitpatentschrift in der englischen Fassung und in einer vom Senat teilweise
geänderten deutschen Fassung wie folgt:

                                              -8-



        2. The video decoding apparatus 2. Die Videodecodierungsvorrichtung (200)
        (200) of claim 1, wherein when nach des Anspruchs 1, wobei, wenn der
        the determined intra prediction bestimmte            Intra-Vorhersagemodus        des
        mode of the current block is the gegenwärtigen Blockes der DC-Modus ist,
        DC       mode    the    filtering     is die Filterung durchgeführt wird, wenn der
        performed when the current gegenwärtige Block ein Block einer Lumablock is a luma component Komponente ist, und die Filterung nicht
        block, and the filtering is not durchgeführt wird, wenn der gegenwärtige
        performed when the current Block ein Block einer Chroma-Komponente
        block is a chroma component ist.
        block.
        3. The video decoding apparatus 3. Die Videodecodierungsvorrichtung (200)
        (200) of claim 1, wherein when nach des Anspruchs 1, wobei, wenn der
        the determined intra prediction bestimmte            Intra-Vorhersagemodus        des
        mode of the current block is the gegenwärtigen Blockes der DC-Modus ist,
        DC       mode    the    filtering     is die Filterung durchgeführt wird, wenn der
        performed when the current gegenwärtige Block eine Größe kleiner als
        block has a size of smaller than 32x32 aufweist.
        32 x 32.


Die Klägerin stützt ihre Klage auf die Nichtigkeitsgründe der mangelnden
Patentfähigkeit mit Blick auf fehlende Neuheit und fehlende erfinderische Tätigkeit
sowie der unzulässigen Erweiterung.


Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:


NK A                    Kopie der Verletzungsklage (teilgeschwärzt);
NK B                    International       Telecommunication     Union,   ITU-T,    H.265
                        (10/2014),      TELECOMMUNICATION           STANDARDIZATION
                        SECTOR       OF      ITU,   SERIES   H:    AUDIOVISUAL        AND
                        MULTIMEDIA           SYSTEMS,    Infrastructure    of   audiovisual

                                -9-



           services – Coding of moving video, High efficiency video
           coding, Recommendation ITU-T H.265;
NK C       Schriftsatz der Klägerin vom 7. November 2022 an das
           Landgericht M … I (21 O 4141/21);
NK I       Europäische Patentschrift des Streitpatents;
NK I-DE    Kopie der deutschen Übersetzung der Streitpatentschrift;
NK II      Auszug des Patent- und Gebrauchsmusterregisters des
           DPMA vom 14. Oktober 2021;
NK III     Merkmalsanalyse des Patentanspruchs 1;
NK IV      EP 2 723 078 A2;
NK IV-KR   WO 2012/177053 A2;
NK V       Prioritätsdokumente und englische Übersetzungen:
NK V1      Englische     Übersetzung       des   Prioritätsdokuments     KR
           20110059850;
NK V1-KR   Prioritätsdokument KR 20110059850;
NK V2      Englische     Übersetzung       des   Prioritätsdokuments     KR
           20110065708;
NK V2-KR   Prioritätsdokument KR 20110065708;
NK V3-KR   Prioritätsdokument     KR   20110119214        mit    Maschinenübersetzung;
NK V4-KR   Prioritätsdokument     KR   20110125353        mit    Maschinenübersetzung;


NK 1       KAZUO SUGIMOTO ET AL., „LUT-based adaptive filtering on
           intra   prediction   samples“    (JCTVC-D109),       4.   JCT-VC-MEETING vom 20. Januar 2011 bis 28. Januar 2011;
NK 2       MARTIN WINKEN ET AL., „Description of video coding
           technology proposal by Fraunhofer HHI“, 1. JCT-VC-MEETING vom 15. April 2010 bis 23. April 2010;

                                    - 10 -



NK 3            YUNFEI ZHENG ET AL., „CE13: Mode Dependent Hybrid
                Intra Smoothing“ (JCTVC-D282), 4. JCT-VC-MEETING vom
                20. Januar 2011 bis 28. Januar 2011;
NK 4            TUNG NGUYEN ET AL., „Improved intra smoothing for UDI
                and new AIS fast mode“ (JCTVC-C302), 3. JCT-VC-MEETING vom 7. Oktober 2010 bis 15. Oktober 2010;
NK 5            KEN MCCANN ET AL., „Samsung’s Response to the Call for
                Proposals on Video Compression Technology“ (JCTVC-A124), 1. JCT-VC-MEETING vom 15. April 2010 bis 23. April
                2010;
NK 6            E. ALSHIN ET AL., „Block-size and pixel position independent
                boundary smoothing for non-directional Intra prediction“
                (JCTVC-F252), 6. JCT-VC-MEETING vom 14. Juli 2011 bis
                22. Juli 2011;
NK 7            englische Übersetzung der koreanischen Patentanmeldung
                KR 20110026079;
NK 7-KR         KR 20110026079;
NK 7-KR DE-ÜS   deutsche Übersetzung der koreanischen Patentanmeldung
                KR 20110026079;
NK 8            EP 2 557 797 A2;
NK 8a           International     Telecommunication        Union,   ITU-T,    H.264
                (03/2010),      TELECOMMUNICATION            STANDARDIZATION
                SECTOR       OF    ITU,      SERIES   H:    AUDIOVISUAL        AND
                MULTIMEDIA         SYSTEMS,      Infrastructure     of   audiovisual
                services – Coding of moving video, Advanced video coding for
                generic audiovisual services, Recommendation ITU-T H.264;
NK 9            EP 2 665 274 A1;
NK 9a           Übersetzung der japanischen Patentanmeldung 2011-004038
                ins Englische mit „VERIFICATION OF TRANSLATION“ von
                Hatsune Hamada vom 7. Juli 2017;
NK 9b           Synopse NK 9 – NK 9a;

                                          - 11 -



NK 10                 JINHO LEE ET AL. „Mode dependent filtering for intra
                      predicted sample“ (JCTVC-F358), 6. JCT-VC-MEETING vom
                      14. Juli 2011 bis 22. Juli 2011;
NK 11                 KAZUO SUGIMOTO ET AL., „CE6.f: LUT-based adaptive
                      filtering on intra prediction samples” (JCTVC-E069), 5.
                      JCT-VC-MEETING vom 16. März 2011 bis 23. März 2011;
NK 12                 Anlage zum Bescheid des Europäischen Patentamts vom
                      5. August 2016;
NK 13                 THOMAS WIEGAND ET AL., „WD3: Working Draft 3 of High-Efficiency    Video    Coding”     (JCTVC-E603),   5.   JCT-VC-MEETING vom 16. März 2011 bis 23. März 2011.


Die Klägerin stellt den Antrag,
             das europäische Patent EP 2 723 078 mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
             nichtig zu erklären.


Die Beklagte stellt zuletzt den Antrag,
             die Klage abzuweisen
             hilfsweise
             das europäische Patent EP 2 723 078 unter Klageabweisung im
             Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik
             Deutschland insoweit für nichtig zu erklären, als es über die Fassung
             -   des Hauptantrags a vom 6. Juli 2023,
             -   des Hilfsantrags I vom 15. März 2022,
             -   des Hilfsantrags I a vom 6. Juli 2023,
             -   des Hilfsantrags II vom 16. Mai 2022,
             -   des Hilfsantrags II a vom 6. Juli 2023,
             -   des Hilfsantrags III vom 16. Mai 2022,
             -   des Hilfsantrags III a vom 6. Juli 2023,
             -   des Hilfsantrags IV vom 15. März 2022,

                                         - 12 -



               -   des Hilfsantrags IV a vom 6. Juli 2023,
               -   des Hilfsantrags V vom 17. April 2023,
               -   des Hilfsantrags V a vom 6. Juli 2023,
               -   des Hilfsantrags VI vom 17. April 2023,
               -   des Hilfsantrags VI a vom 6. Juli 2023,
               -   des Hilfsantrags VII vom 17. April 2023 und
               -   des Hilfsantrags VII a vom 6. Juli 2023
               – in dieser Reihenfolge – hinausgeht.


Die Beklagte erklärt in der mündlichen Verhandlung vom 6. Juli 2023, dass sie die
Patentansprüche gemäß Haupt- und Hilfsanträgen als jeweils geschlossene
Anspruchssätze ansieht, die jeweils insgesamt beansprucht werden.


Die Beklagte, die das Streitpatent mit einem Hauptantrag und hilfsweise beschränkt
mit dem Hauptantrag a und 14 Hilfsanträgen verteidigt, tritt der Argumentation der
Klägerin in allen wesentlichen Punkten entgegen und erachtet den Gegenstand des
Streitpatents für patentfähig. Die beanspruchte Lehre sei jedenfalls in der Fassung
des Hauptantrags a oder zumindest in einer der Fassungen der Hilfsanträge
patentfähig.


Die Klägerin rügt in der mündlichen Verhandlung vom 6. Juli 2023 den
Hauptantrag a und die Hilfsanträge I a bis VII a jeweils vom 6. Juli 2023 als verspätet
und beantragt eine Vertagung der mündlichen Verhandlung.


Gegenüber dem Hauptantrag ist in Patentanspruch 1 in den Hauptantrag a vom
6. Juli 2023 der Beklagten nach den Worten „using a plurality of different filters“
(Merkmal 2.2.1) eingefügt worden
           „for said filtering“


und nach den Worten „and 1/4 of a value of the upper reference pixel“ (Merkmal
8.3) eingefügt worden

                                       - 13 -



          „wherein the at least one other mode uses a filter different from the first,
          second and third filter“.


Patentanspruch 1 nach Hilfsantrag I vom 15. März 2022 unterscheidet sich von dem
erteilten Patentanspruch 1 dadurch, dass nach Merkmal 8.3 das Merkmal
9         „wherein when the determined intra prediction mode of the current block
          is the DC mode the filtering is only performed when the current block has
          a size of smaller than 32 x 32“
angehängt wird (die Merkmalsbezeichnungen aller neuen Merkmale der
Patentansprüche 1 der Hilfsanträge sind vom Senat festgelegt worden).


Hilfsantrag I a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag I vom
15. März 2022 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Gegenüber dem erteilten Patentanspruch 1 werden bei Patentanspruch 1 nach
Hilfsantrag II vom 16. Mai 2022 nach Merkmal 8.3 die beiden Merkmale
10        „wherein whether to perform the filtering depends on the intra prediction
          mode and the size of the prediction block,”
11        „and a filter type for the filtering depends on the intra prediction mode”
angehängt.


Hilfsantrag II a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag II vom
16. Mai 2022 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Patentanspruch 1 nach Hilfsantrag III vom 16. Mai 2022 unterscheidet sich von
Patentanspruch 1 nach Hilfsantrag II vom 16. Mai 2022 dadurch, dass auf die
Merkmale 10 und 11 das Merkmal 9 des Hilfsantrags I vom 15. März 2022 folgt.


Hilfsantrag III a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag III vom
16. Mai 2022 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.

                                         - 14 -



Patentanspruch 1 nach Hilfsantrag IV vom 15. März 2022 geht aus dem erteilten
Patentanspruch 1 hervor, indem nach Merkmal 8.3 das Merkmal
12        „wherein performing the filtering includes adding an offset value and
          applying the arithmetic right-shift operator”
hinzugefügt wird.


Hilfsantrag IV a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag IV vom
15. März 2022 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Patentanspruch 1 nach Hilfsantrag V vom 17. April 2023 unterscheidet sich von
Patentanspruch 1 nach Hilfsantrag I vom 15. März 2022 dadurch, dass nach dem
Merkmal 9 das Merkmal
13        „wherein the number of different intra prediction modes that the current
          block may have is a predetermined fixed value that does not change
          according to a size of the prediction block”
angefügt wird.


Hilfsantrag V a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag V vom
17. April 2023 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Der Patentanspruch 1 nach Hilfsantrag VI vom 17. April 2023 unterscheidet sich
von dem erteilten Patentanspruch 1 dadurch, dass auf Merkmal 8.3 die Merkmale
14.1      „applying the first filter is performed by
          (i) adding a value of the left reference pixel, the prediction value multiplied
          by a value of 2, a value of the upper reference pixel, and a value of 2 to
          generate a first result, and
          (ii) shifting the bits of the first result two positions to the right using an
          arithmetic right shift operator,”


14.2      „applying the second filter is performed by

                                         - 15 -



           (i) adding a value of the left reference pixel, the prediction value multiplied
           by a value of 3, and a value of 2 to generate a second result, and
           (ii) shifting the bits of the second result two positions to the right using an
           arithmetic right shift operator,”


14.3       „applying the third filter is performed by
           (i) adding a value of the upper reference pixel, the prediction value
           multiplied by a value of 3, and a value of 2 to generate a third result, and
           (ii) shifting the bits of the third result two positions to the right using an
           arithmetic right shift operator”
folgen.


Hilfsantrag VI a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag VI vom 17. April
2023 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Patentanspruch 1 nach Hilfsantrag VII vom 17. April 2023 kombiniert die Merkmale
des erteilten Patentanspruchs 1 mit den Merkmalen 9, 13 und 14.


Hilfsantrag VII a vom 6. Juli 2023 weist gegenüber dem Hilfsantrag VII vom 17. April
2023 dieselben Einfügungen auf wie der Hauptantrag a vom 6. Juli 2023.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                           Entscheidungsgründe


Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG i. V. m. Art. 138 Abs. 1 lit. a) EPÜ, Art. 52,
54 und 56 EPÜ sowie der Nichtigkeitsgrund der unzulässigen Erweiterung nach
Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜG i. V. m.       Art. 138 Abs. 1 lit. c) EPÜ und
Art. 123 Abs. 2 EPÜ geltend gemacht werden, ist zulässig.

                                       - 16 -




Die Klage ist auch begründet, weil das Streitpatent wegen fehlender Patentfähigkeit
für nichtig zu erklären und aus demselben Grund auch im Umfang des
Hauptantrags a und der Hilfsanträge nicht patentfähig ist.


Der Nichtigkeitsgrund der unzulässigen Erweiterung, der in Bezug auf den
Patentanspruch 1 in der erteilten Fassung sowie in den Fassungen der Hilfsanträge
I bis V geltend gemacht worden ist, kann unter diesen Umständen dahingestellt
bleiben.




                                         I.


1.   Der in der mündlichen Verhandlung am 6. Juli 2023 eingereichte
Hauptantrag a und die in der mündlichen Verhandlung am 6. Juli 2023 gestellten
Hilfsanträge I a bis VII a waren trotz Rüge der Klägerin nach § 83 Abs. 4
Satz 1 PatG nicht als verspätet zurückzuweisen.


Damit ist über die Verteidigung des Streitpatents nach dem Hauptantrag a und den
Hilfsanträgen I a bis VII a in der Sache zu entscheiden.


Gemäß § 83 Abs. 4 Satz 1 PatG kann das Patentgericht zwar eine Verteidigung des
Beklagten mit einer geänderten Fassung des Patents zurückweisen und bei seiner
Entscheidung unberücksichtigt lassen. Hierfür ist es aber stets erforderlich, dass
dieser Vortrag tatsächliche oder rechtliche Fragen aufkommen lässt, die in der
mündlichen Verhandlung nicht oder nur mit unverhältnismäßigem Aufwand zu klären
sind (vgl. Begründung zum Entwurf eines Gesetzes zur Vereinfachung und
Modernisierung des Patentrechts, BlPMZ 2009, 307, 315). Kann das an sich
verspätete Vorbringen dagegen noch ohne Weiteres in die mündliche Verhandlung
einbezogen werden, ohne dass es zu einer Verfahrensverzögerung kommt, liegen
die Voraussetzungen für eine Zurückweisung nach § 83 Abs. 4 PatG nicht vor (vgl.

                                       - 17 -



Keukenschrijver,   Patentnichtigkeitsverfahren,       7.   Aufl.   2021,    Rn.     223      mit
umfangreichen Nachweisen zur Rechtsprechung des BPatG in Fn. 125).


So liegt der Fall hier, weil die Berücksichtigung des Hauptantrags a und der
Hilfsanträge I a bis VII a zu keiner Verzögerung des Rechtsstreits geführt hat.


Hinzu tritt, dass nach der Rechtsprechung des Senats die Voraussetzungen für eine
Zurückweisung dann nicht vorliegen, wenn – wie hier – die geänderte
Anspruchsfassung     nicht   zur   Bestandsfähigkeit         des      Patents     führt    (vgl.
Keukenschrijver, a. a. O., Rn. 223 mit Nachweisen zur Rechtsprechung des BPatG
in Fn. 127).




2.    Der Antrag der Klägerin, die mündliche Verhandlung zu vertagen, ist
zurückzuweisen (§ 99 Abs. 1 PatG i. V. m. § 227 ZPO), weil die Berücksichtigung
des neuen Vortrags der Beklagten (Hauptantrag a und Hilfsanträge I a bis VII a)
eine Vertagung der mündlichen Verhandlung nicht erforderlich gemacht hat (§ 83
Abs. 4 Satz 1 Nr. 1 PatG).



                                         II.


1.     Die Lehre des Streitpatents liegt auf dem Gebiet der Bilddatenverarbeitung
und befasst sich mit dem Decodieren von Videos.


Gemäß der Beschreibungseinleitung der Streitpatentschrift hätten sich viele Nutzer
im Zuge der Verbreitung von Rundfunkdiensten mit hoher Bildauflösung an
hochauflösende Bilder gewöhnt. Mit zunehmendem Interesse an hochauflösendem
und   ultrahochauflösendem     Fernsehen        sei   eine     Nachfrage        nach      einer
Kompressionstechnologie      für    hochauflösende           Bilder     entstanden.        Zur
Bildkompression könnten Inter-Prädiktionsverfahren (d.h. die Vorhersage von
Pixelwerten eines aktuellen Bilds aus zeitlich davor oder danach kommenden

                                         - 18 -



Bildern), Intra-Prädiktionsverfahren (d.h. die Vorhersage von Pixelwerten eines
aktuellen Bilds unter Verwendung von Pixelinformationen dieses aktuellen Bilds)
und Entropiecodierverfahren (d.h. die Zuweisung kurzer Codes zu häufig
vorkommenden Symbolen und langer Codes zu seltenen Symbolen) verwendet
werden (Streitpatentschrift, Absätze [0002], [0003]).


Der Streitpatentschrift ist ferner zu entnehmen, dass ein Eingangsbild, welches
mittels eines Intra-Prädiktionsverfahrens codiert und decodiert werden soll, in
Blöcke („input blocks“) aufgeteilt wird, von denen Vorhersageblöcke („prediction
blocks“) subtrahiert werden, so dass sich Restblöcke („residuals“, „residual blocks“)
ergeben. Diese werden transformiert, quantisiert und entropiecodiert und in Form
eines Bitstroms an einen Decodierer übertragen (Streitpatentschrift, Absätze [0045]
bis [0051] i. V. m. Figur 1 sowie Absatz [0057]). Um das Eingangsbild zu
rekonstruieren, erzeugt der Decodierer zunächst rekonstruierte Restblöcke, indem
er die entropiecodierten Restblöcke entropiedecodiert, dequantisiert und invers
transformiert. Die Blöcke des rekonstruierten Eingangsbilds („reconstructed blocks“)
ergeben sich, indem zu jedem rekonstruierten Restblock ein Vorhersageblock
addiert wird (Streitpatentschrift, Absätze [0055] bis [0062] i. V. m. Figur 2).


Der Decodierer erzeugt diesen Vorhersageblock auf Basis von Informationen, die
in einem aktuellen zu decodierenden Bild („current picture“) enthalten sind. Dazu
greift er auf die Werte von Referenzpixeln zurück, d.h. von Pixeln bereits decodierter
Blöcke des aktuellen Bildes, die an einen aktuellen Block („current block“, in der
Streitpatentschrift    als    „gegenwärtiger      Block“     übersetzt)     angrenzen
(Streitpatentschrift, Absätze [0071], [0072], [0079] i. V. m. Figur 4B). Durch die Wahl
eines Intra-Vorhersagemodus kann dann festgelegt werden, wie sich die Pixelwerte
des Vorhersageblocks aus den Referenzpixelwerten ergeben. Ein Intra-Vorhersagemodus kann ein „direktionaler“ Modus sein, bei dem Referenzpixelwerte
aus benachbarten Blöcken in den Bereich eines Vorhersageblocks extrapoliert
werden, oder auch ein „nichtdirektionaler“ Modus wie etwa ein planarer Modus oder
ein DC-Modus (Streitpatentschrift, Absätze [0073] bis [0076]). Im DC-Modus werden

                                             - 19 -



alle   Pixelwerte    eines        Vorhersageblocks            auf   einen      Mittelwert    von
Referenzpixelwerten benachbarter Blöcke gesetzt (Streitpatentschrift, Absatz
[0151]).




2.     In der Einleitung des Streitpatents wird eine Aufgabe nicht ausdrücklich
angegeben.


Jedoch führt das Streitpatent aus, dass bei einer referenzpixelbasierten Intra-Vorhersage    Diskontinuitäten        zwischen        einem     Vorhersageblock       und    den
benachbarten Blöcken erzeugt werden können, wenn sich die Auswahl der
Referenzpixel mit dem Vorhersagemodus des jeweils aktuellen Blocks ändert. Bei
einer richtungsabhängigen Intra-Vorhersage etwa nähmen die Vorhersagefehler
der Pixel eines Vorhersageblocks - und damit die Diskontinuitäten - mit
zunehmendem Abstand von einem Referenzpixel zu (Streitpatentschrift, Absatz
[0082]).


Vor diesem Hintergrund schlägt das Streitpatent vor, Pixel eines Vorhersageblocks
zu filtern, indem zum Beispiel ein Bereich innerhalb eines Vorhersageblocks, der
einen großen Vorhersagefehler aufweist, basierend auf den Referenzpixeln adaptiv
gefiltert wird. Dies soll die Vorhersagefehler reduzieren und die Diskontinuitäten
minimieren, was wiederum die Codier- und Decodiereffizienz verbessert
(Streitpatentschrift, Absatz [0083]; s. ferner Absätze [0009] bis [0012] sowie [0269]).


Daraus      lässt    sich         insbesondere         die      Aufgabe        ableiten,    eine
Videodecodiervorrichtung bereitzustellen, die es ermöglicht, bei der Decodierung
von    Videobilddaten,      die    mittels   Intra-Vorhersage        codiert     worden     sind,
Diskontinuitäten zwischen einem Vorhersageblock und dessen benachbarten
Blöcken zu minimieren und dadurch die Decodiereffizienz zu verbessern.

                                         - 20 -



3.    Als zuständigen Durchschnittsfachmann, auf dessen Wissen und Können es
insbesondere für die Auslegung der Merkmale des Streitpatents und für die
Interpretation des Standes der Technik ankommt, sieht der Senat einen
Elektrotechnikingenieur         der     Fachrichtung        Datenverarbeitung          mit
Hochschulabschluss an, der über mehrjährige Berufserfahrung im Bereich der
digitalen Bildverarbeitung sowie der digitalen Videocodierung verfügt und mit den
gängigen Videocodierungsstandards vertraut ist.




4.    Mit     seinem   Patentanspruch       1     schlägt    das    Streitpatent      eine
Videodecodiervorrichtung vor, durch die die oben genannte Aufgabe gelöst wird.


4.1   Diese      Videodecodiervorrichtung         umfasst      (Merkmal      1)       zwei
Erzeugungseinheiten: eine Vorhersageblock-Erzeugungseinheit zum Erzeugen
eines Vorhersageblocks durch Durchführen von Intra-Vorhersage auf einem
gegenwärtigen Block (Merkmale 2, 2.1) sowie eine Rekonstruierte-Blöcke-Erzeugungseinheit zum Erzeugen eines rekonstruierten Blocks basierend auf dem
Vorhersageblock und einem rekonstruierten Restblock, der dem gegenwärtigen
Block entspricht (Merkmal 3).


Für   den   Fachmann      ist   ein   gegenwärtiger    Block    („current   block“)    ein
zusammenhängender rechteckiger Bildbereich, der Teil einer zeitlichen Abfolge von
Blöcken ist und dessen Inhalt zu einem bestimmten Zeitpunkt von dem Decodierer
ermittelt werden soll. Eine solche zeitliche Abfolge beinhaltet im Allgemeinen sowohl
Blöcke, die vor dem gegenwärtigen Block der Erzeugung eines entsprechenden
rekonstruierten Blocks gedient haben (und ebenfalls gegenwärtige Blöcke gewesen
sind) als auch Blöcke, die nach dem gegenwärtigen Block zur Erzeugung eines
rekonstruierten Blocks verwendet werden.


Gemäß den Absätzen [0069] und [0085] der Streitpatentschrift kann ein
gegenwärtiger Block auch als „Decodierzielblock“ („decoding target block“)

                                         - 21 -



bezeichnet werden, welcher seinerseits als „Vorhersagezielblock“ („prediction target
block“) angesehen werden kann, wenn an dem Decodierzielblock eine Intra-Vorhersage durchgeführt wird (was hier der Fall ist, vgl. Merkmal 2.1). Die Begriffe
„Decodierzielblock“ und „Vorhersagezielblock“ bringen zum Ausdruck, dass die
Pixelwerte des gegenwärtigen Blocks durch ein Decodieren bzw. durch eine
Vorhersage ermittelt werden sollen.


Laut Absatz [0100] der Streitpatentschrift kann durch die Intra-Vorhersage an dem
Decodierzielblock   (d.h.   nach   dem     vorstehend   Gesagten    auch   an   dem
gegenwärtigen Block) ein Vorhersageblock erzeugt werden. Ein Vorhersageblock
ist ein zusammenhängender rechteckiger Bildbereich, der durch die Koordinaten
der in ihm enthaltenen Pixel definiert sein kann, der Vorhersage der Pixelwerte
eines zu rekonstruierenden Blocks dient und Pixelwerte enthalten kann, welche die
Pixelwerte des zu rekonstruierenden Blocks zumindest dann approximieren, wenn
die Vorhersage der Pixelwerte des Vorhersageblocks abgeschlossen ist. Daraus
folgt, dass ein anspruchsgemäßer gegenwärtiger Block als ein Bildbereich
angesehen werden kann, der bereits vor der Intra-Vorhersage vorgegeben ist und
dessen Pixelwerte erst durch die Intra-Vorhersage bestimmt werden sollen. Damit
kann ein gegenwärtiger Block die gleiche Größe wie ein Vorhersageblock besitzen
oder aber auch größer als ein Vorhersageblock sein. Die Größe eines
gegenwärtigen Blocks wird durch den erteilten Patentanspruch 1 allerdings nicht
festgelegt.


Diese Feststellungen sind in Einklang mit Absatz [0072] der Streitpatentschrift, aus
dem hervorgeht, dass ein Vorhersageblock einer Codiereinheit („CU“) oder einer
Prädiktionseinheit („PU“) entspricht („The prediction block may correspond to at
least one of a coding unit (CU), a prediction unit (PU), […] the prediction block may
be a square block […]“). Denn in einer CU erkennt der Fachmann einen
gegenwärtigen Block und in einer PU einen Vorhersageblock, der zur Intra-Vorhersage eingesetzt werden und mit einer CU zusammenfallen oder zusammen
mit anderen PUs Bestandteil einer CU sein kann (vgl. NK 5, Abschnitt 2.2.2 - „the

                                        - 22 -



PU is defined only für the last-depth CU and its size is limited to that of the CU […]
we define two different terms to specify the prediction method: the prediction type
and the PU splitting. The prediction type is one of the values among skip, intra or
inter […] Figure 2-4 shows possible PU splittings … The PU for intra has 2 different
possible splittings: 2Nx2N (i.e. no split) and NxN (quarter split)“). Dies gilt
insbesondere für den in Patentanspruch 1 genannten Vorhersageblock.


4.2    Merkmal 2.2 definiert die Vorhersageblock-Erzeugungseinheit dadurch
näher, dass das Erzeugen eines Vorhersageblocks (vgl. Merkmal 2) durch
Durchführen von Filterung auf einem Filterungszielpixel in dem Vorhersageblock
erfolgen soll.


Diese Angabe erscheint auf den ersten Blick widersprüchlich, da der
Vorhersageblock offensichtlich einerseits gemäß Merkmal 2 Ergebnis des
Erzeugens sein soll, aber andererseits gemäß Merkmal 2.2 die Filterung - und damit
das Erzeugen - von „dem“ in Merkmal 2 genannten Vorhersageblock ausgeht. Im
zweiten Fall wäre das Vorhandensein des Vorhersageblocks eine Voraussetzung
für die Filterung, aber gerade nicht deren Ergebnis.


Da der Fachmann generell bestrebt ist, Patenten einen sinnvollen Gehalt zu
entnehmen (vgl. BGH, X ZR 95/05, Urteil vom 31. März 2009, Rn. 16 m. w. N., juris
und GRUR 2009, 653 - Straßenbaumaschine), wird er die Angabe „Filterung auf
einem Filterungszielpixel in dem Vorhersageblock“ in Merkmal 2.2 im Sinne von
„Ermittlung eines gefilterten Werts eines Pixels, das in dem in Merkmal 2
angesprochenen     Vorhersageblock     liegt und/oder ein Vorhersagepixel ist“
verstehen, wobei die Filterung von dem Vorhersageblock - einem Bildbereich -
ausgeht. Nach dieser Lesart betrifft das in Merkmal 2 angesprochene Erzeugen des
Vorhersageblocks die Ermittlung der Pixelwerte des Vorhersageblocks unter
Einsatz der in den Merkmalen 2.1 und 2.2 genannten Maßnahmen, wobei die
Pixelwerte als optionale Bestandteile des Vorhersageblocks verstanden werden

                                           - 23 -



können (s.o., Abschnitt II.4.1). Damit ergibt sich eine widerspruchsfreie
Interpretation der Merkmale 2 bis 2.2.


4.3    Gemäß der Merkmalsgruppe 2.2/2.2.1 soll das Durchführen der Filterung auf
dem Filterungszielpixel in dem Vorhersageblock unter Verwendung einer Mehrzahl
von unterschiedlichen Filtern „für eine Mehrzahl von unterschiedlichen Intra-Vorhersagemodi des gegenwärtigen Blocks“ erfolgen.


Diese Angabe bedeutet aus fachmännischer Sicht, dass eine Filterung auf einem
Filterungszielpixel eines jeweiligen gegenwärtigen Blocks in mindestens zwei Intra-Vorhersagemodi vorgesehen ist. Eine solche Filterung kann z.B. durch Anwendung
eines oder mehrerer 2-Tap- oder 3-Tap-Filter realisiert werden (vgl. Merkmale 8.1
bis 8.3).


Eine breitere Auslegung des Merkmals 2.2.1 hält der Senat nicht für angemessen.
Zwar könnte Merkmal 2.2.1 („unter Verwendung […] von […] Filtern für […] Intra-Vorhersagemodi“) grundsätzlich als unmittelbar auf Merkmal 2.1 („Durchführen von
Intra-Vorhersage“) rückbezogen verstanden werden, und sich damit auf beliebige
Filter beziehen, die bei einer Intra-Vorhersage eingesetzt werden - d.h. auch auf
Filter, mit denen Referenzpixel gefiltert werden. Gegen diese Interpretation spricht
hier aber insbesondere, dass das Merkmal 2.1 in der hier maßgeblichen englischen
Fassung des Patentanspruchs 1 sprachlich durch ein Komma von den Merkmalen
2.2 und 2.2.1 abgesetzt ist, sowie auch die deutliche sprachliche und inhaltliche
Nähe der beiden letztgenannten Merkmale (Merkmal 2.2 - „[…] by performing
filtering […]“; Merkmal 2.2.1 - „using a plurality of different filters […]“).


4.4    Merkmal 2.2.2 bringt zum Ausdruck, dass die Intra-Vorhersagemodi einen
DC-Modus und wenigstens einen von diesem verschiedenen Modus enthalten.


Gemäß Merkmal 2.2.3 soll das Durchführen einer Intra-Vorhersage das Bestimmen
eines Intra-Vorhersagemodus für den gegenwärtigen Block enthalten. Das

                                         - 24 -



bedeutet, dass diesem Block ein Intra-Vorhersagemodus zugeordnet ist.


Dass der rekonstruierte Restblock dem gegenwärtigen Block „entspricht“ (vgl.
Merkmal 3), ist insbesondere dann erfüllt, wenn die Bildbereiche des rekonstruierten
Restblocks    in   einer   bestimmten    Beziehung     zu   den   Bildbereichen    des
gegenwärtigen Blocks stehen.


4.5    Die Merkmale 4, 5, 6.1, 6.2 und 6.3 enthalten jeweils die Vorbedingung „wenn
der bestimmte Intra-Vorhersagemodus des gegenwärtigen Blocks ein/der DC-Modus ist“. Da sich die Merkmale 5.1 sowie 7.1 bis 8.3 über die in ihnen
verwendeten Begriffe eindeutig auf eines der Merkmale 4, 5, 6.1, 6.2 oder 6.3
rückbeziehen, betreffen die Merkmale 4 bis 8.3 ausschließlich die Filterung in einem
DC-Modus.


4.5.1 Gemäß Merkmal 4 soll das Filterungszielpixel ein Vorhersagepixel
(„prediction pixel“) auf einer linken vertikalen und/oder auf einer oberen horizontalen
Vorhersagepixellinie sein („on […] a […] prediction pixel line“). Eine solche
Vorhersagepixellinie definiert einen Bereich innerhalb des Vorhersageblocks,
dessen Pixelwerte mit den Werten zugehöriger Referenzpixel nur schwach
korrelieren, daher einen großen Vorhersagefehler aufweisen können und sich
deshalb für eine Filterung anbieten (vgl. Streitpatent, Absatz [0151] i. V. m. Absatz
[0083]).


Über die Breite der Vorhersagepixellinien macht der Patentanspruch 1 keine
Aussage; die Merkmale 6.1 bis 8.3 schließen den Fall von Vorhersagepixellinien,
die mehr als ein Pixel breit sind, nicht per se aus.


Mit den Ausdrücken „an einer ganz linken Seite des Vorhersageblocks“ bzw. „an
einer obersten Seite des Vorhersageblocks“ („at a leftmost side“/“at an uppermost
side“) in Merkmal 4 wird insbesondere verdeutlicht, dass der Vorhersageblock keine
Vorhersagepixellinien enthält, die weiter links oder weiter oben als die in Merkmal 4

                                          - 25 -



genannten Vorhersagepixellinien angeordnet sind (vgl. Streitpatentschrift, Figur 13,
Bezugszeichen 1310 i. V. m. Absätzen [0150], [0151]).


4.5.2 Mit Merkmal 5 wird zum Ausdruck gebracht, dass im DC-Modus für eine
Mehrzahl von Blockgrößen eines gegenwärtigen Blocks dieselbe Filterform,
dieselben Filtertaps und dieselben Filterkoeffizienten zur Filterung verwendet
werden. Ein Filtertap ist aus Sicht des Fachmanns insbesondere die in einem Filter
enthaltene Information, dass ein bestimmter Wert eines diskreten Signals (hier: ein
bestimmter Pixelwert) bei einer Faltungsoperation mit einem Filterkoeffizienten
gewichtet werden soll. Eine Filterform kann durch eine Menge verschiedener
Filtertaps definiert sein, die sich auf bestimmte Pixelwerte beziehen.


Dass die Mehrzahl von Blockgrößen „4x4, 8x8 und 16x16 enthält“ (vgl. Merkmal
5.1), impliziert in Verbindung mit den Merkmalen 5 sowie 6.1 bis 8.3, dass für
gegenwärtige Blöcke der Größe 4x4, 8x8 und 16x16 dieselbe Filterform, dieselben
Filtertaps und dieselben Filterkoeffizienten verwendet werden, wobei sich diese
Filtervariablen insbesondere aus den Merkmalen 6.1 bis 8.3 ergeben. Merkmal 5.1
beschränkt die Filterung nicht auf Blöcke, die die oben genannten Größen
aufweisen.


4.5.3 Die Merkmale 6.1 bis 8.3 lehren zum einen, dass im DC-Modus in
Abhängigkeit von der Position des Filterungszielpixels im Vorhersageblock drei
verschiedene Filter angewendet werden, und zum anderen, wie diese drei Filter
definiert sind.


a)     Im Zusammenhang mit der Position des Filterungszielpixels geben die
Merkmale 6.2 und 6.3 an, dass dieses „an“ einer Vorhersagepixellinie angeordnet
ist („filtering target pixel is positioned at the […] prediction pixel line“). Das bedeutet
in Verbindung mit Merkmal 4 („prediction pixel on […] a […] prediction pixel line“),
dass das Filterungszielpixel auf der Vorhersagepixellinie liegt.

                                        - 26 -



Merkmal 6.1 enthält die weitere Positionsangabe „an einer ganz linken oberen Seite
des Vorhersageblocks“ („at a leftmost upper side of the prediction block“). Im
Hinblick darauf zeigt Absatz [0174] i. V. m. Figur 16a der Streitpatentschrift ein
Ausführungsbeispiel für den Fall genau ein Pixel breiter Vorhersagepixellinien: dort
ist ein Pixel, das „at the leftmost upper portion in the prediction block“ angeordnet
ist, das (einzige) Pixel, das die Koordinaten (0,0) besitzt und in der linken oberen
Ecke des Vorhersageblocks liegt. Der Fachmann wird die durch Merkmal 6.1
beschriebene Anordnung des Filterungszielpixels - ähnlich wie die Angaben in den
Merkmalen 6.2 und 6.3 in Verbindung mit Merkmal 4 - derart verstehen, dass das
Filterungszielpixel sowohl auf der linken vertikalen Vorhersagepixellinie als auch auf
der oberen horizontalen Vorhersagepixellinie liegt.


Somit wird der erste Filter auf ein Filterungszielpixel angewendet, das auf beiden
Vorhersagepixellinien liegt, wohingegen der zweite und dritte Filter jeweils auf ein
Filterungszielpixel angewendet wird, das sich nur auf einer der beiden Linien
befindet.


b)    Die Filterung mit den drei Filtern soll jeweils auf einem in dem DC-Modus
erzeugten Vorhersagewert sowie auf Werten von rekonstruierten Referenzpixeln
beruhen, die links bzw. oberhalb von dem Filterungszielpixel angeordnet sind. Unter
einem rekonstruierten Referenzpixel versteht das Streitpatent ein Pixel eines bereits
rekonstruierten Blocks, der an den gegenwärtigen Block angrenzt (vgl.
Streitpatentschrift, z.B. Absätze [0071], [0072], [0079] sowie Figuren 4A und 4B).


c)    Die Merkmale 8.1 bis 8.3 legen jeweils konkrete Gewichtungsfaktoren fest,
mit denen der Vorhersagewert und die Werte der rekonstruierten Referenzpixel bei
der Filterung gewichtet werden.


d)    Somit entspricht die vorstehend unter II. 4.5.3 a) bis c) beschriebene Lehre
der Filterdefinition des unter dem Bezugszeichen 1610 in Figur 16A i. V. m. den
Absätzen [0172] bis [0176] dargestellten Ausführungsbeispiels.

                                       - 27 -



                                         III.


Das Streitpatent hat in der erteilten Fassung keinen Bestand, weil der Gegenstand
seines Patentanspruchs 1 nicht patentfähig ist.




1.    Der Gegenstand des erteilten Patentanspruchs 1 beruht gegenüber der aus
der Druckschrift NK 11 bekannten Lehre nicht auf einer erfinderischen Tätigkeit.


1.1   So schlägt die NK 11 ein adaptives Filterungsverfahren für Intra-Prädiktionssamples vor, welches auf einer Lookup-Tabelle basiert und die in der auf
Seite 7 angegebenen Referenz [2] (= NK 1) beschriebene Vorgehensweise
vereinfachen soll (vgl. Abstract und Abschnitt 1, jeweils erster Satz). Das Verfahren
geht von „HM-2.0“ aus (Abschnitt 3, erster Satz); hinter dieser Abkürzung verbirgt
sich aus Sicht des Fachmanns ein „HEVC Test Model 2.0“ - d.h. eine Referenz-Software, die im Rahmen der Entwicklung des „High Efficiency Video Coding“-
Standards für Tests vorgesehen ist. Laut Abschnitt 3 der NK 11 wurde das
vorgeschlagene Verfahren im Rahmen von Simulationen unter Verwendung
derjenigen gängigen Testkonfigurationen ausgeführt, auf die Referenz [3] der
NK 11 Bezug nimmt.


In Abschnitt 8.3.3.1.7 der NK 11 („Filtering process of DC prediction samples“) wird
eine im DC-Modus durchgeführte Filterung von Vorhersagepixeln beschrieben.
Eingabeparameter für diese Filterung sind die Größe nS eines Vorhersageblocks,
die Referenzpixelwerte p[ x, y ] benachbarter Blöcke sowie Vorhersagewerte
predSamples[ x, y ], ausgegeben werden gefilterte Vorhersagepixelwerte
predSamplesF[ x, y ] (vgl. NK 11, Seite 9, Punkt 3. sowie Seite 11 unten). Falls es
sich um 8x8-Blöcke handelt (d.h. falls nS gleich 8 ist), kommen die Filtergleichungen
(6-x5) bis (6-x8) zur Anwendung, da davon auszugehen ist, dass die zur Auswahl
der Filtergleichungen verwendete Größe DCFilterType[nS] in diesem Fall gemäß
der auf Seite 12 oben abgebildeten und auf Seite 11 unten als „Table 6-xx -

                                        - 28 -



Specification of DCFilterType[ nS ] for various prediction unit sizes“ bezeichneten
Tabelle den Wert 2 besitzt. Analog dazu werden bei 4x4- und 16x16-Blöcken (mit
nS = 4 und DCFilterType[4] = 3 bzw. nS = 16 und DCFilterType[16] = 1) die
Filtergleichungen (6-x9) bis (6-x12) bzw. (6-x1) bis (6-x4) herangezogen.


Der Fachmann identifiziert die in den Gleichungen (6-x1) bis (6-x4), (6-x5) bis (6-
x8) und (6-x9) bis (6-x12) enthaltenen Filtervorschriften ohne weiteres mit den in
den Figuren 1 bis 3 der NK 11 illustrierten Filterungen mit den Filtern #C, #B und
#A. Das bedeutet, dass im DC-Modus Vorhersageblöcke der Größe 4x4, 8x8 bzw.
16x16 mit dem Filter #A, #B bzw. #C gefiltert werden.


Dies ist auch in Übereinstimmung mit der in Figur 6 oben gezeigten Lookup-Tabelle,
die für das in NK 11 vorgeschlagene Verfahren („Proposed scheme“) festlegt, für
welche Vorhersageblockgrößen und Intra-Vorhersagemodi welcher Filter eingesetzt
wird (vgl. Bildunterschrift zu Figur 6 - „LUT for each intra prediction unit size and
intra prediction mode“). Der Fachmann wird davon ausgehen, dass die insgesamt
40 Spalten der Lookup-Tabelle gemäß den Werten einer Variablen angeordnet sind,
die die Intra-Vorhersagemodi mit dem Wert 0 beginnend bis zum Wert 39
durchnummeriert. Da dem DC-Modus üblicherweise der Wert 2 zugeordnet ist (vgl.
dazu auch Tabelle 6-1 auf Seite 9 der NK 11), entnimmt er auch der in Figur 6 oben
gezeigten Tabelle, dass im DC-Modus die Filter #A, #B bzw. #C zur Filterung von
Vorhersageblöcken der Größe 4x4, 8x8 bzw. 16x16 herangezogen werden.


Gemäß Figur 6 wird in mehreren vom DC-Modus verschiedenen Intra-Vorhersagemodi eine Filterung auf Referenzpixelwerten mit einem Filter „1“
vorgenommen, der durch die Gleichungen (6-3) bis (6-7) repräsentiert ist. Dies
ergibt sich aus einer Zusammenschau der oberen Tabelle der Figur 6 und der auf
Seite 10 gezeigten Tabelle. NK 11 stellt zudem Ergebnisse vor, die auf einer
Übertragung der Filterung im DC-Modus in den planaren Modus beruhen (vgl. Text
unter Tabelle 1; Figur 7; Tabelle 3).

                                          - 29 -



1.2    Der NK 11 ist ferner zu entnehmen, dass das dort beschriebene
Filterungsverfahren eine Videocodierung und -decodierung auf Basis der Filter #A,
#B und #C umfasst, da in der Tabelle 1 auf Seite 4 - diese betrifft die
Implementierung des in NK 11 vorgeschlagenen Verfahrens - auf relative Codierund Decodierzeitangaben („Enc Time“, „Dec Time“) Bezug genommen wird, die im
Rahmen von rechnergestützten Tests ermittelt worden sind. Dem Fachmann ist klar,
dass die Angaben „Class A“, „Class B“ etc. in Tabelle 1 der NK 11 Testvideos
bezeichnen, die mit dem dort vorgeschlagenen Verfahren verarbeitet worden sind.


Somit lässt die Druckschrift NK 11 unmittelbar auf einen Rechner - d.h. eine
Videodecodiervorrichtung       gemäß      Merkmal      1   -    schließen,    die    eine
Erzeugungseinheit für einen aus den Pixeln [x, y] mit Pixelwerten „predSamples[ x,
y ]“ bestehenden Vorhersageblock durch Durchführen einer Intra-Vorhersage auf
einem gegenwärtigen Block gemäß den Merkmalen 2 und 2.1 (vgl. Formeln auf
Seite 12 i. V. m. dem ersten Satz in Abschnitt 2 - „The tested scheme applies filtering
only on most upper and left edge samples of DC prediction […] where only left and
upper most pixel lines of the prediction samples are filtered“) und durch Durchführen
von Filterung auf einem Filterungszielpixel [x, y] in dem Vorhersageblock gemäß
Merkmal 2.2 enthält (vgl. Gleichungen auf Seite 12). Die Intra-Vorhersagemodi
umfassen den DC-Modus, dem die zweite Spalte der Tabelle entspricht (s.o.,
Merkmal 2.2.2). Da davon auszugehen ist, dass abhängig vom Bilddateninhalt eines
Eingangsblocks eines Testvideos verschiedene Intra-Vorhersagemodi verwendet
werden, muss der für einen aktuell zu rekonstruierenden Block verwendete Modus
bestimmt werden; eine solche Bestimmung ist im Übrigen auch aus der in Abschnitt
8.3.3.1, Seite 9, Punkt 3 angegebenen Aussage „If intra PredMode is equal to 2“
ableitbar (Merkmal 2.2.3).


Gemäß den Bildunterschriften der Figuren 2 und 3 („filter coefficients for DC
prediction edges except the top-left corner sample“, „filter coefficients for the top-left
corner sample in DC prediction samples“) i. V. m. Figur 1 befindet sich ein Pixel,
das gemäß einer der oben genannten Filtergleichungen zu filtern ist, auf einer ganz

                                        - 30 -



links   und/oder       ganz   oben      im       Vorhersagezielblock       angeordneten
Vorhersagepixellinie. Dies lässt sich auch unmittelbar aus den Filtergleichungen
ersehen, die nur dann den Wert eines Vorhersagewerts predSamples[ x, y ]
verändern,      wenn   mindestens    einer   der   Indizes   x   und   y    des   Arrays
PredSamplesF[ x, y ] gleich Null ist.


Damit verwirklicht die Lehre der NK 11 auch das Merkmal 4.


Ferner setzt sich der Filter #B aus drei einzelnen Filtern zusammen. Der erste dieser
Filter wird durch die Gleichung (6-x5) beschrieben und ist in der Mitte der Figur 3
gezeigt. Er wird auf ein Filterungszielpixel in der linken oberen Ecke des
Vorhersageblocks angewendet und gewichtet den zugehörigen Vorhersagewert
predSamples[ 0, 0 ] mit dem Faktor 1/2 und die Werte p[ -1, 0 ] und p[ 0, -1 ] des
linken und oberen benachbarten Referenzpixels jeweils mit einem Faktor 1/4
(Merkmale 6.1 und 8.1). Ferner wird der durch die Gleichung (6-x7) beschriebene
und in der Mitte der Figur 2 gezeigte zweite Filter auf Pixel angewendet, die sich auf
einer im Vorhersageblock ganz links angeordneten Vorhersagepixellinie befinden,
nicht aber in der linken oberen Ecke des Vorhersageblocks. Dieser Filter gewichtet
den Vorhersagewert predSamples[ 0, y ] eines solchen Pixels mit dem Faktor 3/4
und den Wert p[ -1, y ] des links neben diesem Pixel liegenden Referenzpixels mit
dem Faktor 1/4 (Merkmale 6.2 und 8.2). Schließlich wird der durch die Gleichung
(6-x6) beschriebene und ebenfalls in der Mitte der Figur 2 gezeigte dritte Filter auf
Pixel angewendet, das sich auf einer im Vorhersageblock ganz oben angeordneten
Vorhersagepixellinie befindet, und ebenfalls nicht in der linken oberen Ecke des
Vorhersageblocks. Dieser Filter gewichtet den Vorhersagewert predSamples[ x, 0 ]
eines derartigen Pixels mit dem Faktor 3/4 und den Wert p[ x, -1] des unmittelbar
oberhalb dieses Pixels angeordneten Referenzpixels mit dem Faktor 1/4 (Merkmale
6.3 und 8.3).


Dass das obere und linke benachbarte Referenzpixel jeweils ein rekonstruiertes
Referenzpixel oberhalb des bzw. links von dem jeweils gefilterten Pixel ist, ergibt

                                        - 31 -



sich aus dem ersten Satz in Abschnitt 8.3.3.1 auf Seite 8 („The nS*4+1 neighboring
samples p[ x, y ] that are constructed luma samples prior to the deblocking filter
process“) in Verbindung mit Punkt 3 auf Seite 9 („filtering process of DC prediction
samples specified in 8.3.3.1.7 is invoked with the sample array p and the DC
prediction samples as the inputs […]“ sowie den Gleichungen (6-x1) bis (6-x3),
(6-x5) bis (6-x7) und (6-x9) bis (6-x11), in denen die Variable p - wie oben ausgeführt
- einen Referenzpixelwert bezeichnet.


Damit gehen auch die Merkmale 7.1 und 7.2 aus NK 11 hervor.


Allerdings sind der NK 11 die Merkmale 2.2.1 und 3 sowie die Merkmalsgruppe
5/5.1 nicht unmittelbar zu entnehmen.


1.3    Mit den verbleibenden Merkmalen 2.2.1, 3, 5 und 5.1 kann eine erfinderische
Tätigkeit nicht begründet werden.


1.3.1 So gelangt der Fachmann ausgehend von NK 11 unter Berücksichtigung des
aus NK 1 Vorbekannten auf naheliegende Weise zu Merkmal 2.2.1.


a)     Die Druckschrift NK 1 ist - ähnlich wie die Druckschrift NK 11 - ein
Standardisierungsbeitrag, der sich mit der Filterung von Vohersagepixeln befasst
(vgl. z.B. Titel und Abstract).


Der Fachmann wird die NK 1 bereits deshalb berücksichtigen, weil sie in NK 11 als
Referenz [2] zitiert und darüber hinaus im Zuge der Treffen des „Joint Collaborative
Team on Video Coding (JCT-VC)“ auch von demselben Autorenteam veröffentlicht
worden ist, auf das die NK 11 zurückgeht (vgl. Schulte/Moufang, PatG mit EPÜ,
11. Aufl. 2022, § 4 Rn. 22 Fall d)).


b)     Die NK 1 weist den Fachmann ausdrücklich darauf hin, dass zur Erhöhung
der Codiereffizienz auch in anderen Intra-Vorhersagemodi als dem DC-Modus

                                          - 32 -



Filterungszielpixel gefiltert werden können (vgl. NK 1, Abschnitt 1 - „[…] the
advantage in terms of coding efficiency using filtering on intra prediction samples
compared to intra reference sample smoothing […] using various filters depending
on the prediction unit size and the intra prediction mode of the coded block provide
better coding efficiency compared to only one filter […]“ i. V. m. Tabelle 1, in der in
den direktionalen Intra-Vorhersagemodi 3 bis 33 ein anderer Filter („Filter #3“)
eingesetzt wird als im DC-Modus („mode 2“), bei dem auf den „Filter #0“
zurückgegriffen wird); Entsprechendes geht auch aus NK 3 hervor (Abschnitt 1,
erster Absatz, letzter Satz i. V. m. dem Text auf Seite 2 sowie Tabelle 2-1). Dabei
bringt die Formulierung „using various filters“ in der oben zitierten Textstelle aus
NK 1 insbesondere zum Ausdruck, dass sich die in den anderen Vorhersagemodi
verwendeten Filter von den im DC-Modus verwendeten Filtern unterscheiden
können.


Der Fachmann hätte daher zur weiteren Verbesserung der Codiereffizienz
selbstverständlich auch eine Filterung der Vorhersagepixelwerte in einem anderen
als dem DC-Modus in Betracht gezogen und dabei insbesondere in einem
direktionalen Intra-Vorhersagemodus - wie in NK 1 gezeigt - einen Filter eingesetzt,
der sich von den Filtern #A, #B und #C unterscheidet.


1.3.2 Das Merkmal 3 geht nicht über eine fachübliche Vorgehensweise bei der
Intra-Prädiktion hinaus (s. z.B. NK 8, Absatz [0031], letzter Satz; NK 6c, Abschnitt
8.3.3, Punkt 4. vor Abschnitt 8.3.3.1).


1.3.3 Auch die restlichen Merkmale 5 und 5.1 können vor dem Hintergrund der aus
den jeweiligen Entgegenhaltungen NK 11 und NK 1 bekannten Lehre eine
erfinderische Tätigkeit nicht begründen.


a)     Die Druckschriften NK 11 und NK 1 stellen einzelne Beiträge zur
verbesserten Gestaltung der Filterung von Vorhersageblöcken dar, die im Rahmen
der Entwicklung eines standardisierten Videocodierverfahrens durch das „Joint

                                           - 33 -



Collaborative Team in Video Coding“ (JCT-VC) vorgelegt worden sind (vgl. jeweils
den ersten Satz des Abstracts der beiden Druckschriften).


Die Qualität eines solchen Videocodierverfahrens hängt immer von einer Vielzahl
von Kriterien ab (z.B. von der erreichbaren Codiereffizienz, der zu erzielenden
Bitrate, der gerade noch akzeptablen Verzerrung der Bildinhalte, der Komplexität
der Implementierung; vgl. auch NK 1, deren Abschnitt 4 auf den „Tradeoff“ zwischen
Bitrate und Verzerrung Bezug nimmt), welche der Fachmann gegeneinander
abwägt, bevor er sich für eine bestimmte Implementierung entscheidet. Daher ist es
aus fachlicher Sicht selbstverständlich, dass ein Standardisierungsbeitrag wie NK 1
oder NK 11 zwar aufgrund der in ihm auf Basis einer speziellen Filterwahl
erhaltenen Testergebnisse einen guten Ausgangspunkt für eine                    weitere
Entwicklung der Filterung von Vorhersageblöcken bietet, aber keinesfalls einen
Endpunkt einer Entwicklung darstellt, die zu einem in jeder Hinsicht „optimalen“
Filter geführt hat.


Dies wird auch dadurch bestätigt, dass sich weitere Veröffentlichungen im
Verfahren    befinden,   die   ebenfalls     auf    eine   verbesserte   Filterung   von
Vorhersageblöcken abzielen und nach der NK 11 angemeldet bzw. publiziert
worden sind (vgl. NK 6a/NK 6b/NK 6c, NK 8 sowie NK 10).


b)     In dieser technischen Ausgangslage hat der Fachmann mehrere Gründe,
den Weg der Erfindung zu beschreiten.


aa)    So findet er im ersten Absatz von Abschnitt 1 der NK 1 einen Hinweis darauf,
eigene Tests zur Optimierung der Filterung von Vorhersageblöcken durchzuführen.
Dort ist es nämlich im Hinblick auf eine mögliche Erhöhung der Codiereffizienz ganz
allgemein als vorteilhaft beschrieben, Vorhersagepixel anstelle von Referenzpixeln
zu filtern. Eine konkrete Anregung, dabei insbesondere die Filterung im DC-Modus
in den Blick zu nehmen, erhält der Fachmann aus Abschnitt 3 der NK 11. Dort wird
ausdrücklich hervorgehoben, dass die in Tabelle 1 gezeigten Resultate auf die

                                        - 34 -



Filterung im DC-Modus zurückzuführen sind (vgl. Seite 6, Text vor Tabelle 4 - „This
confirms that overall coding gain reported in Table 1 comes from the part of DC
prediction filtering“). Da aus fachmännischer Perspektive weder die NK 11 noch die
NK 1 einen Endpunkt der Filterentwicklung darstellen (s.o.), wird der Fachmann
daraus den Schluss ziehen, dass weitere Verbesserungen der Lehre der NK 11 am
erfolgversprechendsten sind, wenn sie an der Filterung von Vorhersagepixeln im
DC-Modus ansetzen.


Zudem weist die NK 11 in Abschnitt 1 darauf hin, dass die in ihr beschriebene
Filterung von Vorhersagepixeln eine Vereinfachung der in NK 1 beschriebenen
Filterung sei. Der Fachmann, der generell nach Vereinfachungen des Standes der
Technik Ausschau hält (vgl. Schulte/Moufang, a. a. O., § 4 Rn. 155), nimmt sich dies
zum Anlass, insbesondere auch nach Möglichkeiten zu suchen, wie die Lehre der
NK 11 ohne allzu große Performance-Einbußen vereinfacht werden kann.


bb)   Des Weiteren wird        der Fachmann das in NK 11                  beschriebene
Filterungsverfahren nacharbeiten und dazu auf seinem Rechner implementieren.
Denn so kann er zum einen testen, ob die in NK 11 veröffentlichten Testergebnisse
korrekt sind und die dort beschriebene Filterung für seine eigenen Testvideos
vergleichbare   Resultate    liefert,   und      zum   anderen   liegen    ihm   dann
Referenzergebnisse vor, von denen ausgehend er weitere algorithmische
Verbesserungen und/oder Vereinfachungen (s.o., Abschnitt III.1.3.3 b) aa))
vornehmen kann.


Bei der erstmaligen Implementierung eines neuen Berechnungsverfahrens ist es
aber selbstverständlich, dass der Fachmann die zugehörigen Verfahrensparameter
nicht „blind“ übernimmt, sondern die dabei relevanten Variablen systematisch
variiert, um deren Auswirkungen auf die Güte des Berechnungsverfahrens
quantitativ beurteilen zu können und so ein „Gefühl“ für diese Variablen zu
bekommen.

                                       - 35 -



Im vorliegenden Fall bedeutet das, dass der Fachmann im Rahmen der
Implementierung der Lehre der NK 11 nicht nur den Einfluss der Filterung im DC-Modus mit der Filterfolge „A – B – C“ für 4x4-, 8x8- und 16x16-Blöcke ermittelt,
sondern darüber hinaus Testrechnungen durchführt, anhand derer er sich ein
genaues Bild über das Verhalten der Filter #A, #B und #C im Zusammenspiel mit
Parametern machen kann, die für die Filterung im DC-Modus relevant sind. So kann
er   insbesondere    einschätzen,   welche      quantitativen   Verbesserungen   der
Codiereffizienz zu erwarten sind, wenn er ausgehend von den Filtern #A, #B und
#C die Filterung der Vorhersagepixelwerte weiter optimieren würde.


c)     Da Filterungen von Vorhersageblöcken der Größen 32x32 und 64x64 in
NK 11 nicht angesprochen werden und sich die in NK 1 beschriebenen Tests
ausdrücklich auf Blöcke der Größe 4x4, 8x8 und 16x16 beschränken (vgl.
Abschnitt 2 - „The proposed filtering scheme on intra prediction samples is applied
up to 16x16 PU size […]“ i. V. m. den Tabellen 1 und 2), hatte der Fachmann
hinreichende Veranlassung, auch nur die letztgenannten Blockgrößen bei
Testrechnungen zu verwenden.


d)     Um einen Überblick über das Verhalten der einzelnen Filter #A, #B bzw. #C
zu gewinnen, geht der Fachmann systematisch vor und testet daher zunächst
Filterfolgen, bei denen ausschließlich derselbe Filter über verschiedene Blöcke der
Größe 4x4, 8x8 und 16x16 hinweg filtert. Denn ansonsten wären die Einflüsse
verschiedener Filter auf die Ergebnisse vermischt und schwer voneinander zu
trennen. Da es mit den Filtern #A, #B und #C pro Blockgröße (4x4, 8x8 oder 16x16)
drei Filter gibt, die für jede dieser Größen entweder angewendet werden können
oder nicht, bedeutet das, dass der Fachmann zunächst nicht mehr als 3 • 23 = 24
Filterfolgen ausprobiert hätte.


Hierbei bieten sich insbesondere Testreihen an, bei denen die Filterfolge „A – B – C“
(= Filter #A für 4x4-Blöcke, Filter #B für 8x8-Blöcke und Filter #C für 16x16-Blöcke)
durch die Filterfolgen „A – A – A“/„B – B – B“/„C – C – C“ und „0 – 0 – 0“/„B – 0 –

                                         - 36 -



0“/„B – B – 0“/„B – B – B“ ersetzt wird (die Filterbezeichnung „0“ soll bedeuten, dass
für eine bestimmte Blockgröße keine Filterung vorgenommen wird). Denn mit der
ersten Testreihe lässt sich der Einfluss der unterschiedlichen Filter auf die
Codiereffizienz sehr gut quantitativ beurteilen, und mit der zweiten Testreihe der
Einfluss der maximalen Blockgröße, bis zu der hin die Durchführung einer Filterung
sinnvoll ist. Die Testreihe „0 – 0 – 0“/„B – 0 – 0“/„B – B – 0“/„B – B – B“ ist gegenüber
den Testreihen „0 – 0 – 0“/„A – 0 – 0“/„A – A – 0“/„A – A – A“ und „0 – 0 – 0“/„C – 0
– 0“/„C – C – 0“/„C – C – C“ dadurch ausgezeichnet, dass der Filter #B die aus den
Filtern #A, #B und #C bestehende Gruppe am besten repräsentiert, da seine
Filterkoeffizienten zwischen denen der Filter #A und #C liegen.


Da die oben genannten Testreihen mit dem Filter #B jeweils eine Testrechnung mit
der Filterfolge „B – B – B“ enthalten, ergeben sich somit auch die restlichen
Merkmale 5 und 5.1 auf naheliegende Weise.


e)     Dies gilt auch deshalb, weil die Testreihen als Teil einer überschaubaren
Menge von Routineversuchen angesehen werden können, die der Fachmann in der
Praxis bereits ohne Schwierigkeiten zu seiner Orientierung durchführen würde,
bevor er sich über Verbesserungen Gedanken macht, sowie zum Schließen eigener
Wissenslücken im Hinblick auf das Verhalten der Filter #A, #B und #C (vgl.
Schulte/Moufang, a. a. O., § 4 Rn. 51; Busse/Keukenschrijver, PatG, 9. Aufl. 2020,
§ 4 Rn. 83; Benkard/Asendorf/Schmidt/Tochtermann, PatG, 12. Aufl. 2023, § 4
Rn. 100).
Im Übrigen stellt sich in der oben beschriebenen technischen Ausgangslage der
Einsatz der Filterung mit der Filterfolge „B – B – B“ im Rahmen der Testreihen aus
Sicht des Fachmanns insbesondere deshalb als vorteilhaft dar, weil eine solche
Filterung - im Gegensatz zu einer Filterung mit den Filtern #A und #C -
ausschließlich zwei Bit-Shift-Operationen erfordert (vgl. Gleichungen (6-x2), (6-x3),
(6-x6), (6-x7), (6-x10), (6-x11)) und auch in programmiertechnischer Hinsicht eine
Vereinfachung darstellt.

                                        - 37 -




2.     Die in diesem Zusammenhang von der Beklagten vorgebrachten Argumente
können zu keiner anderen Beurteilung führen.


2.1    Die Beklagte wendet sinngemäß ein, die NK 11 lehre entsprechend der
Figur 4 lediglich, Referenzpixel außerhalb des Vorhersageblocks zu filtern.
Außerdem zeige NK 11 bereits die optimale Filterwahl; dies würde der Fachmann
nicht in Frage stellen. Auch gebe es im Stand der Technik keine Lösung, bei der
derselbe Filter bei unterschiedlichen Blockgrößen verwendet werde. Der Fachmann
hätte auch keinen konkreten Anlass gehabt, die im eingesetzten Filter
weiterzuentwickeln     oder    in    Bezug       auf   die   Makroblockgröße      eine
Komplexitätsreduktion anzustreben. Zudem fehle ein Anlass, der Filterung andere
Videos zugrundezulegen als diejenigen, die die Standardisierungsgruppe bei der
Entwicklung des Standards im Rahmen von Testmodellen verwende. Ein Hinweis
auf ein allgemeines Interesse des Fachmanns an einer Verbesserung reiche -
insbesondere im Lichte des BGH-Urteils X ZR 89/15 vom 16. Januar 2018, juris -
nicht aus, um einen Anlass zu begründen.


Diese Argumente erweisen sich jedoch nicht als stichhaltig.


a)     So beschreibt NK 11 ausdrücklich, dass Pixel eines Vorhersageblocks im
Rahmen von Testrechnungen gefiltert werden (vgl. Abstract, erster Satz - „In this
contribution, a test result on LUT-based adaptive filtering on intra prediction samples
defined in Core Experiment 6.f is reported“; Abschnitt 1, erster Satz - „A simplified
version of intra prediction samples filtering proposed in [2] is tested in CE6.f“;
Abschnitt 2, erster Satz - „The tested scheme applies filtering only on most upper
and left edge samples of DC prediction as shown in Figure 1“). Ferner ist der
Druckschrift NK 11 zu entnehmen, dass diese Testrechnungen ein Schema
(„proposed scheme“) betreffen, welches von den Autoren der NK 11 vorgeschlagen
und in Abschnitt 2 und der Bildunterschrift von Figur 4 angesprochen wird (vgl.
Abschnitt 4 - „According to the test results, the proposed scheme achieves […]“

                                        - 38 -



sowie Abschnitt 1 - „[…] is tested in CE6.f. The proposed scheme applies […]“; s.
ferner Abschnitt 2 - „The LUT for the proposed scheme and MDIS are shown in
Figure 6“ - in Verbindung mit Figur 6, deren obere Tabelle insbesondere eine
Filterung von Pixeln im DC-Modus mit den Filtern #A, ‚#B und #C zeigt).


Somit erläutert die Bildunterschrift „Reference samples to be filtered in the proposed
scheme“ der Figur 4 der NK 11 in Verbindung mit Abschnitt 2 („In our proposed
scheme, […] filtering is applied for intra smoothing as shown in Figure 4“) lediglich,
wie Referenzpixel bei den Testrechnungen gefiltert werden. Jedoch kann aus Figur
4 nicht abgeleitet werden, dass sich diese Testrechnungen ausschließlich auf eine
Filterung von Referenzpixeln beschränken.


b)    Ferner hatte der Fachmann - wie oben in Abschnitt III.1.3.3 ausgeführt -
durchaus Veranlassung, im DC-Modus eine Filterfolge auszuprobieren, die sich von
der aus NK 11 bekannten Filterfolge „A – B – C“ unterscheidet. Damit führt auch der
Hinweis der Beklagten nicht weiter, ein Verweis auf ein allgemeines Interesse an
einer Verbesserung genüge nicht. Abgesehen davon unterscheidet sich der in der
BGH-Entscheidung X ZR 89/15 diskutierte Sachverhalt, bei dem es um die
Übertragung einer Möglichkeit zur Änderung eines Betriebssystems von einem
stationären PC auf ein Mobiltelefon geht, grundlegend von der vorliegenden
Problematik.


Dass der Fachmann die Vorgaben der NK 11 ungeprüft übernimmt, mag allenfalls
in seltenen Fällen angebracht sein, in denen ihm nicht viel Zeit für Tests bleibt.
Jedoch ist es der Normallfall, dass sich der Fachmann auf die Lektüre des
Standardisierungsbeitrags NK 11 hin ein eigenes Bild über das Verhalten der Filter
#A, #B und #C macht und dazu entsprechende Parameter variiert, aus denen sich
dieses Filterverhalten ableiten lässt - insbesondere, wenn er im Zusammenhang mit
der    Filterung   von     Vorhersagepixeln      im    DC-Modus       eine    weitere
Komplexitätsreduktion oder eine sonstige Verbesserung anstrebt. Dies wird gerade
auch durch den Umstand belegt, dass die Autoren der NK 10 in Kenntnis der NK 11

                                         - 39 -



- die NK 11 ist in NK 10 als Referenz [1] zitiert - eine der Filterfolge „B - B - B“
entsprechende Filterfolge vorschlagen (vgl. NK 10, Figur 2 i. V. m. Abschnitt 2.1 -
„In this contribution, single filter described in Figure 2 is proposed rather than three
types of filter“; Abschnitt 3 - „The proposals are applied to 4x4~16x16 block sizes“)
und es somit nicht bei der ungeprüften Übernahme der Filterfolge „A – B – C“
bewenden lassen.


Auch der Hinweis im zweiten Absatz von Abschnitt 1 der NK 1, verschiedenartige
Filter     könnten     abhängig      vom      Intra-Vorhersagemodus         und     der
Vorhersageblockgröße verwendet werden, schließt per se nicht aus, dass im DC-Modus derselbe Filter für Blöcke der Größe 4x4, 8x8 und 16x16 verwendet wird,
solange in einem anderen Intravorhersagemodus für diese Blockgrößen
mindestens ein anderer Filter verwendet wird.


c)       Weiterhin ist die Annahme unrealistisch, dass der Fachmann auf dem Gebiet
der Videocodierung seine Entwicklungen nur auf Basis der Ressourcen durchführt,
die von einer Standardisierungsgruppe verwendet werden. Vielmehr hat ein solcher
Fachmann üblicherweise seine eigene Entwicklungsumgebung, in denen er seine
eigenen Codier- und Decodieralgorithmen mit Hilfe eigener Testbilddaten optimiert.
Daher hat er durchaus ein begründetes Interesse, nachzuprüfen, welche
Ergebnisse die Filterwahl der NK 11 in seiner Entwicklungsumgebung liefert.


d)       Im Übrigen war es durchaus auch am ersten Prioritätstag bekannt, dass in
einem Intra-Vorhersagemodus derselbe Filter für verschiedene Blockgrößen
verwendet werden kann (im DC-Modus: vgl. NK 3, Tabelle 2-2; in weiteren Modi:
vgl. NK9/NK9a, Figuren 13 und 20).


2.2      Nach Auffassung der Beklagten sei mit der Implementierung der Filterfolge
„B – B – B“ auch keine angemessene Erfolgserwartung oder große
Erfolgswahrscheinlichkeit    verbunden,    wie    sie   vom   Bundesgerichtshof     zur
Begründung eines Naheliegens gefordert werde; die Beklagte verweist in diesem

                                      - 40 -



Zusammenhang auf das BGH-Urteil X ZR 82/20 vom 21. Juli 2022 („Leuchtdiode“,
juris und GRUR 2023, 39) sowie auf weitere Entscheidungen aus den Gebieten der
Pharmazie und Chemie. Denn wie die in NK 10 beschriebenen Rechnungen
zeigten, gehe die Komplexitätsreduktion, zu der die Implementierung der Filterfolge
„B – B – B“ führe, überraschenderweise nicht zulasten der Codiereffizienz. Der
Fachmann würde somit keine identischen Filter für Blöcke der Größe 4x4, 8x8 und
16x16 vorsehen, weil er in diesem Fall mit einer Verringerung der Codiereffizienz
rechne.


Auch diese Ausführungen überzeugen nicht.


a)    So ist zunächst festzuhalten, dass die von der Beklagten zitierten
Entscheidungen das Aufwachsen von Halbleiterschichten betreffen oder auf
pharmazeutischem oder chemischem Gebiet liegen. In diesen Gebieten stellt sich
der gewünschte Erfolg - das Aufwachsen einer Materialschicht oder die Herstellung
einer Substanz mit gewünschten Eigenschaften -             erst nach zahlreichen
langwierigen, aufwendigen und teuren Versuchen ein. Hingegen geht es im
vorliegenden Fall um die Verwendung der Filterfolge „B – B – B“ in einer Testreihe,
d.h. um eine fachübliche Maßnahme, die sich in wenigen Minuten mittels
Abänderung weniger Programmzeilen umsetzen lässt, sich durch einfache, auf eine
überschaubare Anzahl von Möglichkeiten gerichtete Überlegungen ergibt und dazu
dient, dem Fachmann im Hinblick auf bestimmte Qualitätskriterien und
Testergebnisse eine quantitative Information über das Filterverhalten zu geben.
Eine solche Maßnahme hat bereits dann „Erfolg“, wenn dem Fachmann durch seine
Testreihen quantitative Resultate an die Hand gegeben werden, aus denen er
Schlüsse für die Gestaltung der Filterung ziehen kann. Nachdem die Durchführung
von Testrechnungen zur Routinetätigkeit des Fachmanns gehört und solche
Testrechnungen üblicherweise verwertbare Ergebnisse liefern, ist es bereits alles
andere als überraschend, dass diese Rechnungen in dem vorstehenden Sinne
hinreichend „erfolgreich“ sind.

                                       - 41 -



b)     Im Übrigen entnimmt der Fachmann der in diesem Zusammenhang
relevanten Tabelle 2 der NK 10 (vgl. Überschrift „Table 2 : Performance of
proposal 1 (Single filter for DC predicted samples)“ i. V. m. Abschnitt 2.1 sowie den
ersten beiden Sätzen von Abschnitt 1) allenfalls mit Sicherheit, dass sich die
Ersetzung der Filterfolge „A – B – C“ durch die Filterfolge „B – B – B“ in sehr
geringem Maße auf die Bitrate auswirkt. Zwar deuten die wenigen Tabelleneinträge
mit dem Wert „-0.1“ auf eine Bitratenreduktion hin; jedoch haben die meisten
Einträge den (gerundeten) Wert „0.0“, so dass sich aus der Tabelle 2 sowohl eine
Erhöhung als auch eine Verringerung der Bitrate bzw. der Codiereffizienz ableiten
lässt. Damit ist aus Sicht des Fachmanns der NK 10 bereits der von der Beklagten
postulierte Effekt der Erhöhung der Codiereffizienz nicht eindeutig zu entnehmen.


Dass die Ersetzung der Filterfolge relativ geringe Auswirkungen auf die Bitrate hat,
ist - ebenso wie das Vorzeichen dieser Auswirkungen - aus fachlicher Sicht nicht
weiter überraschend, weil sich die Wirkung der Filter #A und #C in der Filterfolge „A
– B – C“ teilweise kompensiert, die Filter #A, #B und #C maximal drei Pixelwerte
mitteln sowie dieselben Filtertaps und relativ ähnliche Filterkoeffizienten besitzen
(vgl. die Figuren 2 und 3 der NK 11). Der Fachmann wird daher darauf aus sein,
quantitative (ungerundete!) Ergebnisse zu erhalten, um belastbare Aussagen zur
Größe und dem Vorzeichen der Bitratenänderung zu bekommen, die infolge der
Ersetzung der Filterfolge „A – B – C“ durch andere Filterfolgen - wie etwa die Folge
„B – B – B“ - zu erwarten ist.


2.2.3 Die Beklagte ist ferner der Ansicht, ein Fachmann, der das in NK 11
vorgeschlagene Schema weiterentwickeln wollte, könne sehr viele Möglichkeiten
erwägen (z.B. die Verwendung anderer Filter, die Verwendung von Filtern für
Blockgrößen von 32x32 und 64x64, keine Filterung für 4x4-Blöcke). Auch aus
diesem Grund bestehe kein hinreichend konkreter Anlass, genau diejenige
Versuchsreihe durchzuführen, die zur Filterkombination „B – B – B“ führt.
Insbesondere sei nicht ersichtlich, warum der Fachmann zur Ermittlung des
Einflusses der Blockgröße auf die Codiereffizienz Versuche mit unterschiedlichen

                                             - 42 -



Filtern - etwa den Filterfolgen „A - A - A“, „B – B – B“ und „C – C – C“ - durchführen
würde.


Auch dieser Einwand vermag nicht zu überzeugen.


a)     Der Fachmann wird bei seinen ersten Tests alle drei Filter #A, #B und #C
berücksichtigen, weil er a priori nicht weiß, welcher dieser Filter welche quantitativen
Ergebnisse liefert.


b)     Auch wenn der Fachmann ausgehend von NK 11 an die Implementierung
anderer Filter als der Filter #A, #B und #C denken sollte, benötigt er hierfür
sowohl wohldefinierte Referenzrechnungen, anhand derer er den Einfluss dieser
anderen Filter beurteilen kann, als auch ein „Gefühl“ dafür, welche Veränderungen
der Filter #A, #B und #C überhaupt sinnvoll sind. Beides liefern die oben in
Abschnitt III.1.3.3 d)   angesprochenen          Testreihen.     Diese   sind   Teil   einer
überschaubaren Menge von Testmöglichkeiten, welche insbesondere auch den von
der Beklagten angesprochenen Test ohne Filterung von 4x4-Blöcken umfassen.


c)     Selbst wenn der Fachmann über die oben beschriebenen Testreihen hinaus
zusätzliche Tests durchführen würde, bei denen auch 32x32- und 64x64-Blöcke
gefiltert werden, bliebe die Merkmalsgruppe 5/5.1 verwirklicht. Denn der erteilte
Patentanspruch 1 beschränkt die Filterung nicht auf Blöcke der Größe 4x4, 8x8 und
16x16 (s.o., Abschnitt II.4.5.2).


2.2.4 Nach     Auffassung        der      Beklagten    spricht   zudem    der   technische
Zusammenhang          zwischen      der     Größe     des   Vorhersageblocks     und    der
Wahrnehmbarkeit der durch die Vorhersage erzeugten Artefakte gegen das
Naheliegen der Merkmalsgruppe 5.


Auch mit diesem Argument vermag die Beklagte nicht durchzudringen.

                                              - 43 -



So werden zwar gemäß der Filterfolge „A – B – C“ die auf die Referenzpixel
angewendeten Filterkoeffizienten mit zunehmender Blockgröße größer (1/8 – 2/8 –
3/8 - vgl. NK 11, Figuren 2 und 3). Daraus folgt aber noch nicht, dass der Fachmann
keinerlei Testrechnungen mit Filtern durchführt, die diese Eigenschaft nicht
aufweisen. So wird etwa bei den in NK 1 gezeigten Testrechnungen gerade
umgekehrt wie in NK 11 verfahren - dort ist im DC-Modus („mode 2“) der Beitrag
der Referenzpixel für 16x16-Blöcke am geringsten (vgl. NK 1, Figur 2, Tabelle 2),
und bei dem aus NK 3 bekannten Verfahren wird für unterschiedliche Blockgrößen
ein und derselbe Filter verwendet (vgl. dort Tabelle 2-2 für den „Mode 2“).


2.2.5 Schließlich macht die Beklagte geltend, die Druckschriften NK 1 und NK 11
zeigten,     dass     der   Fachmann     danach        strebe,    Filterungen   in   anderen
Vorhersagemodi als dem DC-Modus wegzulassen, so dass er dort keine
zusätzlichen     Filterungen      einführen     würde.    Ein     solches   Vorgehen    (vgl.
Merkmal 2.2.1) würde vielmehr die Komplexität erhöhen, was der Einführung der
komplexitätsreduzierenden Filterkombination „B – B – B“ diametral zuwiderlaufe.


Auch dieses Argument überzeugt nicht.


a)      Denn - wie oben bereits ausgeführt (vgl. Abschnitt III.1.3.1) - findet der
Fachmann in der NK 1 eine Anregung, das Merkmal 2.2.1 zu realisieren.


b)      Zudem berichtet gerade auch die NK 11 von Ergebnissen, die mit dem dort
vorgeschlagenen Filterungsschema in einem - vom DC-Modus verschiedenen -
planaren Vorhersagemodus erhalten worden sind (Abschnitt 3, Seite 4 letzter
Absatz; Figur 7; Tabelle 3; Abschnitt 4, zweiter Absatz).


c)      Ferner impliziert das Argument der Beklagten, dass ein Fachmann, der die
Komplexität eines Videocodierverfahrens reduzieren möchte, ausschließlich in
diese      Richtung    arbeitet   und    gleichzeitig     keine     komplexitätserhöhenden

                                        - 44 -



Maßnahmen vornimmt, auch wenn diese das Codierverfahren an anderer Stelle
deutlich verbessern. Dies ist aber vorliegend nicht der Fall.


Auch die Entscheidung für einen Filter in einem zusätzlichen Vorhersagemodus
beruht immer auf einer Abwägung zwischen den Nachteilen einer Komplexitäts- und
Verzerrungserhöhung und dem Vorteil einer Bitratenreduktion für das gesamte
Codierverfahren. Dies wird gerade auch anhand von NK 1 deutlich. So bezieht sich
das Abstract der NK 1 hauptsächlich auf ein Verfahren, bei dem auch in anderen
Intra-Vorhersagemodi als dem DC-Modus gefiltert wird (vgl. Tabelle 1). Lediglich
am Ende des Abstracts wird eine vereinfachte Version erwähnt, bei der nur im DC-Modus gefiltert wird (vgl. Tabelle 2). Die vereinfachte Version liefert im Hinblick auf
die Bitratenreduktion naturgemäß schlechtere Resultate (vgl. Tabelle 4 mit
Tabelle 3; s. ferner Abschnitt 4). Am Ende von Abschnitt 4 wird festgestellt, dass die
vereinfachte Version hinsichtlich des „Tradeoffs“ zwischen Bitrate und Verzerrung
vorzuziehen sein könnte („might be preferable“). An dieser letztgenannten
Formulierung wird die Abwägung des Fachmanns zwischen den Qualitätskriterien
Komplexität, Bitrate und Verzerrung deutlich. Allein mit einer solchen Abwägung
von Vor- und Nachteilen kann keine erfinderische Tätigkeit begründet werden (vgl.
BGH, Urteil vom 3. Mai 2006, X ZR 24/03, Rn. 34 - Mikrotom, juris und GRUR 2006,
930). Daran ändert auch der Umstand nichts, dass die NK 11 eine Vereinfachung
der Lehre der NK 1 betrifft.


Wäre der Fachmann ausschließlich an einer Komplexitätsreduktion interessiert,
würde er die Vorhersageblöcke auch im DC-Modus nicht filtern. Dies widerspricht
aber sowohl der Lehre der NK 1 als auch der NK 11. Auch die streitpatentgemäße
Erfindung beruht darauf, dass im DC-Modus und darüber hinaus auch noch in
wenigstens einem weiteren Modus Intra-Vorhersageblöcke gefiltert werden (s.o.,
Abschnitt II.4.3).

                                            - 45 -



3.     Somit hat der Patentanspruch 1 des Streitpatents keinen Bestand. In der
erteilten Fassung ist das Streitpatent daher für nichtig zu erklären.




                                             IV.


Auch der Hauptantrag a und die Hilfsanträge I bis VII sowie I a bis VII a bleiben
ohne Erfolg. Der Nichtigkeitsgrund der mangelnden Patentfähigkeit besteht für den
Patentanspruch 1 in den Fassungen aller dieser Anträge unverändert fort.


1.     Dem Hauptantrag a kann nicht stattgegeben werden, weil der Gegenstand
seines Patentanspruchs 1 im Lichte der kombinierten Lehren der Druckschriften
NK 11 und NK 1 nicht auf einer erfinderischen Tätigkeit beruht.


1.1    Patentanspruch 1 nach Hauptantrag a unterscheidet sich von dem erteilten
Patentanspruch 1 dadurch, dass Merkmal 2.2.1 durch das Merkmal


2.2.1a „using a plurality of different filters for said filtering for a plurality of different
         intra prediction modes of the current block, respectively,”


ersetzt und nach Merkmal 8.3 das Merkmal


8.4      „wherein the at least one other mode uses a filter different from the first,
         second and third filter”


angehängt wird (die zu Merkmal 2.2.1a führende Änderung wurde hier durch eine
Unterstreichung kenntlich gemacht).


1.2    Die Einfügung „for said filtering“ in Merkmal 2.2.1a bringt klar zum Ausdruck,
dass die Mehrzahl von unterschiedlichen Filtern, die für eine Mehrzahl von
unterschiedlichen Intra-Vorhersagemodi verwendet werden, die mit Merkmal 2.2

                                        - 46 -



beanspruchte Filterung auf einem Filterungszielpixel in dem Vorhersageblock
betreffen.   Diese    Änderung    beschränkt       den     Gegenstand     des   erteilten
Patentanspruchs 1 nicht (vgl. Abschnitt II.4.3).


Laut Merkmal 8.4 soll der in Merkmal 2.2.2 angesprochene mindestens eine andere
Intra-Vorhersagemodus einen Filter verwenden, der sich jeweils von dem in den
Merkmalen 6.1 bis 6.3 und 8.1 bis 8.3 genannten ersten, zweiten und dritten Filter
unterscheidet.   Da     der   Gegenstand         des     erteilten   Patentanspruchs    1
Ausführungsformen umfasst, bei denen in allen der in Merkmal 2.2.1 genannten
unterschiedlichen Intra-Vorhersagemodi dieselben Sätze unterschiedlicher Filter
verwendet     werden,    beschränkt     Merkmal        8.4     den    Gegenstand       des
Patentanspruchs 1 des Streitpatents.


1.3   Der Fachmann gelangt unter Berücksichtigung einer Kombination der
jeweiligen Lehren der Druckschriften NK 11 und NK 1 zum Gegenstand von
Patentanspruch 1 nach Hauptantrag a, ohne erfinderisch tätig zu werden.


So lehrt NK 1 ausdrücklich, dass in unterschiedlichen Intra-Vorhersagemodi
verschiedenartige Filter eingesetzt werden können (vgl. Abschnitt 1 - „[…] using
various filters depending on […] the intra prediction mode“). Das bedeutet
insbesondere, dass sich diejenigen Filter, die in einem anderen als dem DC-Modus
eingesetzt werden, von den im DC-Modus verwendeten Filtern unterscheiden
können. Dies geht auch aus Figur 1 und Tabelle 1 der NK 1 hervor: dort ist gezeigt,
dass die vom Filter #2 verschiedenen Filter #1 und #3 in den Modi 3, 6 und 9 bzw.
3 bis 33 eingesetzt werden.


Wie bereits ausgeführt (s.o., Abschnitt III.1.3.1), hätte der Fachmann mit diesem
Wissen selbstverständlich auch Vorhersagepixelwerte in einem anderen als dem
DC-Modus gefiltert, um die Codiereffizienz bei Bedarf weiter zu verbessern.

                                          - 47 -



Unter Zugrundelegung der Argumentation aus Abschnitt III.1.3.1 sind damit die
Merkmale 2.2.1a und 8.4 erfüllt.


1.4   Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 1 beruht
die Lehre des Patentanspruchs 1 gemäß Hauptantrag a somit nicht auf einer
erfinderischen    Tätigkeit   und   ist   daher    nicht   patentfähig.   Mit   seinem
Patentanspruch 1 fällt der gesamte Hauptantrag a.




2.    Der Hilfsantrag I kann nicht günstiger als der Hauptantrag beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls im Hinblick auf eine
Kombination der Lehren der Druckschriften NK 11 und NK 1 nicht auf einer
erfinderischen Tätigkeit beruht.


2.1   Der Patentanspruch 1 nach Hilfsantrag I unterscheidet sich vom erteilten
Patentanspruch 1 dadurch, dass nach Merkmal 8.3 das Merkmal


9       „wherein when the determined intra prediction mode of the current block is
        the DC mode the filtering is only performed when the current block has a
        size of smaller than 32 x 32.“


angehängt wird.


2.2   Merkmal 9 geht nicht wörtlich aus der Streitpatentschrift hervor. Es bedeutet
aus fachmännischer Sicht, dass ein gegenwärtiger Block im DC-Modus nur dann
gefiltert wird, wenn seine Größe geringer als 32x32 ist.


Dies ist in Übereinstimmung mit den in der Streitpatentschrift in der dritten Spalte
der Tabelle 8 enthaltenen Angaben zu den im Intra-Vorhersagemodus 2 (= dem DC-Modus) verwendeten Filtertypen, aus denen sich i. V. m. den Absätzen [0235],
[0238] und [0239] ergibt, dass im DC-Modus „nur“ Blöcke gefiltert werden, die

                                           - 48 -



kleiner als 32x32 sind (wenn darüber hinaus angenommen wird, dass größere
Blöcke als 64x64-Blöcke nicht codiert oder zumindest nicht gefiltert werden). Somit
ist Merkmal 9 insbesondere dann erfüllt, wenn eine zu Tabelle 8 der
Streitpatentschrift analoge Tabelle verwendet wird, aus der hervorgeht, dass
allenfalls Blöcke gefiltert werden sollen, die kleiner als 32x32 sind.


Zudem liegt Merkmal 9 bereits dann vor, wenn eine einzelne Testrechnung mit
Filterfolge „B – B – B“ im DC-Modus vorgenommen wird, bei der lediglich Blöcke
gefiltert werden, die kleiner als 32x32 sind (also mit Filterfolge „B – B – B – 0 – 0“,
wobei sich die drei Symbole „B“ auf eine Filterung von 4x4-, 8x8- und 16x16-Blöcken
beziehen und die beiden Nullen bedeuten, dass 32x32- und 64x64-Blöcke jeweils
nicht gefiltert werden) - unabhängig davon, ob noch andere Testrechnungen mit
anderen Filterfolgen durchgeführt werden.


2.3     Auch die Aufnahme von Merkmal 9 in den erteilten Patentanspruch 1 kann
keine erfinderische Tätigkeit begründen.


2.3.1 Denn wie oben bereits ausgeführt (vgl. Abschnitt III.1.3.3 c) bis III.1.3.3 e)),
hatte der Fachmann vor dem Hintergrund einer Kombination der jeweiligen Lehren
der Druckschriften NK 11 und NK 1 Veranlassung, Testreihen durchzuführen, bei
denen der Filter #B nur auf Blöcke der Größe 4x4, 8x8 und 16x16 angewendet wird.


2.3.2 Darüber     hinaus    würde    der     Fachmann    auch    aus     Gründen   der
Komplexitätsreduktion zunächst die Filterung ausschließlich für 4x4-, 8x8- und
16x16-Blöcke beibehalten - beispielsweise dann, wenn er zeitsparende Tests
durchführen möchte.


2.3.3 Im Übrigen war dem Fachmann zumindest am Anmeldetag des Streitpatents
bewusst, dass eine Beschränkung der Filterung gemäß Merkmal 9 sinnvoll sein
kann,    weil   die   Verwendung     zu     großer   Vorhersageblöcke     mit   großen
Ungenauigkeiten behaftet ist, so dass eine Filterung von Vorhersageblöcken, die

                                       - 49 -



mindestens 32x32 Pixel umfassen, keine Verbesserung der Vorhersageeffizienz
erwarten lässt und nur den Rechenaufwand erhöht (vgl. NK 9a, Absatz [0070], dort
letzter Absatz; NK 9, Absatz [0078], letzter Spiegelpunkt).


2.4   Die Beklagte argumentiert, Merkmal 9 sei nur für die in Figur 6 der NK 11
gezeigte Filterfolge „A – B – C“ offenbart. Daraus folge aber noch nicht, dass Blöcke
der Größe 32x32 und 64x64 von der Filterung ausgenommen seien. Der Fachmann
würde sowohl große Blöcke als auch kleine Blöcke filtern wollen.


Auch dieses Argument verfängt nicht.


2.4.1 Denn Merkmal 9 ist bereits dann verwirklicht, wenn eine einzelne
Testrechnung mit Filterfolge „B – B – B – 0 – 0“ durchgeführt wird (s.o., Abschnitt
IV.2.2, letzter Absatz). Wie oben in Abschnitt III.1.3.3 dargelegt, hat der Fachmann
hinreichende Veranlassung, eine solche Rechnung auszuführen und seine Tests
auf Blöcke der Größe 4x4, 8x8 und 16x16 zu beschränken.


2.4.2 Ferner mag es zwar sein, dass der Fachmann grundsätzlich auch daran
interessiert ist, im Rahmen von Tests zu ermitteln, wie sich die Filter #A, #B und #C
auf Blöcke auswirken, die größer als 16x16 Pixel sind. Dieser Umstand weist jedoch
lediglich auf eine alternative Möglichkeit hin, Testrechnungen auszuführen. Selbst
wenn der Fachmann diese Möglichkeit ebenfalls in Betracht ziehen würde, würde
dies am Naheliegen des Merkmals 9 nichts ändern. Denn in diesem Fall lägen
lediglich zwei naheliegende, sich gegenseitig ausschließende Lösungsalternativen
vor, von denen die eine - Durchführung von Testrechnungen nur für Blockgrößen
bis 16x16 - den Vorteil eines geringeren Rechenaufwandes und die andere -
Durchführung von Testrechnungen auch für Blöcke, die größer als 32x32 Pixel sind
- den Vorteil eines größeren Erkenntnisgewinns besitzt (vgl. BGH, X ZR 50/16, Urteil
vom 24. April 2018, Rn. 41 m. w. N., juris und GRUR 2018, 1128 - Gurtstraffer;
BGH, X ZR 56/03, Urteil vom 22. Mai 2007, Rn. 25, juris und GRUR 2008, 56 -

                                           - 50 -



injizierbarer Mikroschaum; BGH, X ZR 58/10, Urteil vom 22. November 2011,
Rn. 46, juris und GRUR 2012, 261 - E-Mail via SMS).


2.5     Mit Rücksicht auf die Argumentation zum erteilten Patentanspruch 1 beruht
der Gegenstand von Patentanspruch 1 nach Hilfsantrag I somit im Lichte einer
Kombination der jeweiligen Lehren der NK 1 und NK 11 nicht auf einer
erfinderischen Tätigkeit.




3.      Der Hilfsantrag II kann nicht günstiger als der Hauptantrag beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls nicht auf einer
erfinderischen Tätigkeit beruht.


3.1     Gegenüber dem erteilten Patentanspruch 1 werden bei Patentanspruch 1
nach Hilfsantrag II nach Merkmal 8.3 die beiden Merkmale


10      „wherein whether to perform the filtering depends on the intra prediction
        mode and the size of the prediction block,”


11      „and a filter type for the filtering depends on the intra prediction mode”


angehängt.


3.2     Dabei betrifft der Ausdruck „the filtering“ in Merkmal 10 angesichts des
Absatzes [0238] der Streitpatentschrift die in den Merkmalen 2.2 bis 2.2.3 allgemein
-     ohne   Bezugnahme      auf   einen     bestimmten    Intra-Vorhersagemodus      -
angesprochene Filterung auf einem Filterungszielpixel eines Vorhersageblocks. Die
Formulierung „whether to perform the filtering depends on […]“ bringt dabei zum
Ausdruck, dass bei der Intra-Vorhersage der Vorhersagemodus und die
Vorhersageblockgröße beeinflussen, ob ein Filterungszielpixel gefiltert wird oder
nicht. Dass ein solches Pixel nicht gefiltert wird, kann laut Streitpatent z.B. dadurch

                                        - 51 -



erreicht werden, dass der Filtertyp „0“ gewählt wird (vgl. die Absätze [0235], [0239]
und [0259] der Streitpatentschrift, die auf diesen Filtertyp hinweisen).


Das Merkmal 11 ist dann verwirklicht, wenn in mindestens zwei verschiedenen
Vorhersagemodi verschiedene Filtertypen verwendet werden. Gemäß dem
Streitpatent kann ein Filtertyp Informationen über eine Filterform, einen Filtertap und
eine Mehrzahl von Filterkoeffizienten beinhalten (vgl. Streitpatentschrift, Absätze
[0017], [0129], [0130], [0177]). Dabei wird der - im erteilten Patentanspruch 1 nicht
genannte - Begriff „Filtertyp“ generell derart verwendet, dass zur Filterung der
Vorhersagewerte eines Vorhersageblocks jeweils genau ein bestimmter Filtertyp
zum Einsatz kommt (vgl. z.B. Absätze [0234] bis [0236], [0253], [0254]).


3.3     Auch mit den Merkmalen 10 und 11 kann das Vorliegen einer erfinderischen
Tätigkeit nicht begründet werden.


3.3.1 So entsprechen die Zeilen und Spalten der oberen, in Figur 6 der NK 11
gezeigten Lookup-Tabelle jeweils einer bestimmten Vorhersageblockgröße bzw.
einem bestimmten Intra-Vorhersagemodus (vgl. Bildunterschrift zu Figur 6 - „LUT
for each intra prediction size and intra prediction mode“).


Gemäß der Lookup-Tabelle hängt die Entscheidung, ob die Vorhersagepixelwerte
eines      gegenwärtigen   Blocks   gefiltert    werden   oder   nicht,    von   einem
Vorhersagemodus und - zumindest im Hinblick auf die zum DC-Modus gehörende
dritte Tabellenspalte von links - auch von einer Vorhersageblockgröße ab. Denn
zum einen werden im DC-Modus Blöcke der Größe 4x4, 8x8 und 16x16 gefiltert,
Blöcke der Größe 32x32 und 64x64 jedoch nicht, da diesen der Filtertyp „0“
zugeordnet ist. Zum anderen kommen laut Tabelle 1 der Figur 6 die Filter #A, #B
und #C nur im DC-Modus, nicht aber in einem anderen Intra-Vorhersagemodus zum
Einsatz.


Damit sind die Merkmale 10 und 11 der NK 11 zu entnehmen.

                                         - 52 -




3.3.2 Zudem hätte der Fachmann bei Bedarf auch Vorhersagepixelwerte in einem
anderen Vorhersagemodus als dem DC-Modus mit Filtern gefiltert, die sich von den
im DC-Modus verwendeten unterscheiden (s.o., Abschnitt III.1.3.1), so dass sich
Merkmal 11 auch auf diesem Wege ergibt.


3.3.3 Im Übrigen weiß der Fachmann, dass es ganze Klassen von Verfahren gibt,
die zur Verbesserung der Codiereffizienz Pixelwerte von Vorhersageblöcken in
Abhängigkeit des Intra-Vorhersagemodus filtern (vgl. NK 3, Titel „CE 13: Mode
Dependent Hybrid Intra Smoothing“; Abschnitte 1 und 2, Tabellen 2-1 und 2.2 - s.
auch NK 1, insbesondere Tabelle 1).


Merkmal 11 geht nicht über die bloße Angabe hinaus, ein solches bekanntes
Verfahren zu verwenden. Die ist nach dem oben in den Abschnitten III.1.3.1 und
III.1.3.3 e) Gesagten auch objektiv zweckmäßig, wenn der Fachmann eine
Erhöhung der Codiereffizienz im Blick hat.


3.4    Unter Berücksichtigung der Ausführungen zum Patentanspruch 1 des
Streitpatents beruht somit auch der Gegenstand von Patentanspruch 1 nach
Hilfsantrag II nicht auf einer erfinderischen Tätigkeit.




4.     Der Hilfsantrag III kann nicht günstiger beurteilt werden, weil der Gegenstand
seines Patentanspruchs 1 ebenfalls nicht auf einer erfinderischen Tätigkeit beruht.


Patentanspruch 1 nach Hilfsantrag III unterscheidet sich von Patentanspruch 1
nach Hilfsantrag II dadurch, dass auf die Merkmale 10 und 11 das Merkmal 9 des
Hilfsantrags I folgt.


Für den Patentanspruch 1 nach Hilfsantrag III gelten daher die obenstehenden
Ausführungen aus den Abschnitten IV.2 und IV.3 analog.

                                         - 53 -



Im Lichte der Argumentationen zu den Hilfsanträgen I und II beruht der Gegenstand
von Patentanspruch 1 nach Hilfsantrag III somit nicht auf einer erfinderischen
Tätigkeit.




5.     Der Hilfsantrag IV kann nicht günstiger als der Hauptantrag beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls im Lichte der Lehre der
NK 11 nicht auf einer erfinderischen Tätigkeit beruht.


5.1    Patentanspruch      1   nach   Hilfsantrag    IV    geht   aus   dem   erteilten
Patentanspruch 1 hervor, indem nach Merkmal 8.3 das Merkmal


12     „wherein performing the filtering includes adding an offset value and applying
       the arithmetic right-shift operator”


hinzugefügt wird.


5.2    Der Fachmann erkennt in dieser Anweisung die verbale Abstraktion zweier
mathematischer Teilschritte der in den Absätzen [0256] bis [0259] der
Streitpatentschrift gezeigten Formeln. Dort verschiebt der Right-Shift-Operator „>>“
eine Binärzahl um zwei Stellen nach rechts und schneidet dabei die beiden ganz
rechts angeordneten Bits der Binärzahl ab. Dadurch wird diese näherungsweise
durch 4 dividiert. Aufgrund der vorher ausgeführten Addition von 2 werden
Rundungsfehler vermieden, die durch das Abschneiden der beiden Bits entstehen.


Den Ausdruck „the filtering“ in Merkmal 12 bezieht der Fachmann auf das Filtern
von Vorhersagepixelwerten im DC-Modus oder auch in einem anderen
Vorhersagemodus. Dabei ist dem Fachmann klar, dass das Filtern üblicherweise
die Bildung eines gewichteten Mittelwerts von Referenzpixelwerten und Pixelwerten
von Vorhersagepixeln umfasst, so dass die zugehörigen binären Operationen
Divisionen   beinhalten,   die   typischerweise     als   Right-Shift-Operationen   mit

                                         - 54 -



vorausgehender     Addition     eines   Offsetwerts   implementiert   werden     (vgl.
Streitpatentschrift, Absätze [0256] bis [0259]).


5.3   Die Aufnahme des Merkmals 12 in den erteilten Patentanspruch 1 kann keine
erfinderische Tätigkeit begründen.
Denn dieses Merkmal geht unmittelbar aus den Gleichungen (6-x1) bis (6-x3), (6-x5)
bis (6-x7) sowie (6-x9) bis (6-x11) der NK 11 hervor.


5.4   Auch der Gegenstand von Patentanspruch 1 nach Hilfsantrag IV beruht
daher im Lichte der Ausführungen zum erteilten Patentanspruch 1 nicht auf einer
erfinderischen Tätigkeit.




6.    Der Hilfsantrag V kann nicht günstiger als der Hauptantrag beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls im Lichte der
kombinierten Lehren der Druckschriften NK 11 und NK 1 nicht auf einer
erfinderischen Tätigkeit beruht.


6.1   Patentanspruch        1   nach    Hilfsantrag   V   unterscheidet   sich   von
Patentanspruch 1 nach Hilfsantrag I dadurch, dass nach dem Merkmal 9 das
Merkmal


13    „wherein the number of different intra prediction modes that the current block
      may have is a predetermined fixed value that does not change according to
      a size of the prediction block“


angefügt wird.


6.2   Das Merkmal 13 versteht der Fachmann vor dem Hintergrund von
Absatz [0073] der Streitpatentschrift derart, dass zur Vorhersage (und ggf. auch zur
Filterung) eines bestimmten gegenwärtigen Blocks eine feste Anzahl von Intra-

                                        - 55 -



Vorhersagemodi zur Verfügung steht, wobei sich diese Anzahl nicht mit der Größe
eines Vorhersageblocks ändert, der mit dem gegenwärtigen Block zusammenfällt
oder in diesem enthalten ist (siehe oben, Abschnitt II.4.1) oder wobei diese Anzahl
unabhängig von einer solchen Vorhersageblockgröße ist.


Merkmal 13 impliziert nicht, dass ein gegenwärtiger Block in einem zur Verfügung
stehenden Vorhersagemodus auch tatsächlich gefiltert werden muss. So geht aus
der Streitpatentschrift hervor, dass basierend auf dem Intra-Vorhersagemodus des
Vorhersageblocks entschieden wird, ob gefiltert wird oder nicht - d.h. der Intra-Vorhersagemodus existiert für einen gegenwärtigen Block unabhängig von der
Filterung (vgl. Absatz [0112] - „the decoder may determine whether or not the
filtering is performed on the prediction block based on the intra prediction mode of
the encoding/decoding target block“; ein „decoding target block“ kann nach Absatz
[0069] ein gegenwärtiger Block sein; s. auch Absatz [0114] - „0 among the values
allocated to the intra prediction mode may indicate that the filtering is not
performed“, oder Absatz [0237] - „the filter type according to the prediction mode
may also include the information on whether or not the filter is applied according to
the block size […] filter type based on the intra prediction mode“). Dies ist dem
Fachmann auch unmittelbar klar, da die Filterung ein optionaler Teil der Intra-Vorhersage ist (vgl. auch Streitpatentschrift, Absatz [0095], erster Satz).


Damit ergibt sich auch kein Widerspruch zwischen den Merkmalen 9 und 13: mit
der Kombination dieser Merkmale ist es z.B. vereinbar, dass einem gegenwärtigen
Block der Größe 32x32 zwar eine bestimmte Anzahl von Intra-Vorhersagemodi
zugeordnet ist, in denen jeweils Vorhersagewerte eines Vorhersageblocks
berechnet werden können, der gegenwärtige Block aber weder in einem dieser Modi
noch in irgendeinem anderen Intra-Vorhersagemodus gefiltert wird.


6.3   Auch die Aufnahme des Merkmals 13 in den Patentanspruch 1 nach
Hilfsantrag I kann eine erfinderische Tätigkeit nicht stützen.

                                        - 56 -



a)      So entnimmt der Fachmann der Bildunterschrift der Figur 6 der NK 11 („LUT
for each intra prediction unit size and intra prediction mode“), dass jede der 40
Spalten der in der Figur oben gezeigten Tabelle einem Intra-Vorhersagemodus
zugeordnet sein und jede der fünf Zeilen einer möglichen Größe eines
Vorhersageblocks entsprechen soll. Mit anderen Worten: Vorhersageblöcken der
Größe 4x4 bis 64x64 soll jeweils eine vorbestimmte feste Anzahl von 40
Vorhersagemodi zugeordnet sein.


Ferner ist es für den Fachmann selbstverständlich, dass ein gegenwärtiger Block
mit einem Vorhersageblock zusammenfallen kann (vgl. Abschnitt II.4.1). In diesem
Fall sind also auch jedem gegenwärtigen Block der Größe 4x4 bis 64x64 die 40
Vorhersagemodi zugeordnet.


Der Fachmann wird ferner davon ausgehen, dass jeder Eintrag der in Figur 6
gezeigten Tabelle auf einen Wert gesetzt werden kann, der entweder die Filterung
eines Referenzpixels oder die Filterung eines Vorhersagepixels nach sich zieht.
Dies ist aber nur dann sinnvoll, wenn in allen 40 Vorhersagemodi Pixelwerte von
Vorhersageblöcken der Größe 4x4, 8x8, 16x16, 32x32 und 64x64 vorhergesagt -
und damit auch Pixelwerte von gegenwärtigen Blöcken dieser fünf Größen ermittelt
- werden. Das bedeutet wiederum nichts anderes, als dass für jede der fünf
Blockgrößen eine feste Anzahl von 40 Intra-Vorhersagemodi zur Verfügung steht.


b)      Darüber hinaus leitet der Fachmann das Merkmal 13 auch dann auf
naheliegende Weise ab, wenn die Lehre der NK 11 derart interpretiert wird, dass
die Anzahl von Intra-Vorhersagemodi, die ein gegenwärtiger Block haben kann,
grundsätzlich    für   verschiedene    Blockgrößen     des   gegenwärtigen    Blocks
unterschiedliche Werte annehmen kann.


Denn für den Fachmann ist es ebenfalls selbstverständlich, dass ein gegenwärtiger
Block    neben   einem einzigen       großen     Vorhersageblock mehrere     kleinere
Vorhersageblöcke enthalten kann (vgl. Abschnitt II.4.1), wobei sich die Anzahl von

                                       - 57 -



Vorhersagemodi, die zur Vorhersage der Pixelwerte des gegenwärtigen Blocks zur
Verfügung steht, in Abhängigkeit der Größe dieser Vorhersageblöcke nicht ändert
bzw. unabhängig von dieser Größe ist (vgl. z.B. Abschnitt 2.2.2 der NK 5, aus dem
hervorgeht, dass eine CU der Größe 2Nx2N aus einer PU der Größe 2Nx2N oder
aus vier quadratischen PUs der Größe NxN bestehen kann i. V. m. Tabelle 2-8 auf
Seite 17, der z.B. zu entnehmen ist, dass eine CU der Größe 8x8 eine vorher
festgelegte Anzahl von 9 Intra-Vorhersagemodi hat, und diese Anzahl unabhängig
davon ist, ob die CU aus einer 8x8 großen PU oder aus vier PUs der Größe 4x4
besteht, und sich daher mit der PU-Größe - 4x4 oder 8x8 - nicht ändert).


6.4   Die Beklagte argumentiert, der NK 11 lasse sich im Hinblick auf die
eingetragenen Nullen nicht entnehmen, „ob die jeweilige Kombination aus
Blockgröße und Vorhersagemodus zwar gewählt werden kann, bei dieser Wahl
jedoch keine Filterung erfolgt, oder ob die Kombination nicht zur Verfügung steht“.
Sie verweist in diesem Zusammenhang auf die NK 13; diese stelle den zum
Zeitpunkt der Abfassung der NK 11 aktuellen Standardentwurf dar, vor dem die
NK 11 zu lesen sei. In Abschnitt 8.3.1 - insbesondere in Tabelle 8-2 - der NK 13 sei
gerade gezeigt, dass die Anzahl „intraPredModeNum“ der Intra-Vorhersagemodi
über die Variable „log2TrafoSize“ von der Größe eines aktuellen Vorhersageblocks
abhänge. Ferner setze die Argumentation des Senats voraus, dass der DC-Vorhersagemodus für die Blockgrößen 32x32 und 64x64 nicht zur Verfügung steht.


Auch diese Ausführungen können nicht überzeugen.


a)    Zwar ist es zutreffend, dass die Bedeutung der eingetragenen Nullen in der
in Figur 6 der NK 11 oben abgebildeten Tabelle nicht ausdrücklich erklärt wird. Wie
oben ausgeführt (vgl. Abschnitt IV.6.3 a)), bedeutet das aber nicht, dass ein
Vorhersagemodus für 32x32- und 64x64-Blöcke nicht zur Verfügung steht.


Für den Fachmann steht vielmehr fest, dass sämtliche Einträge in der Tabelle eine
Filterung betreffen. So beziehen sich die Nullen in der zweiten Spalte der Tabelle

                                       - 58 -



auf den Fall, dass die Variable „DCFilterType“ gleich 0 ist, und die Nullen in den
übrigen Spalten darauf, dass die Variable „intraFilterType“ den Wert 0 hat, so dass
im ersten Fall insbesondere Vorhersagepixelwerte und im zweiten Fall
insbesondere Referenzpixelwerte nicht gefiltert werden. Im Hinblick auf die fehlende
Filterung der Vorhersagepixelwerte ergibt sich dies aus einem Vergleich der
Einträge „A B C 0 0“ in der zum DC-Modus gehörenden dritten Spalte der Tabelle
mit den zu verschiedenen Blockgrößen gehörenden Einträgen „3 2 1 0 0“ für die
Werte der Variablen „DCFilterType“ in der auf Seite 12 der NK 11 gezeigten Tabelle
sowie mit dem auf derselben Seite gezeigten Pseudocode. Im Hinblick auf eine
Filterung von Referenzpixelwerten folgt dies aus der Übereinstimmung der
Tabelleneinträge („0“ oder „1“) in den übrigen Spalten der Tabelle der Figur 6 mit
den entsprechenden Einträgen in der auf Seite 10 der NK 11 gezeigten Tabelle. Da
die Tabelleneinträge selbst nur eine Filterung betreffen und ein Vorhersageblock im
DC-Modus per se nicht unbedingt gefiltert werden muss, bedeutet das also nicht,
dass ein Intra-Vorhersagemodus - insbesondere der DC-Vorhersagemodus - für
32x32- und 64x64-Blöcke nicht zur Verfügung steht.


b)    Im Übrigen ist bereits nicht ersichtlich, dass der Fachmann die Lehre der
NK 11 ausschließlich vor dem Hintergrund der NK 13 interpretieren würde.


Selbst wenn er dies täte und zudem die in der Tabelle 8-2 der NK 13 gezeigten
Anzahlen von Intra-Vorhersagemodi für einen jeweiligen gegenwärtigen Block
vorsehen würde, würde die Argumentation aus Abschnitt IV.6.3 b) analog
entgegenstehen, da auch die NK 13 insbesondere für gegenwärtige Blöcke der
Größe 16x16 und 32x32 gemäß den Werten der Syntaxelemente „slice_type“,
„pred_type“, „IntraSplitFlag“, „pred_mode“ und „intra_part_mode“/“PartMode“ eine
optionale Unterteilung in vier Intra-Vorhersageblöcke der Größe 8x8 bzw. 16x16
vorsieht (vgl. Abschnitt 7.4.6, insbesondere Tabelle 7-11; s. auch Abschnitt 7.3.6).

                                           - 59 -



6.5    Mit Rücksicht auf die Ausführungen zum Patentanspruch 1 nach Hilfsantrag
I beruht der Gegenstand von Patentanspruch 1 nach Hilfsantrag V somit nicht auf
einer erfinderischen Tätigkeit.




7.     Der Hilfsantrag VI kann nicht günstiger beurteilt werden, weil der Gegenstand
seines Patentanspruchs 1 ebenfalls nicht auf einer erfinderischen Tätigkeit beruht.


7.1    Patentanspruch 1 nach Hilfsantrag VI unterscheidet sich von dem erteilten
Patentanspruch 1 dadurch, dass nach Merkmal 8.3 die Merkmale


14.1 „applying the first filter is performed by
       (i) adding a value of the left reference pixel, the prediction value multiplied by
       a value of 2, a value of the upper reference pixel, and a value of 2 to generate
       a first result, and
       (ii) shifting the bits of the first result two positions to the right using an
       arithmetic right shift operator,“


14.2   „applying the second filter is performed by
       (i) adding a value of the left reference pixel, the prediction value multiplied by
       a value of 3, and a value of 2 to generate a second result, and
       (ii) shifting the bits of the second result two positions to the right using an
       arithmetic right shift operator,“


14.3   „applying the third filter is performed by
       (i) adding a value of the upper reference pixel, the prediction value multiplied
       by a value of 3, and a value of 2 to generate a third result, and
       (ii) shifting the bits of the third result two positions to the right using an
       arithmetic right shift operator“


hinzugefügt werden.

                                       - 60 -



Mit den Merkmalen 14.1 bis 14.3 wird sprachlich zum Ausdruck gebracht, wie die
Filteroperationen der Merkmale 6.1 bis 8.3 auf Bitebene mittels entsprechender
Additionen, Multiplikationen und Bit-Shift-Operationen konkret ausgeführt werden.


7.2   Auch die Merkmale 14.1 bis 14.3 können keine erfinderische Tätigkeit
stützen.


Denn diese Merkmale sind den Gleichungen (6-x5) bis (6-x7) der NK 11 zu
entnehmen. Diese Gleichungen zeigen eine spezielle Implementierung der
Filterung mit dem Filter „#B“. Dabei entspricht Gleichung (6-x5) der Anwendung des
ersten Filters gemäß Merkmal 14.1, Gleichung (6-x7) der Anwendung des zweiten
Filters gemäß Merkmal 14.2, und Gleichung (6-x6) der Anwendung des dritten
Filters gemäß Merkmal 14.3.


7.3   Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 1 beruht
auch der Gegenstand von Patentanspruch 1 nach Hilfsantrag VI daher nicht auf
einer erfinderischen Tätigkeit.




8.    Der Hilfsantrag VII kann nicht günstiger als der Hauptantrag beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls im Lichte der Lehre der
NK 11 nicht auf einer erfinderischen Tätigkeit beruht.


8.1   Patentanspruch 1 nach Hilfsantrag VII kombiniert die Merkmale des erteilten
Patentanspruchs 1 mit den Merkmalen 9, 13 und 14.


Die Ausführungen zu Patentanspruch 1 in den Fassungen der Hilfsanträge I, V und
VI gelten hier entsprechend.


Auch der Gegenstand von Patentanspruch 1 nach Hilfsantrag VII beruht daher nicht
auf einer erfinderischen Tätigkeit.

                                          - 61 -




9.     Die Hilfsanträge I a bis VII a teilen das Schicksal der mit ihnen
korrespondierenden Hilfsanträge I bis VII.


9.1    Die Patentansprüche 1 der Hilfsanträge I a bis VII a gehen jeweils aus den
Patentansprüchen 1 der Hilfsanträge I bis VII hervor, indem in jedem dieser
Patentansprüche das Merkmal 2.2.1 durch das Merkmal 2.2.1a ersetzt und nach
Merkmal 8.3 das Merkmal 8.4 angefügt wird.


9.2    Wie bereits oben zum Hauptantrag a ausgeführt (s.o., Abschnitt IV.1), kann
auch nach Aufnahme dieser Änderungen in den erteilten Patentanspruch 1 das
Vorliegen einer erfinderischen Tätigkeit nicht bejaht werden. Dies gilt jeweils analog
für die Aufnahme der Änderungen in den Patentanspruch 1 gemäß jedem der
Hilfsanträge I, II, III, IV, V, VI und VII. Denn zum einen gelten die Ausführungen zu
den jeweiligen Patentansprüchen 1 der Hilfsanträge I bis VII auch für die
Patentansprüche 1 der Hilfsanträge I a bis VII a, und zum anderen ist nicht
erkennbar, dass sich aus der Kombination der Merkmale 2.2.1a und 8.4 mit den
Merkmalen 9 bis 13 sowie 14.1, 14.2 und 14.3 ein Sachverhalt ergibt, der nicht im
Rahmen der Ausführungen zum Hauptantrag a und den Hilfsanträgen I bis VII
erfasst wird.


9.3    Auch der Gegenstand des jeweiligen Patentanspruchs 1 in den Fassungen
der Hilfsanträge I a, II a, III a, IV a, V a, VI a und VII a beruht daher unter
Berücksichtigung der Ausführungen zum Hauptantrag a und den Hilfsanträgen I, II,
III, IV, V, VI und VII nicht auf einer erfinderischen Tätigkeit.

                                       - 62 -



                                            V.


Nachdem das Streitpatent aus den vorstehend ausgeführten Gründen in keiner
seiner durch die Beklagte verteidigten Fassungen Rechtsbestand hat, war es somit
in vollem Umfang für nichtig zu erklären.




                                        VI.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.




                                        VII.


                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt schriftlich oder in elektronischer Form beim Bundesgerichtshof,
Herrenstraße 45a, 76133 Karlsruhe, einzulegen.

                                       - 63 -



Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten.


Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des
angefochtenen Urteils vorgelegt werden.




Hartlieb     Dr. Forkel      Dr. Himmelmann          Dr. Städele         Dr. Harth
