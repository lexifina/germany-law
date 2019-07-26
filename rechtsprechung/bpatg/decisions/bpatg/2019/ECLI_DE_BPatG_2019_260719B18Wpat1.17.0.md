---
ecli: "ECLI:DE:BPatG:2019:260719B18Wpat1.17.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 1/17"
decided: "2019-07-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=33&nr=36400&anz=817&pos=502&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-07-26_18_W-pat_1_17_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 18 W (pat) 1/17 vom 2019-07-26

## Entscheidung

BUNDESPATENTGERICHT


  18 W (pat) 1/17                                                 Verkündet am
_______________                                                   26. Juli 2019
    (Aktenzeichen)                                                     …




                            BESCHLUSS

                          In der Beschwerdesache


              betreffend die Patentanmeldung 10 2007 037 814.0


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. Juli 2019 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, Dipl.-Phys. Dr. Schwengelbeck und
Dr.-Ing. Flaschke




ECLI:DE:BPatG:2019:260719B18Wpat1.17.0

                                       -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der
       Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
       Markenamts vom 18. Oktober 2016 aufgehoben und die Sache
       wird an das Deutsche Patent- und Markenamt zurückverwiesen.




                                   Gründe


                                      I.


1.   Die am 10. August 2007 beim Deutschen Patent- und Markenamt eingereichte Patentanmeldung 10 2007 037 814.0 mit der geltenden Bezeichnung


               „Synchronisieren eines Übersetzungspuffers (TLB)
                    mit einer vergrößerten Paging-Tabelle“,


welche eine US-amerikanische Priorität vom 15. August 2006 (US 11/504,964) in
Anspruch nimmt, wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts mit in der Anhörung vom 18. Oktober 2016 verkündetem
Beschluss zurückgewiesen.


Die Prüfungsstelle hat in ihrem Zurückweisungsbeschluss aufgeführt, dass der
Gegenstand des damals geltenden Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruhe, wobei dies dann damit begründet worden ist, dass der
Gegenstand des Anspruchs 1 nicht so deutlich und vollständig offenbart sei, dass
er für den Fachmann ausführbar sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.

                                      -3-



Im Zurückweisungsbeschluss wurden folgende Druckschriften genannt, ohne darauf weiter Bezug zu nehmen:


     P1: AMD64 Technology, AMD64 Architecture Programmer's Manual, Volume 2: System Programming, Publication No. 24593, Rev. 3.11,
           Dezember 2005, S.172 – 174, S. 464 u. 465
     P2: US 2006 / 0 161 719 A1
     P3: EP 1 681 630 A1
     P4: US 2004 / 0 064 668 A1
     P5: US 2004 / 0 054 518 A1
     P6: US 2006 / 0 026 383 A1
     P7: WO 2006 / 081 582 A2
     P8: US 2004 / 0 117 593 A1.


Als Beleg für die Ausführbarkeit des in der Anmeldung beanspruchten Gegenstands sowie für das Fachwissen des Fachmanns hat die Beschwerdeführerin folgende Anlagen eingereicht:


     A1:     Intel 64 and IA-32 Architectures Software Developer’s Manual, Vol.
             3C: System Programming Guide, Part 3, September 2016


     A2:     MOSBERGER, D., ERANIAN, S.: IA-64 Linux Kernel, Design and Implementation, Prentice Hall, 2001, S.174 - 187


     A3:     BENNETT, S: Next-Generation Intel Virtualization Technologies,
             IVTS005 Intel Developer Forum, 17. April 2007.

                                      -4-



Die Anmelderin beantragt,


     den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patentund Markenamtes vom 18. Oktober 2016 aufzuheben und das Patent auf der
     Grundlage der folgenden Unterlagen zu erteilen:


       − Patentansprüche 1 bis 8, eingereicht in der mündlichen Verhandlung,
       − Beschreibung, Seiten 1 und 3 bis 19, eingegangen am 9. November 2007,
          Seiten 2 und 2a, eingegangen am 4. Juli 2019
       − Figuren 1 bis 5, eingegangen am 9. November 2007.


Der senatsseitig mit einer Gliederung versehene Patentanspruch 1 lautet:


     M1 „Prozessor eines auf Virtualisierung basierenden Systems, der umfasst:

     M2 einen Translation-Lookaside-Puffer, um ein Mapping von einer physikalischen Gastadresse zu einer physikalischen Host-Adresse zu speichern; und

     M3 eine Logikschaltung, um eine Synchronisierung des Mappings von der
          physikalischen Gastadresse zur physikalischen Host-Adresse, die im
          Translation-Lookaside-Puffer gespeichert ist, mit einem entsprechenden Mapping, das in einer erweiterten Paging-Tabelle (EPT) gespeichert ist, durchzuführen,

     M4 wobei das entsprechende Mapping ein in der EPT gespeichertes Mapping mit derselben physikalischen Gastadresse wie das im TLB gespeicherte Mapping aufweist,

     M5 wobei die Synchronisierung auf dem Operanden eines Befehls basiert,
          wobei der Operand einen EPT-Zeiger umfasst, und

                                -5-



M6 wobei eine Abruﬂogik ferner einen ersten Operanden des Befehls, einen zweiten Operanden des Befehls und einen dritten Operanden des
    Befehls empfängt;

    die Logikschaltung ferner

