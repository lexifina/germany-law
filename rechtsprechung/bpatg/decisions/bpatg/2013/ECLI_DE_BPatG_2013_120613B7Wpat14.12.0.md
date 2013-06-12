---
ecli: "ECLI:DE:BPatG:2013:120613B7Wpat14.12.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 14/12"
decided: "2013-06-12"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=33&nr=25220&anz=1167&pos=508&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-06-12_7_W-pat_14_12_NA_0.txt"
---

# Bundespatentgericht, 7 W (pat) 14/12 vom 2013-06-12

## Entscheidung

BUNDESPATENTGERICHT


  7 W (pat) 14/12                                                  Verkündet am
_______________                                                    12. Juni 2013
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


…




               betreffend die Patentanmeldung 103 93 188.0-53




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 12. Juni 2013 durch den Richter Dipl.-Phys. Dipl.-
Wirt.-Phys. Maile als Vorsitzenden sowie die Richter Schwarz, Dipl.-Phys. Dr.
Schwengelbeck und die Richterin Dipl.-Phys. Dr. Otten-Dünnweber




BPatG 154
05.11

                                        -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                     Gründe


                                          I.


Die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts hat
mit Beschluss vom 9. Mai 2007 die Patentanmeldung 103 93 188.0-53 mit der
Bezeichnung


               Verarbeitung von Wiederholungs-String-Operationen


zurückgewiesen, weil der Gegenstand des im Prüfungsverfahren geänderten
Anspruchs 1, eingegangen am 29. März 2007, im Hinblick auf die Druckschrift


        D1: US 5835972 A


nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Mit Schreiben vom 17. Mai 2013 hat der Senat zur Vorbereitung auf die mündliche
Verhandlung auf die Druckschrift


        D2: US 4 992 931 A


hingewiesen.

                                        -3-



In der mündlichen Verhandlung begehrt die Anmelderin die Erteilung des Patents
mit einer unveränderten Anspruchsfassung laut Hauptantrag sowie mit in der
mündlichen Verhandlung eingereichten geänderten Anspruchsfassungen laut 1.,
2. und 3. Hilfsantrag. Sie macht hierzu geltend, dass die geänderten Anspruchsfassungen jeweils zulässig, neu und erfinderisch seien.


Der dem Zurückweisungsbeschluss zugrunde liegende, seitens des Senats mit
einer Gliederung versehene geltende Patentanspruch 1 nach Hauptantrag lautet:


        „Verfahren mit den Schritten:


  M1 Zugreifen auf eine Anforderung einer Wiederholungs-String-Operation mit einer Operandengröße;


  M2 Ausrichten eines Quelldatenorts auf einen ersten ausgerichteten
        Ort, der einen durch eine erste vorbestimmte ganze Zahl teilbaren
        Adreßwert besitzt, wobei das Ausrichten


  M2.1 (1) ein Durchführen einer oder mehrerer String-Operationen, die
        Daten mit einer ersten Größe verwenden, die gleich der Operandengröße ist und


  M2.2 (2) ein Bestimmen, daß der Adreßwert des ersten ausgerichteten
        Orts durch die erste vorbestimmte ganze Zahl teilbar ist, umfaßt
        durch einen Prozessor; und


  M3 nach dem Ausrichten Durchführen einer oder mehrerer String-Operationen, die Daten mit einer größeren Größe als der Operandengröße verwenden.“


Der Patentanspruch 1 nach 1. Hilfsantrag entspricht dem Anspruch 1 nach Hauptantrag unter Anfügen des folgenden Merkmals:

                                       -4-



       M4 „, wobei die erste vorbestimmte Zahl 8 oder 16 ist.“


