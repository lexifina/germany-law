---
ecli: "ECLI:DE:BPatG:2019:060219B18Wpat26.16.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 26/16"
decided: "2019-02-06"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=5&nr=34227&anz=817&pos=83&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-02-06_18_W-pat_26_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 18 W (pat) 26/16 vom 2019-02-06

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 26/16                                                    Verkündet am
_______________                                                     6. Februar 2019
    (Aktenzeichen)                                                         …




                             BESCHLUSS

                           In der Beschwerdesache




              betreffend die Patentanmeldung 10 2013 104 329.1


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 6. Februar 2019 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie den Richter Kruppa, die Richterin Dipl.-Phys. Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater




ECLI:DE:BPatG:2019:060219B18Wpat26.16.0

                                       -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 4. Oktober 2016 aufgehoben und die Sache wird an das
       Deutsche Patent- und Markenamt zurückverwiesen.


                                    Gründe


                                        I.


Die von der Anmelderin am 29. April 2013 unter Inanspruchnahme einer Priorität
vom 21. August 2012 (US 13/590 484) beim Deutschen Patent- und Markenamt
eingereichte Patentanmeldung 10 2013 104 329.1 mit der Bezeichnung


                 „Aufgabenzuteilung in großen und kleinen Kernen“


wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
Markenamts mit Beschluss vom 4. Oktober 2016 zurückgewiesen. Zur Begründung hat die Prüfungsstelle ausgeführt, dass der Gegenstand des jeweiligen Anspruchs 1 gemäß damaligem Hauptantrag und gemäß den damaligen Hilfsanträgen 1 bis 5 nicht auf einer erfinderischen Tätigkeit gegenüber dem Stand der
Technik gemäß der im Prüfungsverfahren als P1 bezeichneten Druckschrift


       D1: Craeynest, K. u. a., Scheduling Heterogeneous Multi-Cores
               through   Performance   Impact    Estimation   (PIE),   ISCA   ’12
               Proceedings of the 39th Annual International Symposium on
               Computer Architecture, Portland, OR, USA, 2012, 9. - 13. Juni,
               Seiten 213 bis 224


i. V. m. dem präsenten fachmännischen Grundwissen beruhen würde.

                                             -3-



Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Mit Anlage zur Ladung vom 26. November 2018 hat der Senat zur Vorbereitung
auf die mündliche Verhandlung auf folgende Druckschriften als Stand der Technik
hingewiesen:


       D2: US 2009/0089470 A1
       D3: US 2007/0245164 A1.


Die Beschwerdeführerin beantragt,


       den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 4. Oktober 2016 aufzuheben
       und das Patent auf der Grundlage der folgenden Unterlagen zu
       erteilten:


       -       Patentansprüche 1 bis 11, eingereicht in der mündlichen Verhandlung,
       -       Beschreibung Seiten 1, 1a, 2, 3, 6, 7, 10 bis 19, eingereicht
               in der mündlichen Verhandlung, Seiten 4, 5, 8, 9, 20 bis 23,
               eingegangen am 26. Juli 2013,
       -       Figuren 1   bis    4,   5A,   5B    und   6,   eingegangen   am
               26. Juli 2013.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 lautet:


       M1           „Verfahren, umfassend:

       M2         -   Ermitteln eines Interrupts an einem Informationsverarbeitungsgerät, das zwei oder mehr Kerne von unterschiedlicher Größe
                      aufweist;

                             -4-



M3   -   Bestimmen, ob das Interrupt an einen größeren Kern oder auf
         einen kleineren Kern gerichtet werden soll, basierend auf einer
         Strategie zum Zuteilen von Interrupts;

M4   -   Richten des Interrupts an den kleinen Kern, wenn der Interrupt
         sich nicht als Ausnahme herausstellt, basierend auf der Strategie zum Zuteilen von Interrupts, um die Verwendung kleinerer Kerne zu maximieren, wodurch ermöglicht wird, größere
         Kerne so oft wie möglich abzuschalten; und

M5   -   Verarbeiten des Interrupts auf einem geeigneten Kern gemäß
         der Strategie zum Zuteilen von Interrupts;

M6   -   wobei ein prädiktives Lernen verwendet wird, um zu bestimmen, welche Interrupts am besten in jedem Kern verarbeitet
         werden können, wobei das Lernen umfasst:

M7   -   dass neue Interrupts, welche bisher noch nicht verarbeitet
         wurden, in größeren Kernen verarbeitet werden um eine akzeptable Leistungsfähigkeit zu sichern; und

M8   -   Verfolgen eines oder mehrerer Parameter während der Verarbeitung eines neuen Interrupts auf dem größeren Kern sowie
         Berücksichtigen eines oder mehrerer Kennzeichen des neuen
         Interrupts und Bestimmen der Strategie zum Zuteilen von Interrupts sowie Zuordnen einer Kernsignatur zu dem neuen
         Interrupt, welche beim erneuten Verarbeiten des neuen Interrupts herangezogen werden, um zu bestimmen, ob das Interrupt auf einen größeren Kern oder einen kleineren Kern gerichtet werden soll.“

                                         -5-



Der geltende Patentanspruch 11 lautet:


          „Informationsverarbeitungsgerät, umfassend:
          -   einen oder mehrere Prozessoren; und
          -   einen Speicher in Kommunikation mit einem oder mehreren Prozessoren;
          -   wobei der Speicher Programminstruktionen speichert, die,
              wenn sie von einem oder mehreren Prozessoren durchgeführt werden, ein Verfahren nach einem der Ansprüche 1 bis 10 ausführen.“


Wegen der geltenden abhängigen Ansprüche 2 bis 10 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht hierzu geltend, dass die geänderte Anspruchsfassung zulässig sei und die Gegenstände der Ansprüche neu und erfinderisch seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.


                                         II.


Die zulässige Beschwerde führt zur Aufhebung des angefochtenen Beschlusses
und zur Zurückverweisung der Sache an das Deutsche Patent- und Markenamt
gemäß § 79 Abs. 3 Satz 1 Nr. 1 und Nr. 3 PatG.


1.     Die Patentanmeldung betrifft Mehrkernprozessoren mit Chips, die Kerne
unterschiedlicher Größe zur Verfügung stellen. Gemäß der Beschreibungseinleitung sei es ein Ziel solcher Mehrkern-Chips, die Leistungsfähigkeit eines größeren
Kerns mit der Energieeffizienz eines kleineren Kerns zu verbinden (vgl. geltende
Beschreibung, S. 1).

                                        -6-



Die Anmeldung erläutert, konventionelle Mehrkernprozessoren wiesen für jeden
Kern die gleiche Leistungsfähigkeit, Frequenz und Leistung auf. Das Betriebssystem teile Aufgaben jedem Kern gleichmäßig zu und wende ein ähnliches Leistungsmanagement auf jeden Kern an. Mit der Entwicklung von Chips, die Mehrfachkerne von unterschiedlichem Niveau der Leistungsfähigkeit auf einem gemeinsamen Bauteil aufwiesen, also Kerne unterschiedlicher Größe, könnten die
Kerne unterschiedlich verwendet werden. Da die kleineren Kerne eine geringere
Leistung aufnehmen würden, aber auch eine geringere Leistungsfähigkeit aufwiesen, werde die Batterielebensdauer ansteigen, je mehr kleinere Kerne verwendet
werden könnten, wenn das System größere Kerne abschalten könne. Falls diese
größeren Kerne nicht benutzt würden, werde die Batterie geschont. Jedoch könnten die Leistungsfähigkeit und selbst die Leistungseinsparungen vermindert werden, wenn die kleineren Kerne nicht geeignet eingesetzt würden (vgl. geltende
Beschreibung, S. 6, zw. Abs.).


Demgemäß besteht die der Erfindung zugrunde liegende Aufgabe darin, ein verbessertes Verfahren zum Zuteilen von Interrupts zu größeren oder kleineren Kernen anzugeben, mit welchem die Verwendung kleinerer Kerne maximiert werden
kann, so dass es ermöglicht wird, größere Kerne so oft wie möglich abzuschalten
(vgl. geltende Beschreibung, S. 1a, vorl. Abs.).


Der für die Lösung der Aufgabe zuständige Fachmann besitzt ein abgeschlossenes Studium der Informationstechnik und weist Erfahrung in der Entwicklung von
Mehrkernprozessoren und der zugehörigen Software zur Ansteuerung auf.


Die Aufgabe soll gelöst werden durch ein Verfahren gemäß Anspruch 1 und ein
Informationsverarbeitungsgerät gemäß Anspruch 11.


