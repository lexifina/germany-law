---
ecli: "ECLI:DE:BPatG:2002:250402B17Wpat2.01.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 2/01"
decided: "2002-04-25"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2002&Sort=1&Seite=39&nr=20606&anz=1911&pos=594&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2002-04-25_17_W-pat_2_01_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 2/01 vom 2002-04-25

## Entscheidung

BUNDESPATENTGERICHT


  17 W (pat) 2/01                                         Verkündet am
 _______________                                          25. April 2002
    (Aktenzeichen)                                             Kreth
                                                         Justizangestellte
                                                       als Urkundsbeamtin
                                                       der Geschäftsstelle

                          BESCHLUSS

                        In der Beschwerdesache


                     betreffend das Patent 35 46 683


…




BPatG 154
6.70

                                       -2-




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 25. April 2002 unter Mitwirkung des Vorsitzenden
Richters Grimm sowie der Richter Dr. Schmitt, Dipl.-Phys. Dr. Greis und Dipl.-Ing.
Bertl


beschlossen:


        Auf die Beschwerde der Patentinhaberin wird der Beschluss der
        Patentabteilung 53 des Deutschen Patent- und Markenamts vom
        25. Oktober 2000 aufgehoben. Das Patent Nr. 35 46 683 wird in
        beschränktem Umfang aufrechterhalten mit folgenden Unterlagen:


        Patentanspruch gemäß "Hauptantrag", überreicht in der mündlichen Verhandlung vom 25. April 2002, Beschreibung gemäß
        Patentschrift mit der Maßgabe, dass die S. 2, Z. 37 bis 64 ersetzt
        wird durch die am 18. Januar 1992 eingegangene

                                         -3-



          "ergänzte Beschreibungseinleitung" unter Streichen von Seite 2,
          letzter Absatz,
          Zeichnungen gemäß Patentschrift.




                                        Gründe


                                               I.


Gegen die Erteilung des Patents mit der Bezeichnung


      "Verfahren zum Betreiben einer Datenverarbeitungsanlage"
wurden fünf Einsprüche erhoben. Die T…
GmbH und S… AG haben ihren Einspruch zurückgenommen. Mit Beschluss
vom 25. Oktober 2000 hat die Patentabteilung 53 des Deutschen Patent- und
Markenamts das Patent widerrufen. In den Gründen ist ausgeführt, dass der
Gegenstand des Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit
beruhe.


Gegen diesen Beschluss richtet sich die Beschwerde der Patentinhaberin. Sie hat
in der mündlichen Verhandlung einen (einzigen) neuen Patentanspruch gemäß
"Hauptantrag" und einen (einzigen) neuen Patentanspruch gemäß "Hilfsantrag"
überreicht.


Der Patentanspruch nach "Hauptantrag" lautet:


          "Verfahren zum Betreiben einer Datenverarbeitungsanlage, insbesondere für Kraftfahrzeuge, mit wenigstens zwei Rechnern, einer
          die Rechner verbindenden Leitung zur Übertragung von Botschaften, wobei die Botschaft zumindest einen Kopfteil und einen
          Datenteil aufweist, wobei der Kopfteil die Namen der Daten enthält

                                      -4-



       und wobei jeder Rechner eine Liste der für ihn relevanten Namen
       aufweist, und der Kopfteil zumindest teilweise mit dieser Liste
       verglichen wird und nur die Botschaften weitergeleitet werden,
       deren Kopfteil zumindest teilweise in der Liste gefunden wird,
       wobei die Rechner an den Bus linear oder sternförmig gekoppelt
       sind, so daß die Botschaft von allen Rechnern gleichzeitig
       empfangen und ausgewertet wird,


            wobei


       eine ankommende Botschaft nur dann in einem Speicher
       (DPRAM) übernommen wird, wenn ihr Name dort gefunden wird,


       wobei in dem Speicher wenigstens eine Folge von Blöcken
       abgelegt ist, wobei jeder Block aus gespeichertem Namen und
       Control-Segment sowie einem Datenteil besteht, und der Datenteil
       die empfangenen und fortgehenden Daten enthält, und das
       Control-Segment wenigstens Steuerinformationen für die Abwicklung des Datenaustausches der Botschaft enthält,


       wobei die Übertragung der ankommenden Botschaften in den
       Speicher bei gesetztem Schreibschutz im Control-Segment für
       diese Botschaft (RECEIVE-TRANSMIT = LOW) blockierbar ist."




