---
ecli: "ECLI:DE:BPatG:2022:280622B17Wpat2.21.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 2/21"
decided: "2022-06-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2022&Sort=1&Seite=18&nr=43244&anz=542&pos=274&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2022-06-28_17_W-pat_2_21_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 2/21 vom 2022-06-28

## Entscheidung

BUNDESPATENTGERICHT


    17 W (pat) 2/21                                                   Verkündet am
 _______________________
                                                                      28. Juni 2022
    (Aktenzeichen)
                                                                           …




                             BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2019 208 496.6


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Juni 2022 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Ing. Baumgardt, der Richterin
Akintche und des Richters Dipl.-Phys. Dr. Städele


beschlossen:


        Der Beschluss der Prüfungsstelle für Klasse G06T des Deutschen
        Patent- und Markenamts vom 7. Dezember 2020 wird aufgehoben
        und die Sache wird zur weiteren Prüfung an das Deutsche Patentund Markenamt zurückverwiesen.



ECLI:DE:BPatG:2022:280622B17Wpat2.21.0

                                       -2-



                                    Gründe


                                         I.


Die vorliegende Patentanmeldung wurde am 12. Juni 2019 beim Deutschen Patentund Markenamt eingereicht. Sie trägt die Bezeichnung


        „ Bereitstellen eines Differenzbilddatensatzes und einer trainierten
                               Generatorfunktion “ .


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 T des
Deutschen Patent- und Markenamts vom 7. Dezember 2020 aus den Gründen des
Bescheids vom 8. Juni 2020 zurückgewiesen.


In dem in Bezug genommenen Bescheid ist sinngemäß ausgeführt, der Anmeldung
sei keine vollständige und für den Durchschnittsfachmann nacharbeitbare
technische Lehre zu entnehmen. Sofern der Gegenstand des (damaligen)
Patentanspruchs 1 dem Patentschutz zugänglich und verständlich sei, sei er
zumindest mangels erfinderischer Tätigkeit im Hinblick auf Druckschrift D1 nicht
gewährbar. Es sei auch nicht erkennbar, wodurch sich dieser Gegenstand von dem
allgemeinen Stand der Technik der Druckschriften D3 bis D5 unterscheide. Des
Weiteren sei ein Verfahren nach dem (damaligen) Patentanspruch 10 gegenüber
dem aus den Druckschriften D1, D2 und D5 bekannten Stand der Technik nicht neu.
In diesen Druckschriften seien auch Systeme zur Ausführung eines Verfahrens
nach dem (damaligen) Patentanspruch 18 offenbart. Die Gegenstände der
(damaligen) Patentansprüche 19 und 20 seien ebenfalls nicht neu.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.

                                        -3-



Die Anmelderin beantragt zuletzt,


       den Beschluss der Prüfungsstelle für Klasse G06T des Deutschen
       Patent- und Markenamts vom 7. Dezember 2020 aufzuheben und
       das nachgesuchte Patent mit folgenden Unterlagen zu erteilen:


             Patentansprüche 1 bis 20, überreicht in der mündlichen
             Verhandlung,

             Beschreibung Seiten 1 bis 55 vom Anmeldetag 12. Juni 2019,
             sowie

             10 Blatt Zeichnungen mit Figuren 1 bis 13, eingegangen am
             12. Juni 2019;


       hilfsweise,


             die Anmeldung zur weiteren Prüfung an die Prüfungsstelle
             zurückzuverweisen.


Der mit einer möglichen Gliederung versehene geltende Patentanspruch 1 lautet
wie folgt, wobei die zum ursprünglichen Patentanspruch 1 neu hinzugekommenen
Merkmale unterstrichen sind:


      M1     1. Computerimplementiertes Verfahren zum Bereitstellen eines
             Differenzbilddatensatzes    (DDS)   eines   Untersuchungsvolumens
             (VOL), umfassend

      M2     – Empfangen (REC-RDS-1) eines ersten Realbilddatensatzes (RDS-1) des Untersuchungsvolumens (VOL),

      M2a wobei das Untersuchungsvolumen (VOL) ein Gefäß umfasst, wobei
             der erste Realbilddatensatz (RDS-1) das Untersuchungsvolumen
             (VOL) umfassend Kontrastmittel abbildet,

                                         -4-



      M3     – Bestimmen (DET-DDS) des Differenzbilddatensatzes (DDS) des
             Untersuchungsvolumens (VOL) durch Anwenden einer ersten
             trainierten Generatorfunktion (GF-1) auf Eingabedaten,

      M3a wobei die Eingabedaten den ersten Realbilddatensatz (RDS-1)
             umfassen,

      M3b wobei ein Parameter der ersten trainierten Generatorfunktion (GF-1)
             auf einem GA-Algorithmus basiert,

      M4     wobei das Training der ersten Generatorfunktion (GF-1) darauf
             basiert,    die   erste   trainierte   Generatorfunktion   (GF-1)   auf
             Realbilddatensätzen mit einem ersten Rauschpegel anzuwenden und
             das Ergebnis mit Differenzbilddatensätzen mit einem zweiten
             Rauschpegel zu vergleichen,

      M4a wobei der erste Rauschpegel höher ist als der zweite Rauschpegel,

      M5     – Bereitstellen (PRV-DDS) des Differenzbilddatensatzes (DDS).



Der auf den ursprünglichen Patentanspruch 10 zurückgehende geltende
Patentanspruch 10 lautet gegliedert (die ergänzten Merkmale sind ebenfalls
unterstrichen; ferner wurde ein Schreibfehler in Merkmal N3a korrigiert):


      N1     10.    Computerimplementiertes Verfahren zum Bereitstellen einer
             ersten trainierten Generatorfunktion (GF-1), umfassend:

      N2     – Empfangen (TREC-RDS-1) eines ersten Realbilddatensatzes
             (RDS-1) eines Untersuchungsvolumens (VOL),

      N2a    wobei der erste Realbilddatensatz (RDS-1) einen ersten Rauschpegel
             aufweist,

      N2b    wobei das Untersuchungsvolumen (VOL) ein Gefäß umfasst,

                                     -5-



