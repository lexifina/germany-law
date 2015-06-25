---
ecli: "ECLI:DE:BPatG:2015:250615B17Wpat46.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 46/12"
decided: "2015-06-25"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=27&nr=27414&anz=851&pos=413&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-06-25_17_W-pat_46_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 46/12 vom 2015-06-25

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 46/12                                                   Verkündet am
_______________                                                     25. Juni 2015
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2006 058 588.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 25. Juni 2015 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der    Richterin   Eder,   des   Richters
Dipl.-Ing. Baumgardt und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                     -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamts vom 27. Dezember 2011 aufgehoben und die Sache zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und
       Markenamt zurückverwiesen.


       Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                  Gründe


                                      I.


Die vorliegende Patentanmeldung, welche die Priorität einer Voranmeldung in den
USA vom 14. Dezember 2005 in Anspruch nimmt, wurde am 12. Dezember 2006
in englischer Sprache beim Deutschen Patent- und Markenamt eingereicht. Sie
trägt in der deutschen Übersetzung die Bezeichnung


   „Verfahren zum Bewerten von Modellen eines Fahrzeugfahrverhaltens oder
                    Fahrzeugverwendungsmodelldetektor“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 27. Dezember 2011 mit der Begründung zurückgewiesen, dass der Gegenstand des (damaligen) Patentanspruchs 1
von einem universell anwendbaren Verfahren zum Ermitteln des wahrscheinlichsten statistischen Modells eines Fahrverhaltens eines beobachteten Fahrzeugs
bestimmt werde, dessen einzelne Schritte einen Algorithmus und somit eine
mathematische Methode als solche darstellten. Der Gegenstand des Patentan-

                                          -3-



spruchs 1 falle damit unter das Patentierungsverbot des § 1 PatG und sei daher
nicht gewährbar.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellt den Antrag,


           den angegriffenen Beschluss aufzuheben und das nachgesuchte
           Patent mit folgenden Unterlagen zu erteilen:


           Patentansprüche 1-7, überreicht in der mündlichen Verhandlung,
           Beschreibung Seiten 1-3, 3a, 16 vom 31.01.2011,
           Beschreibung Seiten 4-15 und
           2 Blatt Zeichnungen mit Figuren 1-3, jeweils vom 08.03.2007.


Sie regt die Rückzahlung der Beschwerdegebühr an.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist die Druckschrift


D1:       US 2002/0128751 A1


genannt worden. Vom Senat wurden zusätzlich die Druckschriften


D2:       LIN, C.; PENG, H.; GRIZZLE, J.: A Stochastic Control Strategy for
Hybrid Electric Vehicles. In: Proceedings of the 2004 American Control
Conference, 2004,


D3:       GUNDLICH, B.; TEUNISSEN, P.: Multiple Models – Fixed, Switching,
Interacting. In: V Hotine-Marussi Symposium on Mathematical Geodesy,
pp. 129-136, Springer, 2004, ISBN 978-3-642-06028-1

                                        -4-



und


D4:   KIM, Y.; HONG, K.: An IMM Algorithm for Tracking Maneuvering
Vehicles in an Adaptive Cruise Control Environment. In: International
Journal of Control, Automation, and Systems, vol 2, no. 3, pp. 310-318,
September 2004


eingeführt.


Der geltende, in der mündlichen Verhandlung überreichte Patentanspruch 1, hier
mit einer möglichen Gliederung versehen, lautet:


        (a´) Verfahren zum Ermitteln des wahrscheinlichsten statistischen
              Modells eines Fahrverhaltens eines beobachteten Fahrzeugs
              von einem Zeitschritt k bis zur Gegenwart, um die Kraftstoffwirtschaftlichkeit bei einem Hybrid-Fahrzeug mit einer Batterie, die eine Batterieleistung liefert, und einer Maschine, die
              eine Maschinenleistung liefert, zu verbessern, wobei das
              Verfahren umfasst, dass


        (a´´) das Fahrverhalten des Fahrzeugs beobachtet wird, was das
              Beobachten der Fahrzeuggeschwindigkeit umfasst;


        (a)   mindestens zwei statistische Modelle eines Fahrverhaltens
              aufgestellt werden, wobei die mindestens zwei statistischen
              Modelle Modelle einer bedingten Wahrscheinlichkeit sind, die
              die Wahrscheinlichkeit von Zuständen bei einem nächsten
              Zeitschritt k  1 beschreiben, wobei


        (a2) die Fahrzeuggeschwindigkeit, ein Drehmoment, eine Beschleunigung, eine Straßenneigung, eine Tageszeit, eine

                                 -5-



      Fahrzeugbeladung, eine Insassenanzahl und eine Fahreridentifikation als Eingaben für die mindestens zwei statistischen Modelle verwendet werden


