---
ecli: "ECLI:DE:BGH:2026:100226UXZR17.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 17/24"
decided: "2026-02-10"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600132026.xml"
neuris_doknr: "KORE600132026"
---

# Bundesgerichtshof, X ZR 17/24 vom 2026-02-10

## Tenor

Auf die Berufung der Klägerin wird das Urteil des 5. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 26. September 2023 abgeändert.

Das europäische Patent 2 433 414 wird für nichtig erklärt.

Die Anschlussberufung wird zurückgewiesen.

Die Beklagte trägt die Kosten des Rechtsstreits.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des europäischen Patents 2 433 414 (Streitpatents), das am 25. Mai 2010 unter Inanspruchnahme von drei europäischen Prioritäten vom 22. Mai, 28. Oktober und 18. Dezember 2009 angemeldet worden ist und einen Identifizierungsdienst betrifft.

2 Patentanspruch 1, auf den 12 weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A system (40, 50) for identifying proximate devices (1, 2) arranged for detecting a sensory identifier (ID) and transmitting request messages (RQ1, RQ2) comprising representations of the detected sensory identifier, the system comprising:

• means for correlating representations of the detected sensory identifiers from the request messages received from the devices (1, 2) so as to match two or more of those devices, and

• means for carrying out an application involving devices that have been matched by said means for correlating representations,

wherein said means for correlating are at least one correlation server (5) and said means for carrying out the application are at least one application server (6), the at least one correlation server (5) and the at least one application server (6) being distinct servers,

wherein the proximate devices (1, 2) are arranged to include, in the request messages (RQ1, RQ2), an indication of an application to be executed, the at least one correlation server (5) being configured to compare the applications indicated by the request messages, and causing a transmitter (88) to transmit the match message based on the match to an application server identified by the matching indications of the application in the matched request messages.

3 Patentanspruch 14 schützt sinngemäß einen Korrelationsserver für den Einsatz in einem solchen System, Patentanspruch 15, auf den drei weitere Ansprüche zurückbezogen sind, ein Verfahren mit korrespondierenden Merkmalen und Patentanspruch 19 ein Computerprogrammprodukt zur Ausführung eines solchen Verfahrens.

4 Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Die Beklagte hat das Streitpatent in seiner erteilten Fassung und mit zwanzig Hilfsanträgen in geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt, soweit dessen Gegenstand über die mit Hilfsantrag 1c verteidigte Fassung hinausgeht, und die weitergehende Klage abgewiesen. Hiergegen richtet sich die Berufung der Klägerin, die ihr Begehren aus dem ersten Rechtszug weiterverfolgt. Die Beklagte tritt dem Rechtsmittel entgegen. Mit ihrer Anschlussberufung verteidigt sie das Streitpatent in der erteilten Fassung, mit ihren in erster Instanz erfolglos gebliebenen Hilfsanträgen und mit einem neuen Hilfsantrag. Höchst hilfsweise verteidigt sie das Schutzrecht in der Fassung ihrer übrigen Hilfsanträge aus erster Instanz und mit acht neuen Hilfsanträgen sowie in der Fassung der erteilten Ansprüche 2, 4, 5, 6, 10, 11 und 17.

## Entscheidungsgründe

6 Beide Rechtsbehelfe sind zulässig. Die Berufung der Klägerin ist begründet und führt zur vollständigen Nichtigerklärung des Streitpatents. Die Anschlussberufung ist unbegründet.

7 I. Das Streitpatent betrifft ein System zum Identifizieren benachbarter Geräte, zum Beispiel von Mobiltelefonen.

8 1. Die Beschreibung des Streitpatents führt aus, mobile Geräte verfügten über eine zunehmende Anzahl von Funktionen, darunter auch Spiele.

9 Bestimmte Spiele erforderten Mitspieler, die jeweils ein eigenes Mobiltelefon nutzten. Bevor ein solches Spiel begonnen werden könne, müssten die Geräte der Spieler identifiziert werden (Abs. 2).

10 Eine Identifikation anhand der Telefonnummern sei unzureichend, wenn die Mitspieler in einer gewissen räumlichen Nähe sein müssten, etwa in Sichtweite (Abs. 3). Die Nutzung von Bluetooth für solche Zwecke sei zu umständlich (Abs. 4).

11 Die internationale Patentanmeldung 2009/014438 (D11) offenbare ein Verfahren zur Identifizierung mit Hilfe sensorischer Identifikatoren und eines Servers. Das erübrige die Bereithaltung von spezieller Hard- und Software auf der Seite der Mobilgeräte und erlaube dementsprechend einfache und kostengünstige Mobilgeräte. Hierbei biete es sich an, die Identifizierung und die weitere Anwendung auf demselben Server durchführen zu lassen. Dies erfordere jedoch die Einrichtung mehrerer Instanzen für den Identifizierungsprozess, wenn verschiedene Anwendungen auf unterschiedlichen Servern bereitgestellt würden (Abs. 8).

12 2. Das Streitpatent betrifft vor diesem Hintergrund das technische Problem, eine einfache und kostengünstige Identifikation von Geräten für eine Vielzahl von Anwendungen bereitzustellen.

13 3. Zur Lösung schlägt das Streitpatent in Patentanspruch 1 ein System vor, dessen Merkmale sich wie folgt gliedern lassen:

14 1

A system (40, 50) for identifying proximate devices (1, 2),

System (40, 50) zum Identifizieren benachbarter Vorrichtungen (1, 2),

1.a

arranged for detecting a sensory identifier (ID)

die eingerichtet sind zum Erfassen eines sensorischen Identifikators (ID)

1.b

and transmitting request messages (RQ1, RQ2), comprising representations of the detected sensory identifier,

und zum Senden von Anfragemeldungen (RQ1, RQ2) mit Darstellungen des erfassten sensorischen Identifikators.

1.c

the system comprising:

means for correlating representations of the detected sensory identifiers from the request messages received from the devices (1, 2) so as to match two or more of those devices, and

Das System umfasst:

Mittel zum Korrelieren von Darstellungen der erfassten sensorischen Identifikatoren aus den von den Vorrichtungen (1, 2) empfangenen Anfragemeldungen, um zwei oder mehr dieser Vorrichtungen abzugleichen,

1.d

means for carrying out an application involving devices that have been matched by said means for correlating representations,

und Mittel zum Ausführen einer Anwendung mit Vorrichtungen, die durch die Mittel zum Korrelieren von Darstellungen abgeglichen wurden.

1.e

wherein said means for correlating are at least one correlation server (5) and

Die Mittel zum Korrelieren bestehen aus mindestens einem Korrelationsserver (5).

1.f

said means for carrying out the application are at least one application server (6),

Die Mittel zum Ausführen der Anwendung bestehen aus mindestens einem Anwendungsserver (6).

1.g

the at least one correlation server (5) and the at least one application server (6) being distinct servers,

Der Korrelationsserver (5) und der Anwendungsserver (6) sind verschiedene Server.

1.h

wherein the proximate devices (1, 2) are arranged to include, in the request messages (RQ1, RQ2), an indication of an application to be executed,

Die benachbarten Vorrichtungen (1, 2) sind dazu eingerichtet, in die Anfragemeldungen (RQ1, RQ2) eine Angabe einer auszuführenden Anwendung einzufügen.

1.i

the at least one correlation server (5) being configured to compare the applications indicated by the request messages,

Der mindestens eine Korrelationsserver (5) ist dazu konfiguriert, die durch die Anfragemeldungen angezeigten Anwendungen zu vergleichen

1.j

