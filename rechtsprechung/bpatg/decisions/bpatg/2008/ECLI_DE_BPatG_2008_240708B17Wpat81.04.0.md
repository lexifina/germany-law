---
ecli: "ECLI:DE:BPatG:2008:240708B17Wpat81.04.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 81/04"
decided: "2008-07-24"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2008&Sort=1&Seite=62&nr=10033&anz=1485&pos=935&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2008-07-24_17_W-pat_81_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0003.md"]
---

# Bundespatentgericht, 17 W (pat) 81/04 vom 2008-07-24

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 81/04                                                   Verkündet am
 _______________                                                    24. Juli 2008
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 197 44 898.4-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 24. Juli 2008 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Fritsch, der Richterin Dr. Mittenberger-Huber sowie des
Richters Dipl.-Ing. Baumgardt und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
08.05

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung ist am 10. Oktober 1997 unter Beanspruchung
der Priorität 97-4621 der Republik Korea vom 15. Februar 1997 beim Deutschen
Patent- und Markenamt unter der Bezeichnung


       „Signaladaptives Filterverfahren und signaladaptives Filter“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 2. Juni 2004 die
Anmeldung zurückgewiesen, da der Gegenstand des damals geltenden Patentanspruchs 1 vom 19. November 1999 nicht neu sei. Der Beschluss wurde am
22. Juni 2004 an die Anmelderin zugestellt.


Gegen diesen Beschluss wendet sich die am 19. Juli 2004 eingegangene Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:
       1. Patentansprüche 1 bis 7 übergeben in der mündlichen Verhandlung vom 24. Juli 2008,

                                        -3-



        2. noch anzupassende weitere Unterlagen (Beschreibung und
        Zeichnungen).


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist folgende
Druckschrift genannt worden:


        D1: EP 0 817 497 A2.


Im Beschwerdeverfahren wurden vom Senat zusätzlich die Druckschriften


        D2: D. Le Gall: „MPEG: a video compression standard for multimedia applications“, Communications of the ACM, April 1991, Vol.
        34 No. 4, S. 46-58


        D3: US 5 245 427


eingeführt.


Der in der mündlichen Verhandlung eingereichte, nunmehr geltende Patentanspruch 1 lautet:


     „1. Signaladaptives Filterverfahren zur Verringerung von Blockeffekten
     und Überschwingrauschen von Bilddaten, mit folgenden Schritten:


         a) Berechnung eines Gradienten der Bilddaten an jedem Pixel
              der Bilddaten;


         b) Vergleichen der Gradientendaten jedes Pixels mit einem globalen Schwellenwert (Tg), der auf der Grundlage eines vorbestimmten Quantisierungsschrittes (Q) eines Quantisierers fest

                               -4-



   gelegt wird, um eine globale Randabbildungsinformation der
   Pixel zu erzeugen;


c) Vergleichen der Gradientendaten jedes Pixels mit einem
   lokalen Schwellenwert (Tn), der für jeden Block festgelegt
   wird, der vorbestimmte Abmessungen aufweist, um eine lokale
   Randabbildungsinformation der Pixel zu erzeugen;


d) Durchführung einer OR-Operation mit der globalen Randabbildungsinformation, die in dem Schritt b) erzeugt wurde,
   und der lokalen Randabbildungsinformation, die in dem
   Schritt c) erzeugt wurde, zur Erzeugung binärer Randabbildungsinformation;


e) Anlegen eines Filterfensters mit vorbestimmten Abmessungen, um festzustellen, ob Ränder in dem Filterfenster vorhanden sind, auf der Grundlage der binären Randabbildungsinformation innerhalb des Filterfensters;


f) pixelweises Filtern der Pixelwerte des entsprechenden Filterfensters unter Verwendung vorbestimmter erster gewichteter Werte, um einen neuen Pixelwert zu erzeugen, wenn in
   dem Schritt e) festgestellt wird, daß Ränder nicht vorhanden
   sind; und


g) pixelweises   Filtern der   Pixelwerte des entsprechenden
   Filterfensters unter Verwendung vorbestimmter zweiter gewich

                                       -5-



           teter Werte, um einen neuen Pixelwert zu erzeugen, wenn in
           dem Schritt e) festgestellt wird, daß Ränder vorhanden sind,
           wobei das Filtern nicht durchgeführt wird, wenn der Pixel, der
           sich im Zentrum des Filterfensters befindet, einen Rand
           darstellt“.


