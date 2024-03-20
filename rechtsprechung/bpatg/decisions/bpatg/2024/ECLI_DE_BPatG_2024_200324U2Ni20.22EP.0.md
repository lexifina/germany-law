---
ecli: "ECLI:DE:BPatG:2024:200324U2Ni20.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 20/22"
decided: "2024-03-20"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=6&nr=44097&anz=391&pos=100&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-03-20_2_Ni_20_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 20/22 vom 2024-03-20

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                       Verkündet am
                                                       20. März 2024
2 Ni 20/22 (EP)

(Aktenzeichen)


                      In der Patentnichtigkeitssache
…




ECLI:DE:BPatG:2024:200324U2Ni20.22EP.0

                                         -2-




               betreffend das europäische Patent EP 3 143 741
                              (DE 60 2015 060 876)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 20. März 2024 unter Mitwirkung der Vorsitzenden
Richterin Hartlieb sowie der Richter Dipl.-Phys. Dr. rer. nat. Friedrich, Dipl.-Phys.
Dr. rer. nat. Zebisch, Dr. Himmelmann und Dr.-Ing. Kapels


für Recht erkannt:


I.      Das europäische Patent EP 3 143 741 wird mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für
        nichtig erklärt, dass seine Ansprüche folgende Fassung erhalten:


        1. A method for transmitting data in a wireless network,
           the method comprising:
           generating (1000), by a transmitter, an orthogonal frequency division
           multiple access, OFDMA, frame including a 256 tone payload (200,
           400, 500) consisting of 234 tones carried in a plurality of symbol based
           resource units, RUs (210, 410, 510), and 22 tones (220, 422, 426, 522,
           526) excluded from the plurality of symbol based RUs,
           wherein each of the plurality of symbol based RUs (210, 410, 510)
           consists of a multiple of 26 tones, the multiple being 1 or 2; and
           transmitting (1020) the generated OFDMA frame to at least one
           receiver over a 20 megahertz, MHz, frequency channel;
           wherein each multiple of 26 tones of the plurality of symbol based RUs
           (210, 410, 510) is composed of 24 data tones and 2 pilot tones.

                                      -3-



       2. The method of claim 1, wherein one of the symbol based RUs consists
         of 4 pilot tones and 48 data tones.


       3. A transmitter (1110) comprising:
         a processor (1104); and
         a computer readable storage medium (1106) storing programming for
         execution by the processor, the programming including instructions to:
         generate an orthogonal frequency division multiple access, OFDMA,
         frame including a 256 tone payload (200, 400, 500) consisting of 234
         tones carried in a plurality of symbol based resource units, RUs (210,
         410, 510), and 22 tones (220, 422, 426, 522, 526) excluded from the
         plurality of symbol based RUs, wherein each of the plurality of symbol
         based RUs (210, 410, 510) consists of a multiple of 26 tones, the
         multiple being 1 or 2; and
         transmit the generated OFDMA frame to at least one receiver over a 20
         megahertz, MHz, frequency channel;
         wherein each multiple of 26 tones of the plurality of symbol based RUs
         (210, 410, 510) is composed of 24 data tones and 2 pilot tones.


       4. The transmitter of claim 3, wherein one of the symbol based RUs consists
         of 4 pilot tones and 48 data tones.


II.    Im Übrigen wird die Klage abgewiesen.


III.   Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.


IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu
       vollstreckenden Betrages vorläufig vollstreckbar.

                                             -4-



                                     Tatbestand




Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in englischer Verfahrenssprache erteilten europäischen Patents EP 3 143 741
(deutsches Aktenzeichen DE 60 2015 060 876.3) (Streitpatent), das am
12. Juni 2015 unter Inanspruchnahme der Prioritäten US 201462011475 P vom
12. Juni 2014, US 201462020902 P vom 3. Juli 2014 und US 201462028208 P vom
23. Juli 2014 angemeldet worden ist und das die Bezeichnung „METHOD AND
TRANSMITTER FOR ORTHOGONAL FREQUENCY DIVISION MULTIPLE
ACCESS      (OFDMA)       RESOURCE            ALLOCATION“       („VERFAHREN        UND
SENDEGERÄT FÜR OFDMA-RESSOURCENZUWEISUNG“) trägt. Der Hinweis
auf die Erteilung des Streitpatents wurde am 21. Oktober 2020 veröffentlicht.


Das in vollem Umfang angegriffene Streitpatent umfasst zwei zueinander
nebengeordnete (Patentansprüche 1 und 3) und zwei auf diese zueinander
nebengeordneten         Ansprüche        direkt      rückbezogene       Unteransprüche
(Patentansprüche 2 und 4).


Der erteilte Patentanspruch 1 lautet gemäß EP 3 143 741 B1 (Streitpatentschrift)
mit einer bei unverändertem Wortlaut eingefügten Gliederung gemäß Anlage NK8
der Klägerin in der Verfahrenssprache Englisch und in der mit der Streitpatentschrift
(vgl. Anlage NK3 der Klägerin) veröffentlichten deutschen Übersetzung:


 1.        A method for transmitting data in Verfahren zur Datenübertragung in
           a wireless network, the method einem drahtlosen Netzwerk, wobei
           comprising:                             das Verfahren Folgendes umfasst:
 1.1.      generating      (1000),      by    a Erzeugen      (1000),    durch    einen
           transmitter,    an        orthogonal Sender,      eines      Rahmens     für
           frequency      division     multiple Orthogonal-Frequenzmultiplexaccess,        OFDMA,         frame Mehrfachzugriff       bzw.    OFDMA-

                                         -5-



           including a 256 tone payload Rahmens,             beinhaltend       256-Ton-
           (200, 400, 500) consisting of       Nutzdaten      (200,     400,        500),
                                               bestehend aus
 1.1.1.    234 tones carried in a plurality of 234   Tönen,     die     in     mehreren
           resource units, RUs (210, 410, Ressourceneinheiten                bzw.   RUs
           510), and                           (210, 410, 510) geführt werden, und
 1.1.2.    22 tones (220, 422, 426, 522, 22 Tönen (220, 422, 426, 522,
           526) excluded from the plurality 526), die von den mehreren RUs
           of RUs,                             ausgeschlossen sind,


 1.1.3.    wherein each of the plurality of wobei jede der mehreren RUs (210,
           RUs (210, 410, 510) consists of 410, 510) aus einem Mehrfachen
           a multiple of 26 tones; and         von 26 Tönen besteht; und
 1.2.      transmitting     (1020)         the Senden      (1020)     des     erzeugten
           generated OFDMA frame to at OFDMA-Rahmens an mindestens
           least one receiver over a 20 einen Empfänger über einen 20
           megahertz,     MHz,    frequency Megahertz-Frequenzkanal bzw. 20
           channel;                            MHz-Frequenzkanal;
 1.3.      wherein each multiple of 26 wobei jedes Mehrfache von 26
           tones of the plurality of RUs Tönen der mehreren RUs (210, 410,
           (210, 410, 510) is composed of 510) aus 24 Datentönen und 2
           24 data tones and 2 pilot tones.    Pilottönen zusammengesetzt ist.


Der erteilte Patentanspruch 3 lautet gemäß Streitpatentschrift mit einer bei
unverändertem Wortlaut eingefügten Gliederung gemäß Anlage NK8 der Klägerin
in der Verfahrenssprache Englisch und in der mit der Streitpatentschrift (vgl. Anlage
NK3 der Klägerin) veröffentlichten deutschen Übersetzung:


 3.        A transmitter (1110) comprising: Sender        (1110),     der     Folgendes
                                               umfasst:

                                           -6-



