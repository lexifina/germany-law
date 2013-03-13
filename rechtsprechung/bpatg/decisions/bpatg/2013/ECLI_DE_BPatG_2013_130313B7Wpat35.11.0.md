---
ecli: "ECLI:DE:BPatG:2013:130313B7Wpat35.11.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 35/11"
decided: "2013-03-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=15&nr=24998&anz=1167&pos=233&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-03-13_7_W-pat_35_11_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 7 W (pat) 35/11 vom 2013-03-13

## Entscheidung

BUNDESPATENTGERICHT


  7 W (pat) 35/11                                                   Verkündet am
_______________                                                     13. März 2013
    (Aktenzeichen)                                                        …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 199 83 857.7 - 53


…




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 13. März 2013 durch den Richter Dipl.-Phys.
Dipl.-Wirt.-Phys. Maile als Vorsitzenden und die Richter Schwarz, Dipl.-Phys. Dr.
rer. nat. Schwengelbeck und Dipl.-Ing. Altvater




BPatG 154
05.11

                                     -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                  Gründe


                                       I.


Die am 29. Dezember 1999 als PCT-Anmeldung PCT/US99/31105 unter Inanspruchnahme der Unionspriorität mit dem Aktenzeichen US 09/223,998 vom
31. Dezember 1998 eingereichte Patentanmeldung 199 83 857.7 - 53 betrifft ein


         Verfahren und Gerät zum Balancieren von Auslastungen zwischen
         den Pfaden in einem Mehrfachpfad-Computersystem


Die Anmeldung wurde am 6. Juli 2000 als WO 00/39679 A2 in englischer Sprache
und am 31. Januar 2002 als DE 199 83 857 T1 in deutscher Übersetzung veröffentlicht.
Die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts hat
die Patentanmeldung mit Beschluss vom 4. September 2007 zurückgewiesen, weil
der Patentanspruch 6 entsprechend der Anlage zum Schriftsatz vom 19. Juni 2007
gemäß § 34 Abs. 3 Satz 3 PatG unklar und daher nicht gewährbar sei. Dies gelte
sinngemäß auch für den nebengeordneten Anspruch 5.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin vom
30. Oktober 2007.


Im Prüfungsverfahren wurden folgende Druckschriften genannt:

                                         -3-



        D1     WO 91/14229 A1
        D2     EP 0 309 428 A2 und
        D3     IBM Technical Disclosure Bulletin, Vol. 18, Nr. 8,
               Januar 1976, Seiten 2722-2725


In der mündlichen Verhandlung verteidigt die Anmelderin ihre Patentanmeldung
mit unveränderten Ansprüchen 1 bis 8 gemäß Hauptantrag und jeweils geänderten Ansprüchen 1 bis 8 gemäß den Hilfsanträgen 1 bis 3. Sie führt aus, dass die
jeweiligen Anspruchssätze nach Hauptantrag und den Hilfsanträgen 1 bis 3 zulässig und patentfähig seien, wobei auch zweifelsfrei klar sei, was jeweils unter
Schutz gestellt werden solle.


Der vom Senat mit einer Gliederung versehene Patentanspruch 1 gemäß Hauptantrag lautet:


(M1)    Verfahren zum Verteilen von Eingabe/Ausgabe I/O-Betriebsschritten zwischen mindestens zwei Pfaden in einem Mehrfachpfad-Computersystem
        mit einem Hauptcomputer (1), einem Speichersystem (3) und mehreren
        Pfaden zum Koppeln des Hauptcomputers (1), mit dem Speichersystem
        (3),


        wobei das Verfahren einen Schritt enthält:


(M2)    (A) Auswahl - für den nächsten I/O-Betriebsschritt, der für die Übertragung
        zwischen dem Hauptcomputer (1) und dem Speichersystem (3) zuzuordnen ist, eines der mindestens zwei Pfade für die Übertragung des nächsten I/O-Betriebsschritts auf der Grundlage eines Zustands zuvor zugeordneter I/O-Betriebsschritte in einer Warteschlange für das Übertragen über
        die mindestens zwei Pfade,

                                      -4-



(M3.1) wobei jeder I/O-Betriebsschritt eine zugeordnete Datenzugangszeit bei
       einer Verarbeitung durch das Speichersystem (3) aufweist, und


(M3.2) dass der Schritt (A) einen Schritt zum Auswählen des einen der mindestens zwei Pfade umfasst, auf der Grundlage der Datenzugangszeiten der
       zuvor zugeordneten I/O-Betriebsschritte in der Warteschlange zu den
       mindestens zwei Pfaden.


Der nebengeordnete Anspruch 5 des Hauptantrags lautet:


       Computerlesbares Medium, codiert mit einem Programm für die
       Ausführung des Verfahrens gemäß Anspruch 1 auf einem Hauptcomputer.


