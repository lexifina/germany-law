---
ecli: "ECLI:DE:BPatG:2014:041114B17Wpat24.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 24/12"
decided: "2014-11-04"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=64&nr=26824&anz=1119&pos=960&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-11-04_17_W-pat_24_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 24/12 vom 2014-11-04

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 24/12                                                      Verkündet am
_______________                                                     4. November 2014
    (Aktenzeichen)                                                         …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2007 018 034.0


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 4. November 2014 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                      -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                  Gründe:


                                       I.


Die vorliegende Patentanmeldung ist am 17. April 2007 beim Deutschen Patentund Markenamt eingereicht worden. Sie beansprucht die Priorität zweier US-Anmeldungen, die älteste vom 16. November 2006, und trägt die Bezeichnung


     „Automatische Bildanalyse und Quantifizierung für Fluoreszenz-In Situ-Hybridisierung“.


Die Prüfungsstelle für Klasse G06T hat am 19. April 2012 die Anmeldung zurückgewiesen, da der Gegenstand des Patentanspruchs 1 aufgrund § 1 Abs. 3 und 4
PatG von der Patentierbarkeit ausgeschlossen sei.


Gegen den Beschluss wendet sich die am 21. Mai 2012 eingegangene Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt sinngemäß,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 21 vom 22. November 2011,
       Beschreibung Seiten 1 bis 43 und

                                       -3-



        35 Blatt Zeichnungen mit Figuren 1 bis 35, wie ursprünglich
        eingereicht.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: Martin Baatz, Nick Arini, Arno Schäpe, Gerd Binnig, Bettina Linssen:
        “Object-Oriented Image Analysis for High Content Screening: Detailed
        Quantiﬁcation of Cells and Sub Cellular Structures with the Cellenger
        Software“, Cytometry Part A, Vol. 69A (2006), Seiten 652 bis 658;
        published      online    5 May 2006,     Wiley      InterScience;   DOI:
        10.1002/cyto.a.20289


        D2: Franck Parazza, Catherine Humbert, Yves Usson: “Method for 3D
        Volumetric Analysis of Intranuclear Fluorescence Distribution in Confocal
        Microscopy”, Computerized Medical Imaging and Graphics, Vol. 17, No. 3
        (1993), Seiten 189 bis 200.


Der geltende, mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft
ein


      a) Computerimplementiertes Analysesystem mit einer Einrichtung zum
         b) Spezifizieren eines Klassennetzes,
         c) Spezifizieren einer Prozessierungshierarchie,
         d) Erfassen von Pixelwerten eines Zellkomponenten beinhaltenden Z-Stapels,


            d1) wobei bestimmte der Zellkomponenten unter Verwendung der
            Fluoreszenz-in situ Hybridisierung (FlSH) als Markierungsverfahren
            markiert sind, und

                                          -4-



              d2) der Z-Stapel aus mehreren Schnittbildern eines Konfokalmikroskops erzeugt ist;


              d3) wobei Schnittbilder und deren Pixelwerte von einem Gewebe
              dreidimensional erzielt sind,


           e) Erzeugen eines Datennetzes auf der Grundlage des Klassennetzes
           und der Prozessierungshierarchie;


           f) Klassifizieren von dreidimensionalen Objekten des Datennetzes als
           Bildartefakte, wenn eine Bedingung an ihr Volumen zutrifft; und


           g) Zählen der markierten Zellkomponenten unter Verwendung derjenigen
           dreidimensionalen Objekte des Datennetzes, die als Zellkomponenten
           klassifiziert sind.


Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.


                                              II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da der Gegenstand des Patentanspruchs 1
nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1
PatG).


1.       Die Patentanmeldung betrifft das Lokalisieren von spezifizierten Bildstrukturen in digitalen Bildern, insbesondere ein computerimplementiertes System zum
automatischen Identifizieren und Quantifizieren von zellulären Strukturen, die zum
Beispiel unter Verwendung von Fluoreszenz-in situ-Hybridisierung bzw. FISH
markiert worden sind (Offenlegungsschrift Abs. [0001]).

                                        -5-



