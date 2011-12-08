---
ecli: "ECLI:DE:BPatG:2011:081211B21Wpat56.09.0"
court: "Bundespatentgericht"
spruchkoerper: "21"
aktenzeichen: "21 W (pat) 56/09"
decided: "2011-12-08"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=83&nr=23028&anz=1310&pos=1245&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-12-08_21_W-pat_56_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002a.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0073.md"]
---

# Bundespatentgericht, 21 W (pat) 56/09 vom 2011-12-08

## Entscheidung

BUNDESPATENTGERICHT


 21 W (pat) 56/09                                                    Verkündet am
_______________                                                   8. Dezember 2011
    (Aktenzeichen)                                                        …




                              BESCHLUSS

                            In der Beschwerdesache


             betreffend die Patentanmeldung 10 2006 039 957.9-35


…




hat der 21. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts aufgrund der mündlichen Verhandlung vom 8. Dezember 2011 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Winterfeldt sowie der Richter Dr. Kortbein,
Dipl.-Phys. Dr. Müller und der Richterin Dipl.-Phys. Zimmerer




BPatG 154
05.11

                                       -2-



beschlossen:


       1. Auf die Beschwerde der Anmelderin wird der Beschluss der
         Prüfungsstelle für Klasse A 61 B des Deutschen Patent- und
         Markenamts vom 20. Januar 2009 aufgehoben und das Patent
         DE 10 2006 039 957 erteilt.


       Bezeichnung: Verfahren zur Auswertung der Herzratenvariabilität


       Anmeldetag: 25. August 2006.


       Der Erteilung liegen folgende Unterlagen zugrunde:


       Patentansprüche 1 bis 7 gemäß Schriftsatz vom 20. Juni 2011 als
       Hilfsantrag


       Beschreibung Seiten 1 bis 3, 5 bis 15 und 18 vom Anmeldetag,
       Seiten 16 und 17, eingegangen am 23. November 2006,
       Seiten 4 und 4a, eingegangen am 20. Juni 2011,


       Figuren 6 bis 10, 12 und 13 vom Anmeldetag, 1 bis 5 und 11, eingegangen am 23. November 2006.


       2. Die weitergehende Beschwerde wird zurückgewiesen.


       3. Die Rückzahlung der Beschwerdegebühr wird angeordnet.

                                            -3-



                                     Gründe


                                             I


Die Patentanmeldung mit dem Aktenzeichen 10 2006 039 957.9-35 wurde am
25. August 2006 unter der Bezeichnung "Verfahren zur Auswertung der Herzratenvariabilität" beim Deutschen Patent- und Markenamt angemeldet. Die Offenlegung
erfolgte am 20. März 2008. Die Prüfungsstelle für Klasse A 61 B hat die Anmeldung durch Beschluss vom 20. Januar 2009 zurückgewiesen.


Im Prüfungsverfahren sind folgende Druckschriften genannt:


        D1 WO 00/51677 A2
        D2 Naidu, V.P.S., et. al.: "Autoregressive (AR) based Power
             Spectral Analysis of Heart Rate Time Series Signal (HRTS
             signal)", IEEE, TENCON 2003, S. 1391-1394
        D3 Nutan D. Ahuja, et. al.: "Heart Rate Variability and its Clinical
             Application for Biofeedback", Proceedings of the 17 th IEEE
             Symposium on Computer-Based Medical Systems, IEEE
             2004, S. 1-4.


In der Offenlegungsschrift ist weiter die


        D4 Malik et. al., Task Force of the European Society of Cardiology
             and the North American Society of Pacing and Electrophysiology: "Heart Rate Variability, Standards of Measurement, Physiological Interpretation, and Clinical Use", Circulation, 1996,
             Vol. 93, Nr. 5, S. 1043-1064


angegeben.

                                            -4-



Im Zurückweisungsbeschluss hat die Prüfungsstelle ausgeführt, dass der Gegenstand des Anspruchs 8 nicht auf einer erfinderischen Tätigkeit beruhe und darüber
hinaus ein Diagnostizierverfahren darstelle. Damit lag nach Auffassung der Prüfungsstelle eine nach den §§ 1 bis 5 PatG patentfähige Erfindung nicht vor.


