---
ecli: "ECLI:DE:BPatG:2025:050225U2Ni1.23EP.0"
court: "Bundespatentgericht"
aktenzeichen: "2 Ni 1/23 (EP)"
decided: "2025-02-05"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/JURE259031904.xml"
neuris_doknr: "JURE259031904"
---

# Bundespatentgericht, 2 Ni 1/23 (EP) vom 2025-02-05

## Tenor

In der Patentnichtigkeitssache

…

betreffend das europäische Patent EP 2 922 233

(DE 60 2009 049 574)

hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der mündlichen Verhandlung vom 5. Februar 2025 unter Mitwirkung der Vorsitzenden Richterin Hartlieb sowie der Richter Dipl.-Phys. Dr. rer. nat. Friedrich, Dipl.-Phys. Dr. rer. nat. Zebisch, Dr. Himmelmann und Dr.-Ing. Kapels

für Recht erkannt:

I. Das europäische Patent EP 2 922 233 wird mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt, dass seine Ansprüche folgende Fassung erhalten:

1. A method for mapping a physical hybrid automatic repeat request indicator channel, PHICH, in groups of a plurality of PHICHs, to orthogonal frequency division multiplexing, OFDM, symbols,

each OFDM symbol comprising of a plurality of resource element groups, each resource element group being comprised of four resource elements,

the method comprising:

• determining indexes of resource element groups in which the PHICH is transmitted,

the method being characterised in that said indexes are determined according to a cell identifier, ID, multiplied by the ratio of the number of available resource element groups in the OFDM symbol, having index , in which the repetitionof the PHICH of a PHICH group is transmitted, being an integer of 0 to 2, and the number or of available resource element groups in the first OFDM symbol, having index 0, of a sub-frame or in the second OFDM symbol, having index 1, of a subframe,

the PHICH being transmitted through one, two or three OFDM symbols,

wherein said indexes are determined according to the ratio when the PHICH is transmitted through one or three OFDM symbols, and

wherein said indexes are determined according to the ratio when the PHICH is transmitted through two OFDM symbols and the first PHICH group is started from the second OFDM symbol,

where the index = 0, if the PHICH is transmitted through one OFDM symbol,

where the index denoting an index of the PHICH group including the PHICH, if the PHICH is transmitted through two OFDM symbols, and

where the index , if the PHICH is transmitted through three OFDM symbols,

available resource element groups being resource element groups which can be used for PHICH transmission in the respective OFDM symbol, and

• mapping the PHICH to the OFDM symbols according to the determined indexes.

2. The method of claim 1, wherein, if the PHICH is transmitted through one or three OFDM symbols, the indexes of the resource element groups in which the PHICH is repeatedly transmitted three times are determined using the following equation:

where denotes a cell ID, denotes an index of the repetition of the PHICH, denotes the ratio between the number of available resource element groups in the OFDM symbol and the number of available resource element groups in the first OFDM symbol of the sub-frame, and denotes an index of a PHICH group including the PHICH.

3. The method of claim 1, wherein, if the PHICH is transmitted through two OFDM symbols, the indexes of the resource element groups in which the PHICH is repeatedly transmitted three times are determined using the following equation:

Where denotes a cell ID, denotes an index of the repetition of the PHICH, denotes the ratio between the number of available resource element groups in the OFDM symbol and the number of available resource element groups in the second OFDM symbol of the sub-frame, and denotes an index of a PHICH group including the PHICH.

4. Base station of a multi-carrier cellular mobile communication system adapted for multiplexing signals transmitted to mobile stations, wherein the base station is adapted for carrying out a method according to any of claims 1 to 3.

5. Mobile station in a multi-carrier cellular mobile communication system, the mobile station being adapted to receive a multiplexed signal from the base station according to claim 4, the signal being formed using the method according to any of claims 1 to 3,

the mobile station being further configured to decode the multiplexed signal received from the base station to receive an ACK/NACK transmitted through a PHICH in the multiplexed signal.

6. The mobile station of claim 5, further configured to determine indexes of resource element groups in which a PHICH is transmitted,

wherein said indexes are determined as specified in any one of claims 1 to 3.

II. Im Übrigen wird die Klage abgewiesen.

III. Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.

IV. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.

## Tatbestand

1 Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland in englischer Verfahrenssprache erteilten europäischen Patents EP 2 922 233 (deutsches Aktenzeichen DE 60 2009 049 574.7) (Streitpatent), dessen Stammanmeldung am 18. Februar 2009 unter Inanspruchnahme der Prioritäten US 29895 P vom 19. Februar 2008 und KR 20080124084 vom 8. Dezember 2008 angemeldet worden ist, und das die Bezeichnung „METHOD FOR MAPPING PHYSICAL HYBRID AUTOMATIC REPEAT REQUEST INDICATOR CHANNEL“ („Verfahren zur Abbildung eines physikalischen Kanals zur Anzeige einer hybriden automatischen Wiederholungsaufforderung“) trägt. Der Hinweis auf die Erteilung des Streitpatents wurde am 22. November 2017 veröffentlicht.

2 Das Streitpatent betrifft ein Abbildungsverfahren eines Signals auf die Frequenz und OFDM (Orthogonal Frequency Division Multiplexing) Zeichenbereiche, das in der Abwärtsverbindung eines Mobilfunk-Paketübertragungssystems übertragen wird (vgl. Streitpatentschrift, Abs. [0001]).

3 Das in vollem Umfang angegriffene Streitpatent umfasst den unabhängigen Verfahrensanspruch 1, die unabhängigen Erzeugnisansprüche 5 und 6 sowie die direkt auf Anspruch 1 rückbezogenen Unteransprüche 2 bis 4.

4 Der erteilte Patentanspruch 1 lautet gemäß der Streitpatentschrift EP 2 922 233 B1 mit einer bei unverändertem Wortlaut eingefügten Gliederung NK8 der Klägerin, die auch von der Beklagten übernommen wurde, folgendermaßen:

5 1.

A method for mapping a physical hybrid automatic repeat request indicator channel, PHICH, in groups of a plurality of PHICHs, to orthogonal frequency division multiplexing, OFDM, symbols,

Verfahren zum Abbilden eines physikalischen Hybridautomatikwiederholungsanforderung-Indikatorkanals, PHICH, in Gruppen von einer Mehrzahl von PHICHs, auf Orthogonales-Frequenzmultiplexverfahren, OFDM, - Symbole, wobei

1.1

each OFDM symbol comprising of a plurality of resource element groups, each resource element group being comprised of four resource elements,the method comprising:

jedes OFDM-Symbol eine Mehrzahl von Ressourcenelementgruppen umfasst, jede Ressourcenelementgruppe vier Ressourcenelemente umfasst, wobei das Verfahren umfasst:

1.2

• determining indexes of resource element groups in which the PHICH is transmitted, the method being characterised in that

• Bestimmen von Indizes von Ressourcenelementgruppen, in welchen der PHICH übertragen wird, wobei das Verfahren dadurch charakterisiert ist, dass

1.2.1

said indexes are determined according to the ratio or

die Indizes gemäß dem Verhältnis oder

1.2.1.a

of the number of available resource element groups in the OFDM symbol, having index n which the th repetition of the PHICH of a PHICH group is transmitted, being an integer of 0 to 2,

der Anzahl von verfügbaren Ressourcenelementgruppen in dem OFDM-Symbol, welches den Index aufweist, in welchem die te Wiederholung des PHICH von einer PHICH-Gruppe übertragen wird, wobei eine ganze Zahl von 0 bis 2 ist, und

1.2.1.b

and the number of available resource element groups in the first OFDM symbol, having index 0, of a subframe or in the second OFDM symbol, having index 1, of a sub-frame,

der Anzahl von verfügbaren Ressourcenelementgruppen in dem ersten OFDM-Symbol, welches Index 0 aufweist, von einem Sub-Frame oder in dem zweiten OFDM-Symbol, welches Index 1 aufweist, von einem Sub-Frame,

1.2.2

the PHICH being transmitted through one, two or three OFDM symbols,

der PHICH durch einen, zwei oder drei OFDM-Symbole übertragen wird,

1.2.2.a

where the index , if the PHICH is transmitted through one OFDM symbol,

wobei der Index , wenn der PHICH durch ein OFDM-Symbol übertragen wird,

1.2.2.b

where the index denoting an index of the PHICH group including the PHICH, if the PHICH is transmitted through two OFDM symbols, and

wobei der Index wobei einen Index der PHICH-Gruppe, welche den PHICH umfasst, bezeichnet, wenn der PHICH durch zwei OFDM-Symbole übertragen wird, und

1.2.2.c

where the index , if the PHICH is transmitted through three OFDM symbols,

wobei der Index , wenn der PHICH durch drei OFDM-Symbole übertragen wird,

1.2.1.c

available resource element groups being resource element groups which can be used for PHICH transmission in the respective OFDM symbol, and

verfügbare Ressourcenelementgruppen Ressourcenelementgruppen sind, welche für eine PHICH-Übertragung in dem jeweiligen OFDM-Symbol verwendet werden können, und

1.3

• mapping the PHICH to the OFDM symbols according to the determined indexes.

• Abbilden des PHICH auf die OFDM-Symbole gemäß den bestimmten Indizes.

6 Die zu Anspruch 1 nebengeordneten Ansprüche 5 und 6 betreffen eine Basisstation und eine Mobilstation und lauten:

7 Anspruch 5:

8 5. Base station of a multi-carrier cellular mobile communication system adapted for multiplexing signals transmitted to mobile stations, wherein the base station is adapted for carrying out a method according to any of claims 1 to 4.

9 Anspruch 6:

10 6. Mobile station in a multi-carrier cellular mobile communication system, the mobile station being adapted to receive a multiplexed signal from the base station according to claim 5, the signal being formed using the method according to any of claims 1 to 4.

11 Zum Wortlaut der ebenfalls angegriffenen Unteransprüche 2 bis 4 wird auf die Streitpatentschrift verwiesen.

12 Die Klägerin stützt ihre Klage auf die Nichtigkeitsgründe der mangelnden Patentfähigkeit mit Blick auf fehlende Neuheit und fehlende erfinderische Tätigkeit sowie darauf, dass der Gegenstand des Streitpatents über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinausgehe.

13 Nach ihrer Auffassung seien die im Laufe des Verfahrens gestellten Hilfsanträge der Beklagten unzulässig und auch die Gegenstände der Hilfsanträge nicht patentfähig.

14 Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:

