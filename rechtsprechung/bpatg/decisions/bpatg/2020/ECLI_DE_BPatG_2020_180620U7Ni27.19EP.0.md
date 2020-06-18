---
ecli: "ECLI:DE:BPatG:2020:180620U7Ni27.19EP.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 Ni 27/19"
decided: "2020-06-18"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=20&nr=40751&anz=666&pos=306&Blank=1.pdf"
corpus_doc_id: "BPatG_JurBeschw-Nichtigkeit_NA_2020-06-18_7_Ni_27_19_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 7 Ni 27/19 vom 2020-06-18

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                       Verkündet am
                                                       18. Juni 2020
7 Ni 27/19 (EP)                                              …

(Aktenzeichen)


                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2020:180620U7Ni27.19EP.0

                                              -2-



                    betreffend das europäische Patent 1 459 165
                                       (DE 602 47 965)


hat der 7. Senat (Juristischer Beschwerdesenat und Nichtigkeitssenat) des
Bundespatentgerichts auf Grund der mündlichen Verhandlung vom 18. Juni 2020
durch die Richterin Püschel als Vorsitzende sowie den Richter Dipl.-Ing. Baumgardt,
die   Richterin     Dr. Schnurr       und    die   Richter    Dipl.-Phys. Dr.    Forkel     und
Dipl.-Ing. Hoffmann


für Recht erkannt:


        I.      Das europäische Patent 1 459 165 wird mit Wirkung für das
                Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
                nichtig erklärt.


        II.     Die Kosten des Rechtsstreits trägt die Beklagte.


        III.    Das Urteil ist im Kostenpunkt gegen Sicherheitsleistung in Höhe von
                120% des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.



                                       Tatbestand


Die Beklagte ist eingetragene Inhaberin des in englischer Verfahrenssprache u. a.
für den Geltungsbereich der Bundesrepublik Deutschland erteilten europäischen
Patents 1 459 165 (Streitpatent) mit der Bezeichnung „Touch-screen image
scrolling      system   and        method“    („Berührungsempfindliche         Anzeigeeinheit,
Bildverschiebungssystem und -verfahren“), das aus der internationalen Anmeldung
PCT/IB2002/005422 (veröffentlicht als Druckschrift WO 2003/060622 A2 = Anlage
NK4) vom 13. Dezember 2002 hervorgegangen ist und die Priorität der US-
amerikanischen Voranmeldung 10/034,375 vom 28. Dezember 2001 in Anspruch
nimmt. Im Deutschen Patent- und Markenamt wird das Streitpatent unter dem
Aktenzeichen        602 47 965.7       geführt.     Die      Patenterteilung     erfolgte    im

                                        -3-



Beschwerdeverfahren durch Entscheidung der zuständigen Beschwerdekammer
des Europäischen Patentamts (Anlage NK5). Das Streitpatent umfasst elf
Ansprüche, die alle mit der vorliegenden Klage angegriffen werden. Die
Ansprüche 2 bis 7 sind als Unteransprüche auf Patentanspruch 1 als unabhängigen
Systemanspruch unmittelbar bzw. mittelbar rückbezogen. Die Ansprüche 9 bis 11
sind auf Patentanspruch 8 als unabhängigen Verfahrensanspruch unmittelbar bzw.
mittelbar rückbezogen.


Patentanspruch 1 hat in der erteilten Fassung folgenden Wortlaut:


   1. A touch-screen image scrolling system, comprising:

      an electronic image display screen (40);
      a microprocessor (42) coupled to said display screen (40) to display
      information thereon and to receive interactive signals there-from;
      timer means (43) associated with said microprocessor (42) to provide timing
      capacity therefore;
      a source of scroll format data capable of display on said display screen (40);
      finger touch program instructions associated with said microprocessor (42)
      for sensing the speed and direction of a finger touch contact with said display
      screen (40);

      characterized in that

      said finger touch program instructions associated with said microprocessor
      (42) are also designed for sensing the time duration of a finger touch contact
      with said display screen (40); and in that said touch-screen image scrolling
      system further comprises:

      scrolling motion program instructions associated with said microprocessor
      (42) responsive to said duration of said stationary finger touch contact such
      that, when during a period having a duration which is greater than a first
      preset minimum time and less than a second preset minimum time motion of
      said finger touch along the surface of said display screen (40) is sensed, said
      display is first moved in correspondence with movement of the finger touch,
      and, following a separation of said finger touch from said screen (40), a scroll
      format display on said display screen (40) is caused to begin to scroll in said
      sensed direction and at said sensed initial speed;

      wherein sensing a finger touch during scrolling displacement of the image on

                                        -4-



      said display screen (40) acts solely as “stop motion“ regardless of the length
      of the touch;

      time decay program instructions associated with said microprocessor (42) for
      reducing the rate of scrolling displacement on said display screen (40) at a
      predetermined rate until motion is terminated;

      stopping motion program instructions associated with said microprocessor
      (42) for terminating scrolling displacement of the image on said display
      screen (40) upon first occurrence of any signal in the group of signals
      comprising:

          (a) a substantially stationary finger touch on the display screen (40)
              enduring for a period longer than a preset minimum time, and
          (b) an end-of-scroll signal received from said scroll format data source,

      wherein said scrolling motion program instructions comprise instructions
      responsive to said duration of said stationary finger touch contact such that,
      when during a period having a duration which is greater than a first preset
      minimum time and less than a second preset minimum time motion of said
      finger touch along the surface of said display screen (40) is sensed, said
      display is first moved in correspondence with movement of the finger touch,
      and, if there is no finger motion at the time when the finger contact with the
      display screen (40) is broken, said display screen (40) will remain in the
      position it is at that time without further motion, and the system reverts to
      "waiting" status,

      wherein said scrolling motion program instructions further comprise
      instructions responsive to said duration of said stationary finger touch contact
      such that, when said duration is less than said second preset minimum time
      and if no motion occurs before separation of said finger from said display
      screen, an item touched is selected, wherein upon selection the selected item
      is highlighted.


Patentanspruch 8 hat in der erteilten Fassung folgenden Wortlaut:


   8. A method of controlling a scroll-like display of data on an electronic display
      screen (40), said method comprising the steps of:

      sensing (100c) the speed and direction of motion of said finger touch contact
      with said display screen (40);

      sensing (100b) the duration of finger touch contact time with an electronic

                                   -5-



display screen (40) having scrollable data displayed thereon;

if the sensed duration of finger touch contact time is greater than a first preset
minimum time and less than a second preset minimum time and is
accompanied by motion along the surface of the display screen (40) moving
said display in correspondence with movement of the finger touch, and -
following separation of said finger touch from said display screen (40), -
initiating (104) scrolling motion of said scrollable data on said display screen
(40) in said sensed direction and at said sensed speed;

upon sensing a finger touch during scrolling displacement of the image on
said display screen (40), regardless of the length of the touch, stopping the
motion of said display;

slowing (106) the speed of said scrolling motion from the initiated speed
thereof, at a predetermined rate; and

terminating said scrolling motion upon first occurrence of any conditions from
the following group of conditions is sensed:

    (a)   a substantially stationary finger touch having a finite duration is
          sensed;
    (b)   an end-of-scroll signal is sensed,

if the sensed duration of said stationary finger touch contact time is greater
than a first preset minimum time and less than a second preset minimum time
and is accompanied by motion of said finger touch along the surface of said
display screen (40), and, if after subsequent moving of said display in
correspondence with movement of the finger touch, there is no finger motion
at the time that the finger contact with the display screen (40) is broken,
maintaining said display screen (40) in the position it is at that time without
further motion, and reverting the system to "waiting" status,

wherein said method comprises the further step (100) of selecting an item
touched if the sensed stationary duration of the finger touch contact time is
less than said second preset minimum time and if no motion occurs before
separation of said finger from said display screen (40), wherein upon
selection the selected item is highlighted.

                                      -6-



Die deutsche Übersetzung wird in der Streitpatentschrift wie folgt wiedergegeben
(bei Patentanspruch 8 mit Korrektur eines offensichtlichen Fehlers in Absatz 2,
siehe Unterstreichung):


   1. Touch-Screen Bild-Scrollsystem, umfassend:

      einen elektronischen Bild-Anzeigeschirm (40);

      einen Mikroprozessor (42), der mit dem Anzeigeschirm (40) gekoppelt ist,
      zum Anzeigen von Information darauf und zum Empfangen interaktiver
      Signale;

      Timer-Mittel (43), die mit dem Mikroprozessor (42) assoziiert sind, und für
      den Mikroprozessor eine Timer-Funktionalität bereitstellen;

      eine Quelle von Scroll-Formatdaten, die zur Anzeige auf dem Anzeigeschirm
      (40) geeignet sind;

      Fingerberührungs-Programmanweisungen, die mit dem Mikroprozessor (42)
      assoziiert sind, zum Erfassen der Geschwindigkeit und Richtung eines
      Fingerberührungskontaktes mit dem Anzeigeschirm (40);

      dadurch gekennzeichnet, dass

      die Fingerberührungs-Programmanweisungen, die mit dem Mikroprozessor
      (42) assoziiert sind, ferner ausgebildet sind, die Zeitdauer eines
      Fingerberührungskontaktes mit dem Anzeigebildschirm (40) zu erfassen; und
      dass das Touch-Screen Bild-Scroll-System weiter umfasst:

      Scroll-Bewegungs-Programmanweisungen, die mit dem Mikroprozessor (42)
      assoziiert sind und auf die Dauer des stationären Fingerberührungskontakts
      ansprechen, so dass, wenn, während einer Periode mit einer Dauer, die
      größer als eine erste vorbestimmte Mindestzeit und kleiner als eine zweite
      vorbestimmte Mindestzeit ist, Bewegung der Fingerberührung über die
      Oberfläche des Anzeigeschirms (40) erfasst wird, die Anzeige zunächst in
      Übereinstimmung mit der Bewegung der Fingerberührung bewegt wird, und
      nach einer Trennung der Fingerberührung von dem Anzeigeschirm (40) eine
      Scrollformatanzeige auf dem Anzeigeschirm (40) veranlasst wird, mit
      Scrollen in der erfassten Richtung und mit der erfassten, anfänglichen
      Geschwindigkeit zu beginnen;

      wobei Erfassen einer Fingerberührung während der Scroll-Verschiebung des
      Bildes auf dem Anzeigeschirm (40) ausschließlich als "Stopp-Bewegung"

                                     -7-



   funktioniert, unabhängig von der Dauer der Berührung;

   Abklingzeit-Programmanweisungen, die mit dem Mikroprozessor assoziiert
   sind, um die Geschwindigkeit der Scroll-Verschiebung auf dem
   Anzeigeschirm (40) mit einer vorbestimmten Rate zu verringern bis die
   Bewegung beendet ist;

   Stopp-Bewegungs-Programmanweisungen, die mit dem Mikroprozessor (42)
   assoziiert sind, zum Beenden der Scroll-Verschiebung des Bildes auf dem
   Anzeigeschirm (40) beim ersten Auftreten eines Signals aus der Gruppe von
   Signalen, umfassend:

       (a)   eine im wesentlichen stationäre Fingerberührung auf dem Anzeigeschirm (40), die für einen Zeitraum andauert, der länger ist als eine
             vorgegebene Mindestzeit, und
       (b)   ein Scroll-Ende-Signal, das von der Quelle von Scroll-Formatdaten
             empfangen wird,

   wobei    die    Scroll-Bewegungs-Programmanweisungen           Anweisungen
   umfassen, die auf die Dauer des stationären Fingerberührungskontaktes
   ansprechen, so dass, wenn, während einer Periode mit einer Dauer, die
   größer als eine erste voreingestellte Mindestzeit und kleiner als eine zweite
   voreingestellte Mindestzeit ist, Bewegung der Fingerberührung über die
   Oberfläche des Anzeigeschirms (40) erfasst wird, die Anzeige zunächst in
   Übereinstimmung mit einer Bewegung der Fingerberührung bewegt wird,

   und so dass, wenn es keine Fingerbewegung zu der Zeit gibt, zu der der
   Fingerkontakt mit dem Anzeigeschirm (40) abbricht, der Anzeigeschirm (40)
   in der Position verharrt, in der er zu diesem Zeitpunkt ohne weitere
   Bewegung ist, und das System in einen „Warte“ Status zurückkehrt,

   wobei die Scroll-Bewegungs-Programmanweisungen ferner Anweisungen
   umfassen, die auf die Dauer des stationären Fingerberührungskontaktes
   ansprechen, so dass, wenn die Dauer kleiner ist als die zweite voreingestellte
   Mindestzeit, und wenn keine Bewegung vor dem Lösen des Fingers von dem
   Anzeigebildschirm auftritt, ein Element, welches berührt wird, ausgewählt
   wird, wobei das ausgewählte Element bei Auswahl hervorgehoben wird.

8. Verfahren zum Steuern einer Scroll-artigen Anzeige von Daten auf einem
   elektronischen Anzeigeschirm (40), wobei das Verfahren die folgenden
   Schritte umfasst:

   Erfassen (100c) der Geschwindigkeit und Richtung einer Bewegung des
   Fingerberührungskontaktes mit dem Anzeigeschirm (40);

                                 -8-



Erfassen (100b) der Dauer einer Fingerberührungskontaktzeit mit einem
elektronischen Anzeigeschirm (40), der scrollbare Daten darauf anzeigt;

wenn die erfasste Dauer der Fingerberührungskontaktzeit größer als eine
erste voreingestellte Mindestzeit und kleiner als eine zweite voreingestellte
Mindestzeit ist und von einer Bewegung entlang der Oberfläche des
Anzeigeschirms (40) begleitet wird, Bewegen der Anzeige in
Übereinstimmung mit der Fingerberührung, und – folgend auf eine Trennung
der Fingerberührung von dem Anzeigeschirm (40) – Einleiten (104) einer
Scroll-Bewegung der scrollbaren Daten auf dem Anzeigeschirm (40) in der
erfassten Richtung und mit der erfassten Geschwindigkeit;

auf ein Erfassen einer Fingerberührung während der Scroll-Verschiebung
des Bildes auf dem Anzeigeschirm unabhängig von der Dauer der
Berührung, Stoppen der Bewegung der Anzeige;

Verlangsamen (106) der Geschwindigkeit der Scroll-Bewegung von der
anfänglichen Geschwindigkeit mit einer vorbestimmten Rate; und

Beenden der Scroll-Bewegung, sobald ein erstes Auftreten einer Bedingung
aus der folgenden Gruppe von Bedingungen erfasst wird:

    (a)   eine im wesentlichen stationäre Fingerberührung mit definierter
          Dauer
    (b)   ein Scroll-Ende-Signal,

wenn die erfasste Dauer der stationären Fingerberührungskontaktzeit größer
als eine erste voreingestellte Mindestzeit und kleiner als eine zweite
voreingestellte Mindestzeit ist, und von einer Bewegung entlang der
Oberfläche des Anzeigeschirms (40) begleitet wird, und wenn es nach einer
darauf folgenden Bewegung der Anzeige in Übereinstimmung mit der
Bewegung der Fingerberührung keine Fingerbewegung gibt zu der Zeit, zu
der der Fingerkontakt mit dem Anzeigeschirm (40) unterbrochen wird,
Beibehalten des Anzeigeschirms (40) in der Position, in der er ist zu der Zeit
ohne weitere Bewegung, und Zurückkehren des Systems zu einem "Warten"
Status;

wobei das Verfahren den weiteren Schritt (100) des Auswählens eines
berührten Elementes umfasst, wenn die stationäre Dauer der
Fingerberührungskontaktzeit kleiner ist als die zweite voreingestellte
Mindestzeit, und wenn keine Bewegung vor dem Lösen des Fingers von dem
Anzeigebildschirm auftritt, wobei das bei Auswahl ausgewählte Element
hervorgehoben wird.

                                        -9-




Wegen des Wortlauts der Unteransprüche 2 bis 7 und 9 bis 11 in englischer bzw.
deutscher Sprache wird auf die Streitpatentschrift EP 1 459 165 B1 Bezug
genommen.


Die Klägerin macht die Nichtigkeitsgründe der mangelnden Patentfähigkeit, der
unzulässigen Erweiterung und der mangelnden Ausführbarkeit (Art. II § 6 Abs. 1
Nr. 1, 2 und 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), b) und c), Art. 54,
56 EPÜ) geltend.


Der Gegenstand des erteilten Patentanspruchs 1 sei im Erteilungsverfahren
unzulässig erweitert worden. Die zweite voreingestellte Mindestkontaktzeit sei ohne
stationäre Berührung oder „touch dragging“ ursprünglich nicht offenbart gewesen.
Dies betreffe die isolierte Aufnahme dieses Merkmalselements in die Merkmale 1.8
/ 8.4 und 1.12 / 8.8. Ebenfalls nicht ursprünglich offenbart seien die Kombination der
Merkmale 1.9 / 8.5 und 1.11 a / 8.7 a sowie das Merkmal 8.5 (siehe
Merkmalsgliederung in den Entscheidungsgründen, I., Abschnitt 2).


Der Gegenstand des Unteranspruchs 4 sei nicht ausführbar. Denn dieser füge den
Stopp-Anweisungen nach Merkmal 1.11 das zusätzliche Element hinzu, dass die
fortlaufende Scroll-Bewegung auch dann gestoppt werde, wenn ein im
Wesentlichen stationärer Fingerberührungskontakt erfolge, der kürzer oder gleich
lang andauere wie eine voreingestellte Mindestzeit.


Zur Begründung des Nichtigkeitsgrundes der mangelnden Patentfähigkeit beruft
sich die Klägerin auf folgende Publikationen:


     D1      Europäische Offenlegungsschrift EP 0 626 635 A2
                                                (entspricht NK9 aus 7 Ni 68/19 (EP))
     D2      Europäische Offenlegungsschrift EP 0 880 091 A2
                                                (entspricht NK6 aus 7 Ni 68/19 (EP))

                                         - 10 -



     D3      „Manipulating Simulated Objects with Real-world Gestures using a
             Force and Position Sensitive Screen”, Computer Graphics, Vol. 18, No
             3, July 1984
     D4      US-Patentschrift 4,157,539
     D5      US-Patentschrift 4,374,381
     D6      US-Patentschrift 4,868,912
     D7      US-Patentschrift 5,864,105
     D8      US-Patentschrift 5,724,985
     NK8     US-Patentschrift 5,977,957


