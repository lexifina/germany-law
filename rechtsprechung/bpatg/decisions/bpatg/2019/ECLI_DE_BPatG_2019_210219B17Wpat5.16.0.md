---
ecli: "ECLI:DE:BPatG:2019:210219B17Wpat5.16.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 5/16"
decided: "2019-02-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=8&nr=34846&anz=817&pos=123&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-02-21_17_W-pat_5_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 5/16 vom 2019-02-21

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 5/16                                                  Verkündet am
_______________                                                   21. Februar 2019
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 10 2011 007 434.1


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 21. Februar 2019 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterinnen Eder und
Dipl.-Phys. Dr. Thum-Rung sowie des Richters Dipl.-Phys. Dr. Forkel


beschlossen:


                     Die Beschwerde wird zurückgewiesen.




ECLI:DE:BPatG:2019:210219B17Wpat5.16.0

                                      -2-



                                   Gründe


                                       I.


Die vorliegende Patentanmeldung wurde am 14. April 2011 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


      „Simulationsmodell für eine Windenergieanlage sowie Erstellung und
                                 Verwendung“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 18. September 2015 aus Gründen
der Bescheide vom 11. Oktober 2011 bzw. 6. Februar 2015 zurückgewiesen,
nachdem der Anmelder um Entscheidung nach Aktenlage gebeten hat. In den
genannten Bescheiden führt die Prüfungsstelle sinngemäß aus, dass mit dem
Verfahren des (damals) geltenden Patentanspruchs 1 ein nicht-technisches Problem mit Mitteln gelöst werden solle, die nicht über den bestimmungsgemäßen
Einsatz einer Datenverarbeitungsanlage hinausgingen. Der Patentanspruch 1 sei
daher gemäß § 1 Abs. 3 i. V. m. Abs. 4 PatG nicht gewährbar.


Gegen diesen Beschluss ist die Beschwerde des Anmelders gerichtet. Er hat
zuletzt eine Entscheidung nach Aktenlage beantragt und ist zur mündlichen Verhandlung – wie angekündigt – nicht erschienen.


Der Anmelder hat mit Eingabe vom 28. Oktober 2015 sinngemäß beantragt,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       gemäß Hauptantrag mit
       Patentansprüchen 1 bis 16 vom 14. April 2012;

                                        -3-



         Beschreibungsseiten 1 bis 29 vom Anmeldetag und
         Figuren 1 bis 5 vom Anmeldetag;


         gemäß Hilfsantrag I mit
         Patentansprüchen 1 bis 6 vom 28. Oktober 2015;
         im Übrigen wie Hauptantrag;


         gemäß Hilfsantrag II mit
         Patentansprüchen 1 bis 5 vom 28. Oktober 2015;
         im Übrigen wie Hauptantrag;


         gemäß Hilfsantrag III mit
         Patentansprüchen 1 bis 5 vom 28. Oktober 2015;
         im Übrigen wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt wurde kein
Stand der Technik ermittelt. Vom Senat wurden zwischenzeitlich die Druckschriften


D1:     JAUCH, C.; CRONIN, T.; SØRENSEN, P.: A Fuzzy Logic Pitch Angle
Controller for Power System Stabilization. In: Wind Energy 10(1): pp 19–30,
2007;     published      online      12 July 2006   in    Wiley   Interscience,
(www.interscience.wiley.com) DOI: 10.1002/we.205

und

D2:     JELAVIĆ, M.; PERIĆ, N.; PETROVIĆ, I.: Identification of Wind Turbine
Model for Controller Design. In: 2006 12th International Power Electronics
and Motion Control Conference, Print ISBN: 1-4244-0121-6; added to IEEE
Xplore: 10 February 2009, DOI: 10.1109/EPEPEMC.2006.4778634


eingeführt.

                                      -4-



Zu den Einzelheiten wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


M1´       Verfahren zur Erstellung eines Software-Simulationsmodells (200) für
          eine Windenergieanlage durch ein Computersystem, wobei das Software-Simulationsmodell (200) zur Integration in ein Stromversorgungsnetz-Simulationsmodell für eine Simulation des Zusammenhangs zwischen mehreren Eingangsgrößen (´wind´, ´PSO´, ´V´) und wenigstens
          einer Ausgangsgröße (Pelec, Qelec) bzw. des Verhaltens der Windenergieanlage im Netzverbund bestimmt ist, wobei das Verfahren aufweist:


M1.1´     Ermitteln von Betriebsbereichen, in denen die Windenergieanlage
          jeweils als ein näherungsweise lineares System betrachtet werden
          kann;


M1.2´     Bestimmen für jeden der Betriebsbereiche jeweils mindestens einer
          Übertragungsfunktion (Pelec1, …, Pelecm, Pelecn, …, Pelecr, Pelecs, …,
          Pelecy), welche das Verhalten der Windenergieanlage im zugehörigen
          Betriebsbereich mit einer vorbestimmten Genauigkeit abbildet;


M1.3´     Einrichten einer Auswahl- und Kombinationsfunktion (FLR), die für jede
          Eingangsgröße (´wind´, ´PSO´, ´V´) wenigstens eine der Übertragungsfunktionen (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t),
          Pelecs(t), …, Pelecy(t)) entsprechend einem aktuellen Betriebszustand
          der Windenergieanlage auswählt und aus den Ausgaben (Pelec1(wind),
          …, Pelecm(wind), Pelecn(PSO), …, Pelecr(PSO), Pelecs(V), …,
          Pelecy(V)) der ausgewählten wenigstens einen der Übertragungsfunktionen (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …,

                                      -5-



        Pelecy(t)) einen aktuellen Wert für die wenigstens eine Ausgangsgröße
        (Pelec, Qelec) der Windenergieanlage bildet; und


M1.5    Bilden des Software-Simulationsmodells (200) aus den Übertragungsfunktionen (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …,
        Pelecy(t)) und der Auswahl- und Kombinationsfunktion (FLR)


