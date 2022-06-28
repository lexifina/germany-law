---
ecli: "ECLI:DE:BPatG:2022:280622B17Wpat32.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 32/20"
decided: "2022-06-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2022&Sort=1&Seite=18&nr=43233&anz=542&pos=275&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2022-06-28_17_W-pat_32_20_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 32/20 vom 2022-06-28

## Entscheidung

BUNDESPATENTGERICHT


    17 W (pat) 32/20                                                  Verkündet am
 _______________________
                                                                      28. Juni 2022
     (Aktenzeichen)
                                                                           …




                             BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2019 207 238.0


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Juni 2022 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Ing. Baumgardt, der Richterin
Akintche und des Richters Dipl.-Phys. Dr. Städele


beschlossen:


         Der Beschluss der Prüfungsstelle für Klasse G06T des Deutschen
         Patent- und Markenamts vom 22. Oktober 2020 wird aufgehoben
         und die Sache wird zur weiteren Prüfung an das Deutsche Patentund Markenamt zurückverwiesen.



ECLI:DE:BPatG:2022:280622B17Wpat32.20.0

                                      -2-



                                    Gründe


                                       I.


Die vorliegende Patentanmeldung wurde am 17. Mai 2019 beim Deutschen Patentund Markenamt eingereicht. Sie trägt die Bezeichnung


                 „Bereitstellen eines Ergebnisbilddatensatzes “.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 T des
Deutschen Patent- und Markenamts vom 22. Oktober 2020 aus den Gründen des
Bescheids vom 17. April 2020 zurückgewiesen.


In dem in Bezug genommenen Bescheid ist sinngemäß ausgeführt, der Anmeldung
sei keine vollständige und für den Durchschnittsfachmann nacharbeitbare
technische Lehre zu entnehmen. Sofern der Gegenstand des (damaligen)
Patentanspruchs 1 dem Patentschutz zugänglich und verständlich sei, sei er
zumindest mangels Neuheit gegenüber den Druckschriften D1 und D2 nicht
gewährbar. Es sei auch nicht erkennbar, wodurch sich dieser Gegenstand von dem
allgemeinen, aus Druckschrift D3 bekannten Stand der Technik unterscheide. Diese
Argumentation gelte auch für die (damaligen) nebengeordneten Patentansprüche
11 bis 15; deren Gegenstände seien ebenfalls nicht neu.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin beantragt zuletzt,


       den Beschluss der Prüfungsstelle für Klasse G06T des Deutschen
       Patent- und Markenamts vom 22. Oktober 2020 aufzuheben und
       das nachgesuchte Patent mit folgenden Unterlagen zu erteilen:

                                      -3-



            Patentansprüche 1 bis 14, überreicht in der mündlichen
            Verhandlung,

            Beschreibung Seiten 1 bis 51 vom Anmeldetag 17. Mai 2019,
            sowie

            9 Blatt Zeichnungen mit Figuren 1-13, eingegangen am 17.
            Mai 2019.



Der mit einer möglichen Gliederung versehene geltende Patentanspruch 1 lautet
wie folgt, wobei die zum ursprünglichen Patentanspruch 1 neu hinzugekommenen
Merkmale unterstrichen sind:


      M1    1. Computerimplementiertes Verfahren zum Bereitstellen eines
            Ergebnisbilddatensatzes (OD), umfassend

      M2    – Empfangen (REC-ID) eines Eingabebilddatensatzes (ID) eines
            ersten Untersuchungsvolumens (VOL), wobei der Eingabebilddatensatz (ID) ein Röntgenbilddatensatz des ersten Untersuchungsvolumens (VOL) ist,

      M3    – Empfangen oder Bestimmen (REC-DET-IP) eines Eingabebildparameters (IP), wobei der Eingabebildparameter (IP) eine Eigenschaft des Eingabebilddatensatzes (ID) betrifft,

      M4    – Empfangen oder Bestimmen (REC-DET-OP) eines Ergebnisbildparameters (OP),

      M5    – Bestimmen (DET-OD) eines Ergebnisbilddatensatzes (OD) des
            ersten Untersuchungsvolumens (VOL) durch Anwendung einer
            trainierten Generatorfunktion (GF) auf Eingabedaten,


      M5a wobei die Eingabedaten auf dem Eingabebilddatensatz (ID) und dem
            Ergebnisbildparameter (OP) basieren,

                                         -4-



      M5b wobei die Eingabedaten weiterhin auf dem Eingabebildparameter (IP)
             basieren,


      M6     wobei der Ergebnisbildparameter eine oder mehrere der folgenden
             Eigenschaften des Ergebnisbilddatensatzes (OD) betrifft:

             --     Röntgendosis des Ergebnisbilddatensatzes (OD),

             --     Rauschpegel des Ergebnisbilddatensatzes (OD),

             --     dem Ergebnisbilddatensatz (OD) entsprechende Röntgenquelle
                    (XSYS.SRC) und/oder Röntgendetektor (XSYS.DTC),

      M7     und wobei ein Parameter der trainierten Generatorfunktion (GF) auf
             einem GA-Algorithmus basiert,

      M8     – Bereitstellen (PROV-OD) des Ergebnisbilddatensatzes (OD).



