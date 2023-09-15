---
ecli: "ECLI:DE:BPatG:2023:150923U4Ni54.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 54/22"
decided: "2023-09-15"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=25&nr=43867&anz=529&pos=376&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-09-15_4_Ni_54_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 54/22 vom 2023-09-15

## Entscheidung

BUNDESPATENTGERICHT
                      IM NAMEN DES VOLKES

                                URTEIL
                                                           Verkündet am
                                                       15. September 2023
                                                               …


    4 Ni 54/22 (EP)

    (Aktenzeichen)



                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:150923U4Ni54.22EP.0

                                             -2-




                    betreffend das europäische Patent 2 127 420

                                 (DE 60 2008 039 121)




hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 15. September 2023 durch den Vorsitzenden Richter Voit, die
Richterin Werner M.A. sowie die Richter Dipl.-Ing. Altvater, Dipl.-Phys. Univ. Dr.
Haupt und Dipl.-Ing. Tischler


für Recht erkannt:

I.     Das europäische Patent 2 127 420 wird mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland teilweise für nichtig erklärt, soweit
       es über folgende Fassung hinausgeht:

     1. A method (500) for controlling discontinuous reception, DRX, in a wireless
       transmit/receive unit, WTRU, (110) the method characterized by comprising:
           receiving DRX configuration parameters from an eNodeB, eNB,
           (120), wherein the DRX configuration parameters comprise
                 a first DRX cycle length,
                 a second DRX cycle length, and
                 a value for a second WTRU timer used for implicitly transitioning the WTRU between DRX cycle lengths;
           operating (502) the WTRU at the first DRX cycle length;
           using a first WTRU timer to trigger a transition to the second DRX
           cycle length;
           operating (508) the WTRU at the second DRX cycle length,
                 wherein the first DRX cycle length is a multiple of the second
                 DRX cycle length;
           setting the second WTRU timer upon beginning operation at the second DRX cycle length;

                                              -3-



             determining that the second WTRU timer has expired; and
             responsive to determining that the second WTRU timer has expired,
             transitioning (512) to the first DRX cycle length without receiving explicit signaling from the eNB.

       9. A wireless transmit receive unit, WTRU, (110), characterized by a processor (215) being configured to:
             receive discontinuous reception, DRX, configuration parameters from
             an eNodeB, eNB, (120), wherein the DRX configuration parameters
             comprise
                  a first DRX cycle length,
                  a second DRX cycle length, and
                  a value for a second WTRU timer used for implicitly transitioning the WTRU between DRX cycle lengths; and
             operate (502) the WTRU at the first DRX cycle length;
             use a first WTRU timer to trigger a transition to the second DRX cycle
             length;
             operate (508) the WTRU at the second DRX cycle length,
                  wherein the first DRX cycle length is a multiple of the second
                  DRX cycle length;
             set the second WTRU timer upon beginning operation at the second
             DRX cycle length;
             determine that the second WTRU timer has expired; and
             responsive to determining that the second WTRU timer has expired,
             transition (512) the WTRU to the first DRX cycle length without receiving explicit signaling from the eNB (120).



II.      Im Übrigen wird die Klage abgewiesen.



III.     Von den Kosten des Rechtsstreits tragen die Klägerin 70 % und die
         Beklagte 30 %.



IV.      Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils
         zu vollstreckenden Betrages vorläufig vollstreckbar.

                                         -4-




                                   Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 2 127 420 (Streitpatent), das
unter Inanspruchnahme der Priorität der US-amerikanischen Voranmeldung
US 887276 P vom 30. Januar 2007 am 30. Januar 2008 als PCT/US2008/001344
(Offenlegungsschrift WO 2008/094681 A1 = Anlage MN2) angemeldet worden ist.
Die Erteilung des europäischen Patents ist am 22. Juli 2015 veröffentlicht worden.
Das in englischer Sprache gefasste Streitpatent ist in Kraft.


Das Deutsche Patent- und Markenamt führt das Streitpatent unter dem Aktenzeichen 60 2008 039 121. Es trägt die Bezeichnung

         “IMPLICIT DRX CYCLE LENGTH ADJUSTMENT CONTROL IN
                               LTE_ACTIVE MODE”
                           in der deutschen Übersetzung
 „Implizite DRX-Zyklus-Längenanpassungssteuerung in einem LTE-Aktivmodus“.

Das Streitpatent umfasst in der erteilten Fassung zwölf Patentansprüche, die die
Klägerin mit ihrer Nichtigkeitsklage vom 6. Mai 2022 in Umfang der Ansprüche
1 und 9 angreift. Dabei sind der das Verfahren zum Steuern eines diskontinuierlichen
Empfangs (DRX) betreffende unabhängige Patentanspruch 1 und der die Drahtlos-Sende- und Empfangseinheit betreffende Patentanspruch 9 nebengeordnet.


Der das Verfahren betreffende Patentanspruch 1 lautet in der erteilten Fassung:

    1. A method (500) for controlling discontinuous reception, DRX, in
        a wireless transmit/receive unit, WTRU, (110) the method characterized by comprising:

           receiving DRX conﬁguration parameters from an eNodeB,
           eNB, (120), wherein the DRX configuration parameters comprise a first DRX cycle length, a second DRX cycle length, and
           a value for a WTRU timer used for implicitly transitioning the
           WTRU between DRX cycle lengths;

                                        -5-



          operating (502) the WTRU at the first DRX cycle length;
          operating (508) the WTRU at the second DRX cycle length,
          wherein the first DRX cycle length is a multiple of the second
          DRX cycle length;
          setting the WTRU timer upon beginning operation at the second DRX cycle length;
          determining that the WTRU timer has expired; and
          responsive to determining that the WTRU timer has expired,
          transitioning (512) to the first DRX cycle length without receiving explicit signaling from the eNB.

Der die Drahtlos-Sende-/Empfangseinheit betreffende Patentanspruch 9 lautet in
der erteilten Fassung:

    9. A wireless transmit receive unit, WTRU, (110), characterized by
        a processor (215) being configured to:

          receive discontinuous reception, DRX, conﬁguration parameters from an eNode B, eNB, (1020) [sic!] , wherein the DRX
          configuration parameters compﬁrse [sic!] a ﬁrst DRX cycle
          length, a second DRX cycle length, and a value for a WTRU
          timer used for implicitly transitioning the WTRU between DRX
          cycle lengths; and
          operate (502) the WTRU at the first DRX cycle length;
          operate (508) the WTRU at the second DRX cycle length,
          wherein the ﬁrst DRX cycle length is a multiple of the second
          DRX cycle length;
          set the WTRU timer upon beginning operation at the second
          DRX cycle length;
          determine that the WTRU timer has expired; and
          responsive to determining that the WTRU timer has expired,
          transition (512) the WTRU to the ﬁrst DRX cycle length without
          receiving explicit signaling from the eNB (120).

                                         -6-



Die Klägerin ist der Ansicht, der Gegenstand gemäß den Patentansprüchen 1 und
9 sei wegen des Nichtigkeitsgrunds der unzulässigen Erweiterung gegenüber den
ursprünglich eingereichten Unterlagen und der mangelnden Patentfähigkeit für nichtig zu erklären. Der Gegenstand nach den Patentansprüchen 1 und 9 sei gegenüber
der Offenbarung der ursprünglich eingereichten und als WO 2008/094681 A1 (Anlage MN2) veröffentlichten Anmeldungsunterlagen unzulässig erweitert und gegenüber dem Stand der Technik bereits nicht neu jedenfalls nicht erfinderisch.


Dabei stützt die Klägerin ihr Vorbringen u. a. auf folgende Entgegenhaltungen:

     D6       Research In Motion Limited, „Supporting Long DRX in LTE_ACTIVE
              for Non-Realtime Traffic”, R2-070101, 3GPP TSG RAN WG2 Meeting #56bis, Sorrent, Italien, 15. – 18. Januar 2007, Seiten 1 bis 3;
     D7       WO 2007/148198 A2, veröffentlicht am 27. Dezember 2007;
     D8       WO 2007/148175 A1, veröffentlicht am 27. Dezember 2007;
     D9       WO 2008/054103 A1, veröffentlicht am 8. Mai 2008;
     D10      LG Electronics, „DRX Scheme“, R2-070265, 3GPP TSG-RAN WG2
              #56bis, Sorrent, Italien, 15. – 19. Januar 2007, Seiten 1 bis 4;
     D11      Nokia, „Active mode DRX details”, R2-063081, 3GPP TSG-RAN
              WG2 Meeting #56, Riga, Lettland, 6. – 10. November 2006, 10
              Seiten;
     D12      Ericsson, „Handover Procedure for DRX Operation in LTE_ACTIVE”,
              R2-070043, 3GPP TSG-RAN WG2 Meeting #56bis, Sorrent, Italien,
              15. – 19. Januar 2007, 4 Seiten;
     D16      NTT DoCoMo, Inc., „Views on DRX/DTX control in LTE“, R2-063397,
              3GPP TSG RAN WG2 #56, Riga, Lettland, 6. – 10. November 2006,
              3 Seiten.


Die Klägerin beantragt,

      das europäische Patent 2 127 420 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der Patentansprüche 1 und 9 für nichtig zu erklären.

                                         -7-



Die Beklagte beantragt,

        die Klage abzuweisen,

hilfsweise, die Klage abzuweisen,

        soweit sie sich auch gegen eine der Fassungen des Streitpatents nach den Hilfsanträgen A.2 bis A.11, bezeichnet als
        „Kategorie A“, und B.1 bis B.11, bezeichnet als „Kategorie B“,
        beide überreicht mit Schriftsatz vom 12. Mai 2023, sowie der
        Hilfsanträge C.1 bis C.11, bezeichnet als „Kategorie C“, und
        D.1 bis D.11, bezeichnet als „Kategorie D“, beide überreicht
        mit Schriftsatz vom 4. September 2023, richtet,

        mit der Maßgabe, dass zunächst die Hilfsanträge der „Kategorie B“ und dann die Hilfsanträge der „Kategorien A, C und
        D“ und innerhalb der Kategorien in der numerischen Reihenfolge geprüft werden sollen und jeweils als geschlossener
        Anspruchssatz gestellt werden.


Wegen des Wortlauts von Hilfsantrag B.1 wird auf den Urteilstenor Bezug genommen. Wegen des Wortlauts der Ansprüche nach den weiteren Hilfsanträgen wird
auf die Akte verwiesen.


Die Beklagte tritt der Argumentation der Klägerin entgegen und ist der Auffassung,
der Gegenstand des Streitpatents beruhe auf den ursprünglich eingereichten Unterlagen, sei gegenüber dem Stand der Technik neu und beruhe auch auf einer
erfinderischen Tätigkeit. Der Gegenstand des Streitpatents sei wenigstens in einer
der verteidigten Fassungen nach den eingereichten Hilfsanträgen schutzfähig.


Die Klägerin tritt auch den Hilfsanträgen entgegen und sieht auch die Gegenstände
der Patentansprüche 1 und 9 in der Fassung der jeweiligen Hilfsanträge als unzulässig erweitert und nicht patentfähig an, insbesondere auch mit den jeweils ergänzenden Merkmalen nicht als neu und nicht erfinderisch.

                                        -8-



Der Senat hat den Parteien einen Hinweis vom 27. März 2023 zugeleitet und hierin
Fristen zur Stellungnahme gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, das Protokoll der mündlichen Verhandlung vom 15. September 2023 sowie den weiteren Akteninhalt Bezug
genommen.




                          Entscheidungsgründe


                                        A.


