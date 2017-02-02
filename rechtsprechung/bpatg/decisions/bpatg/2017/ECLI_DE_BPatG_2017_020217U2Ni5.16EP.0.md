---
ecli: "ECLI:DE:BPatG:2017:020217U2Ni5.16EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 5/16"
decided: "2017-02-02"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=5&nr=29077&anz=809&pos=81&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2017-02-02_2_Ni_5_16_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 5/16 vom 2017-02-02

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                       Verkündet am
                                                      2. Februar 2017
 2 Ni 5/16 (EP)                                              …
hinzuverbunden
2 Ni 11/17 (EP)

(Aktenzeichen)
                     In der Patentnichtigkeitssache

 …




 BPatG 253
 08.05

                                          -2-



…




                  betreffend das europäische Patent 0 734 181
                                     (DE 696 28 487)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 2. Februar 2017 unter Mitwirkung des Vorsitzenden
Richters Guth, der Richterinnen Hartlieb und Dipl.-Phys. Dr. Thum-Rung sowie der
Richter Dipl.-Phys. Dr. Forkel und Dipl.-Ing. Hoffmann


für Recht erkannt:


        I.    Das europäische Patent 0 734 181 wird mit Wirkung für das
              Hoheitsgebiet der Bundesrepublik Deutschland im Umfang
              seiner Ansprüche 5, 6, 7, 13, 14, 15, 19 (soweit dieser auf
              einen der Ansprüche 5 bis 7 rückbezogen ist) und 20 (soweit
              dieser auf einen der Ansprüche 13 bis 15 rückbezogen ist)
              für nichtig erklärt.


        II.   Die Beklagte trägt die Kosten des Rechtsstreits.

                                           -3-



        III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
                des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.


                                     Tatbestand




Mit ihrer Klage begehren die Klägerinnen die Nichtigerklärung des europäischen
Patents EP 0 734 181 im Umfang seiner Patentansprüche 5, 6, 7, 13, 14, 15 und 19
bzw. 19 (soweit dieser auf einen der Patentansprüche 5 bis 7 rückbezogen ist)
und 20 (soweit dieser auf einen der Patentansprüche 13 bis 15 rückbezogen ist).


Die Klage der Klägerin zu 1. und die Klage der Klägerin zu 2., deren Aktenzeichen
zunächst 2 Ni 11/16 lautete, sind mit Beschluss vom 22. März 2016 verbunden worden
und werden unter dem Aktenzeichen 2 Ni 5/16 geführt.


Die Beklagte war eingetragene Inhaberin des am 21. März 1996 unter Inanspruchnahme der Priorität der japanischen Patentanmeldung JP 8860795 vom
23. März 1995 angemeldeten und am 4. Juni 2003 in der Amtssprache Englisch
veröffentlichten europäischen Patents 0 734 181 (Streitpatent) mit der Bezeichnung „Subtitle data encoding/decoding and recording medium for same”, dessen
deutscher Teil vom Deutschen Patent- und Markenamt unter der Nummer
DE 696 28 487 geführt wird. Das Streitpatent, das am 21. März 2016 durch Zeitablauf erloschen ist, umfasst insgesamt 21 Patentansprüche.


Gegen     die    Nichtigkeitsklägerinnen   ist   wegen   Verletzung   des   Streitpatents - gestützt auf dessen Patentansprüche 5 und 19 - Klage erhoben worden.


Hinsichtlich des Wortlauts der erteilten angegriffenen Patentansprüche wird auf
die Patentschrift 0 734 181 B1 verwiesen.

                                            -4-



Die Beklagte, die ihr Patent zunächst in der erteilten Fassung sowie hilfsweise
nach den Hilfsanträgen I bis VI gemäß Anlagen zum Schriftsatz vom
9. Dezember 2016 verteidigt hatte, verteidigt ihr Patent nunmehr im beschränkten
Umfang gemäß Hauptantrag, der dem ursprünglichen Hilfsantrag I entspricht, sowie den Hilfsanträgen II bis VI.


Die Patentansprüche 5, 6, 7, 13, 14, 15, 19 und 20 des Streitpatents lauten in der
beschränkt verteidigten Fassung gemäß Hauptantrag (entspricht im Wortlaut
Hilfsantrag I) in der Verfahrenssprache Englisch (mit bei unverändertem Wortlaut
eingefügter Gliederung; die Unterschiede zum Streitpatent in der erteilten Fassung
sind markiert):


Patentanspruch 5


5            A subtitle decoding apparatus (7) for use in a video image
             display system, said apparatus comprising:
5.1          a colour lookup table (26) having addresses for accessing
             display data;
5.2          means for receiving data blocks (200) including loading
             blocks and pixel data blocks,
5.2.1        said pixel data blocks representing subtitle data and
5.2.2        said    loading       blocks   including   changeover   position
             information,
5.2.2.1      said changeover position information being used to update a
             change position located in the video image, wherein
5.2.2.2      a current address for accessing said colour lookup table is
             changeable to a next address every frame period so that
             different display data are accessed at the change position
             indicated by said changeover position information,
5.2.2.3´     said changeover position information comprising delay length
             data, said delay length data being used to control a delay in
             the update of the change position and further being used to

                                      -5-



           set a length of said delay when the same changeover
           information continues for a plurality of frames;
5.3        means     for   detecting (200)   said   changeover     position
           information from said loading blocks; and
5.4        means for displaying (210 to 209) said subtitles and the
           video image on a display screen as a function of said
           changeover position information and said colour lookup
           table.


Patentanspruch 6


6          An apparatus according to claim 5, wherein
6.1        said display data includes fill data representing a luminance
           level of the subtitle data and
6.2        key data representing a mixing ratio between said fill data
           and the video image.”


Patentanspruch 7


7          An apparatus according to claim 5, wherein
7.1        said changeover position information includes progress bits
           for updating said change position,
7.2        holding bits for delaying an update of said change position
           and
7.3        frame count value bits for setting a length of said delay.


Patentanspruch 13


13         A subtitle decoding method for use in a video image display
           system, said method comprising the steps of:
13.2       receiving data blocks including loading blocks and pixel data
           blocks,

                                          -6-



13.2.1      said pixel data blocks representing subtitle data and
13.2.2      said    loading      blocks   including    changeover      position
            information,
13.2.2.1    said changeover position information being used to update a
            change position located in the video image, wherein
13.2.2.2    a current address for accessing a colour lookup table having
            addresses for accessing display data is changeable to a next
            address every frame period so that different display data are
            accessed       at   the   change    position   indicated   by   said
            changeover position information,
13.2.2.3´   said changeover position information comprising delay length
            data, said delay length data being used to control a delay in
            the update of the change position and further being used to
            set a length of said delay when the same changeover
            information continues for a plurality of frames;
13.3        detecting said changeover position information from said
            loading blocks; and
13.4        displaying said subtitle data and the video image on a display
            screen as a function of said changeover position information
            and said colour lookup table.


Patentanspruch 14


14          A method according to claim 13, wherein said display data
            includes fill data representing a luminance level of the
            subtitle data and key data representing a mixing ratio
            between said fill data and the video image.


Patentanspruch 15


15          A method according to claim 13, wherein said changeover
            position information includes progress bits for updating said

                                     -7-



           change position, holding bits for delaying an update of said
           change position and frame count value bits for setting a
           length of said delay.


Patentanspruch 19


19         An apparatus according to any one of claims 1 to 8, wherein
19.1       said changeover position information comprises colour-wipe
           information and
19.2       updating said change position corresponds to moving a
           colour-wipe forward,
19.3       said colour-wipe being movable forward every frame period
           to shade the subtitle data based on said colour-wipe
           information,
19.4´      and wherein said delay length data are used to control a
           delay of said colour wipe and are further used to set a length
           of said delay.


Patentanspruch 20


20         A method according to any one of claims 9 to 16, wherein
20.1       said changeover position information comprises colour-wipe
           information and
20.2       updating said change position corresponds to moving a
           colour-wipe forward,
20.3       said colour-wipe being movable forward every frame period
           to shade the subtitle data based on said colour-wipe
           information,
20.4´      and wherein said delay length data are used to control a
           delay of said colour wipe and are further used to set a length
           of said delay.

                                             -8-



Patentanspruch 5 nach Hilfsantrag II unterscheidet sich von Patentanspruch 5
nach      Hauptantrag    durch    den     Merkmalskomplex 5.5´,   der    sich   an   den
Merkmalskomplex 5.4 anschließen soll:


5.5´           wherein
5.5.1´         said changeover position information comprises colour-wipe
               information and
5.5.2´         updating said change position corresponds to moving a
               colour-wipe forward,
5.5.3´         said colour-wipe being movable forward every frame period
               to shade the subtitle data based on said colour-wipe
               information, and
5.5.4´         wherein said delay length data are used to control a delay of
               said colour wipe and are further used to set a length of said
               delay.


Patentanspruch 13          nach         Hilfsantrag II   unterscheidet     sich      von
Patentanspruch 13 nach Hauptantrag durch den Merkmalskomplex 13.5´, der sich
an den Merkmalskomplex 13.4 anschließen soll:


13.5´          wherein
13.5.1´        said changeover position information comprises colour-wipe
               information and
13.5.2´        updating said change position corresponds to moving a
               colour-wipe forward,
13.5.3´        said colour-wipe being movable forward every frame period
               to shade the subtitle data based on said colour-wipe
               information, and
13.5.4´        wherein said delay length data are used to control a delay of
               said colour wipe and are further used to set a length of said
               delay.

                                        -9-



Die Patentansprüche 6, 7, 14 und 15 nach Hilfsantrag II sind mit den Patentansprüchen 6, 7, 14 und 15 des Hauptantrags und des erteilten Patents identisch.
Die Patentansprüche 19 und 20 sind gestrichen.


Im Hilfsantrag III wurden die angegriffenen Vorrichtungsansprüche 5, 6, 7 und 19
sowie der Verfahrensanspruch 20 gestrichen. Die Verfahrensansprüche 13, 14
und 15 entsprechen den Verfahrensansprüchen 13, 14 und 15 nach Hilfsantrag II.


Patentanspruch 5 nach Hilfsantrag IV unterscheidet sich von Patentanspruch 5
nach Hauptantrag durch den Merkmalskomplex 5.2.2.3´´, der an die Stelle von
Merkmalskomplex 5.2.2.3´ treten soll:


5.2.2.3´´    said changeover position information comprising delay length
             data, said delay length data being used to control a delay in
             the update of the change position and further being used to
             set a length of said delay when the same changeover
             information continues for a plurality of frames;


Entsprechend unterscheidet sich Patentanspruch 13 nach Hilfsantrag IV von
Patentanspruch 13 nach Hauptantrag durch den Merkmalskomplex 13.2.2.3´´, der
den Merkmalskomplex 13.2.2.3´ ersetzen soll:


13.2.2.3´´   said changeover position information comprising delay length
             data, said delay length data being used to control a delay in
             the update of the change position and further being used to
             set a length of said delay when the same changeover
             information continues for a plurality of frames;


Analog wurden in den Patentansprüchen 19 und 20 die Merkmale 19.4´
und 20.4´ ersetzt durch die Merkmale 19.4´´ und 20.4´´:

                                        - 10 -



19.4´´        and wherein said delay length data are used to delay said
              colour wipe and are further used to set a length of said delay.
und
20.4´´        and wherein said delay length data are used to delay said
              colour wipe and are further used to set a length of said delay.


Die Patentansprüche 6, 7, 14 und 15 nach Hilfsantrag IV sind mit den entsprechenden Patentansprüchen des Hauptantrags identisch.


Patentanspruch 5 nach Hilfsantrag V unterscheidet sich von Patentanspruch 5
nach Hilfsantrag IV durch den Merkmalskomplex 5.5´´, der auf den Merkmalskomplex 5.4 folgen soll:


5.5´´         wherein
5.5.1´´       said changeover position information comprises colour-wipe
              information and
5.5.2´´       updating said change position corresponds to moving a colour-wipe forward,
5.5.3´´       said colour-wipe being movable forward every frame period
              to shade the subtitle data based on said colour-wipe information, and
5.5.4´´       wherein said delay length data are used to delay said colour
              wipe and are further used to set a length of said delay.


Patentanspruch 13 nach Hilfsantrag V unterscheidet sich von Patentanspruch 13 nach Hilfsantrag IV durch den Merkmalskomplex 13.5´´, der sich an den
Merkmalskomplex 13.4 anschließen soll:


13.5´´        wherein
13.5.1´´      said changeover position information comprises colour-wipe
              information and

                                       - 11 -



13.5.2´´     updating said change position corresponds to moving a
             colour-wipe forward,
13.5.3´´     said colour-wipe being movable forward every frame period
             to shade the subtitle data based on said colour-wipe
             information, and
13.5.4´´     wherein said delay length data are used to delay said colour
             wipe and are further used to set a length of said delay.


Die Patentansprüche 6, 7, 14 und 15 nach Hilfsantrag V entsprechen den Patentansprüchen 6, 7, 14 und 15 des Hauptantrags. Die Patentansprüche 19
und 20 wurden gestrichen.


Im Hilfsantrag VI wurden die Vorrichtungsansprüche 5, 6, 7 und 19 und der Verfahrensanspruch 20 gestrichen. Die Verfahrensansprüche 13, 14 und 15 stimmen
mit den Patentansprüchen 13, 14 und 15 nach Hilfsantrag V überein.


Die Klägerin zu 1. greift das Streitpatent im Umfang seiner Patentansprüche 5
und 19, die Klägerin zu 2. im Umfang seiner Patentansprüche 5, 6, 7, 13, 14, 15
und 19 (soweit dieser auf einen der Patentansprüche 5 bis 7 rückbezogen ist)
und 20 (soweit dieser auf einen der Patentansprüche 13 bis 15 rückbezogen ist)
an. Die Klägerinnen machen als Nichtigkeitsgründe geltend, der Gegenstand des
Streitpatents gehe über den Inhalt der Anmeldung in der ursprünglich eingereichten
Fassung hinaus und sei auch nicht patentfähig, da er im Hinblick auf die vorgelegten Dokumente zum Stand der Technik nicht neu sei und nicht auf einer erfinderischen Tätigkeit beruhe. Zudem machen die Klägerinnen geltend, dass die angegriffenen Patentansprüche 5 und 19 bzw. 13 und 20 die angegebene Priorität nicht
wirksam in Anspruch nehmen könnten.