3.1.       a processor (1104); and               einen Prozessor (1104); und
3.2.       a computer readable storage ein                              computerlesbares
           medium        (1106)         storing Speichermedium              (1106),        das
           programming for execution by Programmierung                    zur     Ausführung
           the processor, the programming durch           den     Prozessor         speichert,
           including instructions to:            wobei         die         Programmierung
                                                 Anweisungen beinhaltet zum:
3.2.1.     generate      an         orthogonal Erzeugen         eines       Rahmens         für
           frequency     division       multiple Orthogonal-Frequenzmultiplexaccess,      OFDMA,           frame Mehrfachzugriff          bzw.         OFDMA-
           including a 256 tone payload Rahmens,                beinhaltend         256-Ton-
           (200, 400, 500) consisting of         Nutzdaten        (200,         400,      500),
                                                 bestehend aus
3.2.1.1.   234 tones carried in a plurality of 234       Tönen,      die     in     mehreren
           resource units, RUs (210, 410, Ressourceneinheiten                     bzw.     RUs
           510), and                             (210, 410, 510) geführt werden, und
3.2.1.2.   22 tones (220, 422, 426, 522, 22 Tönen (220, 422, 426, 522, 526),
           526) excluded from the plurality die          von    den       mehreren         RUs
           of RUs,                               ausgeschlossen sind,
3.2.1.3.   wherein each of the plurality of wobei jede der mehreren RUs (210,
           RUs (210, 410, 510) consists of 410, 510) aus einem Mehrfachen
           a multiple of 26 tones; and           von 26 Tönen besteht; und
3.2.2.     transmit the generated OFDMA Senden des erzeugten OFDMA-
           frame to at least one receiver Rahmens               an    mindestens          einen
           over a 20 megahertz, MHz, Empfänger                       über         einen     20
           frequency channel;                    Megahertz-Frequenzkanal bzw. 20
                                                 MHz-Frequenzkanal;
3.2.3.     wherein each multiple of 26 wobei jedes Mehrfache von 26
           tones of the plurality of RUs Tönen der mehreren RUs (210, 410,

                                        -7-



           (210, 410, 510) is composed of 510) aus 24 Datentönen und 2
           24 data tones and 2 pilot tones.    Pilottönen zusammengesetzt ist.


Zum Wortlaut der ebenfalls angegriffenen Unteransprüche 2 und 4 wird auf die
Streitpatentschrift verwiesen.


Die Klägerin stützt ihre Klage auf den Nichtigkeitsgrund der mangelnden
Patentfähigkeit mit Blick auf fehlende Neuheit und fehlende erfinderische Tätigkeit.


Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:
NK1          Verletzungsklageschrift vom 2. März 2022 der Beklagten gegen
             (u.a.) die Klägerin an das Landgericht D… – Patentstreitkammer –;
NK1a         Ladung des Landgerichts D…vom 1. April 2022 zum Haupttermin;
NK2          DPMA: Registerauszug zum Aktenzeichen 60 2015 060 876.3; Stand
             am 25. April 2022 (letzte Aktualisierung im DPMAregister am 3. März
             2022);
NK3          EP 3 143 741 B1 (Streitpatent);
NK4          WO 2015/192 047 A1 (Offenlegungsschrift);
NK5          US-Prioritätsanmeldung 62/011,475 vom 12. Juni 2014;
NK6          US-Prioritätsanmeldung 62/020,902 vom 3. Juli 2014;
NK7          US-Prioritätsanmeldung 62/028,208 vom 23. Juli 2014;
NK8          Merkmalsgliederung des Patentanspruchs 1;


D1           IEEE 802.11-15/0330r4, Shahrnaz Azizi et al.: „OFDMA Numerology
             and Structure”, 13. Mai 2015;
D1_1         IEEE 802.11 Documents, Auszug: TGax 2015;
D1_2         IEEE 802.11-15/0622r00, Yasuhiko Inoue, IEEE 802.11 TGax, May
             2015 Vancouver Meeting Minutes;
D2           EP 3 293 932 A1;
D2_1         US-Prioritätsanmeldung 62/157,344 vom 5. Mai 2015;
D3           WO 2016/164 621 A1;

                                  -8-



D3_1    US-Prioritätsanmeldung 62/144,838 vom 8. April 2015;
D3_2    EP 3 281 345 A0;
D4      WO 2015/187 720 A2;
D4_1    EP 3 149 879 A0;
D5      IEEE Standard for Local and metropolitan area networks, Part 16: Air
        Interface for Fixed and Mobile Broadband Wireless Access Systems,
        Amendment 2: Physical and Medium Access Control Layers for
        Combined Fixed and Mobile Operation in Licensed Bands and
        Corrigendum 1, S. xviii, xix, 513, 514, 528, 529, 532, 534, 542-545,
        28. Februar 2006;
D6      Vortragsfolien Raj Jain: WiMAX Part I: PHY, 2008;
D6_1    Programm: CSE574S: Wireless and Mobile Networking (Spring
        2008);
D6_2    WaybackMachine, Calendar für D6_1;
D7      Jinsoo Choi et al.: „Envisioning 11ax PHY Structure – Part I“, IEEE
        11-14/0804r1 vom 14. Juli 2014;
D7_1:   Screenshot einer IEEE Webseite, die die öffentliche Zugänglichkeit
        von D7 ab dem 16. Juli 2014 dokumentiert;
D8      Dongguk Lim et al.: „Envisioning 11ax PHY Structure – Part II“, IEEE
        11-14/0801r0 vom 14. Juli 2014;
D8_1    Screenshot einer IEEE Webseite, die die öffentliche Zugänglichkeit
        von D8 ab dem 14. Juli 2014 dokumentiert;
D9      Yasuhiko Inoue: Protokoll des IEEE 802.11 TGax Treffens im Juli
        2014 in San Diego, bei dem D7 und D8 vorgestellt wurden, IEEE
        802.11-14/0864r0;
D10     „802.11ac Technology Introduction White Paper“ von
        Rohde & Schwarz, März 2012.

                                          -9-



Die Klägerin stellt den Antrag,
             das europäische Patent EP 3 143 741 mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
             nichtig zu erklären.


Die Beklagte stellt zuletzt den Antrag,
             die Klage abzuweisen
             hilfsweise
             das europäische Patent EP 3 143 741 unter Klageabweisung im
             Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik
             Deutschland insoweit für nichtig zu erklären, als seine Ansprüche über
             die Fassung eines der Hilfsanträge 1 vom 8. Mai 2023, 2 vom
             15. Mai 2023 sowie 3 und 4 jeweils vom 20. März 2024 – in dieser
             Reihenfolge – hinausgehen.


Die Beklagte erklärt in der mündlichen Verhandlung vom 20. März 2024, dass sie
die Patentansprüche gemäß Haupt- und Hilfsanträgen als jeweils geschlossene
Anspruchssätze ansehe, die jeweils insgesamt beanspruche.


Die Beklagte überreicht in der mündlichen Verhandlung vom 20. März 2024 dem
Senat die Hilfsanträge 3 und 4 und der Klägerin Kopien dieser Hilfsanträge.


Die Beklagte, die das Streitpatent mit einem Hauptantrag und hilfsweise beschränkt
mit 4 Hilfsanträgen verteidigt, tritt der Argumentation der Klägerin in allen
wesentlichen Punkten entgegen und erachtet den Gegenstand des Streitpatents für
patentfähig. Die beanspruchte Lehre sei jedenfalls in der Fassung einer der
Hilfsanträge patentfähig.


Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:
HW-NK7AA           Assignment Agreement zwischen der F…Inc. und der
                   Beklagten vom 3. Juni 2015;

                                       - 10 -



