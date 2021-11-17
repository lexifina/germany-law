---
ecli: "ECLI:DE:BPatG:2021:171121B17Wpat8.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 8/20"
decided: "2021-11-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=35&nr=42171&anz=599&pos=532&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2021-11-17_17_W-pat_8_20_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 8/20 vom 2021-11-17

## Entscheidung

BUNDESPATENTGERICHT


    17 W (pat) 8/20
_______________
    (Aktenzeichen)




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 11 2011 104 419.4
…
hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
17. November 2021 unter Mitwirkung des Vorsitzenden Richters Dipl.-
Phys. Dr. Morawek, der Richterin Bayer, des Richters Dipl.-Ing. Baumgardt und
des Richters Dipl.-Ing. Hoffmann




ECLI:DE:BPatG:2021:171121B17Wpat8.20.0

                                      -2-




beschlossen:


Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle
für Klasse G06F des Deutschen Patent- und Markenamts vom 31. Juli
2018 aufgehoben und das Patent mit folgenden Unterlagen erteilt:


Patentansprüche 1 bis 14 vom 11. Oktober 2021,
Beschreibung Seiten 1 bis 21, sowie 4 Blatt Zeichnungen mit Figuren 1 bis
5 jeweils vom 07. September 2021.




                                    Gründe


                                       I.


Die vorliegende Patentanmeldung ist eine PCT-Anmeldung in nationaler Phase,
welche als WO 2012 / 080001 A1 in Englisch und als DE 11 2011 104 417 T5 in
deutscher Übersetzung veröffentlicht wurde. Ihr PCT-Anmeldetag ist der 02.
Dezember 2011. Sie nimmt die Priorität einer US-Voranmeldung vom 16.
Dezember 2010 in Anspruch und trägt in der deutschen Übersetzung die
Bezeichnung:


                 „Bereichsmigration für gepaarte Speicherung“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes in der Anhörung am 31. Juli 2018 mit der Begründung
zurückgewiesen, dass der Gegenstand des Patentanspruchs 1 nach Hauptantrag,

                                           -3-



sowie dem Hilfsantrag 1, soweit sie ein technisches Problem mit technischen
Mitteln lösen, nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie hat ihr
Patentbegehren überarbeitet und die Beschreibung angepasst. Sie stellt nunmehr
den Antrag,


      den Beschluss der Prüfungsstelle vom 31. Juli 2018 aufzuheben und ein
      Patent mit folgenden Unterlagen zu erteilen:
      Patentansprüche 1 bis 14 vom 11. Oktober 2021,
      Beschreibung Seiten 1 bis 21 und
      4 Blatt Zeichnungen mit Figuren 1 bis 5
      jeweils vom 07. September 2021.


Das geltende Patentbegehren, hier beim Anspruch 1 mit einer denkbaren
Gliederung versehen, lautet:


M1    1. Verfahren für die Bereichsmigration durch eine Prozessoreinheit in einer
      Datenspeicherumgebung, die für synchrone Replikation zwischen einem
      Paar aus Primär- und Sekundärspeicherentität konfiguriert ist, die jeweils
      mehrschichtige     Speichereinheiten       besitzen,   wobei   die   Ebenen   der
      mehrschichtigen Speichereinheiten jeweils in einer Speicherhierarchie
      organisiert sind, welche zumindest einer Leistungsmaßzahl entspricht und
      deren höchste Ebene einem höchsten Wert der zumindest einen
      Leistungsmaßzahl entspricht, aufweisend:


M2    Identifizieren eines Bereichs als einen Kandidaten für Bereichsmigration
      aufgrund     mindestens      eines     Speicheraktivitätsfaktors     durch    die
      Primärspeicherentität,

                                              -4-



M3   Berechnen einer relativen Priorität des zu migrierenden Bereichs auf der
     Grundlage     einer     geordneten        Primär-Heat-Map       der    mehrschichtigen
     Speichereinheiten der Primärspeicherentität,