Der Patentanspruch 1 nach 2. Hilfsantrag entspricht dem Anspruch 1 nach Hauptantrag unter Anfügen folgender Merkmale:


       M5 „,wobei das Verfahren des weiteren ein Ausrichten eines
            Zieldatenortes auf einen zweiten ausgerichteten Ort umfaßt,
            der einen durch eine zweite vorbestimmte ganze Zahl teilbaren Adreßwert besitzt, wobei das Durchführen der einen oder
            mehreren String-Operationen zum Ausrichten sowohl des
            Quelldatenortes als auch des Zieldatenortes führt, und der
            zweite ausgerichtete Ort Bytes wiedergibt,


       M6 die zweite vorbestimmte ganze Zahl gleich 16 ist, der erste
            ausgerichtete Ort durch 8 teilbar ist


       M7 und das Durchführen einer oder mehrerer String-Operationen nach dem Ausrichten umfaßt:


            Laden einer ersten Datengruppe mit einer Größe von 8 Byte
            vom Quelldatenort;
            Vorschieben des Quelldatenortes um 8 Byte;
            Laden einer zweiten Datengruppe mit einer Größe von
            8 Byte vom Quelldatenort;


       M8 Verknüpfen der ersten und zweiten Datengruppe in eine 16-
            Byte-Datengruppe; Speichern der 16-Byte-Datengruppe am
            Zieldatenort.“

                                       -5-



Der Patentanspruch 1 nach 3. Hilfsantrag lautet (Änderungen gegenüber dem Anspruch 1 nach 1. Hilfsantrag hervorgehoben, Merkmal M2.2 entfällt):


             „Verfahren


       M0‘ zur Durchführung von Wiederholungs-String-Operationen,
             wobei das Verfahren umfaßt mit den Schritten:


       M1 Zugreifen auf eine Anforderung einer Wiederholungs-String-Operation mit einer Operandengröße;


       M2‘ Ausrichten eines Quelldatenorts auf einen ersten ausgerichteten Ort, der einen durch eine erste vorbestimmte ganze
             Zahl teilbaren ist Adreßwert besitzt, wobei das Ausrichten


       M2.1‘    (1) ein Durchführen einer oder mehrerer String-Operationen umfaßt, die Daten mit einer ersten Größe verwenden,
             die gleich der Operandengröße ist; und


       M3 nach dem Ausrichten Durchführen einer oder mehrerer
             String-Operationen, die Daten mit einer größeren Größe als
             der Operandengröße verwenden,


       M4‘ wobei der ausgerichtete Ort Bytes wiedergibt und die erste
             vorbestimmte ganze Zahl aus der Gruppe bestehend aus 8
             und oder 16 gewählt wird ist.“



Wegen den nebengeordneten Ansprüchen 21 und 22 sowie den jeweiligen Unteransprüchen 2 bis 20 und 23 bis 32 nach Hauptantrag und nach 1. Hilfsantrag, den
nebengeordneten Ansprüchen 18 und 19 sowie den Unteransprüchen 2 bis 17
und 20 bis 29 nach 2. Hilfsantrag sowie den nebengeordneten Ansprüchen 15 und

                                       -6-



18 sowie den Unteransprüchen 2 bis 5, 9, 10, 12 bis 14, 16, 17 und 19 bis 22 nach
3. Hilfsantrag wird auf den Akteninhalt verwiesen.


Die Anmelderin stellt den Antrag,


        den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamtes vom 9. Mai 2007 aufzuheben
        und auf die Anmeldung ein Patent mit den folgenden Unterlagen
        zu erteilen:


        -    Patentansprüche 1 bis 32 laut Anlage zum Schriftsatz vom
             29. März 2007, eingegangen am selben Tag
             hilfsweise (in der nachfolgenden Reihenfolge)


             (1. Hilfsantrag)
             Patentansprüche 1 bis 32 laut dem in der mündlichen Verhandlung vom 12. Juni 2013 überreichten Hilfsantrag I


             (2. Hilfsantrag)
             Patentansprüche 1 bis 29 laut dem in der mündlichen Verhandlung vom 12. Juni 2013 überreichten Hilfsantrag II


             (3. Hilfsantrag)
             Patentansprüche 1 bis 22 laut dem in der mündlichen Verhandlung vom 12. Juni 2013 überreichten Hilfsantrag III


        -    Beschreibung: Seite 1 und 1a laut Anlage zum Schriftsatz
             vom 29. März 2007, eingegangen am selben Tag (Bl. 69-76
             VA), im Übrigen laut der Veröffentlichung

                                       -7-



       -     Zeichnungen (Fig. 1 bis 10) laut der Veröffentlichung.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                        II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn nach dem Ergebnis der mündlichen Verhandlung beruhen die Gegenstände der jeweiligen Ansprüche 1 nach Hauptantrag sowie nach 1. bis 3. Hilfsantrag nicht auf einer erfinderischen Tätigkeit des Fachmanns, der vorliegend als Diplom-Ingenieur der Informationstechnik mit mehrjähriger Erfahrung auf dem Gebiet der Organisation von
