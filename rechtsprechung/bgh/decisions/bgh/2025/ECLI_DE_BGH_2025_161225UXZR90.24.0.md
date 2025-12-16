---
ecli: "ECLI:DE:BGH:2025:161225UXZR90.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 90/24"
decided: "2025-12-16"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600012026.xml"
neuris_doknr: "KORE600012026"
---

# Bundesgerichtshof, X ZR 90/24 vom 2025-12-16

## Tenor

Die Berufung gegen das Urteil des 2. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 18. Juli 2024 wird auf Kosten der Beklagten zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 575 366 (Streitpatents), das am 31. Juli 2012 unter Inanspruchnahme zweier US-Prioritäten vom 27. September 2011 und 14. Juni 2012 angemeldet worden ist.

2 Patentanspruch 1, auf den vier weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

An apparatus, comprising: a video encoder to encode an input video signal to generate an output bitstream; and wherein:

the video encoder employs a single binary tree for use in processing at least one P slice and at least one B slice for generating the output bitstream, characterised in that:

the video encoder employs the single binary tree representing a binarization to encode coding unit (CU) prediction mode in a first syntax element for both the at least one P slice and the at least one B slice for generating the output bitstream; and

the video encoder employs the single binary tree representing said binarization to encode prediction unit (PU) partition mode in a second syntax element for both the at least one P slice and the at least one B slice for generating the output bitstream;

wherein the binarization employed is a function of whether or not a current CU of the at least one P slice or the at least one B slice is the smallest CU, SCU, or not.

3 Patentanspruch 6, auf den ein weiterer Anspruch zurückbezogen ist, schützt sinngemäß ein Verfahren zum Betrieb eines Videocodierers mit korrespondierenden Merkmalen.

4 Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents sei nicht patentfähig und gehe über den Inhalt der ursprünglichen Anmeldeunterlagen hinaus. Die Beklagte hat das Streitpatent in der erteilten Fassung und hilfsweise in vier geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt. Dagegen richtet sich die Berufung der Beklagten, die ihre erstinstanzlichen Anträge weiterverfolgt. Die Klägerin tritt dem Rechtsmittel entgegen.

## Entscheidungsgründe

6 Die zulässige Berufung ist unbegründet.

7 I. Das Streitpatent betrifft die Codierung von Videodaten.

8 1. Nach der Beschreibung des Streitpatents kann es bei der Übertragung von digitalen Videodaten zu einem Zielkonflikt (trade-off) zwischen Durchsatz und Qualität kommen.

9 Im Stand der Technik sei kein Weg bekannt, eine Übertragung in akzeptabler Qualität mit relativ geringem zusätzlichem Aufwand (overhead) zu erreichen und die Endgeräte relativ einfach ausgestalten zu können.

10 Vor diesem Hintergrund betrifft das Streitpatent das technische Problem, eine Übertragung bei möglichst hoher Qualität und geringem Aufwand mit möglichst einfach ausgestalteten Endgeräten zu ermöglichen.

11 2. Zur Lösung schlägt Patentanspruch 1 eine Vorrichtung vor, deren Merkmale sich wie folgt gliedern lassen:

12 1

An apparatus, comprising:

Eine Vorrichtung, die umfasst:

1.1

a video encoder to encode an input video signal to generate an output bitstream; and wherein:

einen Video-Encoder zum Codieren eines Eingangsvideosignals, um einen Ausgangsbitstrom zu erzeugen.

1.2

the video encoder employs a single binary tree for use in processing at least one P slice and at least one B slice for generating the output bitstream,

Der Video-Encoder setzt einen einzelnen Binärbaum zur Verwendung bei der Verarbeitung wenigstens eines P-Slice und wenigstens eines B-Slice zum Erzeugen des Ausgangsbitstroms ein.

1.3

the video encoder employs the single binary tree representing a binarization to encode coding unit (CU) prediction mode in a first syntax element for both the at least one P slice and the at least one B slice for generating the output bitstream; and

Der Video-Encoder setzt zum Erzeugen des Ausgangsbitstroms den eine Binarisierung repräsentierenden einzelnen Binärbaum sowohl für den wenigstens einen P-Slice als auch für den wenigstens einen B-Slice ein

zum Codieren eines Prädiktionsmodus für eine Codiereinheit (CU/Coding Unit) in einem ersten Syntaxelement und

1.4

the video encoder employs the single binary tree representing said binarization to encode prediction unit (PU) partition mode in a second syntax element for both the at least one P slice and the at least one B slice for generating the output bitstream;

zum Codieren eines Partitionsmodus für eine Prädiktionseinheit (PU/Prediction Unit) in einem zweiten Syntaxelement.

1.5

wherein the binarization employed is a function of whether or not a current CU of the at least one P slice or the at least one B slice is the smallest CU, SCU, or not.

Die eingesetzte Binarisierung ist davon abhängig, ob eine aktuelle Codiereinheit (CU) des wenigstens einen P-Slice oder des wenigstens einen B-Slice die kleinste Codiereinheit (SCU/smallest CU) ist.

13 3. Einige Merkmale bedürfen der näheren Erörterung.

14 a) Die in den Merkmalen 1.2 bis 1.5 erwähnten P- und B-Slices unterscheiden sich durch die Art der Prädiktionscodierung.

