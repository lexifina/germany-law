---
ecli: "ECLI:DE:BGH:2025:060525UXZR49.23.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 49/23"
decided: "2025-05-06"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600052025.xml"
neuris_doknr: "KORE600052025"
---

# Bundesgerichtshof, X ZR 49/23 vom 2025-05-06

## Tenor

Die Berufung gegen das Urteil des 8. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 30. Januar 2023 wird auf Kosten der Klägerin zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 707 687 (Streitpatents), welches am 9. Mai 2012 unter Inanspruchnahme einer US-Priorität vom 11. Mai 2011 angemeldet wurde und einen Codierer für Tonsignale betrifft.

2 Patentanspruch 1, auf den 15 weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A coder of an input sound signal (s(n)), comprising:

an adaptive codebook stage structured to search an adaptive codebook (120) to find an adaptive codebook index (T) and an adaptive codebook gain (gp);

a codebook arrangement comprising:

a first codebook stage including one of a time-domain CELP codebook (130, 604, 607) and a transform-domain codebook (320, 520, 605, 606) including a calculator (303) of a transform of a transform-domain codebook target signal (300, 500) and a quantizer (305) of transform-domain coefficients (304, 504) from the transform calculator (303); and

a second codebook stage including the other of the time-domain CELP codebook (130, 604, 607) and the transform-domain codebook (320, 520, 605, 606); wherein the first and second codebook stages are structured to search the respective time-domain CELP codebook (130, 604, 607) and transform-domain codebook (320, 520, 605, 606) to find an innovative codebook index (k), an innovative codebook gain (gc), transform-domain coefficients (304, 504), and a transform-domain codebook gain (gq);

wherein the codebook stages are used in the sequence adaptive codebook stage, first codebook stage, second codebook stage for coding the input sound signal characterized in that the codebook arrangement further comprises:

a selector of an order of the time-domain CELP codebook (130, 604, 607) and the transform-domain codebook (320, 520, 605, 606) in the first and second codebook stages, respectively, as a function of at least one of (a) characteristics of the input sound signal (s(n)) and (b) a bit rate of a codec using the codebook arrangement.

3 Die Klägerin hat das Streitpatent im Umfang der Ansprüche 1 und 6 bis 16 angegriffen geltend gemacht, der angegriffene Gegenstand sei nicht patentfähig. Die Beklagte hat den angegriffenen Gegenstand in der erteilten Fassung und mit fünf Hilfsanträgen in geänderten Fassungen verteidigt. Höchst hilfsweise hat sie die Ansprüche 6 bis 16 einzeln verteidigt.

4 Das Patentgericht hat die Klage abgewiesen. Hiergegen richtet sich die Berufung der Klägerin, die ihr erstinstanzliches Begehren weiterverfolgt. Die Beklagte tritt dem Rechtsmittel mit ihren erstinstanzlichen Anträgen entgegen.

## Entscheidungsgründe

5 Die Berufung ist zulässig, hat aber in der Sache keinen Erfolg.

6 I. Das Streitpatent betrifft einen Codierer für Tonsignale.

7 1. Nach der Beschreibung des Streitpatents werden Tonsignale, insbesondere Sprachsignale, die mit niedrigen Bitraten übertragen werden, häufig nach dem CELP-Modell (Code-Excited Linear Prediction) codiert. Das hierzu eingesetzte Anregungssignal werde mit Hilfe von zwei Codebüchern erzeugt, von denen das eine als adaptives und das andere als innovatives oder festes Codebuch bezeichnet werde. In modernen Codierungssystemen finde das ACELP-Modell (Algebraic Code-Excited Linear Prediction) für das innovative Codebuch Anwendung (Abs. 2-5).

8 ACELP sei bei niedrigen Bitraten sehr effizient. Bei höheren Bitraten sei aber keine vergleichbare Erhöhung der Qualität möglich wie bei anderen Ansätzen, zum Beispiel einer Transformationscodierung und Vektorquantisierung (Abs. 6).

9 2. Vor diesem Hintergrund betrifft das Streitpatent das technische Problem, einen CELP-Codierer bereitzustellen, der eine verbesserte Codierung bei höheren Bitraten ermöglicht.

