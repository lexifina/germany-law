---
ecli: "ECLI:DE:BPatG:2025:280125B18Wpat55.23.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 55/23"
decided: "2025-01-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2025&Sort=1&Seite=1&nr=44515&anz=77&pos=22&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_LE_2025-01-28_18_W-pat_55_23_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0002a.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0100.md"]
---

# Bundespatentgericht, 18 W (pat) 55/23 vom 2025-01-28

## Leitsatz

LE

## Entscheidung

BUNDESPATENTGERICHT


Leitsatz


Aktenzeichen:                      18 W (pat) 55/23

Entscheidungsdatum:                28. Januar 2025

Rechtsbeschwerde zugelassen:       ja

Normen:                            § 2a Abs. 1 Nr. 2 Satz 1 PatG



Entscheidung: Verfahren zur Stenoseerkennung


Ein Verfahren zur automatischen Stenoseerkennung aus Bildern einer medizinischen Bildsequenz ist als Diagnostizierverfahren vom Patentschutz ausgenommen. Dies gilt auch, wenn
die Durchführung des bildgebenden Verfahrens am menschlichen oder tierischem Körper
nicht beansprucht wird, da dieser Schritt eine zwingende Voraussetzung für das beanspruchte Verfahren ist.

                 BUNDESPATENTGERICHT


    18 W (pat) 55/23
 _______________________

     (Aktenzeichen)




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2022 201 347.6
…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Januar 2025 durch den Vorsitzenden Richter
Dipl.-Phys. Dr. Morawek sowie die Richter Veit, Dr. Nielsen und der Richterin kraft
Auftrags Dipl.-Phys. Dr. Schenkl




ECLI:DE:BPatG:2025:280125B18Wpat55.23.0

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.
                     Die Rechtsbeschwerde wird zugelassen.




                                      Gründe



                                        I.


Die am 9. Februar 2022 beim Deutschen Patent- und Markenamt eingereichte
Patentanmeldung 10 2022 201 347.6 trägt die Bezeichnung

           „Verfahren und System zur automatisierten Bestimmung von
                Untersuchungsergebnissen in einer Bildsequenz“.


Die Prüfungsstelle für Klasse A61B hat mit Beschluss vom 27. September 2023 ein
Patent auf Grundlage des Hilfsantrags vom 29.08.2023 erteilt und den Hauptantrag
aus Gründen des Bescheids vom 31. Juli 2023 zurückgewiesen. Im genannten
Bescheid führt die Prüfungsstelle aus, dass der Gegenstand des geltenden
Patentanspruchs 2 aufgrund des Patentierungsausschlusses für Diagnostizierverfahren nicht patentfähig sei. Dies betreffe dann auch alle weiteren abhängigen
Patentansprüche, welche sich auf den Patentanspruch 2 rückbeziehen. Der
Hilfsantrag, in dem die strittigen Merkmale des Patentanspruch 2 gestrichen
wurden, führte zur Patenterteilung.



Bezüglich der Patentfähigkeit wurde auf folgende Druckschriften verwiesen:

     E1   US 2016 / 0 235 388 A1

     E2   US 2014 / 0 301 618 A1

                                       -3-



     E3   GHARBI, Hana; BAHROUN, Sahbi; ZAGROUBA, Ezzeddine. Key frame
          extraction for video summarization using local description and
          repeatability graph clustering. Signal, Image and Video Processing,
          2019, 13. Jg., Nr. 3, S. 507-515.



Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.



Der Beschwerdeführervertreter stellte den Antrag gemäß Schriftsatz vom
14. Januar 2025:



   Den Beschluss des Deutschen Patent- und Markenamts, Prüfungsstelle für
   Klasse A 61 B, vom 27. September 2023 aufzuheben und das Patent mit der
   Bezeichnung “Verfahren und System zur automatisierten Bestimmung von
   Untersuchungsergebnissen in einer Bildsequenz” zu erteilen auf Grundlage
   folgender Unterlagen:

   a) Ansprüche 1 bis 17 gemäß Schriftsatz vom 28. August 2023, eingegangen
   beim Deutschen Patent- und Markenamt am 29. August 2023;

   b) Beschreibung: Seiten 1 bis 34, eingegangen im Deutschen Patent- und
   Markenamt am 18. Januar 2023;

   c) Zeichnungen: Figuren 1 bis 4, eingegangen im Deutschen Patent- und
   Markenamt am 9. Februar 2022.



