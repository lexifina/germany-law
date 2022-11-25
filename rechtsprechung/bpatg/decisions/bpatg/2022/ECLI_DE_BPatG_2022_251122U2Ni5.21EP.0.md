---
ecli: "ECLI:DE:BPatG:2022:251122U2Ni5.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 5/21"
decided: "2022-11-25"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2022&Sort=1&Seite=32&nr=43502&anz=542&pos=487&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2022-11-25_2_Ni_5_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0081.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 5/21 vom 2022-11-25

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

2 Ni 5/21 (EP)                                           Verkündet am
                                 URTEIL               25. November 2022
verbunden mit                                                 …
2 Ni 42/21 (EP)
(Aktenzeichen)




                     In der Patentnichtigkeitssache


…




ECLI:DE:BPatG:2022:251122U2Ni5.21EP.0

                                        -2-




                  betreffend das europäische Patent 2 950 544
                                (DE 60 2006 057 691)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 25. November 2022 unter Mitwirkung der
Vorsitzenden Richterin Hartlieb sowie der Richter Dipl.-Phys. Univ. Dr. Forkel, Dipl.-
Ing. Univ. Hoffmann, Dr. Himmelmann und Dipl.-Phys. Univ. Dr. Städele für Recht
erkannt:


I.      Das europäische Patent EP 2 950 544 wird mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der Ansprüche
        7 und 13 für nichtig erklärt.


II.     Die Kosten des Rechtsstreits trägt die Beklagte.


III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des zu
        vollstreckenden Betrages vorläufig vollstreckbar.

                                             -3-




                                     Tatbestand




Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in englischer Verfahrenssprache erteilten europäischen Patents EP 2 950 544,
deutsches Aktenzeichen DE 60 2006 057 691. Die Anmeldung wurde am
16. Juni 2015        von      der   europäischen    Anmeldung   EP    10153812.2
(Veröffentlichungsnummer EP 2 192 783), die selbst eine Teilungsanmeldung der
europäischen     Stammanmeldung          EP 06841140.4   (Veröffentlichungsnummer
EP 1 982      524)     ist,    abgezweigt.    Die   Stammanmeldung   wurde    am
22. Dezember 2006 unter Inanspruchnahme der Priorität der US-Patentanmeldung
US 766300 P vom 9. Januar 2006 als PCT-Anmeldung PCT/EP2006/012492
angemeldet.


Das im Umfang der Patentansprüche 7 und 13 angegriffene Streitpatent trägt die
Bezeichnung „Adaptive Coding of the Prediction Error in Hybrid Video Coding“
(„Adaptive Kodierung des Prognosefehlers in der Hybridvideokodierung“) und
umfasst 13 Patentansprüche, darunter den unabhängigen, auf ein Verfahren zum
Decodieren eines codierten Videosignals unter Verwendung einer hybriden
Decodierung gerichteten Verfahrensanspruch 7, und den auf einen Decodierer zum
Decodieren eines codierten Videosignals unter Verwendung einer hybriden
Decodierung gerichteten Patentanspruch 13.


Die Klägerin zu 1 hat in ihrer Klageschrift vom 28. Januar 2021 auf den Seiten 6
und 7 sowie in den mit der Klageschrift eingereichten Anlagen NK 4 und NK 5 und
die Klägerin zu 2 hat in ihrer Klageschrift vom 29. Oktober 2021 auf den Seiten 8
und 9 sowie in der mit der Klageschrift eingereichten Anlage NK III eine
Merkmalsgliederung der Patentansprüche 7 und 13 mit Übersetzung zur Akte
gereicht. Danach gliedern sich die unabhängigen Patentansprüche 7 und 13 wie
folgt:

-4-

                                               -5-


Patentanspruch 7:


        Anspruch 7                                     Übersetzung
7.1     A method for decoding a coded video Verfahren zum Decodieren eines
        signal      using     hybrid        decoding, codierten        Videosignals             unter
        comprising:                                    Verwendung              einer       hybriden
                                                       Decodierung, umfassend:
7.2     receiving     a     coded    video      signal Empfangen              eines       codierten
        comprising coded video data that Videosignals,                          das           codierte
        include coded blocks of frequency Videodaten umfasst, die codierten
        domain data and/or coded blocks of Blöcke von Frequenzbereichsdaten
        spatial domain data obtained by und/oder                      codierte         Blöcke     von
        coding    a   prediction       error    signal Ortsbereichsdaten,            welche     durch
        established by reducing temporal Codieren                                               eines
        redundancy by block based motion Prädiktionsfehlersignals, das durch
        estimation;                                    Reduzieren              von         zeitlicher
                                                       Redundanz durch eine blockbasierte
                                                       bewegungskompensierte Prädiktion
                                                       ermittelt wurde, erhalten wurden,
                                                       beinhalten,
7.3     decoding the received coded video Decodieren                      der         empfangenen
        data effectively in the frequency or the codierten Videodaten effektiv im
        spatial domain depending on whether Frequenz- oder im Ortsbereich in
        video data are coded in the frequency Abhängigkeit                    davon,      ob       die
        or in the spatial domain,                      Videodaten im Frequenz- oder im
                                                       Ortsbereich codiert sind,
7.4     wherein       an          inverse       scalar wobei      eine         inverse        skalare
        quantization is used in the spatial Quantisierung sowohl im Ortsbereich
        domain as well as in the frequency als                 auch      im     Frequenzbereich
        domain,                                        verwendet wird
7.5.1   wherein the same method is used for wobei               für    das      Decodieren        der
        the   decoding       of     the     quantized quantisierten           Koeffizienten        im

                                       -6-


        coefficients in the frequency domain Frequenzbereich dieselbe Methode
        as for the decoding of the quantized verwendet        wird      wie        für    das
        samples in the spatial domain,          Decodieren        der        quantisierten
                                                Abtastwerte im Ortsbereich,
7.5.2   wherein the decoding of the quantized wobei       das        Decodieren            der
        coefficients and of the quantized quantisierten Koeffizienten und der
        samples is carried out according to quantisierten        Abtastwerte         gemäß
        CABAC or CAVLC.                         CABAC oder CAVLC durchgeführt
                                                wird.


Patentanspruch 13:


         Anspruch 13                            Übersetzung
13.1     A decoder for decoding a coded Decodierer zum Decodieren eines
         video signal using hybrid decoding, codierten          Videosignals             unter
         comprising:                            Verwendung           einer         hybriden
                                                Decodierung, umfassend:
13.2     receiving means for receiving a Empfangsmittel              zum      Empfangen
         coded video signal comprising coded eines codierten Videosignals, das
         video data that include coded blocks codierte Videodaten umfasst, die
         of frequency domain data and/or codierte                  Blöcke                 von
         coded blocks of spatial domain data Frequenzbereichsdaten                 und/oder
         obtained by coding a prediction error codierte            Blöcke                 von
         signal   established     by   reducing Ortsbereichsdaten,           die         durch
         temporal redundancy by block based Codieren eines Prädiktionsfehlermotion estimation, and                 signals, das durch Reduzieren von
                                                zeitlicher Redundanz durch eine
                                                blockbasierte
                                                bewegungskompensierte Prädiktion
                                                ermittelt wurde, erhalten wurden,
                                                beinhalten, und

                                            -7-


 13.3     adaptive control means (201) for adaptive Steuermittel (201) zum
          adaptively determining whether the adaptiven               entscheiden,       ob   das
          received     coded       video         signal empfangene codierte Videosignal
          represents the prediction error signal das           Prädiktionsfehlersignal        im
          in the spatial domain or in the Ortsbereich                          oder           im
          frequency domain,                            Frequenzbereich repräsentiert,
 13.4     wherein      an        inverse      scalar wobei       eine        inverse     skalare
          quantization is used in the spatial Quantisierung                    sowohl         im
          domain as well as in the frequency Ortsbereich                als          auch     im
          domain,                                      Frequenzbereich verwendet wird,
 13.5.1   wherein the same method is used for wobei            für   das      Decodieren     der
          the   decoding    of     the     quantized quantisieren        Koeffizienten        im
          coefficients in the frequency domain Frequenzbereich dieselbe Methode
          as for the decoding of the quantized verwendet              wird     wie     für   das
          samples in the spatial domain,               Decodieren der quantisierten Abtastwerte im Ortsbereich,
 13.5.2   wherein    the    decoding        of     the wobei     das       Decodieren        der
          quantized coefficients and of the quantisierten Koeffizienten und der
          quantized samples is carried out quantisierten Abtastwerte gemäß
          according to CABAC or CAVLC.                 CABAC oder CAVLC durchgeführt
                                                       wird.


Die Klägerinnen begehren die Nichtigerklärung des deutschen Teils des
Streitpatents im Umfang der Ansprüche 7 und 13. Die Beklagte verteidigt das
Streitpatent in vollem Umfang und hilfsweise beschränkt mit fünf Hilfsanträgen.


Die Klägerinnen stützen ihre Klagen auf die Nichtigkeitsgründe der mangelnden
Patentfähigkeit mit Blick auf fehlende Neuheit und fehlende erfinderische Tätigkeit,
der fehlenden ursprünglichen Offenbarung und der mangelnden Ausführbarkeit.
Zudem nehme das Streitpatent die Priorität nicht wirksam in Anspruch. Die
Klägerinnen halten das Streitpatent auch in der Fassung der Hilfsanträge nicht für
patentfähig.

                                       -8-


Zur Stützung ihres Vorbringens haben die Klägerinnen die folgenden Dokumente
genannt, wobei die in Klammern gesetzten Bezeichnungen auf Unterlagen aus dem
Verfahren 2 Ni 5/21 (EP) hinweisen:


NK A                Kopie der Verletzungsklage vom 20. Mai 2021 (LG München,
                    aus 2 Ni 42/21 (EP));
(NK2)               Kopie der Verletzungsklage vom 17. Juli 2020 (LG Düsseldorf,
                    Aktenzeichen 4c O 44/20 (aus 2 Ni 5/21 (EP));
NK I = (NK1)        Europäische Patentschrift des Streitpatents EP 2 950 544 B1;
NK II, (NK 3)       Auszüge aus dem Register des Deutschen Patent- und
                    Markenamts zum Streitpatent vom 28. Oktober 2021 und vom
                    20. Januar 2021;
NK III              Merkmalsanalyse der Patentansprüche 7 und 13 der Klägerin
                    zu 2;
NK IV = (NK7)       Prioritätsdokument      US    766300       P   mit   Anmeldetag
                    9. Januar 2006        zur      internationalen       Anmeldung
                    PCT/EP2006/012492 vom 22. Dezember 2006;
NK V                Unterlagen der Stammanmeldung EP 06841140.4 zum
                    Streitpatent vom 22. Dezember 2006;
(NK6)               Offenlegungsschrift      WO   2007     /   079   964   A1   der
                    Stammanmeldung;
NK1 = (NK12)        Matthias Narroschke, „Extending the prediction error coder of
                    H.264/AVC by a vector quantizer“, Proc. SPIE 5960, Visual
                    Communications and Image Processing 2005, 59606M,
                    veröffentlicht am 24. Juni 2005;
NK2                 Matthias Narroschke, „Adaptive coding of the prediction error
                    for H.264/AVC“, mit Datumsangabe „December, 2nd 2005“
NK2-V1              Auszug aus der Akte des Europäischen Patentamts, u. a.
                    Entscheidung der Beschwerdekammer des Europäischen
                    Patentamts vom 4. Dezember 2018 in der Sache …;
NK2-V2              Auszug aus dem Internetarchiv „Wayback Machine“ mit URL
                    https://web.archive.org/web/20060813161322/http://itg32.hhi.
                    de:80/dokumente.html; Ausdruck vom 11. April 2021;

                                   -9-


NK3             Y. Wang, J. Ostermann, and Y.Q. Zhang, Video Processing
                and Communications, Prentice Hall, 2002 (in Auszügen);
NK4a            H.264/AVC-Standardentwurf gemäß dem Dokument JVT-C167 mit Datumsangabe „Generated: 2002-05-10“;
NK4b            H.264/AVC-Standard (05/2003), veröffentlicht 2004;
NK5 = (NK14)    Kordasierwicz et al., HARDWARE IMPLEMENTATION OF
                THE OPTIMIZED       TRANSFORM             AND     QUANTIZATION
                BLOCKS OF H.264, veröffentlicht im Mai 2004;
NK6             US 2001 / 0 026 642 A1, veröffentlicht am 4. Oktober 2001;
NK7             Sullivan et al., „The H.264/AVC Advanced Video Coding
                Standard: Overview and Introduction to the Fidelity Range
                Extensions”, veröffentlicht im August 2004;
NK8 = (NK8)     Matthias Narroschke und Hans Georg Musmann, „Adaptive
                prediction error coding in spatial and frequency domain for
                H.264/AVC“, ITU - Telecommunications Standardization
                Sector, STUDY GROUP 16 Question 6, Video Coding Experts
                Group (VCEG), 29th Meeting: Bangkok, Thailand, 16-20
                January, 2006, Document VCEG-AB06, veröffentlicht am
                15. Januar 2006;
NK9 = (NK9)     Matthias Narroschke und Hans Georg Musmann, „Adaptive
                prediction error coding in spatial and frequency domain with a
                fixed scan in the spatial domain“, ITU - Telecommunications
                Standardization Sector, STUDY GROUP 16 Question 6, Video
                Coding Experts Group (VCEG), 30th Meeting: Hangzhou,
                China, 23-27 October, 2006, Document VCEG-AD07,
                veröffentlicht am 29. Oktober 2006;
NK10 = (NK10)   US-Patentschrift    5    543   843        A,    veröffentlicht   am
                6. August 1996;
NK11 = (NK11)   Ralf Schäfer, Thomas Wiegand and Heiko Schwarz, „The
                emerging H.264/AVC standard“, EBU TECHNICAL REVIEW,
                January 2003;
NK12            US-Patentschrift     5,475,501       A,        veröffentlicht    am
                12. Dezember 1995;

                                       - 10 -


(NK13)                 Erweiterter Europäischer Recherchebericht des Europäischen
                       Patentamts vom 27. April 2010;
(NK15)                 Auszug aus einem H.264/AVC-Standard-Dokument mit
                       Datumsangabe „05/2003“.


Die Klägerinnen stellen den Antrag,
          das europäische Patent EP 2 950 544 mit Wirkung für das
          Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der
          Ansprüche 7 und 13 teilweise für nichtig zu erklären.


Die Beklagte stellt den Antrag,
          die Klagen abzuweisen
          hilfsweise
          das europäische Patent EP 2 950 544 unter Klageabweisung im Übrigen
          mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland
          insoweit für nichtig zu erklären, als seine Ansprüche 7 und 13 über die
          Fassung eines der Hilfsanträge 1 bis 5 vom 22. September 2022 – in
          dieser Reihenfolge – hinausgehen.


Die Beklagte erklärt, dass sie die Patentansprüche gemäß Hauptantrag und
Hilfsanträgen als jeweils geschlossene Anspruchssätze ansieht, die jeweils
insgesamt beansprucht werden.


Die Beklagte, die das Streitpatent hinsichtlich der angegriffenen erteilten Ansprüche
unbeschränkt sowie hilfsweise beschränkt mit fünf Hilfsanträgen verteidigt, tritt der
Argumentation der Klägerinnen in allen wesentlichen Punkten entgegen. Sie vertritt
die Auffassung, dass das beanspruchte Verfahren und die beanspruchte
Vorrichtung ursprünglich offenbart und sowohl neu seien als auch auf einer
erfinderischen Tätigkeit des Fachmanns beruhten. Die angegriffenen Ansprüche 7
und 13 seien jedenfalls in einer der Fassungen der Hilfsanträge patentfähig.


Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:

                             - 11 -


ES1    V. Sze, M. Budagavi, G. J. Sullivan [eds.]: High Efficiency
       Video    Coding       (HEVC).     Algorithms    and     Architectures.
       Springer, 2014 (in Auszügen);
ES2    G. J. Sullivan et al.: Overview of the High Efficiency Video
       Coding (HEVC) Standard. IEEE Transactions on Circuits and
       Systems       for   Video      Technology,     Vol.   22,     No.    12,
       Dezember 2012;
ES3    G. J. Sullivan [et al.]: On dead-zone plus uniform threshold
       scalar quantization. Proc. SPIE 5960, Visual Communications
       and Image Processing 2005, 596033, 24. Juni 2005;
ES4    Y. Wang, J. Ostermann, and Y.Q. Zhang, Video Processing
       and Communications, Prentice Hall, 2002 (in Auszügen);
ES5    Vortragsfolien „Verlustbehaftete Komprimierung: Grundlagen“
       von H. Fernau mit Angabe „Datenkompression SoSe 2006“;
ES6    Auszug    der       Website     des   USPTO       zum       Inhalt   von
       provisorischen und nicht provisorischen Patentanmeldungen;
ES7    Auszug aus der „ITU-T Recommendation“ zum Standard
       H.264 mit Datumsangabe „05/2003“;
ES8    Protokolle      der       vom     Fachausschusses            3.2     der
       informationstechnischen Gesellschaft ITG am 2. Dezember
       2005 und am 23. Juni 2006 durchgeführten Treffen;
ES9    Mitteilung von Prof. H… an Dr. N… mit
       Datumsangabe 24. Juli 2013;
ES10   Mitteilung von Dr. S… an N… mit
       Datumsangabe 22. Juni 2009;
ES11   dreiseitige    Notiz     mit    Datumsangabe      „2.12.2005“        und
       Schwärzungen;
ES12   Protokoll der mündlichen Verhandlung zur Anmeldung
       10 153 812.2 vor der EPA-Patentabteilung mit Datumsangabe
       28. März 2013;
ES13   Niederschrift über die Beweisaufnahme durch Einvernahme
       von Zeugen, aufgenommen in der mündlichen Verhandlung
       zur europäischen Patentanmeldung 10 153 812.2;

                                     - 12 -


ES14                Ausdruck von 10 Screenshots;
ES15                Auszug aus Espacenet zur US-Patentschrift 5 543 843 A;
ES16                science.orf.at, „Weniger ist mehr“ fällt schwer, „Einfachheit –
                    die höchste Stufe der Vollendung“, 9. April 2021, 15:00 Uhr.


Hilfsantrag 1 vom 22. September 2022 lautet in der Verfahrenssprache Englisch:

- 13 -

                                     - 14 -


Hilfsantrag 2 vom 22. September 2022 lautet in der Verfahrenssprache Englisch:

- 15 -

                                     - 16 -


Hilfsantrag 3 vom 22. September 2022 lautet in der Verfahrenssprache Englisch:

- 17 -

                                     - 18 -


Hilfsantrag 4 vom 22. September 2022 lautet in der Verfahrenssprache Englisch:

                                     - 19 -


Hilfsantrag 5 vom 22. September 2022 lautet in der Verfahrenssprache Englisch:

- 20 -

                                        - 21 -




Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                           Entscheidungsgründe




Die Klagen, mit der die Nichtigkeitsgründe der fehlenden Patentfähigkeit mit Blick auf
fehlende Neuheit und fehlende erfinderische Tätigkeit nach Art. II § 6 Abs. 1 Satz 1
Nr. 1 IntPatÜG, Art. 138 Abs. 1 lit. a) EPÜ i. V. m. Art. 52, 54 und 56 EPÜ, der
mangelnden Ausführbarkeit nach Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜG, Art. 138
Abs. 1 lit. b) EPÜ i. V. m. Art. 83 EPÜ sowie der unzulässigen Erweiterung nach Art. II
§ 6 Abs. 1 Satz 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 lit. c) EPÜ i. V. m. Art. 123 EPÜ
geltend gemacht werden, sind gemäß § 81 PatG zulässig.