and causing a transmitter (88) to transmit the match message based on the match to an application server identified by the matching indications of the application in the matched request messages,

und einen Sender (88) zum Versenden einer auf der Übereinstimmung basierenden Abgleichsmeldung an einen Anwendungsserver zu veranlassen, der durch die übereinstimmenden Angaben der Anwendung in den abgeglichenen Anfragemeldungen identifiziert wird.

15 4. Einige dieser Merkmale bedürfen der Erläuterung.

16 a) Zu Recht ist das Patentgericht davon ausgegangen, dass Merkmal 1 keine näheren Vorgaben dazu enthält, unter welchen Voraussetzungen Geräte als benachbart anzusehen sind.

17 Aus dem genannten Begriff ergibt sich zwar, dass eine gewisse räumliche Nähe bestehen muss, nicht aber eine bestimmte Obergrenze für die Entfernung.

18 Die auf dieses Merkmal bezogenen Ausführungen in der Beschreibung erwähnen in unterschiedlichen Formulierungen eine gewisse Nähe, enthalten aber ebenfalls keine konkrete Definition.

19 b) Aus den Merkmalen 1.a, 1.b und 1.c, die das Erfassen sensorischer Identifikatoren, das Versenden von Anfragemeldungen (RQ1, RQ2) mit Darstellungen eines erfassten Identifikators dieser Art und Mittel zum Korrelieren von solchen Darstellungen vorsehen, ergibt sich ebenfalls keine konkrete Festlegung dazu, wie weit benachbarte Geräte voneinander entfernt sein dürfen.

20 aa) Entgegen der Auffassung der Klägerin ist ein sensorischer Identifikator im Sinne von Merkmal 1.a allerdings nur ein Identifikator, der durch menschliche Sinne erfasst werden kann.

21 Dies ergibt sich aus den Ausführungen in der Beschreibung, wonach der genannte Begriff im Kontext des Streitpatents in diesem Sinne zu verstehen ist (Abs. 17).

22 Als geeignete Beispiele führt die Beschreibung an derselben Stelle Töne, Bilder, Gerüche, Berührungen, Temperaturen, Bewegungen oder Beschleunigungsvorgänge an. Dem werden andere Identifikatoren gegenübergestellt, zum Beispiel Ortsangaben, die mit Hilfe von GPS oder GSM gewonnen wurden. Solche Identifikatoren können zusätzlich zu sensorischen Identifikatoren eingesetzt werden.

23 Patentanspruch 1 nimmt auf diese Definition zwar nicht ausdrücklich Bezug. Aus der in der Beschreibung enthaltenen Angabe, dass die Definition im Kontext des Streitpatents gilt, geht aber hinreichend deutlich hervor, dass sie für die Auslegung des Anspruchs maßgeblich sein soll.

24 Anhaltspunkte, die für ein anderes Verständnis sprechen könnten, sind der Patentschrift nicht zu entnehmen. Insbesondere kommt bei allen Ausführungsbeispielen ein sensorischer Identifikator im Sinne der genannten Definition zum Einsatz.

25 bb) Aus Merkmal 1.c folgt darüber hinaus, dass das System in der Lage sein muss, Darstellungen zu korrelieren, die sensorische Identifikatoren repräsentieren.

26 (1) Wie die Klägerin im Ansatz zutreffend geltend macht, sind die in den Merkmalen 1, 1.a und 1.b vorgesehenen Vorrichtungen (1, 2) zum Erfassen solcher Identifikatoren und zum Senden von Abfragemeldungen (RQ1, RQ2) allerdings nicht Teil des mit der erteilten Fassung von Patentanspruch 1 geschützten Systems (40, 50).

27 Das System muss lediglich geeignet sein, benachbarte Vorrichtungen zu identifizieren, die die genannten Funktionen aufweisen. Als insoweit relevanten Bestandteil des Systems führt Patentanspruch 1 nur die in Merkmal 1.c vorgesehenen Korrelationsmittel auf. Die Vorrichtungen zum Erfassen von Identifikatoren und zum Senden von Anfragemeldungen sind hingegen nur als Objekt angeführt, von denen die zu korrelierenden Darstellungen stammen und auf die sich der angestrebte Abgleich bezieht.

28 (2) Hieraus ergibt sich jedoch nicht, dass als zu korrelierende Darstellung im Sinne von Merkmal 1.c jede beliebige Datenfolge in Betracht kommt.

29 Merkmal 1.c lässt zwar offen, in welcher Weise die erfassten sensorischen Identifikatoren dargestellt werden. Aus der Anforderung, dass eine Darstellung solcher Identifikatoren zu korrelieren ist, ergibt sich aber, dass die Darstellung eine hinreichend sichere Zuordnung zu einem bestimmten Identifikator und auf dieser Grundlage eine sinnvolle Korrelation ermöglichen muss, d.h. einen Abgleich, der sinnvolle Rückschlüsse darauf zulässt, ob die dargestellten Identifikatoren einen inhaltlichen Bezug zueinander aufweisen.

30 cc) Auch vor diesem Hintergrund ergeben sich aus den Merkmalen 1 bis 1.c jedoch keine konkreten Vorgaben zur Entfernung zwischen benachbarten Geräten.

31 (1) Keines dieser Merkmale enthält konkrete Anforderungen an die maximale Entfernung oder die Genauigkeit, die sich aus der Korrelation ergeben müssen. Zudem gibt Merkmal 1.c nicht vor, nach welchen Kriterien die Korrelation zu erfolgen hat und unter welchen Voraussetzungen eine Übereinstimmung (match) zu bejahen ist.

32 Die in der Beschreibung enthaltenen Ausführungen, die übersandten und für das Korrelieren verwendeten Darstellungen seien vorzugsweise identisch oder zumindest ähnlich (Abs. 16), geben nur bevorzugte Ausgestaltungen an und haben in Patentanspruch 1 keinen Niederschlag gefunden.

33 (2) Die genannten Merkmale schreiben auch nicht vor, dass der erfasste Identifikator vom jeweils anderen Gerät ausgehen muss.

34 Als geeignetes Beispiel für einen sensorischen Identifikator schildert das Streitpatent einen Barcode, der von den Geräten (1, 2) eingescannt wird. Diesen Ausführungen ist nicht zu entnehmen, dass der Barcode fest mit einem Gerät verbunden sein muss. Als geeigneter Identifikator wird vielmehr auch ein räumliches oder temporäres Muster angeführt, das von einem Werbedisplay in einem Laden oder Schaufenster angezeigt wird (Abs. 38).

35 Diese Beispiele mögen auf der Annahme beruhen, dass beide Geräte dieselbe Vorlage zum Erfassen des Barcodes bzw. Musters verwenden. Unter dieser Prämisse deutet ein erfolgreicher Abgleich von zwei Darstellungen mit einiger Wahrscheinlichkeit darauf hin, dass die beiden Geräte, die die Darstellungen übersandt haben, nicht allzu weit voneinander entfernt sind - auch wenn zumindest theoretisch nicht auszuschließen ist, dass zwei räumlich voneinander entfernte Vorlagen verwendet wurden, die denselben Barcode oder dasselbe Muster zeigen. Eine konkrete Vorgabe für die Entfernung, die die Geräte voneinander aufweisen dürfen, ergäbe sich aber auch unter dieser Prämisse allenfalls dann, wenn festgelegt wäre, innerhalb welchen zeitlichen Abstands die beiden Erfassungsvorgänge stattgefunden haben müssen.

36 Solche Festlegungen enthält Patentanspruch 1 nicht.

