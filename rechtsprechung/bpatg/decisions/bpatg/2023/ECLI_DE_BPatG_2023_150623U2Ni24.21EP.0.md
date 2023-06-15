---
ecli: "ECLI:DE:BPatG:2023:150623U2Ni24.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 24/21"
decided: "2023-06-15"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=16&nr=43741&anz=529&pos=244&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-06-15_2_Ni_24_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 24/21 vom 2023-06-15

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      Verkündet am
                                                      15. Juni 2023
2 Ni 24/21 (EP)                                             …

(Aktenzeichen)


                     In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:150623U2Ni24.21EP.0

                                        -2-



               betreffend das europäische Patent EP 2 661 696
                              (DE 60 2011 066 777)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 15. Juni 2023 unter Mitwirkung der Vorsitzenden
Richterin Hartlieb sowie der Richter Dipl.-Phys. Univ. Dr. Forkel, Dr. Himmelmann,
Dipl.-Phys. Univ. Dr. Städele und Dr.-Ing. Harth


für Recht erkannt:


      I.        Das europäische Patent EP 2 661 696 wird mit Wirkung für das
                Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


      II.       Die Kosten des Rechtsstreits trägt die Beklagte.


      III.      Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des zu
                vollstreckenden Betrages vorläufig vollstreckbar.




                                  Tatbestand




Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in englischer Verfahrenssprache erteilten europäischen Patents EP 2 661 696
(deutsches Aktenzeichen DE 60 2011 066 777) (Streitpatent), das am
22. Dezember 2011 unter Inanspruchnahme der Prioritäten US 201161430110 P
vom 5. Januar 2011, US 201113221794 und US 201113221682 jeweils vom
30. August 2011, angemeldet worden ist und das die Bezeichnung „Adaptive Bitrate
Streaming Of Media Stored In Matroska Container Files Using Hypertext Transfer
Protocol“    (Adaptives   Bitraten-Streaming   von   in   Matroska-Containerdateien
gespeicherten Medien mit http) trägt.

                                            -3-



Der Hinweis auf die Erteilung des Streitpatents wurde am 6. Mai 2020 veröffentlicht.
Das Streitpatent geht zurück auf eine beim Europäischen Patentamt eingereichte
Anmeldung mit der Anmeldenummer 11855237.1, die aus der internationalen
Anmeldung PCT/US2011/066927, publiziert als WO 2012/094171 A1, hervorgeht.


Das Streitpatent betrifft das sogenannte Streaming von kodierten Medien (encoded
media) mit Adaption der Bitrate (Streitpatentschrift, Abs. [0001]).


Das in vollem Umfang angegriffene Streitpatent umfasst 13 Patentansprüche, den
unabhängigen Anspruch 1 sowie die abhängigen Ansprüche 2 bis 13.


Der erteilte Patentanspruch 1 lautet gemäß EP 2 661 696 B1 (mit an die Anlage
NK 5 der Klägerin angelehnter Merkmalsgliederung):


 a          A playback device (20) configured Wiedergabegerät (20) eingerichtet
            to      perform      adaptive     bitrate zum   Ausführen     von    Bitratenstreaming, the playback device adaptivem Streaming, wobei das
            comprising a processor configured, Wiedergabegerät einen Prozessor
            via a client application, to request a umfasst, der durch eine Klienttop level index file and container Anwendung dazu eingerichtet ist,
            files via a network;                     eine     Hauptindex-Datei        und
                                                     Container-Dateien       über     ein
                                                     Netzwerk anzufordern,
 c          wherein        the   client   application wobei die Klient-Anwendung ferner
            further configures the processor to:     den Prozessor einrichtet zum:
 c1         commence playback by retrieving Beginn             einer    Wiedergabe    mit
            the top level index file                 Abrufen der Hauptindex-Datei,
 b          that identifies a plurality of container die eine Vielzahl von Containerfiles   that    contain the     streams Dateien bezeichnet, die die Streams,
            available to the playback device for die für das Wiedergabegerät zur
                                                     Verwendung bei Bitraten-adaptivem

                                            -4-



     use in adaptive bitrate streaming, Streaming verfügbar sind, enthalten,
     where                                            worin
b1   the available streams include a die                      verfügbaren       Streams      eine
     plurality     of      alternative          video Vielzahl alternativer Video-Streams
     streams, each of the alternative beinhalten, jeder der alternativen
     video streams (32) is the same Video-Streams                          (32)   der     gleiche
     source video content encoded at a Quell-Video-Inhalt kodiert mit einer
     different bitrate and is stored in a unterschiedlichen Bitrate ist und in
     separate container file as a plurality einer eigenen Container-Datei als
     of portions of video,                            eine    Vielzahl     von Stücken       von
                                                      Videomaterial gespeichert ist,
b2   each portion of video is encoded as wobei jedes Stück Videomaterial als
     at least one closed group of zumindest                              eine     geschlossene
     pictures          starting          with     an Gruppe von Bildern beginnend mit
     Instantaneous         Decoder          Refresh einem IDR-Rahmen (Instantaneous
     (IDR) frame, and                                 Decoding Refresh) kodiert ist, und
b3   each        container        file     includes jede Container-Datei Informationen
     information           concerning             the betreffend die Kodierung des in der
     encoding of the video contained Container-Datei                               enthaltenen
     within the container file and an Videomaterials und einen Index zu
     index to the encoded media within den                    kodierten     Medien      in   der
     the container file and the top level Container-Datei beinhaltet, und die
     index file indicates the portions of Hauptindex-Datei die Bereiche jeder
     each container file containing this Container-Datei angibt, die diese
     information;                                     Informationen enthalten,
c    [wherein      the     client        application [wobei die Klient-Anwendung ferner
     further configures the processor to:] den Prozessor einrichtet zum:]
c2   select      one     or   more         streams Auswählen eines oder mehrerer
     including one of the plurality of Streams, worin einer der Vielzahl
     alternative video streams to utilize alternativer Video-Streams enthalten
     in the playback of media based ist, zur Nutzung bei der Wiedergabe

                                            -5-



     upon the retrieved at least a portion von Medien aufgrund zumindest des
     of the top level index file;                     Teils der Hauptindex-Datei, der/die
                                                      abgerufen wurde,
c3   using the top level index file to Verwenden                        der    Hauptindex-Datei
     request        the      portions       of    the zum Anfordern der Bereiche der
     container       file    that include         the Container-Datei,                die           die
     information            concerning            the Informationen            betreffend           die
     encoding of the video contained Kodierung des in der Containerwithin the container file and the Datei                   enthaltenen          Videomaterials
     index to the encoded media within und den Index zu den kodierten
     the container file                               Medien       in    der        Container-Datei
                                                      enthalten,
c4   configure       a      video    decoder       to Konfigurieren                               eines
     playback the encoded video using Videodekodierers zur Wiedergabe
     the           retrieved             information des kodierten Videomaterials mithilfe
     concerning the encoding of the der                      abgerufenen             Informationen
     video;                                           betreffend        die     Kodierung          des
                                                      Videomaterials,
c5   retrieve encoded media from the Abrufen kodierter Medien von der
     container       file    of     the    selected Container-Datei des ausgewählten
     alternative video stream using the alternativen Video-Streams mithilfe
     requested index information to the der                      angeforderten                   Indexencoded media within the container Informationen                     zu        den     kodierten
     file;                                            Medien in der Container-Datei,
c6   playback the retrieved portions of Wiedergeben                           der     abgerufenen
     video from the selected alternative Stücke                 Videomaterial             aus     dem
     video stream using the decoder; ausgewählten                         alternativen           Videoand                                              Stream mittels des Dekodierers, und,
c7   when      a     change         in    streaming wenn       eine       Änderung          in     den
     conditions is detected, select a new Streaming-Bedingungen                             detektiert
     alternative video stream that is wird,                    Auswählen            eines        neuen

                                        -6-



           more appropriate for the streaming alternativen Video-Streams, der für
           conditions   than   the    previously die Streaming-Bedingungen besser
           selected alternative video stream.    geeignet    ist    als   der    vorher
                                                 ausgewählte       alternative   Video-Stream.


Die Klägerin stützt ihre Klage auf die Nichtigkeitsgründe der mangelnden
Patentfähigkeit mit Blick auf fehlende Neuheit und fehlende erfinderische Tätigkeit
sowie der unzulässigen Erweiterung.


Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:


  D1         3GPP TS 26.234 V9.5.0 (2010-12), 3rd Generation Partnership
             Project; Technical Specification Group Services and System
             Aspects; Transparent end-to-end Packet-switched Streaming
             Service (PSS); Protocols and codecs (Release 9);
  D2         Beitrag zum Treffen der Arbeitsgruppe ISO/IEC JTC1/SC29/WG11
             MPEG/N11578 in Guangzhou, China, Oktober 2010, im Rahmen
             der Standardisierung des MPEG-DASH Standards. Titel: „Text of
             ISO/IEC 23001-6: Dynamic adaptive streaming over HTTP
             (DASH)“;
  D3         WO 2011 / 059 274 A2, angemeldet am 12. November 2010,
             veröffentlicht am 19. Mai 2011;
  NK1        Verletzungsklageschrift der Beklagten an das LG Mannheim vom
             30. September 2020;
  NK2        Streitpatentschrift EP 2 661 696 B1;
  NK3        DPMA, Registerauszug zum Aktenzeichen 60 2011 066 777.7,
             Stand am 19. Mai 2021;
  NK4        Offenlegungsschrift WO 2012 / 094 171 A1 zum Streitpatent;
  NK5        Merkmalsgliederung Anspruch 1;
  NK6        Hauptantrag EPA-Verfahren vom 5. November 2019;

                                    -7-



NK7    Protokoll      der   mündlichen    Verhandlung     am      EPA    vom
       19. Dezember 2019;
NK8    Prioritätsanmeldung US 2011 61/430,110 P vom 5. Januar 2011;
NK9    Prioritätsanmeldung US 2011 13/221,794 vom 30. August 2011;
NK10   Prioritätsanmeldung US 2011 13/221,682 vom 30. August 2011;
NK11   USPTO „Patent Assignment“ zu NK9 (application number
       13 221 794);
