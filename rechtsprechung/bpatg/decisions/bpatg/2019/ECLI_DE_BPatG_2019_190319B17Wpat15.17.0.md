---
ecli: "ECLI:DE:BPatG:2019:190319B17Wpat15.17.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 15/17"
decided: "2019-03-19"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=12&nr=34557&anz=817&pos=189&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-03-19_17_W-pat_15_17_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 15/17 vom 2019-03-19

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 15/17                                                   Verkündet am
_______________                                                     19. März 2019
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2015 115 108.1


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 19. März 2019 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Ing. Baumgardt, des Richters
Dipl.-Ing. Hoffmann und der Richterin Akintche




ECLI:DE:BPatG:2019:190319B17Wpat15.17.0

                                      -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                   Gründe


                                       I.


Die vorliegende Patentanmeldung wurde am 8. September 2015 beim Deutschen
Patent- und Markenamt eingereicht und trägt die Bezeichnung


          „Auslieferung von Werbemitteln durch Server an einen Client“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06Q des Deutschen
Patent- und Markenamtes mit Beschluss vom 13. Dezember 2016 zurückgewiesen. Zur Begründung führt die Prüfungsstelle aus, dass die Lehre des Hauptanspruchs dem Patentschutz gemäß § 1 Abs. 3 i. V. m. Abs. 4 PatG nicht zugänglich
sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Zur mündlichen Verhandlung ist die Anmelderin, wie angekündigt, nicht erschienen.


Die Anmelderin beantragt (s. Beschwerde vom 16. Januar 2017), den Zurückweisungsbeschluss aufzuheben und ein Patent auf Grundlage der anhängigen Unterlagen zu erteilen.
Weiterhin beantragt die Anmelderin die Rückzahlung der Beschwerdegebühr.

                                          -3-



Der geltende Patentanspruch 1 (hier mit einer denkbaren Gliederung versehen)
lautet:


1.
M1        Verfahren zur Bereitstellung von Werbemitteln an einen Webclient,
M2        bei dem geprüft wird, ob auf dem Webclient ein Werbeblocker aktiv ist und,
M3        falls die Prüfung ergibt, dass ein Werbeblocker aktiv ist, ein Webserver
          angewiesen wird, ein Werbemittel mittels einer Server-zu-Server-Verbindung von einem Werbemittelserver abzurufen.


Zu den Unteransprüchen 2 bis 8, sowie zu dem nebengeordneten, auf ein Computerprogramm gerichteten, Anspruch 9 wird auf die Akte verwiesen.




                                           II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie hat jedoch keinen Erfolg, da das Verfahren des Patentanspruchs 1 gemäß
§ 1 Abs. 1 i. V. m. Abs. 3 Nr. 3 und Abs. 4 PatG vom Patentschutz ausgeschlossen ist.




1.        Die vorliegende Patentanmeldung betrifft das Gebiet der Auslieferung von
Internetseiten von einem Webserver an einen Webclient über ein Computernetzwerk wie beispielsweise das Internet (vgl. Offenlegungsschrift, Absatz [0001]).


Aus dem Stand der Technik sei bekannt, dass Inhalte im Internet üblicherweise
von einem Webserver bereitgestellt würden.
Bisher hätten sich im Internet Bezahlmodelle für das Betrachten von Internetseiten
noch nicht durchgesetzt, deshalb bestehe eine verbreitete Möglichkeit zur Monetisierung von Webseiten darin, Webinhalte mit Werbemitteln wie beispielsweise

                                        -4-