Systeme zum Erfassen und Analysieren von Zielmustern in digitalen Bildern würden unter anderem verwendet, um in biomedizinischen Bildern, etwa aus der konfokalen Mikroskopie, Zielmuster wie Organellen, Membranen, Zellkerne, Gene,
Chromosomen und Makromoleküle zu analysieren. In der biomedizinischen Forschung werde das konfokale Laserrastermikroskop (LSCM) hauptsächlich zum
Abbilden von Zellen und Zellkomponenten verwendet, die mit Biomarkern, etwa
Fluoreszenzsonden, markiert worden seien; hierbei könnten in situ-Hybridisierungs- und Fluoreszenz-Techniken, etwa Fluoreszenz-in situ-Hybridisierung bzw.
FISH, verwendet werden, um DNA- und RNA-Sequenzen in Chromosomen zu
untersuchen und um Zellkomponenten, wie Chromosome und Gene, zu analysieren (Offenlegungsschrift Abs. [0002], [0003]).


In einer spezifischen Anwendung werde FISH verwendet, um das Her-2/neu-Gen
in Brustbiopsien zu analysieren und dadurch eine Diagnose- und Prognosemöglichkeit für Brustkrebs zur Verfügung zu stellen. Unter Verwendung von konfokaler
Mikroskopie in Kombination mit FISH berechne ein Pathologe das Ausmaß der
Genamplifizierung als Grundlage für die Diagnose. Hierbei zähle der Pathologe in
mindestens einhundert Zellen manuell die markierten Chromosomen und Gene
(Fluoreszenzsignale) und berechne danach die Verhältnisse der Gene zu den
Chromosomen. Bei diesem manuellen Verfahren könnten Fehler aufgrund von
Ermüdung und Konzentrationsverlust auftreten; zudem sei die Beurteilung, ob ein
Fluoreszenzsignal ein einzelnes Gen oder mehrere überlappende Gene darstelle,
häufig subjektiv (Offenlegungsschrift Abs. [0004]).


Daher sei ein automatisiertes System zum Zählen von Fluoreszenzsignalen erwünscht, die mittels der FISH-Technik erzielt werden. Bestehende automatisierte
Zählsysteme zählten Fluoreszenzsignale auf der Grundlage von zweidimensionalen Bildern. Selbst in bestehenden Systemen, die dreidimensionale Daten aus der
konfokalen Mikroskopie verarbeiteten, werde die dreidimensionale Information zu
zweidimensionalen Bildern komprimiert und diese analysiert, was zu einem Verlust
an dreidimensionaler Information führe. Es sei schwierig, in solchen komprimierten

                                       -6-



Bildern einzelne Zellen und andere Zellkomponenten zu unterscheiden. Fluoreszenzsignale, die andere Signale berührten oder mit diesen überlappten, könnten
nicht genau gezählt werden. Zusätzlich gehe die Information bezüglich der Distanz
zwischen den Signalen und der Größe der einzelnen Signale verloren.
(Offenlegungsschrift Abs. [0005]).


Der Anmeldung soll demgegenüber die Aufgabe zu Grunde liegen, ein computerimplementiertes Verfahren, ein Computerprogrammprodukt und ein computerimplementiertes Analysesystem zum automatischen Zählen von Fluoreszenzsignalen zu schaffen, die dreidimensional in zum Beispiel unter Verwendung der
FISH-Technik erzielten Schnittbildern vorhanden sind (Offenlegungsschrift Abs.
[0006]).


