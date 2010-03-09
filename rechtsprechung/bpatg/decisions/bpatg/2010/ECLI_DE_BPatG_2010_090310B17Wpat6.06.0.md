---
ecli: "ECLI:DE:BPatG:2010:090310B17Wpat6.06.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 6/06"
decided: "2010-03-09"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2010&Sort=1&Seite=18&nr=16437&anz=1397&pos=270&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2010-03-09_17_W-pat_6_06_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0100.md"]
---

# Bundespatentgericht, 17 W (pat) 6/06 vom 2010-03-09

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 6/06                                                           Verkündet am
_______________                                                             9. März 2010
    (Aktenzeichen)                                                               …




                                BESCHLUSS

                              In der Beschwerdesache


                 betreffend die Patentanmeldung 196 26 775.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 9. März 2010 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Fritsch,   des   Richters   Dipl.-Ing. Prasch    sowie   der
Richterinnen Eder und Dipl.-Phys. Dr. Thum-Rung


beschlossen:


                        Die Beschwerde wird zurückgewiesen.




BPatG 154
08.05

                                        -2-



                                     Gründe


                                         I.


Die vorliegende Patentanmeldung ist am 3. Juli 1996 beim Deutschen Patent- und
Markenamt unter der Bezeichnung


                         „Schnelle Faltung von Projektionen“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 12. Oktober 2005
die Anmeldung zurückgewiesen, da das beanspruchte Verfahren nicht auf technischem Gebiet liege und deshalb keine patentfähige Erfindung sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Anmelderin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte Patent
       mit folgenden Unterlagen zu erteilen:
       Patentanspruch vom 29. November 2005, eingegangen am 30. November 2005,
       Beschreibung Seiten 1 und 1a vom 18. April 1997, eingegangen am
       23. April 1997,
       Beschreibung Seiten 2 bis 16 vom Anmeldetag,
       15 Blatt Zeichnungen mit Figuren 1 bis 8, 10 bis 18 vom 12. Mai 1997, eingegangen am 15. Mai 1997,
       1 Blatt Zeichnung mit Figur 9 vom 4. Juni 1997, eingegangen am
       9. Juni 1997.

                                       -3-



Sie regt die Zulassung der Rechtsbeschwerde an zur Frage der Technizität.


Die Anmelderin vertritt die Auffassung, dass das beanspruchte Verfahren für die
Bildrekonstruktion für ein Computertomographiegerät zur Durchführung einer
schnellen Faltung auf technischem Gebiet liege; es erfülle keinen der in § 1 Abs. 3
und 4 PatG aufgezählten Ausschlusstatbestände und sei dem Patentschutz prinzipiell zugänglich. Das Verfahren diene der Gewinnung von rekonstruierten Daten
aus in einem (zweifellos technischen) Computertomographiegerät gemessen
Daten. Dem Verfahren liege auch eine technische Problemstellung zugrunde: Die
Berechnung der bei der Rekonstruktion erforderlichen Faltung benötige sehr viel
Rechenzeit, die durch das vorgeschlagene Verfahren stark reduziert werde.
Zudem würden bei einer gegebenen Hardware die Fehler im rekonstruierten Bild
verringert. Das Verfahren berücksichtige Eigenschaften der Messdaten, nämlich
dass die einzelnen, mit einem Filterkern zu faltenden Projektionen einander ähnlich sind und am Rand sehr geringe Werte aufweisen; dies erlaube eine Wahl
geringer Transformationslängen, ohne dass die entstehenden Überfaltungsfehler
zu groß würden. Der Fachmann müsse sich mit den technischen Gegebenheiten
eines Computertomographiegeräts auseinandersetzen, nämlich mit der Größe des
Messfeldes, der Anzahl der Messkanäle sowie der Anzahl derjenigen Messkanäle,
die unter Anforderungen an die Qualität der rekonstruierten Bilder zu einer geringfügig verfälschten Bildinformation im Außenbereich der Bilder beitragen dürfen.
Außerdem seien technische Überlegungen erforderlich bei der Wahl des Filterkerns. Deshalb sei anzuerkennen, dass dem Verfahren nach dem Patentanspruch
technischer Charakter zukomme. Zu dieser Problematik weist die Anmelderin auf
die Entscheidungen des Bundesgerichtshofs „Suche fehlerhafter Zeichenketten“
vom 17. 10. 2001 - X ZB 16/00 - sowie des Bundespatentgerichts „Computertomograph“ vom 22. 7. 1986 - 21 W (pat) 84/83 hin.

                                       -4-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


        D1: GONZALEZ, R.C.; WOODS, R.E.: Digital Image Processing.
        Addison-Wesley, Reading u. a., 1992, S. 100 - 128.


        D2: VASSILIADIS, K.P. u. a.: Reconstruction of Magnetic Resonance
        Images Using One-Dimensional Techniques. IEEE Transactions on Medical Imaging, Vol. 12, No. 4, Dec. 1993, S. 758 - 763.


