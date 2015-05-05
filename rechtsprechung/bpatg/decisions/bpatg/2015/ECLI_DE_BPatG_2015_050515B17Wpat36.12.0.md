---
ecli: "ECLI:DE:BPatG:2015:050515B17Wpat36.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 36/12"
decided: "2015-05-05"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=19&nr=27233&anz=851&pos=297&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-05-05_17_W-pat_36_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 36/12 vom 2015-05-05

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 36/12                                                  Verkündet am
_______________                                                     5. Mai 2015
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2010 007 967.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 5. Mai 2015 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,   der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Ing. Hoffmann




BPatG 154
05.11

                                         -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                          I.


Die vorliegende Patentanmeldung wurde am 15. Februar 2010 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt nunmehr die Bezeichnung


        „Verfahren, Computerprogramm-Produkt sowie computerlesbares
                   Speichermedium zur generischen Erstellung
            eines Strukturbaums zur Beschreibung eines IT-Verfahrens“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06Q des Deutschen
Patent- und Markenamtes mit Beschluss vom 12. Januar 2012 zurückgewiesen.
Zur Begründung führt die Prüfungsstelle aus, dass die Hauptansprüche gemäß
Haupt- und Hilfsantrag nicht gewährbar seien, da ihre Lehren gemäß § 1 Abs. 3
und 4 PatG dem Patentschutz nicht zugänglich seien.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Sie stellte den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        -   gemäß Hauptantrag mit
            Patentansprüchen 1 bis 16,

                                        -3-



             Beschreibung Seiten 1-54 und
             Zeichnungen mit Figuren 1-7, 10-15, 17-18, 21-23, 28,
             jeweils vom Anmeldetag,
             Figuren 8, 9, 16, 19, 20, 24-27, 29, 30 vom 07.05.2010;


       -     gemäß Hilfsantrag 1 mit
             Patentansprüchen 1 bis 14 vom 23.02.2012;


       -     gemäß Hilfsantrag 2 mit
             Patentansprüchen 1 bis 14 vom 23.02.2012;


       -     gemäß Hilfsantrag 3 mit
             Patentansprüchen 1 bis 13 vom 29.04.2015;


       -     gemäß Hilfsantrag 4 mit
             Patentansprüchen 1 bis 11 vom 29.04.2015,


       wobei für die Hilfsanträge 1 – 4 jeweils Beschreibung und
       Zeichnungen wie Hauptantrag gelten sollen.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


       (A)      Verfahren zur generischen Erstellung eines Strukturbaums zur
                Beschreibung der Topologie eines IT-Verfahrens
       (B)      mit kompletter Umgebung aus Clients, Servern, Middlewarekomponenten, Applikationen und Netzwerkkomponenten,
       (B1)     die ein Endanwender zur Durchführung eines spezifischen IT-
                gestützten Geschäftsprozesses benötigt,
       dadurch gekennzeichnet, dass

                                            -4-



        (D)     zur Beschreibung der Topologie der IT-Verfahrenselemente eine
                Metastruktur verwendet wird, die definiert,
                (d1)   welche IT-Verfahrenselementtypen zulässig sind,
                (d2)   welche Attribute zu den IT-Verfahrenselementtypen zugelassen und/oder erforderlich sind,
                (d3)   welche Relationen zwischen den IT-Verfahrenselementtypen
                       möglich sind, und
                (d4)   welche Attribute zu den Relationen zugelassen und/oder
                       erforderlich sind,
        wobei
        (E)     durch den Formalismus der Metastruktur nur eindeutige und schleifenfreie topologische Beziehungen zwischen den IT-Verfahrenselementen erlaubt werden,
        (F)     indem als Metastruktur ein azyklisch gerichteter Graph verwendet
                wird, der
                (f1)   bei einem Wurzelelement startet und
                (f2)   sich alle Kindelemente unter ihre jeweiligen Elternelemente
                       ordnen, wobei
                (f3)   die Kindelemente wiederum nur für solche Elemente Elternelemente sein dürfen, die nicht ihrerseits zu den Elternelementen dieser Kindelemente zählen.


Der geltende Patentanspruch 1 gemäß Hilfsantrag 1, hier mit einer möglichen
Gliederung versehen, lautet (Unterschiede zum Patentanspruch 1 gemäß Hauptantrag sind unterstrichen):


        (A1)    Verfahren zur Gesamtbehandlung eines IT-Verfahrens
        (B)     mit kompletter Umgebung aus Clients, Servern, Middlewarekomponenten, Applikationen und Netzwerkkomponenten,
        (C1)    wobei eine Topologie des IT-Verfahrens mittels eines Strukturbaumes bereitgestellt wird,

                                      -5-



(C2)    wobei der Strukturbaum vorgesehen ist zum Ermitteln von Installationsaufgaben und zur automatischen Durchführung der Installation
        von IT-Komponenten,
