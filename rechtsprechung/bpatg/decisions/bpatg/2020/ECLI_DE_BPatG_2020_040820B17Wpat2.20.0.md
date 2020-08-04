---
ecli: "ECLI:DE:BPatG:2020:040820B17Wpat2.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 2/20"
decided: "2020-08-04"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=27&nr=39990&anz=666&pos=415&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2020-08-04_17_W-pat_2_20_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md"]
---

# Bundespatentgericht, 17 W (pat) 2/20 vom 2020-08-04

## Entscheidung

BUNDESPATENTGERICHT


      17 W (pat) 2/20                                                 Verkündet am
 _______________________
                                                                     04. August 2020
      (Aktenzeichen)
                                                                            …




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 10 2013 205 886.1


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die     mündliche   Verhandlung   vom   04. August 2020   unter   Mitwirkung    des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, des Richters Dipl.-Phys. Dr. Forkel,
des Richters Dipl.-Ing. Hoffmann und der Richterin Akintche




ECLI:DE:BPatG:2020:040820B17Wpat2.20.0

                                        -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                         I.


Die vorliegende Patentanmeldung wurde am 03. April 2013 beim Deutschen Patentund Markenamt in englischer Sprache eingereicht. Sie nimmt eine US-Priorität
(US 13/440,945) vom 05. April 2012 in Anspruch und trägt in der deutschen Übersetzung die Bezeichnung


             „Dynamische Bankmodus-Adressierung für Speicherzugriff“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 10. Januar 2017 zurückgewiesen.
Zur Begründung führt die Prüfungsstelle sinngemäß aus, dass der Gegenstand des
jeweiligen Anspruchs 1 nach Haupt- und Hilfsantrag nicht neu sei.


Gegen diesen Beschluss ist die am 13. Februar 2017 eingegangene Beschwerde
gerichtet.


Die Anmelderin beantragt, den Beschluss der Prüfungsstelle aufzuheben und das
nachgesuchte Patent auf der Grundlage folgender Unterlagen zu erteilen:
     Patentansprüche 1 bis 10, eingereicht am 24. Juli 2020,
     Beschreibung Seiten 1 bis 44 und
     9 Blatt Zeichnungen mit Figuren 1 bis 5, jeweils vom 03. Juli 2013.

                                         -3-



Der nunmehr geltende Patentanspruch 1, hier mit einer möglichen Gliederung versehen, lautet:


M1    Ein Verarbeitungssubsystem aufweisend:
M2    eine Adressenerzeugungseinheit, die konfiguriert ist zum:
      M2.1 Empfangen von mehreren Speicherzugriffsinstruktionen mit einer ersten Speicherzugriffsinstruktion, die eine individuelle Speicheradresse
             spezifiziert,
      M2.2 wobei ein Speicherbankmodus für jede der mehreren Speicherzugriffsinstruktionen spezifiziert wird;
      M2.3 Empfangen eines Speicherbankmodus für die erste Speicherzugriffsinstruktion, der die Bitbreite pro Speicherbank eines Multibank-Speichers spezifiziert,
      M2.4 wobei der Speicherbankmodus zu einem ersten Mapping einer Speicheradresse zu einer Speicherbank führt, wenn der Speicherbankmodus ein erster Speicherbankmodus ist, und der Speicherbankmodus
             zu einem zweiten Mapping einer Speicheradresse zu einer Speicherbank führt, das sich von dem ersten Mapping unterscheidet, wenn
             der Speicherbankmodus ein zweiter Speicherbankmodus ist; und
      M2.5 dynamischen Mappens der individuellen Speicheradresse basierend
             auf dem Speicherbankmodus, um eine gemappte individuelle Speicheradresse zu erzeugen; und
M3    eine Laden/Speichern-Einheit,
      M3.1 die zwischen der Adressenerzeugungseinheit und dem Multibank-Speicher gekoppelt ist und konfiguriert ist
      M3.2 zum Senden einer Leseanforderung oder einer Schreibeanforderung
             an den Multibank-Speicher, um die erste Speicherzugriffsinstruktion
             auszuführen.