Der auf den ursprünglichen Patentanspruch 11 zurückgehende geltende
Patentanspruch 10 lautet gegliedert (die ergänzten Merkmale sind ebenfalls
unterstrichen; ferner wurde ein Schreibfehler in Merkmal N1 korrigiert):

      N1     10.      Verfahren zum Bereitstellen einer trainierten Generatorfunktion
             (GF) und/oder einer trainierten Klassifikatorfunktion (DF), umfassend:

      N2     – Empfangen (TREC-ID-OD-C) eines Eingabebilddatensatzes (ID)
             und      eines   Vergleichsbilddatensatzes    (OD-C)     eines   ersten
             Untersuchungsvolumens (VOL), wobei der Eingabebilddatensatz (ID)
             ein Röntgenbilddatensatz des ersten Untersuchungsvolumens (VOL)
             ist,

      N3     – Empfangen oder Bestimmen eines Eingabebildparameters (IP),

                                 -5-



N3a   wobei    der   Eingabebildparameter      (IP)   eine    Eigenschaft   des
      Eingabebilddatensatzes (ID) betrifft,

N4    – Empfangen (TREC-OP) eines Ergebnisbildparameters (OP),

N4a   wobei der Ergebnisbildparameter eine oder mehrere der folgenden
      Eigenschaften des Vergleichsbilddatensatzes (OD-C) betrifft:

      --   Röntgendosis des Vergleichsbilddatensatzes (OD-C),

      --   Rauschpegel des Vergleichsbilddatensatzes (OD-C),

      --   dem Vergleichsbilddatensatz (OD-C) entsprechende Röntgenquelle (XSYS.SRC) und/oder Röntgendetektor (XSYS.DTC),

N5    – Bestimmen (TDET-OD) eines Ergebnisbilddatensatzes (OD) des
      ersten   Untersuchungsvolumens       (VOL)      durch   Anwendung     der
      trainierten Generatorfunktion (GF) auf Eingabedaten,

N5a   wobei die Eingabedaten auf dem Eingabebilddatensatz (ID) und dem
      Ergebnisbildparameter (OP) basieren,

N5b   wobei die Eingabedaten weiterhin auf dem Eingabebildparameter (IP)
      basieren,

N6    – Bestimmen (TDET-CL) eines Ergebnisklassifikators und eines
      Vergleichsklassifikators    durch       Anwendung       der    trainierten
      Klassifikatorfunktion (DF) auf den Ergebnisbilddatensatz (OD) und
      den Vergleichsbilddatensatz (OD-C),

N7    – Anpassen       (TADJ)     eines       Parameters      der    trainierten
      Generatorfunktion (GF) und/oder der trainierten Klassifikatorfunktion
      (DF)     basierend   auf   dem      Ergebnisklassifikator     und     dem
      Vergleichsklassifikator,

                                                -6-



       N8      – Bereitstellen (TPROV) der trainierten Generatorfunktion (GF)
               und/oder der trainierten Klassifikatorfunktion (DF).



Zum nebengeordneten, auf ein „Bereitstellungssystem zum Bereitstellen eines
Ergebnisbilddatensatzes“ gerichteten Patentanspruch 11, zu den formal nebengeordneten, jedoch auf vorherige Ansprüche zurückbezogenen Patentansprüchen
12, 13 und 14, zu den Unteransprüchen 2 bis 9 sowie zu den weiteren Einzelheiten
wird auf die Akte verwiesen.




                                                II.


Die rechtzeitig eingegangene und auch sonst zulässige Beschwerde führt zur
Aufhebung des angegriffenen Beschlusses und zur Zurückverweisung der Sache
an das Deutsche Patent- und Markenamt gemäß § 79 Abs. 3 Satz 1 Nr. 1 PatG.


1.     Die vorliegende Anmeldung betrifft die computergestützte Verarbeitung
medizinischer Bilddaten.


In   der    Beschreibungseinleitung       ist    ausgeführt,   dass   die   Vorteile   eines
röntgenüberwachten chirurgischen Eingriffs gegen die Strahlenbelastung durch die
absorbierte Röntgendosis abgewogen werden müssten. Da eine Reduzierung der
Röntgendosis typischerweise auch mit einer Reduzierung der Bildqualität bzw. einer
Erhöhung des Signal-Rausch-Verhältnisses einhergehe, müsse häufig ein
Kompromiss zwischen guter Bildqualität und niedriger Röntgendosis gefunden
werden (Offenlegungsschrift, Absätze [0001], [0002]).


Ein zu hohes Signal-Rausch-Verhältnis könne insbesondere auch zu einer
niedrigen    Bildqualität   bei   einer    digitalen   Subtraktionsangiographie        führen
(Offenlegungsschrift, Absatz [0003]). Zwar ließe sich die Bildqualität durch

                                       -7-



verschiedene Rauschunterdrückungsverfahren erhöhen; diese könnten jedoch den
Bildeindruck verändern und/oder zu Artefakten führen. Weiterhin könne das Signal-Rausch-Verhältnis durch optimierte Wahl der Parameter der Röntgenvorrichtung
optimiert werden. Auch dies könne den Bildeindruck verändern, was ein Problem
darstelle, wenn die Bilddaten durch trainierte Algorithmen weiterverarbeitet werden
sollen und die zum Training verwendeten Algorithmen nur mittels einer
beschränkten Anzahl von Röntgenvorrichtungen aufgenommen worden sind
(Offenlegungsschrift, Absätze [0004], [0005]).


Absatz [0006] der Offenlegungsschrift ist zu entnehmen, dass es Aufgabe der
Erfindung sei, eine Möglichkeit bereitzustellen, das Signal-Rausch-Verhältnis eines
Röntgenbilddatensatzes ohne Änderung des Bildeindrucks zu erhöhen.


1.2    Als Fachmann, der mit dieser Aufgabe betraut wird, ist ein Informatiker,
Physiker oder Hochschulingenieur der Fachrichtung Elektrotechnik mit mehrjähriger
Erfahrung auf dem Gebiet der medizinischen Bilddatenverarbeitung anzusehen, der
gute Kenntnisse in der Anwendung und auch in der Entwicklung von Methoden der
künstlichen Intelligenz besitzt.


