---
court: "Bundespatentgericht"
aktenzeichen: "5 Ni 14/12 (EP) (verb. mit 5 Ni 29/12 (EP))"
decided: "2014-12-10"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/JURE159015644.xml"
neuris_doknr: "JURE159015644"
---

# Bundespatentgericht, 5 Ni 14/12 (EP) (verb. mit 5 Ni 29/12 (EP)) vom 2014-12-10

## Tenor

In der Patentnichtigkeitssache

…

…

betreffend das europäische Patent 1 166 486

(DE 600 40 847)

hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der mündlichen Verhandlung vom 10. Dezember 2014 durch die Vorsitzende Richterin Klante, die Richterin Martens sowie die Richter Dipl.-Ing. Gottstein, Dipl.-Ing. Kleinschmidt und Dipl.-Ing. (Univ.) Albertshofer

für Recht erkannt:

I. Das europäische Patent 1 166 486 wird mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland insoweit für nichtig erklärt, als es über folgende Anspruchsfassung hinausgeht:

1. A telecommunications system for transmitting data packets using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said telecommunications system comprising:

a transmitter (200) having a data link layer (60a) therein for receiving a service data unit (210) containing a plurality of said data packets, said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220);

a discard timer (300) within said transmitter (200) for monitoring a transmission timeout of said service data unit (210), said discard timer (300) being initialized when said service data unit (210) is received by said data link layer (60a); and

a receiver (250) for receiving said at least one protocol data unit (220) from said transmitter (200) over an air interface and transmitting an acknowledgment message (270, 285) to said transmitter (200) over said air interface after determining that said at least one protocol data unit (220) is received correctly,

means for discarding said service data unit (210) by said transmitter (200) and said receiver (250) when said acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires,

wherein said transmitter (200) further comprises:

means for transmitting a "move receiving window" request message to said receiver (250) when said discard timer (300) expires and said acknowledgment message (270, 285) for each said at least one protocol data unit (220) has not been received,

wherein said receiver (250) further comprises:

a receiver buffer (260) for storing said at least one protocol data unit (220), said at least one protocol data unit (220) being removed from said receive buffer (260) when said "move receiving window" request message (280) is received,

wherein said transmitter (200) further comprises:

a receive timer for monitoring a reception time of said "move receiving window" request message (280), said receive timer being initialized when said "move receiving window" request message (280) is transmitted by said transmitter (200), said transmitter (200) retransmitting said "move receiving window" request message (280) to said receiver (250) if said receiver timer expires and a "move receiving window" request acknowledgment message (270, 285) has not been received by said transmitter (200), and

an interval timer within said transmitter (200) for monitoring a time interval between an arrival time of said service data unit (210) at said data link layer (60a) and an arrival time of a successive service data unit (210) at said data link layer (60a), said interval timer being first initialized when said service data unit (210) is received by said data link layer (60a), said successive service data unit (210) being time stamped with the current value of said interval timer when said successive service data unit (210) is received by said data link layer (60a) and said discard timer (300) has not expired.

2. The telecommunications system of Claim 1, wherein said transmitter (200) further comprises:

a network layer (50a) for transmitting said service data unit (210) to said data link layer (60a); and

a physical layer (70a) for receiving said at least one protocol data unit (220) from said data link layer (60a) and transmitting said at least one protocol data unit (220) to said receiver (250) over said air interface.

3. The telecommunications system of Claim 1, wherein said receiver (250) further comprises:

a physical layer (70a) for receiving said at least one protocol data unit (220) from said transmitter (200) over said air interface;

a data link layer (60a) for receiving said at least one protocol data unit from said physical layer (70a), transmitting said acknowledgment message (270) after determining that said at least one protocol data unit (220) is received correctly, and assembling said at least one protocol data unit (220) back into said service data unit (210); and

a network layer (50a) for receiving said service data unit (210) from said data link layer (60a).

4. The telecommunications system of Claim 1, wherein said transmitter (200) further comprises:

a transmit buffer (230) for storing said at least one protocol data unit (220) until said acknowledgment message (270) is received for each said at least one protocol data unit (220) or until said discard timer (300) expires.

5. The telecommunications system of Claim 1, wherein said service data unit (210) has a header associated therewith, said header having a dedicated field therein for storing a default value for said discard timer (300).

6. The telecommunications system of Claim 5, wherein said default value is based on a maximum retransmission delay allowable for data within said data packets.

7. A method for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request,

said method comprising:

receiving, by a data link layer (60a) within said transmitter (200), a service data unit (210) containing a plurality of said data packets;

segmenting the service data unit (210) containing a plurality of said data packets into at least one protocol data unit (220);

initializing a discard timer (300) within said transmitter for monitoring the transmission timeout of said service data unit (210) to said receiver (250);

transmitting said at least one protocol data unit (220) from said transmitter (200) to said receiver (250) over said air interface; and

discarding said service data unit (210) by said transmitter when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires,

wherein said step of discarding further comprises the steps of:

transmitting a "move receiving window" request message from said transmitter (200) to said receiver (250) upon expiration of said discard timer (300) and said acknowledgment message (270, 285) for each said at least one protocol data unit (220) has not been received,

initializing a receive timer upon transmission of said "move receiving window" request message; and

retransmitting said "move receiving window" request message to said receiver (250) if said receiver (250) timer expires prior to receipt of a discard acknowledgment message (270, 285) from said receiver (250)

further comprising the steps of:

initializing an interval timer upon receipt of said service data unit (210) by a data link layer (60a) within said transmitter (200);

receiving a successive service data unit (210) by said data link layer (60a); and

appending a time stamp to said successive service data unit (210) received by said data link layer (60a), said time stamp being the current value of said interval timer when said discard timer (300) has not expired.

8. The method of Claim 7, further comprising the step of:

storing, in a transmit buffer (230) within said transmitter (200), each said at least one protocol data unit (220) until said acknowledgment message (270, 285) is received for each said at least one protocol unit or until said discard timer (300) expires.

9. The method of Claim 7, further comprising the steps of:

stopping said discard timer (300) when said acknowledgment message (270, 285) for each said at least one protocol data unit (220) associated with said service data unit (210) is received by said transmitter (200) or when said discard timer (300) expires; and

reinitializing said discard timer (300) for said successive service data unit (210) with a value of said time stamp.

Im Übrigen werden die Klagen abgewiesen.

II. Von den Kosten des Rechtsstreits tragen die Beklagte 4/5 und die Klägerinnen jeweils 1/10.

III. Das Urteil ist jeweils gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.

## Tatbestand

1 Die Beklagte ist die jetzige Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 1 166 486 (Streitpatent) und mit Zustimmung der Parteien in das Verfahren gegen die ursprüngliche Rechteinhaberin eingetreten. Das Streitpatent ist am 4. April 2000 unter Inanspruchnahme der Priorität der US-amerikanischen Patentanmeldung US 287,392 vom 6. April 1999 angemeldet und in der Verfahrenssprache Englisch veröffentlicht worden. Es trägt die Bezeichnung: „Packet Discard Notification For Semi Reliable Retransmission Protocol“ (Paketeliminierungsmeldung für halbzuverlässiges Wiederholungsprotokoll) und wird beim Deutschen Patent- und Markenamt unter dem Aktenzeichen 600 40 847.7 geführt. Es umfasst 24 Ansprüche, die alle mit der Nichtigkeitsklage angegriffen worden sind.

2 Die nebengeordneten Patentansprüche 1, 11 und 19 haben in der Verfahrenssprache folgenden Wortlaut:

3 “1. A telecommunications system for transmitting data packets using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said telecommunications system comprising:

4 a transmitter (200) having a data link layer (60a) therein for receiving a service data unit (210) containing a plurality of said data packets, said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220);

5 a discard timer (300) within said transmitter (200) for monitoring a transmission timeout of said service data unit (210), said discard timer (300) being initialized when said service data unit (210) is received by said data link layer (60a); and

6 a receiver (250) for receiving said at least one protocol data unit (220) from said transmitter (200) over an air interface and transmitting an acknowledgment message (270, 285) to said transmitter (200) over said air interface after determining that said at least one protocol data unit (220) is received correctly,

7 means for discarding said service data unit (210) by said transmitter (200) and said receiver (250) when said acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires.

8 11. A transmitter (200) for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request,

9 said transmitter comprising:

10 a data link layer (60a) for receiving a service data unit (210) containing a plurality of said data packets, said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220); and

11 a discard timer (300) for monitoring the transmission timeout of said at least one service data unit (210) to said receiver (250), said discard timer (300) being initialized when said service data unit (210) is received by said data link layer (60a), said service data unit (210) being discarded by said data link layer (60a) when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires.

12 19. A method for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request,

13 said method comprising:

14 receiving, by a data link layer (60a) within said transmitter (200), a service data unit (210) containing a plurality of said data packets;

15 segmenting the service data unit (210) containing a plurality of said data packets into at least one protocol data unit (220);

16 initializing a discard timer (300) within said transmitter for monitoring the transmission timeout of said service data unit (210) to said receiver (250);

17 transmitting said at least one protocol data unit (220) from said transmitter (200) to said receiver (250) over said air interface; and

18 discarding said service data unit (210) by said transmitter when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires.”

19 In deutscher Übersetzung lauten die nebengeordneten Patentansprüche 1, 11 und 19 wie folgt:

20 1. Telekommunikationssystem zur Übertragung von Datenpaketen unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei das Telekommunikationssystem umfaßt:

21 einen Sender (200) mit einer Datensicherungsschicht (60a) darin zum Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält, wobei die Datensicherungsschicht (60a) die Dienstdateneinheit (210) in mindestens eine Protokolldateneinheit (220) segmentiert;

22 einen Abwurf-Zeitgeber (300) innerhalb des Senders (200) zur Überwachung einer Übertragungswiederholungs-Zeitüberschreitung der Dienstdateneinheit (210), wobei der Abwurf-Zeitgeber (300) initialisiert wird, wenn die Dienstdateneinheit (210) durch die Datensicherungsschicht (60a) empfangen wird; und

23 einen Empfänger (250) zum Empfangen der mindestens einen Protokolldateneinheit (220) von dem Sender (200) über eine Funkschnittstelle und Übertragen einer Bestätigungsnachricht (270, 285) an den Sender (200) über die Funkschnittstelle, nachdem bestimmt worden ist, daß die mindestens eine Protokolldateneinheit (220) korrekt empfangen worden ist;

24 Mittel zum Abwerfen der Dienstdateneinheit (210) durch den Sender (200) und den Empfänger (250), wenn die Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und der Abwurf-Zeitgeber (300) abläuft.

25 11. Ein Sender (200) zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger (250) unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei der Sender umfaßt:

26 eine Datensicherungsschicht (60a) zum Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält, wobei die Datensicherungsschicht (60a) die Dienstdateneinheit (210) in mindestens eine Protokolldateneinheit (220) segmentiert; und

27 einen Abwurf-Zeitgeber (300) zur Überwachung der Zeitüberschreitung der Übertragungswiederholung der mindestens einen Dienstdateneinheit (210) an den Empfänger (250), wobei der Abwurf-Zeitgeber (300) initialisiert wird, wenn die Dienstdateneinheit (210) durch die Datensicherungsschicht (60a) empfangen wird, wobei die Dienstdateneinheit (210) von der Datensicherungsschicht (60a) abgeworfen wird, wenn eine Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und der Abwurf-Zeitgeber (300) abläuft.

28 19. Verfahren zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger (250) unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei das Verfahren umfaßt:

29 durch eine Datensicherungsschicht (60a) innerhalb des Senders (200) erfolgendes Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält;

30 Segmentieren der Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält, in mindestens eine Protokolldateneinheit (220);

31 Initialisieren eines Abwurf-Zeitgebers (300) innerhalb des Senders zur Überwachung der Übertragungswiederholungs-Zeitüberschreitung der Dienstdateneinheit (210) an den Empfänger (250);

32 Übertragen der mindestens einen Protokolldateneinheit (220) von dem Sender (200) an den Empfänger (250) über die Funkschnittstelle; und

33 Abwerfen der Dienstdateneinheit (210) durch den Sender, wenn eine Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und der Abwurf-Zeitgeber (300) abläuft.

34 Wegen des Wortlauts der auf die nebengeordneten Patentansprüche 1, 11 und 19 jeweils unmittelbar oder mittelbar rückbezogenen Ansprüche 2 bis 10, 12 bis 18 sowie 20 bis 24 wird auf die Streitpatentschrift EP 1 166 486 B1 Bezug genommen.

35 Mit ihren am 22. Februar 2012 bzw. 13. April 2012 erhobenen Nichtigkeitsklagen machen die Klägerinnen geltend, der Gegenstand des Streitpatents sei nicht patentfähig, da er weder neu sei noch auf einer erfinderischen Tätigkeit beruhe. Die Klägerin zu 1) beruft sich zudem auf den Nichtigkeitsgrund der unzulässigen Erweiterung des Streitpatents gegenüber dem Inhalt der Anmeldung in ihrer ursprünglich eingereichten Fassung.

36 Die Klägerinnen stützen ihr Vorbringen zur fehlenden Patentfähigkeit auf folgende Druckschriften:

37 K4 WLAN-Standard IEEE 802.11-1997: Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) specifications, Inhaltsverzeichnis und Seiten 1, 71-96; auch „K4/WLAN-97“ genannt,

38 K5 ETSI, Technischer Report TR 101 173, Version 1.1.1, Mai 1998; auch „K5/ETSI“ genannt,

39 K6 DE 195 43 280 A1, auch „K6/WALKE“ genannt,

40 K7 BAKKER, J. D. et. al.: An Air Interface for High Bandwidth Cellular Digital Communications on Microwave Frequencies. In: Vehicular Technology Conference 1998, 18.-21. Mai 1998, auch „K7/BAKKER“ genannt,

41 K8 TANENBAUM, A.: Computer Networks, 3. Auflage, 1996, Seiten 190-219, auch „K8/TANENBAUM“ genannt,

42 K8a ebenda, Seiten 521-542,

43 K8b ebenda, Seiten 413-416,

44 K9 HETTICH, A.: Entwicklung und Leistungsbewertung eines Selective Repeat-Automatic-Repeat Request (SR-ARQ)-Protokolls für transparenten, mobilen ATM-Zugriff, Diplomarbeit an der RWTH Aachen, 17. Januar 1996, auch „K9/HETTICH“ genannt,

45 K9a Auszüge des Zweijahresberichts des Lehrstuhls für Kommunikationsnetze „ComNets“ der RWTH Aachen, 1994-1996,

46 K12 ITU-T Recommendation I.363.2, Series I: Integrated Services Digital Networks – Overall network aspects and functions – Protocol layer requirements: B-ISDN ATM Adaptation layer specification: Type 2 AAL (Ausgabe 09/97),

47 K14a Internet Protocol, Darpa Internet Program, Protocol Specification, September 1981 (RFC 791),

48 K14b Internet Engineering Task Force: Requirements for Internet Hosts - Communication Layers, October 1989 (RFC 1122),

49 K15 ETSI: Draft EN 301 349 V6.1.0 (1998-08), “Digital cellular telecommunications system (Phase 2+); General Packet Radio Service (GPRS); Mobile Station (MS) - Base Station System (BSS) interface; Radio Link Control / Medium Access Control (RLC/MAC) protocol (GSM 04.60 version 6.1.0 Release 1997)”.

50 Die Klägerinnen beantragen,

51 das europäische Patent EP 1 166 486 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.

52 Die Beklagte beantragt,

53 die Nichtigkeitsklage abzuweisen, soweit das Patent mit den erteilten Patentansprüchen 1 bis 18 und 20 bis 24 wie erteilt und dem mit Schriftsatz vom 20. Oktober 2014 eingereichten Patentanspruch 19 gemäß Hauptantrag, wobei sich die abhängigen Ansprüche 20 bis 24 auf den neuen Patentanspruch 19 beziehen, verteidigt wird.

54 Hilfsweise stellt die Beklagte den Antrag,

55 die Klage mit der Maßgabe abzuweisen, dass das Streitpatent die Fassung des Hilfsantrags 1, überreicht in der mündlichen Verhandlung, bzw. eines der Hilfsanträge 2 bis 6 gemäß Schriftsatz vom 20. Oktober 2014 erhält.

56 Soweit die Beklagte das Streitpatent gemäß Hauptantrag verteidigt, wird Patentanspruch 19 in der erteilten Fassung um das Merkmal ergänzt, dass der Abwurf-Zeitgeber (discard timer) initialisiert wird, wenn die Dienstdateneinheit (service data unit) durch die Datensicherungsschicht (data link layer) empfangen wird. Patentanspruch 19 gemäß Hauptantrag lautet danach wie folgt:

57 Dieser Fassung von Patentanspruch 19 schließen sich die Unteransprüche 20 bis 24 der erteilten Fassung an, wobei sich diese Ansprüche auf den neuen Patentanspruch 19 beziehen.

58 Mit Hilfsantrag 1 in der in der mündlichen Verhandlung überreichten Fassung beantragt die Beklagte, die Klage abzuweisen, soweit das Streitpatent mit den Ansprüchen 1 bis 10 wie erteilt und den Patentansprüchen 17 bis 21 gemäß Hilfsantrag 2, verteidigt wird.

59 Gemäß Hilfsantrag 2 lauten die nebengeordneten Ansprüche 1, 10 und 17 wie folgt:

60 Gemäß Hilfsantrag 3 lauten die nebengeordneten Ansprüche 1, 11 und 19 wie folgt:

61 Gemäß Hilfsantrag 4 lauten die nebengeordneten Ansprüche 1, 10 und 17 wie folgt:

62 Gemäß Hilfsantrag 5 lauten die nebengeordneten Ansprüche 1, 8 und 14 wie folgt:

63 Gemäß Hilfsantrag 6 lauten die nebengeordneten Ansprüche 1, 7 und 12 wie folgt:

64 rückbezogenen Unteransprüche wird auf die Anspruchssätze der jeweiligen Hilfsanträge gemäß den Anlagen zum Schriftsatz der Beklagten vom 20. Oktober 2014 verwiesen.

65 Die Beklagte tritt dem Vorbringen der Klägerinnen in allen Punkten entgegen und hält die Nichtigkeitsklage für unbegründet. Weder sei der Gegenstand des Streitpatents unzulässig erweitert, noch die Lehre des Streitpatents durch den im Verfahren befindlichen Stand der Technik am Prioritätstag neuheitsschädlich vorweggenommen oder dem Fachmann nahe gelegt gewesen.