M7 das Mapping auswählt, das zumindest teilweise in der EPT gespeichert
    ist, basierend auf einer Kontextbezeichnung, die aus dem ersten Operanden des Befehls erhalten wird;

M8 die Gastadresse auswählt, zumindest teilweise basierend auf dem
    zweiten Operanden des Befehls; und

M9 einen Ausführungsmodus des Befehls auswählt, basierend auf dem
    dritten Operanden des Befehls; und wobei es sich bei dem Ausführungsmodus des Befehls um einen der folgenden handelt;

M10 ein erster Modus, in welchem nur ein einziges in dem TLB gespeichertes und zu der physikalischen Gastadresse gehörendes Mapping mit
    der entsprechenden Umsetzung in der EPT synchronisiert wird;

M11 ein zweiter Modus, in welchem alle Mappings, die in dem TLB gespeichert sind und zu einem EPT-Kontext gehören, der aus der Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings in der EPT
    synchronisiert werden, wobei die Synchronisation des Mappings ein
    Synchronisieren jener Einträge im TLB in dem EPT-Kontext, der in dem
    EPT-Zeiger spezifiziert ist, mit der erweiterten Paging-Tabelle (EPT)
    umfasst; und

M12 ein dritter Modus, in welchem alle Mappings, die in dem TLB gespeichert sind und zu irgendeinem EPT-Kontext gehören, der aus der Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings in einer EPT synchronisiert werden.“

                                        -6-



Der nebengeordnete Patentanspruch 5 hat folgenden Wortlaut:


            „Verfahren, welches das folgende umfasst:
            in einem auf Virtualisierung basierenden System, welches einen Host
            und einen Gast umfasst,
            Synchronisieren eines Mappings, welches eine Übersetzung einer
            physikalische Gastadresse in eine physikalische Host-Adresse umfasst, die in einem Translation-Lookaside-Puffer (TLB) gespeichert
            ist, mit einem entsprechenden Mapping, das in einer erweiterten Paging-Tabelle (EPT) des auf Virtualisierung basierenden Systems gespeichert ist; und
            Auswählen des in der EPT gespeicherten Mappings, basierend auf
            einem Operanden des Befehls,
            wobei der Operand einen EPT-Zeiger umfasst,
            ferner mit den Schritten:
            Auswählen des Mappings, das in der EPT gespeichert ist, basierend
            auf einer Kontextbezeichnung, die aus einem ersten Operanden des
            Befehls erhalten wird;
            Auswählen der Gastadresse basierend auf einem zweiten Operanden des Befehls; und
            Auswählen eines Ausführungsmodus des Befehls basierend auf einem dritten Operanden des Befehls;
            wobei es sich bei dem Ausführungsmodus des Befehls um einen der
            folgenden handelt:
            ein erster Modus, in welchem nur ein einziges in dem TLB gespeichertes und zu der physikalischen Gastadresse gehörendes Mapping
            mit der entsprechenden Umsetzung in der EPT synchronisiert wird;
            ein zweiter Modus, in welchem alle Mappings, die in dem TLB gespeichert sind und zu dem EPT-Kontext gehören, der aus der Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings in
            der EPT synchronisiert werden, wobei das Synchronisieren des

                                      -7-



             Mappings ein Synchronisieren jener Einträge im TLB in dem EPT-Kontext, der in dem EPT-Zeiger spezifiziert ist, mit der erweiterten
             Paging-Tabelle (EPT) umfasst; und
             ein dritter Modus, in welchem alle Mappings, die in dem TLB gespeichert sind und zu irgendeinem EPT-Kontext gehören, der aus der
             Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings in einer EPT synchronisiert werden.“

Der nebengeordnete Patentanspruch 7 hat folgenden Wortlaut:


             „Auf Virtualisierung basierendes System, welches das folgende umfasst: einen Prozessor gemäß einem der Ansprüche 1 bis 4; und einen Speicher, welcher über einen Bus mit dem Prozessor verknüpft
             ist.“


Zu den Unteransprüchen 2 bis 4, 6 und 8 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht geltend, dass die Patentansprüche zulässig und
die Anspruchsgegenstände neu und erfinderisch seien. Zudem seien die jeweiligen Gegenstände der Ansprüche in der Anmeldung so deutlich und vollständig
offenbart, dass sie für den Fachmann ausführbar seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                     II.


Die zulässige Beschwerde führt zur Aufhebung des angefochtenen Beschlusses
und zur Zurückverweisung der Sache an das Deutsche Patent- und Markenamt
gemäß § 79 Abs. 3 Satz 1 Nr. 1 und Nr. 3 PatG.

                                        -8-



