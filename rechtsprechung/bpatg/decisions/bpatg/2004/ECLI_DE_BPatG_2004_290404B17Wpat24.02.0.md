---
ecli: "ECLI:DE:BPatG:2004:290404B17Wpat24.02.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 24/02"
decided: "2004-04-29"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=44&nr=19446&anz=2061&pos=669&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-04-29_17_W-pat_24_02_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 24/02 vom 2004-04-29

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 24/02                                       Verkündet am
 _______________                                        29. April 2004
    (Aktenzeichen)                                           …




                          BESCHLUSS

                        In der Beschwerdesache




                     betreffend das Patent 196 00 081


…




BPatG 154
6.70

                                        -2-



hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 29. April 2004 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Fritsch sowie der Richter Dr. Schmitt, Dipl.-Ing. Bertl und
Dipl.-Ing. Prasch


beschlossen:


          Auf die Beschwerde der Einsprechenden wird der Beschluss
          der Patentabteilung 53 des Deutschen Patent- und Markenamts vom 20. Dezember 2001 aufgehoben. Das Patent
          196 00 081 wird widerrufen.




                                    Gründe


                                         I


Gegen die Erteilung des vorliegenden Patents 196 00 081 mit der Bezeichnung


               "Sicherung der Datenintegrität bei Datenträgerkarten"


wurde ein Einspruch erhoben.


Die Patentabteilung 53 des Deutschen Patent- und Markenamts hat das Patent
nach Prüfung des Einspruchs mit Beschluss vom 20. Dezember 2001 beschränkt
aufrechterhalten mit der Begründung, dass der Gegenstand des erteilten Patentanspruchs 1 neu und erfinderisch sei und der um eine Rückbeziehung ergänzte
Patentanspruch 22 gegenüber der erteilten Fassung nicht erweitert sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Einsprechenden.

                                        -3-



Die Patentinhaberin verfolgt das Patent in der von der Patentabteilung beschränkten Fassung mit den Ansprüchen 1 bis 22 weiter, hilfsweise mit Patentansprüchen
1 bis 20 nach Hilfsantrag 1 und nach Hilfsantrag 2.


Der Patentanspruch 1 gemäß dem Hauptantrag lautet:


          „Verfahren zur Sicherung der Integrität von Daten bei einer
          Kommunikation unter Beteiligung einer Datenträgerkarte,
          bei dem eine Sequenz von Schreibvorgängen, für die die Integrität der zu schreibenden Daten sichergestellt werden soll,
          auf der Chipkarte als eine Integritätseinheit definiert wird,
          dadurch gekennzeichnet, dass
          von einem Datenbestand, der mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen verändert
          werden soll, eine Kopie des Datenbestandes in einem Schattenspeicher erzeugt wird, und dass
          die Veränderungen mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen nur an dem Datenbestand oder nur an der Kopie des Datenbestandes ausgeführt
          werden, wobei die zur Integritätseinheit gehörende Sequenz
          von Schreibvorgängen zumindest unteilbar und konsistenzerhaltend ist.“


Der Patentanspruch 1 gemäß dem Hilfsantrag 1 lautet:


          „Verfahren zur Sicherung der Integrität von Daten bei einer
          Kommunikation unter Beteiligung einer Datenträgerkarte,
          bei dem eine Sequenz von Schreibvorgängen, für die die Integrität der zu schreibenden Daten sichergestellt werden soll,
          auf der Chipkarte als eine Integritätseinheit definiert wird,
          dadurch gekennzeichnet, dass

                                        -4-



          von einem Datenbestand, der mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen verändert
          werden soll, eine Kopie des Datenbestandes in einem Schattenspeicher erzeugt wird, und dass
          die Veränderungen mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen nur an dem Datenbestand oder nur an der Kopie des Datenbestandes ausgeführt
          werden, wobei die zur Integritätseinheit gehörende Sequenz
          von Schreibvorgängen als Transaktion unter Verwendung
          des „Two phase commit“-Verfahrens ausgeführt wird.“


Der Patentanspruch 1 gemäß dem Hilfsantrag 2 lautet:


          „Verfahren zur Sicherung der Integrität von Daten bei einer
          Kommunikation unter Beteiligung einer Datenträgerkarte,
          bei dem eine Sequenz von Schreibvorgängen, für die die Integrität der zu schreibenden Daten sichergestellt werden soll,
          auf der Chipkarte als eine Integritätseinheit definiert wird,
          dadurch gekennzeichnet, dass
          von einem Datenbestand, der mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen verändert
          werden soll, eine Kopie des Datenbestandes in einem Schattenspeicher erzeugt wird, und dass
          die Veränderungen mittels der zur Integritätseinheit gehörenden Sequenz von Schreibvorgängen nur an dem Datenbestand oder nur an der Kopie des Datenbestandes ausgeführt
          werden, wobei die zur Integritätseinheit gehörende Sequenz
          von Schreibvorgängen als Transaktion unter Verwendung
          des „Two phase commit“-Verfahrens ausgeführt wird und zusätzlich ein globaler Merker zur Bestimmung der Aktivität einer Transaktion verwendet wird.“

                                       -5-



