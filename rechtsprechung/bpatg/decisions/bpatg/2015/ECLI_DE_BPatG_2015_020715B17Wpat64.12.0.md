---
ecli: "ECLI:DE:BPatG:2015:020715B17Wpat64.12.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 64/12"
decided: "2015-07-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=28&nr=27359&anz=851&pos=431&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-07-02_17_W-pat_64_12_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 64/12 vom 2015-07-02

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 64/12                                                     Verkündet am
_______________                                                        2. Juli 2015
    (Aktenzeichen)                                                          …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2011 006 398.6-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 2. Juli 2015 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,      der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Phys. Dr. Forkel




BPatG 154
05.11

                                       -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                        I.


Die vorliegende Patentanmeldung ist am 30. März 2011 beim Deutschen Patentund Markenamt eingereicht worden. Sie trägt die Bezeichnung


 „Verfahren, Bildverarbeitungseinrichtung und Computertomographiesystem zur
 Ermittlung eines Anteils von nekrotischem Gewebe sowie Computerprogrammprodukt mit Programmcodeabschnitten zur Ermittlung eines Anteils von
                             nekrotischem Gewebe“.


Die Prüfungsstelle für Klasse G06T hat in der Anhörung am 23. Oktober 2012 die
Anmeldung zurückgewiesen, da die Gegenstände des jeweiligen Patentanspruchs 1 nach Hauptantrag und nach Hilfsantrag nicht auf erfinderischer Tätigkeit
beruhten.


Gegen den Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt sinngemäß,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       gemäß Hauptantrag mit
       Patentansprüchen 1 bis 15,

                                       -3-



        Beschreibung Seiten 1 bis 24 und
        4 Blatt Zeichnungen mit Figuren 1 bis 7, jeweils vom Anmeldetag;


        gemäß Hilfsantrag mit
        Patentansprüchen 1 bis 15, überreicht in der Anhörung am 23. Oktober 2012,
        Beschreibung und Figuren jeweils wie Hauptantrag.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


D1: DE 10 2006 009 222 B4,
D2: DE 10 2004 027 710 A1,
D3: Otsu, N.: „A threshold selection method from gray-level histograms“; IEEE
Transactions on Systems, Man, and Cybernetics, Jan. 1979, Vol. 9, Issue 1, pp.
62 bis 66,
D4: Martin Ulrich Sedlmair: “Dual-Energy CT: Physikalische Modelle und Anwendungen”, Dissertation an der Medizinischen Fakultät der Ludwig-Maximilians-Universität München, 2009, Seiten 108 bis 113.


Der Senat hat zusätzlich die Druckschriften


        D5: DE 10 2006 020 864 A1 und
        D6: US 2009/0135994 A1


in das Verfahren eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.

                                       -4-



                                        II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da die Gegenstände des Patentanspruchs 1
nach Hauptantrag und des Patentanspruchs 1 nach Hilfsantrag nicht auf
erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die Patentanmeldung betrifft ein Verfahren, eine Bildverarbeitungseinrichtung und ein Computertomographiesystem zur Ermittlung eines Anteils von nekrotischem Gewebe in einem definierten Gewebebereich, insbesondere eines
Tumors, eines Untersuchungsobjektes. Die Erfindung betrifft außerdem ein Computerprogrammprodukt mit Programmcodeabschnitten zur Ermittlung eines Anteils
von nekrotischem Gewebe in einem definierten Gewebebereich, insbesondere
eines Tumors, eines Untersuchungsobjekts (Offenlegungsschrift Abs. [0001]).


Bei der Einschätzung des Therapieerfolgs von Tumorerkrankungen sei neben der
Feststellung der Größe des Tumorgewebes auch die Bestimmung des Anteils des
nekrotischen Gewebes des Tumorvolumens von Bedeutung, da Tumore auf unterschiedliche Therapieformen unterschiedlich reagierten und nicht gezwungenermaßen ihre Größe veränderten, sondern lediglich teilweise oder ganz abstürben,
d. h. nekrotisierten (Offenlegungsschrift Abs. [0002]). Informationen über die geometrische Lage des vitalen bzw. des nekrotischen Anteils eines Tumors seien
auch bei der Durchführung von Biopsien wertvoll, um sicherzustellen, dass vitales
Gewebe entnommen werde (Offenlegungsschrift Abs. [0003]).


