---
ecli: "ECLI:DE:BGH:2026:210526UXZR47.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 47/24"
decided: "2026-05-21"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE616132026.xml"
neuris_doknr: "KORE616132026"
---

# Bundesgerichtshof, X ZR 47/24 vom 2026-05-21

## Tenor

Die Berufung gegen das Urteil des 2. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 7. März 2024 wird auf Kosten der Beklagten zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 454 735 (Streitpatents), das am 1. Juli 2010 unter Inanspruchnahme zweier US-amerikanischer Prioritäten vom 16. Juli 2009 und vom 15. April 2010 angemeldet worden ist.

2 Patentanspruch 1, auf den elf Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A memory module (402, 402') operable in a computer system with a memory controller (420), the computer system including a set of control signal lines (440, 440') and first number of data signal lines (450, 450') between the memory module (402, 402') and the memory controller, the first number of data signal lines (450, 450') including a second number of sets of data signal lines (450, 450'), each set of data signal lines (450, 450') for conducting a 8-bit section of each data signal between the memory module (402, 402') and the memory controller, the memory module (402, 402') comprising:

a module board (410, 410') configured to be coupled to the memory controller (420) via the set of control signal lines (440, 440') and the first number of data signal lines (450, 450'), the module board (410, 410') being mountable in a module slot of the computer system and having an edge connector comprising a plurality of electrical contacts which are positioned on an edge of the module board (410, 410') and are positioned to be releasably coupled to corresponding contacts of a computer system socket;

a plurality of memory devices (412, 412'), coupled to the module board (410, 410') and arranged in multiple ranks, each rank of the multiple ranks having a bit width equal to a bit width of the memory module (402, 402');

a module controller (430, 430') coupled to the module board (410, 410') and configured to receive input control signals for a read or write operation from the memory controller (420) via the set of control signal lines (440, 440') and to output first module control signals based on the input control signals, the read or write operation being targeted at a specific one of the multiple ranks; and

second number of load-reducing circuits (416, 416') coupled to the module board (410, 410') and configured to receive the first module control signals, each respective one of the second number of load-reducing circuits (416, 416') being coupled to a respective set of the second number of sets of data signal lines (450, 450') and to at least one respective memory device (412, 412') in each of the multiple ranks, the second number of load-reducing circuits (416, 416') being disposed on the module board (410, 410') at respective positions corresponding to respective sets of the second number of sets of data signal lines (450, 450'); and

wherein the each respective one of the load-reducing circuits (416, 416') includes data paths and logic (502) controlling the data paths in response to the first module control signals so that the second number of load-reducing circuits (416, 416') actively drive a data signal corresponding to the read or write operation between the specific one of the multiple ranks on the memory module (402, 402') and the memory controller, and wherein the first module control signals indicate a direction of data flow.

3 Patentanspruch 13, auf den zwei Ansprüche zurückbezogen sind, stellt ein Verfahren zum Betreiben eines entsprechenden Speichermoduls unter Schutz.

4 Die Klägerinnen haben geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Die Beklagte hat das Streitpatent in der erteilten Fassung und hilfsweise in vierzehn geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt. Dagegen wendet sich die Beklagte mit der Berufung, mit der sie mit Ausnahme des Hilfsantrags 12 ihre erstinstanzlichen Anträge weiterverfolgt und das Streitpatent zusätzlich mit drei weiteren Hilfsanträgen verteidigt. Die Klägerinnen treten dem Rechtsmittel entgegen.

## Entscheidungsgründe

6 Die zulässige Berufung ist unbegründet.

7 I. Das Streitpatent betrifft ein Speichermodul und ein Verfahren zum Betreiben eines Speichermoduls in einem Computersystem.

8 1. Nach der Beschreibung des Streitpatents werden Speicherplatinen in einem Speichersteckplatz eines Computersystems befestigt und vom Computerprozessor angesprochen.

9 Speicherplatinen umfassten in der Regel ein oder mehrere Speichermodule, die jeweils eine Vielzahl von Speichervorrichtungen (wie dynamic random access memory, DRAM oder synchronous dynamic random access memory, SDRAM) in einer Konfiguration von Zeilen, Spalten und Bänken aufwiesen. Die Speichervorrichtungen seien als Reihen (ranks) oder Zeilen (rows of memory) angeordnet. Jede Speicherreihe weise eine Bitbreite (bit width) auf. So könne jede Reihe 64 Bit breit sein und damit als eine x64- oder 64-Organisation beschrieben werden (Abs. 3, 4).

10 Die Reihen würden durch Steuersignale ausgewählt oder aktiviert, welche Reihenauswahlsignale (rank-select signals) umfassen könnten (auch als chip-select signals bezeichnet). Die meisten Computer- und Serversysteme unterstützten nur eine begrenzte Anzahl von Reihen (Abs. 6).

11 Der physikalisch adressierbare Speicherplatz sei begrenzt. Er werde durch die Anzahl der Adressbits oder ausgewählten Chips definiert. Das führe zu Problemen, wenn die Anwendung eines Benutzers einen größeren adressierbaren Speicherplatz erfordere als der Speicherplatz, für den das aktuelle elektronische System ausgelegt sei (Abs. 7).

12 Die physikalische Größe eines Speichermoduls könne die Speicherdichte des Moduls begrenzen. Eine Erhöhung der Speicherdichte führe in der Regel zu einer höheren Verlustleistung und verlangsame die Betriebsgeschwindigkeit (Abs. 10, 11).

13 Die Streitpatentschrift gibt an, die nachfolgend in der kolorierten Fassung des Patentgerichts wiedergegebene Figur 2A veranschauliche einen aus dem Stand der Technik bekannten Ansatz zur Erhöhung der Anzahl an Speichervorrichtungen.

14 Bei dem gezeigten Speichersubsystem (200) umfasse jede Reihe des Speichermoduls (210) mehrere Speichervorrichtungen (212). Ein Register (230) empfange Steuerleitungen (240) von der Systemspeichersteuerung (Speichercontroller, 220) und sei über Steuerleitungen (242) mit den Speichervorrichtungen (212) jeder Reihe des Speichermoduls verbunden. Jede Datenleitung einer Anordnung von Datenleitungen (250) stelle eine Verbindung des Speichercontrollers (220) mit den entsprechenden Speichervorrichtungen (212) her. Dies führe dazu, dass der Speichercontroller während einer Schreiboperation alle Speichervorrichtungen als seine Last über die Datenleitungen (250) sehe und dass während einer Leseoperation jede Speichervorrichtung mehrere andere Speichervorrichtungen sowie den Speichercontroller als ihre Last über die Datenleitungen sehe (Abs. 22).

15 In einer sogenannten Fly-by-Konfiguration würden Steuersignale entlang der Steuerleitungen (242) von dem Register (230) zu den Speichervorrichtungen (212) eines gegebenen Ranges gesendet. Dabei erreiche ein Steuersignal die Speichervorrichtung mit der längsten Steuerleitung deutlich später als dasselbe Steuersignal die Speichervorrichtung mit der kürzesten Steuerleitung. Diese unter Umständen über einen Taktzyklus hinausgehenden Zeitunterschiede begrenzten die Betriebsgeschwindigkeit und die Leistung des Speichermoduls. Die großen Lasten hätten außerdem langsamere Taktgeschwindigkeiten zur Folge (Abs. 24, 25).

16 Die Verwendung eines Speicherpuffers zur Handhabung der Steuer- und Datensignale sei ebenfalls mit erheblichen Nachteilen verbunden (Abs. 26, 27).

17 2. Das Patentgericht hat vor diesem Hintergrund das technische Problem des Streitpatents zutreffend darin gesehen, ein Speichermodul mit hoher Speicherdichte und Zugriffsgeschwindigkeit bereitzustellen.

18 3. Zur Lösung schlägt das Streitpatent in Patentanspruch 1 ein Speichermodul vor, dessen Merkmale sich wie folgt gliedern lassen:

19 0

A memory module (402, 402') operable in a computer system with a memory controller (420),

Ein Speichermodul (402, 402'), das ineinem Computersystem mit einem Speichercontroller (420) betriebenwerden kann,

1

the computer system including a set of control signal lines (440, 440')and first number of data signal lines(450, 450') between the memorymodule (402, 402') and the memory controller,

das Computersystem umfasst einenSatz von Steuersignalleitungen (440,440') und eine erste Anzahl von Datensignalleitungen (450, 450') zwischen dem Speichermodul (402, 402') und dem Speichercontroller,

1.1

the first number of data signal lines(450, 450') including a second number of sets of data signal lines(450, 450'),

die erste Anzahl von Datensignalleitungen(450, 450') umfasst eine zweite Anzahlvon Sätzen von Datensignalleitungen(450, 450'),

1.2

each set of data signal lines (450,450') for conducting an 8-bit sectionof each data signal between the memory module (402, 402') and the memory controller,

jeder Satz von Datensignalleitungen (450, 450') dient dem Leiten eines 8-Bit Abschnitts von jedem Datensignalzwischen dem Speichermodul (402, 402') und dem Speichercontroller,

2

the memory module (402, 402') comprising:

das Speichermodul (402, 402') umfasst:

2.1

a module board (410, 410') configured to be coupled to thememory controller (420) via theset of control signal lines (440,440') and the first number of data signal lines (450, 450'),

eine Modul-Leiterplatte (410, 410'),die dazu konfiguriert ist, mit dem Speichercontroller (420) über den Satz von Steuersignalleitungen (440,440') und die erste Anzahl von Datensignalleitungen (450, 450')gekoppelt zu sein,

2.2

the module board (410, 410') beingmountable in a module slot of the computer system and having an edge connector comprising a pluralityof electrical contacts which are positioned on an edge of the moduleboard (410, 410') and are positionedto be releasably coupled to corresponding contacts of a computersystem socket;

wobei die Modul-Leiterplatte (410, 410')in einem Modulschlitz des Computersystems anbringbar ist und einen Randstecker hat, der eine Vielzahl von elektrischen Kontaktenaufweist, die an einem Rand der Modul-Leiterplatte (410, 410') positioniertsind und dazu positioniert sind, lösbar mit korrespondierenden Kontakten eines Computersystemsockels gekoppelt zu werden;

2.3

a plurality of memory devices (412, 412') coupled to the moduleboard (410, 410') and arranged in multiple ranks,

eine Vielzahl von Speichervorrichtungen (412, 412'), die mit der Modul Leiterplatte(410, 410') gekoppelt sind und in mehreren Reihen angeordnet sind,

2.3.1

each rank of the multiple ranks having a bit width equal to a bitwidth of the memory module (402, 402');

wobei jede Reihe von den mehreren Reihen eine Bitbreite hat, die gleichgroß wie eine Bitbreite des Speichermoduls(402, 402') ist;

2.4

a module controller (430, 430') coupled to the module board (410, 410') and configured

einen Modulcontroller (430, 430'), der mit der Modul-Leiterplatte (410, 410') gekoppelt ist und dazu konfiguriert ist,

2.4.1

to receive input control signals for a read or write operation from the memory controller (420) via the set of control signal lines (440, 440') and

Eingangssteuersignale für eine Lese- oder Schreiboperation von dem Speichercontroller (420) über den Satz von Steuersignalleitungen (440, 440') zu empfangen, und

2.4.2

to output first module control signals based on the input control signals,

erste Modulsteuersignale auf der Basis der Eingangssteuersignale auszugeben,

2.4.3

the read or write operation being targeted at a specific one of the multiple ranks;

wobei die Lese- oder Schreiboperation auf eine bestimmte von den mehreren Reihen abgezielt ist;

2.5

and second number of load-reducingcircuits (416, 416') coupled to the module board (410, 410') and configured to receive the first module control signals,

und eine zweite Anzahl von lastredu-zierenden Schaltungen (416, 416'), die mit der Modul-Leiterplatte (410, 410') gekoppelt sind und dazu konfi-guriert sind, die ersten Modulsteuersignale zu empfangen, wobei

2.5.1

each respective one of the second number of load-reducing circuits (416, 416') being coupled to a respective set of the second number of sets of data signal lines (450, 450') and

wobei jede dieser lastreduzierenden Schaltungen (416, 416') mit einem jeweiligen Satz von der zweiten Anzahl von Sätzen von Datensignalleitungen (450, 450') und

2.5.2

to at least one respective memory device (412, 412') in each of the multiple ranks,

mit wenigstens einer jeweiligen Speichervorrichtung (412, 412') in jeder von den mehreren Reihen gekoppelt ist,

2.5.3

the second number of load-reducing circuits (416, 416') being disposed on the module board (410, 410') at respective positions corresponding to respective sets of the second number of sets of data signal lines (450, 450'); and

wobei die zweite Anzahl von lastreduzierenden Schaltungen (416, 416') auf der Modul-Leiterplatte (410, 410') an jeweiligen Positionen angeordnet ist, die jeweiligen Sätzen von der zweiten Anzahl von Sätzen von Datensignalleitungen (450, 450') entsprechen; und

2.5.4

wherein the each respective one of the load-reducing circuits (416, 416') includes data paths and logic (502) controlling the data paths in response to the first module control signals

wobei jede dieser jeweiligen lastreduzierenden Schaltungen (416, 416') Datenpfade und eine Logik (502)zum Steuern der Datenpfade in Reaktion auf die ersten Modulsteuersignale umfasst,

2.5.4.1

so that the second number of load-reducing circuits (416, 416') actively drive a data signal corresponding to the read or write operation between the specific one of the multiple ranks on the memory module (402, 402') and the memory controller, and

so dass die zweite Anzahl von lastreduzierenden Schaltungen (416, 416') aktiv ein Datensignal, das der Lese- oder Schreiboperation entspricht, zwischen der bestimmten einen von den mehreren Reihen auf dem Speichermodul (402, 402') und dem Speichercontroller treibt, und

2.5.4.1

wherein the first module control signals indicate a direction of data flow.

wobei die ersten Modulsteuersignale eine Richtung des Datenflusses angeben.

20 Patentanspruch 13 stellt ein Verfahren zum Betreiben eines solchen Speichermoduls unter Schutz.

21 4. Einige Merkmale bedürfen der Erläuterung.

22 a) Das Speichermodul ist Teil eines im Übrigen nicht beanspruchten Computersystems. Der zum Betreiben des Speichermoduls vorgesehene Speichercontroller ist Bestandteil des Computersystems und über ebenfalls dem Computersystem zugeordnete, jeweils als erste Anzahl zusammengefasste Steuer- und Datensignalleitungen mit dem Speichermodul verbunden (Merkmale 0, 1).

23 b) Merkmal 1.1 ist zu entnehmen, dass die erste Anzahl von Datensignalleitungen in Sätze (Gruppen) von Datensignalleitungen unterteilt ist, so dass die Sätze eine von der ersten Anzahl eingeschlossene zweite Anzahl darstellen.

24 Jeder Satz weist nach Merkmal 1.2 die Eignung auf, einen Abschnitt von acht Bit eines Datensignals zwischen Speichercontroller und Speichermodul zu leiten. Nach den zutreffenden Ausführungen des Patentgerichts sind damit die Bitbreite bzw. bitbreite Abschnitte angesprochen, also die Möglichkeit zur parallelen Datenübertragung. Das Speichermodul nach dem nachfolgend wiedergegebenen Ausführungsbeispiel gemäß Figur 3C (kolorierte Fassung des Patentgerichts) weist danach eine zweite Anzahl von neun Sätzen Datensignalleitungen (450') und bei acht Leitungen pro Satz damit als erste Anzahl insgesamt 72 Datensignalleitungen auf.

25 c) Die nach den Merkmalen 2.1 und 2.2 vorgesehene Modul-Leiterplatte ist Teil des Speichermoduls. Ihre Konfiguration ermöglicht die Kopplung des Speichermoduls mit dem Speichercontroller über die Steuer- und Datensignalleitungen. Die Modulbauweise mit Randstecker macht die lösbare Kopplung mit korrespondierenden Kontakten in einem Sockel des Computersystems möglich.

26 d) Nach Merkmal 2.3 ist mit der Modul-Leiterplatte eine Vielzahl von Speichervorrichtungen (412, 412') gekoppelt. Dabei sind, wie aus den nachfolgend wiedergegebenen Figuren 3A (kolorierte und beschriftete Fassung des Patentgerichts) und 3B ersichtlich, die Speichervorrichtungen in mehreren Reihen (ranks) angeordnet (vertikale Reihen A, B, C und D).

27 Merkmal 2.3.1 gibt vor, dass jede Reihe eine Bitbreite hat, die gleich der Bitbreite des Speichermoduls ist. Damit ist sichergestellt, dass bei jedem Zugriff auf eine Reihe (rank) die volle Bitbreite des Moduls genutzt werden kann. Hat das Speichermodul entsprechend der obigen Figur 3C eine (Gesamt-)Bitbreite von 72, folgt aus Merkmal 2.3.1, dass jede Reihe eine Bitbreite von 72 aufweist.

28 e) Dem Speichermodul ist in gekoppelter Form ein Modulcontroller (430) zugeordnet.

29 aa) Der Modulcontroller empfängt über die Steuersignalleitungen (440, 440') Eingangssteuersignale, die der Speichercontroller für eine die Speichervorrichtungen betreffende Lese- oder Schreiboperation ausgegeben hat (Merkmal 2.4.1). Daraus ergibt sich, dass der Speichercontroller für eine Lese- oder Schreiboperation die Speichervorrichtungsreihen nicht selbst ansteuert, sondern die Steuersignale dem Modulcontroller als zwischengeschaltete Instanz übermittelt, der für deren Umsetzung zu sorgen hat. Der Modulcontroller erzeugt und gibt hierzu eigene (erste) Modulsteuersignale auf der Basis der Eingangssteuersignale des Speichercontrollers aus (Merkmal 2.4.2).

30 bb) Die Lese- oder Schreiboperation, die mit den Steuersignalen angestoßen werden soll, wird in Merkmal 2.4.3 dahingehend näher umschrieben, dass sie auf eine bestimmte von den mehreren Reihen abzielt.

31 (1) Dies gibt nicht zwingend vor, dass die Lese- oder Schreiboperation nur auf eine einzelne Reihe von Speichervorrichtungen zielt, vielmehr kann sie auch auf mehrere Reihen zielen. So werden in der Beschreibung Beispiele erläutert, wonach die Daten in zwei Reihen geschrieben werden sollen (Abs. 38, Sp. 13 Z. 2 ff., Abs. 45, Sp. 17 Z. 15 ff., Abs. 53, Sp. 19 Z. 45 ff.). Ausgeschlossen ist jedoch, dass die Schreiboperation auf sämtliche Reihen des Speichermoduls zielt.

32 (2) Merkmal 2.4.3 ist zu entnehmen, dass die Eingangs- und Modulsteuersignale nicht nur eine allgemeine Vorgabe für eine Lese- oder Schreiboperation beinhalten, sondern dass die Operation von vornherein auf einen bestimmten Speicher- bzw. Leseort ausgerichtet ist. Die Daten sollen danach in eine bestimmte Reihe eingeschrieben bzw. von dieser ausgelesen werden.

33 Merkmal 2.4.3 macht keine näheren Vorgaben dazu, in welcher Weise oder Form die Eingangssteuersignale die Basis für die auszugebenden Modulsteuersignale darstellen. Insbesondere ist dem Anspruchswortlaut nicht zu entnehmen, dass der Modulcontroller das Eingangssteuersignal in keiner Weise umwandeln, abändern oder ergänzen darf.

34 Die Streitpatentschrift nennt verschiedene Beispiele für Steuersignale des Speichercontrollers (bank address signals, row address signals, column address signals, address strobe signals, and rank-address or chip select signals, Abs. 36). Danach nimmt der Speichercontroller zwar aus seiner Sicht eine Adressierung vor. Der Modulcontroller darf zu diesen Signalen jedoch zusätzliche Chipauswahlsignale oder Ausgangsfreigabesignale erzeugen (Abs. 36: "The control circuit 430, 430' may produce additional chip-select signals or output enable signals based on address decoding."). Das Patentgericht hat hieraus und aus dem Verweis auf die US-amerikanische Patentschrift 7 532 537 (Sp. 16, Z. 45 bis Sp. 17 Z. 76, ZP11) zutreffend hergeleitet, dass die Modulsteuersignale auch dann auf den Eingangssteuersignalen basieren, wenn der Modulcontroller die Adresscodierung umwandelt und ein weiteres Chip-Select-Signal erzeugt, etwa wenn die Adresscodierung des Speichercontrollers von einer größeren Speicherkapazität (z.B. 1 GBit) ausgeht, tatsächlich aber nur geringere Kapazitäten vorhanden sind (z.B. 512 Mbit).

35 Soweit in der Patentbeschreibung bekannte Verfahren zur Vergrößerung des Speicherplatzes basierend auf einem Adressdecodierungsschema oder die Kombination von Chip-Select-Signalen mit einem Adresssignal als nachteilig kritisiert werden (Abs. 17, 18), geht es um erhöhte Lasten durch zusätzliche Speicherplätze bei Vorrichtungen, die - anders als nach der Lehre des Streitpatents - keine zusätzlichen lastreduzierenden Schaltungen aufweisen. Einschränkende Vorgaben zu der Erzeugung der Modulsteuersignale sind damit nicht verbunden.

36 Entgegen der Ansicht der Berufung ergibt sich keine andere Beurteilung aus dem Umstand, dass Patentanspruch 1 eine Anordnung in mehreren Reihen (Merkmal 2.3) vorsieht und nicht von durch den Modulcontroller steuerbaren Unterreihen spricht. Patentanspruch 1 sieht eine derartige Differenzierung, die aus den unterschiedlichen Blickwinkeln von Speichercontroller und Modulcontroller im Falle der oben genannten Umwandlung der Adresscodierung resultiert, nicht vor. An dem physischen Vorhandensein mehrerer Reihen ändert dies nichts.

37 f) Schließlich verfügt das Speichermodul nach Merkmal 2.5 über eine (zweite) Anzahl von lastreduzierenden Schaltungen (416). Sie sind mit der Modul-Leiterplatte gekoppelt und konfiguriert, die ausgegebenen (ersten) Modulsteuersignale zu empfangen. Dies erfolgt in den Beispielen nach den obigen Figuren 3A und 3B über die Modulcontroller (430, 430') und lastreduzierende Schaltungen (416, 416') verbindende Leitungen (432, 432').

38 aa) Merkmal 2.5.1 enthält Vorgaben zur Zuordnung der lastreduzierenden Schaltungen zu den Datensignalleitungen. Jede lastreduzierende Schaltung ist danach mit einem Satz von Datensignalleitungen der zweiten Anzahl von Sätzen gekoppelt. In dem Beispiel nach der obigen Figur 3C entspricht die zweite Anzahl nach Merkmal 2.5.1 der zweiten Anzahl nach Merkmal 1.1.

39 bb) Merkmal 2.5.3 ergänzt die vorgenannte Zuordnung um eine räumlich-körperliche Vorgabe. Danach sind die jeweiligen lastreduzierenden Schaltungen so angeordnet, dass ihre jeweilige Position dem jeweiligen Satz von Datensignalleitungen entspricht, mit dem eine Kopplung erfolgt. Damit kann die zweite Anzahl von lastreduzierenden Schaltungen in Entsprechung zu den zweiten Sätzen von Datensignalleitungen über die gesamte Breite des Moduls verteilt werden.

40 cc) Merkmal 2.5.2 hat die Kopplung der lastreduzierenden Schaltungen mit den Speichervorrichtungen zum Gegenstand. Jede lastreduzierende Schaltung ist mit wenigstens einer jeweiligen Speichervorrichtung in jeder von den mehreren Reihen gekoppelt. Danach reicht es nicht aus, dass eine lastreduzierende Schaltung mit (mindestens) einer Speichervorrichtung einer Reihe gekoppelt ist. Vielmehr muss für jede der Reihen eine solche Kopplung vorliegen.

41 g) Merkmal 2.5.4 macht Vorgaben zum internen Aufbau der lastreduzierenden Schaltungen (416). Danach weisen sie jeweils Datenpfade und eine Logik zum Steuern der Datenpfade auf. Die Steuerung geschieht in Reaktion auf die von den lastreduzierenden Schaltungen empfangenen (ersten) Modulsteuersignale.

42 h) Merkmal 2.5.4.1 umschreibt das in Reaktion auf das Modulsteuersignal erfolgende Steuern der Datenpfade durch die Logik (502) näher.

43 Danach wird ein Datensignal für eine Lese- oder Schreiboperation aktiv getrieben. Dies geschieht zwischen den Komponenten, mit denen die lastreduzierenden Schaltungen gekoppelt sind, nämlich der jeweilig einer Schaltung zugeordneten Reihe auf dem Speichermodul einerseits und dem Speichercontroller andererseits.

44 Dadurch kommt den Schaltungen eine lastreduzierende Funktion zu. Der Speichercontroller sieht nicht die Vielzahl an Speichervorrichtungen, sondern nur noch die das Datensignal aktiv treibenden lastreduzierenden Schaltungen mit Schreibpuffer (503) und Lesepuffer (509) als seine Last.

45 i) Die Merkmale 2.5.4 und 2.5.4.1 stehen in einem unmittelbaren technischen Zusammenhang mit Merkmal 2.4.3, nach dem die Lese- oder Schreiboperation auf eine bestimmte von den mehreren Reihen abgezielt ist, die Daten also in eine bestimmte Reihe eingeschrieben bzw. von dieser ausgelesen werden sollen.

46 Der Modulcontroller leitet diese Information mit dem Modulsteuersignal zu den lastreduzierenden Schaltungen. In Reaktion darauf setzt die Logik (502) der lastreduzierenden Schaltungen die Vorgabe mit ihren Datenpfaden um und treibt den Vorgang aktiv mit einem der vorbestimmten Lese- oder Schreiboperation entsprechenden Datensignal.

47 aa) In der Patentbeschreibung wird erläutert, die lastreduzierende Schaltung (416) lasse in Reaktion auf die Modulsteuersignale die Datenübertragung zwischen dem Speichercontroller (420) und mindestens einer ausgewählten Speichervorrichtung selektiv zu oder unterbinde sie. In Übereinstimmung damit wird in dem Ausführungsbeispiel nach der oben wiedergegebenen Figur 3A die Datenübertragung zwischen dem Speichercontroller (420) und entweder ausgewählten Speichervorrichtungen 412A1 und 412C1 oder ausgewählten Speichervorrichtungen 412B1 und 412D1 selektiv zugelassen oder unterbunden. Entsprechendes gilt im Hinblick auf die lastreduzierende Schaltung 4162 für die Datenübertragung zwischen dem Systemspeichercontroller und entweder ausgewählten Speichervorrichtungen 412A2 und 412C2 oder ausgewählten Speichervorrichtungen 412B2 und 412D2 (Abs. 29, 38). Dabei sieht es die Patentbeschreibung als vorteilhaft an, dass die lastreduzierenden Schaltungen nur die aktivierten Speichervorrichtungen elektrisch mit dem Speichercontroller koppeln und so die vom Speichercontroller wahrgenommene Last reduziert werden kann (Abs. 45).

48 Die nachfolgend wiedergegebene Figur 5 (kolorierte Fassung des Patentgerichts) zeigt ein Ausführungsbeispiel einer lastreduzierenden Schaltung (416).

49 Bei einem Schreibvorgang gelangen Daten über die Datenleitung (518) in die lastreduzierende Schaltung (416) und durchlaufen einen Schreibpuffer (503). Die Daten können auf den zwei Datenpfaden A und B angesteuert werden. In Entsprechung dazu sind die Reihen der Speichervorrichtungen ebenfalls in zwei Gruppen unterteilt, von denen eine dem Pfad A und die andere dem Pfad B zugeordnet ist. In Figur 3A handelt es sich bei der ersten Gruppe um die Reihen A und C und bei der zweiten Gruppe um die Reihen B und D. Das Schreiben von Daten und das Zusammenführen von Lesedaten kann in abgewandelten Ausführungsformen aber auch über mehr als zwei Datenpfade erfolgen (Abs. 47).

50 In Reaktion auf ein Freigabesteuersignal des Modulcontrollers (430) wählt die Logik (502) entweder Pfad A oder Pfad B für die Weiterleitung der Daten aus. Bei Freigabe von Pfad A treibt der freigegebene Tristate-Puffer (504) den Datenwert an seinem Ausgang aktiv an, während der zweite Tristate-Puffer (506) in Pfad B gesperrt und sein Ausgang in einen hochohmigen Zustand versetzt wird. Die Daten werden zum Anschluss Y1 geleitet, der mit der ersten Gruppe der Speichervorrichtungen (in Figur 3A den Reihen A und C) verbunden ist und nur mit diesen kommuniziert (Abs. 49).

51 Bei einem Lesevorgang werden in entsprechender Weise Datensignale von dem ersten oder zweiten Anschluss Y1 bzw. Y2 empfangen und einem Multiplexer (508) zugeführt. Nach Auswahl eines Datensignals auf Grundlage eines von der Logik (502) übermittelten Auswahlsignals wird das Datensignal einem Lesepuffer (509) zugeführt und entlang der Datenleitung (518) an den Speichercontroller übertragen (Abs. 49).

52 bb) Bei den Datenpfaden handelt es sich danach um physische Datenleitungen und nicht nur um logische Datenpfade. Dies ist Voraussetzung dafür, zum Zwecke einer auf eine bestimmte Reihe abzielenden Schreib- oder Leseoperation durch selektive Auswahl und Steuerung Daten über den zugehörigen Pfad und unter Ausschluss anderer Pfade leiten zu können.

53 Patentanspruch 1 unterscheidet dementsprechend zwischen den notwendigen Komponenten, nämlich Datenpfade und Logik (Merkmal 2.5.4), und der Signalsteuerung durch und auf diesen Komponenten (Merkmal 2.5.4.1).

54 Das aktive Treiben des Datensignals bestätigt dies. Dieses dient dazu, die Datensignale nur zu den Speichervorrichtungen zu treiben, auf die die Schreib- oder Leseoperation abzielt und die dementsprechend aktiviert sind (Abs. 53). Damit ist beschrieben, wie die Logik (502) die Datenpfade nutzt, um ein Signal elektrisch zu verstärken und gezielt zu einer Reihe zu leiten. Das Merkmal des aktiven Treibens steht in unmittelbaren technischen Zusammenhang zur Zielgerichtetheit der Datenübertragung. Dabei beinhaltet die Aktivierung eines bestimmten Pfades die gleichzeitige Nichtaktivierung eines abweichenden Pfades und damit dessen Isolierung. Danach ist die Auffassung des Patentgerichts, dass die lastreduzierende Schaltung nach Art einer Weiche funktioniert, nicht zu beanstanden.

55 Durch die vorgenannte Vorgehensweise wird zugleich das vom Streitpatent angestrebte Ziel der Lastreduzierung gefördert. So sieht der Speichercontroller beispielsweise bei vier Vier-Reihen-Speichermodulen (four four-rank memory modules) vier lastreduzierende Schaltkreislasten anstatt sechzehn Speicherbausteinlasten vor (Abs. 53 a.E.).

56 (1) Diesem Verständnis stehen die Ausführungen in Absatz 37 der Beschreibung (Sp. 12 Z. 39 ff.) nicht entgegen. Dort wird der Unterschied zwischen den Ausführungsbeispielen nach Figur 3A und Figur 3B dahin erläutert, dass nach Figur 3B jede lastreduzierende Schaltung mit zwei Speichervorrichtungen jeder Reihe gekoppelt ist. Daraus ergibt sich jedoch nicht zwingend, dass die Verbindung zwischen der lastreduzierenden Schaltung und diesen Reihen über eine einzige Datensignalleitung erfolgt.

57 (2) Auch das von der Berufung herangezogene Ausführungsbeispiel gemäß der nachfolgend wiedergegebenen Figur 4A rechtfertigt keine andere Beurteilung.

58 Der Patentbeschreibung zufolge überträgt auch hier die lastreduzierende Schaltung (416) die Datenbits 0-7 selektiv (selectively) an ausgewählte Speichervorrichtungen 412A, 412B, 412C, 412D. Selbst wenn sich zwei Reihen eine Leitung (452) teilen sollten, muss das Signal gezielt in diesen Pfad (A/C) getrieben und der andere Pfad (B/D) isoliert werden. Bereits dies stellt ein aktives Treiben zu einer Reihe bzw. Reihengruppe unter Ausschluss anderer dar.

59 (3) Der erste Satz von Absatz 44 der Beschreibung steht dem vorgenannten Verständnis ebenfalls nicht entgegen.

60 Dieser mag isoliert und rein sprachlich betrachtet die Deutung zulassen, dass eine Gestaltung mitumfasst sein kann, bei der eine lastreduzierende Schaltung über eine Datensignalleitung mit einer oder mehreren Speichervorrichtungen sämtlicher Reihen von Speichervorrichtungen verbunden ist.

61 Aus dem Zusammenhang der Patentschrift ergibt sich ein solches Verständnis jedoch nicht.

62 Der erste Satz von Absatz 44 steht in unmittelbaren Bezug zu dem im nächsten Satz angesprochenen Ausführungsbeispiel nach Figur 3A, bei dem, wie bereits aufgezeigt wurde, die lastreduzierende Schaltung über zwei Datensignalleitungen mit Speichervorrichtungen der Reihen A und C oder der Reihen B und D verbunden ist. Auch sonst enthält die Beschreibung kein Ausführungsbeispiel, das die eingangs genannte Verständnismöglichkeit bestätigt.

63 Die Forderung nach mehreren Datenpfaden und einer Logik zu deren Steuerung gemäß den Merkmalen 2.5.4 und 2.5.4.1 macht ebenfalls deutlich, dass von der lastreduzierenden Schaltung nicht nur eine Datensignalleitung - und damit nur ein Datenpfad - zu den Speichervorrichtungen führen soll.

64 Absatz 44 steht außerdem im Zusammenhang mit der Erläuterung der Ausführungsbeispiele nach Figuren 3A/4A und 3B/4B. Vor diesem Hintergrund lässt sich der erste Satz zwanglos dahin verstehen, dass er den Unterschied beschreibt zwischen dem Ausführungsbeispiel nach Figur 4A - bei der eine Datensignalleitung zu je einer Speichervorrichtung der Reihen A und C führt - und dem Ausführungsbeispiel nach Figur 4B - bei der zwei Datensignalleitungen zu je zwei Speichervorrichtungen der Reihen A und C führen.

65 (4) Gegen das von der Berufung vertretene Verständnis von Patentanspruch 1 spricht schließlich, dass eine Gestaltung, bei der die lastreduzierende Schaltung über nur eine Datensignalleitung mit Speichervorrichtungen aller Reihen verbunden wäre, die angestrebte Lastreduzierung nur eingeschränkt erzielen könnte. Das Vorsehen einer zusätzlichen Schaltung zwischen Modulcontroller und Speichervorrichtungen führte zwar zu einer Reduktion der Last beim Schreibvorgang, weil der Speichercontroller nur die lastreduzierende Schaltung als Last sähe. Für den Lesevorgang würde eine Lastreduzierung jedoch nicht erreicht, weil jede Speichervorrichtung sowohl die Schaltung als auch die anderen Speichervorrichtungen als Last sähe. Aus der Beschreibung des Streitpatents wird jedoch hinreichend deutlich, dass dieses eine Reduzierung der Last auch für den Lesevorgang anstrebt (Abs. 50 f.).

66 II. Das Patentgericht hat seine Entscheidung, soweit im Berufungsverfahren von Interesse, im Wesentlichen wie folgt begründet:

67 Der Gegenstand von Patentanspruch 1 werde durch die US-amerikanische Patentanmeldung 2006/0277355 (NK11) vollständig vorweggenommen.

68 Die Verteidigung von Patentanspruch 1 in der Fassung nach Hilfsantrag 1 sei nicht zulässig, weil sein Gegenstand in den ursprünglichen Anmeldeunterlagen (NK3) nicht vollständig als zur Erfindung gehörig offenbart sei. Zudem habe dieser Gegenstand ausgehend von dem US-amerikanischen Patent 7 464 225 (QE4) nahegelegen. Entsprechendes gelte für Hilfsantrag 2.

69 Der Gegenstand von Patentanspruch 1 in der mit Hilfsantrag 3 verteidigten Fassung sei in den ursprünglichen Anmeldeunterlagen nicht vollständig offenbart. Er sei zudem ausgehend von NK11 nahegelegt. Entsprechendes gelte für Hilfsanträge 8, 10, 13 und 14.

70 Die Verteidigung nach Hilfsantrag 4 sei wegen unzulässiger Erweiterung unzulässig. Zudem sei der so bestimmte Gegenstand durch QE4 nahegelegt. Entsprechendes gelte für Hilfsanträge 5, 6, 7, 9, 11 und 12.

71 III. Diese Beurteilung hält der Überprüfung im Berufungsrechtszug stand.

72 1. Zu Recht hat das Patentgericht entschieden, dass der Gegenstand von Patentanspruch 1 durch NK11 vollständig vorweggenommen wird.

73 a) NK11 befasst sich mit der Erweiterung der Speicherkapazität eines Speichermoduls.

74 Nach NK11 ist die maximale Größe des adressierbaren Speichers auf einem Speichermodul aus physikalischen Gründen und wegen vorgegebener Industriestandards, nach denen das Hinzufügen von mehr Kontaktstellen oder elektrischen Pfaden zu einem Speichermodul oder einer Systemspeichersteuerung oft unzulässig ist, begrenzt. Eine Erhöhung der Busgröße sei in der Regel im Hinblick auf die Abwärtskompatibilität bestehender Vorrichtungen und Standards unerwünscht oder unpraktikabel (Abs. 5).

75 NK11 sieht vor, auf einem Speichermodul eine Steuereinheit (control unit) und einen Speicherbankschalter (memory bank switch) zu montieren und selektiv Schreib- und Leseoperationen zu oder von den Speichervorrichtungen zu steuern. Durch selektives Weiterleiten von Daten zu und von den Speichervorrichtungen könnten mehrere Speichervorrichtungen für das Betriebssystem als eine einzige Speichervorrichtung erscheinen. Die adressierbaren Speicherbänke auf einem Modul würden erweitert, indem zwei Speichervorrichtungen mit geringerer Kapazität eine einzige Speichervorrichtung mit höherer Kapazität emulierten (Abstract; Abs. 10).

76 Die Hinzufügung zusätzlicher Leitungen zum Bus oder zusätzlicher externer Signale sei hierbei nicht notwendig. Die Speicherbankschalter stellten sich für den Bus als eine einzige Last dar, nicht dagegen die Last der einzelnen daran gekoppelten Speichervorrichtungen. Die Steuereinheit stelle eine Zustandsmaschine bereit, die die Befehle an eine Vielzahl von Speichervorrichtungen in mehreren Bänken so steuere, dass eine einzelne Speicherbank gelesen oder geschrieben wird, ohne die anderen Speicherbänke vom Datenbus trennen zu müssen (Abs. 12).

77 Die nachfolgende Figur 2 zeigt ein Blockdiagramm eines entsprechenden kapazitätserweiternden Speichersystems (200) und Figur 5 ein Speichermodul (500).

78 Das Speichersystem (200) ist mit einer DIMM-Schnittstelle (202) gekoppelt, über die Speicheradressen und Befehle an die Steuereinheit (204) und Dateninformationen an die Speicherbankschalter (206, 208) gesendet werden (Abs. 28, 29).

79 Auf dem Substrat (502) des Speichermoduls sind in Reihen mehrere Speichervorrichtungen (504, 512) montiert. Eine Randschnittstelle (506) mit Kontakten an der Kante kann mit einem Steckplatz oder Bus gekoppelt werden. Von der Randschnittstelle empfängt die Speichersteuerung (510) Adress-, Befehls- und Steuersignale. Die Speichersteuerung ist mit den Speicherbankschaltern (508) gekoppelt, um Lese- oder Schreiboperationen zu den Speichervorrichtungen (504, 512) zu steuern. Die Speicherbankschalter sind zum Zwecke der Datenleitung mit einer oder mehreren Speichervorrichtungen (504, 512) sowie mit der Randschnittstelle gekoppelt.

80 Die Speichersteuerung (510) und die Speicherbankschalter (508) bewirken, dass mit den Speichervorrichtungen (504, 512) ein einzelner Speicherbaustein mit der Gesamtkapazität der kombinierten Speichervorrichtungen emuliert werden kann. So kann eine vom Betriebssystem adressierte einzige logische Speicherbank von der Speichersteuerung den physischen Bänken der Speichervorrichtungen (504, 512) zugeordnet werden (Abs. 48, 49). In Figur 5 sind die Speichervorrichtungen als neun Speicherbankschalter oder -sätze (508) mit jeweils zwei Speicherbänken angeordnet. Als Ergebnis der Anordnung erscheinen die als Speichermodul verwendeten 512-MBit-DRAM-Vorrichtungen dem Systemprozessor als eine 1-GBit-DRAM-Vorrichtung (Abs. 50).

81 In Figur 2 enthält der Speicherbankschalter (206) mit Datenbussen (234, 236) gekoppelte Ports A und B. Die vier Speicherbänke (0, 1, 2, 3) empfangen über den Adressbus (220) Adress- und Befehlsinformationen von der Steuereinheit (204). Der Speicherbankschalter (206) und/oder die Steuereinheit (204) bestimmen jedoch, auf welche Speichervorrichtungen oder Bänke für Lese- oder Schreiboperationen zugegriffen wird. Sie können veranlassen, dass Port B aktiviert und Port A deaktiviert wird. Der Speicherbankschalter (206) umfasst zudem Signaltreiber für die Übertragung der Datensignale (Abs. 30, 31).

82 Teil der Steuereinheit (204) ist ein nachfolgend durch Figur 3 veranschaulichtes Adress- und Befehlsverarbeitungssystem (300), bei der von der DIMM-Schnittstelle empfangene Speicheradressen und Befehlsinformationen in einem Register (302) gepuffert und über den Adressbus an die Speicherbänke übermittelt werden.

83 Eine Zustandsmaschine (bank switch state machine, 308) sendet über den Steuerbus (210) an die Bankschalter (206, 208) Steuerinformationen, die anzeigen, welche Speicherbänke aktiviert oder deaktiviert werden sollen. So kann eine logische Speicherbank auf zwei physikalische Speicherbänke abgebildet werden, indem entweder Port A oder Port B selektiv aktiviert oder deaktiviert wird (Abs. 39, 40).

84 Die nachfolgend wiedergegebene Figur 4 zeigt mit dem Datenverarbeitungssystem (400) einen Teil des Speicherbankschalters (206).

85 Über den Datenbus (230) werden Daten zu bidirektionalen Signaltreibern (402, 404) übertragen. Diese übertragen oder empfangen Daten über getrennte Datenbusse (234, 236) zu den verschiedenen Sätzen von Speicherbänken (Abs. 46).

86 Die nachfolgend wiedergegebene Figur 13 zeigt eine Dual-Chip-Select-Speicherkonfiguration, in der eine Steuereinheit (1302) und ein Bankschalter (1304) verwendet werden, um zwei Speicherbänke (1306, 1308) zu steuern, wobei jede Speicherbank zwei Speichervorrichtungen (1310) in einem gemeinsamen Bus aufweist (Abs. 56).

87 b) Damit offenbart NK11, was die Berufung nicht in Zweifel zieht, die Merkmale 0 bis 2.4.2, 2.5 bis 2.5.4 und 2.5.4.2. Insbesondere wendet sich die Berufung nicht mehr gegen die zutreffenden Feststellungen des Patentgerichts zur Offenbarung der Merkmale 2.3 und 2.3.1.

88 c) Entgegen der Ansicht der Berufung offenbart NK11 auch die Merkmale 2.4.3 und 2.5.4.1.

89 Wie sich aus der obigen Auslegung ergibt, setzt das Merkmal des Abzielens auf eine bestimmte der mehreren Reihen nicht voraus, dass der Speichercontroller abschließend den physischen Ort der Reihe vorgibt. Ausreichend ist, wenn der Modulcontroller auf Basis der Eingangssteuersignale des Speichercontrollers die Bestimmung vornimmt, etwa indem der Modulcontroller dem Signal zusätzliche Chipauswahlsignale hinzufügt.

90 Wie insbesondere aus Figur 13 ersichtlich, zielt die Lese- oder Schreiboperation entweder auf die Speicherbank 1306 oder auf die Speicherbank 1308. Dass die Auswahl der konkreten Speicherbank von der Steuereinheit (1302) - und damit im Sprachgebrauch des Streitpatents vom Modulcontroller - vorgenommen wird, steht der Vorwegnahme von Merkmal 2.4.3 nicht entgegen.

91 Auch Merkmal 2.5.4.1 ist offenbart. Der Speicherbankschalter (1304) weist zwei Datenpfade und eine Logik zum Steuern der Datenpfade auf, die in Reaktion auf entsprechende Signale der Steuereinheit (1302) die Daten entweder von oder zu der an Port A angeschlossenen oder von oder zu der an Port B angeschlossenen Speicherbank treiben, während die Verbindung zu der jeweils anderen Speicherbank deaktiviert ist.

92 2. Die Verteidigung des Gegenstands von Patentanspruch 1 in der Fassung nach Hilfsantrag 1 ist unzulässig.

93 a) Nach Hilfsantrag 1 soll Patentanspruch 1 wie folgt geändert und ergänzt werden (Änderungen hervorgehoben):

94 3HA1

wherein, when the memory controller (420) executes a read or write operation, the read or write operation is targeted at a specific one of the multiple ranks of the memory module (402, 402').

2.4

a module controller (430, 430') coupled to the module board (410, 410') and configured

2.4.1HA1

to receive input control signals for the a read or write operation from the memory controller (420) via the set of control signal lines (440, 440') and

2.4.2

to output first module control signals based on the input control signals,

2.4.3HA1

the read or write operation being targeted at the a specific one of the multiple ranks;

2.5

second number of load-reducing circuits (416, 416') coupled to the module board (410, 410') and configured to receive the first module control signals,

2.5.1

each respective one of the second number of load-reducing circuits (416, 416') being coupled to a respective set of the second number of sets of data signal lines (450, 450') and

2.5.2HA1

to at least one respective memory device (412, 412') in each of the multiple ranks via a respective set of module data lines (452, 452'),

2.5.3

the second number of load-reducing circuits (416, 416') being disposed on the module board (410, 410') at respective positions corresponding to respective sets of the second number of sets of data signal lines (450, 450'); and

2.6HA1

wherein each module data line (452, 452') of the respective set of module data lines (452, 452') is connected to a respective memory device (412, 412') in each of the multiple ranks, such that each data signal line (450, 450') of the respective set of the second number of sets of data signal lines (450, 450') and a corresponding module data line (452, 452') of the respective set of module data lines (452, 452') carry data from the memory controller (420) through the respective load-reducing circuit (416, 416') to the respective memory device (412, 412') in each of the multiple ranks.

95 b) Die zusätzlichen oder modifizierten Merkmale bedürfen der Erläuterung.

96 aa) Nach Merkmal 3HA1 gibt der Speichercontroller vor, auf welche bestimmte Reihe (von den mehreren Reihen des Speichermoduls) bei einer Lese- oder Schreiboperation abgezielt wird. Umgesetzt wird dies weiterhin dadurch, dass der Modulcontroller entsprechende Eingangssteuersignale empfängt, auf deren Basis er Modulsteuersignale für die Lese- oder Schreiboperation ausgibt (Merkmale 2.4.1, 2.4.2). Im Rahmen dieses Prozesses darf der Modulcontroller nach der Patentbeschreibung zusätzliche Chipauswahlsignale hinzufügen (Abs. 36). Dem ist nicht anders als für die erteilte Fassung von Patentanspruch 1 zu entnehmen, dass der Modulcontroller von der physischen Reihenangabe abweichen kann.

97 bb) Die Merkmale 2.5.2 HA1 und 2.6HA1 besagen, dass jede interne Datenleitung (Modul-Datenleitung 452) physikalisch mit einem Speicherchip in jeder der vorhandenen Reihen (Ranks) verbunden ist. Weiterhin legt das Merkmal fest, dass die Daten zwingend durch die lastreduzierende Schaltung (416) fließen müssen.

98 Damit soll die Zwischenschaltung einer "Weiche" in der lastreduzierenden Schaltung ausgeschlossen sein.

99 c) Zu Recht hat das Patentgericht entschieden, dass dieser Gegenstand in den ursprünglichen Anmeldeunterlagen, die der internationalen Patentanmeldung 2011/008580 (NK3) entsprechen, nicht als zur Erfindung gehörig offenbart ist.

100 Wie bereits oben aufgezeigt wurde, ist Patentanspruch 1 in der erteilten Fassung auf eine Gestaltung beschränkt, bei der die lastreduzierende Schaltung mindestens zwei Datenpfade und eine Logik aufweist, die in Reaktion auf die Modulsteuersignale bewirkt, dass die Daten entweder über den einen oder den anderen Datenpfad zu bzw. von der jeweiligen spezifischen Reihe von Speichervorrichtungen getrieben werden. Eine Gestaltung, bei der eine Moduldatensignalleitung von der lastreduzierenden Schaltung zu einer Speichervorrichtung in jeder der vorhandenen Reihen von Speichervorrichtungen führt, ist auch in den ursprünglichen Anmeldeunterlagen nicht als zur Erfindung gehörig offenbart.

101 Für das Verständnis der Absätze 51 und 58 der Beschreibung der NK3 gilt nichts anderes als für das Verständnis der inhaltsgleichen Absätze 37 und 44 des Streitpatents.

102 3. Die Verteidigung in der Fassung nach Hilfsantrag 2 bleibt ebenfalls erfolglos.

103 a) Hilfsantrag 2 ist bereits deshalb unzulässig, weil er die Merkmale 2.5.2HA1 und 2.6HA1 umfasst.

104 b) Hilfsantrag 2 fügt dem Gegenstand von Hilfsantrag 1 die folgenden Merkmale hinzu:

105 2.4.1HA1

to receive input control signals for the a read or write operation from the memory controller (420) via the set of control signal lines (440, 440') and

2.4.1.1HA2

wherein the input control signals comprise chip-select signals for selecting the specific one of the multiple ranks;

2.4.1.2HA2

the module controller (430, 430') is further configured to register the input control signals including the chip-select signals, and to transmit registered control signals including registered chip-select signals to the plurality of memory devices (412, 412') via registered control lines (442, 442') to activate the specific one of the multiple ranks to perform the read or write operation;

106 c) Mit der Anforderung, registrierte Steuersignale einschließlich registrierter Chip-Select-Signale zu übertragen, enthält Merkmal 2.4.1.2HA2 nach Auffassung der Beklagten die Vorgabe, die Signale (zeitlich verzögert) unverändert zu übertragen.

107 d) Das Patentgericht hat im Ergebnis zu Recht entschieden, dass Merkmal 2.4.1.2HA2 mit diesem Sinngehalt in der ursprünglichen Anmeldung (NK3) nicht unmittelbar und eindeutig als zur Erfindung gehörig offenbart ist.

108 Aus der dortigen, der Erläuterung der Figur 3A dienenden Beschreibung ergibt sich, dass der Modulcontroller vom Speichercontroller Steuersignale empfängt, wobei das Registrieren der Signale von den Steuerleitungen (440, 440') in einer Weise erfolgen kann, die mit der Funktion eines Adressregisters eines herkömmlichen RDIMM vergleichbar sein mag (Abs. 50 erster u. zweiter Satz). Der Modulcontroller kann seinerseits Steuersignale über die Leitungen (442, 442') an die Speichervorrichtungen geben (Abs. 49). Hinzu kommt die Anforderung, dass der Modulcontroller zusätzlich über die Leitungen (432, 432') die lastreduzierenden Schaltungen steuert (Abs. 50 vierter Satz: "Additionally, the control circuit 430, 430' supplies control signals for the data transmission circuits 416,416' (e.g., via lines 432,432') ..."). Dabei nennt die Anmeldung als Beispiel für die Steuerung Steuersignale, die die Richtung des Datenflusses zu oder von den Speichervorrichtungen (Lesen oder Schreiben) bestimmen.

109 In Übereinstimmung mit den Merkmalen 2.5.4 und 2.5.4.1 ist demnach vorgesehen, dass die lastreduzierenden Schaltungen in Reaktion auf die Modulsteuersignale die Datenpfade schalten, um die Daten zur ausgewählten spezifischen Reihe zu treiben. Eine Variante, bei der das Signal, mit dem der Speichercontroller eine bestimmte Speicherreihe auswählt, vom Modulcontroller unverändert weitergereicht und allein durch dieses Signal die Speicherreihe aktiviert wird, ist damit in der Anmeldung nicht offenbart. Offenbart ist nur ein Vorgehen, bei dem der Modulcontroller (auch) Steuersignale an die lastreduzierende Schaltung gibt, die dann der Steuerung der Datenpfade dienen. Der Modulcontroller ist notwendig einbezogen und steuert die "Weiche".

110 Die Angabe in der Anmeldung, die registrierten Steuerleitungen seien auch operativ mit den Speichergeräten verbunden (Abs. 50 dritter Satz: "The registered control lines 440, 440' are also operatively coupled to the memory devices 412, 412'."), rechtfertigt keine abweichende Beurteilung. Auch hieraus ergibt sich keine eindeutige und unmittelbare Offenbarung einer von der genannten Datenpfadsteuerung abweichenden Durchreich-Variante.

111 4. Hilfsantrag 3 ist nicht günstiger zu beurteilen.

112 Nach Hilfsantrag 3 soll Patentanspruch 1 in der Fassung nach Hilfsantrag 1 um die nachfolgend wiedergegebenen Merkmale ergänzt werden (Änderungen hervorgehoben):

113 2.4.1HA1

to receive input control signals for the a read or write operation from the memory controller (420) via the set of control signal lines (440, 440') and

2.4.1.1HA3

wherein the input control signals comprise column address signals for accessing a particular column in the specific one of the multiple ranks;

2.4.1.2HA3

the module controller (430, 430') is further configured to register the input control bit width signals including the column address signals, and to transmit registered control signals including registered column address signals to the plurality of memory devices (412, 412') via registered control lines (442, 442') to access the particular column in the specific one of the multiple ranks;

...

2.7HA3

and wherein the memory module (402, 402') is further configured to control operation of the second number of load-reducing circuits (416, 416') by using a column address strobe, CAS, latency,

2.7.1HA3

wherein the CAS latency is a delay time which elapses between the moment the memory controller (420) informs the memory module (402, 402') to access the particular column in the specific one of the multiple ranks and the moment the data for or from the particular column is on output pins of the specific one of the multiple ranks.

114 a) Hilfsantrag 3 legt fest, wann und an welcher Stelle (Spaltenadresse) innerhalb der bestimmten Reihe die Datenverarbeitung erfolgt. Die Signale werden im Modulcontroller zwischengespeichert und getaktet, wobei der Modulcontroller die Wartezeit, bis der Speicherchip antwortet, berücksichtigt (CAS-Latenz).

115 b) Zu Recht hat das Patentgericht entschieden, dass Merkmalsgruppe 2.4.1HA3 - nicht anders als die Fassung nach Hilfsantrag 2 - in den ursprünglichen Anmeldeunterlagen nicht als zur Erfindung gehörig offenbart ist.

116 Ob die Merkmalsgruppe 2.7HA3 ursprünglich offenbart ist, kann danach offenbleiben.

117 5. Hilfsantrag 6 bleibt ebenfalls ohne Erfolg.

118 Danach soll Patentanspruch 1 nach Hilfsantrag 2 um folgendes Merkmal ergänzt werden:

119 2.4.4HA6

wherein the module controller (430, 430') is further configured to output the first module control signals to the second number of load reducing circuits (416, 416') in accordance with a column address strobe, CAS, latency parameter, and to control the timing of the data signals corresponding to the read or write operation in the second number of load-reducing circuits (416, 416') in accordance with the CAS latency parameter

120 a) Aus Merkmal 2.4.4HA6 ergibt sich, dass der Modulcontroller die Steuersignale an die lastreduzierenden Schaltungen in Übereinstimmung mit der CAS-Latenz ausgibt. Er steuert dabei das Timing der Datensignale innerhalb dieser Puffer derart, dass die Aktivierung der Datenpfade mit der Speicherchip-spezifischen Wartezeit zur Datenbereitstellung korrespondiert.

121 b) Hilfsantrag 6 ist mit der Aufnahme von Merkmal 2.4.1.2HA2 unzulässig erweitert.

122 Das mit Hilfsantrag 6 hinzugefügte Merkmal 2.4.4HA6 hat das Patentgericht zutreffend als ebenfalls nicht ursprungsoffenbart angesehen.

123 Zwar erwähnt NK3 allgemein, dass die CAS-Latenz zur Steuerung der Datenübertragungsschaltungen verwendet werden kann (Abs. 62). Eine spezifische Ausgestaltung dieser Steuerung wird jedoch nicht beschrieben. Insbesondere ist nicht offenbart, dass der Modulcontroller erste Modulsteuersignale "in Übereinstimmung mit der CAS-Latenz" ausgibt.

124 Nach der weiteren Beschreibung (Abs. 63) liefert der Modulcontroller Freigabesignale an die Steuerlogikschaltung 502 und nicht, wie von Merkmal 2.4.4 gefordert, allgemein an die lastreduzierenden Schaltungen.

125 Außerdem beschränkt sich die Steuerung darauf, dass die Logik zwischen Pfad A oder Pfad B auswählt, um Daten zu leiten (Abs. 63). Eine allgemeine Konfiguration zur Steuerung des Timings der Datensignale für Lese- und Schreibvorgänge lässt sich daraus nicht ableiten.

126 6. Auch Hilfsantrag 14 bleibt erfolglos.

127 Nach Hilfsantrag 14 soll Patentanspruch 1 in der erteilten Fassung am Ende wie folgt ergänzt werden:

128 2.5.5

wherein the each respective load-reducing circuit (416, 416') presents a reduced load such that during a write operation, the memory controller (420) sees a single memory device load from the memory module (402, 402') on each of the first number of data signal lines.

129 a) Nach Merkmal 2.5.5 wird dem Speichercontroller beim Schreibvorgang durch die lastreduzierende Schaltung eine Last präsentiert, die derjenigen einer einzelnen Speichervorrichtung entspricht.

130 Nähere Angaben dazu, um welche Art von Speichervorrichtung es sich handelt und welche Last eine solche präsentiert, sind dem Anspruch nicht zu entnehmen.

131 b) Es bedarf keiner Entscheidung, ob dieses Merkmal durch NK11 unmittelbar und eindeutig vorweggenommen ist. Der Gegenstand von Patentanspruch 1 in dieser Fassung ist ausgehend von NK11 jedenfalls nahegelegt.

132 Nach der Beschreibung der NK11 führt die dort vorgeschlagene Gestaltung gemäß dem Ausführungsbeispiel nach Figur 5 dazu, dass das Speichermodul dem Computersystem eine einzelne elektrische Last präsentiert und mit den bestehenden Standards kompatibel ist (Abs. 50).

133 Auch an anderer Stelle der NK11 wird erläutert, dass die dort beschriebene Lehre bewirkt, dass die dem Bus präsentierte Last nicht erhöht wird, weil die lastreduzierenden Schaltungen dem Bus jeweils nur eine einzelne Last anstelle der Lasten der individuellen Speichervorrichtungen (Abs. 12, Abs. 27) präsentieren.

134 Aufgrund dieser Gegenüberstellung liegt es jedenfalls nahe, die Vorrichtung so zu gestalten, dass die dem System präsentierte Last derjenigen einer einzelnen Speichervorrichtung entspricht.

135 7. Da Patentanspruch 1 in den geänderten Fassungen gemäß den Hilfsanträgen 4, 5, 7 bis 11 und 13 jeweils mindestens eines der Merkmale enthält, die nach den vorstehenden Ausführungen nicht ursprünglich offenbart sind, ist auch die Verteidigung des Streitpatents in diesen Fassungen unzulässig.

136 8. Die Verteidigung des Streitpatents in der Fassung der Hilfsanträge 15 bis 17 ist ebenfalls unzulässig.

137 Die hilfsweise Verteidigung des Streitpatents mit geänderten Ansprüchen in der Berufungsinstanz kann regelmäßig nicht als sachdienlich im Sinne von § 116 Abs. 2 Nr. 1 PatG angesehen werden, wenn die Beklagte dazu bereits in erster Instanz Veranlassung hatte. Ein solcher Anlass zur zumindest hilfsweisen beschränkten Verteidigung ergibt sich regelmäßig daraus, dass das Patentgericht in seinem nach § 83 Abs. 1 PatG erteilten Hinweis mitgeteilt hat, nach seiner vorläufigen Auffassung sei der Gegenstand des Patents nicht patentfähig.

138 Im Streitfall hat das Patentgericht in seinem Hinweis ausgeführt, dass die Lehre von Patentanspruch 1 verlange, dass ein Datenpfad wie bei einer Weiche zu der bestimmten einen Reihe aktiviert und zu den anderen Reihen deaktiviert werde, und durch NK11 vorweggenommen sei.

139 Dieser Hinweis gab der Beklagten Veranlassung, Patentanspruch 1 gegebenenfalls zu ergänzen, wenn sie die geschützte Lehre von der in NK11 offenbarten Lösung abgrenzen wollte. Diese Veranlassung bestand auch für den Fall, dass das Patentgericht - wie geschehen - an seiner Auffassung zur Notwendigkeit einer Konfiguration als Weiche festhält.

140 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG und § 97 Abs. 1 ZPO.

Deichfuß

Kober-Dehm

Marx

Crummenerl

von Pückler
