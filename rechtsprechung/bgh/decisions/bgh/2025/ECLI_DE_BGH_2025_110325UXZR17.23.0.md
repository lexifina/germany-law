---
ecli: "ECLI:DE:BGH:2025:110325UXZR17.23.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 17/23"
decided: "2025-03-11"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600032025.xml"
neuris_doknr: "KORE600032025"
---

# Bundesgerichtshof, X ZR 17/23 vom 2025-03-11

## Tenor

Auf die Berufung der Klägerin wird das Urteil des 4. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 23. November 2022 abgeändert.

Das europäische Patent 1 864 151 wird mit Wirkung für die Bundesrepublik Deutschland für nichtig erklärt.

Die Beklagte trägt die Kosten des Rechtsstreits.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 1 864 151 (Streitpatents), das am 22. März 2006 unter Inanspruchnahme einer US-amerikanischen Priorität vom 22. März 2005 angemeldet worden ist und das Ableiten der Ausgangsposition eines GPS-Geräts betrifft.

2 Patentanspruch 22, auf den elf weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A subscriber station for use in a wireless communication system, the subscriber station comprising:

means for receiving an overhead message from the wireless communication system; and means for deriving the seed position of the subscriber station from a parameter in the overhead message,

characterized in that said means for deriving comprises:

means for deriving a first position estimate of the subscriber station from the parameter;

means for attempting to derive a second position estimate of the subscriber station; means for setting the seed position of the subscriber station to the first position estimate if the second position estimate is unavailable;

means for setting the seed position of the subscriber station to the first position estimate if the second position estimate has a higher position uncertainty than the first position estimate; and

means for setting the seed position of the subscriber station to the second position estimate if the second position estimate has a lower position uncertainty than the first position estimate.

3 Patentanspruch 1, auf den 20 weitere Ansprüche zurückbezogen sind, schützt ein Verfahren mit entsprechenden Merkmalen.

4 Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Die Beklagte hat das Streitpatent in der erteilten Fassung und hilfsweise in einer geänderten Fassung verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt, soweit dessen Gegenstand über die Fassung des Hilfsantrags hinausgeht, und die Klage im Übrigen abgewiesen.

6 Dagegen wendet sich die Berufung der Klägerin, die weiterhin die vollständige Nichtigerklärung des Streitpatents anstrebt. Die Beklagte tritt dem Rechtsmittel entgegen.

## Entscheidungsgründe

7 Die zulässige Berufung ist begründet und führt zur vollständigen Nichtigerklärung des Streitpatents.

8 I. Das Streitpatent befasst sich mit der Positionsbestimmung durch GPS-Geräte.

9 1. Nach der Beschreibung des Streitpatents kann sich die Positionsbestimmung durch ein GPS-Gerät (subscriber station, Teilnehmerstation) sehr schwierig gestalten, wenn keine Informationen über die aktuelle Position und den aktuellen Betriebszustand der hierzu vorgesehenen Satelliten verfügbar sind (Abs. 3-9).

10 Vor diesem Hintergrund betrifft das Streitpatent das technische Problem, die Positionsbestimmung in solchen Situationen zu erleichtern.

11 2. Zur Lösung schlägt das Streitpatent in der im Berufungsverfahren noch verteidigten Fassung von Patentanspruch 15 eine Teilnehmerstation vor, deren Merkmale sich wie folgt gliedern lassen (Änderungen gegenüber dem erteilten Anspruch 22 sind hervorgehoben):

12 0

A subscriber station for use in a wireless communication system, the subscriber station comprising:

Eine Teilnehmerstation zur Verwendung in einem Drahtloskommunikationssystem, die Folgendes aufweist:

1

means for receiving an overhead message from the wireless communication system; and

Mittel zum Empfangen einer Overhead-Nachricht von dem Drahtloskommunikationssystem; und

2

means for deriving the seed position of the subscriber station from a parameter in the overhead message, comprising:

Mittel zum Ableiten der Ausgangsposition der Teilnehmerstation von einem Parameter in der Overhead-Nachricht, aufweisend:

2.1

means for deriving a first position estimate of the subscriber station from the parameter;

Mittel zum Ableiten einer ersten Positionsschätzung der Teilnehmerstation von dem Parameter;

2.2

means for attempting to derive a second position estimate of the subscriber station;

Mittel für den Versuch, eine zweite Positionsschätzung der Teilnehmerstation abzuleiten;

2.3

means for setting the seed position of the subscriber station to the first position estimate if the second position estimate is unavailable;

Mittel zum Einstellen der Ausgangsposition der Teilnehmerstation auf die erste Positionsschätzung, wenn die zweite Positionsschätzung nicht verfügbar ist;

2.4

means for setting the seed position of the subscriber station to the first position estimate if the second position estimate has a higher position uncertainty than the first position estimate; and

