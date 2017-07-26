---
ecli: "ECLI:DE:BPatG:2017:260717B18Wpat179.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 179/14"
decided: "2017-07-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=32&nr=29251&anz=809&pos=481&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-07-26_18_W-pat_179_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 179/14 vom 2017-07-26

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 179/14                                                Verkündet am
_______________                                                   26. Juli 2017
    (Aktenzeichen)                                                      …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 11 2005 002 390.7 - 53


…




hat der 18. Senat (Techn. Beschwerdesenat) des Bundespatentgerichts auf die
mündliche Verhandlung vom 26. Juli 2017 durch die Vorsitzende Richterin
Dipl.-Ing. Wickborn sowie die Richter Kruppa, Dipl.-Phys. Dr. Schwengelbeck und
Dipl.-Ing. Altvater




BPatG 154
05.11

                                        -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                   Gründe


                                         I.


Die vorliegende Patentanmeldung 11 2005 002 390.7 geht aus einer PCT-Anmeldung (veröffentlicht als WO 2006/057963 A2) hervor, die am 17. November 2005 unter Inanspruchnahme der US-amerikanischen Priorität 10/995,850
vom 22. November 2004 eingereicht wurde. Die Anmeldung trägt die Bezeichnung


„Burst-Betrieb für die Speichertransaktion und Speicherkomponenten, welche die
         zeitweilig multiplexierte Fehlerkorrekturcodierung unterstützen“


und wurde mit Beschluss durch die Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts in der Anhörung vom 12. Dezember 2012
zurückgewiesen, weil die Gegenstände der jeweiligen Patentansprüche 1 nach
dem damaligen Hauptantrag und den damaligen Hilfsanträgen 1 bis 3 unter
Berücksichtigung des aus Druckschrift


       D5: US 6 493 789 B2


bekannten Standes der Technik nicht auf einer für die Patentfähigkeit erforderlichen erfinderischen Tätigkeit beruhen würden.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.

                                            -3-



Mit der Ladung vom 23. Mai 2017 zur mündlichen Verhandlung ist die Anmelderin
im Ladungszusatz unter anderem darauf hingewiesen worden, dass die am
20. März 2013 mit der Beschwerdebegründung eingegangenen unabhängigen
Patentansprüche nach Haupt- und Hilfsantrag möglicherweise Merkmale beinhalten, die in unzulässiger Weise über den Inhalt der Anmeldung in der
ursprünglichen Fassung hinausgehen.


In der mündlichen Verhandlung hat die Anmelderin die Patentanmeldung mit
unveränderten Anspruchsfassungen gemäß Haupt- und Hilfsantrag verteidigt.


Die Anmelderin beantragt,


     den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
     Patent- und Markenamts vom 12. Dezember 2012 aufzuheben und
     das Patent auf der Grundlage der folgenden Unterlagen zu erteilen:


     -    Patentansprüche 1 bis 6, eingegangen am 20. März 2013,
          hilfsweise
          Patentansprüche 1 und 2, eingegangen am 20. März 2013,


     -    Beschreibung,    Seiten    1 bis 3,     5 bis 18,   eingegangen   am
          27. März 2007, Seiten 4 und 4a, eingegangen am 19. Mai 2008,


     -    Figuren 1 bis 7, eingegangen am 27. März 2007.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1
gemäß Hauptantrag lautet:


Ma       „Speichervorrichtung (700), mit:

                                       -4-



Mb   einer Speicherzellenanordnung (790), die so angeordnet ist, daß sie Daten
     in mehreren adressierbaren Segmenten von Speicherzellen speichert,
     wobei jedem adressierbaren Segment wenigstens eine indirekt zugreifbare
     Speicherzelle zum Speichern von Fehlerkorrekturkodierdaten zugewiesen
     ist;


Mc   einem Modusregister,
     um Information zu speichern, die einen Fehlerkorrektur-Burst-Modus für die
     Speichervorrichtung anzeigt,
     um Daten gemäß einem vorab festgelegten Datenzyklusformat auszutauschen, das eine zeitliche Abfolge einer ersten Vielzahl von Datenzyklen
     enthält;