Speicherzugriffen zu definieren ist. Die Fragen der Zulässigkeit der geltenden Ansprüche nach Haupt- und Hilfsanträgen sowie der Neuheit der Anspruchsgegenstände können somit dahinstehen (vgl. BGH GRUR 1991, 120, 121 li. Sp. Abs. 3 -
„Elastische Bandage“).




1)    Die Patentanmeldung betrifft ein Verfahren zur Durchführung von Wiederholungs-String-Operationen. Gemäß Beschreibungseinleitung (vgl. Veröffentlichung (Offenlegungsschrift) DE 103 93 188 T5, Abs. [0010]) wird durch ein
      Wiederholungs-Präfix mit dem Zeichen REP ein Prozessor dazu veranlasst,
      einen bestimmten Befehl mit einer angegebenen Anzahl von Wiederholungen auszuführen, beispielsweise das Bewegen und Kopieren eines Strings,
      das heißt einer Zeichenkette, der String kann aus Ein-Byte-, Zwei-Byteoder Vier-Byte-Dateneinheiten bestehen. Jede Wiederholung, also jeder
      einzelne Befehl, umfasst beispielsweise die Ausführung des Datentransfers
      von einem Quelldatenort auf einen Zieldatenort und darauffolgend das Aktualisieren der Register, in welchen die Speicheradresse für die Daten gespeichert ist.

                                       -8-



     Der Patentanmeldung liegt dabei die Aufgabe zugrunde, zur Verbesserung
     der Leistungsfähigkeit des Prozessors wiederholte Befehle auf effiziente
     Weise auszuführen (vgl. Offenlegungsschrift, Abs. [0002], [0010], [0011]).
     Zur Durchführung der String-Operationen soll auf kompatible Operationen
     und/oder auf schnelle Operationen zurückgegriffen werden können. Unter
     einer kompatiblen Operation werden in der Anmeldung String-Operationen
     und Wiederholungs-String-Operationen verstanden, die unter Verwendung
     einer Datengröße, die mit der des Operanden übereinstimmt, auf Daten
     wirkt. Dagegen wirkt eine schnelle Operation auf die Daten unter Verwendung einer größeren Datengröße als der Größe des Operanden. Unabhängig davon, ob schnelle Operationen oder kompatible Operationen verwendet werden, sollen die endgültigen String-Datenergebnisse im Speicher
     identisch sein, auch soll die Leistungsfähigkeit nicht durch Aufspaltungen
     der Daten auf mehrere Cache-Linien beim Zugriff auf die Daten beeinträchtigt sein (vgl. Offenlegungsschrift, Abs. [0038] und [0040]).


     Die Aufgabe soll mit den Merkmalen der jeweiligen nebengeordneten Ansprüche 1, 21 und 22 nach Hauptantrag und 1. Hilfsantrag, den Merkmalen
     der nebengeordneten Ansprüche 1, 18 und 19 nach 2. Hilfsantrag sowie
     den Merkmalen der nebengeordneten Ansprüche 1, 15 und 18 nach
     3. Hilfsantrag gelöst werden.




2) a) Zum Hauptantrag


     Anspruch 1 nach Hauptantrag ist nicht patentfähig.


     Das Verfahren gemäß Patentanspruch 1 nach 1. Hilfsantrag konkretisiert
     das Verfahren gemäß dem breiter gefassten Patentanspruch 1 nach
     Hauptantrag. Nachdem – wie nachfolgend aufgezeigt – das Verfahren des

                                   -9-



  Anspruchs 1 nach 1. Hilfsantrag nicht auf einer erfinderischen Tätigkeit beruht, gilt dies auch für das Verfahren nach Anspruch 1 gemäß Hauptantrag.


