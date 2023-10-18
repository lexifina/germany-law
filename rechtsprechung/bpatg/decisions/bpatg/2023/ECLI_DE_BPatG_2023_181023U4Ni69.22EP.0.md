---
ecli: "ECLI:DE:BPatG:2023:181023U4Ni69.22EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 69/22"
decided: "2023-10-18"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=27&nr=44175&anz=529&pos=412&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-10-18_4_Ni_69_22_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 69/22 vom 2023-10-18

## Entscheidung

BUNDESPATENTGERICHT
                        IM NAMEN DES VOLKES

                                  URTEIL
                                                          Verkündet am
                                                         18. Oktober 2023
                                                                …


    4 Ni 69/22 (EP)

    (Aktenzeichen)




                        In der Patentnichtigkeitssache

…




                  betreffend das europäische Patent 2 227 923

                             (DE 60 2008 039 323)




ECLI:DE:BPatG:2023:181023U4Ni69.22EP.0

                                          -2-




hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf die mündliche
Verhandlung vom 18. Oktober 2023 durch den Vorsitzenden Richter Voit, die Richterin Werner M.A. sowie die Richter Dipl.-Ing. Altvater, Dipl.-Phys. Univ. Dr. Haupt
und Dipl.-Ing. Tischler


für Recht erkannt:

 I.   Das europäische Patent 2 227 923, soweit angegriffen, wird mit Wirkung
      für das Hoheitsgebiet der Bundesrepublik Deutschland teilweise für nichtig erklärt, soweit es über folgende Fassung hinausgeht:

      “1. A method of receiving a random access response, the method comprising:

          a user equipment (UE) transmits a random access preamble to a base station (Node-B) (S430; S930);
          the user equipment (UE) receives the random access response corresponding to the random access preamble from the base station (Node-B) (S450;
          S950),
          the received random access response including information of a transmission time when the random access preamble is transmitted,
          the user equipment (UE) determines whether or not the received random
          access response is the response to the transmitted random access preamble,
          characterized in that the method further comprises:
          the user equipment (UE) stores a subframe number for transmitting the random access preamble (S420);
          the information of the transmission time when the random access preamble
          is transmitted includes a number indicating the transmission time of the random access preamble, the number being a number allocated to a subframe,
          in which a random access channel, RACH, slot is present,
          the user equipment (UE) checks whether the number included in the received random access response is identical to the subframe number of the
          transmitted random access preamble stored by the user equipment (S460;
          S960),

                                      -3-



     the user equipment (UE) determines that the received random access response is the response to the transmitted random access preamble, if the
     number included in the received random access response is identical to the
     subframe number of the transmitted random access preamble stored by the
     user equipment (S460; S960), and
     the user equipment (UE) receives the random access response within a predetermined time span including a predetermined time point after a transmission time when the random access preamble is transmitted, and the predetermined time point is obtained by adding an offset time to the random access preamble transmission time,
     wherein the offset time is equal to half of a round trip time for a hybrid automatic repeat request, HARQ, process.


2.   The method according to claim 1,

     wherein the number is the uplink subframe number of the time point when a
     user equipment (UE) transmits a random access preamble to a base station
     (Node-B).


9.   A user equipment (UE) being adapted

     to transmit a random access preamble to a base station (Node-B) (S430;
     S930);
     to receive a random access response corresponding to the random access
     preamble from the base station (Node-B) (S450; S950), the received random
     access response including information of a transmission time when the random access preamble is transmitted, and
     to determine whether or not the received random access response is the
     response to the transmitted random access preamble,
     characterized in that the information of the transmission time when the random access preamble is transmitted includes a number indicating the transmission time of the random access preamble, the number being a number
     allocated to a subframe, in which a random access channel, RACH, is present,
     in that the user equipment is further adapted to store a subframe number for
     transmitting the random access preamble (S420);

                                          -4-



         to check whether the number included in the received random access response is identical to the subframe number of the transmitted random access preamble stored by the user equipment (S460; S960), and
         to determine that the received random access response is the response to
         the transmitted random access preamble, if the number included in the received random access response is identical to the subframe number of the
         transmitted random access preamble stored by the user equipment (S460;
         S960),
         in that the user equipment (UE) comprises means arranged to receive the
         random access response from the base station (Node-B) within a predetermined time span including a predetermined time point after a transmission
         time of the random access preamble, and means arranged to obtain the predetermined time point as the sum of an offset time and the random access
         preamble transmission time, and
         in that the offset time is equal to half of a round trip time for a hybrid automatic repeat request, HARQ, process.”



II.    Im Übrigen wird die Klage abgewiesen.



III.   Die Kosten des Rechtsstreits werden gegeneinander aufgehoben.



IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu
       vollstreckenden Betrages vorläufig vollstreckbar.

                                          -5-




                                  Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 2 227 923 (Streitpatent), das
– laut Streitpatentschrift unter Inanspruchnahme der Priorität der koreanischen Anmeldung KR 20080047656 (= Dokument NK3-P2) vom 22. Mai 2008 und der US-
amerikanischen Anmeldung US 18492 P vom 1. Januar 2008 (engl.-sprach. Übersetzung als Dokument NK3-P1) – am 31. Dezember 2008 angemeldet worden ist.
Die Erteilung des europäischen Patents ist am 29. Juli 2015 (Streitpatentschrift
EP 2 227 923 B1 = Dokument NK3) veröffentlicht worden. Das in englischer Sprache gefasste Streitpatent ist in Kraft.


Das Deutsche Patent- und Markenamt führt das Streitpatent unter dem Aktenzeichen 60 2008 039 323. Es trägt die Bezeichnung

       „Determination that a random access response received from a base
      station by a user equipment corresponds to a random access preamble
                previously transmitted by the same user equipment”

                         und in der deutschen Übersetzung

   „Feststellung, dass eine aus einer Basistation von einem Benutzer-Endgerät
   empfangene Direktzugriffsantwort einer Direktzugriffsanfrage entspricht, die
             zuvor vom gleichen Benutzer-Endgerät übertragen wurde“

und umfasst in der erteilten Fassung zehn Patentansprüche, die die Klägerin mit
ihrer Nichtigkeitsklage vom 15. August 2022 teilweise und zwar im Umfang der Patentansprüche 1, 2 und 9 angreift.


Der das Verfahren betreffende Patentanspruch 1 lautet in der erteilten Fassung:

  1. A method of receiving a random access response, the method comprising:

          a user equipment (UE) transmits a random access preamble to a
          base station (Node-B) (S430; S930);

                                -6-



  the user equipment (UE) receives the random access response corresponding to the random access preamble from the base station
  (Node-B) (S450; S950),
  the received random access response including information of a
  transmission time when the random access preamble is transmitted,
  the user equipment (UE) determines whether or not the received random access response is the response to the transmitted random access preamble,

characterized in that the method further comprises:

  the user equipment (UE) stores a subframe number for transmitting
  the random access preamble (S420);
  the information of the transmission time when the random access
  preamble is transmitted includes a number indicating the transmission time of the random access preamble, the number being a number allocated to a subframe, in which a random access channel,
  RACH, slot is present,
  the user equipment (UE) checks whether the number included in the
  received random access response is identical to the subframe number of the transmitted random access preamble stored by the user
  equipment (S460; S960),
  the user equipment (UE) determines that the received random access response is the response to the transmitted random access preamble, if the number included in the received random access response is identical to the subframe number of the transmitted random
  access preamble stored by the user equipment (S460; S960), and
  the user equipment (UE) receives the random access response
  within a predetermined time span including a predetermined time
  point after a transmission time when the random access preamble is
  transmitted, and the predetermined time point is obtained by adding
  an offset time to the random access preamble transmission time.

                                        -7-



Der die Vorrichtung betreffende Patentanspruch 9 lautet in der erteilten Fassung:

  9. A user equipment (UE) being adapted
         to transmit a random access preamble to a base station (Node-B)
         (S430; S930);
         to receive a random access response corresponding to the random
         access preamble from the base station (NodeB) (S450; S950), the
         received random access response including information of a transmission time when the random access preamble is transmitted, and
         to determine whether or not the received random access response is
         the response to the transmitted random access preamble, characterized in that the information of the transmission time when the random access preamble is transmitted includes a number indicating the
         transmission time of the random access preamble, the number being
         a number allocated to a subframe, in which a random access channel, RACH, is present,
         in that the user equipment is further adapted
         to store a subframe number for transmitting the random access preamble (S420);
         to check whether the number included in the received random access
         response is identical to the subframe number of the transmitted random access preamble stored by the user equipment (S460; S960),
         and
         to determine that the received random access response is the response to the transmitted random access preamble, if the number
         included in the received random access response is identical to the
         subframe number of the transmitted random access preamble stored
         by the user equipment (S460; S960), and
         in that the user equipment (UE) comprises means arranged to receive the random access response from the base station (Node-B)
         within a predetermined time span including a predetermined time
         point after a transmission time of the random access preamble, and
         means arranged to obtain the predetermined time point as the sum
         of an offset time and the random access preamble transmission time.

                                         -8-



Patentanspruch 2 ist unmittelbar auf Patentanspruch 1 rückbezogen.

Die Klägerin ist der Ansicht, dass die Gegenstände der angegriffenen Patentansprüche 1 und 9 gegenüber der Offenbarung der internationalen Anmeldung vom
31. Dezember 2008 unzulässig erweitert und in der Streitpatentschrift nicht so deutlich und vollständig offenbart seien, dass ein Fachmann sie ausführen könne. Die
Priorität der US-amerikanischen Voranmeldung sei zumindest materiell nicht wirksam in Anspruch genommen. Die Gegenstände der angegriffenen unabhängigen
Patentansprüche 1 und 9 nach Streitpatent seien gegenüber dem Stand der Technik nicht neu und beruhten jedenfalls nicht auf einer erfinderischen Tätigkeit.

Dabei stützt die Klägerin ihr Vorbringen auf folgende Dokumente:

     NK3-P1      englische Übersetzung der US 18492 P vom 1. Januar 2008;
     NK3-PCT     Offenlegungsschrift WO 2009/084924 A2 vom 9. Juli 2009;
     NK4:        CATT, „RA-RNTI design”, R2-081673 (resubmission of R2-
                 080718), 3GPP TSG RAN WG2 #61bis, Shenzhen, China,
                 31st March – 4th April 2008, 5 Seiten;
     NK5:        CN 101128062 A, veröffentlicht am 20. Februar 2008;
     NK6:        CATT, „Text Proposal of RA-RNTI”, R2-082794, 3GPP TSG
                 RAN WG2 #62, Kansas City, USA, May 5-9, 2008, 2 Seiten;
     NK7:        Qualcomm Europe, „RA_WINDOW and RA-RNTI allocation”, R2-081559, 3GPP TSG RAN WG2 #61bis, Shenzhen,
                 China, 31st March – April 4th 2008, 3 Seiten.


Die Klägerin beantragt unter Bezugnahme auf die Klageschrift vom 15. August 2022,

      das europäische Patent 2 227 923 für das Gebiet der Bundesrepublik
      Deutschland im Umfang der Patentansprüche 1, 2 und 9 für nichtig
      zu erklären.


Die Beklagte beantragt,

      die Klage abzuweisen,

                                        -9-




hilfsweise, die Klage abzuweisen,

      soweit sie sich auch gegen eine der Fassungen des Streitpatents
      nach den Hilfsanträgen 1 bis 5, eingereicht mit dem Schriftsatz vom
      9. Juni 2023, richtet,

      mit der Maßgabe, dass die Hilfsanträge in der numerischen Reihenfolge geprüft werden sollen und als geschlossene Anspruchssätze
      gestellt sind.


Die Beklagte tritt der Argumentation der Klägerin entgegen und ist der Auffassung,
das Streitpatent nehme die Priorität der US-amerikanischen Voranmeldung wirksam
in Anspruch, der Gegenstand des Streitpatents in den angegriffenen Patentansprüchen 1, 2 und 9 sei ursprungsoffenbart und gegenüber dem Stand der Technik neu
und beruhe auch auf einer erfinderischen Tätigkeit. Der Gegenstand des Streitpatents sei wenigstens in einer der verteidigten Fassungen nach den eingereichten
Hilfsanträgen schutzfähig.


Wegen des Wortlauts von Hilfsantrag 1 wird auf den Urteilstenor Bezug genommen.
Wegen des Wortlauts der Patentansprüche nach den weiteren Hilfsanträgen wird
auf die Akte verwiesen.


