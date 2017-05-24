---
ecli: "ECLI:DE:BPatG:2017:240517B18Wpat1.15.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 1/15"
decided: "2017-05-24"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=24&nr=29145&anz=809&pos=365&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-05-24_18_W-pat_1_15_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0038.md", "germany/bund/acts/patg/0048.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 18 W (pat) 1/15 vom 2017-05-24

## Entscheidung

BUNDESPATENTGERICHT


  18 W (pat) 1/15                                                    Verkündet am
_______________                                                      24. Mai 2017
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 11 2004 000 626.0-53


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 24. Mai 2017 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, die Richterin Dipl.-Phys. Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater




BPatG 154
05.11

                                       -2-



beschlossen:


   1. Die Beschwerde wird zurückgewiesen.

   2. Die Rückzahlung der Beschwerdegebühr wird angeordnet.




                                    Gründe


                                        I.



Die vorliegende Patentanmeldung 11 2004 000 626.0 geht hervor aus einer PCT-Anmeldung (veröffentlicht als WO 2004/095275 A2), die am 21. April 2004 unter
Inanspruchnahme einer US-amerikanischen Priorität eingereicht worden ist, und
trägt die Bezeichnung


                        „Verfahren und Gerät zur Schaffung einer
                     Programmlauf- bzw. Ausführungsabschirmung“.


Die Patentanmeldung wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts mit Beschluss vom 24. November 2014 aus Gründen des Bescheids vom 9. Oktober 2014 gemäß § 48 PatG zurückgewiesen, wobei die Prüfungsstelle im Bescheid vom 9. Oktober 2014 u. a. ausgeführt hatte, die
Zulässigkeit des Anspruchs 1 könne nicht nachvollzogen werden und der technische Gehalt des beanspruchten Verfahrens ergebe sich aus dem Grundwissen
des Fachmanns. Zum Beleg des fachmännischen Grundwissens wurde auf
Druckschrift


               D3: IA-32 Intel Architecture Software Developer's Manual.
                   Volume 3: System Programming Guide. Order Number
                   245472. 2001, Intel, USA, Seiten 3-1 bis 3-28

                                       -3-



verwiesen. Im Prüfungsverfahren sind außerdem noch folgende Druckschriften
berücksichtigt worden:


              D1: Future direction of PaX – pax-future.txt, 26.1.2003. URL:
                   http://pageexec.virtualave.net/docs/pax-future.txt archiviert
                   durch: URL: http://www.archive.org am 22.02.2003, 7 Seiten
              D2: US 5 701 448 A


Gegen den oben genannten Beschluss richtet sich die Beschwerde der Anmelderin.


Mit Ladungszusatz zur mündlichen Verhandlung vom 10. April 2017 ist die Anmelderin unter anderem darauf hingewiesen worden, dass der geltende Patentanspruch 1 möglicherweise unzulässige Erweiterungen aufweist.


In der mündlichen Verhandlung begehrt die Anmelderin die Erteilung des Patents
mit einer Anspruchsfassung gemäß Hauptantrag sowie geänderten Anspruchsfassungen gemäß den Hilfsanträgen 1 und 2.


Die Beschwerdeführerin beantragt:


       1. den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
          Patent- und Markenamts vom 24. November 2014 aufzuheben und
          das Patent auf der Grundlage der folgenden Unterlagen zu erteilen:


         - Patentansprüche 1 bis 13, eingegangen am 3. Juni 2015,
          hilfsweise gemäß Hilfsantrag 1
          Patentansprüche 1 bis 13, eingereicht in der mündlichen Verhandlung,
          hilfsweise gemäß Hilfsantrag 2
          Patentansprüche 1 bis 13, eingereicht in der mündlichen Verhandlung,

                                        -4-



          -   Beschreibung Seiten 1 bis 20,
          -   Figuren 1 bis 7,
          jeweils eingegangen am 11. Oktober 2005,


     2. die Rückzahlung der Beschwerdegebühr anzuordnen.



