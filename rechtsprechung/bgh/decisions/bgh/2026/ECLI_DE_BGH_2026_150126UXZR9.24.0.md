---
ecli: "ECLI:DE:BGH:2026:150126UXZR9.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 9/24"
decided: "2026-01-15"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600212026.xml"
neuris_doknr: "KORE600212026"
---

# Bundesgerichtshof, X ZR 9/24 vom 2026-01-15

## Tenor

Auf die Berufung der Beklagten wird das Urteil des 4. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 4. Januar 2024 abgeändert.

Die Klage wird abgewiesen.

Die Kosten des Rechtsstreits trägt die Klägerin.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 628 233 (Streitpatents), das am 4. Oktober 2011 unter Inanspruchnahme der Priorität einer europäischen Patentanmeldung vom 13. Oktober 2010 angemeldet wurde und einen Leistungssender und einen Leistungsempfänger für ein induktives Stromübertragungssystem betrifft.

2 Patentanspruch 1, auf den zwei weitere Ansprüche zurückbezogen sind, betrifft einen Leistungssender und lautet in der Verfahrenssprache:

Power transmitter for transmitting power inductively to a power receiver via a transmitter coil (11), the power receiver being connectable to, or part of, a device that is to be charged or provided with power, the power transmitter comprising:

a first unit (17) for receiving first data and second data from the power receiver, said first data indicating a modulation requirement for frequency shift for frequency modulation of the power signal, said second data indicating an inquiry message; and being characterized by further comprising:

a second unit (18) for transmitting a response message to the power receiver via the transmitter coil, the response message being intended for responding to said inquiry message, said second unit comprising:

a modulator (15) for modulating a power signal according to said modulation requirement when transmitting the response message so as to carry the response message;

wherein said second data further indicates at least one of the following:

a format of said response message; and

a time requirement for transmitting said response message;

and the power transmitter is arranged to transmit said response message according to at least one of the format and the time requirement.

3 Patentanspruch 4, auf den zwei weitere Ansprüche zurückbezogen sind, betrifft einen Leistungsempfänger. Patentansprüche 7 und 8 haben Verfahren zur Kommunikation in einem induktiven Stromübertragungssystem zum Gegenstand.

4 Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Die Beklagte hat das Streitpatent wie erteilt und hilfsweise in zwölf geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt. Dagegen richtet sich die Berufung der Beklagten in erster Linie in der erteilten Fassung, hilfsweise die nebengeordneten Ansprüche selbständig, und weiter hilfsweise in der Fassung der Hilfsanträge erster Instanz - mit Ausnahme des Hilfsantrags 8 - sowie in fünf weiteren geänderten Fassungen verteidigt. Die Klägerin tritt dem Rechtsmittel entgegen.

## Entscheidungsgründe

6 Die Berufung ist zulässig und hat auch in der Sache Erfolg.

7 I. Das Streitpatent betrifft Vorrichtungen und Verfahren zur induktiven Übertragung von elektrischer Leistung.

8 1. Nach der Beschreibung ist die induktive Übertragung von elektrischer Leistung von einem Leistungssender (power transmitter) auf einen Leistungsempfänger (power receiver) bekannt. Sie werde etwa verwendet, um Batterien von elektrischen Geräten wie Mobilfunkgeräten, PDA, Fernbedienungen zu laden, aber auch um elektrische Geräte wie Lampen direkt kabellos mit Strom zu versorgen (Abs. 1 bis 4).

9 Zur Vorbereitung und Kontrolle der Leistungsübertragung übermittele der Leistungsempfänger Informationen an den Leistungssender. Physikalisch gesehen könne dies dadurch geschehen, dass das Leistungssignal als Träger genutzt werde und der Leistungsempfänger die Amplitude oder die Phase des Stroms der Primärspule oder die Spannung moduliere. Der Leistungssender könne das Signal demodulieren, um die Daten zu empfangen (Abs. 28).

10 Die Beschreibung nimmt hierzu Bezug auf die Qi wireless power specification, die vom Wireless Power Consortium im Juli 2010 publiziert wurde (Abs. 28 bis 33). Diese Spezifikation enthält nähere Vorgaben für die induktive Leistungsübertragung.

11 Danach stelle der Leistungssender anfangs ein Leistungssignal bereit, wodurch eine Selektionsphase (selection phase) beginne. Die Leistung könne genutzt werden, um die Elektronik des Leistungsempfängers hochzufahren. In der folgenden Ping-Phase (ping phase) werde bestimmt, ob ein Leistungsempfänger im Bereich des Leistungssenders vorhanden sei. Werde das Leistungssignal durch den Leistungssender bereitgestellt, sende der Leistungsempfänger - durch Lastmodulation - ein erstes Datenpaket an den Leistungssender, das Informationen über den Grad der Kopplung zwischen Leistungssender und Leistungsempfänger enthalte. In der anschließenden Konfigurationsphase (configuration phase), die der Vorbereitung der eigentlichen Leistungsübertragung diene, lasse der Leistungsempfänger seine Last noch getrennt (disconnected). Er übermittele dem Leistungssender die erforderlichen Parameter, woraufhin der Leistungsempfänger sich entsprechend konfiguriere. Hieran schließe sich die Leistungsübertragungsphase (power transfer phase) an. Der Leistungsempfänger verbinde seine Last mit der vom Leistungssender bereitgestellten Leistung. Er überwache die Last und übermittele dem Leistungssender in regelmäßigen Abständen, ob die Leistung erhöht, verringert oder gleichbleiben soll.