10 3. Zur Lösung dieser Aufgabe schlägt das Streitpatent in Patentanspruch 1 eine Vorrichtung vor, deren Merkmale sich wie folgt gliedern lassen:

11 0

A coder of an input sound signal (s(n)), comprising:

Ein Codierer für ein Eingangstonsignal (s(n)), umfassend:

1

an adaptive codebook stage structured to search an adaptive codebook (120),

eine adaptive Codebuchstufe, strukturiert zum Durchsuchen eines adaptiven Codebuchs (120),

1.1

to find an adaptive codebook index (T) and an adaptive codebook gain (gp);

um einen adaptiven Codebuchindex (T) und einen adaptiven Codebuchverstärkungsfaktor (gp) zu finden;

2

a codebook arrangement comprising:

eine Codebuchanordnung umfassend:

2.1

a first codebook stage

eine erste Codebuchstufe

2.1.1

including one of a time-domain CELP codebook (130, 604, 607) and a transform-domain codebook (320, 520, 605, 606)

mit einem Zeitdomänen-CELP-Codebuch (130, 604, 607) oder einem Transformationsdomänen-Codebuch (320, 520, 605, 606)

2.1.2

including a calculator (303) of a transform of a transform-domain codebook target signal (300, 500) and

mit einem Kalkulator der Transformation eines Transformationsdomänen-Codebuch-Zielsignals (300, 500) und

2.2

a second codebook stage

einer zweiten Codebuchstufe

2.2.1

including the other of the time-domain CELP codebook (130, 604, 607) and the transform-domain codebook (320, 520, 605, 606);

mit dem anderen der beiden genannten Codebücher (320, 520, 605, 606).

3

wherein the first and second codebook stages are structured to search the respective time-domain CELP codebook (130, 604, 607) and transform-domain codebook (320, 520, 605, 606) to find:

Die erste und die zweite Codebuchstufe sind zum Durchsuchen des jeweiligen Zeitdomänen-CELP-Codebuchs (130, 604, 607) und Transformationsdomänen-Codebuchs (320, 520, 605, 606) strukturiert, um folgendes zu finden:

3.1

an innovative codebook index (k), an innovative codebook gain (gc),

einen innovativen Codebuch-Index (k), einen innovativen Codebuch-Verstärkungsfaktor (gc),

3.2

transform-domain coefficients (304, 504), and a transform-domain codebook gain (gq);

Transformationsdomänen-Codebuch-Koeffizienten (304, 504) und einen Transformationsdomänen-Codebuch-Verstärkungsfaktor (gq).

4

wherein the codebook stages are used in the sequence adaptive codebook stage, first codebook stage, second codebook stage for coding the input sound signal;

Die Codebuchstufen werden in folgender Reihenfolge zur Codierung von Eingangstonsignalen eingesetzt: adaptives Codebuch, erste Codebuchstufe, zweite Codebuchstufe.

5

characterized in that the codebook arrangement further comprises:

Die Codebuchanordnung, umfasst ferner:

5.1

a selector of an order of the time-domain CELP codebook (130, 604, 607) and the transform-domain codebook (320, 520, 605, 606) in the first and second codebook stages, respectively,

einen Selektor für eine Reihenfolge des Zeitdomänen-CELP-Codebuchs (130, 604, 607) und des Transformationsdomänen-Codebuchs (320, 520, 605, 606) in der ersten bzw. zweiten Codebuchstufe,

5.2

as a function of at least one of(a) characteristics of the input sound signal (s(n)) and (b) a bit rate of a codec using the codebook arrangement.

als Funktion mindestens einer der folgenden Parameter:(a) Kenngrößen des Eingangstonsignals (s(n)) und (b) einer Bitrate eines die Codebuchanordnung verwendenden Codecs.

12 4. Verschiedene Merkmale bedürfen der Erläuterung.

13 a) Die Merkmalsgruppen 1 und 2 sehen vor, zusätzlich zu einem adaptiven und einem innovativen Codebuch, wie es insbesondere von CELP und ACELP bekannt war, ein drittes Codebuch einzusetzen, das auf einer Transformationsdomäne beruht.