15 NK1 Verletzungsklageschrift der Beklagten gegen die Klägerin und die … vom 8. Juli 2022 (teilweise geschwärzt; ohne Anlagen);

16 NK2 DPMA: Registerauszug zum Aktenzeichen 60 2009 049 574.7; Stand am 3. Februar 2023;

17 NK3 EP 2 922 233 B1 (Streitpatentschrift);

18 NK4 EP 2 922 233 A1 (Offenlegungsschrift);

19 NK5 Stammanmeldung des Streitpatents in der ursprünglich eingereichten Fassung;

20 NK6 Prioritätsunterlagen US 61/029,895;

21 NK6a englische Übersetzung Prioritätsunterlagen US 61/029,895;

22 NK7 Prioritätsunterlagen KR 10 2008 0 124 084;

23 NK8 Merkmalsgliederung des Anspruchs 1 des Streitpatents (englische Fassung und deutsche Übersetzung);

24 NK9 US 2009/0274037 A1;

25 NK10 „Application Data Sheet“ der Nachanmeldung vom 18. Februar 2009;

26 NK11 „PATENT ASSIGNMENT“ von X … und Y … an die Z … Inc. … vom 18. Juni 2009.

27 D1 3GPP TS 36.211, V8.2.0 (2008-03); 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Channels and Modulation (Release 8);

28 D2 3GPP TS 36.211, V8.4.0 (2008-09); 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; Evolved Universal Terrestrial Radio Access (E-UTRA); Physical Channels and Modulation (Release 8);

29 D3 3GPP TSG RAN WG1 #52, Sorrento, Italy, February 11-15, 2008, R1-081063, LGE, Samsung, Nortel, Panasonic, Motorola, Ericsson, Nokia, NSN, Qualcom: „Text proposal for PHICH to RE mapping with cell ID“;

30 D4 3GPP TSG RAN WG1 Meeting # 52, Sorrento, Italy, February 11-15, 2008, R1-080898, „DRAFT CHANGE REQUEST”;

31 D5 3GPP TSG RAN WG1 Meeting #51bis, Sevilla, Spain, January 14-18, 2008, R1-080029, Samsung, „PHICH mapping”;

32 D6 3GPP TSG RAN WG1 # 52, Sorrento, Italy, February 11-15, 2008, R1-080997, LG Electronics, „Remaining issues on PHICH indexing and PHICH to RE mapping“.

33 Das Streitpatent könne die Priorität vom 19. Februar 2008 (US 29895 P) sowohl aus formellen Gründen als auch aus materiellen Gründen nicht wirksam in Anspruch nehmen, so dass die Druckschrift D1 zu berücksichtigen sei, die als Zeitpunkt ihrer Veröffentlichung in ihrem Titelblatt den März 2008 angibt, einen Zeitpunkt der zwischen dem Anmeldetag der Prioritätsanmeldung und dem Anmeldetag des Streitpatents liegt. Zum einen fehle es an der notwendigen Anmelderidentität und zum anderen sei das mit Anspruch 1 beanspruchte Verfahren dort nicht offenbart.

34 Die Klägerin führt aus, dass es für eine wirksame Inanspruchnahme der ersten Priorität vom 19. Februar 2008 der wirksamen Übertragung des Prioritätsrechts von den Anmeldern der Prioritätsschrift US 61/029,895 P (Anlage NK 6/6a) auf die Anmelderin des Stammpatents (Z … Inc.) bedürfe. Dies werde von ihr bestritten. Die völlig unsubstantiierte Behauptung der Beklagten könne diese nicht davon befreien, im konkreten Fall darzulegen und nachzuweisen, dass auch eine rechtzeitige Übertragung des Prioritätsrechts stattgefunden habe. So obläge es der Beklagten, eine entsprechende Vereinbarung zwischen den Erfindern und der Z … Inc. vorzulegen. Es bestünden somit konkrete Umstände, aus denen sich die Unwirksamkeit der Inanspruchnahme der ersten Priorität ergebe. Die nach der Rechtsprechung des BGH für die rechtmäßige Inanspruchnahme einer Priorität geltende Vermutung sei vorliegend widerlegt. Damit habe die Klägerin ihrer Darlegungs- und Beweislast genüge getan.

35 Die Klägerin stellt den Antrag,

36 das europäische Patent EP 2 922 233 in vollem Umfang mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.

37 Die Beklagte stellt zuletzt den Antrag,

38 die Klage abzuweisen,

39 hilfsweise

40 das europäische Patent EP 2 922 233 unter Klageabweisung im Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig zu erklären, dass seine Patentansprüche die Fassung eines der Hilfsanträge

41 - Hilfsantrag 1 vom 18. September 2023,

42 - Hilfsantrag 1‘: Ansprüche 1-6 von Hilfsantrag 1,

43 - Hilfsantrag 1a vom 2. Januar 2025,

44 - Hilfsantrag 2 vom 18. September 2023,

45 - Hilfsantrag 2‘: Ansprüche 1-6 von Hilfsantrag 2,

46 - Hilfsantrag 2‘‘ vom 5. Februar 2025,

47 - Hilfsantrag 2‘‘‘ vom 5. Februar 2025,

48 - Hilfsantrag 2a vom 2. Januar 2025,

49 - Hilfsantrag 3 vom 18. September 2023,

50 - Hilfsantrag 3‘: Ansprüche 1-6 von Hilfsantrag 3,

51 - Hilfsantrag 3a vom 2. Januar 2025,

52 - Hilfsantrag 4 vom 2. Januar 2025,

53 - Hilfsantrag 4a vom 2. Januar 2025,

54 - Hilfsantrag 5 vom 2. Januar 2025,

55 - Hilfsantrag 5a vom 2. Januar 2025

56 in dieser Reihenfolge erhalten,

57 weiter hilfsweise,

58 die Klage abzuweisen, soweit sie sich gegen das Patent in der Fassung eines der Hilfsanträge 1-5, in denen jeweils die Mobilstationsansprüche gestrichen sind, richtet.

59 Nachdem der Senat den Parteien eingangs einen rechtlichen Hinweis zur Kenntnis gegeben hat, überreicht die Beklagte in der mündlichen Verhandlung vom 5. Februar 2025 dem Senat den Hilfsantrage 2‘‘ und nach einem weiteren rechtlichen Hinweis den Hilfsantrag 2‘‘‘ und der Klägerin Kopien dieser Hilfsanträge.

60 Die Beklagte erklärt in der mündlichen Verhandlung vom 5. Februar 2025, dass sie die Patentansprüche gemäß Hauptantrag und den Hilfsanträgen als geschlossene Anspruchssätze ansehe, die jeweils insgesamt beansprucht würden.

61 Die Beklagte, die das Streitpatent mit einem Hauptantrag und hilfsweise beschränkt mit zwanzig Hilfsanträgen verteidigt, tritt der Argumentation der Klägerin in allen wesentlichen Punkten entgegen und erachtet den Gegenstand des Streitpatents für patentfähig. Sie ist der Ansicht, das Streitpatent nehme die Priorität der US-Anmeldung US 29895 P vom 19. Februar 2008 wirksam in Anspruch, so dass die Entgegenhaltungen D1 und D2 für das Streitpatent keinen Stand der Technik darstellen würden. Die Entgegenhaltungen D3 bis D6 nähmen die Erfindung des Streitpatents nicht neuheitsschädlich vorweg und würden diese dem Fachmann auch nicht nahelegen. Der Gegenstand des Anspruchs 1 des Streitpatents gehe nicht über den Inhalt der Anmeldung des Stammpatents hinaus. Die beanspruchte Lehre sei jedenfalls in der Fassung eines der Hilfsanträge patentfähig.

62 In den Hilfsanträgen 1, 1‘ und 1a vom 18. September 2023 (Hilfsantrag 1) bzw. vom 2. Januar 2025 (Hilfsanträge 1’ und 1a) wurden in den Anspruch 1 zusätzlich die Merkmale

63 1.2.1.dH1 wherein said indexes are determined according to the ratio when the PHICH is transmitted through one or three OFDM symbols, and

64 1.2.1.eH1 wherein said indexes are determined according to the ratio when the PHICH is transmitted through two OFDM symbols,

65 zwischen das Merkmal 1.2.2 und 1.2.2a eingefügt.

66 Im Anspruch 1 der Hilfsanträge 2, 2‘ und 2a vom 18. September 2023 (Hilfsantrag 2) bzw. vom 2. Januar 2025 (Hilfsanträge 2’ und 2a) ist das Merkmal 1.2.1.eH1 durch das Merkmal

67 1.2.1.eH2 wherein said indexes are determined according to the ratio when the PHICH is transmitted through two OFDM symbols and the first PHICH group is started from the second OFDM symbol,

68 ersetzt.

69 Anspruch 1 des Hilfsantrags 2‘‘ vom 5. Februar 2025 hat folgenden Wortlaut:

70 1. A method for mapping a physical hybrid automatic repeat request indicator channel, PHICH, in groups of a plurality of PHICHs, to orthogonal frequency division multiplexing, OFDM, symbols,

71 each OFDM symbol comprising of a plurality of resource element groups, each resource element group being comprised of four resource elements,

72 the method comprising:

73 • determining indexes of resource element groups in which the PHICH is transmitted,

74 the method being characterised in that said indexes are determined according to the ratio or of the numbe of available resource element groups in the OFDM symbol, having index in which the repetitionof the PHICH of a PHICH group is transmitted, being an integer of 0 to 2, and the number of available resource element groups in the first OFDM symbol, having index 0, of a sub-frame or in the second OFDM symbol, having index 1, of a subframe,

75 the PHICH being transmitted through one, two or three OFDM symbols,

76 wherein said indexes are determined according to the ratio when the PHICH is transmitted through one or three OFDM symbols, and

77 wherein said indexes are determined according to the ratio when the PHICH is transmitted through two OFDM symbols and the first PHICH group is started from the second OFDM symbol,

78 where the index = 0, if the PHICH is transmitted through one OFDM symbol,

79 where the index denoting an index of the PHICH group including the PHICH, if the PHICH is transmitted through two OFDM symbols, and

80 where the index if the PHICH is transmitted through three OFDM symbols,

81 available resource element groups being resource element groups which can be used for PHICH transmission in the respective OFDM symbol, and

82 • mapping the PHICH to the OFDM symbols according to the determined indexes.

83 Hilfsantrag 2‘‘‘ vom 5. Februar 2025 ist dem Tenor zu entnehmen.

84 Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