12 Während sich diese Spezifikation nur mit der Kommunikation vom Leistungsempfänger zum Leistungssender befasse, seien auch induktive Leistungsübertragungssysteme bekannt, die eine Kommunikation in die Gegenrichtung ermöglichten (Abs. 33).

13 Die Beschreibung nimmt Bezug auf die US-amerikanische Patentanmeldung 2009/0108805 (D5). Diese sehe die Übertragung von Daten zum Leistungsempfänger durch Modulation der Erregung der primären Spule vor. Dabei könne die Kommunikation hand-shaking und Kompatibilitäts-Checks vorsehen.

14 Die internationale Patentanmeldung 2010/11541 sehe eine Kommunikation durch Ein-/Aus-Tastung (on/off keying, OOK) vor (Abs. 5 f.).

15 Nachteilig hieran sei, dass die bekannten Systeme eine spezifische Ausgestaltung des Leistungsempfängers erforderten, um ihn in die Lage zu versetzen, mit dem Leistungssender zu kommunizieren, insbesondere Daten von ihm zu empfangen (Abs. 7).

16 2. Vor diesem Hintergrund besteht das technische Problem darin, eine Vorrichtung zur induktiven Übertragung von elektrischer Leistung zur Verfügung zu stellen, die eine Kommunikation in beide Richtungen bei möglichst einfacher Ausgestaltung des Leistungsempfängers ermöglicht.

17 3. Zur Lösung schlägt das Streitpatent in Anspruch 1 einen Leistungssender vor, dessen Merkmale sich wie folgt gliedern lassen:

18 1

Power transmitter for transmitting power inductively to a power receiver via a transmitter coil (11), the power receiver being connectable to, or part of, a device that is to be charged or provided with power, the power transmitter comprising:

Leistungssender zum induktiven Übertragen von Leistung an einen Leistungsempfänger über eine Sendespule, wobei der Leistungsempfänger mit einer Vorrichtung oder einem Teil einer Vorrichtung verbindbar ist, die geladen oder mit Leistung versorgt werden soll, umfassend:

2

a first unit (17) for receiving first data and second data from the power receiver,

eine erste Einheit zum Empfangen erster und zweiter Daten vom Leistungsempfänger;

2.1

said first data indicating a modulation requirement for frequency shift for frequency modulation of the power signal,

die ersten Daten zeigen eine Modulationsanforderung für eine Frequenzverschiebung zur Frequenzmodulation des Leistungssignals an;

2.2

said second data indicating an inquiry message;

die zweiten Daten zeigen eine Anfragenachricht an;

5

wherein said second data further indicates at least one of the following:

die zweiten Daten zeigen außerdem mindestens eines von Folgendem an:

5.1

a format of said response message; and

ein Format der Antwortnachricht und

5.2

a time requirement for transmitting said response message;

eine Zeitanforderung zum Senden der Antwortnachricht;

3

a second unit (18) for transmitting a response message to the power receiver via the transmitter coil, the response message being intended for responding to said inquiry message,

eine zweite Einheit zum Senden einer Antwortnachricht an den Leistungsempfänger über die Sendespule; wobei die Antwortnachricht der Antwort auf die Anfragenachricht dient;

4

said second unit comprising a modulator (15) for modulating a power signal according to said modulation requirement when transmitting the response message so as to carry the response message;

die zweite Einheit umfasst einen Modulator zum Modulieren eines Leistungssignals entsprechend der Modulationsanforderung, um die Antwortnachricht zu tragen, wenn diese gesendet wird;

6

and the power transmitter is arranged to transmit said response message according to at least one of the format and the time requirement.

der Leistungssender ist dafür ausgestaltet, die Antwortnachricht entsprechend mindestens diesem Format oder dieser Zeitanforderung zu senden.

19 4. Der Anspruch bedarf der näheren Erläuterung:

20 a) Merkmal 1 gibt vor, dass der Leistungssender einen Leistungsempfänger induktiv mit Leistung versorgen kann und hierfür mit diesem verbindbar ist. Dies schließt nicht aus, dass der Leistungssender geeignet ist, mehr als eine Vorrichtung mit elektrischer Leistung zu versorgen. Eine nähere Festlegung auf bestimmte Leistungsempfänger ist dem Anspruch ebenfalls nicht zu entnehmen.

21 b) Nach Merkmalsgruppe 2 weist der Leistungssender eine erste Einheit auf, die geeignet ist, Daten vom Leistungsempfänger zu empfangen. Diese Daten werden anspruchsgemäß unterschieden in erste und zweite Daten.

22 c) Die ersten Daten zeigen eine Modulationsanforderung an, die der Leistungssender für die Antwort auf die Anfrage erfüllen muss (Merkmal 2.1).