(a4) und wobei die jeweiligen Zustände bei dem momentanen
      Zeitschritt k gegeben sind;


(b)   eine anfängliche Wahrscheinlichkeitsverteilung der mindestens zwei statistischen Modelle eines Fahrverhaltens ermittelt
      wird;


(c)   die Wahrscheinlichkeit ermittelt wird, dass ein beobachteter
      Übergang des Fahrverhaltens durch die mindestens zwei statistischen Modelle eines Fahrverhaltens vorhergesagt wird;


(d)   die Wahrscheinlichkeit berechnet wird, dass die mindestens
      zwei statistischen Modelle ein Fahrverhalten des beobachteten Fahrzeugs bei dem nächsten Zeitschritt k  1 erklären;


(d2) und wobei (c), Ermitteln der Wahrscheinlichkeit des beobachteten Übergangs, und (d), Berechnen der Wahrscheinlichkeit
      der mindestens zwei statistischen Modelle, für alle Zeitschritte
      bis zur Gegenwart wiederholt werden;


(e)   ermittelt wird, welches der mindestens zwei statistischen
      Modelle die größte Wahrscheinlichkeit des Erklärens des
      beobachteten Fahrverhaltens aufweist; und


(f)   auf Grundlage des ermittelten statistischen Modells eines
      Fahrverhaltens das Verhältnis von gegenwärtig verwendeter
      Batterieleistung und Maschinenleistung unter Verwendung

                                        -6-



               von Leistungsverzweigungssteuerungen des Fahrzeugs, die
               zum Beeinflussen dieses Verhältnisses ausgebildet sind,
               beeinflusst wird, um die Kraftstoffwirtschaftlichkeit bei dem
               nächsten Zeitschritt k  1 zu verbessern, wobei den Leistungsverzweigungssteuerungen zugehörige Kalibrierungen
               gesteuert werden.


Der Patentanspruch 2 lautet:


       „Verfahren nach Anspruch 1, wobei das statistische Modell eines
       Fahrverhaltens ein Modell einer bedingten Wahrscheinlichkeit ist,
       das die Wahrscheinlichkeit P        bei einem Zeitschritt k  1 beschreibt, dass eine Fahrzeuggeschwindigkeit v k 1 vorliegt, wobei

       eine Fahrzeuggeschwindigkeit v k bei dem Zeitschritt k gegeben

       ist.“


Der Patentanspruch 3 lautet:


       „Verfahren nach Anspruch 1, wobei das statistische Modell eines
       Fahrverhaltens aus einem Beispiel eines Fahrens gebildet wird,
       das das Fahrverhalten darstellt; und wobei das Beispiel die
       Geschwindigkeit des Fahrzeugs über der Zeit umfasst.“


Der Patentanspruch 4 lautet:


       „Verfahren nach Anspruch 1, wobei (b), Ermitteln der anfänglichen
       Wahrscheinlichkeitsverteilung des statistischen Modells, umfasst,
       dass ein Vektor  0 als die anfängliche Wahrscheinlichkeitsvertei-

       lung festgesetzt wird, wobei der Vektor  0 für jedes statistische

       Modell vorbestimmt wird.“

                                       -7-



Der Patentanspruch 5 lautet:


       „Verfahren nach Anspruch 4, wobei es N statistische Modelle
       eines Fahrverhaltens gibt, wobei jedes Element des Vektors  0

       auf 1 / N gesetzt wird, wodurch jedes Modell eine gleiche Wahrscheinlichkeit eines Übereinstimmens eines Fahrverhaltens des
       beobachteten Fahrzeugs aufweist.“


