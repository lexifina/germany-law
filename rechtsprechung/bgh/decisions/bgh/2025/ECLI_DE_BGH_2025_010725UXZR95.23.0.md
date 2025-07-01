---
ecli: "ECLI:DE:BGH:2025:010725UXZR95.23.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 95/23"
decided: "2025-07-01"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE615072025.xml"
neuris_doknr: "KORE615072025"
---

# Bundesgerichtshof, X ZR 95/23 vom 2025-07-01

## Tenor

Die Berufung gegen das Urteil des 5. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 17. Mai 2023 wird auf Kosten der Klägerin zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 944 065 (Streitpatents), das am 2. Dezember 2013 unter Inanspruchnahme einer US-amerikanischen Priorität vom 11. Januar 2013 angemeldet worden ist und den Austausch von Regeln in einem Paketnetz betrifft.

2 Patentanspruch 1, auf den zwölf weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A method comprising: at a network protection device (100)

receiving a first rule set;

receiving a second rule set;

preprocessing the first rule set and the second rule set;

configuring a plurality of processors (300, 302, 304) of the network protection device to process packets in accordance with the first rule set;

receiving packets;

processing, by at least two of the plurality of processors, a first portion of the packets in accordance with the first rule set;

signaling each of the at least two of the plurality of processors to process packets in accordance with the second rule set;

responsive to the signaling to process packets in accordance with the second rule set:

ceasing, by each of the at least two of the plurality of processors, processing of the packets;

caching, by each of the at least two of the plurality of processors, unprocessed packets;

reconfiguring each of the at least two of the plurality of processors to process packets in accordance with the second rule set; and signaling, by each of the at least two of the plurality of processors, completion of reconfiguration to process packets in accordance with the second rule set; and

responsive to receiving signaling that each of the at least two of the plurality of processors has completed reconfiguration to process packets in accordance with the second rule set, processing, by the at least two of the plurality of processors, the cached unprocessed packets.

3 Patentanspruch 14 stellt eine Vorrichtung unter Schutz, die geeignet ist, dieses Verfahren durchzuführen. Patentanspruch 15 schützt computerlesbare Medien mit Anweisungen zur Durchführung des Verfahrens.

4 Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglichen Anmeldung hinaus und sei nicht patentfähig. Die Beklagte hat das Streitpatent wie erteilt verteidigt.

5 Das Patentgericht hat die Klage abgewiesen. Gegen diese Entscheidung richtet sich die Berufung der Klägerin, mit der sie ihren bisherigen Antrag weiterverfolgt. Die Beklagte tritt dem Rechtsmittel entgegen und verteidigt das Streitpatent hilfsweise in einer geänderten Fassung.

## Entscheidungsgründe

6 Die zulässige Berufung ist unbegründet.

7 I. Das Streitpatent betrifft den Betrieb einer Netzwerkschutzvorrichtung.

8 1. Nach der Beschreibung des Streitpatents waren im Stand der Technik Vorrichtungen bekannt, die dem Schutz von Netzwerken dienen, in denen Datenpakete ausgetauscht werden. Als Beispiele werden Firewalls, Gateways, Switches, Router, Computer oder Server genannt.

9 Solche Vorrichtungen wendeten Regeln an, nach denen Datenpakete an der Netzwerkgrenze behandelt werden. Diese Regeln seien zu Regelgruppen zusammengefasst.

10 Unter bestimmten Voraussetzungen könne es angezeigt sein, von einer Regelgruppe zur anderen zu wechseln. Mit zunehmender Komplexität der Regelgruppen könne dies wegen der dafür aufzuwendenden Ressourcen dazu führen, dass der normale Datenverkehr behindert werde. Ferner könne es dazu kommen, dass Datenpakete noch nach den Regeln einer nicht mehr aktuellen Regelgruppe behandelt würden, was insbesondere im Fall eines bösartigen Angriffs auf das Netzwerk nachteilig sei.

11 2. Vor diesem Hintergrund kann das technische Problem darin gesehen werden, einen effektiven und sicheren Wechsel zwischen Regelgruppen zu ermöglichen.

12 3. Zur Lösung dieses Problems schlägt das Streitpatent im Anspruch 1 ein Verfahren vor, dessen Merkmale sich wie folgt gliedern lassen:

13 0

A method comprising: at a network protection device (100)

Verfahren an einer Netzwerkschutzvorrichtung, umfassend:

1

receiving a first rule set;

Empfangen einer ersten Regelgruppe;

2

receiving a second rule set;

Empfangen einer zweiten Regelgruppe;

3

preprocessing the first rule set and the second rule set;

Vorverarbeiten der ersten und der zweiten Regelgruppe;

4

configuring a plurality of processors (300, 302, 304) of the network protection device to process packets in accordance with the first rule set;