Mittel zum Einstellen der Ausgangsposition der Teilnehmerstation auf die erste Positionsschätzung, wenn die zweite Positionsschätzung eine höhere Positionsunsicherheit hat als die erste Positionsschätzung; und

2.5

means for setting the seed position of the subscriber station to the second position estimate if the second position estimate has a lower position uncertainty than the first position estimate;

Mittel zum Einstellen der Ausgangsposition der Teilnehmerstation auf die zweite Positionsschätzung, wenn die zweite Positionsschätzung eine niedrigere Positionsunsicherheit hat als die erste Positionsschätzung;

2.6

deriving the seed position further comprises:

das Ableiten der Ausgangsposition umfasst ferner:

2.6.1

means for mapping the parameter to a position using a data structure, stored in the memory of the subscriber station, associating possible values of the parameter with corresponding positions; and

Mittel, um den Parameter auf eine Position abzubilden, mit Hilfe einer Datenstruktur, die im Speicher der Teilnehmerstation hinterlegt ist und mögliche Werte des Parameters mit entsprechenden Positionen verknüpft; und

2.6.2

means for setting the seed position to the mapped position provided another estimate of the position of the subscriber station having lower position uncertainty is unavailable;

Mittel, um die Ausgangsposition auf die abgebildete Position zu setzen, sofern eine andere Schätzung der Position der Teilnehmerstation mit einer geringeren Positionsunsicherheit nicht verfügbar ist;

3

means for deriving a fix of the position of the subscriber station from one or more satellite transmissions originating from a GPS-type position determination system, including searching for one or more of such transmissions responsive to the seed position;

Mittel, um eine Bestimmung der Position der Teilnehmerstation aus einer oder mehreren von einem GPS-Positionsbestimmungssystem stammenden Übertragungen abzuleiten, einschließlich der Suche nach einer oder mehreren solchen Übertragungen, in Reaktion auf die Ausgangsposition;

4

the subscriber station further comprises:

die Teilnehmerstation weist ferner auf:

4.1

means for determining whether an update condition is present responsive to the GPS-type position fix of the subscriber station's position, wherein

Mittel, um festzustellen, ob in Reaktion auf die GPS-Bestimmung der Position der Teilnehmerstation eine Aktualisierungsbedingung vorhanden ist;

4.1.1

the data structure also associates possible values of the one or more parameters with corresponding position uncertainty values, and the mapping maps the one or more parameter values from the one or more overhead messages to a corresponding position uncertainty value,

die Datenstruktur verknüpft mögliche Werte des oder der Parameter mit entsprechenden Werten für die Positionsunsicherheit, und beim Abbilden werden die Werte des oder der Parameter aus der oder den Overhead-Nachrichten auf einen entsprechenden Wert für die Positionsunsicherheit abgebildet;

4.1.1.1

wherein the position uncertainty values are coverage values indicating an area of coverage, and

die Werte für die Positionsunsicherheit sind Abdeckungswerte, die ein abgedecktes Gebiet anzeigen;

4.1.2

an update condition is determined to be present if the fix of the subscriber station's position is outside the area of coverage indicated by the mapped coverage value, and

eine Aktualisierungsbedingung wird festgelegt, wenn die ermittelte Position der Teilnehmerstation außerhalb des abgedeckten Gebiets liegt, das durch den abgebildeten Abdeckungswert angezeigt wird;

4.2

means for updating the data structure if an update condition is present.

Mittel zum Aktualisieren der Datenstruktur, wenn eine Aktualisierungsbedingung vorhanden ist.

13 3. Patentanspruch 1 schützt ein Verfahren, das entsprechende Merkmale aufweist und deshalb derselben Beurteilung unterliegt.

14 4. Einige Merkmale bedürfen der Erläuterung.

15 a) Um den Aufwand für die Positionsbestimmung zu verringern, geben die bereits in der erteilten Fassung vorgesehenen Merkmale 1 bis 2.1 vor, dass die Teilnehmerstation von einem Drahtloskommunikationssystem eine Nachricht empfangen kann, die einen Parameter enthält, anhand dessen eine erste Schätzung der aktuellen Position erfolgen kann.

16 Als Beispiel schildert die Beschreibung den Empfang einer Systemnachricht in einem Mobilfunksystem nach den Standards CDMA 2000 oder IS-856, die Angaben zur geographischen Breite und Länge des Standorts der Basisstation enthält. Die Genauigkeit dieser Angabe wird durch die Antennenreichweite der Basisstation bestimmt (Abs. 37-41).

17 Alternativ können zum Beispiel Kennzeichnungen für das System (subscriber station ID, SID), das Netzwerk (network ID, NID) oder die Basisstation (BASE-ID) herangezogen werden, durch die die Teilnehmerstation bedient wird. In Betracht kommt ferner eine Landeskennung (MCC, Abs. 43).

18 Patentanspruch 15 lässt offen, welche Informationen für diese erste Schätzung herangezogen werden.