Md   einem Burst-Controller (750),
     um in dem Fehlerkorrektur-Burst-Modus eine Sequenzierung eines Lese-Bursts zu steuern, die enthält:
     Daten, die aus einem ersten Segment der mehreren adressierbaren
     Segmente von Speicherzellen gelesen wurden; und
     Fehlerkorrekturkodierdaten, die aus der wenigstens einen indirekt zugreifbaren Speicherzelle, die dem ersten Segment zugewiesen ist, gelesen
     wurden;


Me   einer Schreibschaltung, die mit der Speicherzellenanordnung gekoppelt ist,
     wobei der Burst-Controller weiter in dem Fehlerkorrektur-Burst-Modus eine
     Verteilung von Eingangsdaten steuert, die von Dateneingängen der Speichervorrichtung in einem ersten Schreib-Burst von einem Speichercontroller, der mit der Speichervorrichtung (700) gekoppelt ist, empfangen
     wurden,
     wobei der Burst-Controller der Schreibschaltung signalisiert, Daten des
     Schreib-Bursts an ein zweites der adressierbaren Segmente von Speicherzellen zu schreiben,

                                       -5-



      wobei gemäß dem vorab definierten Datenzyklusformat ein erster Datenzyklus des Schreib-Bursts zum Übertragen von Fehlerkorrekturkodierdaten
      von dem Speichercontroller zu der Speichervorrichtung (700) dient; und


Mf    einer Schreib-Maskierschaltung, die mit dem Burst-Controller gekoppelt ist,
      wobei die Schreib-Maskierschaltung basierend auf einem durch einen
      Datenmaskiereingang der Speichervorrichtung von dem Speichercontroller
      empfangenen Maskiersignal betreibbar ist,
      wobei    sich    der   Datenmaskiereingang    von   den    Dateneingängen
      unterscheidet,
      wobei in dem Fehlerkorrektur-Burst-Modus das Maskiersignal, wenn es
      während des Schreib-Bursts festgestellt wird, bewirkt, dass die Schreib-Maskierschaltung verhindert, dass die Schreibschaltung in dem ersten
      Datenzyklus gesendete Fehlerkorrekturkodierdaten, die in dem ersten
      Datenzyklus des Schreibbursts gesendet wurden, an eine indirekt
      zugreifbare Speicherzelle schreibt, die dem zweiten Segment zugewiesen
      ist.“


Wegen des Wortlauts des nebengeordneten Anspruchs 5 und der Unteransprüche
2 bis 4 und 6 wird auf die Akte verwiesen.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1
gemäß Hilfsantrag lautet:


M1    „Speichervorrichtung (700), umfassend:


M2    eine Vielzahl von Speicherzellen;


M3    eine Vielzahl von Dateneingängen,
M3.1 die eingerichtet sind, mittels Zeitmultiplexing Daten und den Daten
      entsprechende Fehlerkorrekturkodierdaten zu empfangen;

                                      -6-



M4    einen Datenmaskiereingang
M4.1 zum Empfangen eines Datenmaskiersignals, das anzeigt, ob Daten oder
      Fehlerkorrekturkodierdaten, die an den Dateneingängen liegen, gespeichert
      werden sollen; und


M5    einen Burst-Controller,
M5.1 der eingerichtet ist, während eines Schreib-Bursts übertragene Daten oder
      Fehlerkorrekturkodierdaten in die Vielzahl von Speicherzellen zu schreiben
      oder ein Schreiben zu verhindern,
M5.2 wobei der Burst-Controller ferner eingerichtet ist, anhand des Datenmaskiersignals über Schreiben oder Nichtschreiben von Daten oder
      Fehlerkorrekturkodierdaten zu entscheiden.“


Wegen des Wortlauts des nebengeordneten Anspruchs 2 wird auf die Akte
verwiesen.