Zu den weiteren Ansprüchen 2 bis 10 wird auf die Akte verwiesen.

                                        -4-



Im Verfahren wurden folgende Druckschriften genannt:
D1:     DE 10 2009 012 409 A1,
D2:     US 6 889 304 B2
sowie
D3:     US 2010/0076941 A1.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig.
Sie hat jedoch keinen Erfolg, da der Gegenstand des Patentanspruchs 1 nicht neu
ist (§§ 1 und 3 PatG).


1.      Die vorliegende Anmeldung bezieht sich generell auf Parallelverarbeitung
und spezifischer auf eine parallele Architektur, die dynamisches Mappen von Speicherbankadressen für Zugriffe auf Multibank-Speicher unterstützt (vgl. Offenlegungsschrift, Absatz [0001]).


Gemäß der Anmeldung (vgl. Offenlegungsschrift, Absätze [0002] und [0003]) seien
in einer einzelne-Instruktions-, mehrfache-Threads-(SIMT)-Verarbeitungsumgebung (engl. „single-instruction, multiple-thread (SIMT) processing environment”) die
Threads in Gruppen bestehend aus P parallelen Threads organisiert. Diese würden
Warps genannt und führten das gleiche Programm aus. Obwohl die P Threads einer
Threadgruppe jede Instruktion des Programmes parallel ausführten, führe jeder
Thread einer Threadgruppe unter Verwendung seiner eigenen Daten und Register
die Instruktion unabhängig aus. Jeder Thread in der Threadgruppe sei dazu konfiguriert, auf einen Multibank-Speicher zuzugreifen. Dieser Zugriff erfolge unter Verwendung eines festen Mappings von Adressen pro Thread (engl. „per-thread
adresses”) auf die Speicherbänke des Multibank-Speichers. Wenn mehrere

                                       -5-



Threads auf zwei oder mehr Stellen in der gleichen Speicherbank zugreifen müssten, als innerhalb eines einzigen Taktzyklus zugegriffen werden könnten, dann liege
ein Speicherbankkonflikt vor.
Anwendungsprogramme seien typischerweise so geschrieben, dass Speicherbankkonflikte vermieden werden, wenn die parallelen Threads einer Threadgruppe den
Multibank-Speicher ausliest und beschreibt, so dass Daten für alle der parallelen
Threads in der Threadgruppe in einem einzigen Taktzyklus gelesen oder geschrieben werden. Ein Programm könne zum Beispiel so geschrieben werden, dass von
einer Threadgruppe auf entweder eine Zeile oder eine Säule von einem Array von
Daten zugegriffen wird, ohne dass ein Speicherbankkonflikt auftritt. Wenn Speicherbankkonflikte aufträten, müssten die Zugriffe für Adressen, die auf die gleiche
Speicherbank gemappt sind, in separaten Taktzyklen durchgeführt werden, wobei
die Performance reduziert werde.


Vor diesem Hintergrund ist es die Aufgabe der Anmeldung ein Verfahren zur Vermeidung von Speicherbankkonflikten anzugeben, wenn parallele Threads einer
Threadgruppe auf einen Multibank-Speicher zugreifen (vgl. Offenlegungsschrift,
Absatz [0004]).


Zur Lösung dieser Aufgabe schlägt der Patentanspruch 1 ein Verarbeitungssubsystem vor (Merkmal M1), das eine Adressenerzeugungseinheit umfasst (Merkmal M2). Das Verarbeitungssubsystem ermöglicht den Zugriff auf einen Multibankspeicher (vgl. Offenlegungsschrift, Absatz [0008]). Die Adressenerzeugungseinheit
ermöglicht die Ausführung von sogenannten Adressenberechnungstasks (vgl.
Offenlegungsschrift, Absatz [0078]). Die Adressenerzeugungseinheit empfängt
mehrere Speicherzugriffsinstruktionen, die eine individuelle Speicheradresse spezifizieren (Merkmal M2.1), mit denen ein Speicherbankmodus für jede der mehreren
Speicherzugriffsinstruktionen spezifiziert wird (Merkmal M2.2). Außerdem empfängt
die Adressenerzeugungseinheit einen Speicherbankmodus für die erste Speicherzugriffsinstruktion, der die Bitbreite pro Speicherbank eines Multibank-Speichers

                                       -6-



