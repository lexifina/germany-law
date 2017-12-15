---
ecli: "ECLI:DE:BPatG:2017:151217B18Wpat15.15.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 15/15"
decided: "2017-12-15"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=52&nr=30003&anz=809&pos=790&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-12-15_18_W-pat_15_15_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0002.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 15/15 vom 2017-12-15

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 15/15                                                   Verkündet am
_______________                                                  15. Dezember 2017
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


              betreffend die Patentanmeldung 10 2013 100 820.8


…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 15. Dezember 2017 durch die Vorsitzende
Richterin   Dipl.-Ing. Wickborn   sowie     die   Richter   Kruppa,   Dipl.-Phys.
Dr. Schwengelbeck und Dipl.-Ing. Altvater




ECLI:DE:BPatG:2017:151217B18Wpat15.15.0

                                      -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 12. August 2015 aufgehoben und das Patent auf der
       Grundlage der folgenden Unterlagen erteilt:


       - Patentansprüche 1 bis 6, eingereicht in der mündlichen Verhandlung,


       - Beschreibung, Seiten 1 bis 7, 7a und 7b, eingereicht in der
        mündlichen Verhandlung, Seiten 8 bis 20 vom 28. Januar 2013,


       - Figuren 1 bis 4 vom 28. Januar 2013.




                                  Gründe


                                       I.


Die am 28. Januar 2013 beim Deutschen Patent- und Markenamt eingereichte
Patentanmeldung 10 2013 100 820.8 mit der geltenden Bezeichnung


       „Verfahren zum sicheren Löschen eines nichtflüchtigen Halbleiter-Massenspeichers und Computersystem“


wurde mit Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patentund Markenamts in der Anhörung vom 12. August 2015 zurückgewiesen, weil die
Gegenstände der Patentansprüche 1 gemäß Haupt- und Hilfsantrag jeweils unter
Berücksichtigung des Standes der Technik gemäß den Druckschriften

                                         -3-



      D6       WO 2012 / 062 233 A1 und
      D7       Wikipedia: Garbage Collection (Version vom 27. Dezember 2012)


nicht auf einer für die Patentfähigkeit erforderlichen erfinderischen Tätigkeit beruhten.


Im Prüfungsverfahren wurden als Stand der Technik zudem die folgenden Druckschriften genannt:


      D1       US 2012 / 0 311 237 A1,
      D2       DE 10 2011 018 558 A1,
      D3       "Method And System for an Optimized Secure Erase of data on Non-Volatile Data Storage Devices", ip.com Inc., West Henrietta, NY,
               USA, 15. März 2011
      D4       "National Industrial Security Program, Operating Manual Supplement
               DoD 5220.22-M-Sup 1", USA, Februar 1995,
               URL: http://www.dtic.mil/whs/directives/corres/pdf/522022MSup1.pdf"
      D5       Wikipedia: TRIM (Version vom 15. Januar 2013), URL:
               http://web.archive.org/web/20130115104138/http://en.wikipedia.org/
               wiki/TRIM.


Gegen den vorstehend genannten Beschluss richtet sich die Beschwerde der Anmelderin. Sie beantragt,


          den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 12. August 2015 aufzuheben
          und das Patent auf der Grundlage der folgenden Unterlagen zu
          erteilen:


          - Patentansprüche 1 bis 7, eingegangen am 14. Juni 2013,
           hilfsweise

                                           -4-



         Patentansprüche 1 bis 6, eingereicht in der mündlichen Verhandlung,
        - Beschreibung, Seiten 1 bis 7, 7a und 7b, eingereicht in der
         mündlichen Verhandlung, Seiten 8 bis 20 vom 28. Januar 2013,
        - Figuren 1 bis 4 vom 28. Januar 2013.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hauptantrag lautet:


M1      Verfahren (V) zum sicheren Löschen eines nichtflüchtigen Halbleiter-Massenspeichers (HMS)
M1a     mit einer Mehrzahl von physikalischen Speichereinheiten, die entweder einem über eine Schnittstelle (SS) des Halbleiter-Massenspeichers (HMS) adressierbaren ersten Speicherbereich (SB1)
        oder einem über die Schnittstelle (SS) nicht-adressierbaren zweiten Speicherbereich (SB2) zugeordnet sind, und
M1b     einen Controller (CNT), der dazu eingerichtet ist, beim Erhalt eines
        Befehls      zum   Überschreiben    von   dem   ersten   Speicherbereich (SB1) zugeordneten Speichereinheiten über die Schnittstelle (SS) die Zuordnung der Speichereinheiten zu dem ersten
        Speicherbereich (SB1) und zweiten Speicherbereich (SB2) gemäß
        einem Algorithmus zur Herstellung eines Abnutzungsausgleichs
        zu verändern,


mit den Schritten:


M2      - Kennzeichnen        des    gesamten      adressierbaren     ersten
        Speicherbereichs (SB1) zum Löschen;
M3      - Aussenden eines Freigabebefehls über die Schnittstelle (SS)
        an den Controller (CNT);

                                      -5-



M4      - Freigeben der dem ersten Speicherbereich (SB1) zugeordneten
        physikalischen Speichereinheiten zum Beschreiben durch den
        Controller (CNT) nach Empfang des Freigabebefehls;
M5      - Aussenden wenigstens eines ersten Schreibbefehls über die
        Schnittstelle (SS) an den Controller (CNT) zum Beschreiben des
        gesamten ersten Speicherbereichs (SB1) mit Datenblöcken mit
        einem vorbestimmten ersten Bitmuster,
M5a     wobei der gesamte erste Speicherbereich (SB1) mit dem ersten
        Bitmuster überschrieben wird; und
M6      - Aussenden wenigstens eines zweiten Schreibbefehls über die
        Schnittstelle (SS) an den Controller (CNT) zum Überschreiben
        wenigstens eines vorbestimmten Teils der zuvor geschriebenen
        Datenblöcke mit einem zweiten, von dem ersten unterschiedlichen
        Bitmuster,
M6a     wobei gemäß dem Algorithmus zur Herstellung eines Abnutzungsausgleichs die dem zweiten Speicherbereich (SB2) zugeordneten
        physikalischen Speichereinheiten beschrieben werden.


Wegen des Wortlauts der nach Hauptantrag geltenden nebengeordneten Ansprüche 6 und 7 sowie der Unteransprüche 2 bis 5 wird auf die Akte verwiesen.


Der seitens des Senats mit einer Gliederung versehene Patentanspruch 1 nach
Hilfsantrag lautet:


M1      Verfahren (V) zum sicheren Löschen eines nichtflüchtigen Halbleiter-Massenspeichers (HMS)
M1a     mit einer Mehrzahl von physikalischen Speichereinheiten, die entweder einem über eine Schnittstelle (SS) des Halbleiter-Massenspeichers (HMS) adressierbaren ersten Speicherbereich (SB1)
        oder einem über die Schnittstelle (SS) nicht-adressierbaren zweiten Speicherbereich (SB2) zugeordnet sind, und

                                           -6-



M1b     einen Controller (CNT), der dazu eingerichtet ist, beim Erhalt eines
        Befehls      zum   Überschreiben    von   dem   ersten   Speicherbereich (SB1) zugeordneten Speichereinheiten über die Schnittstelle (SS) die Zuordnung der Speichereinheiten zu dem ersten
        Speicherbereich (SB1) und zweiten Speicherbereich (SB2) gemäß
        einem Algorithmus zur Herstellung eines Abnutzungsausgleichs
        zu verändern,


mit den Schritten:


M2      - Kennzeichnen        des      gesamten    adressierbaren     ersten
        Speicherbereichs (SB1) zum Löschen,
M2a     wobei der erste Speicherbereich (SB1) mit einem metafilelosen
        Dateisystem formatiert wird;
M3*     - Aussenden eines Freigabebefehls von einem Betriebssystem
        oder einem BIOS über die Schnittstelle (SS) an den Controller CNT);
M4      - Freigeben der dem ersten Speicherbereich (SB1) zugeordneten
        physikalischen Speichereinheiten zum Beschreiben durch den
        Controller (CNT) nach Empfang des Freigabebefehls;
M5*     - Aussenden wenigstens eines ersten Schreibbefehls von dem
        Betriebssystem oder dem BIOS über die Schnittstelle (SS) an den
        Controller (CNT) zum Beschreiben des gesamten ersten Speicherbereichs (SB1) mit Datenblöcken mit einem vorbestimmten
        ersten Bitmuster,
M5a     wobei der gesamte erste Speicherbereich (SB1) mit dem ersten
        Bitmuster überschrieben wird; und
M6*     - Aussenden wenigstens eines zweiten Schreibbefehls von dem
        Betriebssystem oder dem BIOS über die Schnittstelle (SS) an den
        Controller (CNT) zum Überschreiben wenigstens eines vorbe-

                                       -7-



        stimmten Teils der zuvor geschriebenen Datenblöcke mit einem
        zweiten, von dem ersten unterschiedlichen Bitmuster,
M6a     wobei gemäß dem Algorithmus zur Herstellung eines Abnutzungsausgleichs die dem zweiten Speicherbereich (SB2) zugeordneten
        physikalischen Speichereinheiten beschrieben werden.


Anspruch 6 gemäß Hilfsantrag lautet:


        Computersystem (CS), aufweisend ein BIOS, ein Betriebssystem
        und einen nichtflüchtigen Halbleiter-Massenspeicher (HMS) mit
        einem Controller (CNT) und einer Schnittstelle (SS) zum Zugriff
        auf einen ersten Speicherbereich (SB1) des Halbleiter-Massenspeichers (HMS) über den Controller (CNT), wobei
        - die Schnittstelle (SS) dazu eingerichtet ist, Befehle von dem
        Betriebssystem oder dem BIOS zu erhalten und an den
        Controller (CNT) zu übermitteln; und
        - das Computersystem (CS) dazu eingerichtet ist, ein Verfahren (V) nach einem der Ansprüche 1 bis 5 auszuführen.


Wegen des Wortlauts der nach Hilfsantrag geltenden abhängigen Ansprüche 2
bis 5 wird auf die Akte verwiesen.


Die Beschwerdeführerin macht geltend, dass die Anspruchsfassungen gemäß
Haupt- und Hilfsantrag jeweils zulässig und die Gegenstände der jeweiligen Ansprüche im Lichte des Standes der Technik neu seien und auf einer erfinderischen
Tätigkeit beruhten.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                       -8-



                                        II.


Die zulässige Beschwerde hat insoweit Erfolg, als sie zur Aufhebung des angefochtenen Beschlusses und zur Patenterteilung mit geänderten Unterlagen gemäß
Hilfsantrag führt. Im Übrigen war die Beschwerde bezüglich des Hauptantrags zurückzuweisen. Denn der Gegenstand des Anspruchs 1 nach Hauptantrag beruht
nicht auf einer erfinderischen Tätigkeit. Die Fragen der Zulässigkeit der geltenden
Ansprüche gemäß Hauptantrag sowie der Neuheit dieses Anspruchsgegenstandes können somit dahinstehen (vgl. BGH, Urteil vom 18. September 1990 -
X ZR 29/89, GRUR 1991, 120, 121 li. Sp. Abs. 3 - Elastische Bandage).


1. Die Anmeldung betrifft ein Verfahren zum sicheren Löschen eines nichtflüchtigen Halbleiter-Massenspeichers mit einer Mehrzahl von physikalischen Speichereinheiten und einem Controller. Die Erfindung betrifft des Weiteren ein
   Computersystem (vgl. geltende Beschreibung, 1. Abs.).


   Die Anmeldung geht davon aus, dass Computersysteme in der Regel einen
   oder mehrere Massenspeicher zum Speichern von Daten aufweisen. Beispielsweise beim Austausch eines solchen Massenspeichers stelle sich das
   Problem, dass dieser in der Regel private oder vertrauliche Daten enthalte.
   Diese Daten sollten vor dem Austausch gelöscht werden, um einen Missbrauch der Daten zu verhindern. Dabei reiche in der Regel ein einfaches Löschen mittels des Betriebssystems nicht aus, um die Daten unwiderruflich zu
   löschen, da lediglich auf Dateisystemebene die Zuordnung der Dateinamen zu
   physikalischen Speicheradressen des Massenspeichers gelöscht werde. Auf
   physikalischer Ebene verblieben die Daten im Wesentlichen auf dem Massenspeicher. Meist genügten einfache Softwareprogramme, um diese vermeintlich
   gelöschten Daten wieder herzustellen. Eine Erfolg versprechende Methode,
   diese Daten zu löschen, stelle das physische Zerstören des Massenspeichers
   dar, wobei beispielsweise der Massenspeicher entmagnetisiert oder anderweitig mechanisch zerstört werde. In der Regel würden allerdings die ausge-

                                     -9-



