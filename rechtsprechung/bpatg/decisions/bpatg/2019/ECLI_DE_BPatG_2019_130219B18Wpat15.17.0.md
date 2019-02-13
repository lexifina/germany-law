---
ecli: "ECLI:DE:BPatG:2019:130219B18Wpat15.17.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 15/17"
decided: "2019-02-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=6&nr=34455&anz=817&pos=92&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-02-13_18_W-pat_15_17_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 15/17 vom 2019-02-13

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 15/17                                                      Verkündet am
 _______________                                                      15. Februar 2019
    (Aktenzeichen)                                                           …




                               BESCHLUSS

                             In der Beschwerdesache


              betreffend die Patentanmeldung 11 2005 003 874.2


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 15. Februar 2019 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, Dipl.-Ing. Veit und Dipl.-Ing. Altvater




ECLI:DE:BPatG:2019:150219B18Wpat15.17.0

                                      -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 24. Mai 2017 aufgehoben und das Patent auf der
       Grundlage der folgenden Unterlagen erteilt:


               -   Patentansprüche 1 bis 9, eingereicht in der mündlichen
                   Verhandlung,

               -   Beschreibung, Seiten 1 bis 3, 3A, 14, eingereicht in der
                   mündlichen Verhandlung, Seiten 4 bis 13, 15 bis 28, eingegangen am 2. März 2016,

               -   Figuren 1 bis 7, eingegangen am 2. März 2016.




                                  Gründe


                                       I.


Die vorliegende, am 2. März 2016 beim Deutschen Patent- und Markenamt eingereichte Teilungsanmeldung 11 2005 003 874.2 geht aus der Stammanmeldung
11 2005 003 339.2 hervor, die wiederum aus der am 23. Dezember 2005 eingereichten und als WO 2006/071969 A1 in englischer Sprache veröffentlichten PCT-Anmeldung (PCT/US2005/047376) hervorgeht, welche die US-Priorität 11/027,623
vom 29. Dezember 2004 in Anspruch nimmt. Die Patentanmeldung trägt die Bezeichnung


  „Transaktionsgestützter Verarbeitungsbetrieb mit gemeinsam genutzten Daten
                       in einer Multiprozessorumgebung“

                                      -3-



und wurde durch Beschluss der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamts in der Anhörung vom 24. Mai 2017 zurückgewiesen, da
der Gegenstand des Patentanspruchs 1 nach Hauptantrag den Gegenstand der
Anmeldung unzulässig erweitere und sich der Gegenstand des Patentanspruchs 1
nach Hilfsantrag für den Fachmann aus der Druckschrift


      P3     Rajwar, R. u. a.: Speculative Lock Elision: Enabling Highly Concurrent Multithreaded Execution. In: Proceedings of the 34th annual
             ACM/IEEE international symposium on Microarchitecture (MICRO-34), 2001. S. 294-305


und seinem Fachwissen in naheliegender Weise ergebe.


Im Prüfungsverfahren wurden als Stand der Technik zudem die folgenden Druckschriften genannt:


      P1     US 6 665 708 B1,
      P2     Rajwar, R. u. a.: Transactional Execution: Toward Reliable, High-performance Multithreading. In: IEEE Micro, Vol. 23, Issue 6, 2003. S.
             117-125,
      P4     Rajwar, R. u. a.: Transactional Lock-Free Execution of Lock-Based
             Programs. In: ASPLOS X Proceedings of the 10th international conference on Architectural support for programming languages and operating systems, Oktober 2002. S. 5-17.


Der Senat hat in seinem Ladungszusatz vom 3. Januar 2019 noch die Druckschrift


      P5     WO 2004/075044 A2


in das Verfahren eingeführt.

                                        -4-



Gegen den vorstehend genannten Beschluss richtet sich die Beschwerde der Anmelderin. Sie beantragt,


        den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 24. Mai 2017 aufzuheben
        und das Patent auf der Grundlage der folgenden Unterlagen zu
        erteilen:


             -      Patentansprüche 1     bis   9,   eingegangen      am
                    8. Februar 2019,

                    hilfsweise gemäß Hilfsantrag 1

                    Patentansprüche 1     bis   9,   eingegangen      am
                    8. Februar 2019,

                    hilfsweise gemäß Hilfsantrag 2

                    Patentansprüche 1 bis 9, eingereicht in der mündlichen Verhandlung,

             -      Beschreibung, Seiten 1 bis 3, 3A, 14, eingereicht in
                    der mündlichen Verhandlung, Seiten 4 bis 13, 15 bis
                    28, eingegangen am 2. März 2016,

             -      Figuren 1 bis 7, eingegangen am 2. März 2016.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hauptantrag lautet:


      „Prozessor, aufweisend:
M1    Einen Cache-Speicher (240);
M2    Eine mit dem Cache-Speicher gekoppelte Ausführungslogik (275) zum spekulativen Ausführen einer Transaktion und zum spekulativen Wiederausführen der Transaktion, wenn ein invalidierender Zugriff auf eine Mehrzahl von

                                       -5-



      Zeilen in einem gemeinsam genutzten Speicher während der Ausführung
      der Transaktion verfolgt wird;