NK12   USPTO „Patent Assignment“ zu NK10 (application number
       13 221 682);
NK13   3GPP TS 26.244 V9.3.0 (2010-09), 3rd Generation Partnership
       Project; Technical Specification Group Services and System
       Aspects; Transparent end-to-end packet-switched streaming
       service (PSS); 3GPP file format (3GP) (Release 9);
NK14   Engineering Guideline H.264 / AVC Coding and Multiplexing vom
       14. Mai 2009;
NK15   ISO/IEC 14496-14 “Part 14: MP4 file format” von 2003;
NK16   Urteil   des    Landgerichts    Mannheim     vom    11.    März   2022
       (Aktenzeichen: 7 O 88/21; Anm. des Senats: betrifft nicht das
       Streitpatent EP 2 661 696, sondern das Patent EP 3 467 666);
NK17   Berufungsschriftsatz der Klägerin vom 14. März 2022 an das
       Oberlandesgericht Karlsruhe (betrifft das Streitpatent);
NK18   Wikipedia-Artikel „Parser“, zuletzt bearbeitet am 12. Juli 2010,
       13:01 Uhr;
NK19   Schaubild      zu    Media   Presentation   Description   (MPD)    und
       Representations nach D 1;
NK20   Firmenschrift der Microsoft Corporation, BOCHAROV, J. A., et al.:
       „Portable      encoding of audio-video      objects, The Protected
       Interoperable File Format (PIFF)“. Revised 2010-03-09;
NK21   Mitteilung des EPA-Prüfers vom 28. Juni 2022;
NK22   Protokoll      der   mündlichen    Verhandlung     am      EPA    vom
       9. September 2022;
NK23   EPA-Mitteilung vom 16. September 2022.

                                       -8-



Die Klägerin stellt den Antrag,
             das europäische Patent EP 2 661 696 mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
             nichtig zu erklären.


Die Beklagte stellt den Antrag,
             die Klage abzuweisen
             hilfsweise
             das europäische Patent EP 2 661 696 unter Klageabweisung im
             Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik
             Deutschland insoweit für nichtig zu erklären, als es über die Fassung
             eines der Hilfsanträge I vom 15. Februar 2022, II bis V jeweils vom
             27. März 2023 und VI bis VIII jeweils vom 2. Mai 2023 – in dieser
             Reihenfolge – hinausgeht.


Die Beklagte erklärt in der mündlichen Verhandlung vom 15. Juni 2023, dass sie die
Patentansprüche gemäß Hauptantrag und Hilfsanträgen als jeweils geschlossene
Anspruchssätze ansieht, die jeweils insgesamt beansprucht werden.


Die Beklagte, die das Streitpatent mit einem Hauptantrag und hilfsweise beschränkt
mit 8 Hilfsanträgen verteidigt, tritt der Argumentation der Klägerin in allen
wesentlichen Punkten entgegen und erachtet den Gegenstand des Streitpatents für
patentfähig. Hierbei komme es maßgeblich auf das im Wege der Auslegung zu
ermittelnde zutreffende Verständnis der Lehre des Patentanspruchs 1 an. Auf dieser
Grundlage sei der Gegenstand des Streitpatents neu gegenüber der Lehre jeder
der drei Druckschriften D1 bis D3. Ferner sei der Gegenstand des erteilten
Patentanspruchs 1 gegenüber der Ursprungsanmeldung NK 4 nicht unzulässig
erweitert. Die beanspruchte Lehre sei jedenfalls in einer der Fassungen der
Hilfsanträge patentfähig.

                                        -9-



Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:


     ES-NK1      Wikipedia-Artikel „Client“, zuletzt am 12. Oktober 2010 um
                 10:11 Uhr geändert;
     ES-NK2      Wikipedia-Artikel „Server“, zuletzt am 21. November 2010
                 um 23:13 Uhr geändert;
     ES-NK3      Wikipedia-Artikel „Server (Software)“, zuletzt am 26. Februar
                 2010 um 19:14 Uhr geändert;
     ES-NK4      Wikipedia-Artikel     „Client-Server-Modell“,   zuletzt   am
                 16. Oktober 2010 um 10:00 Uhr geändert;
     ES-NK5      Internet-Beitrag „Rusty Techie“, MPEG2TS Stream -
                 Transport Stream, 17. Dezember 2014;
     ES-NK6      Webseite Cambridge Dictionary zum Begriff „retrieval“;
     ES-NK7      Internetartikel – Trapani, G.: „How to set up a personal home
                 web server“, September 2006;
     ES-NK8      Internetartikel (Anm. des Senats: Autor unbekannt) „Turn
                 your iPhone into a Web server“, 9. Februar 2009.


Hilfsantrag I vom 15. Februar 2022 lautet:

- 10 -

- 11 -

                                       - 12 -



Hilfsantrag II vom 27. März 2023 lautet:

- 13 -

                                       - 14 -




Hilfsantrag III vom 27. März 2023 lautet:

- 15 -

                                      - 16 -




Hilfsantrag IV vom 27. März 2023 lautet:

- 17 -

- 18 -

                                      - 19 -



Hilfsantrag V vom 27. März 2023 lautet:

- 20 -

- 21 -

                                         - 22 -



Hilfsantrag VI vom 2. Mai 2023 lautet:

- 23 -

                                          - 24 -




Hilfsantrag VII vom 2. Mai 2023 lautet:

- 25 -

                                       - 26 -




Hilfsantrag VIII vom 2. Mai 2023 lautet:

- 27 -

                                         - 28 -




Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                           Entscheidungsgründe




Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG i. V. m. Art. 138 Abs. 1 lit. a) EPÜ, Art. 52,
54 und 56 EPÜ sowie der Nichtigkeitsgrund der unzulässigen Erweiterung nach
Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜG i. V. m.     Art. 138 Abs. 1 lit. c) EPÜ und
Art. 123 Abs. 2 EPÜ geltend gemacht werden, ist zulässig.

                                             - 29 -



Die Klage ist auch begründet. Denn das Streitpatent hat weder in seiner erteilten
Fassung noch in der Fassung der Hilfsanträge I bis VIII Bestand, weil ihm der
Nichtigkeitsgrund der mangelnden Patentfähigkeit entgegensteht.



                                               I.


1. Das Streitpatent betrifft das Streaming von kodierten Medien (encoded media)
mit Adaption der Bitrate (Streitpatentschrift Abs. [0001]). Der Begriff Streaming
beschreibe die Wiedergabe von Medien durch ein Wiedergabegerät, wobei die
Medien auf einem Server gespeichert seien und kontinuierlich über ein Netzwerk zu
dem Wiedergabegerät gesandt würden (Streitpatentschrift Abs. [0002]). Adaptives
Bitraten-Streaming beinhalte zudem, die vorliegenden Bedingungen (z. B.
Bandbreite) in Echtzeit (real time) zu detektieren und die Qualität der übertragenen
Medien entsprechend anzupassen. Dazu seien die Medien üblicherweise mit
mehreren Bitraten kodiert, zwischen denen das Wiedergabegerät umschalte
(Streitpatentschrift Abs. [0002]).


Auf einem Medienserver (media server) sei üblicherweise eine Hauptindex-Datei (top
level index file) gespeichert, die auf mehrere alternative Datenströme (streams)
hindeute (pointing), welche die eigentlichen Video- und Audio-Daten enthielten.
Jeder Datenstrom sei für gewöhnlich in einer oder mehreren Container-Dateien
(container   files)      abgelegt    (Streitpatentschrift   Abs. [0004]).   Unterschiedliche
Lösungen     für      adaptives     Bitraten-Streaming      bedienten   sich   verschiedener
Hauptindex-Dateien und Medien-Container (Streitpatentschrift Abs. [0004], [0005]).


Aus dem Stand der Technik sei für die Wiedergabe einer Videodatei bekannt, bei
sich ändernden Netzwerkbedingungen von einer Version mit hoher Bitrate auf eine
Version mit niedriger Bitrate umzuschalten (Streitpatentschrift Abs. [0006]). Ferner
sei   bekannt,     für    das     Herunterladen       dynamisch   aus   Mediendateien    mit
unterschiedlicher Qualität auszuwählen, sowie eine auf HTTP beruhende adaptive
Streaming-Technologie (Streitpatentschrift Abs. [0007] bzw. [0008]).

                                       - 30 -




2.     Eine Aufgabe wird im Streitpatent nicht ausdrücklich genannt. Jedoch ist vor
dem Hintergrund der oben genannten Absätze der Streitpatentschrift die Aufgabe
darin zu sehen, ein Wiedergabegerät anzugeben, das ein Streaming mit
verbessertem adaptiven Verhalten verwirklicht.


Diese Aufgabe wird erfindungsgemäß durch ein Wiedergabegerät („playback
device“ in der maßgeblichen englischen Fassung) mit den Merkmalen des
Patentanspruchs 1 nach Hauptantrag gelöst, der sich entsprechend dem Vorschlag
der Klägerin gemäß Anlage NK5, wie vorstehend angegeben, gliedert.




3.     Als Fachmann, der mit der Lösung dieser Aufgabe betraut wird, ist ein
Ingenieur der Fachrichtung Informationstechnik anzusehen, der mehrjährige
Berufserfahrung und Fachkenntnisse auf dem Gebiet des Streamings besitzt und
mit den einschlägigen Standarddokumenten vertraut ist.




4.     Dieser Fachmann legt den Merkmalen des von der Nichtigkeitsklage
angegriffenen Patentanspruchs 1 folgendes Verständnis zugrunde:


4.1    Ein anspruchsgemäßes Wiedergabegerät zum Bitraten-adaptiven Streaming
weist als Vorrichtungsmerkmal einen Prozessor auf. Dieser ist durch eine Klient-Anwendung dazu eingerichtet, eine Hauptindex-Datei und Container-Dateien über
ein Netzwerk anzufordern (Merkmal a; vgl. Streitpatentschrift Absatz [0022], Fig. 1).


