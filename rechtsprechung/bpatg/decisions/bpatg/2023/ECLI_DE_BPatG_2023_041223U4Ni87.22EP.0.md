---
ecli: "ECLI:DE:BPatG:2023:041223U4Ni87.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 87/22"
decided: "2023-12-04"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=33&nr=43972&anz=529&pos=506&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-12-04_4_Ni_87_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 87/22 vom 2023-12-04

## Entscheidung

BUNDESPATENTGERICHT
                      IM NAMEN DES VOLKES

                                 URTEIL

                                                          Verkündet am
                                                       4. Dezember 2023
4 Ni 87/22 (EP)                                                …

(Aktenzeichen)



                      In der Patentnichtigkeitssache
…




ECLI:DE:BPatG:2023:041223U4Ni87.22EP.0

                  betreffend das europäische Patent 2 676 271
                               (DE 60 2012 071 475)



hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts am 4. Dezember 2023 durch den Vorsitzenden Richter Voit, den Richter Dipl.-Ing. Müller, die
Richterin Werner M. A. und die Richter Dipl.-Ing. Matter und Dipl.-Ing. Tischler


für Recht erkannt:

  I.     Die Klage wird abgewiesen.


  II.    Die Kosten des Rechtsstreits hat die Klägerin zu tragen.


  III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des
         zu vollstreckenden Betrages vorläufig vollstreckbar.




                                 Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet
der Bundesrepublik Deutschland in englischer Sprache erteilten Europäischen Patents 2 676 271 (Streitpatent), das unter Inanspruchnahme der US-Priorität
US 201161442960 P vom 15. Februar 2011 am 14. Februar 2012 angemeldet worden ist. Die Anmeldung ist am 23. August 2012 als WO 2012/109734 A1 (MFG3)
veröffentlicht worden und die Erteilung des Streitpatents am 29. Juli 2020.

Das Streitpatent ist in Kraft und wird beim Deutschen Patent- und Markenamt unter
dem Aktenzeichen 60 2012 071 475.1 geführt. Es trägt in der Verfahrenssprache
die Bezeichnung




                                                                                   2/61

 „DEVICE AND METHOD FOR QUANTIZING THE GAINS OF THE ADAPTIVE
   AND FIXED CONTRIBUTIONS OF THE EXCITATION IN A CELP CODEC“

                          und in der deutschen Übersetzung

    „Vorrichtung und Verfahren zur Quantisierung der Verstärkung von adaptiven und festen Beiträgen der Anregung in einem Celp-Koder-Dekoder“.


Es umfasst in der erteilten Fassung 21 Patentansprüche, die die Klägerin mit ihrer
Nichtigkeitsklage vom 28. Oktober 2022 in vollem Umfang angreift.


Der die Vorrichtung der Codiererseite betreffende Patentanspruch 1 lautet gemäß
Streitpatentschrift:

 1. A device for quantizing a gain of a fixed contribution of an excitation in a
     frame, including sub-frames, of a coded sound signal, comprising:

        an input for a parameter representative of a classiﬁcation of the frame;
        an estimator of the gain of the ﬁxed contribution of the excitation in a
        sub-frame of said frame, using the parameter representative of the
        classification of the frame; and
        a predictive quantizer of the gain of the fixed contribution of the excitation, in the sub-frame, using the estimated gain;
        wherein the predictive quantizer determines a correction factor for the
        estimated gain as a quantization of the gain of the ﬁxed contribution of
        the excitation;
        wherein the estimated gain multiplied by the correction factor gives the
        quantized gain of the ﬁxed contribution of the excitation; and
        wherein the estimator comprises, for a ﬁrst sub-frame of the frame:

           (a) a first calculator of a linear estimation of the gain of the ﬁxed
           contribution of the excitation in logarithmic domain in response to
           the parameter representative of the classification of the frame;




                                                                                    3/61

               (b) a subtractor of an energy of a filtered innovation codevector from
               a ﬁxed codebook in logarithmic domain from the linear gain estimation from the first calculator, the subtractor producing a gain in logarithmic domain;
               (c) a converter of the gain in Iogarithmic domain from the subtractor
               to linear domain to produce the estimated gain; and
               (d) a multiplier of the estimated gain by the correction factor to produce the quantized gain of the ﬁxed contribution of the excitation;
               and

         wherein the estimator, for each sub-frame of said frame following the
         ﬁrst sub-frame, is responsive to the parameter representative of the
         classification of the frame and gains of adaptive and ﬁxed contributions
         of the excitation of at least one previous sub-frame of the frame to
         estimate the gain of the fixed contribution of the excitation.


Der nebengeordnete, auf einen der Ansprüche 1 bis 3 rückbezogene Patentanspruch 4, eine Vorrichtung zum gemeinsamen Quantisieren von Verstärkungen von
adaptiven und festen Beiträgen einer Anregung betreffend, lautet gemäß Streitpatentschrift:

 4. A device for jointly quantizing gains of adaptive and ﬁxed contributions of
      an excitation in a frame of a coded sound signal, comprising:

         a quantizer of the gain of the adaptive contribution of the excitation;
         and
         the device for quantizing the gain of the ﬁxed contribution of the excitation as deﬁned in any one of claims 1 to 3.


Der nebengeordnete, eine Vorrichtung der Decodiererseite betreffende Patentanspruch 9 lautet gemäß Streitpatentschrift:

 9. A device for retrieving a quantized gain of a ﬁxed contribution of an excitation in a sub-frame of a frame, comprising:

         a receiver of a gain codebook index;




                                                                                         4/61

       an estimator of the gain of the fixed contribution of the excitation in the
       sub-frame, using a parameter representative of a classification of the
       frame;
       a gain codebook for supplying a correction factor in response to the
       gain codebook index; and
       a multiplier of the estimated gain by the correction factor to provide a
       quantized gain of the ﬁxed contribution of the excitation in said subframe;
       wherein the estimator comprises, for a ﬁrst sub-frame of the frame:

          (a) a calculator of a linear estimation of the gain of the ﬁxed contribution of the excitation in logarithmic domain in response to the parameter representative of the classification of the frame;
          (b) a subtractor of an energy of a filtered innovation codevector from
          a ﬁxed codebook in logarithmic domain from the linear gain estimation from the calculator, the subtractor producing a gain in logarithmic domain; and
          (c) a converter of the gain in logarithmic domain from the subtractor
          to linear domain to produce the estimated gain; and

       wherein the estimator, for each sub-frame of said frame following the
       ﬁrst sub-frame, is responsive to the parameter representative of the
       classification of the frame and gains of adaptive and ﬁxed contributions
       of the excitation of at least one previous sub-frame of the frame to
       estimate the gain of the fixed contribution of the excitation.


Der nebengeordnete, decodiererseitige, eine Vorrichtung zum Abrufen bzw. Wiedergewinnen von quantisierten Verstärkungen von adaptiven und festen Beiträgen
einer Anregung betreffende Patentanspruch 10 lautet gemäß Streitpatentschrift:

 10. A device for retrieving quantized gains of adaptive and fixed contributions
     of an excitation in a sub-frame of a frame, comprising:

       a receiver of a gain codebook index;




                                                                                     5/61

       an estimator of the gain of the ﬁxed contribution of the excitation in the
       sub-frame, using a parameter representative of a classification of the
       frame;
       a gain codebook for supplying the quantized gain of the adaptive contribution of the excitation and a correction factor for the sub-frame in
       response to the gain codebook index; and
       a multiplier of the estimated gain by the correction factor to provide a
       quantized gain of the ﬁxed contribution of the excitation in the subframe;
       wherein the estimator comprises, for a ﬁrst sub-frame of the frame:

          (a) a calculator of a linear estimation of the gain of the ﬁxed contribution of the excitation in logarithmic domain in response to the parameter representative of the classification of the frame;
          (b) a subtractor of an energy of a filtered innovation codevector from
          a ﬁxed codebook in Iogarithmic domain from the linear gain estimation from the calculator, the subtractor producing a gain in logarithmic domain; and
          (c) a converter of the gain in logarithmic domain from the subtractor
          to linear domain to produce the estimated gain; and

       wherein the estimator, for each sub-frame of said frame following the
       ﬁrst sub-frame, is responsive to the parameter representative of the
       classification of the frame and gains of adaptive and ﬁxed contributions
       of the excitation of at least one previous sub-frame of the frame to
       estimate the gain of the fixed contribution of the excitation.


Die nebengeordneten Verfahrensansprüche 12, 15, 18 und 20 entsprechen inhaltlich den Vorrichtungsansprüchen 1, 4, 9 und 10. Die Patentansprüche 2 und 3 sind
unmittelbar bzw. mittelbar auf Patentanspruch 1, Patentansprüche 5 bis 8 unmittelbar bzw. mittelbar auf Patentanspruch 4, Patentanspruch 11 auf Patentanspruch
10, Patentansprüche 13 und 14 unmittelbar bzw. mittelbar auf Patentanspruch 12,
Patentansprüche 16 und 17 unmittelbar bzw. mittelbar auf Patentanspruch 15, Patentanspruch 19 auf Patentanspruch 18 und Patentanspruch 21 auf Patentanspruch



                                                                                    6/61

20 rückbezogen. Wegen des Wortlauts dieser Patentansprüche wird auf die Akte
Bezug genommen.


Die Klägerin ist der Ansicht, das Streitpatent sei wegen der Nichtigkeitsgründe der
unzulässigen Erweiterung, mangelnden Ausführbarkeit und mangelnden Patentfähigkeit für nichtig zu erklären. Die Gegenstände der unabhängigen Patentansprüche seien gegenüber der Offenbarung der internationalen Anmeldung, veröffentlicht
am 23. August 2012, unzulässig erweitert und in der Streitpatentschrift nicht so deutlich und vollständig offenbart, dass ein Fachmann sie ausführen könne. Die Gegenstände der unabhängigen Patentansprüche nach Streitpatent seien gegenüber dem
Stand der Technik nicht neu und beruhten jedenfalls nicht auf einer erfinderischen
Tätigkeit.

Den Einwand der fehlenden Patentfähigkeit stützt die Klägerin auf folgende Dokumente (Nummerierung und Kurzzeichen nach Klägerin):

     JELINIK/MFG5          US 7,778,827 B2
     TADDEI/MFG6           TADDEI, H. et al.: Efficient Coding of Transitional
                           Speech Segments in CELP. Speech Coding, 2002, IEEE
                           Workshop Proceedings. Date of Conference: 09 October
                           2002. DOI 10.1109/SCW.2002.1215708. ISBN-0-7803-
                           7549-1. Seiten 14 bis 16
     GAO/MFG7              US 7,191,122 B1


Die Klägerin beantragt,

       das europäische Patent 2 676 271 mit Wirkung für das Hoheitsgebiet
       der Bundesrepublik Deutschland in vollem Umfang für nichtig zu
       erklären.


Die Beklagte beantragt,

       die Klage abzuweisen.

hilfsweise, die Klage abzuweisen,




                                                                                  7/61

      soweit sie sich auch gegen eine der Fassungen des Streitpatents
      nach den Hilfsanträgen 1 oder 2, überreicht mit Schriftsatz vom
      15. Juni 2023, richtet,

          mit der Maßgabe, dass die Hilfsanträge in der numerischen
          Reihenfolge und alle Anträge als geschlossene Anspruchssätze
          gestellt werden.


Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den Gegenstand des Streitpatents in der erteilten Fassung für schutzfähig.

Wegen des Wortlauts der Ansprüche nach den Hilfsanträgen wird auf die Akte verwiesen.

Die Klägerin wendet sich auch gegen die Hilfsanträge. Sie sieht auch die Gegenstände nach den Patentansprüchen in der Fassung der jeweiligen Hilfsanträge als
unzulässig erweitert, nicht ausführbar und nicht patentfähig.

Der Senat hat den Parteien einen qualifizierten Hinweis vom 27. März 2023 zugeleitet und hierin Fristen zur Stellungnahme auf den Hinweis und auf etwaiges Vorbringen der jeweiligen Gegenpartei gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, auf das Protokoll der mündlichen Verhandlung vom 4. Dezember 2023 sowie den weiteren Akteninhalt Bezug
genommen.




                                                                             8/61

                           Entscheidungsgründe


                                         A.


Die zulässige Klage ist nicht begründet und war daher abzuweisen. Der Gegenstand
des Streitpatents erweist sich als schutzfähig; die geltend gemachten Nichtigkeitsgründe der unzulässigen Erweiterung, mangelnden Ausführbarkeit und fehlenden
Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1, 2 und 3 IntPatÜG, Art. 138 Abs. 1
Buchst. a), b) und c) EPÜ i. V. m. Art. 52, 54, und 56 EPÜ liegen nicht vor.


Auf die Hilfsanträge kam es daher nicht an.



     I. Zum Gegenstand des Streitpatents, zur Aufgabe, zum Fachmann und
                                 zur Auslegung


1.     Das Streitpatent betrifft die Quantisierung der Verstärkung eines festen Beitrags einer Anregung in einem codierten Tonsignal und die gemeinsame Quantisierung der Verstärkungen der adaptiven und festen Beiträge der Anregung in einem
CELP-Codec (Code-Excited Linear Prediction).

Laut Streitpatentschrift wird in einem CELP- oder ACELP-Codec (Algebraic Code-Excited Linear Prediction) ein Sprach- oder Audio-Eingangssignal in als Rahmen
bezeichneten kurzen Abschnitten verarbeitet. Um sich schnell ändernde Eigenschaften eines Eingangstonsignals zu erfassen, wird jeder Rahmen weiter in Unterrahmen unterteilt. Eine CELP-Codec-Struktur erzeugt auch Beiträge eines adaptiven und eines festen Codebuchs einer Anregung, die addiert werden, um eine Gesamtanregung zu bilden. Zu den Beiträgen des adaptiven und festen Codebuchs
der Anregung gehörige Verstärkungen werden quantisiert und zusammen mit anderen Codierparametern an einen Decodierer übertragen (Streitpatentschrift, Abs.
0001, 0002).




                                                                                9/61

Bei einem bekannten CELP-Codierer werden die optimalen nicht-quantisierten Verstärkungen gp,opt, gc,opt der adaptiven bzw. festen Anregung aus einem Fehlersignal
(ei) wie folgt bestimmt (Abs. 0017 – 0020; Figur 1).




                                      Streitpatentschrift, Fig. 1

Nach Figur 1 gilt für das Fehlersignal ei bzw. e(i) des i-ten Abtastwertes, wobei i von
0 bis L – 1 läuft und L die Anzahl der Abtastwerte pro Unterrahmen ist:

               ( )= ( )−              ( )−         ( ),              = 0, … , − 1   (1)

Gleichung (1) lautet in Vektorschreibweise:

               =    −        −                                                      (2)

