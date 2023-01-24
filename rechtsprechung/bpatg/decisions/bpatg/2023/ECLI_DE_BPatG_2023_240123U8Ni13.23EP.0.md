---
ecli: "ECLI:DE:BPatG:2023:240123U8Ni13.23EP.0"
court: "Bundespatentgericht"
spruchkoerper: "8"
aktenzeichen: "8 Ni 13/23"
decided: "2023-01-24"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=1&nr=43432&anz=529&pos=28&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2023-01-24_8_Ni_13_23_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 8 Ni 13/23 vom 2023-01-24

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                       Verkündet am
                                                      24. Januar 2023
8 Ni 13/23 (EP)                                              …

(Aktenzeichen)


                     In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:240123U8Ni13.23EP.0

                                        -2-



                betreffend das europäische Patent EP 2 079 267
                               (DE 60 2009 055 328)


hat der 8. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 24. Januar 2023 durch die Vorsitzende Richterin
Grote-Bittner sowie die Richter Dipl.-Ing. Altvater, Dipl.-Ing. Matter, Dr. Meiser und
Dipl.-Ing. Tischler


für Recht erkannt:



        I.     Die Klage wird abgewiesen.

        II.    Die Klägerin hat die Kosten des Rechtsstreits zu tragen.

        III.   Das Urteil ist wegen der Kosten gegen Sicherheitsleistung in
               Höhe von 120 % des jeweils zu vollstreckenden Betrages
               vorläufig vollstreckbar.



                                   Tatbestand


Die Nichtigkeitsklage richtet sich gegen das u.a. mit Wirkung für die Bundesrepublik
Deutschland erteilte europäische Patent 2 079 267 mit der Bezeichnung „Method
for adjusting transmission timing and transmitting continuous packets and mobile
station threreof“, das am 7. Januar 2009 unter Inanspruchnahme der Priorität der
koreanischen Patentanmeldung 20080003517 vom 11. Januar 2008 angemeldet
und dessen Erteilung am 31. Oktober 2018 veröffentlicht worden ist. Das
Streitpatent wird beim Deutschen Patent- und Markenamt unter der Nr.
60 2009 055 328 geführt, Patentinhaberin ist die Beklagte.


Das Streitpatent umfasst in seiner erteilten Fassung 14 Ansprüche mit den
unabhängigen Patentansprüchen 1 und 8 und den auf diese rückbezogenen
Unteransprüchen 2 bis 7 sowie 9 bis 14. Die Klägerin, die das Streitpatent mit

                                                -3-



Ausnahme der Ansprüche 6 und 13 angreift, macht die Nichtigkeitsgründe der
unzulässigen Erweiterung, nicht ausführbaren Offenbarung und der mangelnden
Patentfähigkeit geltend. Die Beklagte verteidigt das Streitpatent in der erteilten
Fassung.


Der Patentanspruch 1 lautet, versehen mit einer Merkmalsgliederung und unter
Korrektur von offensichtlichen Übersetzungsfehlern in den Merkmalen 3.1, 3.1.1
und      3.3    (korrigierte   Übersetzung       durch     Unterstreichung   hervorgehoben,
Formulierungen der Patentschrift und umgestellte Merkmale in eckigen Klammern)
wie folgt:


             in der Verfahrenssprache Englisch           Übersetzung
 1           A method of transmitting, [1.3] an Verfahren zum Übertragen                eines
             uplink subframe                    Uplink-Unterrahmens,
 1.1         including a plurality of symbols            der eine Mehrzahl von Symbolen [1.2]
                                                         enthält,
 1.2         in a cellular mobile communication in  einem      zellularen              Mobilsystem,                            kommunikationssystem
 1.3         by user equipment, UE,                      durch ein Benutzergerät        (User
                                                         Equipment, UE),
 2           wherein each symbol includes a cyclic wobei jedes Symbol ein zyklisches
             prefix and a data part,               Präfix und einen Datenteil enthält,
 3           the method comprising:                      wobei das     Verfahren    Folgendes
                                                         umfasst:
 3.1         receiving, by the UE,         a    timing Empfangen eines Zeitanpassungsadjustment command                        befehls [Zeitsteuerungsbefehls] durch
                                                       das UE
 3.1.1       for indicating an advance of a zum Anzeigen einer Vorverlegung
             transmission timing of the uplink [eines      Fortschritts]   eines
             subframe                          Übertragungszeitpunkts des Uplink-Unterrahmens
 3.1.2       relative to a current transmission in Bezug auf einen                   aktuellen
             timing;                            Übertragungszeitpunkt;
 3.2         transmitting, by the UE, a previous Übertragen eines vorherigen Uplinkuplink subframe to which the current Unterrahmens durch das UE, auf den
             transmission timing is applied; and  der aktuelle Übertragungszeitpunkt
                                                  angewendet wird; und
 3.3         when the previous uplink subframe is wenn    der           vorherige      Uplinkoverlapped with the uplink subframe Unterrahmen            mit  dem       Uplink-

                                            -4-



        due to the advance of the transmission Unterrahmen       aufgrund      der
        timing of the uplink subframe,         Vorverlegung [des Fortschritts] des
                                               Übertragungszeitpunkts des Uplink-Unterrahmens überlappt,
3.3.1   transmitting, by the UE, a part of the Übertragen eines Teils des Uplinkuplink subframe                        Unterrahmens durch das UE,
3.3.2   that is next to the overlapped part of der sich neben dem überlappten Teil
        the uplink subframe,                   des Uplink-Unterrahmens befindet,
3.3.3   without transmitting the overlapped ohne den                  überlappten    Teil    zu
        part,                               übertragen,
3.3.4   wherein the overlapped part of the             wobei der überlappte Teil des Uplinkuplink subframe includes at least a part       Unterrahmens mindestens einen Teil
        of a cyclic prefix of a starting symbol of     eines zyklischen Präfixes eines
        the uplink subframe.                           Startsymbols       des        Uplink-Unterrahmens enthält.


Der ebenfalls angegriffene nebengeordnete Patentanspruch 8 ist auf ein
Benutzergerät    gerichtet.    Anspruch       8       wiederholt    im    Wesentlichen       die
Verfahrensmerkmale       des    Anspruchs         1     als   funktionale    Merkmale        des
Benutzergeräts und dessen Komponenten, wie die Gegenüberstellung der
Ansprüche 1 und 8 in der Verfahrenssprache Englisch zeigt (Unterschiede durch
den Senat hervorgehoben):


        Anspruch 8                                     Anspruch 1
1       A user equipment (710) configured to A method of transmitting, [1.3] an
        perform communication [1.2] by using uplink subframe
        an uplink subframe
1.1     including a plurality of symbols,              including a plurality of symbols
1.2     in a cellular mobile system                    in a cellular mobile communication
                                                       system,
1.3                                                    by user equipment, UE,
2       wherein each symbol includes a cyclic wherein each symbol includes a cyclic
        prefix and a data part,               prefix and a data part,
3       the user equipment comprising:                 the method comprising:
        a wireless communication unit (712)
        configured to
3.1     receive a timing adjustment command            receiving, by the UE,         a    timing
                                                       adjustment command

                                             -5-



 3.1.1   for indicating an advance of a for indicating an advance of a
         transmission timing of the uplink transmission timing of the uplink
         subframe                          subframe
 3.1.2   relative to a current transmission relative to a current transmission
         timing,                            timing;
 3.2     to transmit a previous uplink subframe transmitting, by the UE, a previous
         to which the current transmission uplink subframe to which the current
         timing is applied and to transmit the transmission timing is applied; and
         uplink subframe according to the timing
         adjustment command; and
         a subframe generating unit configured
         to generate the uplink subframe,
         wherein
 3.3     when the previous uplink subframe is         when the previous uplink subframe is
         overlapped with the uplink subframe          overlapped with the uplink subframe
         due to the advance of the transmission       due to the advance of the transmission
         timing of the uplink subframe,               timing of the uplink subframe,
         the wireless communication unit (712)
         is configured to
 3.3.1   transmit a part of the uplink subframe       transmitting, by the UE, a part of the
                                                      uplink subframe
 3.3.2   that is next to the overlapped part of that is next to the overlapped part of
         the uplink subframe,                   the uplink subframe,
 3.3.3   without transmitting the overlapped without transmitting the overlapped
         part,                               part,
 3.3.4   wherein the overlapped part of the           wherein the overlapped part of the
         uplink subframe includes at least a part     uplink subframe includes at least a part
         of a cyclic prefix of a starting symbol of   of a cyclic prefix of a starting symbol of
         the uplink subframe.                         the uplink subframe.



Wegen des Wortlauts der weiteren Patentansprüche wird auf die Streitpatentschrift
verwiesen.


Die Klägerin vertritt unter Bezugnahme auf die ursprünglichen Anmeldeunterlagen
(vorgelegt als Anlage NK2) die Auffassung, der Gegenstand des Streitpatents in der
erteilten Fassung sei unzulässig erweitert durch die im Verfahrensanspruch 1
aufgenommenen Formulierungen bei den Merkmalsgruppen 3.1 und 3.3 sowie dem
Merkmal 3.2, die nicht in der ursprünglichen Anmeldung enthalten gewesen seien.

                                       -6-



Dies gelte gleichermaßen für den Patentanspruch 8; auch die Unteransprüche 2
und 9 sowie 3 und 10 seien unzulässig geändert worden.


Außerdem seien die Gegenstände der Ansprüche 1 und 8 hinsichtlich des Merkmals
3.1 und der Merkmalsgruppe 3.3 nicht so deutlich und vollständig offenbart, dass
ein Fachmann sie ausführen könne.


Ihr Vorbringen zur fehlenden Patentfähigkeit stützt die Klägerin insbesondere auf
folgende Dokumente:


NK7          IPWireless et al: Tdoc R1-074935 - „Operation of Half Duplex“; 3GPP
             TSG RAN WG1#51, Jeju, Südkorea, November 2007