Vom Senat wurde zusätzlich die Druckschrift


        D3: DE 35 09 777 C2


eingeführt.


Der geltende Patentanspruch lautet:


        „Verfahren für die Bildrekonstruktion für ein Computertomographiegerät
        zur Durchführung einer schnellen Faltung mit der Transformationslänge M
        unter Zulassung geringer Überfaltungsfehler, wobei jeweils p (oder 2p) von
        n mit dem Computertomographiegerät gemessenen Projektionen der
                                                      ^
        Länge N mit einem modifizierten Filterkern h (k) unter Verwendung der
        „Fast Fourier Transform“ (FFT) und der „Inverse Fast Fourier Transform“
        (IFFT) gleichzeitig in einem Schritt gefaltet werden, umfassend folgende
        Schritte:


        a) Zusammenfassung der p Projektionen der Länge N zu einem Vektor
        und Anfügung von S Nullen hinter jeder der p Projektionen der Länge N zu
        einem Vektor

                                        -5-



               p
     υ (k) =      υi (k-(i-1) (N+S) )                         (1)
               i=1


mit der Transformationslänge M,


b) Wahl der Parameter p und S derart, daß die Transformationslänge


     M = p (N+S) = 2m                                         (2)


zur Durchführung der schnellen Faltung eine Zweierpotenz ist,


                                 ^
c) Entwurf des Filterkerns h (k) im Ortsbereich derart, daß er wenigstens
im wesentlichen gleich einer Länge N+S ist, und Auffüllen des Filterkerns h^ (k) mit Nullen auf die Transformationslänge M gemäß


                       h(k) für Ikl < (N+S)/2
        ^
       h (k) =                                                (3)

                       0      sonst


d) Zyklische Durchführung der schnellen Faltung mit der Transformationslänge M gemäß


                       ^                              ^
     y(k) = υ (k) M h (k) = IFFT { FFT{ υ (k) } FFT{ h (k) } } (4)


     mit              k = 0 (1) (M-1) ,


wobei das Faltungsergebnis einer Projektion i die Form


     yi (k) = y (k + (i-1) (N+S))                             (5)

                                          -6-



             mit           k = 0 (1) (N-1)      und
                           i = 1 (1) p


        aufweist.“


Gemäß Seite 3 Absatz 4 der Anmeldeunterlagen soll der Anmeldung die Aufgabe
zugrunde liegen, ein Verfahren der eingangs genannten Art derart auszubilden,
dass der auftretende Fehler im rekonstruierten Bild verringert und die Rechenzeit
für die schnelle Faltung verkürzt wird.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie konnte jedoch keinen
Erfolg haben, da der Gegenstand des Patentanspruchs gemäß § 1 PatG dem
Patentschutz nicht zugänglich ist.


1.   Hintergrund der Anmeldung ist der Bereich der Computertomographie, vgl.
S. 1 Abs. 1 und 2 sowie Fig. 3 mit Beschreibung. In einem Computertomographiegerät wird ein Objekt (z. B. ein Patient P) mit Röntgenstrahlen (Strahlungsquelle 3
in Fig. 3) durchleuchtet, mit Hilfe von Detektoren (Detektorarray 5 in Fig. 3) werden unter unterschiedlichen Winkeln Messwerte gemessen, vgl. S. 1 Abs. 2 sowie
Fig. 3 mit Beschreibung. Zur Rekonstruktion des Bildes (d. h. der räumlichen Verteilung von physikalischen Schwächungswerten im untersuchten Objekt) werden
die ermittelten Projektionen verschiedenen mathematischen Operationen unterzogen, unter Anderem werden sie zur Verbesserung der Bildschärfe mit einem Filterkern gefaltet. Dies entspricht im Wesentlichen einer Hochpassfilterung; auf S. 16
le. Abs. sind verschiedene bekannte Filterkerne namentlich aufgeführt. Die mathematische Faltungsoperation ist zeitkritisch, sie muss schnell durchgeführt werden,

                                       -7-



