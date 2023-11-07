---
ecli: "ECLI:DE:BPatG:2023:071123B17Wpat9.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 9/20"
decided: "2023-11-07"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=29&nr=43903&anz=529&pos=446&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2023-11-07_17_W-pat_9_20_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 9/20 vom 2023-11-07

## Entscheidung

BUNDESPATENTGERICHT



    17 W (pat) 9/20
 _______________________

    (Aktenzeichen)




                             BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 11 2016 001 075.3


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
7. November 2023 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys.
Dr. Morawek, des Richters Dipl. Ing. Hoffmann, der Richterin Akintche und des
Richters Dipl.-Phys. Dr. Städele beschlossen:




ECLI:DE:BPatG:2023:071123B17Wpat9.20.0

                                       -2-



      Auf die Beschwerde der Anmelderin wird der Beschluss der
      Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
      Markenamts vom 25. Juli 2018 aufgehoben und das Patent mit
      folgenden Unterlagen erteilt:


          Patentansprüche 1 bis 10, eingereicht am 10. Juli 2023,
          Beschreibung Seiten 1 bis 78, eingereicht am 06. Juli 2023,
          31 Blatt Zeichnungen mit Figuren 1A bis 10C vom 04. April 2023.




                                      Gründe


                                        I.


Die vorliegende Patentanmeldung ist eine PCT-Anmeldung in nationaler Phase,
welche als WO 2017 / 019 794 A1 (im Folgenden als WO 2017 bezeichnet) in
Englisch und als DE 11 2016 001 075 T5 (im Folgenden als DE-T5 bezeichnet) in
deutscher Übersetzung veröffentlicht wurde. Ihr PCT-Anmeldetag ist der
27. Juli 2016. Sie nimmt die Priorität von zwei US-Voranmeldungen vom
27. Juli 2015 sowie von drei US-Voranmeldungen vom 26. Juli 2016 in Anspruch.


In der deutschen Übersetzung trägt sie die Bezeichnung


              „Verteiltes Speichern und Abrufen von Datensätzen“.


Die Anmeldung war in der Anhörung vom 25. Juli 2018 durch Beschluss der
Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts mit der
Begründung zurückgewiesen worden, dass die Gegenstände der jeweiligen
Patentansprüche 1 nach dem (damals geltenden) Hauptantrag sowie den

                                         -3-



Hilfsanträgen 1 bis 3 nicht auf einer erfinderischen Tätigkeit des Fachmanns
beruhten, soweit sie ein technisches Problem mit technischen Mitteln lösten.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Auf einen
Zwischenbescheid des Senats vom 17. Mai 2022 hin hat diese eine überarbeitete
Fassung der Patentansprüche eingereicht, um die unter Schutz zu stellende
Erfindung klar und deutlich zu umschreiben und um sich gegen den bekannten
Stand der Technik abzugrenzen; die Beschreibung und die Zeichnungen wurden
entsprechend angepasst. Mit der Eingabe vom 10. Juli 2023 stellt die Anmelderin
den Antrag,


      den Zurückweisungsbeschluss der Prüfungsstelle aufzuheben und
      ein Patent zu erteilen auf Basis der folgenden Unterlagen:


          Patentansprüche 1 bis 10, eingereicht am 10. Juli 2023,
          Beschreibung Seiten 1 bis 78, eingereicht am 06. Juli 2023,
          31 Blatt Zeichnungen mit Figuren 1 bis 10C vom 04. April 2023.




Das geltende Patentbegehren, hier bezüglich des Hauptanspruchs mit einer
möglichen Gliederung versehen, lautet:


1. Computerimplementiertes Verfahren, welches Folgendes umfasst:


      VS1     ein Datensatz umfasst mehrere Datensatzteile,
      VS2     gespeicherte Metadaten geben die Organisation von Daten innerhalb
              des Datensatzes an,
      VS3     eine oder mehrere Speichervorrichtungen halten einen Datensatz in
              einer Datendatei,

                                   -4-



VS4   Zuordnungskartendaten, gespeichert in der einen oder mehreren
      Speichervorrichtungen, geben die Organisation des Datensatzes in
      mehrere Datenblöcke innerhalb der Datendatei an,
VS5   die   Zuordnungskartendaten           umfassen    mehrere     Zuordnungskarteneinträge,
VS6   die Metadaten oder die Zuordnungskartendaten geben eine zweite
      Anzahl von Knotenvorrichtungen an, die zuletzt am Speichern des
      Datensatzes innerhalb der Datendatei beteiligt waren,
VS7   die Metadaten oder die Zuordnungskartendaten geben an, ob der
      Datensatz partitionierte Daten umfasst,
VP    wenn der Datensatz partitionierte Daten umfasst:
VP1   die Daten innerhalb des Datensatzes sind zu mehreren Partitionen
      organisiert,
VP2   die Daten innerhalb jeder Partition müssen gemeinsam verarbeitet
      werden,     entsprechend      muss      jede   Partition   einer   einzigen
      Knotenvorrichtung zugewiesen werden, um die Daten innerhalb jeder
      Partition für eine gemeinsame Verarbeitung zusammen zu halten,
VP3   jeder Partition ist ein eindeutiges Partitionsetikett zugeordnet, von
      welchem eine entsprechende gehashte Kennung abgeleitet wird,
      welche die Partition identifiziert,