NK8          IPWireless et al: Tdoc R1-075018 - „Configuration of shortened
             regions“; 3GPP TSG RAN WG1#51, Jeju, Südkorea, November 2007
NK9          Mitsubishi Electric et al: R1-051096 - „Idle period and frame designs
             for half duplex communications“; TSG RAN WG1, San Diego, USA,
             Oktober 2005
NK10         3GPP TS 36.213 V8.1.0 (2007-11) – Physical layer procedures
NK10a        3GPP TS 36.211 V8.1.0 (2007-11) – Physical Channels and
             Modulation
NK11         WO 2007/073701 A1
NK12         WO 2007/024558 A1


Sie meint, dass der Gegenstand des Anspruchs 1 durch die Druckschriften
NK10/NK10a neuheitsschädlich vorweggenommen sei. Jedenfalls beruhe er
aufgrund der Zusammenschau der Druckschriften NK10/NK10a mit der NK11 oder
der NK12 oder in Verbindung mit Fachwissen, belegt durch die NK9, nicht auf
erfinderischer Tätigkeit. Aus den gleichen Gründen seien auch der unabhängige
Patentanspruch 8 sowie die Unteransprüche nicht patentfähig. Zu den
Nichtigkeitsgründen führt die Klägerin im Einzelnen näher aus.


Der Senat hat den Parteien einen qualifizierten Hinweis vom 28. März 2022 erteilt.

                                            -7-



Die Klägerin beantragt,
          das europäische Patent 2 079 267 im Umfang der Patentansprüche 1, 2,
          3, 4, 5, 7 sowie 8, 9, 10, 11, 12, 14 mit Wirkung für das Hoheitsgebiet der
          Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,
          die Klage abzuweisen.


Sie tritt dem Vorbringen der Klägerin in allen Punkten entgegen und meint, dass der
Gegenstand des Streitpatents in der erteilten Fassung weder unzulässig erweitert
noch nicht ausführbar offenbart und darüber hinaus patentfähig sei. Denn keine der
von der Klägerin angeführten Druckschriften würde den Gegenstand des
Streitpatents neuheitsschädlich vorwegnehmen oder eine fehlende erfinderische
Tätigkeit begründen können. Hierzu führt die Beklagte im Einzelnen weiter aus.


Wegen der weiteren Einzelheiten des Sach- und Streitstandes wird auf die
Schriftsätze der Parteien nebst Anlagen und den weiteren Inhalt der Akte Bezug
genommen.



                             Entscheidungsgründe


Die Nichtigkeitsklage, mit der die Nichtigkeitsgründe der unzulässigen Erweiterung,
nicht ausführbaren Offenbarung und der mangelnden Patentfähigkeit geltend
gemacht werden (Art. II § 6 Abs. 1 S. 1 Nr. 1, Nr. 2, Nr. 3 IntPatÜG i. V. m. Art. 138
Abs. 1 lit. a), b), c), Art. 54, Art 56 EPÜ), ist zulässig.

Die Nichtigkeitsklage ist aber unbegründet, weil sich der Gegenstand des
Streitpatents im angegriffenen Umfang sowohl als ausführbar offenbart und als
patentfähig erweist und auch nicht unzulässig erweitert worden ist, mithin
rechtsbeständig ist.

                                         -8-



                                          I.

1.    Das Streitpatent betrifft ein Verfahren zur Anpassung des senderseitigen
Übertragungszeitpunktes bei der kontinuierlichen Übertragung von Datenpaketen,
ein Verfahren zur kontinuierlichen Übertragung von Datenpaketen sowie eine
entsprechende Mobilstation (vgl. Streitpatentschrift, Abs. 0001 i. V. m. 0037 ff).


Dabei geht das Streitpatent von einem orthogonalen Frequenzmultiplexverfahren
(Orthogonal Frequency Division Multiplexing, OFDM) in Funkzugangssystemen
aus. Hierzu erläutert das Streitpatent zunächst Grundlagen des orthogonalen
Frequenzmultiplexverfahrens,      welches      mehrere    orthogonale   Träger       zur
Datenübertragung verwende. Dabei werde ein Datenstrom mit hoher Datenrate in
eine Anzahl Teildatenströme mit niedriger Datenrate aufgeteilt, die gleichzeitig unter
Verwendung einer Mehrzahl von Trägern (die als „sub-carrier“ bezeichnet werden)
übertragen    würden.   Obwohl    sich   die    Frequenzkomponenten      der     Träger
überlappten, könnten die einzelnen Signale beim Empfänger unterschieden
werden, da die Träger orthogonal seien. Die Mehrzahl paralleler Datenströme werde
dabei durch einen Seriell-nach-parallel-Wandler aus dem Datenstrom mit hoher
Datenrate erzeugt und die parallelen Teildatenströme zur Empfängerseite
übertragen. Mit Hilfe von Mehrfachzugangsverfahren (Orthogonal Frequency
Division Multiple Access, OFDMA) könnten einzelne oder mehrere orthogonale
Subträger unterschiedlichen Nutzern zugewiesen werden. Als Beispiel für ein
OFDMA-Schema nennt das Streitpatent SC-FDMA (Single Carrier Frequency
Division Multiple Access) (Abs. 0002 bis 0007, 0030).


Der linke Bereich der Figur 2 des Streitpatents zeigt den Zusammenhang zwischen
Unterrahmen     (subframe),    Symbolen        (symbol)   und   dem     Start-    bzw.
Übertragungszeitpunkt (start timing bzw. transmission timing). Der Unterrahmen
umfasst eine definierte Zahl an Symbolen, bspw. OFDM-Symbolen (OFDM symbol),
wobei jedes Symbol mit einem einleitenden zyklischen Präfix (cyclic prefix, CP)
beginnt. Dieses Präfix soll als Schutzintervall (guard interval) die Störung zwischen
aufeinanderfolgenden Symbolen verhindern, die aufgrund einer unterschiedlichen

                                             -9-



Verzögerung (multipath delay spread) der parallel genutzten Kanäle (sub-carrier)
und/oder aufgrund von Frequenzunterschieden zwischen den Oszillatoren der
Mobil- und der Basisstation entstehen kann (Abs. 0004, 0012, 0031, 0032, 0058):




                             [Fig. 2; farbliche Hervorhebungen und
                         Bezeichnungen durch den Senat ergänzt]


Figur 2 des Streitpatents zeigt zudem im mittleren und rechten Teil der Abbildung –
am Beispiel einer nicht-kontinuierlichen Übertragung – einen Zeitanpassungsbefehl
(subframe start timing adjustment command) und das zugehörige Vorverlegen des
Startzeitpunkts für den (darauffolgenden) Unterrahmen (subframe start timing).


Das Streitpatent geht davon aus, dass es bei einer Anpassung des
Übertragungszeitpunkts (transmission timing) zu Kollisionsproblemen kommen
könne. Falls die Übertragungsseite kontinuierlich Pakete übermittele, könnten zwei
aufeinander folgende Pakete (continuous packets) kollidieren bzw. überlappen,
wenn der Übertragungszeitpunkt vorverlegt (advanced) werde, d.h. wenn während
einer kontinuierlichen Übertragung von Paketen die Benutzereinheit von der
Basisstation einen Anpassungsbefehl (transmission timing adjustment command)
zur Vorverlegung des Startzeitpunkts der Übertragung erhalte und ausführe (Abs.
0008, 0037-0039). Dieser Fall der zeitlichen Überlappung aufgrund eines
Anpassungsbefehls zum Vorverlegen des Startzeitpunkts der Übertragung bei einer
kontinuierlichen Übertragung ist im folgenden Ausschnitt der Figur 3 des
Streitpatents dargestellt:

                                          - 10 -




                [aus Fig. 3; farbliche Hervorhebung durch den Senat ergänzt]


Davon ausgehend liegt der Erfindung die Aufgabe zugrunde, ein Verfahren zur
Anpassung des Übertragungszeitpunkts auf der Senderseite bereitzustellen,
welches dazu eingerichtet ist, eine Verschlechterung der Empfangsqualität zu
verhindern und die Empfangskomplexität zu minimieren, wenn die Senderseite den
Übertragungszeitpunkt bei einer drahtlosen Datenübertragung ändert, bei der
zyklische Präfixe zum Verhindern einer Verschlechterung der Empfangsqualität
durch Effekte der Mehrfachpfad-Technologie (delay spread, timing misalignment)
verwendet werden (vgl. Streitpatentschrift, Abs. 0012). Außerdem sollen ein
Verfahren zur kontinuierlichen Übermittlung von Paketen unter Verwendung des
Verfahrens zur Anpassung des Übertragungszeitpunkts sowie eine Mobilstation
bereitgestellt werden, auf die das Verfahren zur kontinuierlichen Übermittlung von
Paketen angewandt wird (vgl. Streitpatentschrift, Abs. 0013, 0014).


Diese Aufgabenstellung richtet sich an einen Fachmann, der als Ingenieur mit
einem universitären Abschluss (Diplom oder Master) der Fachrichtung Elektro- oder
Nachrichtentechnik über eine mehrjährige Berufserfahrung sowie einschlägige
Kenntnisse    auf     dem    Gebiet     der     drahtlosen     Kommunikationsverfahren
und -protokolle verfügt. Bei diesem Fachmann werden Kenntnisse der vor dem
Prioritätszeitpunkt    geltenden      einschlägigen        Normen,       Standards   und
Standardisierungsbemühungen als bekannt vorausgesetzt.

                                        - 11 -



2.    Die Merkmale der Patentansprüche 1 und 8 bedürfen der Erläuterung.


Der Patentanspruch 1 ist auf ein Verfahren zum Übertragen eines Uplink-Unterrahmens (uplink subframe) (Merkmal 1) durch ein Benutzergerät (user
equipment, UE) (Merkmal 1.3) in einem zellularen Mobilkommunikationssystem
(cellular mobile communication system) (Merkmal 1.2) gerichtet. Die Angabe
„Uplink“ bezeichnet eine Datenübertragung vom Benutzergerät an einen
Netzwerkknoten (network node), bspw. an eine Basisstation (Base Station, BS) (vgl.
Streitpatent, Abs. 0060). Der Uplink-Unterrahmen enthält nach Merkmal 1.1 eine
Mehrzahl von Symbolen (plurality of symbols). In Merkmal 2 ist definiert, dass jedes
Symbol (symbol) ein zyklisches Präfix (cyclic prefix / CP) und einen Datenteil (data
part) umfasst.


