---
ecli: "ECLI:DE:BPatG:2002:170702U4Ni38.00.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 38/00"
decided: "2002-07-17"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2002&Sort=1&Seite=67&nr=16394&anz=1911&pos=1011&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2002-07-17_4_Ni_38_00_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0263.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 38/00 vom 2002-07-17

## Entscheidung

BUNDESPATENTGERICHT


                    IM NAMEN DES VOLKES


                              URTEIL                 Verkündet am
                                                     17. Juli 2002
  4 Ni 38/00                                              …

(Aktenzeichen)


                    In der Patentnichtigkeitssache


…




BPatG 253
9.72

                                       -2-



                     betreffend das deutsche Patent 31 19 669


hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 17. Juli 2002 unter Mitwirkung des Vorsitzenden
Richters Dr. Schwendy, der Richter Dipl.-Ing. Obermayer, Dipl.-Phys. Kalkoff, der
Richterin Schuster und des Richters Dipl.-Phys. Dr. Hartung


für Recht erkannt:


         1. Die Klage wird abgewiesen.
         2. Die Klägerin trägt die Kosten des Rechtsstreits.
         3. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 %
             des zu vollstreckenden Betrages vorläufig vollstreckbar.


                                   Tatbestand


Die Beklagte ist eingetragene Inhaberin des am 18. Mai 1981 angemeldeten, inzwischen durch Zeitablauf erloschenen deutschen Patents 31 19 669 (Streitpatent), das die Unionspriorität der japanischen Patentanmeldung JP 67608-80 vom
21. Mai 1980 in Anspruch nimmt. Das Streitpatent betrifft ein "Verfahren zur Fehlersicherung einer Folge von Datenwörtern, Anordnung zum Bilden von fehlergesicherten Datenwörtern gemäß dem Verfahren, Anordnung zum Decodieren von gemäß dem Verfahren fehlergesicherten Datenwörtern und Datenträger mit gemäß
dem Verfahren erzeugten fehlergesicherten Datenwörtern" und umfaßt 16 Patentansprüche. Die nebengeordneten Patentansprüche 1, 8, 10, und 15 haben folgenden Wortlaut:


        "1. Verfahren zur Fehlersicherung einer Folge von Datenwörtern, bei dem
            a) an jedem einer ersten Anzahl von (n1 - k1) parallelen
                Kanälen je ein Datenwort der Folge in einer ersten zeitlichen Zuordnung zueinander empfangen wird,

                                 -3-



    b) jeweils ein Datenwort eines jeden Kanals einem ersten
          Fehlerkorrekturcoder zugeführt wird zum Bilden wenigstens eines ersten Paritätsworts,
    c) die Datenwörter nach dem Zuführen zum ersten Fehlerkorrekturcoder und jedes daraus gebildete Paritätswort
          um wortweise unterschiedliche Laufzeiten verzögert
          werden zum Bilden einer zweiten zeitlichen Zuordnung
          zueinander,
    d) jeweils ein Datenwort jedes Kanals und ein Paritätswort
          in der zweiten zeitlichen Zuordnung zueinander einem
          zweiten Fehlerkorrekturcoder zugeführt wird zum Bilden
          wenigstens eines zweiten Paritätswort,
    e) jeweils ein Datenwort aus jedem Kanal sowie die zugehörige Anzahl erster und zweiter Paritätswörter in einer
          Anzahl, die gleich der Summe der ersten Anzahl und
          der Anzahl der zusammen gebildeten ersten und zweiten Paritätswörter ist, von Ausgangskanälen wortweise
          seriell anfällt,
dadurch gekennzeichnet, daß vom ersten Fehlerkorrekturcoder
zu den der ersten Anzahl von (n1 - k1) Kanälen zugeführten
Datenwörtern jeweils eine Reihe von k1 > 2 ersten Paritätswörtern derart gebildet werden, daß die Datenwörter und die ersten
Paritätswörter einen fehlerkorrigierbaren Block von n1 Wörtern
bilden,
daß vom zweiten Fehlerkorrekturcoder zu den der ersten Anzahl von (n1 - k1) Kanälen zugeführten Datenwörtern und der
dazu gebildeten Reihe von k1 ersten Paritätswörtern jeweils eine weitere Reihe von k2 > 2 zweiten Paritätswörtern derart gebildet werden, daß die Datenwörter, die Reihe erster Paritätswörter und die Reihe zweiter Paritätswörter einen weiteren fehlerkorrigierbaren Block von n1 + k2 = n2 Wörtern bilden,

                                                      -4-



 daß die Erzeugung von k1 ersten bzw. k2 zweiten Paritätswörtern zur Bildung des jeweiligen fehlerkorrigierbaren Blocks von
 n1 bzw. n2 Wörtern mittels der nachfolgenden Paritätsfehlermatrix erfolgt, wobei n2 < 2mist:


    ⎡1            1             1         −−−−− 1                                1         ⎤
    ⎢ 1                                   − − − − − α π −1                                 ⎥
    ⎢α            α2            α3                                               απ        ⎥
    ⎢α 2          α4            α6        − − − − − α 2(π −1)                    α 2π ⎥
    ⎢                                                                                      ⎥