Bei dem Patentanspruch gemäß "Hilfsantrag" ist dem Patentanspruch gemäß
"Hauptantrag" noch folgendes Merkmal angefügt:


"wobei die Weiterleitung der empfangenen Botschaft im Rechner nur erfolgt, wenn
die Botschaft vollständig empfangen wurde, was durch Rücksetzen eines pending
bit im Control-Segment angezeigt wurde (pending = low)."

                                       -5-




Die Patentinhaberin begründet ihre Auffassung, dass der Patentanspruch gemäß
"Hauptantrag" patentfähig sei, im wesentlichen wie folgt:


Durch das Verfahren nach dem Patentanspruch könne in einem verteilten System,
das aus über einen Bus verbundenen Rechnern bestehe, eine Botschaft auf dem
Bus an allen Empfängern zeitgleich anliegen und zudem gesteuert werden, ob
Daten im Speicher eines Empfängers durch Daten dieser Botschaft überschrieben
werden dürften oder nicht.


Bei dem im Patentanspruch definierten Speicher handle es sich um einen
Speicher für empfangene und fortgehende Botschaften. Die aus gespeichertem
Namen, Control-Segment und Datenteil bestehenden Blöcke hätten immer einen
festen Platz im Speicher.


Bevor eine Botschaft am Rechner ankomme, werde im Control-Segment für eine
Botschaft ein Bit direkt in der Station - vom Interface Management Processor
(IMP) oder der CPU - gesetzt, das anzeige, ob Daten für diese Botschaft in den
Speicher übernommen werden sollten oder nicht. Dieser Schreibschutz sei
zusätzlich zu dem Identifizierervergleich mit der Liste im Rechner vorgesehen. Der
zusätzliche Schreibschutz bestehe aus dem Blockieren der Übernahme der
Botschaft in den Speicher durch das Setzen eines Bits im Control-Segment,
welches nicht von außen über den Bus, sondern intern gesetzt werde.


Damit bestehe die im Patentanspruch definierte Akzeptanzfilterung aus einem
(teilweisen) Kopfteilvergleich und     einem   zusätzlichen Schreibschutz. Das
Verfahren nach dem Patentanspruch habe demnach den Vorteil, dass die
Botschaft von allen Rechnern gleichzeitig empfangen und ausgewertet und
außerdem ein unterschiedlicher Informationsstand vermieden werde. Das
Verfahren     genüge        somit   Echtzeitanforderungen    und      gewährleiste
Datenkonsistenz.

                                              -6-




Aus der US 4 482 951 sei ein System mit über einen Bus verbundenen Rechnern
bekannt, die über den Bus empfangene Botschaften auswerten. Die Übernahme
einer Botschaft in den Rechner erfolge aber lediglich durch einen Vergleich eines
Kopfteils der Botschaft im RAM des Rechners, welcher Vergleich dann Werte von
Null oder Eins liefere. Bei einem erhaltenen Wert von Eins werde die Botschaft in
den Rechner übernommen, bei einem Wert von Null werde sie verworfen. Der US
4 482 951 sei kein zusätzlicher Schreibschutz entnehmbar, der intern im Speicher
eingestellt werden könne.


