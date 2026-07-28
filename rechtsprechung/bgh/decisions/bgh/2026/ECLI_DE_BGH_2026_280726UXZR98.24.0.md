---
ecli: "ECLI:DE:BGH:2026:280726UXZR98.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 98/24"
decided: "2026-07-28"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE303992026.xml"
neuris_doknr: "KORE303992026"
---

# Bundesgerichtshof, X ZR 98/24 vom 2026-07-28

## Leitsatz

Überbrücktes Netzwerk

Ein in der Patentanmeldung enthaltener Hinweis, dass einzelne Verfahrensschritte eines Ausführungsbeispiels nicht zwingend verwirklicht werden müssen, reicht nicht aus, um ein Verfahren, bei dem diese Schritte durch eine konkrete andere Vorgehensweise ersetzt werden, unmittelbar und eindeutig als zur Erfindung gehörend zu offenbaren.62

## Tenor

Die Berufung gegen das Urteil des 5. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 7. Mai 2024 wird auf Kosten der Beklagten zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 057 796 (Streitpatents), das am 19. Juni 2007 unter Inanspruchnahme einer US-amerikanischen Priorität vom 22. August 2006 angemeldet worden ist und eine Punkt-zu-Mehrpunkt-Funktionalität in einem überbrückten Netzwerk betrifft.

2 Patentanspruch 1, auf den vierzehn Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A method being performed by a switch (28) connectable to a first network (26) via a network interface (36) and to a Customer Premises equipment, CPE, (22) addressable by a first Medium Access Control, MAC, address via an interface of a first type (34), the method comprising:

receiving (70), via the interface of the first type, a first unicast frame from the CPE, the first unicast frame having a destination address that is a second MAC address associated with the first network; and

receiving (70), via the network interface, a second frame from the first network, the second frame having a destination address that is the first MAC address; characterized in that:

the first network is an Open System Interface, OSI, Layer-2 Ethernet bridged network that uses MAC address-based routing, and

the method further comprising:

marking (72) the first unicast frame as a first interface frame by placing an indication in the first unicast frame that the frame is a frame received via an interface of the first type:

forwarding (78, 98) the first unicast frame to the first network as a marked frame;

responsive to the second frame being a unicast frame that comprises the indication that the frame is a frame received via an interface of the first type, discarding (80) the second frame; and

responsive to the second frame being a non-unicast frame or not being a unicast frame that comprises the indication that the frame is a frame received via an interface of the first type, forwarding (78, 98) the frame to the CPE via the first type interface.

3 Beide Klägerinnen haben geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Die Klägerin zu 2 hat ergänzend geltend gemacht, die Erfindung sei nicht so offenbart, dass ein Fachmann sie ausführen könne.

4 Die Beklagte hat das Streitpatent in der erteilten Fassung und mit elf Hilfsanträgen in geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt.

6 Mit ihrer dagegen gerichteten Berufung verfolgt die Beklagte ihre erstinstanzlichen Anträge weiter. Die Klägerinnen treten dem Rechtsmittel entgegen.

## Entscheidungsgründe

7 Die Berufung ist zulässig, jedoch nicht begründet.

8 I. Das Streitpatent betrifft die Übertragung von Rahmen (frames) in überbrückten Netzwerken.

9 1. Nach der Beschreibung des Streitpatents verbinden lokale Netzwerke (local area networks, LANs) die Computersysteme in der zweiten Schicht (layer 2).

10 Dieser Begriff beziehe sich auf die zweite Schicht des bekannten OSI-Modells (open systems interface model). Layer 2 werde auch als MAC-Schicht (media access control layer) bezeichnet. Jedes Computersystem werde über eine MAC-Einrichtung mit einem lokalen Netzwerk verbunden.

