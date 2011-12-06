---
ecli: "ECLI:DE:BPatG:2011:061211B17Wpat33.08.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 33/08"
decided: "2011-12-06"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=81&nr=22943&anz=1310&pos=1221&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-12-06_17_W-pat_33_08_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 17 W (pat) 33/08 vom 2011-12-06

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 33/08                                                    Verkündet am
_______________                                                   6. Dezember 2011
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 199 83 793.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 6. Dezember 2011 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch, der Richterin Eder und der Richter
Dipl.-Ing. Baumgardt und Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                     -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamts vom 22. März 2006 aufgehoben und das Patent mit folgenden Unterlagen erteilt:


       Patentansprüche 1–4 und Beschreibung Seiten 1–27, jeweils
       überreicht in der mündlichen Verhandlung,
       5 Blatt Zeichnungen mit 6 Figuren vom 6. Juni 2001, eingegangen
       am 7. Juni 2001.


       Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                  Gründe


                                      I.


Die vorliegende Patentanmeldung ist eine PCT-Anmeldung in nationaler Phase,
welche die Priorität einer Voranmeldung in den USA vom 8. Dezember 1998 in
Anspruch nimmt und als WO 00 / 34 870 A1 in englischer Sprache veröffentlicht
wurde. PCT-Anmeldetag ist der 22. September 1999. Die Bezeichnung lautet in
der geltenden Fassung:


„System mit einem Prozessor, auf dem mehrere, gleichzeitig aktive Ausführungsentitäten ausgeführt werden, und mit einem mehrere, den Ausführungsentitäten
      zugewiesene Cache-Abschnitte aufweisenden Cache-Speicher“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts mit der Begründung zurückgewiesen, dass

                                      -3-



der in den vorangehenden zwei Bescheiden genannte Mangel mit den zuletzt
geltenden Patentansprüchen nicht abgestellt worden sei: der weiterhin auf ein
„System“ gerichtete Patentanspruch 1 sei unklar, da offensichtlich kein komplettes
System, sondern eine Cache-Speicheranordnung unter Schutz gestellt werden
solle; anders gesagt bedeute dies, dass im Patentanspruch 1 nicht klar angegeben sei, was als patentfähig unter Schutz gestellt werden solle (§ 34 Absatz 3
Nr. 3 PatG). Die beantragte Anhörung werde nicht mehr für sachdienlich erachtet,
da nach zwei Bescheiden und dem Angebot einer Anhörung, das von der Anmelderin nicht wahrgenommen worden sei, ausreichend rechtliches Gehör eingeräumt
worden sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.




Die Anmelderin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 4 und Beschreibung Seiten 1 bis 27,
       jeweils überreicht in der mündlichen Verhandlung,
       5 Blatt Zeichnungen mit 6 Figuren vom 6. Juni 2001, eingegangen
       am 7. Juni 2001.


Dazu trägt sie vor, das in der mündlichen Verhandlung überreichte Patentbegehren weise keine formalen Mängel auf und sei durch den bekanntgewordenen
Stand der Technik nicht vorweggenommen und auch nicht nahegelegt.


Ferner regt sie die Rückzahlung der Beschwerdegebühr an und begründet dies
mit „groben Verfahrensfehlern“; zu diesen gehörten die Ablehnung der beantragten, sachdienlichen Anhörung und die Tatsache, dass die Zurückweisung der

                                         -4-



Anmeldung auf einen überraschenden und völlig abwegigen Grund gestützt
worden sei.