Der Patentanspruch 6 lautet:


       „Verfahren nach Anspruch 1, wobei (c), Ermitteln der Wahrscheinlichkeit, dass der beobachtete Übergang durch jedes statistische
       Modell eines Fahrverhaltens vorhergesagt wird, umfasst, dass eine
       Referenznachschlagtabelle eingesetzt wird, wobei die Nachschlagtabelle eine für jedes statistische Modell entwickelte zweidimensionale Matrix ist, wobei es N statistische Modelle eines Fahrverhaltens gibt, wobei die Nachschlagtabelle drei unabhängige
       Indizes aufweist; einen Index, der das statistische Modell, die
       momentane Geschwindigkeit und die vorherige Geschwindigkeit
       des beobachteten Fahrzeugs identifiziert; und eine vorbestimmte
       Matrix M 1 eingesetzt wird, um die Wahrscheinlichkeit eines Übergehens von einem Fahrverhalten zu einem anderen bei jedem
       Beispiel zu definieren, wobei M 1 eine Markov-Matrix ist.“


Der Patentanspruch 7 lautet:


       „Verfahren nach Anspruch 6, wobei (c), Berechnen der Wahrscheinlichkeit, dass das statistische Modell das Fahrverhalten des
       beobachteten Fahrzeugs bei dem Zeitschritt k  1 erklärt, umfasst,
       dass eine vorbestimmte Matrix M 2 eingesetzt wird, um die Wahr-

                                      -8-



         scheinlichkeit eines Übergehens von einem Fahrverhalten zu
         einem anderen bei jedem Beispiel zu definieren, wobei M 2 eine
         Markov-Matrix ist.“


Die Anmelderin trägt vor, dass mit Hilfe des beanspruchten Verfahrens das wahrscheinlichste statistische Modell eines Fahrverhaltens eines beobachteten Fahrzeugs ermittelt werden könne. Der Vorteil des Gegenstandes der Anmeldung
bestehe insbesondere darin, dass zwischen mehreren Modellen umgeschaltet
werden könne, wodurch eine genauere Vorhersage des Fahrverhaltens ermöglicht
werde. Aufgrund der genaueren Vorhersage könne auch eine verbesserte Steuerung des Verhältnisses von Batterie- und Maschinenleistung erzielt werden,
wodurch das Fahrzeug besonders effizient betrieben werden könne.


Ein solches Verfahren sei nicht nur technisch, es sei darüber hinaus durch den
den Druckschriften D1 bis D4 entnehmbaren Stand der Technik weder bekannt
noch durch diesen nahegelegt.




                                       II.


Die rechtzeitig eingegangene und auch sonst zulässige Beschwerde führt zur Aufhebung des angefochtenen Beschlusses und zur Zurückverweisung der Sache an
das Deutsche Patent- und Markenamt gemäß § 79 Abs. 3 Satz 1 Nr. 3 PatG.


1.     Die vorliegende Patentanmeldung bezieht sich auf ein Verfahren zum
Ermitteln der Wahrscheinlichkeit, dass ein statistisches Modell das Fahrverhalten
oder die Verwendung eines beobachteten Fahrzeugs beschreibt (Offenlegungsschrift, [0001]).


Wie in der Anmeldung ausgeführt, umfassen die Ziele für die Entwicklung von
Hybridelektrofahrzeugen die Verbesserung der Kraftstoffwirtschaftlichkeit und die

                                      -9-



Reduzierung von Schadstoffemissionen von Automobilen. Bei der Konstruktion
eines Hybrid-Fahrzeugs werde die Kraftstoffwirtschaftlichkeit mittels optimierter
Operationen und einer Steuerstrategie maximiert. Ein statistisches Modell eines
Fahrverhaltens könne dabei eine Optimierung von Operationen sowohl für Hybridals auch Nicht-Hybrid-Fahrzeuge bieten (Offenlegungsschrift, [0002]). Aus der
Beschreibung geht sinngemäß hervor, dass eine an das jeweilige Fahrverhalten
des Fahrzeugs angepasste Ermittlung statistischer Modelle bislang nicht bekannt
sei, so dass aus Sicht der Steuerung des Hybridmotors z. B. zwischen einem Fahren auf einer Schnellstraße und einem Fahren in der Stadt oftmals nicht eindeutig
unterschieden werden könne.


Die der Anmeldung zugrundeliegende objektive technische Aufgabe sieht der
Senat darin, ein Verfahren zu schaffen, mit dem ein statistisches Modell identifiziert werden kann, welches das momentane Fahrverhalten eines Hybrid-Fahrzeugs am besten beschreibt und auf dessen Grundlage die passende Steuerstrategie für den Hybridmotor gefunden bzw. das Verhältnis aus Batterie- und Maschinenleistung optimal eingestellt werden kann.


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren anzugeben, mit
dem der Kraftstoffverbrauch eines Hybrid-Fahrzeugs optimiert werden kann, ist ein
berufserfahrener Maschinenbauingenieur anzusehen, welcher nicht nur über fundierte Kenntnisse auf dem Gebiet von Brennkraftmaschinen und Hybridantrieben
verfügt sondern auch mit der Anwendung numerischer Lösungsmethoden zur
Bestimmung der charakteristischen Zustandsgrößen vertraut ist.