H = ⎢.            .             .         .                  .                   .         ⎥
    ⎢.            .             .         .                  .                   .         ⎥
    ⎢                                                                                      ⎥
    ⎢.            .             .         .                  .                   .         ⎥
    ⎢α κ −1       α (κ −1)2 α (κ −1)3     −−−−−              α (κ −1)(π −1)      α (κ −1)π ⎥
    ⎣                                                                                      ⎦


 oder


    ⎡1   1             1             −−−−− 1                          1             ⎤
    ⎢1                               −−−−− α          π −2                π −1      ⎥
    ⎢     α   1
                       α   2
                                                                      α             ⎥
    ⎢1    α2           α4            − − − − − α 2(π −2 )             α 2 (π −1) ⎥
    ⎢                                                                               ⎥
H = ⎢.    .            .             .         .                      .             ⎥
    ⎢.    .            .             .            .                   .             ⎥
    ⎢                                                                               ⎥
    ⎢.    .            .             .            .                   .             ⎥
    ⎢1        κ −1         (κ −1)2   − − − − − α (κ −1)(π −1)           (κ −1)(π −1)⎥
    ⎣     α            α                                              α             ⎦


 wobei α eine Wurzel entsprechend F(x)=0 ist, wobei F(x) ein
 unzerlegbares und primitives Polynom des nten Grades über einen Galois-Körper GF(2) ist, und daß empfangsseitig zum Decodieren derartig fehlergesicherter Daten das Verfahren entsprechend umgekehrt angewendet wird.


 8. Anordnung zum Bilden von fehlergesicherten Datenwörtern
      gemäß dem Verfahren nach einem der Ansprüche 1 bis 7
      mit einem ersten Fehlerkorrekturcoder zur Erzeugung mindestens eines ersten Paritätsworts aus jeweils mehreren

                                                            -5-



      über eine Anzahl Datenkanäle parallel zugeführten Datenwörtern, mit mehreren parallelen ersten Verzögerungsanordnungen unterschiedlicher Verzögerungszeit, die wenigstens einen Teil der parallel zugeführten Datenwörter und
      die ersten Paritätswörter empfangen und einem zweiten
      Fehlerkorrekturcoder zur Erzeugung wenigstens eines
      zweiten Paritätsworts zuführen, dadurch gekennzeichnet,
      daß die Fehlerkorrekturcoder derart aufgebaut sind, daß jeder von diesen k1 bzw. k2 Paritätswörter mittels der nachfolgenden Paritätsfehlermatrix erzeugt


    ⎡1            1               1            −−−−− 1                               1         ⎤
    ⎢ 1                                        −−−−− α                 π −1              π     ⎥
    ⎢α            α               α                                                  α
                      2               3
                                                                                               ⎥
    ⎢α 2          α4              α6           − − − − − α 2(π −1)                   α 2π ⎥
    ⎢                                                                                          ⎥
H = ⎢.            .               .            .         .                           .         ⎥
    ⎢.            .               .            .                   .                 .         ⎥
    ⎢                                                                                          ⎥
    ⎢.            .               .            .                   .                 .         ⎥
    ⎢α κ −1                                                                            (κ −1)π ⎥
    ⎣             α (κ −1)2 α (κ −1)3          − − − − − α (κ −1)(π −1)              α         ⎦


 oder


    ⎡1   1                1               −−−−− 1                             1             ⎤
    ⎢1                                    −−−−− α           π −2                  π −1      ⎥
    ⎢    α    1
                          α   2
                                                                              α             ⎥
    ⎢1   α2               α4              − − − − − α 2(π − 2 )               α 2 (π −1) ⎥
    ⎢                                                                                       ⎥
H = ⎢.   .                .               .         .                         .             ⎥
    ⎢.   .                .               .             .                     .             ⎥
    ⎢                                                                                       ⎥
    ⎢.   .                .               .             .                     .             ⎥
    ⎢1                                                                          (κ −1)(π −1)⎥
    ⎣    α κ −1 α (κ −1)2                 − − − − − α (κ −1)(π − 2 )          α             ⎦


      wobei α eine Wurzel entsprechend F(x)=0 ist mit F(x) gleich
      einem unzerlegbaren und primitiven Polynom des nten Grades über einen Galois-Körper GF(2), wobei die parallel zugeführten Datenwörter und die daraus erzeugten Paritäts-

                              -6-



   wörter zusammen jeweils einen fehlerkorrigierbaren Block
   von n1 bzw. n2 Wörtern bilden.


10. Anordnung zum Decodieren von gemäß dem Verfahren
   nach einem der Ansprüche 1 bis 7 fehlergesicherten Datenwörtern mit Verzögerungsanordnungen und Fehlerkorrekturschaltungen, dadurch gekennzeichnet, daß die Fehlerkorrekturschaltungen einen ersten Decoder, der eine erste
   Anzahl Datenwörter und die zugehörigen ersten und zweiten Paritätswörter parallel erhält und unter Steuerung der
   zweiten Paritätswörter mittels eines darin gebildeten Syndroms einen Block von fehlerkorrigierbaren Datenwörtern
   mit den zugehörigen ersten Paritätswörtern an eine Anzahl
   paralleler Verzögerungsanordnungen mit unterschiedlichen
   Verzögerungszeiten abgibt, und einen zweiten Decoder umfassen, der die von den Verzögerungsanordnungen abgegebenen Datenwörter und ersten Paritätswörter empfängt
   und unter Steuerung der letzteren mittels eines in diesem
   zweiten Decoder gebildeten zweiten Syndroms fehlerkorrigierte Datenwörter abgibt, die eine Folge von Datenwörtern
   bilden.