Bannerwerbung zu versehen. Dadurch könne ein Interessensausgleich zwischen
dem Anbieter von Inhalten und dem Konsumenten erreicht werden.
Da sich Konsumenten im Internet durch Werbung unter Umständen gestört fühlten, würden für Webbrowser sogenannte „Werbeblocker“ angeboten, die üblicherweise als Programm im Hintergrund auf dem Client-Rechner abliefen. Ein solcher
Werbeblocker könne die Werbung auf Webseiten entfernen, bevor die Werbung
dem Konsumenten angezeigt werde. Ein Verfahren, mit dem die Auslieferung von
Werbemitteln verhindert werde, bestehe darin, die URL, Dateinamen oder andere
Bestandteile eines Werbemittels durch einen Werbeblocker zu filtern oder zu blockieren.
Bei einem bekannten Verfahren, welches das Blockieren des Abspielens von Werbemitteln vermeiden solle, werde eine Anfrage eines Client-Computers unter Vermittlung eines Proxy-Servers gestellt und die gewünschten Daten würden vom
Werbungs-Server an den Proxy-Server übertragen. Im Proxy-Server werde die
Absenderinformation der Datenpakete und/oder die Absenderinformation einer in
den Datenpaketen enthaltenen, für den Client-Computer bestimmten Cookie-Datei
manipuliert, um zu vermeiden, dass das Abspielen der Daten im Client-Computer
blockiert werde. Dieses Verfahren habe jedoch den Nachteil, dass ein spezieller
Proxy-Server eingesetzt werden müsse (vgl. Offenlegungsschrift, Absätze [0002]–
[0007]).


Der Anmeldung liegt sinngemäß die Aufgabe zugrunde, alternative und verbesserte Verfahren zur Auslieferung von Werbemitteln von einem Werbeserver an
einen Client bereitzustellen (vgl. Offenlegungsschrift, Absatz [0008]).


Zur Lösung dieser Aufgabe schlägt der Patentanspruch 1 ein Verfahren zur
Bereitstellung von Werbemitteln an einen Webclient (Merkmal M1) vor. Bei dem
Verfahren wird geprüft, ob auf dem Webclient ein Werbeblocker aktiv ist (Merkmal M2). Falls die Prüfung ergibt, dass ein Werbeblocker aktiv ist, wird ein Webserver angewiesen, ein Werbemittel mittels einer Server-zu-Server-Verbindung
von einem Werbemittelserver abzurufen (Merkmal M3).

                                        -5-



Als Fachmann, der mit der Aufgabe betraut wird alternative Verfahren zur Auslieferung von Werbemitteln zu entwickeln bzw. bestehende Verfahren zu verbessern,
ist ein Informatiker oder Programmierer mit mehrjähriger Berufserfahrung im
Bereich der Entwicklung von Webanwendungen – insbesondere im Bereich der
Implementierung von Werbeanzeigen – anzusehen.




2.       Das Verfahren des Patentanspruchs 1 ist vom Patentschutz ausgeschlossen. Bei dem beanspruchten Verfahren handelt es sich nämlich um ein Verfahren
für geschäftliche Tätigkeiten als solche (§ 1 Abs. 1 i. V. m. Abs. 3 Nr. 3 und Abs. 4
PatG).


Gemäß der Rechtsprechung des Bundesgerichtshofs ist bei der Prüfung, ob ein
Ausschlusstatbestand vorliegt darauf abzustellen, ob ein konkretes technisches
Problem mit technischen Mitteln gelöst wird (BGH in GRUR 2010, 613 – Dynamische Dokumentengenerierung, BGH in GRUR 2011, 610 – Webseitenanzeige).


Ein technisches Mittel zur Lösung eines technischen Problems liegt vor, wenn
Gerätekomponenten modifiziert oder grundsätzlich abweichend adressiert werden,
wenn der Ablauf eines zur Problemlösung eingesetzten Datenverarbeitungsprogramms durch technische Gegebenheiten außerhalb der Datenverarbeitungsanlage bestimmt wird oder wenn die Lösung gerade darin besteht, ein Datenverarbeitungsprogramm so auszugestalten, dass es auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt (BGH a. a. O. – Dynamische
Dokumentengenerierung, BGH a. a. O. – Webseitenanzeige).