Im Übrigen wurde die beantragte Anhörung als nicht sachdienlich erachtet, da zu
den gerügten Mängeln im Anspruch 8 innerhalb der gesetzten Frist keinerlei Stellungnahme erfolgte und der Antrag auf Anhörung ausdrücklich nur für den Fall gestellt wurde, dass Anspruch 1 Unklarheiten und Mängel aufweist.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin, die ihr Patentbegehren auf der Grundlage der ursprünglichen Patentansprüche 1 bis 8 als
Hauptantrag und hilfsweise mit den Patentansprüchen 1 bis 7 nach Hilfsantrag,
eingereicht mit dem Schriftsatz vom 20. Juni 2011, weiterverfolgt.


Der geltende mit Gliederungspunkten versehene Anspruch 1 nach Hauptantrag
lautet:


 M1       Verfahren zum Auswerten mehrerer Abtastfolgen fh,i (kTs) mit i = 1, 2, 3, ...,
          m und k = 0, 1, 2, ..., n,

 M1a      wobei jede Abtastfolge fh,i (kTs) die Abtastfolge der Herzfrequenz fh eines
          Patienten über den Zeitraum n      s darstellt und


 M1b wobei für jede Abtastfolge fh,i (kTs ) die folgenden Schritte durchgeführt werden:

 M2       Ermittlung einer Verteilungsfunktion Fh,i (f) für jede Abtastfolge fh,i (kTs) als
          Funktion der Frequenz,

 M3       Bestimmung eines ersten Integralanteils lmax,i der Verteilungsfunktion Fh,i (f)
          für einen ersten Frequenzbereich,

                                                      -5-



M3a   wobei der erste Frequenzbereich ein Maximum der Verteilungsfunktion Fh,i
      (f) umfasst,

M4    Bestimmung eines zweiten Integralanteils lref,i der Verteilungsfunktion Fh,i (f)
      für einen zweiten Frequenzbereich,

M4a   der zusätzliche oder andere Frequenzbereiche als den ersten Frequenzbereich umfasst,

M5    Normierung der Integralanteile lmax,i und lref,i mit einem Normierungsfaktor Kref mit


      und


      derart,

M5a   dass für den zweiten Integralanteil die Bedingung                            erfüllt ist,

M6    Bestimmung eines Parameters HRVi für jede Abtastfolge fh,i (kTs) mit den je-

      weiligen Integralanteilen                       und     mit einer Funktion          gemäß

                                        ,

M6a   wobei die Funktion                        für jeden Integralanteil   die Bedingungen




      und
               ~
                 ( )
            ∂f I ref
          0> ~
                                       ~
                                            (
                                     f I ref ,i
                                   >− ~
                                                  )
             ∂I ref    ~              I ref ,i
                       I ref , i


      erfüllt, und

                                          -6-




 M6b wobei die Funktion
                                 ,der erste und zweite Frequenzbereich sowie der
        Normierungsfaktor Kref für alle m ausgewerteten Abtastfolgen fh,i (kTs) gleich
        sind.


Der nebengeordnete Patentanspruch 8 nach Hauptantrag lautet:


        Verwendung des Parameters HRVi gemäß dem Verfahren nach
        einem der Ansprüche 1-7 als Indikator für Abtastfolgen der Herzfrequenz fh eines Patienten, der sich in der Nähe des RSA-Zustands befindet oder den RSA-Zustand erreicht hat.


Der Patentanspruch 1 nach dem Hilfsantrag lautet mit eingefügter Merkmalsgliederung (Unterschiede zu Anspruch 1 gemäß Hauptantrag unterstrichen):


 M1'     Verfahren zur Online-Anzeige eines HRV-Biofeedbacksignals gegenüber
         einem Patienten mit den folgenden Schritten:

 M1''    Bereitstellung mehrerer Abtastfolgen fh,i (kTs) mit i = 1, 2, 3, ..., m und k =
         0, 1, 2, ..., n,

 M1a'    wobei jede Abtastfolge fh,i (kTs) die Abtastfolge der Herzfrequenz fh des Patienten über den Zeitraum n     s darstellt und


 M1b     wobei für jede Abtastfolge fh,i (kTs )die folgenden Schritte durchgeführt werden:

 M2'     Ermittlung einer Verteilungsfunktion Fh,i (f) für jede Abtastfolge fh,i (kTs) als
         Funktion der Frequenz mittels einer Spektralanalyse,

 M3      Bestimmung eines ersten Integralanteils lmax,i der Verteilungsfunktion Fh,i (f)
         für einen ersten Frequenzbereich,

                                                      -7-