Konfigurieren einer Mehrzahl von Prozessoren (300, 302, 304) der Netzwerkschutzvorrichtung zum Verarbeiten von Paketen gemäß der ersten Regelgruppe;

5

receiving packets;

Empfangen von Paketen;

6

processing, by at least two of the plurality of processors, a first portion of the packets in accordance with the first rule set;

Verarbeiten eines ersten Teils der Pakete gemäß der ersten Regelgruppe durch mindestens zwei dieser Prozessoren;

7

signaling each of the at least two of the plurality of processors to process packets in accordance with the second rule set;

Signalisieren an jeden dieser Prozessoren, Pakete gemäß der zweiten Regelgruppe zu verarbeiten;

8

responsive to the signaling to process packets in accordance with the second rule set:

Verarbeiten von Paketen gemäß der zweiten Regelgruppe in Antwort auf dieses Signalisieren:

8.1

ceasing, by each of the at least two of the plurality of processors, processing of the packets;

Beenden der Verarbeitung der Pakete durch jeden dieser Prozessoren;

8.2

caching, by each of the at least two of the plurality of processors, unprocessed packets;

Zwischenspeichern von unverarbeiteten Paketen durch jeden dieser Prozessoren;

8.3

reconfiguring each of the at least two of the plurality of processors to process packets in accordance with the second rule set; and

Rekonfigurieren jedes dieser Prozessoren, um Pakete gemäß der zweiten Regelgruppe zu verarbeiten;

8.4

signaling, by each of the at least two of the plurality of processors, completion of reconfiguration to process packets in accordance with the second rule set; and

Signalisieren des Abschlusses der Rekonfiguration zum Verarbeiten von Paketen gemäß der zweiten Regelgruppe durch jeden dieser Prozessoren; und

9

responsive to receiving signaling that each of the at least two of the plurality of processors has completed reconfiguration to process packets in accordance with the second rule set, processing, by the at least two of the plurality of processors, the cached unprocessed packets.

Verarbeiten der zwischengespeicherten unverarbeiteten Pakete durch diese Prozessoren in Antwort auf das Empfangen eines Signals über den Abschluss der Rekonfiguration zum Verarbeiten von Paketen gemäß der zweiten Regelgruppe durch jeden dieser Prozessoren.

14 4. Einige Merkmale bedürfen der Erläuterung.

15 a) Eine Regelgruppe im Sinne der Merkmale 1 und 2 kann nach der Beschreibung Hunderte, Tausende oder gar Millionen einzelner Regeln umfassen (Abs. 26).

16 Patentanspruch 1 enthält insoweit keine näheren Festlegungen. Er lässt auch offen, wie diese Regelgruppen definiert und von welcher Stelle sie übermittelt werden.

17 b) Die Vorverarbeitung (preprocessing) im Sinne von Merkmal 3 dient nach der Beschreibung dem Zweck, die Anwendung der Richtlinien, die die Regelgruppen enthalten, zu optimieren.

18 Hierzu seien Technologien entwickelt worden, die den Zeitaufwand für die Anwendung großer Regelgruppen reduzierten. Eine solche Vorverarbeitung könne zum Beispiel durch Zusammenfassung oder Trennung von Regeln oder durch deren Reorganisation erfolgen (Abs. 20).

19 Da eine solche Vorverarbeitung unter Umständen erhebliche Ressourcen in Anspruch nehmen könne, sei es vorteilhaft, sie frühzeitig, etwa während des Setups durchzuführen (Abs. 21). Dies könne einen späteren Wechsel von der ersten zur zweiten Regelgruppe beschleunigen (Abs. 22).

20 c) Zur Verarbeitung der Datenpakete gemäß den jeweils geltenden Regelgruppen sieht Merkmal 4 mindestens zwei Prozessoren vor.

21 Entgegen der Auffassung der Berufungserwiderung ist damit nicht festgelegt, dass diese Prozessoren in dem Sinne parallel angeordnet sein müssen, dass jeder Prozessor die gesamte Regelgruppe vollständig prüft.

22 aa) Aus dem in der Beschreibung geschilderten Ausführungsbeispiel ergibt sich kein engeres Verständnis.

23 In den Figuren 3A bis 3F, von denen nachfolgend die Figur 3A exemplarisch wiedergegeben ist, sind die Prozessoren (300, 302, …, 304) allerdings über einen gemeinsamen Datenbus (120) miteinander verbunden.

24 Selbst wenn dies als Parallelschaltung verstanden werden könnte, ergibt sich daraus jedoch nicht zwingend die Schlussfolgerung, dass jeder Prozessor dasselbe Regelwerk verarbeitet.

25 (2) In den Erläuterungen zu diesem Ausführungsbeispiel wird eine Betriebssituation beschrieben, in der zwei Prozessoren zwei unterschiedliche Datenpakete untersuchen (Abs. 29).