Die Klagen sind auch begründet. Das Streitpatent ist im von den Klägerinnen
beantragten und tenorierten Umfang, nämlich im Umfang der Ansprüche 7 und 13,
für nichtig zu erklären.


Denn das Streitpatent hat weder in der erteilten Fassung noch in der Fassung einer
der Hilfsanträge Bestand, da ihm der vorgenannte Nichtigkeitsgrund der fehlenden
Patentfähigkeit entgegensteht, weil die darin beanspruchte Lehre für den Fachmann
jedenfalls durch den Stand der Technik zumindest nahegelegt ist. Es bedarf daher
keiner Entscheidung, ob dem Streitpatent auch die weiterhin geltend gemachten
Nichtigkeitsgründe der mangelnden Ausführbarkeit sowie der unzulässigen
Erweiterung entgegenstehen.

                                          - 22 -


                                            I.


1.    Der Gegenstand des Streitpatents liegt auf dem Gebiet der Videocodierung
und -decodierung.


Ausweislich      der     Beschreibungseinleitung    der    Streitpatentschrift   basieren
standardisierte Videocodierverfahren auf einer hybriden Codierung, bei der ein
Codierschritt im Zeitbereich und ein Codierschritt im Ortsbereich vorgesehen ist. Bei
diesen Verfahren werde die zeitliche Redundanz von Videosignalen mittels
blockbasierter         Bewegungskompensation        reduziert.     Die    verbleibenden
Prädiktionsfehler-Samples       würden    in     Blöcken   angeordnet     und    in   den
Frequenzbereich transformiert. Daraus ergebe sich ein Block von Koeffizienten, die
quantisiert, mittels eines Zickzack-Scans in einer eindimensionalen Datenreihe
angeordnet und anschließend durch einen Codierer entropiecodiert würden. Wenn
die Prädiktionsfehler-Samples korreliert seien, resultiere aus dem Zickzack-Scan
eine Datenreihe abnehmender Energie, für deren Codierung eine kontextadaptive
binäre arithmetische Codierung („CABAC“ = „Context-Based Adaptive Binary
Arithmetic Coding“) oder eine kontextadaptive variable Längencodierung („CAVLC“
= „Context-Adaptive Variable-Length Coding“) vorgeschlagen worden sei. Die
Codiereffizienz der Transformation sei jedoch nur bei korrelierten Prädiktionsfehler-Samples hoch (Streitpatentschrift, Absätze [0001], [0002]).


Weiterhin orientiere sich eine Veröffentlichung aus dem Stand der Technik
(M. Narroschke, „Extending the prediction error coder of H.265/AVC by a vector
quantizer“, Proceedings of SPIE Visual Communications and Image Processing,
Vol. 5960, 12. Juli 2005) an der Beobachtung, dass bei den standardisierten
Videocodierverfahren, die auf einer hybriden Codierung mittels blockweiser
bewegungskompensierter Prädiktion und einer Transformationscodierung des
resultierenden Prädiktionsfehlers beruhen, in vielen Fällen der Aufwand zur
Codierung von Blöcken mit kaum oder diagonal korrelierten Samples höher als der
dazu theoretisch benötigte Aufwand sei. Die Veröffentlichung untersuche daher, ob
die Codiereffizienz verbessert werden kann, wenn die Prädiktion durch einen
Vektorquantisierer erweitert wird. Dazu werde für jeden Prädiktionsfehlerblock

                                        - 23 -


entweder     eine     standardisierte    Transformationscodierung        oder     eine
Vektorquantisierung angewendet und das Verfahren mit dem jeweils geringeren
Aufwand gewählt (Streitpatentschrift, Absatz [0003]).


Vor diesem Hintergrund stellt sich das Streitpatent die Aufgabe, ein Codier- und
Decodierverfahren sowie entsprechende Codierer und Decodierer bereitzustellen,
die effizienter als der Stand der Technik sind (Streitpatentschrift, Absatz [0004]).




2.    Als maßgeblicher Fachmann, der mit dieser Aufgabe betraut wird, ist ein
Hochschulingenieur der Elektro- und Informationstechnik anzusehen, der über eine
mehrjährige Erfahrung in der Entwicklung von Verfahren und Vorrichtungen zur
Codierung und Decodierung von Videosignalen verfügt.




3.    Zur Lösung der Aufgabe schlägt das Streitpatent ein Verfahren zum
Decodieren eines codierten Videosignals gemäß Patentanspruch 7 und einen
Decodierer zum Decodieren eines codierten Videosignals gemäß Patentanspruch
13 vor.




4.    Der jeweilige Gegenstand der erteilten Patentansprüche 7 und 13 bedarf
einer Auslegung.


4.1   Zum Patentanspruch 7 des Streitpatents


4.1.1 Dieser Patentanspruch betrifft ein Verfahren zum Decodieren eines codierten
Videosignals unter Verwendung einer hybriden Decodierung (Merkmal 7.1).


Unter einem Codieren eines Videosignals versteht der Fachmann allgemein das
Ausführen eines Verfahrens, bei dem Daten, die in einem Videosignal enthalten
sind, im Rahmen vorgegebener Regeln in andere Daten transformiert werden.
Dementsprechend werden bei einem Decodieren die transformierten Daten derart

                                            - 24 -


rücktransformiert, dass die ursprünglichen, uncodierten Daten wiederhergestellt
werden, wobei zu beachten ist, dass dies bei einer verlustbehafteten Codierung
z. B. aufgrund von Quantisierungsfehlern nur näherungsweise möglich sein kann.


Ein Decodierverfahren ist vor dem Hintergrund des Absatzes [0002] der
Streitpatentschrift dann als „hybrid“ anzusehen, wenn es einen Decodierschritt im
Ortsbereich und einen Decodierschritt im Zeit- bzw. Frequenzbereich umfasst (so
dass der letztere vor einer Rücktransformation in den Ortsbereich ausgeführt wird).
Typische     Schritte     von    Decodierverfahren       sind     beispielsweise     eine
Entropiedecodierung, ein inverser Scan (d.h. die Anordnung der Elemente einer
eindimensionalen Datenreihe in Form eines zweidimensionalen Datenblocks) oder
eine inverse Quantisierung (vgl. Streitpatentschrift, Figur 2 und Absatz [0021] - nach
den in den Blöcken 201 und 206 bzw. 201, 203 und 204 ausgeführten
Verarbeitungsschritten liegt das vom Block 201 des Decodierers empfangene
codierte Prädiktionsfehlersignal in decodierter Form entweder als im Ortsbereich
invers quantisiertes Signal oder als im Frequenzbereich invers quantisiertes und
invers transformiertes Signal vor).


4.1.2 Bei dem beanspruchten Decodierverfahren soll laut Merkmal 7.2 ein
codiertes Videosignal empfangen werden, das codierte Videodaten umfasst, die
codierte Blöcke von Frequenzbereichsdaten und/oder codierte Blöcke von
Ortsbereichsdaten       beinhalten.   Die     Blöcke   sind     durch    Codieren   eines
Prädiktionsfehlersignals erhalten worden, das durch Reduzieren von zeitlicher
Redundanz durch eine blockbasierte Bewegungsschätzung ermittelt worden ist.


Unter einem solchen Prädiktionsfehlersignal versteht der Fachmann insbesondere
eine blockweise ermittelte Differenz zwischen einem aktuell zu codierenden
Bildsignal    und       einem     Prädiktionssignal,     das       auf     Basis    einer
Bewegungskompensation unter Verwendung von Bewegungsvektoren erzeugt
worden ist (vgl. Streitpatentschrift, Absatz [0021], zweiter Satz).


Für den Fachmann ist unmittelbar klar, dass die in den Videodaten enthaltenen
codierten Blöcke von Frequenzbereichsdaten quantisierte Koeffizienten beinhalten,

                                       - 25 -


d.h. auf Werten beruhen, die aus einem Prädiktionsfehlersignal mittels einer
Frequenztransformation und einer darauffolgenden Quantisierung hervorgegangen
sind, und dass die codierten Blöcke von Ortsbereichsdaten quantisierte Abtastwerte
(„Samples“) beinhalten, d.h. Werte, die aus einem Prädiktionsfehlersignal, das nicht
in den Frequenzbereich transformiert worden ist, mittels einer Quantisierung
hervorgegangen sind (vgl. Streitpatentschrift, Absatz [0021], dritter Satz i. V. m.
Figur 1, Blöcke 106, 107 bzw. Absatz [0021], dritt- und viertletzter Satz i. V. m.
Figur 1, Block 109). Diese quantisierten Koeffizienten bzw. Abtastwerte sind in
codierter Form Bestandteile der codierten Blöcke von Frequenzbereichs- bzw.
Ortsbereichsdaten.


4.1.3 Die empfangenen codierten Videodaten sollen im Frequenz- oder im
Ortsbereich in Abhängigkeit davon decodiert werden, ob die Videodaten im
Frequenz- oder im Ortsbereich codiert sind (vgl. Merkmal 7.3). Dieses Merkmal
impliziert, dass die im Frequenz- und im Ortsbereich codierten Videodaten auf
verschiedene Weise decodiert werden, z.B. weil sich der Decodiervorgang in den
beiden Bereichen unterscheidet und/oder weil dort jeweils verschiedene
Hardwarekomponenten zum Einsatz kommen.


Dass die Videodaten gemäß Merkmal 7.3 „effektiv“ („effectively“) decodiert werden,
besagt - den verschiedenen Bedeutungen des englischen Begriffs „effectively“
entsprechend - zum einen, dass die eingesetzten Decodierverfahren „effizient“ sind,
zum anderen aber auch, dass die Videodaten „tatsächlich“, „wirklich“ oder „wirksam“
decodiert werden.


4.1.4 Merkmal 7.4 ist aufgrund des einleitenden Adverbs „wobei“ unmittelbar auf
Merkmal 7.3 rückbezogen (ein direkter Rückbezug auf Merkmal 7.1 scheidet
aufgrund der Angabe „Verfahren zum Decodieren eines Videosignals, […]
umfassend:“ in Merkmal 7.1 aus). Demnach kommt zum Decodieren der
empfangenen codierten Videodaten sowohl im Orts- als auch im Frequenzbereich
eine inverse skalare Quantisierung zum Einsatz. Das Streitpatent sieht eine solche
Quantisierung ausdrücklich als einen Teilschritt einer Codiermethode an (vgl.
Streitpatentschrift, Absatz [0015] - „a method for coding a video signal is provided

                                       - 26 -


including a step of quantising the prediction error samples in the spatial domain“),
so dass davon auszugehen ist, dass eine inverse Quantisierung dementsprechend
auch einen Teilschritt einer Decodiermethode darstellt.


4.1.5 Die mit „wobei“ eingeleiteten weiteren Anspruchsmerkmale 7.5.1 und 7.5.2
charakterisieren ebenfalls das Decodieren der empfangenen codierten Videodaten
nach Merkmal 7.3.


So soll gemäß Merkmal 7.5.2 das Decodieren der quantisierten Koeffizienten und
der quantisierten Abtastwerte gemäß CABAC oder CAVLC („according to CABAC
or CAVLC“) durchgeführt werden.


Der Fachmann versteht unter den Abkürzungen „CABAC“ bzw. „CAVLC“ Verfahren,
bei denen eine binäre arithmetische Codierung („BAC“ = „Binary Arithmetic Coding“)
bzw. eine variable Längencodierung („VLC“ = „Variable-Length Coding“)
kontextadaptiv („CA“ = „Context-Adaptive“) durchgeführt wird, so dass die
Codierung anhand von Informationen (dem „Kontext“) dynamisch angepasst wird,
die aus zuvor codierten Informationen abgeleitet worden sind (z.B. aus statistischen
Informationen über bereits codierte benachbarte Blöcke).


Merkmal 7.5.2 umfasst aufgrund der Konjunktion „oder“ („according to CABAC or
CAVLC“) sowohl den Fall, dass die quantisierten Koeffizienten und die quantisierten
Abtastwerte mittels derselben Entropiedecodiermethode - entweder mittels CABAC
oder mit CAVLC - decodiert werden, als auch den Fall, dass auf diese Größen
verschiedene Entropiedecodiermethoden angewendet werden (d.h. die CABAC-Methode auf die quantisierten Koeffizienten und die CAVLC-Methode auf die
quantisierten Abtastwerte oder umgekehrt).


4.1.6 Gemäß Merkmal 7.5.1 soll für das Decodieren der quantisierten Koeffizienten
im Frequenzbereich - dem Bedeutungsgehalt des Begriffs „the same method“
entsprechend - dieselbe oder die gleiche Methode wie für das Decodieren der
quantisierten Abtastwerte im Ortsbereich verwendet werden; das Merkmal nimmt
auf das in Merkmal 7.3 angesprochene Decodieren Bezug, weil die codierten

                                          - 27 -


Videodaten        gemäß   Merkmal   7.2    codierte   Blöcke   von     Frequenz-    und
Ortsbereichsdaten enthalten, die der Fachmann insbesondere mit quantisierten
Koeffizienten bzw. mit quantisierten Abtastwerten identifiziert (s.o., Abschnitt
I.4.1.2).


Der Fachmann wird Merkmal 7.5.1 wie folgt auslegen:


a)     Eine Methode ist nach fachmännischem Verständnis grundsätzlich ein
regelhaftes oder planmäßiges Verfahren zur Zielerreichung, welches mehrere
Teilschritte (Teilverfahren) umfasst. So umfasst das mit Merkmal 7.1 beanspruchte
Verfahren zum Decodieren nach dem Anspruchswortlaut insbesondere die
Teilschritte der Merkmale 7.2 („Empfangen […]“) und 7.3 („Decodieren […]“). Setzt
sich ein Teilschritt einer Methode aus mehreren regelhaften oder planmäßigen
Teilschritten zusammen, stellt er wiederum selbst eine Methode dar. Beispielsweise
kann eine inverse Quantisierung oder eine Entropiedecodiermethode einen von
mehreren Teilschritten eines Decodierverfahrens bilden.


Bereits aus prinzipiellen Erwägungen heraus ist dem Fachmann klar, dass zwei
derartige Teilschritte, von denen der eine im Frequenz- und der andere im
Ortsbereich zum Zweck einer Decodierung vorgenommen wird, insbesondere dann
zumindest die gleiche Methode ausführen, wenn die beiden Teilschritte dasselbe
Ziel erreichen oder demselben Zweck dienen und sich allenfalls in Details ihrer
Implementierung unterscheiden. Basiert etwa eine inverse Quantisierung oder eine
Entropiedecodierung im Frequenzbereich auf anderen Parametern als im
Ortsbereich, wird nichtsdestoweniger in beiden Bereichen dieselbe Zielsetzung -
eben        das    Durchführen   einer     inversen    Quantisierung     bzw.      einer
Entropiedecodierung - verwirklicht, so dass in beiden Bereichen die gleiche
Methode „inverse Quantisierung“ bzw. „Entropiedecodierung“ verwendet wird. In
diesem Fall kann eine „Entropiedecodierung mit inverser Quantisierung“ auch als
eine einzige, in beiden Bereichen gleiche Methode angesehen werden.

                                      - 28 -


