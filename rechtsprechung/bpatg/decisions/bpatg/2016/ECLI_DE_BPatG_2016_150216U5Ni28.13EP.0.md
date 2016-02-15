---
ecli: "ECLI:DE:BPatG:2016:150216U5Ni28.13EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 28/13"
decided: "2016-02-15"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2016&Sort=1&Seite=5&nr=27805&anz=906&pos=81&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2016-02-15_5_Ni_28_13_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0139.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 28/13 vom 2016-02-15

## Entscheidung

BUNDESPATENTGERICHT


                     IM NAMEN DES VOLKES


                                URTEIL                An Verkündungs Statt
                                                          zugestellt am
5 Ni 28/13 (EP)                                         15. Februar 2016
                                                               …
(Aktenzeichen)




                     In der Patentnichtigkeitssache

  …




  BPatG 253
  08.05

                                      -2-


…




                    betreffend das europäische Patent …
                                    (DE …)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche Verhandlung vom 2. Dezember 2015 durch den Richter Schwarz als Vorsitzenden, die Richterin Hartlieb sowie die Richter Dipl.-Ing. Gottstein, Dipl.-Ing.
Univ. Albertshofer und Dipl.-Geophys. Dr. Wollny

                                      -3-


für Recht erkannt:


       I.   Das europäische Patent … wird mit Wirkung
            für das Hoheitsgebiet der Bundesrepublik Deutschland
            für nichtig erklärt.


       II. Die Kosten des Rechtsstreits trägt die Beklagte.


       III. Das Urteil ist gegen Sicherheitsleistung in Höhe von
            120 % des zu vollstreckenden Betrages vorläufig volltreckbar.




                                   Tatbestand


Die Beklagte ist eingetragene Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents
… (Streitpatent), das aufgrund der internationalen Anmeldung
… vom 28. Mai 2002, die als … am
5. Dezember 2002 veröffentlicht worden ist, unter Inanspruchnahme der Priorität aus der US-amerikanischen Anmeldung … vom 31. Mai 2001, erteilt worden ist. Das Streitpatent ist in der Verfahrenssprache Englisch veröffentlicht worden und wird beim Deutschen Patent- und Markenamt unter dem
Aktenzeichen DE… geführt. Das Streitpatent trägt die Bezeichnung
„PARALLEL DATA COMMUNICATION WITH MULTIPLE SYNCHRONISATION
CODES“ (in Deutsch laut Streitpatentschrift: „PARALLELE DATENÜBERTRA-GUNG MIT MEHREREN SYNCHRONISIERUNGSKODES“) und umfasst in der
erteilten Fassung 18 Patentansprüche, die mit der am 7. August 2013 erhobenen Nichtigkeitsklage in vollem Umfang angegriffen werden.


Die unabhängigen Patentansprüche 1 und 16 in der erteilten Fassung lauten in
der Verfahrenssprache wie folgt:

                                   -4-


“1. A parallel data communication arrangement (100) adapted to
   compensate for the skewing of digital data, comprising:

       a parallel bus having parallel bus lines (116, 118) adapted
       to transfer digital data;
       a first module (112) adapted to transfer the digital data concurrently on the bus lines;
       each of the bus lines (116, 118) having an associated adjustable data-delay circuit (216a, 216b)

   the arrangement (100) being characterized by:

       the parallel bus having a clock path (122) adapted to carry a
       clock signal for synchronizing digital data carried over the
       plurality of data-carrying lines;
       the first module (112) adapted to transfer the digital data
       concurrently on the bus lines (116, 118) along with the clock
       signal, selected ones of the sets of data including at least
       two synchronization codes transferred contiguously on the
       bus lines (116, 118) to toggle the bus lines with each of the
       synchronization codes transferred;
       a second module (114) adapted to sample the synchronization codes in response to an edge of the clock signal, and
       validate the sampled synchronization codes; and
       the adjustable data-delay circuits (216a, 216b) being responsive to the validated synchronization codes and
       adapted to adjust the edge of the clock signal relative to the
       synchronization codes.”



“16. A parallel data communication method adapted to compensate
    for the skewing of digital data, the method comprising:

                                        -5-


               over a parallel bus having parallel bus lines (116, 118) and
               a clock path (122) adapted to carry a clock signal for synchronizing digital data carried over the plurality of data-carrying lines, transferring the digital data concurrently along
               with the clock signal, selected ones of the sets of data including at least two synchronization codes transferred contiguously to toggle the bus lines (116, 118) with each of the
               synchronization codes transferred;
               receiving the transferred data, including sampling the synchronization codes in response to an edge of the clock signal, and validating the sampled synchronization codes; and
               responsive to the validated synchronization codes, timeadjusting the edge of the clock signal relative to the synchronization codes by controlling an adjustable data-delay
               circuit (216a, 216b) associated with each bus line.”

In deutscher Übersetzung lauten diese Patentansprüche gemäß Streitpatentschrift wie folgt:

      “1. Parallele Datenkommunikationsanordnung (100), die ausgebildet ist, den Versatz digitaler Daten zu kompensieren, umfassend:

               einen parallelen Bus mit parallelen Busleitungen (116, 118),
               die ausgebildet sind, digitale Daten zu übertragen;
               ein erstes Modul (112), das ausgebildet ist, die digitalen
               Daten gleichzeitig auf den Busleitungen zu übertragen; wobei
               jede der Busleitungen (116, 118) eine zugeordnete einstellbare Datenverzögerungsschaltung (216a, 216b) hat; und
               wobei die Anordnung (100) dadurch gekennzeichnet ist,
               dass:

                               -6-


          der parallele Bus einen Taktpfad (122) hat, der ausgebildet ist, ein Taktsignal zum Synchronisieren digitaler
          Daten zu transportieren, die über die Vielzahl von Daten transportierender Leitungen transportiert werden;
          das erste Modul (112) ausgebildet ist, die digitalen Daten gleichzeitig mit dem Taktsignal auf den Busleitungen (116, 118) zu übertragen, wobei von den Datensätzen ausgewählte Datensätze mindestens zwei Synchronisierungscodes enthalten, die zusammenhangend
          auf den Busleitungen (116, 118) übertragen werden,
          um mit jedem der übertragenen Synchronisationscodes
          zwischen den Busleitungen zu schalten;
          ein zweites Modul (114)vorgesehen ist, das ausgebildet
          ist, die Synchronisierungscodes in Reaktion auf eine
          Flanke des Taktsignals abzutasten, und die abgetasteten Synchronisierungscodes zu validieren; und
          dass die einstellbaren Datenverzögerungsschaltungen
          (216a, 216b) ausgebildet sind, auf die validierten Synchronisierungscodes zu reagieren und die Flanke des
          Taktsignals relativ zu den Synchronisierungscodes einzustellen.”

“16. Paralleles Datenkommunikationsverfahren (100), das ausgebildet ist, den Versatz digitaler Daten zu kompensieren, wobei
    das Verfahren umfasst:

          Übertragen digitaler Daten zusammen mit einem Taktsignal über einen parallelen Bus mit parallelen Busleitungen (116, 118) und einem Taktpfad (122), der ausgebildet ist, ein Taktsignal zum Synchronisieren digitaler Daten zu transportieren, die über die Vielzahl Daten
          transportierender Leitungen transportiert werden, wobei

                                           -7-


                     die digitalen Daten gleichzeitig mit dem Taktsignal übertragen werden, und wobei ausgewählte Datensätze mit
                     mindestens zwei Synchronisierungscodes zusammenhängend übertragen werden, um zwischen mit jedem
                     der übertragenen Synchronisierungscodes den Busleitungen (116, 118) zu schalten;
                     Empfangen der übertragenen Daten, einschließlich Abtasten der Synchronisierungscodes in Reaktion auf eine
                     Flanke des Taktsignals, und Validieren der abgetasteten Synchronisierungscodes; und
                     in Reaktion auf die validierten Synchronisierungscodes,
                     zeitliches Einstellen der Flanke des Taktsignals relativ
                     zu den Synchronisierungscodes durch Steuern einer jeweiligen    einstellbaren   Datenverzögerungsschaltung
                     (216a, 216b), die jeder Busleitung zugeordnet ist.“


Bei den Patentansprüchen 2 bis 15 handelt es sich um auf Patentanspruch 1,
bei den Patentansprüchen 17 und 18 um auf Patentanspruch 16 jeweils unmittelbar oder mittelbar rückbezogene Unteransprüche. Wegen deren Wortlaut
wird auf die Akte Bezug genommen.


Die Klägerin ist der Ansicht, dass der mit ihrer Klage angegriffene Gegenstand
des Streitpatents wegen unzulässiger Erweiterung, fehlender Ausführbarkeit
und mangelnder Patentfähigkeit für nichtig zu erklären sei.


Dies stützt sie auf folgende Anlagen und Druckschriften (Nummerierung nach
Klageschriftsatz):


             N1                 EP 1 397 895 B1 (Streitpatent)
             N2                 W0 02/098091 A2 (ursprünglich eingereichte Anmeldung)

                                     -8-


             N3           US 871117 (in Anspruch genommene Prioritätsunterlagen des Streitpatents)
             N4           DE 602 24 666 T2     (deutsche      Übersetzung    der
                          europäischen Patentschrift)
             N5           Merkmalsgliederung des Anspruchs 1 gemäß Streitpatent
             N6           Klageschriftsatz im Verletzungsverfahren vor dem
                          LG München (Aktenzeichen 21 O 6387/13)
             N7           Anspruch 1 gemäß Streitpatent mit Änderungen gegenüber der ursprünglichen Fassung
             N8           Figur zur Ausführbarkeit des streitpatentgemäßen
                          Gegenstandes
             N9           Registerauszug      zum       DPMA       Aktenzeichen
                          602 24 666.0 vom 02.08.2013


             D1de         deutsche      Übersetzung     der   Offenlegungsschrift
                          JP H05-110550
             D1fig        Zeichnungen der JP H05-110550 mit deutschen Erläuterungen
             D1jp         Offenlegungsschrift JP H05-110550
             D2           US 5,513,377
             D3           US 6,031,847
             D4/Garde     W0 99/23787 A2
             D5           EP 1 056 018 A2
             D6           US 5,692,021



Die Streithelferin der Klägerin erachtet den Gegenstand des Streitpatents wegen mangelnder Patentfähigkeit für nicht schutzfähig.

                                        -9-


Sie hat sich hierzu zusätzlich u. a. auf die Druckschrift


              B2            HOKE, J.M. [et al.]: Self-timed interface for S/390 I/O
                            Subsystem     interconnection.   In:   IBM   J.   RES.
                            DEVELOP., Vol. 43, No. 5/6 September/November
                            1999, S. 829 - 846


berufen.


Die Klägerin und die Nebenintervenientin beantragen jeweils,


        das europäische Patent 1 397 895 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
        nichtig zu erklären.


