---
ecli: "ECLI:DE:BPatG:2024:190324B17Wpat16.22.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 16/22"
decided: "2024-03-19"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=6&nr=44133&anz=391&pos=98&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2024-03-19_17_W-pat_16_22_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 16/22 vom 2024-03-19

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 16/22                                               Verkündet am
 _____________________
                                                                 19. März 2024
    (Aktenzeichen)
                                                                      …




                                  BESCHLUSS

                              In der Beschwerdesache
…




              betreffend die Patentanmeldung 10 2021 201 855.6


hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts
auf die mündliche Verhandlung vom 19. März 2024 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Akintche, des
Richters Dipl.-Phys. Univ. Dr. Städele und des Richters Hofmeister


beschlossen:


                         Die Beschwerde wird zurückgewiesen.




ECLI:DE:BPatG:2024:190324B17Wpat16.22.0

                                      -2-



                                    Gründe


                                       I.


Die vorliegende Patentanmeldung ist am 26. Februar 2021 beim Deutschen
Patent- und Markenamt eingereicht worden. Sie trägt die Bezeichnung


           „Verfahren zur Rauschreduzierung in einem Röntgenbild,
 Bildverarbeitungseinrichtung, Computerprogramm und elektronisch lesbarer
                                 Datenträger“.


Die Patentanmeldung wurde durch Beschluss der Prüfungsstelle für Klasse
G06T des Deutschen Patent- und Markenamts vom 05. September 2022 mit
der Begründung zurückgewiesen, dass der Gegenstand des Patentanspruchs
1 nicht als auf einer erfinderischen Tätigkeit (§ 4 PatG) beruhend gelte.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Die Anmelderin stellt den Antrag,


      den Beschluss der Prüfungsstelle für Klasse G06T des Deutschen
      Patent- und Markenamts vom 5. September 2022 aufzuheben und das
      nachgesuchte Patent auf Grundlage folgender Unterlagen zu erteilen:


      -   Patentansprüche 1 bis 14, eingegangen am 26. September 2022,
      -   Beschreibung Seiten 1 bis 26, eingegangen am 26. September 2022
          sowie
      -   4 Blatt Zeichnungen mit Figuren 1 bis 6 vom Anmeldetag 26. Februar
          2021.

                                            -3-



Der geltende Patentanspruch 1 – hier mit einer möglichen Merkmalsgliederung
versehen – lautet:


      M0    Verfahren zur Rauschreduzierung in einem mit einer geringeren
            Dosis als eine Referenzdosis aufgenommenen Niedrigdosis-Röntgenbild (10) mittels eines Rauschreduzierungsalgorithmus
            (9), der einen


            M1       Vorverarbeitungsschritt        (11)          zur    Ermittlung     von
                     Eingangsdaten,


            M2       wenigstens eine trainierte Funktion (7) zur Ermittlung
                     rauschreduzierter Ausgangsdaten aus den Eingangsdaten


            M3       und einen Nachverarbeitungsschritt (14) zur Ermittlung
                     eines Ergebnisbildes (15) aus den Ausgangsdaten,


      umfasst,
      dadurch gekennzeichnet, dass


      M4    wenigstens       ein     wenigstens     eine        gewünschte     durch     die
            Rauschreduzierung          zu    erzielende         Ergebniseigenschaft     des
            Ergebnisbildes         (15) beschreibender Ergebnisparameter (16)
            empfangen oder ermittelt wird,


      M5    und die wenigstens eine Ergebniseigenschaft durch


            M5.1 Modifizierung der Vorverarbeitung zur Einstellung eines aus
                     wenigstens         einem            des        wenigstens         einen
                     Ergebnisparameters           (16)         ermittelten   Rauschwerts

                                          -4-



                     wenigstens eines ersten, eine erste Rauscheigenschaft
                     beschreibenden Rauschparameters,


              M5.2 wobei der Rauschwert von einem Referenzwert, der eine
                     zum   Training      der     trainierten   Funktion   (7)    für   die
                     Trainingsdaten      festgelegte       erste   Rauscheigenschaft
                     beschreibt, abweichend gewählt ist,


        erhalten wird.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt wurden
