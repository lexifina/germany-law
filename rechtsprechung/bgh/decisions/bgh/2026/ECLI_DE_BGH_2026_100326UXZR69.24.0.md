---
ecli: "ECLI:DE:BGH:2026:100326UXZR69.24.0"
court: "Bundesgerichtshof"
aktenzeichen: "X ZR 69/24"
decided: "2026-03-10"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/KORE600142026.xml"
neuris_doknr: "KORE600142026"
---

# Bundesgerichtshof, X ZR 69/24 vom 2026-03-10

## Tenor

Die Berufung gegen das Urteil des 2. Senats (Nichtigkeitssenats) des Bundespatentgerichts vom 14. März 2024 wird auf Kosten der Beklagten zurückgewiesen.

Von Rechts wegen

## Tatbestand

1 Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik Deutschland erteilten europäischen Patents 2 723 094 (Streitpatents), das am 18. Oktober 2013 unter Inanspruchnahme sechs US-amerikanischer Prioritäten aus dem Zeitraum vom 18. Oktober 2012 bis 3. Januar 2013 angemeldet worden ist und eine Digitalempfängerarchitektur mit anwendungsbasierten Sicherheitsdefinitionen betrifft.

2 Patentanspruch 1, auf den fünf weitere Ansprüche zurückbezogen sind, lautet in der Verfahrenssprache:

A method for execution in a media processing device (100)

to establish media pathways in the media processing device (100) having at least one software application (124, 322) and a plurality of selectable components for use in supporting media pathways, the method comprising:

identifying a plurality of potential operational modes of the media processing device (100), each of the operational modes specifying for each of a plurality of pathway nodes a respective set of selectable components, each of the plurality of pathway nodes forming at least a portion of the media pathway (314, 316, 318);

determining a certification requirement associated with the software application (124, 322);

selecting one of the plurality of potential operational modes for use in media-related operations involving the software application (124, 322), wherein the selected operational mode is compliant with the certification requirement;

selecting for each of the plurality of pathway nodes a selectable component in the respective set of selectable components in accordance with the selected operational mode to form at least a portion of a media pathway (314, 316, 318); and

performing media-related operations utilizing the media pathway (314, 316, 318).

3 Patentanspruch 7 schützt sinngemäß eine Vorrichtung, die zur Ausführung dieses Verfahrens geeignet ist.

4 Die Klägerin macht geltend, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei nicht patentfähig. Der Beklagte hat das Streitpatent in der erteilten Fassung und hilfsweise in elf geänderten Fassungen verteidigt.

5 Das Patentgericht hat das Streitpatent für nichtig erklärt.

6 Dagegen richtet sich die Berufung der Beklagten, die das Streitpatent mit ihren erstinstanzlichen Anträgen verteidigt. Die Klägerin tritt dem Rechtsmittel entgegen.

## Entscheidungsgründe

7 Die zulässige Berufung ist unbegründet.

8 I. Das Streitpatent betrifft Systeme zur Verarbeitung von Medien, zum Beispiel Set-Top-Boxen.

9 1. Nach der Beschreibung des Streitpatents unterliegen solche Systeme strengen Zertifizierungsprozessen.

10 Um ein Zertifikat zu erlangen, sei üblicherweise volle Ende-zu-Ende-Sicherheit erforderlich. Bei Set-Top-Boxen und ähnlichen Geräten müsse hierfür häufig zum Herstellungszeitpunkt ein digitales Zertifikat in das Gerät eingebettet werden (Abs. 2). Da ungesicherte, nicht isolierte Teile eines Medienpfads zum Fehlschlagen der Zertifizierung führten, böten herkömmliche Geräte meist nur einen einzigen, sicheren und zertifizierten Pfad an. Bei neueren Multiprozessor-Geräten trenne eine feste Hardware-Grenze den herkömmlichen zertifizierten Pfad von unsicheren Komponenten (Abs. 3).

11 Ein typisches Android-Framework, auf dem mehrere Anwendungen gleichzeitig liefen, isoliere zwar grundsätzlich die einzelnen Anwendungen voneinander. Dieser Schutz sei aber für eine Zertifizierung nicht ausreichend. Beispielsweise könne eine Anwendung, welche einen Code von einem nicht verifizierten Anbieter empfange, Schwachstellen in einem anderen Code ausnutzen und durch unbefugten Zugriff auf Dateisysteme die Sicherheit des Geräts gefährden (Abs. 5).

12 Bei Multiprozessor-Systemen werde der erforderliche Schutz üblicherweise über Zugangsberechtigungen und eine strikte Trennung der Anwendungen und Daten erzielt, etwa durch den Einsatz virtuellen Speichers, der nur für den jeweiligen Prozessor sichtbar und für externe Prozesse nicht zugänglich sei (Abs. 6). In einer Set-Top-Box, die Zugang zu Fernsehsignalen und zum Internet biete, sei üblicherweise nicht erwünscht, dass der Benutzer oder andere Personen aus der unsicheren Umgebung heraus Zugang zu den Anwendungen für Rundfunk oder Premiumkanäle hätten. Wenn der Zugang zu den beiden Umgebungen durch dieselbe Software gesteuert werde, bestehe jedoch ein erhöhtes Risiko von Zugriffsverletzungen, was zu einem Eindringen aus der unsicheren in die sichere Zone führen könne (Abs. 7).