23 Die Übermittlung von Daten vom Leistungssender zum Leistungsempfänger durch Modulation des Leistungssignals kann grundsätzlich auf verschiedene Weise erfolgen, etwa durch Modulation der Amplitude, der Phase oder der Frequenz des Leistungssignals. Gemäß Merkmal 2.1 vermittelt der Leistungsempfänger dem Leistungssender durch die ersten Daten die Information, dass die Übermittlung von Daten vom Leistungssender zum Leistungsempfänger durch Frequenzmodulation erfolgen soll und teilt dazu eine Frequenzverschiebung (frequency shift) mit (Abs. 18 bis 22).

24 Aus Merkmal 2.1 ergibt sich mithin die Anforderung, dass der Leistungssender geeignet sein muss, erste Daten zu empfangen, die eine Modulationsanforderung für eine Frequenzverschiebung zur Frequenzmodulation anzeigen. Dies schließt nicht aus, dass der Leistungssender darüber hinaus auch in der Lage ist, etwa von einem anderen Leistungsempfänger Anforderungen zu empfangen, die sich auf eine andere Art der Modulation, etwa Modulation der Amplitude oder der Phase, beziehen.

25 d) Die zweiten Daten zeigen eine Anfrage (inquiry message) des Leistungsempfängers an, auf die eine Antwort (response message) des Leistungssenders erwartet wird (Merkmal 2.2).

26 Beispiele für solche Anfragen sind in den Absätzen 52 bis 54 der Beschreibung genannt. Danach kann der Leistungsempfänger etwa anfragen, ob er in einen Testmodus oder in einen Kalibrierungsmodus wechseln soll. Der Leistungssender antwortet hierauf mit "ja" oder "nein".

27 Patentanspruch 1 ist durch diese Beispiele nicht auf bestimmte Anfragen oder Antworten beschränkt. Eine Antwort des Leistungssenders im Sinne des Streitpatents erfordert allerdings, dass sie nicht lediglich zeitlich auf die Anfrage folgt, sondern einen Bezug zu der Anfrage aufweist.

28 e) Die zweiten Daten umfassen ferner mindestens die Anzeige eines Formats für die Antwort oder eine Zeitanforderung (time requirement) zum Senden der Antwort (Merkmalsgruppe 5).

29 Als Beispiele für eine Zeitanforderung nennt die Beschreibung die Vorgabe einer Zeit, in der der Leistungssender auf die Anfrage antwortet oder eine Vorgabe zur Datenrate, mit der die Antwort übermittelt wird (Abs. 48 f.).

30 f) Die ersten und zweiten Daten können gemeinsam in einem Datenpaket enthalten sein. Dies ist jedoch, wie sich aus der Beschreibung ergibt (Abs. 51), nicht zwingend.

31 g) Der Leistungssender umfasst eine zweite Einheit, die geeignet ist, über die Sendespule eine Antwort auf die Anfrage des Leistungsempfängers an diesen zu senden (Merkmal 3).

32 Hierzu dient ein Modulator, der die Eignung aufweist, das Leistungssignal entsprechend der mit den ersten Daten vom Leistungsempfänger übermittelten Modulationsanforderung zu modulieren, so dass dieses Signal die Antwort auf die Anfrage tragen kann (Merkmal 4). Da die Modulationsanforderung nach Merkmal 2.1 auf eine Frequenzverschiebung zur Frequenzmodulation des Leistungssignals ausgelegt ist, muss der Leistungssender dazu in der Lage sein, eine Frequenzmodulation des Leistungssignals vorzunehmen. Dies schließt nicht aus, dass der Leistungssender in der Lage ist, das Leistungssignal auch auf andere Weise zu modulieren.

33 Aus dem Zusammenhang von Merkmal 4 mit der Merkmalsgruppe 2 ergibt sich, dass die die ersten Daten vom Leistungssender zeitlich vor der Übermittlung der Antwort auf die Anfrage empfangen werden müssen.

34 h) Merkmal 6 fordert, dass der Leistungssender so ausgestaltet ist, dass er sich bei der Übermittlung der Antwort die mit den zweiten Daten übermittelten Vorgaben hinsichtlich Formal der Antwort oder Zeitanforderung beachten kann.

35 Soll ein Bauteil einer geschützten Vorrichtung nach der Formulierung des Patentanspruchs einen bestimmten Zweck erfüllen, reicht es nach der Rechtsprechung des Senats nicht aus, wenn es hierzu erst durch Aufspielen geeigneter Software oder sonstige Konfigurationsmaßnahmen in die Lage versetzt werden kann. Vielmehr muss es bereits entsprechend konfiguriert sein, also bereits eine Software oder sonstige Mittel umfassen, die in entsprechenden Betriebssituationen die Verwirklichung dieser Funktion ermöglichen (BGH, Urteil vom 11. Januar 2022 - X ZR 4/20, GRUR 2022, 982 - SRS-Zuordnung).

