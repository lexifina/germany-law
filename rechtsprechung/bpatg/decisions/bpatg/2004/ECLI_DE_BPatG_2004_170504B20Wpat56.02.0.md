---
ecli: "ECLI:DE:BPatG:2004:170504B20Wpat56.02.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 56/02"
decided: "2004-05-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=51&nr=19557&anz=2061&pos=772&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-05-17_20_W-pat_56_02_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 20 W (pat) 56/02 vom 2004-05-17

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 56/02                                       Verkündet am
 _______________                                        17. Mai 2004
    (Aktenzeichen)                                           …




                          BESCHLUSS

                        In der Beschwerdesache


                     betreffend das Patent 197 33 748


…




BPatG 154
6.70

                                        -2-



…




hat der 20. Senat des Bundespatentgerichts auf die mündliche Verhandlung vom
17. Mai 2004 durch den Vorsitzenden Richter Dipl.-Phys. Dr. Anders, die Richter
Dipl.-Ing. Obermayer und Dipl.-Phys. Dr. Hartung sowie die Richterin Martens


beschlossen:


        Die Beschwerde wird zurückgewiesen.


                                       Gründe


                                         I


Das Patent 197 33 748 wurde wegen fehlender erfinderischer Tätigkeit widerrufen.


Die Patentinhaberin und Beschwerdeführerin stellt den Antrag,


        das Patent mit den Patentansprüchen 1 bis 8 gemäß Hauptantrag,
        hilfsweise mit den Patentansprüchen 1 bis 8 gemäß den Hilfsanträgen I bis III, jeweils überreicht in der mündlichen Verhandlung,
        aufrechtzuerhalten.


Sie erklärt die Teilung des Patents.


Die Patentinhaberin regt an, zu der in der mündlichen Verhandlung überreichten
Rechtsfrage zur Beurteilung der erfinderischen Tätigkeit die Rechtsbeschwerde
zuzulassen.

                                        -3-



Die Einsprechende und Beschwerdegegnerin stellt den Antrag,


       die Beschwerde zurückzuweisen.


Der Patentanspruch 1 nach Hauptantrag lautet wie folgt (mit eingefügten Gliederungszeichen A) und B)):


       "1. Datenübertragungsvorrichtung zur unidirektionalen seriellen
       Datenübertragung von einer Sendeeinrichtung (10) zu einer Empfangseinrichtung (20), insbesondere von einem Mikrokontroller (µC) zu einem Endstufen-IC (ICE) von einem Kraftfahrzeug-Steuergerät, mit:


       einer in der Sendeeinrichtung (10) vorgesehenen P/S-Umwandlungseinrichtung (100, 105, 110) zum Umwandeln eines in der
       Sendeeinrichtung (10) bereitgestellten parallelen Datenstroms in
       einen   seriellen   Datenstrom   (SDATA)   mit   Übertragungsrahmen (U1, U2, U3) eines vorbestimmten Formats und zum Übertragen des seriellen Datenstroms (SDATA) zur Empfangseinrichtung (20) über einen Datenübertragungskanal (DS);


       einer in der Empfangseinrichtung (20) vorgesehenen S/P-Umwandlungseinrichtung (200, 205, 210) zum Rückumwandeln des
       übertragenen seriellen Datenstroms (SDATA) in den parallelen
       Datenstrom;


       einer einzelnen Taktsignal-Erzeugungseinrichtung zum Erzeugen
       eines Taktsignals (CLK) und zum Zuführen des Taktsignals (CLK)
       an die P/S-Umwandlungseinrichtung (100, 105, 110) und die S/P-Umwandlungseinrichtung (200, 205, 210), um den jeweiligen Um-

                                -4-



wandlungsbetrieb kontinuierlich und mit phasengleichem Takt
durchzuführen; und


einer Synchronisierungseinrichtung (120) zum Erzeugen eines
Synchronisierungssignals (SYNC) entsprechend dem Umwandlungsbetrieb der P/S-Umwandlungseinrichtung (100, 105, 110)
und zum Zuführen desselben an die S/P-Umwandlungseinrichtung (200, 205, 210) zur Synchronisierung des jeweiligen Umwandlungsbetriebs;


dadurch g e k e n n z e i c h n e t , daß


die P/S-Umwandlungseinrichtung (100, 105, 110) aufweist:


     ein mit dem Taktsignal (CLK) getaktetes Eingangsregister (100) zum Empfangen des parallelen Datenstroms
     an einem parallelen Eingang (101) und zum Ausgeben
     eines entsprechenden parallelen Ausgangssignals an
     einem parallelen Ausgang (102);


     ein mit dem Taktsignal (CLK) getaktetes erstes Schieberegister (110) mit einem parallelen Eingang (111)
     zum Empfangen des parallelen Ausgangssignals und
     mit einem seriellen Ausgang (112) zum Ausgeben des
     seriellen Datenstroms an den Datenübertragungskanal (DS); und


     einen ersten internen Bus (105) zur Verbindung des
     Ausgangs (102) des Eingangsregisters (100) mit dem
     Eingang (111) des ersten Schieberegisters (110);

                              -5-