M3    Eine Transaktionsverfolgungslogik zum Verfolgen eines invalidierenden
      Zugriffs auf die Mehrzahl von Zeilen in dem gemeinsam genutzten Speicher, auf die während einer spekulativen Ausführung durch die Transaktion
      verwiesen wird; und
M4    Eine Lockout-Logik (260) zum Sperren des Zugriffs auf die Mehrzahl von
      Zeilen in dem gemeinsam genutzten Speicher, auf die durch die Transaktion verwiesen wird, nach einer ersten Anzahl von Wiederholungen, die
      Transaktion spekulativ wiederauszuführen; und um die Ausführungslogik
      (275) in die Lage zu versetzen die Transaktion nicht spekulativ wiederauszuführen nach dem Sperren des Zugriffs auf die Mehrzahl von Zeilen in
      dem gemeinsam genutzten Speicher.“


Wegen des Wortlauts der nach Hauptantrag geltenden Unteransprüche 2 bis 9
wird auf die Akte verwiesen.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hilfsantrag 1 lautet unter Hervorhebung der Änderungen gegenüber dem Hauptantrag:


      „Prozessor, aufweisend:
M1    Einen Cache-Speicher (240);
M2a   Eine Ausführungslogik (275), die mit dem Cache-Speicher gekoppelt ist,
      wobei die gekoppelte Ausführungslogik eingerichtet ist zum spekulativen
      Ausführen einer Transaktion, und zum spekulativen Wiederausführen der
      Transaktion, wenn ein invalidierender Zugriff auf eine Mehrzahl von Zeilen
      in einem gemeinsam genutzten Speicher während der Ausführung der
      Transaktion verfolgt wird;
M3    Eine Transaktionsverfolgungslogik (275) zum Verfolgen eines invalidierenden Zugriffs auf die Mehrzahl von Zeilen in dem gemeinsam genutzten

                                          -6-



          Speicher, auf die während einer spekulativen Ausführung durch die Transaktion verwiesen wird; und
M3.1a wobei die Transaktionsverfolgungslogik eingerichtet ist, eine Mehrzahl von
          Einträgen zu halten, wobei jeder Eintrag eine Adresse, die mit einer der
          spekulativen Lade- oder Speicheroperationen verbunden ist, und eines oder
          mehrere Bits aufweist, um anzuzeigen, ob die transaktionale Ausführung
          gelingt oder fehlschlägt; und
M4        Eine Lockout-Logik (260) zum Sperren des Zugriffs auf die Mehrzahl von
          Zeilen in dem gemeinsam genutzten Speicher, auf die durch die Transaktion verwiesen wird, nach einer ersten Anzahl von Wiederholungen, die
          Transaktion spekulativ wiederauszuführen; und um die Ausführungslogik
          (275) in die Lage zu versetzen die Transaktion nicht spekulativ wiederauszuführen nach dem Sperren des Zugriffs auf die Mehrzahl von Zeilen in
          dem gemeinsam genutzten Speicher.“


Wegen des Wortlauts der nach Hilfsantrag 1 geltenden abhängigen Ansprüche 2
bis 9 wird auf die Akte verwiesen.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hilfsantrag 2 lautet unter Hervorhebung der Änderungen gegenüber Hilfsantrag 1:


          „Prozessor, aufweisend:
M1        Einen Cache-Speicher (240);
M2b Eine Ausführungslogik (275), die mit dem Cache-Speicher gekoppelt ist,
          wobei die Ausführungslogik eingerichtet ist zum spekulativen Ausführen einer Transaktion, und zum spekulativen Wiederausführen der Transaktion,
          wenn ein invalidierender Zugriff auf zumindest eine Mehrzahl von Zeilen in
          einem gemeinsam genutzten Speicher während der Ausführung der Transaktion verfolgt wird;

                                           -7-



M3b Einen Transaktionspuffer mit einer Transaktionsverfolgungslogik (275) zum
      Verfolgen eines invalidierenden Zugriffs auf die zumindest eine Mehrzahl
      von Zeilen in dem gemeinsam genutzten Speicher, auf die während einer
      spekulativen Ausführung durch die Transaktion verwiesen wird; und
M3.1b wobei die Transaktionsverfolgungslogik eingerichtet ist, eine Mehrzahl von
      Einträgen zu halten, wobei jeder Eintrag eine Adresse, die mit einer der
      spekulativen Lade- oder Speicheroperationen verbunden ist, und ein Feld
      für invalidierende Zugriffe eines oder mehrere Bits aufweist, um anzuzeigen, oh die transaktionale Ausführung gelingt oder fehlschlägt; und
