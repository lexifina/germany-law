---
ecli: "ECLI:DE:BPatG:2005:181005B17Wpat67.03.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 67/03"
decided: "2005-10-18"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2005&Sort=1&Seite=102&nr=18461&anz=1972&pos=1535&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2005-10-18_17_W-pat_67_03_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 67/03 vom 2005-10-18

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 67/03                                                  Verkündet am
 _______________                                                  18. Oktober 2005
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 197 23 908.0-55


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 18. Oktober 2005 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch sowie der Richterin Eder, des Richters
Dipl.-Ing. Schuster und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
08.05

                                     -2-



beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 11 B des Deutschen Patent- und Markenamts vom 24. April 2003 aufgehoben und die Sache zur weiteren
        Prüfung und Entscheidung an das Deutsche Patent- und
        Markenamt zurückverwiesen.


                                  Gründe


                                      I.


Die vorliegende Patentanmeldung ist am 6. Juni 1997 beim Deutschen Patentund Markenamt unter Beanspruchung der Priorität 24447/1996 der Republik
Korea vom 27. Juni 1996 unter der Bezeichnung


        „Automatische Servoadressmarkierungserkennung und Servozeitgebungskompensationsschaltung“


angemeldet worden.


Sie wurde von der Prüfungsstelle für Klasse G 11 B des Deutschen Patent- und
Markenamts durch Beschluss vom 24. April 2003 mit der Begründung zurückgewiesen, dass die in den ursprünglichen Unterlagen angegebene Wirkungsweise
des Anmeldungsgegenstands für einen Fachmann nicht ausreichend deutlich und
vollständig offenbart sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.

                                        -3-



Sie beantragt, den angefochtenen Beschluss aufzuheben und das nachgesuchte
Patent mit folgenden Unterlagen zu erteilen:


      -     Patentanspruch 1, überreicht in der mündlichen Verhandlung,
      -     noch anzupassende Patentansprüche 2 bis 12 vom 5. Februar 2004,
      -     15 Seiten Beschreibung vom Anmeldetag, und
      -     8 Blatt Zeichnungen mit 8 Figuren vom 28. August 1997.


In der Beschwerdebegründung führt die Anmelderin im Einzelnen aus, warum ihrer Meinung nach die Wirkungsweise des Anmeldungsgegenstandes in den Anmeldungsunterlagen für einen Fachmann deutlich und vollständig offenbart ist.


Von der Prüfungsstelle wurden keine Druckschriften in das Verfahren eingeführt.


Der geltende Patentanspruch 1 in der am 18. Oktober 2005 eingereichten Fassung lautet:


          „1.   Schaltung für ein Plattenlaufwerk zum automatischen Erkennen einer Servoadressmarkierung, SAM, innerhalb eines Servosektors auf einer Spur einer Platte und zum Kompensieren einer
          Servozeitgebung, wenn die SAM nicht erkannt wurde, wobei die
          Schaltung umfasst:


          eine Steuerung (22) zum Steuern des Plattenlaufwerks einschließlich der Erkennung von Servo- und Dateninformation in Synchronisation mit der Erkennung der SAM;


          einen SAM-Detektor (16) zum Erkennen der SAM aus Daten, die
          von der Platte gelesen wurden, und zum Erzeugen eines SAM-Detektionssignals (SDO) aus der erkannten SAM;

                                        -4-



       eine    Servozeitgebungskompensationseinheit (31)       mit   einem
       Hauptzähler (34), der in Antwort auf das SAM-Detektionssignal (SDO) Systemtakte (SCLK) zählt, und mit einem Datensektorendpulsgenerator (20) zum Erzeugen eines Datensektorenpulses (ENDS),    der   das      Ende   eines   dem     Servosektor
       nachfolgenden Datensektors und den Anfang eines neuen
       Servosektors anzeigt, wenn nach dem Erkennen des SAM-Detektionssignals (SDO) eine von der Steuerung (22) vorgegebene Anzahl von Systemtakten gezählt wurde;


       eine SAM-Erkennungsfenstererzeugungsschaltung (36) zum Erzeugen eines SAM-Erkennungsverfehlungssignals (A) und eines
       Zählsteuersignals (B), wenn die SAM innerhalb eines Bereichs eines SAM-Fensters (SAMW) eines bestimmten Servosektors nicht
       erkannt wurde;


       wobei der Hauptzähler (34) durch das SAM-Erkennungsverfehlungssignal (A) gestartet wird, wenn die SAM nicht innerhalb des
       Bereichs des SAM-Fensters (SAMW) erkannt wurde;


       wobei   der   Hauptzähler (34)    weiterhin   einen   Zählsteuereingang (LDB) zum Empfangen des Zählsteuersignals (B) aufweist,
       so dass er, wenn die SAM nicht innerhalb des Bereichs des SAM-Fensters (SAMW) erkannt wurde, zum Kompensieren der Verzögerung der Servozeitgebung die Systemtakte (SCLK) mit einem
       Zählwert (LD), der von der Steuerung (22) geladen wurde, zählt.“