die S/P-Umwandlungseinrichtung (200, 205, 210) aufweist:


     ein mit dem Taktsignal (CLK) getaktetes zweites Schieberegister (200) zum Empfangen des seriellen Datenstroms an einem seriellen Eingang (201) und zum Ausgeben eines entsprechenden parallelen Ausgangssignals an einem parallelen Ausgang (202);


     ein mit dem Taktsignal (CLK) getaktetes Ausgangsregister (210) zum Empfangen des parallelen Ausgangssignals des zweiten Schieberegisters (200) an einem parallelen Eingang (211) und zum Ausgeben des parallelen Datenstroms an einem parallelen Ausgang (212);
     und


     einen zweiten internen Bus (205) zur Verbindung des
     Ausgangs (202) des Schieberegisters (200) mit dem
     Eingang (211) des Ausgangsregisters (210);


die Synchronisierungseinrichtung (120) eine einzelne mit dem
Taktsignal (CLK) getaktete Zähleinrichtung (120) zum Erzeugen
eines Synchronisierungsimpulses (SYNC) nach jeweils einem vorbestimmbaren Zählzyklus entsprechend dem vorbestimmten Format des Übertragungsrahmens (U1, U2, U3) aufweist; und


das erste Schieberegister (110) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des über den ersten internen Bus (105)
übertragenen   Ausgangssignals   des   Eingangsregisters      (100)
steuerbar ist und das Ausgangsregister (210) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des über den zweiten in-

                                       -6-



       ternen Bus (205) übertragenen parallelen Ausgangssignals des
       zweiten Schieberegisters (200) steuerbar ist;


       wobei die Zähleinrichtung (120) eine Abwärtszähleinrichtung und
       der Zählzyklus ein Abwärtszählzyklus ist; A) und


       der Synchronisierungsimpuls (SYNC) über eine separate Synchronisierungsleitung (140) an das erste Schieberegister (110) und
       das Ausgangsregister (210) übertragen wird B)."


Im Patentanspruch 1 nach Hilfsantrag I ist nach dem Gliederungszeichen A) das
Wort "und" gestrichen und nach dem Gliederungszeichen B) ist eingefügt


       "; und wobei eine Rücksetzsignalleitung (160) zur Übertragung eines Rücksetzimpuls (RESET) vorgesehen ist, die an das Eingangsregister (100), das erste Schieberegister (110), die Zähleinrichtung (120), das zweite Schieberegister (200) und das Ausgangsregister (210) angeschlossen ist".


Im Patentanspruch 1 nach Hilfsantrag II sind die beiden letzten Absätze im Patentanspruch 1 nach Hauptantrag in ihrer Reihenfolge vertauscht - ohne inhaltliche
Änderung -, der Punkt nach dem beibehaltenen Gliederungszeichen B) ist ersetzt
durch ein Semikolon, das Wort "und" nach dem ebenfalls beibehaltenen Gliederungszeichen A) ist ersetzt durch die folgenden Merkmale (mit zusätzlich eingefügtem Gliederungszeichen C)):


       "wobei das vorbestimmte Format des Übertragungsrahmens (U1,
       U2, U3) ein aus einer vorbestimmten Anzahl von Bits bestehendes
       Datenwort (DATA_WORT; b0 - b7) und ein Paritätsbit (PB) aufweist, das Datenwort (DATA_WORT; b0 - b7) dem vom Eingangsregister (100) am parallelen Ausgang (102) ausgegebenen Aus-

                                      -7-



       gangssignal entspricht, und die Breite des ersten und zweiten
       Schieberegisters (110; 200) der Bitbreite des vorbestimmten Formats entspricht; und


       wobei die P/S-Umwandlungseinrichtung (100, 105, 110) einen mit
       dem ersten internen Bus (105) und dem ersten Schieberegister (110) verbundenen ersten Paritätsgenerator (130) zum Erzeugen des den Datenwortbits entsprechenden Paritätsbits (PB) und
       Eingeben desselben in das erste Schieberegister (110) aufweist
       und das erste Schieberegister (110) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des Paritätsbits (PB) steuerbar ist;
       und


       wobei die S/P-Umwandlungseinrichtung (200, 205, 210) einen mit
       dem zweiten internen Bus (205) und dem Ausgangsregister (210)
       verbundenen zweiten Paritätsgenerator (230) zum Erzeugen des
       den Datenbits des Übertragungsrahmens entsprechenden Paritätsbits (PB) und Eingeben desselben als Ladesignal in das Ausgangsregister (210) aufweist, welches ein Einlesen fehlübertragener Übertragungsrahmen (U1, U2, U3) in das Ausgangsregister (210) verhindert C)."


Im Patentanspruch 1 nach Hilfsantrag III ist nach dem Gliederungszeichen C) des
Patentanspruchs 1 nach Hilfsantrag II - wie auch beim Patentanspruch 1 nach
Hilfsantrag I nach dem dortigen Gliederungszeichen B) - eingefügt:


     "; und wobei eine Rücksetzsignalleitung (160) zur Übertragung eines
     Rücksetzimpuls (RESET) vorgesehen ist, die an das Eingangsregister (100), das erste Schieberegister (110), die Zähleinrichtung (120),
     das zweite Schieberegister (200) und das Ausgangsregister (210) angeschlossen ist".

                                       -8-