Nichts anderes gilt, wenn in Rede steht, ob eine beanspruchte Lehre als Plan,
Regel oder Verfahren für gedankliche oder geschäftliche Tätigkeit (§ 1 Abs. 3
Nr. 3 PatG) oder als Wiedergabe von Informationen (§ 1 Abs. 3 Nr. 4 PatG)
vorliegt (BGH in GRUR 2005, 143 – Rentabilitätsermittlung).

                                       -6-



2.1    In dem beanspruchten Verfahren des Anspruchs 1 können keine Anweisungen bzw. Merkmale erkannt werden, die der Lösung eines konkreten technischen
Problems mit technischen Mitteln dienen.


Der Patentanspruch 1 schlägt ein Verfahren vor, mit dem die Einblendung von
Werbeanzeigen auf einem Webclient, d. h. in einem Browser eines Benutzerrechners trotz eines aktiven Werbeblockers, ermöglicht wird. Hierzu prüft das Verfahren, ob auf dem Webclient ein Werbeblocker aktiv ist. Wenn diese Prüfung ergibt,
dass ein Werbeblocker aktiv ist, wird dieser umgangen, indem die Werbeeinblendung mittels einer Server-zu-Server-Verbindung übertragen wird.


Das zugrunde liegende Problem besteht dabei in der Umgehung eines aktiven
Werbeblockers um die Darstellung von Werbeanzeigen auch dann zu gewährleisten, wenn der Benutzer dies mittels eines Werbeblockers verhindern möchte.
Dieses Problem ist geschäftlicher, jedoch nicht technischer Natur.


Denn die beanspruchte Umgehung des Werbeblockers dient der Sicherstellung
der Anzeige von Werbemitteln und somit der Erzielung von Werbeeinnahmen für
den Betreiber einer Webseite. Sie beruht damit auf rein geschäftlichen Überlegungen.


2.2    Das Verfahren des Anspruchs 1 zeigt darüber hinaus in keinem der beanspruchten Teilmerkmale, dass der Ablauf des Datenverarbeitungsprogramms
durch technische Gegebenheiten außerhalb der Datenverarbeitungsanlage bestimmt wird oder dass das Datenverarbeitungsprogramm so ausgestaltet wäre,
dass es auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt.


Die angegebene Prüfung im ersten Teilmerkmal beschränkt sich beim Aufruf einer
Webseite durch den Webclient auf die Erfassung und Übermittlung von Informa-

                                        -7-



tionen über den Webclient, d. h. einer Information die angibt, ob auf dem Webclient ein Werbeblocker aktiv ist.
Hierzu wird bspw. eine Prüfdatei, mit der eine Prüfvariable gesetzt wird, abgerufen, wobei die Datei bei einem aktiven Werbeblocker blockiert wird. Somit kann
der Webserver anhand der Prüfvariablen feststellen, ob ein Werbeblocker aktiv ist.
Die Prüfdatei wird vom Webserver in jedem Fall an den Webclient gesendet, d. h.
unabhängig davon, ob der Werbeblocker aktiv, inaktiv oder überhaupt auf dem
Webclient installiert ist. Der Webserver erhält demnach nur die Information, dass
der Werbeblocker aktiv oder nicht aktiv ist, wobei bei der Information, dass der
Werbeblocker nicht aktiv ist, keine Unterscheidung zwischen einem installierten
inaktiven Werbeblocker und einem nicht installierten Werbeblocker möglich ist.


Der Ablauf dieser Abfrage (dieses Datenverarbeitungsprogramms) ist somit nicht
durch technische Gegebenheiten außerhalb der Datenverarbeitungsanlage bestimmt.


Darüber hinaus ist auch nicht zu erkennen, dass die Abfrage so ausgestaltet wäre,
dass sie auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt.
Denn im vorliegenden Fall wird, wie bereits ausgeführt, eine Prüfdatei vom Webserver zum Webclient übertragen und der Webserver erkennt anhand einer Prüfvariablen, ob ein Werbeblocker aktiv ist oder nicht.