1.   Die Anmeldung betrifft einen Prozessor eines auf Virtualisierung basierenden
Systems sowie ein entsprechendes Verfahren und das entsprechende System.
Gemäß Beschreibungseinleitung ermöglicht die Virtualisierung einer einzelnen
Host-Maschine eine Abstraktion des Host-Rechners, so dass die zugrunde liegende Hardware der Host-Maschine als eine oder mehrere unabhängig voneinander operierende virtuelle Maschinen erscheint. Die Virtualisierung werde angewandt, um zu ermöglichen, dass mehrere Gastbetriebssysteme koexistieren und
scheinbar gleichzeitig auf mehreren virtuellen Maschinen ausgeführt werden können. Virtualisierungssysteme könnten einen Monitor der virtuellen Maschine, den
sogenannten VMM, aufweisen. Der VMM könne die Komponenten einer realen
Host-Maschine in die virtuelle Maschine umsetzen und virtuelle Komponenten erzeugen, welche in Software emuliert seien. Der VMM könne der Gastsoftware eine
Schnittstelle einer unbestückten virtuellen Maschine bereitstellen. Dabei sei bekannt, dass eine Seitentabelle (page table) eingesetzt werde, um in einem prozessorbasierten System für ein Mapping bzw. eine Umsetzung von einem linearen
Speicher in einen realen Speicher zu sorgen. Bei Seitentabellen handele es sich
im Allgemeinen um speicherresidente Strukturen. Daher verursache der Zugriff auf
eine Seitentabelle einen Speicherzugriff, wodurch sich die Verarbeitungszeit in
einem virtualisierten System verlängere. Um diese Probleme zu verringern, könne
ein Prozessor einen Hochgeschwindigkeitsspeicher umfassen, welcher als Translation Lookaside Buffer (TLB) bezeichnet werde, in welchem aktuelle Umsetzungen zwischengespeichert würden. Dies ermögliche einem Prozessor, schneller auf
eine Übersetzung einer linearen Adresse in die entsprechende reale Adresse zuzugreifen. Um den TLB zu verwalten, würden Befehle bereitgestellt, um z. B. dessen Einträge zu löschen oder zu aktualisieren (vgl. deutsche Übersetzung der
Anmeldeunterlagen, S. 1, Z. 13 - S. 2, Z. 33).


Eine Aufgabe ist in den Anmeldeunterlagen nicht ausgeführt. Das objektive technische Problem liegt darin, ein auf Virtualisierung basierendes System, einen Prozessor sowie ein Verfahren bereitzustellen, bei welchem die Speicherverwaltung

                                             -9-



in einer virtualisierten Umgebung vereinfacht und beschleunigt werde (vgl. Schriftsatz v. 4. Juli 2019, S. 3, dritter Abs.).


Zur Lösung der Aufgabe sind ein Prozessor eines auf Virtualisierung basierenden
Systems gemäß Anspruch 1, ein Verfahren gemäß Anspruch 5 sowie das auf Virtualisierung basierende System gemäß Anspruch 7 vorgesehen.


2.   Als maßgeblichen Fachmann sieht der Senat einen Ingenieur oder Master
für Informationstechnik mit beruflicher Erfahrung auf dem Gebiet der hardwaregestützten Virtualisierung an.


Der so definierte Fachmann legt dem Anspruchsgegenstand des Patentanspruchs 1 das folgende Verständnis zugrunde:


Anspruch 1 betrifft einen Prozessor eines auf Virtualisierung basierenden Systems
(Merkmal M1). Der Prozessor soll einen Pufferspeicher TLB 323 (Translation-Lookaside-Buffer) umfassen, in welchem Umsetzungen von Seitentabellen zwischengespeichert werden können (vgl. Fig. 3 i. V. m. der geltenden Beschreibung,
S. 2, zweiter Abs. u. S. 11, Z 6 - 11).

                                     - 10 -




Konkret sieht der Anspruch 1 vor, dass der Pufferspeicher bzw. TLB ein Mapping
von einer physikalischen Gastadresse zu einer physikalischen Host-Adresse speichert (vgl. Merkmal M2). Dabei handelt es sich bei der physikalischen Gastadresse um die Speicheradresse einer virtuellen Maschine (vgl. geltende Beschreibung, S. 5, erster u. zweiter Abs.). Somit wird mittels des TLBs ein hardwarebasierter Zugriff auf Umsetzungen von virtuellen Adressen zu realen Adressen ermöglicht.

Außerdem soll der Prozessor eine Logikschaltung umfassen, um eine Synchronisierung des Mappings, das im TLB gespeichert ist, mit einem Mapping, das zumindest teilweise in einer erweiterten Seitentabelle (Extended Paging-Table, EPT)
gespeichert ist, durchzuführen (Merkmal M3). Dies bedeutet für den Fachmann
nichts anderes, als dass das im TLB gespeicherte Mapping abgeglichen bzw. ak-

                                         - 11 -



tualisiert werden soll. Unter der erweiterten Seitentabelle EPT ist eine Seitentabelle oder eine Funktion zu verstehen, die bei der Übersetzung zwischen den
Gast- und Host-Adressen eingesetzt wird. Sie enthält hierzu die erforderliche Abbildungsinformation. Für jede der virtuellen Maschinen kann eine separate EPT-Tabelle vorgesehen sein (vgl. geltende Beschreibung, S. 9, erster u. zweiter Abs.).
Der Wortlaut des Anspruchs 1 lässt offen, wo die EPT-Tabellen gespeichert sind.
Beispielsweise können die EPT-Tabellen 328 im Arbeitsspeicher 320 abgelegt
sein (vgl. Fig. 3). Alternativ können sich die Tabellen aber auch direkt im Prozessor 318 befinden (vgl. geltende Beschreibung, S. 9, Z. 10 - 13). Gemäß Merkmal
M4 weist das entsprechende Mapping ein in der EPT gespeichertes Mapping mit
derselben Gastadresse wie das im TLB gespeicherte Mapping auf.