Für die Energie des Fehlersignals (= Fehlervektors) e gilt:

                                               =                ()


Durch Minimierung der Fehlerenergie ergeben sich die folgenden Berechnungsvorschriften für die optimalen nicht-quantisierten Verstärkungsfaktoren:
                             −                                         −
                ,   =                               ,       =                       (3)
                              −                                         −

wobei sich die Konstanten bzw. Korrelationen c0, …, c5 wie folgt berechnen:

               =     ,   =        ,      =     ,        =        ,     =    ,   =    (4)




                                                                                           10/61

Die optimalen, nicht-quantisierten Verstärkungen werden gemeinsam quantisiert,
nachdem eine Prädiktion auf die Verstärkung des festen Beitrags der Anregung angewendet wurde. Die Vorhersage wird durchgeführt, indem ein geschätzter Wert
der Verstärkung gc0 des festen Beitrags der Anregung berechnet wird. Die Verstärkung des festen Beitrags der Anregung ergibt sich aus gc = gcog, wobei g ein Korrekturfaktor ist.

Daher enthält jeder Codebucheintrag (eines Verstärkungscodebuchs) zwei Werte.
Der erste Wert entspricht der quantisierten Verstärkung gp des adaptiven Beitrags
der Anregung, der zweite Wert dem Korrekturfaktor g, der zur Multiplikation der geschätzten Verstärkung gc0 des festen Beitrags der Anregung verwendet wird. Der
optimale Index im Verstärkungscodebuch (gp und g) wird durch Minimierung des
mittleren quadratischen Fehlers zwischen dem Zielsignal und dem gefilterten Gesamtanregungssignal gefunden (Abs. 0021).

In diesem Zusammenhang verweist das Streitpatent auf das 3GPP (3rd Generation
Partnership Project) Dokument TS 126.190 (Adpative Multi-Rate – Wideband (AMR-WB) speech codec; Transcoding functions) (Streitpatentschrift, Abs. 0017). Aus
dieser Spezifikation ist dem Fachmann bekannt, dass die Prädiktion der
Verstärkung des festen Beitrags der Anregung in einem Unterrahmen von dem
quantisierten Energie-Prädiktionsfehler der letzten vier Unterrahmen abhängt (so
auch JELINEK, Sp. 11, Gl. (3) bis (6)), mithin die prädizierte Verstärkung des
festen Beitrags der Anregung in den Unterrahmen eines aktuellen Rahmens
auch von Parametern des vorhergehenden Rahmens abhängt.


2.    Das Streitpatent nennt demzufolge als Aufgabe, eine Technik zum Quantisieren der Verstärkungen der adaptiven und festen Anregungsbeiträge zur Verfügung
zu stellen, die die Robustheit des Codecs gegenüber Rahmenlöschungen oder Paketverlusten verbessert, die während der Übertragung der Codierparameter vom
Codierer zum Decodierer auftreten können (Abs. 0003).

Dazu sieht das Streitpatent vor, dass die Verstärkungen der adaptiven und festen
Beiträge der Anregung ohne eine Zwischen-Rahmen-Vorhersage quantisiert



                                                                              11/61

werden. Dieses Fehlen einer Zwischen-Rahmen-Vorhersage führe zu der gewünschten Verbesserung der Robustheit gegenüber Rahmenlöschungen oder Paketverlusten, die während der Übertragung von codierten Parametern auftreten
könnten. Die Verstärkung des adaptiven Anregungsbeitrags werde direkt quantisiert, während die Verstärkung des festen Anregungsbeitrags durch eine geschätzte
Verstärkung quantisiert werde. Die Schätzung der Verstärkung des festen Beitrags
der Anregung basiere auf Parametern, die sowohl beim Codierer als auch beim Decodierer vorhanden seien. Diese Parameter würden während der Verarbeitung des
aktuellen Rahmens berechnet. Somit seien im Verlauf der Quantisierung oder Decodierung keine Informationen von einem vorherigen Rahmen erforderlich, was die
Robustheit des Codecs gegenüber Rahmenlöschungen verbessere (Abs. 0014,
0015).


3.       Maßgeblicher Fachmann für die Lösung der genannten Aufgabe ist ein Ingenieur mit einem universitären Abschluss (Diplom oder Master) der Fachrichtung
Nachrichten- oder Informationstechnik, der über mehrjährige Berufserfahrung auf
dem Gebiet der Audiocodecs verfügt. Er verfolgt die Sitzungen der einschlägigen
Normierungs- und Standardisierungsgremien und kennt die dort diskutieren Entwicklungsvorschläge.


4.       Die erteilten nebengeordneten, codiererseitigen Vorrichtungsansprüche 1
und 4 lassen sich wie folgt gliedern (deutsche Übersetzung mit sprachlichen Anpassungen durch den Senat):

Patentanspruch 1:

 1        A device for quantizing a gain    Vorrichtung zum Quantisieren einer
                                            Verstärkung

 1.1      of a fixed contribution of an exci- eines festen Beitrags einer Anregung
          tation

 1.2      in a frame, including sub-frames, in einem, Unterrahmen enthaltenden,
          of a coded sound signal,          Rahmen eines codierten Tonsignals,




                                                                                12/61

2     comprising:                         umfassend:

2.1   an input for a parameter repre- einen Eingang für einen Parameter, der
      sentative of a classification of the für eine Klassifizierung des Rahmens
      frame;                              repräsentativ ist;

2.2   an estimator of the gain of the einen Schätzer der Verstärkung des
      fixed contribution of the excita- festen Beitrags der Anregung in einem
      tion in a sub-frame of said frame, Unterrahmen des Rahmens, wobei der
      using the parameter representa- Schätzer den Parameter, der für die
      tive of the classification of the Klassifizierung des Rahmens repräsenframe; and                          tativ ist, verwendet; und

2.3   a predictive quantizer of the gain einen prädiktiven Quantisierer der Verof the fixed contribution of the stärkung des festen Beitrags der Anreexcitation, in the sub-frame, us- gung im Unterrahmen, wobei der präing the estimated gain;             diktive Quantisierer die geschätzten
                                          Verstärkung verwendet;

3     wherein the predictive quantizer wobei der prädiktive Quantisierer einen
      determines a correction factor Korrekturfaktor für die geschätzte Verfor the estimated gain as a quan- stärkung als eine Quantisierung der
      tization of the gain of the fixed Verstärkung des festen Beitrags der
      contribution of the excitation;     Anregung bestimmt;

4     wherein the estimated gain mul- wobei die geschätzte Verstärkung mit
      tiplied by the correction factor dem Korrekturfaktor multipliziert die
      gives the quantized gain of the quantisierte Verstärkung des festen
      fixed contribution of the excita- Beitrags der Anregung ergibt; und
      tion; and

5     wherein     the   estimator   com- wobei der Schätzer für einen ersten Unprises, for a first sub-frame of the terrahmen des Rahmens umfasst:
      frame:




                                                                            13/61

5.1    (a) a first calculator of a linear (a) einen ersten Berechner einer lineaestimation of the gain of the fixed ren Schätzung der Verstärkung des
       contribution of the excitation     festen Beitrags der Anregung

5.1.1 in logarithmic domain               im Iogarithmischen Bereich

5.1.2 in response to the parameter in Reaktion auf den Parameter, der für
       representative of the classifica- die Klassifizierung des Rahmens reprätion of the frame;                 sentativ ist;

5.2    (b) a subtractor                   (b) einen Subtrahierer

5.2.1 of an energy of a filtered innova- einer Energie eines gefilterten Innovatition codevector from a fixed ons-Codevektors aus einem festen
       codebook in logarithmic domain     Codebuch im logarithmischen Bereich

5.2.2 from the linear gain estimation von der linearen Verstärkungsschätfrom the first calculator,         zung aus dem ersten Berechner,

5.2.3 the subtractor producing a gain wobei der Subtrahierer eine Verstärin logarithmic domain;             kung im Iogarithmischen Bereich erzeugt;

5.3    (c) a converter of the gain in Io- (c) einen Wandler der Verstärkung im I-
       garithmic domain from the sub- ogarithmischen Bereich aus dem Subtractor to linear domain to pro- trahierer in den linearen Bereich, um
       duce the estimated gain; and       die geschätzte Verstärkung zu erzeugen; und

5.4    (d) a multiplier                   (d) einen Multiplizierer

5.4.1 of the estimated gain               der geschätzten Verstärkung

5.4.2 by the correction factor            mit dem Korrekturfaktor,

5.4.3 to produce the quantized gain of um die quantisierte Verstärkung des
       the fixed contribution of the exci- festen Beitrags der Anregung zu erzeutation; and                        gen; und




                                                                              14/61

6      wherein the estimator, for each wobei der Schätzer für jeden Unterrahsub-frame of said frame follow- men des Rahmens, der dem ersten Uning the first sub-frame, is respon- terrahmen folgt, reagiert auf
       sive to

6.1    the parameter representative of den Parameter, der für die Klassifiziethe classification of the frame rung des Rahmens repräsentativ ist,
       and                                    und

6.2    gains of adaptive and fixed con- Verstärkungen von adaptiven und festributions of the excitation of at ten Beiträgen der Anregung mindesleast one previous sub-frame of tens eines vorhergehenden Unterrahthe frame                              mens des Rahmens reagiert,

6.3    to estimate the gain of the fixed um die Verstärkung des festen Beitrags
       contribution of the excitation.        der Anregung zu schätzen.




Patentanspruch 4:

4     A device for jointly quantizing gains     Vorrichtung   zum    gemeinsamen
                                                Quantisieren von Verstärkungen

1.3   of adaptive and                           von adaptiven und

1.1   fixed contributions of an excitation      festen Beiträgen einer Anregung

1.2‘ in a frame of a coded sound signal,        in einem Rahmen eines codierten
                                                Tonsignals,

2     comprising:                               umfassend:

2.4   a quantizer of the gain of the adap- einen Quantisierer der Verstärkung
      tive contribution of the excitation; and des adaptiven Beitrags der Anregung; und

1     the device for quantizing the gain of die Vorrichtung zum Quantisieren
      the fixed contribution of the excitation der Verstärkung des festen Beitrags



                                                                                  15/61

        as defined in any one of claims 1 to der Anregung, wie in einem der An-3.                                      sprüche 1 bis 3 definiert.




5.      Der Gegenstand des Streitpatents ist anhand der Patentansprüche 1 und 4
betrachtet. Die Vorrichtungs- und Verfahrensmerkmale der weiteren nebengeordneten Ansprüche entsprechen inhaltlich den funktionalen Merkmalen dieser Ansprüche. Der Fachmann versteht die Angaben in den erteilten Patentansprüchen 1 und
4 wie folgt:


5.1     Wie einleitend ausgeführt, sind dem Fachmann Vorrichtungen zum gemeinsamen Quantisieren von Verstärkungen der adaptiven und festen Beiträge einer
Anregung in einem Rahmen eines codierten Tonsignals, umfassend sowohl einen
Quantisierer der Verstärkung des adaptiven Beitrags der Anregung (Merkmale 4,
1.3, 1.2‘, 2 und 2.4) als auch eine Vorrichtung zum Quantisieren des festen Beitrags
der Anregung (Teil von Merkmal 1; Merkmal 1.1) aus seinem Fachwissen bekannt,
wie es beispielsweise durch die im Streitpatent genannte AMR-WB Spezifikation TS
26.190 und durch die Druckschrift JELINEK (Sp. 6, Z. 42 bis Sp. 11, Z. 61 und Sp.
13, Z. 67 bis Sp. 14, Z. 4), die auf die AMR-WB Spezifikation verweist, belegt ist.

Weiter ist dem Fachmann – wie einleitend dargelegt – bekannt, dass die aus dem
Stand der Technik bekannten Vorrichtungen zum Quantisieren einer Verstärkung
des festen Beitrags der Anregung (Merkmale 1, 1.1), in einem Unterrahmen enthaltenden Rahmen eines codierten Tonsignals (Merkmal 1.2), einen Schätzer der Verstärkung des festen Beitrags der Anregung in einem Unterrahmen des Rahmens
(Teil von Merkmal 2.2) und einen prädiktiven Quantisierer der Verstärkung des
festen Beitrags im Unterrahmen umfassen, der die von dem Schätzer geschätzte
Verstärkung (      ) des festen Beitrags verwendet (Merkmal 2.3) und einen Korrekturfaktor ( ) für die geschätzte Verstärkung als eine Quantisierung der Verstärkung
( ) des festen Beitrags bestimmen (Merkmal 3), wobei die geschätzte Verstärkung
(     ) mit dem Korrekturfaktor ( ) multipliziert die quantisierte Verstärkung ( ) des
festen Beitrags der Anregung ergibt (Merkmal 4). Es gilt mithin
                                         =



                                                                                 16/61

Dabei sind fachüblich in einem Verstärkungscodebuch Wertepaare (             , ) gespeichert, bestehend aus einer quantisierten Verstärkung          für den adaptiven Beitrag
der Anregung und aus dem Korrekturfaktor          für den festen Beitrag der Anregung.
Über die Minimierung der Energie eines Fehlersignals wird im Betrieb des Codecs
für jeden Unterrahmen das optimale Wertepaar (          , ) bestimmt (JELINEK, Sp. 14,
Z. 53 bis Sp. 16, Z. 16; Streitpatentschrift, Abs. 0060 bis 0065):




      Fig. 5 der Streitpatentschrift mit Kolorierung und Kommentierung durch den Senat


5.2     Das Streitpatent beschäftigt sich – wie einleitend dargelegt – mit einer Quantisierung der Verstärkung des festen Beitrags der Anregung, die einen modifizierten Schätzer verwendet, der – im Gegensatz zum Stand der Technik – nicht auf



                                                                                     17/61

Parameterwerte vorhergehender Rahmen zurückgreift, um so gegenüber Rahmenlöschungen und Paketverlusten robuster zu sein.

Mithin geht es dem Streitpatent darum, die in der vorstehend eingeblendeten Figur 5
der Streitpatentschrift gelb markierte geschätzte Verstärkung (estimated gain gc0),
aus der sich durch Multiplikation mit dem Korrekturfaktor g die quantisierte Verstärkung (quantized gain of the fixed part       =     g) ergibt, geeignet zu ermitteln.


                                                          ( )       ( ) ( )
5.3     Für den ersten Unterrahmen eines Rahmens (              =             ) sieht das Streit-
                                                                         ( )
patent die folgende Bestimmung der geschätzten Verstärkung                     und der quanti-
                        ( )
sierten Verstärkung           vor:




      Fig. 2 der Streitpatentschrift mit Kolorierung und Kommentierung durch den Senat

Die einzelnen Merkmale des Anspruchs 1, die Schaltungsblöcke gemäß den Figuren 2 und 5, sowie die darin vorgenommenen Berechnungsschritte hängen wie folgt
zusammen:




                                                                                           18/61

             Merkmalstext mit Bezugszeichen                   Formelzeichen,   Figur
                                                                Gleichung