Die übrigen Merkmale des Patentanspruchs 1 bestimmen die Funktionsweise des
Wiedergabegeräts, indem die Klient-Anwendung den Prozessor ferner dazu
einrichtet   (Merkmal c),    das     Bitraten-adaptive    Streaming     nach     den
Verfahrensschritten gemäß den Merkmalen c1 bis c7 durchzuführen. Dabei
beziehen sich die Verfahrensschritte auf die durch die Merkmalsgruppe b, b1, b2

                                           - 31 -



und b3 festgelegte Datenstruktur, gemäß der die Medien-Daten sowie zugehörige
Daten für deren Handhabung, die dem Fachmann als Metadaten geläufig sind,
abgelegt und aufgefunden werden sollen. Im Anspruchswortlaut werden Medienund Metadaten wie nachfolgend erläutert in mehreren Begriffen angesprochen.


4.2    Die Hauptindex-Datei bezeichnet (identifies) eine Vielzahl von Container-Dateien (Merkmal b). Nach der Beschreibung kann die Hauptindex-Datei deren
Inhalt beschreiben und Verweise auf die Container-Dateien beinhalten (vgl.
Absatz [0023] bzw. [0025]). Demgegenüber lässt das Merkmal b offen, in welcher
Weise die Container-Dateien „bezeichnet“ werden sollen.


Die für das Bitraten-adaptive Streaming in den Container-Dateien enthaltenen
Streams umfassen für den Fachmann die wahlweise wiederzugebenden Medien-Daten (vgl. Streitpatentschrift Fig. 2).


4.3    Die Merkmale b1, b2 und b3 bestimmen lediglich ein Video-Streaming näher,
während andere Arten von Streams (Audio, Untertitel; Absatz [0015]) im Anspruch
nicht genannt sind.


Indem die verfügbaren Streams eine Vielzahl alternativer Video-Streams mit
gleichem Quell-Video-Inhalt jedoch unterschiedlicher Bitrate beinhalten sollen
(Merkmal b1), ist aus fachmännischer Sicht ein adaptives Streaming möglich. Dabei
soll gemäß Merkmal b1 jeder der alternativen Video-Streams in einer eigenen
Container-Datei gespeichert sein, wobei der Fachmann unter der weiterhin
genannten Vielzahl von Stücken von Videomaterial die bei Videos üblichen
Einzelbilder, Frames oder dergleichen versteht.


4.4    In der Anweisung des Merkmals b2, jedes Stück Videomaterial als zumindest
eine geschlossene Gruppe von Bildern beginnend mit einem IDR-Rahmen
(Instantaneous Decoding Refresh) zu kodieren, erschließt der Fachmann die
Bedeutung des in der Streitpatentschrift nicht erläuterten Begriffs IDR-Rahmen
durch sein Fachwissen. Ein IDR-Rahmen gestattet es beispielsweise bei

                                      - 32 -



H.264/MPEG-4-kodierten Videos, nachfolgende Bilder zu dekodieren, ohne dabei
auf Bilder zurückzugreifen, die vor dem IDR-Rahmen empfangen wurden. Im
Einklang damit entnimmt der Fachmann Absatz [0016] der Beschreibung der
Streitpatentschrift, dass eine in einer Container-Datei gespeicherte geschlossene
Gruppe von Bildern wiedergegeben werden kann, ohne dabei auf Videoinhalte in
einem anderen Bereich derselben Container-Datei Bezug zu nehmen.


4.5    Das Merkmal b3 legt nach seinem ersten Teil weitere Inhalte der Container-Dateien fest und bestimmt nach seinem zweiten Teil die Hauptindex-Datei näher.


4.5.1 Hierbei kann die Anweisung des ersten Teils des Merkmals b3 auf zwei
unterschiedliche Weisen gelesen werden. Denn aus dem Wortlaut der englischen
Fassung „each container file includes information concerning the encoding of the
video contained within the container file and an index to the encoded media within
the container file“ geht nicht eindeutig hervor, ob sich die Angabe „information
concerning“ ausschließlich auf das nachfolgende Wort „encoding“ oder zusätzlich
auch auf den im weiteren Verlauf genannten „index“ beziehen soll. Bei der
deutschen Übersetzung verhält es sich genauso: „Informationen betreffend die
Kodierung … und einen Index zu …“.


Deshalb lässt sich der erste Teil des Merkmals b3 dem breitesten Wortsinn nach
dahin verstehen, dass jede Container-Datei Informationen betreffend die Kodierung
des in der Container-Datei enthaltenen Videomaterials und Informationen
betreffend einen Index zu den kodierten Medien in der Container-Datei beinhalten
soll. Bei diesem Verständnis erfasst das Merkmal b3 zwar gleichermaßen den Fall,
dass eine Container-Datei den vollständigen Index enthält; das Merkmal ist jedoch
bereits dann erfüllt, wenn in der Container-Datei lediglich auf den Index bezogene
Informationen gespeichert sind, wie beispielsweise ein Header der Container-Datei,
welcher auf den Index verweist. Ein Ausführungsbeispiel mit einem solchen Header
entnimmt der Fachmann der Figur 8 i. V. m. Absatz [0065] der Streitpatentschrift.
Nach    demselben    Ausführungsbeispiel       gibt   (Merkmal b3:   „indicates”)   die
Hauptindex-Datei mittels einer URI den Header-Bereich der Container-Datei an,

                                       - 33 -



welcher den Ort des Indexes innerhalb der Container-Datei als eine den Index
betreffende Information enthält. Damit erfüllt die Hauptindex-Datei die im zweiten
Teil des Merkmals b3 festgelegte Funktion.


Demzufolge lässt der Wortlaut des Merkmals b3 ein allgemeines Verständnis des
Anspruchsgegenstands zu, welches das Ausführungsbeispiel gemäß Figur 8 mit
umfasst und daher hier für sachgerecht gehalten wird (vgl. BGH, Urteil vom
2. Juni 2015, X ZR 103/13, GRUR 2015, 972 – Kreuzgestänge, Leitsatz 2: „Werden
in   der   Beschreibung   eines    Patents      mehrere   Ausführungsbeispiele   als
erfindungsgemäß vorgestellt, sind die im Patentanspruch verwendeten Begriffe im
Zweifel so zu verstehen, dass sämtliche Beispiele zu ihrer Ausfüllung herangezogen
werden können“).


Doch selbst wenn man dem Einwand der Beklagten folgen wollte, dass der Index
zu den kodierten Medien nach Maßgabe des Merkmals b3 in der jeweiligen
Container-Datei enthalten und unmittelbar aus derselben abrufbar sein müsse, d. h.
ohne den Umweg über eine vorherige Anfrage eines Headers der Container-Datei
zu erfordern, käme es darauf im Ergebnis nicht an. Denn für den Vergleich mit dem
Stand der Technik ist die Ausführungsform mit einem Header innerhalb der
Container-Datei nicht entscheidungserheblich, wie nachstehend ausgeführt.


4.5.2 Weiterhin lässt der Wortlaut des Merkmals b3 offen, ob die Informationen zu
Kodierung und Index in einem zusammenhängenden Bereich oder in mehreren
voneinander getrennten Bereichen der Container-Datei gespeichert sind. Indem das
Merkmal b3 auf das „in der Container-Datei enthaltene Videomaterial“ sowie einen
„Index zu den kodierten Medien“ Bezug nimmt, ist ferner nicht festgelegt, in welcher
konkreten Datenstruktur das Videomaterial bzw. die Medien in der Container-Datei
gespeichert sind. Des Weiteren besagt ein „Index zu den kodierten Medien“ nach
Maßgabe des Merkmals b3 lediglich, dass ein solcher Index es ermöglicht, die
kodierten Medien aufzufinden. Dagegen bleibt die Gliederung der Index-Daten
ebenso offen wie die Art und Weise, in der diese Daten in der Container-Datei
gespeichert sind.

                                        - 34 -




Die Beklagte vertritt die Auffassung, der Index gemäß dem Merkmal b3 nehme
aufgrund   der   Datenstruktur    in   der   Container-Datei   gemäß   Figur 6   der
Streitpatentschrift einen zusammenhängenden Bereich in der Container-Datei ein
und könne auf diese Weise mithilfe der entsprechenden Bereichsinformation in der
Hauptindex-Datei in seiner Gesamtheit vom Wiedergabegerät abgerufen werden.


Diese Auslegung vermag nicht zu überzeugen. Denn sie stützt sich auf ein
einzelnes anhand von Figur 6 erläutertes Ausführungsbeispiel, gemäß dem
innerhalb von Matroska-Container-Dateien Stücke von Videomaterial in Cluster-Elementen und ein Index in Cues-Elementen gespeichert sind. Matroska-Container-Dateien sind in Absatz [0023] der Beschreibung der Streitpatentschrift jedoch
ausdrücklich als eine von vielen möglichen Formen von Container-Dateien genannt.
Auf diesen Umstand weist die Beklagte im Zusammenhang mit Fragen der
Zulässigkeit von Änderungen selbst hin. Aus den im Merkmal b3 lediglich in
allgemeiner Form angegebenen Begriffen „Videomaterial“ und „kodierte Medien“ ist
nicht ersichtlich, dass die zugehörigen Daten irgendwelchen Formatvorgaben,
insbesondere für Matroska-Container-Dateien, genügen müssen. Auch durch die
Bezugnahme auf „Stücke von Videomaterial“ in den Merkmalen b1 und b2 lässt sich
eine Einschränkung auf bestimmte Datenformate nicht begründen.