Der Patentanspruch 1 gemäß Hauptantrag lautet:


  1. Verfahren zur automatisierten Bestimmung von Untersuchungsergebnissen
      in einer Bildsequenz (S, S‘) aus mehreren zeitlich aufeinanderfolgenden
      Frames (F0, F, F1, F2, F3), das Verfahren umfassend die Schritte:

                                       -4-



      - Ermittlung von Befund-Kandidaten (K) in Form von zusammenhängenden
      Bildbereichen in den einzelnen Frames (F0, F, F1, F2, F3) für einen
      vorgegebenen Befund,
      für eine Anzahl der Befund-Kandidaten (K):
      - Ermittlung für einen Befund-Kandidaten (K) in einem Frame (F) welche
      Kandidaten-Bildbereiche (B) in anderen Frames (F0, F1, F2, F3) dem
      Befund-Kandidaten (K) entsprechen,
      - Ermittlung, ob die Kandidaten-Bildbereiche (B) des Befund-Kandidaten (K)
      in den anderen Frames (F0, F1, F2, F3) mit anderen Befund-Kandidaten (K)
      überlappen,
      - Erzeugung eines Graphen (G) mit den ermittelten Befund-Kandidaten (K)
      der Frames (F0, F, F1, F2, F3) als Knoten (N) und den ermittelten
      Überlappungen als Kanten (E),
      - Erzeugung von Gemeinschaften (C, C‘) aus mittels Kanten (E)
      verbundener Knoten (N), wobei Knoten (N) zu einer Gemeinschaft (C, C‘)
      zusammengefasst werden.


Der abhängige Patentanspruch 2 gemäß Hauptantrag lautet:


  2. Verfahren nach Anspruch 1, wobei die Gemeinschaften (C, C‘) ausgegeben
      werden oder für weitere Untersuchungen verwendet werden, bevorzugt im
      Rahmen einer Röntgen-Angiographie-Untersuchung, insbesondere für eine
      automatische Stenoseerkennung oder Stenosebewertung, eine quantitative
      Coronare Angiographie oder eine Lumensegmentierung.



Wegen des Wortlauts der nebengeordneten Patentansprüche 12, 15, 16 und 17,
welche auf ein System zur automatischen Bestimmung von Untersuchungsergebnissen, ein medizintechnisches System, ein Computerporgrammprodukt und
ein computerlesbares Medium gerichtet sind, sowie der abhängigen Ansprüche 2
bis 11, 13 und 14 wird auf die Akte verwiesen.

                                       -5-




Die Beschwerdeführerin vertritt die Auffassung, dass der Patentanspruch 2 gemäß
Hauptantrag nicht dem Patentierungsausschluss unterliege und patentfähig sei.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                        II.



Die zulässige Beschwerde hat in der Sache keinen Erfolg. Das Verfahren des
Patentanspruchs 2 gemäß Hauptantrag betrifft ein Diagnostizierverfahren, das
unter das Patentierungsverbot des § 2a Abs. 1 Nr. 2 Satz 1 PatG fällt.


1.    Die vorliegende Anmeldung betrifft ein Verfahren und ein System zur
automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz,
insbesondere in einer Angiographie-Sequenz. Unter anderem wird eine graphenbasierte Aggregation von Befunden in der Angiographie für eine temporale
Konsistenz erstellt (vgl. Offenlegungsschrift (OS), Abs. [0001] und Ansprüche).

Koronare Angiographie-Untersuchungen bestehen aus mehreren Einzelbilder, die
das Herz zu unterschiedlichen Zeitpunkten (Frames) und aus unterschiedlichen
Winkeln zeigen. Typischerweise erfolgt die Auswertung der Angiogramme durch
medizinische Experten, die mit ihrer Erfahrung die besten Frames für die Befundung
auswählen. Zu den Befunden zählen Läsionen, Stenosen, Totalverschlüsse und
andere Anomalien. Auch wenn in letzter Zeit einige Veröffentlichungen zur
Automatisierung erschienen sind, hat sich eine Automatisierung von solchen
Untersuchungen noch nicht durchgesetzt (vgl. OS, Abs. [0004] - [0007]).


