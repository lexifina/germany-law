---
ecli: "ECLI:DE:BPatG:2022:290322B17Wpat38.19.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 38/19"
decided: "2022-03-29"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2022&Sort=1&Seite=10&nr=43048&anz=542&pos=159&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2022-03-29_17_W-pat_38_19_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 38/19 vom 2022-03-29

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 38/19                                                  Verkündet am
_______________________
                                                                   29. März 2022
    (Aktenzeichen)
                                                                        …




                                 BESCHLUSS

                               In der Beschwerdesache


                betreffend die Patentanmeldung 10 2016 104 236.6


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 29. März 2022 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Phys. Dr. Forkel, der
Richterin Akintche und des Richters Dipl.-Phys. Dr. Städele


beschlossen:


                          Die Beschwerde wird zurückgewiesen.




ECLI:DE:BPatG:2022:290322B17Wpat38.19.0

                                        -2-



                                     Gründe


                                          I.


Die vorliegende Patentanmeldung wurde am 9. März 2016 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


       „Verfahren zur Erstellung eines Modells eines technischen Systems“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F des
Deutschen Patent- und Markenamtes vom 26. April 2019 aus Gründen des
Bescheids vom 12. Oktober 2018 zurückgewiesen. Im genannten Bescheid führte
die Prüfungsstelle aus, dass der Gegenstand des (damaligen) Patentanspruches 1
nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie ist zur
mündlichen Verhandlung – wie angekündigt – nicht erschienen.


Die Anmelderin hat mit Eingabe vom 21. März 2022 sinngemäß beantragt,


        den angefochtenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        gemäß Hauptantrag mit
        Patentansprüchen 1 bis 6 vom Anmeldetag;
        Beschreibungsseiten 1 bis 14 und
        4 Blatt Zeichnungen mit Figuren 1 bis 4 jeweils vom Anmeldetag;


        gemäß Hilfsantrag mit
        Patentansprüchen 1 bis 5 vom 23. Mai 2019;
        im Übrigen wie Hauptantrag.

                                     -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt wurde auf die
Druckschriften


D1: DE 10 2011 081 345 A1,


D2: WO 2014/187828 A1


und


D3: US 2005/0201524 A1


hingewiesen.

Vom Senat wurden zwischenzeitlich die Druckschriften


D4:   Nils Tietze: Model-based Calibration of Engine Control Units Using
Gaussian Process Regression, Doctoral Thesis, 2015 [recherchiert am
15.11.2021]. Im Internet:
https://tuprints.ulb.tu-darmstadt.de/4572/1/20150506_Dissertation_Tietze.pdf,


D5:   Diego Didona; Paolo Romano: Using Analytical Models to Bootstrap
Machine Learning Performance Predictors, 2015 IEEE 21st International
Conference on Parallel and Distributed Systems (ICPADS), 14-17 Dec. 2015,
Date Added to IEEE Xplore: 18 January 2016 [recherchiert am 15.11.2021]. Im
Internet:
https://www.researchgate.net/profile/Diego-Didona/publication/283087011_Using_Analytical_Models_to_Bootstrap_Mac
hine_Learning_Performance_Predictors/links/562a1dfe08ae04c2aeb153fe/Us
ing-Analytical-Models-to-Bootstrap-Machine-Learning-Performance-Predictors.pdf


und

                                         -4-



D6:   Benjamin Berger; Florian Rauscher; Boris Lohmann: Analysing
Gaussian Processes for Stationary Black-Box Combustion Engine
Modelling, Proceedings of the 18th World Congress, The International
Federation of Automatic Control, Milano (Italy) August 28-September 2, 2011,
IFAC Proceedings Volumes, Volume 44, Issue 1, January 2011, Pages 10633-
10640 [recherchiert am 15.11.2021]. Im Internet:
https://www.sciencedirect.com/science/article/pii/S1474667016453218


eingeführt.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet (mit redaktioneller Änderung):


M1            Verfahren


M2            zur Erstellung eines Modells eines technischen Systems, wobei


M3            -       Messpunkte durch Einstellung von Eingangsgrößen und
              Messung von Ausgangsgrößen am technischen System bestimmt
              werden, wobei


M4            -       Simulationspunkte durch Einstellung von Eingangsgrößen und
              Simulation von Ausgangsgrößen mittels eines physikalisch basierten
              Modells des technischen Systems bestimmt werden, wobei


M5            -       die Bildung eines ersten datenbasierten Modells einschließlich
              einer Unsicherheit dieses Modells anhand der Messpunkte erfolgt
              sowie    die    Bildung   eines    zweiten   datenbasierten   Modells
              einschließlich einer Unsicherheit dieses Modells anhand der
              Simulationspunkte erfolgt, wobei

                                      -5-



M6   -      das zweite datenbasierte Modell dadurch weitergebildet wird,
     dass anhand dieses Modells die Eingangsgrößen für eine weitere
     Simulation von Ausgangsgrößen ausgewählt werden, welche eine
     maximale Unsicherheit dieses Modells verursachen sowie weiterhin
     eine Simulation von Ausgangsgrößen anhand dieser ausgewählten
     Eingangsgrößen         erfolgt    und     der    so   bereitstehende      weitere
     Simulationspunkt        zusätzlich       zu     den   schon     bereitstehenden
     Simulationspunkten         einer        erneuten      Bildung    des   zweiten
     datenbasierten Modells zu Grunde gelegt wird, wobei