Der nebengeordnete (und im Übrigen der Zurückweisung der Prüfungsstelle zu
Grunde liegende) Anspruch 6 des Hauptantrags lautet:


       Hauptcomputer (1) zur der Anwendung in einem Mehrfachpfad-Computersystem mit einem Speichersystem und mehreren Pfaden
       zum Koppeln des Hauptcomputers (1) zu dem Speichersystem
       (3), derart, dass der Hauptcomputer enthält:


       einen Treiber, der zum Verteilen der Eingabe/Ausgabe (I/O) Betriebsschritte angepasst ist, die durch den Hauptcomputer (1) initiiert werden, zwischen mindestens zwei der mehreren Pfaden für
       die Übertragung zu dem Speichersystem (3), wobei der Treiber
       angepasst ist, für einen nächsten für die Übertragung von dem
       Hauptcomputer (1) zu dem im Speichersystem (3) zuzuordnenden
       I/O-Betriebsschritt einen der mindestens zwei Pfade auszuwählen,
       auf der Grundlage eines Zustands zuvor zugeordneter I/O-Be-

                                       -5-



        triebsschritte in einer Warteschlange für die Übertragung zu dem
        Speichersystem über die mindestens zwei der mehreren Pfade;


        wobei jeder I/O-Betriebsschritt eine zugeordnete Datenzugangszeit dann aufweist, wenn er durch das Speichersystem (3) verarbeitet wird, und der Treiber angepasst ist, den einen der mindestens zwei der Vielzahl von Pfaden auszuwählen, auf der Grundlage der Datenzugangszeiten der zuvor zugewiesenen I/O-Betriebsschritte in einer Warteschlange zu den mindestens zwei der
        Vielzahl von Pfaden.


Patentanspruch 1 gemäß Hilfsantrag 1 lautet (Merkmalsgliederung seitens des
Senats hinzugefügt, Änderungen gegenüber dem Hauptantrag unterstrichen):


(M1)*   Verfahren zum Verteilen von Eingabe/Ausgabe I/O-Betriebsschritten zwischen mindestens zwei Pfaden in einem Mehrfachpfad-Computersystem
        mit einem Hauptcomputer (1), einem Speichersystem (3) mit unterschiedlichen Speichertypen (7a, 7b, 11) und mehreren Pfaden zum Koppeln des
        Hauptcomputers (1), mit dem Speichersystem (3),


        wobei das Verfahren einen Schritt enthält:


(M2)    (A) Auswahl - für den nächsten I/O-Betriebsschritt, der für die Übertragung
        von Zieldaten zwischen dem Hauptcomputer (1) und dem Speichersystem
        (3) zuzuordnen ist, eines der mindestens zwei Pfade für die Übertragung
        des nächsten I/O-Betriebsschritts auf der Grundlage eines Zustands zuvor
        zugeordneter I/O-Betriebsschritte in einer Warteschlange für das Übertragen über die mindestens zwei Pfade,


(M3.1) wobei jeder I/O-Betriebsschritt eine zugeordnete Datenzugangszeit bei
        einer Verarbeitung durch das Speichersystem (3) aufweist,

                                        -6-




         (M3.1.1)   wobei die Datenzugangszeit die Zeit für den Zugriff auf die
                    Zieldaten ist,


(M3.2) und dass der Schritt (A) einen Schritt zum Auswählen des einen der mindestens zwei Pfade umfasst, auf der Grundlage der Datenzugangszeiten
         der zuvor zugeordneten I/O-Betriebsschritte in der Warteschlange zu den
         mindestens zwei Pfaden.


Patentanspruch 1 gemäß Hilfsantrag 2 lautet (Merkmalsgliederung seitens des
Senats hinzugefügt, Änderungen gegenüber dem Hauptantrag unterstrichen):


(M1)**    Verfahren zum Verteilen von Eingabe/Ausgabe I/O-Betriebsschritten zwischen mindestens zwei Pfaden in einem Mehrfachpfad-Computersystem
          mit einem Hauptcomputer (1), einem Speichersystem (3) mit mindestens
          einem Plattenlaufwerk und einem Cache Speicher und mehreren Pfaden
          zum Koppeln des Hauptcomputers (1), mit dem Speichersystem (3),
          wobei das Verfahren einen Schritt enthält:
(M2)      (A) Auswahl - für den nächsten I/O-Betriebsschritt, der für die Übertragung von Zieldaten zwischen dem Hauptcomputer (1) und dem Speichersystem (3) zuzuordnen ist, eines der mindestens zwei Pfade für die
          Übertragung des nächsten I/0-Betriebsschritts auf der Grundlage eines
          Zustands zuvor zugeordneter I/O-Betriebsschritte in einer Warteschlange
          für das Übertragen über die mindestens zwei Pfade,


(M3.1)    wobei jeder I/O-Betriebsschritt eine zugeordnete Datenzugangszeit bei
          einer Verarbeitung durch das Speichersystem (3) aufweist,


          (M3.1.1) wobei die Datenzugangszeit die Zeit für den Zugriff auf die
                    Zieldaten ist und

                                       -7-



          (M3.1.2) wobei eine kürzere Datenzugangszeit bei einem Zugriffstreffer
                    auf die Zieldaten in einem Cache-Speicher als bei einem Zugriffsfehltreffer auf die Zieldaten in dem Cache-Speicher vorliegt,


(M3.2)    und dass der Schritt (A) einen Schritt zum Auswählen des einen der mindestens zwei Pfade umfasst, auf der Grundlage der Datenzugangszeiten
          der zuvor zugeordneten I/O-Betriebsschritte in der Warteschlange zu den
          mindestens zwei Pfaden.