Die geltenden Patentansprüche, hier mit einer möglichen Gliederung des Hauptanspruchs versehen und in Merkmal (a) geringfügig redaktionell korrigiert (Komma-Verschiebung), lauten:


       „1.    System


       (a)    mit einem Prozessor (200), auf dem mehrere, gleichzeitig
              aktive Ausführungsentitäten, beispielsweise Prozesse, Tasks
              oder Threads, ausgeführt werden können,


       (b)    einem mit dem Prozessor gekoppelten Speicher (206)
       (c)    und einem mit dem Prozessor gekoppelten Cache-Speicher
              (100; 202),
       (c1) wobei der Cache-Speicher (100; 202) mehrere Cache-Abschnitte (102-106) und einen Cache-Controller (108) aufweist, wobei jeder Cache-Abschnitt mehrere Cache-Speicherplätze aufweist,


       (c2) wobei jeder Cache-Abschnitt (102-106) so ausgebildet ist,
              dass er Informationen speichert, die zu Anforderungen aus
              jeweils einer zugehörigen Ausführungsentität der mehreren
              Ausführungsentitäten gehören,


       dadurch gekennzeichnet,


       (d)    dass   jeder Ausführungsentität ein    Ausführungsentitätsidentifizierer (EID) zugeordnet ist,

                                         -5-



       (e)    dass in dem Speicher (206) mehrere Befehlsspeicherbereiche definiert sind, die jeweils zu einem Ausführungsentitätsidentifizierer (EID) gehören, so dass der Ausführungsentitätsidentifizierer (EID) anhand des Speicherbereichs, aus dem
              ein Befehl abgerufen wurde, bestimmt werden kann, und


       (f)    dass der Cache-Controller auf der Basis des Ausführungsentitätsidentifizierers (EID) beim Zugreifen auf den Cache-Speicher (100; 202) einen zugehörigen Cache-Abschnitt
              (102-106) auswählt.


       2. System nach Anspruch 1, dadurch gekennzeichnet, dass die
             Cache-Abschnitte so konfigurierbar sind, dass sie eine verschiedene Cache-Zeilen-Ersetzungsstrategie, Cache-Aktualisierungsstrategie und/oder Cache-Organisation haben.


       3. System nach Anspruch 1 oder 2, dadurch gekennzeichnet,
             dass der Cache-Speicher ein Mehr-Ebenen-Cache-Speicher
             ist, bei dem wenigstens eine Ebene einen Mehr-Einheiten-Cache-Speicher mit mehreren Cache-Abschnitten enthält.


       4. System nach Anspruch 1, dadurch gekennzeichnet, dass jeder
             Cache-Abschnitt auf der Basis der jeweiligen zeitlichen und
             räumlichen Lokalitätseigenschaften, mit denen die Ausführungsentitäten Daten verarbeiten, konfiguriert ist.“


Ihnen soll sinngemäß die Aufgabe zugrunde liegen, eine Speicherarchitektur anzugeben, welche die Speicherleistungsfähigkeit verbessern kann (siehe Beschreibung Seite 3 Absatz 3).

                                        -6-



Aus dem Stand der Technik wurde von der Prüfungsstelle entgegengehalten:


          D1   US 4 928 239


Der Senat hat in einem Ladungszusatz noch benannt:


          D2   EP 0 856 797 A1
          D3   GB 2 311 880 A


                                         II.


Der rechtzeitig eingelegten und auch sonst zulässigen Beschwerde war stattzugeben, da der von der Prüfungsstelle geltend gemachte Zurückweisungsgrund
nicht vorliegt. Zumindest das geltende Patentbegehren erfüllt alle Kriterien für eine
Patenterteilung, insbesondere ist es neu gegenüber dem bekannt gewordenen
Stand der Technik und beruht auf einer erfinderischen Tätigkeit (PatG §§ 1 bis 5,
§ 34).


1.       Die vorliegende Patentanmeldung betrifft Computersysteme, welche für die
Ausführung mehrerer gleichzeitig aktiver Prozesse, Tasks oder Threads ausgelegt
sind, und welche ferner einen Cache-Speicher aufweisen.


Dem Fachmann war bereits vor dem Prioritätstag der Anmeldung vertraut, dass
sich der Zugriff auf einen Hauptspeicher durch das Vorsehen eines Cache-Speichers erheblich beschleunigen lässt. Weil der Cache nur einen kleinen Teil des
Hauptspeichers vorrätig halten kann und für noch nicht im Cache vorhandene
Daten unverändert auf den langsameren Hauptspeicher zugegriffen werden muss,
wurden verschiedene Prinzipien und Strategien entwickelt, um die Trefferquote im
Cache zu optimieren. Der Abruf von Daten aus dem Speicher hängt aber auch wesentlich von der Art des durchzuführenden Programms ab, so dass unterschiedliche Programm-Arten möglicherweise unterschiedliche Cache-Strategien erfor-

                                       -7-



dern. So war es zum Beispiel bekannt, dass der Speicherzugriff auf Programmbefehle nach anderen Regeln erfolgt als auf die zu verarbeitenden Daten; zur Optimierung sieht der Stand der Technik hier daher separate Cache-Einheiten für Befehle und Daten vor (vgl. Anmeldung Seite 1 Absatz 3 bis Seite 2 Absatz 2).