37 c) Als Mittel für die in Merkmal 1.c vorgesehene Korrelation gibt Merkmal 1.e einen hierfür eingerichteten Server (5) vor.

38 aa) Dieser Server muss nach den Merkmalen 1.h und 1.i ferner dazu konfiguriert sein, Angaben zu einer auszuführenden Anwendung - etwa einem Spiel - miteinander zu vergleichen, die in den von den Vorrichtungen (1, 2) übermittelten Abfragemeldungen (RQ1, RQ2) enthalten sind.

39 bb) Nach Merkmal 1.j muss der Korrelationsserver ferner so eingerichtet sein, dass er bei übereinstimmenden Angaben zur Anwendung den Versand einer Abgleichsmeldung an einen durch die übereinstimmenden Angaben identifizierten Anwendungsserver veranlasst.

40 Zu Recht macht die Beklagte geltend, dass damit nicht festgelegt ist, auf welchem Weg die Abgleichsmeldung übermittelt wird.

41 In diesem Zusammenhang ist unerheblich, ob sich aus der Beschreibung unmittelbar und eindeutig ergibt, dass der Versandweg auch vom Korrelationsserver über eines der beiden benachbarten Geräte (1, 2) zum Anwendungsserver verlaufen kann. Selbst wenn diese Frage zu verneinen wäre, ergäbe sich daraus kein einschränkendes Verständnis von Patentanspruch 1. Dieser enthält weder ausdrückliche Vorgaben zum Versandweg noch sonstige Merkmale, die darauf hindeuten, dass der Versand nur auf Wegen erfolgen darf, die in den Ausführungsbeispielen ausdrücklich offenbart sind.

42 d) Aus dem Gesamtzusammenhang der Merkmale ergibt sich, dass eine Abgleichsmeldung im Sinne von Merkmal 1.j nur dann versandt wird, wenn sowohl die Korrelation nach Merkmal 1.c als auch der Abgleich nach Merkmal 1.i zu einem positiven Ergebnis (match) geführt haben.

43 Dies folgt aus Merkmal 1.d, wonach der Anwendungsserver zum Ausführen einer Anwendung vorgesehen ist, die durch den Korrelationsserver abgeglichen worden ist, und aus der Vorgabe, dass sowohl die Korrelation gemäß Merkmal 1.c als auch der Abgleich gemäß Merkmal 1.i durch den Korrelationsserver auszuführen sind, der vom Anwendungsserver verschieden ist. Diese Vorgabe ist nicht eingehalten, wenn der Korrelationsserver den identifizierten Anwendungsserver schon dann benachrichtigt, wenn der Abgleich nach Merkmal 1.i eine Übereinstimmung ergeben hat, und die Korrelation nach Merkmal 1.c am Ende doch dem Anwendungsserver überlassen bleibt.

44 Entgegen der Auffassung der Klägerin führt der Umstand, dass die Merkmale 1.c und 1.i schon dann verwirklicht sind, wenn der Korrelationsserver in der dort spezifizierten Weise ausgestaltet ist, nicht zu einer abweichenden Beurteilung. Die Klägerin geht zwar zu Recht davon aus, dass Patentanspruch 1 das beanspruchte System unabhängig davon schützt, in welcher Weise es verwendet wird. Aus der Vorgabe, dass Korrelationsserver und Anwendungsserver zu trennen sind, ergibt sich aber, dass die in Merkmal 1.j vorgesehene Abgleichsnachricht zur Weiterverarbeitung durch einen Anwendungsserver geeignet sein muss, der die Korrelation nach Merkmal 1.c nicht durchführen kann. Dies setzt voraus, dass an den Anwendungsserver nur dann eine Abgleichsmeldung versandt wird, wenn dieser seine Anwendungen den beiden als benachbart erkannten Geräten (1, 2) ohne weitere Korrelationsschritte zur Verfügung stellen kann.

45 e) Die in den Merkmalen 1.e, 1.f und 1.g vorgesehene Trennung zwischen (mindestens) einem Server, der die Korrelation nach Merkmal 1.c, den Abgleich nach Merkmal 1.i und den Versand der Abgleichsmeldung nach Merkmal 1.j durchführt, und (mindestens) einem anderen Server, der das in Merkmal 1.d vorgesehene Ausführen einer Anwendung übernimmt, ermöglicht es, denselben Korrelationsserver für unterschiedliche Anwendungen auf verschiedenen Servern zu verwenden und damit den in der Beschreibung des Streitpatents geschilderten Nachteil eines gemeinsamen Servers zu überwinden (Abs. 13).

46 Die genannten Merkmale geben nicht vor, in welcher Weise die Server für Korrelation und Anwendung voneinander zu trennen sind.

47 Aus der Funktion der Merkmale ergibt sich die Vorgabe, dass beide Server so eingerichtet sein müssen, dass sie die ihnen zugewiesenen Aufgaben grundsätzlich unabhängig voneinander ausführen können. Dies setzt nicht zwingend voraus, dass die Server auf unterschiedlichen Hardware-Einheiten betrieben werden.

48 II. Das Patentgericht hat seine Entscheidung im Wesentlichen wie folgt begründet:

49 Der Gegenstand der erteilten Fassung von Patentanspruch 1 gehe nicht über den Inhalt der ursprünglich eingereichten Unterlagen (veröffentlicht als WO 2010/134817 A2, NK4) hinaus. Patentanspruch 1 sei dahin auszulegen, dass eine "matching"-Nachricht im Sinne von Merkmal 1.j nur für Geräte versandt werden dürfe, die bereits als benachbart identifiziert worden seien. In der Ursprungsanmeldung sei auch kein weiterer Bestandteil des Korrelationsservers beschrieben, der zwingend erforderlich sei. Der in der Beschreibung geschilderte "message detector" sei integraler Bestandteil des Korrelationsservers.

50 Der Gegenstand von Patentanspruch 1 sei durch den Stand der Technik nicht vollständig vorweggenommen. Die US-Patentanmeldung 2007/0093258 (D1) offenbare nicht die Erfassung und Darstellung sensorischer Identifikatoren und die Übermittlung solcher Darstellungen in den gezeigten Anfragen. D1 offenbare auch nicht eine Anwendungskennung als Teil der Anfragenachricht. Schließlich fehle eine Nachricht an den Anwendungsserver. Entsprechendes gelte für die US-Patentanmeldung 2005/0277472 (D2). Das US-Patent 6 128 660 (D3) beschreibe lediglich allgemein und ohne Rücksicht auf eine räumliche Nähe ein "Matchen" von Geräten. Das europäische Patent 1 471 710 (D4) offenbare ebenfalls nicht die Verwendung sensorischer Identifikatoren.

51 Der Gegenstand von Patentanspruch 1 sei aber ausgehend von D11 durch das mit dem Fachbuch von Joines et al. (Performance Analysis for Java Web Sites, 2003, S. 102, Fig. 3.13, D6) und mit der internationalen Patentanmeldung 03/091894 (D7) belegte Fachwissen nahegelegt.

52 D11 offenbare ein Verfahren zum Identifizieren benachbarter Geräte unter Verwendung von Informationen aus sensorischen Identifikatoren. Es fehle lediglich an einer Trennung der Server für das Korrelieren und das Ausführen der gemeinsamen Anwendungen. Der Einsatz gesonderter Server ergebe sich jedoch aus dem Fachwissen.

