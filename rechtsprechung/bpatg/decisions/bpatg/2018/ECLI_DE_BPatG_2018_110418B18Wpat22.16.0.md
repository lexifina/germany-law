---
ecli: "ECLI:DE:BPatG:2018:110418B18Wpat22.16.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 22/16"
decided: "2018-04-11"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=14&nr=31270&anz=825&pos=217&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2018-04-11_18_W-pat_22_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 22/16 vom 2018-04-11

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 22/16                                                    Verkündet am
_______________                                                      11. April 2018
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2013 022 405.5


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 11. April 2018 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie den Richter Kruppa, die Richterin Dipl.-Phys. Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater




ECLI:DE:BPatG:2018:110418B18Wpat22.16.0

                                        -2-



beschlossen:


      Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom
      19. Juli 2016 aufgehoben und das Patent auf der Grundlage der folgenden Unterlagen erteilt:


       - Patentansprüche 1 bis 8, eingereicht in der mündlichen Verhandlung,
       - Beschreibung, Seite 1, eingereicht in der mündlichen Verhandlung, Seiten 2 bis 32, eingegangen am 27. April 2016,
       - Figuren 1 bis 5, eingegangen am 27. April 2016.




                                   Gründe


                                         I.


Die am 27. April 2016 beim Deutschen Patent und Markenamt eingereichte Teilungsanmeldung      10 2013 022 405.5         geht   aus   der   Patentanmeldung
10 2013 022 299.0 hervor, die selbst wieder als Teilungsanmeldung aus der
Stammanmeldung 10 2013 014 172.9 hervorgegangen ist und die britische Priorität 1215428.2 vom 30. August 2012 in Anspruch nimmt. Die vorliegende Teilungsanmeldung trägt die Bezeichnung


          „Schutz globaler Register in einem Multithreaded-Prozessor“


und wurde durch Beschluss der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamts mit Beschluss vom 19. Juli 2016 zurückgewiesen, da der
Gegenstand des Patentanspruchs 1 für den Fachmann in der Anmeldung nicht so
deutlich und vollständig angegeben sei, dass dieser ihn ausführen könne.

                                      -3-



Gegen den vorstehend genannten Beschluss richtet sich die Beschwerde der Anmelderin.


Die Anmelderin beantragt,


      den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
      Patent- und Markenamts vom 19. Juli 2016 aufzuheben und das
      Patent auf der Grundlage der folgenden Unterlagen zu erteilen:


       - Patentansprüche 1 bis 8, eingereicht in der mündlichen Verhandlung,


       - Beschreibung, Seite 1, eingereicht in der mündlichen Verhandlung, Seiten 2 bis 32, eingegangen am 27. April 2016,


       - Figuren 1 bis 5, eingegangen am 27. April 2016.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 lautet:


       M1 „Verfahren zum Verwalten globaler Ressourcen innerhalb eines Multithreaded-Prozessors,
       M1a wobei der Multithreaded-Prozessor mehrere Hardware-Threads umfasst und das Verfahren umfasst:
       M2 Empfangen (202) einer Instruktion aus einem Hardware-Thread, in eine globale Ressource zu schreiben;
       M3 Überprüfen (204) eines globalen Steuerfelds in einem globalen Register im Multithreaded-Prozessor,
       M3a um zu bestimmen, ob der Hardware-Thread Schreibzugriff
            auf die globale Ressource hat,
       M3b wobei das globale Steuerfeld der globalen Ressource
            zugeordnet ist;

                                       -4-



       M4 in Reaktion auf das Bestimmen, dass der Hardware-Thread
            Schreibzugriff auf die globale Ressource hat, Erlauben (206)
            der Ausgabe der Instruktion; und
       M5 in Reaktion auf das Bestimmen, dass der Hardware-Thread
            keinen Schreibzugriff auf die globale Ressource hat, Verhindern (208) der Ausgabe der Instruktion und Auslösen einer
            Ausnahme.“


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 8 lautet:


       N1   „Multithreaded-Prozessor, umfassend:
       N1a mehrere Hardware-Threads (105-108);
       N1b wenigstens eine globale Ressource (110); und
       N1c Hardware-Logik (403), die ausgelegt ist zum:
       N2   Empfangen einer Instruktion aus einem der mehreren Hardware-Threads, in eine globale Ressource zu schreiben;
       N3   Überprüfen eines globalen Steuerfelds in einem globalen Register im Multithreaded-Prozessor,
       N3a um zu bestimmen, ob der Hardware-Thread Schreibzugriff
            auf die globale Ressource hat,
       N3b wobei das globale Steuerfeld der globalen Ressource
            zugeordnet ist; und
       N4   in Reaktion auf das Bestimmen, dass der Hardware-Thread
            Schreibzugriff auf die globale Ressource hat, Erlauben der
            Ausgabe der Instruktion,
       N5   wobei die Hardware-Logik ferner dafür ausgelegt ist, in
            Reaktion auf das Bestimmen, dass der Hardware-Thread
            keinen Schreibzugriff auf die globale Ressource hat, das
            Ausgeben der Instruktion zu verhindern und eine Ausnahme
            auszulösen.“

                                        -5-



