---
ecli: "ECLI:DE:BPatG:2011:141111B20Wpat22.07.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 22/07"
decided: "2011-11-14"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=76&nr=23273&anz=1310&pos=1142&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-11-14_20_W-pat_22_07_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 20 W (pat) 22/07 vom 2011-11-14

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 22/07                                               Verkündet am
_______________                                              14. November 2011
    (Aktenzeichen)                                                   …




                               BESCHLUSS

                             In der Beschwerdesache


             betreffend die Patentanmeldung 10 2006 007 025.9-35


…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 14. November 2011 durch den Vorsitzenden
Richter Dipl.-Phys. Dr. Mayer, die Richterin Kirschneck sowie die Richter
Dipl.-Ing. Gottstein und Dipl.-Ing. Albertshofer




BPatG 154
05.11

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.


                                    Gründe


                                        I.


Die Patentanmeldung 10 2006 007 025.9 mit der Bezeichnung "Vorrichtung zum
Detektieren einer Signalart" ist im Verfahren vor dem Deutschen Patent- und Markenamt von der Prüfungsstelle für Klasse H 04 B durch Beschluss vom
21. März 2007 zurückgewiesen worden.


Der Zurückweisung lagen die mit Eingabe vom 20. Februar 2007 eingereichten
Patentansprüche 1 bis 15 zugrunde.


Der Anmeldung betrifft die digitale Signalverarbeitung und insbesondere die Signaldetektion. Bei der Übertragung von Datenpaketen über einen Mobilfunkkanal
kommt es zur Mehrwegeausbreitung, welche eine Intersymbol-Interferenz des Signals verursacht. Diese wird üblicherweise mit einer Kombination aus linearem Entzerrer und Viterbi-Algorithmus beseitigt. Das empfangene Signal wird in der Regel
neben der Intersymbol-Interferenz zusätzlich von verschiedenen anderen Störungen, wie z. B. Rauschen, Gleichkanal- und Nachbarkanal-Interferenz, überlagert
(Offenlegungsschrift, S. 1 Absätze 0001 - 0003).


Während bei der Gleichkanal-Interferenz die Störung im gleichen Frequenzband
wie das Nutzsignal liegt und beispielsweise durch einen in einer anderen Zelle des
Netzes aktiven Teilnehmer hervorgerufen wird, liegt die Störung bei der Nachbarkanal-Interferenz in einem der beiden benachbarten Frequenzbänder (Offenlegungsschrift, S. 1, Absatz 0003).

                                          -3-



In vielen Mobilkommunikationssystemen wie z. B. GSM (Global System for Mobile
Communication) und dessen Weiterentwicklung EDGE (Enhanced Data Services
for GSM Evolution) ist die Gesamtübertragungsbandbreite in eine Vielzahl von
schmalbandigen Frequenzbändern (Verkehrskanälen) unterteilt. Dies hat zur Folge, dass das Nutzsignal und die Nachbarkanalstörung einander spektral überlappen. Es ist nicht möglich, die Nachbarkanal-Interferenz vollständig zu unterdrücken, ohne das Spektrum des Nutzsignals einzuengen (Offenlegungsschrift, S. 1
Absatz 0005).


Der Anmeldung liegt daher die Aufgabe zugrunde, ein Konzept zur Detektion von
Signalarten zu schaffen, mit dem auch Störungsarten aufwandsreduziert detektiert
bzw. erkannt werden können (Abs. [0019]).


Die Prüfungsstelle hat ihren Beschluss damit begründet, dass der Gegenstand
des   der       Zurückweisung   zugrunde        liegenden   Patentanspruchs 1   vom
21. Februar 2007 dem Fachmann ausgehend von dem bekannten Stand der
Technik


          (1)   US 2003/0231721 A1


in Verbindung mit seinem fachmännischen Können nahe gelegt sei und damit auf
keiner erfinderischen Tätigkeit beruhe.

                                         -4-



Mit ihrer Beschwerde verfolgt die Anmelderin ihre Anmeldung weiter.