2.   Einige der in den unabhängigen Ansprüchen aufgeführten Merkmale bedürfen der Auslegung.

                                        -7-



Unter die Formulierung eines Informationsverarbeitungsgeräts, das zwei oder
mehr Kerne unterschiedlicher Größe aufweist (vgl. Merkmal M2), fällt sowohl ein
Mehrkernprozessor, also ein Prozessor, der mehrere Kerne aufweist, als auch ein
Informationsverarbeitungsgerät, das mehrere Prozessoren, welche jeweils einen
Kern (oder auch mehrere Kerne) aufweist (vgl. Figur 1: „Chipsatz 110“,
„Kern(e) 120“, „Prozessor(en) 122 z. B. Einzel- oder Mehrkern“).


Anspruch 1 wie auch Anspruch 11 geben für die in Merkmal M4 aufgeführte Ausnahme keinerlei Spezifizierung, d. h. der Begriff einer Ausnahme definiert lediglich,
dass alle Interrupts, die sich nicht als eine – wie auch immer definierte – Ausnahme erweisen, an den kleinen Kern gerichtet werden, wobei dies basierend auf
der Zuteilungsstrategie erfolgen soll (vgl. Merkmal M4). Diese Auslegung, die von
der in der Computertechnik sonst üblicherweisen Verwendung des Begriffs einer
Ausnahme (exception) abweicht, steht in Einklang mit den Unteransprüchen 7, 8
und 9, welche unterschiedliche Definitionen des Begriffs einer Ausnahme vornehmen.


Die Strategie zum Zuteilen von Interrupts ist in Anspruch 1 so definiert, dass nur
Interrupts, welche keine Ausnahme darstellen, an den kleinen Kern gerichtet werden, und dass gemäß der Zuteilungsstrategie des Interrupt auf einem geeigneten
Kern verarbeitet wird (Merkmal M5). Die Merkmale M6 bis M8 benennen die Verfahrensschritte, mit denen in einem Lernvorgang für jeden Interrupt eine sogenannte Kernsignatur festgelegt wird, und die Strategie zum Zuteilen der Interrupts
auf den größeren Kern oder den kleineren Kern bestimmt wird. Der Begriff einer
Kernsignatur ist dabei so zu verstehen, dass Interrupts mit einer kleinen Kernsignatur auf einen kleinen Kern gerichtet werden und Interrupts mit einer großen
Kernsignatur auf einen großen Kern gerichtet werden (vgl. geltende Beschreibung,
S. 11, Z. 25 - S. 12, Z. 2). Dazu sollen beim Lernvorgang „neue“ Interrupts, also
alle Arten von Interrupts, welche bisher noch nicht verarbeitet wurden, in den größeren Kernen verarbeitet werden; während dieser Interrupt-Verarbeitung soll anhand der Verfolgung von Parametern und Kennzeichen bestimmt werden, ob die-

                                       -8-



ser Typ von Interrupt bei späterer Bearbeitung besser auf einen kleineren oder
einen größeren Kern gerichtet werden soll (Merkmal M8, vgl. geltende Beschreibung, S. 11, dr. Abs.). Als Parameter und Kennzeichen, die bei dieser Bestimmungsroutine herangezogen werden, nennt die Beschreibung beispielhaft einen
Leistungsfähigkeitsparameter, die Zeitdauer, die zur Erledigung der Aufgabe von
dem größeren Kern benötigt wird, die Priorität der Aufgabe oder auch in welchem
Modus des Systems, etwa im Tiefschlafmodus, die Aufgabe durchzuführen ist (vgl.
geltende Beschreibung, S. 11, zw. Abs.). Die Angabe, dass hierbei ein „prädiktives“ Lernen verwendet wird, bedeutet nichts anderes, als dass nach Durchlaufen
der in den Merkmalen M6 bis M8 festgelegten Verfahrensschritte eine Kernsignatur für jeden Interrupt mit einer Strategie zum Zuteilen vorliegt, welche in dem
weiteren Verfahren und bei einem erneuten Verarbeiten eines solchen Interrupts
gemäß den Merkmalen M3, M4 und M5 zum Einsatz kommt.


3.   Die Patentansprüche und die geänderte Beschreibung sind zulässig.


Die Merkmale der geltenden Ansprüche sind durch die ursprünglichen Patentansprüche sowie die ursprünglich eingereichte Beschreibung mit den Figuren 1 bis 6
als zur Erfindung gehörig offenbart:


Patentanspruch 1 basiert auf dem ursprünglichen Anspruch 1 i. V. m. den Figuren 3 und 4 sowie den Anmeldeunterlagen Seite 6, Absatz 3, Seite 10, Zeile 23 bis
Seite 12, Zeile 2 und Seite 19, Zeilen 18 bis 26. Patentanspruch 11 basiert auf
dem ursprünglichen Patentanspruch 11 i. V. m. den vorstehend angegebenen Offenbarungsstellen. Die Unteransprüche 2 bis 10 entsprechen inhaltlich den ursprünglichen Unteransprüchen 2 bis 10.


Die Beschreibung wurde in zulässiger Weise an die geltenden Ansprüche angepasst, und der relevante Stand der Technik wurde in der Beschreibungseinleitung
gewürdigt sowie eine Aufgabe formuliert. In den geltenden Ansprüchen und der
geltenden Beschreibung wurden außerdem einzelne Begriffe gemäß den eng-

                                           -9-



lischsprachigen Anmeldeunterlagen an technisch übliche Ausdrücke angepasst
und redaktionelle Änderungen vorgenommen.


4.    Der im bisherigen Prüfungsverfahren und der im Beschwerdeverfahren genannte Stand der Technik steht dem Patentanspruch 1 nicht patenthindernd entgegen, da er dem Fachmann keine Anregung gibt, ein Verfahren mit sämtlichen in
Anspruch 1 aufgeführten Merkmalen auszugestalten.


a)    Der Gegenstand des Anspruchs 1 ist neu gegenüber dem im Verfahren
befindlichen Stand der Technik.


Die im Prüfungsverfahren abgehandelte Druckschrift D1 befasst sich nicht mit
einer Strategie zum Zuteilen von Interrupts, sondern mit der Ablaufkoordination
von Instruktionen oder Tasks in einem Informationsverarbeitungsgerät mit mehreren Kernen unterschiedlicher Größe (vgl. Titel, Abstract: scheduling heterogeneous multi-cores, Abschnitt 4: instructions). Die Druckschrift gibt keinen expliziten
Hinweis darauf, die beschriebenen Zuteilungsstrategien gezielt für die Verarbeitung von Interrupts zu verwenden; auch Angaben zu einem prädiktiven Lernvorgang zur Erstellung einer Kernsignatur und einer Zuteilungsstrategie für neu zu
verarbeitende Interrupts, wie in den Merkmalen M6 bis M8 definiert, gibt die
Druckschrift nicht.


Die im Beschwerdeverfahren eingeführte Druckschrift D2 (US 2009/0089470 A1)
betrifft das Abgleichen (balancing) von Interrupts in einem Mehrkern-Prozessor
(multi-core processor, vgl. Titel, Abs. 0014). Beschrieben werden verschiedene
Strategien zum Zuteilen von Interrupts (vgl. Abs. 0032 - 0035: interrupt handling,
distribution of interrupts). An einem Informationsverarbeitungsgerät (processing
element), das zwei oder mehr Kerne von unterschiedlicher Größe aufweist, werden   Interrupts   ermittelt   (vgl.   Abs. 0011, 0014:   multi-core   processor 100,
Abs. 0015: asymmetric cores; Abs. 0025: any number of processing elements,
Abs. 0029: asymmetric processor with different processing elements, Fig. 3:

                                       - 10 -



Block 305 determine amount of interrupt activity / Merkmale M1, M2). Dabei werden als Informationsverarbeitungsgeräte sowohl Threads, Prozesse, Kontext, logische Prozessoren oder auch Kerne angesehen (vgl. Abs. 0011) und physikalische
Prozessoren mit zwei oder mehreren Kernen behandelt (vgl. Abs. 0012, 0014,
0025). Für die Interrupts wird basierend auf einer Strategie zum Zuteilen bestimmt,
an welchen der mehreren Prozessoren und damit an welchen der Kerne, welche
asymmetrisch sein können, sie gerichtet werden sollen (Merkmal M3). In weniger
aktiven Zeitintervallen der Interrupt-Behandlung werden die Interrupts vorrangig an
einen Prozessor gegeben, wie den Boot-Prozessor (vgl. Abs. 0036). Dieser kann
aufgrund des zu erzielenden Energiesparmodus (power save mode) in Druckschrift D2 als ein Prozessor mit einem kleineren Kern angesehen werden. Die anderen Zeitintervalle sind im Sinne des Anspruchsmerkmals M4 als Ausnahme
anzusehen, so dass das Merkmal M4 durch diese Art der Zuteilung als erfüllt zu
betrachten ist. Mit der Zuweisung des Interrupts an einen solchen Boot-Prozessor
ist das Interrupt gemäß der Verteilstrategie zwangsläufig auch von diesem als geeignet anzusehenden Kern zu verarbeiten (vgl. Abs. 0036 / Merkmal M5). Druckschrift D2 beschreibt verschiedene Strategien zur Verteilung der Interrupts, etwa
anhand einer Statistik zur Häufigkeit oder anhand der Kategorie des Interrupts
(vgl. Abs. 0031, 0033). Offenbart sind damit aber lediglich Verteilstrategien anhand vordefinierter Schemata oder anhand von Werten, die ein Benutzer festlegt.
Angaben zu einem prädiktiven Lernvorgang für Interrupts, welche erstmals an
dem Verarbeitungsgerät auftreten, macht Druckschrift D2 nicht (Merkmale M6 bis
M8 fehlen).


