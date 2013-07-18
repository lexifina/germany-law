---
ecli: "ECLI:DE:BPatG:2013:180713B17Wpat31.09.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 31/09"
decided: "2013-07-18"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=43&nr=25268&anz=1167&pos=659&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-07-18_17_W-pat_31_09_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 31/09 vom 2013-07-18

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 31/09                                                  Verkündet am
_______________                                                    18. Juli 2013
    (Aktenzeichen)                                                      …




                            BESCHLUSS

                          In der Beschwerdesache


             betreffend die Patentanmeldung 10 2007 014 821.8-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 18. Juli 2013 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder, der Richterin Dipl.-Phys.
Dr. Thum-Rung und des Richters Dipl.-Ing. Hoffmann


beschlossen:


                     Die Beschwerde wird zurückgewiesen.




BPatG 154
05.11

                                      -2-



                                   Gründe


                                       I.


Die vorliegende Patentanmeldung wurde am 28. März 2007 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung:


 „System zur Durchführung einer sequenziellen aufsteigenden Anbieterauktion“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 Q des
Deutschen Patent- und Markenamts vom 14. Januar 2009 zurückgewiesen. Die
Prüfungsstelle begründete die Zurückweisung damit, dass die beanspruchte Lehre
im Hinblick auf das Patentierungsverbot von Verfahren für geschäftliche Tätigkeiten sowie von Programmen für Datenverarbeitungsanlagen (§ 1 Abs. 3 Nr. 3
und Abs. 4 PatG) vom Patentschutz ausgeschlossen sei.


Gegen diesen Beschluss wendet sich die Beschwerde des Anmelders.


Der Anmelder stellte den Antrag,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 – 15 vom 27. Februar 2008, eingegangen am
       29. Februar 2008,
       Beschreibung Seiten 1 – 5 vom Anmeldetag.

                                         -3-



Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind folgende
Druckschriften genannt worden:


D1:   WO 2001 / 45002 A1
D2:   WO 2001 / 59658 A1


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie hat jedoch keinen Erfolg, da das System des Patentanspruchs 1 nicht auf
erfinderischer Tätigkeit beruht (§ 1 Abs. 1 i. V. m. § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung betrifft ein Auktionssystem, das sowohl
simultan als auch sequentiell durchgeführt werden kann.


In einem Auktionssystem wird eine zu versteigernde Ware von einem Servercomputer im Internet vorgestellt. Der Servercomputer übernimmt darüber
hinaus die Durchführung der Auktion nach vorher festgelegten Regeln. Ein Bieter,
der sich für die Ware interessiert, kann von seinem Computer aus die Ware
begutachten und an der Auktion durch Abgabe von Geboten teilnehmen. Aufgrund
festgelegter Regeln wird der zeitliche Ablauf einer Auktion gesteuert. Dabei wird
geprüft, ob in einem festgelegten Zeitraum vor Ende der Auktion noch ein Gebot
eingeht und wenn dies der Fall ist, wird das Ende der Auktion um einen ebenso
vorher festgelegten Zeitraum verlängert. Am Ende der Auktion wird anhand der
vorgegebenen Bedingungen ermittelt, ob der letzte Bieter den Zuschlag erhält
oder ob unter allen Bietern, die ein gültiges Gebot abgegeben haben, der
Zuschlag verlost wird.

                                          -4-



Der Anmeldung soll die Aufgabe zugrunde liegen, eine besondere Art der amerikanischen Auktion zur Verfügung zu stellen, welche auch über große Entfernungen zwischen den Bietern und ohne Anwesenheit eines Auktionators durchgeführt werden kann (siehe Beschreibung Seite 2, Z. 1-4).


Diese Aufgabe soll durch das in Patentanspruch 1 angegebene System gelöst
werden. Der geltende Patentanspruch 1, hier mit einer möglichen Gliederung
versehen, lautet:


   1.   System zur Durchführung einer sequenziellen aufsteigenden
        Anbieterauktion,


dadurch gekennzeichnet, dass


        a. von einem Servercomputer über ein Computernetzwerk wenigstens
             Informationen über das zu versteigernde Gut und die Startzeit der
             Auktion veröffentlicht werden,
        b. die Gebote der Teilnehmer über das Computernetzwerk angenommen
             werden,
        c. die Auktion jeweils um den Zeitraum t2 verlängert wird, wenn innerhalb
             des Zeitraums t1 ein weiteres gültiges Angebot eingeht und die
             Auktion auf den maximalen Zeitraum t3 begrenzt wird,
        d. die Auktion über den Zeitraum t3 – t1, wenn t1 > t2, über den Zeitraum
             t3 – t2, wenn t2 > t1 oder über den Zeitraum t3 – t1 (oder t2), wenn t1 = t2
             auf einem Servercomputer frei geschaltet ist,
        e. für ein gültiges Gebot ein vorher festgelegter Geldbetrag G
             unabhängig vom Erfolg am Servercomputer eingehen muss und,
        f.   das Ende der Auktion bei Ablauf des Zeitraums t 3 – t2 oder t3 – t1
             erreicht ist und über das Computernetzwerk veröffentlicht wird, wobei
             das zu versteigernde Gut unter den Teilnehmern der Auktion verlost
             wird und jedes einzelne akzeptierte Gebot gewinnberechtigt ist oder

                                           -5-



        g. das Ende der Auktion bei Ausbleiben des Eingangs eines weiteren
            gültigen Gebots innerhalb eines Zeitraums t1 erreicht ist und auf dem
            Servercomputer über das Computernetzwerk veröffentlicht wird, wobei
            der zuletzt akzeptierte Bieter der Gewinner ist.


Zu den nebengeordneten Ansprüchen 7, 14 und 15, sowie zu den Unteransprüchen 2 bis 6 und 8 bis 13 wird auf die Akte verwiesen.


Mit dem Patentanspruch 1 soll ein System zur Durchführung einer sequentiellen
aufsteigenden Anbieterauktion unter Schutz gestellt werden (Merkmal (1)).


In dem System gemäß Patentanspruch 1 werden von einem Servercomputer
Informationen an ein Computernetzwerk übertragen und somit veröffentlicht. Diese
Informationen geben Auskunft über das zu versteigernde Gut bzw. die zu versteigernde Ware und über die Startzeit der Auktion. Von den Computern der
Auktionsteilnehmer (Bieter) können diese Informationen eingesehen werden
(Merkmal (a)).


Der Servercomputer nimmt die Gebote der Teilnehmer, welche über das
Computernetzwerk übertragen werden, an (Merkmal (b)).


Die Auktion wird um die Zeit t2 verlängert, falls innerhalb eines Zeitraums t1 ein
weiteres Gebot eingeht. Dabei ist die Gesamtzeit der Auktion auf den maximalen
Zeitraum t3 begrenzt (Merkmal (c)).


Weiterhin ist vorgegeben, dass die Auktion
   -   im ersten Fall (t1 > t2) für den Zeitraum t3 – t1,
   -   im zweiten Fall (t2 > t1) für den Zeitraum t3 – t2, und
   -   im dritten Fall (t1 = t2) für den Zeitraum t3 – t1 (oder t2)
auf dem Servercomputer freigeschaltet ist (Merkmal (d)).

                                           -6-



Ein gültiges Gebot liegt vor, wenn ein vorher festgelegter Geldbetrag G unabhängig vom Erfolg am Servercomputer eingeht (Merkmal (e)).


Die Auktion wird beendet und über das Computernetzwerk veröffentlicht, wenn
      -   der Zeitraum t3 – t2 oder t3 – t1 erreicht ist, wobei das zu versteigernde Gut
          dann unter den Teilnehmern der Auktion verlost wird und jedes einzelne
          akzeptierte Gebot gewinnberechtigt ist (Merkmal (f)) oder
      -   kein weiteres gültiges Gebot innerhalb eines Zeitraums t1 mehr eingeht,
          wobei in diesem Fall der zuletzt akzeptierte Bieter der Gewinner ist
          (Merkmal (g)).


Als Fachmann, der mit der Aufgabe betraut wird, eine Auktion auf einem Computersystem zu implementieren, sieht der Senat einen Informatiker oder Programmierer mit Berufserfahrung auf dem Gebiet der Programmierung von geschäftlichen Transaktionen an.


2.        Das System nach Anspruch 1 beruht nicht auf erfinderischer Tätigkeit.


2a)       Nach der Rechtsprechung des Bundesgerichtshofs ist bei Erfindungen mit
Bezug zu Geräten und Verfahren der elektronischen Datenverarbeitung zunächst
zu klären, ob der Gegenstand der Erfindung zumindest mit einem Teilaspekt auf
technischem Gebiet liegt (§ 1 Abs. 1 PatG). Da das Gesetz Programme für
Datenverarbeitungsanlagen (ebenso wie Pläne, Regeln und Verfahren für Spiele
und für geschäftliche Tätigkeiten) als solche durch § 1 Abs. 3 Nr. 3 i. V. m. Abs. 4
PatG vom Patentschutz ausschließt, sind bei der anschließenden Prüfung der
Erfindung auf erfinderische Tätigkeit nur diejenigen Anweisungen zu berücksichtigen, die die Lösung eines technischen Problems mit technischen Mitteln
bestimmen oder zumindest beeinflussen (BGH GRUR 2011, 125 – Wiedergabe
topografischer Informationen; BGH X ZR 27/12 – Fahrzeugnavigationssystem).

                                        -7-