11 Mehrere lokale Netzwerke könnten mit Hilfe von MAC-Brücken miteinander verbunden werden. MAC-Brücken, die den Standard IEEE 802.1D implementierten, ließen MAC-Einrichtungen, die in physikalisch getrennten lokalen Netzen angeordnet seien, im Verhältnis zueinander so erscheinen, als seien sie mit einem einzigen lokalen Netzwerk verbunden (Abs. 2).

12 MAC-Brücken führten eine Weiterleitungsdatenbank (forwarding database, FDB), in der Ziel-MAC-Adressen den einzelnen Schnittstellen (die auch als Ports bezeichnet würden) zugeordnet seien. Hierzu werde die Quell-MAC-Adresse der auf den einzelnen Schnittstellen eingehenden Rahmen gespeichert. Wenn eine MAC-Brücke eine angegebene Ziel-MAC-Adresse in der Datenbank nicht finde, leite sie den empfangenen Rahmen über alle verfügbaren Schnittstellen weiter (flood), mit Ausnahme derjenigen, auf dem dieser Rahmen empfangen worden sei (Abs. 3).

13 Überbrückte Layer-2-Netzwerke seien üblicherweise so konfiguriert, dass sie eine Mehrpunkt-zu-Mehrpunkt Verbindung zwischen allen Computern des Netzwerks bereitstellten. In einigen Anwendungen sei es jedoch insbesondere aus Sicherheitsgründen erforderlich, dass bestimmte Computer nicht direkt miteinander kommunizieren könnten. Dies könne etwa der Fall sein, wenn ein Internet Service Provider (ISP) ein Aggregationsnetzwerk einsetze, um den Kundenverkehr zu und von einem Zugangsrouter zu bündeln (Abs. 4).

14 Melson et al. hätten verschiedene Methoden vorgeschlagen, um eine Direktkommunikation zu unterbinden. Diese seien aber wenig effizient (Abs. 5 f.).

15 2. Das Streitpatent betrifft vor diesem Hintergrund das technische Problem, ein effizientes Verfahren zur Verfügung zu stellen, um eine direkte Kommunikation zwischen Computern in einem überbrückten Layer-2-Netzwerk bei Bedarf zu verhindern.

16 3. Zur Lösung schlägt das Streitpatent in Anspruch 1 ein Verfahren vor, dessen Merkmale sich wie folgt gliedern lassen:

17 1

A method being performed by a switch (28) connectable to a first network (26) via a network interface (36) and to a Customer Premises equipment, CPE (22), addressable by a first Medium Access Control, MAC, address via an interface of a first type (34).

Verfahren, das von einem Switch (28) durchgeführt wird, der über eine Netzwerkschnittstelle (36) mit einem ersten Netzwerk (26) und über eine Schnittstelle eines ersten Typs (34) mit einem Customer Premises Equipment, CPE (22), das über eine erste Medium Access Control, MAC, Adresse adressierbar ist, verbunden werden kann.

4

The first network is an Open System Interface, OSI, Layer-2 Ethernet bridged network that uses MAC address-based routing.

Das erste Netzwerk ist ein überbrücktes Open System Interface, OSI, Layer-2 Ethernet-Netzwerk, das ein MAC-Adressen-basiertes Routing verwendet.

The method comprises:

Das Verfahren umfasst:

2

Receiving (70), via the interface of the first type, a first unicast frame from the CPE, the first unicast frame having a destination address that is a second MAC address associated with the first network;

Empfangen (70) eines ersten Unicast-Frames von dem CPE über die Schnittstelle des ersten Typs, wobei der erste Unicast-Frame eine Zieladresse aufweist, die eine zweite MAC-Adresse ist, die dem ersten Netzwerk zugeordnet ist;

5.1

marking (72) the first unicast frame as a first interface frame by placing an indication in the first unicast frame that the frame is a frame received via an interface of the first type;

Markieren (72) des ersten Unicast-Frames als ersten Schnittstellen-Frame durch Anordnen einer Angabe in dem ersten Unicast-Frame, dass der Frame ein Frame ist, der über eine Schnittstelle des ersten Typs empfangen wurde;