19 b) Merkmal 2.2 sieht vor, dass die Teilnehmerstation eine zweite Positionsschätzung vornehmen kann.

20 Nach der Beschreibung kann diese Schätzung zum Beispiel anhand der Staatsangehörigkeit des Teilnehmers oder anhand einer älteren Positionsbestimmung vorgenommen werden, die mit Hilfe des GPS-Systems erfolgt ist. Im zuletzt genannten Fall hängt die Genauigkeit der Schätzung vom Alter der Positionsbestimmung ab (Abs. 64 f.).

21 Auch insoweit lässt Patentanspruch 15 offen, anhand welcher Informationen die Schätzung erfolgt.

22 c) Die Merkmale 2.3 bis 2.5 legen fest, welche der beiden Schätzungen für die Bestimmung der Ausgangsposition herangezogen wird.

23 Nach Merkmal 2.3 wird die erste Schätzung zu Grunde gelegt, wenn eine zweite Schätzung nicht verfügbar ist. Anderenfalls wird nach den Merkmalen 2.4 und 2.5 diejenige Schätzung herangezogen, die die geringere Positionsunsicherheit aufweist.

24 Wie die Berufung im Ansatz zutreffend ausführt, legen diese Merkmale nicht fest, anhand welcher Umstände die mit der jeweiligen Schätzung verbundene Positionsunsicherheit ermittelt wird. Sie sehen auch nicht vor, diesbezügliche Werte in der Teilnehmerstation vorzuhalten.

25 d) Die nunmehr noch verteidige Fassung sieht ergänzend die Hinterlegung einer Datenstruktur vor, mit deren Hilfe Parameter im Sinne von Merkmal 2 auf Positionen (Merkmal 2.6.1) und Positionsunsicherheitswerte (Merkmal 4.1.1) abgebildet werden können.

26 Diese Positionsunsicherheitswerte zeigen nach Merkmal 4.1.1.1 ein abgedecktes Gebiet an. Dies kann etwa durch Angabe eines Mittelpunkts und eines Radius erfolgen oder durch die geographischen Grenzen eines Landes (Abs. 49).

27 e) Merkmal 2.6.2 modifiziert die Merkmale 2.3 bis 2.5 dahin, dass eine so ermittelte Position als Ausgangsposition herangezogen wird, wenn eine andere Schätzung mit einer geringeren Unsicherheit nicht verfügbar ist.

28 Auch damit ist nicht festgelegt, anhand welcher Umstände die Positionsunsicherheit ermittelt wird. Merkmal 4.1.1 schafft zwar die Möglichkeit, hierfür geeignete Werte in der Datenstruktur zu hinterlegen. Anders als für die in der Datenstruktur hinterlegten Positionen sieht Merkmal 2.6.2 die Verwendung dieser Werte zur Bestimmung der Ausgangsposition aber nicht zwingend vor.

29 f) Nach Merkmal 3 wird die so ermittelte Ausgangsposition zur weiteren Positionsbestimmung mit Hilfe des GPS-Systems eingesetzt.

30 g) Merkmalsgruppe 4 sieht vor, dass die Datenstruktur aktualisiert wird, wenn sich anhand der Positionsbestimmung mittels GPS Bedarf für eine Änderung ergibt. Letzteres ist gemäß Merkmal 4.1.2 der Fall, wenn die ermittelte Position der Teilnehmerstation außerhalb des Gebiets liegt, das durch den in der Datenstruktur hinterlegten Abdeckungswert angezeigt wird.

31 II. Das Patentgericht hat seine Entscheidung, soweit für das Berufungsverfahren von Interesse, wie folgt begründet:

32 Der mit dem erstinstanzlichen Hilfsantrag verteidigte Gegenstand gehe nicht über den Inhalt der Anmeldung hinaus.

33 Er werde durch den Stand der Technik nicht vorweggenommen. Die internationale Patentanmeldung 2005/010549 (K5, Riley) offenbare nicht die Merkmale 4.1, 4.1.2 und 4.2. Die europäische Anmeldung 1 237 009 (K11, Alanen) offenbare weder die Merkmalsgruppe 4 noch die Merkmale 2.4 und 2.5. Die US-Anmeldung 2004/0104841 (K14, Syrjarinne) offenbare die Merkmale 2.2, 2.4 und 2.5 nicht und die Merkmale 2.3 und 2.6.2 nur teilweise.

34 Der mit dem erstinstanzlichen Hilfsantrag verteidigte Gegenstand sei patentfähig.

35 K14 beschäftige sich mit der Erzeugung, Pflege und Verbesserung bzw. Aktualisierung der geographischen Informationen für die Zellen des Mobilfunknetzes. Die dadurch erreichte Verbesserung habe keinen Anlass gegeben, weitere Positionsschätzungen auf Basis von Positionsunsicherheiten in Betracht zu ziehen, zumal in einem Mobilfunknetz regelmäßig Basisstationen mit kleineren Zellradien hinzugefügt würden.