Erörtert wurden ua die folgenden, vom Senat in das Verfahren eingeführten Entgegenhaltungen:


        D5 US 4 710 922 und
        D6 US 5 465 079,


und der - bereits im Einspruchsverfahren vor dem Patentamt genannte - Lehrbuchauszug


        D4 Tietze,   U.,   Schenk,   Ch.:    "Halbleiter-Schaltungstechnik",
            9. Aufl., Springer-Verlag Berlin ua,1990, Seiten 682 bis 685.


Die Patentinhaberin führt aus, der Patentgegenstand sei gegenüber dem Stand
der Technik patentfähig. Nach ihrer Auffassung konnte der Fachmann zum Anmeldetag des Streitpatents aus dem Stand der Technik keinerlei Anregung erhalten
zu Datenübertragungsvorrichtungen gemäß den Patentansprüchen 1 nach Hauptantrag oder Hilfsanträgen. Insbesondere böte der Stand der Technik nach der
Druckschrift D5 dem Fachmann keine Veranlassung dafür, die dort beschriebene
Synchronisierung des Daten-Umwandlungsbetriebs mittels im Datenstrom eingelagerter SYNC-Worte aufzugeben und eine Synchronisierung in Betracht zu ziehen
mittels eines Synchronisierungsimpulses, welcher außerdem über eine separate
Synchronisierungsleitung übertragen wird. Auch sei keine Veranlassung für den
Fachmann erkennbar, ausgehend von der Druckschrift D5 die Druckschrift D6 in
seine Überlegungen einzubeziehen. Überdies hätte der Fachmann - ausgehend
von der D5 - mehrere Gedankenschritte bewältigen müssen, die zumindest in ihrer
Gesamtheit auf einer erfinderischen Tätigkeit beruhten.


Die Einsprechende vertritt die Auffassung, keiner der beanspruchten Gegenstände
beruhe in Anbetracht des durch die im Verfahren befindlichen Druckschriften belegten Standes der Technik auf erfinderischer Tätigkeit.

                                         -9-



Wegen weiterer Einzelheiten, auch zur von der Patentinhaberin vorgelegten
Rechtsfrage, wird auf den Akteninhalt verwiesen.


                                           II


1. Die Beschwerde der Patentinhaberin hat keinen Erfolg. Das Patent ist nicht
rechtsbeständig, sein Gegenstand nach den §§ 1 und 4 PatG nicht patentfähig.
Die Gegenstände der Patentansprüche 1 gemäß Hauptantrag und gemäß den
Hilfsanträgen I, II und III beruhen nicht auf einer erfinderischen Tätigkeit.


Zum Hauptantrag


Der Patentanspruch 1 des Hauptantrags ist weiter gefaßt als die Patentansprüche 1 nach den Hilfsanträgen I bis III und enthält insbesondere den Gegenstand
des Patentanspruchs 1 nach Hilfsantrag III. Nachdem letzterer - wie die nachfolgenden Ausführungen zum Hilfsantrag III zeigen - nicht auf einer erfinderischen
Tätigkeit beruht, ist der Patentanspruch 1 nach Hauptantrag nicht rechtsbeständig.


Zu den Hilfsanträgen I und II


Auch die Patentansprüche 1 nach den Hilfsanträgen I und II umfassen jeweils den
Gegenstand der Patentanspruchs 1 nach Hilfsantrag III und sind wie dieser ebenfalls nicht rechtsbeständig. Zur Begründung wird ebenso wie betreffs des Patentanspruchs 1 nach Hauptantrag auf die nachfolgenden Ausführungen zum Gegenstand der Patentanspruchs 1 nach Hilfsantrag III verwiesen.


Zum Hilfsantrag III


a) Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag III ist dem Fachmann
durch D5 in Verbindung mit seinem Fachwissen und Fachkönnen nahegelegt.
Fachmann ist ein Diplom-Ingenieur mit einem Hochschulabschluß in Elektrotech-

                                         - 10 -



nik, der Datenübertragungssysteme entwickelt und dabei mit Systemanwendungen der seriellen Datenübertragung vertraut ist, und der insbesondere verschiedene Verfahren zur Synchronisation der Datenübertragung kennt.


b) Patentanspruch 1 nach Hilfsantrag III beschreibt - nach Merkmalen gegliedert –
eine


0.     Datenübertragungsvorrichtung zur unidirektionalen seriellen Datenübertragung von einer Sendeeinrichtung (10) zu einer Empfangseinrichtung (20), insbesondere von einem Mikrokontroller (µC) zu einem Endstufen-IC (ICE) von einem Kraftfahrzeug-Steuergerät, mit:


1.     einer in der Sendeeinrichtung (10) vorgesehenen P/S-Umwandlungseinrichtung (100, 105, 110) zum Umwandeln eines in der Sendeeinrichtung (10) bereitgestellten parallelen Datenstroms in einen seriellen Datenstrom (SDATA) mit Übertragungsrahmen (U1, U2, U3) eines vorbestimmten   Formats    und   zum    Übertragen   des   seriellen   Datenstroms (SDATA) zur Empfangseinrichtung (20) über einen Datenübertragungskanal (DS);