tauschten Massenspeicher weiter benutzt und beispielsweise verkauft, wobei
es notwendig sei, den Massenspeicher mittels des Computersystems sicher
und unwiderruflich zu löschen. Im Falle von Magnetfestplattenlaufwerken existierten hierzu Löschalgorithmen, die die Speicherbereiche in der Regel mehrmals mit vorbestimmten Bitmustern überschrieben, sodass ein Wiederherstellen der ursprünglichen Daten praktisch unmöglich sei.
Solche Methoden seien allerdings bei nichtflüchtigen Halbleiter-Massenspeichern nicht anwendbar, da sich diese Massenspeicher technologiebedingt hinsichtlich der Organisation von Daten und freiem Speicherplatz grundsätzlich
anders als Magnetfestplattenspeicher verhielten. Ein direkter Zugriff auf eine
bestimmte Speicheradresse im physikalischen Speicherbereich sei bei einem
Halbleiter-Massenspeicher im Gegensatz zu einem Magnetfestplattenspeicher
in der Regel nicht möglich. Aus der Veröffentlichung „Reliably Erasing Data
From Flash-Based Solid State Drives“ von Michael Wei et al. (2011) sei beispielsweise bekannt, dass existierende Löschmethoden für Magnetfestplattenlaufwerke bei Halbleiter-Massenspeichern wie Solid-State-Drives nicht
effektiv anwendbar seien. Einzig spezifische Algorithmen für Controller der
Halbleiter-Massenspeicher garantierten bei korrekter Implementierung das
sichere Löschen des Halbleiter-Massenspeichers. Dies setze allerdings Eingriffe in die Firmware des jeweiligen Controllers voraus. Zudem sei die Firmware je nach Hersteller des Halbleiter-Massenspeichers unterschiedlich (vgl.
geltende Beschreibung S. 2, vorletzter Absatz bis Seite 3, letzter Abs.).


Die Anmeldung nennt sinngemäß als Aufgabe, ein einfaches Verfahren zum
sicheren Löschen eines Halbleiter-Massenspeichers sowie ein zur Durchführung des Verfahrens geeignetes Computersystem zu beschreiben (vgl.
geltende Beschreibung, S. 4, 1. Abs.).


Der zuständige Fachmann weist eine abgeschlossene Hochschulausbildung
der Elektrotechnik oder Informationstechnik auf und verfügt über mehrjährige

                                  - 10 -



Erfahrung auf dem Gebiet der Ansteuerung und Verwendung von Halbleiter-Massenspeichern.


Die Aufgabe soll gemäß Haupt- und Hilfsantrag durch ein Verfahren zum sicheren Löschen eines       nichtflüchtigen   Halbleiter-Massenspeichers nach
Patentanspruch 1 und ein Computersystem nach Patentanspruch 6 sowie
gemäß Hauptantrag zudem durch einen Datenträger nach Patentanspruch 7
gelöst werden.


Das Verfahren zum sicheren Löschen eines nichtflüchtigen Halbleiter-Massenspeichers nach Anspruch 1 gemäß Hauptantrag sieht einen nichtflüchtigen
Halbleiter-Massenspeicher mit einer Mehrzahl von physikalischen Speichereinheiten vor, wobei die Speichereinheiten entweder einem über eine Schnittstelle des Halbleiter-Massenspeichers adressierbaren ersten Speicherbereich
oder einem über die Schnittstelle nicht-adressierbaren zweiten Speicherbereich zugeordnet sind (Merkmale M1, M1a). Unter einem „sicheren“ Löschen
ist dabei ein unwiderrufliches Löschen des Speichers zu verstehen, das ein
Wiederherstellen oder Rekonstruieren der ursprünglichen Daten praktisch
unmöglich macht (vgl. geltende Beschreibung, S. 3, erster Abs.; S. 17,
dr. Abs.). Der nichtflüchtige Halbleiter-Massenspeicher weist zudem einen
Controller auf, der dazu eingerichtet ist, beim Erhalt eines Befehls zum Überschreiben von dem ersten Speicherbereich zugeordneten Speichereinheiten
über die Schnittstelle die Zuordnung der Speichereinheiten zu dem ersten
Speicherbereich und zweiten Speicherbereich gemäß einem Algorithmus zur
Herstellung eines Abnutzungsausgleichs zu verändern (Merkmal 1b). Der
Abnutzungsausgleich, auch als „Wear Leveling“ bezeichnet, bezieht sich auf
die bei nichtflüchtigen Halbleiter-Massenspeichern bauartbedingt angewandte
Vorgehensweise, beim erneuten Beschreiben oder Löschen von logischen
Andressen die neuen Daten in einen anderen physikalischen Adressblock zu
schreiben, gegebenenfalls weitere Daten des alten Blocks in den neuen Block
zu kopieren sowie die Zuordnung der logischen zu physikalischen Adressen

                                  - 11 -



entsprechend anzupassen (vgl. geltende Beschreibung, S. 8, le. Abs. bis S. 11,
dr. Abs. i. V. m. S. 14, zw. Abs. bis S. 16, erster Abs. sowie Beschreibung zu
Fig. 3 und 4).
Zum sicheren Löschen soll in einem ersten Verfahrensschritt ein Kennzeichnen
des gesamten adressierbaren ersten Speicherbereichs zum Löschen erfolgen
(Merkmal M2), gefolgt vom Aussenden eines Freigabebefehls über die Schnittstelle an den Controller (Merkmal M3) und einem entsprechenden Freigeben
der dem ersten Speicherbereich zugeordneten physikalischen Speichereinheiten zum Beschreiben (Merkmal M4). Ein Aussenden wenigstens eines ersten Schreibbefehls über die Schnittstelle an den Controller zum Beschreiben
des gesamten ersten Speicherbereichs mit Datenblöcken mit einem vorbestimmten ersten Bitmuster bewirkt nach der vorausgehenden Freigabe, dass
der gesamte erste Speicherbereich mit dem ersten Bitmuster überschrieben
wird (Merkmale M5, M5a). In einem weiteren Verfahrensschritt erfolgt das Aussenden wenigstens eines zweiten Schreibbefehls über die Schnittstelle an den
Controller zum Überschreiben wenigstens eines vorbestimmten Teils der zuvor
geschriebenen Datenblöcke mit einem zweiten, von dem ersten unterschiedlichen Bitmuster (Merkmal M6). Dabei werden gemäß dem Algorithmus zur Herstellung eines Abnutzungsausgleichs die dem zweiten Speicherbereich zugeordneten physikalischen Speichereinheiten beschrieben (Merkmal M6a).


Anspruch 1 gemäß Hilfsantrag präzisiert, dass das Aussenden eines Freigabebefehls und das Aussenden wenigstens eines ersten und eines zweiten
Schreibbefehls jeweils von einem Betriebssystem oder BIOS ausgehen (vgl.
Merkmale M3*, M5*, M6*). Zudem soll nach Anspruch 1 gemäß Hilfsantrag der
erste Speicherbereich mit einem metafilelosen Dateisystem formatiert werden
(vgl. Merkmal M2a).