Die Klägerin tritt auch den Hilfsanträgen entgegen und sieht ebenfalls die Gegenstände nach den Patentansprüchen 1, 2 und 9 in der Fassung der jeweiligen Hilfsanträge als unzulässig erweitert, nicht neu und nicht erfinderisch an.


Der Senat hat den Parteien einen Hinweis vom 27. März 2023 zugeleitet und hierin
Fristen zur Stellungnahme gesetzt.


Wegen der weiteren Einzelheiten des Sach- und Streitstands wird auf die zwischen
den Parteien gewechselten Schriftsätze nebst Anlagen, das Protokoll der mündlichen Verhandlung vom 18. Oktober 2023 sowie den weiteren Akteninhalt Bezug
genommen.

                                          - 10 -




                           Entscheidungsgründe


                                           A.


Die zulässige Klage, die sich gegen die Patentansprüche 1, 2 und 9 des Streitpatents richtet, hat in der Sache nur teilweise Erfolg, und zwar hinsichtlich der erteilten
Fassung des Streitpatents. Denn insoweit ist jedenfalls der Nichtigkeitsgrund der
mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG, Art. 138
Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 56 EPÜ gegeben.


In der Fassung nach dem Hilfsantrag 1 erweisen sich die Patentansprüche 1, 2
und 9 hingegen als schutzfähig, so dass die Klage, soweit sie sich auch gegen diese
Fassung richtet, abzuweisen ist. Auf die Frage, ob das Streitpatent auch in der Fassung nach den weiteren Hilfsanträgen Bestand hätte, kommt es bei dieser Sachlage
nicht mehr an.




                       I. Zum Gegenstand des Streitpatents


1.     Gegenstand des Streitpatents sind Verfahren und Vorrichtungen für Kommunikation über Funksignale in Kommunikationssystemen.

Das Streitpatent befasst sich mit drahtlosen Kommunikationssystemen (nachfolgend als Mobilfunknetze bezeichnet), wie z. B. auf dem UMTS- oder dem LTE-Standard basierenden Mobilfunknetzen, bei denen Endgeräte („user equipment“, UE)
und Basisstationen („base station“, Node-B) über Funksignale miteinander kommunizieren (vgl. Streitpatentschrift, Absätze 0001, 0015, 0019 und 0031).

Damit ein Endgerät in einem drahtlosen Kommunikationssystem Informationen austauschen kann, muss das Endgerät zunächst über eine Basisstation Zugang zum
Mobilfunknetz erlangen. Das Endgerät kommuniziert mit der Basisstation dabei
über einen sogenannten Zufallszugriffskanal („random access channel“, RACH).
Das hierfür angewendete und aus dem Stand der Technik bekannte Verfahren wird
als Zufallszugriffsverfahren („random access procedure“) bezeichnet.

                                       - 11 -




Hierbei sendet das Endgerät zunächst zu einem bestimmten Zeitpunkt über einen
Zufallszugriffskanal eine sogenannte Zufallszugriffspräambel („random access
preamble“) an die Basisstation. Die Zufallszugriffspräambel beinhaltet eine von dem
Endgerät zufällig ausgewählte Zahlensequenz („randomly selected sequence“, „sequence number“, „RACH sequence“) (Absätze 0002 und 0003; Figuren 1a und 1b).

Empfängt eine Basisstation eine solche Zufallszugriffspräambel, erfasst sie die darin enthaltene zufällig ausgewählte Zahlensequenz und antwortet mit einer sogenannten Zufallszugriffsantwort („random access response“, „RACH response“), die
ebenfalls die in der Zufallszugriffspräambel enthaltene und von dem Endgerät zufällig ausgewählte Zahlensequenz beinhaltet (Absätze 0002 und 0003; Figuren 1a
und 1b).

Empfängt das Endgerät eines solche Zufallszugriffsantwort, erfasst es die darin enthaltene Zahlensequenz und vergleicht diese mit der vom Endgerät ursprünglich zufällig ausgewählten und als Teil der Zufallszugriffspräambel an die Basisstation gesendete Zahlensequenz. Stimmen beide Zahlensequenzen überein, erkennt das
Endgerät, dass die empfangene Zufallszugriffsantwort für es bestimmt ist (Absätze 0002 und 0003).

Auf Basis dieser Zufallszugriffsantwort wird dann nachfolgend die Funkverbindung
zwischen Basisstation und Endgerät initialisiert, wobei dieser weitere Prozess für
das Streitpatent nicht relevant ist.

Den Endgeräten steht eine größere Anzahl von zufällig auswählbaren Zahlensequenzen zur Verfügung, so dass in der Regel eine Zuordnung der durch das Endgerät ausgesendeten Zufallszugriffspräambel zu der empfangenen Zufallszugriffsantwort anhand des Vergleichs der ausgesendeten Zahlensequenz und der als
Teil der Zufallszugriffsantwort empfangenen Zahlensequenz möglich ist.

Eine einzelne Basisstation bedient in der Regel eine Vielzahl unterschiedlicher Endgeräte. Daher kann es trotz der Vielzahl der zur Verfügung stehenden zufällig auswählbaren Zahlensequenzen vorkommen, dass mehrere Endgeräte zufällig in einem kurzen zeitlichen Abstand dieselbe zufällig ausgewählte Zahlensequenz an

                                          - 12 -



eine Basisstation senden, so dass die Basisstation in einem engen zeitlichen Abstand mehrere Zufallszugriffspräambeln empfängt, welche jeweils die gleiche zufällig von den Endgeräten ausgewählte Zahlensequenz enthalten (Absätze 0004
und 0006; Figuren 1a und 1b).

Empfängt eine Basisstation in einem engen zeitlichen Abstand mehrere Zufallszugriffspräambeln, welche dieselbe zufällig ausgewählte Zahlensequenz enthalten,
sendet sie entsprechend mehrere Zufallszugriffsantworten mit dieser, d. h. mit derselben Zahlensequenz aus. In einem solchen Fall ist eine eindeutige Zuordnung
von Zufallszugriffspräambel und Zufallszugriffsantwort durch die Endgeräte unter
Umständen nicht mehr gewährleistet (Absätze 0003 und 0004). Denn beim Empfang der Zufallszugriffsantworten durch die Endgeräte kann es zu einer Verwechslung kommen, da ein Endgerät die eigentlich für ein anderes Endgerät bestimmte
Zufallszugriffsantwort fälschlicherweise für seine eigene Zufallszugriffsantwort hält,
weil sich in einem solchen Fall die empfangenen Zufallszugriffsantworten allein anhand der darin enthaltenen Zahlensequenz nicht unterscheiden lassen.

Ein solches Szenario ist beispielhaft in der nachfolgend wiedergegebenen Figur 1a
des Streitpatents dargestellt, bei dem zwei Endgeräte („User equipment 1“, „User
equipment 2“) in engem zeitlichen Abstand jeweils eine Zufallszugriffspräambel
(S110, S120) mit derselben zufällig ausgewählten Zahlensequenz („Sequence number 1“) aussenden.




                                Figur 1a des Streitpatents

                                       - 13 -



Bei dem in der Figur 1a dargestellten Szenario empfangen beide Endgeräte zunächst die Zufallszugriffsantwort auf die zuerst bei der Basisstation eingegangene
Zufallszugriffspräambel (S110) und halten diese Zufallszugriffsantwort mit derselben Zahlensequenz („Response having sequence number 1“) für die Antwort auf
die jeweils eigene Zufallszugriffspräambel. In diesem Szenario ist die zunächst eingehende Zufallszugriffsantwort jedoch nur für das erste der beiden Endgeräte bestimmt, sodass das zweite Endgerät diese Zufallszugriffsantwort fälschlich als seine
eigene identifiziert (Absatz 0004).


2.    Das Streitpatent stellt sich im Hinblick auf den vorstehend dargestellten
Stand der Technik die Aufgabe, ein sicheres und effizientes Verfahren zum Empfangen einer Zufallszugriffsantwort bereitzustellen, welches verhindern soll, dass
ein Endgerät, welches eine Zufallszugriffspräambel mit einer zufällig ausgewählten
Zahlensequenz an eine Basisstation sendet, fälschlicherweise eine Zufallszugriffsantwort als Antwort empfängt, die eigentlich für ein anderes Endgerät bestimmt
war, welches mit derselben zufällig ausgewählten Zahlensequenz Zugang zum Mobilfunknetz erhalten wollte (Absatz 0010).

Diese Aufgabe soll mit Hilfe der Gegenstände der von der Klägerin angegriffenen
unabhängigen Patentansprüche 1 und 9 gelöst werden.


3.    Maßgeblicher Fachmann für die Bewältigung dieser Aufgabe ist ein Ingenieur mit einem universitären Abschluss (Diplom oder Master) der Elektrotechnik,
Fachrichtung Nachrichtentechnik, der über eine mehrjährige Erfahrung auf dem Gebiet der Entwicklung von Mobilfunksystemen unter Berücksichtigung von Mobilfunkstandards und Übertragungstechniken in Mobilfunknetzen verfügt, und der sich über
aktuelle Entwicklungen auf diesem Gebiet, auch hinsichtlich der LTE-Standardisierung, auf dem Laufenden hält.


4.    Die nachfolgenden Ausführungen zu den angegriffenen Patentansprüchen 1,
2 und 9 erfolgen anhand der senatsseitig vorgenommenen Merkmalsgliederung.
Die maßgebliche englische Fassung ist ebenso wie die deutsche Fassung der
Streitpatentschrift entnommen.

                                         - 14 -




Patentanspruch 1:

          in der Verfahrenssprache Englisch Übersetzung gemäß Streitpatent

M1        A method of receiving a random Verfahren zum Empfangen einer
          access      response,   the    method Zufallszugriffsantwort, das Verfahcomprising:                             ren umfassend:

M1.1      a user equipment (UE) transmits a ein Endgerät (UE) überträgt eine
          random access preamble to a Zufallszugriffspräambel an eine
          base      station   (Node-B)   (S430; Basisstation      (Node-B)     (S430;
          S930);                                  S930);

M1.2      the user equipment (UE) receives das Endgerät (UE) empfängt die
          the random access response cor- Zufallszugriffsantwort             entspreresponding to the random access chend der Zufallszugriffspräambel
          preamble from the base station von der Basisstation (Node-B)
          (Node-B) (S450; S950),                  (S450; S950),

M1.2.1    the received random access re- wobei die empfangene Zufallszusponse including information of a griffsantwort eine Information eitransmission time when the ran- ner Übertragungszeit, zu der die
          dom access preamble is transmit- Zufallszugriffspräambel           übertrated,                                    gen wird, umfasst,

M1.3      the user equipment (UE) deter- das Endgerät (UE) stellt fest, ob
          mines whether or not the received die            empfangene    Zufallszurandom access response is the re- griffsantwort die Antwort auf die
          sponse to the transmitted random übertragene Zufallszugriffspräamaccess preamble,                        bel ist oder nicht,

          characterized in that the method dadurch           gekennzeichnet,    dass
          further comprises:                      das Verfahren ferner umfasst:

                                  - 15 -



M1.4   the user equipment (UE) stores a das Endgerät (UE) speichert eine
       subframe number for transmitting Subrahmen-Nummer zum Überthe   random   access    preamble tragen der Zufallszugriffspräambel
       (S420);                             (S420);

M1.5   the information of the transmission die Information der Übertragungstime when the random access pre- zeit, zu der die Zufallszugriffspräamble is transmitted includes a ambel übertragen wird, umfasst
       number indicating the transmis- eine Nummer, welche auf die
       sion time of the random access Übertragungszeit der Zufallszupreamble, the number being a griffspräambel hindeutet, wobei
       number allocated to a subframe, in die Nummer eine einem Subrahwhich a random access channel, men zugewiesene Nummer ist, in
       RACH, slot is present,              welchem ein Zufallszugriffskanal,
                                           RACH,-Slot vorhanden ist,

M1.6   the user equipment (UE) checks das Endgerät (UE) prüft, ob die in
       whether the number included in der         empfangenen       Zufallszuthe received random access re- griffsantwort umfasste Nummer
       sponse is identical to the subframe identisch mit der Subrahmennumber of the transmitted random Nummer der übertragenen Zuaccess preamble stored by the fallszugriffspräambel,            welche
       user equipment (S460; S960),        durch das Endgerät gespeichert
                                           ist, ist (S460; S960),

M1.7   the user equipment (UE) deter- das Endgerät (UE) stellt fest, dass
       mines that the received random die         empfangene        Zufallszuaccess response is the response griffsantwort die Antwort auf die
       to the transmitted random access übertragene Zufallszugriffspräampreamble, if the number included bel ist, wenn die in der empfangein the received random access re- nen     Zufallszugriffsantwort   umsponse is identical to the subframe fasste Nummer identisch mit der
       number of the transmitted random Subrahmen-Nummer der übertragenen Zufallszugriffspräambel ist,

                                      - 16 -



          access preamble stored by the welche durch das Endgerät geuser equipment (S460; S960), and speichert ist (S460; S960), und