wobei
(D1)    zur Beschreibung der Topologie des IT-Verfahrens in dem Strukturbaum eine Metastruktur verwendet wird, die definiert,
        (d1)    welche IT-Verfahrenselementtypen zulässig sind,
        (d2)    welche Attribute zu den IT-Verfahrenselementtypen zugelassen und/oder erforderlich sind,
        (d3)    welche Relationen zwischen den IT-Verfahrenselementtypen
                möglich sind, und
        (d4)    welche Attribute zu den Relationen zugelassen und/oder
                erforderlich, sind,
wobei
(E)     durch den Formalismus der Metastruktur nur eindeutige und schleifenfreie topologische Beziehungen zwischen den IT-Verfahrenselementen erlaubt werden,
(F)     indem als Metastruktur ein azyklisch gerichteter Graph verwendet
        wird, der
        (f1)    bei einem Wurzelelement startet und
        (f2)    sich alle Kindelemente unter ihre jeweiligen Elternelemente
                ordnen, wobei
        (f3)    die Kindelemente wiederum nur für solche Elemente Elternelemente sein dürfen, die nicht ihrerseits zu den Elternelementen dieser Kindelemente zählen,
        wobei
        (f4)    der Strukturbaum einem Installationsautomaten übergeben
                wird, welcher aus dem Baum für jedes Element die vollständigen Installationsparameter und die Installationsaufgaben
                ermittelt und die Installationsreihenfolge der Elemente festlegt,

                                        -6-



              (f5)   wobei die Installationsaufgaben durch Installationsskripte
                     durchgeführt werden, denen jeweils ein geeignetes Installationsparameter-Set übergeben wird.


Der geltende Patentanspruch 1 gemäß Hilfsantrag 2, hier mit einer möglichen
Gliederung versehen, lautet (Unterschiede zu den Patentansprüchen 1 der vorhergehenden Anträge sind unterstrichen):


       (A2)   Computer-implementiertes Verfahren zur automatisierten Installation eines IT-Verfahrens,
       (C1*) wobei eine Topologie des IT-Verfahrens durch einen Strukturbaum
              beschrieben wird,
       (C3)   welcher mit einem Wurzelelement startet und in dem alle Elemente
              des IT-Verfahrens hierarchisch in einer Eltern-Kind-Beziehung unter
              dem Wurzelelement angeordnet sind,
       (C4)   wobei der Strukturbaum zur automatisierten IT-Verfahrensinstallation benutzt wird,
       (C5)   wobei der Strukturbaum einem Installationsautomaten übergeben
              wird, welcher aus dem Baum für jedes Element die vollständigen
              Installationsparameter ermittelt und die Installationsreihenfolge der
              Elemente festlegt, und die Installationsaufgaben ermittelt,
       (C6)   wobei die Installationsaufgaben durch Installationsskripte ausgeführt werden, und
       (C7)   wobei den Installationsskripten ein jeweils geeignetes Parameter-Set übergeben wird.


Der geltende Patentanspruch 1 gemäß Hilfsantrag 3, hier mit einer möglichen
Gliederung versehen, lautet (Unterschiede zu den Patentansprüchen 1 der vorhergehenden Anträge sind unterstrichen):

                                    -7-



(A2)    Computer-implementiertes Verfahren zur automatisierten Installation eines IT-Verfahrens,
(B*)    bestehend aus Clients, Servern, Middlewarekomponenten, Applikationen und Netzwerkkomponenten,
(C1*) wobei eine Topologie des IT-Verfahrens durch einen Strukturbaum
        beschrieben wird,
(C3)    welcher mit einem Wurzelelement startet und in dem alle Elemente
        des IT-Verfahrens hierarchisch in einer Eltern-Kind-Beziehung unter
        dem Wurzelelement angeordnet sind,
(C4*) wobei der Strukturbaum zur automatisierten Installation des IT-Verfahrens benutzt wird,
wobei
(D*)    zur Beschreibung der Topologie der IT-Verfahrenselemente in dem
        Strukturbaum eine Metastruktur verwendet wird, die definiert,
        (d1)   welche IT-Verfahrenselementtypen zulässig sind,
        (d2)   welche Attribute zu den IT-Verfahrenselementtypen zugelassen und/oder erforderlich sind,
        (d3)   welche Relationen zwischen den IT-Verfahrenselementtypen
               möglich sind, und
        (d4)   welche Attribute zu den Relationen zugelassen und/oder
               erforderlich sind,
        (d5)   wobei die Elementtypen Server, Middleware und Applikationen umfassen,