M4b Eine Lockout-Logik (260) zum Sperren des Zugriffs auf die zumindest eine
      Mehrzahl von Zeilen in dem gemeinsam genutzten Speicher, auf die durch
      die Transaktion verwiesen wird, nach einer ersten Anzahl von Wiederholungen, die Transaktion spekulativ wiederauszuführen; und um die Ausführungslogik (275) in die Lage zu versetzen die Transaktion nicht spekulativ
      wiederauszuführen nach dem Sperren des Zugriffs auf die zumindest eine
      Mehrzahl von Zeilen in dem gemeinsam genutzten Speicher.“


Wegen des Wortlauts der nach Hilfsantrag 2 geltenden abhängigen Ansprüche 2
bis 9 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht geltend, dass die Anspruchsfassungen gemäß
Hauptantrag und den Hilfsanträgen 1 und 2 jeweils zulässig und die Gegenstände
der jeweiligen Ansprüche im Lichte des Standes der Technik neu seien und auf
einer erfinderischen Tätigkeit beruhten.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                      -8-



                                       II.


Die zulässige Beschwerde hat insoweit Erfolg, als sie zur Aufhebung des angefochtenen Beschlusses und zur Patenterteilung mit geänderten Unterlagen gemäß
Hilfsantrag 2 führt. Im Übrigen war die Beschwerde bezüglich des Hauptantrags
und des Hilfsantrags 1 zurückzuweisen. Denn die jeweiligen Anspruchssätze nach
Hauptantrag und Hilfsantrag 1 beinhalten unzulässige Erweiterungen und sind
damit nicht schutzfähig (§ 38 PatG). Die Frage der Patentfähigkeit der geltenden
Ansprüche gemäß Hauptantrag und Hilfsantrag 1 kann somit dahinstehen (vgl.
BGH, Urteil vom 18. September 1990 – X ZR 29/89, GRUR 1991, 120, 121 li. Sp.
Abs. 3 – Elastische Bandage).


1. Die Patentanmeldung betrifft den Betrieb von verschiedenen integrierten
   Schaltkreisen, Cores, und Threads mit gemeinsam genutzten Daten (vgl. geltende Beschreibung, Abs. 0001).


   Die Anmeldung geht davon aus, dass Fortschritte bei der Halbleiterverarbeitung und in der Logikauslegung eine Erhöhung des Umfangs der Logik ermöglicht haben, die sich auf integrierten Schaltungen befinden kann. Als Ergebnis
   hätten sich Computersystem-Konfigurationen von einem einzelnen oder mehreren integrierten Schaltkreisen in einem System zu mehreren Cores und mehreren Logikprozessoren entwickelt, die sich auf den einzelnen integrierten
   Schaltkreisen befinden. Ein integrierter Schaltkreis umfasse üblicherweise einen einzelnen Prozessorchip, wobei der Prozessorchip eine beliebige Anzahl
   von Cores und logischen Prozessoren aufweisen könne. Jeder Core könne bestimmte Ressourcen gemeinsam nutzen, wie z. B. Caches auf höherer Ebene,
   Busschnittstellen, und Fetch/Decode Einheiten. Außerdem könne eine einzelne
   integrierte Schaltung oder ein einzelner Core mehrere logische Prozessoren
   aufweisen, um mehrfache Software Threads auszuführen, was als integrierter
   Multi-Threading Schaltkreis, oder als Multi-Threading Core bezeichnet werde.
   Die derzeitige Software habe die Fähigkeit, einzelne Software Threads parallel

                                     -9-



auf einer Mehrzahl von Cores oder logischen Prozessoren ablaufen zu lassen.
Jedoch rufe die Steigerung der Anzahl von Software Threads, die gleichzeitig
ausgeführt würden, Probleme bei der Synchronisierung von Daten hervor, die
von mehreren Software Threads gemeinsam genutzt würden.


Eine übliche Lösung zum Zugriff auf gemeinsam genutzte Daten in Systemen
mit mehreren Cores oder mehreren Logikprozessoren umfasse die Verwendung von Sperren mittels Semaphor, um einen gegenseitigen Ausschluss gegenüber mehrfachen Zugriffen auf gemeinsam genutzte Daten zu garantieren.
Jedoch resultiere die steigende Fähigkeit, mehrfache Software Threads auszuführen, potentiell in einer fehlerhaften Konkurrenzsituation und Serialisierung
der Ausführung. Eine fehlerhafte Konkurrenzsituation trete oft wegen der Tatsache auf, dass Semaphore zum Absichern von Datenorten in Abhängigkeit
von der Granularität der gemeinsamen Nutzung eine sehr große Datenmenge
umfassen könnten. Aus diesem Grund wirkten Semaphore als „Verstärker" der
Konkurrenzsituation, da eine Konkurrenzsituation durch mehrfache Software
Threads für die jeweilige Semaphore auftreten könne, obwohl die Software
Threads auf vollkommen unabhängige Datenobjekte zugriffen. Dies führe zu
Situationen, in welchen ein erster Software Thread einen ersten Semaphor
sperre, der einen Datenort absichere, auf den ein zweiter Software Thread sicher zugreifen könne. Da der erste Software Thread den Semaphor gesperrt
habe, müsse der zweite Thread warten, bis der Semaphor entriegelt ist, was
eine Serialisierung anstatt einer parallelen Ausführung bedinge (vgl. geltende
Beschreibung, Abs. 0002-0007).