M7   -      das erste datenbasierte Modell dadurch weitergebildet wird,
     dass anhand dieses Modells die Eingangsgrößen für eine weitere
     Messung von Ausgangsgrößen ausgewählt werden, welche eine
     maximale Unsicherheit dieses Modells verursachen sowie weiterhin
     eine Messung von Ausgangsgrößen anhand dieser ausgewählten
     Eingangsgrößen         erfolgt    und     der    so   bereitstehende      weitere
     Messpunkt zusätzlich zu den schon bereitstehenden Messpunkten
     einer erneuten Bildung des ersten datenbasierten Modells zu Grunde
     gelegt wird


M8   sowie weiterhin der weitere Simulationspunkt dieser erneuten
     Bildung eines ersten datenbasierten Modells zu Grunde gelegt wird,
     welcher auch der erneuten Bildung eines zweiten datenbasierten
     Modells zu Grunde gelegt wird, sofern dieser ein Gültigkeitskriterium
     erfüllt, wobei


M9   -      die    Weiterbildung        des    zweiten     datenbasierten   Modells
     wiederholt erfolgt, wobei
     -      sich      mit     jeder         Wiederholung       die    Anzahl      von
     Simulationspunkten erhöht, wobei

                                             -6-



M10           -            die   Weiterbildung   des   ersten   datenbasierten   Modells
              wiederholt erfolgt, wobei
              -            sich mit jeder Wiederholung die Anzahl von Messpunkten
              erhöht, und sich mit jeder Wiederholung, bei Erfüllung des
              Gültigkeitskriterium[s] außerdem die Anzahl von Simulationspunkten
              erhöht, wobei


M11           -        die Weiterbildung des ersten und des zweiten datenbasierten
              Modells solange wiederholt wird, bis ein Abbruchkriterium erfüllt ist,
              wobei


M12           -        das erste datenbasierte Modell dem zu erstellenden Modell
              des technischen Systems entspricht.


Der mit einer denkbaren Gliederung versehene Patentanspruch 1 gemäß
Hilfsantrag       lautet     (Änderungen     gegenüber    Hauptantrag    markiert,   mit
redaktioneller Änderung):


M1            Verfahren


M2            zur Erstellung eines Modells eines technischen Systems, wobei


M2a           das Modell des technischen Systems für eine Kalibrierung der
              Steuerung/Regelung des technischen Systems zur Verfügung steht,
              wobei


M3´           -        Messpunkte durch EinstellungVariation von Eingangsgrößen
              und Messung von Ausgangsgrößen am technischen System
              bestimmt werden, wobei

                                    -7-



M4´           -Simulationspunkte          durch      EinstellungVariation      von
      Eingangsgrößen und Simulation von Ausgangsgrößen mittels eines
      physikalisch basierten Modells des technischen Systems bestimmt
      werden, wobei


M5´   -       die Bildung eines ersten datenbasierten Modells einschließlich
      einer Unsicherheit dieses Modells anhand der Messpunkte mittels
      einer Regressionsanalyse erfolgt sowie die Bildung eines zweiten
      datenbasierten Modells einschließlich einer Unsicherheit dieses
      Modells      anhand      der        Simulationspunkte       mittels     einer
      Regressionsanalyse erfolgt, wobei


M6´   -       das zweite datenbasierte Modell dadurch weitergebildet wird,
      dass anhand dieses Modells die Eingangsgrößen für eine weitere
      Simulation von Ausgangsgrößen ausgewählt werden, welche eine
      maximale Unsicherheit dieses Modells verursachen sowie weiterhin
      eine Simulation von Ausgangsgrößen anhand dieser ausgewählten
      Eingangsgrößen      erfolgt    und    der    so   bereitstehende      weitere
      Simulationspunkt      zusätzlich     zu     den   schon     bereitstehenden
      Simulationspunkten       einer      erneuten      Bildung    des      zweiten
      datenbasierten Modells zu Grunde gelegt wird, so dass dieses
      Modell danach strebt, seine eigene Zuverlässigkeit zu maximieren,
      wobei


M7´   -       das erste datenbasierte Modell dadurch weitergebildet wird,
      dass anhand dieses Modells die Eingangsgrößen für eine weitere
      Messung von Ausgangsgrößen ausgewählt werden, welche eine
      maximale Unsicherheit dieses Modells verursachen sowie weiterhin
      eine Messung von Ausgangsgrößen anhand dieser ausgewählten
      Eingangsgrößen      erfolgt    und    der    so   bereitstehende      weitere
      Messpunkt zusätzlich zu den schon bereitstehenden Messpunkten

                                    -8-



       einer erneuten Bildung des ersten datenbasierten Modells zu Grunde
       gelegt wird, so dass dieses Modell danach strebt, seine eigene
       Zuverlässigkeit zu maximieren,


M8´    sowie weiterhin der weitere Simulationspunkt dieser erneuten
       Bildung eines ersten datenbasierten Modells zu Grunde gelegt wird,
       welcher auch der erneuten Bildung eines zweiten datenbasierten
       Modells zu Grunde gelegt wird, sofern dieser ein Gültigkeitskriterium
       erfüllt, so dass eine Entscheidung getroffen werden kann, ob ein
       Simulationspunkt      zur   Verbesserung    der     Genauigkeit    für   die
       Fortbildung des ersten datenbasierten Modells herangezogen
       werden soll, wobei


M9´    -     die    Weiterbildung     des    zweiten     datenbasierten   Modells
       wiederholt erfolgt, wobei
       -     sich      mit    jeder       Wiederholung      die    Anzahl       von
       Simulationspunkten erhöht, wobei