M1.8      the user equipment (UE) receives das Endgerät (UE) empfängt die
          the   random   access    response Zufallszugriffsantwort      innerhalb
          within a predetermined time span einer vorbestimmten Zeitspanne,
          including a predetermined time welche einen vorbestimmten Zeitpoint after a transmission time punkt nach einer Übertragungswhen the random access pream- zeit, zu der die Zufallszugriffspräble is transmitted, and the prede- ambel übertragen wird, umfasst,
          termined time point is obtained by und der vorbestimmte Zeitpunkt
          adding an offset time to the ran- dadurch erhalten wird, einen Zeitdom access preamble transmis- versatz zu der Zufallszugriffspräsion time.                           ambel-Übertragungszeit zu addieren.



Abhängiger Patentanspruch 2:

          in der Verfahrenssprache Englisch Übersetzung gemäß Streitpatent

          The method according to claim 1, Verfahren nach Anspruch 1, wobei
          wherein the number is the uplink die Nummer die Uplink-Subrahsubframe number of the time point men-Nummer des Zeitpunktes ist,
          when a user equipment (UE) zu dem ein Endgerät (UE) eine Zutransmits a random access pream- fallszugriffspräambel an eine Bable to a base station (Node-B).      sisstation (Node-B) überträgt.



Nebenanspruch 9:

          in der Verfahrenssprache Englisch Übersetzung gemäß Streitpatent

M9        A user equipment (UE) being Endgerät (UE), welches dazu einadapted                              gerichtet ist,

                                       - 17 -



M9.1     to transmit a random access pre- eine Zufallszugriffspräambel an
         amble to a base station (Node-B) eine Basisstation (Node-B) zu
         (S430; S930);                          übertragen (S430; S930);

M9.2     to receive a random access re- eine Zufallszugriffsantwort entsponse corresponding to the ran- sprechend der Zufallszugriffsprädom access preamble from the ambel               von       der   Basisstation
         base     station   (Node-B)   (S450; (Node-B) zu empfangen (S450;
         S950),                                 S950),

M9.2.1   the received random access re- wobei die empfangene Zufallszusponse including information of a griffsantwort eine Information eitransmission time when the ran- ner Übertragungszeit, zu der die
         dom access preamble is transmit- Zufallszugriffspräambel             übertrated, and                               gen wird, umfasst, und

M9.3     to determine whether or not the re- festzustellen, ob die empfangene
         ceived random access response is Zufallszugriffsantwort die Antwort
         the response to the transmitted auf die übertragene Zufallszurandom access preamble,                griffspräambel ist oder nicht,

         characterized in that                  dadurch gekennzeichnet, dass

M9.5     the information of the transmission die Information der Übertragungstime when the random access pre- zeit, zu der die Zufallszugriffspräamble is transmitted includes a ambel übertragen wird, eine Numnumber indicating the transmission mer umfasst, welche auf die Übertime of the random access pream- tragungszeit              der     Zufallszuble, the number being a number al- griffspräambel hindeutet, wobei
         located to a subframe, in which a die Nummer eine einem Subrahrandom access channel, RACH, is men zugewiesene Nummer ist, in
         present,                               welchem ein Zufallszugriffskanal,
                                                RACH, vorhanden ist,

         in that the user equipment is fur- dass das Endgerät ferner dazu
         ther adapted                           eingerichtet ist,

                                  - 18 -



M9.4   to store a subframe number for eine Subrahmen-Nummer zum
       transmitting the random access Übertragen der Zufallszugriffspräpreamble (S420);                    ambel zu speichern (S420);

M9.6   to check whether the number in- zu prüfen, ob die in der empfangecluded in the received random ac- nen     Zufallszugriffsantwort    umcess response is identical to the fasste Nummer identisch mit der
       subframe number of the transmit- Subrahmen-Nummer der übertrated   random   access   preamble genen        Zufallszugriffspräambel,
       stored by the user equipment welche durch das Endgerät ge-
       (S460; S960), and                   speichert ist, ist (S460; S960), und

M9.7   to determine that the received ran- festzustellen, dass die empfandom access response is the re- gene        Zufallszugriffsantwort   die
       sponse to the transmitted random Antwort auf die übertragene Zuaccess preamble, if the number in- fallszugriffspräambel ist, wenn die
       cluded in the received random ac- in der empfangenen Zufallszucess response is identical to the griffsantwort umfasste Nummer
       subframe number of the transmit- identisch mit der Subrahmented   random   access   preamble Nummer der übertragenen Zustored by the user equipment fallszugriffspräambel,              welche
       (S460; S960), and                   durch das Endgerät gespeichert
                                           ist, ist (S460; S960), und

M9.8   in that the user equipment (UE) dass das Endgerät (UE) ein Mittel,
       comprises means arranged to re- welches dazu angeordnet ist, die
       ceive the random access response Zufallszugriffsantwort von der Bafrom the base station (Node-B) sisstation (Node-B) innerhalb eiwithin a predetermined time span ner vorbestimmten Zeitspanne zu
       including a predetermined time empfangen, welche einen vorbepoint after a transmission time of stimmten Zeitpunkt nach einer
       the random access preamble, and Übertragungszeit der Zufallszumeans arranged to obtain the pre- griffspräambel umfasst, und ein
       determined time point as the sum Mittel, das dazu angeordnet ist,

                                        - 19 -



           of an offset time and the random den vorbestimmten Zeitpunkt als
           access    preamble     transmission die Summe eines Zeitversatzes
           time.                                 und der ZufalIszugriffspräambel-Übertragungszeit zu erhalten, umfasst.




5.      Zur Auslegung der Ansprüche

Die Merkmale der angegriffenen Patentansprüche 1, 2 und 9 bedürfen der Erläuterung.

5.1     Patentanspruch 1

Der Patentanspruch 1 betrifft ein Verfahren zum Empfangen einer Zufallszugriffsantwort („random access response“) (Merkmal M1), d. h. ein Verfahren aus
Sicht eines Endgerätes. Aus fachmännischer Sicht stellt das Versenden (durch eine
Basisstation) und das Empfangen (durch ein Endgerät) einer Zufallszugriffsantwort
jeweils einen von mehreren Schritten innerhalb eines Zufallszugriffsverfahrens
(„random access procedure“) dar.

Hierbei ist vorgesehen, dass das Endgerät eine Zufallszugriffspräambel („random
access preamble”) an die Basisstation (sog. „Node-B“) sendet (Merkmal M1.1), und
eine hierzu korrespondierende Zufallszugriffsantwort von der Basisstation empfängt
(Merkmal M1.2).

Gemäß dem Merkmal M1.2.1 umfasst diese vom Endgerät empfangene Zufallszugriffsantwort eine Information einer „Übertragungszeit, zu der die Zufallszugriffspräambel [von dem Endgerät an die Basisstation] übertragen wird“. Der Gesamtoffenbarung des Streitpatents entnimmt der Fachmann, dass mit dem Begriff „Übertragungszeit“ („transmission time“) nicht die Dauer der Übertragung der Zufallszugriffspräambel gemeint ist, sondern der Übertragungszeitpunkt zu dem die Zufallszugriffspräambel von dem Endgerät an die Basisstation übertragen, d. h. ausgesendet, wurde (vgl. auch Merkmale M1.5 und M1.6).

                                       - 20 -



Das Merkmal M1.3 aus dem Oberbegriff des Patentanspruchs 1 nach Streitpatent
sieht vor, dass das Endgerät eine Feststellung trifft, ob die gemäß dem Merkmal M1.2 empfangene, von der Basisstation ausgesendete Zufallszugriffsantwort
diejenige Zufallszugriffsantwort ist, die sich auf die zuvor gemäß dem Merkmal M1.1
von dem Endgerät an die Basisstation gesendete Zufallszugriffspräambel bezieht,
oder ob sich die empfangene Zufallszugriffsantwort auf eine von einem anderen
Endgerät ausgesendete Zufallszugriffspräambel bezieht.

Wie diese Feststellung konkret erfolgen soll, wird durch die Merkmale aus dem
kennzeichnenden Teil des Patentanspruchs 1 nach Streitpatent definiert. Ziel dieser
Feststellung ist es, einen irrtümlichen Empfang einer nicht für das entsprechende
Endgerät bestimmten Zufallszugriffsantwort zu verhindern (vgl. Streitpatent, Absatz 0033, erster Satz).


Gemäß dem Merkmal M1.4 speichert das Endgerät eine Subrahmen-Nummer „zum
Übertragen“ („for transmitting“) der Zufallszugriffspräambel. Die Formulierung „zum
Übertragen“ versteht der Fachmann auch unter Berücksichtigung der Merkmale M1.6 und M1.7 dahingehend, dass es sich bei der zu speichernden Subrahmen-Nummer um die kennzeichnende Nummer oder eine davon abgeleitete Nummer (s. u.) jenes Subrahmens handelt, innerhalb dessen die Zufallszugriffspräambel
von dem Endgerät an die Basisstation ausgesendet wird.

Bei dem aus dem Streitpatent bekannten Verfahren erfolgt ebenso wie bei den zum
Zeitpunkt der Anmeldung des Streitpatents aus dem Stand der Technik bekannten
Zufallszugriffsverfahren das Aussenden der Zufallszugriffspräambel innerhalb eines
bestimmten Zeitabschnitts eines Funksignals, welches das Endgerät an die Basisstation sendet. Auf der Zeitebene wird ein solches Funksignal in sogenannte Rahmen („frames“) unterteilt, wobei jeder Rahmen eine zeitliche Länge von 10 ms aufweist. Ein Rahmen besteht aus zehn sogenannten Subrahmen („subframes“) mit
jeweils einer zeitlichen Länge von 1 ms; jeder Subrahmen besteht wiederum aus
zwei sogenannten Slots („slots“) mit einer zeitlichen Länge von je 0,5 ms (Figur 2a;
Absätze 0026 und 0027).

                                         - 21 -



Aufgrund der Subrahmen-Nummer lässt sich somit auf den Übertragungszeitpunkt
schließen, zu dem die Zufallszugriffspräambel vom Endgerät ausgesendet wurde,
da jeder Subrahmen sich auf eine bestimmte Zeitspanne von 1 ms bezieht.

Allerdings ist unter der in Patentanspruch 1 nach Streitpatent erwähnten „Subrahmen-Nummer“ nicht nur die Subrahmen-Nummer in engerem Sinne zu verstehen,
d. h. die kennzeichnende Nummer jenes Subrahmens selbst, innerhalb dessen die
Zufallszugriffspräambel von dem Endgerät an die Basisstation ausgesendet wird.
Vielmehr umfasst der Begriff „Subrahmen-Nummer“ auch von der o. g. Subrahmen-Nummer „abgeleitete Nummern“, die dazu geeignet sind, den Subrahmen des Übertragungszeitpunktes zu identifizieren, zu dem die Zufallszugriffspräambel vom Endgerät ausgesendet wurde.


Auch wenn das Merkmal M1.2.1 von einer „Information einer Übertragungszeit, zu
der die Zufallszugriffspräambel übertragen wird“ spricht, welche gemäß den Merkmalen M1.5 und M1.6 eine Nummer umfasst, wobei die Nummer gemäß dem Merkmal M1.5 eine einem Subrahmen zugewiesene („allocated“) Nummer ist, ist das
Übertragen der Subrahmen-Nummer selbst als Teil der Zufallszugriffspräambel,
d. h. vom Endgerät an die Basisstation, in der Beschreibung des Streitpatents im
Zusammenhang mit nicht einschränkenden Ausführungsbeispielen beschrieben
(Seite 6, Zeilen 42 und 43, i. V. m. Figur 3a: „[…] the uplink subframe numbers of
the random access preambles transmitted by the user equipment 1 and the user
equipment 2.“; Seite 8, Zeile 1, i. V. m. Figur 5a: „[…] the sequence number 1 and
the uplink subframe number sf_F_N=O included in the random access preamble
[…]“; Seite 9, Zeilen 23 bis 26, i. V. m. Figur 9: „The user equipment 1 and the user
equipment 2 extract the uplink subframe numbers at time points when the random
access preambles are transmitted and include the extracted uplink subframe numbers in the random access preambles to be transmitted, in steps S920 and S920’,
respectively.“; Seite 9, Zeilen 28 und 29, i. V. m. Figur 9: „[…] the respective uplink
subframe numbers included in the random access preambles transmitted by the
user equipment 1 and the user equipment 2 […]“).

                                      - 22 -



