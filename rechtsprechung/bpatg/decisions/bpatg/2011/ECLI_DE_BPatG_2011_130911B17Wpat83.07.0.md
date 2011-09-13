---
ecli: "ECLI:DE:BPatG:2011:130911B17Wpat83.07.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 83/07"
decided: "2011-09-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=60&nr=22589&anz=1310&pos=901&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-09-13_17_W-pat_83_07_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 83/07 vom 2011-09-13

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 83/07                                                    Verkündet am
_______________                                                   13. September 2011
    (Aktenzeichen)                                                         …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2005 036 999.5-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 13. September 2011 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch, des Richters Dipl.-Ing. Prasch, der
Richterin Eder und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
05.11

                                         -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                          I.


Die vorliegende Patentanmeldung ist am 5. August 2005 unter der Bezeichnung


         „Verfahren und Anordnung zur Darstellung zeitlich veränderlicher
                   Vorgänge in der medizinischen Bildgebung“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 3. Juli 2007 die
Anmeldung zurückgewiesen, da der Gegenstand des Patentanspruchs 1 nicht auf
einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        Patentansprüche 1 bis 4 vom 21. März 2006, eingegangen am
        22. März 2006,
        noch anzupassende Beschreibung Seiten 1 bis 7 und 2 Blatt
        Zeichnungen mit 4 Figuren, jeweils vom Anmeldetag.

                                        -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: US 2003/0031380 A1
        D2: P. A. Henning: Taschenbuch Multimedia, 2. Auflage 2001, Fachbuchverlag Leipzig im Carl Hanser Verlag München Wien, S. 173 bis 187
        D3: Liang Cheng et al: Real-time 3D Graphics Streaming Using MPEG-4,
              Univ. of California, Irvine, CA, July 18, 2004 (veröff. in: Proc. IEEE /
              ACM Workshop on Broadband Wireless Services and Appl., 2004).


Vom Senat wurden zusätzlich die Druckschriften


        D4: US 2002/0180761 A1
        D5: DE 102 10 644 A1
        D6: DE 103 09 165 A1


eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da die Gegenstände des Patentanspruchs 1
und des nebengeordneten Patentanspruchs 3 nicht auf erfinderischer Tätigkeit
beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.   Die Patentanmeldung betrifft ein Verfahren sowie eine Anordnung zur Darstellung zeitlich veränderlicher Vorgänge in der medizinischen Bildgebung, bei
denen von einer bildgebenden Modalität erhaltene 2D- oder 3D-Bilddaten verar-

                                        -4-



beitet werden, um eine zeitliche Folge von Bildern zu erzeugen, zwischen zeitlich
aufeinander folgenden Bildern durch Interpolation Zwischenbilder erzeugt und die
Bilder mit den Zwischenbildern in zeitlicher Abfolge dargestellt werden.


Der Beschreibungseinleitung folgend, werden in der medizinischen Bildgebung
häufig zeitlich veränderliche Vorgänge aufgezeichnet, die dem Anwender geeignet
verarbeitet dargestellt werden müssen. Hierbei werde zwischen der Darstellung
zweidimensionaler (2D-) Bilder der zeitlich veränderlichen Vorgänge und der Darstellung dreidimensionaler (3D-) Bilder der zeitlich veränderlichen Vorgänge unterschieden. Zweidimensionale Bilder könnten beispielsweise Ultraschallbilder, Perfusionsbilder bei der Computertomographie (CT), Bilder aus der CT-Fluoroskopie
oder Aufnahmen der Magnetresonanztomographie (MR) sein. Dreidimensionale
Bilder könnten beispielsweise Aufnahmen des bewegten Herzens mit unterschiedlichen Modalitäten oder Bilder der virtuellen Endoskopie von Hohlorganen wie
Darm, Bronchien, Ventrikel oder Gefäßen mittels CT oder MR, bei Gefäßen auch
mittels Ultraschall sein.