Wegen des Wortlauts der abhängigen Ansprüche 2 bis 7 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht geltend, dass die geänderte Anspruchsfassung
zulässig und die Gegenstände der geltenden Ansprüche im Lichte des Standes
der Technik neu seien und auf einer erfinderischen Tätigkeit beruhten.


Im Prüfungsverfahren wurden als Stand der Technik die folgenden Druckschriften
genannt:


       P1    TriCore 1, 32-bit Unified Processor Core, Volume 1, Core Architecture, V 1.3 & V 1.31 Architecture, User's Manual, V 1.3.8, Ordering
             No. B158-H8581-G2-X-7600, Infineon Technologies AG, Januar
             2008, und
       P2    Kluge, F. u. a.: Use of Helper Threads for OS Support in the Multithreaded Embedded TriCore 2 Processor. In: Proceedings Work-In-Progress-Session of the 13th Real-time and Embedded Technology
             and Applications Symposium, Bellevue, USA, 2007, Seiten 25-27.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                         II.


Die zulässige Beschwerde hat in der Sache Erfolg. Sie führt zur Aufhebung des
angefochtenen Beschlusses und zur Erteilung des nachgesuchten Patents. Denn
der zweifelsfrei gewerblich anwendbare Gegenstand des nunmehr geltenden Patentbegehrens ist gegenüber dem im Verfahren befindlichen Stand der Technik
neu und beruht auf einer erfinderischen Tätigkeit. Auch die weiteren Voraussetzungen zur Patenterteilung sind erfüllt (§§ 1 bis 5, § 34 PatG).

                                        -6-



