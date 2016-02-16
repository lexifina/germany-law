---
ecli: "ECLI:DE:BGH:2016:160216XZR5.14.0"
court: "Bundesgerichtshof"
spruchkoerper: "Zivilsenat-10"
aktenzeichen: "X ZR 5/14"
decided: "2016-02-16"
typ: "U"
bemerkung: "Anrufroutingverfahren\r\nLeitsatzentscheidung"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=2016&Sort=1&Seite=13&nr=75499&anz=3286&pos=411&Blank=1.pdf"
corpus_doc_id: "BGH_Zivilsenat-10_LE_2016-02-16_X_ZR_5_14_NA_Anrufroutingverfahren_0.txt"
cites_law: ["germany/bund/acts/patg/0121.md", "germany/bund/acts/zpo/0091.md"]
---

# Bundesgerichtshof, X ZR 5/14 vom 2016-02-16: Anrufroutingverfahren

## Entscheidung

BUNDESGERICHTSHOF
                   IM NAMEN DES VOLKES

                                URTEIL
X ZR 5/14                                                    Verkündet am:
                                                             16. Februar 2016
                                                             Anderer
                                                             Justizangestellte
                                                             als Urkundsbeamtin
                                                             der Geschäftsstelle
                       in der Patentnichtigkeitssache

Nachschlagewerk:      ja
BGHZ:               nein
BGHR:                 ja



                                                        Anrufroutingverfahren

EPÜ Art. 56

a) Für eine Veranlassung des Fachmanns, eine in einem Entwurf für einen
   technischen Standard beschriebene Routine in bestimmter, dem Ziel des
   Verfahrens dienlicher Weise weiterzuentwickeln, kann es sprechen, wenn im
   Entwurf enthaltene Verfahrensschritte ohnehin darauf angelegt sind, vom
   Fachmann konkretisiert zu werden, oder die Routine aus fachmännischer
   Sicht (möglicherweise) noch lückenhaft und im weiteren Standardisierungsprozess mit ergänzenden Angaben auszufüllen ist.

b) Kommen für den Fachmann zur Lösung eines Problems mehrere Alternativen in Betracht, können mehrere von ihnen naheliegend sein. Grundsätzlich
   ohne Bedeutung ist insofern, welche der Lösungsalternativen der Fachmann
   als erste in Betracht zöge.

BGH, Urteil vom 16. Februar 2016 - X ZR 5/14 - Bundespatentgericht




ECLI:DE:BGH:2016:160216UXZR5.14.0

                                     -2-




Der X. Zivilsenat des Bundesgerichtshofs hat auf die mündliche Verhandlung
vom 16. Februar 2016 durch den Vorsitzenden Richter Prof. Dr. Meier-Beck, die
Richter Dr. Grabinski und Hoffmann sowie die Richterin Schuster und den Richter Dr. Deichfuß


für Recht erkannt:



          Auf die Berufung der Klägerin wird das am 18. September 2013
          verkündete Urteil des 5. Senats (Nichtigkeitssenats) des Bundespatentgerichts abgeändert.

          Das europäische Patent 1 931 094 wird mit Wirkung für die
          Bundesrepublik Deutschland insgesamt für nichtig erklärt.

          Die Kosten des Rechtsstreits hat die Beklagte zu tragen.



                             Von Rechts wegen

                                          -3-




                                      Tatbestand:


1         Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik
    Deutschland erteilten europäischen Patents 1 931 094 (Streitpatents), das am
    30. August 2006 angemeldet wurde und eine Priorität vom 31. August 2005 in
    Anspruch nimmt. Es umfasst in der erteilten Fassung 15 Patentansprüche, von
    denen Patentanspruch 1 in der Verfahrenssprache wie folgt lautet:

          "A Circuit Switched, CS, domain call terminating method of call
          routing characterized in that the method is a method of avoiding
          repeated routing control in a CS domain call terminating flow,
          comprising:
                 receiving, by a GMSC, routing-controlled information of a
                 call carried in a received call initiation message;
                 sending, by the GMSC, the routing-controlled information of
                 the call to a gsmSCF; and
                 executing, a subsequent call flow of the call in accordance
                 with the received routing-controlled information, wherein the
                 executing comprises:
                      determining, by the gsmSCF, that the call has been
                      subject to routing control in accordance with the routing-controlled information;
                      sending, by the gsmSCF, a Continue message to the
                      GMSC; and
                      sending, by the GMSC, to an HLR an SRI message
                      carrying a suppress T-CSI parameter upon receipt of
                      the Continue message to obtain an MSRN through
                      standard call terminating procedures."


