---
ecli: "ECLI:DE:BPatG:2009:220409B19Wpat44.06.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 44/06"
decided: "2009-04-22"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2009&Sort=1&Seite=30&nr=14416&anz=1436&pos=459&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2009-04-22_19_W-pat_44_06_NA_0.txt"
---

# Bundespatentgericht, 19 W (pat) 44/06 vom 2009-04-22

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 44/06                                                    Verkündet am
_______________                                                      22. April 2009
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung DE 100 31 671.9-55


…




hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 22. April 2009 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Ing. Bertl der Richterin Kirschneck und der Richter Dipl.-Ing. Groß
und Dr.-Ing. Scholz




BPatG 154
08.05

                                        -2-



beschlossen:


                         Die Beschwerde wird zurückgewiesen.


                                     Gründe


                                         I.


Das Deutsche Patent- und Markenamt - Prüfungsstelle für Klasse G 05 B - hat die
am 29. Juni 2000 mit der Priorität vom 2. Juli 1999 (US - AKZ 09-347 178) eingereichte Anmeldung durch Beschluss vom 2. Juni 2006 mit der Begründung zurückgewiesen, dass der Gegenstand des Patentanspruchs gegenüber dem Stand der
Technik nicht neu sei.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Die Anmelderin stellte den Antrag, den Beschluss des Deutschen Patent- und
Markenamts vom 2. Juni 2006 aufzuheben und das Patent mit folgenden Unterlagen zu erteilen:


        1. Hauptantrag:


        Patentanspruch 1 vom 12. Dezember 2006


        Patentansprüche 2 bis 6 vom 29. Mai 2006


        Beschreibung S. 1, 5a, 5b vom 12. Dezember 2006


        Ursprüngliche Beschreibung S. 2 bis 4, 6 bis 37 und Zeichnungen
        Figuren 1 bis 4

                                        -3-



         2. Hilfsantrag:


         Patentansprüche 1 bis 12 überreicht in der mündlichen Verhandlung


         Übrige Unterlagen wie Hauptantrag


Die Anmelderin ist der Auffassung der Stand der Technik, insbesondere der Aufsatz


       Goldman, R.P.; Boddy, M.S.: „A Constraint-Based Scheduler for
       Batch Manufacturing” in IEEE Expert, Volume 12, Issue 1,
       Jan/Feb 1997, Seiten 49 - 56,


zeige keine Prozesssteuerung, in die die beanspruchte Geräteauswahl aus Geräteklassen integriert sei. Vielmehr sei dort nur ein theoretischer Entwurf eines Fahrplans (schedule) skizziert, dessen steuerungstechnische Umsetzbarkeit für den
Fachmann nicht erkennbar sei. Es sei zwar in Fig. 1 ein „plant control system” angedeutet. Tatsächliche Regelungs- oder Steuerungsprozeduren seien aber nicht
erwähnt und beschrieben.


Wegen weiterer Einzelheiten wird auf den Akteninhalt verwiesen.


                                         II.


Die Beschwerde ist zwar zulässig, konnte aber keinen Erfolg haben.

                                       -4-



1. Gegenstand des Patents, Aufgabe


Die Anmeldung betrifft ein Prozessregelsystem. Eine verfahrenstechnische Anlage
mit Reaktoren, Mischern, Vorratsbehältern, sowie verbindenden Leitungen, Ventilen, Pumpen usw. soll in „Stapelprozessen“ betrieben werden, was wohl eine wörtliche Übersetzung von „batch process“ ist, und offensichtlich einen diskontinuierlichen Chargenprozess bezeichnen soll. Für einen solchen Prozess muss nach einem „Rezept“ ein „Strang“ aus Mischern, Reaktionsgefäßen usw. zusammengestellt werden. Die Reservierung dieser Elemente erfolgt normalerweise frühzeitig
in einem relativ starren Fahrplan (schedule), was bei Geräteausfall oder kurzfristigen Änderungen zu Schwierigkeiten führt.


