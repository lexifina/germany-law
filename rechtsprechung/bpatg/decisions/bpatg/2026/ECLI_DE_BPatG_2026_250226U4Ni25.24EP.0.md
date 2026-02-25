---
ecli: "ECLI:DE:BPatG:2026:250226U4Ni25.24EP.0"
court: "Bundespatentgericht"
aktenzeichen: "4 Ni 25/24 (EP)"
decided: "2026-02-25"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/JURE269032394.xml"
neuris_doknr: "JURE269032394"
---

# Bundespatentgericht, 4 Ni 25/24 (EP) vom 2026-02-25

## Tenor

In der Patentnichtigkeitssache

…

betreffend das europäische Patent 1 354 491

(DE 601 32 716)

hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche Verhandlung vom 25. Februar 2026 durch die Richterin Werner M. A. als Vorsitzende, den Richter Dipl.-Phys. Univ. Dr. Haupt, den Richter Dipl.-Ing. Tischler, die Richterin Wagner und die Richterin Dipl.-Ing. Hackl

für Recht erkannt:

I. Das europäische Patent 1 354 491 wird mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für nichtig erklärt.

II. Die Beklagte trägt die Kosten des Rechtsstreits.

III. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.

## Tatbestand

1 Die Klägerin strebt mit ihrer Klage vom 2. August 2024 die Nichtigerklärung des europäischen Patents 1 354 491 an.

2 Die Beklagte ist eingetragene Inhaberin des in englischer Sprache auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 1 354 491 (Streitpatent), das unter Inanspruchnahme der finnischen Priorität 20002891 vom 29. Dezember 2000 am 27. Dezember 2001 angemeldet worden ist. Die Erteilung des Patents ist am 6. Februar 2008 veröffentlicht worden. Das Streitpatent wird beim Deutschen Patent- und Markenamt (DPMA) unter dem Aktenzeichen 601 32 716.0 geführt. Das Streitpatent ist laut Register am 27. Dezember 2021 durch Zeitablauf erloschen.

3 Das Streitpatent trägt in der englischen Verfahrenssprache die Bezeichnung

4 "LOCATION ESTIMATION IN WIRELESS TELECOMMUNICATION NETWORKS"

5 und in der deutschen Übersetzung

6 "Positionsschätzung in drahtlosen Telekommunikationsnetzen".

7 Das Streitpatent umfasst in der erteilten Fassung fünfzehn Patentansprüche, welches die Klägerin mit ihrer Klage im vollen Umfang angreift. Beklagte verteidigt das Streitpatent in erteilter Fassung sowie in geänderten Fassungen mit sechs Hilfsanträgen.

8 Die ein Verfahren und eine Positionsschätzvorrichtung zum Schätzen einer Position eines Empfängers in einer drahtlosen Telekommunikationsumgebung sowie einen Empfänger betreffenden unabhängigen Patentansprüche 1, 11 und 12 lauten in der Verfahrenssprache ausweislich der Streitpatentschrift:

9 1. A method for estimating a location (X) of a receiver (R, R’) in a wireless telecommunication environment (RN), the telecommunication environment comprising several channels for simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels;

10 for each of a plurality of calibration points in the wireless telecommunication environment, determining a set of calibration data (CD), each set of calibration data (CD) comprising the location (X) of the respective calibration point

11 and at least one measured signal parameter (V) for each of the several channels at that calibration point;

12 determining a set of observed signal parameters (CO), the set comprising at least one observed signal parameter (V) for each of the several channels at the location (X) of the receiver (R, R’); and

13 characterized in that the method comprises the steps of:

14 maintaining, at least partially on the basis of the sets of calibration data (CD), a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in the wireless telecommunication environment (RN);

15 determining a location estimate (LE) approximating the location (X) of the receiver (R, R’) on the basis of the statistical model (SM) and the set of observed signal parameters (CO).

16 11. A location estimating apparatus (LEM) for estimating a location (X) of a receiver (R, R’) in a wireless telecommunication environment (RN), the telecommunication environment comprising several channels for simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels;

17 characterized by:

18 a model construction module (MCM) for:

19 - receiving a set of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment, each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point; and

20 - maintaining, at least partially, on the basis of the sets of calibration data (CD), a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in the wireless telecommunication environment (RN);

21 and a location calculation module (LCM) for:

22 - receiving a set of observed signal parameters (CO), the set comprising at least one observed signal parameter (V) for each of the several channels at the location (X) of the receiver (R, R’); and

23 - determining a location estimate (LE) approximating the location (X) of the receiver (R, R’) on the basis of the statistical model (SM) and the set of observed signal parameters (CO).

24 12. A receiver (R, R’) comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

25 characterized by means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

26 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

27 In deutscher Übersetzung lauten die Patentansprüche 1, 11 und 12 entsprechend der Streitpatentschrift wie folgt:

28 1. Verfahren zum Schätzen einer Position (X) eines Empfängers (R, R’) in einer drahtlosen Telekommunikationsumgebung (RN), wobei die Telekommunikationsumgebung eine Mehrzahl von Kanälen zur gleichzeitigen Kommunikation umfasst, wobei jeder der mehreren Kanäle mindestens einen Signalparameter (V) aufweist, der sich mit der Position (X) von den anderen der mehreren Kanäle unterschiedlich verändert;

29 für jeden einer Mehrzahl von Kalibrierungspunkten in der drahtlosen Telekommunikationsumgebung, Bestimmen eines Satzes von Kalibrierungsdaten (CD), wobei jeder Satz von Kalibrierungsdaten (CD) die Position (X) des jeweiligen Kalibrierungspunkts und mindestens einen gemessenen Signalparameter (V) für jeden der mehreren Kanäle an dem Kalibrierungspunkt umfasst;

30 Bestimmen eines Satzes von beobachteten Signalparametern (CO), wobei der Satz mindestens einen beobachteten Signalparameter (V) für jeden der mehreren Kanäle an der Position (X) des Empfängers (R, R’) umfasst; und

31 dadurch gekennzeichnet, dass das Verfahren die folgenden Schritte umfasst:

32 Beibehalten, mindestens teilweise auf der Grundlage der Sätze von Kalibrierungsdaten (CD), eines statistischen Models (SM) der Signalparameter (V) der mehreren Kanäle als Funktion einer Position des Empfängers in der drahtlosen Telekommunikationsumgebung (RN);

33 Bestimmen eines Positionsschatzwerts (LE), der die Position (X) des Empfängers (R, R’) auf der Grundlage des statistischen Models (SM) und des Satzes von beobachteten Signalparametern (CO) approximiert.

34 11. Positionsschätzvorrichtung (LEM) zum Schätzen einer Position (X) eines Empfängers (R, R’) in einer drahtlosen Telekommunikationsumgebung (RN), wobei die Telekommunikationsumgebung eine Mehrzahl von Kanälen zur gleichzeitigen Kommunikation umfasst, wobei jeder der mehreren Kanäle mindestens einen Signalparameter (V) aufweist, der sich mit der Position (X) von den anderen der mehreren Kanäle unterschiedlich verändert;

35 gekennzeichnet durch:

36 ein Modellkonstruktionsmodul (MCM) zum:

37 - Empfangen eines Satzes von Kalibrierungsdaten (CD) für jeden einer Mehrzahl von Kalibrierungspunkten in der drahtlosen Telekommunikationsumgebung, wobei jeder Satz von Kalibrierungsdaten (CD) die Position (X) des jeweiligen Kalibrierungspunkts und mindestens einen gemessenen Signalparameter (V) für jeden der mehreren Kanäle an dem Kalibrierungspunkt umfasst; und

38 - Beibehalten, mindestens teilweise, auf der Grundlage der Sätze von Kalibrierungsdaten (CD) eines statistischen Models (SM) der Signalparameter (V) der mehreren Kanäle als Funktion einer Position des Empfängers in der drahtlosen Telekommunikationsumgebung (RN);

39 und ein Positionsberechnungsmodul (LCM) zum:

40 - Empfangen eines Satzes von beobachteten Signalparametern (CO), wobei der Satz mindestens einen beobachteten Signalparameter (V) für jeden der mehreren Kanäle an der Position (X) des Empfängers (R, R’) umfasst; und

41 - Bestimmen eines Positionsschätzwerts (LE), der die Position (X) des Empfängers (R, R’) auf der Grundlage des statistischen Models (SM) und des Satzes von beobachteten Signalparametern (CO) approximiert.

42 12. Empfänger (R, R’) mit einem Mittel zum Bestimmen von Sätzen von beobachteten Signalparametern (CO), wobei jeder Satz mindestens einen beobachteten Signalparameter (V) für jeden der mehreren Kanäle an der Position (X) des Empfängers (R) umfasst, wobei die mehreren Kanäle gleichzeitige Kommunikation unterstützen, wobei jeder der mehreren Kanäle mindestens einen Signalparameter (V) aufweist, der sich mit der Position (X) von den anderen der mehreren Kanäle unterschiedlich verändert;

43 gekennzeichnet durch ein Mittel zum Transportieren der Sätze von beobachteten Signalparametern (CO) zu einem Positionsberechnungsmodul (LCM) zum Bestimmen eines Positionsschätzwerts (LE), der die Position (X) des Empfängers (R) auf der Grundlage der Sätze und eines statistischen Models (SM) der Signalparameter (V) der mehreren Kanäle als Funktion einer Position des Empfängers in einer drahtlosen Telekommunikationsumgebung (RN) approximiert;

44 wobei das statistische Modell (SM) mindestens teilweise auf der Grundlage von Sätzen von Kalibrierungsdaten (CD) für jeden einer Mehrzahl von Kalibrienungspunkten [sic!] in der drahtlosen Telekommunikationsumgebung (RN) beibehalten wird, wobei jeder Satz von Kalibrierungsdaten (CD) die Position (X) des jeweiligen Kalibrierungspunkts und mindestens einen gemessenen Signalparameter (V) für jeden der mehreren Kanäle an dem Kalibrierungspunkt umfasst.

45 Die Patentansprüche 2 bis 10 und 13 bis 15 sind mittelbar bzw. unmittelbar auf die Patentansprüche 1 bzw. 12 rückbezogen. Wegen ihres Wortlauts wird auf die Streitpatentschrift Bezug genommen.

46 Die Klägerin ist der Ansicht, dass die Gegenstände der Patentansprüche 1, 11 und 12 nicht neu und nicht erfinderisch seien und beruft sich u. a. auf folgende Dokumente:

47 D5 WO 01/72060 A1, veröffentlicht am 27. September 2001,

48 Priorität vom 22. März 2000

49 D5a WO 00/18148 A1,veröffentlicht am 30. März 2000

50 D7 ETSI, GSM Technical Specification, Digital cellular telecommunications system (Phase 2+), Physical layer on the radio path, General description, GSM 05.01, Version 5.4.0, April 1998

51 D8 ETSI, GSM Technical Specification, Digital cellular telecommunications system (Phase 2+), Multiplexing and multiple access on the radio path, GSM 05.02, Version 5.1.0, August 1996

52 D9 TURLETTI, T.: A brief Overview of the GSM Radio Interface, March 1, 1996

53 D16 BERLINE, G.; PERRATORE, E.: Wireless LANs. IN: PC Magazine, Volume 11 Number 3, 11. Februar 1992, Deckblatt, Inhaltsverzeichnis, Seiten 291 bis 314.

54 Die Klägerin beantragt,

55 das europäische Patent 1 354 491 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für nichtig zu erklären.

56 Die Beklagte beantragt,

57 die Klage abzuweisen,

58 hilfsweise, die Klage abzuweisen,

59 soweit sie sich auch gegen eine der Fassungen des Streitpatents nach den Hilfsanträgen 1 bis 6 überreicht mit Schriftsatz vom 23. Mai 2025 richtet,