1. Die Anmeldung betrifft den Schutz globaler Register in einem Multithreaded-Prozessor (vgl. geltende Beschreibung, Seite 1, letzter Abs.).


   Die Anmeldung geht davon aus, dass Multithreaded-Prozessoren in der Regel
   lokale und globale Allzweckregister umfassen. Die lokalen Register seien dem
   jeweiligen Hardware-Thread vorbehalten, und nur der Hardware-Thread selbst
   könne darauf zugreifen, während globale Register von verschiedenen Hardware-Threads gemeinsam genutzt würden. In einem Beispiel könne ein
   Multithreaded-Prozessor ein Vier-Thread-Prozessor sein, und diese vier
   Threads könnten alle in der Lage sein, auf einen Satz globaler Register zuzugreifen. Diese globalen Register könnten von verschiedenen Threads für verschiedene Zwecke verwendet werden, und die Zuweisung globaler Register für
   diese verschiedenen Zwecke werde in der Regel von einem Compiler ausgeführt (vgl. geltende Beschreibung, S. 1, ersterAbs.).


   Die Anmeldung nennt als Aufgabe, die Verwaltung des Zugriffs auf globale,
   von mehreren Threads gemeinsam genutzte Ressourcen zu verbessern
   (vgl. geltende Beschreibung S. 1, handschriftlicher Einschub in Zeile 30).


   Der zuständige Fachmann weist eine abgeschlossene Hochschulausbildung
   auf dem Gebiet der Elektrotechnik oder Informationstechnik auf und verfügt
   über mehrjährige Erfahrung in der Entwicklung und Programmierung von
   Multithreaded-Prozessoren.


   Die Aufgabe soll durch ein Verfahren zum Verwalten globaler Ressourcen innerhalb eines Multithreaded-Prozessors nach Patentanspruch 1 und einen
   Multithreaded-Prozessor nach Patentanspruch 8 gelöst werden.


   Im Verfahren nach Anspruch 1 wird von einem Multithreaded-Prozessor ausgegangen, der mehrere Hardware-Threads umfasst (vgl. Merkmale M1,M1a).
   Zum Verwalten globaler Ressourcen innerhalb dieses Prozessors ist vorgese-

                                        -7-



   hen, dass nach Empfang einer Instruktion aus einem Hardware-Thread zum
   Schreiben in eine globale Ressource (Merkmal M2) in einem globalen Register
   im Multithreaded-Prozessor ein Steuerfeld überprüft wird, das der globalen
   Ressource zugeordnet ist (Merkmal M3, M3b). Das Überprüfen dient dazu, zu
   bestimmen, ob der Hardware-Thread Schreibzugriff auf diese globale
   Ressource hat (Merkmal M3a). Wenn der Hardware-Thread Schreibzugriff auf
   die globale Ressource hat, wird die Ausgabe der Instruktion erlaubt (Merkmal M4). Wenn der Hardware-Thread dagegen keinen Schreibzugriff auf die
   globale Ressource hat, wird die Ausgabe der Instruktion verhindert und eine
   Ausnahme ausgelöst (Merkmal M5).


   Anspruch 8 ist auf einen Multithreaded-Prozessor gerichtet, der mehrere
   Hardware-Threads und wenigstens eine globale Ressource umfasst und der
   eine Hardware-Logik aufweist, die zur Ausführung eines Verfahrens entsprechend Anspruch 1 eingerichtet ist.


2. Die geltenden Patentansprüche 1 bis 8 sowie die Beschreibung mitsamt Figuren sind zulässig (§ 38 PatG).


   Die Änderungen in den Ansprüchen 1 bis 8 gegenüber den Anmeldeunterlagen
   liegen im Rahmen der ursprünglichen Offenbarung.


   Der Patentanspruch 1 basiert auf den in der Stammanmeldung ursprünglich
   eingereichten Ansprüchen 1 und 2, wobei der Verfahrensschritt der Überprüfung ausgehend von Seite 4, Zeilen 6 bis 11 der in der Stammanmeldung ursprünglich eingereichten Beschreibung präzisiert wurde. Anspruch 2 basiert
   auf dem ursprünglich eingereichten Anspruch 14, die Ansprüche 3 bis 7 basieren auf den ursprünglich eingereichten Ansprüchen 9 bis 13. Der Patentanspruch 8 umfasst die in der Stammanmeldung ursprünglich eingereichten Ansprüchen 16 und 17, wobei die Überprüfung von Registern gemäß Seite 4,
   Zeilen 6 bis 11 der ursprünglich eingereichten Beschreibung präzisiert wurde.

                                      -8-



  In allen Ansprüchen wurde basierend auf dem ersten Absatz der Seite 1 der in
  der Stammanmeldung ursprünglich eingereichten Beschreibung der Begriff
  „Thread“ dahingehend präzisiert, dass es sich um einen „Hardware-Thread“
  handelt.


  In der Beschreibungseinleitung wurde eine Würdigung des Standes der Technik ergänzt und eine der Anmeldung zugrunde liegende Aufgabe angegeben.
  Die Figuren 1 bis 5 entsprechen inhaltlich den zum Anmeldetag eingereichten
  Figuren.