## Entscheidungsgründe

85 Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG bzw. Art. 138 Abs. 1 lit. a) EPÜ, beide i. V. m. Art. 52, 54 und 56 EPÜ sowie der Nichtigkeitsgrund der unzulässigen Erweiterung nach Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜbkG bzw.Art. 138 Abs. 1 lit. c) EPÜ und Art. 123 Abs. 2 EPÜ geltend gemacht werden, ist zulässig.

86 Die Klage ist teilweise begründet. Zwar hat das Streitpatent weder in seiner erteilten Fassung noch in der Fassung der Hilfsanträge 1, 1‘, 1a, 2, 2‘ und 2‘‘ Bestand und ist deshalb insoweit für nichtig zu erklären. Das Streitpatent hat indes in der Fassung des Hilfsantrags 2‘‘‘ vom 5. Februar 2025 Bestand.

I.

87 1. Das Streitpatent betrifft ein Abbildungsverfahren auf die Frequenz und OFDM (Orthogonal Frequency Division Multiplexing) Zeichenbereiche eines Signals, das in der Abwärtsverbindung eines Mobilfunk-Paketübertragungssystems übertragen wird (vgl. Abs. [0001] der europäischen Patentschrift NK3).

88 Gemäß der Beschreibung des Streitpatents soll ein Empfänger einen Sender in einem Mobilfunksystem bei der Übertragung eines Pakets darüber informieren, ob das Paket erfolgreich empfangen wurde. Wenn der Empfang erfolgreich ist, übertrage der Empfänger ein Bestätigungssignal (ACK), um den Sender dazu zu veranlassen, dass er ein neues Paket sendet. Versagt der Empfang des Pakets, übertrage der Empfänger eine negative Bestätigung (NACK), die den Sender dazu veranlasse, das Paket erneut zu senden. Dieser Vorgang werde automatische Wiederholungsanfrage (Automatic Repeat Request – ARQ) genannt. Inzwischen sei hybride ARQ (HARQ), die eine Kombination von ARQ und einem Kanalcodierungsschema sei, vorgeschlagen worden. HARQ verringere die Fehlerrate, indem sie ein wiederholt gesendetes Paket mit einem vorhergehend erhaltenen Paket kombiniere und die Systemeffizienz verbessere. Um den Durchsatz des Systems zu erhöhen, erfordere HARQ eine im Vergleich zur herkömmlichen ARQ schnellere ACK/NACK Antwort des Empfängers. Deshalb werde die ACK/NACK-Antwort in HARQ durch eine Signalisierungsmethode auf einem physikalischen Kanal übertragen. Das HARQ-Schema könne grob in reine Wiederholung (Chase Combining - CC) und inkrementelle Redundanz (Incremental Redundancy – IR) eingeteilt werden. Beim CC-Verfahren werde ein Paket erneut gesendet, indem das gleiche Modulationsverfahren und die gleiche Kodierungsrate verwendet werden wie bei der Übertragung eines vorhergehenden Pakets. Beim IR-Verfahren werde ein Paket erneut versendet, indem ein anderes Modulationsverfahren und eine andere Kodierungsrate als bei einem vorhergehenden verwendet werden. In diesem Fall könne der Empfänger die Systemleistungsfähigkeit durch Kodierungsvielfältigkeit erhöhen.

89 In einem Vielfachträger Mobilfunksystem übertragen Mobilstationen, die zu einer oder einer Mehrzahl von Funkzellen gehören, ein Aufwärtsdatenpaket zu einer Basisstation. Dies bedeute, da eine Mehrzahl von Mobilstationen innerhalb eines Unterrahmens ein Aufwärtsdatenpaket übertragen könne, dass die Basisstation in der Lage sein müsse, ACK/NACK-Signale zu einer Mehrzahl von Mobilstationen innerhalb eines Unterrahmens zu übertragen. Wenn die Basisstation eine Vielzahl von ACK/NACK-Signalen zu den Mobilstationen innerhalb eines Unterrahmens unter Nutzung eines CDMA-Schemas innerhalb eines Teil-Zeit-Frequenzbereichs eines Abwärtsübertragungsbandes eines Mehrfachträgersystems übertrage, würden ACK/NACK-Signale unterschiedlicher Mobilstationen durch orthogonale Codes oder quasiorthogonale Codes in Verbindung mit einem Zeit-Frequenzbereich voneinander unterschieden. Werde eine Quadraturphasenumtastungsübertragung (QPSK) durchgeführt, könnten die ACK/NACK-Signale durch unterschiedliche orthogonale Phasenkomponenten voneinander getrennt werden.

90 Würden die ACK/NACK-Signale unter Verwendung eines CDMA-Multiplexverfahrens zur Übertragung einer Mehrzahl von ACK/NACK-Signalen innerhalb eines Unterrahmens gesendet, sollte die Antwortcharakteristik des Abwärtsübertragungskanals in einem Zeit-Frequenz-Bereich, in dem die ACK/NACK-Signale übertragen werden, nicht groß geändert werden. Dies deshalb, weil dann, wenn die Orthogonalität zwischen den unterschiedlichen ACK/NACK-Signalen erhalten bleibe, ein Empfänger eine zufriedenstellende Empfangsleistungsfähigkeit aufweisen könne, ohne einen speziellen Empfangsalgorithmus wie einen Kanalausgleich durchführen zu müssen. Folglich sollte das CDMA-Multiplexen der ACK/NACK-Signale innerhalb des Zeit-Frequenz-Bereichs durchgeführt werden, in dem die Mobilfunkantwort nicht wesentlich verändert wird. Wenn aber die Kanalqualität einer bestimmten Mobilstation in dem Zeit-Frequenzbereich, in dem die ACK/NACK-Signale gesendet würden, schlecht sei, werde die ACK/NACK-Empfangsleistungsfähigkeit der Mobilstation stark herabgesetzt.

91 Folglich würden die ACK/NACK-Signale zu jeder Mobilstation innerhalb eines Unterrahmens wiederholt über getrennte Zeit-Frequenz-Bereiche innerhalb einer Vielzahl von Zeit-Frequenz-Linien übertragen, und die ACK/NACK-Signale könnten in jedem Zeit-Frequenz-Bereich mit anderen Mobilstationen durch CDMA gemultiplext werden. So könne der Empfänger eine Zeit-Frequenz-Diversität zum Empfangen des ACK/NACK Signals erlangen.

92 Jedoch gebe es beim herkömmlichen Physikalische-Kanal-HARQ-Anzeigerabbildungsverfahren (PHICH mapping method) das Problem, dass PHICH-Gruppen in verschiedenen benachbarten Funkzellen Schwierigkeiten haben, Kollisionen zu vermeiden. Dies werde in Fig. 1 gezeigt, wovon hier die von der Klägerin aufbereitete Version gezeigt wird (vgl. Abs. [0001] bis [0006] der Streitpatentschrift NK3).

93 Diese Figur 1 bedarf einer Erläuterung, die die Klägerin in ihrem Klageschriftsatz wie folgt angibt:

94 (1) Die Figur 1 des Streitpatents zeigt das Mappen von PHICH-Gruppen zum Übertragen von ACK/NACK-Signalen über den Frequenzbereich eines einzelnen OFDM-Symbols für fünf verschiedene Funkzellen. Jede Funkzelle ist gekennzeichnet durch einen Zellenidentifizierer („cell ID“).

95 (2) Ein OFDM-Symbol (siehe „OS 0“, orange Markierung in der oben eingeblendeten Figur) setzt sich aus mehreren Ressourcenelementgruppen („resource element groups (REGs)“) zusammen. Eine Ressourcenelementgruppe umfasst dabei vier Ressourcenelemente („resource elements (REs)“, siehe Streitpatentschrift NK3, Abs. [0024]). Die REGs sind in der Figur 1 als Kästchen dargestellt und erstrecken sich über den gesamten Frequenzbereich des OFDM-Symbols.

96 (3) Eine ACK-Nachricht wird mit einem Bit „1“ und eine NACK-Nachricht mit einem Bit „0“ codiert. Im zum Prioritätszeitpunkt aktuellen LTE-Standard wird ein PHICH mit je einem ACK- oder NACK-Signal dreimal übertragen, um die bereits beschriebene Diversität zu erhalten. Benötigt werden also insgesamt drei Bits („111“ bzw. „000“). Wird zusätzlich ein Spreizfaktor („spreading factor“) von vier verwendet (siehe NK3, Abs. [0025]), resultieren hieraus für eine ACK/NACK-Nachricht 12 Bits (4 x 3). Zur Übertragung der 12 Bits werden also 12 REs und somit drei REGs benötigt, d.h. für jede Wiederholung eine REG (vgl. NK3, Abs. [0025]).

97 (4) Durch das bereits erwähnte Multiplexing (CDMA-Techniken) ist es dabei möglich, dass mehrere PHICHs für verschiedene Mobilstationen durch dieselben REGs übertragen werden. Diese PHICHs, die sich die gleichen REGs teilen, werden in einer sogenannten PHICH-Gruppe („PHICH group“) zusammengefasst. Die Figur 1 zeigt exemplarisch zwei PHICH-Gruppen 1 und 2 (in gelb und grün hervorgehoben), die aufgrund der dreifachen Übertragung bei einem Spreizfaktor von vier jeweils auf drei REGs eines OFDM-Symbols gemappt wurden, um Frequenz-Diversität zu erreichen.

98 (5) Zur Übertragung des PHICH stehen aber nur solche REGs eines OFDM-Symbols zur Verfügung, die nicht bereits anderweitig besetzt sind. In der Figur 1 wird beispielsweise über das OFDM-Symbol auch der „Physical Control Format Indicator Channel (PCFICH)“ gesendet (siehe oben in rot), weshalb die entsprechenden Frequenzbereiche nicht für das Übertragen des PHICH zur Verfügung stehen.

99 (6) Steht wie in der Figur 1 nur ein OFDM-Symbol zur Verfügung, wird der PHICH möglichst gleichmäßig über das Frequenzspektrum des OFDM-Symbols verteilt (siehe NK3, Abs. [0022]: „If the PHICH is transmitted through one OFDM symbol, the PHICH repeating three times should be evenly distributed over a frequency bandwidth of one OFDM symbol.“). Damit wird die maximale Frequenzdiversität erreicht, d.h. die ACK/NACK-Signale werden zeitgleich über drei unterschiedliche Trägerfrequenzen übermittelt, die so weit wie möglich voneinander entfernt sind. Die gleichmäßige Verteilung über das zur Verfügung stehende Frequenzspektrum führt zu dem möglichst weiten Abstand der einzelnen Übertragungen voneinander. Genau dieses dem Fachmann allgemein bekannte Prinzip findet auch bei dem PCFICH Anwendung, wie ebenfalls aus der Figur 1 ersichtlich ist.