60 wobei die Anträge in der numerischen Reihenfolge geprüft werden sollen und

61 alle Anträge als geschlossene Anspruchsätze gestellt werden.

62 Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den Gegenstand der Patentansprüche 1, 11 und 12 in erteilter Fassung gegenüber dem Stand der Technik für patentfähig. Darüber hinaus sei das Streitpatent wenigstens in einer der hilfsweise verteidigten Fassungen nach den eingereichten Hilfsanträgen 1 bis 6 schutzfähig. Der Gegenstand des Streitpatents sei auch in den Fassungen nach den Hilfsanträgen zulässig, ursprungsoffenbart, ausführbar und wenigstens in einer der verteidigten Fassungen patentfähig.

63 Jeder der Hilfsanträge 1 bis 6 umfasst jeweils die drei einander nebengeordneten Patentansprüche 1, 11 und 12. Hilfsanträge 1 bis 5 umfassen insgesamt 15 Patentansprüche, Hilfsantrag 6 umfasst (nach Streichung des abhängigen Patentanspruchs 3) noch insgesamt 14 Patentansprüche.

64 Im Hilfsantrag 1 ist Patentanspruch 12 gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

65 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein a channel is a frequency band, wherein the several channels are received by the receiver from more than one network , wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

66 characterized by

67 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

68 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

69 Im Hilfsantrag 2 ist Patentanspruch 12 gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

70 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein a channel is a frequency band, wherein the several channels are received by the receiver from more than one network, wherein the more than one network are different types of networks , wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

71 characterized by

72 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

73 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

74 Im Hilfsantrag 3 ist Patentanspruch 12 gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

75 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein the several channels are received by the receiver from more than one network, wherein the more than one network are different types of networks, wherein the different types of networks comprise a cellular network and a wireless local-area network (WLAN) , wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

76 characterized by

77 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

78 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

79 Im Hilfsantrag 4 ist Patentanspruch 12 gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

80 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein the several channels are received by the receiver from more than one network, wherein the several channels are received using different antennas, wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

81 characterized by

82 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

83 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

84 Im Hilfsantrag 5 ist Patentanspruch 12 gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

85 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein a channel is a frequency band, , [sic!] wherein the several channels are received by the receiver from more than one network using different antennas, wherein the more than one network are different types of networks, wherein the different types of networks comprise a cellular network and a wireless local-area network (WLAN) , wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

86 characterized by

87 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

88 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

89 Im Hilfsantrag 6 ist Unteranspruch 3 gestrichen, Patentanspruch 12 ist gegenüber der erteilten Fassung wie folgt geändert (Änderungen durch Unterstreichen kenntlich gemacht):

90 12. A receiver (R, R') comprising means for determining sets of observed signal parameters (CO), each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein the several channels support simultaneous communication, each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

91 characterized by

92 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE) approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver's location in a wireless telecommunication environment (RN);

93 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN), each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point;

