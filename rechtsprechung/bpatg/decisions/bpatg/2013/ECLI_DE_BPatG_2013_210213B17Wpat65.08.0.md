---
ecli: "ECLI:DE:BPatG:2013:210213B17Wpat65.08.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 65/08"
decided: "2013-02-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=10&nr=24813&anz=1167&pos=153&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-02-21_17_W-pat_65_08_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 65/08 vom 2013-02-21

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 65/08                                                    Verkündet am
_______________                                                     21. Februar 2013
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2007 002 533.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 21. Februar 2013 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                         I.


Die vorliegende Patentanmeldung ist am 17. Januar 2007 beim Deutschen Patentund Markenamt eingereicht worden. Die Bezeichnung lautet nunmehr:


  "Vorrichtung zur Bestimmung von Kenngrößen für das Benutzerverhalten von
                           Benutzern eines Netzwerks".


Die Prüfungsstelle für Klasse G06Q hat mit Beschluss vom 10. April 2008 die
Anmeldung zurückgewiesen, da der Gegenstand des (damals geltenden) Patentanspruchs 1 nicht auf erfinderischer Tätigkeit beruhe.


Gegen den Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        Patentansprüche 1 bis 9 und Beschreibung Seiten 1, 1a, 2, 2a,
        jeweils vom 18. Februar 2013 (dort bezeichnet als "Hilfsantrag 2"),
        Beschreibung Seiten 3 bis 15 und 6 Blatt Zeichnungen mit 11 Figuren, jeweils vom Anmeldetag.

                                       -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind keine
Druckschriften genannt worden. Der Senat hat mit Ladungszusatz die Druckschriften


D1: US 2004/0243568 A1
D2: US 6 286 046 B1
D3: US 2005/0125531 A1


in das Verfahren eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da die Vorrichtung des Patentanspruchs 1
nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1
PatG).


1. Die Patentanmeldung betrifft eine Vorrichtung zur Bestimmung von Kenngrößen
für das Benutzerverhalten von Benutzern eines Netzwerks.


Gemäß der jeweiligen S. 2 Abs. 1 der geltenden Unterlagen soll der Anmeldung
die Aufgabe zugrunde liegen, eine Vorrichtung bereit zu stellen, mittels derer eine
exakte Analyse des Benutzerverhaltens von Benutzern dieses Netzwerks ermöglicht wird.

                                            -4-



Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft
eine


       a) Vorrichtung zur Bestimmung von Kenngrößen für das Benutzerverhalten von Benutzern eines Netzwerks, mit
       b) einer Speichereinheit (10), in welcher ein Logfile abgespeichert ist,
         welcher eine Folge von Anfragen (3) eines Kundenrechners an einen
         Server und Antworten (5), die vom Server an den Kundenrechner
         ausgegeben werden, enthält, wobei
       c) die einzelnen Anfragen (3) und Antworten (5) jeweils mit einem
         Zeitstempel und einer Session-ID abgespeichert sind,
       d) mit einer Analyseeinheit (11), in welche der Logfile von der
         Speichereinheit (10) einlesbar und
       d1) in welcher der Logfile nach durch die Session-ID gekennzeichneten
           Sessions sortierbar ist, wobei
       e) die Analyseeinheit (11) einen Logfilefilter (14) und wenigstens eine
         Bewertungseinheit (16) aufweist, wobei
       f) im Logfilefilter (14) Kriterien in Form von Kategorien, welchen vorgegebenen Informationen im Logfile zugeordnet sind, definiert oder
         berechnet und in den Logfile eingefügt werden, wobei
       g) in der wenigstens einen Bewertungseinheit (16)
       g1) für die einzelnen Sessions, nach welchen die Anfragen (3) und
           Antworten (5) des Logfiles sortiert sind, Subprozesse gebildet werden, welche parallel ausgewertet werden,
       g2) in dem durch Bildung von Mengenbedingungen für Kriterien einzelner Sessions Areas bildende Zahlenfolgen zur Bildung von
           Kenngrößen für das Benutzerverhalten des Benutzers der jeweiligen Kundenrechner generiert werden, wobei
       h) eine Area als Zahlengröße die Anzahl der Sessions für welche
         wenigstens ein Kriterium erfüllt ist, enthält.

                                       -5-