M3a   wobei der erste Frequenzbereich ein Maximum der Verteilungsfunktion Fh,i
      (f) umfasst,

M4    Bestimmung eines zweiten Integralanteils lref,i der Verteilungsfunktion Fh,i
      (f) für einen zweiten Frequenzbereich,

M4a   der zusätzliche oder andere Frequenzbereiche als den ersten Frequenzbereich umfasst,

M5    Normierung der Integralanteile lmax,i und lref,i mit einem Normierungsfaktor Kref mit


      und


      derart,

M5a   dass für den zweiten Integralanteil die Bedingung                          erfüllt ist,

M6    Bestimmung eines Parameters HRVi für jede Abtastfolge fh,i (kTs) mit den

      jeweiligen Integralanteilen                      und      mit einer Funktion        gemäß

                                        ,

M6a   wobei die Funktion                        für jeden Integralanteil    die Bedingungen




      und
               ~
                 ( )
            ∂f I ref
          0> ~
                                       ~
                                            (
                                     f I ref ,i
                                   >− ~
                                                  )
             ∂I ref    ~              I ref ,i
                       I ref , i


      erfüllt, und

                                      -8-




 M6b    wobei die Funktion       ,der erste und zweite Frequenzbereich sowie der
        Normierungsfaktor Kref für alle m ausgewerteten Abtastfolgen fh,i (kTs)
        gleich sind.

 M7     Verwendung eines jeden Parameters HRVi für das Biofeedbacksignal zur
        Online-Anzeige gegenüber dem Patienten.


Hinsichtlich des Wortlauts der Unteransprüche 2 bis 7 gemäß Hauptantrag und
der Unteransprüche 2 bis 7 gemäß Hilfsantrag wird auf den Akteninhalt verwiesen.


Die Anmelderin beantragt,


       den Beschluss der Prüfungsstelle für Klasse A 61 B des Deutschen Patent- und Markenamts vom 20. Januar 2009 aufzuheben
       und


       das Patent DE 10 2006 039 957
       mit den ursprünglichen Ansprüchen 1 bis 8 vom Anmeldetag,
       mit der Beschreibung Seiten 1 bis 3, 5 bis 15 und 18 vom Anmeldetag sowie
       mit den am 23. November 2006 eingegangenen Seiten 16 und 17
       und
       mit den am 20. Juni 2011 eingegangenen Seiten 4 und 4a der Beschreibung sowie
       mit den Figuren 6 bis 10, 12 und 13 vom Anmeldetag und
       mit den am 23. November 2006 eingereichten Figuren 1 bis 5 und
       11 (Hauptantrag),
       hilfsweise mit den Ansprüchen 1 bis 7 gemäß dem am
       20. Juni 2011 eingegangenen Hilfsantrag,

                                           -9-



        restliche Unterlagen wie Hauptantrag
        (Hilfsantrag),


        zu erteilen.


Zu weiteren Einzelheiten wird auf den Akteninhalt verwiesen.


                                             II


Die Beschwerde ist zulässig, insbesondere ist sie statthaft sowie form- und fristgerecht eingelegt (§ 73 Abs. 1, Abs. 2 PatG).


Die Beschwerde hat insoweit Erfolg, als sie zur Aufhebung des Beschlusses der
Prüfungsstelle, zur Erteilung auf der Grundlage der Patentansprüche 1 bis 7 nach
Hilfsantrag 1 und zur Rückzahlung der Beschwerdegebühr führt.


1.
Die Erfindung betrifft ein Verfahren zum Auswerten mehrerer Abtastfolgen fh,i(kTs)
mit i = 1, 2, 3, ..., m und k = 0, 1,2, ..., n, wobei jede Abtastfolge fh,i(kTs) die Abtastfolge der Herzfrequenz fh eines Patienten über den Zeitraum n            s darstellt (siehe

Offenlegungsschrift Abs. [0001]). Auf der Grundlage dieser Abtastfolge der Herzfrequenz fh (kTs) mit k = 0, 1, 2, ... wird die Herzratenvariabilität (HRV) (= Veränderung der Frequenz des Herzschlags) ermittelt.