53 Wenn nur ein System eingesetzt werde, sei es mit beschränkter Rechnerleistung bei steigender Nutzerzahl zwangsläufig notwendig, die Leistungsfähigkeit des Systems auf der Serverseite zu erhöhen, um das Angebot dauerhaft funktionsfähig zu erhalten. Dazu biete sich an, Serverfunktionalitäten aufzusplitten oder so zu verteilen, dass nicht alle Kapazitäten in einem einzigen Server zur Durchführung aller an diesen gestellten Anfragen vorgehalten werden müssen. Dieses als "Horizontal Scaling" bezeichnete Vorgehen sei etwa in D6 als generelles Fachwissen belegt. Zudem biete ein modularer Aufbau ohnehin ein weniger fehleranfälliges sowie meist leichter einzurichtendes, zu wartendes und zu aktualisierendes Umfeld.

54 Daher werde der Fachmann, ein Informatiker mit Universitätsabschluss und mehrjähriger Erfahrung in der Konzeption und praktischen Umsetzung von Diensten für Clients in einer Client-Server-Architektur, die mit den Merkmalen 1.h bis 1.j verbundenen Maßnahmen aufgrund seines Fachwissens umsetzen, ohne dass es erfinderischer Tätigkeit bedürfe. Als Beleg für das einschlägige Fachwissen diene D7, die eine praktisch ausgereifte Umsetzung aus einem vergleichbaren Umfeld (game server, online gaming context) lehre. Wie im Streitpatent würden dort Anwendungen auf mehreren separaten Servern (multiple lobby servers and application servers) verwirklicht und geeignete Maßnahmen im Vorfeld zu deren gemeinsamer Einbindung ins Gesamtsystem vorgenommen, etwa entsprechend auszutauschende "messages" mit die Anwendungen identifizierenden Inhalten.

55 Für den Gegenstand von Patentanspruch 15 gelte nichts anderes. Da die Beklagte die erteilte Fassung lediglich als geschlossenen Anspruchssatz verteidige, teilten die übrigen Ansprüche das Schicksal der Patentansprüche 1 und 15.

56 Hilfsantrag 0a, der vorsehe, dass die anfragenden Vorrichtungen (1, 2) zum beanspruchten System gehörten, sei auf eine Erweiterung des Schutzbereichs gerichtet. Unabhängig davon sei der damit verteidigte Gegenstand ebenfalls durch D11 in Verbindung mit dem mittels D7 belegten Fachwissen nahegelegt. Für Hilfsantrag 0b, der eine entsprechende Änderung nur für Patentanspruch 15 vorsehe, und für die Hilfsanträge 1a', 1b1' und 1b2' gelte im Ergebnis nichts anderes.

57 In der mit Hilfsantrag 1c verteidigten Fassung sei das Streitpatent hingegen rechtsbeständig. Das danach vorgesehene Merkmal, dass der Korrelationsserver die Abgleichsmeldung nicht unmittelbar an den Anwendungsserver versendet, sondern mittelbar über eine der benachbarten Vorrichtungen, sei in Figur 4b und den darauf bezogenen Passagen der Beschreibung ursprungsoffenbart. Dieses Merkmal sei durch den Stand der Technik weder vorweggenommen noch nahegelegt. Es erschließe sich nicht, weshalb der Fachmann nur aus seinem Fachwissen heraus den in Rede stehenden Kommunikationsweg einschlagen solle. Ein Wegeverlauf über die Geräte führe zu einer Verlängerung der Laufzeit und sei damit anfälliger für Fehler. Entsprechendes gelte für die Gegenstände der Patentansprüche 14 und 15.

58 III. Diese Würdigung hält der Überprüfung im Berufungsverfahren nur teilweise stand.

59 1. Zu Recht ist das Patentgericht zu dem Ergebnis gelangt, dass der Gegenstand des Streitpatents in der erteilten Fassung nicht patentfähig ist.

60 a) Zutreffend hat das Patentgericht entschieden, dass der Gegenstand von Patentanspruch 1 ausgehend von D11 durch allgemeines Fachwissen nahegelegt war.

61 aa) D11 befasst sich wie das Streitpatent mit der Identifikation benachbarter Mobilgeräte (S. 1 Z. 3-6).

62 D11 schildert den Stand der Technik und die darin bestehenden Schwierigkeiten im Ansatz gleich wie das Streitpatent (S. 1 Z. 7 bis S. 2 Z. 9).

63 Zur Lösung schlägt D11 ein Verfahren vor, bei dem Mobilgeräte sensorische Identifikatoren erfassen und Informationen darüber austauschen.

64 Sensorische Identifikatoren werden in D11 im Wesentlichen gleich beschrieben wie im Streitpatent (S. 9 Z. 31 bis S. 10 Z. 30).

65 Wenn ein Mobilgerät einen solchen Sensor erfasst hat, kann es ihn in einem ersten Schritt verifizieren. Hierzu kann auch ein Server eingesetzt werden (S. 11 Z. 14-16).

66 Nach erfolgreicher Erfassung und gegebenenfalls erfolgreicher Verifikation wird eine Anfrage (request message) an andere Mobilgeräte geschickt, zum Beispiel durch eine Rundmeldung (broadcast). Diese Nachricht enthält vorzugsweise eine Zahl oder einen alphanumerischen Code, durch den der Identifikator repräsentiert wird. Alternativ können Daten eingesetzt werden, die eine Zuordnung zu dem Identifikator ermöglichen (S. 11 Z. 16-27).

67 Wenn ein zweites Mobilgerät, das die Anfrage empfangen hat, denselben sensorischen Identifikator erfasst hat, schickt es eine Bestätigung (acknowledgement message) (S. 11 Z. 28-30). Auf diese Weise wird eine wechselseitige Identifizierung der Geräte ermöglicht (S. 12 Z. 9 f.).

68 Die mobilen Endgeräte können Mobiltelefone, Laptopcomputer oder Personal Digital Assistants sein. Es können aber auch Kommunikationssysteme zum Einsatz kommen, bei denen mobile Geräte teilweise oder vollständig von einem gemeinsamen Server gesteuert werden oder zumindest mit diesem kommunizieren. Ein Teil des Identifikationsprozesses kann dann von einem solchen Server ausgeführt werden (S. 14 Z. 28 bis S. 15 Z. 3).

69 Ein geeigneter Server kann einen Prozessor (µP), einen Speicher (M) und eine Kommunikationseinheit (C) umfassen. Der Prozessor kann für die Verifikation der sensorischen Identifikatoren eingerichtet sein. Dies hat den Vorteil, dass die Mobilgeräte keine entsprechende Hard- oder Software aufweisen müssen und deshalb relativ einfach und kostengünstig ausgestaltet werden können (S. 15 Z. 4-17).

70 Der Prozessor des Servers kann so eingerichtet sein, dass Meldungen über eine erfolgreiche Verifikation (verification confirmation messages) an die Mobilgeräte versendet werden. Diese Nachrichten können spezifisch für eine bestimmte Rolle des Geräts sein, zum Beispiel für ein Spiel oder eine andere Aktivität, die mit dem Gerät durchgeführt werden soll. Der Prozessor kann vorzugsweise auch eingesetzt werden, um Spielregeln für die Spiele anzuwenden, an denen das Mobilgerät beteiligt ist (S. 15 Z. 18-24).

71 Der Prozessor des Servers kann ferner so eingerichtet sein, dass er eine Liste von erfolgreichen Identifikationsvorgängen führt und den einzelnen Mobilgeräten unterschiedliche Rollen zuweist, zum Beispiel Rollen in unterschiedlichen Spielen (S. 8 Z. 26-28).

72 bb) Damit sind die Merkmale 1 bis 1.d und 1.f offenbart.