b) Zum 1. Hilfsantrag


  Das Verfahren des Patentanspruchs 1 gemäß 1. Hilfsantrag beruht nicht
  auf einer erfinderischen Tätigkeit gegenüber dem Stand der Technik gemäß
  der Druckschrift D1 i.V.m. der Druckschrift D2.


  Die Druckschrift D1 offenbart ein Verfahren mit dem Schritt des Zugreifens
  auf eine Anforderung einer Wiederholungs-String-Operation mit einer
  Operandengröße (vgl. Sp. 5, Z. 54: REP MOVS (repeat move string), Fig. 5
  und Sp. 6, Z. 20: an instruction stream 400 is input into the system. The
  instruction stream contains multiple instructions including operations …, Sp.
  6, Z. 27: multiple write instructions). Als typische Operandengröße nennt die
  D1 dabei Dateneinheiten von ein, zwei oder vier Byte (vgl. Sp. 1, Z. 47 - 48:
  a byte (8 bits), a word (16 bits), or a double word (32 bits)). Damit ist aus
  der D1 das Merkmal M1 bekannt.


  Bei dem in der D1 offenbarten Verfahren werden zunächst in Schritt 430
  Daten aus einem Speicher gelesen (vgl. Fig. 5 und Sp. 6, Z. 1 - 2: to fetch
  or read data elements from memory) und in Schritt 450 in einer
  Speichereinheit 345 abgelegt (Sp. 6, Z. 40 - 41: In step 450, the data to be
  written is stored. Steps 430 through 450 are repeated until enough data is
  collected to perform a burst write., Sp. 6, Z. 10: The storage unit is a
  temporary buffer…). Die Schritte des Lesens der Daten (vgl. Fig. 5: step
  430) und des Speicherns (vgl. Fig. 5: store data 450) werden solange
  wiederholt, bis genug Daten für ein Wegschreiben des Datenbündels
  angesammelt worden sind (vgl. Sp. 6, 41 - 43: Steps 430 through 450 are
  repeated until enough data is collected to perform a burst write.).
  Anschließend wird in Schritt 470 – entsprechend dem vorliegenden An-

                                - 10 -



spruch – eine String-Operation durchgeführt (vgl. Fig. 5: perform burst
write), die Daten mit einer größeren Größe als der Operandengröße – 1, 2
oder 4 Byte entsprechend vorstehenden Ausführungen zu Merkmal M1 –
verwendet (vgl. Sp. 8, Z. 42 - 53: In this example, the cache line size is 32
bytes and therefore, the optimum number of bytes to create a burst write
operation. / Merkmal M3teilweise, ohne die Angabe, den Schritt nach einem
Ausrichten durchzuführen).