Der Erfindung soll die Aufgabe zugrunde liegen, ein verbessertes Festplattenlaufwerk und eine verbesserte Schaltung zur automatischen Erkennung einer Servoadressmarkierung, die in einem Servosektor enthalten ist, anzugeben, bei der eine
Überlast aufgrund einer fehlenden Servoadressmarkierungserkennung vermieden

                                        -5-



werden kann und bei der eine Servozeitgebungsverzögerung infolge der nicht erkannten Servoadressmarkierung kompensiert werden kann.


Wegen der weiteren Einzelheiten des Sachverhalts wird auf den Akteninhalt verwiesen.


                                        II.


Die frist- und formgerecht eingelegte Beschwerde ist zulässig. Sie ist auch begründet, da die der Anmeldung zu entnehmende Lehre in den ursprünglichen Unterlagen so deutlich und vollständig offenbart ist, dass ein Fachmann sie ausführen
kann (§ 34 Abs 4 PatG).


Wie in der Anmeldung auf Seiten 1 und 2 sowie in Figur 1 mit der zugehörigen
Beschreibung erläutert ist, weist in einem Plattenlaufwerk jede Spur einer (zu beschreibenden oder zu lesenden) Platte Servo- und Datensektoren auf, die abwechselnd hintereinander angeordnet sind. Der Servosektor enthält jeweils die
Informationen, die zur Steuerung des Lese-/Schreibkopfes beim Zugriff auf den
nachfolgenden Datensektor nötig sind.
Am Beginn jedes Servosektors ist eine Servoadressmarkierung SAM mit einem
charakteristischen Muster aufgezeichnet. Diese SAM wird während des Betriebs
des Plattenlaufwerks jeweils erkannt. In Synchronisation mit der SAM-Erkennung
gibt die Steuerung verschiedene Fenstersignale für die Abtastung von Servo- und
Dateninformationsblöcken aus. Unter anderem wird nach Ablauf einer auf die
SAM-Erkennung folgenden, getakteten Zeitspanne ein Sektorendesignal ENDS
erzeugt, welches das Ende des zum Servosektor gehörigen Datensektors und den
Anfang des nächsten Servosektors anzeigt. Danach wird die SAM des nächsten
Datensektors erkannt usw.
Beim in der Anmeldung beschriebenen Stand der Technik ergibt sich das Problem,
dass die SAM-Suche für jeden Servosektor jeder Spur durchgeführt werden muss.
Wenn die SAM eines Servosektors nicht erkannt wird, werden alle weiteren Ab-

                                      -6-



läufe gesperrt und die SAM-Suche für den relevanten Servosektor neu gestartet.
Wenn sich solche Fehl-Erkennungen häufen, führt das zu einer Überlastung des
Plattenlaufwerks.