26 Dies mag darauf hindeuten, dass jeder Prozessor das vollständige Regelwerk anwendet. Auch hieraus können jedoch keine Schlussfolgerungen für die Auslegung von Patentanspruch 1 gezogen werden. Die genannte Ausgestaltung hat dort keinen Niederschlag gefunden.

27 bb) Ob eine serielle Anordnung in dem Sinne, dass einzelne Prozessoren jeweils nur einen Teil der zu einer Gruppe gehörenden Regeln anwenden, eine hinreichende Verarbeitungsgeschwindigkeit ermöglicht, bedarf keiner abschließenden Beurteilung.

28 Selbst wenn diese Frage zu verneinen wäre, ergäben sich auch daraus keine Schlussfolgerungen für die Auslegung von Merkmal 4. Weder darin noch in den übrigen Merkmalen ist eine bestimmte Verarbeitungsgeschwindigkeit vorgegeben.

29 d) Die Merkmale 7 bis 9 beschäftigen sich mit einem Wechsel von einer Verarbeitung der Datenpakete nach der ersten Regelgruppe zu einer Verarbeitung nach der zweiten Regelgruppe.

30 aa) Ausgangspunkt ist das in Merkmal 7 vorgesehene Signal, die Pakete nunmehr nach der zweiten Regelgruppe zu verarbeiten.

31 Was den Anlass für ein solches Signal bildet und wo dieses Signal seinen Ausgang nimmt, legt der Anspruch nicht fest. Die Beschreibung benennt als Beispiele den Empfang einer entsprechenden Nachricht und das Erkennen von Netzwerkzuständen, die auf eine Netzwerkattacke hindeuten (Abs. 34).

32 Zwingend vorgegeben ist hingegen, dass dieses Signal an alle Prozessoren im Sinne von Merkmal 6 übermittelt wird.

33 bb) Der Empfang des Signals hat nach Merkmal 8.1 zur Folge, dass jeder Prozessor die Verarbeitung der Pakete nach den Regeln der ersten Gruppe beendet. Unverarbeitete Pakete werden nach Merkmal 8.2 in einen Zwischenspeicher abgelegt.

34 (1) Unverarbeitete Pakete in diesem Sinne sind solche, deren Verarbeitung durch den dafür vorgesehenen Prozessor noch nicht begonnen hat.

35 Pakete, die bei Eingang des Signals gerade verarbeitet werden, können wahlweise noch nach den Regeln der ersten Regelgruppe verarbeitet oder ebenfalls im Zwischenspeicher abgelegt werden (Abs. 31).

36 (2) Ausgestaltung und Anordnung des Zwischenspeichers sind nicht näher festgelegt.

37 In dem Ausführungsbeispiel gemäß den Figuren 3A bis 3F ist jedem Prozessor ein eigener Zwischenspeicher zugeordnet. Patentanspruch 1 ist hierauf jedoch nicht beschränkt.

38 (3) Aus dem Zusammenhang ergibt sich, dass der Zwischenspeicher geeignet sein muss, alle unverarbeiteten Pakete, die nach dem Eingang des in Merkmal 7 vorgesehenen Signals anfallen, vorzuhalten und nach erfolgter Umstellung auf die zweite Regelgruppe einer Verarbeitung nach diesen neuen Regeln zuzuführen.

39 cc) Der zweite Schritt besteht gemäß Merkmal 8.3 im Rekonfigurieren aller Prozessoren, um Pakete nach der zweiten Regelgruppe zu verarbeiten.

40 dd) Nach Merkmal 8.4 muss jeder Prozessor den Abschluss dieser Rekonfiguration signalisieren. Die Verarbeitung nach der zweiten Regelgruppe beginnt gemäß Merkmal 9, sobald jeder Prozessor ein Signal über den Abschluss der Rekonfiguration erhalten hat.

41 (1) Damit ist nicht zwingend vorgegeben, dass jeder Prozessor von jedem anderen Prozessor ein entsprechendes Signal erhalten muss. Vielmehr reicht es aus, wenn alle Prozessoren das in Merkmal 8.4 vorgesehene Signal an eine andere Komponente übermitteln und diese oder weitere Komponenten das in Merkmal 9 vorgesehene Signal an die Prozessoren übermitteln.

42 Dies steht in Einklang mit der Darstellung in den nachfolgend wiedergegebenen Figuren 3E und 3F.

43 Bei dieser Ausgestaltung melden die zur Verarbeitung der Pakete eingesetzten Prozessoren (300, 302, … 304) mit dem Signal "Done" jeweils den Abschluss ihrer Rekonfiguration an einen Verwaltungsprozessor (312). Dieser signalisiert den genannten Prozessoren mit dem Signal "Resume", dass die Verarbeitung der Pakete - nunmehr nach den Regeln der zweiten Gruppe - wiederaufgenommen werden soll (Abs. 32).

