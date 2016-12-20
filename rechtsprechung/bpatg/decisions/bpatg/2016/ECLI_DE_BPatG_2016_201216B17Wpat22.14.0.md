---
ecli: "ECLI:DE:BPatG:2016:201216B17Wpat22.14.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 22/14"
decided: "2016-12-20"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2016&Sort=1&Seite=59&nr=28828&anz=906&pos=896&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2016-12-20_17_W-pat_22_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 17 W (pat) 22/14 vom 2016-12-20

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 22/14                                                      Verkündet am
_______________                                                     20. Dezember 2016
    (Aktenzeichen)                                                         …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2010 048 533.0


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 20. Dezember 2016 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                      -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                   Gründe


                                       I.


Die vorliegende Patentanmeldung wurde am 14. Oktober 2010 in englischer Sprache beim Deutschen Patent- und Markenamt eingereicht. Sie trägt in der deutschen Übersetzung die Bezeichnung


            „Verfahren zum Synchronisieren mehrerer Datenbanken“.


Die Anmeldung wurde mit Beschluss vom 20. März 2014 von der Prüfungsstelle
für Klasse G06F des Deutschen Patent- und Markenamtes zurückgewiesen. Zur
Begründung führt die Prüfungsstelle sinngemäß aus, dass der angestrebte Erfolg
der zum Patentschutz angemeldeten Lehre nicht im gesamten beanspruchten
Bereich erzielt werden könne. Sie nimmt dabei Bezug auf § 34 Abs. 4 PatG.


Gegen diesen Beschluss ist die Beschwerde des Anmelders gerichtet.


Er hat mit Eingabe vom 22. April 2014 sinngemäß beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 4 vom 13. Februar 2014;
       Beschreibung Seiten 4, 4a, 5, 5a und 6 vom 23. Oktober 2012,

                                      -3-



        Seiten 1 bis 3 und 7 bis 9 vom 10. Januar 2011 und
        2 Blatt Zeichnungen mit Figuren 1 bis 6 vom 10. Januar 2011.


Zuletzt hat der Anmelder (siehe Eingabe vom 15. Dezember 2016) eine Entscheidung nach Aktenlage beantragt.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind die Druckschriften


D1: Hao SHUAI, Beng Lim HOCK: “Data Synchronization in Distributed and
Constrained Mobile Sensor Networks”, 2007, DOI: 10.1007/978-3-540-73549-
6_66;


D2: FRAGOULI, LE BOUDEC; WIDMER: “Network Coding: An Instant
Primer”, 2005, <Im Internet http://en.scientificcommons.org/27996263>;


D3: Sachin KATTI, Hariharan RAHUL, Wenjun HU [et.al.]: XORs in the Air:
Practical    Wireless     Network      Coding,     SIGCOMM        2006,   DOI:
10.1145/1159913.1159942;


D4: TANG, DONNER, CHAVES, MUHAMMAD: Performance of Database
Synchronization Algorithms via Satellite, Cagliari, 13.–15.09.2010, DOI:
10.1109/ASMS-SPSC.2010.5586921


und


D5: TRACHTENBERG, Ari; STAROBINSKI, David; AGARWAL, Sachin: Fast
PDA Synchronization Using Characteristic Polynomial Interpolation. In:
INFOCOM 2002. Twenty-First Annual Joint Conference of the IEEE Computer

                                          -4-



and Communications Societies. Proceedings. IEEE. IEEE, 2002. S. 1510–
1519. doi: 10.1109/INFCOM.2002.1019402


genannt worden. Der Senat hat zusätzlich die Druckschrift


D6: TANG, C.; DONNER, A.; CHAVES, J. M.; MUHAMMAD, M.: Performance
of Database Synchronization Algorithms via Satellite, 2010 5th Advanced
Satellite Multimedia Systems Conference and the 11th Signal Processing for
Space Communications Workshop, 13–15. Sept 2010 (Date Added to IEEE
Xplore: 27. Sept 2010)