Wie aus der Beschreibungseinleitung weiter hervorgeht, ist die Herzratenvariabilität (HRV) in Ruhe- bzw. Entspannungszuständen beispielsweise dadurch charakterisiert, dass die Herzfrequenz in einem sehr regelmäßigen Rhythmus zunimmt
und wieder abnimmt. Dieser Zustand wird Respiratorische Sinus-Arrhythmie (RSA) genannt (als Sinus-Arrhythmie bezeichnet man im Allgemeinen die unregelmäßige Schlagfolge des Herzens infolge unregelmäßiger Reizbildung im Sinusknoten) (siehe Offenlegungsschrift Abs. [0005]).

                                         - 10 -



Grundsätzlich sind aus dem Stand der Technik verschiedene Parameter der HRV
bekannt, die jeweils als Indikator für den RSA-Zustand verwendbar sein sollen
(siehe Offenlegungsschrift Abs. [0009]). Nach der Beschreibungseinleitung wurde
bislang noch kein Parameter gefunden, der es dem Patienten zuverlässig erlaubt,
durch Veränderung seiner Atemfrequenz über HRV-Biofeedback den RSA-Zustand zu erreichen (siehe Offenlegungsschrift Abs. [0012]).


Aufgabe der Erfindung ist es daher, einen Parameter der HRV bereitzustellen, der
es einem Patienten mittels HRV-Biofeedback erlaubt, den eigenen RSA-Zustand
zuverlässig zu stabilisieren (siehe Offenlegungsschrift Abs. [0013]).


2.
Hauptantrag


2.1.
Die Verfahren gemäß den Patentansprüchen 1 und 8 sind entgegen den anfangs
von der Prüfungsstelle geltend gemachten Vorbehalten ausführbar und enthalten
auch keine Widersprüche.


Eine Erfindung ist dann ausführbar offenbart, wenn die in der Patentanmeldung
enthaltenen Angaben dem fachmännischen Leser so viel an technischer Information vermitteln, dass er mit seinem Fachwissen und seinem Fachkönnen in der Lage ist, die Erfindung erfolgreich auszuführen (vgl. BGH GRUR 2010, 916 ff.
- Klammernahtgerät).


Insbesondere bereitet es dem hier zuständigen Fachmann, einem Dipl.-Physiker
mit langjähriger Erfahrung in der Entwicklung von Verfahren zur Bestimmung und
Auswertung der Herzratenvariabilität, der in medizinischen Fragestellungen einen
Arzt zu Rate zieht, keinerlei Schwierigkeiten, die Begriffe "Abtastfolge", "Integralteil" und "Herzratenvariabilität" fachlich richtig einzuordnen.

                                      - 11 -



Dies folgt auch unmittelbar aus den Ausführungen der Prüfungsstelle im Erstbescheid vom 30. März 2007, in dem der Prüfer letztlich doch in der Lage war, die
zunächst als unklar bezeichneten Ausdrücke sinnvoll auszulegen. Dies gilt zumindest für die bezüglich des Anspruchs 1 vorgebrachten Mängel, die der Prüfer in
Kenntnis des Schriftsatzes vom 10. Juli 2010 in seinem Zurückweisungsbeschluss
nicht mehr beanstandet hat. Dies ergibt sich auch aus der Tatsache, dass der Prüfer die Anhörung u. a. mit der Begründung abgelehnt hat, dass die Anhörung nur
für den Fall beantragt worden sei, dass die gerügten Unklarheiten im Anspruch 1
noch erörterungsbedürftig seien.


Das gilt sinngemäß auch für den nebengeordneten Anspruch 8, dessen Gegenstand der Prüfer im Zurückweisungsbeschluss als nahe liegend bezeichnet hat.
Ein "unklarer" Gegenstand kann dem Fachmann aber nicht nahegelegt werden.


2.2.
Bei der gemäß Anspruch 8 beanspruchten Verwendung des Verfahrens handelt
es sich um ein Diagnostizierverfahren am menschlichen Körper, das von der Patentierung ausgeschlossen ist.