2.     einer in der Empfangseinrichtung (20) vorgesehenen S/P-Umwandlungseinrichtung (200, 205, 210) zum Rückumwandeln des übertragenen seriellen Datenstroms (SDATA) in den parallelen Datenstrom;


3.     einer einzelnen Taktsignal-Erzeugungseinrichtung zum Erzeugen eines
       Taktsignals (CLK) und zum Zuführen des Taktsignals (CLK) an die
       P/S-Umwandlungseinrichtung (100, 105, 110) und die S/P-Umwandlungseinrichtung (200, 205, 210), um den jeweiligen Umwandlungsbetrieb kontinuierlich und mit phasengleichem Takt durchzuführen; und

                                        - 11 -



4.   einer Synchronisierungseinrichtung (120) zum Erzeugen eines Synchronisierungssignals (SYNC) entsprechend dem Umwandlungsbetrieb der
     P/S-Umwandlungseinrichtung (100, 105, 110) und zum Zuführen desselben an die S/P-Umwandlungseinrichtung (200, 205, 210) zur Synchronisierung des jeweiligen Umwandlungsbetriebs;


dadurch g e k e n n z e i c h n e t , daß


5.   die P/S-Umwandlungseinrichtung (100, 105, 110) aufweist:


     5.1 ein mit dem Taktsignal (CLK) getaktetes Eingangsregister (100)
           zum Empfangen des parallelen Datenstroms an einem parallelen
           Eingang (101) und zum Ausgeben eines entsprechenden parallelen Ausgangssignals an einem parallelen Ausgang (102);


     5.2 ein mit dem Taktsignal (CLK) getaktetes erstes Schieberegister (110) mit einem parallelen Eingang (111) zum Empfangen des
           parallelen Ausgangssignals und mit einem seriellen Ausgang (112)
           zum Ausgeben des seriellen Datenstroms an den Datenübertragungskanal (DS); und


     5.3 einen ersten internen Bus (105) zur Verbindung des Ausgangs (102) des Eingangsregisters (100) mit dem Eingang (111)
           des ersten Schieberegisters (110);


6.   die S/P-Umwandlungseinrichtung (200, 205, 210) aufweist:


     6.1 ein mit dem Taktsignal (CLK) getaktetes zweites Schieberegister (200) zum Empfangen des seriellen Datenstroms an einem seriellen Eingang (201) und zum Ausgeben eines entsprechenden
           parallelen Ausgangssignals an einem parallelen Ausgang (202);

                                      - 12 -



     6.2 ein mit dem Taktsignal (CLK) getaktetes Ausgangsregister (210)
          zum Empfangen des parallelen Ausgangssignals des zweiten
          Schieberegisters (200) an einem parallelen Eingang (211) und
          zum Ausgeben des parallelen Datenstroms an einem parallelen
          Ausgang (212); und


     6.3 einen zweiten internen Bus (205) zur Verbindung des Ausgangs (202) des Schieberegisters (200) mit dem Eingang (211)
          des Ausgangsregisters (210);


7.   die Synchronisierungseinrichtung (120) eine einzelne mit dem Taktsignal (CLK) getaktete Zähleinrichtung (120) zum Erzeugen eines Synchronisierungsimpulses (SYNC) nach jeweils einem vorbestimmbaren
     Zählzyklus entsprechend dem vorbestimmten Format des Übertragungsrahmens (U1, U2, U3) aufweist; und


8.   das erste Schieberegister (110) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des über den ersten internen Bus (105)
     übertragenen Ausgangssignals des Eingangsregisters (100) steuerbar
     ist und das Ausgangsregister (210) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des über den zweiten internen Bus (205)
     übertragenen parallelen Ausgangssignals des zweiten Schieberegisters (200) steuerbar ist;


9.   der Synchronisierungsimpuls (SYNC) über eine separate Synchronisierungsleitung (140) an das erste Schieberegister (110) und das Ausgangsregister (210) übertragen wird;


10. wobei die Zähleinrichtung (120) eine Abwärtszähleinrichtung und der
     Zählzyklus ein Abwärtszählzyklus ist;

                                       - 13 -



11. wobei das vorbestimmte Format des Übertragungsrahmens (U1, U2,
    U3) ein aus einer vorbestimmten Anzahl von Bits bestehendes Datenwort (DATA_WORT; b0 - b7) und ein Paritätsbit (PB) aufweist, das Datenwort (DATA_WORT; b0 - b7) dem vom Eingangsregister (100) am
    parallelen Ausgang (102) ausgegebenen Ausgangssignal entspricht,
    und die Breite des ersten und zweiten Schieberegisters (110; 200) der
    Bitbreite des vorbestimmten Formats entspricht; und


    11.1 wobei die P/S-Umwandlungseinrichtung (100, 105, 110) einen mit
           dem ersten internen Bus (105) und dem ersten Schieberegister (110) verbundenen ersten Paritätsgenerator (130) zum Erzeugen des den Datenwortbits entsprechenden Paritätsbits (PB) und
           Eingeben desselben in das erste Schieberegister (110) aufweist
           und das erste Schieberegister (110) durch den Synchronisierungsimpuls (SYNC) zum Einlesen des Paritätsbits (PB) steuerbar ist;
           und


    11.2 wobei die S/P-Umwandlungseinrichtung (200, 205, 210) einen mit
           dem zweiten internen Bus (205) und dem Ausgangsregister (210)
           verbundenen zweiten Paritätsgenerator (230) zum Erzeugen des
           den Datenbits des Übertragungsrahmens entsprechenden Paritätsbits (PB) und Eingeben desselben als Ladesignal in das Ausgangsregister (210) aufweist, welches ein Einlesen fehlübertragener Übertragungsrahmen (U1, U2, U3) in das Ausgangsregister (210) verhindert; und