wobei
(E)     durch den Formalismus der Metastruktur nur eindeutige und schleifenfreie topologische Beziehungen zwischen den IT-Verfahrenselementen erlaubt werden,
(F)     indem als Metastruktur ein azyklisch gerichteter Graph verwendet
        wird, der

                                         -8-



               (f1)     bei einem Wurzelelement startet und
               (f2)     sich alle Kindelemente unter ihre jeweiligen Elternelemente
                        ordnen, wobei
               (f3)     die Kindelemente wiederum nur für solche Elemente Elternelemente sein dürfen, die nicht ihrerseits zu den Elternelementen dieser Kindelemente zählen,
       wobei die Installation umfasst,
       (C5*) der Strukturbaum wird einem Installationsautomaten übergeben,
               welcher aus dem Baum für jedes Element die vollständigen Installationsparameter und die Installationsaufgaben ermittelt und die
               Installationsreihenfolge der Elemente festlegt,
       (C6*) die Installationsaufgaben werden durch Installationsskripte ausgeführt,
       (C7*) wobei den Installationsskripten ein jeweils geeignetes Installationsparameter-Set übergeben wird,
       (C8)    das Installationsparameter-Set wird für die jeweiligen Installationsskripte aus dem Baum heraus ermittelt,
       (C9)    der Installationsautomat findet für jedes Element die Installationsparameter in den Attributen der IT-Verfahrenselemente,
       wobei
       (C10) zuerst die Server installiert werden, dann auf diesen Servern die
               Middleware installiert wird, und dann auf der Middleware die Applikationen installiert werden.


Der geltende Patentanspruch 1 gemäß Hilfsantrag 4, hier mit einer möglichen
Gliederung versehen, lautet (Unterschiede zu den Patentansprüchen 1 der vorhergehenden Anträge sind unterstrichen):


       (A2)    Computer-implementiertes Verfahren zur automatisierten Installation eines IT-Verfahrens,

                                    -9-



(B*)    bestehend aus Clients, Servern, Middlewarekomponenten, Applikationen und Netzwerkkomponenten,
(C1*) wobei eine Topologie des IT-Verfahrens durch einen Strukturbaum
        beschrieben wird,
(C3)    welcher mit einem Wurzelelement startet und in dem alle Elemente
        des IT-Verfahrens hierarchisch in einer Eltern-Kind-Beziehung unter
        dem Wurzelelement angeordnet sind,
(C4*) wobei der Strukturbaum zur automatisierten Installation des IT-Verfahrens benutzt wird,
wobei
(D*)    zur Beschreibung der Topologie der IT-Verfahrenselemente in dem
        Strukturbaum eine Metastruktur verwendet wird, die definiert,
        (d1)   welche IT-Verfahrenselementtypen zulässig sind,
        (d2)   welche Attribute zu den IT-Verfahrenselementtypen zugelassen und/oder erforderlich sind,
        (d3)   welche Relationen zwischen den IT-Verfahrenselementtypen
               möglich sind, und
        (d4)   welche Attribute zu den Relationen zugelassen und/oder
               erforderlich sind,
        (d5)   wobei die Elementtypen Server, Middleware und Applikationen umfassen,
wobei
(E)     durch den Formalismus der Metastruktur nur eindeutige und schleifenfreie topologische Beziehungen zwischen den IT-Verfahrenselementen erlaubt werden,
(F)     indem als Metastruktur ein azyklisch gerichteter Graph verwendet
        wird, der
        (f1)   bei einem Wurzelelement startet und
        (f2)   sich alle Kindelemente unter ihre jeweiligen Elternelemente
               ordnen, wobei

                                   - 10 -



        (f3)     die Kindelemente wiederum nur für solche Elemente Elternelemente sein dürfen, die nicht ihrerseits zu den Elternelementen dieser Kindelemente zählen,
wobei die Installation umfasst,
(C5*) der Strukturbaum wird einem Installationsautomaten übergeben,
        welcher aus dem Baum für jedes Element die vollständigen Installationsparameter und die Installationsaufgaben ermittelt und die
        Installationsreihenfolge der Elemente festlegt,
(C5**) wobei vor der Übergabe des Strukturbaumes an den Installationsautomaten alle Informationen des Strukturbaumes exportiert werden und dem Installationsautomaten übergeben werden,
(C6*) die Installationsaufgaben werden durch Installationsskripte ausgeführt,
(C7*) wobei den Installationsskripten ein jeweils geeignetes Installationsparameter-Set übergeben wird,
(C8)    das Installationsparameter-Set wird für die jeweiligen Installationsskripte aus dem Baum heraus ermittelt,
(C9)    der Installationsautomat findet für jedes Element die Installationsparameter in den Attributen der IT-Verfahrenselemente,
wobei
(C10) zuerst die Server installiert werden, dann auf diesen Servern die
        Middleware installiert wird, und dann auf der Middleware die Applikationen installiert werden,