Die zulässige Klage hat in der Sache nur teilweise Erfolg, und zwar hinsichtlich der
Patentansprüche 1 und 9 der erteilten Fassung des Streitpatents. Denn insoweit ist
jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6
Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 56 EPÜ gegeben.


In der Fassung nach dem Hilfsantrag B.1 erweist sich das Streitpatent hingegen als
schutzfähig, so dass die Klage, soweit sie sich auch gegen diese Fassung richtet,
abzuweisen ist. Auf die Frage, ob das Streitpatent auch in der Fassung nach den
weiteren Hilfsanträgen Bestand hätte, kommt es bei dieser Sachlage nicht mehr an.



I.   Zum Gegenstand der angegriffenen Patentansprüche 1 und 9 des
     Streitpatents (in erteilter Fassung), zur Aufgabe, zum Fachmann und zur
     Auslegung


1.     Das Streitpatent befasst sich mit Verbesserungen des sogenannten diskontinuierlichen Empfangsmodus, kurz DRX-Modus („Discontinuous Reception“, „DRX mode“ bzw. „DRX state“), und einer Drahtlos-Sende-/ Empfangseinheit („Wireless Transmit/Receive Unit“, „WTRU“) innerhalb eines drahtlosen

                                       -9-



Kommunikationssystems, nachfolgend vereinfachend als Mobilfunknetz bezeichnet, nach dem 3GPP Mobilfunkstandard LTE („Long Term Evolution“) (vgl. Streitpatentschrift, Absätze 0002 und 0003).

Bei der Drahtlos-Sende-/Empfangseinheit WTRU kann es sich z. B. um eine Mobilstation oder eine Anwendereinrichtung („user equipment“, UE), d. h. ein Endgerät,
handeln (Absatz 0013).

In einem LTE-Mobilfunknetz kann eine WTRU in unterschiedlichen Betriebsmodi
arbeiten, u. a. in einem sogenannten LTE_ACTIVE-Modus. In diesem LTE_AC-TIVE-Modus kann eine WTRU im DRX-Modus betrieben werden, der es der WTRU
ermöglicht, für eine vorbestimmte Zeit in einem Stromsparmodus („low power
mode“) – auch als Schlafmodus („sleep mode“) bezeichnet – zu arbeiten und dann
für eine andere vorbestimmte Zeit in einen Volllastmodus („full power mode“) – auch
als Wachmodus („awake mode“) bezeichnet – zu wechseln. Dies erlaubt es, den
Batterieverbrauch der WTRU zu reduzieren. Entsprechende DRX-Zykluslängen
werden von dem E-UTRAN Subsystem („Enhanced Universal Terrestrial Radio Access Network“) des Mobilfunknetzes in einer Weise konfiguriert, dass eine LTE-Basisstation („evolved Node B“, eNodeB, eNB) des E-UTRAN Subsystems und die
WTRU auf einen Schlaf- und Wachzyklus synchronisiert sind (Absatz 0003).

Im Idealfall überträgt ein eNodeB immer nur dann Daten an eine WTRU, wenn sich
diese in einem Wachmodus befindet. Sind die WTRU und der eNodeB nicht aufeinander abgestimmt, d. h. nicht im o. g. Sinne synchronisiert, besteht die Gefahr,
dass der eNodeB Daten an die WTRU zu Zeitpunkten übertragen möchte, zu denen
sich die WTRU im Schlafmodus befindet. Diese Daten würde die WTRU dann „verpassen“.

Aufgrund der jeweils aktuellen Verkehrssituation auf der Funkschnittstelle zwischen
der WTRU und dem eNodeB sind häufige Anpassungen der DRX-Zykluslänge notwendig, um Systemleistung, WTRU-Performanz und WTRU-Energieeinsparungen
auszubalancieren. Hierbei bringt die ausschließliche Verwendung von WTRU/E-UTRAN Signalisierungen, um die DRX-Zykluslänge feinzujustieren, eine hohe System- und WTRU-Signalisierungslast mit sich (Absatz 0004).

                                        - 10 -




Implizite, d. h. vordefinierte Regeln für die Anpassung von DRX-Zykluslängen können zu einem DRX-Betrieb mit einem reduzierten Batterieleistungsverbrauch seitens der WTRU führen, ohne hierbei die System- oder WTRU-Performanz zu beeinträchtigen. Implizite Regeln für die Anpassung von DRX-Zykluslängen können
außerdem DRX-Zykluslängenübergänge zwischen der WTRU und dem E-UTRAN
unterstützen, und dadurch erforderliche explizite Signalisierungen zwischen einem
eNodeB und einer WTRU reduzieren (Absatz 0005).


2.    Obwohl im Streitpatent nicht explizit formuliert, liegt dem Streitpatent die Aufgabe zugrunde, ausgehend von den Nachteilen des Standes der Technik, ein verbessertes Verfahren zur Steuerung des diskontinuierlichen Empfangs (DRX) in einer Drahtlos-Sende-/Empfangseinheit (WTRU), sowie eine verbesserte WTRU bereitzustellen (Absatz 0009).

Diese Aufgabe soll mit Hilfe der Gegenstände der erteilten unabhängigen Patentansprüche 1 und 9 gelöst werden.


3.    Maßgeblicher Fachmann für diese Aufgabe ist ein Ingenieur mit einem universitären Abschluss (Diplom oder Master) der Elektrotechnik, Fachrichtung Nachrichtentechnik, der über eine mehrjährige Erfahrung auf dem Gebiet der Entwicklung
von Mobilfunksystemen verfügt und der sich über aktuelle Entwicklungen auf diesem Gebiet, insbesondere im Zusammenhang mit der Luftschnittstelle, auf dem
Laufenden hält. Er ist daher auch mit dem Stand laufender Standardisierungsbemühungen auf diesem Gebiet vertraut und ihm sind die im Rahmen der Standardisierungsprozesse diskutierten Beiträge bekannt.


4.    Die nachfolgenden Ausführungen, die im Übrigen insgesamt auch für den
ebenfalls angegriffenen (letztlich inhaltsgleichen) nebengeordneten Vorrichtungsanspruch 9 gelten, erfolgen anhand der von den Parteien vorgenommenen Merkmalsgliederung des angegriffenen Patentanspruchs 1. Die maßgebliche englische
Fassung ist ebenso wie die deutsche Fassung der Streitpatentschrift entnommen:

                                      - 11 -




         in der Verfahrenssprache Eng- Übersetzung gemäß Streitpatent
         lisch

M1       A method (500) for controlling dis-    Verfahren (500) zum Steuern eicontinuous reception, DRX, in a        nes diskontinuierlichen Empfangs
         wireless transmit/receive unit,        (DRX) in einer Drahtlos-Sende-WTRU, (110) the method charac-         und Empfangseinheit (Wireless
         terized by comprising:                 Transmit/Receive Unit, WTRU)
                                                (110), wobei das Verfahren
                                                dadurch gekennzeichnet ist, dass
                                                es Folgendes umfasst:

M1.1     receiving DRX conﬁguration pa-         Empfangen von DRX-Konﬁguratirameters from an eNodeB, eNB,          onsparametern von einem eNo-
         (120), wherein the DRX configura-      deB (eNB) (120), wobei die DRX-
         tion parameters comprise               Konfigurationsparameter Folgendes umfassen:

M1.1.1   a first DRX cycle length,              eine erste DRX-Zykluslänge,

M1.1.2   a second DRX cycle length, and         eine   zweite   DRX-Zykluslänge,
                                                und

M1.1.3   a value for a WTRU timer used for einen Wert für einen WTRU-Tiimplicitly transitioning the WTRU mer, der zum impliziten Wechseln
         between DRX cycle lengths;        der WTRU zwischen DRX-Zykluslängen verwendet wird;

M1.2     operating (502) the WTRU at the Betreiben (502) der WTRU bei der
         first DRX cycle length;         ersten DRX-Zykluslänge;

M1.3     operating (508) the WTRU at the        Betreiben (508) der WTRU bei der
         second DRX cycle length, wherein       zweiten DRX-Zykluslänge, wobei
         the first DRX cycle length is a mul-   die erste DRX-Zykluslänge ein
         tiple of the second DRX cycle          Vielfaches der zweiten DRX-Zyklength;                                luslänge ist;

M1.4     setting the WTRU timer upon be- Einstellen des WTRU-Timers am
         ginning operation at the second Beginn des Betriebes auf die
         DRX cycle length;               zweite DRX-Zykluslänge;

M1.5     determining that the WTRU timer Bestimmen, dass der WTRU-Tihas expired; and                mer abgelaufen ist; und

                                         - 12 -




 M1.6       responsive to determining that the     in Reaktion auf das Bestimmen,
            WTRU timer has expired, transi-        dass der WTRU-Timer abgelaufen
            tioning (512) to the first DRX cycle   ist, Wechseln (512) zu der ersten
            length without receiving explicit      DRX-Zykluslänge ohne Empfansignaling from the eNB.                gen einer expliziten Zeichengabe
                                                   von dem eNB.



5.      Zur Auslegung der angegriffenen Patentansprüche 1 und 9

Der Patentanspruch 1 betrifft ein Verfahren zum Steuern eines diskontinuierlichen
Empfangs (DRX) in einer Drahtlos-Sende-/Empfangseinheit („Wireless Transmit/Receive Unit“, WTRU) (Merkmal M1). Als Beispiele einer WTRU nennt das
Streitpatent eine Mobilstation („mobile station“) oder ein Mobiltelefon („cellular telephone“). Bei einer WTRU könne es sich aber auch um ein beliebiges Benutzergerät
(„any other type of user device“) handeln, das in der Lage sei, in einer drahtlosen
Umgebung betrieben zu werden (Absatz 0013).

Mit dem Merkmal M1.1 wird konkretisiert, dass von einem eNodeB (eNB) ausgesendete DRX-Konfigurationsparameter von der WTRU empfangen werden. Mit Hilfe
dieser DRX-Konfigurationsparameter ist es der WTRU möglich, den DRX-Modus zu
modifizieren, d. h. den diskontinuierlichen Empfang (DRX) zu steuern.

Bei einem eNodeB handelt es sich um eine netzwerkseitige Komponente eines E-UTRAN Subsystems eines auf dem LTE-Standard basierenden Mobilfunksystems.

Gemäß den Merkmalen M1.1.1, M1.1.2 und M1.1.3 umfassen die DRX-Konfigurationsparameter eine erste DRX-Zykluslänge, eine zweite DRX-Zykluslänge und einen Wert für einen WTRU-Timer, wobei der WTRU-Timer bzw. dessen Ablauf zum
zum Auslösen des Wechselns (siehe Merkmale M1.4 bis M1.6) zwischen DRX-Zykluslängen verwendet wird.


Aus dem Umstand, dass die DRX-Konfigurationsparameter von einem eNodeB an
eine WTRU übertragen werden, erkennt der Fachmann, dass diese DRX-Konfigurationsparameter ggfs. von dem eNodeB auch verändert werden können, und dass

                                       - 13 -



DRX-Konfigurationsparameter in einer WTRU somit nicht unveränderlich hinterlegt,
d. h. hartcodiert, sind.

