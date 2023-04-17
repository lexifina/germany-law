---
ecli: "ECLI:DE:BPatG:2023:170423U5Ni42.20EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 42/20"
decided: "2023-04-17"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=10&nr=43692&anz=529&pos=154&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-04-17_5_Ni_42_20_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0167.md", "germany/bund/acts/zpo/0253.md", "germany/bund/acts/zpo/0261.md", "germany/bund/acts/zpo/0263.md", "germany/bund/acts/zpo/0269.md", "germany/bund/acts/zpo/0286.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 42/20 vom 2023-04-17

## Entscheidung

BUNDESPATENTGERICHT
                         IM NAMEN DES VOLKES

                                    URTEIL

                                                          Verkündet am

                                                           17.04.2023
       5 Ni 42/20 (EP)
       (Aktenzeichen)                                          …




                         In der Patentnichtigkeitssache
…




ECLI:DE:BPatG:2023:170423U5Ni42.20EP.0

                                               -2-




                      betreffend das europäische Patent 1 565 036
                                    (DE 60 2005 053 100)


     hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
     mündlichen Verhandlung vom 17. April 2023 durch den Richter Heimen als
     Vorsitzenden sowie die Richter Schödel, Dipl.-Geophys. Univ. Dr. Wollny, Dipl.-
     Phys. Univ. Bieringer und Dr.-Ing. Ball


     für Recht erkannt:


I.      Das europäische Patent EP 1 565 036 wird mit Wirkung für das Hoheitsgebiet
        der Bundesrepublik Deutschland mit der Maßgabe für nichtig erklärt, dass
        seine Patentansprüche folgende Fassung erhalten:


        1. A method of audio processing for synthesizing an auditory scene,
        comprising:


        processing (702) at least one input channel (312), using an auditory filter bank
        block (702), to generate two or more processed input signals (704);

                                      -3-




filtering (720) the at least one input channel (312), using a filter (720) that
models late reverberation (LR), to generate corresponding two or more LR-
filtered diffuse signals (722); and


for each of the two or more processed input signals and each of the
corresponding two or more diffuse signals, combining (714) one of the two or
more LR-filtered diffuse signals with a corresponding one of the two or more
processed input signals to generate one of a plurality of output channels (324)
for the auditory scene,


the method further comprising:


converting (702) the at least one input channel (312) from a time domain into a
frequency domain to generate a plurality of frequency-domain (FD) input
signals (704); and


wherein processing (702) the at least one input channel (312) comprises:
delaying (706) and scaling (710) the FD input signals to generate a plurality of
scaled, delayed FD signals (712) as processed input signals,


wherein each FD input signal is delayed at a corresponding delay block based
on delay values derived from corresponding inter-channel time difference data,
and


wherein each delayed FD input signal is scaled by a corresponding multiplier
based on scale factors derived from corresponding inter-channel level
difference data.


2. The method of claim 1, wherein:


the LR-filtered diffuse signals (722) are FD diffuse signals; and

                                     -4-




the combining (714) comprises, for each output channel:


summing (714) one of the scaled, delayed FD signals (712) and a
corresponding one of the FD diffuse signals (730) to generate an FD output
signal (716); and


converting (718) the FD output signal (716) from the frequency domain into the
time domain to generate one of a plurality of output channels (324).


3. The method of claim 2, wherein filtering (720) the at least one input channel
(312) comprises:


applying two or more late reverberation filters (720) to the at least one input
channel (312) to generate a plurality of LR-filtered diffuse signals (722);


converting (724) the LR-filtered diffuse signals (712) from the time domain into
the frequency domain to generate a plurality of FD diffuse signals (726); and


scaling (728) the FD diffuse signals (726) to generate a plurality of scaled FD
diffuse signals (730), wherein the scaled FD diffuse signals (730) are combined
with the scaled, delayed FD signals (712) to generate the FD output signals
(716).


4. The method of claim 1, wherein filtering the at least one input channel
comprises:


applying two or more FD late reverberation filters to the FD input signals to
generate a plurality of diffuse FD signals; and

                                      -5-




scaling the diffuse FD signals to generate a plurality of scaled diffuse FD
signals, wherein the scaled diffuse FD signals are combined with the scaled,
delayed FD signals to generate an FD output signal.


5. The method of claim 1, wherein the method:


applies the processing, filtering, and combining for input channel frequencies
less than a specified threshold frequency; and


further applies alternative auditory scene synthesis processing for input
channel frequencies greater than the specified threshold frequency.


6. The method of claim 5, wherein the alternative auditory scene synthesis
processing involves coherence-based binaural cue coding (BCC) without the
filtering that is appliedto the input channel frequencies less than the specified
threshold frequency.


7. Apparatus (322) for audio processing including synthesizing an auditory
scene,
comprising:


means (702) for processing at least one input channel (312) to generate two or
more processed input signals (704);


means (720) for filtering the at least one input channel (312), using a filter that
models late reverberation (LR) to generate corresponding two or more LR-
filtered diffuse signals (722); and


means (714) for combining, for each of the two or more processed input
signals and each of the corresponding two or more diffuse signals, one of the
two or more LR-filtered diffuse signals with a corresponding one of the two or

                                     -6-




more processed input signals to generate one of a plurality of output channels
(324) for the auditory scene,


wherein the means for processing the at least one input channel is configured


   to convert (702) the at least one input channel (312) from a time domain
   into a frequency domain to generate a plurality of frequency-domain (FD)
   input signals (704); and


   to delay (706) and scale (710) the FD input signals to generate a plurality of
   scaled, delayed FD signals (712) as processed input signals,


   wherein each FD input signal is delayed at a corresponding delay block
   based on delay values derived from corresponding inter-channel time
   difference data, and


   wherein each delayed FD input signal is scaled by a corresponding
   multiplier based on scale factors derived from corresponding inter-channel
   level difference data.


8. Apparatus (322) for audio processing including synthesizing an auditory
scene, comprising:


a configuration of at least one time domain (TD) to frequency domain (FD)
converter (702) and a plurality of filters (720) that model late reverberation
(LR), the configuration adapted to generate two or more processed FD input
signals (704) and corresponding two or more LR-filtered diffuse FD signals
(722) from at least one TD input channel (312), wherein each FD input signal is
delayed at a corresponding delay block based on delay values derived from
corresponding inter-channel time difference data, and wherein each delayed

                                            -7-




       FD input signal is scaled by a corresponding multiplier based on scale factors
       derived from corresponding inter-channel level difference data;


       two or more combiners (714), each being adapted to combine one of the two or
       more LR-filtered diffuse FD signals (730) with a corresponding one of the two
       or more processed FD input signals (712) to generate a plurality of synthesized
       FD signals (716); and


       two or more frequency domain to time domain (FD-TD) converters (718), each
       adapted to convert one of the synthesized FD signals (716) into one of a
       plurality of TD output channels (324) for the auditory scene.


       9. The apparatus of claim 8, wherein at least two filters (720) have different
       filter lengths.


       Im Übrigen wird die Klage abgewiesen.


 II.   Von den Gerichtskosten trägt die Klägerin zu 1) 1/2, die Beklagte 1/6 und die
       Klägerin zu 2) 1/3. Von den außergerichtlichen Kosten der Beklagten trägt die
       Klägerin zu 2) 2/3, von den außergerichtlichen Kosten der Klägerin zu 2) trägt
       die Beklagte 1/3. Im Übrigen tragen die Parteien ihre außergerichtlichen
       Kosten selbst.


III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des jeweils zu
       vollstreckenden Betrages vorläufig vollstreckbar.




                                        Tatbestand


   Die Beklagte ist Inhaberin des europäischen Patents 1 565 036 (Streitpatent), das
   – unter Inanspruchnahme der Priorität der US 544 287 P vom 12. Februar 2004 und

                                         -8-




der US 815 591 vom 1. April 2004 – am 4. Februar 2005 angemeldet worden ist.
Die Erteilung des europäischen Patents ist am 22. November 2017 veröffentlicht
worden. Das in englischer Sprache gefasste Streitpatent trägt die Bezeichnung
“LATE REVERBERATION-BASED SYNTHESIS OF AUDITORY SCENES“, ins
Deutsche übersetzt “AUF SPÄTEM NACHHALL BASIERTE SYNTHESE VON
HÖRSZENARIEN”. Es ist in Kraft und umfasst in der geltenden Fassung insgesamt
zehn Patentansprüche mit dem Verfahrensanspruch 1 und auf diesen unmittelbar
und mittelbar zurückbezogenen Unteransprüchen 2 bis 7, den nebengeordneten
Vorrichtungsansprüchen 8 und 9 sowie den auf Anspruch 9 zurückbezogenen
Unteranspruch 10.


Die Klägerin zu 1) hat am 12. Oktober 2020 Klage auf vollständige Nichtigerklärung
des Streitpatents eingereicht. Die Klägerin zu 2) hat mit Schriftsatz vom 28. Oktober
2020, eingegangen bei Gericht am selben Tag, den Beitritt zur Nichtigkeitsklage der
Klägerin zu 1) erklärt. Die Klägerin zu 1) hat dem Beitritt am 29. Oktober 2020
zugestimmt und am 30. Oktober 2020 ihre eigene Klage zurückgenommen. Die
Beklagte hat dieser Klagerücknahme am selben Tag zugestimmt. Die erste
Nichtigkeitsklage ist der Beklagten am 5. November 2020, der Schriftsatz der
Klägerin zu 2) vom 28. Oktober 2020 am 12. November 2020 zugestellt worden.


Die Klägerin zu 2) begehrt ebenfalls die vollständige Nichtigerklärung des
Streitpatents.


Die erteilten unabhängigen Ansprüche 1, 8 und 9 können wie folgt gegliedert
werden:


                                                 Übersetzung laut Streitpatent
1.1    A method of audio processing for          Verfahren des Audio-Verarbeitens zum
       synthesizing an auditory scene,           Synthetisieren einer auditiven Szene,
       comprising:                               das Verfahren aufweisend:
1.2    processing (702) at least one input       Verarbeiten (702) von mindestens einem
       channel (312), using an auditory filter   Eingangskanal (312), unter Verwendung

                                        -9-




      bank block (702), to generate two or eines Auditiv-Filterbank-Blocks (702),
      more processed input signals (704); um zwei oder mehr verarbeitete
                                               Eingangssignale (704) zu erzeugen;
1.3   filtering (720) the at least one input Filtern (720) des mindestens einen
      channel (312), using a filter (720) that Eingangkanals (312), unter Verwendung
      models late reverberation (LR), to eines Filters (720), der späten Widerhall
      generate corresponding two or more (LR) modelliert, um entsprechende zwei
      LR-filtered diffuse signals (722); and oder mehr LR-gefilterte, diffuse Signale
                                               (722) zu erzeugen; und
1.4   for each of the two or more für jedes der zwei oder mehr
      processed input signals and each of verarbeiteten        Eingangssignale    und
      the corresponding two or more jedes der entsprechenden zwei oder
      diffuse signals, combining (714) one mehr diffusen Signale, Kombinieren
      of the two or more LR-filtered diffuse (714) von einem der zwei oder mehr LR-
      signals with a corresponding one of gefilterten, diffusen Signale mit einem
      the two or more processed input entsprechenden einen der zwei oder
      signals to generate one of a plurality mehr verarbeiteten Eingangssignale, um
      of output channels (324) for the einen von einer Mehrzahl von
      auditory scene.                          Ausgangskanälen (324) für die auditive
                                               Szene zu erzeugen.

                                                Übersetzung laut Streitpatent
8.1   Apparatus (322) for audio processing      System (322) zum Audio-Verarbeiten
      including synthesizing an auditory        einschließlich eines Synthetisierens
      scene, comprising:                        einer auditiven Szene, die Vorrichtung
                                                aufweisend:
8.2   means (702) for processing at least       Mittel (702) zum Verarbeiten von
      one input channel (312) to generate       mindestens einem Eingangskanal (312),
      two or more                               um zwei oder mehr verarbeitete
      processed input signals (704);            Eingangssignale (704) zu erzeugen;
8.3   means (720) for filtering the at least    Mittel (720) zum Filtern des mindestens
      one input channel (312), using a filter   einen Eingangskanals (312), unter
      that models late reverberation (LR) to    Verwendung eines Filters, der späten
      generate corresponding two or more        Widerhall      (LR)    modelliert,  um
      LR-filtered diffuse signals (722); and    entsprechende zwei oder mehr LR-
                                                gefilterte, diffuse Signale (722) zu
                                                erzeugen; und
8.4   means (714) for combining, for each       Mittel (714) zum Kombinieren, für jedes
      of the two or more processed input        der zwei oder mehr verarbeiteten
      signals    and    each    of    the       Eingangssignale      und    jedes   der

                                      - 10 -




      corresponding two or more diffuse        entsprechenden zwei oder mehr diffusen
      signals, one of the two or more LR-      Signale, von einem der zwei oder mehr
      filtered diffuse signals with a          LR-gefilterten, diffusen Signale mit
      corresponding one of the two or more     einem entsprechenden einen der zwei
      processed input signals to generate      oder           mehr         verarbeiteten
      one of a plurality of output channels    Eingangssignale, um einen von einer
      (324) for the auditory scene.            Mehrzahl von Ausgangskanälen (324)
                                               für die auditive Szene zu erzeugen.

                                               Übersetzung laut Streitpatent
9.1   Apparatus (322) for audio processing     System (322) zum Audio-Verarbeiten
      including synthesizing an auditory       einschließlich eines Synthetisierens
      scene, comprising:                       einer auditiven Szene, die Vorrichtung
                                               aufweisend:
9.2   a configuration of at least one time     eine Konfiguration von mindestens
      domain (TD) to frequency domain          einem           Zeitbereich      (TD)-in-
      (FD) converter (702) and a plurality     Frequenzbereich (FD)-Umwandler (702)
      of filters (720) that model late         und einer Mehrzahl von Filtern (720), die
      reverberation (LR), the configuration    späten Wiederhall (LR) modellieren,
      adapted to generate two or more          wobei die Konfiguration ausgebildet ist,
      processed FD input signals (704)         um zwei oder mehr verarbeitete FD-
      and corresponding two or more LR-        Eingangssignale           (704)       und
      filtered diffuse FD signals (722) from   entsprechende zwei oder mehr LR-
      at least one TD input channel (312);     gefilterte, diffuse FD-Signale (722) aus
                                               mindestens einem TD-Eingangskanal
                                               (312) zu erzeugen;
9.3   two or more combiners (714), each        zwei oder mehr Kombinierer (714),
      being dapted to combine one of the       wobei jeder ausgebildet ist, um eines der
      two or more LR-filtered diffuse FD       zwei oder mehr LR-gefilterten, diffusen
      signals (730) with a corresponding       FD-Signale        (730)     mit    einem
      one of the two or more processed FD      entsprechenden einen der zwei oder
      input signals (712) to generate a        mehr verarbeiteten, FD-Eingangssignale
      plurality of synthesized FD signals      (712) zu kombinieren, um eine Mehrzahl
      (716); and                               von synthetisierten FD-Signalen (716)
                                               zu erzeugen; und
9.4   two or more frequency domain to          zwei oder mehr Frequenzbereich-intime domain (FD-TD) converters           Zeitbereich (FD-TD)-Umwandler (718),
      (718), each adapted to convert one       wobei jeder ausgebildet ist, um eines der
      of the synthesized FD signals (716)      synthetisierten FD-Signale (716) in
      into one of a plurality of TD output     einen von einer Mehrzahl von TD-

                                       - 11 -




       channels (324) for the auditory Ausgangskanälen (324) für die auditive
       scene.                          Szene umzuwandeln.



Wegen des Wortlauts der mittelbar oder unmittelbar auf den Anspruch 1
rückbezogenen Ansprüche 2 bis 7 und des auf Anspruch 9 rückbezogenen
Anspruchs 10 wird auf die Streitpatentschrift verwiesen.


Die Klägerin zu 2) macht die Nichtigkeitsgründe der unzulässigen Erweiterung (Art.
II § 6 Absatz 1 Nr. 3 IntPatÜG, Art. 138 Absatz 1 Buchst. c) EPÜ) sowie der
mangelnden Neuheit und der mangelnden erfinderischen Tätigkeit (Art. II § 6 Absatz
1 Nr. 1 IntPatÜG, Art. 138 Absatz 1 Buchst. a) i. V. m. Art. 54, 56 EPÜ) geltend. Sie
stützt ihren Vortrag u.a. auf die nachfolgenden Druckschriften:


NK1   FALLER, C.: PARAMETRIC CODING OF SPATIAL AUDIO. THÈSE NO
      3062 (2004); ÉCOLE POLYTECHNIQUE FÉDÉRALE DE LAUSANNE,
      PRÉSENTÉE À LA FACULTÉ INFORMATIQUE ET COMMUNICATIONS,
      Institut de systèmes de communication, SECTION DES SYSTÈMES DE
      COMMUNICATION, POUR L'OBTENTION DU GRADE DE DOCTEUR ÈS
      SCIENCES, 164 S.
NK2   WO 99 / 14 983 A1
NK3   US 5 371 799 A
NK4   US 6 658 117 B2
NK5   SMITH, J.O.; ABEL, S.: Bark and ERB Bilinear Transforms; In: IEEE
      TRANSACTIONS ON SPEECH AND AUDIO PROCESSING, VOL. 7, NO. 6,
      NOVEMBER 1999, S. 697 - 708
NK6   BAUMGARTE, F.: Ein psychophysiologisches Gehörmodel zur Nachbildung
      von Wahrnehmungsschwellen für die Audiocodierung. Vom Fachbereich
      Elektrotechnik und Informationstechnik der Universität Hannover zur
      Erlangung    des   akademischen      Grades    Doktor-Ingenieur   genehmigte
      Dissertation, 2000, 163 S.

                                       - 12 -




NK7   PAN, D.: A Tutorial on MPEG Audio Compression. In: IEEE Multimedia,
      Volume: 2, Issue: 2, Summer 1995. S. 60 – 74
NK8   CHEN, W.-K. [Hrsg.]: The circuits and filters handbook. 2. Auflage, 2003,
      ISBN: 0-8493-0912-3; Preface et al: 7 S., Inhaltsverzeichnis: 8 S., Kap. 4.8:
      6 S.
NK9   US 2003 / 0 219 130 A1
NK10 US 2003 / 0 026 441 A1
NK11 JERUCHIM, M.C. et al.: Simulation of Communication Systems, Modeling
      Methodology and Techniques, 2. Aufl., 2002. Kluwer Academic Publ.;
      NewYork; Boston; S. i – xiv, 8 – 12, 152 – 154.


Auf den qualifizierten Hinweis des Senats vom 17. Januar 2023 hat die Beklagte zur
hilfsweisen Verteidigung des Streitpatents mit Schriftsatz vom 27. Februar 2023
insgesamt 23 Hilfsanträge (1 bis 9B) eingereicht.


Der Vorrichtungsanspruch 1 nach Hilfsantrag 1 enthält gegenüber der erteilten
Fassung in dem Merkmal 1.2 nach obiger Gliederung folgenden Zusatz (Änderung
gegenüber erteiltem Anspruch 1 fettgedruckt):


   1.21   processing (702) at least one input channel (312), using an auditory filter
          bank block (702) performing a time-frequency transform, to generate
          two or more processed input signals (704);


Der Verfahrensanspruch 8 gemäß Hilfsantrag 1 wird entsprechend ergänzt.


Nach Hilfsantrag 2 werden dem Vorrichtungsanspruch 1 am Ende folgende
Merkmale angefügt (Gliederung durch den Senat):


   1.52   converting (702) the at least one input channel (312) from a time domain
          into a frequency domain to generate a plurality of frequency-domain (FD)
          input signals (704); and

                                           - 13 -




   1.62     wherein processing (702) the at least one input channel (312) comprises:
            delaying (706) and scaling (710) the FD input signals to generate a
            plurality of scaled, delayed FD signals (712) as processed input signals.