Die Patentinhaberin beantragt,


        den angefochtenen Beschluss aufzuheben und das Patent in
        beschränktem Umfang aufrechtzuerhalten mit folgenden Unterlagen:
        (einziger)     Patentanspruch     gemäß      "Hauptantrag",     hilfsweise
        gemäß        "Hilfsantrag",   beide    Fassungen   überreicht     in   der
        mündlichen Verhandlung am 25. April 2002,
        Beschreibung gemäß Patentschrift mit der Maßgabe, daß die
        Seite 2, Zeilen 37 bis 64 ersetzt wird durch die am 18. Januar 1992       eingegangene     "ergänzte    Beschreibungseinleitung"
        unter Streichen von Seite 2, letzter Absatz,
        Zeichnungen gemäß Patentschrift.


Die Einsprechende I stellt den Antrag,


        die Beschwerde zurückzuweisen.


Sie trägt im wesentlichen folgendes vor:

                                       -7-



Ursprüngliche Aufgabe des Streitpatents sei, Botschaften auf dem Bus mehreren
Rechnern gleichzeitig zugänglich zu machen, so dass ein unterschiedlicher
Informationsstand vermieden werde. Durch das Blockieren der Übernahme der
Botschaft in den Speicher bei gesetztem Schreibschutz werde aber gerade ein
unterschiedlicher Informationsstand erhalten. Datenkonsistenz sei demnach nicht
gegeben.


Abgesehen davon sei das Setzen von Steuerinformationen zum Blockieren der
Übernahme der Botschaft im Speicher selbst naheliegend, da dies erforderlich sei,
wenn ein Speicher von zwei Seiten zugänglich sei. Aus der DE 31 14 734 A1 sei
ein Koppelspeicher bekannt, der zwischen einem Rechner und externe Teilnehmer geschaltet sei. In dem Koppelspeicher werde von einer Steuereinheit ein
Bit gesetzt, das angebe, dass die Botschaft vollständig übertragen und abholbereit
sei. Außerdem werde auch vom Rechner ein Bit gesetzt, das angebe, ob eine
Botschaft im Koppelspeicher vom Rechner ausgelesen worden sei oder nicht.


Ferner sei der US 4 482 951 sowohl der Kopfteilvergleich als auch der Schreibschutz zu entnehmen. Aus der US 4 482 951 sei bekannt, dass der Kopfteil zum
Adressieren eines RAM verwendet werde, um festzustellen, ob die Botschaft
übernommen werden solle oder nicht. Durch die RAM-Adressierung werde ein Bit
ausgelesen, bei dessen Wert 1 die Botschaft übernommen und bei dessen Wert 0
die Botschaft verworfen werde. Demnach müssten zur Übernahme einer Botschaft
in den Rechner sowohl der Kopfteil im Speicher gefunden werden als auch das
Schreibschutz-Bit rückgesetzt sein. Dieses Bit könne auch vom Rechner gesetzt
werden, wie in Spalte 7, Zeilen 20 ff der US 4 482 951 beschrieben sei.


                                        II.


Die frist- und formgerecht erhobene Beschwerde ist zulässig und führt zur beschränkten Aufrechterhaltung des Patents, da der Gegenstand gemäß Pa-

                                        -8-



tentanspruch 1 gemäß "Hauptantrag" patentfähig ist, insbesondere auf einer
erfinderischen Tätigkeit beruht (§ 4 PatG).


Der in der mündlichen Verhandlung überreichte Patentanspruch gemäß "Hauptantrag" ist gegenüber dem erteilten Patentanspruch 1 nicht in unzulässiger Weise
geändert worden.


Der Patentanspruch beinhaltet vollständig den erteilten Patentanspruch 1.


Das dem erteilten Patentanspruch 1 angefügte Merkmal des Patentanspruchs,
dass "eine ankommende Botschaft nur dann in einen Speicher (DPRAM)
übernommen wird, wenn ihr Name dort gefunden wird", ist der Patentschrift auf
Seite 25, Zeilen 5 und 6 zu entnehmen, wobei der Identifier der Name der
Botschaft ist.