M4   wobei die Primärspeicherentität eine Zuordnung der relativen Priorität zu
     einer      Ebene        der        mehrschichtigen          Speichereinheiten      der
     Primärspeicherentität       auf    der    Grundlage     des    Speichersystems     der
     Primärspeicherentität berechnet,


M5   Senden einer Migrationsanweisung durch die Primärspeicherentität an die
     Sekundärspeicherentität,


     M5.1 wobei die Migrationsanweisung die relative Priorität des zu
             migrierenden Bereichs enthält;


     M5.2 wobei die Primär- und Sekundärspeicherentitäten dieselbe oder eine
             unterschiedliche          hierarchisch      organisierte       Struktur   von
             mehrschichtigen Speichereinheiten umfassen,


     M5.3 wobei die Sekundärspeicherentität eine Zuordnung der relativen
             Priorität zu einer Ebene der mehrschichtigen Speichereinheiten der
             Sekundärspeicherentität auf der Grundlage des Speichersystems der
             Sekundärspeicherentität berechnet,


     M5.4 Empfangen einer Antwort der Sekundärspeicherentität durch die
             Primärspeicherentität, wobei die Antwort die berechnete Ebene der
             mehrschichtigen       Speichereinheiten       der     Sekundärspeicherentität
             angibt,


     M5.5 wobei die Primärspeicherentität die Migration des zu migrierenden
             Bereichs      auf   die     zugeordnete      Ebene     der     mehrschichtigen
             Speichereinheiten           der        Primärspeicherentität       und     die

                                         -5-



            Sekundärspeicherentität die Migration des zu migrierenden Bereichs
            auf die zugeordnete Ebene der mehrschichtigen Speichereinheiten
            der    Sekundärspeicherentität         durchführt,        falls   die    beiden
            zugeordneten Ebenen identisch sind,


     M5.6 wobei die Primärspeicherentität und die Sekundärspeicherentität den
            zu    migrierenden    Bereich      jeweils    auf    diejenige    der    beiden
            zugeordneten Ebenen verschieben, welcher einer niedrigeren
            Leistungsmaßzahl entspricht, falls die beiden zugeordneten Ebenen
            unterschiedlich sind und das Verschieben auf diejenige der beiden
            zugeordneten Ebenen, welcher die niedrigere Leistungsmaßzahl
            entspricht, eine Leistungssteigerung ergibt.


2.   Verfahren nach Anspruch 1, wobei die Migrationsanweisung weiterhin eine
     Zeitverzögerung enthält, deren Ende annähernd gleich einer Zeit der
     beabsichtigten Migration auf der Primärspeicherentität ist, die für eine
     Übertragungszeit     so   abgestimmt       ist,     dass   die    Primär-      und   die
     Sekundärspeicherentitäten die Bereichsmigration zu annähernd derselben
     Zeit durchführen.


3.   Verfahren nach Anspruch 2, weiterhin beinhaltend ein Konfigurieren der
     Migrationsanweisung mit mindestens einem von einem Nachrichtentypfeld,
     einem Bereichskennungsfeld, einem Zeitverzögerungsfeld, in dem die
     Zeitverzögerung enthalten ist, einem Zielebenennummern-Feld und einem
     Feld einer relativen Priorität.


4.   Verfahren nach Anspruch 1, weiterhin beinhaltend bei Empfang der
     Migrationsanweisung durch die Sekundärspeicherentität:
     der Primärspeicherentität diejenige Speichereinheit der mehrstufigen
     Speichereinheiten der Sekundärspeicherentität zu bestätigen, auf welche
     der Bereich migriert werden soll.

                                             -6-




5.   Verfahren nach Anspruch 4, weiterhin beinhaltend ein Ermitteln durch die
     Primärspeicherentität         auf     der     Grundlage        der     Bestätigung      der
     Sekundärspeicherentität, ob die Bereichsmigration auf die bestätigte
     Speichereinheit der mehrstufigen Speichereinheiten durchzuführen ist.