Der Verfahrensanspruch 7 gemäß Hilfsantrag 2 (vormals Anspruch 8) wird
entsprechend ergänzt.


Nach Hilfsantrag 2A werden dem Anspruch 1 in der Fassung des Hilfsantrags 2 am
Ende weiter folgende Merkmale angefügt (Gliederung durch den Senat):


   1.6.12A     wherein each FD input signal is delayed at a corresponding delay
               block based on delay values derived from corresponding inter-channel
               time difference data, and
   1.6.22A     wherein each delayed FD input signal is scaled by a corresponding
               multiplier based on scale factors derived from corresponding interchannel level difference data.


Die unabhängigen Ansprüche 7 und 8 gemäß Hilfsantrag 2A (vormals Ansprüche 8
und 9) erhalten folgende Fassung:


   7. Apparatus (322) for audio processing including synthesizing an auditory
   scene,
   comprising:


   means (702) for processing at least one input channel (312) to generate two or
   more processed input signals (704);


   means (720) for filtering the at least one input channel (312), using a filter that
   models late reverberation (LR) to generate corresponding two or more LR-
   filtered diffuse signals (722); and

                                     - 14 -




means (714) for combining, for each of the two or more processed input
signals and each of the corresponding two or more diffuse signals, one of the
two or more LR-filtered diffuse signals with a corresponding one of the two or
more processed input signals to generate one of a plurality of output channels
(324) for the auditory scene,


wherein the means for processing the at least one input channel is configured


   to convert (702) the at least one input channel (312) from a time domain
   into a frequency domain to generate a plurality of frequency-domain (FD)
   input signals (704); and


   to delay (706) and scale (710) the FD input signals to generate a plurality of
   scaled, delayed FD signals (712) as processed input signals,


   wherein each FD input signal is delayed at a corresponding delay block
   based on delay values derived from corresponding inter-channel time
   difference data, and


   wherein each delayed FD input signal is scaled by a corresponding
   multiplier based on scale factors derived from corresponding inter-channel
   level difference data.


8. Apparatus (322) for audio processing including synthesizing an auditory
scene, comprising:


a configuration of at least one time domain (TD) to frequency domain (FD)
converter (702) and a plurality of filters (720) that model late reverberation
(LR), the configuration adapted to generate two or more processed FD input
signals (704) and corresponding two or more LR-filtered diffuse FD signals
(722) from at least one TD input channel (312), wherein each FD input signal is

                                        - 15 -




   delayed at a corresponding delay block based on delay values derived from
   corresponding inter-channel time difference data, and wherein each delayed
   FD input signal is scaled by a corresponding multiplier based on scale factors
   derived from corresponding inter-channel level difference data;


   two or more combiners (714), each being adapted to combine one of the two or
   more LR-filtered diffuse FD signals (730) with a corresponding one of the two
   or more processed FD input signals (712) to generate a plurality of synthesized
   FD signals (716); and


   two or more frequency domain to time domain (FD-TD) converters (718), each
   adapted to convert one of the synthesized FD signals (716) into one of a
   plurality of TD output channels (324) for the auditory scene.


Wegen der Fassung der Ansprüche im Übrigen und den weiteren Anspruchssätzen
gemäß den Hilfsanträgen 2B bis 9B wird auf die Akte verwiesen.


Die Klägerin zu 2) ist der Ansicht, die Klage sei zulässig, ihre Beitrittserklärung zur
anschließend zurückgenommenen Klage der Klägerin zu 1) sei wirksam. Es
handele sich hierbei um eine Klageänderung, die im Umkehrschluss aus § 263 ZPO
vor Zustellung der Klage der Klägerin zu 1) an die Nichtigkeitsbeklagte ohne
Weiteres     zulässig    sei.   Zudem      müsse      der    Popularcharakter      der
Patentnichtigkeitsklage beachtet werden.
Sie vertritt zu den Nichtigkeitsgründen die Auffassung, dass die Gegenstände der
erteilten Ansprüche 1 und 8 jeweils unzulässig erweitert seien. Deshalb seien auch
die auf den Anspruch 1 rückbezogenen abhängigen Ansprüche ebenfalls
unzulässig erweitert. Zudem gingen die abhängigen Ansprüche 2 bis 7 selbst über
den Inhalt der ursprünglich eingereichten Unterlagen hinaus. Die erteilten
Ansprüche 1, 8 und 9 seien nicht patentfähig, insbesondere vom Gegenstand der
Druckschriften NK1 bis NK4 neuheitsschädlich getroffen.

                                       - 16 -




Sie meint, die Beklagte könne nicht die Priorität der Patentanmeldungen US 544
287 P vom 12. Februar 2004 und der US 815 591 vom 1. April 2004 in Anspruch
nehmen. Sie bestreitet, dass das Patent von den Erfindern Frank Baumgarte und
Christof Faller wirksam auf die Agere Systems Inc., eine Rechtsvorgängerin der
Beklagten, übertragen worden sei. Bei dem beim US-amerikanischen Patentamt
(USPTO) hierzu hinterlegten Dokument (Anlage G5) handele es sich um keinen
einheitlichen, zusammenhängenden Vertrag. Die von den beiden Erfindern im
Rahmen dieses Verfahrens abgegebenen Erklärungen zur Übertragung des
Patents enthielten keinen Vertragstext, so dass ihnen keine Informationen zu dem
Rechtsübergang zu entnehmen seien, die nachgereichten Erklärungen seien auch
nicht glaubhaft. Deshalb habe die Dissertation des Erfinders (NK1) auch als
vorveröffentlichter Stand der Technik zu gelten.

Die Klägerin zu 2) beantragt,

      das europäische Patent EP 1 565 036 mit Wirkung für das Hoheitsgebiet der
      Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,


      die Klage abzuweisen,


      hilfsweise die Klage mit der Maßgabe abzuweisen, dass das Streitpatent die
      Fassung eines der Hilfsanträge 1 bis 9B, eingereicht mit Schriftsatz vom 27.
      Februar 2023, erhält.




Die Beklagte ist der Auffassung, die Klage sei unzulässig, ein Beitritt der Klägerin
zu 2) zur Klage der Klägerin zu 1) vor deren Rechtshängigkeit sei unwirksam, da
mit der Klagerücknahme die Rechtshängigkeit rückwirkend entfallen sei. Die
Rückwirkung der Zustellung gemäß § 167 ZPO sei in diesem Fall nicht anwendbar.
Der Beitritt zu einer zurückgenommenen Klage sei auch nicht sachdienlich,

                                        - 17 -




insbesondere nicht prozessökonomisch, da die Klage noch nicht zugestellt sei. Der
Eintritt der Klägerin zu 2) und das Ausscheiden der Klägerin zu 1) müsse zwischen
diesen abgesprochen gewesen sein. Dadurch habe die Klägerin zu 2) einen
Wissensvorsprung, was zu einer prozessualen Benachteiligung der Beklagten
führe. Sie ist der Ansicht, dass das Streitpatent die Priorität der US 60 / 544 287
vom 12. Februar 2004 und der US 10 / 815 591 vom 1. April 2004 wirksam in
Anspruch nehme. Aus den nachträglichen Erklärungen der Erfinder (Anlagen G7
und G8) sowie der Stellungnahme des Rechtsanwalts (Anlage G6), der an der
Übertragung des Patents mitgewirkt habe, ergebe sich hinreichend deutlich der
Wille, dass das Patent einschließlich Prioritätsrecht zum damaligen Zeitpunkt
übertragen worden sei.


Wegen der weiteren Einzelheiten des Vorbringens der Parteien wird auf die
zwischen den Parteien gewechselten Schriftsätze nebst Anlagen und den weiteren
Inhalt der Akte Bezug genommen.




                                Entscheidungsgründe


Die   Klage   ist   zulässig,   insbesondere ist   die   Klägerin   zu 2)   wirksam
Verfahrensbeteiligte geworden. Die Klage hat in der Sache teilweise Erfolg, denn
das Streitpatent erweist sich als nicht rechtsbeständig soweit es über die mit
Hilfsantrag 2A verteidigte Fassung hinausgeht. Es ist daher im tenorierten Umfang
wegen mangelnder Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138
Abs. 1 Buchst. a) EPÜ i. V. m. Art. 54 EPÜ für nichtig zu erklären.


                                          I.


Die Klägerin zu 2) ist durch Erklärung des Beitritts zur Klage der Klägerin zu 1),
wirksam als (weitere) Klägerin Verfahrensbeteiligte geworden.

                                        - 18 -




Die Beitrittserklärung der Klägerin zu 2) mit Zustimmung der Klägerin zu 1) und
deren anschließender Klagerücknahme vor Rechtshängigkeit der ersten Klage ist
im Ergebnis nicht anders als ein ausdrücklich erklärter Parteiwechsel auf
Klägerseite zu bewerten. In prozessualer Hinsicht handelt es sich hierbei um eine
subjektive Klageänderung auf Klägerseite, deren Zulässigkeit sich nach § 99 Abs. 1
PatG i. V. m. § 263 ZPO richtet. Eine Erweiterung bzw. der Wechsel auf Klägerseite
erfolgt durch Schriftsatz der Erstklägerin und eine dem § 253 Abs. 2 Nr. 2 ZPO
genügende (§ 261 Abs. 2 ZPO) Beitrittserklärung der neuen Klägerin. Beide
Schriftsätze sind der Beklagten zuzustellen. Die Klage der (weiteren) Partei wird
rechtshängig mit Zustellung der entsprechenden Schrift an den Gegner
(Musielak/Voit/Foerste, 19. Aufl., ZPO § 263 Rn. 26 f.; Zöller-Greger, ZPO, 34. Aufl.,
§ 263 Rn. 26). Diese Voraussetzungen liegen hier vor. Auf die Rechtshängigkeit der
ursprünglichen Klage kommt es für die Wirkung der Erklärung nicht an. Der
Erklärung kann auch kein Anhaltspunkt entnommen werden, dass die Klägerin zu
2) nicht als Hauptpartei beteiligt sein wollte. Nach Ansicht des Senats ist es für den
Parteiwechsel auf Klägerseite ausreichend, dass die ursprüngliche Klage im
Zeitpunkt der Erklärung der neuen Klägerin – d. h. bei Eingang des entsprechenden
Schriftsatzes bei Gericht – schon bzw. noch anhängig war und ihre Parteistellung
als Klägerin gegeben war, in die die Klägerin zu 2) eintreten konnte. Die spätere
Rücknahme der ursprünglichen Klage durch die erste Klägerin ist insoweit
unschädlich.