2.     Zur   Lösung    der   Aufgabe   schlägt   die   Anmeldung   ein   computerimplementiertes Verfahren und ein Bereitstellungssystem zum Bereitstellen eines
Ergebnisbilddatensatzes gemäß den geltenden Patentansprüchen 1 und 11 vor,
ferner ein Verfahren zum Bereitstellen einer trainierten Generatorfunktion und/oder
einer trainierten Klassifikatorfunktion gemäß Patentanspruch 10 sowie eine
Röntgenvorrichtung, ein Computerprogrammprodukt und ein computerlesbares
Speichermedium gemäß den Patentansprüchen 12, 13 und 14.


2.1    Bei dem computerimplementierten Verfahren zum Bereitstellen eines
Ergebnisbilddatensatzes nach Patentanspruch 1 wird zunächst ein Röntgenbilddatensatz eines ersten Untersuchungsvolumens als Eingabebilddatensatz
empfangen (Merkmale M1, M2). Ferner werden ein Eingabe- und ein

                                         -8-



Ergebnisbildparameter bestimmt oder empfangen, wobei der Eingabebildparameter
eine Eigenschaft des Eingabebilddatensatzes und der Ergebnisbildparameter eine
oder    mehrere     vorbestimmte      Eigenschaften     des       bereitzustellenden
Ergebnisbilddatensatzes betrifft (Merkmale M3, M4, teilweise Merkmal M6).


Gemäß den Merkmalen M5, M5a und M5b wird ein Ergebnisbilddatensatz des
ersten Untersuchungsvolumens durch Anwendung einer trainierten Generatorfunktion auf Eingabedaten bestimmt, die auf dem Eingabebilddatensatz sowie auf
dem    Eingabe- und dem       Ergebnisbildparameter    basieren. Der Ergebnisbilddatensatz wird ferner ausgegeben (Merkmal M8).


Weiterhin basiert ein Parameter der trainierten Generatorfunktion auf einem GA-Algorithmus   (Merkmal     M7).    Ein    solcher   Algorithmus     umfasst    eine
Generatorfunktion, die synthetische Daten erzeugt, und eine Klassifikatorfunktion,
die zwischen synthetischen und realen Daten unterscheidet. Generator- und
Klassifikatorfunktion können jeweils künstliche neuronale Netzwerke sein.
Netzwerke, welche mittels eines GA-Algorithmus trainiert werden, waren dem
Fachmann am Anmeldetag unter dem Akronym „GAN“ (= „general adversarial
networks“) wohlbekannt (Offenlegungsschrift, Absatz [0022], [0023]; s. ferner den
unten zitierten Stand der Technik). Das Merkmal M7 bezeichnet gemäß den
Ausführungen in der Anmeldung (siehe z.B. Offenlegungsschrift, Absatz [0025],
[0026], [0054], [0122]) keinen bestimmten Parameter, sondern bringt allgemein zum
Ausdruck, dass die trainierte Generatorfunktion mittels eines GA-Algorithmus im
Zusammenspiel mit einer Klassifikatorfunktion trainiert wurde, wobei dort übliche
Parameter Verwendung finden, die die Generatorfunktion charakterisieren.


Dem Fachmann ist vor dem Hintergrund der Beschreibung der vorliegenden
Patentanmeldung klar, dass unter einem Eingabebildparameter (vgl. Merkmal M3)
ein Parameter zu verstehen ist, der eine Eigenschaft angibt, die sich auf die
Gesamtheit der Pixel- oder Voxelwerte des Eingabebilddatensatzes bezieht. So
kann der Eingabebildparameter - ebenso wie der Ergebnisbildparameter (s.u.) - eine

                                             -9-



Röntgendosis oder einen Rauschpegel des Eingabebilddatensatzes oder eine(n)
dem         Eingabebilddatensatz       entsprechende(n)        Röntgenquelle      und/oder
Röntgendetektor betreffen (vgl. Absätze [0028], [0029], [0034], [0104], [0127],
[0128]). Damit in Übereinstimmung wird in den in der Beschreibung verwendeten
Formeln durchgehend zwischen dem Eingabebilddatensatz X und dem Eingabebildparameter pX unterschieden (vgl. Offenlegungsschrift, Absätze [0097], [0104],
[0106], [0108], [0152], [0161]).


Aus Sicht des Fachmanns implizieren die Merkmale M5 und M5b, dass die trainierte
Generatorfunktion anhand entsprechender (Trainings-)Eingangsbildparameter
trainiert worden ist (vgl. das in Figur 1 i. V. m. den Absätzen [0093] bis [0096]
gezeigte Ausführungsbeispiel, in dem die Bildparameter p1,1 und p2,1 dem
Eingangsbildparameter entsprechen - „Ist eine trainierte Bildverarbeitungsfunktion
[…] auf eine abweichende Parameterkombination abgestimmt, […]“; s. auch Absatz
[0146] i. V. m. Absatz [0152]), so dass sich die Anwendung der trainierten
Generatorfunktion auf den Eingangsbildparameter unmittelbar auf die Pixel- bzw.
Voxelwerte des Ergebnisbilddatensatzes auswirkt. Es ist nachvollziehbar, dass dies
zumindest dann zu genaueren Ergebnisbilddatensätzen führt, wenn der
Eingabebildparameter         nicht    aus    den      Pixel-   bzw.     Voxelwerten    des
Eingabebilddatensatzes abgeleitet worden ist (vgl. Offenlegungsschrift, Absatz
[0029]).