folgende Druckschriften eingeführt:


        D1:   EP 3 435 326 A1
        D2:   US 10 726 525 B2
        D3:   HARIHARAN, Sai Gokul [u.a.]: Learning-based x-ray image
              denoising utilizing model-based image simulations. In: Springer:
              22th Medical Image Computing and Computer Assisted
              Intervention (MICCAI) - 13-17 October 2019 - Shenzhen, China,
              2019, S. 549-557. - ISBN 978-3-030-32225-0 (P); 978-3-030-
              32226-7 (E). DOI: 10.1007/978-3-030-32226-7_61. URL:
              https://www.researchgate.net/publication/336462240


Zu den weiteren Einzelheiten wird auf die Akte verwiesen.




                                           II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie
führt   jedoch   nicht   zum   Erfolg,    da      der   Gegenstand    des       geltenden

                                             -5-



Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruht und somit
nicht patentfähig ist.


1.      Die vorliegende Patentanmeldung betrifft die Rauschreduzierung in
einem mit einer geringeren Dosis als eine Referenzdosis aufgenommenen
Niedrigdosis-Röntgenbild,                    wobei             der               verwendete
Rauschreduzierungsalgorithmus einen Vorverarbeitungsschritt, wenigstens
eine    trainierte    Funktion   und        einen    Nachverarbeitungsschritt       umfasst
(Offenlegungsschrift OS Abs. [0001]).


Laut Beschreibung der Anmeldung wird die Röntgenbildgebung häufig zur
Überwachung          medizinischer     Eingriffe,     beispielsweise       minimalinvasiver
Interventionen, verwendet. Dabei sollte die angewandte Röntgendosis so
niedrig   wie   vernünftigerweise       möglich      sein,   während       die   notwendige
Bildqualität aufrechterhalten wird (OS Abs. [0002]).


Allerdings führe eine Reduzierung der Röntgendosis zu einem Anstieg des
Rauschens. Bekannte Rauschreduzierungs-Verfahren würden häufig bei
äußerst niedrigen Dosisniveaus scheitern (OS Abs. [0003] und [0004]).


Zwar zeigten sich Verfahren, die auf künstlicher Intelligenz basieren, als
vielversprechend, wenn entweder aufgenommene Paare von registrierten
Niedrig- und Hochdosisbildern oder simulierte Paare von verrauschten Bildern
in der Trainingsphase eingesetzt würden. So werde in der Patentanmeldung DE
10 2019 207 238 A1 vorgeschlagen, für die Rauschreduzierung ein „Generative
Adversarial Network“ (GAN) zu verwenden. Dieses verwende als Eingabedaten
neben       einem        Eingabebilddatensatz          einen       Ergebnisbildparameter
(insbesondere einen Rauschpegel des Ergebnisbilddatensatzes), um letztlich
einen     Ergebnisbilddatensatz        zu     erzeugen,      der   einen     vorgegebenen
Bildeindruck habe. Dabei sei aber nicht nachvollziehbar und nicht kontrollierbar,
mittels welchem Mechanismus der Rauschpegel auf einen bestimmten Wert

                                           -6-



festgelegt werde, beziehungsweise inwiefern Strukturen auftreten können, die
lediglich Artefakte darstellen (OS Abs. [0005] und [0006]).


Hiervon ausgehend soll der Anmeldung die Aufgabe zugrunde liegen, eine
Möglichkeit zur steuerbaren Rauschreduzierung in Röntgenbildern anzugeben,
die aufgrund eines physikalisch basierten Ansatzes nachvollziehbarer, robuster
und verlässlicher sei (OS Abs. [0007]).


Der      zur   Lösung    dieser   Aufgabe    beauftragte        Fachmann     weist     ein
Hochschulstudium der Informationstechnik oder Physik auf und verfügt über
eine      mehrjährige    Berufserfahrung    in     der   Verarbeitung    medizinischer
Röntgenbilddaten.


2.       Die oben genannte Aufgabe soll nach Patentanspruch 1 gelöst werden
durch ein Verfahren zur Rauschreduzierung in einem mit einer geringeren Dosis
als eine Referenzdosis aufgenommenen Niedrigdosis-Röntgenbild (10)
mittels     eines   Rauschreduzierungsalgorithmus         (9)    (Merkmal    M0).      Als
Referenzdosis ist gemäß OS Absatz [0021] eine Standarddosis zu verstehen,
wie sie zur Aufnahme diagnostischer Röntgenbilder typischerweise verwendet
wird.