Die Einsprechende trägt zur Begründung ihrer Beschwerde vor, dass das beanspruchte Verfahren zur Sicherung der Integrität nach dem Anspruch 1 gemäß
Hauptantrag schon den Mangel aufweise, dass nicht klar erkennbar sei, wie die
zur Integritätseinheit gehörende Sequenz von Schreibvorgängen gestaltet werden
müsse, um unteilbar und konsistenzerhaltend zu sein, wie im letzten Merkmal des
Anspruchs angegeben.
Im übrigen sei das beanspruchte Verfahren auch in den Fassungen gemäß dem
ersten oder zweiten Hilfsantrag durch den Stand der Technik nahegelegt.


Die Einsprechende stellt den Antrag,


          den Beschluss der Patentabteilung aufzuheben und das Patent in vollem Umfang zu widerrufen.


Die Patentinhaberin beantragt,


          die Beschwerde zurückzuweisen,
          hilfsweise den angefochtenen Beschluss dahin abzuändern,
          dass das Patent in weiter eingeschränktem Umfang aufrechterhalten wird mit Patentansprüchen 1 bis 20 nach Hilfsantrag 1 und nach Hilfsantrag 2, beide Fassungen überreicht in
          der mündlichen Verhandlung am 29. April 2004.


Die Patentinhaberin erläutert, dass Datenträgerkarten wie bspw Chipkarten zunehmend zur Durchführung komplexerer Aufgaben verwendet würden. Während beim
Einsatz solcher Karten bisher lediglich sichergestellt werden musste, dass einzelne Schreibvorgänge zuverlässig ausgeführt würden, sei diesem Trend folgend zu
gewährleisten, dass eine Mehrzahl von miteinander zusammenhängenden
Schreibvorgängen sicher ausgeführt würde.

                                          -6-



Dieses Problem werde in den entgegengehaltenen Druckschriften nicht angesprochen, daher könnten diese Druckschriften die mit dem Patentanspruch 1 vorgeschlagene Lösung auch nicht nahe legen.
In der Fassung nach den Hilfsanträgen 1 und 2 werde die mit dem Anspruch 1
vorgeschlagene Lösung durch die Verwendung des "two phase commit" Verfahrens und eines globalen Merkers präzisiert.




                                           II


Die in rechter Frist und Form erhobene Beschwerde ist zulässig.
Sie musste auch zum Erfolg führen, da das mit dem Patent beanspruchte Verfahren in den von der Patentinhaberin verteidigten Fassungen nicht auf erfinderischer
Tätigkeit beruht (§ 4 PatG).


Zum Hauptantrag:
In der Beschreibungseinleitung ist ausgeführt, dass Datenträgerkarten (Smart
Cards) in einer Reihe unterschiedlicher Funktionen Anwendung finden, bspw als
Zahlungsmittel. Aus diesen Gründen müssten an die Integrität der Daten auf der
Datenträgerkarte höchste Ansprüche gestellt werden. Unter Integrität von Daten
sei dabei die Fehlerfreiheit der Daten in dem Sinne zu verstehen, dass sie ein richtiges Abbild der Realität beinhalten. Es wird beispielhaft erläutert, dass eine Chipkarte als elektronische Börse und gleichzeitig als Ausweis zur Berechtigung zum
Besuch eines Fitnessstudios dienen könne, wobei die Berechtigung jeden Monat
durch Ausbuchen der Gebühr aus der Börse verlängert werde. Werde die Chipkarte nach dem Abbuchen des Betrags aus der Börse und vor der Bestätigung der
Abbuchung und der Verlängerung der Berechtigung entnommen, so trete ein inkonsistenter Zustand auf, da der Betrag zwar abgebucht, aber die Berechtigung
nicht verlängert sei (vgl S2, Z 4 - 13 u 30 - 41 der Patentschrift).

                                         -7-



Daher stelle sich die Aufgabe, ein Verfahren und ein System bereit zu stellen, das
die Integrität der Daten beim Schreiben auf die Chipkarte und die Darstellung auf
der Chipkarte erhält (vgl S 2, Z 62 - 63 der Patentschrift).