36 Nach dem Zusammenhang der Merkmale genügt es mithin nicht, dass der Leistungssender in der Lage ist, nach Maßgabe von voreingestellten oder gegebenenfalls mit dem Leistungsempfänger ausgehandelten Kommunikationsbedingungen als Reaktion auf eine Anfrage des Leistungsempfängers Nachrichten an diesen zu übermitteln ("Verhandlungslösung"). Aus Patentanspruch 1 ergibt sich vielmehr die Anforderung, dass der Leistungssender so konfiguriert ist, dass er vom Leistungsempfänger mit den ersten und zweiten Daten übermittelten Vorgaben empfangen, deuten und mit seiner Antwort darauf unmittelbar umsetzen kann ("Befehlslösung").

37 Im allgemeinen Teil der Beschreibung wird dazu erläutert, dass nach der Lehre des Streitpatents die ersten Daten eine Modulationsanforderung vorgeben, die vom Leistungsempfänger bei seiner Antwort auf die Anfrage benutzt werden muss (Absatz 13: "the first data indicates a modulation requirement that has to be used by the power transmitter when responding to the power receiver").

38 Absatz 45 der Beschreibung stehen diesem Verständnis nicht entgegen. Dort ist lediglich beispielhaft anhand einer üblichen Struktur eines Datenpakets, wie sie Figur 4 zeigt, erläutert, dass die Kommunikation vom Leistungsempfänger an den Leistungssender entsprechend einem vordefinierten Standard erfolgen kann.

39 Absatz 46 ist demgegenüber - weitergehend - zu entnehmen, dass der Leistungssender auf eine mit einer Anfragenachricht übermittelte konkrete Anforderung eines Formats, in dem die Antwort erfolgen soll, unmittelbar reagieren können muss. Danach genügt es nicht, wenn eine entsprechende Reaktion erst erfolgen kann, wenn zuvor die fortan anzuwendende Modulation oder das für eine Antwortnachricht anzuwendende Format ausgehandelt werden muss.

40 Das Streitpatent sieht den Vorteil der beanspruchten Lehre darin, dass der Leistungsempfänger vorgeben kann, in welcher Weise das Leistungssignal vom Leistungssender zur Übertragung der erwarteten Antwort moduliert werden muss und welches Format oder welche Zeitanforderung dabei beachtet werden müssen. Dies ermögliche es, den Leistungsempfänger einfach und kostengünstig auszugestalten (Abs. 8, Abs. 58).

41 II. Das Patentgericht hat seine Entscheidung im Wesentlichen wie folgt begründet:

42 Der Gegenstand von Patentanspruch 1 gehe nicht über den Inhalt der ursprünglichen Anmeldung hinaus. Er sei jedoch nicht patentfähig, denn er beruhe gegenüber der US-amerikanischen Patentanmeldung 2010/146308 (D1) nicht auf erfinderischer Tätigkeit. D1 sei zwar nicht zu entnehmen, dass der Leistungsempfänger erste Daten übermittele, die eine Modulationsanforderung für eine Frequenzverschiebung zur Frequenzmodulation anzeige. Die Druckschrift sehe aber die Angabe von zwei Frequenzen für eine binäre Datenübertragung vor. Die Auswahl zwischen der Angabe eines Frequenzhubs, die die Angabe einer Mittenfrequenz voraussetze, und der Angabe zweier Modulationsfrequenzen stelle sich für den Fachmann als beliebig dar. D1 sehe auch die Möglichkeit vor, dass nur der Leistungsempfänger dem Leistungssender seine Kommunikationsparameter vorgebe.

43 Auch die Hilfsanträge blieben erfolglos. Zum Teil sei der damit verteidigte Gegenstand nicht patentfähig, zum Teil gehe er über den Inhalt der ursprünglichen Anmeldeunterlagen hinaus. Der erst in der mündlichen Verhandlung gestellte Hilfsantrag 8 sei verspätet und daher zurückzuweisen.

44 III. Diese Beurteilung hält der Überprüfung im Berufungsrechtszug in einem entscheidenden Punkt nicht stand.

45 1. Der Gegenstand von Patentanspruch 1 geht nicht über den Inhalt der ursprünglichen Anmeldung hinaus, wie er sich aus der internationalen Patentanmeldung 2012/049582 (NK2) ergibt.

46 Entgegen der Auffassung der Berufungserwiderung ist NK2 nicht auf einen Leistungsempfänger beschränkt, der hinsichtlich der mit den ersten Daten übertragenen Modulationsanforderung die Möglichkeit hat, zwischen den Modulationsarten Phase, Amplitude und Frequenz zu wählen.

47 NK2 offenbart zwar die Möglichkeit, das System so zu gestalten, dass der Leistungssender verschiedene Modulationstypen anwenden kann, wodurch eine hohe Flexibilität und Anpassungsfähigkeit erreicht werden kann.

48 NK2 offenbart aber auch für weniger anspruchsvolle Einsatzformen die Möglichkeit, das System so zu gestalten, dass der Leistungsempfänger auf einen bestimmten Modulationstyp eingestellt ist. Dies ermögliche eine kostengünstige Herstellung (S. 4 Z. 15). Danach genügt es ferner, wenn mindestens eine Art der Modulation (type of modulation) des Leistungssignals und für diese wiederum mindestens ein Modulationsbereich (modulation range) ausgewählt wird (S. 5 Z. 12 ff.).

