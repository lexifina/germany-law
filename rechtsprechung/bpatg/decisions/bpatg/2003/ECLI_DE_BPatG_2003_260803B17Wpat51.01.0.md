---
ecli: "ECLI:DE:BPatG:2003:260803B17Wpat51.01.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 51/01"
decided: "2003-08-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2003&Sort=1&Seite=88&nr=20016&anz=2047&pos=1323&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2003-08-26_17_W-pat_51_01_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 51/01 vom 2003-08-26

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 51/01                                                    Verkündet am
 _______________                                                    26. August 2003
    (Aktenzeichen)                                                        …




                               BESCHLUSS

                              In der Beschwerdesache




                   betreffend die Patentanmeldung 199 44 991.0-53




…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. August 2003 unter Mitwirkung des Richters
Dipl.-Ing. Bertl     als   Vorsitzenden    sowie   der    Richter    Dr. Schmitt,
Dipl.-Phys. Dr. Kraus und Dipl.-Ing. Prasch




BPatG 154
6.70

                                          -2-



beschlossen:


      Auf die Beschwerde der Anmelderin wird der Beschluß der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamts vom 13. Februar 2001 aufgehoben und das Patent erteilt.


      Der Erteilung liegen folgende Unterlagen zugrunde:
      Patentansprüche 1 – 4 und Beschreibung Seiten 1 – 7 mit Seite 2a,
      beides   überreicht      in   der   mündlichen   Verhandlung   vom
      26. August 2003,
      sowie 2 Blatt Zeichnungen mit Figuren 1 – 3, eingegangen am Anmeldetag (20. September 1999).




                                      Gründe


                                           I.


Die vorliegende Patentanmeldung wurde von der Prüfungsstelle für Klasse G 06 F
des Deutschen Patent- und Markenamts zurückgewiesen. In den Gründen ist ausgeführt, daß die Gegenstände der Patentansprüche 1 und 2 nicht auf einer erfinderischen Tätigkeit beruhen.


Gegen diesen Beschluß richtet sich die Beschwerde der Anmelderin.


Der geltende Patentanspruch 1 lautet:


      „Verfahren zur Sicherung des Programmablaufs beim Aufruf von
      Unterprogrammen, wobei das aufgerufene Programm eine Überprüfung der vom aufrufenden Programm direkt oder indirekt übermittelten Parameter ausführt

                                          -3-



       dadurch gekennzeichnet, dass
       -     das aufrufende Programm über die zu übergebenden Parameter eine erste Checksumme bildet,
       -     - diese erste Checksumme in einem dafür vorgesehenen Speicherbereich abgelegt wird,
       -     - das aufgerufene Programm zu Beginn seiner Ausführung
             über die erhaltenen Parameter eine zweite Checksumme bildet
             und auf Gleichheit mit der ersten Checksumme überprüft und
       -     bei Ungleichheit der ersten und der zweiten Checksumme das
             Programm abgebrochen oder eine Fehlermeldung ausgegeben
             wird.“


Der Anmeldung liegt die Aufgabe zugrunde, ein Verfahren anzugeben, das die sichere Überprüfung von modular aufgebauten Programmen, insbesondere bei Unterprogrammaufrufen, zuläßt (Beschreibung Seite 2, Zeilen 4 bis 6).


Die Anmelderin führt aus, daß es beim vorliegenden Verfahren darum gehe, den
Schutz von Programmen, die auf einer Chipkarte ablaufen, vor Manipulationen zu
verbessern. Im Unterschied zum Stand der Technik erfolge die Überprüfung zu
Beginn der Ausführung des Unterprogramms und nicht erst beim Rücksprung. Sie
ist der Ansicht, daß der Gegenstand des nunmehrigen Patentanspruchs 1 patentfähig sei.


Sie stellt den Antrag,


       den angefochtenen Beschluß aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 – 4 und Beschreibung, beides überreicht in der
       mündlichen Verhandlung vom 26. August 2003,

                                         -4-



      sowie 2 Blatt Zeichnungen mit Figuren 1 – 3 vom Anmeldetag
      (20. September 1999).


                                         II.


Die Beschwerde ist frist- und formgerecht eingereicht. Sie hat auch Erfolg, da der
Gegenstand des Patentanspruchs 1 patentfähig ist, insbesondere auf einer erfinderischen Tätigkeit beruht (§ 4 PatG).


Mit dem Verfahren nach dem Patentanspruch 1 sollen die Übergänge zu Unterprogrammen sicherer gemacht werden, um Manipulationen bei Chipkarten zu verhindern. Dazu bildet das aufrufende Programm über die zu übergebenden Parameter eine Prüfsumme (Checksumme). Das aufgerufene Unterprogramm bildet
über die empfangenen Parameter zu Beginn der Ausführung ebenfalls eine Prüfsumme. Die beiden Prüfsummen werden verglichen. So wird sichergestellt, daß
die übergebenen Parameter bei der Übergabe nicht verändert worden sind.


Im Prüfungsverfahren wurden folgende Druckschriften genannt:


   1. DE 197 01 166 A1
   2. US-Z: IEEE Transactions on Computer-Aided Design, Vol. 9, No. 6, June
      1990, Seiten 665 – 669
   3. DE 35 02 387 C2
   4. DE 37 09 524 C2.


Das Verfahren nach dem Patentanspruch 1 ist neu gegenüber dem aus diesen
Druckschriften jeweils bekannten Stand der Technik.


Die DE 197 01 166 A1 betrifft ein Verfahren zur Überwachung der bestimmungsgemäßen Ausführung von Softwareprogrammen. Es wird, wie üblich, die Rücksprungadresse über den Stack an das Unterprogramm übergeben. Gleichzeitig

                                      -5-