Der Senat hält die Klageänderung auch für sachdienlich, § 99 Abs. 1 PatG i. V. m.
§ 263 ZPO. Nach ständiger Rechtsprechung ist für das Patentnichtigkeitsverfahren
die Sachdienlichkeit zu bejahen, wenn die Parteierweiterung die Erledigung des
Prozesses nicht verzögert und die weitere Klägerin das Streitpatent ohnehin mit
einer eigenen Nichtigkeitsklage hätte angreifen können. Aus diesem Grund ist auch
die Erwartung der Beklagten nicht schutzwürdig, dass mit der von Klägerin zu 1)
angekündigten Klagerücknahme das Verfahren abgeschlossen sei. Ferner muss im
anhängigen Verfahren unter vollständiger Verwertung des gesamten Prozessstoffs
geklärt werden können, ob das angegriffene Patent für nichtig zu erklären ist (vgl.

                                      - 19 -




BGH GRUR 1996, 865; BPatG 6 Ni 37/18; 6 Ni 46/19). Dies ist nach Ansicht des
Senats hier der Fall. Durch den Beitritt wurde ein weiteres, gesondertes
Klageverfahren der weiteren Klägerin zu 2) entbehrlich. Da der Beitritt zum
frühestmöglichen Zeitpunkt, noch vor Zustellung der ursprünglichen Klage erfolgte,
ist die Beklagte in der Verteidigung ihrer Rechte in keiner Weise behindert und er
führt auch nicht zur Verzögerung des Verfahrens (Thomas/Putzo-Reichold, ZPO,
37. Aufl., § 263 Rn. 8).




                                        II.


Die Klage ist im tenorierten Umfang begründet, da dem Streitpatent insoweit der
Nichtigkeitsgrund der mangelnden Patentfähigkeit entgegensteht, Art. II § 6 Abs. 1
Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54, 56 EPÜ.




1.     Zum Streitpatent


1.1.   Das Streitpatent befasst sich nach der Beschreibung mit der Kodierung von
Audiosignalen und der darauffolgenden Darstellung von Hörszenen aus den
kodierten Audiodaten (vgl. Absatz [0001]).


Wenn eine Person ein Audiosignal höre (z.B. Klänge), die von einer bestimmten
Audio-Quelle erzeugt wurden, treffe das Signal am linken und am rechten Ohr zu
unterschiedlichen Zeiten und mit unterschiedlichen Lautstärkepegeln ein. Dabei
seien die unterschiedlichen Zeiten und Pegel Funktionen der Distanzen zwischen
den Ausbreitungspfaden zum linken bzw. rechten Ohr. Das menschliche Gehirn
werte diese Differenzen so aus, dass sich eine Richtungs- und Entfernungsaussage
der Audio-Quelle in Bezug auf den Standort der Person ergebe. Eine Hörszene sei
dabei das Resultat, das eine Person an ihrem Standort durch das gleichzeitige

                                        - 20 -




Hören mehrerer Audio-Quellen an einem oder mehreren Quellenpositionen
wahrnehme (Streitpatent, Abs. [0003]).


Diese Art der Datenverarbeitung im Gehirn könne dafür genutzt werden, Hörszenen
darzustellen,    die aus mehreren Signalen unterschiedlicher Audio-Quellen
stammten, die absichtlich so verändert worden seien, um rechte und linke
Audiosignale zu erzeugen, die dem Hörer den Eindruck vermitteln, dass sie aus
relativ zur Hörer-Position unterschiedlichen Quellen stammten. Als Beispiel für eine
solche Umsetzung wird die WO 03 / 090 208 genannt. Im Streitpatent zeigt die Figur
1 einen binauralen Signalgenerator 100, der ein aus einer Audio-Quelle
stammendes Signal (z.B. ein Mono-Signal) in ein linkes und ein rechtes Audiosignal
eines binauralen Signals für das linke und rechte Ohr eines Zuhörers umsetze.
Zusätzlich zum Quellsignal empfange der Signalgenerator einen Satz räumlicher
Informationen betreffend die Wunschposition der Audioquelle relativ zum Hörer.
Dabei enthielten die räumlichen Informationen einen sog. „inter-channel level
difference (ICLD) value“, der die Pegelunterschiede zwischen linkem und rechtem
Signal beim Empfang mit dem linken und rechten Ohr repräsentiere, und einen sog.
„inter-channel    time    difference   (ICTD)    value“,     der    die   Differenz    der
Signalankunftszeiten am jeweiligen Ohr beschreibe. Zusätzlich oder alternativ
umfassten        manche       Generatortechniken       die         Modellierung       einer
richtungsabhängigen Transferfunktion für Tonsignale von der Audio-Quelle zum
jeweiligen Ohr (sog. “head-related transfer function (HRTF)“). Die Figur 2 des
Streitpatents zeigt einen binauralen Signalgenerator 200, der eine Vielzahl von
Audio-Quellsignalen (z.B. eine Vielzahl von Monosignalen) in linke und rechte
Audiosignale eines einzigen kombinierten Binaural-Signals konvertiere, wobei
dieser verschiedene Sets von räumlichen Informationen für jede einzelne Audio-Quelle verwende. Dabei würden die linken Signale (z.B. durch einfache Addition) zu
einem kombinierten linken Signal für die Hörszene generiert. Gleiches erfolge für
die rechten Signale (Streitpatent, Abs. [0004] – [0007]).

                                       - 21 -




Eine   Anwendung      dieser    Hörszenen-Synthese   bestehe    bei   Konferenzen.
Beispielsweise mag bei einer virtuellen Konferenz mit mehreren Teilnehmern an
ihren jeweiligen Rechnern an unterschiedlichen Orten neben dem jeweiligen
Monitor auch ein Mikrophon angeschlossen sein, das ein Mono-Quellsignal
generiere, das dem Beitrag des Teilnehmers an der Konferenz entspreche, und je
ein paar Kopfhörer, das diesen Beitrag abzuspielen vermöge. Auf dem Monitor des
Teilnehmers werde eine Konferenzszene dargestellt, die dem Sitzplatz an einem
Konferenztisch entspreche. An verschiedenen Orten des Tisches würden Echtzeit-Videoaufnahmen der anderen Konferenzteilnehmer eingespielt. In üblichen Mono-Konferenzsystemen kombiniert ein Server die Monosignale aller Teilnehmer in ein
einziges Monosignal, das an jeden Teilnehmer zurückgeschickt wird. Um aber eine
realistischere Abbildung der Situation an einem Konferenztisch zu ermöglichen,
könne der Server auch einen Signalgenerator nutzen, der ein passendes Set
räumlicher Informationen auf jedes Monosignal jedes Teilnehmers anwende, sowie
linke und rechte Signale für die Hörszene zu einem einzigen linken und rechten
Signal eines einzigen binauralen Signals kombiniere. Das linke und das rechte
binaurale Signal werde dann zu jedem Teilnehmer gesendet. Dabei bestünden bei
derzeit üblichen Stereo-Konferenzsystemen jedoch Probleme in ihrer Bandbreite
(Streitpatent, Abs. [0008], [0009])


Eine Aufgabe der vorliegenden Erfindung wird im Streitpatent nicht konkret benannt,
jedoch ein Vorgehen vorgestellt, das auf die Behebung des Bandbreitenproblems
in den als vorangegangene Anmeldungen in Absatz [0002] des Streitpatents
genannten Schriften abstellt.


1.2.   Die erteilten nebengeordneten Ansprüche 1, 8 und 9 haben in englischer
Verfahrenssprache mit der Merkmalsgliederung des Senats folgenden Wortlaut:



1.1    A method of audio processing for synthesizing an auditory scene,
       comprising:

                                       - 22 -




1.2   processing at least one input channel, using an auditory filter bank block, to
      generate two or more processed input signals;
1.3   Filtering the at least one input channel, using a filter that models late
      reverberation (LR), to generate corresponding two or more LR-filtered
      diffuse signals; and
1.4   for each of the two or more processed input signals and each of the
      corresponding two or more diffuse signals, combining one of the two or
      more LR-filtered diffuse signals with a corresponding one of the two or more
      processed input signals to generate one of a plurality of output channels for
      the auditory scene.


8.1   Apparatus for audio processing including synthesizing an auditory scene,
      comprising:
8.2   means for processing at least one input channel to generate two or more
      processed input signals;
8.3   means for filtering the at least one input channel, using a filter that models
      late reverberation (LR) to generate corresponding two or more LR-filtered
      diffuse signals; and
8.4   means for combining, for each of the two or more processed input signals
      and each of the corresponding two or more diffuse signals, one of the two
      or more LR-filtered diffuse signals with a corresponding one of the two or
      more processed input signals to generate one of a plurality of output
      channels for the auditory scene.


9.1   Apparatus for audio processing including synthesizing an auditory scene,
      comprising:
9.2   a configuration of at least one time domain (TD) to frequency domain (FD)
      converter and a plurality of filters that model late reverberation (LR), the
      configuration adapted to generate two or more processed FD input signals
      (704) and corresponding two or more LR-filtered diffuse FD signals from at
      least one TD input channel;
9.3   two or more combiners, each being dapted to combine one of the two or
      more LR-filtered diffuse FD signals with a corresponding one of the two or
      more processed FD input signals to generate a plurality of synthesized FD
      signals; and
9.4   two or more frequency domain to time domain (FD-TD) converters, each
      adapted to convert one of the synthesized FD signals into one of a plurality
      of TD output channels for the auditory scene.

                                        - 23 -




1.3   Als zuständigen Fachmann sieht der Senat einen Physiker, Elektrotechniker
oder Toningenieur mit Universitätsabschluss an, der über mehrjährige praktische
Erfahrung mit der Codierung und sonstigen Verarbeitung von Audiosignalen und -
daten zur Generierung verschiedener Höreindrücke/-szenarien über hierfür
geeignete Ausgabemittel (Lautsprecher, Kopfhörer, etc.) verfügt.