Der nebengeordnete Anspruch 6 gemäß Haupt- und Hilfsantrag ist auf ein
Computersystem gerichtet, das zur Ausführung des Verfahrens nach einem
der vorangehenden Ansprüche eingerichtet ist. Anspruch 7 gemäß Hauptan-

                                       - 12 -



   trag ist auf ein auf einem Datenträger gespeichertes Computerprogramm
   gerichtet, das zur Ausführung des Verfahrens nach einem der vorangehenden
   Verfahrensansprüche eingerichtet ist.


2. Der Hauptantrag ist nicht patentfähig.


   a) Der Gegenstand des Anspruchs 1 nach Hauptantrag beruht für den Fachmann ausgehend von Druckschrift D1 und in Kenntnis von Druckschrift D4
   nicht auf einer erfinderischen Tätigkeit (§ 4 PatG).


   Druckschrift D1 ist ein Verfahren zum sicheren Löschen von Speicherzellen
   eines nichtflüchtigen Halbleiter-Massenspeichers zu entnehmen, ohne dass ein
   vollständiges Löschen des gesamten Speichers angesprochen ist (vgl.
   Abs. [0070] / teilweise Merkmal M1). Es ist eine Mehrzahl von physikalischen
   Speichereinheiten vorgesehen, die entweder einem über eine Schnittstelle des
   Halbleiter-Massenspeichers adressierbaren ersten Speicherbereich („data
   blocks“; „logical address“) oder einem über die Schnittstelle nicht-adressierbaren zweiten Speicherbereich („reserved blocks“) zugeordnet sind (vgl. Fig. 2;
   Abs. [0065], bes. le. fünf Sätze auf S. 4 / Merkmal M1a). Weiterhin ist ein
   Controller vorgesehen (vgl. Abs. [0048]), der beim Erhalt eines Befehls zum
   Überschreiben von Speichereinheiten, die dem ersten Speicherbereich zugeordnet sind, die Zuordnung der Speichereinheiten zu dem ersten Speicherbereich und zweiten Speicherbereich gemäß einem Algorithmus zur Herstellung
   eines Abnutzungsausgleichs verändert („In addition, firmware 300 may
   swap…“; vgl. Abs. [0065], insbes. le. vollständiger Satz auf S. 4 / Merkmal
   M1b).
   Druckschrift D1 sieht das Kennzeichnen eines adressierbaren ersten Speicherbereichs zum Löschen vor, ohne dass ein Löschen des gesamten adressierbaren Speichers angesprochen ist („delete request“; vgl. Abs. [0007] und
   Abs. [0045] / teilweise Merkmal M2). Zudem ist ein Freigabebefehl vorgesehen, der vom Host über die Schnittstelle erhalten wird („…generating an inter-

                                  - 13 -



nal trim command in response to the delete request…“; vgl. Abs. [0007], sowie
Abs. [0045] / Merkmal M3), worauf ein Freigeben der dem ersten Speicherbereich zugeordneten physikalischen Speichereinheiten erfolgt (vgl. Abs. [0071]
sowie Abs. [0124] / Merkmal M4). Ein Beschreiben des gesamten (adressierbaren) ersten Speicherbereichs mit Datenblöcken mit einem vorbestimmten
ersten Bitmuster (vgl. Merkmale M5, M5a) wird in Druckschrift D1 nicht aufgeführt. Druckschrift D1 ist jedoch zu entnehmen, dass der Host das Löschen
eines ganzen virtuellen Speicherbereichs verlangen kann, was zu einem Löschen und ggf. Initialisieren der diesem logischen (virtuellen) Adressbereich
zugeordneten physikalischen Adressen führt (vgl. Abs. [0124], bes. erster
vollst. Satz auf S. 12). Dies erfolgt durch Aussenden von Befehlen über eine
Schnittstelle (d. h. durch den Host) an den Controller des Massenspeichers
(vgl. Fig. 1 und 2 mit Beschreibung, bes. Abs. [0048]) (teilweise Merkmale M5
und M5a). Druckschrift D1 sieht darüber hinaus einen Algorithmus zur Herstellung eines Abnutzungsausgleichs vor, der bestimmt, welche dem adressierbaren Speicherbereich zugeordnete physikalische Speichereinheit beschrieben wird, so dass die für den Abnutzungsausgleich vorgesehenen und
einem zweiten Speicherbereich zugeordneten physikalischen Speichereinheiten („reserved blocks“) beschrieben werden („wear leveling“; vgl. Abs. [0065],
S. 4 - 5, seitenübergreifender Satz / Merkmal M6a).
Damit unterscheidet sich Druckschrift D1 vom vorliegenden Anspruchsgegenstand darin, dass Freigabe- bzw. Löschbefehle sich nur auf einzelne adressierbare (virtuelle) Teilbereiche des Speichers beziehen (Merkmale M2, M3)
und ein gezieltes zweifaches Beschreiben eines zu löschenden Speicherbereichs nicht vorgesehen ist (vgl. Merkmale M5, M5a und M6).