Der seitens des Senats mit einer Gliederung versehene Anspruch 1 nach
Hauptantrag entspricht dem zum Zeitpunkt des Zurückweisungsbeschlusses
geltenden Anspruch 1 und lautet:


     M1       „Verfahren zum Sichern des Betriebs eines Befehlsausführungssystems, wobei das Verfahren folgende Schritte aufweist, die durch ein
              Betriebssystem ausgeführt werden:

     M2       Aufrufen (302) des Betriebssystemkerns (702) durch einen Task zum
              Ausführen einer Speicherabbildung (705);

     M3       Zuordnen (308; 402) eines virtuellen Speicherbereichs, welcher
              keine aktiven Abbildungen zu Daten oder zu einem ausführbaren
              Code aufweist und welcher mit dem Task verbunden ist, zu einem
              Adressraum eines virtuellen Speicherraums (704),

     M3.1     wobei der Adressraum die niedrigstmögliche Adresse besitzt;

     M4       Ermitteln der Endadresse des virtuellen Speicherbereichs im Adressraum;

     M5       Vergleichen (408) der ermittelten Endadresse mit einem aktuellen
              dynamischen Codesegment-Grenzwert; und

     M6       falls der aktuelle dynamische Codesegment-Grenzwert kleiner als die
              ermittelte Endadresse ist, Setzen (410) des dynamischen Codesegment-Grenzwerts, so dass der Codesegment-Grenzwert gleich der
              ermittelten Endadresse für den Task ist.“

                                         -5-



Der seitens des Senats mit einer Gliederung versehene Anspruch 1 nach Hilfsantrag 1 lautet (Änderungen gegenüber dem Anspruch 1 nach Hauptantrag hervorgehoben):


    M1         „Verfahren zum Sichern des Betriebs eines Befehlsausführungssystems, wobei das Verfahren folgende Schritte aufweist, die durch ein
               Betriebssystem ausgeführt werden:

    M2*        Aufrufen (302) des Betriebssystemkerns (702) durch einen Task zum
               Ausführen einer Speicherabbildung (705) durch eine Anwendung mit
               mehreren Tasks;

    M3*        Zuordnen (308; 402) eines virtuellen Speicherbereichs von virtuellen
               Speicherregionen, welche mit den Tasks verbunden sind, zu Adressräumen in einem Loch eines virtuellen Speicherraums, welchesr
               keine aktiven Abbildungen zu Daten oder zu einem ausführbaren
               Code aufweist und welcher mit dem Task verbunden ist, zu einem
               Adressraum eines virtuellen Speicherraums (704),

    M3.1* wobei der die Adressräaume die niedrigstmöglichen Adressen besitzent;

    M4*        Ermitteln, für jeden der Tasks, der Endadresse ders virtuellen
               Speicherregionbereichs im Adressraum;

    M5         Vergleichen (408) der ermittelten Endadresse mit einem aktuellen
               dynamischen Codesegment-Grenzwert; und

    M6         falls der aktuelle dynamische Codesegment-Grenzwert kleiner als die
               ermittelte Endadresse ist, Setzen (410) des dynamischen Codesegment-Grenzwerts, so dass der Codesegment-Grenzwert gleich der
               ermittelten Endadresse für den Task ist.“

                                      -6-



Der Patentanspruch 1 nach Hilfsantrag 2 entspricht dem Anspruch 1 nach
Hilfsantrag 1 unter Anfügung des folgenden Merkmals:


     M7      „Fortsetzen der Verarbeitung unter Verwendung einer Programmlaufabschirmung, welche auf dem Codesegment-Grenzwert basiert.“


Wegen der nach Hauptantrag und nach den Hilfsanträgen 1 und 2 geltenden jeweiligen nebengeordneten Ansprüche 9 und 13 sowie der jeweiligen abhängigen
Ansprüche 2 bis 8 und 10 bis 12 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht hierzu geltend, dass die geltenden Ansprüche jeweils zulässig seien, die Gegenstände der geltenden Ansprüche nicht unter den
Ausschlusstatbestand gemäß §1 Abs. 3 Nr. 3 i. V. m. Abs. 4 PatG fielen und neu
und erfinderisch seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                       II.



Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn der Gegenstand
des jeweiligen Anspruchs 1 nach Hauptantrag und nach den Hilfsanträgen 1 und 2
wurde gegenüber dem Inhalt der Anmeldung in der ursprünglich eingereichten
Fassung unzulässig erweitert (§ 38 Satz 1 PatG). Ob die Gegenstände der geltenden Ansprüche im Hinblick auf die §§ 1 bis 5 PatG patentfähig sind, kann somit
dahingestellt bleiben.