44 Das Streitpatent bezeichnet diese Vorgehensweise als Synchronisation. Sie soll gewährleisten, dass die Datenpakete nach den gleichen Regeln behandelt werden - unabhängig davon, welcher Prozessor sie verarbeitet (Abs. 33).

45 (2) Da Merkmal 8.4 und Merkmal 9 keine bestimmten Signalisierungsarten oder -wege vorgeben, ist jedoch nicht ausgeschlossen, dass die Signale auf andere Weise übertragen werden, als dies bei dem Ausführungsbeispiel geschieht.

46 Ausgehend von der Funktion der Merkmale genügt es, wenn jeder Prozessor signalisiert, dass er die Rekonfiguration abgeschlossen hat, und wenn jedem Prozessor ein Signal zur Wiederaufnahme der Paketverarbeitung übermittelt wird, sobald diese Voraussetzung erfüllt ist.

47 e) Patentanspruch 1 gibt nicht zwingend vor, dass alle Verfahrensschritte in der angeführten Reihenfolge absolviert werden.

48 aa) Die Beschreibung stellt ausdrücklich klar, dass die einzelnen Schritte auch in anderer Reihenfolge ausgeführt werden können (Abs. 38).

49 So ist etwa denkbar, dass die zweite Regelgruppe erst nach dem Vorverarbeiten der ersten Regelgruppe empfangen wird.

50 bb) Aus der Funktion einzelner Merkmale kann sich aber eine zwingende Reihenfolge ergeben.

51 Insbesondere darf die Verarbeitung von Paketen erst dann wiederaufgenommen werden, wenn das in Merkmal 8.4 vorgesehene Signal übermittelt worden ist. Dies ergibt sich aus der Festlegung in Merkmal 9, wonach die Verarbeitung in Reaktion auf das Empfangen dieses Signals beginnt.

52 f) Die mit den Patentansprüchen 14 und 15 geschützten Gegenstände werden durch den Rückbezug auf Anspruch 1 geprägt und unterliegen deshalb keiner abweichenden Beurteilung.

53 II. Das Patentgericht hat seine Entscheidung, soweit für das Berufungsverfahren von Interesse, im Wesentlichen wie folgt begründet:

54 Der Beitrag von Katayama et al. (A 10 Gb/s Firewall System for Network Security in Photonic Era, IEICE Transactions on Communications, Mai 2005, NK13) nehme den Gegenstand des Streitpatents nicht vorweg.

55 NK13 beschreibe ein System, das vernetzte Firewalls in Routern an einer Netzwerkgrenze (Border-Router) vorsehe. Das System basiere auf acht seriell verschalteten, rekonfigurierbaren Prozessoren des Typs DAPDNA 2, deren Struktur in einem Datenblatt von F. (NK19) beschrieben sei. Solche Prozessoren seien als Dual-Core-Prozessoren mit einem RISC-Core-DAP (Digital Application Processor) und einer parallelen Datenverarbeitung mittels 376 konfigurierbarer Verarbeitungselemente (Processing Elements, PE) in einer verteilten Netzwerkarchitektur (Distributed Network Architecture, DNA) ausgestattet.

56 NK13 sehe vor, dass ein Border-Router, der einen Angriff erkenne, die anderen Border-Router informiere und ihnen neue Regeln für die Verarbeitung von Datenpaketen sende. Diese Regeln würden in einem umschaltbaren Rekonfigurationsspeicher implementiert. Offenbart sei ferner ein Signal an die acht Prozessoren, das ein Umschalten zwischen den Rekonfigurationsspeicher bewirke und damit die Verwendung der zweiten Regelgruppe signalisiere.

57 NK13 offenbare jedoch hinsichtlich der Implementierung der neuen Regeln keine Details. Es bleibe offen, ob das Umschalten der Prozessoren synchron oder sequentiell erfolge, welche Signale verwendet würden und wie die zum Zeitpunkt des Wechsels in der Verarbeitung befindlichen Datenpakete behandelt würden. NK13 sehe einen Wechsel ohne Verlust von Paketdaten vor. Dies werde dahin beschrieben, dass die Paketverarbeitung innerhalb eines einzigen Taktzyklus unterbrochen und neu ankommende Pakete zwischengespeichert würden.

58 Merkmal 8.2 sei nur teilweise vorweggenommen, da aufgrund der seriellen Anordnung nicht jeder, sondern nur der erste der acht Prozessoren unverarbeitete Pakete zwischenspeichere. Es fehle zudem an einer Offenbarung der Merkmale 8.4 und 9. NK13 sei nicht zu entnehmen, dass die Prozessoren den Abschluss der Rekonfiguration signalisieren und in Reaktion auf ein entsprechendes Signal die zwischengespeicherten unverarbeiteten Pakete nach den neuen Regeln verarbeiten.