Patentanspruch 1 nach Hilfsantrag 3 entspricht Anspruch 1 des Hilfsantrags 2 unter Hinzufügen der folgenden Merkmale am Ende des Anspruchs (Merkmalsgliederung seitens des Senats hinzugefügt):


(M3.3)     und wobei zum Bestimmen der Datenzugangszeit eine Ausführungszeit
           für I/O Betriebsschritte einer Anwendung überwacht wird, und


(M3.4)     auf Grundlage dessen bestimmt wird, mit welcher Prozentzahl für einen
           nächsten I/O Betriebsschritt der Anwendung ein Zugriffstreffer oder ein
           Zugriffsfehltreffer im Cache-Speicher erwartet werden kann.


Wegen des Wortlauts der jeweils ein „Computerlesbares Medium“ bzw. einen
„Hauptcomputer“ betreffenden nebengeordneten Ansprüche 5 bzw. 6 nach den
Hilfsanträgen 1 bis 3, sowie der weiteren abhängigen Ansprüche nach Haupt- und
Hilfsanträgen wird auf den Akteninhalt verwiesen.

Die Anmelderin beantragt,


         den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamtes vom 4. September 2007 aufzu-

                                      -8-



       heben und auf die Anmeldung ein Patent mit den folgenden Unterlagen zu erteilen:


       -    Patentansprüche 1 bis 8 laut Anlage zum Schriftsatz vom
            19. Juni 2007 (Bl. 155 bis 158 VA)


            hilfsweise


            Patentansprüche 1 bis 8 laut dem in der mündlichen Verhandlung vom 13. März 2013 überreichten Ersten Hilfsantrag


            weiter hilfsweise


            Patentansprüche 1 bis 8 laut dem in der mündlichen Verhandlung vom 13. März 2013 überreichten Zweiten Hilfsantrag


            weiter hilfsweise


       -    Patentansprüche 1 bis 8 laut dem in der mündlichen Verhandlung vom 13. März 2013 überreichten Dritten Hilfsantrag


       -    Beschreibung Seiten 1, 2 sowie 5 bis 40 laut Anlage zum
            Schriftsatz vom 27. Juni 2001 (Bl. 9, 10 und 13 bis 48 VA)
            sowie Seiten 3, 3a, 4 und 4a laut Anlage zum Schriftsatz
            vom 12. November 2004 (Bl. 116 bis 119 VA)


       -    Zeichnungen (Fig. 1 bis 6) laut Anlage zum Schriftsatz vom
            27. Juni 2001 (Bl. 67 bis 69 VA)


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                      -9-



                                       II.


Die zulässige, insbesondere form- und fristgerechte Beschwerde führt nach dem
Ergebnis der mündlichen Verhandlung nicht zum Erfolg, da sich die Gegenstände
der jeweiligen Ansprüche 1 nach Hauptantrag und den Hilfsanträgen 1 bis 3 als
nicht patentfähig erweisen. Die Frage der Zulässigkeit der jeweiligen Ansprüche
kann daher ebenso dahinstehen (vgl. BGH GRUR 1991, 120, 121 li. Sp. Abs. 3 -
„Elastische Bandage“) wie die im Zurückweisungsbeschluss angesprochene Frage, ob klar sei, was mit dem Gegenstand des Patentanspruch 6 des Hauptantrags
gemäß § 34 Abs. 3 Satz 3 PatG unter Schutz gestellt werden solle.


1.   Die Patentanmeldung betrifft ein Verfahren und Gerät zum Ausgleichen bzw.
     Balancieren der Auslastungen zwischen den Mehrfachpfaden in einem Mehrfachpfad-Computersystem. In Systemen, in denen mehrere Kommunikationspfade gleichzeitig eingesetzt werden, wurde üblicherweise eine einfache
     zyklische Technik eingesetzt, um die Aktivität über die mehreren Pfade hinweg zu balancieren. Diese zyklische Technik maximierte jedoch nicht das
     Systemleistungsvermögen (vgl. Offenlegungsschrift, S. 2, letzter Absatz, bis
     S. 3, dritter Absatz).


     Der Anmeldung liegt daher die Aufgabe zu Grunde, ein verbessertes Verfahren und Gerät zum Balancieren der Aktivität zwischen den mehreren Pfaden
     in einem Mehrfachpfad-Computersystem bereitzustellen (vgl. Offenlegungsschrift, S. 4, erster Absatz).

     Gelöst wird diese Aufgabe durch die jeweiligen Verfahrensansprüche 1 gemäß Hauptantrag bzw. der Hilfsanträge 1 bis 3, sowie durch den jeweils nebengeordneten, auf ein Computerlesbares Medium gerichteten Anspruch 5,
     sowie den jeweils auf einen Hauptcomputer gerichteten Vorrichtungsanspruch 6.

                                       - 10 -



     Wesentlich ist hierbei, dass die Zugangszeit für die I/O-Betriebsschritte in der
     Warteschlange zu den mehreren Systempfaden in die Kriterien für die Auswahl des kürzesten Pfads für den nächsten I/O-Betriebsschritt mit aufgenommen wird. Diese Zeit für jeden I/O-Betriebsschritt für den Zugriff auf die
     Zieldaten in den Systembetriebsmitteln ist zusätzlich zu der Arbitrier- und
     Datenübertragungszeit ein Faktor, der beeinflusst, wie schnell die in der Warteschlange vorliegenden I/O-Betriebsschritte zu einem bestimmten Pfad abgeschlossen werden (vgl. Offenlegungsschrift, S. 13, erster Absatz).