HW-D4_P1          US-Prioritätsanmeldung 62/006,522 vom 2. Juni 2014;
HW-D4_P2          US-Prioritätsanmeldung 62/027,425 vom 22. Juli 2014.


Die Änderungen in Anspruch 1 des Hilfsantrags 1 vom 8. Mai 2023 und des
Hilfsantrags 2 vom 15. Mai 2023 der Beklagten sind gegenüber der erteilten
Fassung des Streitpatents im Merkmal 1.1.3 erfolgt.


Es lautet im Hilfsantrag 1 vom 8. Mai 2023:
1.1.3H1:     wherein each of the plurality of RUs (210, 410, 510) consists of a
             multiple of 26 tones, the multiple being 1 or 2; and


Es lautet im Hilfsantrag 2 vom 15. Mai 2023:
1.1.3H2:     wherein each of the plurality of RUs (210, 410, 510) consists of a
             multiple of 26 tones, the multiple being 1; and


Das Merkmal 3.2.1.3. des Patentanspruchs 3 wurde im Hilfsantrag 1 vom 8. Mai
2023 und im Hilfsantrag 2 vom 15. Mai 2023 in der gleichen Weise geändert.


Die Ansprüche des Hilfsantrags 3 vom 20. März 2024 sind dem Tenor zu
entnehmen.


Wegen des Wortlauts der Ansprüche des Hilfsantrags 4 und der weiteren
Einzelheiten wird auf den Akteninhalt verwiesen.

                                         - 11 -



                           Entscheidungsgründe




Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG i. V. m. Art. 138 Abs. 1 lit. a) EPÜ, Art. 52,
54 und 56 EPÜ geltend gemacht wird, ist zulässig.


Die Nichtigkeitsklage ist auch insoweit begründet, als das Streitpatent wegen
fehlender Patentfähigkeit für nichtig zu erklären ist, soweit es über die von der
Beklagten zulässigerweise beschränkt verteidigte Fassung nach Hilfsantrag 3
hinausgeht. Auch im Umfang der Hilfsanträge 1 und 2 ist das Streitpatent wegen
fehlender Patentfähigkeit nicht rechtsbeständig. Die Ansprüche 2 und 4 des
Hilfsantrags 2 sind zudem nicht ausführbar.


Dagegen erweist sich das Streitpatent in der Fassung nach dem zulässigen
Hilfsantrag 3 als rechtsbeständig, da die beanspruchten Verfahren und
Gegenstände patentfähig sind. Die Klage ist daher insoweit unbegründet.




                                           I.


1.     Das Streitpatent betrifft ein System und ein Verfahren zur drahtlosen
Kommunikation und insbesondere ein System und ein Verfahren zur OFDMA
(Orthogonal Frequency Division Multiple Access) Ressourcenzuweisung (vgl.
Abs. [0001] des Streitpatents NK3).


Gemäß der Beschreibung des Streitpatents würden WLANs (Wireless Local Area
Networks) in dichtbesiedelten Umgebungen aufgestellt, die Zugangspunkte für eine
große Anzahl von Stationen im selben geographischen Gebiet zur Verfügung stellen
würden. WLANs der nächsten Generation müssten gleichzeitig verschiedene
Datenverkehrstypen mit unterschiedlichen Anforderungen an die Servicequalität

                                      - 12 -



(QoS) unterstützen, denn mobile Geräte würden immer mehr verwendet, um Videos
zu streamen, mobile Spiele zu spielen und andere Services zu nutzen. Der Standard
Institute of Electrical and Electronics Engineers (IEEE) 802.11ax werde entwickelt,
um diesen Herausforderungen gerecht zu werden, und es werde mit ihm ein bis zu
vierfacher Durchsatz der IEEE 802.11ac Netzwerke erwartet (vgl. Abs. [0002] des
Streitpatents NK3).




2.     Die Klägerin erklärt in ihrem Klageschriftsatz den technischen Hintergrund
des Streitpatents ausführlich, weshalb diese Erklärung im Folgenden auszugsweise
wiedergegeben wird.


Unter OFDMA versteht der Fachmann ein orthogonales Frequenzmultiplexverfahren mit Mehrfachzugriff, d.h. eine Mehrbenutzerversion des herkömmlichen
OFDM     Modulationsverfahrens.    Bei    OFDM     handelt   es    sich   um   ein
Modulationsverfahren, bei dem innerhalb eines Frequenzkanals eine Vielzahl
orthogonaler Träger zur digitalen Datenübertragung verwendet wird. Der zu
übertragende Datenstrom wird in eine Vielzahl von Teildatenströmen mit jeweils
niedrigerer Datenrate aufgeteilt, die dann über die Vielzahl von Trägern übertragen
werden. Die Träger werden auch Töne genannt („subcarriers“, „tones“, vgl. auch
Abs. [0010], [0022] des Streitpatents NK3).


Der Unterschied zwischen OFDM und OFDMA erschöpft sich in der Art und Weise,
wie die Zuteilung der Vielzahl von Trägern an einzelne Nutzer erfolgt. Bei OFDM
sind während eines Zeitabschnitts sämtliche Träger einem einzelnen Nutzer
zugeordnet, wie dies in der folgenden, von der Klägerin eingereichten Zeichnung
gezeigt wird:

                                      - 13 -




(Quelle: Wi-Fi 6 & 6E for dummies Seite 21, Anlage der Verletzungsklage)


Bei OFDMA können während eines Zeitabschnitts Teilgruppen der Träger
verschiedenen Nutzern zugeordnet werden, d.h. der Frequenzkanal oder das
Frequenzband wird dynamisch in Unterkanäle oder Teilbänder aufgeteilt, wie dies
in der folgenden von der Klägerin eingereichten Zeichnung gezeigt wird:




(Quelle: Wi-Fi 6 & 6E for dummies Seite 23, Anlage der Verletzungsklage)


In der vorstehenden Abbildung werden im ersten Zeitabschnitt die Daten von zwei
Nutzern übertragen, im zweiten Zeitabschnitt die Daten von vier Nutzern und im

                                         - 14 -



dritten Zeitabschnitt die Daten von nur einem Nutzer. Die Unterkanäle oder Träger-Teilgruppen werden im WLAN Standard IEEE 802.11ax als Ressourceneinheiten
(resource units RU) bezeichnet. Eine RU beschreibt demnach die Zuordnung von
Ressourcen     im   zweidimensionalen        Raum   über   Zeit    und    Frequenz.   Im
Frequenzbereich sind die Ressourcen in Töne unterteilt; im Zeitbereich sind es
Symbole (vgl. Abs. [0015] des Streitpatents NK3 und siehe die hier wiedergegebene
Fig. 3). Ein Ton entspricht einer Trägerfrequenz und ein Symbol entspricht einer
festgelegten Zeiteinheit, während der eine bestimmte die Information enthaltende
Modulation erfolgt. Während eines Symbols kann eine bestimmte Anzahl von Bits
                                   auf jedem der Töne übertragen werden. Die
                                   gesamte Frequenzbandbreite des Sendekanals
                                   wird also bei OFDMA dynamisch in Unterkanäle mit
                                   geringerer     Bandbreite      aufgeteilt,   die   an
                                   unterschiedliche Nutzer vergeben werden können.
                                   OFDMA ist eine bekannte Technologie, die zum
                                   Anmeldezeitpunkt bereits bei den Funk-Standards
                                   WiMax und LTE eingesetzt wurde.


                                   Das Streitpatent zielt auf WLANs (wireless local
                                   area network - drahtlose lokale Netzwerke) der
                                   nächsten, also der sog. sechsten Generation. Ein
                                   WLAN System ist in der hier wiedergegebenen