Die Beklagte beantragt,


        die Klage abzuweisen.


        Hilfsweise verteidigt sie das Patent mit den folgenden Hilfsanträgen:


        Hilfsantrag 0, überreicht in der mündlichen Verhandlung vom
        2. Dezember 2015,


        Hilfsanträge 1, 1A, 2, 2A bis 2C, 3, 3A bis 3C laut Schriftsatz
        vom 14.10.2015 (Bl. 485 ff. GA)


        Hilfsanträge 4 und 5, jeweils überreicht in der mündlichen Verhandlung vom 2. Dezember 2015.

                                       - 10 -


Wegen des Wortlauts der Hilfsanträge wird auf den Akteninhalt (Hilfsantrag 0
Bl. 624 bis 626; Hilfsanträge 1, 1A, 2, 2A bis 2C, 3, 3A bis 3C Bl. 485 bis 544,
Hilfsantrag 4 und 5 Bl. 630 bis 637) verwiesen.


Die Beklagte tritt dem Vorbringen der Klägerin und der Nebenintervenientin in
jeder Hinsicht entgegen. Sie erachtet das Streitpatent zumindest in einer der
Fassungen laut Hauptantrag und Hilfsanträgen für patentfähig.


Der Senat hat den Parteien einen qualifizierten Hinweis nach § 83 Abs. 1 PatG
mit Schreiben vom 26. August 2015 zugestellt. Wegen des Inhalts wird auf Blatt
409 bis 425 der Gerichtsakte Bezug genommen.



                         Entscheidungsgründe


                                         A.


Die zulässige Klage ist begründet.

Das Streitpatent ist nach Artikel II § 6 Absatz 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1
Buchst. a) EPÜ i. V. m. Art. 52, 56 EPÜ für nichtig zu erklären, da sowohl die
erteilte Fassung des Streitpatents als auch die Fassungen nach den Hilfsanträgen sich als nicht patentfähig erweisen.



                     I. Zum Gegenstand des Streitpatents

1.     Das in der Verfahrenssprache Englisch abgefasste Streitpatent betrifft
Verfahren und Anordnungen zum Synchronisieren von Daten, die auf einem
parallelen Datenbus weitergeleitet werden, welcher anfällig für durch Versatz
verursachte Fehler ist (vgl. Streitpatent, Abs. [0001]).

                                       - 11 -


Gemäß den Ausführungen des Streitpatents habe der erhöhte Bedarf an Halbleitervorrichtungen mit hoher Leistungsfähigkeit und hoher Funktionalität zu einem ständig steigenden Bedarf an einer weiteren Erhöhung der Geschwindigkeit geführt, mit der Daten zwischen den Schaltungsblöcken weitergeleitet würden.   Viele   derartige   Hochgeschwindigkeits-Kommunikationsanwendungen
könnten unter Verwendung einer parallelen Datenübermittlung implementiert
werden, bei der mehrere Datenbits gleichzeitig über parallele Kommunikationswege gesendet würden (vgl. Streitpatent, Abs. [0003]).

Aus dem Stand der Technik sei es bekannt, Systeme mit einer Anzahl von Modulen bereitzustellen, die über parallele Datenkommunikationsleitungen verbunden seien und miteinander kommunizierten. Dabei würden von einem sendenden Modul Daten über den Bus synchron mit einem bestimmten Takt an ein
empfangendes Modul übermittelt. Auf diese Weise würden die Übergänge auf
den parallelen Signalleitungen das sendende Modul in einer synchronen Beziehung zueinander und/oder im Takt des sendenden Moduls verlassen. Am anderen Ende der parallelen Datenverbindung empfange das empfangende Modul
die Daten auf dem parallelen Datenbus, wobei der Empfangstakt typischerweise aus dem Takt des sendenden Moduls abgeleitet werde oder synchron mit
diesem sei (vgl. Streitpatent, Abs. [0004]).

In solchen Systemen sei es vorteilhaft, sicherzustellen, dass die empfangenen
Signale (bzw. der Empfangstakt) eine spezifische Phasenbeziehung zum Sendetakt aufwiesen, um eine einwandfreie Datenrückgewinnung zu gewährleisten.
Häufig trete ein Versatz („skew“) zwischen den gesendeten Datensignalen
selbst und zwischen den Datensignalen und dem Empfangstakt am Ziel auf. Es
gäbe viele Ursachen für diesen Versatz, z. B. Übertragungsverzögerungen, die
durch die kapazitive und induktive Belastung der Signalleitungen der parallelen
Verbindung hervorgerufen würden, Variationen der E/A-(Eingang/Ausgang)-
Treiberquelle, Zwischensymbolinterferenz oder Variationen der Impedanz und
Länge der Übertragungsleitungen (vgl. Streitpatent, Abs. [0005]).

                                      - 12 -


Zum Stand der Technik verweist das Streitpatent auf das US-Patent
…, welches ein Mehrkanal-Paralleldatenübertragungssystem offenbare, bei dem eine zeitlich unveränderliche, d. h. konstante, Verzögerung bei
der Signalfortpflanzung zwischen den Kanälen automatisch kompensiert werden könne. Das empfangende Ende des Systems umfasse in jedem Kanal ein
konfigurierbares Verzögerungselement, das auf einen Integrator anspreche,
wobei der Ausgang des Verzögerungselements direkt mit diesem Integrator gekoppelt sei. Dabei werde ein alternierendes Bitmuster über jeden Kanal gesendet, um die Verzögerungselemente zu kalibrieren und eine geeignete Verzögerungskompensation für die anschließend zu empfangenden Signale sicherzustellen, die dann die gleiche Verzögerungsbeziehung aufwiesen wie die empfangenen alternierenden Bitmuster (vgl. Streitpatent, Abs. [0006]).

Für parallele Verbindungen, die Anwendungen mit höherer Geschwindigkeit
dienten, sei festgestellt worden, dass der Versatz „musterabhängig", also nicht
konstant sei, und dass dieses Problem in vielen Fällen abgeschwächt und
größtenteils überwunden werden könne. Wie in der EP … beschrieben
sei, resultiere diese Musterabhängigkeit aus den unvollkommenen Stromquellen, die von den Datenbits auf dem parallelen Bus gemeinsam genutzt würden.
Die gemeinsam genutzten Stromquellen würden einen Versatz beim Treiber
bewirken, der direkt den Toleranzbereich beim Empfänger reduziere, was wiederum    Datenübertragungsfehler     hervorrufen    könne    (vgl.    Streitpatent,
Abs. [0007]).

Herkömmlicherweise werde diesem Versatzproblem begegnet, indem die Verzögerungen auf jeder Leitung manuell eingestellt würden, wobei die Verzögerungen dabei so eingestellt würden, dass die Daten so erschienen, als ob sie
am empfangenden Ende des Busses gleichzeitig angekommen wären. Für viele
Anwendungen sei es jedoch sehr mühsam und/oder aufwendig, auf diese
Weise das Versatzproblem in den Griff zu bekommen (vgl. Streitpatent,
Abs. [0009]).

                                         - 13 -


Vor diesem Hintergrund stelle sich das Streitpatent die Aufgabe, einen Hochgeschwindigkeits-Paralleldatenkommunikationsansatz anzugeben, der diese Versatzprobleme überwinde, indem digitale Daten mit automatischer Neuausrichtung übertragen würden (vgl. Streitpatent, Abs. [0010], Z. 18 bis 21).

Zur Lösung dieser Aufgabe schlägt das Streitpatent mit dem Patentanspruch 1
eine parallele Datenkommunikationsanordnung vor, die sich - in der Verfahrenssprache Englisch und in deutscher Übersetzung – in Anlehnung an die
Merkmalsgliederung der Klägerin – in folgende Merkmale gliedern lässt:


1    A parallel data communication           Parallele Datenkommunikationsanarrangement (100) adapted to            ordnung (100),die ausgebildet ist, den
     compensate for the skewing of           Versatz digitaler Daten zu kompendigital data, comprising:               sieren, umfassend:

2    a parallel bus having parallel bus      einen parallelen Bus mit parallelen
     lines (116, 118) adapted to             Busleitungen(116, 118), die ausgebiltransfer digital data;                  det sind, digitale Daten zu übertragen;

     a first module (112) adapted to         ein erstes Modul (112), das ausgebiltransfer the digital data concur-       det ist, die digitalen Daten gleichzeitig
3
     rently on the bus lines;                auf den Busleitungen zu übertragen;
                                             wobei

4    each of the bus lines (116, 118)        jede der Busleitungen (116, 118) eine
     having an associated adjustable         zugeordnete einstellbare Datenverdata-delay circuit (216a, 216b)         zögerungsschaltung (216a, 216b)
                                             hat; und

5    the parallel bus having a clock         der parallele Bus einen Taktpfad
     path (122) adapted to carry a           (122) hat, der ausgebildet ist, ein
     clock signal for synchronizing          Taktsignal zum Synchronisieren di-

                                         - 14 -


    digital data carried over the plu-       gitaler Daten zu transportieren, die
    rality of data-carrying lines;           über die Vielzahl von Daten transportierender Leitungen transportiert werden;

6   the first module (112) adapted to        das erste Modul (112) ausgebildet ist,
    transfer the digital data concur-        die digitalen Daten gleichzeitig mit
    rently on the bus lines (116, 118)       dem Taktsignal auf den Busleitungen
    along with the clock signal, se-         (116, 118) zu übertragen, wobei von
    lected ones of the sets of data          den Datensätzen ausgewählte Daincluding at least two synchroni-        tensatze mindestens zwei Synchronization codes transferred contigu-        sierungscodes enthalten, die zusamously on the bus lines (116, 118)        menhängend auf den Busleitungen
    to toggle the bus lines with each        (116, 118) übertragen werden, um mit
    of the synchronization codes             jedem der übertragenen Synchronitransferred;                             sationscodes die Busleitungen zu
                                             schalten;

7   a second module (114) adapted            ein zweites Modul (114) vorgesehen
    to sample the synchronization            ist, das ausgebildet ist, die Synchrocodes in response to an edge of          nisierungscodes in Reaktion auf eine
    the clock signal, and validate the       Flanke des Taktsignals abzutasten,
    sampled synchronization codes;           und die abgetasteten Synchronisieand                                      rungscodes zu validieren; und

8   the adjustable data-delay circuits       dass die einstellbaren Datenverzöge-
    (216a, 216b) being responsive to         rungsschaltungen (216a, 216b) austhe validated synchronization            gebildet sind, auf die validierten Syncodes and adapted to adjust the          chronisierungscodes zu reagieren
    edge of the clock signal relative        und die Flanke des Taktsignals relativ
    to the synchronization codes.            zu den Synchronisierungscodes einzustellen.

                                          - 15 -


Das Streitpatent schlägt im nebengeordneten Patentanspruch 16 ein paralleles
Datenkommunikationsverfahren vor, das sich - in der Verfahrenssprache Englisch und in deutscher Übersetzung - wie folgt gliedern lässt:




V1 A parallel data communication              Paralleles Datenkommunikationsvermethod adapted to compensate             fahren, das ausgebildet ist, den Verfor the skewing of digital data, the     satz digitaler Daten zu kompensieren,
     method comprising:                       wobei das Verfahren umfasst:

V2 over a parallel bus having parallel        Übertragen digitaler Daten zusambus lines (116, 118) and a clock         men mit einem Taktsignal über einen
     path (122) adapted to carry a            parallelen Bus mit parallelen Busleiclock signal for synchronizing           tungen (116, 118) und einem Taktdigital data carried over the plu-       pfad (122), der ausgebildet ist, ein
     rality of data-carrying lines,           Taktsignal zum Synchronisieren digitaler Daten zu transportieren, die
                                              über die Vielzahl Daten transportierender Leitungen transportiert werden, wobei

V3 transferring the digital data con-         die digitalen Daten gleichzeitig mit
     currently along with the clock sig-      dem Taktsignal übertragen werden;
     nal;                                     und wobei

V4 selected ones of the sets of data          ausgewählte Datensätze mit minincluding at least two synchroni-        destens zwei Synchronisierungszation codes transferred contigu-        codes zusammenhängend übertraously to toggle the bus lines (116,      gen werden, um zwischen mit jedem
     118) with each of the synchroni-         der übertragenen Synchronisierungszation codes transferred;                codes den Busleitungen (116, 118)
                                              zu schalten;

                                         - 16 -



V5 receiving the transferred data,           Empfangen der übertragenen Daten,
     including sampling the synchroni-       einschließlich Abtasten der Synchrozation codes in response to an          nisierungscodes in Reaktion auf eine
     edge of the clock signal, and vali-     Flanke des Taktsignals, und Validiedating the sampled synchroniza-         ren der abgetasteten Synchronisietion codes; and                         rungscodes; und

V6 responsive to the validated syn-          in Reaktion auf die validierten Synchronization codes, time-adjus-         chronisierungscodes, zeitliches Einting the edge of the clock signal       stellen der Flanke des Taktsignals
     relative to the synchronization         relativ zu den Synchronisierungscodes by controlling an adjustab-       codes durch Steuern der einer jeweile data-delay circuit (216a, 216b)      ligen einstellbaren Datenverzögeassociated with each bus line.          rungsschaltung (216a, 216b), die jeder Busleitung zugeordnet ist.




2.    Zuständiger Fachmann auf dem einschlägigen Technikgebiet ist ein
Hochschulingenieur der Fachrichtung Elektrotechnik, der über mehrjährige
praktische Erfahrung im Bereich der digitalen elektronischen Schaltungs- und
Datenkommunikationstechnik verfügt.

3.    Ausgehend vom Fach- und Erfahrungswissen dieses Fachmanns ist von
folgendem Verständnis des Gegenstandes des Streitpatents auszugehen:

a)    Die Lehre des Streitpatents ist nach dem Merkmal 1 auf eine „parallele
Datenkommunikationsanordnung" („parallel data communication arrangement“)
gerichtet. Diese umfasst jegliche Anordnung zum Übertragen von Daten zwischen zwei Modulen bzw. Funktionsblöcken, die mittels eines parallelen Datenkommunikationspfades gekoppelt sind.

b)    Eine derartige Anordnung ist anfällig für durch Versatz verursachte Fehler (Streitpatent, Abs. [0001], „skew-caused errors“), d. h. es ist häufig ein er-

                                      - 17 -


wartetes Maß an Zeit-Versatz („time „skew““) zwischen den auf den einzelnen
Busleitungen gesendeten Datensignalen selbst und zwischen den Datensignalen und dem Empfangstakt am Ziel vorhanden (vgl. Streitpatent, Abs. [0005]).
Bezüglich der Auswirkungen des Zeitversatzes ist dem Streitpatent zu entnehmen, dass dieser Versatz zu Fehlern in der Datenübertragung führen kann (vgl.
Streitpatent, Abs. [0001], „skew caused errors“) und mittels der vorgeschlagenen Vorrichtung jegliche Fehler dieser Art vermieden werden können (vgl.
Streitpatent, Abs. [0029], Sp. 8, Z. 6 bis 7, „… the data in the FIFO buffer of
Fig. 1 for each clock domain will not have any skew-caused misalignments.“;
Unterstreichung hinzugefügt). Aus diesen Wirkungsangaben schließt der Fachmann, dass der Zeit-Versatz zwischen den einzelnen Datenleitungen auch
mehr als die zeitliche Länge eines Taktimpulses betragen kann.

c)    Gemäß Merkmal 2 umfasst die parallele Datenkommunikationsanordnung einen Bus mit parallelen Busleitungen (116,118), die ausgebildet sind, digitale Daten zu übertragen („a parallel bus having parallel bus lines (116, 118)
adapted to transfer digital data”). Für die Datenübertragung über einen solchen
Bus mit parallelen Datenbusleitungen werden die zu übertragenden Daten zunächst in einzelne Datensätze aufgeteilt, diese Datensätze wiederum in einzelne Bits, welche dann auf den mehreren Busleitungen zeitgleich abgesendet
werden, d. h. ein Datensatz wird auf einmal über die parallelen Datenleitungen
übertragen (vgl. Streitpatent, Abs. [0008] und [0021]).

d)    Soweit Merkmal 3 fordert, dass die digitalen Daten von dem ersten Modul „gleichzeitig“ („concurrently“) auf die Busleitungen übertragen werden, so
bedeutet dies, dass alle Datenbits der zu übertragenen Datensätze zum selben
Zeitpunkt von dem ersten Modul auf die parallelen Busleitungen ausgesendet
werden.

e)    Mittels der „Datenverzögerungsschaltungen“ („data delay circuit“) nach
Merkmal 4 ist es möglich, die auf den jeweiligen Busleitungen eintreffenden
Datensignale so zu verzögern, dass die Daten am Ende des Busses so erscheinen, als ob sie auf allen Busleitungen bei dem zweiten Modul gleichzeitig

                                     - 18 -


angekommen wären (vgl. Streitpatent, Abs. [0009]). Das heißt, die Datenverzögerungsschaltungen sind die wesentlichen Mittel, um den Zeitversatz auf den
einzelnen Busleitungen zu korrigieren.

f)     Gemäß Merkmal 5 ist ein „Taktpfad“ („clock path“) vorhanden, um ein
„Taktsignal“ („clock signal“) zu transportieren, das zum Synchronisieren der
über die mehreren Busleitungen transportierten digitalen Daten dient. Am anderen Ende des Busses sammelt das zweite Modul die empfangenen Datensätze
entsprechend einer vom empfangenen Taktsignal abhängigen Zeitvorgabe (vgl.
Streitpatent, Abs. [0011]).

g)     Mit der „gleichzeitigen" („concurrrently“) Übertragung der Daten auf den
Busleitungen nach Merkmal 6 ist die parallele Übertragung der Daten entsprechend Merkmal 1 und 2 gemeint.

Gemäß Merkmal 6 sind „Synchronisierungscodes“ („synchronization codes“) in
zu übertragenen Daten enthalten; auch diese werden somit parallel in einem
Datensatz übertragen (vgl. Streitpatent, Abs. [0021]). Die Übertragung von
mehreren („mindestens zwei") Synchronisierungscodes erfolgt zudem „zusammenhängend" („contiguously"), was bedeutet, dass die Synchronisierungscodes
unmittelbar aufeinanderfolgend übertragen werden.

Das Merkmal 6 sagt zunächst lediglich aus, dass zumindest zwei Synchronisationscodes zusammenhängend übertragen werden, welche die binären Zustände der Busleitungen umschalten („toggeln“). Der Fachmann erkennt dabei
jedoch zwanglos, dass vor oder hinter diesen „umschaltenden“ Synchronisierungscodes noch weitere Synchronisationscodes übertragen werden müssen.
Denn wenn nur zusammenhängende Synchronisationscodes übertragen würden, die die Busleitungen kippen (z. B. eine Taktfolge „010101“ parallel auf allen Busleitungen), so wäre das Streitpatent nicht ausführbar, da in diesem Fall
kein Versatz, der größer als ein Taktimpuls ist, erkannt werden kann. Dieses
Verständnis entspricht auch der Sicht der Beklagten in ihrer Widerspruchsbegründung.

                                     - 19 -


Dies bedeutet zur Überzeugung des Senats jedoch, dass das Merkmal 6 im
Hinblick auf eine ausführbare Offenbarung nur so ausgelegt werden kann, dass
mit den dort genannten Daten Synchronisationscodes übertragen werden, von
denen mindestens zwei Synchronisationscodes unmittelbar aufeinanderfolgend
übertragen werden, welche die Datenleitungen umschalten („toggeln“).

h)      Gemäß Merkmal 7 müssen alle gemäß Merkmal 6 gesendeten Synchronisierungscodes abgetastet und validiert werden. Das „Abtasten" („sample“)
von Synchronisierungscodes in Reaktion auf eine Taktflanke des Taktsignals
erfordert dabei, dass alle parallelen Busleitungen gleichzeitig ausgelesen
werden, d. h. es wird bei jeder Flanke des Taktsignals ein Datensatz ausgelesen. Ob es sich bei diesen ausgelesenen Datensätzen um die gesendeten
Synchronisierungscodes gemäß Merkmal 6 handelt, steht noch nicht fest, da
diese gemäß Merkmal 7 erst noch validiert werden („… and validate the
sampled synchronization codes”) und – wie oben ausgeführt – ein Versatz von
mehr als der Breite eines Taktimpuls auf einer der Datenbusleitungen vorliegen
kann.

i)      Unter dem „Validieren“ („validate“) der abgetasteten Synchronisierungscodes versteht der Fachmann die Prüfung, ob die vom zweiten Modul empfangenen parallelen Daten (Datensätze) korrekt übertragen wurden, oder ob auf
einer oder mehreren der parallelen Datenleitungen ein Versatz aufgetreten ist.
Das Ergebnis des Validierens der Synchronisierungscodes („validate the sampled synchronization codes“) ist somit die Aussage, ob die empfangenen Datensätze den gesendeten Synchronisierungscodes entsprechen (Versatz auf
keiner der Busleitungen größer als die Breite eines Taktsignals) oder nicht entsprechen (Versatz auf wenigstens einer der Busleitungen größer als die Breite
eines Taktsignals). Soweit daher in den Merkmalen 7 und 8 von Synchronisierungscodes (“synchronization codes”, Merkmal 7) oder validierten Synchronisierungscodes (“validated synchronization codes”, Merkmal 8) gesprochen wird, so
handelt es sich aus Sicht des Fachmanns dabei um Datensätze, die den vom

                                     - 20 -


ersten Modul gesendeten Synchronisierungscodes gemäß Merkmal 6 entsprechen oder nicht entsprechen.