2.   Die Gegenstände der Ansprüche 1 nach Hauptantrag bzw. nach den Hilfsanträgen 1 bis 3 sind nicht patentfähig.


a)   Zum Hauptantrag


     Anspruch 1 nach Hauptantrag beruht unter Berücksichtigung der Druckschrift
     D1 sowie dem fachmännischen Handeln nicht auf einer erfinderischen Tätigkeit des zuständigen Fachmanns. Dieser ist vorliegend als ein Ingenieur der
     Elektrotechnik mit Fachhochschulabschluss und mehrjähriger Erfahrung auf
     dem Gebiet der Kommunikation zwischen einzelnen Komponenten von Datenverarbeitungssystemen anzusehen.


     So ist aus der Druckschrift D1 ein Verfahren zum Verteilen von Eingabe/Ausgabe I/O-Betriebsschritten zwischen mehreren (d.h. mindestens
     zwei) Pfaden („[…] choosing a path for sending a command between main
     processing unit 11-14 and a storage unit“, S. 20, Z. 16-18, i.V.m. Fig. 1 und
     zugehöriger Beschreibung auf S. 8, Z. 5 ff) in einem Mehrfachpfad-Computersystem („data processing system including multi-port mass storage devices“, vgl. S. 1, Z. 6-7, i.V.m. Fig. 1) mit einem Hauptcomputer („main processing unit“), einem Speichersystem („storage unit“) und mehreren Pfaden

                                  - 11 -



(„plurality of paths“) zum Koppeln des Hauptcomputers mit dem Speichersystem (vgl. S. 6, Z. 17-23, i.V.m. Fig. 1) bekannt (Merkmal M1).


Weiterhin ist aus D1 ein Auswahlschritt für den nächsten I/O-Betriebsschritt
(„command“) bekannt, der für die Übertragung zwischen dem Hauptcomputer
(„main processing unit“) und dem Speichersystem („storage unit“) zuzuordnen ist („[…] choosing a path for sending a command between main processing unit 11-14 and a storage unit“, S. 20, Z. 16-18), eines der mehreren (d.h.
mindestens zwei) Pfade für die Übertragung des nächsten I/O-Betriebsschritts („[…] through at least two paths“, vgl. S. 6, Z. 17ff) auf der Grundlage
eines Zustands zuvor zugeordneter I/O-Betriebsschritte in einer Warteschlange mit noch ausstehenden Kommandos („The main processing unit
11-14 controls access to storage units via UCBs […]“, vgl. S. 11, Z. 8-10, mit
einem „path descriptor“ als Teil der zu Grunde liegenden „UCBs“ „The path
descriptor includes […] the number of outstanding commands“, vgl. S. 11,
Z. 24-28) für das Übertragen über die mindestens zwei Pfade (Merkmal M2).


Druckschrift D1 beschreibt weiter verschiedene Charakteristika der Speicherelemente, die eine Abarbeitung von I/O-Betriebsschritten beeinflussen
können (vgl. Seite 11, erster und zweiter Absatz). Hierbei werden Informationen zu den Eigenschaften der einzelnen, vom jeweiligen Hauptcomputer
(„main processing unit“) über einen Pfad („path“) ansprechbaren Speicherelemente („storage units“) bereitgestellt. Die entsprechenden Datenelemente („unit control block“ bzw. „UCB“, ebd.) enthalten unter anderem eine
Information über die Geschwindigkeit des jeweiligen Speicherelements („storage unit speed“). Diese stellt eine allgemeine Beschreibung des Zeitverhaltens des jeweiligen Speicherelements dar und umfasst damit u.a. eine „Datenzugangszeit“ für dieses Speicherelement, ohne dieses explizit auffzuführen. Es ist daher aus der Druckschrift D1 bekannt, dass jeder I/O-Betriebsschritt allgemein ein zugeordnetes Zeitverhalten des Speicherelements („storage unit speed“) bei einer Verarbeitung durch das Speichersystem aufweist

                                  - 12 -



(vgl. S. 11, Z. 8 ff / Merkmal M3.1teilweise, Zuordnung von Eigenschaften des
Speicherelements ohne explizite Nennung einer Datenzugangszeit).


Im Zusammenhang mit den genannten „UCBs“ ist aus Druckschrift D1 weiter
bekannt, dass der Schritt zum Auswählen des Pfades („must determine […]
which paths it may use to communicate with […]“; S10, letzter Abs.) auf
Grundlage der der Speicherelementeigenschaften und somit auch auf Grund
des Zeitverhaltens der Speicherelemente („storage unit speed“ als Information der „UCBs“) erfolgt („The main processing unit 11-14 controls access to
storage units via UCBs linked together in a UCB list“, vgl. S. 11, Z. 8-10).
Dabei umfasst der Auswahlschritt nach Druckschrift D1 einen Schritt zum
Auswählen des einen der mindestens zwei Pfade, auf der Grundlage der zuvor zugeordneten I/O-Betriebsschritte in der Warteschlange zu den mindestens zwei Pfaden („Each Main Processing Unit UCB typically contains […] a
pointer to the active commands of the storage unit […]“, vgl. S. 11, Z. 11ff,
und „The path descriptor includes […] statistics (e.g., the number of times the
path has been used, and the number of outstanding commands)“ S.11, Z. 24-
28, i.V.m. „controls access […] via UCBs“, S. 11, Z. 9-10 / Merkmal
M3.2teilweise, ohne explizite Nennung einer Datenzugangszeit).