Die Anmeldung geht aus von einem Netzwerk (z. B. dem Internet), mit (mindestens) einem Kundenrechner (Client) und einem Server. Ein Kunde kommuniziert interaktiv mit dem Server über Fragen und Antworten; z. B. sucht der Kunde
bestimmte Waren im Angebot eines Online-Händlers und kann diese bestellen.
Das Verhalten der Kunden soll analysiert werden, um z. B. Informationen über das
Kaufverhalten der Kunden zu gewinnen sowie darüber, ob das angebotene Warenspektrum bedarfsgerecht ist (Beschreibung S. 1 Abs. 3; Merkmal a)). Hierfür
werden Anfragen des Kundenrechners an den Server und die zugehörigen
Antworten vom Server, jeweils mit Zeitstempel und Session-ID, in einem Logfile
gespeichert (Merkmale b), c)). Diese Daten werden in eine Analyseeinheit übertragen und dort ausgewertet (Merkmal d)), wobei in einem Logfilefilter Kriterien
(Kategorien) zur Strukturierung der Informationen in den Logfile eingefügt werden
(Merkmal f) i. V. m. e)); wenn z. B. eine Kundenanfrage den Suchbegriff
"gestreifter Anzug" enthält, kann dieser das Kriterium "Herrenmode" zugeordnet
werden (ursprüngliche S. 4 Abs. 3 bis 5, S. 8 Z. 17 bis S. 9 Z. 2; Fig. 2). In einer
Bewertungseinheit (Merkmal g) i. V. m. e)) wird der nach Sessions sortierte Logfile
(Merkmal d1)) in den einzelnen Sessions zugeordneten Subprozessen parallel
ausgewertet (Merkmal g1)). Hierbei werden anhand von Mengenbedingungen für
Kriterien einzelner Sessions (z. B. "In welcher Session ist das Kriterium crit 1
erfüllt?", vgl. S. 11 Satz 1) Zahlenfolgen enthaltende "Areas" gebildet, wobei jede
Area die Anzahl der Sessions enthält, für die wenigstens ein Kriterium erfüllt ist
(Merkmale g2), h)), z. B. die Anzahl der Sessions, in denen nach Herrenmode
gesucht wurde. In einer Area können weitere Zahlen enthalten sein, z. B. die
Zeitdauer der ein Kriterium erfüllenden Sessions (Fig. 5; Unteranspruch 2). Die
Areas enthalten somit Kenngrößen für das Verhalten des Benutzers der jeweiligen
Kundenrechner.


Einige Anspruchsmerkmale bedürfen der Erläuterung:


Durch die Sortierung des Logfiles nach der Session-ID gemäß Merkmal d1)
werden die zur gleichen Session-ID gehörenden Logfileeinträge (die ursprünglich

                                         -6-



an unterschiedlichen Stellen im Logfile stehen können, vgl. Fig. 2) zusammengefasst, so dass danach eine Auswertung nach der Session-ID erfolgen kann.


Wie die Anmelderin in der mündlichen Verhandlung eingeräumt hat, ist in Merkmal f) die Bezeichnung "Logfilefilter" missverständlich, ebenso die Angabe "definiert oder berechnet". Im Lichte des die Erfassung und Analyse von Internetnutzungsdaten betreffenden Fachwissens ist Merkmal f) so zu interpretieren, dass
in einem mit "Logfile-filter" bezeichneten Modul den im Logfile gespeicherten
Anfragen und Antworten Kategorien zugeordnet und in den Logfile eingefügt werden, wobei auf eine vorher gespeicherte Relation zwischen möglichen Anfragen
und Antworten einerseits und Kategorien andererseits zugegriffen wird. Eine
automatische Erzeugung von vorher nicht bekannten Kategorien durch die Vorrichtung ist nicht möglich, auch wenn in den Anmeldeunterlagen der drittletzte
Absatz in S. 8 auf derartiges hindeuten könnte. Dieser Interpretation von Merkmal f) hat die Anmelderin nicht widersprochen.


2. Es kann dahin stehen, ob die Vorrichtung des geltenden Patentanspruchs 1
neu ist, sie beruht zumindest nicht auf erfinderischer Tätigkeit.


2.1. Aus dem Stand der Technik war vor dem Anmeldetag der vorliegenden
Patentanmeldung folgendes bekannt:


D1 zeigt in Fig. 1 ein Netzwerk 106 mit Client 102 und Server 104. In der
Suchmaschine 140 des Servers werden vom Client eingegebene Suchanfragen
und Antworten in einem Logfile in einer entsprechenden Datenbank (log database
220) gespeichert, an eine Auswerteeinheit (log data mining tools 222) übertragen
und dort ausgewertet, vgl. Abstract sowie Fig. 1 mit Beschreibung. Durch die
Auswertung soll mit der Zeit die Performance der Suchmaschine verbessert und
an die Anforderungen des Benutzers angepasst werden, vgl. im Abstract den
vorle. und le. Satz sowie Abs. [0026] und [0061] in Verbindung mit Fig. 2.

                                        -7-



D2 zeigt ein ähnliches System, wobei das Modul zur Speicherung und Auswertung
von Suchanfragen und Antworten (monitor 40) zwischen dem Server und dem
Client angeordnet ist, vgl. Fig. 2 und Sp. 3 Z. 48 bis 61. Die Auswertung einer
Beispielsession (sample session) erfolgt nach dem Abschluss dieser Session,
wobei mit Hilfe des gespeicherten Logfiles die Session simuliert wird.


D3 betrifft ein System zur Sammlung, Analyse und Ergebniswiedergabe des
Benutzerverhaltens auf einer Vielzahl von Webservern. Fig. 1 zeigt ein System mit
mehreren Webservern (101 bis 106), auf denen Benutzungsdaten von Systemnutzern (system users) in Form von Logfiles gespeichert werden, die u. a. Benutzeranfragen (system-user requests, content requested), einen Antwortcode
(return code from the request), Zeitstempel und eine in einem Cookie gespeicherte
Benutzeridentifikation (USERID) beinhalten, vgl. Abs. [0048] bis [0050]. Zu vorbestimmten Zeiten werden die gefilterten Logfiles über Sammelserver (collection
server 107, 108) an eine Analyseeinheit (analysis server 109) übertragen und dort
analysiert, vgl. Fig. 4 und Abs. [0053] bis [0056]. Berichtenutzer (report users)
können verschiedene Analyseergebnisse abfragen, vgl. Fig. 7 i. V. m. Abs. [0076],
unter anderem hinsichtlich der genutzten Inhalte, vgl. auch Fig. 11.


2.2. Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass die
mit dem geltenden Anspruch 1 beanspruchte Vorrichtung für den Fachmann, als
den der Senat einen in der Erfassung und Analyse von Internetnutzungsdaten
erfahrenen Informatiker im Team mit einem Kaufmann ansieht, nahegelegen hat.


Bei der Beurteilung der erfinderischen Tätigkeit sind nur solche Merkmale zu
berücksichtigen, welche die Lösung eines technischen Problems mit technischen
Mitteln bestimmen oder beeinflussen; vgl. BGH in GRUR 2011, 125 - "Wiedergabe
topografischer Informationen".


Wie die oben unter 2.1 erläuterten Druckschriften D1, D2 und D3 beispielhaft
zeigen, war es aus dem Stand der Technik bekannt, in einem System, in welchem

                                       -8-



Kundenrechner und Server über ein Netzwerk miteinander kommunizieren, die
diese Kommunikation betreffenden Daten in einem Logfile zu speichern und im
Hinblick auf das Benutzer-verhalten in einer Analyseeinheit auszuwerten, in
welche der Logfile einlesbar ist – Merkmale a), b), d). Dass aufgrund der innerhalb
kurzer Zeit anfallenden, großen Datenmengen in den Logfiles die für eine Logfile-Auswertung heranzuziehende Datenverarbeitungsanlage eine schnelle Auswertung erlauben muss (vgl. etwa D3 Abs. [0004]), war dem Fachmann vor dem
Anmeldetag der vorliegenden Anmeldung geläufig.


Ausgehend von dem oben geschilderten fachbekannten Rahmen liegt die Leistung
der vorliegenden Anmeldung darin, durch Auswertung eines Logfiles Kenngrößen
für das Benutzerverhalten nach vorgegebenen Kategorien (welchen die Benutzeranfragen und -antworten zugeordnet werden können) zu erzeugen in Form von
nach Kategorien aufgeschlüsselten Anzahlen (und evtl. Zeitdauern, vgl. den Unteranspruch 2) von Sessions mit Benutzeranfragen.


