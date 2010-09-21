---
ecli: "ECLI:DE:BPatG:2010:210910B17Wpat55.06.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 55/06"
decided: "2010-09-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2010&Sort=1&Seite=65&nr=17430&anz=1397&pos=982&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2010-09-21_17_W-pat_55_06_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 55/06 vom 2010-09-21

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 55/06                                                 Verkündet am
_______________                                                21. September 2010
    (Aktenzeichen)                                                      …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2005 001 025.3-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 21. September 2010 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch, der Richterin Eder, des Richters
Dipl.-Ing. Baumgardt und der Richterin Dipl.-Ing. Wickborn




BPatG 154
08.05

                                     -2-



beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 11. Januar 2006 aufgehoben und die Sache zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückverwiesen.




                                  Gründe


                                      I.


Die vorliegende Patentanmeldung wurde am 7. Januar 2005 beim Deutschen
Patent- und Markenamt eingereicht unter der Bezeichnung


     „Multithread-Prozessor mit Kontext-Umschaltung ohne Einschränkungen
      und/oder Zyklenverlust und Verfahren zum Betreiben eines solchen“.


Sie wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts vom 11. Januar 2006 „aus den Gründen des Bescheides
vom 12. Oktober 2005“ zurückgewiesen, nachdem die Anmelderin einen Antrag
auf Entscheidung nach Lage der Akten gestellt hatte. Im genannten Bescheid war
ausgeführt worden, dass der Patentanspruch 1 keine klare Lehre erkennen lasse;
soweit interpretierbar, lasse er gegenüber der in der Anmeldung selbstgenannten
Druckschrift

                                       -3-



       D1     Ungerer, Theo et al.: A Survey of Processors With Explicit
              Multithreading. In: ACM Computing Surveys, Vol. 35, No. 1,
              März 2003, S. 29 - 63


auch keine erfinderische Tätigkeit erkennen.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie stellt
den Antrag,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 und 25, überreicht in der mündlichen Verhandlung, noch anzupassende Patentansprüche 2 - 21, 23 - 24 vom
       Anmeldetag,


       noch anzupassende Beschreibung Seiten 1 - 25 und 2 Seiten
       Bezugszeichenliste vom Anmeldetag,


       4 Blatt Zeichnungen mit 4 Figuren vom 10. Februar 2005, eingegangen am 11. Februar 2005.


In der mündlichen Verhandlung hat sie vorgetragen, dass die Lehre der nunmehrigen Patentansprüche 1 und 25 in der Anmeldung so deutlich und vollständig
offenbart sei, dass ein Fachmann sie ausführen könne; auch sei verständlich
angegeben, was hier als patentfähig unter Schutz gestellt werden solle. Schließlich sei die jetzt beanspruchte Lehre durch den vorliegenden Stand der Technik
nicht vorweggenommen und auch nicht nahegelegt. Damit bestünden die von der
Prüfungsstelle beanstandeten Mängel nicht mehr.

                                        -4-



Der geltende Patentanspruch 1 und der Nebenanspruch 25 lauten (mit einer
redaktionellen Korrektur im Anspruch 1):


       „1.    Multithread-Prozessor (1) mit einer Kontext-Umschaltung
              ohne Zyklenverluste zur Datenverarbeitung einer Mehrzahl
              von Threads, wobei für jeden Thread innerhalb des Multithread-Prozessors (1) ein eigener Kontext (DC, DI, DE) vorgesehen ist, mit:


              einer Umschalt-Tabelle (2), welche


                 – eine interne Ausnahme (IA) eines bestimmten Kontext
                 (DC, DI, DE) zum Aktualisieren dieses Kontext (DC, DI, DE)
                 und zum Umschalten von diesem Kontext (DC, DI, DE)
                 auf einen Zielkontext (DI, DE) der internen Ausnahme (IA)


              und


                 – eine externe Ausnahme (EA) eines bestimmten Kontext (DC, DI, DE) zum Aktualisieren dieses Kontext (DC,
                 DI, DE) und zum Umschalten von dem diesem Kontext
                 (DC, DI, DE) auf einen Zielkontext (DI, DE) der externen
                 Ausnahme (EA)


              empfängt und abhängig davon


              einen Kontextparametersatz (KPS(DC), KPS(DI), KPS(DE))
              dieses Kontext (DC, DI, DE) und/oder einen Kontextparametersatz (KPS(DI)) eines Zielkontext (DI, DE) der internen
              Ausnahme (IA)       und/oder    einen   Kontextparametersatz

                               -5-



      (KPS(DE)) eines Zielkontext (DI, DE) der externen Ausnahme (EA) aktualisiert und


      einen Umschaltparametersatz (UPS) für eine Ablaufsteuerung (7) der zu holenden Programmbefehle (PB) setzt,


      wobei die Ablaufsteuerung (7) für jeden Kontext (DC, DI, DE)
      des Multithread-Prozessors (1), der nicht dem aktuellen
      Kontextflag (Dn) entspricht, den entsprechenden Kontextparametersatz (KPS(notDC)) jeweils aktualisiert und die aktualisierten Kontextparametersätze (KPS(notDC)) in die Programmadresstabelle (3) schreibt.