13 2. Vor diesem Hintergrund betrifft das Streitpatent das technische Problem, nicht vertrauenswürdige Frameworks und Anwendungen in eine sichere Betriebssystemumgebung zu integrieren und zugleich Konformität und Flexibilität in Bezug auf geltende Zertifizierungs- und Sicherheitsmaßnahmen zu gewährleisten (Abs. 8).

14 3. Zur Lösung schlägt das Streitpatent in Anspruch 1 ein Verfahren vor, dessen Merkmale sich wie folgt gliedern lassen:

15 1

A method for execution in a media processing device (100)

Verfahren zur Ausführung in einer Medienverarbeitungseinrichtung (100),

1.1

to establish media pathways in the media processing device (100) having at least one software application (124, 322) and a plurality of selectable components for use in supporting media pathways, the method comprising:

um in der Medienverarbeitungseinrichtung (100), die wenigstens eine Softwareanwendung (124, 322) und eine Mehrzahl auswählbarer Komponenten zur Verwendung bei der Unterstützung von Medienpfaden aufweist, Medienpfade zu erstellen, wobei das Verfahren umfasst:

1.2

identifying a plurality of potential operational modes of the media processing device (100), each of the operational modes specifying for each of a plurality of pathway nodes a respective set of selectable components, each of the plurality of pathway nodes forming at least a portion of the media pathway (314, 316, 318);

Ermitteln einer Mehrzahl möglicher Betriebsmodi der Medienverarbeitungseinrichtung (100), wobei jeder der Betriebsmodi für jeden einer Mehrzahl von Pfadknoten einen Satz auswählbarer Komponenten vorgibt, wobei jeder der mehreren Pfadknoten wenigstens einen Teil des Medienpfads (314, 316, 318) bildet,

1.3

determining a certification requirement associated with the software application (124, 322);

Bestimmen einer Zertifizierungsanforderung, die der Softwareanwendung (124, 322) zugeordnet ist,

1.4

selecting one of the plurality of potential operational modes for use in media-related operations involving the software application (124, 322), wherein the selected operational mode is compliant with the certification requirement;

Auswählen eines der möglichen Betriebsmodi zur Verwendung in medienbezogenen Vorgängen, die die Softwareanwendung (124, 332) einbeziehen, wobei der ausgewählte Betriebsmodus der Zertifizierungsanforderung entspricht,

1.5

selecting for each of the plurality of pathway nodes a selectable component in the respective set of selectable components in accordance with the selected operational mode to form at least a portion of a media pathway (314, 316, 318); and

Auswählen einer auswählbaren Komponente des jeweiligen Satzes auswählbarer Komponenten für jeden der Pfadknoten gemäß dem ausgewählten Betriebsmodus, um wenigstens einen Teil eines Medienpfades (314, 316, 318) zu bilden, und

1.6

performing media-related operations utilizing the media pathway (314, 316, 318).

Durchführen medienbezogener Vorgänge unter Nutzung des Medienpfades (314, 316, 318).

16 4. Die in Patentanspruch 7 geschützte Vorrichtung wird durch ihre Eignung für dieses Verfahren geprägt und unterliegt deshalb derselben Beurteilung.

17 5. Einige Merkmale bedürfen der näheren Erläuterung.

18 a) Eine Medienverarbeitungseinrichtung im Sinne von Merkmal 1 kann eine Set-Top-Box sein, aber auch ein anderes Gerät, das zur Verarbeitung von Medien geeignet ist.

19 Die Beschreibung führt als Beispiele unter anderem Videorecorder, DVD-Spieler und Smartphones an (Abs. 12).

20 b) Medienpfade im Sinne von Merkmal 1.1 bestehen gemäß Merkmal 1.2 aus Knoten, die wiederum aus Komponenten bestehen.

21 Als Komponenten in diesem Sinne kommen zum Beispiel Speicher, Prozessoren sowie Hardware- oder Software-Beschleuniger in Betracht (Abs. 15).

22 Patentanspruch 1 enthält insoweit keine konkreten Vorgaben.

23 c) Gemäß Merkmal 1.2 werden die für einen Pfadknoten jeweils in Betracht kommenden Komponenten dadurch bestimmt, dass die möglichen Betriebsmodi ermittelt werden und jeder Modus für jeden Pfadknoten einen Satz auswählbarer Komponenten vorgibt.

24 aa) Entgegen der Auffassung der Berufung reicht es dabei aus, wenn für jeden Betriebsmodus pro Pfad nur eine auswählbare Komponente vorgegeben wird.

25 (1) Der Wortlaut von Merkmal 1.2 ist insoweit nicht eindeutig.

26 Die Vorgabe, dass für jeden Knoten ein Satz (set) auswählbarer Komponenten vorgegeben ist, mag darauf hindeuten, dass jeweils mehrere Komponenten zur Verfügung stehen müssen. Aus mathematischer Sicht kann ein Satz oder eine Menge aber auch nur aus jeweils einem Element bestehen.

27 (2) Dafür, dass ein einziges Element pro Satz ausreicht, spricht die Darstellung in der nachfolgend wiedergegebenen Figur 2.