§ 2a Abs. 1 Nr. 2 Satz 1 PatG schließt Diagnostizierverfahren, die am menschlichen oder tierischen Körper vorgenommen werden, von der Patentierung aus. Unter Hinweis auf die Entscheidung 21 W (pat) 45/05 bzw. 4 Ni 47/09 (EU) fällt unter
das Patentierungsverbot ein Verfahren zur gesundheitlichen Orientierung, das folgende Schritte umfasst:


       i.    Untersuchung mit Datenerhebung,
       ii.   Vergleich dieser Daten mit Normwerten,
       iii. Feststellung einer Abweichung bei diesem Vergleich,
       iv. Deutung der Abweichung als krankhafter Zustand.

                                            - 12 -



Ein krankhafter Zustand gemäß Schritt iv) ist bereits gegeben, wenn die erhobenen Daten einen nicht normalen Zustand im Sinne von "nicht gesund" gegenüber
den Normwerten darstellen (vgl. auch BPatG Beschluss vom 5. Juli 2001,
21 W (pat) 72/99: "Abweichen der Istwerte vom Normwert").


Im Verfahren nach Patentanspruch 8 werden folgenden Verfahrensschritte durchgeführt:


           i.    Messung der Herzfrequenz, Darstellung als Abtastfolge und
                 die weiteren in Anspruch 1 beschriebenen Schritte, um einen
                 HRV-Parameter zu ermitteln
           ii.   Vergleich mit einem Normwert des HRV-Parameters, der dem
                 RSA-Zustand entspricht.
                 Mit Hilfe des Indikators wird angezeigt (lateinisch indicare =
                 anzeigen), ob der RSA-Zustand erreicht ist. Hierfür ist erforderlich, den Parameter HRV mit Normwerten für den RSA-Zustand zu vergleichen.
           iii. Feststellung der Abweichung des HRV-Parameters vom
                 Normwert des RSA-Zustands.
                 Diese Bewertung ist ebenfalls für den Indikator notwendig.
           iv. Deutung, ob sich der Patient in der Nähe des RSA-Zustands
                 befindet oder den RSA-Zustand erreicht hat.
                 Befindet sich der Patient nicht im RSA-Zustand, so kann dieser Zustand als ein nicht normaler Zustand im Sinne von
                 "nicht gesund" gegenüber den Normwerten angesehen werden. Da dies mit dem Verfahren nach Anspruch 8 angezeigt
                 wird, ist auch der Schritt iv) als gegeben anzusehen.


Damit werden alle für ein Diagnostizierverfahren notwendigen Schritte i) bis iv) mit
dem Verfahren nach Anspruch 8 durchgeführt.

                                      - 13 -



Zu der - wie dargelegt einschlägigen - Entscheidung 21 W (pat) 45/05 des erkennenden Senats hat sich die Anmelderin nicht weiter geäußert, sondern lediglich
auf die insoweit nicht anwendbaren Aussagen der Entscheidung G1/04 der Großen Beschwerdekammer des EPA und die Uraltentscheidung T385/86 einer Technischen Beschwerdekammer des EPA vom 25. September 1987 hingewiesen.


3.
Hilfsantrag


3.1
Der Patentanspruch 1 und die Unteransprüche 2 bis 7 sind zulässig.


Die Online-Anzeige des HRV-Biofeedbacksignals nach den Merkmalen M1' und
M7 ist ursprünglich offenbart. Aus den Absätzen [0013], [0007], [0008] und dem
ursprünglichen Anspruch 8 lässt sich mitlesen, dass das Verfahren als Indikator
für den RSA-Zustand verwendet werden soll (siehe Anspruch 8) und dass der
HRV-Parameter als Biofeedbacksignal dem Patienten bereitgestellt werden soll
(siehe Offenlegungsschrift Abs. [0013]). Zusammen mit der Definition in
Abs. [0012], wonach beim HRV-Biofeedback "ein HRV-Parameter online ermittelt
und durch Aufbereitung dem Patienten in geeigneter Weise angezeigt" wird, ergibt
sich die Online-Anzeige des erfindungsgemäßen HRV-Biofeedbacksignals.


Das Merkmal M1'' wurde aus dem Merkmal M1 des ursprünglichen Anspruchs 1
umformuliert und ist ohne inhaltliche Änderung.
Das Streichen des Merkmals M1b bewirkt keine inhaltliche Änderung, da die Berechnung für jede Abtastfolge auch in Merkmal M2 enthalten ist.
Die Verwendung der Spektralanalyse gemäß Merkmal M2' liest der Fachmann aus
den Absätzen [0005], [0032] und [0033]) mit.