Das Verfahren nach Anspruch 1 unterscheidet sich von dem nach Druckschrift D1 demnach in der Anweisung, dass der Schritt zum Auswählen des
einen der mindestens zwei Pfade auf der Grundlage eines bestimmten Merkmals des Zeitverhaltens der jeweiligen Speicherelemente – nämlich einer
„Datenzugangszeit“ – erfolgen soll (vgl. Merkmale M3.1 und M3.2).

Da der Begriff „storage unit speed“ in der D1 nicht näher definiert ist, hat der
Fachmann Veranlassung, sich mit der Frage zu beschäftigen, welche zeitlichen Parameter die Geschwindigkeiten von Speicherelementen bestimmen.

                                   - 13 -



Es gehört dabei zum Wissen des Fachmanns, dass die Geschwindigkeit von
Speicherelementen – neben anderen zeitlichen Parametern wie beispielsweise die Auslese- bzw. Antwortgeschwindigkeit – zwangsläufig durch die
jeweilige Zeit bestimmt wird, die jeder I/O-Betriebsschritt für den Zugriff auf
Zieldaten benötigt – was nichts anderes als eine Datenzugangszeit im Sinne
der vorliegenden Anmeldung bedeutet (vgl. OS, S. 13, erster Abs.). Damit ist
eine solche Datenzugangszeit als zeitlicher Parameter inhärent in dem Begriff „storage unit speed“ enthalten. Dieser Parameter dient - wie auch in der
vorliegenden Anmeldung - allgemein dazu, den zeitlichen Einfluss des Speicherelements bei der Abarbeitung eines I/O-Betriebsschritts gegenüber dem
Einfluss des Hauptcomputers („Arbitrierungszeit“) und dem Einfluss des Pfades bzw. Übertragungsweges („Übertragungszeit“) abzugrenzen. Für den
Fachmann liegt es somit nahe, bei einem Verfahren zum Verteilen von I/O-Betriebsschritten auch die Datenzugangszeit, die jedem I/O-Betriebsschritt
zugeordnet wird, zu berücksichtigen (Merkmal M3.1Rest) und als Konsequenz
das Auswählen eines von mehreren (und damit mindestens zwei) Pfaden auf
der Grundlage der Datenzugangszeiten der zuvor zugeordneten I/O-Betriebsschritte durchzuführen (Merkmal M3.2Rest).


Das Verfahren nach Anspruch 1 gemäß Hauptantrag ergibt sich somit für
den Fachmann in naheliegender Weise aus Druckschrift D1 und beruht daher nicht auf einer erfinderischen Tätigkeit.


Die Anmelderin vertritt in der mündlichen Verhandlung die Auffassung, dass
es im Unterschied zur vorliegenden Anmeldung bei der in Druckschrift D1
genannten Geschwindigkeit der einzelnen Speicherelemente („storage unit
speed“), lediglich um eine Verarbeitungsgeschwindigkeit des jeweiligen Speicherelements für ein Abarbeiten von Datenblöcken handele. Dieser Interpretation kann nicht gefolgt werden. So findet sich in Druckschrift D1 kein
Hinweis darauf, dass sich die dort genannte Geschwindigkeit („storage unit
speed“) des Speicherlements in der Verabarbeitungsgeschwindigkeit von Da-

                                       - 14 -



     tenblöcken erschöpft. Für den Fachmann ergibt sich vielmehr aus Druckschrift D1 ganz allgemein der Hinweis auf das Zeitverhalten der Speicherelemente, das auch zwangsläufig eine Datenzugangszeit mit umfasst. Im Übrigen steht dem Wortlaut des Anspruchs 1 die Verwendung weiterer Parameter als Grundlage zum Auswahlschritt der zuvor zugeordneten I/O-Betriebsschritte nicht entgegen.


     Die Anmelderin verweist in ihrer Argumentation weiterhin darauf, dass das in
     der Druckschrift D1 offenbarte Verfahren bei der Pfadauswahl auf einem
     „rotating path“ Algorithmus beruhe, der allein auf der Anzahl der I/O-Betriebsschritte in der Warteschlange und nicht auf Datenzugangszeiten der
     I/O-Betriebsschritte basiere. Ein solches Vorgehen ist jedoch nur für ein
     Ausführungsbeispiel („an illustrative embodiment“) der Druckschrift D1 nach
     Fig. 3 beschrieben (vgl. zugehörige Beschreibung S. 20, Z. 16ff). Dieses Beispiel steht aber einer Pfadauswahl an Hand der in den „UCBs“ beschriebenen Informationen (vgl. S. 10, letzter Absatz, bis S. 11, dritter Absatz) nicht
     entgegen.




