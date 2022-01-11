---
ecli: "ECLI:DE:BGH:2022:110122XZR4.20.0"
court: "Bundesgerichtshof"
spruchkoerper: "Zivilsenat-10"
aktenzeichen: "X ZR 4/20"
decided: "2022-01-11"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&Datum=2022&Sort=1&Seite=1&nr=127293&anz=3168&pos=43&Blank=1.pdf"
corpus_doc_id: "BGH_Zivilsenat-10_NA_2022-01-11_X_ZR_4_20_NA_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0119.md", "germany/bund/acts/patg/0121.md", "germany/bund/acts/zpo/0100.md"]
---

# Bundesgerichtshof, X ZR 4/20 vom 2022-01-11

## Entscheidung

BUNDESGERICHTSHOF
                IM NAMEN DES VOLKES
                            URTEIL
X ZR 4/20                                            Verkündet am:
                                                     11. Januar 2022
                                                     Anderer
                                                     Justizangestellte
                                                     als Urkundsbeamtin
                                                     der Geschäftsstelle
                    in der Patentnichtigkeitssache




ECLI:DE:BGH:2022:110122UXZR4.20.0

                                         -2-



Der X. Zivilsenat des Bundesgerichtshofs hat auf die mündliche Verhandlung
vom 11. Januar 2021 durch den Vorsitzenden Richter Dr. Bacher, die Richter
Hoffmann und Dr. Deichfuß, die Richterin Dr. Kober-Dehm und den Richter
Dr. Crummenerl

für Recht erkannt:

      Auf die Berufungen der Parteien wird das Urteil des 5. Senats
      (Nichtigkeitssenats) des Bundespatentgerichts vom 12. Dezember
      2019 unter Zurückweisung der weitergehenden Rechtsmittel
      abgeändert.

      Das europäische Patent 2 178 232 wird mit Wirkung für die
      Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt,
      dass die Patentansprüche die nachfolgende Fassung erhalten:

             1. A mobile station apparatus comprising:
                 a mapping unit (307) configured to map a sounding reference signal (SRS) to a subframe; and
                 a transmitting unit (309) configured to transmit the
                 mapped sounding reference signal (SRS);
                 characterized in that
                 said mapping unit (307) is adapted to map the sounding
                 reference signal (SRS) in a guard time of the subframe
                 in which a random access preamble is transmitted,
                 the guard time during which nothing is transmitted being
                 added to the random access preamble,
                 wherein the guard time is added after the random access
                 preamble, and
                 said mapping unit (307) is adapted to map the sounding
                 reference signal (SRS) in the tail end of the subframe,
                 and

                        -3-



   wherein the random access preamble is transmitted from
   another mobile station apparatus.

2. The mobile station apparatus according to claim 1,
   wherein said mapping unit (307) is adapted to map the
   sounding reference signal (SRS) such that a time gap
   between the sounding reference signal (SRS) and the
   random access preamble is maximized.

3. The mobile station apparatus according to one of claims
   1 to 2, wherein the random access preamble is transmitted from a mobile station apparatus, which is non-synchronized in an uplink.

4. The mobile station apparatus according to one of claims
   1 to 3, wherein said transmitting unit (309) is adapted to
   transmit the sounding reference signal (SRS) at a constant period.

5. The mobile station apparatus according to one of claims
   1 to 4, wherein said transmitting unit (309) is adapted to
   transmit the sounding reference signal (SRS) at a period
   which is m/n times of a period at which a random access
   preamble is transmitted, wherein m and n are positive
   integers.

6. The mobile station apparatus according to one of claims
   1 to 5, wherein said transmitting unit (309) is adapted to
   transmit the sounding reference signal (SRS) at a constant period in at least part of subframes, in which random access preambles are transmitted.

                          -4-



7.   The mobile station apparatus according to one of claims
     1 to 6, wherein said transmitting unit (309) is adapted to
     transmit the sounding reference signal (SRS) at a constant period in subframes including a subframe, in which
     a random access preamble is transmitted.

8. The mobile station apparatus according to one of claims
     4 to 7, wherein the period is defined by a number of subframes.

9. The mobile station apparatus according to one of claims
     1 to 8, wherein said transmitting unit (309) is adapted to
     transmit the sounding reference signal (SRS) using a frequency hopping.

10. The mobile station apparatus according to one of claims
     1 to 9 further comprising a receiving unit (302) configured
     to receive control information related to a time resource
     of the sounding reference signal (SRS), wherein said
     transmitting unit (309) is adapted to transmit the sounding reference signal (SRS) based on the control information.

11. A transmitting method comprising:
     mapping a sounding reference signal (SRS) to a subframe; and
     transmitting by a mobile station apparatus the mapped
     sounding reference signal (SRS);
     characterized by
     mapping the sounding reference signal (SRS) in a guard
     time of the subframe in which a random access preamble
     is transmitted,

                                -5-



          the guard time during which nothing is transmitted being
          added to the random access preamble,
          wherein the guard time is added after the random access
          preamble, and
          said sounding reference signal (SRS) is mapped in the
          tail end of the subframe, and
          wherein the random access preamble is transmitted from
          another mobile station apparatus.

Im Übrigen wird die Klage abgewiesen.

Von den Kosten des Rechtsstreits tragen die Klägerinnen je zwei
Fünftel und die Beklagte ein Fünftel.

                        Von Rechts wegen

                                                -6-



                                           Tatbestand:

1         Die Beklagte ist Inhaberin des mit Wirkung für die Bundesrepublik
    Deutschland erteilten europäischen Patents 2 178 232 (Streitpatents), das am
    7. August 2008 unter Inanspruchnahme der Priorität einer japanischen Patentanmeldung vom 8. August 2007 angemeldet worden ist und eine Vorrichtung sowie
    ein Verfahren zum Zuordnen und Senden eines Sondierungsreferenzsignals
    (Sounding Reference Signal) in einem mobilen Kommunikationssystem betrifft.

2         Patentanspruch 1, auf den elf weitere Ansprüche zurückbezogen sind, sowie Patentanspruch 13 lauten in der Verfahrenssprache:

          1.   A mobile station apparatus comprising:
               a mapping unit (307) configured to map a sounding reference signal (SRS)
               to a subframe; and
               a transmitting unit (309) configured to transmit the mapped sounding reference signal (SRS);
               characterized in that said mapping unit (307) is adapted to map the sounding
               reference signal (SRS) in a guard time of the subframe in which a random
               access preamble is transmitted,
               the guard time during which nothing is transmitted being added to the
               random access preamble.

          13. A transmitting method comprising:
              mapping a sounding reference signal (SRS) to a subframe; and
              transmitting the mapped sounding reference signal (SRS);
              characterized by mapping the sounding reference signal (SRS) in a guard
              time of the subframe in which a random access preamble is transmitted,
              the guard time during which nothing is transmitted being added to the
              random access preamble.

3         Die Klägerinnen haben geltend gemacht, der Gegenstand des Streitpatents gehe über den Inhalt der ursprünglich eingereichten Unterlagen hinaus
    und sei nicht patentfähig. Die Klägerin zu 1 hat ferner geltend gemacht, die Erfindung sei nicht so offenbart, dass ein Fachmann sie ausführen könne. Die Beklagte hat das Streitpatent in der erteilten Fassung und mit fünfundzwanzig Hilfsanträgen verteidigt.

                                          -7-



4         Das Patentgericht hat das Streitpatent unter Abweisung der weitergehenden Klage im Umfang der Patentansprüche 1 bis 12 für nichtig erklärt. Dagegen
    wenden sich die Berufungen der Klägerinnen und der Beklagten, die ihre erstinstanzlichen Anträge weiterverfolgen.




                                 Entscheidungsgründe:

5         Die Berufungen sind zulässig. Das Rechtsmittel der Beklagten ist hinsichtlich des ersten Hilfsantrags begründet. Das Rechtsmittel der Klägerin hat insoweit Erfolg, als es sich gegen die erteilte Fassung von Patentanspruch 13 richtet.
    Die weitergehenden Rechtsmittel sind unbegründet.

6                Das Streitpatent betrifft eine Mobilstation und ein Verfahren zum
    Übertragen eines Sondierungsreferenzsignals (sounding reference signal, SR-Signal) innerhalb eines mobilen Kommunikationssystems.

7         1.     Ausgangspunkt der Erfindung ist der erwartete Einsatz eines SR-Signals in dem am Prioritätstag in der Entwicklung befindlichen Mobilfunkstandard der vierten Generation (Long Term Evolution, LTE) (Abs. 2).

8         Das SR-Signal soll laut der Beschreibung des Streitpatents nach den
    Überlegungen der Standardisierungsgremien zur Schätzung der Kanalqualität für
    die Frequenzplanung (Scheduling), zur Erkennung des Empfangszeitpunkts und
    zur Steuerung der Sendeleistung im Uplink (also im Kommunikationsweg von den
    Mobilstationen zur Basisstation) eingesetzt werden (Abs. 2).

9         Ein solches SR-Signal könne beispielsweise aus einem Long Block (LB)
    mit einer Länge von 71,4 Mikrosekunden bestehen und einen Cyclic Prefix (CP)
    sowie das eigentliche Referenzsignal umfassen. Die Mobilstation könne solche
    Signale periodisch übertragen, zum Beispiel in Intervallen, die der Länge eines
    Teilrahmens (subframe) entsprächen, also im Abstand von jeweils einer Millisekunde (Abs. 3).

                                            -8-



10          In drei Beiträgen für die zuständige Arbeitsgruppe, darunter ein Beitrag
     von T.              (Improved Non-Synchronized Random Access structure
     for E-UTRA, R1-063213, NK17/K19), werde vorgeschlagen, das SR-Signal stets
     in dem ersten Long Block eines Teilrahmens auf dem Kanal PUSCH (Physical
     Uplink Shared Channel) an die Basisstation zu übertragen. Alternativ werde in
     den Beiträgen von N.        (UL sounding reference signal for EUTRA TDD,
     R1-072989, NK9/K7), S.         (Sounding RS Multiplexing in E-UTRA-UL - Interaction with PUCCH, R1-073092, NK10/K14) und C. (Uplink Sounding Reference Signals for TDD with Alternative Frame Structure, R1-071879, NK11/K15)
     diskutiert, das SR-Signal im letzten Long Block eines Teilrahmens anzuordnen
     (Abs. 6).

11          Beide Vorschläge seien problematisch. Mit zunehmender Anzahl der Mobilstationen in einer Zelle werde der für die Übertragung des SR-Signals vorgesehene Long Block entsprechend häufig benutzt. Andere Mobilstationen könnten
     diese Ressource dann nicht mehr zur Übertragung von Daten verwenden, was
     zu einer verringerten Effizienz führe (Abs. 7).