Der geltende, nebengeordnete Patentanspruch 7 lautet:


       „7. Signaladaptives Filter, welches aufweist:


       eine Bildspeichereinheit zur temporären Speicherung dekomprimierter Bilddaten;


       eine Gradientenoperationseinheit zum Empfang der Bilddaten von
       der Bildspeichereinheit in Blockeinheiten mit vorbestimmten
       Abmessungen und zur Berechnung eines Gradienten der Bilddaten in Horizontalrichtung und Vertikalrichtung unter Verwendung
       von Gradientenoperatoren zum Auffinden von Randpixeln;


       einen globalen Randabbildungsgenerator zum Vergleichen der
       Gradientendaten jedes Pixels, die von der Gradientenoperationseinheit ausgegeben werden, mit einem globalen Schwellenwert (Tg), der auf der Grundlage eines Quantisierungsschrittes (Q)
       eines Quantisierers festgelegt wird, um binäre globale Randabbildungsinformation zu erzeugen;


       einen lokalen Randabbildungsgenerator zum pixelweisen Vergleichen der Gradientendaten, die von der Gradientenoperationseinheit ausgegeben werden, mit einem lokalen Schwellenwert, der individuell für jeden Block mit vorbestimmten Abmes-

                                       -6-



       sungen festgelegt wird, um binäre lokale Randabbildungsinformation zu erzeugen;


       ein OR-Gate, um pixelweise eine OR-Operation mit der globalen
       Randabbildungsinformation von dem globalen Randabbildungsgenerator und der lokalen Randabbildungsinformation von dem
       lokalen   Randabbildungsgenerator      durchzuführen,   um    binäre
       Randabbildungsinformation zu erzeugen;


       einen Filterselektor zum Speichern der binären Randabbildungsinformation, die von dem OR-Gate ausgegeben wird, und zum
       Klassifizieren der eingegebenen Bilddaten in einen Randbereich,
       der Information zumindest eines Randes einschließt, und in
       homogene Bereiche ohne Information in Bezug auf irgendwelche
       Ränder, entsprechend der binären Randabbildungsinformation;


       ein Mittlungsfilter zur Durchführung einer Mittlungsfilterung bei einem zentralen Pixel innerhalb eines Filterfensters eines Filterbereiches, wobei der Filterbereich als homogener Bereich durch
       den Filterselektor klassifiziert wurde, zur Erzeugung eines neuen
       Pixelwertes; und


       ein gewichtetes Filter zur Durchführung einer gewichteten Filterung mit dem zentralen Pixel innerhalb eines Filterfensters eines
       Filterbereichs, wobei der Filterbereich als Randbereich durch den
       Filterselektor klassifiziert wurde, zur Erzeugung eines neuen
       Pixelwertes.“


Der Anmeldung soll gemäß der Beschwerdebegründung vom 19. Oktober 2004,
S. 3 vorle. Abs. die Aufgabe zugrunde liegen, ein Verfahren und einen entsprechenden Filter zur Verminderung von Codierfehlern weiter zu verbessern.

                                        -7-



Zu den Einzelheiten wird auf die Akte verwiesen.


                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie ist jedoch nicht begründet, da der Gegenstand des Patentanspruchs 1 und ebenso der Gegenstand des
nebengeordneten Patentanspruchs 7 nicht neu sind (§ 1 Abs. 1 in Verbindung mit
§ 3 Abs. 1 und Abs. 2 Satz 1 PatG).


1.    Gegenstand der Anmeldung ist ein Filterverfahren und ein Filter, mit dem
Bilddaten, die mit einem Standard-Bildkodierverfahren (z. B. MPEG) komprimiert
und danach dekomprimiert wurden, und die demgemäß Artefakte (Blockeffekt,
Treppenrauschen und Überschwingrauschen, vgl. Anmeldeunterlagen S. 1 le. Abs.
bis S. 2 Abs. 2) aufweisen, gefiltert werden, um diese Artefakte zu verringern.