ermittelt. Bei der Druckschrift D6, die inhaltsgleich mit der bereits aus dem Prüfungsverfahren bekannten Druckschrift D4 ist, handelt es sich um diejenige Version des Fachartikels, wie sie im September 2010 (in IEEExplore) online gestellt
worden ist.


Der geltende Patentanspruch 1, hier mit einer möglichen Gliederung versehen,
lautet (mit redaktionellen Änderungen):


(a´)   Verfahren zum Synchronisieren von mindestens drei Datenbanken, wobei
       die Datenbanken Datensätze gleicher Datenstruktur enthalten, welche in
       ihrer Summe den Datenbestand der jeweiligen Datenbank bilden, mit den
       Schritten:


(a)    Auswählen eines der mindestens drei Datenbank-Hosts (A, B, X) als Masterknoten (X), wobei die übrigen Datenbank-Hosts (A, B,) als Slave-Hosts
       definiert werden,


(b)    Vergleichen der des auf dem Masterknoten (X) vorhandenen Datenbestands mit dem Datenbestand jedes Slave-Hosts (A, B),

                                       -5-



(c)   Übermitteln von Datensätzen, die auf dem jeweiligen Slave-Host (A, B) vorhanden sind, von jedem Slave-Host (A, B) zu dem Masterknoten (X), wobei
      beim Übertragen der Datensätze von dem jeweiligen Slave-Host (A, B) zum
      Masterknoten (X) nur diejenigen Datensätze übertragen werden, die auf
      dem Masterknoten (X) nicht vorhanden sind,


(d)   Übermitteln von Datensätzen, die einem oder mehreren Slave-Hosts (A, B)
      fehlen und die auf dem Masterknoten (X) vorhanden sind, von dem Masterknoten (X) zu den Slave-Hosts (A, B), denen die Datensätze fehlen,


(e)   wobei diese Datensätze unter Einsatz eines Netzwerk-Coding-Verfahrens
      übertragen werden, wobei


(f)   die auf dem Masterknoten (X) fehlenden Datensätze von jedem Slave-Host (A, B) nacheinander an den Masterknoten (X) übertragen werden,
      wobei


(g)   Datensätze, die ein vorheriger Slave-Host (A, B) bereits übertragen hat,
      nicht nochmals übertragen werden, und wobei


(h)   das Übermitteln der fehlenden Datensätze vom Masterknoten (X) zu den
      Slave-Hosts (A, B) gemäß Schritt c) d) als Broadcast zu sämtlichen Slave-Hosts durchgeführt wird, wobei


(i)   das Vergleichen des auf dem Masterknoten (X) vorhandenen Datenbestands mit dem Datenbestand jedes Slave-Hosts (A, B) durch das CPI-Sync-Verfahren stattfindet.


Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.

                                       -6-



                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da das Verfahren des Patentanspruchs 1 nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Der Gegenstand der Anmeldung betrifft ein Verfahren zum Synchronisieren
mehrerer Datenbanken.


