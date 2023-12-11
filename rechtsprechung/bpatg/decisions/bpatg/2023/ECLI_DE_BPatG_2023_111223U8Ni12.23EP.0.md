---
ecli: "ECLI:DE:BPatG:2023:111223U8Ni12.23EP.0"
court: "Bundespatentgericht"
spruchkoerper: "8"
aktenzeichen: "8 Ni 12/23"
decided: "2023-12-11"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=34&nr=43896&anz=529&pos=514&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2023-12-11_8_Ni_12_23_EP_0.txt"
cites_law: ["germany/bund/acts/gkg_2004/0063.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patkostg/0002.md", "germany/bund/acts/zpo/0265.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 8 Ni 12/23 vom 2023-12-11

## Entscheidung

beglaubigte Abschrift




                  BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL

8 Ni 12/23 (EP)

(Aktenzeichen)


                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:111223B8Ni12.23EP.0

                                         -2-



                   betreffend das europäische Patent EP 2 667 676
                                (DE 60 2008 054 404)


hat   der    8.     Senat   (Nichtigkeitssenat)   des    Bundespatentgerichts      am
11. Dezember 2023 durch die Vorsitzende Richterin Grote-Bittner sowie die Richter
Dipl.-Ing. Altvater, Dr. Meiser, Dipl.-Phys. Univ. Dr. Haupt und Dipl.-Ing. Tischler
für Recht erkannt:


        I.    Das europäische Patent 2 667 676 wird im Umfang seiner
              Patentansprüche 1, 3, 5, 6, 9 und 10 mit Wirkung für das
              Hoheitsgebiet der Bundesrepublik Deutschland dadurch
              teilweise für nichtig erklärt, dass diese Ansprüche – bei
              Streichung der Ansprüche 5 und 9 – folgende Fassung
              erhalten:


              1.      A mobile station device included in a mobile
              communication system, the mobile station device comprising:
                      a receiver configured to receive, on a physical downlink
              control channel from a base station device, control information
              having a downlink control information format and being
              addressed to the mobile station,

                     wherein the downlink control information format is used
              with a same total number of bits for downlink scheduling and
              an uplink synchronization request,
                    in a case that the downlink control information format is
              used for the downlink scheduling, the control information
              provides a downlink resource assignment,
                      in a case that the downlink control information format is
              used for the uplink synchronization request, a preset value is
              set for a field of the downlink resource assignment, and
              wherein at least one of the following applies:

                           -3-



     (i) in the case that the downlink control information format
is used for the downlink scheduling, the control information
provides no uplink resource assignment; or

       (ii) in the case that the downlink control information
format is used for the uplink synchronization request, the
control information further provides an identification number
specifying a random access preamble; or
       (iii) in the case that the downlink control information
format is used for the uplink synchronization request, the
control information further includes a signature field providing
an identification number specifying a random access
preamble, wherein 6 bits are allocated to the signature field.
3.     A processing method for a mobile station device
included in a mobile communication system, the processing
method comprising:
       receiving, on a physical downlink control channel from
a base station device, control information having a downlink
control information format and being addressed to the mobile
station,
       wherein the downlink control information format is used
with a same total number of bits for downlink scheduling and
an uplink synchronization request,
      in a case that the downlink control information format is
used for the downlink scheduling, the control information
provides a downlink resource assignment,
in a case that the downlink control information format is used
for the uplink synchronization request, a preset value is set for
a field of the downlink resource assignment, and
     wherein at least one of the following applies:
      (i) in the case that the downlink control information
format is used for the downlink scheduling, the control
information provides no uplink resource assignment; or
      (ii) in the case that the downlink control information
format is used for the uplink synchronization request, the

                                   -4-



       control information further provides an identification number
       specifying a random access preamble; or
              (iii) in the case that the downlink control information
       format is used for the uplink synchronization request, the
       control information further includes a signature field providing
       an identification number specifying a random access
       preamble, wherein 6 bits are allocated to the signature field.

       6.    The mobile station according to claim 1, wherein in the
       case that the control information format is used for the uplink
       synchronization request, the control information further
       provides a region on a radio frame available for the random
       access.


       10.    The processing method according to claim 3, wherein
       in the case that the control information format is used for the
       uplink synchronization request, the control information further
       provides a region on a radio frame available for the random
       access.

II.    Von den Kosten des Rechtsstreits tragen die Klägerin 40 %
       und die Beklagte 60 %.


III.   Das Urteil ist wegen der Kosten gegen Sicherheitsleistung in
       Höhe von 120 % des jeweils zu vollstreckenden Betrages
       vorläufig vollstreckbar.


IV.    Der   Streitwert   wird    endgültig   auf   1.250.000,--   Euro
       festgesetzt.

                                            -5-



                                        Tatbestand


Die Teilnichtigkeitsklage richtet sich gegen das u.a. mit Wirkung für die
Bundesrepublik Deutschland erteilte europäische Patent 2 667 676, das auf einer
Teilanmeldung             zur      europäischen    Patentanmeldung      08777144.0
(Stammanmeldung, offengelegt als EP 2 124 362 A1) vom 18. August 2009 beruht,
die ihrerseits auf die internationale Anmeldung PCT/JP2008/060706 (offengelegt
als WO 2008/153078 A1) zurückgeht, am 11. Juni 2008 unter Inanspruchnahme der
Priorität der japanischen Patentanmeldung 2007-155 289 vom 12. Juni 2007
angemeldet und dessen Erteilung am 7. März 2018 veröffentlicht worden ist. Als
Patentinhaberin des beim Deutschen Patent- und Markenamt unter der Nr.
60 2008 054 404 geführten Streitpatents mit der Bezeichnung „Basisstation,
Mobilstation, und Verfahren zur Anforderung von Uplink-Synchronisation“ war zum
Zeitpunkt der Einreichung der Nichtigkeitsklage (8. Januar 2020) die Beklagte
eingetragen, seit 7. Dezember 2021 wird als Patentinhaberin im Register die
M… Co., Ltd. (Tokio, Japan) geführt.


Das Streitpatent umfasst in seiner erteilten Fassung zwölf Ansprüche mit u.a. den
unabhängigen Patentansprüchen 1 und 3 sowie den auf den Anspruch 1
rückbezogenen Unteransprüchen 5 und 6 sowie den auf den Anspruch 3
rückbezogenen Unteransprüchen 9 und 10.


Der erteilte Patentanspruch 1 (mit Korrekturen der deutschsprachigen Version)
lautet wie folgt:


            in          der     Verfahrenssprache Übersetzung gemäß Streitpatent
            Englisch
 M1         A mobile station device included Mobilstationsvorrichtung,     die     in
            in      a     mobile   communication einem
            system, the mobile station device Mobilkommunikationssystem
            comprising:

                                       -6-



                                             enthalten       ist,     wobei         die
                                             Mobilstationsvorrichtung umfasst:
M1.1     a receiver conﬁgured to receive,    einen      Empfänger,      der       dafür
                                             eingerichtet ist, […] zu empfangen,
M1.2     on a physical downlink control auf             einem        physikalischen
         channel from a base station Downlink-Steuerkanal                   von   einer
         device,                             Basisstationsvorrichtung
M1.3     control information                 eine Steuerungsinformation
M1.3.1   having     a     downlink   control die            ein             Downlinkinformation format                  Steuerungsinformationsformat
                                             aufweist
M1.3.2   and being addressed to the und an die Mobilstation adressiert
         mobile station,                     ist,
M1.4     wherein the downlink control wobei                  das            Downlinkinformation format is used with a Steuerungsinformationsformat mit
         same total number of bits for einer gleichen Gesamtzahl von Bits
         downlink       scheduling   and   a für ein Downlink-Scheduling und
         random access order,                eine
                                             Direktzugriffsanweisungreihenfolge
                                             verwendet wird,
M1.4.1   in a case that the downlink falls                  das             Downlinkcontrol information format is used Steuerungsinformationsformat            für
         for the downlink scheduling, the das                Downlink-Scheduling
         control information provides a verwendet                   wird,           die
         downlink resource assignment, Steuerungsinformation                      eine
         and                                 Downlink-Ressourcenzuweisung
                                             vorsieht und
M1.4.2   in a case that the downlink falls                  das             Downlinkcontrol information format is used Steuerungsinformationsformat            für
         for the random access order, a die

                                           -7-



            preset value is set for a field of Direktzugriffsanweisungreihenfolge
            the        downlink         resource verwendet wird, ein voreingestellter
            assignment.                           Wert für ein Feld der Downlink-Ressourcenzuweisung       eingestellt
                                                  wird.


Der erteilte Patentanspruch 3 lautet (mit Korrekturen der deutschsprachigen
Version) wie folgt:


            in    der        Verfahrenssprache Übersetzung gemäß Streitpatent
            Englisch
 M3         A processing method for a mobile Verarbeitungsvfahren [sic] für eine
            station device included in a Mobilstationsvorrichtung,              die    in
            mobile communication system, einem
            the        processing        method Mobilkommunikationssystem
            comprising:                           enthalten      ist,   wobei         das
                                                  Verarbeitungsverfahren umfasst:
 M3.1       receiving,                            Empfangen,
 M3.2       on a physical downlink control auf               einem      physikalischen
            channel from a base station Downlink-Steuerkanal               von    einer
            device,                               Basisstationsvorrichtung,
 M3.3       control information                   einer Steuerungsinformation,
 M3.3.1     having       a   downlink    control die            ein           DownIinkinformation format                    Steuerungsinformationsformat
                                                  aufweist
 M3.3.2     and being addressed to the und an die Mobilstation adressiert
            mobile station,                       ist,
 M3.4       wherein the downlink control wobei                   das          Downlinkinformation format is used with a Steuerungsinformationsformat mit
            same total number of bits for einer gleichen Gesamtzahl von Bits

                                        -8-



           downlink     scheduling   and    a für ein Downlink-Scheduling und
           random access order,                eine
                                               Direktzugriffsanweisungreihenfolge
                                               verwendet wird,
 M3.4.1    in a case that the downlink falls                  das           Downlinkcontrol information format is used Steuerungsinformationsformat          für
           for the downlink scheduling, the das                Downlink-Scheduling
           control information provides a verwendet                 wird,          die
           downlink resource assignment, Steuerungsinformation                    eine
           and                                 Downlink-Ressourcenzuweisung
                                               vorsieht und
 M3.4.2    in a case that the downlink falls                  das           Downlinkcontrol information format is used Steuerungsinformationsformat          für
           for the random access order, a die
           preset value is set for a field of Direktzugriffsanweisungreihenfolge
           the        downlink       resource verwendet wird, ein voreingestellter
           assignment.                         Wert für ein Feld der Downlink-Ressourcenzuweisung          eingestellt
                                               wird.


Wegen des Wortlauts der erteilten Ansprüche 5, 6, 9 und 10 wird auf die
Streitpatentschrift verwiesen.


Die Klägerin greift das Streitpatent teilweise an, nämlich im Umfang der
Patentansprüche 1, 3, 5, 6, 9 und 10. Sie hat die Nichtigkeitsgründe der
unzulässigen Erweiterung und mangelnden Patentfähigkeit wegen fehlender
Neuheit und erfinderischer Tätigkeit geltend gemacht. Die Beklagte verteidigt das
Streitpatent in Bezug auf die angegriffenen Patentansprüche nach Hauptantrag nur
noch in der aus dem Tenor ersichtlichen Fassung und hilfsweise mit mehreren
geänderten Fassungen.

                                        -9-



Die Klägerin beantragt sinngemäß,
         das europäische Patent 2 667 676 im Umfang der Ansprüche 1, 3, 5, 6, 9
         und 10 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland
         für nichtig zu erklären, soweit es nicht von der Beklagten verteidigt wird.


Die weitergehende Klage hat die Klägerin mit Schriftsatz vom 23. November 2023
zurückgenommen.


Die Beklagte beantragt sinngemäß, wie erkannt.


Wegen der Fassungen des Streitpatents nach den Hilfsanträgen I, IIa bis IId, IIIa bis
IIId, IVa bis IVd, V wird auf den Schriftsatz der Beklagten vom 16. November 2023
verwiesen.


Beide Parteien haben sich mit einer Entscheidung im schriftlichen Verfahren
einverstanden erklärt.


Mit Beschluss vom 23. Januar 2020 hat der vormals zuständige 6. Nichtigkeitssenat,
Az.: 6 Ni 2/20, den Streitwert für das vorliegende Nichtigkeitsverfahren auf
1.250.000,-- Euro im Hinblick auf die Streitwertfestsetzung im Urteil vom
23. Juli 2020 im parallelen Verletzungsverfahren mit mehreren Beklagten und der
hiesigen Klägerin als Nebenintervenientin vor dem Landgericht München I, Az.:
7 O 8818/19, für den Zeitraum ab 20. September 2019 mit 1 Million Euro
festgesetzt.



Wegen der weiteren Einzelheiten des Sach- und Streitstandes wird auf den
Akteninhalt verwiesen.

                                      - 10 -



                           Entscheidungsgründe


Die Nichtigkeitsklage ist zulässig. Die Beklagte ist trotz Umschreibung der
Patentinhaberschaft       auf       die        M…       Co.,       Ltd.       nach
Rechtshängigkeit der Nichtigkeitsklage auch weiterhin als Prozessstandschafterin
passiv prozessführungsbefugt (zur Änderung der Rechtsinhaberschaft während des
Nichtigkeitsverfahrens vgl. Busse/Keukenschrijver, PatG, 9. Aufl., § 81, Rn. 119
m.w.N.). Denn die Veräußerung und Umschreibung des Streitpatents während des
Nichtigkeitsverfahrens haben für sich keinen Einfluss auf die Beklagtenstellung
(§ 99 Abs. 1 PatG i.V.m. § 265 Abs. 2 ZPO).


Die Teilnichtigkeitsklage ist insoweit begründet, als das Streitpatent im Umfang
der angegriffenen Patentansprüche 1, 3, 5, 6, 9 und 10 für nichtig zu erklären ist,
soweit es über die von der Beklagten nach Hauptantrag zulässigerweise beschränkt
verteidigte und von der Klägerin nicht angegriffene Fassung - wie aus dem Tenor
ersichtlich – hinausgeht. Über die weitergehende Nichtigkeitsklage war nicht mehr
zu entscheiden, nachdem die Klägerin insoweit die Klage zurückgenommen hat. Auf
die mit den Hilfsanträgen der Beklagten verteidigten geänderten Fassungen des
Streitpatents kam es damit nicht mehr an.



                                          I.


Die Klage ist insoweit begründet, als das Streitpatent, nachdem es jedenfalls auch
in einer zulässigerweise eingeschränkten Fassung verteidigt wird, in dem Umfang,
in dem es nicht mehr verteidigt wird, ohne weitere Sachprüfung für nichtig zu
erklären ist (st. Rspr., vgl. etwa BGH GRUR 2007, 404, Rdn. 15 – Carvedilol II;
GRUR 2011, 707, Rdn. 8 – Dentalgerätesatz; Urteil vom 21. März 2017, X ZR 19/15,
Rdn. 19 - juris).

                                               - 11 -



Durch die von der Beklagten nach Hauptantrag geänderte Fassung der
Patentansprüche 1, 3, 6 und 10 bei Streichung der Ansprüche 5 und 9 ist das
Streitpatent im angegriffenen Umfang in zulässiger Weise beschränkt worden.


Von der angegriffenen, erteilten Fassung unterscheidet sich die verteidigte Fassung
des Patentanspruchs 1 sowie des Patentanspruchs 3 nach Hauptantrag – neben
einer grammatikalischen Anpassung (Streichung bzw. Ergänzung von „and“) in den
Merkmalen M1.4.1 und M1.4.2 bzw. M3.4.1 und M3.4.2 – durch
-       Ersetzung des Begriffs „random access order“ durch den Begriff „uplink
        synchronisation request“ in den Merkmalen M1.4 und M1.4.2 bzw. M3.4 und
        M3.4.2; sowie
-       die Aufnahme der zusätzlichen Merkmale, die lauten:
        „wherein at least one of the following applies:
        (i)         in the case that the downlink control information format is used for the
                    downlink scheduling, the control information provides no uplink
                    resource assignment; or
        (ii)        in the case that the downlink control information format is used for the
                    uplink synchronization request, the control information further provides
                    an identification number specifying a random access preamble; or
        (iii)       in the case that the downlink control information format is used for the
                    uplink synchronization request, the control information further includes
                    a signature field providing an identification number specifying a random
                    access preamble, wherein 6 bits are allocated to the signature field.”


Durch         die     Ersetzung      des   Begriffs     „random   access   order“   (dtsch.:
Direktzugriffsanweisung) durch den Begriff „uplink synchronisation request“ (dtsch.:
Uplink-Synchronisationsaufforderung) in den Merkmalen M1.4 und M1.4.2 bzw.
M3.4 und M3.4.2 wird der Gegenstand der Patentansprüche 1 und 3 nach
Hauptantrag auf die in den Anmeldeunterlagen der Stammanmeldung (veröffentlicht
als EP 2 124 362 A1) offenbarte Ausführungsform beschränkt, wonach die gleiche
Gesamtzahl             von    Bits   des    Downlink-Steuerungsinformationsformats           im

                                          - 12 -



Zusammenhang mit dem Beibehalten einer Uplink-Synchronisation (d. h. „downlink
scheduling“) und der Aufforderung zu einer Uplink-Synchronisation (d. h. „uplink
synchronisation request“) verwendet wird (vgl. Seite 11, Zeilen 33 bis 36 und
Seite 23, Zeilen 5 und 6 der Anmeldeunterlagen der Stammanmeldung bzw.
Spalte 12, Zeilen 14 bis 19 und Spalte 24, Zeilen 31 bis 34 der Offenlegungsschrift
EP 2 124 362 A1).


Die in den Merkmalen M1.4 und M1.4.2 bzw. M3.4 und M3.4.2 vorgenommenen
Ersetzungen sind somit durch die Offenbarung der Anmeldeunterlagen der
Stammanmeldung gestützt.


Das zusätzlich aufgenommene Merkmal
      (i)    in the case that the downlink control information format is used for the
             downlink scheduling, the control information provides no uplink
             resource assignment; or
besagt, dass falls das Downlink-Steuerungsinformationsformat für das Downlink-Scheduling     verwendet    wird,   die      Steuerungsinformation   keine   Uplink-Ressourcenzuweisung vorsieht.


Bei dem in der Figur 1 der Anmeldeunterlagen der Stammanmeldung dargestellten
Ausführungsbeispiel     handelt     es     sich    um   ein   Downlink-Steuerungsinformationsformat, das für Downlink-Scheduling verwendet wird. Dieses Format
weist u. a. ein 12 Bits umfassendes Feld „RESOURCE ASSIGNMENT“ auf, das der
Downlink-Ressourcenzuweisung dient. Das in der Figur 1 dargestellte Downlink-Steuerungsinformationsformat weist darüber hinaus noch fünf weitere Felder auf,
wobei keines dieser Felder der Uplink-Ressourcenzuweisung dient (vgl. S. 10,
Z. 16 – 30 bzw. Sp. 10, Z. 41 – Sp. 12, Z. 7). Obwohl im Zusammenhang mit der
Beschreibung des Ausführungsbeispiels nach der Figur 1 nicht explizit erwähnt
wird, dass mit diesem Downlink-Steuerungsinformationsformat keine „Uplink“-
Ressourcen zugewiesen werden („no uplink resource assignment“), wird dies vom
Fachmann – einen Ingenieur mit universitärem Abschluss (Diplom oder Master) der

                                        - 13 -



Elektrotechnik, Fachrichtung Nachrichtentechnik, der über eine mehrjährige
Erfahrung auf dem Gebiet der Entwicklung von Mobilfunksystemen unter
Berücksichtigung     von    Mobilfunkstandards      und      Übertragungstechnik    in
Mobilfunknetzen verfügt und der sich über aktuelle Entwicklungen auf diesem
Gebiet, auch hinsichtlich der LTE-Standardisierung, auf dem Laufenden hält – bei
der   Würdigung      der    Gesamtoffenbarung        der     Anmeldeunterlagen     der
Stammanmeldung als offensichtlich mitgelesen.


Das zusätzlich aufgenommene Merkmal
      (ii)   in the case that the downlink control information format is used for the
             uplink synchronization request, the control information further provides
             an identification number specifying a random access preamble; or
besagt, dass falls das Downlink-Steuerungsinformationsformat für die Uplink-Synchronisationsaufforderung      verwendet      wird,     die   Steuerungsinformation
außerdem eine Identifikationsnummer vorsieht, welche eine Direktzugriffs-Präambel spezifiziert.


Der Stammanmeldung kann entnommen werden, dass ein Direktzugriffsversuch
von einer Mobilstation entweder unter Verwendung einer „dedicated signature“ oder
unter Verwendung einer „random signature“ durchgeführt werden kann. Ob der
Direktzugriffsversuch unter Verwendung einer „dedicated signature“ oder unter
Verwendung einer „random signature“ durchgeführt werden soll, wird der
Mobilstation mittels eines 2 Bits umfassenden Felds „TYPE“ kommuniziert (vgl.
Figur 3; vgl. S. 11, Z. 15 – 17 bzw. Sp. 11, Z. 45 – 48).


Bei dem Ausführungsbeispiel nach der Figur 6, bei welchem eine „dedicated
signature“ verwendet wird, weist die Uplink-Synchronisationsaufforderung das in
der Figur 3 dargestellte Format auf (vgl. S. 16, Z. 32 bzw. Sp. 17, Z. 36 – 37).
Das in dem Ausführungsbeispiel nach der Figur 3 dargestellte 6 Bits umfassende
Feld „SIGNATURE“ spezifiziert eine sog. „signature ID number“ (vgl. S. 11,
Z. 19 – 21 bzw. Sp. 11, Z. 52 – 55), die als Teil der von der Basisstation an die

                                         - 14 -



Mobilstation gesendeten Downlink-Steuerungsinformation gesendet wird, wenn das
2 Bits umfassende Feld „TYPE“ anzeigt, dass für den Direktzugriffsversuch eine
„dedicated signature“ zu verwenden ist. In diesem Falle entspricht die „signature ID
number“ der „dedicated signature“, welche von der Basisstation an die Mobilstation
als Teil der Uplink-Synchronisationsaufforderung gesendet wird (vgl. Figur 6:
SIGNAL 6-1; vgl. S. 16, Z. 15 – S. 17, Z. 10 bzw. Sp. 17, Z. 8 – Sp. 18, Z. 10). Die
von der Mobilstation auf diese Weise empfangene „dedicated signature“ wird von
der Mobilstation ihrerseits mittels der Direktzugriffs-Präambel an die Basisstation
gesendet (vgl. Figur 6: SIGNAL 6-2; vgl. S. 4, Z. 41 – S. 5, Z. 2 und S. 22, Z. 8 – 12
bzw. Sp. 5, Z. 6 – 9 und Sp. 23, Z. 31 – 38).
Dies berücksichtigend versteht der Fachmann im Falle der Verwendung einer
„dedicated signature“ die in den Anmeldeunterlagen der Stammanmeldung
genannten Bezeichnungen „identification number“ und „signature ID number“ als
Synonyme, so dass das zusätzlich aufgenommenen Merkmal „(ii) …“ (s. o.) im Falle
der Verwendung einer „dedicated signature“ durch die Offenbarung der
Anmeldeunterlagen der Stammanmeldung gestützt ist.


Bei dem Ausführungsbeispiel nach der Figur 7 wird eine „random signature“
verwendet, was der Mobilstation mittels des Felds „TYPE“ als Teil der Uplink-Synchronisationsaufforderung dadurch angezeigt wird, dass das Feld „TYPE“ mit
einer Zufallssignatur gefüllt wird (vgl. S. 18, Z. 7 – 8 bzw. Sp. 19, Z. 9 – 10).
Nach dem Empfang der Uplink-Synchronisationsaufforderung wählt der Signatur-Auswähler („signature selector“, 58) der Mobilstation zufallsabhängig eine Signatur
aus, welche als Teil der Direktzugriffs-Präambel von der Mobilstation an die
Basisstation übertragen wird (vgl. Figur 7: SIGNAL 7-2; vgl. S. 18, Z. 17 – 20 bzw.
Sp. 19, Z. 26 – 30). Die Verwendung dieser zufallsabhängig ausgewählten Signatur
(„random signature“) zum Spezifizieren einer Direktzugriffs-Präambel wird in den
Anmeldeunterlagen der Stammanmeldung zwar nicht explizit genannt, sie ergibt
sich jedoch implizit aus dem in den Anmeldeunterlagen der Stammanmeldung
genannten      E-UTRA-Standard        („Non-Patent      Document      3“),    der   der
Stammanmeldung zugrunde liegt und auf dem die Stammanmeldung aufbaut (vgl.

                                           - 15 -



Figuren 3, 17 und 18; vgl. S. 2, Z. 11 – 18 bzw. Sp. 2, Z. 6 – 18 und Sp. 11,
Z. 45 – 48), insbesondere da unter Berücksichtigung der Gesamtoffenbarung der
Anmeldunterlagen der Stammanmeldung nicht erkennbar ist, warum der Fachmann
der „random signature“ beim Einfügen in eine Direktzugriffs-Präambel durch die
Mobilstation eine andere Bedeutung für die Direktzugriffs-Präambel zurechnen
sollte, als für die „dedicated signature“.


Dies berücksichtigend ist das zusätzlich aufgenommenen Merkmal „(ii) …“ (s. o.) im
Falle der Verwendung einer „random signature“ ebenfalls durch die Offenbarung
der Anmeldeunterlagen der Stammanmeldung gestützt.


Das zusätzlich aufgenommene Merkmal
        (iii)   in the case that the downlink control information format is used for the
                uplink synchronization request, the control information further includes
                a signature field providing an identification number specifying a random
                access preamble, wherein 6 bits are allocated to the signature field
besagt, dass falls das Downlink-Steuerungsinformationsformat für die Uplink-Synchronisationsaufforderung         verwendet      wird,    die    Steuerungsinformation
außerdem ein Signaturfeld umfasst, welches eine Identifikationsnummer vorsieht,
welche eine Direktzugriffs-Präambel spezifiziert, wobei dem Signaturfeld 6 Bits
zugeordnet sind.


Dieses zusätzlich aufgenommene Merkmal präzisiert im Vergleich zu dem
vorangegangenen Merkmal „(ii) …“ (s. o.), dass die Identifikationsnummer mittels
eines      6 Bits     umfassenden      Signaturfeldes       als    Teil   der   Downlink-Steuerungsinformation von der Basisstation an die Mobilstation übertragen wird. Ein
6 Bits umfassendes Signatur-Feld („SIGNATURE“) ist Teil des in der Figur 3 der
Anmeldeunterlagen           der     Stammanmeldung            dargestellten     Downlink-Steuerungsinformationsformats.

                                       - 16 -



Auch das zusätzlich aufgenommenen Merkmal „(iii) …“ (s. o.) ist somit durch die
Offenbarung der Anmeldeunterlagen der Stammanmeldung gestützt.


Die voranstehenden Ausführungen zum Patentanspruch 1 nach Hauptantrag gelten
in gleicher Weise für den Patentanspruch 3 nach Hauptantrag.


Da die Anmeldeunterlagen der (Teil-)Anmeldung, die dem Streitpatent zugrunde
liegen,   in   allen   relevanten   Punkten     mit   den   Anmeldeunterlagen   der
Stammanmeldung übereinstimmen, gelten die zuvor im Zusammenhang mit den
Anmeldeunterlagen der Stammanmeldung genannten Aussagen in gleicher Weise
auch in Bezug auf die Anmeldeunterlagen der (Teil-)Anmeldung.


Die somit zulässige Beschränkung des Streitpatents im angegriffenen Umfang
durch die Beklagte und die Rücknahme der weitergehenden Nichtigkeitsklage durch
die Klägerin haben zur Folge, dass das Streitpatent entsprechend den
(übereinstimmenden) Anträgen beider Parteien ohne Sachprüfung des Restpatents
als rechtsbeständig gilt (vgl. Busse/Keukenschrijver, PatG, 9. Aufl., § 82, Rn. 127
m.w.N.; Schulte, PatG, 11. Aufl., § 81, Rn. 130 m.w.N., BPatG Urteil vom
17. März 2011, Az.: 2 Ni 21/09; Urteil vom 19. Februar 2013, Az.: 4 Ni 25/10 (EU)).


Das Streitpatent im Umfang der angegriffenen Patentansprüche 1, 3, 5, 6, 9 und 10
war daher dadurch teilweise für nichtig zu erklären, dass diese Patentansprüche die
verteidigte Fassung nach Hauptantrag erhalten.



                                         II.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. §§ 92 Abs. 1 1. Alt.,
269 Abs, 3 Satz 2 ZPO. Die ausgeurteilte Kostenverteilung entspricht dem Anteil
des Obsiegens und Unterliegens der Parteien. Denn der wirtschaftliche Wert, der
dem Streitpatent im angegriffenen Umfang aufgrund des als schutzfähig
verbleibenden Patentgegenstands gegenüber der weitergehenden erteilten

                                        - 17 -



Fassung mit der Einschränkung durch die drei neu aufgenommenen Merkmale
zukommt, ist deutlich verringert und mit ungefähr 40 % angemessen bewertet.



Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und Satz 2 ZPO.



Der Streitwert für das Nichtigkeitsverfahren war gemäß § 2 Abs. 1, 2 PatKostG
i. V. m. § 63 Abs. 2 GKG endgültig auf 1.250.000,-- Euro festzusetzen. Er entspricht
der vorläufigen Streitwertfestsetzung gemäß Beschluss vom 23. Januar 2020 des
vormals zuständigen 6. Nichtigkeitssenats. Der Senat hält diesen Streitwert im
Hinblick auf die Streitwertfestsetzung im parallelen Verletzungsprozess vor dem
Landgericht München I betreffend den Zeitraum der Klageeinreichung der
Nichtigkeitsklage und unter Berücksichtigung der ständigen Rechtsprechung des
Bundesgerichtshofes (Aufschlag 25 %, vgl. BGH, GRUR 2011, 757, Rn. 2 f. -
Nichtigkeitsstreitwert; Beschluss vom 16. Februar 2016 - X ZR 110/13, CIPR 2016,
69 Rn. 7; BGH GRUR 2013, 1287 f. - Nichtigkeitsstreitwert II) ebenfalls für
angemessen.




                                         III.


                             Rechtsmittelbelehrung



Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland

                                      - 18 -



zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Grote-Bittner        Altvater      Dr. Meiser      Dr. Haupt            Tischler


                                                                              wr


                beglaubigt


                Weißenburger, Justizbeschäftigte
                als Urkundsbeamtin der Geschäftsstelle