25.   Verfahren zum Betreiben eines Multithread-Prozessors (1)
      mit einer Kontext-Umschaltung ohne Zyklenverlust zur
      Datenverarbeitung von Threads, wobei für jeden Thread
      innerhalb des Multithread-Prozessors (1) ein eigener Kontext (DC, DI, DE) vorgesehen ist, mit folgenden Verfahrensschritten:


      (a)   Empfangen einer internen Ausnahme (IA) eines bestimmten Kontext (DC, DI, DE) zum Aktualisieren dieses Kontext (DC, DI, DE) und Umschalten von diesem
            Kontext (DC, DI, DE) auf einen Zielkontext (DI, DE) der
            internen Ausnahme (IA)


            und einer externen Ausnahme (EA) eines bestimmten
            Kontext (DC, DI, DE) zum Aktualisieren dieses Kontext
            (DC, DI, DE) und Umschalten von diesem Kontext (DC,
            DI, DE) auf einen Zielkontext (DI, DE) der externen
            Ausnahme (EA); und

                                       -6-



                    abhängig von einer Umschalttabelle (2)


              (b)   Aktualisieren   eines    Kontextparametersatzes (KPS
                    (DC)) des aktuellen Kontext (DC) und/oder eines Kontextparametersatzes (KPS (DI, DE)) eines Zielkontext (DI) der internen Ausnahme (IA) und/oder eines
                    Kontextparametersatzes (KPS (DE)) der externen Ausnahme (EA) und


              (c)   Setzen eines Umschaltparametersatzes (UPS) für
                    eine Ablaufsteuerung (7) der zu holenden Programmbefehle (PB),


                    wobei die Ablaufsteuerung (7) für jeden Kontext (DC,
                    DI, DE) des Multithread-Prozessors (1), der nicht dem
                    aktuellen Kontextflag (Dn) entspricht, den entsprechenden Kontextparametersatz (KPS(notDC)) jeweils
                    aktualisiert und die aktualisierten Kontextparametersätze (KPS (notDC)) in die Programmadresstabelle (3)
                    schreibt.“


Bezüglich der übrigen Unterlagen wird auf die Akte verwiesen.


Als zugrundeliegende Aufgabe hat die Anmelderin in der mündlichen Verhandlung sinngemäß angegeben, durch den Gegenstand ihrer Anmeldung solle für
einen Multithread-Prozessor mit einer Kontext-Umschaltung ohne Zyklenverlust
beim Vorliegen von internen und externen Exceptions das Umschalten, d. h. die
Übergangsfolge zwischen den Threads optimiert werden.

                                       -7-



                                       II.


Die zulässige Beschwerde führt zur Aufhebung des angefochtenen Beschlusses
und zur Zurückverweisung der Sache an das Deutsche Patent- und Markenamt
gemäß § 79 Abs. 3 Satz 1 Nr. 1 PatG.


1.    Die vorliegende Patentanmeldung betrifft einen Multithread-Prozessor, der
von seiner Hardware her so ausgelegt ist, dass er zwischen verschiedenen
Threads innerhalb eines Taktzyklusses, d. h. ohne Zyklenverlust umschalten kann.


