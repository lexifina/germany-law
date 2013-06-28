---
ecli: "ECLI:DE:BPatG:2013:280613B7Wpat46.11.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 46/11"
decided: "2013-06-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=39&nr=25441&anz=1167&pos=590&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-06-28_7_W-pat_46_11_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 7 W (pat) 46/11 vom 2013-06-28

## Entscheidung

BUNDESPATENTGERICHT

                                                                 Verkündet am
                                                                 28. Juni 2013
    7 W (pat) 46/11                                                   …
_______________
    (Aktenzeichen)




                             BESCHLUSS

                           In der Beschwerdesache


                betreffend die Patentanmeldung 102 97 166.8-53


…




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Juni 2013 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Schwarz, Dipl.-Phys. Dr. Schwengelbeck
und die Richterin Dipl.-Phys. Dr. Otten-Dünnweber




BPatG 154
05.11

                                        -2-



beschlossen:


                       Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                         I.


Die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts hat
mit Beschluss vom 16. Januar 2008 die Patentanmeldung 102 97 166.8-53 mit der
Bezeichnung


       „Mechanismus zur Interrupt-Abwicklung in Computersystemen,
       welche die gleichzeitige Ausführung mehrerer Threads unterstützen“


zurückgewiesen, weil der Gegenstand des zuletzt geltenden Anspruchs 1 gegenüber der im Prüfungsverfahren ermittelten Druckschrift


       D2: US 5 581 770 A


nicht auf einer erfinderischen Tätigkeit beruhen würde, wobei zum Beleg des fachmännischen Grundwissens auf die folgende Druckschrift verwiesen wurde:


       D3: NEHMER, Jürgen: Systemsoftware: Grundlagen moderner Betriebssysteme; 1. Aufl. – Heidelberg: dpunkt-Verl.,
               1998, Seiten 163 - 165


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.

                                         -3-



Sie stellt sinngemäß den Antrag, aus dem Schriftsatz vom 3. März 2008, der unverändert gilt,


        den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamtes vom 16. Januar 2008 aufzuheben und auf die Anmeldung ein Patent mit folgenden Unterlagen
        zu erteilen:


        -   Patentansprüche 1 bis 20 vom 17. April 2007,


        -   Beschreibungsseiten 2, 2a vom 17. März 2006 sowie ursprüngliche Beschreibungsseiten 1 und 3 bis 15 und 4 Blatt Zeichnungen mit Fig. 1 bis 5 vom 1. März 2004.


Der geltende, seitens des Senats mit einer Gliederung versehene Patentanspruch 1 lautet:


     M1       „Verfahren, das als Reaktion auf einen Interrupt durch jeden Thread,
              der gerade auf einem Mehrfachkontextprozessor ausgeführt wird,
              implementiert wird, mit den Schritten

     M2       - Zugreifen auf einen Interrupt-Handler an einer angegebenen Speicherstelle;

     M3       - Ausführen des Interrupt-Handlers, um einen Wert in einem Interrupt-Anspruch-Register zu lesen;

     M3.1     wobei die Ausführung des Interrupt-Handlers das Lesen des Werts in
              dem Interrupt-Anspruch-Register und

     M3.2     das Schreiben eines zweiten Werts in das Register, ohne die Kontrolle
              über das Register aufzugeben, umfasst und

                                        -4-



     M4      die Ausführung des Interrupt-Handlers beendet wird, wenn der aus dem
             Interrupt-Anspruch-Register gelesene Wert ein erster Wert oder der zweite
             Wert ist.“

Wegen den geltenden nebengeordneten Ansprüchen 2, 7 und 13 sowie den abhängigen Ansprüchen 3 bis 6, 8 bis 12 und 14 bis 20 wird auf den Akteninhalt verwiesen.


Zur Vorbereitung auf die mündliche Verhandlung hat der Senat die Beschwerdeführerin mit Schreiben vom 18. Juni 2013 u.a. darauf hingewiesen, dass auch die
Zulässigkeit des Anspruchs 1 fraglich sei, insbesondere im Hinblick auf das Merkmal, dass „die Ausführung des Interrupt-Handlers beendet wird, wenn der aus
dem Interrupt-Anspruch-Register gelesene Wert ein erster Wert oder der zweite
Wert ist“.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                         II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn nach dem Ergebnis der mündlichen Verhandlung wurde der Gegenstand des geltenden Anspruchs 1 gegenüber dem Inhalt der Anmeldung in der ursprünglich eingereichten
Fassung unzulässig erweitert (§ 38 Satz 1 PatG). Es kann somit dahingestellt bleiben, ob die Gegenstände der geltenden Ansprüche im Hinblick auf die §§ 1 bis 5
PatG patentfähig sind.