14 Wie das Patentgericht zutreffend und insoweit von keiner Partei angegriffen ausgeführt hat, war eine Transformationscodierung im Stand der Technik bekannt. Sie beruht auf der Überführung der Repräsentation des Eingangssignals von der Zeitdomäne in die Frequenzdomäne, etwa mittels einer diskreten Cosinustransformation (DCT).

15 b) Zahlreiche Merkmale von Patentanspruch 1 betreffen die Reihenfolge, in der diese Codebücher zur Codierung von Eingangstonsignalen herangezogen werden.

16 aa) Nach Merkmal 4 kommt als erstes stets das adaptive Codebuch zum Einsatz, das in Merkmalsgruppe 1 näher charakterisiert ist.

17 bb) Die Reihenfolge, in der anschließend das innovative und das Transformationsdomänen-Codebuch (als "erstes" und "zweites" Codebuch) herangezogen werden, kann gemäß Merkmal 5.1 durch einen Selektor festgelegt werden.

18 Diese Festlegung beruht nach Merkmal 5.2 auf Kenngrößen des Eingangstonsignals oder auf der Bitrate des die Codebuchanordnung verwendenden Codecs. Die Berücksichtigung weiterer Parameter ist möglich.

19 Bei dem in der Beschreibung geschilderten Ausführungsbeispiel, das in der nachfolgend wiedergegebenen Figur 6 schematisch dargestellt ist, wird die Reihenfolge anhand der Bitrate und anhand einer Klassifikation des jeweiligen Rahmens festgelegt.

20 Der Selektor umfasst hierzu einen Klassifikator (601), der die einzelnen Rahmen zum Beispiel als aktive oder inaktive Sprachrahmen klassifiziert. Ausgehend von dieser Einteilung und der Bitrate des eingesetzten Codecs wird folgende Reihenfolge festgelegt (Abs. 74 -76):

21 Danach kommen bei niedrigen Bitraten nur das adaptive und das innovative Codebuch zum Einsatz. Bei höheren Bitraten wird zusätzlich das Transformationsdomänen-Codebuch herangezogen, und zwar bei aktiven Sprachrahmen als "erstes" und bei inaktiven Sprachrahmen als "zweites" Codebuch.

22 Um dies zu erreichen, ist ein erster Schalter (602) vorgesehen, dessen Stellung darüber bestimmt, welches Codebuch als "erstes" nach dem adaptiven Codebuch herangezogen wird. Die Stellung eines zweiten Schalters (603) bestimmt darüber, ob anschließend ein "zweites" Codebuch eingesetzt wird oder nicht.

23 cc) Aus der in Merkmal 4 enthaltenen Vorgabe, dass die Codebücher zur Codierung von Eingangssignalen eingesetzt werden müssen, ergibt sich, dass es nicht ausreicht, wenn zwar alle drei Codebücher kumulativ durchsucht werden, anschließend aber nur eines oder zwei davon zum Einsatz gelangen können. Vielmehr muss es möglich sein, dass das Ergebnis von allen drei Suchvorgängen in die Codierung eines einzelnen Eingangssignals - also eines Rahmens oder Unterrahmens - einfließt.

24 c) Zu Recht hat das Patentgericht entschieden, dass es zur Verwirklichung der Merkmale 4 und 5.1 nicht ausreicht, wenn das innovative und das Transformationsdomänen-Codebuch alternativ zum Einsatz gebracht werden können.

25 aa) Wie das Patentgericht und insoweit auch beide Parteien zutreffend annehmen, schließt es Patentanspruch 1 nicht aus, dass in einzelnen Situationen nach dem adaptiven Codebuch nur ein weiteres Codebuch eingesetzt wird.

26 Dies ergibt sich aus den oben aufgezeigten Darlegungen zu dem in Figur 6 dargestellten Ausführungsbeispiel, bei dem mittels des Schalters (603) festgelegt werden kann, ob ein "zweites" Codebuch eingesetzt wird oder nicht.

27 Dieses Verständnis steht zudem in Einklang mit den einleitenden Ausführungen in der Beschreibung, wonach das ACELP-Modell nur bei höheren Bitraten Qualitätsprobleme aufweist.