6.   Verfahren nach Anspruch 5, wobei das Ermitteln, ob die Bereichsmigration
     durchzuführen ist, ein Berücksichtigen von mindestens einem von einem
     Lese/Schreib-Verhältnis, einem Verhältnis sequenzieller Zugriffe zu nichtsequenziellen Zugriffen und einer Anforderung der Dienstgüte beinhaltet.


7.   System für die Bereichsmigration in einer Datenspeicherumgebung, die für
     synchrone    Replikation        zwischen        einem     Paar        aus     Primär-   und
     Sekundärspeicherentität         konfiguriert     ist,   die    jeweils       mehrschichtige
     Speichereinheiten besitzen, wobei die Ebenen der mehrschichtigen
     Speichereinheiten jeweils in einer Speicherhierarchie organisiert sind,
     welche zumindest einer Leistungsmaßzahl entspricht und deren höchste
     Ebene einem höchsten Wert der zumindest einen Leistungsmaßzahl
     entspricht, wobei das System aufweist:
     mindestens     ein       in     der         Datenspeicherumgebung              betreibbares
     Speicherverwaltungsmodul,               wobei           das          mindestens         eine
     Speicherverwaltungsmodul konfiguriert ist zum:
     Identifizieren eines Bereichs als einen Kandidaten für Bereichsmigration
     aufgrund     mindestens         eines        Speicheraktivitätsfaktors          durch    die
     Primärspeicherentität,
     Berechnen einer relativen Priorität des zu migrierenden Bereichs auf der
     Grundlage    einer   geordneten             Primär-Heat-Map      der        mehrschichtigen
     Speichereinheiten der Primärspeicherentität,
     wobei die Primärspeicherentität eine Zuordnung der relativen Priorität zu
     einer      Ebene     der            mehrschichtigen           Speichereinheiten         der

                                           -7-



     Primärspeicherentität     auf   der     Grundlage    des   Speichersystems    der
     Primärspeicherentität berechnet,
     Senden einer Migrationsanweisung durch die Primärspeicherentität an die
     Sekundärspeicherentität, wobei die Migrationsanweisung die relative
     Priorität enthält;
     wobei die Primär- und Sekundärspeicherentitäten dieselbe oder eine
     unterschiedliche hierarchisch organisierte Struktur von mehrschichtigen
     Speichereinheiten umfassen,
     wobei die Sekundärspeicherentität eine Zuordnung der relativen Priorität zu
     einer      Ebene        der     mehrschichtigen        Speichereinheiten      der
     Sekundärspeicherentität auf der Grundlage des Speichersystems der
     Sekundärspeicherentität berechnet,
     Empfangen       einer   Antwort    der      Sekundärspeicherentität   durch   die
     Primärspeicherentität, wobei die Antwort die berechnete Ebene der
     mehrschichtigen Speichereinheiten der Sekundärspeicherentität angibt,
     wobei die Primärspeicherentität die Migration des zu migrierenden Bereichs
     auf die zugeordnete Ebene der mehrschichtigen Speichereinheiten der
     Primärspeicherentität und die Sekundärspeicherentität die Migration des zu
     migrierenden Bereichs auf die zugeordnete Ebene der mehrschichtigen
     Speichereinheiten der Sekundärspeicherentität durchführt, falls die beiden
     zugeordneten Ebenen identisch sind,
     wobei die Primärspeicherentität und die Sekundärspeicherentität den zu
     migrierenden Bereich jeweils auf diejenige der beiden zugeordneten
     Ebenen     verschieben,       welcher    einer   niedrigeren   Leistungsmaßzahl
     entspricht, falls die beiden zugeordneten Ebenen unterschiedlich sind und
     das Verschieben auf diejenige der beiden zugeordneten Ebenen, welcher
     die niedrigere Leistungsmaßzahl entspricht, eine Leistungssteigerung
     ergibt.


