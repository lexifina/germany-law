---
ecli: "ECLI:DE:BPatG:2017:250417U6Ni76.14.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 76/14"
decided: "2017-04-25"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=18&nr=29194&anz=809&pos=276&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2017-04-25_6_Ni_76_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 76/14 vom 2017-04-25

## Entscheidung

BUNDESPATENTGERICHT
                     IM NAMEN DES VOLKES
6 Ni 76/14 (EP
verbunden mit                  URTEIL
6 Ni 77/14 (EP)                                       Verkündet am
(Aktenzeichen)                                        25. April 2017
                                                           …




                     In der Patentnichtigkeitssache

 …

                                gegen




 BPatG 253
 08.05

                                        -2-




…




                betreffend das europäische Patent EP 1 230 818
                                  (DE 600 40 799)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 25. April 2017 durch die Vorsitzende Richterin Friehe sowie die
Richter Schwarz, Dipl.-Phys. Univ. Dipl.-Wirtsch.-Phys. Arnoldi, Dipl.-Ing. Matter
und Dipl.-Phys. Dr. Haupt


für Recht erkannt:


       I.     Das europäische Patent 1 230 818 wird mit Wirkung für das
              Hoheitsgebiet der Bundesrepublik Deutschland teilweise für
              nichtig erklärt, soweit es über folgende Fassung hinausgeht:


            1. A method for conveying measurement information from a
               terminal in a first communication system
               to a GSM communication system,
                            characterised by the steps of:
                            converting a plurality of RSCP downlink measurement values associated with said first communication
               system to a plurality of downlink measurement values for

                           -3-



   said GSM    communication system by using the following
   equation:
               RXLEV = RSCP + OFFSET,
               wherein OFFSET is a constant;
               comparing said converted plurality of downlink
   measurement values with at least one threshold measurement value; and
               if at least one of said converted plurality of
   downlink measurement values exceeds a predetermined
   threshold measurement value, sending said at least one of
   said converted plurality of downlink measurement values on
   a control channel to a control node in said GSM communication system.


2. The method of Claim 1, wherein said first communication
   system comprises a UMTS.


3. The method of Claim 1, wherein said plurality of downlink
   measurement values associated with said GSM communication system comprises a plurality of signal strength values.


4. The method of Claim 1, wherein said control channel comprises a control channel operable in a non-stealing mode.


5. The method of Claim 1, wherein said control channel comprises a SACCH.


6. A mobile terminal for use in conveying measurement information from a first communication system to a GSM communication system,
               characterised by

                            -4-



                means for converting a plurality of RSCP downlink measurement values associated with said first communication system to a plurality of downlink measurement values for said GSM communication system by using the following equation:
                RXLEV = RSCP + OFFSET,
                wherein OFFSET is a constant;
                means for comparing said converted plurality of
   downlink measurement values with at least one threshold
   measurement value; and
                means for sending at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM communication
   system if said at least one of said converted plurality of
   downlink measurement values exceeds a predetermined
   threshold measurement value.


7. The mobile terminal of Claim 6, wherein said first communication system comprises a UMTS.


8. The mobile terminal of Claim 6, wherein said plurality of
   downlink measurement values associated with said GSM
   communication system comprises a plurality of signal
   strength values.


9. The mobile terminal of Claim 6, wherein said control channel
   comprises a control channel operable in a non-stealing
   mode.


10. The mobile terminal of Claim 6, wherein said control channel comprises a SACCH.

                                        -5-



       II.    Im Übrigen werden die Klagen abgewiesen.


       III.   Die Kosten des Rechtsstreits tragen die Klägerinnen zu jeweils 1/8 und die Beklagte zu 3/4.


       IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
              des zu vollstreckenden Betrages vorläufig vollstreckbar.



                                 Tatbestand


Die Beklagte ist seit 7. März 2014 eingetragene Inhaberin des auch mit Wirkung
für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen
Patents 1 230 818 (Streitpatent), das von der früheren Inhaberin, der T…-
…, S…, am 20. Oktober 2000 unter Inanspruchnahme der Priorität aus der US-amerikanischen Anmeldung 09/442,230 vom
17. November 1999 als internationale Anmeldung PCT/SE00/02043 angemeldet
wurde. Diese wurde am 25. Mai 2001 als WO 01/37602 A1 veröffentlicht. Das am
12. November 2008 in der Verfahrenssprache Englisch veröffentlichte Streitpatent
wird beim Deutschen Patent- und Markenamt unter dem Aktenzeichen 600 40 799
geführt. Es trägt die Bezeichnung


        „METHOD FOR IMPROVING HANDOVERS BETWEEN MOBILE
                          COMMUNICATION SYSTEMS“


 (in Deutsch laut Streitpatentschrift: „VERFAHREN ZUR VERBESSERUNG DES
   WEITERREICHENS ZWISCHEN MOBILKOMMUNIKATIONSSYSTEMEN“).


Das Streitpatent umfasst 16 Patentansprüche, die mit den Nichtigkeitsklagen vom
22. bzw. 23. Oktober 2014 in vollem Umfang angegriffen werden.


Die Beklagte verteidigt das Streitpatent nur noch in beschränkter Fassung nach
dem mit Schreiben vom 17. November 2015 eingereichten Hauptantrag, hilfsweise

                                          -6-



nach einem der Hilfsanträge 1 und 2 vom 17. November 2015 sowie weiter hilfsweise nach den mit Schreiben vom 10. Februar 2017 eingereichten Hilfsanträgen 3 bis 6 in dieser Reihenfolge.


Der unabhängige Patentanspruch 1 in der Fassung nach Hauptantrag vom
17. November 2015 lautet in der Verfahrenssprache Englisch wie folgt:


     A method for conveying measurement information from a terminal in a
     ﬁrst communication system to a GSM communication system,
                 characterized by the steps of:
     converting a plurality of downlink measurement values associated with
     said ﬁrst communication system to a plurality of downlink measurement
     values for said GSM communication system;
     comparing said converted plurality of downlink measurement values
     with at least one threshold measurement value; and
     if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold measurement value,
     sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said s GSM
     communication system.


Nach den Hilfsanträgen 1 bis 4 haben die jeweiligen Ansprüche 1 folgende Fassungen:


Hilfsantrag 1:
     A method for conveying measurement information from a terminal in a
     ﬁrst communication system to a GSM communication system,
     the first communication system being of a type different from the GSM
     communication system and
                 the method being characterized by the steps of:

                                          -7-



     converting a plurality of downlink measurement values associated with
     said ﬁrst communication system to a plurality of downlink measurement
     values for said GSM communication system;
     comparing said converted plurality of downlink measurement values
     with at least one threshold measurement value; and
     if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold measurement value,
     sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM
     communication system.


Hilfsantrag 2:
     A method for conveying measurement information from a terminal in a
     UMTS communication system to a GSM communication system,
                 characterized by the steps of:
     converting a plurality of downlink measurement values associated with
     said UMTS communication system to a plurality of downlink measurement values for said GSM communication system;
     comparing said converted plurality of downlink measurement values
     with at least one threshold measurement value; and
     if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold measurement value,
     sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM
     communication system.


Hilfsantrag 3:
     A method for conveying measurement information from a terminal in a
     ﬁrst communication system to a GSM communication system,
                 characterized by the steps of:

                                          -8-



     converting a plurality of RSCP downlink measurement values associated with said ﬁrst communication system to a plurality of downlink
     measurement values for said GSM communication system;
     comparing said converted plurality of downlink measurement values
     with at least one threshold measurement value; and
     if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold measurement value,
     sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM
     communication system.


Hilfsantrag 4:
     A method for conveying measurement information from a terminal in a
     ﬁrst communication system to a GSM communication system,
                 characterized by the steps of:
     converting a plurality of RSCP downlink measurement values associated with said ﬁrst communication system to a plurality of downlink
     measurement values for said GSM communication system
     by using the following equation: RXLEV = RSCP + OFFSET(RSCP),
     wherein OFFSET is a constant;
     comparing said converted plurality of downlink measurement values
     with at least one threshold measurement value; and
     if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold measurement value,
     sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM
     communication system.


Wegen des Wortlauts der Ansprüche 1 bis 10 nach Hilfsantrag 5 wird auf den Tenor Bezug genommen. Wegen des Wortlauts der übrigen Ansprüche in den Fassungen nach dem Hauptantrag sowie nach den Hilfsanträgen 1 bis 4 und 6 wird
auf die Akte verwiesen.

                                       -9-



Die Klägerinnen sind der Ansicht, dass das mit ihren Klagen angegriffene Streitpatent für nichtig zu erklären sei, weil sein Gegenstand nicht so deutlich und vollständig offenbart sei, dass ein Fachmann ihn ausführen könne. Zudem sei der
Gegenstand des Streitpatents nicht neu, beruhe nicht auf einer erfinderischen Tätigkeit und gehe über den Inhalt der europäischen Patentanmeldung in ihrer bei
der für die Einreichung der Anmeldung zuständigen Behörde ursprünglich eingereichten Fassung hinaus.


Ihr Klagevorbringen stützen die Klägerinnen unter anderem auf die Druckschriften
(Kurzzeichen nach gerichtlichem Hinweis):


     E1      Tdoc SMG2 1145/99: „Aspects GSM to UMTS Handover“. ETSI
             STC SMG2, Bordeaux, France, 20. – 24. September 1999.
             Seiten 1 – 9 (= Anlage NK3 der Klägerin zu 2)
     E2      Tdoc SMG2 1273/99: „Paper for discussion to enhance the measurement reporting”. ETSI STC SMG2, Bordeaux, France,
             20. - 24. September 1999. 3 Seiten (= Anlage NK7 der Klägerin zu 2)
     E3      TSGR2#8(99)e61: „Inter-system measurements and reporting“. TSG-RAN Working Group 2 (Radio layer 2 and Radio layer 3), Cheju, Korea, 2. – 5. November 1999 (Anlage D3 der Klägerin zu 1)


Die Klägerinnen beantragen,


        das europäische Patent 1 230 818 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,


        die Klagen abzuweisen, soweit das Patent mit dem Hauptantrag
        und den Hilfsanträgen 1 und 2 vom 17. November 2015 sowie den
        Hilfsanträgen 3 bis 6 vom 10. Februar 2017 in dieser Reihenfolge
        verteidigt wird.

                                     - 10 -



Die Beklagte tritt der Argumentation der Klägerinnen entgegen und hält den Gegenstand des Streitpatents für zulässig und wenigstens in einer der verteidigten
Fassungen für rechtsbeständig. Zur Stützung ihrer Argumentation hat die Beklagte
unter anderem die Druckschriften


     CNK9      ETSI TS 145 008 V5.22.0 (2006-04) Technical Specification.
               Digital cellular telecommuncations system (Phase 2+); Radio
               subsystem link control (3GPP TS 45.008 version 5.22.0 Release 5). RTS/TSGG-0145008v5m0. ETSI, Sophia Antipolis
               Cedex, France.
     CNK9a ETSI TS 125 133 V5.17.0 (2005-12) Technical Specification.
               Universal Mobile Telecommunications System (UMTS); Requirements for support of radio resource management (FDD)
               (3GPP TS 25.133 version 5.17.0 Release 5). RTS/TSGR-0425133v5h0. ETSI, Sophia Antipolis Cedex, France.
     CNK12 SAUTER, M.: Grundkurs Mobile Kommunikationssysteme
               UMTS, HSDPA und LTE, GSM, GPRS und Wireless LAN. 4.,
               überarbeitete und erweiterte Auflage. Wiesbaden: Vieweg +
               Teubner Verlag, 2011. Seiten 37 – 46. – ISBN 978-3-8348-
               1407-4


eingereicht.


Der Senat hat den Parteien mit der Terminsladung vom 19. Dezember 2016 einen
qualifizierten Hinweis zukommen lassen.

                                          - 11 -



                           Entscheidungsgründe


                                           A.


Die zulässigen Klagen sind nur teilweise begründet. Nachdem die Beklagte das
Streitpatent nicht mehr in der erteilten Fassung verteidigt, ist es in Bezug auf diese
Fassung bereits ohne Sachprüfung teilweise für nichtig zu erklären. Aber auch
soweit die Beklagte das Streitpatent mit den Fassungen nach dem (neuen) Hauptantrag sowie nach den Hilfsanträgen 1 bis 4 beschränkt verteidigt, sind die Klagen
begründet, da den Fassungen nach dem Hauptantrag sowie nach den Hilfsanträgen 1 bis 3 der Nichtigkeitsgrund der unzureichenden Offenbarung gemäß Artikel II § 6 Absatz 1 Nr. 2 IntPatÜG, Art. 138 Abs. 1 Buchst. b) EPÜ entgegensteht
und die Fassung nach Hilfsantrag 4 wegen Verstoßes gegen das Deutlichkeitsgebot nach Art. 84 EPÜ unzulässig ist. Demgegenüber stehen der zulässigen Fassung des Streitpatents nach dem Hilfsantrag 5 vom 10. Februar 2017 keine Nichtigkeitsgründe entgegen, so dass die Klagen insoweit abzuweisen sind.




                      I. Zum Gegenstand des Streitpatents


