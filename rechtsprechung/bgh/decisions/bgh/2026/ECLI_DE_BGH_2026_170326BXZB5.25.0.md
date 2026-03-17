---
ecli: "ECLI:DE:BGH:2026:170326BXZB5.25.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZB 5/25"
decided: "2026-03-17"
typ: "Beschluss"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE300032026.xml"
neuris_doknr: "KORE300032026"
---

# Bundesgerichtshof, X ZB 5/25 vom 2026-03-17

## Leitsatz

Automatisierte Bestimmung von Untersuchungsergebnissen

Der Ausschlusstatbestand des § 2a Abs. 1 Nr. 2 Satz 1 Fall 2 PatG ist nur dann erfüllt, wenn alle zur Diagnose gehörenden Verfahrensschritte am menschlichen oder tierischen Körper vorgenommen werden (ebenso EPA, Entscheidung vom 16. Dezember 2005 - G 1/04, GRUR Int. 2006, 514 Abs. 6.4.4 - Diagnostizierverfahren).57 58

## Tenor

Auf die Rechtsbeschwerde der Anmelderin wird der Beschluss des 18. Senats (Technischen Beschwerdesenats) des Bundespatentgerichts vom 28. Januar 2025 aufgehoben.

Die Sache wird zur anderweiten Verhandlung und Entscheidung an das Bundespatentgericht zurückverwiesen.

## Gründe

1 A. Die Anmelderin begehrt die Erteilung eines Patents für ein Verfahren und ein System zur automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz.

2 Die Anmeldung ist am 9. Februar 2022 beim Patentamt eingereicht worden. Die darin formulierten Ansprüche 1 und 2, auf die neun Ansprüche zurückbezogen sind, lauten:

1. Verfahren zur automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz (S, S`) aus mehreren zeitlich aufeinanderfolgenden Frames (F0, F, F1, F2, F3), das Verfahren umfassend die Schritte:

- Ermittlung von Befund-Kandidaten (K) in Form von zusammenhängenden Bildbereichen in den einzelnen Frames (F0, F, F1, F2, F3) für einen vorgegebenen Befund,

für eine Anzahl der Befund-Kandidaten (K):

- Ermittlung für einen Befund-Kandidaten (K) in einem Frame (F) welche Kandidaten-Bildereiche (B) in anderen Frames (F0, F1, F2, F3) dem Befund-Kandidaten (K) entsprechen,

- Ermittlung, ob die Kandidaten-Bildereiche (B) des Befund-Kandidaten (K) in den anderen Frames (F0, F1, F2, F3) mit anderen Befund-Kandidaten (K) überlappen,

- Erzeugung eines Graphen (G) mit den ermittelten Befund-Kandidaten (K) der Frames (F0, F, F1, F2, F3) als Knoten (N) und den ermittelten Überlappungen als Kanten (E),

- Erzeugung von Gemeinschaften (C, C`) aus mittels Kanten (E) verbundener Knoten (N), wobei Knoten (N) zu einer Gemeinschaft (C, C`) zusammengefasst werden.

2. Verfahren nach Anspruch 1, wobei die Gemeinschaften (C, C`) ausgegeben werden oder für weitere Untersuchungen verwendet werden, bevorzugt im Rahmen einer Röntgen-Angiographie-Untersuchung, insbesondere für eine automatische Stenoseerkennung oder Stenosebewertung, eine quantitative Coronare Angiographie oder eine Lungensegmentierung.

3 Anspruch 12, auf den zwei Ansprüche zurückbezogen sind, schützt sinngemäß ein System, das zur Ausführung dieses Verfahrens geeignet ist.

4 Nach einem Hinweis des Patentamts hat die Anmelderin Anspruch 2 hilfsweise dahin geändert, dass der mit "insbesondere" beginnende Satzteil entfällt.

5 Das Patentamt hat den Hauptantrag zurückgewiesen und das Patent nur in der Fassung des Hilfsantrags erteilt. Mit ihrer dagegen gerichteten Beschwerde hat die Patentinhaberin ihren Hauptantrag weiterverfolgt.

6 Das Patentgericht hat die Beschwerde zurückgewiesen. Dagegen richtet sich die vom Patentgericht zugelassene Rechtsbeschwerde der Anmelderin, die weiterhin eine Patenterteilung gemäß Hauptantrag anstrebt.