2.1     an input for a parameter (classification t)                 t            2
        representative of a classification of the
        frame;

2.2     an estimator (200) of the gain (           ) of the                     2, 3
        fixed contribution (202) of the excitation in
        a sub-frame of said frame, using the parameter (t) representative of the classification of the frame; and

2.3     a predictive quantizer (500) of the gain                                2, 5
        (   ) of the fixed contribution (202, 502) of
        the excitation, in the sub-frame, using the
        estimated gain (     );

3       wherein the predictive quantizer (500) determines a correction factor (g) for the estimated gain (     ) as a quantization of the
        gain (   ) of the fixed contribution of the
        excitation;

4       wherein the estimated gain (               ) multi-        =    g      2, 3, 5
        plied by the correction factor (g) gives the
        quantized gain (     ) of the fixed contribution (202, 502) of the excitation; and

5       wherein the estimator (200) comprises,
        for a first sub-frame of the frame:

5.1     (a) a first calculator (201) of a linear esti-             +             2
                                  ( )
        mation of the gain (            ) of the fixed contribution (202, 502) of the excitation

5.1.1   in logarithmic domain                                                    2




                                                                                 19/61

 5.1.2   in response to the parameter (t) repre-                               +                     2
         sentative of the classification of the frame;

 5.2     (b) a subtractor (203)                                                                      2

 5.2.1   of an energy of a filtered innovation                                        ( )            2
                                                                      − log
         codevector (202) from a fixed codebook in
         logarithmic domain (215, 216, 217)

 5.2.2   from the linear gain estimation from the                                            ( )     2
                                                                  +         − log
         first calculator (201),

 5.2.3   the subtractor (203) producing a gain              ( )                                      2
             ( )
         (         ) in logarithmic domain;                                                    ( )
                                                            =     +           − log


                                                                      ( )              ( )
                                                                            = log

 5.3                                           ( )              ( )           ( )
                                                                                                     2
         (c) a converter (204) of the gain (         ) in             = 10
         Iogarithmic domain from the subtractor                                              ( )

         (203) to linear domain to produce the es-          = 10
                             ( )
         timated gain (            ); and




5.3.1 Nach Merkmal 2.2 verwendet der Schätzer den Klassifizierungsparameter.
Nach Auffassung der Klägerin verwendet hingegen der Rahmen (frame) den Parameter, weil „using” durch ein Komma von „frame” getrennt sei. Für ein solches Verständnis gibt es im Streitpatent keinerlei Stütze; stets verwendet der Schätzer 200
bzw. der darin enthaltene Berechner 201 den Klassifizierungsparameter.


5.3.2 Nach Auffassung der Klägerin sei die Formulierung „using the parameter representative of the classification of the frame“ sehr breit, jedenfalls breiter als die
ursprüngliche Formulierung „wherein the estimator is supplied with the parameter
representative of the classification of the frame“, denn sie impliziere jede mögliche




                                                                                                     20/61

Verwendungsmöglichkeit des Parameters. Die Verwendung sei nicht auf eine bestimmte Art und Weise beschränkt. Zudem „falle der Parameter einfach vom Himmel“.

Diese Auffassungen der Klägerin überzeugen nicht. Zunächst ist festzustellen, dass
„using the parameter“ zwar jede mögliche Verwendung in dem Schätzer implizieren
mag, jedoch eine Einschränkung gegenüber der Formulierung im ursprünglichen
Anspruch 1 ist, wonach dem Schätzer der Parameter zwar zur Verfügung gestellt
wurde („the estimator is supplied with the parameter“), aber, jedenfalls vom reinen
Anspruchswortlaut her, offenblieb, ob der Schätzer den Parameter auch tatsächlich
verwendet.

Weiter ist festzustellen, dass der Parameter nicht „vom Himmel fällt“, denn nach
Merkmal 2.1 („an input for a parameter representative of a classification of the
frame”) des erteilten Anspruchs 1 (wortgleich im ursprünglichen Anspruch 1) weist
die beanspruchte Vorrichtung einen Eingang für den Parameter auf, und zudem ist
der Schätzer gemäß Merkmal 2.2 Teil der beanspruchten Vorrichtung. Damit ist
dem Fachmann bewusst, dass dem Schätzer der Parameter intern, d. h. innerhalb
der beanspruchten Vorrichtung, zur Verfügung gestellt wird, nachdem die Vorrichtung den Parameter über ihren Eingang von extern bezogen hat.

Zudem wird die in Merkmal 2.2 genannte Verwendung des Parameters in den Merkmalsgruppen 5 und 6 insofern konkretisiert, dass der Schätzer für den ersten und
die weiteren Unterrahmen eine (lineare) Schätzung der Verstärkung des festen Beitrags des Anregungssignals in Antwort auf den Parameter durchführt, was der Fachmann – entgegen der Auffassung der Klägerin, wonach der Parameter nur im Sinne
eines „Präsenztests“ in die Schätzung eingehe – so versteht, dass der Klassifizierungsparameter die unabhängige Variable der Schätzung ist.

Nach Auffassung der Klägerin schließt der Anspruch 1 nicht aus, dass auch Parameter vergangener Rahmen in die Schätzung der Verstärkung des festen Beitrags
einfließen. Auch dieses Argument greift nicht, denn der Fachmann kann dem Streitpatent nicht entnehmen, dass außer dem Parameter, der für die Klassifizierung des




                                                                              21/61

aktuellen Rahmens repräsentativ ist, Parameter vorhergehender Rahmen einfließen. Im Gegenteil entnimmt der Fachmann dem Streitpatent zweifelsfrei, dass dies
nicht der Fall ist, denn das Streitpatent möchte die Nachteile des Stands der Technik
überwinden, die aus der Verwendung von Parametern vorhergehender Rahmen resultieren (vgl. BGH, Urteil vom 27. November 2018 – X ZR 16/17, GRUR 2019, 491
- Scheinwerferbelüftungssystem).


                                                            ( )
5.4     Die Ermittlung der quantisierten Verstärkung              für die auf den ersten Unterrahmen folgenden Unterrahmen eines Rahmens und der dafür verwendeten ge-
                                                ( )
schätzten, nicht-quantisierten Verstärkung            spiegelt sich in den Merkmalen 4, 6,
6.1, 6.2 und 6.3 sowie in der Figur 3 wider:




      Fig. 3 der Streitpatentschrift mit Kolorierung und Kommentierung durch den Senat



          Merkmalstext mit Bezugszeichen                 Formelzeichen,              Figur

                                                           Gleichung




                                                                                       22/61

 4                                                          ( )                     ( )           ( ) ( )             3, 5
       wherein the estimated gain (                               )                       =
       multiplied by the correction factor
       ( ( ) ) gives the quantized gain
           ( )
       (         ) of the fixed contribution (312)
       of the excitation; and

 6     wherein the estimator (300), for                                                                                3
       each sub-frame (k; k ≥ 2) of said
       frame following the first sub-frame,
       is responsive to

 6.1   the parameter (t) representative of                                                    +                        3
       the classification of the frame and

 6.2                                    ( )       ( )                                                                  3
       gains of adaptive (                    ,         , …) and                    ( )               ( )
                                                                                          +                 ,
                    ( )       ( )
       fixed (            ,         , …) contributions of
       the excitation of at least one previ-
                                                                      = 2, … ,
       ous (k – j; j = 1, … (k-1)) sub-frame
       of the frame

 6.3                                              ( )                  ( )          ( )
                                                                                                                       3
       to estimate the gain (                           ) of the             = 10
       fixed contribution of the excitation.                                          ∑
                                                                                                      ( )       ( )
                                                                      = 10

                                                                                          = 2, … ,




5.5    Das Streitpatent führt somit für jeden Unterrahmen eines aktuellen Rahmens
eine – im logarithmischen Bereich – lineare Schätzung der Verstärkung des festen
Beitrags der Anregung durch, die von einem Parameter (t) abhängt, der für die Klassifizierung des Rahmens repräsentativ ist.

Dem Fachmann ist bewusst, dass eine rahmenbasierte Klassifizierung des Sprachsignals bei CELP-basierten Codecs fachüblich ist. Daher sind dem Fachmann viele
Verfahren bekannt, wie Eigenschaften eines Eingangstonsignals ermittelt und in Abhängigkeit davon eine rahmenbasierte Signalklasse, etwa „unvoiced“, „voiced“, „generic“ oder „transition“, bestimmt werden kann (Abs. 0069 bis 0091).



                                                                                                                       23/61

5.6   Das Streitpatent gibt in einem Ausführungsbeispiel eine mögliche Zuordnung
von rahmenbasierten Signalklassen zu Werten des Klassifizierungsparameters t an,
nämlich t = 1 / 3 / 5 / 7 für die Klassen „unvoiced“, „voiced“, „generic“ und „transition“ bei Schmalbandsignalen und t = 0 / 2 / 4 / 6 für entsprechende Breitbandsignale (Abs. 0033).


Das Streitpatent verwendet, wie vorstehend dargelegt, eine – im logarithmischen
Bereich – lineare Schätzung für die Verstärkung des festen Beitrags der Anregung
im ersten Unterrahmen gemäß der Beziehung
                                ( )
                                      = 10
wobei a0 und a1 Schätzkoeffizienten sind, die bei der, dem Betrieb des Codecs vorgelagerten, Entwicklung des Codecs ermittelt werden und im Betrieb des Codecs
für jeweilige Unterrahmen Konstanten sind (Abs. 0055), weshalb die Beziehung vom
Fachmann wie folgt verstanden wird:
                               ( )          ( )   ( )
                                     = 10
Dadurch, dass auch für die Schätzung der Verstärkung des festen Beitrags der Anregung nur Größen des aktuellen Rahmens verwendet werden, insbesondere der
rahmenspezifische Klassifizierungsparameter t, erhöht sich die vom Streitpatent angestrebte Robustheit gegenüber Rahmenverlusten (Abs. 0031).

Der Klassifizierungsparameter t geht in der Designphase des Codecs in die Bestimmung der Schätzkoeffizienten ai und bi ein, die wiederum in das Design des Verstärkungscodebuchs einfließen, aus dem sich die Verstärkungsquantisierung ergibt,
wie dies in den Absätzen 0033 und 0041 bis 0059 der Streitpatentschrift im Detail
erläutert und in Figur 4 schematisch dargestellt ist:




                                                                                 24/61

              Fig. 4 der Streitpatentschrift mit Kolorierung durch den Senat


5.7    Das Merkmal

      5.1 (a) a first calculator of a linear estimation of the gain of the fixed
           contribution of the excitation

leistet auch einen technischen Beitrag zur patentgemäßen Lösung. Obwohl es, wie
die Klägerin geltend macht, theoretisch möglich wäre, mittels der Beziehung a0 + a1t
eine Tabelle anzulegen, aus der man dann die Schätzwerte in Abhängigkeit vom
Wert des Rahmenklassifizierungsparameter t ablesen könnte, wenn zuvor eine Zuordnung von Rahmenklassen zu entsprechenden Zahlenwerten von t durchgeführt
worden wäre, ändert diese Überlegung nichts an der Tatsache, dass der Term
a0 + a1t eine lineare Schätzung der Verstärkung des festen Beitrags der Anregung
(Merkmal 5.1) im logarithmischen Bereich (Merkmal 5.1.1) in Antwort auf den Klassifizierungsparameter (5.1.2) darstellt, wobei danach von dem linearen Schätzwert
mittels eines Subtrahierers (Merkmal 5.2) die Energie des gefilterten innovativen
Codevektors im logarithmischen Bereich abgezogen wird (Merkmal 5.2.2). Somit
liefert der Subtrahierer eine Verstärkung im logarithmischen Bereich (Merkmal




                                                                                   25/61

5.2.3), die anschließend von einem Umwandler in den linearen Bereich überführt
wird, um die geschätzte Verstärkung zu erzeugen (Merkmal 5.3). Jeder dieser mit
geeigneten Vorrichtungen durchzuführenden Verfahrensschritte ist keine mathematische Methode als solche, sondern gibt konkret an, wie die einzelnen, aus dem
jeweils vorliegenden Tonsignal extrahierten Parameter miteinander zu verknüpfen
sind, um die gesuchte Größe, nämlich die geschätzte Verstärkung (Merkmal 5.3)
bzw. darüber hinaus die quantisierte Verstärkung (Merkmale 5.4, 5.4.1, 5.4.2 und
5.4.3) für den ersten Unterrahmen eines Rahmens zu erhalten.


5.8    Die (Schätz-)Koeffizienten ai und bi werden gemäß den Angaben in der Streitpatentschrift nicht im Betrieb des Codecs, sondern zuvor („offline“), also bei der Entwicklung des Codecs, mittels einer großer Trainingsdatenbank gewonnen, die sowohl reine als auch rauschförmige und gemischte Sprachsignale in verschiedenen
Sprachen von Sprechern bzw. Sprecherinnen enthält (Abs. 0040, letzter Satz; Abs.
0041). Hierfür lässt man den Codec mit optimalen, nicht-quantisierten Werten der
adaptiven und festen Verstärkung, die mittels der oben wiedergegebenen Gleichungen (3) und (4) bestimmt worden sind, auf der großen Datenbank arbeiten, welche
N+1 Rahmen enthält (Abs. 0042, 0043). Der Rahmenindex n (n = 0, …, N) gehört
zu den rahmenbasierten Parametern, wie Klassifizierung, Innovationsenergie im
ersten Unterrahmen und optimale adaptive und feste Codebuch-Verstärkungen
(Abs. 0043).

Die Schätzkoeffizienten ai und bi werden durch Minimierung des mittleren quadratischen Fehlers (mean square error / MSE) zwischen der geschätzten Verstärkung
des festen Codebuchs und der optimalen Verstärkung im logarithmischen Bereich
über alle Rahmen in der Datenbank bestimmt (Abs. 0044). Im ersten Unterrahmen
ist der mittlere quadratische Fehler somit gegeben durch (Abs. 0045, Gl. (7)):


          ( )         ( )            ( )                 ( )               ( )
                =           ( )−      ,    ( )   =             ( ) − log    ,    ( )


Durch Einsetzen der oben wiedergegebenen Beziehung
                               ( )                               ( )
                                     =     +     − log



                                                                                       26/61

in die Gleichung (7) ergibt sich für den Fehler zwischen den geschätzten und optimalen festen Codebuchverstärkungen – über die gesamte Datenbank mit ihren N
Rahmen – folgendes (Abs. 0046, Gl. (8)):


                       ( )                                                           ( )                           ( )
                                =                 +         ( ) − log                      ( ) − log                ,    ( )