8.   System nach Anspruch 7, wobei die Migrationsanweisung weiterhin eine
     Zeitverzögerung enthält, deren Ende annähernd gleich einer Zeit der

                                           -8-



      beabsichtigten Migration auf der Primärspeicherentität ist, die für eine
      Übertragungszeit     so    abgestimmt       ist,    dass        die   Primär-      und    die
      Sekundärspeicherentitäten die Bereichsmigration zu annähernd derselben
      Zeit durchführen.


9.    System       nach    Anspruch        8,         wobei      das        mindestens         eine
      Speicherverwaltungsmodul             weiterhin           konfiguriert           ist,      die
      Migrationsanweisung mit mindestens einem von einem Nachrichtentypfeld,
      einem Bereichskennungsfeld, einem Zeitverzögerungsfeld, in dem die
      Zeitverzögerung enthalten ist, einem Zielebenennummern-Feld und einem
      Feld einer relativen Priorität zu konfigurieren.


10.   System       nach    Anspruch        7,         wobei      das        mindestens         eine
      Speicherverwaltungsmodul weiterhin konfiguriert ist, bei Empfang der
      Migrationsanweisung         durch         die      Sekundärspeicherentität:              der
      Primärspeicherentität      diejenige       Speichereinheit            der     mehrstufigen
      Speichereinheiten der Sekundärspeicherentität zu bestätigen, auf welche
      der Bereich migriert werden soll.


11.   System       nach    Anspruch        10,        wobei      das        mindestens         eine
      Speicherverwaltungsmodul         weiterhin         konfiguriert        ist,   durch       die
      Primärspeicherentität      auf   der       Grundlage        der        Bestätigung       der
      Sekundärspeicherentität zu ermitteln, ob die Bereichsmigration auf die
      bestätigte     Speichereinheit       der         mehrstufigen          Speichereinheiten
      durchzuführen ist.


12.   System        nach        Anspruch         11,          wobei         mindestens          ein
      Speicherverwaltungsmodul weiterhin konfiguriert ist, gemäß dem Ermitteln,
      ob die Bereichsmigration durchzuführen ist, mindestens eines von einem
      Lese/Schreib-Verhältnis, einem Verhältnis sequenzieller Zugriffe zu nicht-

                                        -9-



       sequenziellen Zugriffen und einer Anforderung der Dienstgüte zu
       berücksichtigen.


13.    System     nach      Anspruch     7,    wobei:     das     mindestens      eine
       Speicherverwaltungsmodul als eine Speicherverwaltungsprozessor (storage
       management processor (SMP))-Einheit betreibbar ist, und die Primär- und
       die    Sekundärspeicherentitäten        mindestens       eine     von      einer
       Magnetbandebene, einer Festplattenlaufwerk (Enterprise HDD)-Ebene,
       einer Halbleiterlaufwerk (SSD)-Ebene und einer Cachespeicherebene zum
       Durchführen der Bereichsmigration zwischen ihnen enthalten.


14.    Computerprogrammprodukt         für    die   Bereichsmigration      in     einer
       Datenspeicherumgebung, die für synchrone Replikation zwischen einem
       Paar aus Primär- und Sekundärspeicherentität konfiguriert ist, die jeweils
       mehrschichtige     Speichereinheiten   besitzen,   wobei   die    Ebenen    der
       mehrschichtigen Speichereinheiten jeweils in einer Speicherhierarchie
       organisiert sind, welche zumindest einer Leistungsmaßzahl entspricht und
       deren höchste Ebene einem höchsten Wert der zumindest einen
       Leistungsmaßzahl entspricht, wobei das Computerprogrammprodukt ein
       computerlesbares       Speichermedium        mit     darauf      gespeicherten
       Programmcodeteilen        aufweist,     wobei      die        computerlesbaren
       Programmcodeteile bei Ausführen durch eine Prozessoreinheit den
       Computer veranlassen, das Verfahren nach einem der Ansprüche 1 bis 6
       auszuführen.