In der mündlichen Verhandlung hat die Anmelderin neue Patentansprüche 1 bis
12 eingereicht. Sie beantragt,


        den Beschluss der Prüfungsstelle für Klasse H 04 B des Deutschen Patent- und Markenamts vom 21. März 2007 aufzuheben
        und das nachgesuchte Patent aufgrund folgender Unterlagen zu
        erteilen:


        - Patentansprüche 1 bis 12, überreicht in der mündlichen Verhandlung,
        - Beschreibung,       Seiten 1    bis   22,   vom     Anmeldetag
          15. Februar 2006,
        - 5 Blatt Zeichnungen, Figuren 1 bis 5, vom 9. März 2006.


Der geltende Patentanspruch 1 lautet mit eingefügter Gliederung:


        M1     "Vorrichtung zum Detektieren einer Signalart eines Signals,
               das ein Signalart-abhängiges Signalspektrum aufweist, mit:


        M1a    einem Prozessor (303, 305), der ausgebildet ist,


        M1a1 um eine erste Größe zu bestimmen, die für ein erstes Teilspektrum des Signalspektrums charakteristisch ist, und


        M1a2 um eine zweite Größe zu bestimmen, die für ein zweites
               Teilspektrum des Signalspektrums charakteristisch ist,


               gekennzeichnet durch

                                        -5-



        M1b ein Mittel zum Bestimmen eines Verhältnisses zwischen der
               ersten Größe und der zweiten Größe, und


        M1c    einen Detektor (309), der ausgebildet ist, um das Verhältnis
               mit einem Schwellwert zu vergleichen und um die Signalart
               auf der Basis des Verhältnisses zu detektieren, wobei der
               Detektor (309) ausgebildet ist, um


        M1c1 eine erste Signalart zu detektieren, wenn das Verhältnis
               größer als ein erster Schwellwert ist, um


        M1c2 eine zweite Signalart zu detektieren, wenn das Verhältnis
               kleiner als ein zweiter Schwellwert ist, welcher kleiner als
               der erste Schwellwert ist, und


        M1c3 um in sonstigen Fällen Rauschen zu detektieren."


Bezüglich des Wortlauts der weiteren, in der mündlichen Verhandlung vom
14. November 2011 eingereichten Unteransprüche 2 bis 12 wird auf die Gerichtsakte (Bl. 26 bis 29) verwiesen.


Neben der US 2003/0231721 A1 (1) wurde in der mündlichen Verhandlung auch
die in der Anmeldungsbeschreibung genannte WO 02/067444 A1 (2) diskutiert.


Die Beschwerdeführerin hält die Vorrichtung zum Detektieren einer Signalart nach
den Merkmalen des geltenden Patentanspruchs 1 für patentfähig, da sie durch
den diskutierten Stand der Technik weder neuheitsschädlich vorweggenommen
noch dem Fachmann nahegelegt sei.


Wegen der weiteren Einzelheiten wird auf den Inhalt der Akten Bezug genommen
und verwiesen.

                                       -6-



                                        II.


Die zulässige Beschwerde hat keinen Erfolg. Der Gegenstand des geltenden Patentanspruchs 1 mag zwar neu sein, er beruht jedoch nicht auf einer erfinderischen Tätigkeit i. S. d. § 4 PatG.


1. Der Anmeldegegenstand richtet sich an einen Diplomingenieur der Nachrichtentechnik mit Hochschulabschluss, der mit der Signalübertragung beim Mobilfunk
befasst ist und sich dort auch mit der Problematik bei der Verarbeitung störbehafteter Signale auseinandersetzt.


2. Der US 2003/0231721 A1 (1) ist in der Figur 1 das Blockschaltbild eines Signaldetektors zu entnehmen, der am Eingang zum Empfangen des Signals zumindest
zwei wählbare Filter aufweist, wobei je nach Vorliegen einer bestimmten Störung
auf dem Eingangssignal ein entsprechendes Eingangsfilter ausgewählt wird (Abstract). Ein Element 120 (noise determination) dient zum Erkennen, welche Art einer Störung (z. B. Gleichkanalstörung oder Nachbarkanalstörung) in einem Empfangssignal vorliegt (Fig. 1, Bezugszeichen 120, Absatz [0026]). Je nach Art der
Störung weist das untersuchte Eingangssignal ein anders geformtes Spektrum auf
(vgl. Fig. 7A und 7B). Damit beschreibt diese Druckschrift in Übereinstimmung mit
dem geltenden Patentanspruch 1 eine "Vorrichtung zum Detektieren einer Signalart eines Signals, das ein Signalart-abhängiges Signalspektrum aufweist" (Merkmal M1).