und aus dem Vortrag des ehemals hinzuverbundenen Verfahrens 7 Ni 68/19 (EP),
auf das die Klägerin voll Bezug nimmt:


     NK7     US-Patentschrift 5,880,411
     NK9a    Videoclip, abrufbar unter: https://gigazine.net/gscnews/en/20141007-
             star7-pda sowie https://www.youtube.com/watch?v=iCsTHQS7QqI;
     NK 9b Kopie des Konferenzprogramms der UIST (User Interface Software
             and Technology) Konferenz 1996 (http://uist.acm.org/uist96/schedule
             .html), welches die Präsentation mit dem Titel „Java: a Language
             Driven by a UI Vision" ausweist;
     NK 9c Protokoll einer Zeugenbefragung am 24. Juni 2015 im Rahmen eines
             in den USA geführten Patentrechtsstreits
     NK10    PCT-Veröffentlichung WO 99/57630 A1


Der Gegenstand der Patentansprüche 1 und 8 sei nicht neu gegenüber der
Entgegenhaltung D1 oder zumindest nahegelegt ausgehend von D1, D2 oder
NK9a, insbesondere in Verbindung mit NK10 und auch unter Berücksichtigung des
Fachwissens von dem Ignorieren von Fingerkontakten unterhalb einer zeitlichen
Grenze; Beleg für dieses Fachwissen seien D4 bis D7. Zudem sei der Gegenstand
dem Fachmann durch eine Kombination der Entgegenhaltung D2 mit D1 oder D3
oder auch mit D4 oder D8 nahegelegt gewesen. Auch die Merkmale der

                                            - 11 -



Unteransprüche weisen der Klägerin zufolge keinen erfinderischen Gehalt auf. Dies
gelte insbesondere auch für die Unteransprüche 2 und 6.


Die Klägerin beantragt,


       das europäische Patent EP 1 459 165 mit Wirkung für das
       Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang
       für nichtig zu erklären.


Die Beklagte beantragt,


       die Klage abzuweisen,


       hilfsweise die Klage abzuweisen, soweit sie sich gegen die
       Patentansprüche in der Fassung der mit Schriftsätzen vom 6. und
       29. Mai und vom 9. Juni 2020 eingereichten, in der Reihenfolge
       ihrer Nummerierung gestellten Hilfsanträge I bis VIIb richtet, wobei
       die Hilfsanträge in dieser Reihenfolge zu berücksichtigen sind: I, II,
       IIa, IIb, IIc, VI, VIa, VIb, III, IIIa, IIIb, IIIc, VII, VIIa, VIIb, IV, IVa, IVb,
       IVc, V, Va und Vb.


Gemäß Hilfsantrag I erhalten die Patentansprüche 1 und 8 folgende Fassung,
wobei die übrigen Ansprüche unverändert bestehen bleiben (Änderungen
gegenüber der erteilten Fassung durch Unterstreichung kenntlich gemacht):


   1. „A touch-screen image scrolling system, comprising: (…)“


      (…)    „wherein said scrolling motion program instructions further comprise
      instructions responsive to said duration of said stationary finger touch contact
      on said display screen (40) having a stationary data display, such that, (…).“


   8. „A method of controlling (…)“

                                       - 12 -




      (…)     „wherein said method comprises the further step (100) of selecting an
      item touched if the sensed stationary duration of the finger touch contact time
      on said display screen (40) having a stationary data display, is less than said
      (…).“


Gemäß Hilfsantrag II erhalten die Patentansprüche 1 und 8 folgende Fassung,
wobei die übrigen Ansprüche unverändert bestehen bleiben (Änderungen
gegenüber der erteilten Fassung durch Unterstreichung kenntlich gemacht):


   1. „A touch-screen image scrolling system, comprising: (…)“


      (…) „wherein sensing a stationary finger touch during scrolling displacement
      of the image (…);“


      (…) „wherein said scrolling motion program instructions further comprise
      instructions responsive to said duration of said stationary finger touch contact
      on said display screen (40) having a stationary data display, such that, (…).“


   8. „A method of controlling (…)“


      (…)     „if the sensed duration of finger touch contact time is greater than a
      first preset minimum time and less than a second preset minimum time and
      is accompanied by motion along the surface of the display screen (40), (…)“


      (…)     „upon sensing a stationary finger touch during scrolling displacement
      of the image on said display screen (40), regardless of the length of the touch,
      stopping the motion of said display, wherein the finger touch acts solely as
      “stop motion”,“


      (…)     „wherein said method comprises the further step (100) of selecting an
      item touched if the sensed stationary duration of the finger touch contact time

                                           - 13 -



       on said display screen (40) having a stationary data display, is less than said
       second preset minimum time (…).“


Gemäß Hilfsantrag IIa, der insgesamt aus zwei Patentansprüchen besteht, erhält
Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag II, und der
neue Patentanspruch 2 erhält die Fassung des Patentanspruchs 8 nach
Hilfsantrag II.


Gemäß Hilfsantrag IIb, der insgesamt aus nur einem Patentanspruch besteht,
erhält Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag II.


Gemäß Hilfsantrag IIc, der insgesamt aus nur einem Patentanspruch besteht,
erhält der neue Patentanspruch 1 die Fassung des Patentanspruchs 8 nach
Hilfsantrag II.


Hilfsantrag VI entspricht Hilfsantrag II mit der Modifikation, dass Patentanspruch 8
folgende Fassung erhält (Änderungen gegenüber der erteilten Fassung durch
Unterstreichung kenntlich gemacht):


    8. „A method of controlling (…)“


       (…)        „if the sensed duration of a stationary finger touch contact time is
       greater than a first preset minimum time and less than a second preset
       minimum time and is accompanied by motion along the surface of the display
       screen (40),”


       (…)        „upon sensing a stationary finger touch during scrolling displacement
       of the image on said display screen (40), regardless of the length of the touch,
       stopping the motion of said display, wherein the finger touch acts solely as
       “stop motion”,“


       (…)        „wherein said method comprises the further step (100) of selecting an

                                       - 14 -



      item touched if the sensed stationary duration of the finger touch contact time
      on said display screen (40) having a stationary data display, is less than said
      second preset minimum time (…).“


Hilfsantrag VIa, der insgesamt aus zwei Patentansprüchen besteht, entspricht
Hilfsantrag IIa mit der Modifikation, dass Patentanspruch 2 die Fassung des
Patentanspruchs 8 nach Hilfsantrag VI erhält.


Gemäß Hilfsantrag VIb, der insgesamt aus nur einem Patentanspruch besteht,
erhält Patentanspruch 1 die Fassung des Patentanspruchs 8 nach Hilfsantrag VI.


Gemäß Hilfsantrag III erhalten Patentanspruch 1 und der erteilte Patentanspruch 8
als neuer Patentanspruch 7 folgende Fassung, wobei der erteilte Patentanspruch 2
in geänderter Form in den neuen Patentanspruch 1 eingeht, die erteilten
Patentansprüche 3 bis 7, 9 und 11 – mit angepassten Rückbezügen - zu neuen
Patentansprüchen 2 bis 6, 8 und 9 werden und der erteilte Patentanspruch 10
entfällt (Änderungen gegenüber der erteilten Fassung durch Unterstreichung
kenntlich gemacht):


   1. „A touch-screen image scrolling system, comprising: (…)“


      (…)    „wherein   sensing    a   stationary   finger   touch   during   scrolling
      displacement of the image on said display screen (40) acts solely as "stop
      motion" regardless of the length of the touch;“


      (…)    „wherein said scrolling motion program instructions further comprise
      instructions responsive to said duration of said stationary finger touch contact
      on said display screen (40) having a stationary data display, such that, when
      said duration is less than said second preset minimum time (…);


      2. The touch-screen image scrolling system of claim 1,wherein said scrolling
      motion program instructions further comprise instructions to move a touch-

                                        - 15 -



       selected item relative to the stationary display in correspondence with
       movement of said finger touch, in response to motion following a touch having
       a stationary duration greater than said second preset minimum time.“


    7. „A method of controlling (…)“


       (…)     „if the sensed duration of finger touch contact time is greater than a
       first preset minimum time and less than a second preset minimum time and
       is accompanied by motion along the surface of the display screen (40),”


       (…)     „upon sensing a stationary finger touch during scrolling displacement
       of the image on said display screen (40), regardless of the length of the touch,
       stopping the motion of said display, wherein the finger touch acts solely as
       “stop motion”;“


       (…)     „wherein said method comprises the further step (100) of selecting an
       item touched if the sensed stationary duration of the finger touch contact time
       on said display screen (40) having a stationary data display, is less than said
       second preset minimum time and if no motion occurs before separation of
       said finger from said display screen (40), wherein upon selection the selected
       item is highlighted; wherein said method comprises the further step (103) of
       sensing a stationary finger touch on said screen having a duration greater
       than said second preset minimum time and then moving a touch-selected
       item relative to the stationary display in correspondence with movement of
       the finger touch.“


Gemäß Hilfsantrag IIIa, der insgesamt aus zwei Patentansprüchen besteht, erhält
Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag III und der
neue Patentanspruch 2 erhält die Fassung des Patentanspruchs 7 nach
Hilfsantrag III.


Gemäß Hilfsantrag IIIb, der insgesamt aus nur einem Patentanspruch besteht,

                                         - 16 -



erhält Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag III.


Gemäß Hilfsantrag IIIc, der insgesamt aus nur einem Patentanspruch besteht,
erhält der neue Patentanspruch 1 die Fassung des Patentanspruchs 7 nach
Hilfsantrag III.


Hilfsantrag VII entspricht Hilfsantrag III mit der Modifikation, dass der erteilte
Patentanspruch 8       als   neuer   Patentanspruch 7    folgende    Fassung     erhält
(Änderungen gegenüber der erteilten Fassung des Patentanspruchs 8 durch
Unterstreichung kenntlich gemacht):


   7. „A method of controlling (…)“


       (…)     „if the sensed duration of a stationary finger touch contact time is
       greater than a first preset minimum time and less than a second preset
       minimum time and is accompanied by motion along the surface of the display
       screen (40),”


       (…)     „upon sensing a stationary finger touch during scrolling displacement
       of the image on said display screen (40), regardless of the length of the touch,
       stopping the motion of said display, wherein the finger touch acts solely as
       “stop motion”;“


       (…)     „wherein said method comprises the further step (100) of selecting an
       item touched if the sensed stationary duration of the finger touch contact time
       on said display screen (40) having a stationary data display, is less than said
       second preset minimum time and if no motion occurs before separation of
       said finger from said display screen (40), wherein upon selection the selected
       item is highlighted; wherein said method comprises the further step (103) of
       sensing a stationary finger touch on said screen having a duration greater
       than said second preset minimum time and then moving a touch-selected
       item relative to the stationary display in correspondence with movement of

                                          - 17 -



       the finger touch.“


Hilfsantrag VIIa, der insgesamt aus zwei Patentansprüchen besteht, entspricht
Hilfsantrag IIIa mit der Modifikation, dass der neue Patentanspruch 2 die Fassung
des Patentanspruchs 7 nach Hilfsantrag VII erhält.


Gemäß Hilfsantrag VIIb, der insgesamt aus nur einem Patentanspruch besteht,
erhält der neue Patentanspruch 1 die Fassung des Patentanspruchs 7 nach
Hilfsantrag VII.


Gemäß Hilfsantrag IV erhalten die unabhängigen Patentansprüche 1 und 7
folgende Fassung, wobei der erteilte Patentanspruch 2 in geänderter Fassung in
den neuen Patentanspruch 1 eingeht, die erteilten Patentansprüche 3 bis 7, 9
und 11 mit angepassten Rückbezügen zu neuen Patentansprüchen 2 bis 6, 8 und 9
werden,    der     erteilte   Patentanspruch 8     in   geänderter   Form      zum     neuen
Patentanspruch 7 wird und der erteilte Patentanspruch 10 entfällt (Änderungen
gegenüber der erteilten Fassung durch Unterstreichung kenntlich gemacht):


   1. „A touch-screen image scrolling system, comprising: (…)“


       (…)    „scrolling      motion   program     instructions   associated    with    said
       microprocessor (42) responsive to said duration of said stationary finger
       touch contact such that, when during a period having a duration which is
       greater than a first preset minimum time and less than a second preset
       minimum time motion of said finger touch along the surface of said display
       screen (40) is sensed, said display is first moved in correspondence with
       movement of the finger touch, and, following a separation of said finger touch
       from said screen (40) and, if the finger is in motion at the time when the finger
       contact with the display screen (40) is broken, the, a scroll format display on
       said display screen (40) is caused to begin to scroll in said sensed direction
       and at said sensed initial speed;

                                   - 18 -



 wherein sensing a stationary finger touch during scrolling displacement of the
 image on said display screen (40) acts solely as "stop motion" regardless of
 the length of the touch;


 time decay program instructions associated with said microprocessor (42)
 for, during scrolling displacement, reducing the rate of scrolling displacement
 on said display screen (40) at a predetermined rate until motion is terminated;


 stopping motion program instructions associated with said microprocessor
 (42) for, during scrolling displacement, terminating scrolling displacement of
 the image on said display screen (40) upon first occurrence of any signal in
 the group of signals comprising:“


 (…)    „wherein said scrolling motion program instructions further comprise
 instructions responsive to said duration of said stationary finger touch contact
 on said display screen (40) having a stationary data display, such that, when
 said duration is less than said second preset minimum time and if no motion
 occurs before separation of said finger from said display screen, an item
 touched is selected, wherein upon selection the selected item is highlighted;


 2. The touch-screen image scrolling system of claim 1, wherein said scrolling
 motion program instructions further comprise instructions to move a touchselected item relative to the stationary display in correspondence with
 movement of said finger touch, in response to motion following a touch having
 a stationary duration greater than 30 said second preset minimum time.“


7. „A method of controlling (…)“


 (…)    „if the sensed duration of finger touch contact time is greater than a
 first preset minimum time and less than a second preset minimum time and
 is accompanied by motion along the surface of the display screen (40),
 moving said display in correspondence with movement of the finger touch,

                                         - 19 -



       and - following separation of said finger touch from said display screen (40),
       if the finger is in motion at the time when the finger contact with the display
       screen (40) is broken, - initiating (104) scrolling (…)“


       (…)    „upon sensing a stationary finger touch during scrolling displacement
       of the image on said display screen (40), regardless of the length of the touch,
       stopping the motion of said display, wherein the finger touch acts solely as
       “stop motion”;


       slowing (106), during scrolling displacement, the speed of said scrolling
       motion from the initiated speed thereof, at a predetermined rate; and
       terminating said scrolling motion upon first occurrence of any conditions from
       the following group of conditions is sensed: (…)“


       (…) „wherein said method comprises the further step (100) of selecting an
       item touched if the sensed stationary duration of the finger touch contact time
       on said display screen (40) having a stationary data display, is less than said
       second preset minimum time and if no motion occurs before separation of
       said finger from said display screen (40), wherein upon selection the selected
       item is highlighted; wherein said method comprises the further step (103) of
       sensing a stationary finger touch on said screen having a duration greater
       than said second preset minimum time and then moving a touch-selected
       item relative to the stationary display in correspondence with movement of
       the finger touch.“


Gemäß Hilfsantrag IVa, der insgesamt aus zwei Patentansprüchen besteht, erhält
Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag IV, und der
neue Patentanspruch 2 erhält die Fassung des Patentanspruchs 7 nach
Hilfsantrag IV.


Gemäß Hilfsantrag IVb, der insgesamt aus nur einem Patentanspruch besteht,
erhält Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag IV.

                                        - 20 -




Gemäß Hilfsantrag IVc, der insgesamt aus nur einem Patentanspruch besteht,
erhält der neue Patentanspruch 1 die Fassung des Patentanspruchs 7 nach
Hilfsantrag IV.


Gemäß Hilfsantrag V erhält Patentanspruch 1 die Fassung des Patentanspruchs 1
nach Hilfsantrag IV, die erteilten Patentansprüche 3 bis 7, 9 und 11 werden mit
angepassten Rückbezügen zu neuen Patentansprüchen 2 bis 6, 8 und 9, der
erteilte Patentanspruch 10 entfällt. Der erteilte Patentanspruch 8 erhält als neuer
Patentanspruch 7 folgende Fassung (Änderungen gegenüber der erteilten Fassung
durch Unterstreichung kenntlich gemacht):


   7. „A method of controlling (…)“


       „(…) if the sensed duration of said stationary finger touch contact time is
       greater than a first preset minimum time and less than a second preset
       minimum time and is accompanied by motion along the surface of the display
       screen (40), moving said display in correspondence with movement of the
       finger touch, and - following separation of said finger touch from said display
       screen (40), if the finger is in motion at the time when the finger contact with
       the display screen (40) is broken, - initiating (104) scrolling motion of said
       scrollable data on said display screen (40) in said sensed direction and at
       said sensed speed;


       upon sensing a stationary finger touch during scrolling displacement of the
       image on said display screen (40), regardless of the length of the touch,
       stopping the motion of said display, wherein the finger touch acts solely as
       “stop motion”;


       slowing (106), during scrolling displacement, the speed of said scrolling
       motion from the initiated speed thereof, at a predetermined rate; and
       terminating said scrolling motion upon first occurrence of any conditions from

                                          - 21 -



         the following group of conditions is sensed:”


         (…) „wherein said method comprises the further step (100) of selecting an
         item touched if the sensed stationary duration of the finger touch contact time
         on said display screen (40) having a stationary data display is less than said
         second preset minimum time and if no motion occurs before separation of
         said finger from said display screen (40), wherein upon selection the selected
         item is highlighted;


         wherein said method comprises the further step (103) of sensing a stationary
         finger touch on said screen having a duration greater than said second preset
         minimum time and then moving a touch-selected item relative to the
         stationary display in correspondence with movement of the finger touch.“


Gemäß Hilfsantrag Va, der insgesamt aus zwei Patentansprüchen besteht, erhält
Patentanspruch 1 die Fassung des Patentanspruchs 1 nach Hilfsantrag V, und der
neue Patentanspruch 2 erhält die Fassung des Patentanspruchs 7 nach
Hilfsantrag V.


Gemäß Hilfsantrag Vb, der insgesamt aus nur einem Patentanspruch besteht,
erhält     der   neue     Patentanspruch 1     die   Fassung      des    unabhängigen
Patentanspruchs 7 nach Hilfsantrag V.


Die Beklagte widerspricht dem Vortrag der Klägerin in allen Punkten. Sie hält das
Streitpatent in den von ihr mit Haupt- und Hilfsanträgen verteidigten Fassungen für
patentfähig.