Die Merkmale M5 bis M14 befassen sich mit der Synchronisierung des Mappings.

Merkmal M5 sieht allgemein vor, dass die Synchronisierung auf dem Operanden
eines Befehls basiert, wobei der Operand einen EPT-Zeiger umfasst. Bei dem
EPT-Zeiger handelt es sich um ein Register, welches auf die aktuell aktive EPT-Tabelle verweist (vgl. geltende Beschreibung, S. 13, Z. 28-31).

Bei dem Befehl kann es sich beispielsweise um den Befehl „INVL_EPT“ handeln,
welcher dem Befehlssatz des Prozessors hinzugefügt ist (vgl. geltende Beschreibung, S. 13, Z. 19-28).

Gemäß Merkmal M6 wird konkretisiert, dass der Befehl drei Operanden aufweist,
die von einer Abruflogik abgerufen werden (vgl. geltende Beschreibung, Brückenabs. S. 13/14, S. 15 Z. 9 - 21 u. Fig. 5).



Aus dem ersten Operanden des Befehls wird die Kontextbezeichnung erhalten,
anhand der die Logikschaltung das Mapping auswählt (vgl. Merkmal M7). Die
Kontextbezeichnung definiert dabei einen Abschnitt des Adressraums, für welchen
der Befehl auszuführen ist (vgl. geltende Beschreibung, S. 13 Z. 28).

                                        - 12 -



Der zweite Operand spezifiziert den EPT-Zeiger (vgl. geltende Beschreibung,
S. 13, Z. 32, bis S. 14, Z. 2). Darauf basierend wählt die Logikschaltung die Gastadresse aus (Merkmal M8).

Basierend auf dem dritten Operanden wählt die Logikschaltung einen von drei
möglichen Modi aus, in welchem der Befehl auszuführen ist (vgl. Merkmal M9).


         •   Erster Modus: In diesem Modus soll nur ein einziges, in dem TLB
             gespeichertes und zu der physikalischen Gastadresse gehörendes
             Mapping mit der entsprechenden Umsetzung in der EPT synchronisiert
             werden (vgl. geltende Beschreibung, S. 14, Z. 13 - 16, S. 15
             Abs. 1/Merkmal M10).
         •   Zweiter Modus: In diesem Modus werden alle Mappings, die in dem
             TLB gespeichert sind und zu einem EPT-Kontext gehören, der aus der
             Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings
             in der EPT synchronisiert. Dabei soll die Synchronisation des Mappings
             ein Synchronisieren jener Einträge im TLB in dem EPT-Kontext, der in
             dem EPT-Zeiger spezifiziert ist, mit der erweiterten Paging-Tabelle
             (EPT) umfassen (vgl. (vgl. geltende Beschreibung, S. 14, Z. 18 - 21,
             S. 15 Z. 25 - 32/Merkmal M11).
         •   Dritter Modus: In diesem Modus werden alle Mappings, die in dem TLB
             gespeichert sind und zu irgendeinem EPT-Kontext gehören, der aus der
             Kontextbezeichnung erhalten wird, mit den entsprechenden Mappings
             in einer EPT synchronisiert (vgl. geltende Beschreibung, S. 14, Z. 23 -
             25, S. 15 Z. 23 - 25/ Merkmal M12).


Somit kann basierend auf den Operanden des Befehls das Ausmaß der Synchronisierung spezifiziert werden. Unter anderem können selektiv Einträge im TLB
synchronisiert werden (vgl. geltende Beschreibung, S. 13, Z. 19 - 31 u. S. 14, Z. 9
- 25).

                                      - 13 -



3.   Die Patentansprüche 1 bis 8 sowie die Anpassung der Beschreibung sind
zulässig (§ 38 PatG).


Die Merkmale des Anspruchs 1 sind durch die ursprünglichen Patentansprüche 1,
2, 8, 11 und 12 in Verbindung mit der ursprünglichen Beschreibung als zur Erfindung zugehörend offenbart (vgl. deutsche Übersetzung der Anmeldeunterlagen,
S. 13, Z. 9, bis S. 14, Z. 8).


Die nebengeordneten Ansprüche 5 und 7 gehen auf die ursprünglich eingereichten Ansprüchen 14 und 24 zurück und wurden an den nun geltenden Patentanspruch 1 entsprechend angepasst.


Die Ansprüche 2 bis 4, 6 und 8 basieren auf den ursprünglichen Ansprüchen 3, 4,
10, 20 und 34 unter Anpassung der Nummerierung und der Rückbezüge.


In der Beschreibung wurde der im Prüfungsverfahren ermittelte Stand der Technik
gewürdigt.


4.   Der geltende Anspruch 1 genügt den Anforderungen des § 34 Abs. 4 PatG.


Die Prüfungsstelle hat ihren Beschluss inhaltlich damit gegründet, dass der Gegenstand des damals geltenden Anspruchs 1 in der Anmeldung nicht so deutlich
und vollständig offenbart sei, dass er für den Fachmann ausführbar wäre. Im Einzelnen wurde angegeben, dass der TLB gemäß der Beschreibung mehrere Abbildungstypen speichern könne. Daher sei es für den Fachmann in der Anmeldung
nicht so deutlich und vollständig offenbart, wie zu einer an sich mehrdeutigen Adresse der zutreffende Abbildungstyp bestimmt werden solle und die anderen Abbildungstypen im TLB maskiert werden sollen (vgl. Abschnitt II. auf S. 2, Brückenabsatz zu Seite 3 des Zurückweisungsbeschlusses der Prüfungsstelle).

                                      - 14 -



Diese Begründung trägt nicht.


Das von der Prüfungsstelle konstruierte Problem einer vermeintlichen Mehrdeutigkeit von Gastadressen stellt sich für den Fachmann gar nicht, denn dies war nicht
Gegenstand des damals geltenden Anspruchs 1. Zwar ist der Prüfungsstelle zuzustimmen, dass der damals geltende Anspruch 1 und auch die übrigen Unterlagen offen lassen, wie der zutreffende Abbildungstyp, also das Mapping von einer
physikalischen Gastadresse zu einer physikalischen Host-Adresse konkret bestimmt wird, und wie die anderen Abbildungstypen, also z. B. das Mapping von der
linearen Gastadresse auf eine physikalische Gastadresse im TLB maskiert werden. Dies führt aber nicht zu einer mangelnden Ausführbarkeit oder Nacharbeitbarkeit, sondern zu einem entsprechend breit gefassten Anspruch. Ein breit gefasster Anspruch ist für sich kein Grund zur Beanstandung (Schulte, 10. Aufl., § 34
PatG, Rdn. 141). Vielmehr ist im Interesse der Rechtssuchenden der Gehalt der
Erfindung mit möglichst weitreichend zu formulierenden Patentansprüchen zu
schützen (vgl. BGH PatAnwZ 1/12, Urteil vom 29. November 2013, Abschnitt II b,
bb Abs. 2 Satz 2/Rdn 19). Ein solcher breit gefasster Anspruch muss dann für jeden seiner umfassten Gegenstände die Voraussetzungen für eine Patentierung
erfüllen, d. h. er muss u. a. neu und erfinderisch sein (Schulte, 10. Aufl., § 34
PatG, Rdn. 142). Soweit die Prüfungsstelle in der Begründung des Zurückweisungsbeschlusses eine fehlende erfinderische Tätigkeit (§ 48 i. V. m. § 4 PatG)
mit einer mangelnden Ausführbarkeit (§ 48 i. V. m. § 34 Abs. 4 PatG) verbindet, ist
dies nicht nachvollziehbar (vgl. Zurückweisungsbeschluss, Abschnitt II, erster
Satz, und a. a. O.).


5.   Der Gegenstand des Anspruchs 1 erweist sich gegenüber dem Stand der
Technik nach den bislang im Verfahren vorliegenden Druckschriften als neu und
beruht gegenüber diesem auch auf einer erfinderischen Tätigkeit (§§ 3, 4 PatG).


a)   Der Gegenstand des Patentanspruchs 1 ist neu gegenüber dem im Verfahren befindlichen Stand der Technik (§ 3 PatG).

                                       - 15 -