M2´     wobei die Betriebsbereiche jeweils für einen Zusammenhang zwischen
        jeweils einer der Eingangsgrößen (´wind´, ´PSO´, ´V´) und einer der
        wenigstens einen Ausgangsgröße (Pelec, Qelec) ermittelt werden, und


M2.2´   wobei das Ermitteln der Betriebsbereiche weiter aufweist:
        jeweils Auffinden von Betriebspunkten, an denen der Zusammenhang
        zwischen jeweils einer der Eingangsgrößen (´wind´, ´PSO´, ´V´) und der
        wenigstens einen Ausgangsgrößen (Pelec, Qelec) der Windenergieanlage nicht linear ist, als Ränder der Betriebsbereiche, und


M3      wobei das Bestimmen der Übertragungsfunktionen (Pelec1(t), …,
        Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …, Pelecy(t)) weiter aufweist:


M3.1´   Anwenden eines Systemidentifikationsverfahrens zur Bestimmung von
        jeweils wenigstens einer Übertragungsfunktion (Pelec1(t), …, Pelecm(t),
        Pelecn(t), …, Pelecr(t), Pelecs(t), …, Pelecy(t)) für jeden Betriebsbereich
        basierend auf zueinander gehörigen Wertepaaren der jeweiligen einen
        der Eingangsgrößen und der wenigstens einen Ausgangsgröße,


M3.2´   wobei die Wertepaare insbesondere mittels eines herkömmlichen Simulationsmodells erzeugt werden bzw. wurden und/oder auf Messungen
        an der Windenergieanlage basieren.

                                         -6-



Der mit einer möglichen Gliederung versehene Patentanspruch 1 gemäß Hilfsantrag I lautet:


M1a         Verfahren zur Erstellung eines Software-Simulationsmodells (200) für
            eine Windenergieanlage, WEA, zur Überprüfung der Kompatibilität der
            WEA mit einem Stromversorgungsnetz, besonders der Konformität mit
            gültigen Grid-Codes, und zum Test von Maßnahmen der Netzführung,
            durch ein Computersystem, wobei das Software-Simulationsmodell (200) zur Integration in ein Stromversorgungsnetz-Simulationsmodell für eine Simulation des Zusammenhangs zwischen mehreren Eingangsgrößen (´wind´, ´PSO´, ´V´) und wenigstens einer Ausgangsgröße
            (Pelec, Qelec) bzw. des Verhaltens der WEA im Netzverbund bestimmt
            ist, wobei das Verfahren aufweist:


M1.1        Ermitteln von Betriebsbereichen, in denen die WEA jeweils als ein
            näherungsweise lineares System betrachtet werden kann;


M1.2        Bestimmen für jeden der Betriebsbereiche jeweils mindestens einer
            Übertragungsfunktion (Pelec1, …, Pelecm, Pelecn, …, Pelecr, Pelecs, …,
            Pelecy), welche das Verhalten der WEA im zugehörigen Betriebsbereich mit einer vorbestimmten Genauigkeit abbildet;


M1.3        Einrichten einer Auswahl- und Kombinationsfunktion (FLR), die für jede
            Eingangsgröße (´wind´, ´PSO´, ´V´) wenigstens eine der Übertragungsfunktionen (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t),
            Pelecs(t), …, Pelecy(t)) entsprechend einem aktuellen Betriebszustand
            der WEA auswählt und aus den Ausgaben (Pelec1(wind), …,
            Pelecm(wind), Pelecn(PSO), …, Pelecr(PSO), Pelecs(V), …, Pelecy(V))
            der ausgewählten wenigstens einen der Übertragungsfunktionen
            (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …, Pelecy(t))

                                     -7-



       einen aktuellen Wert für die wenigstens eine Ausgangsgröße (Pelec,
       Qelec) der WEA bildet; und


M1.5   Bilden des Software-Simulationsmodells (200) aus den Übertragungsfunktionen (Pelec1(t), …, Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …,
       Pelecy(t)) und der Auswahl- und Kombinationsfunktion (FLR),


M2     wobei die Betriebsbereiche jeweils für einen Zusammenhang zwischen
       jeweils einer der Eingangsgrößen (´wind´, ´PSO´, ´V´) der WEA, und
       einer der wenigstens einen Ausgangsgröße (Pelec, Qelec) der WEA,
       ermittelt werden,


M2.1   wobei die mehreren Eingangsgrößen (´wind´, ´PSO´, ´V´) der Windenergieanlage ein Wert der aktuellen Windgeschwindigkeit (wind)
       und/oder ein aktueller Wert der aktuellen Netzspannung (´V´) und/oder
       ein aktueller Leistungssollwert (PSO) für die Windenergieanlage
       und/oder ein aktueller Wert der Netzfrequenz und/oder ein Sollwert für
       die von der Windenergieanlage abzugebende elektrische Wirk- und/
       oder Blindleistung sind; und wobei die wenigstens einen Ausgangsgröße (Pelec, Qelec) der Windenergieanlage ein aktueller Wert für die
       aktuell von der Windenergieanlage abgegebene elektrische Wirkleistung (Pelec) und/oder elektrische Blindleistung (Qelec) ist, und


M2.2   wobei das Ermitteln der Betriebsbereiche weiter aufweist:
       jeweils Auffinden von Betriebspunkten, an denen der Zusammenhang
       zwischen jeweils einer der Eingangsgrößen (´wind´, ´PSO´, ´V´) und der
       wenigstens einen Ausgangsgrößen (Pelec, Qelec) der WEA nicht linear
       ist, als Ränder der Betriebsbereiche, und


M3     wobei das Bestimmen der Übertragungsfunktionen (Pelec1(t), …,
       Pelecm(t), Pelecn(t), …, Pelecr(t), Pelecs(t), …, Pelecy(t)) weiter aufweist:

                                       -8-



M3.1      Anwenden eines Systemidentifikationsverfahrens zur Bestimmung von
          jeweils wenigstens einer Übertragungsfunktion (Pelec1(t), …, Pelecm(t),
          Pelecn(t), …, Pelecr(t), Pelecs(t), …, Pelecy(t)) für jeden Betriebsbereich
          basierend auf zueinander gehörigen Wertepaaren der jeweiligen einen
          der Eingangsgrößen der WEA und der wenigstens einen Ausgangsgröße der WEA,