66 Zur Erläuterung ihres Vorbringens bezüglich der Patentfähigkeit nimmt die Beklagte auf folgende Unterlagen Bezug:

67 B3 PERKINS, C.; HODSON, O.: Options for Repair of Streaming Media (Network Working Group, RFC 2354), June 1998

68 B4 PERKINS, Colin; HODSON, Orion; HARDMAN, Vicky: A Survey of Packet Loss Recovery Techniques for Streaming Audio. In: IEEE Network, September/October 1989, Seiten 40-48

69 B5 HARDMAN, Vicky [u. a.]: Reliable Audio for Use over the Internet. In: Proc. INET ’95

70 B6 BERTSEKAS, Dimitri; GALLAGER, Robert: Data Networks. Prentice-Hall, 2. Auflage, 1992, ISBN 0-13-200916-1, Seiten v-vi, 64-86 (Kapitel 2.4 ARQ: Retransmission Strategies).

71 Der Senat hat den Parteien einen qualifizierten Hinweis nach § 83 Abs. 1 PatG zugeleitet, auf diesen Hinweis vom 12. September 2014 (Bl. 257 der Gerichtsakte) wird Bezug genommen.

## Entscheidungsgründe

72 Die Klagen sind zulässig und teilweise – wie aus dem Tenor ersichtlich – begründet.

73 Die Nichtigkeitsklagen sind jedoch abzuweisen, soweit die Beklagte das Streitpatent mit den im Tenor wiedergegebenen Patentansprüchen, die Teil des Hilfsantrags 6 sind, verteidigt. Diesen Ansprüchen steht keiner der geltend gemachten Nichtigkeitsgründe nach Art. II § 6 Abs. 1 Nrn. 1 und 3 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a und c EPÜ entgegen.

I.

74 1. Das Streitpatent betrifft ein Telekommunikationssystem mit einem Sender und einem Empfänger zur Übertragung von Datenpaketen über eine Funkschnittstelle unter Verwendung eines sogenannten „Selective Repeat Automatic Repeat Request“-Verfahrens (SR-ARQ; Ansprüche 1 bis 10). Außerdem betrifft das Streitpatent einen Sender (Ansprüche 11 bis 18) sowie ein Verfahren für eine Übertragung von Datenpaketen mittels SR-ARQ (Ansprüche 19 bis 24).

75 Die Erfindung geht dazu von einem Stand der Technik aus, der in den Absätzen 0002 bis 0007 der Patentschrift beschrieben ist.

76 2. Der Erfindung liegt die Aufgabe zugrunde, Abstufungen für die Zuverlässigkeit der Übertragung zu schaffen (Streitpatent, Absatz 0008).

77 3. Gelöst sieht das Streitpatent die Aufgabe durch ein halb-zuverlässiges Übertragungsprotokoll vor. Diese Halb-Zuverlässigkeit wird laut Streitpatent dadurch erreicht, dass einzelne Pakete vom Sender und vom Empfänger verworfen werden können, ohne dass die Verbindung zurückgesetzt wird. Das Verwerfen erfolgt zeitgesteuert durch einen Zeitgeber, der die maximal zulässige Verzögerungszeit der jeweilig zu übertragenden Dienstdateneinheit berücksichtigt und beispielsweise in Anhängigkeit von einem vorgegebenen Dienstqualitätsmaß („Quality of Service level“) oder von dem zu übertragenden Datentyp festgelegt wird (Absätze 0009, 0020).

78 Die nebengeordneten Patentansprüche 1, 11 und 19 in der mit dem Hauptantrag verteidigten Fassung lassen sich in der Verfahrenssprache wie folgt nach Merkmalen gliedern:

79 Anspruch 1:

80 T.1 A telecommunications system for transmitting data packets using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said telecommunications system comprising:

81 T.2 a transmitter (200) having

82 T.2.1 a data link layer (60a) therein for receiving a service data unit (210) containing a plurality of said data packets,

83 T.2.2 said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220);

84 T.3 a discard timer (300) within said transmitter (200) for monitoring a transmission timeout of said service data unit (210),

85 T.4 said discard timer (300) being initialized when said service data unit (210) is received by said data link layer (60a); and

86 T.6 a receiver (250) for

87 T.6.1 receiving said at least one protocol data unit (220) from said transmitter (200) over an air interface and

88 T.6.2 transmitting an acknowledgment message (270, 285) to said transmitter (200) over said air interface after determining that said at least one protocol data unit (220) is received correctly,

89 T.7 means for discarding said service data unit (210) by said transmitter (200) and said receiver (250) when

90 T.7.1 said acknowledgment message (270) is not received for each said at least one protocol data unit (220) and

91 T.7.2 said discard timer (300) expires.

92 Anspruch 11:

93 S.1 A transmitter (200) for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said transmitter comprising:

94 S.2 a data link layer (60a) for receiving a service data unit (210) containing a plurality of said data packets,

95 S.3 said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220); and

96 S.4 a discard timer (300) for monitoring the transmission timeout of said at least one service data unit (210) to said receiver (250),

97 S.5 said discard timer (300) being initialized when said service data unit (210) is received by said data link layer (60a),

98 S.6 said service data unit (210) being discarded by said data link layer (60a)

99 S.6.1 when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and

100 S.6.2 said discard timer (300) expires.

101 Anspruch 19

102 M.1 A method for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said method comprising:

103 M.2 receiving, by a data link layer (60a) within said transmitter (200), a service data unit (210) containing a plurality of said data packets;

104 M.3 segmenting the service data unit (210) containing a plurality of said data packets into at least one protocol data unit (220);

105 M.4 initializing a discard timer (300) within said transmitter when said service data unit is received by said data link layer for monitoring the transmission timeout of said service data unit (210) to said receiver (250);

106 M.5 transmitting said at least one protocol data unit (220) from said transmitter (200) to said receiver (250) over said air interface; and

107 M.6 discarding said service data unit (210) by said transmitter when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires.

108 In deutscher Übersetzung lauten die gegliederten nebengeordneten Ansprüche gemäß Hauptantrag wie folgt:

109 Anspruch 1:

110 T.1Telekommunikationssystem zur Übertragung von Datenpaketen unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei das Telekommunikationssystem umfaßt:

111 T.2 einen Sender (200) mit

112 T.2.1 einer Datensicherungsschicht (60a) darin zum Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält,

113 T.2.2 wobei die Datensicherungsschicht (60a) die Dienstdateneinheit (210) in mindestens eine Protokolldateneinheit (220) segmentiert;

114 T.3 einen Abwurf-Zeitgeber (300) innerhalb des Senders (200) zur Überwachung einer Übertragungswiederholungs-Zeitüberschreitung der Dienstdateneinheit (210),

115 T.4 wobei der Abwurf-Zeitgeber (300) initialisiert wird, wenn die Dienstdateneinheit (210) durch die Datensicherungsschicht (60a) empfangen wird; und

116 T.6 einen Empfänger (250) zum

117 T.6.1 Empfangen der mindestens einen Protokolldateneinheit (220) von dem Sender (200) über eine Funkschnittstelle und

118 T.6.2 Übertragen einer Bestätigungsnachricht (270, 285) an den Sender (200) über die Funkschnittstelle, nachdem bestimmt worden ist, daß die mindestens eine Protokolldateneinheit (220) korrekt empfangen worden ist;

119 T.7 Mittel zum Abwerfen der Dienstdateneinheit (210) durch den Sender (200) und den Empfänger (250), wenn

120 T.7.1 die Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und

121 T.7.2 der Abwurf-Zeitgeber (300) abläuft.

122 Anspruch 11:

123 S.1 Ein Sender (200) zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger (250) unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei der Sender umfaßt:

124 S.2 eine Datensicherungsschicht (60a) zum Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält, wobei

125 S.3 die Datensicherungsschicht (60a) die Dienstdateneinheit (210) in mindestens eine Protokolldateneinheit (220) segmentiert; und

126 S.4 einen Abwurf-Zeitgeber (300) zur Überwachung der Zeitüberschreitung der Übertragungswiederholung der mindestens einen Dienstdateneinheit (210) an den Empfänger (250),

127 S.5 wobei der Abwurf-Zeitgeber (300) initialisiert wird, wenn die Dienstdateneinheit (210) durch die Datensicherungsschicht (60a) empfangen wird,

128 S.6 wobei die Dienstdateneinheit (210) von der Datensicherungsschicht (60a) abgeworfen wird, wenn

129 S.6.1 eine Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und

130 S.6.2 der Abwurf-Zeitgeber (300) abläuft.

131 Anspruch 19:

132 M.1 Verfahren zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger (250) unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls, das automatische Wiederholungsanforderung mit selektiver Wiederholung verwendet, wobei das Verfahren umfaßt:

133 M.2 durch eine Datensicherungsschicht (60a) innerhalb des Senders (200) erfolgendes Empfangen einer Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält;

134 M.3 Segmentieren der Dienstdateneinheit (210), die eine Vielzahl der Datenpakete enthält, in mindestens eine Protokolldateneinheit (220);

135 M.4 Initialisieren eines Abwurf-Zeitgebers (300) innerhalb des Senders, wenn die Dienstdateneinheit von der Datensicherungsschicht empfangen wurde, zur Überwachung der Übertragungswiederholungs-Zeitüberschreitung der Dienstdateneinheit (210) an den Empfänger (250);