Im Gegensatz zu einem Verfahren, bei dem jede Anpassung der DRX-Zykluslängen, d. h. jeder Wechsel zwischen DRX-Zykluslängen, explizit von einem eNodeB
an eine WTRU signalisiert wird, ist es bei dem erfindungsgemäßen Verfahren ausreichend, die DRX-Konfigurationsparameter (Merkmale M1.1.1 bis M1.1.3) lediglich
einmal zu Beginn des DRX-Betriebs zu übertragen, d. h. zu signalisieren – so lange
die einzelnen DRX-Konfigurationsparameter im Laufe des DRX-Betriebs nicht verändert werden, d. h. nur dann erneut zu signalisieren, falls DRX-Konfigurationsparameter im Laufe des DRX-Betriebs zu verändern sind.

Im Streitpatent wird zwischen mehreren DRX-Modi unterschieden. In der Beschreibung und in den Figuren der Streitpatentschrift werden diese DRX-Modi mit „DRX
level-1“ bzw. „Level-1“, „DRX level-2“ bzw. „Level-2“, „DRX level-3“ bzw. „Level-3“
und „DRX level-n“ bzw. „Level-n“ bezeichnet, wobei jeder dieser DRX-Modi eine
spezifische DRX-Zykluslänge aufweist (Absätze 0010 und 0020), wobei im Patentanspruch 1 nur zwischen zwei unterschiedliche DRX-Zykluslängen („a first DRX
cycle length, a second DRX cycle length“) unterschieden wird. Die kürzeste DRX-Zykluslänge weist der „Level-1“ auf, der z. B. dazu dient, empfangene Downlink-Befehle sofort auszuführen (Absatz 0023). Der „Level-2“ weist eine kürzere DRX-Zykluslänge als der „Level-3“ auf, womit ein häufigerer Datenaustausch zwischen
der WTRU und dem eNodeB als im „Level-3“ einhergeht (Absatz 0022). Die optionalen „Level-n“ weisen längere DRX-Zykluslängen als der „Level-3“ auf (Absatz 0024). Somit ist jedem DRX-Modus eine individuelle DRX-Zykluslänge zugeordnet, wobei sich die DRX-Zykluslängen der einzelnen DRX-Modi unterscheiden
(Absatz 0020).

Die Zusammenhänge zwischen den im Streitpatent verwendeten Bezeichnungen
der DRX-Modi, der DRX-Zykluslängen und der damit einhergehenden Häufigkeit
eines Datenaustausches zwischen der WTRU und dem eNodeB können wie folgt
skizzenhaft dargestellt werden:

                                          - 14 -




             Vom Senat erstellte Skizze (Anm.: Abszisse nicht maßstabsgetreu)


Gemäß dem Merkmal M1.3 ist die erste DRX-Zykluslänge ein Vielfaches der zweiten DRX-Zykluslänge.

Der Patentanspruch 1 nach Streitpatent fordert nicht explizit, dass die erste DRX-Zykluslänge ein (beliebiges) ganzzahliges Vielfaches der zweiten DRX-Zykluslänge
ist.

In den von der Beklagten in diesem Zusammenhang zitierten Absätzen 0030 bis
0032 der Beschreibung des Streitpatents wird ein nicht beschränkendes Ausführungsbeispiel (Absatz 0030: „may be given“) beschrieben, bei dem ausgehend von
einer kürzest möglichen DRX-Zykluslänge L, sich die erste bzw. zweite DRX-Zykluslänge durch eine Multiplikation dieser DRX-Zykluslänge mit einer Zweier-Potenz
2n ergibt, wobei n = 0, 1, 2, 3, etc.. Dadurch könne die Wahrscheinlichkeit einer
Nicht-Synchronität der DRX-Zyklen eines eNodeB und einer WTRU reduziert werden und eine ggfs. notwendige Neu-Synchronisierung vereinfacht werden. Gemäß
diesem Ausführungsbeispiel können die erste bzw. die zweite DRX-Zykluslänge
z. B. die Längen L, 2L, 4L, 8L, 16L, 32L etc. aufweisen, nicht jedoch z. B. die Längen
3L, 5L, 7L, 9L. Dies berücksichtigend sind durch das in den Absätzen 0030 bis 0032
der Beschreibung des Streitpatents offenbarte Ausführungsbeispiel lediglich einzelne Fälle einer ganzzahligen Vielfachheit der ersten DRX-Zykluslänge im Vergleich zur zweiten DRX-Zykluslänge offenbart.

Auch das in Absatz 0033 angegeben Verhältnis von ursprünglicher und verkürzter
Zykluslänge stellt nur ein nicht beschränkendes Ausführungsbeispiel dar (Absatz
0033: „Typically, …“) und nimmt bezüglich einer Definition des Wertes „n“ als ganzzahligem Wert allenfalls Bezug auf ein weiteres Ausführungsbeispiel (Absatz 0031).

                                         - 15 -




Im Übrigen wird der im Merkmal M1.3 enthaltene mathematische Begriff der „Vielfachheit“ von Naturwissenschaftlern nicht nur im Zusammenhang mit dem Verhältnis ganzer Zahlen verwendet, d. h. im Sinne von „zweifach“, „dreifach“, „vierfach“
etc., sondern auch im Zusammenhang mit dem Verhältnis rationaler oder reeller
Zahlen. Daher wird der Fachmann der Angabe in Merkmal M1.3, wonach „die erste
DRX-Zykluslänge ein Vielfaches der zweiten DRX-Zykluslänge ist“ nicht mehr entnehmen, als dass sich die erste und die zweite DRX-Zykluslänge unterscheiden,
wobei die erste größer als die zweite DRX-Zykluslänge ist.

Im DRX-Modus verwendet die WTRU zu jedem Zeitpunkt für den Datenaustausch
mit einem eNodeB immer nur eine der definierten DRX-Zykluslängen, wobei sowohl
der eNodeB als auch die WTRU bei einem störungsfreien Betrieb zu jedem Zeitpunkt die gleiche DRX-Zykluslänge anwenden (Absatz 0020).

Die in den Merkmalen M1.1.1 und M1.1.2 verwendeten Zusätze „erste“ und
„zweite“ dienen zur Differenzierung von zwei unterschiedlichen DRX-Zykluslängen
und damit einhergehend auch zur Differenzierung von zwei unterschiedlichen DRX-Modi. Mittels dieser beiden Adjektive wird jedoch nicht festgelegt bzw. definiert, welchem der im Streitpatent beschriebenen und dargestellten DRX-Modi („Level-1“,
„Level-2“, „Level-3“, „Level-n“) die erste DRX-Zykluslänge bzw. die zweite DRX-Zykluslänge konkret zugeordnet wird.

Der Gesamtoffenbarung des Streitpatents entnimmt der Fachmann, dass mit der
Bezeichnung „Wert für einen WTRU-Timer“ im Merkmal M1.1.3 ein Zeitwert gemeint
ist. Dieser Zeitwert wird von der WTRU im Sinne eines zeitlichen Grenzwertes verwendet, um zu bestimmen, wann ein WTRU-interner Timer, der von der WTRU gestartet, gestoppt und zurückgesetzt werden kann, diesen Zeitwert erreicht hat.


Der erteilte Patentanspruch 1 lässt offen, ob die drei genannten DRX-Konfigurationsparameter (erste und zweite DRX-Zykluslänge, Wert für WTRU-Timer) gleichzeitig, zum Beispiel innerhalb einer einzigen Nachricht, oder zu verschiedenen Zeitpunkten von der WTRU empfangen werden. Die Parameter müssen jedoch zumindest zur Ausführung der Verfahrensschritte gemäß den Merkmalen M1.4 bis M1.6
in der WTRU vorliegen.

                                        - 16 -




Den Merkmalen M1.2, M1.3 und M1.6 entnimmt der Fachmann, dass die WTRU
sowohl unter Anwendung („at“ bzw. „bei“; „to“ bzw. „zu“) der ersten DRX-Zykluslänge, als auch unter Anwendung der zweiten DRX-Zykluslänge betrieben wird.

Die Merkmale M1.4 bis M1.6 konkretisieren das beanspruchte Verfahren im Hinblick auf den Wechsel von der zweiten DRX-Zykluslänge zu der ersten DRX-Zykluslänge.

Zunächst wird durch das Merkmal M1.4 festgelegt, dass am Beginn des Betriebes
der WTRU unter Anwendung der zweiten DRX-Zykluslänge der WTRU-Timer „eingestellt“ („setting“), d. h. gestartet, wird. Im nächsten Verfahrensschritt gemäß dem
Merkmal M1.5 bestimmt die WTRU, dass der WTRU-Timer abgelaufen ist. In Folge
hiervon, wechselt die WTRU automatisch zu der ersten DRX-Zykluslänge, d. h. die
WTRU wird nach dem Ablauf des WTRU-Timers unter Anwendung der ersten DRX-Zykluslänge betrieben (Teil des Merkmals M1.6). Dadurch, dass dieser Wechsel
des Betriebs der WTRU unter Anwendung der zweiten DRX-Zykluslänge zu einem
Betrieb unter Anwendung der ersten DRX-Zykluslänge lediglich an das Bestimmen
des Ablaufens des WTRU-Timers geknüpft ist, ist bei dem Verfahren gemäß dem
erteilten Patentanspruch 1 für diesen Wechsel keine zusätzliche explizite Signalisierung seitens des eNodeB an die WTRU notwendig (Rest des Merkmals M1.6).
Nach Ablauf des WTRU-Timers geht auch der eNodeB davon aus, dass die WTRU
mit Ablauf des WTRU-Timers zur ersten DRX-Zykluslänge zurückgekehrt ist.

Entgegen der Ansicht der Klägerin lässt der erteilte Patentanspruch 1 nicht offen,
unter Anwendung welcher DRX-Zykluslänge die WTRU betrieben wurde, bevor sie
unter Anwendung der zweiten DRX-Zykluslänge gemäß dem Merkmal M1.3 betrieben wird.

Denn zu allen Ausführungsbeispielen des Streitpatents wird beschrieben, dass sich
die WTRU vor ihrem Betrieb unter Anwendung einer vergleichsweise kürzerer DRX-Zykluslänge (d. h. in einem vergleichsweise schnelleren DRX-Modus) bereits in einem Betrieb unter Anwendung einer vergleichsweise längeren DRX-Zykluslänge
(d. h. in einem vergleichsweise langsameren DRX-Modus) befunden hat:

                                      - 17 -



  -   Absatz 0035 i. V. m. Fig. 4: „The WTRU 402 may enter DRX mode 408 at a
      default level which may be a normal cycle length DRX level 3 (306 of Figure
      3). […] The WTRU 402 may receive another RRC message or IE 412 that
      triggers the WTRU 402 to enter a faster DRX cycle mode (DRX level 1302 of
      Figure 3). The WTRU 402 and the E-UTRAN 404 enter the DRX level 1 (414,
      416 respectively).“;
  -   Absatz 0036 i. V. m. Fig. 5: „At step 502 the WTRU is in normal operating
      mode, or Level-3. […] If the WTRU detects a time out signal or a trigger at
      step 504, at step 508, the WTRU determines if it should move to DRX Level
      1 or DRX level 2.”;
  -   Absatz 0037 i. V. m. Fig. 6: „At step 602, the WTRU is in normal or DRX
      Levelmode. […] However, if, at step 606, the WTRU determines that the
      traffic is above a threshold, at step 610, the WTRU changes mode to a shorter
      DRX cycle.”;
  -   Absatz 0039 i. V. m. Fig. 7: „At step 702, the WTRU is in normal DRX level 3
      state. […]”; Absatz 0040 i. V. m. Fig. 7: „This may invoke, at step 716, an
      implicit DRX transition trigger that causes the WTRU to go to a Level-1 DRX
      state […].”.