Eine weitere Ausführungsart der in Rede stehenden Detektorvorrichtung, die in
Übereinstimmung mit dem Anspruchsgegenstand als digitaler Signalprozessor
ausgeführt sein kann (vgl. Absatz [0033] und Patentanspruch 9; Merkmal M1a), ist
in Figur 6 dargestellt. Diese umfasst ein Hochpass- und ein Tiefpassfilter
(Bezz. 670, 680), die jeweils Filterausgangssignale einer ersten und zweiten Größe liefern, die wiederum für ein erstes und zweites Teilspektrum charakteristisch

                                        -7-



sind (vgl. Absatz [0032], Merkmale M1a1 und M1a2) und einer ersten und zweiten
Signalart entsprechen.


Bei dieser aus der US 2003/0231721 A1 (1) bekannten Detektorvorrichtung werden anschließend die Ausgangsgrößen der beiden Filter einem "Max Detector" 690 zugeführt, der die beiden Größen miteinander vergleicht und anhand des
Ergebnisses dieses Vergleichs ein Ausgabesignal erzeugt, welches einen Schalter 695 ansteuert. Dieser schaltet dann, je nachdem welche Signalart vorliegt
(Nachbarkanal- oder Gleichkanalinterferenz), den Empfängereingang auf eines
der Eingangsfilter 610, 620 (Fig. 1, Absatz [0030] bis [0032]).


Wie der Fachmann aus der Arbeitsweise der Schaltungsanordnung nach der Figur 6 unmittelbar erkennt, kann der "Max Detector" 690 eine eindeutige Zuordnung zu einer Signalart nur solange treffen, als die anliegenden Eingangsgrößen
noch unterscheidbar sind. Andernfalls verfällt der "Max Detector" in einen undefinierten Zustand, welcher die Funktionsfähigkeit der Gesamtanordnung in Frage
stellt. Der Fachmann ist daher auf Grund seiner Fachkenntnisse veranlasst, ihm
bekannte Maßnahmen aufzugreifen, die einen sicheren Betrieb gewährleisten. Da
der Signaldetektor gemäß der Figur 6 und damit auch der "Max Detector" 690 innerhalb eines digitalen Signalprozessors realisiert sind (Patentanspruch 9) und es
daher nur geringfügige Änderungen im Programmablauf bedarf, kann der Fachmann aufgrund seiner Fachkenntnisse dieses Problem in einfacher Weise dadurch
umgehen, dass er zur Detektion der Signalart im Signaldetektor zunächst das Verhältnis zwischen diesen beiden Größen bildet (Merkmal M1b, M1c) und dieses
Verhältnis mit zwei Schwellwerten vergleicht (Merkmale M1c und M1c1, M1c2),
d. h. dass er zur Erkennung des undefinierten Zustandes (anspruchsgemäß "Rauschen" genannt) einen Bereich festgelegt durch zwei Schwellwerte vorgibt (Merkmal M1c2) Die Einführung zweier definierter Schwellwerte ist dem Fachmann somit deshalb nahe gelegt, da immer dann, wenn zwischen annähernd gleich großen
Signalen unterschieden werden soll, so eine sichere Entscheidung zwischen den
beiden Signalen möglich ist.

                                       -8-



In diese Richtung zielt auch die Lehre der WO 02/067444 A1 (2), die sich ebenfalls mit der Detektion von Störsignalen wie z. B. Gleichkanal- oder Nebenkanalinterferenz oder auch Rauschen befasst (Seite 19, Zeilen 24 bis 25) und die Fachkenntnisse des zuständigen Fachmanns belegt im Hinblick auf die Nutzung von
Schwellwerten beim Vergleich von zwei ins Verhältnis gesetzten Größen, die aus
Messwerten bestimmt worden sind.