Anmeldungsgemäß wurde erkannt, dass ein besonderes Problem auftritt, wenn
das Computersystem für eine Ausführung mehrerer gleichzeitig aktiver Prozesse,
Tasks oder Threads eingerichtet ist („nebenläufige Programmausführung“). Denn
wenn unterschiedliche Programmteile nebeneinander nahezu gleichzeitig ausgeführt werden, aber dabei denselben Cache benutzen, stört jeder Programmteil die
Cache-Speicherbenutzung der anderen Programmteile, insbesondere wenn unterschiedliche Cache-Strategien erforderlich wären (vgl. Anmeldung Seite 2 Absatz 3
bis Seite 3 Absatz 2).


Daher schlägt die Anmeldung mit dem geltenden Patentanspruch 1 vor, den
Cache-Speicher in mehrere Abschnitte aufzuteilen und diese jeweils zu einzelnen
Prozessen, Tasks oder Threads zuzuordnen. Weil so jeder Programmteil seinen
eigenen Cache-Speicherabschnitt besitzt, sind die gegenseitigen Störungen erheblich vermindert. Für die Zuordnung sieht der Patentanspruch 1 Identifizierer-Codes (EID) vor: den Programmausführungs-Entitäten, welche die einzelnen Prozessen, Tasks oder Threads ausführen, werden solche Identifizierer-Codes zugeordnet, und ferner werden im Hauptspeicher Bereiche für Befehle definiert, die
jeweils zu einem Identifizierer-Code gehören. So lässt sich anhand des Hauptspeicher-Bereichs, aus dem die Befehle abgerufen werden, ein jeweiliger Identifizierer-Code sehr einfach bestimmen, auf dessen Basis dann ein zugehöriger Cache-Abschnitt ausgewählt werden kann.


Der Begriff „(Programm-) Ausführungsentität“ (im englischen Original: „program
execution entity“) wird dabei vom Fachmann verstanden als Sammelbegriff für
Programmteile, die gleichzeitig aktiv sein können, wie Prozesse, Tasks oder
Threads (siehe ursprüngliche Beschreibung Seite 2 Zeile 33/34).

                                        -8-



Als Fachmann, der mit der Aufgabe betraut wird, eine Speicherarchitektur mit
verbesserter Leistungsfähigkeit zu schaffen, sieht der Senat einen Entwicklungsingenieur (Univ. oder FH) für Prozessor- und Speichersysteme mit mehrjähriger
Berufserfahrung an.


2.    Der Zurückweisungsbeschluss war aufzuheben, weil der von der Prüfungsstelle geltend gemachte Mangel nicht vorliegt.


2.1   Der Zurückweisungsbeschluss wird damit begründet, dass offensichtlich
kein komplettes System, sondern eine Cache-Speicheranordnung unter Schutz
gestellt werden solle; anders gesagt bedeute dies, dass im Patentanspruch 1 nicht
klar angegeben sei, was als patentfähig unter Schutz gestellt werden solle (§ 34
Absatz 3 Nr. 3 PatG).


2.2   Für den Fachmann besteht eine solche Unklarheit nach Überzeugung des
Senats jedoch nicht. Der geltende – wie auch der dem Zurückweisungsbeschluss
zugrundeliegende – Patentanspruch 1 ist auf ein „System“ gerichtet, das bestimmte zumindest in der Beschreibung näher erläuterte Bestandteile aufweist.
Damit wird klar definiert, was als patentfähig unter Schutz gestellt werden soll (vgl.
auch die Senatsentscheidung in BPatGE 48, 196 – Systemansprüche).


2.3   Was die Prüfungsstelle zum Ausdruck bringen will, wenn sie meint, „offensichtlich“ solle kein komplettes System, sondern (nur?) eine Cache-Speicheranordnung unter Schutz gestellt werden, ist nicht nachvollziehbar. Gerade im vorliegenden Fall entsteht das anspruchsgemäß gelöste Problem erst durch die Auslegung des Rechners für eine nebenläufige Programmausführung, d.h. durch mehrere gleichzeitig aktive Prozesse, Tasks oder Threads. Bereits die Zuordnung der
Cache-Abschnitte zu diesen rechtfertigt einen Sachanspruch, der über eine reine
Cache-Speicheranordnung hinausgeht.

                                        -9-



Unabhängig davon existiert jedoch auch keine gesetzliche Norm, wonach sich ein
Anmelder mit seinen Patentansprüchen auf die kleinstmögliche Einheit im Sinne
eines „Kerns der Erfindung” beschränken müsste (vgl. 17 W (pat) 27/08;
17 W (pat) 87/07; 17 W (pat) 49/07).


3.    Weil alle Bedingungen dafür erfüllt sind, konnte das Patent so wie nunmehr
beantragt erteilt werden.


