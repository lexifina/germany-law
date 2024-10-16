---
ecli: "ECLI:DE:BPatG:2024:161024U4Ni8.23EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 8/23"
decided: "2024-10-16"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=19&nr=44426&anz=391&pos=299&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-10-16_4_Ni_8_23_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0095.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0269.md", "germany/bund/acts/zpo/0308.md", "germany/bund/acts/zpo/0319.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 8/23 vom 2024-10-16

## Entscheidung

BUNDESPATENTGERICHT
                          IM NAMEN DES VOLKES

                                    URTEIL

 4 Ni 8/23 (EP)
    verbunden mit
 4 Ni 10/23 (EP)
 (Aktenzeichen)


                          In der Patentnichtigkeitssache


…




                    betreffend das europäische Patent 2 352 145

                               (DE 60 2009 030 411)




ECLI:DE:BPatG:2024:161024U4Ni8.23EP.0

                                       -2-



hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 16. Oktober 2024 durch die Richterin Werner M. A. als Vorsitzende sowie die Richter Dipl.-Ing. Altvater, Dipl.-Ing Matter, Dipl.-Phys. Univ.
Dr. Haupt und die Richterin Berner


für Recht erkannt:


I.   Das europäische Patent 2 352 145 wird mit Wirkung für das Hoheitsgebiet der
     Bundesrepublik Deutschland teilweise für nichtig erklärt, soweit es über folgende Fassung hinausgeht:

-3-

                                         -4-




II.    Im Übrigen wird die Klage abgewiesen.



III.   Von den Gerichtskosten tragen die Klägerin zu 1 und die Beklagte je
       ein Viertel und die Klägerin zu 2 die Hälfte.

       Von den außergerichtlichen Kosten der Beklagten trägt die Klägerin
       zu 1 ein Viertel und die Beklagte ein Viertel selbst.

       Die außergerichtlichen Kosten der Klägerin zu 1 trägt die Beklagte zur
       Hälfte und die Klägerin zu 1 im Übrigen selbst.




IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils
       zu vollstreckenden Betrages vorläufig vollstreckbar.

                                             -5-




                                       Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 2 352 145 (Streitpatent), das
unter      Inanspruchnahme       der    Priorität   der   chinesischen   Voranmeldung
CN 200810247009          vom     29. Dezember 2008        am   29. Dezember 2009     als
PCT/CN2009/076194 angemeldet worden ist. Die Erteilung des europäischen Patents ist am 1. April 2015 veröffentlicht worden. Das in englischer Sprache gefasste
Streitpatent ist in Kraft.


Das Deutsche Patent- und Markenamt führt das Streitpatent unter dem Aktenzeichen 60 2009 030 411.9. Es trägt die Bezeichnung

    “TRANSIENT SPEECH SIGNAL ENCODING METHOD AND DEVICE,
        DECODING METHOD AND DEVICE, PROCESSING SYSTEM AND
                  COMPUTER-READABLE STORAGE MEDIUM”
                               in der deutschen Übersetzung
         „Verfahren und Vorrichtung zur Kodierung von Übergangssignalen,
        Dekodierungsverfahren und -vorrichtung, Verarbeitungssystem sowie
                         computerlesbares Speichermedium“.

Das Streitpatent umfasst in der erteilten Fassung 19 Patentansprüche, davon zwei
unabhängige Verfahrensansprüche 1 und 6, weiter zwei unabhängige Vorrichtungsansprüche 10 und 15, zwei nebengeordnete Systemansprüche 17 und 18 sowie den
nebengeordneten Anspruch 19, der auf ein computerlesbares Medium gerichtet ist.


Der das codiererseitige Verfahren betreffende Patentanspruch 1 lautet in der erteilten Fassung:

   1.      A transient signal encoding method for speech signals or audio signals,
           comprising:

             obtaining (11) a reference sub-frame where a maximal time envelope
             having a maximal amplitude value from time envelopes of all subframes of an input signal is located, wherein the input signal is a transient signal;

                                         -6-



          decreasing (13) an amplitude value of the time envelope of each subframe before the reference sub-frame in such a way that a first difference is greater than a preset first threshold, wherein the first difference
          is a difference between the amplitude value of the time envelope of
          each sub-frame before the reference sub-frame and the amplitude
          value of the maximal time envelope; and
          writing (15) the adjusted time envelope obtained by the decreasing
          step into an encoding bitstream.


Der die codiererseitige Vorrichtung betreffende Patentanspruch 10 lautet in der erteilten Fassung:

  10. A transient signal encoding device for speech signals or audio signals,
        comprising:

          a reference sub-frame obtaining module (71), configured to obtain a
          reference sub-frame where a maximal time envelope having a maximal amplitude value from time envelopes of all sub-frames of an input
          signal is located, wherein the input signal is a transient signal;
          a first amplitude value adjusting module (72), configured to decrease
          an amplitude value of the time envelope of each sub-frame before the
          reference sub-frame in such a way that a first difference is greater than
          a preset first threshold, wherein the first difference is a difference between the amplitude value of the time envelope of each sub-frame before the reference sub-frame and the amplitude value of the maximal
          time envelope; and a bitstream writing module (73), configured to write
          the adjusted time envelope output by the first amplitude value adjusting module into an encoding bitstream.


Der das decodiererseitige Verfahren betreffende Patentanspruch 6 lautet in der erteilten Fassung:

  6.    A transient signal decoding method for speech signals or audio signals,
        comprising:

          obtaining (41) a reference sub-frame where a maximal time envelope

                                         -7-



          having a maximal amplitude value from time envelopes of all subframes of a pre-obtained time-domain signal is located, the pre-obtained time-domain signal being a transient signal;
          decreasing (43) an amplitude value of the time envelope of each subframe before the reference sub-frame in such a way that a first difference is greater than a preset first threshold, wherein the first difference
          is a difference between the amplitude value of the time envelope of
          each sub-frame before the reference sub-frame and the amplitude
          value of the maximal time envelope; and
          modifying the pre-obtained time-domain signal according to the adjusted time envelope, so as to obtain a recovered transient signal.


Der die decodiererseitige Vorrichtung betreffende Patentanspruch 15 lautet in der
erteilten Fassung:

  15. A transient signal decoding device for speech signals or audio signals,
        comprising

          a reference sub-frame obtaining module (91), configured to obtain a
          reference sub-frame where a maximal time envelope having a maximal amplitude value from time envelopes of all sub-frames of a preobtained time-domain signal is located, the pre-obtained time-domain
          signal being a transient signal; a first amplitude value adjusting module
          (92), configured to decrease an amplitude value of the time envelope
          of each sub-frame before the reference sub-frame in such a way that
          a first difference is greater than a preset first threshold, wherein the
          first difference is a difference between the amplitude value of the time
          envelope of each sub-frame before the reference sub-frame and the
          amplitude value of the maximal time envelope; and
          a time-domain signal modification module (93), configured to modify
          the pre-obtained time-domain signal according to the adjusted time
          envelope output by the first amplitude value adjusting module, so as
          to obtain a recovered transient signal.


Die beiden nebengeordneten das System betreffenden Patentansprüche 17 und 18

                                         -8-



lauten in der erteilten Fassung:

  17. A transient signal processing system for speech signals or audio signals,
        comprising

           a transient signal encoding device according to any one of claims 10-
           14, and
           a transient signal decoding device, configured to modify a pre-obtained time-domain signal according to the time envelope in the encoding bitstream received from the transient signal encoding device,
           so as to obtain a recovered transient signal.

  18. A transient signal processing system for speech signals or audio signals,
        comprising:

           a transient signal encoding device, configured to write a time envelope
           of each sub-frame of a transient signal into an encoding bitstream; and
           a transient signal decoding device according to any one of claims 15 -
           16.


Der nebengeordnete, das computerlesbares Medium betreffende Patentanspruch
19 lautet in der erteilten Fassung:

  19. A computer readable storage medium, comprising a computer program
        which when run by a computer processor executes the steps according
        to any of the claims 1 to 9.


Die Patentansprüche 2 bis 5 sind unmittelbar oder mittelbar auf Patentanspruch 1,
die Patentansprüche 7 bis 9 unmittelbar oder mittelbar auf Patentanspruch 6, die
Patentansprüche 11 bis 14 unmittelbar oder mittelbar auf Patentanspruch 10 und
Patentanspruch 16 unmittelbar auf Patentanspruch 15 rückbezogen; wegen ihres
Wortlauts wird auf die Akte verwiesen.


Die Klägerin zu 1 hat das Streitpatent mit ihrer Nichtigkeitsklage vom 6. Februar
2023 zunächst beschränkt im Umfang der Patentansprüche 1 bis 4 und 10 bis 13
angegriffen und ihre Klage mit Schriftsatz vom 30. April 2024 erweitert auf den Gesamtangriff auf das Streitpatent.

                                        -9-



Die Klägerin zu 2 hat ihrer Klage vom 20. Februar 2023, mit der sie das Streitpatent
vollumfänglich angegriffen hat, mit Schriftsatz vom 16. September 2024 zurückgenommen.


Die Klägerin zu 1 ist der Ansicht, der Gegenstand gemäß den Patentansprüchen 1
und 10 bzw. 6 und 15 sei wegen des Nichtigkeitsgrunds der unzulässigen Erweiterung gegenüber den ursprünglich eingereichten Unterlagen und der mangelnden
Patentfähigkeit für nichtig zu erklären. Der Gegenstand des Streitpatents sei darüber hinaus nicht so deutlich und vollständig offenbart, dass eine Fachperson ihn
ausführen könne.

Dabei stützt die Klägerin zu 1 ihr Vorbringen auf folgende Dokumente, wobei sie
sich den Vortrag der Klägerin zu 2 und den Vortrag der Klägerin in dem durch Klagerücknahme erledigten Verfahren 4 Ni 79/22 (EP) zu eigen macht:

    AMR (HLNK13)                   ETSI TS 126 090 V7.0.0 (2007-06). Technical
                                   specification. AMR speech Codec; Transcoding
                                   Functions, 57 Seiten
    BOSI (NK5)                     BOSI, M.; GOLDBERG, R. E.: Introduction to
                                   Digital Audio Coding and Standards, Springer,
                                   2003, Seiten v – xxii, 1 – 12, 371 – 382
    CHAKRAVARTHY (NK1/MFG10)            US 2004/0196913 A1
    DAUDET (HLNK11)                Daudet, L.: A review on techniques for the extraction of transients in musical signals, aus dem
                                   Konferenzbericht Computer Music Modeling and
                                   Retrieval CMMR 2005, veröffentlicht im Jahr
                                   2006, Seiten 1 – 15
    DUXBURY (HLNK11b)              Duxbery, Ch. et. al.: Separation of transient information in musical audio using multiresolution
                                   analysis techniques; Proceedings of the COST
                                   G-6 Conference on Digital Audio Effects (DAFX-01), Limerick, Irland, 6.-8. Dezember 2001,
                                   Seiten DAFX-1 bis DAFX-4
    G.723.1 (HLNK14)               ITU-T: G.723.1 (03/96) Dual Rate Speech Coder
                                   for Multimedia Communications Transmitting at

                              - 10 -



                          5.3 and 6.3 kbit/s, 31 Seiten
G.729.1 (MFG17)           ITU-T: G.729.1 Amendment 4 (06/2008); G.729-
                          based embedded variable bit-rate coder: An 8-
                          32 kbit/s scalable wideband coder bitstream interoperable with G.729 Amendment 4: New Annex C (DTX/CNG scheme) plus corrections to
                          main body and Annex B, 128 Seiten
GEISER (MFG12)            Geiser, B. et al.: Bandwidth Extension for Hierarchical Speech and Audio Coding in ITU-T Rec.
                          G.729.1, IEEE Transactions On Audio, Speech,
                          And Language Processing, Vol. 15, No. 8. November 2007, Seiten 2496 – 2509
JELINEK (MFG16)           WO 03/102921 A1
KÖVESI I (NK2/MFG9/HLNK7)        Kövesi, B. et. al.: Pre-echo Reduction in
                          the ITU-T G.729.1 Embedded Coder, 16th European    Signal   Processing     Conference   (EU-SIPCO), Lausanne, Schweiz, 25.-29. August
                          2008, 5 Seiten
KÖVESI II (NK6/MFG5)      WO 2007/096552 A2
KÖVESI II_E (NK6a/MFG5a) US 2009/0313009 A1 (englischsprachiges Familienmitglied von KÖVESI II)
MAHIEUX                   MAHIEUX, Y.: High quality audio transform coding at 64 kbit/s. In: Ann. Télécommun., 47, n° 3-
                          4, 1992, Seiten 95 - 106
MICHAELIS (NK3/MFG6/HLNK12) US 6,889,186 B1
RAGOT (MFG13)             Ragot, S. et al.: ITU-T G.729.1: An 8-32 kbit/s
                          Scalable Coder Interoperable with G.729 for
                          Wideband Telephony and Voice Over IP, 2007
                          IEEE International Conference on Acoustics,
                          Speech and Signal Processing - ICASSP '07,
                          Honolulu, HI, USA, 2007, Seiten IV-529 - IV-532
SIEMENS (MFG15)           US 2007/0282604 A1
SONY (NK4/MFG7)           JP 2008 209 646 A
SONY_E (NK4a)             Übersetzung der NK4 in die englische Sprache

                                       - 11 -



    SPANIAS (HLNK6)               Spanias, A. et. al.: Audio Signal Processing and
                                  Coding, Wiley-Interscience publication, Copyright 2007, ISBN: 978-0-471-79147-8, Kapitel 6
                                  und 10, veröffentlicht im Jahr 2007
    VAFIN (MFG14)                 VAFIN, R. et. al.: Modifying transients for efficient coding of audio. 2001 IEEE International
                                  Conference on Acoustics, Speech, and Signal
                                  Processing.       Proceedings        (Cat.   No.
                                  01CH37221). Vol. 5. IEEE, 2001, 4 Seiten
    ZHANG I (HLNK10)              Zhang, T. et. al.: On the      Pre-echo Control
                                  Method in Transient Signal Coding of AVS audio,
                                  ICALIP2008, 2008, Seiten 242 - 246
    ZHANG II (MFG8)               CN 101308655 A
    ZHANG II_E (MFG8a)            US 2010/0121648 A1 (englischsprachiges Familienmitglied von ZHANG II)