Der Klägerin zufolge ist der Patentanspruch 1 in den Fassungen der Hilfsanträge I,
II bis II c, III bis IIIc, IV bis IVc und V bis Vb unzulässig erweitert und zudem nicht
patentfähig. Der Gegenstand des Hilfsantrags III sowie das neue Merkmal 8.4 seien
zudem unklar: Hilfsantrag III enthalte die Formulierung „berührungsausgewähltes“
Element, deren Sinn sich nicht erschließe. Das neue Merkmal 8.4 betreffend sei

                                      - 22 -



nicht eindeutig, ob nur die Dauer der stationären Fingerberührung gemessen werde
und diese als Steuerparameter in die Gestensteuerung einfließen solle, oder auch
die Dauer der bewegten Fingerberührung, da die stationäre Fingerberührung von
Bewegung „begleitet“ werden solle. Die Hilfsanträge V bis Vb rügt die Klägerin als
verspätet.


Der Senat hat den Parteien mit Schreiben vom 17. März 2020 einen qualifizierten
gerichtlichen Hinweis zukommen lassen.


Das Verfahren 7 Ni 68/19 (EP) ist mit Senatsbeschluss vom 17. Juni 2019 zu
vorliegendem Verfahren hinzuverbunden und nach Rücknahme der dortigen Klage
mit Senatsbeschluss vom 20. Februar 2020 wieder abgetrennt worden.


Wegen des Vorbringens der Parteien im Übrigen wird auf deren Schriftsätze mit
sämtlichen Anlagen und auf das Protokoll der mündlichen Verhandlung vom
18. Juni 2020 verwiesen.

                                        - 23 -



                            Entscheidungsgründe



Die zulässige Klage hat in der Sache Erfolg. Das Streitpatent hat weder in seiner
erteilten noch in einer seiner mit den Hilfsanträgen I bis VIIb verteidigten Fassungen
Bestand. In der erteilten Fassung und in der Fassung nach Hilfsantrag I ist der
Gegenstand des Streitpatents unzulässig erweitert (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG
i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ). In den Fassungen der weiteren
Hilfsanträge II bis VIIb beruht der Gegenstand des Streitpatents nicht auf
erfinderischer Tätigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1
Buchst. a), Art. 56 EPÜ).



                                          I.


1.     Die vorliegende Erfindung betrifft nach ihrer Beschreibung in der Streitpatentschrift die Anzeige von Informationen, die normalerweise aus Listen von
Wörtern und Zahlen in Form aufeinanderfolgender Zeilen bestehen, insbesondere
die   Steuerung   elektronischer   Formen        dieser   Anzeige   (Streitpatentschrift,
Abs. [0001]).


Es sei allgemein üblich geworden, derartige Listen auf elektronischen Bildschirmen
anzuzeigen. Häufig erstreckten sich diese Listen über eine Länge, die die
Abmessungen des elektronischen Bildschirms überschreite, und in solchen Fällen
sei es bekannt geworden, das Bild der Liste über den Bildschirm zu „rollen“ (engl.
„to scroll“), so dass eine Textzeile mit Wörtern, Zahlen oder Symbolen sich von
einem Bildschirmrand zum anderen zu bewegen scheine, bis der gewünschte
Abschnitt der Liste oder Teil einer Zeile erreicht werde (Streitpatentschrift,
Abs. [0002]).


Es sei ferner bekannt, dass die Systeme und Prozesse, die gegenwärtig zur
Steuerung der Bildlaufbewegung des Bildschirmbildes verwendet werden, zahlreichen Einschränkungen und Nachteilen unterlägen. Beispielsweise könne in

                                       - 24 -



einem System ein Cursor an einem Rand des Bildschirms platziert und dann während des Drückens einer ausgewählten Maustaste an den gegenüberliegenden
Rand bewegt werden, wodurch das Bildschirmbild in die gewünschte Richtung
„gezogen“ werde (engl. „dragging“). Es sei allgemein bekannt, dass diese Verschiebung des Bildschirmbildes langsam und umständlich sei. Alle die anderen
bekannten, von der Cursor-Positionierung abhängigen Steuerungssysteme unterlägen ähnlichen Einschränkungen im Hinblick auf eine Desorganisation der Darstellung auf dem Bildschirm, den Mangel an ästhetischer, visueller Attraktivität und
das Erfordernis einer Handhabung des Maussteuergeräts (Streitpatentschrift,
Abs. [0003]).


In den folgenden Absätzen [0004] bis [0017] geht das Streitpatent kurz auf mehrere
Dokumente aus dem Stand der Technik ein und bezeichnet selbst als „vorbekannt“:


–     das Scrollen von Informationen auf einer Anzeige einer Mobilstation durch
      Fingerberührung, wobei die Geschwindigkeit und Richtung der Fingerberührung zum Zeitpunkt, wenn der Finger vom Bildschirm abgehoben wird, die
      anfängliche Scroll-Geschwindigkeit und -Richtung der Scroll-Verschiebung
      der Anzeige bestimmt;


–     das automatische Verringern der Geschwindigkeit, mit der die Scroll-Verschiebung der Anzeige erfolgt, gemäß einer vorbestimmten Rate;


–     das Beenden der Scroll-Verschiebung der Anzeige, wenn während der
      Scroll-Verschiebung eine Fingerberührung, egal welcher Länge, erkannt
      wird;


–     das Messen der Berührdauer der Fingerberührung zur Unterscheidung
      auszulösender Funktionen;


–     das „Ziehen“ von Bildschirm-Objekten zu einer anderen Stelle des Bildschirms hin („drag gesture“).

                                           - 25 -



Im Sinne einer Aufgabenstellung ermögliche es die Erfindung nach der Lehre des
Streitpatents für den Betrachter oder Benutzer, beim Anzeigen scrollbarer Daten auf
elektronischen Bildschirmen auf den gewünschten Teil einer langen Liste von Daten
und Informationen durch Scrollen schnell und „auf natürliche Weise“ zuzugreifen
(Streitpatentschrift, Abs. [0019]).


Dies werde erreicht über eine intuitive Fingersteuerung durch ein Touch-Screen-Bild-Scrollsystem mit den Merkmalen gemäß Patentanspruch 1 und ein Verfahren
zum Steuern einer scrollartigen Anzeige von Daten auf einem elektronischen
Anzeigeschirm gemäß Patentanspruch 8.


2.         Die Merkmale dieser Ansprüche können – entsprechend einem Vorschlag
der Parteien (Anlagen NK6 und B1) – wie folgt gegliedert werden:


Patentanspruch 1:


     1.1    A touch-screen image scrolling          Touch-Screen-Bild-Scrollsystem, umsystem, comprising:                     fassend:
     1.2    an electronic     image    display einen elektronischen Bild-Anzeigescreen (40);                       schirm (40);
     1.3    a microprocessor (42) coupled to        einen Mikroprozessor (42), der mit
            said display screen (40) to display     dem Anzeigeschirm (40) gekoppelt ist,
            information thereon and to              zum Anzeigen von Information darauf
            receive     interactive     signals     und zum Empfangen interaktiver
            therefrom;                              Signale;
     1.4    timer means (43) associated with Timer-Mittel (43), die mit dem Mikrosaid microprocessor (42) to prozessor (42) assoziiert sind, und für
            provide timing capacity therefore; den Mikroprozessor eine Timer-Funktionalität bereitstellen;
     1.5    a source of scroll format data eine Quelle von Scroll-Formatdaten,
            capable of display on said display die zur Anzeige auf dem Anzeigescreen (40);                       schirm (40) geeignet sind;
     1.6    finger touch program instructions Fingerberührungs-Programmanweiassociated with said micropro- sungen, die mit dem Mikroprozessor
            cessor (42) for sensing the speed (42) assoziiert sind, zum Erfassen der

                                     - 26 -




        and direction of a finger touch       Geschwindigkeit und Richtung eines
        contact with said display screen      Fingerberührungskontaktes mit dem
        (40);                                 Anzeigeschirm (40);
        characterized in that                 dadurch gekennzeichnet, dass
1.7     said finger touch program die Fingerberührungs-Programmaninstructions associated with said weisungen, die mit dem Mikropromicroprocessor (42) are also zessor (42) assoziiert sind, ferner
        designed for sensing the time ausgebildet sind, die Zeitdauer eines
        duration of a finger touch contact Fingerberührungskontaktes mit dem
        with said display screen (40);     Anzeigebildschirm (40) zu erfassen;
1.8     and in that said touch-screen und dass das Touch-Screen-Bildimage scrolling system further Scroll-System         weiter    umfasst:
        comprises: scrolling motion pro- Scroll-Bewegungs-Programmanweigram instructions associated with sungen, die mit dem Mikroprozessor
        said microprocessor (42) respon- (42) assoziiert sind und auf die Dauer
        sive to said duration of said des stationären Fingerberührungsstationary finger touch contact kontakts ansprechen, so dass, wenn
        such that, when during a period während einer Periode mit einer
        having a duration which is greater Dauer, die größer als eine erste vorthan a first preset minimum time bestimmte Mindestzeit und kleiner als
        and less than a second preset eine zweite vorbestimmte Mindestzeit
        minimum time motion of said ist, Bewegung der Fingerberührung
        finger touch along the surface of über die Oberfläche des Anzeigesaid display screen (40) is schirms (40) erfasst wird, die Anzeige
        sensed, said display is first moved zunächst in Übereinstimmung mit der
        in correspondence with move- Bewegung            der    Fingerberührung
        ment of the finger touch,           bewegt wird,
1.8.1   and, following a separation of said und nach einer Trennung der Fingerfinger touch from said screen (40), berührung von dem Anzeigeschirm
        a scroll format display on said (40) eine Scrollformatanzeige auf dem
        display screen (40) is caused to Anzeigeschirm (40) veranlasst wird,
        begin to scroll in said sensed mit Scrollen in der erfassten Richtung
        direction and at said sensed initial und mit der erfassten, anfänglichen
        speed;                               Geschwindigkeit zu beginnen;
1.9     wherein sensing a finger touch        wobei Erfassen einer Fingerberühduring scrolling displacement of      rung    während    der    Scroll-Verthe image on said display screen      schiebung des Bildes auf dem
        (40) acts solely as "stop motion"     Anzeigeschirm (40) ausschließlich als
        regardless of the length of the       "Stopp-Bewegung" funktioniert, unabtouch;                                hängig von der Dauer der Berührung;

                                     - 27 -




1.10   time decay program instructions Abklingzeit-Programmanweisungen,
       associated with said micropro- die mit dem Mikroprozessor assoziiert
       cessor (42) for reducing the rate sind, um die Geschwindigkeit der
       of scrolling displacement on said Scroll-Verschiebung auf dem Andisplay screen (40) at a pre- zeigeschirm (40) mit einer vorbedetermined rate until motion is stimmten Rate zu verringern, bis die
       terminated;                       Bewegung beendet ist;
1.11   stopping motion program instruc- Stopp-Bewegungs-Programmanweitions associated with said micro- sungen, die mit dem Mikroprozessor
       processor (42) for terminating (42) assoziiert sind, zum Beenden der
       scrolling displacement of the Scroll-Verschiebung des Bildes auf
       image on said display screen (40) dem Anzeigeschirm (40) beim ersten
       upon first occurrence of any signal Auftreten eines Signals aus der
       in the group of signals comprising: Gruppe von Signalen, umfassend:
       (a) a substantially stationary (a) eine im Wesentlichen stationäre
            finger touch on the display        Fingerberührung auf dem Anzeiscreen (40) enduring for a         geschirm (40), die für einen Zeitperiod longer than a preset        raum andauert, der länger ist als
            minimum time, and                  eine vorgegebene Mindestzeit,
                                               und
       (b) an      end-of-scroll    signal (b) ein Scroll-Ende-Signal, das von
            received from said scroll          der Quelle von Scroll-Formatformat data source,                daten empfangen wird,
1.12   wherein said scrolling motion wobei die Scroll-Bewegungs-Proprogram instructions comprise grammanweisungen               Anweisungen
       instructions responsive to said umfassen, die auf die Dauer des staduration of said stationary finger tionären Fingerberührungskontaktes
       touch contact such that, when ansprechen, so dass, wenn, während
       during a period having a duration einer Periode mit einer Dauer, die
       which is greater than a first preset größer als eine erste voreingestellte
       minimum time and less than a Mindestzeit und kleiner als eine zweite
       second preset minimum time voreingestellte              Mindestzeit    ist,
       motion of said finger touch along Bewegung der Fingerberührung über
       the surface of said display screen die Oberfläche des Anzeigeschirms
       (40) is sensed, said display is first (40) erfasst wird, die Anzeige zumoved in correspondence with nächst in Übereinstimmung mit einer
       movement of the finger touch, Bewegung             der    Fingerberührung
       and,                                  bewegt wird,
1.12.1 if there is no finger motion at the und so dass, wenn es keine Fingertime when the finger contact with bewegung zu der Zeit gibt, zu der der

                                        - 28 -




        the display screen (40) is broken,       Fingerkontakt mit dem Anzeigeschirm
        said display screen (40) will            (40) abbricht, der Anzeigeschirm (40)
        remain in the position it is at that     in der Position verharrt, in der er zu
        time without further motion, and         diesem Zeitpunkt ohne weitere
        the system reverts to "waiting"          Bewegung ist, und das System in
        status,                                  einen "Warte"-Status zurückkehrt,
 1.13   wherein said scrolling motion wobei die Scroll-Bewegungs-Proprogram     instructions     further grammanweisungen ferner Anweicomprise instructions responsive sungen umfassen, die auf die Dauer
        to said duration of said stationary des stationären Fingerberührungsfinger touch contact such that, kontaktes ansprechen, so dass, wenn
        when said duration is less than die Dauer kleiner ist als die zweite
        said second preset minimum time voreingestellte Mindestzeit, und wenn
        and if no motion occurs before keine Bewegung vor dem Lösen des
        separation of said finger from said Fingers von dem Anzeigebildschirm
        display screen, an item touched is auftritt, ein Element, welches berührt
        selected, wherein upon selection wird, ausgewählt wird, wobei das
        the selected item is highlighted.    ausgewählte Element bei Auswahl
                                             hervorgehoben wird.


Patentanspruch 8:


8.1     A method of controlling a scroll-        Verfahren zum Steuern einer scrolllike display of data on an               artigen Anzeige von Daten auf einem
        electronic display screen (40),          elektronischen Anzeigeschirm (40),
        said method comprising the steps         wobei das Verfahren die folgenden
        of:                                      Schritte umfasst:
8.2     sensing (100c) the speed and             Erfassen (100c) der Geschwindigkeit
        direction of motion of said finger       und Richtung einer Bewegung des
        touch contact with said display          Fingerberührungskontaktes mit dem
        screen (40);                             Anzeigeschirm (40);
8.3     sensing (100b) the duration of Erfassen (100b) der Dauer einer
        finger touch contact time with an Fingerberührungskontaktzeit      mit
        electronic display screen (40) einem elektronischen Anzeigeschirm
        having scrollable data displayed (40), der scrollbare Daten darauf anthereon;                          zeigt;
8.4     if the sensed duration of finger wenn die erfasste Dauer der Fingertouch contact time is greater than berührungskontaktzeit größer als eine
        a first preset minimum time and erste voreingestellte Mindestzeit und

                                       - 29 -




        less than a second preset mini-         kleiner als eine zweite voreingestellte
        mum time and is accompanied by          Mindestzeit ist und von einer
        motion along the surface of the         Bewegung entlang der Oberfläche
        display screen (40) moving said         des Anzeigeschirms (40) begleitet
        display in correspondence with          wird, Bewegen der Anzeige in Übermovement of the finger touch,           einstimmung mit der Fingerberührung,
8.4.1   and – following separation of said      und – folgend auf eine Trennung der
        finger touch from said display          Fingerberührung von dem Anzeigescreen (40), – initiating (104)         schirm (40) – Einleiten (104) einer
        scrolling motion of said scrollable     Scroll-Bewegung der scrollbaren
        data on said display screen (40) in     Daten auf dem Anzeigeschirm (40) in
        said sensed direction and at said       der erfassten Richtung und mit der
        sensed speed;                           erfassten Geschwindigkeit;
8.5     upon sensing a finger touch during      auf ein Erfassen einer Fingerberühscrolling displacement of the           rung     während     der     Scrollimage on said display screen (40),      Verschiebung des Bildes auf dem
        regardless of the length of the         Anzeigeschirm unabhängig von der
        touch, stopping the motion of said      Dauer der Berührung, Stoppen der
        display;                                Bewegung der Anzeige;
8.6     slowing (106) the speed of said Verlangsamen (106) der Geschwinscrolling motion from the initiated digkeit der Scroll-Bewegung von der
        speed thereof, at a predetermined anfänglichen Geschwindigkeit mit
        rate; and                           einer vorbestimmten Rate; und
8.7     terminating said scrolling motion Beenden der Scroll-Bewegung, soupon first occurrence of any con- bald ein erstes Auftreten einer Bedinditions from the following group of gung aus der folgenden Gruppe von
        conditions is sensed:               Bedingungen erfasst wird:
        (a) a substantially stationary (a) eine im wesentlichen stationäre
              finger touch having a finite     Fingerberührung mit definierter
              duration is sensed;              Dauer
        (b) an end-of-scroll signal is (b) ein Scroll-Ende-Signal,
              sensed,
8.8     if the sensed duration of said          wenn die erfasste Dauer der statiostationary finger touch contact         nären    Fingerberührungskontaktzeit
        time is greater than a first preset     größer als eine erste voreingestellte
        minimum time and less than a            Mindestzeit und kleiner als eine zweite
        second preset minimum time and          voreingestellte Mindestzeit ist, und
        is accompanied by motion of said        von einer Bewegung entlang der

                                           - 30 -




         finger touch along the surface of Oberfläche des Anzeigeschirms (40)
         said display screen (40),         begleitet wird,
8.8.1    and, if after subsequent moving of         und wenn es nach einer daraufsaid display in correspondence             folgenden Bewegung der Anzeige in
         with movement of the finger touch,         Übereinstimmung mit der Bewegung
         there is no finger motion at the           der Fingerberührung keine Fingerbetime that the finger contact with the      wegung gibt zu der Zeit, zu der der
         display screen (40) is broken,             Fingerkontakt mit dem Anzeigeschirm
         maintaining said display screen            (40) unterbrochen wird, Beibehalten
         (40) in the position it is at that time    des Anzeigeschirms (40) in der Posiwithout further motion, and                tion, in der er ist zu der Zeit ohne
         reverting the system to "waiting”          weitere Bewegung, und Zurückkehren
         status,                                    des Systems zu einem "Warten"
                                                    Status;