15 aa) Bei der Prädiktionscodierung wird einem Macroblock zum Zwecke der Dateneinsparung lediglich ein Residualwert zugewiesen.

16 Der Residualwert kann zum Beispiel aus der Differenz zwischen dem tatsächlichen Wert für diesen Macroblock und einem Vorhersagewert (predicted value) bestehen. Der Vorhersagewert kann auf der Grundlage mindestens eines Bereichs (portion) desselben Rahmens oder Bildes erstellt werden oder auf der Grundlage mindestens eines Bereichs von zumindest einem anderen Rahmen oder Bild (Abs. 50). Im ersten Fall spricht man von Intra-Prädiktion, im letzteren von Inter-Prädiktion (Abs. 77).

17 bb) Nach der Beschreibung des Streitpatents unterscheidet der zum Prioritätszeitpunkt in Entwicklung befindliche Standard HEVC (High Efficiency Video Coding) zwischen Slices der Typen I, P und B:

18 In I-Slices findet Prädiktion allenfalls in Bezug auf denselben Rahmen statt (Abs. 99).

19 P-Slices verwenden eine (einzige) Referenzliste, die jeweils auf einen einzelnen anderen Frame verweist. Dieser kann vor oder nach dem aktuellen Frame angeordnet sein (Abs. 100).

20 In B-Slices können vorangegangene und nachfolgende Rahmen kumulativ zur Prädiktion herangezogen werden. Hierzu können zum Beispiel zwei unterschiedliche Referenzlisten vorhanden sein (Abs. 101).

21 cc) Patentanspruch 1 beruht auf diesem Verständnis.

22 Die Merkmale 1.2 bis 1.5 betreffen mithin Slices, die eine Inter-Prädiktion in jeweils eine Richtung (P-Slices) oder kumulativ in beide Richtungen (B-Slices) ermöglichen.

23 b) Ein Partitionsmodus im Sinne von Merkmal 1.4 ist die Art und Weise, in der eine Codiereinheit (CU) in Prädiktionseinheiten unterteilt ist.

24 aa) Nach der Beschreibung bilden Codiereinheiten im Standard HEVC das Gegenstück zu Macroblocks im Sinne des älteren Standards AVC (Advanced Video Coding, H.264) (Abs. 95).

25 Eine Codiereinheit hat eine quadratische Form. Sie kann in mehreren hierarchischen Stufen in Untereinheiten aufgeteilt sein, die ebenfalls quadratisch sind (Abs. 96). Dies ist in der nachfolgend wiedergegebenen Figur 11 dargestellt.

26 Jede Codiereinheit kann entweder Intra- oder Interprädiktion im oben aufgezeigten Sinne einsetzen (Abs. 97).

27 bb) Jede Codiereinheit ist ferner in Prädiktionseinheiten aufgeteilt. Diese können die gesamte Codiereinheit, jeweils eine Hälfte oder jeweils ein Viertel davon umfassen. Dies ist in der nachfolgend wiedergegebenen Figur 12 dargestellt.

28 Die Aufteilung in vier Viertel (N x N) ist nach HEVC nur für die kleinste Inhaltseinheit (smallest content unit, SCU) zulässig (Abs. 98).

29 c) Ein Binärbaum im Sinne der Merkmale 1.2 bis 1.4 ist eine Datenstruktur, die aus hierarchisch angeordneten Knoten besteht.

30 aa) Zwei Beispiele eines Binärbaums sind in der nachfolgend wiedergegebenen Figur 13 dargestellt.

31 Bei dieser Ausgestaltung werden den Kindknoten jeweils die Binärwerte 0 oder 1 zugeordnet. Jeder Knoten wird durch die Abfolge der seinen Vorgängern und ihm selbst zugeordneten Binärwerte gekennzeichnet. Jeder dieser Binärwertfolgen wird eine bestimmte Bedeutung zugeordnet.

32 Die beiden dargestellten Binärbäume sind ferner so ausgestaltet, dass lediglich Knoten mit dem Wert 0 Kindknoten aufweisen. Dies führt dazu, dass die den einzelnen Knoten zugeordneten Binärwertfolgen unterschiedliche Längen aufweisen. Dies ermöglicht eine so genannte Huffman-Codierung, bei der statistisch häufiger auftretende Werte einer möglichst kurzen Binärwertfolge zugeordnet werden und statistisch seltener auftretende Werte einer längeren (Abs. 103).

33 bb) Patentanspruch 1 gibt weder eine bestimmte Ausgestaltung des Binärbaums noch eine der Huffman-Codierung entsprechende Verteilung der zu codierenden Werte nach Wahrscheinlichkeit zwingend vor.

34 Binärbaum im Sinne des Streitpatents ist deshalb jede Baumstruktur, bei der jeder Knoten nur zwei Kindknoten aufweisen kann.

35 d) Eine Binarisierung im Sinne der Merkmale 1.3 bis 1.5 ist, wie das Patentgericht und die Parteien im Ausgangspunkt übereinstimmend und zutreffend angenommen haben, die Zuordnung einzelner Binärwertfolgen zu einem bestimmten Ausgangswert.