Der Fachmann, der vor der Aufgabe steht, einen nichtflüchtigen Halbleiter-Massenspeicher vollständig und sicher zu löschen, findet in Druckschrift D4
Empfehlungen zum vollständigen Löschen bzw. Bereinigen von Speichermedien (vgl. S. 80, Abs. C8.5.2.4 und S. 81, Abs. C8.5.2.4.3), unter anderem für
nichtflüchtige Halbleiter-Massenspeicher („Solid State Memory Components“,

                                   - 14 -



bspw. „Electronically Erasable PROM (EEPROM)“ bzw. „Flash EPROM
(FEPROM)“, vgl. S. 83, Tabelle C8.T2 / Merkmal M1). Für solche Speicher im
Sinne des Anspruchs 1, bei denen es sich um Halbleiterspeicherbausteine,
beispielsweise Flash-EEPROMs handelt (vgl. geltende Beschreibung, S. 8,
erster Abs.), ist gemäß Druckschrift D4 in einem ersten Schritt das Löschen
des gesamten Massenspeichers vorgesehen (vgl. Merkmal M2 i. V. m. M3)
(vgl. Tabelle C8.T2, S. 84, Schritt i). Als zweiter Schritt ist vorgesehen, alle
Speicherstellen („all locations“) mit einem Bitmuster zu überschreiben
(“Overwrite all locations with a character,...”; vgl. S. 83/84, Tabelle C8.T2,
Schritt d), wobei der Fachmann unter einem Überschreiben aller Speicherstellen ein Beschreiben des gesamten adressierbaren Speicherbereichs des Massenspeichers versteht. Dies entspricht einem ersten Schreibvorgang entsprechend den Merkmalen M5 und M5a. Daraufhin sollen alle Speicherstellen mit
einem zweiten Bitmuster überschrieben werden (“Overwrite all locations with a
character, its complement,…”; vgl. S. 83/84, Tabelle C8.T2, Schritt d). Wendet
der Fachmann diese Vorgehensweise auf einen aus Druckschrift D1 bekannten nichtflüchtigen Halbleiter-Massenspeicher an, welcher einen Abnutzungsausgleich („Wear Leveling“) unterstützt (vgl. Druckschrift D1, Abs. [0041]
i. V. m. Abs. [0065], S. 4 - 5, seitenübergreifender Satz), so wird durch das
wiederholte Schreiben auch eine entsprechende Änderung der einander zugeordneten logischen und physikalischen Adressen aufgrund des „Wear
Leveling“ bewirkt. Damit hat ein zweites vollständiges Überschreiben gemäß
Druckschrift D4 zur Folge, dass auch alle Löschblöcke überschrieben werden,
die nicht direkt adressierbar sind und durch einen Algorithmus zur Herstellung
eines Abnutzungsausgleichs durch den Controller beim Überschreiben adressierbaren Datenblöcken zugewiesen werden. Damit erfüllt ein zweifaches
Überschreiben des gesamten adressierbaren Speichers nach Druckschrift D4
für einen Halbleiter-Massenspeicher gemäß Druckschrift D1 auch die Merkmale M6 und M6a.

                                  - 15 -



Wie die Anmelderin zutreffend ausführt, zielt das Löschen von Daten gemäß
Druckschrift D1 mit virtuellen Speicherbereichen jeweils nur auf einen zugeordneten Teilbereich der dort zugrunde liegenden physikalischen Speichereinrichtung ab. Es fehle nach ihrer Auffassung somit bereits an der Anregung, den
Speicher vollständig zu löschen. Das Ziel einer sicheren vollständigen
Löschung des Speichers ist jedoch Teil der vorliegenden Aufgabenstellung und
nicht der Lösung (vgl. BGH, Urteil vom 30. Juli 2009 - Xa ZR 22/06,
GRUR2010, 44 - Dreinahtschlauchfolienbeutel, erster Leitsatz).


Geht man von den zum Anmeldezeitpunkt typischen Flash-Speichern aus, die
einen Abnutzungsausgleich („Wear Leveling“) nutzen und die beispielsweise in
Druckschrift D1 beschrieben sind, findet der Fachmann in Druckschrift D4
Maßnahmen, die auf ein möglichst umfassendes und sicheres Löschen eines
Speichers abzielen. Das Alter der Druckschrift D4 steht dabei - entgegen der
Auffassung der Anmelderin - einer Berücksichtigung durch den Fachmann
nicht entgegen, da diese Grundlagen zur sicheren Verwendung von Datenträgern beschreibt, die im Wesentlichen auch heute noch ihre Gültigkeit besitzen.
Das dort für Halbleiter-Massenspeicher vorgeschlagene mehrfache Überschreiben des gesamten adressierbaren Speichers führt allein durch Anwendung auf einen aus Druckschrift D1 bekannten Speicher mit Abnutzungsausgleich („Wear Leveling“) bereits ohne weitere Anpassung oder zusätzliche
Maßnahmen zum gewünschten Erfolg. Denn Anspruch 1 schließt ein jeweils
vollständiges Beschreiben des Speichers mit ein, ohne dass beispielsweise die
Zahl der Löschblöcke oder der Algorithmus zum Abnutzungsausgleich selbst
berücksichtigt werden müssen. Dass Druckschrift D4 kein „Wear Leveling“
anspricht und zum Veröffentlichungszeitpunkt möglicherweise noch nicht
berücksichtigen konnte, ist daher ohne Bedeutung.


Im Unterschied zu den Ausführungen der Anmelderin sieht der Senat den Verweis auf das Benutzerhandbuch bei einem Löschen des Speichers gemäß
Druckschrift D4 (vgl. S. 84, Table C8.T2, Punkt i) im Einklang mit den Maß-

                                        - 16 -



   nahmen gemäß den Anspruchsmerkmalen M2 und M3. Denn der vorliegende
   Anspruch 1 gemäß Hauptantrag lässt offen, wie die Kennzeichnung zum
   Löschen und eine entsprechende Freigabe des Speichers realisiert werden.
   Dass dies im Rahmen der vom Speicher unterstützten Befehle erfolgt - worauf
   der Verweis auf das Benutzerhandbuch den Fachmann hinweist - steht daher
   weder im Widerspruch zu Anspruch 1, noch folgt aus dem Hinweis an den Benutzer ein Abweichen vom beanspruchten Verfahrensablauf.


   Der Fachmann, der vor der Aufgabe steht, alle Daten eines typischen Halbleiter-Massenspeichers, wie er aus Druckschrift D1 bekannt ist, sicher, d. h. nicht
   wiederherstellbar zu löschen, gelangt daher in Kenntnis der Maßnahmen nach
   Druckschrift D4 zum Gegenstand des Anspruchs 1 (Hauptantrag), ohne erfinderisch tätig werden zu müssen.


   b) Mit dem nicht patentfähigen Anspruch 1 nach Hauptantrag sind auch die
   nebengeordneten Ansprüche 6 und 7 sowie die Unteransprüche 2 bis 5 nicht
   schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war (vgl. BGH, Beschluss vom 27. Juni 2007, X ZB 6/05, GRUR 2007,
   862, Abschnitt III. 3. a) aa) ´- Informationsübermittlungsverfahren II).


3. Der Hilfsantrag erfüllt die Voraussetzungen für eine Patenterteilung.


   Die zweifelsfrei gewerblich anwendbaren Gegenstände der nebengeordneten
   Patentansprüche 1 und 6 gemäß Hilfsantrag sind gegenüber dem im Verfahren befindlichen Stand der Technik neu und beruhen auf einer erfinderischen Tätigkeit. Auch die weiteren Voraussetzungen zur Patenterteilung sind
   erfüllt (§§ 1 bis 5, § 34 und § 38 PatG).


   a) Die Patentansprüche 1 bis 6 nach Hilfsantrag sowie die Beschreibungsunterlagen mitsamt Figuren sind zulässig (§ 38 PatG).

                                   - 17 -