VP4   jeder Datenblock der mehreren Datenblöcke enthält zumindest einen
      Datenunterblock,
VP5   jeder Datenunterblock enthält Daten einer einzelnen Partition,
VP6   jeder Datenunterblock entspricht einem einzelnen Datensatzteil der
      mehreren Datensatzteile
VP7   jeder der Zuordnungskarteneinträge entspricht einem einzigen
      Datenblock der mehreren Datenblöcke,
VP8   jeder der Zuordnungskarteneinträge enthält einen oder mehrere
      Zuordnungskartenuntereinträge,
VP9   jeder Zuordnungskartenuntereintrag entspricht einem einzelnen
      Datenunterblock,

                                    -5-



VP10 jeder    Zuordnungskartenuntereintrag            enthält   eine     Datenunterblockgröße      und   eine    gehashte    Kennung         der    Partition    des
      entsprechenden Datenunterblocks,
VM    wobei folgende Schritte durch die Prozessorkomponente einer
      Steuervorrichtung durchgeführt werden:
VM1 Empfangen von Angaben von mehreren Knotenvorrichtungen, welche
      von     ihnen     verfügbar     sind     für      die     Ausführung         einer
      Verarbeitungsaufgabe mit wenigstens einem Datensatzteil der
      mehreren Datensatzteile,
VM2 Abrufen der Metadaten und der Zuordnungskartendaten von der einen
      oder den mehreren Speichervorrichtungen über ein Netzwerk,
VM3 ansprechend auf die Angabe innerhalb der Metadaten oder der
      Zuordnungskartendaten, dass der Datensatz partitionierte Daten
      umfasst:
      VM3.1           Bestimmen     einer    ersten    Anzahl     der    verfügbaren
                      Knotenvorrichtungen aus den empfangenen Angaben,
                      welche Knotenvorrichtungen verfügbar sind,
      VM3.2           Zuweisen, jeder der verfügbaren Knotenvorrichtungen,
                      eines Wertes aus einer Reihe positiver ganzzahliger
                      Werte als ein Festlegungswert, wobei sich die Reihe von
                      einem ganzzahligen Wert von 0 bis zu einem positiven
                      ganzzahligen Wert, der gleich der ersten Anzahl minus
                      dem ganzzahligen Wert von 1 ist, erstreckt,
      VM3.3           Abrufen der zweiten Anzahl von Knotenvorrichtungen
                      aus den Metadaten oder den Zuordnungskartendaten,
      VM3.4           Vergleichen der ersten und der zweiten Anzahl von
                      Knotenvorrichtungen,      um       eine     Übereinstimmung
                      zwischen der ersten und der zweiten Anzahl zu
                      erkennen,
      VM3.5           wenn der Datensatz partitionierte Daten umfasst und
                      wenn die erste und die zweite Anzahl übereinstimmen,

            -6-



werden für jeden Zuordnungskarteneintrag der Zuordnungskartendaten folgende Schritte durch die Prozessorkomponente durchgeführt:
a1)   Abrufen,           aus            einem               einzigen
      Zuordnungskartenuntereintrag                              des
      Zuordnungskarteneintrags,              der       gehashten
      Kennung für einen einzigen Datenunterblock
      innerhalb des entsprechenden Datenblocks,
a2)   Abrufen,                   aus                          jedem
      Zuordnungskartenuntereintrag,                            einer
      Datenunterblockgröße        für    jeden        der    Datenunterblöcke innerhalb des entsprechenden Datenblocks,
b)    Bestimmen einer Stelle des entsprechenden
      Datenblocks innerhalb der Datendatei,
c)    Dividieren der gehashten Kennung durch die erste
      Anzahl, um einen Modulo-Wert zu erhalten,
d)    Vergleichen des Modulo-Werts mit dem jeder der
      verfügbaren Knotenvorrichtungen zugewiesenen
      Festlegungswert, um eine verfügbare Knotenvorrichtung   zu     identifizieren,      der    ein     Festlegungswert zugewiesen ist, welcher mit dem
      Modulo-Wert übereinstimmt, und
e)    Übertragen      eines          Zeigers,         von       der
      Steuervorrichtung         an        die          verfügbare
      Knotenvorrichtung, welcher der Festlegungswert
      zugewiesen    ist,    der mit dem            Modulo-Wert
      übereinstimmt, wobei der Zeiger Folgendes
      umfasst:
e1)   eine Angabe zur Stelle des entsprechenden
      Datenblocks und

                                         -7-



                              e2)   eine Summe der Datenunterblockgrößen aller
                                    Datenunterblöcke innerhalb des entsprechenden
                                    Datenblocks.