136 M.5 Übertragen der mindestens einen Protokolldateneinheit (220) von dem Sender (200) an den Empfänger (250) über die Funkschnittstelle; und

137 M.6 Abwerfen der Dienstdateneinheit (210) durch den Sender, wenn eine Bestätigungsnachricht (270) nicht für jede der mindestens einen Protokolldateneinheit (220) empfangen wird und der Abwurf-Zeitgeber (300) abläuft.

138 4. Maßgeblicher Fachmann für die Entwicklung des anspruchsgemäßen Telekommunikationssystems, des anspruchsgemäßen Senders und des anspruchsgemäßen Verfahrens ist nach Auffassung des Senats ein Hochschulingenieur der Fachrichtung Nachrichtentechnik mit einschlägiger Erfahrung auf dem Gebiet der Übertragungstechnik, insbesondere den dabei anzuwendenden Fehlerbehandlungsstrategien. Zu den maßgeblichen Kenntnissen gehören Kenntnisse über die sogenannten automatischen Wiederholungsanfragen (ARQ). Die Lehre des Streitpatents liegt insgesamt auf dem Gebiet der drahtlosen Kommunikation.

139 a) Der Fachmann erkennt ohne Weiteres, dass die Patentschrift weitgehend auf eine Terminologie zurückgreift, wie sie im OSI-Referenzmodell gebräuchlich ist („data link layer (60a)“ = Datensicherungsschicht; „network layer“ = Netzwerk- oder Vermittlungsschicht; „service data unit (210)“ = Dienstdateneinheit; „protocol data unit (220)“ = Protokolldateneinheit). Mangels anders lautender Definitionen versteht der Fachmann die Begriffe im Kontext des OSI-Referenzmodells.

140 b) Die Angabe „said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220)“ („die Datensicherungsschicht (60a) die Dienstdateneinheit (210) in mindestens eine Protokolldateneinheit (220) segmentiert“; Merkmale T.2.2, S.3, M.3) umfasst jeweils auch die Möglichkeit, dass die Dienstdateneinheit in genau eine Protokolldateneinheit segmentiert wird, de facto also nicht unterteilt wird, sondern als ein einziger, ungeteilter Datenblock zur Übertragung bereitgestellt wird. Dies wird immer dann der Fall sein können, wenn eine Dienstdateneinheit kleiner ist als die zu übertragenden Protokolldateneinheiten. Allerdings wird dies nur die Ausnahme und nicht die Regel sein.

141 Die Angabe „said data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220)“ (Merkmale T.2.2, S.3, M.3) wird vom Fachmann mithin dahingehend verstanden, dass die betreffende Vorrichtung die Fähigkeit hat, größere Dienstdateneinheiten, die nicht in eine Protokolldateneinheit passen, zu zerteilen und nicht jede Dienstdateneinheit zerteilt werden muss. Vielmehr kann bei einer kleinen Dienstdateneinheit, sofern sie in eine Protokolldateneinheit hineinpasst, das Zerteilen unterbleiben (vgl. auch Schriftsatz der Klägerin zu 1 vom 24. November 2014, Seite 2).

142 Eine Vorrichtung, die überhaupt nicht über die Fähigkeit zum Segmentieren verfügt, ist nicht Gegenstand des Anspruchs 1. Auf zur Segmentierung fähige Mittel kann nicht verzichtet werden, selbst wenn diese Mittel bezogen auf eine konkrete Dienstdateneinheit tatsächlich keine Segmentierung in mehr als eine Protokolldateneinheit bewirken.

143 Nicht vereinbar mit dem insoweit eindeutigen Anspruchswortlaut wäre aber auch eine Auslegung dahingehend, dass vom Begriff des Segmentierens einer Dienstdateneinheit in mindestens eine Protokolldateneinheit auch die Zusammenfügung mehrerer Dienstdateneinheiten zu einer Protokolldateneinheit umfasst wäre. Dass eine Protokolldateneinheit auch Daten aus mehreren Dienstdateneinheiten umfassen kann, ist zwar in der Patentschrift als mögliche Alternative angegeben (vgl. Absatz 0022), aber in dieser Form nicht beansprucht worden. Dieser – als solcher auch ursprünglich offenbarte – Aspekt ist nicht Teil des erteilten Patents geworden. Dem Anspruchswortlaut kommt gegenüber der Beschreibung Vorrang zu (BGH, Urteil vom 10. Mai 2011 – X ZR 16/09, BGHZ 189, 330, Tz. 23 - Okklusionsvorrichtung).

144 c) Den Begriff des „discarding“ („Abwerfens“), auch in Zusammensetzungen wie „discard timer“ („Abwurf-Zeitgeber“), versteht der Fachmann im Sinne eines Verwerfens, d. h., dass eine bestimmte Dienstdateneinheit als Ganzes nicht weiter verwendet wird. Das entspricht auch der von der hiesigen Nichtigkeitsbeklagte im Verletzungsverfahren verwendeten Diktion, die von den Klägerinnen für das hiesige Verfahren übernommen wurde (siehe Fußnote 3 auf Seite 12 der Klageschrift). Praktischerweise wird das Abwerfen dadurch erreicht, dass die Dienstdateneinheit aus dem nicht ausdrücklich im Anspruch erwähnten, für das Funktionieren aber zwingend vom Fachmann ergänzten Eingangsspeicher („transmit buffer 230“, „receiver buffer 260“, vgl. Absätze 0014 und 0017, Figuren 2 und 3) gelöscht wird bzw. die zu seiner Speicherung jedenfalls reservierten Speicherbereiche wieder freigegeben werden (vgl. Spalte 2, Zeilen 30-32; Spalte 7, Zeilen 13-15). Wie sich aus dem Merkmal T.7 ergibt, sind jedenfalls für das Telekommunikationssystem als Ganzes sowohl auf der Senderseite als auch auf der Empfängerseite Mittel vorgesehen, die das „Abwerfen“ bewerkstelligen können. Dass der Abwurf tatsächlich erfolgt, ist nur für die Senderseite spezifiziert (Merkmale S.6, M.6).

145 Es ist für das Übertragungsverfahren offensichtlich notwendig, dass nicht nur auf der Senderseite, sondern auch auf der Empfängerseite Mittel vorhanden sein müssen, die aus den empfangenen Protokolldateneinheiten, welche Segmente der gesendeten Dienstdateneinheit darstellen, wieder eine Dienstdateneinheit zusammensetzen können. Soweit ein Verwerfen auf der Empfängerseite erfolgen soll (Merkmal T.7: „… means for discarding said service data unit (210) by said transmitter (200) and said receiver (250) …“), versteht der Fachmann hierunter nicht nur das Verwerfen der gesamten, vollständig zusammengesetzten Dienstdateneinheit. Der Fachmann versteht das Verwerfen auf der Empfängerseite auch dahingehend, dass es im Fehlerfall genügt, die zu einer Dienstdateneinheit gehörenden Protokolldateneinheiten zu verwerfen, wenn sich einzelne Protokolldateneinheit als fehlerhaft erweisen oder nicht empfangen werden konnten und deshalb eine Bestätigungsnachricht nicht für jede Protokolldateneinheit empfangen wird (Merkmal T.7.1). Dies kann insbesondere durch die Freigabe der für die zusammengesetzte Dienstdateneinheit reservierten Speicherbereiche erfolgen.

146 Der Fachmann versteht auch, dass nach Eintreten der Bedingungen T.7.1 und T.7.2, die sich auf einzelne Protokolldateneinheiten beziehen, die gesamte Dienstdateneinheit verworfen wird.

147 d) Die Begriffe „data packets“ („Datenpakete“) und „protocol data unit“ („Protokolldateneinheit“) versteht der Fachmann entgegen der von den Klägerinnen vertretenen Auffassung (Klageschrift Seite 17, 2. Absatz) nicht synonym. Bei den Datenpaketen handelt es sich um die Strukturierung der insgesamt zu übertragenden Dienstdateneinheit auf der Eingangsseite der senderseitigen Datensicherungsschicht. Bei den Protokolldateneinheiten hingegen handelt es sich um eine Strukturierung (Segmente) der Dienstdateneinheit auf der Ausgangsseite der senderseitigen Datensicherungsschicht. Die Datenpakete umfassende Dienstdateneinheit wird quasi in der Datensicherungsschicht zu Protokolldateneinheiten umgeformt (zur Definition vgl. auch Absatz 0015).

II.

148 Soweit die Beklagte das Streitpatent nicht mehr verteidigt, ist es ohne weitere Sachprüfung für nichtig zu erklären (BGH, Urteil vom 19. Dezember 2006 - X ZR 236/01, BGHZ 170, 215 – Carvedilol II).

149 Soweit der Gegenstand des Streitpatents über die im Tenor aufgeführten Patentansprüche hinausgeht, ist sein Gegenstand mangels erfinderischer Tätigkeit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ).

150 1. Die selbständigen Ansprüche 1, 11 und 19 gemäß Hauptantrag erweisen sich mangels erfinderischer Tätigkeit als nicht patentfähig (Art. II § 6 Abs. 1 Nrn. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ).