36 Die in K11 beschriebene Auswahl der Ausgangsposition auf der Grundlage einer Schätzung der Bewegungsrichtung der mit drei Basisstationen in Kontakt stehenden Mobilstation erfülle nicht die Merkmale 2.4 und 2.5, weil nicht die Basisstation mit dem geringsten Zellradius ausgewählt werde, sondern diejenige, auf die sich die Mobilstation zubewege. Deshalb würden nach K11 auch keine Positionsunsicherheiten in der Datenbank gespeichert.

37 Da ausgehend von K14 kein Anlass bestanden habe, weitere Positionsschätzungen in Betracht zu ziehen, sei der verteidigte Gegenstand auch nicht durch Kombination von K14 mit K5 nahegelegt.

38 In K5 stehe die Auswertung aktueller Mobilfunksignale im Vordergrund. Angesichts dessen habe sich keine Veranlassung ergeben, eine - in K5 ohnehin nicht explizit genannte - Datenbank zu aktualisieren, auch wenn ein solches Vorgehen aus K14 und die Notwendigkeit zur Aktualisierung von Datenbanken bekannt seien.

39 III. Diese Beurteilung hält der Überprüfung im Berufungsverfahren in einem entscheidenden Punkt nicht stand.

40 1. Zu Recht hat das Patentgericht entschieden, dass der verteidigte Gegenstand durch K11, K5 und K14 nicht vorweggenommen ist.

41 a) K11 offenbart nicht die Speicherung und Aktualisierung von Werten für die Positionsunsicherheit.

42 aa) K11 befasst sich mit der Positionsbestimmung durch drahtlose Kommunikationsgeräte.

43 Nach der Beschreibung von K11 kann es schwierig sein, das von den Satelliten eines Positionsbestimmungssystems wie etwa GPS ausgesendete Signal von Hintergrundrauschen zu unterscheiden (Abs. 3 ff.). Dies führe zu hohem Synchronisationsaufwand, insbesondere nach dem Einschalten des Geräts oder nach einer längeren Phase unzureichenden Empfangs (Abs. 7 ff.).

44 Zur Verbesserung schlägt K11 vor, als Ausgangsposition (default location) die Position eines bekannten Referenzpunkts in der Umgebung des mobilen Geräts heranzuziehen. Hierzu können eine Vielzahl von Referenzpunkten und die zugehörigen Positionsangaben in einer Datenbank hinterlegt werden. Wenn diese Daten auf dem mobilen Gerät nicht gespeichert sind, können sie bei Bedarf über das Kommunikationsnetzwerk abgerufen werden (Abs. 22).

45 Bei einem Ausführungsbeispiel überprüft das mobile Gerät, ob Informationen zur Position der Basisstation verfügbar sind, mit der es verbunden ist. Wenn dies nicht der Fall ist, werden entsprechende Daten über das Netz aus einer Datenbank abgerufen. Mit Hilfe dieser Positionsdaten kann abgeschätzt werden, welche Satelliten sichtbar sind (Abs. 30 f.).

46 Wenn das mobile Gerät von einer Funkzelle in eine andere wechselt, werden die Positionsdaten der neuen Basisstation ermittelt. In dieser Situation können zusätzliche Daten errechnet werden, etwa der Mittelpunkt zwischen den beiden Basisstationen, weil es wahrscheinlich ist, dass das mobile Gerät sich während des Wechsels in diesem Bereich aufhält (Abs. 32 f.).

47 Wenn das mobile Gerät gleichzeitig mit mehreren Basisstationen kommunizieren kann, wie dies etwa bei CDMA möglich ist, kann als Ausgangsposition der geometrische Mittelpunkt zwischen diesen Basisstationen herangezogen werden. Ferner ist es möglich, die Bewegungsdaten des mobilen Geräts auszuwerten und die Position derjenigen Basisstation zu verwenden, die den geringsten Abstand zur Bewegungsrichtung hat (Abs. 34).

48 Neben den Positionsdaten einer Basisstation können auch bekannte Positionsdaten eines lokalen drahtlosen Netzwerks wie zum Beispiel WLAN oder Bluetooth als Ausgangsposition herangezogen werden (Abs. 43).

49 Um die Datenbank zu aktualisieren, kann ein mobiles Gerät, das seine Position erfolgreich ermittelt hat, diese Angaben und die Bezeichnung der Basisstation an den Datenbankserver senden. Dieser kann im Laufe der Zeit für jede Basisstation eine Vielzahl von Positionsangaben speichern. Daraus kann bei Bedarf ein Mittelwert errechnet werden.

50 Wenn an den Server auch der Wert für den Zeitversatz (timing advance, TA) übermittelt wird, mit dem das mobile Gerät Daten an die Basisstation sendet, kann der Abstand zwischen Basisstation und mobilem Gerät abgeschätzt werden (Abs. 46 f.).

