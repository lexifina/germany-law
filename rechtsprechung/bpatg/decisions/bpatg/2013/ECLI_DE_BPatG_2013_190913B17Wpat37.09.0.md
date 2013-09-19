---
ecli: "ECLI:DE:BPatG:2013:190913B17Wpat37.09.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 37/09"
decided: "2013-09-19"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=56&nr=25480&anz=1167&pos=854&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-09-19_17_W-pat_37_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 37/09 vom 2013-09-19

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 37/09                                               Verkündet am
_______________                                              19. September 2013
    (Aktenzeichen)                                                    …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 199 34 515.5-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 19. September 2013 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder sowie der
Richter Dipl.-Ing. Baumgardt und Dipl.-Ing. Hoffmann




BPatG 154
05.11

                                       -2-



beschlossen:


        Die Beschwerde wird zurückgewiesen.


        Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 22. Juli 1999 beim Deutschen
Patent- und Markenamt eingereicht. Sie nimmt die Priorität einer Voranmeldung in
den USA vom 24. Juli 1998 in Anspruch und trägt die Bezeichnung:


  „Verfahren und Einrichtung zum Durchführen von Cache-Segment-Flush- und
                     Cache-Segment-Invalidier-Operationen“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts vom 17. Februar 2009 zurückgewiesen. Die
Prüfungsstelle begründet die Zurückweisung damit, dass der Gegenstand des
damals geltenden Hauptanspruchs gemäß Haupt- und Hilfsantrag mangels Erfindungshöhe nicht gewährbar sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Der Vertreter der Anmelderin stellte den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                     -3-



       gemäß Hauptantrag mit
            Patentansprüchen 1 bis 4, überreicht in der mündlichen Verhandlung,
            Beschreibung Seiten 1 bis 13 und
            Figuren 3, 4A, 4C, jeweils vom 18.05.2001, eingegangen am
            21.05.2001,
            Figuren 1, 2, 4B, 5A - B vom Anmeldetag;
       gemäß 1. Hilfsantrag mit
            Patentansprüchen 1 bis 4, überreicht in der mündlichen Verhandlung,
            im Übrigen wie Hauptantrag;
       gemäß 2. Hilfsantrag mit
            Patentansprüchen 1 bis 4, überreicht in der mündlichen Verhandlung,
            im Übrigen wie Hauptantrag;
       gemäß 3. Hilfsantrag mit
            Patentansprüchen 1 bis 3, überreicht in der mündlichen Verhandlung,
            im Übrigen wie Hauptantrag;
       gemäß 4. Hilfsantrag mit
            Patentansprüchen 1 bis 2, überreicht in der mündlichen Verhandlung,
            im Übrigen wie Hauptantrag.


Er regte die Rückzahlung der Beschwerdegebühr an.


Der geltende Patentanspruch 1 des Hauptantrags lautet:


       1.   Verfahren zum Invalidieren und/oder zum Ausführen einer Flush-Operation eines vorgegebenen Bereichs eines Cache-Speichers (300) in einem Computersystem (100) mit einem Prozes-

                                           -4-



                    sor (105), wobei der Prozessor eine Dekodiereinheit (140) und
                    eine Ausführungseinheit (142) aufweist, wobei:
        a)          ein einzelner Befehl von der Dekodiereinheit dekodiert wird,
                    wobei der Befehl (160, 162, 164, 166) eine Invalidier- und/oder
                    eine Flush-Operation spezifiziert und einen Operanden (212) aufweist;
        b)          in Erwiderung des Dekodierens des einzelnen Befehls (160) von
                    der Ausführungseinheit eine von einem Benutzer spezifizierte
                    Startadresse des vorgegebenen Bereichs des Cache-Speichers
                    gewonnen wird, wobei die Startadresse unter Verwendung des
                    Operanden (212) gewonnen wird; und
        c)          die Ausführung des einzelnen Befehls abgeschlossen wird,
                    indem jeder Eintrag in dem vorgegebenen Bereich des Cache-Speichers beginnend an der vom Benutzer spezifizierten Startadresse von dem Prozessor invalidiert und/oder einer Flush-Operation unterzogen werden, wobei ein Eintrag invalidiert wird,
                    indem ein Ungültig-Bit gesetzt wird, und ein Eintrag einer Flush-Operation unterzogen wird, indem Daten aus dem Eintrag kopiert
                    und die kopierten Daten in einem vom Cache-Speicher getrennten Speicherbereich gespeichert werden.