Anmeldungsgemäß soll deshalb die Auswahl dynamisch erst während des Prozesses erfolgen. Die Geräte werden dazu in Klassen (Mischer, Reaktionsgefäße,
Filter usw.) eingeteilt, aus denen Prioritätslisten erstellt und daraus dann zeitnah
während des laufenden Prozesses das gerade verfügbare Gerät mit der höchsten
Priorität ausgewählt wird.


In der Beschreibungsseite 5a vom 12. Dezember 2006 wird dazu als Aufgabe genannt, ein Prozessregelsystem zur Regelung bzw. Steuerung eines Prozesses bereit zu stellen, der mit einfachen Mitteln eine Vielzahl von replizierten Ausrüstungen steuert oder regelt.


Dazu ist nach Anspruch 1 gemäß Hauptantrag (mit einer für diesen Beschluss eingefügten Gliederung) vorgesehen ein:


        Prozessregelsystem zur Regelung bzw Steuerung eines Prozesses, insbesondere eines Stapelprozesses, umfassend


        a)   - einen Speicher zum Speichern von Geräteprozeduren und

                                      -5-



       b)    - eine Steuerung, die mit einer Vielzahl von Geräten verbunden und derart ausgebildet ist, dass sie diese gemäß
                den Geräteprozeduren steuert,


       c)    wobei der Speicher zur Speicherung von Geräteklassen ausgebildet ist,


       c1) wobei der Speicher Listen von Geräten enthält, die identische oder ähnliche Funktionen innerhalb des Prozesses ausführen, und


       d)    die Steuerung derart ausgebildet ist, dass die Steuerung anhand der Geräteklassen im Speicher


       d1) und von Prioritätslisten


       d2) während der Ausführung der Geräteprozedur


       d3) mindestens ein spezifisches Gerät dynamisch zur Durchführung eines Teils der Geräteprozedur auswählt und dann
             steuert.


Der Anspruch 1 nach Hilfsantrag lautet:


       Prozessregelsystem zur Regelung bzw Steuerung eines Prozesses, umfassend:

                              -6-



a)   - einen Speicher zum Speichern von Geräteprozeduren,


a1) wobei mindestens eine Geräteprozedur eine nicht spezifische Angabe eines zur Durchführung der Geräteprozedur
     geeigneten Geräts enthält, und


b)   - eine Steuerung, die mit einer Vielzahl von Geräten verbunden und derart ausgebildet ist, dass sie diese gemäß
       den Geräteprozeduren steuert,


c)   wobei der Speicher zur Speicherung von Geräteklassen ausgebildet ist


c1) und Listen von Geräten enthält, die identische oder ähnliche
     Funktionen innerhalb des Prozesses ausführen, und


d)   die Steuerung derart ausgebildet ist, dass die Steuerung anhand der Geräteklassen im Speicher


d1) und anhand von Prioritätslisten


d2) während der Ausführung mindestens einer Geräteprozedur


d3) mindestens ein spezifisches Gerät dynamisch zur Durchführung der Geräteprozedur auswählt und dann steuert.

                                        -7-



Der nebengeordnete Anspruch 7 nach Hilfsantrag lautet:


       „Verfahren zum Steuern eines Prozesses mit einer Steuerung, die
       zur Steuerung einer Vielzahl von Geräten an diese angeschlossen
       ist, wobei die Steuerung einen Speicher mit Listen der Geräte umfasst, die die Geräte in Geräteklassen zusammenfasst, die identische oder ähnliche Funktionen innerhalb des Prozesses ausführen, wobei die Steuerung:
       - mindestens eine Steuerprozedur startet, um eine Folge von Geräteprozeduren, die dem Prozess zugeordnet sind, auszuführen, wobei jede Geräteprozedur mindestens ein Gerät verwendet, das einer der Geräteklassen zugeordnet ist;
       - mindestens ein spezifisches Gerät automatisch nach dem Starten der mindestens einen Steuerprozedur zur Durchführung einer Geräteprozedur auswählt, wobei für die Geräteprozedur ein
          bestimmtes Gerät aus einer geeigneten Geräteklasse als das
          Gerät ausgewählt wird, das während der Ausführung der Geräteprozedur verwendet wird.“