Die Beschwerdeführerin führt aus, dass die geltenden Ansprüche zulässig, die
Gegenstände der geltenden Ansprüche dem Patentschutz zugänglich und im
Lichte des im Verfahren befindlichen Standes der Technik patentfähig seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                       II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn die Gegenstände
der jeweiligen Patentansprüche 1 nach Haupt- und Hilfsantrag wurden gegenüber
dem Inhalt der Anmeldung in der ursprünglichen Fassung unzulässig erweitert
(§ 38 Satz 1 PatG). Die Frage der Patentfähigkeit der Ansprüche im Hinblick auf
die §§ 1 bis 5 PatG kann somit dahinstehen (vgl. BGH, Urteil vom 18. Sep-

                                        -7-



tember 1990 – X ZR 29/89, GRUR 1991, 120, 121 li. Sp. Abs. 3 - Elastische
Bandage).


1. Die Anmeldung betrifft digitale Speichersysteme und -komponenten, die eine
  multiplexierende Fehlerkorrektur beim Codieren von Daten in einer impulsartigen Speichertransaktion ermöglichen (vgl. geltende Beschreibung, S. 1,
  le. Abs.).


  Die Anmeldung geht davon aus, dass Prozessoren bzw. Mikroprozessoren ein
  Computerspeicher-Untersystem benutzen, um Daten und Prozessorbefehle zu
  speichern. Diese Computerspeicher-Untersysteme würden oftmals implementiert, indem Speichermodule verwendet würden. Typischerweise würden Speichermodule aus einer Vielzahl von Halbleiter-Speichervorrichtungen aufgebaut,
  wobei jede einzelne Vorrichtung einen Teil jedes Datenwortes speichert, das
  auf dem Modul gespeichert werde. Viele gegenwärtige Speichervorrichtungen
  und Controller böten einen Burst-Modus an, der es erlaube, dass auf mehrere
  aufeinanderfolgende Datenwörter mit einem einzigen Befehl zugegriffen werden
  könne.
  Nicht alle Systeme nutzten einen ECC-(Error Correcting Coding) Schutz, da ein
  ECC-Schutz einen breiteren Datenbus und üblicherweise einen zusätzlichen
  Speicherchip pro Speicherrank erfordere. Weiter erhöhe ECC im Allgemeinen
  die Wartezeit aufgrund einer Fehlerprüffunktion und den Energieverbrauch
  aufgrund eines zusätzlich erforderlichen Chips. Dabei seien ECC- und Nicht-EEC-Speichermodule       nicht   untereinander    austauschbar   (vgl.   geltende
  Beschreibung, S. 2, 1. Abs. bis S. 4, 3. Abs.).


  Gemäß Eingabe vom 6. November 2012 (S. 4, erster Abs.) wird als Aufgabe
  angesehen, die Effizienz einer Fehlerkorrektur bei Verwendung einer einzelnen
  Leitung zu steigern.

                                     -8-



  Den geltenden Ansprüchen gemäß Haupt- und Hilfsantrag dürfte die objektive
  Problemstellung zu Grunde liegen, den Ressourcenbedarf bei ECC-Speichermodulen zu verringern und eine Austauschbarkeit mit Nicht-ECC-Modulen
  zu ermöglichen.


  Der zuständige Fachmann weist eine abgeschlossene Hochschulausbildung auf
  dem Gebiet der Elektrotechnik auf und verfügt über Erfahrung auf dem Gebiet
  von Speichermodulen mit Fehlerkorrektur (ECC-Speichermodule).


  Die vorstehend genannte Aufgabe soll gemäß Hauptantrag mit den Merkmalen
  der nebengeordneten Ansprüche 1 und 5 sowie gemäß Hilfsantrag mit den
  Merkmalen der nebengeordneten Ansprüche 1 und 2 gelöst werden.


  Nach Anspruch 1 gemäß Hauptantrag ist eine Speichervorrichtung mit einer
  Speicherzellenanordnung     (Merkmalsgruppe Mb),     einem      Modusregister
  (Merkmalsgruppe Mc), einem Burst-Controller (Merkmalsgruppe Md), einer
  Schreibschaltung (Merkmalsgruppe Me) und einer Schreib-Maskierschaltung
  (Merkmalsgruppe Mf) als Merkmale der Anordnung vorgesehen.


  Anspruch 1 gemäß Hilfsantrag sieht eine Speichervorrichtung vor, die eine
  Vielzahl von Speicherzellen (Merkmalsgruppe M2), eine Vielzahl von Dateneingängen (Merkmalsgruppe M3), einen Datenmaskiereingang (Merkmalsgruppe M4) und einen Burst-Controller (Merkmalsgruppe M5) als Anordnungsmerkmale aufweist.