28 Für dieses Verständnis spricht zudem Anspruch 3, der einen zweiten Schalter (603) zum Umgehen der "zweiten" Codebuchstufe zwingend vorsieht.

29 In Patentanspruch 1 hat dies dadurch hinreichend Niederschlag gefunden, dass Merkmal 4 für den Fall, dass drei Codebücher herangezogen werden, zwar die Reihenfolge festlegt, aber nicht zwingend vorsieht, dass stets alle Codebücher heranzuziehen sind.

30 bb) Entgegen der Auffassung der Berufung reicht es danach aber nicht aus, wenn das "erste" und das "zweite" Codebuch alternativ zum Einsatz kommen können.

31 Aus den Merkmalen 4 und 5.1 ergibt sich vielmehr, dass es möglich sein muss, alle drei Codebücher nacheinander heranzuziehen.

32 Auch dieses Verständnis steht in Einklang mit der Funktion dieser Merkmale. Wie bereits dargelegt wurde, dient die ergänzende Heranziehung des Transformationsdomänen-Codebuchs dem Zweck, die Qualität bei hohen Bitraten zu verbessern. Dieser Zweck wird nach dem Streitpatent dadurch erreicht, dass dieses Codebuch neben dem adaptiven und dem innovativen Codebuch zum Einsatz kommt.

33 Die bei dem Ausführungsbeispiel nach Figur 6 bestehende und in Anspruch 3 zwingend vorgesehene Möglichkeit, die "zweite" Codebuchstufe zu umgehen, stellt im Verhältnis dazu keine alternative Ausführungsform dar, sondern eine Anforderung, die gegebenenfalls zusätzlich erfüllt sein muss. Um dieser Anforderung gerecht zu werden, reicht es nicht aus, die "zweite" Codebuchstufe stets zu umgehen, also stets nur zwei Codebücher zum Einsatz zu bringen. Vielmehr muss die Möglichkeit bestehen, je nach Betriebszustand nur zwei oder alle drei Codebücher heranzuziehen.

34 Da Patentanspruch 1 die zuletzt genannte Möglichkeit nicht zwingend vorsieht, reicht es allerdings aus, wenn stets alle drei Codebücher herangezogen werden und nur die Reihenfolge des innovativen und des Transformationsdomänen-Codebuchs geändert werden kann. Eine Ausgestaltung, bei der stets nur zwei Codebücher herangezogen werden können, genügt hingegen nicht, weil es dann an der in den Merkmalen 4 und 5.1 vorgesehenen Möglichkeit fehlt, die Reihenfolge der beiden nach dem adaptiven Codebuch eingesetzten Codebücher festzulegen.

35 cc) Entgegen der Auffassung der Berufung führt der Umstand, dass es nach Merkmal 5.2 ausreicht, die Reihenfolge auf der Grundlage der Bitrate zu bestimmen, nicht zu einer abweichenden Beurteilung.

36 Wie die Berufungserwiderung zutreffend ausführt, geht es bei der Festlegung gemäß Merkmal 5.2 nicht darum, welche Bitrate für eine bestimmte Reihenfolge der Codebücher benötigt wird, sondern darum, welche Reihenfolge für eine bestimmte Bitrate von Vorteil ist.

37 II. Das Patentgericht hat seine Entscheidung im Wesentlichen wie folgt begründet:

38 Der Gegenstand von Patentanspruch 1 sei neu.

39 Der Beitrag von Bessette, Gournay und Lefebvre für eine Arbeitsgruppe der Internationalen Standardisierungsorganisation (Proposed CE for extending the LPD mode in USAC, ISO/IEC JTC1/SC29/WG11, MPEG2010/M18481, K8) verfolge das Ziel, die Qualität des codierten Signals bei erhöhter Bitrate zu verbessern. Hierzu solle nach dem Durchsuchen des adaptiven Codebuchs und vor der Suche im innovativen Codebuch das verbleibende Restsignal durch eine neue Komponente codiert werden, die eine diskrete Cosinustransformation und eine adaptive Vektorquantisierung nutze. Damit seien zwar die Merkmale 0 bis 4 offenbart, nicht aber ein Selektor im Sinne der Merkmalsgruppe 5.