M10´   -      die    Weiterbildung    des     ersten   datenbasierten     Modells
       wiederholt erfolgt, wobei
       -      sich mit jeder Wiederholung die Anzahl von Messpunkten
       erhöht, und sich mit jeder Wiederholung, bei Erfüllung des
       Gültigkeitskriterium[s] außerdem die Anzahl von Simulationspunkten
       erhöht, wobei
       -           sich dadurch eine höhere Zuverlässigkeit des ersten
       datenbasierten Modells ergibt, dass dieses Modell auf einer breiteren
       Basis errichtet wird, sowohl aufbauend auf Kombinationen von
       Eingangs- und Ausgangsgrößen des technischen Systems, die durch
       Messungen als auch durch Simulationen mittels eines physikalischen
       Modells gewonnen werden,

                                          -9-



M11                   -die Weiterbildung des ersten und des zweiten datenbasierten
                 Modells solange wiederholt wird, bis ein Abbruchkriterium erfüllt ist,
                 wobei
M12          -        das erste datenbasierte Modell dem zu erstellenden Modell
             des technischen Systems entspricht.


Zu den übrigen Patentansprüchen und den weiteren Einzelheiten wird auf die Akte
verwiesen.




                                           II.




Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da der Gegenstand des jeweiligen Patentanspruchs 1
gemäß Haupt- und Hilfsantrag nicht auf erfinderischer Tätigkeit beruht (§ 1 Abs. 1
in Verbindung mit 4 Satz 1 PatG).


1.    Der Gegenstand der Anmeldung betrifft ein Verfahren zur Erstellung eines
Modells eines technischen Systems (Offenlegungsschrift, Abs. [0001]).


Ausweislich der Anmeldung handle es sich bei dem technischen System
insbesondere um eine Brennkraftmaschine, bei der Ausgangsgrößen, wie
beispielsweise       Schadstoffemissionen         und      Kraftstoffverbrauch,    von
Eingangsgrößen, wie beispielsweise Drehzahl, Drehmoment und Kraftstoffdruck,
abhängig seien. Bei einer Brennkraftmaschine bewirkten folglich bestimmte
Stellgrößen von Aktoren (Eingangsgrößen) wiederum bestimmte Prozessgrößen
(Ausgangsgrößen).        Die   Prozessgrößen     seien   mittels   Sensoren   messbar.
Allerdings sei es schwierig, die Stellgrößen von Aktoren einer Brennkraftmaschine
zu ermitteln, welche bestimmte Ausgangsgrößen bewirken, insbesondere wenn
mehrere Aktoren eingesetzt würden. Mit anderen Worten: zum Auffinden

                                        - 10 -



derjenigen   Stellgrößen,     die   bestimmten    Ausgangsgrößen    bewirken,     wie
beispielsweise      geringe     Schadstoffemissionen     oder     einen       geringen
Kraftstoffverbrauch, sei eine Variation von Stellgrößen und Messung von
Ausgangsgrößen sehr aufwendig (Offenlegungsschrift, Abs. [0002]).


Die Anmeldung geht aus von einem Stand der Technik, wie er in der Druckschrift
WO2014187828A1 beschrieben ist. Dort sei eine Methode zur Ermittlung eines
Modells für eine Ausgangsgröße eines technischen Systems offenbart, wobei die
Ausgangsgröße in nichtlinearer Weise von Eingangsgrößen abhängig sei. Als
Modell werde eine Modellstruktur mit Modellparametern vorgegeben, und die
Modellparameter würden mittels eines iterativen Verfahrens anhand von
gemessenen Ausgangsgrößen optimiert. Anhand dieses datenbasierten Modells
könne dann der Einfluss einer Variation von Stellgrößen auf Ausgangsgrößen
simuliert werden und es könnten die Stellgrößen bzw. Stellgrößenkombinationen
bestimmt werden, welche ein gewünschtes Verhalten des technischen Systems
hervorrufen (Offenlegungsschrift, Abs. [0002]).


Weiterhin nennt die Anmeldung die Druckschrift DE102011081345A1. Diese lehre,
zur   Entwicklung    eines    technischen   Systems    ein   physikalisches    Modell
heranzuziehen. Mittels eines solchen physikalisch basierten Modells werde das
Verhalten des technischen Systems auf Grundlage von bekannten physikalischen
Zusammenhängen mathematisch beschrieben. Damit dieses physikalische Modell
das reale Verhalten des technischen Systems bestmöglich beschreibe, sei es
einerseits erforderlich, das physikalische Modell unter Berücksichtigung der
bekannten Modellparameter zu entwickeln, und andererseits, nicht bekannte
Modellparameter anhand von Versuchen zu bestimmen. Die Bestimmung der nicht
bekannten Modellparameter erfolge gemäß der Druckschrift DE102011081345A1
mittels eines datenbasierten Modells, d. h. das reale technische System werde
vermessen und auf Basis der gemessenen Werte werde ein datenbasiertes Modell
trainiert. Daneben werde ein physikalisches Modell erstellt und es erfolge eine
erste Bestimmung der Modellparameter anhand der technischen Daten des

                                         - 11 -



technischen Systems. Mittels des datenbasierten Modells würden im weiteren
Verlauf die Parameter des physikalischen Modells optimiert. Ferner sei aus dem
genannten Stand der Technik bekannt, eine Angabe über die Unsicherheit des
datenbasierten Modells bei der Bestimmung der nicht bekannten Parameter des
physikalischen Modells zu berücksichtigen, so dass Qualität und Robustheit der
Bestimmung dieser Parameter verbessert würden (Offenlegungsschrift, Abs.
[0003]). Mittels der aus dem Stand der Technik bekannten Verfahren sei es
jedenfalls möglich, den Versuchsaufwand bei der Entwicklung eines technischen
Systems zu reduzieren (Offenlegungsschrift, Abs. [0004]).