2.    Vor diesem Hintergrund ist es Aufgabe der Erfindung, ein Verfahren und ein
entsprechendes System zur automatisierten Bestimmung von Untersuchungsergebnissen in einer Bildsequenz anzugeben, mit dem die aus dem Stand der

                                        -6-



Technik bekannten Nachteile vermieden werden und insbesondere medizinische
Bildsequenzen automatisiert untersucht werden können (vgl. OS, Abs. [0008]).



3.     Die Aufgabe wird unter anderem gelöst durch ein Verfahren gemäß
Patentanspruch 1, insbesondere i.V.m. dem abhängigen Patentanspruch 2.



Der seitens des Senats mit einer Merkmalsgliederung versehene Anspruch 1 lautet
wie folgt:


M1.1    Verfahren zur automatisierten Bestimmung von
        Untersuchungsergebnissen in einer Bildsequenz (S, S‘) aus mehreren
        zeitlich aufeinanderfolgenden Frames (F0, F, F1, F2, F3), das Verfahren
        umfassend die Schritte:
M1.2    - Ermittlung von Befund-Kandidaten (K) in Form von
        zusammenhängenden Bildbereichen in den einzelnen Frames (F0, F, F1,
        F2, F3) für einen vorgegebenen Befund,
        für eine Anzahl der Befund-Kandidaten (K):
M1.3    - Ermittlung für einen Befund-Kandidaten (K) in einem Frame (F) welche
        Kandidaten-Bildbereiche (B) in anderen Frames (F0, F1, F2, F3) dem
        Befund-Kandidaten (K) entsprechen,
M1.4    - Ermittlung, ob die Kandidaten-Bildbereiche (B) des Befund-Kandidaten
        (K) in den anderen Frames (F0, F1, F2, F3) mit anderen Befund-Kandidaten (K) überlappen,
M1.5    - Erzeugung eines Graphen (G) mit den ermittelten Befund-Kandidaten (K)
        der Frames (F0, F, F1, F2, F3) als Knoten (N) und den ermittelten
        Überlappungen als Kanten (E),
M1.6    - Erzeugung von Gemeinschaften (C, C‘) aus mittels Kanten (E)
        verbundener Knoten (N), wobei Knoten (N) zu einer Gemeinschaft (C, C‘)
        zusammengefasst werden.

                                        -7-




Hierauf bezieht sich der mit Merkmalsgliederung versehene Anspruch 2:


M2.1    Verfahren nach Anspruch 1,
M2.1    wobei die Gemeinschaften (C, C‘) ausgegeben werden oder für weitere
        Untersuchungen verwendet werden,
M2.3    bevorzugt im Rahmen einer Röntgen-Angiographie-Untersuchung,
M2.4    insbesondere für eine automatische Stenoseerkennung oder
        Stenosebewertung, eine quantitative Coronare Angiographie oder eine
        Lumensegmentierung.



4.     Als Fachmann ist hier ein Informatiker oder Physiker mit mehrjähriger Berufserfahrung in der Entwicklung von Auswerteverfahren von Angiographie-Sequenzen
anzusehen, der für die automatische Stenoseerkennung und -bewertung eng mit
einem Radiologen zusammenarbeitet.



5.     Der Fachmann legt den Merkmalen der Patentansprüche 1 und 2 folgendes
Verständnis zugrunde:



Beansprucht    wird   ein   Verfahren   zur   automatisierten   Bestimmung      von
Untersuchungsergebnissen in einer Bildsequenz S aus mehreren zeitlich
aufeinanderfolgenden Frames, wobei ein Frame F ein Einzelbild einer bevorzugt
medizinischen Bildsequenz ist. Diese Bildsequenz zeigt stets dasselbe Motiv bzw.
Szene, wobei Unterschiede beispielsweise durch die Herzbewegung entstehen
können. Bevorzugt handelt es sich um 2D-Bilder (Röntgenbilder, Ultraschallbilder),
jedoch kann das Verfahren auch mit 3D-Bildern (rekonstruierte CT- oder MRT-Aufnahmen) durchgeführt werden (vgl. OS, Abs. [0010]).

                                      -8-