2         Die Klägerin hat geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus und sei
    nicht patentfähig. Hinsichtlich der Patentansprüche 14 und 15 hat die Klägerin
    ferner mangelnde Ausführbarkeit geltend gemacht.

                                          -4-




3         Die Beklagte hat das Streitpatent in einer Fassung verteidigt, die Patentanspruch 12 nicht enthält.

4         Das Patentgericht hat das Streitpatent dadurch teilweise für nichtig erklärt, dass Patentanspruch 12 entfällt, und im Übrigen die Klage abgewiesen.
    Hiergegen richtet sich die Berufung der Klägerin, mit der sie den Antrag auf
    vollständige Nichtigerklärung des Streitpatents weiterverfolgt. Die Beklagte tritt
    dem Rechtsmittel entgegen.




                                 Entscheidungsgründe:


5         Die zulässige Berufung hat Erfolg.

6         I.   Das Streitpatent betrifft ein Verfahren zur Herstellung eines Telefonanrufs unter Beteiligung des Mobilfunknetzes.

7         1. Das Streitpatent referiert ein Projekt des 3rd Generation Partnership
    Project (3GPP), einer Kooperation von Standardisierungsgremien für den Mobilfunk, das sich in dem Technical Report 23.806 V1.3.0 (VP2) mit einer Echtzeit-Sprachanrufskontinuität ("Voice Call Continuity" - VCC) für Mobilfunkgeräte befasst, die Anrufe nicht nur in dem leitungsvermittelten ("Circuit Switched" - CS)
    Mobilfunknetz (CS-Domäne), sondern auch z.B. mittels einer WLAN-Anbindung
    an das Internet (IP-Multimedia Subsystem - IMS) nach dem VoIP-Standard vornehmen können. Das Standardisierungsprojekt behandelt hierbei verschiedene
    Szenarien, die unter anderem das Anrufen eines solchen Mobilfunkgeräts und
    das Annehmen solcher Anrufe betreffen, je nachdem, ob das Gerät gerade über
    das Mobilfunknetz (CS-Domäne) oder über das Internet (IMS-Domäne) angebunden ist, wobei das Mobilfunkgerät jeweils unter derselben (Mobilfunk-)
    Rufnummer in beiden Netzen erreichbar sein und anrufen können soll.

                                         -5-




8         Für eines der Szenarien, bei dem ein sich in der CS-Domäne befindendes Mobilfunkgerät ("Other End") ein anderes, sich ebenfalls in einer CS-Domäne befindendes Mobilfunkgerät ("User Equipment" - UE) unter dessen
    Mobilfunkrufnummer anrufen möchte, die sowohl für die CS-Domäne als auch
    für IMS-Domäne als möglicher Verbindungsweg registriert ist, beschreibt VP2 in
    Figur 6.2a.3.2-5 folgenden Verfahrensablauf zur Herstellung des Anrufs, wenn
    dabei der Anruf an die CS-Domäne gerichtet ist:




          Bei diesem Ablauf sendet die Vermittlungsstelle im CS-Mobilfunknetz
9
    ("Gateway Mobile Switch Center" - GMSC, im Folgenden auch nur: Vermittlungsstelle) am Ende von Schritt 2 eine als Initial Detection Point (IDP) bezeichnete Nachricht an die im Streitpatent als Global System for Mobile Communications-Service Control Function (gsmSCF) und in VP2 als Call Continuity
    Control Function (CCCF)/Network Domain Selection (NeDS) bezeichnete Steuerungseinrichtung. Hierbei handelt es sich um eine kombinierte Funktionsein-

                                          -6-




     heit, die gemäß VP2 den Netzwerkstrukturen der CS- und der IMS-Domäne
     hinzugefügt werden soll (VP2 Abschnitt 6.2 bis 6.2.2) und die sowohl die für
     einen Anruf vorzunehmende Netzwerkauswahl (NeDS) als auch die Einhaltung
     der Anforderungen an die Kontinuität eines Anrufs und die Erreichbarkeit bei
     einem Wechsel zwischen diesen beiden Netzwerken (CCCF) sicherstellen soll.
     Teile der Funktionalität der Steuerungseinrichtung CCCF/NeDS (im Folgenden
     auch nur: Steuerungseinrichtung) werden im Streitpatent auch als Domain
     Selection Function (DSF) bezeichnet (Streitpatent Sp. 2 Abs. 8).

           In der am Ende des zweiten Schritts vorgesehenen IDP-Nachricht von