b)    Patentanspruch 7 gibt ausdrücklich zwei Teilschritte an, die zum Decodieren
der codierten Videodaten im Frequenz- und im Ortsbereich (vgl. Merkmal 7.3) zum
Einsatz kommen können, nämlich eine inverse skalare Quantisierung (vgl. Merkmal
7.4) und eine Entropiedecodierung der quantisierten Koeffizienten und quantisierten
Abtastwerte, wobei letztere ebenfalls in beiden Bereichen entweder gemäß CABAC
oder gemäß CAVLC ausgeführt werden kann (s.o., Abschnitt I.4.1.5). Beide
Teilschritte wirken sich auf die rekonstruierten Abtastwerte bzw. die Werte der
rekonstruierten Koeffizienten aus und dienen somit der Decodierung dieser in dem
Videosignal enthaltenen Größen.


Bereits jeder einzelne dieser Teilschritte, aber auch eine beliebige Menge von
(jeweils in beiden Bereichen ausgeführten) Teilschritten, die zumindest die
Teilschritte „inverse skalare Quantisierung“ und „Entropiedecodierung“ umfasst,
kann als „dieselbe oder die gleiche Methode“ im Sinne von Merkmal 7.5.1
angesehen werden (vgl. Abschnitt I.4.1.6 a)). Eine solche Menge kann
insbesondere auch alle Teilschritte umfassen, die sowohl im Frequenz- als auch im
Ortsbereich zur Decodierung der empfangenen codierten Videodaten verwendet
werden.


c)    Somit folgt aus der Systematik des Patentanspruchs 7, dass „dieselbe
Methode“ in Merkmal 7.5.1 mindestens ein Teilschritt (Teilverfahren) eines
Decodierverfahrens ist, der im Orts- und im Frequenzbereich ausgeführt wird, zur
Rekonstruktion der ursprünglichen uncodierten Koeffizienten und Abtastwerte
beiträgt, und mit dem in beiden Bereichen das gleiche Ziel erreicht wird (z.B.
quantisierte Größen zu decodieren, invers zu quantisieren, in bestimmter Weise
anzuordnen, zu anderen Größen hinzuzuaddieren etc.). Dabei sind unterschiedliche
Implementierungen in den beiden Bereichen möglich.


d)    Nichts Anderes ergibt sich, wenn die Beschreibung und die Figuren des
Streitpatents herangezogen werden.


aa)   Die Architektur des streitpatentgemäßen Decodierers ist in Figur 2 i. V. m.
Absatz [0024] der Streitpatentschrift gezeigt. Demnach führt der Decodierer zum

                                      - 29 -


Decodieren der quantisierten Koeffizienten und Abtastwerte sowohl im Orts- als
auch im Frequenzbereich die Teilschritte „inverser Scan“, „Entropiedecodierung“
und „inverse Quantisierung“ aus (zum inversen Scan im Ortsbereich siehe „a scan
control unit 205 provides the correct order of the samples for the entropy decoding
block 201“, woraus folgt, dass die an den Decodierer übertragenen quantisierten
Abtastwerte invers gescannt werden, sowie Absätze [0026], [0027]; zum inversen
Scan der Koeffizienten im Frequenzbereich siehe Absatz [0025] und Figur 3; zur
Entropiedecodierung siehe Absatz [0024], zweiter Satz; zur inversen Quantisierung
siehe Figur 2, Blöcke 203 und 206). Jeder einzelne dieser Schritte, aber auch
mehrere oder alle diese Schritte können als „dieselbe Methode“ im Sinne von
Merkmal      7.5.1   angesehen   werden.   Hingegen    transformiert   die   inverse
Frequenztransformation in Block 204 vom Frequenz- in den Ortsbereich und bildet
somit weder einen Bestandteil eines Verfahrens, bei dem „im Frequenzbereich“
decodiert wird, noch einen Teilschritt einer Methode im Sinne von Merkmal 7.5.1.


bb)    Für die Auslegung des Merkmals 7.5.1 sind ferner die Absätze [0006], [0009]
und [0035] der Streitpatentschrift von Bedeutung. Dort wird der Begriff „the same“
ausdrücklich verwendet - allerdings nur im Zusammenhang mit einem Codieren. Da
ein Decodierer in der Regel die einzelnen Codierschritte des zugehörigen Codierers
(zumindest näherungsweise) wieder rückgängig macht (vgl. Streitpatentschrift,
Absatz [0017], letzter Satz), können die aus den genannten Absätzen abgeleiteten
Schlussfolgerungen grundsätzlich auch auf ein Decodieren übertragen werden.


(1)    Die ersten beiden Sätze in Absatz [0009] des Streitpatents geben an, dass
die Abtastwerte im Ortsbereich mit „im Grunde genommen denselben oder den
gleichen Methoden“ codiert werden können, die für die Koeffizienten im
Frequenzbereich verwendet werden, wobei diese Methoden die CABAC- oder die
CAVLC-Methode sind oder eine dieser Methoden umfassen („the samples in the
spatial domain may be coded by essentially the same methods as being used for
the coefficients in the frequency domain. These methods may include the CABAC
or CAVLC coding methods“; die englischen Begriffe „essentially“ und „the same“
bedeuten „im Grunde genommen“ oder „im Wesentlichen“ bzw. „dieselbe“ oder „die
gleiche“).

                                       - 30 -




Die im vorstehenden Absatz zitierten Angaben interpretiert der Fachmann auf
zweierlei Art: zum einen kann sich der Ausdruck „the same methods“ auf genau
zwei Verfahren beziehen, von denen das eine im Ortsbereich (zum Codieren der
Abtastwerte) und das andere im Frequenzbereich (zum Codieren der Koeffizienten)
verwendet wird, wobei beide Verfahren die CABAC- oder die CAVLC-Methode als
Teilschritt beinhalten und jeweils eines dieser Verfahren insbesondere sämtliche
Codierschritte umfassen kann, die in dem zugehörigen Bereich verwendet werden.
Zum anderen kann mit dem Begriff „the same method“ genau ein Teilschritt (bzw.
ein Teilverfahren) eines Codierverfahrens gemeint sein (z.B. die CABAC- oder die
CAVLC-Entropiecodiermethode, s. auch Absatz [0035] der Streitpatentschrift), so
dass sich der Plural „the same methods“ in diesem Fall auf mehrere solche
Teilschritte bezieht, von denen einer z.B. die CABAC- oder die CAVLC-Methode ist.


Beide Interpretationsmöglichkeiten sind mit der oben aus der Anspruchssystematik
abgeleiteten Auslegung des Merkmals 7.5.1 (vgl. in Abschnitt I.4.1.6 c)) in Einklang.


Dem Absatz [0009] der Streitpatentschrift entnimmt der Fachmann ebenfalls, dass
zwei Codiermethoden auch dann als „im Grunde genommen dieselben“ („essentially
the same“) - d.h. zumindest als die gleichen - gelten können, wenn sie im Detail
Anpassungen an den Orts- oder den Frequenzbereich enthalten ([…] coded by
essentially the same methods […] only little […] adaption of the coding mechanisms
is necessary“). Für den Fall eines Scans oder einer Entropiecodierung sind solche
Anpassungen zur Codierung der Abtastwerte im Ortsbereich auch den
Ausführungsbeispielen des Streitpatents zu entnehmen (vgl. Streitpatentschrift,
Absätze [0026], [0027], [0035]). Allgemeine Kriterien zur Beurteilung der Frage,
wann eine Anpassung einer Methode im Frequenz- oder im Ortsbereich so
umfangreich ist, dass nicht mehr von einer Anwendung der gleichen Methode
gesprochen werden könnte, offenbart das Streitpatent nicht.


(2)   Aus Absatz [0006] der Streitpatentschrift geht insbesondere hervor, dass
diejenigen   Codiermechanismen,      die   nach    einer   Entscheidung,    ob   ein
Prädiktionsfehlersignal im Frequenz- oder im Ortsbereich verarbeitet werden soll,

                                        - 31 -


im Orts- und im Frequenzbereich ausgeführt werden, dieselben oder die gleichen
(„the same“) sind, wenn sie im Ortsraum nicht speziell an die Eigenschaften der
Abtastwerte angepasst worden sind (siehe „it is decided whether to use frequency
domain transform or to maintain the prediction error signal in the spatial domain.
The subsequent coding mechanisms may be the same as for the frequency domain
or they may be adapted to the needs of the samples in the spatial domain“; der
englische Begriff „subsequent” bedeutet „anschließend”, „nachfolgend”, „später”,
„nachherig”).


Unter einem solchen Codiermechanismus versteht das Streitpatent insbesondere
ein Entropiecodierverfahren (vgl. Streitpatentschrift, Absatz [0014] - „a specific code
for the coding mechanisms, as for example CABAC or the like is used”; s. auch
Absatz [0024], dritter Satz). Gemäß den Absätzen [0015], [0026] und [0027] wird
aber auch ein Quantisierungsschritt sowie ein „Scanmechanismus” zur Codierung
eingesetzt, und Absatz [0009] zufolge kann mindestens eine im Ortsbereich
ausgeführte Codiermethode mehrere Codiermechanismen umfassen (siehe „[…]
may be coded by essentially the same methods […] Accordingly, only little or no
adaption of the coding mechanisms is necessary”). Daneben ist Absatz [0036] zu
entnehmen, dass die Menge aller im Frequenz- oder im Ortsbereich ausgeführter
Codierungs-Teilschritte als ein einziger „coding mechanism” angesehen werden
kann (siehe Absatz [0036] - „the side information includes specific flags, which
indicate whether the coding mechanism has adaptively been changed […]”).


Ein   Codiermechanismus        ist   somit    mindestens     ein   Teilschritt   eines
Codierverfahrens, welcher der Codierung eines Prädiktionsfehlerblocks dient.


Gemäß dem Streitpatent kann die in Absatz [0006] genannte Entscheidung
insbesondere für einen jeweiligen Block auf Basis eines sog. „rate distortion“-
Kriteriums getroffen werden, in das ein mittlerer Quantisierungsfehler eingeht, der
sich jeweils bei Codierung im Frequenz- und im Ortsbereich ergibt (vgl.
Streitpatentschrift, Absatz [0007] - „The decision may be made for all samples within
a specific portion of a video signal at once, or e.g. even for a specific number of
blocks“ - dabei kann die „specific portion“ ein Block bzw. die „number of blocks“

                                          - 32 -


gleich 1 sein; Absatz [0008] - „the distortion measure may be the mean square
quantisation error“). Um in diesem Fall die Quantisierungsfehler für einen Block
abschätzen zu können, müssen dessen Abtastwerte und die aus diesen durch eine
Frequenztransformation       hervorgehenden        Koeffizienten   im    Orts-   und    im
Frequenzbereich quantisiert worden sein. Erst danach kann die Entscheidung von
einem Anpassungssteuerungsblock 115 getroffen werden, welcher anschließend
zwei Schalter jeweils in die Stellung „A“ oder „B“ bringt. Dadurch kann die anhand
des    „rate    distortion“-Kriteriums   bestimmte     quantisierte     Größe    in    dem
Entropiecodierer 113 verarbeitet werden. Dieser führt lediglich die Teilschritte
„Scan“ und „Entropiecodierung“ aus (vgl. Figur 1 und Absätze [0021], [0022]).


Damit können unter den in Absatz [0006] der Streitpatentschrift genannten, auf die
Entscheidung folgenden Codiermechanismen („subsequent coding mechanisms“)
auch nur ein Scan und eine Entropiecodierung - d.h. lediglich zwei Teilschritte einer
Codiermethode, die in beiden Bereichen ausgeführt werden - verstanden werden.


Dies ist ebenfalls in Übereinstimmung mit der Schlussfolgerung aus Abschnitt
I.4.1.6 c) (s.o.).


cc)    Ein eingeschränktes Verständnis des Merkmals 7.5.1, gemäß dem nur dann
im Frequenz- und im Ortsbereich dieselbe oder die gleiche Methode ausgeführt
wird, wenn sämtliche Teilschritte, die im Frequenz- und im Ortsbereich zur
Decodierung eingesetzt werden, identisch sind, kann somit auch ausgehend von
Absatz [0006] der Streitpatentschrift nicht begründet werden. Eine derartige enge
Auslegung des Gegenstands von Patentanspruch 7 bleibt auch bei Heranziehung
der Beschreibung und der Figuren des Streitpatents unterhalb des Wortlauts
(Sinngehalts) dieses Patentanspruchs und ist deswegen nicht zulässig (vgl. BGH,
Urteil vom 12. Dezember 2006 – X ZR 131/02, GRUR 2007, 309 –
Schussfädentransport; BGH, Urteil vom 23. Juli 2013 – X ZR 87/12, GRUR 2013,
1279, Rn. 14 - Seitenwandmarkierungsleuchte).


e)     Alles in allem versteht der Fachmann unter „derselben Methode“ in Merkmal
7.5.1 mindestens einen Teilschritt bzw. mindestens ein Teilverfahren eines

                                        - 33 -


Decodierverfahrens, der bzw. das einen Beitrag zur Rekonstruktion der
quantisierten Koeffizienten und Abtastwerte leistet, sowohl im Orts- als auch im
Frequenzbereich ausgeführt wird, und mit dem in beiden Bereichen dasselbe Ziel
erreicht wird. Dabei kann der mindestens eine Teilschritt Anpassungen an
bestimmte Erfordernisse beinhalten, die eine Verarbeitung in einem dieser Bereiche
mit sich bringt.


4.2    Zum Gegenstand des Patentanspruchs 13 des Streitpatents


Die Ausführungen aus Abschnitt 4.1 zu den Merkmalen 7.1, 7.2, 7.4, 7.5.1 und 7.5.2
gelten auch für die korrespondierenden Merkmale 13.1, 13.2, 13.4, 13.5.1 und
13.5.2 des Patentanspruchs 13.


Mit diesem Patentanspruch wird ein Decodierer beansprucht, der gemäß dem
weiteren Merkmal 13.3 adaptive Steuermittel zum adaptiven Bestimmen, ob das
empfangene codierte Videosignal das Prädiktionsfehlersignal im Ortsbereich oder
im Frequenzbereich repräsentiert, umfassen soll. Ein derartiges adaptives
Steuermittel ist aus fachmännischer Sicht insbesondere ein Mittel, durch das
zunächst festgestellt wird, ob ein empfangenes codiertes Videosignal ein
Prädiktionsfehlersignal in einem der beiden Bereiche repräsentiert, und das
abhängig vom Ergebnis dieser Feststellung die Ausführung eines Verfahrens -
beispielsweise zur Decodierung des Prädiktionsfehlersignals - einleitet (vgl.
Streitpatentschrift, Absatz [0016] - „a decoder is provided including adaptive control
means for adaptively deciding whether an input stream of a coded video signal
represents the prediction error signal […] in the spatial domain or in the frequency
domain“; Absatz [0024] - „to switch between frequency and spatial domain […] is
controlled […]“).


4.3    Dem Vorbringen der Beklagten zur Auslegung der Merkmale der erteilten
Patentansprüche 7 und 13 kann nicht gefolgt werden.


4.3.1 Die Beklagte macht geltend, „dieselbe Methode“ in Merkmal 7.5.1 bedeute,
dass die im Ortsbereich verwendete Methode zum Decodieren der quantisierten

                                          - 34 -


Abtastwerte und die im Frequenzbereich verwendete Methode zum Decodieren der
quantisierten Koeffizienten gleich seien. Der einzige Unterschied zwischen den
Decodierschritten des Prädiktionsfehlers im Orts- und im Frequenzbereich liege im
inversen Transformationsschritt. Dies sei auch aus den einleitenden Absätzen
[0004], [0006], [0007] und [0009] der Streitpatentschrift ableitbar. Dabei sei mit dem
Vorschlag „The subsequent coding mechanisms may be the same as for the
frequency domain“ in Absatz [0009] aufgrund des Zusatzes „or they may be adapted
especially to the needs of the samples in the spatial domain“ gerade keine Adaption
gemeint. Zudem wäre Merkmal 7.5.1 überflüssig, wenn es sich nur auf einen
Teilschritt einer Decodiermethode beziehen würde, da in Merkmal 7.4 bereits ein
solcher   Teilschritt   genannt    sei.    Wenn    Patentanspruch    7    unter   der
Entropiedecodierung und der inversen Quantisierung jeweils eine eigene Methode
verstehen würde, müsste in den Ansprüchen entsprechend von denselben
Methoden (Plural) die Rede sein.


In Hinblick auf Merkmal 13.5.1 gelte Entsprechendes.