Da die Generatorfunktion gemäß dem Wortlaut des Patentanspruchs 1 bereits
trainiert    ist,   werden   aus     Sicht   des   Fachmanns      bei    Anwendung      der
Generatorfunktion auf die Eingabedaten (vgl. Merkmal M5) Ergebnisbilddatensätze
erzeugt, deren Bildeindruck durch den in Merkmal M6 definierten Ergebnisbildparameter vorgegeben wird (vgl. Offenlegungsschrift, Absatz [0026]).


Dieser Ergebnisbildparameter kann eine Röntgendosis angeben, die zu einem
Ergebnisbilddatensatz führt, dessen Bildeindruck einer hypothetischen Aufnahme
des    Ergebnisbilddatensatzes         mit   dieser     Röntgendosis      entspricht   (vgl.

                                        - 10 -



Offenlegungsschrift, Absätze [0026], [0031]). In diesem Fall approximiert der
Ergebnisbilddatensatz eine reale Aufnahme mit der vorgegebenen Röntgendosis.
Entsprechendes gilt, wenn als Ergebnisbildparameter ein Rauschpegel des
Ergebnisbilddatensatzes gewählt wird. Die Vorgabe der Röntgendosis oder des
Rauschpegels dient dem Zweck, einen Ergebnisbilddatensatz mit einstellbarem -
insbesondere reduziertem Rauschen - zu erzeugen, so dass die bei der Aufnahme
des Eingabebilddatensatzes tatsächlich verwendete Röntgendosis klein gehalten
werden kann (Offenlegungsschrift, Absatz [0035]). Dies wirkt sich selbstverständlich
positiv auf die Erkennbarkeit von Bildinhalten aus.


Gemäß Merkmal M6 kann der Ergebnisbildparameter auch eine Röntgenquelle
und/oder ein Röntgendetektor sein, die bzw. der bei einer hypothetischen Aufnahme
des   Ergebnisbilddatensatzes     verwendet      werden    würde,    so       dass   der
Ergebnisbilddatensatz eine reale Aufnahme einer bestimmten bildgebenden
Röntgeneinrichtung approximiert. Wie der Fachmann der Beschreibung der
Anmeldung entnimmt, soll dadurch ein Arzt, der an die Interpretation der Aufnahmen
einer bestimmten Röntgenvorrichtung gewöhnt ist, Bildinhalte von Aufnahmen
anderer Röntgenvorrichtungen besser erkennen können (vgl. Offenlegungsschrift,
Absatz [0033] i. V. m. Absätzen [0093] bis [0096]).


2.2   Patentanspruch 10 ist auf ein Verfahren zum Bereitstellen einer trainierten
Generatorfunktion   und/oder    einer   trainierten   Klassifikatorfunktion    gerichtet
(Merkmal N1).


Bei diesem Verfahren wird - ähnlich wie bei dem Verfahren nach Patentanspruch 1
- ein Ergebnisbilddatensatz durch Anwendung einer trainierten Generatorfunktion
auf Eingabedaten bestimmt. Diese basieren auf einem Röntgenbilddatensatz eines
Untersuchungsvolumens sowie auf einem Eingabe- und einem Ergebnisbildparameter, wobei diese Größen jeweils auch empfangen werden (teilweise
Merkmale N2 und N3; Merkmale N4, N5, N5a, N5b).

                                       - 11 -



Der Eingabebildparameter betrifft eine Eigenschaft des Eingabebilddatensatzes
und kann zusätzlich auch bestimmt werden (Merkmal N3a; restlicher Teil von
Merkmal N3). Dass die Eingabedaten gemäß Merkmal N5b auch auf dem
Eingabebildparameter basieren, dient der Beschleunigung derjenigen Trainingsverfahren, die den Eingabebildparameter aus dem Eingabebilddatensatz ableiten
(vgl. Offenlegungsschrift, Absatz [0029]).


Des Weiteren wird ein Vergleichsbilddatensatz des ersten Untersuchungsvolumens
empfangen (restlicher Teil von Merkmal N2). Der Ergebnisbildparameter betrifft
eine oder mehrere Eigenschaften dieses Vergleichsbilddatensatzes, wobei diese
Eigenschaften gemäß Merkmal N4a als Röntgendosis oder Rauschpegel des
Vergleichsbilddatensatzes oder als dem Vergleichsbilddatensatz entsprechende(r)
Röntgenquelle und/oder Röntgendetektor festgelegt werden.


Durch Anwendung der trainierten Klassifikatorfunktion auf den Ergebnisbilddatensatz und den Vergleichsbilddatensatz wird ein Ergebnisklassifikator und
ein Vergleichsklassifikator bestimmt (Merkmal N6). Basierend auf diesen beiden
Klassifikatoren wird die trainierte Generatorfunktion und/oder die trainierte
Klassifikatorfunktion angepasst (Merkmal N7). Schließlich wird die trainierte
Generatorfunktion und/oder die trainierte Klassifikatorfunktion bereitgestellt
(Merkmal N8).


Da die Generatorfunktion gemäß dem Wortlaut von Patentanspruch 10 bereits
trainiert ist, beschreibt Patentanspruch 10 aus Sicht des Fachmanns wesentliche
Teilschritte einer fortgeschrittenen Iteration eines GA-Algorithmus, der dem
weiteren Training und der Bereitstellung einer solchen Generatorfunktion dient.


Dabei stellen der Eingabebilddatensatz und der Vergleichsbilddatensatz ein Paar
von Trainingsdaten dar. Die trainierte Generatorfunktion wird aus Sicht des
Fachmanns gemäß den Merkmalen N4, N4a und N5 mit der Maßgabe angewendet,
die Eingabedaten in einen Ergebnisbilddatensatz zu transformieren, der eine reale

                                      - 12 -