1.    Die Patentanmeldung betrifft ein Verfahren und ein Gerät zur Schaffung
einer Programmlauf- bzw. Ausführungsabschirmung (vgl. Bezeichnung der An-

                                       -7-



meldung). Stapelspeicherüberschreitungen, Datenzeiger- oder Pufferüberläufe
stellten in einigen Bearbeitungsplattformen eine gut bekannte Sicherheitsverletzbarkeit dar (vgl. geltende Beschreibung, S. 1, Z. 12 - 24). Da Daten und auch
Code, welche gespeichert und wiederhergestellt würden, sich konstant veränderten, könne ein Bereich des Speichers manchmal mit einem Code überschrieben
werden, ohne dass dies eine sofortige Auswirkung für die Aufgabe beinhalte; ein
Problem, das bei Plattformen, welche ohne Ausführbits in den Seitentabellen arbeiten, verschärft werde. Es sei deshalb für Angreifer möglich, böswilligen Code in
den virtuellen Speicherraum einzufügen und den Prozessor zur Ausführung zu
veranlassen. Trotz der Existenz von Code-Abschnittsgrenzen bestehe das Problem aufgrund der dynamischen Natur eines mehrprogrammfähigen Systems.
Dem Auftreten von Sicherheitsproblemen, welche durch Pufferüberläufe verursacht würden, werde durch „nicht ausführbare Stapelausbesserung“ begegnet,
welche teilweise dadurch arbeite, dass sie eine Stapelspeicherung einer Anwendung nicht ausführbar mache. Dadurch werde das Risiko einer Überlaufbedingung
zwar reduziert, da der Codesegment-Grenzwert jedoch im Prozessor gleichbliebe
und das Verändern der Ausführgrenzen der verschiedenen Tasks nicht berücksichtige, sei die Wirkung aber begrenzt (vgl. Beschreibung, S. 1, Z. 41 - S. 2,
Z. 38).


Der Anmeldung liegt somit das Problem zugrunde, das Ausgesetztsein gegenüber Stapelspeicher-, Puffer- und Datenanzeigerüberläufen bzw. –überschreitungen zu minimieren, wozu eine Programmlaufabschirmung innerhalb eines virtuellen Speicherraums eines Instruktionsprogrammlaufsystems geschaffen werde (vgl.
Beschreibung, S. 3, Z. 5 - 10).


Als Fachmann zur Lösung der Aufgabe sieht der Senat einen Informatiker oder
einen Ingenieur der Informationstechnik an, der Erfahrung in der Programmierung
von Befehlsausführungssystemen unter Nutzung virtueller Speicheradressierung
besitzt.

                                       -8-



Die Aufgabe soll durch ein Verfahren gemäß Anspruch 1, ein Betriebssystem gemäß Anspruch 9 und ein Computerprogrammprodukt gemäß Anspruch 13 gelöst
werden.




2.    Einige der im jeweiligen Anspruch 1 aufgeführten Merkmale bedürfen der
Auslegung.


Der Betriebssystemkern soll gemäß Merkmal M2 bzw. M2* durch einen Task bzw.
durch eine Anwendung mit mehreren Tasks aufgerufen werden, um eine Speicherabbildung auszuführen. Als Task werden in der Anmeldung somit mit Anwendungen verbundene Aufgaben, Prozesse bzw. Programme verstanden, welche
den Betriebssystemkern triggern (vgl. Beschreibung, S. 6, Z. 37 - 39 und S. 7,
Z. 5 - 7). Merkmal M2 legt auch fest, dass die weiteren Verfahrensschritte M3 bis
M6 bzw. M7 durch den Betriebssystemkern auszuführen sind.


Merkmal M3 bzw. M3* unterscheidet zwischen einem „virtuellen Speicherbereich“
bzw. „virtuellen Speicherregionen“ und einem „virtuellen Speicherraum“. Als virtueller Speicherraum wird dabei der gesamte verfügbare virtuelle Speicher bezeichnet (als Beispiel genannt sind 3 GB in Intel-Systemen, vgl. Beschreibung,
S. 7, Z. 7 - 17). Dagegen wird unter dem virtuellen Speicherbereich bzw. der
Region ein Teil des Speichers verstanden, welcher mit einem Task verbunden ist,
um Code oder Daten zu speichern; synonym verwendet werden in der Anmeldung
hierfür auch die Begriffe „virtuelle Speicherfläche“ oder „Adressraum“ (vgl. Beschreibung, S. 12, Z. Z. 40 - S. 13, Z. 12). Gemäß Merkmal M3 bzw. M3* erfolgt
ein Zuordnen eines virtuellen Speicherbereichs zu einem Adressraum innerhalb
des virtuellen Speicherraums, wobei dieser Adressraum keine aktiven Abbildungen zu Daten oder zu Code aufweisen soll, d. h. aus dem insgesamt zur Verfügung stehenden Speicherraum soll einem Task ein Speicherbereich zugeordnet
werden, der „frei“ ist, bzw. an dessen Stelle ein „Loch“ vorliegt, wie in der Anmel-

                                        -9-