In dem beschriebenen Filterverfahren bzw. Filter werden zunächst die Positionen
im Bild bestimmt, an denen Kanten (in der Anmeldung als Ränder bezeichnet)
auftreten, d.h. Hell-Dunkel- oder Dunkel-Hell-Übergänge. Dies geschieht durch
Gradientenbildung für jedes Pixel und nachfolgenden Vergleich mit Schwellenwerten. Der jeweilige Gradientenwert wird mit einem globalen Schwellenwert Tg
verglichen und außerdem mit einem lokalen Schwellenwert für den Bilddatenblock,
in dem sich das betrachtete Pixel befindet. Ist der Absolutwert des Gradienten an
der jeweiligen Position größer als einer der Schwellenwerte, so wird das betrachtete Pixel als Kantenpixel klassifiziert. Nach der Bestimmung von Kanten im
Bild erfolgt eine Filterung jeweils in einem Filterfenster, wobei abhängig davon, ob
im Filterfenster Kantenpixel vorhanden sind oder nicht, unterschiedlich gefiltert
wird; ist der zentrale Pixel im Filterfenster ein Kantenpixel, so wird keine Filterung
durchgeführt.


Der globale Schwellenwert Tg wird hierbei gemäß dem geltenden Anspruch 1 „auf
der Grundlage eines vorbestimmten Quantisierungsschrittes (Q) eines Quanti-

                                        -8-



sierers“ und gemäß dem geltenden Anspruch 7 „auf der Grundlage eines Quantisierungsschrittes (Q) eines Quantisierers“ festgelegt.


2.   Der Erteilungsantrag liegt im Rahmen der ursprünglichen Offenbarung.


Der geltende Anspruch 1 geht hervor aus dem ursprünglichen Anspruch 1 sowie
der Beschreibung S. 7 Abs. 2 Satz 1. Der geltende Anspruch 7 geht hervor aus
dem ursprünglichen Anspruch 10 sowie der Beschreibung S. 7 Abs. 2 Satz 1.
Die geltenden Unteransprüche 2 bis 6 gehen aus den ursprünglichen Ansprüchen
3 bis 5, 7 und 9 hervor.
Die geltenden Ansprüche 1 bis 7 sind somit in den ursprünglichen Unterlagen
offenbart und sind zulässig.


3.   Das Filterverfahren gemäß dem geltenden Anspruch 1 und das Filter gemäß
dem nebengeordneten Anspruch 7 sind nicht neu gegenüber dem aus der
Druckschrift D1 Bekannten.
Bei der Druckschrift D1 handelt es sich um die Offenlegungsschrift zu einer
europäischen Patentanmeldung, mit der unter Anderem für die Bundesrepublik
Deutschland Schutz begehrt wurde und für die laut dem europäischen Patentregister die entsprechende Benennungsgebühr bezahlt worden ist. Ihr Anmeldetag liegt vor dem Prioritätstag der vorliegenden Anmeldung, die Offenlegung
erfolgte erst nach diesem. Somit stellt der Inhalt dieser Anmeldung, der in D1
offengelegt ist, gemäß § 3 Abs. 2 Satz 1 Nr. 2 PatG einen zur Beurteilung der
Neuheit heranzuziehenden Stand der Technik dar.


D1 betrifft ein signaladaptives Filterverfahren zur Verringerung von Blockeffekten
und Überschwingrauschen von Bilddaten und ein entsprechendes signaladaptives
Filter, vgl. Titel und Satz 1 der Zusammenfassung. An jedem Pixel der Bilddaten
wird ein Gradient berechnet und eine Kantenbestimmung durchgeführt durch
Vergleich von berechneten Gradientendaten mit einem globalen Schwellenwert Tg,
vgl. Sp. 3 Z. 47 bis Sp. 4 Z. 7 (ergibt globale Randabbildungsinformation) und in

                                            -9-