94 wherein the receiver (R') stores a copy of the statistical model (SM) and determines the location estimate (LE) on the basis of the copy of the statistical model (SM);

95 wherein the copy of the statistical model (SM) is compressed to a size which is manageable by the receiver.

96 Die nebengeordneten Patentansprüche 1 und 11 sind in den Hilfsanträgen 1 bis 6 jeweils inhaltlich entsprechend den jeweiligen Änderungen im Patentanspruch 12 geändert. Wegen des Wortlauts der jeweiligen Anspruchssätze der Hilfsanträge wird auf die Akte verwiesen.

97 Die Klägerin wendet sich auch gegen die Hilfsanträge. Sie sieht den Gegenstand des Streitpatents in der Fassung der jeweiligen Hilfsanträge 1 bis 6 als nicht zulässig. Sie ist zudem der Ansicht, dass die Gegenstände der Patentansprüche 1, 11 und 12 in der Fassung der jeweiligen Hilfsanträge nicht neu u. a. gegenüber den Entgegenhaltungen D5 und D5a sowie ausgehend von D5a auch nicht erfinderisch seien.

98 U. a. die Klägerin wird aus dem Streitpatent vor dem Landgericht München I,

99 Az.: …; aufgrund behaupteter Verletzung der Patentansprüche 1 und 12 des

100 Streitpatents in Anspruch genommen.

101 Der Senat hat den Parteien einen qualifizierten Hinweis vom 17. März 2025 zugeleitet und hierin Fristen zur Stellungnahme auf den Hinweis und auf etwaiges Vorbringen der jeweiligen Gegenpartei gesetzt.

102 Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen den Parteien gewechselten Schriftsätze nebst Anlagen, auf das Protokoll der mündlichen Verhandlung vom 25. Februar 2026 sowie den weiteren Akteninhalt Bezug genommen.

## Entscheidungsgründe

A.

103 Auf die zulässige Klage der Klägerin ist das Streitpatent für nichtig zu erklären. Der Gegenstand des Streitpatents erweist sich als nicht rechtsbeständig, da jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54 EPÜ gegeben ist. Auch in den Fassungen nach den Hilfsanträgen 1 bis 6 kann die Beklagte das Streitpatent nicht erfolgreich verteidigen.

I.

104 Die Klage ist zulässig.

105 1. Die Beklagte ist passivlegitimiert, da die Nichtigkeitsklage sich gegen die im Register als Patentinhaberin eingetragene Beklagte richtet, § 81 Abs. 1 Satz 2 PatG.

106 2. Die Klage vom 2. August 2024 ist auch trotz Zeitablauf des Streitpatents seit 27. Dezember 2021 zulässig.

107 Ist ein Patent durch Zeitablauf erloschen, bedarf es eines schutzwürdigen Interesses des Klägers an der Durchführung des Nichtigkeitsverfahrens, da ein Interesse der Allgemeinheit an einer Überprüfung der Rechtsbeständigkeit des Patents nicht mehr besteht (vgl. BGH, Urteil vom 20. Juni 2023 – X ZR 31/21, juris Rn. 12, Urteil vom 21. Juli 2022 - X ZR 110/21, GRUR 2022, 1628 Rn. 15 – Stammzellengewinnung).

108 Auch nach Erlöschen des Patents ist eine Nichtigkeitsklage zulässig, wenn die Klageseite ein individuelles Rechtsschutzbedürfnis an der Nichtigerklärung des Patents hat (st. Rspr.: BGH, Urteil vom 16. Mai 2024 – X ZR 62/22; Urteil vom 20. Juni 2023 – X ZR 31/21, GRUR 2023, 1178 Rn. 12f. – Leistungsüberwachungsgerät; Urteil vom 26. Januar 2021 - X ZR 24/19 – Phytase; Urteil vom 24. Mai 2016 – X ZR 28/14, juris Rn. 11 jeweils m. w. N.). Dabei begründet auch nach Ablauf der Schutzdauer eines Patents eine Verletzungsklage für den Verletzungsbeklagten, auch wenn sie nur auf den Hauptanspruch gestützt ist, ein Rechtsschutzinteresse an einer Nichtigkeitsklage regelmäßig auch in Bezug auf alle, auf diesen rückbezogenen, Unteransprüche des Patents (vgl. BGH, Urteil vom 11. August 2020 – X ZR 96/18, GRUR 2020, 1284 – Datenpaketumwandlung). Ein Rechtsschutzinteresse darf in solchen Fällen nur dann verneint werden, wenn eine Inanspruchnahme aus dem Streitpatent ernstlich nicht mehr in Betracht kommt (BGH, Beschluss vom 13. Juli 2020 – X ZR 90/18, GRUR 2020, 1074 Rn. 25 ff. – Signalübertragungssystem; Urteil vom 20. Juni 2023 – X ZR 31/21, juris Rn. 16 – Leistungsüberwachungsgerät). Maßgeblich für das Vorliegen des Rechtsschutzbedürfnisses ist der Zeitpunkt der letzten mündlichen Verhandlung (BGH, Urteil vom 13. Juli 2004 – X ZR 171/00, GRUR 2004, 849, Rn. 12 – Duschabtrennung; Urteil vom 21. Juli 2022 – X ZR 110/21, GRUR 2022, 1628 Rn. 15 – Stammzellengewinnung).

109 Das Rechtsschutzbedürfnis der Klägerin ergibt sich aus dem u. a. gegen sie aus dem Streitpatent vor dem Landgericht München I geführten Verletzungsverfahren. Zur Zeit der mündlichen Verhandlung im vorliegenden Verfahren war unstreitig das beim Landgericht München I unter dem Az.: … geführte Verletzungsverfahren gegen u. a. die Klägerin aus den Patentansprüchen 1 und 12 anhängig. Die Klägerin war damit unmittelbar einer Inanspruchnahme aus den Patentansprüchen 1 und 12 des Streitpatents ausgesetzt.

110 Auch hinsichtlich der abhängigen Ansprüche 2 bis 10 und 13 bis 15 sowie des nebengeordneten Anspruchs 11, mit dem eine Positionsschätzvorrichtung beansprucht ist, besteht ein Rechtsschutzbedürfnis.

111 Soweit es um Unteransprüche geht, hängt es in der Regel allein von Zweckmäßigkeitserwägungen ab, ob eine Verletzungsklage ausschließlich auf den Hauptanspruch oder hilfsweise auch auf Unteransprüche gestützt wird (s. a. BGH, Urteil vom 11. August 2020 – X ZR 96/18, GRUR 2020, 1284 Rn. 44 – Datenpaketumwandlung). Für nicht angegriffene Nebenansprüche gelten die für die angegriffenen abhängigen Ansprüche genannten Voraussetzungen entsprechend. Eine nur auf einzelne Patentansprüche gestützte, bereits erhobene Verletzungsklage begründet demnach grundsätzlich auch ein Rechtsschutzinteresse in Bezug auf alle Ansprüche des Patents, wenn diese inhaltlich so weitgehend übereinstimmen, dass die Verwirklichung eines Anspruchs (etwa eines Vorrichtungsanspruchs) typischerweise zur Verwirklichung der Merkmale des anderen Anspruchs (etwa eines Verfahrensanspruchs) führt (s. a. BGH, Urteil vom 11. August 2020 – X ZR 96/18, GRUR 2020, 1284 Rn. 46 – Datenpaketumwandlung).

112 Danach besteht ein Rechtsschutzbedürfnis für die Klägerin gerichtet auf die Nichtigerklärung aller Ansprüche des Streitpatents. Aus der Verletzungsklage aus dem Streitpatent gegen u. a. die Nichtigkeitsklägerin gestützt auf die Ansprüche 1 und 12 folgt für die Klägerin auch die Besorgnis, die Pateninhaberin könnte ihr Klageanliegen im Verletzungsverfahren auch auf die auf diese Ansprüche rückbezogenen abhängigen Ansprüche 2 bis 10 und 13 bis 15 stützen. Entsprechendes gilt für den nebengeordneten Anspruch 11, da dieser inhaltlich nahezu identisch ist mit den Ansprüchen 1 (Verfahren) und 12 (Empfänger), die (bislang) zur Begründung der Forderungen im Verletzungsverfahren herangezogen worden sind.

113 II. Zum Streitpatent, zum technischen Problem , zur Fachperson, zur Merkmalsgliederung und zur Auslegung

114 1. Das Streitpatent mit dem Titel "Positionsschätzung in drahtlosen Telekommunikationsnetzen" befasst sich mit einem Verfahren und Vorrichtungen zur Positionsbestimmung eines Empfängers in einer drahtlosen Telekommunikationsumgebung (Streitpatentschrift, Abs. 0001). Eine solche Positionsschätzung könne zur Bereitstellung einer Vielzahl standortabhängiger Dienste genutzt werden.

115 Laut Streitpatent sind bereits Verfahren zur Positionsbestimmung in einem Mobilfunknetz bekannt. Diese würden jedoch zusätzliche Hardware auf der Netzwerkseite erfordern, wie beispielsweise komplexe Antennenanordnungen.Als weiteren Nachteil nennt das Streitpatent, dass zudem Informationen über die Netzwerk-Infrastruktur bekannt sein müssten, um die Position eines mobilen Empfängers bestimmen zu können. Zudem müsse der mobile Empfänger senden, damit seine Position geschätzt werden könne (Abs. 0002). Gleiches gelte für bekannte Verfahren zur Positionsbestimmung mittels eines drahtlosen Netzwerks innerhalb eines Gebäudes, bei welchem ebenso Messungen an den Basisstationen notwendig seien (Abs. 0003).

116 2. Das Streitpatent betrifft vor diesem Hintergrund das technische Problem, die genannten Nachteile zu beseitigen und eine Schätzung einer Position eines Empfängers in einem drahtlosen Kommunikationsnetzwerk ohne vorherige Kenntnis über die Netzwerkinfrastruktur zu ermöglichen (Abs. 0004). Dabei solle der Empfänger, dessen Position geschätzt werden soll, zudem nicht senden müssen, um seine Position abschätzen zu können (Abs. 0009).

117 3 . Der Senat sieht als maßgebliche Fachperson einen Ingenieur oder eine Ingenieurin der Nachrichten- oder Informationstechnik mit einem universitären Master-Abschluss oder Diplom. Sie verfügt über mehrere Jahre Berufserfahrung in der Entwicklung von drahtlosen Kommunikationssystemen, insbesondere zum Thema Lokalisierung von mobilen Endgeräten.

118 4. Die nachfolgenden Ausführungen erfolgen aufgrund der im wesentlichen inhaltlichen Entsprechung der Patentansprüche 1, 11 und 12 anhand der folgenden Merkmalsgliederung des angegriffenen unabhängigen Patentanspruchs 12, an dem sich auch die Parteien bei ihren Ausführungen orientiert haben. Die maßgebliche englischsprachige Fassung stammt ebenso wie die deutschsprachige Fassung aus der Streitpatentschrift:

119 12.1 A receiver (R, R’)

12.1 Empfänger (R, R’)

12.2 comprising means for determining sets of observed signal parameters (CO),

12.2 mit einem Mittel zum Bestimmen von Sätzen von beobachteten Signalparametern (CO), wobei

12.2.1 each set comprising at least one observed signal parameter (V) for each of several channels at the location (X) of the receiver (R), wherein

12.2.1 jeder Satz mindestens einen beobachteten Signalparameter (V) für jeden der mehreren Kanäle an der Position (X) des Empfängers (R) umfasst, wobei

12.2.2 the several channels support simultaneous communication,

12.2.2 die mehreren Kanäle gleichzeitige Kommunikation unterstützen, wobei

12.2.3 each of the several channels having at least one signal parameter (V) that varies with location (X) differently from the other of the several channels:

12.2.3 jeder der mehreren Kanäle mindestens einen Signalparameter (V) aufweist, der sich mit der Position (X) von den anderen der mehreren Kanäle unterschiedlich verändert;

characterized by

gekennzeichnet durch

12.3 means for conveying the sets of observed signal parameters (CO) to a location calculation module (LCM) for determining a location estimate (LE)

12.3 ein Mittel zum Transportieren der Sätze von beobachteten Signalparametern (CO) zu einem Positionsberechnungsmodul (LCM) zum Bestimmen eines Positionsschätzwerts (LE),

12.3.1 approximating the location (X) of the receiver (R) on the basis of said sets and a statistical model (SM) of the signal parameters (V) of the several channels versus a receiver’s location in a wireless telecommunication environment (RN);

12.3.1 der die Position (X) des Empfängers (R) auf der Grundlage der Sätze und eines statistischen Models (SM) der Signalparameter (V) der mehreren Kanäle als Funktion einer Position des Empfängers in einer drahtlosen Telekommunikationsumgebung (RN) approximiert;

12.3.2 wherein the statistical model (SM) is maintained at least partially on the basis of sets of calibration data (CD) for each of a plurality of calibration points in the wireless telecommunication environment (RN),

12.3.2 wobei das statistische Modell (SM) mindestens teilweise auf der Grundlage von Sätzen von Kalibrierungsdaten (CD) für jeden einer Mehrzahl von Kalibrierungspunkten in der drahtlosen Telekommunikationsumgebung (RN) beibehalten wird,

12.3.3 each set of calibration data (CD) comprising the location (X) of the respective calibration point and at least one measured signal parameter (V) for each of the several channels at that calibration point.

12.3.3 wobei jeder Satz von Kalibrierungsdaten (CD) die Position (X) des jeweiligen Kalibrierungspunkts und mindestens einen gemessenen Signalparameter (V) für jeden der mehreren Kanäle an dem Kalibrierungspunkt umfasst.

120 5 . Die Fachperson versteht die im Patentanspruch 12 genannten Merkmale wie folgt:

121 5.1 Als Empfänger gemäß Merkmal 12.1 ist das Gerät bezeichnet, dessen Position bzw. Standort geschätzt werden soll (Abs. 0007 der Streitpatentschrift). Dieser Empfänger wird in seinen Vorrichtungsmerkmalen durch das nachfolgende Merkmal 12.2, welches ein Mittel zum Bestimmen von Sätzen von beobachteten Signalparametern beansprucht, und das Merkmal 12.3, welches ein Mittel zum Transportieren der Sätze von beobachteten Signalparametern zu einem Positionsberechnungsmodul zum Bestimmen eines Positionsschätzwerts beansprucht, in seinen Vorrichtungsmerkmalen ausgebildet. Die weiteren Merkmale 12.2.1, 12.2.2 und 12.2.3 beschreiben zu beobachtende Signalparameter an sich, während sich die Merkmale 12.3.1 bis 12.3.3 auf die Positionsbestimmung im Positionsbestimmungsmodul (LCM) beziehen.

122 5.2 Laut Streitpatent genügt es für den Empfänger, der lokalisiert werden soll, dass dieser Beobachtungen der ihn umgebenen drahtlosen Umgebung durchführt (Merkmal 12.2). Hierzu muss der Empfänger, beispielsweise ein GSM-Telefon, aber keinen Verkehrskanal empfangen. Vielmehr führt der Empfänger allein Beobachtungen auf allen verfügbaren Frequenzen durch (Abs. 0009). Das Streitpatent erläutert, dass technisch gesehen "Beobachtungen" und "Messungen" ähnlich durchgeführt werden. Um Verwechslungen zu vermeiden, wird der Begriff "Messung" im Streitpatent jedoch nur für die Kalibrierungsmessungen verwendet, während die am aktuellen Standort des Empfängers ermittelten Signalparameter als "Beobachtungen" bezeichnet werden(Abs. 0028). Die Fachperson entnimmt dem, dass die Mittel zum Bestimmen der Sätze von beobachteten Signalparametern gemäß dem Merkmal 12.2 zum Messen von verfügbaren Frequenzen in der drahtlosen Umgebung des Empfängers ausgelegt sein müssen, wobei keine aktive Verbindung von dem Empfänger zu einem Netzwerk bestehen muss. Dabei wird im Patentanspruch 12 kein Frequenzbereich, welcher beobachtet wird, angeben. Als Beispiel für einen erfindungsgemäßen Empfänger umfassend Mittel zum Bestimmen von Sätzen von beobachteten Signalparametern nennt das Streitpatent ein GSM-Telefon, welches Signalparameter von GSM-Netzen empfangen und messen kann (Abs. 0009, 0010, 0030). Dabei wird es als vorteilhaft angesehen, die bereits in einem GSM-Telefon verwendeten Zellüberwachungsroutinen zu verwenden bzw. zu modifizieren, so dass sie die verfügbaren Zellen stets umfassend überwachen (Abs. 0030). Die Fachperson sieht die Mittel zum Bestimmen von Sätzen von beobachtenden Signalparametern (CO) somit in einem GSM-Telefon verwirklicht, der Patentanspruch ist jedoch nicht auf ein solches beschränkt.

123 5.3 Merkmal 12 . 2.1 spezifiziert die Sätze von beobachteten Signalparametern (CO current observations) gemäß dem Merkmal 12.2, wobei jeder Satz mindestens einen beobachteten Signalparameter für jeden der mehreren Kanäle an der Position des Empfängers umfasst. Als möglicher Signalparameter, der, wie nachfolgend mit dem Merkmal 12.2.3 beansprucht, in Abhängigkeit eines Standorts variiert, werden in der Streitpatentschrift die Signalstärke, die Laufzeit (timing advance) und ein Fehlerverhältnis (error ratio) genannt (Abs. 0017). Als Fehlerverhältnis wird die Fachperson basierend auf den beispielhaft genannten Mobilfunknetzen eine Bitfehlerrate einer Datenübertragung annehmen. Zudem wird die Fachperson eine Messung der Signalstärke, die im Streitpatent allein zur Verdeutlichung der Erfindung verwendet wird, als vorteilhaft erkennen (Abs. 0006, 0016), da diese am Empfänger gemessen werden kann, ohne den Inhalt eines empfangenen Signals interpretieren zu müssen (Abs. 0016). Der Patentanspruch 12 ist jedoch nicht auf eine Verwendung der Signalstärke beschränkt.

124 Zumindest ein beobachteter Signalparameter wird dabei für jeden von mehreren Kanälen an der Position des Empfängers erfasst. Die Formulierung "mehrere Kanäle" versteht die Fachperson als mindestens zwei Kanäle, wobei sie dem Streitpatent weiter entnimmt, dass eine Positionsschätzung umso genauer ausgeführt werden kann, je mehr Kanäle beobachtet werden (Abs. 0025).

125 Der Begriff Kanal soll laut Streitpatent dabei eine weite Auslegung haben und mehr oder weniger dasselbe bedeuten wie eine Frequenz oder ein Frequenzband (Abs. 0016). Dabei grenzt sich das Streitpatent explizit zur allgemeinen Verwendung des Begriffes Kanal im Sinne eines Verkehrskanals ab, wobei als ein Kanal in drahtlosen Netzwerken allgemein ein zugewiesener Übertragungsbereich zu verstehen ist, über den Daten zwischen einem Endgerät und einer Basisstation ausgetauscht werden können, und welcher einen dedizierten Zeitschlitz umfassen kann. Nach Streitpatent hat in TDMA-Systemen jede Frequenz mehrere Zeitschlitze, von denen jeder einen Kanal darstellt, diese Zeitschlitze derselben Frequenz jedoch identische Informationen bezüglich dem positionsabhängigen Signalparameter liefert. Zwar kann jeder dieser Zeitschlitze als Kanal verwendet werden, jedoch werden Zeitschlitze derselben Frequenz im Sinne der Erfindung nicht als mehrere Kanäle, sondern allein als ein Kanal betrachtet (Abs. 0016). Daraus entnimmt die Fachperson, dass jeder der mehreren beobachteten Kanäle sich demzufolge in der Frequenz von anderen beobachteten Kanälen unterscheiden muss.

126 Laut Streitpatent stellen Signale dreier Sendestationen eines drahtlosen Netzwerks, wie eines GSM-Netzes, geeignete mehrere Kanäle dar (Abs. 0011). Das entspricht zudem dem grundlegenden Verständnis der Fachperson zu GSM. Der Fachperson ist aus ihrem Fachwissen zu GSM allgemein aus Lehrbüchern und GSM Technical Specifications bekannt, etwa durch die D7 bis D9 belegt, dass ein GSM-System Frequenzbereiche z. B. bei 890–915 MHz (Uplink von den Mobilgeräten zur Basisstation) und 935–960 MHz (Downlink) nutzt, wobei ein HF-Kanalabstand 200 kHz beträgt. Dadurch stehen 124 (GSM 900) bzw. 374 (DCS 1800) Funkfrequenzkanäle im GSM-System zur Verfügung (D7, Seite 16, Kapitel 9; D9, Seite 2, Abschnitt 2). Jeder der Kanäle des Downlink eines GSM-Systems stellt dabei einen erfindungsgemäßen Kanal dar, welcher einer Frequenz bzw. einem Frequenzband entspricht. Jeder Zelle wird eine Teilmenge dieser Funkfrequenzkanäle zugewiesen, wobei ein Funkfrequenzkanal zur Übertragung von Synchronisationsinformationen und des Broadcast Control Channels dient, welcher stets durch einen Empfänger beobachtet werden kann. Benachbarte Basisstationen eines GSM-Netzes senden dabei mit einem Frequenzversatz, um Interferenzen zwischen den Basisstationen zu vermeiden.Diese Auslegung wird zudem gestützt durch die im Streitpatent genannte Ausführung, wobei es als vorteilhaft angesehen wird, die bereits in einem GSM-Telefon verwendeten Zellüberwachungsroutinen zu verwenden (Abs. 0030), welche ebenso auf dem Beobachten der Broadcast Control Channel basieren.

127 Ein Verständnis des Merkmals 12.2 dahin, dass ein Kanal der Mehrzahl der Kanäle jeweils einem Frequenzband im Sinne eines, einer Anwendung zugewiesenen, gesamten Spektrums zu verstehen sei, kann die Fachperson den Erläuterungen im Streitpatents entgegen der Ansicht der Beklagten nicht entnehmen.

128 5.4 Gemäß Merkmal 12.2.2 unterstützen die mehreren Kanäle eine gleichzeitige Kommunikation, wobei das Streitpatent als eine gleichzeitige Kommunikation definiert, dass eine vom Empfänger empfangene Menge an Netzwerken gleichzeitig über mehrere Kanäle kommuniziert (Abs. 0011). Die Fachperson entnimmt dieser Definition unter Berücksichtigung der im Abs. 0009 des Streitpatents getroffenen Annahme, dass der Empfänger selbst keinen Verkehrskanal und somit keine Kommunikation mit einem oder mehreren Netzwerken benötigt, dass das eine oder die mehreren Netzwerke gleichzeitig über mehrere Kanäle zumindest Signale senden, wie zellspezifische Broadcast Signale, und der Empfänger somit mehr als ein Signal gleichzeitig beobachten kann (Abs. 0011). Dieses Verständnis steht im Einklang mit der beispielhaft beschriebenen Ausführungsform, wobei ein GSM-Telefon, das an einem GSM-Netzwerk angemeldet ist, zudem die Signalstärken anderer GSM-Netzwerke ausnutzen kann (Abs. 0009). Damit ist Merkmal 12.2.2, wonach die mehreren Kanäle gleichzeitige Kommunikation unterstützen, allein auf ein Vorliegen gleichzeitig zu beobachtender Signalparameter beschränkt zu verstehen. Das Merkmal bildet den Empfänger selbst nicht aus und umfasst auch nicht, dass die vorliegenden Signalparameter gleichzeitig gemessen werden. Vielmehr können sie, wie die Fachperson aus der Verwendung der in einem GSM-Telefon ausgeführten Zellüberwachungsroutinen ableitet, zeitnah nacheinander beobachtet werden (Abs. 0030).Wie in Figur 4B am Beispiel des GSM-Netzes dargestellt, werden Signale von mindestens zwei Sendestationen (BS) durch den Empfänger gleichzeitig empfangen, um jeweils einen Satz von beobachteten Signalparametern zur Standortbestimmung zu erfassen.

129 Auszug aus Figur 4B der Streitpatentschrift mit Kolorierung durch den Senat

130 5.5 Merkmal 12.2.3 ergänzt, dass jeder der mehreren Kanäle mindestens einen Signalparameter (V) aufweist, der sich mit der Position (X) gegenüber den anderen der mehreren Kanäle unterschiedlich verändert. Legt man die Ausführungsform gemäß der Figur 4B des Streitpatents zugrunde, so ist erkennbar, dass die beiden Basisstationen BS jeweils eine Sendestation bilden und über eine Funkschnittstelle (RI) jeweils einen Kanal bereitstellen, dessen Signalparameter am Empfänger gemessen werden. Anhand der zugrundeliegenden Zellenstruktur bzw. dem Abstand der Sendestationen (BS) vom Empfänger im Mobiltelefon (MS) erkennt die Fachperson, dass sich die Signalparameter des vom Empfänger empfangenen Signals des ersten Kanals der ersten Sendestation mit der Position des Empfängers im Vergleich zu dem vom Empfänger empfangenen Signal des zweiten Kanals der zweiten Sendestation unterschiedlich verändern.

131 Figur 4B der Streitpatentschrift mit Kommentierung und Kolorierung

132 durch den Senat

133 Dies steht im Einklang mit der durch das Streitpatent getroffenen Erläuterung, wonach Kanäle, welche über eine gemeinsame Sendeantenne ausgestrahlt werden, die Anforderung "unterschiedlich verändert" gemäß dem Merkmal 12.2.3 nicht erfüllen, da die gemeinsame Sendeantenne allein Kanäle mit Signalparametern bereitstellt, welche bezüglich einer räumlichen Veränderung im Bezug zum Standort des Empfängers nicht ausreichend unterschiedlich variieren (Abs. 0011). Basierend darauf versteht die Fachperson Merkmal 12.2.3 dahin, dass nur mehrere Sendestationen, welche räumlich entfernt angeordnet sind und jeweils einen Kanal mit zumindest jeweils einem Signalparameter bereitstellen, der sich mit der Position des Empfängers von den anderen der mehreren Kanäle, welche durch die weiteren Sendestationen bereitgestellt werden, ausreichend unterschiedlich verändert, die Anforderung erfüllen. Das Merkmal 12.2.3 bildet den Empfänger wiederum selbst nicht aus, sondern beschreibt eine Anforderung an eine drahtlose Umgebung, welche der Empfänger beobachtet.

134 Zum Maß des Unterschieds der Signalparameter ist im Streitpatent explizit nichts angegeben, jedoch erhält die Fachperson aus dem genannten Beispielen einer gemeinsamen Sendeantenne einer einzelnen Sendestation einerseits, welche die Anforderung nicht erfüllt, sowie dem Beispiel eines mehrere Sendeantennen in räumlich entfernten Sendestationen umfassenden drahtlosen Netzwerkes andererseits, welches die Anforderung erfüllt, einen Anhaltspunkt, was als ausreichender Unterschied anzusehen ist.

135 5.6 Gemäß dem Merkmal 12.3 werden Mittel zum Transportieren der Sätze von beobachteten Signalparametern (CO) zu einem Positionsberechnungsmodul (LCM) beansprucht. Generell ist das Bestimmen eines Positionsschätzwerts (LE) in zwei alternativen Ausführungsformen im Streitpatent offenbart, wie den Figuren 4A und 4B zu entnehmen ist. Dabei kann die Positionsschätzung im Empfänger (Figur 4B) oder entfernt in einem Netzwerk (Figur 4A) erfolgen. Im Fall, dass die Positionsschätzung nicht im Empfänger erfolgt, ist das Positionsberechnungsmodul (LCM) und das Statistische Modell (SM) in einer Positionsschätzvorrichtung (LEM) angeordnet, welche über ein drahtloses Netzwerk mit dem Empfänger in Verbindung steht (Abs. 0019, 0020, 0033, 0034). Die Sätze von beobachteten Signalparametern (CO) können in diesem Fall beispielsweise in einer Kurznachricht, über einen Datenanruf oder eine WAP- oder WLAN-Verbindung zu der Positionsschätzvorrichtung (LEM) gesendet werden (Abs. 0020).

136 Figur 4A und 4B der Streitpatentschrift mit Kolorierung durch den Senat

137 Wenn die Standortbestimmung im Empfänger ausgeführt werden soll, muss eine Kopie des statistischen Modells im Empfänger gespeichert werden. Der Empfänger benötigt in diesem Fall keine Übertragungskapazität zum Netzwerk und kann beispielsweise als Pager ausgeführt sein (Abs. 0019, 0034, Figur 4B). Der Figur 4B entnimmt die Fachperson, dass auch in diesem Fall Mittel zum Transportieren vorzusehen sind, über welche die beobachteten Sätze von Signalparametern von einer Empfangseinheit an eine Verarbeitungseinheit, im Figur 4B dargestellt als Mobilstation (MS) und Computer (PC), bereitgestellt werden. Die Mittel können beispielsweise als Kabel ausgebildet sein, mittels welcher die Mobilstation (MS) an den Computer (PC) angeschlossen ist (Figur 4B, Abs. 0034). Der Patentanspruch 12 ist jedoch auf keine bestimmte Ausführungsform der Mittel beschränkt.

138 5.7 Die Merkmale 12.3.1 bis 12.3.3 kennzeichnen das Positionsberechnungsmodul (LCM, location calculation module) und bilden den Empfänger allein aus, wenn das Positionsberechnungsmodul Teil des Empfängers ist.

139 Gemäß dem Merkmal 12.3.1 wird die Position (X) des Empfängers (R) auf der Grundlage der Sätze der beobachteten Signalparameter (CO, current observation) und eines statistischen Models (SM) der Signalparameter der mehreren Kanäle als Funktion einer Position des Empfängers in einer drahtlosen Telekommunikationsumgebung (RN) näherungsweise bestimmt, d. h. abgeschätzt. Als mögliche statistische Modelle nennt das Streitpatent, beispielsweise Wahrscheinlichkeitsmodelle, neuronale Netzwerke, Fuzzy-Logik-Systeme, Support Vector Machines, Entscheidungsbäume, Regressionsbäume und Kalman-Filter (Abs. 0015). Dabei wird laut Streitpatent ein statistisches Modell gewählt, weil hierzu keine Betrachtung einzelner Sätze von Kalibrierungsdaten (CD) für die Standortschätzung erforderlich sei, vielmehr eine Näherung unter Verwendung einer Funktion erfolgt (Abs. 0014). Das statistische Modell (SM) wird auf der Grundlage von Kalibrierungsdaten und optional auf der Grundlage von Vorabinformationen der drahtlosen Umgebung erstellt und beibehalten (Abs. 0026). Dabei ist im Streitpatent hervorgehoben, dass der Begriff "Kalibrierung" bewusst gewählt ist, um zu verdeutlichen, dass das statistische Modell möglicherweise aktualisiert werden muss, wenn sich Bedingungen ändern. Diese Bedingungen werden im Streitpatent nicht näher benannt. Als mögliche sich verändernde Bedingungen wird die Fachperson beispielsweise ein Hinzufügen oder Entfernen von Sendestationen sowie auch bauliche Veränderungen in der Telekommunikationsumgebung annehmen, die einen dauerhaften Einfluss auf zu beobachtende Signalparameter an einer Position haben können. Das statistische Modell kann im Fall der Anordnung im Empfänger online, falls Zugang zum Internet besteht, sowie offline aktualisiert werden (Abs. 0019).

140 Gemäß dem Merkmal 12.3.2 wird das statistische Modell zumindest teilweise auf der Grundlage der Sätze von Kalibrierungsdaten (Calibration Data CD) für jeden einer Mehrzahl von Kalibrierungspunkten beibehalten. Als Kalibrierungspunkte werden Punkte bezeichnet, deren Position und Signalparameter bekannt, beispielsweise gemessen worden sind (Abs. 0018). Für das statistische Modell werden somit zumindest teilweise Sätze von Daten verwendet, die mittels Messungen an bekannten Orten ermittelt wurden, wobei jeder der Sätze von Kalibrierungsdaten gemäß dem Merkmal 12.3.3 zumindest einen gemessenen Signalparameter für jeden der mehreren Kanäle, sowie den Ort an dem die jeweilige Messung durchgeführt wurde, enthalten muss (Abs. 0013). Optional kann zudem die Zeit, zu der die jeweilige Messung durchgeführt wurde, aufgenommen werden (Abs. 0013).

141 5.8 Der Patentanspruch 1 ist auf ein Verfahren zum Schätzen einer Position (X) eines Empfängers (R, R’) in einer drahtlosen Telekommunikationsumgebung (RN) sowie der nebengeordnete Patentanspruch 11 auf eine Positionsschätzvorrichtung (LEM) zum Schätzen einer Position (X) eines Empfängers (R, R’) in einer drahtlosen Telekommunikationsumgebung (RN) gerichtet. Dabei umfassen sowohl das Verfahren nach Patentanspruch 1, wie auch die Positionsschätzvorrichtung nach Patentanspruch 11, die den Empfänger nach Patentanspruch 12 beschreibenden Merkmale in entsprechender Weise. Denn die Positionsschätzvorrichtung nach Patentanspruch 11 beinhaltet die grundlegenden Merkmale der Erstellung des Statistischen Modells SM basierend auf den Kalibrierungsdaten, so dass die Ausführung nach Patentanspruch 11 notwendiger Bestandteil für die Positionsschätzung auch für die Patentansprüche 1 und 12 ist, unabhängig davon, ob die Positionsschätzung basierend auf dem SM im Empfänger oder der Positionsschätzvorrichtung ausgeführt wird. Das zuvor dargestellte Verständnis von Patentanspruch 12 gilt damit auch für die Auslegung der nebengeordneten Patentansprüche 1 und 11.

142 III. Zur erteilten Fassung

143 Dem Bestand des Streitpatents in der erteilten Fassung steht der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54 EPÜ entgegen, da die Gegenstände des erteilten Patentanspruchs 12 sowie der nebengeordneten Patentansprüche 1 und 11 aus der Druckschrift D5a bekannt und somit nicht neu sind.

144 1. Bei D5a (WO 00/18148 A1) handelt es sich um eine am 30. März 2000 vorveröffentlichte Patentanmeldung aus der Patentfamilie der D5, auch wenn das Streitpatent die Priorität der am 29. Dezember 2000 veröffentlichten FI 20002891 wirksam in Anspruch nimmt.

145 1.1 D5a beschreibt ein Verfahren zur Positionsschätzung einer mobilen Vorrichtung (mobile unit, MU), wobei gemäß der Erfindung der Standort der MU derart bestimmt werden kann, indem eine Momentaufnahme eines vordefinierten Abschnitts des Hochfrequenzspektrums (HF-Spektrum) von der MU aufgenommen und mit einer Referenzdatenbank verglichen wird, die mehrere Momentaufnahmen von verschiedenen Standorten enthält (S. 1 Z. 35-45). Die Erfindung basiert dabei auf der Erkenntnis, dass jeder Ort einen einzigartigen spektralen Fingerabdruck (RF) aufweist (S. 2 Z. 44 – S. 3 Z. 2) und somit über den Schnappschuss eines Hochfrequenzspektrums identifiziert werden kann. Der spektrale Fingerabdruck wird in diesem Zusammenhang als eine vorbestimmte Kombination beobachtbarer HF-Spektralparameter definiert. Dabei stellt die beobachtete Signalstärke einer vorbestimmten Menge von Signalen im HF-Spektrum einen solchen Fingerabdruck dar. Gemäß D5a wird heute weltweit praktisch das gesamte HF-Spektrum bis 2 GHz und darüber hinaus von verschiedenen Anwendungen genutzt, wobei die Signalcharakteristika innerhalb dieses Spektrums starkvariiert. Für jeden beliebigen Ort ist es jedoch möglich, einen Spektrumsbereich und eine Kombination von Signalparametern in diesem Bereich auszuwählen, welche für diesen Ort eindeutig sind (S. 2 Z. 44 – S. 3 Z. 9).

146 Zur Erfassung des Hochfrequenzspektrums weist die MU (S. 2 Z. 20) die entsprechende Schaltungstechnik und Software auf, um die erforderlichen Signale und deren Parameter zu erfassen.In einer Ausführungsform verfügt die MU über eine Antenne, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt z.B. von 70 MHz bis 1 GHz (S. 3 Z. 10-12, S. 4 Z. 17-20). So kann die MU zum Empfangen eines bestimmten Frequenzbandes, wie einem Band eines Mobilfunknetzes, oder mehrerer verschiedener Frequenzbänder ausgebildet sein, wozu die MU dementsprechende Empfänger (Fingerprint Capture Component) aufweist (S. 3 Z. 12-24, Fig. 2).

147 Figur 2 der D5a mit Kolorierung durch den Senat

148 Figur 2 zeigt eine MU mit einer Komponente 101, welche Informationen aus dem HF-Spektrum über eine Antenne 102 empfängt, sowie einer Kommunikationskomponente 105 zur Informationsübertragung an eine andere Vorrichtung über eine bestehende drahtlose Infrastruktur (S. 3 Z. 25-26). Zur Standortbestimmung der MU wird die Komponente 101 aktiviert. Damit können nachfolgend vorbestimmte Informationen aus einem vorbestimmten Abschnitt des HF-Spektrums erfasst werden (S. 3 Z. 45 – S. 4 Z. 2).

149 Figur 4 der D5a zeigt die Struktur eines Fingerabdrucks gemäß einer Ausführungsform der Erfindung. Der Fingerabdruck umfasst dabei Merkmale empfangener Signale bei mehreren Frequenzen, wobei jede Spalte Informationen zu einer bestimmten Frequenz oder einem bestimmten Träger enthält (Figur 4, S. 6 Z. 30-31, Z. 39-41). Als Signalparameter des spektralen Fingerabdrucks kann die Signalstärke verwendet werden, die Erfindung gemäß D5a ist jedoch nicht auf diese beschränkt (S. 4 Z. 10-14). Die Signalstärke kann für jede Frequenz mehrfach abgetastet werden, um etwaige Abweichungen auszugleichen.

150 Figur 4 der D5a mit Kolorierung durch den Senat

151 Dabei können Anweisungen bezüglich der zu erfassenden Informationen und des entsprechenden HF-Spektrums entweder in der MU vorprogrammiert oder in Echtzeit generiert werden. Die MU erfasst basierend darauf dann diese Informationen aus dem entsprechenden HF-Spektrum (S. 4 Z. 3-8).

152 Weiter offenbart D5a, dass sobald ein Fingerabdruck generiert wurde, seine Zuordnung zu einem bestimmten Ort ermittelt werden kann.Dies geschieht mithilfe einer Fingerabdruckdatenbank, die eine Reihe von Fingerabdrücken zusammen mit ihren entsprechenden Ortsangaben enthält, welche in einer Ausführungsform in der MU gespeichert ist.Der generierte Fingerabdruck wird mit den Fingerabdrücken in der Datenbank verglichen, und derjenige, der dem generierten Fingerabdruck am nächsten kommt, wird als Treffer ausgewählt.In einer anderen Ausführungsform verwendet der Suchalgorithmus mehrere Fingerabdrücke aus der Datenbank, die dem generierten Fingerabdruck am nächsten liegen, und interpoliert den wahrscheinlichsten Ort für die MU.Ist die Fingerabdruckdatenbank in einer anderen Vorrichtung gespeichert, so wird der generierte Fingerabdruck von der MU mittels der Kommunikationskomponente über die drahtlose Verbindung an die andere Vorrichtung übertragen und von dieser die Position bestimmt (S. 5, Z. 4-20).

153 Weiter beschreibt D5a, dass die Referenzdatenbank beispielsweise durch Computerberechnungen und basierend auf Feldmessungen erstellt werden kann, mit dem Ziel, eine erlernte Beziehung zwischen Position und Signalstärke zu erhalten, sodass bei einer beliebigen Position die entsprechende Signalstärke für jeden bestimmten Frequenzkanal erhalten werden kann. Das System kann zudem lernen, sodass die Datenbank kontinuierlich verbessert wird (S. 7 Z. 34 - S. 8 Z. 12). Für den Schritt des Bestimmens des am besten passenden Fingerabdrucks zeigt die D5a verschiedene Optionen, die auf dem Gebiet des statistischen Mustervergleichs liegen. Beispielsweise kann der geringste mathematische Abstand zwischen gespeicherten Fingerabdrücken und dem erfassten Fingerabdruck zur Positionsschätzung bestimmt (S. 6 Z. 4-29) werden.

154 1.2 Damit sind die Merkmale 12.1 bis 12.3.3 als in der D5a offenbart anzusehen.

155 Die D5a zeigt mit der MU einen Empfänger mit Mittel zum Bestimmen von Sätzen von beobachtenden Signalparametern, hier in Form einer Komponente 101, welche Informationen aus dem Hochfrequenzspektrum (HF)-Spektrum über eine Antenne 102 empfangen kann, wie in Figur 2 dargestellt (S. 3 Z. 25-26). Dabei ist die MU ausgebildet, eine Momentaufnahme eines vordefinierten Abschnitts des HF-Spektrum mittels der Antenne zu empfangen, wobei die Momentaufnahme des HF-Spektrums den Sätzen von beobachteten Signalparametern entspricht (S. 3 Z. 45 – S. Z. 2). Damit offenbart die D5a die Merkmale 12.1 und 12.2.

156 Wie in Figur 4 der D5a gezeigt, umfasst jeder Fingerprint dabei mindestens einen beobachteten Signalparameter für jeden der mehreren Spektralbereiche bzw. jede der Frequenzen (S. 6 Z. 39 –Z. 40), welche streitpatentgemäße Kanäle darstellen, an der Position der MU, wie die Signalstärken 1 bis m, womit D5a Merkmal 12.2.1 offenbart.

157 Daraus, dass Signalparameter für die mehreren Frequenzen, welche demnach mehreren Kanälen entsprechen, gleichzeitig empfangen werden können, entnimmt die Fachperson unmittelbar, dass auf diesen Frequenzen gleichzeitig Informationen gesendet werden, somit eine gleichzeitige Kommunikation unterstützen wird, womit Merkmal 12.2.2 in D5a verwirklicht ist.

158 Mit der Signalstärke 1 bis m wird für jede der mehreren Frequenzen F1 bis Fn mindestens ein Signalparameter S11 bis SSmn erfasst, der sich mit der Position von den anderen der mehreren Frequenzen unterschiedlich verändert, da eine derartige Änderung der Signalstärke bei der Signalausbreitung inhärent ist, womit D5a ebenso Merkmal 12.2.3 vorwegnimmt.

159 Die Kommunikationskomponente 105, welche zur Informationsübertragung an eine andere Vorrichtung über eine bestehende drahtlose Infrastruktur dient, stellt ein Mittel zum Transportieren der Sätze von beobachteten Signalparametern zu einem Positionsberechnungsmodul zum Bestimmen eines Positionsschätzwerts dar, welches insbesondere verwendet wird, wenn die Positionsbestimmung nicht in der MU, sondern in der anderen Vorrichtung ausgeführt wird (S. 5 Z. 16-20).Damit ist D5a Merkmal 12.3 zu entnehmen.

160 Wie in D5a beschrieben, wird die Position der MU basierend auf dem generierten Fingerabdruck, somit der beobachteten Signalparameter der mehreren Kanäle, für eine Zuordnung zu einem bestimmten Ort verwendet, wobei dies mithilfe einer Fingerabdruckdatenbank, die eine Reihe von Fingerabdrücken zusammen mit ihren entsprechenden Ortsangaben enthält, somit ein statistisches Model der Signalparameter darstellt, erfolgt. Dabei wird der generierte Fingerabdruck mit den Fingerabdrücken in der Datenbank verglichen. Dabei kann in einer Ausführungsform der Suchalgorithmus mehrere Fingerabdrücke aus der Datenbank verwenden, die dem generierten Fingerabdruck am nächsten liegen. In einer anderen Ausführung interpoliert der Suchalgorithmus den wahrscheinlichsten Ort für die MU (S. 5, Z. 4-15). Damit offenbart D5a ein Positionsberechnungsmodul gemäß dem Merkmal 12.3.1 zum Bestimmen eines Positionsschätzwerts, welches die Position des Empfängers auf der Grundlage der Sätze und eines statistischen Models der Signalparameter der mehreren Kanäle als Funktion einer Position des Empfängers in einer drahtlosen Telekommunikationsumgebung (RN) approximiert.

161 Weiter ist in D5a offenbart, dass die Referenzdatenbank beispielsweise durch Computerberechnungen und basierend auf Feldmessungen erstellt werden kann, mit dem Ziel, eine erlernte Beziehung zwischen Position und Signalstärke zu erhalten. Die erhaltenen Fingerabdruck-Informationen werden zusammen mit den Standortkoordinaten in die Datenbank eingetragen. Je geringer dieser Abstand ist, desto höher ist die Auflösung. Dabei kann das System auch durch Interpolation und "on the fly" eine Position ermitteln, sodass die Datenbank kontinuierlich verbessert werden kann (S. 7 Z. 34 - S. 8 Z. 12). Damit sind die Merkmale 12.3.2 und 12.3.3 zu entnehmen, wonach jeder Satz von Kalibrierungsdaten die Position eines jeweiligen Kalibrierungspunkts und mindestens einen gemessenen Signalparameter für jeden der mehreren Kanäle an dem Kalibrierungspunkt umfasst.

162 Der Gegenstand des erteilten Patentanspruchs 12 erweist sich demnach als nicht neu gegenüber der aus dem Dokument D5a bekannten Vorrichtung.

163 2. Das Familiendokument D5 (WO 01/72060 A1), das die Priorität der US 09/532,418 vom 22. März 2000 in Anspruch nimmt, zeigt die gleiche technische Lehre wie oben aus der D5a als bekannt beschrieben und steht dem Gegenstand des Streitpatents daher ebenfalls neuheitsschädlich entgegen. Zu den Einzelheiten nimmt der Senat auf die Ausführungen im qualifizierten Hinweis vom 17. März 2025 Bezug.

164 3. Die nebengeordneten Patentansprüche 1 und 11 erweisen sich entsprechend der vorangegangenen Begründung der mangelnden Patentfähigkeit von Patentanspruch 12 aus denselben Gründen als nicht neu gegenüber dem Stand der Technik aus dem Dokument D5a und damit als nicht patentfähig. Wie bereits zuvor im Rahmen der Auslegung der Merkmale des Streitpatents ausgeführt, ist der nebengeordnete Patentanspruch 11 auf eine Positionsschätzvorrichtung (LEM) zum Schätzen einer Position (X) eines Empfängers (R, R’) in einer drahtlosen Telekommunikationsumgebung (RN) gerichtet und dabei umfassen sowohl das Verfahren nach Patentanspruch 1 wie auch die Positionsschätzvorrichtung nach Patentanspruch 11 die den Empfänger nach Patentanspruch 12 beschreibenden Merkmale in entsprechender Weise.

165 4. Da die Beklagte, wie sie in der mündlichen Verhandlung zu Protokoll erklärt hat, das Streitpatent in der erteilten Fassung als geschlossenen Anspruchssatz verteidigt, haben die weiter angegriffenen abhängigen Patentansprüche der erteilten Fassung insgesamt keinen Rechtsbestand; sie fallen jeweils mit den Patentansprüchen 1, 11 und 12 (vgl. hierzu näher BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator). Dass die in den abhängigen Ansprüchen enthaltenen Einschränkungen die Patentfähigkeit begründen könnten, hat die Beklagte nicht behauptet. Einer isolierten Prüfung der Unteransprüche der erteilten Fassung bedarf es daher nicht.

166 IV. Zu den Hilfsanträgen

167 Die Beklagte kann das Streitpatent auch in den Fassungen der Hilfsanträge 1 bis 6 nicht erfolgreich verteidigen, da diesen jeweils zumindest der Nichtigkeitsgrund der fehlenden Patentfähigkeit entgegensteht, Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a), EPÜ i. V. m. Art. 52, 54, 56 EPÜ.