Die Klägerin zu 1 beantragt,

      das europäische Patent 2 352 145 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,

      die Klage (der Klägerin zu 1) abzuweisen,

hilfsweise, die Klage (der Klägerin zu 1) abzuweisen,

        soweit sie sich gegen das Streitpatent im Umfang der Ansprüche
        1 bis 5, 10 bis 14 und 17 (Ansprüche mit Codiererbezug) richtet

        mit der Maßgabe, dass die Ansprüche als geschlossener Anspruchssatz gestellt werden,

weiter hilfsweise, die Klage (der Klägerin zu 1) abzuweisen,

        soweit sie sich auch gegen eine der Fassungen des Streitpatents

                                          - 12 -



        nach den mit den Schriftsätzen vom 25. Juli 2023 und 24. November 2023 (jeweils vorgelegt im Verfahren mit dem
        Az.: 4 Ni 10/23 (EP)) eingereichten Hilfsanträgen

        0a, 0aa, 0aa1, 0aa2, 0aa3, 0b, 0c, 0d, 0da, 0da1, 0da2, 0da3,
        0e, 0f, 1a, 2a, 3a, 4a, 5a, 6a richtet,

        mit der Maßgabe, dass die Hilfsanträge in dieser angegebenen
        Reihenfolge geprüft werden sollen und jeweils als geschlossener
        Anspruchssatz gestellt werden,

weiter höchst hilfsweise, die Klage (der Klägerin zu 1) abzuweisen,

        soweit sie sich auch gegen eine der Fassungen des Streitpatents
        nach den mit den Schriftsätzen vom 25. Juli 2023 und 24. November 2023 (jeweils vorgelegt im Verfahren mit dem Az.: 4 Ni
        10/23 (EP)) eingereichten Hilfsanträgen

        0a, 0aa, 0aa1, 0aa2, 0aa3, 0b, 0c, 0d, 0da, 0da1, 0da2, 0da3,
        0e, 0f, 1a, 2a, 3a, 4a, 5a, 6a richtet,

        mit der Maßgabe, dass

        die Hilfsanträge nur die angegriffenen Ansprüche 1 bis 5, 10 bis
        14 und 17 enthalten sollen (d. h. ohne die Ansprüche 6 bis 9, 15
        bis 16 und 18 bis 19 gestellt werden),

        die Hilfsanträge in dieser angegebenen Reihenfolge geprüft werden sollen

        und jeweils insoweit als geschlossener Anspruchssatz gestellt
        werden.


Wegen des Wortlauts des als ersten gestellten (unbenannten) Hilfsantrags wird auf
den Urteilstenor Bezug genommen. Wegen des Wortlauts der Ansprüche nach den
weiteren Hilfsanträgen wird auf die Akte verwiesen.


Die Beklagte tritt der Argumentation der Klägerin zu 1 entgegen und ist der Auffassung, der Gegenstand des Streitpatents beruhe in zulässiger Weise auf den ursprünglich eingereichten Unterlagen, sei ausführbar offenbart, gegenüber dem

                                        - 13 -



Stand der Technik neu und beruhe auch auf einer erfinderischen Tätigkeit. Der Gegenstand des Streitpatents sei wenigstens in einer der verteidigten Fassungen nach
den eingereichten Hilfsanträgen schutzfähig.


Die Klägerin zu 1 tritt auch den Hilfsanträgen entgegen und sieht auch die Gegenstände der Patentansprüche 1 und 10 bzw. 6 und 15 in der Fassung der jeweiligen
Hilfsanträge als unzulässig erweitert und nicht patentfähig an, insbesondere auch
mit den jeweils ergänzten Merkmalen nicht als neu und nicht erfinderisch.


Der Senat hat den Parteien einen Hinweis vom 14. März 2024 zugeleitet und hierin
Fristen zur Stellungnahme gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, das Protokoll der mündlichen Verhandlung vom 16. Oktober 2024 sowie den weiteren Akteninhalt Bezug
genommen.




                          Entscheidungsgründe


                                         A.


Die zulässige Klage der Klägerin zu 1 hat in der Sache nur teilweise Erfolg, und zwar
hinsichtlich der erteilten Fassung des Streitpatents. Denn insoweit ist jedenfalls der
Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 Int-PatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54, 56 EPÜ gegeben.


In der Fassung nach dem als ersten gestellten (unbenannten) Hilfsantrag erweist
sich das Streitpatent hingegen als schutzfähig, so dass die Klage, soweit sie sich
auch gegen diese Fassung richtet, abzuweisen ist. Auf die Frage, ob das Streitpatent auch in der Fassung nach den weiteren Hilfsanträgen Bestand hätte, kommt es
bei dieser Sachlage nicht mehr an.

                                        - 14 -



I.   Gegenstand des Streitpatents (in erteilter Fassung), Aufgabe, Fachperson und Auslegung


1.     Das Streitpatent bezieht sich auf Verfahren und Vorrichtungen zum Codieren
und Decodieren eines transienten Audiosignals (Streitpatentschrift; Abs. 0001, nebengeordnete Ansprüche 1, 6, 10, 15, 17, 18).

Laut Streitpatent kann die akustische Qualität übertragener Sprachsignale durch
eine Erhöhung der Bandbreite verbessert werden. Aktuelle Audio-Codecs verwenden für das niedrige Frequenzband eines Sprachsignals herkömmliche Codier- und
Decodieralgorithmen wohingegen sie eine Bandbreitenerweiterungstechnologie
nutzen, um Informationen über das hohe Frequenzband mit einer geringen Anzahl
von Bits zu codieren und so die zu übertragende Datenmenge zu verringern (Streitpatentschrift, Abs. 0002 - 0004).

Der Artikel „Pre-Echo Reduction in the ITU-T G.729.1 coder“ (hier im Verfahren als
KÖVESI I geführt) stellt laut Streitpatent eine neue Methode vor, um das durch die
Transformationscodierung mit niedrigen Bitraten entstehende Vor-Echo-Artefakt
(pre-echo artefact) zu adressieren. In dem Artikel (KÖVESI I) werde angenommen,
dass das Eingangssignal zunächst im Zeit- und dann im Transformationsbereich
codiert wird. Die erste Stufe rekonstruiere ein in der Regel vorechofreies Signal.
Daher könne die Transformationscodierung dieses rekonstruierte Signal als Nebeninformation zur Vorecho-Erkennung und -Reduzierung nutzen. Das Verfahren
werde als adaptiver Begrenzer auf der Decodiererseite implementiert und benötige
keine Übertragung von Hilfsdaten. Es ist laut Streitpatent Teil des standardisierten
ITU-T G.729.1-Codierers, wo es in zwei getrennten Teilbändern verwendet werde.
Experimentelle Testergebnisse zeigten, dass dieses Verfahren bei sehr geringer
Komplexität einen signifikanten Einfluss auf die Qualität im Standard G.729.1 habe
(Abs. 0006).

Laut Streitpatent hat sich jedoch herausgestellt, dass sich ein transientes von einem
nicht-transienten Signal u. a. dadurch unterscheidet, dass im Zeitbereich die Signalenergie des transienten Signals eine große momentane Änderung aufweist,
während sein Frequenzspektrum glatt (smooth) ist. Im Stand der Technik werde die

                                       - 15 -



zeitliche Hüllkurve des transienten Signals nicht modifiziert. Aufgrund des Einflusses der Verarbeitung in dem Signalcodierprozess, wie z. B. durch rahmenweise
Verarbeitung, Zeit-Frequenz-Transformation und Bildung von Frequenzhüllkurven,
erzeuge das transiente Signal regelmäßig ein Vor-Echo. Daher habe der Stand der
Technik den Nachteil, dass die Wirkung des im Decodierer wiederhergestellten transienten Signals nicht zufriedenstellend sei (Abs. 0007).



2.     Zwar nennt das Streitpatent explizit keine Aufgabe, jedoch sei es auf Verfahren, Vorrichtungen und Verarbeitungssysteme zum Codieren und Decodieren von
Audiosignalen gerichtet, die die Qualität der Wiederherstellung von transienten Signalen verbesserten (Abs. 0008). Somit liegt die Aufgabe in der Verbesserung der
Qualität von im Decodierer wiederhergestellten transienten Signalen.



3.     Die maßgebliche Fachperson hat einen universitären Abschluss (Diplom oder Master) im Bereich der Nachrichten- oder Informationstechnik, verfügt über eine
mehrjährige Berufserfahrung auf dem Gebiet der Sprach- und Audiocodecs, verfolgt
die Sitzungen der einschlägigen Normierungs- und Standardisierungsgremien und
kennt die dort diskutieren Entwicklungsvorschläge.



4.     Die Aufgabe soll unter anderem mit einem Verfahren zur Codierung nach
Patentanspruch 1 bzw. einem Verfahren zur Decodierung nach Patentanspruch 6
gelöst werden.

Die Patentansprüche 1 und 6 lassen sich in der erteilten Fassung in der Verfahrenssprache Englisch sowie in deutscher Übersetzung (beides gemäß Streitpatentschrift) wie folgt gliedern:

Anspruch 1 (Verfahren zur Codierung):
 0    A transient signal encoding method Verfahren zur Codierung von transienfor speech signals or audio signals, ten Signalen für Sprachsignale oder
      comprising:                           Audiosignale, umfassend:

                                        - 16 -



1    obtaining (11) a reference sub- Erfassen (11) eines Referenz-Subfraframe                                   mes,

1.1 where a maximal time envelope bei dem sich eine maximale zeitliche
     having a maximal amplitude value Einhüllende mit einem maximalen
     from time envelopes of all sub- Amplitudenwert von zeitlichen Einhülframes of an input signal is located, lenden aller Subrahmen eines Eingangssignals befindet,

1.2 wherein the input signal is a transi- wobei das Eingangssignal ein tranent signal;                             sientes Signal ist;

2    decreasing (13) an amplitude value Verringern (13) eines Amplitudenwerts
     of the time envelope                    der zeitlichen Einhüllenden

2.1 of each sub-frame before the refer- von jedem Subrahmen vor dem Refeence sub-frame                          renz-Subrahmen

2.2 in such a way that a first difference in einer Weise, dass eine erste Diffeis greater than a preset first thresh- renz größer als eine vorbestimmte
     old, wherein the first difference is a erste Schwelle ist, wobei die erste Difdifference between the amplitude ferenz eine Differenz zwischen dem
     value of the time envelope of each Amplitudenwert der zeitlichen Einhülsub-frame before the reference lenden von jedem Subrahmen vor dem
     sub-frame and the amplitude value Referenz-Subrahmen              und     dem
     of the maximal time envelope; and       Amplitudenwert der maximalen zeitlichen Einhüllenden ist; und

3    writing (15) the adjusted time enve- Schreiben (15) der durch den Verrinlope obtained by the decreasing gerungsschritt erhaltenen angepassstep into an encoding bitstream.        ten zeitlichen Einhüllenden in einen
                                             codierenden Bitstrom.

                                        - 17 -



Anspruch 6 (Verfahren zur Decodierung):

0‘    A transient signal decoding method Verfahren zur Dekodierung von tranfor speech signals or audio signals, sienten Signalen für Sprachsignale ocomprising:                                der Audiosignale, umfassend:

1‘    obtaining (41) a reference sub- Erfassen (41) eines Referenz-Subfraframe                                      mes,

1.1‘ where a maximal time envelope bei dem sich eine maximale zeitliche
      having a maximal amplitude value Einhüllende mit einem maximalen
      from time envelopes of all sub- Amplitudenwert von zeitlichen Einhülframes of a pre-obtained time-do- lenden aller Subrahmen eines vorher
      main signal is located,                    erfassten Zeitbereichssignals befindet,

1.2’ the pre-obtained time-domain sig- wobei das vorher erfasste Zeitbenal being a transient signal;              reichssignal ein transientes Signal ist;

2’    decreasing (43) an amplitude value Verringern (43) eines Amplitudenof the time envelope                       werts der zeitlichen Einhüllenden

2.1   of each sub-frame before the refer- von jedem Subrahmen vor dem Refeence sub-frame                             renz-Subrahmen

2.2   in such a way that a first difference in einer Weise, dass eine erste Diffeis greater than a preset first thresh- renz größer als eine vorbestimmte
      old, wherein the first difference is a erste Schwelle ist, wobei die erste Difdifference between the amplitude ferenz eine Differenz zwischen dem
      value of the time envelope of each Amplitudenwert der zeitlichen Einhülsub-frame before the reference lenden von jedem Subrahmen vor
      sub-frame and the amplitude value dem Referenz-Subrahmen und dem
      of the maximal time envelope; and          Amplitudenwert der maximalen zeitlichen Einhüllenden ist; und

                                                - 18 -



 3’      modifying the pre-obtained time- Verändern des vorher erfassten Zeitdomain signal according to the ad- bereichssignals gemäß der angepassjusted time envelope, so as to ob- ten zeitlichen Einhüllenden, um ein
         tain a recovered transient signal.              wiederhergestelltes transientes Signal
                                                         zu erhalten.




5.       Der Gegenstand des Streitpatents bedarf der Erläuterung.

5.1 Wie einleitend dargelegt, geht das Streitpatent von einem sogenannten Transformationscodierer aus, der transiente Eingangssignale vom Zeit- in den Frequenzbereich transformiert und anschließend codiert. Wenn das Eingangssignal eines
solchen Transformationscodierers einen transienten Signalabschnitt umfasst, weist
das vom Decodierer wiederhergestellte Audiosignal regelmäßig ein durch einen
menschlichen Nutzer wahrnehmbares und damit störendes Vor-Echo auf.