Die Klägerin zu 2. erklärt, sie habe ein Rechtsschutzbedürfnis auch an der Vernichtung der Patentansprüche 6, 7, 13, 14, 15, 19 und 20. Bei diesen Patentansprüchen handele es sich um mögliche Rückfallpositionen der Beklagten als Klägerin im Verletzungsverfahren, auf die diese zurückgreifen könnte.

                                     - 12 -



Die Klägerinnen stützen ihr Vorbringen auf die folgenden Dokumente (im Interesse
einheitlicher Bezeichnungen wird, wenn möglich, die Nomenklatur der Klägerin
zu 2. verwendet; vom Senat geänderte Bezeichnungen sind durch Unterstreichen
markiert):


NK1            EP 0 734 181 B1 (Streitpatentschrift)
NK1a           zugehörige europäische Patentanmeldung
NK1b           englische Übersetzung der japanischen Patentanmeldung
               JP 88607/95 (Prioritätsdokument)
NK1c           DE 696 28 487 T2 (deutsche Übersetzung der NK1;
               NK2 der Klägerin zu 1.)
NK2            Registerauszug
NK3, NK4       Klageschriften von Verletzungsklagen am Landgericht
               Mannheim
NK3a           Replik der Verletzungsklägerin (hiesige Beklagte) im
               Verletzungsverfahren gegen die Klägerin zu 2. vom
               13. März 2015
NK4a           Prüfungsbescheid des Europäischen Patentamts
NK4b           Antwort der Nichtigkeitsbeklagten auf den Prüfungsbescheid
NK5            Standard „DVD Specifications for Read-Only Disc”, Part 3
               Video Specifications V1.1
NK6            EP 0 725 541 A2
NK6a           englische Übersetzung des japanischen Prioritätsdokuments der Europäischen Patentanmeldung zu NK6
NK6b           DE 696 00 670 T2 (deutsche Übersetzung der Patentschrift zu NK6; NK7a der Klägerin zu 1.)
NK7            EP 0 677 954 A2
NK8            US 5 453 570 A
NK9            EP 0 339 931 A2
NK10           JP 6-118979
NK10a‘         deutsche Übersetzung der NK10

                             - 13 -



NK10a   JP 3149574 B2 (Patentschrift zu NK10)
NK10b   maschinelle Übersetzung der NK10a ins Englische
NK11    US 5 208 413 A
NK12    WO 95/01704 A1
NK12a   EP 0 622 770 A1 (englischsprachige Veröffentlichung der
        internationalen Anmeldung NK12)
NK13    EP 0 622 745 A2
NK14    EP 0 372 678 A2
NK15    JP 6-22331
NK15a   Übersetzung der NK15 ins Deutsche
NK16    EP 0 488 732 A2
NK17    EP 0 720 347 A2
NK17a   englische Übersetzung des Prioritätsdokuments der Europäischen Patentanmeldung NK17
NK18    WO 96/19077 A1
NK18a   Prioritätsdokument der internationalen Patentanmeldung
        zu NK18
NK19    US 4 853 681 A
NK20    Dokument „DVB subtitling system“, mit Datum 31. Oktober
        1995
NK21    WO 94/11858 A1
NK22    WO 96/03746 A1
NK23    EP 0 465 245 A2
NK24    US 5 400 077 A
NK25    EP 0 514 214 A2
NK26    JP 3-032288
NK26a   maschinelle Übersetzung des Abstracts der NK26
NK27    JP 1-241083
NK27a   maschinelle Übersetzung des Abstracts der NK27
NK28    JP 1-286682
NK28a   maschinelle Übersetzung des Abstracts der NK28
NK29    JP 3-185678

                                          - 14 -



NK29a          maschinelle Übersetzung des Abstracts der NK29
NK30           JP 3-249889
NK30a          maschinelle Übersetzung des Abstracts der NK30
NK31           D. R. Tarrant: „A new teletext decoder with advanced OSD
               features for wide screen TV“, IEEE Transactions on
               Consumer Electronics, Vol. 39, No. 3, 1993, veröffentlicht
               im August 1993
NK32           Merkmalsgliederung
NK33           Widerspruchsbegründung                   der        Patentinhaberin
               (= Nichtigkeitsbeklagte)            im         Nichtigkeitsverfahren
               5 Ni 44/14 (EP)      betreffend          das     Streitpatent    vom
               14. April 2015
NK34           Auszug aus dem Lehrbuch „Compact Disc Technology“,
               1. Ausgabe,      Heitaro    Nakajima       und     Hiroshi   Ogawa,
               Ohmsha, Ltd., 1992, ISBN 4-274-03347-3
NK35           Auszug    aus     dem      Lehrbuch       „The     Compact      Disk“,
               1. Ausgabe, Ken C. Pohlmann, A-R Editions, Inc., 1989,
               ISBN: 0-89579-234-6
NK36           Auszug aus dem Standard IEC 908:1987, „Compact disc
               digital audio system“.


Die Klägerinnen sind der Meinung, der Gegenstand des Streitpatents gehe - auch
in seiner nunmehr beschränkt verteidigten Fassung gemäß Hauptantrag - über
den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus, da
insbesondere dasjenige Merkmal des Patentanspruchs 5, das verlange, dass die
Umsteuerpositionsinformation Verzögerungslängendaten enthalte, die zur Steuerung von Verzögerungen benutzt würden, in unzulässiger Weise verallgemeinert
sei. Auch in Patentanspruch 19 seien weitere unzulässige Erweiterungen enthalten. Unzulässig erweitert sei insbesondere Merkmal 19.2, wonach das Aktualisieren der Änderungsposition einem Bewegen der Farbwischblende nach vorn entspricht. Abgesehen davon sei das Merkmal „…Bewegen der Farbwischblende
nach vorn …“ unklar.

                                       - 15 -



Da diese Merkmale auch nicht in der Prioritätsanmeldung offenbart seien, könnten
die angegriffenen Patentansprüche 5 und 19 bzw. 13 und 20 auch die Priorität der
japanischen Patentanmeldung JP 88607/95 vom 23. März 1995 nicht wirksam in
Anspruch nehmen.


Die Klägerinnen sind weiter der Auffassung, dass das Streitpatent - auch in seiner
nunmehr beschränkt verteidigten Fassung gemäß Hauptantrag - insbesondere in
Bezug auf die Druckschrift EP 0 725 541 A2 (NK6) nicht neu sei.


Die erfinderische Tätigkeit fehlt nach Meinung der Klägerinnen dem Gegenstand
von Patentanspruch 5 und 19 gegenüber dem Stand der Technik gemäß der
Druckschrift NK7 in Verbindung mit den Druckschriften NK8 bzw. NK10 oder ausgehend von der Druckschrift NK9 in Verbindung mit den Druckschriften NK10 bzw.
NK11 sowie ausgehend von der Druckschrift NK12 in Verbindung mit den Druckschriften NK10 oder NK11.


Die fehlende Patentfähigkeit der übrigen angegriffenen Patentansprüche ergebe
sich aus dem Fachwissen, den Druckschriften NK9, NK6, NK10, NK11, NK12,
NK14 und NK16 sowie weiteren Druckschriften, die auch in Verbindung mit den
Patentansprüchen 5 und 19 genannt werden.


In den Hilfsanträgen II bis VI seien die jeweiligen Gegenstände der unabhängigen
Patentansprüche nicht neu, da ihre jeweiligen Merkmale in der Druckschrift NK6
und in deren Prioritätsanmeldung offenbart seien.


Zudem enthielten auch die Patentansprüche der Hilfsanträge II bis VI unzulässige
Änderungen.


Ferner bestehen aus Sicht der Klägerin zu 1. Zweifel an der Ausführbarkeit der
streitpatentgemäßen Lehre. Nach Auffassung der Klägerin zu 2. könne außerdem
der Schutzbereich des Streitpatents in den jeweiligen Fassungen der Hilfsanträge IV bis VI infolge der Streichung eines Merkmals erweitert sein.

                                        - 16 -



Die Klägerin zu 1. stellt den Antrag,


        das europäische Patent 0 734 181 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland im Umfang seiner Ansprüche
        5 und 19 für nichtig zu erklären.


Die Klägerin zu 2. stellt den Antrag,


        das europäische Patent 0 734 181 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland im Umfang seiner Ansprüche 5, 6, 7, 13, 14, 15, 19 (soweit dieser auf einen der Ansprüche 5 – 7 rückbezogen ist) und 20 (soweit dieser auf einen der
        Ansprüche 13 – 15 rückbezogen ist) für nichtig zu erklären.


Die Beklagte erklärt, dass sie die Ansprüche gemäß Hauptantrag und Hilfsanträgen jeweils als geschlossene Anspruchssätze betrachtet und beantragt,


        unter Abweisung der Klage im Übrigen das europäische Patent
        0 734 181 mit Wirkung für das Hoheitsgebiet der Bundesrepublik
        Deutschland im Umfang seiner Ansprüche 5, 6, 7, 13, 14, 15, 19
        (soweit dieser auf einen der Ansprüche 5 – 7 rückbezogen ist)
        und 20 (soweit dieser auf einen der Ansprüche 13 – 15 rückbezogen ist) für nichtig zu erklären, soweit seine Ansprüche über
        die Fassung des Hilfsantrags I - nun Hauptantrag - hilfsweise
        über die Fassung eines der Hilfsanträge II bis VI, jeweils gem.
        Anlagen zum Schriftsatz vom 9. Dezember 2016 hinausgehen,
        wobei die Hilfsanträge in der Reihenfolge ihrer Nummerierung
        berücksichtigt werden.


Die Beklagte tritt der Argumentation der Klägerinnen in vollem Umfang entgegen.
Sie ist der Ansicht, der ursprüngliche Patentanspruch 5 offenbare in allgemeiner
Form Umsteuerpositionsinformation, die Verzögerungslängendaten enthalte. Auch

                                        - 17 -



das Merkmal 19.2, mit dem sämtliche notwendigen Informationen, nämlich das
Verzögern der Farbwischblende und die Dauer des Verzögerns, bereits beansprucht würden, sei durch den Rückbezug auf den Anspruch 5 ursprünglich offenbart. Außerdem wird u. a. auf die Beschreibung zu Fig. 10 des Prioritätsdokuments verwiesen. Das Streitpatent sei somit nicht unzulässig erweitert und könne
auch die Priorität der japanischen Voranmeldung in Anspruch nehmen.


Die Gegenstände der angegriffenen Patentansprüche seien auch patentfähig.


Die Druckschrift NK6 offenbare keine Umsteuerpositionsinformation im Sinne des
Merkmals 5.2.2, keine Farbnachschlagtabelle und auch nicht die Merkmale 5.3.,
5.4., 5.2.2.1. und 5.2.2.2.


Die Druckschrift NK7, die nach dem Prioritätsdatum des Streitpatents veröffentlicht
worden sei, offenbare keine Farbwischblendenoperation und keine hierzu einsetzbare Umsteuerpositionsinformation. Auch in Verbindung mit den Druckschriften
NK8 oder NK10 bzw. NK11 gebe es keine Veranlassung, zum Gegenstand des
Streitpatents zu gelangen. Entsprechendes gelte für die Druckschriften NK9 in
Verbindung mit den Druckschriften NK10 bzw. NK11.


Die Beklagte stützt ihr Vorbringen auf die folgenden Dokumente:


NB1                   Wikipedia-Artikel zum Begriff „colour look-up table“
NB2 (=NK1a)           EP 0 734 181 A2
NB3                   japanisches Prioritätsdokument der NK7
NB3a (=NK6a)          englische Übersetzung der NB3
NB4                   Wikipedia-Artikel zum Begriff „palette (computing)“
NB5                   Wikipedia-Artikel „Color Graphics Adapter“


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                       - 18 -



                            Entscheidungsgründe


                                         I.


Die Klagen sind zulässig und in der Sache jeweils in vollem Umfang erfolgreich.


1.   Einer Zulässigkeit der Klagen steht auch nicht das Erlöschen des Streitpatents wegen Zeitablaufs entgegen. Das insoweit erforderliche Rechtsschutzbedürfnis ergibt sich daraus, dass die Klägerinnen von der Beklagten wegen Verletzung des Streitpatents - gestützt auf dessen Ansprüche 5 und 19 - gerichtlich in
Anspruch genommen werden. Dies gilt auch in Bezug auf die lediglich von der
Klägerin zu 2. angegriffenen Ansprüche 6, 7, 13, 14 und 20 (soweit dieser auf einen der Ansprüche 13 bis 15 rückbezogen ist). Die Klägerin zu 2. hat insoweit
ausreichend dargelegt, dass sie auch im Umfang dieser Ansprüche ein schutzwürdiges Interesse an der Durchführung des Nichtigkeitsverfahrens hat. Dieses
liegt vor, wenn sie als Patentverletzer in Anspruch genommen wird oder eine solche Inanspruchnahme befürchten muss (vgl. BGH GRUR 2010, 1084, Tz. 10 -
Windenergiekonverter). Die Klägerin zu 2. hat erklärt, dass sie befürchte, dass die
Verletzungsklägerin sich auf diese bislang nicht angegriffenen Ansprüche berufe.
Vor dem Hintergrund, dass jedenfalls die Fälle eines ersichtlich fehlenden Rechtsschutzbedürfnisses für eine Klage gegen ein erloschenes Patent - wenn der Patentinhaber auf alle Ansprüche aus dem Patent verzichtet hat oder eine Inanspruchnahme aus dem Schutzrecht ernsthaft nicht in Betracht kommt (vgl. BGH
GRUR 1995, 342, 343 - Tafelförmige Elemente) auszuschließen sind, hat die Klägerin zu 2. ihr Rechtsschutzbedürfnis im vorliegenden Fall nach Ansicht des Senats im ausreichenden Umfang begründet.


2.   In der Sache erweisen sich die Klagen, mit denen u. a. der Nichtigkeitsgrund
der fehlenden Patentfähigkeit nach Artikel II § 6 Abs. 1 Nr. 1 IntPatÜG, Artikel 138
Abs. 1 lit. a) EPÜ i. V. m. Artikel 54 Abs. 1, 2 und Artikel 56 EPÜ geltend gemacht
wird, auch als begründet.

                                       - 19 -