168 1. Die Beklagte kann das Streitpatent auch in der Fassung gemäß Hilfsantrag 1 nicht mit Erfolg verteidigen, denn die Gegenstände der Patentansprüche 1, 11 und 12 nach Hilfsantrag 1 erweisen sich als nicht patentfähig.

169 Dabei kann dahinstehen, ob der Teil des zusätzlich aufgenommenen Merkmals "wherein the several channels are received by the receiver from more than one network" in den Patentansprüchen 1, 11 und 12 zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führt, denn die Patentansprüche nach Hilfsantrag 1 sind gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) nicht schutzfähig.

170 1.1 Mit Hilfsantrag 1 ergänzt die Klägerin Patentanspruch 12 - mit einer Merkmalsgliederung durch den Senat - wie folgt (Übersetzung durch den Senat):

171 12.2.1.1Hi1 wherein, a channel is a frequency band,

12.2.1.1Hi1 wobei ein Kanal ein Frequenzband ist,

12.2.1.2Hi1 wherein the several channels are received by the receiver from more than one network,

12.2.1.2Hi1 wobei die mehreren Kanäle von dem Empfänger von mehr als einem Netzwerk empfangen werden.

172 Wie zur Auslegung des Streitpatents ausgeführt, versteht die Fachperson unter einem Kanal im Zusammenhang mit einer drahtlosen Telekommunikations-umgebung zunächst eine Ressource, welche für eine Sprach- oder Datenübertragung verwendet wird, wobei das Streitpatent den Kanal weiter eingrenzt und vorgibt, dass jeder der mehreren beobachteten Kanäle sich in seiner Frequenz unterscheiden soll, was einem Funkfrequenzkanal entspricht. Ein Funkfrequenzkanal stellt jeweils eine Bandbreite zur Verfügung, welche je nach Übertragungstechnik variiert. Beispielsweise beträgt die Bandbreite eines Funkfrequenzkanals bei GSM 200 kHz, welche die Fachperson als eine Frequenz bzw. als ein Frequenzband, welches durch eine untere und obere Frequenz begrenzt ist, im Sinne des Streitpatents verstehen wird.