Im Zusammenhang mit dem Ausführungsbeispiel nach der Figur 8 beschreibt das
Streitpatent die Möglichkeit, Subrahmen-Nummern neu zuzuweisen (Seite 9, Zeilen 9 und 10: „[…] are reallocated […]“) und ggfs. zusätzlich eine Gruppierungsmethode, z. B. die Modulo-Funktion, anzuwenden. Im Unterschied zu den Ausführungsbeispielen nach den Figuren 5a und 7a bzw. 7b ist bei dem Ausführungsbeispiel nach der Figur 8 explizit vorgesehen, dass die im Verfahrensschritt S820 neu
zugewiesene Subrahmen-Nummer vom Endgerät im Verfahrensschritt S840 gespeichert wird (Absatz 0050: „In a step S810, subframes in which an RACH slot is
present are detected. In a step S820, numbers are reallocated to only the uplink
subframes in which the RACH slot is present. In a step S830, the reallocated number of an uplink subframe at a time point when a random access will be transmitted
is decided. In a step S840, the decided reallocated number is stored. Although, in
this embodiment, the RACH slots are present only in even-numbered frames, the
RACH slots may be present in any numbered frames. That is, the reallocation of the
numbers in the step S830 may use the grouping method. In more detail, the modulo
operation may be used.”).

Dies berücksichtigend, entnimmt der Fachmann dem Streitpatent, dass es sich bei
der vom Endgerät gespeicherten Subrahmen-Nummer um die Subrahmen-Nummer
selbst oder um eine davon abgeleitete Nummer handeln kann.


Der Zusammenhang der in den Merkmalen M1.4 und M1.5 erwähnten Nummern
wird in den Merkmalen M1.6 und M1.7 erläutert.


Das Merkmal M1.6 sieht eine Prüfung dahingehend vor, ob die gemäß dem Merkmal M1.4 im Endgerät gespeicherte Subrahmen-Nummer mit der in der empfangenen Zufallszugriffsantwort gemäß dem Merkmal M1.2.1 enthaltenen Nummer („Information der Übertragungszeit“) übereinstimmt. Die inhaltliche Definition dieser
Prüfung erfolgt im Merkmal M1.7.


Das Merkmal M1.7 definiert als erste Bedingung für die Feststellung, dass die vom
Endgerät empfangene Zufallszugriffsantwort die Antwort auf die von dem Endgerät
übertragene Zufallszugriffspräambel ist, dass die gemäß dem Merkmal M1.4 im

                                        - 23 -



Endgerät gespeicherte Subrahmen-Nummer mit der in der empfangenen Zufallszugriffsantwort gemäß dem Merkmal M1.2.1 enthaltenen Nummer („number“) übereinstimmt. Bei einem solchermaßen positiven Ergebnis der in den Merkmalen M1.6
und M1.7 beschriebenen Prüfung weiß das Endgerät somit, dass die empfangene
Zufallszugriffsantwort sich auf die von diesem Endgerät ausgesendete Zufallszugriffspräambel bezieht, und nicht etwa eine Zufallszugriffsantwort auf eine von einem anderen Endgerät ausgesendete Zufallszugriffspräambel ist.


Dem Patentanspruch 1 nach Streitpatent ist keine weiterführende inhaltliche Definition der im Merkmal M1.5 erwähnten Nummer („number“) zu entnehmen, insbesondere kann dem Patentanspruch 1 nicht entnommen werden, dass es sich bei der im
Merkmal M1.5 erwähnten Nummer („number“) um die Subrahmen-Nummer selbst
handeln muss.
Erst im abhängigen Patentanspruch 2 nach Streitpatent wird definiert, dass es sich
bei der im Merkmal M1.5 erwähnten Nummer um die Uplink-Subrahmen-Nummer
des Zeitpunktes handelt, zu dem das Endgerät eine Zufallszugriffspräambel an eine
Basisstation überträgt, d. h. um die Subrahmen-Nummer selbst. Gemäß den nicht
angegriffenen abhängigen Patentansprüchen 3 und 4 ist die im Merkmal M1.5 erwähnte Nummer als eine durch eine Modulo-Funktion erhaltene Nummer definiert.


Das Merkmal M1.8 sieht als zweite Bedingung für die Feststellung, dass die empfangene Zufallszugriffsantwort die Antwort auf die übertragene Zufallszugriffspräambel ist (Merkmal M1.7), vor, dass der Empfang der von der Basisstation ausgesendeten Zufallszugriffsantwort durch das Endgerät innerhalb einer vorbestimmten
Zeitspanne nach dem Aussenden der Zufallszugriffspräambel durch das Endgerät
zu erfolgen hat, d. h. dass die Zufallszugriffsantwort vom Endgerät innerhalb dieser
Zeitspanne empfangen wird. Diese vorbestimmte Zeitspanne umfasst als zeitliche
End-Begrenzung gemäß dem Merkmal M1.8 einen Zeitpunkt, der ermittelt wird, indem ein Zeitversatz zum Übertragungszeitpunkt der Zufallszugriffspräambel hinzuaddiert wird. Kriterien bzw. eine Definition hinsichtlich der Länge dieser vorbestimmten Zeitspanne können weder dem Patentanspruch 1 noch dem Rest der Streitpatentschrift entnommen werden.

                                        - 24 -



5.2   Abhängiger Patentanspruch 2

Der Patentanspruch 2 nach Streitpatent definiert, dass es sich bei der im Merkmal M1.5 erwähnten, von der vom Endgerät empfangenen Zufallszugriffsantwort
umfassten Nummer, um die Uplink-Subrahmen-Nummer des Zeitpunktes handelt,
zu dem ein Endgerät eine Zufallszugriffspräambel an eine Basisstation überträgt,
d. h. aussendet, und somit um die Subrahmen-Nummer selbst.


5.3   Nebenanspruch 9

Die Ausführungen zu den Merkmalen M1 bis M1.8 aus dem Patentanspruch 1 nach
Streitpatent gelten sinngemäß in entsprechender Weise auch für die Merkmale M9
bis M9.8 aus dem Nebenanspruch 9 nach Streitpatent.




                       II. Zur erteilten Fassung (Hauptantrag)


Die zulässige Klage, die sich gegen die Patentansprüche 1, 2 und 9 des Streitpatents richtet, hat in der Sache teilweise und zwar hinsichtlich der erteilten Fassung
des Streitpatents Erfolg. Insoweit ist, obwohl die angegriffenen Patentansprüche 1, 2 und 9 nicht unzulässig erweitert und ausführbar sind, jedenfalls der Nichtigkeitsgrund der mangelnden Patentfähigkeit gemäß Art. II § 6 Abs. 1 Nr. 1 Int-PatÜG, Art. 138 Abs. 1 Buchst. a) EPÜ i. V. m. Art. 52, 54, 56 EPÜ gegeben.

Da die Dokumente NK4 bis NK7 vorveröffentlichten Stand der Technik darstellen,
nachdem das Streitpatent die Priorität der US-amerikanischen Voranmeldung
US 18492 P (engl.-sprach. Übersetzung als Dokument NK3-P1) vom 1. Januar 2008 materiell nicht wirksam in Anspruch nehmen kann, kann dahinstehen, ob
die Gegenstände der unabhängigen Patentansprüche 1 und 9 nach Streitpatent gegenüber dem Stand der Technik nach den Dokumenten NK4 bis NK 7 neu sind und
hinsichtlich den Dokumenten NK4 und NK5 auch auf einer erfinderischen Tätigkeit
beruhen. Gegenüber dem Stand der Technik ergeben sie sich für den Fachmann in
naheliegender Weise ausgehend von der Lehre des Dokuments NK6 unter Berücksichtigung der Lehre des Dokuments NK7.

                                          - 25 -



1.        Entgegen der Auffassung der Klägerin geht der Gegenstand der erteilten Patentansprüche 1, 2 und 9 nicht über den Inhalt der ursprünglichen Anmeldeunterlagen (offengelegt als WO 2009/084924 A2 = NK3-PCT) hinaus.


1.1       Zum Patentanspruch 1 nach Streitpatent
Die Merkmale M1 bis M1.6 des Gegenstands des Patentanspruchs 1 nach Streitpatent sind in den Anmeldeunterlagen ursprungsoffenbart.

Entgegen der Annahme der Klägerin führen auch die Merkmale M1.7 und M1.8 zu
keiner unzulässigen Erweiterung des Gegenstands des Patentanspruchs 1 nach
Streitpatent. Insbesondere ist
     a)    eine Verwendung eines Zeitversatzes (Merkmal M1.8) zusammen mit einer
           Übertragungszeit (Merkmale M1.2 bis M1.7) offenbart; und
     b)    eine Verwendung eines Zeitversatzes (Merkmal M1.8) nicht nur im Zusammenhang mit weiteren Merkmalen offenbart.


1.1.1 Verwendung eines Zeitversatzes (Merkmal M1.8) zusammen mit einer
Übertragungszeit (Merkmale M1.2 bis M1.7)

Zwar sieht der Patentanspruch 1 nach Streitpatent eine zweiteilige Prüfung der
empfangenen Zufallszugriffsantwort vor. Zum einen soll die Zufallszugriffsantwort
eine Information umfassen, die sich auf den Übertragungszeitpunkt der zugehörigen
Zufallszugriffspräambel bezieht (vgl. Merkmale M1.2 bis M1.7). Zum anderen soll
die Zufallszugriffsantwort innerhalb einer vorbestimmten Zeitspanne empfangen
werden, die auf Basis eines vorbestimmten Zeitversatzes zum Übertragungszeitpunkt der Zufallszugriffspräambel bestimmt wird (vgl. Merkmal M1.8). Der Fachmann erkennt allerdings, dass es sich dabei um sich ergänzende Aspekte im Rahmen der Gesamtoffenbarung der Erfindung handelt.

Wie die Klägerin sieht der Senat, dass ursprünglich drei unabhängige Patentansprüche 1, 7 und 10 eingereicht worden sind, wobei

     -    Patentanspruch 1 auf ein Verfahren gerichtet ist, das durch ein Endgerät auszuführen ist, und bei dem eine Information über die Übertragungszeit, d. h.
          den Übertragungszeitpunkt, der Zufallszugriffspräambel durch das Endgerät

                                       - 26 -



      als Teil der Zufallszugriffsantwort der Basisstation gesendet und von dem
      Endgerät empfangen wird (Teil des Merkmals M1.7);
  -   Patentanspruch 10 auf ein Verfahren gerichtet ist, das durch ein Endgerät
      auszuführen ist, und bei dem die Zufallszugriffsantwort innerhalb einer vorbestimmten Zeitspanne vom Endgerät empfangen werden soll, wobei die
      Zeitspanne einen vorbestimmten Zeitversatz zum Übertragungszeitpunkt der
      Zufallszugriffspräambel durch das Endgerät aufweist (Teil des Merkmals M1.8); und
  -   Patentanspruch 7 auf ein Verfahren gerichtet ist, das durch eine Basisstation
      auszuführen ist, und auf die Verwendung einer Übertragungszeit (korrespondierend zum Patentanspruch 1) oder einer basisstationsinternen Verarbeitungsverzögerungszeit als Teil der Zufallszugriffsantwort gerichtet ist.

Das endgeräteseitige Empfangen einer Information über die Übertragungszeit, d. h.
des Übertragungszeitpunkts, der Zufallszugriffspräambel durch das Endgerät (vgl.
ursprünglich eingereichter Patentanspruch 1) und das Vorsehen eines vorbestimmten Zeitversatzes für den endgeräteseitigen Empfang der Zufallszugriffsantwort (vgl.
ursprünglich eingereichter Patentanspruch 10) werden somit in den Anmeldeunterlagen durch separate unabhängige Patentansprüche beansprucht. Auch die ursprünglich eingereichten abhängigen Patentansprüche stellen keine unmittelbare
Offenbarung für die Kombination dieser beiden Verfahren bereit.

In den ursprünglich eingereichten Figuren sowie den zu diesen einzelnen Figuren
korrespondierenden Teilen der ursprünglich eingereichten Beschreibung sind die
durch die Merkmale M1.7 (vgl. Figuren 3 und 4) und M1.8 (vgl. Figur 13) des Patentanspruchs 1 nach Streitpatent definierten zwei Prüfaspekte ebenfalls mittels
voneinander unabhängiger Ausführungsbeispiele offenbart.