4.3.2 Der Beklagten ist insoweit zuzustimmen, dass mit „derselben Methode“ in
den Merkmalen 7.5.1 und 13.5.1 u.a. eine Methode gemeint sein kann, die jeweils
im Orts- und im Frequenzbereich ausgeführt wird und jeweils sämtliche
Decodierschritte eines der beiden Bereiche umfasst (s.o., Abschnitt I.4.1.6 b),
zweiter Absatz sowie Abschnitt I.4.2). Wie oben dargelegt, umfasst der jeweilige
Gegenstand der Patentansprüche 7 und 13 jedoch nicht nur diese spezielle
Ausführungsform; dies ergibt sich bereits aus Absatz [0009], aber auch selbst dann
aus Absatz [0006] der Streitpatentschrift, wenn die dort angesprochenen
nachfolgenden Codiermechanismen nicht als adaptiert angesehen werden. Im
Übrigen hat die Beklagte mit Patentanspruch 7 nach Hilfsantrag 5 zum Ausdruck
gebracht (s. u., Abschnitt III.5.1.4, Merkmal 7.5.1Hi5), dass „dieselbe Methode“ eine
im Orts- und im Frequenzbereich ausgeführte Entropiedecodiermethode - d.h. auch
nur ein Teilschritt eines in beiden Bereichen ausgeführten umfassenderen
Decodierverfahrens - sein kann.

                                         - 35 -


Zudem können die Merkmale 7.5.1 und 13.5.1 gemäß der oben dargestellten
Auslegung durchaus auch beschränkend wirken, wenn unter „derselben Methode“
ein Teilschritt eines Decodierverfahrens verstanden wird, der nicht (nur) die inverse
Quantisierung ist. Daher sind die Merkmale eben nicht überflüssig.




                                          II.


Das Streitpatent hat in der erteilten Fassung keinen Bestand, weil die jeweiligen
Gegenstände seiner unabhängigen Patentansprüche 7 und 13 nicht patentfähig
sind.


1.      Die Lehre des erteilten Patentanspruchs 7 beruht gegenüber dem der
Druckschrift NK10 entnehmbaren Stand der Technik nicht auf einer erfinderischen
Tätigkeit.


1.1     In NK10 ist ein Codierverfahren beschrieben, bei dem Blöcke mit homogener
Bildinformation im Rahmen einer DCT-Codierung („DCT coding“ = „discrete cosine
transform coding“) einer diskreten Kosinustransformation in den Frequenzbereich
unterzogen werden, wohingegen Blöcke mit inhomogener Bildinformation (z.B. mit
Konturen) im Rahmen einer NTC-Codierung („NTC coding“ = „non-transform
coding“) ohne eine solche Frequenzbereichstransformation, d.h. im Ortsbereich
codiert werden (Spalte 2, Zeile 23 bis 38; die NTC-Codierung wird in NK10 auch als
prädiktive Intrablockcodierung („intra-block predictive coding“) bezeichnet, s. z.B.
Spalte 2, Zeile 3, 4 und 8 sowie Zeile 56).


Dementsprechend      verarbeitet   das    bei     dem   Codierverfahren   eingesetzte
Codiersystem DV1 ein aus aufeinanderfolgenden Blöcken eines digitalen
Eingangsvideosignals („digital input motion picture signal“) zusammengesetztes
digitales Eingangsbildsignal („block digital input picture signal“) DIN mittels einer
DCT-Codiereinheit 1, einer NTC-Einheit 2 und einer Codiermethoden-Umschalt-Beurteilungseinheit 3. Das Eingangsbildsignal DIN wird an einen Differenzrechner 8
sowie einen Prädiktor 5 übertragen, der ein Prädiktionssignal S1 erzeugt. Der

                                         - 36 -


Differenzrechner 8 führt entweder eine Intra-Frame- oder eine InterFrame-Codierung aus, um ein Signal S2 zu erhalten, das die Differenz zwischen dem
Prädiktionssignal S1 und DIN repräsentiert. Das Differenzsignal S2, in dem der
Fachmann      ein    Prädiktionsfehlersignal      mit   im     Ortsbereich     vorliegenden
Abtastwerten erkennt, wird in die DCT-Codiereinheit 1 und in die NTC-Einheit 2
eingespeist und der Codiermethoden-Umschalt-Beurteilungseinheit 3 übermittelt
(Spalte 4, Zeile 39 bis 54 sowie Claim 1). Die Transformationseinheit 11 der DCT-Codiereinheit 1 wandelt das Differenzsignal S2 in ein DCT-Ausgangssignal S3 um,
welches Koeffizienten enthält, die die Beiträge verschiedener Frequenzbänder zum
Differenzsignal      S2      charakterisieren.        Die     Codiermethoden-Umschalt-Beurteilungseinheit 3 erhält das DCT-Ausgangssignal S3, wählt die im Hinblick auf
einen Datenkompressionsfaktor vorteilhaftere Codiermethode aus und veranlasst
dementsprechend die DCT-Codiereinheit 1 oder die NTC-Einheit 2, das
Differenzsignal S2 zu codieren (Spalte 4, Zeile 60 bis 63; Spalte 6, Zeile 6 bis 25).


In der DCT-Codiereinheit 1 wird das DCT-Ausgangssignal S3 einer Quantisierung
in einem ersten Quantisierer 12 unterzogen, so dass ein quantisiertes Signal S4
erhalten wird, welches quantisierte Koeffizienten enthält. Nachdem dieses einen
Verzögerungsschaltkreis 13 („DLY“) der DCT-Codiereinheit 1 durchlaufen hat, wird
es     in    einer        VLC-Codiereinheit       6         zusammen     mit       weiteren
Übertragungsverwaltungsdaten S7 in ein entropiecodiertes VLC-Signal S6
transformiert (Figur 1, Blöcke 11, 12, 13; Spalte 4, Zeile 60 bis Spalte 5, Zeile 5).


In der NTC-Einheit 2 wird das Differenzsignal S2 in einen Intra-Block-Prädiktor 21
eingespeist. Dieser ermittelt einen typischen Wert eines Blocks des Differenzsignals
S2 sowie ein weiteres Signal, das die Differenz zwischen dem typischen Wert und
den Pixelwerten des Blocks darstellt, als prädiktives Codiersignal S10 in einen
zweiten Quantisierer 22 eingespeist, dort in ein quantisiertes Signal S11
umgewandelt und an einen Scankonverter 23 übertragen wird, welcher
anschließend ein umgeordnetes quantisiertes Signal S12 erzeugt (Spalte 5, Zeile
34 bis 45). Dieses wird anschließend entweder direkt - oder optional über einen
Differentiator 24 - der VLC-Codiereinheit 6 übermittelt (zur Verarbeitung des Signals
S12 mit Hilfe des Differentiators 24 vgl. Spalte 5, Zeile 43 bis 60 sowie Spalte 11,

                                         - 37 -


Zeile 48 bis Spalte 12, Zeile 33 und Figur 5; zur Verarbeitung ohne den Differentiator
24 vgl. Spalte 12, Zeile 34 bis 50 und Figur 17).


Das Codiersystem DV1 überträgt die von der VLC-Codiereinheit 6 codierten Daten
als Ausgangssignal DOUT an einen Pufferschaltkreis 31 eines Decodiersystems
DV2, welches zunächst das Ausgangssignal in der inversen VLC-Codiereinheit 32
einer inversen variablen Längencodierung unterzieht (Spalte 6, Zeile 32 bis 36 i. V.
m. Spalte 5, Zeile 1 bis 7; Figuren 1 und Figur 2). Das resultierende decodierte
quantisierte Signal S21 wird entweder in dem aus der Blockgruppe 33
(Verzögerungsschaltkreis), 34 (inverser Quantisierer) und 35 (inverser DCT-Schaltkreis) oder dem aus der Blockgruppe 36 (optionaler inverser Differentiator),
37 (inverser Scankonverter), 38 (inverser Quantisierer) und 39 (inverser Intra-Block-Prädiktor) bestehenden Zweig des Decodierers DV2 decodiert, so dass sich die
rekonstruierten Differenzsignale S22 bzw. S23 ergeben (Spalte 6, Zeile 37 bis 57;
Spalte 18, Zeile 63 bis Spalte 19, Zeile 14; Figur 2).


1.2   Somit decodiert das Decodiersystem DV1 sowohl Daten im Frequenzbereich
mittels der Blöcke 32 und 34 als auch im Ortsbereich mittels der Blöcke 32, 37, 38,
39 und ggf. 36 (s.o.; vgl. insbesondere Spalte 12, Zeile 24 bis 50; Spalte 18, Zeile
63 bis Spalte 19, Zeile 17).


Die Druckschrift NK10 offenbart demzufolge ein Verfahren zum Decodieren eines
codierten   Videosignals       unter   Verwendung    einer       hybriden   Decodierung
(Merkmal 7.1).


1.3   Da die Bildsignale in der DCT-Codiereinheit 1 und der NTC-Einheit 2 jeweils
blockweise codiert werden (vgl. Spalte 2, Zeile 23 bis 27 und Spalte 4, Zeile 39 bis
46; s. z.B. auch Figuren 3 bis 5 und 17), empfängt der Pufferschaltkreis 31 des
Decodiersystems DV2 ein codiertes Videosignal, das codierte Videodaten umfasst,
die codierte Blöcke von Frequenzbereichsdaten und codierte Blöcke von
Ortsbereichsdaten       beinhalten,       welche         durch       Codieren     eines
Prädiktionsfehlersignals - des Differenzsignals S2 - erhalten wurden. Dieses basiert
auf einer blockweisen Prädiktion, da es die Differenz des Prädiktionssignals S1 und

                                       - 38 -


des Eingangsbildsignals Din repräsentiert (erster Teil von Merkmal 7.2 „receiving a
coded video signal comprising coded video data that include coded blocks of
frequency domain data and/or coded blocks of spatial domain data obtained by
coding a prediction error signal established by block based motion estimation“).


Ferner ermittelt der Differenzrechner 8 das Differenzsignal S2 insbesondere im
Rahmen einer Inter-Frame-Codierung (Spalte 4, Zeile 39 bis 54). In diesem
Zusammenhang lehrt NK10, dass die von dem Prädiktor 5 des Codiersystems DV1
erzeugten Verwaltungsdaten Bewegungsvektoren (Spalte 5, Zeile 19 bis 25)
umfassen, die vom Prädiktor 43 des Decodiersystems DV2 zur Erzeugung eines
Prädiktionssignals S24 verwendet werden, welches zu den rekonstruierten
Differenzsignalen S22 bzw. S23 addiert wird, um die rekonstruierten Daten DOUTX
zu erzeugen (Spalte 6, Zeile 42 bis Spalte 7, Zeile 11). Dem Fachmann ist geläufig,
dass solche Bewegungsvektoren insbesondere dann verwendet werden, wenn bei
einer Inter-Frame-Codierung die Relativpositionen einander entsprechender
Bildblöcke unterschiedlicher Frames angegeben und beim Erzeugen eines
Prädiktionssignals Objektbewegungen kompensiert werden sollen, die zwischen
den Aufnahmezeitpunkten dieser Frames stattgefunden haben, so dass sich die
zeitliche Redundanz der zu codierenden Bildinformation reduziert. Da das
Decodiersystem DV2 die Codierschritte des Codiersystems DV1 rückgängig macht,
ist   auch   das   von   dem     Prädiktor      5   erzeugte   Prädiktionssignal   S1
bewegungskompensiert. Da das Eingangsbildsignal DIN blockweise an den
Differenzrechner 8 zur Erzeugung des Differenzsignals S2 übertragen wird (vgl.
Spalte 4, Zeile 39 bis 46), ist es auch erforderlich, dass das Prädiktionssignal S1
blockweise verarbeitet wird.


Somit entnimmt der Fachmann der NK10 auch, dass die im Codiersystem DV1
ausgeführte blockbasierte Prädiktion bewegungskompensiert ist, wodurch sich die
zeitliche Redundanz der zu codierenden Bildinformation reduziert (verbleibender
Teil von Merkmal 7.2).

                                          - 39 -


1.4   Weiterhin werden die Videodaten anhand eines im Bitstrom mitübertragenen
DCT/NTC-Schaltsignals entweder im Frequenzbereich durch die Blöcke 32 und 34
oder im Ortsbereich durch die Blöcke 32, 37, 38, 39 und ggf. 36 von dem
Decodiersystem DV2 tatsächlich („effectively“) decodiert (Spalte 18, Zeile 63 bis
Spalte 19, Zeile 2 i. V. m. Figur 2). Da der Fachmann in diesen Blöcken
insbesondere verschiedene Hardware-Komponenten erkennt, ist auch Merkmal 7.3
in NK10 offenbart.


1.5   Zum Decodieren wird eine inverse skalare Quantisierung sowohl im Orts- als
auch im Frequenzbereich verwendet (Figur 2, Blöcke 34 und 38). Die skalare Natur
der   inversen     Quantisierung    im   Frequenzbereich      ergibt    sich      aus   dem
koeffizientenweise ausgeführten Schritt „QUANTIZING“ in Figur 3 i. V. m. Spalte 7,
Zeile 37 bis 45; für den Ortsbereich folgt dies z.B. daraus, dass der
Quantisierungsschritt, mit dem gemäß Figur 5 (B), (C) und Figur 17 (B), (C) der
Block K12 in den Block K13 umgewandelt wird, separat für jeden einzelnen
Abtastwert ausgeführt wird; s. ferner auch Figur 6 i. V. m. Spalte 8, Zeile 20 bis 40,
insbesondere die werteweise ausgeführte Gleichung (2), oder auch die
Gleichungen (13) und (17).


Damit liegt Merkmal 7.4 vor.


1.6   Zum Decodieren der in dem quantisierten Signal S4 enthaltenen
quantisierten Koeffizienten und der in den quantisierten Signalen S11 und S12
enthaltenen quantisierten Abtastwerte werden im Decodiersystem DV2 sowohl im
Frequenz-    als     auch     im   Ortsbereich     die    Methoden     „inverse     variable
Längencodierung“ (Figur 2, Block 32; vgl. auch Spalte 18, Zeile 49 bis 55) und
„inverse Quantisierung“ (Figur 2, Blöcke 34 und 38) verwendet. Zudem wird in
beiden Bereichen ein inverser Scan ausgeführt. Für den Frequenzbereich ergibt
sich dies, weil die gemäß Figur 3 i. V. m. Spalte 7, Zeile 45 bis 51 gescannten
entropiedecodierten         DCT-Koeffizienten      nach     der   inversen         variablen
Längencodierung in Block 32 in eine blockweise Anordnung gebracht werden
müssen, um blockweise weiterverarbeitet und schließlich gemäß Spalte 6, Zeile 64
bis 67 zu dem Prädiktionssignal des Prädiktors 43 addiert werden zu können; im

                                        - 40 -


Ortsbereich wird der (inverse) Scan von dem Block 37 gemäß einer an die
Ortsbereichsdaten angepassten Reihenfolge durchgeführt, vgl. z.B. Figur 17 (C) i.
V. m. Figur 14 (C) sowie Spalte 11, Zeile 23 bis 39 i. V. m. Spalte 19, Zeile 9 bis 14.


Damit sind NK10 drei Teilschritte zu entnehmen, die sowohl im Orts- als auch im
Frequenzbereich zur Decodierung der quantisierten Koeffizienten bzw. Abtastwerte
eingesetzt werden. Je nach Teilschritt wird in beiden Bereichen die Zielsetzung
verwirklicht, quantisierte Größen einer inversen variablen Längencodierung zu
unterziehen, entropiedecodierte Größen invers zu quantisieren oder invers zu
scannen.


Somit kann jeder einzelne dieser Teilschritte, aber auch die Gesamtheit aller dieser
Teilschritte als „dieselbe Methode“ im Sinne von Merkmal 7.5.1 angesehen werden.


Damit wird das Merkmal 7.5.1 realisiert, wenn das aus NK10 bekannte
Decodierverfahren ausgeführt wird.


1.7    Weiterhin ist NK10 zu entnehmen, dass das entropiecodierte VLC-Signal S6
in der inversen variablen Längencodiereinheit 32 gemäß einer variablen
Längencodierung („VLC“) decodiert wird, so dass sich ein decodiertes quantisiertes
Signal S21 ergibt, auf dessen Basis das ursprüngliche Differenzsignal S2 (bis auf
Quantisierungsfehler) als Signal S22 bzw. S23 wiederhergestellt wird (Spalte 5,
Zeile 32 bis 67).


Damit wird der erste Teil von Merkmal 7.5.2 („wherein the decoding of the
quantized coefficients and of the quantized samples is carried out according to
VLC”) verwirklicht.


Laut   NK10    werden    im   Frequenz-    und    im   Ortsbereich   unterschiedliche
Codiertabellen verwendet, weil sich die statistischen Eigenschaften der in den
Frequenzbereich transformierten und der im Ortsbereich codierten Signale
unterscheiden. Die Auswahl dieser Tabellen orientiert sich daran, dass die durch
die DCT-Einheit 1 und die NTC-Einheit 2 codierten Daten unterschiedliche

                                         - 41 -


statistische Eigenschaften besitzen, und wird konkret anhand des von der
Codiermethoden-Umschalt-Beurteilungseinheit 3 bereitgestellten Umschaltsignals
S20 ausgeführt, welches anhand der Bildinhalte des jeweils zu codierenden Blocks
festgelegt wird (Spalte 18, Zeile 56 bis 62 i. V. m. Spalte 6, Zeile 9 bis 12). Auf Basis
dieses Umschaltsignals wird das Codierverfahren dynamisch an die zu codierenden
Bildinhalte angepasst.


Dies genügt allerdings noch nicht, um die variable Längencodierung auch als
„kontextadaptiv“ bezeichnen zu können, da die Bildinhalte des jeweils zu
codierenden Blocks, anhand dessen das Umschaltsignal S20 festgelegt wird, keiner
Information entsprechen, die bereits zuvor codiert worden ist.