3. Der Gegenstand der unabhängigen Patentansprüche 1 und 8 ist gegenüber
  dem im Verfahren befindlichen Stand der Technik neu (§ 3 PatG).


  Der Fachmann entnimmt Druckschrift P1 das Verwalten von Ressourcen innerhalb eines Prozessors gemäß Anspruch 1, sowie einen entsprechenden
  Prozessor gemäß Anspruch 8, wobei der Prozessor jedoch keine Hardware-Threads umfasst und es sich somit nicht um einen „Multithreaded-Prozessor“
  im Sinne der vorliegenden Anmeldung handelt (teilweise Merkmal M1/N1).
  Den Ausführungen zu Adressräumen und Tasks (S. 10-5, Kap. 10.4; S. 4-1,
  Kap. 4.1; sowie S. 3-8 und S. 1-7, erster Satz) entnimmt der Fachmann zudem
  das Ausführen einer Mehrzahl an Prozessen und von Threads, wobei er aufgrund der beschriebenen Kontext-Wechsel ein softwareseitiges Multithreading
  mitliest (teilweise Merkmale M1a/N1a).
     Aus der Beschreibung der Schreibberechtigung („Global Address Register
  Write Permission“, vgl. S. 3-8) liest der Fachmann die Möglichkeit mit, Instruktionen aus einem von mehreren Threads zu empfangen, um in ein globales
  Register zu schreiben, wobei das Register („Global Address Register“) als globale Ressource angesehen werden kann. Auch in diesem Zusammenhang
  sind keine Hardware-Threads genannt (teilweise Merkmal M2/N2).
     Ein „Global Register Write Permission Flag“ sagt aus, ob der in Ausführung
  befindliche Thread in das (globale) Adressregister schreiben darf oder nicht

                                     -9-



und ist damit der globalen Ressource zugeordnet. Das Flag ist Teil des „Program Status Word Register“ (vgl. S. 3-6, Kap. 3.2.2, i. V. m. S. 3-8). Dieses
Register enthält jedoch keine Benennung des aktiven Threads, sondern ist
taskspezifisch („task-specific“) und wird bei einem Kontext-Wechsel gesichert.
Es handelt sich daher nicht um ein globales Register, womit es sich bei der
enthaltenen   Angabe     der   Schreibberechtigung    („Global   Register   Write
Permission“) auch nicht um ein globales Steuerfeld in einem globalen Register
handelt (teilweise Merkmale M3/N3, M3a/N3a, M3b/N3b). Aus der genannten
Schreibberechtigung ergeben sich für den aktiven Thread implizit die beiden
Möglichkeiten, dass ein Schreibzugriff auf die globale Ressource zugelassen
oder verhindert wird. Auch hier bezieht sich der Schreibzugriff nicht auf einen
Hardware-Thread sondern einen Software-Thread. Die Ausgabe einer Ausnahme bei fehlender Schreibberechtigung ist nicht vorgesehen (teilweise
Merkmale M4/N4, M5/N5).
   Der Druckschrift P1 entnehmbare Prozessor unterscheidet sich damit vom
Gegenstand des Anspruchs 1 und 8 jeweils darin, dass keine Hardware-Threads vorgesehen sind (vgl. Merkmale M1a/N1a, M2/N2, M3a/N3a, M4/N4,
M5/N5). Druckschrift P1 ist zudem kein globales Steuerfeld eines globalen Registers zu entnehmen (vgl. Merkmale M3/N3, M3b/N3b). Das Auslösen einer
Ausnahme in Reaktion auf das Prüfen eines globalen Steuerfeldes, wenn ein
Hardware-Thread bei Empfang einer Schreib-Instruktion keinen Schreibzugriff
auf die globale Ressource hat, ist ebenfalls nicht zu entnehmen (vgl. Merkmal
M5/N5).


Druckschrift P2 ist zu entnehmen, dass es sich bei der Nachfolgeversion des in
Druckschrift P1 beschriebenen Prozessor-Kerns um einen Multithreaded-Prozessor mit Hardware-Threads im Sinne des vorliegenden Anspruchs 1 bzw.
des Anspruchs 8 handelt (vgl. S. 25, li. Sp., Abstract; S. 25, re. Sp., erster und
zw. Abs.; sowie Definition von „multithreaded processor“, S. 25, li. Sp., zw.
Abs. / Merkmal M1a/N1a, teilweise Merkmale M2/N2, M3a/N3a, M4/N4,
M5/N5 bzgl. Hardware-Threads). Druckschrift P2 sind keine Angaben zur

                                      - 10 -



  Ausführung von Instruktionen oder zur Verwendung von globalen Registern
  oder Ressourcen des Prozessors zu entnehmen (vgl. Merkmale M2/N2
  bis M5/N5).
  Weiterer relevanter Stand der Technik ist nicht bekannt geworden.


  Die Gegenstände des Anspruchs 1 und des Anspruchs 8 sind daher jeweils
  neu gegenüber dem im Verfahren befindlichen Stand der Technik.