Der Anspruch 1 gemäß dem Hauptantrag schlägt zunächst vor, die Daten, deren
Integrität sichergestellt werden soll und die in einer Sequenz von Schreibvorgängen auf der Chipkarte verändert werden sollen, als eine Integritätseinheit zu definieren. Um bei Veränderungen an dem Datenbestand einer Integritätseinheit die
Integrität des Datenbestands zu sichern, wird vor der Durchführung von Schreibvorgängen eine Kopie des Datenbestands in einem Schattenspeicher erzeugt.
Dem letzten Merkmal des Anspruchs 1 gemäß sollen sodann Veränderungen der
Daten durch die Sequenz von Schreibvorgängen entweder nur an dem (in einem
nichtflüchtigen Speicher der Chipkarte gespeicherten) Datenbestand oder nur an
der Kopie im Schattenspeicher ausgeführt werden, wobei die Sequenz der
Schreibvorgänge unteilbar und konsistenzerhaltend sein soll.


Es ist der Einsprechenden hinsichtlich des von ihr vorgebrachten Arguments beizutreten, dass der Anspruch 1 nicht ohne weiteres erkennen lässt, wie bei einem
unbeabsichtigten Abbruch der Sequenz von Schreibvorgängen die Konsistenz
bzw Integrität des Datenbestandes sichergestellt werden soll.
Aus dem Umstand, dass der Anspruch das Anlegen einer Sicherungskopie in einem Schattenspeicher vorschlägt, wird der auf dem Gebiet der kaufmännischen
Datenverarbeitung tätige Ingenieur oder Informatiker als zuständiger Fachmann
jedoch schließen, dass bei einer unbeabsichtigten Unterbrechung der Sequenz
von Schreibvorgängen, die nur teilweise geänderte, also inkonsistente Daten zur
Folge hat, auf den unverändert gebliebenen Datenbestand in einem der Speicher
zurückgegriffen wird, da dieser in seiner Integrität bzw Konsistenz unverändert geblieben ist.
Es kann sonach zu Gunsten der Patentinhaberin unterstellt werden, dass der Anspruch 1 eine nachvollziehbare Lehre vermittelt.

                                       -8-



Das Verfahren nach dem Anspruch 1 gemäß dem Hauptantrag beruht aber nicht
auf erfinderischer Tätigkeit.


Aus der US 4,922,456 ist ein Verfahren vorbekannt, das dazu dienen soll, Daten
fehlerfrei in einen nichtflüchtigen Speicher zu schreiben. Dabei kann, wie in Sp 4,
Z 50 - 56 ua erläutert, der Fall auftreten, dass eine Schreiboperation, die eine Sequenz von Schreibvorgängen (several write steps), dh das Schreiben mehrerer
Wörter umfasst, durch einen Spannungsausfall unterbrochen wird, so dass nur einige der Schreibvorgänge ausgeführt werden, was zu einer Verfälschung (corruption) des Datenbestandes führt. Zur Vermeidung solcher Verfälschungen schlägt
die Druckschrift die Verwendung eines Schattenspeichers (double buffer) vor, in
den ein Doppel der zu verändernden Daten geschrieben wird. Wird eine Verfälschung des eingeschriebenen Datenbestandes anhand eines "flag" erkannt, wird
auf das unveränderte und damit fehlerfreie Doppel der Daten zurückgegriffen (vgl
Sp 2, Z 5 - 20 u Anspruch 1).
Dieses bekannte Verfahren zur Sicherung der Integrität von Daten befasst sich sonach - entgegen der Auffassung der Patentinhaberin - mit der Konsistenzerhaltung
eines aus mehreren Worten bestehenden Datenbestandes, der durch eine Sequenz von miteinander zusammenhängenden Schreibvorgängen verändert wird.


Das Verfahren nach dem Patentanspruch 1 unterscheidet sich von dem bekannten Verfahren durch die Angabe einer zweiten Alternative, die darin besteht, dass
die Veränderungen durch die Schreibsequenz nicht an dem Doppel im Schattenspeicher vorgenommen werden, sondern am originalen Datenbestand. Bei dieser
Alternative gelingt die Wiederherstellung der unveränderten und fehlerfreien Daten
bei Auftreten einer Verfälschung durch Rückgriff auf den Datenbestand des unveränderten Doppels im Schattenspeicher.


Diese zweite Alternative war dem Fachmann jedoch bei Kenntnis der ersten in der
US 4,922,456 beschriebenen Alternative nahegelegt. Denn der Fachmann konnte
ohne weiteres erkennen, dass das bekannte Verfahren entscheidend darauf be-

                                       -9-



ruht, dass von dem zu verändernden Datenbestand vor Beginn der Schreibvorgänge ein Doppel angefertigt wird, auf das bei Auftreten einer fehlerhaften Unterbrechung der Sequenz von Schreibvorgängen zurückgegriffen werden kann. Ob
die Veränderungen durch die Sequenz von Schreibvorgängen dann am Original
oder am Doppel erfolgten, war für ihn absehbar gleichwertig, weil jedenfalls ein
Datenbestand unverändert blieb und damit die Konsistenz trotz Auftretens einer
Verfälschung sichergestellt werden konnte.
Eine erfinderische Besonderheit kann auch in dem Umstand, dass das beanspruchte Verfahren zur Änderungen von Datenbeständen in Speichern einer Datenträgerkarte dienen soll, nicht gesehen werden. Denn ersichtlich liegen hier keine Umstände vor, die von denen abweichen, die im Patentanspruch 1 der
US 4,922,456 für das Beschreiben von (nichtflüchtigen) Speichern in Einrichtungen jeglicher Art gelten.