2.    Computerimplementiertes Verfahren nach Anspruch 1, wobei ansprechend auf
      die Angabe, dass der Datensatz partitionierte Daten umfasst, und ansprechend
      auf die Erkennung eines Fehlens einer Übereinstimmung zwischen der ersten
      und    der    zweiten    Anzahl   für   jeden    Zuordnungskarteneintrag    der
      Zuordnungskartendaten werden von der Prozessorkomponente die folgenden
      Schritte ausgeführt:
      für   jeden   Zuordnungskartenuntereintrag       innerhalb    des   Zuordnungskarteneintrags:
      Abrufen der Datenunterblockgröße und der gehashten Kennung des
      entsprechenden Datenunterblocks innerhalb des entsprechenden Datenblocks
      aus dem Zuordnungskartenuntereintrag,
      Bestimmen einer Stelle des entsprechenden Datenunterblocks innerhalb der
      Datendatei,
      Dividieren der gehashten Kennung durch die erste Anzahl, um einen Modulo-Wert zu erhalten,
      Vergleichen       des   Modulo-Werts    mit     dem   jeder   der   verfügbaren
      Knotenvorrichtungen zugewiesenen Festlegungswert, um eine verfügbare
      Knotenvorrichtung zu identifizieren, der ein Festlegungswert zugewiesen ist,
      welcher mit dem Modulo-Wert übereinstimmt, und
      Übertragen, von der Steuervorrichtung, eines Zeigers an die verfügbare
      Knotenvorrichtung, welcher der Festlegungswert zugewiesen ist, der mit dem
      Modulo-Wert übereinstimmt, wobei der Zeiger Folgendes umfasst:
      eine Angabe zur Stelle des Datenunterblocks und die Datenunterblockgröße.


3. Computerimplementiertes Verfahren nach Anspruch 1, welches Folgendes
     umfasst:

                                               -8-



   ansprechend      auf     eine     Angabe     innerhalb     der    Metadaten   oder     der
   Zuordnungskartendaten, dass der Datensatz keine partitionierten Daten umfasst,
   werden für jeden Zuordnungskarteneintrag der Zuordnungskartendaten von der
   Prozessorkomponente die folgenden Schritte ausgeführt:
   Abrufen einer Datenblockgröße und einer Datenblockanzahl aus dem
   Zuordnungskarteneintrag,           wobei     die     Datenblockanzahl      eine     Anzahl
   benachbarter Datenblöcke in der Datendatei, die dem Zuordnungskarteneintrag
   entsprechen, angibt, und
   für jeden Datenblock, der dem Zuordnungskarteneintrag entspricht:
   Bestimmen einer Stelle des entsprechenden Datenblocks innerhalb der
   Datendatei,
   Auswählen einer der verfügbaren Knotenvorrichtungen und
   Übertragen eines Zeigers an die ausgewählte der verfügbaren Knotenvorrichtungen, wobei der Zeiger Folgendes umfasst:
   eine Angabe zur Stelle des entsprechenden Datenblocks innerhalb der
   Datendatei und die Datenblockgröße.


4. Computerimplementiertes Verfahren nach Anspruch 3, wobei die Auswahl einer
   der verfügbaren Knotenvorrichtungen eine Ringauswahl einer der verfügbaren
   Knotenvorrichtungen umfasst.


5. Computerimplementiertes Verfahren nach Anspruch 1, wobei, ansprechend
   darauf,   dass         der      Datensatz     partitionierte     Daten    umfasst,     die
   Prozessorkomponente der Steuervorrichtung als eine der verfügbaren Knotenvorrichtungen agiert, indem eine Angabe der Stelle und einer entsprechenden
   Summe     der    Datenunterblockgrößen             sämtlicher    Datenunterblöcke    eines
   Datenblocks entsprechend einem der Zuordnungskarteneinträge verwendet
   werden, um den Datenblock aus der Datendatei zumindest teilweise parallel zu
   zumindest einer anderen der verfügbaren Knotenvorrichtungen abzurufen.

                                        -9-



6. Computerimplementiertes       Verfahren       nach    Anspruch       5,     wobei       eine
   Verarbeitungsaufgabe mit jedem Datenunterblock innerhalb des Datenblocks als
   die eine der verfügbaren Knotenvorrichtungen zumindest teilweise parallel zu
   zumindest einer anderen der verfügbaren Knotenvorrichtungen ausgeführt wird.


7. Computerimplementiertes Verfahren nach Anspruch 1, wobei das Abrufen der
   Zuordnungskartendaten aus der einen oder mehr als einen Speichervorrichtung
   Folgendes umfasst:
   Abrufen einer Basiszuordnungskarte aus der Datendatei,
   Analysieren der Basiszuordnungskarte zum Feststellen, ob zumindest ein Teil
   der   Zuordnungskartendaten       innerhalb      einer    oder   mehr           als     einer
   Zuordnungskartenerweiterung innerhalb der Datendatei gespeichert ist, und
   ansprechend      auf   eine   Feststellung,    dass      zumindest        ein    Teil    der
   Zuordnungskartendaten innerhalb einer oder mehr als einer Zuordnungskartenerweiterung gespeichert ist:
   Abrufen der einen oder mehr als einen Zuordnungskartenerweiterung aus der
   Datendatei und
   Abrufen zumindest einer Untermenge der Zuordnungskarteneinträge aus der
   einen oder mehr als einen Zuordnungskartenerweiterung.


8. Computerimplementiertes Verfahren nach Anspruch 7, wobei beim Abrufen der
   Zuordnungskartendaten von der einen oder mehr als einen Speichervorrichtung
   ansprechend auf eine Feststellung, dass kein Teil der Zuordnungskartendaten
   innerhalb einer oder mehr als einer Zuordnungskartenerweiterung gespeichert
   ist, alle Zuordnungskarteneinträge aus der Basiszuordnungskarte abgerufen
   werden.