Nach welchen Kriterien die Auswertung erfolgen soll und welche Art von Ergebnis
sie liefern soll (Auswertung nach vorbestimmten, möglichen Benutzeranfragen
zugeordneten Kategorien, wobei Informationen hinsichtlich der Anzahl der
Sessions und evtl. deren Zeitdauer erzeugt werden sollen, vgl. die Merkmale g2)
und h)), ist als eine rein geschäftliche Vorgabe anzusehen, die dem Informatiker
oder Programmierer vom Kaufmann vorgegeben wird, und der keine technischen
Überlegungen zugrunde liegen; vgl. das in der BGH-Entscheidung "Wiedergabe
topografischer Informationen" (a. a. O.) für eine Vorgabe zur Wiedergabe von
Informationen Ausgeführte, wobei die bloße Wiedergabe von Informationen
patentrechtlich nicht anders zu behandeln ist als andere Anweisungen, welche
keine Lösung einer technischen Problemstellung mit technischen Mitteln zum
Gegenstand haben, wie z. B. rein geschäftliche Tätigkeiten, vgl. BGH in
GRUR 2005, 141 - "Anbieten interaktiver Hilfe". Diese Beurteilung gilt auch für die
Einteilung der Benutzeranfragen in (im Anspruch nicht näher definierte und in ihrer
Anzahl nicht beschränkte) Kategorien. Definition und Anzahl der Kategorien leiten

                                         -9-



sich daraus ab, für welches Benutzerverhalten sich der Kaufmann besonders
interessiert (beispielsweise wie oft sich Kunden nach Herrenmode erkundigen);
die Lösung eines technischen Problems wird dadurch nicht beeinflusst. Auch die
Art der im Logfile zu speichernden Daten (Zeitstempel und Session-ID, Merkmal c)) ergibt sich aus der geschäftlichen Vorgabe und trägt nicht zur Lösung
eines technischen Problems bei.


Die geschäftliche Vorgabe wird dadurch umgesetzt, dass in der Analyseeinheit
bzw. in entsprechenden Untereinheiten (Logfilefilter, Bewertungseinheit) die
Schritte Sortieren, Zuordnen und Einfügen von Kategorien sowie paralleles statistisches Auswerten für die einzelnen Sessions durchgeführt werden.


Auch diese Anweisungen tragen nicht zur Lösung eines technischen Problems mit
technischen Mitteln bei. Sie sind allein dem Gebiet der Datenverarbeitung
zuzuordnen und betreffen die Bereitstellung und Auswertung von Informationen.
Die in der Analyseeinheit auszuführenden Schritte Sortieren, Zuordnen und Einfügen von Kategorien zum Logfile, paralleles statistisches Auswerten für die
einzelnen Sessions zur Bildung von Zahlenfolgen für die Kategorien bzw. Kriterien
gehen nicht über die Sammlung, Speicherung und Verarbeitung von Daten hinaus,
so dass in ihnen nur Maßnahmen der Datenverarbeitung zu sehen sind und nicht
die Lösung eines konkreten technischen Problems (BGH in GRUR 2011,
610 - Webseitenanzeige; BGH in GRUR 2009, 479 - Steuerungseinrichtung für
Untersuchungsmodalitäten). Das Sortieren von Daten (Merkmal d1)) ist eine reine
Maßnahme der Datenorganisation. Auch das Zuordnen und Einfügen von Kategorien in den Logfile (Merkmal f)) dient der Organisation der Daten, nämlich deren
Einteilung in die geschäftlich vorgegebenen Kategorien, und hat keinen technischen Hintergrund. Insbesondere ist auch die parallel durchzuführende Auswertung der einzelnen Sessions (Merkmal g1) in Verbindung mit g2) und h)) als
reine Maß-nahme der Datenverarbeitung zu bewerten. Die Parallelität mag zwar
durchaus dazu beitragen, dass die Auswertung relativ schnell erfolgen kann. Dies
beruht   jedoch   ausschließlich   auf   dem   verwendeten   Datenverarbeitungs-

                                       - 10 -