spezifiziert (Merkmal M2.3). Damit werden der Adressenerzeugungseinheit Anweisungen bzw. Parameter übergeben, die die Grundlage für die Berechnung der Speicheradressen bilden. Der Wortlaut dieser Merkmale lässt dabei offen, ob die individuelle Speicheradresse, der Speicherbankmodus sowie die Bitbreite zusammen
mit der Speicherzugriffsinstruktion übergeben werden, oder diese Daten in der Speicherzugriffsinformation bereits enthalten sind und aus dieser erst berechnet werden
müssen. Merkmal M2.4 sieht zwei unterschiedliche Speicherbankmodi (erster und
zweiter Speicherbankmodus) vor, die jeweils zu einem anderen Mapping einer Speicheradresse (erstes bzw. zweites Mapping einer Speicheradresse) zu einer Speicherbank führen. Basierend auf dem Speicherbankmodus erfolgt ein dynamisches
Mappen der individuellen Speicheradresse, um eine gemappte individuelle Speicheradresse zu erzeugen (Merkmal M2.5). Somit wird in Abhängigkeit vom jeweiligen Speicherbankmodus die Speicheradresse dynamisch erzeugt, um bspw.
Zugriffe auf den Speicher von Programmen zu ermöglichen, die für unterschiedliche
Speicherbankbreiten geschrieben sind. Das Verarbeitungssubsystem beinhaltet
weiterhin eine Laden/Speichern-Einheit (Merkmal M3), die zwischen der Adressenerzeugungseinheit und dem Multibank-Speicher angeordnet ist (Merkmal M3.1) und
die das Ausführen einer Speicherzugriffsinstruktion bewirkt, d.h. das Senden einer
Lese- oder Schreibanforderung (Merkmal M3.2). Mit dieser Einheit wird demnach
der eigentliche Speichervorgang ausgeführt wie bspw. ein Lese- oder Schreibzugriff
auf einen Speicher.




Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zur Vermeidung
von Speicherbankkonflikten beim Zugriff paralleler Threads einer Threadgruppe auf
einen Multibank-Speicher zu verbessern, ist ein Diplom-Ingenieur der Fachrichtung
Elektrotechnik oder ein Informatiker mit mehrjähriger Berufserfahrung im Bereich
der Entwicklung und Implementierung von Speichersteuerungen (Memory-Controllern) anzusehen.

                                        -7-



2.       Der Gegenstand des Patentanspruchs 1 ist nicht neu.


Als im Stand der Technik besonders relevant sieht der Senat die Druckschrift D2
an.