Dem Patentbegehren soll die Aufgabe zugrunde liegen, ein verbessertes
Verfahren zur Bereichsmigration zwischen einem Paar aus Primär- und
Sekundärspeicherentität zu schaffen (siehe geltende Beschreibung Seite 2 Z.27-
29).

                                         - 10 -




                                           II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
Erfolg, da das nunmehr geltende Patentbegehren durch den bekannt gewordenen
Stand der Technik nicht vorweggenommen oder nahegelegt ist und auch die
übrigen Kriterien für eine Patenterteilung erfüllt sind (PatG §§ 1 bis 5, § 34).


1.     Die vorliegende Erfindung betrifft die Bereichsmigration zwischen einem
Paar aus Primär- und Sekundspeicherentität.


Gemäß der Anmeldung (vgl. geltende Beschreibung Seite 1 Z.10 bis Seite 2 Z.8)
seien Computer überall anzutreffen, dabei erfolge die Speicherung der Daten
zunehmend in mehreren, teilweise von der angezeigten lokalen Oberfläche
entfernten, Speicherumgebungen. Die Speicherumgebungen könnten viele
verschiedene Speichereinheiten umfassen und große Datenmengen organisieren
und verarbeiten.
Aus dem Stand der Technik seien Systeme bekannt, welche unnötige
Dateimigrationen begrenzten. Derartige hierarchische Speichersysteme würden
eine Datei, auf die häufig zugegriffen werde, in eine obere Ebene und eine Datei,
auf die selten zugegriffen werde, in eine untere Ebene migrieren. Ebenso sei es
bekannt, die Hierarchie eines lokalen Speichersystems in einem Remote-Speichersystem widerzuspiegeln (vgl. geltende Beschreibung Seite 2 Z.9-24).


Mit   dem   Verfahren des      geltenden     Anspruchs    1   soll   eine   verbesserte
Bereichsmigration zwischen einem Paar aus Primär- und Sekundärspeicherentität
geschaffen werden.


Als Fachmann, der mit der Aufgabe betraut wird, ein derartiges Verfahren zu
entwickeln, ist ein Diplom-Ingenieur der Fachrichtung Datenverarbeitung oder ein
Physiker mit fundierten Kenntnissen auf dem Gebiet der Entwicklung von

                                     - 11 -



Speichercontrollern – insbesondere im Bereich der Speichermigrationstechnologie
– anzusehen.


2.    Der Erteilungsantrag liegt im Rahmen der ursprünglichen Offenbarung.


Anspruch 1 geht aus den ursprünglichen Ansprüchen 1 und 3 sowie aus der
ursprünglichen Beschreibung (S.7 Z.14 – S.8 Z.11, S.14 Z.25-32, S.10 Z.5-15,
S.12 Z.15-16, S.9 Z.10-20, S.27 Z.10-22, S.11 Z.10-12, S.13 Z.1-9, S.13 Z.16-29,
S.11 Z.18-22, S.5 Z.11-15) hervor.


Anspruch 2 basiert auf dem ursprünglichen Anspruch 2 sowie auf der
ursprünglichen Beschreibung (S.5 Z.11-15, S.11 Z.18-22).


Die Ansprüche 3 bis 6 entsprechen den ursprünglichen Ansprüchen 4 bis 7.


Anspruch 7 geht aus den ursprünglichen Ansprüchen 8 und 10 sowie aus der
ursprünglichen Beschreibung (S.7 Z.14 – S.8 Z.11, S.14 Z.25-32, S.10 Z.5-15,
S.12 Z.15-16, S.9 Z.10-20, S.27 Z.10-22, S.11 Z.10-12, S.13 Z.1-9, S.13 Z.16-29,
S.11 Z.18-22, S.5 Z.11-15) hervor.


Anspruch 8 basiert auf dem ursprünglichen Anspruch 9 sowie auf der
ursprünglichen Beschreibung (S.5 Z.11-15, S.11 Z.18-22).