Über die Darstellung in Figur 2 hinaus definiert das Streitpatent den Begriff „Uplink-Unterrahmen“ (uplink subframe) nicht. Ein „Rahmen“ (frame) bezeichnet in der
digitalen Übertragungstechnik und Nachrichtentechnik üblicherweise eine Einheit
der Datenübertragung (vgl. bspw. en.wikipedia.org: Frame (networking); NK10a,
Seite 10, Kap. 4 und 4.1). Bei der Paketvermittlung ist der Rahmen ein Container
für ein Datenpaket des Netzwerks, der neben den Nutzdaten weitere Protokoll- und
ggf. Synchronisierungs-Informationen enthält.
Auch der Begriff „Symbol“ (symbol) ist im Streitpatent über die Darstellung in Figur 2
hinaus nicht näher definiert. Es wird nur darauf verwiesen, dass der Begriff „Symbol“
OFDM- und SC-FDMA-Symbole umfassen soll (vgl. Streitpatent, Abs. 0030; NK10a,
Seite 10, letzter Satz); das Streitpatent ist aber nicht auf diese beschränkt. Als
„Symbol“    (symbol)     wird   in    der      digitalen   Übertragungstechnik    und
Nachrichtentechnik üblicherweise die jeweilige Zeicheneinheit zur Übertragung des
Informationsgehaltes     bezeichnet    (vgl.     bspw.     de.wikipedia.org:   Symbol
(Nachrichtentechnik)).
Das Streitpatent verwendet im Zusammenhang mit der Übertragung der Daten auch
den Begriff „Pakete“ (packets) (vgl. bspw. Titel und Beschreibung zu Figuren 2, 3,
5, 6 und 8). Mit der Übertragung von „Paketen“ nimmt das Streitpatent implizit auf

                                           - 12 -



Datenpakete (im Sinne von Paketvermittlung / packet switching) in Abgrenzung zur
übertragenen Information Bezug. Der Begriff „Pakete“ selbst ist in der Anmeldung
nicht definiert und wird daher vom Fachmann als allgemeiner Oberbegriff für die
übertragenen Dateneinheiten – unabhängig von einer bestimmten Technologie oder
Protokollebene – verstanden.


Wie aus der Problembeschreibung in Absatz 0012 des Streitpatents folgt, dient das
zyklische Präfix (cyclic prefix) dazu, die Verschlechterung der Empfangsqualität zu
verhindern,     die     in    drahtlosen   Kommunikationssystemen      aufgrund    der
Ausbreitungsverzögerung oder durch nicht angepasste Zeitgeber verursacht wird (a
cyclic prefix (CP) for preventing deterioration in reception performance due to delay
spread or timing misalignment). Die in Absatz 0012 genannten Effekte (delay
spread; timing misalignment) können zu Intersymbolinterferenzen führen, da es
durch sie bei der Übertragung zu einer (teilweisen) Überlagerung von Symbolen
kommen kann. Das jeweilige Präfix dient üblicherweise (unter anderem) als
Schutzintervall (guard interval), das die Symbole voneinander trennt und die
Intersymbolinterferenz verringern kann (vgl. Abs. 0004 i. V. m. 0012).
Damit beschreibt das Streitpatent die gebräuchliche Verwendung eines „Präfix“, wie
sie dem Fachmann auf dem Gebiet der digitalen Übertragungstechnik und der
Nachrichtentechnik vertraut ist.


Das       Verfahren   umfasst      nach    Merkmal    3.1   das   Empfangen       eines
Zeitanpassungsbefehls (timing adjustment command) durch das Benutzergerät, der
angibt, einen Übertragungszeitpunkt des Uplink-Unterrahmens in Bezug auf einen
aktuell     geltenden        Übertragungszeitpunkt   (current   transmission   timing)
vorzuverlegen (Merkmale 3.1.1, 3.1.2). Dabei wird auf den vorherigen Uplink-Unterrahmen (noch) der aktuell geltende Übertragungszeitpunkt angewendet
(Merkmal 3.2).
Als Übertragungszeitpunkt („transmission timing“, auch als „start timing“ bezeichnet)
ist im Kontext des Streitpatents aus fachmännischer Sicht der Startzeitpunkt der
Übertragung des jeweiligen Datenpakets, bspw. eines Unterrahmens, zu verstehen,

                                        - 13 -



soweit das Streitpatent auf die Übertragung eines bestimmten Symbols oder
Unterrahmens Bezug nimmt. Der Zeitanpassungsbefehl bezieht sich damit auf die
Anpassung des Startzeitpunkts, beginnend mit der darauf folgenden Übertragung.
Allgemein versteht der Fachmann den – auch in der deutschsprachigen
Fachliteratur verwendeten Begriff - „Timing“ im Sinne einer „Zeiteinteilung“ oder
„Zeitplanung“, denn der Startzeitpunkt für die Übertragung eines Uplink-Unterrahmens ist durch die Ressourcenzuweisung für die Uplink-Übertragung und
die vorgegebene Struktur der Datenpakete (Symbol, Unterrahmen) bestimmt und
beschreibt auch die (geplanten) Zeitpunkte, an denen jeweils die Übertragung der
Unterrahmen bei einer kontinuierlichen Übertragung starten (vgl. Fig. 2, 3). Die
Kenntnis dieser Zeitbeziehungen ist dem Fachwissen zuzurechnen, wie
beispielsweise der als Dokument NK10 bzw. NK10a vorgelegte LTE-Standard
verdeutlicht (vgl. NK10, S. 7, Abschnitt 4.2.4 i. V. m. NK10a, S. 9, Fig. 4.1-1). Damit
gilt für den als „vorherigen Uplink-Unterrahmen“ bezeichneten Unterrahmen der
„aktuelle Übertragungszeitpunkt“ (current transmission timing) und für den „Uplink-Unterrahmen“, welcher den als nächstes zu übertragenden Unterrahmen
bezeichnet, gilt der angepasste, vorverlegte Startzeitpunkt.


Nach Merkmal 3.3 überlappt der „vorherige Uplink-Unterrahmen“ (previous uplink
subframe) mit dem als „Uplink-Unterrahmen“ (uplink subframe) bezeichneten
folgenden Unterrahmen aufgrund der Vorverlegung des Übertragungszeitpunkts für
diesen „Uplink-Unterrahmen“, sofern es sich um eine kontinuierliche Übertragung
handelt, wie sie bspw. in Figur 3 dargestellt ist. In diesem Fall wird nach den
Merkmalen 3.3.1 und 3.3.2 nur derjenige Teil des (nächsten) Uplink-Unterrahmens
durch das Benutzergerät übertragen, der sich neben (next to) dem überlappten Teil
des Uplink-Unterrahmens befindet, ohne nach Merkmal 3.3.3 den überlappten Teil
zu übertragen, wobei der Fachmann im Kontext des Streitpatents den Begriff „next
to“ nicht als räumliche Beziehung sondern als Bezugnahme auf den (zeitlich)
nachfolgenden und damit nächsten Teil versteht (vgl. u. a. Fig. 8 mit Beschreibung).
Auch eine Bezugnahme auf eine (parallele) Übertragung in einem anderen
Subträger, welche die Klägerin in Figur 8 zu erkennen glaubt, lässt sich aus der

                                         - 14 -



Formulierung des Merkmals 3.3.3 („next to“) nicht ableiten, da sich das Streitpatent
allein mit zeitlichen Beziehungen zwischen zeitlich aufeinander folgenden
Unterrahmen bei der Uplink-Übertragung befasst. Aus den Merkmalen 3.3.1 bis
3.3.3 folgt damit, dass nur der Teil dieses Uplink-Unterrahmens übertragen wird,
der sich an den überlappenden Teil anschließt. Dabei enthält nach Merkmal 3.3.4
der gemäß Merkmal 3.3.3 nicht übertragene, überlappte Teil dieses Uplink-Unterrahmens mindestens einen Teil des zyklischen Präfixes des Startsymbols
dieses Uplink-Unterrahmens. Das „Startsymbol“ ist dabei als das erste Symbol des
jeweiligen Uplink-Unterrahmens zu verstehen. Dieser Fall ist schematisch in Figur 8
des Streitpatents aus Sicht der Empfangsseite dargestellt:




                                         [Fig. 8]


Die Ausführungen zu Anspruch 1 gelten in gleicher Weise für die funktionalen
Merkmale des Vorrichtungsanspruchs 8.



                                           II.


1.     Zur Frage der unzulässigen Erweiterung
Der Gegenstand des Streitpatents geht nicht über den Inhalt der Anmeldung in ihrer
ursprünglich eingereichten Fassung hinaus (Art. II § 6 Abs. 1 S. 1 Nr. 3 IntPatÜG
i. V. m. Art. 138 Abs. 1 lit. c) EPÜ).


Denn eine unzulässige Erweiterung der ursprünglichen Offenbarung ist nur dann
gegeben,     wenn     eine    Änderung     gegenüber   dem    vorliegt,   was   der
Durchschnittsfachmann der Gesamtheit der ursprünglichen Anmeldeunterlagen als

                                       - 15 -



offenbart entnimmt (vgl. BGH GRUR 1990, 432 – Spleißkammer; GRUR 1992, 157
– Frachtcontainer; GRUR 2005, 1023 – Einkaufswagen II; Schulte, PatG, 11. Aufl.,
§ 21, Rn. 54).