15. Datenträger mit gemäß dem Verfahren nach einem der Ansprüche 1 bis 7 erzeugten fehlergesicherten Datenwörtern
   in Form von Datenblöcken, dadurch gekennzeichnet, daß
   jeder Block eine aus den geradzahligen der den parallelen
   Kanälen zugeführten Datenwörter abgeleitete Information,
   eine aus den ersten Paritätswörtern abgeleitete Information,
   eine aus den ungeradzahligen der den parallelen Kanälen
   zugeführten Datenwörter abgeleitete Information und eine
   aus den zweiten Paritätswörtern abgeleitete Information
   enthält."

                                       -7-



Wegen der unmittelbar und mittelbar auf die zitierten Nebenansprüche zurückbezogenen Unteransprüche wird auf die Streitpatentschrift verwiesen.


Die Klägerin, die zunächst nur die Patentansprüche 15 und 16, später das Patent
in vollem Umfang angegriffen hat, behauptet, die Lehre des Streitpatents sei nicht
ausführbar, sei nicht neu bzw. beruhe nicht auf einer erfinderischen Tätigkeit. Die
Ansprüche 15 und 16 gäben i.S.v. § 1 Abs. 2 Nr. 4 PatG nur Informationen wieder;
der Gegenstand des Anspruchs 15 gehe zudem über den Inhalt der ursprünglichen Anmeldung hinaus. Zur Begründung beruft sie sich auf folgende Druckschriften:


        -    Lexikon der Fabrikorganisation und Fördertechnik 1971,
             Bd. 15, S. 102 f (N2)
        -    DE 29 10 390 C2 (N3)
        -    DE 29 12 216 C2 (N4)
        -    DE 29 35 789 C2 (N5)
        -    Toshi T. Doi et. al., "A Long Play Digital Audio Disc System2,   62nd    AES-Convention,      March 1979,     Brussels,
             Belgium (N9)
        -    G.D. Forney, 2Concatenated Codes", Research Monograph    No. 37,    The     M.I.T.     Press,      Cambridge,
             Massachusetts, 1966, S. 21, 26 bis 29, 100 bis 105, 134
             bis 142 (N10)
        sowie auf:
        -    DE 29 16 102 A1
        -    E.R. Berlekamp, "Algebraic Coding Theory", McGraw-Hill
             Book Comp. 1968, S. 347 bis 349.


Die Klägerin beantragt,


        das deutsche Patent 31 19 669 für nichtig zu erklären.

                                       -8-



Die Beklagte beantragt,


       die Klage abzuweisen.


Sie ist dem Vorbringen der Klägerin - auch der Klageerweiterung hinsichtlich der
Ansprüche 1 bis 14 - entgegengetreten und hält das Streitpatent für bestandsfähig.
                             Entscheidungsgründe


Die Klage, mit der die in § 22 Abs 2 iVm § 21 Abs 1 Nr 1, 2 und 3 PatG vorgesehenen Nichtigkeitsgründe der mangelnden Patentfähigkeit, der mangelnden Ausführbarkeit und der unzulässigen Änderung geltend gemacht werden, ist zulässig
aber nicht begründet.


1. Die Schutzdauer des Patents ist zwar am 18. Mai 2001 abgelaufen. In Anbetracht des vor dem LG Hamburg anhängigen Verletzungsstreitverfahrens ist aber
das Rechtsschutzbedürfnis der Klägerin im vorliegenden Verfahren hinsichtlich
des gesamten Patents gegeben, auch wenn sie derzeit im Verletzungsstreit nur
aus einzelnen Patentansprüchen in Anspruch genommen wird (vgl Busse, Patentgesetz, 5. Aufl, § 81 Rn 53 mNachw).


2. Die mit der Erweiterung der Klage auf das gesamte Patent, also auch auf den
anfangs nicht angegriffenen Anspruch 1, vorgenommene Klageänderung hält der
Senat gemäß § 99 PatG iVm § 263 ZPO für sachdienlich, da sich durch sie der
Prozessstoff nicht wesentlich ändert und ein weiterer Rechtsstreit vermieden wird
(vgl Busse aaO § 83 Rn 7-9; Zöller, Zivilprozessordnung, 22. Aufl § 263 Rn 13;
BPatGE 33, 240 - Parteiwechsel).


3. Das Streitpatent betrifft ein Verfahren zur Fehlersicherung einer Folge von Datenwörtern, eine Anordnung zur Bildung und eine Anordnung zum Decodieren derart fehlergesicherter Datenwörter sowie einen Datenträger mit derart fehlergesicherten Datenwörtern. Nach der Patentbeschreibung ist im Stand der Technik ein

                                           -9-



Verfahren bekannt, bei dem aus jeweils zwei Datenwörtern ein Paritätswort und
aus dem verzögerten Datenwort und dem unterschiedlich dazu verzögerten Paritätswort ein weiteres Paritätswort gebildet werde. Das eine Datenwort werde dabei
nicht verzögert, was als Verzögerung um die Laufzeit Null angesehen werden könne. Die unterschiedlichen Verzögerungen stellten eine Verflechtung im Zeitbereich
dar. Dies führe zu einer Verringerung der Anzahl fehlerhafter Wörter in einem Fehlerkorrekturblock dadurch, dass die im Fehlerkorrekturblock enthaltenen Paritätswörter und die Datenwörter für die Fehlersicherung zeitlich gestreut und bei der
Decodierung wieder in die ursprüngliche Zeitlage zurückgebracht würden. Dadurch würden beim Auftreten einer Fehlerhäufung zwischen der Erzeugung der
fehlergesicherten Datenwörter und deren Decodierung die fehlerhaften Wörter
zeitlich gestreut. Dadurch sei eine Fehlerkorrektur wenn nicht durch die ersten, so
oft doch durch die zweiten Paritätswörter möglich und umgekehrt. Wenn jedoch
beim bekannten Verfahren ein Wort nur ein einziges fehlerhaftes Bit enthalte, werde das gesamte Wort als fehlerhaft behandelt. Dadurch ermögliche die bekannte
Verflechtung im Zeitbereich nicht immer eine ausreichende Fehlerkorrektur, wenn
die zu decodierenden Daten eine größere Anzahl einzelner Fehler enthielten.