Die Änderungen in den nebengeordneten Ansprüchen 1 und 6 und in den Patentansprüchen 2 bis 5 gegenüber den Anmeldeunterlagen liegen im Rahmen
der ursprünglichen Offenbarung.


Der Patentanspruch 1 basiert auf dem ursprünglich eingereichten Anspruch 1
unter Streichung eines fakultativen Merkmals (vgl. Merkmal M3*) und Präzisierungen einzelner Merkmale basierend auf Seite 4, erster und dritter Absatz
(vgl. Merkmal M5a), Seite 5, zweiter Absatz in Verbindung mit Seite 12, letzter
Absatz (vgl. Merkmal M2a) sowie Seite 6, vorletzter Absatz und Seite 12, dritter Absatz (vgl. Merkmale M3*, M5* und M6*) der ursprünglich eingereichten
Beschreibung.
Anspruch 2 basiert auf dem ursprünglich eingereichten Anspruch 2 unter Streichung des ersten Teilmerkmals, das aufgrund der Ergänzungen in Anspruch 1
bereits mit umfasst ist. Die Patentansprüche 3 und 4 wurden gegenüber der
ursprünglich eingereichten Fassung getauscht und in ihren Rückbezügen
angepasst. Anspruch 5 stimmt mit dem entsprechenden ursprünglichen Patentanspruch überein. Anspruch 6 basiert auf dem ursprünglich eingereichten
Anspruch 6 in Verbindung mit Seite 6, dritter Absatz der ursprünglich eingereichten Beschreibung.


In der geltenden Beschreibung wurde eine Würdigung des Standes der Technik ergänzt. Zudem wurde die Beschreibungseinleitung an die geltenden
nebengeordneten Ansprüche angepasst und redaktionelle Änderungen vorgenommen. Die geltenden Figuren entsprechen den ursprünglich eingereichten
Figuren.


b) Patentanspruch 1 gemäß Hilfsantrag ist neu gegenüber dem im Verfahren
befindlichen Stand der Technik (§ 3 PatG).


Patentanspruch 1 gemäß Hilfsantrag unterscheidet sich vom Patentanspruch 1
gemäß Hauptantrag dadurch, dass zusätzlich Merkmal M2a vorgesehen ist,

                                    - 18 -



wonach „der erste Speicherbereich (SB1) mit einem metafilelosen Dateisystem
formatiert wird“ und durch die Präzisierung in den Merkmalen M3*, M5* und
M6*, wonach das Aussenden eines Freigabebefehls, eines ersten Schreibbefehls sowie wenigstens eines zweiten Schreibbefehls „von einem Betriebssystem oder einem BIOS“ an den Controller vorgenommen wird.


Zu Druckschrift D1 wird zu den mit dem Hauptantrag übereinstimmenden
Merkmalen auf die Ausführungen in Abschnitt II.2. verwiesen. Die im Hilfsantrag im Patentanspruch 1 hinzugefügten Merkmale sind aus Druckschrift 1
nicht entnehmbar, denn Druckschrift D1 liefert dem Fachmann keine Hinweise
auf das Formatieren des ersten (adressierbaren) Speicherbereichs mit einem
metafilelosen Dateisystem (Merkmal M2a fehlt). Dies gilt in gleicher Weise für
die in Anspruch 1 gemäß Hilfsantrag hinsichtlich der Befehlsaussendung von
einem Betriebssystem bzw. BIOS eingeschränkten Merkmale.
Damit sind Druckschrift D1 die Merkmale M2 und M3*, M5*, M5a nur teilweise,
und die Merkmale M2a und M6* gemäß Anspruch 1 des Hilfsantrags nicht zu
entnehmen. Anspruch 1 gemäß Hilfsantrag ist damit neu gegenüber Druckschrift D1.


Druckschrift D2 befasst sich dem beschleunigten Schreiben von Bilddateien in
den Speicher eines Mobiltelefons, wobei lediglich der Löschvorgang von Teilbereichen des Speichers beim Schreiben von Daten in den Speicher berücksichtigt wird (Abs. [0009]). Druckschrift D2 ist daher zur Beurteilung der vorliegenden Anmeldung nicht weiter relevant.


Druckschrift D3 ist in Bezug auf Anspruch 1 gemäß Hilfsantrag ein sicheres
Löschen eines nichtflüchtigen Halbleiter-Massenspeichers zu entnehmen (vgl.
Titel / Merkmal M1). Druckschrift D3 verweist dabei auf ein Solid State Drive
(SSD) (vgl. S. 2, 4. Abs.), wobei der Fachmann das Vorhandensein einer
Mehrzahl von physikalischen Speichereinheiten mitliest, die bauartbedingt in
der Regel einen adressierbaren ersten und einen nicht-adressierbaren Spei-

                                    - 19 -



cherbereich aufweisen (Merkmal M1a). Ein Controller des nichtflüchtigen
Halbleiter-Massenspeichers ist implizit daraus zu entnehmen, dass die Implementierung des vorgeschlagenen Löschverfahrens im Halbleiter-Massenspeicher erfolgen soll (S. 2, Abs. „Solution“, 5. Aufzählungspunkt), jedoch wird ein
Algorithmus zur Herstellung eines Abnutzungsausgleichs zur Veränderung der
Zuordnung der Speicherbereiche nicht aufgeführt (teilweise Merkmal M1b).
Es ist weiterhin ein Kennzeichnen eines adressierbaren ersten Speicherbereichs zum Löschen vorgesehen, womit eine Löschung des gesamten adressierbaren Bereichs des Speichers ebenfalls nicht angesprochen wird (teilweise Merkmal M2). Dabei erfolgt ein Aussenden eines Freigabebefehls durch
das Betriebssystem des Host-Rechners („TRIM command“; vgl. 2, drittle. Abs. /
Merkmal M3*), der zum Freigeben des genannten ersten Speicherbereichs
durch den Disk Controller führt (vgl. S. 3, Abbildung; drittl. Abs. / Merkmal M4).
Druckschrift D3 unterscheidet sich vom Gegenstand des vorliegenden
Anspruchs 1 durch das Fehlen des Aussendens von Schreibbefehlen (vgl.
Merkmale M5*, M5a, M6*) und der Anwendung eines Algorithmus zur Herstellung eines Abnutzungsausgleichs (vgl. Merkmal M6a). Zudem ist hinsichtlich
der Freigabe zum Löschen nicht der gesamte adressierbare Bereich angesprochen (vgl. Merkmal M2), und Druckschrift D3 sind keine Hinweise auf das
Formatieren des ersten (adressierbaren) Speicherbereichs mit einem metafilelosen Dateisystem zu entnehmen (vgl. Merkmal M2a). Ein sicheres Löschen
setzt gemäß Druckschrift D3 zudem die Änderung der Firmware des Halbleiter-Massenspeichers (bzw. des Disk Controllers) voraus (vgl. S. 2, Abs. „Solution“,
le. Aufzählungspunkt; S. 3, Abbildung). Anspruch 1 gemäß Hilfsantrag ist damit
ebenfalls neu gegenüber Druckschrift D3.