9. Computerimplementiertes Verfahren nach Anspruch 1, wobei beim Empfang von
   Angaben, welche Knotenvorrichtungen von den mehreren Knotenvorrichtungen
   verfügbar sind, Folgendes ausgeführt wird:

                                         - 10 -



   wiederholtes Empfangen von Angaben zum Status von den mehreren
   Knotenvorrichtungen und
   wiederholtes Aktualisieren einer gespeicherten Angabe zur Verfügbarkeit jeder
   Knotenvorrichtung von den mehreren Knotenvorrichtungen.


10. Computerimplementiertes Verfahren nach Anspruch 1, wobei eine Angabe zu
   einer   mit   dem       Datensatz   auszuführenden      Aufgabe     den   mehreren
   Knotenvorrichtungen bereitgestellt wird, um es zumindest einer ersten
   Knotenvorrichtung von den mehreren Knotenvorrichtungen zu ermöglichen, die
   Aufgabe mit einem ersten Datensatzteil des Datensatzes auszuführen, und es
   zumindest      einer     zweiten    Knotenvorrichtung      von     den    mehreren
   Knotenvorrichtungen zu ermöglichen, die Aufgabe mit einem zweiten
   Datensatzteil des Datensatzes zumindest teilweise parallel auszuführen.




Eine konkrete Aufgabe ist in der Anmeldung nicht angegeben.


Aus der Anmeldung ist zu entnehmen, dass eine Verbesserung des verteilten
Speicherns und Abrufens eines von mehreren Knotenvorrichtungen verarbeiteten
Datensatzes von den beschriebenen Ausführungsformen umfasst sei (vgl. DE-T5-
Schrift, Absatz [0073]).



                                           II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
Erfolg, da das nunmehr geltende Patentbegehren durch den bekannt gewordenen
Stand der Technik nicht vorweggenommen oder nahegelegt ist und auch die übrigen
Kriterien für eine Patenterteilung erfüllt sind (PatG §§ 1 bis 5, § 34).

                                       - 11 -



1.      Die vorliegende Patentanmeldung betrifft die Nutzung verteilter Rechen-Ressourcen in einem Netz von Rechenknoten (Knotenvorrichtungen) und genauer
die Koordination zwischen Rechenknoten und Speichern sowie die Organisation
des Speicherns von Datensätzen, um das verteilte Speichern und Abrufen eines
von mehreren Rechenknoten verarbeiteten Datensatzes zu verbessern. Die
Ausführung von Analysen großer Datensätze („Big Data“) werde auf verschiedenen
Gebieten wie z.B. Simulationen, Prozessüberwachung, Entscheidungstreffung,
Verhaltensmodellierung und Vorhersagebildung zunehmend üblich. Solche Analysen würden häufig durch Rechen-Netze („Grids“) mit unterschiedlicher Anzahl verfügbarer Knotenvorrichtungen (= Rechenknoten) ausgeführt, während die zu verarbeitenden Datensätze häufig innerhalb eines separaten Satzes von Speichervorrichtungen gespeichert seien. Dies bringe die Herausforderung mit sich, solche
großen Datensätze zwischen Speichervorrichtungen und verschiedenen Rechenknoten des Netzes auf effektive Weise auszutauschen (vgl. DE-T5, Absätze [0002],
[0003]).


Der neue Patentanspruch 1 betrifft ein computerimplementiertes Verfahren
(Merkmal 1.) und soll die Effektivität beim Datenaustausch erhöhen.


Im ersten Merkmalskomplex (VS) sind die Datensätze, die Speicherung sowie die
Metadaten und Zuordnungskartendaten spezifiziert.


Konkret umfasst ein Datensatz mehrere Datensatzteile, d.h. es erfolgt eine
Organisation bzw. Strukturierung der Daten (vgl. DE-T5, Absatz [0194] – Merkmal
VS1).


Die Metadaten beschreiben, wie die Daten innerhalb eines Datensatzes organisiert
sind (vgl. DE-T5, Absatz [0192], Fig. 12A-12C – Merkmal VS2), wobei die
Datensätze in einem oder mehreren Speichern abgelegt sind (vgl. DE-T5, Absatz
[0192], Fig. 12A-12C – Merkmal VS3).

                                            - 12 -



Weiter sind in den Speichern Zuordnungskartendaten abgelegt, die die Aufteilung
der Datensätze in Datenblöcke angeben (vgl. DE-T5, Absatz [0197], Fig. 12A-12C –
Merkmal        VS4).         Dabei         weisen       die       Zuordnungskartendaten
Zuordnungskarteneinträge auf, mit denen bspw. die Größe eines Datenblocks
definiert wird (vgl. DE-T5, Absatz [0206], Fig. 12A-12C – Merkmal VS5).


Die Metadaten oder die Zuordnungskartendaten geben zum einen eine zweite
Anzahl von Knotenvorrichtungen an, die zuletzt am Speichern des Datensatzes
innerhalb der Datendatei beteiligt waren, und zum anderen, ob der Datensatz
partitionierte Daten umfasst (vgl. DE-T5, Absatz [0011] – Merkmale VS6 und VS7).
Eine Knotenvorrichtung ist in der Lage, eine Verarbeitungsaufgabe mit wenigstens
einem Datensatzteil auszuführen (vgl. DE-T5, Absatz [0011]).


Bei den folgenden Merkmalen wird die Partitionierung für den Fall, dass der
Datensatz partitionierte Daten aufweist (Merkmal VP), präzisiert.