12. wobei eine Rücksetzsignalleitung (160) zur Übertragung eines Rücksetzimpuls (RESET) vorgesehen ist, die an das Eingangsregister (100),
    das erste Schieberegister (110), die Zähleinrichtung (120), das zweite
    Schieberegister (200) und das Ausgangsregister (210) angeschlossen
    ist.

                                      - 14 -



c) Aus der Druckschrift D5, vgl die Figur 1 und Spalte 4 Zeile 13 bis Spalte 5 Zeile 18, ist eine Datenübertragungsvorrichtung zur unidirektionalen seriellen Datenübertragung (Transmission Media 107) von einer Sendeeinrichtung 101, 102, 103
zu einer Empfangseinrichtung 104, 105, 106 als bekannt entnehmbar (Merkmal 0).


In der Sendeeinrichtung ist eine P/S-Umwandlungseinrichtung (insbesondere Input Latch 601 und Schieberegister 606, vgl die Fig 6 in Verbindung mit Fig 2 und
3, Sp 8 Z 46-49, Sp 16 Z 5–16, Z 28-39) vorgesehen, zum Umwandeln eines in
der Sendeeinrichtung bereitgestellten parallelen Datenstroms (Data/Command
Signals 201, Fig 2, 3 und 6) in einen seriellen Datenstrom (Serout 205) mit Übertragungsrahmen eines vorbestimmten Formats (vgl Fig 10, insbesondere unter 8.,
9. und 10.) und zum Übertragen des seriellen Datenstroms zur Empfangseinrichtung über einen Datenübertragungskanal (Transmission Media 107 – Merkmal 1).


In der Empfangseinrichtung ist eine S/P-Umwandlungseinrichtung (insbesondere
Schieberegister 1601 und Parallel Output Latch 1604, vgl die Fig 16 in Verbindung
mit Fig 12 und 13, Sp 22 Z 57-60, Sp 25 Z 67 bis Sp 26 Z 3, Sp 26 Z 45-59) vorgesehen zum Rückumwandeln des übertragenen seriellen Datenstroms (Fig 12, 13
und 16, Serin 1206) in den parallelen Datenstrom (Data/Command 1201 – Merkmal 2).


Takterzeugungseinrichtungen sind sowohl für den Sender als auch für den Empfänger vorgesehen (Fig 6 und 16, Takterzeugungseinrichtungen 605, 1607), die jeweils an die P/S-Umwandlungseinrichtung und an die S/P-Umwandlungseinrichtung ein Taktsignal zuführen (Fig 6 Bit Clock 696, Fig 16 Bit Clock 1685), um den
jeweiligen Umwandlungsbetrieb kontinuierlich und mit phasengleichem Takt
durchzuführen (Sp 25 Z 36-66). Der Begriff "mit phasengleichem Takt" im Patentanspruch 1 ist dabei - auch nach Auffassung der Patentinhaberin - zu verstehen
als "Takt mit gleicher Frequenz", wie dies auch bei der aus D5 als bekannt entnehmbaren Vorrichtung der Fall ist (Teil von Merkmal 3).

                                      - 15 -



Weiter ist bei der D5 eine Synchronisierungseinrichtung vorgesehen zum Erzeugen eines Synchronisierungssignals (SYNC (-Worte); Fig 10 und 19) entsprechend dem Umwandlungsbetrieb der P/S-Umwandlungseinrichtung und zum Zuführen desselben an die S/P-Umwandlungseinrichtung zur Synchronisierung des
jeweiligen Umwandlungsbetriebs (vgl Fig 10, insbesondere unter 8., 9. und 10.;
Fig 16 Byte Sync Logic 1608, dazu Einzelheiten in Fig 18; Fig 19, insbesondere
unter 1., 2., 3., 6. und 7.; Sp 16 Z 40 bis Sp 17 Z 2, Sp 18 Z 6-19, Z 28-31; Sp 26
Z 7-37, Fig 18 – Merkmal 4).


Die aus D5 als bekannt entnehmbare P/S-Umwandlungseinrichtung, vgl Figur 6,
weist auf


-   ein mit einem Taktsignal (von Clock Gen 605 über Strb/Ack Ckt 604) getaktetes Eingangsregister (Input Latch 601) zum Empfangen des parallelen Datenstroms (DATA) an einem parallelen Eingang (0, 1, 2...) und zum Ausgeben eines entsprechenden parallelen Ausgangssignals an einem parallelen Ausgang
    (Merkmal 5.1);