Aufnahme       des    Ergebnisbilddatensatzes      approximiert,    welche       unter
Zugrundelegung des Ergebnisbildparameters erhalten wird (vgl. Abschnitt II.2.1).
Die   Maßnahmen      der Merkmale     N6   und N7      dienen dem Zweck, die
Generatorfunktion im Hinblick darauf zu optimieren.


2.3    Auf die übrigen Patentansprüche kommt es vorerst nicht weiter an (s.u.
Abschnitt II.8.)



3.     Das geltende Patentbegehren ist zulässig.


Der geltende Patentanspruch 1 geht auf die ursprünglichen Patentansprüche 1 bis
3 zurück, wobei das neu hinzugekommene Merkmal M6 das nunmehr gestrichene
Merkmal     „wobei   der   Ergebnisbildparameter    (OP)   eine    Eigenschaft    des
Ergebnisbilddatensatzes betrifft“ des ursprünglichen Patentanspruchs 1 mit
umfasst. Der geltende Patentanspruch 10 ergibt sich aus dem ursprünglichen
Patentanspruch 11, wobei die ergänzten Merkmale aus den Absätzen [0030] und
[0159] der Offenlegungsschrift hervorgehen.


Der geltende Patenanspruch 11 beruht auf dem ursprünglichen Patentanspruch 12
mit entsprechenden Ergänzungen, die sich auf dieselben zu den Patentansprüchen
1 und 10 genannten Fundstellen stützen können (vgl. auch die Absätze [0079] und
[0080] der Offenlegungsschrift). Die geltenden nebengeordneten Patentansprüche
12 bis 14 sowie die Unteransprüche 2 bis 9 gehen aus den ursprünglichen
Patentansprüchen 13 bis 15 bzw. 3 bis 10 hervor, wobei lediglich Rückbezüge
angepasst wurden, um dem Wegfall des ursprünglichen Patentanspruchs 2
Rechnung zu tragen.


Die geltende Beschreibung sowie die zugehörigen Figuren sind am Anmeldetag
eingegangen.

                                       - 13 -



4.    Die jeweilige Lehre der geltenden Patentansprüche 1 und 10 ist in der
Anmeldung so deutlich und vollständig offenbart, dass ein Fachmann sie ausführen
kann (§ 34 Abs. 4 PatG).


4.1   Eine für die Ausführbarkeit ausreichende Offenbarung im Sinne von § 34
Abs. 4 PatG ist dann gegeben, wenn es dem Fachmann ohne erfinderisches Zutun
und ohne unzumutbare Schwierigkeiten möglich ist, die Erfindung anhand der
Offenbarung in Verbindung mit dem allgemeinen Fachwissen am Anmeldetag
praktisch so zu verwirklichen, dass der angestrebte Erfolg erreicht wird. Es muss
mindestens ein Weg zum Ausführen eindeutig aufgezeigt werden; allerdings muss
die Erfindung nicht so offenbart werden, dass dem fachkundigen Leser in allen
Einzelheiten vorgeschrieben wird, was er zu tun hat. Generell gilt, dass
Unvollkommenheiten, die sich bei der Ausführung der Erfindung einstellen,
unschädlich sind, wenn das eigentliche Ziel der Erfindung für den Fachmann
erreichbar ist (Schulte, PatG, 11. Auflage (2022), § 34 Rdn 332 ff;
Busse/Keukenschrijver, PatG, 9. Auflage (2020), Rdn 214 ff).


4.2   Die vorstehenden Kriterien sind im vorliegenden Fall erfüllt.


So betreffen die Anweisungen der Patentansprüche 1 und 10 grundlegende, für
Algorithmen auf dem Gebiet der künstlichen Intelligenz typische Datenverarbeitungsschritte.


Die diesen Anweisungen zugrundeliegenden Verfahren sind in der Anmeldung
ausführlich   dargestellt.   Insbesondere   werden   konkrete   Beispiele   für   die
verwendeten Eingabe- und Ausgabegrößen - d.h. für den Eingabe- und
Ergebnisbilddatensatz, den Eingabe- und den Ergebnisbildparameter - angegeben
(vgl. Offenlegungsschrift, Absätze [0011] bis [0018], [0030] bis [0034], [0039],
[0040]). Darüber hinaus sind die trainierte Generatorfunktion sowie wesentliche
Elemente und Teilschritte des - dem Fachmann ohnehin bekannten - GA-Trainingsalgorithmus näher beschrieben (vgl. Offenlegungsschrift, etwa Absätze

                                          - 14 -



[0019] bis [0025], [0049], [0054] bis [0066], [0070] bis [0078], [0093] bis [0101],
[0125] bis [0131], [0146] bis [0164] sowie Figur 2); insbesondere enthält die
Patentanmeldung konkrete Ausführungen zum Verständnis der Merkmale M7 und
O7 und zur Verwendung des Eingabebildparameters als Bestandteil der
Eingabedaten (vgl. Offenlegungsschrift, Absätze [0025] und [0029]). Ferner werden
in der Beschreibung Vorteile genannt, anhand derer der Verwendungszweck der
erfindungsgemäßen      Lösungen     hinreichend     deutlich   erkennbar   ist    (vgl.
Offenlegungsschrift, Absätze [0001] bis [0005], [0026], [0029], [0035], [0077],
[0078], [0096] in Verbindung mit Figur 1).