Aus der D2 (Abstract, Anspruch 1, Fig.3) ist ein System für die Speicherverwaltung
zu entnehmen. Das System kann dabei bspw. als eigenes Teilsystem bzw. Verarbeitungssubsystem auf einem Motherboard (Sp.8 Z.13-19) implementiert sein
(Merkmal M1).
Das System erhält den Befehl, einen Speicherzugriff bzw. mehrere Speicherzugriffe
auszuführen, wobei der Befehl bzw. die Befehle eine Speicheradresse umfasst
(Sp.2 Z.29-58, Sp.4 Z.38-66, Fig.3). Wird der Befehl ausgeführt, so werden Daten
in den Speicher geschrieben bzw. aus dem Speicher ausgelesen, wobei hierzu die
Speicheradressen bestimmt werden (Fig.3, Sp.4 Z.63 – Sp.5 Z.6, Sp.13 Z.49-65,
Sp.14 Z.37-42). Die Daten werden dabei zu einem Speicherort „geroutet“, d.h. es
erfolgt die Bestimmung des Speicherplatzes und somit eine Adressumsetzung. Als
Adressumsetzungseinheit i.S.d. Merkmals M2 fungiert die Logik 310 (Sp.4 Z.63
– Sp.5 Z.6, Fig.3 „configuration logic“), der Speicherzugriffsbefehle zugeführt werden, auf deren Basis die Speicheradressen festgelegt werden (Merkmale M2 und
M2.1).
Die Zugriffssignale, d.h. die Anforderung für den Speicherzugriff, enthalten weitere
Informationen. Die weiteren Informationen, wie z.B. die Speicherbank, die Speicherbankbreite sowie der Speicherplatz, werden vor dem Zugriff generiert und mit
dem Zugriffssignal übertragen (Sp.5 Z.50-64, Sp.7 Z.25-31, Sp.14 Z.24-25). Auf
Basis der Bitbreite der logischen Speicherbank wird ein entsprechender Modus
ausgewählt und bei mehreren Zugriffen werden unterschiedliche Modi ausgewählt
(Sp.7 Z.25-31, Sp.14 Z.24-42 „mode select“). Damit sind die Merkmale M2.2 und
M2.3 aus der D2 zu entnehmen.
Die Zugriffsadressen werden dynamisch festgelegt (Sp.5 Z.50-64, Sp.14 Z.24-42),
wobei ein erster Zugriff auf eine oder einen ersten Teil der Speicherbänke und ein
zweiter Zugriff auf eine andere oder einen anderen Teil der Speicherbänke

                                       -8-



„geroutet“ wird (Sp.4 Z.46-51, Sp.5 Z.7-40, Sp.5 Z.50-64, Sp.14 Z.24-42). Mit dem
„Routing“ wird demnach für eine erste Speicherbank in einem ersten Modus und für
eine zweite Speicherbank in einem zweiten Modus die entsprechende Adresse
dynamisch festgelegt. Weiterhin wird der Fachmann in dem „Routing“ der D2 das
anspruchsgemäße „Mapping“ erkennen. Ihm ist dabei geläufig, dass ein solches
„Mapping“ nichts Anderes bedeutet, als dass die Speicheradresse aus dem Speicherzugriffsbefehl berechnet bzw. diese aus einer Speicherzugriffstabelle ausgelesen wird. Aus der D2 entnimmt der Fachmann hinsichtlich der Berechnung und
Umsetzung der Adressen, dass diese auf Basis von Parametern ermittelt und
anschließend durch Anlegen von Signalen auf die Adresssteuerleitungen angesteuert werden. Dabei ist konkret ausgeführt, dass die Signale (Schreib- bzw. Lesesignale) anhand von der programmierten Datenbreite, d.h. der Datenbreite des
zugreifenden Programms, und von weiteren Adressinformationen generiert und weitergegeben werden (Sp.5 Z.58-64). Weiter ist eine dynamische Auswahl zwischen
verschiedenen Speichermodi in Abhängigkeit von der Datenbreite des Programms
und somit eine dynamische Auswahl des Speichermodus sowie der dem Modus
entsprechenden Adressumsetzung gezeigt (Sp.14 Z.34-46). Somit offenbart die D2
die in der vorliegenden Anmeldung beanspruchte Ermittlung der Speicheradresse
und insbesondere ein „Mapping“ i.S.d. Merkmale M2.4 und M2.5.
Schließlich ist in der D2 (Fig.3, Sp.5 Z.65 – Sp.6 Z.61, „Data control circuit“ 315)
eine Schreib-/Lese-Einheit (Laden/Speichern-Einheit) gezeigt, die zwischen der
Adresserzeugungseinheit 310 und dem Multibankspeicher 305 angeordnet ist.
Diese Einheit führt die übertragenen Befehle und somit die Speicherzugriffe aus.
Damit sind auch die Merkmale M3, M3.1 und M3.2 aus der Druckschrift zu
entnehmen.