Damit erfolgt aber gerade keine Berücksichtigung der technischen Gegebenheiten, da die Leistungsfähigkeit der Hard- und Softwarekomponenten auf die Abfrage keinerlei Einfluss hat. Es erfolgt auch keine Berücksichtigung der Ressourcen der technischen Komponenten, wie bspw. der begrenzten Leistungsfähigkeit
eines Leitrechners (vgl. BGH a. a. O. – Dynamische Dokumentengenerierung).
Vielmehr werden Einstellungsparameter einer Softwarekomponente abgefragt und
für eine weitere Verarbeitung von Daten bzw. für die Wahl des Übermittlungsweges von Werbung verwendet. Dies geht jedoch über die bloße Verarbeitung von

                                        -8-



Daten nicht hinaus und betrifft nicht die Berücksichtigung der technischen Gegebenheiten der Datenverarbeitungsanlage (vgl. BGH a. a. O. – Webseitenanzeige
Rn. 23 und 25), sondern beschränkt sich auf den bestimmungsgemäßen Einsatz
einer Datenverarbeitungsanlage.


Das zweite Teilmerkmal bezieht sich auf die Auswahl eines alternativen Übertragungsweges, falls ein Werbeblocker aktiv ist.
Durch die Verwendung des alternativen Übertragungsweges soll sichergestellt
werden, dass der Werbeblocker die Werbeeinblendung nicht mehr anhand deren
Absenderadresse erkennen kann und diese somit nicht mehr blockiert.


Ein Einfluss von technischen Gegebenheiten außerhalb der Datenverarbeitungsanlage, d. h. außerhalb des verwendeten Datennetzwerkes, für die Wahl der Übertragungsserver liegt daher nicht vor.


Die Implementierung eines alternativen Übertragungsweges nimmt auch nicht auf
die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht.
Die technische Ausgestaltung der Datenverarbeitungsanlage lässt sowohl eine
direkte Übertragung von Daten von dem Webserver zum Webclient als auch eine
Übertragung von Daten über eine Server-zu-Server-Verbindung zu. Damit
beschränkt sich die Anweisung in diesem Teilmerkmal auf die Vorgabe an den
Programmierer in Abhängigkeit des Wertes einer Prüfvariablen einen von zwei
möglichen Übertragungswegen für die Daten festzulegen. Damit wird aber kein
technisches Problem gelöst und es wird auch nicht auf die technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht genommen, sondern es wird die
Anzeige der Werbeeinblendung und somit Bezahlung des Webseitenbetreibers
ermöglicht.


Beide Merkmale dienen somit dem geschäftlichen Zweck eine Manipulation zu
erkennen und diese zu umgehen um die Auslieferung der Werbung zu ermöglichen und damit die Bezahlung des Webseitenbetreibers sicher zu stellen. Diese

                                        -9-



allgemeine Zielsetzung führt aber gerade nicht zur Überwindung des Ausschlusstatbestands.


2.3   Die Argumentation der Anmelderin konnte zu keiner anderen Beurteilung
führen.