(G)     wobei zur Installation eines Upgrades des IT-Verfahrens
        (g1)     der Strukturbaum eines vorhandenen Releases in ein Dateiformat exportiert wird, das die Darstellung hierarchisch strukturierter Daten unterstützt,
        (g2)     der Strukturbaum eines geplanten Releases erstellt und
                 ebenfalls in ein Dateiformat exportiert wird, das die Darstellung hierarchisch strukturierter Daten unterstützt,

                                         - 11 -



                (g3)   die in (g1) und (g2) erstellten Dateien von einer Datenverarbeitungsanlage verglichen werden und die Ergebnisse des
                       Vergleichs in strukturierter Form ausgegeben werden, wobei
                       erkennbar wird,
                       - ob ein Element beim Upgrade mit all seinen Attributen verändert wird,
                       - welche Elemente beim Upgrade gelöscht werden,
                       - welche Relationen beim Upgrade gelöscht werden,
                       - welche Elemente beim Upgrade ergänzt wurden,
                       - welche Relationen beim Update hinzugefügt wurden,
                (g4)   nur die Änderungen installiert werden.


Der Senat hat mit Ladungszusatz folgende Druckschriften in das Verfahren eingeführt:


D1:      US 2007/0220509 A1,
D2:      DE 693 34 172 T2.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie hat jedoch keinen Erfolg, da die Verfahren des jeweiligen Patentanspruchs 1 nach Hauptantrag und nach den Hilfsanträgen 1 bis 4 gemäß § 1 Abs. 3
Nr. 3 i. V. m. Abs. 4 PatG vom Patentschutz ausgeschlossen sind.


1.       Die vorliegende Patentanmeldung betrifft ein Verfahren, ein Computerprogramm-Produkt sowie ein computerlesbares Speichermedium zur generischen
Erstellung eines Strukturbaums zur Beschreibung eines IT-Verfahrens.

                                       - 12 -



Aus dem Stand der Technik (Offenlegungsschrift Absätze [0010]-[0018]) seien
bereits Verfahren bekannt, die eine Modellierung von IT-Systemen ermöglichen.
Dazu würden die Daten der Systemelemente und deren Parameter innerhalb
eines logischen Modells organisiert und in einer Datenbank gespeichert. Ein Nachteil dieser Verfahren bestünde darin, dass sie für eine Verwendung in einem
Managementsystem, bspw. für einen Installationsvorgang, ungeeignet seien, da
sich die Beschreibungsstrukturen der Elemente unterschieden und somit nicht alle
notwendigen Details aufwiesen. Ein weiterer Nachteil sei in der aufwändigen und
fehleranfälligen Pflege der Daten zu sehen.


Der Anmeldung soll die Aufgabe zugrunde liegen, ein Verfahren zur generischen
Erstellung eines Strukturbaums zur Beschreibung der Topologie eines IT-Verfahrens bereitzustellen, mit dem es möglich ist, alle zur Gesamtbehandlung eines IT-Verfahrens erforderlichen Informationen in einer definierten Struktur zu sammeln
und zu verwalten, so dass alle für das Management eines IT-Verfahrens relevanten Vorgänge aus einer Daten-Quelle schöpfen und automatisiert werden können
(Offenlegungsschrift Absatz [0019]).
Weiterhin soll der Anmeldung die Aufgabe zugrunde liegen, alle technischen
Parameter des zu installierenden IT-Verfahrens (d. h. die technischen Parameter
der einzelnen IT-Komponenten sowie die technischen Parameter, welche das
Zusammenwirken der IT-Komponenten untereinander festlegen bzw. erst ermöglichen) so bereitzustellen, dass diese eine automatisierte Installation aller IT-Komponenten des IT-Verfahrens bzw. ein automatisiertes Upgrade des IT-Verfahrens
ermöglichen, und ein Verfahren bereitzustellen mit dem eine automatisierte Installation (Upgrade) bewerkstelligbar ist (Eingabe vom 29.04.2015, S. 3).


Zur Lösung dieser Aufgabe schlägt der Patentanspruch 1 nach Hauptantrag ein
Verfahren zur generischen Erstellung eines Strukturbaums vor, welches eine
Beschreibung der Topologie eines IT-Verfahrens ermöglicht (Merkmal (A)). Dabei
beinhaltet das IT-Verfahren die komplette Umgebung aus Clients, Servern,
Middlewarekomponenten, Applikationen und Netzwerkkomponenten, die ein End-

                                      - 13 -



anwender zur Durchführung eines spezifischen IT-gestützten Geschäftsprozesses
benötigt (Merkmale (B), (B1)). Für die Beschreibung der Topologie, d. h. für den
Strukturbaum, wird eine Metastruktur verwendet, in der die zulässigen IT-Verfahrenselementtypen und deren Attribute sowie die Relationen zwischen den IT-Verfahrenselementtypen und die Attribute der Relationen definiert werden (Merkmale (D), (d1)-(d4)). Zusätzlich gibt die Metastruktur vor, dass nur eindeutige und
schleifenfreie topologische Beziehungen zwischen den IT-Verfahrenselementen
erlaubt werden (Merkmal (E)). Die Metastruktur ist als azyklisch gerichteter Graph
ausgebildet, der bei einem Wurzelelement startet, bei dem sich alle Kindelemente
unter ihre jeweiligen Elternelemente ordnen und die Kindelemente wiederum nur
für solche Elemente Elternelemente sein dürfen, die nicht ihrerseits zu den Elternelementen dieser Kindelemente zählen, was eine Schleifenfreiheit garantieren soll
(Merkmale (F), (f1)-(f3)).