Als Aufgabe wird in der Anmeldung genannt, den Versuchsaufwand bei der
Entwicklung eines technischen Systems noch weiter zu reduzieren und die
Genauigkeit    der    dabei   verwendeten     Modelle   noch   weiter    zu   steigern
(Offenlegungsschrift, Abs. [0005]).


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zur Erstellung
eines Modells eines technischen Systems zu verbessern, ist ein Ingenieur der
Fachrichtung Elektrotechnik anzusehen, der mehrjährige Berufserfahrung im
Bereich der Steuerungs- und Regelungstechnik hat und der insbesondere über
fundierte Kenntnisse in der numerischen Mathematik und den Algorithmen des
maschinellen Lernens verfügt.


2.    Zu Haupt- und Hilfsantrag
Sowohl dem Haupt- wie auch dem Hilfsantrag kann nicht stattgegeben werden,
weil der Gegenstand ihres jeweiligen Patentanspruchs 1 nicht patentfähig ist.




2.1   Zur Lehre des Patentanspruchs 1
Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 gemäß
Hilfsantrag,    der     inhaltlich    sämtliche   Merkmale     des      ursprünglichen
Patentanspruchs 1 (Hauptantrag) umfasst, ein Verfahren zur Erstellung eines

                                           - 12 -



Modells eines technischen Systems vor (Merkmale M1, M2). Hintergrund ist die
Reduzierung des Versuchsaufwands bei der Entwicklung eines technischen
Systems sowie die Steigerung der Genauigkeit der dabei verwendeten Modelle
(Offenlegungsschrift, Abs. [0005]). Ein technisches System ist z. B. eine
Brennkraftmaschine.      Ein     solches     System      ist   durch      Eingangs-    und
Ausgangsgrößen beschreibbar (Offenlegungsschrift, Abs. [0002]). Das Modell des
technischen Systems wird insbesondere für Anwendungen im Rahmen der
Entwicklung bzw. Kalibrierung der Steuerung bzw. Regelung des technischen
Systems benötigt (Merkmal M2a).


Gemäß dem beanspruchten Verfahren werden zwei Modelle, nämlich ein erstes
Datenmodell      und    ein    zweites     Datenmodell     sowie    die    dazugehörigen
Unsicherheiten gebildet. Die Bildung des ersten datenbasierten Modells
einschließlich einer Unsicherheit dieses Modells erfolgt anhand von Messpunkten.
Die Bildung des zweiten datenbasierten Modells einschließlich einer Unsicherheit
dieses Modells erfolgt anhand von Simulationspunkten (Merkmal M5). Die Bildung
des ersten und zweiten datenbasierten Modells einschließlich der Unsicherheit
dieser Modelle erfolgt jeweils mittels einer Regressionsanalyse (Merkmal M5´), so
dass auf diese Weise eine Angabe der Unsicherheit des betreffenden Modells zur
Verfügung steht (Offenlegungsschrift, Abs. [0015]). Eine Angabe der Unsicherheit
des jeweiligen Modells entspricht einem Fehlerbereich (Offenlegungsschrift,
Abs. [0017]; Fig. 2).


Einerseits    werden    Messpunkte       durch      Einstellung    bzw.    Variation   von
Eingangsgrößen und Messung von Ausgangsgrößen am technischen System
bestimmt und andererseits Simulationspunkte durch Einstellung bzw. Variation
von Eingangsgrößen und Simulation von Ausgangsgrößen mittels eines
physikalisch basierten Modells des technischen Systems bestimmt (Merkmale M3,
M3´, M4, M4´).

                                       - 13 -



Im Verlauf des Verfahrens nach Patentanspruch 1 werden die beiden
datenbasierten Modelle weitergebildet. So wird das zweite datenbasierte Modell
dadurch weitergebildet, dass anhand dieses Modells die Eingangsgrößen für eine
weitere Simulation von Ausgangsgrößen ausgewählt werden, welche eine
maximale Unsicherheit dieses Modells verursachen. Daraufhin erfolgt eine
Simulation von Ausgangsgrößen anhand dieser ausgewählten Eingangsgrößen
und der so bereitstehende weitere Simulationspunkt wird zusätzlich zu den schon
bereitstehenden   Simulationspunkten     einer   erneuten   Bildung   des   zweiten
datenbasierten Modells zu Grunde gelegt (Merkmal M6). Auf diese Weise wird
erreicht, die Zuverlässigkeit des zweiten datenbasierten Modells zu erhöhen
(Merkmal M6´).


Das erste datenbasierte Modell wird dadurch weitergebildet, dass anhand dieses
Modells die Eingangsgrößen für eine weitere Messung von Ausgangsgrößen
ausgewählt werden, welche eine maximale Unsicherheit dieses Modells
verursachen. Daraufhin erfolgt eine Messung von Ausgangsgrößen anhand dieser
ausgewählten Eingangsgrößen. Der so bereitstehende weitere Messpunkt wird
dann zusätzlich zu den schon bereitstehenden Messpunkten einer erneuten
Bildung des ersten datenbasierten Modells zu Grunde gelegt (Merkmal M7), so
dass auch die Zuverlässigkeit des ersten datenbasierten Modells gesteigert wird
(Merkmal M7´).