1.1   Merkmalsgruppe 3.1 des Patentanspruchs 1
In den ursprünglich eingereichten Anmeldeunterlagen (Anlage NK 2) werden nach
Auffassung der Klägerin die Ausdrücke „an advance of a transmission timing“
(Merkmal 3.1.1) und „relative to a current transmission timing“ (Merkmal 3.1.2) nicht
verwendet. Auch Seite 3, Zeilen 3 bis 7 sowie Seite 8, Zeile 30 bis Seite 9, Zeile 5
der Anmeldung offenbarten jeweils nicht, dass der neue Übertragungszeitpunkt
gegenüber dem alten Übertragungszeitpunkt vorverlegt werde.


Dieser Auffassung folgt der Senat nicht.


Die Ursprungsanmeldung führt die Zusammenhänge zwischen Unterrahmen
(subframe), Symbolen (symbol), zyklischem Präfix (cyclic prefix) und Startzeitpunkt
(subframe start timing) im Zusammenhang mit Figur 2 ein. Diese Definitionen gelten
in gleicher Weise für die weiteren Abbildungen, insbesondere auch für die Figuren
3 und 8, welche auf den gleichen Datenstrukturen und Zeitbeziehungen zwischen
den Datenelementen basieren. Beide von der Klägerin angeführten Formulierungen
ergeben sich daher für den Fachmann aus Figur 8 in Verbindung mit den zu Figur
2 beschriebenen Zusammenhängen zwischen Unterrahmen, Symbolen, zyklischem
Präfix und Startzeitpunkt sowie der Problembeschreibung auf Seite 3, Zeilen 3 bis
7 und Seite 8, Zeile 30 bis Seite 9, Zeile 5 der ursprünglichen Anmeldung. Diesen
Textstellen   ist   zu   entnehmen,    dass     die   betrachtete   Anpassung    des
Übertragungszeitpunkts des Unterrahmens eine Vorverlegung dieses Zeitpunkts ist.
Bei einer Verzögerung des Übertragungszeitpunkts, also bei der Verschiebung auf
einen späteren Zeitpunkt, tritt das im Streitpatent adressierte Problem dagegen
nicht auf. Es gibt auch keinen Hinweis darauf, dass die Darstellung der Überlappung
einschließlich der Markierungen, welche die jeweiligen Startzeitpunkte der
Subframes bezeichnen, in den Figuren 3, 4 und 8 anders zu verstehen ist als in

                                            - 16 -



Figur 2, auch wenn die Startzeitpunkte und deren Anpassungen in diesen
Zeichnungen nicht durchgängig beschriftet sind.


Die beschriebene Problemstellung spricht zwar allgemein von Paketen (packet
transmission timing) (vgl. Seite 3, Zeilen 3 bis 7) und nicht von Unterrahmen
(subframes). Der Zusammenhang zwischen einer „unit of packet transmission
times“ und einer „unit of subframes“ ergibt sich jedoch aus Seite 8, Zeilen 11 bis 17,
der Anmeldung. Zudem entnimmt der Fachmann unter anderem dem Beispiel nach
Figur 8 in Verbindung mit Figur 2, dass die Datenpakete als Unterrahmen
(subframes) gegliedert sein können. Für den Fall der Überlappung nimmt die
zugehörige Beschreibung zu Figur 8 jeweils Bezug auf das nächste bzw. das
vorhergehende OFDM Symbol (OFDM symbol), das wiederum einleitend in Figur 2
als Teil der Unterrahmen (subframe) dargestellt ist und ein zyklisches Präfix (cyclic
prefix / CP) umfasst:




                        [Fig. 2; farbliche Hervorhebung durch den Senat]


Ergänzend dazu stellen auch die ursprünglich eingereichten Patentansprüche auf
„Unterrahmen“ (subframes) ab und sind ebenfalls im Zusammenhang mit der
Darstellung in Figur 8 in Verbindung mit der Erläuterung der einzelnen
Darstellungselemente in Figur 2 zu verstehen.


Es trifft zwar zu, dass zu den Figuren 5 bis 8 ein Vorverlegen (an advance of a
transmission timing) gemäß Merkmal 3.1.1 nicht explizit als eine Anpassung des
Übertragungszeitpunkts (adjustment of the transmission timing) bezeichnet wird,
sondern nur in Figur 2 dargestellt und nur zu Figur 3 im Kontext einer

                                       - 17 -



kontinuierlichen Übertragung explizit beschrieben ist (vgl. die ursprüngliche
Beschreibung, Seite 8, Zeile 30 bis Seite 9, Zeile 5). Jedoch ist aus dem
Gesamtzusammenhang ersichtlich, dass es sich bei der jeweils betrachteten
Anpassung (adjustment) des Übertragungszeitpunkts um ein Vorverlegen
(advance) im Sinne der oben genannten Problemstellung nach Seite 3, Zeilen 10
bis 17, handeln muss, da es sonst zu keiner Überlappung kommen kann. Im Übrigen
bezeichnen die ursprünglichen Ansprüche 9 und 10 das Vorverlegen des
Übertragungszeitpunktes als Anpassen des Übertragungszeitpunktes.


Ein solches Vorverlegen des Startzeitpunkts (if packet transmission timing is
advanced…) steht zudem zwangsläufig in Bezug zu einem zuvor geltenden
Startzeitpunkt für die Übertragung (current transmission timing), womit die Angabe
des neuen, vorverlegten Startzeitpunkts relativ zu dem, zum Zeitpunkt des
Anpassungsbefehls geltenden, aktuellen Startzeitpunkt erfolgt (relative to a current
transmission timing), wie dies bspw. durch den Pfeil in Figur 2 der
Anmeldeunterlagen verdeutlicht ist.


1.2   Merkmal 3.2 des Patentanspruchs 1
Der Begriff eines „vorherigen Uplink-Unterrahmens“ (previous uplink subframe)
findet sich nach Auffassung der Klägerin an keiner Stelle der ursprünglichen
Unterlagen.   Auch   finde   sich   darin   kein   Hinweis   auf   einen   „aktuellen
Übertragungszeitpunkt“ (current transmission timing).


Es trifft zwar zu, dass sich die genannten Formulierungen nicht wörtlich in der
Ursprungsanmeldung finden, wobei in den ursprünglichen Ansprüchen 1, 2 und 8
zumindest von einem „vorherigen Unterrahmen“ (previous subframe) die Rede ist,
und dass die Beschreibung zu Figur 8 (nur) auf das vorausgehende und das
nächste Symbol Bezug nimmt. Dies ist jedoch wiederum im Zusammenhang mit der
einleitenden Darstellung des Zusammenhangs zwischen Unterrahmen und
Symbolen in Figur 2 sowie der dortigen Bezugnahme des Anpassungsbefehls auf
den Übertragungsbeginn des Unterrahmens zu sehen. Der Figur 2 ist insbesondere

                                      - 18 -



der Zusammenhang zwischen Symbol (symbol) und Unterrahmen (subframe) zu
entnehmen. Aus Seite 8, Zeilen 11 bis 17, ergibt sich weiter der Zusammenhang
zwischen einer „unit of packet transmission times“ und einer „unit of subframes“.
Damit entnimmt der Fachmann der Figur 8 in Verbindung mit der Figur 2 und der
jeweils   zugehörigen   Beschreibung       zweifelsfrei,    dass    zwischen   einem
Übertragungszeitpunkt   vor   und   nach       dem   Befehl   zur   Anpassung   des
Übertragungszeitpunkts unterschieden wird und, dass vor und nach diesem Befehl
der jeweils geltende Übertragungszeitpunkt auf den zur Übertragung anstehenden
Unterrahmen angewandt wird, wobei aufgrund                 der Beziehung zwischen
Unterrahmen und Symbolen mit dem ersten bzw. letzten Symbol des jeweiligen
Unterrahmens    zwangsläufig auch      der entsprechende folgende          bzw. der
vorangehende Unterrahmen betroffen ist.


Der „aktuelle“ Übertragungszeitpunkt (Merkmal 3.2: …current transmission timing)
ist dabei als sprachliche Unterscheidung zu dem auf einen Anpassungsbefehl
folgenden verschobenen Übertragungszeitpunkt zu verstehen, wie er sich aus den
Figuren 2, 5 und 6 ergibt. Mit dem Begriff wird auf die Merkmalsgruppe 3.1 Bezug
genommen, der zu entnehmen ist, dass es sich dabei um den Zeitpunkt handelt,
relativ zu dem die Vorverlegung durch den Zeitanpassungsbefehl gegenüber der
Beibehaltung der bestehenden Zeitbedingungen erfolgt (Merkmal 3.1.2: relative to
a current transmission timing). Ebenso ist der „vorherige“ Uplink-Unterrahmen, für
den der aktuelle Startzeitpunkt gilt und relativ zu dem die Anpassung erfolgt
(Merkmal 3.2: a previous uplink subframe to which the current transmission timing
is applied), zweifelsfrei als Abgrenzung zu dem zur Übertragung anstehenden
Unterrahmen zu verstehen, da der Befehl nach Merkmal 3.1 und 3.1.1 nicht
rückwirkend erfolgen kann (Merkmale 3.1.1: …indicating an advance of a
transmission timing of the uplink subframe). Dieser zur Übertragung anstehende
Unterrahmen wird in Anspruch 1 in Abgrenzung zum „vorherigen Uplink-Unterrahmen“ (previous uplink subframe) durchgängig (nur) als der „Uplink-Unterrahmen“ bezeichnet.

                                         - 19 -



1.3   Merkmalsgruppe 3.3 des Patentanspruchs 1
In den ursprünglichen Unterlagen ist nach Auffassung der Klägerin keine Rede von
einem Teil des Uplink-Unterrahmens, der sich „neben“ dem überlappten Teil des
Uplink-Unterrahmens befinde (a part of the uplink subframe that is next to the
overlapped part of the uplink subframe).


