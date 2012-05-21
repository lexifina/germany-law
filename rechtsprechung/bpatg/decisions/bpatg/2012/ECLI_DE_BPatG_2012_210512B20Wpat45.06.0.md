---
ecli: "ECLI:DE:BPatG:2012:210512B20Wpat45.06.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 45/06"
decided: "2012-05-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2012&Sort=1&Seite=39&nr=23647&anz=1451&pos=599&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2012-05-21_20_W-pat_45_06_NA_0.txt"
---

# Bundespatentgericht, 20 W (pat) 45/06 vom 2012-05-21

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 45/06                                                      Verkündet am
_______________                                                        21. Mai 2012
    (Aktenzeichen)                                                          …




                              BESCHLUSS

                            In der Beschwerdesache


                betreffend die Patentanmeldung 43 93 148.0-51


…




hat der 20. Senat (Technischer Beschwerdesenat) auf die mündliche Verhandlung
vom 21. Mai 2012 durch den Vorsitzenden Richter Dipl.-Phys. Dr. Mayer, die Richterin Kopacek sowie die Richter Dipl.-Ing. Gottstein und Dipl.-Ing. Musiol


beschlossen:


                     Die Beschwerde wird zurückgewiesen.




BPatG 154
05.11

                                        -2-



                                     Gründe


                                         I.


Das Deutsche Patent- und Markenamt - Prüfungsstelle für Klasse H 04 J - hat die
am 1. Juli 1993 angemeldete Patentanmeldung mit der Bezeichnung "Verfahren
zum Empfangen eines in einem synchronen, digitalen Telekommunikationssystem
benutzten Signals" durch Beschluss vom 24. Mai 2006 zurückgewiesen.


Der Zurückweisung lagen die am 30. Dezember 1994 eingereichten Patentansprüche 1 und 2 und die am 26. Mai 2005 eingereichten Patentansprüche 3 und 4 zu
Grunde.


Die Prüfungsstelle hat ihren Beschluss damit begründet, dass sich der Gegenstand des geltenden Patentanspruchs 1 für den Durchschnittsfachmann in nahe
liegender Weise aus dem bekannten Stand der Technik


          (1)   Annex PI to ETS DE/TM 1015 (1992-01-03), Seiten 1 bis 3


ergebe.


Wegen weiterer Einzelheiten wird auf den Inhalt des Beschlusses verwiesen.

                                        -3-



Gegen diesen Beschluss richtet sich die am 8. August 2006 beim Deutschen Patent- und Markenamt eingegangene Beschwerde, mit der die Anmelderin sinngemäß beantragt,


       den Beschluss der Prüfungsstelle für Klasse H 04 J des Deutschen Patent- und Markenamts vom 24. Mai 2006 aufzuheben
       und das Patent auf der Grundlage folgender Unterlagen zu erteilen:


       Patentansprüche: Patentansprüche 1              und      2      vom
                              30. Dezember 1994, Patentansprüche 3 und
                              4 vom 26. Mai 2005


       Beschreibung:          Seiten 1 bis 24 vom 30. Dezember 1994


       Zeichnungen:           Figuren 1 bis 6, Figuren 7A und 7B vom
                              30. Dezember 1994.


Der geltende Patentanspruch 1 hat folgende Fassung:


       "1.    Verfahren zum Empfangen eines in einem synchronen, digitalen Telekommunikationssystem, wie in einem SDH- oder
              SONET-System, benutzten Signals, welches Signal eine
              Rahmenstruktur hat, die eine vorherbestimmte Anzahl von
              Bytes mit fester Länge und einen Pointer aufweist, der die
              Phase der Nutzlast innerhalb der Rahmenstruktur bezeichnet, welches Verfahren Pointerinterpretation aufweist, bei der
              der Empfänger drei eventuelle Hauptzustände hat, zwischen
              denen er unter Kontrolle von Ereigniszählern Übergänge
              durchmacht, wobei die Hauptzustände ein normaler Zustand (NORM), ein Pointerverlustzustand (LOP) und ein

                                        -4-



             Alarmzustand (AIS) sind, welche Zähler vorherbestimmte Ereignisse in jedem Hauptzustand zählt, welche Ereignisse
             Empfang negative Pointeranpassung anzeigender Dekrementdaten (dec_ind) und Empfang positive Pointeranpassung anzeigender Inkrementdaten (inc_ind) aufweisen, wobei im Pointer enthaltene I- und D-Bits zur Anzeige der Taktanpassungsfunktionen benutzt werden, und Empfang eines
             Neudatenflags (NDF_enable), das einen neuen Pointerwert
             anzeigt, dadurch gekennzeichnet, daß im Normalzustand
       - (i) alle Ereignisse, in denen der Wert "normal" (NDF_disabled)
             für das Neudatenflag empfangen worden ist und die Mehrzahl der I-Bits invertiert ist und die Mehrzahl der D-Bits nicht
             invertiert ist, als Inkrementdaten betrachtet werden, und
       - (ii) alle Ereignisse, in den der Wert "normal" (NDF_disabled) für
             das Neudatenflag empfangen worden ist und die Mehrzahl
             der D-Bits invertiert ist und die Mehrzahl der I-Bits nicht invertiert ist, als Dekrementdaten betrachtet werden,
             wobei "0110" und davon innerhalb bestimmter Grenzen abweichende Werte als Wert "normal" für das Neudatenflag betrachtet werden."