Die im Beschwerdeverfahren eingeführte Druckschrift D3 beschreibt, dass in einem sogenannten Schlafmodus (sleeping state) die Interrupt-Prozesse an eine
kleinere CPU (sub-CPU) mit geringerer Leistungsaufnahme gerichtet werden und
für den Fall, dass der Schlafmodus nicht aktiv ist, sondern ein Betriebsmodus
(operating state), die Interrupts an eine größere CPU (main CPU) gerichtet werden
(vgl. Fig. 1, 2 u. 5: Schritte S22 u. S32 bzw. Schritte S22 u. S27, Abs. 0009 - 0012
/ Merkmale M1, M2, M3). Bei der Verarbeitung im Betriebsmodus stellen die Inter-

                                      - 11 -



rupts dabei eine Ausnahme im Sinne von Merkmal M4 dar. Beschrieben werden
weitere verschiedene Strategien zum Zuteilen der Interrupts an die verschiedenen
Kerne (main CPU, sub-CPU) des Informationsverarbeitungsgeräts, etwa dass anhand der Häufigkeit des Ereignisses oder anhand der erforderlichen Verarbeitungsleistung eine Auswahl der zuständigen CPU erfolgt (vgl. Abs. 0038, 0166,
0184 / Merkmal M5). Einen Hinweis darauf, neue Interrupts vom größeren Kern
verarbeiten zu lassen und während der Verarbeitung Parameter und Kennzeichen
zum Erstellen einer Kernsignatur zu verwenden, um somit eine prädiktive Strategie zum Zuteilen von Interrupts zu erstellen, ist Druckschrift D3 jedoch nicht zu
entnehmen (Merkmale M6 bis M8 fehlen).


Somit offenbart keine der im Verfahren befindlichen Schriften ein Verfahren mit
sämtlichen Merkmalen des Gegenstands des Patentanspruchs 1.


b)   Der Gegenstand des Anspruchs 1 ist dem Fachmann durch den im Verfahren befindlichen Stand der Technik auch nicht nahegelegt.


Keine der im Verfahren befindlichen Druckschriften offenbart eine Strategie zum
Zuteilen von Interrupts, bei der prädiktives Lernen verwendet wird, wie im vorigen
Abschnitt zur Neuheit ausgeführt. Die Druckschriften geben dem Fachmann auch
keinen Hinweis, während der Verarbeitung von neuen Interrupts Parameter oder
Kennzeichen zu verfolgen, um den verschiedenen Kernen jeweils eine Kernsignatur zuordnen zu können, anhand der später eine Zuweisung der Interrupts erfolgen
kann. Für den Fachmann ist ein Verfahren gemäß Anspruch 1 daher auch aus
einer beliebigen Zusammenschau der Druckschriften D1 bis D3 heraus nicht nahegelegt.


Auch das allgemeine Fachwissen gibt dem Fachmann keine Anregungen, bei der
Zuteilung von Interrupts an die verschiedenen Kerne eines Mehrkernprozessors
eine prädiktive Lernstrategie für erstmalig auftretende Interrupts einzusetzen, bei

                                      - 12 -