36 In dem oben dargestellten Beispiel aus Figur 13 wird den einzelnen Prädiktionsmodi jeweils einer der im Binärbaum dargestellten Binärwerte zugewiesen. Der Binärbaum repräsentiert die auf diese Weise vorgenommene Binarisierung.

37 e) Die in den Merkmalen 1.2 bis 1.4 formulierten Vorgaben, dass ein einzelner Binärbaum sowohl für mindestens einen P-Slice und mindestens einen B-Slice als auch zum Codieren eines Prädiktionsmodus für eine Codiereinheit und zum Codieren eines Partitionsmodus für eine Prädiktionseinheit eingesetzt werden muss und dass für die beiden Modi zwei Syntaxelemente vorgesehen sein müssen, werden in der Beschreibung nicht im Zusammenhang erläutert.

38 aa) Der Einsatz desselben Binärbaums für P- und B-Slices ist im Zusammenhang mit der oben wiedergegebenen Figur 13 und im Zusammenhang mit Figur 14 geschildert.

39 (1) Nach der Beschreibung ist der in Figur 13 dargestellte Binärbaum in erster Linie für die Codierung von P-Slices vorgesehen. Alternativ kann derselbe (the very same) Binärbaum zugleich für die Codierung von B-Slices eingesetzt werden (Abs. 105).

40 (2) Ähnliche Alternativen schildert die Beschreibung im Zusammenhang mit der nachfolgend wiedergegebenen Figur 14.

41 Auch in diesem Zusammenhang zeigt die Beschreibung zwei alternative Ausgestaltungen auf.

42 Bei einer ersten Ausführungsform wird der in Figur 14 dargestellte Binärbaum für die Codierung von B-Slices eingesetzt und der auf der rechten Seite von Figur 13 (und nochmals in Figur 15) dargestellte Binärbaum für die Codierung von P-Slices. Der Einsatz des zuletzt genannten Baums hat Vorteile, weil er weniger Daten benötigt. Andererseits erfordert diese Ausgestaltung den Einsatz unterschiedlicher Codebücher für B- und P-Slices (Abs. 108).

43 Alternativ kann der in Figur 14 dargestellte Binärbaum sowohl für B- als auch für P-Slices eingesetzt werden. Der Einsatz desselben (the very same) Baums ist vorteilhaft, weil nur ein Codebuch benötigt wird (Abs. 109).

44 (3) Nach der Beschreibung kann eine Vielzahl unterschiedlicher Ausgestaltungen implementiert werden.

45 So könne in einigen Situationen (instances) eine einheitliche Verarbeitung von P- und B-Slices unter Einsatz eines gemeinsamen Binärbaums wie in Figur 14 erfolgen. In anderen Situationen, in denen getrennte und unterschiedliche Binärbäume und Codebücher eingesetzt würden, und insbesondere dann, wenn die kleinste Inhaltseinheit (SCU) nicht eingesetzt werde, könne für P-Slices ein modifizierter Binärbaum wie auf der rechten Seite von Figur 13 (und in Figur 15) eingesetzt werden und für B-Slices der Binärbaum aus Figur 14 (Abs. 113).

46 bb) Der Einsatz desselben Baums für die Codierung von Prädiktions- und Partitionsmodus ist nur im Zusammenhang mit Figur 14 dargestellt.

47 Die Beschreibung führt hierzu aus, der Standard HEVC sehe unterschiedliche Codewörter für den Partitionsmodus bei P- und B-Slices vor. In P-Slices würden der Prädiktions- und der Partitionsmodus in getrennten Syntaxelementen codiert, in B-Slices hingegen gemeinsam in einem einzelnen Syntaxelement. Wenn wie in Figur 14 derselbe Binärbaum für P- und B-Slices eingesetzt werde, könne derselbe Ansatz aber auch für die Codierung von Prädiktions- und Partitionsmodus eingesetzt werden (Abs. 112).

48 cc) Der Einsatz von zwei getrennten Syntaxelementen für Prädiktions- und Partitionsmodus wird in der Beschreibung ebenfalls als eine von zwei möglichen Ausgestaltungen geschildert.

49 (1) Im Zusammenhang mit der zweiten Ausführungsform aus Figur 13 - also dem Einsatz desselben Binärbaums für P- und B-Slices - führt die Beschreibung aus, für den Prädiktions- und den Partitionsmodus könnten unterschiedliche Syntaxelemente eingesetzt werden (Abs. 106).

50 (2) Im Zusammenhang mit Figur 14 wird ausgeführt, die beiden Modi würden gemeinsam in einem einzelnen Syntaxelement codiert (Abs. 107).

51 (3) In den bereits erwähnten Erläuterungen zur Möglichkeit, die Codebücher für den Partitionsmodus für P- und B-Slices zu vereinheitlichen, wird ausgeführt, auch bei einer solchen Ausgestaltung könnten die beiden Modi wahlweise in getrennten Syntaxelementen codiert werden oder gemeinsam in einem einzigen Syntaxelement (Abs. 112).

52 (4) Bei der beispielhaften Schilderung von Verfahren, die von den aufgezeigten Codierungsmöglichkeiten Gebrauch machen, wird die Verwendung getrennter Syntaxelemente oder eines gemeinsamen Syntaxelements ebenfalls als Alternative dargestellt.