Zusätzlich wird auch der weitere Simulationspunkt dieser erneuten Bildung eines
ersten datenbasierten Modells zu Grunde gelegt, welcher auch der erneuten
Bildung des zweiten datenbasierten Modells zu Grunde gelegt wird, sofern dieser
ein Gültigkeitskriterium erfüllt (Merkmal M8). Anhand des Gültigkeitskriteriums
kann entschieden werden, ob ein Simulationspunkt zur Verbesserung der
Genauigkeit für die Fortbildung des ersten datenbasierten Modells herangezogen
wird (Merkmal M8´).

                                        - 14 -



Gemäß dem Verfahren nach Patentanspruch 1 erfolgt die Weiterbildung des
zweiten datenbasierten Modells wiederholt (Merkmal M9´), so dass sich mit jeder
Wiederholung die Anzahl von Simulationspunkten erhöht (Merkmal M9).


Die Weiterbildung des ersten datenbasierten Modells erfolgt ebenfalls wiederholt,
so dass sich mit jeder Wiederholung die Anzahl von Messpunkten erhöht und sich
mit jeder Wiederholung – bei Erfüllung des Gültigkeitskriteriums – außerdem die
Anzahl von Simulationspunkten erhöht (Merkmal M10). Laut Merkmal M10´ ergibt
sich eine höhere Zuverlässigkeit des ersten datenbasierten Modells dadurch, dass
die zu Grunde liegenden Kombinationen von Eingangs- und Ausgangsgrößen des
technischen Systems sowohl aus Messungen als auch Simulationen mittels eines
physikalischen Modells gewonnen werden.


Die Weiterbildung des ersten und zweiten datenbasierten Modells wird solange
wiederholt, bis ein Abbruchkriterium erfüllt ist (Merkmal M11).


Als Resultat steht das erste datenbasierte Modell als Modell des technischen
Systems für Anwendungen im Rahmen der Entwicklung bzw. Kalibrierung der
Steuerung    bzw.     Regelung    des    technischen     Systems   zur   Verfügung
(Merkmal M12).


2.2   Die mit dem jeweiligen Patentanspruch 1 gemäß Haupt- und Hilfsantrag
beanspruchte Lehre ist so deutlich und vollständig offenbart, dass ein Fachmann
sie ausführen kann.


2.3   Der Gegenstand des jeweiligen Patentanspruchs 1 gemäß Haupt- und
Hilfsantrag beruht jedoch nicht auf erfinderischer Tätigkeit.


2.3.1 Zur Beurteilung der jeweils beanspruchten Lehren sind die Druckschriften
D4 und D5 von besonderer Bedeutung.

                                         - 15 -



So führt die Druckschrift D4, die als nächstliegender Stand der Technik anzusehen
ist, den Fachmann zu einem Verfahren, das dazu dient, ein Modell eines
technischen Systems zu erstellen. Das erzeugte Modell steht für eine Kalibrierung
der Steuerung bzw. Kalibrierung des technischen Systems zur Verfügung. Das
bekannte Verfahren beruht im Wesentlichen auf einer Lokalen Gaußprozess-Regression (LPGR). Der in der D4 vorgestellte Modellierungsansatz ermöglicht
eine flexible und iterative Modellbildung, um robuste und valide dynamische
Modelle   zu erzeugen.      Er   kann    insbesondere für die       Kalibrierung von
Motorsteuergeräten eingesetzt werden (Seite VII, unten, siehe „The adapted
LGPR approach is employed for the ECU calibration of dynamical automotive
systems, which is critical regarding system excitation. …“ – Merkmale M1, M2,
M2a).


Unter Abschnitt 4.1 (Seite 109, „Close-PI Effect“) der D4 werden für die
Kalibrierung eines Dieselmotors die wichtigen Eingangsgrößen genannt, die den
Lärm des Dieselmotors („noise of a diesel engine“) beeinflussen. Diese sind die
Luftmenge („air mass“), der Ladedruck („boost pressure“), die Voreinspritzung
(„pilot injection“), der Kraftstoffdruck („rail pressure“), der Steuerungsanlauf („start
of control“) und die Verzögerung zwischen Vor- und Haupteinspritzung („delay
between pilot injection and main injection“). Insbesondere führt die Verzögerung
zwischen Vor- und Haupteinspritzung zu einem starken nicht-linearen Effekt für
den Lärm des Dieselmotors, welcher lokal auftritt, wenn die Verzögerung zwischen
Vor- und Haupteinspritzung gering ist (Seite 109, zweiter Absatz). Die Figuren 4.6,
4.8 und 4.9 (Seiten 110 bis 113) zeigen die aufgenommenen Messpunkte für die
Eingangsgröße „Verzögerung zwischen Vor- und Haupteinspritzung“ und die
Ausgangsgröße „Lärm des Dieselmotors“. Die Modellierung des Motors erfolgt
mittels verschiedener Regressionsmethoden (GPR, LGPR), deren Resultate
miteinander verglichen werden (Seite 113, erster Absatz u. a.). Der Fachmann
wird erkennen, dass die Messungen inklusive Modellierung genauso gut für eine
Mehrzahl von Ein- und Ausgangsgrößen ausgeführt werden können, deren Werte
variiert werden (Merkmale M3, M3´).

                                               - 16 -