b)   Zum Hilfsantrag 1


     Anspruch 1 nach Hilfsantrag 1 beruht ebenfalls unter Berücksichtigung der
     Druckschrift D1 sowie dem fachmännischen Handeln auf keiner erfinderischen Tätigkeit.


     Anspruch 1 gemäß Hilfsantrag 1 unterscheidet sich vom Anspruch 1 des
     Hauptantrags darin, dass


     -    es sich beim Speichersystem um ein Speichersystem „mit unterschiedlichen Speichertypen“ handelt (in Merkmal M1*), und

                                  - 15 -



-    definiert wird, dass die „Datenzugangszeit die Zeit für den Zugriff auf
     die Zieldaten ist“ (Merkmal 3.1.1).


Diese Merkmale können jedoch ebenfalls keine erfinderische Tätigkeit begründen. Wie zum Anspruch 1 nach Hauptantrag ausgeführt, ist aus der
Druckschrift D1 ein Verfahren zur Verteilung von Eingabe/Ausgabe I/O-Betriebsschritten mit dem Merkmal M2, sowie den Merkmalen 3.1 und 3.2 mit
Ausnahme einer Nennung der Datenzugangszeit bekannt. Eine Wahl der
Datenzugangszeit als Kriterium für die Auswahl von Pfaden entsprechend
den Merkmalen M3.1 und M3.2 liegt dabei - ausgehend von D1 - im Rahmen
des fachmännischen Handelns. Auf die entsprechenden, vorstehenden Ausführungen zu diesen Merkmalen wird Bezug genommen.


Wie vorstehend ausgeführt ist die Zeit für den Zugriff auf die Zieldaten – und
somit die Datenzugangszeit – inhärent als zeitlicher Parameter im Begriff
„storage unit speed“ enthalten (vgl. Ausführungen zur Datenzugangszeit in
den Merkmalen M3.1 und M3.2 des Anspruchs 1 des Hauptantrags). Es liegt
somit für den Fachmann nahe, die Datenzugangszeit als Zeit für den Zugriff
auf die Zieldaten zu berücksichtigen (Merkmal M3.1.1). Auf die entsprechende Argumentation zum Hauptantrag, welche die jetzt in den Anspruchswortlaut eingefügte Definition bereits berücksichtigt, wird verwiesen.


Ein Speichersystem mit unterschiedlichen Speichertypen entsprechend des
gegenüber dem Hauptantrag geänderten Merkmals M1* ist ebenfalls aus
Druckschrift D1 bekannt (vgl. z.B. „it being understood that any mass storage
technology […] can be substituted“, S. 1, zweiter Absatz, sowie Fig. 2, Bezugszeichen 201, 203, 205). Zudem kann gemäß D1 eine Speichereinheit
(„storage unit“) aus einzelnen Speicherelementen oder selbst wiederum aus
Gruppen von Speicherelementen bestehen und beschreibt auch in dieser
Hinsicht in ihrem Verhalten unterschiedliche Typen von Speicherelementen
(vgl. S. 1, zweiter Absatz). Eine Beschränkung der Lehre der D1 auf nur ei-

                                       - 16 -



     nen Speichertyp, wie sie die Anmelderin als Argument vorgebracht hat, kann
     der Senat in der Beschreibung des Speichersystems in Druckschrift D1 daher nicht erkennen. Für die restlichen Teilmerkmale des Merkmals M1*, welche mit Merkmal M1 des Anspruchs 1 im Hauptantrag übereinstimmen, wird
     auf die Ausführungen zum Hauptantrag verwiesen (Merkmal M1*).


     Auch das Verfahren nach Anspruch 1 gemäß Hilfsantrag 1 ergibt sich somit
     für den Fachmann in naheliegender Weise aus Druckschrift D1 und beruht
     daher nicht auf einer erfinderischen Tätigkeit.




c)   Zum Hilfsantrag 2


     Anspruch 1 nach Hilfsantrag 2 beruht ebenfalls unter Berücksichtigung der
     Druckschrift D1 sowie dem fachmännischen Handeln auf keiner erfinderischen Tätigkeit.


     Anspruch 1 gemäß Hilfsantrag 2 unterscheidet sich vom Anspruch 1 des
     Hauptantrags darin, dass


       -   es sich beim Speichersystem um ein Speichersystem „mit mindestens
           einem Plattenlaufwerk und einem Cache Speicher“ handelt (Merkmal
           M1**),


       -   die Datenzugangszeit als „Zeit für den Zugriff auf die Zieldaten“ definiert ist (Merkmal M3.1.1), und diese für ein Speichersystem entsprechend Merkmal M1** das Verhalten zeigt, dass „eine kürzere Datenzugangszeit bei einem Zugriffstreffer auf die Zieldaten in einem Cache-Speicher als bei einem Zugriffsfehltreffer auf die Zieldaten in dem
           Cache-Speicher vorliegt“ (Merkmal M3.1.2).

                                  - 17 -