4.5.3 In seinem zweiten Teil bestimmt das Merkmal b3, dass die Hauptindex-Datei
die Bereiche (portions) jeder Container-Datei „angibt“ (indicates), die Informationen
zu Kodierung und Index enthalten. In Figur 2 der Streitpatentschrift ist durch Pfeile
ohne technische Details dargestellt, wie die Hauptindex-Datei auf Container-Dateien „hindeutet“ (indicates). Konkretere Angaben hierzu gibt die Beschreibung
im Absatz [0067] der Streitpatentschrift. Dieser vermittelt dem Fachmann, dass in
der Hauptindex-Datei enthaltene URIs (Uniform Resource Identifiers) geeignet
strukturiert sein können, um byte-weise definierte Bereiche anzufordern, die
zumindest Teile des Indexes einer Container-Datei enthalten. Wie die URIs im
Einzelnen zu strukturieren sind und auf welche Weise die byte-weisen Anfragen zu
formulieren sind, lässt das Streitpatent offen.

                                      - 35 -




Das Merkmal b3 ist indessen in seinem zweiten Teil nicht auf eine solche
Ausführung beschränkt. Vielmehr versteht der Fachmann unter der Anweisung „the
top level index file indicates the portions of each container file containing this
information“ die allgemeine Lehre, dass die Hauptindex-Datei in einer Weise auf die
Container-Datei hindeuten soll (indicates), die es ermöglicht, Bereiche der
Container-Datei mit Informationen zu Kodierung und Index anzufordern. Durch
welche Mittel das Hindeuten anspruchsgemäß zu erfolgen hat, geht aus Merkmal b3
nicht hervor.


Die Beklagte vertritt den Standpunkt, dass die Hauptindex-Datei den Ort der Index-Information in der Container-Datei hinreichend genau und direkt angeben müsse,
also insbesondere ohne den Umweg über einen Header wie in Figur 8 der
Streitpatentschrift. Sie weist hierzu unter anderem auf die Datenstrukturen Cues
und CuePoint sowie SeekHead und Tracks hin. Zudem müsse die „Verzeigerung“
von der Hauptindex-Datei hin zur Container-Datei eine genaue Zuordnung geben,
weshalb das Merkmal b3 technisch eng zu verstehen sei. Auch sei die Leistung der
Erfindung darin zu sehen, dass vor allem das Merkmal b3 lehre, in der Hauptindex-Datei nur einen (einzelnen) Verweis auf den Index in der Container-Datei
vorzusehen.


Einer solch verengenden Auslegung des Merkmals b3 kann nicht gefolgt werden.
Denn die vorgenannten Datenstrukturen sind nicht Bestandteile einer Hauptindex-Datei, sondern innerhalb einer Container-Datei angeordnet (vgl. Abs. [0045], [0055]
bzw. [0065] und [0066] der Beschreibung der Streitpatentschrift). Hierbei dienen
Cues, CuePoint und SeekHead einem Indexieren innerhalb einer Container-Datei,
nicht aber einem Hindeuten von einer Hauptindex-Datei zu einer Container-Datei.
Deshalb lassen die genannten Datenstrukturen weder einen Rückschluss darauf zu,
wie präzise die Hauptindex-Datei den Ort der Index-Information in der Container-Datei anzugeben hat, noch darauf, dass dies direkt erfolgen muss. Im Übrigen
handelt es sich bei den Datenstrukturen SeekHead und Tracks um Header-Elemente einer Container-Datei des im Streitpatent anhand von Figur 8 erläuterten

                                      - 36 -



Ausführungsbeispiels, welches die Beklagte ohnehin nicht unter den Wortlaut des
Merkmals b3 subsumiert wissen will.


Um ihr technisch enges Verständnis des Merkmals b3 zu untermauern, vermag die
Beklagte folglich auf keine Stelle in der Streitpatentschrift hinzuweisen, die eine
derartige Auslegung stützen könnte. Eine solche Stelle ist auch nach Überzeugung
des Senats nicht auffindbar. Es ist insbesondere kein Umstand ersichtlich, weshalb
der allgemein gehaltene Wortlaut des Merkmals b3 lediglich einen einzelnen
Verweis aus der Hauptindex-Datei in eine jeweilige Container-Datei erfassen soll.


4.6    Das Bitraten-adaptive Streaming soll nach den Verfahrensschritten gemäß
den Merkmalen c1 bis c7 des Patentanspruchs 1 erfolgen.


Die Wiedergabe beginnt mit einem Abrufen der Hauptindex-Datei (Merkmal c1).
Dies kann gemäß Figur 8 der Streitpatentschrift durch Austausch zweier
Nachrichten „Top Level Index Request“ bzw. „… Response“ geschehen.


Aufgrund zumindest des Teils der Hauptindex-Datei, der/die abgerufen wurde, ist
ein Stream oder sind mehrere Streams zur Nutzung bei der Wiedergabe
auszuwählen, worin einer der Vielzahl alternativer Video-Streams enthalten ist
(Merkmal c2). Dabei bleibt offen, ob neben einem Video-Stream in einer Container-Datei auch Streams für beispielsweise Audio und Untertitel enthalten sind (vgl.
Streitpatentschrift Figur 4d).


Die Hauptindex-Datei wird zum Anfordern derjenigen Bereiche der Container-Datei
verwendet, die die Informationen betreffend die Kodierung des in der Container-Datei enthaltenen Videomaterials und den Index zu den kodierten Medien in der
Container-Datei enthalten (Merkmal c3). Der Wortlaut des Merkmals c3 ist analog
zum Merkmal b3 gehalten und folglich in dem zuvor beschriebenen Sinne
auszulegen (vgl. Abschnitt I.4.5). Zum Anfordern der Informationen betreffend
Kodierung und Index zeigt die Streitpatentschrift in Figur 8 i. V. m. Absatz [0065]
und [0066] die Nachrichten MKV Headers Request sowie MKV Index Request.

                                        - 37 -




Mithilfe   der   abgerufenen     Informationen    betreffend   die   Kodierung   des
Videomaterials    wird   ein   Videodekodierer    zur Wiedergabe des       kodierten
Videomaterials konfiguriert, also beispielsweise eine Bildfrequenz und Auflösung
eingestellt (vgl. Streitpatentschrift Absatz [0066] – Merkmal c4).


Die angeforderten Index-Informationen zu den kodierten Medien in der Container-Datei dienen dazu, kodierte Medien von der Container-Datei des ausgewählten
alternativen Video-Streams abzurufen (Merkmal c5). Dabei bedeutet die Anweisung
„mithilfe der angeforderten Index-Informationen zu den kodierten Medien“ („retrieve
… using the requested index information to the encoded media“) im Einklang mit
der oben getroffenen Auslegung des Merkmals b3, dass der Index entweder indirekt
(vgl. Streitpatentschrift Figur 8: Nachrichtenfolge MKV Headers Request und MKV
Index Request) oder aber direkt zum Wiedergabegerät gelangt ist. Das Abrufen
kodierter Medien zeigt Figur 8 als wiederholende Schleife mit den Nachrichten MKV
Cluster Element(s) Request/Download.


Die abgerufenen Stücke Videomaterial aus dem ausgewählten alternativen Video-Stream werden mittels des Dekodierers wiedergegeben (Merkmal c6).


Wird eine Änderung in den Streaming-Bedingungen detektiert, soll ein neuer
alternativer Video-Stream ausgewählt werden, der für die Streaming-Bedingungen
besser geeignet ist als der vorher ausgewählte alternative Video-Stream (Merkmal
c7). Auf diese Weise kann reagiert werden, wenn sich die verfügbare Bandbreite
erhöht oder verringert (vgl. Streitpatentschrift Absatz [0070]).




                                          II.


Das Streitpatent ist in der Fassung nach Hauptantrag nicht rechtsbeständig, weil
der Gegenstand des Patentanspruchs 1 nicht patentfähig ist. Die von der Klägerin

                                      - 38 -



ebenfalls geltend gemachte fehlende Zulässigkeit der erteilten Fassung braucht
deshalb nicht beurteilt zu werden.


1. Der Gegenstand des Patentanspruchs 1 nach Hauptantrag ist nicht neu
gegenüber der Lehre der Druckschrift D1 unter Einschluss der dort in Bezug
genommenen Druckschrift NK13.


1.1   Aus der Druckschrift D1 ist ein Wiedergabegerät zum Ausführen von
Bitraten-adaptivem Streaming zu entnehmen (vgl. S. 87 Abschnitt 12.1 Figur 12.1:
„HTTP Streaming Client“). Hierzu lädt das Wiedergabegerät zunächst die
relevanten Metadaten und anschließend die eigentlichen Medien-Daten der
Streams über ein Netzwerk herunter (vgl. den letzten Absatz von Abschnitt 12.1).
Dabei werden die Mediendaten der Streams in Container-Dateien aufbewahrt
(3GPP File Format, vgl. S. 98 Abschnitt 12.4.1 i. V. m. dem dort als Referenz [50]
zitierten Dokument, welches als NK13 vorliegt). Ferner können Metadaten in Form
von Segment Index-Informationen in den Container-Dateien gespeichert sein (vgl.
Abschnitt 12.4.3 erster Absatz).


Dass das in der D1 gezeigte Wiedergabegerät in Gestalt eines „HTTP Streaming
Clients“ einen Prozessor mit zugehöriger Klient-Anwendung umfasst, ist für den
Fachmann selbstverständlich. Das Wiedergabegerät kann gemäß Abschnitt 12.1
Absatz 3 eine „Media Presentation Description (MPD)“ genannte Datei über ein
Netzwerk (S. 17 Figur 1: „Packet based network interface“) anfordern, die einer
Hauptindex-Datei gleichkommt. Nach dem letzten Absatz des Abschnitts 12.1 sind
die Mediendaten in Container-Dateien im 3GP-Dateiformat abgelegt und folglich
auch diese Dateien anzufordern. Somit ist Merkmal a gezeigt.


Eine Wiedergabe beginnt nach der Lehre von D1 gemäß Abschnitt 12.1 Absatz 4
(„To initiate the streaming service to the user”) durch Abrufen von Metadaten
(„downloading the relevant metadata”), die nach dem vorangegangenen Absatz von
D1 unter anderem der Hauptindex-Datei MPD entstammen – Merkmale c und c1.

                                          - 39 -