2. Fachmann


Als Fachmann sieht der Senat einen Diplomingenieur (FH) der Fachrichtung Regelungstechnik mit Erfahrung in der Entwicklung von Steuerungen und Regelungen für verfahrenstechnische Anlagen.


3. Auslegung der Ansprüche


Einige Merkmale der Ansprüche sind aus sich heraus nicht ohne weiteres verständlich oder eindeutig und bedürfen der Auslegung:

                                       -8-



Unter einem Prozessregelsystem zur Regelung bzw. Steuerung eines Prozesses,
insbesondere eines Stapelprozesses, versteht der Fachmann ein Steuer- bzw. Regelsystem (das gewöhnlich Steuer- und Regelkomponenten umfassen wird) für eine verfahrenstechnische Anlage und darauf ablaufende diskontinuierliche Chargenprozesse, wie bereits unter Punkt 1 beschrieben. Der Begriff „System“ sagt
ihm dabei, dass es aus mehreren gegebenenfalls verteilten Komponenten - auch
mehreren Rechnern - bestehen kann.


Unter den abgespeicherten Geräteprozeduren versteht der Fachmann die jeweiligen Regel- und Steuerprogramme. Der bestimmte Artikel „der Speicher“ in Merkmal c) und c1) könnte so verstanden werden, dass damit auf den Speicher für die
Geräteprozeduren nach Merkmal a) Bezug genommen wird. Dem Fachmann ist
aber geläufig, dass der physikalische Ort der Abspeicherung bei solchen Systemen völlig unbedeutend ist, dass es somit auf eine physikalische Identität der
Speicher nicht ankommen kann. Im Übrigen wäre eine solche Identität auch gar
nicht ursprünglich offenbart. Er wird also den Merkmalen a) und c) insoweit nur die
Möglichkeit der Abspeicherung in einem Speicher entnommen.


Dass der Speicher gemäß Merkmal c) zur Speicherung von Geräteklassen ausgebildet ist, wird der Fachmann so verstehen, dass dieser Speicher für die klassenweise organisierte Abspeicherung der Gerätedaten vorgesehen ist. Eine besondere Ausbildung benötigt der Speicher dafür nicht. Für Datenspeicher ist der Inhalt
der abgespeicherten Daten grundsätzlich bedeutungslos.


Die Geräteklassen ergeben sich durch die Art der Geräte, wobei der Fachmann im
vorliegenden Fall der in Merkmal c1) beanspruchten Funktion (z. B. Reaktion, Filterung, Absperrung) auch die Bauart (Reaktionsgefäß, Filter, Ventil) zuordnen
wird.

                                          -9-



Unter den Prioritätenlisten in Merkmal d1) wird der Fachmann eine Auflistung verstehen, bei der den in Frage kommenden Geräten einer Klasse eine Reihung zugeordnet wird. Sie kann der Eignung der Geräte für den vorgesehenen Prozess
entsprechen, muss es aber nicht. So entspricht zum Beispiel die in der Beschreibung auf Seite 32 unten angesprochene Reihung nach der Ruhezeit nicht ohne
weiteres der Eignung für den Prozess. Ob die Prioritätenliste abgespeichert vorliegt, oder jeweils aktuell erstellt wird, bleibt im Anspruch 1 offen.


„Während der Ausführung mindestens eine Geräteprozedur“ nach Merkmal d2)
bezieht der Fachmann auf den gesamten Prozess. Selbstverständlich muss die
Auswahl und Zuordnung des jeweiligen Geräts vor der Ausführung der eigenen
Geräteprozedur erfolgen. Deshalb kann dieses Merkmal auch nicht für das zeitlich
erste verwendete Gerät gelten.