Das beanspruchte Verfahren zur Rauschreduzierung umfasst einen
     -   Vorverarbeitungsschritt     (11)    zur    Ermittlung    von   Eingangsdaten
         (Merkmal M1),
     -   wenigstens eine trainierte Funktion (7) zur Ermittlung rauschreduzierter
         Ausgangsdaten aus den Eingangsdaten (Merkmal M2)
     -   und   einen    Nachverarbeitungsschritt         (14)   zur   Ermittlung     eines
         Ergebnisbildes (15) aus den Ausgangsdaten (Merkmal M3).

                                            -7-



Diese Schritte M1, M2, M3 sind Teile des Rauschreduzierungsalgorithmus (9)
und im Lichte der unten abgebildeten Figur 1 der Anmeldung i. V. m. der
Beschreibung wie folgt auslegbar:




      Ausschnitt aus Fig. 1 der Anmeldung




      Merkmal       M1:    Der     Vorverarbeitungsschritt       (11),    der   auf   die
      Niedrigdosis-Röntgenbilder (10) angewandt wird, kann laut OS Abs.
      [0022]        ff      eine        Rauschvarianzstabilisierungstransformation,
      beispielsweise eine generalisierte Anscombe-Transformation (GAT),
      umfassen. Durch eine GAT wird erreicht, dass eine Poisson-Verteilung
      von Zufallsgrößen (also z.B. von Photonenereignissen geringer Anzahl)
      in eine Standard-Gauß-Verteilung mit definierter Varianz transformiert
      wird.     Auf       eine     solche    Verteilung       lassen     sich    übliche
      Rauschreduzierungsalgorithmen               anwenden.     Das      Ergebnis     des
      Vorverarbeitungsschritts (11) wird im Patentanspruch 1 Eingangsdaten
      genannt.


      Merkmal M2: Die trainierte Funktion (7) hat den Zweck, aus den
      Eingangsdaten – gemäß Fig. 1 durch Anwenden (13) der trainierten

                                      -8-



      Funktion (7) – rauschreduzierte Ausgangsdaten zu ermitteln. Gemäß OS
      Abs. [0020] kann die trainierte Funktion (7) ein neuronales Netzwerk
      umfassen.


      Merkmal M3: Aus den rauschreduzierten Ausgangsdaten wird in einem
      Nachverarbeitungsschritt (14) ein Ergebnisbild (15) ermittelt. Gemäß
      OS Abs. [0043] kann es sich bei diesem Schritt um eine inverse
      Rauschvarianzstabilisierungstransformation     handeln,     wobei    dem
      Fachmann klar ist, dass hier beispielsweise die zu einer in Merkmal M1
      verwendeten GAT korrespondierende inverse GAT angewandt werden
      kann.


Das beanspruchte Verfahren soll weiterhin dadurch gekennzeichnet sein, dass
wenigstens ein wenigstens eine gewünschte durch die Rauschreduzierung zu
erzielende Ergebniseigenschaft des Ergebnisbildes (15) beschreibender
Ergebnisparameter (16) empfangen oder ermittelt wird (Merkmal M4). Gemäß
Patentanspruch    3     soll   die   Ergebniseigenschaft   eine   Stärke   der
Rauschreduzierung sein. Der Umstand, dass der Ergebnisparameter (16)
„empfangen oder ermittelt“ wird, kann im Kontext der Anmeldung so interpretiert
werden, dass der Ergebnisparameter (16) im Rahmen einer Eingabe eines
Nutzers über eine Benutzerschnittstelle entgegengenommen wird. Das
Merkmal M4 kann also – entsprechend OS Abs. [0044] – so verstanden werden,
dass beispielsweise der Nutzer über den Ergebnisparameter (16) die
gewünschte            Stärke         der       Rauschreduzierung           des
Rauschreduzierungsalgorithmus (9) steuern soll, etwa um eine optimale Stärke
der Rauschreduzierung zu erreichen.


Die wenigstens eine Ergebniseigenschaft soll erhalten werden (Merkmal M5)
durch die Schritte der Merkmale M5.1 und M5.2:

                               -9-



Der Schritt gemäß Merkmal M5.1 besteht aus der Modifizierung der
Vorverarbeitung zur Einstellung eines aus wenigstens einem des
wenigstens einen Ergebnisparameters (16) ermittelten Rauschwerts
wenigstens eines ersten, eine erste Rauscheigenschaft beschreibenden
Rauschparameters.


Das bedeutet für den Fachmann zunächst, dass eine Vorverarbeitung
(11) zu dem Zweck modifiziert werden soll, dass ein Rauschwert eines
Rauschparameters, der eine Rauscheigenschaft beschreibt, eingestellt
werden kann.