M3.2      wobei die benötigten Wertepaare auf Messungen an der WEA basieren.


Der Patentanspruch 1 gemäß Hilfsantrag II unterscheidet sich von Patentanspruch 1 gemäß Hilfsantrag I durch Merkmal M1.4, das zwischen die Merkmale
M1.3 und M1.5 eingefügt werden soll, d. i.


M1.4      „wobei das Einrichten der Auswahl- und Kombinationsfunktion weiter
          aufweist: Bilden der Auswahl- und Kombinationsfunktion durch einen
          Fuzzy-Logik-Regler (FLR); und“


Patentanspruch 1 gemäß Hilfsantrag III beruht auf Patentanspruch 1 gemäß
Hilfsantrag II, wobei Merkmal M1a durch Merkmal M1b ersetzt wird, d. i.


M1b       „Simulation einer Windenergieanlage, WEA, und eines Stromversorgungsnetzwerks, mit dem die WEA gekoppelt ist, zur Überprüfung der
          Kompatibilität der WEA mit einem Stromversorgungsnetz, besonders
          der Konformität mit gültigen Grid-Codes, und zum Test von Maßnahmen der Netzführung unter Verwendung eines Software-Simulationsmodells, das mit einem Verfahren zur Erstellung eines Software-Simulationsmodells (200) für die WEA durch ein Computersystem erzeugt
          wurde, wobei das Software-Simulationsmodell (200) zur Integration in
          ein Simulationsmodell des Stromversorgungsnetzes für eine Simulation
          des Zusammenhangs zwischen mehreren Eingangsgrößen (´wind´,
          ´PSO´, ´V´) und wenigstens einer Ausgangsgröße (Pelec, Qelec) bzw.

                                       -9-



           des Verhaltens der WEA im Netzverbund bestimmt ist, wobei das Verfahren aufweist:“


In Hinblick auf die übrigen Patentansprüche wird auf den Akteninhalt verwiesen.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da der Gegenstand des jeweiligen Patentanspruchs 1
gemäß Hauptantrag sowie den Hilfsanträgen I bis III nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.     Die Anmeldung betrifft die Erstellung eines – insbesondere mit Softwaremitteln implementierten – Simulationsmodells für eine Windenergieanlage, ein entsprechendes Simulationsmodell sowie die Verwendung des Simulationsmodells
bei der Simulation wenigstens eines Stromversorgungsnetzes (Offenlegungsschrift, Abs. [0002]).


Ausweislich der Anmeldung hat der Hersteller einer Windenergieanlage – bevor
diese in ein öffentliches Stromversorgungsnetz integriert werden könne, d. h. als
Lieferant für elektrische Energie an das Netz angeschlossen werden dürfe – die
Konformität der Anlage mit den jeweils gültigen Anschlussregeln (Grid-Codes)
nachzuweisen. Hierbei habe der Hersteller der Anlage dem Betreiber des Stromversorgungsnetzes ein Software-Simulationsmodell für die Anlage zur Verfügung
zu stellen. Für das Simulationsmodell seien technische Design-Parameter der Bestandteile der Anlage erforderlich, die zumindest dem Hersteller bekannt seien
(Offenlegungsschrift, Abs. [0003]). Ein solches Software-Simulationsmodell ermögliche es dem Netzbetreiber, das Netzverhalten der Windenergieanlage im
Netzverbund zu simulieren. Damit könnten z. B. die Kompatibilität der Anlage mit
dem Netz überprüft, aber auch Maßnahmen der Netzführung getestet werden

                                       - 10 -



(Offenlegungsschrift, Abs. [0004]). In der Vergangenheit sei der Forderung der
Netzbetreiber durch Bereitstellung fertig kompilierter Software-Simulationsmodelle
für die jeweiligen Windkraftanlagen entsprochen worden. Mittlerweile forderten
jedoch sowohl Netzbetreiber als auch Zulassungsbehörden die Bereitstellung der
zugehörigen Quellcodes sowie ausführlicher Beschreibungen der Simulationsmodelle, um z. B. bei Bedarf Anpassungen an unterschiedliche Simulationsumgebungen vornehmen zu können (Offenlegungsschrift, Abs. [0005]). Um eine Windenergieanlage überhaupt auf dem Markt anbieten zu können, sei der Hersteller
daher immer mehr gezwungen, den Quellcode des Simulationsmodells herausgeben zu müssen, wodurch aber gleichzeitig technische Informationen offengelegt
würden (Offenlegungsschrift, Abs. [0007]), die eigentlich nicht zur Veröffentlichung
vorgesehen seien und die auch der Anlage selbst nicht ohne weiteres zu entnehmen seien (Offenlegungsschrift, Abs. [0008]).


Als Aufgabe wird in der Beschwerdebegründung (Seite 3, vorletzter Absatz)
genannt, ein Software-Simulationsmodell bereitzustellen, bei dem der Quellcode
hinsichtlich nicht zur Veröffentlichung vorgesehener technischer Parameter der
Windenergieanlage nicht transparent ist. Mit anderen Worten: das beanspruchte
Verfahren soll in erster Linie dazu dienen, dass aus dem Simulationsmodell einer
Windenergieanlage keine Rückschlüsse auf die entsprechenden technischen Details der betreffenden Anlage gezogen werden können (Offenlegungsschrift, Abs.
[0007]–[0009]).


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zur Erstellung
eines Simulationsmodells für eine Windenergieanlage zu verbessern, ist ein Ingenieur der Fachrichtung Maschinenbau oder Elektrotechnik mit mehrjähriger
Berufserfahrung in der Entwicklung und dem Betrieb von Windkraftanlagen anzusehen, der insbesondere über fundierte Kenntnisse auf dem Gebiet der rechnergestützten Entwicklungsmethoden, wie z. B. computergestützte Konstruktion einschließlich Simulation, verfügt.

                                         - 11 -