51 bb) Wie das Patentgericht in dem gemäß § 83 Abs. 1 PatG erteilten Hinweis vom 14. März 2022 zutreffend angenommen hat, sind damit die Merkmale 2.2 bis 2.5 und 3 offenbart.

52 (1) In den Fällen, in denen die Position mehrerer Basisstationen ermittelt und die Position der Basisstation mit dem geringsten Abstand zur Bewegungsrichtung des mobilen Geräts ausgewählt wird, finden zwei Positionsschätzungen statt, von denen diejenige herangezogen wird, die eine geringere Unsicherheit aufweist.

53 Als Kriterium für die Auswahl zwischen zwei in Betracht kommenden Positionen wird in dieser Konstellation die Wahrscheinlichkeit herangezogen, mit der sich das mobile Gerät näher an der einen Basisstation befindet als an der anderen. Diese Wahrscheinlichkeit ist ein Maß für die Zuverlässigkeit der jeweiligen Positionsschätzung und damit zugleich ein Maß für die Positionsunsicherheit im Sinne der Merkmale 2.4 und 2.5. Da die beschriebene Auswahl nur dann vorgenommen wird, wenn die Positionen von zwei in Betracht kommenden Basisstationen verfügbar sind, ist auch Merkmal 2.3 verwirklicht.

54 (2) In Fällen, in denen das mobile Gerät von einer Funkzelle in die nächste wechselt, führt die in K11 vorgeschlagene Vorgehensweise dazu, dass anstelle des als erste Schätzung in Betracht kommenden Standorts der nunmehr aktuellen Basisstation der als wahrscheinlicher angesehene Mittelpunkt zwischen den beiden Funkzellen herangezogen wird.

55 Auch dies ist eine Auswahl auf der Grundlage von Wahrscheinlichkeiten und damit von möglichen Positionsunsicherheiten.

56 (3) Die Ableitung der GPS-Position des mobilen Geräts unter Verwendung der Vorgabeposition verwirklicht Merkmal 3.

57 cc) Es fehlt jedoch an einer Offenbarung der Merkmalsgruppe 4.

58 (1) Wie das Patentgericht zutreffend ausgeführt hat, offenbart K11 nicht die Speicherung von Werten für die Positionsunsicherheit in der Datenstruktur, wie dies die Merkmale 4.1.1 und 4.1.1.1 vorsehen.

59 In der Datenbank werden nur Angaben zur Position gespeichert, nicht aber die zur Auswahl herangezogene Bewegungsrichtung des mobilen Geräts. Dies ist zudem keine Eigenschaft, die mit dem Standort der jeweiligen Basisstation verknüpft ist und ein abgedecktes Gebiet anzeigt, sondern ein temporärer Zustand des mobilen Geräts.

60 (2) Eine Aktualisierung von Daten anhand von GPS-Positionsdaten offenbart K11 ebenfalls nur für die Positionsdaten der Basisstationen.

61 Wenn eine Vielzahl von Positionen für eine einzelne Basisstation gemeldet und in der Datenbank hinterlegt werden, ermöglicht dies zwar Rückschlüsse auf das von dieser Station abgedeckte Gebiet. K11 offenbart aber nicht, dass diese Daten herangezogen werden, um eine Auswahl zwischen in Frage kommenden Positionen zu treffen.

62 b) K5 offenbart eine Bestimmung der Ausgangsposition nach den Merkmalen 0 bis 2.5 und 2.6.2 und eine Positionsbestimmung im Sinne von Merkmal 3, nicht aber die Aktualisierung einer Datenstruktur im Sinne der Merkmalsgruppe 4.

63 aa) K5 befasst sich mit der Bestimmung der Position von Mobilfunkgeräten.

64 K5 führt aus, es gebe unterschiedliche Ansätze zur Positionsbestimmung, deren Effizienz zumindest teilweise vom geographischen Standort des mobilen Geräts abhänge. Deshalb sei es wünschenswert, wenn das Gerät die jeweilige Methode auswählen könne (Abs. 1006).

65 Vor diesem Hintergrund schlägt K5 vor, Positionsdaten auf zwei unterschiedlichen Wegen zu bestimmen und zwischen diesen beiden Angaben auf der Grundlage von vordefinierten Kriterien auszuwählen. Die erste Bestimmung (coarse pre-fix position) kann netzwerkbasierte Messungen umfassen, etwa der Pilotphase oder der Signalverzögerung. Die zweite Bestimmung (more precise pre-fix position) kann satellitenbasierte Messungen umfassen, etwa mittels GPS. Als Auswahlkriterium kann eine Schätzung des möglichen Positionsfehlers herangezogen werden (Abs. 1007-1009).