Zu den Unteransprüchen 2 bis 4 wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 des ersten Hilfsantrags unterscheidet sich in den
Merkmalen a) und c) vom Patentanspruch 1 des Hauptantrags (Unterschiede sind
unterstrichen).


        a.1)      ein einzelner Befehl von der Dekodiereinheit dekodiert wird, wobei
                  der Befehl (160, 162, 164, 166) eine Invalidier- und/oder eine Flush-Operation spezifiziert und einen Operanden (212) aufweist, der ein

                                         -5-



                Register oder einen Speicherplatz spezifiziert, das bzw. der eine
                Startadresse enthält;


         c.1)   die Ausführung des einzelnen Befehls abgeschlossen wird, indem
                jeder Eintrag in dem vorgegebenen Bereich des Cache-Speichers
                beginnend an der vom Benutzer spezifizierten Startadresse durch
                den Prozessor invalidiert und/oder einer Flush-Operation unterzogen werden, wobei ein Eintrag invalidiert wird, indem ein Ungültig-Bit gesetzt wird, und ein Eintrag einer Flush-Operation unterzogen
                wird, indem Daten aus dem Eintrag kopiert und die kopierten Daten
                in einem vom Cache-Speicher getrennten Speicherbereich gespeichert werden.


Zu den Unteransprüchen 2 bis 4 wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 des zweiten Hilfsantrags unterscheidet sich in
Merkmal a) vom Patentanspruch 1 des Hauptantrags (Unterschied ist unterstrichen).


         a.2)   ein einzelner Befehl von der Dekodiereinheit dekodiert wird, wobei
                der Befehl (160, 162, 164, 166) eine Invalidier- und/oder eine Flush-Operation spezifiziert und einen Operanden (212) aufweist, der ein
                Register spezifiziert, das eine Startadresse enthält;


Zu den Unteransprüchen 2 bis 4 wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 des dritten Hilfsantrags unterscheidet sich vom
Patentanspruch 1 des zweiten Hilfsantrags durch Hinzufügung des Merkmals d).

                                         -6-



       d)     im Schritt b) zum Gewinnen der Startadresse:
              b.1) ein Abschnitt der Startadresse aus einem in dem dekodierten
              Befehl spezifizierten Register gewonnen wird;
              b.2) der Abschnitt der Startadresse um eine vorgegebenen Anzahl
              von Bitpositionen verschoben wird.


Zu den Unteransprüchen 2 bis 3 wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 des vierten Hilfsantrags unterscheidet sich vom
Patentanspruch 1 des dritten Hilfsantrags durch Aufnahme der Merkmale e) und
f).


       e)     im Schritt b.1) der Abschnitt der Startadresse eine Mehrzahl von am
              höchsten bewerteten Bits der Startadresse enthält, und
       f)     im Schritt b.2) die vorgegebene Anzahl von Bitpositionen der Anzahl der verbleibenden, am geringsten bewerteten Bits der Startadresse entspricht.


Zu Unteranspruch 2 wird auf die Akte verwiesen.


Der Anmeldung liegt gemäß der Beschreibungseinleitung die Aufgabe zugrunde,
die in der Anmeldung genannten Nachteile einer Cache-Steuerung zu vermeiden
(siehe Beschreibung Seite 3 Z. 16-17).




                                         II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig.

                                        -7-



Sie hat jedoch keinen Erfolg, weil das beanspruchte Verfahren zum Invalidieren
und/oder zum Ausführen einer Flush-Operation eines vorgegebenen Bereichs
eines Cache-Speichers weder in der Fassung nach Hauptantrag noch nach einem
der vier Hilfsanträge auf einer erfinderischen Tätigkeit beruht (§ 4 PatG).


1.    Die vorliegende Patentanmeldung bezieht sich auf ein Verfahren in einem
Computersystem, das, mit Hilfe neuer Befehle, in einem vorgegebenen Abschnitt /
Bereich eine Invalidier- bzw. eine Flush-Operation für eine Mehrzahl von Cache-Zeilen durchführen kann.