Weiterhin    lehrt   die    D4,     anhand      der     aufgenommenen        Messpunkte    ein
datenbasiertes (erstes) Datenmodell zu erstellen (Seite 113, erster Absatz, siehe
„Thus the motivation of using LGPR for this regression problem is being able to
separate the local effect in order to generate a local model and combine it with the
global one.“). Dies geschieht mittels der Lokalen Gaußprozess-Regression, die
nicht nur eine Erwartungswertfunktion sondern auch eine Varianzfunktion
bereitstellt (Seite 98, Gl. (3.34); Seite 99, Gl. (3.37)). Letztere gibt bekanntlich ein
Maß für die Unsicherheit der modellierten Funktion an einem Abfragepunkt. Damit
geht ein Teil des Merkmals M5 bzw. M5´ aus der D4 hervor.


Ferner wird anhand der Figuren 4.2 bis 4.4 der D4 klar, dass der
Modellierungsansatz und die grafische Benutzeroberfläche der zugehörigen
Modellierungssoftware es erlauben, die Varianz der Gaußprozess-Modellierung
anzuschauen und diejenigen Punkte zu bestimmen, die eine hohe Varianz
besitzen und damit eine schlechte Prognose darstellen (Seite 108, unten). Dass
der Benutzer aber gerade diese Punkte auswählt, um dort neue Messpunkte zu
setzen, geht aus der D4 nicht unmittelbar hervor. Merkmal M7 bzw. M7´ ist somit
allenfalls teilweise in der D4 offenbart.


Mittels der Lokalen Gaußprozess-Modellierung kann z. B. der oben genannte
Dieselmotor      iterativ     vermessen          werden,         während     die   relevanten
Zustandsraumregionen Schritt für Schritt (messtechnisch) erfasst werden und
dadurch das Modell kontinuierlich verbessert wird (Seite VII, unten bis Seite VIII,
oben, siehe „Using LGPR, it is possible to measure the system iteratively while
exploring the relevant state-space regions and improving the quality oft he model
step by step …“ - teilweise Merkmale M10 bzw. M10´).


Dass diese Weiterbildung des Gaußprozess-Modells für den Dieselmotor nicht
unendlich lange wiederholt werden kann, und somit ein Abbruchkriterium
eingeführt    werden        muss,     stellt     aus     Sicht     des     Fachmannes     eine
Selbstverständlichkeit dar (teilweise Merkmal M11). Ferner ist klar, dass bei

                                        - 17 -



Erfüllung eines solchen Abbruchkriteriums ein datenbasiertes Modell zur
Verfügung steht, dass sich dem realen Verhalten des Dieselmotors gut annähert,
diesem also „entspricht“ (Merkmal M12).


Weiterhin beschreibt auch die Druckschrift D5 ein Verfahren zur Erstellung eines
Modells eines technischen Systems. Das bekannte Verfahren beruht auf der
„Bootstrapping“-Technik, mit der eine Gray-Box-Modellierung durchgeführt wird
(Abstract; Fig. 1). Mit dem erstellten Modell wird die Performanz eines
Computersystems - also eines technischen Systems - beim elastischen
Computing in einer Cloud-Umgebung nachgebildet (Abstract; Seite 3, rechte
Spalte, Punkt iii), siehe „the ML is trained on the updated ST and outputs a new
application performance model.“ – Merkmale M1, M2).


Mit Hilfe eines analytischen Modells werden aus diversen Eingangsgrößen x (vgl.
Seite 3, linke Spalte, fünfter Absatz, siehe „… the AM is queried to compute a
prediction of the performance …“; Seite 5, linke Spalte, sechster Absatz, siehe
„This study is, thus, an example of a modeling/learning problem defined over a
large dimensional space (spanning 7 dimensions in our case) and characterized
by a complex performance function.“) Vorhersagewerte am.query(x) für die
Performanz als Ausgangsgröße bestimmt (Merkmale M4, M4´), die als simulierte
Trainingsdaten ST für eine Black-Box-Modellierung dienen (Seite 3, linke Spalte,
Punkt iii)). Im weiteren Verlauf werden die simulierten Trainingsdaten mit
Stichproben aus Messpunkten angereichert, die aus Messungen am laufenden
System stammen (Seite 3, linke Spalte, letzter Absatz bis Seite 3, rechte Spalte,
Punkt iii), siehe „collection of real samples“, „update of the training set“ und „black
box model update“). Auch die Merkmale M3 und M3´ sind damit in der Lehre der
D5 verwirklicht.


Außerdem wird entsprechend der „Bootstrapping“-Technik ein datenbasiertes
Modell (im Folgenden „erstes datenbasiertes Modell“ genannt) anhand von
Messpunkten gebildet (Seite 3, rechte Spalte, Punkt iii), siehe „black box model

                                          - 18 -



update (Line 9): the ML is trained on the updated ST and outputs a new
application performance model.“). Darüber hinaus sieht das Verfahren der D5 die
Bildung   eines    weiteren   datenbasierten        Modells        (im   Folgenden       „zweites
datenbasiertes Modell“ genannt) vor, das sich aus den Simulationspunkten <x,
am.query(x)> des analytischen Modells mittels eines maschinellen Lernschritts
ergibt (Seite 3, linke Spalte, Punkt iii), siehe „black box model construction
(Line 5): the ML is trained on ST and produces a statistical model of the
application´s     performance;     …“).   Beide          Modelle     können      mittels    einer
Regressionsanalyse erstellt werden, was sich unmittelbar der D5 auf Seite 3, linke
Spalte entnehmen lässt (siehe Punkt iii): „… note that the ML can be based on
alternative algorithms, e. g., Decision Trees (DT), Artificial Neural Networks (ANN)
and Support Vector Machines (SVM)…“). Der Fachmann liest an dieser Textstelle
mit,   dass     neben   den   genannten      Algorithmen           zur   Regressionsanalyse
selbstverständlich auch auf einen Gaußprozess zurückgegriffen werden kann,
zumal die „Bootstrapping“-Technik ausweislich der D5 mit beliebigen Algorithmen
des maschinellen Lernens implementiert werden kann (Seite 6, linke Spalte,
vorletzter Absatz, siehe „… the Bootstrapping technique can be implemented with
any black box learner.“). Dem Fachmann ist geläufig, dass ein Gaußprozess zu
den Mess- und Simulationspunkten immer auch eine Funktion für die Varianzen
bzw. Unsicherheiten an Abfragepunkten bereitstellt. Die Merkmale M5 und M5´
sind damit aus der D5 ableitbar.