Im Schritt I der Figur 1 erfolgt die Auswertung der einzelnen Frames. Für einen
vorgegebenen Befund werden diesen repräsentierende Bildbereiche beispielsweise
mittels eines für den vorgegebenen Befund trainierten neuronalen Netzwerks
ermittelt (vgl. OS, Abs. [0072,0093]). Die erhaltenen Merkmalskarten M, auf denen
Pixel mit hoher Befund-Wahrscheinlichkeit größere Werte aufweisen, durchlaufen
eine Grenzwertfilterung und eine Connected-Component-Analyse, so dass als
Befund-Kandidaten K zusammenhängende Bildbereiche P ermittelt werden (M1.2).
Als Ergebnis ergibt sich eine Anzahl von Befund-Kandidaten in verschiedenen
Frames.



Die Befund-Kandidaten sind Repräsentanten von medizinischen Befunden
(Pathologien), wie eine Gefäßwandunregelmäßigkeit, insbesondere eine Stenose.
Es können auch anatomische Merkmale (z.B. Bifurkationen in Gefäßen) sein
(vgl. OS, Abs. [0034]).



Die nachfolgenden Schritte II bis V basieren auf der Graphentheorie. Für jeden
ermittelten Befund-Kandidaten in dem Frame F werden zunächst beispielweise
unter Berücksichtigung eines Deformationsfelds die Kandidaten-Bildbereiche B in
den anderen Frames (z.B. F1), welche dem Befund-Kandidaten entsprechen,
ermittelt (Schritt II, M1.3). Dann erfolgt die Ermittlung, ob die Kandidaten-

                                           -9-



Bildbereiche B in den anderen Frames mit deren Befund-Kandidaten K überlappen
(Schritt III, M1.4). Anschließend wird ein Graph G erzeugt, welcher die ermittelten
zusammengehörigen Befund-Kandidaten als Knoten N und die ermittelten
Überlappungen als Kanten E ausweist (Schritt IV, M1.5). Der letzte Schritt des
graphenbasierten Verfahrens betrifft die Erzeugung von Gemeinschaften C aus
mittels Kanten verbundener Knoten (Schritt V, M1.6). Hierbei werden Knoten,
welche nur eine einzige Überlappung zu einem Befund-Kandidaten eines weiteren
Frames aufweisen, nicht in die Gemeinschaft C aufgenommen.



In den weiteren Verfahrensschritten gemäß Anspruch 2 werden diese Gemeinschaften C dann entweder beispielsweise in Form eines Schlüssel-Frames KF,
welcher den Befund schnell erkennen lässt, ausgegeben. Alternativ können die
Gemeinschaften auch für weitere Untersuchungen (der Gemeinschaften) durch
eine Befundungs-Einheit verwendet werden (M2.2, vgl. OS, Abs. [0027]). Diese
Untersuchungen im Rahmen einer Röntgen-Angiographie-Untersuchung (M2.3)
können neben der Lumensegmentierung, welche eine physikalische Größe des
Blutgefäßes     ermittelt,   auch   eine   automatische     Stenoseerkennung     oder
Stenosebewertung und eine quantitative Coronare Angiographie betreffen (M2.4,
vgl. OS, Abs. [0029]).


6.       Der Gegenstand des Anspruchs 1 ist patentfähig (§§ 3 und 4 PatG).


In dem Tracking-Verfahren der D1 wird aus einer Bildsequenz aus mehreren zeitlich
aufeinanderfolgenden Frames (vgl. Abs. [0007]: receiving image flames … 2D
fluoroscopy images from an X-Ray imaging device) die räumliche Veränderung
eines Blutgefäßes bestimmt (vgl. Abs. [0007]: method for tracking vessels, M1.1).
Hierzu     werden    Befund-Kandidaten      in   Form     von   zusammenhängenden
Bildbereichen aus den Frames ermittelt (vgl. Abs. [0007]: a set of tracking points are
determined M1.2), wobei für einen Befund-Kandidaten in einem Frame, die
entsprechenden Kandidaten-Bildbereiche in den anderen Frames ermittelt werden

                                           - 10 -