Ursache des Vor-Echos ist das durch den großen Dynamikbereich transienter Signale hervorgerufene und nicht ausreichend maskierte Quantisierungsrauschen vor
dem Signalanstieg, was der Fachperson bereits Jahrzehnte vor dem Prioritätstag
des Streitpatents bekannt war:




      MAHIEUX (1992), S. 104, Fig. 6a (Original signal), 6b (Reconstructed signal, before postfiltering) mit zusätzlicher Beschriftung und Markierung durch den Senat


Der Vor-Echo-Effekt tritt auch dann auf, wenn die Transformationscodierung nur für
einen Teil des zu codierenden Frequenzbandes, typischerweise den oberen, vorge-

                                          - 19 -



nommen und/oder wenn eine zweistufige Codierung, erst im Zeit- und dann im Frequenzbereich, durchgeführt wird (Streitpatentschrift, Abs. 0006: CELP + transform
embedded coding; KÖVESI I, Fig. 2 und 5; SIEMENS, Ansprüche 16 bis 23).


5.2 In einem Ausführungsbeispiel des Streitpatents wird das Eingangssignal des
Codierers (Input signal) in einen niedrigen und einen hohen Frequenzbereich geteilt
(Decompose the signal 21), wobei nur im oberen Frequenzbereich eine Transformationscodierung (Perform time-frequency transform 211, Calculate the frequency
envelope 213, Quantify the frequency envelope 215) durchgeführt wird, die bei transienten Signalen ein Vor-Echo erzeugt (Streitpatentschrift, Abs. 0060 – 0065 und
Fig. 2):




    Streitpatentschrift, Fig. 2 mit Kommentierung und Kolorierung durch den Senat


Um im Decodierer eine Reduzierung des Vor-Echos im hochfrequenten Bereich zu
ermöglichen, wird im Codierer bestimmt, ob der hochfrequente Anteil des Eingangssignals ein transientes Signal ist (Determine the signal type of the input signal 25).
In Abhängigkeit davon wird eine zuvor berechnete zeitliche Einhüllende des hochfrequenten Signalanteils (Calculate the time envelope 26) streitpatentgemäß modifiziert (Transient signal; Modify the time envelope 27) oder nicht (Non-transient signal) und anschließend in jedem Fall quantisiert (Quantify the time envelope 29). Von

                                        - 20 -



dem niederfrequenten Anteil des Eingangssignals werden, wie dies bei Zeitbereichscodierern wie CELP (Code Excited Linear Prediction) üblich ist, Codierungsparameter, die kein Vor-Echo enthalten, bestimmt (Input parameters of the low-frequency band signal 23) und in den zum Decodierer zu übertragenden Bitstrom eingeschrieben (Code stream 217).

Der vom Codierer erzeugte Bitstrom umfasst somit die den niederfrequenten Signalanteil charakterisierenden Parameter (23), Informationen über die – bei einem
transienten Signal modifizierten – zeitlichen Einhüllenden des hochfrequenten Signalanteils (29), eine Information über den Signaltyp (transient oder nicht) des hochfrequenten Signalanteils (25) sowie Informationen über die spektralen Einhüllenden
des hochfrequenten Signalanteils (215).

Beim Decodierer kann aus diesen Informationen ein breitbandiges Audiosignal rekonstruiert werden, wobei – falls der hochfrequente Anteil des codierten Signals
einen transienten Signalcharakter hat und daher im Transformationscodierer ein
Vor-Echo erzeugt wurde – mittels der modifizierten zeitlichen Einhüllenden des
hochfrequenten Signalanteils eine Reduzierung dieses Vor-Echos möglich ist.


5.3 In einem weiteren Ausführungsbeispiel ist beschrieben, dass ein Decodierer
einen Bitstrom empfängt, der – falls ein transientes Signal codiert wurde – im hochfrequenten Signalanteil ein Vor-Echo enthält (Fig. 5 mit Beschreibung). Bei der Rekonstruktion des breitbandigen Audiosignals werden – bei einem transienten Signal
– die zeitlichen Einhüllenden des hochfrequenten Signalanteils streitpatentgemäß
modifiziert (Modify the time envelope 52):

                                         - 21 -




      Streitpatentschrift, Fig. 5 mit Kommentierung und Kolorierung durch den Senat


5.4 Auch nach den Angaben in den Absätzen 0070 und 0153 bis 0163 der Streitpatentschrift kann ein erfindungsgemäßes Verarbeitungssystem für ein transientes
Signal entweder im Codierer ein Verfahren nach Anspruch 1 oder im Decodierer ein
Verfahren nach Anspruch 6 durchführen, wie es sich in den nebengeordneten Ansprüchen 17 (Signalverarbeitungssystem mit einer Vorrichtung zur Codierung nach
einem der Ansprüche 10 bis 14) und 18 (Signalverarbeitungssystem mit einer Vorrichtung zur Decodierung nach einem der Ansprüche 15 oder 16) widerspiegelt.

Eine Implementierung oder gleichzeitige Verwendung der streitpatentgemäßen Verfahren im Codierer und Decodierer einer Übertragungsstrecke erwähnt das Streitpatent zwar nicht, jedoch nutzt die decodiererseitige Implementierung eine Information über den Signaltyp (transient oder nicht-transient), die im Codierer als Teil der

                                        - 22 -



codiererseitigen Implementierung gewonnen und an den Decodierer übertragen
worden sein kann (Abs. 0069, 0078, 0081 bis 0084, 0110, 0111).


5.5    Die Ansprüche 1 und 6 sind auf ein Verfahren zur Codierung bzw. Decodierung von transienten Sprach- oder Audiosignalen gerichtet (Merkmale 0, 0‘). Der
Fachperson ist bekannt, dass Sprachsignale eine echte Teilmenge der Audiosignale bilden, daher versteht sie das Teilmerkmal „für Sprachsignale oder Audiosignale“ als „für Audiosignale, insbesondere Sprachsignale“.


5.6    Unter einem transienten Signal (transient signal; Merkmale 1.2, 1.2‘) versteht
die Fachperson für Audio-Codecs ein in der englischen Sprache auch als „attack“
oder „onset“ bezeichnetes Signal, dessen Amplitude und damit Energie sich in kurzer Zeit deutlich ändert, insbesondere erhöht und danach gegebenenfalls wieder
abfällt (Streitpatentschrift, Abs. 0007; CHAKRAVARTY, Abs. 0010; G.729.1, S. 54,
Kap. 7.3.10, Abs. 1). Das Frequenzspektrum eines transienten Signalabschnitts ist
vergleichsweise „glatt“ (Streitpatentschrift, Abs. 0007), da die Fouriertransformierte
eines idealen Einheitspulses, d. h. einer Delta-Distribution („Delta-Funktion“), die
„Einsfunktion“ ist.


5.7    Damit das beanspruchte Codier- bzw. Decodierverfahren nur auf transiente
Signale (Merkmale 0, 1.2 bzw. 0‘, 1.2‘) angewendet wird, beschreibt das Streitpatent
beispielhaft, wie codiererseitig jeweils für einen bestimmten Zeitabschnitt (long
frame, 15 ms) des Eingangssignals ermittelt wird, ob ein transientes oder ein nichttransientes Signal vorliegt (Abs. 0030 bis 0042, 0133 bis 0140; Ansprüche 4, 5, 13,
14). Der decodiererseitige Anspruch 6 schließt nicht aus, dass alternativ oder zusätzlich zu dieser codiererseitigen Signaltypbestimmung, deren Ergebnis gegebenenfalls an den Decodierer übertragen wird (Ansprüche 4, 13), im Decodierer festgestellt wird, ob das vorher erfasste Zeitbereichssignal ein transientes Signal ist
(vgl. Merkmal 1.2‘).


5.8    Das Eingangssignal des Codierers (input signal; Anspruch 1, Merkmal 1.1)
und das vorher erfasste Zeitbereichssignal des Decodierers (pre-obtained time domain signal; Anspruch 6, Merkmal 1.1‘) umfassen mehrere Subrahmen. Wie dargelegt, ist es der Fachperson bekannt, dass transiente Signale regelmäßig nur sehr

                                                 - 23 -



kurz andauern und dass die Bestimmung, ob ein transientes oder ein nicht-transientes Signal vorliegt, für Zeitabschnitte bestimmter Länge durchgeführt wird. Der
Fachperson ist es weiter bekannt, dass die Signalverarbeitung in Audio-Codecs typischerweise für aufeinanderfolgende Rahmen (frames) von einigen Millisekunden
Länge durchgeführt wird, wobei einige Verarbeitungsschritte kürzere Zeitabschnitte,
sogenannte Subrahmen, und andere Verarbeitungsschritte längere Abschnitte, wie
long frames oder superframes, verwenden (Streitpatentschrift, Abs. 0036; G.729.1,
S. 10, Tabelle 4).

Jedenfalls impliziert die Verwendung des Begriffs „Subrahmen“ in den unabhängigen Ansprüchen 1 und 6, dass es auch zeitlich längere „Rahmen“ gibt.


5.9   Auch, wenn im Anspruch 1 – anders als im Anspruch 6 – nicht explizit angegeben ist, dass das Eingangssignal im Zeitbereich vorliegt, so entnimmt die Fachperson dies aus der subrahmenbasierten Signalverarbeitung gemäß den Merkmalsgruppen 1 und 2 sowie aus der Bestimmung der im Anspruch 1 genannten „zeitlichen Einhüllenden“ (time envelopes) für jeden Subrahmen des (betrachteten Zeitabschnitts) des Eingangssignals.


5.10 Für jeden Subrahmen des Eingangssignals (Anspruch 1) bzw. des zuvor erfassten Zeitbereichssignals (Anspruch 6) wird ein Amplitudenwert einer zeitlichen
Einhüllenden bestimmt, der eine Information über die Amplituden der mehreren Abtastwerte des Subrahmens darstellt. Hierzu werden die Amplituden der im Zeitbereich vorliegenden Abtastwerte des Signals im betrachteten Subrahmen geeignet
verarbeitet, z. B. durch eine Mittelwertbildung, eine Spitzenwertbestimmung oder –
gemäß dem Ausführungsbeispiel – durch die Bestimmung einer durchschnittlichen
Energie des abgetasteten Signals. Aus den Absätzen 0033 bis 0036 der Streitpatentschrift entnimmt die Fachperson, dass sich die durchschnittliche Energie des i-ten
Subrahmens, der L Abtastwerte x[j] (j = 1, …, L) umfasst, berechnet zu:

                                             1        ∑𝐿𝐿𝑗𝑗=1(𝑥𝑥[𝑗𝑗] ∗ 𝑥𝑥[𝑗𝑗])
                     𝑠𝑠𝑠𝑠𝑠𝑠_𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔[𝑖𝑖] =     log10 �                         �
                                             2                   𝐿𝐿


5.11 Nach der Bestimmung der zeitlichen Einhüllenden „aller“ Subrahmen (Merkmal 1.1 bzw. 1.1‘), also eines Amplitudenwerts je Subrahmen für die Subrahmen

                                         - 24 -



des betrachteten Zeitabschnitts (z. B. für die 12 aufeinanderfolgenden Subrahmen,
die zusammen einen „langen Rahmen“ bilden), wird der maximale Amplitudenwert
(maximal amplitude value) der zeitlichen Einhüllenden ermittelt. Der zugehörige
Subrahmen, der die „maximale zeitliche Einhüllende“ (maximal time envelope) mit
dem maximalen Amplitudenwert aufweist, ist der „Referenz-Subrahmen“ des betrachteten Zeitabschnitts (Merkmal 1 bzw. 1‘). Im Referenz-Subrahmen befindet
sich somit gewissermaßen die „Spitze“ des transienten Signals.


5.12 Um den transienten Signalcharakter zu verstärken bzw. zu „schärfen“, werden gemäß den Merkmalsgruppen 2 (für die Codierung) bzw. 2‘ (für die Decodierung) die Amplitudenwerte der zeitlichen Einhüllenden der zeitlich vor dem Referenz-Subrahmen liegenden Subrahmen verringert. Umfasst der betrachtete Zeitabschnitt beispielsweise zwölf Subrahmen und ist der achte Subrahmen der Referenz-Subrahmen, so werden die Amplitudenwerte der sieben vorhergehenden Subrahmen reduziert.

In einer Weiterbildung können zudem die Amplitudenwerte der dem Referenz-Subrahmen folgenden Subrahmen verringert (Anspruch 2) und der Amplitudenwert des
Referenz-Subrahmens erhöht (Anspruch 3) werden.


5.13 Die Merkmale 2.2 bzw. 2.2‘ konkretisieren die Reduzierung der Amplitudenwerte. Hierzu wird u. a. ein voreingestellter erster Schwellenwert (preset first
threshold) verwendet. Der Fachperson ist vor dem Hintergrund der technischen
Lehre des Streitpatents bewusst, dass die Ermittlung dieses Schwellenwerts nicht
notwendigerweise fest vorgegeben sein muss, sondern vielmehr für den betrachteten Signalabschnitt, z. B. für einen zwölf Subrahmen umfassenden langen Rahmen,
in Abhängigkeit von den ermittelten Amplitudenwerten bestimmt werden kann und
insofern für die nachfolgende Reduzierung gemäß den Merkmalsgruppen 2 bzw. 2‘
für den betrachteten Zeitabschnitt „voreingestellt“ ist.

Der Absatz 0050 erläutert hierzu, was der Fachperson auch ohne diese explizite
Angabe unmittelbar verständlich wäre, nämlich, dass bei einer schon bestehenden
großen Differenz zwischen den Amplitudenwerten der vor dem Referenz-Subrahmen liegenden Subrahmen und dem Amplitudenwert des Referenz-Subrahmens

                                       - 25 -



nur eine geringe Reduzierung der Amplitudenwerte der vor dem Referenz-Subrahmen liegenden Subrahmen erforderlich ist, wohingegen bei einer geringen Differenz
eine stärkere Reduzierung nötig ist, um eine ausreichende Verstärkung bzw.
„Schärfung“ des transienten Signalcharakters zu erzielen.