10
     der Vermittlungsstelle an die Steuerungseinrichtung wird zur Bezeichnung des
     angerufenen Teilnehmers dessen im ersten Schritt mit der Initial Address Message (IAM) übermittelte, weltweit eindeutige Mobilfunkrufnummer (MSISDN)
     verwendet. Die darauf folgenden Schritte dienen unter anderem der Feststellung der Route, auf der der angerufene Teilnehmer erreicht werden kann, und
     der damit verbundenen Routinginformationen, die mit den in Schritten 8 und 9
     übersandten INVITE- und IAM-Nachrichten von der Steuerungseinrichtung an
     die Vermittlungsstelle in Form einer CS-Domain Routing Number (CSRN) übertragen werden. Mit Schritt 10 wird eine Sending-Routing-Information-(SRI-)
     Nachricht an das als Datenbank für den angerufenen Mobilfunkteilnehmeranschluss fungierende Home Location Register (HLR) übermittelt, wobei hierfür
     dessen MSISDN verwendet wird. In Schritt 11 folgt sodann erneut eine IDP-Nachricht von der Vermittlungsstelle an die Steuerungseinrichtung, die nach
     dem in der VP2 vorgesehenen Ablaufplan zum Szenario gemäß Figur 6.2a.3.2-5 mit einer CONTINUE-Nachricht beantwortet werden soll.

                                          -7-




           Das Streitpatent geht davon aus, dass bei der erneuten Sendung einer
11
     IDP-Nachricht in Schritt 11 die MSISDN des angerufenen Mobilfunkgeräts und
     nicht die für ein Routing zu diesem Gerät erforderliche CSRN an die Steuerungseinrichtung übermittelt wird, bei der der Anruf verankert ist. Damit könne
     die Steuerungseinrichtung nicht feststellen, ob der Anruf bereits einer Routingsteuerung entsprechend den vorangegangenen Schritten 2 bis 9 unterzogen
     wurde, ob es sich mit anderen Worten bei der IDP-Nachricht um eine solche
     gemäß Schritt 2 handelt. Dies könne zu einer wiederholten Routingsteuerung
     gemäß den Schritten 2 bis 8 anstelle einer CONTINUE-Nachricht gemäß
     Schritt 12 führen, so dass der Anruf in der CS-Domäne nicht normal vermittelt
     werden könne (Streitpatent Sp. 8 Abs. 42 Z. 37 bis 51).

12         Demnach liegt dem Streitpatent die Aufgabe zugrunde, wiederholte Routingsteuerungsschritte zu vermeiden, um so den Ablauf zur Herstellung eines
     Anrufs zu einem sowohl in der CS-Domäne als auch in der IMS-Domäne verwendbaren Mobilfunkgerät zu verbessern.

13         2. Zur Lösung schlägt das Streitpatent ein Verfahren zur Herstellung eines Anrufs mit folgenden Merkmalen vor [in eckigen Klammern die Merkmalsgliederung des angefochtenen Urteils]:

           1. Das Verfahren dient dem Anrufabschluss mittels eines Anrufroutings in einer leitungsvermittelten CS-Domäne (circuit
              switched [CS] domain call terminating method of call routing)
              [1.1],
               1.1 wobei eine wiederholte Routingsteuerung in einem CS-Domänen-Anrufabschlussfluss vermieden wird (a
                   method of avoiding repeated routing control in a CS domain call terminating flow) [1.2].
           2. Das Verfahren umfasst folgende Schritte [1.2]:
               2.1 Eine Vermittlungsstelle GMSC empfängt in einer Anrufeinleitungsnachricht ("call initiation message") Informationen zur Routingsteuerung eines Anrufs (receiving, by a

                                         -8-




                    GMSC, routing-controlled information of a call carried in
                    a received call initiation message) [1.3].
               2.2 Die Vermittlungsstelle GMSC sendet eine die Routingsteuerung des Anrufs enthaltende Information an eine
                   Steuerungseinrichtung gsmSCF (sending, by the GMSC,
                   the routing-controlled information of the call to a
                   gsmSCF) [1.4].
           3. Der nachfolgende Anruffluss erfolgt gemäß der empfangenen
              Information zur Routingsteuerung (executing a subsequent
              call flow of the call in accordance with the received routingcontrolled information) [1.5]:
               3.1 Die Steuerungseinrichtung gsmSCF stellt anhand der
                   empfangenen Information zur Routingsteuerung fest,
                   dass der Anruf einer Routingsteuerung unterlag (determining, by the gsmSCF, that the call has been subject to
                   routing control in accordance with the routing-controlled
                   information) [1.5.1].
               3.2 Die Steuerungseinrichtung gsmSCF sendet eine CON-TINUE-Nachricht an die Vermittlungsstelle GMSC
                   (sending, by the gsmSCF, a Continue message to the
                   GMSC) [1.5.2].
               3.3 Die Vermittlungsstelle GMSC sendet eine SRI-Nachricht
                   an ein Lokalisierungsregister HLR mit einem Terminating-CAMEL-Subscription-Information-(T-CSI-) Unterdrückungsparameter, um nach dem Empfang der CONTI-NUE-Nachricht eine Roaming-Nummer (Mobile Station
                   Roaming Number - MSRN) aufgrund von Standard-Anrufabschlussverfahren zu erhalten (sending, by the
                   GMSC, to an HLR an SRI message carrying a suppress
                   T-CSI parameter upon receipt of the Continue message
                   to obtain an MSRN through standard call terminating
                   procedures) [1.5.3].