1.2   In der Datenstruktur der Hauptindex-Datei MPD sowie der 3GP-Container-Dateien gemäß D1 sind die Merkmale b, b1, b2 und b3 vorweggenommen:


a)    Die Hauptindex-Datei MPD enthält eine Vielzahl von URLs zu sogenannten
„Media Presentations“, welche Streams repräsentieren (Abschnitt 12.2.5.1 Absatz 1
und 2). Die URLs bezeichnen („identifies“ im Merkmal b) 3GP-Container-Dateien
(vgl. Abschnitt Q.2.2.1, Angabe „sourceURL=”clip2x.3gp” am Ende des ersten
MPD-Beispiels), welche die für das Bitraten-adaptive Streaming verfügbaren
Streams enthalten – Merkmal b.


b)    Verfügbare Streams (Media Presentations) sind als eine Abfolge von
„Periods“ gegliedert, von denen jede eine oder mehrere „Representations“ mit
demselben Quell-Inhalt enthält (Abschnitt 12.2.1 S. 88). Dabei enthalten die
Representations beispielsweise denselben Video-Inhalt (Abschnitt 7.4 Video)
kodiert mit einer unterschiedlichen Bitrate (Abschnitt 12.2.3 Representation Abs. 2).


Die Representations können ihrerseits aus einem oder mehreren „Segments“
bestehen    (Abschnitt 12.2.1   S. 88),     die    „self-contained   movie    fragments“
(Abschnitt 12.4.2.3 Media Segment Format S. 100) enthalten. Solche Segmente
umfassen demnach eine Vielzahl von Stücken von Videomaterial.


Das   Dateiformat    der   3GP-Container-Dateien         bestimmt     D1     ausdrücklich
(Abschnitt 12.4.3 erster Satz) anhand der Spezifikation TS 26.244, die als NK13 im
Verfahren ist. Nachdem D1 durch die Bezugnahme den Inhalt von NK13 aufnimmt,
sind auch die Bestimmungen von NK13 beim Merkmalsvergleich zu berücksichtigen
(vgl. BGH, Beschluss vom 17. Januar 1980, X ZB 4/79, GRUR 1980, 283 –
Terephthalsäure, Leitsatz 1). NK13 definiert im Abschnitt 5.4.3 (siehe beim ersten
Spiegelstrich: „a file shall be self-contained“), dass Video-Streams nach dem „Basic
profile“ in einer eigenen 3GP-Container-Datei gespeichert sind.


Im Ergebnis sind folglich alle Teile des Merkmals b1 gezeigt.

                                         - 40 -



c)    Jedes Stück Videomaterial eines Segments kann mit einem sogenannten
„random access point (RAP)“ beginnen (D1: vgl. Abschnitt 12.2.4.1 dritter
Unterpunkt; Abschnitt 12.6.4 vorletzter Absatz; NK13: Seite 49 vorletzter Absatz).
Dem Fachmann ist bekannt, dass beim H.264-Standard die IDR-Rahmen
(Instantaneous   Decoding     Refresh)     einen   RAP   definieren   (siehe   zum
diesbezüglichen Fachwissen beispielsweise NK14 S. 9 Abschnitt 6.2). Im Fall eines
solchen H.264-Video-Codecs ist daher jedes Stück Videomaterial als eine Gruppe
von Bildern beginnend mit einem IDR-Rahmen kodiert. Aus der technischen
Funktion eines IDR-Rahmens als Beginn einer Gruppe von Bildern, die ohne
Kenntnis vorheriger Bilder dekodiert werden kann, ergibt sich zudem, dass diese
eine geschlossene Gruppe von Bildern bildet – Merkmal b2.


d)    Die Anweisungen des Merkmals b3 nach seinem ersten und zweiten Teil sind
gleichfalls in D1 vorbeschrieben.


aa)   Die im Rahmen des 3GPP Adaptive HTTP-Streaming genutzten 3GP-Container-Dateien entsprechen dem 3GP „Adaptive Streaming Profile“ nach NK13
(D1 Abschnitt 12.4.3). Daher enthalten die 3GP-Container-Dateien eine moov-Box
als Datenelement (NK13 Abschnitt 5.4.9 S. 14 erster Unterpunkt). In der moov-Box
sind Informationen zum Identifizieren der Eigenschaften der Mediendaten beinhaltet
(D1 Abschnitt 12.4.2.2 S. 99 Abs. 4), d. h. Informationen betreffend die Kodierung
des enthaltenen Videomaterials.


Außerdem beinhaltet eine 3GP-Container-Datei als optionales Datenelement eines
Media Segments oder eines Self-Initialising Media Segments eine Segment Index
Box (kurz: „sidx“; D1 Abschnitt 12.4.2.3 S. 100 fünfter Unterpunkt bzw.
Abschnitt 12.4.2.4 sechster Unterpunkt). Eine solche sidx-Box bietet einen
kompakten Index zu Medienfragmenten und anderen sidx-Boxen eines Segments
(NK13 Abschnitt 13.4) und ist infolgedessen als Index zu den kodierten Medien in
der Container-Datei anzusehen.

                                       - 41 -



Demnach ist in der Lehre der Druckschrift D1 das Merkmal b3 nach seinem ersten
Teil erfüllt.


bb)     Die Hauptindex-Datei MPD gibt für jedes Segment eines Video-Streams
durch einen URL den Bereich der Container-Datei an, der das betreffende Segment
enthält (D1 Tabelle 12.2 S. 94). Hierbei definiert ein jeweiliger Parameter „range“
den Anfang und das Ende des Speicherbereichs, den das Segment in der
Container-Datei einnimmt (vgl. Abschnitt Q.2.2.1 am Ende des MPD-Beispiels die
Angabe      „range=“500-2000”“   zu   einem     Segment      innerhalb   einer   durch
„sourceURL=”clip2x.3gp”“ angegebenen Container-Datei).


Der Anfangsbereich eines jeden Segments bildet jeweils einen Bereich der
Container-Datei mit Informationen zu Kodierung und Index. So steht am Anfang der
Container-Datei eine moov-Box (NK13 Abschnitt 5.4.9 S. 14 erster Unterpunkt) als
Teil eines Initialisation Segments mit Informationen zur Kodierung (vgl. D1
Abschnitt 12.4.2.2 Abs. 2) und ebenso eines Self-Initialising Media Segments (vgl.
D1 Abschnitt 12.4.2.4 erster Unterpunkt zu „3GP Adaptive-Streaming profile“
i. V. m. NK13 Abschnitt 5.4.9 erster Unterpunkt). Weiterhin befindet sich eine sidx-Box mit Index-Informationen sowohl in einem Media Segment als auch in einem
Self-Initialising Media Segment jeweils im Anfangsbereich des Segments (siehe D1
Abschnitt 12.4.2.3 S. 100 fünfter Unterpunkt bzw. Abschnitt 12.4.2.4 sechster
Unterpunkt).


Aufgrund dieses Aufbaus der Segmente sind in einer Container-Datei mit einer
Representation eines Video-Streams ohne vorherige Initialisierung zwangsläufig
Informationen zu Kodierung und Index im Anfangsbereich der Container-Datei
abgelegt. Denn die Container-Datei beginnt entweder mit einem kurzen Initialisation
Segment ohne jegliche Mediendaten, welches am Anfang die moov-Box enthält, an
das sich mindestens ein Media Segment anschließt, das am Anfang die sidx-Box
beinhaltet; oder die Container-Datei beginnt mit einem Self-Initialising Media
Segment, in dessen Anfangsbereich sowohl moov-Box als auch sidx-Box abgelegt
sind (vgl. D1 Abschnitt 12.4.2.1 letzte zwei Unterpunkte).

                                         - 42 -




Indem die Hauptindex-Datei MPD durch URLs die vordefiniert strukturierten
Segmentbereiche innerhalb der Container-Datei angibt, deutet (indicates) die MPD
zugleich auf diejenigen Segmentbereiche am Anfang der Container-Datei hin,
welche Informationen zu Kodierung und Index beinhalten, wodurch es ermöglicht
wird, ebendiese Informationen anzufordern. So lehrt die D1 beispielsweise, dass die
Klient-Anwendung basierend auf der MPD Zugang zu einer Media Segment URL
eines jeden Segments erhalten und eine sidx-Box gezielt byteweise abrufen kann
(Abschnitt 12.6.4 S. 105 zweiter bzw. letzter Absatz). Infolgedessen vermittelt die
D1 dem Fachmann denselben Lösungsgedanken wie die Streitpatentschrift im
Absatz [0067], gemäß dem es in der Hauptindex-Datei enthaltene URIs gestatten,
Byte-Bereiche mit Index-Informationen von einem Server anzufordern.


Sonach ist der Druckschrift D1 auch der zweite Teil des Merkmals b3, so wie er aus
der   Auslegung    hervorgeht,    und   gemeinsam    mit   dem   Vorangegangenen
schlussendlich das gesamte Merkmal b3 zu entnehmen.


1.3    Ein bitraten-adaptives Streaming gemäß den weiteren Verfahrensschritten c2 bis c7 ist in D1 ebenfalls offenbart:


a)     Der Klient-Anwendung stehen alternative (Video-)Streams in Form
verschiedener Representations unterschiedlicher Bitrate zur Verfügung, von denen
sie einen für die Wiedergabe auszuwählen hat (S. 88 Abschnitt 12.2.3 zweiter
Absatz). Hierzu enthält die zuvor im Schritt c1 (siehe Abschnitt II.1.1) abgerufene
Hauptindex-Datei MPD für jede Representation ein Element gleichen Namens mit
einem Sub-Element „bandwidth“, das Auskunft über die benötigte „minimum
bandwidth“ gibt (Tabelle 12.2 S. 93).         Aufgrund   dieser Informationen der
Hauptindex-Datei MPD wählt die Klient-Anwendung einen der Vielzahl alternativer
Video-Streams aus, zur Nutzung bei der Wiedergabe von Medien – Merkmal c2.


b)     Die D1 gibt für den Ablauf des Streamings vor (Abschnitt 12.1 letzter Absatz),
zunächst die Metadaten herunterzuladen, und erst im Anschluss daran die

                                       - 43 -