151 Die Druckschrift K6/WALKE offenbart ein zellulares Mobilfunksystem auf der Basis der ATM-Technologie (Spalte 1, Zeilen 22-27; Spalte 2, Zeilen 29-32; Spalte 3, Zeilen 39-50; Spalte 9, Zeilen 21-25; Merkmale T.1, T.2, T.2.1, T.6, T.6.1, T.6.2, S.1, S.2, M.1, M.2, M.5). Die Übertragung von ATM-Zellen, die den anspruchsgemäßen Dienstdateneinheiten entsprechen, erfolgt in Rahmen, welche wiederum den Protokolldateneinheiten entsprechen (Spalte 7, Zeile 54; Merkmale T.2.2, S.3, M.3), wobei ein Fehlerkorrekturverfahren basierend auf einem Fensteralgorithmus zum Einsatz kommt (Spalte 5, Zeilen 40-45).

152 Hierbei können einzelne Datenpakete (ATM-Zellen = Dienstdateneinheiten) verworfen werden (Spalte 9, Zeilen 21-33; Spalte 12, Zeilen 51-54). Insbesondere kann dies geschehen, wenn eine ATM-Zelle nach einer erfolglosen, insbesondere fehlerhaften Übertragung vom Empfänger zur wiederholten Übertragung angefordert wird, aber zwischendurch ihre maximale Verzögerung erreicht hat (Spalte 12, Zeilen 59-66; Merkmale T.7teilweise, T.7.1, T.7.2, S.6, S.6.1, S.6.2, M.6).

153 Der Fachmann entnimmt der Druckschrift K6/WALKE darüber hinaus, dass für das Verwerfen von Datenpaketen nach Ablauf der maximalen Zeitverzögerung, die Verweildauer der einzelnen Datenpaket im Sender mit Hilfe eines sogenannten Ignore-Timers/Zeitgeber zu ermitteln (Spalte 11, Zeilen 23-40; Merkmale T.3, S.4). Der Ignore-Timer wird bei Versenden eines N-Rahmens mit der Laufnummer N(S) auf die doppelte ARQ-Rahmenlaufzeit gesetzt (initialisiert) und bis zu dessen Ablauf werden alle Anfragen zur wiederholten Übertragung dieses Rahmens mit dem Befehl SREJ(N(S)) verworfen, weil diese offensichtlich vom Empfänger vor dem Empfang des zuletzt gesendeten Rahmens abgesendet wurden und sich noch nicht auf den zuletzt übertragenen Rahmen beziehen können (Spalte 11, Zeilen 32-40; Merkmale T.4teilweise, S.5teilweise, M.4teilweise).

154 a) Von dem, was der Fachmann der der Druckschrift K6/WALKE entnehmen kann, unterscheidet sich der Gegenstand des erteilten und insoweit im Rahmen des Hauptantrags auch verteidigten Patentanspruchs 1 zunächst durch den Zeitpunkt der Initialisierung des Zeitgebers. Im Gegensatz zum Stand der Technik gemäß der Druckschrift K6/WALKE wird der Timer nicht beim Versenden der den N-Rahmen entsprechenden Protokolldateneinheiten, sondern bereits beim Empfang der Dienstdateneinheit durch die Datensicherungsschicht (data link layer) initialisiert (Merkmal T.4Rest: „… initializing a discard timer (300) … when said service data unit is received by said data link layer …“).

155 Eine solche Maßnahme erschöpft sich in der Festlegung eines geeigneten Zeitpunktes für den Start des Timers. Der Fachmann versteht, dass das in der Druckschrift K6/WALKE offenbarte Merkmal, wonach der Timer beim Versenden des N-Rahmens initialisiert wird, hinsichtlich des Zeitpunktes der Initialisierung nicht zwingend ist und der Startzeitpunkt grundsätzlich beliebig gewählt werden kann, sofern er sich überhaupt nur auf den N-Rahmen bezieht. Dies setzt – wie für den Fachmann unschwer zu erkennen – lediglich voraus, dass der N-Rahmen zu diesem Zeitpunkt identifizierbar ist, hier also insbesondere in der Datensicherungsschicht des Senders zur Verfügung steht. In Abhängigkeit von der getroffenen Festlegung ist dann lediglich die maximale Zeitverzögerung (= Zeit bis zum Ablauf des Abwurf-Zeitgebers = Differenz zwischen Initialisierung und frühestem Zeitpunkt der Verwerfung der Datenpakete) anzupassen. Dies lässt sich vom Fachmann auch ohne Weiteres auf die den N-Rahmen entsprechenden Protokolldateneinheiten übertragen.

156 Den Abwurf-Zeitgeber – wie in Merkmal T.4 vorgesehen – zum frühesten möglichen Zeitpunkt zu initialisieren, nämlich zu dem Zeitpunkt, in dem die Dienstdateneinheit (210) durch die Datensicherungsschicht (60a) empfangen wird, stellt sich für den Fachmann als nahe liegende Lösung dar, wenn er in Betracht zieht, dass die Dienstdateneinheiten in Sender und Empfänger jeweils als Ganzes verworfen werden sollen. Unter diesen Umständen kommt es nämlich nicht mehr auf einen zeitlichen Zusammenhang mit der Protokolldateneinheit, sondern mit der Dienstdateneinheit an. Hierdurch kann der Aufwand für den Abwurf-Zeitgeber allein schon dadurch wesentlich reduziert werden, dass nicht für jede Protokolldateneinheit ein separater Abwurf-Zeitgeber implementiert werden muss. Insoweit führen zur Überzeugung des Senats schon reine Zweckmäßigkeitserwägungen, die der Fachmann routinemäßig anstellt, zu dem Merkmal T.4Rest.

157 Darüber hinaus unterscheidet sich die Lehre des verteidigten Patentanspruchs 1 vom Stand der Technik gemäß der Druckschrift K6/WALKE durch die ausdrückliche Angabe, dass das Verwerfen nicht nur durch den Sender, sondern auch durch den Empfänger erfolgt (Merkmal T.7Rest: „… discarding said service data unit (210) by … said receiver (250) …“).

158 Diese Maßnahme verwirklicht lediglich die auf der Hand liegende Überlegung, dass der Empfänger auf ein Datenpaket nicht mehr warten braucht bzw. die weitere Übertragung eines Datenpakets auf der Empfängerseite nicht mehr erwarten kann, wenn die für das betreffende Datenpaket relevante maximale Zeitverzögerung erreicht bzw. überschritten ist. Man könnte zwar versuchen, eine Dienstdateneinheit aus möglicherweise bereits korrekt empfangenen Protokolldateneinheiten zusammenzusetzen, dies erfordert aber einen vergleichsweise großen Rechen- und damit Zeitaufwand, der in Echtzeitanwendungen kaum zur Verfügung steht. Darüber hinaus ist es für den Fachmann ohne Weiteres einsichtig, dass der auf Empfängerseite für eine Dienstdateneinheit reservierte Speicherplatz spätestens dann freigegeben werden sollte, wenn feststeht, dass er nicht mehr sinnvoll mit korrekt empfangenen Datenpaketen gefüllt werden kann. Der zunächst reservierte Speicherplatz wird nachfolgend für später übertragene Dienstdateneinheiten benötigt und bedarf schon deshalb der Freigabe, mithin des Verwerfens von nicht korrekt empfangenen Dienstdateneinheiten (Merkmal T.7Rest). Das Verwerfen durch den Empfänger erschöpft sich insoweit in einer rein handwerklichen Maßnahme, die der Fachmann im Kontext des Anwendungsgebietes der Erfindung ohnehin vorsieht.

159 Somit wird mit dem Patentanspruch 1 gemäß Hauptantrag eine Lehre beansprucht, die ausgehend von der Druckschrift K6/WALKE durch routinemäßige Zweckmäßigkeitserwägungen dem Fachmann nahe gelegt ist. Der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag beruht unter diesen Umständen nicht auf einer erfinderischen Tätigkeit.

160 b) Soweit sich der Gegenstand des Nebenanspruchs 11 (Sender) von der oben erläuterten Lehre der Druckschrift K6/WALKE dadurch unterscheidet, dass der Abwurf-Zeitgeber initialisiert wird, wenn die Dienstdateneinheit durch die Datensicherungsschicht empfangen wird (Merkmal S.5Rest: „… being initialized when said service data unit (210) is received by said data link layer (60a) …“), so gelten die Erwägungen unter II.1.a1 entsprechend. Ausgehend davon, dass nach Zeitablauf eine Dienstdateneinheit als Ganzes verworfen wird, und geleitet von dem Wunsch nach möglichst aufwandsarmer Gestaltung liegt es zur Überzeugung des Senats für den Fachmann auf der Grundlage seines Fachwissen nahe, den Zeitgeber beim Empfang der zu übertragenden Dienstdateneinheit im Sender zu initialisieren.

161 Unter diesen Umständen beruht auch der Gegenstand des Nebenanspruchs 11 nicht auf einer erfinderischen Tätigkeit.

162 c) Die gegenüber dem erteilten Patentanspruch 19 vorgenommene Änderung des Anspruchs durch Einfügung der Wörter „when said service data unit is received by said data link layer“ (Teil des Merkmals M.4) ist zulässig. Die Einfügung, die eine Einschränkung des Verfahrensanspruchs darstellt, ist durch den Gesamtoffenbarungsinhalt von Anmeldung und erteiltem Patent gestützt. Dasselbe Teilmerkmal ist in den Nebenansprüchen 1 (Merkmal T.4) und 11 (Merkmal S.5) enthalten und der Fachmann erkennt aus dem Zusammenhang ohne Weiteres, dass die Festlegung des Initialisierungszeitpunktes auch für das Verfahren gelten soll.