Nach der Aufzeichnung der Messdaten mit der entsprechenden bildgebenden
Modalität würden diese Daten in der Regel zunächst geeignet vorverarbeitet, um
aus diesen Messdaten 2D- oder 3D-Bilddaten zu erhalten. Bei der Bildgebung zur
Darstellung zeitlich veränderlicher Vorgänge werde eine Folge von 2D- oder 3D-Bilddatensätzen erhalten, die zu unterschiedlichen Aufnahmezeitpunkten mit der
bildgebenden Modalität erfasst würden. Diese Bilddatensätze würden anschließend weiterverarbeitet, um die für den Anwender geeignete Bilddarstellung zu
erhalten. Das Ergebnis seien zweidimensionale Bilder, die in zeitlicher Abfolge an
einem Bildschirm dargestellt würden. Die Bildrate werde dabei vom Algorithmus
der Verarbeitung, von der Geschwindigkeit der für die Verarbeitung eingesetzten
Verarbeitungseinheit sowie, falls eine Darstellung in Echtzeit erfolgen solle, von
der Datenrate des Aufnahmesystems der bildgebenden Modalität bestimmt. Da die
Darstellung der Bilder häufig auf einer oder mehreren örtlich beliebig verteilten
Darstellungseinheiten erfolge, sei die Bildrate zudem noch durch die Geschwindig-

                                       -5-



keit der Datenverbindung zu diesen Darstellungseinheiten begrenzt. Dies führe
dazu, dass die Bildrate häufig nicht ausreichend hoch sei, eine flüssige Darstellung der aufgezeichneten zeitlichen Veränderungen zu erreichen.


Die Aufgabe der vorliegenden Erfindung soll darin bestehen, ein Verfahren sowie
eine Anordnung zur Darstellung zeitlich veränderlicher Vorgänge in der medizinischen Bildgebung anzugeben, mit denen sich demgegenüber eine flüssigere Darstellung erreichen lässt, vgl. S. 2 Abs. 2 der Anmeldeunterlagen.


Der mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft ein


        a) Verfahren zur Darstellung zeitlich veränderlicher Vorgänge in der medizinischen Bildgebung,

        b) bei dem von einer bildgebenden Modalität erhaltene 2D- oder 3D-Bilddaten (1, 2) in einer als Server dienenden Verarbeitungseinheit (10)
        verarbeitet werden, um eine zeitliche Folge von Bildern (8) eines zeitlich
        veränderlichen Vorgangs zu erzeugen, die an eine als Client dienende
        Darstellungseinheit (14) übermittelt werden,

        c) wobei in der als Client dienenden Darstellungseinheit (14) durch eine
        Interpolation (6) zwischen zeitlich aufeinander folgenden Bildern (8) bisher
        nicht vorhandene Zwischenbilder (9) erzeugt werden und die Bilder (8) mit
        den Zwischenbildern (9) in zeitlicher Abfolge dargestellt werden.


Der nebengeordnete Patentanspruch 3 betrifft eine


        A) Anordnung zur Darstellung zeitlich veränderlicher Vorgänge in der medizinischen Bildgebung, mit

        B) einer Verarbeitungseinheit (10) als Server, die eine Speichereinheit (11) zur Speicherung von 2D- oder 3D- Bilddaten (1, 2) eines zeitlich

                                       -6-



        veränderlichen Vorgangs sowie ein Verarbeitungsmodul (12) zur Erzeugung einer zeitlichen Folge von Bildern (8) des zeitlich veränderlichen Vorgangs aus den 2D- oder 3D- Bilddaten (1, 2) umfasst, und

        C) einer mit der Verarbeitungseinheit (10) über eine Datenverbindung (13) verbundene Darstellungseinheit (14) als Client, die ein Interpolationsmodul (15) zur Erzeugung von bisher nicht vorhandenen Zwischenbildern (9) aus der von der Verarbeitungseinheit (10) übertragenen
        zeitlichen Folge von Bildern (8) und ein Darstellungsmodul (16) zur Darstellung der Bilder (8) und Zwischenbilder (9) umfasst.


Als Fachmann sieht der Senat hier einen in der medizinischen Bilddatenverarbeitung und -darstellung erfahrenen Fachhochschul- oder Hochschul-Ingenieur der
Fachrichtung Informationstechnik an.


2.   Aus dem Stand der Technik erachtet der Senat die Druckschriften D4 und D6
als besonders relevant. Diese zeigen Folgendes:


D4 betrifft ein medizinisches Darstellungssystem. Die darzustellenden Datensätze
können z. B. medizinische Bilder desselben Körperteils sein, die zu unterschiedlichen Zeitpunkten aufgenommen wurden und zeitliche Änderungen zeigen, vgl.
Abs. [0002] Satz 2 und Abs. [0010] letzter Satz. Die von einem Bildgenerator 11
kommenden Bilder werden bei Bedarf in Pixeldaten konvertiert und liegen dann
als aufeinander folgende Frames von Pixeldaten (2D-Datensätze) vor, vgl.
Abs. [0011] sowie Fig. 1. In einem Videoprozessor 15 werden Bewegungsvektorfelder zwischen benachbarten Frames bestimmt, welche die Verschiebung von
Bildelementen zwischen benachbarten Frames repräsentieren. Mit Hilfe der Bewegungsvektorfelder werden interpolierte Bilder berechnet und zwischen die Frames
eingefügt, vgl. Abstract sowie Abs. [0014] und [0017]. Die so erzeugte, in einem
Bildspeicher 17 abgelegte Bildsequenz kann als Film auf einem Videodisplay
abgespielt werden, vgl. Abs. [0018]. Im Fall zeitlicher Bildfolgen zeigt dieser Film

                                       -7-



Veränderungen in inneren Organen oder Geweben, mit glatten, ruckfreien Übergängen zwischen den einzelnen Bildern, vgl. Abstract und Abs. [0020].


D6 betrifft eine medizinische Systemarchitektur zur interaktiven Übertragung und
progressiven Darstellung von komprimierten Bilddaten. Gemäß Fig. 2 mit Beschreibung werden von bilderzeugenden medizinischen Systemen (1 bis 4) aufgenommene Daten verarbeitet und die Bilddaten als Rohdaten in einer Datenbank 17 und in komprimierter und paketierter Form in einer Datenbank 19 gespeichert, vgl. Abs. [0036]. Aus letzterer können Benutzer (Clients 11a bis 11c) Bilder
mit verschiedener Auflösung abrufen, die ihnen vom Bild-Server 14 geliefert werden, vgl. Abs. [0037] bis [0040] sowie Fig. 3. Eine Client-Workstation 11 ist beispielsweise ein sehr schneller Kleincomputer auf Basis eines oder mehrerer
schneller Prozessoren, in dem die gelieferten Bilddatenpakete dekomprimiert,
lokal abgespeichert, zur Befundung abgerufen und als Multikomponentenbilder
wie Bildserien oder Volumina in progressiver Qualität visualisiert werden können,
vgl. Abs. [0001], [0031] und [0039] bis [0041]. Gemäß Abs. [0058] können in
einem „Movie-Mode“ die Einzelkomponenten eines Multikomponentenbildes
schichtweise durchlaufen werden.


3.   Die Gegenstände des geltenden Anspruchs 1 und des nebengeordneten
Anspruchs 3 beruhen nicht auf erfinderischer Tätigkeit.


Wie oben ausgeführt, zeigt D6 eine Systemarchitektur mit Client/Server-Struktur
und damit auch ein entsprechendes Verfahren, in der bzw. dem medizinische Multikomponentenbilder verarbeitet und dargestellt werden. Multikomponentenbilder
können z. B. Sätze von 2D-Bilddaten sein und Bildsequenzen zeitlich veränderlicher Vorgänge beinhalten, wie sie bei Herzuntersuchungen anfallen, etwa bei der
digitalen Subtraktionsangiographie DSA, vgl. Abs. [0003] und [0029] - Merkmale a), A). Die in einer als Server dienenden Verarbeitungseinheit verarbeiteten
und in komprimierter und paketierter Form in einer Datenbank gespeicherten Bilddaten werden zum Client übertragen und dort dekomprimiert, lokal gespeichert

                                         -8-