Soweit die Beklagte das Streitpatent im Wege der zulässigen Selbstbeschränkung
nicht mehr verteidigt, war es mit Wirkung für die Bundesrepublik Deutschland
ohne Sachprüfung für nichtig zu erklären (zur st. Rspr. im Nichtigkeitsverfahren
vgl. z. B. BGH GRUR 2007, 404, 405 - Carvedilol II; Busse/Keukenschrijver, PatG,
8. Aufl., § 82 Rdn. 119 f. m. w. Nachw.; Schulte/Voit, PatG, 9. Aufl., § 81
Rdn. 128).


Auch im Übrigen sind die Klagen begründet, denn das Streitpatent hat in keiner
der nach dem Hauptantrag und der nach den Hilfsanträgen verteidigten Fassungen Bestand, da die hiermit verteidigten Gegenstände nicht patentfähig sind.


In Bezug auf die Nichtigerklärung des Patentanspruchs 19 ist klarzustellen, dass
diese sich sowohl auf diesen Patentanspruch als solchen als auch auf seine
Rückbezüge auf die Ansprüche 5 bis 7 bezieht.


Es bedarf keiner Entscheidung, ob dem Streitpatent in den nach dem Hauptantrag
und den nach den Hilfsanträgen verteidigten Fassungen auch die weiterhin geltend gemachten Nichtigkeitsgründe der unzulässigen Erweiterung (Artikel II § 6
Abs. 1 Nr. 3 IntPatÜG i. V. m. Artikel 138 Abs. 1 lit. c) EPÜ) und der Erweiterung
des Schutzbereichs des europäischen Patents (Artikel II § 6 Abs. 1 Nr. 4 IntPatÜG
i. V. m. Artikel 123 Abs. 3 EPÜ) entgegenstehen. Im Übrigen hat der erkennende
Senat keine Zweifel daran, dass das Streitpatent die Erfindung so deutlich und
vollständig offenbart, dass ein Fachmann sie ausführen kann (Artikel II § 6 Abs. 1
Nr. 2 IntPatÜG i. V. m. Artikel 83 EPÜ).




                                           II.


1.   Das Streitpatent betrifft Verfahren und Vorrichtungen zum Codieren,
Decodieren und Anzeigen von Untertiteln, die zusammen mit einem Videodatenstrom an ein Anzeigesystem übertragen werden können und Text- oder Grafik-

                                       - 20 -



elemente enthalten, welche den Videobildern bei ihrer Darstellung überlagert werden (Streitpatent, Absätze [0001], [0002]).


Insbesondere dienen solche Untertitel zur Darstellung von Textinformationen, welche z. B. die gesprochenen Inhalte aus einer Fremdsprache übersetzen. Ferner
finden Untertitel beim Karaoke Anwendung. Hierbei werden Musikstücke nur instrumental ohne ihren Gesang wiedergegeben und die Liedtexte werden parallel
dazu auf einem Bildschirm angezeigt, so dass ein Karaokesänger zur Musik singen kann. Zur Orientierung des Sängers kann die gerade zu singende Textstelle
durch eine zeitlich veränderliche Position eines Farbwechsels des Untertitels markiert werden. Die auf dem Anzeigebildschirm dargestellte Textzeile kann z. B. in
zwei aneinander anschließenden horizontalen Bereichen mit jeweils unterschiedlichen Farben dargestellt werden, und der Übergang der Farbbereiche, der im
Streitpatent auch als Änderungsposition bezeichnet wird, kann dann an der jeweils
zu singenden Textstelle positioniert werden. Hierfür wird die Übergangsposition
passend zur Musik in Textrichtung bewegt. Die Einfärbung mit der Farbe des bereits gesungenen Textes, die auch als Wischbalken bzw. Farbwischblende bezeichnet wird, schreitet im Gesangsrhythmus in Textrichtung voran, bis sie die gesamte Textzeile umfasst. Diese Funktion wird im Streitpatent als Farbwischblendenoperation bezeichnet. Der Gegenstand des Streitpatents befasst sich vor allem
damit, wie Untertiteldaten zur Durchführung solcher Farbwischblendenoperationen
codiert und decodiert werden können.


Untertiteldaten sind hierbei in der Regel zusammen mit den zu überlagernden Videodaten und gegebenenfalls vorhandenen Audiodaten in einem gemeinsamen
Datenstrom gebündelt. Dieser wird dadurch erzeugt, dass die zunächst in separaten Datenströmen vorliegenden Untertitel-, Video- und Audiodaten „gemultiplext“
werden. Der gemeinsame Datenstrom beinhaltet ein bestimmtes Muster aufeinanderfolgender Datenblöcke der verschiedenen Einzeldatenströme und kann über
einen Übertragungskanal gesendet oder auf einem Aufzeichnungsmedium gespeichert werden.

                                       - 21 -



Zur Wiedergabe extrahiert das Decodiersystem die Datenblöcke der Einzeldatenströme aus dem gemeinsamen Datenstrom. Danach werden die decodierten Untertitel den ebenfalls decodierten Videobildern überlagert, um die Videobilder und
Untertitel auf einem Anzeigebildschirm auszugeben.


2.   Ausgehend vom bekannten Stand der Technik adressiert das Streitpatent
das Problem, das erforderliche Datenvolumen der Steuerdaten zum Steuern einer
Farbwischblendenfunktion zu reduzieren und die Codierung der Steuerdaten insoweit effizienter zu gestalten. Insbesondere soll dabei das Datenvolumen verringert werden, wenn sich die Farbwischblende über eine Anzahl von Videorahmen
hinweg nicht ändert (Seite 3 des Schriftsatzes der Beklagten vom 27. März 2015
bzw. 15. Mai 2015; vgl. auch Streitpatent, Absätze [0016] sowie [0125] bis [0127]).


Als weiteren, zur Lösung dieses Problems nicht hinreichend geeigneten Stand der
Technik nennt das Streitpatent die Speicherung von Untertiteln als Bestandteil von
Videobild-Daten auf einem Medium, z. B. einer Video-Disk. Bei einer solchen Video-Disk wird das Videosignal aufgezeichnet, nachdem die Untertitel dem Videobild überlagert worden sind (Streitpatent, Absatz [0002]). Alternativ können die
Untertitel als von Videobild-Daten unabhängige Daten gespeichert werden (Streitpatent, Absätze [0003], [0004]). In diesem Fall werden die Untertitel-Daten in einem Abspielgerät decodiert und danach mittels einer Mischeinrichtung dem Videobild überlagert (Streitpatent, Absätze [0026]), [0060]). Das Streitpatent geht insbesondere von einem Stand der Technik aus, der die Speicherung von Untertitel-Daten im Format CD Graphics (CD-G) für das Decodieren und Überlagern in einem Abspielgerät beschreibt (Streitpatent, Absätze [0004], [0013]). Das Format
CD-G erweist sich für eine sich ändernde Darstellung von Untertiteln als ungeeignet, da es aufgrund langer Übertragungszeiten bei den bekannten Anzeigeverfahren unmöglich ist, die überlagerten Untertitel in ausreichend kurzer Zeit zu ändern,
um die Untertitel mit dem Videobild weiterwandern zu lassen (Streitpatent, Absätze [0016], [0021]). Als nächstliegender Stand der Technik wird im Streitpatent
die Druckschrift EP 0 662 770 A1 genannt, die zur Verwirklichung einer Farbwischblenden-operation vorschlägt, Chroma-Vektoren innerhalb der Untertitelda-

                                      - 22 -



ten zu übertragen. Dadurch, dass die Untertiteldaten durch die Verwendung eines
Chroma-Vektors für jeden einzelnen Videorahmen codiert werden, entstehen in
den Chroma- und Positionsdaten Redundanzen, wenn die Untertitel für eine
Mehrzahl von Videorahmen gleich bleiben.


Aufgrund dieser Redundanzen entsteht ein hohes Datenvolumen der in den Untertiteldaten codierten Steuerdaten, die zur Ausführung der Wischblendenfunktion
nötig sind.


3.   Die oben genannte Aufgabe soll durch die jeweiligen Vorrichtungen bzw.
Verfahren der unabhängigen Patentansprüche 5 und 13 in der Fassung von
Hauptantrag und Hilfsantrag II bis VI gelöst werden.


4.   Als zuständiger Fachmann ist ein Diplom-Ingenieur der Elektrotechnik
anzusehen, der über eine mehrjährige Berufserfahrung und einschlägige Kenntnisse in der Entwicklung von Videosystemen sowie der dazugehörigen Codierung
und Decodierung von Bild- und Toninformation verfügt.


5.   Dem Patentanspruch 5 bzw. 13 gemäß Hauptantrag lässt sich entsprechend
der Beschreibung und den Figuren 1 bis 14 des Streitpatents die folgende Lehre
entnehmen:


Unter Schutz gestellt wird mit dem unabhängigen Vorrichtungsanspruch 5 eine
Vorrichtung, die in der Lage ist, Untertitel so zu decodieren, dass sie in einem
System zur Anzeige von Videobildern verwendet werden können (Merkmal 5).
Der Patentanspruch 13 betrifft ein entsprechendes Verfahren. Da der Patentanspruch 13 inhaltlich nicht über den Patentanspruch 5 hinausgeht, wird nur der
Patentanspruch 5 abgehandelt. Die Aussagen gelten entsprechend für den Patentanspruch 13.


Gemäß Merkmal 5.1 umfasst die Vorrichtung eine Farbnachschlagtabelle mit Adressen für den Zugriff auf Anzeigedaten. Bei der Farbnachschlagtabelle handelt es

                                           - 23 -



sich um eine „Colour Look-Up Table“ („CLUT“), in der die zur Darstellung der Untertitel verwendeten Farben in codierter Form gespeichert sind und die nach fachmännischem Verständnis eine Unterauswahl aus einer größeren Menge darstellbarer Farben repräsentiert.


In den Absätzen [0058] und [0059] sowie in Figur 6 der Streitpatentschrift wird
eine solche Farbnachschlagtabelle beschrieben. Die Tabelle der Figur 6 weist eine
Adress- und eine Farbwertspalte auf und dient der Zuordnung eines Farbwerts zu
einer Adresse. Die Tabelle beruht z. B. auf der Zuordnung von Kombinationen von
Werten eines YCrCbK-Farbmodells zu einer Anzahl von Adressen. Dabei werden
die Farbwerte durch einen Luminanzparameter Y, zwei Farbdifferenzparameter Cr
und Cb und Schlüsseldaten K spezifiziert. Letztere geben ein Mischungsverhältnis
zwischen Hintergrunddaten und den Parametern Y, Cr und Cb an. Bei der Decodierung der Untertiteldaten werden die darin enthaltenen Farbadressen ausgelesen und mittels der Nachschlagtabelle in die zugehörigen Farbwertdarstellungen
der betreffenden Farben übersetzt. Farbnachschlagtabellen dienen der Reduzierung der an das Videosystem zu übertragenden Datenmenge, weil die Adresse
eines Farbeintrags der Tabelle mit weniger Bits als der Farbwert selbst darstellbar
ist. Für die Darstellung eines Pixels reicht es aus, wenn neben der Position des
Pixels die Adresse des Eintrags der Farbnachschlagtabelle bekannt ist.


Die Vorrichtung weist außerdem eine Einrichtung zum Empfangen von Datenblöcken auf, die Ladeblöcke und Pixeldatenblöcke enthalten (Merkmal 5.2). Damit ist
gemeint, dass sich der Untertiteldatenstrom entsprechend der im Streitpatent vorgesehenen Datenstruktur aus Datenblöcken zusammensetzt, in denen Pixeldatenblöcke und Ladeblöcke aneinandergefügt           sind   (Streitpatentschrift, Absätze [0091], [0092], Fig. 8A, Fig. 8B).


Gemäß Merkmal 5.2.1 repräsentieren die Pixeldatenblöcke Untertiteldaten. In Absatz [0092] der Streitpatentschrift wird hierzu ausgeführt, dass die anspruchsgemäßen Pixeldatenblöcke die grafischen Daten beinhalten, z. B. die Daten einer
Bitmap-Grafik, die die darzustellenden Untertitel beschreibt. Beispielsweise wer-

                                        - 24 -



den die Farben jedes Pixels der Bitmap mit vier Bit codiert, die dann als Adresse
für den Zugriff auf die Farbnachschlagtabelle verwendet werden (Streitpatentschrift, Absatz [0084]).


Merkmal 5.2.2 besagt, dass die Ladeblöcke eine Umsteuerpositionsinformation
(„changeover position information“) beinhalten, mit deren Hilfe Farbwechsel an Pixeln gesteuert werden. Der Begriff „Umsteuern“ („changeover“) bedeutet im Streitpatent, dass auf eine andere Farbe in der Farbnachschlagtabelle zugegriffen wird
(Streitpatentschrift, Absatz [0122]), was wiederum eine Farbänderung an einer bestimmten Stelle des Untertitels, der „Änderungsposition“ („change position“) hervorruft (Streitpatentschrift, Absatz [0094]). Insbesondere soll die Umsteuerpositionsinformation Farbwischblendenoperationen steuern, indem das Fortschreiten
der Position des Farbwechsels an einer Wischblende sowie dessen Verzögerung
bestimmt werden. Durch diese Information wird die Farbwischblende sowohl in
örtlicher als auch zeitlicher Hinsicht festgelegt, und die Änderungsposition ergibt
sich aus der horizontalen Position innerhalb der Untertitelgrafik, an der die Farbwischblende aktuell endet und sich die Farbe der Untertitel ändert. Zur Steuerung
dieses Vorgangs wird die Umsteuerpositionsinformation genutzt, die an anderer
Stelle des Streitpatents auch Umsteuerinformation („changeover information“) genannt wird (Streitpatentschrift, Absatz [0093]). Zu diesem Zweck enthält im Ausführungsbeispiel des Streitpatents ein Ladeblock als Umschaltinformation ein P-Bit
(„progressing bit“) sowie ein H-Bit („holding bit“). Während das P-Bit zur Aktualisierung der Änderungsposition benutzt wird, gibt das H-Bit an, ob die Position der
Farbänderung über eine gewisse Anzahl von (Video-)Rahmen („frames“) des Videobilds unverändert bleibt oder nicht. Die Anzahl dieser Rahmen ist in weiteren
Bits („frame count value bits“) des Ladeblocks codiert (Streitpatentschrift, Absätze [0093], [0094]). Die Umsteuerpositionsinformation ist damit durch P-Bit, H-Bit und Videorahmenanzahl gegeben.