dung in Zusammenhang mit Figur 3 erläutert ist. Merkmal M3.1 bzw. M3.1* legt
dabei fest, dass der dem Speicherbereich oder der Speicherregion jeweils zugeordnete Adressraum die jeweils niedrigstmögliche Adresse besitzt. Dies bedeutet
nichts anderes, als dass mit dem Suchen nach freien virtuellen Speicherbereichen
im virtuellen Speicherraum bei niedrigen Adressen begonnen wird, und der erste
freie Bereich mit zugehöriger Adresse dem jeweiligen Task zugeordnet wird (vgl.
Beschreibung, S. 12, Z. 40 - S. 13, Z. 17).
Für den zugeordneten Speicherbereich wird gemäß Merkmal M4 bzw. M4* die
Endadresse ermittelt, welche die Endadresse des von dem Task beanspruchten
Speicherbereichs darstellt (vgl. Beschreibung, S. 14, Z. 26 - 28).


Diese ermittelte Endadresse soll gemäß Merkmal M5 mit einem „aktuellen dynamischen Codesegment-Grenzwert“ verglichen werden.
Als Codesegment wird vorliegend der Bereich des Arbeitsspeichers bezeichnet,
der das zur Ausführung geladene Programm oder den zur Ausführung geladenen
Task geladen hat. Der Codesegment- Grenzwert stellt den aktuellen Adresswert
dar, welcher als Adressgrenze für die Codeausführung gespeichert vorliegt und
vom Prozessor überwacht wird (vgl. Beschreibung, S. 6, Z. 27 - 31 und S. 7, Z. 35
- 37). Dieser wird gemäß Merkmal M6 für den Fall, dass er kleiner als die ermittelte Endadresse ist, auf die ermittelte Endadresse für den Task gesetzt. Denn der
Codesegment-Grenzwert soll so gesetzt werden, dass er im Wesentlichen gleich
der Ausführgrenze für den gerade laufenden Code (den aktuell laufenden Task) ist
(vgl. S. 3, Z. 35 - 37). Durch den Zusatz „dynamisch“ für den Codesegment-Grenzwert in den Merkmalen M5 und M6 ist festgelegt, dass die im Merkmal M6
festgelegte Anpassung des Grenzwerts zur Laufzeit ständig – taskbezogen – erfolgt, gemäß Merkmal M2 etwa bei jedem Aufruf eines (neuen) Tasks.


Merkmal M7 erläutert, dass die Verarbeitung unter Verwendung einer Programmlaufabschirmung mit dem Codesegment-Grenzwert fortgesetzt wird, was lediglich
bedeutet, dass entweder der bereits festgelegte aktuelle Codesegment-Grenzwert

                                          - 10 -



herangezogen wird oder der aufgrund der Anpassung gemäß Merkmal M6 dynamische Codesegment-Grenzwert (vgl. Fig. 4, Schritte 408, 410, 412).




3.       Der Gegenstand des Anspruchs 1 nach Hauptantrag geht über den Inhalt
der Anmeldung in der ursprünglich eingereichten Fassung hinaus (§ 38 Satz 1
PatG).


Der mit den ursprünglichen Anmeldeunterlagen eingereichte Patentanspruch 1
lautete:


              „Verfahren zum Sichern des Betriebs eines Befehlsausführungssystems, wobei das Verfahren aufweist:
              Abbilden einer Vielzahl von virtuellen Speicherbereichen, wobei die
              Vielzahl der virtuellen Speicherbereiche mit einer Vielzahl von Aufgaben verbunden ist, in eine Vielzahl von Adressräumen, welche
              substanziell die niedrigstmöglichen Adressen besitzen;
              Verfolgen einer Ausführungsgrenze für jede aus der Vielzahl von
              Aufgaben, wobei die Ausführungsgrenze mit einer höchsten ausführbaren virtuellen Speicheradresse für wenigstens eine aus der Vielzahl von Aufgaben korrespondiert;
              Setzen eines dynamischen Codesegment-Grenzwertes, so dass er
              substanziell gleich der Ausführungsgrenze für eine aktuelle Aufgabe
              aus der Vielzahl von Aufgaben ist; und
              Ablehnen einer Übertragung der Ausführungssteuerung auf einen
              Code, welcher bei einer virtuellen Speicheradresse positioniert ist,
              welche höher als diejenige ist, welche durch den Codesegment-Grenzwert definiert ist.“

                                         - 11 -



Gegenüber diesem ursprünglichen Anspruch 1 ist im geltenden Anspruch 1 nach
Hauptantrag u. a. kein Verfolgen einer Ausführungsgrenze für jede Aufgabe vorgesehen und kein Ablehnen einer Übertragung der Ausführungssteuerung.


Zur Offenbarung des geltenden Anspruchs 1 nach Hauptantrag hat die Anmelderin
verwiesen auf die Figuren 3 und 4 sowie auf die Seite 12, Zeilen 23 bis 26 und 40
bis 41, Seite 13, Zeilen 5 bis 6 und 9 bis 12, Seite 14, Zeilen 10 bis 15 und 19 bis
35 sowie Seite 18, Zeilen 7 bis 11 der vorliegenden Anmeldung (vgl. Abschnitt 2.1
der Beschwerdebegründung vom 1. Juni 2015). Hinsichtlich der in den Ausführungsbeispielen gemäß Figur 3 und 4 vorgesehenen Prüfung von Speicherausführbits verweist die Anmelderin auf den ersten Absatz auf Seite 12 der Beschreibung.


