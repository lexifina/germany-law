---
ecli: "ECLI:DE:BPatG:2015:130115B17Wpat21.11.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 21/11"
decided: "2015-01-13"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=0&nr=26875&anz=851&pos=6&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-01-13_17_W-pat_21_11_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 17 W (pat) 21/11 vom 2015-01-13

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 21/11                                                     Verkündet am
_______________                                                      13. Januar 2015
    (Aktenzeichen)                                                          …




                               BESCHLUSS

                             In der Beschwerdesache


             betreffend die Patentanmeldung 10 2007 041 691.3 - 53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die     mündliche    Verhandlung   vom   13. Januar 2015   unter   Mitwirkung   des
Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Eder sowie der
Richter Dipl.-Ing. Baumgardt und Dipl.-Ing. Hoffmann


beschlossen:


                        Die Beschwerde wird zurückgewiesen.



BPatG 154
05.11

                                        -2-



                                    Gründe


                                         I.


Die vorliegende Patentanmeldung, welche die Priorität einer Voranmeldung in
Japan vom 24. November 2006 in Anspruch nimmt, wurde am 3. September 2007
beim Deutschen Patent- und Markenamt in deutscher Sprache eingereicht unter
der Bezeichnung


           „ Datenträgermigrationsprogramm, -verfahren und -system “.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06F des
Deutschen Patent- und Markenamts vom 7. Februar 2011 mit der Begründung
zurückgewiesen, dass der Gegenstand des Hauptanspruchs mangels erfinderischer Tätigkeit nicht gewährbar sei. Denn er ergebe sich aus der Zusammenschau
der Druckschriften D3 und D4 (s. u.).


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Mit ihrer
Eingabe vom 3. September 2012 stellt sie den Antrag,


        den Beschluss des Deutschen Patent- und Markenamtes vom
        7. Februar 2011 betreffend die Zurückweisung der deutschen
        Patentanmeldung 10 2007 041 691.3 aufzuheben und die Patenterteilung zu dieser Patentanmeldung mit den (dort im Einzelnen
        aufgeführten) Unterlagen des Hauptantrags zu beschließen,


        hilfsweise mit den (dort im Einzelnen aufgeführten) Unterlagen des
        Hilfsantrags zu beschließen,


        und weiter hilfsweise eine mündliche Verhandlung anzuberaumen,
        falls eine Patenterteilung nach dem Hauptantrag oder nach dem

                                        -3-



        Hilfsantrag alleine im schriftlichen Verfahren nicht möglich erscheint.


Dazu trägt die Anmelderin schriftlich vor, sie halte die Interpretationen des Prüfers
für unbegründet ausgedehnt, was zu einer unzutreffenden Beurteilung und Verneinung der Patentfähigkeit geführt habe. Insbesondere seien die beanspruchten
Schritte „Beurteilen“ und „Blockieren des tatsächlichen Zugriffs“ völlig verschieden
von dem, was aus der Entgegenhaltung D4 (s. u.) hervorgehe.


In der Fassung nach Hauptantrag lautet der Patentanspruch 1 (hier mit einer
möglichen Gliederung versehen):


        (a)   1. Ein Datenträgermigrationsverfahren zum Veranlassen, um
              eine Migration von einem ersten Datenträgermanager (3) zu
              einem zweiten Datenträgermanager (7) durchzuführen, wobei das Datenträgermigrationsverfahren umfasst:


        (b)   indem der erste Datenträgermanager (3) veranlasst wird, tatsächliche Zugriffe auf ein physikalisches Medium (13) durchzuführen, Erhalten (S5) von Information einer Zuordnung,
              durch den ersten Datenträgermanager (3), zwischen Abständen eines logischen Datenträgers und physikalischen Blöcken auf dem physikalischen Medium (13);


        (c)   Beurteilen (S7), basierend auf der erhaltenen Information der
              Zuordnung, ob ein außergewöhnliches Datenlayout gemacht
              wird oder nicht; und


        (d)   nach einem Erkennen (Nein-Route bei Schritt S7), dass
              beurteilt wird, dass das außergewöhnliche Datenlayout nicht
              gemacht wird, nur Aktualisieren eines Headerbereichs auf

                                          -4-



              dem physikalischen Medium (13) für den zweiten Datenträgermanager (7), und


        (e)   wobei das Erhalten durchgeführt wird, indem ein Programmmodul zum Blockieren des tatsächlichen Zugriffs durch den
              ersten Datenträgermanager (3) auf das physikalische Medium (13) verwendet wird.