Aus Sicht des Fachmanns kann dies realisiert sein, indem eine
Vorverarbeitung (11) dadurch modifiziert wird, dass sie eine GAT
umfasst, deren Rauschvarianz-Parameter σn2 (siehe OS Abs. [0023],
[0042], [0045] sowie ferner die Formel (3) in der D3) auf bestimmte Werte
eingestellt werden.


Der Rauschwert soll gemäß Merkmal M5.1 aus dem Ergebnisparameter
(16) ermittelt werden. Da ein Parameter in der Datenverarbeitung stets
dazu dient, neue Werte zu übernehmen, ist Merkmal M5.1 i. V. m. den
Merkmalen M4 und M5 demnach so auslegbar, dass als Vorverarbeitung
(11) eine GAT eingesetzt wird, und der Nutzer im Zuge dessen den
Rauschwert des Rauschparameters (also den Wert des Parameters σn2
der GAT) auf gewünschte Werte einstellt. Der Fachmann weiß, dass
optimal eingestellte GAT-Parameter es ermöglichen, dass eine GAT die
Rauschverteilung von Niedrigdosis-Bildern an eine Gauß-Verteilung
annähert,      welche      üblicherweise      von      nachgeschalteten
Rauschreduzierungs-Funktionen für eine optimale Rauschreduzierung
vorausgesetzt wird.

                                     - 10 -



      Gemäß Merkmal M5.2 soll der Rauschwert von einem Referenzwert, der
      eine zum Training der trainierten Funktion (7) für die Trainingsdaten
      festgelegte erste Rauscheigenschaft beschreibt, abweichend gewählt
      sein. Daraus schließt der Fachmann, dass sich der Wert des
      Rauschparameters (in der mit Patentanspruch 1 beanspruchten
      Anwendungsphase)      von   einem       Referenzwert   (also   etwa   einem
      speziellen Wert der Rausch-Varianz σ n2) unterscheiden soll, der für die
      Trainingsdaten festgelegt war, mit denen die trainierte Funktion (7) in
      einer mit Patentanspruch 1 nicht beanspruchten, der Anwendungsphase
      vorgelagerten Trainingsphase trainiert wurde.


3.    Der Gegenstand des Patentanspruchs 1 ist nicht patentfähig, denn er
beruht nicht auf einer erfinderischen Tätigkeit gegenüber der Druckschrift D3 in
Verbindung mit der Druckschrift D1. Ob der Inhalt der geltenden Unterlagen
ursprünglich offenbart war, kann daher dahingestellt bleiben (BGH, Urteil vom
18. September 1990 – X ZR 29/89, GRUR 1991, 120 – Elastische Bandage).


3.1   Die Druckschrift D3 lehrt die Erzeugung von Trainingsbilddaten (vgl. den
Titel „[…] Image Simulations“) sowie das Trainieren eines lernbasierten
Rauschreduzierungs-Netzwerks in der GAT-Domäne (vgl. Titel und Formel (7)
mit Beschreibung).


Im Kontext des Lern- bzw. Trainings-Prozesses und zur Bereitstellung von
Trainingsbilddaten beschreibt die Druckschrift D3 im Kapitel „2.2 Denoising of
low-dose X-ray images“ zunächst, wie realistische simulierte Niedrigdosis-Trainingsbilddaten aus Standarddosis-Röntgenbildern mit Hilfe einer GAT
(Formel (3)) gewonnen werden.