5.14 In Absatz 0018 der Streitpatentschrift ist im Rahmen eines Ausführungsbeispiels angegeben, dass zur Berechnung des voreingestellten ersten Schwellenwerts die im betrachteten Zeitabschnitt vorliegenden Amplitudenwerte der zeitlichen
Einhüllenden der Subrahmen vor dem Referenz-Subrahmen auf 1/8 bis 1/2 ihres
ursprünglichen Wertes reduziert werden und danach „eine“ Differenz zwischen
„den“ angepassten Amplitudenwerten der zeitlichen Einhüllenden der Subrahmen
und dem Amplitudenwert der zeitlichen Einhüllenden des Referenz-Subrahmens
gebildet wird und diese „eine“ Differenz als erster voreingestellter Schwellenwert
verwendet wird.

Die Fachperson erkennt, dass sich die Angaben „eine“ und „die“ Differenz im Absatz
0018 offensichtlich auf die Festlegung des ersten voreingestellten Schwellenwertes
bezieht, da es regelmäßig mehr als einen Subrahmen vor dem Referenz-Subrahmen und somit mehrere unterschiedliche Differenzen für die Amplitude der jeweiligen Subrahmen gegenüber dem Referenz-Subrahmen geben wird. Da in Merkmal
2.2 weiter angegeben ist, dass die – nicht mit der ersten Differenz zur Bestimmung
des ersten Schwellenwerts gemäß Absatz 0018 gleichzusetzende – „erste“ Differenz zwischen „dem“ Amplitudenwert der zeitlichen Einhüllende jedes Subrahmens
vor dem Referenz-Subrahmen und dem Amplitudenwert des Referenz-Subrahmens
größer als der voreingestellte erste Schwellenwert sein muss, versteht die Fachperson die Angaben in Absatz 0018 so, dass es sich bei der dort genannten „einen“
Differenz um den Minimalwert der möglichen Differenzen handelt, der sich durch
Subtraktion des größten reduzierten Amplitudenwerts unter den mehreren reduzierten Amplitudenwerten von dem Amplitudenwert des Referenz-Subrahmens ergibt.
Gestützt wird dieses Verständnis auch dadurch, dass zur Beurteilung der Verstärkung bzw. „Schärfung“ der Signalcharakteristik bestimmt werden muss, wie weit der
Amplitudenwert des transienten Signals im Referenz-Subrahmen gegenüber den
betrachteten vorausgehenden Subrahmen – d. h. den Amplitudenwerten des vorausgehenden Signalverlaufs – abgegrenzt bzw. hervorgehoben ist.

                                                           - 26 -




Mit diesem Verständnis ergibt sich für den ersten voreingestellten Schwellenwert S1
und den Größen

    •    𝐷𝐷𝑖𝑖𝑆𝑆 : mögliche Differenzen zur Bestimmung des voreingestellten ersten
         Schwellenwerts,
    •    Aref: Amplitude der zeitlichen Einhüllenden des Referenz-Subrahmens,
    •    Ai: ursprüngliche Amplitudenwerte im i-ten Subrahmen;
    •    𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 : multiplikativer Faktor zur Reduzierung der ursprünglichen Amplitudenwerte Ai zur Berechnung des ersten Schwellenwerts;
    •    Ai,red,S: durch Multiplikation der ursprünglichen Amplitudenwerte Ai mit dem
         Faktor 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 < 1 erzeugte reduzierte Amplitudenwerte der zeitlichen Einhüllenden der Subrahmen vor dem Referenz-Subrahmen:
                                               𝐴𝐴𝑖𝑖,𝑟𝑟𝑟𝑟𝑟𝑟,𝑆𝑆 = 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 ∗ 𝐴𝐴𝑖𝑖
                                                   1              1
                                                     ≤ 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 ≤
                                                   8              2
  𝑆𝑆1 = min 𝐷𝐷𝑖𝑖𝑆𝑆 = min�𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝐴𝐴𝑖𝑖,𝑟𝑟𝑟𝑟𝑟𝑟,𝑆𝑆 � = min(𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 ∗ 𝐴𝐴𝑖𝑖 ) = 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 𝐴𝐴𝑚𝑚𝑚𝑚𝑚𝑚
           𝑖𝑖             𝑖𝑖                                  𝑖𝑖


Damit die in Merkmal 2.2 genannte „eine erste Differenz“ (a first difference) D1 für
alle reduzierten Amplitudenwerte Ai,red (amplitude value of the time envelope of each
subframe) größer als der erste voreingestellte Schwellenwert S1 ist, muss die streitpatentgemäße Reduzierung der Amplitudenwerte (Merkmalsgruppe 2 bzw. 2‘) mit
einem Faktor 𝑟𝑟𝑟𝑟𝑟𝑟 durchgeführt werden, der kleiner ist als der zur Bestimmung der
vorgegebenen ersten Schwelle S1 verwendete Faktor 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 , d. h. es muss für alle
Subrahmen i gelten:
                          𝐷𝐷1,𝑖𝑖 = 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟 ∗ 𝐴𝐴𝑖𝑖 > 𝑆𝑆1 = 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 𝐴𝐴𝑚𝑚𝑚𝑚𝑚𝑚
                                          −𝑟𝑟𝑟𝑟𝑟𝑟 ∗ 𝐴𝐴𝑖𝑖 > −𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆 𝐴𝐴𝑚𝑚𝑚𝑚𝑚𝑚
                                                                    𝐴𝐴𝑚𝑚𝑚𝑚𝑚𝑚
                                                𝑟𝑟𝑟𝑟𝑟𝑟 < 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆
                                                                      𝐴𝐴𝑖𝑖

Diese Bedingung ist insbesondere auch für 𝐴𝐴𝑖𝑖 = 𝐴𝐴𝑚𝑚𝑚𝑚𝑚𝑚 , d. h. für den größten Amplitudenwert der zeitlichen Einhüllenden der Subrahmen vor dem Referenz-Subrahmen
zu erfüllen, womit sich ergibt:
                                                     𝑟𝑟𝑟𝑟𝑟𝑟 < 𝑟𝑟𝑟𝑟𝑟𝑟𝑆𝑆

                                                      - 27 -



5.15 Der Fachperson ist bewusst, dass die Subrahmen vor dem Referenz-Subrahmen regelmäßig nicht nur das unerwünschte, durch eine Transformationscodierung entstehende Vor-Echo beinhalten, sondern darüber hinaus regelmäßig auch
„echte“, d. h. erwünschte Audiosignale, z. B. leise Passagen eines Musikstücks,
enthalten. Daher darf die streitpatentgemäße Reduzierung nicht zu stark, insbesondere nicht auf „Null“, durchgeführt werden, denn dann wäre der Informationsgehalt
dieser Signalanteile gelöscht.


5.16 Gemäß den Angaben in den Absätzen 0050 und 0088 der Streitpatentschrift
können die vorstehend genannten, einen gewissen Aufwand erfordernden Schritte
zur Bestimmung eines signalabhängigen ersten voreingestellten Schwellenwerts
und eines davon abhängigen Reduktionsfaktors für jeden betrachteten Zeitabschnitt
eines transienten Signals insofern vereinfacht werden, als dass ein fester, nicht signalabhängiger Faktor, z. B. 0,5 gewählt wird. Der Fachperson ist bewusst, dass eine
solche Reduzierung regelmäßig eine geringere Verbesserung der Audioqualität zur
Folge haben wird als eine signalstärkenabhängige Reduzierung, sei es durch eine
zu geringe Unterdrückung des Vor-Echos oder durch eine zu starke Reduzierung
gewünschter Signalanteile.


5.17 Jedenfalls ist auch eine solche Reduzierung der Amplitudenwerte mittels eines festen Reduktionsfaktors 𝑟𝑟𝑟𝑟𝑟𝑟𝐹𝐹𝐹𝐹𝐹𝐹 von den Ansprüchen 1 und 6 umfasst, denn
auch damit lassen sich die Anforderungen der Merkmale 2.2 und 2.2‘ erfüllen. Mit
den vorstehend genannten Größen ergibt sich dann für den – im betrachteten Zeitabschnitt – ersten voreingestellten Schwellenwert 𝑆𝑆1 die folgende Beziehung, die
sich stets mit einem ersten Schwellenwert 𝑆𝑆1 > 0 erfüllen lässt, da 𝐴𝐴𝑖𝑖,𝑚𝑚𝑚𝑚𝑚𝑚 stets kleiner als 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 und 𝑟𝑟𝑟𝑟𝑟𝑟𝐹𝐹𝐹𝐹𝐹𝐹 stets kleiner als Eins ist:

                                   𝐷𝐷1,𝑖𝑖 = 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝐹𝐹𝐹𝐹𝐹𝐹 ∗ 𝐴𝐴𝑖𝑖 > 𝑆𝑆1
                              𝐷𝐷1,𝑚𝑚𝑚𝑚𝑚𝑚 = 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝐹𝐹𝐹𝐹𝐹𝐹 ∗ 𝐴𝐴𝑖𝑖,𝑚𝑚𝑚𝑚𝑚𝑚 > 𝑆𝑆1
                                     𝑆𝑆1 < 𝐴𝐴𝑟𝑟𝑟𝑟𝑟𝑟 − 𝑟𝑟𝑟𝑟𝑟𝑟𝐹𝐹𝐹𝐹𝐹𝐹 ∗ 𝐴𝐴𝑖𝑖,𝑚𝑚𝑚𝑚𝑚𝑚


5.18 Nach alledem versteht die Fachperson die Angaben im Merkmal 2.2 lediglich
insofern konkretisierend für die Merkmale 2 und 2.1, dass eine angemessene Reduzierung der Amplitudenwerte der zeitlichen Einhüllenden der Subrahmen vor dem

                                          - 28 -



Referenz-Subrahmen erreicht werden muss. Ob dabei mit einem festen Reduktionsfaktor oder mit einem signalabhängigen Reduktionsfaktor gearbeitet wird, ist unerheblich, da sich – wie gezeigt – stets die Anforderungen aus Merkmal 2.2, d. h.
Differenzen größer als erster voreingestellter Schwellenwert, erfüllen lassen.

Damit erfüllt jede nicht zu kleine und nicht zu große Amplitudenreduzierung, die zu
einer wahrnehmbaren Reduzierung des Vor-Echos und damit zu einer hörbaren
Qualitätsverbesserung führt, ohne zugleich erwünschte Signalanteile zu stark zu
dämpfen, die Anforderungen des Merkmals 2.2.


5.19 Im Übrigen müssen – wie bereits im gerichtlichen Hinweis festgestellt und
von den Parteien nicht bestritten – nicht alle Amplitudenwerte der dem Referenz-Subrahmen vorausgehenden Subrahmen in exakt gleicher Weise reduziert werden,
um die Anforderungen des Merkmals 2.2 zu erfüllen. Mithin können unterschiedliche
Reduktionsfaktoren verwendet werden, auch wenn eine solche unterschiedliche
Reduzierung der Amplituden der zeitlichen Einhüllenden der Subrahmen vor dem
Referenz-Subrahmen zu einer ungleichmäßigen Änderung der in diesen Subrahmen, neben dem unerwünschten Vor-Echo, erwünschten Audiosignalen führt.




                        II. Zur erteilten Fassung (Hauptantrag)


Die zulässige Klage der Klägerin zu 1 hat hinsichtlich der erteilten Fassung des
Streitpatents Erfolg.

Das Streitpatent in der erteilten Fassung erweist sich als nicht patentfähig, da die
Gegenstände der unabhängigen Patentansprüche 6 und 15 aus der Entgegenhaltung JP 2008 209 646 A (mit der Kurzbezeichnung: SONY - NK4/MFG7) bekannt
sind (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Nr. 1, Art. 52, 54 EPÜ).


Da sich das Streitpatent in der erteilten Fassung als nicht patentfähig erweist, kann
dahinstehen, ob der Gegenstand des Streitpatents in der erteilten Fassung über die
ursprünglich eingereichten Unterlagen hinausgeht und somit auf einer unzulässigen
Erweiterung beruht und nicht so deutlich und vollständig offenbart ist, dass eine

                                        - 29 -



Fachperson ihn ausführen kann, Art. II § 6 Abs. 1 Nr. 2 und 3 IntPatÜG i. V. m.
Art. 138 Abs. 1 lit. b) und c), 123 Abs. 3 EPÜ).


1.    Die Entgegenhaltung SONY (JP 2008 209 646 A), im Folgenden wird hinsichtlich der Figuren auf das japanische Originaldokument und hinsichtlich der Beschreibung auf die Übersetzung in die englische Sprache mit der Kurzbezeichnung
SONY_E (NK4a) Bezug genommen, legt ihrer Betrachtung Audio-Codecs zugrunde, bei denen transiente Signale trotz Gegenmaßnahmen, wie codiererseitiger
Amplitudenabflachung und kompensierender, decodiererseitiger Verstärkung (AT-RAC3, ATRAC-X) bzw. Umschaltung von Blocklängen (MP3), Vor- und Nach-Echos
erzeugen, die die Hörqualität beeinträchtigen (SONY_E, Abs. 0002, 0004).


Daher stellt sich SONY die Aufgabe, Echos zu reduzieren und bezeichnet das entsprechende decodiererseitige Verfahren als Rauschreduktion (noise reduction)
(SONY_E, Abs. 0005).

Ein transientes Eingangssignal des Decodierers wird im Zeitbereich in mehrere Bereiche unterteilt. Danach werden die maximalen Amplitudenwerte der jeweiligen Bereiche ermittelt, der Bereich mit dem größten maximalen Amplitudenwert erfasst,
die Verhältnisse der maximalen Amplitudenwerte zu dem größten maximalen
Amplitudenwert bestimmt und in Abhängigkeit davon in den Bereichen, die den Bereich mit dem größten maximalen Amplitudenwert umgeben, die Amplituden reduziert (SONY_E, Abs. 0006 bis 0009).