-   ein mit obigem Taktsignal getaktetes erstes Schieberegister 606 mit einem parallelen Eingang zum Empfangen des parallelen Ausgangssignals und mit einem seriellen Ausgang 697 zum Ausgeben des seriellen Datenstroms an den
    Datenübertragungskanal (Serout+, Serout-; Merkmal 5.2); und


-   einen ersten internen Bus zur Verbindung des Ausgangs des Eingangsregisters 601 mit dem Eingang des ersten Schieberegisters 606 (Fig 6, Bus zur
    Verbindung von 601 nach 606 – Merkmal 5.3).

                                        - 16 -



Die aus D5 als bekannt entnehmbare S/P-Umwandlungseinrichtung, vgl Figur 16,
weist auf


-   ein mit einem Taktsignal (von PLL Clock Generator 1606 und Clock
    Gen 1607) getaktetes zweites Schieberegister 1601 zum Empfangen des seriellen Datenstroms (Serin+, Serin-) an einem seriellen Eingang (NRZ) und
    zum Ausgeben eines entsprechenden parallelen Ausgangssignals an einem
    parallelen Ausgang (Merkmal 6.1);


-   ein mit vorgenanntem Taktsignal getaktetes Ausgangsregister 1604 zum Empfangen des parallelen Ausgangssignals des zweiten Schieberegisters 1601 an
    einem parallelen Eingang und zum Ausgeben des parallelen Datenstroms an
    einem parallelen Ausgang (DATA – Merkmal 6.2); und


-   einen zweiten internen Bus zur Verbindung des Ausgangs des Schieberegisters 1601 mit dem Eingang des Ausgangsregisters 1604 (Fig 16, Bus zur Verbindung von 1601 nach 1604 – Merkmal 6.3).


Die aus D5 bekannte Synchronisierungseinrichtung (Fig 6, SIDQ 608, Sp 16 Z 44
bis Sp 17 Z 2) weist zwar ebenfalls eine mit einem Taktsignal der Sendeeinrichtung getaktete Zähleinrichtung auf (Fig 6, Taktsignal-Erzeugungseinrichtung 605,
Fig 8, Zähler 852, Sp 13 Z 39-43, Z 61 bis Sp 14 Z 22, Sp 14 Z 58 bis Sp 15 Z 5),
diese erzeugt auch Ladesignale auf Leitung 630 und Synchronisierungssignale
nach jeweils einem vorbestimmbaren Zählzyklus entsprechend dem vorbestimmten Format des Übertragungsrahmens (byte boundary), jedoch werden diese Synchronisierungssignale als Synchronisierungsworte erzeugt, nicht als Synchronisierungsimpulse (SYNC (-Worte), Fig 10 und 19, in Verbindung mit Sp 16 Z 17-25,
Sp 16 Z 44 bis Sp 17 Z 2). Entsprechend werden in der Empfangseinrichtung nach
D5 Taktsignal und Synchronisierungssignal aus dem von der Sendeeinrichtung
übertragenen Datenstrom zurückgewonnen, Spalte 25 Zeilen 36 bis 39, Spalte 26
Zeilen 4 bis 37 und Zeilen 45 bis 59 in Verbindung mit den Figuren 16 und 18. Er-

                                        - 17 -



stes (Fig 6, 606) und zweites (Fig 16, 1601) Schieberegister, resp Eingangs- und
Ausgangsregister, sind durch diese Takt- und Synchronisierungssignale (Synchronisierungsworte) der Sendeeinrichtung, resp der Empfangseinrichtung, nach D5
insbesondere zum Einlesen der jeweiligen Ausgangssignale steuerbar, vgl die Figur 10 in Verbindung mit Spalte 17 Zeile 25 bis Spalte 18 Zeile 36 und die Figur 19 in Verbindung mit Spalte 28 Zeile 24 bis Spalte 29 Zeile 17 (Teile aus
Merkmalen 7, 8 und 9). Die Festlegung der Zähleinrichtung (Master Counter 852
in Fig 8) als eine Abwärtszähleinrichtung - und entsprechend des Zählzyklus als
einen Abwärtszählzyklus - liegt dabei im Belieben des Fachmanns (Merkmal 10).


Die aus D5 als bekannt entnehmbare Vorrichtung weist somit im Gegensatz zu
der des Patentanspruchs 1 nach Hilfsantrag III nicht eine einzelne Taktsignal-Erzeugungseinrichtung auf, und die bekannte Sychronisierungseinrichtung beruht
auf der Übertragung der Rückgewinnung des Taktes aus dem Datenstrom und
von Synchronisierungsworten, demzufolge weist die bekannte Vorrichtung auch
keine separate Synchronisierungsleitung im anspruchsgemäßen Sinn auf, über die
ein Synchronisierungsimpuls an das erste Schieberegister und an das Ausgangsregister übertragen wird (Merkmal 9).