66 Die Kombination von netzwerkbasierten und anderen Methoden ermögliche eine Positionsbestimmung sowohl in ländlichen Regionen, in denen wenige Sendestationen in Reichweite des Mobilfunkgeräts seien, dafür aber guter GPS-Empfang herrsche, als auch in dichtbesiedelten Gebieten und in Gebäuden, in denen die entgegengesetzte Ausgangslage vorliegen könne (Abs. 1021 f.).

67 bb) Damit sind, wie das Patentgericht zutreffend ausgeführt hat, die Merkmale 0 bis 2.5, 2.6.2 und 3 offenbart.

68 cc) Ob K5 zu entnehmen ist, dass die zur netzwerkbasierten Positionsbestimmung herangezogenen Daten wie etwa der Radius einer Funkzelle in einer Datenstruktur im Speicher des mobilen Geräts hinterlegt werden, kann dahingestellt bleiben. Wie das Patentgericht zu Recht angenommen hat, offenbart K5 jedenfalls keine Aktualisierung solcher Datenstrukturen gemäß der Merkmalsgruppe 4.

69 c) K14 offenbart zwar eine Aktualisierung im Sinne der Merkmale 2.6.1 und 3 sowie der Merkmalsgruppe 4, nicht aber eine Auswahl zwischen zwei Schätzungen im Sinne der Merkmale 2.2 bis 2.5 und 2.6.2.

70 aa) K14 befasst sich mit der Erstellung und Aktualisierung von Datenbanken zur Unterstützung der Positionsbestimmung von mobilen Endgeräten (Abs. 1).

71 Nach der Beschreibung von K14 erfordert die Positionsbestimmung mittels GPS unter schlechten Empfangsbedingungen eine gewisse Unterstützung. Wenn der Empfänger mit einem Mobilfunknetz verbunden sei, bestehe die einfachste Möglichkeit darin, über dieses Netzwerk Navigationsdaten an den GPS-Empfänger zu versenden (Abs. 7).

72 Eine anspruchsvollere Möglichkeit der Unterstützung des Empfängers sei die Übermittlung der genauen GPS-Zeit an den Empfänger. Ergänzend zur exakten Zeit sei die Angabe einer bekannten Position in der Nähe der erwarteten Position des Empfängers erforderlich (Abs. 8). In einem Mobilfunknetz könnten hierzu die Koordinaten der Zelle verwendet werden, in der sich das mobile Gerät befinde. Die üblicherweise verwendeten Kennungen für Zellen enthielten solche Daten aber nicht (Abs. 9).

73 Ferner sei es zweckmäßig, die Verlässlichkeit einer Referenzposition zu kennen, d.h. die maximale Entfernung zwischen dieser Position und der aktuellen Position des Empfängers. Wenn die Genauigkeit der Referenzposition für bestimmte Anwendungen ausreiche, sei ein Einsatz von GPS sogar entbehrlich (Abs. 10).

74 In herkömmlichen Systemen seien Angaben zur Genauigkeit allenfalls durch ein Mobilfunknetz zu erhalten (Abs. 11). Um zu vermeiden, dass jedes Mal auf das Mobilfunknetz zugegriffen werden müsse, schlage K11 das Vorhalten und die Verwendung einer Datenbank vor. Dort sei aber nicht offenbart, wie die dafür erforderlichen geographischen Informationen geschätzt werden könnten (Abs. 13).

75 K14 schlägt hierzu vor, unter Rückgriff auf Satellitensignale oder Netzwerke wie WLAN oder Bluetooth eine Position des mobilen Geräts zu berechnen, daraus geographische Informationen zur Zelle abzuleiten und diese zusammen mit einer Kennung der Zelle (z.B. CGI) in der Datenbank zu hinterlegen (Abs. 15). Wenn mehrere Angaben zu einer Zelle vorhanden sind, können diese verwendet werden, um eine Referenzposition zu ermitteln, die möglichst nahe am Mittelpunkt der Zelle liegt. Auf diese Weise kann der maximale Abstand zwischen Mobilgerät und Referenzposition minimiert werden (Abs. 18).

76 Ergänzend zu geographischen Informationen kann der Bereich einer Zelle geschätzt und zur Speicherung in der Datenbank bereitgestellt werden. Hierfür kann zum Beispiel der Radius der Zelle herangezogen werden (Abs. 23). In einer bevorzugten Ausführungsform können die geographischen Informationen und der geschätzte Zellenbereich aktualisiert werden (Abs. 24).

77 bb) Damit sind, wie das Patentgericht zutreffend ausgeführt hat, die Merkmale 2.6.1 und 3 sowie die Merkmalsgruppe 4 offenbart.