damit das berechnete Bild unmittelbar nach der Messung bereitgestellt werden
kann.


In der Anmeldung geht es um eine Methode zur schnellen Durchführung der
mathematischen Faltung. Eine Faltung eines Vektors mit einem Filterkern kann
bekanntermaßen mit Hilfe schneller Fouriertransformation, Multiplikation mit der
Fouriertransformierten des Filterkerns und Rücktransformation durchgeführt werden, wobei die Transformationslänge auf eine Zweierpotenz M (unter Einfügung
von Nullen) aufgerundet wird; dies kann zu hohen Rechenzeiten führen, vgl. die
Ausführungen zum Stand der Technik auf S. 1 le. Abs. bis S. 2 Abs. 2. Wird die
Zweierpotenz M kleiner gewählt als für eine fehlerfreie Faltung erforderlich, so
reduziert sich die Rechenzeit. Jedoch ergeben sich Überfaltungsfehler, die je nach
Wahl von M ein nicht tolerierbares Ausmaß annehmen können, vgl. S. 2 le. Abs.
und S. 3 Abs. 1 und 3.


Die Anmeldung lehrt demgegenüber, die Vektorwerte mehrerer einzelner Projektionen hintereinander in einem Gesamtvektor anzuordnen, der insgesamt die
Länge einer Zweierpotenz hat, wobei zwischen je zwei Einzelvektoren eine
Anzahl S von Nullen eingefügt werden; dieser Gesamtvektor wird mit dem Filterkern gefaltet. Die Einschränkung der Transformationslänge auf eine Zweierpotenz
gilt dann nur für den Gesamtvektor, nicht für die einzelnen Projektionsvektoren, so
dass zumindest für bestimmte Längen der Einzelvektoren weniger Rechenoperationen nötig sind als bei einer getrennten Faltung für jeden Einzelvektor, vgl. S. 5
Z. 4 bis 10.
Je nach Wahl der Anzahl S von einzufügenden Nullen und der Länge des Filterkerns können sich unterschiedliche Faltungsfehler ergeben, wobei ein relativ kurzer Abstand S zwischen den einzelnen Projektionen im Gesamtvektor durch einen
ebenfalls etwas zu kurz gewählten Filterkern teilweise kompensiert werden kann,
vgl. S. 5 bis S. 7 Abs. 1 i. V. m. Fig. 2 und 5. Insbesondere entstehen im
Fall S   N-1 bei geeignet gewählter Länge des Filterkerns keine Fehler; im
Fall S < N-1 entstehen Überfaltungsfehler, da in eine gefaltete Projektion fälschli-

                                         -8-



cherweise Randwerte der Nachbarprojektion eingehen, und zwar umso mehr, je
kleiner S ist, vgl. S. 5 Z. 16 bis 36.
Der Algorithmus wird auf einem (üblichen) Rechner (8 in Fig. 3) durchgeführt; es
ist keine an den Algorithmus angepasste spezielle Rechnerarchitektur ausgewiesen.


2.     Als Fachmann sieht der Senat hier einen Mathematiker oder Physiker mit
Erfahrung in der Entwicklung von Algorithmen an, wie sie etwa in der Bilddatenverarbeitung eingesetzt werden.