2. Die jeweiligen Ansprüche 1 nach Haupt- und Hilfsantrag beinhalten Änderungen
  gegenüber dem Inhalt der Anmeldung in der ursprünglichen Fassung, die den
  Anmeldungsgegenstand unzulässig erweitern (§ 38 Satz 1 PatG).

                                    -9-



a)   Zum Hauptantrag


Der auf eine Speichervorrichtung gerichtete Anspruch 1 gemäß Hauptantrag
sieht in der Merkmalsgruppe Mc ein Modusregister vor, um Information zu
speichern, die einen Fehlerkorrektur-Burst-Modus für die Speichervorrichtung
anzeigt, um Daten gemäß einem vorab festgelegten Datenzyklusformat auszutauschen, das eine zeitliche Abfolge einer ersten Vielzahl von Datenzyklen
enthält.


Mit der Ladung zur mündlichen Verhandlung hat der Senat darauf hingewiesen,
dass ein Modusregister in der ursprünglichen Beschreibung nur an zwei Stellen
erwähnt ist, die jeweils vom vorliegenden Anspruchsinhalt abweichen. So ist ein
Modusregister als „ein Teil der Adreß- und Steuerlogik“ vorgesehen, dessen
Werte „auf den Signaleingängen ADD empfangen und durch das Adreßregister
720 gesperrt“ werden (vgl. deutsche Übersetzung der ursprünglich eingereichten PCT-Anmeldung vom 27. März 2007, Fig. 7 mit Beschreibung, S. 13,
le. Abs.; sowie entsprechende Textstelle der Veröffentlichung der PCT-Anmeldung als WO 2006/057963 A2, S. 11, vorl. Abs.). Außerdem ist ein
Modusregister für den Fall beschrieben, dass kein Datenmaskiereingang
verwendet   wird,   wobei   abweichend    vom    vorliegenden   Anspruch    ein
„Modulpositionsregister“ und eine Vergleichslogik für dessen Vergleich mit dem
angeforderten „Spaltenadreßbereich“ vorgesehen sind (vgl. deutsche Übersetzung der Anmeldung, Seite 11 bis 12, seitenüberbrückender Absatz; sowie
Veröffentlichung der PCT-Anmeldung, Seite 9 bis 10, seitenüberbrückender
Absatz). Die Funktion eines Modusregisters ist in den ursprünglich eingereichten Anmeldeunterlagen ausschließlich im Zusammenhang mit diesen
beiden Ausführungsformen offenbart.


Die Anmelderin hat in der mündlichen Verhandlung mit Verweis auf die
deutsche Fassung der Anmeldeunterlegen behauptet, dass ein Modusregister
gemäß Merkmalsgruppe Mc in der vorstehend genannten Textstelle des letzten

                                      - 10 -



Absatzes der Seite 11 klar erkennbar sei, da dessen Realisierung dem Belieben
des Fachmanns überlassen bleibe und die Textstelle keine weiteren Komponenten umfasse.
Dieser Argumentation kann sich der Senat nicht anschließen, da die zitierte
Textstelle auf ein „Modulpositionsregister“ und eine Vergleichslogik zur Verwendung des Modusregisters bei der Realisierung eines Fehlerkorrektur-Burst-Modus verweist. Zudem bezieht sich die genannte Textstelle auf eine Ausführungsvariante, in der im Unterschied zum vorliegenden Anspruch 1
ausdrücklich kein Datenmaskiereingang (DM-Signaleingänge) und somit kein
Datenmaskiersignal verwendet wird (vgl. Merkmalsgruppe Mf).


Die Kombination der Merkmalsgruppe Mc mit den weiteren Anspruchsmerkmalen ist den ursprünglich eingereichten Unterlagen damit nicht zu entnehmen.


b) Zum Hilfsantrag