Eine bisher übliche Methode, den nekrotischen Anteil eines Tumorgewebes bestimmen zu können, sei eine Kontrastmitteluntersuchung unter Verwendung eines
Single-Source-Computertomographen. Bei einer derartigen Untersuchung würden
zwei Aufnahmen bzw. zwei Scans durchgeführt, eine erste (native) Aufnahme
ohne Kontrastmittel und zumindest eine zweite Aufnahme nach Zufuhr des Kontrastmittels (meist Jod). Das Kontrastmittel reichere sich im Tumor vorübergehend

                                       -5-



an, wobei das nekrotische Gewebe kein Kontrastmittel aufnehme, da es abgestorben sei. Häufig erfolgten nach der Kontrastmittelgabe sogar mehrere Aufnahmen
in unterschiedlichen Anreicherungsphasen des Kontrastmittels im Gewebe, beispielsweise in einer arteriellen, einer venösen und in einer spätvenösen Phase,
um so zusätzliche Informationen über das vitale Gewebe durch dessen Jodaufnahmeverhalten zu gewinnen (Offenlegungsschrift Abs. [0004]).


Zur Bestimmung des nekrotischen Gewebes könnte eine Differenzbildung der auf
Basis dieser Messungen gewonnenen Bilddatensätze durchgeführt werden. Hierzu würden die Werte (z. B. Röntgen-Schwächungswerte) der jeweiligen Bildpunkte
der beiden (zwei- oder dreidimensionalen) Bilddatensätze voneinander subtrahiert.
Dieses Subtraktionsverfahren erfordere allerdings eine exakte Ausrichtung und
Anpassung der aufgenommenen Gewebeabschnitte bzw. des Tumorgewebes in
den verschiedenen Bilddatensätzen zueinander. Da zwischen den beiden Aufnahmen eine gewisse Zeitdauer verstreiche, könne es in der Zwischenzeit zu Patientenbewegungen und/oder zu Deformationen des Tumorgewebes aufgrund der oft
weichen Gewebestruktur kommen. Diese Gewebeverschiebungen könnten zwar
meist durch eine nicht-rigide, also elastische, Registrierung ausgeglichen werden.
Derartige Verfahren erforderten jedoch große Rechnerkapazitäten und lieferten
zudem nicht immer einwandfreie Ergebnisse. Daher werde dieses Verfahren in der
klinischen Praxis kaum verwendet (Offenlegungsschrift Abs. [0005]).


Der Erfindung soll daher die Aufgabe zugrunde liegen, ein Verfahren und eine
Bildverarbeitungseinrichtung, ein Computertomographiesystem und ein Computerprogrammprodukt bereitzustellen, das bei reduziertem Datenverarbeitungsaufwand verbesserte Ergebnisse liefert (Offenlegungsschrift Abs. [0006]).

                                        -6-



Der mit einer möglichen Gliederung versehene Patentanspruch 1 nach Hauptantrag betrifft ein


        a) Verfahren zur Ermittlung eines Anteils von nekrotischem Gewebe (14) in einem definierten Gewebebereich (16) eines
        Untersuchungsobjekts (12)
        b) auf Basis eines den Gewebebereich (16) des Untersuchungsobjekts (12) umfassenden Hochenergie-Bilddatensatzes (46) und
        eines den Gewebebereich des Untersuchungsobjekts umfassenden Niedrigenergie-Bilddatensatzes (48),
        mit folgenden Schritten:
        c) Ermitteln (ER) eines virtuellen Kontrastmittelbildes (20) auf
        Basis des Hochenergie-Bilddatensatzes (46) und des Niedrigenergie-Bilddatensatzes (48),
        d) Segmentieren (SE) des Gewebebereiches (16) in einem auf
        dem Hochenergie-Bilddatensatz (46) und/oder dem Niedrigenergie-Bilddatensatz (48) basierenden Segmentierungs-Bilddatensatz
        (22),
        e) Übertragen (UE) eines Segmentierungsergebnisses (40) in das
        virtuelle Kontrastmittelbild (20) zur Segmentierung des Gewebebereichs (16) im virtuellen Kontrastmittelbild (20), und
        f) Durchführen einer Analyse (AN) von Werten von zum segmentierten Bereich (34) des virtuellen Kontrastmittelbildes (20)
        gehörenden Bildpunkten zur Identifizierung von Bildpunkten, die
        nekrotischem Gewebe (14) zuzuordnen sind.