2.      Der Gegenstand des jeweiligen Patentanspruchs 1 gemäß Hauptantrag
sowie den Hilfsanträgen I bis III beruht nicht auf erfinderischer Tätigkeit.


2.1     Zur Lehre des Patentanspruchs 1


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hilfsantrag II, der sämtliche Merkmale des Patentanspruchs 1 gemäß Hilfsantrag I
sowie inhaltlich bis auf Merkmal M3.2´ auch alle Merkmale des Patentanspruchs 1
gemäß Hauptantrag mit umfasst, ein Verfahren zur Erstellung eines Software-Simulationsmodells für eine Windenergieanlage vor, wobei das Simulationsmodell
zur Integration in ein Simulationsmodell eines Stromversorgungsnetzes vorgesehen ist, um den Zusammenhang zwischen mehreren Eingangsgrößen und
wenigstens einer Ausgangsgröße bzw. das Verhalten der Windenergieanlage im
Netzverbund zu simulieren. Mit Hilfe des beanspruchten Verfahrens werden die
Kompatibilität der Anlage mit dem Netz, insbesondere die Konformität der Anlage
mit den gültigen Grid-Codes überprüft und Maßnahmen der Netzführung getestet
(Merkmal M1a, M1´).


Merkmal M1.1 bzw. M1.1´ sieht die Ermittlung von Betriebsbereichen vor, in denen
die Windenergieanlage jeweils als quasi-lineares System angesehen werden
kann.


Laut Merkmal M1.2 bzw. M1.2´ wird für jeden der Betriebsbereiche mindestens
eine Übertragungsfunktion bestimmt, die das Verhalten der Windenergieanlage im
zugehörigen Betriebsbereich mit einer vorbestimmten Genauigkeit abbildet.


Weiterhin wird gemäß Merkmal M1.3 und M1.3´ eine Auswahl- und Kombinationsfunktion eingerichtet, die für jede Eingangsgröße wenigstens eine der Übertragungsfunktionen entsprechend einem aktuellen Betriebszustand der Windenergieanlage auswählt und aus den Ausgaben der ausgewählten Übertragungsfunk-

                                      - 12 -



tionen einen aktuellen Wert für die wenigstens eine Ausgangsgröße der Windenergieanlage bildet.


Laut Merkmal M1.4 wird als Auswahl- und Kombinationsfunktion ein Fuzzy-Logik-Regler verwendet.


Das Software-Simulationsmodell wird aus den Übertragungsfunktionen und der
Auswahl- und Kombinationsfunktion gebildet (Merkmal M1.5).


Die Merkmalskomplexe M2 und M2´ sehen vor, dass die Betriebsbereiche jeweils
für einen Zusammenhang zwischen jeweils einer der Eingangsgrößen und einer
der wenigstens einen Ausgangsgröße ermittelt werden.


In Merkmal M2.1 werden Ein- und Ausgangsgrößen der Windenergieanlage konkret angegeben: bei den Eingangsgrößen soll es sich um die Windgeschwindigkeit, die Netzspannung, einen Leistungssollwert der Anlage, die Netzfrequenz,
einen Sollwert für die von der Anlage abzugebende elektrische Wirk- und/oder
Blindleistung handeln. Die wenigstens eine Ausgangsgröße ist die von der Anlage
aktuell abgegebene elektrische Wirk- und/oder Blindleistung.


Zur Bestimmung der Betriebsbereiche und deren Ränder werden diejenigen Betriebspunkte ermittelt, an denen der Zusammenhang zwischen einer der Eingangsgrößen und einer Ausgangsgröße der Anlage nicht mehr linear beschrieben
werden kann (Merkmal M2.2, M2.2´).


Merkmalskomplex M3 befasst sich mit der Bestimmung der Übertragungsfunktionen.


Um die Übertragungsfunktionen zu bestimmen, wird ein Systemidentifikationsverfahren angewandt. Hierbei werden die Übertragungsfunktionen auf der Grundlage

                                      - 13 -



von zueinander gehörigen Wertepaaren der betrachteten mehreren Eingangsgrößen und der zugehörigen Ausgangsgröße ermittelt (Merkmal M3.1, M3.1´).


Merkmal M3.2 sieht vor, dass die benötigten Wertepaare auf Messungen an der
Windenergieanlage beruhen.


Patentanspruch 1 gemäß Hauptantrag geht inhaltlich über Patentanspruch 1
gemäß Hilfsantrag II lediglich insofern hinaus, als dass gemäß Merkmal M3.2´ die
für die Systemidentifikation benötigten Wertepaare mittels eines herkömmlichen
Simulationsmodells erzeugt werden und/oder auf Messungen an der Windenergieanlage basieren.


In Merkmal M1b des Patentanspruchs 1 gemäß Hilfsantrag III wird im Wesentlichen die Durchführung einer Simulation einer Windenergieanlage und eines
Stromversorgungsnetzwerks beansprucht, wobei unter Verwendung des erstellten
Simulationsmodells die Kompatibilität der Anlage mit dem Stromversorgungsnetz
überprüft und Maßnahmen der Netzführung getestet werden sollen.


2.2   Zu Hauptantrag und Hilfsanträgen I bis III


Dem Hauptantrag und den Hilfsanträgen I bis III kann nicht stattgegeben werden,
weil der Gegenstand ihres jeweiligen Patentanspruchs 1 nahegelegen hat.


2.2.1 Zur Beurteilung der beanspruchten Lehre sind die Druckschriften D1 und
D2 von besonderer Bedeutung.


Die Druckschrift D1 befasst sich mit einem Fuzzy Logik Neigungswinkelregler für
eine active-stall-geregelte Windturbine, der zur Stabilisierung eines Stromversorgungssystems angewendet wird. Der Fachartikel führt den Fachmann zu einem
Verfahren zur Erstellung eines Software-Simulationsmodells für eine Windenergieanlage. Das bekannte Verfahren umfasst insbesondere den Designprozess für

                                      - 14 -