49 Entsprechend genügt es nach dem in NK2 formulierten Patentanspruch 4, wenn der Leistungssender in der Lage ist, eine Modulationsanforderung zu empfangen, die mindestens einer Art der Modulation des Leistungssignals entspricht.

50 2. Entgegen der Auffassung des Patentgerichts ist der Gegenstand von Patentanspruch 1 patentfähig.

51 a) Die Lehre von Patentanspruch 1 wird durch D1 nicht vollständig offenbart.

52 aa) Gegenstand der D1 ist ein tragbares Gerät zur induktiven Versorgung eines mobilen Computers mit elektrischer Leistung.

53 Im Stand der Technik seien Dockingstationen bekannt, die dazu verwendet werden könnten, ein mobiles Computergerät mit Leistung zu versorgen oder aufzuladen. Herkömmliche Vorrichtungen dieser Art, bei denen eine elektrische Verbindung über einen Stecker hergestellt werde, wiesen Nachteile auf.

54 Vor diesem Hintergrund schlägt D1 eine Vorrichtung vor, mit der ein mobiles Gerät induktiv mit Leistung versorgt werden kann. Zugleich könne die induktive Verbindung genutzt werden, um Datensignale zu übertragen (Abs. 64 f.). Dazu sollen eine Dockingstation (dockingstation, dock) und ein mobiles Computergerät (mobile computer device, MCD) so ausgestaltet werden, dass die Station Leistung an das MCD liefert und die beiden Komponenten Datensignale austauschen können, wenn das MCD induktiv mit der Station gekoppelt ist (Abs. 68, 78).

55 Anhand der nachstehend wiedergegebenen Figur 2A erläutert D1, dass die Station eine Signalquelle (224) aufweise, von der ein Signal (228), zum Beispiel elektrische Leistung, an das MCD übertragen werde.

56 Das MCD weise eine Spule (214) auf, mit der das Signal (228) in elektrische Leistung umgewandelt werden könne (Abs. 85). Auf diesem Signalpfad könnten auch Daten vom MCD an die Station übertragen werden (Abs. 86, Abs. 89 f.).

57 Die nachstehend wiedergegebene Figur 4 zeige ein System, das eine Station und ein MCD umfasse, die jeweils mit einem Leistungs-Subsystem (422, 412) und einem Kommunikations-Subsystem (426, 416) ausgestattet seien, wobei die Leistungsquelle auf der Seite der Station angeordnet sei (Abs. 93).

58 Die Kommunikationssubsysteme dienten der Übertragung von Daten auf dem induktiven Signalpfad entweder durch Modulation eines induktiven Leistungssignals oder über einen separaten Datensignalpfad (Abs. 94). Die CPU (424) der Station könne über das Kommunikationssubsystem vom MCD eingehende Datensignale verarbeiten und Daten steuern, die unter Verwendung des induktiven Signalpfads an das MCD übertragen werden (Abs. 95). Das Kommunikationssubsystem des MCD sei so konfiguriert, dass Daten vom Dock empfangen oder an dieses gesendet werden könnten. Es ermögliche die Implementierung von Protokollen zur Regelung der induktiven Leistungsübertragung und zum Austausch von Daten. Hierfür sei das Kommunikationssubsystem des MCD in der Lage, modulierte Leistungssignale oder andere Signale zur Kommunikation mit der Station zu erzeugen (Abs. 96, Abs. 101, Abs. 104). Die Übertragung von Daten vom MCD an die Station könne auch dazu dienen, die nachfolgende Kommunikation zwischen den Geräten zu ermöglichen (Abs. 105).

59 Entsprechend könne die Station einen Signalhandler zum Senden oder Empfangen von Daten auf dem induktiven Signalpfad umfassen (Abs. 110).

60 Die nachstehend wiedergegebene Figur 7A zeige ein vereinfachtes Blockdiagramm eines MCD.

61 Danach umfasst das MCD unter anderem einen Signalprozessor (740). Dieser implementiere ein Protokoll, das die Erzeugung von Daten, die über den induktiven Signalpfad übermittelt würden, und den Empfang und die Deutung von eingehenden Daten ermöglichten. Zugleich steuere der Signalprozessor den Empfang bzw. die Übertragung von Leistung.

62 Das Leistungssignal, das beim MCD eingehe, könne moduliert, zum Beispiel frequenzmoduliert sein, um gleichzeitig mit der Leistung auch Daten zu übertragen. So könne eine Frequency Shift-Key-Modulation (FSK-Modulation) verwendet werden, um Daten vom Dock zum MCD zu signalisieren. Der Signalhandler des MCD könne hierfür einen FSK-Detektor umfassen (Abs. 123, Abs. 177, Abs. 182).

63 Wie D1 hierzu anhand der nachstehend wiedergegebenen Figur 9A erläutert, kann hierfür in der Station ein Ausgangsbereich (826) vorgesehen sein, der für die Modulation des Leistungssignals sorgt (Abs. 129).