1.    Die Erfindung betrifft den Bereich der mobilen Kommunikation und
insbesondere ein Verfahren zur Verbesserung der Leistung eines sogenannten
Handover zwischen unterschiedlichen mobilen Kommunikationssystemen (vgl.
Absatz [0001] der Streitpatentschrift).


a)    Technischer Hintergrund


Zum technischen Hintergrund der Erfindung, der in Absatz [0002] der Streitpatentschrift nur zum Teil beschreiben wird, ist Folgendes auszuführen:


Zum Prioritätszeitpunkt, also Ende 1999, war GSM ein etablierter Mobilfunkstandard der sogenannten zweiten Generation (2G) zur digitalen Sprach- und zuneh-

                                      - 12 -



mend auch Datenübertragung. Leistungsfähigere Mobilfunksysteme der sogenannten dritten Generation (3G), insbesondere zur Datenübertragung mit deutlich
größeren Datenübertragungsraten, wie z. B. UMTS, befanden sich in der Endphase ihrer Spezifikation bzw. im Prototypen-Testbetrieb.


Mobiltelefone mit UMTS-Funktionalität wurden damals wegen der noch lückenhafte Netzabdeckung bei Einführung von UMTS grundsätzlich als sogenannte
„dual-mode“-Geräte (UMTS + GSM) ausgeführt. Die „dual-mode“-Endgeräte und
die Infrastruktur sowohl der UMTS- als auch der GSM-Netze mussten einen
Wechsel (im der vom Streitpatent übernommenen Fachterminologie als „handover“ bezeichnet) von GSM zu UMTS und zurück beherrschen bzw. unterstützen,
und zwar nicht nur, wie im Streitpatent adressiert, während einer aktiven Telefonoder Datenverbindung (vgl. Absätze [0002] – [0004]), sondern auch im sogenannten „idle mode“, also bei eingeschaltetem Mobiltelefon ohne aktive Verbindungen.


Bei der Erstellung der UMTS-Spezifikationen einen Netzwechsel zwischen GSM
und UMTS zu berücksichtigen, war vergleichsweise einfach, denn diese Anforderung lag bereits zu Beginn der UMTS-Entwicklungsphase vor. Die entsprechende,
nachträgliche Anpassung der GSM-Spezifikationen, insbesondere hinsichtlich der
GSM-Infrastruktur wie Base Station Controller (BSC) und Mobile Switching Centre
(MSC), war jedoch schwieriger.


Wegen der besseren Eigenschaften und erweiterten Möglichkeiten (insbesondere
hinsichtlich der Datenverbindungen mit höheren Datenübertragungsraten) des
UMTS-Netzes war naheliegend, dass ein „dual-mode“-Mobiltelefon bevorzugt das
UMTS-Netz nutzen sollte, wenn es verfügbar ist. Allerdings sollte ein Mobiltelefon
während einer aktiven Sprach- oder Datenverbindung nicht unverzüglich das aktuelle Netz schon dann verlassen, wenn das jeweils andere eine etwas „bessere“
Verbindungsqualität bieten könnte. Denn ein häufiger Wechsel zwischen GSM-
und UMTS-Netz ist deshalb unerwünscht, weil jeder netzübergreifende Handover-Vorgang mit zusätzlichen Signalisierungen verbunden ist, die nicht unerheblich

                                      - 13 -



Funkressourcen und Energie verbrauchen. Davon geht auch das Streitpatent aus,
denn dort wird das GSM-Netz – jedenfalls für Nutzer mit dual-mode-Geräten –
lediglich als Rückfalllösung für solche räumlichen Gebiete angesehen, in denen
UMTS noch nicht verfügbar ist (Absatz [0002]).


Findet ein Handover, sei er netzintern oder netzübergreifend, aber statt, bedarf es
zuvor der Übertragung von Messwertberichten von dem mobilen Endgerät zur der
Basisstation; dieser Vorgang wird – auch im Streitpatent - als „Uplink“ bezeichnet.
Wie in dem hierfür maßgeblichen vorveröffentlichten GSM-Standarddokument
„Radio Subsystem link control (GSM 05.08)“ (vgl. Anlage D3A der Klägerin zu 1 =
GSM 05.08 V6.3.0 (1998-11), Seite 21, Kap. 8.1.3) und in Absatz 0014 des Streitpatents beschrieben, misst ein im GSM-Netz eingebuchtes mobiles Endgerät kontinuierlich u. a. die Signalstärke bzw. -leistung der von ihm auf der Downlink-Verbindung empfangenen Signale, d. h. der Signale, die von der Basisstation der eigenen GSM-Zelle bzw. den Basisstationen der benachbarten GSM-Zellen auf ihrem jeweiligen Rundsendekanal BCCH (Broadcast Control Channel) ausgesendet
werden.


Diese Messwerte überträgt das mobile Endgerät an die GSM-Basisstation (BTS =
Base Transceiver Station) und weiter an den GSM Base Station Controller (BSC)
in der Form eines GSM-Messwerteberichts auf einem speziellen logischen Kanal,
dem SACCH (slow associated control channel) (Anlage D3A der Klägerin zu 1 =
GSM 05.08 V6.3.0 (1998-11), Seite 24, Kap. 8.4.1). Damit ist der GSM BSC stets
über die Qualität der Funkverbindungen zwischen einem mobilen Endgerät und
den dieses umgebenden Basisstationen informiert und kann bei Bedarf, z. B.
wenn sich das mobile Endgerät mit einem Kraftfahrzeug bewegt, einen GSM-internen Handover-Vorgang von der aktuellen GSM-Basisstation auf eine andere
GSM-Basisstation einleiten.


Ein einleitend genanntes dual-mode-Endgerät (UMTS + GSM) ermittelt zusätzlich
zu den GSM- auch UMTS-Messwerte aus den Signalen, die es von den umgebenden UMTS-Basisstationen empfängt, wie dies aus der hierfür maßgeblichen

                                      - 14 -



vorveröffentlichten UMTS-Spezifikation „TS 25.331 RRC Protocol Specification“
ersichtlich ist (vgl. Anlage D3B der Klägerin zu 1 = Anlage NK4 der Klägerin zu 2 =
TS 25.331 V3.0.0 (1999-10), Seite 84, Kap. 8.4.2), wobei die UMTS-Messwerte
die Qualität der potentiellen UMTS-Funkverbindungen kennzeichnen sollen.


b)    Zum Streitpatent


Von dem vorgenannten technischen Hintergrund geht auch das Streitpatent aus,
auch wenn dies in der Beschreibung nicht so ausführlich beschrieben ist. Das
Streitpatent, das nur den Wechsel vom GSM- zum UMTS-Netz thematisiert, beschäftigt sich dabei insbesondere mit der bereits oben beschriebenen, jedem
netzintern oder netzübergreifend durchgeführten Handover-Vorgang vorgelagerten
Aufgabe der Übertragung von Messwertberichten von dem mobilen Endgerät zur
der Basisstation.


Da im GSM-Standard, wie ausgeführt, zum Prioritätsdatum die Koexistenz mit
dem UMTS-Kommunikationssystem nicht berücksichtigt war, gab es zumindest
während einer aktiven Sprech- oder Datenverbindung im GSM-Netz keine Reservekapazität zur Übertragung der UMTS-Messwerte zur GSM-Basisstation und
damit zum GSM BSC (vgl. Absatz [0003] der Streitpatentschrift).


Als eine zum Prioritätszeitpunkt bekannte Lösung zu diesem Problem beschreibt
das Streitpatent in Absatz [0004], Messinformationen von einem UMTS-Teil der
Mobilstation über den sogenannten GSM „Fast Associated Control Channel
(FACCH)“ an den GSM BSC zu senden. Hierbei ergebe sich jedoch das Problem,
dass der FACCH in einem sogenannten „Stealing Mode“ arbeite, also einer „stehlenden Arbeitsweise“, bei dem ein Sprachsegment mit der Länge von 20 Millisekunden durch Signalinformationen ersetzt wird, die für einen Handover-Vorgang
erforderlich sind. Für ein Handover von einem GSM-Netz zu einem UMTS-Netz
würden somit Sprachrahmen verwendet, um UMTS-Messinformationen von der
Mobilstation an den GSM BSC zu übertragen. Dies könne die Sprachqualität erheblich reduzieren.

                                      - 15 -



Als Lösung dieses Problems wird im Absatz [0005] der Streitpatentschrift die
Übertragung der UMTS-Messwerte auf dem vorstehend bereits erläuterten, u. a.
für die Übertragung der GSM-Messwerte vorgesehenen, Kanal SACCH genannt
(Slow Associated Control Channel), der in einem „Non Stealing-Mode“ arbeitet.


2.    Die im Absatz [0005] beschriebene Übertragung der UMTS-Messwerte auf
dem SACCH-Kanal löst zwar das im Absatz [0004] der Streitpatentschrift genannte Problem der Beeinträchtigung der Qualität der Sprachübertragung. Allerdings sind die unabhängigen Patentansprüche des Streitpatents weder in der erteilten Fassung noch in einer der Fassungen nach den jetzt geltenden Anträgen
der Beklagten hierauf gerichtet. Zudem geht eine solche Lösung ebenfalls zu
Lasten einer anderen Information, da in den von dem mobilen Endgerät an den
GSM BSC gesendeten Messwertberichten UMTS-Messwerte mindestens teilweise
originäre GSM-Messwerte ersetzen (Absatz [0016]; Figur 2, Verfahrensschritte
106 und 108).


Objektiv gesehen beschäftigt sich das Streitpatent daher mit der Lösung einer anderen Aufgabe, was auch zwischen den Parteien unstreitig ist. Zur Vorbereitung
einer in dem GSM BSC zu treffenden Entscheidung, ob während einer aktiven
GSM-Verbindung ein Handover vom GSM-Netz zum, wie einleitend ausgeführt,
regelmäßig bevorzugten UMTS-Netz möglich und sinnvoll ist, müssen dem GSM
BSC auch UMTS-Messwerte betreffend die Qualität der Funkverbindung zwischen
dem mobilen Endgerät und den Basisstationen des UMTS-Netzes in einer solchen
Form übermittelt werden, dass sie von dem GSM BSC als originäre GSM-Messwerte interpretiert und mit diesen verglichen werden können.


Dabei ergibt sich die Schwierigkeit, dass die von einem dual-mode-Mobilgerät gewonnenen GSM- und UMTS-Messwerte sich voneinander unterscheiden (vgl. Absatz [0013]). Während der GSM-Teil des mobilen Endgeräts die Signalstärken
RXLEV (received signal level,) im Sinne der Signalleistungen der von den einzelnen GSM-Basisstationen empfangenen Signale misst, ermittelt der UMTS-Teil des

                                        - 16 -



mobilen Endgeräts die Größen RSCP (received signal code power) und E c/I0
(code energy-to-interference ratio) (vgl. Absatz [0014]).


Daraus ergibt sich die objektive Aufgabe, die UMTS-Messwerte qualitativ und
quantitativ in einer solchen Art und Weise umzuwandeln, dass sie zum einen über
einen GSM-Steuerkanal, bevorzugt den SACCH, an den GSM BSC übertragen
werden können und dass sie zum anderen mit den originären GSM-Messwerten
vergleichbar werden, um dem GSM BSC eine Grundlage für eine netzübergreifende Handover-Entscheidung zu bieten.


Zusätzlich muss die Umwandlung der UMTS-Messwerte in GSM-Messwerte so
durchgeführt werden, dass die begrenzte Übertragungskapazität des GSM-Steuerkanals möglichst gut genutzt wird, insbesondere unter dem Gesichtspunkt, dass
nur solche umgewandelten UMTS-Messwerte übertragen werden, die für potentiell
aufzubauende UMTS-Verbindungen mit einer hinreichenden Übertragungsqualität
stehen. Denn anderenfalls würde die Übertragung der originären GSM-Messwerte
der GSM-Nachbarzellen so stark reduziert, dass ein ggfs. erforderlicher GSM-interner Handover verzögert oder sogar verhindert würde.