2.    Das geltende Patentbegehren ist zulässig. Zudem ist der Gegenstand nach
Patentanspruch 1 dem Patentschutz grundsätzlich zugänglich sowie durch den
aus den Druckschriften D1 bis D4 entnehmbaren Stand der Technik weder neuheitsschädlich vorweggenommen noch durch diesen nahegelegt.

                                      - 10 -



2.1    Zur Lösung der genannten Aufgabe schlägt der Patentanspruch 1 ein Verfahren nach den Merkmalen (a´) bis (f) vor.


Der Patentanspruch 1 bedarf der Auslegung.


Mit Hilfe des beanspruchten Verfahrens soll das wahrscheinlichste statistische
Modell ermittelt werden, das das Fahrverhalten eines beobachteten Hybrid-Fahrzeugs von einem Zeitschritt k bis zu einem gegenwärtigen Zeitpunkt beschreibt.
Es soll dazu dienen, die Kraftstoffwirtschaftlichkeit des Fahrzeugs zu verbessern,
d. h. seinen Kraftstoffverbrauch zu optimieren. Laut Patentanspruch 1 verfügt das
Fahrzeug über eine Batterie und eine Maschine, die jeweils eine Batterie- und
Maschinenleistung erbringen (Merkmal (a´)). Der Senat versteht dabei unter der
Maschine in erster Linie eine Brennkraftmaschine.


Im Verfahrensschritt (a´´) wird das Fahrverhalten des Fahrzeugs beobachtet, was
das Beobachten der Fahrzeuggeschwindigkeit umfasst. Die gemäß Anspruchswortlaut gewählte Umschreibung „Beobachten der Fahrzeuggeschwindigkeit“, bei
der es sich nach dem Verständnis des Senats um eine zielgerichtete Wahrnehmung des Fahrzeugs bzw. von dessen Geschwindigkeit handelt, lässt dabei offen,
ob das Merkmal (a´´) auf eine Simulation mit Test oder eine reale Messung
abstellt.


Merkmal (a) besagt, dass wenigstens zwei statistische Modelle erstellt werden, die
jeweils ein Fahrverhalten beschreiben. Jedes Modell beinhaltet bedingte Wahrscheinlichkeiten, die die jeweiligen Wahrscheinlichkeiten für das Eintreten eines
Zustandes zu einem nächsten Zeitschritt k  1 angeben unter der Bedingung, dass
ein bestimmter Zustand, beschrieben durch die unter Merkmal (a2) aufgezählten
Größen, zu einem früheren Zeitschritt k bereits vorliegt (Merkmal (a4)). Laut
Merkmal (a2) werden die Fahrzeuggeschwindigkeit, ein Drehmoment, eine
Beschleunigung, eine Straßenneigung, eine Tageszeit, eine Fahrzeugbeladung,
eine Insassenanzahl und eine Fahreridentifikation als Eingaben für die mindestens

                                          - 11 -



zwei statistischen Modelle verwendet. Entsprechend der Beschreibung geben die
bedingten Wahrscheinlichkeiten eines Modells z. B. dann an, mit welcher Wahrscheinlichkeit eine Fahrzeuggeschwindigkeit v k 1        zu einem späteren Zeit-

punkt k  1 angenommen wird, wenn ein Zustand mit einer gewissen Fahrzeuggeschwindigkeit v k , einem Drehmoment Tk usw. beobachtet wird (Offenlegungs-

schrift, [0014], [0037]).


Das beanspruchte Verfahren umfasst ferner, eine anfängliche Wahrscheinlichkeitsverteilung für die mindestens zwei statistischen Modelle festzulegen, welche
jeweils ein bestimmtes Fahrverhalten beschreiben (Merkmal (b)). Wie in der
Beschreibung ausgeführt, wird diese Wahrscheinlichkeitsverteilung durch einen
Vektor repräsentiert, der die anfängliche Wahrscheinlichkeit umfasst, dass überhaupt eines der wenigstens zwei Modelle mit dem Fahrverhalten übereinstimmt
(Offenlegungsschrift, [0015]). Insoweit entspricht Merkmal (b) der Initialisierung
einer Wahrscheinlichkeit zu einem Anfangszeitpunkt. Aus der Beschreibung geht
hervor, dass jedes statistische Modell für ein spezielles Fahrverhalten steht, z. B.
ein Fahren auf einer Schnellstraße bzw. in der Stadt oder einen aggressiven Fahrstil (Offenlegungsschrift, [0005]).