Der verbleibende Teil von Merkmal 7.5.2 - eine kontextadaptive Ausbildung der
variablen Längencodierung im Orts- und im Frequenzbereich - geht somit nicht aus
NK10 hervor.


Dem Fachmann ist jedoch bewusst, dass eine Anpassung der Codierung an den
Kontext generell zu einer Erhöhung der Codiereffizienz führt und dass hierzu
geeignete     kontextadaptive     Codierverfahren      vor    dem     Prioritätstag    in
Videocodierstandards Einzug gefunden hatten (z.B. „CAVLC“ im H.264/AVC-Standard, zum Nachweis s. etwa NK1, Abstract und Abschnitt 3; NK7, Abschnitt
2.1.5 und NK11, Seite 7). Da der Fachmann immer nach technischen
Verbesserungen strebt, liegt es für ihn auf der Hand, auch die in NK10 beschriebene
variable Längencodierung kontextadaptiv zu gestalten, um so die Codiereffizienz zu
steigern. Dazu wird er z.B. Referenztabellen für das Codieren der quantisierten
DCT-Koeffizienten und das Codieren der Werte des quantisierten Signals S11 (vgl.
Spalte 18, Zeile 56 bis 61) in beiden Bereichen anhand von Informationen
auswählen, die in einem jeweiligen Bereich zuvor codiert worden sind. Dadurch wird
die (inverse) variable Längencodierung an die jeweiligen Anforderungen angepasst,
die sich im Orts- und im Frequenzbereich stellen.

                                            - 42 -


Somit gelangt der Fachmann zum verbleibenden Teil von Merkmal 7.5.2 und damit
zur vollständigen Lehre des Patentanspruchs 7 des Streitpatents, ohne erfinderisch
tätig zu werden.




2.     Der   Argumentation       der      Beklagten,    der   Gegenstand        des   erteilten
Patentanspruchs 7 beruhe gegenüber der Lehre der Druckschrift NK10 auf einer
erfinderischen Tätigkeit, kann nicht beigetreten werden.


2.1   Die Beklagte bringt vor, in dieser Druckschrift sei nicht gezeigt, dass die NTC-Einheit 2 auch bei der Codierung des Prädiktionsfehlers einer Inter-Prädiktion
(Merkmal 7.2) vorgesehen wäre. Das Prädiktionsbild K12 werde in NK10
ausgehend von dem ursprünglichen Bewegtbildsignal („original picture“) ermittelt,
dem in den Figuren 5 und 17 das Originalbild K11 mit für einen Prädiktionsfehler im
8-Bit-Bildformat untypisch hohen Pixelwerten entspreche. Der Fachmann habe
keinen Anlass, die zusätzliche Intra-Block-Prädiktion wegzulassen, die das
Eingangssignal um einen typischen Basiswert BASE vermindere.


Dieses Argument vermag nicht zu überzeugen.


So zeigt NK10 ausdrücklich, dass ein im Rahmen einer Inter-Frame-Codierung aus
einer Subtraktion zwischen dem Prädiktionssignal S1 und einem Eingangsbildsignal
DIN hervorgegangenes Differenzsignal S2 in den Intra-Block-Prädiktor 21 der NTC-Einheit 2 eingespeist und von diesem verarbeitet wird (vgl. Spalte 4, Zeile 47 bis 56
i. V. m. Spalte 5, Zeile 34 bis 39 und Spalte 6, Zeile 23 bis 25). Der Fachmann setzt
das Differenzsignal S2 insbesondere deshalb mit einem Prädiktionsfehler einer
Inter-Prädiktion    gleich,   weil   es    laut   NK10      berechnet     wird,   indem    ein
Prädiktionssignal von einem Eingangsbildsignal subtrahiert wird und sich aus der
Verwendung         von    Bewegungsvektoren            im     Prädiktor    43     auf     eine
Bewegungskompensation des Differenzsignals schließen lässt. Da es keinen Sinn
ergibt, ein Signal zunächst von dem Intra-Block-Prädiktor 21 verarbeiten zu lassen,
aber dann nicht weiter in den Blöcken 22, 23 und 6 zu codieren und an das
Decodiersystem zum Zwecke der Decodierung zu übertragen, folgert der

                                          - 43 -


Fachmann, dass das auf die vorstehend beschriebene Weise erhaltene
Differenzsignal S2 auch von der NTC-Einheit 2 vollständig codiert, an das
Decodiersystem DV2 übertragen und dort decodiert wird.


Dem steht nicht entgegen, dass gemäß dem in Figur 5 (A) i. V. m. Spalte 7, Zeile 12
und 13 sowie Spalte 7, Zeile 65 bis Spalte 8 Zeile 6 („when one block […] of picture
data, which contains an edge of a pattern at the left bottom corner, shown as original
picture K11 […], is fed as difference signal S2, […]“) gezeigten Ausführungsbeispiel
der NK10 ein „Originalbild“ in die Intra-Block-Prädiktionseinheit 21 eingespeist wird.
Denn dieser Textabschnitt lässt die Möglichkeit offen, dass nicht nur „unechte“
Differenzsignale     K11,     sondern      auch     andere     „echte“,    aus     einer
Subtraktionsoperation     resultierende    Differenzsignale   S2,   die   einem    Inter-Prädiktionsfehler entsprechen, von der NTC-Einheit 2 weiterverarbeitet werden
können. Zudem ist es nicht gänzlich ausgeschlossen, dass der in Figur 5 (A)
gezeigte Block K11 einen Prädiktionsfehler repräsentiert (z.B. wenn in einem Frame
erstmalig eine sehr helle Bildstruktur mit einer Kante vor einem sehr dunklen
Bildhintergrund erscheint).


Des Weiteren weisen weitere Textstellen der NK10 auf die Codierung eines
Prädiktionsfehlers einer Inter-Prädiktion hin. So ist aus Spalte 2, Zeile 49 bis 54 („the
coding mode is switched to the DCT or intra-block predictive coding mode for each
unit area (or block) of intra- or inter-picture signal“) abzuleiten, dass die
Umschaltung zwischen einer Verarbeitung in der DCT-Codiereinheit 1 und der NTC-Einheit 2 unabhängig von der Umschaltung zwischen einer Inter- und einer Intra-Frame-Codierung vorgenommen wird, woraus folgt, dass insbesondere auch ein
Inter-Prädiktionsfehler („inter-picture signal“) von der NTC-Einheit 2 codiert wird.
Damit in Übereinstimmung ist, dass ein Makroblock gemäß NK10 offensichtlich
voneinander unabhängige Informationen darüber enthalten kann, ob er durch ein
Inter- oder ein Intra-Frame-Codieren erzeugt wurde und ob er Blöcke umfasst, die
gemäß der NTC-Methode codiert sind (Spalte 16, Zeile 61 bis Spalte 17, Zeile 2; s.
auch Spalte 17, Zeile 3 bis 21, insbesondere Zeile 8 bis 10, 13 und 14 sowie 20 und
21). Auch werden die Signale S14 und S23, die dem decodierten Differenzsignal S2
im Ortsbereich entsprechen, in NK10 weiterhin als Differenzsignale bezeichnet (vgl.

                                            - 44 -


Figur 1, Blöcke 21, 22, 25 und 26 i. V. m. Spalte 5, Zeile 64 bis Spalte 6, Zeile 5 -
„predictive difference signal S14“; Figur 2 i. V. m. Spalte 6, Zeile 32 bis 57 -
„reproduced difference signal S23“). Diese Signale repräsentieren also auch nach
der Decodierung eine Differenz.


Für den Fachmann ist somit klar, dass das Decodiersystem DV2 der NK10
insbesondere auch ein Prädiktionsfehlersignal erhalten und verarbeiten kann, das
im Rahmen einer Inter-Frame-Codierung durch Reduzieren von zeitlicher
Redundanz durch eine blockbasierte Bewegungsschätzung erhalten worden ist.


2.2     Die Beklagte wendet ferner ein, Merkmal 7.5.1 gehe nicht aus NK10 hervor.
Diese    Druckschrift    lehre,   im     Ortsbereich   anders    zu     verfahren     als    im
Frequenzbereich. Auch führten die Blöcke 34 und 38 jeweils nur einen Teilschritt
der beiden Decodiermethoden im Orts- und Frequenzbereich durch; dies könne
nicht mit dem Ausführen derselben Methode gleichgesetzt werden. Des Weiteren
verzichte der Frequenzbereichszweig auf den Teilschritt der inversen Intra-Block-Prädiktion, bei der es sich nicht um eine bloße Anpassung eines genauso im
Frequenzbereichszweig verwendeten Teilschritts an die Eigenschaften der
Abtastwerte im Ortsbereich handele.


Auch diese Einwände verfangen nicht.


So wird Merkmal 7.5.1 gemäß Abschnitt I.4.1.6 bereits dann realisiert, wenn
mindestens ein Teilschritt eines Decodierverfahrens im Frequenz- und im
Ortsbereich     gleich    ist     (was     Anpassungen      an        die   Codier-         bzw.
Decodieranforderungen in diesen Bereichen umfassen kann). Es ist somit
unerheblich, ob die Decodierverfahren im Orts- und Frequenzbereich noch weitere
Teilschritte aufweisen, in denen sie sich unterscheiden, und ob die Menge der drei
Teilschritte „inverse Quantisierung”, „inverser Scan” und „Entropiedecodierung”
bereits alle Decodierschritte umfasst, die gemäß NK10 in beiden Bereichen
ausgeführt werden.

                                            - 45 -


2.3    Die Beklagte macht ferner geltend, NK10 führe bewusst zusätzliche
Verarbeitungsblöcke ein, was insbesondere aus Spalte 11, Zeile 4 bis 13 ersichtlich
sei.


Auch sehe das Streitpatent vor, die Transformation unter gewissen Umständen zu
überspringen bzw. ganz wegzulassen; im Gegensatz dazu ersetze die inverse Intra-Block-Prädiktion im Block 21 die DCT-Transformation im Block 11. Dadurch
versuche die NK10, die fehlende Transformation im Ortsbereich durch eine
alternative   Maßnahme       auszugleichen       und     die    Decodierschritte    an   die
Eigenschaften der Abtastwerte im Ortsbereich anzupassen.


Auch diese Einwände sind nicht überzeugend.


2.3.1 So folgt aus Spalte 11, Zeile 3 bis 8 der NK10 („The functions of the quantizer
and inverse quantizer described with the above first to fourth adaptive quantizing
methods are the same as those broadly used in the […] DCT […] coding except for
the execution of the subtraction or addition of a typical value of block”), dass bei der
ersten bis vierten adaptiven Quantisierungsmethode nur der Schritt einer Addition
bzw. Subtraktion des typischen Werts in eine bereits existierende (inverse) adaptive
Quantisierungsmethode integriert wird. Entsprechendes zeigen auch die inversen
Quantisierungsgleichungen (2), (13) und (17). Aus Spalte 11, Zeile 8 bis 13 kann
dann   allenfalls    abgeleitet   werden,     dass     zur     Umsetzung   der     (inversen)
Quantisierungsoperationen im Frequenzbereichszweig bzw. der in den Blöcken 22
bzw. 38 ausgeführten (inversen) Quantisierungsoperationen im Ortsbereichszweig
vorteilhafterweise    derselbe    (inverse) Quantisierer         bzw.   dieselbe    (inverse)
Quantisierungshardware verwendet werden kann.


2.3.2 Zwar trifft es zu, dass sich sowohl die Frequenztransformation in Block 11 als
auch die inverse Intra-Block-Prädiktion in Block 21 auf die von den Blöcken 12 und
22 quantisierten Werte auswirkt und der Block 21 den Block 11 in diesem Sinne
„ersetzt“. Für die Beurteilung, ob gemäß Merkmal 7.5.1 „dieselbe Methode“ im
Frequenz- und im Ortsbereich durchgeführt wird, kommt es jedoch nur auf einen
Vergleich der im Decodiersystem DV2 im Frequenzbereich bis zur inversen

                                       - 46 -


Frequenztransformation in Block 35 bzw. im Ortsbereich bis zur Rekonstruktion der
Differenzsignale S22 und S23 ausgeführten Verfahrensschritte an. Aus diesem
Vergleich ergibt sich (vgl. Abschnitt II.1.6), dass Merkmal 7.5.1 bei Ausführung des
aus NK10 bekannten Verfahrens erfüllt ist.


Im Übrigen kann genausogut argumentiert werden, dass der Block 21 den Block 11
gerade nicht ersetzt, da diese Blöcke ganz verschiedene Funktionen haben: so
dient Block 11 der Umwandlung der in einem Bildblock enthaltenen Bildinformation
in eine andere Repräsentation, wohingegen Block 21 diese Bildinformation (durch
Subtraktion des typischen Werts) in den meisten Fällen auch tatsächlich reduziert.
Der entsprechende Einwand der Beklagten führt somit nicht weiter.


2.4    Weiterhin ist die Beklagte der Auffassung, in NK10 fehle es an codierten
Blöcken von Ortsbereichsdaten im empfangenen codierten Videosignal (vgl.
Merkmal 7.2) und an einem (Entropie-)Decodieren der quantisierten Abtastwerte
(vgl. Merkmal 7.5.2).


Zur Begründung führt sie sinngemäß aus, der im Codiersystem in Block 21
bestimmte Intra-Prädiktionsfehler S10, der sich von den Ortsbereichsdaten
unterscheide, die dem Block 21 des Codiersystems zugeführt werden, werde im
Ortsbereichszweig des Decodiersystems DV2 von dem „BASE“-Wert getrennt
decodiert. Dies ergebe sich daraus, dass der „BASE“-Wert als Teil eines
Übertragungsmanagementsignals S7 an das Decodiersystem übertragen, dort von
den quantisierten Prädiktionsfehlerdaten getrennt und als Prädiktionsmodussignal
S25 an den Prädiktor 43 übertragen werde. Die Ortsbereichsdaten würden erst in
der Summierungsreproduktionsschaltung 41 aus den Signalen S22 und S24
rekonstruiert.


Auch    diese    Argumente    führen    zu      keiner   anderen   Beurteilung   der
streitpatentgemäßen Lehre.


So erfordert Merkmal 7.2 lediglich, dass die empfangenen codierten Videodaten
codierte Blöcke von Ortsbereichsdaten beinhalten. Dies trifft insbesondere für die

                                          - 47 -


codierten Blöcke des Intra-Prädiktionsfehlers S10 zu, da diese im Ortsbereich
codiert   worden     sind.    Diese   Blöcke   werden   in   der   inversen    variablen
Längencodiereinheit 32 des Decodiersystems DV2 entropiedecodiert und bilden
einen Bestandteil des decodierten quantisierten Signals S21 (vgl. Spalte 6, Zeile 32
bis 50; ein Entropiedecodieren des quantisierten Intra-Prädiktionsfehlers S10 (vgl.
Figuren 5 (C), 17 (C)) ist z.B. in den Figuren 5 (E), (F) und 17 (E), (F) illustriert).
Somit kommt zum Decodieren der quantisierten Abtastwerte eine inverse - nach
Abschnitt II.1.7 auch kontextadaptive - variable Längendecodierung zum Einsatz.
Mehr verlangen auch die Merkmale 7.5.1 und 7.5.2 nicht; insbesondere kann aus
dem Wortlaut dieser Merkmale nicht abgeleitet werden, dass das Decodieren der
quantisierten Koeffizienten bzw. Abtastwerte nach der Entropiedecodierung
abgeschlossen sein muss und bereits dann die ursprünglichen Werte dieser Größen
vorliegen.


Falls der typische Wert eines Blocks (z.B. „BASE“) gleich Null ist, ist außerdem ein
Block des prädiktiven Codiersignals S10, der vom Block 21 des Codiersystems DV1
ausgegeben wird, mit den Ortsbereichsdaten identisch, die dem Block 21 zugeführt
werden - und damit insbesondere mit dem „Originalbild“ („original picture“) K11. In
diesem Fall wird das ursprüngliche Differenzsignal S2 im Ortsbereich quantisiert,
entropiecodiert,     an      das   Decodiersystem    DV2     übertragen       und   dort
entropiedecodiert.


2.5    Im Hinblick auf Merkmal 7.5.2 führt die Beklagte aus, der Fachmann würde
eine adaptive Codierung wie CABAC oder CAVLC nicht als geeignetes
Codierungsverfahren ansehen, da die adaptiven Verfahren auch frühere Codes zur
Adaption berücksichtigten, was die Adaptionsfähigkeiten von CABAC und CAVLC
negativ beeinflussen könne. Zudem gebe die NK11 keinen Hinweis darauf, das
CABAC- oder CAVLC-Verfahren für die Codierung bzw. Decodierung von um einen
typischen Basiswert BASE verminderten Daten geeignet sei. Nur weil ein
bestimmtes Codierverfahren in einer bestimmten Situation (z.B. für die Codierung
von Transformationskoeffizienten) erfolgreich eingesetzt werde, bedeute dies nicht
notwendigerweise, dass das gleiche Codierverfahren auch in einer anderen
Situation gut funktioniere.

                                         - 48 -




Auch diese Einwände vermögen nicht zu überzeugen.