7 B. Die kraft Zulassung statthafte und auch im Übrigen zulässige Rechtsbeschwerde hat in der Sache Erfolg und führt zur Zurückverweisung der Sache an das Patentgericht.

8 I. Die Anmeldung betrifft ein Verfahren und ein System zur automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz, insbesondere in einer Angiographie-Sequenz.

9 1. Nach der Beschreibung der Patentanmeldung dient eine Angiographie dazu, Gefäße wie Blutgefäße mittels diagnostischer Bildgebungsverfahren (Röntgen oder Magnetresonanztomographie) in Aufnahmen (sog. Frames) radiologisch darzustellen (Abs. 3).

10 Bei einer koronaren Angiographie könnten auf diese Weise Informationen aus mehreren Ansichten während des gesamten Herzzyklus erhoben, Befunde, wie Stenosen, d.h. Verengungen der Blutgefäße, zuverlässig verfolgt und die besten Frames für eine genaue Analyse (Erkennung, Einstufung, Lokalisierung, Qualitative Comparative Analyse, weitere Bewertung) durch medizinische Experten (manuell) ausgewählt werden (Abs. 5).

11 Nach dem Stand der Technik sei zwar eine automatisierte Untersuchung einzelner Frames möglich, nicht aber eine automatisierte Auswertung der gesamten Bildsequenz (Abs. 6 f.).

12 Die Anmeldung betrifft vor diesem Hintergrund das technische Problem, die automatisierte Auswertung einer gesamten Bildsequenz zu ermöglichen.

13 2. Zur Lösung schlägt die Anmeldung in den Ansprüchen 1 und 2 des Hauptantrages ein Verfahren vor, dessen Merkmale sich wie folgt gliedern lassen (Unterschiede zum Hilfsantrag sind hervorgehoben):

14 1.1

Verfahren zur automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz (S, S') aus mehreren zeitlich aufeinanderfolgenden Frames (F0, F, F1, F2, F3), das Verfahren umfassend die Schritte:

1.2

- Ermittlung von Befund-Kandidaten (K) in Form von zusammenhängenden Bildbereichen in den einzelnen Frames (F0, F, F1, F2, F3) für einen vorgegebenen Befund,

für eine Anzahl der Befund-Kandidaten (K):

1.3

- Ermittlung für einen Befund-Kandidaten (K) in einem Frame (F), welche Kandidaten-Bildbereiche (B) in anderen Frames (F0, F1, F2, F3) dem Befund-Kandidaten (K) entsprechen,

1.4

- Ermittlung, ob die Kandidaten-Bildbereiche (B) des Befund-Kandidaten (K) in den anderen Frames (F0, F1, F2, F3) mit anderen Befund-Kandidaten (K) überlappen,

1.5

- Erzeugung eines Graphen (G) mit den ermittelten Befund-Kandidaten (K) der Frames (F0, F, F1, F2, F3) als Knoten (N) und den ermittelten Überlappungen als Kanten (E),

1.6

- Erzeugung von Gemeinschaften (C, C') aus mittels Kanten (E) verbundenen Knoten (N), wobei Knoten (N) zu einer Gemeinschaft (C, C') zusammengefasst werden.

15 2.1

Verfahren nach Anspruch 1,

2.2

wobei die Gemeinschaften (C, C') ausgegeben werden oder für weitere Untersuchungen verwendet werden,

2.3

bevorzugt im Rahmen einer Röntgen-Angiographie-Untersuchung,

2.4

insbesondere für eine automatische Stenoseerkennung oder Stenosebewertung, eine quantitative Coronare Angiographie oder eine Lumensegmentierung.

16 3. Einige Merkmale bedürfen näherer Erläuterung.

17 a) Die in den Merkmalen 1.2 bis 1.6 vorgesehenen Verfahrensschritte sind in der nachfolgend wiedergegebenen Figur 1 schematisch dargestellt.

18 b) Eine Bildsequenz (S) im Sinne von Merkmal 1 besteht aus Frames (F).

19 Frames sind nach der insoweit maßgeblichen Definition in der Beschreibung Einzelbilder (Abs. 10).