Unter Beobachtung des Fahrverhaltens bzw. der Fahrzeuggeschwindigkeit wird
die Wahrscheinlichkeit dafür ermittelt, dass ein Übergang des Fahrverhaltens
(z. B. von Schnellstraße zu Stadtverkehr) durch die wenigstens zwei statistischen
Modelle für das Fahrverhalten vorhergesagt wird (Merkmal (c)). Damit findet die
Wahrscheinlichkeit für einen Wechsel zwischen den statistischen Modellen zum
Zeitschritt k Berücksichtigung (Offenlegungsschrift, [0017], siehe Ptrans,mdli ).


Merkmal (d) besagt, dass außerdem die Wahrscheinlichkeit dafür berechnet werden soll, dass die wenigstens zwei statistischen Modelle ein Fahrverhalten des
Fahrzeugs bei dem nächsten Zeitschritt k  1 erklären bzw. beschreiben. Diese
wird in der Beschreibung durch einen Vektor repräsentiert, dessen Komponen-

                                       - 12 -



ten Pmdl,k 1 die jeweiligen Wahrscheinlichkeiten dafür angeben, dass eines der

statistischen Modelle das Fahrverhalten zum Zeitschritt k  1 richtig kennzeichnet
(Offenlegungsschrift, [0018]).


Entsprechend Merkmal (d2) sollen die Berechnung der Wahrscheinlichkeit für eine
Änderung im Fahrverhalten gemäß Merkmal (c) sowie die Ermittlung der Wahrscheinlichkeit für die richtige Beschreibung des (zu einem späteren Zeitschritt vorliegenden) Fahrverhaltens durch eines der statistischen Modelle gemäß Merkmal (d) rekursiv wiederholt werden, und zwar für alle betrachteten Zeitschritte bis
zu einem gegenwärtigen Zeitpunkt.


Merkmal (e) sieht vor zu bestimmen, welches der mindestens zwei statistischen
Modelle die größte Wahrscheinlichkeit besitzt, das Fahrverhalten des Fahrzeugs
in geeigneter Weise zu beschreiben.


Auf der Grundlage des auf diese Weise gefundenen statistischen Modells sollen
mit Hilfe von Leistungsverzweigungssteuerungen des Fahrzeugs Batterie- und
Maschinenleistung derart eingestellt werden, dass die Kraftstoffwirtschaftlichkeit
des Fahrzeugs verbessert wird. Hierbei sollen Kalibrierungen, die zu den Leistungsverzweigungssteuerungen gehören, gesteuert werden (Merkmal (f)). In der
Beschreibung wird hierzu ausgeführt, dass die Leistungsverzweigungssteuerungen das Verhältnis von Batterie- und Maschinenleistung, die zu einem gegenwärtigen Zeitpunkt erbracht werden, beeinflussen. Dies geschieht mittels „steuerbarer“
Betriebsparameter des Fahrzeugs, die Kalibrierungen und „andere geeignete
Parameter“ umfassen sollen (Offenlegungsschrift, [0038]). Die Kalibrierung des in
der Beschreibung geschilderten „Allgemeinen Algorithmus“ erfolgt anhand von
anfänglichen Wahrscheinlichkeitsverteilungen der statistischen Modelle, Markov-Matrizen und bedingten Übergangswahrscheinlichkeiten (Offenlegungsschrift,
[0020]-[0023]).


2.2   Das geltende Patentbegehren ist zulässig.

                                         - 13 -



Der Patentanspruch 1 geht hervor aus dem ursprünglichen Patentanspruch 10
und Teilen der Beschreibung.


So beruht das „Verfahren zum Ermitteln des wahrscheinlichsten statistischen
Modells eines Fahrverhaltens eines beobachteten Fahrzeugs von einem Zeitschritt k bis zur Gegenwart“ zusammen mit den Merkmalen (a), (a4) und (b) bis
(e) auf dem ursprünglichen Patentanspruch 10.