Diese Merkmale können jedoch keine erfinderische Tätigkeit begründen. Wie
zum Anspruch 1 nach Hauptantrag ausgeführt, ist aus der Druckschrift D1
ein Verfahren zur Verteilung von Eingabe/Ausgabe I/O-Betriebsschritten mit
dem Merkmal M2, sowie den Merkmalen M3.1 und M3.2 mit Ausnahme einer expliziten Nennung der Datenzugangszeit bekannt. Eine Wahl der Datenzugangszeit als Kriterium für die Auswahl von Pfaden entsprechend den
Merkmalen M3.1 und M3.2 entsprechend der Beschreibung der Datenzugangszeit als die Zeit für den Zugriff auf die Zieldaten (Merkmal M3.1.1) liegt
dabei - ausgehend von D1 - für den Fachmann nahe (vgl. Ausführungen zum
1. Hilfsantrag). Auf die entsprechenden vorstehenden Ausführungen zu diesen Merkmalen wird Bezug genommen.


Druckschrift D1 sieht allgemein vor, dass es sich bei den Elementen des beschriebenen Speichersystems um eine beliebige Kombination, bspw. von
Plattenlaufwerken („hard disk“) und auch Cache Speichern („cache memory“)
handeln kann („it beeing understood, that any mass storage technology --
i.e., hard disk, floppy disk, optical disk, tape, cache memory or other technology -- can be substituted“, vgl. S. 1, Zn. 18-21). Druckschrift D1 beschreibt
weiterhin ein Verfahren zum Verteilen von Eingabe/Ausgabe I/O-Betriebsschritten mit einem solchen Speichersystem, welches bspw. in Fig. 2 der D1
dargestellt ist, mit Plattenlaufwerken (Mehrzahl von „storage devices“, Fig. 2,
Bezugszeihen 205) und einem Cache Speicher (Schreib- und Lesebuffer,
„buffer“, Fig. 2, Bezugszeichen 201, 203). Für die weiteren, mit Merkmal M1*
des Anspruchs 1 in Hilfsantrag 1 übereinstimmenden Teilmerkmale des
Merkmals M1** sei auf die entsprechenden Ausführungen zu Hilfsantrag 1
verwiesen. Aus Druckschrift D1 ist daher ein Verfahren zum Verteilen von
Eingabe/Ausgabe I/O-Betriebsschritten zwischen mindestens zwei Pfaden in
einem Mehrfachpfad-Computersystem mit einem Hauptcomputer, einem
Speichersystem mit mindestens einem Plattenlaufwerk und einem Cache-Speicher (vgl. Fig. 2, Bezugszeichen 201, 203, 205) und mehreren Pfaden

                                   - 18 -



zum Koppeln des Hauptcomputers mit dem Speichersystem bekannt (Merkmal M1**).


Der Auffassung der Anmelderin, dass es sich bei den in Druckschrift D1,
Fig. 2, als „Buffer“ bezeichneten Elementen 201 und 203 nur um einen
Pufferspeicher, nicht um einen Cache handelt, kann sich der Senat nicht
anschließen. Denn Druckschrift D1 unterscheidet hierbei ausdrücklich
zwischen den genannten Buffer-Elementen (Bezugszeichen 201, 203) und
einer   jeweiligen   Pufferung     der      Speicherelemente   („Data   Buffer“,
Bezugszeichen 204). Hierbei sind die „Buffer“ 201 und 203 von einem
Prozessor („Microprocessor“) gesteuert und stellen somit funktional für den
Fachmann erkennbar einen üblichen Cache-Speicher dar, wie er in D1
beispielgebend auf S. 1, Z. 18 ff genannt ist.


Es ist dabei für den Fachmann offensichtlich, dass eine kürzere Datenzugangszeit bei einem Zugriffstreffer auf die Zieldaten in einem Cache-Speicher als bei einem Zugriffsfehltreffer auf die Zieldaten in dem Cache-Speicher vorliegt (Merkmal M3.1.2); somit kann auch dieses Merkmal ebenfalls
keine erfinderische Tätigkeit begründen.


Im Übrigen stellen die hinzugenommenen Merkmale lediglich aggregative
Mittel dar, welche in Zusammenschau keinen synergistischen Effekt erkennen lassen. Ein solcher ist im Übrigen auch von der Anmelderin nicht vorgetragen worden.


Das Verfahren nach Anspruch 1 gemäß Hilfsantrag 2 ergibt sich somit für
den Fachmann in naheliegender Weise aus Druckschrift D1 und beruht daher nicht auf einer erfinderischen Tätigkeit.

                                      - 19 -



d)   Zum Hilfsantrag 3


     Anspruch 1 nach Hilfsantrag 3 beruht ebenfalls unter Berücksichtigung der
     Druckschrift D1 sowie dem fachmännischen Handeln auf keiner erfinderischen Tätigkeit.


     Anspruch 1 gemäß Hilfsantrag 3 ergänzt Anspruch 1 des Hilfsantrags 2
     durch die zusätzlich angefügten Merkmale, wonach


       -   zum Bestimmen der Datenzugangszeit eine Ausführungszeit für I/O-Betriebsschritte einer Anwendung überwacht wird (vgl. Merkmal M3.3),
           und


       -   auf Grundlage dessen bestimmt wird, mit welcher Prozentzahl für einen nächsten I/O-Betriebsschritt der Anwendung ein Zugriffstreffer
           oder ein Zugriffsfehltreffer im Cache-Speicher erwartet werden kann
           (vgl. Merkmal M3.4).


     Hinsichtlich der Merkmale M1, M2, M3.1.1, M3.1.2 und M3.2 des Anspruchs
     sei auf die Ausführungen zu den entsprechenden, übereinstimmenden
     Merkmalen des Anspruch 1 gemäß Hilfsantrag 2 verwiesen.


     Aus Druckschrift D1 ist dabei bekannt, die Ausführung der I/O-Betriebsschritte einer Anwendung allgemein zu überwachen (vgl. bspw. „error statistics“ der UCBs, sowie „statistics“ und „path state“ der damit verbundenen
     „path descriptors“, vgl. S.11, Z. 13 und Z. 24-30). In diesem Kontext ist dem
     Fachmann nahegelegt, auf Grund der weiterhin in den genannten „UCBs“
     enthaltenen „storage unit speed“, auch die Ausführungszeit der I/O-Betriebsschritte zu überwachen (vgl. hierzu auch die entsprechenden Ausführungen
     zum Hauptantrag), um zu einer Aussage über das Zeit- bzw. Geschwindig-

                                  - 20 -