12          Ferner werde für LTE der Einsatz einer Random-Access-Präambel für den
     ersten Zugriff einer Mobilstation auf das Netzwerk, die Aktualisierung des Übertragungszeitpunkts und die Bestimmung der Kanalgüte im Uplink untersucht. Bei
     dieser Präambel handele es sich um ein Signal, das Identifikationsmerkmale der
     Mobilstation enthalte. Die Präambel werde - ebenso wie das SR-Signal - periodisch auf Anweisung der Basisstation übertragen. Nach den bisherigen Überlegungen betrage die Zeitdauer der Präambel eine Millisekunde, was der Länge
     eines Teilrahmens bzw. vierzehn Long Blocks entspreche. Die Präambel umfasse neben dem eigentlichen Identifikationsmerkmal einen Cyclic Prefix und
     eine Schutzzeit (Guard Time, GT) (Abs. 4).

13          Die Schutzzeit sei eine Nichtübertragungsperiode (Abs. 4). Sie werde benötigt, um Interferenzen durch Signalüberschneidungen mit Daten des nächsten
     Teilrahmens zu vermeiden. Diese könnten entstehen, weil das Signal einer nicht

                                            -9-



     mit der Basisstation synchronisierten Mobilstation verzögert ankommen könne
     (Abs. 5).

14            2.    Vor diesem Hintergrund liegt dem Streitpatent das technische Problem zugrunde, eine effizientere Übertragung des SR-Signals zu ermöglichen.

15            3.    Zur Lösung schlägt das Streitpatent in den Patentansprüchen 1 und
     13 eine Mobilstation und ein Verfahren vor, deren Merkmale sich wie folgt gliedern lassen (die in einem Detail abweichende Merkmalsgliederung des Patentgerichts ist in eckigen Klammern angegeben):

16            a)    Patentanspruch 1:

17    1.       A mobile station apparatus com-       Mobilstationsvorrichtung umfasprising                               send:
      1.1      a mapping unit (307)                  eine Abbildungseinheit (307),
      1.1.1    configured to map a sounding ref- die konfiguriert ist zum Abbilden
               erence signal (SRS) to a subframe eines SR-Signals auf einem Teilrahmen,
      1.1.2    said mapping unit (307) is adapted    und eingerichtet ist zum Abbilden
               to map the sounding reference         des SR-Signals in einem Schutzsignal (SRS) in a guard time of the   zeitintervall des Teilrahmens, in
               subframe in which a random ac-        dem eine Random-Access-Präcess preamble is transmitted,         ambel gesendet wird,
      1.1.3    the guard time during which noth-     wobei das Schutzzeitintervall,
               ing is transmitted being added to     während dem kein Signal gesenthe random access preamble;           det wird, zu der Random-Access-
               [1.1.2]                               Präambel hinzugefügt wird;
      1.2      a transmitting unit (309)             eine Sendeeinheit (309),
      1.2.1    configured to transmit the mapped     die zum Senden des zugeordnesounding reference signal (SRS).      ten SR-Signals konfiguriert ist.

                                            - 10 -




18           b)     Patentanspruch 13:

19    13.     A transmitting method comprising:      Sendeverfahren umfassend:

      13.1    mapping a sounding reference sig- Abbilden eines SR-Signals auf
              nal (SRS) to a subframe; and      einem Teilrahmen,
      13.2    mapping the sounding reference         und zwar in einem Schutzzeitsignal (SRS) in a guard time of the    intervall des Teilrahmens, in dem
              subframe in which a random ac-         eine Random-Access-Präambel
              cess preamble is transmitted,          gesendet wird,
      13.3    the guard time, during which noth-     wobei das Schutzzeitintervall,
              ing is transmitted being added to      während dem kein Signal gesenthe random access preamble;            det wird, zu der Random-Access-Präambel hinzugefügt wird;
      13.4    transmitting the mapped sounding       Senden des abgebildeten SR-
              reference signal (SRS).                Signals.


20           4.     Als Fachmann ist nach den zutreffenden und insoweit von den Parteien nicht beanstandeten Ausführungen des Patentgerichts ein Ingenieur der
     Nachrichten- oder Kommunikationstechnik anzusehen, der über mehrjährige Berufungserfahrung mit der Entwicklung und Standardisierung von Mobilfunksystemen verfügt.

21           Dieser Fachmann ist, wovon das Patentgericht ebenfalls zu Recht ausgegangen ist, mit der aktuellen Version und den wesentlichen Verbesserungsvorschlägen des zum Prioritätstag des Streitpatents in der Entwicklung befindlichen
     LTE-Mobilfunkstandards vertraut. Dass die Entwicklung dieses Standards am
     Prioritätstag in der Fachwelt verfolgt und diskutiert wurde, geht auch aus der Beschreibung des Streitpatents hervor.

                                           - 11 -



22           5.     Einige Merkmale bedürfen näherer Betrachtung:

23           a)     Die Patentansprüche 1 und 13 sehen keine Beschränkung auf LTE
     oder andere Mobilfunkstandards vor.

24           Die vorgeschlagene Lösung ist zwar an den Besonderheiten von LTE
     orientiert. In den Patentansprüchen kommt dies aber nur insoweit zum Ausdruck,
     als SR-Signale sowie Teilrahmen mit einer Random-Access-Präambel und
     einem Schutzzeitintervall vorgesehen sind. Die nähere Ausgestaltung dieser Elemente ist nicht auf die besonderen Festlegungen beschränkt, die der LTE-Standard insoweit vorsieht.

25           b)     Die Merkmale 1.1.1 und 13.1 legen nicht im Einzelnen fest, wie ein
     SR-Signal zusammengesetzt ist.

26           aa)    Wie bereits oben dargelegt wurde, dient ein SR-Signal nach der Beschreibung (Abs. 2) in LTE-Systemen zur Schätzung der Kanalqualität für die
     Frequenzplanung (Scheduling), zur Erkennung des Empfangszeitpunkts und zur
     Steuerung der Sendeleistung im Uplink.

27           Diese Definition ist für die Auslegung der Merkmale 1.1 und 13.1 maßgeblich.

28           Patentanspruch 1 nimmt zwar nicht auf einen bestimmten Mobilfunkstandard Bezug. Er geht aber von dem oben aufgezeigten Verständnis eines SR-Signals aus.

29           bb)    Die nähere Ausgestaltung eines solchen Signals bleibt demgegenüber dem Fachmann überlassen.

30           Insbesondere ist nicht erforderlich, dass das SR-Signal einem Signal entspricht, wie es in LTE-Systemen für die genannten Zwecke eingesetzt wird.

                                            - 12 -



31          cc)    Vor diesem Hintergrund kann auch zur Auslegung des Begriffs des
     Teilrahmens nicht auf die im LTE-Standard einschlägigen Definitionen zurückgegriffen werden.

32          Als Teilrahmen im Sinne von Patentanspruch 1 ist danach eine beliebige
     Struktur anzusehen, die zur Anordnung einer Random-Access-Präambel einschließlich eines Schutzzeitintervalls geeignet ist und die ihrerseits Teil einer beliebigen größeren Struktur ist. Wie diese Strukturen im Einzelnen beschaffen
     sind, bleibt dem Fachmann überlassen.

33          dd)    Die Merkmale 1.1.1 und 13.1 setzen nicht voraus, dass die Mobilstation, die das SR-Signal abbildet und versendet, bereits mit der Basisstation
     synchronisiert ist und dass die Random-Access-Präambel von einer anderen Mobilstation gesendet wird.

34          In diesem Zusammenhang ist unerheblich, ob die Versendung beider Signale durch dieselbe Mobilstation in einem LTE-Netz technisch möglich und sinnvoll ist. Die Patentansprüche 1 und 13 sind nicht auf solche Netze beschränkt
     und sehen auch in Bezug auf die hier relevanten Fragen keine Beschränkungen
     vor.

35          Solche Beschränkungen sind nur in den Patentansprüchen 4 und 5 vorgesehen. Nach Patentanspruch 4 muss die Random-Access-Präambel von einer
     nicht synchronisierten Mobilstation versendet werden. Nach Patentanspruch 5
     muss dies eine andere Mobilstation sein als diejenige, die das SR-Signal abbildet
     und versendet.

36          c)     Zentrale Bedeutung für das angestrebte Ziel der Effizienz kommt
     dem in den Merkmalen 1.1.2 und 1.1.3 bzw. 13.2 und 13.3 vorgesehenen Abbilden des SR-Signals in einem Schutzzeitintervall zu.

                                           - 13 -



37           aa)   Ein Schutzzeitintervall ist nach den Merkmalen 1.1.3 und 13.3 ein
     Zeitraum, der zu einer Random-Access-Präambel hinzugefügt wird und in dem
     keine Signale übertragen werden.

38           Wie bereits oben dargelegt wurde, trägt ein solches Intervall in LTE-Systemen dem Umstand Rechnung, dass die Signale einer noch nicht synchronisierten Mobilstation mit einer gewissen Zeitverzögerung an der Basisstation ankommen können, weil die Entfernung zwischen Mobilstation und Basisstation noch
     nicht bekannt ist und die Mobilstation deshalb nicht die Laufzeit berücksichtigen
     kann, die das Signal bis zur Ankunft an der Basisstation benötigt. Dadurch kann
     es zu Interferenzen mit nachfolgenden Signalen anderer Mobilstationen kommen. Diese lassen sich vermeiden, wenn die noch nicht synchronisierte Mobilstation in bestimmten Intervallen keine Signale überträgt.

39           Diese Zwecksetzung hat in den Patentansprüchen 1 und 13 jedoch keinen
     Niederschlag gefunden. Diese Ansprüche legen sich nicht auf den LTE-Standard
     fest und weisen dem Schutzzeitintervall keine besonderen Funktionen zu. Wie
     bereits dargelegt wurde, sehen sie auch nicht zwingend vor, dass die Random-Access-Präambel von einer nicht synchronisierten Mobilstation und das SR-Signal von einer anderen, synchronisierten Mobilstation übertragen wird.

40           Ein Schutzzeitintervall im Sinne des Streitpatents liegt mithin schon dann
     vor, wenn die beiden eingangs genannten Voraussetzungen erfüllt sind - unabhängig davon, zu welchem Zweck die Übertragung von Signalen unterbleibt.

41           bb)   Das Einfügen von Schutzzeitintervallen hat zur Folge, dass die für
     die Signalübertragung zur Verfügung stehenden Ressourcen nicht vollständig
     genutzt werden. Das Streitpatent setzt einen Teil dieser ungenutzten Ressourcen
     ein, um SR-Signale zu übertragen, und ermöglicht dadurch eine Effizienzsteigerung.

                                            - 14 -



42         Im Ergebnis wird damit das der Random-Access-Präambel hinzugefügte
     Intervall, in dem keine Signale übertragen werden, verkürzt, weil dieses Intervall
     zumindest teilweise zur Übertragung eines SR-Signals genutzt wird.