N2c   wobei       der        erste     Realbilddatensatz         (RDS-1)      das
      Untersuchungsvolumen (VOL) umfassend Kontrastmittel abbildet,

N3    – Empfangen       (TREC-DDS-C)          eines     Vergleichsdifferenzbilddatensatzes (DDS-C) des Untersuchungsvolumens (VOL),

N3a   wobei der Vergleichsdifferenzbilddatensatz (DDS-C) einen zweiten
      Rauschpegel aufweist, wobei der erste Rauschpegel höher ist als der
      zweite Rauschpegel,

N4    – Bestimmen (TDET-DDS) eines Differenzbilddatensatzes (DDS) des
      Untersuchungsvolumens (VOL) durch Anwenden einer ersten
      trainierten Generatorfunktion (GF-1) auf erste Eingabedaten,

N4a   wobei die ersten Eingabedaten den ersten Realbilddatensatz (RDS-1)
      umfassen,

N5    – Bestimmen (TDET-CV-1) eines ersten Klassifikationswertes durch
      Anwenden einer ersten trainierten Klassifikatorfunktion (DF-1) auf den
      Differenzbilddatensatz (DDS),

N5a   – Bestimmen (TDET-CV-2) eines zweiten Klassifikationswertes durch
      Anwenden der ersten trainierten Klassifikatorfunktion (DF-1) auf den
      Vergleichsdifferenzbilddatensatz (DDS-C),

N6    – Anpassen (TADJ-1) der ersten trainierten Generatorfunktion (GF-1)
      und/oder der ersten trainierten Klassifikatorfunktion (DF-1) basierend
      auf   dem    ersten      Klassifikationswert    und/oder    dem      zweiten
      Klassifikationswert,

N7    – Bereitstellen (PRV-GF-1) der ersten trainierten Generatorfunktion
      (GF-1).

                                           -6-



Zu den geltenden nebengeordneten Patentansprüchen 18, 19 und 20, zu den
Unteransprüchen 2 bis 9 und 11 bis 17 sowie zu den weiteren Einzelheiten wird auf
die Akte verwiesen.




                                           II.


Die rechtzeitig eingegangene und auch sonst zulässige Beschwerde führt zur
Aufhebung des angegriffenen Beschlusses und zur Zurückverweisung der Sache
an das Deutsche Patent- und Markenamt gemäß § 79 Abs. 3 Satz 1 Nr. 1 PatG.


1.     Die vorliegende Anmeldung betrifft die computergestützte Verarbeitung
medizinischer Bilddaten.


In   der   Beschreibungseinleitung   ist    ausgeführt,   dass   die   Vorteile   eines
röntgenüberwachten chirurgischen Eingriffs gegen die Strahlenbelastung durch die
absorbierte Röntgendosis abgewogen werden müssten. Da eine Reduzierung der
Röntgendosis typischerweise auch mit einer Reduzierung der Bildqualität bzw. einer
Erhöhung des Signal-Rausch-Verhältnisses einhergehe, müsse häufig ein
Kompromiss zwischen guter Bildqualität und niedriger Röntgendosis gefunden
werden (Offenlegungsschrift, Absätze [0001], [0002]).


Ein zu hohes Signal-Rausch-Verhältnis könne insbesondere auch zu einer
niedrigen Bildqualität bei einer digitalen Subtraktionsangiographie (kurz „DSA“)
führen (Offenlegungsschrift, Absatz [0003]). In der DSA würden ein oder mehrere
Gefäße in einem Untersuchungsvolumen durch Röntgenaufnahmen dargestellt,
wobei zur Unterdrückung von weiteren Strukturen im Untersuchungsvolumen
Aufnahmen des Gefäßes ohne Kontrastmittel (sog. Maskenaufnahmen) mit
Aufnahmen des Gefäßes einschließlich eines Kontrastmittels, welches sich im
Gefäß befindet (sog. Füllbilder), kombiniert würden. Bei einem hohen Signal-Rausch-Verhältnis könne insbesondere die notwendige Registrierung eines

                                            -7-



Masken- und eines Füllbilddatensatzes nicht möglich sein, oder das Rauschen
könne      in   der   Registrierung   zu     Artefakten   führen.    Auch     werde    das
Untersuchungsvolumen einer hohen Röntgenbelastung ausgesetzt, da für eine
digitale   Subtraktionsangiographie        sowohl   Aufnahmen       des   Gefäßes     ohne
Kontrastmittel als auch Aufnahmen des Gefäßes einschließlich eines Kontrastmittels aufgenommen werden (Offenlegungsschrift, Absätze [0003] bis [0005]).


Zwar ließe sich die Bildqualität durch verschiedene Rauschunterdrückungsverfahren erhöhen; diese könnten jedoch den Bildeindruck verändern und/oder zu
Artefakten führen. Weiterhin könne das Signal-Rausch-Verhältnis durch optimierte
Wahl der Parameter der Röntgenvorrichtung optimiert werden. Auch dies könne den
Bildeindruck verändern, was ein Problem darstelle, wenn die Bilddaten durch
trainierte Algorithmen weiterverarbeitet werden sollen und die zum Training
verwendeten Algorithmen nur mittels einer beschränkten Anzahl von Röntgenvorrichtungen aufgenommen worden sind (Offenlegungsschrift, Absätze [0006],
[0007]).