59 Aus dem Stand der Technik ergebe sich keine Anregung, das System so auszugestalten, dass sämtliche Prozessoren beim Eintreffen eines Signals nach Merkmal 7 unverarbeitete Pakete zwischenspeichern. Auch das Vorbringen der Klägerin dazu, dass der angestrebte Wechsel der Regelgruppe ohne Datenverlust eine Signalisierung gemäß den Merkmalen 8.4 und 9 nahelege, rechtfertige nicht den Schluss, der Gegenstand von Patentanspruch 1 habe nahegelegen. Im Stand der Technik, etwa aus der US-amerikanischen Patentanmeldung 2004/0015905 (NK17), seien alternative Möglichkeiten der Implementierung bekannt gewesen, die ohne Signalisierung auskämen.

60 III. Diese Beurteilung hält der Überprüfung im Berufungsrechtszug stand.

61 1. Die Erwägungen, mit denen das Patentgericht eine unzulässige Erweiterung verneint hat, greift die Berufung nicht an. Dieser Nichtigkeitsgrund ist daher in der Berufungsinstanz nicht mehr zu prüfen (vgl. BGH, Urteil vom 4. Februar 2010 - Xa ZR 4/07, GRUR 2010, 660 Rn. 14 - Glasflaschenanalysesystem).

62 2. Zu Recht hat das Patentgericht entschieden, dass NK13 den Gegenstand von Patentanspruch 1 nicht vollständig vorwegnimmt.

63 a) NK13 befasst sich mit dem Schutz von Rechnern vor Angriffen aus dem Internet.

64 aa) Als Beispiele für solche Angriffe führt NK13 Würmer und Denial-of-Service-Attacken an (S. 1914 f.). Herkömmliche Firewall-Systeme seien direkt vor dem Server angeordnet und könnten ein Eindringen schädlichen Verkehrs in das Netzwerk nicht verhindern (S. 1915 unter 3.1).

65 bb) Zur Abhilfe schlägt NK13 eine verteilte Architektur aus Firewalls vor, die sich an den Grenzen des Netzwerks befinden (S. 1915 unter 3.1). Eine solche Architektur ist exemplarisch in der nachfolgend wiedergegebenen Figur 1 dargestellt.

66 Als erforderliche Eigenschaften eines solchen Systems benennt NK13 eine Paketverarbeitungsleistung von 10 Gb/s, die Fähigkeit, Angriffe zu erkennen und bösartigen Verkehr zu verhindern, und die Möglichkeit, den Firewall-Algorithmus ohne Unterbrechung der Dienste (hitless) zu aktualisieren (S. 1914 rechts oben).

67 cc) Das in NK13 vorgeschlagene Verfahren zum Betrieb einer solchen Architektur umfasst vier Schritte (S. 1915 rechts):

68 Die einzelnen Firewalls sind an den Routern an der Grenze zwischen dem zu schützenden und einem potentiell gefährlichen Netzwerk angeordnet und so konfiguriert, dass sie Angriffe auf den Router erkennen und abwenden können.

69 Wenn ein Angriff erkannt worden ist, wird sofort eine Regel erstellt, um die bösartigen Pakete zu verwerfen.

70 Informationen über den Angriff (zum Beispiel Typ und Zeitpunkt) sowie die in Reaktion darauf erstellten Regeln werden an die anderen Firewalls weitergegeben.

71 Nach Erhalt dieser Information wird die neue Regel zur jeweiligen Filtertabelle hinzugefügt.

72 dd) Als wesentliche Anforderung für ein solches System bezeichnet NK13 die Möglichkeit, Filterregeln oder Algorithmen ohne Unterbrechung des Dienstes und ohne Verlust von Paketen (hitless) zu aktualisieren (S. 1917 unter 4.2).

73 Die Änderung mittels Softwarelösungen ermögliche allenfalls eine Verarbeitungsgeschwindigkeit von einigen hundert Megabit pro Sekunde. Um Flexibilität mit hoher Geschwindigkeit zu kombinieren, schlägt NK13 deshalb den Einsatz von Geräten vor, bei denen die Konfiguration durch Beschreiben eines Konfigurationsspeichers geändert werden kann.

74 Solche Geräte seien in zwei Varianten verfügbar:

75 Der Schalter-Typ weise zwei rekonfigurierbare Geräte mit jeweils eigenem Konfigurationsspeicher auf. Dadurch werde der erforderliche Umfang an Hardware verdoppelt.

76 Beim Puffer-Typ seien einem Gerät mehrere Rekonfigurationsspeicher zugeordnet, die dynamisch ausgetauscht werden könnten. Während der Rekonfiguration würden die Pakete in einem Puffer gespeichert.