43         Diese Vorgehensweise erhöht die Gefahr von Interferenzen, der das Einfügen der Schutzzeitintervalle entgegenwirken soll. Nach der Beschreibung des
     Streitpatents kann diese Gefahr jedoch durch bestimmte Maßnahmen minimiert
     und für Mobilstationen, die nicht allzu weit von der Basisstation entfernt sind, sogar vollständig ausgeschlossen werden (Abs. 53 f.). Die Patentansprüche 1 und
     13 enthalten insoweit jedoch keine Beschränkungen. Sie lassen offen, wie stark
     der Zeitraum, in dem keine Signale übertragen werden, durch das Abbilden des
     SR-Signals verkürzt wird und lassen sogar die Möglichkeit zu, diesen Zeitraum
     vollständig durch das SR-Signal auszufüllen.

44         cc)     Aus den Merkmalen 1.1.3 und 13.3 ergibt sich nicht, an welcher
     Stelle das Schutzzeitintervall in den Teilrahmen für die Random-Access-Präambel einzufügen ist.

45         Aus der in diesen Merkmalen verwendeten Formulierung, dass das
     Schutzzeitintervall der Random-Access-Präambel hinzuzufügen ist, ergeben sich
     insoweit keine Anforderungen. Ein Hinzufügen ist danach sowohl vor als auch
     nach der Präambel möglich. Möglich ist auch, sowohl vor als auch nach der Präambel ein Schutzzeitintervall vorzusehen, wie dies bei einem der in der Beschreibung geschilderten Ausführungsbeispiele (Abs. 69 ff.) erfolgt.

46         Weitergehende Anforderungen sieht insoweit Patentanspruch 2 vor. Danach muss das SR-Signal am Ende eines Teilrahmens platziert sein. Daraus
     folgt, dass auch das Schutzzeitintervall, in dem das SR-Signal gemäß Merkmal
     1.1.2 abgebildet wird, am Ende des Teilrahmens angeordnet sein muss.

                                          - 15 -



47         d)     Die Merkmale 1.2.1 und 13.4 legen nicht fest, wie häufig und über
     welchen Kanal das SR-Signal gesendet wird.

48         Auch insoweit ist unerheblich, welche Zeitintervalle und Kanäle im Stand
     der Technik üblich waren. Die Patentansprüche 1 und 13 enthalten keine Festlegung auf einen bestimmten Standard.

49         e)     Die in Patentanspruch 1 geschützte Mobilstation muss Einrichtungen aufweisen, die geeignet sind, die in den Merkmalen 1.1.1, 1.1.2 und 1.2.1
     vorgesehenen Funktionen zu erfüllen.

50         aa)    Die Merkmale eines Vorrichtungsanspruchs haben die Funktion,
     die geschützte Sache als solche zu beschreiben, so dass der auf diese Weise -
     regelmäßig räumlich-körperlich - definierte Gegenstand unabhängig davon geschützt ist, wie er hergestellt worden ist und zu welchem Zweck er tatsächlich
     verwendet wird (vgl. BGH, Urteil vom 7. Juni 2006 - X ZR 105/04, GRUR 2006,
     923, 925 - Luftabscheider für Milchsammelanlage; Urteil vom 13. Dezember 2005
     - X ZR 14/02, GRUR 2006, 399, 401 - Rangierkatze).

51         Deswegen sind im Patentanspruch enthaltene Zweck-, Wirkungs- oder
     Funktionsangaben jedoch nicht schlechthin bedeutungslos. Sie können vielmehr
     als Bestandteile des Patentanspruchs an dessen Aufgabe teilnehmen, den geschützten Gegenstand zu bestimmen und damit zugleich zu begrenzen, wenn sie
     das Vorrichtungselement, auf das sie sich beziehen, als ein solches definieren,
     das so ausgebildet sein muss, dass es die betreffende Funktion erfüllen kann
     (st. Rspr., zuletzt BGH, Urteil vom 3. November 2020 - X ZR 85/19, GRUR 2021,
     462 Rn. 49 - Fensterflügel; Urteil vom 24. April 2018 - X ZR 50/16, GRUR 2018,
     1128 Rn. 12 - Gurtstraffer).

52         bb)    Nach diesen Grundsätzen erfordern die Merkmale 1.1.1 und 1.1.2,
     dass die Mobilstation so ausgebildet ist, dass sie ein SR-Signal im Schutzzeitintervall eines Teilrahmens abbilden kann, in dem eine Random-Access-Präambel
     gesendet wird.

                                          - 16 -



53         (1)    Wie auch das Patentgericht im Ansatz nicht verkannt hat, genügt
     es hierfür nicht, wenn die Mobilstation durch Programmierung so eingerichtet
     werden kann, dass sie die genannte Funktion erfüllen kann.

54         Nach der Beschreibung des Streitpatents können die Funktionen zwar
     wahlweise mit speziell konfigurierten integrierten Schaltkreisen (Abs. 102) oder
     mit universell einsetzbaren Prozessoren (Abs. 103) verwirklicht werden. Auch im
     zuletzt genannten Fall genügt es aber nicht, wenn die Mobilstation durch Aufspielen geeigneter Software oder sonstige Konfigurationsmaßnahmen in den Stand
     versetzt werden kann, die erforderlichen Funktionen zu erfüllen. Vielmehr muss
     sie bereits entsprechend konfiguriert sein, also bereits eine geeignete Software
     oder sonstige Mittel umfassen, die in entsprechenden Betriebssituationen die
     Verwirklichung dieser Funktionen ermöglichen.

55         (2)    Dies schließt nicht aus, dass die auf der Mobilstation absolvierten
     Verfahrensschritte von der Basisstation oder sonstigen externen Komponenten
     aufgerufen und gesteuert werden. Die Mobilstation muss aber auch in diesem
     Fall zumindest so eingerichtet sein, dass sie entsprechende Aufrufe und Steuerbefehle interpretieren und verarbeiten kann. Hieran fehlt es zum Beispiel, wenn
     die Mobilstation hierzu erst umprogrammiert oder mit zusätzlichen oder geänderten Hardwarekomponenten ausgerüstet werden muss.

56         (3)    Entgegen der Auffassung des Patentgerichts ist andererseits nicht
     ausgeschlossen, dass die Mobilstation das SR-Signal (auch) aufgrund "eigener
     Entscheidungsfreiheit", also unabhängig von Vorgaben der Basisstation abbildet.

57         In diesem Zusammenhang ist unerheblich, ob und inwieweit eine solche
     Vorgehensweise in einem LTE-Netz oder sonstigen gebräuchlichen Mobilfunknetzen technisch möglich und sinnvoll ist. Patentanspruch 1 enthält keine Festlegung auf ein bestimmtes System.

                                           - 17 -



58         (4)    Die geringfügige Abweichung im Wortlaut der Merkmale 1.1.1 (configured) und 1.1.2 (adapted) führt nicht zu inhaltlichen Unterschieden.

59         Beide Merkmale erfordern, dass die Mobilstation ohne Umprogrammierung und ohne Ergänzung oder Änderung von Hardwarekomponenten zur Erfüllung der entsprechenden Funktionen geeignet ist, wie dies oben im Einzelnen
     dargelegt wurde.

60         cc)    Entsprechend dazu muss die Mobilstation gemäß Merkmal 1.2.1 so
     ausgebildet sein, dass sie das zugeordnete SR-Signal versenden kann.

61         f)     Nach Patentanspruch 13 müssen die in den korrespondierenden
     Merkmalen 13.1, 13.2 und 13.4 vorgesehenen Verfahrensschritte tatsächlich
     ausgeführt werden. Zutreffend gehen das Patentgericht und die Parteien davon
     aus, dass dies in der Mobilstation geschieht.

62         Die zuletzt genannte Anforderung ist zwar im Wortlaut von Patentanspruch 13 nicht ausdrücklich vorgesehen. Sie ergibt sich aber aus dem bereits
     oben aufgezeigten Umstand, dass ein SR-Signal zur Festlegung von Parametern
     im Uplink dient. Diesem Umstand ist zu entnehmen, dass das Signal von einer
     Mobilstation gebildet und versendet werden muss. Dass dieser Vorgang von der
     Basisstation ausgelöst und gesteuert wird, ist auch in diesem Zusammenhang
     weder ausgeschlossen noch zwingend erforderlich.

63                Zur Begründung seiner Entscheidung hat das Patentgericht, soweit
     für das Berufungsverfahren von Bedeutung, im Wesentlichen ausgeführt:

64         Der Gegenstand des Streitpatents gehe nicht über den Inhalt der ursprünglich eingereichten Unterlagen hinaus. Diese offenbarten auch Ausführungsformen, bei denen die Mobilstation ausschließlich Vorgaben der Basisstation umsetze. Ebenfalls offenbart sei eine Abbildungseinheit (mapping unit). Die
     in den Anmeldeunterlagen verwendeten Begriffe "to arrange" und "arrangement"
     umfassten die im Streitpatent verwendeten Begriffe "to map" und "mapping".

                                            - 18 -



     Diese beschrieben eine Minimalausgestaltung und seien bereits vor dem Prioritätstag für das Anordnen eines SR-Signals in einem Teilrahmen verwendet worden.

65          Der Gegenstand der erteilten Fassung von Patentanspruch 1 sei durch
     NK9/K7 vollständig vorweggenommen. Dieser Beitrag beschäftigte sich zwar nur
     mit der Abbildung und Versendung eines SR-Signals, nicht hingegen mit einer
     Random-Access-Präambel. Eine entsprechend den Vorschlägen aus NK9/K7
     ausgestaltete Mobilstation sei aber in der Lage, ein SR-Signal im Schutzzeitintervall eines Teilrahmens für eine Random-Access-Präambel abzubilden, weil
     es nach NK9/K7 möglich sein müsse, das SR-Signal im ersten oder im letzten
     Long Block eines jeden Teilrahmens zu platzieren. Dass diese Eignung erst
     durch weitere Maßnahmen in der Mobilstation erreicht werden könnte, sei nicht
     erkennbar.

66          Aus entsprechenden Gründen sei der mit den Hilfsanträgen 1, 2, 2A, 3,
     3A, 5A, 6, 7, 8 und 9 verteidigte Gegenstand von Patentanspruch 1 ebenfalls
     nicht patentfähig. In der Fassung nach den Hilfsanträgen 4 und 5 sei Patentanspruch 1 unzulässig erweitert.

67          Dagegen sei der mit Hilfsantrag 10 isoliert verteidigte Gegenstand von
     Patentanspruch 13 patentfähig.

68          Das tatsächliche Abbilden des SR-Signals in dem Schutzzeitintervall eines
     Teilrahmens für eine Random-Access-Präambel werde durch NK9/K7 weder vorweggenommen noch nahegelegt. Ein solches Verfahren werde auch durch den
     Beitrag von T.               (Random Access preamble design for E-UTRA,
     R1-061392, K9) nicht vorweggenommen. K9 beschäftige sich nicht mit der Übermittlung eines SR-Signals einer synchronisierten Mobilstation. Merkmal 1.1.1
     setze demgegenüber voraus, dass die Mobilstation, die das SR-Signal abbilde,
     bereits im Uplink synchronisiert sei. Gleiches gelte hinsichtlich zwei weiterer Vorschläge von T.                   (Synchronized Random Access structure for
     E-UTRA, R1-063215, K18; Preamble Based Scheduling Request: a Generic

                                          - 19 -



     Structure, R1-072193, ZP21); dort sei zudem kein Schutzzeitintervall vorgesehen. Die internationale Patentanmeldung 2007/126793 (K12) sowie die Beiträge
     NK10/K14 und NK11/K15 offenbarten nicht, ein SR-Signal in einem Schutzzeitintervall abzubilden. Gleiches gelte für die US-Patentschrift 6 381 229 (K13),
     deren Offenbarungsgehalt nicht über denjenigen von K9 hinausgehe.