40 Der Beitrag von Bessette, Salami, Laflamme und Lefebvre (A wideband speech and audio codec at 16/24/32 kbit/s using hybrid ACELP/TCX techniques; IEEE Proceedings of Workshop on Speech Coding; Porvoo, Finnland, Juni 1999, S. 7-9, K9) schlage einen Algorithmus vor, bei dem zwischen einem ACELP- und einen TCX-Modus (transform coded and excitation) hin und her geschaltet werden könne. Damit fehle es an einer Offenbarung der Merkmale 4, 5.1 und 5.2, weil die beiden Codebücher nur alternativ, nicht aber kumulativ zum Einsatz gelangen könnten.

41 Der dieselbe Tagung wie K9 betreffende Beitrag von Schnitzler et al. (Wideband speech coding using forward/backward adaptive prediction with mixed time/frequency domain excitation, aaO S. 4-6, K10) schlage einen CELP-Breitband-Codierer mit einem Umschalter zwischen einen ACELP- und einem TCX-Codebuch vor. Auch damit sei nur ein alternativer Einsatz dieser beiden Codebücher offenbart, nicht aber ein kumulativer. Dass im Abstract dieses Beitrags von einem alternativen oder parallelen Einsatz die Rede sei, führe nicht zu einer abweichenden Beurteilung. Im Beitrag selbst werde ein paralleler Einsatz nur dergestalt beschrieben, dass für jeden Unterrahmen in beiden Codebüchern die optimalen Vektoren gesucht und anhand dieser der Modus mit dem besten Signal-zu-Rausch-Verhältnis ausgewählt werde.

42 Der Gegenstand von Patentanspruch 1 sei dem Fachmann, einem Ingenieur der Elektro-, Informations- oder Nachrichtentechnik mit Universitätsabschluss, mehrjähriger Berufserfahrung und einschlägigen Kenntnissen im Bereich der Codierung von Tonsignalen, auch nicht nahegelegt gewesen. Da keine der genannten Entgegenhaltungen den kumulativen Einsatz eines Zeitbereichs- und eines Transformationsbereichs-Codebuchs und einen Selektor zur Bestimmung der hierbei zu beachtenden Reihenfolge offenbare, führe auch ihre Zusammenschau nicht zum Gegenstand des Streitpatents. Aus dem Fachwissen habe sich ebenfalls keine Anregung in diese Richtung ergeben.

43 III. Diese Erwägungen halten der Überprüfung im zweiten Rechtszug stand.

44 1. Zu Recht hat das Patentgericht den Gegenstand von Patentanspruch 1 als neu angesehen.

45 a) K8 offenbart nicht die Merkmale 4 und 5.1.

46 aa) K8 führt aus, die Effizienz der bei einem ACELP-Codierer im LPD-Modus (linear prediction domain) eingesetzten Codebücher nehme bei höheren Bitraten ab. K8 schlägt deshalb vor, die innovativen Codebücher dieses Modus zu erweitern (Abschnitt 1).

47 Die vorgeschlagenen Modifikationen sind in der nachfolgend wiedergegebenen Figur 1 dargestellt.

48 Die zusätzlich vorgesehene Komponente wird als zweite Stufe vor (above) der ACELP-Anregung eingesetzt (Abschnitt 4). Sie nutzt zur Codierung DCT- und AVQ-Werkzeuge (discrete cosinus transformation, adaptive vector quantisation). Mit zunehmender Bitrate wird ein immer größerer Anteil an Bits für diese Komponente genutzt (Abschnitt 2 Abs. 1).

49 bb) Damit fehlt es, wie das Patentgericht zu Recht angenommen hat, an einer Offenbarung der Merkmale 4 und 5.1.

50 Ein Einsatz der zusätzlichen Komponente nach (below) dem innovativen ACELP-Codebuch ist in K8 nicht beschrieben.