einen Fuzzy Logik Regler (Abstract), der in das Modell einer Windturbine integriert
wird, die über ein Stromnetz mit einem Energiesystem (power system) verbunden
ist (Seite 22, oben; Fig. 1, 2). Auf Grundlage des Simulationsmodells wird untersucht, inwieweit die Windturbine in der Lage ist, Frequenzschwankungen im
Stromversorgungsnetz auszugleichen und dadurch die Stromversorgung zu stabilisieren (Seite 20, sechster Absatz). Die Auswirkungen einer Erhöhung und Verminderung der von der Anlage abgegebenen elektrischen Leistung auf die Steuerung des Gesamtsystems werden analysiert (Seite 20, dritter Absatz, siehe „This
can be achieved by a variation in output power of the wind farm“; Seite 20, Abschnitt „System Description“). Insoweit ermöglicht das Simulationsmodell nicht nur
eine Überprüfung, ob die modellierte Windenergieanlage eine wichtige systemstützende Funktion im Verteilernetz übernehmen und damit eine der typischen
technischen Anforderungen an Anlagen im Übertragungsnetz erfüllen kann,
wodurch Kompatibilität mit dem Verteilernetz erzielt wird. Das Modell erlaubt
außerdem, die Steuerung der elektrischen Leistung als Maßnahme der Netzführung zu testen. Das Simulationsmodell der Windturbine wird laut Druckschrift D1 in
das Simulationsmodell eines Stromversorgungsnetzes integriert (Seite 20, drittletzter Absatz, siehe „The wind turbine model and the power system model are
implemented in the power system simulation tool PowerFactory …“) und wird zur
Simulation eines Zusammenhangs zwischen mehreren Eingangsgrößen (Seite 23,
Abschnitt „Input Signals“) und wenigstens einer Ausgangsgröße (Fig. 2, siehe Pm
bzw. Pel) der Windenergieanlage genutzt. Merkmal M1a bzw. M1´ geht somit aus
der Druckschrift D1 hervor.


In dem in der Druckschrift D1 offenbarten Verfahren wird wenigstens eine Übertragungsfunktion ermittelt, die das Verhalten der Windenergieanlage bzw. der
Windturbine in einem Betriebsbereich mit einer bestimmten Genauigkeit abbildet
(Seite 22, letzter Absatz, siehe „Although the system simulated here is a realistic
simulation model described in terms of transfer functions, it does not describe a
wind turbine to its full extent.“). Merkmal M1.2 bzw. M1.2´ ist demnach zumindest
teilweise erfüllt.

                                      - 15 -



Weiterhin ist im Simulationsmodell der Druckschrift D1 ein Fuzzy Logik Regler
(Fuzzy Logic Controller) vorgesehen, der als Auswahl- und Kombinationsfunktion
fungiert (Seite 22, Absatz „Fuzzy Logic Controller“; Fig. 2) und dadurch das Verhalten der Windenergieanlage bestimmt (teilweise Merkmal M1.3, M1.3´; Merkmal
M1.4).


Als Eingangsgröße der Windenergieanlage wird insbesondere ein aktueller Wert
der Netzfrequenz f (inklusive deren zeitliche Abhängigkeit df/dt) genannt, als Ausgangsgröße wird die elektrische Wirkleistung Pel betrachtet (Fig. 2 – Merkmal
M2.1).


Der Fachartikel D2 befasst sich mit dem Design eines Neigungswinkelreglers für
eine Windenergieanlage, das auf dem Modell einer Windturbine beruht. Auch die
Druckschrift D2 lehrt ein Verfahren zur Erstellung eines Software-Simulationsmodells für eine Windenergieanlage bzw. Windturbine (u. a. Abstract). Das Modell
liefert die Grundlage für die Simulation eines Zusammenhangs zwischen mehreren Eingangsgrößen und wenigstens einer Ausgangsgröße. Die betrachteten Größen sind in Gl. (1) der Seite 2 genannt und betreffen in erster Linie Windgeschwindigkeit, Einstellwinkel der Rotorblätter, elektromagnetisch erzeugtes Drehmoment des Generators sowie die Rotordrehzahl. Der Fachmann wird erkennen,
dass die Rotordrehzahl (entsprechend der Drehzahlkennlinie des verwendeten
Generators) die an der Anlage abgegebene elektrische Leistung eindeutig
bestimmt und somit indirekt für diese als Ausgangsgröße steht. Merkmal M1a bzw.
M1´ geht demnach zumindest teilweise aus der Druckschrift D2 hervor.


Aufgrund des stark nicht-linearen Verhaltens der Windturbine (Seite 2, linke
Spalte, letzter Absatz), das die Verwendung eines einzigen linearen Modells
unmöglich macht, schlägt die Druckschrift D2 eine Mehrzahl linearer Modelle vor,
wobei jedes Modell das Verhalten der Windturbine in einer gewissen Umgebung
um einen bestimmten Betriebspunkt hinreichend gut beschreibt (Seite 2, rechte
Spalte, erster Absatz; siehe „A possible solution is using set of linear models

                                         - 16 -



where one model describes wind turbine behaviour around one operating point.“).
So werden in der Druckschrift D2 30 lineare Modelle betrachtet, die jeweils einem
Betriebspunkt bzw. Betriebsbereich zugewiesen sind (Seite 4, rechte Spalte,
zweiter Absatz; Seite 5, rechte Spalte, erster Absatz). Merkmal M1.1 bzw. M1.1´
ist damit erfüllt.


Ein lineares Modell, das das Verhalten der Windturbine im i-ten Betriebspunkt
beschreibt, ist in Gl. (2) der Seite 2 ganz allgemein formuliert. Für jeden der Betriebspunkte bzw. -bereiche werden drei Übertragungsfunktionen G ermittelt, die
das Verhalten der Windturbine im zugehörigen Betriebsbereich mit einer gewissen
Genauigkeit abbilden (Seite 3, linke Spalte, dritter Absatz oben; Seite 3, rechte
Spalte oben – Merkmal M1.2, M1.2´).