73 cc) Entgegen der Auffassung der Beklagten ist auch Merkmal 1.e offenbart.

74 (1) Wie die Beklagte im Ansatz zutreffend geltend macht, wird die Funktion eines Servers in D11 zunächst im Zusammenhang mit der Verifikation von sensorischen Identifikatoren näher beschrieben (S. 11 Z. 15 f.).

75 Wie die Klägerin zu Recht geltend macht, zeigt D11 jedoch auch die Möglichkeit auf, dass die Mobilgeräte ganz oder teilweise von einem Server gesteuert werden und dieser einen Teil der Identifikation ausführt (S. 14 Z. 28 bis S. 15 Z. 3). Sowohl der Systematik der Ansprüche 1 und 5 der D11 als auch der Beschreibung (S. 11 Z. 15 f.) lässt sich diesbezüglich entnehmen, dass es dabei nicht um die schon zuvor erwähnte Verifikation geht, die unabhängig von der Ausgestaltung der Endgeräte auf einen Server ausgelagert werden kann, sondern um Teile des Identifikationsvorgangs, die bei den zuvor geschilderten Ausführungsbeispielen auf den Endgeräten stattfinden und bei bestimmten Arten von Endgeräten ebenfalls auf einen Server ausgelagert werden können.

76 (2) Bei der zuletzt genannten Variante ist Merkmal 1.e verwirklicht.

77 (a) Der in D11 als Identifikation bezeichnete Vorgang ist eine Korrelation im Sinne von Merkmal 1.c, weil damit durch Vergleich von zwei sensorischen Identifikatoren oder deren Darstellungen ermittelt wird, ob zwei Mobilgeräte denselben Identifikator erfasst haben. Diese Identifikation kann nach D11 wahlweise auf einem Server stattfinden.

78 (b) Dem steht nicht entgegen, dass D11 in diesem Zusammenhang nur von einem Teil des Identifikationsprozesses spricht.

79 Patentanspruch 1 gibt nicht im Einzelnen vor, welche Korrelationsschritte auf dem Server durchgeführt werden, und schließt nicht aus, dass vorbereitende oder nachgelagerte Schritte auf einem Endgerät ausgeführt werden.

80 (c) Keiner abschließenden Entscheidung bedarf in diesem Zusammenhang die Frage, ob der Server, den D11 für die Identifikation vorschlägt, derselbe ist wie derjenige, der die Verifikation durchführt.

81 Eine Verifikation ist in Patentanspruch 1 nicht vorgesehen und auch nach D11 nur optional. Unabhängig davon lässt Merkmal 1.e ausdrücklich die Möglichkeit offen, dass mehrere Korrelationsserver zum Einsatz kommen. Dies umfasst Ausgestaltungen, bei denen jeder Server nur einen Teil des Korrelationsprozesses ausführt.

82 dd) Nicht offenbart sind in D11 die Merkmale 1.g bis 1.j.

83 ee) Zu Recht ist das Patentgericht zu dem Ergebnis gelangt, dass eine Ausgestaltung gemäß Merkmal 1.g ausgehend von D11 nahelag.

84 Nach der Rechtsprechung des Senats kann die Anwendung eines bestimmten Mittels auch ohne entsprechende Anregung naheliegen, wenn dieses als ein generelles, für eine Vielzahl von Anwendungsfällen in Betracht zu ziehendes Mittel seiner Art nach zum allgemeinen Fachwissen des angesprochenen Fachmanns gehört, die Nutzung der in Rede stehenden Funktionalität sich in dem zu beurteilenden Zusammenhang als objektiv zweckmäßig darstellt und keine besonderen Umstände feststellbar sind, die eine Anwendung aus fachlicher Sicht als nicht möglich, mit Schwierigkeiten verbunden oder sonst untunlich erscheinen lassen (vgl. nur BGH, Urteil vom 11. März 2014 - X ZR 139/10, GRUR 2014, 647 Rn. 26 - Farbversorgungssystem; Urteil vom 3. September 2024 - X ZR 106/22, GRUR 2024, 1790 Rn. 43 - Scheibenbremse III).

85 Diese Voraussetzungen sind im Streitfall erfüllt.

86 (1) Nach den Feststellungen des Patentgerichts gehörte es im Stand der Technik zum allgemeinen Fachwissen, dass es von Vorteil sein kann, Serverfunktionalitäten auf verschiedene Server zu verteilen.

87 Die Beklagte zeigt keine konkreten Anhaltspunkte auf, die Zweifel an der Vollständigkeit oder Richtigkeit dieser Feststellung begründen (§ 117 PatG und § 529 Abs. 1 Nr. 1 ZPO).

88 Entgegen der Auffassung der Beklagten hat das Patentgericht seine Feststellung nicht auf D7 gestützt. Es hat vielmehr ausgeführt, dass es sich um ein allgemeines Lösungsprinzip handelt, das zum Beispiel in einem von der Klägerin zitierten Lehrbuch (D6) beschrieben und in D7 zur Anwendung gelangt ist.

89 Das Patentgericht hat sich in diesem Zusammenhang nicht auf Einzelheiten des in D7 vorgeschlagenen Systems bezogen, sondern als ausschlaggebend angesehen, dass das eingangs genannte Lösungsprinzip in die praktisch ausgereifte Umsetzung aus D7 Eingang gefunden hat.

90 Entgegen der Auffassung der Beklagten ergibt sich keine abweichende Beurteilung daraus, dass die vom Patentgericht herangezogenen Ausführungen in D6 (S. 102 f. mit Fig. 3.13) das "Horizontal Scaling" hervorheben, also die Möglichkeit, gleichartige Aufgaben auf eine Vielzahl von Servern zu verteilen. Aus diesen Ausführungen geht zugleich hervor, dass unterschiedliche Aufgaben auf mehrere Server verteilt werden können, wie dies Figur 3.13 beispielhaft für http- und Applikationsserver zeigt.

91 (2) Der Einsatz dieses Mittels stellte sich auch im Kontext von D11 als objektiv zweckmäßig dar.

92 (a) Ausgehend von D11 bestand Anlass, sich näher mit der Frage zu befassen, welche Teile des Vorgangs auf welcher Einheit durchgeführt werden sollen.

93 D11 lässt offen, welche Einheit für die Ausführung des vom Nutzer gewünschten Spiels eingesetzt wird. Der zur Verifikation eingesetzte Server kann zwar vorzugsweise zugleich zur Anwendung von Spielregeln eingesetzt werden (S. 15 Z. 23 f.). Selbst wenn dies dahin zu verstehen wäre, dass der Server zugleich als Anwendungsserver im Sinne von Merkmal 1.f des Streitpatents fungiert, ist diese Ausgestaltung nach D11 aber nur optional.

94 Darüber hinaus ist D11 nicht eindeutig zu entnehmen, ob der Server, der optional zur Identifikation eingesetzt wird, derselbe ist, auf dem die Verifikation erfolgt. Auch deshalb bestand ungeachtet der in D11 angedeuteten Präferenz Anlass, andere Lösungsmöglichkeiten in Betracht zu ziehen.

95 (b) D11 zeigt sowohl im Zusammenhang mit der Verifikation als auch mit der Identifikation auf, dass diese Schritte wahlweise auf einem Endgerät oder auf einem Server durchgeführt werden können.

96 Daraus ergibt sich, dass die Einheit, auf der diese Aufgaben durchgeführt werden, im Wesentlichen nach Gründen der Zweckmäßigkeit ausgewählt werden kann. Bei der Implementierung auf einem Server stand folglich die Möglichkeit offen, einzelne Aufgaben auf verschiedenen Servern auszuführen, wie dies als allgemeines Lösungsmittel bekannt war.