In der geltenden Beschreibung ist als Aufgabe genannt, einen Prozessor bereitzustellen, mit dem eine Konkurrenzsituation zwischen Threads und eine Serialisierung einer Thread-Ausführung bei Multi-Thread-Prozessoren vermindert
werden kann (vgl. S. 3, dritter Abs.).

                                   - 10 -



Der zuständige Fachmann weist ein abgeschlossenes Hochschulstudium der
Fachrichtung Elektrotechnik oder Informationstechnik auf und hat eine mehrjährige Berufserfahrung auf dem Gebiet der Entwicklung von Prozessorarchitekturen, die Multi-Threading unterstützen.


Die Aufgabe soll gemäß Hauptantrag und den Hilfsanträgen 1 und 2 durch einen Prozessor nach dem jeweiligen Patentanspruch 1 gelöst werden.


Als Lösung wird gemäß Anspruch 1 nach Hauptantrag ein Prozessor beansprucht, der einen Cache-Speicher (vgl. Merkmal M1), eine mit dem Cache-Speicher gekoppelte Ausführungslogik, eine Transaktionsverfolgungslogik und
eine Lockout-Logik aufweist.
Die Ausführungslogik dient zum spekulativen Ausführen einer Transaktion sowie zum spekulativen Wiederausführen der Transaktion, falls ein invalidierender Zugriff auf eine Mehrzahl von Zeilen in einem gemeinsam genutzten Speicher während der Ausführung der Transaktion festgestellt wird (vgl. Merkmal
M2). Die Transaktionsverfolgungslogik verfolgt hierzu invalidierende Zugriffe
auf die Mehrzahl von Zeilen in dem gemeinsam genutzten Speicher, auf die
während einer spekulativen Ausführung durch die Transaktion verwiesen wird
(vgl. Merkmal M3). Dies ist so zu verstehen, dass die Transaktionslogik dazu
eingerichtet ist, alle Zugriffe auf die von der Transaktion während der spekulativen Ausführung verwendeten Speicherzeilen zu überwachen (vgl. geltende
Beschreibung, Abs. 0037). Nur wenn kein solcher invalidierender Zugriff, bspw.
durch einen externen Agenten erfolgt ist, wird die spekulative Ausführung der
Transaktion als erfolgreich angesehen und ihr Ergebnis übernommen (vgl.
geltende Beschreibung, Abs. 0028, 0051). Die Lockout-Logik sperrt nach einer
ersten Anzahl von Wiederholungen der spekulativen Wiederausführung der
Transaktion den Zugriff auf die Mehrzahl von Zeilen in dem gemeinsam genutzten Speicher, auf die durch die Transaktion verwiesen wird, um die Ausführungslogik nach dem Sperren des Zugriffs auf die Mehrzahl von Zeilen in
dem gemeinsam genutzten Speicher in die Lage zu versetzten, die Transaktion

                                     - 11 -



  nicht spekulativ wiederauszuführen (vgl. Merkmal M4). Dies ist so zu verstehen, dass die Lockout-Logik nach einer mehrfachen, erfolglosen spekulativen
  Ausführung der Transaktion die verwendeten Speicherzeilen zur exklusiven
  Nutzung durch die Transaktion sperrt, beispielsweise durch die Verwendung
  von Semaphoren (vgl. geltende Beschreibung, Abs. 0054 f, „vierte Option“).
  Damit kann die Transaktion nicht-spekulativ ausgeführt werden.


  Im Hilfsantrag 1 wird zum Gegenstand des Anspruchs 1 gemäß Hauptantrag
  ergänzt, dass die Transaktionsverfolgungslogik eingerichtet ist, eine Mehrzahl
  von Einträgen zu halten, wobei jeder Eintrag eine mit der spekulativen Ladeoder Speicheroperation verbundene Adresse und ein oder mehrere Bits aufweist, um anzuzeigen, ob die transaktionale Ausführung gelingt oder fehlschlägt (vgl. Merkmal M3.1a).
  Die nur sprachliche Anpassung des Merkmals M2a führt zu keiner inhaltlichen
  Änderung gegenüber dem Merkmal M2 gemäß Hauptantrag.


  Im Anspruch 1 des Hilfsantrags 2 wird gegenüber Anspruch 1 des Hilfsantrags 1 ergänzt, dass die Transaktionsverfolgungslogik Teil eines Transaktionspuffers ist (vgl. Merkmal M3b). Zudem wird klargestellt, dass sich der Zugriff
  auf den gemeinsam genutzten Speicherbereich jeweils auf eine oder mehrere
  Zeilen bezieht (vgl. Merkmale M2b, M3b, M4b). Außerdem wird präzisiert, dass
  die Transaktionsverfolgungslogik neben den Adresseinträgen ein Feld für invalidierende Zugriffe aufweist (vgl. Merkmal M3.1b), d. h. ein Feld zum Ablegen
  von Informationen über Zugriffe, die zu einem Fehlschlagen der spekulativ
  ausgeführten Transaktion führen (vgl. Abs. 0038, 0044).