14         3. Einige Merkmale bedürfen näherer Erläuterung:

15         a) Mit "Anrufabschluss" ist das Herstellen einer Sprachverbindung mit
     einem Mobilfunkgerät aufgrund eines an die zugehörige Mobilfunkrufnummer
     gerichteten Anrufs gemeint.

                                           -9-




16           b) Das Anrufrouting gemäß Merkmal 1 bestimmt, über welche Stationen
     im Kommunikationsnetz die Verbindung mit dem Mobilfunkgerät hergestellt
     wird.

17           c) Eine wiederholte Routingsteuerung wird gemäß Merkmal 1.1 dann
     vermieden, wenn Schritte zur Routingsteuerung bei der Herstellung eines Anrufs zu einem Mobilfunkgerät nicht unnötig mehrfach vorgenommen werden.

18           d) Informationen zur Routingsteuerung gemäß Merkmal 2.1 sind Informationen, die der Herstellung einer Verbindungsroute zum angerufenen Mobilgerät dienen und nicht dessen MSISDN darstellen, sondern die mögliche Route
     weiter konkretisieren. Die Beschreibung des Streitpatents bringt zum Ausdruck,
     dass das Senden lediglich der MSISDN in dem dem Merkmal 2.2 entsprechenden Verfahrensschritt gerade der Grund ist, warum eine wiederholte Routingsteuerung entstehen kann, und dass dies mit dem Senden einer von der
     MSISDN abweichenden Information zur Routingsteuerung vermieden wird
     (Streitpatent Sp. 8 Abs. 42 Z. 29 bis Sp. 9 Abs. 43 Z. 5). Für die Schritte gemäß
     den Merkmalen 2.2 bis 3.1 reicht es hinsichtlich der die Routingsteuerung enthaltenden Information und der Information zur Routingsteuerung aus, eine Information beispielsweise in Form eines einzelnen Bits zu senden, dergemäß
     zuvor eine über die MSISDN hinausgehende Routingsteuerung stattfand
     (Streitpatent Sp. 10 Abs. 52 Z. 38 bis 41). Der die Routingsteuerung konkretisierende Inhalt muss in den gemäß den Merkmalen 2.2 bis 3.1 übersandten
     beziehungsweise ausgewerteten Informationen nicht enthalten sein.

19           e) Mit einer SRI-Nachricht gemäß Merkmal 3.3 fragt die Vermittlungsstelle GMSC das Register HLR nach weiteren Routinginformationen. Um nicht
     (nur) die Nachricht zu erhalten, dass das angerufene Mobilgerät mit der gewählten Rufnummer sowohl in der CS-Domäne als auch in der IMS-Domäne erreichbar ist, wird ein T-CSI-Parameter im Schritt gemäß Merkmal 3.3 gesendet.
     Dies veranlasst das Register, eine Roaming-Nummer MSRN zu senden, an-

                                            - 10 -




     hand deren die Vermittlungsstelle und andere Funktionseinheiten des Mobilfunknetzes eine Verbindung zu dem angerufenen Mobilfunkgerät (UE) nach
     standardisierten Prozeduren herstellen.