5.2

forwarding (78, 98) the first unicast frame to the first network as a marked frame.

Senden (78, 98) des ersten Unicast-Frames an das erste Netzwerk als markierten Frame.

3

Receiving (70), via the network interface, a second frame from the first network, the second frame having a destination address that is the first MAC address;

Empfangen (70) eines zweiten Frames von dem ersten Netzwerk über die Netzwerkschnittstelle, wobei der zweite Frame eine Zieladresse aufweist, welche die erste MAC-Adresse ist;

5.3

responsive to the second frame being a unicast frame that comprises the indication that the frame is a frame received via an interface of the first type, discarding (80) the second frame;

in Reaktion darauf, dass der zweite Frame ein Unicast-Frame ist, der die Angabe umfasst, dass der Frame ein Frame ist, der über eine Schnittstelle des ersten Typs empfangen wird, Verwerfen (80) des zweiten Frames;

5.4

responsive to the second frame being a non-unicast frame or not being a unicast frame that comprises the indication that the frame is a frame received via an interface of the first type, forwarding (78, 98) the frame to the CPE via the first type interface.

in Reaktion darauf, dass der zweite Frame ein Non-Unicast-Frame ist oder kein Unicast-Frame ist, der die Angabe umfasst, dass der Frame ein Frame ist, der über eine Schnittstelle des ersten Typs empfangen wird, Senden (78, 98) des Frames über die Schnittstelle des ersten Typs an das CPE.

18 4. Einige Merkmale bedürfen der näheren Erörterung.

19 a) Eine Netzwerkstruktur, in der das geschützte Verfahren ausgeführt werden kann, ist beispielhaft in der nachfolgend wiedergegebenen Figur 1 dargestellt.

20 b) Das geschützte Verfahren wird gemäß Merkmal 1 auf einem Switch (28) ausgeführt, der mindestens zwei Schnittstellen aufweist.

21 aa) Eine als Netzwerkschnittstelle (36) bezeichnete Schnittstelle dient der Verbindung mit einem ersten Netzwerk (26).

22 Dieses Netzwerk ist gemäß Merkmal 4 ein überbrücktes Layer-2-Netzwerk mit Ethernet-Technologie.

23 Aus dem Erfordernis einer Überbrückung ergibt sich, dass es mindestens eine weitere Einrichtung geben muss, die Computern den Zugang zu diesem Netzwerk ermöglicht.

24 Figur 1 zeigt hierzu exemplarisch drei Switches (28) mit je einer Netzwerkschnittstelle (36) und zwei Verbindungsknoten (30), die zusätzlich eine Schnittstelle (32) zu einem öffentlichen Netzwerk aufweisen. Patentanspruch 1 lässt offen, welche anderen Einrichtungen einen Zugang zu dem überbrückten Netz ermöglichen.

25 bb) Eine als Schnittstelle ersten Typs bezeichnete Schnittstelle (34) dient der Verbindung mit einem lokalen Gerät (Customer Premises Equipment, CPE) (22), das über eine MAC-Adresse adressiert werden kann.

26 Dies kann zum Beispiel ein Computer sein (Abs. 21).

27 Nach Merkmal 1 genügt es, wenn der Switch eine einzige Schnittstelle dieses Typs aufweist. Damit ist nicht ausgeschlossen, dass mehrere solcher Schnittstellen vorhanden sind, wie dies Figur 1 für alle dort dargestellten Switches (28) und Verbindungsknoten (30) zeigt. Möglich ist auch, dass an eine Schnittstelle dieses Typs ein kundenseitiges lokales Netzwerk (customer-premises LAN) angeschlossen ist (Abs. 23 Z. 51-53).

28 c) Die Merkmale 2 und 3 sowie die Merkmalsgruppe 5 definieren Vorgaben für zwei unterschiedliche Betriebssituationen.