173 Die Fachperson entnimmt dem Streitpatent zudem, dass es zur Erfüllung des Empfangs mehrerer Netzwerke ausreicht, dass die Netze die gleiche Netzwerkart aufweisen und allein von verschiedenen Betreibern bereitgestellt werden, so wie im Streitpatent beschriebenen Beispiel gezeigt, vom Typ GSM sein können und durch verschiedene Betreiber bereitgestellt werden (Abs. 0010). Die Fachperson wird als mehrere Netzwerke somit sowohl Netzwerke verschiedener Netzwerkarten, wie auch Netzwerke mehrerer Betreiber verstehen.

174 1.2 Aus D5a (WO 00/18148 A1) ist eine mobile Einheit (MU) bekannt, welche mehrere Informationen oder Daten aus verschiedenen Bereichen des Spektrums erfassen, somit empfangen kann (S. 4 Z. 7-8). Dabei wird zugrunde gelegt, dass weltweit nahezu das gesamte HF-Spektrum bis 2 GHz und darüber hinaus von verschiedenen Anwendungen genutzt wird, deren Signalcharakteristika innerhalb dieses Spektrums für jeden beliebigen Ort erheblich variiert und somit zur eindeutigen Positionsbestimmung verwendet werden kann. Dabei ist die MU mit der entsprechenden Schaltungstechnik und Software ausgestattet, um die erforderlichen Signale und deren Parameter zu erfassen. Beispielsweise kann die MU Signalcharakteristika des UHF-Fernsehbandes nutzen und entsprechende Fernsehkanäle empfangen. In einem anderen Beispiel ist die MU mit einem Tuner ausgestattet, der für den Empfang von AM- oder FM-Radiosignalen ausgelegt ist und entsprechende Radio-Sendebänder empfangen kann. So kann die MU über eine Antenne verfügen, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt, z. B. von 70 MHz bis 1 GHz. Als weitere Ausführungsform ist, für den Fall, dass sich die vorbestimmten Abschnitte des HF-Spektrums vom Band für drahtlose Kommunikation, also dem Mobilfunk, stark unterscheiden, hierzu auch eine zusätzliche Schaltung vorgesehen (S. 3 Z. 4-7; S. 4 Z. 16-20; S. 4 Z. 29-43).