Das lernbasierte Rauschreduzierungs-Netzwerk wird mit den simulierten
Trainingsdaten in der GAT-Domäne trainiert (Abs. oberhalb von Formel (7):
„The network … is then trained with P randomly chosen pairs of noisy regions

                                          - 11 -



{l1′ (i), l2′(i)}P i=1“, wobei sich die gestrichenen Parameter auf die GAT-Domäne
beziehen (vgl. Absatz oberhalb von Formel (5): „As mentioned earlier, we have
performed an NVS on yl1 and yl2 as per Eq. 3 to obtain y‘l1 and y‘l2,
respectively“).         Der    Ausdruck        „NVS“    meint         hierbei     eine
Rauschvarianzstabilisierungstransformation (siehe Satz über Formel (3) -
„noise variance stabilization (NVS) based on the generalized Anscombe
transform (GAT)“).


In der D3 werden Möglichkeiten gezeigt, mit „low to low“-Bildpaaren (d. h. mit
simulierten, GAT-transformierten Bildregionen l‘1 und l‘2, die das Rauschen von
Niedrigdosis-Bildern aufweisen) oder auch mit „low to high“-Bildpaaren (d. h.
mit Paaren von Bildregionen eines simulierten Niedrigdosis-Bildes und eines
Standarddosis-Bildes) zu trainieren (Kap. 2.2, letzter Absatz).


Da gemäß der D3 das lernbasierte Rauschreduzierungs-Netzwerk in der GAT-Domäne trainiert wird und folglich in der GAT-Domäne arbeitet, liest der
Fachmann mit, dass das Bild, dessen Rauschen reduziert werden soll, vor der
Anwendung         des    Rauschreduzierungs-Netzwerks     in    die     GAT-Domäne
transformiert und danach mittels einer inversen GAT wieder rücktransformiert
werden muss (wie es z.B. auch in dem Abstract und der Titelfigur der D1 explizit
gezeigt ist).


3.2    Bezogen auf den Patentanspruch 1 zeigt die Druckschrift D3 ein
Verfahren zur Rauschreduzierung in einem mit einer geringeren Dosis als eine
Referenzdosis       aufgenommenen     Niedrigdosis-Röntgenbild         mittels   eines
Rauschreduzierungsalgorithmus (vgl. den Titel “Learning-based X-ray Image
Denoising …”; Kap. „3 Results“- „In Fig. 1, we have presented the input as well
as the processed regions of interest (ROIs) of an angiographic thorax phantom
acquired at 30% of the standard X-ray dose.”). Somit verwirklicht die D3 das
Merkmal M0.

                                     - 12 -



Mit den Niedrigdosis-Trainingsbildern wird eine trainierte Funktion „network
D(l1′, θ)“ in der GAT-Domäne trainiert (Formel (7) und zugehöriger Absatz). Eine
der Methoden, die auf der Anwendung dieser Funktion basieren, ist mit „L2L“
bezeichnet (Kap. 2.2, letzter Absatz „Since the proposed method involves pairs
of low-dose images as input, we have referred to it as L2L (low2low as analogy
to noise2noise [9])“). Damit ist das Merkmal M2 verwirklicht.


Die gemäß der L2L-Methode trainierte Funktion D wird in Verbindung mit einer
Rauschvarianzstabilisierungstransformation NVS angewendet (Bildunterschrift
von Figur 1 (i) - „L2L with NVS“), unter der insbesondere eine GAT zu verstehen
ist (s.o.). Dabei ist für den Fachmann klar, dass sich der Ausdruck „NVS“ in der
Bildunterschrift zu Figur 1 nicht auf die Trainingsbilder bezieht (die ohnehin
NVS-transformiert sind – siehe Formel (7)), sondern (als „Vorverarbeitung“) auf
die Anwendungsphase. Damit ist das Merkmal M1 aus der D3 entnehmbar.


Ferner erkennt der Fachmann, dass bei Anwendung der NVS auch wieder eine
inverse NVS (als „Nachverarbeitung“) erforderlich ist. Zum Nachweis für das
Wissen und Mitlesen des Fachmanns bezüglich der Vor-/Nachverarbeitung wird
auf das Abstract und die Figur 1 der D1 (vgl. Bezugszeichen (7) und (9))
verwiesen. Damit ergibt sich Merkmal M3 implizit aus der D3.


Die D3 verwendet eine NVS bzw. GAT nicht nur zur Erzeugung von
Trainingsbildern, sondern auch in der Anwendungsphase des trainierten
Rauschreduzierungsalgorithmus (s.o., Bildunterschrift Fig. 1 (i) „L2L with
NVS“). Dabei erkennt der Fachmann, dass der Rauschvarianz-Parameter σn2
der in der Anwendungsphase verwendeten GAT in vorteilhafter Weise derart
gewählt (und damit auch empfangen) werden sollte, um eine optimale Stärke
der Rauschreduzierung bei der nachfolgenden Anwendung der Funktion D für
ein jeweils aktuelles Bild zu erreichen (vgl. Satz unterhalb Formel (2) der D3
„The imaging parameters α and σn2 can, for example, be obtained from the
system speciﬁcations or using calibration measurements [11]“). Dass der

                                       - 13 -



Parameter σ n2 der GAT eingestellt wird, um eine gewünschte optimale Stärke
der Rauschreduzierung zu erreichen, ergibt sich auch daraus, dass der Wert
dieses Parameters grundsätzlich jeweils abhängig vom zu verarbeitenden Bild
zu wählen ist, damit die nachfolgende Rauschreduzierungsfunktion D optimal
arbeiten kann (so auch D1 Abs. [0016] letzter Satz „the transform parameters
might also change from image to image“ und Abs. [0022] „The at least one
transform parameter, especially noise stabilization transform parameters, can
be determined from the image data.“)


Somit gehen auch die Merkmale M5 und M5.1 aus D3 hervor.


Nicht unmittelbar aus der D3 entnehmbar ist das verbleibende Merkmal M5.2.


Mit diesem Merkmal kann allerdings eine erfinderische Tätigkeit nicht
begründet werden.


So    verwendet   die   D3   zum    Trainieren      (D3,   Formel   (6))   des    L2L-Rauschreduzierungsalgorithmus Regionen l1′, l2′ der GAT-transformierten
Bilder yl1 und yl2 (Abs. unterhalb Formel (4)). Dem Fachmann ist klar, dass dabei
die Rauschwerte der Trainingsbilder möglichst ähnlich zu den Rauschwerten der
Bilder der Anwendungsphase sein sollten, um die optimale Stärke der
Rauschreduzierung mittels der trainierten Funktion L2L zu erhalten. Daraus ergibt
sich auch, dass die Werte der Rauschvarianzparameter der GAT in der
Trainingsphase und der GAT in der Anwendungsphase nach Möglichkeit gleich sein
sollten.


Wie    zum    Merkmal    M5.1      bereits      ausgeführt,   ist   der    Wert   des
Rauschvarianzparameters der GAT in der Anwendungsphase grundsätzlich
abhängig vom jeweils aktuellen, zu verarbeitenden Bild zu wählen.

                                       - 14 -



Zwar wäre es grundsätzlich möglich, in der Anwendungsphase für jedes neue
Bild,       das         andere        Rauschparameter          aufweist,         den
Rauschreduzierungsalgorithmus             mit    diesen       anderen,         neuen
Rauschparametern konsistent zu trainieren; jedoch ist dem Fachmann bewusst,
dass dies überaus aufwändig ist. Er wird daher in vielen Fällen nicht für jedes
neue Bild, dessen Rauschen reduziert werden soll, die (bereits) trainierte
Funktion auf Basis dieses neuen Bildes neu trainieren, sondern lediglich den
Rauschvarianz-Parameter σ n2 der GAT in der Anwendungsphase so anpassen,
dass die Anwendung der Funktion D zu einer optimalen Rauschunterdrückung
führt (was keine nennenswerten zusätzlichen Aufwände verursacht). In diesem
Fall weicht der einzustellende Rauschvarianz-Parameter σn2 der GAT von dem
der Trainingsbilder ab, so dass auch das verbleibende Merkmal M5.2 erfüllt ist.


Somit ergibt sich der Gegenstand des Patentanspruchs 1 für den Fachmann in
naheliegender Weise aus dem Stand der Technik.


4.      Mit dem nicht patentfähigen Patentanspruch 1 sind auch die weiteren
Patentansprüche des geltenden Antrags nicht schutzfähig, da auf diese
Patentansprüche kein eigenständiges Patentbegehren gerichtet ist und über einen
Antrag nur einheitlich entschieden werden kann (vgl. BGH, Beschluss vom 27. Juni
2007    -   X     ZB   6/05,   GRUR    2007,    862,   Abs.   III.   3.   a)   aa)   -
Informationsübermittlungsverfahren II).

                                        - 15 -



                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde
nicht zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1.    das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2.    bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung
         des Richteramtes kraft Gesetzes ausgeschlossen oder wegen
         Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3.    einem Beteiligten das rechtliche Gehör versagt war,
   4.    ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes
         vertreten   war,   sofern   er nicht    der   Führung   des    Verfahrens
         ausdrücklich oder stillschweigend zugestimmt hat,
   5.    der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist,
         bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt
         worden sind, oder
   6.    der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des
Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe durch
eine beim Bundesgerichtshof zugelassene Rechtsanwältin oder durch einen
beim Bundesgerichtshof zugelassenen Rechtsanwalt einzulegen.




  Dr. Morawek                Akintche            Dr. Städele           Hofmeister