Das hinzugefügte Teilmerkmal, wonach das beanspruchte Verfahren eingesetzt
wird, um die Kraftstoffwirtschaftlichkeit in einem Hybrid-Fahrzeug zu verbessern,
welches über eine Batterie, die eine Batterieleistung liefert, und eine Maschine, die
eine Maschinenleistung liefert, verfügt, wird auf der Beschreibungsseite 13, Zeilen 9 bis 23 beschrieben (Offenlegungsschrift, [0038]).


Das Beobachten des Fahrverhaltens des Fahrzeugs zusammen mit der Fahrzeuggeschwindigkeit gemäß Merkmal (a´´) findet seine Stütze auf Seite 9, Zeilen 1
bis 10 der Beschreibung (Offenlegungsschrift, [0026]).


Merkmal (f), welches die Beeinflussung des Verhältnisses von Batterie- und
Maschinenleistung betrifft, geht hervor aus Seite 13, Zeilen 9 bis 23 (Offenlegungsschrift, [0038]).


Merkmal (a2) ist in der Beschreibung auf der Seite 4, Zeile 26 bis Seite 5, Zeile 6
und der Seite 12, Zeile 27 bis Seite 13, Zeile 5 offenbart (Offenlegungsschrift,
[0013], [0037]).


Die abhängigen Patentansprüche 2 bis 7 sind mit den ursprünglichen Patentansprüchen 2, 3 sowie 5 bis 8 identisch.


Die in den Beschreibungsseiten vorgenommenen Änderungen sind zulässig.

                                     - 14 -



Die geltenden Figuren entsprechen den ursprünglich eingereichten Figuren.


2.3   Das Verfahren nach Patentanspruch 1 ist dem Patentschutz grundsätzlich
zugänglich, da es die Lösung eines konkreten technischen Problems (vgl. die
oben angegebene Aufgabe) mit technischen Mitteln liefert.


2.4   Die Lehre des Patentanspruches 1 ist durch den bisher bekannten Stand
der Technik weder vorbekannt noch nahegelegt. Denn aus keiner der Druckschriften ist entnehmbar, dass die Fahrzeuggeschwindigkeit, ein Drehmoment,
eine Beschleunigung, eine Straßenneigung, eine Tageszeit, eine Fahrzeugbeladung, eine Insassenanzahl und eine Fahreridentifikation als Eingaben für die mindestens zwei statistischen Modelle verwendet werden.


Die Druckschrift D1 befasst sich mit einem Verfahren zur automatischen Erkennung von langfristigen Fahrmustern eines Fahrzeugs in Echtzeit unter Verwendung eines statistischen Muster-Erkennungssystems ([0003]; [0032]). Die Mustererkennung ist durch vorwärtsgekoppelte neuronale Netzwerkmodelle implementiert, die zur Erkennung von beispielsweise vier Klassen einer Fahrumgebung aus
Daten des Fahrzeug-Leistungsverhaltens entwickelt wurden ([0032]; Fig. 1). Als
Eingangsgrößen können zeitliche Mittelwerte, Standardabweichungen und mittlere
Abweichungen von Fahrzeugparameterverläufen in das Verfahren eingehen
([0037] bis [0039]). Das vorgestellte System beinhaltet Modelle, die die
gewünschten Klassifikationsschemata aus empirischen Daten lernen anstatt entsprechend vorprogrammiert zu werden. Die angewandten neuronalen Netze werden z. B. darauf trainiert, vier Kategorien von Fahrmustern zu erkennen, nämlich
Autobahn („highway“), Hauptstraße („main road“), Vorstadt („suburban“) und
Innenstadt („city driving“). Eine wichtige Anwendung des bekannten Verfahrens
besteht in einer an erkannte Fahrmuster angepassten Optimierung von Motor- und
Fahrwerkparametern in Echtzeit oder in einer Unterstützung von Fahrerassistenzsystemen ([0053]).

                                        - 15 -



Die Druckschrift D1 setzt sich im Wesentlichen damit auseinander, wie ein Fahrverhalten einem Fahrmuster zugeordnet werden kann ([0033], siehe „Bayes Theorem“).