Darüber hinaus wird im Streitpatent im Zusammenhang mit allen relevanten Ausführungsbeispielen (Figuren 4 bis 7) beschrieben, dass die WTRU am Ende des
Betriebs unter Anwendung der vergleichsweise kürzeren DRX-Zykluslänge zu jenem DRX-Modus zurückwechselt, in dem sie sich vor dem Betrieb unter Anwendung der vergleichsweise kürzeren DRX-Zykluslänge befunden hat, d. h. zu dem
DRX-Modus unter Anwendung der vergleichsweise längeren DRX-Zykluslänge.

Bei den o. g. Ausführungsbeispielen wird der jeweilige Betrieb unter Anwendung
einer vergleichsweise kürzeren DRX-Zykluslänge immer durch einen Trigger bzw.
ein Ereignis in einem vorausgehenden Betriebszustand ausgelöst und der DRX-Modus, in den zurückgekehrt wird, wird jeweils als „normaler“ DRX-Modus/-Level
bezeichnet („normal cycle length DRX“, „normal operating mode“, „normal DRX level“), was ebenfalls das Verständnis stützt, dass die erste DRX-Zykluslänge auch
dem Ausgangszustand vor dem Betrieb unter Anwendung einer vergleichsweise
kürzeren zweiten DRX-Zykluslänge entspricht.

                                      - 18 -




Hinweise dahingehend, dass die WTRU ihren Betrieb unmittelbar unter Anwendung
der vergleichsweise kürzeren DRX-Zykluslänge beginnt, können dem Streitpatent
dagegen nicht entnommen werden.

Danach versteht der Fachmann das mit dem erteilten Patentanspruch 1 beanspruchte Verfahren dahingehend, dass die WTRU

  -   zunächst unter Anwendung der ersten DRX-Zykluslänge betrieben wird
      (Merkmal M1.2),
  -   daran anschließend unter Anwendung der zweiten DRX-Zykluslänge betrieben wird, die um ein Vielfaches kleiner als die erste DRX-Zykluslänge ist
      (Merkmal M1.3), wobei am Beginn dieses Betriebes unter Anwendung der
      zweiten DRX-Zykluslänge der WTRU-Timer gestartet wird (Merkmal M1.4),
      und
  -   nachdem von der WTRU bestimmt wurde, dass der WTRU-Timer abgelaufen
      ist (Merkmal M1.5), die WTRU wieder unter Anwendung der ursprünglichen
      ersten DRX-Zykluslänge betrieben wird (Merkmal M1.6).

Über die Gründe bzw. Veranlassungen für den Wechsel von einem Betrieb der
WTRU unter Anwendung der ersten DRX-Zykluslänge (Merkmal M1.2) zu einem
Betrieb unter Anwendung der zweiten DRX-Zykluslänge (Merkmal M1.3) können
dem Patentanspruch 1 nach Streitpatent selbst keine Vorgaben entnommen werden. Gemäß den nicht beschränkenden Ausführungsbeispielen des Streitpatents,
kann ein solcher Wechsel

  -   aufgrund einer RRC-Nachricht („RRC message“) oder eines Informationselements („Information Element“, IE) oder Triggers (Figur 4);
  -   aufgrund eines Triggers oder Timers (Figur 5);
  -   aufgrund des Ergebnisses einer Verkehrsvolumenmessung („traffic volume
      measurement“) (Figur 6); oder
  -   aufgrund des Ergebnisses einer Handover-Messung („serving cell measurement“) (Figur 7)
erfolgen.

                                        - 19 -



Der Wechsel von einem Betrieb der WTRU unter Anwendung der ersten DRX-Zykluslänge (Merkmal M1.2) zu einem Betrieb unter Anwendung der zweiten DRX-Zykluslänge (Merkmal M1.3) schließt nicht aus, dass eine Überwachung der ersten
DRX-Zykluslänge parallel zum Betrieb unter Anwendung der zweiten DRX-Zykluslänge weiterläuft, insbesondere um z. Bsp. im Fehlerfall möglichst schnell eine erneute Synchronisation zwischen der WTRU und dem eNodeB wieder herstellen zu
können.

Allerdings folgt aus dem in den Merkmalen M1.1.3 und M1.6 definierten „Wechseln
… zwischen DRX-Zykluslängen“ bzw. „Wechseln … zu der ersten DRX-Zykluslänge“ aus fachmännischer Sicht, dass zu jedem Zeitpunkt ein Betrieb der WTRU
unter Anwendung einer einzigen DRX-Zykluslänge erfolgt, d. h. insbesondere auch
kein temporär paralleler Betrieb und Anwendung mehrerer, unterschiedlich langer
DRX-Zykluslängen. Gegen einen solchen temporär parallelen Betrieb unter Anwendung mehrerer, unterschiedlich langer DRX-Zykluslängen spricht auch das Zustandsdiagramm gemäß der Figur 3 der Streitpatentschrift, bei dem jedem Betriebszustand genau eine bestimmte DRX-Zykluslänge zugeordnet ist.

Das im Patentanspruch 1 nach Streitpatent beschriebene Wechseln zwischen dem
Betrieb der WTRU bei unterschiedlichen DRX-Zykluslängen schließt zeitliche Phasen (d. h. DRX-Pausen) aus, in denen weder die erste DRX-Zykluslänge, noch die
zweite DRX-Zykluslänge angewendet wird.


Die obigen Ausführungen zu den Merkmalen M1 bis M1.6 aus dem Patentanspruch 1 nach Streitpatent gelten sinngemäß in entsprechender Weise auch für die
Merkmale M9 bis M9.6 aus dem Nebenanspruch 9 nach Streitpatent.



                       II. Zur erteilten Fassung (Hauptantrag)


Die zulässige Klage hat in der Sache teilweise Erfolg, und zwar hinsichtlich der erteilten Fassung des Streitpatents. Denn insoweit ist jedenfalls der Nichtigkeitsgrund
der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138
Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54, 56 EPÜ gegeben.

                                        - 20 -



1.    Entgegen der Auffassung der Klägerin gehen die Gegenstände der erteilten
Patentansprüche 1 und 9 nicht über den Inhalt der ursprünglichen Anmeldeunterlagen hinaus.

Soweit die Klägerin die nach ihrer Ansicht vorliegende unzulässige Erweiterung gegenüber    der    Offenbarung     der    ursprünglich    eingereichten    und     als
WO 2008/094681 A1 (Anlage MN2) veröffentlichten Anmeldeunterlagen damit begründet, dass in diesen Anmeldeunterlagen lediglich von einer Rückkehrzeitperiode
(„resume period“) die Rede sei, an deren Ablauf die Rückkehr zu einem ursprünglichen (dritten) DRX-Zustand mit einer größten DRX-Zykluslänge geknüpft sei, und
hierzu auf den abhängigen Patentanspruch 30, sowie die Absätze 0044 und 0046
der Offenlegungsschrift MN2 verweist, teilt der Senat diese Ansicht nicht.

Im Absatz 0044 der Offenlegungsschrift MN2 wird erläutert, dass ein Übergang von
einem DRX-Zustand zu einem anderen DRX-Zustand durch sog. Trigger als Informationselemente („transition trigger IEs“, „transition trigger information elements“)
ausgelöst wird. Entsprechende Trigger werden von einem eNodeB an die entsprechende WTRU übermittelt.

Absatz 0044 in Verbindung mit „Table 2“ der Offenlegungsschrift MN2 beschreibt
verschiedene solcher Trigger und differenziert hierbei, ob der entsprechende Trigger, d. h. das entsprechende Informationselement, grundsätzlich („mandatory“) vom
eNodeB an die WTRU übermittelt wird, oder nicht („optional“). Demnach handelt es
sich beim Trigger „Timer Value“ um ein immer zu übertragendes Informationselement (vgl. Eintrag „MP“ in Spalte „Need“), während der Trigger „resume period“ nicht
grundsätzlich übertragen wird (vgl. Eintrag „CV-Trigger-UP-2“ in Spalte „Need“ als
Verweis auf den optionalen Trigger „Trigger-UP-2“ in der Tabelle 1 (vgl. Eintrag
„OP“ in Spalte „Need“)).

Welcher dieser von einem eNodeB übermittelten Trigger bzw. Informationselemente von der WTRU verwendet wird, hängt vom jeweiligen, in der WTRU und dem
eNodeB implementierten Verfahren ab. In der Offenlegungsschrift MN2 werden die
einzelnen Verfahren, d. h. Ausführungsbeispiele, im Anschluss an den Absatz 0044
und die Tabelle 2 beschrieben.

                                       - 21 -




Bei den Ausführungsbeispielen gemäß den Figuren 5 und 6 wird jeweils eine „resume period“ verwendet, nicht jedoch ein Timer bzw. Timer Value. Hingegen wird
bei dem Ausführungsbeispiel gemäß der Figur 4 – auf das sich der Patentanspruch 1 nach Streitpatent offensichtlich bezieht – als Trigger ein „Timer“ bzw. der
korrespondierende „Timer Value“ verwendet, während eine „resume period“ bei diesem Ausführungsbeispiel keine Rolle spielt.

Daher ist das Berücksichtigen eines Timers bzw. eines Timer Values als Trigger
bzw. als Informationselement gemäß dem Patentanspruch 1 nach Streitpatent insbesondere im Zusammenhang mit dem Ausführungsbeispiel gemäß der Figur 4 der
Anmeldeunterlagen offenbart.

Eine unzulässige Erweiterung gegenüber der Offenbarung der ursprünglich eingereichten und als WO 2008/094681 A1 (Anlage MN2) veröffentlichten Anmeldeunterlagen liegt somit nicht vor.


2.     Unabhängig davon, dass das Streitpatent die Priorität aus der US-amerikanischen Voranmeldung US 887276 P (60/887,276 = Anlage MN3) vom 30. Januar 2007 wirksam in Anspruch nehmen kann, ist der Gegenstand des erteilten Patentanspruchs 1 gegenüber dem aus der Druckschrift D8 (WO 2007/148175 A1) bekannten Verfahren zum Steuern eines diskontinuierlichen Empfangs (DRX) in einer
Drahtlos-Sende- und Empfangseinheit (Wireless Transmit/Receive Unit, WTRU)
nicht neu und beruht zudem ausgehend von der Lehre der Druckschrift D12 (Ericsson, „Handover Procedure for DRX Operation in LTE_ACTIVE”, R2-070043) unter
Berücksichtigung des Fachwissens des Fachmanns nicht auf einer erfinderischen
Tätigkeit.


2.1    Zur Frage der wirksamen Prioritätsinanspruchnahme

Das Streitpatent nimmt die Priorität seiner US-amerikanischen Voranmeldung
US 887276 P (60/887,276 = Anlage MN3) vom 30. Januar 2007 (materiell) wirksam in Anspruch.

                                     - 22 -



Die nachfolgenden Ausführungen nehmen Bezug auf den Patentanspruch 1 nach
Streitpatent, gelten jedoch in analoger Weise auch für den Nebenanspruch 9 nach
Streitpatent.


2.1.1 Entgegen der Ansicht der Klägerin, stellt das Nichtspezifizieren des LTE-Standards und des LTE_ACTIVE-Modus im Patentanspruch 1 nach Streitpatent
keine erweiternde Verallgemeinerung dar.