Weiterhin wird im bekannten Verfahren eine Auswahl- und Kombinationsfunktion
in Form eines Fuzzy Modells angewendet, die für jede in der Gl. (2) aufgeführte
Eingangsgröße eine Übertragungsfunktion G auswählt, die sich am aktuellen Betriebszustand der Anlage bzw. dem aktuellen Einstellwinkel der Rotorblätter orientiert (Seite 5, rechte Spalte, Abschnitt IV, insbes. Gl. (3)). Aus den Ausgaben der
Übertragungsfunktionen G wird gemäß Gl. (2) ein Wert für die Rotordrehzahl als
Ausgangsgröße der Anlage errechnet (Merkmal M1.3, M1.3´).


Merkmal M1.4, das einen Fuzzy Logik Regler vorsieht, ist aufgrund von Abschnitt IV der Druckschrift D2 ebenfalls erfüllt.


Aus Gl. (3) der Seite 5 in Verbindung mit Gl. (2) der Seite 2 folgt unmittelbar, dass
das Simulationsmodell der Druckschrift D2 sowohl auf den Übertragungsfunktionen G als auch infolge der fuzzy rules auf der Auswahl- und Kombinationsfunktion beruht (Merkmal M1.5).


Aus Gl. (2) folgt auch, dass die Betriebsbereiche bzw. -punkte für einen Zusammenhang der Eingangsgrößen auf der rechten Seite der Gl. (2) und der Rotor-

                                       - 17 -



drehzahl als Ausgangsgröße bestimmt werden (Merkmal M2, M2´). Jeder der Betriebsbereiche entspricht einem eigenen linearen Modell aus Gl. (2).


Als Eingangsgrößen werden in der Druckschrift D2 Windgeschwindigkeit, Einstellwinkel und elektromagnetisches Drehmoment genannt. Ausgangsgröße ist die
Rotordrehzahl in einem gewissen Betriebspunkt, der ein bestimmter Wert für die
abgegebene elektrische Leistung zugeordnet ist. Merkmal M2.1 ist damit erfüllt.


Für den Fachmann ist selbstverständlich, die einzelnen Betriebsbereiche derart zu
wählen, dass der Zusammenhang zwischen Eingangsgrößen und Ausgangsgröße
durch ein lineares Modell noch hinreichend gut beschrieben wird. Dementsprechend wird er die Ränder der Betriebsbereiche immer so einstellen, dass diese
den linearen Zusammenhang gerade noch erfüllen (Merkmal M2.2, M2.2´). Dass
die Einstellwinkel pro lokalem Betriebsbereich dynamisch angepasst und somit die
Ränder eines Betriebsbereichs eingestellt werden können, geht aus den Gln. (5)
bis (7) der Druckschrift D2 hervor.


Ferner zeigt die Druckschrift D2 die Anwendung von Techniken der Systemidentifikation zur Abschätzung der Übertragungsfunktionen G für jeden Betriebsbereich
(Seite 3, linke Spalte, zweiter Absatz; dritter Absatz, siehe „Experiment was
repeated for each operating point… Fig. 4 shows estimated frequency characteristic of G for one operating point.“). Die Systemidentifikation beruht auf der Ermittlung der quantitativen Abhängigkeit der Rotordrehzahl (Ausgangsgröße) von dem
Einstellwinkel der Rotorblätter, dem elektromagnetischen Drehmoment des Generators und der Windgeschwindigkeit (Eingangsgrößen) auf Basis zusammengehöriger Wertepaare (Fig. 3, 4 und 5 – Merkmale M3, M3.1, M3.1´).


Die in der Druckschrift D2 durchgeführte Systemidentifikation stützt sich v. a. auf
die Resultate der kommerziellen Software GH Bladed, um eine reale Windturbine
nachzubilden. Alternativ wird aber auf die Möglichkeit einer Verwendung experimenteller Ergebnisse aus Messungen an realen Turbinen hingewiesen. Diese

                                      - 18 -



experimentelle Methode werde aber für die vorgeschlagene Lösung nicht in Betracht gezogen, da sie in der Regel aus Sicherheitsgründen beschränkt sei
(Seite 2, linke Spalte, Abschnitt III, erster Absatz). Demzufolge ist zumindest die
erste Alternative aus Merkmal M3.2´ verwirklicht.


2.2.2 Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
der mit dem jeweiligen Patentanspruch 1 gemäß Hauptantrag sowie Hilfsantrag I
bis III beanspruchte Gegenstand für den Fachmann nahegelegen hat. Dies gilt
selbst dann, wenn der Prüfung der gesamte Patentanspruch mit allen seinen
Merkmalen zugrunde gelegt wird. Damit kann dahingestellt bleiben, ob der jeweils
beanspruchte Gegenstand gemäß § 1 Abs. 3 i. V. m. Abs. 4 PatG vom Patentschutz ausgeschlossen ist, und ob der jeweilige Patentanspruch 1 Merkmale enthält, die nicht die Lösung eines technischen Problems mit technischen Mitteln
bestimmen oder beeinflussen und somit bei der Prüfung der erfinderischen Tätigkeit nicht zu berücksichtigen sind (BGH GRUR 2011, 125 – Wiedergabe topografischer Informationen).


Aufgrund der Tatsache, dass in der Lösung der Druckschrift D1 zur Implementierung eines Fuzzy Logik Reglers in das Modell einer Windenergieanlage Übertragungsfunktionen (transfer functions) herangezogen werden sollen (vgl. D1
Seite 22, letzter Absatz), hatte der Fachmann Veranlassung, sich überall dort nach
Anregungen umzusehen, wo effektive, auf der Verwendung von Übertragungsfunktionen basierende Algorithmen zur rechnerischen Simulation von Windenergieanlagen zum Einsatz kommen. Eine mögliche Lösung wird in der Druckschrift D2 aufgezeigt, welche lehrt, nicht nur Modelle für Windturbinen mittels
Übertragungsfunktionen zu erstellen, sondern auch Simulationen der charakteristischen Größen durchzuführen.