Die Druckschrift D2 beschreibt ein Verfahren zur Ermittlung einer stochastischen
Steuerungsstrategie für das Antriebsmanagement in Elektro-Hybridfahrzeugen.
Um eine solche Strategie zu erhalten, wird im Wesentlichen vorgeschlagen, die
durch den Fahrer des Hybrid-Fahrzeugs angeforderte Motorleistung als Markov-Kette bzw. Markov-Prozess zu modellieren. Eine optimale Steuerungsstrategie
wird dann durch den Mechanismus der Stochastischen Dynamischen Programmierung („Stochastic Dynamic Programming“ SDP) bestimmt (Abstract). Die Güte
der präsentierten stochastischen Näherung wird sowohl anhand von Standard-Fahrzyklen, die das Fahren in der Innenstadt, der Vorstadt oder auf der Autobahn
repräsentieren, als auch anhand von zufallsbedingten Fahrzyklen in einer
SIMULINK-Umgebung überprüft (Seite 3, linke Spalte, siehe „It follows that specifying driving-cycle characteristics is equivalent to specifying the transition probabilities … and highway driving.“; Seite 5, Abschnitt 5.2 - „Simulation Results“). Insbesondere wird das Leistungsverzweigungsverhältnis („Power-Split-Ratio“ PSR)
aus der Leistung der Brennkraftmaschine und der angeforderten Motorleistung
optimiert (Seite 5, linke Spalte, erster Absatz). Das Verfahren der Druckschrift D2
beruht u. a. auf der Anwendung zumindest eines statistischen Modells, welches
bedingte Wahrscheinlichkeiten beinhaltet. In ein solches statistisches Modell können wenigstens zwei verschiedene Zustandsgrößen, nämlich die zu einem Zeitpunkt k angeforderte Motorleistung Pdem und die Radgeschwindigkeit wh , eingege-

ben und als Wahrscheinlichkeitsbedingung berücksichtigt werden (Seite 3, linke
Spalte, Gleichung (6) u. a.).


Die Druckschrift D3 behandelt in erster Linie die wahrscheinlichkeitstheoretische
Beschreibung dynamischer Systeme mittels Bayesscher Statistik. Der mathematische Formalismus unter der jeweiligen Annahme eines festgelegten Modells
(„fixed“), mehrerer wechselnder Modelle („switching“) und miteinander wechselwir-

                                       - 16 -



kender („interacting“) Modelle wird dargestellt (Seiten 130-134). Aus der Druckschrift D3 geht zumindest hervor, dass im Fall der Beschreibung eines dynamischen Systems durch mehrere statistische Modelle nicht nur die bedingten Wahrscheinlichkeiten für den Übergang von Zustandsgrößen sondern ebenso Wahrscheinlichkeiten für einen Wechsel der statistischen Modelle in geeigneter Weise
berücksichtigt werden müssen (Seite 132, rechte Spalte, siehe „Time Update“ und
„Measurement Update“).


Die Druckschrift D4 befasst sich mit einem IMM („Interacting Multiple Model“)
Algorithmus für eine anpassungsfähige Geschwindigkeitsregelung in einem Fahrerassistenzsystem („ACC System“). Das „ACC System“ eines Fahrzeugs beinhaltet eine Fahrerschnittstelle, einen Radarsensor zur Messung der jeweiligen
Entfernungen und Geschwindigkeiten vorausfahrender Fahrzeuge sowie eine
Steuereinrichtung zur Ansteuerung von Stellgliedern für Ventile und Bremssysteme. Die Möglichkeit, die Bewegung und das Fahrverhalten vorausfahrender
Fahrzeuge in einem Fahrerassistenzsystem genau vorherzusagen, versetzt die
Steuereinrichtung in die Lage, das Fahrverhalten des Fahrzeugs problemlos an
die Bewegung vorausfahrender Fahrzeuge anzupassen (Seite 310, rechte Spalte).


Die Druckschrift geht davon aus, dass das Fahrverhalten von Fahrzeugen durch
die Verwendung mehrerer miteinander wechselwirkender Modelle (IMMs) besser
abgeschätzt bzw. beschrieben werden kann als wenn lediglich ein einziges Modell
zugrunde gelegt wird (Seite 312, rechte Spalte, Abschnitt 2.3. - Two kinamtic
models). Dementsprechend basiert der vorgestellte Algorithmus auch auf der
Verwendung wenigstens zweier kinematischer Modelle, die eine geradlinige und
eine kurvenförmige Bewegung vorausfahrender Fahrzeuge berücksichtigen
(Seite 313, Gleichungen (5) und (11); Seite 313, rechte Spalte, letzter Absatz). Die
zur Lösung der Modelle angewandten Kalmanfilter liefern die charakteristischen
Größen zur Beschreibung eines vorausfahrenden Fahrzeugs, nämlich einen
Schätzwert für den Zustandsvektor des Fahrzeugs (Ort, Geschwindigkeit, Beschleunigung, Kurvenradius usw.), Kovarianz und Modellwahrscheinlichkeit (Sei-

                                       - 17 -



te 314, linke Spalte, siehe „Remark 1“). Der präsentierte IMM Algorithmus beruht
auf miteinander wechselwirkenden Modellen mit bedingten Wahrscheinlichkeiten
für Zustandsgrößen eines Fahrzeugs.