Als Fachmann, der mit der Lösung der oben genannten Aufgabe betraut wird,
sieht der Senat einen Programmierer oder Informatiker mit mehrjähriger Berufserfahrung in der Modellierung von IT-Systemen und der Systemadministration an.


2.     Das jeweilige Verfahren sowohl nach dem Patentanspruch 1 nach Hauptantrag als auch nach den Patentansprüchen 1 der Hilfsanträge 1 bis 4 ist nicht
patentfähig, da es gemäß § 1 Abs. 3 Nr. 3 i. V. m. Abs. 4 PatG vom Patentschutz
ausgeschlossen ist.


2.1.   Das Verfahren nach Patentanspruch 1 nach Hauptantrag und auch die Verfahren nach den Patentansprüchen 1 nach den Hilfsanträgen 1 bis 4 liegen schon
deshalb zumindest mit einem Teilaspekt auf technischem Gebiet, weil sie eine
bestimmte Nutzung der Komponenten einer Datenverarbeitungsanlage lehren und
damit eine Anweisung zum technischen Handeln geben (BGH GRUR 2010, 613
- Dynamische Dokumentengenerierung).

                                      - 14 -



Darüber hinaus ist ein Verfahren gemäß der Rechtsprechung des Bundesgerichtshofs, das sich zur Herbeiführung des angestrebten Erfolges eines Programms bedient, mit dessen Hilfe eine Datenverarbeitungsanlage so gesteuert
wird, dass der gewünschte Erfolg erzielt wird, nicht schon wegen des Vorgangs
der elektronischen Datenverarbeitung dem Patentschutz zugänglich. Die beanspruchte Lehre muss vielmehr Anweisungen enthalten, die der Lösung eines konkreten technischen Problems mit technischen Mitteln dienen. (BGH GRUR 2005,
143 - RentabilitätsermittIung, BGH GRUR 2011, 125 - Wiedergabe topografischer
Informationen).


2.2.   Die Verfahren des jeweiligen Patentanspruchs 1 nach Hauptantrag und
nach den Hilfsanträgen 1 bis 4 sind vom Patentschutz ausgeschlossen, da keine
Anweisungen erkannt werden können, die der Lösung eines konkreten technischen Problems mit technischen Mitteln dienen. Dabei ist das technische Problem,
welches durch eine Erfindung gelöst wird, objektiv danach zu bestimmen, was die
Erfindung tatsächlich leistet (BGH GRUR 2005, 141 - Anbieten interaktiver Hilfe).
Weiterhin ist zu berücksichtigen, ob die Anmeldung über die außertechnischen
Vorgänge der Sammlung, Speicherung, Auswertung und Verwendung von Daten
hinaus für deren Umsetzung eine dem Patentschutz zugängliche technische Lehre
offenbart (BGH GRUR 2009, 479 - Steuerungseinrichtung für Untersuchungsmodalitäten).


Die Leistung der mit Patentanspruch 1 nach Hauptantrag beanspruchten Lehre
besteht darin, dass aus den Daten der IT-Umgebung ein Strukturbaum erstellt
wird, der die Topologie und die Beziehungen der Elemente dieser IT-Umgebung
abbildet. Weiterhin ist beansprucht, auf welchem Formalismus die Metastruktur
basiert, welche Definitionen für die Elemente und die Relationen zulässig sind und
welcher Aufbau der Metastruktur zugrunde liegt.
In Patentanspruch 1 nach Hilfsantrag 1 ist darüber hinaus ein Installationsautomat und ein Installationsskript beansprucht. Der Strukturbaum wird zur Ermittlung
der Installationsaufgaben an den Installationsautomaten übergeben, der aus den

                                       - 15 -