Ein solcher Fachmann entnimmt dem Patentanspruch die Modifikation eines an
sich bekannten mathematischen Algorithmus zur Faltung mehrerer Vektoren (Projektionen) einer vorgegebenen Länge N mit einem Filterkern. Durch geschickte
Zusammenfassung und Anordnung der Eingangsdaten und Operationsschritte
sowie geeignete Wahl verschiedener Parameter (Transformationslänge M, Anzahl p der zusammengefassten Vektoren, Anzahl S der einzufügenden Nullen,
Länge des Filterkerns) wird die Anzahl der für die Faltung durchzuführenden
Rechenschritte reduziert. Den „Entwurf des Filterkerns“ gemäß Merkmal c) interpretiert der Fachmann in der Weise, dass ein Filterkern, dessen grundsätzliche
Form in Gestalt einer mathematischen Funktion (im Wesentlichen beliebig) vorgebbar ist, hinsichtlich seiner Dimension in für die Faltung mathematisch sinnvoller
Weise an vorgegebene und an gewählte Parameter angepasst wird. Die Faltung
soll „unter Zulassung geringer Überfaltungsfehler“ durchgeführt werden. Da der
Anspruch jedoch die Transformationslänge M und die Anzahl S der einzufügenden
Nullen nicht nach oben beschränkt, umfasst er auch die in den Anmeldeunterlagen
auf S. 5 Z. 16 bis 24 angesprochene Parameterwahl ohne Überfaltungsfehler (S   N-1, wobei die Länge des Filterkerns von ungefähr N+S zwischen 2N-1
und 2S+1 liegt).


Als dem beanspruchten Verfahren objektiv zugrunde liegende Aufgabe ist die
Reduzierung der Anzahl der Rechenschritte und damit der zur Durchführung

                                       -9-



benötigten Rechenzeit anzusehen; eine Verringerung von Bildfehlern gegenüber
bekannten Verfahren, die bei geeigneter Parameterwahl ohne Überfaltungsfehler
arbeiten, leistet das Verfahren gemäß dem Patentanspruch nicht.


Es erscheint glaubhaft, dass die Berechnung mit dem anmeldungsgemäßen Algorithmus schneller durchgeführt werden kann als mit einem vorbekannten Faltungsalgorithmus.


3.   Das Verfahren nach dem Patentanspruch ist jedoch nicht patentfähig, da es
als mathematische Methode als solche gemäß § 1 Abs. 3 und 4 PatG vom Patentschutz ausgeschlossen ist.


a)   Nach der Rechtsprechung des Bundesgerichtshofs ist ein Verfahren, das
sich zur Herbeiführung des angestrebten Erfolges eines Programms bedient, mit
dessen Hilfe eine Datenverarbeitungsanlage so gesteuert wird, dass der gewünschte Erfolg erzielt wird, nicht schon wegen des Vorgangs der elektronischen
Datenverarbeitung dem Patentschutz zugänglich. Die beanspruchte Lehre muss
vielmehr Anweisungen enthalten, die der Lösung eines konkreten technischen
Problems mit technischen Mitteln dienen. Nichts anderes gilt, wenn in Rede steht,
ob eine beanspruchte Lehre als mathematische Methode als solche anzusehen
ist, vgl. BGH in GRUR 2005, 143, 144 - Rentabilitätsermittlung, m. w. N.; vgl. auch
BGH in GRUR 2009, 479 - „Steuerungseinrichtung für Untersuchungsmodalitäten“, m. w. N.


Im Verfahren nach dem Patentanspruch können keine Anweisungen erkannt werden, die der Lösung eines konkreten technischen Problems mit technischen Mitteln dienen.


Der Patentanspruch schlägt vor, einen mathematischen Algorithmus durch geschickte Zusammenfassung und Anordnung der Eingangsdaten und Operationsschritte sowie geeignete Wahl verschiedener Parameter so zu verändern, dass die

                                       - 10 -



Anzahl der durchzuführenden Rechenschritte und damit die Rechenzeit reduziert
wird.
Der Patentanspruch enthält jedoch keine Anweisungen zur Modifikation von technischen Mitteln oder zur Kompensation von Unzulänglichkeiten, die sich aus der
Gestaltung solcher Mittel ergeben. Weder wird ein Computertomographiegerät,
welches der dem beanspruchten Verfahren vorgelagerten Datenaufnahme dient,
in irgendeiner Weise verändert, noch wird eine zur Durchführung des Verfahrens
eingesetzte Vorrichtung (Datenverarbeitungsanlage, Prozessor) modifiziert. In der
Optimierung allein eines mathematischen Algorithmus kann keine technische Leistung erkannt werden, vgl. die Entscheidung des Senats vom 18. 1. 2007
- 17 W (pat) 16/04.
Der Anspruch lässt zudem eine exakte Berechnung der Faltung ohne Fehler zu
und beinhaltet keine Einschränkung, die zu Überfaltungsfehlern führen würde, vgl.
das oben unter II.2 Ausgeführte. Insbesondere enthält er keine Anweisungen
dahingehend, wie unter Berücksichtigung spezieller, auf technische Gegebenheiten zurückzuführender Eigenschaften der Messdaten Verfahrensparameter zu
wählen sind, so dass Fehler zwar auftreten (was den Algorithmus schneller
macht), sich jedoch in einem tolerierbaren Rahmen halten, und löst damit auch
kein entsprechendes Problem.