Da
                        ( )                                 ( )                            ( )
                                ( ) = log                         ( ) − log                 ,     ( ) ,      = 0, … ,      −1

eine normalisierte Verstärkung des innovativen Codevektors im logarithmischen Bereich ist, gilt dann:

                                                      ( )                                        ( )
                                                            =           +       ( )−                   ( )


Die Lösung des so definierten MSE-Problems, also die beiden Schätzkoeffizienten
                                                                                                             ( )                ( )
a0 und a1, erhält man durch Lösung der Gleichungen                                                                 = 0 und            =0

(vgl. Abs. 0051, Gl. (11)).


Entsprechend wird für alle auf den ersten Unterrahmen folgenden Unterrahmen verfahren (Gl. (12)):

                                            ( )                 ( )            ( )
                                                  =                   ( )−      ,    ( ) ,             = 2, … ,

Es ergibt sich ein umfangreiches lineares Gleichungssystem (Gl. (13), (14)), um für
den                  k-ten              Unterrahmen                      die           jeweiligen                   Schätzkoeffizienten
 ( )       ( )        ( )       ( )          ( )
       ,         ,          ,         ,…,               zu bestimmen. Dieses wird offline mit einem linearen
Gleichungslöser, wie MATLAB, gelöst (Abs. 0053 – 0058).


5.9        Wie einleitend dargelegt wird im Betrieb des Codierers das zuvor (offline)
während der Entwicklung des Codecs bestimmte Verstärkungsquantisierungscodebuch (designed gain codebook 503) verwendet, um für jeden Unterrahmen denjenigen von insgesamt Q Einträgen (q = 0, …, Q-1) zu ermitteln, der den kleinsten mittleren quadratischen Fehler MMSE (Minimum Mean Square Error) zwischen dem



                                                                                                                                  27/61

Zielsignal x(i) und dem gesamten Anregungssignal liefert, wobei jeder Eintrag des
Verstärkungscodebuchs aus einem Wertepaar besteht, nämlich der quantisierten
adaptiven Verstärkung gp und dem Korrekturfaktor , mit dem die nicht-quantisierte,
geschätzte Verstärkung gc0 multipliziert wird:




   Figur 5 der Streitpatentschrift mit Kolorierung und Kommentierung durch den Senat


Die zu minimierende Fehlerenergie E (505) ergibt sich zu (Gl. (15)):

                      =      =    −       −           −    −

Durch Ersetzen von gc durch gc0 und mit den aus Gleichung (4) ermittelten Konstanten bzw. Korrelationen c0, …, c5 ergibt sich (Gl. (16)):
                =    +       −2       +          −2        +2

wobei die geschätzte feste Verstärkung gc0 zuvor streitpatentgemäß – wie beschrieben – ermittelt wurde. Insofern wird das Verstärkungscodebuch 503 durchsucht, um




                                                                                  28/61

denjenigen Eintrag (adaptive quantisierte Verstärkung gp und Korrekturfaktor ) zu
bestimmen, der die in Gleichung (16) angegebene Fehlerenergie E minimiert.


5.10   Einen weiteren Quantisierer zeigt die Figur 6 der Streitpatentschrift:




                             Fig. 6 der Streitpatentschrift


Der Block 602 berechnet die Konstanten oder Korrelationen c0, …, c5 mittels Gleichung (4) aus dem Zielvektor x, dem gefilterten adaptiven Anregungsvektor y aus
dem adaptiven Codebuch und dem gefilterten festen Codevektor z aus dem festen
Codebuch. Der Block 603 verwendet Gleichung (16), um die Energie E des Fehlersignals ei aus der geschätzten nicht-quantisierten Verstärkung gc0 des festen Codebuchs, den Korrelationen c0, …, c5, der quantisierten adaptiven Verstärkung gp und
dem Korrekturfaktor    zu berechnen, wobei gp und             aus dem Verstärkungscodebuch 601 entnommen werden. Die Energie 604 des Fehlersignals wird an den Verstärkungscodebuch-Suchmechanismus zurückgeführt. Wie bei dem Quantisierer
nach Figur 5 werden die Einträge des Verstärkungscodebuchs 601 durchsucht, und
der Index, der die niedrigste Fehlerenergie 604 ergibt, wird ausgewählt und an den
Decodierer gesendet (Abs. 0066).



                                                                                   29/61

5.11     Im Decodierer wird der empfangene Index verwendet, um die Werte der
quantisierten Verstärkung gp des adaptiven Codebuchs und des Korrekturfaktors
aus dem Verstärkungscodebuch abzurufen. Die Schätzung der festen Codebuchverstärkung gc0 wird auf die gleiche Weise wie in dem Codierer durchgeführt. Der
quantisierte Wert gc der festen Codebuchverstärkung wird durch die Gleichung
     =        berechnet. Sowohl der adaptive Codevektor als auch der Innovationscodevektor werden aus dem Bitstrom decodiert und werden zu adaptiven und festen
Anregungsbeiträgen, die mit den jeweiligen Verstärkungen des adaptiven und festen Codebuchs multipliziert werden. Beide Anregungsbeiträge werden zur Gesamtanregung addiert. Das Synthesesignal wird erzeugt, indem die Gesamtanregung
durch ein LP-Synthesefilter gefiltert wird, wie es bei CELP-Codierung üblich ist (Abs.
0067).




                          II.   Zur unzulässigen Erweiterung

Der Gegenstand des Streitpatents geht nicht über den Inhalt der ursprünglichen
Anmeldung hinaus.


1.       Der Gegenstand des Anspruchs 1 in der erteilten Fassung geht in zulässiger
Weise      wie    folgt   auf   die   ursprüngliche   Anmeldung      (veröffentlicht    als
WO 2012/109734 A1, Anlage MFG3), zurück:

     Die Merkmale 1, 1.1, 1.2, 2, 2.1 und 2.3 sind wortidentisch dem ursprünglichen
     Anspruch 1 entnommen, die Merkmale 3 und 4 dem ursprünglichen Anspruch 2,
     die Merkmale 5, 5.1.1, 5.1.2, 5.2, 5.2.1, 5.2.2, 5.2.3, 5.3, 5.4, 5.4.1 und 5.4.2 dem
     ursprünglichen Anspruch 4 und die Merkmale 6, 6.1, 6.2 und 6.3 dem ursprünglichen Anspruch 5.

     Das Merkmal




                                                                                       30/61

  2.2 an estimator of the gain of the fixed contribution of the excitation in a subframe of said frame, using the parameter representative of the classification of the frame; and

basiert auf dem ursprünglichen Anspruch 1,

       an estimator of the gain of the fixed contribution of the excitation in a
       subframe of said frame, wherein the estimator is supplied with the
       parameter representative of the classiﬁcation of the frame; and

dem ursprünglichen Anspruch 26,

       receiving a parameter representative of the classification of the frame;
       estimating the gain of the fixed contribution of the excitation in a subframe of said frame, using the parameter representative of the classification of the frame; …

und dem Absatz 0032

       Only one estimation parameter is used by the calculator 201, the parameter t representative of the classification of the current frame.


Das Merkmal

  5.1 a first calculator of a linear estimation of the gain of the fixed contribution
       of the excitation

geht zurück auf den ursprünglichen Anspruch 4

       a calculator of a linear estimation of the gain of the ﬁxed contribution of
       the excitation

auf den Absatz 0032 und Figur 2 (zeigt einen ersten Berechner 201):

       the estimator 200 comprises a calculator 201 of a linear estimation of the
       fixed codebook gain

i. V. m. Absatz 0043 und Figur 3 (zeigt einen zweiten Berechner 302):

       a calculator 302 computes a linear estimation of the ﬁxed codebook gain
       again in logarithmic domain



                                                                                31/61

2.    Der von der Klägerin behauptete Unterschied in der Bedeutung des Merkmals 2.2 der erteilten Fassung („an estimator of the gain … using the parameter“)
zum ursprünglichen Anspruch 1 („an estimator of the gain … is supplied with the
parameter“) liegt bereits deshalb nicht vor, weil die ursprünglich offenbarte Zurverfügungstellung des Parameters an den Schätzer für den Fachmann die im Merkmal
2.2 genannte Verwendung des Parameters durch den Schätzer impliziert.


Dabei nimmt Merkmal 2.2 aufgrund des bestimmten Artikels („the parameter“) auf
den Parametereingang nach Merkmal 2.1 („an input for a parameter“) Bezug – somit
auf die Zurverfügungstellung des Parameters im Kontext der beanspruchten Vorrichtung. Zudem ist die in der erteilten Fassung genannte Verwendung des Parameters („using the parameter“), wie ausgeführt, ohnehin wörtlich in dem ursprünglichen Verfahrensanspruch 26 offenbart.