69         Der Gegenstand von Patentanspruch 13 habe ausgehend von NK9/K7
     auch nicht in Kombination mit der der technischen Spezifikation 3GPP TS 36.211
     V1.2.0 (2007-06) (NK19/K8) nahegelegen. NK9/K7 weise keinen Bezug zu einer
     Random-Access-Präambel auf. Zudem entnehme der Fachmann NK19/K8, das
     Schutzzeitintervall der Random-Access-Präambel von einer Datenübertragung
     freizuhalten. Gegenteiliges folge nicht daraus, dass sich aus K18, einem weiteren
     Beitrag von T.             (Synchronized Random Access structure and performance for E-UTRA, 3GPP, R1-061750, K20) und ZP21 der Hinweis entnehmen lasse, in einem PRACH-Kanal auch noch andere Signale zu senden. Hieraus ergebe sich keine Anregung, ein SR-Signal gerade in dem nach dem Stand
     der Technik übertragungsfreien Schutzzeitintervall einer Random-Access-Präambel anzuordnen.

70                Diese Beurteilung hält der Überprüfung im Berufungsverfahren
     nicht in vollem Umfang stand.

71         1.     Das Patentgericht hat zutreffend entschieden, dass der Gegenstand der Patentansprüche 1 und 13 nicht über den Inhalt der ursprünglich eingereichten Unterlagen hinausgeht.

72         a)     Wie bereits ausgeführt wurde, lassen die Patentansprüche 1 und
     13 offen, ob das Abbilden (mapping) des SR-Signals ausschließlich aufgrund von
     Systemvorgaben oder zumindest teilweise aufgrund eigener "Entscheidungskompetenz" der Mobilstation umgesetzt wird.

                                          - 20 -



73         b)     Dies ist entgegen der Auffassung der Klägerinnen bereits den ursprünglichen Anmeldeunterlagen als zur Erfindung gehörend zu entnehmen.

74         Entgegen der Auffassung der Klägerinnen sind mit den in der Anmeldung
     verwendeten Begriffen nicht nur Mobilstationen offenbart, denen zumindest eine
     gewisse eigene Entscheidungsfreiheit bei der Anordnung des SR-Signals verbleibt, sondern auch solche, bei denen diese Vorgänge von der Basisstation gesteuert werden.

75         aa)    Die in den ursprünglichen Unterlagen formulierten Ansprüche 13
     und 14 betreffen eine Mobilstation mit einem Funktionsumfang, wie er auch in
     den Merkmalen 1.1.1, 1.1.2 und 1.1.3 definiert ist. Dass die Mobilstation nach
     den Ansprüchen 13 und 14 der Anmeldung die betreffenden Verfahrensschritte
     ausführt, während das Streitpatent nur vorsieht, dass die Mobilstation entsprechend konfiguriert bzw. eingerichtet ist, begründet keinen relevanten Unterschied.

76         Dabei kann dahingestellt bleiben, ob die in der Anmeldung formulierten
     Ansprüche nur auf solche Vorrichtungen gerichtet sind, bei denen die spezifizierten Funktionen tatsächlich ausgeführt werden. Selbst wenn diese Frage zu bejahen wäre, ergäbe sich schon aus dem Umstand, dass die Anmeldung Schutz für
     eine Vorrichtung begehrt, hinreichend deutlich, dass sich dieses Begehren auch
     auf solche Vorrichtungen bezieht, die eine entsprechende Eignung aufweisen.

77         bb)    Dass in der Anmeldung anstelle der in der Patentschrift verwendeten Begriffe "to map" und "mapping unit" die Begriffe "to arrange" und "arrangement section" verwendet werden, begründet ebenfalls keine inhaltliche Abweichung.

78         Selbst wenn mit dem Patentgericht anzunehmen wäre, dass der Begriff "to
     arrange" auch Vorgehensweisen mit eigener Entscheidungsbefugnis umfasst,
     während der Begriff "to map" auf die Umsetzung externer Vorgaben beschränkt

                                          - 21 -



     ist, ergäbe sich aus dem Umstand, dass die Anmeldung den weiteren Begriff verwendet, nur, dass eine eigenständige Vorgehensweise der Mobilstation nicht
     ausgeschlossen ist. Weder dem Wortlaut der Ansprüche noch dem sonstigen Inhalt der Anmeldung ist hingegen zu entnehmen, dass diese Möglichkeit zwingend
     verwirklicht sein muss.

79         (1)    Wie das Patentgericht zutreffend ausgeführt hat, umfasst der Begriff "to arrange" jedenfalls auch eine extern gesteuerte Vorgehensweise im
     Sinne von "to map".

80         (2)    Entgegen der Auffassung der Klägerinnen ergeben sich aus den in
     der Anmeldung - ebenso wie im Streitpatent - geschilderten Ausführungsbeispielen (NK2/K2 Abs. 45 ff.) keine weitergehenden Anforderungen.

81         Diese Ausführungen beschreiben allerdings lediglich Verfahrensschritte,
     bei denen die Mobilstation die maßgeblichen Verfahrensparameter bestimmt und
     die Signale entsprechend anordnet. Hierbei ist jedoch vorgesehen, dass die
     Mobilstation Vorgaben zu den maßgeblichen Zeitintervallen erhält (Abs. 57 f.).
     Dies lässt die Möglichkeit offen, dass die Mobilstation die Anordnung ausschließlich anhand solcher Vorgaben vornimmt.

82         Selbst wenn den Ausführungsbeispielen zu entnehmen wäre, dass der
     Mobilstation ein eigener Entscheidungsspielraum verbleibt, könnte der Anmeldung vor diesem Hintergrund nicht entnommen werden, dass eine solche Ausgestaltung zwingend ist, abweichende Ausgestaltungen also nicht zur Erfindung
     gehören.

83         Der Umstand, dass alle in einer Anmeldung geschilderten Ausführungsbeispiele ein bestimmtes Merkmal aufweisen, steht der Beanspruchung von
     Schutz für Ausführungsformen ohne dieses Merkmal nicht entgegen, wenn sich
     dem Inhalt der Anmeldung kein konkreter Bezug zwischen dem betreffenden

                                           - 22 -



     Merkmal und den im Anspruch vorgesehenen Mitteln zur Lösung eines geschilderten technischen Problems entnehmen lässt (vgl. BGH, Urteil vom 7. November 2017 - X ZR 63/15, GRUR 2018, 175 Rn. 35 - Digitales Buch).

84         Im Streitfall ist den ursprünglich eingereichten Unterlagen nicht zu entnehmen, dass eine zumindest partielle Entscheidungsfreiheit der Mobilstation für die
     offenbarte Vorgehensweise und die Lösung des technischen Problems, ein SR-Signal möglichst effizient zu übertragen, mit Vorteilen verbunden ist. Solche Vorteile werden von den Klägerinnen auch nicht aufgezeigt.

85         2.     Ferner hat das Patentgericht mit zutreffender Begründung angenommen, dass der Gegenstand des Streitpatents so offenbart ist, dass ein Fachmann ihn ausführen kann. Die Klägerinnen erheben in ihrer Berufung insoweit
     keine Einwendungen.

86         3.     Entgegen der Auffassung des Patentgerichts ist der Gegenstand
     von Patentanspruch 1 in NK9/K7 nicht vollständig offenbart.

87         a)     NK9/K7, die im Streitpatent als Stand der Technik benannt ist
     (Abs. 6), knüpft an den in der Entwicklung befindlichen LTE-Mobilfunkstandard
     an und befasst sich mit einer möglichen Anordnung von SR-Signalen im Uplink.

88         In NK9/K7 wird ausgeführt, nach den bisherigen Überlegungen sei für die
     Übersendung der SR-Signale im Uplink ein Long Block vorgesehen. Allerdings
     sei die Platzierung des SR-Signals im Rahmen noch offen (S. 1 Nr. 1).

89         In der Rahmenstruktur für Zeitduplex (time division duplex, TDD) sei die
     Verwendung eines SR-Signals zumindest für die kanalabhängige Zeitplanung
     (channel dependent scheduling) im Uplink vorgesehen. Hierzu solle ein Long
     Block pro Übertragungszeitintervall (TTI) verwendet werden. Die Häufigkeit der
     Übertragung werde durch die Basisstation vorgegeben. Wenn ein solches kanalabhängiges Scheduling unterstützt werde, sei es von entscheidender Bedeutung,

                                             - 23 -



     dass die Mobilstation die Möglichkeit habe, ein Uplink-SR-Signal in jedem Teilrahmen zu senden, und zwar unabhängig von der Anzahl der Uplink-Teilrahmen
     (S. 1 Nr. 2). In der abschließenden Zusammenfassung wird daher vorgeschlagen, dass jeder Uplink-Teilrahmen die Uplink-Sondierungsfähigkeit (sounding
     capability) aufweisen sollte (S. 2 Nr. 3).

90          Wegen der Reziprozität der Kanäle bei Zeitduplex könne das SR-Signal
     daneben auch zur Unterstützung bestimmter Funktionen im Downlink verwendet
     werden (S. 1 Nr. 2).

91          Zur Platzierung des SR-Signals sei bislang vorgeschlagen worden, dieses
     entweder im ersten oder im letzten Long Block eines Teilrahmens anzuordnen.
     Wenn das SR-Signal zur Unterstützung von Downlink-Funktionen genutzt werde,
     sei die Frage der Platzierung des SR-Signals mit Blick auf die Kanalreziprozität
     von größerer Bedeutung (S. 1 Nr. 2).

92          Die möglichen Anordnungen eines SR-Signals am Anfang oder am Ende
     eines Uplink-Teilrahmens ergäben sich aus den nachfolgend wiedergegebenen
     Figuren 1 und 2 betreffend einen TDD-Rahmen des Typs 2.

                                          - 24 -




93          Figur 1 zeigt die Anordnung eines (grün kolorierten) SR-Signals im letzten
     Long Block eines Uplink-Teilrahmens, der durch einen nach oben gerichteten
     Pfeil gekennzeichnet ist. Figur 2 stellt die Anordnung des SR-Signals im ersten
     Long Block eines Uplink-Teilrahmens dar (S. 1 Nr. 2 unten).