Um dieses Problem zu lösen, wird in der Anmeldung vorgeschlagen, im Falle einer
nicht erkannten SAM ein SAM-Erkennungsverfehlungssignal A zu erzeugen, dieses anstelle eines SAM-Detektionssignals SDO in die Steuerung einzugeben und
damit den üblichen Betriebsablauf ohne Unterbrechung weiterlaufen zu lassen, vgl
Figur 2 bis 4 mit Beschreibung. Auch wenn ein A-Signal anstelle eines SAM-Erkennungssignals erzeugt wurde, sollen die üblichen Fenstersignale, insbesondere das Sektorendesignal ENDS generiert werden, was normalerweise durch
Zählung der Zeittakte ab SAM-Erkennung (hier: A-Erzeugung) und Vergleich mit
vorgegebenen Werten geschieht. Da die SAM innerhalb einer bestimmten Zeitspanne (SAM-Fenster SAMW) erwartet wird und erst nach Ablauf dieser Zeitspanne (im Falle der Nichterkennung) das A-Signal erzeugt wird, gibt es eine Verzögerung zwischen dem Start der Zeitzählung im Fall einer erkannten SAM und im
Fall eines erzeugten A-Signals, wenn die SAM nicht erkannt wurde, vgl hierzu in
Figur 7 den zeitlichen Verlauf der Signale SDO und A. Diese Zeitverzögerung soll
bei der Zeitzählung zumindest teilweise kompensiert werden, vgl Beschreibung
Seite 3 vorletzter Absatz sowie Figur 2 mit der Beschreibung auf Seite 5 letzter
Absatz und Seite 6 erster Absatz.


Zur Durchführung des oben dargelegten Ablaufs sind verschiedene Steuerungseinheiten vorgesehen, die in Figur 2 mit Beschreibung gezeigt sind, insbesondere:


  -   eine Steuerung (CPU 22) für das Plattenlaufwerk,
  -   ein SAM-Detektor (16), der wenn möglich die SAM erkennt und dann ein
      SAM-Detektionssignal SDO ausgibt,
  -   eine Servozeitgebungskompensationseinheit (31), die die Zeitzählung in einem Hauptzähler (34) in Synchronisation mit der SAM-Erkennung bzw der
      Erzeugung des SAM-Erkennungsverfehlungssignals A vornimmt, dabei die

                                      -7-



      oben erläuterte Zeitverzögerung kompensiert und ein ENDS-Signal ausgibt,
      vgl auch die Beschreibung auf Seite 6 letzter Absatz sowie Fig 3A und 3B,
  -   eine SAM-Erkennungsfenstererzeugungsschaltung (36), die nach ergebnislosem Ablauf der mit dem ENDS-Signal beginnenden, für die SAM-Erkennung    vorgesehenen    Zeitspanne   (Servoadressmarkierungsfenster
      SAMW) ein Erkennungsverfehlungssignal A und ein die Zählzeitkompensation im Hauptzähler (34) beeinflussendes Zählsteuersignal B abgibt, vgl
      Fig 4 mit Beschreibung.


Der von der Prüfungsstelle beanstandete Offenbarungsmangel wurde im
Beschwerdeverfahren dadurch geheilt, dass nunmehr wieder die ursprünglichen
Figuren A und 4 und die ursprüngliche Beschreibung gelten sollen. Die Anmelderin
hat ausgeführt, dass die in den ursprünglichen Figuren 3A und 4 dargestellten
Schaltungen tatsächlich funktionieren. Dies habe die physikalische Ursache, dass
jedes logische Gatter eine Zeitverzögerung der durchlaufenden Signale von einigen Nanosekunden verursache. Die in der Schaltung gemäß Figur 3A vorhandenen Inverter und UND-Gatter führten zu Laufzeitverzögerungen. Dadurch werde
das D-Flipflop (50) nicht sofort nach dem Setzen des ENDS-Signals zurückgesetzt, sondern erst mit einer gewissen Verzögerung, wie sie in jeder logischen
Schaltung zu beobachten sei. Die Verzögerung zwischen dem Ausgangssignal
des D-Flipflops (50) und dem Systemtakt erlaube es, dass das ENDS-Signal am
Ausgang des D-Flipflops (56) auf einen niedrigen Wert zurückkehrt. Ähnliches
gelte für das Erkennungsverfehlungssignal A in der Schaltung gemäß Figur 4.