1)
Die Patentanmeldung betrifft einen Mechanismus zur Abwicklung von Interrupts in
Computersystemen, die die gleichzeitige Ausführung mehrerer Threads unterstützen (vgl. die Offenlegungsschrift DE 102 97 166 T5, Abs. [0001]). Mit dem Begriff
Thread werden in der Anmeldung Ausführungsstränge bei der Abarbeitung eines

                                         -5-



Programms bezeichnet, die unabhängig voneinander und zeitgleich ausgeführt
werden könnten; die Threads besäßen jeweils einen identischen Kontext, worunter
der Verweis auf die Register verstanden werde, die den Architekturzustand eines
Threads für eine bestimmte Prozessorarchitektur speicherten. Nach der Offenlegungsschrift seien moderne Hochleistungsprozessoren dafür ausgelegt, in jedem
Taktzyklus mehrere Anweisungen auszuführen; zur Erhöhung des Anweisungsdurchsatzes seien die Prozessoren so entworfen, dass sie die Anweisungen von
zwei oder mehr Anweisungsthreads gleichzeitig ausführen könnten. Die Leistungsvorteile von Prozessoren, die mehrere Threadkontexte unterstützten – in der Anmeldung Mehrfachkontextprozessoren genannt –, hingen von der Fähigkeit der
Prozessoren ab, als mehrere, äquivalente logische Prozessoren zu erscheinen. Es
sei ein Ziel, dass ein Mehrfachkontextprozessor als ein symmetrisches Mehrprozessorsystem erscheine (vgl. Offenlegungsschrift, Abs. [0002], [0003], [0008]).


Nach der Offenlegungsschrift ist in der Regel jedem logischen Prozessor eine
Interrupt-Einheit zugeordnet, die als Schnittstelle zwischen dem logischen Prozessor und Betriebsmitteln auf Systemebene oder gemeinsam benutzten Betriebsmitteln des Prozessors fungiere. Ein Nachteil der mehrfach vorliegenden Interrupt-Einheiten bestehe darin, dass ein Interrupt häufig von allen logischen Prozessoren
gesehen werde. Die symmetrische Konfiguration der logischen Prozessoren verpflichte jeden der logischen Prozessoren, den Interrupt-Code auszuführen, obwohl
es in vielen Fällen genügen würde, wenn lediglich einer der logischen Prozessoren den Interrupt abwickeln würde (vgl. Abs. [0009] und [0010] der Offenlegungsschrift).


Die Anmeldung befasst sich daher mit den Problemen, die mit der Interrupt-Abwicklung in Prozessoren, welche die gleichzeitige Ausführung mehrerer Threads
unterstützen, verbunden sind (vgl. Offenlegungsschrift Abs. [0011]). Die zugrunde
liegende Aufgabe bestehe darin, einen sicheren Betrieb eines logischen Prozessors auch für den Fall unerwünschter Interrupts, wie beispielsweise durch einen
Lüfterausfall, zu schaffen (vgl. Schriftsatz vom 17. April 2007).

                                        -6-



Diese Aufgabe soll durch einen Mechanismus gelöst werden, der es einem bestimmten logischen Prozessor gestattet, die volle Interrupt-Abwicklungsroutine für
einen Interrupt, der durch alle logischen Prozessoren registriert wird, auszuführen
(vgl. Offenlegungsschrift, Abs. [0024]). Als Reaktion auf einen Interrupt konkurrierten die logischen Prozessoren um den Zugriff auf ein gemeinsam benutztes Register. Der erste der logischen Prozessoren, der auf das gemeinsam benutzte Register zugreift, wickele den Interrupt ab. Die übrigen logischen Prozessoren kehrten aus dem Interrupt-Handler zurück (vgl. Offenlegungsschrift Abs. [0048]).