51 Dass die zusätzliche Komponente nur bei höheren Bitraten eingesetzt wird, in bestimmten Situationen also nur die beiden aus ACELP bekannten Codebücher zum Einsatz gelangen, reicht zur Verwirklichung der Merkmale 4 und 5.1 aus den oben dargelegten Gründen nicht aus.

52 b) K9 offenbart die Merkmale 4 und 5.1 ebenfalls nicht.

53 aa) K9 führt aus, bei der Standardisierung von Codierern habe sich ergeben, dass keine der bekannten Techniken alle Anforderungen für Sprache und Musik bei allen Bitraten erfüllten.

54 LP-basierte Techniken könnten die Anforderungen für Sprache bei 16 kbit/s erfüllen. Sie hätten aber ein Problem mit Musiksignalen. Transformationsbasierte Techniken zeigten selbst bei 16 kbit/s eine sehr gute Leistung für Musiksignale. Bei Sprachsignalen zeigten sie aber eine schlechtere Leistung als LP-basierte Techniken, insbesondere bei 16 kbit/s (Abschnitt 1).

55 Zur Verbesserung schlägt K9 einen hybriden Algorithmus vor, der ACELP und TCX (transform-coded excitation) kombiniert. Diese Vorgehensweise ist in der nachfolgend wiedergegebenen Figur 1 schematisch dargestellt.

56 Die Einleitung von K9 fasst diese Vorgehensweise dahin zusammen, dass der Algorithmus zwischen den beiden Modi rahmenweise hin und herschalte (Abstract).

57 bb) Damit sind die Merkmale 4 und 5.1 nicht offenbart.

58 Nach der übereinstimmenden Darstellung in Figur 1 und in den einleitenden Erläuterungen werden der ACELP- und der TCX-Modus nur alternativ eingesetzt. Hinweise auf einen kumulativen Einsatz sind K9 nicht zu entnehmen.

59 c) Für K10 ergibt sich keine abweichende Beurteilung.

60 aa) K10 führt aus, durch Kombination von CELP und Subband-Codierung habe sich bei Bitraten bis zu 16 kbit/s eine hohe Sprachqualität ergeben. Für Musiksignale bedürfe es aber zusätzlicher Verbesserungen.

61 Hierfür kämen insbesondere der Einsatz von TCX (transform coded excitation) und eine Erhöhung der spektralen Auflösung des Synthesefilters in Betracht. K10 schlägt vor, beide genannten Techniken einzusetzen (S. 4 links).

62 Die vorgeschlagene Vorgehensweise ist in der nachfolgend wiedergegebenen Figur 2 schematisch dargestellt.

63 Zunächst kommt das adaptive Codebuch zum Einsatz. Bei einer Anregung in der Zeitdomäne wird danach ein ACELP-Codebuch eingesetzt. Alternativ gelangt ein auf diskreter Cosinustransformation beruhendes Codebuch der Frequenzdomäne zum Einsatz.

64 Wenn entweder der ACELP- oder der TCX-Modus erzwungen werde, führe dies zu einer vergleichbaren Qualität. Wenn dem Codierer ermöglicht werde, zwischen diesen beiden Codebüchern auf der Grundlage des maximalen Signal-Rausch-Verhältnisses (signal to noise ratio, SNR) auszuwählen, komme bei mehr als der Hälfte der Blöcke das TCX-Codebuch zum Einsatz. Dies führe zu einer erheblichen Qualitätssteigerung (S. 6 links).

65 In der Einleitung wird dies dahin zusammengefasst, die Anregung auf der Grundlage der Frequenzdomäne könne alternativ oder parallel zu einem Codebuch auf der Grundlage der Zeitdomäne eingesetzt werden (Abstract).

66 bb) Zu Recht hat das Patentgericht entschieden, dass die Merkmale 4 und 5.1 damit nicht offenbart sind.

67 (1) Sowohl nach der zeichnerischen Darstellung in Figur 2 als auch nach den hierauf bezogenen Erläuterungen kann der Codierer nach dem Einsatz des adaptiven Codebuchs zwischen zwei unterschiedlichen Codebüchern auswählen. Ein kumulativer Einsatz dieser beiden Codebücher ist nicht beschrieben.