100 (7) Wird bei Verteilung einer PHICH-Gruppe über den zur Verfügung stehenden Frequenzbereich eines OFDM-Symbols allerdings die zugrundeliegende Funkzelle ignoriert, führt das zu dem Ergebnis, dass in verschiedenen Funkzellen die jeweiligen PHICH-Gruppen einem identischen Frequenzbereich zugeordnet werden können. Dies ist in der oben eingeblendeten Figur 1 im Hinblick auf die PHICH-Gruppen 1 und 2 in Relation zur Frequenz des OFDM-Symbols ersichtlich. Abgesehen von kleinen Verschiebungen aufgrund des PCFICH werden stets die identischen Frequenzbereiche in den jeweiligen Funkzellen verwendet (siehe blaue Umrandungen).

101 (8) Nach der Streitpatentschrift könne es durch die Verwendung der gleichen Frequenzbereiche beim Übertragen der PHICHs insbesondere im Randbereich von Funkzellen zu Interferenzen zwischen verschiedenen Funkzellen kommen, wodurch sich die Übertragungseffizienz des PHICH verschlechtern könne.

102 2. Hiervon ausgehend nennt das Streitpatent in Absatz [0008] die Aufgabe, ein PHICH-Abbildungsverfahren zur Verfügung zu stellen, bei dem durch die Wiederholung des PHICH keine Interferenz zwischen benachbarten Funkzellen mit unterschiedlichen Funkzellen IDs entsteht unter Beachtung der zur Verfügung stehenden Ressourcenelemente, die sich mit den OFDM-Symbolen ändern.

103 3. Diese Aufgabe wird durch das Verfahren nach dem erteilten Anspruch 1, die Basisstation nach dem erteilten Anspruch 5 und die Mobilstation nach dem erteilten Anspruch 6 gelöst.

104 Die Erfindung des Streitpatents besteht in einem Verfahren, das von der Basisstation durchgeführt wird und dessen Ergebnis von der Mobilstation verstanden werden soll. Dabei werden die ACK/NACK-Antworten einer Basisstation, die Hybridautomatikwiederholungsanforderungen, auf OFDM-Symbole umgesetzt, im Fachjargon „gemappt“. Ein OFDM-Symbol erstreckt sich über die gesamte Bandbreite des OFDM-Signals und ist eine bestimmte Zeit lang. Seine Bandbreite ist in eine Vielzahl von Ressourcenelementen aufgeteilt.

105 Beim Verfahren des Streitpatents wird von Ressourcenelementgruppen (REG) ausgegangen, die jeweils 4 Ressourcenelemente (RE) enthalten. Ein einzelnes ACK/NACK-Signal ist durch nur ein Bit darstellbar, so beispielsweise durch eine 1 für ACK und eine 0 für NACK. Es wird aber nicht nur ein einzelnes Bit gesendet, sondern die Bits werden gespreizt, d.h. es werden mehrere Bits gesendet, um weniger fehleranfällig zu sein. Die Anzahl der gesendeten Bits wird als Spreizungsfaktor bezeichnet. So wird statt einer einzelnen 1 beispielsweise bei einem Spreizungsfaktor von 4 die 4 Bit lange Kombination 1111 gesendet, bei einer 0 die Kombination 0000. Jedes dieser nun 4 Bits wird in einem Ressourcenelement (RE) gesendet. 4 von diesen Ressourcenelementen werden nach Anspruch 1 zu einer Ressourcenelementgruppe (REG) zusammengefasst. Dabei teilen sich mehrere Mobilstationen ein Ressourcenelement und damit auch eine Ressourcenelementgruppe. Dies ist in der hier wiedergegebenen Fig. 3 dargestellt.

106 Wie aus Fig. 3 ersichtlich ist, werden zusätzlich auch noch andere Informationen in den OFDM-Symbolen mitübertragen, was zur Folge hat, dass nicht alle Ressourcenelemente für die Übertragung der ACK/NACK-Signale zur Verfügung stehen. In Figur 3 sind dies die mit RS0 bis RS3 bezeichneten Ressourcenelemente, die in den ersten beiden OFDM-Symbolen nicht für die Übertragung von ACK/NACK-Signalen genutzt werden können, so dass in den ersten beiden Symbolen weniger REGs untergebracht werden können als im 3. OFDM-Symbol. Die Ressourcenelementgruppen werden von links nach rechts, mit 0 beginnend, nummeriert. Dies bedeutet, dass das erste und das zweite OFDM-Symbol im linken Teil des Frequenzspektrums die Ressourcenelementgruppen 0 und 1 und das 3. OFDM-Symbol die Ressourcenelementgruppen 0 bis 3 aufweisen. Das Verfahren besteht nun darin, dass die Indizes der Ressourcenelementgruppen, in denen die ACK/NACK-Signale, also der PHICH, übertragen wird, zunächst bestimmt werden (Merkmalsgruppe 1.2) und dann die ACK/NACK-Signale auf die ermittelten Ressourcenelementgruppen des OFDM-Signals abgebildet werden (Merkmal 1.3), also in diesen übertragen werden.

107 Der Hauptteil des Anspruchs 1 beschäftigt sich mit der Bestimmung der Indizes. Dabei wird beansprucht, dass die Indizes in Abhängigkeit von dem Verhältnis oder bestimmt wird. Dabei ist die Anzahl von zur Verfügung stehenden REGs im OFDM-Symbol mit der Nummer 0, die Anzahl von zur Verfügung stehenden REGs im OFDM-Symbol mit der Nummer 1 und , die Anzahl von zur Verfügung stehenden REGs in dem OFDM-Symbol in den die -te Wiederholung übertragen wird. Dabei ist 0, 1 oder 2. Dies bedeutet, dass der PHICH drei Ausführungen des gespreizten ACK/NACK-Signals enthält, die mit 0, 1 und 2 durchnummeriert werden. Eine genaue Berechnung der Indizes wird in Anspruch 1 noch nicht angegeben.

108 Es wird jedoch im Merkmalskomplex 1.2.2 noch eine Angabe zum Index , also des OFDM-Symbols der -ten Wiederholung gemacht. Hierfür werden 3 Fälle unterschieden, nämlich, dass der PHICH in 1, 2 oder 3 OFDM-Symbolen übertragen wird. Die Übertragung in einem OFDM-Symbol ist einfach. Dort erfolgen die Übertragungen aller drei Ausführungen, die als Wiederholungen bezeichnet werden, im OFDM-Symbol mit dem Index 0, also dem einzigen OFDM-Symbol (Merkmal 1.2.2.a). Bei drei OFDM-Symbolen wird festgelegt, dass jede der Wiederholungen in einem anderen der drei OFDM-Symbole erfolgen soll (1.2.2c). Bei zwei OFDM-Symbolen erfolgt die Übertragung ebenfalls auf die OFDM-Symbole verteilt. Bei der einen Hälfte zwei Wiederholungen im ersten OFDM-Symbol und eine im zweiten OFDM-Symbol, bei der anderen Hälfte umgekehrt. Dies wird formal im Merkmal 1.2.2b angegeben und in der hier wiedergegebenen Figur 9 dargestellt.

109 4. Als hier zuständiger Fachmann ist ein berufserfahrener Ingenieur der Nachrichtentechnik oder ein Informatiker mit Hochschulabschluss zu definieren, der im Bereich der Entwicklung von Verfahren für die Nachrichtenübertragung in Funknetzwerken tätig ist und deren Standardisierung aufmerksam verfolgt.

110 5. Entgegen der Ansicht der Klägerin nimmt das Streitpatent die Priorität der provisorischen US-amerikanischen Anmeldung 61/029,895 (NK6) vom 19. Februar 2008 formal zu Recht in Anspruch.

111 5.1. Das Streitpatent wurde von der Z … Inc. angemeldet, während die US-amerikanische Prioritätsanmeldung von X … und Y …, den Erfindern, getätigt wurde, die in der Stammanmeldung und auch im Streitpatent als Erfinder genannt werden.

112 Der Senat hat keinen Zweifel daran, dass die für eine wirksame Inanspruchnahme der ersten Priorität vom 19. Februar 2008 erforderliche Übertragung des Prioritätsrechts von den Anmeldern der Prioritätsschrift US 61/029,895 P (Anlage NK 6/6a) auf die Anmelderin des Streitpatents (Z … Inc.) erfolgt ist. Entgegen der Ansicht der Klägerin obliegt es vorliegend nicht der Beklagten, eine Vereinbarung über die Übertragung des Prioritätsrechts zwischen den Erfindern und der Z … Inc. vorzulegen, um eine Berechtigung zur Inanspruchnahme der Priorität zu beweisen. Es obliegt vielmehr der Klägerin, nachzuweisen, dass es im konkreten Fall an einer entsprechenden Berechtigung fehlt.

113 So hat die Große Beschwerdekammer des EPA hat am 10. Oktober 2023 (verbundene Verfahren G 1/22 und G 2/22; ABl. EPA, 2024, A50) zu Art. 87 Abs. 1 EPÜ entschieden:

114 „Leitsatz I: Es gibt eine widerlegbare Vermutung nach dem autonomen Recht des EPÜ, dass ein Anmelder, der eine Priorität unter Beachtung des Art. 88 Abs. 1 EPÜ und der entsprechenden Regeln der Ausführungsordnung beansprucht, zur Inanspruchnahme der Priorität berechtigt ist.

115 Leitsatz II: Die widerlegbare Vermutung gilt auch in Fällen, in denen die europäische Patentanmeldung auf einer PCT-Anmeldung beruht und/oder der bzw. die Prioritätsanmelder und der bzw. die Nachanmelder nicht identisch sind. ...

116 Rn. 110: Die widerlegbare Vermutung ist mit einer Umkehr der Beweislast verbunden, d. h. ein Beteiligter, der die Prioritätsberechtigung des Nachanmelders anficht, muss nachweisen, dass die Berechtigung fehlt.“

117 Der BGH ist dieser Auslegung der Regelung in Art. 87 Abs. 1 EPÜ beigetreten und hat in dem Urteil Sorafenib-Tosylat (Urteil vom 28. November 2023, X ZR 83/21, juris; Bestätigung im Urteil Happy Bit (Urteil vom 9. Januar 2024, X ZR 74/21, juris)) entschieden:

118 „Leitsatz 2a.: Für die Berechtigung zur Inanspruchnahme eines Prioritätsrechts bei der Anmeldung eines europäischen Patents spricht eine widerlegbare Vermutung.

119 Leitsatz 3.: Im Patentnichtigkeitsverfahren liegt die Darlegungs- und Beweislast hinsichtlich der Voraussetzungen für eine wirksame Inanspruchnahme der Priorität beim Nichtigkeitskläger.

120 Rn. 123: Ungeachtet des im Patentnichtigkeitsverfahren geltenden Untersuchungsgrundsatzes geht es zu Lasten des Nichtigkeitsklägers, wenn das Ergebnis der Verhandlung und der Beweisaufnahme zu keiner eindeutigen Feststellung im Sinne des Klagevorbringens geführt hat. Nachdem das Patent ordnungsgemäß erteilt worden ist, kann dem Patentinhaber die dadurch erlangte Rechtsstellung nur dann genommen werden, wenn zweifelsfrei feststeht, dass er sie zu Unrecht erlangt hat (BGH, Urteil vom 23. Januar 1990 - X ZR 75/87, GRUR 1991, 522, juris Rn. 36 - Feuerschutzabschluss; Urteil vom 12. Mai 1992 - X ZR 109/90, BGHZ 118, 221 = GRUR 1992, 839, juris Rn. 49 - Linsenschleifmaschine; Urteil vom 4. Mai 1995 - X ZR 29/93, GRUR 1996, 757, juris Rn. 77 - Zahnkranzfräser; Urteil vom 11. Mai 2010 – X ZR 51/06, GRUR 2010, 901 Rn. 32 - Polymerisierbare Zementmischung; Urteil vom 22. März 2018 – X ZR 128/15 Rn. 42).“

121 Entgegen der Ansicht der Klägerin wird ihr durch die Umkehr der Beweislast keine unzumutbare Belastung auferlegt - auch wenn es um einen Vorgang geht, der sich nicht in ihrem Wahrnehmungsbereich abgespielt hat -, da dies ebenso für die Beklagte zutrifft, die keinen leichteren Zugang zu näheren Angaben hätte.

122 „Der Nichtigkeitskläger war in der Regel zwar nicht an den Vereinbarungen beteiligt, aus denen sich die Berechtigung zur Inanspruchnahme der Priorität ergibt. Wenn er den Verdacht hegt, der Patentanmelder könnte das einem Dritten zustehende Prioritätsrecht zu Unrecht in Anspruch genommen haben, steht es ihm jedoch frei, den Dritten hierzu zu befragen. Sofern dieser keine Auskünfte erteilt, spricht dies typischerweise dafür, dass er mit der Inanspruchnahme des Prioritätsrechts einverstanden war.“ (BGH Sorafenib-Tosylat a. a. O. Rn 127).

123 5.2. Nach Art. 87 Abs. 2 EPÜ wird als prioritätsbegründend „…jede Anmeldung anerkannt, der … die Bedeutung einer vorschriftsmäßigen nationalen Anmeldung zukommt.“

124 Nach Regel 52 Abs. 1 Satz 1 EPÜ besteht die in Art. 88 Abs. 1 EPÜ genannte Prioritätserklärung aus einer Erklärung über den Tag der früheren Anmeldung und den Vertragsstaat der Pariser Verbandsübereinkunft oder das Mitglied der Welthandelsorganisation, in dem oder für den sie eingereicht worden ist, sowie aus der Angabe des Aktenzeichens.

125 Nach Regel 53 Abs. 1 EPÜ hat ein Anmelder, der eine Priorität in Anspruch nimmt, innerhalb von sechzehn Monaten nach dem frühesten Prioritätstag eine Abschrift der früheren Anmeldung einzureichen. Diese Abschrift und der Tag der Einreichung der früheren Anmeldung sind von der Behörde, bei der die Anmeldung eingereicht worden ist, zu beglaubigen.

126 Das EPA prüft nach den genannten Vorschriften insofern die Priorität. Der Vortrag der Klägerin in ihren Schriftsätzen vom 4. Juli 2023 und 15. Januar 2025 ist nicht geeignet, die grundsätzliche Vermutung für die Berechtigung zur Inanspruchnahme der Priorität zu erschüttern und zu beweisen, dass die Priorität US 61/029,895 vom 19. Februar 2008 von der Beklagten nach Prüfung durch das EPA nicht wirksam in Anspruch genommen worden ist (Große Beschwerdekammer EPA vom 10. Oktober 2023, G 1/22 und G 2/22, Rn. 110; BGH – Sorafenib-Tosylat, Leitsatz 3 und Rn. 121, 122, 123, 129).

127 Diesen Beweis hat die Klägerin auch in der mündlichen Verhandlung nicht erbracht. Die Angabe der Z … Inc. in der Assignee Information der Prioritätsanmeldung sieht der Senat als weiteres Indiz dafür, dass die Z … Inc. berechtigt war, die Priorität der Anmeldung NK6 für die Anmeldung des Streitpatents zu nutzen, auch wenn im Formblatt des USPTO zur Assignee Information angegeben wird, dass die dortige Erklärung eine Übertragungserklärung im USPTO nicht ersetzt.

128 Auch die von der Klägerin weiter eingereichten Dokumente NK9, NK10 und NK11 lassen keine Zweifel des Senats an der Prioritätsberechtigung aufkommen. Druckschrift NK9 ist eine US-amerikanische Patentanmeldung der Erfinder des Streitpatents, die am selben Tag wie das Streitpatent angemeldet wurde und ebenfalls die US-Anmeldung 61/029,895 wie eine innere Priorität in Anspruch nimmt. Das Dokument NK11 zeigt, dass diese Anmeldung NK9 erst am 18. Juni 2009 auf die Z … Inc. übertragen wurde, also nach der Anmeldung des Streitpatents. Daraus könnte möglicherweise der Schluss gezogen werden, dass zum Anmeldezeitpunkt des Streitpatents die US-amerikanische Prioritätsanmeldung noch nicht auf die Anmelderin des Streitpatents übertragen war. Doch auch wenn dies der Fall wäre, so bedeutet dies nicht, dass die Anmelderin des Streitpatents nicht autorisiert war, die US-Anmeldung 61/029,895 als Priorität zu nutzen. Dabei ist zu berücksichtigen, dass die Erfinder Mitarbeiter der Anmelderin waren und dass es nach dem US-Patentrecht zum Zeitpunkt der Anmeldung des Streitpatents nur den Erfindern möglich war, ein Patent anzumelden.

129 Für den Senat bestehen daher keine Zweifel, dass das Streitpatent die Priorität formal zu Recht in Anspruch nimmt.

130 5.3 In Bezug auf das Verfahren des erteilten Anspruchs 1 kann das Streitpatent die US-amerikanische Priorität 61/029,895 sachlich jedoch nicht zu Recht in Anspruch nehmen.

131 Die US-amerikanische provisorische Anmeldung NK6 besteht aus einem ersten Teil in koreanischer Sprache und einem zweiten Teil in englischer Sprache. Für den ersten Teil in koreanischer Sprache hat die Klägerin eine englische Übersetzung NK6a eingereicht, die allerdings erkennbar fehlerhaft ist, denn auf Seite 9 der Übersetzung heißt es: „If the PHICH is mapped beginning with the second OFDM symbol, the parameter m‘ should be changed to . Im koreanischen Original steht an dieser Stelle jedoch . Dies ergibt dann anders als in der Übersetzung NK6a auch einen Sinn.

132 Ersichtlich ist aus den Prioritätsunterlagen der US-amerikanischen provisorischen Anmeldung NK6, dass das Verhältnis dort zweimal enthalten ist, nämlich an der bereits genannten Stelle und in den zweiten Gleichungen unter Punkt 7. An beiden Stellen ist die Verwendung dieses Verhältnisses an Stelle des Verhältnisses an Bedingungen geknüpft. Anspruch 1 des Streitpatents enthält diese Bedingungen nicht. Dort handelt es sich, wie die Klägerin zurecht angibt, um zwei frei wählbare Alternativen. Diese Lehre des Streitpatents ist in der Priorität NK6 nicht enthalten.

133 Im Prioritätsdokument wird darauf abgestellt, dass eine Normierung auf die Anzahl der zur Verfügung stehenden Ressourcenelementgruppen in dem OFDM-Symbol erfolgt, in dem die erste Wiederholung der ersten PHICH-Gruppe erfolgt. Damit kann der erteilte Anspruch 1 die Priorität NK6 nicht zu Recht in Anspruch nehmen.

134 Hinzu kommt, dass in der Prioritätsschrift NK6 keine beliebige Abhängigkeit des Index der zur Übertragung des PHICH genutzten Ressourcenelementgruppen von den Quotienten und besteht. So beschäftigt sich die Prioritätsschrift NK6 mit der Vermeidung von Kollisionen der Übertragungen des PHICH in verschiedenen Zellen. Sie führt dazu zunächst aus, dass die Interferenz dieser Signale vermieden werden kann, wenn der Übertragungsort des PHICH im Signal in den jeweiligen Zellen unterschiedlich ist. Zur Lösung des Problems wird die Zellen ID für die Bestimmung der Mapping-Orte des PHICH verwendet (vgl. NK6a, S. 6, 7 seitenübergreifender Abs.: „If locations for transmitting the PHICHs in respective cells are the same, PHICH transmission performance may be deteriorated due to interference caused by transmission of the PHICH between neighbor cells. Accordingly, if transmission locations of the PHICH in respective cells differ, interference caused by transmission of the PHICH between neighbor cells is reduced. Consequently, PHICH transmission performance can be improved. Namely, if mapping locations of the PHICH are determined according to cell IDs, the above-described problem can be solved.“).