2. Der Gegenstand des Patentanspruchs 1 nach Hauptantrag wurde gegenüber
  dem Inhalt der Anmeldung in der ursprünglichen Fassung, wie er in der
  Stammanmeldung eingereicht und als WO 2006/071969 A1 veröffentlicht
  wurde, unzulässig erweitert (§ 38 Satz 1 PatG).

                                         - 12 -



   Die ursprünglich eingereichten Unterlagen der Stammanmeldung sehen eine
   „Transaktionsverfolgungslogik“ (transaction tracking logic) ausschließlich als
   Teil eines „Transaktionspuffers“ (transaction buffer; vgl. Fig. 3 und Abs. 0036,
   0037)   oder   in Verbindung        mit   einer   „Transaktionsausscheidungslogik“
   (transaction retirement logic; vgl. ursprünglich eingereichter Anspruch 1) vor.
   Dem Anspruch 1 gemäß Hauptantrag ist jedoch weder ein Transaktionspuffer
   noch eine Transaktionsausscheidungslogik zu entnehmen, sondern nur die
   „Transaktionsverfolgungslogik“ gemäß Merkmal M3.


   Der Gegenstand des Anspruchs 1 gemäß Hauptantrag stellt damit eine Verallgemeinerung dar und geht in unzulässiger Weise über den Inhalt der ursprünglich eingereichten Unterlagen hinaus.


   Mit dem nicht zulässigen Anspruch 1 gemäß Hauptantrag sind auch die weiteren Ansprüche des Hauptantrags nicht schutzfähig, da auf diese Ansprüche
   kein eigenständiges Schutzbegehren gerichtet war (vgl. BGH, Beschluss vom
   27. Juni 2007 – X ZB 6/05; GRUR 2007, 862 Abschnitt III 3. a) aa) - Informationsübermittlungsverfahren II).


3. Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 wurde ebenfalls
   gegenüber dem Inhalt der Anmeldung in der ursprünglichen Fassung unzulässig erweitert (§ 38 Satz 1 PatG).


   Anspruch 1 gemäß Hilfsantrag 1 unterscheidet sich von Anspruch 1 des
   Hauptantrags inhaltlich allein in einer ergänzten Beschreibung der Funktion der
   Transaktionsverfolgungslogik in Merkmal M3.1a. Merkmal M2a wurde nur
   sprachlich überarbeitet. Wie im Hauptantrag ist dem geltenden Anspruch 1
   gemäß Hilfsantrag 1 damit in Verbindung mit der „Transaktionsverfolgungslogik“ weder ein Transaktionspuffer noch eine Transaktionsausscheidungslogik
   zu entnehmen, was eine Verallgemeinerung gegenüber den ursprünglich eingereichten Unterlagen darstellt.

                                        - 13 -




   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1 geht daher ebenfalls in
   unzulässiger Weise über den Inhalt der ursprünglich eingereichten Unterlagen
   hinaus.


   Mit dem nicht zulässigen Anspruch 1 gemäß Hilfsantrag 1 sind auch die weiteren Ansprüche des Hilfsantrags 1 nicht schutzfähig, da auf diese Ansprüche
   kein eigenständiges Schutzbegehren gerichtet war (vgl. BGH, a. a. O. - Informationsübermittlungsverfahren II).


4. Der Hilfsantrag 2 erfüllt die Voraussetzungen für eine Patenterteilung.


   Der zweifelsfrei gewerblich anwendbare Gegenstand des Patentanspruchs 1
   gemäß Hilfsantrag 2 ist gegenüber dem im Verfahren befindlichen Stand der
   Technik neu und beruht auf einer erfinderischen Tätigkeit. Auch die weiteren
   Voraussetzungen zur Patenterteilung sind erfüllt (§§ 1 bis 5, § 34 und § 38
   PatG).


    a) Die Patentansprüche 1 bis 9 nach Hilfsantrag 2 sowie die Beschreibungsunterlagen mitsamt Figuren sind zulässig (§ 38 PatG).


   Die Änderungen in den Patentansprüchen 1 bis 9 gegenüber der ursprünglichen Fassung, wie sie in der Stammanmeldung eingereicht und als
   WO 2006/071969 A1 veröffentlicht wurde, liegen im Rahmen der ursprünglichen Offenbarung.


   Der auf einen Prozessor gerichtete Patentanspruch 1 basiert auf dem ursprünglich eingereichten Verfahrensanspruch 17, wobei die Verfahrensmerkmale ausgehend von dem zu Figur 2 beschriebenen Prozessor als funktionale
   Merkmale der jeweiligen Komponenten abgefasst wurden (vgl. Merkmale M1,
   M2b, M3b, M4b). Die Beschreibung der Transaktionsverfolgungslogik als Teil

                                    - 14 -