Der ursprüngliche unabhängige Anspruch 26 korrespondiert, anders als die Klägerin meint, nicht mit einem anderen Ausführungsbeispiel als der ursprüngliche Anspruch 1. Die ursprüngliche Anmeldung (veröffentlicht als WO 2012/109734 A1 (Anlage MFG3) wie auch das Streitpatent zeigen hinsichtlich der Quantisierung der Verstärkung des festen Beitrags des Anregungssignals in einem Rahmen eines codierten Tonsignals, der mehrere Unterrahmen umfasst, nur ein Ausführungsbeispiel,
wobei Figur 2 das Vorgehen für den ersten Unterrahmen und Figur 3 für die weiteren
Unterrahmen des Rahmens beschreibt. Dabei ist der ursprüngliche Anspruch 26
nichts Anderes als der zum ursprünglichen Vorrichtungsanspruch 1 korrespondierende Verfahrensanspruch.

Auch der Einwand der Klägerin, nach dem ursprünglichen Anspruch 1 müsse der
„strukturelle Schätzer“ mit dem Parameter beliefert werden, während nach dem ursprünglichen Anspruch 26, der ein Verfahren betreffe, das auch als rein geistige
Tätigkeit ausgeführt werden könne, ein struktureller Schätzer nicht notwendig sei
und daher auch die Zurverfügungstellung des Parameters nicht erforderlich sei,
überzeugt nicht. Entscheidend ist, was der Fachmann der Gesamtheit der ursprünglichen Unterlagen entnommen hat und nicht, wie einzelne ursprüngliche Ansprüche




                                                                                32/61

– isoliert betrachtet – ausgelegt werden können. Der Fachmann hat den ursprünglichen Unterlagen entnommen, dass der Schätzer einen Eingang für den Klassifizierungsparameter hat, diesen also von extern zur Verfügung gestellt bekommt (ursprünglicher Anspruch 1: an input for a parameter; ursprünglicher Anspruch 26: receiving a parameter) und dann diesen Parameter für die Schätzung auch tatsächlich
verwendet (Figuren 2 und 3 mit zugehöriger Beschreibung).

Auch der Blick in Absatz 0032 der Offenlegungsschrift WO 2012/109734 A1 (Anlage
MFG3) führt zu keinem anderen Ergebnis. Dort wird lediglich die allgemeine Verwendung des Parameters im Schätzer (ursprünglicher Anspruch 26) insofern konkretisiert, dass der Parameter vom Berechner 210 verwendet wird, der wiederum
Teil des Schätzers 200 ist.

„Using the parameter“ mag zwar für sich genommen jede mögliche Verwendung in
dem Schätzer implizieren, ist im Kontext des Streitpatents jedoch eine Einschränkung gegenüber der Formulierung im ursprünglichen Anspruch 1, nach der dem
Schätzer der Parameter zur Verfügung gestellt wird (the estimator is supplied with
the parameter), vom Anspruchswortlaut her allerdings offenbleibt, ob der Schätzer
den Parameter auch tatsächlich verwendet.

Die Argumentation der Klägerin, der Fachmann sei von der erteilten Fassung des
Streitpatents insofern „überrascht“, als dass der Klassifizierungsparameter dort nur
als „Trigger“, also als Auslöser für etwas fungiere, wohingegen nach der ursprünglichen Anmeldung der Parameter konkret in die Schätzung der Verstärkung des festen Beitrag des Anregungssignals eingehe, überzeugt nicht. Denn der erteilte Anspruch 1 umfasst – wie vorstehend ausgeführt – die Verwendung des Klassifizierungsparameters durch den Schätzer, wobei die (lineare) Schätzung den Parameter
als unabhängige Variable verwendet. Im Übrigen war die von der Klägerin herangezogene Formulierung „in response to“ auch schon in der ursprünglichen Anmeldung
enthalten (Anlage MFG3: Abs. 0031; Ansprüche 3, 4, 19, 28, 29, 44).




                                                                               33/61

3.    Der Anspruch 2 geht in zulässiger Weise auf die ursprünglichen Ansprüche
6 und 7 zurück, Anspruch 3 auf Anspruch 10, Anspruch 4 auf Anspruch 12 und die
Ansprüche 5 bis 8 auf die Ansprüche 13 bis 16.

Der Anspruch 9 geht in zulässiger Weise auf die ursprünglichen Ansprüche 18, 19,
20 und auf Absatz 0075 der ursprünglichen Anmeldung zurück, der Anspruch 10
auf den Anspruch 23 und den Absatz 0075, der Anspruch 11 auf den Anspruch 24.

Der Anspruch 12 geht in zulässiger Weise auf die ursprünglichen Ansprüche 26, 27,
29 und 30 zurück, der Anspruch 13 auf die Ansprüche 31 und 32, der Anspruch 14
auf den Anspruch 35.

Der Anspruch 15 geht in zulässiger Weise auf den ursprünglichen Anspruch 37 zurück, der Anspruch 16 auf den Anspruch 38.

Der Anspruch 18 geht in zulässiger Weise auf die ursprünglichen Ansprüche 43, 44
und 45 und auf Absatz 0075 der Offenlegungsschrift (Anlage MFG3) zurück, Anspruch 19 auf Anspruch 46.

Der Anspruch 20 geht in zulässiger Weise auf den ursprünglichen Anspruch 48 und
auf Absatz 0075 der Offenlegungsschrift (Anlage MFG3) zurück, Anspruch 21 auf
Anspruch 49.




                             III.   Zur Ausführbarkeit

Die Erfindung ist im Streitpatent so deutlich und vollständig offenbart, dass der
Fachmann sie ausführen kann. Das Streitpatent gibt dem Fachmann eine vollständige und nacharbeitbare Lösung an die Hand.


1.    Entgegen der Behauptung der Klägerin kann der Fachmann den in den Merkmalen 2.1, 2.2, 5.1.2 und 6.1 genannten Parameter bestimmen, der repräsentativ
für die Klassifizierung des Rahmens ist, ohne selbst erfinderisch tätig zu werden.




                                                                               34/61

In Absatz 0033 der Streitpatentschrift sind – wie bereits zur Auslegung dargelegt –
konkrete Beispiele für Zahlenwerte des Parameters t in Abhängigkeit von der jeweils
vorliegenden Rahmenklasse angegeben. Für Schmalbandsignale der Klassen „unvoiced“, „voiced“, „generic“ und „transition frame“ die Werte 1, 3, 5, bzw. 7 und für
Breitbandsignale der genannten Klassen die Werte 0, 2, 4 bzw. 6. Damit gibt das
Streitpatent dem Fachmann eine vollständige und nacharbeitbare Lösung an die
Hand. Diese kann er zudem als Grundlage für eigene Optimierungsversuche heranziehen, da ihm aus dem Streitpatent (Abs. 0033, 0041 bis 0059) bekannt ist, dass
und wie der Klassifizierungsparameter t in die Bestimmung der Schätzparameter ai
und bi für die Verstärkung gc0 des festen Beitrags des Anregungssignals einfließt.
In diesem Sinne ist der Fachmann auch frei in der Festlegung der Werte des Klassifizierungsparameters t im Sinne einer Wahl nach freiem Ermessen (Abs. 0033:
„can be chosen arbitrarily“).

Die in den Absätzen 0041 bis 0059 beschriebene Bestimmung der Schätzkoeffizienten ai und bi ist – jedenfalls für eine Patentschrift – ungewöhnlich ausführlich
und detailreich und versetzt den Fachmann in die Lage, die Lehre des Streitpatents
nachzuarbeiten. Die dort genannte große (Trainings-)Datenbank enthält – wie dies
dem Fachmann geläufig ist – eine große Anzahl von Signalen unterschiedlicher
Sprechproben, nämlich ungestörte und gestörte, leise und laute Sprachsignalabschnitte in verschiedenen Sprachen und verschiedenen Frequenzbereichen (Abs.
0041). Eine solche Datenbank zum Training von Audio-Codecs aufzubauen und zu
verwenden gehört zur fachmännischen Routinearbeit und bedarf daher keiner weitergehenden Erläuterung. Die Datenbank enthält N+1 Rahmen, wobei sich der Klassifizierungsparameter t je nach den Signaleigenschaften der einzelnen Rahmen von
Rahmen zu Rahmen unterscheiden kann (Abs. 0043). Die einzelnen Berechnungsschritte zur Ermittlung der Schätzkoeffizienten ai und bi mittels der Datenbank und
unter Verwendung der optimalen, nicht-quantisierten Verstärkungswerte sind dem
Fachmann zum einen bekannt, zum anderen werden sie im Streitpatent im Einzelnen beschrieben.

Wie dargelegt, geht auch der Klassifizierungsparameter t in die Trainingsdatenbank
und damit in die Entwicklung des Verstärkungsquantisierungscodebuchs ein (Abs.



                                                                                35/61

0051, Gl. (11); Abs. 0056, Gl. (14)). Er stellt somit einen von mehreren Optimierungsparametern dar. Ausgehend von den im Streitpatent genannten Zahlenwerten
für unterschiedliche Rahmenklassen (Abs. 0033) geht es über fachübliche Routinearbeit nicht hinaus, diese Werte zu variieren, um eine (weitere) Optimierung zu erreichen. Die Behauptung der Klägerin, die Wahl geeigneter Werte des Klassifizierungsparameters liege nicht im Wissen des Fachmanns und er könne auch keine
sinnvollen Experimente durchführen, trifft somit nicht zu.

Die Auffassung der Klägerin, die in Absatz 0033 genannten Zahlenwerte für den
Parameter t, 1 für stimmlose und 3 für stimmhafte Signale, seien technisch unsinnig,
weil sich – bei der Annahme eines positiven Schätzkoeffizientens a1 (in den Schätzwert geht der Term a0 + a1t ein) – für stimmhafte Signale ein größerer Schätzwert
für die Verstärkung des festen Beitrags des Anregungssignals ergebe als für stimmlose Signale, wobei dem Fachmann jedoch bekannt sei, dass bei stimmhaften Signalen, die durch eine große Periodizität der Signalanteile gekennzeichnet seien, die
Verstärkung des adaptiven Signalanteils der Anregung größer und die des festen
(innovativen) Signalanteils kleiner sein müsse als bei stimmlosen Signalen, überzeugt nicht. Es kann allerdings dahinstehen, ob der Fachmann aufgrund seines
Fachwissens im Absatz 0033 der Streitpatentschrift eine offensichtliche Unrichtigkeit erkennt, die er zu „for narrowband signals, the values of parameter t are set to:
1, 3, 5, and 7, for voiced, unvoiced, generic, and transition frames, respectively“
korrigiert, denn jedenfalls wird dort für allgemeine Rahmen und Übergangsrahmen
eine größere Verstärkung (5 bzw. 7) für den festen (innovativen) Signalanteil vorgeschlagen als für Sprachsignale (1 bzw. 3), was die Vorurteile des Fachmanns bestätigt und ihn veranlasst, wie ausgeführt, die im Absatz 0033 genannten beispielhaften Zahlenwerte als Startwerte für eine nachgelagerte Optimierung zu verwenden.


2.     Auch kann der Fachmann dem Streitpatent entnehmen, was die lineare
Schätzung
                           ( )          ( )
                                 = 10         = 10




                                                                                 36/61

(Merkmale 2, 2.1, 2.2, 5 bis 5.3) leisten soll. Dies gilt auch dann, wenn gemäß Absatz 0032 der Streitpatentschrift nur zwei unterschiedliche Parameterwerte für die
Klassen „stimmhaft“ (voiced) und „stimmlos“ (unvoiced) verwendet werden.

Selbst wenn das Streitpatent im Absatz 0032 eine Variante mit nur zwei Rahmenklassen und dementsprechend zwei Parameterwerten offenbart, ergibt eine lineare
Schätzung, beinhaltend den Term a0 + a1t, einen Schätzwert in (linearer) Abhängigkeit vom jeweiligen Parameterwert t eines Rahmens. Zudem geht der Fachmann
unter Berücksichtigung der Angaben in den Absätzen 0032 und 0033 ohnehin davon aus, dass regelmäßig vier oder mehr (strongly voiced, voiced, unvoiced;
strongly unvoiced, generic, transition) verschiedene Rahmenklassen und entsprechende Parameterwerte verwendet werden. Dem Fachmann ist dabei bewusst,
dass eine lineare Schätzung basierend auf dem Klassifizierungsparameter t – im
Vergleich zu Schätzungen, bei denen der Parameter z. B. quadratisch in den
Schätzwert eingeht – eine vergleichsweise einfache Berechnung zur Folge hat und
damit Vorteile bei der Entwicklung des Codecs und bei seinem späteren Betrieb
bietet (Absätze 0041 bis 0059).


3.       Nach alledem ist der Fachmann in der Lage die Erfindung so nachzuarbeiten,
dass sich der gewünschte Effekt – die Unabhängigkeit der Schätzung der Verstärkung des festen Beitrags des Anregungssignals von Parametern vorhergehender
Rahmen – einstellt.




                             IV.    Zur Patentfähigkeit

Der Gegenstand des Streitpatents in der erteilten Fassung erweist sich als patentfähig.

Das Streitpatent löst ein technisches Problem mit technischen Mitteln; eine „mathematischen Methode als solche“ im Sinne des Art. 52 Abs. 2 Buchst. a) EPÜ i. V. m
Art. 52 Abs. 3 EPÜ liegt nicht vor. Die unter Schutz gestellte Lehre erweist sich zu-




                                                                                37/61

dem gegenüber dem im Verfahren entgegengehaltenen Stand der Technik JE-LINEK (US 7,778,827 B2; Anlage MFG5), TADDEI (Efficient coding of transitional
speech segments in CELP; Anlage MFG6) und GAO (US 7,191,122 B1; Anlage
MFG7) als neu und auf erfinderischer Tätigkeit beruhend, Art. II § 6 Abs. 1 Nr. 1
IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54 und 56 EPÜ.


1.      Das Streitpatent löst ein technisches Problem mit technischen Mitteln. Weder liegt eine „mathematischen Methode als solche“ im Sinne des Art. 52 (2) lit. a
EPÜ i. V. m Art. 52 (3) EPÜ vor, noch sind einzelne Merkmale als nicht-technisch
bei der Prüfung auf Patentfähigkeit nicht zu beachten.

Entgegen dem Verständnis der Klägerin leisten alle Merkmale des Gegenstands
des Anspruchs 1 einen Beitrag zur Lösung des der Erfindung zugrundeliegenden
technischen Problems, insbesondere auch die Merkmalsgruppen 5.1, 5.2 und 5.3,
die sich mit der Bestimmung eines Schätzwertes der Verstärkung des festen Signalanteils für den ersten Unterrahmen befassen, ohne auf vorhergehende Rahmen
oder Unterrahmen zurückzugreifen.

Der Senat vermag sich der Auffassung der Klägerin, die lineare Schätzung der Verstärkung des festen Beitrags des Anregungssignals auf Grundlage des Klassifizierungsparameters t sei technisch nicht nachvollziehbar und habe auch keinen technischen Effekt, nicht anzuschließen. Auch ihre Behauptung, es sei nicht erkennbar,
wie die lineare Schätzung der festen Verstärkung die Robustheit gegen Rahmenverluste verbessere, vielmehr stelle sie nur eine mathematische Methode im Sinne
von Art. 52 Abs. 2 Buchst. a) EPÜ dar, sodass zumindest die Merkmalsgruppen 5.1,
5.2 und 5.3 bei der Betrachtung der Patentfähigkeit außer Acht bleiben müssten, da
diese nach dem Ansatz des Europäischen Patentamts als nicht-technische Merkmale anzusehen seien, überzeugt nicht. Auch teilt der Senat die Sichtweise der Klägerin nicht, der Klassifizierungsparameter t sei im Streitpatent völlig willkürlich (Abs.
0033: …can be chosen arbitrarily) definiert, sodass er beliebige Werte annehmen
könne, wobei völlig im Belieben stehende Werte keine technische Wirkung entfalten
könnten, und keine Zuordnung von Rahmenklassen auf (willkürliche) Werte des
Klassifizierungsparameters offenbare.



                                                                                    38/61

Das Streitpatent löst das technische Problem, die Robustheit gegenüber Rahmenverlusten zu erhöhen, d. h. Störungen, die durch Rahmenverluste bei dem auf der
Decodiererseite rekonstruierten Sprachsignal auftreten würden, zu verhindern oder
zumindest zu verringern (Abs. 0003, 0014, 0015, 0031). Hierfür setzt das Streitpatent mehrere technische Mittel ein. So werden die optimalen, nicht-quantisierten
adaptiven und innovativen Verstärkungen, die für das Training und das Design des
Verstärkungscodebuchs (welches die quantisierte adaptive Verstärkung und den
Korrekturfaktor für die feste Verstärkung enthält) verwendet werden (Abs. 0021),
nur auf Grundlage der Signale im aktuellen Rahmen bestimmt (Abs. 0019, 0020).
Im Betrieb des Codecs werden die adaptive Verstärkung gp, der Korrekturfaktor
und die geschätzte innovative Verstärkung gc0 mittels Fehlerminimierung auf Unterrahmen-Basis ermittelt, d. h. ebenfalls ohne Einbeziehung von Werten aus vorhergehenden Rahmen (Fig. 5, 6; Gl. (5) – (16)). Ein Verlust eines oder mehrerer vorhergehender Rahmen wirkt sich daher nicht negativ auf die im aktuellen Rahmen
bestimmten adaptiven und innovativen Verstärkungen aus.

Die unterrahmenbasierte Schätzung der innovativen Verstärkung muss für den ersten Unterrahmen des aktuellen Rahmens anders ausgeführt werden als für die noch
folgenden Unterrahmen dieses Rahmens, da noch keine Werte der adaptiven und
innovativen Verstärkung aus der Vergangenheit vorliegen. Das Streitpatent verwendet eine lineare Schätzung für die innovative Verstärkung im ersten Unterrahmen,
wobei der Klassifizierungsparameter t die unabhängige Variable der linearen Schätzung ist:
                           ( )          ( )
                                 = 10         = 10
Wie bereits zur Ausführbarkeit der Erfindung dargelegt, ist die Wahl des Klassifizierungsparameters t nicht völlig willkürlich, vielmehr nimmt der Fachmann, ausgehend
von den in Absatz 0033 der Streitpatentschrift genannten klassenspezifischen Parameterwerten, eine weitere Optimierung vor. In den einzelnen Verfahrensschritten
gemäß den Merkmalsgruppen 5.1, 5.2 und 5.3, die von der vorstehend genannten
Gleichung abgebildet werden, werden im Betrieb des Codes für den ersten Unterrahmen eines aktuellen Rahmens der Rahmenparameter t und die Energie Ei des
innovativen Codevektors verarbeitet, wobei die Schätzkoeffizienten a0 und a1 – wie




                                                                                39/61

dargelegt – feste (aber für jeden Unterrahmen andere) Werte sind. Das Ergebnis
des Verfahrensablaufs gemäß den Merkmalsgruppen 5.1 bis 5.3 ist die geschätzte
Verstärkung gc0 des festen Beitrags des Anregungssignals im ersten Unterrahmen
des aktuellen Rahmens, die mithin ohne Rückgriff auf Werte vorausgehender Rahmen bestimmt wurde. Damit wird ein technisches Problem gelöst, wobei die eingesetzten Mittel technischer Natur sind, weil tatsächlich vorliegende Signale bzw. daraus abgeleitete Größen geeignet weiterverarbeitet werden, um die gesuchte Größe
zu bestimmen.

Auch soweit die Klägerin der Auffassung ist, ein Teil der oben genannten Gleichung
zur Bestimmung von gc0, nämlich der Term a0 + a1t, könnte auch in Form einer Look-Up-Tabelle gespeichert werden, wobei dann im Betrieb für die jeweiligen Werte des
Parameters t gespeicherte, dem Ausdruck a0 + a1t entsprechende, Werte aus der
Tabelle ausgelesen werden könnten, stützt dies nicht die Annahme mangelnder
Technizität. Vielmehr handelt es sich dabei nur um eine hypothetische Variante zur
Implementierung der Verfahrensschritte zur linearen Schätzung der Verstärkung gc0
des festen Beitrags des Anregungssignals gemäß den Merkmalsgruppen 5.1, 5.2
und 5.3. Selbst ein solches Auslesen aus einer Tabelle würde nichts daran ändern
, dass der Term a0 + a1t eine lineare Schätzung der Verstärkung des festen Beitrags
der Anregung (Merkmal 5.2) im logarithmischen Bereich (Merkmal 5.1.1) in Antwort
auf den Klassifizierungsparameter (5.1.2) liefern würde, wobei von dem linearen
Schätzwert mittels eines Subtrahierers (Merkmal 5.2) die Energie des gefilterten
innovativen Codevektors im logarithmischen Bereich abgezogen würde (Merkmal
5.2.2). Somit liefert der Subtrahierer eine Verstärkung im logarithmischen Bereich
(Merkmal 5.2.3), die anschließend von einem Umwandler in den linearen Bereich
überführt wird, um die geschätzte Verstärkung zu erzeugen (Merkmal 5.3). Jeder
dieser Verfahrensschritte ist keine mathematische Methode als solche, sondern gibt
konkret an, wie die einzelnen technischen Parameter, die auf gemessenen Signalen
bzw. daraus abgeleiteten Größen basieren, miteinander zu verknüpfen sind, um die
gesuchte Größe, nämlich die geschätzte Verstärkung (Merkmal 5.3) bzw. darüber
hinaus die quantisierte Verstärkung (Merkmale 5.4, 5.4.1, 5.4.2 und 5.4.3) für den
ersten Unterrahmen eines Rahmens zu erhalten.




                                                                               40/61