8.9      wherein said method comprises wobei das Verfahren den weiteren
         the further step (100) of selecting Schritt (100) des Auswählens eines
         an item touched if the sensed berührten Elementes umfasst, wenn
         stationary duration of the finger die stationäre Dauer der Fingerberühtouch contact time is less than said rungskontaktzeit kleiner ist als die
         second preset minimum time and zweite voreingestellte Mindestzeit,
         if no motion occurs before und wenn keine Bewegung vor dem
         separation of said finger from said Lösen des Fingers von dem Anzeidisplay screen (40), wherein upon gebildschirm auftritt, wobei das bei
         selection the selected item is Auswahl ausgewählte Element herhighlighted.                         vorgehoben wird.


3.      Bei dem hier einschlägigen Durchschnittsfachmann, der damit betraut wird,
das Anzeigen scrollbarer Daten auf elektronischen Bildschirmen zu vereinfachen
und es Benutzern zu ermöglichen, auf den gewünschten Teil einer langen Liste
schnell und „auf natürliche Weise“ zuzugreifen, handelt es sich, soweit technische
Probleme betroffen sind, um einen Informatiker mit Universitätsabschluss und
mehrjähriger Berufserfahrung in der Entwicklung und Programmierung von
grafischen Benutzeroberflächen für Endgeräte mit berührungsempfindlichem
Bildschirm.

                                        - 31 -



4.    Dieser Fachmann legt den unabhängigen Patentansprüchen 1 und 8
folgendes Verständnis zugrunde:


4.1   Patentanspruch 8 bezieht sich auf ein mehrschrittiges Verfahren zum
Steuern einer scroll-artigen Anzeige von Daten auf einem berührungsempfindlichen
Bildschirm (Touch-Screen) mithilfe eines Fingers, Patentanspruch 1 auf das
zugehörige Touch-Screen-Bild-Kontrollsystem.


Das System wird durch einen Mikroprozessor gesteuert. Dieser führt Programmanweisungen aus zur Erfassung von Daten über den Kontakt des steuernden
Fingers mit dem Bildschirm, und zwar speziell von Richtung, Geschwindigkeit und
Zeitdauer des Berührkontakts; sowie zur Anzeige von „scroll format data capable of
display on said display screen“, d. h. von solchen Daten, die sich in Form z. B. einer
scrollbaren Liste auf dem Bildschirm darstellen lassen (Merkmale 1.1 bis 1.7 bzw.
8.1 bis 8.3, wobei sich Patentanspruch 8 nur allgemein auf „scrollable data“
bezieht).


4.2   Grundsätzlich soll, wenn der Benutzer den Bildschirm mit dem Finger berührt
und den Finger dann bewegt, das Anzeigebild der Fingerbewegung folgen. Wenn
jetzt der Finger vom Bildschirm gelöst wird, soll das Bild automatisch weiterbewegt
werden („scrolling displacement“ bzw. „scrolling motion“), wobei die Richtung und
Geschwindigkeit     der    Fingerbewegung        die   Verschiebungsrichtung      und
Anfangsgeschwindigkeit des Bildes bestimmen, jedoch dann die Scroll-Geschwindigkeit allmählich abnimmt (Merkmale 1.8.1 und 1.10, bzw. 8.4.1 und 8.6 – eine
solche automatische Weiterbewegung war als „kinetic scroll“ oder „inertial scroll“
bereits vorbekannt, vgl. Streitpatentschrift, Abs. [0005]). Für das Stoppen der
Bildbewegung sind in den Ansprüchen 1 und 8 drei Auslöser angegeben: das Bild
läuft solange weiter, bis das Ende der „scroll format data”, d. h. der anzeigbaren
Daten erreicht wird (Merkmal 1.11 b bzw. 8.7 b); oder bis der Benutzer die
Bewegung durch Berühren des Bildschirms manuell stoppt (Merkmale 1.9 bzw. 8.5,
sowie 1.11 a bzw. 8.7 a); oder bis die allmählich abnehmende Geschwindigkeit

                                          - 32 -



„Null“ erreicht (Merkmal 1.10, nicht in 8.6); auch diese Lehren waren vorbekannt,
siehe Streitpatentschrift, Abs. [0008].


Hinzu kommen folgende ergänzende Funktionen:


–      Wenn das Anzeigebild mit dem Finger in Bewegung gesetzt wurde, folgt,
solange der Benutzer den Finger nicht abhebt, das gesamte Bild dem Finger in
beliebiger Richtung („sticks to the finger" = „klebt am Finger“; siehe die Merkmale
1.8 und 1.12, bzw. 8.4 und 8.8); erst wenn der Finger abgehoben wird, startet die
automatische Weiterbewegung.


–      Wenn das Anzeigebild mit dem Finger in Bewegung gesetzt wurde, der
Finger sich aber zum Zeitpunkt des Lösens vom Bildschirm nicht bewegt, bleibt das
Bild in der erreichten Position stehen, und das System gelangt in einen "Warte"-
Status (Merkmale 1.12.1 und 8.8.1).


–      Wenn der Benutzer den Finger während der Berührung nicht bewegt, kann
er ein berührtes Bildelement dadurch „auswählen“ („select“), wobei ein ausgewähltes Element [optisch] hervorgehoben dargestellt werden soll (Merkmal 1.13
bzw. 8.9). Wenn er den berührenden Finger nach der Auswahl bewegt, folgt nur das
ausgewählte Bildelement der Spur des Fingers („touch dragging“) (siehe die
Unteransprüche 2 und 10).


–      Wenn dem Benutzer die Geschwindigkeit der automatischen Weiterbewegung nicht (mehr) zusagt, kann er durch eine erneute Wisch-Bewegung auf dem
sich bewegenden Bild mit anderer (höherer oder niedrigerer) Geschwindigkeit eine
Übernahme dieser neuen Geschwindigkeit auf die Bildbewegung veranlassen
(siehe Unteransprüche 3 und 11).


Stationäre Berührkontakte unterhalb einer bestimmten Mindestdauer können vom
System ignoriert werden (vgl. Streitpatentschrift, Abs. [0031]). Der Fachmann
versteht das so, dass derartige kurze Berührkontakte als Fehlbedienung oder als
durch ein „Störsignal“ entstanden interpretiert werden.

                                       - 33 -



4.3       Das Streitpatent selbst bezeichnet die meisten der genannten Einzelmaßnahmen „für sich betrachtet“ als vorbekannt. Die Leistung des Streitpatents besteht
nach dem Vortrag der Beklagten darin, ein Gesamtkonzept zu schaffen, welches
die Messwerte der Fingerberührung (Dauer, Geschwindigkeit, Richtung) und die
Informationen über den Anzeige-Zustand (stationäres oder scrollendes Bild) miteinander in Beziehung setzt und Vorgaben macht, welche Berührung unter welchen
Bedingungen welche weitere Funktion auslösen soll. Die Beklagte spricht in diesem
Zusammenhang von einer „Zustandsmaschine“; denn der Folgezustand des
Systems hängt nicht nur von den Messwerten der Fingerberührung, sondern auch
vom vorherigen Zustand (hier insbes.: scrollt das Bild oder nicht?) ab. Die Beschwerdekammer des EPA hat in der Entscheidung vom 30. Juni 2015, mit welcher
das Streitpatent erteilt wurde, eine Tabelle erstellt (Anlage NK5 Gliederungspunkt
1.1.3),     welche   für   den   Verfahrensanspruch 8   die   anspruchsgemäßen
Zusammenhänge zu beschreiben versucht. Weil diese aber nicht von der exakten
Merkmalsformulierung ausgeht und auch die Unterschiede zwischen den
Ansprüchen 1 und 8 nicht erkennen lässt, verwendet der Senat die folgenden
ergänzten und korrigierten Tabellen:

                                          - 34 -




Merkmal            Voraussetzung                        dann folgende Aktion:

                responsive to duration                     display is moved in

  1.8         of stationary finger touch,          correspondence with movement
             in period „ t1 < duration < t2 “              of the finger touch
             (any) motion of finger touch                („sticks to the finger“)

            display moving „sticked to the         initiate scrolling displacement
 1.8.1        finger“ (finger touch is “in             in direction of finger move and
            motion”) + separation of finger            at sensed initial speed of finger

                                                     reducing the rate of scrolling
  1.10          scrolling displacement
                                                        at a predetermined rate
                      + no touch
                                                       until motion is terminated

  1.9           scrolling displacement
                                                     solely stop scroll (no select)
                 + (any) finger touch

                scrolling displacement
 1.11 a        + stationary finger touch                        stop scroll
                      duration > t0

                scrolling displacement
 1.11 b          + end-of-scroll signal                         stop scroll
                   from data source

  1.12          responsive to duration                     display is moved in
 (ident.      of stationary finger touch,          correspondence with movement
             in period „ t1 < duration < t2 “              of the finger touch
  1.8)
             (any) motion of finger touch                („sticks to the finger“)

            display moving „sticked to the         display will remain in the position
 1.12.1    finger“, + no finger motion at the       it is at that time, without further
             time of separation of finger               motion; "waiting” status

                responsive to duration
  1.13        of stationary finger touch,            an item touched is selected;
               duration < t2 + no motion              selected item is highlighted
              before separation of finger

                                         - 35 -




Merkmal           Voraussetzung                         dann folgende Aktion:

            t1 < duration of (any) finger
                                                  moving said display in correspontouch < t2
  8.4                                             dence with movement of the finger
           + finger touch is accompanied
                                                      touch („stick to the finger“)
                     by motion

           display moving „sticked to the              initiate scrolling motion
 8.4.1       finger“ (finger touch is “in          of scrollable data, in direction of finger
           motion”) + separation of finger          move and at sensed speed of finger

                  scrolling motion
  8.6                                                     slowing scroll speed
                     + no touch

                  scrolling motion
  8.5                                                            stop scroll
                + (any) finger touch

                  scrolling motion
 8.7 a        + stationary finger touch                          stop scroll
               having a finite duration

                  scrolling motion
 8.7 b                                                           stop scroll
                + end-of-scroll signal

          t1 < duration of stationary finger      subsequent moving of said display
                      touch < t2                        in correspondence with
  8.8
           + finger touch is accompanied             movement of the finger touch
                     by motion                            („stick to the finger“)

           display moving „sticked to the         maintain display in the position it is
 8.8.1    finger“, + no finger motion at the      at that time, without further motion;
            time of separation of finger                     "waiting” status

               stationary duration of
                  finger touch < t2                   selecting an item touched;
  8.9
           + no motion before separation              selected item is highlighted
                      of finger

                                        - 36 -



4.4    Einzelaspekte


4.4.1 Wenn sich Merkmal 8.3 auf das Erfassen der Dauer einer Fingerberührungskontaktzeit „mit einem elektronischen Anzeigeschirm (40), der scrollbare
Daten darauf anzeigt“ („with an electronic display screen (40) having scrollable data
displayed thereon“) bezieht, obwohl zuvor die Merkmale 8.1 und 8.2 bereits einen
solchen Anzeigeschirm (40) und das Steuern der scroll-artigen Anzeige betrafen,
wird der Fachmann dem keine besondere Bedeutung beimessen; aus der
Beschreibung des Streitpatents ergibt sich ohne Weiteres, dass das Merkmal 8.3
lediglich ungeeignet formuliert ist und sich auf denselben Bildschirm und dieselben
scrollbaren Daten wie die Merkmale 8.1 und 8.2 bezieht.


4.4.2 Gemäß Merkmal 1.8 / 1.12 und sinngemäß ebenso Merkmal 8.4 / 8.8.1 soll
„die Anzeige“ zunächst in Übereinstimmung mit der Bewegung der Fingerberührung
bewegt werden („said display is moved in correspondence with …“). Dabei bezieht
sich „said display“ zurück auf Merkmal 1.5 „scroll format data capable of display on
said display screen (40)“ bzw. Merkmal 8.3 „display screen (40) having scrollable
data displayed thereon”; d. h. das Streitpatent unterscheidet zwischen dem Bild-Anzeigeschirm (40) und den darauf dargestellten Scroll-Daten. Dementsprechend
handelt es sich bei der „Anzeige“, die in Übereinstimmung mit der Bewegung der
Fingerberührung bewegt werden soll, nicht zwangsläufig um die gesamte
Bildschirmfläche, sondern um die dargestellten scrollbaren Daten; nur diese werden
durch die Formulierung „said display“ adressiert.


Die Beklagte vertritt eine andere Auffassung und verweist dazu auf die Beschreibung Spalte 6 Zeile 34, Zeile 58 und Spalte 7 Zeile 2, wonach „the entire display“
mit dem Finger bewegt werden solle. Auch hier stellt sich jedoch die Frage, ob mit
„display“ der gesamte Bildschirm oder nur der Datenanzeige-Bereich gemeint sein
soll (vgl. etwa Spalte 6 Zeile 47 / 48 „scrolling motion of the displayed data“; ferner
war dem Fachmann geläufig, dass auf einem Touch-Screen „feste“ Berührfelder für
permanent verfügbare Funktionen oder permanente Anzeigefelder vorgesehen sein
können, die nicht mitbewegt wurden). Vor allem aber hat die Formulierung „the

                                       - 37 -



entire display“ keine Aufnahme in die Patentansprüche gefunden, so dass der Senat
einer solchen Auslegung nicht folgt.


4.4.3 Was in Merkmal 1.9 ausgeschlossen sein soll („solely as a "stop motion"
signal“ = ausschließlich als "Stopp-Bewegung"), ergibt sich aus Abs. [0037] des
Streitpatents: „Although it has been stated above, that a relatively long-term finger
touch while scrolling motion is taking place serves as both a "selection" and a "stop
motion" signal, it will be obvious that the method could be set up easily so that a
finger touch during the scrolling process would act solely as a "stop motion" signal
regardless of the length of the touch; this would protect against the possibility of
unintended "selections" resulting from inadvertently long touches that were intended
only to "stop" the scrolling“. D. h. Merkmal 1.9 ist darauf gerichtet, dass während
einer Scroll-Verschiebung der Anzeige eine Fingerberührung, egal von welcher
Länge, ausschließlich das Stoppen der Scroll-Bewegung bewirken soll, aber keine
„Auswahl“.


4.4.4 Die Merkmale 1.8 und 1.12 sowie 8.4 und 8.8 beziehen sich auf eine Bewegung der Fingerberührung während einer Periode „größer als eine erste vorbestimmte Mindestzeit und kleiner als eine zweite vorbestimmte Mindestzeit“ (bzw.
„voreingestellte Mindestzeit“ – in der englischen Anspruchsfassung übereinstimmend: „first / second preset minimum time”). In der Diskussion wurde dafür die
Kurzformel „t1 < Δt < t2“ verwendet, wobei Δt die Dauer der Berührung bezeichnet.


Eine „second minimum time“ findet sich in der Beschreibung nur in Spalte 6 Zeile 38
und – darauf bezugnehmend – in Spalte 6 Zeile 44/45. Diese soll gemäß Spalte 6
Zeile 38 kürzer sein als die erste Mindestzeit. Das würde jedoch bedeuten, dass es
eine Periode mit einer Dauer größer als die erste, aber kleiner als die zweite Zeit
(die kürzer sein soll als die erste) nicht geben könnte; im Wege der Auslegung muss
daher davon ausgegangen werden, dass die „first preset minimum time” der
Ansprüche 1 und 8 der „second minimum time” des Abs. [0031] entspricht, und die
„second preset minimum time” der Ansprüche 1 und 8 der “first predetermined
minimum time” der Beschreibung.

                                          - 38 -



4.4.5 Nach Merkmal 1.11 a soll die Scroll-Verschiebung des Bildes auf dem
Anzeigeschirm beendet werden, wenn eine stationäre Fingerberührung erkannt
wird, die länger andauert als eine vorgegebene Mindestzeit („longer than a preset
minimum time“). In der Streitpatentschrift findet sich hierzu in Abs. [0020] „for a finite
period of time“, sowie „If a finger is applied to the surface of the screen for a shorter
period of time, for example for a period less than a minimum set time“; in Abs. [0025]
„for a predetermined period of time“. Jedenfalls gibt es keinen Hinweis, dass es sich
dabei um dieselbe Zeit t1, t2 wie die „first” oder „second preset minimum time” der
o.g. Merkmale 1.8 und 1.12 sowie 8.4 und 8.8 handeln könnte.


Scheinbar im Unterschied dazu verlangt das korrespondierende Merkmal 8.7 a für
die stationäre Fingerberührung „having a finite duration“. Nach dem Verständnis des
Senats drückt diese Formulierung „mit definierter Dauer“ aber nichts Anderes aus
als die Bedingung des Merkmals 1.11 a „länger als eine vorgegebene Mindestzeit“.
Die beiden Merkmale sind insoweit also gleich zu verstehen.


4.4.6 Alternativ soll nach Merkmal 1.11 b die Scroll-Verschiebung des Bildes auf
dem Anzeigeschirm beendet werden, wenn ein „Scroll-Ende-Signal“ von der Quelle
von Scroll-Formatdaten empfangen wird. Dieses zeigt an, dass das Ende der
darstellbaren Daten erreicht wurde, d. h. die letzten Daten der Liste angezeigt
worden sind (vgl. Streitpatentschrift Abs. [0021] „having reached the end of the
"scroll"“). Das Merkmal 8.7 b ist verallgemeinernd nur auf den Empfang eines
„Scroll-Ende-Signals“ gerichtet (ohne „received from said scroll format data
source“). Nachdem aber in der gesamten Streitpatentschrift kein anderes „Scroll-Ende-Signal“ erwähnt und auch nicht recht erkennbar ist, was der Fachmann sich
sonst darunter vorstellen könnte, sind auch hier die beiden Merkmale insoweit gleich
zu verstehen.


4.4.7 Die Beklagte hat vorgebracht, das Streitpatent unterscheide zwischen der
„Länge der Berührung“ („length of the touch“) in Merkmal 1.9 und der „Dauer“
(„enduring for a period longer than …“) in Merkmal 1.11 a. Wie Absatz [0037] des
Streitpatents jedoch vor Augen führt, werden die Begrifflichkeiten „duration of contact“ und „length of the touch“ synonym verwendet. Erkenntnisse für die Auslegung

                                        - 39 -



lassen sich zur Überzeugung des Senats aus der unterschiedlichen Formulierung
nicht gewinnen.