Druckschrift P1 befasst sich mit der AMD64-Architektur für x86-Prozessoren. Insbesondere wird ein Prozessor eines auf Virtualisierung basierenden Systems beschrieben (vgl. erster Abs. des Abschnitts 5.5, S. 172 i. V. m. S. 173 Abs. 5;
Merkmal M1). Der Prozessor umfasst einen Translation-Lookaside-Puffer (TLB),
um ein Mapping von einer linearen zu einer physikalischen Adresse, d. h. einer
physikalischen Gastadresse (virtuelle Adresse im Gastadressraum) zu einer physikalischen Host-Adresse zu speichern (vgl. Abschnitt 5.5, S. 172 ff. i. V. m. erstem u. zweitem Abs. des Abschnitts 15.15, S. 464 u. S. 465, Abschnitt 15.15.2;
Merkmal M2). Der Fachmann liest mit, dass der Prozessor eine Logikschaltung
umfasst, um eine Synchronisierung des Mappings von der physikalischen Gastadresse zur physikalischen Host-Adresse, die im Translation-Lookaside-Puffer
gespeichert ist, mit einem entsprechenden Mapping durchzuführen. Dabei ist mit
dem sogenannten „Nested Paging“ eine zusätzliche Übersetzungsschicht vorgesehen, wobei jeder virtuellen Maschine ein eigenes virtualisiertes CR3-Register,
das die physikalische Gastadresse speichert, zur Verfügung gestellt wird. Für jede
Gastadresse sieht der Virtual Machine Monitor (VMM) eine „host page table“ vor,
um die physikalische Gastadresse in eine physikalische Hostadresse umzusetzen
(vgl. erster u. zweiter Abs. des Abschnitts 15.15, S. 464 i. V. m. S. 465, Abschnitt 15.15.2). Die „host page tables“ sind damit als erweiterte Seitentabellen zu
verstehen. Die Speicherverwaltung des TLBs basiert auf dem Befehl „INVLPGA“,
welcher einem VMM erlaubt, selektiv Einträge im TLB zu löschen. Die punktuelle
Invalidierung erfolgt hierbei über den Adress Space ID (ASID), mit der der VMM
die Möglichkeit hat, einzelne ASID-Felder im TLB zu löschen (vgl. Abschnitt 15.15.2). Das Löschen von Einträgen versteht der Fachmann als Teil einer
Synchronisation (Merkmal M3). Der Fachmann geht dabei davon aus, dass das in
der „host page table“ gespeicherte Mapping dieselbe Gastadresse wie das im TLB
gespeicherte Mapping aufweist (Merkmal M4). Der Befehl „INVLPGA“ umfasst
auch den Operanden „rAX“, welcher als EPT-Zeiger zu verstehen ist (vgl. Abschnitt 15.15.2; Merkmal M5).