77 ee) Bei dem in NK13 geschilderten Ausführungsbeispiel werden dynamisch rekonfigurierbare Prozessoren des Anbieters F. mit der Typenbezeichnung DAPDNA-2 eingesetzt.

78 Diese Prozessoren arbeiten mit einer Taktfrequenz von 166 MHz und umfassen jeweils vier dynamische Rekonfigurationsspeicher. Ein Austausch der Rekonfigurationsspeicher erfolgt innerhalb eines Taktes, also in ca. 6 Nanosekunden (S. 1917 unter 5).

79 Bei der vorgeschlagenen Implementierung werden acht dieser Prozessoren sowie ein Puffer zur Aktualisierung ohne Unterbrechung der Dienste eingesetzt. Diese Ausgestaltung ist in der nachfolgend wiedergegebenen Figur 8 schematisch dargestellt (S. 1918 links).

80 Das System kann Nutzdaten mit 10 Gb/s und Steuerdaten mit 5 Gb/s verarbeiten.

81 b) Ein solches System nimmt die Merkmale 1 bis 8.1 vorweg.

82 Soweit die Berufungserwiderung eine Offenbarung der Merkmale 4 und 6 in Zweifel zieht, beruht dies auf der Annahme, Patentanspruch 1 erfordere eine "parallele" Verarbeitung von Paketen. Diese Annahme trifft aus den oben dargestellten Gründen nicht zu.

83 c) Ein Zwischenspeichern von unverarbeiteten Paketen durch jeden dieser Prozessoren im Sinne von Merkmal 8.2 ist dagegen nicht unmittelbar und eindeutig offenbart.

84 aa) Entgegen der Auffassung der Berufung ergibt sich aus den oben wiedergegebenen Ausführungen, wonach während der Rekonfiguration alle Pakete in dem Puffer gespeichert werden, kein eindeutiger Hinweis darauf, dass jeder der acht Prozessoren Pakete in diesem Puffer ablegt.

85 Wie auch die Berufung nicht in Zweifel zieht, deutet die Darstellung in Figur 8 darauf hin, dass die Pakete die einzelnen Prozessoren sukzessiv durchlaufen und jeder Prozessor nur einen Teil des jeweils gültigen Regelwerks anwendet.

86 Von den in Figur 8 dargestellten Komponenten kommt allenfalls das als "Reconfiguration queue" bezeichnete Element als Puffer im Sinne von NK13 und damit als Zwischenspeicher im Sinne von Merkmal 8.2 in Betracht. Eine Verbindung, die es den Prozessoren ermöglicht, Pakete entgegen der Laufrichtung in dieser Warteschlange abzulegen, geht aus Figur 8 nicht hervor und wird auch im Text von NK13 nicht erwähnt. Dies spricht für die von der Berufungserwiderung geäußerte Annahme, dass die Datenpakete den Puffer auch während des normalen Betriebs durchlaufen und dass deshalb lediglich der erste Prozessor in der Lage ist, Pakete in diesem Puffer zwischenzuspeichern, indem er sie vorübergehend nicht daraus abruft.

87 bb) Ob das in Figur 8 nach dem letzten Prozessor im Datenstrom angeordnete Element ebenfalls eine Warteschlange bzw. einen Zwischenspeicher darstellt, bedarf keiner Entscheidung.

88 Selbst wenn die Frage zu bejahen wäre, ergäbe sich daraus allenfalls, dass der letzte Prozessor Pakete in diesem Speicher ablegen kann, nicht aber, dass auch die Prozessoren an der zweiten bis siebten Stelle diese Möglichkeit haben.

89 Zudem geht weder aus Figur 8 noch aus dem sonstigen Inhalt von NK13 hervor, dass Pakete, die in diesem Speicher vorgehalten werden, einer erneuten Verarbeitung durch die Prozessoren zugeführt werden können, wie dies nach Merkmal 9 erforderlich ist. Innerhalb des mit "Reconfiguration queue" bezeichneten Blocks ist zwar ein Pfeil vom achten zum ersten Prozessor eingezeichnet. Dabei handelt es sich aber, wie aus der Geschwindigkeitsangabe "5 Gb/s" hervorgeht, nur um Steuerdaten. Für die mit einer Geschwindigkeit von 10 Gb/s verarbeiteten Nutzdaten ist ein entsprechender Pfad nicht vorgesehen.

90 cc) Aus den technischen Daten des in NK13 vorgeschlagenen Prozessortyps ergeben sich keine weitergehenden Hinweise.