Das nach D5 vorbestimmte Format des Übertragungsrahmens entspricht wiederum dem vom Eingangsregister am parallelen Ausgang ausgegebenen Ausgangssignal und der Breite des ersten und zweiten Schieberegisters (Fig 6, 601, 606,
Fig 16, 1601) und weist ein aus einer vorbestimmten Anzahl von Bits bestehendes
Datenwort und ein Paritätsbit auf (Sp 4 Z 33-49, Sp 19 Z 20-25 – Merkmal 11). Ein
erster und zweiter Paritätsgenerator entsprechend den Merkmalen 11.1 und 11.2
des Anspruchs 1 werden in der D5 jedoch nicht beschrieben.


Auch beschreibt die D5 keinen Rücksetzimpuls und keine zugehörige Rücksetzleitung (Merkmal 12).

                                     - 18 -



d) Einen solchen Rücksetzimpuls - und den damit verbundenen definierten Zustand einer elektronischen Schaltung, zB nach deren Einschalten - sieht der Fachmann aber grundsätzlich vor. Ein solches Vorgehen gehört zu seinen Grundkenntnissen, wie sie bspw durch den Lehrbuchauszug D4, Seite 684 letzter Absatz bis
Seite 85 erster Absatz nach der Abb. 21.21, dokumentiert sind. Insbesondere belegt das vorgenannte Zitat auch das Vorsehen eines Hardware-RESET mit entsprechendem Anschluß (Rücksetzsignalleitung) an die rückzusetzenden Komponenten (Merkmal 12).


Im Zusammenhang mit der seriellen Datenübertragung ist dem Fachmann auch
die Verwendung von Paritätsbits geläufig (D4, S 683, vierter Absatz, Abb. 21.19),
die außerdem bereits in der D5 erwähnt sind (Sp 4 Z 33-49). Da Paritätsbits nach
dem Verständnis des Fachmanns verhindern sollen, daß fehlerhaft übertragene
Daten weiterbearbeitet werden, sieht der Fachmann nicht nur Bauteile vor zur Erzeugung und Überprüfung von Paritätsbits (Paritätsgeneratoren), sondern sorgt
auch dafür, daß ein Einlesen fehlerhaft übertragener Übertragungsrahmen in das
Ausgangsregister verhindert wird, indem Paritätsbits erzeugende und prüfende
Systemkomponenten zweckentsprechend miteinander verschaltet werden (Merkmale 11.1 und 11.2).


Ebenso ist dem Fachmann bei Datenübertragungsvorrichtungen zur seriellen Datenübertragung auch das zentrale Problem der Synchronisation gegenwärtig, siehe dazu ebenfalls die D4, S 683, dritter und vierter Absatz. Der Fachmann kennt
aus seinem Fachwissen heraus - außer dem in D5 beschriebenen Verfahren einer
Synchronisation mittels Synchronisationsworten - weitere Arten der Synchronisation, er wägt deren Vor- und Nachteile ab und versteht es, das Synchronisationsverfahren auszuwählen und zum Einsatz zu bringen, das insbesondere dem Systemumfeld - hier einem Kraftfahrzeug - angemessen ist und welches überdies im
jeweiligen Praxisfall seinem allgemeinen Streben nach Vereinfachung entgegenkommt.

                                      - 19 -



Eine solche weitere Art der Synchronisation ist die Verwendung eines Taktsignals
eines einzelnen Taktgenerators. Daß sie dem Fachmann - gerade auch als Anwendung in einem Kraftfahrzeug – bekannt ist, belegt Druckschrift D6 (Fig 1). Die
in D6 beschriebene Datenübertragungsvorrichtung zur seriellen Datenübertragung
weist eine Sendeeinrichtung (Fig 5, 320, 322, 324) und eine Empfangseinrichtung
(Fig 8 und 9, 502, 516, 518, 504) auf. Eine einzelne Taktsignalerzeugungseinrichtung 312, 314 erzeugt ein Taktsignal, das der P/S-Umwandlungseinrichtung 304a,
304b, 310 und der S/P-Umwandlungseinrichtung 504, 556 - über eine separate
Taktleitung (Fig 5, 8 und 9, Serial Clock) - zugeführt wird, um den jeweiligen Umwandlungsbetrieb kontinuierlich und mit phasengleichem Takt durchzuführen
(Sp 16 Z 7-25 – Merkmal 3 und auf die einzelne Taktsignalerzeugungseinrichtung
und das (einzige) Taktsignal bezogene Teil-Merkmale aus 5.1, 5.2, 5.3, 6.1, 6.2,
6.3, 7).


Des weiteren weist die in D6 beschriebene Datenübertragungsvorrichtung eine
Synchronisierungseinrichtung 312 auf, die in Abhängigkeit von dem Taktsignal
(von 314) getaktete Synchronisierungsimpulse (Frame Sync) erzeugt nach jeweils
einem vorbestimmbaren (Zähl-) Zyklus entsprechend dem vorbestimmten Format
des Übertragungsrahmens, Figur 5, Spalte 16 Zeilen 18-25 (auf den Synchronisierungsimpuls bezogene Teile aus den Merkmalen 7 und 8).