53 (a) Bei einer ersten Variante, die in der nachfolgend wiedergegebenen Figur 16B dargestellt ist, wird ein einzelner (a single) Binärbaum eingesetzt, um den Prädiktions- und den Partitionsmodus in einem einzelnen Syntaxelement zu codieren (Abs. 117).

54 (b) Eine zweite Variante ist in der nachfolgend wiedergegebenen Figur 17A dargestellt.

55 Bei dieser Ausgestaltung wird zunächst ein einzelner (a single) Binärbaum eingesetzt, um den Prädiktionsmodus in einem ersten Syntaxelement zu codieren, und zwar gleichermaßen für jeweils mindestens einen P- und einen B-Slice (Abs. 118).

56 Anschließend wird der einzelne (the single) Binärbaum eingesetzt, um den Partitionsmodus in einem zweiten Syntaxelement zu codieren, wiederum gleichermaßen für jeweils mindestens einen P- und einen B-Slice (Abs. 119).

57 f) Vor diesem Hintergrund erweist sich die vom Patentgericht vorgenommene Auslegung der Merkmale 1.3 und 1.4 nicht in allen Punkten als zutreffend.

58 aa) Im Ausgangspunkt zutreffend ist das Patentgericht davon ausgegangen, dass die in den Merkmalen 1.3 und 1.4 vorgesehenen Binärbäume nicht identisch sein müssen.

59 (1) Der diesbezügliche Wortlaut von Merkmal 1.4 legt allerdings ein abweichendes Verständnis nahe.

60 Die Verwendung des bestimmten Artikels (the single binary tree) und die Bezugnahme auf eine bestimmte Binarisierung (representing said binarization) sprechen bei isolierter Betrachtung dafür, dass für die Codierung des Partitionsmodus gemäß Merkmal 1.4 derselbe Binärbaum zum Einsatz kommen muss, der gemäß Merkmal 1.3 für die Codierung des Prädiktionsmodus eingesetzt wird.

61 Andererseits geben sowohl Merkmal 1.4 als auch Merkmal 1.3 abweichend von den Erläuterungen zu den Figuren 13 und 14 nicht vor, denselben (the very same) Binärbaum einzusetzen, sondern einen einzelnen (single) Binärbaum.

62 (2) Gegen eine Gleichsetzung dieser beiden Begriffe spricht der Umstand, dass die Merkmale 1.3 und 1.4 für den Prädiktionsmodus und den Partitionsmodus jeweils ein eigenes Syntaxelement vorgeben.

63 (a) Als Syntaxelement in diesem Sinne kann mangels näherer Festlegungen in Patentanspruch 1 zwar grundsätzlich jeder Teilbereich der codierten Daten angesehen werden. Aus der Vorgabe, dass der Prädiktionsmodus in ein erstes und der Partitionsmodus in ein zweites Syntaxelement zu codieren ist, ergibt sich aber entgegen der Auffassung des Patentgerichts, dass die Informationen bezüglich der beiden Modi separat voneinander abgelegt werden müssen.

64 Dies schließt zwar entgegen der Auffassung der Berufung nicht aus, dass ein Syntaxelement auf mehrere nicht unmittelbar aufeinander folgende Teilbereiche der codierten Daten verteilt ist. Ein Element, das Informationen zum einen Modus enthält, darf aber grundsätzlich keine Informationen zum anderen Modus enthalten.

65 (b) Die Verwendung desselben (the very same) Binärbaums für die Codierung von Prädiktions- und Partitionsmodus sieht die Beschreibung nur für den Fall vor, dass beide Informationen in ein gemeinsames Syntaxelement codiert werden. Für den Fall, dass zwei getrennte Syntaxelemente eingesetzt werden, ist demgegenüber nur der Einsatz eines einzelnen (single) Binärbaums vorgesehen.

66 Diese Unterscheidung ist technisch sinnvoll, weil der zweimalige Einsatz eines Binärbaums, der Informationen zu beiden Modi repräsentiert, zu Redundanzen führt und deshalb in Widerspruch zu dem im Streitpatent hervorgehobenen Ziel einer möglichst effizienten Codierung steht.

67 Patentanspruch 1 schließt solche Redundanzen zwar nicht zwingend aus. Eine Auslegung, bei der dieses Ergebnis nicht nur möglich, sondern praktisch unvermeidlich wäre, stünde aber in Widerspruch zum Zweck der Merkmale 1.3 und 1.4.

68 (3) Dieses Verständnis hat allerdings zur Folge, dass die in den Figuren 13 und 14 dargestellten Ausführungsbeispiele die Merkmale 1.3 und 1.4 nicht verwirklichen.

69 Wie die Berufung zu Recht annimmt, gälte dasselbe indes auch dann, wenn Merkmal 1.4 dahin ausgelegt würde, dass derselbe Binärbaum zum Einsatz kommen muss wie nach Merkmal 1.3.

70 (a) Die beiden in Figur 13 dargestellten Binärbäume repräsentieren lediglich Informationen zum Partitionsmodus. Für die Codierung eines Prädiktionsmodus muss deshalb zwingend ein zweiter Binärbaum eingesetzt werden.