4. Der Gegenstand der unabhängigen Patentansprüche 1 und 8 beruht gegenüber dem im Verfahren befindlichen Stand der Technik auch auf einer erfinderischen Tätigkeit (§ 4 PatG).


  Druckschrift P1 fehlt jeglicher Hinweis auf eine Realisierung des Prozessors
  als Multithreaded-Prozessor mit Hardware-Threads. Druckschrift P2 ist jedoch
  entnehmbar, dass ein Prozessor gemäß Druckschrift P1 auch mit Hardware-Threads realisiert werden kann. Der in Druckschrift P2 beschriebene Prozessor
  ist dabei kompatibel zu seiner in Druckschrift P1 beschriebenen Vorgängerversion (vgl. P2, S. 25, re. Sp., erster Abs.), so dass der Fachmann die Merkmale
  des Prozessors nach Druckschrift P1 auch in einem Multithreaded-Prozessor
  mit Hardware-Threads gemäß Druckschrift P2 als realisiert ansieht. Die Merkmale M1a, M2 und M3a des Anspruchs 1 sowie die Merkmale N1a, N2, N3a
  des Anspruchs 8 ergeben sich damit in naheliegender Weise aus dem vorliegenden Stand der Technik.
     Die Gestaltung des „Program Status Word Register“ gemäß Druckschrift P1
  (vgl. S. 3-6, Kap. 3.2.2, i. V. m. S. 3-8) gibt jedoch keinen Hinweis darauf, die
  Zugriffsinformationen dieses Registers als globales Steuerfeld eines globalen
  Registers zu realisieren (vgl. Merkmal M3 bzw. N3). Da das Register nach
  Druckschrift P1 eine Zuordnung zum aktiven Thread voraussetzt und keine
  Speicherung oder Zuordnung der Identifikation des entsprechenden Threads
  vorsieht, weist dies allenfalls auf eine lokale Lösung innerhalb des Kontexts
  des Threads hin. Druckschrift P2 gibt ebenfalls keinen Hinweis auf ein entspre-

                                       - 11 -



   chendes Merkmal, da ihr keine näheren Angaben zur Ausführung von Instruktionen oder Threads und den zu deren Verwaltung vorzusehenden Registern
   zu entnehmen sind. Das Auslösen einer Ausnahme in Reaktion auf das Fehlen
   einer Schreibberechtigung für eine globale Ressource beim Prüfen eines zugeordneten globalen Steuerfeldes ist ebenfalls weder Druckschrift P1 noch
   Druckschrift P2 zu entnehmen (vgl. Merkmal M5 bzw. N5).
      Somit erhält der Fachmann auch bei einer Zusammenschau der Druckschriften P1 und P2 und unter Einbeziehung seines Fachwissens keinen Hinweis auf eine Verwaltung von Schreibrechten in einem globalen und somit für
   alle Hardware-Threads zugänglichen gemeinsamen Register.


   Es ist daher anzuerkennen, dass die Gegenstände der Ansprüche 1 und 8 jeweils auf einer erfinderischen Tätigkeit beruhen und patentfähig sind.


5. Gleichfalls patentfähig sind die über das Selbstverständliche hinausgehenden
   Ausführungsformen gemäß den Ansprüchen 2 bis 7, die auf Anspruch 1 direkt
   oder indirekt rückbezogen sind.


6. Da die vorgelegten geltenden Unterlagen auch den weiteren Voraussetzungen
   zur Patenterteilung (§§ 1, 2, 5, 34 PatG) genügen, war auf die Beschwerde der
   Anmelderin     der     Zurückweisungsbeschluss       der     Prüfungsstelle   für
   Klasse G 06 F des Deutschen Patent- und Markenamts aufzuheben und ein
   Patent zu erteilen.




                                         III.
                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                     - 12 -



   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
      Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
      Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
      war, sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
      der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
      sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.




Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn            Kruppa              Dr. Otten-Dünnweber             Altvater


                                                                            Fi/Pf