des Transaktionspuffers basiert dabei auf Absatz 0037 der ursprünglichen
Unterlagen (vgl. Merkmal M3b), die Klarstellung, dass sich ein invalidierender
Zugriff auf zumindest eine Zeile (einer Mehrzahl von Zeilen) bezieht, ergibt sich
für einen Cache-Speicher gemäß Merkmal M1 aus Absatz 0036 in Verbindung
mit Absatz 0037, sowie aus den ursprünglichen Ansprüchen 17 und 18 (vgl.
Merkmale M2b, M3b, M4b).
Die Beschreibung der Transaktionsverfolgungslogik nach Merkmal M3.1b basiert auf Absatz 0037 in Verbindung mit den Absätzen 0038 und 0044, wobei
die zusammenfassende Beschreibung der Mittel für Schreib- und Lesezugriffe
auf dem ursprünglichen Anspruch 18 in Verbindung mit Anspruch 17 beruht.


Die Ansprüche 2 bis 9 basieren auf den ursprünglich eingereichten Verfahrensansprüchen 18 bis 25, die wiederum als funktionale Merkmale des Prozessors
nach Figur 2 abgefasst wurden. Dabei wurden die Ansprüche 2 bis 4 hinsichtlich des Zugriffs auf zumindest eine Zeile entsprechend Anspruch 1 klargestellt
und in den Ansprüchen 8 und 9 ein Übersetzungsfehler korrigiert.


In der geltenden Beschreibung wurden eine Würdigung des Standes der Technik und eine Aufgabe aufgenommen (vgl. geltende Beschreibung, Seite 3). Auf
Seite 14 wurde ein Übersetzungsfehler und ein offensichtlich fehlerhafter Verweis auf Figur 4 korrigiert. Die weiteren Beschreibungsseiten und Figuren sind
unverändert gegenüber der deutschen Übersetzung der Stammanmeldung.


a) Patentanspruch 1 gemäß Hilfsantrag 2 ist neu gegenüber dem im Verfahren
  befindlichen Stand der Technik (§ 3 PatG).


Druckschrift P3 sieht Prozessoren mit gemeinsam genutztem Cache vor (vgl.
u. a. S. 299-300, Abschnitt „5.3 Misspeculation conditions and their detection“ /
Merkmal M1), die eine Ausführungslogik zur spekulativen Ausführung von
Transaktionen aufweisen, wobei auch ein Wiederholen der Ausführung ermöglicht wird („Execute critical section speculatively…“; vgl. S. 297, li. Spalte, zw.

                                      - 15 -



Abs., Schritt „2.“, und Abstract sowie S. 297, li. Sp., drittletzter Abs.: „In step 3.
…“/ Merkmal M2b). Dabei werden invalidierende Zugriffe auf die von der
Transaktion verwendeten Speicherbereiche durch eine geeignete Logik zur
Überwachung dieser Speicherbereiche erkannt (vgl. S. 297, li. Spalte, Schritt
„3.“ i. V. m. S. 298, li. Sp., vorl. Abs.), wobei dies nicht durch einen eigenständigen Transaktionspuffer, sondern im Rahmen der Kohärenz-Mechanismen
des Caches erfolgt (vgl. S. 299-300, Abschnitt 5.3 / teilweise Merkmal M3b).
Beim Auftreten solcher Zugriffe kann die spekulative Ausführung von Transaktionen (mehrfach) wiederholt werden. Falls auch diese Wiederholungen scheitern, kann die Transaktion bei Sperrung des Speicherbereichs für andere Zugriffe ausgeführt werden (vgl. S. 297, li. Sp., Schritt „3.“ i. V. m. Beschreibung
zu „In step 3. …“ / Merkmal M4b).


Im Unterschied zum Gegenstand des vorliegenden Anspruchs 1 sieht Druckschrift P3 keinen Transaktionspuffer mit einer Transaktionsverfolgungslogik
vor, bei dem die Transaktionsverfolgungslogik Adressen der spekulativen
Lade- oder Speicheroperationen und ein Feld für invalidierende Zugriffe aufweist. Damit ist Druckschrift P3 das Merkmal M3.1b gemäß Anspruch 1 des
Hilfsantrags 2 nicht zu entnehmen. Vergleichbar dem Merkmal M3b ist Druckschrift P3 nur allgemein eine Verfolgung von invalidierenden Speicherzugriffen
zu entnehmen. Anspruch 1 gemäß Hilfsantrag 2 ist damit neu gegenüber
Druckschrift P3.


Druckschrift P5 sieht vergleichbar mit Druckschrift P3 ebenfalls Prozessoren
mit gemeinsam genutztem Cache vor (vgl. u. a. Abstract / Merkmal M1), die
eine Ausführungslogik zur spekulativen Ausführung von Transaktionen aufweisen, wobei auch ein Wiederholen der Ausführung ermöglicht wird („Executing a
Critical Section“ bzw. „transactional execution“; vgl. Abs. 0056 bis 0058 und
Abs. 0061 bis 0063 / Merkmal M2b). Dabei werden durch eine geeignete Logik
invalidierende Zugriffe auf die von der Transaktion verwendeten Speicherbereiche durch eine geeignete Überwachung dieser Speicherbereiche erkannt

                                    - 16 -