3.       Zur Lösung der genannten objektiven Aufgabe schlägt das Streitpatent in
der Fassung nach Hauptantrag vom 17. November 2015 ein Verfahren mit den im
Anspruch 1 angegebenen Merkmalen vor, wobei sich dieser Anspruch wie folgt
gliedern lässt:


     1         A method for conveying measurement information
     1.1       from a terminal in a ﬁrst communication system
     1.2GSM to a GSM communication system,
               characterized by the steps of:
     2GSM      converting a plurality of downlink measurement values associated
               with said ﬁrst communication system to a plurality of downlink measurement values for said GSM communication system;

                                       - 17 -



     3        comparing said converted plurality of downlink measurement values
              with at least one threshold measurement value; and
     4.3      if at least one of said converted plurality of downlink measurement
              values exceeds a predetermined threshold measurement value,
     4        sending said at least one of said converted plurality of downlink
              measurement values
     4.1      on a control channel
     4.2GSM to a control node in said GSM communication system.


Der Anspruch 1 des mit Schriftsatz vom 17. November 2015 überreichten Hilfsantrags 1 unterscheidet sich vom Anspruch 1 in der Fassung nach Hauptantrag
durch die zusätzliche Kennzeichnung des ersten Kommunikationssystems als verschieden von dem GSM Kommunikationssystem (Änderungen ggü. dem Anspruch 1 in der Fassung nach Hauptantrag sind gekennzeichnet):


     1         A method for conveying measurement information
     1.1           from a terminal in a ﬁrst communication system
     1.2GSM        to a GSM communication system,
     1.1.1Not-GSM the first communication system being of a type different
                   from the GSM communication system and
               the method being characterized by the steps of:
     2GSM      converting a plurality of downlink measurement values associated with said ﬁrst communication system to a plurality of
               downlink measurement values for said GSM communication
               system;
     3         comparing said converted plurality of downlink measurement
               values with at least one threshold measurement value; and
     4.3           if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold
                   measurement value,
     4         sending said at least one of said converted plurality of downlink measurement values

                                       - 18 -



     4.1           on a control channel
     4.2GSM        to a control node in said GSM communication system.


Der Anspruch 1 nach Hilfsantrag 2 vom 17. November 2015 basiert auf dem Anspruch 1 nach Hauptantrag und konkretisiert darüber hinaus das erste Kommunikationssystem als UMTS-Kommunikationssystem. Er lautet (Änderungen ggü.
dem Anspruch 1 in der Fassung nach Hauptantrag sind gekennzeichnet):


     1         A method for conveying measurement information
     1.1UMTS       from a terminal in a UMTS communication system
     1.2GSM        to a GSM communication system,
               characterized by the steps of:
     2GSM-UMTS      converting a plurality of downlink measurement values
               associated with said UMTS communication system to a plurality of downlink measurement values for said GSM communication system;
     3         comparing said converted plurality of downlink measurement
               values with at least one threshold measurement value; and
     4.3           if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold
                   measurement value,
     4         sending said at least one of said converted plurality of downlink measurement values
     4.1           on a control channel
     4.2GSM        to a control node in said GSM communication system.


Der Anspruch 1 nach Hilfsantrag 3 vom 10. Februar 2017 basiert auf dem Anspruch 1 nach Hauptantrag und beschränkt zudem die mit dem ersten Kommunikationssystem assoziierten Downlink-Messwerte auf RSCP Messwerte. Er lautet
(Änderungen ggü. dem Anspruch 1 in der Fassung nach Hauptantrag sind gekennzeichnet):

                                       - 19 -



     1        A method for conveying measurement information
     1.1          from a terminal in a ﬁrst communication system
     1.2GSM       to a GSM communication system,
              characterized by the steps of:
     2GSM-RSCP     converting a plurality of RSCP downlink measurement
              values associated with said ﬁrst communication system to a
              plurality of downlink measurement values for said GSM communication system;
     3        comparing said converted plurality of downlink measurement
              values with at least one threshold measurement value; and
     4.3          if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold
                  measurement value,
     4        sending said at least one of said converted plurality of downlink measurement values
     4.1          on a control channel
     4.2GSM       to a control node in said GSM communication system.


Der Anspruch 1 nach Hilfsantrag 4 vom 10. Februar 2017 basiert auf dem Anspruch 1 nach Hilfsantrag 3 und beinhaltet zusätzlich die Angabe, dass das Umwandeln einer Vielzahl von mit dem ersten Kommunikationssystem assoziierten
RSCP Downlink-Messwerten in eine Vielzahl von Downlink-Messwerten für das
GSM-Kommunikationssystem        nach     der    Gleichung   „RXLEV   =   RSCP     +
OFFSET(RSCP)“ ausgeführt wird, wobei OFFSET eine Konstante ist. Er lautet
(Änderungen ggü. Anspruch 1 in der Fassung nach Hilfsantrag 3 sind gekennzeichnet):


     1        A method for conveying measurement information
     1.1          from a terminal in a ﬁrst communication system
     1.2GSM       to a GSM communication system,
              characterized by the steps of:

                                       - 20 -



     2GSM-RSCP      converting a plurality of RSCP downlink measurement
               values associated with said ﬁrst communication system to a
               plurality of downlink measurement values for said GSM communication system
     2.1Equ1   by using the following equation: RXLEV = RSCP +
               OFFSET(RSCP), wherein OFFSET is a constant;
     3         comparing said converted plurality of downlink measurement
               values with at least one threshold measurement value; and
     4.3           if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold
                   measurement value,
     4         sending said at least one of said converted plurality of downlink measurement values
     4.1           on a control channel
     4.2GSM        to a control node in said GSM communication system.


Der Anspruch 1 nach Hilfsantrag 5 vom 10. Februar 2017 basiert auf dem
Anspruch 1 nach Hilfsantrag 4, wobei OFFSET nunmehr keine Funktion von
RSCP ist, sondern eine Konstante. Er lautet (Änderungen ggü. dem Anspruch 1 in
der Fassung nach Hilfsantrag 4 sind gekennzeichnet):


     1         A method for conveying measurement information
     1.1           from a terminal in a ﬁrst communication system
     1.2GSM        to a GSM communication system,
               characterized by the steps of:
     2GSM-RSCP      converting a plurality of RSCP downlink measurement
               values associated with said ﬁrst communication system to a
               plurality of downlink measurement values for said GSM communication system
     2.1Equ2   by using the following equation: RXLEV = RSCP +
               OFFSET(RSCP), wherein OFFSET is a constant;

                                        - 21 -



     3           comparing said converted plurality of downlink measurement
                 values with at least one threshold measurement value; and
     4.3            if at least one of said converted plurality of downlink measurement values exceeds a predetermined threshold
                    measurement value,
     4           sending said at least one of said converted plurality of downlink measurement values
     4.1            on a control channel
     4.2GSM         to a control node in said GSM communication system.


4. Der zuständige Fachmann, bei dem es sich um einen Diplom-Ingenieur der
Elektro- oder Nachrichtentechnik mit Universitätsausbildung, mehrjähriger Berufserfahrung und einschlägigen Kenntnissen auf dem Gebiet der Konzeption von
Mobilfunksystemen, insbesondere im Bereich GSM- und UMTS-Netzwerke, handelt, versteht die Angaben in den Ansprüchen wie folgt:


a)       first communication system [being of a type different from the GSM
communication system], UMTS communication system (Merkmale 1.1, 1.1.1Not-GSM, 1.1UMTS):

         Das erste Kommunikationssystem nach Merkmal 1.1 und das GSM-Kommunikationssystem nach Merkmal 1.2GSM unterscheiden sich zumindest in einem technischen Aspekt derart voneinander, dass die im
         Merkmal 2GSM genannte Umwandlung der Messwerte erforderlich wird.
         Insofern versteht der Fachmann das Merkmal 1.1 nach Hauptantrag
         und Hilfsanträgen 3 bis 5 in Sinne des Merkmals 1.1.1Not-GSM gemäß
         Hilfsantrag 1 und schließt somit aus, dass es sich bei dem ersten
         Kommunikationssystem um ein GSM-Kommunikationssystem handelt.
         Merkmal 1.1UMTS gemäß Hilfsantrag 2 definiert das erste Kommunikationssystem als UMTS-Kommunikationssystem.


b)       a plurality of [RSCP] downlink measurement values associated with said
ﬁrst [UMTS] communication system (ein Teil der Merkmale 2GSM, 2GSM-UMTS bzw.

                                       - 22 -



2GSM-RSCP):
      b1)     Unter einer Abwärtsverbindung (downlink) versteht der Fachmann den von einem Knoten eines Kommunikationssystems (z. B. einer UMTS-Basisstation) zu dem Endgerät (terminal) gerichteten Sendepfad. Die mit dem ersten Kommunikationssystem assoziierten
      Messwerte der Abwärtsverbindung (downlink measurement values
      associated with said first communication system) gewinnt das Endgerät durch Empfang und anschließende Auswertung der von einem
      Knoten des ersten Kommunikationssystems ausgesendeten Signale.


      b2)     Unter solchen    Messwerten       versteht   der Fachmann   bei
      Funkkommunikationssystemen neben komplexen Größen wie der
      Bitfehlerrate, die eine Messung über einen längeren Zeitraum erfordern, in erster Linie die von dem Endgerät empfangene Leistung, die
      ein Maß für den Kanalverlust, d. h. für die Entfernung zwischen Sender und Empfänger, darstellt.


      b3)     Bei dem schmalbandigen, TDMA (time divison multiple access)
      und FDMA (frequency division mulitple access) nutzendem GSM-Kommunikationssystem ermittelt das Endgerät die empfangene Leistung durch Auswertung des in einem bestimmten Zeitschlitz (= Zeitspanne) und in einem bestimmten (schmalen) Frequenzbereich, z. B.
      200 kHz, vorliegenden Signals. Da gleichfrequente Störsignale aus
      weiter entfernten Funkzellen (sogenannte Gleichkanalstörer = cochannel interferer) die Messwerte nahezu nicht beeinflussen, lässt
      sich die im GSM-Standard mit RXLEV (received signal level) bezeichnete Empfangsleistung des gewünschten Signals relativ genau bestimmen und sie ist als Maß für die Qualität der GSM-Funkverbindung
      aussagekräftig (vgl. Anlage D3A der Klägerin zu 1 = GSM 05.08
      V6.3.0, Kap. 8 bis 8.1.4, Seiten 20 – 22).

                                - 23 -



b4)   Bei dem breitbandigen, CDMA (code division multiple access)
nutzendem UMTS-Kommunikationssystem gestaltet sich die Ermittlung der Empfangsleistung aufwändiger. Denn bei UMTS werden die
zu sendenden Signale in einer Funkzelle durch Multiplikation einer
festen Mittenfrequenz mit jeweils einem speziellen, nur dem Sender
und dem zugehörigen Empfänger bekannten Code in der Bandbreite
gespreizt (Spreizcode), so dass ihre Energie jeweils auf einen großen
Frequenzbereich von z. B. 5 MHz verteilt ist. Viele unterschiedlich codierte Sendesignale teilen sich somit ggfs. zeitgleich diesen großen
Frequenzbereich. Ein Empfänger empfängt das gesamte Frequenzband mit der Mehrzahl der verschiedenen Sendesignale und extrahiert
dann mittels digitaler Signalverarbeitung das an ihn gerichtete Sendesignal durch Multiplikation mit dem „richtigen“ Code (entspreizen).


Für die Messung der Empfangsleistung hat das zur Folge, dass ein
UMTS-Empfänger zum einen unmittelbar – vergleichbar mit einem
GSM-Empfänger – die Leistung in dem großen Frequenzbereich von
z. B. 5 MHz misst. Diese als RSSI (received signal strength indicator)
bezeichnete Summenleistung setzt sich aus den Empfangsleistungen
der von den verschiedenen UMTS-Basisstationen (= Zellen) und anderen UMTS-Endgeräten ausgesendeten Sendesignalen und der
Rauschleistung in diesem breiten Frequenzbereich zusammen (vgl.
Anlage M&N 7 der Klägerin zu 1 = Anlage NK6 der Klägerin zu 2 = 3G
TS 25.215 V3.0.0 (1999-10), Seite 9, Kap. 5.1.5 „UTRA carrier RSSI“).