29 aa) Die Merkmale 2, 5.1 und 5.2 betreffen den Fall, dass der Switch (28) über die Schnittstelle des ersten Typs einen Unicast-Rahmen empfängt, der von einem lokalen Gerät (CPE) stammt und als Zieladresse eine MAC-Adresse enthält, die dem ersten Netzwerk (26) zugeordnet ist.

30 (1) Unicast-Rahmen sind Rahmen, die an eine einzige Zieladresse gerichtet sind.

31 Dieses dem allgemeinen technischen Sprachgebrauch entsprechende Verständnis liegt auch dem Streitpatent zu Grunde.

32 Die Beschreibung des Streitpatents unterscheidet - ebenfalls in Einklang mit dem allgemeinen technischen Sprachgebrauch - zwischen Unicast-, Multicast- und Broadcast-Rahmen (Abs. 37).

33 Das Streitpatent verwendet den Begriff "broadcast" für Rahmen, die an alle verfügbaren Schnittstellen weitergeleitet werden (Abs. 12).

34 Den Begriff "Multicast-Rahmen" verwendet die Beschreibung für Rahmen, die an eine Gruppe von Schnittstellen weitergeleitet werden (Abs. 40).

35 In Einklang damit spricht die Beschreibung von "Unicast-Rahmen", wenn es darum geht, einen Rahmen - sofern die zur Zieladresse gehörende Schnittstelle bekannt ist - nur an eine einzelne Schnittstelle weiterzuleiten (insbesondere Abs. 40).

36 (2) Ein empfangener Unicast-Rahmen, der den in Merkmal 2 definierten Kriterien entspricht, wird gemäß Merkmal 5.1 mit einer Markierung versehen, die anzeigt, dass er über eine Schnittstelle des ersten Typs empfangen worden ist.

37 (3) Nach Merkmal 5.2 wird der Rahmen mit dieser Markierung an das erste Netzwerk weitergeleitet.

38 (4) Wie der Switch mit Multicast- oder Broadcast-Rahmen zu verfahren hat, die er über eine Schnittstelle des ersten Typs von einem lokalen Gerät (CPE) empfängt, ist in Patentanspruch 1 nicht festgelegt.

39 bb) Die Merkmale 3, 5.3 und 5.4 betreffen den Fall, dass der Switch (28) über die Netzwerkschnittstelle (36) einen Rahmen empfängt, der aus dem ersten Netzwerk (26) stammt und als Zieladresse die erste MAC-Adresse aufweist.

40 (1) Die erste MAC-Adresse im Sinne von Merkmal 3 ist gemäß der Definition in Merkmal 1 die MAC-Adresse eines lokalen Geräts (CPE), das mit einer Schnittstelle des ersten Typs verbunden ist.

41 (2) Gemäß Merkmal 5.3 wird ein solcher Rahmen verworfen, wenn es sich um einen Unicast-Rahmen handelt und dieser eine Kennzeichnung aufweist, aus der sich ergibt, dass er über eine Schnittstelle des ersten Typs empfangen worden ist.

42 Diese Vorgehensweise soll verhindern, dass Unicast-Rahmen, die von einem lokalen Gerät (CPE) stammen, zu einem solchen Gerät weitergeleitet werden (Abs. 47). Sie stellt also sicher, dass lokale Geräte (CPE) nicht direkt miteinander kommunizieren können.

43 (3) Gemäß Merkmal 5.4 wird ein Rahmen, der die in Merkmal 3 vorgesehenen Kriterien erfüllt, hingegen an das lokale Gerät (CPE) weitergeleitet, wenn er kein Unicast-Rahmen ist oder wenn er keine Kennzeichnung aufweist, aus der sich ergibt, dass er über eine Schnittstelle des ersten Typs empfangen worden ist.

44 Im Ergebnis werden mithin alle Broadcast- und Multicast-Rahmen weitergeleitet, außerdem alle Unicast-Rahmen, die die in Merkmal 5.1 vorgesehene Kennzeichnung nicht tragen.