28 Bei dieser Ausführungsform werden an jedem Knoten (1, 2, 3, ...) Hardware- oder Software-Komponenten in Abhängigkeit vom angestrebten Betriebsmodus ausgewählt. Für jeden Betriebsmodus sind spezifische Grenzen für Sicherheits- und Zertifizierungsdienste und ein Schema für Schlüssel-, Authentifizierungs- und Sicherheitsmanagement zur Verwaltung von Ressourcen wie Hardwarebeschleunigung und Software-Anwenderprogrammschnittstellen (API) definiert (Abs. 17).

29 Jeder der im oberen Teil von Figur 2 dargestellten Medienpfade weist pro Knoten jeweils eine Komponente auf. Die jeweils auswählbaren Komponenten sind im unteren Teil dargestellt. Daraus ist erkennbar, dass für den ersten Betriebsmodus an jedem Knoten jeweils eine auswählbare Komponente zur Verfügung steht; für den zweiten Betriebsmodus stehen an jedem Knoten jeweils zwei Komponenten und beim letzten, als unsicher bezeichneten Betriebsmodus, fünf Komponenten für den ersten, eine Komponente für den zweiten und zwei Komponenten für den dritten Knoten zur Verfügung.

30 Daraus ist zu entnehmen, dass es ausreicht, wenn pro Knoten jeweils eine Komponente zur Verfügung steht. Eine weitergehende Auswahlmöglichkeit ist zwar nicht ausgeschlossen, aber nicht zwingend erforderlich.

31 Entgegen der Auffassung der Berufung lassen sich der Patentschrift demgegenüber keine ausreichenden Hinweise darauf entnehmen, dass zumindest für einen Betriebsmodus an jedem Knoten mindestens zwei Komponenten auswählbar sein müssen. Bei dem in Figur 2 dargestellten Ausführungsbeispiel ist diese Anforderung zwar für den zweiten Betriebsmodus erfüllt. Im Wortlaut von Merkmal 1.2 hat diese Anforderung aber keinen Niederschlag gefunden.

32 bb) Merkmal 1.2 enthält auch keine zwingenden Anforderungen bezüglich der Kriterien und der Art und Weise, anhand der die auswählbaren Komponenten vorgegeben werden.

33 Damit reicht es aus, wenn für jeden möglichen Betriebsmodus, der gemäß Merkmal 1.2 ermittelt worden ist, schon im Voraus die auswählbaren Komponenten festgelegt werden, mit der Ermittlung der möglichen Betriebsmodi also zugleich feststeht, aus welchen Komponenten ein dafür in Frage kommender Medienpfad besteht.

34 d) Die Auswahl eines der möglichen Betriebsmodi erfolgt gemäß Merkmal 1.4 anhand einer Zertifizierungsanforderung. Diese ist gemäß Merkmal 1.3 einer Softwareanwendung zugeordnet.

35 aa) Wie das Patentgericht zu Recht angenommen hat, ergibt sich daraus nicht, dass die jeweilige Softwareanwendung den ihr zugeordneten Zertifizierungsanforderungen entsprechen muss.

36 Patentanspruch 1 fordert lediglich, dass der Softwareanwendung eine Zertifizierungsanforderung zugeordnet ist, anhand derer die für die weitere Verarbeitung in Frage kommenden Betriebsmodi ausgewählt werden, nicht aber, dass die Softwareanwendung selbst diesen Anforderungen genügt.

37 bb) Merkmal 1.3 schließt andererseits nicht aus, dass die Softwareanwendung zusammen mit den für die Medienpfade einsetzbaren Komponenten ein Teilsystem bildet, das den jeweils maßgeblichen Zertifizierungsanforderungen entspricht.

38 Dabei kann zugunsten der Beklagten unterstellt werden, dass die Softwareanwendung im Sinne von Merkmal 1.3 nicht zugleich eine Komponente im Sinne von Merkmal 1.2 sein kann. Auch unter dieser Prämisse ist nicht ausgeschlossen, dass nicht nur der Medienpfad und dessen Komponenten Teil eines zertifizierten und besonders gesicherten Systems sind, sondern auch die Softwareanwendung, die diese Komponenten aufruft, um einen Medieninhalt wiederzugeben.

39 cc) Entgegen der Auffassung der Berufung kommt als Softwareanwendung im Sinne von Merkmal 1.3 auch Software in Betracht, die Funktionen zur digitalen Rechteverwaltung (DRM) umfasst.

40 Wie die Berufung im Ansatz zutreffend geltend macht, sind DRM-Elemente, die von einer oder mehreren Softwareapplikationen bereitgestellt werden, in Figur 3 des Streitpatents zwar als Beispiel für eine Komponente im Sinne von Merkmal 1.2 aufgeführt. Daraus ergibt sich aber nicht, dass die in Merkmal 1.3 vorgesehene Softwareapplikation solche Funktionen nicht aufweisen darf.

41 Wie bereits oben dargelegt wurde und durch Figur 3 bestätigt wird, können Komponenten im Sinne von Merkmal 1.2 auch aus Software bestehen. In Figur 3 wird in diesem Zusammenhang der auch in Merkmal 1.3 verwendete Begriff Softwareapplikation gebraucht.

42 Die in Merkmal 1.3 vorgesehene Softwareapplikation wird in Patentanspruch 1 nur dahin spezifiziert, dass ihr die Zertifizierungsanforderung zugeordnet ist, die für die Auswahl von Betriebsmodi maßgeblich ist.

43 Dem ist zu entnehmen, dass zur Verwirklichung von Merkmal 1.3 jede Software in Betracht kommt, die eine solche Zuordnung ermöglicht - unabhängig von den Funktionen, die sie ansonsten umfasst.