Soweit die Klägerin die Ansicht vertritt, dass es sich bei den durch die Merkmale M1.7 und M1.8 definierten Prüfaspekten um zwei voneinander unabhängige
Alternativen zur Erreichung desselben Ziels handle, ohne eine klare und eindeutige
Offenbarung für die gemeinsame Verwendung dieser beiden Alternativen, sieht der
Senat dies nicht. Auch soweit die Klägerin dies damit begründet, dass in der ur-

                                        - 27 -



sprünglich eingereichten Beschreibung im Zusammenhang mit der durch die Ausführungsform nach der Figur 13 dargestellten Alternative (Merkmal M1.8) als Vorteil
dieser Ausführungsform erläutert werde, dass mit dieser Ausführungsform im Vergleich zu der Ausführungsform nach den Figuren 3 und 4 der Signalisierungsaufwand verringert werden könne, da die entsprechenden Informationen hinsichtlich
des Übertragungszeitpunktes bzw. der Subrahmen-Nummer der Zufallszugriffspräambel nicht als Teil der Zufallszugriffsantwort übertragen werden müssten (vgl.
Seite 28, Zeile 24 bis Seite 29, Zeile 3 der Anlage NK3-PCT), teilt der Senat diese
Ansicht nicht.

Denn in der ursprünglich eingereichten Beschreibung wird explizit darauf hingewiesen, dass die einzelnen in den Anmeldeunterlagen beschriebenen Ausführungsbeispiele nicht als voneinander unabhängig zu betrachten sind, sondern miteinander
kombiniert werden können – z. B. auch durch Kombination der Gegenstände unabhängiger Patentansprüche (vgl. Seite 32, Zeilen 14 bis 21: „Also, some constituent
components and/or characteristics may be combined to implement the embodiments of the present invention. The order of operations to be disclosed in the embodiments of the present invention may be changed to another. Some components
or characteristics of any embodiment may also be included in other embodiments,
or may be replaced with those of the other embodiments as necessary. It will be
apparent to those skilled in the art that unrelated claims are combined so as to configure embodiments or are included in new claims by amendments after an application.“).

Dabei spricht auch der im Zusammenhang mit der Ausführungsform nach der Figur 13 beschriebene Vorteil eines vergleichsweise verringerten Signalisierungsaufwands nicht gegen eine Verwendung einer vorbestimmten Zeitspanne (vgl. Merkmal M1.8) zusammen mit der Übertragung von Zeitinformationen (vgl. Merkmal M1.7), sondern vielmehr für eine gemeinsame Durchführung dieser beiden
Prüfteile. Denn dadurch, dass bei der Verwendung einer vorbestimmten Zeitspanne
(Merkmal M1.8) keine zusätzlichen Zeitinformationen übertragen werden müssen,
erkennt der Fachmann darin eine einfache Möglichkeit, dieses Kriterium bei der
Auswertung der empfangenen Zufallszugriffsantwort zusätzlich zur Auswertung des

                                         - 28 -



empfangenen      Übertragungszeitpunktes          der   Zufallszugriffspräambel   (Merkmal M1.7) hinzuzuziehen, um dadurch die Fehleranfälligkeit des Zufallszugriffsverfahrens weiter zu reduzieren, ohne dass hierfür zusätzliche Signalisierungsinformationen als Teil der Zufallszugriffsantwort übertragen werden müssen. Aus fachmännischer Sicht handelt es sich bei den Ausführungsformen nach den Figuren 3 und 4
(vgl. Merkmal M1.7) und nach der Figur 13 (vgl. Merkmal M1.8) daher um sich ergänzende Aspekte im Rahmen der Gesamtoffenbarung der Erfindung.

Das Merkmal M1.7 ist demnach in Verbindung mit dem Merkmal M1.8 ursprünglich
offenbart.


1.1.2 Verwendung eines Zeitversatzes (Merkmal M1.8)

Entgegen der Ansicht der Klägerin bedingt die Verwendung eines Zeitversatzes in
dem beanspruchten Verfahren weder die explizite Erwähnung, eine korrespondierende Zeitspanne werde durch das Endgerät festgelegt, noch, dass vom Endgerät
eine Bestimmung durchgeführt wird, ob die Zufallszugriffsantwort innerhalb der vorbestimmten Zeitspanne empfangen wird.


Grundlage für die Ursprungsoffenbarung des Merkmals M1.8 ist insbesondere die
zusammenfassende Beschreibung der Ausführungsformen nach den Figuren 11
bis 13 (vgl. Seite 26, Zeilen 6 bis 14: „FIGs. 11, 12 and 13 are views facilitating the
understanding of the other embodiments of the present invention, which show the
principle of an ARQ, the principle of a HARQ and a detailed example of a HARQ
process, respectively. In the other embodiments of the present invention, a user
equipment waits for a response at a predetermined time period. The user equipment
which transmits a random access preamble can previously know a time point when
a response of the random access preamble transmitted by the user equipment is
transmitted, on the basis of the predetermined time period.“), sowie die konkrete
Beschreibung der Ausführungsform nach der Figur 13 (siehe zuvor unter II. 1. 1.1a)
zusammen mit einer Übertragungszeit (Merkmale M1.2 bis M1.7)).

Darüber hinaus ist nicht ersichtlich, warum es „essenziell“ sein sollte, dass das Endgerät die vorbestimmte Zeitspanne festlegt. Wesentlich ist vielmehr die Tatsache,

                                        - 29 -



dass im Endgerät eine vorbestimmte Zeitspanne für den (erwarteten) Empfang der
Zufallszugriffsantwort verwendet wird. Welche Systemkomponente diese Zeitspanne festlegt, ist für den Ablauf des erfindungsgemäßen Verfahrens hingegen
nicht relevant. Im Übrigen wird auch im ursprünglich eingereichten Nebenanspruch 10 nicht definiert, dass der vorbestimmte Zeitpunkt („predetermined time
point“) durch das Endgerät festgelegt wird, auch wenn dies aus fachmännischer
Sicht die naheliegendste Realisierungsmöglichkeit sein dürfte (Vermeidung zusätzlich notwendiger Signalisierungen zwischen Basisstation und Endgerät).

Daher fordert das Merkmal M1.8 für den Fachmann erkennbar, dass das Endgerät
bestimmt, d. h. überprüft, ob es die Zufallszugriffsantwort der Basisstation innerhalb
der vorbestimmten Zeitspanne empfangen hat, da das Endgerät seine weitere Vorgehensweise von dem Ergebnis dieser Bestimmung bzw. Überprüfung abhängig
macht.


1.2   Zum abhängigen Patentanspruch 2 nach Streitpatent
Entgegen der Annahme der Klägerin ist eine unzulässige Erweiterung des Gegenstands des Patentanspruchs 2 nach Streitpatent schon nicht in dessen Rückbezug
auf den Patentanspruch 1 nach Streitpatent begründet, so dass der Gegenstand
des erteilten Patentanspruch 2 aus denselben Gründen wie der Gegenstand des
erteilten Patentanspruchs 1 nicht unzulässig erweitert ist.

Darüber hinaus sind die zusätzlichen Merkmale des Gegenstands des erteilten Patentanspruchs 2 z. B. auf der Seite 14, Zeilen 4 bis 7, und Seite 14, Zeile 24 bis
Seite 15, Zeile 3 i. V. m. Figur 3a der Anmeldeunterlagen offenbart.


1.3   Zum Nebenanspruch 9 nach Streitpatent
Der Senat sieht, wie die Klägerin, dass die Ausführungen zum erteilten Patentanspruch 1 mutatis mutandis für die entsprechenden Merkmale des Gegenstands des
erteilten Nebenanspruchs 9 gelten, jedoch mit der von der Ansicht der Klägerin abweichenden Konsequenz, dass der Gegenstand des erteilten Nebenanspruchs 9
ebenfalls nicht über den Offenbarungsgehalt der Anmeldeunterlagen hinausgeht.

                                         - 30 -



2.     Die Gegenstände der Patentansprüche 1, 2 und 9 nach Streitpatent sind in
der Streitpatentschrift auch so deutlich und vollständig offenbart, dass ein Fachmann diese ausführen kann.

Die nachfolgenden Ausführungen zum Patentanspruch 1 nach Streitpatent gelten
mutatis mutandis auch für den Nebenanspruch 9 nach Streitpatent.


2.1    Kombination zweier Ausführungsformen in den Merkmalen M1.7 und M1.8
Entgegen der Ansicht der Klägerin ist die Kombination der Ausführungsformen
„Senden der Übertragungszeit der Zufallszugriffspräambel als Teil der Zufallszugriffsantwort“ (Teil des Merkmals M1.7) und „Empfangen der Zufallszugriffsantwort
innerhalb einer vorbestimmten Zeitspanne“ (Teil des Merkmals M1.8) in der Streitpatentschrift offenbart und für den Fachmann ausführbar.

Die beiden Ausführungsformen „Senden der Übertragungszeit der Zufallszugriffspräambel als Teil der Zufallszugriffsantwort“ (nachfolgend als „erste Ausführungsform“ bezeichnet) und „Empfangen der Zufallszugriffsantwort innerhalb einer
vorbestimmten Zeitspanne“ (nachfolgend als „zweite Ausführungsform“ bezeichnet)
sind, und insoweit unstreitig, für sich genommen in der Beschreibung und in den
Figuren der Streitpatentschrift jeweils so deutlich und vollständig offenbart, dass ein
Fachmann anhand dieser Angaben und unter Verwendung seines Fachwissens
ohne Weiteres in der Lage ist, die jeweils offenbarte technische Lehre praktisch zu
verwirklichen.

Es sind weder Widersprüche noch Kompatibilitätsprobleme oder sonstige technische Schwierigkeiten erkennbar, welche den Fachmann von einer Kombination der
beiden o. g. Ausführungsformen im Rahmen eines endgeräteseitig zu implementierenden Verfahrens gemäß dem Patentanspruch 1 nach Streitpatent abhalten könnten.

Eine Kombination der beiden Ausführungsformen ist im Streitpatent zudem nicht
explizit ausgeschlossen.

                                         - 31 -



Daher sieht der Senat eine Kombination der beiden o. g. Ausführungsformen innerhalb eines endgeräteseitig zu implementierenden Verfahrens gemäß dem Patentanspruch 1 nach Streitpatent als für den Fachmann so deutlich und vollständig
offenbart, dass er auch diese Kombination ausführen kann.

Auch soweit die Klägerin ausführt, dass bei einer Kombination der beiden o. g. Ausführungsformen innerhalb eines endgeräteseitig zu implementierenden Verfahrens
der im Absatz 0063 der Streitpatentschrift angeblich offenbarte Erfindungsgedanke,
den Signalisierungsaufwand dadurch zu verringern, dass anstelle der Übertragung
der Übertragungszeit (erste Ausführungsform) ein Zeitversatz (zweite Ausführungsform) verwendet wird, nicht erzielt werden könne, sieht der Senat dies nicht. Auch
die Begründung der Klägerin, dass gemäß Patentanspruch 1 nach Streitpatent als
Teil der Zufallszugriffsantwort auch die Übertragungszeit der Zufallszugriffspräambel gesendet werde (erste Ausführungsform), und dadurch kein Signalisierungsaufwand eingespart werde und somit der Gegenstand des Patentanspruchs 1 nach
Streitpatent, also die Kombination der beiden Ausführungsformen, auch aufgrund
der im Streitpatent beschriebenen Aufgabe für den Fachmann nicht als erfindungszugehörig zu entnehmen sei, teilt der Senat nicht.


Zunächst kann festgestellt werden, dass sich das Streitpatent gemäß dem Absatz 0010 der Streitpatentschrift die Aufgabe stellt, ein sicheres und effizientes Verfahren zum Empfangen einer Zufallszugriffsantwort bereitzustellen, welches verhindern soll, dass ein Endgerät, welches eine Zufallszugriffspräambel mit einer zufällig
ausgewählten Zahlensequenz an die Basisstation sendet, fälschlicherweise eine
Zufallszugriffsantwort als Antwort empfängt, die eigentlich für ein anderes Endgerät
bestimmt ist, welches mit derselben zufällig ausgewählten Zahlensequenz Zugang
zum Mobilfunknetz erhalten wollte.

Der von der Klägerin referenzierte Absatz 0063 der Streitpatentschrift bezieht sich
auf die Ausführungsform nach der Figur 13, welche eine Implementierung der o. g.
zweiten Ausführungsform, d. h. unter Berücksichtigung des Merkmals M1.8, wiedergibt. Daher handelt es sich bei dem im Absatz 0063 beschriebenen Vorteil um einen
relativen Vorteil dieser Ausführungsform, im Vergleich zu anderen in der Streitpatentschrift offenbarten Ausführungsformen. Für den Fachmann bedeutet dies, dass

                                        - 32 -