1.4   Der Senat legt den Merkmalen nach Anspruch 1 folgendes Verständnis
zugrunde:


Mit dem Anspruch 1 wird allgemein ein Datenverarbeitungsverfahren („method") für
Audiosignale ("audio processing") beansprucht, wobei nach Anwendung einiger
Datenverarbeitungsschritte eine sog. „auditory scene" - also ein Hörszenario -
erschaffen („synthesizing") werden soll. Dabei wird an dieser Stelle weder auf die
Art der zu verarbeitenden Signale noch auf die Datenverarbeitungsschritte, die zur
beanspruchten Hörszene führen, eingegangen (Merkmal 1.1).


Als erster Verfahrensschritt wird im Wortlaut des Merkmals ein „processing" - also
eine Datenverarbeitung - beansprucht, die aus mindestens einem Eingangskanal
(„input channel") unter Verwendung eines „auditory filter bank (AFB) block" zwei
oder mehrere „processed input signals" - also verarbeitete Eingangssignale -
herstellt („to generate"), wobei hier zur konkreten Art, zum Format o.ä. der
Processingergebnisse keine weiteren Angaben gemacht werden (Merkmal 1.2).


Die Streitparteien legen den Begriff „auditory filter bank block" unterschiedlich aus.


Der Fachmann versteht unter einer Filterbank ein ein- oder mehrdimensionales
Array von Filtern und unter dem Fachbegriff einer „auditory filter bank (AFB)" eine
Anordnung von Bandpassfiltern mit nicht gleichmäßiger Verteilung der Bandbreiten,
da sich diese für die konkrete Ausgestaltung einzelner Bandbreiten an der
Frequenzauflösung des menschlichen Gehörs orientiert (vgl. hierzu zum
einschlägigen Fachwissen insbesondere den als Stand der Technik in diesem

                                          - 24 -




Verfahren genannten Fachartikel NK5 aus den peer reviewed IEEE Transactions
on speech and audio processing, Vol. 7, No. 6, November 1999, S. 698, Kapitel I A,
„Auditory Filterbanks").
Das Streitpatent weicht von diesem fachmännischen Verständnis einer AFB jedoch
ab, es lehrt vielmehr als bevorzugte Ausführungsformen eine „fast fourier transform“
(FFT)- bzw. „short time forrier transform“ (STFT)-basierte Filterbank mit einer
gleichförmigen Verteilung der Koeffizienten auf der Frequenzachse, wobei die
Koeffizienten in unterschiedlicher Anzahl zu Unterbändern („sub-band") gruppiert
werden, die den kritischen Frequenzbändern („critical band") des menschlichen
Gehörs entsprechen (Streitpatent, Abs. [0022], [0032], [0049]). Die NK5 nennt eine
FFT-basierte Implementierung einer Filterbank zwar explizit als Alternative für eine
herkömmliche AFB, allerdings unter einer anderen Bezeichnung (vgl. NK5, S. 698,
Kapitel I A, letzter Absatz, „... an alternative to the use of an auditory filterbank is a
simpler uniform filterbank, such as a fast Fourier transform (FFT), ...").
Diese Diskrepanz zwischen dem gängigen Fachverständnis und der Offenbarung
des Streitpatents lässt somit für den Senat nur den Schluss zu, dass die
Streitpatentschrift den Begriff der AFB eigenständig definiert und insoweit als ihr
eigenes Lexikon zu lesen ist (st. Rspr., vgl. BGH, Urteil vom 2.3.1999 - X ZR 85/96
- Spannschraube).
Das Streitpatent bezeichnet zunächst einen „auditory filter block" - also noch keine
Filterbank - in Absatz [0021] als ein Mittel zum Verarbeiten („processing")
mindestens eines „input channel" und zum Generieren von zwei oder mehreren
„processed input signals", ohne explizit auf eine Ausgestaltung des Filters
umfassend Filtertyp und Übertragungsfunktion einzugehen (bspw. digitaler FIR-Fllter, Bandpass, etc.). Weiter beschreibt das Streitpatent den „auditory filter bank
(AFB) block 502" auch hinsichtlich einer Audiosynthese. Dabei nimmt dieser bspw.
unter Anwendung einer FFT eine Transformation vom Zeitbereich in den
Frequenzbereich vor und stellt Kopien der transformierten Signale bereit
(Streitpatent, Fig. 5 i. V. m. Abs. [0036], insb.: „In particular, BCC synthesizer 322
has an auditory filter bank (AFB) block 502, which performs a time-frequency (TF)
transform (e.g. a fast Fourier transform (FFT)) to convert time-domain combined

                                       - 25 -




channel 312 into C copies of a corresponding frequency-domain signal 504 ( ̃ (k)).").
Diese Beschränkung der AFB auf eine Zeit-Frequenz-Umsetzung findet im
Anspruch 1 noch keinen Eingang, sie wird erst mit Unteranspruch 2 beansprucht.
Zusammenfassend betrachtet versteht der Fachmann auf Basis der Offenbarung
des Streitpatentes unter einer AFB gemäß diesem Merkmal in allgemeinster Form
einen „auditory filter block", der aus dem mindestens einen Eingangskanal die o.g.
zwei oder mehreren verarbeiteten Eingangssignale generiert und als Filterbank, d.h.
einem Array von Filtern, aufgebaut sein muss. Dabei ist keinerlei weitere
Einschränkung hinsichtlich der speziellen Ausgestaltung der Filter anzunehmen, die
über die ursprüngliche Aufgabe eines Filters - nämlich zu filtern - hinausgeht, d.h.
beispielsweise keine Bandpass-Funktion.


Im Merkmal 1.3 wird beschrieben, dass das Filtern („filtering") des mindestens einen
Eingangskanals dergestalt erfolgen soll, dass ein weiterer Filter Anwendung findet,
der den späten Widerhall eines Signals („late reverberation (LR)") zu modellieren
vermag, um daraus zwei oder mehrere miteinander korrespondierende „diffuse
signals" zu erzeugen („to generate"), die in der Konsequenz LR-gefiltert sein sollen.
Dabei ist unter einem solchen Signal ein akustischer Höreindruck zu verstehen, wie
er beispielsweise in einem Konzertsaal entsteht, wenn ein örtliches Zuordnen der
Herkunft eines mehrfach reflektierten Audiosignals für den Hörer nicht mehr möglich
ist (Streitpatent, Abs. [0054]).


Als letzter Verfahrensschritt wird mit Merkmal 1.4 die Erzeugung eines von einer
Mehrzahl von Ausgangskanälen („output channels") beansprucht, die für eine
„auditory scene" notwendig sind. Dabei wird von dem oder den verarbeiteten
Eingangssignalen und den jeweils korrespondierenden zwei oder mehr diffusen
Signalen ausgegangen, die jeweils miteinander zu kombinieren sind. Nach
Auffassung des Senats ist diesem Merkmal zumindest eine eindeutige 1:1-
Zuordnung von jeweils einem LR-gefllterten, diffusen Signal mit jeweils einem
zugehörigen („corresponding one") verarbeiteten Eingangssignal zu entnehmen,
um ein Ausgangssignal zu erzeugen. Eine im Streitpatent, Absatz [0097],

                                        - 26 -




beschriebene Kombination mit einer ungleichen Anzahl von Kanälen und LR-Filtern
fällt nicht unter den Anspruchswortlaut. In welcher konkreten Weise bzw. unter
Anwendung welcher konkreter Zwischenschritte diese Kombination erfolgt und/oder
welche konkrete physikalische Form das mindestens eine Ausgangssignal aufweist,
ist nicht festgelegt.


Hinsichtlich der Merkmale 1.2 bis 1.4 werden im Streitpatent zwar mögliche
Ausgestaltungsvarianten anhand zweier Ausführungsbeispiele beschrieben, denen
u. a. verschiedene Datenverarbeitungsalternativen mit AFBs und LR-Filtern zu
entnehmen sind. Jedoch ist weder die dortige Zeitbereich-Frequenzbereich-Wandlung (TD-FD-Wandlung) in den AFBs, noch die Art bzw. Position der LR-Filterung im Frequenzbereich-Zeitbereich Teil des beanspruchten Gegenstands
gemäß Anspruch 1. Gleiches gilt für die Weiterverarbeitung der Signale in den
gezeigten Zwischenschritten wie Multiplikation und Verzögerung (Delay) der
Signale    anhand       der   Audioszenenparameter    bzw.    der   dortigen    BCC
Seiteninformation, womit diese auch nicht Eingang in die Auslegung des Anspruchs
1 finden können.


1.5    Das Streitpatent nimmt zurecht die Priorität der US-amerikanischen
Anmeldung US 10/815,591 vom 01.04.2004 in Anspruch. Damit gehört die
Dissertation „Parametric Coding Of Spatial Audio“ (NK1), unstreitig veröffentlicht im
September 2004, nicht zum berücksichtigungsfähigen Stand der Technik.


Bei der Voranmeldung US 10/815,591 handelt es sich um dieselbe Erfindung, die
auch der Gegenstand des Streitpatents ist. Die wirksame Inanspruchnahme der
Priorität einer Voranmeldung setzt nach Art. 87 Abs. 1 EPÜ ferner voraus, dass die
Anmelder     identisch sind, oder der Nachanmelder Rechtsnachfolger des
Erstanmelders ist. Dies ist der Fall, da die Beklagte belegen konnte, dass Herr
F. Baumgarte und Herr C. Faller, die Erfinder und Anmelder der Erstanmeldung,
diese und zugleich das Prioritätsrecht auf die unstreitige Rechtsvorgängerin der
Beklagten, die Agere Systems Inc., übertragen haben.

                                        - 27 -




Die Frage der wirksamen Übertragung der Anmeldung ist vom Senat im Rahmen
der freien Beweiswürdigung (§ 99 Abs. 1 PatG i. V. m. § 286 Abs. 1 ZPO) zu
entscheiden. Bei der von der Beklagten vorgelegten Abschrift des beim USPTO
hinterlegten Übertragungsvertrags (Anlage G5) bestehen noch Zweifel, ob es sich
um eine einheitliche Urkunde handelt, die eine Rechteübertragung belegen kann.
Sie besteht aus drei Blättern, von denen das erste den Vertragstext enthält, das
zweite die notariell beglaubigte Unterschrift von Frank Baumgarte und das dritte die
Unterschrift von Christof Faller. Das Blatt 1 enthält keine Fax-Kopfzeile, Blatt 2
und 3 enthalten jeweils unterschiedliche Fax-Kopfzeilen, die unterschiedliche
Übertragungsdaten, nämlich 26.03.2004 bzw. 01.04.2004, ausweisen und sich
auch vom Druckbild her so unterscheiden, dass damit allein nicht nachgewiesen ist,
dass sie zu einem einheitlichen Vertragsdokument gehörten. Die Beklagte hat
jedoch aktuelle Erklärungen der beiden Erfinder vom 10. Februar 2023 bzw. 13.
Februar 2023 eingereicht (Anlagen G7 und G8), worin diese bestätigen, dass sie
die    Übertragung   des   Prioritätsrecht   zum   damaligen   Zeitpunkt   auf   die
Rechtsvorgängerin gezeichnet haben. Auch Rechtsanwalt Steve Mendelsohn, der
den Übertragungsvertrag entworfen hat, hat in seiner schriftlichen Stellungnahme
(Anlage G6) bestätigt, dass es damals übliche Praxis in seiner Kanzlei gewesen sei,
die beim USPTO eingereichten Dokumente aus dem Originalvertragstext und den
per Fax übermittelten Seiten mit den Unterschriften zusammenzustellen. Hiernach
verbleiben keine vernünftigen Zweifel, dass das Prioritätsrecht wirksam übertragen
worden ist.


Die Beklagte kann sich indes nicht auf die Inanspruchnahme der früheren Priorität
der US 60 / 544,287 P vom 12.02.2004 berufen, weil sie dazu nichts vorgetragen
hat.

                                        - 28 -




1.6    Die Klägerin zu 2) ist der Ansicht, dass mit dem erteilten Anspruch 1 in den
beiden Merkmalen 1.2 und 1.4 eine gegenüber den Ursprungsunterlagen
unzulässige Erweiterung vorliegt. Dies ist jedoch nicht der Fall, da zum einen
ursprünglich eingereichte Patentansprüche zur Ursprungsoffenbarung einer
Patentanmeldung zählen, so dass der Anmelder im Prüfungsverfahren stets auch
aus diesen schöpfen kann (vgl. „at least one input channel“- und „a plurality of output
channels“ im ursprünglichen Anspruch 1 [Unterstreichungen hinzugefügt]). Zum
anderen weisen die Ausführungsbeispiele der Ursprungsunterlagen (z.B. die
Figuren 3, 5 und 7 mit den zugehörigen Beschreibungsteilen) illustrativen Charakter
auf und wirken folglich auch nicht beschränkend (vgl. BGH, Urteil vom 19.
Dezember 2017 – X ZR 5/16; BGH, Urteil vom 17. Juli 2012 – X ZR 117/11 –
Polymerschaum I). Dafür sprechen auch die Überschriften auf Seite 18 („Exemplary
Reverberation-Based Audio Synthesizer“) und auf Seite 28, Zeilen 8 bis 16 (Titel:
„Alternative Embodyments“), die dem erkennenden Fachmann vermitteln, dass mit
den in den Figuren offenbarten Realisierungen nur Beispiele dargestellt sind, die
der Fachmann bei entsprechenden Randbedingungen auch gemäß seiner
Fachkenntnis geeiget abzuwandeln bzw. weiter auszugestalten versteht.


Gleiches gilt mit derselben Begründung auch für die klageseitig in diesem Kontext
gegenüber dem Anspruch 8 vorgebrachte Ansicht einer unzulässigen Erweiterung.


1.7    Der Gegenstand des Anspruchs 1 ist gegenüber der Lehre der Druckschrift
NK2 (WO 99 / 14 983 A1) nicht patentfähig, da er mit sämtlichen Merkmalen aus
dieser Druckschrift bekannt und folglich nicht neu ist (vgl. Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52, 54 EPÜ). Denn aus ihr ist ein
Verfahren zur Datenverarbeitung akustischer Eingangssignale („audio inputs 11“)
bekannt, die ein Hörszenerio i. S. d. Streitpatents im Rahmen von Kopfhörern zu
synthetisieren vermag (NK2, Fig. 1, 4 und 17 i. V. m. S. 1, Z. 3 – 5, insb.: „…
inventions relates to the fields of audio signal processing and audio reproduction,
particularly over headphones and further discloses sound reproduction techniques
which create enhanced effects such as spatialization of objects around a listener …“

                                        - 29 -




und S. 6, Z. 23 - 27, insb.: „Once decoded, the speaker feeds are suitable … as
inputs 41 to the arrangement 40 of Fig. 4 which produces headphone outputs 42.
Each of the five speaker feeds is passed through a filter e.g. 43, 44 for each ear and
summed e.g. 45 to produce the headphone signal …“; Merkmal 1.1).


Diese Datenverarbeitung mindestens eines Eingangskanals nutzt auch einen
Filterbankblock für akustische Signale i. S. des Streitpatents gemäß obiger
Auslegung, um zwei oder mehr verarbeitete Ausgabesignale zu erzeugen. Die NK2
zeigt dies in den Figuren 1, 4 und 17, insbesondere im Rahmen der dort
angegebenen Signalwege von „AUDIO INPUT“ zum einen durch zwei „FIR (50
TAP)“ Filterbankblöcke, zum anderen über die „DELAY LINE“ zu mindestens vier
weiteren „FIR (50 TAP)“ Filterbankblöcken bzw. über die beiden angegebenen
„REVERBERANT FIR (32k TAP)“ Filterbankblöcke, deren jeweilige Ausgänge
entweder über ein Summenglied für den „LEFT OUTPUT“ oder eines für den
„RIGHT OUTPUT“ aufaddiert werden (Merkmal 1.2).


Hier erfolgt durch eine entsprechende Filterung letztlich auch eine Modellierung
später   Widerhallsignale,    um    mindestens     zwei     entsprechend     gefilterte
Ausgangssignale zu erzeugen, wie sich in der NK2 der Figur 17 mit zugehöriger
Figurenbeschreibung über den Signalweg durch die „REVERBERANT FIR (32k
TAP)“ Filterbankblöcke zu den Addierern „+“ entnehmen läßt (NK2, Fig. 17 i. V. m.
S. 12, Z. 7 - 12, insb.: „… an alternative implementation 170 of a 3-D sound
processing system where the late reverberant part is implemented using a pair of
long FIR filters 171. In this example … the 32k Tap FIR filters will allow acoustic
spaces to be simulated with reverberation times of up to 670ms. By making use of
real, measured binaural acoustic responses, the Reverberant FIR filters 171 in Fig.
17 can provide a much more accurate 3-D acoustic impression than the recursive
reverberation structures used in Fig. 16.“; Merkmal 1.3).


Dabei wird auch jedes der zwei oder mehr prozessierten Eingangssignale jeweils
mit einem der für die Modellierung später Widerhallsignale gefilterten Signale

                                       - 30 -




kombiniert, um auf diese Weise einen von einer Mehrzahl von Ausgangskanälen für
das beanspruchte Hörszenerio zu verwirklichen. Dies ist der Figur 17 der NK2 im
Rahmen der abzählbaren Signalwege ausgehend von den dargestellten jeweiligen
„FIR (50 TAP)“ zu den Summationsgliedern für den linken und den rechten Ausgang
im Vergleich zu den Signalwegen ausgehend von den beiden „REVERBERANT FIR
(32k TAP)“ zu den eben genannten Summationsgliedern zu entnehmen (NK2, Fig.
17 i.V.m. S. 12, Z. 7 – 12; Merkmal 1.4).


Damit sind sämtliche Merkmale des erteilten Anspruchs 1 aus der Druckschrift NK2
neuheitsschädlich bekannt.


1.8   Die vorstehenden Ausführungen gelten entsprechend auch für den
nebengeordneten Vorrichtungsanspruch 8. Dieser ist ebenfalls nicht patentfähig, da
er lediglich die Verfahrensanspruchsmerkmale des Anspruchs 1 für eine
Vorrichtung umformuliert und keinen weiteren eigenständig patentfähigen Inhalt hat.


1.9   Da sich der Gegenstand des Anspruchs 9 von der Vorrichtung gemäß
Anspruch 8 in den entsprechenden Teilmerkmalen der Merkmale 9.2 bis 9.4
lediglich dadurch unterscheidet, dass diese vor der eigentlichen Filterung des
Eingangssignals zum Zwecke der Modellierung eines Hörszenerios ausdrücklich
Zeitbereich-Frequenzbereich-Wandler und Frequenzbereich-Zeitbereich-Wandler
vor der Endausgabe an die beiden Kopfhörer vorsieht, können diese vor dem
Hintergrund der Lehre der Druckschrift NK2 jedenfalls keine erfinderische Tätigkeit
begründen. Es handelt sich hierbei lediglich um fachübliche Maßnahmen bzw.
Bauteile im Rahmen einer digitalen Signalverarbeitung. Der Fachmann wird eine
solche Art der Signal-Hin- und -Rückwandlung wie sie z.B. eine FFT bzw. IFFT mit
den entsprechenden Wandlern darstellt, implementieren, wenn sie sich in dem zu
beurteilenden Zusammenhang als objektiv zweckmäßig darstellt und keine
besonderen Umstände feststellbar sind, die eine Anwendung aus fachlicher Sicht
als nicht möglich, mit Schwierigkeiten verbunden oder sonst untunlich erscheinen

                                         - 31 -




lassen     (vgl.   BGH,   Urteil   vom   11.      März   2014    -   X    ZR   139/10    –
Farbversorgungssystem). Dies ist hier der Fall.


Der Einsatz von Datenverarbeitungsmaßnahmen, die die Wandlung von Signalen
vom Zeit- in den Frequenzbereich bzw. umgekehrt im Rahmen einer akustischen
Datenverarbeitung betreffen, ist jedenfalls Teil des Fachwissens, wie dem als
Anlage NK11 eingreichten Lehrbuch zur digitalen Signalverarbeitung (NK11, S. 9,
Abs. 2 i. V. m. S. 152, Abs. 1) und im Kontext einer zum Streitpatent verwandten
akustisch technischen Problemstellung im Rahmen eines Konferenzsystems der
Druckschrift NK9 zu entnehmen sind. Aus der Lehre der NK9 geht unmittelbar
hervor, dass aus einem Monosignal, das zunächst einer Umwandlung vom Zeit- in
den Frequenzbereich unterworfen wird, und „BCC PARAMETERS“ letztlich über
einen     „AUDITORY       SCENE    SYNTHESIZER           504“   mittels   „INVERSE      TF
TRANSFORM 506, 508“ eine Rückumwandlung von Signalen vom Frequenz- in den
Zeitbereich vollzogen wird, bevor die Signale in die Ausgabe eines linken und
rechten Audiosignals münden (NK9, Fig. 4 und 5 i. V. m. [0036], insb.: „… As shown
in FIG. 4, audio analyzer 310 comprises two time-frequency (TF) transform blocks
402 and 404, which apply a suitable transform, Such as a short-time discrete Fourier
transform (DFT) of length 1024, to convert the left and right input audio signals L
and R, respectively, from the time domain into the frequency domain. Each
transform block generates a number of outputs corresponding to different frequency
Sub-bands of the input audio signals.“).




2.       Zum Hilfsantrag 1


2.1      Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1 ist nicht patentfähig,
da dieser sich in naheliegender Weise aus der Lehre der Druckschrift NK2
zusammen mit dem Fachwissen ergibt (vgl. Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. a), Art. 52, 56 EPÜ).

                                          - 32 -




Der geänderte Anspruch 1 unterscheidet sich im Vergleich zur erteilten Fassung
darin, dass das Merkmal 1.2 folgende ergänzte Fassung erhält (Änderung
hervorgehoben):


      1.21   processing (702) at least one input channel (312), using an auditory filter
             bank block (702) performing a time-frequency transform, to generate
             two or more processed input signals (704);


Die Ergänzung des Anspruchs um eine Zeitbereich-Frequenzbereich-Wandlung vor
der eigentlichen Signalverarbeitung im beanspruchten Verfahren, die letztlich zum
Synthetisieren einer Audio-Szenerie führen soll, stellt lediglich eine fachübliche
Maßnahme im Rahmen einer digitalen Signalverarbeitung dar. Es wird auf die
entsprechenden Ausführungen zur Vorrichtung gemäß dem erteilten Anspruch 9
unter Abschnitt II.1.9 verwiesen. Denn ein derartiges Vorgehen in einem Verfahren
unterscheidet sich technisch betrachtet in seiner Wirkung letztlich nicht von der dort
räumlich-körperlich beanspruchten Vorrichtung, die dies bewerkstelligen soll.


Hinsichtlich der unveränderten Merkmale wird zur Begründung auf die
entsprechenden Ausführungen im Rahmen des Hauptantrags verwiesen.


2.2      Der Anspruch 8 gemäß Hilfsantrag 1 unterscheidet sich im Vergleich zur
erteilten Fassung darin, dass das Merkmal 8.2 folgende ergänzte Fassung erhält
(Änderung hervorgehoben):


         8.21   means for processing at least one input channel, using an auditory
                filter bank block performing a time-frequency transform, to generate
                two or more processed input signals;


Diese Präzisierung des Merkmals im Rahmen eines Vorrichtungsanspruchs stellt
nur dieselbe Maßnahme dar, wie sie bereits für den Verfahrensanspruch 1 im
Rahmen des Merkmals 1.2 des Hauptantrags bzw. des Merkmals 1.21 des

                                          - 33 -




Hilfsantrags 1 beansprucht wurde. Zur Begründung der fehlenden Patentfähigkeit
wird auf die dortigen Ausführungen verwiesen.


2.3       Der Anspruch 9 gemäß Hilfsantrag 1 enthält gegenüber der erteilten Fassung
keine Änderungen. Auf die obigen Ausführungen unter Abschnitt II.1.9 wird
verwiesen.




3.        Zum Hilfsantrag 2


3.1       Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 2 ist ebenfalls nicht
patentfähig, da dieser sich in naheliegender Weise aus der Lehre der Druckschrift
NK2 zusammen mit dem Fachwissen ergibt und sein Gegenstand sich mangels
erfinderischer Tätigkeit als nicht patentfähig erweist.


Der Anspruch 1 gemäß Hilfsantrag 2 unterscheidet sich im Vergleich zur erteilten
Fassung durch zwei am Ende angefügte Verfahrensmerkmale die (vom Senat
gegliedert) folgendermaßen lauten:


      1.52   converting the at least one input channel from a time domain into a
             frequency domain to generate a plurality of frequency-domain (FD) input
             signals; and
      1.62   wherein processing the at least one input channel comprises: delaying
             and scaling the FD input signals to generate a plurality of scaled, delayed
             FD signals as processed input signals.


Das neu hinzugetretene Merkmal 1.52 und wesentliche Teile des Merkmals 1.62
stellen      ebenso   nichts   Anderes    dar,     als   eine   fachübliche   Zeitbereich-Frequenzbereich-Wandlung, wie sie im Zusammenhang mit den vorangegangenen
Hilfsanträgen bereits erörtert worden ist.

                                        - 34 -




Die weiteren mit dem neuen Merkmal 1.62 beanspruchten Schritte, nämlich die
Verzögerung von Signalanteilen bzw. deren Skalierung i. S. d. Streitpatents, sind
ebenfalls bereits aus der Druckschrift NK2 als übliche Verarbeitung akustischer
Signale bekannt (vgl. NK2, Fig. 17: „DELAY LINE“, „+“).


Hinsichtlich der unveränderten Merkmale wird zur Begründung auf die
entsprechenden Ausführungen im Rahmen des Hauptantrags verwiesen.


3.2   Der Gegenstand nach Anspruch 7 gemäß Hilfsantrag 2 stellt nur die
Anpassung der im Rahmen des Anspruchs 1 gemäß Hilfsantrag 2 neu
hinzugetretenen Verfahrensmerkmale 1.52 und 1.62 an eine Vorrichtung gemäß
dem erteilten Anspruch 8 dar und enthält damit nichts Neues im Vergleich zu dem,
was bereits im Rahmen des Anspruchs 1 ausgeführt wurde. Auf die Ausführungen
zum Anspruch 1 gemäß Hilfsantrag 2 hinsichtlich seiner mangelnden erfinderischen
Tätigkeit wird verwiesen.


3.3   Der Gegenstand des Anspruchs 8 gemäß Hilfsantrag 2 unterscheidet
inhaltlich nicht von dem des erteilten Anspruchs 9. Es wird auf die Ausführungen
unter Abschnitt II.1.9 verwiesen.




4.    Zum Hilfsantrag 2A


Der Gegenstand des mit dem Hilfsantrag 2A zulässig verteidigten Anspruchs 1
erweist sich gegenüber dem im Verfahren befindlichen Stand der Technik als neu
und beruht auch auf einer erfinderischen Tätigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG
i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52, 54, 56 EPÜ).


4.1   Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 2A unterscheidet sich
im Vergleich zur Fassung gemäß Hilfsantrag 2 durch die Ergänzung zweier weiterer

                                            - 35 -




Merkmale im Anschluss an das bisherige letzte Merkmal 1.62 aus dem Hilfsantrag
2, die (vom Senat gegliedert) folgendermaßen lauten:


      1.6.12A   wherein each FD input signal is delayed at a corresponding delay
                block based on delay values derived from corresponding inter-channel
                time difference data, and
      1.6.22A   wherein each delayed FD input signal is scaled by a corresponding
                multiplier based on scale factors derived from corresponding interchannel level difference data.


4.2      Da mit der Fassung des Hilfsantrags 2A - mit derselben Begründung wie zum
erteilten Anspruch 1 ausgeführt - keine unzulässigen Erweiterungen gegenüber den
Ursprungsunterlagen verbunden sind, ist dieser zulässig (vgl. die Ausführungen
unter Abschnitt II.1.6).


4.3      Der Anspruch 1 gemäß Hilfsantrag 2A ist neu gegenüber dem im Verfahren
befindlichen Stand der Technik, da aus keiner der genannten Druckschriften dessen
sämtliche Merkmale bekannt sind. Insbesondere sind die neuen Merkmale 1.6.12A
und 1.6.22A keiner der Druckschriften unmittelbar und eindeutig zu entnehmen.


4.4      Der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 2A beruht ausgehend
vom im Verfahren genannten Stand der Technik auch auf einer erfinderischen
Tätigkeit, da er durch diesen nicht nahegelegt ist.


4.4.1 Ausgehend von der Druckschrift NK2 vermag der Fachmann die neuen
Merkmale 1.6.12A und 1.6.22A nicht in naheliegender Weise aus dem Fachwissen
oder in Kenntnis eines anderen Standes der Technik, wie er im Verfahren genannt
ist, zu deren Lehre ergänzen, denn dazu fehlt ihm jeglicher Anlass. Ein solcher
wurde seitens der Klägerin zu 2) auch nicht in überzeugender Weise vorgetragen.

                                           - 36 -




Zwar lehrt die Druckschrift NK2 ein Verfahren, das ohne explizite Zusatzinformation
zum analogen Eingangssignal vom Zeitbereich ausgehend eine akustische
Datenverarbeitung vornimmt, um dem Nutzer eines Kopfhörers ein möglichst
realitätsnahes Hörempfinden zu vermitteln. Der Fachmann wird ggf. auch weitere in
diesem Fachbereich übliche Datenverarbeitungsmaßnahmen vorsehen, wie sie
etwa       Zeitbereich-Frequenzbereich-Wandlungen        und     umgekehrt    darstellen.
Jedenfalls ist ihm aber ausgehend von der Druckschrift NK2 nicht nahegelegt,
digitale      Datenverarbeitungsschritte       im      Rahmen      einer     akustischen
Signalverarbeitung        vorzunehmen,          die      auf      Zeitdifferenz-      und
Intensitätsdifferenzdaten verschiedener Kanäle im Frequenzbereich aufbauen.


Diese Art von Datenverarbeitungsmaßnahmen mag zwar per se aus der
Druckschrift NK9 hervorgehen (NK9, Abs. [0013] und [0034]), allerdings lässt sich
für den       Fachmann zur Überzeugung              des Senats    ohne rückschauende
Betrachtungsweise keine begründet nachvollziehbare Veranlassung feststellen,
zwei so unterschiedliche Ansätze akustischer Datenverarbeitung zu kombinieren
(NK2:      „audio   reproduction   …   over     headphones“      mit   diffuser    (Nach-)
Hallberücksichtigung; NK9: „Binaural Cue Coding BCC“ ohne Berücksichtigung des
(späten) Widerhalls). Ein bloßes Hinzufügen der mit der Lehre gemäß Druckschrift
NK2 nicht verwirklichter, aber im Rahmen der Druckschrift NK9 bekannter Merkmale
im Sinne einer Lückenfüllung in der genannten Lehre reicht jedenfalls nicht aus, weil
hierfür kein Anreiz von der Klägerin substantiert vorgetragen wurde und auch sonst
nicht ersichtlich ist.


4.4.2 Auch ausgehend von der Druckschrift NK3 gelangt der Fachmann weder
durch das Fachwissen, noch durch die Kombination mit einer der anderen im
Verfahren befindlichen Druckschriften zum Gegenstand des Anspruches 1.
Die Druckschrift NK3 beschreibt die Verarbeitung von Audiosignalen für eine
Wiedergabe über Kopfhörer, um für den Hörer/Nutzer den Eindruck zu erwecken,
die jeweils zu hörenden Schallquellen seien an unterschiedlichen Orten in seiner
Umgebung (NK3, Sp. 2, Z. 4 - 9). Für die Datenverarbeitung geht ihre Lehre von

                                        - 37 -




einer Dreiteilung des zu verarbeitenden Audiosignals aus und zwar einem
Direktwellenanteil (Schall der direkt zum Ohr gelangt), frühen Reflexionen (das
reflektierte Ursprungssignal nach wenigen Reflexionen in der Umgebung) und dem
Endteil (später Widerhall nach einer Vielzahl von Reflexionen). Aus der Druckschrift
NK3 sind die Merkmale 1.1 bis 1.4 grundsätzlich bekannt, wie sich im Einzelnen aus
den Signalwegen in den Figuren 1, 3 und 5 i. V. m. den zugehörigen
Figurenbeschreibungen ergibt (Merkmal 1.1: Fig. 1 + 3 i. V. m. Sp. 2, Z. 4 - 9;
Merkmal 1.2: Signalwege in Fig. 3 bzw. 5 i. V. m. Sp. 4, Z. 12 - 16 und Sp. 2, Z. 29
- 32 bzw. Sp. 5, Z. 49 - 69; Merkmal 1.3: Signalwege in Fig. 3 bzw. 5 i. V. m. Sp. 5,
Z. 10 - 18 bzw. Sp. 5, Z. 10 - 16 und Sp. 6, Z. 8 - 15; Merkmal 1.4: Fig. 3 und 5 i. V.
m. Sp. 4, Z. 44 - 50 bzw. vgl. Zitate zum Merkmal 1.3).


Wie bereits für die Druckschrift NK2 ausgeführt, mag der Fachmann zwar die
Datenverarbeitung der Audiosignale in der NK3, die sich im Zeitbereich abspielt
(auch wenn lediglich im Rahmen der Figurenbeschreibung zu den Figuren 6A bis
6C in der Spalte 4, Zeile 53 bis 59 nur einmal die Begrifflichkeit „time domain
convolution“ für die gemäß der Lehre dieser Druckschrift im Einsatz befindlichen
Transferfunktionen benannt wird), auch im Frequenzbereich durchführen - sofern
es ihm sinnvoll und/oder notwendig erscheint -, ohne dass es hierfür einer
erfinderischen Tätigkeit bedarf. Somit mögen dem Fachmann auch die Merkmale
1.52 und 1.62 naheliegen. Die weiteren Merkmale 1.6.12A und 1.6.22A vermag der
Fachmann jedoch zur Überzeugung des Senats auch ausgehend von der
Druckschrift NK3 nicht in naheliegender Weise aus dem Fachwissen oder
ausgehend von einem anderen Stand der Technik, wie er im Verfahren genannt ist,
zu ergänzen. Denn dazu fehlt ihm auch hier ein nachvollziehbar vorgetragener
Anlass.


4.4.3 Der Fachmann gelangt auch ausgehend von der Druckschrift NK9 nicht zum
Gegenstand des Anspruchs 1 nach Hilfsantrag 2A. Diese Druckschrift beschreibt in
ähnlichem Kontext wie das Streitpatent zwar eine kohärenzbasierte Audiokodierung
und Audiosynthese, die einen Audio-Synthesizer mit einer im Vorfeld auf ein

                                       - 38 -




Monosignal angewandten „TF TRANSFORM“ (z.B. NK9, Fig. 4 und 5) lehrt - wobei
eine Gruppierung von Koeffizienten in kritische Frequenz-Subbänder thematisiert
wird - und nach der Audiosynthese unter Einbeziehung der bereits o.g. „BCC
PARAMETERS“ eine entsprechende Rücktransformation in den Zeitbereich zur
Ausbildung eines „LEFT“ bzw. „RIGHT AUDIO SIGNAL“ zeigt (NK9, ebenda). Auch
die Einbeziehung von Kanalpegeldifferenzen („interaural level difference, ILD“) und
Zeitverzögerungen zwischen unterschiedlichen Signalanteilen („interaural time
delay, ITD“) in die Erstellung eines zweikanaligen Ausgabesignals werden – worauf
die Klägerin zu Recht hinweist - dort bereits erwähnt, zudem auch im Rahmen des
Einsatzes von Kopfhörern (NK9, Abs. [0007] - [0008]). Jedoch wird in dieser
Druckschrift weder ein Umgang mit dem späten Widerhall akustischer Signale in
Form von entsprechenden Filtermaßnahmen gelehrt, noch diese Problematik an
sich thematisiert. Daher sind dieser Druckschrift aus der Sicht des Senats bereits
das Merkmal 1.4 allenfalls teilweise und das Merkmal 1.3 nicht entnehmbar. Der
Senat kann nicht feststellen, dass der Fachmann ausgehend von der
funktionsfähigen Lehre dieser Druckschrift Veranlassung hatte, insbesondere
Signalanteile des späten Widerhalls in seine Überlegungen einzubeziehen und ggf.
Aspekte aus der zeitbereichsgestützten Lehre der Druckschrift NK2 und/oder NK3
in sein datenverarbeitungstechnisch betrachtet bereits höher entwickeltes
Verfahren einzubinden, das im Wesentlichen auf Signalverarbeitungsmaßnahmen
im Frequenzbereich basiert. Aus Sicht des Senats ist ein solcher Weg für den
Fachmann vor dem Hintergrund der signaltechnischen Zusammenhänge vielmehr
rückschauend und kann daher nicht greifen (vgl. auch die Ausführungen im
Abschnitt II.4.4.1).


4.4.4 Die Druckschrift NK4 zeigt zur Überzeugung des Senats bereits keine
Filterbank i. S. d. Streitpatents, sondern lediglich Multiplikatoren (NK4, Fig. 1,
„multipliers 11, 12, 13, 14“) und liegt damit weiter ab. Daher hätte der Fachmann in
Ermangelung des wesentlichsten Bausteins der streitpatentlichen Lehre ausgehend
von dieser Druckschrift auch nicht ohne weiteres zum Gegenstand des beschränkt
verteidigten Gegenstandes gelangen können.

                                        - 39 -




4.4.5 Auch die übrigen Druckschriften NK5 bis NK8, sowie NK10 und NK11
schildern jeweils für sich betrachtet lediglich Teilaspekte des Streitgegenstandes
oder sind nur zum Nachweis fachmännischen Wissens geeignet. Ihre Lehre liegt
jeweils weiter ab und eignet sich damit jeweils weder als Ausgangspunkt für
technische Überlegungen des Fachmanns, die in die Richtung der Lehre des
Streitpatents zielen, noch in einer etwaigen Zusammenschau (deren Anlass zudem
im Verfahren nicht ersichtlich ist), um in naheliegender Weise zum beschränkten
Gegenstand des Anspruchs 1 gemäß Hilfsantrag 2A zu gelangen.


4.5   Der Gegenstand des mit dem Hilfsantrag 2A verteidigten Anspruchs 1 erweist
sich folglich gegenüber dem im Verfahren befindlichen Stand der Technik als
patentfähig.


Gleiches gilt mit derselben Begründung auch für die nebengeordneten Ansprüche
7 und 8 des Hilfsantrages 2A, da diese neue, inhaltlich an die beiden
Vorrichtungsansprüche angepasste und ebenfalls die Patentfähigkeit begründende
Merkmale enthalten, wie sie der Anspruch 1 mit den Merkmalen 1.6.12A und 1.6.22A
aufweist.


Auch die auf den Anspruch 1 und 8 rückbezogenen Unteransprüche 2 bis 6 sowie
9 gemäß Hilfsantrag 2A bilden deren Gegenstände, auf die sie jeweils direkt oder
indirekt rückbezogen sind, in nicht selbstverständlicher Weise weiter und erweisen
sich daher ebenfalls als patentfähig.




5.    In Anbetracht der erfolgreichen Verteidigung des Streitpatents mit Hilfsantrag
2A war über die weiteren Hilfsanträge sowie alle nachrangigen Unteransprüche
nicht mehr zu entscheiden.

                                      - 40 -




                                       III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i.V.m. §§ 92 Abs. 1 Satz 1
269 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i.V.m. § 709 Satz 1 und 2 ZPO.



                                       IV.
                      Rechtsmittelbelehrung



Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Heimen          Schödel          Dr. Wollny         Bieringer          Dr. Ball