Im Patentanspruch 1 des Hilfsantrags sind gegenüber dem Patentanspruch 1 des
Hauptantrags die Merkmale c) und d) ersetzt durch (die neu hinzu gekommenen
Teilmerkmale sind kursiv geschrieben)

                                       -7-



        c‘   Ermitteln (ER) eines virtuellen Kontrastmittelbildes (20) auf
        Basis des Hochenergie-Bilddatensatzes (46) und des Niedrigenergie-Bilddatensatzes (48), in dem an den einzelnen Bildpunkten die reinen Kontrastmittelintensitätswerte dargestellt werden,
        d‘) Segmentieren (SE) des Gewebebereiches (16) in einem auf
        dem Hochenergie-Bilddatensatz (46) und/oder dem Niedrigenergie-Bilddatensatz (48) basierenden Segmentierungs-Bilddatensatz
        (22), wobei der Segmentierungs-Bilddatensatz entweder aus dem
        Hochenergie-Bilddatensatz oder dem Niedrigenergie-Bilddatensatz besteht oder durch eine gewichtete Addition der Bildpunkte
        des Hochenergie-Bilddatensatzes und des Niedrigenergie-Bilddatensatzes besteht,


Die Lehre der vorliegenden Patentanmeldung besteht im Wesentlichen in Folgendem:


Um den Anteil von nicht durchblutetem, nekrotischem Gewebe in einem Gewebebereich eines (Kontrastmittel enthaltenden) Untersuchungsobjekts zu ermitteln
(Merkmal a)), werden zwei (Röntgen-)Datensätze des Objekts aufgenommen, einer mit hoher Energie und einer mit niedriger Energie (Merkmal b); Offenlegungsschrift Abs. [0009]). Aus diesen beiden Datensätzen wird ein virtuelles Kontrastmittelbild ermittelt, das an den einzelnen Bildpunkten nur die auf das Kontrastmittel zurückzuführenden Intensitätsanteile enthält; die Intensitätswerte der verschiedenen Gewebeanteile sind dabei herausgerechnet (Merkmale c), c‘)). In
einem der beiden Datensätze oder in einer gewichteten Kombination der Datensätze wird eine Segmentierung des interessierenden Gewebebereichs durchgeführt (Merkmale d), d‘); Offenlegungsschrift Abs. [0010]), dieser Bereich wird somit
markiert. Das Ergebnis der Segmentierung wird auf das virtuelle Kontrastmittelbild
übertragen, so dass dieses nunmehr zusätzlich die Umrisse des segmentierten
Bereichs (z. B. der Leber) enthält (Merkmal e); Offenlegungsschrift Abs. [0011]).

                                       -8-



Innerhalb des segmentierten Bereichs werden die Kontrastmittelwerte des virtuellen Kontrastmittelbildes analysiert, z. B. mittels eines Schwellwerts, wobei Bereiche ohne Kontrastmittel (d. h. nicht durchblutete Bereiche) als nekrotisch eingestuft werden (Merkmal f); Offenlegungsschrift Abs. [0012], [0026]).


Als Fachmann sieht der Senat hier einen Informatiker oder Physiker an, der Erfahrung in der Aufnahme und Auswertung von medizinischen Bilddaten besitzt.


2.    Das Verfahren nach dem Patentanspruch 1 gemäß Hauptantrag und ebenso das Verfahren des Patentanspruchs 1 gemäß Hilfsantrag ist nicht patentfähig,
da diese Verfahren nicht auf erfinderischer Tätigkeit beruhen.


Diese Verfahren waren nämlich angesichts des Standes der Technik und im Lichte
seines Fachwissens für den Fachmann naheliegend.


Aus der Druckschrift D1 war ein Verfahren bekannt, in welchem ein Hochenergie-Bilddatensatz und ein Niedrigenergie-Bilddatensatz aufgenommen werden (Patentanspruch 1) – Merkmal b). Aus diesen Datensätzen werden die Anteile zweier
verschiedener Gewebearten sowie der Substanz (Kontrastmittel) berechnet, aus
letzterer erhält man ein reines Kontrastmittelbild z. B. der Leber (Abs. [0012],
[0013], [0014], [0028]) - Merkmale c), c‘). Durch Subtraktion dieser Bildwerte von
den beiden Datensätzen können zudem Nativbilder ohne Kontrastmittel erhalten
werden (Abs. [0014]).