Erst nach der „Entspreizung“ des Signalgemischs, d. h. der Wiedergewinnung bzw. Extraktion des gewünschten Signals, kann der Empfänger auch die Empfangsleistung des ihn interessierenden Signals
bestimmen. Dieser Messwert wird in UMTS als RSCP (received signal
code power) bezeichnet (vgl. Anlage M&N 7 der Klägerin zu 1 = Anlage NK6 der Klägerin zu 2 = 3G TS 25.215 V3.0.0 (1999-10), Seite 8,
Kap. 5.1.2 „RSCP“).

                               - 24 -



Bei einem CDMA-System wie UMTS ist es wegen der zeitlichen
Koexistenz des gewünschten Signals mit den störenden Signalen in
einem gemeinsamen Frequenzbereich üblich, neben der Gesamt-Empfangsleistung RSSI in dem breiten Frequenzbereich (z. B. 5 MHz)
und der Empfangsleistung RSCP des gewünschten Signals diese beiden Größen miteinander ins Verhältnis zu setzen, um so eine Aussage
darüber zu erhalten, wie groß das gewünschte Signal im Vergleich zur
Summe aus gewünschtem Signal, Störsignalen und Rauschen ist.
Dieses Verhältnis wird mit Ec/N0 bzw. Ec/I0 (im Streitpatent, Absatz [0014]: „Code Energy-to-Interference Ratio“; Anlage M&N 7 der
Klägerin zu 1 = Anlage NK6 der Klägerin zu 2 = 3G TS 25.215 V3.0.0
(1999-10), Seite 9, Kap. 5.1.7: „CPICH Ec/NO”) bezeichnet. Dabei gilt
Ec/I0 = RSCP/RSSI bzw. in der bei Funksystemen üblichen logarithmischen Darstellung von Leistungen (dBm = Dezibel Milliwatt ist die Einheit des Leistungspegels LP, der das Verhältnis einer Leistung P im
Vergleich zur Bezugsleistung von 1 mW beschreibt: LP = 10 log10(P/1
mW)):


                Ec/I0 [dB] = RSCP[dBm] – RSSI[dBm]


Je größer das gewünschte Signal (RSCP) und je geringer die Summenleistung (kleiner RSSI-Wert) sind, umso höher ist der Ec/I0-Messwert und damit die Empfangsqualität.


Die Ec/I0-Messwerte sind somit als Maß für die Qualität einer UMTS-Funkverbindung noch aussagekräftiger als die RSCP-Messwerte.


Im Lichte der Lehre des Streitpatents versteht der Fachmann daher unter
den „downlink measurement values associated with said first [UMTS] communication system“ nach Merkmal 2GSM bzw. 2GSM-UMTS (Hauptantrag und
Hilfsanträge 1, 2) in erster Linie die genannten UMTS-Messwerte RSCP
und Ec/I0. Nach Merkmal 2GSM-RSCP (Hilfsanträge 3 bis 5) handelt es sich

                                       - 25 -



      konkret um RSCP-Messwerte.


      b5)    Da gemäß den Absätzen [0015] und [0016] der Streitpatentschrift sowohl die umzuwandelnden UMTS-Messwerte als auch die GSM-Messwerte
      in einem lokalen Speicher des Endgeräts gespeichert werden, bevor sie
      von dem Mikroprozessor des Endgeräts ausgelesen, umgewandelt (UMTS-Messwerte) und anschließend miteinander oder mit einem Schwellmesswert verglichen werden, liest der Fachmann mit, dass die im Endgerät gewonnenen zunächst noch analogen Messwerte einer anschließenden
      Quantisierung und damit einer digitalen Kodierung unterworfen werden. Jedoch muss diese Kodierung nicht mit derjenigen übereinstimmen, die für
      eine Übertragung der Messwerte in einem Messwertebericht, z. B. auf dem
      Kontrollkanal SACCH (6 Bit), erforderlich ist.


c)    converting a plurality of [RSCP] downlink measurement values associated
with said ﬁrst [UMTS] communication system to a plurality of downlink measurement values for said GSM communication system (vollständige Merkmale 2GSM,
2GSM-UMTS bzw. 2GSM-RSCP):
      Der Fachmann entnimmt dem Streitpatent die Lehre, dass die Umwandlung der (UMTS-)Downlink-Messwerte des ersten Kommunikationssystem in Downlink-Messwerte für das GSM-Kommunikationssystem so erfolgt, dass nicht nur eine Übertragung der umgewandelten UMTS-Messwerte über einen Steuerkanal nach Merkmal 4.1 an
      einen Steuerknoten des GSM-Kommunikationssystems nach Merkmal
      4.2GSM möglich ist, sondern dass auch eine Vergleichbarkeit der umgewandelten UMTS-Messwerte mit den originären GSM-Messwerten
      gegeben ist und so eine systemübergreifende Handover-Entscheidung
      durch den GSM BSC getroffen werden kann. Die originären GSM-Messwerte und die für das GSM-Kommunikationssystem umgewandelten UMTS-Messwerte müssen jeweils als ein Maß für die Qualität
      der zugehörigen Funkverbindung geeignet sein. Dem Fachmann war
      zum Prioritätsdatum bekannt, dass die beiden Kommunikationssys-

                                         - 26 -



      teme deutliche Unterschiede aufweisen und daher ein unmittelbarer
      Qualitätsvergleich zwischen einer GSM-Verbindung und einer UMTS-Verbindung schwierig ist. Dennoch war dem Fachmann bewusst, dass
      z. B. die Stärke des jeweiligen Empfangssignals, die in erster Linie von
      der Sendeleistung und der Entfernung zwischen Sender und Empfänger (Kanalverlust) abhängt, bei beiden Funksystemen bestimmbar ist
      und die Verbindungsqualität maßgeblich beeinflusst.


d)    comparing said converted plurality of downlink measurement values with at
least one threshold measurement value (Merkmale 3):
      Unter dem hier genannten Vergleich der für das GSM-Kommunikationssystem umgewandelten Downlink-Messwerte des ersten Kommunikationssystems mit mindestens einem Schwellmesswert versteht der
      Fachmann eine Prüfung jedes einzelnen der umgewandelten Messwerte, ob dieser größer oder kleiner (gleich) als der oder die Schwellenmesswerte sind. Wie vorstehend unter Gliederungspunkt b5 ausgeführt, liest der Fachmann mit, dass der oder die Schwellmesswerte
      in Form eines digitalen Wertes im Endgerät vorliegen.


e)    by using the following equation:
RXLEV = RSCP + OFFSET(RSCP) [RXLEV = RSCP + OFFSET],
wherein OFFSET is a constant (Merkmale 2.1Equ1 bzw. 2.1Equ2):
      e1)   Dieses Merkmal gibt in Form einer mathematischen Gleichung
      an, wie die RSCP-Downlink-Messwerte des ersten [UMTS-] Kommunikationssystems in RXLEV-Downlink-Messwerte des GSM-Kommunikationssystems umzuwandeln sind. Wie ausgeführt versteht der
      Fachmann unter RSCP (received signal code power) solche Downlink-Messwerte, die der UMTS-Teil des Endgeräts nach Empfang des
      breiten Frequenzbereichs (z. B. 5 MHz) und Entspreizung mittels eines ihm bekannten Kodes als Leistung des gewünschten Empfangssignals ermittelt hat. Dabei entnimmt der Fachmann der Gleichungsstruktur (Addition eines Offset-Wertes), dass es sich bei den in der

                                 - 27 -



Gleichung angegebenen Termen (RXLEV, RSCP, OFFSET) fachüblich jeweils um logarithmierte Leistungsangaben handelt, die bei Funksystemen typisch in der Einheit dBm (Dezibel Milliwatt) angegeben ist.
Da die Umwandlung der Messwerte mittels der Gleichung vom Endgerät bzw. fachnotorisch von dessen Digitalteil (zentraler Mikroprozessor, Signalprozessor oder Digitalteil eines sogenannten Mixed-Signal-Bausteins) vorgenommen wird, müssen die RSCP-Werte als quantisierte, d. h. digital kodierte Werte vorliegen, zu denen dann ein ebenfalls digital kodierter Offset-Wert addiert wird. Die RXLEV (received level)-Werte sind für den Fachmann solche, die die Empfangsleistung
eines GSM-Signals in dBm angeben. Auch hierbei handelt es sich um
digital codierte Werte, wobei die Kodierung im Endgerät vor der Übertragung über den Steuerkanal geändert werden kann. Bei der Umwandlung der Messwerte gemäß der Gleichung könnten die Messwerte RSCP, OFFSET und damit auch das Ergebnis RXLEV mit einer
Auflösung von z. B. 8 Bit vorliegen, während zur Übertragung der umgewandelten Messwerte z. B. nur 6 Bits vorliegen.


e2)   Die Angabe OFFSET(RSCP) nach Merkmal 2.1Equ1 versteht der
zuständige Fachmann so, dass die Größe OFFSET eine insofern beliebige Funktion der RSCP-Messwerte ist, als dass eine echte Abhängigkeit von der Größe RSCP besteht. Insofern steht die Angabe, dass
OFFSET eine Konstante ist, im Widerspruch zu der Angabe
„OFFSET(RSCP)“. Dabei wird darauf hingewiesen, dass es in den
Naturwissenschaften und insbesondere in der Technik fachüblich ist,
eine Schreibweise mit einer Variablen in Klammer nur dann zu verwenden, wenn damit eine „echte“ funktionale Abhängigkeit gemeint ist.
Beim Einsetzten einer Konstante als Funktionsargument, welche die
Funktion insgesamt zur Konstanten macht, wäre es üblich, nur ihren
Wert anzugeben oder eben den zughörigen Platzhalter, der dann aber
ein Parameter wäre.

                                        - 28 -



f)    if at least one of said converted plurality of downlink measurement values
exceeds a predetermined threshold measurement value (Merkmal 4.3):
      Gemäß Mermal 4.3 ist zumindest einer der im Merkmal 3 genannten
      Schwellmesswerte vorbestimmt (predetermined). Aus dem Streitpatent
      ist nicht ersichtlich, ob sich der hier genannte Schwellmesswert aufgrund seiner Vorbestimmtheit von den in Merkmal 3 angegebenen
      Schwellmesswerten unterscheidet. Nach dem nicht beschränkenden
      Ausführungsbespiel (Absatz [0016], zweite Alternative) handelt es sich
      um einen vorbestimmten (GSM-)Signalstärkeschwellwert, wobei der
      Fachmann diesen im Sinne der mit RXLEV (receive level) bezeichneten Empfangsleistung versteht.


g)    sending said at least one of said converted plurality of downlink measurement values on a control channel to a control node in said GSM communication
system. (Merkmale 4, 4.1 und 4.2GSM):
      g1)   Hierunter versteht der Fachmann, dass die umgewandelten
      Downlink-Messwerte des ersten Kommunikationssystems, welche das
      in Merkmal 4.3 genannte Kriterium erfüllen, im Uplink von dem Endgerät an das GSM-System übertragen werden. Dem Fachmann sind im
      Uplink der FACCH (fast associated control channel), der SACCH (slow
      associated control channel) und der SDCCH (standalone dedicated
      control channel) als Steuerkanäle bekannt, die für eine solche teilnehmerbezogene Informationsübertragung grundsätzlich geeignet
      sind (vgl. Anlage CNK12 der Beklagten = SAUTER, M.: Grundkurs
      Mobile Kommunikationssysteme, Seiten 40 und 41).


      g2)   Unter einem Steuerknoten des GSM-Kommunikationssystems
      versteht der Fachmann die GSM-Basisstation BTS (Base Transceiver
      Station), die die im Uplink übertragenen Messwerte empfängt, oder
      den GSM BSC (Base Station Controller), an den die Basisstation BTS
      die Messwerte weiterleitet und der die Handover-Entscheidung trifft
      oder zumindest vorbereitet.

                                       - 29 -



      g3)     Ob neben den umgewandelten UMTS-Messwerten, die größer
      als der vorbestimmte Schwellmesswert sind, ggfs. auch noch originäre
      GSM-Messwerte in dem GSM-Messwertebericht übertragen werden,
      lässt sich dem Anspruch 1 nicht unmittelbar entnehmen. Zur Überzeugung des Senats liest der Fachmann dies jedoch vor dem geschilderten Hintergrund des Streitpatents mit, insbesondere angesichts der
      anzustrebenden möglichst geringen Änderung des bestehenden GSM-Standards. Dem Fachmann ist bewusst, das z. B. im SACCH nach
      GSM-Spezifikation nur die RXLEV-Werte der eigenen und der sechs
      benachbarten Zellen übertragen werden können (vgl. Anlage D3A der
      Klägerin zu 1 = GSM 05.08 V 6.3.0 (1998-11), Seite 24, Kap. 8.4.1)
      und ausreichend viele dieser originären GSM-Werte übertragen werden sollten, damit ein ggfs. notwendiges GSM-internes Handover
      durchgeführt werden kann. Ein solcher Handover-Vorgang könnte
      nämlich auch dann erforderlich sein, wenn zwar genügend „gute“
      UMTS-Messwerte übertragen werden und damit grundsätzlich ein
      Handover von GSM zu UMTS möglich wäre, jedoch aus anderen
      Gründen, z. B. Überlastung des UMTS-Netzes, nicht erwünscht ist.




            II. Zur beschränkten Verteidigung nach dem Hauptantrag