Die weitere Annahme der Klägerin, die Verfahrensansprüche 12, 15, 18 und 20
seien nichts weiter als Teile einer mathematischen Methode, weil ein Fachmann die
einzelnen Verfahrensschritte, die rein geistige Tätigkeiten darstellten, auf einem
Blatt Papier ausführen könne, trifft ebenfalls nicht zu. Es kann dahinstehen, ob Verfahrensschritte von einer Person auf einem Blatt Papier (oder mittels eines Computerprogramms) ausgeführt werden können. Jedenfalls beschreiben die Verfahrensansprüche 12, 15, 18 und 20 die Arbeitsweise der Vorrichtungen gemäß den Ansprüchen 1, 4, 9 und 10, d. h. auch die einzelnen Verfahrensmerkmale beschreiben
technische Maßnahmen durch die eine technische Aufgabe gelöst wird, nämlich die
Verstärkung des festen Beitrags der Anregung in einem Rahmen eines codierten
Tonsignals einzeln (Anspruch 12) bzw. gemeinsam mit der adaptiven Verstärkung
zu quantisieren (Anspruch 15) bzw. entsprechende Schritte auf Seiten des Decodierers durchzuführen (Ansprüche 18 und 20).
Jedenfalls ist dem Fachmann gegenwärtig, dass die unter Schutz gestellten Verfahren auf einer konkreten technischen Vorrichtung ablaufen, um Audiosignale in der
angegebenen Art und Weise codieren und decodieren zu können.

Nach alledem löst das Streitpatent ein technisches Problem mit technischen Mitteln.


2.   Der Gegenstand von Patentanspruch 1 ist neu gegenüber dem vorliegenden
Stand der Technik nach JELINEK, TADDEI und GAO und wird dem Fachmann
durch diesen auch nicht nahegelegt.

Die folgenden Ausführungen zum Vorrichtungsanspruch 1 gelten jeweils in gleicher
Weise für die weiteren nebengeordneten Vorrichtungs- und Verfahrensansprüche
4, 9, 10, 12, 15, 18 und 20, die jeweils Merkmale umfassen, die mit den Merkmalsgruppen 5 und 6 übereinstimmen oder diesen inhaltlich entsprechen.


2.1 Der Gegenstand des Anspruchs 1 des Streitpatents ist nicht vollständig aus
JELINEK (US 7,778,827 B1) bekannt und somit dieser Druckschrift gegenüber neu.




                                                                                41/61

2.1.1      Die Druckschrift JELINEK beschäftigt sich wie das Streitpatent mit der
gemeinsamen Quantisierung der Verstärkung des adaptiven und des festen Beitrags des Anregungssignals bei einem Breitband-Sprachcodec, wobei im Betrieb
des Codecs für jeden Unterrahmen eines Rahmens ein optimales Wertepaar in einem Verstärkungscodebuch, welches quantisierte adaptive Verstärkungen gp und
Korrekturfaktoren     (zur Quantisierung der festen Verstärkung) enthält, ermittelt
wird. Dabei findet – ebenfalls wie im Streitpatent und wie aus dem AMR-WB Standard bekannt, auf den auch JELINEK verweist – eine Prädiktion der Verstärkung
des festen Beitrags des Anregungssignals statt, mithin eine Bestimmung des
Schätzwertes g‘c, im Streitpatent als gc0 bezeichnet, wobei sich die quantisierte Verstärkung gc ergibt durch (JELINEK, Sp. 10, Z. 35 bis Sp. 11, Z. 61):

                                           =

Für die Prädiktion von      wird ein gleitender Mittelwert (moving average) über die
letzten vier vorhergehenden Unterrahmen gebildet, wobei ein Rahmen vier Unterrahmen umfasst, so dass stets Parameterwerte vorhergehender Rahmen in die
Schätzung eingehen (Sp. 10, Z. 57 bis Sp. 11, Z. 36), wie es auch aus dem AMR-WB Standard bekannt ist, und wie es das Streitpatent gerade vermeiden möchte:

                                               ∑                   ∑     ()
                                      = 10 ,
                         ( ( )    )                 (   )
            ( ) = 10 ,

Dabei ist N die Anzahl der Abtastwerte im Unterrahmen n (N = 64),         ist der Mittelwert der Energie des festen (innovativen) Codevektors und wird – ebenfalls wie im
AMR-WB Standard – als fester Wert 30 dB angenommen,               sind die Prädiktionskoeffizienten [b1, b2, b3, b4] = [0.5, 0.4, 0.3, 0.2], c(i) sind die Elemente des festen
(innovativen) Anregungsvektors und         ( − ) ist der quantisierte Energieprädiktionsfehler des Unterrahmens n-i.


2.1.2 In dem Abschnitt „Gain Quantization in Variable Bit Rate Coding“ geht JE-LINEK auf quellengesteuerte VBR-Codecs ein, insbesondere auf den quellengesteuerten, multimodalen VBR-Codec des CDMA2000-Systems in der Konfiguration
„Rate Set II“, den JELINEK als VMR-WB-Codec (Variable Multi-Rate Wide-Band)
bezeichnet und der vier Quellen-Bitraten umfasst (13,3 (FR = Full Rate), 6,2 (HR =
Half Rate), 2,7 (QR = Quarter Rate) und 1,0 kbit/s (ER = Eigth Rate)) und dessen



                                                                                   42/61

höchste Bitrate (FR) auf dem AMR-WB Standard mit 12,65 kbit/s basiert. Für stationäre stimmhafte Rahmen wird ein stimmhaftes HR-Codierungsmodell verwendet,
für stimmlose Rahmen ein stimmloses HR- oder QR-Model, für Rahmen mit Hintergrundrauschen ein ER Komfortrauschgenerator. Falls der Bitratenauswahlalgorithmus für einen bestimmten Rahmen FR wählt, aber das Kommunikationssystem nur
HR zulässt, wird ein generisches HR-Modell verwendet, das auch für Rahmen geeignet ist, die weder als stimmhaft noch als stimmlos klassifiziert wurden und die
eine relativ geringe Energie haben (Sp. 11, Z. 62 – Sp. 13, Z. 15):




Für die höchste Bitrate FR wird ein Verstärkungsquantisierungscodebuch mittels
bekannten Trainingsmethoden entwickelt, das für alle Signalklassen (voiced, unvoiced, transient, onset, offset) gilt. Auch bei „Voiced and Generic HR“ müssen
adaptive und innovative Verstärkung quantisiert werden.

Jedoch ist es bei niedrigen Bitraten vorteilhaft, die Anzahl der Quantisierungsbits zu
reduzieren, was die Entwicklung neuer Codebücher erforderlich macht. Darüber hinaus ist für „Voiced HR“ ein neues signalklassenspezifisches Verstärkungsquantisierungscodebuch erforderlich (Sp. 13, Z. 17 – 29).

Daher stellt JELINEK eine Verstärkungsquantisierung für CELP-basierte VBR-Codierung zur Verfügung, die eine Reduzierung der Bitanzahl ermöglicht, ohne dass
neue Quantisierungscodebücher für die Codierung bei niedrigen Bitraten erforderlich wären (Sp. 13, Z. 29 – 34). Insbesondere wird (nur) ein Teil des für den „Generic
FR coding type“ entwickelten Codebuchs verwendet. Das Verstärkungsquantisierungscodebuch wird basierend auf der adaptiven Verstärkung geordnet. Basierend




                                                                                 43/61

auf einer anfänglichen adaptiven Verstärkung, die während einer längeren Zeitspanne, z. B. während zweier Unterrahmen, berechnet worden ist, wird der entsprechende Teil des Verstärkungsquantisierungscodebuchs ausgewählt (Sp. 13, Z. 34
– 45).

Die nicht-quantisierte adaptive Verstärkung in einem Unterrahmen berechnet sich
zu (x(n): Zielsignal; y(n): gefilterter adaptiver Codebuchvektor; N: Anzahl der Abtastwerte im Unterrahmen) (Gl. (10)):
                                       ∑    ( ) ( )
                                   =
                                       ∑    ( ) ( )

Nach einem ersten Ausführungsbeispiel von JELINEK (Sp. 14, Z. 6 – Sp. 18, Z. 35)
wird für den ersten Unterrahmen eines vier Unterrahmen umfassenden Rahmens
eine anfängliche adaptive Verstärkung gi auf der Basis der ersten beiden Unterrahmen des gleichen Rahmens berechnet (Anzahl der Abtastwerte für zwei Unterrahmen: 2N) (Gl. (11)):
                                      ∑     ( ) ( )
                                  =
                                      ∑     ( ) ( )

Bei einer Halbratencodierung (HR) der ersten beiden Unterrahmen wird die gemeinsame Quantisierung der adaptiven Verstärkung gp und der innovativen Verstärkung
gc auf einen Teil des Vollratencodebuchs (FR) eingeschränkt, wobei dieser Teil
durch den Wert von gi, also der anfänglichen (über zwei Unterrahmen berechneten)
adaptiven Verstärkung, bestimmt wird. Nach dem ersten Ausführungsbeispiel von
JELINEK werden bei FR-Codierung die Verstärkungen gp und gc gemeinsam mit 7
Bits quantisiert, wobei, wie bereits vorstehend erläutert, eine gleitende Mittelwert-Prädiktion (MA) für die innovative Anregungsenergie im logarithmischen Bereich
angewendet wird, um eine prädizierte innovative Codebuchverstärkung zu erhalten;
danach wird der Korrekturfaktor   quantisiert. Bei einer anfänglichen adaptiven Verstärkung gi kleiner als 0,768606 wird die Quantisierung in den ersten beiden Unterrahmen auf die erste Hälfte des entsprechenden FR-Codebuchs (Sp. 15, 16:
TABLE 3), ansonsten auf die zweite Hälfte eingeschränkt (Sp. 14, Z. 41 – Sp. 15,
Z. 1). Für jeweils zwei Unterrahmen wird ein Bit benötigt, um (dem Decodierer) an-




                                                                                44/61

zuzeigen, welcher Teil des Quantisierungs-Codebuchs für die Quantisierung verwendet wird (Sp. 15, Z. 4 – 6). Für den dritten und vierten Unterrahmen eines Rahmens wird entsprechend verfahren (Sp. 16, Z. 61 – Sp. 17, Z. 5).

Im Vergleich zur Übertragung von 28 Bits pro Rahmen (7 Bits pro Unterrahmen) bei
einer FR-Codierung zum Quantisieren der Verstärkungen gp und gc, benötigt die
von JELINEK für eine HR-Codierung vorgeschlagene Verwendung jeweils nur einer
Hälfte des Codebuchs nur 26 Bits pro Rahmen (6 Bits pro Unterrahmen plus 2 extra
Bits pro Rahmen zur Signalisierung, welche Hälfte des Codebuchs für den ersten
und zweiten bzw. den dritten und vierten Unterrahmen verwendet wird). Dieser Ansatz liefere im Vergleich zu einer Neuentwicklung eines 6-Bit-Codebuchs eine bessere Qualität, die sogar gleich oder besser sei als die, die mit dem ursprünglichen
7-Bit-Quantisierer erreicht wurde (Sp. 17, Z. 28 – 38).


2.1.3 Der Annahme der Klägerin, die von JELINEK zur Auswahl der „passenden“
Hälfte des Verstärkungsquantisierungscodebuchs verwendete anfängliche (über
die ersten beiden bzw. über den dritten und vierten Unterrahmen berechnete) adaptive Verstärkung gi sei ein Klassifizierungsparameter im Sinne von Merkmal 2.1,
denn der Fachmann wisse, dass die adaptive Verstärkung von der Klassifizierung
des Rahmens abhänge, und der Wert von gi gehe gemäß Merkmal 2.2 in die Schätzung der Verstärkung des festen Beitrags des Anregungssignals ein, teilt der Senat
nicht.

Der Anspruch 1 des Streitpatents beansprucht nach den Merkmalen 1 und 1.1 eine
Vorrichtung zur Quantisierung der Verstärkung des festen Beitrags eines Anregungssignals, die gemäß Merkmal 2.1 einen Eingang für einen Rahmenklassifizierungsparameter hat und gemäß dem Merkmal 2.2 einen Schätzer für die Verstärkung des festen Beitrags der Anregung umfasst, der diesen Parameter auch verwendet, wie in den Merkmalen 5.1.2 und 6.1 für die verschiedenen Unterrahmen
angegeben.

Dem Fachmann ist zwar bekannt, dass die in JELINEK bestimmte anfängliche
adaptive Verstärkung gi in einem gewissen Zusammenhang zur den Signaleigenschaften des Rahmens (bzw. zu den Signaleigenschaften der für die Bestimmung


                                                                              45/61

der anfänglichen adaptiven Verstärkung verwendeten ersten beiden Unterrahmen)
steht. Jedoch wird gemäß JELINEK der Wert von gi nur zur Auswahl eines Teilbereichs des bei der Verstärkungsquantisierung verwendeten Codebuchs herangezogen, hilft also dabei, die Suche nach dem optimalen Wertepaar (gp; γ) zu vereinfachen; für die Schätzung der Verstärkung g‘c des festen Beitrags des Anregungssignals, die vor der Quantisierung durchgeführt wird, spielt der Wert von gi bei der aus
JELINEK bekannten Vorrichtung hingegen keine Rolle. Insofern sind jedenfalls die
Merkmale 2.2, 5.1.2 und 6.1 aus JELINEK nicht bekannt.


2.1.4 Auch die Annahme der Klägerin, der Mittelwert          der Energie des festen (innovativen) Codevektors sei ein Parameter, der für die Rahmenklasse repräsentativ
sei und gehe über die aus JELINEK bekannte Beziehung
                                               ∑    (    )            ∑     ()
            ( ) = 10 ,    ( ( )   )
                                      = 10 ,