135 Gemäß der Prioritätsschrift NK6/NK6a besteht eine weitere Anforderung darin, die Wiederholungen gleichmäßig über die gesamte Frequenzbandbreite zu übertragen. Dies ist nicht gewährleistet, wenn die einzelnen OFDM-Symbole unterschiedliche Anzahlen von Ressourcenelementgruppen besitzen (vgl. NK6a, S.7, 8 seitenübergreifender Abs.: „When the PHICH is transmitted through multiple OFDM symbols including different REGs, since the number of REGs in each OFDM symbol differs, repetition of each PHICH is not evenly dispersed over an entire frequency bandwidth. The location of the first REG should be designated according to a cell ID and a repetitive pattern should be allocated at regular intervals based on an index of the first REG.“). Die gleichmäßige Verteilung wird trotz der unterschiedlichen Anzahl von zur Verfügung stehenden Ressourcenelementgruppen in den einzelnen OFDM-Symbolen gewährleistet, indem der Startort entsprechend der Zellen ID unter Berücksichtigung des Verhältnisses der Anzahl von Ressourcenelementgruppen des ersten Startsymbols zu der Anzahl von Ressourcenelementgruppen der anderen Symbole bestimmt wird (vgl. S. 8, 2. Abs.: „Therefore, when the PHICH is transmitted through multiple OFDM symbols, if the start location according to the cell ID is determined in consideration of a ratio of REGs of the first start symbol to REGs of the other symbols, the above problem can be solved.“) Dies wird anschließend in den Formeln konkretisiert, die auch im Streitpatent als „Equation 2“ und „Equation 3“ enthalten sind. Der Fachmann wird die Prioritätsschrift somit so verstehen, dass nicht eine willkürliche Abhängigkeit der Indizes der Ressourcenelementgruppen von den Quotienten und besteht, sondern dass eine Abhängigkeit von diesen Quotienten mit einer Verknüpfung der Zellen ID, logischerweise einer Multiplikation mit der Zellen ID, wie sie auch die Gleichungen in NK6/NK6a zeigen, besteht.

136 Auch aus diesem Grund kann der erteilte Anspruch 1 die Priorität der US-amerikanischen Prioritätsschrift NK6 nicht zu Recht in Anspruch nehmen.

137 5.4 In den Ansprüchen 1 der Hilfsanträge 1, 1‘, 1a, 2, 2‘ und 2‘‘ ist zwar die Möglichkeit der willkürlichen Wahl der Quotienten und aufgehoben, doch fehlt auch dort die Verknüpfung dieser Quotienten mit der Zellen ID. Dies bedeutet, dass die Ansprüche 1 auch dieser Hilfsanträge als Zeitrang den Anmeldetag des Streitpatents, also den 18. Februar 2009 besitzen.

138 Beim Anspruch 1 des Hilfsantrags 2‘‘‘ wird hingegen neben der Fallaufteilung auch die Multiplikation der Quotienten und mit der Zellen ID beansprucht, wie dies die Prioritätsschrift NK6 offenbart. Dabei wird die Fallaufteilung in einer Weise beansprucht, wie dies auch die Prioritätsschrift NK6 offenbart, nämlich, dass der Quotient benutzt wird, der im Nenner die Anzahl der Ressourcenelementgruppen des Symbols angibt, in dem die erste Wiederholung der ersten PHICH-Gruppe übertragen wird (vgl. S. 8, 9 der NK6a und die Gleichungen im mit „6.9.3 Mapping to resource elements“ überschriebenen Absatz.) Damit ist der Zeitrang des Anspruchs 1 des Hilfsantrags 2‘‘‘ der Anmeldetag der US-amerikanischen Prioritätsanmeldung NK6, also der 19. Februar 2008.

139 Auch die nebengeordneten Ansprüche 4 und 5 besitzen diesen Zeitrang, denn auch wenn im Prioritätsdokument NK6/NK6a keine genaueren Details über die Basisstation oder die Mobilfunkstation angegeben werden, werden diese doch so erwähnt, dass der Fachmann mitliest, dass die Basisstation das geschilderte Verfahren ausführt und die Mobilstation als Gegenstück das übertragene Signal auch entsprechend versteht (vgl. S. 3 bis 6 der NK6a).

140 6. Die mit dem erteilten Anspruch 1 und den Ansprüchen 1 der Hilfsanträge 1, 1‘, 1a, 2, 2‘ und 2‘‘ beanspruchten Verfahren sind gegenüber der Lehre der Druckschrift D1 nicht neu und damit nicht patentfähig.

141 6.1 Die Klägerin zeigt in ihrem Klageschriftsatz den Auszug aus der Datenbank von 3GPP, in der das Dokument D1 enthalten ist und der belegt, dass dieses Dokument am 20. März 2008 also vor dem Prioritätstag der zweiten Priorität, jedoch nach dem Prioritätstag der US-amerikanischen Priorität NK6 auf den Server von 3 GPP hochgeladen wurde. Das Dokument D1 kann im Internet bei 3GPP von diesem Zeitpunkt an bis heute so erhalten werden. Bei dem Dokument handelt es sich um eine Version des Standards TS 36.211, nämlich die Version V8.2.0.

142 Wie die Klägerin angibt, beschreibt Druckschrift D1 die physikalischen Kanäle für die Luftschnittstelle des Mobilfunkstandards LTE („evolved UTRA“, siehe D1, S. 2, Abschnitt 1: „Scope“).

143 In Abschnitt 6 werden, wie die Klägerin angibt, die physikalischen Kanäle für den Downlink, also von der Basisstation zur Mobilstation erläutert. Unter diesen physikalischen Kanälen befindet sich auch der „Physical Hybrid ARQ Indicator Channel“, PHICH (vgl. Abs. 6.1.1 „Physical channels“). Dieser wird ausführlich im Abschnitt 6.9 „Physical hybrid ARQ indicator channel“ beschrieben. Die Definition einer Ressourcenelementgruppe erfolgt dem Streitpatent entsprechend (vgl. den Text im Abschnitt 6.9).

144 Dokument D1 offenbart in Übereinstimmung mit dem Wortlaut des Anspruchs 1 des Streitpatents

145 1. ein Verfahren zum Abbilden eines physikalischen Hybridautomatikwiederholungsanforderung-Indikatorkanals, PHICH, in Gruppen von einer Mehrzahl von PHICHs (vgl. Abschnitt 6.9.3 „Mapping to resource elements“, „The sequence for each of the PHICH groups is defined by where the sum is over all PHICHs in the PHICH group and represents the symbol sequence from the i :th PHICH in the PHICH group.“), auf Orthogonales-Frequenzmultiplexverfahren, OFDM, - Symbole (siehe die hier gezeigte Fig. 6.2.2-1 und vgl. Abschnitt 6.2.1 „Resource grid“ „The transmitted signal in each slot is described by a resource grid of subcarriers and OFDM symbols.”), wobei

146 1.1 jedes OFDM-Symbol eine Mehrzahl von Ressourcenelementgruppen umfasst, jede Ressourcenelementgruppe vier Ressourcenelemente umfasst (vgl. Abs. 6.9.3 „Mapping to resource elements“ „Let denote symbol quadruplet i for antenna port p. Mapping to resource elements is defined in terms of symbol quadruplets according to steps 1–10 below:“, „6) Symbol-quadruplet from PHICH group m’ is mapped to the resource-element group represented by (k’, l’) i as defined in Section 6.2.4 where the indices k’ i and l’ i are given by steps 7 and 8 below:” Eine genauere Angabe, was gemäß der Lehre des Dokuments D1 Ressourcenelementgruppen sind, wird im Abschnitt 6.2.4 „Resource-element groups” gegeben. Dort wird eine Situation beschrieben, wie sie in Fig. 3 des Streitpatents gezeigt wird. Es wird angegeben, dass immer ein Quadrupel auf eine Ressourcenelementgruppe abgebildet wird, die Ressourcenelementgruppen aber möglicherweise mehr als 4 Ressourcenelemente aufweisen, wobei ein Teil mit zellenspezifischen Referenzsignalen besetzt ist.), wobei das Verfahren umfasst:

147 1.2 Bestimmen von Indizes von Ressourcenelementgruppen, in welchen der PHICH übertragen wird (vgl. Abs. 6.9.3 „Mapping to resource elements“, „Set the frequency-domain index k’ i to the resource-element group assigned the number in step 3 above,, …“), wobei das Verfahren dadurch charakterisiert ist, dass

148 1.2.1 die Indizes gemäß dem Verhältnis oder bestimmt werden (vgl. die beiden Gleichungssysteme unter Punkt 8 im Abschnitt 6.9.3)

149 1.2.1a der Anzahl , von verfügbaren Ressourcenelementgruppen in dem OFDM-Symbol, welches den Index aufweist, in welchem die te Wiederholung des PHICH von einer PHICH-Gruppe übertragen wird, wobei eine ganze Zahl von 0 bis 2 ist (vgl. Abschnitt 6.9.3, Punkt 5: „For each value of i = 0,1,2“), und

150 1.2.1b der Anzahl von verfügbaren Ressourcenelementgruppen in dem ersten OFDM-Symbol, welches Index 0 aufweist, von einem Sub-Frame oder in dem zweiten OFDM-Symbol, welches Index 1 aufweist, von einem Sub-Frame (vgl. Abschnitt 6.9.3, Punkt 2: „Let n i denote the number of resource element groups not assigned to PCFICH in OFDM symbol i“, d.h. n 0 entspricht n‘ 0 und n 1 entspricht n‘ 1 ),

151 1.2.2 der PHICH durch einen, zwei oder drei OFDM-Symbole übertragen wird (vgl. Absatz 6.9.3, Punkt 7 und vergleiche dies mit Tabelle 6.9.3-1:

152 Die Dauer wird dabei in OFDM-Symbolen gemessen und reicht von 1 bis 3)

153 1.2.2a wobei der Index , wenn der PHICH durch ein OFDM-Symbol übertragen wird,

154 1.2.2b wobei der Index wobei einen Index der PHICH-Gruppe, welche den PHICH umfasst, bezeichnet, wenn der PHICH durch zwei OFDM-Symbole übertragen wird, und

155 1.2.2c wobei der Index wenn der PHICH durch drei OFDM-Symbole übertragen wird (vgl. Abschnitt 6.9.3, Punkt 7:

156 Die erste Zeile gibt den Fall „normal PHICH duration“ an, der nach Tabelle 6.9.3-1 ein OFDM-Symbol lang ist. Durch weiteren Vergleich mit der Tabelle 6.9.3-1 ist ersichtlich, dass die Fälle der zweiten und der dritten Zeile den PHICH in zwei OFDM-Symbolen übertragen. Es bleibt nur noch der Fall für alle anderen PHICH-Dauern übrig. Dieser überträgt nach Tabelle 6.9.3-1 in drei OFDM-Symbolen und fällt unter den Fall „otherwise“ der vierten Zeile.)

157 1.2.1c verfügbare Ressourcenelementgruppen Ressourcenelementgruppen sind, welche für eine PHICH-Übertragung in dem jeweiligen OFDM-Symbol verwendet werden können (vgl. Abschnitt 6.9.3, Punkt 2), und