Es kann dahingestellt bleiben, ob eine beschränkte Verteidigung des Streitpatents
in der Fassung des Hauptantrags schon mangels Zulässigkeit, insbesondere, wie
die Klägerin zu 2 geltend macht, wegen einer unzulässigen Erweiterung nach
Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ, ausscheidet, denn der Fassung des Streitpatents nach dem Hauptantrag steht auf jeden
Fall der Nichtigkeitsgrund mangelnder Ausführbarkeit (Art II § 6 Abs. 1 Nr. 2 Int-PatÜG i. V. m. Art 138 Abs. 1 Buchst. b) EPÜ) entgegen.


Wie zum Gegenstand des Streitpatents und zur Auslegung dargelegt, versteht der
Fachmann unter der Umwandlung der (UMTS-)Downlink-Messwerte des ersten

                                       - 30 -



Kommunikationssystems in Downlink-Messwerte des GSM-Kommunikationssystems nach dem Merkmal 2GSM unter Beachtung der Lehre des Streitpatents die
Umwandlung der UMTS-Downlink-Messwerte Ec/I0 bzw. RSCP in GSM-Downlink-Signalstärkemesswerte RXLEV.


a)    Die im Streitpatent genannte Umwandlung der UMTS-Messgröße Ec/I0 in
einen GSM-RXLEV-Messwert (vgl. Streitpatent, Absätze [0014], [0015]; Anspruch 4, Figur 2, Schritt 104) ist nicht so deutlich und vollständig offenbart, dass
ein Fachmann sie ausführen kann.


Wie zur Auslegung unter Gliederungspunkt b) ausgeführt (Ec/N0 = RSCP/RSSI
bzw. Ec/N0 [dB] = RSCP [dBm] – RSSI [dBm]) ist der Ec/No-Wert über den Zählerterm RSCP zwar direkt proportional zur Empfangsleistung des gewünschten entspreizten Signals, jedoch geht diese Empfangsleistung auch in den Nennerterm
RSSI ein, der die Summe des gewünschten Signals, der Störsignale und der
Rauschanteile in dem breitbandigen UMTS-Frequenzbereich darstellt. Zudem beeinflussen alle UMTS-Störsignale in dem betrachteten Frequenzbereich den Ec/No-Wert, so dass der Fachmann bei der Suche nach einer geeigneten Vorschrift für
die Umwandlung der Ec/No-Messwerte des UMTS-Kommunikationssystems in
Messwerte für das GSM-Kommunikationssystem, etwa Signalstärkewerte RXLEV,
in erfinderischer Weise tätig werden muss.


Dem steht der Einwand der Beklagten nicht entgegen, den diese auf das UMTS-Standard-Dokument ETSI TS 125 133 V5.17.0 (2005-12) (Anlage CNK9a der Beklagten) gestützt hat. Die Beklagte hat hierzu ausgeführt, Tabelle 9.9 (Seite 61)
dieses Dokuments zeige, wie der Wertebereich des Ec/I0-Werts von -24 dB bis 0
dB in 0.5 dB-Schritten auf die Werte 00 bis 49 linear abgebildet werde. Da das
Streitpatent mit der Gleichung RXLEV = RSCP + OFFSET(RSCP) eine lineare
Umwandlungsvorschrift der RSCP-Werte in RXLEV-Werte enthalte, sei es für den
Fachmann naheliegend, auch die Ec/I0-Wert entsprechend abzubilden, mithin in
der Form RXLEV = Ec/I0 + OFFSET(Ec/I0). Die Bestimmung eines geeigneten Offset-Wertes sei für Fachmann möglich, weil er den (Ziel-)Wertebereich der RXLEV-

                                      - 31 -



Werte kenne.


Diese Argumentation geht aus mehreren Gründen fehl. Zunächst bezieht sich die
Beklagte diesbezüglich auf zwei nachveröffentliche Spezifikationen (neben dem
vorstehend genannten UMTS-Standard nach Anlage CNK9a noch auf die GSM-Spezifikation 3GPP TS 45.008 V5.22.0 (2006-04), eingereicht als Anlage CNK9),
die erst im Dezember 2005 bzw. April 2006, mithin mindestens 6 Jahre nach dem
Prioritätsdatum (November 1999), veröffentlicht wurden. Somit ist nicht davon
auszugehen, dass die dort beschriebenen Verfahren bereits am Prioritätszeitpunkt
zum Fachwissen zählten.


Aber selbst unter der Annahme, zum Prioritätsdatum sei für das in der Definitionsphase befindliche UMTS-System zumindest der Wertebereich der Größe Ec/I0 in
groben Zügen bekannt gewesen, ergibt sich daraus für den Fachmann noch nicht
in naheliegender Weise ein Umwandlungsvorschrift in GSM-RXLEV-Werte, die
eine sinnvolle Vergleichbarkeit der Messwerte ermöglichen würde. Wie man den
nachveröffentlichten UMTS- und GSM-Spezifikationen entnehmen kann (vgl. Anlage CNK9 der Beklagten = 3GPP TS 145 008 V5.22.0 (2006-04), Kap. 8.1.5.1,
Seite 33; Anlage CNK9a der Beklagten = TS 125 133 V5.17.0 (2005-12), Tabelle
9.9, Seite 61) ist die Abbildung der Ec/I0-Werte auf die RXLEV-Werte komplex:
Zum einen werden die Ec/I0-Werte in 0.5 dB- statt in 1 dB-Schritten kodiert und
zum anderen wird der zur Verfügung stehende Bereich (0 bis 63) nur teilweise (0
bis 49) ausgenutzt, um die Ec/I0-Werte in RXLEV-Werte umzuwandeln, die an den
GSM BSC berichtet werden. Eine solche komplexe Abbildungsvorschrift war ersichtlich für den Fachmann am Prioritätsdatum nicht aufzufinden, ohne erfinderisch tätig werden zu müssen.


b)      Die im Streitpatent genannte Umwandlung der UMTS-Messgröße RSCP in
einen    GSM-RXLEV-Wert      gemäß     der     Gleichung   RXLEV   =   RSCP     +
OFFSET(RSCP) (vgl. Streitpatent, Absatz [0015]; Anspruch 4; Figur 2, Schritt 104)
ist nicht so deutlich und vollständig offenbart, dass ein Fachmann sie ausführen
kann. Der Streitpatentschrift ist im Absatz [0015] folgendes zu der Umwandlung

                                      - 32 -



von RSCP-Messwerten in RXLEV-Messwerte zu entnehmen:


      “For example, the UMTS RSCP measurement information retrieved by
      the MS 22 can be converted to appropriate GSM signal strength measurement information (RXLEV) by using the following equation:
                   RXLEV = RSCP + OFFSET(RSCP)             (1)
      where RXLEV represents GSM signal strength measurements [e.g., -
      110,-47] in dBm, RSCP represents UMTS signal strength measurements in dBm, and OFFSET represents offset values that can be constant or variable with RSCP.”


b1)    Hier   besteht    ein    Offenbarungsmangel     bezüglich     des   Terms
„OFFSET(RSCP) … variable with RSCP“, also der Frage, wie die unbekannte
funktionale Abhängigkeit des OFFSET-Wertes von RSCP bestimmt werden
könnte.


Die Beklagte hat in der mündlichen Verhandlung ausgeführt, der Fachmann verstehe den Term OFFSET(RSCP) im Lichte der Beschreibung (vgl. Seite 3,
Zeile 57: OFFSET represents offset values that can be constant or variable with
RSCP) so, dass die Größe OFFSET für bestimmte Bereiche (= Intervalle) von
RSCP zwar unterschiedliche, aber in diesen Bereichen jeweils konstante Werte
annehmen könne („constant … with RSCP“). Die Bestimmung dieser Mehrzahl
von konstanten OFFSET-Werten sei für den Fachmann möglich, ohne dass er
hierzu erfinderisch tätig werden müsse.


Dieser Sichtweise kann sich der Senat nicht anschließen. Der Formulierung
OFFSET(RSCP) in der Gleichung (1) (Streitpatentschrift, Seite 3, Zeile 55) in
Kombination mit der oben genannten Beschreibung (constant or variable with
RSCP) entnimmt der Fachmann zwei alternative Möglichkeiten:


Im ersten Fall nimmt die Größe OFFSET einen konstanten Wert an, d. h. sie ist
unabhängig von dem Messwert RSCP. Im zweiten Fall ist OFFSET eine beliebige,

                                      - 33 -



jedoch nicht konstante Funktion des Messwerts RSCP. Das Streitpatent macht
zum zweiten Fall keinerlei weitere Angaben.


Den ersten Fall (OFFSET ist eine Konstante) sieht der Senat zwar als ausführbar
offenbart an (siehe die folgenden Ausführungen zum Hilfsantrag 5). Der Einwand
der Beklagten, das Streitpatent offenbare mit der Gleichung RXLEV = RSCP +
OFFSET, wobei eine OFFSET eine Konstante ist, zumindest eine ausführbare
Ausführungsart der Erfindung, so dass das Merkmal 2 GSM insgesamt so deutlich
und vollständig offenbart sei, dass es ausführbar wäre, greift nicht durch. Mangels
näherer Angaben im Anspruch 1 sucht der Fachmann im Streitpatent nach Möglichkeiten der Umwandlung der UMTS-Messwerte, mit denen das Ziel, die Herstellung einer hinreichend guten Vergleichbarkeit der umgewandelten UMTS-Messwerte mit den originären GSM-Signalstärkewerten, erreicht werden kann.


Als allgemeinste Form der technischen Lehre, durch die das der Erfindung zugrundeliegende Problem gelöst wird, erachtet der Senat die Umwandlung der
UMTS-Messwerte RSCP in GSM-Messwerte RXLEV unter Berücksichtigung eines
konstanten Offsets (siehe die noch folgenden Ausführungen zum Merkmal 2.1 Equ2
nach Hilfsantrag 5). Der Gegenstand des Anspruchs 1 nach Hauptantrag geht jedoch hierüber hinaus und genügt damit dem Erfordernis einer ausführbaren Offenbarung nicht (vgl. BGH, Beschluss vom 11. September 2013, X ZB 8/12,
GRUR 2013, 1210 - Dipeptidyl-Peptidase-Inhibitoren).




II. Zur beschränkten Verteidigung des Streitpatents nach den Hilfsanträgen 1
                                      bis 3


Die Fassung des Anspruchs 1 nach Hilfsantrag 1 weist gegenüber der Fassung
nach Hauptantrag die zusätzliche Anweisung auf, dass das erste Kommunikationssystem nicht als GSM-Kommunikationssystem ausgebildet ist:
     1.1.1Not-GSM the first communication system being of a type different
                  from the GSM communication system and

                                     - 34 -



Die Fassung des Anspruchs 1 nach Hilfsantrag 2 unterscheidet sich von der Fassung nach Hauptantrag durch die zusätzliche Anweisung, dass das erste Kommunikationssystem als UMTS-Kommunikationssystem ausgebildet ist:
     1.1UMTS      from a terminal in a UMTS communication system
     …
     2GSM-UMTS      converting a plurality of downlink measurement values
               associated with said UMTS communication system to a plurality of downlink measurement values for said GSM communication system;


Die Fassung des Anspruchs 1 nach Hilfsantrag 3 enthält gegenüber der Fassung
nach Hauptantrag die zusätzliche Anweisung, dass es sich bei den mit dem ersten
Kommunikationssystem assoziierten Downlink-Messwerten um RSCP-Messwerte
handelt:
     2GSM-RSCP      converting a plurality of RSCP downlink measurement
               values associated with said ﬁrst communication system to a
               plurality of downlink measurement values for said GSM communication system;