j)     Gemäß Merkmal 8 werden die Datenverzögerungsschaltungen eingestellt, um den Zeitablauf der gesammelten Datensätze „relativ“ („relative“) zu
der Taktflanke des Taktsignals anzupassen. Dies bedeutet für den Fachmann,
dass die Datenverzögerungsschaltungen die Datensignale auf den einzelnen
Busleitungen mittels einer physischen Verzögerung relativ zu dem Taktsignal
verzögern, um den Versatz auf den entsprechenden Datenbusleitungen zu korrigieren.

Soweit die Beklagte in der mündlichen Verhandlung hiergegen eingewandt hat,
dass unter den validierten („validated“) Synchronisationscodes nur solche Synchronisationscodes zu verstehen wären, die mit den gesendeten Synchronisationscodes übereinstimmen, so kann der Senat dem nicht folgen. Ist der Versatz
auf einer Datenbusleitung größer als die Breite eines Taktimpulses, so führt das
gerade zu einer Fehlabtastung, die entscheidend für die Erkennung derartiger
Versatze ist. Dieses Verständnis wurde den Beteiligten im Rahmen des gerichtlichen Hinweises nach § 83 PatG vorab dargelegt (vgl. gerichtlicher Hinweis:
„Unter dem „Validieren“ („validate“) der abgetasteten Synchronisierungscodes
versteht der Fachmann die Prüfung, ob die vom zweiten Modul empfangenen
parallelen Daten richtig übertragen wurden oder ob in einer der parallelen Datenleitungen ein Versatz aufgetreten ist.“; „…es müssen die mindestens zwei
ausgelesenen parallelen Datensätze daraufhin geprüft (validiert) werden, ob sie
die zwei erwarteten aufeinanderfolgenden Synchronisierungscodes enthalten
oder nicht.“; Unterstreichung hinzugefügt). Diese Auslegung des Senats war der
Beklagten offensichtlich auch bewusst, da sie in der mündlichen Verhandlung
einen von ihr bereits vor der mündlichen Verhandlung vorbereiteten und im
Laufe der Verhandlung nochmals angepassten Hilfsantrag 0 eingereicht hat, mit
dem sie speziell auf diese Auslegung des Senats reagiert hat.

Der Beklagten war zu der in der mündlichen Verhandlung im Einzelnen erörterten Auslegung der Merkmale 6 bis 8 deshalb auch nicht auf ihren in der

                                      - 21 -


mündlichen Verhandlung gestellten Antrag ein Schriftsatznachlass zu gewähren, da die Voraussetzungen nach § 99 Abs. 1 PatG i. V. m. § 139 Abs. 5 ZPO
nicht vorlagen. Denn die vorstehende Auslegung der Merkmale, die von den
Auslegungsvarianten ausgeht, welche der Senat bereits in seinem Qualifizierten
Hinweis mitgeteilt hat, beruht wie oben ausgeführt auf den Ausführungen der
Beklagten. Insofern handelt es sich um keinen für die Beklagte neuen rechtlichen Gesichtspunkt. Hinzu kommt, dass die Auslegung der einzelnen Begriffe -
und dabei auch gerade diejenigen der Merkmale 6 bis 8 - zwischen den Parteien von Anfang an streitig war und von ihnen bereits schriftsätzlich ausführlich
erörtert worden war, so dass ein Erfordernis, der Beklagten hierzu erneut Gelegenheit zur Stellungnahme zu geben, nicht ersichtlich ist. Aus diesem Grund
war am Schluss der mündlichen Verhandlung der hierauf gerichtete Antrag der
Beklagten zurückzuweisen.




                           II. Zur erteilten Fassung

Es kann dahinstehen, ob der geltend gemachte Nichtigkeitsgrund nach Art. II
§ 6 Abs. 1 Nr. 2 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. b) EPÜ oder Art. II § 6
Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ für den Gegenstand des Patentanspruchs 1 gegeben ist, denn die Gegenstände des Streitpatents laut den nebengeordneten Patentansprüchen 1 und 16 der erteilten
Fassung gelten vor dem Hintergrund des Standes der Technik laut Druckschrift
B2/Hoke nicht mehr als neu i. S. d. Art. 54 Abs. 1 und 2 EPÜ.

1.    Die Druckschrift B2/Hoke betrifft einen Datenbus zur Verbindung eines
Prozessors mit einem I/O-Subsystem und das dazugehörige Datenbus-Interface, das auch als "STI" („self-timed interface“) bezeichnet wird. Die Daten werden dabei über den Datenbus von einem Sendemodul („MBA chip“) zu einem
Empfängermodul („Bridge chip“) übertragen, vgl. folgende Abbildung A:

                                      - 22 -




                        Abb. A - Figur 2 aus B2/Hoke (S. 831)


Der Datenbus weist acht Datenleitungen, eine Leitung zur Übertragung des
Taktsignals („clock“) und eine Leitung zur Übertragung von Paritätsbits auf, vgl.
folgende Abbildung B:

                                         - 23 -




             Abb. B - Figur 3 (S. 831) und Figur 6 (S. 834) aus B2/Hoke

Die Druckschrift B2/Hoke beschreibt die Übertragung von 32-Bit-Wörtern. Diese
Wörter werden in Gruppen zu je acht Bit aufgeteilt; die acht Bit einer Gruppe
(entspricht einem Datensatz) werden gleichzeitig auf dem Datenbus versandt;
die Versendung der vier Acht-Bit-Gruppen erfolgt zeitlich nacheinander, d. h.
seriell. Diesen Vorgang der Aufteilung und Nacheinander-Versendung bezeichnet die Druckschrift auch als "Serialisierung" („serialization“) (vgl. B2/Hoke,
S. 832 in Verbindung mit Fig. 4 (a)).

Beim Empfänger werden die nacheinander übersandten Acht-Bit-Gruppen wieder zu 32-Bit-Wörtern zusammengesetzt. Diesen Vorgang nennt die Druckschrift "Deserialisierung" („deserialization“) (vgl. B2/Hoke, S. 834 in Verbindung
mit Fig. 6). Die Übertragungslogik ist dabei für jede der acht Datenleitungen
identisch und wird als „one bit“ bezeichnet (vgl. B2/Hoke, S. 831, li. Spalte, unter Überschrift „STI physical send macro“).

                                     - 24 -


Aufgrund von unterschiedlichen Laufzeiten auf den einzelnen Busleitungen
kommen die gleichzeitig abgesendeten Datenbits eines Datensatzes (d. h. die
einzelnen Bits einer Acht-Bit-Gruppe) im Allgemeinen versetzt („skewed“) beim
Empfänger an (vgl. B2/Hoke, S. 835, re. Sp., letzter Absatz: „Although the data
for each conductor is launched at the same time, the arrival times at the receiver are skewed because of the variations of the individual transmission
paths,…”, i. V. m. S. 836, Fig. 8, in der von den acht Datenleitungen nur sechs
zeichnerisch dargestellt sind).

Während in dem Beispiel nach der
Figur 8 der Druckschrift B2/Hoke die
Datenleitungen A bis D bis auf die
Datenleitung B zwar nicht zentriert,
aber korrekt abgetastet werden, sind
die Datenleitungen E und F so stark
verzögert, dass es zu einer Fehlabtastung des mit der Taktflanke („clock
(R)“)    abgetasteten      Datensatzes
kommt (im Folgenden als Fall 1 bezeichnet; vgl. B2/Hoke, S. 836, re. Sp.
                                              Abb. C- Figur 8 aus B2/Hoke (S. 836)
erster Absatz, „Conductor E and Conductor F are sampled incorrectly“). Würde der Abtastzeitpunkt auf allen Leitungen wie auf den Leitungen A bis D, im Beispiel nach der Fig. 8 also auch bei
den Leitungen E und F, liegen, so wäre der Abtastzeitpunkt zunächst zwar nicht
auf allen Leitungen zentriert, aber der Datensatz würde korrekt abgetastet (was
im Folgenden als Fall 0 bezeichnet wird).

Das in der Druckschrift B2/Hoke beschriebene Inferface („STI“) stellt eine Lösung für dieses Versatzproblem vor, mit der die ankommenden Datenbits automatisch an dem empfangenen Taktsignal ausgerichtet werden (vgl. B2/Hoke,
S. 835, re. Sp. 1. Abs., „The STI provides a solution to this problem by auto-

                                       - 25 -


matically aligning the incoming data bits with the received clock.“). Hierzu sind
verschiedene Maßnahmen vorgesehen:

   a) „bit synchronization“ (vgl. B2/Hoke, S. 836, re. Sp., “The STI solution”,
       2. Absatz, „This process is known as bit synchronization“)
   b) “byte and word synchronization” (vgl. B2/Hoke, S. 842, re. Sp., “Byte and
       word synchronization”)

Aus der Druckschrift B2/Hoke geht mithin eine parallele Datenkommunikationsanordnung bzw. –verfahren hervor, die/das ausgebildet ist, den Versatz digitaler
Daten zu kompensieren (Merkmal 1; V1), wobei diese einen parallelen Bus mit
parallelen Busleitungen aufweist, die ausgebildet sind, digitale Daten zu übertragen (Merkmal 2, V2teilw). Das erste Modul (vgl. Fig. 2, „MBA-Chip“) ist ausgebildet, die digitalen Daten gleichzeitig auf die Busleitungen, gesteuert durch
die Flanke des Taktsignals, zu übertragen (vgl. B2/Hoke, S. 836, Fig. 8,
„Clock(S)“; S. 835, re. Sp. letzter Absatz: „Although the data for each conductor
is launched at the same time … “; Merkmal 3, V3).

Um den Versatz zu korrigieren, weist jede der Busleitungen eine zugeordnete
einstellbare Datenverzögerungsschaltung auf (vgl. B2/Hoke, S. 836, Fig. 9 in
Verbindung mit der zugehörigen Beschreibung; S. 843, Fig. 19 in Verbindung
mit S. 842, re. Sp., Kapitel „Byte and word synchronization“; Merkmal 4).

Der Acht-Bit-Bus von B2/Hoke weist neben den acht Datenleitungen auch eine
Leitung für ein Taktsignal, d.h. einen Taktpfad auf, der dazu ausgebildet ist, ein
Taktsignal zum Synchronisieren digitaler Daten zu transportieren, die über die
Vielzahl von Daten transportierenden Leitungen transportiert werden (vgl.
B2/Hoke, S. 830, Brückenabsatz li. Sp./re. Sp., S. 831, Fig. 3, „clock out“,
S. 834, Fig. 6, “clock in”; Merkmal 5; V2rest).

Im Rahmen eines Timing-Modus erfolgt auf dem Acht-Bit-Bus die Übertragung
eines (in Hexadezimalzahlen ausgedrückten) Timing-Musters („timing pattern“)
„FF 00 FF 00 00 00 FF 00 00 00 FF 00 00 00 FF 00“, mithin von Synchronisationscodes, wobei "FF" bzw. "00" bedeuten, dass auf allen acht Leitungen des

                                          - 26 -