Figur 1 des Streitpatents dargestellt. Ein
Zugangspunkt („access point“) 110
sendet an eine Vielzahl von mobilen
Stationen    120.    Dabei     bezeichnet
„downlink“ die Datenübertragung vom
Zugangspunkt          in          Richtung
Mobilstationen      und     „uplink“   die
Datenübertragung            von        den
Mobilstationen         in         Richtung

                                       - 15 -



                                    Zugangspunkt       (vgl.     Abs.      [0013]    des
                                    Streitpatents   NK3        und     siehe   die   hier
                                    wiedergegebene      Figur        1).   OFDMA     soll
                                    erlauben, dass der Zugangspunkt im Downlink
                                    zeitgleich in Richtung einer Vielzahl von
                                    Mobilstationen, d.h. an verschiedene Nutzer
                                    senden kann, während im Uplink zeitgleich eine
                                    Vielzahl     von     Mobilstationen        Richtung
                                    Zugangspunkt senden.


                                    Einige Träger bzw. Unterträger („subcarrier“)
                                    enthalten keine Nutzdaten, sondern sind sog.
                                    Pilotsignale, auch „Pilottöne“ genannt, deren
                                    Daten der Synchronisation zwischen Sender
und Empfänger dienen. Im Downlink, bei dem der Zugangspunkt einen Rahmen mit
sämtlichen Unterkanälen (RUs) versendet, können hierfür gemeinsame Pilottöne
vorgesehen sein, die nicht in den RUs enthalten sind (vgl. Abs. [0016] und siehe
Fig. 4 des Streitpatents NK3, „common pilot tones“).


Im Uplink, in dem jede Mobilstation nur in den ihr zugeordneten RUs Daten einfügt,
müssen die Pilottöne in den RUs vorgesehen sein, da ansonsten die Sender (die
Mobilstationen) keine Pilottöne einfügen könnten (vgl. Abs. [0017] und siehe die
Fig. 5 des Streitpatents NK3 „pilots per RU“).




3.    Das Streitpatent gibt keine Aufgabenstellung an. Die Beklagte gibt in ihrer
Widerspruchsbegründung vom 24. November 2022 auf Seite 4 an, dass die
objektive Aufgabe in der Bereitstellung einer OFDMA Rahmenstruktur für 20 MHz
Bandbreite mit einer 256-Ton-Payload mit einer geeigneten minimalen RU
Granularität und Struktur bestünde, die eine hohe Spektrumseffizienz bereitstellt
und eine verlässliche Phasen- und/oder Frequenzabschätzung ermögliche. Zum

                                        - 16 -



Nachweis verweist sie auf Fig. 6 und Sp. 3, Z. 36 bis 41 der Beschreibung des
Streitpatents NK3. Dieser Aufgabenstellung stimmt der Senat zu.




4.    Die angegebene Aufgabe wird durch das Verfahren des Anspruchs 1 des
Streitpatents und den Gegenstand des dazu nebengeordneten Anspruchs 3 gelöst.


Auch wenn neben dem mit Anspruch 1 beanspruchten Verfahren mit Anspruch 3
ein Sender beansprucht wird, besteht die Erfindung in einem OFDMA-Tonplan für
eine Bandbreite von 20 MHz. Die Bandbreite wird dabei in 256 Töne mit dann
78,125 kHz Bandbreite aufgeteilt. Dies ist die zum Anmeldezeitpunkt übliche
Bandbreite für OFDM und dessen Subcarrier, die auch als Töne bezeichnet werden.
Von diesen 256 Tönen werden 234 für Ressourceneinheiten (RU) verwendet, die
dann Nutzern, also Empfängern zugewiesen werden können. Die verbleibenden 22
Töne werden keiner Ressourceneinheit zugewiesen. Anspruch 1 lässt offen, ob
diese Töne Verwendung finden und welche Verwendung sie finden.


Die hier gezeigte Fig. 5 zeigt, dass 8 der 22 verbleibenden Töne beispielsweise als
reservierte   (common     reserved     tones     522)   für    andere   Zwecke       der
Informationsübertragung verwendet werden, während die restlichen 14 als Nulltöne
verwendet werden. Nulltöne tragen keine Information und können als DC oder
Guardtöne dienen (vgl. Abs. [0017] der Streitpatentschrift).


Die   234 Töne     sind   in   eine   Mehrzahl („plurality“),   also    mindestens    2
Ressourceneinheiten (RU) aufgeteilt. Jede dieser Ressourceneinheiten besitzt ein
Vielfaches („multiple“) von 26 Tönen, wobei auch der Faktor 1 als Vielfaches
anzusehen ist, wie Fig. 5 zeigen dürfte, da dort 9 Ressourceneinheiten gezeigt
werden, die 9 ∙ 26 = 234 Töne aufweisen (vgl. auch Abs. [0010], Sp. 3, Z. 32 bis 35:
„In one embodiment, each RU in an OFDMA frame consists of a multiple of 26 data
tones (e.g., 26 data tones, 52 data tones, 78 data tones, etc.).”). Anspruch 1 macht
auch keine Angaben darüber, wo im Gesamtspektrum die Töne einer RU liegen.

                                      - 17 -



                                           Insbesondere wird nicht beansprucht,
                                           dass die Töne einer RU benachbart
                                           zueinander sein müssen.


                                           Jedes dieser Vielfachen von 26 Tönen
                                           weist 24 Datentöne und 2 Pilottöne auf.
                                           Dies      bedeutet,   dass     in    den
                                           Ressourceneinheiten für jeweils 26
                                           Töne zwei Pilottöne vorhanden sein
                                           müssen, d.h. 2 bei 26 Tönen, 4 bei 52,
                                           6 bei 78 usw.). Wo diese Pilottöne in der
                                           Ressourceneinheit angeordnet sind,
                                           wird mit Anspruch 1 nicht festgelegt.


                                           Ebenfalls nicht festgelegt wird, ob der
                                           beanspruchte Rahmen im Uplink oder
                                           im Downlink verwendet wird, d.h., ob
der Rahmen vom Sender im Accesspoint (AP, 110 in Fig. 1) oder im mobilen Gerät
(120 in Fig. 1) verwendet wird. In der Beschreibung wird zwar auf eine Verwendung
des Rahmens im Uplink hingewiesen (vgl. Abs. [0017]: „FIG. 5 illustrates a diagram
of another embodiment tone allocation scheme for a 256-tone payload 500 in an
uplink OFDMA frame communicated over a 20MHz frequency channel. …“), doch
ist dies für den Schutzbereich nicht beschränkend.




5.    Der hier zuständige Fachmann ist als Ingenieur der Fachrichtung
Nachrichtentechnik oder als Informatiker mit Hochschulabschluss zu definieren, der
eine mehrjährige Tätigkeit auf dem Gebiet der Entwicklung oder Weiterbildung von
drahtlosen   Informationsübertragungsnetzen       ausübt   und   dabei   auch   die
Veröffentlichungen der Normierungsgremien verfolgt.

                                       - 18 -



6.    Für den von der Klägerin angegebenen Klagegrund der fehlenden
Patentfähigkeit muss zunächst der Zeitrang der Ansprüche festgestellt werden,
denn die Klägerin macht geltend, dass das Streitpatent die angegebenen US-
amerikanischen Prioritäten vom 12. Juni 2014 (NK5), 3. Juli 2014 (NK6) und 23. Juli
2014 (NK7) zu Unrecht beanspruche, so dass der Zeitrang des Streitpatents der
Anmeldetag 12. Juni 2015 sei.