Um den Interferenztyp zu bestimmen, werden dort vorab "Interference Templates"
bestimmt, die bestimmten Störsignalen entsprechen, und in einer Datenbank gespeichert sind (Seite 21, Zeile 12 ff.). Aus einem empfangenen Signal wird dann
eine Größe abgeleitet, die mit den abgespeicherten Templates verglichen wird
(Seite 23, Zeilen 18 ff.). Anschließend wird der Abstand dieser Größe zu den in
der Datenbank hinterlegten "Interference Templates" ermittelt und das "Interference Template" ausgewählt, das den geringsten Abstand zu der Größe aufweist
(Seite 24, Zeilen 9 bis 10). Um die Verlässlichkeit der Entscheidung zu erhöhen,
wird der geringste Abstand mit dem Abstand zum zweitnächsten "Interference
Template" verglichen. Diese Abstände entsprechen vom Verständnis her den Ausgangsgrößen der beiden Filter 670, 680 gemäß Figur 6 der Druckschrift (1). Nur
wenn sich diese Abstände hinreichend unterscheiden, wird davon ausgegangen,
dass ein Interferenztyp mit hoher Wahrscheinlichkeit korrekt bestimmt wurde (Seite 24, Zeile 12-15). Für diese Wahrscheinlichkeitsbetrachtung wird das Verhältnis
(Quotient) der beiden Abstände zu den am nächsten kommenden Interferenztypen
gebildet, wobei immer der Abstand, der einer möglichen Interferenz am nächsten
kommt (z. B. Interferenz 1), im Nenner steht. Dabei ergibt sich zwangsläufig ein
Quotient größer als 1. Dieser Quotient wird mit einem Schwellwert (= 1.2) verglichen und falls der Wert größer als der Schwellwert ist, wird ein bestimmter Störungstyp ("Signalart") mit hoher Wahrscheinlichkeit erkannt (Seite 24, Zeilen 17 bis
26). Dem Fachmann ist dabei sofort klar, dass diese Vorgehensweise gleichbedeutend mit der Vorgehensweise ist, den Quotienten der beiden kleinsten Abstände zu bilden, unabhängig davon, welcher im Nenner steht, und diesen Quotienten
dann mit zwei Schwellwerten zu vergleichen. Steht der geringere Abstand nicht im

                                        -9-



Nenner, sondern im Zähler des Quotienten, so ist dieser Quotient kleiner als 1. Für
eine Erkennung mit hoher Wahrscheinlichkeit muss der Quotient dann kleiner als
der Kehrwert des Schwellwertes (= 1.2), also kleiner als 0,83 sein. Setzt man also
die zwei ermittelten Abstände ins Verhältnis, so ergeben sich zwei Schwellwerte,
die für eine Erkennung des Interferenztyps mit hoher Wahrscheinlichkeit erforderlich sind. Falls der Quotient größer als 1.2 (erster Schwellwert) ist, wird mit hoher
Wahrscheinlichkeit die Interferenz 1 ("erste Signalart", entspricht der Größe im
Nenner) ermittelt, und wenn der Quotient kleiner als 0.83 (zweiter Schwellwert) ist,
wird mit hoher Wahrscheinlichkeit der Interferenztyp 2 ("zweite Signalart", entspricht der Größe im Zähler) ermittelt. Liegt der Quotient zwischen den beiden
Schwellwerten, so ist die Wahrscheinlichkeit für eine bestimmte Interferenz zu gering und es wird keine Interferenz festgestellt ("Rauschen"). Dies entspricht den
Merkmalen M1c1, M1c2 und M1c3 des geltenden Patentanspruchs 1.


Der Fachmann gelangt zur Überzeugung des Senats somit in Anwendung seiner
Fachkenntnisse ausgehend von der Detektorvorrichtung nach der Druckschrift (1)
auf naheliegende Weise zum Gegenstand von Anspruch 1; er muss nicht erfinderisch tätig werden. Man würde die Kenntnisse und Fähigkeiten des Fachmanns
unterschätzen, würde man ihm solches Handeln nicht zutrauen.


3. Nachdem sich der Patentanspruch 1 als nicht patentfähig erweist, kann die beantragte Patenterteilung nicht erfolgen. Mit dem Patentanspruch 1 fallen auch alle
anderen Ansprüche. Aus der Fassung des Antrags und dem zu seiner Begründung Vorgebrachten ergeben sich keine Zweifel an dem prozessualen Begehren
der auch in der mündlichen Verhandlung anwaltlich vertretenen Anmelderin, das
Patent ausschließlich in der beantragten Fassung zu erteilen (BGH, Beschluss

                                    - 10 -



vom 27. Februar 2008 - X ZB 10/07, GRUR-RR 2008, 456, Tz. 22 - Installiereinrichtung, m. w. N.).




Dr. Mayer              Kirschneck            Gottstein           Albertshofer




                                                                          Pü