97 (3) Besondere Schwierigkeiten, die den Einsatz dieses Lösungsmittels im Kontext von D11 als untunlich erscheinen lassen könnten, sind weder aufgezeigt noch sonst ersichtlich.

98 ff) Vor diesem Hintergrund hat das Patentgericht zu Recht entschieden, dass ausgehend von D11 auch die Merkmale 1.h, 1.i und 1.j nahegelegen haben.

99 (1) Die Ausführungen in D11, wonach der zur Verifikation eingerichtete Server zugleich so eingerichtet sein kann, dass er eine auf ein bestimmtes Spiel oder eine bestimmte andere Anwendung bezogene Bestätigungsmeldung ausgibt, legen zumindest nahe, dass das Endgerät in der Anfrage auch Angaben zu einer bestimmten Anwendung macht, damit der Server eine darauf bezogene Meldung erstellen kann, und dass nur dann ein positives Ergebnis des Abgleichs gemeldet wird, wenn beide Anfragen dieselbe Anwendung betreffen.

100 Selbst wenn zugunsten der Beklagten unterstellt wird, dass dieser Server nicht die in D11 geschilderte Identifikation durchführt, lag es jedenfalls nahe, solche Angaben gegebenenfalls auch an den zur Identifikation eingesetzten Server zu senden und dessen positive Antwort davon abhängig machen, dass die Angaben zur Anwendung übereinstimmen.

101 Die Identifikation dient nach D11 dem Zweck, Mobilgeräte in den Stand zu versetzen, miteinander in Transaktion zu treten (S. 12 Z. 24 f.). Damit dieser Zweck erreicht wird, ist es sinnvoll, eine erfolgreiche Identifikation nur dann zu bestätigen, wenn in der Anfrage mitgeteilt wird, für welche Anwendung die Identifikation erfolgen soll, und wenn diese Angaben übereinstimmen.

102 (2) Eine solche Vorgehensweise wird zusätzlich durch den erwähnten Hinweis in D11 nahegelegt, dass der Server optional eine Liste von erfolgreichen Identifikationsvorgängen führen und den einzelnen Mobilgeräten unterschiedliche Rollen zuweisen kann.

103 Wenn der Server diese Aufgaben wahrnimmt, ist es zweckmäßig, ihn nicht nur mit der Verifikation, sondern auch mit der Identifikation zu betrauen und in diesem Zusammenhang Angaben zu derjenigen Anwendung zu übermitteln, für die die Identifikation erfolgen soll.

104 (3) Eine Trennung zwischen Identifikations- und Anwendungsserver, wie sie aus den oben genannten Gründen durch das Fachwissen nahegelegt war, hat ferner zur Folge, dass die Meldung über den erfolgreichen Abgleich auch den Anwendungsserver erreichen muss, damit dieser die in Rede stehende Anwendung für die erfolgreich identifizierten Endgeräte freigeben kann.

105 2. Ebenfalls zu Recht hat das Patentgericht entschieden, dass das Streitpatent auch in der Fassung von Hilfsantrag 0a keinen Bestand hat.

106 a) Nach Hilfsantrag 0a soll die erteilte Fassung von Patentanspruch 1 wie folgt geändert werden:

107 1

A system (40, 50) for identifying proximate devices (1, 2),

System (40, 50) zum Identifizieren benachbarter Vorrichtungen (1, 2).

1.a'

the system comprising:

said devices, wherein said proximate devices are arranged for detecting a sensory identifier (ID)

Das System umfasst:

die genannten benachbarten Vorrichtungen, die eingerichtet sind zum Erfassen eines sensorischen Identifikators (ID)

1.b'

and transmitting request messages (RQ1, RQ2), comprising representations of the detected sensory identifier,

und zum Senden von Anfragemeldungen (RQ1, RQ2) mit Darstellungen des erfassten sensorischen Identifikators.

108 b) Die erteilte Fassung von Patentanspruch 15 soll korrespondierend hierzu wie folgt geändert werden:

109 15

A method of identifying proximate devices (1, 2)

Verfahren zum Identifizieren benachbarter Vorrichtungen (1, 2)

15.a'

arranged for the method comprising the steps of:

detecting a sensory identifier (ID) by said devices

eingerichtet zum Das Verfahren umfasst folgende Schritte:

Erfassen eines sensorischen Identifikators (ID) durch die genannten Vorrichtungen

15.b'

and transmitting request messages (RQ1, RQ2), comprising representations of the detected sensory identifier by said devices,

und Senden von Anfragemeldungen (RQ1, RQ2) mit Darstellungen des erfassten sensorischen Identifikators durch die genannten Vorrichtungen.

110 c) Wie das Patentgericht zu Recht entschieden hat, war dieser Gegenstand aus denselben Gründen naheliegend wie der Gegenstand der erteilten Fassung von Patentanspruch 1.

111 3. Hilfsantrag 0b unterliegt derselben Beurteilung.

112 Nach Hilfsantrag 0b soll nur Patentanspruch 15 in der oben dargestellten Weise geändert werden. In dieser Fassung kann das Patent aus den bereits dargelegten Gründen ebenfalls keinen Bestand haben.

113 4. Für den erstmals in der Berufungsinstanz gestellten Hilfsantrag 0a' gilt nichts anderes.

114 Nach Hilfsantrag 0a' sollen in den Patentansprüchen 1 und 15 die Merkmale 1.a und 1.b bzw. 15.a und 15.b aus der erteilten Fassung mit den Merkmalen 1.a' und 1.b' bzw. 15.a' und 15.b' gemäß Hilfsantrag 0a kombiniert werden.

115 Diese Doppelung vermag nicht zu einer abweichenden Beurteilung zu führen.

116 5. Die Hilfsanträge 1a', 1b1' und 1b2' haben ebenfalls keinen Erfolg.

117 a) Nach allen diesen Hilfsanträgen sollen die Patentansprüche 1 und 15 um folgendes Merkmal ergänzt werden:

118 1.k

wherein the match message is transmitted from the at least one correlation server to the application server through one of the proximate devices.

Die Abgleichsmeldung wird vom Korrelationsserver über eine der benachbarten Vorrichtungen zum Anwendungsserver übermittelt.

119 b) Nach Hilfsantrag 1a' sollen die Patentansprüche 1 und 15 ferner um die beiden zusätzlichen Merkmale aus Hilfsantrag 0a' ergänzt werden.

120 Nach Hilfsantrag 1b1' soll nur Patentanspruch 1 diese zusätzliche Änderung erfahren, nach Hilfsantrag 1b2' nur Patentanspruch 15.

121 c) Die mit den Hilfsanträgen 1a', 1b1' und 1b2' verteidigten Gegenstände sind nicht patentfähig.

122 aa) Die Merkmale 1.a' und 1.b' sind aus denselben Gründen im Stand der Technik offenbart wie die Merkmale 1.a und 1.b.

123 bb) Die vom Patentgericht im Zusammenhang mit Hilfsantrag 1c angestellten Erwägungen zu Merkmal 1.k halten der Überprüfung im Berufungsverfahren nicht stand.

124 Zur Bejahung einer erfinderischen Tätigkeit reicht es nicht aus, wenn die vom Streitpatent vorgeschlagene technische Lösung aus der Sicht des Standes der Technik mit Nachteilen oder ihre Realisierung mit Schwierigkeiten verbunden ist, die vorgeschlagenen Lösungsbeispiele diese Nachteile oder Schwierigkeiten aber ignorieren und schlicht in Kauf nehmen (BGH, Urteil vom 24. April 2018 - X ZR 50/16, GRUR 2018, 1128 Rn. 37 - Gurtstraffer).