6.1. Die Klägerin gibt an, dass die Inhaberin und auch Anmelderin des Streitpatents
die H…Ltd sei (siehe die Offenlegungsschrift NK4). Die Anmelderin der
Prioritätsanmeldungen ist aber die F…Inc., …, U…. Damit bestehe keine Identität
des Anmelders des Streitpatents und des Anmelders der Prioritätsanmeldungen.
Da die Beklagte keinen Nachweis für den Übergang der Prioritätsanmeldungen NK
5 und NK6 auf sie erbracht hat, ist davon auszugehen, dass die Rechte aus diesen
beiden Prioritäten zum Anmeldezeitpunkt nicht auf sie übergegangen waren, so
dass sie nicht wirksam in Anspruch genommen werden können (Art. 87 EPÜ).


Für die Priorität NK7 vom 23. Juli 2014 hat die Beklagte das Dokument NK7AA
eingereicht, mit dem die F…Inc. die Rechte an der Prioritätsanmeldung NK7 am 3.
Juni 2015 auf die Beklagte übertragen hat. Damit besaß die Beklagte am
Anmeldetag des Streitpatents, also am 12. Juni 2015 die Rechte auf die
Prioritätsanmeldung NK7, so dass sie deren Priorität wirksam in Anspruch nehmen
konnte.


6.2 Die Priorität NK7 vom 23. Juli 2014 offenbart zwei verschiedene Ausführungen
von Zuweisungsmustern für Ressourceneinheiten (RU), nämlich eine, die für
Ressourceneinheiten mit unbestimmter zeitlicher Länge (k, siehe Fig. 4 und vgl.
Abs. [0026]: „Figure 3 illustrates the OFDMA WLAN frame structure excluding the
PHY header. The frame structure occupies a two-dimensional space in time and
frequency as shown in Figure 3. A resource unit in general includes n subcarriers
and k OFDMA symbols as shown in Figure 3.“) gilt und am Beispiel einer Länge von
k = 8 erläutert wird, sowie einer weiteren („another“), die symbolbasiert ist und als

                                       - 19 -



SRU bezeichnet wird (vgl. Abs. [0020]: „With respect to OFDMA symbol by symbol
resource allocation, in order to accommodate the conventional WLAN encoder and
interleaver processing unit on a symbol basis, an embodiment provides another
resource allocation design, a symbol-based RU (SRU).“).


Für den ersten Fall offenbart das Dokument NK7 Ressourceneinheiten (RU) mit 26
Tönen (vgl. Abs. [0003]: „An embodiment method for wireless communications
includes allocating tones in an Orthogonal Frequency-Division Multiple Access
(OFDMA) frame in accordance with a resource unit (RU) having 26 tones in a
frequency domain and 8 symbols in a time domain.”). Damit ergeben sich bei einer
Bandbreite von 20 MHz, aufgeteilt auf 256 Töne automatisch 234 (= 9 · 26)
Datentöne (vgl. Abs. [0016]: „OFDMA resource allocation designs were proposed in
[1]-[4]. An embodiment herein provides an additional OFDMA resource allocation.
We designed an RU based on 242 data and pilot tones, and 14 guard tones and DC
Null for 256 FFT per 20 MHz [1]. As for the downlink (DL) OFDMA frames, we
designed a total of 234 data tones, 8 common pilot tones (the pilots across the whole
OFDMA symbol), and 14 guard tones (including one DC Null) per OFDMA symbol
[1].“).


Weiter wird vorgeschlagen, im Uplink, anders als im Downlink Pilottöne in den
Ressourceneinheiten zu benutzen und zwar 2 in einer RU (vgl. Abs. [0018]: „The
uplink (UL) OFDMA frames use assigned pilot(s) per RU, different from the DL
OFDMA frames. An embodiment provides 26 subcarriers per RU in the frequency
domain, where 24 of those tones are for data and 2 of those tones are for pilots.
There are 8 OFDMA symbols in the time domain per RU. Because two tones are
set aside for pilots every symbol in an RU, there are a total of 192 tones available
for data, and 16 tones are set aside for pilots in an RU. The channel encoder and
interleaver are processed on an RU basis. The 8 common pilots in the UL OFDMA
frames are still located in the same position as the DL OFDMA frames, which
become the left-over tones for the UL OFDMA frames.”). Damit ist zunächst ein
Tonplan mit 256 Tönen bestehend aus 234 Tönen, die in einer Mehrzahl von RUs

                                          - 20 -



enthalten sind, aus der Priorität NK7 bekannt. Zudem sind dort RUs offenbart, die
ein Vielfaches von 26 Tönen aufweisen. Dies ist für Ressourceneinheiten mit der
Länge k nämlich für das Vielfache N = 1 aus den Figuren 1 und 2 ersichtlich. Weitere
Tonanzahlen werden für die Länge k nicht offenbart.


Für die zweite Ausführung, nämlich symbolbasierte Ressourceneinheiten, wird auch
das Vielfache N = 2 (52 Töne) offenbart (vgl. Abs. [0022]: „For an SRU with the 12
tone multiple allocation sets, there are 26 (24 data tones, 2 pilot tones), 52 (48 data
tones, 4 pilot tones), 102 (96 tones, 6 pilot tones), 200 (192 data tones, 8 pilot tones),
and 400 (384 data tones, 16 pilot tones) OFDMA SRU sets. The AP may generate
34 total modes in combination of the above 5 SRU sets, but 11 combination modes
among the 34 total modes are selected and the remaining 23 modes are discarded
according to the size of unused tones, that is, the modes with small unused tone
sizes are selected. The detailed SRU combination modes are provided in the
attached document entitled "SRU Subchannelization Table," which is filed herewith
and incorporated herein by reference”). Nicht offenbart sind dagegen RUs mit einem
Tonumfang der weiteren Vielfachen N = 3 (78 Töne), N = 4 (104 Töne), N = 5 (130
Töne), N = 6 (156 Töne), N = 7 (182 Töne), N = 8 (208 Töne) und N = 9 (234 Töne).
Dafür werden andere, nicht durch 26 teilbare Tonanzahlen angegeben, da, anders
als im Streitpatent, der relative Anteil der Pilottöne in den RUs oder SRUs mit
zunehmender Tonanzahl abnimmt (vgl. Abs. [0022]).


Dies bedeutet, dass der Fachmann der Priorität NK 7 die beanspruchte Lehre, dass
die RUs einen Tonumfang aufweisen, der ein Vielfaches von 26 Tönen ist (Merkmal
1.1.3.), nicht entnehmen kann, denn dass zwei der aufgelisteten Breiten der RUs
ein Vielfaches von 26 sind, die anderen aber nicht, lässt ihn keinesfalls zwingend
auf diese allgemeine Regel schließen. Genauso wenig kann er ihr entnehmen, dass
in den RUs das Verhältnis von Datentönen zu Pilottönen immer 24 zu 2 ist, wie dies
im Merkmal 1.3. beansprucht wird.

                                      - 21 -



Hinzu kommt, dass das Prioritätsdokument NK7 Pilottöne in den RUs der Länge k
nur für den Uplink vorsieht nicht jedoch für den Downlink (vgl. Abs. [0018]: „The
uplink (UL) OFDMA frames use assigned pilot(s) per RU, different from the DL
OFDMA frames“), was in den Ansprüchen 1 und 3 des Streitpatents NK3 mangels
einer entsprechenden Beschränkung auf den Uplink mitbeansprucht wird.


Daraus folgt, dass das in Anspruch 1 des Streitpatents NK3 beanspruchte Verfahren
in der Priorität NK7 in der beanspruchten Breite nicht offenbart ist und das
Streitpatent für seine Ansprüche auch die Priorität auf die Anmeldung NK7 zu
Unrecht in Anspruch nimmt. Der Zeitrang der Ansprüche des Streitpatents ist
deshalb der Anmeldetag und damit der 12. Juni 2015.