68 (2) Vor diesem Hintergrund hat das Patentgericht zutreffend entschieden, dass der einleitende Hinweis, die Codebücher könnten alternativ oder parallel eingesetzt werden, einen kumulativen Einsatz nicht eindeutig offenbart.

69 Dieser Hinweis lässt nicht erkennen, dass das in K10 vorgeschlagene Verfahren eine zusätzliche Möglichkeit umfasst, die in den Detailausführungen nicht erwähnt ist. Angesichts dessen ist jedenfalls nicht auszuschließen, dass als parallele Verarbeitung derjenige Modus gemeint ist, bei dem TCX als Alternative nicht fest vorgegeben ist, sondern der Codierer bei jedem Block anhand des Signal-Rausch-Verhältnisses zwischen den beiden Codebüchern wählen kann.

70 2. Ebenfalls zu Recht hat das Patentgericht entschieden, dass der Gegenstand von Patentanspruch 1 patentfähig ist.

71 a) Entgegen der Auffassung der Berufung ergab sich ausgehend von K10 keine Anregung, einen kumulativen Einsatz aller drei Codebücher mit der Möglichkeit zu einem Wechsel der Reihenfolge zwischen dem "ersten" und dem "zweiten" Codebuch zu kombinieren.

72 aa) Dabei kann zugunsten der Berufung unterstellt werden, dass ausgehend von K10 Anlass bestand, angesichts der im Laufe der Zeit größer gewordenen Bedarfs nach weiteren Möglichkeiten zur Optimierung der Codierung bei höheren Bitraten zu suchen.

73 Hierzu ergab sich aus K8 die Anregung, jedenfalls bei höheren Bitraten alle drei Codebücher einzusetzen.

74 bb) Entgegen der Auffassung der Berufung lag es aber auch unter diesem Gesichtspunkt nicht nahe, die in K8 offenbarte Vorgehensweise im Wege eines "Analogieschlusses" aus K10 dahin zu ergänzen, dass die Reihenfolge, in der die beiden zusätzlichen Codebücher eingesetzt werden, anhand von Kenngrößen des Eingangstonsignals oder der Bitrate des eingesetzten Codecs geändert wird.

75 In diesem Zusammenhang kann dahingestellt bleiben, ob das in K10 als Kriterium für die Auswahl zwischen zwei Codebüchern herangezogene Signal-Rausch-Verhältnis als Kenngröße des Eingangssignals im Sinne von Merkmal 5.2(a) angesehen werden kann. Selbst wenn dies zu bejahen wäre, legt die in K10 vorgeschlagene Heranziehung dieses Parameters als Kriterium für die Auswahl eines zusätzlichen Codebuchs nicht nahe, ihn bei dem in K8 vorgeschlagenen Verfahren zur Bestimmung der Reihenfolge heranzuziehen, in der die beiden zusätzlichen Codebücher eingesetzt werden.

76 Nach den Feststellungen des Patentgerichts gehörte es allerdings zum Fachwissen, dass es vorteilhaft ist, zuerst dasjenige Codebuch einzusetzen, das den größeren Beitrag liefert. Im Stand der Technik ist hieraus jedoch lediglich die Schlussfolgerung gezogen worden, das adaptive Codebuch als erstes einzusetzen, weil es in der Regel einen größeren Beitrag liefert als ein festes Codebuch, nicht hingegen, die Reihenfolge dieser Codebücher anhand von Kenngrößen des jeweiligen Eingangstonsignals situationsabhängig zu ändern. Vor diesem Hintergrund bedurfte es einer konkreten Anregung, das in K10 vorgeschlagene situationsabhängige Vorgehen nicht nur für die Auswahl zwischen zwei Codebüchern in Betracht zu ziehen, sondern auch für die Festlegung der Reihenfolge von zwei kumulativ herangezogenen Codebüchern. Eine solche Anregung ergab sich aus K10 und K8 auch bei einer Zusammenschau dieser Entgegenhaltungen nicht.

77 b) Entgegen der Auffassung der Berufung kann ausgehend von K8 eine erfinderische Tätigkeit nicht deshalb verneint werden, weil die vom Streitpatent vorgesehene Möglichkeit zur Änderung der Reihenfolge als technisch sinnlos anzusehen wäre.