45 II. Das Patentgericht hat seine Entscheidung - soweit im Berufungsverfahren von Interesse - im Wesentlichen wie folgt begründet:

46 Der Gegenstand von Patentanspruch 1 sei ursprünglich offenbart. Nach dem Inhalt der Anmeldung werde die Unterscheidung zwischen Unicast- und Nicht-Unicast-Rahmen aufgrund der Weiterleitungsdatenbank (MAC FBD 58) und der Auswertung der Zieladresse (MAC DA) getroffen. Alle anderen Rahmen würden über die Ausgangsschnittstelle des Switches weitergeleitet. Zwar würden gemäß Figur 4 empfangene Frames in Schritt 72 mit einem so genannten UNI-Type-Marker versehen, der den Schnittstellentyp angebe. Dieser werde in dem Ausführungsbeispiel jedoch nicht ausgewertet. Insofern sei ursprünglich offenbart, dass alle nicht markierten Unicast-Frames in herkömmlicher Weise weitergeleitet würden. Das gelte auch für alle Broadcast-Frames, die das Netzwerk von außen erreichten.

47 Der Gegenstand von Patentanspruch 1 ergebe sich für den Fachmann, einen Diplom-Ingenieur der Elektrotechnik oder Informatik mit mehrjähriger Erfahrung im Bereich von Netzwerken und Netzwerkgeräten in einer Layer-2-Netzwerkumgebung, jedoch in naheliegender Weise aus der internationalen Patentanmeldung 2004/075509 (NK6-1). Deshalb könne dahingestellt bleiben, ob die Erfindung so offenbart sei, dass ein Fachmann sie ausführen könne.

48 III. Diese Beurteilung hält der Nachprüfung im Berufungsverfahren zwar nicht in allen Punkten der Begründung, aber im Ergebnis stand.

49 1. Entgegen der Auffassung des Patentgerichts geht der Gegenstand des Streitpatents über den Inhalt der ursprünglich eingereichten Unterlagen hinaus.

50 a) Wie das Patentgericht im Ausgangspunkt zutreffend dargelegt hat, sieht die Anmeldung (veröffentlicht als WO 2008/023360 A2, NK2-1) - ebenso wie die Beschreibung des Streitpatents - in den Erläuterungen zu der nachfolgend wiedergegebenen Figur 4 ein Verwerfen von Rahmen nur unter der in Merkmal 5.1 formulierten Bedingung vor.

51 Bei diesem Ausführungsbeispiel erhalten eingehende Rahmen eine Markierung, die den Typ der Schnittstelle angibt, über den der Rahmen eingegangen ist (user network interface type, UNI type). Bei dem Beispiel gibt es die Typen "hub" und "spoke". Der Typ "spoke" entspricht dem ersten Typ im Sinne von Merkmal 1; der Typ "hub" bezeichnet eine Schnittstelle, die zu einem öffentlichen Netzwerk führt (S. 7 Z. 24-29).

52 Rahmen, die über eine Schnittstelle vom Typ "hub" oder "spoke" eingehen, erhalten in Schritt 72 eine entsprechende Markierung. Rahmen, die über die Netzwerkschnittstelle eingehen, werden beim Eingang nicht markiert, weil sie notwendigerweise schon zuvor markiert worden sind (S. 11 Z. 23-29).

53 In Schritt 74 werden bereits vorhandene Einträge in der Weiterleitungsdatenbank angepasst und bestimmte Rahmen, die aufgrund einer Schleife auf Kundenseite eingetroffen sein könnten, optional verworfen (S. 12 Z. 9 bis S. 13 Z. 2).