7.    Druckschrift D1 (IEEE 802.11-15/0330r4) wurde, wie aus dem Dokument
D1_1 ersichtlich ist, am 13. Mai 2015 und damit vor dem Anmeldetag auf den Server
von IEEE 802.11 hochgeladen und war damit vor dem Anmeldetag des Streitpatents
der Öffentlichkeit zugänglich. Dokument D1 ist somit relevanter Stand der Technik.


Dokument D1 beschäftigt sich, wie alle Dokumente der IEEE 802.11 Gruppe mit
dem sog. WLAN (Wireless Local Area Network) und damit mit der Übertragung in
einem „drahtlosen“ Netzwerk. Es offenbart u.a. eine OFDMA-Übertragung bei einer
Bandbreite von 20 MHz (vgl. Folie 10: „It was agreed to use 4x OFDM symbol
duration in 11ax [5,6] as follows – 11ax has duration 12.8 us (without CP) based on
a 256 FFT in 20 MHz, 512 FFT in 40 MHz, 1024 FFT in 80 MHz/80+80 MHz and
2048 FFT in 160 MHz – 4x symbol duration allows better granularity for OFDMA •
There are more number of tones in a given OFDMA bandwidth”), was eine
Gesamtanzahl von 256 Tönen bedeutet.


Für eine Bandbreite von 20 MHz werden RUs definiert, die 26 Töne mit 2 Pilottönen,
52 Töne mit 4 Pilottönen, 106 Töne, mit ebenfalls 4 Pilottönen und 242 Töne mit 8
Pilottönen aufweisen (vgl. Folie 14: „The Proposed Resource Units in 20MHz BW

                                       - 22 -



• The proposed resource units have the following sizes – 26-tone with 2 pilots – 52-
tone with 4 pilots – 106-tone with 4 pilots – 242-tone with 8 pilots”). Von diesen
weisen die ersten beiden ein Vielfaches von 26 Tönen auf, nämlich ein- und
zweimal.




Auf den Folien 22 und 23, deren Zeichnungen hier wiedergegeben sind, werden die
Möglichkeiten aufgezeigt, die es mit den vorgegebenen RUs gibt. Dabei wird
rechnerisch nur angenähert die RU mit 106 Tönen als 4 ∙ 26 = 104 Töne dargestellt
(vgl. Folie 22: „Note that to help with visualizing the analysis, we have illustrated

                                        - 23 -



106-tone block as 4 units of 26-tone in the pictures below.“) In der Tabelle wird dies
aber richtig aufgeführt. Von Interesse für die Beurteilung des Streitpatents sind die
Fälle für K = 5, die erste für K = 6, K = 7, 8 und 9, denn bei diesen Fällen ist keine
RU mit 106 Tönen vorhanden, so dass alle RUs eine Anzahl von Tönen aufweist,
die ein Vielfaches von 26 ist. Da zudem die RU mit 26 Tönen 2 Pilottöne und die mit
2 · 26 = 52 Tönen 4 Pilottöne aufweist, ist dort auch jedes Mehrfache von 26 Tönen
der mehreren RUs aus 24 Datentönen und 2 Pilottönen zusammengesetzt.
Während bei den Nulltönen durchaus auf Uplink und Downlink eingegangen wird
(vgl. Folie 17), wird zu den Pilottönen kein Unterschied zwischen Uplink und
Downlink erwähnt, so dass der Fachmann davon ausgeht, dass die Pilottöne in den
Ressourceneinheiten sowohl im Uplink als auch im Downlink vorhanden sind.


Bei jeder der relevanten Einteilungen in RUs gibt es 9 Einheiten zu 26 Tönen und
damit 234 Töne innerhalb der RUs. Somit verbleiben 256 – 234 = 22 Töne
außerhalb der RUs.


Damit offenbart das Dokument D1 in Übereinstimmung mit dem Wortlaut der
deutschen Übersetzung des Anspruchs 1 des Streitpatents NK3 ein


1. Verfahren zur Datenübertragung in einem drahtlosen Netzwerk, wobei das
Verfahren Folgendes umfasst:
1.1.   Erzeugen,    durch   einen   Sender,      eines   Rahmens    für   Orthogonal-Frequenzmultiplex-Mehrfachzugriff bzw. OFDMA-Rahmens, beinhaltend 256-Ton-Nutzdaten (vgl. den unteren Abs. auf Folie 10), bestehend aus:
1.1.1. 234 Tönen, die in mehreren Ressourceneinheiten bzw. RUs (vgl. die
Einteilung in RUs in den Folien 22 und 23) geführt werden, und
1.1.2. 22 Tönen (256 Töne – 234 Töne = 22 Töne), die von den mehreren RUs
ausgeschlossen sind,
1.1.3. wobei jede der mehreren RUs aus einem Mehrfachen von 26 Tönen besteht
(26 oder 52 Töne für K = 5, 6, 7, 8 und 9); und

                                       - 24 -



1.2.   Senden des erzeugten OFDMA-Rahmens an mindestens einen Empfänger
über einen 20 Megahertz-Frequenzkanal bzw. 20 MHz-Frequenzkanal (vgl. Folie
14);
1.3.   wobei jedes Mehrfache von 26 Tönen der mehreren RUs aus 24 Datentönen
und 2 Pilottönen zusammengesetzt ist (vgl. Folie 14 für den Fall von 26 und 52
Tönen pro RU).


Da das Verfahren des Anspruchs 1 keine weiteren Merkmale aufweist, war es
demnach zum Anmeldezeitpunkt nicht neu (Art. 54 EPÜ) und damit nicht patentfähig
(Art. 52 EPÜ).


Das Dokument D1 offenbart zwar den Aufbau des Senders nicht, jedoch ist der mit
Anspruch 3 beanspruchte Aufbau mit einem Prozessor, der gespeicherte
Anweisungen ausführt, üblich, weshalb der Gegenstand des Anspruchs 3 durch das
Dokument D1 dem Fachmann nahegelegt ist (Art. 56 EPÜ).




8.     Im Hilfsantrag 1 wurden Anspruch 1 und 3 darauf beschränkt, dass das
Vielfache 1 oder 2 ist. Auch ein Verfahren mit dieser Beschränkung ist aber nicht im
Prioritätsdokument NK7 offenbart, denn zum einen ist eine Breite der
Ressourceneinheit von 2 · 26 = 52 Tönen für Ressourceneinheiten der Länge k dort
nicht offenbart, zum anderen wird auch nach wie vor eine Übertragung mit
Pilottönen innerhalb der Ressourceneinheit mangels einer entsprechenden
Beschränkung sowohl im Uplink als auch im Downlink mit dem Anspruchstext auch
für Ressourceneinheiten der Länge k beansprucht. Damit ist der Zeitrang der
Ansprüche des Hilfsantrags 1 ebenfalls der Anmeldetag.


In der Folge steht dem mit Anspruch 1 beanspruchten Verfahren ebenfalls die Lehre
des Dokuments D1 entgegen. Hierzu wird auf die Folie 23 verwiesen, die
verschiedene Beispiele gemäß dem Anspruch 1 des Hilfsantrags 1 offenbart. Das

                                       - 25 -



Verfahren des Anspruchs 1 ist somit gegenüber der Druckschrift D1 ebenfalls nicht
neu (Art. 54 EPÜ) und damit nicht patentfähig (Art. 52 EPÜ).