4.4.8 Die Merkmale 1.13 und 8.9 geben an, wie der Benutzer die Auswahl eines
einzelnen Objektes der Scroll-Liste bewirken kann („selection“ / Merkmal 1.13: „(…)
ein Element, welches berührt wird, ausgewählt wird, wobei das ausgewählte
Element bei Auswahl hervorgehoben wird“, Merkmal 8.9: „(…) des Auswählens
eines berührten Elementes … wobei das bei Auswahl ausgewählte Element hervorgehoben wird“). Das Streitpatent versteht unter „selection“ lediglich ein Markieren oder eine Vor-Auswahl, keine Auslösung einer Funktion (siehe Abs. [0030]: „(…)
selection path, beginning with (…) highlighting“; „the "selected" item (…) will "stick
to the finger").


4.4.9 Im Zuge dieser Merkmals-Auslegung ist auf einen in der Streitpatentschrift
enthaltenen offensichtlichen Fehler hinzuweisen. In Abs. [0036] heißt es: „If the
touch is stationary and the contact continues for less than a predetermined minimum
time (…). On the other hand, if the touch is stationary but the contact does not
continue for more than the minimum time (…)“. Offensichtlich sollte hier eine
Unterscheidung getroffen werden, die aber wegen inhaltlich übereinstimmender
Voraussetzungen („less“ = „not more“) nicht zustande kommt. Ein Vergleich mit Abs.
[0037] „(…) that a relatively long-term finger touch while scrolling motion is taking
place serves as both a "selection" and a "stop motion" signal (…)“ macht deutlich,
dass es in Spalte 7 Zeile 47 offenbar „continues for less MORE than a
predetermined minimum time” heißen sollte. Nach der Rechtsprechung des
Bundesgerichtshofs ist dieser offensichtliche Fehler zu korrigieren (vgl. etwa BGH
Mitt. 2002, 176 – Gegensprechanlage, II. 2. b) aa)).

                                     - 40 -



4.5    Zu berücksichtigende Unterschiede zwischen den Ansprüchen 1 und 8


4.5.1 Merkmal 8.4 gegenüber Merkmal 1.8


Nach Merkmal 1.8 soll die Dauer „des stationären Fingerberührungskontakts“
bestimmt werden, und „wenn während einer Periode mit einer Dauer (…) Bewegung
der Fingerberührung über die Oberfläche des Anzeigeschirms erfasst wird“, die
Anzeige zunächst „in Übereinstimmung mit der Bewegung der Fingerberührung
bewegt“ werden. Nach Merkmal 8.4 soll - ohne Beschränkung auf eine stationäre
Fingerberührung - „die (…) Dauer der Fingerberührungskontaktzeit“ erfasst werden,
und wenn diese Dauer die angegebene Zeit-Bedingung erfüllt „und von einer
Bewegung entlang der Oberfläche des Anzeigeschirms (40) begleitet wird“, soll ein
„Bewegen der Anzeige in Übereinstimmung mit der Fingerberührung“ erfolgen.


Hiervon ausgehend ist zur Überzeugung des Senats das Merkmal 8.4 nicht - wie
die Merkmale 1.8 und 8.8 - als beschränkt auf eine stationäre Fingerberührung
auszulegen. Denn es „darf im Nichtigkeitsverfahren nicht etwa deshalb eine
einengende Auslegung der angegriffenen Patentansprüche zugrunde gelegt
werden, weil mit dieser die Schutzfähigkeit eher bejaht werden könnte“ (BGH GRUR
2004, 47 – Blasenfreie Gummibahn I). Für eine einschränkende Auslegung besteht
hier kein Anlass, weil die beanspruchte Lehre auch bei sich bewegendem Finger
sinnvoll sein kann, selbst wenn kein konkretes Ausführungsbeispiel dazu gegeben
sein sollte.


4.5.2 Merkmal 8.5 gegenüber Merkmal 1.9


Nach Merkmal 1.9 soll das Erfassen einer Fingerberührung während der Scroll-Verschiebung des Bildes auf dem Anzeigeschirm ausschließlich als "Stopp-Bewegung" funktionieren, unabhängig von der Dauer der Berührung. Nach Merkmal
8.5 soll das Erfassen einer Fingerberührung während der Scroll-Verschiebung des
Bildes auf dem Anzeigeschirm, unabhängig von der Dauer der Berührung, ein
Stoppen der Bewegung der Anzeige bewirken – aber nicht „ausschließlich“.

                                       - 41 -



Wie oben bereits ausgeführt (siehe Abschnitt 4.4.3) ist Merkmal 1.9 so zu verstehen,
dass eine Fingerberührung während einer Scroll-Bewegung der Anzeige, welche
das Stoppen der Scroll-Bewegung bewirken soll, vom System nicht zusätzlich noch
für einen anderen Zweck, insbesondere nicht als „Auswahl“ interpretiert werden
darf.


Beim Merkmal 8.5 fehlt jedoch der Begriff „ausschließlich“ („solely“), d. h. die Formulierung erlaubt hier, dass zusammen mit dem Stoppen der Scroll-Verschiebung
auch das berührte Element „ausgewählt“ werden könnte.


Nachdem eine solche Lehre „brauchbar“ ist und nicht im Widerspruch zu anderen
Anspruchsmerkmalen steht, besteht für eine einschränkende Auslegung des
Merkmals 8.5 kein Anlass (vgl. oben Abschnitt 4.5.1 und den Bezug auf die BGH-Entscheidung Blasenfreie Gummibahn I).



4.6     Widersprüche in Anspruchsmerkmalen


Nach der Rechtsprechung des Bundesgerichtshofs „ist die Patentschrift in einem
sinnvollen Zusammenhang zu lesen und der Patentanspruch im Zweifel so zu verstehen, dass sich keine Widersprüche zu den Ausführungen in der Beschreibung
und den bildlichen Darstellungen in den Zeichnungen ergeben (…). Diese Maßgabe
für die Auslegung gilt erst recht zur Vermeidung von Widersprüchen zwischen
mehreren Merkmalen eines Patentanspruchs“ (BGH GRUR 2018, 1128 – Gurtstraffer, Tz. 16).


4.6.1 Merkmal 1.9 bzw. 8.5 gegenüber Merkmal 1.11 a bzw. 8.7 a


Nach Merkmal 1.9 soll das Erfassen einer Fingerberührung während der Scroll-Verschiebung des Bildes auf dem Anzeigeschirm ausschließlich als "Stopp-Bewegung" funktionieren, unabhängig von der Dauer der Berührung; nach Merkmal 1.11
a soll hingegen eine im Wesentlichen stationäre Fingerberührung auf dem
Anzeigeschirm das Beenden der Scroll-Verschiebung des Bildes bewirken, wenn

                                        - 42 -



sie für einen Zeitraum andauert, der länger ist als eine vorgegebene Mindestzeit.
Ähnlich soll nach Merkmal 8.5 eine Fingerberührung während der Scroll-Verschiebung des Bildes, unabhängig von der Dauer der Berührung, die Bewegung
der Anzeige stoppen; gemäß Merkmal 8.7 a erfordert das Beenden der Scroll-Bewegung eine im Wesentlichen stationäre Berührung mit definierter Dauer.


Die Beklagte möchte Merkmal 1.9 einschränkend auslegen im Sinne einer Unteroder Nachordnung gegenüber Merkmal 1.11 a, dass also eine stationäre Fingerberührung länger als eine vorgegebene Mindestzeit während des Scrollens
„reserviert“ sein solle für „stop motion“, so dass (nur) die stationäre Berührung
gemäß Merkmal 1.11 a ausschließlich als "Stopp-Bewegung" funktionieren solle –
das schließe aber nicht aus, dass kurze Fingerberührungen ignoriert werden
könnten, und gelte nicht für bewegte Fingerberührungen.


a)      „Stationäre“ Fingerberührungen zum Stoppen der Scroll-Bewegung lassen
sich zwar anhand der Beschreibung des Streitpatents belegen (siehe Abs. [0020]
„Motion of the displayed image may be stopped manually by applying a finger to the
screen without moving it along the surface of the screen for a finite period of time“;
Abs. [0037] „duration of contact for a stationary finger touch on the screen serves
as the distinction between a "selection" touch and a "stop scrolling" touch”).
Allerdings besteht bei einer am Wortlaut orientierten Auslegung des Merkmals, die
darüber hinaus auch einen bewegten Finger einbezieht, kein Widerspruch zu
anderen Merkmalen (die Merkmale 1.8, 1.12 und 1.13 betreffen einen „stationären“
Finger, wie auch die Unteransprüche 3 und 11 zwar einen sich bewegenden Finger
betreffen, dessen Bewegung aber auf eine bestimmte stationäre Berührung folgt);
die Lehre des Merkmals 1.9 „funktioniert“ auch bei bewegtem Finger, so dass für
eine einschränkende Auslegung kein Anlass besteht.


Analog gilt für Merkmal 8.5, dass seine Lehre auch bei bewegtem Finger
„funktioniert“ und somit nicht unter ihrem Wortlaut auszulegen ist.

                                          - 43 -



b)      Eine Auslegung, wonach sich das Merkmal 1.9 („acts solely as “stop
motion”“) nur auf die Fingerberührungen des Merkmals 1.11 a beziehen sollte, lässt
sich bei Heranziehung der Beschreibung nicht rechtfertigen.


Die Teil-Lehre „acts solely as “stop motion”“ des Merkmals 1.9 wird allein in
Abs. [0037] des Streitpatents erläutert. Dort geht es darum, dass anhand der
Berührdauer zwischen „Auswahl“ und „stopp scrolling“ unterschieden werden soll
(„the duration of contact for a stationary finger touch on the screen serves as the
distinction between a "selection" touch and a "stop scrolling" touch“); alternativ
könnte eine Fingerberührung während des Scrollens „allein“ als Stopp-Signal
interpretiert werden, um die Gefahr unbeabsichtigter Auswahlen durch zu lange
Berührungen zu vermeiden. D. h. das Streitpatent beschreibt an dieser Stelle zwei
Alternativen, die sich gegenseitig ausschließen. Das Merkmal 1.9 bezieht sich
eindeutig auf die zweite Alternative, wonach also zur Vermeidung unbeabsichtigter
„Select“-Funktionen eine (gemäß Beschreibung: stationäre) Berührung während
des Scrollens, unabhängig von ihrer Dauer („regardless of the length of the touch“),
in keinem Fall als „select“ interpretiert werden soll. Dass dies nur für Berührungen
„länger als eine vorgegebene Mindestzeit“ gelten sollte, lässt sich Abs. [0037] nicht
entnehmen.


Auf der anderen Seite ergibt sich die Lehre, dass kurze Fingerberührungen ignoriert
werden könnten, allein aus Abs. [0031] des Streitpatents („In another feature, if no
motion of the finger occurs while the screen is stationary, and the contact continues
for less than a second minimum time which is less than the first minimum time by a
readily measurable finite value, then step 100 ignores the contact” – wird in
Abs. [0032] noch einmal aufgegriffen); sie bezieht sich deutlich nur auf einen stationären, d. h. nicht scrollenden Bildschirm, und gerade nicht auf die Voraussetzung
einer Scroll-Verschiebung gemäß Merkmal 1.9.


Auch Abs. [0020] (Spalte 4 Zeile 30 bis 33) „Motion of the displayed image may be
stopped manually by applying a finger (…) for a finite period of time“ hilft nicht weiter,
weil dies im Gegensatz steht zu Spalte 4 Zeile 33 ff. „If a finger is applied to the
surface of the screen for a shorter period of time, for example for a period less than

                                       - 44 -



a minimum set time, the finger touch can be deemed to be a "selection"(…)” – d. h.
hier wird eine „kürzere“ Berührung als „Auswahl“ erkannt (was der ersten, nicht
unter Schutz gestellten Alternative aus Abs. [0037] entspricht). Eine konkrete Lehre,
dass kurze Fingerberührungen während des Scrollens ignoriert werden könnten,
gibt das Streitpatent nicht. Damit verbietet sich aber eine Auslegung, dass sich
Merkmal 1.9 auf die Fingerberührungen „länger als eine vorgegebene Mindestzeit“
des Merkmals 1.11 a beziehen könnte, oder dementsprechend das Merkmal 8.5
einen Unterfall der „Fingerberührung mit definierter Dauer“ des Merkmals 8.7 a
darstellen könnte.


c)      Der Widerspruch kann nur dahingehend aufgelöst werden, dass umgekehrt
das Merkmal 1.11a dem Merkmal 1.9, und das Merkmal 8.7 a dem Merkmal 8.5
nachgeordnet ist, wie es auch der Reihenfolge im jeweiligen Anspruch entspricht.


Die Merkmale 1.9 und 8.5 zielen explizit auf eine Berührung „unabhängig von der
Dauer“ ab. Eine ausdrückliche Verknüpfung mit den im Anspruch 1 bzw. 8 nachfolgenden Merkmalen 1.11 a und 8.7 a und deren Einschränkung für die Berührdauer ist nach dem Anspruchswortlaut nicht gegeben. Es besteht auch sonst kein
Anhalt, die Merkmale 1.11 a und 8.7 a als den allgemeiner gefassten Merkmalen
1.9 und 8.5 übergeordnet zu verstehen und damit letztere unter ihrem Wortlaut
auszulegen. Die Wiederholung in Form der Merkmale 1.11 a und 8.7 a mit einer
Einschränkung für die Berührdauer mag der Fachmann als eine mögliche weitere
neben den Merkmalen 1.9 und 8.5 stehende Ausführungsvariante, die aber dann
von diesen Merkmalen (weil dort „unabhängig von der Dauer“) bereits umfasst ist,
oder als Überbestimmung auffassen.


Dies führt dazu, dass den Merkmalen 1.11 a und 8.7 a keine über eine bereits
umfasste Ausführungsvariante hinausgehende Bedeutung zukommt.


d)      Die Ansicht der Beklagten, dass eine solche Auslegung den Grundsätzen
der systematischen Anspruchsauslegung widerspreche, teilt der Senat nicht. Die
Beklagte hat insoweit auf die Entscheidung BGH GRUR 2011, 129 - Fentanyl-TTS
hingewiesen, wonach es sich verbiete, einen vermeintlichen Widerspruch

                                       - 45 -



dahingehend aufzulösen, dass einem Merkmal keine Bedeutung beigemessen
werde.


Damit ist der Leitsatz der Entscheidung allerdings unvollständig zitiert: „Ein
vermeintlicher Widerspruch zwischen Angaben im kennzeichnenden Teil und
Merkmalen des Oberbegriffs darf nicht dahin aufgelöst werden, dass den
Merkmalen des Oberbegriffs keine Bedeutung beigemessen wird, obwohl der
Wortsinn des Patentanspruchs eine widerspruchsfreie Auslegung zulässt und diese
durch die in der Beschreibung geschilderten Ausführungsbeispiele nahegelegt
wird.“


An letzterem fehlt es im vorliegenden Fall: Wie oben unter b) ausgeführt, kann der
Beschreibung eben nicht entnommen werden, dass kurze Fingerberührungen
während des Scrollens ignoriert werden könnten. Ferner ist die von der Beklagten
favorisierte Auslegung auch nicht „widerspruchsfrei“, denn sie würde beim Unteranspruch 4 zu dem gleichen Widerspruch aus anderer Perspektive führen: Gemäß
Unteranspruch 4 soll die Scroll-Bewegung des Bildschirms zusätzlich noch beendet
werden bei Vorliegen folgender Bedingung: „(c) a substantially stationary finger
touch on the display screen (40) enduring for a period shorter than or equal to said
preset minimum time“ – d. h. nach Merkmal 1.11 a wird das Scrollen durch eine
stationäre Fingerberührung länger als eine „preset minimum time“ beendet, nach
Unteranspruch 4 durch eine stationäre Fingerberührung kürzer oder gleich
derselben „preset minimum time“; zusammengefasst beendet somit jede stationäre
Fingerberührung unabhängig von ihrer Dauer das Scrollen, die „preset minimum
time“ hätte dann ebenfalls keine Bedeutung mehr.


Als weiteres Gegenargument macht die Beklagte geltend, das Streitpatent
unterscheide zwischen der „Länge der Berührung“ („length of the touch“) in Merkmal
1.9 und der „Dauer“ („enduring for a period longer than (…)“) in Merkmal 1.11 a.
Dem konnte der Senat jedoch, wie oben bereits in Abschnitt 4.4.7 ausgeführt,
aufgrund der synonymen Verwendung in Abs. [0037] des Streitpatents nicht folgen.

                                         - 46 -



4.6.2 Merkmal 1.13 gegenüber Merkmal 1.9


Nach Merkmal 1.13 soll eine stationäre Fingerberührung, deren Dauer kleiner ist als
die zweite voreingestellte Mindestzeit, wenn keine Bewegung vor dem Lösen des
Fingers von dem Anzeigebildschirm auftritt, ein berührtes Element auswählen; diese
Lehre umfasst offensichtlich auch Fingerberührungen während der Scroll-Verschiebung des Bildes. Nach Merkmal 1.9 soll eine Fingerberührung während der
Scroll-Verschiebung des Bildes (unabhängig von der Dauer der Berührung)
ausschließlich als "Stopp-Bewegung", d. h. nicht als „Auswahl“ („select“) fungieren.


Da sich die Merkmale 1.13 und 1.9 für den Fall einer Scroll-Verschiebung des Bildes
widersprechen, ist die beanspruchte Lehre insoweit „nicht ausführbar“. Die Beklagte
möchte Merkmal 1.13 einschränkend so auslegen, dass es einen stationären (nichtscrollenden) Bildschirm voraussetze.


Nachdem sich auch in der Beschreibung eine solche Einschränkung finden lässt
(vgl. Abs. [0029] / [0030]: „(…) to begin in step 100 with sensing the touch of a finger
upon electronic display screen 100a having a stationary data display (…). If
no motion occurs and the touch contact continues for less than a as to a predetermined minimum time, the touch is treated in step 100 as a "selection" of the data
term touched”), ist der Widerspruch daher in diesem Sinne aufzulösen: Merkmal
1.13 ist so auszulegen, dass es sich auf ein stationäres Display bezieht.


Für das Verfahrensmerkmal 8.9, welches dem Merkmal 1.13 entspricht, ist ein
solcher Widerspruch nicht festzustellen, weil das dem Merkmal 1.9 entsprechende
Verfahrensmerkmal 8.5 die Einschränkung „solely“ nicht enthält und somit eine
„Auswahl“ nicht ausschließt, vgl. oben Abschnitt 4.5.2.

                                       - 47 -



                                         II.