Merkmal 5.2.2.1 besagt, dass mittels der Umsteuerpositionsinformation eine in
dem Videobild liegende Änderungsposition aktualisiert wird, d. h. anhand der in
den Ladeblöcken enthaltenen Umsteuerpositionsinformation wird an einer Position

                                      - 25 -



des Untertitels ein Farbwechsel erzeugt bzw. im Fall einer Farbwischblende ein
Fortschreiten der Position des Farbwechsels ausgelöst.


Laut Merkmal 5.2.2.2 kann eine aktuelle Adresse für den Zugriff auf die Farbnachschlagtabelle in jeder Videorahmenperiode in eine nächste Adresse verändert
werden, so dass an der durch die Umsteuerpositionsinformation angegebenen
Änderungsposition auf unterschiedliche Anzeigedaten zugegriffen wird. Die Adresse für den Zugriff auf die CLUT kann somit in jeder Rahmenperiode verändert
werden, so dass die möglichen Farbwechsel mit der Periode der Videorahmen
(frames) synchronisiert werden können, d. h. die Farbwechsel können mit derselben Geschwindigkeit stattfinden, mit der die einzelnen Videorahmen erscheinen.
Dabei entspricht eine Rahmenperiode der Anzeigedauer eines (einzigen) Videorahmens des von den Untertiteln überlagerten Videosignals.


Weiterhin sind in der Umsteuerpositionsinformation Verzögerungslängendaten
(„delay length data“) enthalten. Die anspruchsgemäßen Verzögerungslängendaten
dienen dazu, die Verzögerung bei der Aktualisierung der Änderungsposition zu
steuern. Soll sich die Position des Farbwechsels bzw. die Farbwischblende über
mehrere Videorahmen nicht ändern, d. h. soll sich die gleiche Umsteuerinformation („CLUT changeover information“) über mehrere Rahmen fortsetzen, so wird
dies durch die Berücksichtigung von Verzögerungslängendaten bewerkstelligt, die
eine Zeitdauer festlegen, wie lange die Änderungsposition im Untertitel erhalten
bleibt (Merkmal 5.2.2.3´).


Merkmal 5.3 sieht vor, dass die beanspruchte Vorrichtung über eine Einrichtung
verfügt, mit der die Umsteuerpositionsinformation aus den Ladeblöcken erfasst
werden kann. In Absatz [0114] der Streitpatentschrift wird hierzu ausgeführt, dass
die Ladeblöcke in ein Register eingelesen und die P- und H-Bits detektiert werden.


Außerdem umfasst die Vorrichtung noch eine Einrichtung, mit der die Untertitel
und das Videobild auf einem Bildschirm angezeigt werden. Die Anzeige erfolgt in

                                      - 26 -



Abhängigkeit von der Umsteuerpositionsinformation und der Farbnachschlagtabelle (Merkmal 5.4).


Aus den Absätzen [0060] und [0033] der Streitpatentschrift geht hervor, dass die
dem Videobild mittels einer Mischeinrichtung überlagerten Untertitel auf einem
externen Bildschirm angezeigt werden. Die Untertitel werden wiederum mit der
Farbwischblendeninformation vermischt (Streitpatentschrift, Absatz [0097]).


6.   Erläuterungsbedürftig in Hinblick auf Merkmal 5.2.2.3´ bzw. 13.2.2.3´ ist
insbesondere die Bedeutung des Begriffs „Verzögerungslängendaten“ („delay
length data“):


Gemäß Merkmal 5.2.2.3´ des Patentanspruchs 5 gemäß Hauptantrag sind unter
den Verzögerungslängendaten Daten zu verstehen, die eine Verzögerungslänge
enthalten und die zur Steuerung der Verzögerung bei der Aktualisierung der Änderungsposition benutzt werden und dazu dienen, eine Länge der Verzögerung, also
eine Verzögerungsdauer festzulegen, wenn sich die gleiche Umsteuerinformation
über mehrere Rahmen fortsetzt. Bei Berücksichtigung des Ausführungsbeispiels
des Streitpatents ist die Verzögerungslänge derart auszulegen, dass sie auch
durch eine Anzahl von Videorahmen bzw. einen Rahmenzählwert („frame count
value“) beschrieben werden kann, der eine Verzögerungsdauer, also eine Zeitspanne repräsentiert. Der Begriff Verzögerungslänge ist aber nicht allein auf dieses Ausführungsbeispiel beschränkt. Da der Patentanspruch 5 nicht ausschließt,
dass die Umsteuerpositionsinformation zusätzliche Angaben wie etwa Zeitpunkte
oder Videorahmennummern enthält, können die Verzögerungslängendaten jegliche Daten beinhalten, welche zur Angabe von Zeiten dienen, zu denen neue Positionen des Farbwechsels im Untertitel eingenommen werden. Demnach ist durch
die Verzögerungslängendaten eine Zeitsteuerung mit umfasst, bei der die Verzögerungsdauer nicht explizit festgesetzt wird, sondern lediglich absolute Zeitpunkte
vorgegeben sind, an denen sich der Farbwechsel an vorbestimmten Positionen
befindet. Unter die anspruchsgemäßen Verzögerungslängendaten fallen daher
grundsätzlich alle Startzeit-Informationen, die die jeweiligen Zeitpunkte zur Aus-

                                       - 27 -



führung beliebiger Untertitel-Steuer-Sequenzen festlegen und aus denen sich implizit die Länge einer Verzögerung ergibt.


Mit anderen Worten: zur Verzögerung können in gleichwirkender Weise sowohl
eine Verzögerungslänge als auch absolute Zeitangaben verwendet werden, die
implizit eine Verzögerungslänge angeben.


7.   Im Patentanspruch 5 bzw. 13 gemäß Hilfsantrag II wird die Umsteuerposition durch den Merkmalskomplex 5.5´ bzw. 13.5´ dahingehend konkretisiert, dass
sie eine Farbwischblendeninformation umfasst und eine Aktualisierung der Änderungsposition einer Bewegung der Farbwischblende nach vorn entspricht. Auf
Grundlage der Farbwischblendeninformation wird die Farbwischblende in Vorwärtsrichtung bewegt, um Untertitel abzuschatten. Die Verzögerungslängendaten
dienen dazu, eine Verzögerung der Farbwischblende zu steuern und eine Verzögerungsdauer festzulegen. Der Fachmann wird im Merkmalskomplex 5.5´ bzw.
13.5´ im Wesentlichen die Wirkung der durch die Umsteuerpositionsinformation
verursachten Zeitsteuerung erkennen, durch die sich für einen Betrachter eine
Farbwischblende in den Videorahmen in einer Vorwärtsrichtung von links nach
rechts bewegt, so dass die Untertitel allmählich eingefärbt werden.


Der Patentanspruch 5 bzw. 13 gemäß Hilfsantrag IV ist gegenüber dem Patentanspruch 5 bzw. 13 gemäß Hauptantrag dahingehend eingeschränkt, dass
die Verzögerungslängendaten dazu benutzt werden, die Aktualisierung der Änderungsposition zu verzögern, d. i. eine Verzögerung auszulösen, und zugleich eine
Länge dieser Verzögerung festzulegen (Merkmal 5.2.2.3´´ bzw. 13.2.2.3´´).


Dementsprechend sollen die im Merkmalskomplex 5.5´´ bzw. 13.5´´ des Patentanspruchs 5 bzw. 13 gemäß Hilfsantrag V enthaltenen Verzögerungslängendaten das Fortschreiten der Farbwischblende verzögern („wherein said delay
length data are used to delay said colour wipe“), d. i. eine solche Verzögerung
auslösen, anstelle zur Verzögerung der Farbwischblende lediglich beizutragen (d.
i. die Verzögerung zu „steuern“ - vgl. Merkmalskomplex 5.5´ bzw. 13.5´).

                                       - 28 -



8.   Wirksamkeit des Prioritätsanspruchs


8.1 Merkmal 5.2.2.3´ des jeweiligen Patentanspruchs 5 gemäß Hauptantrag
und Hilfsantrag II sowie Merkmal 13.2.2.3´ des jeweiligen Patentanspruchs 13
gemäß Hauptantrag und Hilfsantrag II und III gehen aus den Prioritätsunterlagen
zum Streitpatent nicht unmittelbar und eindeutig hervor.


Aus den Prioritätsunterlagen zum Streitpatent (Anlage NK1b) konnte der Fachmann nicht die allgemeine Lehre entnehmen, dass Verzögerungslängendaten
vorgesehen sind, die zur Steuerung der Verzögerung bei der Aktualisierung von
Änderungspositionen benutzt werden („used to control a delay in the update of the
change position“) und dazu dienen, eine Länge der Verzögerung festzulegen („and
further being used to set a length of said delay“). So ergibt die Auslegung des Begriffs Verzögerungslängendaten, dass die Merkmale 5.2.2.3´ und 13.2.2.3´ eine
Steuerung der Farbwechsel durch die Angabe von Zeitpunkten mit umfassen. An
der Stelle des Prioritätsdokuments, die eine Verzögerung des Einfärbens betrifft,
wird eine Steuerung mit P-Bit, H-Bit und Rahmenzählwert (Seite 34, letzter Absatz
bis Seite 35, erster Absatz; Figuren 9 und 10 mit Beschreibung) präsentiert, die
sich jedoch deutlich von einer Steuerung mit Zeitpunkten unterscheidet, nicht
gleichwirkend mit einer solchen ist und keinen Hinweis auf eine Derartiges einschließende Verallgemeinerung gibt. So werden sich im Fall einer Zeitsteuerung
gemäß dem Ausführungsbeispiel eine fehlerhafte Codierung oder eine fehlerhafte
Übertragung der Steuerdaten immer so auswirken, dass die gesamten Farbwechsel (bzw. die gesamte Farbwischblende) ab einer falschen Verzögerung falsch
ablaufen. Demgegenüber würde sich eine durch absolute Zeitpunkte gesteuerte
Farbwischblende als weniger fehleranfällig erweisen, weil die fehlerhafte Codierung einer einzelnen absoluten Zeitangabe keinen Einfluss auf die nachfolgenden
absoluten Zeitangaben hat, die die Farbwechsel bzw. Farbwischblende somit
weiterhin richtig steuern.


Die Beklagte argumentiert, dass auf Seite 35 des Prioritätsdokuments zwar insbesondere auf das H-Bit und den Rahmenzählwert Bezug genommen werde, jedoch

                                      - 29 -



werde hier das H-Bit funktional als ein Mittel zur Steuerung der Aktualisierung von
Änderungspositionen offenbart, wenn sich dieselbe Umsteuerinformation über
mehrere Videorahmen erstrecke. Der Fachmann erkenne daraus, dass auch andere Daten für diesen Zweck eingesetzt werden könnten. Diese Auffassung werde
auch durch die Beschreibung der Figur 10 des Prioritätsdokuments gestützt. Dieser Offenbarung entnehme der Fachmann, dass es darum gehe, die für das Fortschreiten der Farbwischblende relevanten Zeitpunkte durch Steuerdaten geeignet
zu definieren, ohne dass es darauf ankomme, dass dies mittels des H-Bits bewerkstelligt werde. Der Fachmann erkenne daher, dass die im Prioritätsdokument
offenbarte Erfindung nicht auf Verzögerungslängendaten beschränkt sei, die das
H-Bit enthielten.


Der Einwand der Beklagten vermag nicht zu überzeugen. In den Patentansprüchen des Prioritätsdokuments NK1b ist lediglich Farbwischen („color wipe“) in allgemeiner Form angesprochen, eine Verzögerung ist nicht erkennbar. Verzögerung
im Zusammenhang mit einer Farbnachschlagtabelle ist nur aus den Figuren 8 bis
12 mit der zugehörigen Beschreibung zu entnehmen. Gemäß Seite 34, letzter
Absatz bis Seite 35, erster Absatz weist der Ladeblock Folgendes auf: ein P-Bit,
welches eine aktualisierte Änderungsposition für den Zugriff auf die Farbnachschlagtabelle (CLUT) anzeigt, ein H-Bit zur Steuerung der Aktualisierung der
Änderungsposition im nächsten Rahmen, wenn dieselbe CLUT-Änderungsposition
sich für eine Mehrzahl von Rahmen fortsetzt, und einen Rahmenzählwert von 10
Bit, der die Anzahl fortlaufender Rahmen im obigen Fall angibt. Wie aus der Beschreibung zu den Figuren 9 und 10 hervorgeht, ist das H-Bit nur dann gesetzt,
wenn für eine Mehrzahl von Rahmen keine Änderung erfolgen soll; dadurch wird
(nach der Änderung im ersten Rahmen) in Verbindung mit dem Rahmenzählwert
das Rahmenherunterzählen im Zähler 202 und das Anhalten des Farbwischens in
der zugehörigen Zeitspanne (also eine Verzögerung) ermöglicht (Fig. 11 mit Beschreibung).


Damit ist eine Ausführung offenbart mit einem H-Bit und einem Rahmenzählwert,
denen spezielle Aufgaben zugewiesen sind. Nach Überzeugung des Senats

                                      - 30 -



konnte der Fachmann dieser speziellen Ausführungsform daher nicht unmittelbar
und eindeutig die allgemeine Lehre entnehmen, dass Verzögerungslängendaten
vorgesehen sind, die zur Steuerung der Verzögerung bei der Aktualisierung der
Änderungsposition benutzt werden (Merkmale 5.2.2.3´ und 13.2.2.3´), zumal den
Prioritätsunterlagen kein Hinweis auf eine allgemeinere Lehre zu entnehmen ist,
die z. B. auch eine auf absoluten Zeitangaben beruhende Steuerung der Farbwechsel beinhaltet (vgl. BGH GRUR 2014, 542-545 - Kommunikationskanal (Leitsatz und III.1.a) bis c)) oder BGH, Urteil vom 19. Mai 2015 - X ZR 48/13 (Orientierungssatz 1 und 2 in Juris)).