Die Anmelderin stellt dar, die Leistung der vorliegenden Erfindung bestehe nicht in
der Lösung eines geschäftlichen Problems, sondern eines technischen Problems,
nämlich in der Umgehung eines auf einem Rechner bzw. in einem Internetbrowser
installierten Werbeblockers. Derartige Umgehungsmöglichkeiten von Werbeblockern seien als technische Komponenten eines Computersystems dem Patentschutz nach gängiger Rechtsprechung zugänglich.
Die vorliegende Erfindung falle in die Kategorie (3) der BGH-Entscheidung „Webseitenanzeige“, da sie so ausgestaltet sei, dass sie erkenne, ob ein Werbeblocker
auf einer Datenverarbeitungsanlage installiert sei oder nicht. Folglich nehme die
vorliegende Erfindung auf die technischen Gegebenheiten einer Datenverarbeitungsanlage Rücksicht, da sie auf die rein technische Fragestellung, wie die technische Filterfunktion eines Werbeblockers ausgehebelt werden könne, abziele. Ein
Webserver hätte keine Möglichkeit zu erkennen, ob auf einem Client ein Werbeblocker eingerichtet sei, oder nicht, da die Blockierung von Werbung vom Client
und nicht vom Server durchgeführt würde. Zur Erkennung dieser Manipulation
stelle die erfindungsgemäße Lehre insofern eine Art „Messvorrichtung“ dar, die es
dem Server ermögliche, zu erkennen, ob auf einer Datenverarbeitungsanlage ein
Werbeblocker eingerichtet sei oder nicht. Hierzu sehe die erfindungsgemäße Lösung insbesondere vor, auf dem Webserver eine „Prüfvariable“ ad_id zu konfigurieren, sowie eine spezielle „Prüfdatei“ auf einem Datenspeicher abzulegen. Der
Server würde den Client instruieren, diese Prüfdatei abzurufen und aufgrund des
erfolgreichen bzw. nicht erfolgreichen Abrufens erkennen bzw. „messen“, ob ein
Werbeblocker im Client aktiv sei, oder nicht.

                                      - 10 -



Dieser Ausführung kann nicht gefolgt werden. Denn es findet keine Messung im
Sinne der Ermittlung einer quantitativen Aussage über eine physikalische Größe
statt. Es findet auch keine Erfassung z. B. von technischen Umweltparametern
durch eine geeignete Messeinrichtung statt. Vielmehr erfolgt eine Übertragung von
zusätzlichen Daten (Prüfdatei) gemeinsam mit den Daten der anzuzeigenden
Webseite von dem Webserver zu dem Webclient beim Aufruf einer Webseite.
Diese zusätzlichen Daten werden von dem Webclient verarbeitet und wieder an
den Webserver übermittelt. Der Webserver erkennt anhand der nunmehr empfangenen Daten (bspw. einer Prüfvariablen), ob ein Werbeblocker aktiv ist oder nicht.
Diese Vorgehensweise bei der Überprüfung auf einen aktiven Werbeblocker
basiert jedoch auf der Abfrage eines Parameters innerhalb der Software und führt
somit nicht zur Überwindung des Ausschlusstatbestandes (s. oben 2.2).
Die geltend gemachte Verlagerung der Abfrage, welche vom Webserver aus erfolgen soll, betrifft die äußerlich organisatorische Verlagerung von Aufgaben der
Datenverarbeitung zwischen mehreren Netzwerkkomponenten. Darin ist jedoch
nur eine Maßnahme der Datenverarbeitung und nicht die Lösung eines konkreten
technischen Problems mit technischen Mitteln zu sehen (vgl. BGH a. a. O. – Webseitenanzeige).


Die Anmelderin verweist darüber hinaus auf den ersten Leitsatz der BGH-Entscheidung „Dynamische Dokumentengenerierung“. Gemäß dieser Entscheidung
ist das Zusammenwirken der Elemente eines Datenverarbeitungssystems stets
technischer Natur. Deshalb stelle auch das hier vorliegende Zusammenwirken
eines Clients und eines Servers ein technisches Problem dar. Insbesondere wäre
analog zu der genannten Entscheidung die Gesamtarchitektur des Datenverarbeitungssystems aus Sicht des Systemdesigners zu betrachten und damit wären
die unterschiedlichen Eigenschaften und die Leistungsfähigkeit von Hard- und
Softwarekomponenten zu berücksichtigen.

                                        - 11 -