(„… the system continually monitors data references made by other processes“, vgl. Abs. 0061 i. V. m. Abs. 0064 und Abs. 0058), wobei dies nicht durch
einen (eigenständigen) Transaktionspuffer, sondern unter Verwendung von
Erweiterungen des Caches erfolgt (vgl. „load-marking bit“ bzw. „store-marking
bit“, Abs. 0051 bzw. 0054 / teilweise Merkmal M3b). Beim Auftreten solcher
Zugriffe kann die spekulative Ausführung von Transaktionen (mehrfach)
wiederholt werden (vgl. Abs. 0063). Falls auch diese Wiederholungen scheitern, kann die Transaktion bei Sperrung des Speicherbereichs für andere Zugriffe ausgeführt werden (vgl. Abs. 0063 / Merkmal M4b).


Im Unterschied zum Gegenstand des vorliegenden Anspruchs 1 sieht auch
Druckschrift P5 keinen Transaktionspuffer mit einer Transaktionsverfolgungslogik vor, bei dem die Transaktionsverfolgungslogik Adressen der spekulativen
Lade- oder Speicheroperationen und ein Feld für invalidierende Zugriffe aufweist. Damit ist Druckschrift P5 das Merkmal M3.1b gemäß Anspruch 1 des
Hilfsantrags 2 nicht zu entnehmen. Vergleichbar mit dem Merkmal M3b ist
auch Druckschrift P5 nur allgemein eine Verfolgung von invalidierenden
Speicherzugriffen zu entnehmen. Anspruch 1 gemäß Hilfsantrag 2 ist damit
neu gegenüber Druckschrift P5.


Die Druckschriften P1, P2 und P4 liegen jeweils weiter ab vom Gegenstand
des geltenden Anspruchs 1.


Druckschrift P1 betrifft allgemein die parallele Ausführung von zwei oder mehr
Aufgaben („two or more concurrently executed jobs“), die gemeinsam einen
Speicher nutzen, und bei der geprüft wird, ob es zu Kollisionen bei der Ausführung dieser Aufgaben in Form von gemeinsamen Zugriffen auf vorab definierte
Datenbereiche kommt. Hierzu werden diese Datenbereiche definiert und Zugriffe auf diese in zugeordneten Datenfeldern protokolliert (vgl. Sp. 4, Z. 47 bis
Sp. 5, Z. 8, i. V. m. Sp. 1, Z. 8-13). Im Unterschied zum vorliegenden Anspruch 1 erfolgt dies nicht in einem eigenständigen Transaktionpuffer, sondern

                                        - 17 -



in einem Bereich des Systemspeichers (vgl. Fig. 6 mit Beschreibung). Zudem
findet eine Überwachung nur in Bezug auf zwei (oder mehr) vorab festgelegte
und parallel ausgeführte Aufgaben statt, während die vorliegende Anmeldung
beliebige invalidierende Speicherzugriffe in Bezug auf die spekulative Ausführung einer kritischen Befehlssequenz betrifft. Eine Strategie zur wiederholten
Ausführung von Transaktionen ohne und mit Sperren des verwendeten Speicherbereichs (vgl. Merkmal M2b i. V. m. M4b) ist ebenfalls nicht Gegenstand
der Druckschrift P1.


Druckschrift P2 geht inhaltlich nicht über Druckschrift P3 hinaus, sondern verweist auf diese Druckschrift sowie auf Druckschrift P4. Gegenstand ist ein
Überblick über das „Speculative Lock Elision“ Verfahren (SLE) nach Druckschrift P3 und ein „Transactional Lock Removal“ Verfahren (TLR) nach Druckschrift P4.


Das in Druckschrift P4 erläuterte „Transactional Lock Removal“ Verfahren
(TLR) ist als Ergänzung oder Alternative zum „Speculative Lock Elision“ Verfahren (SLE) nach Druckschrift P3 vorgesehen. Dabei unterscheidet sich das
TLR-Verfahren nach Druckschrift P4 vom Gegenstand des vorliegenden Anspruchs 1 insbesondere in einem Zeitstempel-basierten Verfahren zur Konfliktlösung (vgl. S. 6, li. Sp., letzte drei Absätze).


c) Der Gegenstand des Anspruchs 1 nach Hilfsantrag 2 beruht gegenüber
dem im Verfahren befindlichen Stand der Technik auch auf einer erfinderischen Tätigkeit (§ 4 PatG).


Keine der im Verfahren befindlichen Druckschriften sieht einen Transaktionspuffer mit einer Transaktionsverfolgungslogik zum Verfolgen eines invalidierenden Zugriffs auf zumindest eine Zeile in dem gemeinsam genutzten Speicher vor, auf die während einer spekulativen Ausführung durch die Transaktion
verwiesen wird (vgl. Merkmal M3b), wobei die Transaktionsverfolgungslogik

                                   - 18 -