Der Senat kann der Klägerin zwar dahingehend zustimmen, dass die in der US-
amerikanischen Voranmeldung thematisierten Probleme, Aufgaben und Lösungen
ausschließlich im Zusammenhang mit einem E-UTRAN Subsystem eines auf dem
LTE-Standard basierenden Mobilfunksystems beschrieben werden (vgl. u. a. Titel
in Absatz 0001: „IMPLICIT DRX CYCLE LENGTH ADJUSTMENT CONTROL IN
LTE_ACTIVE MODE“; Field of Invention in Absatz 0003: „… in an active mode of a
long term evolution (LTE) wireless communication system.“; Zusammenfassung in
Absatz 0010: „The present invention is related to a method and system for managing discontinuous reception (DRX) in LTE_ACTIVE DRX mode operation of a
long term evolution (LTE) compatible wireless communication system.“; Patentanspruch 1: „… in an evolved universal terrestrial radio access network (E-UTRAN) …“).

Gemäß dem Merkmal M1.1 sollen im Rahmen des mit dem Patentanspruch 1 nach
Streitpatent beanspruchten Verfahren DRX-Konfigurationsparameter „von einem
eNodeB (eNB)“ empfangen werden. Dem Fachmann ist selbstverständlich bekannt,
dass es sich bei einem eNodeB um eine Komponente eines E-UTRAN Subsystems
eines auf dem LTE-Standard basierenden Mobilfunksystems handelt.


Ebenso selbstverständlich ist es für den Fachmann, dass sich eine WTRU nicht im
LTE_IDLE-Modus befinden darf, sondern sich im LTE_ACTIVE-Modus befinden
muss, um DRX-Zykluslängen anpassen zu können.

Somit stellt das Nichtspezifizieren des LTE-Standards und des LTE_ACTIVE-Modus im Patentanspruch 1 nach Streitpatent keine erweiternde Verallgemeinerung

                                        - 23 -



dar, die im vorliegenden Fall einer wirksamen Inanspruchnahme der Priorität der
US-amerikanischen Voranmeldung entgegensteht.


2.1.2 Auch die Ansicht der Klägerin, dass der Patentanspruch 1 nach Streitpatent
offen lasse, in welchem DRX-Modus sich die WTRU befand, d. h. mit welcher DRX-Zykluslänge die WTRU betrieben würde, bevor ein Betrieb mit der zweiten DRX-Zykluslänge (Merkmal M1.3) erfolge, und demnach vom Patentanspruch 1 nach
Streitpatent insbesondere umfasst sei, dass die WTRU bereits initial bei einer zweiten DRX-Zykluslänge betrieben werde und im Anschluss daran, d. h. nach Ablauf
des WTRU-Timers (Teil des Merkmals M1.6), erstmalig zu einem Betrieb mit der
längeren ersten DRX-Zykluslänge wechsle, eine solche Lösung jedoch in der US-
amerikanischen Voranmeldung nicht offenbart sei, teilt der Senat nicht.

Der US-amerikanischen Voranmeldung ist zu entnehmen, dass bei dem mit deren
Patentanspruch 1 beanspruchten Verfahren mehrere definierte DRX-Level relevant
sind, wobei gemäß dem Patentanspruch 2 der US-amerikanischen Voranmeldung
jeder DRX-Level eine entsprechende DRX-Zykluslänge aufweist. Die DRX-Level
unterscheiden sich somit in ihrer DRX-Zykluslänge (vgl. Patentanspruch 8 der US-
amerikanischen Voranmeldung). Zwischen diesen DRX-Leveln soll gewechselt werden, wenn ein vordefiniertes Kriterium erfüllt ist (vgl. Patentanspruch 3 der US-amerikanischen Voranmeldung).

Gemäß dem Patentanspruch 24 der US-amerikanischen Voranmeldung wird ein
Rückkehrperioden-Timer („resume period timer“) gestartet, wenn die DRX-Zykluslänge angepasst wurde, d. h., wenn in einen anderen DRX-Level gewechselt wird.
Wenn der Rückkehrperioden-Timer abgelaufen ist, wird die DRX-Zykluslänge auf
ihren ursprünglichen Wert („original value“) zurückgesetzt. Dies ist gleichbedeutend
mit der Aussage, dass mit dem Ablauf des Rückkehrperioden-Timers die DRX-Zykluslänge auf jenen Wert zurückgesetzt wird, den sie vor ihrer Veränderung aufgrund
des vorangegangenen Wechsels des DRX-Levels hatte.

Wie bereits im Zusammenhang mit der Auslegung des Patentanspruchs 1 nach
Streitpatent erläutert, versteht der Fachmann den Patentanspruch 1 unter Berücksichtigung der Gesamtoffenbarung des Streitpatents dahingehend, dass die WTRU

                                      - 24 -



im Rahmen des beanspruchten Verfahrens vor ihrem Betrieb mit einer zweiten
DRX-Zykluslänge bereits mit einer ersten DRX-Zykluslänge betrieben wurde, und
dass die WTRU nach dem Bestimmen, dass der WTRU-Timer abgelaufen ist, zu
dieser ursprünglichen ersten DRX-Zykluslänge zurückwechselt und daran anschließend wieder mit dieser ersten DRX-Zykluslänge betrieben wird.

Dies berücksichtigend versteht der Fachmann die in den Merkmalen M1.1.1
und M1.2 des Patentanspruchs 1 nach Streitpatent erwähnte „erste DRX-Zykluslänge“ als den in der US-amerikanischen Voranmeldung als ursprünglichen Wert
der DRX-Zykluslänge (vgl. Patentanspruch 24: „original value“) bezeichneten Wert,
von dem aus zu der in den Merkmalen M1.1.2 und M1.3 des Patentanspruchs 1
nach Streitpatent erwähnten „zweite[n] DRX-Zykluslänge“ gewechselt wird, und zu
dem gemäß dem Patentanspruch 24 der US-amerikanischen Voranmeldung nach
Ablauf des Rückkehrperioden-Timers („resume period timer“) gemäß den Merkmalen M1.5 und M1.6 des Patentanspruchs 1 nach Streitpatent wieder zurückgewechselt wird.

Im Übrigen wird auch in den Absätzen 0032, 0040 und 0042 der US-amerikanischen
Voranmeldung im Zusammenhang mit den jeweiligen Ausführungsbeispielen erläutert, dass ein Wechsel vom Level-1 – aus fachmännischer Sicht im Sinne des Streitpatents der zweiten DRX-Zykluslänge – zurück zur ursprünglichen bzw. vorhergehenden DRX-Zykluslänge – aus fachmännischer Sicht im Sinne des Streitpatents
der ersten DRX-Zykluslänge – erfolgt, falls ein von einem eNodeB auszusendender
Befehl von der WTRU nicht innerhalb einer „resume period“ empfangen werde, wobei für den Fachmann klar ist, dass zur Feststellung des Ablaufs einer Periode aus
Gründen der einfachen Realisierbarkeit üblicherweise ein Timer verwendet wird.

Dass der Fachmann den Patentanspruch 1 nach Streitpatent dahingehend verstehen würde, dass das mit diesem Patentanspruch 1 beanspruchte Verfahren – wie
von der Klägerin behauptet – nicht mit der in den Merkmalen M1.1.1 und M1.2 erwähnten „erste[n] DRX-Zykluslänge“, sondern direkt mit der „zweite[n] DRX-Zykluslänge“ gemäß den Merkmalen M1.1.2 und M1.3 des Patentanspruchs 1 nach
Streitpatent beginnt, kann der Senat nicht nachvollziehen.

                                       - 25 -



Nach der Ursprungsoffenbarung in der US-amerikanischen Voranmeldung beginnt
das mit dem Patentanspruch 1 nach Streitpatent beanspruchte Verfahren, zunächst
mit einer ersten DRX-Zykluslänge gemäß den Merkmalen M1.1.1 und M1.2 des
Patentanspruchs 1 nach Streitpatent, wechselt dann zu einer zweiten DRX-Zykluslänge gemäß den Merkmalen M1.1.2 und M1.3 und startet dadurch auch einen
DRX-Timer (Merkmal M1.4), um nach Ablauf dieses Timers gemäß den Merkmalen M1.5 und M1.6 des Patentanspruchs 1 nach Streitpatent zu der ursprünglich
verwendeten ersten DRX-Zykluslänge zurück zu wechseln.


2.2 Die Druckschrift D8 (WO 2007/148175 A1) nimmt die Gegenstände der angegriffenen Patentansprüche 1 und 9 nach Streitpatent neuheitsschädlich vorweg.


2.2.1 Bei der Druckschrift D8 handelt es sich um eine am 27. Dezember 2007
veröffentlichte Publikationsschrift, welche auf die internationale Anmeldung
PCT/IB2007/001461 vom 4. Juni 2007 zurückgeht und u. a. die Priorität der US-
amerikanischen Voranmeldung 11/549,761 (= Druckschrift D8a) vom 16. Oktober 2006 in Anspruch nimmt.

Nachdem das Streitpatent, wie zuvor beschrieben, die Priorität der US-amerikanischen Voranmeldung US 887276 P (60/887,276 = Anlage MN3) vom 30. Januar 2007 wirksam in Anspruch nehmen kann, stellt die Druckschrift D8 gegenüber
dem Gegenstand des Streitpatents einen Stand der Technik nach Artikel 54 Abs. 3
EPÜ dar, da die Druckschrift D8 die Priorität ihrer US-amerikanischen Voranmeldung (= Druckschrift D8a) wirksam in Anspruch nimmt. Die Passagen der Druckschrift D8, auf welche nachstehend Bezug genommen wird, finden sich identisch in
der prioritätsbegründenden US-Patentanmeldung D8a.


2.2.2 Die Druckschrift D8 beschäftigt sich mit Verfahren zum Steuern eines diskontinuierlichen Empfangs („discontinuous reception“, DRX) eines Empfangsgerätes
(„receiving device“) innerhalb eines z. Bsp. auf dem UMTS-Standard basierenden
Kommunikationsnetzwerkes („communication network“) (vgl. Bezeichnung; Seite 1,
Zeilen 5 bis 22; Seite 3, Zeilen 25 bis 27). Bei dem in der Figur 1 der Druckschrift
D8 dargestellten Ausführungsbeispiel kommuniziert hierbei ein NodeB 20 als Teil

                                          - 26 -