Die Verwendung von einem Cache-Speicher, um die Zugriffszeiten des Prozessors auf Daten oder Befehle zu verkürzen, ist bekannt. Der Cache-Speicher befindet sich zwischen dem Prozessor und dem Hauptspeicher und wird durch eine
Cachesteuereinheit bzw. durch einen Cachecontroller gesteuert. In dem Cache-Speicher sind die am häufigsten aufgerufenen Daten gespeichert. Damit wird
erreicht, dass der Prozessor zur Ausführung eines Programms beim Zugriff auf
Daten diese nicht aus dem Hauptspeicher laden bzw. in diesen schreiben muss,
sondern von dem schnelleren Cache-Speicher lädt bzw. in diesen schreibt. Die
Daten im Cache-Speicher sind somit immer aktuell und eine Synchronisierung mit
dem Hauptspeicher ist nur in besonderen Fällen notwendig.


Wenn allerdings andere Systemkomponenten auf den Hauptspeicher zugreifen,
befinden sich unterschiedliche Datenstände im Cache-Speicher und im Hauptspeicher. Dies kann zu Problemen führen, wenn der Prozessor mit den Daten des
Cache-Speichers arbeitet und diese eventuell nicht mehr aktuell sind.


Findet ein solcher Zugriff von anderen Systemkomponenten auf den Hauptspeicher statt, unterscheidet man u. a. folgende zwei Fälle:


        a)     Bei einem Zugriff einer Systemkomponente (z. B. DMA-Controller)
               auf den Hauptspeicher, bei dem die Daten in dem Hauptspeicher

                                       -8-



              überschrieben werden, muss der Cache-Speicher informiert werden, dass die im Cache gehaltenen Daten ungültig sind. Diese
              Daten bzw. Befehle werden dann als ungültig gekennzeichnet. Diesen Vorgang nennt man „Cache-Invalidieren“.


        b)    Wenn ein Cache-Speicher mit einer so genannten Rück-Schreib-Strategie ausgestattet ist, werden die Daten nach der Verarbeitung
              aus dem Prozessor nur in den Cache, nicht aber den Hauptspeicher zurückgeschrieben. Erfolgt dann aber ein Zugriff auf den
              Hauptspeicher von anderen Systemkomponenten, dann müssen
              vorher alle Daten des Cache-Speichers in den Hauptspeicher übertragen werden. Diese Operation nennt sich „Cache-Flush“.


In der Anmeldung ist ausgeführt, dass es für die beiden oben angeführten Operationen bereits bekannte Lösungen gebe. Bei einer Lösung sei vorgesehen, dass
die Befehle in Hardware implementiert sind, damit könne die Invalidierung bzw.
das Flushen nur für eine einzelne Speicherzelle durchgeführt werden. Zum anderen sei eine Softwarelösung für diese Befehle bekannt, bei welcher aber ein Invalidieren bzw. Flushen nur für den gesamten Cache-Speicher durchführbar ist.


Ausgehend von den Alternativen nur eine einzelne Speicherzelle oder aber den
ganzen Speicher zu bearbeiten, setzt sich das vorliegende Patentbegehren das
Ziel, ein Invalidieren bzw. Flushen von vorbestimmten Teilen bzw. von Bereichen
des Cache-Speichers zu ermöglichen.


Die Lösung dieses Problems gemäß dem Hauptanspruch des Hauptantrags
besteht darin, einen neuen Befehl zu schaffen, der eine Invalidier- bzw. eine
Flush-Operation spezifiziert und einen Operanden aufweist (Merkmal a)). Dabei
wird nach dem Dekodieren des Befehls von der Ausführungseinheit aus dem Operanden eine, von einem Benutzer spezifizierte, Startadresse gewonnen (Merk-

                                       -9-



mal b)). Beginnend bei dieser Startadresse wird für jeden Eintrag in dem angegebenen Bereich eine Invalidier- bzw. Flush-Operation ausgeführt (Merkmal c)).


In den Hilfsanträgen werden bestimmte Details weiter ausgebildet.