In der Lehre der D5 werden unter Anwendung der Funktionen „MERGE“, „RNN“,
„RNR“ und „RNR2“, die Gültigkeitskriterien formulieren, Simulationspunkte dem
ersten datenbasierten Modell zu Grunde gelegt. Anhand dieser Kriterien wird
entschieden, ob Simulationspunkte, die schon bei der wiederholten Bildung des
zweiten datenbasierten Modells herangezogen worden sind, Bestandteil eines
Trainingsdatensatzes     bleiben    und    so      für     eine    Fortbildung     des     ersten
datenbasierten Modells herangezogen werden sollen (Seite 4, rechte Spalte,
erster Absatz, siehe „incremental refinement“; Seite 4, rechte Spalte, Mitte bis

                                       - 19 -



Seite 5, linke Spalte, siehe Punkte 1) bis 4)). Merkmal M8 bzw. M8´ geht somit aus
der D5 hervor.


Die D5 zeigt, dass sowohl das erste als auch zweite datenbasierte Modell
wiederholt weitergebildet werden (Seite 3, siehe „Bootstrapping main loop“ und
„Initialization phase“), wobei sich für das zweite datenbasierte Modell mit jeder
Wiederholung die Anzahl der Simulationspunkte erhöht (Seite 3, rechte Spalte,
Abschnitt A, zweiter Absatz; Seite 4, linke Spalte, zweiter Absatz – Merkmale M9,
M9´). Die Bildung des ersten datenbasierten Modells stützt sich auf Messpunkte
aus dem laufenden System und auf Simulationen mittels des analytischen bzw.
physikalischen Modells für das technische System, wobei sich mit jeder
Wiederholung die Anzahl an Messpunkten erhöht (Seite 4, rechte Spalte, erster
Absatz, siehe „This function is responsible for incorporating real samples coming
from the running application into the initial synthetic training set …“ – teilweise
Merkmale M10, M10´).


In der D5 wird das zweite datenbasierte Modell unter Zugrundelegung von
Simulationspunkten aus dem analytischen Modell iterativ so lange weitergebildet,
bis es das analytische Modell hinreichend gut approximiert bzw. eine brauchbare
Menge an Trainingsdaten zur Verfügung steht, so dass das zweite datenbasierte
Modell als zuverlässig angenommen werden kann (Seite 3, rechte Spalte, dritter
Absatz, siehe „Then, proceeding iteratively, it aims to find a value x such that
training ml over a synthetic training set of size x produces a black box model which
well approximates am.“). Ein Abbruchkriterium für die Bildung des zweiten
datenbasierten Modells findet sich z. B. in Seite 4, linke Spalte, zweiter Absatz,
Punkt iv). Dementsprechend wird das erste datenbasierte Modell unter
Zugrundelegung von Messpunkten aus Stichproben ständig weitergebildet, um
ungenaue Vorhersagewerte aus dem analytischen Modell zu korrigieren (Seite 4,
rechte Spalte, erster Absatz, siehe „… thus allowing the black box model to
gradually correct inaccurate performance predictions by the white box model.“).
Dass auch die Weiterbildung des ersten datenbasierten Modells über ein

                                           - 20 -



Abbruchkriterium verfügt (z. B. die maximale Anzahl von Online-Messungen), ist
selbstverständlich (Merkmal M11).


Wird dieses Abbruchkriterium erfüllt, stellt das erste datenbasierte Modell eine
gute Näherung für das gewünschte Modell des betrachteten technischen Systems
dar (Seite 4, rechte Spalte, erster Absatz, siehe „… it allows for the incremental
refinement of the initial performance model.“ - Merkmal M12).


2.3.2 Die Würdigung dieses Materials aus dem Stand der Technik ergibt, dass
der mit dem jeweiligen Patentanspruch 1 gemäß Haupt- und Hilfsantrag
beanspruchte Gegenstand für den Fachmann nahegelegen hat.


Da der zuständige Fachmann stets bestrebt ist, den Kalibrierprozess von
Motorsteuergeräten zu beschleunigen (vgl. D4, siehe Abstract), hatte er
Veranlassung,    sich   überall     dort      kundig   zu   machen,     wo     effektive
Modellierungsmethoden     zum     Einsatz       kommen.     Hierbei   konnte   er   auf
Druckschrift D5 stoßen, die die Anwendung der „Bootstrapping“-Technik auf ein
technisches System lehrt. Für ihn lag es auf der Hand, die Lehre der D5 auf den
aus der D4 bekannten Modellierungsansatz derart anzuwenden, dass neben dem
dort beschriebenen Gaußprozess für das Motorsteuergerät ein analytisches
Modell bzw. Simulationsmodell nach dem Vorbild der D5 entsprechend der
„Bootstrapping“-Technik implementiert wird, um Simulationspunkte in die Bildung
eines mit Messpunkten angereicherten datenbasierten Modells mit einzubeziehen,
damit mit vertretbarem Aufwand ein möglichst genaues datenbasiertes Modell
erstellt werden kann (vgl. D5, Seite 8, rechte Spalte, Abschnitt E, siehe „…if
properly tuned, this technique can yield considerable gains in terms of accuracy
with respect to AM and ML employed singularly …“).