64 D1 sieht weiter vor, dass das MCD als leistungsempfangendes Gerät an die Station als Leistungssender sogenannte Enumerationsinformationen übermittelt. Diese könnten unter anderem verwendet werden, um Vorgänge, Funktionen oder andere Aspekte der Leistungsübertragung zwischen den beiden Geräten auszuwählen (Abs. 151). Die entsprechenden Daten würden von der Station empfangen und flössen in die Steuerung der Leistungsübertragung ein (Abs. 152).

65 D1 beschreibt Ausführungsformen, bei denen ein Protokoll implementiert sei, das es dem MCD ermögliche, Nachrichten an die Station zu übermitteln, auf die die Station antworte. Solche Nachrichten können unterschiedlich groß sein und über unterschiedliche Modulationsschemata gesendet werden. Die Nachrichten könnten beispielsweise der Regelung der Leistungsübertragung dienen, aber auch einem sonstigen Austausch zwischen Station und MCD (in Abs. 158 als periphere Kommunikation bezeichnet). Das Protokoll könne etwa vorsehen, dass das von der Station übermittelte Signal mithilfe von Frequenzmodulation übertragen werde. Dabei könnten unterschiedliche Frequenzbereiche, etwa 110/125 kHz und 113/119 kHz, verwendet werden. Ein solches Protokoll sehe zudem die Verwendung strukturierter Datenformate vor (Abs. 159).

66 Weiterhin beschreibt D1, dass ein Signalübertragungsprotokoll vorsehen kann, dass die Kommunikation zwischen Dock und MCD asymmetrisch abläuft, indem das Dock Pakete mit vier Bits und das MCD Pakete mit nur zwei Bits sende. Dabei könne für diese Kommunikation eine Frequenzumtastung mit den Frequenzen 110 und 125 kHz verwendet werden, um die Werte 0 und 1 zu signalisieren. D1 lehrt hierzu ergänzend, dass auch andere Bereiche wie zum Beispiel 113 und 119 kHz verwendet werden können ("More defined ranges may alternatively be used"). Die Umsetzung des Protokolls könne durch Programmierung oder Konfiguration vorgenommen werden (Abs. 159).

67 b) Damit offenbart D1 einen Leistungssender (Dockingstation), der zur induktiven Übertragung von Leistung an ein MCD als Leistungsempfänger geeignet ist.

68 D1 ist weiter zu entnehmen, dass zwischen Station und MCD in beide Richtungen Daten übermittelt werden können. Dies kann auch durch Frequenzmodulation des Leistungssignals erfolgen.

69 Das MCD ist zudem in der Lage, Signale zu übermitteln, auf die eine Antwort der Station erwartet wird. Wie oben ausgeführt wurde, kommt es auf den konkreten Inhalt von Anfrage und Antwort nicht an.

70 c) Dagegen offenbart D1 nicht unmittelbar und eindeutig die Merkmale 4 und 6, denen zufolge der Leistungssender so konfiguriert ist, dass er eine Modulationsanforderung und eine Formatvorgabe oder Zeitanforderung des Leistungsempfängers für eine Antwortnachricht unmittelbar befolgen und umsetzen kann.

71 Entgegen der Auffassung der Klägerin ergibt sich solches nicht aus Absatz 151 der Beschreibung. Dort ist lediglich vorgesehen, dass der Leistungsempfänger dem Leistungssender Enumerationsinformationen übermittelt, die dazu dienen, die wechselseitige Identifikation und die Kommunikation zwischen den Geräten zu ermöglichen. Dagegen ist die Möglichkeit einer einseitigen, vom Leistungssender umzusetzenden Vorgabe durch den Leistungsempfänger nicht beschrieben.

72 In Absatz 158 ist zwar eine Kommunikation in beide Richtungen beschrieben. Auch dort ist jedoch nicht unmittelbar und eindeutig offenbart, dass der Leistungssender so konfiguriert ist, dass er Vorgaben des Leistungsempfängers bezüglich einer Frequenzmodulation des Leistungssignals und des Formats der Antwort unmittelbar umsetzen kann.

73 Absatz 159 sieht zwar die Verwendung unterschiedlicher Frequenzbereiche für die Datenübertragung vor, beschreibt jedoch nur, dass diese in einem Signalübertragungsprotokoll vorgesehen sind, das in beiden Geräten implementiert werden kann. Dies offenbart jedoch nicht, dass solche vom Leistungssender übermittelte, einer Anforderung gleichkommenden Informationen vom Leistungssender unmittelbar befolgt und umgesetzt werden. Ob und wie es tatsächlich zu einer Änderung eines Frequenzbereichs für die Frequenzmodulation oder eines Formats für eine Antwortnachricht kommt, ist danach nicht Gegenstand der D1, vielmehr bleibt die weitere Ausgestaltung dem Fachmann überlassen.

74 3. Der Gegenstand von Patentanspruch 1 wird auch durch die US-amerikanische Patentanmeldung 2010/0013322 (D2) nicht vollständig vorweggenommen.