Zwar trifft es zu, dass das gemäß dem H.264/AVC-Standard verwendete CAVLC-Verfahren nur hinsichtlich der Entropiecodierung der Transformationskoeffizienten
kontextadaptiv ist (vgl. NK7, Satz vor Abschnitt 2.1.5.1 - „in the case of CAVLC,
context adaptivity is used only for transform coefficients“; NK11, Seite 7, zweiter
Absatz, erster Satz). Jedoch kann aus dem Umstand, dass dabei eine Codierung
von quantisierten Abtastwerten im Ortsbereich gar nicht vorgesehen ist, nicht
geschlossen    werden,    dass   es     grundsätzlich    nicht   angebracht     ist,   ein
kontextadaptives Entropiecodierverfahren zur Codierung solcher Abtastwerte im
Ortsbereich    zu   verwenden.     Im    vorliegenden     Fall   ist     eine   Huffman-Entropie(de)codierung im Ortsbereich bereits aus NK10 bekannt. Dem Fachmann
ist es ohne Weiteres möglich, diese etwa durch eine entsprechend angepasste
Auswahl von Referenztabellen (vgl. NK10, Spalte 18, Zeile 56 bis 62) für den
Frequenz- und den Ortsbereich kontextadaptiv zu gestalten, was ihm eine Erhöhung
der Codiereffizienz verspricht, wenn die Bildinformationen der zu codierenden
Blöcke jeweils innerhalb eines der beiden Bereiche räumlich und zeitlich korreliert
sind. Letzteres ist bei typischen Videodaten der Fall.




3.     Somit ist der Gegenstand des erteilten Patentanspruchs 7 für den Fachmann
ausgehend von der Lehre der Druckschrift NK10 nahegelegt.




4.     Auch der Gegenstand des Patentanspruchs 13 des Streitpatents beruht im
Hinblick auf die aus der NK10 bekannte Lehre nicht auf einer erfinderischen
Tätigkeit.


Für   diesen   Patentanspruch     gelten    die   vorstehenden         Ausführungen    zu
Patentanspruch 7 (s.o., Abschnitte II.1 und II.2) entsprechend.

                                         - 49 -


Insbesondere zeigt die NK10 in Figur 2 ein Decodiersystem zur Ausführung des in
NK10 beschriebenen hybriden Decodierverfahrens (Merkmal 13.1). Der Puffer 31
des Decodiersystems stellt ein Empfangsmittel zum Empfangen der im Frequenzund Ortsbereich insbesondere durch eine Inter-Frame-Codierung codierten
Prädiktionsfehlerblöcke dar (vgl. Spalte 18, Zeile 64 und 65; Merkmal 13.2). Ferner
bestimmt die inverse variable Längencodierungseinheit 32 anhand eines
decodierten Schaltsignals, ob ein jeweiliger Block gemäß DCT oder gemäß NTC
decodiert werden soll, und wählt anschließend das entsprechende Verfahren aus
(Spalte 18, Zeile 66 bis Spalte 19, Zeile 2). Diese Einheit bildet daher ein adaptives
Steuermittel zum adaptiven Bestimmen im Sinne von Merkmal 13.3.


Die übrigen Merkmale 13.4 bis 13.5.2 sind mit den Merkmalen 7.4 bis 7.5.2 identisch
und werden - wie oben zu Patentanspruch 7 beschrieben - dem Fachmann durch
NK10 nahegelegt.




5.     Somit haben die angegriffenen Patentansprüche 7 und 13 des Streitpatents
keinen Bestand. Das Streitpatent ist daher im Umfang dieser Patentansprüche für
nichtig zu erklären.




                                          III.


Das Streitpatent ist ferner in keiner der Fassungen der zur Akte gereichten
Hilfsanträge 1 bis 5 patentfähig.


1.     Dem Hilfsantrag 1 kann nicht stattgegeben werden, weil der Gegenstand
seines Patentanspruchs 1 ebenfalls ausgehend von Druckschrift NK10 nicht auf
einer erfinderischen Tätigkeit beruht.


1.1    Patentanspruch     7   gemäß      Hilfsantrag   1   unterscheidet   sich   von
Patentanspruch 7 gemäß Hauptantrag in der eingereichten englischsprachigen
Fassung dadurch, dass Merkmal 7.2 durch das Merkmal

                                        - 50 -




7.2Hi1         receiving a coded video signal comprising coded video data that
               include coded blocks of values which represent motion-compensated
               prediction error samples in the frequency domain data and/or coded
               blocks of values which represent motion-compensated prediction error
               samples in the spatial domain data,
               with the coded blocks of values obtained by coding prediction error
               samples of a prediction error signal established by reducing temporal
               redundancy by block based motion estimation;


ersetzt wird und dass nach Merkmal 7.4 das zusätzliche Merkmal


7.4.1Hi1       wherein the inverse quantization comprises inverse quantizing the
               values which represent motion-compensated prediction error samples
               in the spatial domain back into the corresponding motion-compensated prediction error samples,


eingeschoben wird (bei allen Hilfsanträgen sind Änderungen der Merkmale des
erteilten Patentanspruchs 7 durch Unter- und Durchstreichungen kenntlich
gemacht).


Die neuen Merkmale bringen zum Ausdruck, dass in den vom Decodierer
empfangenen codierten Blöcken Werte enthalten sind, die bewegungskompensierte
Prädiktionsfehler-Abtastwerte repräsentieren, wobei sich diese Abtastwerte - bis auf
mögliche       Quantisierungsfehler    -    unmittelbar    aus     dem     inversen
Quantisierungsschritt ergeben (vgl. Merkmal 7.4.1Hi1 - „inverse quantizing the
values […] back into the […] prediction error samples“).


1.2      Eine Patentfähigkeit lässt sich mit den Merkmalen 7.2Hi1 und 7.4.1Hi1 nicht
begründen.


1.2.1 Da das im Ortsbereich blockweise codierte und an das Decodiersystem DV2
in codierter Form übertragene quantisierte Signal S11 aus dem Differenzsignal S2

                                          - 51 -


hervorgegangen ist, repräsentiert es - ebenso wie das Differenzsignal S2, das
prädiktive Codiersignal S10 oder das im Frequenzbereich blockweise codierte
quantisierte    Signal    S4     -   bewegungskompensierte        Abtastwerte    eines
Prädiktionsfehlersignals (s.o., Abschnitte II.1.3, II.2.1).


Somit wird Merkmal 7.2Hi1 im Rahmen der aus NK10 bekannten Lehre realisiert.


1.2.2 Merkmal 7.4.1Hi1 leitet der Fachmann aus NK10 wie folgt ab:


a)     Die im Ortsbereich vorgenommene NTC-Codierung umfasst eine adaptive
Quantisierung zur Reduktion von Verzerrungen (dies ergibt sich z.B. aus Spalte 3,
Zeile 10 bis 14; Spalte 8, Zeile 20 bis 24). Diese Quantisierung ist insbesondere
deshalb als adaptiv zu bezeichnen, weil von den einzelnen Abtastwerten ein
typischer, für einen Block repräsentativer Wert subtrahiert wird, der auf den
Abtastwerten eines homogenen Bereichs eines jeweiligen Bildblocks basiert (vgl.
NK10, Abstract sowie Spalte 3, Zeile 10 bis 13 - „adaptive quantizing by transmitting
a typical value of the block and quantizing width”).


b)     Gemäß dem in Spalte 7, Zeile 66 bis Spalte 8, Zeile 19 i. V. m. Spalte 5,
Zeile 36 bis 42 und den Figuren 5 (A) bis (C) beschriebenen Beispiel wird dabei vom
Intra-Block-Prädiktor 21 ein typischer Mittelwert „BASE” eines homogenen
Bildbereichs eines Blocks ermittelt, von dessen Abtastwerten subtrahiert und die
resultierende Differenz von dem Quantisierer 22 quantisiert. Dies gilt entsprechend
für das in Figur 17 gezeigte Beispiel, bei dem keine Differentiation im Differentiator
24 vorgenommen wird.


Daraus folgt, dass die Blöcke 21 und 22 gemeinsam eine adaptive Quantisierung
realisieren, welche die Subtraktion des typischen Werts umfasst. Diese Subtraktion
kann als eine blockweise Anpassung der Quantisierung an das Erfordernis einer
effizienten Codierung von Abtastwerten angesehen werden, die sich in räumlich
homogenen       Bereichen      der   einzelnen     Bildblöcke   befinden   und   nicht
frequenztransformiert werden sollen.

                                        - 52 -


Entsprechendes gilt für die vier, in NK10 ab Spalte 8, Zeile 20 ausdrücklich als
„adaptiv” bezeichneten Quantisierungsmethoden. Die erste dieser Methoden
umfasst die in den Quantisierungsgleichungen enthaltene Subtraktion eines
eindimensionalen, zeilen- oder spaltenweisen gebildeten blockindividuellen
Mittelwerts M, (vgl. Spalte 8, Zeile 20 bis 40 - „A first method of adaptive quantizing
[…] The quantizing code Lq is given as following: Lq = (L – M)//Q”). In gleicher Weise
wird bei der zweiten Methode ein minimaler Wert am Rande eines Blocks subtrahiert
(vgl. Spalte 8, Zeile 52 bis 55), und bei der dritten und vierten Methode der kleinere
Wert X1 von zwei Werten X1, X2, die jeweils an einem Ende einer
(eindimensionalen)    Zeile    oder   Spalte     eines   Blocks   liegen,   bzw.    im
zweidimensionalen Fall der für X1 repräsentative Wert „BASE1” bzw. „BASE” (vgl.
Spalte 9, Zeile 10 bis Spalte 10, Zeile 67, insbesondere Spalte 9, Zeile 24 und 25,
Spalte 10, Zeile 14 bis 21 und 63 bis 67 sowie Gleichungen (12) bis (14) und (17)).
Aus Spalte 5, Zeile 36 bis 39 ergibt sich, dass auch bei diesen vier adaptiven
Methoden ein typischer Wert durch den Intra-Block-Prädiktor 21 von den
Pixelwerten eines Blocks subtrahiert wird.


c)     Im Zusammenhang mit der Decodierung des Differenzsignals S2 lehrt NK10,
dass der inverse Intra-Block-Prädiktor 39 des Decodiersystems DV2 die
komplementäre Struktur des Intra-Block-Prädiktors 21 des Codiersystems DV1
besitzt (Spalte 19, Zeile 12 bis 14). Daraus folgt in Verbindung mit Spalte 5, Zeile
36 bis 39 unmittelbar, dass der inverse Intra-Block-Prädiktor 39 den typischen Wert
zu dem Signal des inversen Quantisierers 38 addiert (vgl. die Transformation von
Block K20 in Block K21 in Figur 17 (G), (F), bei der der Wert 198 hinzuaddiert wird;
im Hinblick auf die Addition des typischen Werts M bzw. X1 vgl. z.B. Spalte 8, Zeile
37 bis 40 - „The restored value LX is given as following: LX = Lq * Q + M” sowie die
Gleichungen (13) und (17)).


Somit machen die Blöcke 38 und 39 die im Codiersystem DV1 in den Blöcken 21
und 22 vorgenommene adaptive Quantisierung wieder rückgängig und führen daher
gemeinsam eine inverse (adaptive) Quantisierung aus, aus der sich das
Differenzsignal S2 (bis auf Quantisierungsfehler) als rekonstruiertes Differenzsignal
S23 ergibt (siehe auch Spalte 6, Zeile 50 bis 57 und 64 bis 67 i. V. m. Figur 2 - „The

                                         - 53 -


decoded quantized signal S21 is […] inversely converted through an inverse
quantizer 38 and an inverse intra-block predictor 39, thus obtaining a reproduced
difference signal S23“).


Damit kann die im Rahmen der (inversen) Intra-Block-Prädiktion vorgenommene
Subtraktion (Addition) des typischen Werts unter eine (inverse) adaptive
Quantisierung subsumiert werden.


d)     Für den speziellen Fall, dass Blöcke verarbeitet werden, die im Codiersystem
DV1 den Differentiator 24 durchlaufen haben, und BASE1 der typische Wert eines
Blocks ist, zeigt NK10 außerdem, dass erst der Prädiktor 43 und der Addierer 41
des Decodiersystems DV2 den Wert BASE1 zu den invers quantisierten
Koeffizienten K18 addieren, um einen rekonstruierten Bildblock K19 zu erhalten
(vgl. Spalte 12, Zeile 24 bis 33 i. V. m. Figuren 5 (F), (G)). In diesem Fall wirken die
Komponenten 38, 39, 41 und 43 zusammen, um die adaptive Quantisierung im
Ortsbereich rückgängig zu machen.


e)     Damit liefert der inverse Quantisierungsblock 38 des Decodiersystems DV2
die ursprünglichen Abtastwerte des Differenzsignals S2 bis auf einen typischen zu
addierenden Wert, der anschließend durch den inversen Intra-Block-Prädiktor 39
(oder ggf. durch den Prädiktor 43 und den Addierer 41) hinzuaddiert wird. Mit dieser
Addition ist die inverse (adaptive) Quantisierung abgeschlossen. Das bedeutet,
dass die ursprünglichen Werte des Differenzsignals S2 im Ortsbereich bis auf
Quantisierungsfehler unmittelbar nach der inversen (adaptiven) Quantisierung
vorliegen - Merkmal 7.4.1Hi1.


1.2.3 Im Übrigen wird Merkmal 7.4.1Hi1 insbesondere auch dann realisiert, wenn
der typische Wert eines Blocks Null ist.


Dieser Fall liegt z.B. vor, wenn ein Block des Differenzsignals S2 einen homogenen
Bereich aufweist, der im Wesentlichen schwarze Pixel mit Abtastwerten sehr nahe
bei Null enthält. Der typische Wert kann zudem für Inter-Frame-codierte Blöcke
auch generell auf Null gesetzt werden (vgl. Spalte 16, Zeile 8 bis 13), wobei aus

                                       - 54 -


dem Nachsatz „Alternatively, it is possible to transmit the typical value BASE1 even
if the macro-block to be coded is a non-intra-frame coded macro-block” der Zeilen
10 bis 13 folgt, dass zumindest der typische Wert BASE1 bei einer Inter-Frame-Codierung an das Decodiersystem DV2 mitübertragen werden kann.


a)    Falls der typische Wert gleich Null ist, werden die Werte des rekonstruierten
Differenzsignals S23 bereits von dem inversen Quantisierungsblock 38 ausgegeben
(das Signal S23 entspricht in diesem Fall z.B. bereits dem in Figur 17 der NK10
gezeigten Block K20). Zu diesen Werten wird später lediglich noch der typische
Wert Null hinzuaddiert (vgl. z.B. die Transformation des Blocks K20 in den Block
K21 in Figur 17 (F), (G)), was jedoch die Werte selbst nicht verändert.


Auch aufgrund dieser Überlegung kann Merkmal 7.4.1Hi1 aus NK10 abgeleitet
werden.


b)    Entsprechend verhält es sich insbesondere bei den als erste, dritte und vierte
adaptive Quantisierungsmethode bezeichneten Verfahren (vgl. Spalte 8, Zeile 23 ff;
Spalte 9, Zeile 9 ff; Spalte 10, Zeile 25 ff). Bei diesen Verfahren enthält ein
rekonstruierter Block, der aus pixelweisen Operationen der Form LX = Lq*Q in den
Gleichungen (2), (13) und (17) resultiert, bis auf Quantisierungsfehler das
ursprüngliche Differenzsignal S2, falls ein typischer Wert des Blocks (z.B. die Größe
M oder X1) gleich Null ist. Das von Block 38 ausgegebene rekonstruierte
Differenzsignal S23 ändert sich durch die Addition von Null nicht mehr, so dass
Merkmal 7.4.1Hi1 verwirklicht wird.


1.3   Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 7 beruht
die Lehre des Patentanspruchs 1 gemäß Hilfsantrag 1 somit nicht auf einer
erfinderischen Tätigkeit und ist daher nicht patentfähig. Mit seinem Patentanspruch
7 fällt der gesamte Hilfsantrag 1.


Im vorliegenden Fall hat die Beklagte in der mündlichen Verhandlung erklärt, sie
sehe die Patentansprüche gemäß den Hilfsanträgen als jeweils geschlossene
Anspruchssätze an, die jeweils insgesamt beansprucht werden. Dies schließt für

                                         - 55 -


den Hilfsantrag 1 sowie für alle weiteren Hilfsanträge eine separate Betrachtung
einzelner Patentansprüche aus, wenn sich ein Patentanspruch des betroffenen
Anspruchssatzes, wie hier, als nicht patentfähig erweist.




2.       Der Hilfsantrag 2 kann nicht günstiger als der Hilfsantrag 1 beurteilt werden,
weil der Gegenstand seines Patentanspruchs 1 ebenfalls im Lichte der Lehre der
NK10 nicht auf einer erfinderischen Tätigkeit beruht.


2.1      Patentanspruch 7 gemäß Hilfsantrag 2 beruht auf dem erteilten
Patentanspruch 7, wobei Merkmal 7.2 durch das Merkmal


7.2Hi2         receiving a coded video signal comprising coded video data that
               include coded blocks of quantized coefficients in the frequency domain
               data and/or coded blocks of quantized samples in the spatial domain
               data,
               with the coded blocks obtained by coding of a prediction error signal
               established by reducing temporal redundancy by block based motion
               estimation;


ersetzt wird und nach Merkmal 7.4 die neuen Merkmale


7.4.1Hi2       wherein, when the video data are coded in the spatial domain, the
               decoded prediction error signal is directly obtained by inversely
               quantizing the samples,


