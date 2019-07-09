---
ecli: "ECLI:DE:BPatG:2019:090719B17Wpat31.16.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 31/16"
decided: "2019-07-09"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=29&nr=36127&anz=817&pos=448&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-07-09_17_W-pat_31_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 31/16 vom 2019-07-09

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 31/16                                                Verkündet am
 _______________                                                  9. Juli 2019
    (Aktenzeichen)                                                     …




                            BESCHLUSS

                          In der Beschwerdesache


              betreffend die Patentanmeldung 10 2014 101 174.0


…




hat der 17. Senat (Technischer-Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 9. Juli 2019 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Phys. Dr. Forkel und der
Richterinnen Dipl.-Phys. Zimmerer und Akintche




ECLI:DE:BPatG:2019:090719B17Wpat31.16.0

                                        -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                     Gründe


                                         I.


Die vorliegende Patentanmeldung wurde am 30. Januar 2014 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


 „System und Verfahren zum Unterbinden einer Auslieferung von Werbeinhalten“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F des
Deutschen Patent- und Markenamtes in der Anhörung vom 10. März 2016 zurückgewiesen. Zur Begründung führte die Prüfungsstelle aus, dass der Gegenstand
des jeweiligen Patentanspruchs 1 nach Hauptantrag sowie Hilfsantrag I und II
mangels einer erfinderischen Tätigkeit nicht patentfähig sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellte den Antrag,


        den Beschluss der Prüfungsstelle für Klasse G06F des Deutschen
        Patent- und Markenamts vom 10. März 2016 aufzuheben und das
        nachgesuchte Patent auf der Grundlage folgender Unterlagen zu
        erteilen:

                                      -3-



        gemäß Hauptantrag mit
        Patentansprüchen 1 bis 18 vom 10. März 2016,
        Beschreibung Seiten 1 bis 21 sowie
        3 Blatt Zeichnungen mit Figuren 1 bis 3, jeweils vom Anmeldetag;


        gemäß Hilfsantrag I mit
        Patentansprüchen 1 bis 17 vom 10. März 2016,
        Beschreibung und Zeichnungen wie Hauptantrag;


        gemäß Hilfsantrag II mit
        Patentansprüche 1 bis 14 vom 10. März 2016,
        Beschreibung und Zeichnungen wie Hauptantrag;


        gemäß Hilfsantrag III mit
        Patentansprüchen 1 bis 15 vom 2. Juli 2019,
        Beschreibung und Zeichnungen wie Hauptantrag;


        gemäß Hilfsantrag IV mit
        Patentansprüchen 1 bis 14 vom 2. Juli 2019,
        Beschreibung und Zeichnungen wie Hauptantrag;


        gemäß Hilfsantrag V mit
        Patentansprüchen 1 bis 11 vom 2. Juli 2019,
        Beschreibung und Zeichnungen wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind die Druckschriften


D1:    Firewall – Wikipedia. Mit Stand vom 13. Januar 2014.
URL: http://de.wikipedia.org/w/index.php?title=Firewall&oldid=126432695;

                                     -4-



D2:    Cisco: PIX/ASA URL Filtering Configuration Example. Mit Stand vom
10. Oktober 2008.
URL:      http://www.cisco.com/c/en/us/support/docs/security/pix-500-seriessecurity-appliances/97277-pix-asa-url-filtering.html;


D3:    Application firewall – Wikipedia. Mit Stand vom 04.01.2014.
URL: https://en.wikipedia.org/w/index.php?title=Application_firewall&
oldid=589113873 [abgerufen am 11.02.2016];


D4:    RFC 6455 – The WebSocket Protocol. Internet Engineering Task Force
(IETF), Dezember 2011.
URL: https://tools.ietf.org/html/rfc6455 [abgerufen am 11.02.2016]


und


D5:    Ereignis (Programmierung) – Wikipedia. Mit Stand vom 03.04.2013.
URL:
https://de.wikipedia.org/w/index.php?title=Ereignis_%28Programmierung
%29&oldid=116865717
[abgerufen am 10.03.2016]


genannt worden. Vom Senat wurden zusätzlich die Druckschriften


D6:    US 2006/0235960 A1;


D7:    US 8 527 774 B2;


D8:    US 2003/0233482 A1


und

                                       -5-



Dy:    HTML5 – WebSockets Tutorial.
URL:
http://web.archive.org/web/20130802031616/http://www.tutorialspoint.com/ht
ml5/html5_websocket.htm [abgerufen am 04.07.2019]


eingeführt.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


M1     Verfahren zum Unterbinden einer Auslieferung von Werbeinhalten und/oder
       Werbemitteln (35) von einer Servereinrichtung an eine Clienteinrichtung (5),
       wobei


M2     an der Clienteinrichtung ein elektronisches Dokument zur Anzeige gebracht
       wird, wobei


M3     in dem elektronischen Dokument ein Clientskript eingebettet ist, das beim
       Laden oder nach dem Laden des elektronischen Dokuments zur Ausführung
       gebracht wird, wobei


M4     das Clientskript über eine Socketverbindung (SV) eine Werbemittelanfragenachricht (WMA) an die Servereinrichtung sendet, und wobei


M5     ein Werbeblocker (15) der Clienteinrichtung


M6     (a)     Verbindungsaufbauversuche der Clienteinrichtung (5) zu der Servereinrichtung überwacht (S10),

                                         -6-



M7      (b)   bei einem erkannten Verbindungsaufbauversuch (S15) ermittelt, ob
        für den Verbindungsaufbauversuch das WebSocket-Protokoll verwendet
        wird (S20),


M8      (c)   falls für den Verbindungsaufbauversuch das WebSocket-Protokoll
        verwendet wird, für den Uniform Resource Identifier (URI) des Verbindungsaufbauversuches überprüft, ob dieser für den Verbindungsaufbau verwendet
        werden darf (S30),


M9      (d)   und falls die Prüfung (S30) ergibt, dass der Uniform Resource Identifier (URI) für den Verbindungsaufbau nicht verwendet werden darf (S40),
        den Verbindungsaufbauversuch beendet (S50),


M10     und anderenfalls den Verbindungsaufbauversuch zur Servereinrichtung
        zulässt (S60) und die mit einer Werbemittelübertragungsnachricht von der
        Servereinrichtung entgegengenommenen und in der Werbemittelübertragungsnachricht enthaltenen Werbeinhalte (35) in das elektronische Dokument einfügt.


Im Patentanspruch 1 gemäß Hilfsantrag I schließen sich die jeweiligen Merkmale
M6x, M6y und M6z direkt an Merkmal M6 an. Merkmal M7 wird ersatzlos gestrichen:


M6x     wobei das Überwachen der Verbindungsaufbauversuche (S10) von einem
        Event-Listener durchgeführt wird, der an der Clienteinrichtung für Verbindungsaufbau-Ereignisse registriert worden ist,


M6y wobei ein Event ausgelöst wird, wenn für einen Verbindungsaufbauversuch
        das Websocket-Protokoll verwendet wird,

                                       -7-



M6z   wobei das Event den für den Verbindungsaufbauversuch verwendeten Uniform Resource Identifier (URI) umfasst,


Der Patentanspruch 1 gemäß Hilfsantrag II unterscheidet sich vom Patentanspruch 1 gemäß Hilfsantrag I durch die jeweiligen Merkmale M8x, M8y und M8z,
die zwischen den Merkmalen M8 und M9 eingeschoben werden, d. i.


M8x   wobei in einem Schritt (S31) überprüft wird, ob Verbindungsaufbauversuche
      generell zugelassen werden, indem eine in der Clienteinrichtung (5) gespeicherte eindeutige Kennung an einen Drittserver übertragen wird


M8y und als Antwort auf die übertragene eindeutige Kennung von dem Drittserver eine Rückgabenachricht empfangen wird, die eine Information darüber
      umfasst, ob die Überprüfung positiv ist


M8z   und falls diese Überprüfung positiv ist, den Verbindungsaufbauversuch zur
      Servereinrichtung zulässt, wobei die eindeutige Kennung eine Benutzerkennung ist,


Patentanspruch 1 gemäß Hilfsantrag III basiert auf Patentanspruch 1 gemäß
Hauptantrag, wobei Merkmal M2k an die Stelle von Merkmal M2 tritt. Außerdem
wird Merkmal M6k zwischen den Merkmalen M6 und M7 und Merkmal M9k zwischen den Merkmalen M9 und M10 eingefügt, d. i.


M2k an der Clienteinrichtung eine Clientsoftware zur Ausführung gebracht wird,
      in der ein elektronisches Dokument zur Anzeige gebracht wird, wobei


M6k wobei ein Verbindungsaufbauversuch ein Versuch ist, eine Verbindung zur
      Servereinrichtung aufzubauen,

                                      -8-



M9k   wodurch eine Kommunikation von der Clientsoftware zur Servereinrichtung
      nicht zustande kommt,


Patentanspruch 1 gemäß Hilfsantrag IV geht aus Patentanspruch 1 gemäß Hilfsantrag I hervor, wobei Merkmal M2k das Merkmal M2 ersetzt. Merkmal M6k wird
zwischen den Merkmalen M6 und M6x, Merkmal M9k wird zwischen den Merkmalen M9 und M10 eingefügt.


Patentanspruch 1 gemäß Hilfsantrag V beruht auf Patentanspruch 1 gemäß Hilfsantrag II. Dabei ersetzt Merkmal M2k das Merkmal M2. Merkmal M6k folgt unmittelbar auf Merkmal M6, Merkmal M9k folgt auf Merkmal M9.


In Hinblick auf die übrigen Patentansprüche wird auf den Akteninhalt verwiesen.


Die Anmelderin trägt vor, der Zweck des anspruchsgemäßen Verfahrens bestehe
darin, im Rahmen einer zweistufigen Überprüfung das Anfragen von anzuzeigenden Werbeinhalten mit Hilfe eines Werbeblockers zu unterbinden, sofern die Werbeinhalte mittels des WebSocket-Protokolls von vorbestimmten Servereinrichtungen angefragt würden. Falls also für einen bestimmten nicht zugelassenen URI
das WebSocket-Protokoll verwendet werde, werde bereits der Verbindungsaufbauversuch von dem Werbeblocker blockiert, d. h. beendet, so dass eine Verbindung zu einem Werbemittelserver erst gar nicht eingerichtet bzw. hergestellt
werde. Eine zweistufige Überprüfung, wie sie in der Lehre des Patentanspruchs 1
realisiert sei, sei aus dem bislang aufgezeigten Stand der Technik weder bekannt
noch durch diesen nahegelegt.


Der genannte Stand der Technik könne die Lehre des jeweiligen Patentanspruchs 1 gemäß Hauptantrag sowie Hilfsantrag I bis V weder vorwegnehmen
noch nahelegen. Der Gegenstand des jeweiligen Patentanspruchs 1 gemäß
Hauptantrag und Hilfsanträgen I bis V sei somit nicht nur neu, sondern beruhe
auch auf erfinderischer Tätigkeit.

                                       -9-



                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da das Verfahren nach dem jeweiligen Patentanspruch 1
gemäß Hauptantrag sowie gemäß den Hilfsanträgen I bis V nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung betrifft ein Verfahren und ein System
zum Unterbinden einer Auslieferung von Werbeinhalten und/oder Werbemitteln,
die an einer Clientsoftware, etwa einem Browser, in einem elektronischen Dokument, beispielsweise einer Webseite zur Anzeige gebracht werden sollen (Offenlegungsschrift, Absatz [0001]).


Ausweislich der Anmeldung sei es allgemein bekannt, in elektronischen Dokumenten, etwa Webseiten, Werbeinhalte bzw. Werbemittel einzublenden. Der Betreiber der Website könne durch das Einblenden der Werbeinhalte zusätzliche
Einnahmen generieren, beispielsweise dann, wenn ein Benutzer der Webseite die
Werbung anklicke. Inhalteanbieter, die ihre Inhalte auf Webseiten publizierten,
finanzierten sich in den meisten Fällen über die auf der Webseite zusätzlich eingeblendete Werbung (Offenlegungsschrift, Absatz [0002]). Die Betreiber solcher
Webseiten verwalteten die eingeblendete Werbung in den meisten Fällen nicht
selbst, sondern bezögen diese von einem externen Werbemittelvermarkter, der
die verfügbaren Werbemittel bzw. Werbeinhalte auf einem Werbemittelserver zum
Abruf bereithalte. Der Betreiber der Webseite müsse lediglich einen Verweis auf
den einzublendenden Werbeinhalt auf dem Werbemittelserver in die Webseite
einfügen, so dass beim Abruf der Webseite, beispielsweise in einem Internetbrowser, die Webseite von dem Webserver des Betreibers der Webseite und die Werbeinhalte von dem Werbemittelserver des Werbemittelvermarkters geladen würden (Offenlegungsschrift, Absatz [0003]). Das Laden der Werbeinhalte von dem
Werbemittelserver des Werbemittelvermarkters könne unter Verwendung des
Websocket-Protokolls erfolgen. Hierbei werde die Webseite in herkömmlicher

                                      - 10 -



Weise unter Verwendung des HTTP-Protokolls von dem Webserver geladen.
Während des Ladens der Webseite könne ein in die Webseite eingebundenes
Script die anzuzeigenden Werbeinhalte unter Verwendung des Websocket-Protokolls von einem Werbemittelserver nachladen und in der geladenen Webseite zur
Anzeige bringen (Offenlegungsschrift, Absatz [0004]). Nachteilig sei hierbei allerdings, dass die Werbeinhalte auch dann eingeblendet würden, wenn der Benutzer,
der die Webseite abrufe, diese Werbeinhalte gar nicht sehen möchte, um beispielsweise die zu übertragende Datenmenge zu reduzieren (Offenlegungsschrift,
Absatz [0005]). Ferner sei es bekannt, zahlenden Benutzern Webseiten ohne
Werbemittel bzw. Werbeinhalte auszuliefern. Sofern die Webseiten allerdings
auch von nicht zahlenden Benutzern abgerufen werden könnten, habe dies den
Nachteil, dass die Webseiten in zwei Versionen zur Verfügung gestellt werden
müssten, nämlich ohne und mit Werbeinhalten. Damit gehe ein erhöhter Aufwand
für die Pflege der Webseiten einher. Auf Benutzerseite ergebe sich der Nachteil,
dass sich der zahlende Benutzer gegenüber dem Anbieter der Webseiten authentifizieren müsse, damit der Betreiber der Webseiten entscheiden könne, ob eine
abgerufene Webseite mit oder ohne Werbeinhalte ausgeliefert werde. Dies könne
beispielsweise mittels eines Log-ins des Benutzers erfolgen. Alternativ könnten an
der Clienteinrichtung des Benutzers Cookies gespeichert werden, die Informationen darüber enthielten, ob eine abgerufene Webseite mit oder ohne Werbeinhalte
auszuliefern sei. Seien solche Cookies nicht verfügbar, weil z. B. das Speichern
von Cookies auf der Clienteinrichtung nicht erlaubt sei, würden die vom Benutzer
angeforderten Webseiten im Zweifel immer mit den Werbeinhalten ausgeliefert,
selbst wenn der Benutzer diese Werbeinhalte nicht möchte (Offenlegungsschrift,
Absatz [0006]).


Der Anmeldung soll die Aufgabe zugrunde liegen, ein System und ein Verfahren
bereitzustellen, welche die aus dem Stand der Technik bekannten Nachteile
zumindest teilweise vermeiden und die es ermöglichen, das Einblenden von Werbemitteln bzw. Werbeinhalten in einem elektronischen Dokument, etwa einer

                                        - 11 -



Website, auf einfache Art und Weise zuverlässig zu verhindern und/oder zu steuern (Offenlegungsschrift, Absatz [0007]).


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zum Unterbinden
einer Auslieferung von Werbeinhalten und/oder Werbemitteln von einem Server an
einen Client zu verbessern, ist ein Diplom-Informatiker mit mehrjähriger Berufserfahrung in der Applikationsentwicklung anzusehen, der insbesondere über fundierte Kenntnisse auf dem Gebiet der Softwareentwicklung in einer verteilten Systemumgebung verfügt.


2.    Der Hauptantrag hat keinen Erfolg, weil das Verfahren seines Patentanspruchs 1 nicht auf erfinderischer Tätigkeit beruht.


2.1   Zur Lehre des Patentanspruchs 1


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hauptantrag ein Verfahren zum Unterbinden einer Auslieferung von Werbeinhalten von einer Servereinrichtung an eine Clienteinrichtung vor (Merkmal M1), wobei
ein Clientscript, das in ein an der Clienteinrichtung zur Anzeige bringbaren Dokument eingebettet ist, die Werbeinhalte mittels einer Werbemittelanfragenachricht
von der Servereinrichtung anfragt (Merkmale M2, M3, M4).


Ein Werbeblocker überwacht hierbei die Verbindungsaufbauversuche der Clienteinrichtung zu der Servereinrichtung (Merkmale M5, M6). Er ermittelt, ob für einen
Verbindungsaufbauversuch das WebSocket-Protokoll verwendet wird (Merkmal
M7) und überprüft, ob der Uniform Resource Identifier (URI) des Verbindungsaufbauversuches verwendet werden darf, sofern für den Verbindungsaufbauversuch
das WebSocket-Protokoll verwendet wurde (Merkmal M8).


Falls der URI nicht verwendet werden darf, wird der Verbindungsaufbauversuch
beendet (Merkmal M9). Andernfalls wird der Verbindungsaufbauversuch fortge-

                                      - 12 -



setzt, und die Clienteinrichtung nimmt die angefragten Werbeinhalte entgegen und
bettet diese in das Dokument ein (Merkmal M10).


2.2   Zur Beurteilung der beanspruchten Lehre ist die Druckschrift D6 von besonderer Bedeutung.


Die Druckschrift D6 offenbart ein Verfahren zum Unterbinden unerwünschter Werbung beim Navigieren im Web (Abs. [0002]; Abstract). Das bekannte Verfahren
beruht auf einer Software 3, die im Speicher 2 eines elektronischen Geräts 1 hinterlegt ist und die über wenigstens ein Sperrmodul 30 (blocking module) verfügt.
Im Sperrmodul 30 sind eine Sperrbedingung 31 und eine Verarbeitungsbedingung
32 definiert, die bei Ausführung der Software 3 während des Herunterladens von
Webseiten berücksichtigt werden. Wenn das Computerprogramm 3 feststellt, dass
ein Teil einer heruntergeladenen Webseite die Sperrbedingung 31 eines Sperrmoduls 30 erfüllt (also unerwünscht ist), wird der Inhalt der Webseite gemäß derjenigen Verarbeitungsbedingung 32 weiterverarbeitet, welche der Sperrbedingung 31
entspricht, und die Anzeige der nicht gewollten Webinhalte, z. B. von Werbung auf
dem elektronischen Gerät 1 wird verhindert. Die gewünschten bzw. nicht gesperrten Webinhalte werden hingegen wie gewohnt wiedergegeben (Fig. 1, 2; Abs.
[0027]).
Das Computerprogramm 3 ist entweder im Betriebssystem des elektronischen
Geräts 1 eingebunden oder aber im Browser eingebettet, so dass Webinhalte
bereits beim Download verarbeitet werden können (Abs. [0028]).


So führt die Druckschrift D6, die als nächstliegender Stand der Technik anzusehen
ist, den Fachmann zu einem Verfahren zum Unterbinden einer Auslieferung von
Werbeinhalten von einer Server- an eine Clienteinrichtung bzw. einem elektronischen Gerät (Abstract, siehe „… blocking network advertising …“; Abs. [0028],
siehe „If any content is downloaded to the electronic device 1 after the electronic
device 1 is connected to the network, the electronic device 1 will immediately use
the blocking software program 3 to process the webpage editing content and block

                                      - 13 -



the unwanted network advertising.“; Fig. 1). Merkmal M1 ist somit in der Druckschrift D6 offenbart.


Im bekannten Verfahren wird an der Clienteinrichtung ein elektronisches Dokument zur Anzeige gebracht. Bei dem Dokument handelt es sich um eine aus dem
Internet herunter geladene Webseite, die in einem Browser ausgegeben wird
(Abs. [0029] u. a. – Merkmal M2).


Weiterhin ist im elektronischen Dokument wenigstens ein Clientscript eingebunden, das beim Laden des Dokuments ausgeführt wird. So wird in der Druckschrift
D6 auf die Ausführung von Popupbefehlen aus JavaScript hingewiesen, die mit
speziellen Webadressen verknüpft sind (Abs. [0030], siehe „such as window.open
and document.open instructions of JavaScript“ – Merkmal M3).


Im Verfahren der Druckschrift D6 schickt das Clientscript eine Werbemittelanfragenachricht an die Servereinrichtung. Gleichzeitig öffnet das elektronische Gerät
entsprechend einem Popupbefehl ein weiteres Browserfenster, in dem die über
eine Webadresse angeforderte Webseite mit Werbeinhalten dargestellt wird (Abs.
[0030], siehe „… and another webpage editing content is loaded from the specified
URL address … to display the popup advertising.“ – teilweise Merkmal M4).


Um die Ausgabe unerwünschter Werbeinhalte auf dem elektronischen Gerät zu
verhindern, ist im Verfahren der Druckschrift D6 ein Werbeblocker in Gestalt eines
Computerprogramms mit einer Mehrzahl von Sperrmodulen vorgesehen (Fig. 1;
Abs. [0027] u. a. – Merkmal M5).


Das bekannte Computerprogramm wird ausgeführt, während eine Webseite auf
das elektronische Gerät heruntergeladen wird.
Anhand von in den Sperrmodulen enthaltenen Bedingungen („blocking conditions“) überwacht das Computerprogramm, ob gewisse Webinhalte angezeigt werden sollen bzw. ob der Versuch, zur zugehörigen Servereinrichtung eine Verbin-

                                       - 14 -



dung aufzubauen, überhaupt erfolgreich durchgeführt werden kann (Abs. [0027] –
Merkmal M6). Insbesondere wird mittels eines Blacklist Sperrmoduls geprüft, ob
ein in die Webseite eingebundener Befehl, z. B. ein JavaScript-Befehl ausgeführt
und eine zugehörige Webadresse für einen Verbindungsaufbau zur Servereinrichtung verwendet werden darf (Abs. [0033] – teilweise Merkmal M8).


Stimmt die Webadresse mit einer der im Sperrmodul hinterlegten Adressen überein, wird ein Verbindungsaufbauversuch beendet (d. h. der zugehörige JavaScript
Befehl kommt erst gar nicht zur Ausführung), wodurch ein Herunterladen von
Webinhalten bzw. Werbung verhindert wird (Abs. [0033], siehe „… and the specified URL address of the blocking condition 31 defined by the blacklist blocking
module 301, the the electronic device 1 will prohibit loading and processing the
specified URL address. Therefore, the download will be prohibited and the instructions such as popup instruction, floating instruction or descriptive instruction will
not be executed …“ – Merkmal M9).


Andernfalls wird ein Verbindungsaufbauversuch zur Servereinrichtung zugelassen
und die angefragten Webinhalte mit Werbung werden auf das elektronische Gerät
heruntergeladen und dort dargestellt (Abs. [0033], siehe „… then such webpage
editing content will be considered normal and the download and processing will be
carried out as usual.“). Merkmal M10 ist somit in der Lehre der Druckschrift D6
verwirklicht.


Die Verwendung von WebSocket-Verbindungen (restlicher Teil von Merkmal M4),
die Ermittlung, ob für einen Verbindungsaufbauversuch das WebSocket-Protokoll
verwendet wird (Merkmal M7) sowie die Bedingung, den URI dann zu überprüfen,
wenn für einen Verbindungsaufbauversuch das WebSocket Protokoll verwendet
wird (restlicher Teil des Merkmals M8) gehen aus Druckschrift D6 aber direkt nicht
hervor.

                                        - 15 -



2.3   Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
das mit dem Patentanspruch 1 gemäß Hauptantrag beanspruchte Verfahren für
den Fachmann nahegelegen hat.


Da der Fachmann stets bestrebt ist, technische Weiterentwicklungen zu berücksichtigen, lag es für in nahe, in der Lehre der Druckschrift D6 neben JavaScript
noch andere – insbesondere für Java-Entwickler relevante – Webtechnologien,
wie z. B. WebSockets mit einzubeziehen, mit denen Browser und Server Nachrichten austauschen können, ohne sich an den aus dem HTTP-Protokoll bekannten Anfrage-Antwort-Zyklus halten zu müssen und die eine persistente Verbindung
ermöglichen. Dem Fachmann ist geläufig, wie die zum Öffnen einer WebSocket
erforderliche Anweisung in JavaScript Code eingebunden werden muss, um beim
Herunterladen einer Webseite zwischen Client und Server Nachrichten übertragen
zu können. Dass das Einbinden von WebSockets in HTML-Seiten bzw.
JavaScript-Code bereits vor dem Anmeldetag der Patentanmeldung hinlänglich
bekannt war, wird z. B. in Druckschrift Dy gezeigt (siehe Seite 2, Abschnitt „Client
Side HTML & JavaScript Code“). Für den Fachmann bot es sich an, das Sperrmodul aus Druckschrift D6 derart zu erweitern, dass der zugehörige Werbeblocker
nicht nur JavaScript-Befehle zum Öffnen neuer Fenster erkennen und verarbeiten
kann, sondern ebenso in der Lage ist, Anweisungen zu überwachen, die
WebSockets erzeugen und die neben dem jeweiligen URL optional einen Subprotokollparameter übernehmen (vgl. Dy Seite 1, Befehl new webSocket (url,
[protocol])). Eine solche erweiterte Lehre ermöglicht nicht nur, bei einem Verbindungsaufbauversuch zu erkennen, ob eine WebSocket eingerichtet werden soll
(anhand des new WebSocket Befehls – Merkmal M7), sondern auch, ob der zugehörige URL verwendet werden darf bzw. zulässig ist. Dementsprechend wird eine
Werbemittelanfragenachricht über eine Socketverbindung vom Clientskript an die
Servereinrichtung dann versandt (restlicher Teil von Merkmal M4), wenn sowohl
das WebSocket Protokoll verwendet wird (restlicher Teil von Merkmal M8) als
auch der zugehörige URL zulässig ist.

                                       - 16 -



Demgegenüber argumentiert die Anmelderin, die Druckschrift D6 offenbare nicht,
dass ein Verbindungsaufbauversuch – also der Versuch, eine Verbindung aufzubauen – beendet werde. Vielmehr werde dort nicht ein Verbindungsaufbauversuch
beendet, sondern es würden Maßnahmen vorgeschlagen, die verhindern sollen,
dass es zu einem solchen Verbindungsaufbauversuch kommt. Da es nach der
Lehre der Druckschrift D6 für nicht zugelassene Webadressen erst gar nicht zu
einem Verbindungsaufbauversuch komme, offenbare die Druckschrift D6 auch
nicht, einen solchen Verbindungsaufbauversuch zu beenden.


Dem Einwand kann nicht gefolgt werden. Da sich die Beschreibung der Patentanmeldung in Hinblick auf den Begriff Verbindungsaufbauversuch im Wesentlichen in der Feststellung erschöpft, ein Verbindungsaufbauversuch sei ein Versuch, eine Verbindung zur Servereinrichtung aufzubauen, ist aus fachmännischer
Sicht davon auszugehen, dass ein solcher Versuch sämtliche Ereignisse und Verfahrensschritte umfasst, die der für den Datenverkehr eingerichteten Verbindung
vorangegangen sind und die zu deren Zustandekommen unmittelbar beigetragen
haben. Demnach wird der Fachmann einen Verbindungsaufbauversuch bereits
darin erkennen, wenn eine Webseite mit eingebettetem Script in den Browser
geladen wird, wobei das Script die URL-Zieladresse einer Datei umfasst, die in ein
neues Browserfenster geladen werden soll. Nichts anderes ist aber in der Druckschrift D6 offenbart.


Ferner führt die Anmelderin aus, ein wesentlicher Vorteil der beanspruchten Lehre
bestehe darin, sogar verschleierte („obfuscated“) URLs erkennen und verarbeiten
zu können. Die aus dem aufgezeigten Stand der Technik bekannten Verfahren
seien hierzu grundsätzlich nicht in der Lage.


Der Einwand geht bereits deswegen fehl, weil der Patentanspruch 1 ersichtlich
nicht verlangt, dass die beanspruchte Lehre im Fall verschleierter Webadressen
wirksam angewendet werden soll.

                                      - 17 -



Es waren für den Fachmann somit lediglich fachgemäße Überlegungen erforderlich, um in Kenntnis der Druckschrift D6 zu einem Verfahren mit sämtlichen Merkmalen des Patentanspruchs 1 in der Fassung des Hauptantrags zu gelangen.


2.4   Da über einen Antrag nur einheitlich entschieden werden kann, sind auch
die Patentansprüche 2 bis 18 gemäß Hauptantrag nicht gewährbar (BGH GRUR
1997, 120 – Elektrisches Speicherheizgerät).


3.    Hilfsantrag I ist nicht günstiger als der Hauptantrag zu bewerten.


3.1   Patentanspruch 1 gemäß Hilfsantrag I unterscheidet sich von Patentanspruch 1 gemäß Hauptantrag durch die Merkmale M6x bis M6z. Merkmal M7 ist
weggelassen.


Der anspruchsgemäße Werbeblocker ist dazu ausgelegt, Verbindungsaufbauversuche der Client- zu einer Servereinrichtung, die das WebSocket-Protokoll verwenden, zu überwachen. Laut Merkmal M6x ist zu diesem Zweck auf der Clienteinrichtung ein Listener registriert, der Events bzw. Ereignisse zu Verbindungsaufbauversuchen abhört, die das WebSocket-Protokoll nutzen. Sobald ein Verbindungsaufbauversuch über das WebSocket-Protokoll durchgeführt wird, wird
gemäß Merkmal M6y ein entsprechendes Event ausgelöst, das von einem dem
Event zugeordneten Programm verarbeitet wird. Merkmal M6z besagt, dass das
Event den für den Verbindungsaufbauversuch verwendeten Uniform Resource
Identifier (URI) als Parameter umfasst, der an das das Event verarbeitende Programm übergeben wird.


Zwar ist die Überwachung und Verarbeitung von Events bzw. Ereignissen einer
der grundlegenden Aspekte der Programmierung mit JavaScript, denn üblicherweise werden entsprechende Programme nicht linear durchlaufen, sondern die
einzelnen Programmteile werden erst beim Eintritt bestimmter Ereignisse ausgeführt, wobei die Ereignisse, welche zur Steuerung des Kontrollflusses verwendet

                                       - 18 -



werden können, vielfältig sind, z. B. Mausklicks oder Statusmeldungen im
Browser. Dennoch handelt es sich bei einer Ereignisbehandlung aus fachmännischer Sicht um ein allgemeines Programmierkonzept, das nicht nur auf die
Anwendung von JavaScript in Webseiten beschränkt ist, sondern das sich prinzipiell mit den gängigen Konzepten der objektorientierten Programmierung unter
diversen Programmiersprachen gut kombinieren lässt. Dementsprechend wird der
Fachmann den Begriff Event-Listener ganz allgemein als Event-Handler bzw.
Ereignisbehandlungsroutine auslegen, der bzw. die aufgerufen werden soll, wenn
ein bestimmtes Ereignis eingetreten ist.


3.2     Für den Patentanspruch 1 gemäß Hilfsantrag I ist eine andere Beurteilung
als für den Patentanspruch 1 gemäß Hauptantrag nicht gerechtfertigt. Die zusätzlichen Merkmale enthalten nichts, was eine Patentfähigkeit begründen könnte.


So geht Merkmal M6x bereits aus der Druckschrift D6 hervor. Das aus der Druckschrift D6 bekannte Computerprogramm mit Sperrmodulen fungiert als Event-Listener, der während des Herunterladens von Webseiten auf einem Client ausgeführt wird (Abs. [0027], siehe „… such that during the process of the electronic
device 1 reading a webpage editing content, the electronic device executes the
blocking software program 3.“) und der dazu eingerichtet ist, Verbindungsaufbauversuche zu wenigstens einem Server zu überwachen, indem in den Webseiten
eingebettete JavaScript-Anweisungen zusammen mit URLs auf Zulässigkeit überprüft werden, wobei bei Auftreten eines unzulässigen URLs ein Verbindungsaufbau zum Server erst gar nicht stattfindet und somit ein mit dem Herunterladen
einer Webseite eingeleiteter Verbindungsaufbauversuch beendet wird (Abs.
[0033], siehe „… then the electronic device 1 will prohibit loading and processing
the specified URL address.“). Der Fachmann wird erkennen, dass das Auftreten
eines unzulässigen URLs ein Ereignis, z. B. in Form einer Statusmeldung bzw.
eines (geänderten) Signalstatus auslöst, das durch das Computerprogramm der
Druckschrift D6 nach Art einer Ausnahmebehandlung verwertet wird (Merkmal
M6x).

                                       - 19 -



Insofern ist einem solchen Ereignis immer auch ein URL zugeordnet, der für einen
Verbindungsaufbau verwendet werden soll (Merkmal M6z).
Merkmal M6y, wonach ein Event bzw. Ereignis ausgelöst wird, wenn für einen
Verbindungsaufbauversuch das WebSocket-Protokoll verwendet wird, geht aus
Druckschrift D6 nicht unmittelbar hervor.
Aus fachmännischer Sicht ergeben sich allerdings Ereignisse, die durch Verwendung des WebSocket-Protokolls ausgelöst werden, in der durch WebSockets (vgl.
Dy) ergänzten Lehre der Druckschrift D6 als unmittelbare Folge.
Zur Vermeidung von Wiederholungen sei daher an dieser Stelle auf die Ausführungen unter Abschnitt 2.3 hingewiesen (Merkmal M6y).


Unter Berücksichtigung der Ausführungen zum Hauptantrag sind sämtliche Merkmale des Gegenstandes nach Patentanspruch 1 gemäß Hilfsantrag I aus der
Druckschrift D6 nahegelegt.


3.3   Mit dem Patentanspruch 1 gemäß Hilfsantrag I fallen auch die Patentansprüche 2 bis 17.


4.    Auch dem Hilfsantrag II kann nicht stattgegeben werden, weil die Lehre seines Patentanspruchs 1 für den Fachmann nahegelegen hat.


4.1   Gegenüber Patentanspruch 1 gemäß Hilfsantrag I sind in Patentanspruch 1
gemäß Hilfsantrag II noch die Merkmale M8x bis M8z neu hinzugekommen.


Merkmal M8x sieht vor, dass der Werbeblocker überprüft, ob Verbindungsaufbauversuche generell zugelassen werden, indem eine in der Clienteinrichtung gespeicherte eindeutige Kennung an einen Drittserver übertragen wird. In Merkmal M8y
wird beansprucht, dass als Antwort auf die übertragene eindeutige Kennung von
dem Drittserver eine Rückgabenachricht empfangen wird, die eine Information
darüber umfasst, ob die Überprüfung positiv ist. Erweist sich die Überprüfung als

                                        - 20 -



positiv, wird der Verbindungsaufbauversuch laut Merkmal M8z zugelassen. Dabei
stellt die eindeutige Kennung eine Benutzerkennung dar.


4.2    Für die Beurteilung der Patentfähigkeit der beanspruchten Lehre ist neben
der Druckschrift D6 noch die Druckschrift D7 von Bedeutung.


Die Druckschrift D7 offenbart ein System und Verfahren zur Unterstützung eines
Sicherheitsmanagements für Webanwendungen. Im bekannten Verfahren arbeitet
ein Gateway Server als Vermittler mit Client und Remote Server Systemen zusammen, um eine Sicherheitslösung für verteilte Webanwendungen zu verwirklichen
(Abstract).


Die Druckschrift D7 lehrt somit ein Verfahren zur sicheren Nutzung von Webdiensten, die die Auslieferung beliebiger Informationen, wie z. B. Nachrichtenartikel
oder Informationen zum Wertpapierhandel von Server- an Clienteinrichtungen
anbieten. Die Nutzung der Webdienste wird allerdings auf registrierte Benutzer
beschränkt, so dass die Auslieferung von Informationen an Benutzer ohne Zugangsberechtigung unterbunden ist (Spalte 3, Zeilen 35 bis 38; Spalte 3, Zeile 66
bis Spalte 4, Zeile 4). Insoweit ist Merkmal M1 wenigstens teilweise erfüllt.


Im Verfahren der Druckschrift D7 wird an einer der Clienteinrichtungen ein elektronisches Dokument bzw. eine Webseite zur Anzeige gebracht (Spalte 3, Zeile 66
bis Spalte 4, Zeile 4 u. a. – Merkmal M2).


Im elektronischen Dokument ist eine Web Client-Anwendung eingebettet, die nach
dem Laden des elektronischen Dokuments zur Ausführung gebracht wird (Spalte 4, Zeilen 65 bis Spalte 5, Zeile 3, siehe „Web-client application 64“ – Merkmal M3).

                                       - 21 -



Weiterhin nutzt die Lehre der Druckschrift D7 Webdienste, indem Client-Anwendung und Server über WebSocket-Verbindungen miteinander kommunizieren
(Spalte 5, Zeilen 15 bis 19 – restlicher Teil von Merkmal M4).


Um im Verfahren der Druckschrift D7 eine WebSocket-Verbindung zwischen Web
Client-Anwendung und Webdienst einzurichten, wird ein Sicherheitstoken („secure
token“) zunächst an einen Gateway Server, d. i. einen Drittserver übertragen. Dort
wird das Token validiert und die daraus gewonnenen Anmeldedaten des Benutzers überprüft. Wird die Gültigkeit des Tokens nachgewiesen, wird der Verbindungsaufbau zum Webdienst grundsätzlich zugelassen (Spalte 11, Zeile 57 bis
Spalte 12, Zeile 12 – Merkmal M8x).


Wird das Sicherheitstoken als gültig erkannt, d. h. die Überprüfung ist positiv, wird
das Token in einer Bestätigungsnachricht vom Gateway Server zurück an die
Client-Anwendung übertragen (Spalte 12, Zeilen 7 bis 10). Merkmal M8y ist
sonach erfüllt.
Bei positiver Überprüfung wird in der Druckschrift D7 der Verbindungsaufbau zwischen Client-Anwendung und Webdienst zugelassen (Spalte 12, Zeilen 1 bis 12
u. a.). Dabei enthält das Token als eindeutige Kennung die Benutzeranmeldeinformationen (Spalte 10, Zeilen 11 bis 14; Spalte 11, Zeilen 65 bis 67 – Merkmal M8z).


Nach Validierung des Sicherheitstokens und erfolgreicher Authentifizierung mittels
der darin enthaltenen Anmeldedaten wird im bekannten Verfahren der Zugriff auf
den Webdienst gestattet bzw. der Verbindungsaufbauversuch zur entsprechenden
Servereinrichtung zugelassen (Spalte 11, Zeile 65 bis Spalte 12, Zeile 12 – teilweise Merkmal M10). Andernfalls wird der Verbindungsaufbauversuch beendet
(Merkmal M9).

                                        - 22 -



4.3    Mit Rücksicht auf den den Druckschriften D6 und D7 entnehmbaren Stand
der Technik fehlt es der Lehre des Patentanspruchs 1 gemäß Hilfsantrag II an der
für die Patentfähigkeit erforderlichen erfinderischen Tätigkeit.


Aufgrund der Tatsache, dass der in der Lösung der Druckschrift D6 enthaltene
Werbeblocker insbesondere bei der Nutzung von Multimediadiensten angewendet
werden soll (vgl. D1, Abs. [0011]), hatte der Fachmann Veranlassung, sich überall
dort nach Anregungen umzusehen, wo Methoden für den sicheren und schnellen
Zugriff auf Webdienste zum Einsatz kommen. Eine mögliche Lösung wird in der
Druckschrift D7 aufgezeigt, welche lehrt, sichere Verbindungen zwischen Web
Client-Anwendungen und Webdiensten über WebSockets aufzubauen.


Angesichts des in der Druckschrift D7 gegebenen Hinweises, WebSocket-basierende, bidirektionale und echtzeitfähige Kommunikationsverbindungen zwischen
Web Client-Anwendungen und Webdiensten zu ermöglichen (vgl. D7 Spalte 3,
Zeilen 47 bis 51), bot es sich für den Fachmann an, die Lehre der Druckschrift D7
auf das System der Druckschrift D6 anzuwenden, indem der Zugang zu Webdiensten, insbesondere Informations- und Werbediensten, nicht nur durch die
URL-Filter der lokalen Sperrmodule (vgl. D6 Fig. 1) sondern zusätzlich durch eine
Vergabe von Zugangsberechtigungen in Form von Sicherheitstokens entsprechend dem Vorbild der Druckschrift D7 gesteuert wird.


Von einer solchen kombinierten Lehre unterscheidet sich die Lehre nach Patentanspruch 1 gemäß Hilfsantrag II im Wesentlichen nur noch dadurch, dass ermittelt
wird, ob für einen Verbindungsaufbauversuch das WebSocket-Protokoll verwendet
wird (Merkmal M7) und der URL dann überprüft wird, falls dieses für einen Verbindungsaufbauversuch genutzt wird (restlicher Teil des Merkmals M8).
Entsprechend den Ausführungen unter Abschnitt 2.3 lag es für den Fachmann
aber nahe, in der Lehre der Druckschrift D6 auch WebSockets zu berücksichtigen
bzw. zu überprüfen (Merkmal M7, restlicher Teil des Merkmals M8).

                                              - 23 -



Nach allem beruht die Lehre des Patentanspruchs 1 gemäß Hilfsantrag II nicht auf
erfinderischer Tätigkeit.


4.4      Mit dem Patentanspruch 1 gemäß Hilfsantrag II fallen auch die übrigen
Patentansprüche.


5.       Die Hilfsanträge III bis V bleiben ohne Erfolg, weil ihr jeweiliger Patentanspruch 1 nichts Zusätzliches enthält, was eine Patentfähigkeit tragen könnte, und
auch kein kombinatorischer Effekt ersichtlich ist.


Die im jeweiligen Patentanspruch 1 gemäß Hilfsantrag III bis V mit den Merkmalen
M2k, M6k und M9k vorgenommenen Klarstellungen können das Vorliegen einer
erfinderischen Tätigkeit nicht begründen.




                                                III.


Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde der
Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für Klasse
G06F des Deutschen Patent- und Markenamtes zurückzuweisen.




                                   Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


      1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
      2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
         kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,

                                            - 24 -



   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek                  Dr. Forkel                     Zimmerer                Akintche




                                                                                           Fa