Zwar findet sich diese Formulierung nicht wörtlich in der Ursprungsanmeldung. Wie
bereits im Rahmen der Auslegung dargelegt, ist aber offensichtlich, dass im Kontext
des Streitpatents bzw. der ursprünglichen Unterlagen „next to“ nicht als räumliche
Beziehung verstanden werden kann, da sich das Streitpatent ebenso wie die
ursprünglichen Unterlagen allein mit zeitlichen Beziehungen zwischen aufeinander
folgenden Unterrahmen bei der Uplink-Übertragung befassen. Dabei wird in Figur 8
der ursprünglichen Unterlagen deutlich, dass anhand des Bereichs der
Überlappung (collision part) des betrachteten (aktuellen) Unterrahmens (uplink
subframe) und des vorausgehenden Unterrahmens (previous uplink subframe) für
den   aktuellen   Unterrahmen      zwischen       zwei   aufeinanderfolgenden   Teilen
unterschieden wird, von dem der erste, hervorgehobene Teil als nicht übertragen
(not transmitted) gekennzeichnet ist.




                     [ursprüngliche Unterlagen, Anlage NK02, Fig. 8]


Der Fachmann entnimmt daher der Figur 8 der ursprünglichen Unterlagen einen zu
übertragenden „nächsten“ Teil des Unterrahmens, der auf den überlappenden, nicht
übertragenen Teil dieses Unterrahmens folgt. Dies ergibt sich auch implizit aus der
Aussage des ursprünglich eingereichten Patentanspruchs 1, nach dem der an die
Zeitanpassung angepasste (nächste) Unterrahmen den mit dem vorausgehenden

                                       - 20 -



Unterrahmen überlappenden Teil nicht umfasst, also dieser überlappende Teil nicht
übertragen wird.


1.4    Patentanspruch 8
Aufgrund der funktionalen Merkmale des Vorrichtungsanspruchs 8, die den
Verfahrensmerkmalen des Anspruchs 1 entsprechen, gelten die Ausführungen zu
Anspruch 1 für Anspruch 8 in gleicher Weise.


1.5    Abhängige Patentansprüche
In den ursprünglichen Unterlagen findet sich nach Auffassung der Klägerin keine
Offenbarung,    wonach    der   übertragene     vorherige     Uplink-Unterrahmen     ein
vollständiger   Unterrahmen     (complete   subframe)       im    Sinne   der   erteilten
Patentansprüche 2 und 9 ist. Auch fehle in den ursprünglichen Unterlagen jeglicher
Hinweis auf eine vorbestimmte Schrittgröße (predetermined step size) im Sinne der
Patentansprüche 3 und 10.


Auch dieser Auffassung folgt der Senat nicht.


Eine   vollständige   Übertragung     des     zuletzt   vor      der   Anpassung    des
Übertragungszeitpunkts übertragenen Unterrahmens (complete subframe) ist
nämlich den ursprünglichen Unterlagen in Figur 8 in Verbindung mit Figur 2 zu
entnehmen (vgl. die Darstellung der Symbole im Bereich zwischen den
Markierungen des jeweiligen Übertragungszeitpunkts in Figur 8, der nach Figur 2
einen Unterrahmen darstellt). Dass die Möglichkeit verworfen wird, diesen
(vorherigen) Unterrahmen teilweise nicht zu übertragen, ist zu Figur 4 beschrieben
(vgl. ursprüngliche Beschreibung, Seite 9, Zeilen 12 bis 24). Es trifft zwar zu, dass
sich die Beschreibung zu den Figuren 4 und 8 jeweils nur auf das erste bzw. letzte
Symbol zweier Pakete bezieht und den Unterrahmen nicht explizit erwähnt. Jedoch
stellt Figur 8 die Symbole vor der Zeitanpassung, im Unterschied zum ersten
Symbol nach der Zeitanpassung, als vollständige Symbole dar. Die zwischen einem

                                          - 21 -



ersten und einem darauffolgenden Übertragungszeitpunkt liegenden Symbole
bilden entsprechend der Beschreibung zu Figur 2 wiederum einen Unterrahmen.


Eine vorbestimmte Schrittgröße (predetermined step size) folgt aus Seite 8, Zeilen
3 bis 17 der ursprünglichen Beschreibung (the base station can advance … the
transmission timing of each mobile station by one or more predetermined steps …
advancing … the subframe by one or more steps on a time axis). Im Übrigen werden
in    Mobilfunksystemen           selbstverständlich   nur         vorbestimmte,    den
Kommunikationspartnern        bekannte,     Schrittgrößen    zur     Verschiebung   des
Startzeitpunkts einer Übertragung verwendet (NK10, S. 7, Kap. 4.2.4 i. V. m.
NK10a, S. 9, Kap. 4, Satz 1).


1.6    Figuren 6 und 8
Entgegen der Auffassung der Klägerin besteht schließlich kein Widerspruch
zwischen Figur 8 und Figur 6 der ursprünglichen Unterlagen, so dass diese Figuren
(in Bezug auf die Merkmalsgruppe 3.1) eine eindeutige Ursprungsoffenbarung der
Anspruchsmerkmale nicht in Frage stellen. Denn die Beschreibung zu Figur 6 trifft
keine Aussage dazu, welche Daten im Falle der Kollision bzw. Überlappung von
Unterrahmen übertragen oder weggelassen werden, sondern beschreibt allgemein
das notwendige Erzeugen und Einfügen des zu übertragenden Präfixes – unter
Berücksichtigung des Anpassungsbefehls – für ein nächstes Symbol. Die
Beschreibung zu Figur 8 erläutert dann, welcher Teil von welchem Unterrahmen
(subframe) nicht übertragen wird, wobei auf zwei überlappende (Daten-)Pakete
Bezug genommen wird. Zwar bezieht sich die Beschreibung der Figur 6 nur auf
Symbole (a next symbol), nicht auf Unterrahmen. Aus der Beschreibung dieser
Figur im Zusammenhang mit Seite 8, Zeilen 11 bis 17 der Anmeldung (und den
urspr. Ansprüchen 1 und 2) ergibt sich aber, dass sich ein „start timing adjustment“-
Befehl auf die Übertragung eines nächsten Unterrahmens (subframe) bezieht und
dieser wiederum aus Symbolen aufgebaut ist (vgl. Figuren 2, 3, 8 i. V. m. Seite 3,
Zeile 25 bis Seite 4, Zeile 3).

                                        - 22 -



Figur 8 zeigt (wie auch Figur 4), entgegen der Auffassung der Klägerin, keine
Datenpakete auf unterschiedlichen Subträgern und stellt damit eine eindeutige
Ursprungsoffenbarung der Anspruchsmerkmale ebenfalls nicht in Frage. So ist in
keiner der Darstellungen des Streitpatents eine vertikale Achse dargestellt oder in
der zugehörigen Beschreibung erwähnt. Vielmehr wird im Gesamtkontext des
Streitpatents ausschließlich die zeitliche Abfolge der Unterrahmen thematisiert. Die
versetzte Darstellung von vorhergehendem und aktuellem Unterrahmen in Figur 8
ist daher dem Ziel geschuldet, die Zugehörigkeit des jeweils zu übertragenen bzw.
nicht zu übertragenen Teils des vorhergehenden und aktuellen Unterrahmens für
den Überlappungsbereich der beiden Unterrahmen graphisch nachvollziehbar
darzustellen. Daher erkennt der Fachmann zweifelsfrei, in welchem Verhältnis die
Datenpakete     zueinander stehen.     Dafür, dass     Figur 8    Datenpakete    auf
unterschiedlichen Subträgern zeigt, findet sich dagegen im Streitpatent kein
Hinweis.



2.     Zur Frage der Ausführbarkeit
Der Gegenstand des Streitpatents ist so deutlich und vollständig offenbart, dass ein
Fachmann ihn ausführen kann (Art. II § 6 Abs. 1 S. 1 Nr. 2 IntPatÜG i. V. m. Art. 138
Abs. 1 lit. b) EPÜ).


2.1    Merkmalsgruppe 3.1
Die Klägerin vertritt die Auffassung, dass sich dem Fachmann nicht erschließt, wie
ein Fortschritt eines Übertragungszeitpunkts des Uplink-Unterrahmens in Bezug auf
einen aktuellen Übertragungszeitpunkt angezeigt werden kann.


Dieser Auffassung ist nicht zuzustimmen.


Das Merkmal 3.1 nimmt Bezug auf den Anpassungsbefehl zur Anpassung des
Übertragungszeitpunkts. Die Kenntnis der Zeitbeziehungen und Datenstrukturen
(Unterrahmen,     Symbole,   Präfix)   ist   dem   Fachwissen    zuzurechnen,    wie
beispielsweise der als Anlagen NK10 und NK10a vorgelegte LTE-Standard

                                           - 23 -



verdeutlicht (vgl. NK10, S. 7, Kap. 4.2.4 i. V. m. NK10a, S. 9, Kap. 4 und 4.1,
Fig. 4.1-1). Wie die zeitliche Anpassung (adjustment) angegeben wird, ist in den
Abschnitten 0033 und 0034 des Streitpatents beschrieben. Bei dem Begriff
„Fortschritt“ in der deutschen Übersetzung des Merkmals handelt es sich im Kontext
des Streitpatents um eine unpassende Übersetzung des Begriffs „advance“ (vgl.
Merkmal 3.1.1 in der Verfahrenssprache Englisch: „...for indicating an advance of a
transmission timing of the uplink subframe“), da das Streitpatent nur eine
Verschiebung des Startzeitpunkts in Richtung eines früheren Zeitpunkts näher
betrachtet, wie sie anhand des Pfeils in Figur 2 oder anhand der Überlappung in
den Figuren 3, 4 und 8 verdeutlicht ist.


2.2   Merkmalsgruppe 3.3
Die Klägerin vertritt die Auffassung, dass im Streitpatent nicht beschrieben werde,
wie, wann und durch welches Element eine etwaige Überlappung des vorherigen
Uplink-Unterrahmens mit dem Uplink-Unterrahmen aufgrund des Fortschritts des
Übertragungszeitpunkts des Uplink-Unterrahmens zu bestimmen sei. Dem
Fachmann fehlten ferner Angaben darüber, wie ein Übertragen eines Teils des
Uplink-Unterrahmens durch das UE, der sich zeitlich neben dem überlappten Teil
des Uplink-Unterrahmens befinde, ohne den überlappten Teil zu übertragen,
geschehen solle.