Aus einer älteren, nachveröffentlichten Patentanmeldung sei es ferner bekannt,
durch Anwendung einer trainierten Funktion auf einen Realbilddatensatz einen
Differenzbilddatensatz zu bestimmen, ohne eine zusätzliche Maskenaufnahme
durchzuführen. Hierbei entspreche aber der Rauschpegel des Differenzbilddatensatzes dem Rauschpegel des Realbilddatensatzes. Daher könne zwar auf
eine Maskenaufnahme verzichtet werden, für eine Verringerung des Rauschpegels
im Differenzbilddatensatz müsse aber ein Realbilddatensatz mit niedrigem
Rauschpegel und damit hoher Röntgendosis verwendet werden (Offenlegungsschrift, Absatz [0008]).


Es sei daher Aufgabe der Erfindung, basierend auf einem Realbilddatensatz einen
Differenzbilddatensatz      mit   einem      niedrigen    Rauschpegel       bereitzustellen
(Offenlegungsschrift, Absatz [0009]).

                                            -8-



1.2    Als Fachmann, der mit dieser Aufgabe betraut wird, ist ein Informatiker,
Physiker oder Hochschulingenieur der Fachrichtung Elektrotechnik mit mehrjähriger
Erfahrung auf dem Gebiet der medizinischen Bilddatenverarbeitung anzusehen, der
gute Kenntnisse in der Anwendung und auch in der Entwicklung von Methoden der
künstlichen Intelligenz besitzt.


2.     Zur      Lösung     der       Aufgabe       schlägt      die    Anmeldung      ein
computerimplementiertes       Verfahren      und    ein      Bereitstellungssystem   zum
Bereitstellen eines Differenzbilddatensatzes eines Untersuchungsvolumens gemäß
den Patentansprüchen 1 und 18 vor, ferner ein (weiteres) computerimplementiertes
Verfahren zum Bereitstellen einer ersten trainierten Generatorfunktion gemäß
Patentanspruch        10   sowie      ein    Computerprogrammprodukt           und    ein
computerlesbares Speichermedium gemäß den Patentansprüchen 19 und 20.


2.1    Bei dem computerimplementierten Verfahren zum Bereitstellen eines
Differenzbilddatensatzes eines Untersuchungsvolumens gemäß Patentanspruch 1
wird zunächst ein erster „Realbilddatensatz“ des Untersuchungsvolumens
empfangen, der ein Untersuchungsvolumen abbildet, welches ein Gefäß sowie
Kontrastmittel umfasst (Merkmale M1, M2, M2a).


Aus Sicht des Fachmanns ist ein solcher Realbilddatensatz ein Bilddatensatz, der
mit einer bildgebenden Vorrichtung aufgenommen worden ist (vgl. Offenlegungsschrift, Absätze [0016], [0026] - „Dadurch kann bei der Aufnahme der Realbilddatensätze eine niedrigere Röntgendosis verwendet werden […]). Für den Fachmann ist klar, dass ein solcher Realbilddatensatz in Verbindung mit Merkmal M2a
ein Füllbild ist, das bei der digitalen Subtraktionsangiographie aufgenommen
worden    ist   und   neben      kontrastmittelgefüllten     Blutgefäßen   auch   weitere
Bildstrukturen (z.B. Gewebe, Knochen oder chirurgische Instrumente) abbildet.


Gemäß den Merkmalen M3 und M3a wird ein „Differenzbilddatensatz eines
Untersuchungsvolumens“ bestimmt, indem eine erste trainierte Generatorfunktion

                                        -9-



auf Eingabedaten angewendet wird, die den ersten Realbilddatensatz umfassen.
Der Differenzbilddatensatz wird ferner ausgegeben (Merkmal M5).


Hinsichtlich   der    Bedeutung   des    Begriffs     „Differenzbilddatensatz   eines
Untersuchungsvolumens“ ist zu beachten, dass Patentanmeldungen im Hinblick auf
die dort gebrauchten Begriffe gleichsam ihr eigenes Lexikon darstellen (vgl. BGH
GRUR 1999, 909 - Spannschraube). In diesem Zusammenhang wird in Absatz
[0016] der Offenlegungsschrift ein Differenzbilddatensatz als ein Bilddatensatz
definiert, der eine „Differenz einer tatsächlichen Verteilung von Werten und/oder
Intensitäten in einem Untersuchungsvolumen“ abbildet. Ferner entspricht der
Differenzbilddatensatz gemäß Absatz [0118] (zumindest näherungsweise) der
Differenz aus dem ersten Realbilddatensatz und einem Bilddatensatz, der das
kontrastmittelfreie    Untersuchungsvolumen           bezüglich     der       gleichen
Abbildungsgeometrie wie der erste Realbilddatensatz abbildet - also etwa einem
Maskenbilddatensatz.


In Verbindung mit der Lehre des Patentanspruchs 1 interpretiert dies der Fachmann
derart, dass ein Differenzbilddatensatz eines Untersuchungsvolumens eine
Differenz zweier realer Bildaufnahmen dieses Volumens zumindest näherungsweise abbildet (z.B. die Differenz der Strahlungsintensitätsverteilungen eines Füllund eines Maskenbilddatensatzes, vgl. Absätze [0115] und [0118] der Offenlegungsschrift) und das unmittelbare Ergebnis der Anwendung der ersten trainierten
Generatorfunktion auf den ersten Realbilddatensatz ist. Für einen Differenzbilddatensatz D gilt also D ≈ A - B oder D = A - B, wobei A und B Bilddatensätze
sind, die mit einer bildgebenden Vorrichtung aufgenommen worden sind und das
Untersuchungsvolumen zeigen. Dem Absatz [0016] der Offenlegungsschrift kann
der Fachmann entnehmen, dass die Anmeldung den Differenzbilddatensatz im Fall
D = A - B auch als „Subtraktionsbilddatensatz“ bezeichnet.