71 Dieser zweite Binärbaum kann zwar theoretisch aus denselben Binärwertfolgen bestehen, wie sie in Figur 13 dargestellt sind. Diese müssen aber einer anderen Bedeutung zugeordnet werden. Damit handelt es sich nicht um dieselbe Binarisierung.

72 (b) Die in Figur 14 dargestellten Binärbäume repräsentieren zwar sowohl einen Prädiktions- als auch einen Partitionsmodus und können deshalb zur Codierung beider Modi eingesetzt werden.

73 Wie bereits oben dargelegt wurde, werden die diesbezüglichen Informationen aber in einem gemeinsamen Syntaxelement codiert. Dies steht in Widerspruch zu den Merkmalen 1.3 und 1.4.

74 bb) Entgegen der Auffassung des Patentgerichts ist den Merkmalen 1.3 und 1.4 vor diesem Hintergrund nicht zu entnehmen, dass die beiden Binärbäume in irgendeiner Weise inhaltlich zusammenhängen müssen. Vielmehr genügt es, wenn für P- und B-Slices jeweils derselbe Binärbaum eingesetzt wird. Der Binärbaum zur Codierung des Prädiktionsmodus kann sich hingegen vom Binärbaum zur Codierung des Partitionsmodus in grundsätzlich beliebiger Weise unterscheiden.

75 Wie die Berufungserwiderung - wenn auch mit anderer Stoßrichtung - im Ansatz zu Recht geltend macht, läuft die Argumentation der Berufung, wonach es genügt, wenn beide Binärbäume als Teilmengen (Unterbinärbäume) eines übergeordneten Binärbaums dargestellt werden können, auf dasselbe Ergebnis hinaus. Auch unter dieser Prämisse besteht zwischen dem Inhalt der einzelnen Unterbinärbäume kein zwingender Zusammenhang.

76 Entgegen der Auffassung der Berufungserwiderung folgt daraus nicht, dass die Argumentation der Berufung fehlgeht. Sie gibt vielmehr die aus den oben dargelegten Erwägungen abgeleitete Auslegung im Ergebnis zutreffend wieder.

77 cc) Zu Recht ist das Patentgericht davon ausgegangen, dass die Merkmale 1.3 und 1.4 nicht zwingend vorgeben, dass der Inhalt der beiden Syntaxelemente unabhängig vom Inhalt des jeweils anderen sein muss, etwa dergestalt, dass das Element für den Partitionsmodus für Codiereinheiten mit Inter-Prädiktion dieselben Werte vorsehen muss wie für Codiereinheiten mit Intra-Prädiktion.

78 Wie bereits oben dargelegt wurde, formuliert Patentanspruch 1 keine näheren Anforderungen hinsichtlich der Ausgestaltung der beiden Syntaxelemente. Dies lässt die Möglichkeit offen, die Elemente so zu konzipieren, dass für Codiereinheiten mit Inter-Prädiktion andere Partitionsmodi zur Verfügung stehen als für Codiereinheiten mit Intra-Prädiktion.

79 dd) Zu Recht ist das Patentgericht davon ausgegangen, dass die Codierung gemäß den Merkmalen 1.3 und 1.4 nicht für alle Slices, Codiereinheiten oder Prädiktionseinheiten eingesetzt werden muss.

80 (a) Nach Merkmal 1.2 genügt es, wenn ein einzelner Binärbaum zumindest für einen P- und einen B-Slice eingesetzt wird.

81 Daraus ergibt sich, dass andere Slices - auch andere P- und B-Slices - nach anderen Methoden codiert werden dürfen.

82 (b) Die Merkmale 1.3 und 1.4 sehen die dort spezifizierte Codierart jeweils für eine Codiereinheit und für eine Prädiktionseinheit vor.

83 Daraus hat das Patentgericht zutreffend die Schlussfolgerung gezogen, dass es nicht ausgeschlossen ist, andere Codier- und Prädiktionseinheiten nach anderen Methoden zu codieren.

84 g) Ebenfalls zutreffend hat das Patentgericht angenommen, dass Merkmal 1.5 nicht zwingend vorgibt, dass sowohl die kleinste Inhaltseinheit (SCU) als auch größere Codiereinheiten (CU) nach den Vorgaben der Merkmale 1.3 und 1.4 codiert werden.

85 Merkmal 1.5 gibt lediglich vor, dass für die kleinste Inhaltseinheit (SCU) eine andere Binarisierung - und damit ein anderer Binärbaum im Sinne der Merkmale 1.2 bis 1.4 - eingesetzt wird als für größere Codiereinheiten (CU).

86 Diese Unterscheidung trägt dem in der Beschreibung des Streitpatents mehrfach hervorgehobenen Umstand Rechnung, dass der Partitionsmodus N x N bei bestimmten Implementationen nicht für alle Codiereinheiten eingesetzt werden darf, sondern nur für bestimmte, zum Beispiel nur für die kleinste Inhaltseinheit (SCU) (Abs. 104, 111, 113).

87 Wie das Patentgericht zu Recht angenommen hat, ergibt sich auch aus dieser Vorgabe nicht, dass alle Codiereinheiten oder zumindest jeweils eine kleinste Inhaltseinheit (SCU) und eine andere Codiereinheit gemäß den Vorgaben der Merkmale 1.3 und 1.4 codiert werden müssen. Aus dem Zusammenhang der Merkmale 1.3 bis 1.5 folgt vielmehr, dass es ausreicht, wenn zumindest eine Codier- bzw. Prädiktionseinheit in der genannten Weise codiert wird und der hierfür eingesetzte Binärbaum danach ausgewählt worden ist, ob es sich um die kleinste Inhaltseinheit (SCU) oder eine größere Codiereinheit handelt.