175 1.3 D5a offenbart die Merkmale 12.2.1.1Hi1 und 12.2.1.2Hi1 und nimmt damit den Gegenstand des Anspruchs 12 nach Hilfsantrag 1 neuheitsschädlich vorweg.

176 Die in der D5a beschriebene MU verfügt einerseits über eine Antenne, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt, und andererseits sieht diese MU, falls sich die vorbestimmten Abschnitte des HF-Spektrums vom Band für drahtlose Kommunikation stark unterscheidet, hierzu eine zusätzliche Schaltung vor, welche diese Teile des Frequenzspektrums zugehörig zu verschiedenen Anwendungen für drahtlose Kommunikation empfängt (S. 3 Z. 4-7; S. 4 Z. 16-20; S. 4 Z. 29-43). Damit offenbart D5a Mittel zum Beobachten von Signalparametern von mehreren Kanälen, wobei ein Kanal einem Frequenzband entspricht und wobei die Kanäle von verschiedenen Netzen empfangen werden, wie in den Merkmalen 12.2.1.1Hi1 und 12.2.1.2Hi1 des Hilfsantrags 1 beansprucht.

177 2. Die Beklagte kann das Streitpatent auch in der Fassung gemäß Hilfsantrag 2 nicht mit Erfolg verteidigen. Dabei kann dahinstehen, ob die mit Hilfsantrag 2 aufgenommenen Merkmale "wherein the several channels are received by the receiver from more than one network" und "wherein the more than one network are different types of networks" in den Patentansprüchen 1, 11 und 12 zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führen, denn Hilfsantrag 2 erweist sich gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) als nicht patentfähig.

178 2.1 Mit Hilfsantrag 2 ergänzt die Klägerin Patentanspruch 12 gemäß Hilfsantrag 1 nach Merkmal 12.2.1.2Hi1 - mit einer Merkmalsgliederung durch den Senat - wie folgt: (Übersetzung durch den Senat):

179 12.2.1.3Hi2 wherein the more than one network are different types of networks,

12.2.1.3Hi2 wobei es sich bei den mehr als einem Netzwerk um unterschiedliche Netzwerktypen handelt.