54 In Schritt 76 wird die Schnittstelle bestimmt, an die der Rahmen weitergeleitet wird. Hierzu wird bei Unicast-Rahmen die Weiterleitungsdatenbank (MAC FDB 58) herangezogen, für Broadcast- und Multicast-Rahmen hingegen die Flood-Datenbank (60). Unicast-Rahmen, die die Markierung "spoke-type" tragen und deren Zieladresse in der Weiterleitungsdatenbank ebenfalls als "spoke-type" markiert sind, werden als unzulässig betrachtet und deshalb in Schritt 80 verworfen. Andere Rahmen werden in Schritt 78 über die entsprechende, in Schritt 76 bestimmte Ausgangsschnittstelle weitergeleitet (S. 13 Z. 7-13).

55 b) Entgegen der Auffassung des Patentgerichts ergibt sich aus dem zuletzt zitierten Satz nicht, dass bei dem in Figur 4 dargestellten Beispiel alle Rahmen, die die in Merkmal 5.1 definierte Bedingung nicht erfüllen, weitergeleitet werden. Der in diesem Zusammenhang angeführte Schritt 76, in dem die Ausgangsschnittstelle bestimmt wird, sieht vielmehr ebenfalls vor, dass Rahmen, die die Markierung "spoke-type" tragen, nicht an Zieladressen dieses Typs weitergeleitet werden.

56 aa) Die Details des Schritts 76 sind in der nachfolgend wiedergegebenen Figur 5 dargestellt (S. 13 Z. 20 f.).

57 In diesem Zusammenhang werden in Schritt 90 der Typ der Schnittstelle, über die der Rahmen eingegangen ist, und in Schritt 96 der Typ der Schnittstelle der Zieladresse überprüft. Rahmen mit der Markierung "spoke-type" werden nicht an Schnittstellen vom Typ "spoke-type" weitergeleitet (flooded) (S. 14 Z. 2 f.).

58 bb) Entgegen der Auffassung der Berufung werden in diesem Beispiel auch Multicast-Frames in der dargestellten Weise geprüft und gegebenenfalls verworfen.

59 Schon aus den oben wiedergegebenen Ausführungen zu Figur 4 ergibt sich, dass grundsätzlich alle eingehenden Rahmen eine Markierung erhalten. Eine diesbezügliche Unterscheidung zwischen Unicast- und Non-Unicast-Rahmen ist diesen Ausführungen nicht zu entnehmen.

60 Die Anmeldung enthält darüber hinaus den ausdrücklichen Hinweis, dass auch in der Flood-Datenbank (60) UNI-Kennungen vergeben werden sollten, um die Weiterleitung von Multicast- und Broadcast-Rahmen zu steuern (S. 11 Z. 15-17).

61 cc) Dem Umstand, dass die Figuren 4 und 5 und die darauf bezogenen Passagen der Anmeldung nur ein Ausführungsbeispiel betreffen und dass die Verwerfung von Rahmen in Figur 4 nur als optional dargestellt wird, mag zu entnehmen sein, dass die Markierung von Multicast- und Broadcast-Rahmen und die in Figur 5 dargestellte Vorgehensweise nicht zwingend erforderlich ist und stattdessen andere Verfahrensschritte vorgesehen werden können.

62 Patentanspruch 1 beschränkt sich aber nicht darauf, andere Verfahrensschritte zuzulassen, sondern sieht eine konkrete Vorgehensweise zwingend vor, nämlich die Verwerfung von Unicast-Rahmen des ersten Typs und die Weiterleitung von allen anderen Rahmen. Diese Vorgehensweise ist in der Anmeldung nicht beschrieben.

63 2. Hinsichtlich der Hilfsanträge ergibt sich keine abweichende Beurteilung.

64 Die mit den Hilfsanträgen verteidigten Gegenstände gehen ebenfalls über den Inhalt der ursprünglich eingereichten Unterlagen hinaus, weil sie durchweg das Merkmal 5.4 umfassen.

65 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG und § 97 Abs. 1 ZPO.

Bacher

Hoffmann

Kober-Dehm

Rensen

Crummenerl