Vor diesem Hintergrund formuliert die Streitpatentschrift die Aufgabe, ein Verfahren der eingangs genannten Art anzugeben, bei dem sowohl Fehlerhäufungen als
auch Einzelfehler gut korrigierbar sind.


Patentanspruch 1 beschreibt demgemäß ein Verfahren zur Fehlersicherung einer Folge von Datenwörtern, bei dem
        a) an jedem einer ersten Anzahl (n1-k1) parallelen Kanälen je
            ein Datenwort der Folge in einer ersten zeitlichen Zuordnung zueinander empfangen wird,
        b) jeweils ein Datenwort eines jeden Kanals einem ersten
            Fehlerkorrekturcoder zugeführt wird zum Bilden wenigstens
            eines ersten Paritätsworts,

                              - 10 -



c)   die Datenwörter nach dem Zuführen zum ersten Fehlerkorrekturcoder und jedes daraus gebildete Paritätswort
     um wortweise unterschiedliche Laufzeiten verzögert werden zum Bilden einer zweiten zeitlichen Zuordnung zueinander,
d)   jeweils ein Datenwort jedes Kanals und ein Paritätswort in
     der zweiten zeitlichen Zuordnung zueinander einem zweiten Fehlerkorrekturcoder zugeführt wird zum Bilden wenigstens eines zweiten Paritätsworts,
e)   jeweils ein Datenwort aus jedem Kanal sowie die zugehörige Anzahl erster und zweiter Paritätswörter in einer Anzahl, die gleich der Summe der ersten Anzahl und der Anzahl der zusammen gebildeten ersten und zweiten Paritätswörter ist, von Ausgangskanälen wortweise seriell anfällt,
f)   vom ersten Fehlerkorrekturcoder zu den der ersten Anzahl
     von (n1-k1) Kanälen zugeführten Datenwörtern jeweils eine Reihe von k1 > 2 ersten Paritätswörtern derart gebildet
     werden, daß die Datenwörter und die ersten Paritätswörter einen fehlerkorrigierbaren Block von n1 Wörtern bilden,
g)   vom zweiten Fehlerkorrekturcoder zu den der ersten Anzahl von (n1-k1) Kanälen zugeführten Datenwörtern und
     der dazu gebildeten Reihe von k1 ersten Paritätswörtern
     jeweils eine weitere Reihe von k2 > 2 zweiten Paritätswörtern derart gebildet werden, daß die Datenwörter, die Reihe erster Paritätswörter und die Reihe zweiter Paritätswörter einen weiteren fehlerkorrigierbaren Block von n1+k2 =
     n2 Wörtern bilden,

                                                     - 11 -



h)   die Erzeugung der Reihen von k1 ersten bzw k2 zweiten
     Paritätswörtern zur Bildung der jeweiligen fehlerkorrigierbaren Blocks von n1 bzw n2 Wörtern mittels der nachfolgenden Paritätsfehlermatrix erfolgt, wobei n2 < 2mist:


         ⎡1            1              1              −−−−− 1                            1         ⎤
         ⎢ 1                                         − − − − − α π −1                             ⎥
         ⎢α            α2             α3                                                απ        ⎥
         ⎢α 2          α4             α6             − − − − − α 2(π −1)                α 2π ⎥
         ⎢                                                                                        ⎥
i)   H = ⎢.            .              .              .         .                        .         ⎥
         ⎢.            .              .              .                   .              .         ⎥
         ⎢                                                                                        ⎥
         ⎢.            .              .              .                   .              .         ⎥
         ⎢α κ −1           (κ −1)2         (κ −1)3   − − − − − α (κ −1)(π −1)             (κ −1)π ⎥
         ⎣             α              α                                                 α         ⎦


     oder


         ⎡1   1              1                −−−−− 1                        1             ⎤
         ⎢1                                  −−−−− α              π −2           π −1      ⎥
         ⎢     α   1
                             α   2
                                                                             α             ⎥
         ⎢1    α2            α4              − − − − − α 2(π −2 )            α 2 (π −1) ⎥
         ⎢                                                                                 ⎥
j)   H = ⎢.    .             .               .         .                     .             ⎥
         ⎢.    .             .               .                .              .             ⎥
         ⎢                                                                                 ⎥
         ⎢.    .             .               .                .              .             ⎥
         ⎢1        κ −1          (κ −1)2      − − − − − α (κ −1)(π −1)         (κ −1)(π −1)⎥
         ⎣     α             α                                               α             ⎦


k)   wobei α eine Wurzel entsprechend F(x)=0 ist, wobei F(x)
     ein unzerlegbares und primitives Polynom des nten Grades über einen Galois-Körper GF(2) ist,
l)   und wobei empfangsseitig zum Decodieren derartig fehlergesicherter Daten das Verfahren entsprechend umgekehrt
     angewendet wird.

                                       - 12 -