Dass durch das Durchlaufen der logischen Gatter die erforderliche Zeitverzögerung bewirkt wird, ist Realität. Bereits eine Verzögerung im Bereich weniger
Taktlängen zwischen dem Systemtaktsignal SCLK, das in der Schaltung gemäß
Fig 3A bzw 4 das Hochsetzen des ENDS-Signals im Flipflop (56) bzw des A-Signals im Flipflop (68) bewirkt, und dem Ausgangssignal des D-Flipflops (50) in
Fig 3A bzw (60) in Fig 4 nach dessen Rücksetzen reicht aus, um noch so viele

                                       -8-



Systemtakte durch das UND-Gatter (A2) bzw (A4) passieren zu lassen, dass das
ENDS-Signal bzw das A-Signal zurückgesetzt wird.


Der von der Prüfungsstelle beanstandete Offenbarungsmangel wurde damit im
Beschwerdeverfahren ausgeräumt. Die der Anmeldung zu entnehmende Lehre ist
in den ursprünglichen Unterlagen so deutlich und vollständig offenbart, dass ein
Fachmann sie ausführen kann.


Zum geltenden Patentanspruch:


Der geltende Patentanspruch 1 ist zulässig.
Er ist gestützt durch die ursprünglichen Ansprüche 1 bis 3, die ursprüngliche Beschreibung auf Seiten 1 und 2 sowie die ursprünglichen Figuren 1 bis 4 und 7 mit
den zugehörigen Beschreibungsteilen. Insbesondere geht die Kompensation der
Verzögerung der Servozeitgebung (im Falle der SAM-Nichterkennung) durch
Empfangen des Zählsteuersignals B im Hauptzähler (34) und Zählen mit einem
Zählwert (LD) aus Fig 2, 3 und 4 in Verbindung mit der Beschreibung hervor; die
Funktion des Zählwerts (LD) ist auf Seite 8 Zeilen 31 bis 35, Seite 10 Zeilen 13 bis
22, Seite 14 Zeilen 23 bis 27 sowie in dem ursprünglichen Anspruch 7 offenbart.
Bei Eingabe des Zählsteuersignals B in den Hauptzähler beginnt demnach die
Zählung nicht beim üblichen Wert (wie bei der durch die SAM-Erkennung getriggerten Zählung), sondern bei einem anderen, durch LD bestimmten Wert, der ein
„Vorwärtsspringen“ des Zeitzählers und damit eine zumindest teilweise Kompensation der Verzögerung der Servozeitgebung im Fall der SAM-Nichterkennung
bewirkt.


Mit der im Beschwerdeverfahren erfolgten Klärung bezüglich der Ausführbarkeit
der in der Patentanmeldung dargelegten Lehre gemäß § 34 Abs 4 PatG ist die
Grundlage für den Beschluss der Prüfungsstelle entfallen.
Da die vollständige Prüfung der Patentanmeldung und die dazu erforderliche Ermittlung des Standes der Technik noch aussteht und es regelmäßig geboten ist,

                                       -9-



dies dem Patentamt zu überlassen (vgl Schulte, Patentgesetz, 7. Aufl, § 79
Rdn 20 f mwN; Benkard, Patengesetz, 9. Aufl, § 79 Rdn 27; BPatG in BlPMZ 75,
325), war die Sache zur Durchführung der Prüfung und zur erneuten Entscheidung
gemäß § 79 Abs 3 Satz 1 PatG an das Deutsche Patent- und Markenamt zurückzuverweisen. Aus diesem Grund konnte auch auf die Anpassung der Unteransprüche und der Beschreibung im Beschwerdeverfahren verzichtet werden.


Für die weitere Prüfung einschließlich der evtl Formulierung von Unteransprüchen
wird auf Folgendes hingewiesen:


Weitere wichtige Elemente der Patentanmeldung stellen die in den Figuren 2, 5
und 6 mit Beschreibung dargestellten Einheiten SAM-Erkennungsverfehlungssignalzähler (38) und SAM-Suchmodussteuerung (40) dar. Die deutliche Offenbarung   von   deren   Wirkungsweise     hat   die   Prüfungsstelle   im   bisherigen
Prüfungsverfahren ebenfalls in Frage gestellt.
Zur Wirkungsweise des SAM-Erkennungsverfehlungssignalzählers und der SAM-Suchmodussteuerung ist den ursprünglichen Unterlagen, insbesondere den Figuren 5 und 6 sowie der Beschreibung auf Seite 10 letzter Absatz und Seite 11 erster
Absatz Folgendes zu entnehmen:
In der Schaltung des Erkennungsverfehlungssignalzählers gemäß Fig 5 wird das
SCH2-Signal nach dem erstmaligen Verfehlen der SAM-Erkennung (erster Puls
des Erkennungsverfehlungssignals A) hochgesetzt, SCH3 wird durch den zweiten
A-Puls hochgesetzt, SCH4 wird durch den dritten A-Puls hochgesetzt, und SCH5
wird durch den vierten A-Puls hochgesetzt (das Umschalten jedes D-Flipflops erfolgt nur an der ansteigenden Flanke des am Takteingang CK anliegenden Signals). Entsprechend werden die zu den SCH2- bis SCH5-Signalen invertierten
Signale PSAM2 bis PSAM5 niedrig gesetzt. In der Schaltung der SAM-Suchmodussteuerung gemäß Fig 6 werden durch die Auswahlsignale (SEL0,
SEL1) in den Multiplexern MUXA und MUXB eines der PSAM-Signale (aus
PSAM2 bis PSAM5) und das dazugehörige, zum PSAM-Signal invertierte SCH-Signal ausgewählt und mit dem nächsten A-Puls über die D-Flipflops (82 und 84)

                                      - 10 -



ausgegeben. Solange das ausgewählte SCH-Signal niedrig ist, kann der übliche
Betriebsablauf mit Servozeitgebungskompensation durchgeführt werden. Wenn
das ausgewählte SCH-Signal hoch ist, wird durch das invertierte SCHB-Signal der
Hauptzähler (34) zurückgesetzt (vgl Fig 3 sowie Beschreibungsseite 15 Zeilen 10
und 11) und durch das SCH-Signal die SAM-Suche gestartet, bis die SAM erkannt
wird (vgl Fig 2 und Beschreibungsseite 7 Zeilen 26 bis 31). In der SAM-Suchmodussteuerung wird folglich durch die Auswahlsignale (SEL0, SEL1) ausgewählt, nach wie vielen SAM-Fehl-Erkennungen der Hauptzähler zurückgesetzt und
eine (zur SAM-Erkennung führende) SAM-Suche gestartet wird. Auch die missverständliche Formulierung auf Seite 14 letzter Satz bis Seite 15 erster Absatz
("Wenn die CPU 22 sequentiell angibt, dass die SAM fünfmal nicht erkannt wurde,
unter Verwendung der Auswahlsignale SEL0 und SEL1,...") ist in diesem Sinne zu
interpretieren.
Wenn somit in der SAM-Suchmodussteuerung (40) festgestellt wird, dass die im
SAM-Erkennungsverfehlungssignalzähler (38) gezählte Anzahl der aufeinanderfolgenden Servosektoren, in denen die SAM nicht erkannt wurde, einen bestimmten, durch die Auswahlsignale (SEL0, SEL1) vorgegebenen Wert überschreitet,
wird der Hauptzähler zurückgesetzt und die SAM-Suche so lange wiederholt, bis
die nächste SAM erkannt wird.
Auf eine derartige Ausgestaltung könnten Unteransprüche gerichtet werden.




Dr. Fritsch           Dr. Thum-Rung            Schuster                     Eder




                                                                            WA