Gemäß dem Hauptanspruch des ersten Hilfsantrags spezifiziert der Operand des
Befehls ein Register oder einen Speicherplatz, das bzw. der eine Startadresse
enthält (Merkmal a.1)).
Im Hauptanspruch des zweiten Hilfsantrags wird auf eine der zwei Alternativen
des ersten Hilfsantrags verzichtet. Der Operand spezifiziert nur noch ein Register,
welches die Startadresse enthält (Merkmal a.2)).
Nach dem Hauptanspruch des dritten Hilfsantrags wird zum Gewinnen der Startadresse (Merkmal d)) ein Abschnitt der Startadresse aus dem als Operand spezifizierten Register gewonnen, wobei der Abschnitt um eine vorgegebene Anzahl
von Bitpositionen verschoben wird.
Der Hauptanspruch des vierten Hilfsantrags schränkt den dritten Hilfsantrag noch
weiter ein, indem der Abschnitt der Startadresse eine Mehrzahl von am höchsten
bewerteten Bits der Startadresse enthält, und die vorgegebene Anzahl von Bitpositionen, um die der Abschnitt verschoben wird, der Anzahl der verbleibenden, am
geringsten bewerteten Bits der Startadresse entspricht (Merkmale e) und f)).


Als Fachmann, der mit der Aufgabe betraut wird, einen neuen Befehl für die Ausführung von Cache-Operationen zu entwickeln, sieht der Senat einen Diplomingenieur der Elektrotechnik oder einen Informatiker mit Hochschulabschluss an, der
über mehrjährige Berufserfahrung im Bereich der Entwicklung von Befehlssätzen
für Prozessoren verfügt.


2.    Das Verfahren zum Invalidieren und/oder zum Ausführen einer Flush-Operation eines vorgegebenen Bereichs eines Cache-Speichers gemäß Patentanspruch 1 des Hauptantrags beruht nicht auf erfinderischer Tätigkeit.

                                      - 10 -



Von besonderer Bedeutung dafür ist die von der Prüfungsstelle entgegengehaltene Druckschrift:


         D2    EP 0 210 384 A1


2.1.    Druckschrift D2 nimmt die Merkmale des Patentanspruchs 1 nach Hauptantrag weitgehend vorweg.


D2 geht von einem Cache-Speicher aus, der Daten und Befehle enthält, die eine
Kopie eines Teils der Daten und Befehle des Hauptspeichers darstellen. Das in D2
gezeigte System verfügt weiterhin über eine CPU (Prozessor), die für die Steuerung der direkten Speicherzugriffe zum Hauptspeicher und die Steuerung des
Cache-Speichers ausgebildet ist.


Ziel von D2 ist es neue Befehle bzw. Routinen zur Verfügung zu stellen, mit denen
die Übereinstimmung der Daten und Befehle zwischen dem Cache-Speicher und
dem Hauptspeicher gewährleistet wird. Insbesondere soll dadurch die Invalidierung (invalidation) und das Flushen (removal) von Blöcken verbessert werden (vgl.
S.5 Z.5-17).


Zum Erreichen dieses Ziels wird zuerst erläutert, dass die CPU in dem Computersystem Befehle lädt (fetch), Befehle dekodiert (decode) und anschließend die
Befehle ausführt (execute). Dabei werden, während der Ausführung eines Programms, die Daten und Befehle aus dem Hauptspeicher in den Prozessor geladen
und nach Bearbeitung wieder in den Hauptspeicher zurück geschrieben (vgl. S.6
Z.20 - S.7 Z.3). Um die Ausführung zu beschleunigen, ist ein Cache-Speicher vorgesehen. Dazu muss aber der Prozessor über weitere Befehle für die Cache-Steuerung verfügen (vgl. S.9 Z.5-9). Zusätzlich ist in D2 noch ausgeführt, dass der
Cache-Speicher alle Einträge, also Befehle und Daten, in einem gemeinsamen
Speicherbereich (vgl. Fig.2) oder in getrennten Bereichen (vgl. Fig.3) speichern
kann.

                                      - 11 -



Aus der D2 sind damit die Merkmale 1) und a), mit Ausnahme der Vorgabe, dass
die Operation in einem „vorgegebenen Bereich“ ausgeführt werden soll und mit
Ausnahme, dass der Befehl einen Operanden aufweist, vorweggenommen.