Datenbusses das Bit 1 bzw. das Bit 0 übertragen wird (vgl. S. 844, li. Spalte,
unter der Überschrift „Timing mode and functional mode“). Betrachtet man eine
einzelne   Leitung,   so     wird   auf     jeder   Leitung   seriell   die   Bitfolge
„1010 0010 0010 0010“ übertragen. Diese Bitfolge hat die Eigenschaft, dass sie
aus Vierergruppen besteht, die sich alle im zweiten, dritten und vierten Bit gleichen ("010") und sich im ersten Bit unterscheiden können. Eine dies charakterisierende Kurzschreibweise lautet "X010", wobei "X" für den Bitwert 0 oder 1
steht (vgl. B2/Hoke, S. 844, li. Sp., 2. Abs.). Das erste Modul (der „MBA chip“)
ist demnach dazu ausgebildet, die digitalen Daten gleichzeitig mit dem Taktsignal auf den Busleitungen (116, 118) zu übertragen, wobei - entsprechend dem
Verständnis des Merkmals M6 - mit den Daten Synchronisationscodes übertragen werden, von denen mindestens zwei Synchronisationscodes unmittelbar
aufeinanderfolgend übertragen werden, welche die Datenleitungen schalten
(toggeln) (Merkmal 6, V4).

Die von dem ersten Modul („MBA chip“) gesendeten Daten werden von dem
zweiten Modul („Bridge chip“) empfangen (vgl. B2/Hoke, S. 831, Fig. 2). Die
Abtastung der Signale auf den Datenbusleitungen erfolgt zu demjenigen Zeitpunkt, zu dem das Taktsignal eine Flanke aufweist (vgl. Abb. C, B2/Hoke,
S. 836, Fig. 8, „Clock (R)“). Mittels der folgenden „bit synchronization“ und der
„byte and word synchronization“ wird ein ggfs. auftretender Versatz auf den einzelnen Busleitungen korrigiert.

a) „bit synchronization“

Die auf jeder Datenbusleitung vorgesehenen Maßnahme a) der „bit synchronization“ dient der Sicherstellung einer eindeutigen Abtastung. Dabei wird das
betreffende Datensignal so verzögert, dass die den Abtastzeitpunkt bestimmende Flanke des Taktsignals in der Mitte des sogenannten Datenfensters
("data window") zu liegen kommt (vgl. B2/Hoke, S. 836, 2. Abs. unter der
Überschrift "The STI Solution", „Tap D is chosen as the tap from which data is
sampled, because the sampling edge of the C2 clock falls directly into the center of the data window. This process is also known as bit synchronization.”).

                                       - 27 -


Diese dient mithin dazu, einen Versatz von weniger als einem Bit auf einer Datenbusleitung zu korrigieren. Dabei wird eine Verzögerung (“bulk delay”) für
jede Busleitung mit dem Ziel ermittelt, das Datenfenster für die Abtastung zu
zentrieren (vgl. B2/Hoke, S. 835, li. Sp. 4. Abs., „Serial data first enters the bulk
delay chain, where delay is added to each data bit on an individual basis, with
the primary goal being to center the data-bit window for sampling within the fine
delay chain“, Unterstreichungen hinzugefügt). Im Anschluss an den “Timing
mode” werden diese Werte für jede Busleitung eingefroren, d.h. dauerhaft auf
den ermittelten Wert eingestellt (vgl. B2/Hoke, S. 844, re. Sp. erster Abs., letzter
Satz, „Once timing mode is complete, the bulk delay values are frozen …“).

b) „byte und word synchronization“

Die weiteren Maßnahmen der „byte and word synchronization” (vgl. B2, S. 842,
re. Sp. ab der Überschrift) dienen dazu, die besagte Fehlzuordnung bei einem
Versatz von mehr als einem Bit zu korrigieren, wie er beispielsweise in der Figur 8 der B2/Hoke auf den Datenleitungen E und F dargestellt ist.

Dabei werden die seriell empfangenen Daten im Rahmen der „byte synchronization“ innerhalb einer Datenleitung (vgl. B2/Hoke, S. 843, li. Sp. letzter Absatz, „During timing mode, each one bit goes through byte synchronization indepentently.“; vgl. B2/Hoke, S. 843, li. Spalte in Verbindung mit den Figuren 18
und 19) auf zwei Datenleitungen aufgeteilt („Data1“ und „Data2“) und daraufhin
untersucht, ob die innerhalb jeder Datenleitung am Empfänger empfangenen
Daten in der richtigen Reihenfolge („X010“) auftreten.

Um einen eventuell auftretenden Datenversatz von mehr als einem Bustakt in
der Leitung zu korrigieren, sind Verzögerungsschaltungen für eine Verzögerung
des Datensignals zwischen 0 bis 3 Bit vorgesehen, die über entsprechende
Schalter zugeschaltet werden können, damit am Ende der Bytesynchronisation
am Ausgang jeder der Datenbusleitungen die Bitfolge „X010“ entsprechend
dem vom ersten Modul („MBA chip“) gesendeten Timing-Muster anliegt (vgl.
B2/Hoke, S. 843, li. Sp., letzter Absatz, „During timing mode, each one-bit goes

                                         - 28 -


through byte synchronization independently. The two-bit control counter is cycled until the signature detector recognizes a good signature (i.e., ‚X010‘) as
provided by the timing pattern.“ Fig. 19, Bezz. „SRL“, „Switch A“, „Switch B“),
d. h. das dritte Bit ist auf allen Datenleitungen „1“, in jeder Richtung benachbart
von einer „0“.

Für den oben genannten Fall 0 (der Versatz ist auf allen Datenbusleitungen
kleiner als 1 Bit), stimmt das empfangene Muster auf allen Leitungen mit dem
gesendeten Muster überein und die Datenverzögerung wird für diesen Fall 0 auf
allen Busleitungen auf 0 Bit eingestellt (vgl. B2/Hoke, S. 843, li. Sp. in Verbindung mit Fig. 19 und 20, „delay=0 (reference)“).




                       Abb. D - Figur 19 und Figur 20 aus B2/Hoke


Bei der im Anschluss an die „byte synchronization“ stattfindenden „word synchronization“ wird global über alle Busleitungen - also für den ausgelesenen
Datensatz - untersucht, ob für jedes empfangene Muster ‚X010‘ (vgl. B2/Hoke,
S. 843, li. Sp., 2. Absatz, letzter Satz; „For example, if the data stream is a
repeating pattern of ‚X010‘“) das erste Bit („X“-Bit) des gesendeten Timing-Musters „X010“ auf allen Busleitungen identisch ist (vgl. B2/Hoke, S. 843,
re. Sp., vorletzter Absatz, „This logic compares every cycle to ensure that the X
bits of the timing pattern are identical for each one-bit”).

Es wird somit mittels der „byte und word synchronization“ überprüft, ob das
erste Bit auf allen Datenleitungen gleich ist (entweder „0“ oder „1“) und das

                                         - 29 -


dritte Bit des ,X010‘.-Musters auf allen Leitungen „1“ ist (vgl. B2/Hoke, S. 844, li.
Sp., 2. Absatz, „Summarizing byte and word synchronization, the byte-alignment logic will adjust until the third bit of the 'X010' timing pattern is always one.
If this is not the case, it advances the two-bit counter until the condition is attained. The global synchronization logic compares all most significant bits X
(one or zero) of all one-bits to verify that they are all the same.“; Unterstreichungen hinzugefügt). Auf Grund der vorgegebenen Synchronisierungscodes
besitzt das zweite und vierte Bit zwangsläufig auf allen Busleitungen den
Wert 0. Im Ergebnis wird für alle gemäß Merkmal 6 gesendeten Synchronisationscodes      eines     jeden     Musters       (das    gesamte     Timing-Muster
„FF 00 FF 00 00 00 FF 00 00 00 FF 00 00 00 FF 00“ besteht aus vier ’X010‘
Mustern) validiert.

Mithin ist gemäß dem bekannten Stand der Technik nach der Druckschrift
B2/Hoke ein zweites Modul („Bridge chip“) vorgesehen, das ausgebildet ist, die
Synchronisierungscodes in Reaktion auf eine Flanke des Taktsignals abzutasten, und die abgetasteten Synchronisierungscodes, wozu auch die aufeinanderfolgend gesendeten Synchronisierungscodes gehören, die die Datenleitungen schalten, zu validieren (Merkmal 7, V5).

Falls das Ergebnis der Prüfung negativ ist, ist zur Korrektur bei einem auftretenden Fehler auf der entsprechenden „one bit“-Datenleitung eine (weitere) Verzögerungsschaltung vorhanden, um eine Verzögerung von 4 Bit einzustellen
(vgl. B2/Hoke, S. 843, re. Sp., vorletzter Absatz, „… and introduces an additional four bit-times of delaPy to the one-bits it affects”).

Ist das Ergebnis der Prüfung positiv, d. h. auf allen Datenbusleitungen liegt
beim Empfänger das gesendete Timing Muster an, werden die Einstellungen
sowohl der „bit synchronization“ (der Wert für „bulk delay“) als auch der „byte
and word synchronization“ eingefroren, d. h. sie werden für den folgenden
“operational mode” entsprechend eingestellt (vgl. S. 844, re. Sp., erster Abs.,
letzter Satz, „Once timing mode is complete, the bulk delay values are frozen,
as are the byte-alignment and word-alignment logic, leaving the fine delay line

                                     - 30 -


and edge-detection process to continue into operational mode.“). Mithin endet
die Verarbeitung der empfangenen Daten gemäß dieser Druckschrift ausdrücklich nicht mit dem Validieren der Datensätze, sondern es werden im Anschluss
an die Validierung die einstellbaren Datenverzögerungsschaltungen entsprechend eingestellt.

Aus diesem Grunde kann der Senat auch der von der Beklagten in der mündlichen Verhandlung vertretenen Auffassung nicht folgen, dass der Ablauf gemäß
der Druckschrift B2/Hoke nach der „Validierung“ enden und danach kein Anpassen der Datenverzögerungsschaltungen mehr stattfinden würde. Vielmehr
sind gerade die einstellbaren Datenverzögerungsschaltungen, wie eben ausgeführt, dazu ausgebildet, auf die (sowohl mit positivem auch als auch mit negativem Ergebnis) validierten Synchronisierungscodes zu reagieren und die
Flanke des Taktsignals relativ zu den Synchronisierungscodes einzustellen
(Merkmal 8, V6).

Die Gegenstände der nebengeordneten Patentansprüche 1 und 16 sind somit
nicht mehr neu gegenüber der Druckschrift B2/Hoke.