3.1   Der Erteilungsantrag verlässt nicht den Rahmen der ursprünglichen Offenbarung, welche sich aus den englischsprachigen PCT-Anmeldeunterlagen gemäß
WO 00 / 34 870 A1 ergibt (vgl. Busse, PatG, 6. Auflage (2003), § 34 Rdnr. 241 –
Fußnote 508 mit Verweis auf EPA T 605/93).


Der neue Patentanspruch 1 ergibt sich aus den ursprünglichen Ansprüchen 1
und 6, Seite 2 Zeile 5/6 sowie Figur 1 und 2 und zugehöriger Beschreibung, wobei
die kennzeichnenden Merkmale (d), (e) und (f) insbesondere Seite 11 Zeile 3/4,
Zeilen 10–17 und Zeilen 26–32 entnehmbar sind. Die Unteransprüche 2, 3 und 4
basieren auf den ursprünglichen Ansprüchen 7–10, 11 und 12.


Die Beschreibung wurde in zulässiger Weise an das geltende Patentbegehren angepasst, wobei in Seite 17 Absatz 2 Satz 1 vom Senat noch eine redaktionelle
Korrektur vorgenommen wurde.


3.2   Die Patentansprüche geben auch klar und deutlich an, was durch sie unter
Schutz gestellt werden soll (vgl. oben 2.2).


3.3   Der ermittelte Stand der Technik steht nicht entgegen.


3.3.1 Der Gegenstand des Anspruchs 1 ist neu, da ein System mit allen beanspruchten Merkmalen am Prioritätstag nicht zum Stand der Technik gehörte.

                                      - 10 -



Als nahekommend wurden die o. g. Druckschriften D1, D2 und D3 ermittelt.


D1 (US 4 928 239) beschreibt verschiedene Strategien zur Ersetzung von Datenblöcken in einem Cache und liefert bereits die Erkenntnis, dass die optimale
Strategie nicht für alle Datenstrukturen gleich sein kann (siehe Spalte 3 Zeile 10–
34). Deshalb wird dort vorgeschlagen, Computerbefehle, die einen Cache-Speicherzugriff beinhalten, um ein Befehlsfeld (cache control specifier CCS 45) zu
erweitern, das eine von verschiedenen Cache-Ersetzungsstrategien kennzeichnet;
dadurch kann vom Computerprogramm aus die für den aktuellen Anwendungsfall
bestgeeignetste Strategie vorgegeben werden.


Eine nebenläufige Programmausführung verschiedener Prozesse, Tasks oder
Threads und die dadurch verursachten Auswirkungen auf einen Cache-Speicher
werden in D1 jedoch nicht erwähnt. Entsprechend gibt es auch keine Zuordnung
von Cache-Abschnitten zu solchen Ausführungsentitäten und keine diesen zugeordnete Identifizierer-Codes. Zwar werden verschiedene Cache-Speicherblöcke
(Set A – Set N, siehe Spalte 4 Zeile 40 ff.) unterschieden, die man als „Cache-Abschnitte“ verstehen könnte. Diese sind aber lediglich bestimmten Speicherblöcken
des Hauptspeichers temporär zugeordnet, wie es für Cache-Speicher typisch ist.
Dass außerdem die so zugeordneten Speicherblöcke des Hauptspeichers zu bestimmten Ausführungsentitäten gehören sollten, wobei ein Identifizierer-Code, der
die Zugehörigkeit festlegt, anhand des Hauptspeicherbereichs bestimmt werden
könnte (wie es insbesondere Gegenstand von Merkmal (e) ist), lässt sich D1
weder direkt noch in Form einer Anregung entnehmen.


Die Lehre der D2 (EP 0 856 797 A1) nimmt zwar die Merkmale des Oberbegriffs
des Patentanspruchs 1 vorweg (siehe insbesondere Zusammenfassung – processor capable of executing a plurality of processes: Merkmal (a); Hauptspeicher 6
(Figur 1): Merkmal (b); cache memory divided into cache partitions, each … having a plurality of addressable storage locations / cache controller 20 (Figur 1):
Merkmale (c), (c1); partition indicator is allocated to each process identifying

                                      - 11 -



which … cache partition is to be used for holding items for use in the execution of
that process: Merkmal (c2)). Auch ist jedem Prozess ein „partition indicator“
zugeordnet, der festlegt, welche Cache-Abschnitte bei Datenanforderungen des
Prozesses mit Daten aus dem Hauptspeicher neu beschrieben werden dürfen
(ähnlich den Merkmalen (d) und (f) siehe z. B. Seite 6 Zeilen 48-50; Seite 7
Zeile 58 - Seite 8 Zeile 1). Jedoch ist D2 keine Lehre in Richtung auf eine
Aufteilung des Hauptspeichers in mehrere Befehlsspeicherbereiche entnehmbar,
die auch noch in irgendeiner Weise mit „partition indicators“ verknüpft wären
(Merkmal (e) fehlt).