Wie dem Fachmann geläufig war, enthalten Kontrastmittelbilder wie das virtuelle
Kontrastmittelbild der Druckschrift D1 medizinisch interessante Information über
die Durchblutung von Geweben und Gewebeteilen, jedoch keine oder kaum Information über deren Lage in Bezug auf das Untersuchungsobjekt, insbesondere
über nicht oder kaum durchblutete Gewebe und Gewebegrenzen, was für einen
Anwender naturgemäß die für eine Auswertung notwendige Orientierung in

                                        -9-



derartigen Bildern erschwert. Somit lag der Wunsch nahe, derartigen Kontrastmittelbildern zur besseren Orientierung Lageinformation beizufügen.


Der Fachmann, der sich diesbezüglich im die Auswertung medizinischer Bilddaten
betreffenden Stand der Technik umsah, konnte auf die Druckschrift D5 stoßen,
welche zum Ziel hat, eine genauere Lokalisierung eines Zielvolumens in einem
medizinischen Bilddatensatz zu ermöglichen (Abs. [0008]).
Die Druckschrift D5 geht aus von bekannten Verfahren, um aus medizinischen
Aufnahmen wie Magnetresonanz-Perfusionsaufnahmen oder Viabilitätsaufnahmen
die Kontrastmitteleinflutung oder –anreicherung in einem Zielvolumen zu bestimmen, wobei auch nekrotisches Gewebe aufgespürt werden kann (Abs. [0002] bis
[0006]). Hierbei ist es wichtig, nur das tatsächlich interessierende Zielvolumen zu
betrachten, dessen Segmentierung jedoch aufgrund mangelhaften Kontrastes der
anatomischen Grenzen stark fehlerbehaftet sein kann (Abs. [0006]). Zur genauen
Lokalisierung des Zielvolumens im Falle mindestens zweier aufgenommener und
registrierter Bilddatensätze lehrt die Druckschrift D5, insbesondere im Post-Processing die Segmentierung des kontrastreichsten Bilddatensatzes auf den oder
die anderen Bilddatensätze zu übertragen (Abs. [0008] bis [0011]). Dies ermöglicht es, innerhalb des lokalisierten Zielvolumens die gewünschten Informationen
zu extrahieren, etwa über schlecht oder gar nicht durchblutete Gewebegebiete
bzw. über das Vorhandensein von vitalem oder avitalem Gewebe oder gar ganzer
nekrotischer Gebiete (Abs. [0023], [0037]; Fig. 2, 3 und 4 mit Beschreibung).


Um im Verfahren der Druckschrift D1 für die Auswertung des reinen Kontrastmittelbildes eine verbesserte Orientierung zu ermöglichen, bot es sich für den
Fachmann an, gemäß der Lehre der Druckschrift D5 in einem Bild, welches die
unterschiedlichen enthaltenen Gewebebereiche mit ihren Grenzen in relativ kontrastreicher Form zeigt (hierfür bot sich in der Druckschrift D1 einer der beiden
aufgenommenen Bilddatensätze oder ein hieraus abgeleitetes Nativbild an) das
Zielvolumen zu segmentieren und das Segmentierungsergebnis auf das insoweit
kontrastärmere Bild (in der Druckschrift D1 ist dies das reine Kontrastmittelbild) zu

                                       - 10 -



übertragen – Merkmale d), d‘), e). Eine Auswertung des Kontrastmittelbilds, etwa
eine Bestimmung schlecht durchbluteter oder sogar nekrotischer Anteile, wird
dann wie üblich nur im interessierenden Bereich, hier also im Bereich des segmentierten Zielvolumens vorgenommen – Merkmale a), f).


Damit war ein Verfahren mit allen Merkmalen des Patentanspruchs 1 gemäß
Hauptantrag und ebenso ein Verfahren mit allen Merkmalen des Patentanspruchs 1 gemäß Hilfsantrag für den Fachmann naheliegend.


Der jeweilige Patentanspruch 1 des Hauptantrags und des Hilfsantrags ist nicht
gewährbar.


3.     Auch die jeweiligen übrigen Patentansprüche 2 bis 15 des Hauptantrags
und des Hilfsantrags sind nicht gewährbar, da über einen Antrag nur einheitlich
entschieden werden kann (BGH GRUR 1997, 120 - Elektrisches Speicherheizgerät).




                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


     das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
        Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
        Befangenheit mit Erfolg abgelehnt war,
     einem Beteiligten das rechtliche Gehör versagt war,

                                     - 11 -



   ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
       sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der
       die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
       sind, oder
   der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Dr. Morawek              Eder             Dr. Thum-Rung               Dr. Forkel




                                                                             Me