20 Bevorzugt bilden die Frames eine medizinische Bildsequenz wie etwa eine Angiographie-Sequenz. Ferner zeigen sie dasselbe Motiv und sind ohne Bewegung der Aufnahmeeinheit erstellt worden. In Betracht kommen 2D-Bilder wie etwa Röntgen- oder Ultraschallbilder, aber auch 3D-Bilder wie zum Beispiel rekonstruierte CT- oder MRT-Aufnahmen (Abs. 10). All dies ist nach den Ansprüchen 1 und 2 jedoch nicht zwingend.

21 Die Anzahl der Frames pro Sequenz ist in den Ansprüchen 1 und 2 ebenfalls nicht festgelegt. Aus dem Zusammenhang mit den Merkmalen 1.3 und 1.4 ergibt sich lediglich, dass eine Sequenz mindestens zwei Frames enthalten muss.

22 c) Entgegen der Auffassung des Patentgerichts gehört die Erzeugung der Bildsequenz nicht zu dem Verfahren nach den Ansprüchen 1 und 2.

23 Merkmal 1 setzt zwar voraus, dass eine Bildsequenz erzeugt worden ist. Die Ansprüche 1 und 2 sehen diesen Vorgang jedoch nicht als Teil des beanspruchten Verfahrens vor, sondern lediglich als Ausgangspunkt und Objekt der weiteren Verfahrensschritte.

24 Die Ansprüche 1 und 2 lassen auch offen, auf welche Weise und zu welchem Zeitpunkt die Bildsequenz entstanden ist. Selbst der zeitliche Abstand zwischen der Aufnahme der einzelnen Frames ist nicht festgelegt.

25 Ebenfalls nicht erforderlich ist, dass die Verfahrensschritte an demselben Ort durchgeführt werden, an dem die Bildsequenz aufgenommen wurde. Die Beschreibung gibt als bevorzugte Ausführungsform für ein System zur Durchführung des Verfahrens einen Cloud-Dienst an, d. h. eine IT-Infrastruktur, die Daten und Befehle über ein Netzwerk entgegennimmt (Abs. 68 f.).

26 d) Befund-Kandidaten (K) im Sinne von Merkmal 1.2 sind zusammenhängende Bildbereiche in den einzelnen Frames, die mit einiger Wahrscheinlichkeit auf einen vorgegebenen Befund hinweisen (Abs. 14, 72 und 93).

27 Vorzugsweise handelt es sich um medizinische Befunde, insbesondere von Pathologien. In Betracht kommen aber auch beliebige Befunde über andere anatomische Merkmale, zum Beispiel Bifurkationen in Gefäßen (Abs. 34).

28 e) Die weiteren Verfahrensschritte beruhen auf der so genannten Graphentheorie und dienen dem Zweck, Überlappungen zwischen Befund-Kandidaten in den einzelnen Frames darzustellen.

29 aa) Diese Verfahrensschritte können nach Anspruch 1 für alle Befund-Kandidaten (K) oder für einzelne davon durchgeführt werden.

30 Nach der Beschreibung ist das Verfahren besonders effektiv, wenn alle Befund-Kandidaten einbezogen werden. Auch dann können bei rechenintensiven Auswertungen einzelne Kandidaten ignoriert werden, zum Beispiel wenn sie auf offensichtlichen Fehleinschätzungen beruhen (Abs. 15).

31 bb) Nach Merkmal 1.4 werden die in die Auswertung einbezogenen Frames darauf untersucht, ob sich darin gefundene Befund-Kandidaten (K) überlappen, d. h. auch in entsprechenden Bildbereichen anderer Frames finden.

32 Hierbei kann auch der Grad einer festgestellten Überlappung erfasst werden (Abs. 75, 97).

33 cc) Um die Feststellung von Überlappungen zu ermöglichen, wird nach Merkmal 1.3 vorab ermittelt, welchen Bildbereich der jeweils untersuchte Kandidat in den anderen Frames einnehmen würde. Dies ist erforderlich, weil zwischen der Aufnahme der einzelnen Frames eine Bewegung stattgefunden und dies zur Folge haben kann, dass sich Form oder Ort des Kandidaten verändern (Abs. 74, 95).