Die „nicht spezifischen Angaben“ nach Merkmal a1) im Anspruch 1 nach Hilfsantrag erkennt der Fachmann als Platzhalter oder Sammelbegriff für die spezifischen
Angaben, nämlich die Geräte- und Regelparameter. Das Merkmal sagt dem Fachmann damit, dass die abgespeicherten Geräteprozeduren nicht parametrisiert
sind.


Der Anspruch 7 nach Hilfsantrag ist im Unterschied zum Gegenstand des Anspruchs 1 auf ein Verfahren zur Steuerung gerichtet, wobei die Regelung gestrichen wurde. Weiterhin wählt dort die Steuerung das spezifische Gerät nach dem
Starten der Steuerprozedur aus, was aber der Fachmann nach Überzeugung des
Senats als inhaltsgleich mit der Auswahl „während der Ausführung“ gemäß Anspruch 1 erkennt. Auch im Übrigen sieht der Fachmann nach Überzeugung des
Senats den Anspruch 7 in seinem Sinngehalt inhaltsgleich mit dem Anspruch 1
nach Hauptantrag. Etwas anderes wurde auch nicht von der Anmelderin vorgetragen.

                                          - 10 -



4. Stand der Technik


Der nächstkommende Stand der Technik ist der Aufsatz von Goldman:
„A Constraint-Based Scheduler…“ a. a. O. Er zeigt ein unter anderem aus
„Scheduler“ und „Plant control system“ bestehendes System zur Prozessteuerung
für eine Anlage mit vielen parallel angeordneten Vorrats- und Speichertanks, Vormischern und Reaktoren (S. 53, Fig. B), die im Chargenbetrieb (Titel, S. 49, l. Sp.,
Abs. 1) nach Plan zusammengestellt werden. Die Nachteile eines starren Plans
(Schedule) sollen vermieden, die Betriebsmittel für schnelle Reaktion flexibel zugewiesen werden (S. 49, mittl. u. r. Sp.). Auch dort wird aus einer Klasse von Geräten (S. 53, r. Sp „premixers“, „reactors“; Fig. B, Absatz „Need for flexibility“ im
Kasten rechts neben Fig. B) ein Gerät ausgewählt. Das kann zeitlich vorlaufend
bei der Erstellung des Fahrplans, aber auch „just in time“ (S. 52, mittl. Sp. Abs. 2)
durch Fahrplanmodifikation oder Fahrplanänderung (rescheduling) erfolgen (S. 54,
l. Sp.).


Damit ist mit den Worten des Anspruchs 1 nach Hauptantrag bekannt ein:


           Prozessregelsystem zur Regelung bzw Steuerung eines Prozesses, insbesondere eines Stapelprozesses (S. 49, l. Sp.), umfassend


           a)     - einen Speicher zum Speichern von Geräteprozeduren
                    (Fig. 1, Plant control system, Plant Database) und


           b)     - eine Steuerung, die mit einer Vielzahl von Geräten verbunden und derart ausgebildet ist, dass sie diese gemäß
                    den Geräteprozeduren steuert (Fig. 1, Plant control
                    system),

                                         - 11 -



        c)    wobei der Speicher (Plant Database) zur Speicherung von
              Geräteklassen ausgebildet (im Sinne von vorgesehen) ist,


        c1) wobei der Speicher Listen von Geräten enthält, die identische oder ähnliche Funktionen innerhalb des Prozesses ausführen (S. 50, Fig. 1, r. Sp., Z. 20-25 i. V. m. S. 51, mittl. Sp.
              Abs. 2, „subclasses and central classes“ und Fig. B mit Text),
              und


        d)    die Steuerung derart ausgebildet ist, dass die Steuerung anhand der Geräteklassen im Speicher (S. 53 Abs. „Resource
              assignment“, Fig. B) und


        d2) während der Ausführung der Geräteprozedur (just in time, rescheduling)


        d3) mindestens ein spezifisches Gerät dynamisch zur Durchführung eines Teils der Geräteprozedur auswählt und dann
              steuert.