Ausweislich der Patentanmeldung sei bekannt, dass im Rahmen von sogenannten
Distributed Databases (DDB) Daten auf mehrere Datenbank-Hosts verteilt werden
könnten, die logisch miteinander verbunden seien. Physikalisch könnten sich
diese Datenbank-Hosts an verschiedenen Stellen in einem Computernetzwerk befinden. Um die Zuverlässigkeit der Daten an allen Punkten des Netzwerks zu gewährleisten, müssten die Datenbestände, die sich an den einzelnen Datenbank-Hosts im Netzwerk befänden, synchronisiert werden (Offenlegungsschrift, [0002]).
Dabei handle es sich bei der Datensynchronisation um einen Prozess, um ausgehend von einer Datenquelle zu einer Zieldatenbank und umgekehrt einen konsistenten Datenbestand zu erreichen. Dieser Prozess könne eine kontinuierliche Harmonisierung der Daten über die Zeit involvieren. Für eine Datenbanksynchronisierung stehe eine Reihe von Algorithmen zur Verfügung, wie beispielsweise Slow-Sync und CPI-Sync. Andere Mechanismen seien auf spezielle Datenbanksysteme
ausgerichtet, wie beispielsweise Maatkit für MySQL-Datenbanken. Die genannten
Algorithmen arbeiteten im Rahmen einer Punkt-zu-Punkt-Verbindung zwischen
den Datenbank-Hosts. Ein derartiges Szenario umfasse zwei Hosts, wobei jeder
Host eine Datenbank aufweise, die unabhängig von der anderen Datenbank wachse. Um Datenkonsistenz zu erreichen, müssten beide Datenbestände zu einem
bestimmten Zeitpunkt zusammengeführt werden und auf beiden Hosts bereitgestellt werden. Um in einer Punkt-zu-Punkt-Verbindung beide Hosts miteinander zu
synchronisieren, würden bei Verwendung des Slow-Sync-Verfahrens die gesamten Daten von jedem Host auf die Gegenseite übermittelt. Danach finde in jedem

                                      -7-



Host ein Zusammenführen (Merging) der alten mit den neuen Datensätzen statt,
wobei die neuen Informationen beibehalten würden und die alten Informationen
geupdated oder entfernt würden, wenn keine Veränderungen vorlägen. Nachteilig
an diesem Verfahren sei der große Overhead, der über das Übertragungsmedium
übermittelt werde (Offenlegungsschrift, [0003]–[0008]). Im Rahmen von CPI-Sync,
einem effizienteren Synchronisationsverfahren, würden zwei physikalisch getrennte Datensets mit einem Minimum an Kommunikation zwischen den Hosts
abgeglichen. Unter Verwendung der Characteristic-Polynomial-Interpolation werde
ein Algorithmus angewandt, bei dem ein Hashing, ein Faktorisieren und ein Interpolieren stattfinde, um die Unterschiede zwischen den Datensets der beiden Hosts
zu bestimmen. Anschließend würden nur diese Unterschiede übertragen, was zu
einer Reduzierung des Overheads gegenüber dem Slow-Sync-Verfahren führe
(Offenlegungsschrift, [0009] und [0010]). Wenn drei Datenbank-Hosts X, A und B
anstelle von nur zwei Hosts vorhanden seien, müssten bei Anwendung des CPI-Sync-Verfahrens drei aufeinanderfolgende Synchronisationsschritte durchgeführt
werden. In einem ersten Schritt finde eine Synchronisierung zwischen X und A
statt, in einem zweiten Schritt eine Synchronisierung zwischen X und B und in
einem dritten Schritt eine Synchronisierung zwischen A und B, so dass schließlich
das gesamte System synchronisiert sei (Offenlegungsschrift, [0012]). Zur Übertragung der Datenpakete müsse in Summe eine Mehrzahl von Übertragungsschritten
durchgeführt werden (Offenlegungsschrift, [0014]).


Laut Beschreibung soll der Anmeldung die Aufgabe zugrunde liegen, ein vereinfachtes Verfahren zum Synchronisieren von mindestens drei Datenbanken bereitzustellen (Offenlegungsschrift, [0015]). Der Senat sieht die der Anmeldung zugrundeliegende objektive Aufgabe darin, ein Verfahren anzugeben, mit dem die
Synchronisation von wenigstens drei Datenbank-Hosts in einem Netzwerk beschleunigt werden kann.

                                         -8-



Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zum Synchronisieren mehrerer Datenbanken zu verbessern, ist ein Systemprogrammierer anzusehen, welcher über eine mehrjährige Berufserfahrung in der Entwicklung und im
Betrieb verteilter Datenbankmanagementsysteme verfügt.


2.     Dem Verfahren des Patentanspruchs 1 mangelt es an der für die Patentfähigkeit erforderlichen erfinderischen Tätigkeit.