180 Die Fachperson wird als verschiedene Arten von Netzwerken basierend auf den Ausführungen des Streitpatents, wobei ein fortgeschrittener Empfänger verschiedene Arten von Netzwerken, wie beispielsweise ein Mobilfunknetz und Rundfunknetz (Abs. 0010: "A more advanced receiver may observe many types of networks, such as cellular networks and broadcast networks”) empfangen kann, dahin verstehen, dass die verschiedenen Netzwerke jeweils unterschiedliche Anwendungen in jeweils den der Anwendung zugewiesenen Frequenzbändern unterstützen. Eine Aufzählung von als geeignet angesehenen Netzwerken beschränkt sich auf eine Nennung verschiedener Funknetze, wie Mobilfunknetze (wie GSM, GPRS, UMTS, usw.), Rundfunknetze (Analog-Audio, DAB oder DVB), drahtlose lokale Netzwerke (WLAN) oder Mikrowellen-Kurzstreckennetze wie Bluetooth (Abs. 0011).

181 2.2 Wie bereits zum Hilfsantrag 1 ausgeführt, zeigt die D5a eine mobile Einheit (MU), welche mehrere Informationen oder Daten aus verschiedenen Bereichen des Spektrums empfangen kann (S. 4 Z. 7-8). Dabei ist die MU mit der entsprechenden Schaltungstechnik und Software ausgestattet, um die erforderlichen Signale und deren Parameter zu erfassen. Beispielsweise kann die MU Signalcharakteristika des UHF-Fernsehbandes nutzen und entsprechende Fernsehkanäle empfangen. In einem anderen Beispiel ist die MU mit einem Tuner ausgestattet, der für den Empfang von AM- oder FM-Radiosignalen ausgelegt ist und kann somit entsprechende Radio-Sendebänder empfangen. Die MU kann über eine Antenne verfügen, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt, z. B. von 70 MHz bis 1 GHz. Als weitere Ausführungsform kann, wenn sich die vorbestimmten Abschnitte des HF-Spektrums vom Band für drahtlose Kommunikation, also dem Mobilfunk, stark unterscheiden, hierzu auch eine zusätzliche Schaltung vorgesehen sein (S. 3 Z. 4-7, S. 4 Z. 16-20, Z. 29-43).

182 2.3 D5a offenbart neben den Merkmalen 12.2.1.1Hi1 und 12.2.1.2Hi1 das weitere Merkmal 12.2.1.3Hi2 und nimmt damit den Gegenstand des Anspruchs 12 nach Hilfsantrag 2 neuheitsschädlich vorweg.

183 Mit der Ausführung der MU, wobei diese über eine Antenne verfügt, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt und der weiteren Ausführung der MU derart, dass zusätzliche Schaltungen vorgesehen sind, womit Teile des Frequenzspektrums zugehörig zu verschiedenen Anwendungen für drahtlose Kommunikation, wie des Mobilfunks, für UHF-Fernsehen sowie AM- oder FM-Radio empfangen werden können, offenbart D5a Mittel zum Beobachten von Signalparametern von mehreren Kanälen, wobei ein Kanal einem Frequenzband entspricht und wobei die Kanäle von verschiedenen Netzwerkarten empfangen werden.

184 3. Das Streitpatent kann auch in der Fassung gemäß Hilfsantrag 3 nicht mit Erfolg verteidigt werden. Es kann dabei dahinstehen, ob das zusätzlich aufgenommene Merkmal "wherein the different types of networks comprise a cellular network and a wireless local-area network (WLAN)" in den Patentansprüchen 1, 11 und 12 nach Hilfsantrag 3 zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führt, da sich auch Hilfsantrag 3gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) als nicht patentfähig erweist.

185 3.1 Mit Hilfsantrag 3 ergänzt die Klägerin Patentanspruch 12 gegenüber Hilfsantrag 12 nach Merkmal 12.2.1.3Hi2 und unter Auslassung des Merkmals 12.2.1.1Hi1 - mit einer Merkmalsgliederung durch den Senat - wie folgt (Übersetzung durch den Senat):

186 12.2.1.4Hi3 wherein the different types of networks comprise a cellular network and a wireless local-area network (WLAN);

12.2.1.4Hi3 wobei die verschiedenen Netzwerktypen ein Mobilfunknetz und ein drahtloses lokales Netzwerk (WLAN) umfassen;

187 Als geeignete Netzwerke werden im Streitpatent allgemein Mobilfunknetze (wie GSM, GPRS, UMTS usw.), Rundfunknetze (Analog-Audio, DAB oder DVB), drahtlose lokale Netzwerke (WLAN) oder Mikrowellen-Kurzstreckennetze wie Bluetooth genannt (Abs. 0011).

188 Dem Merkmal 12.2.1.4Hi3 wie den Ausführungen des Streitpatents, insbesondere Absatz 0011, ist für die Fachperson nicht eindeutig zu entnehmen, ob WLAN allgemein als Abkürzung für ein drahtloses lokales Netzwerk steht, wie von der Klägerin vorgebracht, oder ein bestimmtes drahtloses Netzwerk, insbesondere ein drahtloses lokales Netzwerk nach dem Standard IEEE 802.11, wie von der Beklagten ausgeführt, benennen soll.

189 Der Fachperson ist die Abkürzung WLAN unstreitig allgemein als Oberbegriff für drahtlose lokale Netzwerke bekannt. Die weitere mögliche Bedeutung des Wortes WLAN als Synonym für ein drahtloses lokales Netzwerk gemäß dem IEEE 802.11 Standard (Wi-Fi), welche allein teilweise im deutschen Sprachraum verwendet wird, wird die Fachperson hingegen dem Streitpatent, welches original in englischer Sprache angemeldet wurde, nicht zugrunde legen. Dies folgt allein schon aus dem Grund, dass im englischen Sprachraum für ein drahtloses lokales Netzwerk gemäß IEEE 802.11 Standard allein die Abkürzung Wi-Fi verwendet wird. Zudem ist dem Streitpatent keine Einschränkung auf ein Wi-Fi oder den Wi-Fi Standard IEE 802.11 zu entnehmen. Die Fachperson versteht die Abkürzung WLAN mangels anderslautender expliziter Definition bzw. Hinweise somit allgemein im Sinne eines drahtlosen lokalen Netzwerks.

190 3.2 Wie bereits ausgeführt, zeigt D5a eine mobile Einheit (MU), welche mehrere Informationen oder Daten aus verschiedenen Bereichen des Spektrums empfangen kann (S. 4 Z. 7-8), wobei die MU mit der entsprechenden Schaltungstechnik und Software ausgestattet ist, um die erforderlichen Signale und deren Parameter zu erfassen. Dabei stellt die vorliegende Erfindung ein neues Verfahren zur Bestimmung des Standorts von MU 10 bereit, welches in Gebieten funktioniert, in denen üblicherweise keine GPS-Abdeckung verfügbar sind, wie in Innenräumen (S. 2 Z. 38-41; S. 3 Z. 41-42). So kann die MU über eine Antenne verfügen, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt, z. B. von 70 MHz bis 1 GHz, sowie zum Empfang vorbestimmter Abschnitte des HF-Spektrums auch eine zusätzliche Schaltung aufweisen (S. 3 Z. 10-24; S. 4 Z. 16-20). Dabei weist D5a darauf hin, dass weltweit nahezu das gesamte HF-Spektrum bis 2 GHz und darüber hinaus von verschiedenen Anwendungen genutzt wird, deren Signalcharakteristika innerhalb dieses Spektrums für jeden beliebigen Ort erheblich variieren und somit zur eindeutigen Positionsbestimmung verwendet werden können.

191 3.3 D5a offenbart, wie bereits zu Hilfsantrag 1 und 2 ausgeführt, die Merkmale 12.2.1.2Hi1 und 12.2.1.3Hi2. Es kann allerdings dahinstehen, ob auch das weitere Merkmal 12.2.1.4Hi3 in D5/D5a als unmittelbar und eindeutig offenbart anzusehen ist, denn jedenfalls ergibt sich das Merkmal 12.2.1.4Hi3 für die Fachperson unter Berücksichtigung ihres Fachwissens, belegt durch die D16, in naheliegender Weise aus D5a und kann ein Vorliegen einer erfinderischen Tätigkeit nicht begründen.

192 Die Fachperson ist durch D5a veranlasst, das gesamte HF-Spektrum bis 2 GHz und darüber hinaus, welches von verschiedenen Anwendungen genutzt wird, zu betrachten, da D5a betont, dass die Signalcharakteristika innerhalb dieses Spektrums für jeden beliebigen Ort erheblich variiert und somit zur eindeutigen Positionsbestimmung geeignet ist. Dabei wird die Fachperson insbesondere Anwendungen betrachten, deren vorbestimmte Abschnitte des HF-Spektrums sich vom Frequenzband für drahtlose Kommunikation, also dem Mobilfunk, nicht so stark unterscheiden, da für diesen Fall keine zusätzliche Schaltung vorzusehen ist. Die MU verfügt bereits über eine Antenne, deren Bandbreite einen großen Teil des VHF- und UHF-Spektrums abdeckt, z. B. von 70 MHz bis 1 GHz. Die Fachperson wird sich somit insbesondere mit Anwendungen, welche dieses HF-Spektrums nutzen, beschäftigen und somit auch lokale drahtlose Netzwerke betrachten. Drahtlose lokale Netzwerke waren zum Zeitrang der Priorität des Streitpatents der Fachperson bereits allgemein bekannt, wie von der Klägerin mit D16 belegt. Die D16, eine Fachzeitschrift, stellt zum Thema Konnektivität verschiedene drahtlose lokale Netzwerke vor, und zeigt insbesondere eine Übersicht über das HF-Spektrum und die dieses nutzende Anwendungen (D16 S. 308).

193 Ausschnitt aus Seite 308 der D16 mit Hervorhebung durch den Senat

194 Die Fachperson entnimmt dem, dass mittels der in der MU bereits vorhandenen Antenne und zugehöriger Schaltung insbesondere drahtlose lokale Netzwerke wie Wave LAN, welche den Bereich von 902 MHz bis 928 MHz belegen, ebenso zur Schätzung einer Position genutzt werden können und wird diese insbesondere durch ihre Nähe zum vom Mobilfunk genutzten Spektrum naheliegend berücksichtigen.

195 3.4 Auch die von der Beklagten weiter vorgetragene Argumentation, dass sich die Erfindung gemäß der Hilfsanträge 2 und 3 grundlegend von den Ausführungen der D5a unterscheide, da ein streitpatentgemäßer Empfänger nicht allein verschiedene Frequenzen, sondern bestimmte ausgewählte Kanäle verschiedener Netzwerkarten beobachte und diese der Positionsbestimmung zugrunde lege, kann zu keiner abweichenden Einschätzung führen.

196 Zum einen ist den von der Beklagten angegebenen Absätzen 0011 und 0024 der Streitpatentschrift eine derartige Ausführung für die Fachperson nicht zu entnehmen. So definiert Absatz 0011, was unter einer drahtlosen Umgebung zu verstehen ist, wobei beschrieben wird, dass diese über mehrere Kanäle, im Sinne des Streitpatents über mehrere Frequenzen oder Frequenzbänder, gleichzeitig kommunizieren können müsse, wobei jeder Kanal einen Signalparameter, welcher sich ortsabhängig anders verändere, aufweise. Zudem werden geeignete Netzwerke genannt, welche dieser Anforderung genügen. Eine Ausgestaltung bezüglich des Empfängers ist hingegen nicht zu entnehmen. Absatz 0024 zeigt in Verbindung mit Figur 1 lediglich zum Hintergrund der Erfindung eine Ausbreitung zweier Signalparameter in Abhängigkeit vom Empfängerort, wobei die Fachperson entnimmt, dass sich Signalparameter, wie hier die Signalstärke, ortsabhängig verändern, jedoch eine Rekonstruktion des Signals schwierig ist. Eine Ausgestaltung des Empfängers oder der Erfindung an sich ist dem Absatz 0024 hingegen nicht zu entnehmen.

197 Zum anderen wäre eine Ausführung, wonach ein Empfänger nicht allein verschiedene Kanäle und somit verschiedene Frequenzen, sondern bestimmte ausgewählte Kanäle verschiedener Netzwerkarten beobachtet, zudem auch durch D5a vorweggenommen. So offenbart D5a als vorteilhaft, für die Schätzung der Position eines Empfängers bei der Erstellung eines Fingerabdrucks insbesondere bestimmte Teile des Frequenzspektrums bzw. bestimmte Anwendungen zu berücksichtigen. So ist die MU mit Schaltungen und Software ausgestattet, die in der Lage sind, Informationen aus vorbestimmten Abschnitten des HF-Spektrums zu erfassen (S. 3 Z. 5-12). Die MU kann dabei eine vorkonfigurierte Auswahl der zu beobachteten Frequenzen enthalten. Alternativ kann die MU dynamisch von einer anderen Vorrichtung die zu beobachtenden Teile des Frequenzspektrums erhalten und zur Positionsbestimmung verwenden (S. 3 Z. 45 – S. 4 Z. 20). In einer Ausführungsform wird die MU von einer anderen Vorrichtung angewiesen, ausgewählte Spektralbereiche abzutasten und ausgewählte Parameter aus den empfangenen Signalen zu erfassen (S. 4 Z. 27-29), in einer anderen Ausführungsform wird die Auswahl durch die MU selbst bestimmt (S. 4 Z. 41-43).