Damit bietet der in Druckschrift P1 angegebene Befehl die Möglichkeit, einzelne
ASID-Felder im TLB selektiv zu löschen. Druckschrift P1 offenbart aber keine

                                      - 16 -



Synchronisierung des Mappings von einer physikalischen Gastadresse zu einer
physikalischen Host-Adresse, bei der das Ausmaß der Synchronisierung konkret
auf drei Operanden des Befehls gemäß den Merkmalen M6 bis M9 basiert. Insbesondere lassen sich der Druckschrift P1 die drei möglichen Ausführungsmodi gemäß den Merkmalen M10 bis M12 nicht entnehmen.

Druckschrift P2 befasst sich mit dem Betreiben von virtuellen Maschinen unter
Verwendung von erweiterten Paging-Tabellen. Hierzu wird ein Prozessor eines auf
Virtualisierung basierenden Systems beschrieben (vgl. Fig. 3 i. V. m. Abs. 0022 u.
0023; Merkmal M1). Der Prozessor umfasst eine Logikschaltung und einen Speicher 320 mit einer erweiterten Paging-Tabelle (EPT), in dem zumindest teilweise
ein Mapping von der physikalischen Gastadresse zur physikalischen Host-Adresse
gespeichert ist (vgl. Fig. 3 u. 5 i. V. m. Abs. 0043; teilweise Merkmal M3, ohne
Synchronisation mit dem TLB). In Figur 6 wird in Verbindung mit den Absätzen 0046 und 0052 eine Umsetzung einer physikalischen Gastadresse in eine
physikalische Hostadresse unter Verwendung eines EPT-Zeigers 620 beschrieben.

                                      - 17 -




Im Unterschied zum Gegenstand nach vorliegendem Anspruch 1 umfasst der in
Druckschrift P2 beschriebene Prozessor keinen TLB (vgl. Fig. 3). Demnach wird
auch keine Synchronisation des Mappings, welches im TLB gespeichert ist, beschrieben (Merkmale M2 und M4 bis M12 fehlen, Merkmal M3 fehlt teilweise).

Bei Druckschrift P3 handelt es sich um ein Familienmitglied zu Druckschrift P2.
Dabei geht Druckschrift P3 nicht über Druckschrift P2 hinaus, insbesondere was
den nicht offenbarten TLB und die Synchronisation des Mappings betrifft.


Druckschrift P4 beschreibt einen Prozessor mit einem „monitor“ als Virtualisierungsfunktion, welcher zwischen der Hardwareschicht eines Computersystems
und einem oder mehreren Gastbetriebssystemen angeordnet ist (vgl. Abs. 0003,
0006, 0038, 0066; Merkmal M1). Der als Hypervisor bzw. VMM zu verstehende
Monitor verwaltet das Mapping von einer physikalischen Gastadresse zu einer

                                        - 18 -



physikalischen Hostadresse für jedes Gastbetriebssystem (vgl. Abs 0066). Der
Prozessor umfasst auch einen TLB, um ein Mapping von einer physikalischen
Gastadresse zu einer physikalischen Host-Adresse zu speichern (vgl. Abs. 0038,
0046, 0047 u. insb. 0074 u. 0075; Merkmal M2). Des Weiteren umfasst der Prozessor eine Logikschaltung (integrated circuits, hardware, Abs. 0004, 0049), um
das Mapping von der physikalischen Gastadresse zur physikalischen Host-Adresse, die im TLB gespeichert ist, zu aktualisieren. Dies erfolgt mithilfe einer „virtual hash page table (VHPT)“, die der Fachmann als eine erweiterte Paging-Tabelle ansieht (vgl. Abs. 0049). Dies ist als eine Synchronisierung des Mappings,
das im TLB gespeichert ist, mit einem entsprechenden Mapping, das teilweise in
einer erweiterten Seitentabelle gespeichert ist, zu verstehen (Merkmal M3). Dabei
weist das entsprechende Mapping ein in der VHPT gespeichertes Mapping mit
derselben Gastadresse wie das im TLB gespeicherte Mapping auf (vgl. Abs. 0054;
Merkmal M4).

Druckschrift P4 offenbart aber keine Synchronisierung, die auf dem Operanden
eines Befehls basiert, wobei der Operand einen EPT-Zeiger umfasst (Merkmal M5
fehlt). Es wird auch keine Logikschaltung beschrieben, welche basierend auf drei
Operanden eines Befehls gemäß den Merkmalen M6 bis M9 und mit drei möglichen Ausführungsmodi gemäß den Merkmalen M10 bis M12 die Synchronisierung
entsprechend durchführt.


Druckschrift P5 beschreibt die Emulation und Virtualisierung in einem Multiprozessorsystem. Eine Synchronisierung des Mappings von einer physikalischen Gastadresse zur physikalischen Hostadresse gemäß den Merkmalen M3 bis M12 wird
nicht beschrieben.