Die D2 spezifiziert im Weiteren sechs neue Prozessorbefehle, die zur Steuerung
des Cache-Speichers verwendet werden (vgl. S.9 Z.5 - S.10 Z.16). Mit diesen
Befehlen wird das Betriebssystem angewiesen z. B. ein Invalidieren von Einträgen
oder ein Flushen des Cache-Speichers durchzuführen. Noch detaillierter wird
einerseits beschrieben, wie, im Falle des I/O-Zugriffs auf den Hauptspeicher, ein
Befehl eine Routine ausführt, die auf jeden Eintrag im Cache-Speicher in einem
Bereich (range of addresses) angewandt wird (vgl. S.10 Z.25 - S.11 Z.20). Andererseits ist für eine Rückschreib-Operation ein Flush-Data-Cache für einen
Adressbereich (index range) erläutert, der ein schrittweises (stepping through)
Flushen des Speichers durchführt (vgl. S.12 Z.14-23).


Bei der Ausführung der oben angegebenen Befehle und Routinen beschreibt die
D2 auch, dass die Invalidierung bzw. das Flushen durchgeführt wird, indem das
Status Bit gesetzt wird bzw. indem die Einträge in den Hauptspeicher zurück geschrieben werden (vgl. insbes. Ansprüche 1 - 3, S.11 Z.11-13).


Somit sind aus D2 auch teilweise die Merkmale b) und c) vorweggenommen. In
D2 ist nicht explizit angegeben, dass „eine von einem Benutzer spezifizierte Startadresse“ aus einem „Operanden“ gewonnen wird und dass „beginnend an der
vom Benutzer spezifizierten Startadresse“ die Operation für einen vorgegebenen
Bereich ausgeführt wird.


2.2.   Der Vertreter der Anmelderin weist zu Recht darauf hin, dass sich die Lehre
des Patentanspruchs 1 nach Hauptantrag von der Lehre der D2 in einigen Punkten unterscheidet. Diese Unterschiede vermögen das Vorliegen einer erfinderischen Tätigkeit jedoch nicht zu begründen.

                                          - 12 -



Insbesondere soll eine von einem Benutzer spezifizierte Startadresse unter Verwendung des Operanden des Befehls gewonnen werden. Anschließend wird bei
der Ausführung des Befehls an der vom Benutzer spezifizierten Startadresse mit
der Operation begonnen und die Operation für einen Bereich von Speicherzellen
durchgeführt.


D. h. der von der Anmelderin beanspruchte neue Prozessorbefehl soll einen vorgegebenen Cache-Bereich bearbeiten und dazu einen Operanden enthalten, der
die Startadresse des Bereichs festlegt.


Der strukturelle Aufbau von Prozessorbefehlen und deren Verwendung hat sich
seit der Einführung der ersten Prozessoren bzw. Mikrocontrollern nicht grundlegend verändert. Dem Fachmann, der sich mit Prozessorbefehlen und Befehlssätzen beschäftigt, sind die Grundlagen des Befehlsaufbaus bekannt.


Bei allen Prozessoren sind die Befehle nach der gleichen Struktur aufgebaut. Dieser Aufbau ist dem Fachmann hinlänglich bekannt. Beispielsweise besteht ein einfacher Additionsbefehl aus einem OpCode (Operationscode = Add-Befehl), einem
ersten Operanden und einem zweiten Operanden. Der Benutzer kann in diesem
Fall direkt anschließend an den Befehlscode die Operanden eintragen. Die meisten Befehle enthalten jedoch keine Operanden, sondern verweisen auf Speicheradressen aus denen der Operand geladen wird. Ein derartiger Verweis kann durch
die direkte Angabe einer Adresse oder durch die Angabe eines Registers erfolgen.
Bei einer direkten Angabe der Adresse gibt der Anwender den Befehl (Add),
gefolgt von den Adressen der Summanden, ein. Bei der Registeradressierung
könnte der oben angegebene Additionsbefehl aus einem OpCode und z. B. drei
Registeradressen (R1, R2 und R3) bestehen, in denen die Speicheradressen
abgelegt sind. Bei der Ausführung des Befehls wird aus der Speicherzelle, auf die
die Adresse des ersten Registers verweist, der erste Operand (erste Summand)
geladen und, aus der zweiten Speicherzelle, auf die die Adresse des zweiten
Registers verweist wird der zweite Operand (zweiter Summand) geladen. Das

                                       - 13 -



Ergebnis der Operation wird in die Speicherzelle geschrieben, deren Adresse im
dritten Register angegeben ist.