Anspruch 1 gemäß Hilfsantrag sieht neben einer Vielzahl von Speicherzellen
(Merkmal M2), einer Vielzahl von Dateneingängen (Merkmal M3) und einem
Datenmaskiereingang (Merkmal M4) gemäß Merkmalsgruppe M5 einen Burst-Controller vor. Dieser soll dazu eingerichtet sein, während eines Schreib-Bursts
übertragene Daten oder Fehlerkorrekturkodierdaten in die Vielzahl von
Speicherzellen zu schreiben oder ein Schreiben zu verhindern (vgl. Merkmal
M5.1)   sowie    anhand   des   Datenmaskiersignals     über   Schreiben   oder
Nichtschreiben von Daten oder Fehlerkorrekturkodierdaten zu entscheiden (vgl.
Merkmal M5.2).


Mit der Ladung zur mündlichen Verhandlung hat der Senat ebenfalls darauf
hingewiesen, dass die in der Beschwerdebegründung zur Offenbarung der
Merkmalsgruppe M5 angeführten Textstellen zu Figur 7 (vgl. deutsche
Übersetzung      der   ursprünglich     eingereichten   PCT-Anmeldung      vom
27. März 2007, Seite 13, Zeilen 11 bis 14 und 22 bis 25, sowie Seite 14,

                                   - 11 -



Zeilen 5 bis 8) einen Burst-Controller (bzw. „Burst/ECC-Controller/Zähler“) nur
in Verbindung mit einer „Adreß-und Steuerlogik“, einem „Adreßregister“, einer
„I/O-Ausblender-   und Maskenlogik“, „I/O-Registern und Empfänger“ und der
Verwendung von „Spaltenadressen“ und „Modusregisterwerten“ offenbaren,
welche allesamt keinen Niederschlag im vorliegenden Anspruch gefunden
haben.


Die Anmelderin hat hierzu in der mündlichen Verhandlung auf den zweiten
Absatz der Seite 12 der deutschen Übersetzung der ursprünglich eingereichten
Beschreibung verwiesen (vgl. auch Veröffentlichung der PCT-Anmeldung als
WO 2006/057963 A2, S. 10, 2. Abs.), nach dem mehrere der zu Figur 7
genannten Komponenten („Blöcke“) Durchschnittsfachleuten vertraut seien.
Diese bekannten Komponenten bräuchten daher im Anspruch 1 nach Hilfsantrag nicht weiter angegeben werden, zumal auch nicht alle genannten Komponenten erfindungswesentlich seien.


Dieser Auffassung der Anmelderin kann der Senat nicht beitreten, da bereits
der zweite Teil des von der Anmelderin zitierten Satzes auf Seite 12 der
deutschen Übersetzung der ursprünglichen Beschreibung darauf verweist, dass
andere dieser zu Figur 7 genannten Blöcke modifiziert seien, um mit dem
beschriebenen Fehlerkorrektur-Burstbetrieb in Einklang zu sein. Dies betrifft
zumindest die - im Anspruch nicht erwähnten - Komponenten „I/O-Ausblenderund Maskenlogik“ und „I/O-Registern und Empfänger“, da diese Voraussetzung
für die Verwendung des Datenmaskiersignals beim Lesen und Schreiben der
anliegenden Daten in die Speicherzellen sind. Die ursprüngliche Beschreibung
dieser Komponenten gibt aufgrund des Datenmaskiersignals auch keinen
Anhaltspunkt dahingehend, dass es sich hier um von einem Fachmann
mitgelesene Standardkomponenten handelt. Dies wird insbesondere in Merkmal M5.2 deutlich, da der dort geforderte Zusammenhang zwischen dem
„Burst-Controller“ und dem „Datenmaskiersignal“ gemäß der ursprünglichen
Beschreibung ausschließlich über die „I/O-Registern und Empfänger“ oder

                                    - 12 -



indirekt über den „Spaltendecodierer“ und die „I/O-Ausblender-und Maskenlogik“ besteht (vgl. deutsche Übersetzung der Anmeldung bzw. Veröffentlichung
der PCT-Anmeldung, Figur 7 mit zugehörigem Text). Diese im vorliegenden
Anspruch nicht genannten Komponenten sind damit die Voraussetzung dafür,
dass   der   Burst-Controller   überhaupt    in   der   Lage   ist,   „anhand   des
Datenmaskiersignals“ über ein Schreiben oder Nichtschreiben von Daten oder
Fehlerkorrekturkodierdaten zu entscheiden.