Dementsprechend erfolgt eine Aufteilung der Daten eines Datensatzes in mehrere
Partitionen, wobei die Daten jeder Partition einer Knotenvorrichtung zugewiesen und
von dieser gemeinsam verarbeitet werden müssen. Um die Zuordnung zu der
Knotenvorrichtung      zu    gewährleisten,     ist   jeder   Partition   ein   eindeutiges
Partitionsetikett zugeordnet, von dem wiederum ein Hash-Wert (eine „gehashte
Kennung“) abgeleitet wird, der die Partition identifiziert (vgl. DE-T5, Absatz [0249] –
Merkmale VP1 bis VP3).


Weiter ist beansprucht, dass jeder Datenblock mindestens einen Datenunterblock
enthält, der Daten einer einzelnen Partition umfasst und einem einzelnen
Datensatzteil entspricht (vgl. DE-T5, Absatz [0261] – Merkmale VP4 bis VP6).


Zusätzlich   entspricht     jeder    der   Zuordnungskarteneinträge       einem   einzigen
Datenblock. Dabei enthält der Zuordnungskarteneintrag einen oder mehrere
Zuordnungskartenuntereinträge, von denen jeder einem einzelnen Datenunterblock

                                        - 13 -



entspricht. Jeder Zuordnungskartenuntereintrag enthält eine Datenunterblockgröße
und eine gehashte Kennung der Partition des entsprechenden Datenunterblocks
(vgl. DE-T5, Absatz [0206] – Merkmale VP7 bis VP10).


Im Folgenden (vgl. DE-T5, Fig.20A-20C, Absätze [0275]-[0284]) werden die Schritte
des Verfahrens, die durch die Prozessorkomponente einer Steuervorrichtung
durchgeführt werden, weiter konkretisiert (Merkmal VM).


Zu Beginn werden Angaben von mehreren Knotenvorrichtungen, welche für die
Ausführung einer Verarbeitungsaufgabe mit wenigstens einem Datensatzteil der
mehreren Datensatzteile verfügbar sind, empfangen – Merkmal VM1.


Weiter werden Metadaten und Zuordnungskartendaten von der einen oder den
mehreren Speichervorrichtungen über ein Netzwerk abgerufen – Merkmal VM2.


Wenn die Metadaten oder die Zuordnungskartendaten angeben, dass der Datensatz
partitionierte Daten umfasst (Merkmal VM3), wird eine erste Anzahl der verfügbaren
Knotenvorrichtungen aus den empfangenen Angaben bestimmt (Merkmal VM3.1).
Jeder der verfügbaren Knotenvorrichtungen wird ein Wert aus einer Reihe positiver
ganzzahliger Werte als ein Festlegungswert zugewiesen. Dabei erstreckt sich die
Reihe von 0 bis zu einem positiven ganzzahligen Wert, der gleich der ersten Anzahl
minus 1 ist (Merkmal VM3.2).
Als nächstes wird eine zweite Anzahl von Knotenvorrichtungen bestimmt (Merkmal
VM3.3). Die zweite Anzahl umfasst alle Knotenvorrichtungen, die zuletzt am
Speichern des Datensatzes innerhalb der Datendatei beteiligt waren (Absatz [0016]).
Anschließend werden die erste und die zweite Anzahl der Knotenvorrichtungen
dahingehend überprüft, ob eine Übereinstimmung vorliegt (VM3.4).


Sind alle Bedingungen erfüllt, d.h. der Datensatz umfasst partitionierte Daten und die
erste   und    die   zweite    Anzahl   stimmen     überein,   werden     für   jeden

                                     - 14 -



Zuordnungskarteneintrag der Zuordnungskartendaten die folgenden Schritte durch
die Prozessorkomponente ausgeführt (Merkmal VM3.5):
Aus einem einzigen Zuordnungskartenuntereintrag wird die gehashte Kennung für
einen einzigen Datenunterblock ermittelt (Merkmal a1)) und aus jedem
Zuordnungskartenuntereintrag wird die Datenunterblockgröße für jeden der Datenunterblöcke innerhalb des entsprechenden Datenblocks ermittelt (Merkmal a2)).
Anschließend wird für die Bereitstellung eines Zeigers eine Stelle des
entsprechenden Datenblocks innerhalb der Datendatei bestimmt (Merkmal b)).
Danach wird die gehashte Kennung durch die erste Anzahl der Knotenvorrichtungen
dividiert, um einen Modulo-Wert zu erhalten (Merkmal c)), und dieser Modulo-Wert
wird mit allen Werten, die den verfügbaren Knotenvorrichtungen zugewiesen worden
sind, auf Übereinstimmung verglichen, um eine verfügbare Knotenvorrichtung zu
ermitteln (Merkmal d)). An diese Knotenvorrichtung wird ein Zeiger übertragen
(Merkmal e)). Dabei umfasst der Zeiger eine Angabe zur Stelle des entsprechenden
Datenblocks (Merkmal e1)) und eine Summe der Datenunterblockgrößen aller
Datenunterblöcke innerhalb des entsprechenden Datenblocks (Merkmal e2)).