2.    Damit erübrigen sich an dieser Stelle weitere Ausführungen zur von der
Klägerin und der Nebenintervenientin geltend gemachten mangelnden Ausführbarkeit der Lehre des Streitpatents und zur angeblich unzulässigen Änderung
des Gegenstandes des Streitpatents gegenüber der ursprünglich offenbarten
Fassung.

3.    Die weiteren Patentansprüche des Hauptantrags bedürfen keiner weiteren, isolierten Prüfung, weil die Beklagte sowohl schriftsätzlich als auch in der
mündlichen Verhandlung zu erkennen gegeben hat, dass sie den Hauptantrag
als geschlossenen Anspruchssatz versteht und das Streitpatent in der Reihenfolge Hauptantrag und Hilfsanträge 0, 1, 1A, 2, 2A, 2B, 2C, 3, 3A, 3B, 3C, 4 und
5 verteidigt (vgl. BGH, Beschluss vom 27. Juni 2007 - X ZB 6/05, BGHZ 173, 47
- Informationsvermittlungsverfahren II; Beschluss vom 26. September 1996 -
X ZB 18/95, GRUR 1997, 120 - Elektrisches Speicherheizgerät; BPatG, Urteil

                                        - 31 -


vom 29. April 2008 – 3 Ni 48/06 (EU), BPatGE 51, 45 – Ionenaustauschverfahren).


                             III. Zu den Hilfsanträgen

Der erst in der mündlichen Verhandlung gestellte Hilfsantrag 0 ist ebenso wie
die weiteren in der mündlichen Verhandlung gestellten Hilfsanträge 4 und 5
entgegen dem Antrag der Klägerin nicht als verspätet zurückzuweisen, weil die
Voraussetzungen des § 83 Abs. 4 Satz 2 PatG nicht vorliegen. Denn die Berücksichtigung dieser neuen Hilfsanträge macht keine Vertagung der mündlichen Verhandlung erforderlich (§ 83 Abs. 4 Satz 1 Nr. 1 PatG). Die Beurteilung
der Zulässigkeit und Patentfähigkeit der Gegenstände nach diesen Hilfsanträgen kann nämlich ohne Weiteres anhand der bereits im Verfahren befindlichen
Druckschriften erfolgen; dementsprechend hat auch die Klägerin hierzu in der
mündlichen Verhandlung hinreichend Stellung genommen. Aus diesem Grund
war auch der Antrag der Klägerin auf Vertagung zurückzuweisen.

1. Zu Hilfsantrag 0

a)       Der in der Verfahrenssprache Englisch abgefasste nebengeordnete Patentanspruch 1 laut Hilfsantrag 0 unterscheidet sich von der erteilten Fassung
darin, dass in dem Merkmal 8 der Begriff „validated“ durch „valid“ ersetzt wird
(Änderung gegenüber der erteilten Fassung durch Streichung bzw. Unterstreichung hervorgehoben):

        8HA0   the adjustable data-delay circuits (216a, 216b) being responsive to the valid validated synchronization codes and
               adapted to adjust the edge of the clock signal relative to the
               synchronization codes.

Entsprechend ist auch das Merkmal V6 des Patentanspruchs 16 nach Hilfsantrag 0 gegenüber der erteilten Fassung geändert (V1 bis V5 sind unverändert):

                                     - 32 -


     V6HA0   responsive to the valid validated synchronization codes,
             time-adjusting the edge of the clock signal relative to the
             synchronization codes by controlling an adjustable data-delay circuit (216a, 216b) associated with each bus line.

b)    Selbst wenn man zugunsten der Beklagten von einer zulässigen Änderung ausgeht – was die Klägerin und die Nebenintervenientin bestreiten –
erweist sich das Patent mit dieser Änderung als nicht patentfähig, da die Gegenstände der Patentansprüche 1 und 16 gemäß Hilfsantrag 0 nicht neu gegenüber der Druckschrift B2/Hoke sind.

Bezüglich der unveränderten Merkmale 1 bis 7 und V1 bis V5 wird auf die Ausführungen zur erteilten Fassung verwiesen.

Mit der durchgeführten Änderung werden nach Ansicht der Beklagten die Gegenstände der Patentansprüche 1 und
16 dahingehend eingeschränkt, dass in
dem Merkmal 8 (bzw. V6) lediglich auf
Synchronisationscodes reagiert wird,
bei denen die Validierung in Merkmal 6
bzw. V5 zu einem positiven Ergebnis
geführt hat, d. h. es betrifft den Fall,
dass die empfangenen, abgetasteten
Datensätze mit den gesendeten Synchronisationscodes übereinstimmen. Es
können aus Sicht des Fachmannes damit nur Versatze von weniger als der           Abb. E- Figur 8 aus B2/Hoke (S. 836)

Breite eines Taktsignals korrigiert werden. Dieser Spezialfall betrifft den für die Offenbarung der Druckschrift B2/Hoke
zur erteilten Fassung als Fall 0 bezeichneten Umstand, dass die Taktflanke
(„clock (R)“) – wie bereits auf den Leitungen A bis D in der Figur 8 der Druckschrift B2/Hoke – auch bei den restlichen Leitungen (im Beispiel der Figur 8 die
Leitungen E und F) in einem bestimmten Bereich liegt (frühe oder späte

                                      - 33 -


Abtastung), so dass die einzelnen Datenleitungen und somit der komplette
Datensatz korrekt abgetastet wird.

Tritt dieser Fall bei der Druckschrift B2/Hoke – beispielsweise bereits zu Beginn
des „Timing Mode“ – auf, so wird auch hierbei der Abtastzeitpunkt für die empfangenen Datenbits zunächst im Rahmen der „bit synchronization“ zentriert,
wobei ein entsprechender Wert für „bulk delay“, der zu Beginn des Timing Modus auf jeder Leitung auf 0 zurückgesetzt wird (vgl. B2/Hoke S. 844, li. Sp.
Vorletzter Abs., „At the beginning of timing mode, the bulk delay of each one-bit
is reset to zero, …“), ermittelt wird (vgl. auch die Ausführungen zur „bit synchronization“ in der Druckschrift B2/Hoke im Rahmen der erteilten Patentansprüche).

Bei der Überprüfung im Rahmen der Byte- und Wortsynchronisation gemäß der
Druckschrift B2/Hoke ergibt sich im Anschluss für diesen speziellen Fall, dass
die empfangenen Datensätze mit den gesendeten Synchronisationscodes übereinstimmen (es liegt ja auf keiner Leitung ein Versatz größer als eine Taktbreite
vor). Alle gemäß der Druckschrift B2/Hoke empfangenen Datensätze entsprechen damit den gesendeten Synchronisationscodes. Es werden daraufhin für
jede Datenbusleitung sowohl der Wert für „bulk delay“ als auch der Wert für die
Byte- und Wortsynchronisation (Versatz = 0 Bit) eingefroren, d.h. sie werden im
Anschluss an das Validieren für den folgenden “operational mode” entsprechend eingestellt (vgl. B2/Hoke, S. 844, re. Sp., erster Abs., letzter Satz, „Once
timing mode is complete, the bulk delay values are frozen, as are the bytealignment and word-alignment logic, leaving the fine delay line and edge-detection process to continue into operational mode.“). Der Senat kann daher dem
Argument der Beklagten nicht folgen, dass bei der Druckschrift B2/Hoke in diesem Fall nach der Validierung der Synchronisationscodes keine Einstellung des
Taktsignals relativ zu den Synchronisationscodes im Sinne des Streitpatents
vorliegen würde.

Mithin reagieren gemäß der Druckschrift B2/Hoke die einstellbaren Datenverzögerungsleitungen auf Synchronisationscodes, bei denen die Überprüfung als

                                    - 34 -


Ergebnis eine Übereinstimmung der gesendeten mit den empfangenen Synchronisationscodes liefert, mithin auf valide („valid“) Synchronisationscodes
nach dem Verständnis der Patentinhaberin, um das Taktsignal relativ zu den
Synchronisationscodes einzustellen (Merkmal 8HA0, V6HA0).

c)    Mit keinem der nebengeordneten Patentansprüche 1 und 16 in der Fassung des Hilfsantrags 0 kann das Patent somit Bestand haben.

d)    Damit erübrigen sich an dieser Stelle weitere Ausführungen zur von
Klägerin und Nebenintervenientin geltend gemachten mangelnden Ausführbarkeit, mangelnden Klarheit und Schutzbereichserweiterung des Streitpatents in
dieser verteidigten Fassung.

2. Zu Hilfsantrag 1 und 1A

a)    Der in der Verfahrenssprache Englisch abgefasste Patentanspruch 1 laut
Hilfsantrag 1 und Hilfsantrag 1A unterscheidet sich von der erteilten Fassung
jeweils im Merkmal 6. Die Merkmale 1 bis 5, 7 und 8 bleiben unverändert.

Gemäß Hilfsantrag 1 lautet das Merkmal 6 wie folgt (Unterschied zur erteilten
Fassung durch Unterstreichung hervorgehoben):

     6HA1   the first module (112) adapted to transfer the digital data concurrently on the bus lines (116, 118) along with the clock signal, selected ones of the sets of data including at least two synchronization codes that are such characterized that they cause the bus
            lines to toggle between digital states when sent immediately after
            one another and transferred contiguously on the bus lines (116,
            118) to toggle the bus lines with each of the synchronization codes
            transferred;

Gemäß Hilfsantrag 1A lautet dieses (Unterschied zur erteilten Fassung durch
Unterstreichung hervorgehoben):

                                     - 35 -


     6HA1A   the first module (112) adapted to transfer the digital data concurrently on the bus lines (116, 118) along with the clock signal, selected ones of the sets of data including at least two synchronization codes, wherein the at least two synchronization codes are
             transferred contiguously on the bus lines (116, 118) to toggle the
             bus lines with each of the synchronization codes transferred;

Entsprechend ist jeweils auch das Merkmal V4 des Patentanspruchs 16 gemäß
Hilfsantrag 1 und 1A gegenüber der erteilten Fassung geändert.

b)    Es kann dahinstehen, ob diese Änderungen, wie die Klägerin und die
Nebenintervenientin beanstanden, zulässig sind, denn sie sind aus der Druckschrift B2/Hoke bekannt.

Bezüglichen der unveränderten Merkmale wird auf die Ausführungen zur erteilten Fassung verwiesen.

Mit diesen beiden Hilfsanträgen hat die Beklagte auf die vom Senat im gerichtlichen Hinweis nach § 83 aufgeworfenen Auslegungsvarianten zu Merkmal 6
reagiert, mit denen verdeutlicht werden soll, dass die wenigstens zwei Synchronisationscodes die Datenleitungen schalten und unmittelbar aufeinanderfolgend
übertragen werden. Durch die aus fachmännischer Sicht vorgenommene Auslegung des Patentanspruchs, wie oben unter Punkt I./3. ausgeführt, handelt es
sich bei diesen Änderungen lediglich um Klarstellungen, da der Senat zur Erreichung einer ausführbaren Offenbarung von einem derartigen Verständnis des
Merkmals 6 ausgeht. Diesbezüglich hat die Beklagte in der mündlichen Verhandlung auch nichts mehr vorgetragen.