88 4. Das in Patentanspruch 6 geschützte Verfahren wird durch Codierschritte geprägt, die den Merkmalen 1.1 bis 1.5 entsprechen.

89 Dieser Gegenstand unterliegt deshalb derselben Beurteilung wie der Gegenstand von Anspruch 1.

90 II. Das Patentgericht hat seine Entscheidung wie folgt begründet:

91 Der Gegenstand des Patentanspruchs 1 sei nicht neu gegenüber einem von Mediatek USA eingereichten Vorschlag zum Standard HEVC (Syntax and structure for coding and utilizing partition types, Document JCTVC-E081, 5th meeting, Genf, 16. bis 23. März 2011, D2a). D2a schlage eine Codierung vor, die für P- und B-Slices denselben Binärbaum einsetze und sowohl den Prädiktions- als auch den Partitionsmodus angebe. Der Code bestehe aus drei Syntaxelementen. Das erste davon enthalte Angaben zum Prädiktions- und zum Partitionsmodus. Das zweite zeige an, ob es sich bei der aktuellen Codiereinheit (CU) um eine kleinste Informationseinheit (SCU) handle. Wenn letzteres der Fall sei, werde mit zwei weiteren Bits angezeigt, ob die Codiereinheit in vier Prädiktionsblöcke aufgeteilt sei und welcher Prädiktionsmodus zum Einsatz komme. Damit seien alle Merkmale von Patentanspruch 1 offenbart. Dass die betreffende Codierung nur für kleinste Informationseinheiten (SCU) eingesetzt werde, stehe dem nicht entgegen.

92 Der mit Hilfsantrag 1 verteidigte Gegenstand sei ebenfalls durch D2a vorweggenommen.

93 Die mit den Hilfsanträgen 2 bis 4 verteidigten Gegenstände hätten ausgehend von einem Entwurf des Standards HEVC (Working Draft 1 of High-Efficiency Video Coding, Document JCTVC-C403, 3rd meeting, Guangzhou, 7. bis 15. Oktober 2010, D3) und einem von LG Electronics zu derselben Sitzung eingereichten Vorschlag (Encoding complexity reduction for Intra prediction by Disabling NxN Partition, Document JCTVC-C21, D10a) nahegelegen. D3 offenbare eine Codierung des Prädiktions- und des Partitionsmodus in getrennten Syntaxelementen. Ausgehend davon habe es für den Fachmann, einen Diplomingenieur der Elektrotechnik oder Diplominformatiker mit Hochschulausbildung mit mehrjähriger Berufserfahrung und einschlägigen Kenntnissen auf dem Gebiet der Codierung und Decodierung von Bild- und Videodaten, nahegelegen, eine Binarisierung nach einem CABAC-Verfahren (context-adaptive binary arithmetic coding) vorzunehmen. Hierzu habe das Truncated-Unary-Format gehört, welches einer Binarisierung durch einen Binärbaum im Sinne des Streitpatents entspreche. Da D3 eine einheitliche Syntax und Semantik für P- und B-Slices vorsehe, habe ferner Anlass bestanden, diese Slices in gleicher Weise zu binarisieren. Schließlich empfehle D10a, die Codiereinheiten abhängig von ihrer Größe unterschiedlich zu binarisieren.

94 Die mit den Hilfsanträgen 3 und 4 verteidigten Gegenstände gingen zudem über den Inhalt der ursprünglich eingereichten Unterlagen hinaus.

95 III. Dies hält der Nachprüfung im Berufungsverfahren im Ergebnis stand.

96 1. Ob der Gegenstand von Patentanspruch 1 von D2a neuheitsschädlich getroffen wird, bedarf keiner Entscheidung.

97 2. Aus den im Ergebnis zutreffenden Erwägungen, die das Patentgericht im Zusammenhang mit Hilfsantrag 2 angestellt hat, folgt, dass der Gegenstand von Patentanspruch 1 ausgehend von D3 nahelag.

98 a) D3 enthält einen ersten Arbeitsentwurf für den Standard HEVC.

99 Der Entwurf enthält unter anderem Festlegungen zu Datenformaten (Kapitel 6) sowie zu Syntax und Semantik (Kapitel 7).

100 Die in Tabellenform dargestellte Syntax für Codiereinheiten (Abschnitt 7.3.6) unterscheidet zwischen I-Slices und anderen Slices (d.h. P- und B-Slices). Für letztere sind Elemente vorgesehen, die Angaben zum Prädiktionsmodus (pred_mode) und zum Partitionsmodus für Inter-Prädiktion (inter_partitioning_idc) enthalten. Für Codiereinheiten mit Intra-Prädiktion ist ein Flag (intra_split_flag) vorgesehen.

101 Die Festlegungen zur Semantik (Abschnitt 7.4.6) sehen vor, dass die Anwesenheit des Elements intra_split_flag anzeigt, dass die Codiereinheit in vier Prädiktionsblöcke aufgeteilt ist.