78 Anders als K11 sieht K14 nicht nur die Speicherung und Aktualisierung von geographischen Informationen zur Position einer Basisstation im Sinne von Merkmal 2.6.1 vor, sondern auch Angaben zu deren Abdeckungsbereich. Die hinterlegten und anhand von GPS-Messungen bei Bedarf aktualisierten Angaben zu Mittelpunkt und Radius der zu einer Basisstation gehörenden Funkzelle ermöglichen Rückschlüsse über das von dieser Zelle abgedeckte Gebiet und verwirklichen deshalb die Merkmale 4.1.1 und 4.1.1.1. Der in K14 vorgeschlagene Ablauf für eine Aktualisierung verwirklicht die Merkmale 3, 4.1, 4.1.2 und 4.2.

79 cc) Nicht offenbart sind eine zweite Positionsschätzung im Sinne von Merkmal 2.2 und eine Auswahl zwischen zwei Schätzungen nach den Merkmalen 2.3 bis 2.5 und 2.6.2.

80 2. Entgegen der Auffassung des Patentgerichts war der verteidigte Gegenstand ausgehend von K14 durch K11 nahegelegt.

81 a) Ausgehend von K14 bestand Anlass, die in der Datenbank hinterlegten Informationen für eine Positionsbestimmung einzusetzen, wie sie K11 vorschlägt.

82 aa) Wie bereits oben dargelegt wurde, führt K14 als wesentlichen Kritikpunkt bezüglich K11 lediglich an, dass dort nicht offenbart werde, wie die in einer Datenbank hinterlegten geographischen Informationen geschätzt werden könnten. K14 befasst sich mit diesem Aspekt und zeigt Wege auf, um eine solche Datenbank aufzubauen und zu aktualisieren. Grundlegend abweichende Möglichkeiten, um solche Informationen zu einer ersten Positionsbestimmung heranzuziehen, sind K14 demgegenüber nicht zu entnehmen.

83 Vor diesem Hintergrund stellt sich das in K14 beschriebene Verfahren nicht als vollständige Alternative zu der in K11 vorgeschlagenen Positionsbestimmung dar, sondern als Ergänzung mit dem Ziel einer verbesserten Datenhaltung und -aktualisierung. Dies gab Anlass, eine Datenbank nach dem Vorbild von K14 für eine Positionsbestimmung einzusetzen, wie sie K11 offenbart.

84 bb) Dem steht nicht entgegen, dass die in K14 vorgeschlagene Art der Datenhaltung und -aktualisierung je nach Einzelfall die Möglichkeit bietet, die Positionsbestimmung schon auf der Grundlage einer einzigen Schätzung vorzunehmen.

85 Wie das Patentgericht im Einzelnen dargelegt hat, eröffnet das in K14 vorgeschlagene Verfahren allerdings die Aussicht, dass die in der Datenbank hinterlegten Angaben im Laufe der Zeit immer genauer und zuverlässiger werden und so insbesondere in kleinen Funkzellen eine zweite Schätzung, wie sie K11 und das Streitpatent vorschlagen, nicht erforderlich ist.

86 Wie die Berufung zu Recht geltend macht, bestand jedoch auch vor diesem Hintergrund Anlass, die in K11 vorgeschlagenen Möglichkeiten zur Auswahl zwischen mehreren in Betracht kommenden Basisstationen beizubehalten.

87 Die in K14 vorgeschlagene Datenhaltung und -aktualisierung liefert nur dann genaue und zuverlässige Ergebnisse, wenn hinreichende Daten über die Funkzelle vorliegen, mit der das Mobilgerät verbunden ist. Die Wahrscheinlichkeit, dass solche Daten vorliegen, nimmt zwar mit zunehmender Nutzungsdauer zu. Dennoch ist stets damit zu rechnen, dass über einzelne Funkzellen nur unzureichende Daten vorliegen - etwa über solche Funkzellen, mit denen das Mobilgerät erstmals in Verbindung tritt.

88 Auch bei Verfügbarkeit genauerer Daten kann sich zudem die in K11 beschriebene Situation einstellen, dass das Mobilgerät mit zwei oder mehr Funkzellen in Verbindung steht und sich deshalb die Frage stellt, welche Zelle als maßgeblich betrachtet werden soll.

89 Da K14 diese Fragen nicht vertieft behandelt, lag es nahe, es insoweit bei den in K11 vorgeschlagenen Vorgehensweisen zu belassen, also zum Beispiel die Positionsdaten derjenigen Zelle heranzuziehen, deren Mittelpunkt der Bewegungsrichtung des mobilen Geräts am nächsten liegt, oder den Mittelpunkt zwischen zwei Funkzellen.

90 Ob damit für die Auswahl zwischen zwei in Frage kommenden Positionen ein Kriterium herangezogen wird, das in der Datenbank nicht abgespeichert ist, ist für die Entscheidung des Streitfalls nicht erheblich. Wie die Berufung zutreffend geltend macht, geben die Merkmale 2.3, 2.5 und 2.6.2 nicht zwingend vor, welcher Wert für die Positionssicherheit bei der Auswahl herangezogen wird. Entsprechend beschreibt das Streitpatent seinerseits Positionsunsicherheiten, die auf anderen Grundlagen als dem abgespeicherten Abdeckungsbereich einer Funkzelle beruhen, wie etwa der zeitlichen Alterung einer älteren GPS-Schätzung (Abs. 138, Figur 35).