Gemäß dem nunmehr geltenden Patentanspruch 1 sollen 3D-Bilddaten (vorliegend als z-Stapel) analysiert werden, die von einem Zellen enthaltenden, mit
einem bestimmten Fluoreszenz-Markierungsverfahren (FISH) markierten Gewebe
mit Hilfe eines Konfokalmikroskops aufgenommen wurden (Merkmale a), d), d1),
d2), d3)).
Hierbei werden ein Klassennetz und eine Prozessierungshierarchie verwendet, die
spezifiziert werden müssen (Merkmale b), c)); vgl. Fig. 10 mit Beschreibung. Das
Klassennetz definiert die Charakteristika von Objekten, die als verschiedene Zellkomponenten klassifiziert werden. Die Prozessierungshierarchie beinhaltet Prozessierungsschritte, die den Fluss der Analysen und Berechnungen steuern, die
an den Pixelwerten und Objekten vorgenommen werden (Abs. [0078]). Auf der
Grundlage der Messdaten (Pixelwerte von z-Schnittbildern), des Klassennetzes
und der Prozessierungshierarchie wird ein Datennetz (mit klassifizierten Objekten)
erzeugt (Merkmal e); Abs. [0078]); es kann auch weitere Daten beinhalten, etwa
Daten eines Patienten (ursprünglicher Anspruch 20).
Im Laufe der Analyse werden Pixel dreidimensionalen Objekten zugeordnet, die
Zellen oder Zellkomponenten darstellen können. Abhängig von ihrem Volumen
werden Objekte als Bildartefakte klassifiziert (Merkmal f)). Die als Zellkomponen-

                                         -7-



ten (z. B. Zellkernmembranen, Zentromere oder Gene) klassifizierten Objekte des
Datennetzes werden gezählt (Merkmal g); Abs. [0084]).
Die Spezifizierung der Netze erfolgt durch den Anwender, vgl. Fig. 13 mit Beschreibung, insbesondere das Spezifizieren des Klassennetzes, mit Definitionen,
Eigenschaften, Zugehörigkeitskriterien usw. von Klassen (Abs. [0090] ff, Fig. 14
und 15) und das Spezifizieren der Prozessierungshierarchie mit Vorgabe von Prozessierungsschritten mit Domänen (Klassen, die Objekte des Datennetzes definieren) und Algorithmen, etc. (Abs. [0097] ff, Fig. 16 und 18). Der Anmelder gibt auch
Verknüpfungen zwischen Klassen, Prozessierungsschritten und Objekten vor; das
Datennetz wird dann durch Verknüpfen von Tabellendatenwerten (entsprechend
Messwerten) mit Objekten auf der Grundlage des Klassennetzes und der Prozessierungshierarchie erzeugt (Fig. 13 Schritte 56 und 58, Abs. [0109] ff, Abs. [0119]).


Als Fachmann sieht der Senat hier einen in der Entwicklung von Prozessierungsnetzwerken erfahrenen Ingenieur der Fachrichtung Informatik an, der auch Kenntnisse in der Bildanalyse, insbesondere von mikrobiologischen Proben besitzt oder
hierfür einen weiteren Experten mit Erfahrung in der medizinischen Bildverarbeitung zu Rate zieht.


2.     Das Analysesystem des geltenden Anspruchs 1 ist nicht patentfähig, da es
nicht auf erfinderischer Tätigkeit beruht.


Dieses Verfahren war nämlich angesichts des Standes der Technik und im Lichte
seines Fachwissens für den Fachmann naheliegend.
Hierbei sind diejenigen Merkmale nicht zu berücksichtigen, welche nicht die
Lösung eines technischen Problems mit technischen Mitteln bestimmen oder
beeinflussen, vgl. den Aufsatz Meier-Beck, GRUR 2011, 857-867, I.1, I.4.e: „...
das vom Gesetzgeber mit den Ausschlusstatbeständen verfolgte Anliegen [wird]
nach der neueren BGH-Rechtsprechung – nicht anders als nach der Rechtsprechung der Technischen Beschwerdekammern des EPA – im Wesentlichen
dadurch verwirklicht [...], dass jedenfalls bei der Prüfung einer Erfindung auf

                                        -8-