20         II. Das Patentgericht hat den - für ursprungsoffenbart und ausführbar
     erachteten - Gegenstand des Streitpatents als patentfähig angesehen und dies
     im Wesentlichen wie folgt begründet:

           Das Szenario zu Figur 6.2a.3.2-5 der VP2 zeige ein Anrufabschlussverfahren mit den Merkmalen 1, 2, 2.1, 3.2 und 3.3. Selbst wenn Merkmal 1.1 bei
     der Prüfung der Patentfähigkeit nicht berücksichtigt würde, weil es kein unmittelbares Merkmal des geschützten Verfahrens, sondern nur ein zu erreichendes
     Ziel darstelle, zeige die VP2 nicht die Verfahrensschritte 2.2, 3 und 3.1 und sei
     daher nicht neuheitsschädlich. Ihr könne nicht unmittelbar und eindeutig entnommen werden, dass an die Steuerungseinrichtung eine die Routingsteuerung
     enthaltende Information gesendet werde, diese feststelle, dass der Anruf einer
     Routingsteuerung unterlegen habe, und der weitere Anrufabfluss gemäß dieser
     Information durchgeführt werde.

           Das Senden einer CONTINUE-Nachricht gemäß Schritt 12 der Figur 6.2a.3.2-5 in VP2 gebe dem Fachmann nicht unmittelbar und eindeutig zu
     erkennen, dass die Steuerungseinrichtung mit der IDP-Nachricht im Schritt 11
     zuvor eine die Routingsteuerung enthaltende Information erhalte habe und diese auswerte, denn die VP2 spreche an keiner Stelle das Problem des wiederholten Routens an. Die Annahme der Klägerin, dass die Vermittlungsstelle
     GMSC zuvor in einer IAM-Nachricht als "Called Party Number" die CSRN erhalten habe und deshalb diese Information in der sodann folgenden IDP-Nachricht
     verwendet werde, überzeuge nicht, denn zuvor werde aus der CSRN wieder die
     MSISDN ermittelt, weshalb der Fachmann diese Nummer als "Called Party
     Number" verwenden werde. Es sei daher keineswegs selbstverständlich, in der
     VP2 die CSNR in der IDP-Nachricht zu verwenden, und Gleiches gelte für die

                                            - 11 -




     Druckschrift 3GPP TSG SA WG2 Architecture - VCC Ad hoc, 9. bis 11. August
     2005 (VP1), die im Wesentlichen den gleichen Sachverhalt betreffe.

23          Der Gegenstand des Streitpatents beruhe auch auf erfinderischer Tätigkeit. Ausgehend von der VP2, der unterschiedliche Ausführungsbeispiele für
     das Verankern eines Anrufs in der CS-Domäne zu entnehmen seien, stelle sich
     dem Fachmann nicht das Problem, ein CS-Domänenverbindungsabschlussverfahren zu entwickeln, bei dem eine wiederholte Routingsteuerung verhindert
     werde, denn die VP2 bringe dieses Problem an keiner Stelle zum Ausdruck.
     Der Fachmann habe deshalb keine Veranlassung gehabt, von dem im Stand
     der Technik bekannten Vorgehen für den Rufaufbau in einer CS-Domäne abzuweichen. Soweit andere Druckschriften des Projekts 3GPP wie die technischen Spezifikationen 3GPP TS 23.078 V6.6.0 (VP3) und 3GPP TS 29.078
     7.0.0 (VP4) Ausführungen zur Erstellung einer IDP-Nachricht enthielten, werde
     darin eine "Called Party Number" übertragen, bei der es sich um die MSISDN
     des angerufenen Mobilgeräts handele. Der Fachmann werde deshalb für einen
     Ablauf gemäß Figur 6.2a.3.2-5 der VP2 ebenfalls auf die MSISDN für eine Initial-DP-Nachricht gemäß Schritt 11 dieses Szenarios zurückgreifen, da diese
     Nummer für den Schritt zuvor aus der IAM-Nachricht und darin übermittelten
     CSRN ermittelt werde. Selbst wenn der Fachmann erkennen würde, dass es
     bei einer Verwendung der MSISDN in diesem Schritt zu einem wiederholten
     Routing komme, könnte er der VP2 keinen Hinweis und keine Anregung dafür
     entnehmen, statt der MSISDN die CSRN zu übersenden.

24          III. Dies hält der Nachprüfung im Berufungsverfahren nicht stand.

25          1. Der Gegenstand des Patentanspruchs 1 ist nicht patentfähig. Es
     kann offen bleiben, ob das darin beschriebene Verfahren im Stand der Technik
     bereits neuheitsschädlich offenbart war. Jedenfalls beruht dieses Verfahren
     nicht auf einer erfinderischen Tätigkeit.

                                          - 12 -




26         a) Das Patentgericht hat den Fachmann rechtsfehlerfrei und unangefochten als einen Diplomingenieur der Fachrichtung Nachrichtentechnik mit
     Schwerpunkt auf dem Gebiet der Signalverarbeitung in Mobilfunksystemen und
     mehrjähriger Berufserfahrung in Bezug auf Anrufroutingverfahren definiert.