vorbestimmte Abmessungen aufweisenden Blöcken mit einem lokalen Schwellenwert Tn, vgl. Sp. 3 Z. 48 bis 51 und Sp. 4 Z. 35 (ergibt lokale Randabbildungsinformation) sowie anschließende Oder-Verknüpfung der beiden Ergebnisse (ergibt binäre Randabbildungsinformation), vgl. in Fig. 2 die „binary edge
mapping unit 100“ mit „global edge mapper 30“, „local edge mapper 40“ und
„logical OR unit 50“ sowie die zugehörige Beschreibung in Sp. 3 Abs. 2 ff. -
Merkmale a), c), d), teilweise b). Es wird jeweils ein Filterfenster mit vorbestimmten Abmessungen angelegt und in Abhängigkeit von der Bildkanteninformation
(binären Randabbildungsinformation) bestimmt, ob Kanten (Ränder) im Filterfenster vorhanden sind, vgl. den „filter determiner“ in Fig. 2 mit der Beschreibung
in Sp. 5 Z. 45 bis 58. Im jeweiligen Filterfenster wird pixelweise gefiltert, wobei
Fenster ohne Kanten unter Verwendung vorbestimmter erster gewichteter Werte
gefiltert werden („average filter“ in Fig. 2 sowie „average filtering“ in Fig. 3 unten
links) und Fenster mit Kanten unter Verwendung vorbestimmter zweiter gewichteter Werte gefiltert werden („weighted filter“ in Fig. 2 sowie „weight filtering“ in
Fig. 3 unten rechts); wenn der Pixel im Zentrum des Filterfensters ein Kantenpixel
ist, wird nicht gefiltert, vgl. Sp. 6 Z. 36 bis 38 - Merkmale e), f), g).


Hinsichtlich des globalen Schwellenwertes Tg ist in D1 Sp. 4 Z. 6 und 7 angegeben, dass dieser globale Schwellenwert Tg „100“ ist, wenn jeder Pixel in
einem Bild 256 Graustufen hat (d. h. wenn die Grauwerte in 256 Stufen eingeteilt
sind). Wie der Fachmann ohne Weiteres erkennt, bedeutet dies, dass im Fall einer
anderen Quantisierung der Bilddaten (z. B. in 64 Graustufen) ein anderer
Schwellenwert angewendet werden muss, d. h. dass der globale Schwellenwert Tg
von der Anzahl der Graustufen der Bilddaten abhängig ist. Die Einteilung in eine
bestimmte Anzahl von Graustufen ergibt sich hierbei, wie der Fachmann als
selbstverständlich mitliest, aus einer Quantisierung der (in einer natürlichen Szene
kontinuierlichen) Grauwerte in einem Quantisierer mit einem vorbestimmten
Quantisierungsschritt, etwa bei der Aufnahme der ursprünglichen Videodaten (vgl.
Sp. 2 Z. 31 „input video signal“) über eine Videokamera mit einem als Quantisierer
wirkenden Analog/Digital-Wandler. Somit erfolgt die Festlegung des globalen

                                        - 10 -



Schwellenwertes Tg auf der Grundlage eines vorbestimmten Quantisierungsschrittes eines Quantisierers - restlicher Teil des Merkmals b).


Demnach beinhaltet das aus D1 bekannte Verfahren alle im geltenden Anspruch 1
aufgeführten Merkmale. Dem Gegenstand des Anspruchs 1 fehlt somit die erforderliche Neuheit.


Anspruch 1 ist daher nicht gewährbar.


Entsprechendes gilt für das Filter gemäß dem nebengeordneten Anspruch 7,
wobei der hier zusätzlich aufgeführte Bildspeicher aus D1 Fig. 2 Bezugszeichen
10 („image store“) mit Beschreibung hervorgeht; dieser Bildspeicher erhält jeweils
die gemäß Fig. 1 und der Beschreibung in Sp. 2 Z. 22 bis 30 blockweise dekomprimierten Bilddaten und gibt diese an die Gradientenoperationseinheit („binary edge
mapping unit“ 100 mit „gradient image generator“ 20) weiter, vgl. Fig. 2.


Auch der nebengeordnete Anspruch 7 ist mangels Neuheit seines Gegenstandes
gegenüber dem aus D1 Bekannten nicht gewährbar.


Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die abhängigen Patentansprüche 2 bis 6 nicht gewährbar (BGH in GRUR 1997, 120
"Elektrisches Speicherheizgerät").




Dr. Fritsch       Dr. Mittenberger-Huber          Baumgardt         Dr. Thum-Rung




                                                                              Me