91 Unabhängig davon fließen bei der durch K14 nahegelegten Vorgehensweise im Falle des Wechsels von einer Funkzelle in eine andere auch die in der Datenbank aus K14 hinterlegten Werte zum Abdeckungsbereich in die Auswahlentscheidung ein, weil Mittelpunkt und Radius der jeweiligen Funkzelle Auswirkungen auf die Lage des Mittelpunkts zwischen zwei Basisstationen haben.

92 3. Entgegen der Auffassung des Patentgerichts war der verteidigte Gegenstand auch ausgehend von K5 durch K14 nahegelegt.

93 a) Ausgehend von K5 ergab sich Anlass für die Suche nach weiteren Verbesserungsmöglichkeiten insbesondere aus dem in K5 enthaltenen Hinweis, dass wegen der unterschiedlichen Empfangsbedingungen je nach dem aktuellen Standort des mobilen Geräts unterschiedliche Methoden zur Standortbestimmung von Vorteil sein können (Abs. 1021 f.).

94 Wie die Berufung zutreffend vorbringt, bot dies Veranlassung, nach Verbesserungsmöglichkeiten für die Ableitung der Ausgangsposition aus netzwerkbasierten Informationen zu suchen, um die Ausgangsposition auch dann möglichst genau bestimmen zu können, wenn ihre Ableitung aus vorangegangenen GPS-Satellitensignalen erschwert ist, wie etwa in städtischen Gebieten (Abs. 1022).

95 b) Daraus ergab sich die Anregung, die in K14 offenbarten Möglichkeiten zum Erzeugen, Vorhalten und Aktualisieren von Datenstrukturen auf dem mobilen Gerät in Erwägung zu ziehen, um eine möglichst genaue Bestimmung der Ausgangsposition auch an diesen Orten oder an solchen Orten zu ermöglichen, an denen der Abruf solcher Daten über das Netzwerk Schwierigkeiten bereitet.

96 c) Entgegen der Ansicht der Beklagten stand dem nicht entgegen, dass K14 sich in erster Linie mit dem Aufbau und der Pflege einer Datenbank zur Modellierung eines Zellenbereichs einer Basisstation befasst. Wie ausgeführt hebt K14 hervor, dass die beschriebene Datenstruktur für die Positionsbestimmung eines mobilen Geräts verwendet werden soll (Abs. 1, Abs. 14). Dies legte es nahe, sie in die Überlegungen zur Verbesserung der in K5 vorgesehenen netzwerkbezogenen Positionsschätzung einzubeziehen.

97 d) Zugleich bestand Anlass, das in K5 vorgeschlagene Grundkonzept einer Auswahl der Ausgangsposition anhand von zwei Positionsbestimmungen in Verbindung mit Genauigkeitskriterien beizubehalten.

98 aa) K5 beschreibt, dass je nach Standort der eine oder der andere Ansatz vorteilhaft sein kann.

99 Wie das Patentgericht zutreffend ausgeführt hat, ermöglicht das in K14 vorgeschlagene Konzept zur Gewinnung und Aktualisierung von Daten zwar eine hohe Genauigkeit, insbesondere wenn eine Vielzahl von Mobilfunkzellen vorhanden ist. Damit ist allerdings, wie K5 hervorhebt, nicht gewährleistet, dass solche Ausgangsbedingungen an jedem Standort, insbesondere auch in ländlichen Gegenden, anzutreffen sind (Abs. 1021). Folglich war es konsequent, das Grundkonzept aus K5 beizubehalten und um die Optimierung der netzwerkbezogenen Positionsschätzung nach dem Vorbild von K14 zu ergänzen.

100 bb) Anlass für die Beibehaltung des in K5 offenbarten Konzepts ergab sich zudem daraus, dass eine Positionsschätzung nach dem in K14 beschriebenen Verfahren ausgeschlossen ist, wenn für den Zellenbereich, in dem sich das mobile Gerät befindet, noch keine Daten in der Datenbank abgelegt sind, weil noch keine Position des mobilen Geräts in der Zelle berechnet worden ist.

101 Auch in dieser Konstellation erweist sich die Ableitung der Ausgangsposition des mobilen Geräts aus einer weiteren als der in K14 beschriebenen Positionsschätzung, insbesondere eine aus einer älteren GPS-Position abgeleitete Schätzung im Sinne der K5 als vorteilhaft.

102 IV. Die Kostenentscheidung beruht auf § 91 Abs. 1 ZPO.

Bacher

Hoffmann

Rensen

Crummenerl

von Pückler