2.1    Zur Lehre des Patentanspruchs 1


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 ein Verfahren zum Synchronisieren von mindestens drei Datenbanken vor. Die in den
jeweiligen Datenbanken abgelegten Datensätze haben gleiche Datenstruktur. Der
Datenbestand einer Datenbank wird dabei durch die Gesamtheit der darin enthaltenen Datensätze gebildet (Merkmal (a´)).


Das beanspruchte Verfahren umfasst die folgenden Schritte: Zunächst wird einer
der mindestens drei Datenbank-Hosts als Masterknoten ausgewählt. Die übrigen
Datenbank-Hosts werden als Slave-Hosts festgelegt (Merkmal (a)).


Gemäß Merkmal (b) wird der Datenbestand des Masterknotens mit dem Datenbestand jedes Slave-Hosts verglichen.


Anschließend werden von jedem Slave-Host nur diejenigen Datensätze an den
Masterknoten übermittelt, die zwar auf dem jeweiligen Slave-Host, nicht aber auf
dem Masterknoten vorhanden sind (Merkmal (c)).


Danach werden diejenigen Datensätze, die einem oder mehreren Slave-Hosts
fehlen und die auf dem Masterknoten vorhanden sind, vom Masterknoten an die
betreffenden Slave-Hosts übertragen (Merkmal (d)).

                                        -9-



Diese Datenübertragung erfolgt unter Einsatz eines Network-Coding-Verfahrens
(Merkmal (e)). Laut Beschreibung können mit Hilfe der Network-Coding-Technik
einige Datenpakete bzw. Datensätze vor der Übertragung kombiniert werden, da
nach dem Senden der Daten von den Slave-Hosts zum Masterknoten dieser vollständige Kenntnis von den in jedem Slave-Host vorhandenen und verlangten
Informationen hat. Durch Network-Coding ist es möglich, die Anzahl notwendiger
Datenübertragungsschritte zu reduzieren (Offenlegungsschrift, [0018], [0019]).


Weiterhin werden die auf dem Masterknoten fehlenden Datensätze von jedem
Slave-Host nacheinander an den Masterknoten übertragen, wobei Datensätze, die
ein vorheriger Slave-Host bereits übertragen hat, nicht noch einmal übertragen
werden (Merkmale (f), (g)).


Laut Merkmal (h) sollen die Datensätze vom Masterknoten an sämtliche Slave-Hosts über einen Broadcast-Kanal übermittelt werden.


Merkmal (i) besagt, dass die auf dem Masterknoten vorhandenen Datensätze mit
den Datensätzen jedes Slave-Hosts unter Anwendung des CPI-Sync-Verfahrens
verglichen werden.


2.2   Zur Beurteilung der beanspruchten Lehre sind die Druckschriften D6 und
D3 von besonderer Bedeutung.


Die Druckschrift D6 untersucht die Tauglichkeit von Algorithmen unterschiedlicher
Synchronisations- und Replikationsstrategien in Hinblick auf eine Verwendung in
der Datenbanksynchronisation über Satellitenfunkverbindungen (Abstract). Im
Wesentlichen werden vier verschiedene Algorithmen beleuchtet: Slow Sync
(Seite 456, rechte Spalte, zweiter Absatz), Maatkit (Seite 456, rechte Spalte, dritter
Absatz), Basic-CPISync und Partitioned CPISync (Seiten 457, linke Spalte bis
Seite 458, linke Spalte).

                                       - 10 -