Dazu sind bestimmte Register, Zähler und Statusbits mehrfach vorhanden und
jeweils einem Thread zugeordnet (vgl. Absatz [0044] der Offenlegungsschrift: „wobei für jeden Thread innerhalb des Multithread-Prozessors 1 ein eigener Kontext
vorgesehen ist“). Unter „Thread-Kontext“ ist ein temporärer Prozessorzustand zu
verstehen, definiert insbesondere durch Programmzählregister und Statusregister,
der bei einem Thread-Wechsel für den alten Thread gespeichert und für den
neuen Thread wiederhergestellt werden muss (siehe Absatz [0002], zweite Hälfte).
Durch das Vorhandensein von eigenen Registern und Zählerspeichern für jeden
Thread („Kontextspeicher“) wird ein schneller Wechsel der Arbeitsumgebung von
einem Thread zu einem anderen ermöglicht.


Die Anmelderin hat in der mündlichen Verhandlung erläutert, dass ein solchermaßen ausgerüsteter Multithread-Prozessor zwar bereits vorbekannt gewesen sei.
Die Umschaltung zwischen verschiedenen Threads werde aber dann problematisch, wenn unterschiedliche Anforderungen zeitlich nahe beieinander vorlägen.
Vor allem beim nahezu gleichzeitigen Aufeinandertreffen von internen und externen Exceptions (siehe Absatz [0045], [0067] und Figur 3) sei eine Abarbeitungsreihenfolge sicherzustellen, die schnell genug bestimmt werden könnte (so dass
keine zusätzlichen Taktzyklen allein für die Bestimmung erforderlich würden) und
eine sachgerechte Priorisierung ermöglichte. Hierfür schlage die Anmeldung im
Besonderen die Verwendung einer Umschalttabelle vor, welche die Auswahl der

                                        -8-



erforderlichen Kontext-Parametersätze und des Umschaltparametersatzes (vgl.
Figur 2) schnell steuern und außerdem relativ einfach erzeugt werden könne, weil
sich die verschiedenen Ablaufoptionen darin übersichtlich widerspiegelten. Eine
derartige Umschalttabelle ermögliche, über die reine Bestimmung der aktuell erforderlichen Parametersätze hinaus, auch noch die Aktualisierung weiterer Kontext-Parametersätze, welche von einer aktuellen Umschaltung indirekt betroffen seien
(vgl. dazu Absatz [0064], Absatz [0086] / [0087]; Absatz [0077] „wobei der Kontextparametersatz des zweiten Kontext DE derart vorbereitet wird…“, Abs. [0079]
„dass bei ersterem es nicht erlaubt ist, den Kontextparametersatz des zweiten
Kontext                                       a.).


Als Fachmann, der mit der Aufgabe betraut wird, die internen Abläufe in einem
Multithread-Prozessor zu optimieren, ist hier ein Entwicklungsingenieur für Mikroprozessoren mit Hochschulabschluss und längerer Berufserfahrung anzusehen.


2.    Die geltenden Patentansprüche 1 und 25 sind zulässig.


Patentanspruch 1 ergibt sich aus dem ursprünglichen Anspruch 22 und dessen
Rückbezug auf den ursprünglichen Anspruch 1, wobei einige Klarstellungen vorgenommen wurden. Insbesondere wird nun deutlich, dass die Formulierung „mit
einer Kontext-Umschaltung ohne Zyklenverluste“ die Art des Multithread-Prozessors definiert, auf den sich die beanspruchte Lehre richtet.


Patentanspruch 25 basiert auf dem ursprünglichen Anspruch 25, ist jetzt aber
deutlicher an den geltenden Patentanspruch 1 angelehnt und bezieht auch das
zusätzliche Merkmal aus Anspruch 22 mit ein.


3.    Der Zurückweisungsbeschluss war damit begründet worden, dass der
damalige Patentanspruch 1 keine klare Lehre erkennen lasse. Ein solcher Mangel
liegt jedenfalls in der geltenden Anspruchsfassung nicht (mehr) vor.

                                        -9-



„Keine klare Lehre“ ist, für sich allein betrachtet, kein gesetzlicher Zurückweisungsgrund, sondern vermischt zwei Anforderungen des Patentgesetzes:


3.1   Einerseits ist „die Erfindung … in der Anmeldung so deutlich und vollständig
zu offenbaren, dass ein Fachmann sie ausführen kann“ (§ 34 Absatz 4 PatG).
Dazu sind die Anmeldeunterlagen vom jeweiligen Durchschnittsfachmann „aus
sich selbst heraus und insbesondere nach dem mit der offenbarten technischen
Lehre verfolgten Zweck auszulegen“ und bilden insoweit gewissermaßen ihr eigenes Lexikon (vgl. BGH Mitt. 2002, 176 – Gegensprechanlage).


Nachdem von der Prüfungsstelle beanstandete Begriffe (wie z. B. „ohne Zyklenverlust“, „Aktualisieren eines Kontext“ u. a.) in der Beschreibung hinreichend erläutert sind, kann der Senat einen Mangel hinsichtlich vollständiger Offenbarung oder
Ausführbarkeit nicht erkennen.


3.2   Darüber hinaus verlangt § 34 Absatz 3 Satz 3 PatG, dass die Anmeldung
Patentansprüche enthalten muss, anhand derer identifiziert werden kann, was als
patentfähig unter Schutz gestellt sein soll. Im Erteilungsverfahren ist für Patentansprüche zu sorgen, die die unter Schutz gestellte Erfindung klar und deutlich
umschreiben (BGH GRUR 1988, 757 – Düngerstreuer) und geeignet sind, den
Anmeldungsgegenstand eindeutig zu kennzeichnen und vom Stand der Technik
abzugrenzen (BGH GRUR 1979, 461 – Farbbildröhre). Der Schutzbereich muss,
ggf. unter Auslegung mittels der Beschreibung, so klar und eindeutig definiert sein,
dass er „für Außenstehende hinreichend sicher vorhersehbar ist“ (BGH BlPMZ 90,
240 – Batteriekastenschnur).


Diese Anforderungen sieht der Senat ebenfalls als erfüllt an, insbesondere da die
geltende Fassung der Patentansprüche 1 und 25 nunmehr deutlich macht, dass
durch die Formulierung „mit einer Kontext-Umschaltung ohne Zyklenverluste“ einschränkend die Art des Multithread-Prozessors beschrieben ist, und dass die

                                       - 10 -



beanspruche Umschalttabelle für das Auftreten einer internen und einer externen
Ausnahme vorgesehen ist.


4.    Der Gegenstand der geltenden Patentansprüche 1 und 25 ist durch die in
der Anmeldung bereits zitierte, von der Prüfungsstelle aufgegriffene Druckschrift:


        D1   Ungerer, Theo et al.: A Survey of Processors With Explicit
             Multithreading. In: ACM Computing Surveys, Vol. 35, No. 1,
             März 2003, S. 29 - 63


nicht neuheitsschädlich vorbekannt und auch nicht ohne weiteres nahegelegt.


Zwar beschreibt D1 verschiedene Konzepte und Realisierungsarten von Multithreading, unter anderem auch Multithread-Prozessoren mit einer Kontext-Umschaltung ohne Zyklenverluste (siehe z. B. Seite 43 rechte Spalte unten: „zerocycle overhead context switching“, oder Seite 45 rechte Spalte unten: „The processor may switch context every cycle“). Eine solche Kontext-Umschaltung wird
auch für nebeneinander zu bearbeitende synchrone Ausnahmen und asynchrone
Ereignisse beschrieben, siehe Seite 37 rechte Spalte Absatz 1 letzter Satz.


Ferner ist aus Seite 43 rechte Spalte Absatz 2 die Verwendung von FPGAs zur
Steuerung der Thread-Umschaltung bekannt, was für den Fachmann vergleichbar
zur Nutzung einer Umschalttabelle ist. Dass dabei jeweils nicht nur die umzuschaltenden Kontexte aktualisiert würden (sondern auch noch weitere Kontext-Parametersätze, welche (nur) indirekt betroffen sind), lässt sich D1 aber nicht entnehmen.


5.    Weil der den geltenden Patentansprüchen 1 und 25 zugrundeliegende
ursprüngliche Anspruch 22 bisher nicht Gegenstand des Prüfungsverfahrens vor
dem Deutschen Patent- und Markenamt war, erscheint eine weitere Sachaufklärung notwendig.

                                  - 11 -



Die Anmeldung war daher, auch um der Anmelderin keine Tatsacheninstanz zu
nehmen, zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und
Markenamt zurückzuverweisen.




Dr. Fritsch           Eder                 Baumgardt            Wickborn




                                                                      Fa