Gemäß Merkmal M3 wird ein virtueller Speicherbereich zu einem Adressraum eines virtuellen Speicherraums zugeordnet, wodurch der Speicherbereich mit dem
Task verbunden wird. Der zugeordnete Speicherbereich soll als einzige weitere
Bedingung keine aktiven Abbildungen zu Daten oder zu ausführbarem Code aufweisen, also nicht belegt sein. Der Speicherbereich kann somit zur Abbildung von
Daten oder für ausführbaren Code oder beides gemeinsam genutzt werden. Die
weiteren Verfahrensschritte betreffen somit ebenfalls als abzubildende Bereiche
einschließlich der Endadresse sowohl Datenbereiche als auch ausführbare Bereiche. Die Ablaufdiagramme der Figuren 3 und 4, welche, wie die Anmelderin in der
mündlichen Verhandlung erläuterte, die im geltenden Anspruch 1 beanspruchte
Initialisierung der Prozesse betreffen, umfassen jedoch jeweils einen Überprüfungsschritt, ob es sich bei den abzubildenden Bereichen um Datenbereiche oder
um ausführbare Bereiche handelt. In der Figur 3 ist dieses als PROT_EXEC Bit
realisiert (vgl. Schritt 304, S. 12, Z. 29 - 34), in der Figur 4 entsprechend als virtuelles Speicherausführbit (vgl. Schritt 404, S. 14, Z. 15 - 23). Wenn diese Bits nicht
gesetzt sind, so handelt es sich bei den abzubildenden Bereichen nicht um ausführbare Bereiche, sondern um Datenbereiche. Für Datenbereiche erfolgt, wie in
den Figuren 3 und 4 in den Schritten 306 bzw. 406 festgelegt, eine „normale Ab-

                                      - 12 -



bildung“ bzw. „normale Verarbeitung“, das heißt, das Verfahren der in den Schritten 308 bis 312 bzw. 408 bis 412 festgelegten Programmlaufabschirmung, wie sie
in den Merkmalen M3.1 bis M6 beansprucht ist, wird nicht durchlaufen. Eine Überprüfung, ob es sich bei den für den Task abzubildenden Bereichen um Datenbereiche oder um Bereiche mit ausführbarem Code handelt, ist im geltenden Anspruch 1 hingegen nicht vorgesehen. Aus den ursprünglichen Ansprüchen wie
auch der Beschreibung der vorliegenden Anmeldung ist jedoch kein Verfahren
zum Sichern des Betriebs eines Befehlsausführungssystem offenbart, bei dem
eine Speicherabbildung mit der Programmlaufabschirmung auch für Datenbereiche, welche dem Task zugeordnet sind, durchgeführt wird.


Die Anmelderin hat in der mündlichen Verhandlung hierzu ausgeführt, es sei dem
Betriebssystem bekannt, welcher Task welchen Speicher verwende und es ergebe
sich aus dem ersten Absatz auf Seite 12 der Beschreibung, dass bei bestimmten
Binärformaten, insbesondere ELF-Binärformatapplikationen, Daten und Codesegmente gemeinsam als Ganzes verschoben bzw. kopiert werden könnten. Aus der
Kenntnis solcher Daten und Code umfassender Bereiche folge, so die Anmelderin,
dass die anspruchsgemäße Prüfung und Anpassung des Codesegment-Grenzwerts nicht zwangsläufig auf reine Codesegmente beschränkt sei. In besagtem
Absatz wird erläutert, dass für den Fall, dass der Code, die Daten und weitere Bereiche zusammenbleiben müssen, diese gemeinsam verschoben werden können;
zur Beibehaltung der Flexibilität würden daher bei bestimmten Binärformaten „einige dieser Bereiche“ „in der Abschirmung weggelassen“. Dies besagt nichts anderes, als dass für Bereiche, die sowohl Code als auch Daten enthalten, keine
Programmlaufabschirmung erfolgt, sondern eine „normale Verarbeitung“ vorgesehen ist, wie auch in den Figuren 3 und 4 in den Schritten 306 bzw. 406 gezeigt.
Entgegen der Argumentation der Anmelderin gibt die herangezogene Zitatstelle
daher gerade keinen Hinweis darauf, die Programmlaufabschirmung auch für Binärformate mit gemischten Code- und Daten-Speicherbereichen durchzuführen.

                                      - 13 -