Angesichts des in der Druckschrift D2 gegebenen Hinweises, das stark nichtlineare Verhalten einer Windturbine durch Verwendung linearer Modelle hinreichend gut annähern zu können (vgl. D2 Seite 2, linke Spalte, Abschnitt III, zweiter

                                      - 19 -



Absatz oben; Seite 2, rechte Spalte, erster Absatz), bot es sich für den Fachmann
an, die Lehre der Druckschrift D2 auf das System der Druckschrift D1 anzuwenden, indem die Windturbine aus dem Modell zur Stabilisierung der Stromversorgung (vgl. D1 Fig. 2) durch das Modell eines Reglers nach dem Vorbild der Druckschrift D2 beschrieben wird und die Eingangsgrößen Netzfrequenz f und elektrische Leistung P den Pitch Winkel steuern.


Von einer solchen kombinierten Lehre unterscheidet sich die Lehre nach dem
jeweiligen Patentanspruch 1 gemäß Hilfsantrag I und II im Wesentlichen nur noch
dadurch, dass die für die Systemidentifikation benötigten Wertepaare auf Messungen an der Windenergieanlage (anstatt auf Resultaten einer professionellen Software wie in der D2) beruhen sollen (Merkmal M3.2).


In der Druckschrift D2 wird diesbezüglich eine Verwendung von Resultaten aus
einem herkömmlichen Simulationsmodell der Software GH Bladed bevorzugt. Der
Fachmann entnimmt der Druckschrift D2 aber auch die Alternative, anstatt dessen
Ergebnisse aus Messungen an realen Windturbinen zu verwerten (siehe oben).
Für die Auswahl einer der beiden ihm bekannten Möglichkeiten unter Abwägen
der jeweiligen Vor- und Nachteile und unter Inkaufnahme der entsprechenden
Nachteile ist aber kein erfinderisches Zutun erforderlich (Merkmal M3.2, vgl. BGH
GRUR 2006, 930 – Mikrotom).


2.2.2.1      Es waren für den Fachmann somit lediglich fachgemäße Überlegungen erforderlich, um ausgehend von der Druckschrift D1 zu einem Verfahren mit
sämtlichen Merkmalen des jeweiligen Patentanspruchs 1 gemäß Hilfsantrag I und
II zu gelangen.


2.2.2.2      Patentanspruch 1 gemäß Hauptantrag ist nicht günstiger zu beurteilen, da dessen Merkmale M1´ bis M3.1´ inhaltlich nicht über die jeweiligen Merkmale des Anspruchs 1 gemäß Hilfsantrag II hinausgehen und zumindest die erste
Alternative des Merkmals M3.2´ unmittelbar aus der Druckschrift D2 folgt.

                                      - 20 -



2.2.2.3       Unter Berücksichtigung der Ausführungen zu den Hilfsanträgen I und
II beruht auch der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag III nicht
auf erfinderischer Tätigkeit.


Insbesondere ergibt sich Merkmal M1b des Patentanspruchs 1 gemäß Hilfsantrag III, das im Wesentlichen eine Simulation einer Windenergieanlage unter Verwendung eines Software-Simulationsmodells vorsieht, direkt aus der Druckschrift D1. Dort werden auf den Seiten 26ff. die Resultate von Simulationsrechnungen mit dem eingangs beschriebenen Design eines Fuzzy Logik Reglers vorgestellt


2.2.3 Die vom Anmelder schriftsätzlich vorgetragenen Einwände greifen nicht
durch.


2.2.3.1       Dem Vorbringen des Anmelders, die Druckschrift D1 gebe kein Verfahren zur Erstellung eines Software-Simulationsmodells, mit dem sich eine Überprüfung von Grid-Codes vornehmen lasse, konnte nicht gefolgt werden.


So wird in der Druckschrift D1 ein Fuzzy Logic Controller per Simulation bewertet
(Abstract, siehe „The performance of the controller is assessed by simulation …“);
einzelne Schritte für den Designprozess und damit die Modellerstellung werden
auf Seite 23, dritter Absatz genannt. Darüber hinaus wird der Fachmann in den in
der Druckschrift D1 geschilderten Untersuchungen von Maßnahmen zur Netzstabilisierung immer auch eine Überprüfung der Einhaltung von seitens der Netzbetreiber gestellten Anforderungen erkennen, die gewöhnlich in den Grid-Codes
ihren Ausdruck finden.


2.2.3.2       Dem Anmelder ist zwar darin zuzustimmen, dass die Druckschrift D1
nicht direkt die Auswahl von Übertragungsfunktionen zum Ziel hat. Allerdings ist
das dort vorgeschlagene realistische Simulationsmodell hinsichtlich seiner Einzelkomponenten wenigstens in Übertragungsfunktionen formuliert (Seite 22, letzter

                                      - 21 -



Absatz, siehe „…described in terms of transfer functions“), weswegen sich dem
Fachmann ausgehend von der Druckschrift D1 die Druckschrift D2 zur Ausgestaltung der Übertragungsfunktionen besonders anbot.


2.2.3.3      Nach Auffassung des Anmelders sieht die beanspruchte Lehre im
Gegensatz zu den Druckschriften D1 und D2 vor, ausschließlich der Anlage „von
außen eingeprägte Größen“ zu nutzen, um wiederum „nach außen abgegebene
Größen“ zu ermitteln.


Diesem Vorbringen kann im Wesentlichen nicht gefolgt werden.


Dem Anmelder ist zwar darin zuzustimmen, dass die Druckschrift D1 einen Fuzzy
Logik Regler als Auswahl- und Kombinationsfunktion vorstellt, mit der ein Pitch
Winkel bestimmt wird und nicht etwa eine oder mehrere Übertragungsfunktionen,
die das Verhalten einer Windenergieanlage abbilden. Auch werden – wie der Anmelder richtig erkennt – in der Lehre der Druckschrift D2 die Übertragungsfunktionen entsprechend dem Pitch Winkel ausgewählt, der eine interne Größe der
Windenergieanlage darstellt.