Druckschrift P6 beschreibt einen Prozessor eines auf Virtualisierung basierenden
Systems (vgl. Abs. 0025, 0027; Merkmal M1). Dabei wird ein Virtual Machine Monitor (VVM) eingesetzt (vgl. Abs. 0002, 0007, 0026). Der Prozessor umfasst einen
TLB, um ein Mapping von einer physikalischen Gastadresse zu einer physikalischen Host-Adresse zu speichern (vgl. Abs. 0007, 0044, 0046; Merkmal M2). Der

                                        - 19 -



Prozessor umfasst auch eine Logikschaltung (Abs. 0025, 0046), um das Mapping
von der physikalischen Gastadresse zur physikalischen Host-Adresse, die im TLB
gespeichert ist, zu aktualisieren (vgl. Abs. 0046: the translation can be moved from
the VHPT to he TLB). Die Synchronisierung erfolgt mithilfe einer „virtual hash page
table (VHPT)“, die der Fachmann als eine erweiterte Paging-Tabelle ansieht (vgl.
Abs. 0035, 0044, 0046). Dies ist als eine Synchronisierung des Mappings, das im
TLB gespeichert ist, mit einem entsprechenden Mapping, das in einer erweiterten
Seitentabelle gespeichert ist, zu verstehen (Merkmal M3). Das entsprechende
Mapping weist dabei ein in der VHPT gespeichertes Mapping mit derselben Gastadresse wie das im TLB gespeicherte Mapping auf (vgl. Abs. 0040, 0046; Merkmal M4). Die Synchronisierung basiert auf dem Operanden eines Befehls, wobei
der Operand entsprechend Merkmal M5 einen EPT-Zeiger (instruction pointer 338) umfasst, (vgl. Abs. 0029 u. Fig. 3A).

Druckschrift P6 offenbart jedoch ebenfalls keine Synchronisierung des Mappings
von einer physikalischen Gastadresse zu einer physikalischen Host-Adresse, bei
der das Ausmaß der Synchronisierung auf drei Operanden des Befehls gemäß
den Merkmalen M6 bis M9 basiert. Auch gibt es in der Druckschrift keinen Hinweis
auf die Merkmale M10 bis M12, welche sich auf drei Ausführungsmodi beziehen.


Die Druckschriften P7 und P8 beschreiben jeweils einen Virtual Machine Monitor
(VMM), welcher auf eine emulierte und virtualisierte Hardware zugreift. Die Übersetzung von den virtuellen Adressen des Gastsystems über die physikalischen
Adressen des Gastsystems, die den virtuellen Adressen des VMM entsprechen, in
die physikalischen Adressen des Hosts erfolgt dabei mittels Seitentabellen einer
sogenannten Shadow-/Schattenstruktur. Hierzu wird ein virtueller TLB verwendet,
der die Funktionalität des physischen TLB des Prozessors emuliert. Die Synchronisierung eines Mappings von der physikalischen Gastadresse zu einer physikalischen Hostadresse entsprechend den Merkmalen M3 bis M12 ist beiden Druckschriften nicht zu entnehmen.

                                       - 20 -



Der von der Anmelderin als Beleg für das Fachwissen des Fachmanns eingereichte Auszug aus dem Fachbuch gemäß Anlage A2 befasst sich im Kapitel 4 mit
der Speichervirtualisierung von 64-Bit-Prozessoren (vgl. Kap. 4.4, erster Satz;
Merkmal M1). Dabei wird auf den Seiten 174 bis 187 die Verwaltung eines
Translation Lookaside Buffer beschrieben, um ein Mapping von einer virtuellen
Adresse zu einer physikalischen Adresse zu speichern (teilweise Merkmal M2,
ohne Mapping von einer physikalischen Gastadresse zu einer physikalischen
Host-Adresse). Die Übersetzung einer virtuellen Adresse läuft dabei in folgenden
Schritten ab: im TLB wird nach einem passenden Eintrag gesucht. Ist der Eintrag
nicht vorhanden, so durchsucht der Prozessor die VHTP (Virtual Hash Page
Table) und aktualisiert den TLB. Die VHTP ist als eine erweiterte Paging-Tabelle
zu verstehen, wobei das im TLB gespeicherte Mapping basierend auf dem in der
VHTP gespeicherten Mapping aktualisiert bzw. synchronisiert wird (vgl. S. 175,
letzter Absatz i. V. m. S. 176, drittem Absatz: A final challenge in using a TLB is
hour to keep it sychronized … with the underlying page table; teilweise entsprechend den Merkmalen M3 und M4, ohne Mapping von einer physikalischen
Gastadresse zu einer physikalischen Host-Adresse). Die Synchronisierung basiert
dabei auf dem Operanden eines Befehls, wobei der Operand einen EPT-Zeiger
umfasst (vgl. S. 176, zweiter Absatz, S. 82 le. Abs.; Merkmal M5).
Die Druckschrift offenbart zwar verschiedene Modi der Befehlausführung, um selektiv Mappings im TLB zu synchronisieren (vgl. Kap. 4.4.2 S. 82 ff).


Anlage A2 befasst sich allerdings nicht mit der Adressierung virtueller Maschinen,
bei der eine physikalische Gastadresse zu einer physikalischen Host-Adresse umgesetzt wird (Merkmale M2, M3 und M4 fehlen teilweise). Dementsprechend wird
auch keine Synchronisation des Mappings von einer physikalischen Gastadresse
zu einer physikalischen Host-Adresse beschrieben (Merkmale M6 bis M12 fehlen).