Die für die Inanspruchnahme einer Priorität erforderlichen Voraussetzungen in
Bezug auf die Merkmale 5.2.2.3´ und 13.2.2.3´ sind damit nicht erfüllt. Dementsprechend ist die Priorität für den jeweiligen Patentanspruch 5 gemäß Hauptantrag und Hilfsantrag II nicht wirksam. Entsprechendes gilt für die nebengeordneten Patentansprüche 13 gemäß Hauptantrag sowie Hilfsantrag II und III.


8.2 Auch die Merkmale 5.2.2.3´´ und 13.2.2.3´´ sind in den Prioritätsunterlagen
nicht offenbart.


In den Merkmalen 5.2.2.3´´ und 13.2.2.3´´ ist das Teilmerkmal „said delay length
data being used to delay the update of the change position and further being used
to set a length of said delay“ derart auszulegen, dass Daten (“delay length data”)
vorhanden sind, die sowohl zum Auslösen der Verzögerung als auch zum Einstellen der Verzögerungslänge verwendet werden; d. h. es sind Daten vorhanden,
die eine „Doppelfunktion“ (Auslösen einer Verzögerung und Einstellen der Verzögerungslänge) ausüben. Daten mit einer solchen „Doppelfunktion“ sind aber in den
Prioritätsunterlagen nicht zu erkennen. Vielmehr werden für das Auslösen einer
Verzögerung und dem Einstellen einer Verzögerungslänge getrennte Daten verwendet, nämlich das H-Bit und der Rahmenzählwert („frame count value“). Dies
folgt insbesondere aus Seite 35, erster Absatz und den Figuren 9 und 10 des Prioritätsdokuments. In den Prioritätsunterlagen treten das P-Bit, das H-Bit und der
Rahmenzählwert jeweils gemeinsam auf (Seite 34, letzter Absatz bis Seite 35,

                                        - 31 -



erster Absatz; Fig. 9). Ein Zusammenfassen des H-Bits und des Rahmenzählwerts
zu Verzögerungslängendaten, die sowohl zum Auslösen einer Verzögerung als
auch zum Einstellen einer Verzögerungslänge angewendet werden, konnte der
Fachmann dem Prioritätsdokument nicht unmittelbar und eindeutig entnehmen.


Im Übrigen gelten die Ausführungen unter Abschnitt 8.1 für die Merkmale 5.2.2.3´´
und 13.2.2.3´´ in gleicher Weise.


Damit kann die Priorität auch für den jeweiligen Patentanspruch 5 gemäß Hilfsantrag IV und V sowie für den jeweiligen Patentanspruch 13 gemäß Hilfsantrag IV
bis VI nicht in Anspruch genommen werden.




                                          III.


Die jeweiligen Gegenstände des Patentanspruchs 5 gemäß Hauptantrag und
Hilfsantrag IV sind nicht neu, und die jeweiligen Gegenstände des Patentanspruchs 5 gemäß Hilfsantrag II und V sowie die jeweiligen Gegenstände des Patentanspruchs 13 gemäß Hilfsantrag III und VI beruhen gegenüber dem Stand
der Technik nicht auf erfinderischer Tätigkeit (Artikel 138 Abs. 1 lit. a) EPÜ i. V. m.
Artikel 54 und Artikel 56 EPÜ, Artikel II § 6 Abs. 1 Nr. 1 IntPatÜG).


1.   Zu Hauptantrag und Hilfsantrag IV


Das Streitpatent kann in den jeweiligen nach dem Hauptantrag und Hilfsantrag IV verteidigten Fassungen keinen Bestand haben, da die jeweiligen Gegenstände ihrer Patentansprüche 5 und 13 mangels Neuheit nicht patentfähig sind.


1.1 Von besonderer Bedeutung ist die Druckschrift NK6 („Image information encoding/decoding system“), die als nächstkommender Stand der Technik anzusehen ist.

                                       - 32 -



Die Druckschrift NK6 wurde am 7. August 1996 veröffentlicht. Bei ihr handelt es
sich um eine europäische Patentanmeldung, die am 2. Februar 1996 eingereicht
wurde und die Deutschland als Bestimmungsland benennt.


Diese Anmeldung beansprucht die Priorität einer japanischen Patentanmeldung
mit Anmeldedatum vom 3. Februar 1995 (englische Übersetzung in der Anlage
NK6a), also noch vor dem Prioritätsdatum des Streitpatents (23. März1995). Bei
all den Textpassagen der Druckschrift NK6, auf die im weiteren Verlauf Bezug genommen wird, handelt es sich um nachveröffentlichten Stand der Technik für das
Streitpatent gemäß Artikel 54 Abs. 3 EPÜ, da deren Inhalte bereits in der prioritätsbegründenden Druckschrift NK6a offenbart sind.


1.2 Gegenüber diesem Stand der Technik sind die jeweiligen Gegenstände des
Patentanspruchs 5 gemäß Hauptantrag und Hilfsantrag IV nicht neu.


1.2.1 Die Druckschrift NK6 führt den Fachmann zu einer Vorrichtung zum Decodieren von Untertiteln, die in einem Videobild-Anzeigesystem verwendet werden
kann.


Bei der bekannten Vorrichtung handelt es sich um ein Wiedergabesystem („playback system“), welches mit einem Untertitel-Prozessor („sub-picture processor“)
ausgestattet ist (Spalte 1, Zeilen 1 bis 17; Spalte 38, Zeilen 20 bis 25; Spalte 38,
Zeilen 7 bis 14; Spalte 38, Zeile 57 bis Spalte 39, Zeile 2; vgl. NK6a: Absätze [0001], [0002], [0031], [0036]). Ein Decoder für Untertiteldaten ist in der Figur 11 der Druckschrift NK6 wiedergegeben (vgl. NK6a: Absätze [0035], [0036]).
Damit geht Merkmal 5 des Patentanspruchs 5 aus der Druckschrift NK6 hervor.


Die Ausführung der Bilddecodierung wird in den Flussdiagrammen der Figuren 15
und 16 dargestellt. In Spalte 29, Zeile 25 bis Spalte 30, Zeile 50 der Druckschrift
NK6 wird die Decodierverarbeitung beschrieben. Insbesondere wird hier ausgeführt, dass der Mikrocomputer zunächst den Header der lauflängenkomprimierten
Überlagerungsbilddaten lädt (Pixeldaten haben dabei eine 2-Bit-Konfiguration) und

                                      - 33 -



dessen Inhalt analysiert (Spalte 29, Zeilen 25 bis 36). Weiterhin wird darauf hingewiesen (Spalte 30, Zeilen 42 bis 45), dass in der beschriebenen Ausführungsform die Pixelfarbinformation („pixel color information“) Farbinformationsstücke
dreier Farben aufweist, die z. B. aus einer 16-farbigen Farbpalette ausgewählt
werden.


Der Fachmann wird eine solche Farbpalette als Farbnachschlagtabelle bzw. „Colour Look-Up Table“ („CLUT“) auslegen, bei der die Farbinformation eines Pixels
durch die Adresse einer Farbe einer Farbpalette gegeben ist. Damit umfasst die
aus der Druckschrift NK6 bekannte Dekodiervorrichtung eine Farbnachschlagtabelle in Gestalt einer Farbpalette, mit der den Pixeldaten Farbwerte zugeordnet
werden können. Laut Figur 39 und Spalte 43, Zeilen 26 bis 53 der Druckschrift
NK6 sind dabei den vier definierten Pixeltypen „EMPH. PIX. 2“, „EMPH. PIX. 1“,
„PATTERN PIX.“ und „BACKGND PIX.“ - diese entsprechen den aus der DVD
Spezifikation bekannten Pixeltypen „Emphasis 2“, „Emphasis 1“, „Pattern“ und
„Background“ - bestimmte darzustellende „color codes“ für Farben zugeordnet. Die
Zuordnung erfolgt durch den Befehl SET_COLOR, der die Startfarbe der vier verschiedenen Pixeltypen für alle horizontalen Zeilen der Anzeigefläche festlegt. Die
4-Bit-wertigen „color codes“ fungieren dabei als die Adressen einer Farbnachschlagtabelle, die den Zugriff auf Anzeigedaten, d. h. auf Farbwerte erlauben. Eine
solche Farbindizierung geht auch aus der Figur 11 in Verbindung mit den Absätzen [0059] und [0060] der Druckschrift NK6a hervor, in der die Farbwerte („color
data“) durch einen 4-Bit-wertigen „palette code“ referenziert werden und in einem
Farbregister („color register“) hinterlegt werden. Nach allem ist auch Merkmal 5.1
im System der Druckschrift NK6 bzw. NK6a verwirklicht.


Der Untertitel-Prozessor („sub-picture processor“) aus den Figuren 11 und 17 decodiert die Untertitel-Daten-Pakete („sub-picture data packets“), die er z. B. von
einer optischen Platte oder einem Rundfunksender empfangen hat (Spalte 39,
Zeilen 8 bis 13; vgl. NK6a: Absatz [0036]). Die Untertitel-Daten-Pakete weisen
u. a. Untertitel-Content-Daten („sub-picture content data“) und Untertitel-Steuerungs-Daten („display control sequence table“ bzw. eine Untertitel-Steuer-Se-

                                       - 34 -



quenz-Tabelle 33) auf (Spalte 38, Zeilen 15 bis 19; Fig. 29; vgl. NK6a: Fig. 1
bis 3). Die Untertitel-Steuerungs-Daten beinhalten mehrere Untertitel-Steuer-Sequenzen DCSQT. Jede DCSQT besteht laut Figur 29 aus einer Startzeit-Information für die Steuerbefehle dieser Sequenz SPDCTS, einer Startadresse der
nächsten Untertitel-Steuer-Sequenz SPNDCSQA sowie verschiedenen Steuerbefehlen („COMMAND“) für die Anzeige der Untertitel, z. B. Angabe von Farbe und
Position (Spalte 38, Zeilen 39 bis 49; vgl. NK6a: Fig. 2, Absatz [0030]). Damit repräsentieren die in den Untertitel-Daten-Paketen enthaltenen Untertitel-Steuerungs-Daten Ladeblöcke i. S. d. Streitpatents. Bei den Untertitel-Content-Daten
handelt es sich hingegen um die Pixel-Daten (Spalte 41, Zeilen 29 bis 40; Fig. 50;
vgl. NK6a: Fig. 2, siehe „PXD Area“). Die Merkmale 5.2 und 5.2.1 des Streitpatents sind somit in der Druckschrift NK6 offenbart.


Die Merkmale 5.2.2 und 5.2.2.1 bis 5.2.2.3´ bzw. 5.2.2.3´´ betreffen die Zeitsteuerung des Farbwechsels an der Änderungsposition. Auch diese ergeben sich aus
der Druckschrift NK6.


Zu den obigen Steuerbefehlen für die Anzeige der Untertitel-Content-Daten gehören insbesondere die Befehle SET_COLOR und CHG_COLCON (Spalte 43, Zeilen 36 bis 53; Spalte 44, Zeilen 21 bis 25; Fig. 34). Der Befehl SET_COLOR legt
eine Startfarbe der Pixeltypen für alle Zeilen fest (Spalte 43, Zeilen 36 bis 44).
Demgegenüber wird durch den Befehl CHG_COLCON nicht die Ausgangsfarbe
einer jeden Zeile sondern deren Farbänderung bestimmt. Er findet Verwendung,
wenn sich während der Wiedergabe die Farbe einzelner Pixel in einer Zeile ändern soll (Spalte 44, Zeilen 21 bis 25; vgl. NK6a: Fig. 8). Der Befehl
CHG_COLCON enthält als Steuerinformation Pixel-Steuerungs-Daten („pixel control data“; PCD) (Spalte 44, Zeilen 26 bis 27; vgl. NK6a: Absatz [0064], Fig. 15).
Die in den „pixel control data“ enthaltene Zeilen-Steuer-Information („line control
information“ LCINF) gibt diejenige Anfangs- und Endzeile an, an deren dazwischen liegenden Zeilen eine oder mehrere Änderungen vorgenommen werden
(Spalte 44, Zeilen 39 bis 42; Fig. 46; „change start line number“ und „change termination line number“). Eine Anzahl von Positionen für Farbänderungen („number

                                       - 35 -



of changes“ bzw. „change point count“), die innerhalb der betreffenden Zeilen
gleichmäßig verteilt sind, wird ebenfalls mit angegeben (Spalte 44, Zeilen 39 bis
42; Fig. 46). In der Pixel-Steuer-Information („pixel control information“ PCINF)
wird dann die horizontale Position zwischen Anfangs- und Endzeile festgelegt, ab
der eine Farbänderung beginnen soll, sowie der Inhalt der Änderung. Hierzu wird
für jeden Pixeltyp in der Farbänderungsposition ein neuer Farbcode bzw. eine
neue Zuweisung zu einer Farbpalette angegeben, die die neu anzuwendenden
Farben bestimmen (Spalte 44, Zeilen 51 bis 57; Fig. 47).


Die beschriebenen Einzelheiten der „pixel control data“ gehen ebenfalls aus der
Druckschrift NK6a hervor (Absätze [0065] bis [0071]; Fig. 16 bis 18). Der Fachmann liest in der Druckschrift NK6 bzw. Nk6a mit (vgl. Spalte 44, Zeilen 43 bis 50;
Nk6a: Absatz [0066]), dass die Zeilen-Steuer-Information LCINF so eingestellt
werden kann, dass ein ganzer Untertitel bzw. Anzeigebereich für Untertitel-Content-Daten von Farbwechseln an bestimmten (horizontalen) Farbänderungspositionen erfasst wird.
Mit anderen Worten: die Anfangszeile der Änderung in der LCINF kann gleich der
obersten Zeile eines Untertitels, und die Endzeile der Änderung in der LCINF kann
gleich der untersten Zeile des Untertitels gesetzt werden.


Der Steuerbefehl CHG_COLCON repräsentiert zusammen mit der Zeilen- und Pixel-Steuer-Information LCINF und PCINF eine Umsteuerpositions- bzw. Umsteuerinformation, die einen Farbwechsel an einer horizontalen Position innerhalb des
durch LCINF festgelegten Zeilenbereichs hervorruft (Merkmal 5.2.2).