Daten des Strukturbaums die Installationsaufgaben und Installationsparameter
ermittelt, welche anschließend an ein Installationsskript, welches die Installation
durchführt, übergeben werden.
Gemäß Patentanspruch 1 nach Hilfsantrag 2 ist für die Durchführung der Installation ein Computer-implementiertes Verfahren vorgesehen.
Patentanspruch 1 nach Hilfsantrag 3 beinhaltet zusätzlich eine genaue Reihenfolge der Installation, d. h. zuerst die Server, dann die Middleware und abschließend die Applikationen.
In Patentanspruch 1 nach Hilfsantrag 4 wird zusätzlich die Installation eines Upgrades beansprucht.
Ein erstes objektives Problem, welches auch den Kern der Anmeldung betrifft,
besteht demnach darin, eine Datenstruktur zur Verfügung zu stellen, in welcher
die gesamten Daten (Attribute, Relationen usw.) der Elemente einer (realen oder
virtuellen) IT-Umgebung geordnet speicherbar sind, so dass eine IT-Umgebung
modelliert werden kann (Hauptanspruch).
Weitere objektiv erkennbare Probleme bestehen in
        -   der Bereitstellung eines Installationsautomaten und eines Installationsskripts, sowie der Übertragung von Daten und dem gezielten Extrahieren von Werten, die für eine automatisierte Installation benötigt werden (Hilfsantrag 1),
        -   das Vorsehen eines Computer-implementierten Verfahrens zur Durchführung der bereits aufgeführten Aufgaben (Hilfsantrag 2),
        -   in der genauen Festlegung einer Installationsreihenfolge (Hilfsantrag 3) und
        -   in der Verwendung des Verfahrens für die Installation eines Upgrades
            (Hilfsantrag 4).


Sämtliche der genannten Probleme betreffen jedoch die Datenverarbeitung und
die Datenorganisation. Denn sie gehen nicht über das Sammeln von Daten, das
Speichern von Daten in einer vorgegebenen Struktur (Organisation), die Übertra-

                                       - 16 -



gung von Daten und die Verarbeitung bzw. Verwendung von Daten (Generierung
von Werten und Abarbeiten von Programmschritten) hinaus.


Damit liegen die objektiven Probleme nur auf dem Gebiet der Datenverarbeitung,
da lediglich Daten erfasst, verarbeitet und übermittelt werden.
Die beanspruchten Verfahrensschritte gehen nicht über die Erfassung, Verarbeitung, Speicherung und Übermittlung von Daten hinaus. Dies ist nicht ausreichend
zur Überwindung des Ausschlusstatbestands des § 1 Abs. 3 Nr. 3 i. V. m. Abs. 4
PatG (BGH GRUR 2011, 610 - Webseitenanzeige).
Auch fließen keine auf technischen Überlegungen beruhenden Erkenntnisse in die
beanspruchte Lehre ein, was zur Überwindung der Ausschlusskriterien des § 1
PatG führen könnte (BGH GRUR 2000, 498 - Logikverifikation).


2.3.   Auch liegt keinem der einzelnen Teilschritte des beanspruchten Verfahrens
nach dem jeweiligen Patentanspruch 1 nach Hauptantrag und Hilfsantrag 1 bis 4
ein technisches Problem zugrunde.


2.3.1. Gemäß dem vorliegenden Patentanspruch 1 nach Hauptantrag wird ein
Strukturbaum erstellt, der die Topologie einer IT-Umgebung beschreibt, die ein
Benutzer benötigt. Eine derartige Erfassung von Daten und deren Organisation in
einer bestimmten Struktur geht jedoch nicht über die Zielsetzung hinaus, sich zur
Erreichung eines außertechnischen Ergebnisses einer Datenverarbeitungsanlage
zu bedienen. Dies begründet für sich aber noch kein technisches Problem (Merkmale (A), (B), (B1)).
Die Verwendung einer Metastruktur, die eine Definition der Verfahrenselementtypen und der Relationen sowie der zugeordneten Attribute festlegt, stellt ein Problem der Datenorganisation dar und löst somit ebenso kein technisches Problem
(Merkmale (D), (d1) bis (d4)).
Dies gilt in gleicher Weise für die Vorgabe, nach der innerhalb der Metastruktur
nur eindeutige und schleifenfreie Beziehungen zwischen den Elementen erlaubt
sind (Merkmal (E)) und für die Bedingung, dass die Metastruktur einem azyklisch

                                       - 17 -



gerichteten Graphen entspricht, der bei einer Wurzel startet und festgelegte Kriterien für die Beziehungen zwischen Elternelementen und Kindelementen aufweist
(Merkmale (F), (f1) bis (f3)).


Der Vertreter erläuterte hierzu, dass der Aufbau der Metastruktur, in der Attribute
und Relationen der Verfahrenselemente abgebildet werden, technisches Wissen
über die Komponenten des IT-Verfahrens und deren Zusammenwirken erfordere
und somit auf technischen Überlegungen beruhe.
Dem kann jedoch nicht gefolgt werden, da die zugrunde liegende Problemstellung
die Organisation der Daten betrifft. Durch die Metastruktur wird lediglich ein Regelwerk vorgegeben, nach dem die Daten sortiert bzw. in den Strukturbaum eingetragen werden. Auf welche Weise spezielle technische Gegebenheiten der verwendeten IT-Komponenten berücksichtigt werden könnten, ist nicht Gegenstand der
Patentansprüche.


Patentanspruch 1 nach Hauptantrag sind somit keine Anweisungen zur Lösung
eines technischen Problems mit technischen Mitteln entnehmbar.