Ein Verfahren zum Sichern eines Betriebs eines Befehlsausführungssystems, das
ein Zuordnen eines Speicherbereichs auch für Bereiche ohne gesetztes Speicherausführbit – also auch für Datenbereiche – ohne weitere Überprüfung vornimmt,
stellt somit eine unzulässige Verallgemeinerung der Ausführungsbeispiele dar.
Auch aus den ursprünglichen Ansprüchen, welche jeweils das Verfolgen einer
Ausführungsgrenze umfassten und damit ebenfalls direkt auf die Speicherabbildung von Code zielten, lässt sich eine Programmlaufabschirmung auch für Speicherbereiche von Daten nicht entnehmen. Das mit dem Anspruch 1 nach Hauptantrag beanspruchte Verfahren betrifft in der Gesamtheit seiner Merkmale somit
eine technische Lehre, die der Fachmann den ursprünglichen Unterlagen nicht als
mögliche Ausgestaltung der Erfindung entnehmen kann (vgl. BGH, Beschluss vom
11. September 2001 – X ZB 18/00, GRUR 2002, 49, Amtlicher Leitsatz – Drehmomentübertragungseinrichtung; BGH, Urteil vom 5. Juli 2005 – X ZR 30/02,
GRUR 2005, 1023, Amtlicher Leitsatz – Einkaufswagen II).




4.    Die in den Anspruch 1 nach Hilfsantrag 1 aufgenommenen Umformulierungen und Ergänzungen beheben die unzulässige Erweiterung nicht.


Anspruch 1 nach Hilfsantrag 1 unterscheidet sich von Anspruch 1 nach Hauptantrag darin, dass eine Anwendung mit mehreren Tasks vorgesehen ist (vgl. Merkmal M2*) und dass dementsprechend mehrere virtuelle Speicherregionen, welche
mit den Tasks verbunden sind, vorgesehen sind und für jeden der Tasks eine
Endadresse ermittelt wird (vgl. Merkmale M3* bis M4*). Zur Offenbarung der geänderten Merkmale hat die Anmelderin verwiesen auf Seite 12, Zeile 40, Seite 7,
Zeilen 14 bis 17, Seite 13, Zeilen 9 bis 12 der Beschreibung sowie auf die Figuren
3, 5 und 6.


Auch das mit Anspruch 1 nach Hilfsantrag 1 beanspruchte Verfahren weist keinen
Überprüfungsschritt auf, welcher dafür sorgt, dass die Programmlaufabschirmung

                                       - 14 -



nur bei gesetztem Speicherausführbit, also nur für ausführbare Bereiche, eingerichtet wird. Das zum Anspruch 1 nach Hauptantrag Ausgeführte gilt somit auch
für den Anspruch 1 nach Hilfsantrag 1, so dass dieser ebenfalls in der Gesamtheit
seiner Merkmale eine technische Lehre betrifft, die der Fachmann den ursprünglichen Unterlagen nicht als mögliche Ausgestaltung der Erfindung entnehmen kann.




5.       Für den Hilfsantrag 2 gilt nichts anderes. Anspruch 1 nach Hilfsantrag 2
unterscheidet sich von Anspruch 1 nach Hilfsantrag 1 durch das hinzugefügte
Merkmal M7, wonach ein Fortsetzen der Verarbeitung unter Verwendung einer
Programmlaufabschirmung erfolgt, welche auf dem Codesegment-Grenzwert basiert.


Die Angabe, dass die Programmlaufabschirmung auf dem Codesegment-Grenzwert basiert, besagt lediglich, dass der vom Prozessor gespeicherte Codesegment-Grenzwert, der eine virtuelle Speicheradressgrenze definiert (vgl. Beschreibung, S. 7, Z. 35 - 37), entweder als unveränderter Wert oder als dynamisch angepasster Wert gemäß Merkmal M6 bei der weiteren Verarbeitung herangezogen
wird. Eine Überprüfung, ob es sich bei den den Tasks zuzuordnenden Speicherregionen um Adressräume für Daten oder für ausführbaren Code handelt, ist mit
Merkmal M7 nicht gefordert. Somit fehlt auch in Anspruch 1 nach Hilfsantrag 2 ein
Verfahrensschritt der Überprüfung, welcher sicherstellen würde, dass die Programmlaufabschirmung nur für Bereiche eingerichtet wird, für die ein Speicherausführbit gesetzt ist. Das zum Anspruch 1 nach Hauptantrag und nach Hilfsantrag 1 Ausgeführte gilt somit auch für den Anspruch 1 nach Hilfsantrag 2, so dass
dieser ebenfalls in der Gesamtheit seiner Merkmale eine technische Lehre betrifft,
die der Fachmann den ursprünglichen Unterlagen nicht als mögliche Ausgestaltung der Erfindung entnehmen kann.

                                         - 15 -