eigentlichen Mediendaten des Streams abzurufen. Der Fachmann versteht unter
den in einer 3GP-Container-Datei gespeicherten Metadaten unter anderem die in
der moov- und sidx-Box enthaltenen Informationen betreffend die Kodierung (moov)
bzw. den Index (sidx).


Ausdrücklich zeigt die D1 in Abschnitt 12.6.4 im letzten Absatz, die sidx-Box vorab
herunterzuladen. An gleicher Stelle gibt die D1 die Lehre an, hierfür partielle HTTP-Abfragen (partial HTTP requests) einzusetzen, und dass die MPD der Klient-Anwendung den Zugriff auf jeden Media Segment URL bietet (Abschnitt 12.6.4
zweiter Absatz). Aufgrund des explizit genannten HTTP-Protokolls sieht der
Fachmann in den von D1 genannten partiellen HTTP-Abfragen der sidx-Box ein
konkretes Beispiel für das im Abschnitt 12.3 erläuterte Prinzip, mittels partieller
HTTP GET-Abfragen sowohl ganze Media Segmente als auch Teile davon
abzurufen (siehe Abschnitt 12.3 letzter Absatz: „to retrieve Initialisation Segments
or parts thereof and Media Segments or parts thereof“). Eingeordnet in den
Kontext des Abschnitts 12.6.4 vermittelt die D1 dem Fachmann folglich die Lehre,
die Hauptindex-Datei MPD für den URL-gestützten Zugriff auf das jeweilige Media
Segment zu verwenden, und mittels partieller HTTP GET-Abfragen Bereiche der
3GP-Container-Datei anzufordern, welche die sidx-Box und mithin den Index
enthalten.


Weiterhin lehrt die D1 entsprechend dem Grundsatz, zuerst die Metadaten
abzurufen, vorab das Initialisation Segment herunterzuladen (Abschnitt 12.6.4
erster Absatz letzter Satz). Hierfür wird, wie zu dem Merkmal b3 ausgeführt, der in
der Hauptindex-Datei MPD abgelegte Segment-URL verwendet. Das Initialisation
Segment beinhaltet die moov-Box mit Informationen betreffend die Kodierung.
Außerdem sieht die D1 auch für Initialisation Segments vor (siehe Abschnitt 12.3
letzter Absatz), diese ganz oder teilweise mittels partieller HTTP GET-Abfragen
abzurufen. Somit ist der D1 auch entnehmbar, die Hauptindex-Datei MPD zu
verwenden, um einen Bereich der Container-Datei anzufordern, der Informationen
betreffend die Kodierung – hier die moov-Box eines Initialisation Segments (analog:
Self-Initialising Media Segments) – enthält.

                                        - 44 -




Im Ergebnis ist folglich das Merkmal c3 erfüllt.


c)    Die Metadaten dienen dem Dekodieren und Wiedergeben der Mediendaten
(Abschnitt 12.2.1 S. 88 vierter Unterpunkt) mittels Dekodierern, welche in D1 auch
für Video-Streams spezifiziert sind (Abschnitt 12.5 i. V. m. Abschnitt 7.4). Dabei ist
es für den Fachmann selbstverständlich, dass ein Videodekodierer vor der
Wiedergabe des kodierten Videomaterials anhand von Metadaten zu konfigurieren
ist, wie sie in der zuvor abgerufenen moov-Box enthalten sind – Merkmal c4.


d)    Dem in D1 vorgezeichneten Weg entsprechend (Abschnitt 12.1) werden im
Anschluss an die Metadaten die Mediendaten des Video-Streams abgerufen. Die in
der sidx-Box enthaltenen Metadaten sind ein Index zu den Mediendaten im
betreffenden Segment (vgl. Erläuterungen zu Merkmal b3 im Abschnitt II.1.2 d) aa)).
Daher werden mithilfe der angeforderten Index-Informationen, wie sie durch die
sidx-Box gegeben sind, die kodierten Medien von der Container-Datei des
ausgewählten alternativen Video-Streams abgerufen – Merkmal c5.


e)    Streaming dient nach Definition von D1 im Abschnitt Introduction letztendlich
einem Wiedergeben von Streams, zu denen beispielsweise Video-Streams
gehören. Dementsprechend werden die zuvor abgerufenen Stücke Videomaterial
aus dem ausgewählten alternativen Video-Stream mittels des Dekodierers
(Abschnitt 12.5 i. V. m. Abschnitt 7.4) wiedergegeben – Merkmal c6.


f)    Bei der Wiedergabe kann gemäß der D1 (Abschnitt 12.6.2 S. 102
Unterpunkt 5.) zwischen Representations gewechselt werden, wobei berücksichtigt
wird, wenn sich beispielsweise die verfügbare Bandbreite ändert. Dies schließt mit
ein, dass eine Änderung in den Streaming-Bedingungen (available bandwidth)
detektiert wird. Des Weiteren kommt der Wechsel einer Representation dem
Auswählen eines neuen alternativen Video-Streams gleich, durch den die
Streaming-Bedingungen berücksichtigt sind, da er besser geeignet ist als der vor
der Änderung ausgewählte Video-Stream – Merkmal c7.

                                       - 45 -



2.    Der Auffassung der Beklagten, dass der Gegenstand des erteilten
Patentanspruchs 1 aus der Druckschrift D1 nicht hervorgehe, folgt der Senat nicht.


a)    Die Beklagte vertritt den Standpunkt, die in der D1 offenbarte MPD zeige
nicht direkt den Ort der sidx-Box innerhalb der Container-Datei. Vielmehr stehe der
Fachmann angesichts der Anweisung des Abschnitts 12.6.4, die sidx-Box vorab
herunterzuladen, vor dem ungelösten Problem, die sidx-Box innerhalb des von der
MPD angegebenen Segments zu finden. Um die sidx-Box wie in D1 vorgeschlagen
durch „byte range requests“ anzufordern, fehle dem Fachmann in D1 die Größe der
sidx-Box. Im Gegensatz dazu sei in der Streitpatentschrift genau gezeigt, wie der
Bereich mit dem Index zu finden sei. So offenbare die Streitpatentschrift hierzu
insbesondere in Absatz [0055] und [0056] ein Cues-Datenelement und Cluster-Elemente mit bekannter Größe.


Dieser Einwand vermag nicht zu überzeugen. Das gemäß dem Matroska-Containerformat spezifizierte Cues-Datenelement kann innerhalb der Container-Datei gespeichert werden (Streitpatentschrift Absatz [0054] erster und zweiter Satz)
und bildet einen Index zu den kodierten Medien in der Container-Datei
(Streitpatentschrift Absatz [0055] erster Satz). Somit ist das Cues-Datenelement mit
der in der D1 als Index angegebenen sidx-Box vergleichbar. Die Größe des Cues-Datenelements ist in der Streitpatentschrift nicht angegeben. Vielmehr lässt die
Streitpatentschrift offen, wie diese Größe ermittelt werden soll. In der Lehre der D1
verhält es sich zwar ähnlich. Doch der Fachmann wird selbstverständlich die Größe
der sidx-Box aus der Norm ISO/IEC 14496-12 ableiten, welche in D1 als
Referenz [104] sowie in NK13 als Referenz [7] genannt ist.


Indessen ist der Beklagten dahingehend beizupflichten, dass der in Tabelle 12.2 der
D1 zu den Segment-URLs angegebene „range“-Parameter nicht mit dem Begriff
„range“ in der Wendung „byte range“ des Abschnitts 12.6.4 verwechselt werden
darf. Da Letztere wie im Abschnitt II.1.3 b) erläutert vom Fachmann jedoch ohne
Weiteres den partiellen HTTP GET-Abfragen zugeordnet wird, ändert sich durch
diese Klarstellung am Ergebnis letztlich nichts.

                                        - 46 -



b)    Die Beklagte argumentiert ferner, die D1 zeige in Bezug auf das Merkmal b3
nicht, wie die MPD Bereiche innerhalb der Container-Datei angebe, die
Informationen zu Kodierung und einem Index enthielten. Sie weist hierzu auf das in
Abschnitt Q.2.2.1 der D1 dargestellte Beispiel hin, aus welchem unter anderem
41 MPD-Einträge für 40 Container-Dateien abzuleiten seien, wohingegen gemäß
dem Merkmal b3 ein einziger Verweis aus der Hauptindex-Datei auf einen Index in
der Container-Datei gefordert sei.


Dieses Argument ist nicht stichhaltig. Denn das Merkmal b3 schreibt nicht vor, wie
viele Einträge eine Hauptindex-Datei enthalten darf, um die Bereiche jeder
Container-Datei mit Informationen zu Kodierung und einem Index anzudeuten
(indicates). Wie bereits im Abschnitt I.4.5.3 zur Auslegung des Merkmals b3
ausgeführt, zeigt die     Streitpatentschrift      nicht,   wie die    im Absatz [0067]
ausschließlich im Plural genannten URIs auszugestalten sind, anhand derer Byte-Bereiche aus Matroska-Container-Dateien mit zumindest einem Teil des Indexes
angefordert   werden    können.      Dabei   ist    festzuhalten,     dass   die   D1   im
Abschnitt Q.2.2.1 ein umfangreiches Beispiel für den Inhalt einer Hauptindex-Datei
gibt, dem unter anderem vollständig formulierte URLs und viele weitere Details
entnehmbar sind. Demgegenüber offenbart die Streitpatentschrift a. a. O. lediglich
in allgemeiner Form, dass die Hauptindex-Datei URIs – ohne jegliches Detail – für
das Anfordern von Byte-Bereichen beinhalten kann. Diese im Vergleich zur Lehre
der D1 äußerst knappe Offenbarung lässt keinen Raum dafür, dem Merkmal b3
einen technischen Sinngehalt beizulegen, wonach die Hauptindex-Datei im
Unterschied zur Lehre der D1 nur einen einzigen Verweis auf einen Index in der
Container-Datei enthalten darf.