94          Wenn SR-Signale auch zur Unterstützung von Downlink-Funktionen verwendet würden, sei eine Platzierung des SR-Signals am Ende des Teilrahmens
     vorzuziehen, weil dies die Verwendung eines Kanals mit der kürzest möglichen
     Verzögerung im Downlink ermögliche (S. 2 oben). Zur Unterstützung von Uplink-Funktionen sei die Platzierungsfrage weniger bedeutsam. Eine Anordnung im
     letzten Long Block ermögliche aber eine höhere Genauigkeit der Kanalzuweisung (S. 2 vor Nr. 3).

95          Abschließend weist NK9/K7 darauf hin, die anhand von TDD-Rahmen des
     Typs 2 gezogenen Schlussfolgerungen seien auch für TDD-Rahmen des Typs 1
     gültig (S. 2 Nr. 3).

                                            - 25 -



96          b)     Damit fehlt es an einer Offenbarung des Merkmals 1.1.2.

97          aa)    Vorweggenommen sind, wie auch die Beklagte nicht in Zweifel
      zieht, die Merkmale 1, 1.1, 1.1.1 und 1.2.

98          bb)    Nicht offenbart ist Merkmal 1.1.2.

99          (1)    Wie auch das Patentgericht im Ansatz nicht verkannt hat, offenbart
      NK9/K7 nicht die Anordnung von SR-Signalen in einem Teilrahmen für eine Random-Access-Präambel.

100         NK9/K7 befasst sich nur mit der Übertragung von SR-Signalen und geht
      hinsichtlich der Struktur der hierfür eingesetzten Rahmen vom damaligen Stand
      der Technik aus, der zwei unterschiedliche Typen von TDD-Rahmen vorsah.

101         (2)    Diese Strukturen sind in der ebenfalls vom Juni 2007 stammenden
      Spezifikation NK19/K8 dargestellt.

102         (a)    Die TDD-Rahmenstruktur des Typs 1 ist in der nachfolgend wiedergegebenen Figur 1 dargestellt.




103         Ein solcher Rahmen weist eine Dauer von zehn Millisekunden auf. Jeder
      Rahmen besteht aus zwanzig Slots (0 bis 19) zu je einer halben Millisekunde. Ein
      Teilrahmen besteht aus zwei aufeinanderfolgenden Slots (Abschnitt 4.1).

                                            - 26 -



104         Die Struktur einer Random-Access-Präambel für TDD-Rahmen vom Typ 1
      ist in der nachfolgend wiedergegebenen Figur 19 dargestellt.




105         Die Gesamtdauer TRA ist in Tabelle 20 mit einer Millisekunde angegeben,
      also der Dauer eines Teilrahmens. Hiervon entfallen 0,8 Millisekunden auf die
      eigentliche Präambel und jeweils rund 0,1 Millisekunden auf einen Cyclic Prefix
      (CP) und ein Schutzintervall (TGT). Letzteres ist als Zeitraum definiert, während
      dessen nichts übermittelt wird (Abschnitt 6.7.1).

106         (b)    Eine TDD-Rahmenstruktur des Typs 2 ist in der nachfolgend wiedergegebenen Figur 2 dargestellt.

                                             - 27 -



107          Ein solcher Rahmen weist ebenfalls eine Dauer von zehn Millisekunden
      auf und ist unterteilt in zwei Halbrahmen mit einer Länge von jeweils fünf Millisekunden. Jeder Halbrahmen besteht aus sieben Slots (0 bis 6) zu je 0,675 Millisekunden (insgesamt also 4,725 Millisekunden) und aus drei Spezialfeldern. Ein
      Teilrahmen wird durch jeweils einen Slot gebildet. Im letzten Teil der Teilrahmen
      1 bis 6 wird kein Signal übertragen. Hierdurch entsteht ein Schutzintervall. Das
      Spezialfeld UpPTS und der Teilrahmen 1 sind stets für die Übertragung im Uplink
      reserviert (Abschnitt 4.2).

108          Eine Random-Access-Präambel wird in dieser Rahmenstruktur in dem
      Spezialfeld UpPTS abgebildet (Abschnitt 6.7.1, Tabelle 20). Das Schutzintervall
      umfasst danach einen Zeitraum von rund 0,008 Millisekunden (244 oder 256 x
      TS; mit TS = 1/30720 Millisekunde, vgl. oben Figuren 1 und 2 sowie Abschnitt 4).

109          Diese Struktur stimmt überein mit der Struktur, die in den Figuren 1 und 2
      von NK9/K7 dargestellt ist. Diese zeigt nach dem Teilrahmen 0 jeweils einen
      schraffierten Bereich für die Spezialfelder.

110          (3)    Wie auch das Patentgericht nicht verkannt hat, ergibt sich auch vor
      diesem Hintergrund aus NK9/K7 nicht der Vorschlag, SR-Signale im Schutzintervall eines Teilrahmens für eine Random-Access-Präambel anzuordnen.

111          Bei den in NK9/K7 dargestellten TDD-Rahmen des Typs 2 werden die SR-Signale nicht in den Spezialfeldern nach dem ersten Teilrahmen angeordnet,
      sondern in dem darauf folgenden zweiten Teilrahmen. Selbst wenn unterstellt
      würde, dass sich die in NK9/K7 definierte Anforderung, die Mobilstation müsse in
      der Lage sein, ein SR-Signal in jedem Teilrahmen anzuordnen, auch auf die Spezialfelder bezieht, ergäbe sich daraus, dass von dieser Möglichkeit bei Rahmen
      des Typs 2 kein Gebrauch gemacht wird.

112          In Bezug auf TDD-Rahmen des Typs 1 ergibt sich kein weitergehender
      Offenbarungsgehalt. Dem pauschalen Hinweis am Ende von NK9/K7, dass für
      diese Rahmen dasselbe gelte wie für Rahmen des Typs 2, lässt sich allenfalls

                                            - 28 -



      entnehmen, dass auch bei Rahmen des Typs 1 das SR-Signal im ersten Teilrahmen für den Uplink angeordnet werden soll. Über den Standort von Random-Access-Präambeln kann der Hinweis hingegen keinen Aufschluss geben, weil
      die hierfür beim Typ 2 vorgesehenen Spezialfelder beim Typ 1 nicht zur Verfügung stehen. Auch NK19/K8 enthält hierzu keine Festlegungen.

113          (4)    Entgegen der Auffassung des Patentgerichts kann vor diesem Hintergrund nicht angenommen werden, dass eine Mobilstation, die die Anforderungen aus NK9/K7 erfüllt, ohne weiteres geeignet ist, das SR-Signal im Schutzzeitintervall eines Teilrahmens für eine Random-Access-Präambel abzubilden.

114          Hierbei kann mit dem Patentgericht unterstellt werden, dass die erforderliche Eignung bestünde, wenn eine entsprechend den Anforderungen aus NK9/K7
      eingerichtete Mobilstation den Befehl, das SR-Signal in einem beliebigen, von
      der Basisstation vorgegebenen Teilrahmen abzubilden, unabhängig von allen anderen Gegebenheiten ausführen würde. Eine solche Ausgestaltung der Mobilstation lässt sich NK9/K7 jedenfalls nicht eindeutig entnehmen.

115          (a)    Die in NK9/K7 formulierten Anforderungen, die Mobilstation müsse
      in der Lage sein, ein Uplink-SR-Signal in jedem Teilrahmen zu senden, und jeder
      Uplink-Teilrahmen sollte die Uplink-Sondierungsfähigkeit (sounding capability)
      aufweisen, könnte bei isolierter Betrachtung allerdings dahin verstanden werden,
      dass dies ohne jede Einschränkung gilt, also auch für Uplink-Teilrahmen, in
      denen eine Random-Access-Präambel mit einem am Ende angeordneten
      Schutzintervall enthalten ist.

116          (b)    Diese Anforderungen wären jedoch nur dann zu verwirklichen,
      wenn nicht nur das in NK9/K7 behandelte Konzept für SR-Signale geändert
      würde, sondern zusätzlich auch die in NK19/K8 vorgegebene Rahmenstruktur.

                                            - 29 -



117          Bei Rahmen des Typs 2 ergibt sich dies schon daraus, dass in dem für die
      Random-Access-Präambel vorgesehenen Spezialfeld UpPTS nur rund 0,008 Millisekunden für ein Schutzintervall zur Verfügung stehen, ein SR-Signal aber rund
      0,07 Millisekunden benötigt, also rund den neunfachen Zeitraum.

118          Bei Rahmen des Typs 1 müsste die in NK19/K8 definierte Struktur zumindest insoweit geändert werden, als der für das Schutzintervall der Random-Access-Präambel vorgesehene Bereich entgegen der Vorgabe aus NK19/K8 zumindest teilweise für die Übertragung von Signalen genutzt wird.

119          (c)    Eine eindeutige und unmittelbare Anweisung, die in NK19/K8 vorgegebene Rahmenstruktur zu modifizieren, lässt sich NK9/K7 nicht entnehmen.

120          Wie bereits oben dargelegt wurde, verweist NK9/K7 wegen der Rahmenstruktur auf den damaligen Stand der Entwicklungsarbeiten, wie er in NK19/K8
      dokumentiert ist. Hinweise darauf, dass diese Struktur ebenfalls einer Anpassung
      bedarf, finden sich in dem Beitrag nicht. Vielmehr wird für Rahmen des Typs 2
      eine Lösung vorgeschlagen, die sich in die vorhandenen Strukturen einfügt, und
      die Einschätzung geäußert, dass diese Vorgehensweise auch für Rahmen des
      Typs 1 geeignet sei.

121          (d)    Bei dieser Ausgangslage kann nicht angenommen werden, dass
      ein entsprechend den Vorgaben aus NK9/K7 konfiguriertes Mobilteil in der Lage
      ist, ein SR-Signal im Schutzzeitintervall eines Teilrahmens für eine Random-Access-Präambel abzubilden.

122          Die in NK9/K7 enthaltene Bezugnahme auf die vorgegebene Rahmenstruktur lässt vielmehr erwarten, dass ein Mobilteil so konfiguriert ist, dass es
      auch den Anforderungen aus NK19/K8 genügt, also in Bereichen, die für Schutzintervalle vorgesehen sind, keine Signale überträgt. Ein solches Mobilteil ist ohne
      Änderungen an der Soft- oder Hardware nicht in der Lage, in solchen Bereichen
      ein SR-Signal abzubilden. Es könnte einen entsprechenden Befehl der Basisstation folglich nicht ausführen.

                                            - 30 -



123          (e)   NK9/K7 offenbart entgegen der Auffassung der Klägerinnen auch
      nicht, dass eine Mobilstation zur Umsetzung der dort genannten Anforderungen
      so auszubilden ist, dass sie beim Abbilden eines SR-Signals am Ende eines Teilrahmens ausschließlich Anweisungen der Basisstation befolgt und solche Anweisungen auch dann ohne weiteres umsetzen kann, wenn diese zu Vorgaben, die
      sich aus anderen Teilen der Spezifikation ergeben, in Widerspruch stehen.