125 Bei Anlegung dieses Maßstabs vermag die vom Patentgericht angestellte Erwägung, die Ausgestaltung nach Merkmal 1.k sei nicht naheliegend, weil sie mit Nachteilen verbunden sei, die angefochtene Entscheidung nicht zu tragen.

126 cc) Die angefochtene Entscheidung stellt sich insoweit nicht aus anderen Gründen als richtig dar (§ 119 Abs. 1 PatG).

127 (1) Wie die Beklagte zu Recht geltend macht, ist die Ausgestaltung nach Merkmal 1.k allerdings nicht technisch unsinnig.

128 Eine Kommunikation zwischen den beteiligten Servern auf dem Umweg über eine der benachbarten Vorrichtungen mag die vom Patentgericht angeführten Nachteile in Bezug auf Laufzeit und Fehleranfälligkeit aufweisen.

129 Die Beklagte weist aber zu Recht darauf hin, dass diese Ausgestaltung jedenfalls nicht unsinnig ist, weil im Ergebnis sowohl der Anwendungsserver als auch die benachbarten Vorrichtungen eine Information über einen erfolgreichen Abgleich benötigen. Hierbei mag ein unmittelbarer Versand von Server zu Server Vorteile bieten, wenn die beiden Server räumlich oder netzwerktechnisch nahe zueinander angeordnet sind. Der Gegenstand des Streitpatents ist aber nicht auf eine solche Anordnung beschränkt. Unabhängig davon ist eine zuverlässige und schnelle Benachrichtigung des Anwendungsservers von beschränktem Wert, wenn die Kommunikationswege zu den benachbarten Vorrichtungen nicht zur Verfügung stehen oder langsam sind.

130 (2) Entgegen der Auffassung des Patentgerichts ergab sich jedoch schon ausgehend von D11 Anlass, auch eine indirekte Kommunikation zwischen dem Korrelationsserver und dem Anwendungsserver in Betracht zu ziehen.

131 (a) Wie oben im Einzelnen aufgezeigt wurde, beschreibt D11 eine direkte Kommunikation zwischen den beteiligen Mobilgeräten, schlägt aber für verschiedene Funktionen optional die Einschaltung eines Servers vor, ohne insoweit konkrete Kommunikationspfade aufzuzeigen. Dies gab Anlass, über mögliche Ausgestaltungen nachzudenken.

132 Vor dem oben aufgezeigten Hintergrund boten sich eine direkte Kommunikation zwischen den beteiligten Servern und eine Kommunikation über die Mobilgeräte dafür gleichermaßen an. Selbst wenn eine direkte Kommunikation gewisse Vorteile bieten mag, sind diese nicht so eindeutig, dass eine indirekte Verbindung von vornherein ausscheidet.

133 (b) Angesichts dessen vermag die Auswahl zwischen einer dieser Ausgestaltungen nicht zur Bejahung erfinderischer Tätigkeit zu führen.

134 Wenn zur Lösung eines Problems mehrere Alternativen in Betracht kommen können, können auch mehrere von ihnen naheliegend sein. Hierbei ist es grundsätzlich ohne Bedeutung, welche der Lösungsalternativen der Fachmann als erste in Betracht zöge (BGH, Urteil vom 24. April 2018 - X ZR 50/16, GRUR 2018, 1128 Rn. 41 - Gurtstraffer).

135 6. Hinsichtlich der weiteren Hilfsanträge ergibt sich keine abweichende Beurteilung.

136 a) Der mit Hilfsantrag 1c verteidigte Gegenstand ist entgegen der Auffassung des Patentgerichts nicht patentfähig.

137 Nach Hilfsantrag 1c soll die erteilte Fassung von Patentanspruch 1 um das oben dargestellte Merkmal 1.k ergänzt werden. Diese Ausgestaltung war aus den oben aufgezeigten Gründen durch den Stand der Technik nahegelegt.

138 b) Für die Hilfsanträge 1a und 1b gilt nichts anderes.

139 Nach diesen Hilfsanträgen sollen die Änderungen nach den Hilfsanträgen 0a und 0b um das Merkmal 1.k ergänzt werden.

140 Auch diese Kombination ist aus den genannten Gründen nicht patentfähig.

141 c) Die Hilfsanträge 2a, 2b, 2a', 2b' und 2c unterliegen ebenfalls keiner anderen Beurteilung.

142 aa) Nach diesen Hilfsanträgen sollen die Anspruchsfassungen verschiedener vorangegangener Hilfsanträge wie folgt ergänzt werden:

143 1.j'

and causing a transmitter (88) to transmit in response to a successful match the match message based on the match to an application server identified by the matching indications of the application in the matched request messages,

und einen Sender (88) in Reaktion auf einen erfolgreichen Abgleich zum Versenden einer auf der Übereinstimmung basierenden Abgleichsmeldung an einen Anwendungsserver zu veranlassen, der durch die übereinstimmenden Angaben der Anwendung in den abgleichenden Anfragemeldungen identifiziert wird.

144 bb) Daraus ergibt sich keine zusätzliche Einschränkung.

145 Dass die Abgleichsmeldung nur nach einem erfolgreichen Abgleich der Angaben zur auszuführenden Anwendung versendet wird, ergibt sich aus den oben dargelegten Gründen schon aus der erteilten Fassung von Merkmal 1.j.

146 d) Die mit den übrigen Hilfsanträgen verteidigten Gegenstände sind ebenfalls nicht patentfähig.

147 aa) Nach diesen Hilfsanträgen sollen die mit zahlreichen vorangegangenen Hilfsanträgen verteidigten Fassungen zusätzlich wie folgt ergänzt werden:

148 1.j''

and causing a transmitter (88) to transmit in response to a successful match the match message based on the match and including an object indicative of the successful match to an application server identified by the matching indications of the application in the matched request messages,

und einen Sender (88) in Reaktion auf einen erfolgreichen Abgleich zum Versenden einer auf der Übereinstimmung basierenden, ein den erfolgreichen Abgleich anzeigendes Objekt enthaltenden Abgleichsmeldung an einen Anwendungsserver zu veranlassen, der durch die übereinstimmenden Angaben der Anwendung in den abgleichenden Anfragemeldungen identifiziert wird.

149 bb) Ob dies zu einer sachlichen Einschränkung führt, kann dahingestellt bleiben.

150 Jedenfalls lag es nahe, eine Meldung, die nach einem erfolgreichen Abgleich versandt wird, mit einem Inhalt zu versehen, der auf dieses Ergebnis hinweist.

151 7. Der Gegenstand der gesondert verteidigten Ansprüche ist ebenfalls nicht patentfähig.

152 a) Der Gegenstand von Patentanspruch 2 liegt ausgehend von D11 ebenfalls nahe.

153 aa) Patentanspruch 2 sieht ergänzend folgendes Merkmal vor:

154 1.l

the correlation server is configured to generate a session identifier in response to the detected match and to transmit the session identifier back to the proximate devices involved in the match, and to generate a further message specifying the session identifier and identifiers of the matched devices to the application server

Der Korrelationsserver ist so konfiguriert, dass er als Reaktion auf das erfasste Abgleichen einen Sitzungsidentifikator generiert und diesen an die an dem Abgleichen beteiligten benachbarten Vorrichtungen zurücksendet und eine weitere den Sitzungsidentifikator spezifizierende Meldung und Identifikatoren der abgeglichenen Vorrichtungen zum Anwendungsserver generiert.