Der Synchronisierungsimpuls gemäß D6 wird über eine separate Synchronisierungsleitung (Frame Sync, Fig 5, 8, 9) von der Sende- zur Empfangseinrichtung
übertragen (Teil-Merkmal 9). Die Erzeugung des Synchronisierungsimpulses und
seine Verwendung in Sende- und Empfangseinrichtung, insbesondere dessen Zuführung zu den zu synchronisierenden Bauteilen (erstes und zweites Schieberegister, Eingangs- und Ausgangsregister) erfolgt dabei in analoger Weise zum Stand
der Technik nach der Druckschrift D5, insbesondere Fig 6 mit 8 und 16 mit 18
(Merkmale 7 bis 10).

                                        - 20 -



Die in D6 beschriebene und als "well known in the art" bezeichnete (Sp 16 Z 23-
25) zentrale Synchronisation mit einem einzelnen Taktsignalgenerator anstelle der
Synchronisation durch Taktwiedergewinnung und Übertragung von Synchronisationsworten nach D5 zieht der Fachmann in Betracht, wenn der Vorteil geringeren
Schaltungsaufwands den Nachteil zusätzlicher Leitungen überwiegt. Dies ist bei
kurzen Entfernungen wie in Kraftfahrzeugen der Fall, vergl. D6.


e) Damit ist der Fachmann aber ohne erfinderische Überlegungen bereits zum Gegenstand des Patentanspruchs 1 nach Hilfsantrag III gelangt.


Zwar mag, wie die Patentinhaberin und Beschwerdeführerin argumentiert, die Gesamtheit der vorstehend erörterten vom Stand der Technik zum Anspruchsgegenstand führenden Maßnahmen formal in mehrere gesonderte Maßnahmen (Schritte) auflösbar sein, jedoch handelt es sich dabei – wie vorstehend aufgezeigt – lediglich um eine routinemäßige Anwendung des dem Fachmann zur Verfügung stehenden Wissens und Könnens hinsichtlich einer dem Systemumfeld angepaßten
Synchronisation einer seriellen Datenübertragung unter der Randbedingung, Ressourcen wirtschaftlich einzusetzen, insbesondere unnötigen Aufwand zu vermeiden. Dabei wird der Rahmen fachmännischen Handelns nicht verlassen. Überraschende kombinatorische Wirkungen, die diese Schlußfolgerung in Frage stellen
könnten, sind nicht ersichtlich. Vorliegend geht es bei der Beurteilung der erfinderischen Tätigkeit nicht um die Frage, ob die Kombination der Druckschrift D5 mit der
Druckschrift D6 nahe liegt, sondern dann, daß der Fachmann anstelle des in D5
beschriebenen Synchronisationsverfahrens ein anderes bekanntes in Betracht
zieht, wie es in D6 beschrieben ist.


Auch die weiteren Einwände der Patentinhaberin, der Fachmann hätte hinsichtlich
des im Streitpatent vorliegenden Anwendungsfalles "Kraftfahrzeug" gewissermaßen ein Vorurteil überwinden müssen, um, ausgehend von Druckschrift D5, zum
Gegenstand des Anspruchs 1 zu gelangen, und er ziehe eine Synchronisierung
nach D6 nicht in Betracht, da letztere diametral verschieden sei von der in D5 be-

                                      - 21 -



schriebenen, greifen nicht durch, weil gerade auch die in D6 beschriebene Vorrichtung ihre Anwendung im Kraftfahrzeug-Bereich findet.


Schließlich hätte auch eine unmittelbare Verbindung des Ausgangs des Eingangsregisters mit dem Eingang des ersten Schieberegisters resp eine solche des Ausgangs des zweiten Schieberegisters mit dem Eingang des Ausgangsregisters jeweils über einen internen Bus (Merkmale 5.3 und 6.3) das Vorliegen einer erfinderischen Tätigkeit bei der Datenübertragungsvorrichtung des Anspruchs 1 nach
Hilfsantrag III nicht begründen können. Eine solche unmittelbare Verbindung wird
zwar durch die vorliegende Formulierung des Anspruchs 1 ohnehin nicht gestützt,
wurde aber von der Patentinhaberin hinsichtlich der internen Bussysteme nach D5
ins Feld geführt, bei der weitere Bauteile zu (De-) Codierungszwecken der Daten
an den Bus angeschlossen sind (D5, Fig 6 und 16). Wenn im Einzelfall eine Umcodierung in ein spezielles Format, wie den NRZ-Code nach D5, nicht notwendig
ist, verzichtet der Fachmann selbstverständlich auf die entsprechenden – überflüssigen - Systemkomponenten und wäre somit naheliegenderweise auch zu einer
unmittelbaren Verbindung im oben angesprochenen Sinne gelangt.


2. Für eine Zulassung der Rechtsbeschwerde gemäß § 100 Abs 2 PatG besteht
keine Veranlassung. Weder kommt der Rechtsfrage grundlegende Bedeutung zu,
noch ist eine Entscheidung des Bundesgerichtshofes zur Fortbildung des Rechts
oder zur Sicherung einer einheitlichen Rechtsprechung erforderlich.




Dr. Anders              Obermayer               Dr. Hartung              Martens




                                                                               Pü