163 Von der oben erläuterten Lehre der Druckschrift K6/WALKE unterscheidet sich der Gegenstand des Nebenanspruchs 19 (Verfahren) gerade durch das eingefügte Teilmerkmal, dass der Abwurf-Zeitgeber genau dann initialisiert wird, wenn die Dienstdateneinheit durch die Datensicherungsschicht empfangen wird (Merkmal M.4Rest: „… initializing a discard timer (300) … when said service data unit is received by said data link layer …“). Hierfür gelten aber die Erwägungen unter II.1.a1 und II.1b entsprechend.

164 Auch der Gegenstand des Nebenanspruchs 19 beruht folglich nicht auf einer erfinderischen Tätigkeit.

165 2. Mit Hilfsantrag 1 verteidigt die Beklagte das Streitpatent mit den erteilten Patentansprüchen 1 bis 10 (Telekommunikationssystem) sowie den Patentansprüchen 17 bis 21 (Verfahren) gemäß Hilfsantrag 2.

166 Die selbständigen Ansprüche 1 und 17 gemäß Hilfsantrag 1 erweisen sich mangels erfinderischer Tätigkeit als nicht patentfähig (Art. II § 6 Abs. 1 Nrn. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ).

167 a) Der Gegenstand des erteilten Patentanspruchs 1 ist – wie oben unter II.1.a im Einzelnen ausgeführt – mangels Beruhens auf einer erfinderischen Tätigkeit nicht patentfähig.

168 b) Der selbständige Nebenanspruch 17 betrifft ein Verfahren zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger. Er umfasst die Merkmale der erteilten Verfahrensanspruchs 19 und des auf ihn unmittelbar rückbezogenen Unteranspruchs 21.

169 Er ist zulässig, da er insoweit bereits Teil des erteilten Patents ist, und lässt sich wie folgt in Merkmale gliedern:

170 M.1 A method for transmitting data packets over an air interface to a receiver (250) using a semi-reliable retransmission protocol that utilizes selective repeat automatic repeat request, said method comprising:

171 M.2 receiving, by a data link layer (60a) within said transmitter (200), a service data unit (210) containing a plurality of said data packets;

172 M.3 segmenting the service data unit (210) containing a plurality of said data packets into at least one protocol data unit (220);

173 M.4’ initializing a discard timer (300) within said transmitter for monitoring the transmission timeout of said service data unit (210) to said receiver (250);

174 M.5 transmitting said at least one protocol data unit (220) from said transmitter (200) to said receiver (250) over said air interface; and

175 M.6 discarding said service data unit (210) by said transmitter when an acknowledgment message (270) is not received for each said at least one protocol data unit (220) and said discard timer (300) expires,

176 wherein said step of discarding further comprises the step of:

177 M.7 transmitting a "move receiving window" request message from said transmitter (200) to said receiver (250)

178 M.7.1 upon expiration of said discard timer (300) and

179 M.7.2 said acknowledgment message (270, 285) for each said at least one protocol data unit (220) has not been received.

180 Wie schon unter II.1 dargelegt, ist aus der Druckschrift K6/WALKE ein Verfahren mit den Schritten M.1 bis M.3, M.4‘, M.5 und M.6 bereits bekannt. Das Merkmal M.4‘ entspricht vollständig dem oben als „M.4teilweise“ bezeichneten Teilmerkmal.

181 Die hinzugefügte Merkmalsgruppe M.7, wonach eine Aufforderungsnachricht zur „Empfangsfensterverschiebung“ von dem Sender (200) an den Empfänger (250) bei Ablaufen des Abwurf-Zeitgebers (300) übertragen wird, wenn die Bestätigungsnachricht (270, 285) für jede der mindestens einen Protokolldateneinheit (220) nicht empfangen worden ist, kann die Patentfähigkeit des Gegenstandes nicht begründen.

182 Denn aus der Druckschrift K6/WALKE ist dem Fachmann für das dort beschriebene ARQ-Verfahren bereits bekannt, dass der Sender dem Empfänger immer dann eine Mitteilung in Form eines sogenannten Delay-Befehls übermittelt, wenn die maximale Verzögerung für eine nicht korrekt übertragene ATM-Zelle erreicht ist und die ATM-Zelle danach nicht mehr weiter übertragen wird (Spalte 12, Zeile 51 bis Spalte 13, Zeile 9). Auf der Grundlage des Delay-Befehls, den der Empfänger zugleich als Aufforderung zur Empfangsfensterverschiebung versteht, reagiert der Empfänger und verschiebt sein Empfangsfenster entsprechend. Der Fachmann kennt diesen etablierten Verfahrensschritt auch aus anderen Veröffentlichungen, wie z. B. den Druckschriften K8/TANENBAUM (Abschnitt 3.4 SLIDING WINDOWS PROTOCOLS) und K7/BAKKER.

183 Der Gegenstand des Patentanspruchs 17 beruht mithin ebenfalls nicht auf einer erfinderischen Tätigkeit.

184 3. Mit Hilfsantrag 2 verteidigt die Beklagte das Streitpatent mit selbständigen Patentansprüchen 1 (Telekommunikationssystem), 10 (Sender) und 17 (Verfahren) und diesen jeweils nachgeordneten Unteransprüchen.

185 Die Gegenstände der selbständigen Ansprüche 1 und 17 gemäß Hilfsantrag 2 erweisen sich mangels erfinderischer Tätigkeit als nicht patentfähig (Art. II § 6 Abs. 1 Nrn. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ). Anspruch 10 ist gegenüber dem erteilten Patent unzulässig geändert.

186 a) Der zulässige Patentanspruch 1 betrifft ein Telekommunikationssystem zur Übertragung von Datenpaketen unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls. Er fasst die Merkmale der erteilten Patentanspruchs 1 und des auf ihn unmittelbar rückbezogenen Unteranspruchs 5 zusammen und umfasst somit die Merkmale T.1 bis T.7.2 gemäß Hauptantrag sowie die zusätzliche Merkmalsgruppe

187 wherein said transmitter (200) further comprises:

188 T.8 means for transmitting a "move receiving window" request message to said receiver (250)

189 T.8.1 when said discard timer (300) expires and

190 T.8.2 said acknowledgment message (270, 285) for each said at least one protocol data unit (220) has not been received.

191 Diese Merkmalsgruppe entspricht vollinhaltlich den Merkmalen M.7 bis M.7.1 des Anspruchs 17 gemäß Hilfsantrag 1, so dass diesbezüglich die Ausführungen betreffend die Patentfähigkeit unter II.2.b entsprechend gelten.

192 Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2 beruht mithin ebenfalls nicht auf einer erfinderischen Tätigkeit.

193 b) Der Patentanspruch 10 betrifft einen Sender zur Übertragung von Datenpaketen über eine Funkschnittstelle an einen Empfänger. Er umfasst neben den Merkmalen des erteilten Anspruchs 11 zusätzlich das Merkmal:

194 S.7 means for transmitting a "move receiving window" request message to said receiver (250) when said discard timer (300) expires and said acknowledgment message (270, 285) for each said at least one protocol data unit (220) has not been received.

195 Dieses Merkmal weicht vom Wortlaut des auf den Nebenanspruch 11 rückbezogenen Unteranspruchs 14 dadurch ab, dass nicht eine „discard message“ (Abwurf-Nachricht), sondern eine „move receiving window request message“ (Aufforderungsnachricht zur Empfangsfensterverschiebung) an den Empfänger übertragen wird.

196 Ein Sender, der derart ausgestaltet ist, dass er eine „move receiving window request message“ an den Empfänger überträgt, ist jedoch nicht Gegenstand des erteilten Patents, womit sich die hilfsweise verteidigte Fassung des Patentanspruchs 10 als unzulässig erweist.

197 c) Patentanspruch 17 gemäß Hilfsantrag 2 ist mit dem ist Patentanspruch 17 gemäß Hilfsantrag 1 identisch, so dass die Ausführungen unter II.2.b zu verweisen ist.

198 4. In den selbständigen Ansprüchen 1, 11 und 19 bzw. 1, 10 und 17 der Hilfsanträge 3 und 4 ist gegenüber der erteilten Fassung neben weiteren Änderungen und abgesehen von inhaltlich unbedeutenden sprachlichen Abwandlungen jeweils die Angabe

199 “… data link layer (60a) segmenting said service data unit (210) into at least one protocol data unit (220) …”

200 durch die Angabe

201 “… data link layer (60a) concatenating said plurality of service data units (210) into one protocol data unit (220) …”

202 ersetzt (Unterstreichungen hinzugefügt). An die Stelle des Segmentierens einer Dienstdateneinheit in mindestens eine Protokolldateneinheit tritt somit eine Verknüpfung von mehreren Dienstdateneinheiten zu einer Protokolldateneinheit.

203 Dass eine Protokolldateneinheit auch Daten aus mehreren Dienstdateneinheiten durch Verknüpfung umfassen kann, ist zwar in der Patentschrift als mögliche Alternative angegeben (vgl. Absatz 0022), aber in dieser Form in keiner Weise, weder als Sachanspruch noch als Verfahrensanspruch beansprucht worden. Diesen - als solchen auch ursprünglich offenbarte – Aspekt nunmehr zum Gegenstand der Ansprüche zu machen, führt schon für sich genommen dazu, dass nunmehr völlig andere Gegenstände beansprucht werden, als sie durch das erteilte Patent geschützt sind (aliud). Denn der Begriff der Segmentierung in mindestens eine Protokolldateneinheit umfasst den Begriff der Verknüpfung mehrerer Protokolldateneinheiten nicht.