Das weiter angefügte Merkmal des Patentanspruch, dass "in dem Speicher
wenigstens eine Folge von Blöcken abgelegt ist, wobei jeder Block aus gespeichertem Namen und Control-Segment sowie einem Datenteil besteht, und der
Datenteil die empfangenen und fortgehenden Daten enthält, und das Control-Segment wenigstens Steuerinformationen für die Abwicklung des Datenaustausches der Botschaft enthält", ist der Patentschrift auf Seite 25, Zeilen 28, 29
und 36 bis 39, Seite 26, Zeilen 33 bis 38 sowie den Abbildungen auf Seite 26 zu
entnehmen. Demnach ist der Speicher in Blöcken organisiert, die jeweils einen
Namen (Identifier), ein Control-Segment und einen Datenteil (Data-Field)
enthalten. Im Speicher gibt es für jeden Namen einer Botschaft einen zugehörigen
Block, in dessen Datenteil die empfangenen und fortgehenden Daten enthalten
sind. Der Patentanspruch bezieht sich somit auf einen Speicher für empfangene
und fortgehende Daten.


Das letzte angefügte Merkmal des Patentanspruchs, dass "die Übertragung der
ankommenden Botschaften in den Speicher bei gesetztem Schreibschutz im

                                        -9-



Control-Segment für diese Botschaft (RECEIVE-TRANSMIT=LOW) blockierbar
ist", ist der Patentschrift auf Seite 28, Zeilen 15 bis 31 und dem Patentanspruch 4
zu entnehmen. Bei diesem Merkmal handelt es sich um einen zusätzlichen
Schreibschutz, wie es auf Seite 25, Zeilen 5 und 6 der Patentschrift angeführt ist.
Dort ist beschrieben, dass eine ankommende Botschaft nur dann in den Speicher
übernommen wird, wenn ihr Name dort gefunden wird und wenn sie auch
empfangen werden soll, was durch das Receive/Transmit Bit angezeigt wird.
Dieses Bit wird im Control-Segment, d.h. im Speicher des Rechners, intern, nicht
über eine Botschaft von der Leitung, gesetzt.


In der mündlichen Verhandlung wurden die im Einspruchsverfahren zitierten
Druckschriften US 4 482 951 und DE 31 14 734 A1 aufgegriffen.


Das Verfahren nach dem Patentanspruch gemäß "Hauptantrag" ist neu und beruht
auf erfinderischer Tätigkeit.


Aus der US 4 482 951 ist ein Verfahren zum Betreiben einer Datenverarbeitungsanlage bekannt mit wenigstens zwei Rechnern 22-1...22-N, die über eine
Leitung 21 zur Übertragung von Botschaften 39 verbunden sind. Eine Botschaft
enthält einen Funktionscode bzw. eine Funktionsadresse 49. Zur Überprüfung, ob
die Botschaft auf der Leitung in einen Speicher 31 eines Rechners 22 übernommen werden soll, wird die Funktionsadresse der Botschaft an ein RAM 61
einer Busschnittstelle 34 des Rechners 22 angelegt, und das Bit des RAM 61 an
dieser Adresse wird ausgelesen. Hat das Bit den Wert Null, wird die übertragene
Botschaft verworfen. Hat das Bit den Wert Eins, wird die Botschaft akzeptiert und
übernommen (vgl. Spalte 6, Zeile 42 bis Spalte 7, Zeile 19). Der Inhalt des RAM
61 kann geändert werden, indem eine Steuerbotschaft über die Leitung 21
übertragen wird oder indem eine Botschaft direkt von einer Benutzerschnittstelle
zu dem RAM gesendet wird (vgl. Spalte 7, Zeilen 20 bis 35). Wird eine Botschaft
akzeptiert, stößt sie einen Speichervorgang zur Speicherung der Botschaft im
Speicher 31 an (vgl. Spalte 7, Zeilen 36 bis 57).

                                      - 10 -




Der US 4 482 951 ist demnach ein RAM 61 zur Überprüfung, ob eine Botschaft
vom zugehörigen Rechner akzeptiert wird, und ein Speicher 31 zur Speicherung
der Botschaft bzw. deren Dateninhalts zu entnehmen. Durch diese Anordnung
sollen an der Busschnittstelle ankommende Botschaften ohne Verzögerung direkt
im Speicher 31 gespeichert werden (vgl. Spalte 2, Zeilen 54 bis 60).