102 Für die Elemente pred_mode und inter_partitioning_idc sind folgende Werte vorgesehen (Hervorhebungen im Original):

Table 7-7 - Name association to prediction mode

slice_type

pred_mode

Name of pred_mode(PredMode)

I

inferred

MODE_INTRA

P and B

0

MODE_DIRECT

1

MODE_INTER

2

MODE_INTRA

inferred

MODE_SKIP

inferred

MODE_MERGE

Table 7-8 - Name association to partitioning type

inter_partioning_idc

Name of inter_partioning_idc(PartMode)

0

PART_2Nx2N

1

PART_2NxN

2

PART_Nx2N

3

PART_NxN

103 b) Damit sind nur die Merkmale 1 und 1.1 offenbart.

104 aa) Die Merkmale 1.2 bis 1.4 sind nur insoweit offenbart, als der Prädiktions- und der Partitionsmodus auf der in D3 definierten Syntax-Ebene in separaten Elementen (pred_mode; intra_split_flag/inter_partitioning_idc) zu signalisieren sind, und zwar in gleicher Weise für B- und für P-Slices.

105 Dem steht abweichend von der Auffassung der Berufung nicht entgegen, dass die Angaben zum Partitionsmodus für Codiereinheiten mit Inter-Prädiktion anders strukturiert sind als für Codiereinheiten mit Intra-Prädiktion. Wie bereits oben dargelegt wurde, enthält Patentanspruch 1 insoweit keine zwingenden Vorgaben.

106 bb) Nicht offenbart ist eine Codierung der vorgesehenen Werte mit Hilfe eines Binärbaums.

107 cc) Ebenfalls nicht offenbart ist eine besondere Codierung für den Fall, dass es sich um die kleinste Informationseinheit (SCU) handelt, wie dies Merkmal 1.5 vorsieht.

108 c) Zu Recht ist das Patentgericht zu dem Ergebnis gelangt, dass der Gegenstand von Patentanspruch 1 ausgehend von D3 nahelag.

109 aa) Zutreffend ist das Patentgericht davon ausgegangen, dass es nahelag, die in D3 vorgesehenen Werte für den Prädiktions- und den Partitionsmodus zu binarisieren, die Binarisierung für jedes in D3 für die Semantik bereits vorgesehene Element auch auf der Ebene der Binarisierung als Syntaxelement getrennt vorzunehmen und hierbei jeweils einen Binärbaum einzusetzen.

110 (1) Eine Binarisierung war schon deshalb erforderlich, weil die in D3 vorgesehenen Elemente pred_mode und inter_partitioning_idc nicht nur die Werte 0 und 1 enthalten können und deshalb in ein binäres Format umgewandelt werden müssen.

111 Der Einsatz eines Binärbaums war, wie sich schon aus D2a ergibt, ein allgemein hierfür in Betracht kommendes Mittel.

112 (2) Vor diesem Hintergrund lag es auch nahe, die Binarisierung für die in D3 vorgesehenen Syntaxelemente getrennt durchzuführen.

113 Wie etwa D2a zeigt, bestand zwar auch die Möglichkeit, einen gemeinsamen Binärbaum für zwei Parameter (Prädiktions- und Partitionsmodus) vorzusehen. Diese Vorgehensweise war aber nicht zwingend. Vielmehr bestand die Möglichkeit, die in D3 vorgesehene Struktur, bei der die beiden Angaben in getrennten Syntaxelementen enthalten sind, auch bei der Binarisierung beizubehalten. Beide Möglichkeiten bieten Vor- und Nachteile. Die Auswahl zwischen ihnen, etwa anhand der Ergebnisse von Simulationen, erfordert keine erfinderische Tätigkeit.

114 bb) Ob darüber hinaus Anlass bestand, ein CABAC-Verfahren anzuwenden und hierbei das Truncated-Unary-Verfahren einzusetzen, kann offenbleiben. Patentanspruch 1 sieht eine solche Ausgestaltung nicht zwingend vor.

115 cc) Ebenfalls zu Recht hat das Patentgericht angenommen, dass es nahelag, für P- und B-Slices dieselbe Binarisierung vorzusehen.

116 Anlass dazu ergab sich schon aus dem Umstand, dass D3 für diese beiden Slice-Arten dieselbe Syntax und Semantik vorsah.

117 Wie die Berufung anhand des vierten Arbeitsentwurfs des Standards HEVC (Working Draft 4 of High-Efficiency Video Coding, Document JCTVC-F803_d, 6th meeting, Turin, 14. bis 22. Juli 2011, D6) aufzeigt, schloss dies zwar nicht aus, dennoch eine unterschiedliche Binarisierung vorzunehmen.

118 Wie die Berufungserwiderung zutreffend ausführt, bedurfte die Auswahl zwischen diesen beiden Möglichkeiten aber keiner erfinderischen Tätigkeit. Wie die Berufungserwiderung im Einzelnen dargelegt hat, ist jede der beiden Möglichkeiten mit gewissen Vorteilen, aber auch gewissen Nachteilen verbunden. Die Auswahl einer dieser Möglichkeiten erfordert danach eine Abwägung im jeweiligen Anwendungsfall und eventuell die Durchführung von Simulationen, um die Wirkungen besser einschätzen zu können, nicht aber eine erfinderische Tätigkeit. Besondere Wirkungen, die eine einheitliche Binarisierung im Kontext des Streitpatents hervorrufen könnten, sind weder aufgezeigt noch sonst ersichtlich.