204 Die vorgenommenen Änderungen führen dadurch zu einer unzulässigen Erweiterung des Schutzbereichs des Patents (Art. II § 6 Abs. 1 Nr. 4 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. d EPÜ).

205 Zur Zulässigkeit der weiteren Änderungen in den Ansprüchen der Hilfsanträge 3 und 4 bedarf es unter diesen Umständen keiner Entscheidung.

206 5. Mit Hilfsantrag 5 verteidigt die Beklagte das Streitpatent mit selbständigen Patentansprüchen 1 (Telekommunikationssystem), 8 (Sender) und 14 (Verfahren) und diesen jeweils nachgeordneten Unteransprüchen.

207 Die Gegenstände der selbständigen Ansprüche gemäß Hilfsantrag 5 erweisen sich mangels erfinderischer Tätigkeit als nicht patentfähig (Art. II § 6 Abs. 1 Nrn. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ).

208 a) Der zulässige Patentanspruch 1 betrifft ein Telekommunikationssystem zur Übertragung von Datenpaketen unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls. Er ist inhaltlich weitgehend identisch mit dem erteilten Patentanspruch 7, der wegen der direkten und indirekten Rückbeziehungen insgesamt die Merkmale der Ansprüche 1, 5, 6 und 7 kombiniert.

209 Zu den Merkmalen T.1 bis T.8.2 (vgl. Patentanspruch 1 gemäß Hilfsantrag 2) treten zusätzlich die Merkmale:

210 wherein said receiver (250) further comprises:

211 T.9 a receiver buffer (260) for storing said at least one protocol data unit (220), said at least one protocol data unit (220) being removed from said receive buffer (260) when said “move receiving window” request message (280) is received,

212 wherein said transmitter (200) further comprises:

213 T.10 a receive timer for monitoring a reception time of said “move receiving window” request message (280), said receive timer being initialized when said “move receiving window“ request message (280) is transmitted by said transmitter (200), said transmitter (200) retransmitting said “move receiving window“ request message (280) to said receiver (250) if said receiver timer expires and a “move receiving window“ request acknowledgment message (270, 285) has not been received by said transmitter (200).

214 a1) Das Merkmal T.9 verlangt, dass im Empfänger zusätzlich ein Empfangszwischenspeicher zum Speichern der mindestens einen Protokolldateneinheit vorgesehen ist, wobei die mindestens eine Protokolldateneinheit aus dem Empfangszwischenspeicher entfernt wird, wenn eine Aufforderungsnachricht zur Empfangsfensterverschiebung empfangen wird.

215 Dies erschöpft sich aber in einer Selbstverständlichkeit, da ein Empfänger, der am Selective-Repeat-ARQ-Verfahren teilnehmen will, stets über einen derartigen Empfangszwischenspeicher verfügen muss. Anders kann die Rekonstruktion der Dienstdateneinheit auf der der Grundlage der empfangenen Protokolldateneinheiten auf Empfängerseite nicht erfolgen. Das Merkmal ist für den Fachmann folglich zwingend für das Funktionieren des Systems.

216 Das Beruhen auf einer erfinderischen Tätigkeit kann hieraus nicht abgeleitet werden.

217 a2) Das Merkmal T.10 verlangt, dass im Sender ein Empfangszeitgeber („receive timer“) zur Überwachung einer Empfangszeit der Aufforderungsnachricht zur Empfangsfensterverschiebung vorgesehen ist, wobei der Empfangszeitgeber initialisiert wird, wenn die Aufforderungsnachricht zur Empfangsfensterverschiebung durch den Sender übertragen wird, und wobei der Sender die Aufforderungsnachricht zur Empfangsfensterverschiebung an den Empfänger erneut überträgt, wenn der Empfangszeitgeber abläuft und eine Aufforderungsnachricht zur Empfangsfensterverschiebung durch den Sender nicht empfangen worden ist (Merkmal T.10).

218 Dieses Merkmal ist dem Fachmann ausgehend von der Druckschrift K6/WALKE durch sein allgemeines Fachwissen, wie es unter anderem durch die Druckschrift K8/TANENBAUM belegt ist, nahe gelegt. Aus der Druckschrift K8/TANENBAUM ergibt sich nämlich, dass es zu den gängigen Verfahren gesicherter Datenübertragung nach dem ARQ-Prinzip gehört, im Sender innerhalb einer bestimmten Zeitspanne eine Bestätigungsnachricht vom Empfänger zu erwarten (vgl. T8/TANENBAUM, Absatz am Übergang von Seite 200 auf Seite 202). Wird eine solche Bestätigungsnachricht nicht empfangen, erfolgt regelmäßig ein zweiter oder weitere Sendeversuche für die Ursprungsnachricht.

219 Das Merkmal T.10 beschreibt lediglich die Anwendung dieses allgemeinen Ansatzes auf die vom Sender abgesetzte Aufforderungsnachricht zur Empfangsfensterverschiebung im Empfänger. Auch hierin kann eine erfinderische Tätigkeit nicht gesehen werden.

220 a3) Auch die Kombination der Merkmale T.1 bis T.10 insgesamt liegt ausgehend von der Druckschrift K6/WALKE für den Fachmann nahe, so dass der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 3 insgesamt nicht auf einer erfinderischen Tätigkeit beruht.

221 b) Der Patentanspruch 8 betrifft einen Sender zur Übertragung von Datenpaketen. Er ist inhaltlich weitgehend identisch mit dem erteilten Patentanspruch 15, der wegen der direkten und indirekten Rückbeziehungen insgesamt die Merkmale der Ansprüche 11, 14 und 15 kombiniert. Das Merkmal des Patentanspruchs 14 ist allerdings – wie in den Hilfsanträge 2 und 4 – wieder dahingehend abgewandelt, dass statt einer „discard message“ (Abwurf-Nachricht) eine „move receiving window request message“ (Aufforderungsnachricht zur Empfangsfensterverschiebung) an den Empfänger übertragen wird.

222 Dies führt wie beim Anspruch 10 gemäß Hilfsantrag 2 dargelegt zur Unzulässigkeit (vgl. hierzu Ausführungen unter II.3.b).

223 c) Der zulässige Patentanspruch 14 betrifft das Verfahren zur Übertragung von Datenpaketen. Er ist inhaltlich identisch mit dem erteilten Patentanspruch 22, der wegen der direkten und indirekten Rückbeziehungen insgesamt die Merkmale der Ansprüche 19, 21 und 22 kombiniert.

224 Zu den Merkmalen M.1 bis M.7.2 (vgl. Patentanspruch 17 gemäß den Hilfsanträgen 1 und 2) treten zusätzlich die Merkmale:

225 M.8 initializing a receive timer upon transmission of said "move receiving window" request message; and

226 M.9 retransmitting said "move receiving window" request message to said receiver (250) if said receiver (250) timer expires prior to receipt of a discard acknowledgment message (270, 285) from said receiver (250).

227 Mithin soll ein Empfangszeitgeber bei Übertragung der Aufforderungsnachricht zur „Empfangsfensterverschiebung“ initialisiert werden und die Aufforderungsnachricht zur Empfangsfensterverschiebung erneut an den Empfänger übertragen werden, wenn der Empfangszeitgeber vor Empfang einer Abwurfbestätigungsnachricht von dem Empfänger abläuft.

228 Dies entspricht vollumfänglich dem Merkmal T.10 des Patentanspruchs 1 gemäß Hilfsantrag 5. Zur patentrechtlichen Bewertung gilt das unter II.5.a2 zu diesem Merkmal Ausgeführte entsprechend.

229 Das zusätzliche Merkmal kann das Beruhen auf einer erfinderischen Tätigkeit nicht begründen.

230 6. Mit Hilfsantrag 6 verteidigt die Beklagte das Streitpatent mit selbständigen Patentansprüchen 1 (Telekommunikationssystem), 7 (Sender) und 12 (Verfahren) und diesen jeweils nachgeordneten Unteransprüchen.

231 Die Gegenstände der selbständigen Ansprüche 1 und 12 gemäß Hilfsantrag 6 erweisen sich als patentfähig. Der Nichtigkeitsgrund der fehlenden Patentfähigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a EPÜ) steht dem Hilfsantrag 6 nicht entgegen. Anspruch 7 ist gegenüber dem erteilten Patent unzulässig geändert.

232 a) Der zulässige Patentanspruch 1 betrifft ein Telekommunikationssystem zur Übertragung von Datenpaketen unter Verwendung eines halbzuverlässigen Übertragungswiederholungsprotokolls. Er umfasst die Merkmale des erteilten Patentanspruch 7, der wegen der direkten und indirekten Rückbeziehungen insgesamt die Merkmale der Ansprüche 1, 5, 6 und 7 kombiniert, sowie die Merkmale des auf den erteilten Patentanspruch 1 rückbezogenen Unteranspruchs 10.

233 Zu den Merkmalen T.1 bis T.10 (vgl. Patentanspruch 1 gemäß Hilfsantrag 5) treten zusätzlich die Merkmale:

234 T.11 an interval timer within said transmitter (200) for monitoring a time interval between an arrival time of said service data unit (210) at said data link layer (60a) and an arrival time of a successive service data unit (210) at said data link layer (60a),

235 T.12 said interval timer being first initialized when said service data unit (210) is received by said data link layer (60a),

236 T.13 said successive service data unit (210) being time stamped with the current value of said interval timer when said successive service data unit (210) is received by said data link layer (60a) and said discard timer (300) has not expired.

237 Danach umfasst das Telekommunikationssystem zusätzlich einen Intervallzeitgeber innerhalb des Senders zur Überwachung eines Zeitintervalls zwischen einer Ankunftszeit der Dienstdateneinheit in der Datensicherungsschicht und einer Ankunftszeit einer darauffolgenden Dienstdateneinheit in der Datensicherungsschicht (T.11), wobei der Intervallzeitgeber erstmalig initialisiert wird, wenn die Dienstdateneinheit durch die Datensicherungsschicht empfangen wird (T.12) und die darauffolgende Dienstdateneinheit mit dem aktuellen Wert des Intervallzeitgebers zeitgestempelt wird, wenn die darauffolgende Dienstdateneinheit durch die Datensicherungsschicht empfangen wird und der Abwurf-Zeitgeber nicht abgelaufen ist (T.13).

238 Für diese Merkmale fehlen im Stand der Technik, soweit er von den Klägerinnen in das Verfahren eingeführt wurde jegliche Vorbilder und Anregungen. Keine der in Betracht gezogenen Druckschriften K1 bis K15 beschäftigen sich im Zusammenhang mit dem „selective repeat automatic repeat request“ (SR-ARQ) mit der Überwachung eines Zeitintervalls zwischen einer Ankunftszeit der Dienstdateneinheit in der Datensicherungsschicht und einer Ankunftszeit einer darauffolgenden Dienstdateneinheit in der Datensicherungsschicht mit Hilfe eines Intervallzeitgebers (Merkmal T.11), der Initialisierung eines solchen Intervallzeitgebers (Merkmal T.12) und der Anbringung eines Zeitstempels an den Dienstdateneinheiten, der Auskunft über den aktuellen Wert des Intervallzeitgebers gibt (Merkmal T.13).

239 Es fehlt zur Überzeugung des Senats auch an Anregungen aus dem Fachwissen des hier angesprochenen Fachmanns.

240 Die Kombination der Merkmale T.1 bis T.13 ist neu und beruht auch auf einer erfinderischen Tätigkeit.

241 b) Der Patentanspruch 7 betrifft einen Sender zur Übertragung von Datenpaketen. Er umfasst die Merkmale des erteilten Patentanspruch 15, der wegen der direkten und indirekten Rückbeziehungen insgesamt die Merkmale der Ansprüche 11, 14 und 15 kombiniert, sowie die Merkmale des auf den erteilten Patentanspruch 11 rückbezogenen Unteranspruchs 18.

242 Das Merkmal des Patentanspruchs 14 ist allerdings – wie in den Hilfsanträgen 2, 4 und 5 – wieder dahingehend abgewandelt, dass statt einer „discard message“ (Abwurf-Nachricht) eine „move receiving window request message“ (Aufforderungsnachricht zur Empfangsfensterverschiebung) an den Empfänger übertragen wird.

243 Dies führt wie beim Anspruch 10 gemäß Hilfsantrag 2 zur Unzulässigkeit (vgl. hierzu Ausführungen unter II.3.b).

244 c) Der zulässige Patentanspruch 12 betrifft ein Verfahren zur Übertragung von Datenpaketen. Er umfasst die Merkmale des erteilten Patentanspruch 19 und der auf ihn unmittelbar rückbezogenen Unteransprüche 21, 22 und 23.

245 Zu den Merkmalen M.1 bis M.9 (vgl. Patentanspruch 14 gemäß Hilfsantrag 5) treten zusätzlich die Merkmale:

246 M.10 initializing an interval timer upon receipt of said service data unit (210) by a data link layer (60a) within said transmitter (200);

247 M.11 receiving a successive service data unit (210) by said data link layer (60a); and

248 M.12 appending a time stamp to said successive service data unit (210) received by said data link layer (60a), said time stamp being the current value of said interval timer when said discard timer (300) has not expired.

249 Danach umfasst das Verfahren zusätzlich die Verfahrensschritte des Initialisierens eines Intervallzeitgebers bei Empfang der Dienstdateneinheit durch eine Datensicherungsschicht innerhalb des Senders (M.10), des Empfangens einer darauf folgenden Dienstdateneinheit durch die Datensicherungsschicht (M.11) und des Anhängen eines Zeitstempels an die durch die Datensicherungsschicht empfangene darauffolgende Dienstdateneinheit, wobei der Zeitstempel der aktuelle Wert des Intervallzeitgebers ist, wenn der Abwurf-Zeitgeber nicht abgelaufen ist (M.11).

250 Diese Merkmale entsprechen inhaltlich den Merkmalen T.11 bis T.13. Die Erwägungen in Bezug auf diese Merkmale unter II.6.a gelten mutatis mutandis auch für die Merkmale M.10 bis M.12.

251 d) Die den patentfähigen selbständigen Patentansprüchen 1 und 12 nachgeordneten Unteransprüche 2 bis 6, 13 und 14 gestalten die Lehren der jeweils in Bezug genommenen Patentansprüche weiter aus und erschöpfen sich nicht nur in Selbstverständlichem.

252 Die Unteransprüche 8 bis 11 fallen mit dem unzulässigen Patentanspruch 7, da sie ebenfalls das unzulässige abgewandelte Merkmal des erteilten Patentanspruchs 14 umfassen.

253 7. Der Gegenstand des Streitpatents geht auch nicht über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus (Art. 138 Abs. 1 lit. c EPÜ i. V. m. Art. II § 6 Abs. 1 Nr. 3 IntPatÜG).

254 Die Klägerin zu 1 macht neben fehlender Patentfähigkeit geltend (vgl. Klageschriftsatz vom 22. Februar 2012, Seite 40, Ziffer VIII), dass der erteilte Anspruch 1 des Streitpatents dadurch unzulässig gegenüber der ursprünglichen Anmeldung geändert worden sei, dass vom Wortlaut des Anspruchs auch solche Lehren erfasst seien, bei denen nicht für jede einzelne Protokolldateneinheit eine Bestätigungsnachricht übertragen werden würde, sondern beispielsweise eine zusammengefasste Bestätigungsnachricht für mehrere Protokolldateneinheiten (Merkmal T.6.2).

255 Das beanstandete Merkmal, das auch in dem Patentanspruch 1 gemäß Hilfsantrag 6 enthalten ist, ist jedoch in der beanspruchten Form in der ursprünglichen Anmeldung offenbart. In der Beschreibung der ursprünglich eingereichten Unterlagen - deren Inhalt mit demjenigen der veröffentlichten Fassung der Anmeldung übereinstimmt - wird nämlich ausgeführt:

256 „If, and when, a PDU 220 is correctly received, the data link layer 60b of the receiver 250 transmits an acknowledgment message 270 to the data link layer 60a of the transmitter 200, informing the transmitter 200 that the PDU 220 was correctly received.“

257 (vgl. K3a, Seite 8, Zeilen 11-14). Dies entspricht inhaltlich vollständig dem Merkmal T.6.2. Dem Wortlaut des in der ursprünglichen Anmeldung enthaltenen Anspruchs 1, der hiervon abweicht, kommt keine ausschlaggebende Bedeutung zu (zuletzt BGH, Urteil vom 27. Mai 2014 – X ZR 2/13 - Analog-Digital-Wandler, Rn. 18).

258 Soweit die Klägerinnen weiter argumentieren, dass eine unzulässige Änderung darin zu sehen sei, dass der Anspruch 1 in der erteilten Fassung – und damit entsprechend der Patentanspruch 1 gemäß Hilfsantrag 6 – auch vom Empfänger an den Sender übermittelte Bestätigungen umfasse, die nicht positiv den erfolgreichen Empfang eines Datenpakets (Protokolldateneinheit), sondern auch den „Schlecht-Empfang“ signalisieren, so kann auch dies nicht durchgreifen. Der Anspruch lässt nämlich offen, ob Negativ-Meldungen gesendet werden oder nicht. Dies war auch schon ursprünglich so offenbart. Auch wurde offen gelassen, ob im Falle eines „Schlecht-Empfangs“ eine Meldung an den Sender geschickt wird oder nicht.

259 8. Nach alledem war das Patent – wie geschehen – insoweit für nichtig zu erklären, wie es über die Ansprüche 1 bis 6 und 12 bis 14 gemäß Hilfsantrag 6 hinausgeht.

260 Die aus dem Tenor ersichtliche, gegenüber dem Hilfsantrag 6 geänderte Nummerierung der dort enthaltenen Ansprüche 12 bis 14 sowie die Anpassung der Rückbezüge in den dortigen Unteransprüchen 8 und 9 hat der Senat mit Einwilligung der Beklagten vorgenommen.

III.

261 Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 Satz 1, 1. Alt. ZPO. Die Entscheidung über die vorläufige Vollstreckbarkeit erfolgt gemäß § 99 Abs. 1 PatG i. V. m. § 709 ZPO.