Allerdings offenbart bereits die Druckschrift D1 „von außen eingeprägte Größen“,
z. B. die Netzfrequenz f oder die elektrische Leistung P der Windenergieanlage,
die dazu verwendet werden, um (über den Pitch Winkel) eine „nach außen abgegebene Größe“, z. B. die am Generator abgegriffene elektrische Leistung Pel zu
bestimmen (Seite 23, siehe „Input Signals“; Fig. 2). Darüber hinaus weist das in
der Druckschrift D2 vorgeschlagene Modell zumindest die „externe Eingangsgröße“ Windgeschwindigkeit auf (vgl. Seite 2, Gl. (1)). Weiterhin stellt sich der
Pitch Winkel in einem aus den jeweiligen Simulationsmodellen der Druckschriften D1 und D2 zusammengesetzten Modell für den Fachmann als Funktion der
elektrischen Größen Netzfrequenz f und Leistung P dar, so dass im kombinierten
System externe Eingangsgrößen auf die externe Ausgangsgröße Rotordrehzahl

                                        - 22 -



abgebildet werden, die wiederum eine Aussage über die abgegebene elektrische
Leistung Pel macht.


2.2.3.4      Der Anmelder argumentiert, in der Lehre der Druckschrift D2 gebe es
keinen Zusammenhang zwischen Drehzahl und Drehmoment im Volllastbereich,
weswegen sich auch kein verlässlicher Zusammenhang zwischen Drehzahl und
Wirkleistung ergebe. Allenfalls im Teillastbereich im stationären Betrieb ergebe
sich ein Zusammenhang zwischen Drehzahl und Wirkleistung.


Der Einwand vermochte nicht zu überzeugen.


So verlangt der jeweilige Patentanspruch 1 nicht, dass das anspruchsgemäße
Software-Simulationsmodell lediglich auf den Volllastbetrieb einer Windenergieanlage ausgerichtet ist. Vielmehr sind vom Patentanspruch 1 auch andere Betriebsbereiche, z. B. ein Teillastbetrieb mit umfasst. Weiterhin ist nicht erkennbar,
dass die Lehre der Druckschrift D2 auf ganz bestimmte Betriebsbereiche beschränkt sein soll, so dass grundsätzlich außer einem Volllast- auch ein Teillastbetrieb mit Zusammenhang zwischen Drehzahl und Wirkleistung modelliert werden kann.
Selbst wenn unterstellt wird, dass es im Volllastbetrieb der Windenergieanlage
keinerlei verlässlichen Zusammenhang zwischen Drehzahl und Drehmoment bzw.
elektrischer Wirkleistung gibt, ist es für den Fachmann mehr als naheliegend, in
einem ergänzten Generatormodell, das mit leicht interpretierbaren Übertragungsfunktionen beschrieben wird, die Rotordrehzahl auf eine elektrische Leistung abzubilden, die – falls keine sonstigen Einschränkungen berücksichtigt werden – der
elektrischen Wirkleistung entspricht.


2.2.3.5      Ferner führt der Anmelder aus, die Anwendung einer Systemidentifikation auf eine reale Windenergieanlage sei neu. Nach der Druckschrift D2 werde
der Fachmann reale Messergebnisse nicht zugrunde legen.

                                       - 23 -



Dem Einwand konnte nicht gefolgt werden. So ist aus Druckschrift D2 die Anwendung einer Systemidentifikation bekannt (Seite 3, linke Spalte, 2. Absatz), um
Übertragungsfunktionen zu bestimmen. Zu diesem Zweck konnte der Fachmann
entweder auf die Resultate von Simulationen, wie die der professionellen Software
Bladed aus Druckschrift D2 zurückgreifen oder aber auf Messungen an realen
Windturbinen aufsetzen. Beide Möglichkeiten werden in der Druckschrift D2 angesprochen (Seite 2, linke Spalte, Abschnitt III, erster Absatz, unten). Nach geltender
Rechtsprechung kann jedoch die Auswahl einer der beiden ihm bekannten Möglichkeiten das Vorliegen einer erfinderischen Tätigkeit nicht begründen (BGH
a. a. O. – Mikrotom). Im Übrigen ist bei der professionellen Simulationssoftware
Bladed davon auszugehen, dass sich diese – um eine Windenergieanlage möglichst realitätsnah zu beschreiben – auch auf experimentelle Parameter stützt. Der
vom Anmelder schriftsätzlich vorgetragene Einwand, die Systemidentifikation der
Druckschrift D2 sei aufgrund von „Sprungfunktionen“ in den simulierten Eingangsgrößen nicht auf eine Systemidentifikation mit realen Messergebnissen übertragbar, geht bereits deswegen fehl, weil sich der Einwand offenbar auf simulierte
Testergebnisse zum bereits erstellten Modell stützt (Fig. 6, 8) und nicht etwa auf
Zeitreihenanalysen zur Bestimmung der frequenzabhängigen Übertragungsfunktionen G entsprechend den Figuren 3 und 4 (vgl. D2 Seite 3, linke Spalte, Mitte;
siehe „…From recorded input and output signals we are able to estimate frequency characteristics using spectral analysis …“). Solche Zeitreihenanalysen
sind grundsätzlich auch an realen Windenergieanlagen denkbar, indem z. B. die
Rotordrehzahl induktiv bzw. optisch gemessen wird, die Blattwinkelmessung per
Laser erfolgt und die Windgeschwindigkeit mit geeigneten Windmessgeräten
ermittelt wird.


2.2.4 Nach allem ist der Gegenstand des jeweiligen Patentanspruchs 1 gemäß
Hauptantrag und Hilfsantrag I bis III mit sämtlichen Merkmalen durch den den
Druckschriften D1 und D2 entnehmbaren Stand der Technik nahegelegt und somit
nicht patentfähig.

                                            - 24 -



2.2.5 Mit dem jeweiligen Patentanspruch 1 gemäß Hauptantrag und Hilfsantrag I
bis III fallen auch die jeweiligen übrigen Patentansprüche, da über einen Antrag
nur einheitlich entschieden werden kann (BGH GRUR 1997, 120 – Elektrisches
Speicherheizgerät).




                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
      kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek                 Eder                  Dr. Thum-Rung                   Dr. Forkel




                                                                                           Fa