198 Somit wäre auch eine Ausführungsform, bei der der Empfänger nicht allein verschiedene Frequenzen, sondern bestimmte ausgewählte Kanäle verschiedener Netzwerkarten beobachten könnte, entgegen der Annahme der Beklagten und wenn diese im Streitpatent offenbart wäre, nicht geeignet, eine Patentfähigkeit zu begründen.

199 4. Die Beklagte kann das Streitpatent auch in der Fassung gemäß Hilfsantrag 4 nicht mit Erfolg verteidigen. Dabei kann dahinstehen, ob die Ergänzung "wherein the several channels are received using different antennas" in den Patentansprüchen 1, 11 und 12 nach Hilfsantrag 4 zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führt, da sich Hilfsantrag 4 gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) als nicht patentfähig erweist.

200 4.1 Mit Hilfsantrag 4 ergänzt die Klägerin Patentanspruch 12 der erteilten Fassung nach Merkmal 12.2.1 – mit einer Merkmalsgliederung durch den Senat – wie folgt (Übersetzung durch den Senat):

201 12.2.1.2Hi1 wherein the several channels are received by the receiver from more than one network,

12.2.1.2Hi1 wobei die mehreren Kanäle von dem Empfänger von mehr als einem Netzwerk empfangen werden,

12.2.1.5Hi4 wherein the several channels are received using differentantennas;

12.2.1.5Hi4 wobei die verschiedenen Kanäle mit unterschiedlichen Antennen empfangen werden;

202 4.2 D5a zeigt eine mobile Einheit MU, welche mittels Schaltungen und Software Informationen aus vorbestimmten Bereichen des HF-Spektrums erfassen kann. D5a führt aus, dass, wenn vorbestimmte Bereiche des HF-Spektrums, welches beobachtet werden soll, innerhalb oder in unmittelbarer Nähe desselben Frequenzbands wie das vom drahtlosen Kommunikationsnetz genutzte Frequenzband liegen, dieselbe Hardware-Schaltung verwendet werden kann. Unterscheiden sich hingegen die vorbestimmten Bereiche des HF-Spektrums vom Frequenzband des drahtlosen Kommunikationsnetzes, sind in diesem Fall jedoch zusätzliche Schaltungen erforderlich. Dabei führt D5a aus, dass in einer Ausführung der MU mittels einer Antenne große Bereiche eines Spektrums empfangen werden können. In einer weiteren Ausführung der MU weist diese eine schmalbandige Antenne auf, welche auf einen Frequenzbereich begrenzt ist. Diese Antennen sind gemäß D5a kostengünstiger und weniger störanfällig (S. 4 Z. 7-24).

203 4.3 D5a offenbart damit neben dem Merkmal 12.2.1.1Hi1 auch das weitere Merkmal 12.2.1.5Hi4.

204 Die D5a zeigt als eine Ausführungsform, dass die MU, welche einen streitpatentgemäßen Empfänger darstellt, mehrere Informationen oder Daten aus verschiedenen Bereichen des Spektrums erfassen kann, wobei die Fachperson versteht, dass über mehrere schmalbandige Antennen jeweils ein Spektralbereich, somit einen Kanal, empfangen werden kann. Dabei erkennt sie diese Ausführungsform als vorteilhaft, da diese kostengünstiger und weniger störanfällig ist. Damit ist Merkmal 12.2.1.5Hi4 der D5a zu entnehmen (S. 4 Z. 7-24).

205 5. Die Beklagte kann das Streitpatent auch in der Fassung gemäß Hilfsantrag 5 nicht mit Erfolg verteidigen. Dabei kann dahinstehen, ob die zusätzlich in den Patentansprüchen 1, 11 und 12 aufgenommenen Merkmale nach den Hilfsanträgen 3 und 4, die auch im Hilfsantrag 5 enthalten sind, zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führen, da sich Hilfsantrag 5 gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) als nicht patentfähig erweist.

206 Mit dem Hilfsantrag 5 kombiniert die Beklagte die Merkmale der Hilfsanträge 1 bis 4, ohne dass über die einzelnen Merkmale hinaus ein weiterer darüber hinausreichender Synergieeffekt erzielt würde, was die Beklagte auch nicht behauptet. Damit gelten die Ausführungen zur Patentfähigkeit hinsichtlich der Hilfsanträgen 1 bis 4 in gleicher Weise zum Hilfsantrag 5.

207 6. Die Beklagte kann das Streitpatent auch in der Fassung gemäß Hilfsantrag 6 nicht mit Erfolg verteidigen. Es kann auch hier dahinstehen, ob das zusätzlich in den Patentansprüchen 1, 11 und 12 aufgenommene Merkmal M12.3.4.1Hi6 des Hilfsantrags 6 "wherein the copy of the statistical model (SM) is compressed to a size which is manageable by the receiver" zu einer unzulässigen Erweiterung im Hinblick auf die Ursprungsoffenbarung führt, oder der Gegenstand nach Patentanspruch 12 gemäß Hilfsantrag 6 nicht ausführbar sein könnte, da sich schließlich auch Hilfsantrag 6 gegenüber dem Stand der Technik nach dem Dokument D5a (WO 00/18148 A1) als nicht patentfähig erweist.

208 6.1 Mit dem Hilfsantrag 6 wird die Positionsbestimmung gegenüber der erteilten Fassung ausgestaltet. Dabei ist gegenüber dem Hauptantrag nach Merkmal 12.3.3 Folgendes eingefügt (Gliederung und Übersetzung durch den Senat):

209 12.3.4Hi6 wherein the receiver (R') stores a copy of the statistical model (SM) and determines the location estimate (LE) on the basis of the copy of the statistical model (SM);

12.3.4Hi6 wobei der Empfänger (R') eine Kopie des statistischen Modells (SM) speichert und die Standortschätzung (LE) auf Basis dieser Kopie bestimmt;

12.3.4.1Hi6 wherein the copy of the statistical model (SM) is compressed to a size which is manageable by the receiver.

12.3.4.1Hi6 wobei die Kopie des statistischen Modells (SM) auf eine für den Empfänger handhabbare Größe komprimiert wird.

210 6.2 Gemäß einem Aspekt der Erfindung der D5a kann der Standort einer mobilen Einheit (MU) bestimmt werden, indem eine von der MU aufgenommene Momentaufnahme eines vordefinierten Abschnitts des Hochfrequenzspektrums (HF-Spektrum) mit einer Referenzdatenbank verglichen wird. Hierzu enthält die Referenzdatenbank mehrere an verschiedenen Standorten aufgenommene Momentaufnahmen, wobei das Ergebnis des Vergleichs der Feststellung, ob sich die MU an einem bestimmten Standort befindet, dient. Die D5a betont bereits einleitend, dass diese Ermittlung in der MU durchgeführt werden kann (S. 1 Z. 38-45). Weiter führt sie aus, dass sobald der Fingerabdruck erzeugt ist, seine Zuordnung zu einem bestimmten Ort ermittelt werden muss.Dies erfolgt mithilfe einer Fingerabdruckdatenbank, die eine Reihe von Fingerabdrücken zusammen mit ihren jeweiligen Standortinformationen enthält.In einer Ausführungsform ist die Datenbank im Verarbeitungsmodul der MU gespeichert.Der erzeugte Fingerabdruck wird mit den Fingerabdrücken der Datenbank verglichen, und derjenige Fingerabdruck in der Datenbank, der dem erzeugten Fingerabdruck am ähnlichsten ist, wird als Übereinstimmung ausgewählt (S. 5 Z. 4-11). Zur Datenbankerstellung selbst führt D5a aus, dass diese in einer Ausführungsform durch Offline-Aufnahmen von Fingerabdrücken an verschiedenen Orten erstellt wird, wobei die Fingerabdruckinformationen zusammen mit den Koordinaten des jeweiligen Ortes in die Datenbank eingetragen werden. Zudem können die Fingerabdrücke mithilfe hochempfindlicher Messgeräte erfasst werden, welche es ermöglichen, dass auch sehr nahe beieinanderliegende Orte unterschiedliche Fingerabdrücke aufweisen (D5a S. 7 Z. 34-45).

211 6.3 D5a offenbart das Merkmal 12.3.4Hi6 unmittelbar und eindeutig. Das Merkmal 12.3.4.1Hi6 ist hingegen der D5a nicht unmittelbar zu entnehmen. Jedoch ergibt sich das Merkmal 12.3.4.1Hi6 für die Fachperson naheliegend aus der D5a und kann ein Vorliegen einer erfinderischen Tätigkeit nicht begründen.

212 D5a offenbart, dass eine Positionsbestimmung basierend auf der in der MU, somit in dem Empfänger, gespeicherten Datenbank erfolgen kann, welche zuvor mittels entsprechender Messung erzeugt wird. Die Datenbank stellt ein statistisches Modell im Sinne des Streitpatents dar, wobei die Standortschätzung auf Basis dieser Datenbank bestimmt wird. Die Fachperson liest aus den Ausführungen der D5a mit, dass es sich bei der in der MU gespeicherten Datenbank um eine Kopie einer vorab erstellten Datenbank handelt, da die Datenbankerstellung in der D5a insbesondere unter Verwendung besonders präziser Messtechnik erfolgten Messungen als aufwendig beschrieben ist und somit nicht exklusiv allein für eine MU erzeugt wird. Angesichts des hohen Erstellungsaufwands weiß die Fachperson zudem, dass die Datenbank auch nicht von der MU erzeugt wird und es sich auch deshalb in der MU um eine Kopie handeln muss.

213 Weiter entnimmt die Fachperson den Ausführungen der D5a, dass, wenn in der MU eine Kopie der Datenbank gespeichert werden soll, die Datenbank hierzu eine Größe aufweisen muss, die es der MU möglich macht, diese auch speichern zu können. Damit zeigt die D5a einen Empfänger, der eine Kopie des statistischen Modells speichert und die Standortschätzung auf Basis der Datenstruktur der Datenbank bestimmt. Da der Speicherplatz mobiler Geräte, wie Mobiltelefonen, PDAs oder Palmtops, stets begrenzt ist, wird die Fachperson auch die Möglichkeit einer Komprimierung der Daten vorsehen, um ein Speichern im Empfänger zu unterstützen. Sie gelangt damit naheliegend zum Gegenstand des Patentanspruchs 12 gemäß dem Hilfsantrag 6 ohne erfinderisch tätig zu werden.

214 7. Da die Beklagte, wie in der mündlichen Verhandlung zu Protokoll erklärt, auch die Fassungen der Hilfsanträge 1 bis 6 ausdrücklich als geschlossene Anspruchssätze verteidigt, erweisen diese sich insgesamt als nicht schutzfähig. Die weiter angegriffenen nebengeordneten und abhängigen Patentansprüche der Hilfsanträge teilen das Schicksal von Patentanspruch 12, der sich jeweils nicht als patentfähig erweist (vgl. BGH, Urteil vom 13. September 2016, X ZR 64/14, GRUR 2017, 57 – Datengenerator).

B.

215 Nebenentscheidungen

216 Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs.1 ZPO.

217 Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG i. V. m. § 709 ZPO.