in die Bestimmung des Schätzwertes         ( ) der Verstärkung des festen Beitrags ein,
wie es von den Merkmalen 2.1, 2.2, 5.1.2 und 6.1 gefordert werde, verfängt nicht.
Wie bereits dargelegt, nimmt JELINEK für den Mittelwert            stets, d. h. unabhängig
von den tatsächlich vorliegenden Signaleigenschaften im aktuellen Rahmen, einen
festen Wert von 30 dB an (JELINEK, Sp. 11, Z. 12). Somit erfüllt auch der Mittelwert
  der Energie des festen (innovativen) Codevektors nicht die Anforderungen gemäß
den Merkmalen 2.1 und 2.2.


2.1.5 Auch die Annahme der Klägerin, dass wegen der aus JELINEK bekannten
Zusammenhänge

                         ( ) = ( ) − ( ) = 20 log       = 20 log

und
                                               ∑    (    )            ∑     ()
            ( ) = 10 ,    ( ( )   )
                                      = 10 ,

in die Schätzung der Verstärkung des festen Beitrags des Anregungssignals für die
weiteren, auf den ersten Unterrahmen folgenden Unterrahmen, auch Verstärkungen
der festen Beiträge des Anregungssignals vorhergehender Unterrahmen des aktuellen Rahmens eingingen, wie von den Merkmalen 6.2 und 6.3 gefordert, überzeugt
nicht. Es kann dahinstehen, ob aufgrund des Unterschieds zwischen                ( ) und



                                                                                     46/61

 ( − ) der von der Klägerin gezogene Schluss zutrifft. Weiter kann dahinstehen,
ob der Fachmann – vor dem Hintergrund der Probleme des Standes der Technik,
die das Streitpatent lösen will – die Merkmalsgruppe 6 so versteht, dass Verstärkungswerte von Unterrahmen, die nicht zum aktuellen, sondern zum vorhergehenden Rahmen gehören, nicht in die Schätzung der Verstärkung des festen Beitrags
eingehen dürfen, was nach JELINEK für alle vier Unterrahmen (Sp. 14, Z. 9) eines
aktuellen Rahmens der Fall ist, weil stets Werte der vier dem aktuellen Unterrahmen
vorausgehenden Unterrahmen eingehen. Denn jedenfalls ist den obigen Gleichungen im Unterschied zu Merkmal 6.2 nicht zu entnehmen, dass auch Verstärkungen
der adaptiven Beiträge des Anregungssignals in die Schätzung der Verstärkung des
festen Beitrags der Anregung eingehen.


2.1.6 Entgegen der Annahme der Klägerin sind weder die Parameter gi und , noch
der in Tabelle 4 von JELINEK genannte Parameter „Class Info“, der nach Auffassung der Klägerin gemäß Merkmal 2.2 vom Schätzer des festen Beitrags des Anregungssignals verwendet wird, als Parameter im Sinne des Merkmals 2.1 anzusehen. Der Parameter „Class Info“ wird in JELINEK vom Codierer bestimmt und ist die
Grundlage für die Auswahl des im betrachteten Rahmen verwendeten Codier-Modells (Sp. 12, Z. 11 bis 15 und 33 bis 38). Zwar trifft es zu, dass der Parameter
„Class Info“ gemäß Merkmal 2.1 repräsentativ für die Klassifikation des aktuellen
Rahmens ist, jedoch kann der Fachmann JELINEK nicht entnehmen, dass dieser
Parameter gemäß den Merkmalen 2.1, 5.1.2, und 6.1 von dem Schätzer zur Verstärkung des festen Beitrags des Anregungssignals verwendet würde.


2.1.7       Nach alledem ist aus JELINEK nicht mehr bekannt als:

        1    A device for quantizing a gain
                 Fig. 4, Schritt 402: finding intial index in 7-bit joint gain quantization codebook; Schritt 405: find index best meeting search criterion; Schritt 406: Quantizer for expressing index selected by
                 searcher 405 with 6 bits per subframe; Anspruch 31: An encoder
                 … being arranged … to perform a joint quantization to jointly
                 quantize the first and second gain parameters …



                                                                                     47/61

1.1     of a fixed contribution of an excitation
           Anspruch 31: second gain parameter[s], Anspruch 39: the second gain parameter is an innovation gain; Anspruch 40: the second gain parameter ist an innovation gain correction factor
1.2     in a frame, including sub-frames, of a coded sound signal,
           Anspruch 31: consecutive frames, each frame comprising a number of sub-frames
2      comprising
2.1     an input for a parameter representative of a classification of the frame;
           Wie einleitend dargelegt, kann sowohl die anfängliche adaptive
           Verstärkung gi als Parameter angesehen werden, der – im weitesten Sinne – für die Klassifizierung des Rahmens repräsentativ
           ist, also auch der Parameter „Class Info“.
2.2teils an estimator of the gain of the fixed contribution of the excitation in a
        sub-frame of said frame, using the parameter representative of the
        classification of the frame; and
           Wie dargelegt, wird die Verstärkung         ( ) des festen Beitrags des
           Anregungssignals in dem n-ten Unterrahmen wie folgt geschätzt:

                                          ∑                   ∑    ()
                         ( ) = 10 ,           (    )



           Daraus ist zu erkennen, dass weder die – möglicherweise die Rahmenklasse repräsentierende – anfängliche adaptive Verstärkung
           noch der Parameter „Class Info“ in die Schätzung von          eingeht.

2.3     a predictive quantizer of the gain of the fixed contribution of the excitation, in the sub-frame, using the estimated gain;
           Sp. 11, Z. 40, Gl. (7) umgeformt:       =
3      wherein the predictive quantizer determines a correction factor for the
       estimated gain as a quantization of the gain of the fixed contribution of
       the excitation;
           Sp. 11, Z. 40, Gl. (7):    =

4      wherein the estimated gain multiplied by the correction factor gives the
       quantized gain of the fixed contribution of the excitation; and


                                                                             48/61

            Sp. 11, Z. 40, Gl. (7)) umgeformt:      =
5       wherein the estimator comprises, for a first sub-frame of the frame:
5.1      (a) a first calculator of a linear estimation of the gain of the fixed contribution of the excitation
5.1.1     in logarithmic domain
5.1.2nicht in response to the parameter representative of the classification of
          the frame;
            Wie zum Merkmal 2.2 ausgeführt, geht weder gi noch „class info“ in
            die Schätzung des festen Beitrags der Verstärkung ein.
5.2      (b) a subtractor
5.2.1     of an energy of a filtered innovation codevector from a fixed codebook in logarithmic domain
5.2.2     from the linear gain estimation from the first calculator,
5.2.3     the subtractor producing a gain in logarithmic domain;
5.3      (c) a converter of the gain in Iogarithmic domain from the subtractor to
         linear domain to produce the estimated gain; and
            Zu den Merkmalen 5 bis 5.3: Gemäß JELINEK findet die Prädiktion
            für die ersten beiden Unterrahmen und danach für den dritten und
            vierten Unterrahmen eines Rahmens statt. Insofern gilt die Prädiktion nach JELINEK auch für den ersten Unterrahmen eines Rah-
                                                    ∑                   ∑      ()
            mens. Zudem gilt           ( ) = 10 ,         (   )
                                                                                    .
            Die lineare Schätzung spiegelt sich in dem Term ∑            ( − ) wider, wobei      (   − ) der quantisierte Energieprädiktionsfehler im
            Unterrahmen n - i ist und die lineare Schätzung im logarithmischen
            Bereich stattfindet, da der Term ∑           ( − ) im Exponenten der
            Funktion 10(…) steht. Für die Schätzung wird die Energie                =

            10 log     ∑        ( ) subtrahiert, wobei    die Energie des gefilter-

            ten innovativen Codevektors ist (Sp. 11, Z. 25 – 30). Über die Funktion 10(…) findet die Umwandlung vom logarithmischen in den linearen Bereich statt.

5.4      (d) a multiplier



                                                                               49/61

5.4.1     of the estimated gain
5.4.2     by the correction factor
5.4.3     to produce the quantized gain of the fixed contribution of the excitation; and
            Zu der Merkmalsgruppe 5.4: Sp. 11, Z. 40, Gl. (7) ergibt umgeformt:
               =
6       wherein the estimator, for each sub-frame of said frame following the
        first sub-frame, is responsive to
6.1nicht the parameter representative of the classification of the frame and
            Wie zum Merkmal 2.2 ausgeführt, geht weder gi noch „class info“ in
            die Schätzung des festen Beitrags der Verstärkung ein.
6.2teils gains of adaptive and fixed contributions of the excitation of at least
         one previous sub-frame of the frame
6.3      to estimate the gain of the fixed contribution of the excitation.
            Zu der Merkmalsgruppe 6: Gemäß JELINEK ist die innovative
            Verstärkung für den zweiten Unterrahmen gleich derjenigen des
            ersten Unterrahmens; der dritte und vierte Unterrahmen werden
            ähnlich bestimmt wie der erste und zweite. Wie einleitend dargelegt gehen in die zu Merkmal 2.2 angegebene Gleichung jedenfalls keine adaptiven Verstärkungen von mindestens einem vorhergehenden Unterrahmen des betrachteten Rahmens ein. Zudem geht der Prädiktionsfehler der letzten vier Unterrahmen der
            dem betrachteten Unterrahmen vorhergehenden Unterrahmen
            ein, d. h. in die Schätzung der Verstärkung des festen Beitrags
            der Anregung gehen gemäß JELINEK stets Größen aus den vorhergehenden Rahmen ein, was der Fachmann, wie einleitend
            dargelegt, beim Gegenstand des Anspruchs 1 des Streitpatents
            ausschließt, da das Streitpatent wegen der angestrebten Robustheit gegenüber Rahmenlöschungen keine Parameterwerte
            vorhergehender Rahmen verwendet.




                                                                             50/61

Danach ist der Gegenstand des Anspruchs 1 nicht vollständig aus JELINEK bekannt
und somit dieser gegenüber neu.


2.2    Der Gegenstand des Patentanspruchs 1 ist neu gegenüber der Entgegenhaltung TADDEI (Efficient coding of transitional speech segments in CELP, Anlage
MFG6).


2.2.1 Gemäß TADDEI enthalten Sprachsignale eine beträchtliche Menge von transienten Segmenten (z. B. onsets), die bei rahmen- bzw. unterrahmenbasierter Signalverarbeitung nur schwer mit guter Qualität zu codieren seien. TADDEI schlägt
zur Verbesserung der Codierung von transienten Unterrahmen vor, den Beitrag des
adaptiven Codebuchs zum Anregungssignal außer Acht zu lassen und den Beitrag
des innovativen (festen) Codebuchs zu stärken, was bei jedem CELP-ähnlichen
Standardsprachcodierer ohne Änderung der Bitrate angewendet werden könne
(Abstract).

TADDEI stellt fest, dass in nicht-stationären Sprachabschnitten das adaptive Anregungssignal keinen konstruktiven (sinnvollen) Beitrag leisten würde, weil es naturgemäß (nur) die periodischen Signalanteile repräsentiere. Dennoch würden normalerweise viele Bits zur Codierung der adaptiven Codebuchverstärkung und der Tonhöhe verwendet, was nutzlos sei. Damit stünden weniger Bits für die (in dieser Situation) wichtigere innovative (feste) Anregung zur Verfügung (Abschnitt 1. Introduction, S. 14, li. Sp., letzter Abs. bis S. 14, re. Sp., Abs. 1).

Ein weiteres Problem sieht TADDEI in der recht groben gemeinsamen Vektorquantisierung von adaptiver und fester Codebuchverstärkung. Dies könne zu Situationen
führen, in denen – trotz niedriger adaptiver und hoher innovativer Verstärkung – der
ausgewählte Verstärkungsvektor eine große adaptive und eine kleine innovative
Verstärkung aufweise. Dies sei der niedrigen Anzahl von Codewörtern in dem Verstärkungsquantisierungscodebuch und der Optimierung hinsichtlich stationärer Unterrahmen geschuldet (Abschnitt 1. Introduction, S. 14, re. Sp., Abs. 2; Abschnitt 2.
Classfication: Onset Detection, S. 15, li. Sp., Abs. 2, 3).




                                                                                51/61

2.2.2 Daher sei es laut TADDEI besser, sich sowohl in Phasen mit stark steigender
Energie als auch in Phasen mit großer Energie der innovativen Anregung auf eine
möglichste genaue Quantisierung der innovativen (festen) Verstärkung zu fokussieren, als zu versuchen, eine gemeinsame Quantisierung von adaptiver und innovativer Verstärkung zu optimieren. Insbesondere bei sehr großen innovativen Verstärkungen sei es besser, diese skalar zu quantisieren (S. 15, li. Sp., Abs. 3).

TADDEI detektiert „onsets“ durch Überwachung der Energien aufeinanderfolgender
Rahmen- und Unterrahmen:




(   ,   : Energie des aktuellen bzw. vorherigen Rahmens;       ,   : Energie des ersten bzw. zweiten Unterrahmens des aktuellen Rahmens;          : Energie des zweiten
Unterrahmens des vorherigen Rahmens).


2.2.3 TADDEI geht von einem ITU-T 4 kps Codec-Vorschlag aus, der einen
„mode 1“ für periodische Rahmen und einen „mode 0“ für nicht-periodische Rahmen
vorsieht:




                                                                                52/61

TADDEI modifiziert den „mode 0“, bei dem die adaptive und die innovative (feste)
Verstärkung mit 7 Bits je Unterrahmen gemeinsam vektorquantisiert werden, insofern, als dass einer der 128 Einträge des Vektorquantisierungsverstärkungscodebuchs zur Anzeige eines „Onsets“ verwendet wird. Wenn der Decodierer diesen
Eintrag empfängt, weiß er, dass ein Onset vorliegt und Tonhöhe (pitch (lag) value)
und Tonhöhenverstärkung (adaptive gain) nicht verwendet, sondern als „Null“ angenommen werden. Da der Tonhöhenwert nicht übertragen wird, können die dafür
vorgesehen Bits zur skalaren Quantisierung der Verstärkung gf des festen Beitrags
des Anregungssignals verwendet werden (S. 15, re. Sp., zweiter und vorletzter
Abs.).

Wenn im „Mode 0“ ein Onset in einem der beiden Unterrahmen detektiert wird, stehen laut TADDEI im betreffenden Unterrahmen 108 Werte (entspricht 6,75 Bits), die
nun nicht mehr für die Codierung des Tonhöhensignals (pitch lag) benötigt werden,
für die Codierung der innovativen (festen) Verstärkung zur Verfügung, was jedoch
gar nicht erforderlich ist. Daher schlägt TADDEI vor, die innovative (feste) Verstärkung mit 54 Werten (entspricht 5,75 Bits) skalar zu quantisieren und das so „gewonnene“ Bit ergänzend für die Quantisierung des innovativen (festen) Anregungssignals zu verwenden (S. 16, li. Sp., Abs. 2):