Die im RAM 61 durchgeführte Überprüfung ist wie der Vergleich eines Kopfteils
mit einer Liste im RAM zu sehen. Soll eine Botschaft von der Busschnittstelle nicht
mehr akzeptiert werden, muss das Bit an der Funktionsadresse der Botschaft auf
den Wert Null geändert werden. Dies entspricht dem Streichen eines Kopfteils aus
der Liste.


Dem Kopfteilvergleich gemäß dem Patentanspruch nach "Hauptantrag" zur Feststellung, ob eine Botschaft überhaupt in den Rechner weitergeleitet wird, entspricht demnach das in der US 4 482 951 beschriebene Auslesen des RAM 61.
Der zusätzliche intern im Speicher durchgeführte Schreibschutz gemäß dem
Patentanspruch zum Blockieren der Speicherung einer grundsätzlich übernehmbaren Botschaft im Speicher lässt sich hingegen der US 4 482 951 nicht
entnehmen. In der US 4 482 951 ist beschrieben, dass die Daten der Botschaft im
Speicher 31 angrenzend abgelegt werden können (vgl. Spalte 8, Zeilen 5 bis 16).
Jedoch ist der Speicher 31 nicht in Blöcken jeweils bestehend aus einem Namen,
einem Control-Segment und einem Datenteil organisiert wie der Speicher gemäß
dem Patentanspruch und enthält zudem nicht empfangene und fortgehende
Daten, d.h. von der Leitung empfangene und zu der Leitung fortgehende Daten.


Der Fall, wie er in dem Speicher gemäß dem Patentanspruch auftreten kann, dass
Daten einer über die Leitung an dem Rechner ankommenden Botschaft mit dem
Namen X über die Daten in dem Block mit dem Namen X, der im Speicher
(DPRAM) gespeichert ist, geschrieben werden können, kann im Speicher 31 der
US 4 482 951 nicht auftreten. Der durch die Speicherorganisation gemäß dem

                                       - 11 -



Patentanspruch gegebenen Möglichkeit des unerwünschten Überschreibens von
Daten im Speicher wird im Verfahren gemäß dem Patentanspruch durch die
zusätzliche Blockierungsmöglichkeit der Übertragung der ankommenden Botschaft
durch Setzen des Schreibschutzes im Control-Segment begegnet.


Der Fachmann fand also in der US 4 482 951 weder eine Anregung, den Speicher
für empfangene und fortgehende Daten in Blöcken aus gespeichertem Namen,
Control-Segment und Datenteil zu organisieren, noch eine Anregung zur Lösung
eines sich aus dieser Organisation ergebenden möglichen Überschreib-Konflikts.


In der DE 31 14 734 A1 ist eine Anordnung zur Datenübertragung zwischen einem
Rechner und externen Teilnehmern über einen Koppelspeicher beschrieben.
Dabei kann der Datenaustausch zwischen dem Rechner und dem Koppelspeicher
ohne Behinderung durch Nachrichten stattfinden, die gerade von Teilnehmern
ankommen (vgl. Seite 5, Absatz 2). Der Koppelspeicher ist ein Schreib/Lesespeicher, der in Bereiche für Sende- und Empfangsdaten unterteilt ist (vgl. Seite 5,
Absatz 3). Er beinhaltet Speicherblöcke mit Angaben der Blocklänge sowie eine
Adressenliste der Anfangsadressen der zu sendenden Blöcke, wobei in jeder
Anfangsadresse eine Stelle für die Anzeige eines Sendeauftrags vorhanden ist.
Ferner kann im Bereich für den Empfang je Teilnehmer ein zirkular beschreibbarer
Speicherabschnitt vorhanden sein, in den die Telegrammen zugeordneten Daten
byteweise gelangen, wobei jedes Telegramm in einem Block abgelegt wird und je
Block im Speicherabschnitt eine Stelle für die Anzeige der Vollständigkeit der
eingelesenen Daten und eine Stelle für die Anzeige des Auslesens des Blocks
durch den Rechner vorgesehen ist (vgl. Seite 5, letzter Absatz; vgl. auch Seite 9,
Absätze 2 und 3).


