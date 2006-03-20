---
ecli: "ECLI:DE:BPatG:2006:200306B17Wpat93.05.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 93/05"
decided: "2006-03-20"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2006&Sort=1&Seite=23&nr=281&anz=1665&pos=355&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2006-03-20_17_W-pat_93_05_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 93/05 vom 2006-03-20

## Entscheidung

BUNDESPATENTGERICHT



 17 W (pat) 93/05
_______________________

    (Aktenzeichen)




                             BESCHLUSS

                            In der Beschwerdesache


                 betreffend die Patentanmeldung 196 50 520.8-53


…




hat der 17. Senat des Bundespatentgericht am 20. März 2006 unter Mitwirkung
…




BPatG 152
08.05

                                        -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 8. März 2005 aufgehoben. Die Sache wird unter
       Zugrundelegung der folgenden Unterlagen zur weiteren Prüfung
       an das Deutsche Patent- und Markenamt zurückverwiesen:


       -       Patentansprüche 1 – 3 eingeg. 10.2.2006
       -       Beschreibung Seiten 1, 4, 4a eingeg. 25.4.2005
                             sowie 2, 3 und 5 – 22 vom 5.12.1996
       -       Figuren 1 – 4, 5 A – 5 F vom 5.12.1996




                                     Gründe


                                         I.


Die vorliegende Patentanmeldung, für die die Priorität einer Anmeldung in den
USA vom 1. März 1996 in Anspruch genommen wird, ist am 5. Dezember 1996
beim Deutschen Patent- und Markenamt unter der Bezeichnung


„Adressenaggregationssystem und -Verfahren zum Erhöhen des Adressendurchsatzes von einem Prozessor zu einem Datencache"


angemeldet worden.


Sie wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
Markenamts durch Beschluss vom 8. März 2005 mit der Begründung zurückgewiesen, mit dem neuen Patentanspruch 1 bleibe weiterhin unklar, was unter
Schutz gestellt werden soll (§ 34 Absatz 3 Satz 3 PatG).

                                        -3-



Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Sie hat mit Eingabe vom 9. Februar 2006 neue Patentansprüche eingereicht und
beantragt:


       die Anmeldung zur Prüfung an das Deutsche Patent- und Markenamt zurückzuverweisen,


       hilfsweise die Anberaumung eines Termins zur mündlichen Verhandlung.


Der geltende Patentanspruch 1 lautet:


       „Verfahren zum Verarbeiten von Datenadressen in einem Prozessor (14) und zum Erhöhen des Durchsatzes der Datenadressen (99a, 99b) von dem Prozessor (14) zu einem Datencache (24), wobei der Datencache (24) eine ungerade Bank (98a)
       und eine gerade Bank (98b) aufweist, um während eines einzelnen Prozessorzyklus gleichzeitig Adressen an der ungeraden Bank (98a) und an der geraden Bank (98b) zu empfangen,
       und wobei der Prozessor (14) eine Adreßberechnungseinrichtung (58) zum Bereitstellen von Adressen und eine Adreßspeicherschlange (38b) aufweist, wobei das Verfahren (80) folgende Schritte aufweist:


       (a) falls die Adreßspeicherschlange (38b) keine geraden
       Adressen enthält:
            (a.1) Bestimmen derjenigen ungeraden Adresse (88a) in
                  der Adreßspeicherschlange (38b), die einem ältesten empfangenen Befehl mit einer ungeraden Adresse entspricht, und

                                     -4-



             (a.2) während eines einzelnen Zyklus des Prozessors
                   (14), Übermitteln der im Schritt (a.1) bestimmten

                   ungeraden Adresse (88a) zu der ungeraden Bank
                   des Datencache (24) und Schalten eines Umwegpfades (92b) für eine gerade Adresse von der
                   Adreßberechnungseinrichtung (58) direkt zu der geraden Bank des Datencache (24); und


       (b)   falls die Adreßspeicherschlange (38b) keine ungeraden
             Adressen enthält:
             (b.1) Bestimmen derjenigen geraden Adresse (88b) in
                   der Adreßspeicherschlange (38b), die einem ältesten empfangenen Befehl mit einer geraden Adresse
                   entspricht, und
             (b.2) während eines einzelnen Zyklus des Prozessors
                   (14), Übermitteln der im Schritt (b.1) bestimmten
                   geraden Adresse (88b) zu der geraden Bank des
                   Datencache (24) und Schalten eines Umwegpfades
                   (92a) für eine ungerade Adresse von der Adreßberechnungseinrichtung (58) direkt zu der ungeraden
                   Bank des Datencache (24).“