wird die Rücksprungadresse auch in einem Speicher 3 hinterlegt. Bei Beendigung
des Unterprogramms wird die Rücksprungadresse aus dem Unterprogramm mit
der hinterlegten Adresse im Speicher 3 verglichen, um Manipulationen erkennen
zu können. Im Patentanspruch 5 heißt es, daß als Sicherungsinformationen die
Rücksprungadresse oder charakteristische Daten verwendet werden. Nähere Angaben hierzu enthält die Beschreibung nicht.


Unterschiedlich ist schon der Zeitpunkt der Überprüfung, beim Anmeldungsgegenstand zu Beginn des Unterprogramms und am Ende des Unterprogramms
nach dieser Druckschrift.


Die Druckschrift 2 beschreibt eine Möglichkeit, Programme schneller zu testen.
Dazu werden über Datenfelder Checksummen gebildet und mit Checksummen
von einem Referenzprogramm verglichen, um so Fehler im Programmablauf zu
entdecken.


Bei der DE 35 02 387 C2 geht es um die Überwachung von Mikroprozessorsystemen. Im Programmablauf sind eine Vielzahl von Kontrollpunkten vorgesehen, die
zu vorgegeben Zeitabläufen im Programmablauf erreicht werden müssen. Dazu ist
eine Uhr vorgesehen, die immer wieder nach Erreichen eines Kontrollpunktes neu
"aufgezogen" wird.


Nach der DE 37 09 524 C2 werden zur Sicherung von Speicherinhalten Prüfsummen über vorgegebene Speicherbereiche gebildet und in einem Speicher abgelegt. Diese Prüfsummen können dann zu gewünschten Zeitpunkten überprüft werden.


Die Druckschriften 2 bis 4 betreffen nicht die Ausführung von Unterprogrammen;
sie können schon deshalb die Neuheit des Verfahrens nach dem Anspruch 1 nicht
in Frage stellen.

                                      -6-



Das Verfahren nach dem Patentanspruch 1 beruht auch auf einer erfinderischen
Tätigkeit.


Aus der DE 197 01 166 A1 ist ein Verfahren nach dem Oberbegriff des Patentanspruchs 1 bekannt, nämlich zur Sicherung des Pragrammablaufs beim Aufruf von
Unterprogrammen, wobei das aufgerufene Programm eine Überprüfung der vom
aufrufenden Programm direkt oder indirekt übermittelten Daten ausführt (vgl. insb.
Figur 1 und zugehörige Beschreibung). Zwar ist die Verwendung beim Aufruf von
Unterprogrammen nicht ausdrücklich erwähnt, doch der Fachmann erkennt, daß
dieses Verfahren bei Verwendung von Unterprogrammen angewendet wird (vgl.
insb. Spalte 2, Zeilen 51 bis 63).


Dazu legt das aufrufende Programm Parameter in einem dafür vorgesehenen
Speicherbereich (3) ab, das aufgerufene Programm überprüft die vom aufrufenden
Programm erhaltenen Parameter (in 1) auf Gleichheit (in 5) mit den abgelegten
Parametern. Bei Ungleichheit wird das Programm abgebrochen oder eine Fehlermeldung ausgegeben.


Nach dem Ausführungsbeispiel der Figur 2 dieser Druckschrift ist noch ein
Schreibschutzbit für die Rücksprungadressen im Stack vorgesehen.


Im Patentanspruch 5 ist aufgeführt, daß als Sicherungsinformation die Rücksprungadresse selbst oder diese repräsentierende oder charakterisierende Daten
verwendet werden können. Zusätzliche Hinweise hierzu gibt es in den übrigen
Unterlagen nicht. Der Fachmann weiß zwar, daß hierunter eine Quer- oder
Checksumme fallen kann, doch führt die Beschreibung, insb der Figur 2 mit dem
Schreibschutz, vor allem Spalte 6, Zeilen 50 bis 58, ihn in eine andere Richtung.
Dies hängt vor allem mit der unterschiedlichen Überprüfung zusammen. Der
Schreibschutz ist vorgesehen, weil der Vergleich erst nach Beendigung des Unterprogramms erfolgt und die Daten deshalb geschützt werden müssen. Im Ge-

                                       -7-



gensatz hierzu erfolgt beim Anmeldungsgegenstand der Vergleich zu Beginn des
Unterprogramms, wo ein Überschreiben noch nicht zu befürchten ist.
Dadurch werden nach dem beanspruchten Verfahren Auswirkungen von Fehlern
von vornherein verhindert.


Die Druckschriften 2 (US-Z: IEEE Transactions on Computer-Aided Design, Vol. 9,
No. 6, June 1990, Seiten 665 – 669) und 3 (DE 35 02 387 C2) befassen sich nicht
mit Unterprogrammen. Bei der Druckschrift 4 (DE 37 09 524 C2) werden feste Parameter (Speicherplätze) überprüft und keine sich während des Programmablaufs
ergebenden Parameter.


Auch bei Kenntnis der DE 197 01 166 A1 ergibt eine Zusammenschau mit diesen
Druckschriften nicht das Verfahren nach dem Patentanspruch 1.


Die Patentansprüche 2 bis 4 enthalten nicht selbstverständliche Ausgestaltungen
des Verfahrens nach dem Patentanspruch 1.


Der Beschwerde ist somit stattzugeben und das nachgesuchte Patent zu erteilen.




Bertl                    Dr. Schmitt         Dr. Kraus                  Prasch


                                                                            Bb