Die D1 macht keine expliziten Aussagen hinsichtlich eines Ausrichtens des
Quelldatenortes und zugehöriger Eigenschaften der Quelldaten entsprechend den Merkmalen M2, M2.1, M2.2 oder M4, nennt jedoch als
mögliche Quelldatenorte den Hauptspeicher, einen internen Datencache
des Prozessors wie auch externe Cache-Speicher (vgl. Sp. 6, Z. 34 - 37: In
step 430, the data to be written is read from memory. Data is read from a
source address in memory, either from the internal processor data cache,
external cache or from external main memory.). Sofern der Quelldatenort
ein Cache-Speicher ist, muss dieser zunächst mit Daten aus dem
Hauptspeicher befüllt werden (vgl. Sp. 5, Z. 16 - 18: The instruction and
data cache are filled from main memory 220 through the bus interface unit.).
Damit der Zugriff von einem Cache-Speicher zum Hauptspeicher in einem
einzigen blockweisen Datentransfer erfolgen kann, sind Cache-Speicher
üblicherweise in Form von Lines oder Byteblöcken aufgebaut (vgl. hierzu
auch Sp. 5, Z. 57 - 65), und das Schreiben bzw. Lesen erfolgt nur auf bzw.
von Adressorten, deren Adresswerte ausgerichtet sind. Dabei wird es von
der speziellen Struktur des Hauptspeichers wie auch des Cache-Speichers
und von der Größe der Quelldaten abhängen, ob für das Ausrichten eigene
Operationen vonnöten sind. Bei der Nutzung eines Cache-Speichers
entsprechend der in der D1 erläuterten Ausführungsvariante, die zwingend
solche Operationen erfordert, ist der Fachmann veranlasst, auf aus dem
Stand der Technik bekannte Verfahren zur Ausrichtung von Quelldaten
zurückgreifen, wobei er – gemäß der in der Anmeldung (vgl. Abs. [0011] der

                                 - 11 -



Offenlegungsschrift) angegebenen Aufgabe einer Verbesserung der
Leistungsfähigkeit – bevorzugt Verfahren berücksichtigen wird, die eine
schnelle Ausrichtung von Daten gewährleisten. Bei der Suche nach
Verfahren zur Ausrichtung von Daten mit verbesserter Leistungsfähigkeit
stößt der Fachmann auf die Druckschrift D2, die sich mit der Korrektur der
Ausrichtung von Daten und der Formatierung von Datenstrukturen befasst.


So offenbart die D2 ein Verfahren zum Ausrichten eines Quelldatenorts
(vgl. D2, Sp. 1, Z. 42 - 43: … perform alignment correction of a data
structure at high speed by a common processing routine). Dabei werden die
Daten auf einen [ersten] ausgerichteten Ort ausgerichtet (vgl. Sp. 1, Z. 14 -
15: a head of a word must be aligned to a halfword or fullword boundary),
was nichts anderes bedeutet, als dass der ausgerichtete Ort einen durch
eine vorbestimmte ganze Zahl teilbaren Adresswert besitzt (entsprechend
Merkmal M2).


Um eine Datenstruktur an verschiedene architekturspezifische Speicherzugriffe anzupassen (vgl. Sp. 4, Z. 50 - 56: 4-byte boundary, 2-byte
boundary, 1-byte boundary), werden in der D2 weiterhin Quelldaten (source
data structure 20) in eine andere Datenstruktur transferiert (object data
structure 21), wobei Fülldaten (vgl. Sp. 3, Z. 1 - 2: A data byte to be deleted
is padding data which is inserted for alignment correction.) ergänzt oder
gelöscht werden. Bei dem in der D2 offenbarten Prozess des Ausrichtens
werden String-Operationen durchgeführt (vgl. Fig. 3A, 3B, Schritte S10 read
out, S22 read out / write, S28 generate / write), welche Daten mit einer
ersten Größe verwenden, die gleich der Operandengröße ist – hier
beispielsweise 1 Byte (vgl. Sp. 5, Z. 15 - 17: advance to a position of the
next byte to be read out, a position to the next byte to be written /
entsprechend Merkmal M2.1). In der D2 wird ferner bestimmt, ob für das
Ausrichten eine weitere String-Operation vonnöten ist (vgl. Fig. 3A, 3B,
Schritt S14 COMPLETED?, Sp. 4, Z. 14 - 19: CPU 18 checks whether the

                                 - 12 -



content of counter 15 exceeds the size value set in register section 14, in
step S14. If N (NO) in step S14, CPU 18 determines that the alignment
correction processing […] is not completed, and the flow returns). Für den
Fall, dass keine weitere String-Operation zum Ausrichten vonnöten ist,
entspricht dies einem Bestimmen durch einen Prozessor (vgl. Sp. 3, Z. 21 -
22: CPU 18 for executing a variety of alignment correction instructions),
dass    der   Adresswert   des   ausgerichteten      Orts   durch   die   [erste]
vorbestimmte ganze Zahl teilbar ist (entsprechend Merkmal M2.2).