In einem Ausführungsbeispiel von SONY wird einem MP3-Decodierer (50) eine
„Rauschreduktionseinheit“ (60) nachgeschaltet, die das Decodierer-Ausgangssignal analysiert und danach eine entsprechende Signalkorrektur durchführt, um Vorund Nach-Echos zu reduzieren (Fig. 23 und Abs. 0107-0116):

                                        - 30 -




                   SONY, Fig. 23 mit Kommentierung durch den Senat


Ohne die „Rauschreduktion“ weist ein vom Decodierer rekonstruiertes transientes
Signal ein störendes Vor- und Nachecho auf (Fig. 28, 29 und Abs. 0149 bis 0153):




                  SONY, Fig. 28, mit Kommentierung durch den Senat




                  SONY, Fig. 29, Reduzierung von Vor- und Nachecho

                                          - 31 -




Der gesamte decodiererseitige Verfahrensablauf ist aus Figur 27 ersichtlich und ab
Absatz 0136 (SONY_E) beschrieben:




                    SONY, Fig. 27 mit Kommentierung durch den Senat




2.       Somit ist aus dem Dokument SONY (JP 2008-209646 A) in Worten des erteilten Anspruchs 6 folgendes bekannt:

     0’       A transient signal decoding method for speech signals or audio signals, comprising:
                 Das von SONY vorgeschlagene Verfahren zur Reduzierung
                 von Vor- und Nachechos wird in der Rauschreduktionsschaltung 60 durchgeführt, die dem MP3-Decodierer 50 nachgeschaltet ist (Fig. 23), also decodiererseitig.
     1        obtaining (Fig. 27: S33, S34, S35) a reference sub-frame (Dz)

                                - 32 -



         Die durch Unterteilung von Blöcken erhaltenen kürzeren Sub-Blöcke Dx, Dy und Dz (Abs. 0138: …sets an area corresponding to the sub-block size as the intervals Dx, Dy, and Dz)
         stellen streitpatentgemäße Subrahmen dar.
1.1’   where a maximal time envelope having a maximal amplitude value
       (bspw. Pz) from time envelopes of all sub-frames (Dx, Dy, Dz bzw.
       area X, Y, Z) of a pre-obtained time-domain signal (Abs. 0102: time
       signal Tn’; Abs. 0107: Fig. 23: Ausgangssignal Raw Decoded PCM
       des MP3-Decodierers 50) is located
                                          In den Schritten S31 bis S33
                                         des in Figur 27 dargestellten
                                         Verfahrens wird das Ausgangssignal des Decodierers (Fig. 23:
                                         Raw    Decoded      PCM)     der
                                         Rauschreduktionsschaltung 60
                                         zugeführt und in Subblöcke unterteilt, z. B. in drei Subblöcke
                                         Dx, Dy und Dz (Abs. 0136 -
         0138). Im Schritt S34 wird die maximale Amplitude in jedem
         der Subrahmen ermittelt, z. B. Px, Py und Pz (Abs. 0139: …
         detects the peak (Px, Py, Pz) in each peak detection interval
         (Dx, Dy, Dz)). Im Schritt S35 wird derjenige Subrahmen lokalisiert, der die größte maximale Amplitude aller Subrahmen
         aufweist (Abs. 0140: … detects a maximum peak from the
         peak values Px, Py, and Pz; sowie Abs. 0159 - 0163), z. B.
         der letzte der drei betrachteten Subrahmen, Dz, mit der
         Amplitude Pz in Figur 33A. Wie zur Auslegung dargelegt, ist
         die maximale Amplitude (Spitzenwert) der Amplituden der Abtastwerte in einem Subrahmen ein streitpatentgemäßer
         „Amplitudenwert der zeitlichen Einhüllenden eines Subrahmens“.
1.2’   the pre-obtained time domain signal (Raw Decoded PCM) is a transient signal;

                                - 33 -



        Wie einleitend dargelegt, zeigen die Figuren 28A und 28B ein
        transientes Signal (plötzlicher Übergang von kleiner zu großer
        und wieder zu kleiner Amplitude) am Eingang des Codierers
        (Fig. 28A), was am Ausgang des Decodierers (Fig. 28B) ohne
        Gegenmaßnahmen ein Vor- und ein Nach-Echo verursacht.
        Ein weiteres Beispiel für ein Vor-Echo zeigen die Figuren 33A
        und 33B.
2     decreasing (S39, S40, S41, S42) an amplitude value (Px, Py) of the
      time envelope
2.1   of each sub-frame (Dx, Dy) before the reference sub-frame (Dz)
        Gemäß den Angaben in den Absätzen 0144 bis 0147 werden
        für die Subrahmen Dx, Dy vor dem Referenz-Subrahmen Dz
        Korrekturwerte U und V berechnet und die jeweiligen Amplituden Px und Py durch Multiplikation mit U bzw. V reduziert, vgl.
        Fig. 33:




                              SONY, Fig. 33A, 33B

2.2   in such a way that a first difference is greater than a preset first
      threshold, wherein the first difference is a difference between the
      amplitude value (Px, Py) of the time envelope of each sub-frame (Dx,
      Dy) before the reference sub-frame (Dz) and the amplitude value
      (Pz) of the maximal time envelope (Dz); and
        Die Fachperson kann SONY entnehmen (SONY_E, Abs.
        0141, 0142, 0123), dass die Reduktionsfaktoren U und V von
        dem Verhältnis der maximalen Amplitude in dem jeweiligen

                                       - 34 -



               Subrahmen vor dem Referenz-Subrahmen zu der maximalen
               Amplitude des Referenz-Subrahmens abhängen, wobei das
               berechnete Verhältnis noch mit Anpassungskoeffizienten (α
               und β) skaliert wird. Dabei liest die Fachperson mit, dass die
               in SONY gezeigte signalstärkeabhängige Reduzierung der
               Amplitude stets so gewählt ist, dass die Echo-Effekte ausreichend reduziert werden, also die reduzierten Amplituden einen Mindestabstand zur Amplitude des Referenz-Subrahmens aufweisen. Zugleich werden die Amplituden jedoch nicht
               auf null reduziert. Wie zur Auslegung gezeigt, fällt eine solche
               signalabhängige Reduzierung unter das Merkmal 2.2. Wie
               ebenfalls zur Auslegung dargelegt, müssen die vor dem Referenz-Subrahmen liegenden Subrahmen nicht alle durch den
               gleichen Reduzierungsfaktor verringert werden. Insofern erfüllt das aus SONY bekannte Verringern der einzelnen Subblöcke durch Multiplikation mit unterschiedlich großen Faktoren die Anforderungen gemäß Merkmal 2.2.
     3’      modifying the pre-obtained time-domain signal according to the adjusted time envelope, so as to obtain a recovered transient signal.
               SONY, Fig. 27: Verfahrensschritte S40 bis S42 i. V. m. den
               Absätzen 0145 bis 0148 von SONY_E


Der Gegenstand des Anspruchs 6 in der erteilten Fassung ist demnach vollständig
aus der Druckschrift JP 2008-290646 A (SONY) bekannt und erweist sich somit als
nicht neu. Gleiches gilt für den Gegenstand des Vorrichtungsanspruchs 15, der inhaltlich korrespondierende funktionale Merkmale aufweist.



3.    Selbst unter der – von der vorstehenden Auslegung abweichenden – Annahme, dass die Bestimmung eines Amplitudenwerts für eine zeitliche Einhüllende
eines Subrahmens eine Verarbeitung, insbesondere eine Mittelwertbildung, mehrere Abtastwerte je Subrahmen erfordern würde, wären die Gegenstände der Ansprüche 6 und 15 nicht patentfähig. Die Fachperson hat ausgehend von SONY eine

                                        - 35 -



Veranlassung, die, z. B. durch Rausch-oder Störsignale fehleranfällige, Spitzenwertermittlung durch eine Mittelwertbildung der Amplituden- oder Energiewerte je Subblock zu ersetzen, um eine aussagekräftigere bzw. genauere Charakterisierung des
Signals in jedem Subblock zu ermöglichen und letztendlich eine zuverlässigere Vorund Nach-Echounterdrückung zu erzielen. Ein solches Vorgehen gehört zum Fachwissen und ist im Übrigen beispielsweise aus dem Dokument KÖVESI II_EN (Abs.
0109: calculating the energy of each of the sub-blocks“) und aus dem Audio-Codec-Standard G.729.1 (S. 54, letzter Absatz: subframe energy is computed) bekannt.
Bei Zugrundelegen der vorstehend genannten anderen Auslegung des Streitpatents
ergeben sich die Gegenstände der Ansprüche 6 und 15 des Streitpatents für die
Fachperson somit jedenfalls in naheliegender Weise aus SONY und ihrem Fachwissen, hier belegt durch KÖVESI II_EN und G.729.1.



4.     Die weiteren angegriffenen Patentansprüche nach Hauptantrag bedürfen keiner weiteren, isolierten Prüfung, weil die Beklagte (auch) den Hauptantrag als geschlossenen Anspruchssatz versteht und das Streitpatent auch insoweit nur als
Ganzes verteidigt; dies rechtfertigt, das Patent in der erteilten Fassung insgesamt
für nichtig zu erklären, nachdem sich der Gegenstand eines Patentanspruchs aus
dem vom Patentinhaber verteidigten Anspruchssatz als nicht patentfähig erweist
(vgl. BGH, Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator).




     III.   Zur Fassung des Streitpatents nach dem als ersten gestellten
            Hilfsantrag


In der Fassung nach dem als ersten gestellten, „unbenannten“ Hilfsantrag erweist
sich das Streitpatent als zulässig und schutzfähig, so dass die Klage, soweit sie sich
auch gegen diese Fassung richtet, abzuweisen ist.


1.     Der Gegenstand des Streitpatents gemäß dem als ersten gestellten, „unbenannten“ Hilfsantrag geht nicht über den Inhalt der Anmeldung in ihrer ursprünglich
eingereichten Fassung hinaus.

                                           - 36 -




1.1       Der als erstes gestellte, „unbenannte“ Hilfsantrag umfasst nur die Ansprüche
mit Codiererbezug, d. h. die Ansprüche 1 bis 5, 10 bis 14 und 17, jeweils in der
erteilten Fassung.


1.2       Der Gegenstand des Anspruchs 1 gemäß dem als ersten gestellten Hilfsantrag (der dem Anspruch 1 der erteilten Fassung entspricht) geht wie folgt auf die
ursprüngliche Anmeldung (veröffentlicht als WO 2010/078816 A1 in chinesischer
Sprache, wobei im Folgenden auf die englischsprachige Veröffentlichung
EP 2 352 145 A1 Bezug genommen wird) zurück (Unterstreichungen vom Senat
hinzugefügt):

      0      A transient signal encoding method for speech signals or audio signals, comprising:
                Anspruch 1: A transient signal encoding method, comprising;
                Abs. 0003: speech signals … audio encoding algorithm;
                Abs. 0004: coded voice and audio;
                Abs. 0006: the transient signal is likely to generate a pre-echo;
                therefore, the prior art has the disadvantage that the effect of the
                transient signal recovered at the decoding end is not satisfactory.
                Abs. 0007: The present invention is directed to a transient signal
                encoding method and device … which are configured to improve
                the quality of recovery of transient signals.
                Auch wenn Sprach- und Audiosignale explizit nur im Zusammenhang mit dem Stand der Technik genannt werden, liest die Fachperson in der ursprünglichen Anmeldung mit, dass das beschriebene Verfahren für die Codierung solcher Signale geeignet sein
                soll, denn es sollen die aus dem Stand der Technik bekannten
                Verfahren zur Codierung transienter Sprach- und Audiosignale
                hinsichtlich ihrer Probleme, d. h. hinsichtlich der unvollkommenen Unterdrückung von Vor-Echos, verbessert werden.
      1      obtaining (11) a reference sub-frame
                Merkmal 1 ist wörtlich aus dem ursprünglichen Anspruch 1 übernommen.

                                     - 37 -



1.1 where a maximal time envelope having a maximal amplitude value
     from time envelopes of all sub-frames of an input signal is located,
        Anspruch 1: where a maximal time envelope having a maximal
        amplitude value is located from time envelopes of all sub-frames
        of an input transient signal;
        Auch wenn die Wörter “is located” ursprünglich anders platziert
        waren, hat die Fachperson bereits die ursprüngliche Formulierung im Sinne des Merkmals 1.1 verstanden, nämlich, dass der
        Referenz-Subrahmen derjenige Subrahmen (eines Zeitabschnitts) des Eingangssignals ist, dessen zeitliche Einhüllende
        den maximalen Amplitudenwert der zeitlichen Einhüllenden aller
        Subrahmen (des betrachteten Zeitabschnitts) des Eingangssignals aufweist.
1.2 wherein the input signal is a transient signal;
        Anspruch 1: of an input transient signal