In Kenntnis dieser Grundlagen ist kein erfinderisches Zutun notwendig, um in einer
Ausführungseinheit aus einem Operanden eines Befehls eine Startadresse zu
gewinnen, deren Daten dann, entsprechend der im Befehl angegebenen Operation, bearbeitet werden. Darüber hinaus ist für den Fachmann auch kein erfinderisches Zutun notwendig, um mit den in D2 angegebenen Ausführungsformen, nach
denen eine Operation mit den Daten in einem spezifischen Bereich des Cache-Speichers ausgeführt wird, zu einer Ausgestaltung zu gelangen, die beginnend bei
einer Startadresse eine Invalidier- bzw. Flushoperation durchführt.


Da der Fachmann aus der D2 bereits die wesentlichen Merkmale des geltenden
Hauptanspruchs nach Hauptantrag entnehmen konnte, musste er, um zur Lösung
des gegebenen Problems zu gelangen, allenfalls in einigen Details Änderungen
mit bekannten Mitteln vornehmen. Das erforderte übliches fachmännisches Überlegen und Handeln, jedoch keine erfinderische Tätigkeit.


3.     Mit dem Patentanspruch 1 fallen auch die Unteransprüche 2 bis 4, da über
einen Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120
- Elektrisches Speicherheizgerät).


4.     Die vier Hilfsanträge sind nicht anders zu bewerten.


Im Folgenden wird, zur Vermeidung von Wiederholungen, lediglich auf die Merkmale eingegangen, die sich von den Merkmalen der bereits behandelten Anträge
unterscheiden.


4.1.   Der Hauptanspruch des ersten Hilfsantrags gibt an, dass der Operand ein
Register oder einen Speicherplatz spezifiziert, das bzw. der eine Startadresse enthält. Wie bereits unter 2.2. ausgeführt, sind in dem Befehlssatz eines nahezu

                                       - 14 -



jeden Prozessors Befehle verfügbar, die eine Registeradressierung ermöglichen.
Die Registeradressierung ist üblich und dem Fachmann vertraut. Diese bei neuen
Befehlen einzusetzen, ist selbstverständlich und erfordert keine erfinderische
Tätigkeit.


Somit gelangt der Fachmann in Kenntnis der D2 und unter Zuhilfenahme seines
Wissens ohne erfinderisches Zutun zum Gegenstand des Hauptanspruchs des
ersten Hilfsantrags.


Mit dem Patentanspruch 1 fallen auch die Unteransprüche 2 bis 4 des ersten Hilfsantrags, da über einen Antrag nur einheitlich entschieden werden kann.


4.2.   Im Hauptanspruch des zweiten Hilfsantrags entfällt das Merkmal, nach dem
der Operand einen Speicherplatz spezifiziert. Der Anspruch bezieht sich nur noch
auf die Verwendung eines Operanden, der ein Register spezifiziert, welches eine
Startadresse enthält. Damit ist der Hauptanspruch des zweiten Hilfsantrags aus
den unter 4.1. dargelegten Gründen ebenfalls nicht gewährbar. Auch fallen mit
dem Hauptanspruch die Unteransprüche 2 bis 4.


4.3.   Gemäß dem Hauptanspruch des dritten Hilfsantrags wird zum Gewinnen
der Startadresse ein Abschnitt der Startadresse aus einem in dem dekodierten
Befehl spezifizierten Register gewonnen und der Abschnitt der Startadresse um
eine vorgegebenen Anzahl von Bitpositionen verschoben.


Dem Fachmann sind verschiedene Arten der Adressierung, wie bspw. eine Registeradressierung, bekannt. In diesem Zusammenhang sind aber auch Befehle
bekannt, die eine Adressierung von längeren Speicheradressen ermöglichen. Derartige Befehle wurden aufgrund der stetig wachsenden Speicherkapazitäten und
der damit einhergehenden größeren Adressräume notwendig. Um in einem großen Speicher alle Speicherzellen adressieren zu können, wurden verschiedene
Verfahren entwickelt. Einerseits gibt es die Möglichkeit in einem Register lediglich

                                       - 15 -