(vgl. Abs. [0007]: For each respective image frame, a set of tracking points are
determined according to a tracking algorithm comprising selecting landmark
hypothesis points for each tracking target in the respective frame based on a
comparison with a previous image frame M1.3). Anschließend wird ermittelt, ob sich
die Bildbereiche überlappen (vgl. Abs. [0008]: by performing a similarity matching
process with the previous image frame. Techniques such as scoring may be applied
to the graph for the purposes of determining similarity. This unary score may be
based on, for example, one or more of local intensity similarity, Frangi vesselness
response, and a location constraint. M1.4). Schließlich wird ein Graph erzeugt,
wobei jedoch die Knoten unterschiedlichen Befund-Kandidaten entsprechen (vgl.
Abs. [0009]: A graph (e.g., a directed acyclic graph) is constructed where each node
of the graph corresponds to the one or more landmark hypothesis points. [0042]:
FIG. 5 provides an example of the construction of a directed acyclic graph for use
in finding the optimal vessel landmarks on a frame f, M1.5ohne Überlappungen als Kanten).


Ausgehend von dem Tracking-Verfahren der D1 hat der Fachmann nicht die
Veranlassung, einen Graphen mit Knoten der Kandidaten-Bereiche des einen
Befund-Kandidaten in den unterschiedlichen Frames und der ermittelten
Überlappungen als Kanten zu erzeugen (M1.5). Zudem fehlt die Erzeugung von
Gemeinschaften aus diesen Graphen (M1.6).


Aus der D2 ist ebenfalls ein Tracking-Verfahren bekannt, welches allerdings noch
ferner abliegt. Hier dient die Bildung eines Graphs zur Erstellung eines
Blutgefäßbaums in einem Frame und nicht für die Erzeugung von Gemeinschaften
mit Knoten aus unterschiedlichen Frames.


Aus der D3 ist ein Bildauswahl-Verfahren zur automatischen Bestimmung von „Key
Frames“ in einer Bildsequenz aus mehreren zeitlich aufeinanderfolgenden Frames
bekannt (M1.1ohne     Untersuchungsergebnisse).   Hierfür werden interessante Punkte
ermittelt, wobei der Fachmann hierbei einen zusammenhängenden Bildbereich
mitliest (M1.2ohne Befund/vorgegebenen Befund). Weiterhin werden die interessanten

                                      - 11 -



Punkte ermittelt, welche denen in den anderen Frames entsprechen (vgl. Abs. 3.2,
Formel (1); It is the average number of matched interest points detected between
two images undergoing different transformation changes (rotation, viewpoint,
luminance…), noise and blur [29]. R represents the number of corresponding
interest points and (n1, n2) represents the number of interest points detected,
respectively, in both images. M1.3). Statt der Überlappung wird die Ähnlichkeit
zwischen den Frames ermittelt (Merkmal 1.4ohne Überlappung). Es wird ein Graph aus
einzelnen Frames als Knoten und der Ähnlichkeiten als Kanten erstellt (vgl. Fig. 2,
Abs. 3.2: let a graph G= (V, E) consisting of N =|V| vertices and m =|E| edges. In
our context, we represent frames by vertices ‘V’ and we connect each vertex i with
all vertices corresponding to the frames coming after in a chronological order i +
1,…, N. Each edge connecting two vertices is weighted by Wi,j where Wi,j
corresponds to the repeatability value between frames i and j. By this way, Wi,j is
assimilated to the edge weight which can correspond to the similarity between
edges. M1.5ohne Überlappung). Anschließend werden Gemeinschaften aus den mittels
Kanten verbundenen Knoten erzeugt (vgl. Abs. 3.3: The principle of network
clustering via approaching modularity is to keep intra-cluster edges and eliminate
the inter-cluster ones. It consists in eliminating edges based on the difference
between their weights.).


Nicht bekannt aus der D3 ist die Anwendung des Extraktionsverfahrens auf
(medizinische) Untersuchungsergebnisse mit Befund-Kandidaten (M1.1, M1.2 -
M1.5) sowie die räumliche Überlappung der Kandidaten-Bildbereiche als
Ähnlichkeitskriterium (M1.4). Auch hier fehlt es dem Fachmann an einer
Veranlassung, dieses Verfahren auf medizinische Bildsequenzen und Befund-Kandidaten anzuwenden.


Zusammenfassend ist der Gegenstand des Patentanspruchs 1 neu und beruht auf
einer erfinderischen Tätigkeit.

                                      - 12 -



7.    Die Erfindung ist jedoch nach § 2a Abs. 1 Nr. 2 Satz 1 PatG vom Patentschutz
ausgeschlossen. Sie betrifft ein Diagnostizierverfahren, das am menschlichen oder
tierischen Körper vorgenommen wird.