2.3.2. Der Patentanspruch 1 nach Hilfsantrag 1 unterscheidet sich von Patentanspruch 1 nach Hauptantrag durch die Merkmale (A1), (C1), (C2), (D1), (f4) und
(f5).


Die Merkmale (A1) und (C1) betreffen die Gesamtbehandlung eines IT-Verfahrens
zur Erstellung eines Strukturbaums, der die Topologie einer IT-Umgebung beschreibt. Analog zu den Ausführungen zum Hauptantrag begründet auch ein derartiges Verfahren für sich noch kein technisches Problem.
Das Ermitteln von Installationsaufgaben für die automatische Installation von IT-Komponenten aus den Daten des Strukturbaums (Merkmal (C2)) stellt ebenfalls
kein technisches Problem dar, sondern betrifft die Datenverarbeitung und somit
eine Programmieraufgabe. Denn es bedarf lediglich der Festlegung, welche Daten
für die Durchführung der Installationsaufgaben aus den Daten des Strukturbaums

                                       - 18 -



verwendet werden und wie diese ausgelesen werden. Für die Durchführung einer
automatisierten Installation ist anschließend die Übergabe der Daten an ein weiteres Programmodul notwendig.
In Merkmal (D1) ist angegeben, dass die Topologie des IT-Verfahrens in dem
Strukturbaum beschrieben wird. Dies bedeutet, dass zusätzlich zu Merkmal (D)
nach Patentanspruch 1 nach Hauptantrag, nicht nur die Topologie der Elemente,
sondern auch deren Beziehungen in dem Strukturbaum abgebildet werden. Eine
Abbildung der Beziehungen zwischen den Elementen ist jedoch bereits in den
Merkmalen (d3) und (d4) des Patentanspruchs 1 nach Hauptantrag beansprucht.
Wie bereits ausgeführt betreffen diese Merkmale die Datenorganisation und kein
technisches Problem (siehe 2.2.).
Die Übergabe des Strukturbaums an einen Installationsautomaten, der die Installationsparameter und die Installationsreihenfolge festlegt und der entsprechend
dieser Daten ein Installationsparameter-Set an ein Installationsskript zur Durchführung der automatisierten Installation übergibt, betrifft die modulare Programmierung. Denn sowohl der Installationsautomat als auch das Installationsskript stellen
einen Prozess dar, der durch entsprechende Programmmodule abgearbeitet wird
(Merkmale (f4) und (f5)).


Der Vertreter machte geltend, dass der Installationsautomat den Strukturbaum
erhält und aus dessen Daten die Installationsparameter sowie die Installationsreihenfolge ermittelt und an ein Installationsskript übergibt. Dadurch könnten gegenüber einer Installation von Hand Fehler stark verringert werden.


Dies ändert jedoch nichts daran, dass es sich hierbei um reine Maßnahmen der
Datenverarbeitung handelt. Die Übergabe von Daten an ein Modul (Installationsautomat) sowie das Verarbeiten der Daten wie bspw. das Auslesen von Informationen und die Weitergabe dieser Informationen sind übliche Programmschritte.


Somit sind auch dem Patentanspruch 1 nach Hilfsantrag 1 keine Anweisungen zur
Lösung eines technischen Problems mit technischen Mitteln entnehmbar.

                                     - 19 -



2.3.3. Der Patentanspruch 1 nach Hilfsantrag 2 bedient sich eines übergeordneten Programms zur automatischen Installation (Merkmal (A2)). Die dabei verwendete Beschreibung der Topologie durch einen Strukturbaum (Merkmal (C1*)) entspricht dem Merkmal (C1) des Patentanspruchs 1 nach Hilfsantrag 1. Eine Angabe der Anordnung der Elemente in dem Strukturbaum beschreibt lediglich die
Organisation der Daten (Merkmal (C3)). Schließlich stellen auch hier die Übergabe
der Daten, deren Verarbeitung, wie bspw. das Generieren von Parametern und
das anschließende Ausführen eines Programmmoduls unter Verwendung dieser
Parameter reine Maßnahmen der Datenverarbeitung dar.


Zu diesem Antrag stellte der Vertreter dar, dass der Aufbau des Strukturbaums,
insbesondere die deutliche Angabe der Eltern-Kind-Beziehungen, bei der Installation grundlegende Bedeutung habe. So werde dadurch ein Schutz bspw. gegen
unbeabsichtigtes Löschen von vorhandener Software bei einer Installation gewährleistet.


Es erscheint durchaus plausibel, dass dieses Vorgehen Vorteile bietet. Jedoch
gehen auch diese Maßnahmen nicht über den Bereich der Organisation und Verarbeitung von Daten hinaus.


Auch dem Patentanspruch 1 nach Hilfsantrag 2 sind demnach keine Anweisungen
zur Lösung eines technischen Problems mit technischen Mitteln entnehmbar.