27         b) Entsprechend den weiteren Ausführungen des Patentgerichts war
     diesem Fachmann ausgehend von der VP2 mit deren am 19. August 2005 veröffentlichte Entwurfsversion V1.3.0 insbesondere hinsichtlich des darin anhand
     Figur 6.2a.3.2-5 beschriebenen Szenarios ein Verfahren mit den Merkmalen 1,
     2, 2.1, 3.2 und 3.3 in dem für ihn relevanten Stand der Technik offenbart. Die
     Beklagte tritt dem auch nicht entgegen.

28         c) Die VP2 erwähnt nicht ausdrücklich, ob und gegebenenfalls wie sich
     die IDP-Nachricht gemäß Schritt 11 der Figur 6.2a.3.2-5 von der in Schritt 2
     beschriebenen IDP-Nachricht unterscheidet und aufgrund welcher Programmvorgaben die Steuerungseinrichtung CCCF nach Schritt 11 nicht die gleiche
     Antwort gibt wie nach der IDP-Nachricht in Schritt 2, sondern in Schritt 12 eine
     CONTINUE-Nachricht sendet.

29         d) Sollte, wie das Patentgericht angenommen hat, der Fachmann dem
     Gesamtablauf nach der Figur 6.2a.3.2-5 nicht bereits entnommen haben, dass
     die IDP-Nachricht gemäß Schritt 11 sich von derjenigen in Schritt 2 inhaltlich
     unterscheiden muss, damit die Steuerungseinrichtung in Schritt 12 aufbauend
     auf einem dafür getroffenen Entscheidungsprozess eine andere Antwort (CON-TINUE-Nachricht) gibt als in Schritt 3 (CONNECT-Nachricht), und dass hierfür
     die mit der im Schritt 9 übersandte CSRN als Unterscheidungsmerkmal oder ein
     anderes klares Unterscheidungsmerkmal zu verwenden war, musste sich der
     Fachmann jedenfalls Gedanken darüber machen, wie er den mit der VP2 offenbarten Standardisierungsentwurf zweckmäßig umsetzen und gegebenenfalls
     weiterentwickeln konnte. Dies gab ihm jedenfalls Veranlassung, mit der IDP-Nachricht nach Schritt 11 nicht die MSISDN, sondern die CSRN zu übertragen.

                                         - 13 -




30         aa) Zunächst ist zu berücksichtigen, welche Qualität der als VP2 veröffentlichte Entwurf besaß. Der Inhalt dieses Entwurfs war entsprechend seinem
     Vorwort (VP2 S. 7) Gegenstand weitergehender Arbeit und Überlegungen und
     noch nicht abschließend durch dafür vorgesehene Gremien bestätigt. Für den
     Fachmann bedeutete dies, dass der Entwurf noch Lücken enthalten konnte, die
     der Ausfüllung bedurften. Weiterhin sollte der entworfene Standard dem Fachmann nicht jeden Befehl für zu entwerfende Programme vorgeben, die in den
     jeweiligen Funktionseinheiten für ein dem Standard gemäßes Verfahren erforderlich sind. Die in VP2 entworfenen Szenarien waren mithin darauf angelegt,
     hinsichtlich ihrer technischen Umsetzung durch den Fachmann weiter konkretisiert zu werden.