Es liegt damit für den Fachmann nahe, bei einem Verfahren, wie es aus der
Druckschrift D1 bekannt ist, einen Quelldatenort nach dem Vorbild der D2
auf einen ersten ausgerichteten Ort auszurichten, der einen durch eine
erste vorbestimmte ganze Zahl teilbaren Adresswert besitzt (Merkmal M2),
wobei dementsprechend auch String-Operationen durchgeführt werden, die
Daten mit einer ersten Größe verwendet, die gleich der Operandengröße ist
(Merkmal M2.1) und entsprechend der Lehre der D2 dann auch durch
einen   Prozessor   zu     bestimmen,     ob   der   Adresswert     des   ersten
ausgerichteten Orts durch die erste vorbestimmte ganze Zahl teilbar ist
(Merkmal M2.2).


In der D1 erfolgt das Transferieren der Quelldaten auf den Cache-Speicher,
welches – wie vorstehend ausgeführt – nach der Lehre der D2 ein
Ausrichten beinhaltet, zeitlich vor dem Durchführen der String-Operationen,
die das Wegschreiben des Datenbündels betreffen. Somit muss das
Durchführen der String-Operationen, die Daten mit einer größeren Größe
als der Operandengröße verwenden, auch zwingend nach dem Ausrichten
des Quelldatenortes erfolgen (vgl. D1, Fig. 5, Schritte 430, 470 / Merkmal
M3 Rest).


Gemäß Merkmal M4 soll die erste vorbestimmte Zahl 8 oder 16 sein, was
nichts anderes bedeutet, als dass der erste ausgerichtete Ort (vgl.

                                - 13 -



Merkmale M1, M2) auf eine Datengröße von 8 oder 16 Bytes ausgerichtet
ist. In der D1 sind als typische Größen von Cachelines 16, 32 oder 64 bytes
genannt (vgl. Sp. 5, Z. 59 - 61). Wenn der Fachmann als Quelldatenort
einen Cache-Speicher vorsieht, auf den – wie zum Merkmal M2 ausgeführt
– ausgerichtet geschrieben wird und der beispielsweise eine der in der D1
explizit genannten Cacheline-Größen aufweist, so bedeutet dies aber nichts
anderes, als dass die erste vorbestimmte ganze Zahl ein Teiler der Größe
der Cacheline ist – für eine Cacheline in der Größe von beispielsweise 32
Byte ist der Speicherort daher auf die Datengrößen 32, 16, 8, 4, 2 und
1 Byte ausgerichtet, wovon als erste vorbestimmte ganze Zahl auch 8 und
16 umfasst sind (Merkmal M4).


Den Ausführungen der Anmelderin in der mündlichen Verhandlung, in der
D1 werde kein „aktives Ausrichten“ beschrieben und eine Ausrichtung
könne allenfalls zufällig auftreten, kann seitens des Senats nicht gefolgt
werden. Beim beanspruchten Verfahren mag es zwar je nach Größe der
auszurichtenden Quelldaten und der Startadresse der auszurichtenden
Quelldaten möglich sein, ein Ausrichten eines Quelldatenorts ohne
Überschreiben von Daten zu erreichen, indem die Daten in Größe der
Operandengröße in ein und demselben Speicher lediglich vor- oder
zurückverschoben werden. Das vorliegend beanspruchte Verfahren macht
aber hinsichtlich der Startadresse oder der Größe der auszurichtenden
Daten keine Einschränkung. Daher wird auch beim jetzt beanspruchten
Verfahren der Schritt des Ausrichtens ggf. nicht ohne              ein Zwischenspeichern der auszurichtenden Daten durchgeführt; explizit wird in
der vorliegenden Anmeldung dazu erläutert, dass „die Vermeidung eines
Überschreibens auf eine Vielzahl von Arten berücksichtigt werden [kann],
wie beispielsweise dadurch, dass […] Werte an temporären Orten gespeichert werden“ (vgl. Abs. [0056] der Offenlegungsschrift). Dies entspricht
jedoch der in der D1 erläuterten Ausführungsvariante, bei der Daten

                                  - 14 -



  zunächst vom Hauptspeicher in einen Cache-Speicher gespeichert werden,
  was – wie erläutert – regelmäßig ein Ausrichten beinhaltet.


  Der Fachmann gelangt somit zum Verfahren des Anspruchs 1 nach
  1. Hilfsantrag, indem er das aus der Druckschrift D1 bekannte Verfahren
  zur Verarbeitung von Wiederholungs-String-Operationen in der Variante mit
  einem Zwischenspeichern der Daten in einem Cache-Speicher implementiert und die zwingend notwendige Ausrichtung der Quelldatenorte in diesem Zwischenspeicher in naheliegender Weise nach dem Vorbild des in der
  Druckschrift D2 offenbarten Verfahrens ausführt.