2b)    Die grundsätzliche Technizität (§ 1 Abs. 1 PatG) eines Systems zur Durchführung einer Auktion, welches über einen Servercomputer und ein Computernetzwerk verfügt, steht hier außer Frage.


2c)    Jedoch sind zumindest die Merkmale, die eine Verlängerung der Auktion
(Merkmal (c)) und die Dauer der Freischaltung (Merkmal (d)) definieren, bei der
Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen. Gleiches gilt für die
Vorgabe eines festgelegten Geldbetrags für ein gültiges Gebot, für die Festlegung
des Endes der Auktion und der Vorgabe, wer die versteigerte Ware letztendlich
erhält (Merkmale (e), (f) und (g)).
Denn diesen Merkmalen liegt kein technisches Problem zugrunde. Sie definieren
Regeln (im Sinne von Spielregeln), mit denen Anweisungen für die Durchführung
der Auktion vorgegeben werden. Diese Regeln und Anweisungen beruhen lediglich auf geschäftlichen Überlegungen; sie dienen zur Erhöhung des geschäftlichen
Erfolgs einer Auktion, welche durch die Art der Regeln für die Mitspieler möglichst
interessant gestaltet werden soll. Die Implementierung auf dem Computernetzwerk mit Servercomputern erfolgt durch ein Computerprogramm, wozu es lediglich
des Handwerkszeugs eines Programmierers bedurfte. Technische Überlegungen
waren hierfür nicht erforderlich. Auch ist eine besondere technische Ausgestaltung, etwa im Sinne einer speziell angepassten Hardware, nicht ersichtlich.


2d)    Die für die Prüfung der erfinderischen Tätigkeit danach allenfalls in Betracht
kommenden Merkmale (1), (a) und (b) sind aus dem Stand der Technik zu
entnehmen.


D1 zeigt (insbes. Abstract, S. 6 Z. 17 – S. 7 Z. 14, S. 8 Z. 17-24 und Fig. 1) ein
System zur Durchführung einer Anbieterauktion mit einem Servercomputer und
einem Computernetzwerk, bei dem die Ware und auch der Start der Auktion auf
einem Bietercomputer angezeigt werden (Merkmale (1) und (a)). Eine Übertragung der Gebote des Bieters über das Computernetzwerk (Merkmal (b)) ist
ebenso in D1 (bspw. S. 8 Z. 25-29) beschrieben.

                                    -8-



Der Anspruch 1 ist demnach nicht gewährbar.


3.    Mit dem Patentanspruch 1 fallen auch die nebengeordneten Ansprüche 7,
14 und 15 sowie die Unteransprüche 2 bis 6 und 8 bis 13, da über einen Antrag
nur einheitlich entschieden werden kann (BGH GRUR 1997, 120 – Elektrisches
Speicherheizgerät).




Dr. Morawek             Eder              Dr. Thum-Rung            Hoffmann




                                                                          Me