der Verarbeitungsparameter und Kennzeichen des Interrupts zum Erstellen einer
Kernsignatur herangezogen werden, wie in den Merkmalen M6 bis M8 definiert.


Durch den bisher ermittelten Stand der Technik ist das Verfahren des Anspruchs 1
dem Fachmann – auch unter Einbeziehung seines Fachwissens – daher nicht nahegelegt.


Damit trägt der im Zurückweisungsbeschluss genannte Grund nicht mehr.


c)   Die Ausführungen zu Anspruch 1 gelten ebenso für den nebengeordneten
Anspruch 11, der auf ein Informationsverarbeitungsgerät mit einem oder mehreren
Prozessoren und Speicher gerichtet ist, der zur Ausführung eines Verfahrens gemäß Anspruch 1 geeignete Programminstruktionen speichert. Auch der Gegenstand von Anspruch 11 ist dem Fachmann durch den im Verfahren befindlichen
Stand der Technik nicht nahegelegt.


5.   Die Sache war gemäß § 79 Abs. 3 Satz 1 Nr. 1 und Nr. 3 PatG an das Deutsche Patent- und Markenamt zurückzuverweisen, da zu den geltenden Ansprüchen bislang keine Sachentscheidung des Deutschen Patent- und Markenamts
erfolgt ist und neue Tatsachen vorliegen.


In den geltenden Patentanspruch 1 wurden gegenüber dem ursprünglichen Anspruch 1 und gegenüber dem jeweiligen Anspruch 1 nach den im Prüfungsverfahren geltenden Hilfsanträgen 1 bis 5 unter anderem die Merkmale M6 und M8
neu aufgenommen, welche der Beschreibung entstammen. Die Amtsakte weist als
einzigen Bescheid einen Zusatz zur Ladung vom 10. August 2016 zur Anhörung
auf sowie die Niederschrift über die Anhörung vom 4. Oktober 2016. Soweit aus
der Amtsakte ersichtlich, sind die neu aufgenommenen Merkmale M6 und M8,
welche die Verfahrensschritte zum prädiktiven Lernen betreffen, nicht Gegenstand
der Recherche im bisherigen Prüfungsverfahren gewesen.

                                       - 13 -



Das nunmehr vorliegende Patentbegehren genügt den formalen Anforderungen
der §§ 34 und 38 PatG und erfüllt damit die Voraussetzungen für die Prüfung der
Patentfähigkeit gemäß §§ 1 bis 5 PatG.


Aus dem im Verfahren befindlichen Stand der Technik sind das nunmehr unter
Aufnahme von bislang ungeprüften Merkmalen aus der Beschreibung beanspruchte Verfahren nach Anspruch 1 sowie die Vorrichtung nach Anspruch 11
– wie vorstehend unter Abschnitt II. 4 dargelegt – dem Fachmann nicht nahegelegt. Der Senat hat davon abgesehen, in der Sache selbst zu entscheiden und
das Patent zu erteilen, weil er die Frage, ob der jeweilige Gegenstand der unabhängigen Ansprüche auch auf einer erfinderischen Tätigkeit beruht, anhand des
derzeit ermittelten Standes der Technik nicht abschließend beurteilen kann. Es
kann daher nicht ausgeschlossen werden, dass insbesondere unter dem Gesichtspunkt der §§ 3 und 4 PatG ein einer Patenterteilung möglicherweise entgegenstehender Stand der Technik existiert. Zu dessen Ermittlung sind in erster
Linie die Prüfungsstellen des Patentamts berufen, welche hierzu über geeignete
Recherchemittel und Fachkenntnisse verfügen. Da eine sachgerechte Entscheidung nur aufgrund einer vollständigen Recherche des relevanten Standes der
Technik ergehen kann, war die Sache – auch um der Anmelderin keine Tatsacheninstanz zu nehmen – zur weiteren Prüfung und Entscheidung an das
Deutsche Patent- und Markenamt zurückzuverweisen.




                                         III.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                       - 14 -



     1.    das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2.    bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung
           des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
     3.    einem Beteiligten das rechtliche Gehör versagt war,
     4.    ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
           stillschweigend zugestimmt hat,
     5.    der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist,
           bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt
           worden sind, oder
     6.    der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn              Kruppa           Dr. Otten-Dünnweber                 Altvater


                                                                                 Fi