Bezüglich der nebengeordneten Patentansprüche 7 und 11 sowie der Unteransprüche 2 bis 6 und 8 bis 10 wird auf die Akte verwiesen.


In der Fassung des Hilfsantrags lautet der Patentanspruch 1 (mit einer ähnlichen
Gliederung wie beim Hauptantrag versehen):


        (a)   1. Ein Datenträgermigrationsverfahren zum Veranlassen, um
              eine Migration von einem ersten Datenträgermanager (3) zu
              einem zweiten Datenträgermanager (7) durchzuführen, wobei das Datenträgermigrationsverfahren umfasst:


        (b') Veranlassen des ersten Datenträgermanagers (3), tatsächliche Zugriffe auf ein physikalisches Medium (13) durchzuführen,


        (e') Unterbrechen (S5) der tatsächlichen Zugriffe durch den ersten Datenträgermanager durch ein Programmmodul zum
              Blockieren der tatsächlichen Zugriffe durch den ersten Datenträgermanager (3) auf das physikalische Medium (13), um
              ein von dem ersten Datenträgermanager (3) durchgeführtes
              Abbilden (S5) zu erzeugen, zwischen Abständen eines logischen Datenträgers und physikalischen Blöcken auf dem
              physikalischen Medium (13);

                                        -5-



        (c') Beurteilen (S7), ob das Abbilden identisch mit einem zweiten
              Abbilden basierend auf einer Datenträgerkonfigurationsinformation, die in einem Headerbereich auf dem physikalischen
              Medium gespeichert ist, ist oder nicht; und


        (d') nach einem Erkennen (Ja-Route bei Schritt S7), dass beurteilt wird, dass das Abbilden identisch mit dem zweiten Abbilden ist, Aktualisieren (S11) eines Headerbereichs auf dem
              physikalischen Medium (13) für den zweiten Datenträgermanager (7).


Die ihm nebengeordneten Patentansprüche 6 und 9 sowie die Unteransprüche 2
bis 5 und 7, 8 sind ebenfalls der Akte zu entnehmen.


Als Aufgabe ist in der Anmeldung, Absatz [0007] angegeben: eine Technik bereitzustellen, um die Datenträgermigration mit hoher Geschwindigkeit zu ermöglichen,
selbst wenn der Datenträgermanager verwendet wird, dessen Spezifikation nicht
vollständig zugänglich ist.


Im Verfahren sind folgende Druckschriften entgegengehalten worden:


        D1    US 2006 / 47 923 A1
        D2    US 2006 / 129 537 A1
        D3    WO 2005 / 101 181 A2
        D4    EP 1 158 397 A2




                                         II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, weil der Patentanspruch 1 nach Hauptantrag eine unzulässige Änderung gegenüber dem Gegenstand der Anmeldung aufweist (§ 38 PatG),

                                       -6-



und die Lehre des Patentanspruchs 1 nach Hilfsantrag in der Anmeldung nicht so
deutlich und vollständig offenbart ist, dass ein Fachmann sie ausführen könnte
(§ 34 Abs. 4 PatG).


1.    Die vorliegende Patentanmeldung betrifft Speichersysteme mit einer Mehrzahl von physikalischen und insbesondere logischen Datenträgern, die von einem
„Datenträger-Manager“-Programm verwaltet werden.


Dabei kann es erforderlich werden, solche Datenträger von einem Datenverwaltungssystem auf ein anderes zu „migrieren“, d. h. sämtliche Daten aus dem einen
in das andre Datenverwaltungssystem zu übertragen; dabei müssen die Daten
natürlich unverändert bleiben, jedoch wird sich die Art der Abspeicherung und die
Verwaltung der zugeordneten Datenblöcke abhängig vom Datenverwaltungssystem (Datenträger-Manager) ändern.


Eine unmittelbar einleuchtende, „sichere“ Methode für die Datenträger-Migration
besteht darin, alle Speicherblöcke des Datenträgers von dem dort verwendeten
Datenträger-Manager auslesen zu lassen, an den Datenträger-Manager des Ziel-Systems zu übergeben und von diesem neu speichern zu lassen (siehe Offenlegungsschrift Absatz [0002]). Damit ist sichergestellt, dass alle Daten von dem
Datenträger-Manager des Ziel-Systems zuverlässig wieder abrufbar sind, da dieser selber die Speicherung veranlasst hat.


Andererseits ist im Zielsystem jedoch nur die Verwaltung der Datenblöcke unterschiedlich, die Daten selber dürfen sich durch die Migration nicht verändern. Die
Anmeldung geht von der Idee aus, dass unter bestimmten Bedingungen ein physikalisches Kopieren der Daten unnötig sei und es genügen könne, nur die Verwaltungsdaten für den Datenträger-Manager des Ziel-Systems zu aktualisieren.


Eine solche Bedingung soll anmeldungsgemäß dann vorliegen, wenn die benutzten Datenblöcke im Quellsystem „nicht in einem außergewöhnlichen Datenlayout“
abgelegt seien. Dafür gibt die Anmeldung die Lehre (siehe Figur 7), bei einer Mig-

                                       -7-



ration zunächst zu prüfen, ob die „Abbildung zwischen logischen (Speicher-) Blöcken und physikalischen (Speicher-) Blöcken“, basierend auf „Datenträger-Konfigurationsinformation“, mit der „tatsächlichen Abbildung“ übereinstimmt (Schritt S7
in Verbindung mit den Schritten S3, S5). Die tatsächliche Abbildung könne angeblich abweichen, wenn z. B. ein „alternierender Block“ vorliege, in dem Sinne dass
ein auf dem physikalischen Medium defekter Block durch die Abbildung eines
anderen Blocks ersetzt wird (Offenlegungsschrift Absatz [0006]).


Nur wenn die beiden Abbildungen nicht übereinstimmen (Schritt S7: Nein-Zweig),
sollen die Daten des betroffenen Blocks zwischengepuffert werden (Schritt S9);
wenn sie jedoch übereinstimmen (Schritt S7: Ja-Zweig), kann der Schritt S9 übersprungen werden. Im nächsten Schritt S11 soll für beide Fälle die Datenträger-Konfigurationsinformation im Header durch den Datenträger-Manager des Ziel-Systems angepasst werden. Wenn Daten eines Blocks zwischengepuffert wurden
(Abfrage: Schritt S13), sollen diese im Schritt S15 durch den Datenträger-Manager
des Ziel-Systems zurückgeschrieben werden. Auch dieser Schritt kann jedoch
übersprungen werden, wenn nach der Abfrage im Schritt S7 keine Zwischenpufferung erfolgte.


Im Ergebnis brauchen also, wenn die beiden genannten Abbildungen übereinstimmen bzw. wenn „das außergewöhnliche Datenlayout nicht gemacht (d. h. erkannt?) wird“, die Daten nicht physikalisch umkopiert zu werden. Durch dieses
Vermeiden eines vollständigen Lesens und Zurückschreibens der Daten der Migrationsquelle, falls entsprechend günstige Bedingungen vorliegen, kann fraglos die
Geschwindigkeit der Datenmigration erhöht werden.


Als Fachmann, der mit der Aufgabe betraut wird, eine Datenträgermigration mit
hoher Geschwindigkeit zu ermöglichen, ist ein Systemprogrammierer oder Informatiker anzusehen, der im Bereich der Speicherverwaltungs-Programmierung für
Rechnersysteme mehrjährige Berufserfahrung besitzt.

                                       -8-



2.    Es kann dahinstehen, ob die vorliegend beanspruchte Erfindung überhaupt
ein konkretes technisches Problem löst, und ob alle Merkmale der Patentansprüche bei der Prüfung auf erfinderische Tätigkeit zu berücksichtigen wären (BGH
GRUR 2011, 125 - Wiedergabe topografischer Informationen). Denn die geltenden
Anträge weisen andere Mängel auf, die einer Patentierbarkeit im Wege stehen.


2.1   Dem Hauptantrag kann bereits deshalb nicht gefolgt werden, weil die
Lehre seines Patentanspruchs 1 an einer Stelle vom Gegenstand der Anmeldung
unzulässig abweicht (§ 38 PatG).


Merkmal (d) des Patentanspruchs 1 nach Hauptantrag lautet:


       (d)   nach einem Erkennen (Nein-Route bei Schritt S7), dass
             beurteilt wird, dass das außergewöhnliche Datenlayout nicht
             gemacht wird, nur Aktualisieren eines Headerbereichs auf
             dem physikalischen Medium (13) für den zweiten Datenträgermanager (7)


D. h. im Schritt S7 der Figur 7 soll, wenn erkannt wurde, dass kein „außergewöhnliches Datenlayout“ vorliegt, der Schritt S9 übersprungen und mit dem unmittelbar
folgenden Schritt S11 nur der Headerbereich aktualisiert werden (entsprechend
auch in der Beschreibung – Absatz [0044] der Offenlegungsschrift).


Dies ist in Figur 7 aber ersichtlich die „Ja-Route bei Schritt S7“. Anspruchsmerkmal (d) steht daher im Widerspruch zur in Bezug genommenen Figur 7. Die
Ergänzung „(Nein-Route bei Schritt S7)“ erfolgte mit Eingabe vom 22. April 2009
und stellt somit eine unzulässige Änderung dar.


Mit dem Patentanspruch 1 fällt der gesamte Hauptantrag, da über einen Antrag
nur einheitlich entschieden werden kann.

                                        -9-



2.2   Auch der Hilfsantrag muss ohne Erfolg bleiben, weil die Lehre seines Patentanspruchs 1 in der Anmeldung nicht so deutlich und vollständig offenbart ist,
dass ein Fachmann sie ausführen könnte (§ 34 Abs. 4 PatG).


Wie bereits erläutert, besteht ein wesentliches Merkmal der beanspruchten Lehre
in der Prüfung, ob die „Abbildung zwischen logischen (Speicher-) Blöcken und
physikalischen (Speicher-) Blöcken“, basierend auf „Datenträger-Konfigurationsinformation“, mit der „tatsächlichen Abbildung“ übereinstimmt (Figur 7: Schritt S7 in
Verbindung mit den Schritten S3, S5).


Um letztere „tatsächliche Abbildung“ zu erhalten, soll der erste Datenträgermanager veranlasst werden, tatsächliche Zugriffe auf das physikalische Medium durchzuführen (Merkmal (b') des Patentanspruchs 1 nach Hilfsantrag). Dann sollen
jedoch die tatsächlichen Zugriffe des ersten Datenträgermanagers durch ein Programmmodul unterbrochen bzw. blockiert werden, „um ein von dem ersten Datenträgermanager (3) durchgeführtes Abbilden (S5) … zwischen Abständen eines
logischen Datenträgers und physikalischen Blöcken auf dem physikalischen Medium“ zu erzeugen (Merkmal (e‘) des Patentanspruchs 1 nach Hilfsantrag).


Was genau damit gemeint ist und wie das gesuchte Abbild entstehen könnte,
bleibt dabei rätselhaft. Die Beschreibung hilft hier nicht weiter: Zwar sollte gemäß
Absatz [0039] die konkrete Durchführung anhand der Figuren 8 und 9 sowie der
zugehörigen Absätze [0040] bis [0043] erläutert werden. An keiner Stelle ist dort
aber deutlich dargelegt, wieso durch das Unterbrechen der tatsächlichen Zugriffe
(Merkmal (e‘)) ein Abbild der Zuordnung erstellt werden könnte. Der Fachmann ist
gehalten, hier Vermutungen anzustellen - etwa derart, dass die gewünschte Zuordnungstabelle im Datenträgermanager vorliegt und durch die in Auftrag gegebenen, jedoch nicht ausgeführten Zugriffe „irgendwie“ verfügbar gemacht werden
könnte. Eine „unmittelbare und eindeutige“ Offenbarung (vgl. BGH GRUR 2010,
910 - Fälschungssicheres Dokument) dafür, wie der Fachmann hier vorgehen soll,
liefert die Anmeldung jedoch nicht.

                                           - 10 -



Möglicherweise müsste die gewünschte Abbildung aber auch allein durch den
zusätzlichen „Umfangsextraktionstreiber 5“, also durch ein speziell dafür eingerichtetes Programm-Modul, erzeugt werden (siehe Absatz [0039]). Dann ist jedoch rätselhaft, warum Datenzugriffe zuerst in Auftrag gegeben und danach blockiert werden - ein zusätzliches Programm-Modul sollte auch ohne solche „Programmiertricks“ in der Lage sein, eine vom Datenträgermanager benutzte Zuordnungstabelle einfach auszulesen.


Allein aufgrund der Angaben in der Anmeldung, und auch bei Rückgriff auf sein
allgemeines Fachwissen, ist der Fachmann nach alledem nicht in der Lage, das
beanspruchte Datenträgermigrationsverfahren durchzuführen.


Mit dem Patentanspruch 1 fällt auch hier der gesamte Hilfsantrag, da über einen
Antrag nur einheitlich entschieden werden kann.


2.3      Die genannten (und weitere) Mängel von Haupt- und Hilfsantrag wurden der
Anmelderin zusammen mit der Ladung zur mündlichen Verhandlung übermittelt.
Sie hat sich hierzu jedoch nicht mehr geäußert und ist zur mündlichen Verhandlung nicht erschienen.




                                  Rechtsmittelbelehrung

Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

      1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
      2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
         Erfolg abgelehnt war,
      3. einem Beteiligten das rechtliche Gehör versagt war,
      4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,

                                       - 11 -



   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
      Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                 Eder                Baumgardt                 Hoffmann




                                                                                  Fa