So führt die Druckschrift D6 den Fachmann zu einem Verfahren zum Synchronisieren von zwei Datenbanken. Von den hier vorgestellten Strategien zur Synchronisation und Replikation eignet sich insbesondere CPISync für eine Verwendung
über Satellitenfunkverbindungen (Abstract; Seite 461, linke Spalte). Obwohl die
Vor- und Nachteile der offenbarten Strategien vor allem am Beispiel zweier Datenbank-Hosts diskutiert werden, ist die Anwendung der aus der Druckschrift D6
bekannten Synchronisationsverfahren nicht bloß auf den Datenabgleich zwischen
zwei Datenbank-Hosts beschränkt. Die offenbarten Synchronisationsverfahren
können grundsätzlich ebenso für die Synchronisation von mehr als zwei Datenbank-Hosts verwendet werden, wenn z. B. Algorithmen zur Auflösung von Versionskonflikten berücksichtigt werden (Seite 458, rechte Spalte, zweiter Absatz).
Dass der geschilderte CPISync-Algorithmus, der u. a. auf der Bildung eines charakteristischen Polynoms beruht (Seite 457, linke Spalte), idealerweise auf den
beteiligten Datenbank-Hosts dieselben Datenstrukturen voraussetzt, las der Fachmann mit. Merkmal (a´) geht damit aus der Druckschrift D6 hervor.


Im beschriebenen CPISync-Verfahren wird einer der beiden Datenbank-Hosts
(Host A) als Masterknoten ausgewählt, auf dem der Hauptteil des Algorithmus
abgearbeitet wird. Der andere Knoten wird als Slave-Host definiert (Host B). Durch
CPISync werden diejenigen Datensätze ermittelt, die auf dem Masterknoten fehlen, jedoch auf dem Slave-Host vorhanden sind und umgekehrt. Jeder Host erhält
die ihm fehlenden Datensätze vom jeweils anderen Knoten (Seiten 457–458, Abschnitt „C. CPISync“ – teilweise Merkmale (a), (b), (c), (d) und (i)). Die Bestimmung von Masterknoten und Slave-Hosts, der Vergleich der Datenbestände zwischen den Hosts sowie die nachfolgende Übermittlung von Datensätzen am Beispiel einer Konfiguration von wenigstens drei Datenbanken gehen aber aus der
Druckschrift D6 konkret nicht hervor (restlicher Teil der Merkmale (a), (b), (c), (d)
und (i)).

                                       - 11 -



Die Druckschrift D3 beschäftigt sich in erster Linie mit dem drahtlosen Network-Coding. Der Fachartikel beschreibt COPE, eine neue Architektur für drahtlose vermaschte Netzwerke. Zusätzlich zur bloßen Weiterleitung von Datenpaketen, mischen Hosts die von verschiedenen Quellen empfangenen Datenpakete, um für
den anschließenden Übertragungsschritt den Inhalt an Information zu vergrößern.
Ein geeignetes Mischen bzw. Codieren von Datenpaketen erhöht hierbei den
Datendurchsatz im Netzwerk (Abstract). Die Druckschrift D3 führt den Fachmann
zu einer Anwendung des Network Codings in Drahtlosnetzwerken mit Broadcast,
bei dem codierte Datenpakete von einem mittleren Knoten (z. B. Seite 499, Fig. 2,
„Node B“), auf dem die Codierung der Datenpakete abläuft und der somit als
Masterknoten fungiert, zu einer Mehrzahl von benachbarten Hosts (z. B.
Seite 499, Fig. 2, Nodes A, C, D), den Slave-Hosts übertragen werden (Abstract;
Seiten 498–499, Abschnitt III. – „Cope Overview“; Fig. 2 inklusive Beschreibung;
Seite 502, rechte Spalte – Merkmale (e), (h)).


2.3   Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
der Gegenstand nach Patentanspruch 1 mit all seinen Merkmalen für den Fachmann nahegelegen hat.


Aufgrund des in der Druckschrift D6 gegebenen Hinweises, die dort offenbarten
Algorithmen zur paarweisen Synchronisation von Datenbank-Hosts auf ein Datenbanksystem mit einer Mehrzahl von Hosts ausdehnen zu wollen (Seite 461, linke
Spalte, zweiter Absatz), hatte der Fachmann Veranlassung, sich über geeignete
Netzwerk-Topologien und die hierauf basierenden Kommunikationsverbindungen
kundig zu machen oder aber entsprechenden Rat einzuholen. Hierbei konnte er
auf die Druckschrift D3 stoßen, die eine bewährte Netzwerktechnik zur Übertragung von Datenpaketen zwischen den Hosts eines Drahtlosnetzwerkes lehrt (Network Coding).

                                          - 12 -