D3 (GB 2 311 880 A) lehrt ebenfalls eine Aufteilung des Cache in mehrere Abschnitte, wobei die Abschnitte bestimmten „Anforderungsgebern“ (request sources) zugeordnet werden (siehe z. B. Seite 2 unten / Seite 3 oben); diese können
gemäß Figur 9 und Seite 9 Zeile 9–18 verschiedene Tasks eines Multitasking-Betriebssystems sein (Merkmale (a), (c), (c1) und (c2)). Dass ein Hauptspeicher
vorhanden ist (Merkmal (b)), liest der Fachmann als selbstverständlich mit. Ein
„Identifizierer“ im Sinne der Merkmale (d), (e) und (f) wird jedoch nirgendwo erwähnt, wie auch von einer Aufteilung und Zuordnung von Hauptspeicherbereichen
keine Rede ist.


Weiterer heranziehbarer Stand der Technik insbesondere aus der PCT-Recherche
oder aus einem parallelen Prüfungsverfahren vor dem US-Patentamt liegt ersichtlich weiter ab und war nicht Gegenstand des hiesigen Verfahrens.


3.3.2 Das System nach dem geltenden Patentanspruch 1 beruht auch auf einer
erfinderischen Tätigkeit.


Als nächstkommenden Stand der Technik sieht der Senat die Druckschrift D2 an,
welche über die Merkmale des Oberbegriffs des Patentanspruchs 1 hinaus bereits
die Idee enthält, für das Nachfüllen von Daten aus dem Hauptspeicher eine Zuordnung zwischen Prozessen und Cache-Abschnitten mithilfe eines Identifizierungs-

                                      - 12 -



codes vorzunehmen (8 bit group number zur Erzeugung des partition indicators,
siehe Seite 6 Zeile 23/24).


Weder der D2 noch den übrigen herangezogenen Dokumenten lässt sich aber
irgendeine Anregung entnehmen, im Sinne von Merkmal (e) des Anspruchs 1
einen solchen Identifizierungscode anhand desjenigen von mehreren Bereichen
des Hauptspeichers, aus dem der Befehl abgerufen wurde, auf einfache Weise zu
bestimmen.


Eine solche Maßnahme übersteigt auch das übliche fachmännische Handeln. Sie
genügt, um im gegebenen Zusammenhang das Vorliegen einer erfinderischen Tätigkeit zu begründen.


3.3.3 Die Unteransprüche 2, 3 und 4 betreffen nicht selbstverständliche Weiterbildungen und sind in Verbindung mit Anspruch 1 ebenfalls gewährbar.




                                       III.


Die Rückzahlung der Beschwerdegebühr entspricht der Billigkeit.


Wie der Senat wiederholt entschieden hat, stellt bereits die Ablehnung der beantragten Anhörung ohne tragfähige Begründung einen Verfahrensfehler dar.


Eine tragfähige Begründung kann sicherlich nicht darin gesehen werden, dass die
Anmelderin ein „Angebot zur Durchführung einer Anhörung … nicht wahrgenommen“ hätte. Das Angebot der Prüfungsstelle erfolgte im Bescheid vom 21. Januar 2005 in Form einer Aufforderung, sich bei fortbestehendem Interesse telefonisch mit der Prüfungsstelle zur Terminvereinbarung in Verbindung zu setzen.
Die Anmelderin hat statt dessen auf den Bescheid ausführlich schriftlich erwidert

                                    - 13 -



und erneut hilfsweise eine Anhörung beantragt. Dass darin ein Verzicht auf die
angebotene Anhörung liegen könnte, erscheint abwegig.


Auch dass „nach zwei Bescheiden … ausreichend rechtliches Gehör eingeräumt“
worden sei, kann angesichts der wiederholten Bemühungen der Anmelderin, den
Einwänden der Prüfungsstelle jeweils durch Änderungen in den Patentansprüchen
Rechnung zu tragen, und ihrer ausführlichen Argumentation dazu nicht hingenommen werden.




Dr. Fritsch             Eder                 Baumgardt             Dr. Forkel




                                                                           Me