9.     Im Hilfsantrag 2 sind die Lehren der Patentansprüche 2 und 4, die auf die
Ansprüche 1 bzw. 3 rückbezogen sind, nicht ausführbar (Art. 83 EPÜ), denn gemäß
Anspruch 1 bzw. 3 des 2. Hilfsantrags gibt es keine Ressourceneinheiten mit
4 Pilottönen und 48 Datentönen, denn alle Ressourceneinheiten haben genau
26 Töne. Damit kommt es zu einem Widerspruch im Text der Ansprüche. Die
Ausführbarkeit wurde von der Klägerin zwar nicht angegriffen, doch ist sie bei neuen
Ansprüchen, wie sie die Ansprüche der Hilfsanträge sind, von Amts wegen zu
überprüfen.


Zudem ist auch der Zeitrang der Ansprüche des Hilfsantrags 2 der Anmeldetag,
denn   der    Wortlaut   der   Ansprüche    1   und    3   enthält   weiterhin   eine
richtungsunabhängige Übertragung der beanspruchten Ressourceneinheiten, die
aber im Dokument NK7, wie bereits ausgeführt wurde, für Ressourceneinheiten der
Länge k nicht offenbart ist. Damit ist auch für den Anspruch 1 des Hilfsantrags 2
Dokument D1 relevanter Stand der Technik. Es nimmt mit seinem letzten Beispiel
auf Folie 23, das nur Ressourceneinheiten mit 26 Tönen, von denen gemäß Folie
14 zwei Töne Pilottöne sind, das mit Anspruch 1 beanspruchte Verfahren
neuheitsschädlich vorweg.




10.    Das Verfahren des Anspruchs 1 des Hilfsantrags 3 ist ursprünglich offenbart
und patentfähig, da es sowohl neu ist als auch auf einer erfinderischen Tätigkeit des
Fachmanns beruht. Dies gilt auch für den Gegenstand des nebengeordneten
Anspruchs 3. Damit hat das Streitpatent im Umfang dieses Antrags Rechtsbestand.
Auf Hilfsantrag 4 kommt es damit nicht mehr an.

                                         - 26 -



10.1 Das Verfahren des Anspruchs 1 ist ursprünglich offenbart (Art. II § 6 Abs. 1
Satz 1 Nr. 3 IntPatÜbkG i.V.m. Art. 138 Abs. 1 lit. c) EPÜ), denn Anspruch 1 des
erteilten Patents wurde dahingehend eingeschränkt, dass das Vielfache von 26
Tönen im Merkmal 1.1.3 auf das ein- oder zweifache von 26 Tönen, also auf 26 oder
52 Töne eingeschränkt wurde. Diese beiden Möglichkeiten sind im in Bezug auf die
ursprüngliche Offenbarung nicht angegriffenen Anspruch 1 bereits enthalten, denn
sie sind zwei Möglichkeiten aus der Formulierung „multiple of 26 tones“ und werden
in der Offenlegungsschrift NK4 explizit als Beispiele genannt (vgl. S. 3, Z. 22 bis 24:
„In one embodiment, each RU in an OFDMA frame consists of a multiple of 26 data
tones (e.g., 26 data tones, 52 data tones, 78 data tones, etc.)“).


Die weitere Einschränkung des Anspruchs 1 des Hilfsantrags 3 auf eine
symbolbasierte Ressourceneinheit kann dem Absatz [0011] des Streitpatents NK3,
der aus dem Absatz Seite 3, Zeile 35 bis Seite 4, Zeile 3 der Offenlegungsschrift
NK4 hervorgeht („Embodiments of this disclosure further provide symbol based RU
tone allocation schemes in which an RU carried in an OFDMA frame consists of a
multiple of either 26 or 28 tones. In one, embodiment, the RU consists of a multiple
of 26 tones, with each multiple of 26 tones consisting of 24 data tones and 2 pilot
tones. In another embodiment, the RU consists of a multiple of 28 tones, with each
multiple of 28 tones consisting of 26 data tones and 2 pilot tones.“), entnommen
werden. Entgegen der Ansicht der Klägerin versteht der Fachmann auf Grund des
Absatzes    [0011]   des     Streitpatents   NK3     den   Ausdruck   „symbolbasierte
Ressourceneinheit“     des     Anspruchs     1     so,   dass   die   Zuweisung    der
Ressourceneinheit symbolbasiert erfolgt und nicht über mehrere Symbole. Das
Verfahren des Anspruchs 1 und in der Folge auch der Gegenstand des Anspruchs
3 sind somit ursprünglich offenbart. Da sie gegenüber dem erteilten Anspruch 1 und
dem erteilten Anspruch 3 auch beschränkt sind (Art. II, § 6 Satz 1 Nr.4 IntPatÜbkG),
sind sie somit zulässig.


10.2 Der Zeitrang des Anspruchs 1 des Hilfsantrags 3 ist der Anmeldetag der
Priorität NK7, der 23. Juli 2014.

                                       - 27 -



Anspruch 1 ist auf symbolbasierte Ressourceneinheiten beschränkt. Diese werden
in der Prioritätsschrift NK7 als SRUs bezeichnet und stellen das zweite
Ausführungsbeispiel der NK7 dar. Für dieses Beispiel wird keine Aussage darüber
getroffen, ob die Ressourceneinheiten mit Pilottönen sowohl für den Uplink als auch
für den Downlink verwendet werden oder nur für den Uplink. Der Senat teilt die
Ansicht nicht, dass die Verteilung der Pilottöne dieselbe ist wie im vorhergehenden
Beispiel mit k Symbolen als Länge der Ressourceneinheiten, denn die beiden
Beispiele werden deutlich durch „another“ voneinander getrennt. Für SRUs werden
in Abs. [0022], wie bereits ausgeführt, Ressourceneinheiten mit 26 und 52 Tönen
als Vielfache von 26 genannt. Dabei steht in Klammern zur Erläuterung 24
Datentöne und 2 Pilottöne bzw. 48 Datentöne und 4 Pilottöne. Entgegen der Ansicht
der Klägerin handelt es sich bei den in Klammern gesetzten Wörtern um eine
Erläuterung und nicht um eine Alternative für den Uplink. Dies geht aus dem
einführenden Halbsatz des Absatzes [0022] hervor, der auf Vielfache von 12 Tönen
verweist, wie es 24 und 48, nicht jedoch 26 und 52 sind (vgl. Abs. [0022]: „For an
SRU with the 12 tone multiple allocation sets, …“). Dem widerspricht entgegen der
Ansicht der Beklagten auch die Tabelle auf Seite 16 nicht. Für die Interpretation des
mittleren Tabellenteils als Ausführung ohne Pilottöne gibt es keinen Hinweis, denn
dies ist der Tabelle nicht zu entnehmen. Zu entnehmen ist ihr jedoch, dass die
Möglichkeiten der Ressourceneinheiten mit 52 Tönen nicht ausgewählt sind. Dies
spielt aber für die Offenbarung der verwendbaren Moden keine Rolle, da die
Überschrift der mittleren Tabelle u.a. sagt, dass bei der Auswahl Moden mit einer
Kombination von kleinen und großen Ressourceneinheiten bevorzugt sein sollen,
was aber die anderen Moden nicht unmöglich macht.


Damit ist das Verfahren des Anspruchs 1 im Prioritätsdokument NK7 offenbart. Der
Gegenstand des Anspruchs 3 kann dann der Figur 7 entnommen werden (vgl. Abs.
[0035]: „Figure 7 is a block diagram of a processing system that may be used for
implementing the devices and methods disclosed herein. Specific devices may
utilize all of the components shown, or only a subset of the components, and levels
of integration may vary from device to device. Furthermore, a device may contain

                                        - 28 -



multiple instances of a component, such as multiple processing units, processors,
memories, transmitters, receivers, etc. The processing system may comprise a
processing unit equipped with one or more input output devices, such as a speaker,
microphone, mouse, touchscreen, keypad, keyboard, printer, display, and the like.“)