Eine      Interpretation    des      Begriffs       „Differenzbilddatensatz     eines
Untersuchungsvolumens“ im Sinne eines Bilddatensatzes, der sich von dem ersten

                                          - 10 -



Realbilddatensatz nur irgendwie unterscheidet (vgl. die Option im Prüfungsbescheid
vom 8. Juni 2020), hält der Senat nicht für sachgerecht. Für ein solches Verständnis,
das letztlich dazu führen würde, dass dem im Begriff „Differenzbilddatensatz“
enthaltene Bestimmungswort „Differenz“ kein eigenständiger Bedeutungsgehalt
zukäme, liefert die vorliegende Patentanmeldung auch keine Anhaltspunkte.


Ferner basiert ein Parameter der ersten trainierten Generatorfunktion auf einem GA-Algorithmus      (Merkmal     M3b).    Ein    solcher        Algorithmus      umfasst     eine
Generatorfunktion, die synthetische Daten erzeugt und eine Klassifikatorfunktion,
die zwischen synthetischen und realen Daten unterscheidet. Generator- und
Klassifikatorfunktion können jeweils künstliche neuronale Netzwerke sein.
Netzwerke, welche mittels eines GA-Algorithmus trainiert werden, waren dem
Fachmann am Anmeldetag unter dem Akronym „GAN“ (= „general adversarial
networks“) wohlbekannt (Offenlegungsschrift, Absatz [0020], [0021]; s. ferner den
unten zitierten Stand der Technik). Das Merkmal M3b bezeichnet gemäß den
Ausführungen in der Anmeldung (siehe z.B. Offenlegungsschrift, Absatz [0022],
[0040] bis [0043], [0143] u.a.) keinen bestimmten Parameter, sondern bringt
allgemein zum Ausdruck, dass die trainierte Generatorfunktion mittels eines GA-Algorithmus im Zusammenspiel mit einer Klassifikatorfunktion trainiert wurde, wobei
dort   übliche   Parameter      Verwendung         finden,     die   die    Generatorfunktion
charakterisieren.


Gemäß den Merkmalen M4 und M4a basiert das Training der ersten trainierten
Generatorfunktion darauf, diese auf Realbilddatensätze mit einem ersten
Rauschpegel anzuwenden und das Ergebnis mit Differenzbilddatensätzen mit
einem zweiten, niedrigeren Rauschpegel zu vergleichen. Das bedeutet, dass zum
Trainieren der ersten trainierten Generatorfunktion Paare von Real- und
Differenzbilddatensätzen verwendet werden, wobei der Rauschpegel eines
jeweiligen    Differenzbilddatensatzes       kleiner     als     der       Rauschpegel    des
korrespondierenden Realbilddatensatzes ist. Laut Beschreibung kann durch
Anwendung        einer      derart    trainierten      Generatorfunktion         auf     einen

                                           - 11 -



Röntgenbilddatensatz der Rauschpegel eines Differenzbilddatensatzes gesenkt
werden, ohne gleichzeitig die Röntgendosis und damit die Strahlenbelastung zu
erhöhen, der das Untersuchungsvolumen ausgesetzt ist (Offenlegungsschrift,
Absatz [0029]).


2.2     Mit Patentanspruch 10 wird ein computerimplementiertes Verfahren zum
Bereitstellen einer ersten trainierten Generatorfunktion beansprucht (Merkmal N1).


Bei diesem Verfahren wird eine erste trainierte Generatorfunktion auf einen ersten
Realbilddatensatz angewendet, der ein Untersuchungsvolumen abbildet, welches
ein Gefäß und Kontrastmittel umfasst, so dass ein Differenzbilddatensatz resultiert
(Merkmale N2, N2b, N2c, N4, N4a), d.h. ein Bilddatensatz, der eine Differenz zweier
Bildaufnahmen des Untersuchungsvolumens zumindest näherungsweise abbildet
(s.o., Abschnitt II.2.1).


Zusätzlich wird ein „Vergleichsdifferenzbilddatensatz des Untersuchungsvolumens“
empfangen (Merkmal N3), wobei der erste Realbilddatensatz einen höheren
Rauschpegel als der Vergleichsdifferenzbilddatensatz aufweist (Merkmale N2a,
N3a).    Mittels   einer    ersten   trainierten    Klassifikatorfunktion   wird   für   den
Differenzbilddatensatz und den Vergleichsdifferenzbilddatensatz jeweils ein
Klassifikationswert bestimmt (Merkmale N5, N5a). Basierend auf zumindest einem
dieser Werte wird die erste trainierte Generatorfunktion und/oder die erste trainierte
Klassifikatorfunktion angepasst (Merkmal N6), etwa zur Minimierung einer
Kostenfunktion (vgl. Offenlegungsschrift, Absatz [0143]). Des Weiteren wird die
erste trainierte Generatorfunktion bereitgestellt (Merkmal N7).


Da der Begriff „erste trainierte Generatorfunktion“ impliziert, dass diese Generatorfunktion bereits trainiert ist, beschreibt Patentanspruch 10 aus Sicht des Fachmanns
wesentliche Teilschritte einer fortgeschrittenen Iteration eines GA-Algorithmus, der
dem weiteren Training und der Bereitstellung der Generatorfunktion dient.

                                       - 12 -