Da der Fachmann stets bestrebt ist, den Datendurchsatz innerhalb eines Netzwerkes zu erhöhen, Verzögerungen zu reduzieren und das Netzwerk insgesamt zu
stabilisieren, bot es sich für ihn an, das CPISync-Verfahren der Druckschrift D6
auf eine Mehrzahl von Datenbank-Hosts derart zu erweitern, dass die einzelnen
Knoten in einer Konfiguration mit nur einem Masterknoten (auf dem im Wesentlichen CPISync-Verfahren inklusive Codierung der Datenpakete ablaufen) und
mehreren Slave-Hosts – in Übereinstimmung mit den vorgeschlagenen Topologien der Druckschrift D3 – angeordnet sind (z. B. Seite 500, Fig. 3 (c) und (d);
„Cross topology“ oder „Wheel topology“ mit jeweils großem „Coding Gain“;
Seite 501, links oben), so dass dementsprechend die Datensynchronisationen
paarweise zwischen den jeweiligen Slave-Hosts und dem Masterknoten entlang
der eingerichteten Kommunikationspfade erfolgen. Der Fachmann zog die Druckschrift D3 umso mehr in Betracht, als sie gerade lehrt, dass sich die hier beschriebenen Topologien mit Network Coding für eine Verwendung in drahtlosen Sensornetzen bzw. Ad-hoc-Netzen eignen (Seite 508, linke Spalte, letzter Absatz –
Seite 508, rechte Spalte, erster Absatz), d. i. in Rechnernetzen von per Funk
kommunizierenden Computern, wie sie u. a. in Satellitennetzen vorliegen.


Die Synchronisation einer Mehrzahl von Datenbank-Hosts, eine Bestimmung von
Masterknoten und Slave-Hosts, sowie der Vergleich (durch CPISync) und die
Übermittlung von Datensätzen zwischen den einzelnen Knoten sind damit durch
den aus den Druckschriften D6 und D3 bekannten Stand der Technik nahegelegt
(restlicher Teil der Merkmale (a), (b), (c), (d) und (i)).


Von einer solchen kombinierten Lehre unterscheidet sich die Lehre nach dem
Patentanspruch 1 im Wesentlichen nur noch dadurch, dass die einem Masterknoten fehlenden Datensätze nacheinander von jedem Slave-Host übertragen werden, wobei ein bereits übermittelter Datensatz nicht nochmals übertragen werden
soll (Merkmale (f) und (g)).

                                     - 13 -



Bei der Maßnahme, die Datensätze in Form von Datenpaketen nacheinander und
nicht etwa gleichzeitig von den jeweiligen Slave-Hosts an den Masterknoten zu
übermitteln, handelt es sich um eine aus fachmännischer Sicht notwendige Maßnahme, um die Konsistenz des gesamten Datenbanksystems zu erhalten (Merkmal (f)). In diesem Zusammenhang bereits übertragene Datensätze nicht ein weiteres Mal zu kommunizieren, stellt aufgrund beschränkter Netzwerkressourcen
und aus Performanzgründen eine dem Fachmann selbstverständliche Maßnahme
dar (Merkmal (g)).


Nach allem waren für den Fachmann lediglich übliche fachgemäße Überlegungen
erforderlich, um in Kenntnis der Druckschriften D6 und D3 zu einem Verfahren mit
sämtlichen Merkmalen des Patentanspruchs 1 zu gelangen.


3.    Da über einen Antrag nur einheitlich entschieden werden kann, sind auch
die übrigen Patentansprüche nicht gewährbar (BGH GRUR 1997, 120 – Elektrisches Speicherheizgerät).

                                            - 14 -



                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
      kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek                  Eder                 Dr. Thum-Rung                    Dr. Forkel




                                                                                           Fa