bei einer Implementierung der o. g. ersten Ausführungsform (Merkmal M1.7) die zusätzliche Implementierung der o. g. zweiten Ausführungsform (Merkmal M1.8),
d. h., dass die Zufallszugriffsantwort innerhalb einer vorbestimmten Zeitspanne von
dem Endgerät zu empfangen ist, keinen zusätzlichen Signalisierungs-Overhead erfordert. Der Fachmann erkennt eine Kombination der ersten Ausführungsform und
der zweiten Ausführungsform aufgrund des Hinweises im Absatz 0063 der Streitpatentschrift als besonders vorteilhaft, um ohne zusätzlichen Signalisierungs-Overhead die Fehleranfälligkeit des resultierenden Zufallszugriffsverfahrens weiter reduzieren zu können.

Diese Kombination der beiden o. g. Ausführungsformen kann der Fachmann auch
ausführen und zugleich damit die in der Streitpatentschrift genannte Aufgabe erfüllen.


2.2    Entgegen der Ansicht der Klägerin sieht der Senat die Ausführbarkeit des
Patentanspruchs 1 nach Streitpatent nicht dadurch in Frage gestellt, dass das Merkmal M1.8 des Gegenstands des Patentanspruchs 1 nach Streitpatent nicht mit einer
expliziten Bestimmung, d. h. Überprüfung, verknüpft ist, ob die Zufallszugriffsantwort innerhalb der vorbestimmten Zeitspanne tatsächlich empfangen wurde, sondern diesbezüglich allgemein gehalten ist. Auch, dass die Beschreibung des Streitpatents im vorletzten Satz von Absatz 0066 eine entsprechende Überprüfung
(„check“) seitens des Endgerätes offenbare, und dem Fachmann somit in der Streitpatentschrift kein anderer Weg außer dem o. g. expliziten endgeräteseitigen „check“
im Zusammenhang mit der Verwendung eines Zeitversatzes offenbart werde und
damit der Patentanspruch 1 nach Streitpatent nicht über seine gesamte Breite ausführbar sei, sieht der Senat nicht.

Grundlage für die Offenbarung des Merkmals M1.8 in der Streitpatentschrift ist insoweit insbesondere die zusammenfassende Beschreibung der Ausführungsformen nach den Figuren 11 bis 13 (vgl. Absätze 0055 und 0056). In Absatz 0056 der
Streitpatentschrift ist auch die Möglichkeit offenbart, dass der Empfang der Zufallszugriffsantwort durch ein Endgerät während der im Merkmal M1.8 beschriebenen
Zeitspanne abgewartet wird: „In the other embodiments of the present invention, a
user equipment waits for a response at a predetermined time period. The user

                                       - 33 -



equipment which transmits a random access preamble can previously know a time
point when a response of the random access preamble transmitted by the user
equipment is transmitted, on the basis of the predetermined time period.“.

Die im Absatz 0056 der Streitpatentschrift beschriebene Vorgehensweise fordert
zumindest implizit, dass das Endgerät bestimmt, d. h. überprüft, ob es die Zufallszugriffsantwort der Basisstation innerhalb der vorbestimmten Zeitspanne tatsächlich
empfangen hat, da das Endgerät seine weitere Vorgehensweise von dem Ergebnis
dieser Bestimmung bzw. Überprüfung abhängig macht.


Daher ist das Merkmal M1.8 für den Fachmann so deutlich und vollständig offenbart, dass er es ausführen kann.


3.    Der Gegenstand der unabhängigen Patentansprüche 1 und 9 nach Streitpatent ergibt sich für den Fachmann gegenüber dem Stand der Technik in naheliegender Weise ausgehend von der Lehre dem Dokument NK6 unter Berücksichtigung
der Lehre des Dokuments NK7.

Bei den Dokumenten NK6 und NK7 handelt es sich um zu berücksichtigenden, vorveröffentlichten Stand der Technik, da das Streitpatent die Priorität der US-amerikanischen Voranmeldung US 18492 P (engl.-sprach. Übersetzung als Anlage NK3-
P1) vom 1. Januar 2008 materiell nicht wirksam in Anspruch nehmen kann.

Die Frage, ob das Streitpatent die Priorität der koreanischen Voranmeldung
KR 20080047656 vom 22. Mai 2008 materiell wirksam in Anspruch nimmt, kann dahinstehen, nachdem alle von der Klägerin genannten Dokumente NK4 bis NK7 vor
dem Anmeldetag der koreanischen Voranmeldung veröffentlicht worden sind.


3.1   Die US-amerikanische Voranmeldung US 18492 P erfolgte am 1. Januar 2008 in koreanischer Sprache. Nachfolgende Referenzierungen im Zusammenhang mit der US-amerikanischen Voranmeldung beziehen sich auf die von der
Klägerin vorgelegte beglaubigte englischsprachige Übersetzung (= Dokument NK3-
P1). Hierbei ist zu berücksichtigen, dass in dem Dokument NK3-P1 zwei mit „FIG. 1“
bezeichnete Figuren enthalten sind. Um Verwechslungen zu vermeiden, wird daher

                                          - 34 -



nachfolgend im Zusammenhang mit einer Referenzierung auf eine dieser beiden
Figuren 1 immer die zugehörige Seitenzahl (Seite 3 bzw. 5) angegeben.


3.1.1     Die US-amerikanische Voranmeldung offenbart die beanspruchte Kombination von „Senden der Übertragungszeit der Zufallszugriffspräambel als Teil der
Zufallszugriffsantwort“ (Teil des Merkmals M1.7) und „Empfangen der Zufallszugriffsantwort innerhalb einer vorbestimmten Zeitspanne“ (Teil des Merkmals M1.8)
nicht.

In dem Dokument NK3-P1 werden ausgehend vom Stand der Technik (vgl. Figur 1
auf Seite 3) mehrere Ausführungsbeispiele beschrieben.

•       Bei dem Ausführungsbeispiel „Method 1“ gemäß der Figur 1 auf Seite 5 weiß
        das Endgerät aufgrund einer vorbestimmten Zeitspanne („predetermined timing period“) bereits zum Zeitpunkt des Aussendens der Zufallszugriffspräambel an eine Basisstation, wann es die von der Basisstation ausgesendete
        und für dieses Endgerät bestimmte Zufallszugriffsantwort empfangen sollte
        (vgl. Seite 5, erster Satz). Daher falle bei diesem Ausführungsbeispiel auch
        keine zusätzliche Signalisierung bei der Übertragung der jeweiligen Zufallszugriffsantwort von der Basisstation an das Endgerät an (vgl. Seite 4, letzter Absatz: „no overhead case“). Die weiteren Erläuterungen zu diesem Ausführungsbeispiel (vgl. Seite 5, zweiter Satz bis Seite 6, zweiter Absatz) beschreiben verschieden Vorgehensweisen zur Bestimmung bzw. Festlegung dieser
        vorbestimmten Zeitspanne.

        Die „Method 1“ steht demnach im Zusammenhang mit der Offenbarung des
        Merkmals M1.8.

•       Abweichend von der o. g. „Method 1“ wird bei den übrigen, im Zusammenhang
        mit den zu einer „Method 2“ beschriebenen Ausführungsbeispielen endgeräteseitig keine vorbestimmte Zeitspanne verwendet. Stattdessen wird bei diesen Ausführungsbeispielen von der Basisstation als Teil der Zufallszugriffsantwort eine Zeitinformation an das Endgerät übertragen (vgl. Seite 9, erster Absatz: „Accordingly, time information is preferably included in the RACH

                                   - 35 -



response.“). Aufgrund dieser bei der „Method 2“ übertragenen Zeitinformation
seien die Ausführungsbeispiele gemäß der „Method 2“ – im Vergleich zur o. g.
„Method 1“ – mit einer zusätzlichen Signalisierung, d. h. einem Overhead, verbunden (vgl. Seite 7, erster Absatz: „enduring signaling overhead“).

Bei der zu übertragenden Zeitinformation kann es sich um die Subrahmen-Nummer des RACH-Slots zum Zeitpunkt des Aussendens der Zufallszugriffspräambel durch das Endgerät handeln. Diese Subrahmen-Nummer kann
von der Basisstation unter Berücksichtigung des Radius der entsprechenden
Funkzelle ermittelt werden (vgl. Seite 7, vorletzter Absatz i. V. m. Figur 2: „A
base station can know a UL subframe number of a received signal in consideration of a size which can be supportably by a cell. Accordingly, the base station transmits the subframe number in a state of being included in the response
in addition to the detected sequence information, …”). Bei der zu übertragenden Zeitinformation kann es sich aber auch um die Nummer eines umnummerierten Subrahmens handeln (vgl. Seite 7, letzter Absatz, i. V. m. Figur 3:
„renumbered subframes“).

Es ist auch möglich, dass die Basisstation die Aussendung der Zufallszugriffsantwort an das Endgerät im Bedarfsfall zeitlich verzögert (vgl. Figur 4:
„delayed response“).

Der o. g. Signalisierungs-Overhead kann dadurch reduziert werden, dass die
Basisstation in ihrer Zufallszugriffsantwort nicht die (umnummerierte) Subrahmen-Nummer an das Endgerät überträgt, sondern lediglich eine Information
über einen zeitlichen Relativversatz („offset“) des Aussendezeitpunktes der
Zufallszugriffsantwort der Basisstation in Bezug auf einen zuvor definierten basisstationsseitigen Empfangszeitpunkt der Zufallszugriffspräambel eines Endgerätes (vgl. Seite 9, zweiter Absatz).

Darüber hinaus kann anstelle der Subrahmen-Nummer auch eine daraus mittels einer Modulo-Operation ermittelte Nummer als Teil der Zufallszugriffspräambel und der Zufallszugriffsantwort übertragen werden (vgl. Seite 9, letzter
Absatz, bis Seite 10, erster Absatz, i. V. m. Figur 5).

                                      - 36 -




       Die in dem Dokument NK3-P1 im Rahmen der „Method 2“ beschriebenen Ausführungsbeispiele stehen daher im Zusammenhang mit der Offenbarung des
       Merkmals M1.7.


3.1.2 Entgegen der von der Beklagten in ihrer Widerspruchsbegründung geäußerten Ansicht versteht der Fachmann die Beschreibung des Ausführungsbeispiels gemäß der „Method 1“ als unabhängig von der Beschreibung der Ausführungsbeispiele gemäß der „Method 2“. Auch den weiteren Teilen des Dokuments NK3-P1
sind keine Hinweise für eine Kombination des Ausführungsbeispiels gemäß der
„Method 1“ mit einem der Ausführungsbeispiele gemäß der „Method 2“ zu entnehmen.

Selbst wenn der Fachmann erkennen sollte, dass sich die „Method 1“ und die „Method 2“ nicht gegenseitig ausschließen, sondern prinzipiell miteinander kombiniert
werden könnten, ohne dass es hierbei zu unerwünschten gegenseitigen Beeinflussungen kommen würde, so ist eine Kombination der „Method 1“ und der „Method 2“
im Sinne einer Kombination der Merkmale M1.8 und M1.7 als Teil eines einzigen
Verfahrens für den Fachmann dem Dokument NK3-P1 nicht unmittelbar und eindeutig als zur Erfindung gehörend zu entnehmen.


3.2      Der Gegenstand der unabhängigen Patentansprüche 1 und 9 nach Streitpatent ergibt sich für den Fachmann in naheliegender Weise ausgehend von der
Lehre des Dokuments NK6 unter Berücksichtigung der Lehre des Dokuments NK7.

Bei dem Dokument NK6 handelt es sich um eine Beschlussvorlage der CATT aus
dem LTE-Standardisierungsverfahren für das 3GPP TSG RAN WG2 #62-Meeting
vom 5. bis 9. Mai 2008 in Kansas City, USA.
Bei dem Dokument NK7 handelt es sich um einen Diskussionsbeitrag und eine Beschlussvorlage von Qualcomm Europe aus dem LTE-Standardisierungsverfahren
für das 3GPP TSG-RAN WG2 #61bis-Meeting vom 31. März bis 4. April 2008 in
Shenzhen, China.

                                       - 37 -



Das Dokument NK6 wurde am 9. Mai 2008 und das Dokument NK7 wurde am
25. März 2008 auf den FTP-Server der 3GPP hochgeladen und dadurch der Öffentlichkeit zugänglich gemacht, d. h. jeweils nach dem Anmeldedatum der US-amerikanischen Voranmeldung (1. Januar 2008) des Streitpatents, vor dem Anmeldedatum der koreanischen Voranmeldung (22. Mai 2008) des Streitpatents und vor der
Anmeldung des Streitpatents (31. Dezember 2008).