In der DE 31 14 734 A1 wird keine Überprüfung dahingehend durchgeführt, ob
eine Botschaft überhaupt vom Rechner empfangen werden soll, d.h. es erfolgt
kein Vergleich eines Namens einer Botschaft mit einer Liste im Speicher. Des
weiteren ist der DE 31 14 734 A1 keine Organisation des Speichers in Blöcken

                                     - 12 -



aus gespeichertem Namen, Control-Segment und Datenteil entnehmbar. Der
Koppelspeicher ist vielmehr ein zirkularer Speicher, in den empfangene
Botschaften fortlaufend geschrieben und aus dem die empfangenen Botschaften
fortlaufend vom Rechner ausgelesen werden. Außerdem ist er in Bereiche für
empfangene und fortgehende Daten unterteilt.


Dagegen ermöglicht die feste Speicherorganisation gemäß dem Patentanspruch
dem Rechner einen einfachen Zugriff auf neue Informationen, da er immer nur an
einer bestimmten Stelle im Speicher nachschauen muss, ob neue Daten bezüglich
eines bestimmen Namens eingetroffen sind (vgl. Patentschrift Seite 3, Zeilen 51
bis 54). Wie vorstehend angeführt, ist mit dieser Speicherorganisation jedoch die
Möglichkeit verbunden, dass Daten im Speicher mit dem Namen X von einer
ankommenden und angenommenen Botschaft mit dem Namen X überschrieben
werden. Dies ist unerwünscht, wenn es sich bei den Daten im Speicher um
fortgehende Daten handelt (vgl. Patentschrift Seite 3, Zeilen 59, 60; Seite 28,
Zeilen 15 bis 31). Durch die interne Schreibschutz-Funktion gemäß dem Patentanspruch wird ein unerwünschtes Überschreiben verhindert.


Da der Koppelspeicher der DE 31 14 734 A1 verschiedene Bereiche für
empfangene und fortgehende Daten aufweist, können selbst bei einer Speicherorganisation in Blöcken gemäß dem Patentanspruch keine Konflikte auftreten.
Der Fachmann erhielt demnach auch aus der DE 31 14 734 A1 keinen Hinweis,
den Speicher derart wie im Patentanspruch definiert zu organisieren, und auch
keine Anregung, den sich aus der Speicherorganisation ergebenden Überschreib-Konflikt zu lösen.


Selbst bei Hinzuziehung der Lehren beider Druckschriften konnte der Fachmann
nicht zu einem Verfahren gelangen, bei dem die Speicherung einer grundsätzlich
in einen Speicher eines Rechners zu übernehmenden Botschaft zusätzlich intern
durch einen Schreibschutz blockiert werden kann, wobei der Speicher ein

                                      - 13 -



Speicher für empfangene und fortgehende Daten und in Blöcken organisiert ist,
die jeweils aus gespeichertem Namen, Control-Segment und Datenteil bestehen.


Die übrigen im bisherigen Verfahren genannten, in der mündlichen Verhandlung
nicht wieder aufgegriffenen Druckschriften kommen dem Gegenstand des Patents
nicht näher, wie eine Überprüfung durch den Senat ergeben hat.


Der Gegenstand des Patentanspruchs ist nach alledem patentfähig.


Da auch die übrigen Unterlagen den an sie zu stellenden Forderungen entsprechen, war zu entscheiden wie im Beschlusstenor angegeben.


Nachdem dem Hauptantrag stattgegeben wird, ist über den Hilfsantrag nicht mehr
zu befinden.




Grimm                   Dr. Schmitt            Dr. Greis                  Bertl


                                                                            Na