2    decreasing (13) an amplitude value of the time envelope
        Anspruch 1: adjusting an amplitude value of the time envelope of
        each sub-frame before the reference sub-frame in such a way
        that a first difference is greater than a preset first threshold;
        Abs. 0051: increasing the amplitude value … on the time envelope having the maximal amplitude value, and/or, … decreasing
        the amplitude value is performed on all other time envelopes;
        Abs. 0157: transient signal processing signal i. V. m.
        Abs. 0158: The modification of the time envelope of the transient
        signal may be performed at the encoding end i. V. m.
        Abs. 0159: adjust an amplitude value of the time envelope of
        each sub-frame before the reference sub-frame in such a way
        that a first difference is greater than a preset first threshold i. V. m
        Abs. 0161: the time envelope of the transient signal is modified
        at the encoding end, and the difference between the amplitude
        value of the time envelope having the maximal amplitude value
        among the time envelopes of all sub-frames of the transient signal and the amplitude values of other time envelopes is enlarged,
        so as to highlight the characteristics of the transient signal,

                                          - 38 -



                thereby improving the quality of the transient signal recovered at
                the decoding end.
                Die Fachperson entnimmt der ursprünglichen Anmeldung die
                technische Lehre, dass zur Verstärkung oder „Schärfung“ des
                transienten Signalcharakters die Amplituden der zeitlichen Einhüllenden der Subrahmen vor dem Referenz-Subrahmen zu verringern sind (Anspruch 1), wobei zusätzlich noch die Amplituden
                der zeitlichen Einhüllenden der Subrahmen nach dem Referenz-Subrahmen verringert werden können (Anspruch 2) und weiter
                zusätzlich die Amplitude der zeitlichen Einhüllenden des Referenz-Subrahmens vergrößert werden kann (Anspruch 3).
      2.1 of each sub-frame before the reference sub-frame
                Merkmal 2.1 ist wörtlich aus dem ursprünglichen Anspruch 1
                übernommen.
      2.2 in such a way that a first difference is greater than a preset first threshold, wherein the first difference is a difference between the amplitude
             value of the time envelope of each sub-frame before the reference
             sub-frame and the amplitude value of the maximal time envelope; and
                Merkmal 2.2 ist wörtlich aus dem ursprünglichen Anspruch 1
                übernommen.
      3      writing (15) the adjusted time envelope obtained by the decreasing
             step into an encoding bitstream.
                Anspruch 1: encoding method … writing the adjusted time envelope into bitstream.
                Abs. 0157 bis 0162, insbesondere Abs. 0159: write the adjusted
                time envelope into bitstream


1.3       Der Gegenstand des Streitpatents nach dem „unbenannten“ Hilfsantrag geht
nicht deshalb über den Gegenstand der ursprünglichen Anmeldung hinaus, weil in
Merkmal 2 des Anspruchs 1 von „Verringern“ (decreasing) der Amplitudenwerte der
zeitlichen Einhüllenden der vor dem Referenz-Subrahmen liegenden Subrahmen
die Rede ist, während im ursprünglichen Anspruch 1 die Formulierung „Anpassen“
(adjusting) verwendet wurde.

                                       - 39 -



Wie vorstehend dargelegt, offenbart die ursprüngliche Anmeldung, dass die erfindungsgemäße Verstärkung bzw. „Schärfung“ des transienten Signalcharakters alleine durch Verringern der Amplituden der zeitlichen Einhüllenden der Subrahmen,
die vor dem Referenz-Subrahmen liegen, erreicht werden kann. Eine zwingende
Kombination mit den weiteren offenbarten Anpassungsmöglichkeiten (Amplitudenverringerung nach dem Referenz-Subrahmen bzw. Erhöhung im Referenz-Subrahmen) ist dagegen auch in den ursprünglichen Anmeldeunterlagen nicht gefordert.

Auch die konkrete Verringerung dieser Amplituden auf die Hälfte ihres ursprünglichen Wertes gemäß den Figuren 2 und 3 der ursprünglichen Anmeldung mit zugehöriger Beschreibung stützt dieses Verständnis der Fachperson der ursprünglichen
Anmeldung. Denn danach wird diese Reduzierung (Schritt 2707) immer durchgeführt – jedenfalls wenn ein transientes Eingangssignal vorliegt (Ausgang „Transient
signal“ aus Block 26 in Figur 2) – wohingegen die Verringerung der Amplituden der
zeitlichen Einhüllenden der nach dem Referenz-Subrahmen liegenden Subrahmen
(Schritt 2717) und die Vergrößerung der Amplitude der zeitlichen Einhüllenden des
Referenz-Subrahmens (Schritt 2715) von einer weiteren Bedingung (Schritt 2711)
abhängig ist und daher nicht in jedem Fall durchgeführt werden.


1.4   Der Gegenstand des Streitpatents nach dem „unbenannten“ Hilfsantrag geht
auch nicht deshalb über den Gegenstand der ursprünglichen Anmeldung hinaus,
weil der in Merkmal 2.2 genannte „erste voreingestellte Schwellenwert“ bei der Beschreibung der Ausführungsform gemäß den Figuren 2 und 3, die eine feste Reduzierung auf die Hälfte vorsieht, nicht genannt wird. Zunächst kommt es schon nicht
auf das Ausführungsbeispiel gemäß den Figuren 2 und 3 an, da die Fachperson
bereits den übrigen Beschreibungsteilen, wie vorstehend dargelegt, den Gegenstand des Anspruchs 1 erteilter Fassung den ursprünglichen Unterlagen als zur angemeldeten Erfindung gehörend entnommen hat.

Darüber hinaus entnimmt die Fachperson, wie zur Auslegung dargelegt und begründet, dem Streitpatent, was in gleicher Weise für die ursprüngliche Anmeldung gilt,
da sich die Figuren und die zugehörigen Beschreibungsteile insofern inhaltlich nicht
unterscheiden, dass sich die Ausführungsform nach den Figuren 2 und 3 als eine
vereinfachte Konkretisierung der Ausführungsform nach der Figur 1 erweist. Dies

                                        - 40 -



auch deshalb, weil im Absatz 0055 der ursprünglichen Anmeldung die feste Reduzierung auf die Hälfte des ursprünglichen Wertes unmittelbar im Anschluss an die
signalstärkenabhängige Reduzierung, nämliche größere Reduzierung bei geringen
anfänglichen Amplitudenunterschieden und umgekehrt, genannt wird und beide
Ausführungsformen unter die am Beginn des Absatzes 0055 genannte, allgemeine
Reduzierung zum Erhalt einer modifizierten zeitlichen Einhüllenden gemäß Schritt
2707 fallen sollen, auch wenn in Figur 3 zum Schritt 2707 nur eine der beiden Ausführungsformen dargestellt ist.


1.5   Die vorstehenden Ausführungen gelten in entsprechender Weise für den unabhängigen, auf eine Vorrichtung zum Codieren gerichteten Anspruch 10 und für
den nebengeordneten, auf ein System zum Verarbeiten eines transienten Signals
gerichteten Anspruch 17, der auf einen der Ansprüche 10 bis 14 rückbezogen ist.


1.6   Die abhängigen Ansprüche 2 bis 5 und 11 bis 14 in der Fassung nach dem
als ersten gestellten Hilfsantrag (die den Ansprüchen 2 bis 5 und 11 bis 14 der erteilten Fassung entsprechen) gehen in zulässiger Weise auf die ursprünglichen Ansprüche 2 bis 5 und 11 bis 14 zurück. Hinsichtlich der Zulässigkeit des „Verringerns“
(decreasing) der Amplitude in den Ansprüchen 2 und 11 erteilter Fassung anstelle
des „Anpassens“ (adjusting) in den ursprünglichen Ansprüchen 2 und 11 wird auf
die obigen Ausführungen zum Anspruch 1 verwiesen, die hier entsprechend gelten.



2.    Die Erfindung ist in dem Streitpatent in der Fassung nach dem „unbenannten“
Hilfsantrag so deutlich und vollständig offenbart, dass eine Fachperson sie ausführen kann.


2.1   Wie zur Auslegung dargelegt und begründet, lehrt das Streitpatent sowohl
eine signalstärkenabhängige Reduzierung der Amplitudenwerte (im Abs. 0018
quantitativ, im Abs. 0050 qualitativ) als auch eine Reduzierung durch Multiplikation
mit einem festen Faktor kleiner als Eins, z. B. 0,5 (Abs. 0050). Wie ebenfalls zur
Auslegung dargelegt, kann die Fachperson dem Streitpatent für beide Fälle entnehmen, wie die Anforderungen des Merkmals 2.2 erfüllt werden können.

                                        - 41 -



Hinsichtlich der signalstärkeabhängigen Variante ist die Fachperson auch in der
Lage, aus dem im Absatz 0018 genannten Wertebereich (1/8 bis 1/2) zur Bestimmung des ersten voreingestellten Schwellenwerts mittels einer überschaubaren Anzahl orientierender Versuche – in diesem Fachgebiet sind dies fachüblich Simulationen, gegebenenfalls ergänzt durch Messungen – zu ermitteln, welcher Reduzierungsfaktor die besten Ergebnisse, d. h. die beste Qualität des rekonstruierten Audiosignals liefert. Die Durchführung und Auswertung dieser Versuche ist eine typische Routinearbeit der angesprochenen Fachperson, für die keine eigenen erfinderischen Überlegungen nötig sind. Diese Versuche sind selbstverständlich auch nur
einmal, nämlich bei der Entwicklung des Audio-Codecs, durchzuführen. Im Betrieb
des Audio-Codecs kann dann zur Bestimmung des signalabhängigen ersten
Schwellenwerts immer gleich vorgegangen werden.

Gleiches gilt für die Angabe „größer als“ (greater than) in Merkmal 2.2. Denn die
Fachperson kann mittels der oben genannten Versuche ebenfalls problemlos ermitteln, ob die „erste Differenz“ bzw. „die ersten Differenzen“ zwischen den verringerten
Amplitudenwerten der Subrahmen vor dem Referenz-Subrahmen und dem Amplitudenwert des Referenz-Subrahmens nur minimal oder deutlich größer als der zuvor
bestimmte erste Schwellenwert sein muss, um die angestrebte Qualitätsverbesserung des im Decodierer wiederhergestellten Audiosignals zu erreichen.

Die Wahl der in Merkmal 2.2 genannten Größen stellt die Fachperson auch deshalb
nicht vor größere Schwierigkeiten, da sie einerseits nicht von einem beliebigen Signalverlauf ausgeht, sondern von einem identifizierten transienten Signalverlauf,
dessen „Spitze“ im als Referenz gewählten Subrahmen liegt und andererseits das
Ziel vor Augen hat, die Charakteristik dieses transienten Signals deutlicher hervorzuheben, ohne den ursprünglichen Signalverlauf vor (und nach) dem transienten
Signal zu unterdrücken.



3.    Der Gegenstand des Patentanspruchs 1 gemäß dem als ersten gestellten
„unbenannten“ Hilfsantrag ist neu. Keines der im Verfahren befindlichen Dokumente
des Standes der Technik zeigt ein Verfahren mit allen Merkmalen des Anspruchs 1.

                                         - 42 -



3.1    Der Gegenstand des Anspruchs 1 des Streitpatents in der Fassung nach dem
als ersten gestellten „unbenannten“ Hilfsantrag (= Anspruch 1 der erteilten Fassung)
ist   gegenüber    dem     Dokument     mit       der   Kurzbezeichnung   MICHAELIS
(US 6,889,186 B1 – NK3, MFG6, HLNK12) neu.


3.1.1 Die Entgegenhaltung MICHAELIS geht von der Erkenntnis aus, dass wegen
des großen Dynamikbereichs menschlicher Sprache einige Konsonanten-Töne oftmals eine deutlich geringere Amplitude als Vokal-Töne hätten und dadurch unter
die Sprach-Hörschwelle rutschen könnten, was die Verständlichkeit von Sprache
beeinträchtige. Die dagegen bislang verwendete Amplituden-Kompression führe zur
Verstärkung schwacher Störgeräusche, was die Qualität verschlechtere (Sp. 1,
Z. 13 – 36).

Zur Verbesserung der Sprachverständlichkeit schlägt MICHAELIS vor, ein Sprachsignal in Rahmen (frames) oder Segmente (segments) zu unterteilen, wie es bei
LPC- oder CELP-Codierern üblich sei, für jeden Rahmen mittels einer Spektralanalyse einen Klang-Typ zu bestimmen (Anspruch 25: said means for determining a
spoken sound type includes means for determining whether a frame includes at
least one of the following: a vowel sound, a voiced fricative, an unvoiced fricative, a
voiced plosive, and an unvoiced plosive) und abhängig davon den Rahmen zu modifizieren, z. B. durch Veränderung der Amplitude des Rahmens, wobei auch umgebende Rahmen modifiziert werden könnten (Sp. 1, Z. 44 – Sp. 2, Z. 10).

In dem Ausführungsbeispiel gemäß der Figur 3 werden im Codierer bei Detektion
eines Rahmens mit dem Klangtyp unvoiced fricative die Amplitude dieses Rahmens
erhöht, bei dem Klangtyp voiced plosive die Amplitude des vorhergehenden Rahmens verringert und bei dem Klangtyp unvoiced plosive die Amplitude dieses Rahmens erhöht und die Amplitude des vorhergehenden Rahmens verringert (Sp. 4, Z.
39 – Sp. 5, Z. 8; Sp. 5, Z. 18 – 42).

Die Rahmen (frames) haben – wie dies bei Audio-Codecs typisch ist – eine Länge
von ca. 20 – 25 ms (Sp. 2, Z. 66, 67; Sp. 4, Z. 62, 63). Die Spektralanalyse findet
rahmenweise statt. Eine zeitlich genauere Analyse und/oder Modifizierung, z. B. auf
der Basis von Subrahmen, ist aus MICHAELIS nicht bekannt.

                                        - 43 -



Darüber hinaus ist es aus MICHAELIS nicht bekannt, zeitliche Einhüllende eines
Zeitabschnitts zu bilden und jeweils einen Amplitudenwert je zeitlicher Einhüllenden
zu bestimmen. Zwar ist in MICHAELIS im Anspruch 1 allgemein von der „Modifizierung eines Klangparameters“ die Rede, jedoch offenbart MICHAELIS als einzige
Konkretisierung die Modifizierung der Amplitude des im Frequenzbereich
vorliegenden Signals (Sp. 3, Z. 30 – 33: The modified and unmodified frame information is next transferred to the data assembly unit 24 which assembles the spectral
information for all of the frames to generate the compressed output signal …“; Sp. 3,
Z. 49 – 55: … to describe each frame’s spectral content in terms of human speech
mechanism analogs, such as overall amplitude, … the pitch of the sound”; Sp. 4,
Z. 3 – 9: … to modify the frame information of selected frames based on the determined sound type. The spectral information for each of the frames, whether modified
or unmodified, is then used to develop the compressed speech signal in a conventional manner”; Sp. 4, Z. 16, 17: … spectral parameters such as amplitude … and
pitch (if any) of sounds will be measured; Sp. 4, Z. 23 – 30: information corresponding to the frame may be modified … the modification of the frame information will
include boosting or reducing the amplitude of the corresponding frame.).