31         bb) Im Hinblick auf diese Konstellation war vom Fachmann die Erkenntnis zu erwarten, dass sich in dem Szenario der VP2 zu Figur 6.2a.3.2-5 der Ablauf nach der IDP-Nachricht in Schritt 2 von dem Ablauf nach der IDP-Nachricht
     gemäß Schritt 11 unterscheiden sollte. Nach Schritt 2 soll eine Anfrage der
     Steuerungseinrichtung bei dem Register HLR erfolgen. Für Schritt 11 gibt die
     VP2 hingegen an, dass mit dieser IDP-Nachricht die Ausführung der zweckdienlichen logischen Schritte für den Anruf (VP2, 6.2a.3.2.3.2.2.3 Nr. 11: "for
     execution of appropriate service logic for the incoming session") und in
     Schritt 12 eine CONTINUE-Nachricht folgen soll. Dem Fachmann musste damit
     klar sein, dass die Steuerungseinrichtung eine Unterscheidung zwischen den
     beiden Schritten treffen muss und es hierfür einer Entscheidungsgrundlage bedarf. Der Fachmann hatte deshalb Veranlassung, Überlegungen anzustellen,
     wie eine solche Entscheidungsgrundlage für die Steuerungseinrichtung nach
     Empfang der IDP-Nachrichten in den Schritten 2 und 11 jeweils hergestellt werden konnte.

           Aus dem Szenario zu Figur 6.2a.3.2-5 wusste der Fachmann, dass sich
32
     die beiden von der Vermittlungsstelle an die Steuerungseinrichtung gesandten

                                          - 14 -




     IDP-Nachrichten in den Schritten 2 und 11 darin unterschieden, dass der Vermittlungsstelle bei Schritt 2 für das Anrufrouting nur die Rufnummer des angerufenen Mobilfunkgeräts (die mit Schritt 1 per IAM-Nachricht übermittelte
     MSISDN) bekannt war und die darauf folgenden Schritte dazu führen sollten,
     aufgrund der mit Schritt 2 erfolgenden IDP-Nachricht weitere Informationen zur
     Konkretisierung der Anrufroute zu erhalten. Diese weitere Routinginformation
     soll die Vermittlungsstelle GMSC mit der IAM-Nachricht gemäß Schritt 9 in
     Form der CSRN erhalten.

           Für die Vermittlungsstelle unterscheidet sich die Situation vor Schritt 2
33
     einerseits und Schritt 11 andererseits mithin dadurch, dass sie vor Schritt 2 in
     einer IAM-Nachricht eine MSISDN und vor Schritt 11 in einer IAM-Nachricht
     eine CSRN empfängt. Diese Information stellt für die Vermittlungsstelle GMSC
     das Kriterium dar, um zwischen Schritt 2 und Schritt 11 unterscheiden zu können. Mit Blick auf die Notwendigkeit, es auch der Steuerungseinrichtung CCCF
     zu ermöglichen, die Situationen nach den Schritten 2 und 11 zu unterscheiden,
     bot es sich deshalb an, eben diesen Unterschied in der Datenlage auch der
     Steuerungseinrichtung zu übermitteln.

           Hierfür sprach auch die Offenbarung in der Technischen Spezifikation
34
     3GPP TS 29.078 7.0.0 (VP4) zum CAMEL-Protokoll, die in Annex A unter A.1
     beschreibt, wie die Daten für eine IDP-Nachricht aus einer vorangegangenen
     IAM-Nachricht zusammengestellt ("mapping") werden. Als erstes Datum wird
     dabei die Nummer des angerufenen Mobilgeräts aus der IAM-Nachricht in die
     IDP-Nachricht übertragen. Üblicherweise handelt es sich zwar wie in den Schritten 1 und 2 der Figur 6.2a.3.2-5 um die MSISDN des angerufenen Mobilgeräts.
     Wenn jedoch mit der vorangegangenen IAM-Nachricht eine CSRN als Rufnummer des angerufenen Mobilgeräts übermittelt wird, hat der Fachmann sich
     zumindest die Frage zu stellen, ob er für die folgende IDP-Nachricht die CSRN
     oder eine aus dieser ermittelten MSISDN überträgt. Im Hinblick auf die Veran-

                                           - 15 -




     lassung des Fachmanns, für die Steuerungseinrichtung CCCF ein Kriterium zur
     Unterscheidung der beiden IDP-Nachrichten der Schritte 2 und 11 zu finden,
     war danach von ihm zu erwarten, für die IDP-Nachricht nicht eine aus der
     CSRN ermittelte MSISDN, sondern die CSRN selbst als Rufnummer des angerufenen Mobilfunkgeräts zu verwenden.

35           cc) Dem steht nicht entgegen, dass die VP2 zu Figur 6.2a.3.2-5 unter
     Nr. 10 für die Vermittlungsstelle GMSC die Anweisung enthält, vor Schritt 10 für
     die an das Register HLR zu übermittelnde SRI-Nachricht die MSISDN aus der
     CSRN tatsächlich zu ermitteln. Die Klägerin hat dies unwidersprochen damit
     erklärt, dass das Register nur die MSISDN, nicht aber die CSRN verarbeiten
     kann.

36           dd) Weiterhin steht dem nicht entgegen, dass ein wiederholtes Durchlaufen der Routingsteuerung in den Schritten 2 bis 10 auch durch andere Maßnahmen hätte vermieden werden können. Der Patentfähigkeit ermangelt nicht
     nur die nächstliegende Lösung für ein technisches Problem, sondern jede für
     den Fachmann naheliegende Lösung. Kommen für den Fachmann mehrere
     Alternativen in Betracht, können folglich mehrere von ihnen naheliegend sein.
     Grundsätzlich ohne Bedeutung ist insofern auch, welche der Lösungsalternativen der Fachmann als erste in Betracht zöge (vgl. BGH, Urteil vom 6. März
     2012 - X ZR 50/09, juris Rn. 19).