2.2.4 Trotz dieser Änderungen muss laut TADDEI die ursprüngliche Struktur der
Vektorquantisierung mit der gleitenden Mittelwertvorhersage (moving average prediction) der Energie beibehalten werden, um die Speicher des moving average Filters für nachfolgende Unterrahmen, die keinen „Onset“ enthalten, zu aktualisieren
(S. 16, li. Sp., Abs. 2). Hier entnimmt der Fachmann, dass TADDEI grundsätzlich



                                                                                53/61

von einem prädiktiven Quantisierer der Verstärkung des festen Beitrags des Anregungssignals ausgeht, der – wie z. B. aus JELINEK bekannt – mittels Parameterwerten vorhergehender Unterrahmen einen Schätzwert für die feste Verstärkung
ermittelt und diesen Schätzwert durch Multiplikation mit einem Korrekturfaktor quantisiert, der über eine übliche Fehlerminimierung bestimmt wurde (S. 14, 15, Abschnitt 2).


Die Annahme der Klägerin, der Fachmann entnehme TADDEI, dass für einen transienten Unterrahmen, also einen Unterrahmen mit detektiertem Onset, von der fachüblichen und auch in TADDEI genannten gleitenden Mittelwertvorhersage zur Bestimmung der Verstärkung des festen Beitrags des Anregungssignals abgewichen
und stattdessen diese Verstärkung ohne Rückgriff auf Parameter des vorhergehenden Rahmens bestimmt würde, überzeugt nicht.

Wie ausgeführt lässt sich TADDEI nur entnehmen, dass bei einem detektierten Onset in einem Unterrahmen die adaptive Verstärkung nicht gemeinsam mit der festen
Verstärkung vektorquantisiert wird, sondern dass in diesem Fall nur die skalar quantisierte feste Verstärkung bestimmt und an den Decodierer übertragen wird. Wie die
quantisierte feste Verstärkung für einen Onset-Unterrahmen ermittelt wird, lässt sich
TADDEI nicht im Detail entnehmen, insbesondere nicht, dass dafür eine lineare
Schätzung auf Basis eines Klassifikationsparameters durchgeführt wird.

Im Übrigen lehrt TADDEI, wie vorstehend dargelegt, die – fachübliche und z. B. aus
JELINEK bekannte – gleitende Mittelwertvorhersage zur Bestimmung eines Schätzwertes der Verstärkung des festen Beitrags der Anregung beizubehalten, d. h. für
alle Unterrahmen eines Rahmes, auch für diejenigen mit einem detektierten Onset,
die Verstärkung des festen Beitrags des Anregungssignals mit Hilfe von Parametern
vorhergehender Unterrahmen, und damit auch vorhergehender Rahmen, zu schätzen, wenngleich der so ermittelte Wert für die „Onset-Unterrahmen“ nicht für die
Quantisierung der Verstärkung des festen Beitrags verwendet wird.

Im Übrigen offenbart TADDEI – selbstverständlich – nicht, dass stets nur der erste
Unterrahmen eines Rahmens einen „Onset“ aufweist (Table 2).




                                                                                54/61

2.2.5         Nach alledem zeigt TADDEI nicht mehr als

        1      A device for quantizing a gain
        1.1     of a fixed contribution of an excitation
                   S. 16, li. Sp., Abs. 2: a 5.75 bit scalar quantizer for gf
        1.2     in a frame, including sub-frames, of a coded sound signal,
                   S. 15, re. Sp., Abschnitt 3: In mode 0, a frame is composed of
                   two subframes with 10 ms each
        2      comprising
        2.1teils an input for a parameter representative of a classification of the frame
                subframe;
                   S. 16, li. Sp., Tab. 2: Es wird nicht auf Rahmen- sondern auf Unterrahmenbasis detektiert, ob ein Onset vorliegt oder nicht.
        2.2teils an estimator of the gain of the fixed contribution of the excitation in a
                sub-frame of said frame, using the parameter representative of the
                classification of the frame; and
                   Wenn ein Onset in einem Unterrahmen detektiert wird, wird der
                   adaptive Beitrag des Anregungssignals und die adaptive Verstärkung auf Null gesetzt (S. 15, re. Sp., vorletzter Abs.); wie dargelegt
                   kann der Fachmann TADDEI nicht entnehmen, wie in diesem Fall
                   die quantisierte Verstärkung des festen Beitrags des Anregungssignals bestimmt wird; selbst wenn er mitlesen würde, dass bei einem
                   Onset-Unterrahmen der optimale quantisierte Wert (von 54 möglichen Werten, vgl. S. 16, li. Sp., Abs. 2) der festen Verstärkung mittels Minimierung des mittleren quadratischen Fehlers ermittelt wird,
                   wäre dies nicht als „Schätzung“ des Verstärkungswertes im Sinne
                   des Streitpatents zu verstehen; ein rahmenspezifischer Klassifizierungsparameter des Rahmens geht in die Bestimmung der festen
                   Verstärkung ohnehin nicht ein.

                   Jedoch liest der Fachmann in TADDEI – wie einleitend dargelegt –
                   mit, dass für Unterrahmen, in denen kein Onset detektiert wird, eine
                   Schätzung der Verstärkung des festen Beitrags des Anregungssignals mittels gleitender Mittelwertvorhersage zum Einsatz kommt,



                                                                                     55/61

             wie sie auch aus JELINEK bekannt ist. Insofern kann das Merkmal
             2.2 für die „Nicht-Onset-Unterrahmen“ als aus TADDEI bekannt angesehen werden.

2.3teils a predictive quantizer of the gain of the fixed contribution of the excitation, in the sub-frame, using the estimated gain;
             vgl. die vorstehenden Ausführungen zu Merkmal 2.2, d. h. für die
             „Nicht-Onset-Unterrahmen“ liest der Fachmann einen prädiktiven
             Quantisierer für die Verstärkung des festen Beitrags der Anregung
             in TADDEI mit; für die Onset-Unterrahmen gilt dies nicht.

3teils   wherein the predictive quantizer determines a correction factor for the
         estimated gain as a quantization of the gain of the fixed contribution of
         the excitation;
             vgl. die einleitenden Bemerkungen und die vorstehenden Ausführungen zu den Merkmalen 2.2 und 2.3
4teils   wherein the estimated gain multiplied by the correction factor gives the
         quantized gain of the fixed contribution of the excitation; and
             vgl. die einleitenden Bemerkungen und die vorstehenden Ausführungen zu den Merkmalen 2.2 und 2.3
5teils   wherein the estimator device comprises, for a first an onset sub-frame
         of the frame:
             Wie dargelegt, wird für einen Onset-Unterrahmen zwar eine quantisierte Verstärkung des festen Beitrags der Anregung bestimmt, jedoch findet für einen Onset-Unterrahmen keine Schätzung eines
             Verstärkungswertes statt, der anschließend mittels Multiplikation eines Korrekturfaktors quantisiert würde.
5.1nicht (a) a first calculator of a linear estimation of the gain of the fixed contribution of the excitation
5.1.1nicht in logarithmic domain
5.1.2nicht in response to the parameter representative of the classification of
           the frame;
5.2nicht (b) a subtractor




                                                                               56/61

5.2.1nicht of an energy of a filtered innovation codevector from a fixed codebook in logarithmic domain
5.2.2nicht from the linear gain estimation from the first calculator,
5.2.3nicht the subtractor producing a gain in logarithmic domain;
5.3nicht (c) a converter of the gain in Iogarithmic domain from the subtractor to
         linear domain to produce the estimated gain; and
5.4nicht (d) a multiplier
5.4.1nicht of the estimated gain
5.4.2nicht by the correction factor
5.4.3nicht to produce the quantized gain of the fixed contribution of the excitation; and
           zu den Merkmalen 5.1 bis 5.4.3: vgl. die vorstehenden Ausführungen zu den Merkmalen 2.2, 2.3 und 5
6teils   wherein the estimator, for each sub-frame of said frame following the
         first onset sub-frame, is responsive to
           vgl. die Ausführungen zu den Merkmalen 2.2, 2.3 und 5, sowie
           S. 16, li. Sp., Tab. 2, Zeile “Subframe1: yes; Subframe 2: no”, wonach die quantisierte Verstärkung des festen Beitrags des Anregungssignals für Unterrahmen, die auf einen Onset-Unterrahmen
           folgen, fachüblich mit einer Schätzung und einem Korrekturfaktor
           zur Quantisierung bestimmt wird, und dabei weder ein rahmenklassenspezifischer Parameter noch adaptive Verstärkungen der vorhergehenden Unterrahmen eingehen; zudem gehen – was das
           Streitpatent vermeidet – Parameter vorhergehender Unterrahmen
           ein, wie vorstehend zu JELINEK dargelegt.
6.1nicht the parameter representative of the classification of the frame and
6.2teils gains of adaptive and fixed contributions of the excitation of at least
         one previous sub-frame of the frame
           Wie vorstehend und wie zu JELINEK dargelegt, gehen bei der fachüblichen und aus JELINEK bekannten Schätzung allenfalls Verstärkungswerte der festen Beiträge des Anregungssignals aus vorhergehenden Unterrahmen ein; im Unterschied zum Streitpatent jedoch auch Werte vorhergehender Rahmen.


                                                                            57/61

      6.3teils to estimate the gain of the fixed contribution of the excitation.
                 vgl. die Ausführungen zu Merkmal 6


Danach ist der Gegenstand des Anspruchs 1 neu gegenüber der aus TADDEI bekannten Vorrichtung.


2.3    Der Gegenstand des Patentanspruchs 1 des Streitpatents ergibt sich für den
Fachmann auch nicht in naheliegender Weise aus einer Kombination der technischen Lehren von JELINEK und TADDEI.


2.3.1 Es ist schon nicht ersichtlich, warum der Fachmann ausgehend von der Entgegenhaltung JELINEK, die sich mit dem Einsparen von zu übertragenden Bits des
Verstärkungscodebuchs in Abhängigkeit vom Wert der adaptiven Verstärkung in
den ersten zwei Unterrahmen eines vier Unterrahmens umfassenden Rahmens beschäftigt, die Druckschrift TADDEI, die sich mit einer effizienten Codierung von Onset-Unterrahmen beschäftigt, heranziehen sollte. Aber selbst wenn der Fachmann
die beiden Druckschriften kombinieren würde, ist – angesichts der jeweiligen Unterschiede zum Gegenstand des Streitpatents – nicht zu erkennen, wie sich der Gegenstand des Anspruchs 1 des Streitpatents für den Fachmann in naheliegender
Weise aus den beiden Druckschriften ergeben sollte.


2.3.2 Es ist nicht dem Wissen des Fachmanns zuzuordnen, dass die adaptive und
feste Verstärkung signalklassenabhängig sind, dass fachüblich die Rahmenklasse
bei Codecs bestimmt wird, und dass es bei einer Signalübertragung regelmäßig zu
Rahmenverlusten kommen kann.


Selbst ausgehend von der Aufgabe, die Verstärkung für einen Rahmen festzulegen,
der auf einen verlorengegangenen Rahmen folgt, ist kein Anlass erkennbar, der den
Fachmann zu der Überlegung führen würde, eine lineare Schätzung in Abhängigkeit
eines Klassifizierungsparameters der jeweiligen Rahmenklasse vorzunehmen.




                                                                                   58/61

Demnach ergibt sich die streitpatentgemäße Lösung, die lineare Schätzung der festen Verstärkung in Abhängigkeit eines klassenspezifischen Parameters ohne Rückgriff auf vorherige Rahmen vorzunehmen, für den Fachmann nicht als „platte Selbstverständlichkeit“.

Es ist schon zweifelhaft, ob sich der Fachmann ausgehend von JELINEK überhaupt
mit dem Problem von Rahmenlöschungen beschäftigen würde. Aber selbst unter
der Annahme, er würde dies tun, könnte der Fachmann bei dem aus JELINIK bekannten gleitenden Mittelwertverfahren zur Bestimmung der prädizierten Energie
 ( )=∑          ( − ) z. B. einen Mechanismus vorsehen, der bei einer Rahmenlöschung für den quantisierten Energievorhersagefehler ( − ) vergangene Werte
unverändert beibehält.

Danach ist nicht ersichtlich, wie der Fachmann ausgehend von JELINEK in naheliegender Weise zum Gegenstand des Anspruchs 1 des Streitpatents gelangen
sollte. Auch die Berücksichtigung der in TADDEI offenbarten Lehre führt den Fachmann nicht in naheliegender Weise zum Gegenstand des Anspruchs 1 des Streitpatents, insbesondere, da auch TADDEI weder die streitpatentgemäße lineare
Schätzung der Verstärkung des festen Beitrags der Anregung auf Basis eines rahmenklassenspezifischen Parameters noch – für die auf den ersten Unterrahmen
folgenden Unterrahmen – die Berücksichtigung der adaptiven Verstärkungen mindestens eines vorhergehenden Unterrahmens des aktuellen Rahmens zeigt.


2.4     Der Gegenstand von Patentanspruchs 1 ist durch die Entgegenhaltung
GAO (US 7,778,827 B2) weder vorweggenommen noch dem Fachmann in Verbindung mit seinem Fachwissen nahegelegt.

Auch GAO kann keine Anregungen liefern, ausgehend von JELINEK zum Gegenstand des Anspruchs 1 des Streitpatents zu gelangen, denn GAO geht hinsichtlich
der Schätzung der festen Codebuchverstärkung (GAO, Sp. 36, Z. 10 – 45) nicht
über die entsprechende Lehre von JELINEK (JELINEK, Sp. 10, Z. 57 – Sp. 11, Z.
43) hinaus.




                                                                             59/61

2.5    Die vorstehenden Ausführungen zur Patentfähigkeit der codiererseitigen Vorrichtung nach Anspruch 1 gelten in entsprechender Weise auch für den zugehörigen
codiererbezogenen Verfahrensanspruch 12 sowie die entsprechenden decodiererbezogenen Ansprüche 9 und 18.

Auch wenn die in den nebengeordneten Ansprüche 4, 15, 10 und 20 – im Vergleich
zu den Ansprüchen 1, 12, 9 und 18 – zusätzlich genannte gemeinsame Quantisierung der adaptiven und festen Verstärkungen bzw. deren Empfang als solche fachüblich ist (vgl. JELINEK, Sp. 15, Tab. 3), ergibt sich die Patentfähigkeit ihrer Gegenstände aus den übrigen Merkmalen, wie zum Anspruch 1 dargelegt.




                                          B.
                              Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                          C.
                              Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130) eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im
Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur


                                                                                  60/61

nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur
versehen sein, die von einer internationalen Organisation auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich zur Bearbeitung durch das
jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung
oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die
Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Voit             Müller              Werner           Matter             Tischler




                                                                              61/61