7.4.2Hi2       and when the video data are coded in the frequency domain, the
               decoded prediction error signal is directly obtained by inversely
               transforming the inversely quantized coefficients from the frequency
               domain to the spatial domain,


eingefügt werden.

                                         - 56 -


Merkmal 7.2Hi2 bringt nun zum Ausdruck, dass die codierten Blöcke von Orts- und
Frequenzbereichsdaten quantisierte Abtastwerte bzw. quantisierte Koeffizienten
umfassen, die durch das Codieren des Prädiktionsfehlersignals erhalten worden
sind.


Die Angaben „the decoded prediction error signal is directly obtained by inversely
quantizing/transforming […]“ in den Merkmalen 7.4.1Hi2 und 7.4.2Hi2 sind dem
Streitpatent    nicht    wörtlich   zu     entnehmen.        Dass     das       decodierte
Prädiktionsfehlersignal hier „direkt“ erhalten wird, bedeutet aus Sicht des
Fachmanns,      dass    das    ursprüngliche      Prädiktionsfehlersignal   -    bis   auf
Quantisierungsfehler - unmittelbar nach der inversen Quantisierung bzw. der
inversen Transformation vorliegt.


2.2     Auch mit den zu Merkmal 7.2Hi2 führenden Änderungen sowie mit den neuen
Merkmalen 7.4.1Hi2 und 7.4.2Hi2 kann eine Patentfähigkeit nicht begründet werden.


2.2.1 Dass die codierten Blöcke des Videosignals quantisierte Abtastwerte im
Ortsbereich bzw. quantisierte Koeffizienten im Frequenzbereich enthalten, welche
durch Codieren des Prädiktionsfehlersignals erhalten wurden (vgl. Merkmal 7.2Hi2),
ergibt sich daraus, dass die Blöcke der quantisierten Signale S4 und S11 auf einer
Codierung der Abtastwerte des Differenzsignals S2 beruhen, jeweils in der VLC-Codiereinheit 6 entropiecodiert werden, in dem aus dieser Entropiecodierung
resultierenden VLC-Signal S6 enthalten sind und in entropiecodierter Form an das
Decodiersystem DV2 übertragen werden (s.o., Abschnitte II.1.1, II.1.3, II.2.1).


Merkmal 7.2Hi2 ist somit erfüllt.


2.2.2 Im Hinblick auf Merkmal 7.4.1Hi2 gilt die vorstehende Argumentation zu
Merkmal 7.4.1Hi1 aus Abschnitt III.1.2 ebenfalls:


a)      Da die Blöcke 38 und 39 - ggf. im Zusammenspiel mit dem Prädiktor 43 und
dem Addierer 41 - gemeinsam eine adaptive inverse Quantisierung im Ortsbereich
durchführen, liegt das ursprüngliche Differenzsignal S2 unmittelbar nach der

                                         - 57 -


adaptiven inversen Quantisierung im Ortsbereich (bis auf Quantisierungsfehler) als
rekonstruiertes Differenzsignal S23 vor (s.o., Abschnitt III.1.2.2).


b)      Wenn der typische zu addierende Wert eines Blocks gleich Null ist, ergibt
sich ein invers quantisierter Block im Ortsbereich bereits unmittelbar aus der
inversen Quantisierung in Block 38, da die Addition des typischen Werts Null die
Abtastwerte des invers quantisierten Blocks nicht mehr verändert (s.o., Abschnitt
III.1.2.3).


Somit wird Merkmal 7.4.1Hi2 sowohl im Fall a) als auch im Fall b) verwirklicht.


2.2.3 Weiterhin ergibt sich das ursprüngliche Differenzsignal S2 bis auf
Quantisierungsfehler unmittelbar - d.h. ohne einen weiteren Decodierschritt - als
Differenzsignal S22 aus der inversen Kosinustransformation in Block 35 (vgl. NK10,
Spalte 6, Zeilen 37 bis 43 und 64 bis 67 - „[…] fed to an inverse discrete cosine
transform circuit 35 to reproduce the difference signal S22“ i. V. m. Figur 2,
Bezugszeichen 35).


Daher ist auch Merkmal 7.4.2Hi2 der NK10 zu entnehmen.


2.3     Somit beruht die Lehre des Patentanspruchs 7 gemäß Hilfsantrag 2 mit
Rücksicht auf die Ausführungen zum erteilten Patentanspruch 7 nicht auf einer
erfinderischen Tätigkeit und ist deswegen nicht patentfähig. Mit seinem
Patentanspruch 7 fällt der gesamte Hilfsantrag 2.




3.      Hilfsantrag   3   hat   keinen    Erfolg,   weil   der   Gegenstand   seines
Patentanspruchs 7 ausgehend von Druckschrift NK10 nahegelegt ist.


3.1     Bei Patentanspruch 7 gemäß Hilfsantrag 3 werden gegenüber dem erteilten
Patentanspruch 7 unmittelbar nach Merkmal 7.2 noch die Merkmale

                                        - 58 -


7.2.1Hi3      wherein the coding of the prediction error signal comprises deciding
              whether to transform the prediction error signal into the frequency domain or to maintain the prediction error signal in the spatial domain,


7.2.2Hi3      and applying the same subsequent coding mechanisms in the spatial
              domain as in the frequency domain;


eingeschoben, sowie unmittelbar nach Merkmal 7.3 noch das Merkmal


7.3.1Hi3      the decoding of the received coded video data comprises inversing
              the coding of the prediction error signal.


3.1.1 Die Merkmale 7.2.1Hi3 und 7.2.2Hi3 betreffen das Codieren durch ein
Entscheiden („deciding”, vgl. Merkmal 7.2.1Hi3) oder durch ein Anwenden von
Codiermechanismen („applying […] coding mechanisms”, vgl. Merkmal 7.2.2Hi3),
d.h. von Teilschritten eines Codierverfahrens.


Hingegen bezieht sich Merkmal 7.3.1Hi3 auf das in Merkmal 7.3 genannte
Decodieren der empfangenen codierten Videodaten, welches ein Umkehren des
Codierens des Prädiktionsfehlersignals umfassen soll („[…] comprises inversing the
coding of the prediction error signal”). Bei einem derartigen Umkehren werden
diejenigen Codierschritte rückgängig gemacht, die die Werte des ursprünglichen
Prädiktionsfehlersignals verändern und zu codierten Blöcken von Frequenz- und
Ortsbereichsdaten mit den codierten quantisierten Koeffizienten und Abtastwerten
führen (vgl. Merkmale 7.2, 7.5.1), so dass das ursprüngliche Prädiktionsfehlersignal
zumindest näherungsweise wiederhergestellt wird.


Die Codierschritte, die dem Merkmal 7.3.1Hi3 entsprechend umgekehrt werden
sollen,    umfassen    somit   die    gemäß      Merkmal    7.2.2Hi3   angewendeten
Codiermechanismen sowie etwaige weitere Codierschritte, die das Codieren des
Prädiktionsfehlersignals anspruchsgemäß beinhalten kann und die die Werte des
ursprünglichen Prädiktionsfehlersignals verändern (vgl. Merkmale 7.2.1Hi3 und
7.2.2Hi3 - „das Codieren […] ein Entscheiden beinhaltet […], und ein Anwenden

                                            - 59 -


[…]”). Der in Merkmal 7.2.1Hi3 genannte Codierschritt („deciding whether to
transform   […]”)   fällt   nicht   unter    die     Umkehrung,   da   eine   von   dem
streitpatentgemäßen Codierer einmal getroffene Entscheidung in keinem Fall von
dem zugehörigen Decodierer rückgängig gemacht werden kann.


3.1.2 Gemäß der Wortbedeutung der englischen Begriffe „the same” und
„subsequent” sollen in Merkmal 7.2.2Hi3 dieselben oder die gleichen nachfolgenden
Codiermechanismen („the same subsequent coding mechanisms”) im Orts- und im
Frequenzbereich angewendet werden.


Patentanspruch 7 nach Hilfsantrag 3 legt sich nicht ausdrücklich auf ein bestimmtes
Referenzereignis (z.B. auf einen bestimmten Codierschritt) fest, anhand dessen
beurteilt werden kann, wann ein Codiermechanismus ein „nachfolgender” oder ein
„späterer” ist und wann nicht. Jedoch ergibt sich sowohl aus dem Anspruchswortlaut
(vgl. Merkmale 7.2.1Hi3 und 7.2.2Hi3) als auch aus Absatz [0006] der
Streitpatentschrift, dass ein solches Referenzereignis die Entscheidung sein kann,
ob das Prädiktionsfehlersignal in den Frequenzbereich transformiert wird. Da diese
Entscheidung insbesondere nach einer Quantisierung, aber vor einem Scan und
einer Entropiecodierung getroffen werden kann (s.o., Abschnitt I.4.1.6 d) bb)), bringt
die Angabe „and applying the same subsequent coding mechanisms” in Merkmal
7.2.2Hi3 allenfalls zum Ausdruck, dass mindestens zwei Teilschritte eines
Codierverfahrens, die nach der Entscheidung in Merkmal 7.2.1Hi3 im Orts- und
Frequenzbereich ausgeführt werden, dieselben oder die gleichen sind. Hingegen
lässt diese Angabe - auch ihrem Wortlaut nach - nicht darauf schließen, dass
sämtliche Schritte desselben Codierverfahrens, welches zum einen im Orts- und
zum anderen im Frequenzbereich ausgeführt wird, dieselben oder die gleichen sein
müssen.


In diesem Zusammenhang ist anzumerken, dass Merkmal 7.2.2Hi3 gerade nicht die
Formulierung in Absatz [0006] der Streitpatentschrift („The subsequent coding
mechanisms may be the same […]”) wörtlich übernimmt, welche einen deutlicheren
Bezug zu allen Codiermechanismen herstellt, die auf die Entscheidung folgen.

                                       - 60 -


3.1.3 Nach alledem ergibt sich aus den neu in Patentanspruch 7 nach Hilfsantrag
3 aufgenommenen Merkmalen 7.2.1Hi3, 7.2.2Hi3 und 7.3.1Hi3 im Hinblick auf die
Anwendung „derselben” Decodiermethode im Frequenz- und im Ortsbereich (vgl.
Merkmal 7.5.1), dass mindestens zwei Codierschritte, die zu den codierten Blöcken
von Frequenz- und Ortsbereichsdaten mit den codierten quantisierten Koeffizienten
und Abtastwerten führen, insbesondere nach der in Merkmal 7.2.1Hi3 getroffenen
Entscheidung umgekehrt werden sollen.


3.2    Die in Patentanspruch 7 nach Hilfsantrag 3 neu aufgenommenen Merkmale
7.2.1Hi3, 7.2.2Hi3 und 7.3.1Hi3 sind der Druckschrift NK10 zu entnehmen. Eine
erfinderische Tätigkeit kann mit ihnen nicht begründet werden.


So ist aus NK10 bekannt, dass die Codiermethoden-Umschalt-Beurteilungseinheit
(„coding method switching judgement unit”) 3 im Codiersystem DV1 insbesondere
anhand der untransformierten Datenblöcke entscheidet, ob die DCT-Codiereinheit
1 oder die NTC-Einheit 2 das Differenzsignal S2 codieren soll (NK10, Spalte 6, Zeile
6 bis 25; Spalte 12, Zeile 51 bis Spalte 13, Zeile 7 - „The coding method switching
judgment unit 3 judges any coding method […], based on a spatial area or […] being
within the intra-block picture information”). Wird das Differenzsignal von der NTC-Einheit 2 codiert, wird es nicht in den Frequenzbereich transformiert, sondern im
Ortsbereich beibehalten.


Somit ist Merkmal 7.2.1Hi3 gezeigt.


Nach der Entscheidung der Codiermethoden-Umschalt-Beurteilungseinheit 3
werden im Codiersystem DV1 im Orts- und im Frequenzbereich mit einer
Quantisierung (Figur 1, Blöcke 12 bzw. 21/22), einem Scan (Figur 3, Schritt K4,
Spalte 7, Zeile 45 bis 49 bzw. Figur 1, Block 23) und einer variablen
Längencodierung (Figur 1, Block 6) sowohl im Orts- als auch im Frequenzbereich
mehrere Codierschritte angewendet, die die Werte des Differenzsignals S2
verändern und zu Blöcken von codierten quantisierten Koeffizienten und
Abtastwerten führen, die an das Decodiersystem DV2 übertragen werden (s.o.,
Abschnitt II.).

                                         - 61 -




Damit liegt auch Merkmal 7.2.2Hi3 vor.


Falls die Bildsignale nach dem Scan geringe Eigenkorrelationen aufweisen, so dass
der Differentiationsblock 24 übergangen werden kann (vgl. Spalte 3, Zeile 17 bis 20;
Spalte 11, Zeile 58 bis 61; Spalte 12, Zeile 12 bis 17 und 34 bis 47), kehrt das in
Figur 2 gezeigte Decodiersystem DV2 die Codierschritte „Quantisierung”, „Scan”
und „Entropiecodierung” um, mit denen das in Figur 1 gezeigten Codiersystem DV1
das Differenzsignal S2 im Frequenz- und im Ortsbereich codiert, und rekonstruiert
mit den Signalen S22 und S23 bis auf etwaige Quantisierungsfehler jeweils das
ursprüngliche Differenzsignal S2.


Somit werden von dem Decodiersystem DV2 drei Teilschritte des Codierverfahrens
rückgängig gemacht, die verschiedene Ziele erreichen und nach der Entscheidung
der Codiermethoden-Schalt-Entscheidungseinheit 3 in beiden Bereichen ausgeführt
werden.


Im Übrigen stellen diese drei Teilschritte sämtliche von dem Decodiersystem DV2
umzukehrenden Teilschritte des Codierverfahrens dar, da der Differentiator 24
übergangen werden kann (vgl. Spalte 12, Zeile 34 bis 50) und der Delay-Block 13
lediglich der Signalverzögerung dient, ohne sich auf die Arbeitsweise des
Decodierers auszuwirken (vgl. Spalte 5, Zeile 61 bis 63).


Dies gilt insbesondere dann, wenn Blöcke verarbeitet werden, deren typischer Wert
Null ist.


Somit liegt auch Merkmal 7.3.1Hi3 vor.


3.3     Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 7 ist der
Gegenstand des Patentanspruchs 7 gemäß Hilfsantrag 3 somit nicht patentfähig.
Mit dem Patentanspruch 7 fällt der gesamte Hilfsantrag 3.

                                             - 62 -


4.       Hilfsantrag   4     hat    keinen    Erfolg,      weil   der    Gegenstand    seines
Patentanspruchs 7 ausgehend von der Druckschrift NK10 nicht auf einer
erfinderischen Tätigkeit beruht.


4.1      Patentanspruch      7     gemäß     Hilfsantrag     4    geht   aus   dem    erteilten
Patentanspruch 7 hervor, indem Merkmal 7.2 durch das Merkmal


7.2Hi2         receiving a coded video signal comprising coded video data that
               include coded blocks of of quantized coefficients in the frequency
               domain data and/or coded blocks of quantized samples in the spatial
               domain data,
               with the coded blocks obtained by coding of a prediction error signal
               established by reducing temporal redundancy by block based motion
               estimation;


und die Merkmale 7.5.1 und 7.5.2 durch die Merkmale


7.5.1Hi4       wherein the same methods are is used for the decoding of the
               quantized coefficients in the frequency domain as for the decoding of
               the quantized samples in the spatial domain,


7.5.2Hi4       wherein the entropy decoding of the quantized coefficients and of the
               quantized samples is carried out according to the CABAC method or
               the CAVLC method.


ersetzt werden.


4.1.1 Merkmal 7.5.1Hi4 bringt zum Ausdruck, dass entweder eine Decodiermethode
im Frequenzbereich (zum Decodieren der Koeffizienten) und eine Decodiermethode
im Ortsbereich (zum Decodieren der Abtastwerte) verwendet wird, wobei diese
beiden Methoden dasselbe Ziel (z.B. ein Decodieren) erreichen, oder dass sowohl
im Orts- als auch im Frequenzbereich mehrere Teilschritte (Teilverfahren) eines
Decodierverfahrens verwendet werden sollen, die in beiden Bereichen der

                                       - 63 -


Verwirklichung jeweils derselben Zielsetzung dienen (s.o., Abschnitt I.4.1.6 c), d),
e)).


a)     Es werden also bereits dann in beiden Bereichen dieselben Methoden
verwendet,   wenn     z.B.   mindestens    zwei    Teilschritte   aus    der     Gruppe
„Entropiedecodierung, inverser Scan, inverse Quantisierung“ jeweils im Orts- und
im Frequenzbereich ausgeführt werden.


Falls die Entropiedecodierung unter diesen Teilschritten ist, bedeutet Merkmal
7.5.2Hi4 insbesondere, dass in beiden Bereichen einheitlich die CABAC-Methode,
oder in beiden Bereichen einheitlich die CAVLC-Methode verwendet wird.


Kommen bei der Decodierung neben der Entropiedecodierung mindestens zwei
weitere Methoden zum Einsatz (dies ist möglich - Merkmal 7.5.2Hi4 lautet ja gerade
nicht „wherein these methods are CABAC or CAVLC”), können die CABAC- und die
CAVLC-Methode gemäß der Merkmalsgruppe 7.5.1Hi4/7.5.2Hi4 in beiden Bereichen
alternativ verwendet werden.