Im Ergebnis ermöglicht die beanspruchte Lehre eine Verbesserung des verteilten
Speicherns und Abrufens eines von mehreren Knotenvorrichtungen verarbeiteten
Datensatzes (vgl. DE-T5 Abs. [0073]), so dass ein großer Datensatz für eine
Verarbeitungsaufgabe, die auf mehrere Rechenknoten verteilt wird, partitioniert,
gespeichert und abgerufen werden kann, womit eine möglichst effektive
Verarbeitung der gespeicherten Datensätze möglich wird.


Als Fachmann, der mit der Aufgabe einer derartigen Verbesserung betraut wird,
sieht der Senat einen Informatiker mit Hochschulabschluss an, der über eine
mehrjährige Berufserfahrung auf dem Gebiet der Datenverarbeitung in verteilten
Rechen-Netzen – insbesondere auch unter dem Gesichtspunkt der koordinierten
Speicherung von Datensätzen in einem verteilten Speichersystem – verfügt.

                                      - 15 -



2.    Das geltende Patentbegehren ist zulässig. Die Patentansprüche und die
überarbeitete Beschreibung bleiben innerhalb des Rahmens der ursprünglichen
Offenbarung. Auch andere Mängel liegen nicht vor.


2.1   Die Änderungen, die in den in der Anmeldung enthaltenen Angaben
vorgenommen worden sind, erweitern den Gegenstand der Anmeldung nicht.


2.1.1 Der Senat hat die von der Anmelderin in der Beschwerdebegründung vom
29. Januar 2019 als (damaligen) Hauptantrag beanspruchte Anspruchsfassung (Ansprüche 1 bis 30, eingegangen am 18. Juli 2018) im Zwischenbescheid vom
17. Mai 2022 als mängelbehaftet angesehen, weil die unter Schutz zu stellende
Erfindung diesen Patentansprüchen nicht klar und deutlich entnehmbar war. Er hat
festgestellt, dass die Lehre der Anmeldung und insbesondere der damals geltenden
Patentansprüche an vielen Stellen ungenau, mehrdeutig oder teilweise auch gar
nicht im Detail nachvollziehbar ist. Im Zwischenbescheid wurden zahlreiche Fragen
dazu gestellt, wobei auf konkrete Unklarheiten und Widersprüche hingewiesen
wurde.


Denn im Patent-Erteilungsverfahren ist für Patentansprüche zu sorgen, die die unter
Schutz gestellte Erfindung klar und deutlich umschreiben (BGH GRUR 1988, 757 –
Düngerstreuer, Abschnitt V Absatz 3) und geeignet sind, den Anmeldungsgegenstand eindeutig zu kennzeichnen und vom Stand der Technik abzugrenzen
(BGH GRUR 1979, 461 – Farbbildröhre, II. 2d). Der Schutzbereich muss, ggf. unter
Auslegung mittels der Beschreibung, so klar und eindeutig definiert sein, dass er
„für Außenstehende hinreichend sicher vorhersehbar ist” (BGH GRUR 1989, 903 –
Batteriekastenschnur, III.2.). Die Beseitigung vermeidbarer Unklarheiten hat im
Prüfungsverfahren zu erfolgen (BGH GRUR 2013, 1210 – Dipeptidyl-Peptidase-Inhibitoren, III. 1a)). Diese Grundsätze gelten auch für die Erteilung im
Beschwerdeverfahren.

                                       - 16 -



Die Anmelderin hat daraufhin die Patentansprüche überarbeitet und eine neue
Anspruchsfassung vorgelegt.


Die vorliegende Patentanmeldung erfolgte in englischer Sprache. Als Ursprungsunterlagen sind die am Anmeldetag eingereichten englischsprachigen Unterlagen
anzusehen. Zum Beleg der ursprünglichen Offenbarung wird auf die ursprüngliche
Anmeldung (WO 2017) Bezug genommen.


2.1.2 Zum Hauptanspruch


Der geltende Hauptanspruch geht zurück auf den Claim 21 der WO 2017.


Die Merkmalsgruppe VS basiert auf dem Claim 21, den Fig. 12A-12C und den
Absätzen [0011], [0013], [0072], [0073], [00190]-[00195], [00204].


Die Merkmalsgruppe VP ergibt sich aus dem Claim 21 und den Absätzen [0021],
[0026], [0032], [0041], [0073], [0075], [0081], [00200], [00203], [00204], [00205],
[00247], [00259] sowie [00271].


Die Merkmalsgruppe VM ist aus dem Claim 21, den Figuren 20A-20C und den
Absätzen [00273]-[00282] zu entnehmen.


Den mit der Anmeldung ursprünglich formulierten Patentansprüchen kommt im
Rahmen des Erteilungsverfahrens keine eine weitergehende Offenbarung in der
Beschreibung einschränkende Bedeutung zu (BGH GRUR 2005, 1023 –
Einkaufswagen II). Vielmehr ist es (lediglich) erforderlich, dass der Fachmann die
im Anspruch bezeichnete technische Lehre den Ursprungsunterlagen unmittelbar
und eindeutig als mögliche Ausführungsform der Erfindung entnehmen kann; dabei
ist eine unangemessene Beschränkung des Anmelders bei der Ausschöpfung des
Offenbarungsgehalts der Anmeldung zu vermeiden (BGH GRUR 2015, 976 –
Einspritzventil, Rn 45).

                                       - 17 -