eines E-UTRAN Subsystems des Kommunikationsnetzwerkes mit einem Endgerät
10 („mobile terminal" oder „user equipment“, UE), und damit mit einer Drahtlos-Sende- und Empfangseinheit WTRU im Sinne des Streitpatents (Merkmal M1)
(Seite 6, Zeilen 17 bis 29).

Von einer DRX-Steuereinheit („DRX control unit“) des NodeB empfängt das Endgerät zunächst eine erste DRX-Zykluslänge als DRX-Konfigurationsparameter eines
regulären DRX-Schemas („regular DRX scheme“) (Merkmale M1.1 und M1.1.1).
Dieses reguläre DRX-Schema kann auch als Default-DRX-Schema dienen (Seite
7, Zeilen 4 bis 10, 21 bis 24; Seite 10, Zeilen 6 bis 11).

Die Druckschrift D8 sieht insbesondere vor, die vom Endgerät angewandte DRX-Zykluslänge gegenüber der beim regulären DRX-Schema angewandten ersten
DRX-Zykluslänge temporär zu verkürzen (Seite 7, Zeilen 21 bis 26; Seite 9, Zeilen
8 und 9). Die hierbei zu verwendenden DRX-Konfigurationsparameter

  -    first control value „DRX(meas)“ und
  -    second control value „DRX(ho)“

empfängt das Endgerät von der DRX-Steuereinheit des NodeB (Merkmal M1.1)
(Seite 5, Zeilen 24 bis 28; Seite 7, Zeilen 15 bis 17; Seite 9, Zeilen 1 bis 6; Seite 10,
Zeilen 21 bis 23).

Bei dem DRX-Konfigurationsparameter DRX(meas) handelt es sich um die gegenüber der beim regulären DRX-Schema angewandten ersten DRX-Zykluslänge verkürzte DRX-Zykluslänge (Seite 4, Zeilen 16 bis 21; Seite 5, Zeilen 24 bis 28; Seite
7, Zeile 31 bis Seite 8, Zeile 3; Seite 8, Zeilen 25 bis 33; Seite 10, Zeilen 21 bis 23),
d. h. um die im Merkmal M1.1.2 definierte zweite DRX-Zykluslänge.

Bei dem DRX-Konfigurationsparameter DRX(ho) handelt es sich um einen Wert für
einen Timer (DRX timer circuit 14) des Endgerätes, der die Dauer („certain specified
time interval or lifetime“, „lifetime of the shortened DRX cycle“) definiert, während
der vom Endgerät die zweite DRX-Zykluslänge angewendet werden soll, bevor das
Endgerät wieder in einen DRX-Betrieb unter Anwendung der ersten, vergleichsweise längeren DRX-Zykluslänge wechselt, und der somit von dem Endgerät zum
impliziten Wechseln zwischen den beiden DRX-Zykluslängen verwendet wird

                                          - 27 -



(Merkmal M1.1.3) (Seite 5, Zeilen 24 bis 28; Seite 7, Zeilen 15 bis 17 und Seite 7,
Zeile 31 bis Seite 8, Zeile 3; Seite 8, Zeilen 31 bis 35; Seite 9, Zeilen 1 bis 6; Seite
10, Zeilen 29 bis 31).

Die durch den DRX-Konfigurationsparameter DRX(ho) definierte Dauer, während
der die zweite DRX-Zykluslänge angewendet wird, kann z. B. als Zeitwert („time“)
oder als Anzahl von Funk(sub)rahmen („frames“, „subframes“) oder als Anzahl von
Wiederholungen von DRX-Zykluslängen („repetitions“) vorgegeben werden (Seite
9, Zeilen 27 bis 31; Seite 10, Zeilen 35 und 36).

Die einzelnen Phasen des in der Druckschrift D8 offenbarten Verfahrens sind in den
Figuren 3 und 4B sowie 4C visualisiert.


Zunächst wird das Endgerät im regulären DRX-Schema betrieben, d. h. unter Anwendung der ersten DRX-Zykluslänge (Merkmal M1.2) (Seite 3, Zeilen 32 und 33;
Seite 10, Zeilen 6 bis 13 i. V. m. Fig. 3: Schritt S101).

Nachdem durch das Endgerät autonom entschieden wurde, dass ein Wechsel des
DRX-Schemas vorzunehmen ist, wird das Endgerät nicht mehr unter Anwendung
der ersten DRX-Zykluslänge betrieben, sondern temporär unter Anwendung der gegenüber der ersten DRX-Zykluslänge verkürzten zweiten DRX-Zykluslänge (Teil
des Merkmals M1.3) (Seite 3, Zeile 35 bis Seite 4, Zeile 2; Seite 4, Zeilen 31 bis
33; Seite 6, Zeilen 31 bis 34, erste Alternative; Seite 10, Zeilen 18 bis 27 i. V. m.
Fig. 3: Schritte S103 bis S105).

Bei dem Ausführungsbeispiel gemäß den Figuren 4A bis 4C beträgt die zweite DRX-Zykluslänge „x msec“ (x Millisekunden), während die erste DRX-Zykluslänge „1 s“
(1 Sekunde) beträgt, d. h. die erste DRX-Zykluslänge ist ein Vielfaches der zweiten
DRX-Zykluslänge (Rest des Merkmals M1.3).

Da mit Hilfe des DRX-Konfigurationsparameters DRX(ho) die Dauer der Anwendung der zweiten DRX-Zykluslänge definiert wird (s. o.), muss der entsprechende
Timer des Endgerätes, d. h. der DRX timer circuit 14, der zur Überwachung dieser
Anwendungsdauer dient, zu Beginn der Phase der Anwendung der zweiten DRX-

                                         - 28 -



Zykluslänge eingestellt, d. h. gestartet, werden (Merkmal M1.4) (Seite 4, Zeilen 11
bis 14; Seite 5, Zeilen 24 bis 26; Seite 9, Zeilen 1 bis 6 und 27 bis 31).

Wenn durch das Endgerät bestimmt wurde, dass dieser Timer des Endgerätes abgelaufen ist (Merkmal M1.5), was gleichbedeutend damit ist, dass dieser Timer den
Wert des DRX-Konfigurationsparameters DRX(ho) erreicht hat, erfolgt automatisch
ein Wechsel zur Anwendung der ersten DRX-Zykluslänge (Seite 6, Zeilen 34 bis 37;
Seite 10, Zeilen 29 bis 31 i. V. m. Fig. 3: Schritt S107). Ein Empfangen einer expliziten Zeichengabe von dem NodeB seitens des Endgerätes ist hierfür nicht notwendig (Merkmal M1.6).

Der Gegenstand des Patentanspruchs 1 nach Streitpatent erweist sich somit nicht
als neu gegenüber dem aus der Druckschrift D8 bekannten Verfahren.

Der Senat teilt im Übrigen die Ansicht der Beklagten nicht, dass im Zusammenhang
mit der ersten und der zweiten DRX-Zykluslänge gemäß der Druckschrift D8 das
Merkmal M1.3 „bei zutreffender Auslegung“ fordere, dass die erste DRX-Zykluslänge ein „ganzzahliges Vielfaches der zweiten Zykluslänge“ sei, wobei die Beklagte
auf die Absätze 0030 bis 0032 der Beschreibung des Streitpatents verweist.

Wie bereits im Zusammenhang mit der Auslegung des Patentanspruchs 1 nach
Streitpatent erläutert, wird im Merkmal M1.3 „ein ganzzahliges“ Vielfaches nicht erwähnt, sondern lediglich „ein Vielfaches“ („a multiple“). Ein „Vielfaches“ ergibt sich
aus der Druckschrift D8 bereits aus der beispielgebend genannten Größenordnung
der Zykluslängen im Ausführungsbeispiel gemäß den Figuren 4A bis 4C, wobei die
zweite DRX-Zykluslänge „x msec“ (x Millisekunden) beträgt, während die erste
DRX-Zykluslänge „1 s“ (1 Sekunde) beträgt, womit die erste DRX-Zykluslänge ein
Vielfaches der zweiten DRX-Zykluslänge ist.

In der Druckschrift D8 wird im Zusammenhang mit dem Verhältnis der zweiten, vergleichsweise kürzeren DRX-Zykluslänge zur ersten, vergleichsweise längeren
DRX-Zykluslänge ausgeführt (Seite 10, Zeilen 33 bis 35): „The shortened DRX cycle
("DRX(meas)") could be defined based on a modulus (MOD) of the regular DRX
interval/cycle or based on a specific number, and the life-time of the Interim DRX
scheme.”). Die Frage, wie der Fachmann die Angabe „based on a modulus (MOD)

                                        - 29 -



of“ versteh, kann dahingestellt bleiben, da bereits aus dem Verhältnis der zweiten,
vergleichsweise kürzeren zur ersten vergleichsweise längeren DRX-Zykluslänge
die Forderung der Vielfachheit gemäß Merkmal M1.3 nach fachmännischer Auslegung erfüllt ist (vgl. Ausführungen im Zusammenhang mit der Auslegung des Patentanspruchs 1) und somit das Merkmal M1.3 in der Druckschrift D8 offenbart ist.

Da der im Merkmal M1.3 enthaltene mathematische Begriff der „Vielfachheit“ nicht
nur im Zusammenhang mit dem Verhältnis ganzer Zahlen verwendet wird (vgl. Ausführungen im Zusammenhang mit der Auslegung des Patentanspruchs 1) ist somit
das Merkmal M1.3 in der Druckschrift D8 offenbart.


2.3    Dem Fachmann waren die Gegenstände der angegriffenen Patentansprüche
1 und 9 nach Streitpatent zudem ausgehend von der Lehre der Druckschrift D12
(R2-070043) und unter Berücksichtigung des Fachwissens des Fachmanns nahegelegt und sie beruhen demnach nicht auf einer erfinderischen Tätigkeit.


2.3.1 Bei der Druckschrift D12 (R2-070043) handelt es sich um einen Diskussionsbeitrag und eine Beschlussvorlage von Ericsson aus dem LTE-Standardisierungsverfahren für das 3GPP TSG-RAN WG2 Meeting #56bis vom 15. bis 19. Januar 2007 in Sorrent, Italien.

Die Druckschrift D12 wurde am 12. Januar 2007 auf den FTP-Server der 3GPP
hochgeladen und dadurch der Öffentlichkeit zugänglich gemacht, d. h. vor dem Anmeldedatum der US-amerikanischen Voranmeldung (30. Januar 2007) des Streitpatents. Zum Nachweis des Zeitpunkts der öffentlichen Zugänglichkeit der Druckschrift D12 hat die Klägerin mit der Nichtigkeitsklage Screenshots des Downloadbereichs des FTP-Servers der 3GPP vorgelegt. Gemäß diesen wurde die Druckschrift D12 am 12. Januar 2007 auf den öffentlichen FTP- Server der 3GPP hochgeladen und somit zum Download öffentlich zur Verfügung gestellt (vgl. Dokument
D6a). Anhaltspunkte, an diesen Veröffentlichungsdaten sowie deren Zugänglichkeit
für die Öffentlichkeit zu zweifeln, bestehen nicht (vgl. auch BGH, Urteil vom 13. Juli
2021 – X ZR 81/19, GRUR 2022, 59 – Diskontinuierliche Funkverbindung; BGH,
Urteil vom 3. Mai 2022 – X ZR 32/20, GRUR 2022, 1200 – Initialisierungsverfahren).

                                      - 30 -



Unabhängig von der Frage der Wirksamkeit der Inanspruchnahme der Priorität der
US-amerikanischen Voranmeldung durch das Streitpatent, stellt die Druckschrift
D12 somit relevanten Stand der Technik gemäß Art. 54 Abs. 2 EPÜ dar.


2.3.2 Der Gegenstand des Patentanspruchs 1 nach Streitpatent ist neu gegenüber
dem aus der Druckschrift D12 bekannten Verfahren.