Der Schutzzweck des Patentierverbotes ist es, die Krankheit des Menschen nicht
zu kommerzialisieren und dem behandelnden Arzt die Freiheit der Untersuchungsmethoden zum Erkennen einer Krankheit zu erhalten (Benkard, PatG, 12. Aufl., §
2a Rn. 58). Dabei versteht man in der Medizin unter einer Diagnose die Zuordnung
von Befunden oder Symptomen zu einem Krankheitsbegriff. Die Methoden der
Diagnosefindung werden unter dem Begriff Diagnostik zusammengefasst und
umfassen z. B. die Befragung des Patienten zur Anamneseerhebung (Krankengeschichte), einfache körperliche Untersuchungen durch den Arzt, Messungen am
Körper des Patienten (z. B. Puls, Blutdruck, EKG), bildgebende Verfahren (z. B.
Röntgen, CT) und Laboruntersuchungen (z. B. Blut, Gewebeuntersuchungen).
Diagnostizierverfahren sind somit Verfahren am lebenden menschlichen oder
tierischen Körper zu medizinischen Zwecken, die der Erkennung, Lokalisierung
oder dem Ausschluss von pathologischen (krankhaften) Zuständen dienen und
deren Ergebnisse eine Grundlage für die weitere Therapie sein können (siehe
Schulte, PatG, 12. Aufl., § 2a Rn. 80). Eine eindeutige Diagnose kann gestellt
werden, wenn die ermittelten Befunde oder Symptome für eine bestimmte Krankheit
spezifisch sind. Viele Krankheiten sind jedoch lediglich durch unspezifische
Symptome gekennzeichnet. Der behandelnde Arzt versucht dann durch weitere
Untersuchungen     die   Zahl   der   möglichen    Krankheiten    einzuschränken
(Ausschlussdiagnose). Die Auswertung der Befunde oder Symptome kann daher
bei einer geringen Anzahl von Befunden oder bei unklaren Befunden auch nur zu
einem sehr allgemeinen Krankheitsbild bzw. zu mehreren möglichen Diagnosen
führen. Die Bandbreite der Zuordnung von Befunden zu einem Krankheitsbegriff
reicht daher bei einer Diagnose von der Erkennung einer bestimmten Krankheit über
den Ausschluss von Krankheiten bis zu der Erkenntnis, dass der Patient nicht
gesund ist, ohne dass die Befunde einer bestimmten Krankheit zugeordnet werden
können.

                                       - 13 -




Hiervon ausgehend unterteilt die Rechtsprechung ein Diagnostizierverfahren in
folgende Schritte:


1) Untersuchung mit Datenerhebung,
2) Vergleich dieser Daten mit Normwerten,
3) Feststellung einer Abweichung bei diesem Vergleich,
4) Deutung der Abweichung als krankhafter Zustand.


Die Untersuchung nach Schritt 1) wird am menschlichen oder tierischen Körper
vorgenommen. Die Schritte 2) bis 4) werden dagegen regelmäßig nicht am
menschlichen oder tierischen Körper vorgenommen. Soweit im Sinne einer
restriktiven Auslegung des Patentierungsverbotes angenommen wird, dass alle vier
Verfahrensschritte am menschlichen oder tierischen Körper vorgenommen werden
müssen, schließt sich der Senat dieser Auffassung nicht an (vgl. zum Streitstand:
Busse/Keukenschrijver, PatG, 9. Aufl., § 2a Rn. 52). Andernfalls wären letztlich alle
technischen Verfahren, die über ärztliches Hören, Sehen, Riechen und Tasten
hinausgehen, vom Patentierungsverbot ausgenommen.


Eine Deutung als krankhafter Zustand gemäß Schritt 4) ist bereits gegeben, wenn
die erhobenen Daten einen nicht normalen Zustand im Sinne von „nicht gesund“
gegenüber den Normwerten darstellen (BPatG, GRUR 2008, 981 – Verfahren zur
gesundheitlichen Orientierung).