Das Streitpatent hat in seiner erteilten Fassung keinen Bestand. Denn der
Gegenstand der unabhängigen Patentansprüche 1 und 8 geht über den Inhalt der
Anmeldung in ihrer ursprünglich eingereichten Fassung hinaus (Art. II § 6 Abs. 1
Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ).


Folgende    Merkmale    der   Patentansprüche 1     und 8    sind   gegenüber    der
ursprünglichen Offenbarung (vgl. PCT-Anmeldung WO 2003 / 060 622 A2, Anlage
NK4) unzulässig erweitert:


1.    Merkmal 1.9


Wie bereits ausgeführt (s. o. I., Abschnitt 4.6.1 a)), ist die als "Stopp-Bewegung"
funktionierende Fingerberührung gemäß Merkmal 1.9 ihrem Wortlaut nach nicht auf
„stationäre“ Fingerberührungen beschränkt. Die spezielle Lehre („acts solely as
"stop motion" regardless of the length of the touch“) kann sich jedoch ausschließlich
auf die Offenbarung auf Seite 6 Zeile 12 bis 19 der NK4 stützen; diese Passage
betrifft aber laut Zeile 13 nur „a stationary finger touch“, und auch der folgende
Absatz (Zeile 20) beginnt mit „In contrast to stationary touching (…)“. Eine Lehre,
wonach auch ein bewegter Finger „ausschließlich als "Stopp-Bewegung"“
interpretiert werden könnte, so wie es vom Merkmal 1.9 umfasst ist, lässt sich der
Anmeldung nicht entnehmen.


2.    Merkmal 8.5


a)    Zwar enthält das dem Merkmal 1.9 entsprechende Verfahrens-Merkmal 8.5
nicht den Ausdruck „solely” - wohl aber die Formulierung „regardless of the length
of the touch“. Hierfür findet sich kein anderer Offenbarungsort als die o. g. Seite 6
Zeile 12 bis 19 der NK4, welche – wie ausgeführt – nur eine stationäre
Fingerberührung betrifft. Eine Lehre, wonach auch eine sich bewegende
Fingerberührung während der Scroll-Verschiebung des Bildes, unabhängig von der

                                       - 48 -



Dauer der Berührung, ein Stoppen der Bewegung der Anzeige bewirken würde, so
wie es vom Merkmal 8.5 umfasst ist, lässt sich der Anmeldung nicht entnehmen.


b)    Wie zuvor festgestellt, kann sich die Bedingung des Merkmals 8.5 „regardless of the length of the touch“ allein auf die Passage Seite 6 Zeile 12 bis 19 der
NK4 stützen. Dort werden zwei sich ausschließende Alternativen beschrieben,
nämlich dass entweder anhand der Berührdauer zwischen „Auswahl“ und „Stopp
Scrolling“ unterschieden werden soll (was aufgrund der Formulierung „regardless of
the length of the touch“ offensichtlich nicht Gegenstand des Merkmals 8.5 ist), oder
dass eine Fingerberührung während des Scrollens – unabhängig von ihrer Dauer –
„ausschließlich“ als Stopp-Signal interpretiert wird (und nicht als Auswahl), um
unbeabsichtigtes Auswählen durch zu lange Berührungen zu vermeiden.


Durch das Fehlen von „ausschließlich“ („solely“) umfasst das Merkmal 8.5 jedoch
den Fall, dass gleichzeitig mit dem Stoppen der Scroll-Verschiebung auch das berührte Element „ausgewählt“ werden könnte. Eine solche Lehre lässt sich der
Anmeldung jedoch nicht entnehmen.


Aus diesem Grund gehen die Patentansprüche 1 und 8 über den Inhalt der
Anmeldung in ihrer ursprünglich eingereichten Fassung hinaus. In seiner erteilten
Fassung hat das Streitpatent daher keinen Bestand.




                                        III.


In seiner Fassung nach Hilfsantrag I hat das Streitpatent ebenfalls keinen Bestand.
Denn der Gegenstand der unabhängigen Patentansprüche 1 und 8 in ihrer Fassung
nach Hilfsantrag I geht ebenso über den Inhalt der Anmeldung in ihrer ursprünglich
eingereichten Fassung hinaus (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138
Abs. 1 Buchst. c) EPÜ).

                                         - 49 -



In   ihrer   Fassung     nach   Hilfsantrag I   werden   die   beiden   unabhängigen
Patentansprüche in ihren Merkmalen 1.13 und 8.9 durch folgende markierte
Zusatzbedingungen ergänzt:


1.13x    „ (…) responsive to said duration of said stationary finger touch
         contact on said display screen (40) having a stationary data display,
         such that, when said duration is less than (…)”


         bzw.


8.9x     „ (…) if the sensed stationary duration of the finger touch contact
         time on said display screen (40) having a stationary data display, is
         less than (…)”.


Damit wird einer der erläuterten Widersprüche zwischen den Anspruchsmerkmalen
aufgelöst, indem die Merkmale 1.13 und 8.9 auf ein stationäres, d. h. nicht
scrollendes Display beschränkt werden, so wie es bereits der Auslegung entspricht
(s. o. I., Abschnitt 4.6.2).


Diese beiden Ergänzungen sind zulässig, da sie eine Beschränkung des erteilten
Patents im Rahmen der ursprünglichen Offenbarung bewirken (vgl. Streitpatent,
Abs. [0029] und [0030]).


Die zuvor (s. o. II.) dargestellte unzulässige Erweiterung hinsichtlich der Merkmale
1.9 und 8.5 wird damit aber nicht behoben. Auch in ihrer Fassung nach Hilfsantrag I
gehen die Patentansprüche 1 und 8 damit unverändert über den Inhalt der
Anmeldung in ihrer ursprünglich eingereichten Fassung hinaus. Auch in dieser
Fassung ist Streitpatent daher nicht patentfähig.

                                        - 50 -



                                             IV.


In seiner Fassung nach Hilfsantrag II, wie auch nach den gleich zu beurteilenden
Hilfsanträgen IIa, IIb und IIc, hat das Streitpatent ebenfalls keinen Bestand.


Der Gegenstand der unabhängigen Patentansprüche 1 und 8 in der Fassung nach
Hilfsantrag II beruht nicht auf erfinderischer Tätigkeit (Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 56 EPÜ). Angesichts dessen kann
dahinstehen, ob der Gegenstand des Streitpatents in der Fassung nach
Hilfsantrag II, wie die Klägerin geltend macht, gegenüber der ursprünglich
offenbarten Fassung zudem unzulässig erweitert ist. Auch auf eine möglicherweise
mangelnde Ausführbarkeit der Lehre des Unteranspruchs 4 kommt es nicht an.


1.     Die Fassung des Streitpatents nach Hilfsantrag II enthält die entsprechend
der Fassung des Hilfsantrags I geänderten Merkmale 1.13x und 8.9x. Zusätzlich
erhalten die Merkmale 1.9 und 8.5 folgende Fassung (Änderungen markiert):


1.9x    „wherein sensing a stationary finger touch during scrolling displacement of the image on said display screen (40) acts solely as
        "stop motion" regardless of the length of the touch;”


8.5x    “upon sensing a stationary finger touch during scrolling displacement of the image on said display screen (40), regardless of the
        length of the touch, stopping the motion of said display, wherein the
        finger touch acts solely as "stop motion";”


Durch diese Ergänzungen werden die zuvor in II. erläuterten „unzulässigen
Erweiterungen“ der Merkmale 1.9 und 8.5 in zulässiger Weise behoben.


2.     Der Gegenstand des Patentanspruchs 1 in der Fassung nach Hilfsantrag II
beruht nicht auf erfinderischer Tätigkeit.

                                        - 51 -



2.1   Der Streitpatentschrift lässt sich entnehmen (s. o. I., Abschnitt 1.), dass die
einzelnen Bedienungsmaßnahmen des Patentanspruchs 1 „für sich betrachtet“ aus
dem Stand der Technik vorbekannt waren.


a)    Die    Druckschrift   D1   (EP 0 626 635 A2)     beschreibt    eine   grafische
Benutzerschnittstelle für ein Fernsteuerungs-Gerät 170 (Figur 1a / 1b) insbesondere
mit einem berührungsempfindlichen Bildschirm (siehe z. B. Spalte 9 Zeile 20 bis 25,
Spalte 10 Zeile 47 bis 55). Dabei werden verschiedene Arten der Berührung durch
den Benutzer („Gesten“) unterschieden und diesen jeweils unterschiedliche
Funktionalitäten zugeordnet (Spalte 21 Zeile 25 ff.: „Point“, „Select“, „Pan“, „Spin“,
„Pickup“, „Drop“).


Eine mögliche Anwendung geht von einem „Object Wheel“ aus, welches eine
scrollbare Liste mit einer Vielzahl von Elementen auf dem Bildschirm darstellt, die
durch Berührungen in Bewegung versetzt werden kann, bis ein gewünschtes
Element auf dem Bildschirm erscheint; dieses kann dann z. B. ausgewählt werden
(vgl. Figur 11 bis Figur 16a). Zum Auslösen der Scroll-Verschiebung der Anzeige
dient die „Spin“-Geste (Spalte 23 Zeile 32 ff.): der Finger berührt das „Object Wheel“
[an beliebiger Stelle], und wenn der Finger parallel zur Richtung der möglichen
Drehung bewegt wird, „folgt“ das „Object Wheel“ dem Finger, d. h. die Elemente der
Liste werden über den Bildschirm „gerollt“ („scroll“). Je schneller der Finger sich
bewegt, umso schneller dreht sich das Rad. Ferner ist an anderer Stelle
beschrieben, dass sich die Drehbewegung des „Object Wheel“ mit der Zeit
verlangsamt, so wie ein reales Rad durch Reibung abgebremst wird (Spalte 20
Zeile 56 bis Spalte 21 Zeile 5). Gemäß Spalte 21 Zeile 15 bis 17 kann das drehende
Rad durch einfaches Berühren eines seiner Objekte jederzeit angehalten werden.
Dabei wählt eine einfache Berührung eines Objektes („Point“-Geste, Spalte 21 Zeile
54 bis Spalte 22 Zeile 12) das Objekt aus (entspr. dem „select“ des Streitpatents);
wenn aber die Berührung länger als eine bestimmte Mindestzeit andauert, wird die
dem Objekt zugeordnete Funktion ausgelöst („Select“-Geste, siehe Spalte 22
Zeile 14 bis 36, insbes. Zeile 32 bis 34: „If the object is a button, then the method
invoked performs a function associated with the button“ – d. h. „select“ wird hier
anders verstanden als im Streitpatent, s. o. I., Abschnitt 4.4.8). Dabei dient die

                                        - 52 -



Dauer der Berührung zur Unterscheidung zwischen „Point“ und „Select“ (Spalte 22
Zeile 26 ff.: „If the user continues to Point to the object for a predetermined minimum
period of time, the object becomes Selected“).


b)     Es gehörte zum Grundwissen des Fachmanns, dass bei der Auswertung
einer Fingerberührung sinnvollerweise eine untere und eine obere Zeitgrenze zu
berücksichtigen ist (Zeit-Bedingung „t1 < ∆t < t2“).


So war es lange schon üblich, zu kurze Berührungen zu ignorieren (vgl. beispielhaft
die Druckschrift D7 (US 5 864 105 A) Spalte 3 Zeile 49 ff.: „For example, a debounce
capability is provided to eliminate short, transient signals. A time delay (e.g., 0.5
second) is provided to ignore a first portion of a touch indicating signal to permit a
certain amount of unintended touch to the touch pad 22.”). Ebenso ist klar, dass ein
technisches System nicht „endlos“ auf das Ende einer Berührung warten darf (vgl.
– ebenfalls beispielhaft – die Druckschrift D7, Spalte 3 Zeile 53 ff.: “Also, a touch
indicating signal existing for an inordinate duration is ignored. Such an extended
duration signal may result from an article being jammed against the touch pad 22
(e.g., an umbrella or flashlight stored next to the touch pad)“. Damit beschreibt die
Schrift D7 die Zeit-Bedingung „t1 < ∆t < t2“.


c)     In Bezug auf Anspruch 1 des Streitpatents findet sich in der Druckschrift D1
ein Touch-Screen-Bild-Scrollsystem mit einem Bild-Anzeigeschirm (37) und einem
Mikroprozessor (30) zur Verarbeitung interaktiver Eingangssignale und zur
Steuerung der Anzeige, der, wie der Fachmann weiß, Timer-Mittel für eine Timer-Funktionalität aufweist. Gleiches gilt für eine Quelle für Scroll-Formatdaten, die zur
Anzeige auf dem Anzeigeschirm (37) geeignet sind (siehe Figur 1b und zugehörige
Beschreibung, Figur 9 bis 11 und Spalte 31 Zeile 35 bis 48 i. V. m. „Object Wheel“
Spalte 20 Zeile 26 bis 36 – Merkmale 1.1 bis 1.5); wobei der Mikroprozessor
Programmanweisungen ausführt zur Erfassung von Geschwindigkeit, Richtung und
Zeitdauer eines Fingerberührungskontaktes mit dem Bildschirm (siehe z. B. Spalte
23 Zeile 50 / 51; Spalte 23 Zeile 5 bis 10, Zeile 43 / 44; Spalte 22 Zeile 26 bis 28 –
Merkmale 1.6 und 1.7).

                                              - 53 -



d)       Darüber hinaus ist der Patentanspruch 1 gemäß Hilfsantrag II, basierend auf
der Auslegung (s. o. I., Abschnitt 4.), auf folgende Maßnahmen gerichtet:


Merkmal                Voraussetzung                        dann folgende Aktion:

                    responsive to duration                     display is moved in

      1.8         of stationary finger touch,          correspondence with movement
                 in period „ t1 < duration < t2 “              of the finger touch
                 (any) motion of finger touch                („sticks to the finger“)

                display moving „sticked to the         initiate scrolling displacement
     1.8.1        finger“ (finger touch is “in             in direction of finger move and
                motion”) + separation of finger            at sensed initial speed of finger

                                                         reducing the rate of scrolling
      1.10          scrolling displacement
                                                            at a predetermined rate
                          + no touch
                                                           until motion is terminated

      1.9x          scrolling displacement
                                                         solely stop scroll (no select)
                   + stationary finger touch

                    scrolling displacement
     1.11 a        + stationary finger touch                        stop scroll
                          duration > t0

                    scrolling displacement
     1.11 b          + end-of-scroll signal                         stop scroll
                       from data source

      1.12          responsive to duration                     display is moved in
     (ident.      of stationary finger touch,          correspondence with movement
                 in period „ t1 < duration < t2 “              of the finger touch
      1.8)
                 (any) motion of finger touch                („sticks to the finger“)

                display moving „sticked to the         display will remain in the position
     1.12.1    finger“, + no finger motion at the       it is at that time, without further
                 time of separation of finger               motion; "waiting” status

     1.13x          responsive to duration               an item touched is selected;
                of stationary finger touch on a           selected item is highlighted

                                           - 54 -




                  stationary data display,
                 duration < t2 + no motion
                before separation of finger



e)     Diese einzelnen Maßnahmen waren dem Fachmann bekannt:


–      Die Zeitbedingung „t1 < duration < t2 “ für die Berührdauer der Merkmale 1.8
und 1.12 war dem Fachmann vertraut, siehe oben b) und die Fundstellen in
Druckschrift D7. Dies betrifft gleichermaßen die Zeitbedingung in Merkmal 1.13x,
wobei eine Unterscheidung zweier auszulösender Aktionen anhand der Berührdauer schon in Druckschrift D1 vorgenommen wird (Unterscheidung zwischen der
„Point“- und „Select“-Geste, siehe D1 Spalte 22 Zeile 26 ff.).


–      Das sog. „touch dragging“, also das Verschieben der Anzeige in Übereinstimmung mit der Bewegung des berührenden Fingers entsprechend dem zweiten
Teil der Merkmale 1.8 und 1.12, ist in D1 nur „gegenläufig“ beschrieben („Pan“-
Geste, siehe D1 Spalte 23 Zeile 4 bis 13: „If a user places his finger on the background of Figure 4 and then slides the finger on the touch screen to the right, the
view will correspondingly pan to the right by moving the background image of the
Space and all the objects within the Space to the left.“). Das Streitpatent selbst
verweist hierzu jedoch in Abs. [0006] auf die Druckschrift D2 (EP 0 880 091 A); dort
ist in Spalte 5 Zeile 24 bis 30 beschrieben, wie die dargestellte Liste 12 dem Finger
17 über die Oberfläche der Anzeige folgt. Das Gleiche lässt sich der Druckschrift
D3 („Computer Graphics“, 1984), Seite 198 linke Spalte Mitte entnehmen („The
button follows the finger until the finger lifts off the screen“).


–      Das Scrollen von Scroll-Formatdaten auf einem Touch Screen entsprechend
den Merkmalen 1.8.1 und 1.10, ausgelöst durch Fingerbewegung, wobei die
Geschwindigkeit und Richtung einer Fingerberührung die anfängliche Scroll-Geschwindigkeit und -Richtung der Scroll-Verschiebung der Anzeige bestimmt, und
wobei die Geschwindigkeit der Scroll-Verschiebung gemäß einer vorbestimmten
Rate automatisch verringert wird, ist in der Druckschrift D1 vorbeschrieben (s. o. a):

                                        - 55 -



„Object Wheel“). Alternativ verweist das Streitpatent selbst in Abs. [0008] dazu auf
Druckschrift D2.


–     Das Stoppen der Scroll-Verschiebung der Anzeige i. S. d. Merkmals 1.9x,
wenn während der Scroll-Verschiebung eine Fingerberührung, egal welcher Länge,
erkannt wird, war aus der Druckschrift D1 Spalte 21 Zeile 15 bis 17 vorbekannt.
Alternativ verweist das Streitpatent selbst dazu in Abs. [0005] und in Abs. [0008] auf
die Druckschrift D2.


–     Auch das „Auswählen“ von Bildschirm-Objekten durch Berührung, wie es Teil
von Merkmal 1.13x ist, war dem Fachmann am Prioritätstag des Streitpatents
hinlänglich bekannt, siehe dazu die Schrift D1 Spalte 21 Zeile 55 ff. („Point“-Geste).
Die Entgegenhaltung D1 beschreibt eine akustische Rückmeldung für den Erfolg
(Spalte 22 Zeile 10 bis 12) – das beanspruchte „highlighting“ nach Merkmal 1.13x
stellt eine entsprechende optische Rückmeldung dar, die im gegebenen Kontext für
den Fachmann nahe lag.