keitsverhalten der jeweiligen Speicherelemente zu gelangen. Dies schließt
auch ein Bestimmen der Datenzugangszeit mit ein (Merkmal M3.3).


Weiterhin beschreibt Druckschrift D1 allgemein die Bestimmung von Fehlerstatistiken für die jeweiligen Speicherelemente („error statistics“, vgl. S.11,
Z. 13 / Merkmal M3.4teilweise, ohne Nennung, mit welcher Prozentzahl für
einen nächsten I/O-Betriebsschritt der Anwendung ein Zugriffstreffer oder ein
Zugriffsfehltreffer im Cache-Speicher erwartet werden kann).


Der Fachmann erhält damit aus der Information der „UCBs“, die gemäß D1
Grundlage der Pfadauswahl sind, den Hinweis, auch Fehlerstatistiken bei der
Auswahl der Pfade zum Zugriff auf die Speicherelemente für I/O-Betriebsschritte zu berücksichtigen. Für den zuständigen Fachmann ergibt sich hieraus die Veranlassung, aus der begrenzten Zahl möglicher Fehlerindizien
(bspw. nicht erfolgreicher I/O-Betriebsschritte oder verzögerter I/O-Betriebsschritte) eine geeignete Auswahl zu treffen, die für das Zeitverhalten bei der
Abarbeitung der I/O-Schritte relevant ist. Die Berücksichtigung des typischen
Cache-Verhaltens, das sich in den durch Zugriffsfehltreffer bedingten Verzögerungen widerspiegelt, liegt dabei angesichts der in D1 vorgesehenen
Cache-Speicher (vgl. Ausführungen zu Hilfsantrag 2) im Rahmen des fachmännischen Handelns. Dabei assoziiert der Fachmann mit dem Begriff
„Fehlerstatistik“ bzw. „error statistics“, wie er der D1 auf S. 11, Z. 13, im Zusammenhang mit einer „storage unit“ aufgeführt wird, eine Prozentzahl bzgl.
Zugriffsfehltreffern. Somit liegt es für den Fachmann nahe, zu bestimmen, mit
welcher Prozentzahl für einen nächsten I/O Betriebsschritt der Anwendung
ein Zugriffsfehltreffer im Cache-Speicher erwartet werden kann. Die Berücksichtigung von Zugriffsfehltreffern zur Pfadauswahl für I/O-Betriebsschritte
bei der Verwendung von Cache-Speichern in einem entsprechenden Mehrfachpfad-Computersystem kann daher ausgehend von Druckschrift D1 für
den einschlägig vorgebildeten Fachmann keine erfinderische Tätigkeit begründen (Merkmal M3.4Rest).

                                        - 21 -



     Im Übrigen stellen die hinzugenommenen Merkmale lediglich aggregative
     Mittel dar, welche in Zusammenschau keinen synergistischen Effekt erkennen lassen. Ein solcher ist im Übrigen auch von der Anmelderin nicht vorgetragen worden.


     Das Verfahren nach Anspruch 1 gemäß Hilfsantrag 3 ergibt sich somit für
     den Fachmann in naheliegender Weise aus Druckschrift D1 und beruht daher nicht auf einer erfinderischen Tätigkeit.




3.   Mit den jeweils nicht patentfähigen Ansprüchen 1 nach Hauptantrag bzw.
     Hilfsantrag 1 bis Hilfsantrag 3 sind auch die hiervon abhängig formulierten
     jeweiligen Verfahrensansprüche 2 bis 4, die jeweiligen nebengeordneten, auf
     ein Computerlesbares Medium gerichteten Ansprüche 5, die jeweiligen nebengeordneten, auf einen Hauptcomputer gerichteten Ansprüche 6, sowie
     die jeweiligen auf diese rückbezogenen Ansprüche 7 und 8 nicht schutzfähig,
     da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet ist
     (vgl. BGH GRUR 2007, 862, Leitsatz – „Informationsübermittlungsverfahren
     II“).




4.   Nachdem die jeweiligen Anspruchssätze nach Hauptantrag bzw. den jeweiligen Hilfsanträgen 1 bis 3 nicht patentfähig sind, war die Beschwerde zurückzuweisen.




Maile                 Schwarz              Dr. Schwengelbeck            Altvater


                                                                              Hu