4. Zum Patentanspruch 1
Der Patentanspruch 1 ist rechtsbeständig. Der von der Klägerin geltend gemachte
Widerrufsgrund der mangelnden Patentfähigkeit steht ihm nicht entgegen. Der
Fachmann - hier ein Entwickler mit nachrichtentechnischer Hoch- oder Fachhochschulausbildung und mit mehrjährigen Erfahrungen auf dem Gebiet der digitalen
Fehlerkodierung - konnte den Anspruchsgegenstand aus dem entgegengehaltenen Stand der Technik weder entnehmen, noch konnte er ihn, ohne erfinderisch
tätig werden zu müssen, daraus ableiten.


Vorab ist festzustellen, daß Anspruch 1, wie für den Fachmann klar ersichtlich ist
und von den Parteien nicht bestritten wird, so zu verstehen ist, daß es sich im
Merkmal k) um ein Polynom des mten Grades, nicht nten Grades handelt, vergleiche dazu in der ursprünglichen Anmeldung Seite 3 Zeile 21 sowie in der Patentschrift Seite 2 Zeile 47, 48 und Seite 8 Zeilen 34 bis 36. Gleiches gilt für das entsprechende Merkmal des Anspruchs 8.


Die Neuheit des beanspruchten Verfahrens ist schon dadurch gegeben, daß keine
der entgegengehaltenen Druckschriften ein Fehlersicherungsverfahren mit den
Paritätsfehlermatrizen gemäß Merkmalen i) und j) des Anspruchs 1 zeigt.


Das beanspruchte Verfahren beruht auch auf erfinderischer Tätigkeit.


Zum Oberbegriff des Anspruchs 1 nennt die Klägerin - außer der schon im Prüfungsverfahren berücksichtigten DE 29 16 102 A1 - die Druckschrift N9. Gemäß
der dortigen Figur 5 werden an zwei parallelen Kanälen L und R Folgen von Datenwörtern Li, Ri empfangen, und aus diesen wird in insgesamt drei Codern P, Q
und CRCC je ein Paritätswort Pi, Qi und CRC gebildet. Zwei Datenwörter und drei
Paritätswörter bilden jeweils einen fehlerkorrigierbaren Unterblock, vergleiche dazu die Darstellung eines Frame oberhalb der Figur 5. Zwischen den Codern P und
Q sowie zwischen den Codern Q und CRCC befinden sich jeweils Verzögerungsstrecken, mit denen die Datenwörter und die Paritätswörter um wortweise unter-

                                       - 13 -



schiedliche Laufzeiten verzögert werden, so daß sie jedem der Coder in einer unterschiedlichen zeitlichen Zuordnung zueinander zugeführt werden.


Bei den dortigen Codern handelt es sich um Modulo-2-Addierer bzw um einen
CRC-Coder. Jeder dieser Coder ist für sich lediglich zur Fehleranzeige geeignet;
eine Fehlerkorrektur wird erst durch die Kombination der Paritätswörter mindestens zweier Coder ermöglicht, wie dort zB aus Abschnitt 4-2. auf Seiten 5 und 6
sowie auch aus dem dann folgenden Abschnitt 4-3. hervorgeht.


Um von diesem Stand der Technik zum anspruchsgemäßen Verfahren zu gelangen, mußte der Fachmann eine Reihe von Überlegungen anstellen.


Zunächst mußte er - etwa um die Fehlerkorrektur zu verbessern - andere Fehlerkorrekturcodes in Betracht ziehen und dabei für jeden von zwei aufeinanderfolgenden Codern einen Reed-Solomon-Code (abgekürzt RS-Code) auswählen.


Schon diese Überlegung lag dem Fachmann nicht ohne weiteres nahe. Sie beinhaltete nämlich ein Übergehen von den in N9 gezeigten, einfach aufgebauten binären Codern, die für sich nur fehleranzeigend, nicht aber fehlerkorrigierend sind,
zu kompliziert aufgebauten nicht-binären Codern, die je für sich fehlerkorrigierend
sind, nämlich jeweils einen fehlerkorrigierbaren Block bilden (Merkmale f) und g)
des Anspruchs 1). Zudem entnahm er aus dem Stand der Technik nach N10 lediglich miteinander verkettete RS-Coder (dort S 100 und 101), nicht aber RS-Coder,
die über eine zeitliche Verschachtelungseinrichtung miteinander verbunden sind.


Weiterhin mußte der Fachmann für die beiden aufeinanderfolgenden RS-Coder
Paritätsfehlermatrizen bilden, wie sie im Anspruch 1 aufgeführt sind.


Die Klägerin hat diesbezüglich auf N10 verwiesen und dargelegt, daß die anspruchsgemäßen Paritätsfehlermatrizen aus der dortigen allgemeinen Definitionsgleichung (2.2) für RS-Codes auf Seite 21 ableitbar sind.

                                                       - 14 -



Dies ist zwar zutreffend; jedoch hatte der Fachmann auch dabei eine Reihe gedanklicher Schritte zu vollziehen.


So mußte er in der erwähnten Definitionsgleichung (2.2), in der mo eine beliebige
ganze Zahl sein soll, den Fall mo=0 auswählen. Dadurch gelangte er zu einer Gleichung, die in Matrix-Schreibweise folgendermaßen lautet:


⎛ 1         1          1        ...   1 ⎞         ⎛ f1 ⎞
⎜                                             ⎟   ⎜ ⎟
⎜ Z1        Z2         Z3       ...  Zn ⎟         ⎜ f2 ⎟
⎜ .           .          .             . ⎟        ⎜ . ⎟
⎜                                             ⎟   ⎜ ⎟ =o
⎜ .           .          .             . ⎟        ⎜ . ⎟
⎜ .           .          .             . ⎟⎟       ⎜ . ⎟
⎜                                                 ⎜ ⎟
⎜ Z d −2   Z 2d − 2   Z 3d −2   ... Z nd − 2 ⎟⎠   ⎜f ⎟
⎝ 1                                               ⎝ n⎠