Die Druckschrift D12 beschäftigt sich mit Verfahren zum Steuern eines diskontinuierlichen Empfangs (DRX) in einem Endgerät („User Equipment“, UE), d. h. in einer
Drahtlos-Sende- und Empfangseinheit (WTRU) (Merkmal M1), das sich im
LTE_ACTIVE-Modus befindet, und berücksichtigt hierbei insbesondere einen
Handover-Fall (vgl. Titel; Kapitel 1). Ein Handover könne durch ein „UE measurement reporting“, d. h. ein Berichten von Messergebnissen des Endgerätes an einen
eNodeB initiiert werden (Kapitel 2.1). Nachdem das Endgerät ein solches „UE measurement reporting“ an den eNodeB übermittelt habe, liege es in der Verantwortung
des eNodeB, einen Antwortbefehl zur Durchführung eines Handovers an das Endgerät zu übermitteln. Problematisch sei in diesem Zusammenhang, dass ein Endgerät, das sich im DRX-Modus befinde, lediglich in periodischen Abständen prüfe,
ob es Befehle von einem eNodeB erhalten habe, was insbesondere bei langen
DRX-Zykluslängen u. U. zu einer verzögerten Ausführung des Handovers führen
könne. Allerdings solle ein Handover, wenn es notwendig sei, möglichst schnell
durchgeführt werden. Dem gegenüber stehe die effiziente Nutzung der Batterieleistung des Endgerätes, die es erfordere, dass das Endgerät nicht permanent die Empfangskanäle hinsichtlich eines Empfangs von Befehlen des eNodeB überwache,
nachdem es ein „UE measurement reporting“ an den eNodeB gesendet habe (Kapitel 2.2, erster Absatz).

Die Druckschrift D12 schlägt daher eine Vorgehensweise vor, um vor dem o. g. Hintergrund sicherzustellen, dass von einem eNodeB ein Befehl zur Durchführung eines Handovers ohne unnötige Verzögerung dem Endgerät kommuniziert werden
könne, wobei die Druckschrift D12 davon ausgeht, dass sich das Endgerät vor der
Durchführung eines Handovers in einem DRX-Modus unter Anwendung einer „nor-

                                       - 31 -



malen“ DRX-Zykluslänge („normal DRX cycle“) befinde, d. h. im Sinne des Patentanspruchs 1 nach Streitpatent unter Anwendung einer ersten DRX-Zykluslänge
(Merkmal M1.2).

Bei der in der Druckschrift D12 vorgeschlagenen Vorgehensweisen wird die DRX-Zykluslänge nach jedem endgeräteseitigen Aussenden eines „UE measurement reporting“ temporär verkürzt (Kapitel 2.2, erster Gliederungspunkt: „DRX cycle adjustment (continuous monitoring or with short DRX) after every measurement report“),
um bei einem Handover eine vergleichsweise geringe Latenzzeit zu gewährleisten
(Kapitel 2.2, erster Absatz). Hierzu unterbricht („interrupts“) das Endgerät die Anwendung der „normalen“, ersten DRX-Zykluslänge nach dem Aussenden des „UE
measurement reporting“ und beginnt mit der Überwachung des entsprechenden
Antwort-Übertragungskanals („scheduling control Channel“) des eNodeB unter Anwendung einer vorkonfigurierten, kürzeren DRX-Zykluslänge, d. h. im Sinne des
Merkmals M1.3 des Patentanspruchs 1 nach Streitpatent unter Anwendung einer
zweiten DRX-Zykluslänge (Kapitel 2.2.1: „… the UE interrupts its DRX activity after
every event triggered measurement report (E1) and starts monitoring the scheduling
control channel … according to a pre-configured shorter DRX cycle.”).

Der Druckschrift D12 können zwar keine Aussagen zu konkreten Längenverhältnissen zwischen der „normalen“, ersten und der kürzeren, zweiten DRX-Zykluslänge
entnommen werden. Da im Patentanspruch 1 nach Streichpatent jedoch nicht definiert ist, dass die „normale“, erste DRX-Zykluslänge ein „ganzzahliges“ Vielfaches
der kürzeren, zweiten DRX-Zykluslänge sein soll, sondern lediglich, dass es sich
bei diesem Längenverhältnis um ein „Vielfaches“ handeln soll, offenbart die Druckschrift D12 aus den bereits im Zusammenhang mit der Druckschrift D8 beschriebenen Gründen (siehe Abschnitt II.2.2.2) auch den entsprechenden Teil („Vielfaches“)
des Merkmals M1.3.

Sollte das Endgerät innerhalb einer bestimmten Zeitdauer keinen Befehl des eNodeB zur Durchführung des Handovers empfangen, kehrt es wieder zur Anwendung
der „normalen“, ersten DRX-Zykluslänge zurück, wobei diese bestimmte Zeitdauer
netzwerkseitig konfiguriert werden kann (Kapitel 2.2: „The UE shall revert to the
normal DRX cycle in case it is not scheduled for certain duration. The duration can

                                         - 32 -



also be configured by the network.”). Für den Fachmann ist es zur Überzeugung
des Senats jedoch selbstverständlich, die o. g. bestimmte Zeitdauer („certain duration“) bzw. deren Ende mittels eines endgeräteseitigen Timers zu überwachen, so
dass der Fachmann die Merkmale M1.4 bis M1.6 des Gegenstands des Patentanspruchs 1 nach Streitpatent mitliest.

Der Druckschrift D12 können keine expliziten Aussagen entnommen werden, wonach die „normale“, erste DRX-Zykluslänge, die kürzere, zweite DRX-Zykluslänge
und die o. g. bestimmte Zeitdauer bzw. ein hierzu korrespondierender Timerwert im
Sinne von DRX-Konfigurationsparametern von dem Endgerät empfangen werden
(Merkmale M1.1 und M1.1.1 bis M1.1.3).

Der Gegenstand des Patentanspruchs 1 nach Streitpatent erweist sich somit als
neu gegenüber dem aus der Druckschrift D12 bekannten Verfahren.


2.3.3 Der Gegenstand des Patentanspruchs 1 nach Streitpatent beruht allerdings
gegenüber der Lehre der Druckschrift D12 nicht auf einer erfinderischen Tätigkeit.

Da die Druckschrift D12 als eines ihrer Ziele die Optimierung der Batterieleistung
des Endgerätes nennt (Kapitel 2.2: „… it is equally important that efficient use of UE
battery, which is one the main motivations of having DRX in LTE_ACTIVE …“), ist
es aus fachmännischer Sicht naheliegend, die zur Einstellung der „normalen“, ersten DRX-Zykluslänge, der kürzeren, zweiten DRX-Zykluslänge und der o. g. bestimmten Zeitdauer („certain duration“) bzw. eines hierzu korrespondierenden Timerwerts notwendigen Parameter dem Endgerät nach Möglichkeit lediglich einmalig zu Beginn des DRX-Betriebs im LTE_ACTIVE-Modus zu signalisieren. Dafür
spricht auch, dass in der Druckschrift D12 selbst explizit erwähnt wird, dass die o. g.
bestimmte Zeitdauer „certain duration“ netzwerkseitig, d. h. seitens des eNodeB,
konfiguriert werden kann (Kapitel 2.2.1: „The UE shall revert to the normal DRX
cycle in case it is not scheduled for certain duration. The duration can also be configured by the network.”).

                                       - 33 -



Somit werden dem Fachmann die Merkmale M1.1 und M1.1.1 bis M1.1.3 des Gegenstands des Patentanspruchs 1 nach Streitpatent ausgehend von der bekannten
Lehre der Druckschrift D12 nahegelegt.




                       III. Zur Fassung nach Hilfsantrag B.1


In der Fassung nach dem Hilfsantrag B.1 erweist sich das Streitpatent als schutzfähig, so dass die Klage, soweit sie sich auch gegen diese Fassung richtet, abzuweisen ist.


1.     Patentanspruch 1 nach Hilfsantrag B.1 entspricht dem erteilten Patentanspruch 1 mit der Maßgabe, dass der Wechsel von dem Betrieb mit der ersten DRX-Zykluslänge zu der zweiten DRX-Zykluslänge unter Verwendung eines ersten
WTRU-Timers („first WTRU timer“) ausgelöst wird. Hierzu ist zwischen den Merkmalen M1.2 und M1.3 das Merkmal M1.7 eingefügt:

           using a first WTRU timer to trigger a transition to the second DRX cycle
           length;


Zur Unterscheidung zwischen dem bereits im erteilten Patentanspruch 1 genannten
„WTRU timer“ und dem mit dem Hilfsantrag B.1 zusätzlich eingeführten „first WTRU
timer“, wird der im erteilten Patentanspruch 1 genannte „WTRU timer“ im Patentanspruch 1 nach Hilfsantrag B.1 als „second WTRU timer“ bezeichnet (betrifft die
Merkmale M1.1.3 und M1.4 bis M1.6).

Analoge Änderungen wurden im nebengeordneten Patentanspruch 9 nach Hilfsantrag B.1 im Vergleich zum erteilten nebengeordneten Patentanspruch 9 vorgenommen.


2.     Entgegen der Ansicht der Klägerin geht der Patentanspruch 1 nach Hilfsantrag B.1 mit dem hinzugefügten Merkmal M1.7 nicht in unzulässiger Weise über die
ursprünglich eingereichten Unterlagen hinaus, lässt auch hinreichend erkennen,

                                         - 34 -



was unter Schutz gestellt werden soll und schränkt den Schutzbereich des erteilten
Patents durch die Spezifizierung mit Merkmal M1.7 ein.

Im Zusammenhang mit der Auslegung des angegriffenen erteilten Patentanspruchs
1 (vgl. Ziffer A.I.5) wurde bereits ausgeführt, dass dem erteilten Patentanspruch 1
selbst keine Vorgaben über die Gründe bzw. Veranlassungen für den Wechsel von
einem Betrieb der WTRU unter Anwendung der ersten DRX-Zykluslänge (Merkmal
M1.2) zu einem Betrieb unter Anwendung der zweiten DRX-Zykluslänge (Merkmal
M1.3) entnommen werden kann.

Gemäß dem Ausführungsbeispiel nach der Figur 5 i. V. m. Absatz 0047 der Beschreibung der als WO 2008/094681 A1 (Anlage MN2) veröffentlichten Anmeldeunterlagen („[…] At step 504, the WTRU checks to see if a timer has timed-out, or a
trigger has been received that would force the WTRU to move to another DRX state.
[…]“) kann ein solcher Wechsel im Verfahrensschritt 504 („[…] OR TIMER“) jedoch
aufgrund eines Timers erfolgen.

Auch im Zusammenhang mit der Beschreibung des Ausführungsbeispiels nach der
Figur 3 wird in den veröffentlichten Anmeldeunterlagen (Anlage MN2) offenbart,
dass ein Timer zur Initiierung eines Wechsels von einem Betrieb der WTRU unter
Anwendung der ersten DRX-Zykluslänge zu einem Betrieb unter Anwendung der
zweiten DRX-Zykluslänge verwendet werden kann (Absatz 0034: „For a WTRU 110
at DRX level 3 306, a timer or counter trigger may be defined to trigger a transition
to DRX level 2 304 […]“; Absatz 0035: „The timer or counter triggers may be used
as transition triggers to bring up the DRX cycle length as well as to bring down the
DRX cycle length as the DRX state changes.“).

Das zusätzlich aufgenommene Merkmal M1.7 geht somit in zulässiger Weise auf
die ursprünglich eingereichten Unterlagen zurück und führt zu einer Einschränkung
des Schutzbereiches gegenüber der erteilten Fassung.