34 dd) Ermittelte Überlappungen zwischen Befund-Kandidaten (K) werden gemäß Merkmal 1.5 in einem Graphen (G) dargestellt, d. h. einer grafischen Struktur mit Knoten (N) und diese verbindenden Kanten (E).

35 Hierbei werden die Befund-Kandidaten aus den einzelnen Frames als Knoten (N) und die ermittelten Überlappungen als Kanten (E) dargestellt.

36 Den Kanten kann optional eine Stärke zugewiesen werden, die den Grad der Überlappung wiedergibt (Abs. 21).

37 ee) Nach Merkmal 1.6 werden durch Kanten (E) verbundene Knoten (N) zu Gemeinschaften (C, C') zusammengefasst.

38 Eine solche Gemeinschaft kann aus allen Knoten bestehen, die unmittelbar oder mittelbar (Abs. 101) durch Kanten miteinander verbunden sind. Alternativ können nur solche Kanten berücksichtigt werden, deren Stärke einen bestimmten Schwellenwert überschreitet (Abs. 22). Auch alleinstehende Knoten können optional als Gemeinschaft angesehen werden (Abs. 79).

39 f) Anspruch 2 sieht in Merkmal 2.2 vor, dass die Gemeinschaften (C, C') ausgegeben oder für weitere Untersuchungen verwendet werden.

40 aa) Die Art der Untersuchung ist in Anspruch 2 - ebenso wie in Anspruch 1 - nicht festgelegt.

41 Merkmal 2.3 führt als bevorzugt eine Röntgen-Angiographie-Untersuchung an, enthält aber keine diesbezügliche Festlegung.

42 bb) Das Ziel der Untersuchung ist ebenfalls nicht festgelegt.

43 Merkmal 2.4 führt als Beispiele eine Stenoseerkennung oder -bewertung, eine quantitative koronare Angiographie und eine Lumensegmentierung an, enthält aber ebenfalls keine zwingende Vorgabe.

44 II. Das Patentgericht hat seine Entscheidung, soweit für das Rechtsbeschwerdeverfahren von Bedeutung, im Wesentlichen wie folgt begründet:

45 Zwar sei der Gegenstand des Anspruchs 1 neu und beruhe auf erfinderischer Tätigkeit. Die Erfindung sei aber nach § 2a Abs. 1 Nr. 2 Satz 1 PatG vom Patentschutz ausgeschlossen, weil sie ein Diagnostizierverfahren betreffe, das am menschlichen oder tierischen Körper vorgenommen werde.

46 Ein Diagnostizierverfahren gemäß § 2a Abs. 1 Nr. 2 Satz 1 PatG setze sich aus der Untersuchung mit Datenerhebung am menschlichen oder tierischen Körper (Schritt 1), dem Vergleich dieser Daten mit Normwerten (Schritt 2), der Feststellung einer Abweichung bei diesem Vergleich (Schritt 3) und der Deutung der Abweichung als krankhafter Zustand (Schritt 4) zusammen. Der Patentierungsausschluss greife bereits dann, wenn der erste Schritt, d.h. die Untersuchung mit Datenerhebung, am menschlichen oder tierischen Körper vorgenommen werde.

47 Die Erfindung verwirkliche nicht nur die Schritte 2 bis 4, sondern auch den Schritt 1. Die in Anspruch 1 vorgesehene Bildsequenz werde mittels bildgebender Verfahren am menschlichen oder tierischen Körper erzeugt. Die Erfindung umfasse eine entsprechende Untersuchung des Patienten zwar nicht, setze diesen Schritt aber denknotwendig voraus.

48 Hierbei sei auch zu berücksichtigen, dass das Patentgesetz anders als Art. 84 EPÜ nicht fordere, alle wesentlichen Merkmale, die für die deutliche und vollständige Definition der Erfindung notwendig seien, in den Anspruch aufzunehmen. Daraus ergebe sich die Gefahr, dass das Patentierungsverbot schon durch Weglassen eines Merkmals umgangen werden könnte.