algorithmus und der darin vorgenommenen Organisation der Daten; eine
technische Ausgestaltung, etwa in Form einer speziell verwendeten Hardware ist
in der gesamten Anmeldung nicht zu erkennen; vgl. auch den Senatsbeschluss
17 W (pat) 11/08. Die zur Auswertung eingesetzte Datenverarbeitungsanlage
arbeitet gemäß ihrer Bestimmung; sie wird weder verändert, noch ist der
Algorithmus an einen speziellen Aufbau der Datenverarbeitungsanlage angepasst.
Auch die vorrichtungsmäßige Einkleidung der beanspruchten Lehre (mit Analyseeinheit, Bewertungseinheit und Logfilefilter; Merkmale e), g)) kann an dieser
Beurteilung nichts ändern, zumal eine technische Ausgestaltung der einzelnen
Module (etwa in Form spezieller elektronischer Schaltungen) oder eine sonstige
spezielle Anpassung an technische Gegebenheiten nicht gelehrt wird; vgl. auch
BGH in GRUR 2010, 613 - "Dynamische Dokumentengenerierung".


Somit tragen zumindest die Merkmale c), d1), e), f), g), g1), g2) und h) nicht zur
Lösung eines technischen Problems mit technischen Mitteln bei und sind bei der
Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen.
Wie oben erläutert, war eine Vorrichtung mit den übrigen Merkmalen des Anspruchs 1 fachbekannt.


Damit beruht die Vorrichtung gemäß Anspruch 1 zumindest nicht auf erfinderischer Tätigkeit.


Unabhängig davon wäre der Anspruch 1 im Ergebnis selbst dann nicht anders zu
beurteilen, wenn man davon ausginge, dass sowohl die parallele Verarbeitung als
auch die Sortierung und die Zuordnung und Einfügung von Kategorien in den
Logfile zu einer technischen Problemlösung beitragen und zu berücksichtigen
sind. Ausgehend von einer fachbekannten Vorrichtung zur Logfileauswertung (vgl.
etwa D1) und der oben geschilderten geschäftlichen Vorgabe waren diese
Merkmale nämlich für den Fachmann naheliegend. Da gemäß der geschäftlichen
Vorgabe jeweils die Anzahl der Sessions (nicht die Anzahl der Benutzer oder die
Anzahl der Klicks) für jede Kategorie berechnet werden soll, drängte es sich

                                        - 11 -



geradezu auf, vor der weiteren Auswertung die zu einer Session gehörigen
einzelnen Logfileeinträge zusammenzufassen; hierfür bot sich eine einfache
Sortierung nach Session-ID an. Zudem war es dem Fachmann aus seinem
Fachwissen geläufig, dass Benutzereingaben in natürlicher Sprache abgefasst
werden können, wobei Anfragen und Antworten im Logfile gespeichert werden
(vgl. etwa D1 Abs. [0025] und [0026]). In diesem Fall sind naturgemäß den
Anfragen noch keine Kategorien zugeordnet; sie müssen daher bei der
Auswertung der Logfiles hinzugefügt werden. In einem geeigneten Programmodul
(Logfilefilter) den Informationen im Logfile solche Kategorien zuzuordnen und
diese für die weitere Auswertung im Logfile zu speichern, lag damit im Griffbereich
des Fachmanns. Diesem war zudem bekannt, dass die Auswertung von Logfiles
aufgrund der großen Datenmengen zeitkritisch ist und daher zeitlich möglichst
optimiert werden muss, vgl. etwa D3 Abs. [0004]. Die schnelle, parallele Verarbeitung von Verfahrensschritten gehörte zu seinem Standard-Handwerkszeug.
Damit lag es für ihn nahe, Programmteile, die in immer gleicher Weise wiederholt
werden, parallel auszuführen; hierfür bot sich eine parallele Verarbeitung nach den
einzelnen, jeweils in gleicher Weise auszuwertenden Sessions an.


3. Der geltende Anspruch 1 nicht demnach gewährbar.
Auch die abhängigen Patentansprüche 2 bis 9 sind nicht gewährbar, da über
einen Antrag nur einheitlich entschieden werden kann, vgl. BGH in GRUR 1997,
120 "Elektrisches Speicherheizgerät".


Dr. Morawek               Eder               Dr. Thum-Rung              Dr. Forkel




                                                                               Me