Die Zi (i= 1,...,n) sollen gemäß den beiden auf Gleichung (2.2) folgenden Zeilen
sowie gemäß Seite 26 4. Absatz voneinander verschiedene Elemente des
Galois-Feldes GF(q) mit q= 2m sein.


Weiterhin war es nun erforderlich, in der vorstehenden Paritätsfehlermatrix die
Elemente Zi durch verschiedene Potenzen einer Wurzel                      eines primitiven Polynoms F(x) darzustellen und die Potenzen von                     in jeder Zeile der Matrix ansteigend anzuordnen, dh Zi= i (i=1,..., n) zu setzen, um so zu einer Matrix gemäß der
ersten Alternative i) des Anspruchs 1 zu gelangen. Dabei war von den d-Werten
auf k-Werte gemäß d=k + 1 überzugehen. Zwar war dem Fachmann eine derartige
Potenzdarstellung der Elemente eines Galois-Feldes geläufig; die Wahl der Potenzdarstellung und die Anordnung nach in Zeilenrichtung ansteigenden Potenzen
war aber jedenfalls nicht zwangsläufig.


Schließlich mußte der Fachmann vorsehen, daß die Matrix für jeden der beiden
Coder in gleichartiger Weise unter Verwendung derselben Wurzel , dh mit demselben Alphabet, aufgebaut wird.

                                       - 15 -



Zum Auffinden der zweiten Alternative gemäß Merkmal j) des Anspruchs 1 war
dann zusätzlich noch eine Umformung der Matrix unter Ausnutzung der zyklischen
Eigenschaft des RS-Codes erforderlich, wie die Klägerin im einzelnen auf Seite 16
ihres Schriftsatzes vom 18. April 2001 zutreffend dargelegt hat.
Aus den Druckschriften DE 29 16 102 A1 und Berlekamp konnte der Fachmann
keine über den oben behandelnten Stand der Technik hinausgehenden Gesichtspunkte entnehmen. DE 29 16 102 A1 zeigt in Figuren 1 und 7 Fehlerkorrekturschaltungen, bei denen ähnlich wie nach N9 Codierer in Form von Modulo-2-Addierern eingesetzt werden. Berlekamp zeigt in Figur 14.5 zwei verkettete Coder,
von denen der äußere ein RS-Coder sein kann.


Nach Überzeugung des Senats hat jedenfalls die Gesamtheit der oben dargelegten, vom Stand der Technik zum beanspruchten Verfahren führenden, aufeinander
aufbauenden Schritte erfinderische Tätigkeit des Fachmanns erfordert. Dabei hat
der Senat als Indiz für erfinderische Tätigkeit berücksichtigt, daß ein anspruchsgemäßes Fehlerkorrekturverfahren zum Standard für die Compact Disc (CD) geworden ist (DIN-Norm EN 60908) und wesentlich zu dem weltweiten wirtschaftlichen
Erfolg derselben beigetragen hat.


5. Zu den Ansprüchen 2 bis 14
Die Ansprüche 8 und 10 betreffen eine Anordnung zum Bilden von fehlergesicherten Datenwörtern gemäß dem Verfahren nach einem der Ansprüche 1 bis 7 bzw
eine Anordnung zum Decodieren von gemäß dem Verfahren nach einem der Ansprüche 1 bis 7 fehlergesicherten Datenwörtern und stellen parallele Ausprägungen des dem Anspruch 1 zugrunde liegenden erfinderischen Gedankens dar. Die
Ansprüche 2 bis 7, 9 und 11 bis 14 beinhalten besondere Ausführungsarten des
Verfahrens nach Anspruch 1 bzw der Anordnung nach Anspruch 8 bzw 10.


Gegen diese Ansprüche hat die Klägerin keine gesonderten, dh unabhängig von
dem oben behandelnden Angriff auf den Anspruch 1 bestehenden Bedenken vorgetragen. Für den Senat ist nichts erkennbar, was bei rechtsbeständigem Anspruch 1 den Rechtsbestand dieser Ansprüche in Frage stellen könnte.

                                         - 16 -



6. Zum Anspruch 15
Der Patentanspruch 15 ist ebenfalls rechtsbeständig. Die von der Klägerin geltend
gemachten Widerrufsgründe stehen ihm nicht entgegen.
a) Die Fassung des Patentanspruchs 15 macht in Verbindung mit der Patentschrift
hinreichend klar, was unter Schutz stehen soll.


Anspruch 15 ist ein auf einen Datenträger gerichteter Sachanspruch. Sein Gegenstand ist durch Merkmale gekennzeichnet, die die Struktur von auf ihm aufgezeichneter Information betreffen. Die Information soll aus Datenwörtern in Form
von Datenblöcken bestehen, wobei die Datenwörter "gemäß dem Verfahren nach
einem der Ansprüche 1 bis 7" erzeugt sein sollen.


Weitere die Struktur der Information betreffende Merkmale sind im kennzeichnenden Teil des Anspruchs 15 aufgeführt. Sie besagen, daß jeder Block je eine aus
den geradzahligen bzw aus den ungeradzahligen Datenwörtern abgeleitete Information sowie je eine aus den ersten bzw den zweiten Paritätswörtern abgeleitete
Information aufweist. Ersichtlich sind mit den Daten- und Paritätswörtern die im
Merkmal e) des Anspruchs 1 aufgeführten Wörter gemeint.