Im Übrigen offenbart die D1 eine Ausführungsform mit einem einzigen Verweis,
wodurch das Merkmal b3 nach seinem zweiten Teil sogar nach dem – vom Senat
nicht geteilten – engen Verständnis der Beklagten erfüllt ist. Denn im
Abschnitt 12.4.2.1 (letzte Zeile) nennt die D1 eine Representation, die aus genau
einem Self-Initialising Media Segment besteht. Ein solches Segment kann in einer
eigenen Container-Datei gespeichert sein. Die Hauptindex-Datei MPD beinhaltet

                                      - 47 -



dann für diese Container-Datei und dessen Segment auch nur eine einzige
Segment-URL. Das entspricht dem zweiten Teil des Merkmals b3 nach der
Auslegung der Beklagten.


Darüber hinaus enthält eine derartige Container-Datei lediglich eine einzige sidx-Box, welche einen Index zu sämtlichen kodierten Medien in der gesamten
Container-Datei bildet. Diese sidx-Box befindet sich definitionsgemäß im
Anfangsbereich der Container-Datei, welchen die Hauptindex-Datei MPD durch den
vorgenannten Segment-URL – ohne jeden Zweifel auffindbar – angibt. Außerdem
ist eine solche einzelne sidx-Box kompakt und ohne Header adressierbar, so dass
sie selbst nach der Auslegung der Beklagten als Index im Sinne des Merkmals b3
zu gelten hat.


c)    Die Beklagte meint ferner, die in der MPD-Datei nach D1 gespeicherten
URLs würden einen Index zu den kodierten Medien in der Container-Datei bilden.
Dieser befinde sich folglich in der MPD-Datei selbst. Anspruchsgemäß umfasse
hingegen jede Container-Datei einen derartigen Index (Merkmal b3).


Mit diesem Einwand vermag die Beklagte nicht durchzudringen. Aus dem Umstand,
dass die in der MPD-Datei enthaltenen URLs es gestatten, Segmente zu finden, in
denen unter anderem kodierte Medien abgelegt sind, folgt nicht zwangsläufig, dass
die D1 keine andere Datenstruktur offenbart, welche den Bedingungen des
Merkmals b3 im Hinblick auf den Index genügt. Durch die sidx-Box ist eine solche
Datenstruktur gegeben, wie oben ausgeführt.


d)    Die Beklagte wendet außerdem ein, das „Basic Profile“ nach NK13 komme
nicht in Betracht, weil D1 für adaptives Streaming nur solche Container-Dateien
zulasse, die die Anforderungen des „Adaptive Streaming Profile“ erfüllten.


Diesem Argument steht entgegen, dass eine Container-Datei gemäß NK13
mehreren Profilen genügen kann (Abschnitt 5.4.1 „General“). Die Anforderungen
gemäß „Basic profile“ und „Adaptive-Streaming profile“ betreffen voneinander

                                       - 48 -



unabhängige Sachverhalte (Abschnitt 5.4.3 bzw. 5.4.9). Dementsprechend zählt die
NK13 in Tabelle 5.1 (letzte Zeile) für das „Adaptive-Streaming profile“ nach
Release 9 („3gh9“) als kompatible Profile ausdrücklich das „Basic profile“ nach
Release 6, 7 und 8 auf, indem dort „Compatible brands“ mit den Bezeichnungen
„3gp6, 3gp7, 3gp8“ genannt sind.


e)    Weiterhin ist die Beklagte der Ansicht, das Standarddokument D1 offenbare
viele, insbesondere optionale, Elemente eines adaptiven Streaming-Systems, nicht
aber eine unter die Vorgaben des Patentanspruchs 1 fallende konkrete Streaming-Variante, weil diese vom Fachmann ausgehend von der D1 durch mehrfache
Entscheidungen erst ausgewählt werden müsse.


Diesem Argument kann nicht gefolgt werden. Die Beklagte scheint aus dem Umfang
des Dokuments D1 zu schließen, es bedürfe über die zahlreichen in der D1
unmittelbar und eindeutig offenbarten Elemente hinaus noch einer gesonderten
Begründung, warum der Fachmann gerade eine bestimmte Untermenge aus dieser
Gesamtheit herausgreifen würde. Ein solches Erfordernis sieht das Patentgesetz
nicht vor. Die Beklagte hat auch keine Rechtsnorm genannt, auf die sie ihre
Auffassung stützt.


Soweit die Beklagte in diesem Zusammenhang auf die BGH-Entscheidungen
Olanzapin (BGH, Urteil vom 16. Dezember 2008, X ZR 89/07, GRUR 2009, 382)
und Dentalgerätesatz (BGH, Urteil vom 5. April 2011, X ZR 1/09, GRUR 2011, 707)
hinweist, geht dieser Versuch fehl. Denn beide Entscheidungen betreffen jeweils
einen anderen Sachverhalt.


So befasst sich die Olanzapin-Entscheidung des Bundesgerichtshofs mit der Frage,
inwieweit eine allgemein offenbarte chemische Strukturformel dem Fachmann
durch Mitlesen darüber hinaus konkrete chemische Einzelverbindungen offenbart,
die nicht ausdrücklich genannt sind. Vorliegend geht es jedoch um Sachverhalte,
die der D1 durchwegs unmittelbar und eindeutig entnehmbar sind, weshalb sich die
Frage eines Mitlesens überhaupt nicht stellt.

                                        - 49 -



In der weiterhin genannten Dentalgerätesatz-Entscheidung des Bundesgerichtshofs
wird festgehalten, dass ein Gerätesatz nicht bereits deswegen neuheitsschädlich
vorweggenommen ist, wenn dessen verschiedene Komponenten im Stand der
Technik zwar als Einzelgegenstände vorbekannt waren, jedoch ohne die
zusätzliche Angabe, funktionsbestimmt zusammengefügt werden zu können.
Demgegenüber ist vorliegend der einem einzelnen Offenbarungsort, nämlich der D1
einschließlich NK13, entnehmbare Stand der Technik zu betrachten, der in einem
dedizierten Abschnitt 12 der D1 als ein adaptives Streaming spezifiziert ist, dessen
Gestaltungsmöglichkeiten sich sämtlich in ein und denselben funktionalen
Bezugsrahmen einordnen.


f)      Auch dem Einwand der Beklagten, Patentanspruch 1 sei auf ein Gerät
gerichtet, wohingegen die D1 ein Protokoll beschreibe, kann nicht beigetreten
werden. Denn das anspruchsgemäße Wiedergabegerät ist nahezu ausschließlich
durch Verfahrensmerkmale bestimmt. Diese gehen, wie erläutert, ohne Weiteres
aus der D1 hervor.


Sofern die Beklagte darüber hinaus argumentiert, die D1 sei ein noch nicht
verabschiedeter Entwurf und daher womöglich unvollständig und widersprüchlich,
führt dies zu keiner anderen Beurteilung. Denn die Beklagte hat in der Lehre der D1
keine Widersprüche aufgedeckt. Zudem sind die Anweisungen der D1 zumindest
im Hinblick auf den Anspruchsgegenstand vollständig genug, um diesen
nacharbeiten zu können.




                                         III.


Auch die Hilfsanträge bleiben ohne Erfolg. Der Nichtigkeitsgrund der mangelnden
Patentfähigkeit besteht in den Fassungen der Hilfsanträge I bis VIII unverändert fort.
Im Hinblick darauf kann dahingestellt bleiben, ob die Fassungen jeweils zulässig
sind.

                                             - 50 -



1.    Der Hilfsantrag I          hat keinen      Erfolg,   weil der       Gegenstand seines
Patentanspruchs 1 nicht neu ist.


Im Unterschied zur erteilten Fassung ist im Patentanspruch 1 gemäß Hilfsantrag I
zwischen den Merkmalen c3 („using the top level index file to request the portions
of the container file …“) und c4 („configure a video decoder …“) das folgende
Merkmal des erteilten Unteranspruchs 2 (mit vom Senat vergebener Bezeichnung
c8 sowie redaktionellen Änderungen) eingefügt:


 c8         wherein the retrieved portion of the wobei                 dieder      abgerufenen
            container     file    of   the   selected Bereiche der Container-Datei des
            alternative     video       stream     that ausgewählten alternativen Videocontains the index to the encoded Streams, der den Index zu den
            media within the container file kodierten Medien in der Containerincludes sufficient index information Datei enthält, ausreichende Indexto stream the entirety of the Informationen                      enthält,   um   die
            selected      alternative    stream       of Gesamtheit derdes ausgewählten
            video;                                         alternativen    Video-Streams     zu
                                                           streamen,


Demnach wird für den abgerufenen Bereich (engl.: „the retrieved portion“) der
Container-Datei des ausgewählten alternativen Video-Streams, der den Index zu
den kodierten Medien in der Container-Datei enthält, über die erteilte Fassung
hinaus festgelegt, dass dieser Bereich ausreichende Index-Informationen enthält,
um die Gesamtheit (entirety) des ausgewählten alternativen Video-Streams zu
streamen.


Doch jedenfalls dann, wenn die Gesamtheit der Mediendaten eines ausgewählten
alternativen Video-Streams in einem Self-Initialising Media Segment nach D1 und
folglich in einer einzelnen Container-Datei gespeichert ist (d. h. in dem in
Abschnitt II.2.b) erläuterten Fall), bildet die sidx-Box dieses einzigen Segments
einen Index mit ausreichenden Index-Informationen, um die Gesamtheit des

                                       - 51 -



Segments und somit auch des darin enthaltenen Video-Streams zu streamen –
Merkmal c8.


Der Einwand der Beklagten, der D1 sei keine Lehre dahingehend zu entnehmen,
die sidx-Boxen mehrerer Mediensegmente gleichzeitig herunterzuladen, greift
daher zumindest bei der vorgenannten Fallgestaltung mit einem einzigen Segment
nicht durch.




2.       Auch Hilfsantrag II hat keinen Erfolg, weil der Gegenstand seines
Patentanspruchs 1 nicht neu ist.