und visualisiert, z. B. in einem „Movie-Mode“ - Merkmale b), B). Um im System
gemäß D6 eine möglichst flüssige, ruckfreie Darstellung der zeitlich aufeinander
folgenden Bilder zu ermöglichen, bot es sich für den Fachmann an, bei Bedarf
gemäß der aus D4 bekannten Lehre durch Interpolation zwischen zeitlich aufeinander folgenden Bildern bisher nicht vorhandene Zwischenbilder zu erzeugen
und einzufügen, so dass die Bilder und die Zwischenbilder in zeitlicher Abfolge am
Client dargestellt werden - teilweise Merkmale c), C). Für die Durchführung der
Interpolation zwischen den einzelnen Bildern boten sich dem Fachmann zwei
Möglichkeiten, nämlich die Durchführung am Server, an dem bereits eine Verarbeitung und Komprimierung der Daten stattfindet, oder die Durchführung am
Client, der aufgrund seiner Ausstattung als sehr schneller, mit schnellen Prozessoren ausgestatteter Kleincomputer ebenfalls eine Bilddatenverarbeitung erlaubt
und auf dem bereits die Dekompression der übertragenen Bilddaten stattfindet.
Hierbei musste der Fachmann Vor- und Nachteile dieser beiden Möglichkeiten
abwägen: Bei Interpolation am Server werden auch die interpolierten Daten (in
komprimierter Form) zentral gespeichert und stehen jedem anfordernden Client
zur Verfügung, wobei allerdings eine größere Datenmenge an den Client übertragen werden muss; bei Interpolation am Client muss nur eine geringere Datenmenge an den Client übertragen werden, jedoch müssen an jedem anfordernden
Client, der eine flüssigere Darstellung wünscht, relativ aufwändige Rechenoperationen durchgeführt werden. Eine solche Abwägung zwischen zwei Möglichkeiten
der Durchführung von Rechenoperationen fällt in den Bereich typischen fachmännischen Handelns. Wenn der Transfer der Bilddaten an den Client ein „Nadelöhr“
darstellt (vgl. die in D6 Abs. [0001] angesprochene möglicherweise geringe Übertragungsbandbreite sowie der in D6 zur Komprimierung, Paketierung und Übertragung der Daten in unterschiedlichen Auflösungsstufen getriebene Aufwand, der
einen Betrieb mit relativ geringer Datenübertragungsrate an den Client ermöglicht), und wenn zu erwarten ist, dass nur wenige Clients (etwa nur diejenigen, die
eine Bildsequenz in voller Auflösung darstellen wollen) interpolierte Bilddaten
benötigen, verlagert der Fachmann ohne Weiteres die Interpolation auf den Client
- restlicher Teil der Merkmale c), C).

                                       -9-



Durch diese Überlegungen konnte der Fachmann zum Verfahren gemäß dem geltenden Anspruch 1 gelangen, wozu keine erfinderische Tätigkeit erforderlich war.


Entsprechendes gilt für die Anordnung gemäß dem nebengeordneten Anspruch 3.


Nach Ansicht der Anmelderin zeigt D6 einen anderen Weg als die vorliegende
Anmeldung, um mit einer geringen Übertragungsrate zwischen Server und Client
zurechtzukommen, nämlich die Übertragung komprimierter und paketierter Bilddaten in unterschiedlichen Auflösungsstufen. Zudem hätte der Fachmann in D6
ebenso wie alle übrigen Verarbeitungsschritte auch die Interpolation am Server
durchgeführt; eine Interpolation am Client, an dem üblicherweise keine Verarbeitung durchgeführt wird, hätte er nicht in Betracht gezogen.


Dem konnte sich der Senat nicht anschließen. In den geltenden Ansprüchen 1 und
3 und ebenso in der gesamten vorliegenden Anmeldung ist nichts darüber ausgesagt, in welcher Form die Übertragung der Bilddaten vom Server an den Client
erfolgen soll; eine Komprimierung der Daten vor der Übertragung mit nachfolgender Dekomprimierung im Client wie in D6 ist nicht ausgeschlossen, diese Möglichkeit ist von den geltenden Ansprüchen 1 und 3 mit umfasst. Zudem ist eine
Datenverarbeitung am Client in Form einer Dekompression der übertragenen Daten bereits in D6 ausgewiesen; auch war es dem Fachmann aus seinem Fachwissen bekannt, am Client weitere Verarbeitungsschritte durchzuführen, etwa
interaktiv durch den Benutzer gesteuerte Operationen wie Hervorhebung und
Bearbeitung bestimmter Bildbereiche. Somit hätte es der Fachmann ohne Weiteres in Betracht gezogen, auch andere Bildverarbeitungsoperationen, etwa die
durch D4 nahegelegte Interpolation zwischen Bildern, am Client durchzuführen.


Der Anspruch 1 und ebenso der nebengeordnete Anspruch 3 ist nicht gewährbar.

                                      - 10 -



4.   Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
abhängigen Patentansprüche 2 und 4 nicht gewährbar (BGH in GRUR 1997, 120
„Elektrisches Speicherheizgerät“).




Dr. Fritsch       Eder        Ri Prasch ist nach Beschluss-     Dr. Thum-Rung
                              fassung mit Ablauf des Monats
                              September 2011 in den Ruhestand getreten und daher an
                              der Unterschrift gehindert.

                              Dr. Fritsch, 4. Oktober 2011




                                                                             Fa