Nach alledem gehen sämtliche Merkmale des Anspruchs 1 aus der D2 hervor.




Die Ausführungen der Anmelderin vermochten nicht zu überzeugen.

                                       -9-



Die Anmelderin führt aus, dass aus der D2 lediglich eine feste Zuordnung der Speicherbänke (ähnlich einer festen Verdrahtung) zu den Speicherbankmodi zu entnehmen sei. Damit sei jedem Speicherzugriff eine Speicherbank entsprechend der
Wortbreite des Zugriffs zugeordnet. Dies gehe durch die Bezeichnung „Routing“ und
die Verwendung von „Latches“ aus der D2 hervor.


Diesem Einwand kann nicht gefolgt werden. Denn aus der D2 ist zwar zu entnehmen, dass jeder physikalischen Speicherbank sogenannte „Latches“ zugeordnet
sind (Sp.5 Z.50-51). Jedoch erfolgt die Ansteuerung der Speicherbänke über
Signale, welche von der Steuerungslogik („Configuration logic 310“) auf Basis der
Bitbreite der Programmdaten und weiteren Adressinformationen generiert und
damit ebenfalls für jeden Schreib- bzw. Lesezugriff berechnet werden (Sp.5
Z.58-64).




Weiter gibt der Vertreter der Anmelderin an, dass die D2 nicht zeige, dass mit den
Speicherzugriffsinstruktionen eine individuelle Andresse sowie ein Speicherbankmodus mitgegeben werden.


Diese Darstellung greift zu kurz. Wie bereits ausgeführt lässt der Anspruchswortlaut
offen, ob diese Vorgaben bereits zusammen mit der Speicherzugriffsinstruktion
übergeben werden, oder ob sie aus der Speicherzugriffsinformation berechnet werden. Aus der D2 ist jedenfalls die Berechnung der Adressierung anhand der Bitbreite der Programmdaten sowie weiteren Adressinformationen (Sp.5 Z.58-64) zu
entnehmen, was nach fachmännischem Verständnis der zweiten Alternative entspricht.




Schließlich führt die Anmelderin aus, dass ein erstes Mapping zu einer ersten Speicherbank in einem ersten Speicherbankmodus und ein zweites Mapping zu einer
zweiten Speicherbank in einem zweiten Speicherbankmodus, welches dynamisch

                                            - 10 -



basierend auf dem Speicherbankmodus erzeugt wird, nicht aus der D2 zu entnehmen sei.


Auch diesen Ausführungen kann nicht beigetreten werden. Denn die D2 zeigt, dass
die Zugriffsadressen dynamisch festgelegt (Sp.5 Z.50-64, Sp.14 Z.24-42) werden.
Dabei erfolgt in Abhängigkeit der aus der Speicherzugriffsinstruktion berechneten
Zugriffsdaten ein erster Zugriff auf eine oder einen ersten Teil der Speicherbänke
und ein zweiter Zugriff auf eine andere oder einen anderen Teil der Speicherbänke
(Sp.4 Z.46-51, Sp.5 Z.7-40, Sp.5 Z.50-64, Sp.14 Z.24-42).




3.      Mit dem Anspruch 1 fallen auch die Ansprüche 2 bis 10, da über einen Antrag
nur einheitlich entschieden werden kann (BGH GRUR 1997, 120 - Elektrisches
Speicherheizgerät).




4.      Eine Zurückverweisung der Sache an das Deutsche Patent- und Markenamt
kam nicht in Betracht, denn die Sache war entscheidungsreif, es bedarf keiner weiteren Aufklärung des Sachverhalts.




Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
        Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,

                                          - 11 -



   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern
       er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
       hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof
zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Morawek                   Forkel                   Hoffmann                      Akintche