Somit werden für jeden Rahmen spektrale Parameter, u. a. „die Amplitude des Rahmens“ bestimmt. Die Fachperson versteht diese Angaben so, dass je Rahmen ein
das Spektrum repräsentierender Amplitudenwert, beispielsweise der Mittelwert der
Amplituden der einzelnen spektralen Komponenten über den Frequenzbereich, bestimmt und dann modifiziert wird. Hierfür empfängt eine „frame modification unit“ ein
zuvor von einer „frame analysis unit“ vom Zeit- in den Frequenzbereich transformiertes Signal und ändert in Abhängigkeit vom ermittelten Klang-Typ gegebenenfalls die Amplitude des Frequenzspektrums des Rahmens (Fig. 1 mit zugehöriger
Beschreibung).

Nach der Lehre von MICHAELIS kann die Modifizierung der Amplituden im Codierer
oder im Decodierer durchgeführt werden (Ansprüche 16 und 17 bzw. 18 und 19; Sp.
5, Z. 56 – 64; Sp. 6, Z. 21 – 29).


3.1.2 Aus der Entgegenhaltung MICHAELIS ist in Worten des Anspruchs 1 gemäß
dem als ersten gestellten „unbenannten“ Hilfsantrag Folgendes bekannt:

                                    - 44 -



0    A transient signal encoding method for speech signals, comprising:

        Sp. 5, Z. 22 – 31: Plosive sounds are thus characterized by a sudden drop in amplitude followed by a sudden rise in amplitude within
        a speech signal … the amplitude “spike” that characterizes plosive
        sounds is accentuated, resulting in enhanced intelligibility; Sp. 5, Z.
        36 – 38:… to emphasize the amplitude “spike” of the plosive as described above;
        Gemäß MICHAELIS sind Signalabschnitte, die Plosive, und zwar
        sowohl stimmlose als auch stimmhafte Plosive, enthalten, transiente Signale im Sinne des Streitpatents, da nach einem kurzen
        Amplitudenabfall die Amplitude plötzlich ansteigt und einen Spitzenwert (spike) erreicht.

1teils obtaining (56) a reference sub-frame

        Gemäß Figur 3, Schritt 56 wird rahmenweise eine Spektralanalyse
        durchgeführt, wobei neben dem Signaltyp des Rahmens auch ein
        spektraler Amplitudenwert je Rahmen bestimmt wird. Wenn in einem Rahmen als Signaltyp ein Plosiv ermittelt wird, wird dieser
        Rahmen – im Vergleich zu dem vorhergehenden Rahmen – hervorgehoben (accentuated) und bildet somit einen „Referenz-Rahmen“
        (Sp. 5, Z. 18 – 42).

1.1teils where a maximal time envelope [frequency spectrum] having a maximal amplitude value from time envelopes [frequency spectra] of all subframes of an input signal is located,

        Gemäß MICHAELIS ist ein Plosiv dadurch charakterisiert, dass die
        Amplitude nach einem plötzlichen Abfall einen plötzlichen Anstieg
        zeigt. Ein Plosiv wird durch einen Amplitudenvergleich mit benachbarten Rahmen identifiziert (Sp. 5, Z. 22 – 28: comparing the
        amplitudes of adjacent frames). Wie einleitend zu MICHEALIS dargelegt, werden jedoch keine zeitlichen Einhüllenden gebildet und
        deren (mittlere) Amplituden bestimmt, sondern es wird für jeden
        Rahmen eine Spektralanalyse durchgeführt und dabei jeweils ein
        (z. B. mittlerer) Amplitudenwert des Frequenzspektrums bestimmt

                                     - 45 -



        (Sp. 4, Z. 13 – 18: spectral analysis … spectral parameters such as
        amplitude, voicing and pitch; Sp. 4, Z. 25 – 30: … the modification
        of the frame information will include boosting or reducing the
        amplitude of the corresponding frame).

1.2 wherein the input signal is a transient signal;

        Wie zu Merkmal 1 dargelegt, bildet der Sprachsignalabschnitt, der
        den Plosiv beinhaltet, ein transientes Signal.

2teils decreasing (13) an amplitude value of the time envelope[frequency spectrum]

2.1teils of each sub-frame before the reference sub-frame

        Sowohl bei stimmhaften als auch bei stimmlosen Plosiven wird die
        spektrale Amplitude des Signals in dem vorhergehenden Rahmen
        verringert (Fig. 3: 60, 62; Sp. 5, Z. 18 – 20, 32 – 36; Anspruch 1).
        Ob damit die spektralen Amplituden der Signale in allen vorhergehenden Rahmen verringert werden, hängt davon ab, aus wie vielen
        Rahmen das betrachtete Signal bzw. der betrachtete Signalabschnitt besteht. Wie zur Auslegung ausgeführt, werden nach der
        Lehre des Streitpatents selbstverständlich ebenfalls nicht „alle“
        Subrahmen vor dem Referenz-Subrahmen in ihrer Amplitude reduziert, sondern nur diejenigen Subrahmen, die zum betrachteten Signalabschnitt gehören, der in den Ausführungsbeispielen des Streitpatents bspw. zwölf Subrahmen umfassen kann. Wenn also bei MI-CHAELIS der betrachtete Signalabschnitt aus beispielsweise drei
        Rahmen besteht – einer vor und einer nach dem Referenz-Rahmen
        – so werden die Amplituden aller Rahmen vor dem Referenz-Rahmen reduziert.
        Jedoch werden nach der Lehre von MICHAELIS keine zeitlichen
        Einhüllenden gebildet und deren Amplituden modifiziert, sondern
        die Amplitudenverringerung findet im Frequenzbereich statt.

2.2teils in such a way that a first difference is greater than a preset first threshold, wherein the first difference is a difference between the amplitude

                                    - 46 -



     value of the time envelope [frequency spectrum] of each sub-frame before the reference sub-frame and the amplitude value of the maximal time
     envelope [frequency spectrum]; and

        Die Fachperson entnimmt MICHAELIS im Zusammenhang mit der
        Vergrößerung der spektralen Amplitude des Referenz-Rahmens
        bei einem Frikativ als mögliche Varianten der Amplitudenänderung
        eine Erhöhung durch einen vorbestimmten Verstärkungswert, auf
        einen vorbestimmten Amplitudenwert und eine Erhöhung um einen
        Betrag, der von den Amplituden der benachbarten Rahmen abhängt (Sp. 5, Z. 4 – 8). Dabei liest die Fachperson entsprechende
        Varianten auch für die Reduzierung der spektralen Amplitude des
        vor einem Plosiv liegenden Rahmens bei der daran anschließenden
        Beschreibung der Behandlung stimmhafter und stimmloser Plosive
        (Sp. 5, Z. 18 ff) mit. Wie zur Auslegung des Streitpatents dargelegt,
        erfüllen sowohl signalabhängige als auch signalunabhängige Reduzierungen die Anforderungen des Merkmals 2.2.
        Jedoch werden gemäß MICHAELIS keine Amplituden zeitlicher
        Einhüllenden, sondern spektrale Amplituden reduziert.

3teils writing the adjusted time envelope [spectral information] obtained by the
     decreasing step into an encoding bitstream.

        Anspruch 17: said system is implemented within a … (CELP) encoder
        Sp. 4, Z. 33 – 38: The spectral information corresponding to the
        frames, whether modified or unmodified, is then assembled into a
        compressed speech signal (step 38). This compressed speech signal can later be decoded to generate an audible speech signal having enhanced intelligibility.
        Gemäß MICHAELIS werden keine modifizierten Amplitudenwerte
        zeitlicher Einhüllenden, sondern modifizierte Spektralwerte in den
        Bitstrom eingeschrieben.

                                       - 47 -



Danach ist der Gegenstand des Anspruchs 1 in der Fassung nach dem als ersten
gestellten Hilfsantrag nicht vollständig aus der Druckschrift MICHAELIS bekannt
und erweist sich somit als neu gegenüber dieser Entgegenhaltung.


3.2    Der Gegenstand des Anspruchs 1 des Streitpatents in der Fassung nach dem
als ersten gestellten „unbenannten“ Hilfsantrag (der dem Anspruch 1 der erteilten
Fassung entspricht) ist auch gegenüber der Druckschrift SONY (JP 2008-209646 A)
neu.

Wie zum Hauptantrag dargelegt, sind aus der Entgegenhaltung SONY zwar die Gegenstände der decodiererbezogenen Ansprüche 6 und 15 bekannt, jedoch finden
gemäß der Lehre von SONY die Amplitudenreduzierungen ausschließlich im Decodierer statt, wohingegen als Codierer ein nicht veränderter MP3- bzw. ATRAC-Codierer zum Einsatz kommt.

Insofern sind aus SONY die Merkmale 0 (A transient signal encoding method for
speech signals and audio signals) und 3 (writing the adjusted time envelope obtained by the decreasing step into an encoding bitstream) nicht bekannt und die übrigen Merkmale insofern nicht, als dass sie nicht im Codierer, sondern im Decodierer
durchgeführt werden.


3.3    Der Gegenstand des Anspruchs 1 des Streitpatents nach dem als ersten gestellten Hilfsantrag ist auch neu gegenüber der technischen Lehre des Dokuments
KÖVESI II (WO 2007/096552 A2) bzw. dem englischsprachigen Familienmitglied
KÖVESI II_E (US 2009/0313009 A1), denn dieses beschäftigt sich nur mit der Reduzierung von Amplituden im Decodierer (KÖVESI II, Fig. 7), nicht jedoch im Codierer. KÖVESI II lehrt eine decodiererseitige Technik zur Unterscheidung, ob ein
Echo vorliegt oder nicht. Insbesondere soll verhindert werden, dass Maßnahmen
zur Unterdrückung eines Echos im Decodierer ergriffen werden, wenn tatsächlich
kein Echo vorliegt (Verhinderung eines „falschen Alarms“) (Abs. 0038 – 0041). Dabei wird mit Hilfe von zeitlichen Einhüllenden unterschieden, in welchen zeitlichen
Abschnitten ein Echo auftritt, sowie, ob Echos in einem niedrigen und/oder einem
hohen Frequenzband auftreten (KÖVESI II, Abs. 0077 – 0092; Fig. 3a). Figur 3d
von KÖVESI II zeigt, wie ein Vor-Echo in dem (Zeit-)Bereich der Abtastwerte 0 bis

                                       - 48 -



etwa 85 durch Anwendung einer Amplitudenverringerung (Pre-echo processing
gain kleiner als 1) verhindert wird (unterstes Diagramm), obwohl der für den hohen
Frequenzbereich verwendete TDAC-Decodierer ein Vor-Echo erzeugt (drittes Diagramm von oben). Eine codiererseitige Reduzierung des Vor-Echos ist somit aus
KÖVESI II nicht bekannt.


3.4    Auch die Dokumente GEISER (vgl. insbesondere Fig. 3), KÖVESI I (vgl. insbesondere Fig. 1), MAHIEUX (vgl. insbesondere Fig. 1), RAGOT (vgl. insbesondere
Fig. 1) und SIEMENS (vgl. insbesondere Fig. 4) zeigen jeweils nur eine Signalveränderung im Decodierer zur Verringerung von Vor-Echo-Effekten.


3.5    Die Dokumente ZHANG I (Fig. 3) und ZHANG II (Fig. 1, 2) zeigen zwar jeweils eine codiererseitige Änderung von Amplituden, jedoch werden dabei die
Amplituden der Abtastwerte aller Zeitabschnitte eines transienten Signals reduziert,
d. h. auch die Amplitude des Zeitabschnitts mit der maximalen Amplitude, so dass
gemäß ZHANG I und ZHANG II – im Gegensatz zum Streitpatent – keine codiererseitige Verstärkung bzw. „Schärfung“ der Charakteristik von transienten Signalen
stattfindet.


3.6    Die Dokumente DAUDET und DUXBURY liegen vom Gegenstand des Anspruchs 1 in der Fassung nach dem als ersten gestellten „unbenannten“ Hilfsantrag
noch weiter weg. Diese Dokumente beschäftigen sich u. a. mit der Trennung von
tonalen und transienten Signalanteilen in Musiksignalen und zeigen insbesondere
keine Amplitudenreduzierung zeitlicher Einhüllender von Subrahmen vor einem Referenz-Subrahmen (wie der Senat in seinem Hinweis vom 11. April 2023 in dem
Nichtigkeitsverfahren das Streitpatent betreffend zum Az.: 4 Ni 79/22 (EP), mit dem
die Parteien sich auseinandergesetzt haben und dessen Ausführungen sie insoweit
nicht entgegengetreten sind, ausführlich dargelegt hat).



4.     Der Gegenstand des Patentanspruchs 1 nach dem als ersten gestellten Hilfsantrag beruht auch auf einer erfinderischen Tätigkeit. Aus keinem der im Verfahren
befindlichen Dokumente ergibt sich ein Verfahren gemäß Anspruch 1 für die Fachperson in naheliegender Weise.

                                       - 49 -




4.1   Wie zur Neuheit des Gegenstands des Anspruchs 1 nach dem als ersten
gestellten „unbenannten“ Hilfsantrag dargelegt und begründet, zeigt das Dokument
MICHAELIS nur einen Teil der Merkmale 1, 1.1, 2, 2.1 und 3, da aus MICHAELIS
insbesondere nicht bekannt ist, Amplitudenwerte von zeitlichen Einhüllenden von
Subrahmen zu bilden und diese zu modifizieren. Die Fachperson hat ausgehend
von den in MICHAELIS genannten LPC- und CELP-Codecs auch keine Veranlassung, anstelle der dort verwendeten spektralen Parameter, zeitliche Einhüllende zu
bilden, zu modifizieren und solchermaßen angepasste zeitliche Einhüllende in einen
codierenden Bitstrom einzuschreiben. Denn zum einen sehen, wie der Fachperson
bekannt ist, Zeitbereichs-Codecs wie LPC und CELP keine Bildung, Codierung und
Übertragung von zeitlichen Einhüllenden vor, und zum anderen ist auch nicht ersichtlich, welcher Veranlassung für die Fachperson bestehen sollte, von der in MI-CHAELIS gelehrten Veränderung der spektralen Amplituden abzuweichen. Dabei
ist zu berücksichtigen, dass sich MICHAELIS nicht mit der Vermeidung von Vor-Echos, sondern mit der Erhöhung der Verständlichkeit relativ leiser Sprachlaute beschäftigt und weiterhin, dass MICHAELIS keine Transformations-Codecs erwähnt,
welche Vor-Echos verursachen, und bei den verwendeten Zeitbereichs-Codecs
(LPC und CELP) keine Vor-Echos auftreten.