b)      Etwas anderes ergibt sich auch nicht aus der Entscheidung des Bundesgerichtshofs „Logikverifikation“ (vgl. BlPMZ 2000, 273), in welcher die Zugänglichkeit
zum Patentschutz bejaht wurde für einen Zwischenschritt in einem Prozess, der
mit der Herstellung von Chips endete. In diesem Zwischenschritt wurde lediglich
von einer bestimmungsgemäß eingesetzten Datenverarbeitungsanlage Gebrauch
gemacht, ohne diese in irgendeiner Weise zu verändern. Dem Zwischenschritt
wurde technischer Charakter zugestanden, da die ihm zugrunde liegende Lehre
geprägt war von auf technischen Überlegungen beruhenden Erkenntnissen und
deren Umsetzung.

                                      - 11 -



Im vorliegenden Fall beruht dagegen die beanspruchte Lehre lediglich auf mathematischen Überlegungen. Insbesondere ergibt sich die Wahl von Parametern einschließlich der Dimensionierung des Filterkerns lediglich aus mathematischen
Überlegungen zur Durchführung der Faltung vorgegebener Eingangsdaten (Projektionen bestimmter Länge N) mit einem in seiner grundsätzlichen mathematischen Form vorgebbaren Filter; darüber hinausgehende Eigenheiten, etwa in Gestalt einer speziellen Anpassung des Filterkerns an physikalisch-technische Gegebenheiten der Datenaufnahme oder des untersuchten Objekts sind dem Anspruch
nicht zu entnehmen. Auch sonst war eine Auseinandersetzung mit technischen
Sachverhalten wie oben erwähnt nicht erforderlich.


c)   Die Anmelderin ist der Ansicht, dass das beanspruchte Verfahren nach der
Entscheidung „Suche fehlerhafter Zeichenketten“ auf technischem Gebiet liege, da
der Bundesgerichtshof dort der Aufarbeitung von Messergebnissen technischen
Charakter zugestanden habe.


Wie in den Gründen der Entscheidung „Suche fehlerhafter Zeichenketten“ (GRUR
2002, 143-146) unter B.III.1.bb) ausgeführt wird, kann ein Programm patentiert
werden, wenn es in technische Abläufe eingebunden ist, etwa dergestalt, dass es
Messergebnisse aufarbeitet.
Eine Einbindung in einen technischen Ablauf ist nach der Rechtsprechung des
Bundesgerichtshofs unverzichtbarer Bestandteil einer solchen als technisch anzusehenden Lehre. Dies wird besonders deutlich in der Entscheidung des Bundesgerichtshofs „Tauchcomputer“ (GRUR 1992, 430, X ZR 43/91 vom 4. Februar 1992), auf welche in der neueren Entscheidung des Bundesgerichtshofs
„Steuerungseinrichtung    für   Untersuchungsmodalitäten“,    X ZB 22/07    vom
20. 1. 2009 unter II.2.b) letzter Absatz im Zusammenhang mit der Aufarbeitung
von Messergebnissen explizit Bezug genommen wird.
Gegenstand der Entscheidung „Tauchcomputer“ war eine Anzeigeeinrichtung für
die Parameter eines Tauchgangs. Eine Lehre zum technischen Handeln wurde
vom Bundesgerichtshof darin gesehen, „dass mit einem Betrieb von Tiefen- und

                                     - 12 -



Zeitmesser, Datenspeicher, Auswerte- und Verknüpfungsstufe, Wandlereinrichtung sowie Anzeigemittel nach einer bestimmten Rechenregel (Programm oder
Denkschema) ermöglicht wird, mit Hilfe von Messgeräten ermittelte Messgrößen in
der Anzeigeeinrichtung automatisch ohne Einschaltung menschlicher Verstandestätigkeit anzuzeigen.“ (vgl. a. a. O., 430). Die Merkmale der Lehre umschrieben
eine enge Beziehung der Rechenregel mit (technischen) Mitteln wie Anzeige,
Speicher, Auswerte- und Verknüpfungsstufe, Wandler, Tiefen- und Zeitmesser.