Die Druckschrift NK6 offenbart nicht nur allgemein eine Abfolge von Steuersequenzen DCSQT, wobei jede Steuersequenz zu einem durch einen Zeitstempel
definierten Zeitpunkt („sub-picture display control time stamp“ SPDCTS) ausgeführt wird (Fig. 29; Spalte 38, Zeilen 50 bis 56; Spalte 40, Zeilen 42 bis 46), sie
zeigt insbesondere, dass CHG_COLCON-Befehle mehrfach hintereinander ausgeführt werden können („… the parameters (LCINF, PCINF) of pixel control data
PCD … are held in the internal registers …, unless command CHG_COLCON …

                                       - 36 -



is executed again.“; Spalte 45, Zeilen 41 bis 57; vgl. NK6a: Absatz [0073]), so
dass z. B. die einmal gesetzten Parameter eines CHG_COLCON-Befehls durch
ein erneutes Ausführen eines weiteren CHG_COLCON-Befehls überschrieben
werden können. Dies bedeutet aber gleichzeitig, dass die Umsteuerpositionsinformationen LCINF und PCINF geändert und damit auch Farbänderungspositionen mit der Zeit aktualisiert werden können (Merkmal 5.2.2.1). Da die Druckschrift
NK6 darüberhinaus offenbart, dass die Untertitel-Content-Daten dynamisch angezeigt und dass eine Farbänderung in den Untertitel-Daten in Einheiten von Pixeln
eingestellt wird (Spalte 5, Zeilen 3 bis 11; vgl. NK6a: Absatz [0023]) ergibt sich
zwingend, dass die aus der Druckschrift NK6 bekannte Vorrichtung bzw. der zugehörige Decoder so ausgelegt sind, dass das zeitliche Fortschreiten einer Farbänderung im Untertitel-Anzeigebereich bzw. das einer Änderungsposition wiedergegeben werden kann, wenn entsprechend codierte Untertitel-Daten bereitgestellt
und verarbeitet werden.


Gemäß der Druckschrift NK6 werden die Steuerungs-Sequenzen in jedem Videorahmen entsprechend dem Zeitstempel SPDCTS verarbeitet (Spalte 42, Zeilen 26
bis 37; Spalte 39, Zeilen 25 bis 35; Spalte 44, Zeile 58 bis Spalte 45, Zeile 2; vgl.
NK6a: Absätze [0025]; [0052] bis [0054]; [0039]). Damit kann in jeder Videorahmenperiode wenigstens ein Steuerbefehl, z. B. der CHG_COLCON-Befehl ausgeführt werden. In Verbindung mit der „pixel control information“ PCINF bewirkt
der Befehl CHG_COLCON, dass für eine Farbänderung für jeden Pixel-Typ ab einer bestimmten Stelle („change start pixel“) eine andere Farbe aus der Farbpalette
verwendet werden kann (Spalte 44, Zeilen 51 bis 57; Fig. 47; vgl. NK6a: Fig. 15,
Fig. 17, Absatz [0067]). Merkmal 5.2.2.2 ist demnach aus der Druckschrift NK6
bekannt.


In Spalte 45, Zeilen 41 bis 57 der Druckschrift NK6 (vgl. NK6a: Absätze [0060],
[0073]) wird ausgeführt, dass die Parameter eines Steuerbefehls so lange in Registern des Untertitel-Prozessors festgehalten werden, bis sie von einem Befehl
des gleichen Typs überschrieben werden. Wenn also kein weiterer Befehl aufgrund seines Zeitstempels SPDCTS zur Ausführung kommt, bleibt der bereits

                                       - 37 -



ausgeführte Befehl bestehen. Die Ausführung eines neuen Befehls wird verzögert.
Insbesondere gilt dies für den Steuerbefehl CHG_COLCON, so dass sich die Pixel-Steuerungs-Daten PCD - also die Umsteuerinformation - über mehrere Videorahmen fortsetzen. Versteht man unter den beanspruchten Verzögerungslängendaten alle zeitbezogenen Daten, die auf irgendeine Weise zur Zeitsteuerung des
Farbwechsels beitragen und eine Verzögerungslänge festlegen, so stellen auch
die Zeitstempel SPDCTS der Steuersequenzen DCSQT Verzögerungslängendaten dar, da sich aus ihnen jederzeit Verzögerungslängen bestimmen lassen
(Merkmal 5.2.2.3´).


Darüberhinaus wird für die Aktualisierung einer Änderungsposition immer dann
eine Verzögerung zu einem Zeitstempel SPDCTS ausgelöst, wenn in der zugehörigen Steuersequenz kein neuer CHG_COLCON Befehl enthalten ist, der zur
Ausführung kommen kann (Merkmal 5.2.2.3´´).


Weiterhin werden die bereitgestellten Untertitel-Daten-Pakete in einem Puffer zwischengespeichert (Spalte 39, Zeilen 17 bis 20, Fig. 11, siehe „buffer 121“; vgl.
NK6a: Absatz [0036]), und die darin enthaltenen Untertitel-Content-Daten und
Untertitel-Steuerungs-Daten (Fig. 29; Spalte 38, Zeilen 15 bis 19; NK6a: Fig. 2,
Absatz [0030]) werden aus den Daten-Paketen eingelesen (Merkmal 5.3).


Das aus der Druckschrift NK6 bekannte Wiedergabesystem (Spalte 1, Zeilen 3
bis 6; Spalte 1, Zeilen 13 bis 17; vgl. NK6a: Absätze [0001], [0002]) verfügt naturgemäß über Mittel zum Anzeigen der Untertitel und des Videobildes. Im Übrigen
weist Figur 23 der Druckschrift NK6 (vgl. NK6a: Fig. 20, Fig. 21) auf die Verwendung eines Computers hin. Dieser umfasst gewöhnlich Ein- und Ausgabegeräte,
wie z. B. Tastatur und Display (Merkmal 5.4).


1.2.2 Der Einwand der Beklagten, die Druckschrift NK6 offenbare keine Farbnachschlagtabelle, greift nicht durch. Vielmehr wird der Fachmann die aus der Druckschrift NK6 bekannte „16-color palette“ (Spalte 30, Zeilen 42 bis 50) als Farbnachschlagtabelle verstehen, in der bestimmten Farbcodes („color codes“) bzw.

                                        - 38 -



Farbadressen bestimmte Farbwerte bzw. Anzeigedaten zugeordnet werden. Eine
solche Farbnachschlagtabelle folgt auch aus der Druckschrift NK6a, wo in den Figuren 11 und 17 von „palette codes“, d. h. von Codes einer Farbpalette gesprochen wird. Bei der Farbpalette handelt es sich hierbei um eine Datenstruktur mit
indizierten Farben. Dass es sich bei den Farbpaletten der Druckschriften NK6 und
NK6a darüber hinaus um eine Unterauswahl aus einer größeren Menge darstellbarer Farben handeln muss (im Sinne einer „Colour Look-Up Table“ „CLUT“), folgt
bereits daraus, dass es sich bei dem „palette code“ (z. B. NK6: Fig. 47; NK6a:
Fig. 11, Fig. 17) um einen 4-Bit Wert handelt, der bekanntlich eine Farbcodierung
mit lediglich 16 Farben ermöglicht.


Denn dem Fachmann ist geläufig, dass es zum Veröffentlichungszeitpunkt der
Druckschriften NK6 und NK6a kein gebräuchliches Anzeigesystem für Videofilme
gab, welches nur mit 16 Farben arbeitete; vielmehr waren Anzeigesysteme mit
16 Mio. Farben üblich, was auch durch den Lehrbuchauszug NK34 belegt ist. Dort
wird   insbesondere   ausgeführt,     dass   „CLUT“-Grafiken   256 Farben   (8 Bit),
128 Farben (7 Bit) und 16 Farben (4 Bit) umfassen, wobei die für die Verwendung
benötigten Farben aus den 16 Mio. möglichen Farben ausgewählt werden
(Seite 207, siehe Absatz (b) „Graphics“). Daher wird der Fachmann unter der aus
der Druckschrift NK6 bzw. NK6a bekannten Farbpalette eine „CLUT“ verstehen,
die nur eine Untermenge darstellbarer Farben abbildet. An dieser Feststellung
vermag auch der in der Anlage NB5 beschriebene Color Graphics Adapter (CGA),
eine farbfähige Grafikkarte für IBM-PCs aus den 80er Jahren nichts zu ändern.
Deren Modi wurden allenfalls von PC-Spielen mit niedriger Farbauflösung, nicht
aber von Videofilmen verwendet (vgl. NB5 Seiten 3 und 4).


1.2.3 Die weitere Argumentation der Beklagten, die Druckschriften NK6 und NK6a
offenbarten keinerlei Umsteuerpositionsinformation, geht schon deshalb fehl, weil
aus beiden Druckschriften eine Abfolge von CHG_COLCON-Steuerbefehlen hervorgeht, durch die die Steuerparameter LCINF und PCINF geändert und Farbänderungspositionen aktualisiert werden können (vgl. NK6: Spalte 45, Zeilen 41 bis
57; vgl. NK6a: Absatz [0073]). Diese Steuerparameter bilden zusammen mit den

                                      - 39 -



Zeitstempeln SPDCTS die Grundlage für dynamische Farbänderungen in den
Untertitel-Inhaltsdaten (vgl. NK6: Spalte 5, Zeilen 3 bis 11; vgl. NK6a: Absatz [0023]). Insbesondere repräsentieren die Zeitstempel SPDCTS Verzögerungslängendaten (z. B. NK6: Fig. 29; NK6a: Fig. 7), die nicht nur zur Zeitsteuerung von Farbänderungen beitragen sondern auch implizit Verzögerungslängen
festlegen.


1.2.4 Nach allem gehen sämtliche Merkmale des Patentanspruchs 5 gemäß
Hauptantrag und Hilfsantrag IV aus der Druckschrift NK6 bzw. NK6a hervor. Die
Vorrichtung des Patentanspruchs 5 ist sonach nicht neu.


1.3 Die jeweiligen unabhängigen Patentansprüche 13 gemäß Hauptantrag und
Hilfsantrag IV, die auf ein Verfahren zum Dekodieren von Untertiteln gerichtet
sind, sind nicht günstiger zu bewerten als die zugehörigen Patentansprüche 5. Sie
enthalten nichts Zusätzliches, womit sich eine eigenständige Patentfähigkeit begründen ließe.


1.4 Dass die zusätzlichen Merkmale der angegriffenen Unteransprüche zu einer
anderen Beurteilung der Patentfähigkeit führen könnten, wurde weder geltend
gemacht, noch ist es ersichtlich.


2.   Zu Hilfsantrag II und III sowie Hilfsantrag V und VI


Der Beklagten ist zuzustimmen, dass der Gegenstand der Patentansprüche nach
den Hilfsanträgen II, III, V und VI nicht mehr ohne weiteres als durch die Lehre
der Druckschrift NK6 neuheitsschädlich vorweggenommen bezeichnet werden
kann. Dennoch bleiben alle vier Hilfsanträge ohne Erfolg, weil ihr jeweiliger Gegenstand - wie in der mündlichen Verhandlung diskutiert - durch NK7 und NK10
(NK10a‘) nahegelegt ist.


2.1 Die jeweiligen Lehren der Hilfsanträge II, III, V und VI unterscheiden sich im
Wesentlichen von der Lehre des Hauptantrags und Hilfsantrags IV durch das Fort-

                                         - 40 -



schreiten einer Farbwischblende in den Videorahmen in Vorwärtsrichtung, so dass
Untertitel eingefärbt werden, wobei Verzögerungslängendaten die Bewegung der
Farbwischblende verzögern (bzw. die Verzögerung steuern (Hilfsantrag II)) und
eine Dauer der Verzögerung festlegen. Ob diese Unterschiedsmerkmale für den
Fachmann in der Druckschrift NK6 offenbart sind, kann offen bleiben, da der jeweils mit den Hilfsanträgen II, III, V und VI beanspruchte Gegenstand durch einen
anderen Stand der Technik nahegelegt ist.


2.1.1 Als weiterer Stand der Technik sind die Druckschriften NK7 und NK10 von
Bedeutung.


Die Druckschrift NK7 wurde am 18. Oktober 1995 veröffentlicht. Wie bereits ausgeführt, können die angegriffenen Patentansprüche 5 und 13 gemäß Hilfsantrag II,
III, V und VI den Zeitrang des im Streitpatent angegebenen Prioritätsdatums (d. i.
23. März 1995) nicht wirksam beanspruchen, da insbesondere die Merkmale 5.2.2.3´ und 5.2.2.3´´ („Verzögerungslängendaten“) dem japanischen Prioritätsdokument des Streitpatents nicht zu entnehmen sind. Die Druckschrift NK7
gehört somit zum vorveröffentlichten Stand der Technik für das Streitpatent.


Die Druckschrift NK7 behandelt Strukturen für Untertiteldaten, die etwa bei der
Steuerung der Darstellung von Fernsehbildern Verwendung finden. Figur 1 zeigt
ein Untertitel-Datenpaket, das unter anderem einen Pixeldatenblock („sub image
display data“) und einen Ladeblock („sub image control data“) enthält. In dem
Ladeblock sind Rahmen-Steuerdaten („frame control data“) für die einzelnen
Bildrahmen vorhanden (Fig. 17), welche den einzelnen Rahmen zugeordnete
Farbverteilungen enthalten. Diese Rahmen-Steuerdaten beinhalten jeweils Zeilen
und Positionen innerhalb von Zeilen („change line numbers“ und „change pixel
numbers“), an denen sich die Farbe innerhalb des Rahmens ändert, sowie die
zugehörigen Farben in Form von Adressen für eine Farbnachschlagtabelle (vgl.
insbesondere Fig. 8, 17, 18, 19 und 20 mit Beschreibung); sie enthalten somit
Umsteuerpositionsinformationen.     In     den    einzelnen   Rahmen    sind   die
Farbverteilungen (in den Rahmen-Steuerdaten) beliebig vorgebbar, wobei sich

                                        - 41 -



sowohl die Positionen für die Farbänderungen als auch die zugehörigen
Änderungsfarben (d. h. die Adressen für die Farbnachschlagtabelle) von Rahmen
zu Rahmen ändern können.