155 bb) Der damit spezifizierte Sitzungsidentifikator ermöglicht es nach der Beschreibung, die mobilen Geräte für Zwecke der Korrelation und der Anwendung zu identifizieren, untereinander aber anonym zu halten (Abs. 73).

156 cc) Eine solche Ausgestaltung lag, wie die Klägerin bereits in der Klageschrift dargelegt hat, innerhalb dessen, was D11 mit dem Vorschlag, den beteiligten Mobilgeräten eine bestimmte Rolle zuzuweisen, angeregt hat.

157 Dass hierbei auch Aspekte des Datenschutzes berücksichtigt werden, vermag eine erfinderische Tätigkeit nicht zu begründen.

158 b) Für Patentanspruch 4 gilt Entsprechendes.

159 aa) Nach Patentanspruch 4 soll folgendes Merkmal hinzugefügt werden:

160 1.m

the system comprising a plurality of application servers for performing mutually different applications, the request messages each indicating at least one of said applications, the at least one correlation server (5) being configured to determine whether the request messages with correlated representations received from the devices (1, 2) indicate a same one of the applications and to match the devices (1, 2) only if this is the case.

Das System umfasst eine Vielzahl von Anwendungsservern zum Ausführen voneinander unterschiedlicher Anwendungen, wobei die Anfragemeldungen mindestens eine der Anwendungen anzeigen, wobei mindestens ein Korrelationsserver (5) dazu konfiguriert ist, um zu bestimmen, ob die Anfragemeldungen mit den korrelierten Darstellungen, die von den Vorrichtungen (1, 2) empfangen werden, dieselbe Anwendung anzeigen, und die Vorrichtungen (1, 2) nur dann abzugleichen, wenn dies der Fall ist.

161 bb) Dies betrifft nur handwerkliche Details der durch den Stand der Technik nahegelegten Ausgestaltung gemäß Patentanspruch 1 und vermag ebenfalls nicht zur Bejahung erfinderischer Tätigkeit zu führen.

162 c) Patentanspruch 5 unterliegt keiner abweichenden Beurteilung.

163 aa) Patentanspruch 5 ist auf Anspruch 4 zurückbezogen und sieht das folgende zusätzliche Merkmal vor:

164 1.n

the correlation server (5) is configured to transmit a match message to a selected one of the application servers in response to detection that the request messages received from the devices (1, 2) contain correlated representations and indicate a same one of the applications, a selected one of the application servers being selected according to whether it performs said same one of the applications.

Der Korrelationsserver (5) ist dazu konfiguriert, eine Abgleichsmeldung an einen ausgewählten der Anwendungsserver als Reaktion auf das Erfassen zu senden, dass die von den Vorrichtungen (1, 2) empfangenen Anfragemeldungen korrelierte Darstellungen enthalten und eine gleiche der Anwendungen angeben, wobei einer der Anwendungsserver, je nachdem, ob er dieselbe der Anwendungen ausführt, ausgewählt wird.

165 bb) Auch dies betrifft nur untergeordnete Details der Ausgestaltung.

166 d) Für Patentanspruch 6 ergibt sich keine abweichende Beurteilung.

167 aa) Patentanspruch 6 sieht ergänzend folgendes Merkmal vor:

168 1.q

the at least one application server (6) is arranged for communicating with the devices (1, 2) directly, at least after receiving a match message indicating the devices based on detection of said correlation from the correlation server.

Der mindestens eine Anwendungsserver (6) ist dazu eingerichtet, direkt mit den Vorrichtungen (1, 2) zu kommunizieren, mindestens nachdem er eine Abgleichsmeldung empfangen hat, die die Vorrichtungen auf Grundlage des Erfassens dieser Korrelation vom Korrelationsserver angibt.

169 bb) Eine direkte Kommunikation zwischen dem Anwendungsserver und den benachbarten Vorrichtungen (1, 2) war aus den zu Merkmal 1.k dargelegten Gründen in gleicher Weise nahegelegt wie eine indirekte Kommunikation.

170 e) Der Gegenstand von Patentanspruch 10 ist ebenfalls nicht patentfähig.

171 aa) Patentanspruch 10 sieht ergänzend folgendes Merkmal vor:

172 1.r

the system comprising at least two correlation servers (5), further comprising at least one proxy server for routing request messages (RQ1, RQ2) from the devices (1, 2) to a correlation server (5), the at least one proxy server preferably being arranged for routing in dependence of the sensory identifier (ID).

Das System umfasst mindestens zwei Korrelationsserver (5), ferner mindestens einen Proxy-Server zum Weiterleiten von Anfragemeldungen (RQ1, RQ2) von den Vorrichtungen (1, 2) an einen Korrelationsserver (5), wobei der mindestens eine Proxy-Server vorzugsweise zum Weiterleiten in Abhängigkeit von dem sensorischen Identifikator (ID) angeordnet ist.

173 bb) Auch dies betrifft einzelne Details der Ausgestaltung, die nicht zur Bejahung erfinderischer Tätigkeit zu führen vermögen.

174 f) Für Patentanspruch 11 gilt nichts anderes.

175 aa) Patentanspruch 11 ist auf Anspruch 10 zurückbezogen und sieht zusätzlich folgendes Merkmal vor:

176 1.s

wherein the at least one proxy server is configured to associate each correlation server with a predetermined range of values of the sensory identifier, a base station through which the request message is transmitted, a type of the sensory identifier and/or a combination of part or all of these properties, and to route each respective request messages (RQ1, RQ2) from the devices (1, 2) to a selected one or a selected plurality of correlation servers (5), associated with the range or ranges in which a value of the sensory identifier, the source cell through which the respective request message is transmitted, a type of the sensory identifier and/or a combination of part or all of these properties lies.

Der mindestens eine Proxy-Server ist dazu konfiguriert, jeden Korrelationsserver mit einem vorbestimmten Wertebereich des sensorischen Identifikators, einer Basisstation, durch die die Anfragemeldung gesendet wird, einem Typ des sensorischen Identifikators und/oder einer Kombination aus einem Teil oder allen dieser Eigenschaften zu verbinden, und die jeweiligen Anfragemeldungen (RQ1, RQ2) von den Vorrichtungen (1, 2) zu einem ausgewählten oder einer ausgewählten Vielzahl von Korrelationsservern (5) weiterzuleiten, die mit dem Bereich oder Bereichen verbunden sind, in denen ein Wert des sensorischen Identifikators, die Quellzelle, durch die die jeweilige Anfragemeldung gesendet wird, eine Art des sensorischen Identifikators und/oder eine Kombination aus einem Teil oder allen diesen Eigenschaften liegt.

177 bb) Dies betrifft einzelne Details der Aufgabenverteilung zwischen den einzelnen Servern, die nicht als erfinderisch angesehen werden können.

178 g) Patentanspruch 17 unterliegt ebenfalls keiner abweichenden Beurteilung.

179 aa) Patentanspruch 17 sieht ergänzend zu Anspruch 15 folgendes Merkmal vor:

180 15.t

the step of correlating takes previous matches into account.

Der Schritt des Korrelierens berücksichtigt früheres Abgleichen.

181 bb) Diese Vorgehensweise lag schon aus Gründen der Effizienz nahe.

182 IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG in Verbindung mit § 97 Abs. 1 und § 91 Abs. 1 Satz 1 ZPO.

Bacher

Deichfuß

Kober-Dehm

Marx

Rensen