Der erste Realbilddatensatz und der zum Training der ersten trainierten Generatorfunktion verwendete Vergleichsdifferenzbilddatensatz stellen ein Paar von
Trainingsdaten dar. Aus Sicht des Fachmanns ist es selbstverständlich, dass nicht
nur der Differenzbilddatensatz, sondern auch der Vergleichsdifferenzbilddatensatz
eine Differenz zweier Bildaufnahmen des Untersuchungsvolumens zumindest
näherungsweise abbildet, da andernfalls nicht garantiert ist, dass das beanspruchte
Verfahren eine trainierte Generatorfunktion liefert, deren Anwendung in einem
Differenzbilddatensatz im Sinne der vorliegenden Anmeldung (s.o., Abschnitt II.2.1)
resultiert.   Der   Vergleichsdifferenzbilddatensatz   kann    insbesondere     ein
Bilddatensatz sein, der die Differenz des ersten Realbilddatensatzes und eines
Bilddatensatzes, der das kontrastmittelfreie Untersuchungsvolumen bezüglich der
gleichen Abbildungsgeometrie wie der erste Realbilddatensatz zumindest
näherungsweise abbildet (Offenlegungsschrift, Absatz [0134]), wie etwa die
Differenz eines Füll- und eines Maskenbilds in der digitalen Subtraktionsangiographie.


2.3    Auf die übrigen Patentansprüche kommt es vorerst nicht weiter an (s.u.
Abschnitt II.8.)


3.     Das geltende Patentbegehren ist zulässig.


Die geltenden nebengeordneten Patentansprüche 1, 10 und 18 bis 20 gehen auf
die ursprünglichen Ansprüche 1, 10 und 18 bis 20 zurück, wobei die in den
Patentansprüchen 1 und 10 neu hinzugekommenen Merkmale M4, M4a sowie N2a
und N3a dem Absatz [0027] der Offenlegungsschrift zu entnehmen sind;
entsprechendes gilt auch für den Patentanspruch 18. Die in Patentanspruch 10
darüber hinaus ergänzten Merkmale N2b und N2c ergeben sich aus den Absätzen
[0012] und [0013] der Offenlegungsschrift.


Die Merkmale der weiteren nebengeordneten Patentansprüche 19 und 20 sowie der
abhängigen Patentansprüche 2 bis 9 und 11 bis 17 gehen aus den jeweiligen am

                                       - 13 -



Anmeldetag eingereichten Patentansprüchen 2 bis 9, 11 bis 17 sowie 19 und 20
hervor.


Die Beschreibung und die Figuren sind am Anmeldetag eingegangen.


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
verwendeten Eingabe- und Ausgabegrößen - d.h. für den ersten Realbilddatensatz,
den Vergleichsdifferenzbilddatensatz und den Differenzbilddatensatz - angegeben.

                                           - 14 -



Darüber hinaus sind die trainierte Generatorfunktion sowie wesentliche Elemente
und Teilschritte des - dem Fachmann ohnehin bekannten - GA-Trainingsalgorithmus
näher beschrieben (vgl. Offenlegungsschrift, Absätze [0017] bis [0022], [0040] bis
[0054] sowie Figuren 2 bis 4 mit Beschreibung); insbesondere enthält die Patentanmeldung konkrete Ausführungen zum Verständnis des Merkmals M3b und zur
Bedeutung des Differenzbilddatensatzes (vgl. Offenlegungsschrift, Absätze [0022],
[0023], und [0115] bis [0119]). Ferner werden in der Beschreibung Vorteile genannt,
anhand derer der Verwendungszweck der erfindungsgemäßen Lösungen
hinreichend deutlich erkennbar ist (vgl. Offenlegungsschrift, Absätze [0016], [0023],
[0026], [0029]).


Auch kann der Fachmann das Ziel der mit den Patentansprüchen 1 und 10
umschriebenen Erfindungen - die Erzeugung und Anwendung einer trainierten
Generatorfunktion,    die    zu    einem     Differenzbilddatensatz   im   Sinne     des
Patentanspruchs 1 führt - ohne besondere Schwierigkeiten erreichen. Denn bei der
praktischen Umsetzung eines Algorithmus auf dem Gebiet der künstlichen
Intelligenz gehört es zur üblichen Vorgehensweise des Fachmanns, verschiedene -
selbst entwickelte oder bereits von anderen Fachleuten veröffentlichte -
Trainingsdatensätze    und       Programmbausteine      auszuprobieren     und     derart
anzupassen, dass der Algorithmus zu zufriedenstellenden Ergebnissen führt (z.B.
durch Optimierung charakteristischer Parameter einer Generatorfunktion und eines
GA-Algorithmus sowie durch Zusammenstellung geeigneter Trainingsdaten). Dies
dürfte zwar nicht immer sofort zum angestrebten Erfolg führen; jedoch ist davon
auszugehen, dass der Fachmann nach einer überschaubaren Anzahl von
Versuchen zumindest für bestimmte Trainingsdatensätze und Parameterkombinationen zu brauchbaren trainierten Generatorfunktionen gelangt. Dafür
sprechen insbesondere die zahlreichen Veröffentlichungen über neuronale
Netzwerke und GA-Algorithmen, die bereits zum Anmeldetag Stand der Technik
waren und ersichtlich zu publizierbaren Resultaten geführt hatten (vgl. etwa die
unten in Abschnitt II.6 genannten Druckschriften D1, D2 und D5 bis D9 mit den darin
enthaltenen Literaturzitaten).

                                        - 15 -



Die der Anmeldung entnehmbare Lehre versetzt den Fachmann somit in die Lage,
die beanspruchten Verfahren mit zumutbarem Aufwand in Form von Programmen
zu implementieren, die eine trainierte Generatorfunktion verwenden oder liefern, bei
deren Anwendung ein Differenzbilddatensatz im Sinne des Patentanspruchs 1
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
Leistung darin besteht, aus einem Bilddatensatz, der ein Untersuchungsvolumen
mit einem Gefäß und mit Kontrastmittel zeigt und einen hohen Rauschpegel
aufweist, einen Bilddatensatz mit einem demgegenüber geringeren Rauschpegel zu
erzeugen unter der Maßgabe, zumindest näherungsweise eine Differenz zweier -

                                        - 16 -



hypothetischer oder bereits durchgeführter - realer Bildaufnahmen eines
Untersuchungsvolumens abzubilden.