b)     Auch im Hinblick auf die vorgenommenen Änderungen ist Merkmal 7.5.2Hi4
aus    fachmännischer    Sicht   unverändert      so   zu   verstehen,     dass     „die”
anspruchsgemäßen CABAC- und CAVLC-Methoden („the CABAC method”, „the
CAVLC method”) nicht nur die speziellen, in Videocodierstandards verwendeten
speziellen Implementierungen der CABAC- und der CAVLC-Methode sind, sondern
auch beliebige kontextadaptive binäre arithmetische Codierungsmethoden oder
beliebige kontextadaptive variable Längencodierungsmethoden (vgl. z.B. NK7 - die
in der dortigen Figur 5 schematisch gezeigte Entropiecodierungsmethode wird in
der Bildunterschrift als „the CABAC entropy coding scheme” bezeichnet und in den
beiden    darauffolgenden      Absätzen    unabhängig       von    einer       speziellen
Implementierung beschrieben).


4.2    Die Maßnahmen der Merkmale 7.2Hi2, 7.5.1Hi4 und 7.5.2Hi4 können eine
erfinderische Tätigkeit nicht begründen.

                                       - 64 -


4.2.1 So geht Merkmal 7.2Hi2 aus NK10 hervor (s.o., Abschnitt III.2.2.1).


4.2.2 Gemäß der Argumentation in Abschnitt II.1.7 (s.o.) gelangt der Fachmann
ausgehend von NK10 in naheliegender Weise zu einem Verfahren, bei dem im Ortsund im Frequenzbereich eine kontextadaptive inverse Längencodierung („CAVLC”)
vorgenommen wird.


Damit sind die Merkmale 7.5.1Hi4 und 7.5.2Hi4 verwirklicht.


4.2.3 Im Übrigen würde der Fachmann zur Realisierung einer kontextadaptiven
variablen Längencodierung im Orts- und im Frequenzbereich auch auf eine CAVLC-Implementierung aus einem Videocodierstandard zurückgreifen, ohne dabei
erfinderisch tätig zu werden.


Denn gerade die allgemein bekannten und weit entwickelten Vorgehensweisen der
Standards bieten sich für ihn an, eine kontextadaptive variable Längencodierung
bzw. -decodierung im Orts- und im Frequenzbereich auf effiziente Art und Weise zu
realisieren, ohne dass er sich nähere Gedanken über die Implementierung der
Kontextadaptivität machen muss. Zudem ist ihm bewusst, dass die im Ortsbereich
ermittelten Abtastwertfolgen ebenso wie die im Frequenzbereich ermittelten
typischen Koeffizientenfolgen (insbesondere gegen das Ende einer Folge hin) viele
Nullen enthalten (vgl. NK10, Figur 3, Blöcke K3, K4 sowie Figur 17, Block K17) und
daher die standardgemäßen Entropiecodierverfahren auch zur Codierung solcher
Folgen im Ortsbereich sehr gut geeignet sind.


Ferner dürfte der Fachmann bereits deswegen Anlass haben, die im Standard
vorgesehenen       Implementierungen        der     CABAC-       bzw.       CAVLC-Entropie(de)codiermethoden heranzuziehen, weil er die gängigen internationalen
Videocodierstandards kennt und sich vorliegend mit der punktuellen Verbesserung
einer Entropiecodierung befasst, die generell in diesen Standards vorgesehen ist
(vgl. BGH, Urteil vom 22. November 2011, X ZR 58/10, GRUR 2012, 261 - E-Mail
via SMS).

                                           - 65 -


4.3      Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 7 und zum
Patentanspruch 7 nach Hilfsantrag 2 beruht die Lehre des Patentanspruchs 7
gemäß Hilfsantrag 4 somit nicht auf einer erfinderischen Tätigkeit und ist daher nicht
patentfähig. Mit seinem Patentanspruch 7 fällt der gesamte Hilfsantrag 4.




5.       Hilfsantrag   5   hat    keinen    Erfolg,      weil   der    Gegenstand    seines
Patentanspruchs 7 ausgehend von der Druckschrift NK10 nicht auf einer
erfinderischen Tätigkeit beruht.


5.1      Patentanspruch    7     gemäß     Hilfsantrag     5    geht   aus   dem    erteilten
Patentanspruch 7 hervor, indem die Merkmale 7.2, 7.3, 7.5.1 und 7.5.2 durch die
Merkmale


7.2Hi5         receiving a coded video signal comprising coded video data that
               includes (i) coded motion compensation information and (ii) coded
               blocks of quantized coefficients in the frequency domain data and/or
               coded blocks of quantized samples in the spatial domain data, with the
               coded blocks obtained by coding a prediction error signal established
               by reducing temporal redundancy by block based motion estimation;


7.3Hi5         decoding the received coded video data effectively in the frequency
               or the spatial domain depending on whether video data is are coded
               in the frequency or in the spatial domain,


7.5.1Hi5       wherein the same method is used for the entropy decoding of the
               quantized coefficients in the frequency domain as for the entropy
               decoding of the quantized samples in the spatial domain,


7.5.2Hi5       wherein the entropy decoding of the quantized coefficients and of the
               quantized samples is carried out according to CABAC or CAVLC.


ersetzt werden, und ferner unmittelbar nach Merkmal 7.3 die neuen Merkmale

                                     - 66 -




7.3.1Hi5   wherein the decoding the received coded video data comprises:


7.3.2Hi5   inputting the coded video data to entropy-decoding means (201, 202),
           wherein the entropy-decoding means (201, 202) entropy-decode the
           coded blocks and the coded motion compensation information in the
           coded video data, and


7.3.3Hi5   if the prediction error signal represented by a coded block is coded in
           the frequency domain:
           inputting the entropy-decoded block of quantized coefficients to an
           inverse quantization block (203) to output inverse quantized coeffi
           cients in the frequency domain, and
           inputting the inverse quantized coefficients in the frequency domain to
           an inverse transformation block (204) to output inverse transformed
           coefficients in the spatial domain,
           wherein the inverse quantized samples in the spatial domain form the
           decoded prediction error signal (207) of the block, and:


7.3.4Hi5   if the prediction error signal represented by a coded block is coded in
           the spatial domain:
           inputting the entropy-decoded block of quantized samples to an inverse quantization block (206) to output inverse quantized samples in
           the spatial domain,
           wherein the inverse quantized samples in the spatial domain form the
           decoded prediction error signal (207) of the block, and


7.3.5Hi5   inputting the entropy-decoded motion compensation information to a
           motion compensation block (209) to output a motion compensated
           prediction picture, and

                                        - 67 -


7.3.6Hi5      summing the decoded prediction error signal of the blocks with the
              motion compensated prediction picture to provide the decoded video
              signals (210).


eingefügt werden.


5.1.1 Das codierte Videosignal soll nunmehr entsprechend Merkmal 7.2Hi5 auch
codierte Bewegungskompensationsinformationen enthalten, die gemäß den
Merkmalen 7.3.2Hi5 und 7.3.5Hi5 von Entropiedecodiermitteln entrodpiedecodiert
und in einen Bewegungskompensationsblock eingegeben werden, um ein
bewegungskompensiertes Vorhersagebild auszugeben, welches gemäß Merkmal
7.3.6Hi5 zu dem decodierten Prädiktionsfehlersignal hinzuaddiert wird, um die
decodierten            Videosignale         bereitzustellen.          Zu       den
Bewegungskompensationsinformationen, unter die der Fachmann all diejenigen
Informationen subsumiert, die eine Bewegungskompensation betreffen, gehören
insbesondere Bewegungsvektoren (vgl. Streitpatentschrift, Absatz [0024], zweiter
Satz).


5.1.2 Mit den Ausdrücken der Form „inputting […] to a […] block […] to output […]”
in den Merkmalen 7.3.3Hi5 bis 7.3.5Hi5 wird jeweils eine Verarbeitung von Daten
durch entsprechende Verarbeitungsmittel zum Ausdruck gebracht, die mit dem Ziel
ausgeführt wird, dass bestimmte Daten ausgegeben werden. Die Figur 2 der
Streitpatentschrift zeigt ein vereinfachtes Blockdiagramm eines Decodierers, in
dessen schematisch dargestellten Blöcken 203, 204, 206 und 209 der Fachmann
ähnlich    wie   bei    den    Entropiedecodierblöcken    201   und    202   solche
Verarbeitungsmittel erkennt.


Dabei impliziert Merkmal 7.3.4Hi5 nicht, dass die Daten, die der inverse
Quantisierungsblock ausgibt, das decodierte Prädiktionsfehlersignal des codierten
Blocks sein müssen. Denn dieses Merkmal lässt offen, welche Einheit die invers
quantisierten Samples im Ortsbereich ausgibt; es verlangt nur, dass das Eingeben
des entropiedecodierten Blocks von quantisierten Koeffizienten in den inversen
Quantisierungsblock einer Ausgabe von invers quantisierten Samples im

                                      - 68 -


Ortsbereich dient („inputting […] to an inverse quantization block […] to output
inverse quantized samples”).


5.1.3 Die Änderung in Merkmal 7.3Hi5 stellt lediglich eine sprachliche, aber keine
inhaltliche Änderung dar.


5.1.4 Mit Merkmal 7.5.1Hi5 wird nunmehr konkret zum Ausdruck gebracht, dass
„dieselbe Methode” eine Entropiedecodierungsmethode sein soll.




5.2   Auch der Gegenstand des Patentanspruchs 7 gemäß Hilfsantrag 5 liegt für
den Fachmann ausgehend von NK10 nahe.


5.2.1 So generiert der Prädiktor 5 des Codiersystems DV1 Verwaltungsdaten, die
einen Bewegungsvektor repräsentieren und in einem an die VLC-Einheit 6
gesendeten Übermittlungsmanagementsignal S7 enthalten sind (NK10, Spalte 5,
Zeile 1 bis 7 und 19 bis 25 - „the predictor 5 generates management data
representing motion vector […] these data being fed as the transmission
management signal S7 to the variable length coding unit 6 for coding […]”). Daten,
die einen Bewegungsvektor repräsentieren, betreffen vor dem Hintergrund einer
Inter-Frame-Codierung eine Bewegungskompensation. Aus der Angabe „for
coding” in dem oben zitierten Satz ist abzuleiten, dass diese Daten auch codiert
werden (und damit selbstverständlich auch einen Teil des codierten Videosignals
bilden). Dass ein Bewegungsvektor codiert wird, ist zudem Spalte 16, Zeile 59 und
60 i. V. m. Spalte 17, Zeile 11 bis 14 der NK10 ausdrücklich zu entnehmen („The
following information is used for the macro-block coding […] Third coding
information is macro-block motion predictive vector (Motion_vector). This
information is a VLC code representing a motion predictive vector value in case
when the macro-block is of the inter-frame coding mode”).


Damit ergibt sich aus NK10 auch der über die in Merkmal 7.2Hi2 vorgenommenen
Ergänzungen hinausgehende Zusatz in Merkmal 7.2Hi5, gemäß dem das codierte
Videosignal codierte Bewegungskompensationsinformationen umfasst.

                                          - 69 -


5.2.2 Ferner     erhält   der Prädiktor    43 des Decodiersystems         DV2 einen
Bewegungsvektor und rekonstruiert ein Prädiktionssignal 24 (s.o., Abschnitt II.1.3
sowie NK10, Spalte 7, Zeile 1 bis 8; Figur 2 i. V. m. Figur 1). Da ein solcher
Bewegungsvektor zuvor codiert worden ist (s.o., Abschnitt III.5.2.1), folgert der
Fachmann, dass der codierte Bewegungsvektor in Block 32 entropiedecodiert und
zur Erzeugung des Prädiktionssignals S24 verwendet wird.


Dass die im Orts- und Frequenzbereich variabel längencodierten Blöcke
entropiedecodiert werden, ist platt selbstverständlich und geht auch aus NK10
hervor (vgl. Spalte 12, Zeile 24 bis 28 im Fall der Codierung im Ortsbereich; Spalte
4, Zeile 60 bis Spalte 5, Zeile 7 sowie Spalte 6, Zeile 32 bis 43 im Fall der Codierung
im Freuqenzbereich).


Somit zeigt die NK10 auch die Merkmale 7.3Hi5, 7.3.1Hi5, 7.3.2Hi5 und 7.3.5Hi5.


5.2.3 Die Merkmale 7.3.3Hi5 und 7.3.4Hi5 ergeben sich wie folgt aus der
spezifischen Verarbeitung im Orts- und im Frequenzbereichszweig der NK10 (vgl.
dort Figur 2):


a)     Im Frequenzbereichszweig wird ein entropiedecodierter Block quantisierter
Koeffizienten in den inversen Quantisierungsblock 34 eingegeben, woraus inverse
Koeffizienten im Frequenzbereich resultieren, welche ihrerseits in den inversen
Transformationsblock 35 eingegeben werden, woraus inverse Koeffizienten im
Ortsbereich resultieren, die das decodierte, dem entropiedecodierten Block
quantisierter Koeffizienten entsprechende Differenzsignal S22 bilden (Merkmal
7.3.3Hi5).


b)     Im Ortsbereichszweig gibt der inverse Scanconversionsblock 37 einen
entropiedecodierten Block quantisierter Abtastwerte aus (vgl. Spalte 12, Zeile 28 bis
30 i. V. m. Figur 5; s. auch Spalte 3, Zeile 17 bis 20), welche in den inversen
Quantisierungsblock 38 eingegeben werden. Dies dient dem Zweck, im weiteren
Verlauf des Decodierverfahrens invers quantisierte Samples im Ortsbereich

                                            - 70 -


auszugeben, die das decodierte, dem entropiedecodierten Block quantisierter
Abtastwerte entsprechende Differenzsignal S23 bilden (Merkmal 7.3.4Hi5).


aa)    Dies gilt insbesondere dann, wenn der für einen Block typische Wert (z.B.
der Wert „BASE”) gleich Null ist (s.o., Abschnitt III.1.2.3); in diesem Fall gibt bereits
der Block 38 das decodierte Prädiktionsfehlersignal des Blocks aus.


bb)    Da die Blöcke 38 und 39 eine inverse adaptive Quantisierung gemeinsam
realisieren (s.o., Abschnitt III.1.2.2), bilden sie zusammengenommen ein Mittel, das
den entropiedecodierten Block quantisierter Samples mit dem Ziel verarbeitet,
quantisierte   Samples     im    Ortsbereich         auszugeben,   die   das   decodierte
Prädiktionsfehlersignal des Blocks bilden. Auch auf diese Weise wird Merkmal
7.3.4Hi5 verwirklicht.


5.2.4 NK10 ist ferner zu entnehmen, dass das - im Falle der Inter-Frame-Codierung bewegungskompensierte - Prädiktionssignal S24 zu den rekonstruierten
Differenzsignalen S22 und S23 addiert wird, um das decodierte rekonstruierte
Bildsignal bereitzustellen (Spalte 6, Zeile 64 bis 67; Merkmal 7.3.6Hi5).


5.2.5 Für die Merkmale 7.5.1Hi5 und 7.5.2Hi5 gilt weiterhin die Argumentation aus
Abschnitt II.1.7, gemäß der eine kontextabhängige variable Längendecodierung im
Orts- und im Frequenzbereich für den Fachmann naheliegt.


5.2.6 Somit entnimmt der Fachmann die neuen Merkmale von Patentanspruch 7
nach Hilfsantrag 5 der NK10, ohne dabei erfinderisch tätig zu werden.


5.2.7 Im Übrigen ist festzustellen, dass zumindest die Anweisungen der Merkmale
7.2Hi5, 7.3Hi5, 7.3.1Hi5, 7.3.2Hi5,    7.3.5Hi5 und 7.3.6Hi5 nicht über fachübliche
Maßnahmen         hinausgehen,        die      eine      Inter-Frame-Decodierung      mit
Bewegungskompensation ausmachen und die der Fachmann auch in NK1 (vgl.
dort Abschnitt 1, erster Absatz sowie Figur 1 mit Beschreibung) oder NK11 (vgl.
Abschnitt „Video coding layer”, insbesondere vorletzter Absatz) ohne Weiteres
erkennt.

                                         - 71 -




5.3   Mit Blick auf die Ausführungen zum erteilten Patentanspruch 7 und zum
Patentanspruch    7      nach    Hilfsantrag      2   beruht   der   Gegenstand   des
Patentanspruchs 7 gemäß Hilfsantrag 5 somit nicht auf einer erfinderischen
Tätigkeit, so dass das Streitpatent in seiner Fassung nach Hilfsantrag 5 ebenfalls
keinen Bestand hat.




6.    Aus den vorstehend ausgeführten Gründen war das Streitpatent, das somit
in keiner seiner durch die Beklagte verteidigten Fassungen Bestand hatte, im
angegriffenen Umfang für nichtig zu erklären.




                                          IV.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.




                                          V.


                                Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133
Karlsruhe, einzulegen.

                                       - 72 -




Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht       (BGH/BPatGERVV)       auf   elektronischem    Weg    beim
Bundesgerichtshof              einzulegen,             wird             hingewiesen
(www.bundesgerichtshof.de/erv.html).




Hartlieb     Dr. Forkel         Hoffmann          Dr. Himmelmann         Dr. Städele