erfinderische Tätigkeit nur diejenigen Anweisungen berücksichtigt werden, die die
Lösung des technischen Problems mit technischen Mitteln bestimmen oder
zumindest beeinflussen“ (mit Zitierungen). Im vorliegenden Fall sind für diese
Betrachtung insbesondere die Ausschlusstatbestände der Pläne, Regeln und Verfahren für gedankliche Tätigkeiten sowie der Programme für Datenverarbeitungsanlagen (§ 1 Abs. 3 Nr. 3 iVm Abs. 4 PatG) relevant.


Aus der Druckschrift D2 ist ein computerimplementiertes Verfahren (und ein entsprechendes System) zur 3D-Volumenanalyse der Fluoreszenzverteilung in Zellkernen bekannt, wobei mit einem konfokalen Mikroskop als Schnittbilder eines z-Stapels aufgenommene dreidimensionale Fluoreszenzdaten analysiert werden (S.
189 re. Sp. vorle. Abs. Mitte) – Merkmale a), d), d2), d3), teilweise d1). Nach einer
ersten Korrektur von Artefakten (S. 190 li. Sp. Kap. „Preprocessing“ erster Absatz)
werden die im Datensatz enthaltenen Objekte anhand ihrer Voxelwerte segmentiert und markiert (S. 191f Kap. „Processing“ mit den Unterkapiteln „Object
segmentation“ und „Labeling“). Während der Markierung eines Objekts wird auch
dessen Größe (Volumen) berechnet; Objekte außerhalb eines bestimmten Größenbereichs werden eliminiert, d. h sie werden von der weiteren Bearbeitung ausgeschlossen (S. 192 li. Sp. Abs. 1, insbesondere „The user sets a size range in
which objects are kept and labeled (objects outside this size range are
eliminated)“). Damit ist Merkmal f) erfüllt (es kommt nicht darauf an, ob man diese
Bereiche explizit Bildartefakte nennt oder nicht, jedenfalls werden sie nicht weiter
analysiert), mit Ausnahme der Angabe, dass es sich um Objekte eines Datennetzes handelt. Danach wird für alle Voxel eines Objekts deren Entfernung vom
Objektmittelpunkt (in einer „distance map“) berechnet (Zwiebelschalenmodell),
auch dreidimensional, und auf das Objekt werden morphologische Operationen
angewendet, um es zu glätten und von Nachbarobjekten zu trennen (Kap.
„Distance encoding and morphological operations“, insbesondere S. 192 re. Sp.
vorle. Abs. „onion skin“, S. 193 re. Sp. „extension to the third dimension“, S. 195
li. Sp. „Morphological operations ...“). Das Verfahren wird auf menschliche Zellen
angewendet, um die Verteilung der DNA-Replikationsfoki in 3D-Zellkernvolumina

                                        -9-



zu bestimmen; hierbei werden ein DNA-Kernvolumen und innerhalb dessen die
DNA-Foki segmentiert (Kap. „Biological application“ auf S. 195). Insgesamt wird
somit aus den Messdaten mit Hilfe einer Folge geeigneter Prozessierungsschritte
eine Datenstruktur mit markierten, unterschiedlichen Objektklassen (DNA-Replikationsfoki und DNA-Kernvolumen als Hintergrund) zugeordneten Voxeln erzeugt
– teilweise Merkmal e). Die markierten, klassifizierten Zellkomponenten (DNA-Replikationsfoki) werden gezählt (S. 195 re. Sp. Abs. 2, insbesondere „For each
level surface of the distance map (Ddv), the number of object voxels (Bdv) was
counted … In addition, the size of each object (replication foci) was calculated ...“)
– Merkmal g) mit Ausnahme der Angabe, dass es sich um Objekte eines Datennetzes handelt.
Zudem ist in D2 angegeben, dass die verschiedenen Werkzeuge für viele biologische Anwendungen nutzbar sind (S. 198 re. Sp. le. Satz). Eine Anwendung des
Fluoreszenzmarkierungen auswertenden Verfahrens auf FISH-markierte Zellen
lag damit vor dem Anmeldetag der vorliegenden Anmeldung im Griffbereich des
Fachmanns – restlicher Teil des Merkmals d1).