Wie beim Hauptantrag kann auch bei den Fassungen des Streitpatents nach den
Hilfsanträgen 1 bis 3 dahingestellt bleiben, ob eine beschränkte Verteidigung des
Streitpatents mit einer dieser Fassungen schon mangels Zulässigkeit, insbesondere infolge einer, wie die Klägerin zu 2 geltend macht, unzulässigen Erweiterung
ausscheidet. Denn der von den Klägerinnen geltend gemachte Nichtigkeitsgrund
der nicht ausführbaren Offenbarung liegt wie beim Hauptantrag auf jeden Fall
auch bei den Fassungen des Streitpatents nach den Hilfsanträgen 1 bis 3 vor.


Hinsichtlich des Hilfsantrags 1 ergibt sich dies schon daraus, dass sich der Anspruch 1 nach Hilfsantrag 1 im Hinblick auf das diesbezüglich relevante Merkmal
2GSM nicht vom Anspruch 1 nach Hauptantrag unterscheidet.

                                       - 35 -



Gleiches gilt auch für den Anspruch 1 nach Hilfsantrag 2. Dass dieser im Unterschied zum Hauptantrag im Hinblick auf das diesbezüglich relevante Merkmal
2GSM-UMTS nunmehr vorsieht, dass das erste Kommunikationssystem als UMTS-Kommunikationssystem ausgebildet ist, ändert nichts daran, dass die nicht ausführbare Offenbarung der Umwandlung der Ec/I0- bzw. der RSCP-Downlink-Messwerte (mit einem von RSCP funktional abhängigen OFFSET) des UMTS-Kommunikationssystem in Downlink-Messwerte für das GSM-Kommunikationssystem
auch beim Hilfsantrag 2 besteht.


Der Anspruch 1 nach Hilfsantrag 3 schließlich unterscheidet sich im Hinblick auf
das diesbezüglich relevante Merkmal 2GSM-RSCP nur dadurch vom Anspruch 1 nach
Hauptantrag, dass die mit dem ersten Kommunikationssystem assoziierten Downlink-Messwerte als RSCP-Messwerte ausgestaltet sind. Durch die Konkretisierung
auf die Umwandlung von RSCP-Downlink-Messwerten im Merkmal 2GSM-RSCP ist
zwar die Problematik hinsichtlich der unzureichenden Offenbarung der Umwandlung der Ec/I0-Werte in RXLEV-Werte nicht mehr gegeben, die der unzureichenden
Offenbarung der Umwandlung der RSCP-Werte mit einem von RSCP funktional
abhängigen OFFSET bleibt jedoch bestehen, vgl. die obigen Ausführungen im
Abschnitt b1) zum Gegenstand des Anspruchs 1 nach Hauptantrag.




 III.      Zur beschränkten Verteidigung des Streitpatents nach Hilfsantrag 4


Die Fassung des Anspruchs 1 nach Hilfsantrag 4 konkretisiert gegenüber der Fassung nach Hilfsantrag 3 die Umwandlung der RSCP-Messwerte:
        2.1Equ1   by using the following equation: RXLEV = RSCP +
                  OFFSET(RSCP), wherein OFFSET is a constant;


Auch hier kann dahingestellt bleiben, ob der Fassung von Anspruch 1 des Streitpatents nach Hilfsantrag 4 bereits der von der Klägerin zu 2 geltend gemachte
Nichtigkeits der unzulässigen Erweiterung (Art II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m.
Art 138 Abs. 1 Buchst. c) EPÜ) entgegensteht.

                                        - 36 -



Denn jedenfalls genügt die Fassung von Anspruch 1 des Streitpatents nach diesem Hilfsantrag entgegen der Auffassung der Beklagten nicht den Anforderungen
des Art. 84 EPÜ, sodass das Streitpatent mit Hilfsantrag 4 nicht in zulässiger
Weise verteidigt werden kann.


Bei der Formulierung beschränkter Patentansprüche im Patentnichtigkeitsverfahren ist das Gebot der Deutlichkeit (Klarheit), wie es in Art. 84 EPÜ niedergelegt ist,
zu beachten (vgl. BGH, Urteil vom 18. März 2010, Xa ZR 54/06, GRUR 2010, 709
- Proxyserversystem, Rdn: 55 und Leitsatz).


Diese Anforderung erfüllt der Anspruch 1 nach Hilfsantrag 4 nicht, denn der angesprochene Fachmann liest den im Anspruch enthaltenen Term OFFSET(RSCP) –
wie zur Auslegung bereits dargelegt – in der Weise, dass eine echte Abhängigkeit
der Größe OFFSET von der Größe RSCP vorliegt. Damit ist aber der Fall
OFFSET = const. ausgeschlossen, denn einer Konstante fehlt die vorgenannte
Abhängigkeit. Damit ergibt sich jedoch ein Widerspruch zu der weiteren Angabe
im Anspruch „wherein OFFSET is a constant“, so dass im Merkmal 2.1Equ1 nicht
deutlich angegeben ist, für welchen Gegenstand Schutz begehrt wird.




   IV. Zur beschränkten Verteidigung des Streitpatents nach Hilfsantrag 5


Demgegenüber erweisen sich die Klagen als unbegründet, soweit sie sich auch
gegen die beschränkte Verteidigung des Streitpatents nach Hilfsantrag 5 richten.
Denn mit dieser zulässigen Fassung kann die Beklagte das Streitpatent beschränkt verteidigen, da ihr keine Nichtigkeitsgründe entgegenstehen.


Die Fassung des Anspruchs 1 nach Hilfsantrag 5 konkretisiert gegenüber der Fassung nach Hilfsantrag 3 die Umwandlung der RSCP-Messwerte:
     2.1Equ2   by using the following equation: RXLEV = RSCP + OFFSET,
               wherein OFFSET is a constant;

                                       - 37 -



1.    Unzulässige Erweiterung (Art II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138
Abs. 1 Buchst. c) EPÜ)


Entgegen der Ansicht der Klägerin zu 2 steht der beschränkten Verteidigung des
Streitpatents in der Fassung nach Hilfsantrag 5 nicht der Nichtigkeitsgrund der
unzulässigen Erweiterung nach Art II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art: 138
Abs. 1 Buchst. c) EPÜ entgegen.


Denn das zusätzliche Merkmal 2.1Equ2 ist ursprungsoffenbart (vgl. Seite 5, Zeilen 7
bis 13 der WO 01/37602 A1). Dort heißt es
      “For example, the UMTS RSCP measurement information retrieved by
      the MS 22 can be converted to appropriate GSM signal strength
      measurement infonnation (RXLEV) by using the following equation:
                    RXLEV = RSCP + OFFSET(RSCP),            (1)
      where RXLEV represents GSM signal strength measurements [e.g., -
      110,-47] in dBm, RSCP represents UMTS signal strength measurements in dBm, and OFFSET represents offset values that can be constant or variable with RSCP.”
Für den Fall “OFFSET represent offset values that can be constant” lässt sich die
Gleichung (1) vereinfachen zu
                            RXLEV = RSCP + OFFSET,
so dass diese Form in Kombination mit der Angabe „wherein OFFSET is a
constant“ als ursprünglich offenbart anzusehen ist.


Die Klägerinnen haben hiergegen eingewandt, die oben genannte ursprüngliche
Offenbarung sei als „wherein OFFSET represents offset values that can be
constant … with RSCP“ zu lesen. Damit sei auch für diesen Fall eine Abhängigkeit
von RSCP, z. B. im Sinne einer nur bereichsweisen Konstanz der Größe OFFSET,
ursprünglich offenbart. Die Änderung von „OFFSET(RSCP)“ zu „OFFSET“ würde
daher über den Gegenstand der Anmeldung in der ursprünglichen Fassung hinausgehen.

                                      - 38 -



Dem kann nicht zugestimmt werden. Für den Fachmann steht außer Frage, dass
der zitierten Textpassage der ursprünglichen Anmeldung unmittelbar und eindeutig zwei alternative Fälle: Zum einen „RXLEV = RSCP + OFFSET … where …
OFFSET represents offset values that can be constant”, und zum anderen
„RXLEV = RSCP + OFFSET(RSCP) … where OFFSET represents offset values
that can be … variable with RSCP”.


Weiter haben den Klägerinnen eingewandt, dass wegen der fehlenden Aufnahme
der Einheit „dBm“ für die RXLEV- und die RSCP-Werte im Merkmal 2.1Equ2 eine
unzulässige Erweiterung vorliege. Denn das Merkmal 2.1Equ2 umfasse auch die
Variante, dass es sich jeweils um Bitwerte handele, was ursprünglich nicht offenbart sei. Dem kann ebenfalls nicht zugestimmt werden. Wir zur Auslegung im Abschnitt e1) ausgeführt, versteht der Fachmann die Gleichung nach Merkmal
2.1Equ2 ohnehin so, dass die ursprünglich analogen Messwerte RSCP im Endgerät digitalisiert, d. h. in Bitwerte umgewandelt werden und dann ein ebenfalls als
digitaler Wert vorliegender Offset-Wert, der einem bestimmten analogen dB-Wert
entspricht, addiert wird, wodurch sich ein neuer Bitwert als Repräsentant eines
RXLEV-dBm-Wertes ergibt.


2.    Zulässigkeit nach Artikel 84 EPÜ


Der beschränkten Verteidigung des Streitpatents mit Hilfsantrag 5 steht anders als
bei Hilfsantrag 4 auch nicht Art. 84 EPÜ entgegen.


Die zum Hilfsantrag 4 aufgezeigten Mängel im Hinblick auf die Deutlichkeit (Klarheit) des Merkmal 2Equ1 liegen beim Merkmal 2Equ2 nicht vor, denn diese Fassung
ist insofern widerspruchsfrei, als dass die Größe OFFSET einen konstanten Wert
aufweist.


Der Einwand der Klägerinnen, die im Merkmal 2Equ2 angegebene Gleichung lasse
nicht klar erkennen, ob es sich bei den Größen RXLEV, RSCP und Offset um Bitwerte oder dBm-Werte handele, greift ebenfalls nicht durch. Wie bereits dargelegt,

                                     - 39 -



entnimmt der Fachmann diesem Merkmal im Lichte der Lehre des Streitpatents,
dass es sich bei den RSCP-Werten um Bitwerte handelt, die aus ursprünglich
analogen Leistungsmesswerten durch die Verarbeitungsschritte Normierung (d. h.
Teilen des Leistungswerte durch 1 mW), Logarithmierung und nachfolgend digitale
Kodierung entstanden sind.


3.     Ausführbare Offenbarung (Art II § 6 Abs. 1 Nr. 2 IntPatÜG i. V. m.
Art: 138 Abs. 1 Buchst. b) EPÜ)


Der von den Klägerinnen geltend gemachte Nichtigkeitsgrund der nicht ausführbaren Offenbarung liegt beim Hilfsantrag 5 nicht vor, denn der Anspruch 1 nach
Hilfsantrag 5 schränkt die Umwandlung der RSCP-Messwerte in die RXLEV-Messwerte auf den Fall ein, dass die Größe OFFSET eine Konstante ist.


Wie zur Auslegung des Merkmals 2GSM (2GSM-UMTS, 2GSM-RSCP) erläutert, sind sowohl die Messgröße RSCP in UMTS als auch die Messgröße RXLEV in GSM ein
Maß für die jeweilige Empfangsleistung auf einem Kanal und damit automatisch
(bei jeweils bekannter Sendeleistung der Basisstation) ein Maß für den sogenannten Kanalverlust. Damit sind – vereinfacht ausgedrückt und Effekte wie
Mehrwegeausbreitung etc. vernachlässigend – beide Größen ein Maß für die
Entfernung zwischen Sender (im hier interessierenden Downlink-Fall die Basisstation) und Empfänger (= Endgerät).


Dabei ist zu beachten, dass die Empfänger in Mobilfunksystemen einen sehr großen „Dynamikbereich“ verarbeiten müssen (und können, z. B. bei GSM von ca.
-110 dBm entsprechend 10 Femtowatt (= 10-14 Watt) bis ca. +30 dBm entsprechend 1 Watt; d. h. die untere und die obere Grenze der verarbeitbaren Signalleistungen unterscheidet sich durch den Faktor 1014). Dementsprechend stark variiert der Kanalverlust.


Angesichts dieses sehr großen Bereichs von möglichen Eingangsleistungen fallen
andere systemabhängige Faktoren, wie unterschiedlich große Sendeleistungen

                                      - 40 -



der UMTS- und GSM-Basisstationen oder unterschiedliche Anforderungen an das
notwendige minimale Signal-zu-Rauschverhältnis nicht so sehr ins Gewicht bzw.
sie können mit einem geeignet gewählten Offset-Wert von einigen dBm zwischen
RXLEV und RSCP berücksichtigt werden.