44 dd) Entgegen der Auffassung der Berufung ergibt sich aus Merkmal 1.3 nicht, dass die für die Auswahl der Betriebsmodi maßgeblichen Zertifizierungsanforderungen ausschließlich aufgrund der Softwareanwendung bestimmt werden dürfen, die Berücksichtigung weiterer Kriterien also unzulässig wäre.

45 Nach der Beschreibung kann eine Anwendung installiert werden, die Zertifikationsanforderungen vervollständigt, die mit einem Dienste- oder Inhaltsanbieter in Zusammenhang stehen. Zur Vervollständigung eines zertifizierten Pfades können zertifizierte Basispfade (wie von der Softwareanwendung spezifiziert) zusammen mit zusätzlichen (ebenfalls von der Softwareanwendung spezifizierten) Anforderungen verwendet werden (Abs. 18 und 26).

46 Bei einem Ausführungsbeispiel kann ein Anbieter verschiedene Versionen eines Medieninhalts zur Verfügung stellen, die sich etwa in ihrer Darstellungsqualität unterscheiden und deshalb unterschiedlichen Sicherheitsanforderungen unterliegen (Abs. 27). Die Sicherheitsanforderungen in Bezug auf einen einzelnen Medieninhalt können auch zeitlichen Änderungen unterliegen (Abs. 28).

47 Daraus ergibt sich, dass die Sicherheitsanforderungen und damit die Zertifizierungsanforderungen im Sinne von Merkmal 1.3 nicht allein von der eingesetzten Softwareanwendung, sondern auch von Eigenschaften des jeweils wiederzugebenden Inhalts abhängen können.

48 Für eine Zuordnung im Sinne von Merkmal 1.3 reicht es mithin aus, wenn sich die Zertifizierungsanforderungen aus dem Einsatz einer bestimmten Softwareanwendung und den Eigenschaften des jeweils wiederzugebenden Inhalts ergeben.

49 e) Auf der Grundlage des ausgewählten Betriebsmodus wird gemäß Merkmal 1.5 für jeden Pfadknoten eine auswählbare Komponente im Sinne von Merkmal 1.2 ausgewählt.

50 Da es aus den bereits dargelegten Gründen ausreicht, wenn für jeden Pfadknoten nur eine auswählbare Komponente zur Verfügung steht, kann sich diese Auswahl darauf beschränken, die für den jeweiligen Pfadknoten vorgesehene Komponente zu ermitteln und als Teil des Medienpfades einzusetzen.

51 f) Mit dem so definierten Medienpfad werden gemäß Merkmal 1.6 medienbezogene Vorgänge durchgeführt, also zum Beispiel ein Video oder ein Film empfangen und modifiziert, um ihn auf einem Empfangsgerät auszugeben (Abs. 36).

52 II. Das Patentgericht hat seine Entscheidung, soweit im Berufungsverfahren von Interesse, im Wesentlichen wie folgt begründet:

53 Der Gegenstand von Patentanspruch 1 in der erteilten Fassung ergebe sich für den Fachmann, einen Hochschul-Ingenieur der Fachrichtung Elektrotechnik oder Informationstechnik mit mehrjähriger Berufserfahrung und einschlägigen Kenntnissen auf dem Gebiet der Medienverarbeitung, in naheliegender Weise aus der Veröffentlichung von Texas Instruments (Android 4.0 on the OMAP™ 4 Platform, D2), deren Vorveröffentlichung durch die vorgelegten Unterlagen (NK8 bis NK11) bewiesen sei, und dem allgemeinen Fachwissen, das unter anderem durch die in D2 zitierte Veröffentlichung der GlobalPlatform Inc. (The Trusted Execution Environment: Delivering Enhanced Security at a Lower Cost to the Mobile Market, NK13) belegt sei.

54 Für die mit den Hilfsanträgen verteidigten Gegenstände gelte Entsprechendes.

55 III. Diese Beurteilung hält der Nachprüfung im Berufungsverfahren im Ergebnis stand.

56 1. Der Gegenstand von Patentanspruch 1 ist durch D2 und NK13 vorweggenommen.

57 a) D2 befasst sich mit der Nutzung des Betriebssystems Android 4.0 auf Multikern-Mobil-Prozessoren der Familie OMAP 4 des Herstellers Texas Instruments (TI).

58 aa) Um eine schnelle Markteinführung zu ermöglichen, habe TI bereits ein Board Support Package (BSP) für die OMAP-4-Plattform herausgegeben.

59 In die neue Sicherheits-Programmierschnittstelle (security API) von Android 4.0 sei die mobile Sicherheitstechnologie M-Shield von TI vollständig integriert. Auf OMAP-4-Prozessoren seien DRM-Inhalte (digital right management content) durch hardware-basierte Sicherheitsmaßnahmen während der Entschlüsselung, Decodierung und Bildaufbereitung (decryption, decoding and rendering) durchgehend von Ende zu Ende gesichert. Die OMAP-4-Prozessoren hätten eine Netflix-HD-Zertifizierung (mit der digitalen Rechteverwaltung Microsoft PlayReady) und seien konform mit den für das Streamen von HD-Inhalten erforderlichen höchsten Sicherheitsstufen der digitalen Rechteverwaltung Widevine (Summary S. 1).