Die Merkmale 6HA1 und 6HA1A sind somit aus den analogen Gründen, wie zur
erteilten Fassung ausgeführt, aus der der Druckschrift B2/Hoke bekannt.

c)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in den Fassungen der Hilfsanträge 1 bzw. 1A kann das Patent somit Bestand haben.

                                      - 36 -


3. Zu Hilfsantrag 2

a)    Patentanspruch 1 nach Hilfsantrag 2 unterscheidet sich von der erteilten
Fassung in dem Merkmal 7 (Änderungen gegenüber der erteilen Fassung durch
Unterstreichung hervorgehoben):

     7HA2    a second module (114) adapted to sample the sets of data including the synchronization codes in response to an edge of the clock
             signal, collect the sets of data according to timing defined as a
             function of the clock signal, and validate the sampled synchronization codes; and

Entsprechend ist auch Merkmal V5 des Patentanspruchs 16 gemäß Hilfsantrag 2 gegenüber der erteilten Fassung geändert.

b)    Mit diesen Änderungen kann eine Patentfähigkeit nicht erreicht werden,
da die beanspruchten Gegenstände nicht neu gegenüber der Druckschrift
B2/Hoke sind.

Bezüglich der unveränderten Merkmale 1 bis 6 und 8 bzw. V1 bis V4 und V6
wird auf die Ausführungen zur erteilten Fassung der Patentansprüche 1 und 16
verwiesen.

Wie zur erteilten Fassung ausgeführt, werden bei der Druckschrift B2/Hoke die
Datensätze ‚FF 00 FF 00‘ bzw. ‚00 00 FF 00‘, die die Synchronisierungscodes
gemäß Merkmal 6 enthalten, bei einer Flanke des Taktsignals abgetastet. Diese
abgetasteten Datensätze werden dort in einem gemeinsamen Prozess deserialisiert (vgl. B2/Hoke, S. 835, li. Sp., unter der Überschrift „STI physical receive
macro“; „The physical receive macro (PRM) receives the signals from the cable,
resynchronizes the data signals with the transmitted clock, and deserializes the
byte-wide data bus back into a word-wide interface for delivery to the logical
receive macro (LRM).”) und anschließend validiert. Im Rahmen dieser Deserialiserung werden von den vier nacheinander übersendeten Acht-Bit-Synchronisierungscodes die ersten drei ggfs. so verzögert, dass sie am Ausgang in ei-

                                       - 37 -


nem 32-bit Wort vorliegen. Hierzu werden die empfangenen Daten in so genannten „Latches“ gespeichert, die durch die Schalter A, B und C selektiv aktivierbar sind (vgl. B2/Hoke, Fig. 9, Bezz. A, B, C, Dout0, Dout1, Dout2, Dout3 ). Bei
diesem Speichern in Latches handelt es sich aus fachmännischer Sicht um das
Sammeln der Datensätze im Sinne des von der Beklagten vorgetragenen Verständnisses. Entgegen der Auffassung der Beklagten wird durch diese Vorgehensweise aber das Timing auf der Empfängerseite nicht zerstört. Bei dieser
Maßnahme handelt es sich vielmehr um einen Zwischenschritt, um einen - bei
der Übertragung wegen eines Versatzes auf einer oder mehrerer der parallelen
Datenleitungen „zerstörten“ - Synchronisationscodes (Versatz auf einer Datenleitung größer als ein Bit) zu rekonstruieren.

Dieses Sammeln erfolgt dabei entsprechend dem durch das Taktsignal vorgegeben Timing (vgl. B2/Hoke, S. 835, li. Sp., unter der Überschrift „STI physical
receive macro“; „… resynchronizes the data signals with the transmitted clock
…”).

Mithin geht auch das Merkmal 7HA2 aus der Druckschrift B2/Hoke neuheitsschädlich hervor.

Für den Gegenstand des Patentanspruchs 16 nach Hilfsantrag 2 gelten diese
Ausführungen entsprechend.

c)     Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung gemäß Hilfsantrag 2 kann das Patent somit Bestand haben.

d)     Bei dieser Sachlage bedarf es keiner Entscheidung, ob ein anderer der
von der Klägerin und Nebenintervenientin zu Hilfsantrag 2 genannten Nichtigkeitsgründe vorliegt.

4. Zu Hilfsantrag 2A

a)     Der Hilfsantrag 2A unterscheidet sich vom Patentanspruch 1 in seiner
Fassung nach Hilfsantrag 2 im folgenden Merkmal (Änderungen durch Unterstreichung hervorgehoben):

                                    - 38 -


     8HA2A    the adjustable data-delay circuits (216a, 216b) being responsive
              to the validated synchronization codes and adapted to adjust the
              edge of the clock signal relative to the synchronization codes,
              thereby aligning the collected sets of data relative to the clock
              signal.

Entsprechend ist auch Patentanspruch 16 gemäß Hilfsantrag 2A geändert.

b)    Es kann dahinstehen, ob diese Änderung, wie die Klägerin und die Streithelferin beanstanden, zulässig ist, denn auch dieses Merkmal ist aus der
Druckschrift B2/Hoke bekannt.

Bezüglich der gegenüber dem Hilfsantrag 2 unveränderten Merkmale wird auf
die diesbezüglichen Ausführungen zu Hilfsantrag 2 verwiesen.

Wie zur erteilten Fassung ausgeführt, wird bei der Druckschrift B2/Hoke durch
die Byte- und Wortsynchronisation mittels Datenverzögerungsschaltungen in
den einzelnen Datenleitungen ein Versatz von mehr als einem Bit korrigiert. Da
diese Datenverzögerungsschaltungen für alle empfangenen Datensätze verwendet werden, werden auch alle gesammelten Datensätze relativ zum Taktsignal im Sinne des Streitpatents eingestellt. Nichts anderes wird jedoch mit
dem Merkmal 8HA2A beansprucht, weshalb auch dieses keine Patentfähigkeit
begründen kann.

Für Patentanspruch 16 des Hilfsantrags 2A gelten diese Ausführungen entsprechend.

c)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung des Hilfsantrags 2A kann das Patent somit Bestand haben.

5. Zu Hilfsantrag 2B

a)    Der Hilfsantrag 2B unterscheidet sich im Patentanspruch 1 von der Fassung nach Hilfsantrag 2 in dem folgenden Merkmal (Änderungen gegenüber der
Fassung nach Hilfsantrag 2 durch Unterstreichung hervorgehoben):

                                    - 39 -


         7HA2B a second module (114) adapted to sample the sets of data
              including the synchronization codes in response to an edge of
              the clock signal, collect the sets of data according to timing defined as a function of the clock signal, and validate the sampled
              synchronization codes included in the collected sets of data; and

Entsprechend ist auch Merkmal V5 des Patentanspruchs 16 gemäß Hilfsantrag 2B gegenüber der Fassung nach Hilfsantrag 2 geändert.

b)    Es kann dahinstehen, ob diese Änderung, wie die Klägerin und die
Nebenintervenientin beanstanden, zulässig ist, denn auch diese Merkmale sind
aus der Druckschrift B2/Hoke bekannt.

Bezüglich der gegenüber Hilfsantrag 2 unveränderten Merkmale wird auf die
dortigen Ausführungen verwiesen.

Wie zur erteilten Fassung der Patentansprüche 1 und 16 ausgeführt, werden
die Synchronisierungscodes, die die Datenleitungen schalten, validiert, wobei
diese jeweils in den übermittelten und gesammelten Mustern ‚FF 00 FF 00‘ bzw.
‚00 00 FF 00‘ enthalten sind. Damit geht auch das Merkmal 7HA2B aus der
Druckschrift B2/Hoke hervor.

Für Patentanspruch 16 des Hilfsantrags 2B gelten diese Ausführungen entsprechend.

c)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung des Hilfsantrags 2B kann das Patent somit Bestand haben.

6. Zu Hilfsantrag 2C

a)    Bei Patentanspruch 1 nach Hilfsantrag 2C handelt es sich um eine
Zusammenfassung der Änderungen aus den Hilfsanträgen 2, 2A und 2B gegenüber der erteilten Fassung.

                                     - 40 -


Wie zu den Hilfsanträgen 2, 2A und 2B ausgeführt, sind diese geänderten
Merkmale bereits aus der Druckschrift B2/Hoke bekannt. Auch die Gegenstände der Patentansprüche 1 und 16 nach Hilfsantrag 2C sind somit gegenüber der Druckschrift B2/Hoke nicht mehr neu.

b)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung des Hilfsantrags 2C kann das Patent somit Bestand haben.

c)    Bei dieser Sachlage kann dahinstehen, ob diese Änderungen, wie die
Klägerin und die Streithelferin beanstanden, zulässig sind.

7. Zu Hilfsantrag 3

a)    Patentanspruch 1 nach Hilfsantrag 3 unterscheidet sich vom Patentanspruch 1 nach Hilfsantrag 2 in dem Merkmal 7 (Änderungen gegenüber der
Fassung nach Hilfsantrag 2 durch Unterstreichung hervorgehoben):

     7HA3    a second module (114) adapted to sample the sets of data including the synchronization codes in response to an edge of the clock
             signal, collect the sets of data according to timing defined as a
             function of the clock signal, and validate the sampled synchronization codes, wherein validating the synchronization codes includes
             searching for the synchronization codes; and

Entsprechend ist auch Merkmal V5 des Patentanspruchs 16 gemäß Hilfsantrag 3 gegenüber der Fassung nach Hilfsantrag 2 geändert.

b)    Es kann dahinstehen, ob diese Änderung, wie die Klägerin und die
Nebenintervenientin beanstanden, zulässig ist, denn auch mit diesem Merkmal
7HA3 kann eine Patentfähigkeit nicht erreicht werden.

Zur Offenbarung der Änderung gemäß Merkmal 7HA3 verweist die Beklagte auf
Absatz [0011], Spalte 3, Zeile 42 bis 48 und Absatz [0022], Spalte 6, Zeilen 6
bis 15 des Streitpatents. Die genannten Textstellen lauten (Unterstreichung hinzugefügt):

                                       - 41 -


Absatz [0011]:

        „At the receiving end, a second module collects, for each group,
        the sets of data according to timing defined as a function of the
        clock signal received for the group, and searches for the synchronization codes. ln response to these synchronization codes, the
        timing is adjusted and the data collected for each group is aligned
        with the clock signal received for the group.”