Zu Druckschrift D4 wird zu den mit dem Hauptantrag übereinstimmenden
Merkmalen auf die Ausführungen in Abschnitt II.2. verwiesen. In Druckschrift
D4 ist vorgesehen, alle Speicherstellen mit einem ersten und zweiten Bitmuster
zu überschreiben, wobei der Fachmann die Verwendung üblicher Schreibbefehle unter Verwendung des Betriebssystems des Hostrechners mitliest (vgl.

                                   - 20 -



S. 83/84, Tabelle C8.T2, Schritt d) (Merkmale M5*, M5a und M6*). Druckschrift D4 verweist jedoch im Unterschied zu Anspruch 1 gemäß Hilfsantrag
darauf, eine spezielle, vom Hersteller vorgesehene Löschfunktion des Halbleiter-Massenspeichers zu verwenden (vgl. S. 84, Tabelle C8.T2, Schritt i), während Anspruch 1 vorsieht, dass die Befehle zum Kennzeichnen und Freigeben
des Speichers vom Betriebssystem bzw. BIOS ausgehen (vgl. Merkmal M3*),
d. h. der übliche Betriebssystem-Befehlssatz genutzt wird. Schließlich sind
Druckschrift D4 keine Hinweise auf das Formatieren des ersten (adressierbaren) Speicherbereichs mit einem metafilelosen Dateisystem zu entnehmen
(vgl. Merkmal M2a).
Damit fehlen in Druckschrift D4 die Merkmale M1a, M1b, M2a, M4, M6a. Die
Merkmale M2 und M3* fehlen zumindest teilweise. Anspruch 1 gemäß Hilfsantrag ist damit ebenfalls neu gegenüber Druckschrift D3.


Druckschrift D5 beschreibt Fachwissen in Bezug auf den in der Anmeldung
und im weiteren Stand der Technik erwähnten TRIM-Befehl, welcher der Speicherfreigabe durch das Betriebssystem dient, um Probleme zu verringern, die
insbesondere durch den Abnutzungsausgleich („Wear Leveling“) entstehen.
Der Fachmann entnimmt Druckschrift D5 in Bezug auf Anspruch 1 gemäß
Hilfsantrag allenfalls einen Hinweis auf ein Kennzeichnen von adressierbaren
Speicherbereichen zum Löschen und deren Freigabe, jedoch ohne dass sich
diese auf den gesamten adressierbaren Speicherbereich bezieht (Merkmale
M2, M3* und M4 fehlen teilweise) und ohne einen Hinweis auf ein Formatieren
des Speicherbereichs mit einem metafilelosen Dateisystem zu geben (Merkmal
M2a fehlt). Ein Aussenden von Schreibbefehlen im Sinne der Merkmale M5*,
M5a und M6* ist ebenfalls nicht angesprochen. Anspruch 1 gemäß Hilfsantrag
ist damit ebenfalls neu gegenüber Druckschrift D5.


Druckschrift D6 betrifft eine verbesserte Funktion des bekannten TRIM-Befehls.

                                   - 21 -



Der Fachmann entnimmt ihr in Bezug auf Anspruch 1 gemäß Hilfsantrag ein
Verfahren zum Löschen von Bereichen eines Halbleiter-Massenspeichers (vgl.
S. 6, Z. 1-8 / teilweise Merkmal M1). Dieser umfasst eine Mehrzahl von physikalischen Speichereinheiten (vgl. S. 3, le. Abs.), die über eine Schnittstelle
adressierbar sind, was der Fachmann der Mitteilung nicht mehr benötigter
Daten entnimmt (vgl. S. 6, Z. 1-8). Dass ein Speicherbereich mit nicht direkt
adressierbaren Speicherzellen vorliegt, liest der Fachmann aufgrund des angesprochenen Flash-Speichers in Verbindung mit dem Verweis auf „Wear
Leveling“ mit (vgl. S. 2, vorl. Abs. / Merkmal M1a). Es ist weiterhin ein
Controller vorgesehen („Speichercontroller MC“), der beim Erhalt eines Befehls
zum Überschreiben von adressierbaren Speichereinheiten deren Zuordnung zu
dem ersten Speicherbereich und zweiten Speicherbereich gemäß einem Algorithmus zur Herstellung eines Abnutzungsausgleichs verändert (vgl. „Wear
Leveling“, vgl. S. 2, vorl. Abs. i. V. m. S. 8, Z. 16-29 und S. 4, erster Abs./
Merkmal M1b). Ein Kennzeichnen eines adressierbaren ersten Speicherbereichs zum Löschen bezieht sich auf einen bestimmten Adressbereich und
nicht auf den gesamten adressierbaren Speicher (vgl. S. 4, Z. 13-15 / teilweise
Merkmal M2), wobei das Veranlassen der Freigabe durch einen Freigabebefehl erfolgt („TRIM-Kommando“; vgl. S. 4, Z. 13-15 und S. 6, Z. 2-6 / Merkmal
M3*). Daraufhin erfolgt das Freigeben der dem ersten Speicherbereich zugeordneten physikalischen Speichereinheiten zum Beschreiben durch den Controller nach Empfang des Freigabebefehls vom Betriebssystem (vgl. S. 6, Z. 6-
8 / Merkmal M4). Außerdem ist Druckschrift D6 ein Zuordnen von physikalischen Speichereinheiten (d. h. einem neuen physikalische Pufferblock) gemäß
dem Algorithmus zur Herstellung eines Abnutzungsausgleichs zu entnehmen
(vgl. S. 8, Z. 17-29 / Merkmal M6a).
Ein mehrfaches Beschreiben des gesamten adressierbaren Speicherbereichs
ist im Unterschied zum vorliegenden Anspruch 1 nicht vorgesehen (Merkmale
M5*, M5a und M6* fehlen). Ebenso fehlt ein Hinweis auf das Formatieren des
ersten (adressierbaren) Speicherbereichs mit einem metafilelosen Dateisystem
(vgl. Merkmal M2a). Die Maßnahmen nach Druckschrift D6 beziehen sich im

                                   - 22 -