Auch dieser Ansicht folgt der Senat nicht.


Das Streitpatent beschreibt zwar keine konkreten Verfahrensschritte, um eine
etwaige Überlappung des vorherigen Uplink-Unterrahmens mit dem Uplink-Unterrahmen zu bestimmen. Die Überlappung ergibt sich für den Fachmann jedoch
eindeutig daraus, dass von einer kontinuierlichen Übertragung ausgegangen wird
und, neben der zeitlichen Länge von Unterrahmen, Symbol und Präfix, der jeweilige
Startzeitpunkt zur Übertragung von Unterrahmen und die Vorverlegung dieses
Zeitpunkts dem Benutzergerät bekannt sind. Die Kenntnis der grundlegenden

                                           - 24 -



Zeitbeziehungen ist dabei dem Fachwissen zuzurechnen (NK10, S. 7, Abschnitt
4.2.4 i. V. m. NK10a, S. 9, Fig. 4.1-1).


Das Übertragen des Teils des Uplink-Unterrahmens durch das Benutzergerät, der
sich „neben“ dem überlappten Teil des Uplink-Unterrahmens befindet, ohne den
überlappten Teil zu übertragen, erfolgt anspruchsgemäß dadurch, dass der
überlappende Teil, der in der Regel einen Teil des zyklischen Präfixes bildet,
weggelassen wird (vgl. Merkmal 3.3.4). Hierzu offenbart die Beschreibung des
Streitpatents zu Figur 5 in Absatz 0046 auch das Generieren eines entsprechend
angepassten zyklischen Präfixes.


2.3    Figuren 6 und 8
Figur 8 zeigt entgegen dem Verständnis der Klägerin keine verschiedenen
Subträger und zwischen den Figuren 6 und 8 besteht kein Widerspruch. Hierzu wird
auf die vorstehenden Ausführungen zu den von der Klägerin vorgebrachten
Argumenten zu den Figuren 6 und 8 im Hinblick auf eine fehlende (eindeutige)
Ursprungsoffenbarung verwiesen. Die genannten Zeichnungen stellen die
Ausführbarkeit der Lehre des Streitpatents nicht in Frage.



3.     Zur Frage der Patentfähigkeit
Die jeweiligen Gegenstände der angegriffenen unabhängigen Patentansprüche 1
und 8 sind neu gegenüber dem im Verfahren befindlichen Stand der Technik und
dem Fachmann durch den im Verfahren befindlichen Stand der Technik auch nicht
nahegelegt (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a), Art. 54,
56 EPÜ).


3.1    Die Gegenstände der Ansprüche 1 und 8 sind aus den Druckschriften NK10
(3GPP TS 36.213 V8.1.0) und NK10a (3GPP TS 36.211 V8.1.0) weder bekannt
noch ergeben sie sich für den Fachmann in naheliegender Weise aus diesen.

                                        - 25 -



Bei den Druckschriften NK10 und NK10a handelt es sich jeweils um eine technische
Spezifikation des 3GPP (3rd Generation Partnership Project) zu E-UTRA (Evolved
Universal Terrestrial Radio Access), die die Luftschnittstelle des LTE-Standards
bezeichnet. Die Dokumente NK10 und NK10a können als ein gemeinsames
Dokument angesehen werden, da beide jeweils Teile der physikalischen Schicht
von E-UTRA spezifizieren und darüber hinaus jeweils aufeinander Bezug nehmen
(vgl. NK10, Seite 6, Kap. 2, Punkt [3]; NK10a, Seite 7, Kap. 2, Punkt [4]).


Die Druckschriften NK10/NK10a zeigen die folgenden Merkmale in den Worten des
Patentanspruchs 1:
Verfahren zum Übertragen eines Uplink-Unterrahmens, der eine Mehrzahl von
Symbolen enthält (Merkmale 1, 1.1)
      Figur 4.1-1 der NK10a zeigt eine mögliche Rahmenstruktur (Frame structure
      type 1), bestehend aus 10 Unterrahmen (subframes) zur Verwendung bei der
      Uplink- und Downlink-Übertragung, wobei jeder Unterrahmen aus zwei
      Zeitschlitzen (slots) besteht (vgl. NK10a, Seite 9, Kap. 4.1 Frame structure
      type 1)




                                      [NK10a, Fig. 4.1-1]


      Die Zeitschlitze im Uplink sind weiter in „Symbole“ (symbols) unterteilt, die
      jeweils auf einer Vielzahl von Unterträgern (subcarriers) übertragen werden
      (The number of SC-FDMA symbols in a slot depends on the cyclic prefix
      length configured by higher layers…; vgl. NK10a, Seite 10, letzter Satz und
      Seite 11, Fig. 5.2.1-1).

                                       - 26 -



in einem zellularen Mobilkommunikationssystem durch ein Benutzergerät (User
Equipment, UE) (Merkmale 1.2, 1.3),
      Druckschriften NK10/NK10a betreffen mit E-UTRA (vgl. NK10 und NK10a,
      jeweils Titel und Kap. 1 Scope) die Luftschnittstelle von LTE, somit ein
      zellulares Mobilkommunikationssystem. Die Verwendung der zu Merkmal 1
      gezeigten Datenstruktur im Uplink-Fall bedeutet eine Übertragung durch ein
      Benutzergerät (vgl. NK10a, Seite 9, Kap. 4.1).


wobei jedes Symbol ein zyklisches Präfix und einen Datenteil enthält (Merkmal 2),
      Die Zeitschlitze sind in „Symbole“ (symbols) unterteilt, die einen zyklischen
      Präfix und (implizit) einen Datenteil für die Nutzdaten aufweisen (The number
      of SC-FDMA symbols in a slot depends on the cyclic prefix length configured
      by higher layers…; vgl. NK10a, Seite 10, letzter Satz und Seite 11, Fig. 5.2.1-
      1).


Das Verfahren umfasst dabei das Empfangen eines Zeitanpassungsbefehls (timing
adjustment command) durch das Benutzergerät (UE) zum Anzeigen einer
Vorverlegung    (an      advance)   eines   Übertragungszeitpunkts     des   Uplink-Unterrahmens in Bezug auf einen aktuellen Übertragungszeitpunkt (Merkmale 3,
3.1, 3.1.1 und 3.1.2);
      Upon reception of a timing advance command, the UE shall adjust its uplink
      transmission timing. The timing advance command is expressed in multiples
      of 16 Ts and is relative to the current uplink timing; vgl. NK10, Seite 7, Kap.
      4.2.4 Transmission timing adjustments.


Übertragen eines vorherigen Uplink-Unterrahmens durch das Benutzergerät (UE),
auf den der aktuelle Übertragungszeitpunkt angewendet wird (Merkmal 3.2);
      Dies folgt implizit daraus, dass der Zeitanpassungsbefehl (timing adjustment
      command) nicht auf den aktuellen Unterrahmen n, sondern erst auf einen der
      folgenden Unterrahmen (n+x) anzuwenden ist, womit auf den aktuellen
      Unterrahmen der aktuelle Übertragungszeitpunkt angewendet wird (For a

                                          - 27 -



         timing advance command received on subframe n, then corresponding
         adjustment occurs at the beginning of subframe n+x; vgl. NK10, Seite 7, Kap.
         4.2.4 Transmission timing adjustments, letzter Satz).


Den Druckschriften NK10/NK10a sind jedoch keine Angaben zu möglichen
negativen Auswirkungen der Anpassung des Übertragungszeitpunkts der Uplink-Unterrahmen zu entnehmen. Insbesondere sind weder dadurch entstehende
Probleme angesprochen noch gibt es einen Hinweis auf eine konkrete Lösung
gemäß der Merkmalsgruppe 3.3 des Anspruchs 1 des Streitpatents. Dies gilt in
gleicher Weise für die korrespondierenden Merkmale des Patentanspruchs 8.


Zwar ist nach Überzeugung des Senats ausgehend von der in den Druckschriften
NK10/NK10a dargestellten Datenstruktur und einer kontinuierlichen Übertragung
von Unterrahmen (vgl. NK10a, Figur 4.1-1) davon auszugehen, dass der Fachmann
angesichts der beschriebenen Zeitanpassung erkennt, dass dies zu einer
Überlappung zwischen kontinuierlich aufeinander folgenden Unterrahmen führt. In
dieser     Überlappung    erkennt   der     Fachmann,   der      mit   einer   möglichen
Intersymbolinterferenz, bspw. aufgrund der Ausbreitungsverzögerung (delay
spread) und der Funktion eines Präfixes der jeweiligen Symbole als Schutzintervall
vertraut ist, nicht zwangsläufig ein zusätzliches Problem. Ein solches Problem ist in
den Standard-Dokumenten NK10 und NK10a nicht angesprochen. Daher fehlt den
Dokumenten auch jeglicher Hinweis dazu, wie ein solches, aus der Zeitanpassung
zusätzlich resultierendes Problem zu behandeln wäre.


a)       Aufgrund von Kanalverzögerungen durch Multipfadausbreitung und der
daraus resultierenden Variation der Übertragungsdauer (delay spread) ist bei der
kontinuierlichen     Übertragung     über     eine   Funkstrecke       regelmäßig    mit
Überschneidungen bzw. Überlappungen aufeinanderfolgender Datenpakete zu
rechnen. Eine gebräuchliche Maßnahme, Störungen durch diese Effekte zu
vermeiden, ist die Verwendung des zyklischen Präfixes als Schutzintervall (guard
interval) zwischen benachbarten Symbolen. Hiervon geht auch das Streitpatent aus

                                       - 28 -