49 Anders als in einem vom Bundesgerichtshof entschiedenen Fall (BGH, Beschluss vom 31. August 2010 - X ZB 9/09, BGHZ 187, 20 = GRUR 2010, 1081 Rn. 11 - Bildunterstützung bei Katheternavigation) lasse eine sachgemäße Auslegung der Offenlegungsschrift im Streitfall eine andere Verwendung der Erfindung als die Feststellung krankhaft veränderter Gefäße nicht erkennen.

50 III. Dies hält der rechtlichen Überprüfung nicht stand.

51 Entgegen der Auffassung des Patentgerichts ist das beanspruchte Verfahren nicht nach § 2a Abs. 1 Nr. 2 Satz 1 Fall 2 PatG von der Patentierung ausgeschlossen.

52 1. Der Ausschlusstatbestand des § 2a Abs. 1 Nr. 2 Satz 1 Fall 2 PatG ist nur dann erfüllt, wenn alle zur Diagnose gehörenden Verfahrensschritte am menschlichen oder tierischen Körper vorgenommen werden.

53 a) Wie das Patentgericht im Ansatz zutreffend angenommen hat, erfasst ein Diagnostizierverfahren im Sinne von § 2a Abs. 1 Nr. 2 Satz 1 Fall 2 PatG in der Regel die Schritte der Untersuchung und Datenerhebung, den Vergleich der erhobenen Daten mit Normwerten und die Bewertung des Vergleichsergebnisses.

54 Dies entspricht den Schritten, die die Große Beschwerdekammer des Europäischen Patentamtes (EPA, Entscheidung vom 16. Dezember 2005 - G 1/04, GRUR Int. 2006, 514 Abs. 5; ebenso zu § 5 Abs. 2 PatG a.F.: BGH, Beschluss vom 31. August 2010 - X ZB 9/09, BGHZ 187, 20 = GRUR 2010, 1081 Rn. 22 f. - Bildunterstützung bei Katheternavigation) als charakteristisch für ein Diagnostizierverfahren im Sinne von Art. 52 Abs. 4 EPÜ a.F. angesehen hat:

(i) Untersuchungsphase mit der Sammlung von Daten,

(ii) Vergleich dieser Daten mit den Normwerten,

(iii) Feststellung einer signifikanten Abweichung, d.h. eines Symptoms, bei diesem Vergleich,

(iv) Zuordnung der Abweichung zu einem bestimmten Krankheitsbild (deduktive human- oder veterinärmedizinische Entscheidungsphase).

55 b) Diese Übereinstimmung beruht darauf, dass die Voraussetzungen, unter denen Diagnostizierverfahren nach dem bis 12. Dezember 2007 geltenden Recht (Art. 52 Abs. 4 EPÜ a.F., § 5 Abs. 2 PatG a.F.) als nicht gewerblich anwendbare Erfindungen gelten und nach neuem Recht (Art. 53 Buchst. c EPÜ, § 2a Abs. 2 Nr. 2 PatG) von der Patentierung ausgeschlossen sind, im Patentgesetz in gleicher Weise definiert sind wie im Europäischen Patentübereinkommen.

56 Der vom Gesetzgeber bewusst angestrebte Gleichklang (BT-Drucks. 7/3712 S. 28; BT-Drucks. 16/4382 S. 11) hat zur Folge, dass das Patentgesetz insoweit in gleichem Sinne auszulegen ist wie das Europäische Patentübereinkommen. Inhaltlich besteht auch kein Unterschied zwischen dem früher und dem seit 13. Dezember 2007 geltenden Recht (BGH, Beschluss vom 31. August 2010 - X ZB 9/09, BGHZ 187, 20 = GRUR 2010, 1081 Rn. 25 ff. - Bildunterstützung bei Katheternavigation).

57 c) Die Große Beschwerdekammer des Europäischen Patentamts hat entschieden, dass der Ausschlusstatbestand des § 52 Abs. 4 EPÜ a.F. nur dann erfüllt ist, wenn alle technischen Verfahrensschritte eines Diagnostizierverfahrens am menschlichen oder tierischen Körper vorgenommen werden müssen (EPA, Entscheidung vom 16. Dezember 2005 - G 1/04, GRUR Int. 2006, 514 Abs. 6.4.4).

58 Für § 2a Abs. 1 Nr. 2 PatG gilt dasselbe.