Soweit die Klägerin argumentiert, dass die Gegenstände der Patentansprüche 1
und 9 nach Hilfsantrag B.1 nicht so deutlich offenbart seien, dass ein Fachmann
diese ausführen könne, da offenbleibe,
  a) wie der Wert für den ersten WTRU-Timer erhalten werde,

                                        - 35 -



  b) in welchem Verhältnis, d. h. Zusammenhang, der erste WTRU-Timer zum
       Beginn des Betriebs mit der ersten DRX-Zykluslänge stehe,
  c) wodurch der erste WTRU-Timer eingestellt werde und zu laufen beginne, und
  d) ob mit dem Ablauf des ersten WTRU-Timers tatsächlich notwendigerweise
       ein unmittelbarer Wechsel von der ersten DRX-Zykluslänge zu der zweiten
       DRX-Zykluslänge erfolge,
teilt der Senat diese Sichtweisen der Klägerin nicht.


Zunächst ist festzustellen, dass die von der Klägerin vorgebrachten o. g. Aspekte
a), b) und c) keinen Merkmalen des Verfahrens gemäß Patentanspruch 1 nach Hilfsantrag B.1 entsprechen.

Ungeachtet dessen hat der Fachmann zur Überzeugung des Senats keine Probleme mit der technischen Realisierung eines ersten WTRU-Timers gemäß dem Patentanspruch 1 nach Hilfsantrag B.1.

So könnte der Wert für den ersten WTRU-Timer der WTRU in einer separaten Nachricht von dem eNodeB kommuniziert werden, oder der Wert für den ersten WTRU-Timer könnte im Sinne eines Standard-Wertes bereits bei der Produktion/Initialisierung der WTRU in der WTRU hinterlegt/eingespeichert sein (o. g. Aspekt a)) und
somit der ersten DRX-Zykluslänge zugeordnet wird (o. g. Aspekt b)). Üblicherweise
implementiert der Fachmann den ersten WTRU-Timer derart, dass dieser mit dem
Start des Betriebs unter Anwendung der ersten DRX-Zykluslänge zu laufen beginnt
(o. g. Aspekt c)).

Hinsichtlich des o. g. Aspekts d) liest der Fachmann unter Berücksichtigung der
Gesamtoffenbarung der Anmeldeunterlagen (insbesondere Absatz 0047 i. V. m. Figur 5) mit, dass mit Ablauf des erstens WTRU-Timers die WTRU unmittelbar von
einem „DRX NORMAL STATE“-Betrieb unter Anwendung einer ersten DRX-Zykluslänge zu einem Betrieb unter Anwendung einer zweiten DRX-Zykluslänge wechselt.
Gründe warum dieser Wechsel nicht unmittelbar mit Ablauf des ersten WTRU-Timers, sondern zeitverzögert erfolgen soll, können den Anmeldeunterlagen nicht entnommen werden.

                                        - 36 -



Eine nicht ausführbare Offenbarung aufgrund der Einführung des ersten WTRU-Timers kann der Senat daher nicht feststellen.

Entsprechendes gilt für den Vorrichtungsanspruch 9 nach Hilfsantrag B.1, der dem
Verfahrensanspruch 1 nach Hilfsantrag B.1 inhaltlich im Wesentlichen entspricht.


3.    Das Streitpatent in der Fassung nach Hilfsantrag B.1 erweist sich auch als
patentfähig.


3.1   Die Druckschrift D8 lehrt, dass der Wechsel vom Betrieb mit der ersten,
vergleichsweise langen DRX-Zykluslänge zum Betrieb mit der zweiten, vergleichsweise kurzen DRX-Zykluslänge auf Grundlage des Sendens eines Messberichts
durch das UE, d. h. das Endgerät bzw. die WTRU, stattfindet:
-     Seite 3, Zeile 35 bis Seite 4, Zeile 2: „[…] switching from said regular discontinuous reception cycle to a shorter temporary discontinuous reception cycle
      or switching off said discontinuous reception scheme, in response to an event
      which triggers a reply of said communication network to said receiving device.”
-     Seite 4, Zeilen 31 bis 33: „Additionally, a simple solution to the above problem
      can be provided by having the receiving device enter a pre-determined and
      rather short DRX cycle for a certain time interval after the reply-triggering
      event.”
-     Seite 7, Zeilen 21 bis 24 und 28 bis 31: „According to the preferred embodiment, the DRX cycle (which may as well be designated as "DRX period" or
      "DRX interval") of the DRX timer circuit 14 of the UE 10 can be shortened or
      even stopped when a predetermined event which may trigger a network reply
      occurs. […] When the signalling control unit 16 at the UE 10 has initiated
      transmission of a certain or even any mobility measurement report to the network, e.g., node B 20, the signaling control unit 16 triggers the DRX control
      unit 12 of the UE 10 to apply a shortened DRX cycle or stop using the DRX
      cycle.”
-     Seite 10, Zeilen 18 bis 23, i. V. m. Figur 3: „Accordingly, the signaling control
      unit 16 of the UE 10 initiates transmission of a measurement report to which

                                           - 37 -



          a network reply can be expected and which thus can be regarded as a triggering event for the shortened DRX cycle (step S102). Consequently, the
          signaling control unit 16 triggers the DRX control unit 12 to autonomously set
          the shortened DRX cycle "DRX(meas)" and the associated lifetime "DRX(ho)"
          at the DRX timer circuit 14 (step S103).”


Die Verwendung eines WTRU-Timers, um den Wechsel vom Betrieb mit der ersten,
vergleichsweise langen DRX-Zykluslänge zum Betrieb mit der zweiten, vergleichsweise kurzen DRX-Zykluslänge zu initiieren (Merkmal M1.7), ist der Druckschrift D8
nicht zu entnehmen.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag B.1 ist somit neu gegenüber dem aus der Druckschrift D8 bekannten Verfahren.


Die Frage einer eventuell erfinderischen Tätigkeit im Zusammenhang mit dem Merkmal M1.7 stellt sich bei der Druckschrift D8 nicht, da sie gegenüber dem Gegenstand des Streitpatents einen Stand der Technik nach Artikel 54 Abs. 3 EPÜ darstellt.


Entsprechendes gilt für den Vorrichtungsanspruch 9 nach Hilfsantrag B.1, der dem
Verfahrensanspruch 1 nach Hilfsantrag B.1 inhaltlich im Wesentlichen entspricht.


3.2       Wie aus den Ausführungen zur erteilten Fassung des Patentanspruchs 1
ersichtlich ist, wird bei dem aus der Druckschrift D12 bekannten Verfahren die
DRX-Zykluslänge        nach    jedem    endgeräteseitigen    Aussenden     eines    „UE
measurement reporting“ temporär verkürzt (Kapitel 2.2, erster Spiegelstrich: „DRX
cycle adjustment (continuous monitoring or with short DRX) after every
measurement report“), um bei einem Handover eine vergleichsweise geringe
Latenzzeit zu gewährleisten (Kapitel 2.2, erster Absatz). Hierzu unterbricht
(„interrupts“) das Endgerät die Anwendung der „normalen“, ersten DRX-Zykluslänge
nach dem Aussenden des „UE measurement reporting“ und beginnt mit der
Überwachung des entsprechenden Antwort-Übertragungskanals („scheduling
control Channel“) des eNodeB unter Anwendung einer vorkonfigurierten, kürzeren
DRX-Zykluslänge, d. h. im Sinne des Merkmals M1.3 des Patentanspruchs 1 unter

                                           - 38 -



Anwendung einer zweiten DRX-Zykluslänge (Kapitel 2.2.1: „… the UE interrupts its
DRX activity after every event triggered measurement report (E1) and starts
monitoring the scheduling control channel … according to a pre-configured shorter
DRX cycle.”).

Die Verwendung eines WTRU-Timers, um den Wechsel vom Betrieb mit der ersten,
vergleichsweise   langen    DRX-Zykluslänge         zum   Betrieb   mit   der   zweiten,
vergleichsweise kurzen DRX-Zykluslänge zu initiieren (Merkmal M1.7), ist der
Druckschrift D12 nicht zu entnehmen.

Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag B.1 ist somit neu gegenüber dem aus der Druckschrift D12 bekannten Verfahren.

Ein Timer-basierter Wechsel vom Betrieb mit der ersten, vergleichsweise langen
DRX-Zykluslänge zum Betrieb mit der zweiten, vergleichsweise kurzen DRX-Zykluslänge ist mit dem aus der Druckschrift D12 bekannten Konzept nicht
vereinbar, so dass der Fachmann auch keine Veranlassung hat das aus der
Druckschrift D12 bekannte Verfahren grundlegend abzuändern, um zu einem
Verfahren zu gelangen, das das Merkmal M1.7 des Gegenstands des
Patentanspruchs 1 nach dem Hilfsantrag B.1 aufweist.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag B.1 ist somit gegenüber
dem Stand der Technik nach der Druckschrift D12 nicht nur neu, sondern beruht
auch auf einer erfinderischen Tätigkeit.


Entsprechendes gilt für den Vorrichtungsanspruch 9 nach Hilfsantrag B.1, der dem
Verfahrensanspruch 1 nach Hilfsantrag B.1 inhaltlich im Wesentlichen entspricht.


3.3   Der weitere im Verfahren vorliegende Stand der Technik liegt weiter ab vom
Gegenstand der unabhängigen Patentansprüche 1 und 9 gemäß Hilfsantrag B.1 als
der nach den Druckschriften D8 und D12. Ein Naheliegen der Gegenstände der
Patentansprüche 1 oder 9 nach Hilfsantrag B.1 ist ausgehend von diesen Druckschriften D6, D7, D9 bis D11 und D16 ebenfalls nicht ersichtlich.

                                      - 39 -



3.4      Die Gegenstände der unabhängigen Patentansprüche 1 und 9 gemäß Hilfsantrag B.1 sind somit durch den im Verfahren befindlichen Stand der Technik weder
bekannt noch nahegelegt.




                                       B.
                             Nebenentscheidungen

Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs.1 ZPO.

Dabei hat der Senat berücksichtigt, dass der als schutzfähig verbleibende Patentgegenstand in der beschränkt verteidigten Fassung nach Hilfsantrag B.1 gegenüber
demjenigen der erteilten Fassung durch die Aufnahme eines zweiten „WTRU timers“ in den Patentansprüchen 1 und 9, der nun zur Annahme der patentgemäßen
Lehre nach dem Streitpatent vorliegen muss, trotz weitgehenden Aufrechterhalten
der erteilten patentgemäßen Lehre nicht nur eine geringfügige Einschränkung erfährt.

Diese Einschränkung macht nach der Schätzung des Senats daher 30 % der wirtschaftlichen Verwertbarkeit des von der Klägerin angegriffenen Streitpatents aus.
Demnach hat die Beklagten 30 % der Kosten des Rechtstreits zu tragen, während
der verbleibende Patentgegenstand und damit der, von der Klägerin zu tragende
Anteil mit 70 % zu bewerten ist.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                       C.
                             Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

                                       - 40 -



Die Berufungsschrift, die auch als elektronisches Dokument nach Maßgabe der Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130) eingereicht werden kann, muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder
im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur versehen sein, die von einer internationalen Organisation auf dem Gebiet des
gewerblichen Rechtsschutzes herausgegeben wird und sich zur Bearbeitung durch
das jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils,
gegen das die Berufung gerichtet wird, sowie die Erklärung enthalten, dass gegen
dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils, spätestens aber mit dem
Ablauf von fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die
Berufung vor Fristablauf beim Bundesgerichtshof eingeht.




Voit             Werner            Altvater                Dr. Haupt                Tischler
                                                Zugleich für den wegen Erkrankung an der Unterschriftsleistung
                                                gehinderten RiBPatG Dr. Haupt




                                                        (VRiBPatG Voit)