einen Abschnitt des Speichers zu adressieren. Die Daten in dem Register geben
dann die höherwertigen Bits an (msb = most signifikant bits), wobei dann für einen
Zugriff auf eine Speicherzelle oder auf einen Speicherbereich die fehlenden Bits,
je nach Befehlssatz, mit Null oder Eins ergänzt werden. Andererseits ist es bekannt in einem Befehl, wie oben bereits erläutert, mehrere Register anzugeben.
Dies bedeutet, dass in einem Befehl nach dem OpCode ein erstes Register bspw.
die 8 höchsten Bits, ein zweites Register die 8 niedrigsten Bits der Adresse enthalten kann. Bei der Ausführung des Befehls werden die Bits des ersten Registers
eingelesen, um 8 Stellen nach links verschoben und anschließend die Bits des
zweiten Registers angehängt. Ein solches Vorgehen ist bei einem 8-Bit-Prozessor,
der auf einen Speicher mit einem 16 Bit großen Adressraum zugreift üblich. Dem
Fachmann sind diese Arten der Adressierung vertraut. Es kann keine erfinderische
Tätigkeit darin gesehen werden, sie auf neue Befehle anzuwenden.


Der Hauptanspruch des dritten Hilfsantrags beruht somit ebenfalls auf keiner erfinderischen Tätigkeit, da in Kenntnis der D2 allenfalls fachmännische Überlegungen
notwendig waren, um zu dessen Gegenstand zu gelangen.


Die Unteransprüche 2 und 3 fallen auch hier mit dem Hauptanspruch, da über
einen Antrag nur einheitlich entschieden werden kann.


4.4.   Nach dem Hauptanspruch des vierten Hilfsantrags enthält der Abschnitt der
Startadresse eine Mehrzahl von am höchsten bewerteten Bits; die vorgegebene
Anzahl von Bitpositionen, um die die am höchsten bewerteten Bits verschoben
werden, entspricht der Anzahl der verbleibenden, am geringsten bewerteten Bits
der Startadresse.
Eine Adressierung eines Speichers, bei der eine Verschiebung der höherwertigen
Bits um eine bestimmte Anzahl von Stellen notwendig ist, wurde bereits unter 4.3.
dargestellt.

                                       - 16 -



Somit gelangt der Fachmann aufgrund seines Fachwissens und der Lehre der D2
auch zum Gegenstand des Hautpanspruchs des vierten Hilfsantrags. Der Hauptanspruch gemäß dem vierten Hilfsantrag beruht demnach ebenso auf keiner erfinderischen Tätigkeit.


Auch der Unteranspruch 2 fällt mit dem Hauptanspruch, da über den Antrag nur
einheitlich entschieden werden kann.


5.     Nachdem keiner der gestellten Anträge Erfolg haben kann, war die Beschwerde der Anmelderin gegen den Beschluss der Prüfungsstelle zurückzuweisen.




                                        III.


Die Rückzahlung der Beschwerdegebühr entspricht der Billigkeit.


Wie der Senat bereits mehrfach festgestellt hat, stellt die Ablehnung einer von der
Anmelderin beantragten Anhörung in der Regel einen Verfahrensfehler dar.
Im vorliegenden Fall wurde die beantragte Anhörung von der Prüfungsstelle mit
der Begründung abgelehnt, dass die Sache ausreichend diskutiert wurde, sich
gefestigte, gegenüberstehende Standpunkte gebildet hätten und der Anmelderin
ausreichend rechtliches Gehör gewährt worden wäre.
Die Anmelderin hat auf jeden Bescheid der Prüfungsstelle reagiert. Insbesondere
hat sie auf den letzten Bescheid der Prüfungsstelle, mit dem auch eine neue
Druckschrift in das Verfahren eingeführt wurde, neue Ansprüche gemäß Hauptund Hilfsantrag eingereicht und, wie auch in den vorangegangenen Erwiderungen,
eine Anhörung beantragt. Eine mangelnde Bereitschaft der Anmelderin an einer
konstruktiven Gestaltung des Verfahrens ist nicht zu erkennen. Gerade im Hinblick
auf den neuen Sachverhalt wäre eine Anhörung für das Verfahren förderlich gewesen.

                                    - 17 -



Aus diesen Gründen entspricht es der Billigkeit, die Beschwerdegebühr zurückzuzahlen.




Dr. Morawek               Eder               Baumgardt              Hoffmann




                                                                            Fa