(vgl. Abs. 0012 i. V. m. 0004). Der mit der Datenübertragung in Mobilfunksystem
befasste Fachmann ist aufgrund seines Fachwissens mit den genannten
Verzögerungseffekten und der Verwendung eines zyklischen Präfixes vertraut.
Aufgrund seines Fachwissens erkennt er daher auch in den Druckschriften
NK10/NK10a, dass es bei einer kontinuierlichen Übertragung durch die
Vorverlegung   des   Startzeitpunkts   eines    Subrahmens    ebenfalls   zu   einer
Überlappung kommen kann.


Das Streitpatent geht jedoch über die bekannte Verwendung des zyklischen
Präfixes hinaus, und bildet diese durch die Merkmalsgruppe 3.3 weiter bzw. ergänzt
sie, um möglichen Störungen aus Kanalbedingungen (delay spread) und der
Vorverlegung eines Übertragungszeitpunkts zu begegnen. Die Erkenntnis,
ergänzende Maßnahmen nach Merkmalsgruppe 3.3 vorzusehen, die über die
Verwendung eines Schutzintervalls durch das zyklische Präfix hinausgehen, ist
daher bereits als Teil der Erfindung anzusehen, die sich dem Fachmann nicht
bereits aufgrund der erkannten möglichen Überlappung von Unterrahmen bei deren
kontinuierlichen Übertragung in naheliegender Weise ergibt.


b)    Die Textstelle „For a timing advance command received on subframe n, then
corresponding adjustment occurs at the beginning of subframe n+x“ (vgl. NK10,
Seite 7, Abschnitt 4.2.4) gibt – entgegen dem Verständnis der Klägerin – nur den
Zeitpunkt an, für den die dem Befehl entsprechende Änderung des Timings
(corresponding adjustment) erfolgt – nämlich mit Beginn des Unterrahmens n+x (at
the beginning of subframe n+x). Dazu, wie dieser Übergang in Bezug auf die
Unterrahmen n+x und den vorausgehenden Unterrahmen n+xumgesetzt wird,
findet sich in der NK10/10a kein Hinweis. Insbesondere ist dieser Textstelle keine
Aussage dazu zu entnehmen, in welchem der Unterrahmen Maßnahmen zur
Vermeidung einer Störung durch ein Überlappen beim Vorverlegen des
Startzeitpunkts des folgenden Rahmens zu treffen sind. Da die Druckschriften
NK10/NK10a keine möglichen, aus der Zeitanpassung resultierenden Probleme
ansprechen, ergibt sich für den Fachmann aus der Angabe zum Zeitpunkt der

                                        - 29 -



Zeitanpassung auch keine Veranlassung, sich mit Maßnahmen zur Lösung einer
solchen Problemstellung zu befassen. Da in den Druckschriften NK10/NK10a
bereits das Überlappen der Unterrahmen bei Vorverlegung des Startzeitpunkts im
Falle einer kontinuierlichen Übertragung nicht angesprochen ist, führen die
Druckschriften NK10/NK10a den Fachmann nicht „automatisch“ zur Lösung gemäß
Merkmalsgruppe 3.3 des Streitpatents.


c)    Selbst wenn man – abweichend von den vorstehenden Überlegungen –
davon ausginge, dass der Fachmann nicht nur ein mögliches Überlappen von
Unterrahmen bei einer kontinuierlichen Übertragung beim Vorverlegen des
Startzeitpunkts erkennt, sondern auch, dass dies in Verbindung mit einer
Verschlechterung      der   Empfangsqualität     durch    Effekte   der   Mehrfachpfad-Technologie (delay spread, timing misalignment) zu einem Problem führt, das allein
durch das Vorsehen eines zyklischen Präfix möglicherweise nicht verhindert wird,
würde er aufgrund seines Fachwissens nicht in naheliegender Weise zur Lösung
gemäß Streitpatent gelangen.


So stellt sich für den Fachmann bereits die Frage, ob das erkannte Problem für den
Uplink-Fall besser in der Basisstation oder dem Benutzergerät gelöst wird. Denn die
Basisstation weist die Ressourcen für die Uplink-Übertragung zu und veranlasst
auch den Anpassungsbefehl für den Übertragungszeitpunkt. Störende Einflüsse
des Übertragungswegs (delay spread) werden dagegen durch das zyklische Präfix
adressiert, das jeweils durch das Benutzergerät den zu übertragenden Daten
hinzugefügt wird. Somit gibt es aus dem Fachwissen zumindest keinen eindeutigen
Hinweis, ob das Problem bevorzugt auf Seiten des Benutzergeräts oder der
Basisstation gelöst werden kann.


Auch die Überlegungen der Klägerin, dass sich dem Fachmann nur drei
gleichwertige Lösungen aufgrund seines Fachwissens aufdrängen würden – d. h.
vollständiges    Übertragen    des   anstehenden         Unterrahmens,     vollständiges
Übertragen      des   vorausgehenden    Unterrahmens        oder    Übertragen   beider

                                       - 30 -



Unterrahmen – greifen nicht. Dass das Streitpatent diese Möglichkeiten betrachtet,
ist weder als ein Hinweis auf gleichwertige Lösungen noch als ein Hinweis auf das
Fehlen von weiteren Alternativen zu verstehen; vielmehr stellt die Einschätzung der
Klägerin eine rückschauende Betrachtung des beanspruchten Gegenstands dar.
Darüber hinaus sind – selbst ohne Betrachtung einer basisstationsseitigen Lösung
– auf Seiten des Benutzergeräts weitere Lösungen denkbar, von einem Aufschieben
der    Zeitanpassung   bis   zur   Verringerung   der   Bandbreite   (bspw.   durch
Übertragungspausen, Freihalten einzelner Symbole, Wiederholen von Symbolen
oder Unterrahmen), wie auch durch den weiteren vorgelegten Stand der Technik
(Dokumente NK9, NK11, NK12) offensichtlich ist.


Der Gegenstand des Patentanspruchs 1 ist daher weder durch die Druckschriften
NK10/NK10a vorweggenommen noch ergibt er sich für den Fachmann ausgehend
von diesen Druckschriften und unter Berücksichtigung seines Fachwissens in
naheliegender Weise. Dies gilt in gleicher Weise für den Gegenstand des
nebengeordneten Anspruchs 8.


3.2.   Der Gegenstand des Patentanspruchs 1 ist dem Fachmann auch nicht durch
die Druckschriften NK10/NK10a unter Berücksichtigung der Druckschrift NK9
(R1-051096), nahegelegt. Dies gilt in gleicher Weise für den nebengeordneten
Anspruch 8.


Die Klägerin verweist im Zusammenhang mit den Dokumenten NK10 und NK10a
auf Druckschrift NK9 als Beleg des Fachwissens. Dabei handelt es sich um einen
Diskussionsbeitrag für das Arbeitsgruppentreffen der TSG RAN WG1 (Technical
Specification Group Radio Access Network Working Group 1) des 3GPP (3rd
Generation Partnership Project) in San Diego vom 10. bis 14. Oktober 2005.


Die Druckschrift NK9 befasst sich mit der Notwendigkeit von Übertragungspausen
(idle period), um eine gegenseitige Störung von aufeinanderfolgenden Uplink- und
Downlink-Unterrahmen zu vermeiden, wenn in einer Halb-Duplex-Kommunikation

                                      - 31 -



unter Verwendung eines zyklischen Präfixes eine Interferenz bzw. ein Überlappen
von Unterrahmen erfolgt (vgl. Abschnitt 2). Im Hinblick auf ein mögliches
Überlappen wird darauf verwiesen, dass eine kurze Übertragungspause (idle
period) benötigt werden könnte. Bei einem solchen Überlappen von Unterrahmen
könnten Synchronisierungsprobleme statt mit Übertragungspausen auch mittels
anderer Signaleigenschaften wie dem zyklischen Präfix des SC-FDMA (cyclic prefix
of SC-FDMA) oder des OFDMA Multiplexverfahrens (OFDMA multiple access
techniques) vermieden werden (vgl. NK9, Abschnitt 2.4). Aus diesem zitierten
Absatz folgt – entgegen der Auffassung der Klägerin – allerdings nicht, dass das
Präfix am Anfang jedes Unterrahmens am ehesten „entbehrlich“ sei. Hierfür findet
sich im Dokument NK9 auch an keiner anderen Stelle ein Hinweis. In Verbindung
mit Abschnitt 2.2 entnimmt der Fachmann der NK9 allenfalls, dass bestimmte
Inhalte des ersten (oder letzten) Unterrahmens, bspw. aufgrund von enthaltenen
Steuerdaten (control information), wichtig sein könnten, was bei der Gestaltung des
Übergangs zwischen den Unterrahmen ggf. zu berücksichtigen sei.


Die Merkmalsgruppe 3.3 des Anspruchs 1 des Streitpatents ist dem Fachmann
ausgehend von den Druckschriften NK10/NK10a in Verbindung mit Druckschrift
NK9 nicht nahegelegt. Denn Druckschrift NK9 nennt beispielgebend (may also…)
drei verschiedene Ansatzpunkte, wie mit der Problematik der Anpassung des
Übertragungszeitpunkts umgegangen werden könnte – neben dem zyklischen
Präfix sind das Übertragungspausen und OFDMA Multiplexverfahren. Damit führt
auch Druckschrift NK9 den Fachmann ohne weitergehende eigene Überlegungen
nicht zu einer Verwendung eines zyklischen Präfixes an Stelle der in NK9
genannten Lösungsmöglichkeiten. Hinzu kommt, dass Druckschrift NK9 trotz
Nennung des zyklischen Präfixes keinen Hinweis darauf gibt, wie mit diesem im
Falle der Überlappung zu verfahren ist. Der Fachmann müsste daher nicht nur das
Problem der Überlappung erkennen und die Teile des Unterrahmens näher
betrachten, sondern zusätzlich erkennen, dass er den Unterrahmen, insbesondere
das Präfix, auch verkürzen kann. Die NK9 gibt ihm jedoch keinen Hinweis darauf,

                                         - 32 -



einen Teil des Präfixes oder ggf. über das Präfix hinaus Teile des überlappenden
Unterrahmens wegzulassen (vgl. Merkmal 3.3.4 i. V. m. 3.3.1).