91 Dem Datenblatt zu diesem Prozessortyp (NK19) lässt sich entnehmen, dass die Prozessoren einen Speicher (On-Chip-RAM) umfassen, der grundsätzlich für beliebige Zwecke einsetzbar ist. Weder daraus noch aus NK13 geht jedoch hervor, dass der Speicher verwendet wird, um unverarbeitete Datenpakete während der Rekonfiguration zwischenzuspeichern.

92 d) Die Merkmale 8.4 und 9 sind in NK13 ebenfalls nicht unmittelbar und eindeutig offenbart.

93 NK13 enthält keine ausdrücklichen Angaben dazu, wie die Rekonfiguration der Prozessoren ausgelöst wird und was nach Abschluss der Rekonfiguration geschieht.

94 Entgegen der Auffassung der Berufung ist eine Signalisierung im Sinne von Merkmal 8.4 in NK13 auch nicht implizit offenbart.

95 In diesem Zusammenhang kann dahingestellt bleiben, ob eine solche Signalisierung für einen sinnvollen Betrieb des in NK13 vorgeschlagenen Systems erforderlich ist, wie dies die Berufung geltend macht. Selbst wenn dies zu bejahen wäre, ergäbe sich diese Erkenntnis nicht unmittelbar aus NK13, sondern allenfalls durch ergänzende Heranziehung von Fachwissen. Dies reicht für eine neuheitsschädliche Offenbarung nicht aus.

96 3. Entgegen der Auffassung der Berufung ist der Gegenstand von Patentanspruch 1 ausgehend von NK13 nicht nahegelegt.

97 a) Aus NK13 ergab sich keine Anregung, das System so auszugestalten, dass jeder Prozessor unverarbeitete Pakete zwischenspeichert, wie dies Merkmal 8.2 vorsieht.

98 aa) Auch bei einer sequentiellen Verarbeitung kann es allerdings sinnvoll sein, Pakete zwischenzuspeichern, die bereits von einem oder mehreren Prozessoren verarbeitet worden sind. Dies gilt insbesondere dann, wenn sichergestellt werden soll, dass Pakete, die beim Eintreffen des in Merkmal 7 vorgesehenen Signals bereits in Bearbeitung sind, aber noch nicht vollständig untersucht wurden, nach den neuen Regeln bearbeitet werden, wie dies auch die Beschreibung des Streitpatents als vorteilhaft bezeichnet.

99 Aus NK13 ergibt sich aber keine Anregung zu einer solchen Vorgehensweise.

100 Wie bereits oben aufgezeigt wurde, enthält NK13 - abgesehen von dem Hinweis auf die Speicherung von Paketen während der Rekonfiguration in einem vor dem ersten Prozessor angeordneten Puffer - keine näheren Angaben dazu, ob Pakete von den Prozessoren zwischengespeichert werden. Die Entgegenhaltung verhält sich auch nicht dazu, wie mit Paketen umzugehen ist, die beim Eintreffen einer neuen Regel bereits teilweise verarbeitet sind. Dies mag zwar Anlass gegeben haben, über mögliche Ausgestaltungen nachzudenken. Entgegen der Auffassung der Berufung ergibt sich aber selbst unter der Annahme, dass es insoweit nur die zwei Möglichkeiten gibt, die auch das Streitpatent anführt - die weitere Bearbeitung nach der ersten Regelgruppe oder eine Neubearbeitung nach der zweiten Regelgruppe - nicht, dass beide Möglichkeiten gleichermaßen nahelagen.

101 Wie bereits oben dargelegt wurde, deutet die Darstellung in Figur 8 darauf hin, dass eine Rückführung von teilweise bearbeiteten Paketen in die Eingangswarteschlange nicht vorgesehen ist.

102 Die in NK13 verwendeten Prozessoren verfügen zwar über einen Speicher, der geeignet ist, ankommende Daten zu puffern. Ein solcher Speicher mag auch die Eignung aufweisen, unverarbeitete Datenpakete zwischenzuspeichern. Aus dem Stand der Technik ergab sich jedoch keine Anregung, über die Pufferung ankommender Pakete in dem vor dem ersten Prozessor angeordneten Puffer hinaus vorzusehen, dass jeder Prozessor diesen Speicher als zusätzlichen Puffer für unverarbeitete Pakete nutzt.

103 Gegen eine solche Vorgehensweise sprach zudem, dass einzelne Pakete dann teils nach dem alten und teils nach dem neuen Regelsatz geprüft würden. Dies mag sich zwar durch geeignete Zuordnung der Regeln zu den einzelnen Prozessoren vermeiden lassen. Auch insoweit ergeben sich aus NK13 aber keine Hinweise.

104 bb) Aus der US-amerikanischen Patentanmeldung 2011/0055916 (NK8) ergibt sich entgegen der Auffassung der Berufung keine weitergehende Anregung.

105 (1) NK8 beschreibt eine Kombination von serieller und paralleler Anordnung von Prozessoren zur beschleunigten Verarbeitung einer Gesamtheit von Regeln einer Firewall.