3.2.1    Das Dokument NK6 befasst sich mit der Ausgestaltung des RA-RNTI (Random Access – Radio Network Temporary Identifier) (vgl. Titel: „Text Proposal of RA-RNTI“) und enthält einen Änderungsvorschlag für das Kapitel 5.1.4 „Random Access Response reception“ der Standardspezifikation TS 36.321 des LTE-Standards. Auf welche Version der Standardspezifikation TS 36.321 sich dieser Änderungsvorschlag bezieht, ist in dem Dokument NK6 nicht angegeben.

In dem Dokument NK6 wird vorgeschlagen, dass der RA-RNTI des für die Zufallszugriffspräambel verwendeten PRACH-Steuerkanals gemäß folgender Gleichung
vom Endgerät berechnet werden soll (vgl. Kapitel 1):

        RA-RNTI = t_id + 10 * f_id,

        mit   t_id … Nummer („index“) des ersten Subrahmens der spezifizierten
                      PRACH-Ressource, mit 0 <= t_id < 10
              f_id … Nummer („index“) der spezifizierten PRACH-Ressource innerhalb dieses ersten Subrahmens, in aufsteigender Reihenfolge
                      gemäß der Frequenz, mit 0 <= f_id < 6.


Nachdem die Zufallszugriffspräambel vom Endgerät an die Basisstation ausgesendet wurde, soll das Endgerät den von der Basisstation ausgesendeten PDCCH-Steuerkanal auf eine zu der ausgesendeten Zufallszugriffspräambel korrespondierende Zufallszugriffsantwort hin überwachen, welche durch den nach obiger Gleichung berechneten RA-RNTI gekennzeichnet sei.

In dem Dokument NK6 wird zwar nicht explizit erwähnt, dass das Endgerät die Nummer des Subrahmens, in welchem die Zufallszugriffspräambel übertragen wird,
speichert. Vielmehr wird in dem Dokument NK6 erwähnt, dass die Feststellung ob

                                       - 38 -



eine empfangene Zufallszugriffsantwort zu der vom Endgerät ausgesendeten Zufallszugriffspräambel korrespondiert, auf Basis des für die Aussendung der Zufallszugriffspräambel verwendeten RA-RNTI vorgenommen werde. Um einen solchen
Vergleich durchführen zu können, muss selbstverständlich der RA-RNTI des Zeitpunkts der Aussendung der Zufallszugriffspräambel abgespeichert worden sein.
Der gemäß der o. g. Gleichung berechnete und vom Endgerät notwendigerweise
gespeicherte RA-RNTI entspricht im Falle von FDD („Frequency Division Duplex“),
d. h. f_id = 0, der Subrahmen-Nummer t_id zum Zeitpunkt der Aussendung der Zufallszugriffspräambel.

Somit sind dem Dokument NK6 die Merkmale M1, M1.1, M1.2, M1.2.1, M1.3, M1.4
und M1.5, sowie – abweichend von der Ansicht der Beklagten – auch die Merkmale
M1.6 und M1.7 des Gegenstands des Patentanspruchs 1 entweder explizit zu entnehmen, oder der Fachmann liest diese aufgrund seines Fachwissens bei der Lehre
dem Dokument NK6 mit.

Soweit die Beklagte die Ansicht vertritt, dass das Merkmal M1.8 in dem Dokument
NK6 nicht offenbart sei, und dem Fachmann auch nicht bei einer Kombination dem
Dokument NK6 und NK7 nahegelegt werde, teilt der Senat diese Schlussfolgerungen
der Beklagten nicht.

Gemäß dem Dokument NK6 kann die Überwachung des PDCCH-Steuerkanals im
Hinblick auf eine zu der Zufallszugriffspräambel passende Zufallszugriffsantwort
vom Endgerät beendet werden, nachdem es eine Zufallszugriffsantwort empfangen
hat, welche zu der von ihm ausgesendeten Zufallszugriffspräambel korrespondiert
(„The UE may stop monitoring for Random Access Response(s) after successful
reception of a Random Access Response corresponding to the Random Access
Preamble transmission.”).

Darüber hinaus wird in dem Dokument NK6 erläutert, dass das Endgerät den
PDCCH-Steuerkanal während eines bestimmten Zeitfensters nach einer Zufallszugriffsantwort hin überwachen soll („… the UE shall monitor the [PDCCH] … in the
TTI window [RA_WINDOW_BEGIN—RA_WINDOW_END] for Random Access
Response(s).“),    wobei    dieses   Zeitfenster   durch    einen    Startzeitpunkt

                                       - 39 -



(„RA_WINDOW_BEGIN“) und einen Endzeitpunkt („RA_WINDOW_END“) begrenzt
wird.

Dies berücksichtigend soll das Endgerät die zu der ausgesendeten Zufallszugriffspräambel korrespondierende Zufallszugriffsantwort gemäß der Lehre des Dokuments NK6 nur innerhalb eines vorbestimmten Zeitfensters empfangen können,
welches durch den Startzeitpunkt („RA_WINDOW_BEGIN“) und durch den Endzeitpunkt („RA_WINDOW_END“) gekennzeichnet ist. Dass zumindest dieser Endzeitpunkt des vorbestimmten Zeitfensters nach dem Aussendezeitpunkt der Zufallszugriffspräambel liegen muss, ist in diesem Zusammenhang selbstverständlich. Allerdings kann eine weitergehende Definition des Startzeitpunktes des vorbestimmten
Zeitfensters entsprechend Merkmal M1.8 insbesondere in Bezug auf dessen mögliche Abhängigkeit vom Aussendezeitpunkt der Zufallszugriffspräambel oder von
anderen Parametern oder Ereignissen dem Dokument NK6 nicht entnommen werden. Dem Dokument NK6 können auch keine Details dahingehend entnommen werden, ob der Endzeitpunkt des vorbestimmten Zeitfensters z. B. lediglich durch eine
vorbestimmte Zeitspanne nach dem Startzeitpunkt definiert ist, d. h. Startzeitpunkt
+ Δt, oder ob dieser Endzeitpunkt z. B. von weiteren Parametern oder Ereignissen
abhängig ist.

Somit ist das Merkmal M1.8 des Gegenstands des Patentanspruchs 1 nach Streitpatent zumindest nicht vollständig in dem Dokument NK6 offenbart.

Der Gegenstand des Patentanspruchs 1 nach Streitpatent ist daher gegenüber dem
Stand der Technik nach dem Dokument NK6 neu.


3.2.2   Das Dokument NK7 befasst sich mit dem Zeitfenster („RA response
window“, „RA_WINDOW“) für den endgeräteseitigen Empfang einer Zufallszugriffsantwort, welche von einer Basisstation als Folge des Empfangs einer Zufallszugriffspräambel ausgesendet wird (vgl. Titel: „RA_WINDOW …“; Kapitel 1, erster
Absatz: „The UE monitors for the random access response during a window [
RA_WINDOW_BEGIN—RA_WINDOW_END ] …”) und möchte einen Vorschlag für
die Definition des Startzeitpunktes und des Endzeitpunktes dieses Zeitfensters unterbreiten (vgl. Kapitel 1, erster und dritter Absatz: „RA_WINDOW_BEGIN and

                                       - 40 -



RA_WINDOW_END need a definition. … This paper proposes to progress the definition of begin and end of the window …“).

Sowohl das Dokument NK6, als auch das Dokument NK7 wurde im Zusammenhang
mit Meetings der 3GPP TSG-RAN WG2-Arbeitsgruppe veröffentlicht, wobei das
Meeting, welches im Zusammenhang mit dem Dokument NK6 steht, nur ca. fünf
Wochen nach jenem Meeting stattfand, welches im Zusammenhang mit dem Dokument NK7 steht. Daher ist es auch nachvollziehbar, dass in beiden Dokumente NK6
und    NK7     die   gleichen    Bezeichnungen      für   den    Anfangszeitpunkt
(„RA_WINDOW_BEGIN“) und den Endzeitpunkt („RA_WINDOW_END“) des Zeitfensters verwendet werden. Hierbei ist insbesondere zu berücksichtigen, dass sich
die Teilnehmer an diesen beiden Meetings auch aufgrund der geschilderten zeitlichen Konstellation aus der gleichen Gruppe von Fachleuten zusammengesetzt haben dürften, jedenfalls denselben Teilnehmerkreis adressiert haben, und demnach
auch die Veröffentlichungen im Zusammenhang mit diesen beiden Meetings von
einer jedenfalls ähnlichen Gruppe von Fachleuten analysiert worden sein dürften,
so dass der Fachmann den inhaltlichen Zusammenhang zwischen den beiden Dokumenten NK6 und NK7 erkennen konnte.

Auch deswegen ist es für den Fachmann naheliegend, bei der technischen Realisierung des in dem Dokument NK6 lediglich allgemein beschriebenen Zeitfensters
zum Empfang der Zufallszugriffsantwort, insbesondere dessen Startzeitpunktes,
Endzeitpunktes und Dauer, auf den in dem Dokument NK7 beschriebenen Ausgestaltungsvorschlag zurückzugreifen.

In dem Dokument NK7 wird vorgeschlagen, einen festen Zeitpunkt als Startzeitpunkt („RA_WINDOW_BEGIN“) des Zeitfensters zum Empfang der Zufallszugriffsantwort festzulegen. Unter Berücksichtigung einer angemessenen Verarbeitungszeit der von der Basisstation empfangenen Zufallszugriffspräambel des Endgerätes könne der Startzeitpunkt dieses Zeitfensters 2, 3 oder 4 Millisekunden nach
Ende der Aussendung der Zufallszugriffspräambel liegen. Da ein Subrahmen des
PRACH-Steuerkanals eine zeitliche Länge von 1 Millisekunde aufweise, könne das
o. g. endgeräteseitige Empfangszeitfenster somit 2, 3 oder 4 Subrahmen nach dem
Ende der Aussendung der Zufallszugriffspräambel starten/beginnen.

                                        - 41 -




Bei dem in der Figur 1 dem Dokument NK7 dargestellten auf FDD basierenden Ausführungsbeispiel startet/beginnt das endgeräteseitige Zeitfenster („RA response
window“) zum Empfang der Zufallszugriffsantwort drei Subrahmen („3ms“) nach
dem Ende der Aussendung der Zufallszugriffspräambel („RA_WINDOW_BEGIN“).




                             Figur 1 des Dokuments NK7


Der Endzeitpunkt („RA_WINDOW_END“) des Zeitfensters zum endgeräteseitigen
Empfang     der    Zufallszugriffsantwort        solle   relativ   zum    Startzeitpunkt
(„RA_WINDOW_BEGIN“) festgesetzt werden, und zwar eine vordefinierte Zeitspanne („RA_WINDOW_WIDTH DL“) nach dem Startzeitpunkt des Zeitfensters,
wobei diese vordefinierte Zeitspanne einer vordefinierten Anzahl von Subrahmen
entsprechen soll (vgl. Kapitel 2.3, dritter und vierter Absatz: „We propose to set
RA_WINDOW_END           relative   to       RA_WINDOW_BEGIN              as    follows[:]
RA_WINDOW_END is set to the subframe occurring RA_WINDOW_WIDTH DL
subframes after RA_WINDOW_BEGIN.“).

Somit ist aus dem Dokument NK7 ein Verfahren bekannt, bei dem das Endgerät die
Zufallszugriffsantwort innerhalb einer vorbestimmten Zeitspanne („RA response
window“, „RA_WINDOW“) empfängt, welche einen vorbestimmten Zeitpunkt
(„RA_WINDOW_END“) nach einer Übertragungszeit („PRACH TX ended“), zu der
die Zufallszugriffspräambel übertragen wird, umfasst. Bei dem in der Figur 1 des
Dokuments NK7 dargestellten Ausführungsbeispiel wird dieser vorbestimmte Zeitpunkt dadurch erhalten, dass ein Zeitversatz – bestehend aus der Dauer des Zeitfensters und aus der zeitlichen Länge dreier Subrahmen (d. h. 3 * 1 Millisekunde) –

                                      - 42 -



zu dem Zeitpunkt des Endes der Aussendung der Zufallszugriffspräambel („PRACH
TX ended“) addiert wird.

Aus dem Dokument NK7 ist somit ein Verfahren zum Empfangen einer Zufallszugriffsantwort bekannt, welches das Merkmal M1.8 des mit dem Patentanspruchs 1
nach Streitpatent beanspruchten Verfahrens aufweist.