Bei der Druckschrift NK10a´ handelt es sich um die deutsche Übersetzung der japanischen Patentanmeldung JP 6-118979 (NK10), die im Jahr 1994 veröffentlicht
wurde und damit Stand der Technik für das Streitpatent darstellt. Sie offenbart
eine Karaoke-Vorrichtung mit einer Liedertextanzeige, auf der die Schriftzeichenfolge des Liedertextes synchron zur abgespielten Begleitmusik angezeigt wird,
wobei verschiedene Anzeigeschriftarten verwendet werden (Abstract; Absätze [0001]; [0004]). Außerdem beschreibt sie eine Farbsteuerung, die entsprechend den jeweiligen Farbpositionsinformationen die angezeigten Schriftzeichen
passend zum Fortgang des zugehörigen Liedes bzw. Musikstücks in einer anderen Farbe einfärbt (Abstract; Absatz [0017]).


2.1.2 Die Druckschrift NK7 zeigt alle Merkmale des jeweiligen Patentanspruchs 5
nach Hilfsantrag II und V mit Ausnahme des Merkmals 5.2.2.3´ bzw. 5.2.2.3´´
und Teilen des Merkmalskomplexes 5.5´ bzw. 5.5´´.


Die Druckschrift NK7 befasst sich mit einem Wiedergabesystem für Untertitel-Daten („sub image“), die von einer optischen Platte eingelesen werden
(Spalte 5, Zeilen 34 bis 41; Spalte 1, Zeilen 1 bis 5; Fig. 1 – Merkmal 5).


Das bekannte System verfügt über eine Farbnachschlagtabelle bzw. Farbpalette
(„color palette“), auf die über Adressen („palette address“) auf Farbinformation zugegriffen wird (Spalte 8, Zeilen 45 bis 57; Fig. 2; Fig. 8, siehe „color palette“ 11;
Parameter SPCINFO). Dass es sich bei der Farbpalette um eine „Colour Look-Up
Table“ handelt, ergibt sich für den Fachmann einerseits aus dem Header eines
Untertitel-Daten-Pakets, in dem die 16 Farben der Palette durch eine 4-Bit-wertige
„palette color number“ referenziert werden (Fig. 2), und andererseits aus der
exemplarischen Datenstruktur für Steuerungs-Daten (Fig. 21), in der die Farbinformation ebenfalls durch einen 4-Bit Wert adressiert wird (Merkmal 5.1).

                                        - 42 -



Dem Wiedergabesystem werden Untertitel-Daten-Pakete („sub image data packet“) zugeführt (Spalte 5, Zeilen 34 bis 41; Fig. 1), die sich entsprechend Figur 1
aus einem Untertitel-Header („sub image header“ 6), Untertitel-Anzeige-Daten
(„sub image display data“ 7) und Untertitel-Steuerungs-Daten („sub image control
data“ 8) zusammensetzen (Spalte 5, Zeilen 47 bis 55). Während die Steuerungs-Daten Ladeblöcke i. S. d. Streitpatents darstellen (Spalte 11, Zeilen 18 bis 20;
Fig. 17), handelt es sich bei den Untertitel-Anzeige-Daten um Pixeldaten (Spalte 8,
Zeilen 34 bis 37; Fig. 7; Spalte 12, Zeilen 9 ff.; Fig. 18; Fig. 19). Die Merkmale 5.2
und 5.2.1 sind damit im System der Druckschrift NK7 verwirklicht.


Die Figur 17 gibt die Datenstruktur der Untertitel-Steuerungs-Daten wieder, die
wiederum einen Header 31 und Rahmen-Steuerungs-Daten 32 („frame control
data“) beinhalten (Spalte 11, Zeilen 18 bis 20). Die Rahmen-Steuerungs-Daten 32
werden anhand der Figuren 18, 19 und 20 näher beschrieben. Sie bewirken Farbänderungen im Untertitel (Spalte 11, Zeile 48 bis Spalte 12, Zeile 42 u. a.). In den
Rahmen-Steuerungs-Daten 32 sind Umsteuerinformationen in Form von Zeilennummern („change line number“) und Pixelpositionen („change start pixel number“) codiert (Merkmal 5.2.2).


Für je einen Rahmen des Videobildes geben die Pixelpositionen diejenigen Pixel
an, ab denen eine andere Farbe im Untertitel verwendet werden soll (Spalte 11,
Zeilen 54 bis 56; Spalte 12, Zeilen 9 bis 11). Eine Abfolge von Rahmen-Steuerungs-Daten ruft das Fortschreiten von Farbänderungen im Untertitel hervor, d. h.
eine Aktualisierung von Änderungspositionen (Merkmal 5.2.2.1).


Die Rahmen-Steuerungs-Daten werden Rahmen für Rahmen des Videobilds,
d. h. für jede Videorahmenperiode bereitgestellt (Spalte 6, Zeilen 29 bis 35;
Spalte 6, Zeilen 48 bis 54; Spalte 11, Zeilen 30 bis 34, siehe „frame by frame“;
Fig. 17) und bewirken, dass ab einer durch die Steuerungs-Daten festgelegten Pixelposition auf eine andere Farbe („sub image color after change“) der Farbpalette
zugegriffen wird (Fig. 21 – Merkmal 5.2.2.2). Für beliebige Farbwechsel - also
auch für solche einer sich in einer Vorzugsrichtung bewegenden Farbwisch-

                                       - 43 -



blende -   erfolgt   die   Aktualisierung   der    Änderungspositionen   in   jeder
Videorahmenperiode (teilweise Merkmal 5.5.3´ bzw. 5.5.3´´).


Die Untertitel-Daten-Pakete werden vom Wiedergabesystem der Druckschrift NK7
eingelesen und in Untertitel Header, Untertitel-Anzeige-Daten („sub image display
data“) sowie Untertitel-Steuerungs-Daten („sub image control data“) zerlegt
(Spalte 6, Zeilen 13 bis 18). Letztere beinhalten die Rahmen-Steuerungs-Daten
bzw. Umsteuerinformationen (Spalte 11, Zeilen 18 bis 20). Merkmal 5.3 ist demnach in der Druckschrift NK7 offenbart.


Außerdem verfügt das bekannte System über ein Mischer-System („mixing process system“), welches einem Videobild Untertitel überlagert, und zwar anhand
der Untertitel-Farbinformation („sub image color information“) und den Untertitel-Daten („sub image data“). Das überlagerte Bild wird auf einem Bildschirm angezeigt (Spalte 1, Zeilen 1 bis 5; Spalte 9, Zeilen 48 bis 57; Fig. 10; Spalte 9,
Zeile 56 bis Spalte 10, Zeile 10 – Merkmal 5.4).


Damit sind alle Merkmale des angegriffenen Patentanspruchs 5 in der Fassung
von Hilfsantrag II und V in der Druckschrift NK7 enthalten, bis auf das Merkmal 5.2.2.3´ bzw. 5.2.2.3´´, welches die Verwendung von Verzögerungslängendaten vorsieht, und bis auf Teile des Merkmalskomplexes 5.5´ bzw. 5.5´´, die im
Wesentlichen das Fortschreiten einer Farbwischblende im Untertitel betreffen.


2.1.3 Die Verwendung von Verzögerungslängendaten für Farbänderungen und
eine hierauf basierende Zeitsteuerung für das Fortschreiten einer Farbwischblende im Untertitel sind aus der Druckschrift NK10 bekannt.


Die Druckschrift NK10 (deutsche Übersetzung NK10a´) führt den Fachmann zu
einer Karaoke-Vorrichtung mit einer Anzeigeeinheit (Abb. 1 mit Bezugszeichen 22;
Absatz [0009]), auf der Musik zusammen mit Liedtexten ausgegeben wird. Die
Liedtexte werden zusammen mit Standbildern und Bewegtbildern angezeigt (Absatz [0012]). Gemäß den Absätzen [0017] und [0018] der Druckschrift NK10 ist für

                                      - 44 -



jeden Musiktitel eine Spur „TK4“ (ein „Track“) vorgesehen, die Untertitel-Text-Daten (Schriftzeichenfolge Liedtext „WS“) und Untertitel-Steuerungs-Information
(z. B. Information zur Verfärbungsposition) beinhaltet (Abb. 2; Abb. 3), wobei die
Steuerungs-Information dazu dient, passend zum Fortgang des Gesangs die
Schriftzeichenfolgen des Liedtextes nach und nach einzufärben, um so einem
Karaoke-Sänger den Fortschritt im Liedtext farblich anzuzeigen (Absatz [0017]).


Eine solche Untertitel-Steuerungs-Information ist der Abbildung 3 in Verbindung
mit Absatz [0021] der NK10 bzw. NK10a´ zu entnehmen: demnach enthält die
Untertitel-Steuerungs-Information Farbpositionsinformationen „CP“ (vgl. NK10b:
„coloring position information“), zwischen die Zeitinformationen (vgl. NK10b: „time
information“ Δt) eingeschoben werden.


Daneben gibt die Zeitinformation gemäß den Absätzen [0020] und [0021] der
Druckschrift NK10 auch die Zeitdauer zwischen zwei aufeinanderfolgenden, aus
Bildern und Tönen bestehenden Ereignissen („Events“) an und kann beliebig variiert werden (NK10a´: Seite 6, Absatz [0020]), um Bildinformationen, Begleitmusik
und Liedtext miteinander zu synchronisieren (Absätze [0012], [0013]). Die Farbpositionsinformationen „CP“ folgen aus den Koordinaten für die jeweiligen Positionen
der Schriftzeichen auf dem Bildschirm. Zeichencodes „CC“ und Schrifttypencodes
„CS“, die Fontgröße und Schriftart der Schriftzeichen anzeigen, sind im Liedtext
„WS“ angeordnet (Absatz [0021]). Entsprechend den Farbpositionsinformationen
„CP“ färbt eine Farbsteuerung die auf dem Bildschirm angezeigten Schriftzeichen
passend zum Fortgang des Gesangs in einer anderen Farbe (Absatz [0023]). In
den Absätzen [0012], [0019] und [0020] wird beschrieben, dass die jeweiligen
Grafikinformationen von Stand- und Bewegtbildern zusammen mit den Bildinformationen zu den Schriftzeichen des Liedtextes für jedes Ereignis („Event“) aus einem Ton und einem Bild (d. h. einem Frame) festgelegt werden, wobei zwischen
benachbarten Ereignissen die Zeitinformation Δt eingefügt wird, die die zwischen
den Ereignissen verstrichene Zeit angibt. Die Spur „TK4“ enthält die anspruchsgemäßen Ladeblöcke, die sich aus den Informationen zur Verfärbungsposition
„CP“ und den Zeitinformationen Δt zusammensetzen (Abb. 3), die gemeinsam als

                                       - 45 -



Umsteuerpositionsinformationen i. S. d. Streitpatents wirken und eine Aktualisierung von Änderungspositionen, d. h. Farbwechsel innerhalb der jeweiligen Videorahmen hervorrufen (Merkmale 5.2.2 und 5.2.2.1).


Die bekannten Zeitinformationen Δt repräsentieren insbesondere Verzögerungslängendaten i. S. d. Streitpatents, also Daten zur Festlegung einer Verzögerungsdauer, wenn sich die gleichen Umsteuerpositionsinformationen in Gestalt von
Farbpositionsinformationen „CP“ und Zeitinformationen Δt über mehrere Videorahmen erstrecken, mithin sich die Einfärbung der Schriftzeichen über eine Zeitspanne hinweg nicht ändert (Absatz [0020]).


Hierbei tragen die Zeitinformationen Δt nicht bloß zur Verzögerung von Farbwechseln ganz allgemein bei (im Sinne einer Steuerung – vgl. „to control a delay in the
update of the change position“) sondern lösen eine solche Verzögerung im Anschluss an die decodierten Farbpositionsinformationen „CP“ auch aus (vgl. „to
delay the update of the change position“). Die Merkmale 5.2.2.3´ und 5.2.2.3´´
sind damit in der Lehre der Druckschrift NK10 verwirklicht.


Laut Druckschrift NK10 bzw. NK10a´ wird mit der Veränderung der Anzeigefarbe
der Schriftzeichen das Gesangstiming beim Karaoke bildlich zum Ausdruck gebracht (Absatz [0026]). Der Fachmann wird in der Einfärbung der Schriftzeichen
eine Farbwischblende erkennen, wobei die Farbpositionsinformation „CP“ und die
Zeitinformation Δt als Farbwischblendeninformation fungieren (Merkmale 5.5.1´,
5.5.1´´), die ein allmähliches Fortschreiten eines Farbwechsels der Blende nicht
nur beschreiben sondern auch im Wesentlichen bestimmen (Merkmale 5.5.2´,
5.5.2´´; restlicher Teil der Merkmale 5.5.3´, 5.5.3´´). Entsprechend obiger Ausführungen zu den Merkmalen 5.2.2.3´ und 5.2.2.3´´ trägt die Zeitinformation Δt
nicht nur zur Verzögerung beim Fortschreiten der Farbwischblende bei, sondern
löst eine solche Verzögerung auch aus. Darüberhinaus legt sie eine beliebig einstellbare Zeitdauer der Verzögerung - eine Verzögerungslänge - fest (NK10a´:
Seite 6, Absatz [0020] - Merkmale 5.5.4´, 5.5.4´´). Damit gehen alle Teilmerkmale
der Merkmalskomplexe 5.5´ und 5.5´´ aus der Druckschrift NK10 bzw. NK10a´

                                       - 46 -



hervor, mit Ausnahme der hohen Zeitauflösung einer Videorahmenperiode für die
einzelnen Farbwechsel (teilweise Merkmal 5.5.3´ bzw. 5.5.3´´).


2.1.4 Der Gegenstand des jeweiligen Patentanspruchs 5 nach Hilfsantrag II und V
ist durch den aus den Druckschriften NK7 und NK10 bekannten Stand der Technik nahegelegt und beruht daher nicht auf erfinderischer Tätigkeit.


In der Druckschrift NK7 ist deutlich das Bestreben erkennbar, die zu übertragende
Datenmenge dadurch zu reduzieren, dass Daten, die in gleicher Form wiederholt
aufeinanderfolgend vorkommen, nur einmal übertragen werden.