Die in der mündlichen Verhandlung von der Anmelderin als Beleg für ein
solches Entscheiden des Burst-Controllers über Schreiben oder Nichtschreiben
von Daten oder Fehlerkorrekturkodierdaten angeführte Textstelle bezieht sich
auf ein Setzen des ECC-Adressüberschreibsignals (ECC-AO) (vgl. deutsche
Übersetzung der ursprünglichen Beschreibung, S. 16, le. Abs., 2. Satz; bzw.
Veröffentlichung der PCT-Anmeldung, S. 14, 2. Abs.). Dieses Signal dient dem
Burst-Controller zum Steuern des Spaltendekodierers, um damit nur indirekt
adressierbare Speicherzellen zum Schreiben oder Lesen von Fehlerkorrekturkodierdaten anzusteuern (vgl. deutsche Übersetzung der ursprünglichen
Beschreibung, S. 16, le. Abs., i. V. m. S. 15, 2. Abs. bis S. 16, 3. Abs.; bzw.
Veröffentlichung der PCT-Anmeldung, S. 14, 2. Abs. i. V. m. S. 13, 1. Abs. bis
S. 14, 1. Abs.). Damit beschreibt die zitierte Textstelle jedoch nicht, dass
entsprechend Merkmal M5.2 durch den Burst-Controller „anhand des
Datenmaskiersignals über Schreiben oder Nichtschreiben von Daten oder
Fehlerkorrekturkodierdaten“ entschieden wird (Unterstreichung hinzugefügt).
Vielmehr zeigt diese Textstelle weitere Merkmale der Speichervorrichtung
(Signal ECC-AO mit daran angepasstem Spaltendekodierer), die Voraussetzungen für die beanspruchte Funktion des Burst-Controllers sind.


Das Weglassen der vorstehend genannten Komponenten der Speichervorrichtung in Anspruch 1 gemäß Hilfsantrag, welche der ursprünglichen Beschreibung als wesentlich für die Funktion des Burst-Controllers bei einer
Datenmaskierung gemäß der Merkmalsgruppe M5 bzw. Merkmal M5.2 zu

                                       - 13 -



  entnehmen sind, stellt daher einen in unzulässiger Weise verallgemeinerten
  Zusammenhang dar, der über den Inhalt der ursprünglichen Offenbarung
  hinausgeht.




3. Es kann dahingestellt bleiben, ob die weiteren Merkmale der jeweiligen
  Ansprüche 1 nach Haupt- und Hilfsantrag oder Merkmale nach Anspruch 5
  gemäß Hauptantrag oder Anspruch 2 gemäß Hilfsantrag, die ebenfalls
  Änderungen gegenüber dem jeweiligen ursprünglich eingereichten Ansprüchen
  beinhalten, in den ursprünglichen Anmeldungsunterlagen offenbart sind.




4. Mit den jeweils nicht zulässigen Ansprüchen 1 nach Haupt- und Hilfsantrag sind
  auch die weiteren Ansprüche nach Haupt- und Hilfsantrag nicht schutzfähig, da
  auf diese Ansprüche kein eigenständiges Schutzbegehren gerichtet war (BGH,
  Beschluss vom 27. Juni 2007 - X ZB 6/05; GRUR 2007, 862 Abs. III 3. a) aa) –
   Informationsübermittlungsverfahren II).




5. Bei dieser Sachlage war die Beschwerde zurückzuweisen.




                                         III.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht der am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                        - 14 -



1.    das beschließende Gericht nicht vorschriftsmäßig besetzt war,
2.    bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
      Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
      Befangenheit mit Erfolg abgelehnt war,
3.    einem Beteiligten das rechtliche Gehör versagt war,
4.    ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
      war, sofern er nicht der Führung des Verfahrens ausdrücklich oder
      stillschweigend zugestimmt hat,
5.    der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
      der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
      sind, oder
6.    der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.


Wickborn             Kruppa                 Dr. Schwengelbeck           Altvater




                                                                              Me