Auch kann der Fachmann das Ziel der mit den Patentansprüchen 1 und 10
umschriebenen Erfindungen - die Erzeugung und Anwendung einer trainierten
Generatorfunktion,    die    zu   einem     Ergebnisbilddatensatz   im   Sinne     des
Patentanspruchs 1 führt - ohne besondere Schwierigkeiten erreichen. Denn bei der
praktischen Umsetzung eines Algorithmus auf dem Gebiet der künstlichen
Intelligenz gehört es zur üblichen Vorgehensweise des Fachmanns, verschiedene -
selbst entwickelte oder bereits von anderen Fachleuten veröffentlichte -
Trainingsdatensätze    und    Programmbausteine       auszuprobieren     und     derart
anzupassen, dass der Algorithmus zu zufriedenstellenden Ergebnissen führt (z.B.
durch Optimierung charakteristischer Parameter einer Generatorfunktion und durch
Zusammenstellung geeigneter Trainingsdaten). Dies dürfte zwar nicht immer sofort
zum angestrebten Erfolg führen; jedoch ist davon auszugehen, dass der Fachmann
nach einer überschaubaren Anzahl von Versuchen zumindest für bestimmte
Trainingsdatensätze und Parameterkombinationen zu brauchbaren trainierten
Generatorfunktionen gelangt. Dafür sprechen insbesondere die zahlreichen
Veröffentlichungen über neuronale Netzwerke und GA-Algorithmen, die bereits zum
Anmeldetag Stand der Technik waren und ersichtlich zu publizierbaren Resultaten
geführt hatten (vgl. etwa die unten in Abschnitt II.6 genannten Druckschriften D1,
D2 und D6 bis D9 mit den darin enthaltenen Literaturzitaten).

                                        - 15 -



Die der Anmeldung entnehmbare Lehre versetzt den Fachmann somit in die Lage,
die beanspruchten Verfahren mit zumutbarem Aufwand in Form von Programmen
zu implementieren, die eine trainierte Generatorfunktion verwenden oder liefern, bei
deren Anwendung ein Ergebnisbilddatensatz im Sinne des Patentanspruchs 1
erzeugt wird. Dies gilt insbesondere für die computergestützte Umsetzung des mit
Patentanspruch 10 umschriebenen GA-Algorithmus, dessen Teilschritte der
Fachmann mit Hilfe seines Fachwissens und den Angaben in der Anmeldung
geeignet ergänzt.



5.     Für die geltenden Fassungen der Patentansprüche 1 und 10 liegt ein
genereller Patentierungsausschluss gemäß § 1 Abs. 3 i. V. m. Abs. 4 PatG nicht
vor.


5.1    Nach der Rechtsprechung des Bundesgerichtshofs sind mathematische
Methoden nur dann patentierbar, wenn sie der Lösung eines konkreten technischen
Problems mit technischen Mitteln dienen. Welches technische Problem durch eine
Erfindung gelöst wird, ist objektiv danach zu ermitteln, was die Erfindung tatsächlich
leistet. Als nicht-technisch kann eine mathematische Methode nur dann angesehen
werden, wenn sie im Zusammenhang mit der beanspruchten Lehre keinen Bezug
zur gezielten Anwendung von Naturkräften aufweist (BGH GRUR 2005, 141 -
Anbieten interaktiver Hilfe, II.4 b); BGH GRUR 2015, 983 - Flugzeugzustand,
Leitsätze a), b)).


5.2    Das Verfahren gemäß Patentanspruch 1 ist gemäß § 1 Abs. 3 i. V. m. Abs. 4
PatG dem Patentschutz zugänglich.


Denn bei diesem Verfahren handelt es sich um eine mathematische Methode, deren
Leistung darin besteht, aus einem empfangenen Röntgenbilddatensatz einen
neuen, synthetischen Bilddatensatz zu erzeugen, der einen unter bestimmten
(anderen) technischen Bildaufnahmebedingungen erzeugten Röntgenbilddatensatz
approximiert.

                                      - 16 -



Damit zeigt die beanspruchte Lehre einen konkreten Bezug zur gezielten
Anwendung von Naturkräften und stellt die Lösung eines konkreten technischen
Problems dar.


Es ist auch nicht festzustellen, dass einzelne Merkmale des Patentanspruchs 1 nicht
zur Lösung dieses Problems beitragen; zur Überzeugung des Senats gelingt die
Lösung des technischen Problems erst durch das Zusammenwirken aller
Anspruchsmerkmale.


5.3   Auch das Verfahren gemäß Patentanspruch 10 stellt die Lösung eines
konkreten technischen Problems mit technischen Mitteln dar.


Bei diesem Verfahren handelt es sich ebenfalls um eine mathematische Methode,
deren Merkmale ersichtlich dem Zweck dienen, eine trainierte Generatorfunktion
derart anzupassen, dass bei deren Anwendung auf einen Röntgenbilddatensatz ein
weiterer Bilddatensatz erzeugt werden kann, der einen unter bestimmten
technischen     Bildaufnahmebedingungen        erzeugten     Röntgenbilddatensatz
approximiert. Insbesondere liefert das beanspruchte Verfahren einen solchen
weiteren Bilddatensatz (vgl. Merkmale N4 bis N5b).


Auch die mit Patentanspruch 10 beanspruchte mathematische Methode weist damit
einen hinreichenden Bezug zur gezielten Anwendung von Naturkräften auf.

                                         - 17 -



6.    Der bisher ermittelte Stand der Technik steht den Patentansprüchen 1 und
10 nicht patenthindernd entgegen.


6.1   Im Laufe des Verfahrens sind folgende Druckschriften entgegengehalten
worden:


D1)   NIE, D. et al.: Medical Image Synthesis with Context-Aware Generative Adversarial Networks. arXiv, 2016,
      URL: https://arxiv.org/abs/1612.05362 [recherchiert am 09.04.2020]