Absatz [0022]:

        “At the receiving end, a second module collects, for each group,
        the sets of data according to timing defined as a function of the
        clock signal received for the group, and attempts to validate the
        synchronization codes. ln response to these synchronization
        codes, delay circuits at the sending and/or receiving module (typically interfacing in or to each data line of the parallel bus) are activated and deactivated, in response to a feedback line, to adjust
        the timing of the data collected relative to the clock edge in each
        group. ideally, the timing is adjusted so that the data is centered at
        the clock edge.”

Wie oben unter Kapitel I./3., Gliederungspunkt i) ausgeführt, versteht der Fachmann unter dem „Validieren“ („validate“) der abgetasteten Synchronisierungscodes die Prüfung, ob die vom zweiten Modul empfangenen parallelen Daten (Datensätze) korrekt übertragen wurden, oder ob auf einer oder mehrerer der parallelen Datenleitungen ein Versatz aufgetreten ist. Es wird mithin überprüft, ob
sich der gesendete Synchronisierungscode und der empfangene Datensatz
gleichen. Diesen Vorgang wird der Fachmann auch als „Suchen“ bezeichnen,
denn dieses Verständnis ergibt sich aus den von der Beklagten genannten
Textstellen, in denen diese Begriffe als Synonyme verwendet werden (vgl. Unterstreichungen). Dass unter dem „Suchen“ etwas anderes als das „Validieren“
zu verstehen wäre, kann der Streitpatentschrift jedenfalls nicht entnommen

                                     - 42 -


werden. Es handelt sich vielmehr bei dem ergänzten "searching"-Merkmal
lediglich um eine Wiederholung des bereits im erteilten Anspruch 1 enthaltenen
"validating"-Merkmals. Der Schutzbereich des beanspruchten Gegenstandes
wird durch diese eingeführte Ergänzung gemäß Merkmal 7HA3 gegenüber der
Fassung nach Hilfsantrag 2 somit nicht verändert.

Die Gegenstände nach Patentanspruch 1 und 16 sind daher – wie zu Hilfsantrag 2 ausgeführt – gegenüber der Druckschrift B2/Hoke nicht neu.

c)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung des Hilfsantrags 3 kann das Patent somit Bestand haben.

d)    Bei dieser Sachlage bedarf es keiner Entscheidung, ob ein anderer der
von der Klägerin zu Hilfsantrag 3 genannten Nichtigkeitsgründe vorliegt.

8. Zu Hilfsantrag 3A, 3B und 3C

a)    Die Änderungen in Patentanspruch 1 bzw. 16 in der Fassung nach den
Hilfsanträgen 3A, 3B und 3C entsprechenden Änderungen in den Hilfsanträgen
2A, 2B und 2C gegenüber dem Hilfsantrag 2.

Da sich die nebengeordneten Patentansprüche 1 und 16 gemäß Hilfsantrag 2
und 3 – wie zu Hilfsantrag 3 ausgeführt – inhaltlich nicht unterscheiden, gelten
die Ausführungen bezüglich der Hilfsanträge 2A, 2B und 2C auch für die Fassungen der nebengeordneten Patentansprüche nach den Hilfsanträgen 3A, 3B
und 3C. Eine Patentfähigkeit kann dadurch nicht erreicht werden, wozu auf die
Ausführungen zu den Hilfsanträgen 2A, 2B und 2C verwiesen wird.

b)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 16 in der Fassung der Hilfsanträge 3A, 3B oder 3C kann das Patent somit Bestand haben.

                                      - 43 -


9. Zu Hilfsantrag 4

a)    Bei den nebengeordneten Patentansprüchen 1 bzw. 15 nach Hilfsantrag 4 handelt es um eine Zusammenfassung der erteilten Patentansprüche 1
und 2 bzw. 16 und 17. Die Anspruchsfassung ist somit zulässig.

Patentanspruch 1 nach Hilfsantrag 4 enthält gegenüber der erteilten Fassung
das zusätzliche Merkmal

     9HA4   wherein each adjustable data-delay circuit (216a, 216b) is further
            adapted to adjust the edge of the clock signal relative to the synchronization codes by causing the synchronization codes to be missampled by the second module (114).


und Patentanspruch 15 das zusätzliche Merkmal

     V7HA4 further including adjusting the edge of the clock signal relative to the
            synchronization codes by causing the synchronization codes to be
            missampled.


b)    Selbst wenn man von dem Verständnis der Beklagten ausgeht - was
Klägerin und Nebenintervenientin bestreiten -, dass das auf Grund einer „Fehlabtastung“ („missampled“) beanspruchte Anpassen des Taktsignals gemäß
Merkmal 9HA4 anspruchsgemäß im Anschluss an das „Validieren“ stattfindet,
kann eine Patentfähigkeit nicht erreicht werden, denn die Gegenstände dieser
nebengeordneten Patentansprüche beruhen auf keiner erfinderischen Tätigkeit
gegenüber der Druckschrift B2/Hoke.

                                     - 44 -


Wie zur erteilten Fassung des Patentanspruchs 1 ausgeführt, werden die abgetasteten Datensätze im Rahmen der
„bit synchronization“ nach dem Abtasten zentriert und damit ein Versatz von
weniger als einem Bit korrigiert. Dabei
wird das betreffende Datensignal so
verzögert, dass die den Abtastzeitpunkt
bestimmende Flanke des Taktsignals in
der Mitte des sogenannten Datenfensters ("data window") zu liegen kommt
(vgl. B2/Hoke, S. 836, 2. Abs. unter der
Überschrift "The STI Solution", „Tap D
is chosen as the tap from which data is        Abb. F- Figur 10 aus B2/Hoke (S. 837)
sampled, because the sampling edge of the C2 clock falls directly into the
center of the data window. This process is also known as bit synchronization.”).
Um dies zu erreichen, wird ein Wert für ein „bulk delay“ ermittelt. Hierzu werden
durch Verzögerung des Datensignals die Grenzen ermittelt, bei denen es zu
einer Fehlabtastung kommen würde (vgl. Fig. 10 der B2/Hoke, „C2 finds this
leading edge“; C2 finds this trailing edge“). Mithin geht aus der Druckschrift
B2/Hoke hervor, das Taktsignal relativ zu den Synchronisationscodes einzustellen, indem diese durch das zweite Modul („PRM“) fehlabgetastet werden.

Die gemäß den Patentansprüchen 1 und 15 nach Hilfsantrag 4 beanspruchten
Gegenstände unterscheiden sich lediglich darin, dass diese Einstellung nach
Merkmal 9HA4 - im Gegensatz zur Offenbarung der Druckschrift B2/Hoke - nach
der „Validierung“ der empfangenen Datensätze stattfindet. Als das zu lösende
technische Problem ergibt sich somit aus fachmännischer Sicht, einen Versatz,
der möglicherweise durch unterschiedliche Laufzeiten in der Elektronik des
zweiten Moduls im Rahmen der „byte and word synchronization“ auftreten kann,
zu kompensieren.

                                      - 45 -


Stellt der Fachmann bei der Nacharbeitung der Lehre der Druckschrift B2/Hoke
fest, dass es bei der Verarbeitung der Daten in dem Empfangsmodul zu einer
derartigen Versatzproblematik kommt, so hat er auch Veranlassung, sich auch
mit der Lösung des Problems zu beschäftigen, da die Druckschrift B2/Hoke gerade auch eine Lösung von Versatzproblemen offenbart (vgl. B2/Hoke, S. 835,
re. Sp., letzter Absatz: „Although the data for each conductor is launched at the
same time, the arrival times at the receiver are skewed because of the variations of the individual transmission paths, …”). Dabei liegt es für ihn auf der
Hand, die ihm bereits aus dieser Druckschrift bekannte Maßnahme der „bit synchronization“ ggfs. (auch) nach der „Validierung“ der Datensätze durchzuführen.
Einer erfinderischen Tätigkeit bedarf es hierzu nicht.

c)    Mit keinem der nebengeordneten Patentansprüche 1 bzw. 15 in der Fassung des Hilfsantrags 4 kann das Patent somit Bestand haben.

10. Zu Hilfsantrag 5

a)    Patentanspruch 1 in der Fassung nach Hilfsantrag 5 unterscheidet sich
von der erteilten Fassung in den Merkmalen

     7HA5    a second module (114) adapted to sample the synchronization
             codes in response to an edge of the clock signal, and validate the
             sampled contiguously transferred synchronization codes; and

     8HA5    the adjustable data-delay circuits (216a, 216b) being responsive to
             the validated contiguously transferred synchronization codes and
             adapted to adjust the edge of the clock signal relative to the synchronization codes.

Entsprechend sind jeweils auch die Merkmale V5 und V6 des Patentanspruchs
16 des Hilfsantrags 5 gegenüber der erteilten Fassung geändert.

b)    Auch diese Änderungen können eine Patentfähigkeit nicht begründen.

                                     - 46 -


Wie bereits zur erteilten Fassung der nebengeordneten Patentansprüche 1 und
16 ausgeführt (vgl. Abschnitt II.), werden gemäß der Druckschrift B2/Hoke alle
zusammenhängend auf den Busleitungen übertragenen Synchronisierungscodes („contigously transferred synchronization codes“) validiert und die einstellbaren Datenverzögerungsschaltungen reagieren auf diese Synchronisationscodes. Somit sind die Gegenstände der nebengeordneten Patentansprüche 1 und
16 nicht neu gegenüber der Druckschrift B2/Hoke.

c)    Bei dieser Sachlage bedarf es keiner Entscheidung, ob ein anderer der
von der Klägerin zu Hilfsantrag 5 genannten Nichtigkeitsgründe vorliegt.

11. Unteransprüche

Nachdem die unabhängigen Patentansprüche sich somit in keiner der verteidigten Fassungen als patentfähig erweisen, ist das Streitpatent auch hinsichtlich der hierauf unmittelbar oder mittelbar rückbezogenen Unteransprüche für
nichtig zu erklären, da bis auf den Patentanspruch 2 (vgl. Hilfsantrag 4) weder
geltend gemacht wurde noch ersichtlich ist, dass sie etwas eigenständig Patentfähiges enthalten (BGH, Urteil vom 29. September 2011 - X ZR 109/08,
GRUR 2012, 149 Rn. 96 - Sensoranordnung).


                                       IV.

Das Patent kann somit in keiner der verteidigten Fassungen Bestand haben.


                           B. Kostenentscheidung

Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO,
die Entscheidung über die vorläufige Vollstreckbarkeit auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.


                          C. Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

                                     - 47 -


Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof
und Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I
S. 2130) eingereicht werden kann, muss von einer in der Bundesrepublik
Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von
einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit
einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit
einer fortgeschrittenen elektronischen Signatur versehen sein. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung gerichtet
wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.


Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches Dokument in die elektronische Poststelle des Bundesgerichtshofes
(www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist
beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist
ist nur gewahrt, wenn die Berufung vor Fristablauf beim Bundesgerichtshof
eingeht.




Schwarz            Hartlieb        Gottstein      Albertshofer           Wollny


                                                                             Hu