Durch die im geltenden Anspruch 1 aufgeführten Komponenten Klassennetz, Prozessierungshierarchie und Datennetz wird ein allgemeines Gerüst bereitgestellt,
eine Art organisatorischer Überbau, der in weiten Grenzen ausgestaltet werden
kann, in den beliebige Algorithmen und Daten eingefügt und beliebig verknüpft
werden können (vgl. auch den letzten Absatz der Beschreibung, wonach die
Erfindung in unterschiedlichen Bereichen einsetzbar ist). Konkrete Ausgestaltungen (insbesondere Algorithmen zur Datenanalyse) sind nicht angegeben, dies
bleibt dem Anwender überlassen. Dieser muss das Klassennetz und die Prozessierungshierarchie spezifizieren und einen hierzu passenden Aufbau des Datennetzes vorgeben, d. h. er muss einen grob vorgegebenen organisatorischen
Rahmen mit Inhalt füllen. Vgl. hierzu das oben zum Gegenstand der Anmeldung
Ausgeführte.

                                        - 10 -



Die Vorgaben „Klassennetz“, „Prozessierungshierarchie“ und „Datennetz“ lösen
allenfalls organisatorische Probleme, tragen jedoch nicht zur Lösung eines technischen Problems aus dem Problemkreis „Auswertung von Messdaten“ bei.


Das Spezifizieren des Klassennetzes und der Prozessierungshierarchie und
ebenso Vorgaben für das Erzeugen eines Datennetzes beruhen auf der gedanklichen Tätigkeit des Anwenders, nicht auf dem Einsatz beherrschbarer Naturkräfte
zur Erreichung eines kausal übersehbaren Erfolgs, und tragen nicht zur Lösung
eines technischen Problems mit technischen Mitteln bei.


Zudem ist eine mögliche Beschleunigung der Datenauswertung (was evtl. als
Lösung eines technischen Problems angesehen werden könnte) nur dann zu
erreichen, wenn der Anwender das Organisationsgerüst in geeigneter Weise
spezifiziert und dessen einzelne Bestandteile (Algorithmen, Verknüpfungen …) in
geeigneter Weise vorgibt; das allgemeine Gerüst selbst trägt nicht zur Lösung
dieser Aufgabe bei.


Damit tragen die Merkmale b), c), die restlichen, die Netzstruktur und Hierarchie
betreffenden Teile des Merkmals e) sowie die Angabe „Objekte des Datennetzes“
in den Merkmalen f) und g) nicht zur Lösung eines technischen Problems mit
technischen Mitteln bei und sind nach ständiger Rechtsprechung bei der Beurteilung der erfinderischen Tätigkeit nicht zu berücksichtigen.


Wie oben ausgeführt, waren die übrigen Anspruchsmerkmale durch D2 nahegelegt.


Das System des Anspruchs 1 beruht somit nicht auf erfinderischer Tätigkeit.


Anspruch 1 ist demnach nicht gewährbar.

                                       - 11 -



3.     Auch die übrigen Patentansprüche sind nicht gewährbar, da über einen
Antrag nur einheitlich entschieden werden kann (BGH in GRUR 1997, 120
„Elektrisches Speicherheizgerät“).




                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
        Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
        Befangenheit mit Erfolg abgelehnt war,
     einem Beteiligten das rechtliche Gehör versagt war,
     ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
        sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
     der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
        die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
        sind, oder
     der Beschluss nicht mit Gründen versehen ist.

                                   - 12 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek               Eder          Dr. Thum-Rung            Dr. Forkel




                                                                        Me