Von einer solchen kombinierten Lehre unterscheidet sich die jeweilige Lehre nach
dem Patentanspruch 1 gemäß Haupt- und Hilfsantrag nur noch dadurch, dass bei
der aus dem Stand der Technik abgeleiteten Lösung keine Auswahl von

                                             - 21 -



Eingangsgrößen für eine Messung bzw. Simulation von Ausgangsgrößen iSd
Merkmale M7 und M7´         bzw. M6 und M6´ stattfindet und dadurch, dass das
anspruchsgemäße erste datenbasierte Modell sukzessive mit immer mehr
Simulationspunkten angereichert wird bzw. dieses auf einer immer breiteren Basis
errichtet wird (restlicher Teil der Merkmale M10, M10´).


Es liegt jedoch im Bereich des Wissens des Fachmanns, dass bei der Erstellung
eines     datenbasierten   Modells      im    Rahmen     einer        automatischen   Online-Optimierung Messpunkte gerade an denjenigen Stellen gesetzt werden, wo sich
die Unsicherheit der Ausgangsgrößen als besonders hoch erweist. Dieser
Umstand ist aus der Black-Box-Modellierung an Verbrennungsmotoren mittels
Gaußprozessen hinreichend bekannt und findet sich z. B. in der D6 (Seite 10634,
linke Spalte, Punkt (6) – restlicher Teil von Merkmal M7, M7´). Ein analoges
Vorgehen bei der Erstellung des datenbasierten Modells aus dem analytischen
Modell der D5 vorzusehen, d. h. Simulationspunkte an Stellen äußerst hoher
Unsicherheit zu setzen, drängt sich aus statistischen Erwägungen heraus
geradezu auf (Merkmal M6, M6´).


Weiterhin ist das verbliebene Unterschiedsmerkmal, d. h. der restliche Teil von
Merkmal M10 bzw. M10´ kein technisches.


Beim System gemäß Druckschrift D5 sind bereits alle erforderlichen Informationen
(Daten,     Datenstrukturen)      und    Anwendungen            (z.    B.   collectSamples(),
updateKB(ST, D) oder ml.train(ST)) vorhanden, und ihre Verwendung gemäß der
„Bootstrapping“-Technik     ist   beschrieben.        Hiervon     ausgehend     betrifft   das
Unterschiedsmerkmal lediglich noch die Frage, ob die Bestimmung einer
passenden Größe des synthetischen Trainingsdatensatzes ST komplett vor der
Verarbeitung der Messpunkte zu einem Gray-Box-Modell stattfinden soll (wie in
der D5, wo die Initialisierungsphase vollständig vor der Updatephase durchlaufen
wird) oder ob die Erstellung eines Gray-Box-Modells für jeden Wert currSize des
synthetischen Trainingsdatensatzes ST erfolgen soll (mit einer entsprechend dem

                                       - 22 -



Wert currSize iterativ anwachsenden Anzahl von Simulationspunkten). Diese
Frage richtet sich aber nicht an den Entwicklungsingenieur. Sie betrifft vielmehr
die reine Programmierung und hier insbesondere eine Umsortierung von
Rechenoperationen unabhängig von technischen Zusammenhängen, die dem
technischen Entwickler im Rahmen einer Spezifikation von einem Systemdesigner
vorgegeben wird.


Dass eine solche Umsortierung von Rechenoperationen auf technischen
Überlegungen beruht, wurde von der Anmelderin schriftsätzlich auch nicht
vorgetragen. Weil das verbliebene         Unterschiedsmerkmal somit zu einer
technischen Problemlösung nichts beiträgt, ist es bei der Prüfung auf Neuheit und
erfinderische Tätigkeit nicht zu berücksichtigen (vgl. T0717/04 v. 28.02.07 – Space
game; BGH GRUR 2011, 125 – Wiedergabe topografischer Informationen; BGH
GRUR 2013, 275 - Routenplanung) (restlicher Teil der Merkmale M10, M10´).


2.3.3 Nach allem ist der Gegenstand des jeweiligen Patentanspruchs 1 gemäß
Haupt- und Hilfsantrag durch den den Druckschriften D4 und D5 entnehmbaren
Stand der Technik nahegelegt und somit nicht patentfähig.


2.4   Mit dem jeweiligen Patentanspruch 1 gemäß Haupt- und Hilfsantrag fallen
auch die jeweiligen übrigen Patentansprüche, da über einen Antrag nur einheitlich
entschieden    werden     kann    (BGH    GRUR      1997,       120   –   Elektrisches
Speicherheizgerät).




                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                             - 23 -



das beschließende Gericht nicht vorschriftsmäßig besetzt war,

   1. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
       kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg
       abgelehnt war,
   2. einem Beteiligten das rechtliche Gehör versagt war,
   3. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
       nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   4. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   5. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses       beim     Bundesgerichtshof          in    Karlsruhe,    durch     eine    beim
Bundesgerichtshof        zugelassene       Rechtsanwältin        oder    durch     einen    beim
Bundesgerichtshof zugelassenen Rechtsanwalt einzulegen.




Dr. Morawek                   Dr. Forkel                   Akintche                 Dr. Städele


                                                                                              Fi