Damit zeigt die beanspruchte Lehre einen konkreten Bezug zur gezielten
Anwendung von Naturkräften und stellt die Lösung eines konkreten technischen
Problems dar.


Es ist auch nicht festzustellen, dass einzelne Anspruchsmerkmale nicht zur Lösung
dieses Problems beitragen.


Denn sämtliche Anspruchsmerkmale dienen dem Zweck, aus einem Bilddatensatz
eines     Untersuchungsvolumens       einen      demgegenüber       rauschreduzierten
Bilddatensatz zu erzeugen, dessen Bildinhalt die Differenz zweier Bildaufnahmen
des Untersuchungsvolumens mit und ohne Kontrastmittel approximieren soll. Sie
weisen damit jeweils einen hinreichenden Bezug zur gezielten Anwendung von
Naturkräften auf und tragen somit zur Lösung des konkreten technischen Problems
mit technischen Mitteln bei (vgl. BGH - Flugzeugzustand, a.a.O., Rn. 28 und 29).
Nach der Überzeugung des Senats gelingt die Lösung des technischen Problems
erst durch das Zusammenwirken aller Merkmale des Patentanspruchs 1.


5.3     Auch das Verfahren gemäß Patentanspruch 10 stellt die Lösung eines
konkreten technischen Problems mit technischen Mitteln dar.


Bei diesem Verfahren handelt es sich ebenfalls um eine mathematische Methode,
deren Merkmale ersichtlich dem Zweck dienen, mittels eines GA-Algorithmus eine
trainierte Generatorfunktion derart anzupassen, dass durch deren Anwendung ein
Realbilddatensatz in einen Bilddatensatz mit einem niedrigeren Rauschpegel
transformiert werden kann, welcher zumindest näherungsweise eine Differenz
zweier realer Bildaufnahmen eines Untersuchungsvolumens abbildet. Mit einem
solchen    Differenzbilddatensatz   liefert   das   beanspruchte    Verfahren    einen
Bilddatensatz,   dessen    Rauschpegel        gegenüber   dem      Rauschpegel    des
untransformierten Realbilddatensatzes reduziert ist (vgl. Merkmal N4).

                                         - 17 -



Die mit Patentanspruch 10 beanspruchte mathematische Methode weist damit
einen hinreichenden Bezug zur gezielten Anwendung von Naturkräften auf und
beschreibt die Lösung eines konkreten technischen Problems mit technischen
Mitteln.


6.     Der bisher ermittelte Stand der Technik steht den Patentansprüchen 1 und
10 nicht patenthindernd entgegen.


6.1    Im Laufe des Verfahrens sind folgende Druckschriften entgegengehalten
worden:


D0)    DE 10 2019 207 238 A1
D1)    NIE,   D.   et   al.:   Medical   Image    Synthesis   with   Context-Aware
              Generative Adversarial Networks. arXiv, 2016,
       URL: https://arxiv.org/abs/1612.05362 [recherchiert am 09.04.2020]
D2)    US 2019 / 0 090 834 A1
D3)    Generative Adversarial Networks. In: Wikipedia. URL: https://de.wikipedia.org/w/index.php?title=Generative_Adversarial_Networks&oldid=
       186990065, Stand 27.03.2019 [abgerufen am 06.04.2020]
D4)    GOODFELLOW, Ian J. [u.a.]: Generative Adversarial Nets. 10-06-2014.
       arXiv:1406.2661v1. S. 1-9. URL: https://arxiv.org/pdf/1406.2661 [abgerufen
       am 2018-09-27]
D5)    MONTOYA, Juan C., et al.: 3D Deep Learning Angiography (3D-DLA) from
       C-arm Conebeam CT. American Journal of Neuroradiology, 2018, 39. Jg.,
       Nr. 5, Seiten 916-922
D6)    WOLTERINK, Jelmer M., et al.: Generative Adversarial Networks for Noise
       Reduction in Low-Dose CT. IEEE transactions on medical imaging, 2017, 36.
       Jg., Nr. 12, Seiten 2536-2545
D7)    HAO, H.: Vessel Layer Separation of X-ray Angiographic Images using Deep
       Learning Methods. Master Thesis, TU Delft, 2018, online verfügbar unter

                                        - 18 -



      https://repository.tudelft.nl/islandora/object/uuid%3Aae819077-c7cd-4737-
      ad6ecb39e3bd
D8)   UNBERATH, M. [et al.]: Deep Learning-based Inpainting for Virtual DSA.
      Konferenzbeitrag     vom     November      2017,    online   verfügbar    unter
      https://www.researchgate.net/publication/321251358_Deep_Learningbased_Inpainting_for_Virtual_DSA
D9)   ARMANIUOS, K. [et al.]: Unsupervised Medical Image Translation Using
      Cycle- MedGAN. Preprint 1903.03374v1 auf arXiv.org, 8. März 2019.


Die Druckschrift D0 ist die Offenlegungsschrift einer Patentanmeldung, die vor dem
Anmeldetag der vorliegenden Patentanmeldung (am 17. Mai 2019) angemeldet,
aber erst nach diesem veröffentlicht worden ist. Die D0 ist somit nur bei der Prüfung
der Neuheit zu berücksichtigen.