Daher gelangt der Fachmann auch ausgehend von den Druckschriften NK10/10a in
Zusammenschau mit Druckschrift NK9 nicht in naheliegender Weise zum
Gegenstand des Patentanspruchs 1.


Es kann daher dahinstehen, ob der Inhalt der Druckschrift NK9 als Beleg des
Fachwissens dienen kann.


3.3    Die Gegenstände der Patentansprüche 1 und 8 sind dem Fachmann auch
nicht durch eine Zusammenschau der Druckschriften NK10/NK10a mit der
Druckschrift NK11 (WO 2007/073701 A1) nahegelegt.


Die Druckschrift     NK11 betrifft die Sender/Empfänger-Architektur bei der
Weiterentwicklung eines VDSL (very-high speed digital subscriber line) Systems
(vgl. Titel; Seite 2, Zeilen 13 ff; Seite 6, Zeilen 5 - 9), wobei auch
Drahtloskommunikation angesprochen ist (Seite 7, Zeilen 30, 31: WiMAX).


Die Druckschrift NK11 beschreibt die Verwendung eines zyklischen Präfixes (cyclic
prefix) am Anfang eines übertragenen Rahmens, um Störungen zwischen zwei
aufeinanderfolgenden Rahmen aufgrund der Kanaleigenschaften zu vermeiden
(Due to the communication channel dispersion, the cyclic prefix is added at the
beginning of the transmitter frame so that the previous DMT frame does not
interference [sic!] with the current DMT frame; vgl. Seite 5, Zeilen 3-5). In Ergänzung
dazu ist ein zyklisches Suffix (cyclic suffix) vorgesehen, das dazu dient, zusammen
mit einem Mechanismus zur Zeitanpassung bzw. dem Vorverlegen des
Übertragungszeitpunkts (timing advance mechanism) eine Zeitangleichung
zwischen Sender und Empfänger zu ermöglichen (The cyclic suffix is used together
with a timing advance mechanism to make sure that the transmitters and receivers
are sufficiently aligned in time; vgl. Seite 5, Zeilen 12-14).

                                        - 33 -



Der Fachmann entnimmt damit der Druckschrift NK11, dass das zyklische Suffix
(und nicht das zyklische Präfix) dazu vorgesehen ist, einen Sicherheitsbereich für
den Mechanismus einer Vorverlegung des Übertragungszeitpunkts zu schaffen.
Aus dem darauffolgenden Satz, wonach ein Sicherstellen der Orthogonalität bei
korrekter Verwendung der Zeitanpassung dadurch erfolgt, dass die Länge von
Präfix   und     Suffix    zusammen      größer    ist   als     Zeitdispersion   und
Übertragungsverzögerung des Kommunikationskanals, ergibt sich ebenfalls nicht,
dass das zyklische Präfix zur Fehlervermeidung beim Ausgleichen der
Zeitanpassung dient. Vielmehr wird damit nur darauf verwiesen, dass bei korrektem
Setzen der Zeitanpassung die Orthogonalität erhalten bleibt, wenn die Gesamtlänge
von Präfix und Suffix für eine Verzögerung durch die Kanaleigenschaften
ausreichend ist (If the time-advance is properly set, the orthogonality can always be
maintained as far as the total length of the cyclic prefix and cyclic suffix is longer
than the time-dispersion and propagation delay of the communication channel; vgl.
Seite 5, Zeilen 14-17).


Aus der implizit entnehmbaren Anpassung der Länge des Präfixes (Rest_of_cp) auf
Seite 20, Zeilen 16 bis 24, ist ebenfalls kein Beschneiden des Präfixes aufgrund der
Anpassung des Übertragungszeitpunkts abzuleiten, da ebenso ein Rest des
Suffixes (Rest_of_cs) erwähnt ist und in diesem Beschreibungsabschnitt kein Bezug
zu möglichen Problemen der Zeitanpassung hergestellt wird. Vielmehr ist in diesem
Zusammenhang nur eine (anpassbare) Aufteilung der gemeinsamen Länge von
Suffix und Präfix aufgrund der Kanaleigenschaften beschrieben (vgl. Seite 19,
Zeilen 14-28 i. V. m. Seite 5, Zeilen 14-17), aber keine Reaktion auf eine
Überlappung von Rahmen aufgrund einer Zeitanpassung.


Damit führt die Lehre der Druckschrift NK11 den Fachmann von einem Weglassen
eines    Teils   des      zyklischen   Präfixes   bei    einer   Vorverlegung     des
Übertragungszeitpunkts eines (Unter-)Rahmens weg, da Druckschrift NK11 für die
Anpassung des Übertragungszeitpunkts zwingend ein zusätzliches, zyklisches
Suffix (cyclic suffix) vorsieht (vgl. NK11, Seite 5, Zeilen 12-14), wobei Druckschrift

                                              - 34 -



NK11      keinen    direkten    Zusammenhang             zwischen    einer   Anpassung     des
Übertragungszeitpunkts der betrachteten Rahmen und dem genannten zyklischen
Präfix    (cyclic   Prefix)    herstellt.   Allenfalls    ist   in   Druckschrift   NK11   ein
Zusammenwirken von Suffix und Präfix offenbart (vgl. Seite 19, Zeile 14 bis Seite
20, Zeile 14), um Störungen durch die Kanaleigenschaften in Verbindung mit einer
Vorverlegung des Übertragungszeitpunkts zu vermeiden, was ebenfalls von einer
Lösung mittels Weglassen eines Teils des folgenden Unterrahmens bzw. Präfix
entsprechend dem Streitpatent wegführt.


3.4      Die Gegenstände der Patentansprüche 1 und 8 sind dem Fachmann jeweils
auch nicht durch eine Zusammenschau der Druckschriften NK10/NK10a mit der
Druckschrift NK12 (WO 2007/024558 A1) nahegelegt.


Die Druckschrift NK12 betrifft die Anpassung des Übertragungszeitpunkts in einem
drahtlosen Kommunikationssystem (vgl. Titel und Seite 2, Zeile 24 bis Seite 3,
Zeile 3). Aus der Druckschrift NK12 ist bekannt, dass eine Anpassung des
Übertragungszeitpunkts auf einem Downlink-Kanal (vgl. Anspruch 1; Seite 11,
Zeilen 22 ff) zu einer Überlappung von aufeinanderfolgenden Unterrahmen führt,
wenn der Unterrahmen vor der Zeitanpassung nicht leer ist – also eine
kontinuierliche Übertragung im Sinne des Streitpatents erfolgt (This embodiment
differs principally in that the subframe immediately prior to the timing adjustment is
not empty, and thus overlaps can create a conflict; vgl. Seite 10, letzter Satz und
Figur 5).
Für eine solche Überlappung von Unterrahmen schlägt die Druckschrift NK12 vor,
jeweils den überlappenden Unterrahmen fallen zu lassen und direkt den folgenden
Unterrahmen zu übertragen (…This overlap issue is overcome by the base station
130 discarding the overlapping subframe 506 (HICH for SFNisub1), and instead
transmitting the next subsequent subframe 508 (HICH for SFNisub2) as shown
at 502A; vgl. Seite 11, Zeilen 17-20).

                                       - 35 -



Für das Weglassen nur eines Teils des Unterrahmens, bspw. eines Teils des
zyklischen Präfixes, zur Vermeidung oder Verringerung von Störungen durch das
Vorverlegen   des     Übertragungszeitpunkts         während   einer   kontinuierlichen
Übertragung gibt es in der Druckschrift NK12 keinen Hinweis. Vielmehr führt auch
die Lehre der Druckschrift NK12 von der Lösung nach Merkmalsgruppe 3.3 des
Anspruchs 1 des Streitpatents weg. Denn für eine Überlappung von Unterrahmen
aufgrund einer Zeitanpassung schlägt die Druckschrift NK12 vor, jeweils den
überlappenden Unterrahmen (vollständig) fallen zu lassen und direkt den folgenden
Unterrahmen zu übertragen (…This overlap issue is overcome by the base station
130 discarding the overlapping subframe 506 (HICH for SFNisubl), and instead
transmitting the next subsequent subframe 508 (HICH for SFNisub2) as shown
at 502A; vgl. Seite 11, Zeilen 17-20; Unterstreichung durch den Senat).


Außerdem ist eine Zeitanpassung für Unterrahmen eines Uplink-Kanals und daraus
möglicherweise     resultierende   Probleme     in    der   Druckschrift   NK12   nicht
angesprochen. Vielmehr befasst sich die Druckschrift NK12 nur mit der Downlink-Übertragung (vgl. Anspruch 1; Seite 11, Zeilen 22 ff) und sieht insbesondere keine
Maßnahmen auf Seiten des Benutzergeräts vor. Selbst wenn der Fachmann
Parallelen zwischen den Problemen bei einer kontinuierlichen Übertragung im
Uplink- und Downlink-Fall erkennen sollte, würde er Lösungsmaßnahmen, welche
die Basisstation im Downlink-Fall vornimmt, nicht zwangsläufig auf die Mobilstation
übertragen, da die Basisstation auch für den Uplink-Fall die Kontrolle über die
Ressourcenvergabe und die Zeitanpassung hat, d. h. beides von der Basisstation
und nicht durch das Endgerät festgelegt wird.


3.5   Ein Naheliegen der jeweiligen Gegenstände der Patentansprüche 1 und 8 ist
ausgehend vom weiteren, bereits im Streitpatent genannten Stand der Technik
gemäß den Druckschriften NK7 und NK8 nicht ersichtlich und wurde auch nicht
geltend gemacht.

                                        - 36 -



3.6    Der Gegenstand der Patentansprüche 1 und 8 ist somit durch den im
Verfahren befindlichen Stand der Technik weder bekannt noch nahegelegt. Die
Unteransprüche werden durch die unabhängigen Patentansprüche getragen.



                                         III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 Satz 1
ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und Satz 2 ZPO.



                               Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Grote-Bittner       Altvater            Matter         Meiser           Tischler