Die übrigen Merkmale in Anspruch 1 sind auch im ursprünglichen Anspruch 1 vorhanden.

                                          - 14 -



Die Unteransprüche 2 bis 7 entsprechen den ursprünglich eingereichten Ansprüchen 2 bis 7.


3.2
Das Verfahren nach Patentanspruch 1 stellt kein Diagnostizierverfahren dar, da
kein Vergleich mit Normwerten, keine Auswertung des Vergleichs und keine Deutung als krankhafter Zustand erfolgt.
Bei der Verwendung als Biofeedbacksignal werden lediglich Zustandsgrößen biologischer Vorgänge angezeigt.


3.3
Das Verfahren nach dem Patentanspruch 1 ist neu.


Aus der Druckschrift D1 ist ein Verfahren zur Anzeige eines HRV-Biofeedbacksignals gegenüber einem Patienten mit der Bereitstellung mehrerer Abtastfolgen fh,i (kTs) mit i = 1, 2, 3, ..., m und k = 0, 1, 2, ..., n, wobei jede Abtastfolge fh,i
(kTs) die Abtastfolge der Herzfrequenz fh eines Patienten über den Zeitraum nTs
darstellt, bekannt (vgl. D1 Anspruch 1 "A method, characterized by: sampling a
heart beat of a subject, S. 14 Z. 16-23: "The spectral analysis of this signal is obtained from the successive discrete series of R-R duration values taken from the
ECG signal sampled at 256 Hz and FFTed. ", Fig. 7B (48)) [=Merkmal M1a]. Eine
Online-Anzeige eines HRV-Biofeedbacksignals gemäß Merkmal M1’ ist nicht bekannt.
Für jede Abtastfolge wird mittels einer Spektralanalyse eine Verteilungsfunktion
HRV als Funktion der Frequenz ermittelt (vgl. D1 S. 14 Z. 24-29 "HRV data is analyzed for 5 minutes before and for 5 minutes during the practice of FF. The time
domain traces are analyzed by obtaining the overall mean heart rate for both 5-minute periods and calculating the Standard deviation around that mean.", Anspruch 11 "expressing the HRV as a function of frequency") [=Merkmal M2’].

                                         - 15 -



Hierzu wird ein erster Integralanteil lmax,i (VLF, LF) der Verteilungsfunktion HRV(f)
für einen ersten Frequenzbereich bestimmt (vgl. D1 S. 14 Z. 27 – S. 15 Z. 3:
"FFTs of the time domain data are analyzed by dividing the power spectra into
three frequency regions: VLF (0.01 to 0.05 Hz), LF (0.05 to 0.15 Hz) and HF (0.15
to 0.5 Hz). The integral of the total power in each of these regions, ... are calculated for each individual in the baseline and FF periods." [=Merkmale M3, M3a]. Dabei liest der Fachmann aus der Angabe LF mit, dass der Frequenzbereich ein Maximum der Verteilungsfunktion Fh,i (f) umfasst (vgl. D4 Fig. 3).


Auch wird ein zweiter Integralanteil lref,i (HF) der Verteilungsfunktion Fh,i (f) für einen zweiten Frequenzbereich bestimmt, der zusätzliche oder andere Frequenzbereiche als den ersten Frequenzbereich umfasst (vgl. D1 S. 14 Z. 27 – S. 15 Z. 3)
[=Merkmale M4, M4a].
Auch die Normierung der Integralanteile ist in der Druckschrift D1 offenbart (vgl.
D1 Fig. 7B (62) "Normalize the power spektrum"). Hierfür einen Normierungsfaktor
zu verwenden, liest der Fachmann mit. Damit ist auch das Merkmal M5 als bekannt anzusehen. Die Bedingung nach Merkmal M5a ist der Druckschrift D1 jedoch nicht zu entnehmen.


Aus den ersten und zweiten Integralanteilen (VLF, LF und HF) werden in der
Druckschrift D1 weitere Parameter (VLF/HF ratio, LF/(VLF+HF) ratio) bestimmt
(vgl. D1 S. 14 Z. 30 - S. 15 Z. 2 "The integral of the total power in each of these regions, the total power over all regions (VLF+LF+HF), the VLF/HF ratio and the
LF/(VLF+HF) ratio are calculated for each individual in the baseline and FF periods"). Bei den Parametern VLF/HF und LF/(VLF+HF) kann eine Funktion f(HF)
gemäß Merkmal M6, nach dem HRVi = LF * f(HF) berechnet wird, angegeben werden:
f(HF) = 1/(HF) bzw. f(HF) = 1/(VLF+HF).


Für keine dieser Funktionen gilt jedoch die erste Bedingung gemäß Merkmal M6a.

                                        - 16 -



Auch die Merkmale M6b und M7 können aus der Druckschrift D1 nicht mitgelesen
werden, da weder der Normierungsfaktor in der D1 näher definiert ist, noch der
Parameter HRV als Biofeedbacksignal online angezeigt wird.


Analog zur Druckschrift D1 zeigt auch die Druckschrift D4 lediglich die Bestimmung des Leistungsverhältnisses LF/HF. Eine Korrelationsfunktion nach dem
Merkmal M6a wird auch in der D4 nicht gezeigt.


Im Absatz "spectral components" auf S. 358 wird ein Verfahren zur Berechnung
von HRV-Parametern zeigt: So werden mehrere Abtastfolgen ("short-term recordings") der Herzfrequenz eines Patienten ausgewertet und die nachfolgende
Spektralanalyse durchgeführt (vgl. D4 S. 358 li. Spalte Abs. 3) [=Merkmale M1’’,
M1a, M1b].


Für jede Abtastfolge wird mittels Spektralanalyse eine Verteilungsfunktion als
Funktion der Frequenz ermittelt (vgl. D4 S. 358 li. Spalte Abs. 3: "Three main
spectral components are distinguished in a spectrum calculated from short-term
recordings of 2 to 5 min") [=Merkmal M2].
Für die Verteilungsfunktion ("spectrum") werden ein erster Integralanteil ("LF power component") bestimmt, der ein Maximum der Verteilungsfunktion Fh,i (f) umfasst (vgl. D4 S. 358 li. Spalte Abs. 3 "The distribution of the power and the central
frequency of LF and HF ..." , re. Spalte Abs. 2: "Measurement of VLF, LF and HF
power components is ...", Fig. 3, Fig. 4 "Only the LF and HF components correspond to peaks of the spectrum while the VLF and ULF can be approximated by a
line in this plot with logarithmic scales on both axes.") [=Merkmale M3, M3a].


Weiter wird ein zweiter Integralanteil ("HF power component") bestimmt, der zusätzliche oder andere Frequenzbereiche als den ersten Frequenzbereich umfasst
(vgl. D4 S. 358 li. Spalte Abs. 3, re. Spalte Abs. 2, Fig. 3) [=Merkmale M4, M4a].

                                     - 17 -



Auch eine Normierung der Integralanteile HF und LF ist in der Druckschrift D4 offenbart (vgl. D4 S. 358 re. Spalte Abs. 2 "LF and HF may also be measured in normalized units"). Der Fachmann liest dabei mit, dass die Normierung mittels eines
Normierungsfaktors durchgeführt wird [=Merkmal M5].


Als Parameter wird in der D4 wiederum der Quotient LF/HF berechnet (vgl. D4
Fig. 3, 5) [=Merkmal M6]. Dieser Parameter erfüllt nicht die Bedingung des Merkmals M6a.


In der Druckschrift D2 erfolgt ebenfalls eine Auswertung der LF- und HF-Frequenzen, wobei auch wiederum der Integralanteil (power = Spektralleistung) der
LF- und HF-Frequenzen bzw. die Peakleistung berechnet wird. Als Parameter
werden die Quotienten
PRLH (power ratio) = PLF (power concentrated in LF region) / PHF (power concentrated in HF region), als auch
PPRLH (peak power ratio) = PPLF (peak power concentrated in LF region) / PPHF
(peak power concentrated in HF region)
ermittelt (vgl. D2 Table 1).
Der Parameter PRLH entspricht den in den Druckschriften D1 und D4 ermittelten
Parameter LF/HF und erfüllt damit nicht das Merkmal M6a.
Dies gilt analog auch für den Parameter PPRLH, da dieser lediglich den Frequenzbereich für die Berechnung des Integrals verändert (peak), jedoch nicht den
grundsätzlichen Zusammenhang Parameter = Imax/Irel. Damit gilt auch für den Parameter PPRLH, dass er die Bedingung aus Merkmal M6a nicht erfüllt.
In der Druckschrift D3 wird die als bekannt vorausgesetzte Berechnung des
LF/HF-Quotienten aus dem EKG des Patienten als Index für das autonome
Gleichgewicht verwendet (vgl. D3 S. 3 Abs. 2). Weitere Parameter werden nicht
genannt.


In keiner der Verfahren nach dem Stand der Technik wird ein Parameter HRVi bestimmt, der die Bedingungen nach Merkmal M6a erfüllt.

                                      - 18 -



3.4
Das Verfahren nach dem Patentanspruch 1 beruht auch auf einer erfinderischen
Tätigkeit.


Das Merkmal M6a wird für den Fachmann durch den Stand der Technik auch nicht
nahe gelegt, auch nicht in Verbindung mit seinem allgemeinen Fachwissen.


Zwar ist es – wie auch die Druckschriften D1 bis D4 zeigen – grundsätzlich bekannt, verschiedene Parameter HRV aus den Integralanteilen nach den Merkmalen M3/M3a und M4/M4a zu ermitteln. Dabei wird der Fachmann zur Korrelation
der beiden Integralanteile die üblichen statischen Methoden oder eine einfache
Korrelation mittels Differenz oder Quotientenbildung verwenden. Dies ist auch in
den Druckschriften D1 bis D4 offenbart.


Für die Korrelation der Integralanteile mit der in Merkmal M6a genannten Bedingung fehlt dem Fachmann jeglicher Hinweis. Wie zur Neuheit ausgeführt zeigen
weder die Druckschrift D1 noch die Druckschriften D2 bis D4 eine derartige Funktion.


Mit der Bedingung im Merkmal M6a ergibt sich darüber hinaus die vorteilhafte Lösung, dass für den Parameter HRV der zweite Integralanteil stärker gewichtet ist.
Die Korrelation lag nach Ansicht des Senats auch nicht im Bereich fachüblichen
Handelns.


Das Verfahren des Anspruchs 1 gemäß Hilfsantrag ergibt sich für den Fachmann
daher nicht in nahe liegender Weise aus dem Stand der Technik.


Die Patentfähigkeit des Gegenstands nach dem Anspruch 1 hatte im Übrigen
schon die Prüfungsstelle im Erstbescheid vom 30. März 2007 im letzten Absatz
von Abschnitt III anerkannt.

                                        - 19 -



3.5
Die Unteransprüche 2 bis 7 nach Hilfsantrag betreffen vorteilhafte Ausgestaltungen des Anspruchs 1, und die übrigen Unterlagen erfüllen insgesamt die an sie zu
stellenden Anforderungen.


4.
Die Beschwerdegebühr ist zurückzuzahlen. Die Billigkeit der antragsgemäßen Zurückzahlung der Beschwerdegebühr ergibt sich vorliegend daraus, dass die Prüfungsstelle die beantragte Anhörung abgelehnt hat, ohne dass die von ihr dafür
genannten oder auch andere Gründe dies rechtfertigen könnten.


Eine einmalige Anhörung ist grundsätzlich in jedem Verfahren sachdienlich, selbst
wenn keine geänderten Patentansprüche vorgelegt werden (Schulte, PatG,
8. Aufl.,   § 46   Rdnr. 8   sowie   aktuell     BPatG,   Beschl.   v.   28. April 2009
- 21 W (pat) 41/05 m. w. Nachw.).


In der Erwiderung ging die Anmelderin ausführlich auf die Mängel im Hauptanspruch 1 ein, um zu einem gewährbaren Anspruch 1 zu gelangen. Die Überarbeitung der Beschreibung wurde zurückgestellt, bis ein gewährbarer Hauptanspruch
vorliegt (Eingabe vom 10. Juli 2007). Es war damit davon auszugehen, dass die
Anmelderin den nebengeordneten Anspruch 8 ebenfalls noch angepasst hätte.
Dies hätte auch im Rahmen der beantragten Anhörung geschehen können.

                                       - 20 -



Damit wäre bei angemessener Sachbehandlung der Erlass eines Zurückweisungsbeschlusses nicht in Betracht gekommen und eine Beschwerde hätte vermieden werden können.




Dr. Winterfeldt         Dr. Kortbein            Dr. Müller       Zimmerer




                                                                       Pü