D2)   US 2019 / 0 090 834 A1
D3)   Generative Adversarial Networks. In: Wikipedia. URL: https://de.wikipedia.org/w/index.php?title=Generative_Adversarial_Networks&oldid
      =186990065, Stand 27.03.2019 [abgerufen am 06.04.2020]
D4)   Bedingte Anweisung und Verzweigung. In: Wikipedia. URL: https://de.wikipedia.org/w/index.php?title=Bedingte_Anweisung_und_Verzweigung
      &oldid=185434103, Stand 06.02.2019 [abgerufen am 09.04.2020]
D5)   DE 101 56 215 A1
D6)   US 2019 / 0 108 904 A1
D7)   Yi, X. [et al.]: Generative Adversarial Network in Medical Imaging: A Review.
      Preprint 1809.07294v2 auf arxiv.org, 5. März 2019
D8)   KANG, E. [et al.]: Wavelet Domain Residual Network (WaveResNet) for Low-Dose-X-Ray CT Reconstruction, Preprint 1703.01383v1 auf arxiv.org,
      4. März 2017
D9)   BASHKIROVA, D. [et al.]: Unsupervised Video-to-Video-Translation. Preprint
      1806.03698v1 auf arxiv.org, 10. Juni 2018.


Die Druckschrift D1 befasst sich mit der Erzeugung eines Röntgenbildes („CT
image“) aus einem Magnetresonanzbild („MR image“) durch Anwendung einer
Generatorfunktion, die mittels eines GA-Algorithmus trainiert worden ist. Dadurch
soll vermieden werden, dass ein reales Röntgenbild aufgenommen wird und ein
Patient dadurch Strahlenbelastungen ausgesetzt ist (vgl. Abstract; Abschnitt 1,

                                          - 18 -



zweiter und vorletzter Absatz). Bei dem in Abschnitt 2.1 näher beschriebenen GA-Algorithmus    wird    die   trainierte    Generatorfunktion     lediglich   auf   das
Magnetresonanzbild angewendet, nicht aber auf Eingabedaten, die ein Röntgenbild
sowie einen Eingabe- und einen Ergebnisbildparameter umfassen. Nur am Rande
wird angesprochen, dass das beschriebene Verfahren nicht nur zur Vorhersage
eines Röntgenbildes, sondern auch zur Reduktion von Bildrauschen verwendet
werden kann (vgl. Abschnitt 5, letzter Satz).


Die Druckschrift D2 zeigt ein Verfahren, bei dem eine im Rahmen eines GA-Algorithmus    trainierte    Generatorfunktion     auf   einen      dreidimensionalen
Mammographiedatensatz angewendet wird, um daraus einen zweidimensionalen
Mammographiedatensatz zu generieren, so dass dieser nicht eigens aufgenommen
werden muss und das untersuchte Gewebe keiner weiteren Strahlenexposition
ausgesetzt ist (Absätze [0003], [0004], [0011]; Figur 1). Bei diesem Verfahren wird
die Generatorfunktion jedoch weder auf einen Eingabeparameter noch auf einen
Ergebnisbildparameter gemäß Merkmal M6 bzw. der Merkmalsgruppe N4 bis N5b
angewendet, sondern allenfalls auf einen geometrischen Richtungsparameter „int
direction“, welcher Bestandteil des dreidimensionalen Eingabebilddatensatzes ist
(vgl. Claim 1 und Absätze [0124], [0126], [0172], [0178] sowie Figuren 5 und 6).
Dies gilt auch für den in Druckschrift D2 beschriebenen Trainingsalgorithmus (vgl.
Absätze [0140], [0168]).


Die Druckschriften D3 und D4 stellen Hintergrundwissen zu GA-Algorithmen und zu
in der Software-Programmierung relevanten bedingten Verzweigungsanweisungen
dar.


Die Druckschrift D5 betrifft ein Verfahren zur Verarbeitung medizinisch relevanter
Daten im Rahmen einer durchzuführenden Untersuchung eines Patienten, bei dem
anhand von eingegebenen symptom- und/oder diagnosespezifischen Informationen
unter Verwendung einer symptom- und/oder diagnosebasierten Datenbank eine

                                        - 19 -



oder   mehrere    zur   Untersuchung    des      Patienten   durchzuführende   Untersuchungsmodalitäten ausgewählt werden (vgl. den dortigen Patentanspruch 1). Um
die Anwendung von GA-Algorithmen zur Erzeugung von Bildern mit vorgegebenen
Bildeigenschaften geht es dabei jedoch nicht.


Die Druckschrift D6 geht von dem Problem aus, dass die Bildqualität von
röntgentomographischen Bildern, die mit geringer Röntgendosis aufgenommen
worden sind, geringer als bei Hochdosisbildern ist (Absatz [0006]). Zur
Problemlösung wird vorgeschlagen, das Rauschen rekonstruierter Bilder zu
reduzieren, indem diese von „deep learning“-Netzwerken verarbeitet werden (Figur
1A, Bezugszeichen 135, 170 sowie Absätze [0028], [0032], [0043]; „DL“ = „deep
learning“). Ein solches „DL network 135“ kann aus mehreren Netzwerken bestehen,
die jeweils für unterschiedliche Gegebenheiten und Parameter eines CT-Scans
optimiert sind (Absätze [0056], [0057], [0064] bis [0066]). Beim Training der
Netzwerke werden verschiedene Klassen von Trainingsdaten verwendet, die
jeweils unterschiedlichen Scangegebenheiten entsprechen (Absätze [0033], [0035],
[0039], [0057], [0058]). Da ein Sichtfeld eines Röntgengeräts („field of view“, „FOV“)
das Bildrauschen beeinflusst, können auch mehrere Sätze von tiefen neuronalen
Netzwerken („deep neural networks“, „DNNs“) zur Rauschreduktion verwendet
werden, wobei ein einzelnes Netzwerk darauf trainiert ist, aus rekonstruierten
Röntgenbildern, die mit einem bestimmten Sichtfeld aufgenommen worden sind,
Bilddaten mit einem vom Nutzer gewünschten Rauschpegel zu erzeugen (Figur 12
sowie Absätze [0123], [0145] bis [0150] und [0158]). Jedoch ist keine
Generatorfunktion offenbart, die mittels eines GA-Algorithmus trainiert worden ist
und deren Eingabedaten einen Eingangs- und einen Ergebnisbildparameter im
Sinne von Patentanspruch 1 oder 10 umfassen.