eine Mehrzahl von Einträgen aufweist, die jeweils eine Adresse und ein Feld
für invalidierende Zugriffe aufweisen (vgl. Merkmal M3.1b).


Die Druckschriften P3 und P5 sehen im Unterschied zu Anspruch 1 gemäß
Hilfsantrag 2   jeweils   keinen   eigenständigen     Transaktionspuffer    mit
Transaktionsverfolgungslogik entsprechend den Merkmalen M3b und M3.1b
vor. Vielmehr realisieren beide Druckschriften eine Überwachung der Speicherzugriffe innerhalb des Cache-Speichers. Hierbei nutzt Druckschrift P3 die
vorliegende Hardware zur blockweisen Verwaltung der Cache-Kohärenz (vgl.
S. 299-300, Abschnitt „5.3 Misspeculation conditions and their detection“) während Druckschrift P5 den Cache um zusätzliche Bits für jede Cache-Zeile ergänzt (vgl. Abs. 0051 bis 0055). Dies führt im Unterschied zum Gegenstand
des vorliegenden Anspruchs 1 dazu, dass jede Wiederholung der Transaktionsausführung ein Löschen der zusätzlichen Datenfelder des Cache bzw. ein
vollständiges Aktualisieren des Cache voraussetzt.


Die vorstehend genannten Druckschriften P1 bis P5 können auch in beliebiger
Zusammenschau dem Fachmann die Merkmale des Anspruchs 1 nach Hilfsantrag 2 nicht nahelegen, da diese Druckschriften – auch unter Ergänzung
durch sein Fachwissen auf diesem Gebiet – keine Anregung zur Verwendung
eines eigenständigen Transaktionspuffers mit Transaktionsverfolgungslogik zur
Überwachung der spekulativen Ausführung einer Transaktion im Sinne der
Merkmale M3b und M3.1b in Verbindung mit einer Strategie zur Wiederausführung dieser Transaktion (vgl. Merkmale M2b, M4b) geben.
Zwar sieht Druckschrift P1 eine separate Sammlung von Informationen zur
Überwachung eines gemeinsamen Zugriffs von parallel ausgeführten Aufgaben
auf definierte, gemeinsam genutzte Speicherbereiche vor, die damit Parallelen
zur Transaktionsverfolgungslogik nach Merkmal M3.1b aufweist. Diese erfolgt
nach Druckschrift P1 jedoch nicht in einem eigenständigen Transaktionpuffer,
sondern in einem Bereich des Systemspeichers (vgl. Fig. 6 mit Beschreibung).
Zudem erfolgt in Druckschrift P1 nur eine Betrachtung von Abhängigkeiten

                                       - 19 -



   zwischen den parallel vom Prozessor ausgeführten Aufgaben (vgl. Sp. 4,
   Z. 47-50), wozu vorab eine Definition von zu überwachenden, gemeinsam genutzten Speicherbereichen der genannten Aufgaben erforderlich ist (vgl. Sp. 4,
   Z. 50-56). Um zum Anspruchsgegenstand zu gelangen, müsste der Fachmann
   von einer Cache-internen Lösung nach Druckschrift P3 oder P5 abweichen, zur
   Speicherung der Zugriffsinformationen jedoch abweichend von Druckschrift P1
   eine eigenständige Komponente vorsehen und gleichzeitig den Ablauf zur wiederholten Ausführung der Transaktion nach Druckschrift P3 oder P5 beibehalten. Für eine solche mosaikartige Kombination von Merkmalen ergibt sich für
   den Fachmann keine Veranlassung aus den genannten Druckschriften. Daher
   gelangt der Fachmann auch bei einer gemeinsamen Betrachtung von Druckschrift P1 und jeweils einer der Druckschriften P3 oder P5 nicht naheliegend
   zum Gegenstand des Anspruchs 1 gemäß Hilfsantrag 2.


   Es ist daher anzuerkennen, dass der Gegenstand des Anspruchs 1 gemäß
   Hilfsantrag 2 auf einer erfinderischen Tätigkeit beruht und patentfähig ist.


   d) Gleichfalls patentfähig sind die über das Selbstverständliche hinausgehenden Ausführungsformen gemäß den Ansprüchen 2 bis 9 nach Hilfsantrag 2, die
   auf Anspruch 1 rückbezogen sind.


5. Da die vorgelegten geltenden Unterlagen auch den weiteren Voraussetzungen
   zur Patenterteilung (§§ 1, 2, 5, 34 PatG) genügen, war auf die Beschwerde der
   Anmelderin der Zurückweisungsbeschluss der Prüfungsstelle für Klasse
   G 06 F des Deutschen Patent- und Markenamts aufzuheben und ein Patent
   gemäß Hilfsantrag zu erteilen.

                                       - 20 -



                                         III.


                       Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


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

                                    - 21 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn                 Kruppa               Veit                    Altvater


                                                                           prö