Unterschied zu Anspruch 1 nicht auf den gesamten (adressierbaren) Speicherbereich (Merkmale M1 und M2 fehlen teilweise). Anspruch 1 gemäß Hilfsantrag
ist damit ebenfalls neu gegenüber Druckschrift D6.


Druckschrift D7 beschreibt Fachwissen zum Thema der automatischen Speicherbereinigung („Garbage Collection“). Sie ist zur Beurteilung der vorliegenden Anmeldung nicht relevant, da Hinweise zu einer Umsetzung der erwähnten
Löschung von physikalischen Speicherblöcken bei Halbleiter-Massenspeichern
in Druckschrift D7 ebenso fehlen wie ein Hinweis auf ein zumindest zweifaches
Beschreiben gelöschter Blöcke mit einem vorgegebenen Bitmuster.


c) Auch der nebengeordnete Patentanspruch 6 gemäß Hilfsantrag ist neu gegenüber dem im Verfahren befindlichen Stand der Technik (§ 3 PatG).


Die vorstehenden Ausführungen zur Neuheit des Anspruchs 1 gemäß Hilfsantrag gegenüber den Druckschriften D1 bis D7 gelten in gleicher Weise für den
nebengeordneten, auf ein Computersystem gerichteten Anspruch 6 des Hilfsantrags, gemäß dem das Computersystem eingerichtet sein soll, ein Verfahren
nach einem der Ansprüche 1 bis 5 auszuführen. Da das Verfahren gemäß
Anspruch 1 neu ist gegenüber dem Stand der Technik ist auch ein zur entsprechenden Verfahrensdurchführung eingerichtetes Computersystem neu.


d) Die jeweiligen Gegenstände der nebengeordneten Patentansprüche 1
und 6 nach Hilfsantrag beruhen gegenüber dem im Verfahren befindlichen
Stand der Technik auch auf einer erfinderischen Tätigkeit (§ 4 PatG).


Keine der im Verfahren befindlichen Druckschriften sieht vor, den ersten
(adressierbaren) Speicherbereich im Rahmen des Löschens mit einem metafilelosen Dateisystem zu formatieren (vgl. Merkmal M2a).
Ein solches Formatieren ist dem Fachmann auch durch keine der Druckschriften D1 bis D7 nahegelegt. Die Druckschriften D1 und D6 sehen jeweils nur ein

                                  - 23 -



Löschen einzelner Speicherbereiche vor. Sicherheitsaspekte eines vollständigen und sicheren Löschens eines Halbleiter-Massenspeichers spielen dabei
keine Rolle, so dass davon ausgehend auch keine Veranlassung zur Berücksichtigung von Metadaten des Dateisystems besteht. Gleiches gilt für Druckschrift D3, die eine Verbesserung des TRIM-Befehls anstrebt und keinen Hinweis auf das Dateisystem liefert. Druckschrift D4 befasst sich zwar mit dem
vollständigen Löschen eines Halbleiter-Massenspeichers. Doch im Zusammenhang mit dem Löschen des Speichers findet sich in Druckschrift D4 weder ein
Hinweis auf das jeweilige Dateisystem noch auf die möglicherweise aus den
Metadaten des Dateisystems resultierenden Sicherheitsaspekte. Die Druckschriften D2 sowie D5 und D7 stellen keinen Bezug zum vollständigen und
sicheren Löschen eines Halbleiter-Massenspeichers her und befassen sich
folglich nicht mit den Auswirkungen auf das Löschen durch ein jeweiliges
Dateisystem.
Auch eine gemeinsame Betrachtung der Druckschriften D1 und D4 kann den
Gegenstand des Anspruchs 1 gemäß Hilfsantrag nicht nahelegen. Zwar ist
dem Fachmann aus diesen Druckschriften Anspruch 1 gemäß Hauptantrag
nahegelegt (vgl. Ausführungen zum Hauptantrag in Abschnitt II.2.a)). Jedoch
ist keiner der beiden Druckschriften ein Formatieren mit einem metafilelosen
Dateisystem gemäß Merkmal M2a entsprechend Anspruch 1 des Hilfsantrags
zu entnehmen. Die Druckschriften D1 und D4 enthalten auch keinen Hinweis
auf eine Berücksichtigung des Dateisystems im Hinblick auf ein sicheres und
vollständiges Löschen eines Halbleiter-Massenspeichers. Zudem verweist
Druckschrift D4 im Unterschied zur Verwendung von Betriebssystem- bzw.
BIOS-Befehlen zum Kennzeichnen und Freigeben des Speichers (vgl. Merkmal
M3*) darauf, eine vom Hersteller vorgesehene Löschfunktion des Halbleiter-Massenspeichers zu verwenden (vgl. S. 84, Tabelle C8.T2, Schritt i).


Die vorstehend genannten Druckschriften D1 bis D7 können auch in beliebiger
Zusammenschau dem Fachmann die Merkmale des Anspruchs 1 nach Hilfsantrag nicht nahelegen, da diese Druckschriften - auch unter Ergänzung seines

                                       - 24 -



   Fachwissens auf diesem Gebiet - keine Anregung zur Verwendung eines metafilelosen Dateisystems geben und mit Ausnahme von Druckschrift D4 auch
   kein mehrfaches Beschreiben des adressierbaren Speichers vorsehen.


   Es ist daher anzuerkennen, dass der Gegenstand des Anspruchs 1 gemäß
   Hilfsantrag auf einer erfinderischen Tätigkeit beruht und patentfähig ist. Gleiches gilt für den auf den nebengeordneten und auf ein Computersystem
   gerichteten Anspruch 6, gemäß dem das Computersystem eingerichtet sein
   soll, ein Verfahren nach einem der Ansprüche 1 bis 5 auszuführen.


   e) Gleichfalls patentfähig sind die über das Selbstverständliche hinausgehenden Ausführungsformen gemäß den Ansprüchen 2 bis 5 nach Hilfsantrag, die
   auf Anspruch 1 rückbezogen sind.


4. Da die vorgelegten geltenden Unterlagen auch den weiteren Voraussetzungen
   zur Patenterteilung (§§ 1, 2, 5, 34 PatG) genügen, war auf die Beschwerde des
   Anmelders der Zurückweisungsbeschluss der Prüfungsstelle für Klasse G 06 F
   des Deutschen Patent- und Markenamts aufzuheben und ein Patent gemäß
   Hilfsantrag zu erteilen.




                                         III.


                              Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

                                     - 25 -



   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
      Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
      Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten
      war, sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei
      der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden
      sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn            Kruppa              Dr. Schwengelbeck                Altvater


                                                                              Pr