c) Zum 2. Hilfsantrag


  Auch das Verfahren gemäß 2. Hilfsantrag beruht nicht auf einer erfinderischen Tätigkeit, da es sich für den Fachmann in naheliegender Weise aus
  dem Stand der Technik gemäß den Druckschriften D1 und D2 i.V.m. dem
  fachmännischen Handeln ergibt.


  In Patentanspruch 1 des 2. Hilfsantrags sind die Merkmale M1 bis M3 wortgleich zu den entsprechenden Merkmalen des Anspruchs 1 nach
  1. Hilfsantrag, so dass hinsichtlich dieser Merkmale auf die Ausführungen
  unter Abschnitt 2) b) verwiesen wird.


  Gemäß Merkmal M5 ist zusätzlich ein Ausrichten des Zieldatenortes gefordert. Die D1 offenbart ein Ausrichten eines Zieldatenorts auf einen zweiten
  ausgerichteten Ort (vgl. D1: Anspruch 6 und Sp. 6, Z. 47 - 48: burst writes
  to cache memory must be the size (number of bytes) of a cache line and
  aligned on a cache line boundary), wobei der zweite ausgerichtete Ort in
  Form des als Cache-Speicher ausgebildeten Zielspeichers zweifelsohne
  Bytes wiedergibt (M5teilweise, ohne Angabe wie das Ausrichten durchzuführen ist). Analog zu den Ausführungen zum Merkmal M4 aus den Ausfüh-

                                  - 15 -



rungen zum 1. Hilfsantrag, bedeutet das Ausrichten auf eine Cacheline –
hier jetzt für den Zieldatenort (vgl. D1: Sp. 10, Z. 52 - 53: the destination
address is aligned on a cache line boundary) – aber nichts anderes, als
dass die zweite vorbestimmte ganze Zahl ein Teiler der Größe der Cacheline ist, der ausgerichtete Ort des Zieldatenorts also einen durch eine zweite
vorbestimmte ganze Zahl teilbaren Adresswert besitzt. Das Ausrichten der
Datenorte wird der Fachmann – wie zum Merkmal M2.1 ausgeführt – in naheliegender Weise in Form des aus der D2 bekannten Verfahrens implementieren, so dass String-Operationen zum Ausrichten sowohl des Zieldatenorts wie des Quelldatenorts führen (Merkmal M5 Rest).


Die D1 offenbart als typische Cacheline-Größe beispielsweise auch 16 Byte
(vgl. Sp. 5, Z. 64: a 16 byte cache line size), was für die ausgerichteten Orte
aber bedeutet, dass die zweite vorbestimmte ganze Zahl auch die Zahl 16
umfasst und bei einem als Cache-Speicher ausgebildeten Quelldatenort der
erste ausgerichtete Ort schließlich auch durch 8 teilbar ist (Merkmal M6).