Unter Berücksichtigung der in dem Dokument NK7 genannten Vorschläge zur Realisierung eines Zeitfensters zum endgeräteseitigen Empfang der Zufallszugriffsantwort bei dem aus dem Dokument NK6 bekannten Verfahren, gelangt der Fachmann
somit auf naheliegende Weise zu einem Verfahren mit den Merkmalen des Gegenstands des Patentanspruchs 1 nach Streitpatent.

Das Verfahren gemäß dem Patentanspruch 1 nach Streitpatent beruht demnach
gegenüber dem Stand der Technik nach dem Dokument NK6 in Verbindung mit der
Lehre des Dokuments NK7 nicht auf einer erfinderischen Tätigkeit.

Die vorstehenden Ausführungen zum Patentanspruch 1 nach Streitpatent gelten
entsprechend für den Nebenanspruch 9 nach Streitpatent.


3.3 Die zusätzlichen Merkmale des Gegenstands des abhängigen Patentanspruchs 2 nach Streitpatent sind aus den im Zusammenhang mit dem Patentanspruch 1 nach Streitpatent genannten Gründen (FDD-Fall, d. h. f_id = 0) bekannt.




                      III. Zur Fassung nach Hilfsantrag 1


In der Fassung nach dem Hilfsantrag 1 erweist sich das Streitpatent hingegen als
schutzfähig, so dass die Klage, soweit sie sich auch gegen diese Fassung richtet,
abzuweisen ist. Auf die Frage, ob das Streitpatent auch in der Fassung nach den
weiteren Hilfsanträgen Bestand hätte, kommt es bei dieser Sachlage nicht mehr an.

                                         - 43 -



1.     Patentanspruch 1 nach Hilfsantrag 1 basiert auf dem Patentanspruch 1 nach
Streitpatent, wobei dieser im Anschluss an das Merkmal M1.8 durch das Merkmal
M1.8.1H1 ergänzt wurde, das lautet:

     M1.8.1H1     wherein the offset time is equal to half of a round trip time for a
                  hybrid automatic repeat request, HARQ, process.


Gemäß dem Merkmal M1.8.1H1 ist der im Merkmal M1.8 erstmals erwähnte, jedoch
nicht näher spezifizierte Zeitversatz („offset time”) gleich der Hälfte einer Umlaufzeit
eines HARQ-Prozesses (Prozess einer hybriden automatischen Widerholungsanforderung).


2.     Entgegen der Ansicht der Klägerin geht das hinzugefügte Merkmal M1.8.1H1
nicht in unzulässiger Weise über die ursprünglich eingereichten Unterlagen oder
den Schutzbereich des erteilten Patents hinaus und lässt auch hinreichend erkennen, was unter Schutz gestellt werden soll.


Die Offenbarungsgrundlage des Merkmals M1.8.1H1 findet sich im ursprünglich eingereichten Patentanspruch 10 (vgl. Anlage NK3-PCT), der lautet:

     „A method of receiving a random access response, the method comprising:
     transmitting a random access preamble; and
     receiving the random access response,
     wherein the receiving of the random access response is performed within a
           predetermined time span including a predetermined time point after a
           transmission time when the random access preamble is transmitted, and
     the predetermined time point is obtained by adding half of the round trip time
           for a hybrid automatic repeat request (HARQ) process to the random access preamble transmission time.”


Bei dem ursprünglich eingereichten Patentanspruch 10 handelt es sich um einen
Nebenanspruch, dessen Gegenstand zumindest die Merkmale M1.2.1 und M1.3
bis M1.7 nicht explizit aufweist.

                                       - 44 -



Das mit dem ursprünglich eingereichten Nebenanspruch 10 beanspruchte Verfahren geht auf die in der ursprünglich eingereichten Beschreibung (Seite 27, Zeile 20
bis Seite 28, Zeile 18) beschrieben Ausführungsbeispiele zurück, welche auf dem
in der Figur 13 der Anmeldeunterlagen beispielhaft dargestellten Übertragungsverhalten im Uplink und im Downlink aufbauen. Insbesondere wird das mit dem ursprünglich eingereichten Nebenanspruch 10 beanspruchte Verfahren hierbei durch
das auf der Seite 28, Zeilen 7 bis 11 beschriebene Verfahren gestützt: „The user
equipment which attempts random access may wait for a half of the HARQ round
trip time […] from a time point when a random access preamble is transmitted, and
wait for a response within a predetermined time period from a time point when a half
of the HARQ round trip time […] elapses.”.

Die im Zusammenhang mit der Figur 13 beschriebenen Ausführungsbeispiele befassen sich ausschließlich mit Fragen des zeitlichen Empfangs einer von einer Basisstation ausgesendeten Zufallszugriffsantwort seitens eines Endgeräts unter Berücksichtigung von bidirektionalen Übertragungs- bzw. Verzögerungszeiten zwischen dem Endgerät und der Basisstation. Dass dies unter Berücksichtigung der
thematischen Zielsetzung und des inhaltlich-technischen Schwerpunkts der Anmeldeunterlagen jedoch nur einer von mehreren relevanten Aspekten ist, ist für den
Fachmann offensichtlich, so dass der Fachmann schon aus diesem Grunde erkennt, dass er die im Zusammenhang mit der Figur 13 offenbarten Ausführungsbeispiele mit anderen ursprungsoffenbarten Ausführungsbeispielen kombinieren kann.

Darüber hinaus wird in den Anmeldeunterlagen explizit darauf hingewiesen, dass
die offenbarten Ausführungsformen auch miteinander kombiniert werden können –
z. B. auch durch Kombination der Gegenstände unabhängiger Patentansprüche
(Seite 32, Zeilen 14 bis 21: „Also, some constituent components and/or characteristics may be combined to implement the embodiments of the present invention. The
order of operations to be disclosed in the embodiments of the present invention may
be changed to another. Some components or characteristics of any embodiment
may also be included in other embodiments, or may be replaced with those of the
other embodiments as necessary. It will be apparent to those skilled in the art that
unrelated claims are combined so as to configure embodiments or are included in
new claims by amendments after an application.“).

                                        - 45 -




Dies berücksichtigend, erkennt der Fachmann das Merkmal M1.8.1H1 als durch den
ursprünglich eingereichten Patentanspruch 10 offenbart, ebenso wie die Möglichkeit, dieses Merkmal mit den Merkmalen M1 bis M1.8 kombinieren zu können, wobei aus den im Zusammenhang mit dem Patentanspruch 1 nach Streitpatent erläuterten Gründen keine Zweifel an der Ursprungsoffenbarung der Merkmale M1
bis M1.8 bestehen.


Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 geht demnach nicht
über den Offenbarungsgehalt der Anmeldeunterlagen hinaus.


3.    Durch die Aufnahme des Merkmals M1.8.1H1 fehlt es Patentanspruch 1 nach
Hilfsantrag 1 weder an der erforderlichen Klarheit noch an einer ausführbaren Offenbarung.

Der Senat teilt die Ansicht der Klägerin, dass unklar sei, welche Bedeutung der Definition des Zeitversatzes („offset time“) im Patentanspruch 1 nach Hilfsantrag 1 zukommen solle, nicht.

Durch das hinzugenommene Merkmal M1.8.1H1 wird der im Merkmal M1.8.1 erstmals erwähnte jedoch nicht näher spezifizierte Zeitversatz („offset time”) dahingehend präzisiert, dass dieser gleich der Hälfte einer Umlaufzeit („round trip time“)
eines HARQ-Prozesses (Prozess einer hybriden automatischen Widerholungsanforderung) ist. Die Aufnahme des Merkmals M1.8.1H1 führt auch zu einer Einschränkung des Schutzbereichs.

Die Bedeutung der Umlaufzeit eines HARQ-Prozesses ist dem zuständigen Fachmann als Grundlagenwissen bekannt, und wird in den Anmeldeunterlagen außerdem auch im Zusammenhang mit den Ausführungsbeispielen nach der Figur 13 erläutert (Seite 27, Zeile 20 bis Seite 28, Zeile 6), so dass der Senat keine Zweifel an
einer inhaltlichen Klarheit oder Ausführbarkeit des Merkmals M1.8.1H1 für den Fachmann hat.

                                        - 46 -



4.     Das Streitpatent in der Fassung nach Hilfsantrag 1 erweist sich auch als patentfähig.

Keines der Dokumente NK4 bis NK7 offenbart ein Verfahren mit dem Merkmal M1.8
des Gegenstands des erteilten Patentanspruchs 1, und somit auch nicht einen Gegenstand mit dem Merkmal M1.8.1H1, der das Merkmal M1.8 weiter ausgestaltet.

Das Dokument NK7 befasst sich zwar mit einer Zeitspanne, innerhalb derer das
Endgerät die Zufallszugriffsantwort empfangen muss, damit es feststellen kann,
dass die empfangene Zufallszugriffsantwort die Antwort auf die von ihm übertragene
Zufallszugriffspräambel ist, so dass das Merkmal M1.8 des Gegenstands des Patentanspruchs 1 nach Streitpatent aus dem Dokument NK7 bekannt ist (vgl. Ausführungen im Zusammenhang mit der mangelnden Patentfähigkeit der erteilten Patentansprüche in Abschnitt II. 3.2.2). Die Umlaufzeit eines HARQ-Prozesses spielt
bei dem aus dem Dokument NK7 bekannten Verfahren allerdings keine Rolle und
es ist auch nicht ersichtlich, dass der der Fachmann bei dem aus dem Dokument
NK7 bekannten Verfahren veranlasst war, eine solche Umlaufzeit bei seinen Überlegungen in Erwägung zu ziehen. Insbesondere erhält er weder in dem Dokument
NK7 noch in einem anderen Dokument aus dem vorliegenden Stand der Technik
einen Hinweis oder eine Anregung, den im Merkmal M1.8 nicht spezifizierten Zeitversatz (gerade) über die Eigenschaften eines HARQ-Prozesses festzulegen.

Auch bei Berücksichtigung der Lehre des Dokuments NK7 oder seines fachmännischen Wissens, gelangt der Fachmann somit ausgehend von der Lehre des Dokuments NK6 nicht auf naheliegende Weise zum Gegenstand des Patentanspruchs 1
nach Hilfsantrag 1.

Die Dokumente NK4 und NK5 liegen deutlich weiter ab vom Gegenstand des Patentanspruchs 1 nach Streitpatent als das Dokument NK7 und können somit ebenfalls nicht zu einer Patentfähigkeit des Patentanspruchs 1 nach Hilfsantrag 1 beitragen.


Somit ist der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 gegenüber
dem verfahrensgegenständlichen Stand der Technik neu und beruht auf einer
erfinderischen Tätigkeit.

                                        - 47 -




Die vorstehenden Ausführungen zum Patentanspruch 1 nach Hilfsantrag 1 gelten
entsprechend für den inhaltlich korrespondierenden Nebenanspruch 9 nach Hilfsantrag 1.




                                         B.
                              Nebenentscheidungen

Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1 ZPO.

Dabei hat der Senat berücksichtigt, dass der als schutzfähig verbleibende Patentgegenstand in der beschränkt verteidigten Fassung nach Hilfsantrag 1 gegenüber demjenigen der erteilten Fassung im angegriffenen Umfang aufgrund der Einschränkung
auf eine konkrete Vorgabe der Zeitverhältnisse etwa der Hälfte der erteilten Fassung
im angegriffenen Umfang entspricht. Das Streitpatent erfährt in der Fassung nach
Hilfsantrag 1 durch die Beschränkung mit Aufnahme des Merkmals M1.8.1H1 eine
deutliche Einschränkung, andererseits keine, die nur die Auswahl einer einzigen aus
einer beliebig großen Menge an Gestaltungsmöglichkeiten darstellt.

Die Ausgestaltung, nach welcher der Zeitversatz („offset time”) gleich der Hälfte einer Umlaufzeit eines HARQ-Prozesses (Prozess einer hybriden automatischen Widerholungsanforderung) ist, ist im Zusammenhang damit zu sehen, dass bereits in
der erteilten Fassung für den Fachmann aufgrund seines Fachwissens ersichtlich
war, dass der Zeitversatz nicht beliebig, sondern nur im Rahmen der Zeitverhältnisse eines Zufallszugriffsverfahrens gewählt werden kann.

Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.




                                         C.
                             Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

                                       - 48 -




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




Voit             Werner             Altvater             Dr. Haupt                  Tischler
                                                Zugleich für den wegen Erkrankung an der Unterschriftsleistung
                                                gehinderten RiBPatG Dr. Haupt




                                                    (VRiBPatG Voit)