75 a) D2 befasst sich mit der induktiven Versorgung eines Leistungsempfängers (power receiving device), etwa eines Mobiltelefons, durch eine Leistungsübertragungsvorrichtung (power transmission device, im Folgenden: Leistungssender). Es sei wünschenswert, dass ein solcher Leistungssender in der Lage sei, Leistungsempfänger unterschiedlicher Art mit Leistung zu versorgen.

76 Die nachstehend wiedergegebene Figur 2 zeigt schematisch einen Leistungssender und einen Leistungsempfänger

77 Der Leistungsübertragungsbereich (12) des Leistungssenders und der Leistungsempfängerbereich (42) des Leistungsempfängers wiesen jeweils eine Spule auf. Mit dem Leistungsempfänger sei eine Last verbunden, die mit Leistung versorgt werden solle, etwa die Batterie eines Mobiltelefons. Der Leistungsübertragungsbereich erzeuge eine Wechselstromspannung und versorge damit die Primärspule L1. Zur Übertragung von Daten könne die Frequenz variiert werden (Abs. 68). Der Leistungsempfänger weise eine Vorrichtung auf, die etwa bei einer Datenübertragung durch Frequenzmodulation die Daten erkenne (Abs. 81).

78 Auf der Seite des Leistungssenders könnten die Kommunikationsbedingungen eingestellt werden. Dies könne dadurch geschehen, dass Informationen mit dem Leistungsempfänger ausgetauscht würden. Die Kommunikationsbedingungen könnten das Kommunikationsverfahren und die Kommunikationsparameter umfassen. Das Kommunikationsverfahren umfasse verschiedene Modulationsverfahren, etwa die Frequenzmodulation. Die Kommunikationsparameter umfassten etwa im Falle der Frequenzmodulation eine Frequenz (Abs. 84 bis 87).

79 Zur Erläuterung der Abläufe zur Vorbereitung und Durchführung der Leistungsversorgung nimmt D2 Bezug auf das Flussdiagramm der nachstehend wiedergegebenen Figuren 11 und 12 (Abs. 174 ff.). Dabei zeigt die linke Seite das Geschehen auf der Seite des Leistungssenders an, die rechte Seite das Geschehen auf der Seite des Leistungsempfängers.

80 Der Leistungssender starte eine temporäre Leistungsübertragung (S2). Dies ermögliche die Einschaltung des Leistungsempfängers (S22), die sich auf die Frequenz des temporären Leistungsübertragungssignals einstelle. Die elektrische Verbindung zwischen dem Leistungsempfänger und der Last werde zunächst unterbrochen.

81 Stelle der Leistungsempfänger fest, dass er sich in einer korrekten Position befindet, erstelle er einen Verhandlungsrahmen (negotiation frame) und übertrage diesen durch Modulation des Leistungssignals an den Leistungssender (S25). Der Verhandlungsrahmen enthalte Informationen, die für die beabsichtigten Leistungsversorgung benötigt würden. Der Leistungssender überprüfe daraufhin, ob unter den mit dem Verhandlungsrahmen übermittelten Informationen und Bedingungen eine Leistungsversorgung möglich sei (S5). In diesem Fall erstelle er seinerseits einen Verhandlungsrahmen und übermittele ihn an den Leistungsempfänger (S7). Dieser Verhandlungsrahmen enthalte ebenfalls Informationen über die beabsichtigte Leistungsversorgung.

82 Entspreche der Verhandlungsrahmen den Möglichkeiten des Leistungsempfängers, erstelle dieser einen Einrichtungsrahmen (setup frame) und übermittele ihn an den Leistungssender (S28). Der Einrichtungsrahmen könne unter anderem Informationen über die Kommunikationsbedingungen umfassen, wie die Ansteuerspannung und die Ansteuerfrequenz, aber auch die Arten von möglichen Befehlen (Abs. 183, s. auch Abs. 139). Stelle der Leistungssender nach Empfang des Einrichtungsrahmens (S8) fest, dass dieser angemessen sei, erstelle er einen Einrichtungsrahmen, um ihn an den Leistungsempfänger zu übertragen (S10).

83 Stelle der Leistungsempfänger fest, dass der Einrichtungsrahmen angemessen sei (S29, S30), erstelle er einen Startrahmen und übertrage diesen an den Leistungssender (S31). Daraufhin gehen beide Seiten in einen Befehlszweig über (S41 und S61). Sofern kein anderer Befehl vorliege, werde sodann die eigentliche Leistungsübertragung gestartet (S46).

84 Bis zu diesem Zeitpunkt erfolge die Kommunikation gemäß einem voreingestellten Verfahren mit voreingestellten Parametern (Abs. 114 f., Abs. 117 f.). Erst nach dem Start der normalen Leistungsübertragung werde die Kommunikation auf die zwischen Leistungssender und -empfänger festgelegten Bedingungen umgestellt. Unter bestimmten Voraussetzungen sei es möglich, die Leistungsübertragung zu unterbrechen und die Kommunikation wieder unter den voreingestellten Bedingungen stattfinden zu lassen (Abs. 126 f.).