Im Unterschied zum Gegenstand des Anspruchs 1 nach Hauptantrag ist dort eine
Prioritätsliste nicht erwähnt.


Einen Unterschied in der Art der Steuerung kann der Senat entgegen den Ausführungen der Anmelderin nicht erkennen. Auch dort besteht das Gesamtsystem aus
dem Scheduler mit den Auswahlroutinen und der eigentlichen Steuerung, dem
Plant control system. Dass der Scheduler nur einmalig vorab dem Plant control
system seine Daten mitteilen und dann untätig bleiben sollte widerspricht ganz offensichtlich der auf Seite 49 dargelegten Intention eines flexiblen Plans, und auch
im Besonderen der auf S. 54 beschriebenen Planmodifikation oder Planänderung
(rescheduling). Das setzt auch eine enge Verzahnung von Prozesssteuerung und

                                        - 12 -



Scheduler voraus, wobei der Scheduler zwangsläufig einen Teil der Steuerungsaufgaben, nämlich die zeitflexible Zuweisung der Resourcen, übernimmt.


5. Technizität


Der Senat zieht nicht in Zweifel, dass die beanspruchten Systeme und das Verfahren zu ihrer Steuerung technisch ist.


Ob für manche Merkmale neben der technischen Auslegung auch noch eine nichttechnische Auslegung möglich wäre, ist ohne Bedeutung, da die jeweils beanspruchten Gegenstände in ihrer Gesamtheit betrachtet technischen Charakter
haben.


6. Erfinderische Tätigkeit


6.1 Der Gegenstand des Anspruchs 1 nach Hauptantrag ist nicht erfinderisch.


Ausgehend von dem bekannten System steht der Fachmann vor der Aufgabe dem
System Kriterien mitzuteilen, nach denen es das Gerät, das dann tatsächlich zum
Einsatz kommt, aus den möglichen Geräten der jeweiligen Klasse bestimmt. Ohne
solche Kriterien kann ein System nämlich kein Gerät aus einer Mehrzahl von Geräten auswählen. Diese Kriterien können vielfältig sein und die Eignung für den
vorgesehenen Prozess, die Ruhezeit, die Kosten oder auch eine zufallsähnliche
Wahl nach Art des ersten besten Geräts umfassen. Stets resultiert aber daraus eine Reihung der Geräte nach diesen Kriterien, und somit eine Prioritätenliste. Damit ist der Fachmann ohne erfinderische Überlegungen bei dem System nach Anspruch 1 angelangt.


6.2 Der Gegenstand des Anspruchs 1 nach Hilfsantrag ist nicht erfinderisch.

                                     - 13 -



Der Anspruch 1 nach Hilfsantrag unterscheidet sich vom Anspruch 1 nach Hauptantrag nur durch die unparametrisiert abgespeicherten Geräteprozeduren nach
Merkmal a1). Das ist aber allgemein üblich und kann keine erfinderische Leistung
begründen.


6.3 Weitere Ansprüche


Mit den nicht patentfähigen Ansprüchen 1 nach Hauptantrag und Hilfsantrag fallen
auch die jeweils darauf rückbezogenen Ansprüche 2 bis 6.


Da das Patent nur so erteilt werden darf, wie es beantragt ist, kommt eine Erteilung des nebengeordneten Verfahrensanspruchs 7 und der darauf rückbezogenen
Ansprüche 8 bis 12 nach Hilfsantrag ohne den nicht patentfähigen Anspruch 1
nach Hilfsantrag nicht in Betracht (BGH GRUR 2007, 862 „Informationsübermittlungsverfahren II“). Im Übrigen ist aber auch das Verfahren nach dem nebengeordneten Anspruch 7 aus den vorstehend genannten Gründen nicht erfinderisch.


Bertl               Kirschneck                  Groß                 Dr. Scholz


                                                                              Be