Die Druckschrift D0 nimmt ein Verfahren mit den Merkmalen M1, M2, M3, M3a, M3b
und M5 vorweg (vgl. die dortigen Patentansprüche 1, 8 und 12 sowie Absätze
[0051], [0052], [0079], [0080]). Zum Training der zum Einsatz kommenden
Generatorfunktion kann diese auf einen Eingabebilddatensatz angewendet werden
(z.B. auf einen Füllbilddatensatz, vgl. Absatz [0051]; allerdings wird in diesem
Zusammenhang ein Kontrastmittel nicht ausdrücklich erwähnt). Zum Anpassen
eines Parameters der trainierten Generatorfunktion und/oder einer trainierten
Klassifikatorfunktion wird letztere auf den Ergebnisbilddatensatz und einen
Vergleichsbilddatensatz angewendet, so dass ein Ergebnisklassifikator und ein
Vergleichsklassifikator resultiert. Diese beiden Klassifikatoren werden anschließend
miteinander verglichen (vgl. Absätze [0071], [0072], [0082], [0150] bis [0155], [0159]
sowie Anspruch 11); um einen Vergleich eines Differenzbilddatensatzes mit einer
anderen Größe (vgl. Merkmal M4) geht es dabei allerdings nicht. Der Rauschpegel
von Eingabe-, Vergleichs- und Ergebnisbilddatensatz entspricht jeweils einem
bestimmten Signal-Rausch-Verhältnis (Absätze [0030], [0032], [0037]).

                                        - 19 -



Die Druckschrift D1 befasst sich mit der Erzeugung eines Röntgenbildes („CT
image“) aus einem Magnetresonanzbild („MR image“) durch Anwendung einer
Generatorfunktion, die mittels eines GA-Algorithmus trainiert worden ist. Dadurch
soll vermieden werden, dass ein reales Röntgenbild aufgenommen wird und ein
Patient dadurch Strahlenbelastungen ausgesetzt ist (vgl. Abstract; Abschnitt 1,
zweiter und vorletzter Absatz). Der GA-Algorithmus ist in Abschnitt 2.1 näher
beschrieben; über das Training einer Generatorfunktion im Hinblick auf die
Erzeugung eines Differenzbilddatensatzes aus einem Bilddatensatz, welcher ein
Kontrastmittel zeigt und dessen Rauschpegel höher als der Rauschpegel eines
Vergleichsdifferenzbilddatensatzes ist, findet sich jedoch nichts. Es wird lediglich
am Rande angesprochen, dass das beschriebene Verfahren nicht nur zur
Vorhersage eines Röntgenbildes, sondern auch zur Reduktion von Bildrauschen
verwendet werden kann (vgl. Abschnitt 5, letzter Satz).


Die Druckschrift D2 zeigt ein Verfahren, bei dem eine trainierte Generatorfunktion
auf einen dreidimensionalen Mammographiedatensatz angewendet wird, um
daraus einen zweidimensionalen Mammographiedatensatz zu erzeugen. Als
Motivation wird die Vermeidung einer zusätzlichen Strahlenexposition angeführt
(Absätze [0003], [0004], [0011]; Figur 1). Jedoch ist weder ein Kontrastmittel im Bild
vorhanden,    noch    ist   der   zweidimensionale   Mammographiedatensatz        ein
Differenzbilddatensatz im Sinne der vorliegenden Patentanmeldung. Beim Training
der Generatorfunktion (vgl. Absätze [0137] bis [0171] i. V. m. Figuren 3 und 4) wird
das Ergebnis der Anwendung der trainierten Generatorfunktion auch nicht mit
Differenzbilddatensätzen verglichen; um eine Reduktion eines Rauschpegels geht
es ebenfalls nicht.


Die Druckschriften D3 und D4 stellen Hintergrundwissen zu GA-Algorithmen dar.


Die Druckschrift D5 stellt ein Verfahren vor, bei dem aus dreidimensionalen
rekonstruierten Röntgenbildern eines Untersuchungsobjekts, dessen Blutgefäße
ein Kontrastmittel enthalten (sogenannten „fill scans“), mittels eines neuronalen

                                          - 20 -



Faltungsnetzwerks („convolutional neural network“, „CNN“) 3D-Angiogramme der
Blutgefäße („subtracted 3D cerebral angiograms“) generiert werden (vgl. Abstract,
Seite 917, linke Spalte, erster und zweiter vollständiger Absatz). Ein solches 3D-Angiogramm besteht aus Voxeln, die von einem CNN als Blutgefäß („vasculature“)
klassifiziert worden sind (vgl. Figur 2 sowie S. 918, linke Spalte unten - „The final
vasculature tissue was used to generate the 3D-DLA images“ i. V. m. dem
Druckschriftentitel „3D Deep Learning Angiography (3D-DLA)“) und stellt einen
Differenzbilddatensatz im Sinne der vorliegenden Anmeldung dar. Die Druckschrift
D5 nennt allerdings nur wenige Einzelheiten zu dem konkret verwendeten
Trainingsverfahren und beschreibt insbesondere keinen GA-Algorithmus. Eine
Reduktion eines Rauschpegels wird ebenfalls nicht angesprochen.


Die Druckschrift D6 zeigt verschiedene Verfahren, bei denen aus einem
Niedrigdosisröntgenbild („low dose CT image“) durch Anwenden eines auf Basis
eines GA-Algorithmus trainierten Generatornetzwerks ein Normaldosisröntgenbild
(„routine-dose CT image“, „denoised CT“) erzeugt wird (vgl. Abstract, Abschnitt II.,
sowie Figuren 1 und 2). Allerdings stellen weder dieses Bild noch die gemäß
Abschnitt II.C zum Training verwendeten Röntgenbilder Differenzbild- oder
Vergleichsdifferenzbilddatensätze im Sinne der vorliegenden Anmeldung dar; in
Druckschrift   D6   wird   auch   nicht    gezeigt,   dass   die   Röntgenbilder   ein
kontrastmittelgefülltes Untersuchungsvolumen umfassen.