Da solche Faktoren dem Fachmann zum Prioritätszeitpunkt bekannt waren,
konnte er bereits aufgrund theoretischer Überlegungen einen sinnvollen Wert der
konstanten Größe OFFSET in der Gleichung nach Merkmal 2Equ2 zwischen
RXLEV und RSCP berechnen und/oder mittels einer überschaubaren Anzahl von
Versuchen ermitteln, um ähnliche Empfangsqualitäten im Sinne von z. B. einer
bestimmten Bitfehlerrate zu erhalten. Dabei ist – worauf bereits oben bei der Darstellung des Erfindungsgegenstandes hingewiesen wurde – zu berücksichtigen,
dass es dem Streitpatent nicht darum geht, sofort zu dem „besten“ Netz zu wechseln, sondern darum, hinreichend „gute“ UMTS-Messwerte so in GSM-Messwerte
umzuwandeln, dass sie nach der Umwandlung mit originären GSM-Messwerten
zumindest grob vergleichbar sind. Diese grobe Vergleichbarkeit kommt im Streitpatent z. B. in den Formulierungen „convert … into some adequate GSM signal
strength“ (Figur 2, Schritt 104), „the MS 22 converts the retrieved UMTS … RSCP
measurement information to appropriate GSM signal strength information, which
can be used by the GSM BSC 14 for making handover decisions.“ (Absatz [0015])
und “MS 22 then retrieves a predetermined number … of the “best” measurement
values … to be reported in a measurememt report to the GSM BSC” (Absatz [0016]) zum Ausdruck.


Nach alledem ist festzustellen, dass die Messgröße RSCP im UMTS-System zumindest dann näherungsweise mit der Messgröße RXLEV im GSM-System vergleichbar ist, wenn die Einflüsse von Störsignalen bei UMTS vernachlässigt werden. In diesem Fall können die Unterschiede zwischen RSCP und RXLEV, die
z. B. in der unterschiedlichen Anforderung an das Signal-zu-Rausch-Verhältnis
begründet sind, durch einen konstanten, leicht zu ermittelnden Offset von typischerweise einigen wenigen dBm berücksichtigt werden.

                                        - 41 -



Der Einwand der Klägerinnen, zum Prioritätszeitpunkt des Streitpatents sei die
Umwandlung der UMTS-Messwerte in GSM-Messwerte ein ungelöstes Problem
gewesen, welches auch vom Streitpatent nicht gelöst werde, greift nicht durch.
Gerade der von den Klägerinnen in der mündlichen Verhandlung aufgegriffene
Bericht (Anlage M&N 9A der Klägerin zu 1 = „Approved Report oft he TSG-RAN
AdHoc meeting on RRM (Torino, Italy, 9-11 February 2000)“ RPA000064 von
Hans van der Veen, ETSI Mobile Competence Centre) sagt zu dem Nokia-Vorschlag „RPA000055 Flexible Mapping Function to Compare GSM and UMTS
Measurements“ lediglich aus, dass eine Formel gefunden werden sollte, die einen
Vergleich von GSM und UMTS ermöglicht, wobei eine solche Formel wegen der
nicht sehr großen Genauigkeiten der GSM- und UMTS-Messwerte problematisch
sein könnte (vgl. Seite 13). Diese Schlussfolgerung macht lediglich deutlich, dass
– im Gegensatz zum Streitpatent – nicht erkannt wurde, dass es auf eine sehr
große Genauigkeit bei dem Vergleich der Messwerte nicht ankommt.


4.    Patentfähigkeit   (Art II   §6   Abs. 1    Nr. 1   IntPatÜG   i. V. m.   Art. 138
Abs. 1 Buchst. a), Art. 52 ff. EPÜ)


Der Gegenstand des Anspruchs 1 nach dem Hilfsantrag 5 gilt als neu gegenüber
dem im Verfahren befindlichen Stand der Technik und beruht gegenüber diesem
auch auf einer erfinderischen Tätigkeit.


4.1     Druckschrift E1 (Tdoc SMG2 1145/99), zu der die Klägerinnen in der
mündlichen Verhandlung allein noch weitere Ausführungen gemacht haben, steht
der Fassung des Streitpatents nach Hilfsantrag 5 weder neuheitsschädlich entgegen, noch vermag sie die erfinderische Tätigkeit in Frage zu stellen.


Die Druckschrift E1, bei der es sich um einen schriftlichen Beitrag der Firma Ericsson für ein Treffen der ETSI-Arbeitsgruppe STC SMG2 (STC = Subtechnical
Committee; SMG2 = Special Mobile Group 2) im September 1999 in Bordeaux
handelt, beschäftigt sich mit dem Wechsel eines dual-mode-Mobiltelefons (vgl.
Seite 2, Kap. 2.1, Absatz 1: „A UE (GSM/UMTS) capable mobile“) von GSM zu

                                       - 42 -



UMTS (vgl. Seite 1, Titel: „Aspects GSM to UMTS Handover“), und zwar sowohl
im idle mode (vgl. Seite 2, Kap. 2.2: „UE in idle mode“) als auch während einer
aktiven Daten-(packet switched) bzw. Telefonverbindung (circuit switched) (vgl.
Seite 3, Kap. 2.3.1: „CS Mode“ und Kap. 2.3.2: „PS Mode“), vgl. Seite 1, Kap. 1:


         „a concept for a packet and circuit switched handover from GSM to
         UMTS with focus on release 99 of GSM specifications. The basic concepts outlined are downloading of measurement orders, the UE measurements, the UMTS measurement reporting and the Handover execution.”


Im GSM-Netz wird an alle oder einzelne Mobiltelefone eine Aufforderungsnachricht (measurement order) geschickt, um bei den Mobiltelefonen UMTS-Messungen zu starten. In der Aufforderungsnachricht kann auch ein UMTS-Schwellwert
übertragen werden, von dem es in der Folge abhängt, ob bzw. wann UMTS-Messwerte von dem Mobiltelefon an das GSM-Netz berichtet werden oder nicht,
vgl. Seite 2, Kap. 2.1:


         „The measurement order may be broadcast in the GSM cell or sent to
         a specific UE camping on a GSM cell … In addition to Neighbouring
         Cell info the measurement order may also contain thresholds on
         UMTS measurements … the UMTS threshold may trigger the UMTS
         measurement reporting”


Während eines über GSM abgewickelten Telefongesprächs kann vom GSM-Netz
über den bidirektionalen Steuerkanal SACCH eine Aufforderung an das Mobiltelefon gesendet werden, auch UMTS-Messungen vorzunehmen, vgl. Seite 3, Kap.
2.3.1:


         „The downlink UMTS measurement order may be sent either on a
         SACCH, FACCH or SDCCH”

                                     - 43 -



Es nimmt dann in bestimmten Zeitabschnitten sowohl GSM-Messungen als auch
UMTS-Messungen vor, vgl. Seite 3, Kap. 2.4.3:


      „The UE shall use the four idle frames per SACCH block period for
      UMTS neighbouring cell measurements. These “search" frames are
      also used for the decoding of BSIC for GSM neighbouring cells as described in GSM 05.08. Consequently during these idle frames the UE
      will both perform measurements on UMTS neighbouring cells and decode BSIC on the maximum six strongest GSM neighbouring cells”


Die auf die Messungen folgenden UMTS-Messwertberichte sind von den GSM-Messwertberichten unabhängig, vgl. Seite 5, Kap. 2.5:


      „The UMTS Measurement reports from the UE are sent transparently
      through the BTS as a L3 message. The measurement reporting of
      UMTS and GSM cells are independent of each other. Both measurement reports are sent transparently through the BTS up to the BSC.
      Different options exist for sending the Measurement Reports.”


Wie im Streitpatent werden die – jedoch nicht umgewandelten – UMTS-Messwerte
über den GSM-Steuerkanal SACCH übertragen, vgl. S. 5, Kap. 2.5:


      „The SACCH may be used to send UMTS Measurement Reports for
      CS calls“


Um das GSM BSS (Base Station System, d. h. BSC (Base Station Controller) plus
BTS (Base Transceiver Station)) zu entlasten, soll das Mobiltelefon eine Vorauswahl treffen, in welcher Reihenfolge die UMTS- bzw. GSM-Messwerte im Messwertebericht an das GSM-Netz übertragen werden, vgl. Seite 6, Abs. 3:


      „To ease the implementation costs in BSS and to make GSM BSS
      more future resistant to changes in UTRAN the ranking of UMTS and

                                         - 44 -



        GSM measurements shall be done by the UE (the ranking is done
        separately, i.e. no direct comparison between a measurement on a
        UMTS cell and a measurement on a GSM cell). The UE shall then
        send indication of the ‘best’ measured UMTS cell in the measurement
        report. The measurement report is split in two parts, one GSM Measurement Report message and one UMTS Measurement report message.”


Hier kann entnommen werden, dass die UMTS- und die GSM-Messwerte in dem
Endgerät nicht direkt verglichen werden (no direct comparison) und es demzufolge
kein gemeinsames Messwerte-Ranking gibt (the ranking is done separately) und
dass die UMTS-Messwerte und die GSM-Messwerte getrennt voneinander übertragen werden („measurement report is split in two parts“).


Eine Anregung für den Fachmann, die UMTS-Messwerte in dem Endgerät in
GSM-Messwerte umzuwandeln, um sie dort mit den originären GSM-Messwerten
oder mit einem GSM-Schwellwert zu vergleichen, ist nicht ersichtlich. Dementsprechend ist der Druckschrift E1 auch keine konkrete Umwandlungsvorschrift für
RSCP-Messwerte in RXLEV-Messwerte zu entnehmen, wobei RSCP-Messwerte
als solche der Druckschrift E1 ohnehin nur mittelbar zu entnehmen sind (vgl.
Seite 2, Kap. 2.1, letzter Spiegelstrich „Path loss, signalstrength“).


Damit ist der Gegenstand des Anspruchs 1 des Streitpatents in der Fassung nach
Hilfsantrag 5 durch die Druckschrift E1 weder vorweggenommen noch nahe gelegt.


Nach dem Vorschlag in der Druckschrift E1 werden zwar sowohl die GSM- als
auch die UMTS-Messwerte jeweils in einer Rangliste gereiht, die beiden Messwertarten werden jedoch in separaten Nachrichten oder Teilnachrichten gesendet
und der Vergleich zwischen den beiden Messwertearten findet erst beim GSM
BSC (vgl. Seite 6, Kap. 2.6, Absätze 1 und 2) oder bei einem übergeordneten Radio Network Controler (RNC) statt (vgl. Seite 6, Kap. 2.6, Absatz 4).

                                         - 45 -



Zwar wird in Kapitel 3 (Seite 8) angesprochen, dass das GSM-Netz so wenig wie
möglich beeinflusst werden soll und es Probleme geben könnte, die neu hinzuzufügenden UMTS-bezogenen Informationen in den begrenzten Ressourcen der
GSM-Nachrichten unterzubringen, jedoch findet sich in der nachfolgenden Auflistung der möglicherweise betroffenen Nachrichten der GSM-Steuerkanal SACCH
nicht.


Auch handelt es sich bei dem Schwellwert, der die Übertragung der UMTS-Messwerte auslöst, nicht um einen GSM-, sondern um einen UMTS-Schwellwert (vgl.
Seite 2, Kap. 2.1), so dass keine Veranlassung für den Fachmann besteht, die
UMTS-Messwerte in GSM-Messwerte umzuwandeln, um sie mit einem GSM-Schwellwert zu vergleichen.


Aus der Druckschrift E1 ist nach alledem in den Worten des Patentanspruchs 1 in
der Fassung nach Hilfsantrag 5 nur bekannt


1        A method for conveying measurement information
           (vgl. Seite 5, Kap. 2.5: “Measurement reporting”)
1.1      from a terminal (UE) in a ﬁrst communication system (UMTS)
           (vgl. S. 5, Kap. 2.5, Abs. 2: “The UMTS Measurement reports from
           the UE are sent transparently through the BTS as a L3 message”)
1.2GSM        to a GSM communication system,
           (vgl. S. 5, Kap. 2.5, Abs. 2: “The UMTS Measurement reports from
           the UE are sent transparently through the BTS as a L3 message”,
           wobei BTS die Base Transceiver Station, also die Basisstation des
           GSM-Systems ist)