85 Wie aus der bereits oben wiedergegebenen Figur 2 ersichtlich, weisen beide Seiten einen Bereich zum Einstellen der Kommunikationsbedingungen (34, 64) auf, der nach D2 dazu dient, die Bedingungen für eine Kommunikation unter Berücksichtigung der wechselseitig hierzu übermittelten Informationen einzustellen (Abs. 9, Abs. 29, Abs. 84 ff.).

86 Enthalte der Einrichtungsrahmen, den der Leistungsempfänger übermittele, Informationen über die Kommunikationsbedingungen, stelle der Bereich zur Einrichtungsverarbeitung (38) den Leistungssender entsprechend ein (Abs. 118 f., Abs. 139). Wie die Beschreibung erläutert, sei es hierdurch möglich, dass der Leistungssender mit Leistungsempfängern unterschiedlicher Art zusammenwirke (Abs. 10 bis 12). Dabei könnten sich die Kommunikationsbedingungen vor und nach dem Start der normalen Leistungsübertragung auch unterscheiden (Abs. 14, Abs. 100). Hierzu übermittele der Leistungsempfänger, wie bereits erwähnt wurde, Bedingungen für die Kommunikation an den Leistungssender (Abs. 85 bis 88).

87 Als eine der Möglichkeiten zur Kommunikation nennt D2 die Frequenzmodulation des Leistungssignals (Abs. 15 f., Abs. 68, Abs. 87). Auf Seiten des Leistungsempfängers sei eine Erkennungsschaltung (59) vorgesehen, die in der Lage sei, die vom Leistungssender durch Frequenzmodulation übertragenen Daten zu erkennen (Abs. 81).

88 Der Leistungssender weise zudem einen Kommunikationsverarbeitungsbereich (36) auf, mit dem Daten entsprechend den zuvor vom Leistungsempfänger übermittelten Konditionen, etwa durch Frequenzmodulation übertragen werden könnten (Abs. 89 f.).

89 Nach dem erfolgreichen Austausch von Verhandlungsrahmen und Einrichtungsrahmen könnten Befehle verarbeitet werden. Beide Seiten seien in der Lage, einen Befehl zu geben oder auszuführen (Abs. 121).

90 b) Damit sind jedenfalls die Merkmale 4 und 6 nicht offenbart.

91 Soweit danach eine Kommunikation zwischen Leistungssendern stattfindet, mit der die Frequenzbereiche für eine Frequenzmodulation sowie die Formate für eine Antwortnachricht konfiguriert werden können, wird dies nach D2 ausgehandelt. Dabei werden zunächst von beiden Seiten unter Anwendung der anfänglichen Kommunikationsbedingungen Informationen ausgetauscht, die einer festgelegten Prozedur folgend schließlich zur Anwendung einer neuen Konfiguration führen können. Dagegen offenbart D1 nicht die Möglichkeit, dass der Leistungsempfänger eine Modulationsanforderung und das Format oder eine Zeitanforderung für eine erwartete Antwort übermittelt, die Leistungssender unmittelbar und ohne eine weitere Kommunikation bei der Übermittlung der Antwort noch unter Anwendung des unveränderten Modus umsetzt. Vielmehr sieht D2 vor, dass hierbei von beiden Seiten Informationen unter Anwendung der initialen Kommunikationsparameter ausgetauscht, also Kommunikationsbedingungen ausgehandelt werden. Während dieses Prozesses werden die anfänglichen Kommunikationsbedingungen verwendet. Erst wenn andere Kommunikationsbedingungen ausgehandelt sind, kann die Befehlsverarbeitung auf deren Grundlage erfolgen (Abs. 113 ff., Figuren 3A bis 5B).

92 4. Die Lehre des Patentanspruchs 1 hat für den Fachmann nicht nahegelegen und beruht damit auf erfinderischer Tätigkeit.

93 Insoweit kommt es entgegen den Ausführungen des Patentgerichts nicht darauf an, ob D1 oder D2 bereits die Übermittlung von Informationen seitens des Leistungssenders offenbare, mit der im Sinne einer Modulationsanforderung gemäß Merkmal 2.1 ein Frequenzhub als Bereichsauswahl für eine Frequenzmodulation angefordert werde oder ob eine solche Ausgestaltung für den Fachmann nahegelegen habe.

94 Wie oben aufgezeigt wurde, offenbaren weder D1 noch D2, dass der Leistungssender so konfiguriert ist, dass er geeignet ist, auf eine solche Modulationsanforderung und die Anforderung eines Formats der Antwortnachricht oder eine Zeitanforderung zum Senden einer Antwortnachricht unmittelbar zu reagieren.

95 Die Klägerin zeigt nicht auf und es ist auch sonst nicht ersichtlich, dass es ausgehend von D1 oder von D2 einen Anlass gab, einen Leistungssender so zu konfigurieren, dass er zur unmittelbaren Befolgung der jeweiligen Anforderung in der Lage ist.

96 5. Der Gegenstand der nebengeordneten Ansprüche 4, 7 und 8 ist durch die gleichen Merkmale geprägt und unterliegt daher der gleichen Beurteilung.

97 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG und § 91 Abs. 1 ZPO.

Deichfuß

Hoffmann

Marx

Rensen

Crummenerl