Die Druckschrift D7 beschäftigt sich mit der Segmentierung von Adern in
angiographischen Bildern. In Abschnitt 2 (vgl. insbesondere Figur 2.1) wird
beschrieben, dass eine trainierte Generatorfunktion („Generator G“) auf ein
Eingabeangiogramm („Input XA“) angewendet wird - d.h. auf einen Bilddatensatz,
der ein Untersuchungsvolumen mit Gefäßen sowie Kontrastmittel abbildet (Figur 2.1
i. V. m. Abschnitt 2.1.1, zweiter Satz sowie Abschnitt 2.2, vorletzter Satz). Dadurch
wird ein Bilddatensatz erhalten, in dem die Blutgefäße besser zu sehen sind, aber
deren umgebende Strukturen fehlen (Figur 2.1 - Bild über dem Text „Generated“ i.
V. m. Abschnitt 2.1.2). Die trainierte Generatorfunktion wird mittels eines GA-

                                        - 21 -



Algorithmus erhalten (Figur 2.1 i. V. m. Abschnitt 2.2, erster Absatz und „Algorithm
1“ auf Seite 10). Im zweiten Absatz auf Seite 8 ist ferner erwähnt, dass ein
„adversarial training“ gute Rauschunterdrückungsergebnisse liefert. Da die zum
Training verwendeten Referenzbilder ungenau und verrauscht sind, wird allerdings
konkret vorgeschlagen, zur Erzeugung besserer Referenzbilder genauere manuelle
Annotationen sowie „noisy label learning“-Techniken zu verwenden (Abschnitt 3.2,
Punkt 2.).


Die Druckschrift D8 befasst sich mit einer Methode zur Erzeugung von DSA-Maskenbilddatensätzen aus Füllbilddatensätzen („virtual DSA“, s. Abschnitt I.,
zweiter Absatz, erster Satz) mittels eines neuronalen Netzwerks (Figur 1 sowie
Absatz II), um Bewegungsartefakte bei der Anwendung von DSA auf bewegliche
Objekte zu vermeiden (Abschnitt I., erster Absatz). Dabei werden die Adern
entsprechenden Bildbereiche segmentiert (vgl. die „defect images“ in Figur 2) und
anschließend von dem neuronalen Netzwerk auf Basis der umgebenden
Bildbereiche aufgefüllt („semi-blind inpainting“, vgl. Figur 2 und linke Spalte unter
Figur 2, erster vollständiger Absatz). Um die Berechnung von Differenzbilddatensätzen geht es dabei nicht; zudem kommt kein GA-Algorithmus zum
Einsatz.


Die Druckschrift D9 beschreibt eine Erweiterung eines GA-Algorithmus für Bild-zu-Bild-Translationsprobleme, bei denen keine pixelweise gepaarten Trainingsdaten
vorliegen (Abstract, Abschnitt 1, dritter und fünfter Absatz). Die Erweiterung besteht
in der Einführung einer zweiten Generatorfunktion G2, die das durch die erste
Generatorfunktion    G1   erzeugte   Bild   wieder   auf   das   ursprüngliche    Bild
rücktransformieren soll (Figur 1, Abschnitt II, insbesondere Gleichung (2)). Der
Unterschied zwischen dem rücktransformierten und dem ursprünglichen Bild, der
„cycle consistency loss“, wird bei der iterativen Optimierung zusätzlich berücksichtigt (Gleichungen (2) und (6)). Als Anwendungsfälle sind die Erzeugung von
Röntgenbildern aus PET-Aufnahmen sowie die Korrektur von Bewegungsartefakten
in Magnetresonanzaufnahmen gezeigt (erste Seite, rechte Spalte, letzter Satz i. V.

                                      - 22 -



m. Figuren 1 bis 3). Dabei wird kein Differenzbilddatensatz im Sinne der
vorliegenden Patentanmeldung erzeugt; um eine Reduktion eines Rauschpegels
geht es ebenfalls nicht.


6.2   Somit sind keiner der Druckschriften D0 bis D9 die neuen Merkmale M4 und
M4a des Patentanspruchs 1 hinsichtlich des Trainings der ersten trainierten
Generatorfunktion zu entnehmen.


Auch ein Verfahren gemäß Patentanspruch 10 geht aus keiner dieser
Druckschriften   hervor.   Dies gilt insbesondere für den      Merkmalskomplex
N1/N2/N2a/N3/N3a/N4, dessen Merkmale der Reduktion eines Rauschpegels
dienen und damit einen hinreichenden Bezug zur gezielten Anwendung von
Naturkräften aufweisen und bei der Prüfung der erfinderischen Tätigkeit zu
berücksichtigen sind.


Derzeit ist für den Senat nicht ersichtlich, wie der Durchschnittsfachmann ausgehend allein von den Druckschriften D1 bis D9 in naheliegender Weise zur
jeweiligen Lehre der Patentansprüche 1 und 10 hätte gelangen können.


7.    Die Patentansprüche 1 und 10 umfassen jedoch neue, aus der Beschreibung
stammende Merkmale, die erst im Beschwerdeverfahren eingeführt wurden. Diese
Ansprüche wurden bisher vom Deutschen Patent- und Markenamt noch nicht
geprüft, insbesondere hat noch keine auf die Merkmalsgruppen M4/M4a und N2 bis
N4 gerichtete Recherche stattgefunden.


Weil das Deutsche Patent- und Markenamt somit noch nicht in der Sache selbst
entschieden hat, war die Anmeldung gemäß § 79 Abs. 3 Satz 1 Nr. 1 PatG dorthin
zurückzuverweisen (siehe z.B. Schulte, PatG, 11. Auflage, § 79 Rn. 21).


8.    Da die grundsätzliche Frage der Patentierbarkeit der auf computerimplementierte Verfahren gerichteten Patentansprüche 1 und 10 noch offen ist, hat
sich der Senat mit den übrigen geltenden Patentansprüchen nicht weiter befasst.

                                            - 23 -




                         Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


    1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
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




 Dr. Morawek                Baumgardt                Akintche                 Dr. Städele