2.3.4. In Patentanspruch 1 nach Hilfsantrag 3 sind neben rein redaktionellen
Änderungen (Merkmale (B*), (C4*), (D*)) noch die Merkmale (d5), (C5*), (C6*),
(C7*), (C8), (C9) und (C10) neu hinzugekommen. Mit der zusätzlichen Angabe,
wonach die Elementtypen der Metastruktur auch Server, Middleware und Applikationen umfassen, wird die Organisation der Daten weiter spezifiziert (Merkmal (d5)). Die Übergabe des Strukturbaums, d. h. des gesamten strukturierten
Datensatzes an den Installationsautomaten fällt in den Bereich der Datenübermittlung. Der folgende Prozess der Extrahierung von einzelnen Daten oder Para-

                                       - 20 -



metern, deren Weitergabe und das Ausführen eines Programms in einer durch die
Parameter definierten Reihenfolge erfolgt mittels Programmmodulen und geht
nicht über die computergestützte Datenverarbeitung hinaus.


Der Vertreter machte geltend, dass die Metastruktur des Strukturbaums, wie sie
hier beansprucht ist, die notwendigen Attribute und Parameter weiter konkretisiere. Aus diesen Werten generiere der Installationsautomat die Parameter-Sets
für das Installationsskript, wodurch die gesamte Steuerung der Installation auf den
Daten des Strukturbaums beruhe. Sowohl der Installationsautomat als auch die
Installationsskripte seien damit technische Mittel zur Lösung des technischen
Problems, die Installation von Komponenten auf einem IT-System zu steuern.


Auch diese Ausführungen tragen nicht zu einer geänderten Beurteilung der Sachlage bei. Wie bereits mehrfach dargestellt definiert die Metastruktur des Strukturbaums die Organisation der Daten. Die bei der Installation durchgeführten Verarbeitungsschritte fallen vollständig in den Bereich der rechnergestützten Datenverarbeitung. Damit sind der Installationsautomat und das Installationsskript als Programmmodule anzusehen. Anweisungen, die über einen Verfahrensablauf innerhalb der Datenverarbeitungsanlage hinausweisen, etwa im Sinne der Steuerung
einer externen technischen Einrichtung, sind nicht ersichtlich.


Dem Patentanspruch 1 nach Hilfsantrag 3 sind demnach ebenfalls keine Anweisungen zur Lösung eines technischen Problems mit technischen Mitteln entnehmbar.


2.3.5. Schließlich sind in Patentanspruch 1 nach Hilfsantrag 4 die Merkmale (C5**), (G) und (g1) bis (g4) neu ergänzt. Ein Export von Parametern und deren
Übergabe betrifft ein Problem der Datenverarbeitung und Übertragung (Merkmal (C5**)). Die Installation eines Upgrades, bei dem notwendige Daten exportiert
und in eine Struktur gebracht werden und bei dem ein Vergleich von Daten statt-

                                     - 21 -



findet, wobei nach dem Vergleich anhand der Parameter Ablaufschritte eines Upgrade-Programms festgelegt werden, stellt eine Programmieraufgabe dar.


Hinsichtlich dieses Antrags führte der Vertreter aus, dass ein Strukturbaum eines
vorhandenen Release und ein Strukturbaum eines geplanten Release exportiert
werden. Nach einem Vergleich werden die notwendigen Daten für ein Upgrade
extrahiert und mit diesen Daten wird das Upgrade durchgeführt. Dadurch würden
bei einem Upgrade nur die minimal notwendigen Änderungen der Software vorgenommen.


Auch diese Ausführungen können die patentrechtliche Beurteilung nicht ändern.
Denn die Daten des Strukturbaums der existierenden IT-Umgebung liegen nach
der Erfassung in strukturierter Form vor. Die Daten des geplanten Upgrades, die
aus dem Softwarerelease ermittelt werden, werden nach den gleichen Organisationsregeln in einen weiteren Strukturbaum eingetragen. Ein anschließender Vergleich wird durch ein Programm bewerkstelligt. Die Ergebnisse des Vergleichs liefern die notwendigen Parameter für die folgende, wiederum durch ein Programm
durchgeführte, automatische Installation des Upgrades.


Damit sind dem Patentanspruch 1 nach Hilfsantrag 4 keine Anweisungen zur
Lösung eines technischen Problems mit technischen Mitteln entnehmbar.


2.4.   Mit dem jeweiligen Anspruch 1 nach Hauptantrag und nach den Hilfsanträgen 1 bis 4 fallen auch die übrigen Patentansprüche (2 bis 16 gemäß Hauptantrag, 2 bis 14 gemäß erstem Hilfsantrag, 2 bis 14 gemäß zweitem Hilfsantrag, 2
bis 13 gemäß drittem Hilfsantrag und 2 bis 11 gemäß viertem Hilfsantrag) da über
einen Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120
- Elektrisches Speicherheizgerät).

                                            - 22 -



Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
       Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
       sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
       zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                  Eder                Dr. Thum-Rung                 Hoffmann




                                                                                        Fa