2)
Der Gegenstand des geltenden Anspruchs 1 geht über den Inhalt der Anmeldung
in der ursprünglich eingereichten Fassung hinaus. Denn gemäß Merkmal M4 wird
beansprucht, dass die Ausführung des Interrupt-Handlers beendet wird, wenn der
aus dem Interrupt-Anspruch-Register gelesene Wert ein erster Wert oder der
zweite Wert ist. Dass die Ausführung des Interrupt-Handlers unter den in Merkmal
M4 angegebenen allgemeinen Bedingungen, nämlich sowohl für den Fall, dass
der gelesene Wert ein erster Wert ist, wie auch für den Fall, dass der gelesene
Wert ein zweiter Wert ist, beendet wird, ist den ursprünglichen Unterlagen jedoch
nicht zu entnehmen.


In der Anmeldung wird unterschieden zwischen dem „Abschließen der Ausführung
des Interrupt-Handlers“ und dem „Beenden der Ausführung des Interrupt-Handlers“. Gemäß den Angaben in der Beschreibung beinhaltet ein Abschließen der
Ausführung des Interrupt-Handlers, dass der logische Prozessor mit der Interrupt-Abwicklungsroutine fortfährt (vgl. Offenlegungsschrift, Abs. [0035] und [0039]
sowie den ursprünglichen Anspruch 20), also den Interrupt abwickelt. Hingegen
bedeutet das Beenden der Ausführung des Interrupt-Handlers, dass der logische
Prozessor aus dem Interrupt zurückkehrt und seinen unterbrochenen Thread wieder aufnimmt (vgl. Offenlegungsschrift, Abs. [0029] und [0035] sowie den ursprünglichen Anspruch 22).

                                       -7-



Der geltende Anspruch 1 basiert auf dem ursprünglichen Anspruch 20, in dessen
letzter Merkmalsgruppe gefordert war, dass ein Abschließen der Ausführung des
Interrupt-Handlers erfolgt, wenn der aus dem Interrupt-Anspruch-Register gelesene Wert ein erster Wert ist. Die Beschreibung erläutert dazu: „Der logische Prozessor, der den ersten Wert liest, setzt die Ausführung des Interrupt-Handlers fort.
Die übrigen logischen Prozessoren lesen den zweiten Wert, der ihnen signalisiert,
aus dem Interrupt zurückzukehren, z.B. um die Ausführung ihrer unterbrochenen
Threads wieder aufzunehmen“ (vgl. Abs. [0026] der Offenlegungsschrift). Dementsprechend war im ursprünglichen Anspruch 22 gefordert, dass „die Ausführung
des Interrupt-Handlers beendet wird, wenn der aus dem Interrupt-Anspruch-Register gelesene Wert der zweite Wert ist“. Laut geltendem Anspruch 1 soll jedoch
die Ausführung des Interrupt-Handlers beendet werden, wenn der aus dem Interrupt-Anspruch-Register gelesene Wert ein erster Wert oder der zweite Wert ist
– was nichts anderes bedeutet, als dass der Interrupt weder von dem logischen
Prozessor, der den ersten Wert liest, noch von dem logischen Prozessor, der den
zweiten Wert liest, ausgeführt wird, sondern die Prozessoren unabhängig vom
gelesenen Wert aus dem Interrupt zurückkehren.


Ein solches Verfahren, bei dem auch der logische Prozessor, der den ersten Wert
liest, die Ausführung des Interrupt-Handlers nicht fortsetzt, sondern beendet, kann
den ursprünglichen Unterlagen nicht als mögliche Ausgestaltung der Erfindung
entnommen werden. Der beanspruchte Gegenstand geht daher in unzulässiger
Weise über den Inhalt der ursprünglichen Anmeldung hinaus.


Für eine weitergehende Beurteilung des Patentbegehrens war daher kein Raum
mehr. Vielmehr ist der Anspruch 1 schon deshalb nicht gewährbar, weil sein Gegenstand über den Offenbarungsgehalt der ursprünglichen Unterlagen hinaus
unzulässig erweitert wurde.

                                     -8-



3)
Mit dem nicht zulässigen Anspruch 1 sind auch die auf den Anspruch 1 rückbezogenen nebengeordneten Ansprüche 2, 7 und 13, nicht schutzfähig ebenso die
auf diese Ansprüche direkt oder indirekt rückbezogenen Unteransprüche nicht
schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war (vgl. BGH, GRUR 2007, 862 Leitsatz – „Informationsübermittlungsverfahren II“).




4)
Bei dieser Sachlage war die Beschwerde zurückzuweisen.




Wickborn         Schwarz        Dr. Schwengelbeck        Dr. Otten-Dünnweber


                                                                           Hu