Wegen der Unteransprüche 2 und 3 wird auf die Akten verwiesen.


                                      II.


Die Beschwerde führt zur Aufhebung des angefochtenen Beschlusses und zur Zurückverweisung der Sache an das Deutsche Patent- und Markenamt gemäß § 79
Abs. 3 Satz 1 Nr. 1 PatG.


1. Die Anmeldung betrifft nunmehr im Besonderen ein Verfahren zum Erhöhen
des Durchsatzes für einen Cache-Speicher. Ein wesentliches Lösungsmerkmal ist
dabei, dass der Cache aus zwei Speicherbänken besteht, die sich beide innerhalb

                                       -5-



eines Prozessortaktes gleichzeitig nutzen lassen, wodurch sich der Durchsatz
verdoppeln könnte. Die für die Ansteuerung der „geraden“ und der „ungeraden“
Speicherbank erforderliche Trennung in „gerade“ und „ungerade“ Adressen geschieht in einer Adressenwarteschlange („Adressspeicherschlange“), in der mehrere gewünschte Adressen auf Abarbeitung warten.


Für den Sonderfall, dass entweder keine gerade oder keine ungerade Adresse
mehr ansteht, soll zusätzlich ausgehend von der Adressberechnungseinheit des
Prozessors ein Umgehungspfad geschaltet werden, so dass eine dort anstehende
Adresse, falls sie passend „gerade“ oder „ungerade“ ist, unter Umgehung der Adressenwarteschlange direkt benutzt werden kann. So wird eine Möglichkeit geschaffen, anstelle von Leerlauf einen zusätzlichen Speicherzugriff abzuarbeiten,
d. h. der Durchsatz wird wie beabsichtigt noch etwas weiter erhöht.


Als Fachmann für solche Speicheransteuerungen wird ein Entwicklungsingenieur
für Halbleiterspeicherschaltungen mit Hochschul- oder Fachhochschulausbildung
und mehrjähriger Berufserfahrung angesehen.


2. Der Zurückweisungsbeschluss wurde mit Unklarheit des zuvor geltenden Patentanspruchs 1 begründet, der auf eine „Befehls-Abruf und Verarbeitungseinrichtung“ gerichtet war. Dieser Anspruch und seine Unteransprüche werden mit den
neu eingereichten Patentansprüchen nicht weiterverfolgt.


Der geltende Hauptanspruch ist auf das Schalten eines Umgehungspfades (Umwegpfad) gerichtet, falls entweder keine gerade oder keine ungerade Adresse in
der Adressenwarteschlange ansteht. Dieses Merkmal war nicht in den ursprünglichen Patentansprüchen enthalten; es basiert auf den Seiten 13/14 der Beschreibung (Offenlegungsschrift Spalte 7 Zeile 48 ff., insbesondere Spalte 7 Zeile 61 –
Spalte 8 Zeile 5, Spalte 8 Zeile 57 – 60) und Figur 3, ist somit als erfindungswesentlich offenbart. Das geltende Patentbegehren ist daher zulässig, und die Pa-

                                       -6-



tentansprüche geben nunmehr verständlich an, was unter Schutz gestellt werden
soll.


Damit ist der Grund für den Zurückweisungsbeschluss ausgeräumt.


3. Der im bisherigen Verfahren zitierte Stand der Technik steht dem geltenden
Hauptanspruch nicht patenthindernd entgegen, da er in Hinsicht auf das neue
Merkmal des Schaltens von Umgehungspfaden, ausgelegt für die Ansteuerung
zweier Speicherbänke mit „geraden“ / „ungeraden“ Adressen, keine Anregung
enthält. Allenfalls Druckschrift 3: WO 94 / 08 287 A1 beschreibt in Figur 3 einen
Umgehungspfad 330 zu einem Adressmultiplexer 340 aus einer Adressberechnungseinrichtung DAFU 230, gibt aber keinen Hinweis auf eine geeignete Ansteuerung in Abhängigkeit von geraden bzw. ungeraden Adressen zum Erhöhen des
Durchsatzes.


Das neue Merkmal ist ersichtlich nicht Gegenstand des bisherigen Prüfungsverfahrens gewesen. In den Bescheiden und dem Protokoll der Anhörung findet sich
kein Hinweis darauf.


Demnach hat das Deutsche Patent- und Markenamt für die geltende Fassung der
Patentansprüche bisher nicht geprüft, ob die Voraussetzungen für die Erteilung
eines Patents erfüllt sind. Weil es damit noch nicht in der Sache selbst entschieden hat, war die Anmeldung – auch um der Anmelderin keine Tatsacheninstanz zu
nehmen – zurückzuverweisen.




gez.
Unterschriften