Die Ansprüche 9 bis 13 entsprechen den ursprünglichen Ansprüchen 11 bis 15.


Anspruch 14 basiert auf dem ursprünglichen Anspruch 16 und auf der
ursprünglichen Beschreibung (S.7 Z.14-25).


Darüber hinaus wurden in den Ansprüchen redaktionelle Änderungen bzw.
Korrekturen vorgenommen.

                                       - 12 -



Die Beschreibung wurde an die nunmehr geltenden Ansprüche angepasst, der
Stand der Technik wurde aufgenommen und es wurden redaktionelle Änderungen
sowie Klarstelllungen eingefügt.


In der Figur 2 wurde ein Bezugszeichen ergänzt und in Figur 5 ein offensichtlicher
Fehler (Vertauschung der Ausgänge J/N des Bocks 218) korrigiert; die übrigen
Figuren wurden nicht geändert.




3.    Das geltende Patentbegehren ist durch den bisher bekannten Stand der
Technik weder vorbekannt noch nahegelegt.


Folgende Druckschriften wurden im Laufe des Verfahrens entgegengehalten:


D1:   US 2010/0274826 A1
D2:   EP 1 840 723 A2


Die Begründung der mangelnden Patentfähigkeit im angefochtenen Beschluss,
wonach der Gegenstand des Patentanspruchs 1 mangels erfinderischer Tätigkeit
– soweit dessen Merkmale bei der Prüfung auf erfinderische Tätigkeit zu
berücksichtigen seien – nicht gewährbar sei, stützt sich allein auf die Druckschrift
D1 und auf das Wissen des Fachmanns.
Dieser Begründung kann nicht gefolgt werden.
Denn die D1 zeigt eine Anordnung mit einem einzigen hierarchischen
Speichersystem,    welches    aus   mehreren    unterschiedlichen    Speichertypen
aufgebaut ist (Fig.1, Fig.2, Absätze [0041] und [0043]). Weiterhin zeigt die D1 das
Verschieben (Migrieren) von Dateien von einer unteren auf eine obere
Speicherhierarche bzw. von einer oberen auf eine untere Speicherhierarchie,
wobei die Häufigkeit des Aufrufs der Dateien über die Verschiebung entscheidet
(Fig. 13, Absätze [0108]-[0117], Fig.14, Absätze [0118]-[0131]).

                                          - 13 -



Aus der D1 sind somit allenfalls Teile der Merkmale M2, M3 und M4 zu
entnehmen. Die Eigenschaft, wonach es sich um eine synchrone Replikation
zwischen einem Paar aus Primär- und Sekundärspeicherentität handelt (Merkmal
M1) ist in der D1 nicht gezeigt. Damit ist aber auch der restliche Teil der Merkmale
M2, M3 und M4, d.h. die angegebene Primärspeicherentität, nicht in der D1
gezeigt. Die weiteren Merkmale M5 bis M5.6 sind aus der D1 ebenfalls nicht zu
entnehmen.




Aus der D2 ist ein System zu entnehmen, welches einen lokalen Speicher und
einen entfernten Speicher umfasst (Fig.1, Absätze [0009], [0010]). Beide Speicher
sind    mehrschichtig      aufgebaut,     d.h.      sie      umfassen         unterschiedliche
Speicherelemente, die als Speicherklassen bezeichnet werden (Fig.2, Absätze
[0011], [0012]). Weiter ist ein Migrieren von Dateien in dem lokalen System (Fig.8,
Absatz [0021]) zu entnehmen. Nach dem Migrieren der Dateien in dem lokalen
System wird ein Kommando an den entfernten Speicher gesendet, wobei das
Kommando das Migrieren der gleichen Datei in dem entfernten System auslöst
und anschließend wird eine Bestätigung an das lokale System gesendet (Fig.8,
Absatz [0022]). Schließlich ist hinsichtlich der unterschiedlichen Speicherelemente
angegeben,     dass      diese    aus   Elementen         bestehen,   die      eine     größere
Speicherkapazität aufweisen, dafür kostengünstigerer aber auch langsamer sind
und aus schnelleren Elementen bestehen, die jedoch weniger Speicherkapazität
aufweisen und teurer sind (Absatz [0012]).