Zusammenfassend behebt die geltende Fassung des Anspruchs 1 Unstimmigkeiten
und Ungenauigkeiten der ursprünglichen Fassung, stellt letztlich aber nur eine
etwas andere Übersetzung der englischen Anspruchsfassung dar, ohne den
Schutzbereich inhaltlich zu verändern. Die ursprüngliche Offenbarung lässt sich, wie
ausgeführt, nachvollziehbar belegen.


2.1.3 Zu den Unteransprüchen 2 bis 10


Die Unteransprüche 2 bis 10 basieren auf den Claims 22 bis 30.


Damit ist auch für diese Patentansprüche die ursprüngliche Offenbarung gegeben.


2.1.4 Die Beschreibung wurde unter Berücksichtigung des entgegengehaltenen
Standes der Technik in zulässiger Weise daran angepasst. Insbesondere wurden
die ursprünglichen Figuren 1 bis 10 und die zugehörige Beschreibung gestrichen,
weil sie sich auf andere Aspekte des verteilten Speicherns beziehen.


2.2   Der Gegenstand des geltenden Patentanspruchs 1 ist durch den bekannt
gewordenen Stand der Technik weder vorweggenommen noch nahegelegt.


2.2.1 Im Prüfungsverfahren wurden entgegengehalten:


      D1     US 2011 / 0 099 351 A1
      D2     Intagly: „How Could I Have the Index of an Array 'Roll Over'
             When     Incrementing“,   Juli     2011,   im   Internet   <URL:
             https://stackoverflow.com/questions/6826826/how-could-ihave-the-index-of-an-array-roll-over-when-incrementing>


Die D1 betrifft ein Verfahren zur Deduplizierung von Daten in einem
Speichersystem. Dabei werden Werte berechnet, die den Inhalt der Daten
repräsentieren und jeweils als sogenanntes geometrisches Zentrum für einen
Knoten bezeichnet werden. Wenn eine Schreibanforderung empfangen wird, wird

                                            - 18 -



der   Knoten     für   das    Speichern     ausgewählt,   dessen     Daten   die   größte
Übereinstimmung mit bereits gespeicherten Daten aufweist. Damit soll das
Speichern von unnötigen Duplikaten von Daten über verschiedene Knoten im
Speichersystem hinweg vermieden werden (Absatz [0013]).
Bei dem Verfahren wird ein Block („chunk“) in mehrere Datensegmente unterteilt
(Absätze [0014], [0067]-[0069] – Merkmal VS1).
Zum Auffinden der Segmente wird eine clusterweite Datenbank verwendet (Absätze
[0072]-[0074]). Weiter ist in diesen Absätzen die Organisation der Daten, das
Speichern in einer Datendatei, sowie die Verwendung von Einträgen für die
Adressierung gezeigt – Merkmale VS2 bis VS5 und VM2).
Schließlich ist beschrieben, dass ein Knoten, dessen gespeicherte Datenmenge
sich der physischen Grenze des Speichers nähert, nicht mehr für die Speicherung
verwendet      wird,   d.h.   es   findet    eine    Prüfung   der   Verfügbarkeit   von
Knotenvorrichtungen statt (Absatz [0065] – Merkmale VM und VM1).
Aus der Druckschrift ist jedoch nicht zu entnehmen, dass die Einträge eine Angabe
über die zuletzt für das Speichern verwendeten Knoten enthalten. Somit ist das
Merkmal VS6 nicht gezeigt.
Der Begriff „Partition“ ist nur in Absatz [0020] der D1 zu finden, bezieht sich aber
auf die Verteilung der Datenblöcke über die Knoten des Speicherclusters.
Partitionen i. S. d. Anspruchs 1, die jeweils einer Knotenvorrichtung zugewiesen
werden müssen, gehen nicht aus der Druckschrift hervor. Sonach ist die
Merkmalsgruppe VP nicht gezeigt.
Das gleiche gilt auch für die Merkmale VS7 und VM3 bis VM3.5 e2), die ebenfalls
auf dem Vorliegen partitionierter Daten basieren.


Die Druckschrift D2 zeigt einen Blog-Eintrag aus dem Jahr 2011 („asked Jul 26,
2011 at 7:45 - user avatar: intagli“). Auf die Frage eines Programmierers: „So I have
an Array with the length of 4. When I increment it by 1 and the number gets bigger
than the length of the array, I'd like it to rollover“ wird ihm der „Modulo-Operator“
vorgeschlagen: „You can use the modulo operator: current_index = (current_index
+ n) % 4;“. Insofern belegt diese Druckschrift lediglich, dass ein Programmierer die

                                        - 19 -



Modulo-Funktion und ihre Anwendung, um einen Index beim Hochzählen innerhalb
des Bereichs der Array-Größe zu halten, kannte. Weitere Einzelheiten zu der
beanspruchten Speicherung und Verarbeitung partitionierter Daten fehlen. In Bezug
auf den neuen Patentanspruch 1 sind der Druckschrift somit allenfalls Teile der
Merkmale VM3.5c) bis VM3.5e) zu entnehmen.


2.2.2 Mit dem Zwischenbescheid vom 17. Mai 2022 hat der Senat nachträglich
noch die folgenden Druckschriften ins Verfahren eingeführt:


      D3     US 2015 / 0 134 796 A1
      D4     US 2004 / 0 015 478 A1