Die von der Anmelderin als Beleg für die Ausführbarkeit des in der Anmeldung
beanspruchten Gegenstands eingereichten Anlagen A1 und A3 sind nachveröf-

                                      - 21 -



fentlicht und daher bei der Beurteilung der Neuheit bzw. erfinderischen Tätigkeit
nicht zu berücksichtigen.


Somit offenbart keine der im Verfahren befindlichen Druckschriften zum Stand der
Technik ein Verfahren mit sämtlichen Merkmalen des Gegenstands des Patentanspruchs 1.


b)   Der Gegenstand des Patentanspruchs 1 ist dem Fachmann durch den im
Verfahren befindlichen Stand der Technik auch nicht nahegelegt.


Wie vorstehend ausgeführt, offenbaren weder die Druckschriften P1 bis P8 noch
das Fachbuch gemäß Anlage A2 alle Merkmale des Patentanspruchs 1. Insbesondere die Synchronisierung des Mappings von einer physikalischen Gastadresse zu einer physikalischen Host-Adresse basierend auf drei Operanden des
Befehls gemäß den Merkmalen M6 bis M9 und mit drei möglichen Ausführungsmodi gemäß den Merkmalen M10 bis M12 ist in den genannten Druckschriften
nicht beschrieben und auch nicht entnehmbar.


Der Fachmann erhält weder aus einer beliebigen Zusammenschau des im Verfahren befindlichen Stands der Technik noch aus seinem Fachwissen eine Anregung
oder Veranlassung, beim Synchronisieren des Mappings von einer physikalischen
Gastadresse zu einer physikalischen Host-Adresse einen Prozessor mit einer Logikschaltung einzusetzen, die durch die Merkmale M6 bis M12 gekennzeichnet ist.


Somit beruht der Gegenstand des Anspruchs 1 im Lichte des im Verfahren befindlichen Stands der Technik auch auf einer erfinderischen Tätigkeit.


6.   Auch die Gegenstände der nebengeordneten Patentansprüche 5 und 7
erweisen sich gegenüber den im Verfahren genannten Druckschriften ebenfalls als
patentfähig.

                                       - 22 -



Das Verfahren gemäß Anspruch 5 sowie das auf Virtualisierung basierende System gemäß Anspruch 7 weisen jeweils Merkmale auf, die den Merkmalen M1 bis
M12 des auf einen Prozessor gerichteten Anspruchs 1 inhaltlich entsprechen. Die
vorstehenden Ausführungen zu Anspruch 1 gelten damit ebenso für die nebengeordneten Ansprüche 5 und 7. Damit sind die Gegenstände der nebengeordneten
Ansprüche nicht anders zu bewerten als der patentfähige Gegenstand gemäß Anspruch 1.
Dies gilt in gleicher Weise für die abhängigen Ansprüche 2 bis 4, 6 und 8, die über
das Selbstverständliche hinausgehende Ausgestaltungen des Gegenstands des
Anspruchs 1 betreffen.


7.     Der Senat hat jedoch nach § 79 Abs. 3 Satz 1 PatG davon abgesehen, in der
Sache selbst zu entscheiden und ein Patent zu erteilen.


Eine Zurückverweisung kommt insbesondere dann in Betracht, wenn die Gründe,
die der angefochtenen Entscheidung zugrunde liegen, nicht mehr bestehen (§ 79
Abs. 3 Satz 1 Nummer 1 PatG), aber eine neue Sachprüfung erforderlich ist, weil
die Patentfähigkeit noch nicht oder nicht ausreichend Gegenstand der Prüfung war
(§ 79 Abs. 3 Satz 1 Nummer 1 und 3 PatG, vgl. Engels in Busse/Keukenschrijver,
PatG, 8. Auflage, § 79 Rdn. 79, Schulte/Püschel, PatG, 10. Auflage, § 79 Rdn. 19,
20).


Dies ist vorliegend der Fall, da die Prüfungsstelle, soweit aus der Akte ersichtlich,
zu den in den nun geltenden Anspruch 1 aus dem ursprünglichen Unteranspruch 11 aufgenommenen zusätzlichen Merkmalen nicht Stellung genommen
hat.


Der Senat kann nicht ausschließen, dass weiterer Stand der Technik existiert, der
alleine oder in Verbindung mit dem bereits im Verfahren befindlichen Stand der
Technik einer Patenterteilung im beantragten Umfang entgegenstehen könnte.

                                        - 23 -



Da eine sachgerechte Entscheidung nur aufgrund einer vollständigen Recherche
des relevanten Standes der Technik ergehen kann, war die Sache – auch um der
Anmelderin keine Tatsacheninstanz zu nehmen – zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückzuverweisen.




                                       III.


                       Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     1.   das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2.   bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung
          des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
     3.   einem Beteiligten das rechtliche Gehör versagt war,
     4.   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
          stillschweigend zugestimmt hat,
     5.   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist,
          bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt
          worden sind, oder
     6.   der Beschluss nicht mit Gründen versehen ist.

                                    - 24 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn         Kruppa            Dr. Schwengelbeck             Dr. Flaschke


                                                                        Fi/prö