124          NK9/K7 enthält keine näheren Erläuterungen zu der Frage, wie die dort
      formulierten Anforderungen in einer Mobilstation technisch umgesetzt werden
      sollen. Ein eindeutiger Offenbarungsgehalt zu dieser Frage könnte der Entgegenhaltung deshalb allenfalls dann entnommen werden, wenn die von den Klägerinnen postulierte Vorgehensweise am Prioritätstag aus fachlicher Sicht die
      einzige Möglichkeit dargestellt hätte, die genannten Anforderungen zu erfüllen.

125          Diese Voraussetzung liegt entgegen der Auffassung der Klägerinnen nicht
      vor.

126          Die Beklagte hat insoweit unwidersprochen vorgetragen, dass die Anforderungen aus NK9/K7 auch dergestalt umgesetzt werden können, dass die
      Basisstation der Mobilstation einerseits die abstrakte Regel vorgibt, ein SR-Signal grundsätzlich am Ende jedes Uplink-Teilrahmens zu übertragen, andererseits
      aber mitteilt, welche Ressourcen für die Übertragung von Random-Access-Präambeln reserviert sind, und dass die Mobilstation diese divergierenden Vorgaben
      dahin umsetzt, dass die Anordnung eines SR-Signals in Teilrahmen unterbleibt,
      die für Random-Access-Präambeln reserviert sind. Bei dieser Ausgestaltung verwirklicht die Mobilstation das Merkmal 1.1.2 nicht.

127                Das angefochtene Urteil erweist sich in Bezug auf die erteilte Fassung von Patentanspruch 1 aus anderen Gründen als im Ergebnis zutreffend
      (§ 119 Abs. 1 PatG).

                                            - 31 -



128           Entgegen der Auffassung des Patentgerichts ist der Gegenstand von
      Patentanspruch 13 nicht neu. Für Patentanspruch 1 ergibt sich keine abweichende Beurteilung.

129           1.    Der Gegenstand von Patentanspruch 13 ist nicht neu.

130           a)    Wie das Patentgericht mit zutreffender Begründung entschieden
      hat, wird der Gegenstand von Patentanspruch 13 durch NK9/K7 nicht vollständig
      vorweggenommen.

131           NK9/K7 offenbart nicht die Merkmale 13.2 bis 13.4.

132           Wie bereits im Zusammenhang mit Patentanspruch 1 ausgeführt wurde,
      lässt sich NK9/K7 nicht eindeutig und unmittelbar die Anweisung entnehmen, ein
      SR-Signal in dem Schutzintervall eines Teilrahmens für eine Random-Access-Präambel abzubilden und zu senden.

133           b)    Ob der Gegenstand von Patentanspruch 13 durch die weiteren Dokumente, insbesondere durch K9 und eine Zusammenschau von K18 bis K20
      vorweggenommen ist, kann dahinstehen, weil sein Gegenstand jedenfalls durch
      K13 vollständig vorweggenommen ist.

134           aa)   K13 betrifft die Datenübermittlung durch eine Mobilstation, insbesondere in einem WCDMA-Kommunikationssystem (Wideband Code Division
      Multiple Access).

135           In dem beschriebenen System sendet eine Mobilstation zum Erstzugriff
      auf das Netzwerk eine Präambel und eine Signatur. Zugleich ist die Übermittlung
      eines Datenteils vorgesehen. Das zu sendende Signal wird stark gespreizt, so
      dass es eine große Bandbreite annimmt. Mit dem Empfang der Präambel und
      der Signatur kann die Basisstation insbesondere die sogenannten Rake-Finger
      allokieren, um damit die nachfolgende Verarbeitung der Datenteile durch die
      Rake-Empfängereinheit zu ermöglichen (Sp. 3 Z. 36-47; Sp. 8 Z. 7 ff., Sp. 10
      Z. 23 ff.).

                                             - 32 -



136          Die Verarbeitung der Präambel und der Signatur in der Basisstation benötigt allerdings Zeit. Deshalb muss die Basisstation die empfangenen Signale
      unter Umständen zwischenspeichern (Sp. 4 Z. 8-25).

137          Zur Lösung dieses Problems schlägt K13 unter Verweis auf die parallele
      US-Patentanmeldung 09/079438 vor, die Datenübertragung nach der Übermittlung von Präambel und Signatur erst mit einem zeitlichen Versatz zu beginnen
      (Sp. 4 Z. 31 ff.). Eine solche Ausgestaltung ist in Figur 4 dargestellt, die nachfolgend wiedergegeben ist.




138          Die Rahmenstruktur ist mit einem separaten Präambel- und Datenteil ausgestattet. Ein Schutzintervall (TG) wird vorzugsweise zwischen den Präambelund den Datenteilen eingefügt (Sp. 7 Z. 29 ff., Sp. 6 Z. 24 und Z. 62 ff.). Hierbei
      handelt es sich um eine Sendeunterbrechung, um einen zeitlichen Versatz für
      den Empfang der Datenteile zu erreichen (Sp. 4 Z. 32). Die Dauer bzw. Länge
      des neuen Rahmens ergibt sich aus der Addition der Längen der Präambel (TPA),
      der Schutzzeit (TG) und des Datenteils (Sp. 7 Z. 53 f.).

139          Problematisch sei diese Lösung, wenn ein kurzes Schutzintervall generiert
      werde, insbesondere dann, wenn die Zeit, die zum Ein- und Ausschalten des
      Leistungsverstärkers der Mobilstation benötigt werde, in der gleichen Größenordnung liege wie das Schutzintervall (Sp. 4 Z. 44 f.).

                                             - 33 -



140          Zur Verbesserung schlägt K13 vor, die Übertragungsleistung des Senders
      nicht zu unterbrechen oder herunterzufahren, sondern Füllsymbole ohne Änderung der Sendeleistung zu übertragen (Sp. 4 Z. 61-63; Sp. 12 Z. 55). Dies ist in
      der nachfolgend wiedergegebenen Figur 10 dargestellt.




141          Um dies zu erreichen, schlägt K13 beispielhaft vor, dass die Mobilstation
      während der Schutzzeit so genannte dummy chips sendet, die als Füllmaterial
      genutzt werden, die die Basisstation nicht detektieren muss (Sp. 5 Z. 1 ff.). Alternativ könne die Mobilstation auch Symbole spreizen und übermitteln, um das
      Schutzintervall in dem Random-Access-Rahmen zu generieren. Solche Signale
      könnten erforderlichenfalls in der Basisstation detektiert und beispielweise als
      Pilotsignale für die Kanalschätzung verwendet werden (Sp. 5 Z. 5-10, Sp. 13
      Z. 7-15).

142          bb)   Damit sind die Merkmale 13 und 13.1 offenbart.

143          (1)   Die von der Mobilstation in K13 gesendeten Pilotsignale sind SR-Signale im Sinne von Merkmal 13.1, denn sie ermöglichen eine Kanalschätzung.
      Ob sie von der Basisstation für diesen Zweck eingesetzt werden, ist unerheblich,
      weil Patentanspruch 1 diesbezüglich keine Festlegungen enthält.

                                           - 34 -



144          (2)   Die in Figur 10 dargestellte Struktur enthält Teilrahmen im Sinne
      von Merkmal 13.1.

145          Eine Unterteilung der für die Übertragung eingesetzten Rahmen in Teilrahmen ist in K13 zwar nicht erwähnt. Angesichts des Umstands, dass K13 einen
      anderen Mobilfunkstandard betrifft, kann auch nicht davon ausgegangen werden,
      dass die dargestellte Struktur den Rahmen und Teilrahmen eines LTE-Netzwerks
      entspricht. Wie bereits oben dargelegt wurde, lassen sich Merkmal 13.1 aber
      keine näheren Anforderungen an die Struktur eines Teilrahmens entnehmen, weil
      Patentanspruch 13 keine Festlegung auf einen bestimmten Mobilfunkstandard
      enthält.

146          Vor diesem Hintergrund genügt zur Offenbarung von Merkmal 13.1, dass
      in Figur 10 sowohl für die Nutzdaten als auch für die Präambel und das Schutzzeitintervall besondere Teilstrukturen definiert sind. Dabei kann aufgrund der
      letztlich beliebigen Anordnung der Teilstrukturen innerhalb der übergeordneten
      Rahmenstruktur auch das aus Präambel und Schutzbereich bestehende und in
      Figur 10 als N * TTs definierte Zeitintervall als ein Teilrahmen in diesem Sinne
      angesehen werden.

147          cc)   Ebenfalls offenbart sind die Merkmale 13.2 bis 13.4.

148          (1)   Entgegen der Auffassung der Beklagten ist die in Figur 10 dargestellte Schutzzeit ein Schutzzeitintervall im Sinne der Merkmale 13.2 und 13.3.

149          Nach den Feststellungen des Patentgerichts ist in WCDMA-Systemen ein
      Schutzzeitintervall zur Vermeidung von Interferenzen zwar nicht zwingend notwendig, weil eine Präambel stark gespreizt und deshalb weniger anfällig gegen
      schmalbandige Störungen ist. Wie bereits oben dargelegt wurde, ist zur Verwirklichung der Merkmale 13.2 und 13.3 aber nicht erforderlich, dass das Schutzzeitintervall der Vermeidung von Interferenzen dient.

                                            - 35 -



150            Ausreichend ist danach, dass es sich um ein der Random-Access-Präambel zugeordnetes Intervall handelt, in dem keine Signale übertragen werden.
      Diese Voraussetzung ist bei der in Figur 10 dargestellten Struktur erfüllt.

151            (2)   Das zur Kanalschätzung geeignete Pilotsignal wird in diesem
      Schutzzeitintervall abgebildet.

152            Wie beim Streitpatent wird ein Zeitraum, in dem aus bestimmten Gründen
      keine Signale übertragen werden, für die Übertragung eines Signals genutzt, das
      anderen Zwecken dient und der Erreichung des mit dem Schutzzeitintervall angestrebten Ziels nicht diametral entgegensteht.

153            Dies gilt selbst dann, wenn man mit der Beklagten davon ausgeht, dass
      nach Figur 10 Präambel und Schutzzeit nicht Teil derselben Struktur, sondern
      jeweils in separaten Strukturen angeordnet sind. Denn Anspruch 12 der K13 offenbart darüber hinaus auch eine Ausgestaltung, in der die Schutzzeit im
      Präambelteil enthalten ist.

154            2.    Mit dem Verfahren gemäß Patentanspruch 13 ist zugleich eine Mobilstation gemäß Patentanspruch 1 offenbart. Deshalb kann das Streitpatent in
      der erteilten Fassung hinsichtlich beider Ansprüche keinen Bestand haben.

155                  Der mit Hilfsantrag 1 verteidigte Gegenstand ist demgegenüber
      patentfähig.

156            1.    Nach Hilfsantrag 1 sollen die Ansprüche 2 und 5 gestrichen werden.
      Patentanspruch 1 soll folgende zusätzliche Merkmale enthalten:

157    1.1.4     wherein the guard time is added     wobei das Schutzintervall nach
                 after the random access pream-      der Random-Access-Präambel
                 ble,                                hinzugefügt wird und
       1.1.5     and said mapping unit is adapted    die Abbildungseinheit so eingeto map the sounding reference       richtet ist, dass sie das SR-Signal

                                                - 36 -



                 signal in the tail end of the sub-      am Ende des Teilrahmens abbilframe,                                  det,
       1.1.6     and wherein the random access           und wobei die Random-Accesspreamble is transmitted from an-        Präambel von einer anderen Moother mobile station apparatus          bilstationsvorrichtung gesendet
                                                         wird


158            Entsprechende Verfahrensschritte sollen auch in den in dieser Fassung
      als Patentanspruch 11 vorgesehenen Verfahrensanspruch aufgenommen werden.

159            1.     Der damit zulässigerweise verteidigte Gegenstand ist patentfähig.

160            a)     Er ist neu.

161            aa)    In K13 sind die Merkmale 1.1.6 und 11.6 nicht offenbart.

162            Die Random-Access-Präambel und das Pilotsignal werden dort von derselben Mobilstation übertragen.

163            Der von der Klägerin zu 2 in diesem Zusammenhang angeführte Umstand,
      dass die in K13 offenbarte Struktur in einem Netz durch mehrere Mobilstationen
      parallel übertragen werden kann, könnte nur dann zu einer abweichenden Beurteilung führen, wenn das Pilotsignal einer Mobilstation in derselben Struktur übertragen würde wie die Random-Access-Präambel einer anderen Mobilstation. Anhaltspunkte hierfür lassen sich K13 nicht entnehmen.

164            bb)    Der mit Hilfsantrag 1 verteidigte Gegenstand wird auch durch K9
      nicht vollständig vorweggenommen.

165            (1)    K9 befasst sich mit dem möglichen Aufbau einer Random-Access-Präambel, die eine noch nicht im Uplink synchronisierte Mobilstation an die
      Basisstation in einem LTE-Netz übermittelt.

                                           - 37 -



166          Der Beitrag konzentriert sich auf ein TDM/FDM-Schema (Time Division
      Multiplexing, Frequency Division Multiplexing) oder ein reines FDM-Schema und
      die dafür vorgesehenen Kanäle (S. 1 Nr. 1).

167          Eine Random-Access-Präambel werde von der Basisstation zur Erkennung des Direktzugriffsversuchs der Mobilstation und zur Schätzung der Paketumlaufzeit verwendet. Die genaue Gestaltung der Präambel sei noch offen (S. 1
      Nr. 1, S. 1 Nr. 2).

168          Bei der Untersuchung verschiedener Bandbreiten einer Random-Access-Präambel mit Blick auf die optimale Erkennungsleistung durch die Basisstation
      habe sich gezeigt, dass der Präambel eine schmale Bandbreite von maximal
      2,5 MHz zugewiesen werden sollte. Die restliche Frequenzressource könne entweder anderen Random-Access-Präambeln oder - optional bei TDM/FDM - anderen geplanten Daten zugewiesen werden (S. 2 Nr. 2).

169          Allerdings seien bei einer schmalbandigen Präambel weitere Mittel zur
      Schätzung des Kanalfrequenzgangs erforderlich (S. 5 Nr. 4).

170          Hierzu schlägt K9 vor, so genannte Breitbandpiloten (wideband pilot) an
      die Präambel anzuhängen (attached) oder in diese einzubetten (embedded), wie
      dies in der nachfolgend wiedergegebenen Figur 3 dargestellt ist.

                                            - 38 -




171          In der links dargestellten Variante des angehängten Breitbandpiloten übermittelt die Mobilstation ein Signal, das aus den Präambeln a und b, zwei Breitbandpiloten a und b sowie einer Schutzzeit besteht.

172          In der Variante des angehängten Breitbandpiloten sei dessen Interferenz
      mit Präambeln anderer Mobilstationen auf einen überlappenden Bereich, wie in
      Figur 3 gezeigt, begrenzt (S. 4 Nr. 4.1). Hierfür sei ein geringer Overhead erforderlich, während beim eingebetteten Breitbandpiloten kein Overhead anfalle
      (S. 5 Nr. 4.3 Tabelle 3).

173          (2)    Damit sind die Merkmale 1 und 11 offenbart.

174          K9 beschäftigt sich mit der Übertragung von einer Mobil- an eine Basisstation und betrifft damit auch ein Sendeverfahren.

175          (3)    Entgegen der Auffassung der Beklagten sind auch die Merkmale
      1.1.1 und 11.1 offenbart.

                                            - 39 -



176          (a)      Die Beklagte wendet sich im Ausgangspunkt zu Recht nicht gegen
      die Feststellung des Patentgerichts, dass die in K9 offenbarten Pilotsignale a und
      b als SR-Signale anzusehen sind.

177          Die neben der eigentlichen (schmalbandigen) Random-Access-Präambel
      vorgesehenen Pilotsignale enthalten zusätzliche Informationen über die Kanalqualität der beabsichtigten Verbindung im Uplink. Dies entspricht einer möglichen
      Funktion des in den Patentansprüchen 1 und 11 vorgesehenen SR-Signals.

178          (b)      Diese SR-Signale werden nach dem Offenbarungsgehalt der K9 auf
      einem Teilrahmen abgebildet.

179          K9 befasst sich zwar nicht näher mit der Struktur von Rahmen oder Teilrahmen. Aus dem in der Einleitung enthaltenen Hinweis auf den in der Entwicklung befindlichen LTE-Standard ergibt sich aber unmittelbar und eindeutig, dass
      die vorgeschlagene Vorgehensweise innerhalb der Strukturen stattfinden soll, die
      damals für diesen Standard vorgesehen waren.

180          Eine zusätzliche Bestätigung dafür bildet insbesondere die Darstellung in
      Figur 3. Der dort verwendete Begriff "RACH burst" knüpft, wie die Klägerinnen
      unwidersprochen und überzeugend vorgetragen haben, an den Begriff des Random-Access-Burst an, der etwa in der in K9 in Bezug genommenen K11 verwendet wird.

181          In der damit schon im Rahmen der Neuheitsprüfung ergänzend heranzuziehenden K11 ist vorgesehen, einen Random-Access-Burst in einem Teilrahmen zu übermitteln (S. 66). Mehr ist für die Offenbarung von Merkmal 11.1 nicht
      erforderlich.

                                            - 40 -



182          (4)    Ob die Merkmale 1.1.2 und 11.2 und 1.1.6 und 11.6 vollständig offenbart sind, bedarf im Streitfall keiner Entscheidung. K9 offenbart jedenfalls
      nicht, die Pilotsignale a und b im Schutzzeitintervall am Ende eines Teilrahmens
      abzubilden, wie dies nach den Merkmalen 1.1.5 und 11.5 vorgesehen ist.

183          (a)    Unter der von den Klägerinnen postulierten Prämisse, dass das in
      Figur 3 als "RACH burst duration" Signal stets eine feste Länge aufweist, kann
      das in Figur 3 nach dem angehängten Breitbandpiloten a vorgesehene Zeitintervall allerdings als übertragungsfreie Zeitspanne im Sinne des Streitpatents angesehen werden.

184          Kommt die Präambel b rechtzeitig an, bleibt dieser Bereich bei einer festen
      Länge der "RACH burst duration" im Ergebnis übertragungsfrei. Bei einer verspäteten Übertragung der Präambel b wird dieser Bereich hingegen zumindest teilweise für den dieser Präambel zugeordneten Breitbandpiloten genutzt.

185          Dies entspricht der Anordnung eines SR-Signals in einer Schutzzeit nach
      den Merkmalen 1.1.2 und 11.2.

186          (b)    Auch unter dieser Prämisse fehlt es jedoch an einer Anordnung des
      Piloten b am Ende eines Teilrahmens, wie dies Merkmal 1.1.5 vorsieht.

187          Am Ende eines Teilrahmens steht nach der Darstellung in Figur 3 nicht ein
      Breitbandpilot, sondern ein (weiteres) Schutzintervall.

188          cc)    Der Gegenstand von Hilfsantrag 1 wird auch durch eine Zusammenschau der Dokumente K18, NK17/K19 und K20 nicht vorweggenommen.

189          Dabei kann offenbleiben, ob ein Fachmann diese drei Dokumente, wie die
      Klägerin zu 2 geltend macht, als eine gemeinsame Veröffentlichung in den Blick
      nehmen würde. Auch unter dieser Prämisse sind die Merkmale 1.1.2 und 11.2
      nicht offenbart.

                                           - 41 -



190         (1)    K18 befasst sich mit der Struktur einer synchronisierten Random-Access-Präambel (SRA) für LTE.

191         Die synchronisierte Random-Access-Präambel werde von einer Mobilstation gesendet, die bereits im Uplink synchronisiert sei, aber noch keine Übertragungsressourcen zugewiesen bekommen habe (S. 1 Nr. 2).

192         In K18 wird für solche Fälle unter anderem die Übersendung eines SRA-Bursts durch die Mobilstation mit einer Struktur vorgeschlagen, die in der nachfolgend wiedergegebenen Figur 1 dargestellt ist.




193         Das Signal besteht aus einem Cyclic Prefix (CP), der eigentlichen Präambelsequenz, einem weiteren Cyclic Prefix und einem Breitbandpiloten. Der Slot,
      in dem das Signal übertragen wird, besteht aus vier Frequenzblöcken. Der erste
      Cyclic Prefix und die Präambel belegen nur einen dieser Frequenzblöcke. In den
      verbleibenden Blöcken können weitere synchronisierte Random-Access-Präambeln übertragen werden. Der zweite Cyclic Prefix und der Breitbandpilot belegen
      demgegenüber alle vier Frequenzblöcke. Mit Blick auf ein mögliches Multiplexen
      von verschiedenen Piloten weiterer Präambeln verweist K18 auf andere Dokumente aus dem Stand der Technik (S. 1 Nr. 3).

                                           - 42 -



194         Der Breitbandpilot bietet dem Frequenz-Planer Mittel zur Kanalsondierung
      an. Das Senden und Empfangen des Breitbandpiloten ist daher identisch zum
      Senden und Empfangen des Referenzsignals, das für die Kanalsondierung in
      einem regulären Uplink-Teilrahmen-Kurzblock verwendet wird (S. 3 Nr. 6).

195         K18 befasst sich ferner mit Optimierungsmöglichkeiten für größere Zellen.
      Hierzu wird vorgeschlagen, die Länge der einzelnen SRA-Bursts zu verdoppeln
      und die Anzahl der Frequenzblöcke zu halbieren (S. 5 Nr. 11 mit Figur 4).

196         (2)    K20 ist eine Vorgängerversion von K18.

197         In K18 wird hierzu ausgeführt, die in K20 vorgesehene Struktur habe angepasst werden müssen wegen der Entscheidung des Standardisierungsgremiums, das Übertragungszeitintervall (TTI) auf eine Millisekunde zu erhöhen und
      Änderungen an den zur Verfügung stehenden Trägersymbolen vorzunehmen
      (K18 S. 1 Nr. 1).