In der D1 wird als ein konkretes Ausführungsbeispiel das Verfahren mit einem viermaligen Laden von Daten in die Speichereinheit 345 und einem
anschließenden Speichern eines Bitbündels von 32 Byte, was durch die
Größe der gewählten Cacheline des Zielspeichers bedingt ist, erläutert.
Damit offenbart die D1, dass vom Quelldatenort wiederholt eine Datengruppe mit einer Größe von 8 Byte geladen wird (vgl. Sp. 9, Z. 13 - 15: Continuing with Step 560A from step 540A, this step is repeated four times to
create a burst write of four 64 bit writes (for a cache line size of 32 bytes).).
Dabei erfolgt zwingend nach dem Laden einer ersten Datengruppe mit einer
Größe von 8 Byte ein Vorschieben des Quelldatenortes um 8 Byte (vgl. Fig.
6: Schritt 560A: INCREMENT SOURCE_INDEX und Sp. 12, Table I,
14. Zeile von unten: source_index = source_index +8), bevor eine zweite
Datengruppe mit einer Größe von 8 Byte vom Quelldatenort geladen wird
(Merkmal M7).

                                   - 16 -




  In der D1 erfolgt schließlich im Schritt 570A ein Schreiben des Bitbündels
  (vgl. Fig. 6 und Sp. 9, Z. 21: a burst write is performed in step 570 A), wobei
  die Datengruppe am Zieldatenort gespeichert wird (vgl. Sp. 9, Z. 59 - 60:
  The data elements in the buffer are written to the address indicated by destination_index as a burst write.). Bei einer gewählten Cacheline-Größe von
  32 Byte, gemäß dem in der D1 erläuterten Ausführungsbeispiel, erfolgt das
  Speichern am Zieldatenort für eine 32-Byte-Datengruppe. Es liegt aber im
  Belieben des Fachmanns, eine andere Cacheline-Größe zu wählen, beispielsweise die in der D1 ebenfalls als typisch genannte Cacheline-Größe
  von 16 Byte. Bei einer Cacheline-Größe von 16 Byte, erfolgt zwangsläufig
  bereits nach zweimaligem Laden, d.h. dem Sammeln der Datengruppen in
  der Speichereinheit 345, ein Verknüpfen der ersten und zweiten Datengruppe in eine 16-Byte-Datengruppe, an das sich das Speichern der 16-
  Byte-Datengruppe an den Zieldatenort (einen Cache mit 16 Byte großer
  Cacheline) anschließt, so dass dem Fachmann aus der Druckschrift D1
  auch das Merkmal M8 nahegelegt ist.


  Auch die zusätzlich im Anspruch 1 nach 2. Hilfsantrag aufgeführten Merkmale M5 bis M8 sind somit bereits aus der D1 bekannt bzw. dem Fachmann nahegelegt.


  Der Anspruch 1 nach 2. Hilfsantrag ist daher nicht patentfähig.


d) Zum 3. Hilfsantrag


  Anspruch 1 nach 3. Hilfsantrag entspricht dem Anspruch 1 nach 1. Hilfsantrag, wobei das Merkmal M2.2 gestrichen ist, ein Merkmal M0‘ vorangestellt
  ist und in den Merkmalen M2‘, M2.1‘ und M4‘ sprachliche Umformulierungen vorgenommen wurden, die hinsichtlich des beanspruchten Verfahrens
  keine Änderungen bedingen. Das Merkmal M0‘ beinhaltet eine Verwen-

                                         - 17 -



        dungsangabe, welche das beanspruchte Verfahren nicht weiter einschränkt.
        Im Übrigen ist die jetzt aufgenommene Verwendung auch aus der D1 bekannt (vgl. D1: Anspruch 1: a method of writing a plurality of data elements).
        Damit gilt das zum Verfahren nach Anspruch 1 gemäß 1. Hilfsantrag Gesagte hier in analoger Weise.

        Das Verfahren nach Anspruch 1 gemäß 3. Hilfsantrag ist somit ebenfalls
        nicht patentfähig.




3)      Mit den jeweils nicht patentfähigen Ansprüchen 1 nach Hauptantrag und
        nach den Hilfsanträgen 1 bis 3 sind auch die auf diese Ansprüche direkt
        oder indirekt rückbezogenen Unteransprüche nicht schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war (vgl. BGH,
        GRUR 2007, 862 Leitsatz – „Informationsübermittlungsverfahren II“).




4)      Nachdem die jeweiligen Anspruchssätze nach Hauptantrag bzw. nach den
        Hilfsanträgen 1 bis 3 nicht patentfähig sind, war die Beschwerde zurückzuweisen.




Maile               Schwarz             Dr. Schwengelbeck     Dr. Otten-Dünnweber


                                                                                   Hu