60 bb) In Android 4.0 seien die Ebenen zum Zusammenstellen und Aufbereiten (composition and rendering) von Grafik und Video stark verändert worden. Eine Nutzung des Grafikprozessors (GPU) ermögliche eine kombinierte Ausgabe, erfordere aber ein hohes Maß an Leistung und Performance (White Paper S. 2).

61 Prozessoren vom Typ OMAP4460 ermöglichten insoweit eine starke Beschleunigung. Während der Zusammenstellung werde nunmehr eine neue Android-Komponente aufgerufen. Die Implementierung dieser Komponente auf der OMAP-Plattform weise die vier hierfür zur Verfügung stehenden Pipelines dynamisch zu. Dies ermögliche ein hohes Maß an Flexibilität (White Paper S. 3).

62 cc) M-Shield sei eine neue, für OMAP-Plattformen optimierte Sicherheitstechnologie, die Hardware, Software und Entwicklungswerkzeuge kombiniere, um die Verteilung (deployment) von Sicherheitslösungen auf Mobil- und Verbrauchergeräten zu erleichtern. Besondere Hardware-Mechanismen, sichere Startprozeduren (secure boot) und eine sichere Laufzeitumgebung (secure run-time) stellten sicher, dass nur vertrauenswürdiger Code auf sichere Ressourcen wie etwa besondere Speicherbereiche, Peripherieeinrichtungen und Hardwarebeschleuniger zugreifen könne (White Paper S. 10).

63 Wenn Android 4.0 auf OMAP-4-Prozessoren laufe, würden DRM-geschützte Videostreams geschützt, indem der gesamte Entschlüsselungs-, Decodierungs- und Bildaufbereitungsprozess vom Rest des Systems getrennt (firewalled) werde. Die Umgebung für eine vertrauenswürdige Ausführung (Trusted Execution Environment, TEE) sei eine separate sichere Laufzeitumgebung, die neben der Android-Plattform angeordnet sei (resides alongside the Android platform) und Sicherheitsdienste für das Android-Framework und Applikationen zur Verfügung stelle. Bevor geschützter Inhalt entschlüsselt werde, gehe die OMAP-4-Plattform in den sicheren M-Shield-Modus und führe den Widevine DRM-Agenten in der TEE aus. In diesem Modus erzwängen die Firewalls der Hardware strenge Grenzen für den Zugriff auf Speicher und Peripherieeinrichtungen, um sicherzustellen, dass DRM und Entschlüsselung vor internen und externen Ausspähversuchen geschützt seien (White Paper S. 11).

64 Diese Vorgänge sind in der nachfolgend wiedergegebenen Figur 6 schematisch dargestellt.

65 Obwohl die M-Shield-Technologie spezifisch für OMAP-Prozessoren sei, entspreche sie in Bezug auf Programmierschnittstellen (APIs) und Sicherheit Industriestandards wie OMTP TR1, GlobalPlatform TEE und FIPS 140-2. Dies sei wichtig, um Portabilität über Plattformgrenzen hinweg zu ermöglichen. Zu diesem Zweck stelle M-Shield Werkzeuge und Programmierschnittstellen zur Verfügung, die den Spezifikationen von GlobalPlatform entsprächen (White Paper S. 12).

66 Im Zusammenhang mit TEE wird NK13 zitiert (White Paper S. 13).

67 b) NK13 beschreibt das in D2 angesprochene Trusted Execution Environment (TEE).

68 TEE sei aufgrund von Sicherheitsbedenken im Markt für mobile Endgeräte entwickelt worden. Von Bedeutung sei dabei unter anderem die Möglichkeit, mit solchen Geräten HD-Video wiederzugeben und zu streamen, Fernsehsender zu empfangen und 3D-Spiele in Konsolenqualität zu spielen (S. 6).

69 TEE sei eine separate Ausführungsumgebung (execution environment) die neben (alongside) dem funktionsreichen Betriebssystem (Rich OS) laufe und diesem Sicherheitsdienste zur Verfügung stelle. Die TEE isoliere den Zugang zu ihren Hardware- und Software-Ressourcen vom Rich OS und dessen Applikationen (S. 10).

70 Diese Architektur ist in der nachfolgend wiedergegebenen Figur 1 schematisch dargestellt.

71 TEE ermöglicht damit die sichere Ausführung von zugelassener (authorized) Sicherheitssoftware, die auch als Trusted Applications bezeichnet wird. Um die ursprüngliche Sicherheit (root of trust) zu gewährleisten, wird die TEE authentifiziert und dann während des sicheren Bootprozesses vom Rest des Rich OS isoliert. Innerhalb der TEE ist jede vertrauenswürdige Applikation unabhängig von den anderen und kann nicht auf deren Sicherheitsressourcen zugreifen. Vertrauenswürdige Applikationen können von mehreren Anbietern (providers) stammen. Dies begründet die Erwartung, dass ein großes Ökosystem mit solchen Anbietern entsteht (S. 10).

72 c) Wie auch die Berufung nicht in Zweifel zieht, offenbart D2 damit die Merkmale 1 und 1.6.

73 d) Entgegen der Auffassung der Berufung offenbart D2 jedenfalls aufgrund der Bezugnahme auf NK13 auch die Merkmale 1.1 und 1.2.