Die Druckschrift D3 betrifft die dynamische Partitionierung von Datenströmen (vgl.
Titel). Der Datenstrom besteht aus einer Folge von Datensätzen („data records“,
vgl. Absatz [0054]). Zur Speicherung der Stream-Datensätze ist angegeben, dass
hierfür Richtlinien vorgegeben werden, welche bspw. Sequenznummern (für die
einzelnen Datensätze) beinhalten können, die Bestandteil des Datensatzes sind
(vgl. Absätze [0044], [0054], [0100]). Ausgeführt wird die Speicherung durch ein
Stream-Management-System (SMS), welches u.a. ein „SMS control subsystem“
und ein „storage subsystem“ für die Durchführung des Speichervorgangs umfasst
(vgl. Absatz [0058]). Jedes SMS kann einen oder mehrere Knoten oder
Komponenten umfassen, die Datensätze basierend auf den Richtlinien empfangen
und an das SMS-Subsystem zum Speichern weiterleiten, wobei mehrere
Verarbeitungsvorgänge an den Datensätzen auch gleichzeitig, d.h. parallel
durchgeführt werden können (vgl. Absatz [0058]). Für die Speicherung der
Datensätze kann der Sender („data producer“) einen expliziten Partitionsschlüssel
angeben, es kann aber auch ein Partitionsschema oder eine Hash-Funktion
verwendet werden (vgl. Absatz [0071]). Bei der Verwendung einer Hash-Funktion
erfolgt eine Unterteilung in Bereiche positiver Zahlen, von denen jeder einen
Teilbereich einer Partition kennzeichnet (vgl. Absätze [0071], [0107]). Weiter ist die
Möglichkeit beschrieben, dass ein Knoten eines SMS-Subsystems derart

                                      - 20 -



konfiguriert ist, dass er Datensätze von mehr als einer Partition verarbeitet (vgl.
Absatz [0072]). Ebenso können Datensätze einer Partition von mehr als einem
Knoten gespeichert werden (vgl. Absatz [0072]). Zudem wird auch der Abruf von
gespeicherten Datensätzen anhand von Sequenznummern angesprochen (vgl.
Absätze [0099] bis [0104] i. V. m. Figuren 13 und 14; s. auch Absätze [0082] bis
[0084] sowie Figur 8). Schließlich ist als Beispiel die Ausführung von sogenannten
„Big Data-Anwendungen“ angegeben (vgl. Absatz [0168]).


Hinsichtlich des neuen Anspruchs 1 sind demnach einzelne Elemente bei einer
isolierten Betrachtung wie bspw. die Organisation von Daten (Merkmal VS2), das
Halten bzw. Speichern eines Datensatzes in einer Datendatei (Merkmal VS3), die
Organisation der Daten in Partitionen, deren Verarbeitung sowie die Vorgabe eines
Partitionierungsetiketts (Merkmal VP1, teilweise Merkmale VP2 und VP3) und die
Speicherung auf Basis einer Hash-Funktion (Merkmal VM3.5a1)) in der Druckschrift
D3 gezeigt.


Aus den Absätzen [0072] und [0086] sowie Fig.15 ist eine Zuordnung von Knoten
zu den zu speichernden Partitionen zu entnehmen. Eine Unterscheidung zwischen
ersten und zweiten Knotenvorrichtungen, die insbesondere darauf beruht, welche
Knotenvorrichtungen zuletzt am Speichern beteiligt waren, geht aus der Druckschrift
nicht hervor. Somit sind zumindest die Merkmale VS6 sowie VM3.1 bis VM3.5
nicht zu entnehmen.


In der Druckschrift D4 ist eine Datenbank-Struktur beschrieben, die einen
besonderen Index für einen einfacheren Zugriff auf die Elemente der Datenbank
aufweist. Gemäß den Absätzen [00134] bis [0139] werden Hash-Funktionen benutzt, um den Offset, d.h. die Position eines Elementes K in einem Array mit N Elementen zu bestimmen. Demnach waren derartige Berechnungen und insbes. die
Nutzung der „Modulo“-Funktion für eine bestimmte, begrenzte Anzahl von
Elementen (= Array) dem Fachmann hinlänglich bekannt. Neben der Verwendung
einer „Hash-Funktion“ entnimmt der Fachmann jedoch allenfalls die Merkmale VS1

                                            - 21 -



bis VS4 sowie VP und VP1 des Anspruchs 1 aus der Druckschrift D4 (vgl. Absätze
[0268] bis [0273] i. V. m. Figur 23).


2.2.3 Demnach nimmt keine der in Betracht gezogenen Druckschriften die Lehre
des geltenden Patentanspruchs 1 vorweg, und es sind auch keine Anregungen
erkennbar, die in naheliegender Weise zu dieser Lehre führen würden.


3.      Der geltende Patentanspruch 1 ist sonach gewährbar. Seine Unteransprüche 2 bis 10 sind ebenfalls gewährbar.


Das Patent war daher so wie nunmehr beantragt zu erteilen.




                                  Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
        Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
        Befangenheit mit Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern
        er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt
        hat,
     5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
        Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder

                                        - 22 -



   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe durch eine beim Bundesgerichtshof
zugelassene Rechtsanwältin oder durch einen beim Bundesgerichtshof zugelassenen
Rechtsanwalt einzulegen.




 Dr. Morawek               Hoffmann                   Akintche           Dr. Städele