158 1.3 Abbilden des PHICH auf die OFDM-Symbole gemäß den bestimmten Indizes (vgl. den Titel des Abschnitts 6.9.3: „Mapping to resource elements“)

159 Da das mit Anspruch 1 des Streitpatents beanspruchte Verfahren keine weiteren Merkmale aufweist, ist es nicht neu gegenüber dem im Dokument D1 offenbarten Verfahren und damit nicht patentfähig.

160 6.2 Druckschrift D1 offenbart auch die in den Anspruch 1 des Hilfsantrags 1, der identisch zu den Ansprüchen 1 der Hilfsanträge 1‘ und 1a ist, eingefügten Merkmale

161 1.2.1.dH1 wobei besagte Indizes entsprechend dem Verhältnis bestimmt werden, wenn der PHICH durch ein oder drei OFDM Symbole übertragen wird, und

162 1.2.1.eH1 wobei besagte Indizes entsprechend dem Verhältnis bestimmt werden, wenn der PHICH durch zwei OFDM Symbole übertragen wird.

163 Dies ist aus den Punkten 7) und 8) des Abschnitts 6.9.3 auf den Seiten 49 und 50 der Druckschrift D1 ersichtlich. Dort wird der PHICH bei einer normalen Dauer („normal PHICH duration, all subframes”) in einem OFDM-Symbol mit der Nummer 0, also im ersten übertragen, bei einer erweiterten PHICH Dauer („extended PHICH duration”) in zwei OFDM-Symbolen und im Übrigen in drei OFDM-Symbolen, da nach Punkt 5) nacheinander 0, 1 und 2 ist. Diese Fälle werden im Punkt 8) wiederaufgenommen, wobei nur eine Unterscheidung nach den Fällen mit der erweiterten PHICH Dauer und anderen Fällen vorgenommen wird. Die Fälle mit den erweiterten PHICH Dauern sind die, bei denen die Übertragung in zwei OFDM-Symbolen erfolgt. Bei ihnen erfolgt eine Multiplikation der Zellen ID mit dem Quotienten Verhältnis dort als bezeichnet. Bei allen anderen Fällen, also auch den Fällen mit einer Übertragung in einem oder drei OFDM-Symbolen erfolgt eine Multiplikation der Zellen ID mit dem Quotienten Verhältnis, , dort als bezeichnet. Damit sind auch die Verfahren der Ansprüche 1 der Hilfsanträge 1, 1‘, 1a mangels Neuheit gegenüber der Lehre der Druckschrift D1 nicht patentfähig.

164 6.3 Druckschrift D1 offenbart auch das in dem Anspruch 1 des Hilfsantrags 2, der identisch zu den Ansprüchen 1 der Hilfsanträge 2‘ und 2‘‘ ist, enthaltene Merkmal

165 1.2.1.eH2 wobei besagte Indizes entsprechend dem Verhältnis bestimmt werden, wenn der PHICH durch zwei OFDM Symbole übertragen wird und die erste PHICH-Gruppe im zweiten OFDM-Symbol gestartet wird,

166 Dies ergibt sich aus den Punkten 5), 7) und 8) in Abschnitt 6.9.3 auf den Seiten 49 und 50 der Druckschrift D1. Wie bereits ausgeführt nimmt gemäß Punkt 5) nacheinander die Werte 0, 1 und 2 an. Damit wird die Nummer der drei Wiederholungen angegeben. Für die erste Wiederholung, die die Nummer 0 trägt, erfolgt nach der Formel in Punkt 7) bei einer Übertragung in zwei OFDM-Symbolen die Übertragung im OFDM-Symbol mit der Nummer 1, denn für = 0 ergibt sich für die erste PHICH-Gruppe, die die Nummer = 0 trägt:

167 Das OFDM-Symbol mit der Nummer 1 ist, da auch die Nummerierung der OFDM-Symbole mit 0 startet, das zweite OFDM-Symbol.

168 Damit sind auch die Verfahren der Ansprüche 1 der Hilfsanträge 2, 2‘ und 2‘‘ mangels Neuheit gegenüber der Lehre der Druckschrift D1 nicht patentfähig.

169 Da die Beklagte angegeben hat, dass sie die Anträge als geschlossene Anspruchssätze ansieht, teilen die übrigen Ansprüche des jeweiligen Antrags das Schicksal des jeweiligen Patentanspruchs 1.

170 7. Die im Tenor wiedergegeben Ansprüche des Hilfsantrags 2‘‘‘ sind zulässig, die mit ihnen beanspruchten gewerblich anwendbaren Verfahren und Gegenstände sind ausführbar offenbart und auch patentfähig gegenüber dem im Verfahren befindlichen Stand der Technik. Das Patent hat deshalb in diesem Umfang Bestand.

171 7.1 Die Ansprüche des Hilfsantrags 2‘‘‘ sind zulässig, da die mit ihnen beanspruchten Verfahren und Gegenstände ursprünglich offenbart sind (Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜbkG bzw. Art. 138 Abs. 1 lit. c) EPÜ und Art. 123 Abs. 2 EPÜ) und sie den Schutzbereich des Streitpatents nicht erweitern (§ 6 Abs. 1 Satz 1 Nr. 4 IntPatÜbkG bzw. Art. 138 Abs. 1 lit. d) EPÜ.

172 7.1.1 Anspruch 1 des Streitpatents geht aus der Kombination der ursprünglichen Ansprüche 1, 3, 4, 5, 6 und 8 hervor. Die ursprünglichen Ansprüche 3, 4, 5, 6 und 8 sind dabei jeweils nur auf Anspruch 1 zurückbezogen, so dass ein Verfahren mit allen Merkmalen dieser Ansprüche in den ursprünglichen Ansprüchen nicht enthalten ist. Jedoch offenbart der Beschreibungstext in seiner Gesamtheit, dass auch alle Merkmale des Anspruchssatzes, soweit sie nicht widersprüchlich zueinander sind, gleichzeitig vorhanden sein können, indem in der Wiedergabe der Ansprüche im Abschnitt „Technical Solution“ der Beschreibung die beanspruchten Sachverhalte jeweils mit „may“ eingeleitet werden, was zu keinem gegenseitigen Ausschluss führt.

173 Es verbleiben folgende Merkmale, die in diesen Ansprüchen und damit auch im Abschnitt „Technical Solution“ der Beschreibung nicht enthalten sind:

174 1. ist eine ganze Zahl von 0 bis 2 (in Merkmal 1.2.1a). Dies bedeutet, dass drei Wiederholungen gesendet werden.

175 2. Verfügbare Ressourcenelementgruppen sind Ressourcenelementgruppen, welche für eine PHICH-Übertragung in dem jeweiligen OFDM-Symbol verwendet werden können (Merkmal 1.2.1c).

176 3. Die besagten Indizes werden entsprechend dem Verhältnis bestimmt, wenn der PHICH durch ein oder drei OFDM Symbole übertragen wird (Merkmal 1.2.1dH1).

177 4. Die besagten Indizes werden entsprechend dem Verhältnis bestimmt, wenn der PHICH durch zwei OFDM Symbole übertragen wird und die erste PHICH-Gruppe im zweiten OFDM-Symbol gestartet wird (Merkmal 1.2.1.eH2).

178 Zu 1: Auf Seite 7 der ursprünglichen Beschreibung ist in Zusammenhang mit der Gleichung 1, die auch im Anspruch 1 enthalten ist, offenbart, dass es drei Wiederholungen des PHICH gibt, so dass die Werte 0, 1 und 2 besitzt (vgl. S. 7, Z. 21 bis 24: „In Equation 1, denotes an index of an OFDM symbol in which i-th repetition of a PHICH group is transmitted, denotes an index of a PHICH group, and i denotes the number of repetitions of a PHICH. When the PHICH is repeated three times, i has values of 0, 1, and 2.“).

179 Zu 2: Merkmal 1.2.1c ist eine eingefügte Erklärung des Ausdrucks „available resource element groups“. Es wird in den ursprünglichen Unterlagen in Zusammenhang mit den Fig. 1 und 3 offenbart, so beispielsweise im Absatz auf Seite 6, Zeilen 15 bis 18 oder Seiten 6, Zeile 32 bis Seite 7, Zeile 3 der ursprünglichen Beschreibung in NK 5.

180 Zu 3 und 4: Diese Merkmale 1.2.1dH1 und 1.2.1.eH2 sind dem Abschnitt auf Seite 9, Zeile 5 bis Seite 10, Zeile 7 der ursprünglichen Anmeldung NK5 zu entnehmen, wo die Gleichungen 2 und 3 erläutert werden, die auch in den ursprünglichen Ansprüchen 7 und 9 enthalten sind.

181 Damit ist ein Verfahren mit allen Merkmalen des Anspruchs 1 nach dem Hilfsantrag 2‘‘‘ in den ursprünglichen Anmeldungsunterlagen NK5 offenbart. Die Beschreibung der ursprünglichen Anmeldung NK5 findet sich auch in der ersten Teilung EP 2 637 348 A1 und in der Offenlegungsschrift NK4 des Streitpatents.

182 7.1.2 Unteranspruch 2 geht aus dem ursprünglichen Unteranspruch 7 und Unteranspruch 3 aus dem ursprünglichen Unteranspruch 9 hervor. In diese Ansprüche wurden die Merkmale der Fallunterscheidung aufgenommen, die sich auch im Anspruch 1 finden.

183 7.1.3 Der nebengeordnete Anspruch 4 des Hilfsantrags 2‘‘‘ geht aus dem ursprünglichen Anspruch 10 hervor. Sein Gegenstand ist demnach ebenfalls ursprünglich offenbart.

184 7.1.4 Die ursprünglichen Unterlagen offenbaren explizit keine Mobilstationen, die besonders an das Signal der Basisstation angepasst sind. Für den Fachmann ist es allerdings selbstverständlich, dass die Mobilstationen, die in der ursprünglichen Beschreibung genannt werden (vgl. S. 2 der NK5), auch in der Lage sein müssen, die empfangenen Signale zu verstehen, so dass sie Gegenstücke zur beanspruchten Basisstation bilden. Insoweit sind die mit den Ansprüchen 5 und 6 beanspruchten Mobilstationen ebenfalls ursprünglich offenbart.