74 aa) Aus der oben wiedergegebenen Figur 6 und den darauf bezogenen Ausführungen ergibt sich, dass für Inhalte, die Zertifizierungsanforderungen unterliegen, ein besonderer, aus mehreren Knoten bestehender Medienverarbeitungspfad zur Verfügung steht.

75 Für diesen Pfad ist zwar nur am letzten Knoten (Render) eine Auswahlmöglichkeit zwischen zwei Komponenten dargestellt, die eine Aufbereitung der Bilder für LCD- und HDMI-Monitore ermöglichen. Wie oben dargelegt wurde, reicht es für die Verwirklichung von Merkmal 1.2 aber aus, wenn für jeden Pfadknoten eine auswählbare Komponente zur Verfügung steht. Diese Anforderung ist bei dem in Figur 6 dargestellten Ausführungsbeispiel erfüllt.

76 bb) Dass daneben weitere Medienpfade zur Verfügung stehen, ergibt sich jedenfalls aus NK13.

77 (1) Aufgrund der ausdrücklichen Bezugnahme in D2 (S. 12 Abs. 1) gehören jedenfalls die in NK13 enthaltenen Ausführungen zu Werkzeugen und Programmierschnittstellen der TEE zum Offenbarungsgehalt von D2.

78 (2) Aus Figur 1 und den darauf bezogenen Ausführungen in NK13 ergibt sich, dass es neben dem in der gesicherten Umgebung (TEE) vorgesehenen Medienverarbeitungspfad die herkömmliche Android-Umgebung (Rich OS) gibt, in der grundsätzlich jede Android-Anwendung laufen kann.

79 Daraus geht hinreichend deutlich hervor, dass in dieser Umgebung auch Verarbeitungspfade für die Wiedergabe von nicht geschützten Videoinhalten eingerichtet werden können, wenn ein Betriebsmodus ausreicht, der keinen Zertifizierungsanforderungen unterliegt.

80 e) D2 offenbart auch die Merkmale 1.3 und 1.4.

81 aa) Die für den Einsatz der geschützten Umgebung (TEE) und damit für einen bestimmten Betriebsmodus maßgeblichen Zertifizierungsanforderungen sind jedenfalls der in D2 als Widevine DRM Agent bezeichneten Software zugeordnet.

82 Diese Software wird aufgerufen, bevor geschützte Inhalte entschlüsselt werden (D2 White Paper S. 11 oben). Ihr Einsatz deutet folglich darauf hin, dass besondere Zertifizierungsanforderungen zu beachten sind.

83 bb) Ob die Software einen Teil der geschützten Umgebung (TEE) bildet, wie dies im Text von D2 (White Paper S. 11 oben) ausgeführt wird, oder ob sie außerhalb dieser Umgebung steht, wie dies in Figur 6 dargestellt ist, bedarf keiner Entscheidung.

84 Wie oben dargelegt wurde, lässt Merkmal 1.3 beide Ausgestaltungen zu.

85 cc) Dass die Software DRM-Funktionen umfasst, ist unerheblich.

86 Wie bereits oben dargelegt wurde, genügt es zur Verwirklichung von Merkmal 1.3, dass die Software eine solche Zuordnung zu einer Zertifizierungsanforderung ermöglicht. Welche Funktionen sie daneben noch umfasst, ist in diesem Zusammenhang nicht von Bedeutung.

87 dd) Ob der Einsatz des besonderen Medienpfades zusätzlich auch von den Eigenschaften des jeweils wiederzugebenden Inhalts abhängt, ist ebenfalls unerheblich.

88 Wie oben dargelegt wurde, steht eine solche Ausgestaltung der Verwirklichung von Merkmal 1.3 nicht entgegen.

89 f) Merkmal 1.5 ist in D2 ebenfalls offenbart.

90 Wie oben dargelegt wurde, reicht es im Zusammenhang mit Merkmal 1.5 - ebenso wie im Zusammenhang mit Merkmal 1.2 - aus, wenn für jeden Pfadknoten eine auswählbare Komponente zur Verfügung steht.

91 Vor diesem Hintergrund ist Merkmal 1.5 schon dadurch verwirklicht, dass beim Aufruf der sicheren Umgebung (TEE) die in Figur 6 dargestellten Komponenten zum Einsatz gelangen - selbst wenn an jedem Knoten nur eine Komponente auswählbar wäre.

92 2. Ebenfalls zu Recht hat das Patentgericht die mit den Hilfsanträgen verteidigten Gegenstände als nicht patentfähig angesehen.

93 a) Der mit Hilfsantrag 1 verteidigte Gegenstand lag ausgehend von D2 nahe.

94 aa) Nach Hilfsantrag 1 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

wherein the media processing device (100) further has a certified application programming interface for use by the software application (124, 322) to determine security requirements, and to communicate the security requirements from the software application (124, 322) to a key management and certification support system.

95 bb) Wie die Berufungserwiderung zu Recht ausführt, ist eine solche Ausgestaltung jedenfalls durch die in Figur 1 von NK13 dargestellte Schnittstelle zwischen der Android-Umgebung (Rich OS) und der gesicherten Umgebung (TEE) offenbart.

96 Diese Schnittstelle ermöglicht vertrauenswürdigen Anwendungen den kontrollierten Zugriff auf Sicherheitsressourcen und -dienste (NK13 S. 10). Dies setzt voraus, dass mit ihrer Hilfe die erforderlichen Sicherheitsanforderungen bestimmt werden können.