Der Anspruch 1 nach Hilfsantrag 2 geht somit ebenfalls über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus (§ 38 Satz 1 PatG).




6.     Es kann dahingestellt bleiben, ob die Patentfähigkeit des Gegenstands des
jeweiligen Anspruchs 1 nach Hauptantrag und nach den Hilfsanträgen 1 und 2 in
Frage steht gegenüber dem im Verfahren befindlichen Stand der Technik gemäß
Druckschrift D1 bis D3. Ebenso kann dahingestellt bleiben, ob die vom Betriebssystemkern durchzuführenden Verfahrensschritte zum dynamischen Anpassen
eines Codesegment-Grenzwerts als ein technisches Mittel zur Lösung einer technischen Problemstellung anzusehen sind und der Ausschlusstatbestand gemäß
§ 1 Abs. 3 Nr. 3 i. V. m. Abs. 4 PatG greift.




7.     Mit dem jeweils nicht zulässigen Anspruch 1 nach Hauptantrag und nach
den Hilfsanträgen 1 und 2 sind auch die jeweiligen nebengeordneten Ansprüche 9
und 13 sowie die auf diese Ansprüche direkt oder indirekt rückbezogenen Unteransprüche 2 bis 8 und 10 bis 12 nicht schutzfähig, da auf diese Ansprüche kein
eigenständiges Patentbegehren gerichtet war (vgl. BGH, Beschluss vom
27. Juni 2007, X ZB 6/05, GRUR 2007, 862, Abschnitt III. 3. a) aa) – Informationsübermittlungsverfahren II).




8.     Nachdem die jeweiligen Anspruchssätze nach Hauptantrag und nach den
Hilfsanträgen 1 und 2 nicht schutzfähig sind, war die Beschwerde zurückzuweisen.

                                              - 16 -



                                               III.


Die Rückzahlung der Beschwerdegebühr war nach § 80 Abs. 3 PatG anzuordnen.


Nach dieser Vorschrift kann die Rückzahlung der Beschwerdegebühr angeordnet
werden, wenn dies der Billigkeit entspricht. Dies kommt insbesondere bei Verfahrensfehlern      oder     unsachgemäßer          Sachbehandlung             in     Betracht     (vgl.
Schulte/Püschel,        PatG,    9. Aufl.,   § 80      Rdn. 112 f.    und        § 73   Rdn. 131 ff.;
Busse/Keukenschrijver – Engels, PatG, 8. Aufl., § 80 Rdn 85 ff. u. Rdn. 92 ff.).


Im angefochtenen Beschluss liegen Verfahrensfehler vor (Schulte/Püschel,
a. a. O., § 73 Rdn. 143, 145). Die von der Prüfungsstelle im herangezogenen Bescheid vom 9. Oktober 2014 ausgeführte Begründung weist Mängel auf, da sie
nicht nachvollziehbar, formelhaft und unvollständig ist und eine unzutreffende
Auslegung des Patentanspruchs vorgenommen wurde.


In der vorliegenden Akte fand nach fünf Prüfungsbescheiden am 25. Januar 2012
eine Anhörung statt, in der die Anmelderin die Patentansprüche 1 bis 13, welche
dem vorliegend geltenden Hauptantrag entsprechen, vorlegte. Ausweislich des
Protokolls wollte die Prüfungsstelle ins schriftliche Verfahren zurückkehren und
den Aspekt des „Verändern des Codesegment-Grenzwertes im laufenden Betrieb“
recherchieren.      Auf         eine   Sachstandsanfrage             der     Anmelderin         vom
12. September 2014 erfolgte am 9. Oktober 2014 eine Ladung zur Anhörung am
25. November 2014, verbunden mit einem Bescheid, in dem als allgemeiner Stand
der Technik die Druckschrift D3 neu ins Verfahren eingeführt wurde.


In dem Bescheid wird zunächst – ohne jegliche inhaltliche Bezugnahme zu Merkmalen des Anspruchs – ausgeführt, die Zulässigkeit des Anspruchs könne nicht
nachvollzogen werden.

                                       - 17 -



Zur Auslegung des Anspruchs führt die Prüfungsstelle u. a. aus:




Es folgen Ausführungen zu Begriffen des Anspruchs, die möglicherweise die Klarheit der Merkmale in Frage stellen sollen. Schließlich wird festgestellt, der technische Gehalt des Anspruchs 1 lasse sich damit wie folgt zusammenfassen:




Das so beanspruchte Verfahren, so die Prüfungsstelle weiter, ergebe sich aus
dem Grundwissen des Fachmanns. Dazu führt sie u. a. aus, unterstelle man, dass
ein Codesegment eine ähnliche funktionale Bedeutung habe wie ein Codesegment in einer Intel-Architektur (siehe Druckschrift D3), so sei klar, dass der zugeordnete Teil des Speichers nur dann durch den Task adressierbar sei, wenn er
vollständig im Codesegment liege. Wenn die Endadresse des Teils des Speichers
größer als der dynamische Codesegment-Grenzwert sei, liege es damit nahe, den
Codesegment-Grenzwert auf die Endadresse zu erhöhen. Der Grenzwert werde
damit dynamisch der Endadresse angepasst.

                                      - 18 -



Mit Schriftsatz vom 20. November 2014 teilte die Anmelderin mit, die mündliche
Verhandlung (am 25. November 2014) nicht wahrnehmen zu wollen und beantragte   eine    Entscheidung     nach    Aktenlage.    Daraufhin     erging   am
24. November 2014 der Zurückweisungsbeschluss aus Gründen des Bescheids
vom 9. Oktober 2014.


Der Zurückweisungsbeschluss stützt sich somit darauf, der von der Prüfungsstelle
ausgelegte technische Gehalt des Verfahrens nach Anspruch 1 ergebe sich aus
dem Grundwissen des Fachmanns. Bei der Auslegung, die die Prüfungsstelle offenbar auf Art. 69 EPÜ stützt, hat die Prüfungsstelle den Anspruch 1 auf die oben
aufgeführten Schritte 1. bis 3. verkürzt, und dabei gegenüber dem geltendem Anspruch 1 insbesondere Merkmal M3.1, wonach der Adressraum die niedrigstmögliche Adresse besitzen soll, Merkmal M4, wonach die Endadresse des Speicherbereichs zu ermitteln ist, sowie die Adjektive „aktuell und dynamisch“ für den
Codesegment-Grenzwert weggelassen. Dies stellt eine nicht zulässige Verallgemeinerung des beanspruchten Verfahrens auf einzelne Teilmerkmale dar. Ob
diese unzutreffende Auslegung dadurch begründet war, dass die Prüfungsstelle
sich auf einen Artikel des EPÜ bezieht, der im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt auch für eine PCT-Anmeldung in nationaler Phase
unbeachtlich ist, kann dahingestellt bleiben. Die von der Prüfungsstelle angeführte
Begründung, das so (wie von der Prüfungsstelle ausgelegte) beanspruchte Verfahren ergebe sich aus dem Grundwissen des Fachmanns, beruht allein auf Behauptungen und stellt für den Anmelder keine nachprüfbare Argumentation dar.
Zudem wurde der Fachmann von der Prüfungsstelle im gesamten Prüfungsverfahren, und insbesondere in dem Bescheid vom 9. Oktober 2014, auf den die Zurückweisung sich stützt, nicht definiert, so dass ungeklärt bleibt, was zu dessen
Fachwissen gehört. Auch aus der im Bescheid als „allgemein und im Übrigen“
noch aufgeführten Zitatstelle aus Druckschrift D1 und den knappen Ausführungen
dazu ergibt sich kein konkreter Bezug zu den beanspruchten Verfahrensschritten,
der für den Anmelder nachvollziehbar gewesen wäre.

                                       - 19 -



Zudem wurde eine Zurückweisung der Anmeldung mangels einer zulässigen Änderung des Patentanspruchs angekündigt, falls die Anmelderin die ursprüngliche
Offenbarung des Anspruchs 1 nicht detailliert nachweise. Dass die Zulässigkeit
des Anspruchs 1 nicht nachvollzogen werden könne, stellt lediglich eine Behauptung der Prüfungsstelle dar, da jegliche Bezugnahme zu Merkmalen des Anspruchs 1 fehlt.


Der Senat sieht diese nicht nachvollziehbare, formelhafte und unvollständige Begründung und die unzutreffende, willkürlich verknappte Auslegung des Patentanspruchs als eine mangelhafte Begründung und mängelbehaftete Sachbehandlung
der Anmeldung durch die Prüfungsstelle an, so dass eine Einbehaltung der Beschwerdegebühr unbillig erschiene (Schulte/Püschel, a. a. O., § 73 Rdn. 143, 145
und Busse/Keukenschrijver – Engels, a. a. O., § 80 Rdn. 97, 129).



                                         IV.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,

   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
       Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
       Befangenheit mit Erfolg abgelehnt war,

   3. einem Beteiligten das rechtliche Gehör versagt war,

   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
       war, sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,

                                     - 20 -



   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
      der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
      sind, oder

   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn                Kruppa       Dr. Otten-Dünnweber                Altvater


                                                                              Hu