185 Den Ausführungen der Klägerin, dass das Nichtigkeitsverfahren nicht dazu diene, neue Gegenstände in das Patent einzuführen, was in den Hilfsanträgen bezüglich der Mobilstation erfolgt sei, weshalb diese Patentansprüche unzulässig seien, ist nicht zu folgen, denn das Streitpatent hat in seinem erteilten Anspruchssatz mit Patentanspruch 6 bereits eine Mobilstation beansprucht, die mit den neuen Patentansprüchen des Hilfsantrags 2‘‘‘ lediglich beschränkt beansprucht wird.

186 7.1.5 Die Aufnahme von weiteren Merkmalen, die die Fallunterscheidung in Anspruch 1 einführen und diese dann weiter konkretisieren, schränken den Schutzbereich ein und führen, da das Wort „oder“ im Merkmal 1.2.1.b des Patentanspruchs 1 kein exklusives oder ist auch zu keiner Verschiebung des Schutzbereichs. Damit sind die Ansprüche des Hilfsantrags 2‘‘‘ zulässig.

187 7.2 Die Lehren der Ansprüche des Hilfsantrags 2‘‘‘ sind auch so deutlich und vollständig offenbart, dass ein Fachmann sie ausführen kann (Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜbkG bzw. Art. 138 Abs. 1 lit. b) EPÜ), da in der Beschreibung ein unter die Ansprüche fallendes Verfahren mit Angabe von Formeln offenbart ist, nach dessen Vorgabe der Fachmann Software entwickeln kann, mit deren Hilfe eine Basisstation dann das Verfahren ausführt.

188 7.3 Das Verfahren des Anspruchs 1 und die Gegenstände der Ansprüche 4 und 5 sind gegenüber dem im Verfahren befindlichen Stand der Technik auch neu und beruhen auf einer erfinderischen Tätigkeit des Fachmanns, so dass sie patentfähig sind (Art. II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜbkG bzw. Art. 138 Abs. 1 lit. a) EPÜ, beide i.V.m. Art. 52, 54 und 56 EPÜ).

189 7.3.1 Das Dokument D1 wurde, wie bereits ausgeführt, am 20. März 2008 also vor dem Prioritätstag der zweiten Priorität, jedoch nach dem Prioritätstag der US-amerikanischen Priorität, dem 19. Februar 2008, auf den Server von 3 GPP hochgeladen, so dass es am Prioritätstag der US-amerikanischen Priorität 61/029,895 der Öffentlichkeit nicht zugänglich war. Damit bildet das Dokument D1 für den Anspruch 1 des Hilfsantrags 2‘‘‘, der wie ausgeführt die Priorität zur Recht in Anspruch nimmt, keinen Stand der Technik. Es bleibt somit unberücksichtigt.

190 7.3.2 Die Klägerin ist der Ansicht, dass das Verfahren des Anspruchs 1 dem Fachmann ausgehend vom Dokument D3 nahegelegen habe. Das Dokument D3 wurde anlässlich der Tagung #52 der TSG RAN WG1, die vom 11. bis 15. Februar 2008 in Sorrent, Italien stattfand, eingereicht und nachweislich am 15. Februar 2008 um 17:15h auf den Server des 3GPP hochgeladen. Es stellt, da die Veröffentlichung vor der US-amerikanischen Prioritätsanmeldung erfolgt ist, für das Streitpatent Stand der Technik dar. Es stellt, wie unter dem Punkt „3. Conclusion“ angegeben, einen Änderungsentwurf für den zu diesem Zeitpunkt aktuellen Änderungsentwurf des Standards TS 36.211 dar, also eine „Verbesserung des Änderungsentwurfs“. Dieser Änderungsentwurf ist im Dokument D4 enthalten, das zum gleichen Zeitpunkt wie das Dokument D3 auf den Server des 3GPP hochgeladen wurde, also ebenfalls vorveröffentlicht ist.

191 Sowohl das Dokument D3 als auch das Dokument D4 enthalten in ihren Berechnungen der Nummer der Ressourcenelementgruppe, auf die eine Wiederholung abgebildet wird, den Quotienten oder nicht. Die Klägerin argumentiert nun zum einen, dass für den Fall, dass alle Wiederholungen in nur einem OFDM-Symbol übertragen werden, der Quotient = 1 sei und damit nicht explizit in der Formel aufgeführt werden müsse. Dies ist zwar sachlich richtig, entspricht aber nicht dem Verständnis des Fachmanns. Der Fachmann versteht nämlich Anspruch 1 des Streitpatents und auch des Hilfsantrags 2‘‘‘ so, dass das Verhältnis oder in einem Verfahrensschritt bestimmt werden muss. Bei dem Verfahren des Anspruchs 1, das üblicherweise in Software ausgeführt sein dürfte, muss es demnach eine oder mehrere Anweisungen geben, die oder bestimmen und die eine Fallunterscheidung vornehmen, also eine dem Anspruchswortlaut gemäße „if-Anweisung“. Fehlen solche Anweisungen, so handelt es sich um kein anspruchsgemäßes Verfahren. Somit legen die Dokumente D3 und D4 das Verfahren des Anspruchs 1 nicht auf diese triviale Weise nahe.

192 Die Dokumente D3 und D4 zeigen allerdings, dass es sich in beiden Fällen um nicht ganz fertige Vorschläge handelt. Dies erkennt der Fachmann an den Formeln für die Ressourcenelementgruppen für die -te Wiederholung relativ schnell. Im Dokument D4 kann diese Nummer, wie die Formeln unter Punkt 8 im Abschnitt 6.9.3 zeigen, über die Anzahl der verfügbaren Ressourcenelementgruppen hinausgehen, denn es wird immer die gleiche Anzahl als Ausgangspunkt verwendet, obwohl vorher im Punkt 6) definiert wird, das die Anzahl der Ressourcenelemente definiert, die noch nicht dem PCFICH oder PHICH im OFDM-Symbol zugewiesen wurden, also die Anzahl der verfügbaren Ressourcenelementgruppen. wird nur zur Festlegung der Nummer der Ressourcenelementgruppe in Punkt 7) verwendet.

193 Im Dokument D3 wird dieser Fehler beseitigt, die Abhängigkeit von der Zellennummer eingeführt und zusätzlich ein neuer Fehler eingeführt. Dort wird im Abschnitt 6.9.3 unter Punkt 2) als Anzahl der Ressourcenelementgruppen, die nicht dem PCFICH im OFDM Symbol zugeordnet wurden, definiert. Im Punkt 8) werden dann die Ressourcenelementgruppennummern bestimmt, auf die die -te Wiederholung gemappt wird. Dabei wird vergessen, dass die Wiederholungen in einem, zwei oder drei OFDM-Symbolen gesendet werden können. Die Ressourcenelementgruppennummer ist immer von den verfügbaren Ressourcenelementgruppen in den ersten drei OFDM-Symbolen () abhängig, unabhängig davon, ob die Wiederholungen in einer, in zwei oder in drei OFDM-Symbolen gesendet wird. Auch die im Dokument D3 offenbarten Formeln sind somit nicht richtig. Der Fachmann wird sie demnach berichtigen und die gewünschte Frequenzdiversität herstellen. Das Ergebnis dieser Berichtigung bei maximal möglicher Frequenzdiversität könnte zu einer Nutzung der im erteilten Anspruch 1 enthaltenen Verhältnisse oder als Normierung führen. Der Senat hat allerdings bereits Zweifel daran, dass der Fachmann ohne einen weiteren Hinweis tatsächlich zu der Verwendung dieser Quotienten kommt.

194 Zweifellos benötigt der Fachmann jedoch einen Hinweis auf eine Fallunterscheidung, zur Verwendung der Quotienten oder in den Formeln zur Ermittlung der Nummern der Ressourcenelementgruppen für die verschiedenen Wiederholungen. Einen solchen Hinweis gibt es in den Dokumenten D3 und D4 nicht, weshalb diese das Verfahren des Anspruchs 1 des Hilfsantrags 2‘‘‘ auch nicht nahelegen können.

195 7.3.3 Dokument D2 wurde nach seiner Angabe auf dem Titelblatt erst im September 2008 veröffentlicht, also deutlich nach dem Prioritätsdatum der US-amerikanischen Priorität und stellt deshalb ebenfalls keinen Stand der Technik für die Ansprüche des Hilfsantrags 2‘‘‘ dar. Die weiteren Druckschriften D5 und D6 enthalten ebenfalls keinen Hinweis auf die mit Anspruch 1 des Hilfsantrags 2‘‘‘ beanspruchte Fallunterscheidung. Damit gilt das Verfahren des Anspruchs 1 des Hilfsantrags 2‘‘‘ als neu und auf einer erfinderischen Tätigkeit des Fachmanns beruhend. Es ist somit patentfähig.

196 7.3.4 Auch die mit den Ansprüchen 4 und 5 des Hilfsantrags 2‘‘‘ beanspruchten Gegenstände sind patentfähig, denn sie ziehen ihre Patentfähigkeit aus der des Verfahrens des Anspruchs 1, auf den sie sich zurückbeziehen. Dies gilt auch für die Verfahren der Ansprüche nach den Unteransprüchen 2 und 3 sowie den Gegenstand des Patentanspruchs 6.

197 8. Bei dieser Sachlage hat das Streitpatent im Umfang des Hilfsantrags 2‘‘‘ Bestand. Die weiteren in der Antragsstellung der Beklagten nachgeordneten Hilfsanträge 2a, 3, 3‘, 3a, 4, 4a, 5, 5a sowie 1 bis 5 ohne die Mobilstationsansprüche spielen für die Entscheidung damit keine Rolle mehr.

II.

198 Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG i. V. m. § 92 Abs. 1 Satz 1 ZPO.

199 Zwar ist der als schutzfähig verbleibende Patentgegenstand nach der beschränkt verteidigten Fassung gemäß Hilfsantrag 2‘‘‘ gegenüber demjenigen der erteilten Fassung erheblich eingeschränkt. Diese Einschränkung macht nach Ansicht des Senats jedoch im Hinblick darauf, dass das nach Anspruch 1 beanspruchte Verfahren immer noch unter den Standard fällt, nicht mehr als die Hälfte der wirtschaftlichen Verwertbarkeit des angegriffenen Streitpatents aus. Daher haben die Klägerin und die Beklagte bezogen auf den verbleibenden Patentgegenstand jeweils den gleichen Anteil zu tragen, so dass die Kosten des Rechtsstreits gegeneinander aufzuheben sind.

200 Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG i. V. m. § 709 Satz 1 und 2 ZPO.