97 b) Für Hilfsantrag 2 gilt Entsprechendes.

98 aa) Nach Hilfsantrag 2 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

wherein the set of selectable components comprises a plurality of hardware acceleration functions.

99 bb) Zu Recht ist das Patentgericht zu dem Ergebnis gelangt, dass dieses zusätzliche Merkmal in D2 offenbart ist.

100 Wie auch die Berufung im Ansatz nicht verkennt, offenbart D2 eine Vielzahl an Hardwarebeschleunigern.

101 Entgegen der Auffassung der Berufung offenbart D2 auch, dass diese Beschleuniger entsprechend den jeweiligen Sicherheitsanforderungen zugewiesen werden.

102 Dabei kann dahingestellt bleiben, ob sich dies schon aus der Darstellung in Figur 6 ergibt, die "Crypto Accelerators" für den gesicherten Modus vorsieht. Eine vom Modus abhängige Zuweisung ergibt sich jedenfalls aus den bereits oben wiedergegebenen Ausführungen, wonach spezifische Hardware-Mechanismen gewährleisten, dass nur vertrauenswürdiger Code auf sichere Ressourcen wie besondere Speicherbereiche, Peripherieeinrichtungen und Hardwarebeschleuniger zugreifen kann (S. 10 unten).

103 c) Der mit Hilfsantrag 3 verteidigte Gegenstand ist ebenfalls nicht patentfähig.

104 aa) Nach Hilfsantrag 3 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

performing media-related operations utilizing the selected operational mode; modifying the respective set of selectable components specified by the selected operational mode to form a new media pathway (314, 316, 318) compliant with the certification requirement; and continuing media-related operations utilizing the new media pathway (314, 316, 318).

105 bb) Wie das Patentgericht im Zusammenhang mit der erteilten Fassung von Patentanspruch 1 zu Recht angenommen hat, legt der Umstand, dass D2 für den dritten in Figur 6 dargestellten Verarbeitungsschritt (Render) zwei auswählbare Komponenten vorsieht, jedenfalls nahe, entsprechende Auswahlmöglichkeiten auch für die übrigen Verarbeitungsschritte vorzusehen.

106 Ergänzende Hinweise in diese Richtung ergeben sich aus dem Umstand, dass Figur 6 auch beim ersten Verarbeitungsschritt (Decrypt) mehrere Beschleuniger (Crypto Accelerators) vorsieht. Daraus mag sich nicht eindeutig ergeben, dass je nach Betriebsmodus einer dieser Beschleuniger ausgewählt wird. Das vom Patentgericht festgestellte Fachwissen, dass es während des Betriebs zum Beispiel aufgrund eines Wechsels der Bitrate zu Änderungen kommen kann und es vorteilhaft ist, hierfür unterschiedliche Komponenten vorzusehen, legte es jedenfalls nahe, von dieser Möglichkeit auch bei dem in D2 offenbarten System Gebrauch zu machen.

107 d) Für Hilfsantrag 4 gilt Entsprechendes.

108 aa) Nach Hilfsantrag 4 soll Patentanspruch 1 in der Fassung von Hilfsantrag 3 wie folgt ergänzt werden:

wherein the step of performing media-related operations is performed on a first version of a media item, and the step of continuing media-related operations performed on a second version of the media item.

109 bb) Eine solche Ausgestaltung ist aus den zu Hilfsantrag 3 dargelegten Gründen ausgehend von D2 ebenfalls nahegelegt.

110 e) Hilfsantrag 5 hat ebenfalls keinen Erfolg.

111 aa) Nach Hilfsantrag 5 soll die erteilte Fassung von Patentanspruch 1 in Merkmal 1.1 wie folgt geändert werden:

to establish media pathways in the media processing device (100) having at least one a software application (124, 322), which is a certified media streaming application, and a plurality of selectable components for use in supporting media pathways, the method comprising.

112 bb) Eine solche Ausgestaltung ist durch D2 jedenfalls nahegelegt.

113 Wie bereits oben aufgezeigt wurde, ist zumindest die in D2 als Widevine DRM Agent bezeichnete Software eine Softwareanwendung im Sinne von Merkmal 1.3. Diese bildet zwar nicht nach der Darstellung in Figur 6, wohl aber nach dem darauf bezogenen Text (D2 White Paper S. 11 oben) einen Teil der geschützten Umgebung (TEE).

114 Vor diesem Hintergrund lag es jedenfalls nahe, die Software in die geschützte Umgebung einzubeziehen und zu diesem Zweck zertifizieren zu lassen, wie dies NK13 in Tabelle 2 für Applikationen in dieser Umgebung vorsieht.

115 f) Der mit Hilfsantrag 6 verteidigte Gegenstand ist ebenfalls nicht patentfähig.

116 aa) Nach Hilfsantrag 6 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

adapting the media path (314, 316, 318) based upon pathway component availability.

117 bb) Zu Recht hat das Patentgericht entschieden, dass diese Ausgestaltung ausgehend von D2 schon deshalb nahelag, weil in Figur 6 unter anderem ein HDMI-Ausgang dargestellt ist, von dem nicht sicher ist, ob ein Ausgabegerät angeschlossen ist.

118 Entgegen der Auffassung der Berufung stellt auch dieser Ausgang einen Pfadknoten dar.