Der geltende nebengeordnete Patentanspruch 3 lautet:


       "3.   Empfänger zum Empfangen eines in einem synchronen, digitalen Telekommunikationssystem, wie in einem SDH- oder
             SONET-System, benutzten Signals, welches Signal eine
             Rahmenstruktur hat, die eine vorherbestimmte Anzahl von
             Bytes mit fester Länge und einen Pointer aufweist, der die
             Phase der Nutzlast innerhalb der Rahmenstruktur bezeichnet, der Empfänger hat drei eventuelle Hauptzustände in der
             Pointerinterpretation, zwischen denen es so eingerichtet ist,

                                        -5-



            unter Kontrolle von Ereigniszählern Übergänge durchzumachen,    wobei    die   Hauptzustände       ein    normaler       Zustand (NORM), ein Pointerverlustzustand (LOP) und ein
            Alarmzustand (AIS) sind, welche Zähler vorherbestimmte Ereignisse in jedem Hauptzustand zählt, welche Ereignisse
            Empfang negative Pointeranpassung anzeigender Dekrementdaten (dec_ind) und Empfang positive Pointeranpassung anzeigender Inkrementdaten (inc ind) aufweisen, wobei
            im Pointer enthaltene I- und D-Bits zur Anzeige der Taktanpassungsfunktionen benutzt werden, und Empfang eines
            Neudatenflags (NDF_enable), das einen neuen Pointerwert
            anzeigt, dadurch gekennzeichnet, daß im Normalzustand
            der Empfänger so eingerichtet ist, dass
       - (i) die für Inkrementdaten gehaltene alle die Ereignisse sind, in
            denen der Wert "normal" (NDF_disabled) für das Neudatenflag empfangen worden ist und die Mehrzahl der I-Bits invertiert ist und die Mehrzahl der D-Bits nicht invertiert ist, und
       - (ii) die für Dekrementdaten gehaltene die Ereignisse sind, in den
            der Wert "normal" (NDF_disabled) für das Neudatenflag
            empfangen worden ist und die Mehrzahl der D-Bits invertiert
            ist und die Mehrzahl der I-Blts nicht invertiert ist,
            wobei der Empfänger so eingerichtet ist, dass er berücksichtigt, dass der Wert "normal" für das Neudatenflag "0110" ist
            und Werte davon innerhalb bestimmter Grenzen abweichenden."


Die ordnungsgemäß geladene Anmelderin hat gemäß schriftlicher Ankündigung
vom 15. Mai 2012 an der mündlichen Verhandlung nicht teilgenommen.


Wegen weiterer Einzelheiten wird auf den Akteninhalt verwiesen.

                                       -6-



                                        II.


1. Die zulässige Beschwerde konnte keinen Erfolg haben, weil der Gegenstand
des Patentanspruchs 1 nicht auf einer erfinderischen Tätigkeit beruht, wie sich aus
der zutreffenden Begründung der Prüfungsstelle für Klasse H 04 J des Deutschen
Patent- und Markenamts in ihrem Zurückweisungsbeschluss vom 24. Mai 2006 im
Einzelnen nachvollziehbar ergibt. Der Senat macht sich diese Begründung zu eigen und verweist insoweit auf sie (vgl. BGH, Beschluss vom 22. Juni 1993
- X ZB 22/92, GRUR 1993, 896 - Leistungshalbleiter).


2. Mit dem Patentanspruch 1 fallen jeweils auch die weiteren Ansprüche, da das
Patent nur so erteilt werden kann, wie es beantragt ist und ein eigenständiger Erfindungsgehalt des Nebenanspruchs 3 sowie der Unteransprüche 2 und 4 von der
Beschwerdeführerin weder geltend gemacht wurde noch für den Senat erkennbar
ist (BGH, Beschluss vom 22. Juni 1993 - X ZB 22/92, GRUR 1993, 896 - Leistungshalbleiter; BGH, Beschluss vom 27. Februar 2008 - X ZB 10/07, GRUR-RR 2008, 456, Tz. 22 - Installiereinrichtung, mit weiteren Nachweisen).




Dr. Mayer                Kopacek                  Gottstein                Musiol




                                                                                Pü