Aus der D2 sind somit die Merkmale M1, M5 und M5.2 zu entnehmen.


Die    Identifizierung    einer   Datei   für      die    Migration     auf     Basis     eines
Speicheraktivitätsfaktors, und die Berechnung einer relativen Priorität auf der
Grundlage einer geordneten Primär-Heat-Map sowie eine Migrationsanweisung,
welche die berechnete relative Priorität des zu migrierenden Bereichs enthält
(Merkmale M2, M3, M4, M5.1) ist in der D2 nicht gezeigt.

                                           - 14 -



Ebenso ist die Berechnung einer Zuordnung der relativen Priorität zu einer Ebene
der mehrschichtigen Speichereinheiten der Sekundärspeicherentität auf der
Grundlage des Speichersystems der Sekundärspeicherentität (Merkmal M5.3) und
das     Empfangen     einer   Antwort      der      Sekundärspeicherentität      durch   die
Primärspeicherentität,     wobei     die      Antwort    die     berechnete     Ebene    der
mehrschichtigen Speichereinheiten der Sekundärspeicherentität angibt (Merkmal
M5.4) aus der D1 nicht zu entnehmen.
Schließlich ist aus der D1 auch keine Migration gemäß den Merkmalen M5.5 und
M5.6 zu entnehmen.


Keine    der      beiden   Druckschriften        gibt   somit    die   Lehre,    dass    die
Migrationsanweisung die relative Priorität des zu migrierenden Bereichs enthält
und dass in der Sekundärspeicherentität eine Zuordnung berechnet wird, welche
der Primärspeicherentität mitgeteilt wird.
Des Weiteren ist aus den beiden Druckschriften nicht zu entnehmen, dass eine
identische Zuordnung in der Primär- und in der Sekundärspeicherentität
vorgenommen wird, falls die beiden Ebenen der beiden Speichereinheiten
identisch sind.
Schließlich ist auch keine Migration auf eine Ebene, welche einer niedrigeren
Leistungsmaßzahl       entspricht,    falls      die    beiden    zugeordneten      Ebenen
unterschiedlich sind und das Verschieben auf die diejenige der beiden
zugeordneten Ebenen, welcher die niedrigere Leistungsmaßzahl entspricht, eine
Leistungssteigerung ergibt, aus den beiden Druckschriften zu entnehmen.


Nachdem den genannten Druckschriften auch keinerlei Anregung in dieser Hinsicht entnommen werden kann, ist der Gegenstand des geltenden Hauptanspruchs nicht nur neu, sondern ergibt sich für den Fachmann auch nicht in naheliegender Weise aus dem Stand der Technik.

                                      - 15 -



4.    Der nunmehr geltende Patentanspruch 1 ist nach alledem gewährbar.
Der nebengeordnete Patentanspruch 7 ist auf ein entsprechendes System und der
nebengeordnete Anspruch 14 auf ein entsprechendes Computerprogrammprodukt
gerichtet, sie können nicht anders beurteilt werden. Die Unteransprüche 2 bis 6
und 8 bis 13 sind in Verbindung mit Anspruch 1 bzw. mit Anspruch 7 ebenfalls
gewährbar.
Nach der von der Anmelderin durchgeführten Anpassung der Beschreibung sowie
der Figuren liegen für eine Patenterteilung geeignete Unterlagen vor.

                                             - 16 -



                                   Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
       Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
       Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
       sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
       zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof,    Herrenstr.     45     a,   76133    Karlsruhe,   durch   einen     beim
Bundesgerichtshof     zugelassenen        Rechtsanwalt    als   Bevollmächtigten    schriftlich
einzulegen.




Dr. Morawek                  Bayer                    Baumgardt                    Hoffmann