119 Ob es ausgehend von D2 nahelag, den Umstand, dass der HDMI-Ausgang nicht genutzt wird, zum Anlass für einen kompletten Pfadwechsel zu nehmen, kann offenbleiben. Auch ein solcher Wechsel ist eine Anpassung im Sinne von Hilfsantrag 6.

120 g) Der mit Hilfsantrag 7 verteidigte Gegenstand lag ebenfalls nahe.

121 aa) Nach Hilfsantrag 7 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

wherein a media source or content provider provides different versions of a media item differing in quality for selective or adaptive delivery via the software application based on the quality of service or security level of an available media pathway, and wherein the step of performing media-related operations utilizing the formed media pathway comprises delivery of a version of the media item in accordance with the quality of service or security level of the formed media pathway.

122 bb) Eine solche Ausgestaltung lag ausgehend von D2 schon deshalb nahe, weil sich daraus ergibt, dass besondere Zertifizierungsanforderungen bestehen können, wenn darzustellende Videoinhalte in HD-Qualität wiedergegeben werden sollen. Daraus ergab sich die Anregung, den Medienpfad anzupassen, wenn sich die Darstellungsqualität ändert.

123 h) Für Hilfsantrag 8 ergibt sich keine abweichende Beurteilung.

124 aa) Nach Hilfsantrag 8 soll die erteilte Fassung von Patentanspruch 1 in den Merkmalen 1.2, 1.3 und 1.5 wie folgt geändert werden:

1.2' identifying a plurality of potential operational modes of the media processing device (100) comprising at least two secure operational modes corresponding to different security levels as defined by the software application, each of the operational modes specifying for each of a plurality of pathway nodes a respective set of selectable components, each of the plurality of pathway nodes forming at least a portion of the media pathway (314, 316, 318);

1.3' determining a certification requirement associated with defined by the software application (124, 322);

1.5' selecting for each of the plurality of pathway nodes a selectable component in the respective set of selectable components in accordance with the selected operational mode to form at least a portion of a media pathway (314, 316, 318) that has the security level determined by the selected operational mode.

125 bb) Zu Recht hat das Patentgericht entschieden, dass diese Ausgestaltung ausgehend von D2 ebenfalls nahelag.

126 D2 befasst sich zwar nur mit einem Sicherheitsmodus. Wie das Patentgericht zu Recht ausgeführt hat, ergab sich aus dem Hinweis, dass Widevine drei unterschiedliche Sicherheitsniveaus vorsieht, die Anregung, für diese gegebenenfalls eigene Medienpfade zu definieren.

127 Dass D2 sich nur mit dem höchsten Sicherheitsniveau befasst, führt entgegen der Auffassung der Berufung nicht zu einem abweichenden Ergebnis. Wenn ein System in der Lage ist, die höchste von drei unterschiedlichen Sicherheitsanforderungen zu erfüllen, spricht alles dafür, es so auszugestalten, dass es auch geringeren Anforderungen gerecht wird, und hierfür jeweils eigene Betriebsmodi vorzusehen.

128 i) Für Hilfsantrag 9 ergibt sich keine abweichende Beurteilung.

129 Nach Hilfsantrag 9 soll die erteilte Fassung von Patentanspruch 1 um die zusätzlichen bzw. geänderten Merkmale nach den Hilfsanträgen 5 und 8 ergänzt werden.

130 Diese Merkmale lagen aus den oben aufgezeigten Gründen auch in ihrer Kombination nahe.

131 j) Der mit Hilfsantrag 10 verteidigte Gegenstand ist ebenfalls nicht patentfähig.

132 aa) Nach Hilfsantrag 10 soll die erteilte Fassung von Patentanspruch 1 wie folgt ergänzt werden:

wherein each operational mode corresponds to a particular certification service boundary definition and key and security management scheme for managing resources, and wherein security definitions provided by the software application (124, 322) are utilized in a key management and certification support system (102) of the media processing device (100) to establish a secure or certified media pathway (314, 316, 318).

133 bb) Zu Recht hat das Patentgericht entschieden, dass diese Ausgestaltung ausgehend von D2 ebenfalls nahelag.

134 Wie auch das Patentgericht nicht verkannt hat, ist eine derart fein granulierte Ausgestaltung der Medienpfade zwar in D2 nicht offenbart. Aus dem Hinweis, dass sich aus bestimmten Zertifizierungsanforderungen besondere Sicherheitsvorkehrungen ergeben können, und aus dem Hinweis, dass das in D2 offenbarte System die Anforderungen mehrerer Anbieter erfüllt, ergab sich aber die Anregung, die jeweiligen Medienpfade bei Bedarf an diese unterschiedlichen Anforderungen anzupassen.

135 k) Für Hilfsantrag 11 gilt nichts anderes.

136 aa) Nach Hilfsantrag 11 soll Patentanspruch 1 in der Fassung von Hilfsantrag 9 wie folgt ergänzt werden:

wherein the selection of the respective components within the device (100) is made to effectuate delivery of signals or media based upon the secure or unsecure nature of a component.

137 bb) Diese Ausgestaltung lag aus den zu den Hilfsanträgen 9 und 10 dargelegten Gründen ausgehend von D2 ebenfalls nahe.

138 IV. Die Kostenentscheidung ergibt sich aus § 121 Abs. 2 PatG und § 97 Abs. 1 ZPO.

Bacher

Deichfuß

Kober-Dehm

Rensen

von Pückler