f)    Nicht unmittelbar dem zitierten Stand der Technik entnehmen lässt sich die
Lehre des Merkmals 1.12.1, wonach nach einer Bewegung der Anzeige in Übereinstimmung mit der Bewegung der Fingerberührung (s. o. zu den Merkmalen 1.8
und 1.12) der Bildschirm stehenbleibt und das System in einen „Warte“-Status
zurückkehrt, wenn keine Fingerbewegung zu dem Zeitpunkt erfasst wird, an dem
der Berührkontakt abbricht. Jedoch lässt sich dies beispielsweise aus der Lehre der
Schrift D1 zur „Spin“-Geste ableiten, wonach sich das Rad umso schneller dreht, je
schneller der Finger über den Touch Screen bewegt wird (D1 Spalte 23 Zeile 49 bis
53); denn dann wird ein stehengebliebener Finger (mit der Geschwindigkeit „Null“)
zwangsläufig eine Scroll-Verschiebung mit der Geschwindigkeit „Null“, d. h. keine
Scroll-Verschiebung    erzeugen,    und    notwendigerweise     „wartet“   dann   die
Fingerberührungserkennung auf nachfolgende Berührungen. Dasselbe lässt sich
aus der Druckschrift D2 ableiten (siehe dort z. B. den Anspruch 3 „(…) to scroll at a
rate measured for a vertical speed of said pointing means (17) at the last moment
before it was removed“).

                                       - 56 -



g)     Ebenfalls dem vorliegenden Stand der Technik nicht entnehmen lässt sich
eine Beendigung der Scroll-Verschiebung durch ein „Scroll-Ende-Signal“ i. S. v.
Merkmal 1.11 b, welches gemäß Streitpatent Abs. [0021] das Ende der scrollbaren
Daten anzeigen soll – d. h. anspruchsgemäß soll die durchlaufende Anzeige der
Liste stehenbleiben, wenn das Ende der Liste erreicht ist. Gemäß D1 würde das
„Object Wheel“ sich weiterdrehen, d. h. nach dem letzten Objekt der scrollbaren
Liste wieder das erste Objekt vom Anfang der Liste anzeigen (vgl. D1 Spalte 21
Zeile 12 bis 14 „Like a real wheel (…) and never stop in between object choices“).
Allerdings trägt dieser Unterschied nicht zur Lösung eines technischen Problems
bei, sondern betrifft eine andere Art der Wiedergabe von Informationen („Anhalten“
beim letzten Objekt der Liste, anstatt „Weiterdrehen“ mit Anfangs-Objekten);
derartige Maßnahmen sind bei der Prüfung auf erfinderische Tätigkeit nicht zu
berücksichtigen (vgl. GRUR 2011, 125 – Wiedergabe topografischer Informationen,
Leitsatz c); BGH GRUR 2015, 660 – Bildstrom; BGH GRUR 2020, 599 –
Rotierendes Menü).


h)     Die Beklagte hat vorgetragen, eine Einbeziehung des derzeitigen Zustands
der Anzeige (d. h. ob das Display in Bewegung ist oder stillsteht) als Parameter für
die auszulösenden Funktionen, so wie es Merkmal 1.13x fordert, sei dem Stand der
Technik nicht zu entnehmen. Auch werde im Stand der Technik die Frage, ob der
Finger beim Lösen des Berührkontakts sich bewege oder nicht (Merkmal 1.12.1),
nicht ausgewertet.


Dem folgt der Senat nicht. Die Frage, ob das Display in Bewegung ist oder stillsteht,
mag zwar in den zitierten Dokumenten bei der Beschreibung der dortigen
Berührfunktionen nicht ausdrücklich gestellt sein. Trotzdem ist klar, dass eine
Berührung des Bildschirms auch im Stand der Technik nur dann als Befehl zum
Anhalten der Scroll-Verschiebung interpretiert wird, wenn das Display in Bewegung
ist (vgl. etwa D1 Spalte 21 Zeile 15 bis 17 „A user can stop a spinning object wheel
at any time by Pointing to a moving object on the object wheel while the object wheel
is spinning“).

                                        - 57 -



Auch eine Auswertung, ob der Finger beim Lösen des Berührkontakts in Bewegung
ist oder nicht, ergibt sich bei genauer Betrachtung aus dem Stand der Technik –
siehe z. B. die in Druckschrift D2 Anspruch 3 formulierte Bedingung: „to scroll at a
rate measured for a vertical speed of said pointing means (17) at the last moment
before it was removed“ (wobei “keine Bewegung des Fingers” dann auch “kein
Scrollen der Anzeige” zur Folge hat).


Hierbei ist zudem zu berücksichtigen, dass nach dem Verständnis des Senats eine
echte Messung der Geschwindigkeit des Fingers zu einem bestimmten Zeitpunkt
mit herkömmlichen Touch-Screens gar nicht möglich ist: üblicherweise wird das
Teilsystem, welches die Berührung erfasst, aus der Ortsveränderung der Berührung
die Geschwindigkeit ableiten. Wenn aber die Geschwindigkeit aus mehreren
aufeinanderfolgenden Messwerten berechnet wird, kann sich nicht exakt die
Geschwindigkeit zum Zeitpunkt des Ablösens des Fingers ergeben, sondern nur
eine „mittlere“ Geschwindigkeit während des Messintervalls. Damit unterscheidet
sich die Bedingung des Streitpatents „finger motion at the time when the finger
contact with the display screen is broken“ nicht mehr von einer allgemeinen
Berücksichtigung der Fingergeschwindigkeit.


i)    Schließlich hat die Beklagte im Hinblick darauf, dass bei der Beurteilung der
erfinderischen Tätigkeit keine „rückschauende Betrachtungsweise“ eingenommen
werden dürfe, noch auf Folgendes hingewiesen.


Zum Prioritätszeitpunkt des Streitpatents, dem 28. Dezember 2001, seien
berührungsempfindliche Bildschirme als solche bereits seit nahezu 40 Jahren
bekannt und seit fast 20 Jahren in Computern genutzt gewesen. Die dem
Streitpatent zugrundeliegende Erfindung sei somit etwa sechs Jahre vor der
Einführung des ersten Apple iPhone und etwa sieben Jahre vor der Einführung des
ersten Android-Smartphones getätigt worden. Im Prioritätsjahr des Streitpatents sei
eines der erfolgreichsten Mobiltelefone, das Nokia 6210, wie zu dieser Zeit üblich
mit einem kleinen Bildschirm und einer dazugehörigen Tastatur ausgestattet
gewesen. Die Mobiltelefone seien hierbei über die Tastatur bedient worden, wobei
in dem Fall, in dem der Text zu lang war, um als Ganzes auf dem Bildschirm gezeigt

                                         - 58 -



zu werden, die „Hoch“- und „Runter“- Pfeiltasten der Tastatur verwendet worden
seien. Dieser Stand sei der zutreffende Ausgangspunkt für die Bewertung der
Patentierbarkeit, nicht der Blick auf die heutzutage omnipräsenten Smartphones.


Zwar ist dieser Hinweis grundsätzlich berechtigt. Das Streitpatent befasst sich
allerdings weder mit Smartphones noch mit anderen tragbaren Mobilgeräten – die
Beschreibung erwähnt Mobilgeräte oder eine besondere Eignung dafür an keiner
Stelle. Vielmehr ist der Figur 2 des Streitpatents deutlich ein Desktop-PC mit
separater Tastatur und einem vom Rechner getrennt angeordneten Touch
Screen 10 zu entnehmen. Der maßgebliche Durchschnittsfachmann war mit den
Bedienmöglichkeiten von berührungsempfindlichen Bildschirmen „an sich“ im Jahr
2001 bereits seit längerem vertraut. Die Möglichkeiten der Berühr-Technik für
Benutzeroberflächen wurden in den 80iger Jahren erdacht (vgl. etwa die
Druckschrift D3 aus dem Jahre 1984) und in der ersten Hälfte der 90iger Jahre
weiterentwickelt (vgl. die Aussagen zum Video NK9a, die 1994 veröffentlichte
Druckschrift D1 und die 1998 veröffentlichte Druckschrift D2). Dass sich erst Jahre
später – und zwar nach dem Prioritätstag des Streitpatents – eine besondere Eignung für Mobiltelefone herausstellte, ist weder die Leistung des Streitpatents noch
Maßstab für seine Beurteilung in technischer Hinsicht.


2.2    Der Argumentation der Beschwerdekammer des EPA, mit welcher das Vorliegen von erfinderischer Tätigkeit begründet wurde (siehe Anlage NK5,
insbesondere Seite 14 bis 18) stützt sich wesentlich darauf, dass der Parameter der
Berührungsdauer in Form von verschiedenen Zeitintervallen einen weiteren
Freiheitsgrad bei der Gestaltung einer gestengesteuerten Mensch-Maschine-Schnittstelle darstelle. Damit könnten die erfassten stationären Berührungen leicht
klassifiziert werden als kurze (∆t < t1), lange (t1 < ∆t < t2) und noch längere (∆t > t2)
Berührungen,      wodurch      der     Gesten-Funktions-Mapping-Raum           in    der
Größenordnung von drei erweitert werde (NK5 Seite 15 Mitte: „extending the
resulting gesture-to-function space (…) by the order of three“).


Dieser Argumentation zur Erweiterung der Zuordnungen von Berührungen zu
Funktionen „in der Größenordnung von drei“ folgt der Senat nicht. Denn das

                                            - 59 -



Streitpatent sieht für so definierte „kurze“ Berührungen (∆t < t1) keine Zuordnung
einer Funktion vor – sie werden vielmehr als „Fehlbedienung“ oder als basierend
auf einem Störsignal verstanden und ignoriert (siehe die einzige Fundstelle zur
„zweiten Mindestzeit“ t1 im Streitpatent Abs. [0031] und oben I., Abschnitt 4.2 letzter
Absatz). Da somit keine Zuordnung einer Funktion vorgesehen ist, wird der Gesten-Funktions-Mapping-Raum dadurch auch nicht erweitert.


Davon abgesehen gehörte sowohl das Ignorieren zu kurzer Berührungen als auch
das Zuordnen mehrerer Funktionen abhängig von der Berührdauer zum Grundwissen des hier zuständigen Durchschnittsfachmanns (s. o. 2.1 b)) und kann deshalb das Vorliegen einer erfinderischen Tätigkeit nicht begründen.


2.3    Vom Stand der Technik unterscheidet sich der Gegenstand des
Patentanspruchs 1 durch konkrete Vorgaben, „welche“ Berührung unter „welchen“
Voraussetzungen „welche“ Bedienfunktion auslöst – d. h. die Zuordnung von
messbaren Parametern (Dauer der Fingerberührung, Richtung, Geschwindigkeit)
und Systemzuständen („Anzeige scrollt gerade“ oder nicht) zu gewünschten
Systemfunktionen      (Steuerung      der      Scroll-Verschiebung,   Auswahl    eines
dargestellten Elements). Die Lehre des Streitpatents verknüpft an sich bekannte
Funktionen so zu einem „Bedien-Konzept“, das sich für den Patentanspruch 1 in der
obigen Tabelle manifestiert (s. o. 2.1 d)).


Von einer reinen Menü-Struktur unterscheidet sich diese Lehre dadurch, dass sie
die Menü-Befehle bestimmten Berühr-Abläufen zuordnet. Die Unterscheidbarkeit
der Berühr-Befehle z. B. abhängig von der Dauer - oder durch Auswertung von
Geschwindigkeit und Richtung der Berührung - umfasst fraglos einzelne technische
Aspekte. Die technischen Möglichkeiten der Erfassung der Fingerberührung und
der Auslösung von Bedienfunktionen waren im Prioritätszeitpunkt des Streitpatents
allerdings, wie ausgeführt, bereits bekannt.


2.4    Das beanspruchte Bedien-Konzept als solches stellt jedoch keine
„technische Problemlösung“ dar und ist deshalb bei der Prüfung auf erfinderische
Tätigkeit nicht zu berücksichtigen.

                                         - 60 -



Die   Frage,   welche    Kombinationen       von   Berührfunktionen   und    dadurch
auszulösenden Bedienfunktionen sich für mögliche Benutzer als „intuitiv“ erweisen,
eine Bedienung „auf natürliche Weise“ erlauben und als „schnelle, bequeme und
natürlich wirkende Vorgehensweise“ angesehen werden (vgl. Streitpatent
Abs. [0019], [0022], [0025], [0041]), ist nichttechnischer Art. So beschreibt das
Streitpatent beispielsweise in Abs. [0037] eine bestimmte Bedienmöglichkeit,
nämlich die Unterscheidung von „stop scrolling“ und „select“ anhand der
Berührdauer.    Weil    diese   Unterscheidung     aber   eine   Quelle     möglicher
Fehlbedienungen sein könnte, schlägt das Streitpatent als eine Alternative vor, auf
die Unterscheidung zu verzichten und jegliche Berührung, egal welcher Dauer, nur
als Befehl zum Stoppen der Scroll-Verschiebung („act solely as a "stop motion"-
signal”) zu interpretieren. Damit werden zwei an sich unterschiedliche Lehren zur
Bedienung als gleichwertig nebeneinandergestellt.


Zur Bewertung derartiger Bedienkombinationen als „intuitiv“ berufen wäre
beispielsweise eine Person, die Benutzerwünsche und Bedienmöglichkeiten
sammelt, z. B. in einem „usability lab“ Benutzer beobachtet und die beobachteten
Bedienkombinationen bewertet, jedoch nicht der technische Fachmann. Die
Schaffung einer neuen Menüstruktur erfordert für sich genommen keine
„technischen“ Überlegungen. Als „nichttechnische Vorgaben für den technischen
Fachmann“ sind derartige Überlegungen bei der Prüfung auf erfinderische Tätigkeit
nicht zu berücksichtigen (vgl. hierzu BGH GRUR 2011,125 – Wiedergabe
topografischer Informationen, Tz. 31).


Der Senat sieht die patentgemäße Zuordnung von Berühr-Bedingungen zu Bedienfunktionen, also das o.g. Bedien-Konzept, nicht anders als das bekannte Menü-Konzept üblicher PC-Programme, bei welchem bestimmten Ordnungsbegriffen wie
„Datei“, „Bearbeiten“, „Ansicht“ untergeordnete Menüpunkte (z.B. bei „Datei“:
„Speichern unter“ usw.) zugeordnet sind. Hier hätte jetzt ein „Erfinder“ auf die Idee
kommen können, andere Ordnungsschemata zu verwenden, weil sie seiner
Meinung nach ergonomischer und intuitiv seien (vielleicht ein Oberbegriff „Ändern“
und darunter: „Seitenlayout“; „Sprache“ (…) o. ä.). Die Schaffung einer solchen
neuen Menüstruktur allein würde jedoch keine „technischen“ Überlegungen

                                      - 61 -



erfordern. Das Streitpatent unterscheidet sich davon dadurch, dass es die Menü-Befehle bestimmten Berühr-Abläufen zuordnet. Die Unterscheidbarkeit der Berühr-Befehle, z. B. abhängig von der Dauer oder durch Auswertung von Geschwindigkeit
und Richtung der Berührung, umfasst fraglos technische Aspekte, die aber
vorbekannt waren. Die spezielle Zuordnung, „welche“ Berühr-Abläufe „welche“
Menü-Befehle auslösen, stellt hingegen keine technische Problemlösung mehr dar.


Wenn aber das gegebene Bedienkonzept als Anleitung, welche Berührung unter
welchen Voraussetzungen welche Bedienfunktion auslösen soll, keine „auf technischen Überlegungen beruhende Erkenntnisse“ nutzt, somit auch keine „Bereicherung der Technik“ darstellt (BGH GRUR 2002, 143 – Suche fehlerhafter Zeichenketten; BGH GRUR 2004, 667 – Elektronischer Zahlungsverkehr) und deshalb bei
der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen ist, dann geht die
Lehre des Patentanspruchs 1 nicht über den Stand der Technik hinaus.


2.5   Die Beklagte wendet ein, die unabhängigen Patentansprüche lösten in ihrer
Gesamtheit die technische Aufgabe, die Bediensicherheit des zugrundeliegenden
Systems zu erhöhen. Deshalb dürften einzelne Merkmale nicht von der
Berücksichtigung ausgeschlossen werden.


Nach ständiger Rechtsprechung sind bei der Prüfung auf erfinderische Tätigkeit
jedoch „nur diejenigen Anweisungen zu berücksichtigen, die die Lösung des
technischen Problems mit technischen Mitteln bestimmen oder zumindest
beeinflussen“ (vgl. BGH GRUR 2011, 125 – Wiedergabe topografischer
Informationen, Leitsatz b)).


Ein konkretes technisches Problem kann hier darin erkannt werden, unterscheidbare Berührungen so zu definieren, dass sie mit einem entsprechenden technischen
System als unterschiedlich erkannt werden können (im Streitpatent konkret gelöst
durch Erfassung von Richtung, Geschwindigkeit und Dauer einer Berührung). Dies
war allerdings vorbekannt (s. o.). Die darüberhinausgehende Zuordnung der
unterschiedlichen Berührungen zu Bedien-Funktionen liefert hingegen, wie
ausgeführt, zu einer technischen Problemlösung keinen Beitrag.

                                        - 62 -



Von einer „Erhöhung der Bediensicherheit“ ist im Streitpatent allenfalls an einer
einzigen Stelle die Rede: gemäß Abs. [0037] („this would protect against the
possibility of unintended "selections" resulting from inadvertently long touches that
were intended only to "stop" the scrolling“) könnte dem Merkmal 1.9 bzw. 8.5 ein
solcher Gedanke zugrunde liegen. Die merkmalsgemäße Lösung, eben keine
Unterscheidung der Druckdauer vorzusehen, entspricht dann aber dem Vorbekannten (siehe z. B. D1 Spalte 21 Zeile 15 bis 17 „A user can stop a spinning
object wheel at any time by Pointing to a moving object on the object wheel while
the object wheel is spinning“). Selbst wenn man - entgegen der durch den Senat
vertretenen Auffassung - insoweit eine technische Problemstellung anerkennen
wollte, ist die angebotene Lösung daher nicht erfinderisch.


Darüber hinaus macht das Streitpatent keine Ausführungen zu einer Erhöhung der
Bediensicherheit. Vorteile, die das eigentliche Wesen der Erfindung ausmachen
sollen, müssten jedoch, wenn sie patentbegründend sein sollen, in der Patentschrift
offenbart sein (vgl. BGH GRUR 1960, 542 – Flugzeugbetankung I), woran es im
vorliegenden Fall fehlt.