106 NK8 führt aus, im Stand der Technik sei vorgeschlagen worden, die Regeln in funktionell unabhängige Listen mit voneinander abhängigen Regeln aufzuteilen, um eine parallele Prüfung gegen mehrere Listen zu ermöglichen. Bei einer sehr großen Anzahl von Regeln würden die damit zu erzielenden Vorteile aber durch andere Faktoren zunichtegemacht (Abs. 3).

107 Zur Verbesserung schlägt NK8 unter anderem vor, nach disjunkten Regeln zu suchen, d.h. Regeln, deren Reihenfolge geändert werden kann, ohne dass die Integrität der Firewall-Richtlinie beeinträchtigt wird (Abs. 7). Ferner wird eine Kombination von serieller und paralleler Verarbeitung vorgeschlagen (Abs. 22).

108 Ein Ausführungsbeispiel ist in der nachfolgend wiedergegebenen Figur 3 schematisch dargestellt.

109 Die Regeln zur Prüfung der Datenpakete sind in drei Teilmengen (A, B, C) eingeteilt. Die Regeln innerhalb dieser Teilmengen sind jeweils disjunkt. Die Regeln jeder Teilmenge sind aber von denjenigen der jeweils vorangehenden Teilmenge abhängig (Abs. 22). Die Regeln der ersten und der dritten Teilmenge (A, C) werden von jeweils einem Prozessor (300, 306) verarbeitet, die Regeln der zweiten Teilmenge (B) parallel von zwei Prozessoren (302, 304) (Abs. 23).

110 Der Wechsel von einer ersten zu einer zweiten Regelgruppe und die Frage, wie bei einem solchen Wechsel mit bislang unverarbeiteten Paketen umzugehen sei, werden in NK8 nicht angesprochen.

111 (2) Daraus ergab sich ausgehend von NK13 jedenfalls deshalb keine Anregung in Richtung auf Merkmal 8.2, weil kein Anlass bestand, einzelne der in NK13 vorgeschlagenen rekonfigurierbaren Prozessoren zur parallelen Verarbeitung von Paketen einzusetzen.

112 Nach den Feststellungen des Patentgerichts ermöglichen die in NK13 eingesetzten Prozessoren einen Datendurchsatz von 16 GB/s, also 60 % mehr als die dort angestrebte Geschwindigkeit von 10 GB/s. Hieraus hat das Patentgericht zutreffend die Schlussfolgerung gezogen, dass kein Anlass bestand, den Durchsatz des Systems durch abweichende Anordnung der Prozessoren weiter zu verbessern.

113 Wie die Berufung im Ansatz zu Recht geltend macht, mag nicht auszuschließen sein, dass es Einsatzzwecke gab, die einen Datendurchsatz von mehr als 10 GB/s oder sogar mehr als 16 GB/s erfordern. Wie die Berufungserwiderung zutreffend vorträgt, ergeben sich aus dem Datenblatt des in NK13 vorgeschlagenen Prozessortyps (NK19) aber keine hinreichenden Hinweise darauf, dass eine Steigerung über 16 GB/s hinaus durch Parallelisierung möglich ist.

114 In den Erläuterungen zu der hierfür allein in Frage kommenden Schnittstelle (DNA Direct I/O) wird ausgeführt, diese ermögliche die Verbindung mehrerer Prozessoren und deren Integration in ein Gesamtsystem mit einem Durchsatz von 16 GB/s (S. 2 Abs. 3). Möglichkeiten zu einer weiteren Steigerung des Gesamtdurchsatzes werden nicht erwähnt.

115 Aus dem ergänzenden Hinweis, die Schnittstelle könne auch zur direkten Kommunikation mit anderen externen Geräten eingesetzt werden (S. 2 Abs. 4), ergeben sich ausgehend von NK13 keine weitergehenden Anregungen. NK13 hebt hervor, dass gerade die dort vorgeschlagenen Prozessoren erforderlich sind, um den hohen Anforderungen an die Verarbeitungsgeschwindigkeit zu genügen. Angesichts dessen bestand auch im Lichte von NK8 kein Anlass, diese Prozessoren mit parallel arbeitenden anderen Prozessoren zu kombinieren.

116 b) Vor diesem Hintergrund kann offenbleiben, ob sich ausgehend von NK13 eine Anregung ergab, den Abschluss der Rekonfiguration in der in Merkmal 8.4 vorgesehenen Weise zu signalisieren und erst in Antwort auf ein solches Signal die Verarbeitung von Paketen wiederaufzunehmen, wie dies Merkmal 9 vorsieht.

117 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG und § 97 Abs. 1 ZPO.

Bacher

Hoffmann

Deichfuß

Kober-Dehm

Rensen