Im übrigen konnte der Fachmann aus Figur 2 des Patents ersehen, wie ein Datenund Paritätswörter enthaltender Block aufgebaut sein kann, der einem zB aus einem Aufzeichnungs- und Wiedergabegerät bestehenden Übertragungskanal zugeführt wird (Patentschrift S 8 Z 12 bis 17).


Der beanspruchte Datenträger unterscheidet sich von bekannten Datenträgern
- etwa gemäß N3 bis N5 - durch die Struktur der auf ihm aufgezeichneten Information. Ob ein Datenträger anspruchsgemäß ausgebildet ist, kann vom Fachmann
dadurch festgestellt werden, daß die aufgezeichnete Information ausgelesen wird
und mittels einer geeigneten Vorrichtung überprüft wird, ob sich die ausgelesenen
Daten als Datenwörter und Paritätswörter interpretieren lassen, die mit den Maßnahmen des Anspruchs 1 erzeugt worden sind, so daß die Daten dementsprechend decodiert werden können.

                                        - 17 -



An dieser Sachlage ändern die Hinweise der Klägerin auf in den Ansprüchen 1
und 15 nicht aufgeführte, in der Praxis aber mögliche Zwischenschritte - wie Aufzeichnung auf einen Glasmaster und Übertragung der Aufzeichnung über weitere
Zwischenträger - nichts. Daß zusätzliche Schritte möglich sind, entnimmt der
Fachmann bereits den Ansprüchen 2, 3 und 7 sowie der Figur 2 (dort ersichtliche
Hinzufügung eines Synchronwortes). Außerdem versteht es sich für ihn von
selbst, daß zB die Daten- und Paritätswörter zum Aufzeichnen auf den Datenträger in ein dafür geeignetes Signalformat umgesetzt werden müssen. Als wesentlich sieht es der Fachmann dabei an, daß die durch das Fehlersicherungsverfahren nach Anspruch 1 erzeugte Struktur von Daten- und Paritätswörtern derart auf
den Datenträger gelangt, daß die beim Auslesen des Datenträgers erhaltenen Daten nach Maßgabe des Merkmals l) des Anspruchs 1 durch entsprechend umgekehrte Anwendung des im Anspruch 1 aufgeführten Codierverfahrens decodiert
werden können.


Auf die in diesem Zusammenhang von der Klägerin aufgewordene Frage, inwieweit der in der Rechtssprechung verwendete Begriff product-by-proces auf den
Anspruch 15 zutrifft, kommt es dabei ersichtlich nicht an.


b) Der Gegenstand des Anspruchs 15 geht entgegen der Auffassung der Klägerin
nicht über den Inhalt der ursprünglichen Anmeldung hinaus.


Anspruch 15 beruht im wesentlichen auf dem ursprünglichen Anspruch 10. Dieser
lautet:


          "10. Datenträger, der mittels eines Verfahrens nach einem der
               Ansprüche 1 bis 7 erzeugt wird, mit einer Reihe von
               Blöcken, dadurch gekennzeichnet, dass jeder Block folgende Informationen enthält:
               eine dritte Anzahl von Wörtern gleich der Hälfte der ersten
               Anzahl und abgeleitet aus geradzahligen Datenwörtern
               der Reihe von Datenwörtern,

                                       - 18 -



             eine vierte Anzahl von Wörtern, abgeleitet aus der ersten
             Reihe von Paritätswörtern,
             eine weitere dritte Anzahl von Wörtern, die aus ungeradzahligen Datenwörtern der Reihe von Datenwörtern abgeleitet wird, und
             eine weitere vierte Anzahl von Wörtern, die aus der zweiten Reihe von Paritätswörtern abgeleitet wird."


Die Formulierung des ursprünglichen Anspruchs 10
"Datenträger, der mittels eines Verfahrens nach einem der Ansprüche 1 bis 7 erzeugt wird, mit einer Reihe von Blöcken" konnte fachmännisch nur so verstanden
werden, daß ein Datenträger beansprucht wird, der in Blöcken angeordnete Daten
trägt, die mittels des Verfahrens nach einem der Ansprüche 1 bis 7 erzeugt worden sind. Die Formulierung des Anspruchs 15 des Streitpatents "Datenträger mit
gemäß dem Verfahren nach einem der Ansprüche 1 bis 7 erzeugten fehlergesicherten Datenwörtern in Form von Datenblöcken" ist in diesem Sinne präzisiert
und somit zulässig.


Auch den weiteren Bedenken der Klägerin, in Anspruch 15 sei in allgemeiner
Weise jeweils von einer "abgeleiteten Information" die Rede, während der ursprüngliche Anspruch 10 konkreter jeweils von einer quantitativ definierten Anzahl
von Wörtern spreche, die aus Daten- oder Paritätswörtern abgeleitet seien, kann
nicht beigetreten werden.


Im einzelnen ist nämlich festzustellen, daß die im Anspruch 15 des Patents mehrmals aufgeführte "Information" nicht, wie die Klägerin meint, beliebig gestaltet sein
kann; vielmehr soll gemäß dem Oberbegriff der Datenträger Datenwörter in Form
von Datenblöcken aufweisen. Der Fachmann zieht daraus den Schluß, daß unter
der im Anspruch 15 mehrmals aufgeführten "abgeleiteten Information", die jeder
Block enthalten soll, Wörter zu verstehen sind. Bestätigt wird ihm diese Auslegung
durch den in Figur 2 des Patents dargestellten Datenblock. Er besteht aus einem

                                     - 19 -