Im Gegensatz hierzu ist im vorliegenden Fall kein konkreter Bezug auf technische
Mittel oder Abläufe erkennbar. In dem beanspruchten Verfahren werden keine
speziellen Eigenschaften der Messdaten berücksichtigt, die sich aus dem zur Aufnahme der Projektionsdaten verwendeten (zweifellos technischen) Computertomographiegerät bzw. -verfahren oder aus der physikalischen Struktur des vermessenen Objekts ergeben. Das beanspruchte Verfahren soll im Gegenteil nicht auf
die Computertomographie beschränkt, sondern auch auf andere Fälle anwendbar
sein, vgl. S. 15 le. Abs. bis S. 16 Abs. 1; angesichts des relativ allgemeinen
Patentanspruchs, der die Möglichkeit einer fehlerfreien Faltung von als Vektoren
gleicher Länge vorliegenden und ansonsten beliebigen Eingangsdaten mit einem
Filter im Wesentlichen beliebiger Form umfasst, sind entgegen dem Vorbringen
der Anmelderin sogar Anwendungen außerhalb der Verarbeitung von auf messtechnischem Wege gewonnenen Bilddaten denkbar.


Somit ist das beanspruchte Verfahren auch unter Berücksichtigung der Entscheidungen „Suche fehlerhafter Zeichenketten“, „Steuerungseinrichtung für Untersuchungsmodalitäten“ und „Tauchcomputer“ einem Patentschutz nicht zugänglich.


d)   Die Anmelderin weist außerdem auf die Entscheidung des Bundespatentgerichts „Computertomograph“ vom 22. 7. 1986 - 21 W (pat) 84/83 hin.


Gemäß der in ABl EPA 1988, 50 veröffentlichten Zusammenfassung wurde in dieser Entscheidung einem computergestützten Arbeitsverfahren technischer Charak-

                                       - 13 -



ter zugebilligt, bei dem das zur Durchführung benutzte Arbeitsmittel, nämlich ein
Computertomograph mit spezieller Auswerteschaltung, im Einzelnen angeführt
war, auch wenn das Arbeitsmittel durch das auf einer Berechnungsmethode beruhende allgemeine Prinzip umschrieben wurde.


Im vorliegenden Fall ist jedoch keine spezielle Ausbildung eines technischen Mittels, etwa eine spezielle Schaltung erkennbar. Auch aus dieser Entscheidung kann
somit nicht auf einen technischen Charakter der vorliegenden Lehre geschlossen
werden.


Nach alledem kann das Verfahren nach dem Patentanspruch nicht als Erfindung
im Sinne des § 1 PatG anerkannt werden.


4.   Die Anmelderin hat die Zulassung der Rechtsbeschwerde nach § 100 Abs. 2
PatG angeregt. Die Rechtsbeschwerde ist zuzulassen, wenn eine Rechtsfrage von
grundsätzlicher Bedeutung zu entscheiden ist oder die Fortbildung des Rechts
oder die Sicherung einer einheitlichen Rechtsprechung eine Entscheidung des
Bundesgerichtshofs erfordert.


Eine Rechtsfrage grundsätzlicher Bedeutung, über die noch keine Rechtsprechung des Bundesgerichtshofs vorliegt, wird mit der vorliegenden Anmeldung
nicht aufgeworfen. Insbesondere in den oben erwähnten Entscheidungen „Rentabilitätsermittlung“, „Logikverifikation“, „Suche fehlerhafter Zeichenketten“, „Steuerungseinrichtung für Untersuchungsmodalitäten“ und „Tauchcomputer“ hat der
Bundesgerichtshof die wesentlichen und auch für den vorliegenden Anmeldungsgegenstand relevanten Kriterien dargelegt, unter denen ein im Wesentlichen
mathematisches Verfahren als dem Patentschutz zugängliche Erfindung anerkannt werden kann. Eine vom vorliegenden Beschluss abweichende Rechtsprechung eines anderen Senats des Bundespatentgerichts ist nicht erkennbar.

                                 - 14 -



Die Anregung der Anmelderin auf Zulassung der Rechtsbeschwerde war daher
nicht aufzugreifen.




Dr. Fritsch           Eder                Prasch          Dr. Thum-Rung




                                                                     Fa