198         Zusätzlich zu den Überlegungen in K18 wird in K20 der für LTE vorgesehene Random-Access-Kanal näher betrachtet. Dies sei ein konfliktbasierter Kanal, der mit geplanten Daten in einem TDM/FDM-Verfahren gemultiplext werde.
      Er sei während Random-Access-Slots mit einer Dauer tra und einer Periode Tra
      verfügbar (K20 S. 1 Nr. 2).

199         Dieser Aufbau ist in der nachfolgend wiedergegebenen Figur 1 der K20 für
      synchronisierte Random-Access-Slots dargestellt.




200         Um den Aufwand für die Zusatzdaten (Overhead) im Vergleich zu den geplanten (Nutz-)Daten zu verringern, schlägt K20 vor, dass synchrone und nicht

                                             - 43 -



      synchrone Random-Access-Slots zusammengeführt (merged) werden könnten.
      Innerhalb eines Slots könne die Bandbreitenressource zwischen synchronen und
      asynchronen Random-Access-Präambeln proportional zu ihrer relativ erwarteten
      Last geteilt werden (S. 1 Nr. 2).

201          (3)    NK17/K19, der im Streitpatent als Stand der Technik benannt ist
      (Abs. 6), befasst sich demgegenüber mit einer verbesserten Struktur einer nichtsynchronen Random-Access-Präambel (NSRA), die eine nicht im Uplink synchronisierte Mobilstation an die Basisstation für einen Erstzugriff auf das Netzwerk übermittelt.

202          Ein solcher NSRA-Burst bestehe nach den bisherigen Überlegungen aus
      einem Cyclic Prefix (CP), der eigentlichen Präambel und einer Schutzzeit (GT),
      um den NSRA-Slot von vorherigen und kommenden im Uplink synchronisierten
      Teilrahmen zu isolieren (S. 1 Nr. 2). Ein solcher Aufbau ist in der nachfolgend
      wiedergegebenen Figur 1 dargestellt.




203          Auf dieser Grundlage schlägt K19 geringfügige Änderungen bezüglich der
      Dauer des Cyclic Prefix und der Schutzzeit vor (vgl. Figur 4).

204          (4)    Damit sind die Merkmale 1 und 11 offenbart.

205          Alle Beiträge befassen sich mit der Übermittlung von Random-Access-Präambeln von einer Mobilstation an eine Basisstation und betreffen damit ein
      Sendeverfahren.

                                            - 44 -



206           (5)   Ob auch die Merkmale 1.1.1 und 11.1 offenbart sind, bedarf keiner
      abschließenden Entscheidung. Jedenfalls fehlt es an einer Offenbarung der
      Merkmale 1.1.2 und 11.2.

207           (a)   Ein Schutzzeitintervall ist nur in NK17/K19 offenbart, nicht aber in
      K18 und K20.

208           Dies ist folgerichtig, weil K18 und K20 sich mit bereits synchronisierten
      Mobilstationen befassen, bei denen ein Schutzzeitintervall zu dem in der
      Beschreibung des Streitpatents angeführten Zweck nicht erforderlich ist.

209           (b)   Entgegen der Auffassung der Klägerin zu 2 ergibt sich aus den in
      K18 enthaltenen Ausführungen zum Aufbau der Präambel-Sequenz kein Hinweis
      auf ein Schutzzeitintervall.

210           In K18 wird ausgeführt, die dort vorgeschlagene Präambelsequenz sei
      nach den bisherigen Überlegungen der Standardisierungsgremien auch für die
      nicht synchronisierte Random-Access-Präambel vorgesehen (Nr. 4).

211           Diese Ausführungen beziehen sich nur auf die eigentliche Präambel. Sie
      lassen nicht erkennen, dass die Strukturen einer nicht synchronisierten Präambel
      auch bezüglich anderer Aspekte übernommen werden sollen.

212           (c)   Entgegen der Auffassung der Klägerin zu 2 ergibt sich aus dem in
      K20 enthaltenen Vorschlag, synchronisierte und nicht synchronisierte Random-Access-Präambeln zusammenzuführen, kein weitergehender Offenbarungsgehalt.

213           In K20 wird nicht näher dargelegt, in welcher Weise die vorgeschlagene
      Zusammenführung erfolgen soll. Deshalb kann nicht davon ausgegangen werden, dass die unterschiedlichen Präambeln so kombiniert werden, dass der in
      K18 und K20 offenbarte Breitbandpilot im Schutzzeitintervall der in NK17/K19
      offenbarten Präambel angeordnet wird.

                                           - 45 -



214         b)     Der mit Hilfsantrag 1 verteidigte Gegenstand war durch den Stand
      der Technik auch nicht nahegelegt.

215         aa)    Ausgehend von K13 ergab sich hierfür keine Anregung.

216         Zumindest in NK9/K7, NK18, NK17/K19 und NK20 sowie möglicherweise
      auch in K9 werden eine Random-Access-Präambel und der Breitbandpilot zwar
      von unterschiedlichen Mobilstationen gesendet. Die Kombination einer dieser
      Entgegenhaltungen mit K13 lag, wie das Patentgericht zutreffend ausgeführt hat,
      aber nicht nahe, weil K13 andere technische Ausgangsbedingungen im Blick hat.
      Im Gegensatz zu LTE sind in WCDMA durch das starke Spreizen der Signale
      gerade keine durch schmalbandige Signale bedingte Störungen zu erwarten.

217         bb)    Auch ausgehend von NK9/K7 ergab sich aus dem allgemeinen
      Fachwissen kein Anlass, die dort offenbarte Lehre in Richtung des Gegenstandes der Patentansprüche 1 und 11 gemäß Hilfsantrag 1 fortzuentwickeln.

218         Aus NK9/K7 ergibt sich insbesondere kein Hinweis, die im Stand der Technik auch für die TDD-Rahmenstruktur besonders normierte Übertragung einer
      Random-Access-Präambel einer nicht synchronisierten Mobilstation durch Spezialfelder (Typ 2) oder durch einen vollständig ausgenutzten Teilrahmen (Typ 1)
      zu ändern und das übertragungsfreie Schutzintervall dennoch für die Übertragung eines SR-Signals vorzusehen.

219         cc)    Aus der insoweit durch die Klägerinnen zusätzlich geltend gemachten Kombination von NK9/K7 mit NK19/K8 oder dem technischen Report 3GPP
      TR 25.814 V7.1.0 (2006-09) (NK23) lässt sich keine Anregung entnehmen, eine
      Mobilstation so auszugestalten, dass diese die im Stand der Technik übertragungsfreie Schutzzeit eines Teilrahmens für eine Random-Access-Präambel
      dennoch zur Übertragung eines SR-Signals nutzen kann.

                                           - 46 -



220         dd)    Dies gilt auch mit Blick auf das von der Klägerin zu 2 besonders
      hervorgehobene Dokument NK23.

221         (1)    In NK23 ist die Problematik, dass bei der Übersendung eines Random-Access-Burst einer nicht synchronisierten Mobilstation Interferenzen mit der
      Datenübertragung anderer Mobilstationen auftreten können, ausdrücklich angesprochen (S. 82 Abs. 9.1.2.1.1.1). Dementsprechend wird auch die Funktion der
      Schutzzeit eines Random-Access-Burst hervorgehoben, nämlich die Vermeidung
      von Ungewissheiten beim Uplink-Timing (S. 83 Abs. 9.1.2.1.1.1). Hierzu stünde
      es in Widerspruch, in diesem Zeitraum dennoch Signale zu übertragen.

222         (2)    Gegenteiliges ergibt sich entgegen der Auffassung der Klägerin
      zu 2 nicht aus der nachfolgend wiedergegebenen Figur 9.1.2.1.1.1.-1.

                                             - 47 -



223         Dieser Figur ist zu entnehmen, dass das rot gekennzeichnete Schutzzeitintervall nach der Random-Access-Präambel (TRA) vor Beginn des nächsten Teilrahmens freizuhalten ist. Dies entspricht der oben wiedergegebenen Erläuterung
      in NK23. Die mit der Abkürzung BW RA und einem senkrechten Doppelpfeil gekennzeichneten Einheiten beschreiben die Bandbreite, mit der die Präambel
      übertragen wird (S. 82 letzter Absatz).

224         Aus dem Umstand, dass nach Figur 1 die mit Pfeilen gekennzeichneten
      weiteren Frequenzressourcen zur Übertragung anderer Random-Access-Kanäle
      oder für Datenübertragungen verwendet werden können, ergibt sich entgegen
      der Auffassung der Klägerin zu 2 ebenfalls nicht die Anregung, das der Random-Access-Präambel angehängte Schutzintervall zur Datenübertragung zu nutzen.
      Der Hinweis auf die Möglichkeit zur Übertragung weiterer Kanäle oder Daten bezieht sich gerade nicht auf die Frequenzressource, die für die Random-Access-Präambel genutzt wird.

225         ee)     Der Gegenstand von Hilfsantrag 1 war auch ausgehend von K9
      nicht nahegelegt.

226         Insoweit ist keine Anregung ersichtlich, den Gegenstand von K9 im Sinne
      des Gegenstandes von Hilfsantrag 1 fortzuentwickeln. Vielmehr wird in K9 der
      als Schutzzeit vorgesehene Bereich am Ende des Teilrahmes gerade freigehalten. In K9 ist allenfalls die Möglichkeit offenbart, eine vorgelagerte übertragungsfreie Zeitspanne eines Teilrahmens einer verspätet gesendeten Random-Access-Präambel zur Verfügung zu stellen, wodurch sich der Breitbandpilot in diese
      verschieben kann.

227         Ausgehend davon ergibt sich keine Anregung, gerade den für die Vermeidung von Interferenzen mit den Daten des nächsten Teilrahmens besonders relevanten Bereich der Schutzzeit am Ende des Teilrahmens für die Anordnung
      eines SR-Signals vorzusehen.

                                           - 48 -



228         ff)    Aus den Dokumenten K18 mit NK17/K19 und K20 ergeben sich
      keine weitergehenden Anregungen.

229         Wie bereits dargelegt wurde, führt eine Zusammenschau der Dokumente
      nicht zur Vorwegnahme des Gegenstandes der Ansprüche 1 und 11. Anregungen, die Lehre dieser Dokumente im Sinne des Streitpatents fortzuentwickeln,
      sind weder dargetan noch sonst ersichtlich.

230         c)     Die weiteren Dokumente liegen weiter ab und führen nicht zu einer
      abweichenden Beurteilung.

                                          - 49 -



231               Die Kostenentscheidung beruht auf § 121 Abs. 2 Satz 2 PatG sowie
      § 92 Abs. 1 und § 100 Abs. 1 ZPO.


      Bacher                              Hoffmann                       Deichfuß


                     Kober-Dehm                         Crummenerl




      Vorinstanz:
      Bundespatentgericht, Entscheidung vom 12.12.2019 - 5 Ni 42/16 (EP) -