Dies gilt zum einen für Pixeldatenblöcke („sub image display data“), die für eine
Mehrzahl von Videorahmenperioden nur einmal übertragen werden, solange sich
die Gestalt der Untertitel nicht ändert (vgl. NK7 Spalte 16, Zeilen 23 bis 31 und
Spalte 17, Zeilen 11 bis 19), zum anderen für über mehrere Zeilen gleich
bleibende Farbänderungen innerhalb eines Videorahmens, die nur einmal übertragen werden, zusammen mit den jeweiligen Anfangs- und Endnummern der
zugehörigen Zeilen (vgl. NK7 Fig. 20(a) mit „change line number (lines 4
to 11)“ und den zugehörigen Farbänderungen gemäß der „change start pixel
number“ für die Positionen A, B und C, vgl. NK7 Fig. 19 bis 24).


Ausgehend von dem in der Druckschrift NK7 beschriebenen Vorteil, die Menge
der in den Datenpaketen der Untertitel codierten Pixeldaten verringern zu können,
hatte der zuständige Fachmann Veranlassung, nach weiteren geeigneten
Konzepten für Systeme zur Darstellung von Untertiteln zu suchen, welche die zu
übertragenden Datenmengen noch mehr reduzieren, gerade wenn die zu
codierenden Daten mehrfach aufeinanderfolgend in gleicher Form auftreten.
Hierbei konnte er auf die Druckschrift NK10 stoßen, die ein Karaoke-System
beschreibt, bei dem dem Anwender in einer handelsüblichen Systemumgebung
eine Vielzahl von Informationen bei vertretbaren Datenmengen vermittelt wird
(NK10    bzw.     NK10a´:   Absätze [0005],     [0009]).   Sie   offenbart   u. a.   die
Datenstrukturen     eines    Karaoke-Systems,        in    denen      zwischen       den

                                       - 47 -



Farbpositionsinformationen zur Steuerung von Farbwechseln in Untertiteln
beliebig festlegbare Zeitinformationen bzw. Verzögerungen (als Vielfaches einer
zeitbezogenen       Grundeinheit)    eingefügt      werden,         wenn     sich      die
Farbpositionsinformation für eine Mehrzahl von Videorahmen nicht ändern soll.


Dem Fachmann bot es sich daher an, zur weiteren Begrenzung der zu
übertragenden Datenmengen das aus der Druckschrift NK7 bekannte System
entsprechend dem Vorbild der Druckschrift NK10 dahingehend zu erweitern, dass
anstelle sich mehrfach wiederholender Rahmen-Steuerdaten (die gemäß NK7
Fig. 17 für die aufeinanderfolgenden Rahmen hintereinander gespeichert sind), die
betreffenden Rahmen-Steuerdaten nur einmal zusammen mit passenden
Zeitinformationen bzw. Verzögerungslängen codiert werden, aus denen sich dann
Zeitpunkt     und   Dauer   der   Verzögerung    (z. B.   codiert    als   eine     Anzahl
aufeinanderfolgender Videorahmen) erschließen lassen (Merkmale 5.2.2.3´,
5.2.2.3´´).


Solche sich wiederholenden Rahmen-Steuerdaten in Gestalt von Farbpositionsund Zeitinformationen treten im System der Druckschrift NK10 etwa dann auf,
wenn beim Karaoke Gesangspausen auftreten (z. B. bei Musikabschnitten mit
reiner Instrumentalmusik), und die Farbwechsel an einer Stelle im Untertitel
temporär stehen bleiben, wobei naturgemäß die zu einem Untertitel gehörigen
Farben intervallweise über mehrere Videorahmen gleich bleiben müssen.
Dementsprechend resultiert aus der Kombination der jeweiligen Lehren der
Druckschriften NK7 und NK10 eine Farbwischblende, die sich - in Abhängigkeit
von den zu decodierenden Daten - mit der Auflösung einer Videorahmenperiode
(siehe Abschnitt 2.1.2) relativ zu dem für den Benutzer angezeigten Gesangstext
in Vorwärtsrichtung bewegt oder aber während der Gesangspausen stillsteht.
Damit ist der Merkmalskomplex 5.5´ bzw. 5.5´´ aus dem aufgezeigten Stand der
Technik nahegelegt.

                                       - 48 -



Durch die geschilderten Überlegungen konnte der Fachmann zum Gegenstand
des jeweiligen Patentanspruchs 5 nach Hilfsantrag II und V gelangen, ohne dabei
erfinderisch tätig zu werden.


2.1.5 Demgegenüber macht die Beklagte geltend, dass im System der Druckschrift
NK7 für jeden einzelnen Rahmen des Videobilds grundsätzlich auch dann eigene
Steuerdaten auf dem Aufzeichnungsmedium gespeichert würden, wenn sich die
individuell eingefärbten Bereiche der Untertitelgrafik nicht ändern. Die Druckschrift
NK7 lehre insbesondere, anstelle von mehrmalig übertragenen Bitmap-Daten eine
Kombination aus einmalig übertragenen Bitmap-Daten und mehrmalig übertragenen Steuerdaten vorzusehen, wenn sich die Form einer Untertitelgrafik nicht ändere. Der Druckschrift NK7 lasse sich jedoch keine allgemeine Lehre dahin entnehmen, zeitliche Redundanzen durch die einmalige Übermittlung von Daten unter
Angabe von Start- und Endzeitpunkten zu vermeiden.


Außerdem sehe die Druckschrift NK7 bereits eine Möglichkeit vor, um die redundante Übermittlung von Rahmensteuerdaten zu vermeiden: falls die Untertitelgrafik keine individuell eingefärbten Bereiche enthalte, könne im bekannten System
auf die Übermittlung von Untertitelsteuerungsdaten verzichtet werden, so dass das
Anzeigesystem die Farbgebung (und weitere Parameter) anhand vorgegebener
Standardwerte vornehme, die in den Headern der Untertiteldatenpakete spezifiziert seien. Hierzu verweist die Beklagte auf die folgenden Textstellen der Druckschrift NK7: Spalte 2, Zeilen 52 bis 58; Spalte 7, Zeilen 18 bis 30; Spalte 5,
Zeile 56 bis Spalte 6, Zeile 12. Davon ausgehend werde der Fachmann für die Implementierung einer Farbwischblendenfunktion auf die hier explizit offenbarte
Möglichkeit zurückgreifen, wenn er die redundante Übermittlung von Rahmensteuerdaten vermeiden möchte. Dabei könne er die Farbwischblende in den Pixeldaten codieren, so dass die betreffenden Ausprägungen der Blende ohne Verwendung von Rahmensteuerdaten angezeigt würden. Eine solche Implementierung unterscheide sich von der Lehre nach Patentanspruch 5 nach Hilfsantrag II
bzw. V, nach der für die Bewegung der Farbwischblende Umsteuerpositionsinformationen in Ladeblöcken vorgesehen seien. Merkmal 5.2.2.3´ bzw. 5.2.2.3´´ gehe

                                          - 49 -



weder aus der Druckschrift NK7 hervor noch sei es durch die Druckschrift NK7
nahegelegt. Darüberhinaus sei der Gegenstand des Patentanspruchs 5 auch im
Hinblick auf eine Kombination der Druckschriften NK7 und NK10 nicht naheliegend.


Diese Sichtweise greift jedoch zu kurz.


Zwar ist der Beklagten darin zuzustimmen, dass der Druckschrift NK7 keine Lehre
zu entnehmen ist, mit der zeitliche Redundanzen durch die einmalige Übermittlung
von Daten unter Angabe von Start- und Endzeitpunkten vermieden werden können. Allerdings handelt es sich bei der von der Beklagten angesprochenen und in
der Druckschrift NK7 beschriebenen Möglichkeit, auf die Untertitelsteuerdaten zu
verzichten um den Modus „110“ (Fig. 2 oben; Spalte 7, Zeilen 18 bis 30).


Dieser behandelt lediglich den Fall, dass die Untertitelgrafiken jeweils so dargestellt werden, wie sie als Bitmap-Daten übertragen worden sind, ohne dabei farbliche Änderungen innerhalb der Grafiken zu berücksichtigen. Soll jedoch eine vorgegebene, einmal übertragene Untertitelgrafik im zeitlichen Verlauf mit unterschiedlichen Farbänderungen innerhalb der Grafik dargestellt werden, so ist auf
den Modus „101“ abzustellen (Fig. 2 oben; Spalte 7, Zeilen 31 bis 54), wobei nicht
die Untertitelsteuerdaten sondern die Untertiteldisplaydaten, d. h. die Bitmap-Daten weggelassen werden. So sind im Fall langsamer Farbänderungen, wobei ein
geänderter Farbverlauf jeweils über mehrere Videorahmen gleichbleiben kann,
Untertitelsteuerdaten notwendig, um bei gleichbleibenden Bitmap-Daten den nach
mehreren Videorahmenperioden jeweils geänderten Farbverlauf festzulegen; auf
sie kann nicht verzichtet werden. Werden die in den Untertitelsteuerdaten (Fig. 17;
„sub image control data“) enthaltenen Videorahmensteuerdaten (Fig. 17; „frame
control data“) mehrerer aufeinanderfolgender Frames zusammengefasst, so bietet
es sich für den Fachmann an, die zugehörigen Steuerdaten (z. B. Zeitinformationen Δt nach dem Vorbild der NK10) ebenfalls in den Untertitelsteuerdaten und
nicht etwa in einem Header der jeweiligen Datenstrukturen zu hinterlegen. Infolge

                                       - 50 -



des Zusammenfassens lässt sich die Menge der Untertitelsteuerdaten bereits
deutlich reduzieren.


2.1.6 Die Beklagte hält ferner entgegen, der Fachmann werde die Druckschrift
NK10 bereits deswegen nicht in Betracht ziehen, da das hier offenbarte System
zur Darstellung von Untertiteln im Wesentlichen auf einem Zeichengenerator
beruhe. In der Druckschrift NK7 würden jedoch Bitmap-Daten anstelle von
Zeichencodes verarbeitet. Die aus den Druckschriften NK7 und NK10 bekannten
Systeme seien aus diesem Grunde inkompatibel zueinander, weswegen der
Fachmann keine Veranlassung habe, beide Druckschriften miteinander zu
kombinieren. Außerdem sehe die Lehre des Streitpatents vor, dass Änderungen
der Anzeige nur von einem Rahmen zum nächsten vorgenommen werden
könnten, so dass die Videorahmenperiode das kleinstmögliche Zeitintervall für
Änderungen der Anzeige darstelle. Das Dokument NK10 gebe aber keinen
Hinweis darauf, dass die Änderungsposition einer Farbwischblende in jeder
Videorahmenperiode aktualisiert werden könne.


Der Fachmann habe auch keine Veranlassung dazu, im System der Druckschrift
NK10 eine Bewegung der Farbwischblende mit einer solch hohen Zeitauflösung in
Betracht zu ziehen. Aus der Druckschrift gehe somit nur eine Farbwischblende
hervor, die buchstabenweise voranschreite. Mithin stelle ein Buchstabe die
kleinste räumliche Einheit in den codierten Untertiteldaten dar, so dass auch die
Position der Farbwischblende nicht mit einer höheren räumlichen Auflösung
angegeben werden könne.


Auch dieser Einwand der Beklagten greift nicht durch. Zwar geben die Untertiteldaten in der Lehre der Druckschrift NK10 die Buchstaben anhand von zugehörigen Codes an (die keine Pixeldaten bzw. –typen darstellen), wobei ein Zeichengenerator die Umsetzung des Zeichencodes in ein lesbares Zeichen erledigt und
die Darstellung des Zeichens erst im Anzeigesystem erzeugt wird. Jedoch kommt
es darauf nicht an. Für die Frage, ob der Fachmann die Druckschrift NK10 überhaupt in Betracht gezogen hätte, ist nicht die Art der Codierung der Untertiteldaten

                                          - 51 -



entscheidend. Vielmehr orientiert sich die Frage daran, ob in den zugrundeliegenden Datenstrukturen neben den Untertiteldaten Ladeblöcke mit Umsteuerinformationen enthalten sind, die eine Aktualisierung von Farbwechseln in Videorahmen
überhaupt ermöglichen. Solche Umsteuerinformationen wird der Fachmann aber
speziell in den Zeitinformationen Δt aus der Druckschrift NK10 erkennen und
diese auch in der Lehre der Druckschrift NK7 mit berücksichtigen.


Darüberhinaus kann die Frage, ob die Aktualisierung der Farbwechsel der aus der
Druckschrift NK10 bekannten Farbwischblende mit der hohen Zeitauflösung einer
Videorahmenperiode stattfindet, dahinstehen, da bereits die Lehre der Druckschrift
NK7 erlaubt, beliebige Farbwechsel mit der Zeitauflösung einer Videorahmenperiode und der räumlichen Auflösung eines Pixels durchzuführen.


2.1.7 Der Gegenstand des jeweiligen Patentanspruchs 5 gemäß Hilfsantrag II
und V ist sonach mit Rücksicht auf den aus den Druckschriften NK7 und NK10
bekannten Stand der Technik nahegelegt. Entsprechendes gilt für die jeweiligen
Patentansprüche 13, die inhaltlich nicht über die Patentansprüche 5 hinausgehen.


2.1.8 Die Hilfsanträge III und VI können nicht günstiger als die Hilfsanträge II
und V beurteilt werden, da die jeweiligen Lehren ihres Patentanspruchs 13, die
den jeweiligen Lehren des Patentanspruchs 13 nach Hilfsantrag II und V entsprechen, nicht auf erfinderischer Tätigkeit beruhen.


2.2 Einen     eigenen    erfinderischen     Gehalt   der   jeweiligen   angegriffenen
Unteransprüche der Hilfsanträge II, III, V und VI hat die Beklagte nicht geltend
gemacht. Ein solcher ist auch für den Senat nicht erkennbar.


3.   Das Streitpatent hat weder in der Fassung des Hauptantrags noch in einer
der Fassungen der Hilfsanträge II bis VI Bestand.

                                       - 52 -



                                        IV.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 ZPO. Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG i. V. m.
§ 709 Satz 1 und 2 ZPO.




                                        V.


                               Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG
statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils - spätestens nach Ablauf von fünf Monaten nach Verkündung -
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt    schriftlich    beim   Bundesgerichtshof,     Herrenstraße     45a,
76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


     - die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
     - die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.

                                     - 53 -



Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht (BGH/BPatGERVV) auf elektronischem Weg beim Bundesgerichtshof einzulegen, wird hingewiesen (www. bundesgerichtshof.de/erv.html).




Guth           Hartlieb       Dr.Thum-Rung         Dr. Forkel          Hoffmann


                                                                                 Pr