Die Druckschrift D7 ist ein Übersichtsartikel, der den Einsatz von GA-Algorithmen
in der medizinischen Bildgebung darstellt. In Abschnitt 2.2.2 sind sogenannte
„conditional generative adversarial networks“ beschrieben, mit deren Hilfe
Ergebnisbilder mit gewünschten Eigenschaften erzeugt werden können, wenn dazu

                                      - 20 -



zusätzliche Information bereitgestellt wird. In diesem Fall kann der Prozess zur
Erzeugung eines Ergebnisbilds xg mathematisch in Form der Gleichung xg = G(z, c)
ausgedrückt werden, wobei die Variable c („conditional input“) ein Eingabebild oder
eine Klassenangabe, die Variable z Rauschen und die Größe G eine
Generatorfunktion bezeichnet (vgl. Abschnitt 2.2.2, zweiter bis vierter Absatz in
Verbindung mit Abschnitt 2.1, erster Absatz).


Die Druckschrift D8 befasst sich mit der Reduktion von Rauschen durch Anwendung
eines trainierten neuronalen Netzwerks („WavResNet“) auf verrauschte Bilddaten,
die mittels Wavelet-Zerlegung transformiert worden sind (vgl. Figur 1 und
Abschnitt I. letzter Absatz).


Die Druckschrift D9 beschreibt die Umwandlung von Videos mittels einer
Generatorfunktion, die unter Verwendung eines GA-Algorithmus trainiert worden ist
(vgl. Abschnitt 1).


6.2    Allerdings ist keiner der Druckschriften D1 bis D9 der aus den Merkmalen M3
sowie M5 bis M7 bestehende Merkmalskomplex des Patentanspruchs 1 zu
entnehmen. Insbesondere ist in diesen Druckschriften nicht gezeigt, dass eine
trainierte Generatorfunktion sowohl auf einen Röntgenbilddatensatz als auch auf
einen Eingabe- und einen Ergebnisbildparameter angewendet wird, wobei der
Eingabebildparameter eine Bildeigenschaft des Röntgenbilddatensatzes und der
Ergebnisbildparameter eine der in Merkmal M6 definierten Bildeigenschaften eines
Ergebnisbilddatensatzes betrifft.


6.3    Auch ein Verfahren gemäß Patentanspruch 10 geht aus keiner dieser
Druckschriften hervor. Insbesondere sind die Merkmale N4a bis N5b diesen
Druckschriften nicht zu entnehmen. Diese Merkmale dienen insbesondere dem
Zweck, aus einem Röntgenbilddatensatz einen weiteren Bilddatensatz zu erzeugen,
der einen unter bestimmten technischen Bildaufnahmebedingungen erhaltenen
Röntgenbilddatensatz approximiert. Sie weisen einen hinreichenden Bezug zur

                                            - 21 -



gezielten Anwendung von Naturkräften auf, so dass sie bei der Prüfung der
erfinderischen Tätigkeit zu berücksichtigen sind.


6.4     Derzeit ist für den Senat nicht ersichtlich, wie der Durchschnittsfachmann
ausgehend allein von den Druckschriften D1 bis D9 in naheliegender Weise zur
jeweiligen Lehre der geltenden Patentansprüche 1 und 10 hätte gelangen können.



7.      Die Patentansprüche 1 und 10 umfassen jedoch neue Merkmale, die erst im
Beschwerdeverfahren eingeführt wurden. Diese Ansprüche wurden bisher vom
Deutschen Patent- und Markenamt noch nicht geprüft, insbesondere hat noch keine
auf die Merkmalsgruppen M3 bis M7 sowie N3 bis N5b gerichtete Recherche
stattgefunden.


Weil das Deutsche Patent- und Markenamt somit noch nicht in der Sache selbst
entschieden hat, war die Anmeldung gemäß § 79 Abs. 3 Satz 1 Nr. 1 PatG dorthin
zurückzuverweisen (siehe z.B. Schulte, PatG, 11. Auflage, § 79 Rn. 21).


8.      Da die grundsätzliche Frage der Patentierbarkeit der Patentansprüche 1 und
10 sonach noch offen ist, hat sich der Senat mit den übrigen geltenden
Patentansprüchen nicht weiter befasst.




                          Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


      1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,

                                          - 22 -



    2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
      Erfolg abgelehnt war,
    3. einem Beteiligten das rechtliche Gehör versagt war,
    4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern
      er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
      hat,
    5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
      Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
    6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe durch eine beim Bundesgerichtshof
zugelassene Rechtsanwältin oder durch einen beim Bundesgerichtshof zugelassenen
Rechtsanwalt einzulegen.




 Dr. Morawek               Baumgardt                Akintche                  Dr. Städele