a)    Den Schritt 1) eines Diagnostizierverfahrens im Sinne von § 2 Abs. 1 Nr. 2
Satz 1 PatG (Untersuchung mit Datenerhebung am menschlichen oder tierischen
Körper) verwirklicht die Erfindung in Anspruch 1 durch die beanspruchte Bildsequenz, die der Ermittlung von Befund-Kandidaten bzw. der Erzeugung von
Graphen zugrundeliegt. Diese wird mittels bildgebender Verfahren (z.B. im Rahmen
einer Angiographie, vgl. OS, Abs. [0002]) am menschlichen oder tierischen Körper

                                       - 14 -



erzeugt. Die Durchführung der Datenerhebung am menschlichen Körper selbst wird
jedoch nicht beansprucht.


b)    Der Vergleich der in Schritt 1) gewonnenen Daten mit Normwerten, der in
Schritt 2) eines Diagnostizierverfahrens erfolgt, wird gemäß der Erfindung von
einem neuronalen Netzwerk durchgeführt, das zuvor mit Stenose-Annotationen
trainiert wurde (vgl. OS, Abs. [0093]). Dabei wird der Fachmann die Offenlegungsschrift ohne Weiteres dahingehend verstehen, dass das Training mit „Stenose-Annotationen“ sowohl Bilder von Stenosen als auch von gesunden Blutgefäßen als
Normwert umfasst.


c)    Damit verwirklicht die beschwerdegegenständliche Erfindung auch Schritt 3)
eines Diagnostizierverfahrens. Mit dem Vergleich der in Schritt 1) gewonnenen
Daten mit Normwerten (Schritt 2) stellt das neuronale Netzwerk zugleich
Abweichungen von der Norm fest, wenn diese vorliegen. Die ermittelten
Unterschiede zwischen Befund-Kandidat und Norm werden mittels einer Merkmalskarte M ausgegeben, welche Pixeln mit hoher Stenosewahrscheinlichkeit, also
größerem Unterschied, höhere Werte zuordnet. Mittels eines Grenzwertvergleichs
und einer Nachbarschaftsanalyse werden die Befund-Kandidaten aus den
Merkmalskarten ermittelt (vgl. OS, Abs. [0093]). In Anspruch 3 wird dargelegt, dass
ein Befund-Kandidat bevorzugt den Fund einer Gefäßwandunregelmäßigkeit,
insbesondere einer Stenose, oder den Befund einer Bifurkation repräsentiert.


d)    Hieraus folgt auch, dass mit der Identifizierung eines von der Norm
abweichenden Befund-Kandidaten als Zwischenschritt, eine Deutung als krankhafter Zustand einhergeht (Schritt 4). Gemäß Anspruch 2, dient das erfindungsgemäße Verfahren dem Erkennen und Bewerten von Stenosen. Dabei versteht man
unter einer Stenose (bzw. einer Koronarstenose, nachdem vorliegend bevorzugt
koronare Befunderhebungen angesprochen sind (vgl. OS, Abs. [0001]) die
Verengung eines Herzkranzgefäßes, die in der internationalen Klassifikation der
Krankheiten (ICD) als Krankheit aufgelistet wird.

                                       - 15 -




e)    Die oben dargestellte Deutung eines Befundes als krankhafter Zustand
mittels eines neuronalen Netzwerkes fällt unter das Patentierverbot nach § 2 Abs. 1
Nr. 2 Satz 1 PatG. Zwar wird der Schritt 4) des Diagnostizierverfahrens, also die
Deutung einer aufgefundenen Abweichung von der Norm, üblicherweise von einem
Arzt als rein geistige Tätigkeit durchgeführt. Die Bewertung als krankhafter Zustand
wird jedoch zunehmend auch von automatisierten Systemen übernommen (BPatG,
a. a. O.; EPA, GRUR Int, 2006, 514 – Diagnostizierverfahren, Ziffer 6.3.). Bei
einfachen Diagnosen kann sich die deduktive medizinische Entscheidung, ob eine
Abweichung von der Norm eine Krankheit ist, ohne Weiteres ergeben. Bei anderen
Abweichungen von der Norm können Diagnosen auch durch die Erhebung
verschiedener Messwerte und Daten durch adaptive Systeme mit medizinischen
Wissensdatenbanken technisch realisiert werden.