Angesichts dieser gravierenden Unterschiede kann dahinstehen, ob die Fachperson ausgehend von MICHAELIS Veranlassung hatte, allein eine feinere zeitliche
Unterteilung in Subrahmen statt Rahmen vorzunehmen.

Auch die weiteren im Verfahren befindlichen Druckschriften liefern der Fachperson
keinen Anlass, die technische Lehre von MICHAELIS in Richtung des Gegenstands
des Anspruchs 1 nach Streitpatent abzuändern.


4.2   Wie zum Hauptantrag (erteilte Fassung) dargelegt und begründet, ist aus
dem Dokument SONY der Gegenstand des Anspruchs 6 erteilter Fassung, d. h. die
decodiererseitige Verstärkung bzw. „Schärfung“ des transienten Signalcharakters
zur Verminderung von Vor-Echos bekannt.

                                       - 50 -



SONY geht von zwei bekannten codiererseitigen Maßnahmen zur Reduzierung des
Vor-Echos aus, nämlich der Abflachung der transienten Signale, inklusive des maximalen Amplitudenwerts, gemäß ATRAC3- bzw. ATRAC X-Codierer (und entsprechende Umkehrung der Abflachung im Decodierer) und der Umschaltung auf eine
kürzere Blocklänge bei transienten Signalen gemäß MP3-Codierer. SONY erkennt
in beiden bekannten Ansätzen Nachteile und entscheidet sich zu deren Überwindung ausdrücklich für ein decodiererseitiges Verfahren, das in einer Rauschreduktionseinheit durchgeführt wird, die einem Decodierer gemäß ATRAC bzw. gemäß
MP3 nachgeschaltet ist, so dass weiterhin die Codierer und Decodierer gemäß den
entsprechenden Standards genutzt werden können.

Es ist nicht ersichtlich, weshalb die Fachperson von dieser Lösung abweichen sollte
und – streitpatentgemäß – den Codierer selbst insofern ändern sollte, als dort zeitliche Einhüllende von Subrahmen vor einem ermittelten Referenz-Subrahmen in ihrer Amplitude reduziert werden und diese geänderten Amplitudenwerte in den Bitstrom des Codierers einfließen.

Eine Motivation, den Decodierer „einfach“ zu halten und die in SONY gezeigte decodiererseitige Vor-Echo-Reduzierung auf die Codiererseite zu „verschieben“ besteht nicht. Zunächst sind bei den hier im Vordergrund stehenden Anwendungen
der Sprach-Codecs in Mobilfunksystemen regelmäßig Basisstationen und Mobilstationen mit denselben Codecs ausgestattet, insbesondere umfasst die Mobilstation
selbstverständlich Codierer und Decodierer, um Sprachsignale senden und empfangen zu können. Insofern führt eine Verlagerung einer bestimmten Lösung vom
Decodierer zum Codierer (oder umgekehrt) zu keiner Verringerung des Gesamtaufwands für eine Mobilstation.

Weiter trifft es zwar zu, dass die Entwicklung von Sprach-Codecs stets Codierer und
Decodierer gemeinsam betrachtet und optimiert und teilweise ähnliche Hard- und
Software auf beiden Seiten verwendet. Dennoch gibt es selbstverständlich spezifische Unterschiede und Besonderheiten von Codierern und Decodierern, die eine
einfache Übertragung „von der einen auf die andere Seite“ erschweren oder sogar
verhindern.

                                        - 51 -



So verhält es sich auch hier. Der Versuch, die aus SONY bekannte, dem Decodierer
nachgeschaltete Rauschreduktionsvorrichtung in den Codierer zu verschieben,
würde bei den in SONY ausschließlich thematisierten Frequenzbereich-Codecs
(ATRAC, MP3) dazu führen, dass in einer dem Frequenzbereich-Codierer vorgelagerten Schaltung Amplitudenwerte von Subrahmen vor dem Referenz-Subrahmen
zu reduzieren wären. Diese Art der codiererseitigen Verstärkung des transienten
Signalcharakters würde jedoch in der nachfolgenden Transformationscodierung zu
einer Verstärkung statt zu einer Reduzierung des Vor-Echos führen, weswegen die
Fachperson einen solchen Ansatz im Codierer als unergiebig bzw. wegen der unerwünschten Wirkung mit erforderlichem Mehraufwand als sinnlos verwerfen würde.
Wie zur Auslegung dargelegt, geht das Streitpatent auf der Codiererseite einen anderen Weg, in dem es die modifizierten zeitlichen Einhüllenden parallel mit den
durch Transformationscodierung gewonnenen spektralen Einhüllenden überträgt,
so dass gemäß Streitpatent die Amplitudenreduzierung im Codierer gerade nicht zu
einer Erhöhung des Vor-Echos im transformationscodierten oberen Frequenzbereich führt.


4.3      Aus den gleichen Gründen gelangt die Fachperson auch nicht in naheliegender Weise ausgehend von den decodiererseitigen Implementierungen, wie sie aus
KÖVESI II, GEISER, RAGOT und SIEMENS bekannt sind, zu einer codiererseitigen
Implementierung.

Da KÖVESI II explizit den Codierer einfach halten möchte (Abs. 0038) wird die
Fachperson die speziell auf den Decodierer ausgerichtete technische Lehre von
KÖVESI II nicht auf den Codierer übertragen. Auch der in Abs. 0016 von KÖVESI II
enthaltende Hinweis auf das Dokument MAHIEUX liefert der Fachperson keine Veranlassung zur Übertragung der decodiererbezogenen Lehre von KÖVESI II auf den
Codierer, denn auch MAHIEUX reduziert Vor-Echos im Decodierer (MAHIEUX, S.
103, Abschnitt VI.1. Preecho reduction by Kalman filtering … This filtering operates
at the decoder on the reconstructed samples which are located before the transient.).

                                            - 52 -



4.4    Weiter ist nicht ersichtlich, weshalb die Fachperson die aus ZHANG I und
ZHANG II bekannte codiererseitige Amplitudenkompression aller Zeitabschnitte eines transienten Signals durch eine Amplitudenreduzierung nur der zeitlichen Einhüllenden der vom dem Referenz-Subrahmen liegenden Subrahmen ändern sollte,
denn dies würde – wie unter Abschnitt 4.2 zu SONY dargelegt – zu einer unerwünschten Vergrößerung des Vor-Echos führen.




                                             B.
                               Nebenentscheidungen

I.     Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs.1 ZPO,
§ 269 Abs. 3 Satz 2 ZPO und § 100 Abs. 1 ZPO i. V. m. § 99 Abs.1 PatG.

1.     In dem verbundenen Nichtigkeitsverfahren ist eine einheitliche Kostenentscheidung zu treffen (Grundsatz der Einheit der Kostenentscheidung), weshalb die
Klägerin zu 2 trotz Klagerücknahme hinsichtlich des Kostenausspruchs weiter am
Verfahren beteiligt ist.


2.     Der Kostenentscheidung hat der Senat zugrunde gelegt, dass beide Klägerinnen das Streitpatent insgesamt angreifen und der Wert ihrer Klageangriffe demzufolge jeweils gleich zu beurteilen ist.

Der nach der Klage der Klägerin zu 1 als schutzfähig verbleibende Patentgegenstand ist nach der beschränkt verteidigten Fassung nach dem als ersten gestellten
(unbenannten) Hilfsantrag gegenüber demjenigen der erteilten Fassung durch die
Beschränkung auf die codiererseitigen Patentansprüchen 1 bis 5, 10 bis 14 und 17
nicht nur geringfügig eingeschränkt. Diese Einschränkung macht nach Ansicht des
Senats die Hälfte der wirtschaftlichen Verwertbarkeit des von der Klägerin zu 1 angegriffenen Streitpatents aus. Infolgedessen haben die Beklagten und die Klägerin
zu 1 bezogen auf den verbleibenden Patentgegenstand jeweils den gleichen Anteil
zu tragen.

                                         - 53 -



Hinsichtlich der außergerichtlichen Kosten der Beklagten haften die Klägerinnen
nach Kopfteilen im Umfang der Klagerücknahme bzw. ihres Unterliegens.

Nachdem die Klägerin zu 2 ihre Klage zurückgenommen hat, wären ihr demnach
insoweit anteilig die Kosten aufzuerlegen, § 269 Abs. 3 Satz 2 ZPO; die Klägerin
zu 2 hätte daher die Hälfte der außergerichtlichen Kosten der Beklagten zu tragen,
§ 269 Abs. 3 Satz 2 ZPO i. V. m. § 99 Abs. 1 PatG. Eine Entscheidung über die
außergerichtlichen Kosten der Beklagten, soweit diese von der Klägerin zu 2 zu
tragen wären, ist jedoch nicht veranlasst. Nach Rücknahme der Klage ist gemäß
§ 269 Abs. 4 ZPO nur auf Antrag über die Kosten zu entscheiden. Einen dahingehenden Antrag gegenüber der Klägerin zu 2 hat die Beklagte nicht gestellt.

Soweit der in der mündlichen Verhandlung am 24. Oktober 2022 verkündete Tenor
eine Kostenentscheidung zu Lasten der Klägerin zu 2 enthalten hat, handelt es sich
um eine offenbare Unrichtigkeit im Sinne von § 95 PatG bzw. § 319 Abs. 1 ZPO, die
von Amts wegen zu berichtigen ist. Schon aus dem Tatbestand ergibt sich eindeutig,
dass die Beklagte betreffend die Klägerin zu 2 keinen Antrag und damit auch keinen
Kostenantrag gestellt hat. Die Berichtigung kann zugleich mit der Erstellung der
schriftlichen Urteilsfassung erfolgen; ein gesonderter Berichtigungsbeschluss ist insoweit nicht notwendig (vgl. Schulte, PatG, 11. Aufl., § 95 Rn. 8).

Die Klägerin zu 1 hat die Kosten im Umfang ihres Unterliegens zu tragen, § 84
Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO; die Klägerin zu 1 hat daher den hälftigen Anteil der verbliebenen Hälfte der außergerichtlichen Kosten der Beklagten, also ein
Viertel dieser Kosten zu tragen. Die Beklagte hat insoweit im Umfang ihres Unterliegens ein Viertel (den hälftigen Unterliegensanteil hinsichtlich des hälftigen Anteils
des verbliebenden Streitpatents) ihrer außergerichtlichen Kosten selbst zu tragen.

Schließlich hat die Beklagte entsprechend ihrem Unterliegen anteilig die Hälfte der
außergerichtlichen Kosten der Klägerin zu 1 zu tragen, § 84 Abs. 2 PatG i. V. m.
§ 92 Abs. 1 ZPO, die darüber hinaus ihre Kosten selbst zu tragen hat.


3.     Hinsichtlich der Gerichtskosten war hingegen gemäß § 308 Abs. 2 ZPO auch
ohne Antrag der Beklagten insgesamt im Urteil eine Entscheidung zu treffen, weil

                                        - 54 -



die Klagerücknahme nicht den gesamten Streitgegenstand betrifft (vgl. BGH, Beschluss vom 28. Januar 1999 - III ZB 39/89, NJW-RR 1999, 1741).

Die Klägerinnen haften jedoch insoweit hier nicht gesamtschuldnerisch, da die Voraussetzungen des § 100 Abs. 4 ZPO nicht erfüllt sind, denn die Klägerinnen sind
in der Hauptsache nicht als Gesamtschuldnerinnen verurteilt worden.

Danach haben von den Gerichtskosten die Klägerin zu 2 die Hälfte und die Klägerin
zu 1 sowie die Beklagte jeweils ein Viertel zu tragen.

Eine abweichende Kostenregelung, die nach dem letzten Halbsatz des § 269 Abs. 3
Satz 2 ZPO auch im vorliegenden Zusammenhang relevant wäre, ist nicht ersichtlich. Die Ankündigung der Beklagten, gegen die Klägerin zu 2 keinen Kostenantrag
zu stellen, bildet keinen anderen Grund im Sinne von § 269 Abs. 3 Satz 2 ZPO. Sie
kann in der vorliegenden Konstellation allenfalls dazu führen, dass die Beklagte daran gehindert wäre, gegen die Klägerin zu 2 einen Antrag auf Kostenfestsetzung zu
stellen.


4.     Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99
Abs. 1 PatG i. V. m. § 709 ZPO.




                                         C.
                              Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift, die auch als elektronisches Dokument eingereicht werden
kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung nach den hierfür geltenden gesetzlichen Bestimmungen elektronisch signiert sein, d. h. mit einer qualifizierten elektronischen Signatur nach dem
Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur versehen
sein, die von einer internationalen Organisation auf dem Gebiet des gewerblichen

                                       - 55 -



Rechtsschutzes herausgegeben wird und sich zur Bearbeitung durch das jeweilige
Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das
die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil
Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.


Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches Dokument in die elektronische Poststelle des Bundesgerichtshofes (Informationen unter
www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt
mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber
mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt,
wenn die Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Werner            Altvater             Matter             Dr. Haupt           Berner

                                   - 56 -



Bundespatentgericht


       4 Ni 8/23 (EP)
        verbunden mit

       4 Ni 10/23 (EP)
         (Aktenzeichen)




Verkündet am

16. Oktober 2024

…

Justizbeschäftigte
als Urkundsbeamtin der Geschäftsstelle