Der Verweis der Anmelderin auf den angegebenen ersten Leitsatz greift zu kurz,
denn dieser betrifft die grundsätzliche Technizität gemäß § 1 Abs. 1 PatG, welche
im vorliegenden Fall nicht bestritten wird.
Die weiter geltend gemachte Analogie der vorliegenden Anmeldung zum Gegenstand der zitierten Entscheidung trifft jedoch nicht zu.
Der zitierten Entscheidung lag das Problem zugrunde, ein Verfahren bereitzustellen, das es ermöglicht, auch auf Leitrechnern mit beschränkten Ressourcen ein
vom Client angefordertes strukturiertes Dokument dynamisch zu generieren. Zur
Lösung des technischen Problems (Leitrechner mit beschränkten Ressourcen)
werden die Anweisungen der Dienstnehmer durch ein auf dem Leitrechner vorhandenes Schnittstellenmodul extrahiert und auf einen korrespondierenden
– beschränkten – Befehlssatz abgebildet. Dies bedeutet, dass der Ablauf des Verfahrens der zitierten Entscheidung explizit auf die Eigenschaften des Systems
ausgerichtet ist und auf diese Rücksicht nimmt.
Im Gegensatz dazu erfolgt in dem Verfahren der vorliegenden Anmeldung die
Übertragung und Auswertung von Daten unabhängig von der verwendeten Hardware und auch unabhängig davon ob die Software (der Werbeblocker) auf dem
Webclient installiert ist. Das beanspruchte Verfahren überprüft somit weder die
Leistungsfähigkeit der Hardware noch werden die Eigenschaften der Software
ermittelt. Die Prüfung in dem beanspruchten Verfahren dient lediglich der Feststellung ob eine Software (ein Werbeblocker) aktiv ist oder nicht.


Sonach ist, im Gegensatz zur Ansicht der Anmelderin, der anzusetzende Fachmann im vorliegenden Fall ein Programmierer und nicht der Systemdesigner, da
die Aufgabe die Umsetzung von Vorgaben in ein Programm und nicht die Berücksichtigung besonderer technischer Eigenschaften, wie z. B. der begrenzten Leistungsfähigkeit eines Leitrechners (vgl. oben 2.2) erfordert.




3.     Mit dem Anspruch 1 fallen auch die übrigen Ansprüche, da über einen Antrag nur einheitlich entschieden werden kann.

                                            - 12 -



4.      Für eine Rückzahlung der Beschwerdegebühr gemäß § 80 Abs. 3 PatG
sieht der Senat keinen Anlass. Eine Rückzahlung der Beschwerdegebühr ist anzuordnen, wenn dies der Billigkeit entspricht. Dies ist dann der Fall, wenn die
Beschwerde bei sachgemäßer Behandlung durch das Patentamt vermeidbar
gewesen wäre, wobei alle Umstände des Falls zu berücksichtigen sind, insbesondere das Verhalten der Beteiligten und die Ordnungsmäßigkeit und Angemessenheit der Sachbehandlung durch das Patentamt. Ein Begründungsmangel oder eine
fehlende Begründung des angefochtenen Beschlusses, welche die Rückzahlung
rechtfertigen könnten, ist aber nicht erkennbar. Vielmehr hat die Prüfungsstelle
den angefochtenen Beschluss hinreichend mit Gründen versehen. Im vorliegenden Fall stellte die Prüfungsstelle dar, dass und warum das Verfahren des
Anspruchs 1 keine Anweisungen enthalte, die der Lösung eines technischen Problems mit technischen Mitteln dienten.
Die Angabe eines konkreten Standes der Technik ist entgegen der Ansicht der
Anmelderin nicht erforderlich, wenn die Zurückweisung aus anderen Gründen als
einem Vergleich des Anspruchsgegenstandes mit dem Stand der Technik erfolgt.
Die Prüfungsstelle hat demnach keine fehlerhafte Sachbehandlung vorgenommen,
die eine Rückzahlung der Beschwerdegebühr rechtfertigen würde.




Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
        Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,

                                          - 13 -



   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
       sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
       zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                Baumgardt               Hoffmann                     Akintche




                                                                                        Fa