37           Die Beklagte trägt vor, ein wiederholtes Durchlaufen der Schritte 2 bis 10
     hätte ebenso vermieden werden können, indem die Steuerungseinrichtung
     CCCF bei Schritt 8 speichert, dass sie eine bestimmte CSRN für eine konkrete
     Kombination aus angerufener Rufnummer und anrufender Rufnummer für die in
     diesem Schritt folgende INVITE-Nachricht vergeben hat, diese Speicherung für
     einen eng begrenzten Zeitraum aufrecht erhält, sodann nach der IDP-Nachricht
     in Schritt 11 anhand der dabei übermittelten MSISDN die bereits vollzogene

                                         - 16 -




     Übermittlung einer CSRN erkennt und deshalb in Schritt 12 die Entscheidung
     für die Übersendung einer CONTINUE-Nachricht trifft.

38          Es kann offen bleiben, ob eine solche Lösung überhaupt nahegelegt war.
     Jedenfalls kam sie für den Fachmann nicht allein und nicht einmal bevorzugt in
     Betracht. Vielmehr weist diese Lösung Nachteile auf. Das Speichern der
     Vergabe einer CSRN in Schritt 8 nebst Löschen dieser Speicherung und Vergleich dieses Datums mit den in Schritt 11 in der IDP-Nachricht übersandten
     Daten, nur um festzustellen, dass die in Schritt 11 übermittelte IDP-Nachricht
     auf einer vorangegangenen Routingsteuerung beruht, stellt - wie von der Klägerin unwidersprochen dargelegt - einen erheblich größeren Datenverarbeitungsaufwand dar, als schlicht mit der IDP-Nachricht die Information zu verbinden,
     dass bereits eine Routingsteuerung stattgefunden hat und deshalb von der
     Steuerungseinrichtung CCCF in Schritt 12 eine CONTINUE-Nachricht zu senden ist.

39          ee) Vom Fachmann war daher zu erwarten, mit der IDP-Nachricht gemäß Schritt 11 auch die Information zu übersenden, dass die Nachricht seitens
     der Vermittlungsstelle GMSC dem Empfang der CSRN folgt. Hierfür konnte die
     CSRN in der IDP-Nachricht übertragen oder ein gesondertes Bit übersandt
     werden, das diese Informationsgrundlage im Sinne einer die Routingsteuerung
     enthaltenden Information anzeigt (Merkmal 2.2), damit die Steuerungseinrichtung feststellen kann, dass der Anruf einer Routingsteuerung unterlag (Merkmale 3 und 3.1), eine CONTINUE-Nachricht an die Vermittlungsstelle folgen kann
     (Merkmal 3.2) und nicht wiederholt die Schritte 2 bis 10 ausgeführt werden
     (Merkmal 1.1).

40          e) Mit einer Konkretisierung oder Weiterentwicklung des in VP2 zu Figur 6.2a.3.2-5 gezeigten Szenarios, bei der mit der IDP-Nachricht gemäß
     Schritt 11 die CSRN oder eine andere, die fortgeschrittene Routingsteuerung
     anzeigende Information übertragen und somit in der Datenverarbeitung der

                                        - 17 -




     Steuerungseinrichtung CCCF auf dieser Informationsgrundlage die Entscheidung getroffen wird, in Schritt 12 eine CONTINUE-Nachricht zu senden, gelangte der Fachmann mithin in naheliegender Weise für das in Figur 6.2a.3.2-5 beschriebene und gegebenenfalls weitere, ähnliche Szenarien - wie beispielsweise das in den Figuren 6.2a.3.2-3 und 6.2a.3.2-4 der VP2 beschriebene - zu einem Verfahren mit allen Merkmalen des Gegenstands von Patentanspruch 1.

41          2. Für eine abweichende Beurteilung der Patentfähigkeit des Gegenstands der Nebenansprüche 9, 14 und 15, mit denen jeweils Vorrichtungen beziehungsweise ein System von Vorrichtungen beansprucht werden, die in der
     Lage sind, ein Verfahren gemäß der Lehre von Patentanspruch 1 durchzuführen, sowie der den Patentansprüchen 1, 9, 14 und 15 untergeordneten Ansprüche des Streitpatents ist nichts geltend gemacht und für den Senat nichts ersichtlich.

                                        - 18 -




42          IV. Die Kostenentscheidung beruht auf § 121 Abs. 2 PatG, § 91 Abs. 1
     ZPO.


     Meier-Beck                        Grabinski                       Hoffmann


                       Schuster                        Deichfuß



     Vorinstanz:
     Bundespatentgericht, Entscheidung vom 18.09.2013 - 5 Ni 72/11 (EP) -