10.3 Die Druckschriften D1 bis D3 sind kein für die Beurteilung der Patentfähigkeit
der Verfahren und Gegenstände des Hilfsantrags 3 relevanter Stand der Technik,
denn Druckschrift D1 wurde am 13. Mai 2015 der Öffentlichkeit zugänglich gemacht,
die älteste Priorität von Druckschrift D2 datiert vom 5. Mai 2015 und die älteste
Priorität der Druckschrift D3 vom 8. April 2015. Diese Daten liegen alle nach dem
Zeitrang des Streitpatents, dem 23. Juli 2014, so dass das Streitpatent älter ist.


10.4 Druckschrift D4 (WO 2015/187720 A2) ist eine internationale Anmeldung, die
am 2. Juni 2015 und damit vor dem Anmeldetag des Streitpatents, jedoch nicht vor
dem für den Zeitrang der Ansprüche des Hilfsantrags 3 des Streitpatents relevanten
Tag eingereicht wurde. Die Druckschrift D4 besitzt ebenfalls zwei Prioritäten, die vor
dem 23. Juli 2014 liegen, nämlich den 2. Juni 2014 und den 22. Juli 2014. Wie
Druckschrift D4_1 zeigt, ist die Anmeldung in die europäische nationale Phase
eingetreten, so dass Druckschrift D4 Stand der Technik in Form einer

                                       - 29 -



nachveröffentlichten älteren Anmeldung darstellen könnte, die nur für die Frage der
Neuheit eine Rolle spielt (Art. 54 Abs. 3 EPÜ).


Die Prioritätsschriften zur Druckschrift D4 hat die Klägerin zwar nicht eingereicht,
jedoch hat sie die Beklagte als HW-D4_P1 und HW-D4_P2 eingeführt. Keine dieser
beiden Prioritätsschriften offenbart eine konkrete Größe von Ressourceneinheiten
oder eine bestimmte Anzahl von Pilottönen in einer Ressourceneinheit. Damit sind
diese Prioritäten im Hinblick auf die Patentansprüche des Hilfsantrags 3 nicht
wirksam, weshalb der relevante Zeitrang frühestens der Anmeldetag der
Druckschrift D4 sein kann, der nach dem Zeitrang der Ansprüche des Hilfsantrags
3 liegt. Damit stellt auch Druckschrift D4 keinen Stand der Technik dar.


10.5 Der IEEE-Standard D5 (IEEE Standard for Local and metropolitan area
networks Part 16, IEEE Std 802.16eand IEEE Std 802.16-2004/Cor1-2005)
beschäftigt sich, wie schon der Titel angibt („Part 16: Air Interface for Fixed and
Mobile Broadband Wireless Access Systems“) mit einem Verfahren zur
Datenübertragung in einem drahtlosen Netzwerk. Er offenbart auch die
Verwendung eines OFDMA-Rahmens (vgl. S. 513: „8.4.6 OFDMA subcarrier
allocations“), sieht dafür aber gerade keinen Rahmen mit 256 Tönen, sondern nur
solche mit 1024, 512, und 128 Tönen vor (vgl. S. 514).


Die Klägerin verweist dazu auf die englischsprachige Version des Wikipedia-Artikels
„WiMax“, wohl in der heutigen Version. Dort heißt es, dass anders als bei OFDM mit
256 Trägern der WiMax-Version OFDMA hinzugefügt wurde mit Trägeranzahlen
von 128, 512, 1024 und 2048. Dies bedeutet, dass 256 Träger wohl OFDM
vorbehalten war und von diesen, wie der Artikel angibt, nur 200 genutzt wurden und
nicht 234 (vgl. den Klageschriftsatz: „802.16-2004 was updated by 802.16ein
2005 and uses scalable orthogonal frequency-division multiple access [18]
(SOFDMA), as opposed to the fixed orthogonal frequency-division multiplexing
(OFDM) version with 256 sub-carriers (of which 200 are used) in 802.16d.“). Es ist
somit kein Grund ersichtlich, warum der Fachmann ausgehend vom Standard D5

                                      - 30 -



einen OFDMA-Rahmen mit 256 Tönen verwenden sollte, wenn ausgerechnet dieser
Wert für OFDMA weggelassen wurde. Auch fehlen die konkreten Angaben über die
Größe der RUs, wie die Klägerin selbst zugibt.


Sie argumentiert jedoch, dass für das Streitpatent die Werte entsprechend aus einer
Mehrzahl von ursprünglich offenbarten Möglichkeiten ausgewählt würden, so dass
demnach auch ausgehend von den alten Standards die beanspruchten Werte in
Griffweite des Fachmanns lägen, da die grundlegende Struktur eines OFDMA-Rahmens bekannt gewesen sei und die beanspruchten Werte in der aus dem Stand
der Technik bekannten Größenordnung lägen. Hierzu sei in Dokument D5 auf die
Tabellen 310a bis 310c und 315a bis 315c verwiesen, wo die Anzahl der Töne in
einem Unterkanal, also einer RU, mit 24 und 48 angegeben wird. Einen
nachvollziehbaren Grund, warum statt 24 und 48 Trägern bzw. Tönen der
Fachmann 26 und 52 Töne verwenden sollte, gibt sie nicht an. Ein solcher ist auch
nicht erkennbar. Damit kann Druckschrift D5 das Verfahren des Anspruchs 1 nach
Hilfsantrag 3 auch nicht nahelegen.


10.6 Der Inhalt des Vortrags D6 (Raj Jain: WiMAX, Part I: PHY) beschäftigt sich mit
WiMAX und geht in Bezug auf das Streitpatent nicht über das hinaus, was auch
dem Standard D5 entnommen werden kann. Auch ausgehend von diesem Vortrag
kommt der Fachmann somit nicht in naheliegender Weise zum mit Anspruch 1 des
Hilfsantrags 3 beanspruchten Verfahren.


10.7 Die Dokumente D7 und D8 offenbaren einige Konzepte und Änderungen des
neuen WLAN-Standards IEEE 802.11 ax gegenüber seinem Vorgänger.
Ausführungen zu Ressourceneinheiten sind in diesen Dokumenten nicht enthalten.


10.8 Die Druckschrift D10 betrifft den WLAN-Standard IEEE 802.11 ac. In diesem
gibt es keine Ressourceneinheiten. Beschrieben wird u.a. die Aufteilung des zur
Verfügung stehenden Frequenzbereichs in Frequenzbänder von 20 MHz, 40 MHz,
80 MHz, 80+80 MHz und 160 MHz Breite.

                                       - 31 -




11.   Insgesamt sind die im Verfahren befindlichen Dokumente somit nicht
geeignet, die Neuheit (Art. 54 EPÜ) oder die erfinderische Tätigkeit (Art. 56 EPÜ)
der mit Hilfsantrag 3 beanspruchten Verfahren oder Gegenstände in Frage zu
stellen. Damit sind diese, da sie zweifellos auch gewerblich anwendbar sind (Art. 57
EPÜ), auch patentfähig (Art. 52 EPÜ). Das Streitpatent ist somit im Umfang des
Hilfsantrags 3 rechtsbeständig.




                                         II.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 92 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.




                                        III.


                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt schriftlich oder in elektronischer Form beim Bundesgerichtshof,
Herrenstraße 45a, 76133 Karlsruhe, einzulegen.

                                       - 32 -



Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten.


Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des
angefochtenen Urteils vorgelegt werden.




Hartlieb     Dr. Friedrich      Dr. Zebisch      Dr. Himmelmann         Dr. Kapels