Durch keine dieser Druckschriften ist jedoch unmittelbar nahegelegt, in Hinblick
auf die Erstellung wenigstens zweier statistischer Modelle eines Fahrverhaltens
die Fahrzeuggeschwindigkeit, ein Drehmoment, eine Beschleunigung, eine Straßenneigung, eine Tageszeit, eine Fahrzeugbeladung, eine Insassenanzahl und
eine Fahreridentifikation als Eingabegrößen für die statistischen Modelle zu verwenden, die den Zustand des Hybrid-Fahrzeugs bei einem Zeitschritt k beschreiben sollen.


Nach allem ist nicht erkennbar, wie der Fachmann in Kenntnis lediglich des aus
den ermittelten Druckschriften bekannten Standes der Technik zur Lehre des
Patentanspruches 1 hätte gelangen können.


3.    Die Anmeldung war an das Deutsche Patent- und Markenamt zurückzuverweisen.


Eine unmittelbare Patenterteilung hält der Senat für nicht sachgerecht. Denn das
Amt hat für die Patentansprüche in der Fassung des Hauptantrages bislang nicht
geprüft, ob die Voraussetzungen für die Erteilung eines Patents erfüllt sind.


Insbesondere das Merkmal (a2) des Patentanspruches 1, welches vorsieht,
zugleich die Fahrzeuggeschwindigkeit, ein Drehmoment, eine Beschleunigung,
eine Straßenneigung, eine Tageszeit, eine Fahrzeugbeladung, eine Insassenanzahl und eine Fahreridentifikation in die statistischen Modelle einzugeben, war
nicht Gegenstand des bisherigen Prüfungsverfahrens. Es deutet nichts darauf hin,
dass die bisherige Recherche zum Stand der Technik auch auf eine solche Vielzahl von Zustandsgrößen in den statistischen Modellen ausgerichtet war.

                                       - 18 -



Eine Recherche, die diesem Umstand Rechnung trägt, wird nunmehr nachzuholen
sein.


4.      Die Beschwerdegebühr ist zurückzuzahlen.


In ihren Eingaben ist die Anmelderin auf die Argumentation der Prüfungsstelle in
den vorangegangenen Prüfungsbescheiden eingegangen und hat hilfsweise eine
Anhörung beantragt. Die Anmeldung wurde mit geänderten Patentansprüchen
weiterverfolgt. Nach dem zweiten Prüfungsbescheid erfolgte der Zurückweisungsbeschluss, in welchem die Durchführung einer Anhörung mit der Begründung
abgelehnt wurde, dass der sachliche Gehalt des Patentbegehrens unstrittig sei
und unterschiedliche Sichtweisen somit lediglich bezüglich des Zutreffens der
Ausschlusskriterien des § 1 PatG existierten. Durch die Bescheide der Prüfungsstelle sei der Anmelderin bereits ausreichend rechtliches Gehör gewährt worden,
so dass eine Anhörung aus Gründen der Verfahrensökonomie als nicht sachdienlich angesehen werde.


Wie der Senat in früheren Entscheidungen bereits mehrfach dargelegt hat, war
das Prüfungsverfahren in solchen Fällen regelmäßig mängelbehaftet; es kann
nicht ausgeschlossen werden, dass dieser Mangel ursächlich für die Beschwerdeerhebung war (vgl. etwa 17 W (pat) 74/07, 17 W (pat) 86/07, 17 W (pat) 113/07,
17 W (pat) 76/09, 17 W (pat) 83/10, 17 W (pat) 32/12, 17 W (pat) 43/12).


Es entspricht daher der Billigkeit, die Beschwerdegebühr zurückzuzahlen.




                                         III.


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                            - 19 -



   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
      kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek                     Eder                   Baumgardt                  Dr. Forkel




                                                                                           Fa