Das Verfahren nach dem Patentanspruch 1 gemäß Hauptantrag beruht sonach
nicht auf erfinderischer Tätigkeit.


Zum Hilfsantrag 1:
Der Anspruch 1 in dieser Anspruchsfassung unterscheidet sich von Anspruch 1
gemäß dem Hauptantrag hinsichtlich des letzten Merkmals, nach dem die zur Integritätseinheit gehörende Sequenz von Schreibvorgängen als Transaktion unter
Verwendung des "Two phase commit"-Verfahrens ausgeführt werden soll.
Bedenken gegen die Zulässigkeit dieser Anspruchsfassung bestehen nicht. Dass
ein "Two phase commit"-Verfahren Anwendung finden soll, ist auf S 3, Z 41 - S 4,
Z 4 der Patentschrift bzw auf S 5 unten der ursprünglichen Unterlagen angegeben.
Diese Ergänzung erweitert den Gegenstand des erteilten Anspruchs 1 nicht, sondern kann als Präzisierung angesehen werden.


Die Ergänzung vermittelt dem Fachmann, dass für das beanspruchte Verfahren
zur Sicherung der Integrität von Daten die im Zusammenhang mit (Datenbank-)
Transaktionen herrschenden Grundsätze gelten sollen. Wie auf S 3, Z 44 - 50 er-

                                      - 10 -



läutert, sind Transaktionen durch vier Eigenschaften gekennzeichnet, von denen
durch das "Two phase commit"-Verfahren" zwei sichergestellt werden sollen, nämlich die Unteilbarkeit und die Konsistenzerhaltung der Datensätze. Durch das Verfahren soll garantiert werden, dass innerhalb einer Transaktion entweder alle Aktionen, dh Schreibvorgänge auf der Chipkarte ausgeführt werden oder keine (vgl
S 3, Z 57 - 58).
Genau dies aber leistet das aus der US 4,922,456 zur Anwendung bei jeglichen
Schreibvorgängen in nichtflüchtigen Speichern bekannte und nicht nur auf Datenbanktransaktionen beschränkte Verfahren, nach dem die Integrität eines Datenbestandes dadurch sicher gestellt wird, dass die Sequenz von Schreibvorgängen
entweder vollständig (unteilbar) ausgeführt wird, oder dass zu dem Zustand vor
Beginn der Schreibvorgänge zurückgekehrt wird, was einem Zustand der Konsistenz entspricht.
Der in dieser Anspruchsfassung ergänzte Bezug zu Transaktionen unter Benutzung des "Two phase commit"-Verfahrens stellt daher keine erfinderische Besonderheit dar.


Zum Hilfsantrag 2:
In dieser Fassung des Anspruchs 1 ist gegenüber dem vorhergehenden Hilfsantrag ergänzt, dass zusätzlich ein globaler Merker zur Bestimmung der Aktivität einer Transaktion verwendet wird.


Wie auf S 5, Z 33 - 43 der Patentschrift erläutert, erlaubt der globale Merker
"Transaktion in Bearbeitung" zu jedem Zeitpunkt die Klärung, welche Daten bei
Start einer neuen Transaktion gültig sind, dh er liefert eine Aussage darüber, ob
die Änderungen an dem Datenbestand durch die Sequenz von Schreibvorgängen
erfolgreich abgeschlossen wurde oder nicht.
Ein Merker, der eine solche Aussage liefert, ist in der US 4,922,456 als "flag" beschrieben. Wie dort in Sp 2, Z 17 - 19 ausgeführt, wird dieses "flag" nach dem erfolgreichem Abschluss der Schreibvorgänge in den Schattenspeicher (double buf-

                                        - 11 -



fer) gesetzt und zeigt sonach an, dass bei Start einer neuen Transaktion bzw Sequenz von Schreibvorgängen nunmehr diese Daten gültig sind.


Auch das Verfahren nach dem Patentanspruch 1 gemäß dem Hilfsantrag 2 beruht
sonach nicht auf erfinderischer Tätigkeit.


Das Patent konnte daher in keiner der von der Patentinhaberin beantragten Fassungen aufrechterhalten werden.
Der Beschluss der Patentabteilung 53 des Deutschen Patent- und Markenamts
war daher aufzuheben und das Patent zu widerrufen.




Dr. Fritsch               Dr. Schmitt            Bertl                   Prasch


                                                                             Ko