3teils   comparing said plurality of downlink measurement values (“Path loss,
         signalstrength, C/I, BER”, vgl. Seite 2, Kap. 2.1) with at least one threshold
         measurement value; and
           (da UMTS-Schwellwerte zum Mobiltelefon übertragen werden und
           diese UMTS-Schwellwerte einen UMTS-Messwertbericht auslösen
           sollen, liest der Fachmann einen Vergleich der – jedoch nicht um-

                                        - 46 -



            gewandelten – UMTS-Messwerte mit einem Schwellwert mit; vgl.
            Seite 2, Kap. 2.1, Abs. 1: „the UMTS threshold may trigger the
            UMTS measurement reporting“)
4.3teils if at least one of said plurality of downlink measurement values exceeds a
          predetermined threshold measurement value,
4teils    sending said at least one of said plurality of downlink measurement values
4.1       on a control channel
4.2GSM to a control node in said GSM communication system.
            (vgl. Ausführungen zum Merkmal 3 und Seite 5, drittletzter Punkt: “The
            SACCH may be used to send UMTS Measurement Reports for CS
            calls.”)


Danach ist der Gegenstand des Anspruchs 1 nach Hilfsantrag 5 neu gegenüber
der Druckschrift E1; er ergibt sich für den Fachmann auch nicht in naheliegender
Weise aus ihr.


4.2      Bei der Druckschrift E2 (Tdoc SMG2 1273/99) handelt es sich um einen
schriftlichen Beitrag der Firma Nokia für das im Zusammenhang mit der Druckschrift E1 bereits genannte Treffen der ETSI-Arbeitsgruppe STC SMG2 im September 1999 in Bordeaux.


Die Druckschrift E2 beschäftigt sich mit der Problematik, dass in GSM das verwendete Qualitätsmaß RXQUAL die tatsächliche Verbindungsqualität teilweise nur
ungenügend wiedergibt (vgl. Seiten 1 und 2, Kapitel „Usage of RXQUAL for quality
assessment“).


Zudem wird das Problem angesprochen, dass in Systemen mit mehreren Frequenzbändern (3-Band-GSM) oder mehreren Standards (GSM900, GSM1800,
UMTS) nur die Messwerte von sechs benachbarten Stationen in einem GSM-Messwertebericht von dem Mobiltelefon zu dem GSM-Netz übertragen werden
könnten, was als zu niedrig angesehen wird.

                                      - 47 -



Die Druckschrift E2 geht davon aus, dass die Anzahl der für jedes Netz zu übertragenden Messwerte gleich ist (z. B. jeweils zwei Messwerte bei einem 3-Band-System, vgl. Seite 2, letzter Absatz: „If it should be possible to report more than
two neighbours from the serving band“), insofern ist ein Vergleich der verschiedenen Messwerte mit dem Ziel ein sinnvollen Aufteilung offensichtlich nicht erforderlich.


Die Druckschrift E2 schlägt zur Verbesserung der Überwachung der Verbindungsqualität lediglich vor, die Anzahl der Messwerte in einem Messwertebericht zu erhöhen (vgl. Seite 3, Abs. 1: „Solutions to increase the number of reported neighbour cells should be concidered“).


Damit entnimmt der Fachmann der Druckschrift E2, dass GSM- und UMTS-Messwerte gemeinsam in einem GSM-Messwertbericht übertragen werden. Die Umwandlung von UMTS-Messwerten in Messwerte für das GSM-Kommunikationssystem ist aus der Druckschrift E2 nicht zu entnehmen und sie liefert hierzu auch
keine Hinweise oder Anregungen.


4.3     Bei der Druckschrift E3 (TSGR2#8(99)e61) handelt es sich um einen
schriftlichen Beitrag der Firma Ericsson für das 8. Arbeitstreffen des Jahres 1999
der 3GPP TSG-RAN Working Group 2 in Cheju, Korea, vom 2 bis
5. November 1999. Die Druckschrift E3 beschäftigt sich schwerpunktmäßig mit
dem Handover von UMTS zu GSM und den hierfür erforderlichen Messwertberichten und auslösenden Ereignissen. Handover von GSM zu UMTS (wie im
Streitpatent) sind ebenfalls angesprochen, wobei die Druckschrift E3 hierfür u. a.
auf das vorstehend als Druckschrift E1 genannte Dokument Tdoc SMG2 1145/99
verweist (vgl. Seite 1, Kap. 1: „inter-system measurement reporting and events for
support of Inter-System handover … Since the evaluation         of handover from
UTRAN to GSM needs to harmonise with the handover from GSM to UTRAN the
measurements and triggering conditions for the UE while connected to a GSM
system is also discussed. Aspects of the GSM part of the solution for GSM to
UTRAN handover has been discussed in Tdoc SMG2 1145/99”). Bezüglich des

                                          - 48 -



Wechsels von UMTS zu GSM wird eine Ereignis “3a” definiert, dass angibt, unter
welchen Bedingungen die GSM-Messwerte an das UMTS-Netz berichtet werden
sollen, nämlich dann, wenn die Qualität der aktuellen UMTS-Verbindung zu
schlecht wird und die Qualität der ggfs. aufzubauenden GSM-Verbindung hinreichend gut ist (vgl. Seite 2, Kap. 2.3, zweiter Satz). Die GSM-Messwerte werden in
einem UMTS-Messwerte-Bericht als solche, d. h. unverändert, übertragen (vgl.
Seite 2, letzter Satz: „The RSSI measurements on a GSM cell "GSM carrier RSSI"
[3] shall use the same mapping and range as specified in GSM 5.08“; Seite 3,
Kap. 2.5, Punkt 4: “and the best GSM cell have a GSM carrier RSSI above a
threshold Q_accept_GSM”; Seite 3, Kap. 2.5, Punkt 5: “Included in this report is
…”GSM carrier RSSI””). Jedoch wären zu den GSM-Messwerten ggfs. zellenindividuelle Offsets zu addieren bzw. zu subtrahieren (vgl. Seite 2, Kap. 2.2: „The
need for cell individual offset on GSM cells is for FFS”). Dies bringt zum Ausdruck,
dass solche zellenindividuellen Offsets im GSM-Standard 05.08 V6.3.0, auf den
die Druckschrift E3 verweist (vgl. Seite 1, Kap. 1, Abs. 2 mit Referenz [4]), nicht
vorgesehen sind.


Im Gegensatz dazu waren zellenindividuelle Offsets zur Beeinflussung des
Handover-Verhaltens innerhalb des UMTS-Netzes aus dem UMTS-Standard
25.331 V3.0.0, auf den die Druckschrift E3 ebenfalls verweist, bekannt. Solche
positiven oder negativen Offsets werden von dem UMTS-Netz an die Mobiltelefone übermittelt und dort zu den eigentlichen UMTS-Messwerten addiert (vgl. Anlage D3B der Klägerin zu 1 = Anlage NK4 der Klägerin zu 2 = TS 25.331 V3.0.0
(1999-10), Seite 237, Kap. 14.1.5.3: “For each cell that is monitored, an offset can
be assigned with inband signalling. The offset can be either positive or negative.
The offset is added to the measurement quantity before the UE evaluates if an
event has occurred. The UE receives the cell individual offsets for each primary
CPICH(FDD)/CCPCH(TDD)          in   the     measurement   object   field   of   the
MEASUREMENT CONTROL message”). Die veränderten UMTS-Messwerte sind
dann die Grundlage für die Auslösung eines Handovers innerhalb des UMTS-Netzes.

                                      - 49 -



Die Klägerinnen vertreten die Auffassung, dass die für den Wechsel von UMTS zu
GSM nur angedeutete und noch zu entwickelnde Möglichkeit der Addition von Offsets zu den GSM-Messwerten vor ihrer Übertragung auf einem UMTS-Steuerkanal dem Fachmann nahe legen würde, dass bei einem Wechsel von GSM zu
UMTS in gleicher Weise zu den UMTS-Messwerten Offsets addiert bzw. subtrahiert würden. Somit fände eine Umwandlung der UMTS-Messwerte in Messwerte
für das GSM-Netz statt.


Dem kann nicht zugestimmt werden. Der UMTS-Standard sieht die Berücksichtigung von Offsets vor, jedoch stammen diese vom UMTS-Netz und setzen somit
voraus, dass ein Mobiltelefon eine aktive UMTS-Telefon- oder Datenverbindung
betreibt oder sich zumindest im UMTS idle-mode befindet. Ist dies nicht der Fall,
weil das Mobiltelefon im relevanten Handover-Szenario zunächst im GSM-Netz
eingebucht ist, wäre es allenfalls denkbar, dass das GSM-Netz die im UMTS-System vorgesehen Werte für zellenindividuelle Offsets liefert, da in der Druckschrift E3 darauf hingewiesen wird (Seite 3, unterer Abschnitt, Punkt 4), dass bei
im GSM-Netz eingebuchten Mobiltelefon die UMTS-Messung auch dadurch ausgelöst werden könne, dass es sich um eine solche GSM-Zelle handelt, die UMTS-Nachbarzellen hat (vom Netzbetreiber definiert).


Möglicherweise könnte der Fachmann hier eine Anregung dafür erhalten, dass bei
einem im GSM-Netz eingebuchten Mobiltelefon UMTS-Offset-Informationen vom
GSM-Netz an die Mobiltelefone übertragen werden und dass diese UMTS-Offset-Werte zu den UMTS-Messwerten addiert werden.


Dies ist jedoch nicht damit gleichzusetzen, dass UMTS-Messwerte in Messwerte
für das GSM-Kommunikationssystem umgewandelt werden, um sie mit GSM-Messwerten vergleichbar zu machen. Vielmehr handelt es sich bei der Berücksichtigung der UMTS-Offsetwerte um einen Vorgang der nur für das UMTS-Netz
relevant ist.

                                      - 50 -



Daher sieht der Senat auch bei der Druckschrift E3 die streitpatentgemäße Umwandlung von UMTS-Messwerten in Messwerte für das GSM-Kommunikationssystem als nicht gegeben und auch nicht angeregt an.


4.4   Die weiteren im Verfahren befindlichen Druckschriften liegen, wie der Senat
bereits in seinem qualifizierten Hinweis angedeutet hatte, weiter ab und können
dem Fachmann daher ebenfalls die verteidigte Lösung der Aufgabe des Patents
nicht nahe legen. Etwas Gegenteiliges haben die Klägerinnen nach dem Hinweis
nicht geltend gemacht.


4.5   Die vorstehenden Ausführungen gelten entsprechend auch für den
nebengeordneten Anspruch 6 laut Hilfsantrag 5, dessen Gegenstand die Vorrichtung zur Durchführung des Verfahrens nach Anspruch 1 mit den dafür erforderlichen Merkmalen ist.
Auch den untergeordneten Ansprüchen nach Hilfsantrag 5, welche vorteilhafte
Ausgestaltungen des Erfindungsgegenstands betreffen, begegnen keinen Bedenken. Solche haben auch die Klägerinnen nicht vorgetragen.


V.    Da sich somit die mit dem Hauptantrag und den Hilfsanträgen 1 bis 4 verteidigten Fassungen der Ansprüche als nicht ausreichend offenbart bzw. als nicht
zulässig erweisen, während der mit Hilfsantrag 5 vorgelegte Anspruchssatz zulässig ist und ihm keine Nichtigkeitsgründe entgegenstehen, war das Streitpatent mit
Wirkung für die Bundesrepublik Deutschland nur insoweit teilweise für nichtig zu
erklären, als es über die Fassung laut Hilfsantrag 5 hinausgeht, und die weitergehenden Klagen abzuweisen.




                                       B.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1, § 100
Abs. 1 ZPO. Der Kostenverteilung hat der Senat dabei zugrunde gelegt, in welchem Umfang der nach Hilfsantrag 5 als schutzfähig verbleibende Patentgegen-

                                       - 51 -



stand gegenüber demjenigen der erteilten Fassung eingeschränkt ist. Da es sich
nach Auffassung des Senats um eine erhebliche Einschränkung handelt, ist es
gerechtfertigt, der Beklagten 3/4 der Kosten aufzuerlegen.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1
PatG i. V. m. § 709 ZPO.




                                        C.


                       Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130)
eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen
elektronischen Signatur versehen sein, die von einer internationalen Organisation
auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich
zur Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die
Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen
Urteils vorgelegt werden.


Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches

                                        - 52 -



Dokument     in   die   elektronische      Poststelle   des      Bundesgerichtshofes
(www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens
aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur
gewahrt, wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Friehe              Schwarz          Arnoldi            Matter            Dr. Haupt


                                                                                 prö