Synchronwort, 24 Datenwörtern und 8 Paritätswörtern und ist ua zur Zuführung zu
einem Aufzeichnungsgerät vorgesehen (S 8 Z 12 bis 17 der Patentschrift).


Aus den Angaben in den ursprünglichen Ansprüchen 1 und 10 zu einer "ersten
Anzahl" und "dritten Anzahl" ist im Ergebnis zu entnehmen, daß die Anzahl der
aus den Datenwörtern abgeleiteten Wörter gleich der der Datenwörter sein soll.
Obwohl die Angaben über die jeweilige Anzahl im erteilten Anspruch 15 nicht
mehr vorhanden sind, versteht der Fachmann das Ableiten der Wörter aus den
Datenwörtern im ursprünglichen Sinn, dh als Ableiten ohne Veränderung der Anzahl. Die gesamten Patentunterlagen einschließlich der schon erwähnten Figur 2
zeigen nichts Anderes.


Der erteilte Anspruch 15 bleibt somit - abgesehen von der oben erwähnten Präzisierung im Oberbegriff - fachmännisch verstanden im Rahmen des im ursprünglichen Anspruch 10 Offenbarten.


c) Mit ihrer Rüge, der Fachmann könne der Patentschrift nicht entnehmen, welche
Schritte er beim Speichern der erzeugten Datenwörter durchzuführen habe, macht
die Klägerin mangelnde Ausführbarkeit im Sinne von § 21 Abs 1 Nr 2 PatG geltend. Dem vermochte der Senat jedoch nicht beizutreten.


Die den parallelen Kanälen zuzuführenden Datenwörter sind vorgegeben, zB entsprechend den Abtastwerten eines akustischen Signals. Die Erzeugung der dazugehörenden Binärwörter sowie der aus den Datenwörtern und den Binärwörtern
gebildeten fehlerkorrigierbaren Blöcke wird im Anspruch 1 hinreichend beschrieben. Der Fachmann am Prioritätstag hatte keine Schwierigkeiten, entsprechend
den Angaben des Anspruchs 15 aus diesen Größen abgeleitete Informationen auf
einem Datenträger aufzuzeichnen.

                                       - 20 -



d) Entgegen der Auffassung der Klägerin steht dem Anspruchsgegenstand auch
nicht der Ausschließungsgrund des § 21 Abs 1 Nr 1 iVm § 1 Abs 1 Nr 4 und Abs 3
PatG (Wiedergabe von Informationen als solchen) entgegen.


Um eine bloße Wiedergabe von Informationen handelt es sich schon deshalb
nicht, weil der beanspruchte Aufzeichnungsträger mit der auf ihm aufgezeichneten
Informationsstruktur nicht dazu bestimmt ist, dem Menschen Informationsinhalte
direkt zu vermitteln, wie es zB bei Tabellen, Formularen, Schriftanordnungen und
dergleichen der Fall ist, die deswegen vom Patentschutz ausgeschlossen sind
(Schulte PatG, 6. Aufl § 1 Rdn 119). Vielmehr dient der Aufzeichnungsträger, wie
für den Fachmann ohne weiteres klar ist, dazu, mit einer Wiedergabeeinrichtung
zusammenzuwirken, die zur Abtastung und Verarbeitung der aufgezeichneten Datenblöcke ausgebildet ist.


Auch wenn man die von der Beklagten erörterte, zu der gleichlautenden Bestimmung von Artikel 52 (2) (d) (3) EPÜ ergangene Entscheidung "Datenstrukturprodukt/PHILIPS" des EPA (GRUR Int 2001, 167) betrachtet, ist festzustellen, daß
auch deren Grundsätze nicht dazu führen, im Anspruchsgegenstand eine Wiedergabe von Informationen im Sinne von § 1 Abs 2 Nr 4 PatG zu erblicken.


Der vorliegend beanspruchte Aufzeichnungsträger ist nämlich durch die auf ihm
aufgezeichnete funktionelle Datenstruktur gekennzeichnet, die auf das System abgestimmt ist, in dem der Aufzeichnungsträger zu verwenden ist, wohingegen ein
kognitiver Gehalt der aufgezeichneten Daten keine Rolle spielt.


Die auf dem beanspruchten Datenträger befindliche Datenstruktur dient der Lösung der technischen Aufgabe, eine gute Korrigierbarkeit von Fehlerhäufungen so
wie von Einzelfehlern zu erreichen (Patentschrift S 2 Z 22 und 23).


e) Die Patentfähigkeit des Gegenstandes des Anspruchs 15 ergibt sich daraus,
daß er eine weitere parallele Ausprägung des dem Anspruch 1 zugrunde liegenden erfinderischen Gedankens darstellt.

                                     - 21 -



7. Bei rechtsbeständigem Anspruch 15 ist auch Anspruch 16, der eine besondere
Ausführungsart des Datenträgers nach Anspruch 15 betrifft, rechtsbeständig.


Die Kostenentscheidung beruht auf § 84 Abs 2 PatG iVm § 91 Abs 1 Satz 1 ZPO,
der Ausspruch zur vorläufigen Vollstreckbarkeit auf § 99 Abs 1 PatG iVm § 709
ZPO.


Dr. Schwendy     Obermayer           Kalkoff          Schuster       Dr. Hartung


                                                                              Be