59 aa) Die Große Beschwerdekammer hat ihre Beurteilung insbesondere auf die Erwägung gestützt, eine breitere Auslegung, nach der es ausreicht, wenn einer der genannten Schritte am menschlichen oder tierischen Körper vorgenommen werden muss, würde gegen den Grundsatz der Rechtssicherheit verstoßen.

60 Ob diese Erwägung für sich genommen ausreicht, um zu einer engeren Auslegung der Vorschrift zu gelangen, bedarf keiner Entscheidung.

61 Die Auffassung der Großen Beschwerdekammer ist jedenfalls deshalb zutreffend, weil sie mit dem Wortlaut der Vorschrift im Einklang steht und weil Ausnahmevorschriften grundsätzlich eng auszulegen sind.

62 bb) Entgegen der Auffassung des Patentgerichts führt dieses Verständnis nicht dazu, dass alle technischen Verfahren, die über ärztliches Hören, Sehen, Riechen und Tasten hinausgehen, vom Patentierungsverbot ausgenommen sind.

63 Ein Verfahrensschritt muss am menschlichen oder tierischen Körper vorgenommen werden, wenn er eine Wechselwirkung mit dem menschlichen oder tierischen Körper beinhaltet, die zwangsläufig dessen Präsenz voraussetzt (EPA, Entscheidung vom 16. Dezember 2005 - G 1/04, GRUR Int. 2006, 514 Abs. 6.4.4).

64 Eine solche Wechselwirkung kann auch bei anderen technischen Verfahren als den vom Patentgericht genannten erforderlich sein. Auch bei einer engen Auslegung ist der Ausschlusstatbestand mithin nicht bedeutungslos.

65 cc) Die Überlegungen, die das Patentgericht auf der Grundlage seines abweichenden Verständnisses zur möglichen Gefahr von Umgehungen des Ausschlusstatbestandes angestellt hat, führen ebenfalls nicht zu einer abweichenden Beurteilung.

66 Auch auf der Grundlage des oben aufgezeigten Verständnisses mag für den Anmelder allerdings die Möglichkeit bestehen, ein Diagnostizierverfahren, dessen Schritte durchweg am menschlichen oder tierischen Körper vorgenommen werden, um zusätzliche Schritte zu ergänzen, die diese Voraussetzung nicht erfüllen.

67 Sofern Maßnahmen hinzugefügt werden, die den oben aufgeführten Schritten eines Diagnostizierverfahrens zeitlich vor- oder nachgelagert sind, vermag dies jedoch schon deshalb nicht zur Patentierbarkeit zu führen, weil das Erfordernis der Vornahme am menschlichen oder tierischen Körper nur für die zum Diagnostizierverfahren gehörenden Schritte gilt. Nichts anderes gilt für Schritte, die zwar während des Diagnostizierverfahrens erfolgen, aber nicht in funktionellem Zusammenhang damit stehen.

68 2. Bei Anlegung dieses rechtlichen Maßstabs ist der Tatbestand von § 2a Abs. 1 Nr. 2 Satz 1 Fall 2 PatG im Streitfall nicht erfüllt.

69 Wie das Patentgericht zutreffend angenommen hat, werden die in den Merkmalen 1.2 bis 1.6 vorgesehenen Schritte nicht am menschlichen oder tierischen Körper vorgenommen. Damit ist der Ausschlusstatbestand nicht erfüllt.

70 Dies gälte selbst dann, wenn in diesem Zusammenhang die Erstellung einer Bildsequenz als weiterer Verfahrensschritt zu berücksichtigen wäre, obwohl ihn die Ansprüche 1 und 2 nur voraussetzen, nicht aber als Teil des beanspruchten Verfahrens vorsehen.

71 IV. Die Sache ist deshalb unter Aufhebung der angefochtenen Entscheidung zur anderweiten Verhandlung und Entscheidung an das Patentgericht zurückzuverweisen (§ 108 Abs. 1 PatG).

72 V. Eine Kostenentscheidung und eine Festsetzung des Gegenstandswerts sind nicht veranlasst (§ 109 PatG; § 63 GKG).

73 VI. Eine mündliche Verhandlung hält der Senat nicht für erforderlich (§ 107 Abs. 1 PatG).

Bacher

Deichfuß

Kober-Dehm

Rensen

von Pückler