f)    Der Umstand, dass die Erfindung die Untersuchung des betreffenden
Patienten selbst, also die Durchführung eines bildgebenden Verfahrens am
menschlichen oder tierischen Körper, nicht umfasst, gibt zu keiner anderen
Entscheidung Anlass. Denn die Erfindung setzt diesen Schritt denknotwendig
voraus. Bei medizinischen Bildgebungsverfahren mittels Röntgenstrahlung, Ultraschall oder Kernspinresonanz ist eine Wechselwirkung mit dem menschlichen oder
tierischen Körper zwingend erforderlich und setzt zwangsläufig dessen Präsenz
voraus. Die im Patentanspruch 1 beanspruchte Bildsequenz ist somit in Wechselwirkung mit einem menschlichen oder tierischen Körper entstanden und eine
zwingende Voraussetzung für das beanspruchte Verfahren. Zudem ist auch zu
berücksichtigen, dass das Patentgesetz, anders als Art. 84 EPÜ, nicht fordert, alle
wesentlichen Merkmale, die für die deutliche und vollständige Definition der
Erfindung notwendig sind, in einen Patentanspruch aufzunehmen. Insofern besteht
die Gefahr, dass das Patentierungsverbot nach § 2 Abs. 1 Nr. 2 Satz 1 PatG schon
durch Weglassen eines Merkmals, welches der Diagnose selbstverständlich und
zwingend vorausgeht, umgangen werden könnte.

                                        - 16 -



g)      Auch der Beschluss des Bundesgerichtshofs vom 31. August 2010, Az. X/ZB
9/09 (BGH, GRUR 2010, 1081 – Bildunterstützung bei Katheternavigation), führt
nicht zum Erfolg der Beschwerde. Dort hat der Bundesgerichtshof ein Patentierungsverbot im Sinne von § 2 Abs. 1 Nr. 2 Satz 1 PatG verneint und ausgeführt,
dass eine Sache oder Vorrichtung unabhängig von dem Zweck zu dem sie nach
den Angaben im Patentanspruch verwendet werden soll, durch räumlich-körperlich
umschriebene Merkmale als Schutzgegenstand definiert wird. Entsprechendes
gelte auch für in Verfahrensansprüchen enthaltene Zweck-, Wirkungs- oder
Funktionsangaben (BGH a. a. O., Rn. 11). Vorliegend ist bei sachgemäßer
Auslegung der Offenlegungsschrift jedoch keine andere Verwendung der Erfindung
als zur Feststellung krankhaft veränderter Gefäße erkennbar. Selbst wenn in Absatz
[0001] ausgeführt wird, dass die Erfindung ein Verfahren betrifft, das insbesondere
im medizinischen Bereich zur Anwendung kommen kann, verdeutlicht die
Beschreibung im Übrigen, dass vorliegend tatsächlich nur der medizinische Bereich,
insbesondere das Auffinden von Stenosen, betroffen ist. Weiterhin beschreibt
Patentanspruch 3 - ohne formelhafte sprachliche Einschränkungen im Sinne von
„vorzugsweise“ oder „insbesondere“ - ein Verfahren, das medizinische Befunde
betrifft.


8.      Die Rechtsbeschwerde war nach § 100 Abs. 2 Nr. 1 PatG zuzulassen. Im
vorliegenden Beschwerdeverfahren sind Rechtsfragen             von    grundsätzlicher
Bedeutung zu entscheiden. So ist höchstrichterlich noch nicht geklärt, ob das Patentierungsverbot nach § 2 Abs. 1 Nr. 2 Satz 1 PatG auch dann bejaht werden kann,
wenn die Ansprüche die Datenerhebung am menschlichen oder tierischen Körper
nicht mit umfassen, sondern lediglich denknotwendig voraussetzen. Weiterhin ist
noch nicht mit vollständiger Rechtssicherheit geklärt, ob nur der erste oder alle vier
Verfahrensschritte am menschlichen oder tierischen Körper durchzuführen sind.
Gleiches gilt für die Erstellung von Diagnosen allein durch automatisierte Verfahren.

                                     - 17 -



                             Rechtsmittelbelehrung



Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch
einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten
schriftlich einzulegen.




Dr. Morawek           Dr. Nielsen             Veit          Dr. Schenkl

                                  - 18 -



Bundespatentgericht

     18 W (pat) 55/23
         (Aktenzeichen)




Verkündet am

28. Januar 2025

…
Justizbeschäftigter
als Urkundsbeamter der Geschäftsstelle