Um einer etwaigen Unzulässigkeitsrüge zu begegnen, ist im Patentanspruch 1
gemäß Hilfsantrag II ein Teil des Merkmals c2 wie folgt gestrichen:


 c2_II             select one or more streams including one of the plurality of
                   alternative video streams to utilize in the playback of media
                   based upon the retrieved at least a portion of the top level
                   index file;


Weiterhin sind in den Merkmalen b3 und c3 jeweils die Zeichenfolgen „(i)“ und „(ii)“
in folgender Weise eingefügt:


 b3_II            each container file includes (i) information concerning the
                  encoding of the video contained within the container file and (ii)
                  an index to the encoded media within the container file and the
                  top level index file indicates the portions of each container file
                  containing this information;
                  ...

                                           - 52 -



 c3_II               using the top level index file to request the portions of the
                     container file that include (i) the information concerning the
                     encoding of the video contained within the container file and (ii)
                     the index to the encoded media within the container file


In den abgeänderten Merkmalen b3_II und c3_II soll jeweils klargestellt werden,
dass die Container-Datei (i) Informationen betreffend die Kodierung und zudem (ii)
einen Index zu den kodierten Medien beinhalten soll.


Die Patentfähigkeit des Gegenstands des gemäß Hilfsantrag II abgefassten
Patentanspruchs 1 ist nicht anders zu beurteilen als beim erteilten Anspruch 1
gemäß Hauptantrag. Denn die D1 offenbart, wie im Abschnitt II.1.2 d) aa)
ausgeführt, auch einen Index (sidx) zu den kodierten Medien in der Container-Datei
gemäß den geänderten Merkmalen b3_II und c3_II; und einen Stream aufgrund der
abgerufenen Hauptindex-Datei auszuwählen (Merkmal c2_II), geht aus den im
Abschnitt II.1.3 a) zu dem Merkmal c2 erläuterten Stellen der D1 hervor.




3.       Hilfsantrag III kann nicht günstiger beurteilt werden.


Patentanspruch 1          gemäß    Hilfsantrag III   vereinigt    die   Änderungen   der
Hilfsanträge I und II gegenüber der erteilten Fassung. Der dadurch gebildete
Anspruchsgegenstand gibt wegen der technischen Unabhängigkeit der geänderten
Merkmale keinen Anlass, die Patentfähigkeit anders zu beurteilen als bei den
jeweils für sich genommen Hilfsanträgen I und II.




4.       Hilfsantrag IV    hat    keinen   Erfolg,   weil   der     Gegenstand   seines
Patentanspruchs 1 durch die D1 in Verbindung mit der NK13 neuheitsschädlich
vorweggenommen ist.

                                        - 53 -



Basierend auf Hilfsantrag II sind im Patentanspruch 1 nach Hilfsantrag IV die
Container-Dateien (Merkmal b, b1) durch folgende Änderungen näher bestimmt:


 b_IV      that identifies a plurality of container files that each contain the a
           streams available to the playback device for use in adaptive bitrate
           streaming, where
 b1_IV     the available streams include a plurality of alternative video streams,
           each of the alternative video streams (32) is the same source video
           content encoded at a different bitrate and is stored as a single stream
           in a separate container file as a plurality of portions of video,


Demnach sollen gemäß dem geänderten Merkmal b_IV die Container-Dateien
jeweils einen Stream enthalten (container files that each contain a stream), und
analog dazu soll gemäß dem geänderten Merkmal b1_IV jeder der alternativen
Video-Streams als ein einzelner Stream in einer eigenen Container-Datei
gespeichert sein (stored as a single stream in a separate container file).


Im Abschnitt II.1.2 b) ist bereits in Bezug auf das Merkmal b1 erläutert, dass Video-Streams nach der Lehre der NK13 gemäß dem „Basic profile“ in einer eigenen 3GP-Container-Datei gespeichert sein können. Für das „Basic profile“ legt die NK13 im
Abschnitt 5.4.3 fest, dass die maximale Anzahl an Spuren bei Video-Streams genau
eins betragen soll (maximum number of tracks shall be one for video). Demzufolge
geht aus der NK13 hervor, dass in einer dem „Basic profile“ entsprechenden 3GP-Container-Datei ein Video-Stream nur einzeln gespeichert werden darf. Es ist davon
auszugehen, dass diese Eigenschaft auch bei einer Kombination des „Basic Profile“
mit dem „Adaptive-Streaming Profile“ erhalten bleibt, da sich in diesem Fall die
Eigenschaften einer 3GP-Containerdatei gemäß Abschnitt 5.4.1 der NK13 nach den
Bedingungen beider Profile richten (may conform to several profiles). Somit ist der
Gegenstand     nach   den    geänderten     Merkmalen b_IV      und    b1_IV   gemäß
Hilfsantrag IV durch die NK13, auf welche die D1 Bezug nimmt, vorweggenommen.

                                         - 54 -



5.      Hilfsantrag V ist nicht günstiger zu beurteilen.


Patentanspruch 1      gemäß     Hilfsantrag V     weist    sämtliche   Änderungen    der
Hilfsanträge I, II und IV gegenüber der erteilten Fassung auf. Auch diese
geänderten Merkmale sind, wie zu den zugrundeliegenden Hilfsanträgen erläutert,
im   durch    Druckschrift D1 unter     Einschluss        der   in Bezug genommenen
Druckschrift NK13 gegebenen Stand der Technik vorbeschrieben.




6.      Auch den Hilfsanträgen VI und VII kann nicht stattgegeben werden.


Patentanspruch 1 in der jeweiligen Fassung gemäß Hilfsantrag VI und VII geht aus
vom Anspruchswortlaut nach Hilfsantrag IV bzw. V und ergänzt das Merkmal a
folgendermaßen:


 a_VI        A playback device (20) configured to perform adaptive bitrate
             streaming, the playback device comprising a processor configured, via
             a client application, to request a top level index file and container files
             from a remote server via a network;


Demzufolge wird in dem geänderten Merkmal a_VI festgelegt, dass Hauptindex-Datei und Container-Dateien von einem entfernten Server (from a remote
server) über ein Netzwerk angefordert werden sollen.


In Abschnitt 12.1 mit Figur 12.1 der D1 ist offenbart, dass ein HTTP Streaming
Client sowohl die Hauptindex-Datei MPD als auch die übrigen Metadaten und
Mediendaten von einem HTTP Streaming Server anfordert. Demnach ist das
Merkmal a_VI (… from a remote server …) gleichfalls der D1 entnehmbar.
Infolgedessen ist der jeweilige Gegenstand des Patentanspruchs 1 gemäß
Hilfsantrag VI und VII nicht anders zu beurteilen als nach den zugrundeliegenden
Hilfsanträgen IV bzw. V.

                                        - 55 -



7.     Hilfsantrag VIII kann gleichfalls keinen Erfolg haben.


Ausgehend vom Patentanspruch 1 nach Hilfsantrag VII wird am Ende des
Anspruchs Folgendes hinzugefügt:


 c9         wherein the client application configures the playback device to request
            portions of the top level index file and the container files from remote
            servers via Hypertext Transfer Protocol (HTTP) byte range requests.


In    dem   neu   gebildeten    Merkmal c9       gemäß   Hilfsantrag VIII   wird   das
Wiedergabegerät dahin näher bestimmt, dass es Teile der Hauptindex-Datei und
Container-Dateien von entfernten Servern mittels Hypertext Transfer Protocol
(HTTP) „byte range requests“ anfordern soll.


Der in D1 spezifizierte Adaptive HTTP-Streaming Client soll gemäß Abschnitt 12.3
Initialisierungssegmente und Mediensegmente oder Teile davon mittels HTTP GET-Abfragen anfordern. Diese sind wie das gesamte HTTP-Protokoll im Internet-Standard RFC2616 normiert, den die D1 als Referenz [17] benennt (ebda). An
anderer Stelle (S. 19 Abs. 6) lehrt die D1, 3GP-Container-Dateien herunterzuladen,
indem fortschreitend (progressive) „HTTP GET requests with byte ranges“ gemäß
dem Standard [17] eingesetzt werden. Damit ist der die Container-Dateien
betreffende Teil des Merkmals c9 in D1 vorbeschrieben.


Weiterhin ist der D1 entnehmbar (Abschn. 12.2.5.1 Introduction Abs. 4), dass die
Hauptindex-Datei MPD mittels HTTP-Protokoll zum Wiedergabegerät übermittelt
werden kann (If the MPD is delivered over HTTP). Dies kann gemäß dem im
Abschnitt 12.6.7 genannten Status Codes 206 mittels partieller HTTP GET-Abfragen, die ebenso als „HTTP GET requests with byte ranges“ bezeichnet
werden, erfolgen. Demzufolge ist das auf die Hauptindex-Datei gerichtete
Teilmerkmal des Merkmals c9 aus D1 gleichfalls bekannt.

                                       - 56 -



Im Ergebnis offenbart die Druckschrift D1 auch das mit Hilfsantrag VIII hinzugefügte
Merkmal c9.




                                         IV.


Nachdem der Patentanspruch 1 des Streitpatents weder in der erteilten Fassung
nach Hauptantrag noch in einer der Fassungen gemäß den Hilfsanträgen Bestand
hat und die abhängigen Patentansprüche nicht gesondert verteidigt werden, war
das Streitpatent insgesamt für nichtig zu erklären.




                                         V.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.




                                         VI.


                               Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt     schriftlich   beim    Bundesgerichtshof,     Herrenstraße     45a,
76133 Karlsruhe, einzulegen.

                                         - 57 -



Die Berufungsschrift muss


-     die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-     die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten.


Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des
angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht       (BGH/BPatGERVV)         auf   elektronischem    Weg    beim
Bundesgerichtshof einzulegen, wird hingewiesen (www.bundesgerichtshof.de/
erv.html).




        Hartlieb        Dr. Forkel   Dr. Himmelmann        Dr. Städele     Dr. Harth
     wg. Urlaubs an
     der Unterschrift
        gehindert
    Dr. Himmelmann