119 d) Zutreffend ist das Patentgericht ferner zu dem Ergebnis gelangt, dass es nahelag, bei der Binarisierung zwischen kleinsten Inhaltseinheiten (SCU) und anderen Codiereinheiten (CU) zu unterscheiden.

120 Anlass zu einer solchen Unterscheidung ergab sich schon daraus, dass verschiedene Dokumente wie etwa D2a und D10a vorschlagen, den Partitionstyp N x N nur für kleinste Inhaltseinheiten (SCU) vorzusehen. Ausgehend davon bot es sich im Interesse einer möglichst effizienten Codierung an, jeweils nur für diejenigen Werte eine Binärwertfolge vorzusehen, die in der jeweiligen Situation vorkommen können.

121 D2a bietet dafür ein Vorbild, weil dort zwischen den Fällen CU > SCU und CU = SCU unterschieden wird, und zwar sowohl in der dort als bekannt dargestellten Codierung als auch in der von D2a vorgeschlagenen Abwandlung.

122 e) Auch wenn danach an mehreren Stellen jeweils zwischen zwei Möglichkeiten auszuwählen war, bedurfte es keiner erfinderischen Tätigkeit, um zu der vom Streitpatent geschützten Kombination zu gelangen.

123 Die einzelnen Gestaltungsmöglichkeiten ergaben sich unabhängig voneinander. Jede Ausgestaltung war mit gewissen Vor- und Nachteilen verbunden, die als solche bekannt waren. Dass die vom Streitpatent geschützte Kombination besondere Synergieeffekte oder sonstige Vorteile bietet, ist weder aufgezeigt noch sonst ersichtlich.

124 3. Für die Hilfsanträge ergibt sich keine abweichende Beurteilung.

125 a) Der mit Hilfsantrag 1 verteidigte Gegenstand ist ebenfalls nicht patentfähig.

126 aa) Nach Hilfsantrag 1 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

1.6 wherein the first syntax element indicates intra-prediction processing or inter-prediction processing; and the second syntax element indicates CU partition shape.

127 bb) Diese Ausgestaltung lag aus den oben dargelegten Gründen ausgehend von D3 ebenfalls nahe.

128 D3 sieht getrennte Syntaxelemente für den Prädiktions- und Partitionsmodus vor.

129 b) Für Hilfsantrag 2 gilt Entsprechendes.

130 aa) Nach Hilfsantrag 2 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

1. 2aindependent of whether or not the current coding unit (CU) of the at least one P slice or the at least one B slice is the smallest CU, SCU, or not

131 bb) Diese Ausgestaltung lag ausgehend von D3 ebenfalls nahe.

132 Aus den oben aufgezeigten Gründen bestand ausgehend von D3 zwar Veranlassung, unterschiedliche Codierungen für kleinste Inhaltseinheiten (SCU) und sonstige Codiereinheiten (CU) vorzusehen. Daraus ergab sich aber kein Grund, bei einer dieser Kategorien abweichend von der in D3 vorgeschlagenen Vorgehensweise zwischen P- und B-Slices zu differenzieren.

133 c) Hilfsantrag 3 unterliegt keiner abweichenden Beurteilung.

134 aa) Nach Hilfsantrag 3 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

1.4a wherein the second syntax element is suitable for selectively encoding each of the partition modes possible for the respective CU, and

1.4b wherein the second syntax element is used independent of the partition mode of the respective CU.

135 bb) Wie das Patentgericht zutreffend ausgeführt hat, ergibt sich aus diesen zusätzlichen Merkmalen nicht, dass das Syntaxelement für den Partitionsmodus so ausgestaltet sein muss, dass es stets alle denkbaren Werte wiedergibt. Vielmehr genügt es, wenn alle Werte abgebildet werden können, die die jeweilige Codiereinheit haben kann, und wenn der Einsatz des Elements nicht vom Partitionsmodus der jeweiligen Codiereinheit abhängt.

136 cc) Wie das Patentgericht zutreffend ausgeführt hat, sind diese Anforderungen auch bei den in D3 vorgeschlagenen Syntaxelementen erfüllt.

137 Bei Codiereinheiten mit Intra-Prädiktion steht zur Anzeige des Partitionsmodus zwar nur ein einzelnes Flag zur Verfügung. Die daraus folgende Binarisierung von nur zwei Alternativen für diesen Modus reicht aber aus, um den Anforderungen der Merkmale 1.4 bis 1.4b zu entsprechen.

138 d) Für Hilfsantrag 4 gilt entsprechendes.

139 Nach Hilfsantrag 4 soll die erteilte Fassung von Patentanspruch 1 um die zusätzlichen Merkmale aus den Hilfsanträgen 2 und 3 ergänzt werden.

140 Diese Merkmale lagen aus den oben aufgezeigten Gründen auch in ihrer Kombination nahe.

141 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG und § 97 Abs. 1 ZPO.

Bacher

Hoffmann

Deichfuß

Marx

Rensen