2.6    Selbst wenn man dem beanspruchten Bedienkonzept einen technischen
Gehalt zuerkennen würde, beruht der Gegenstand von Patentanspruch 1
gleichwohl nicht auf erfinderischer Tätigkeit.


Denn bei dem streitpatentgemäßen Konzept zur Zuordnung bestimmter Fingerberührungen zu Bedienfunktionen handelt es sich um Maßnahmen, die letztlich in
das Belieben des Fachmanns gestellt sind.


Es wird Gebrauch gemacht von bekannten Parametern und Funktionen, die der
Fachmann je nach Zweckmäßigkeit einsetzen wird. Sofern eine technische Lösung
(wie hier eine bestimmte messtechnisch erfassbare Berührfunktion) als ein
generelles, für eine Vielzahl von Anwendungsfällen in Betracht zu ziehendes Mittel
ihrer Art nach zum allgemeinen Fachwissen des zuständigen Fachmanns gehört,
„kann Veranlassung zu ihrer Heranziehung bereits dann bestehen, wenn sich die
Nutzung ihrer Funktionalität in dem zu beurteilenden Zusammenhang als objektiv

                                       - 63 -



zweckmäßig darstellt und keine besonderen Umstände feststellbar sind, die eine
Anwendung aus fachlicher Sicht als nicht möglich, mit Schwierigkeiten verbunden
oder sonst untunlich erscheinen lassen“ (siehe BGH GRUR 2014, 647 –
Farbversorgungssystem; bestätigt auch durch BGH GRUR 2018, 509 –
Spinfrequenz; BGH GRUR 2018, 716 – Kinderbett).


So liegt der Fall hier, weil die verschiedenen an sich bekannten Berührfunktionen
vom Fachmann wie ein „Baukasten“ verstanden werden, aus dem er sich je nach
Wunsch bedienen kann. Bei der Verwirklichung der Zuordnung bestimmter
Fingerberührungen zu Bedienfunktionen hat es sich daher aus Sicht des
Fachmanns insgesamt um Routinearbeit gehandelt, ohne dass die Beklagte
aufzuzeigen vermochte, welche besonderen technischen Vorteile gerade mit der
beanspruchten Kombination von Berührfunktionen verbunden sind. Auch bei einer
Betrachtung aus diesem Blickwinkel beruht das beanspruchte Konzept nicht auf
erfinderischer Tätigkeit.


3.     Für die Lehre des Patentanspruchs 8 gemäß Hilfsantrag II gilt nichts
Anderes. Denn sie unterscheidet sich nach der vorgenommenen Auslegung von der
Lehre des Patentanspruchs 1 hauptsächlich noch durch das Fehlen des
Merkmalsbestandteils „stationär“ bei der Fingerberührung in Merkmal 8.4. Doch
dies hat auf die oben ausgeführte Beurteilung der erfinderischen Tätigkeit keinen
Einfluss.


4.      Auch in den Fassungen der Hilfsanträge IIa, IIb und IIc ist das Streitpatent
nicht bestandsfähig. Gegenüber der Fassung nach Hilfsantrag II enthalten diese
Hilfsanträge unveränderte unabhängige Patentansprüche.




                                        V.


Keine der Fassungen des Streitpatents nach einem der weiteren Hilfsanträge kann
günstiger beurteilt werden, weil der jeweilige Gegenstand des unabhängigen

                                        - 64 -



System-Anspruchs und / oder des unabhängigen Verfahrensanspruchs zumindest
nicht auf erfinderischer Tätigkeit beruht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. a), Art. 56 EPÜ).


1.       In der Fassung nach Hilfsantrag VI hat das Streitpatent ebenfalls keinen
Bestand.


Die Fassung nach Hilfsantrag VI unterscheidet sich von der Fassung des
Streitpatents nach Hilfsantrag II lediglich durch folgende markierte Ergänzung in
Merkmal 8.4 des Verfahrensanspruchs 8:


8.4x “if the sensed duration of a stationary finger touch contact time is
      greater than a first preset minimum time and less than a second preset minimum time and is accompanied by motion along the surface
      of the display screen (40), moving said display in correspondence
      with movement of the finger touch”.


Die   Klägerin    macht    insoweit   geltend,   weil   nunmehr   eine   „stationäre“
Fingerberührung von Bewegung „begleitet“ werden solle, sei nicht eindeutig, ob nur
die Dauer der stationären Fingerberührung gemessen werde und diese als
Steuerparameter in die Gestensteuerung einfließen solle, oder auch die Dauer der
bewegten Fingerberührung.


Es ist einzuräumen, dass die Formulierung Raum für Missverständnisse lässt. Die
Beschreibung ist hier deutlicher: gemäß Abs. [0032] soll innerhalb eines Zeitraums
zwischen der ersten und der zweiten Mindestzeit überprüft werden, ob der Finger
sich bewegt („if step 100 senses motion in association with the finger touch on the
screen, during the finite period between the first predetermined time and the second,
then (…)“). In diesem Sinne legt der Senat die Formulierung des Merkmals 8.4x
daher aus.


Auch nach Einschränkung auf eine „stationäre“ Fingerberührung bleibt das Merkmal
jedoch     Bestandteil    des   beschriebenen      Bedienkonzepts,    welches     als

                                         - 65 -



„nichttechnische Vorgabe für den technischen Fachmann“ bei der Prüfung auf
erfinderische Tätigkeit nicht zu berücksichtigen ist (s. o. IV., Abschnitt 2.4).


Wie ausgeführt, handelt es sich zudem um eine ins Belieben des Fachmanns
gestellte Maßnahme, mit welcher sich eine Erfindungshöhe des Streitpatents in der
Fassung nach Hilfsantrag VI nicht begründen lässt (s. o. IV., Abschnitt 2.6).


2.     In den Fassungen nach Maßgabe der Hilfsanträge VIa und VIb wurde
(allein) der unabhängige Verfahrensanspruch jeweils durch das Merkmal 8.4x so
abgeändert wie oben für den Hilfsantrag VI dargestellt. Zu den Ausführungen unter
1. ergeben sich dadurch keine Änderungen.



3.     Auch die jeweiligen Gegenstände der unabhängigen Patentansprüche 1 und
7 bzw. 2 in ihren Fassungen nach Maßgabe der Hilfsanträge III, IIIa, IIIb und IIIc
beruhen nicht auf erfinderischer Tätigkeit.


3.1    Die Fassung nach Hilfsantrag III geht von der Anspruchsfassung nach
Hilfsantrag II aus, wobei an den dortigen Systemanspruch, den Patentanspruch 1
mit den Merkmalen 1.9x und 1.13x, der erteilte Unteranspruch 2 als Merkmal 1.14,
und an den Verfahrensanspruch, Patentanspruch 7 mit den Merkmalen 8.5x und
8.9x, der erteilte Unteranspruch 10 als Merkmal 8.10 angehängt wird:


1.14    “wherein said scrolling motion program instructions further comprise
        instructions to move a touch-selected item relative to the stationary
        display in correspondence with movement of said finger touch, in
        response to motion following a touch having a stationary duration
        greater than said second preset minimum time.”;


8.10    “wherein said method comprises the further step (103) of sensing a
        stationary finger touch on said screen having a duration greater
        than said second preset minimum time and then moving a touch-

                                         - 66 -



        selected item relative to the stationary display in correspondence
        with movement of the finger touch.”.


Auf diese Weise kommt die Lehre hinzu, dass bei „stationärem Bildschirm“ dann,
wenn die stationäre Berührdauer nicht (länger als die erste, aber) kürzer als die
„zweite voreingestellte Mindestzeit“ ist (wie es die Merkmale 1.8 / 1.12 bzw. 8.4 /
8.8 fordern), sondern länger andauert und dadurch außerhalb der Bedingung der
genannten Merkmale liegt, eine andere Bedienfunktion ausgelöst wird, nämlich ein
„touch dragging“, d. h. ein dem Finger folgendes Verschieben nur für das zuvor
ausgewählte Element (nicht für den ganzen Bildschirm) (vgl. Streitpatent
Abs. [0030] – „stick to the finger“).


3.2    Die Lehre dieser zusätzlichen Merkmale rechtfertigt keine andere Beurteilung. Sowohl das „touch dragging“ (vgl. oben IV., Abschnitt 2.1 e), zweiter
Spiegelstrich) als auch das Auslösen unterschiedlicher Bedienfunktionen abhängig
von der Berührdauer (vgl. oben IV., Abschnitt 2.1 e), erster Spiegelstrich, oder die
Verweise in Abs. [0012] und Abs. [0014] des Streitpatents) waren, wie ausgeführt,
vor dem Prioritätstag des Streitpatents bekannt.


Durch die genannten zusätzlichen Funktionen wird das Bedienkonzept des
Streitpatents in der Fassung nach Hilfsantrag II um eine weitere - für sich bekannte
- Bedienmöglichkeit erweitert, ohne dass „auf technischen Überlegungen
beruhende Erkenntnisse“ zugrunde liegen. Auch das erweiterte Bedienkonzept
stellt eine „nichttechnische Vorgabe für den technischen Fachmann“ dar, die bei der
Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen ist (s. o. IV., Abschnitt
2.4). Unabhängig davon handelt es sich zudem um in das Belieben des Fachmanns
gestellte Maßnahmen, mit welchen sich das Vorliegen einer erfinderischen Tätigkeit
nicht begründen lässt (s. o. IV., Abschnitt 2.6).


3.3    Nachdem die Hilfsanträge IIIa, IIIb und IIIc auf gegenüber dem Hilfsantrag III
unveränderte Patentansprüche 1 und / oder 7 gerichtet sind, ist das Streitpatent in
keiner dieser Fassungen patentfähig.

                                         - 67 -



4.     Gleiches gilt für die Beurteilung des Streitpatents in einer der Fassungen der
Hilfsanträge VII, VIIa und VIIb.


4.1    Die Fassung nach Hilfsantrag VII unterscheidet sich von der Fassung nach
Hilfsantrag III lediglich durch folgende, bereits aus dem Hilfsantrag VI bekannte
Ergänzung in Merkmal 8.4 des Verfahrensanspruchs 7:


8.4x “if the sensed duration of a stationary finger touch contact time is
       greater than a first preset minimum time and less than a second preset minimum time and is accompanied by motion along the surface
       of the display screen (40) moving said display in correspondence with
       movement of the finger touch”.


Hierfür gilt das oben in Abschnitt 1. für den Hilfsantrag VI Ausgeführte: Auch nach
Einschränkung auf eine „stationäre“ Fingerberührung bleibt das Merkmal
Bestandteil des angesprochenen Bedienkonzepts, welches als „nichttechnische
Vorgabe für den technischen Fachmann“ bei der Prüfung auf erfinderische Tätigkeit
nicht zu berücksichtigen ist; zudem handelt es sich auch um eine ins Belieben des
Fachmanns gestellte Maßnahme, mit welcher sich das Vorliegen einer
erfinderischen Tätigkeit nicht begründen lässt.


4.2    Dies betrifft in gleicher Weise die Fassungen des Streitpatents nach
Maßgabe der Hilfsanträge VIIa und VIIb, bei denen der unabhängige
Verfahrensanspruch jeweils durch das Merkmal 8.4x abgeändert wurde wie oben
für die Hilfsanträge VI und VII dargestellt.



5.     Die jeweiligen Gegenstände der unabhängigen Patentansprüche 1 und 7
bzw. 2 in den Fassungen des Streitpatents nach Maßgabe der Hilfsanträge IV, IVa,
IVb und IVc beruhen ebenfalls nicht auf erfinderischer Tätigkeit.


5.1    Hilfsantrag IV geht von der Anspruchsfassung nach Hilfsantrag III aus, wobei
beim dortigen Systemanspruch, Patentanspruch 1 umfassend die geänderten

                                         - 68 -



Merkmale 1.9x und 1.13x und das Merkmal 1.14, drei weitere Merkmale sowie beim
Verfahrensanspruch, Patentanspruch 7 umfassend die geänderten Merkmale 8.5x
und 8.9x und das Merkmal 8.10, zwei weitere Merkmale folgendermaßen ergänzt
wurden:


1.8.1x “and, following a separation of said finger touch from said screen
        (40) and, if the finger is in motion at the time when the finger contact
        with the display screen (40) is broken, the, a scroll format display
        on said display screen (40) is caused to begin to scroll in said
        sensed direction and at said sensed initial speed;”


1.10x   “time decay program instructions associated with said microprocessor (42) for, during scrolling displacement, reducing the rate of
        scrolling displacement on said display screen (40) at a predetermined rate until motion is terminated;”


1.11x   “stopping motion program instructions associated with said microprocessor (42) for, during scrolling displacement, terminating
        scrolling displacement of the image on said display screen (40)
        upon first occurrence of any signal in the group of signals
        comprising: (…)”


8.4.1x “and – following separation of said finger touch from said display
        screen (40), if the finger is in motion at the time when the finger
        contact with the display screen (40) is broken, – initiating (104)
        scrolling motion of said scrollable data on said display screen (40)
        in said sensed direction and at said sensed speed;”


8.6x    “slowing (106), during scrolling displacement, the speed of said
        scrolling motion from the initiated speed thereof, at a predetermined
        rate; and (…)”.

                                       - 69 -



5.2   Diese scheinbaren Beschränkungen der beanspruchten Lehre ändern jedoch
nichts an der Beurteilung als „für den Fachmann naheliegend“.


Die Ergänzungen gemäß den Merkmalen 1.10x, 1.11x und 8.6x „during scrolling
displacement” können allenfalls als (unnötige) Klarstellungen verstanden werden,
da sie sich auf Situationen beziehen, die offensichtlich bereits von einem scrollenden Bildschirm ausgehen. Sie ändern an der beanspruchten Lehre nichts.


Die Ergänzungen in den Merkmalen 1.8.1x und 8.4.1x beziehen die Überprüfung,
ob der Finger zu dem Zeitpunkt, zu dem der Fingerkontakt mit dem Bildschirm
abbricht, in Bewegung ist (wie sie von den Merkmalen 1.12.1 bzw. 8.8.1 bekannt
ist), ausdrücklich auch auf das Auslösen des Scroll-Vorgangs.


Wie ausgeführt (s. o. IV., Abschnitt 2.1 h), letzter Absatz), ergeben sich keine
wesentlichen Unterschiede zur bekannten Erfassung der Finger-Geschwindigkeit
zum Auslösen der Scroll-Verschiebung. Für sich betrachtet stellt die Ergänzung
keine technische Besonderheit dar (vgl. die Druckschrift D2 Anspruch 3 „to scroll at
a rate measured for a vertical speed of said pointing means (17) at the last moment
before it was removed“). Entsprechend der Beurteilung des zugrundeliegenden
Hilfsantrags III stellt das Streitpatent auch in seiner Fassung nach Hilfsantrag IV
lediglich bekannte Maßnahmen in einem Gesamt-Konzept zusammen (s. o. IV.,
Abschnitte 2.4 und 2.6). Das Vorliegen einer erfinderischen Tätigkeit kann damit
nicht begründet werden.


5.3   Weil die Hilfsanträge IVa, IVb und IVc auf gegenüber dem Hilfsantrag IV
unveränderte Patentansprüche 1 und / oder 7 gerichtet sind, ist das Streitpatent in
keiner dieser Fassungen patentfähig.



6.    Die Fassungen des Streitpatents nach Maßgabe der Hilfsanträge V, Va und
Vb sind nicht anders als die Fassung nach Hilfsantrag IV zu beurteilen.

                                          - 70 -



6.1      Die Fassung nach Hilfsantrag V unterscheidet sich von der Fassung nach
Hilfsantrag IV    lediglich   durch   folgende     Ergänzung   in   Merkmal   8.4   des
Verfahrensanspruchs, des Patentanspruchs 7:


8.4y “if the sensed duration of said stationary finger touch contact time is
         greater than a first preset minimum time and less than a second preset minimum time and is accompanied by motion along the surface
         of the display screen (40) moving said display in correspondence with
         movement of the finger touch”.


6.2      Zwar ist die so beanspruchte Lehre nicht aus sich heraus verständlich, weil
es im Patentanspruch 7 keinen vorherigen Bezugspunkt für „said stationary finger
touch“ gibt. Der Senat legt die Änderung wie bei den Hilfsanträgen VI und VII im
Sinne von „a stationary finger touch” anstelle von „said stationary finger touch“ aus.


6.3      Es ergibt sich das bereits oben in Abschnitt 1. für den Hilfsantrag VI und in
Abschnitt 3. für den Hilfsantrag VII Festgestellte: Auch nach Einschränkung auf eine
„stationäre“ Fingerberührung bleibt das Merkmal Bestandteil des angesprochenen
Bedienkonzepts, welches als „nichttechnische Vorgabe für den technischen
Fachmann“ bei der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen ist.
Zudem handelt es sich um eine ins Belieben des Fachmanns gestellte Maßnahme,
mit welcher sich die erforderliche Erfindungshöhe des Streitpatents nicht begründen
lässt.


6.4      Gleiches gilt für das Streitpatent in den Fassungen nach Maßgabe der
Hilfsanträge Va und Vb mit entsprechender Änderung des unabhängigen
Verfahrensanspruchs jeweils durch das Merkmal 8.4y. In keiner dieser Fassungen
hat das Streitpatent somit Bestand.

                                        - 71 -




                                         VI.


Mithin haben weder der unabhängige Systemanspruch noch der unabhängige
Verfahrensanspruch des Streitpatents in einer der von der Beklagten beantragten
Fassungen Bestand. Da die Hilfsanträge im Sinne geschlossener Anspruchssätze
zu verstehen sind, sind die Unteransprüche in der erteilten Fassung bzw. in den
Fassungen der Hilfsanträge von Amts wegen nicht auf patentfähige Inhalte zu
prüfen. Das Streitpatent ist vielmehr insgesamt für nichtig zu erklären.




                                         VII.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 2 PatG i. V. m. § 91 Abs. 1
Satz 1 ZPO, der Ausspruch über die vorläufige Vollstreckbarkeit auf § 99 Abs. 1
PatG i. V. m. § 709 ZPO.

                                       - 72 -



                                       VIII.


                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland
zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der
Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt
unterzeichnet    und   innerhalb    eines       Monats   beim     Bundesgerichtshof,
Herrenstraße 45a, 76133 Karlsruhe eingereicht werden.


Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten
Urteils, spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung.
Die Berufungsfrist kann nicht verlängert werden.


Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung
gerichtet wird, sowie die Erklärung enthalten, dass gegen dieses Urteil Berufung
eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Püschel         Baumgardt          Dr. Schnurr           Dr. Forkel       Hoffmann