78 Dem diesbezüglichen Vorbringen der Klägerin ist lediglich zu entnehmen, dass die mit einer Änderung der Reihenfolge erzielbaren Vorteile auch auf anderem Weg erzielt werden können. Selbst wenn dies zutrifft, kann der vom Streitpatent geschützte Weg nicht als technisch sinnlos angesehen werden. Eine technische Wirkung, die zur Bejahung der Patentfähigkeit führen kann, liegt schon dann vor, wenn im Vergleich zum Stand der Technik ein anderer Weg aufgezeigt wird, um ein bestimmtes Ziel zu erreichen (BGH, Beschluss vom 30. Juni 2015 - X ZB 1/15, GRUR 2015, 983 Rn. 31 - Flugzeugzustand). Jedenfalls einen solchen Weg zur effizienten Codierung zeigt das Streitpatent auf.

79 c) Aus K31 ergeben sich keine weitergehenden Anregungen.

80 aa) K31 befasst sich mit der Vektorquantisierung von LSP-Parametern (line spectral pair).

81 (1) K31 führt aus, ein CELP-Codierer führe eine lineare prädiktive Analyse durch, um geeignete lineare Prädiktionskoeffizienten (LPC) zu finden. Um solche Koeffizienten zu codieren, könnten sie in LSP umgewandelt werden. LSP würden häufig einer Vektorquantisierung unterzogen. Hierzu werde ein Codebuch eingesetzt (Abs. 3). Bekannt sei auch eine mehrstufige Quantisierung, bei der auf einer ersten Stufe unterschiedliche Codebücher für breitbandige und schmalbandige LSP eingesetzt würden (Abs. 4 f.). Auf der zweiten Stufe komme hingegen ein gemeinsames Codebuch zum Einsatz; dies könne zu Ungenauigkeiten führen (Abs. 6).

82 (2) Zur Verbesserung schlägt K31 vor, auf der zweiten Stufe mehrere Codebücher einzusetzen, wie dies etwa in der nachfolgend wiedergegebenen Figur 2 dargestellt ist.

83 (3) Die Nutzung eines solchen Vektorquantisierers in einem CELP-Codierer ist in der nachfolgend wiedergegebenen Figur 7 dargestellt (Abs. 89).

84 Bei dieser Ausgestaltung wird ein Vektorquantisierer (100) nach dem Vorbild von Fig. 2 als Quantisierabschnitt (403) eingesetzt (Abs. 92).

85 (4) Eine alternative Ausführungsform eines Vektorquantisierers (500) ist in der nachfolgend wiedergegebenen Figur 11 dargestellt.

86 Bei dieser Ausgestaltung kann die Reihenfolge, in der die Codebücher (506, 507) auf der zweiten Stufe herangezogen werden, durch einen Schalter (505) ausgewählt werden (Abs. 156). Dieser Schalter wird gesteuert durch zwei Bestimmungseinheiten (502, 503, Abs. 151).

87 bb) Wie auch die Berufung im Ansatz nicht verkennt, ist der Gegenstand von Patentanspruch 1 dadurch schon deshalb nicht offenbart, weil Figur 11 keinen CELP-Codierer zeigt, sondern einen Vektorquantisierer.

88 cc) Entgegen der Auffassung der Berufung ergab sich aus K31 keine Anregung, den in Figur 11 dargestellten Schalter (505) auch in einem modifizierten CELP-Codierer nach dem Vorbild von K8, K9 oder K10 einzusetzen.

89 K31 lässt nicht erkennen, dass die dort als Option geschilderte Änderung der Reihenfolge auch im Zusammenhang mit einer CELP-Codierung unter Einsatz von drei Codebüchern von Vorteil sein kann. Mangels eines solchen Hinweises lag es nicht nahe, dieses einzelne Lösungselement auf die in K8, K9 oder K10 vorgeschlagenen Systeme zu übertragen.

90 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG in Verbindung mit § 97 Abs. 1 ZPO.

Bacher

Deichfuß

Marx

Rensen

von Pückler
