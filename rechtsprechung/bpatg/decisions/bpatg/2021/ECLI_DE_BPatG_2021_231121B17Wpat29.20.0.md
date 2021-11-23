---
ecli: "ECLI:DE:BPatG:2021:231121B17Wpat29.20.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 29/20"
decided: "2021-11-23"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=35&nr=42386&anz=599&pos=538&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2021-11-23_17_W-pat_29_20_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 29/20 vom 2021-11-23

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 29/20                                                   Verkündet am
_______________                                                  23. November 2021
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 10 2015 105 725.5


…
hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 23. November 2021 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Morawek, der Richterin Bayer, des Richters Dipl.-
Ing. Hoffmann und des Richters Dr.-Ing. Harth
beschlossen:


                     Die Beschwerde wird zurückgewiesen.




ECLI:DE:BPatG:2021:231121B17Wpat29.20.0

                                       -2-




                                    Gründe


                                         I.
Die vorliegende Patentanmeldung wurde am 15. April 2015 beim Deutschen Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung:


                    „Beförderungsverfahren und -vorrichtung“.

Die Anmeldung wurde von der Prüfungsstelle für Klasse G06Q des Deutschen
Patent- und Markenamtes mit Beschluss vom 29. Juni 2020 zurückgewiesen. Zur
Begründung führt die Prüfungsstelle aus, dass der geltende Anspruch 1 nicht gewährbar sei, da seine Lehre nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss ist die Beschwerde des Anmelders gerichtet.


Der Vertreter des Anmelders stellte sinngemäß den Antrag,


den angegriffenen Beschluss aufzuheben und das nachgesuchte Patent mit
folgenden Unterlagen zu erteilen:


gemäß Hauptantrag mit
      Patentansprüche 1-10 vom 22. Oktober 2018,
      Beschreibung Seiten 1-4 vom 22. Oktober 2018,
      Beschreibung Seiten 5-12 vom 15. April 2015 (=AT),
      3 Blatt Zeichnungen mit Figur 1-3 vom AT;


gemäß Hilfsantrag 1:
      Patentansprüche 1-8 vom 10. November 2021,
      Beschreibung Seiten 1-4 vom 10. November 2021,

                                        -3-



      Beschreibung Seiten 5-12 vom 15. April 2015 (=AT),
      3 Blatt Zeichnungen mit Figur 1-3 vom AT;


gemäß Hilfsantrag 2:
      Patentansprüche 1-2 vom 10. November 2021,
      Beschreibung Seiten 1-3 vom 10. November 2021,
      Beschreibung Seite 4 letzter Absatz und
      Seiten 5-12 vom 15. April 2015 (=AT),
      3 Blatt Zeichnungen mit Figur 1-3 vom AT.




Zur mündlichen Verhandlung ist der Vertreter des Anmelders, wie angekündigt,
nicht erschienen.




Der geltende Anspruch 1 nach Hauptantrag (mit einer denkbaren Gliederung
versehen) lautet:


1.
M1    Beförderungsverfahren für Nutzer, die mittels eines Fahrzeugs von einem
      Startort zu einem Zielort befördert werden,
M2    wobei das Fahrzeug von einem Anbieter betrieben wird und
M3    wobei ein Server bereitgestellt wird zur Kommunikation mit den Nutzern und
      den Anbietern über ein Kommunikationsnetz,
M4    der Server als ein Taxi-Verteilserver (1) Anfragen über Taxifahrten von Nutzern (M1, M2, ...Mn, S1, S2, ... Sn) mit Angeboten über Taxifahrten von Taxiunternehmen (T1, T2, ... Tn) vermittelt,
M5    wobei auf Anfrage (10) eines Master-Nutzers (M1) eine Taxifahrt (f1) mit einer Taxifahrtkennung (ID1) angelegt wird,

                                       -4-



     M5.1 für die angefragte Taxifahrt (f1) bei einem Taxiunternehmen (T1, T2,
            ... Tn) eine Anfrage (11) gesendet wird, ob die angefragte Taxifahrt
            durch das Taxiunternehmen (T1, T2, ... Tn) durchgeführt werden kann,
     M5.2 dass bei Buchungsbestätigung der angefragten Taxifahrt (f1) durch
            ein Taxiunternehmen (T1) taxifahrtbezogene Parameter (p1) für die
            angefragte Taxifahrt (f1) berechnet und
     M5.3 ein Bestätigungssignal (13) an den Master-Nutzer (M1) gesendet
            wird, so dass die angefragte Taxifahrt als gebuchte Taxifahrt (f1)
            stattfindet,
M6   dass bei Anfrage durch einen Slave-Nutzer (S1) nach einer weiteren Taxifahrt, in einer Zeit zwischen der Buchungsbestätigung (13) und einem
     Startzeitpunkt der gebuchten Taxifahrt (f1) die mit der gebuchten Taxifahrt
     des Master-Nutzers (M1) zumindest teilweise übereinstimmt,
     M6.1 bei dem Master-Nutzer (M1) nachgefragt wird, ob der Slave-Nutzer
            (S1) an der angefragten Taxifahrt teilnehmen darf oder nicht,
     M6.2 wobei dem Master-Nutzer (M1) geänderte taxifahrtbezogene Parameter (p2) mitgeteilt werden, und
     M6.3 dass dem Slave-Nutzer (S1) ein Bestätigungssignal übersandt wird,
            wenn der Master-Nutzer (M1) den geänderten taxifahrtbezogenen
            Parameter (p2) der geänderten Taxifahrt zustimmt, so dass die Taxifahrt (f2) mit den geänderten taxifahrtbezogenen Parametern (p2)
            durchgeführt wird,
M7   dass eine Bestätigung (19) die geänderte Taxifahrt (f2) an den Master-Nutzer (M1) und an den Slave-Nutzer (S1) erfolgt, wobei die geänderten
     Preise (P2, P3) für die geänderte Taxifahrt (f2) mitgeteilt werden.

                                            -5-



Der geltende Anspruch 1 nach Hilfsantrag 1 (mit einer denkbaren Gliederung
und gekennzeichneten Unterschieden zu Anspruch 1 nach Hauptantrag versehen)
lautet:


1.
M1        Beförderungsverfahren für Nutzer, die mittels eines Fahrzeugs von einem
          Startort zu einem Zielort befördert werden,
M2        wobei das Fahrzeug von einem Anbieter betrieben wird und
M3        wobei ein Server bereitgestellt wird zur Kommunikation mit den Nutzern und
          den Anbietern über ein Kommunikationsnetz,
M4        der Server als ein Taxi-Verteilserver (1) Anfragen über Taxifahrten von Nutzern (M1, M2, ...Mn, S1, S2, ... Sn) mit Angeboten über Taxifahrten von Taxiunternehmen (T1, T2, ... Tn) vermittelt,
M5        wobei auf Anfrage (10) eines Master-Nutzers (M1) eine Taxifahrt (f1) mit einer Taxifahrtkennung (ID1) angelegt wird,
          M5.1 für die angefragte Taxifahrt (f1) bei einem Taxiunternehmen (T1, T2,
                 ... Tn) eine Anfrage (11) gesendet wird, ob die angefragte Taxifahrt
                 durch das Taxiunternehmen (T1, T2, ... Tn) durchgeführt werden kann,
          M5.2 dass bei Buchungsbestätigung der angefragten Taxifahrt (f1) durch
                 ein Taxiunternehmen (T1) taxifahrtbezogene Parameter (p1) für die
                 angefragte Taxifahrt (f1) berechnet und
          M5.3 ein Bestätigungssignal (13) an den Master-Nutzer (M1) gesendet
                 wird, so dass die angefragte Taxifahrt als gebuchte Taxifahrt (f1)
                 stattfindet,
M6        dass bei Anfrage durch einen Slave-Nutzer (S1) nach einer weiteren Taxifahrt, in einer Zeit zwischen der Buchungsbestätigung (13) und einem
          Startzeitpunkt der gebuchten Taxifahrt (f1) die mit der gebuchten Taxifahrt
          des Master-Nutzers (M1) zumindest teilweise übereinstimmt,
          M6.1 bei dem Master-Nutzer (M1) nachgefragt wird, ob der Slave-Nutzer
                 (S1) an der angefragten Taxifahrt teilnehmen darf oder nicht,

                                        -6-



      M6.2 wobei dem Master-Nutzer (M1) geänderte taxifahrtbezogene Parameter (p2) mitgeteilt werden, und
      M6.3 dass dem Slave-Nutzer (S1) ein Bestätigungssignal übersandt wird,
             wenn der Master-Nutzer (M1) den geänderten taxifahrtbezogenen
             Parameter (p2) der geänderten Taxifahrt zustimmt, so dass die Taxifahrt (f2) mit den geänderten taxifahrtbezogenen Parametern (p2)
             durchgeführt wird,
M7    dass eine Bestätigung (19) die geänderte Taxifahrt (f2) an den Master-Nutzer (M1) und an den Slave-Nutzer (S1) erfolgt, wobei die geänderten
      Preise (P2, P3) für die geänderte Taxifahrt (f2) mitgeteilt werden,
M8    dass über ein Bestätigungssignal oder ein Nichtbestätigungssignal das
      Master-Nutzers (M1) entschieden wird, ob die Taxifahrt nach Anfrage durch
      den Slave-Nutzer (S1) mit den ursprünglichen tarifbezogenen Parametern
      (p1) oder mit den geänderten taxifahrtbezogenen Parametern (p2) stattfindet.




Der geltende Anspruch 1 nach Hilfsantrag 2 ist identisch mit Anspruch 1 nach
Hilfsantrag 1.


Zu den weiteren Ansprüchen des Hauptantrags sowie der Hilfsanträge 1 und 2
wird auf die Akte verwiesen.


Im Verfahren wurde folgender Stand der Technik genannt:
D1:   US 2008/0114629 A1
D2:   US 2011/0999040 A1
D3:   DE 103 43 486 A1
D4:   US 2014/0082069 A1



Zu den Einzelheiten wird auf die Akte verwiesen.

                                         -7-




                                          II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie hat jedoch keinen Erfolg, da der Gegenstand des Patentanspruchs 1 nach
Hauptantrag sowie des jeweiligen Patentanspruchs 1 nach den Hilfsanträgen 1
und 2 nicht auf einer erfinderischen Tätigkeit beruht, wobei bei der Prüfung auf
erfinderische Tätigkeit diejenigen Anweisungen, die die Lösung eines technischen
Problems mit technischen Mitteln nicht bestimmen oder zumindest beeinflussen,
nicht zu berücksichtigen sind (vgl. BGH GRUR 2011, 125 Wiedergabe topografischer Informationen; BGH GRUR 2011, 610 – Webseitenanzeige; BGH GRUR
2013, 275 – Routenplanung).




1.      Die Erfindung betrifft ein Beförderungsverfahren für Nutzer, die mittels eines
Fahrzeugs von einem Startort zu einem Zielort befördert werden, wobei das Fahrzeug von einem Anbieter betrieben wird und wobei ein Server bereitgestellt wird
zur Kommunikation mit den Nutzern und den Anbietern über ein Kommunikationsnetz.
Ferner betrifft die Erfindung ein Beförderungssystem für Nutzer, die mittels eines
Fahrzeugs von einem Startort zu einem Zielort befördert werden, wobei das Fahrzeug von einem Anbieter betrieben wird, mit einem Server zur Kommunikation mit
den Nutzern und den Anbietern über ein Kommunikationsnetz (vgl. Offenlegungsschrift, Absätze [0001], [0002]).


Gemäß der Anmeldung sei ein Beförderungsverfahren für Nutzer bekannt, bei
dem ein Server die Koordinierung von Anbietern von Mitfahrgelegenheiten einerseits und Nutzern von Mitfahrgelegenheiten andererseits übernimmt. Weiter sei
ein Beförderungsverfahren bekannt, bei dem Nutzer auf Fahrzeuge von Taxiunternehmen zurückgreifen können (vgl. Offenlegungsschrift, Absatz [0003]).

                                       -8-




Die der Anmeldung zugrundeliegende Aufgabe ist es, ein Beförderungsverfahren
bzw. ein Beförderungssystem für Nutzer anzugeben, dass bei hoher Beförderungssicherheit den Komfort für die Nutzer erhöht und insbesondere die Beförderungskosten niedrig gehalten werden können (vgl. Offenlegungsschrift, Absatz
[0004]).


Zur Lösung dieser Aufgabe schlägt der Patentanspruch 1 nach Hauptantrag ein
Verfahren für die Vermittlung einer Fahrt von Benutzern von A nach B mit einem
Fahrzeug eines Anbieters wie bspw. eines Taxiunternehmens vor (Merkmale M1
und M2).


Für die Vermittlung von Anfragen der Benutzer mit Angeboten der Taxiunternehmen wird ein sogenannter Taxi-Verteilserver verwendet, der mit den Benutzern
und dem Anbieter über ein Netz (z.B. Internet) verbunden ist (Merkmale M3 und
M4).


Zur Durchführung des Verfahrens stellt ein Master-Nutzer (Mx / erster Benutzer)
eine Anfrage für eine Taxifahrt (fx). Für diese Taxifahrt wird eine Taxifahrtkennung
(IDx) angelegt. Dem Taxiunternehmen wird eine Anfrage gesendet, ob diese Fahrt
durchgeführt werden kann. Bei einer Bestätigung durch das Taxiunternehmen
werden fahrtbezogene Parameter (px) berechnet. Dem Master-Nutzer wird mittels
einer Bestätigung mitgeteilt, dass die gebuchte Fahrt stattfindet (Merkmale M5,
M5.1 und M5.2).


Wenn innerhalb der Zeit zwischen der Buchungsbestätigung für den Master-Nutzer und dem Startzeitpunkt der Fahrt des Master-Nutzers eine Anfrage eines
Slave Nutzers (Sx / weiterer Benutzer) für eine Fahrt eingeht, welche mit der gebuchten Fahrt des Master-Nutzers zumindest teilweise übereinstimmt, wird bei
dem Master-Nutzer nachgefragt, ob der Slave-Nutzer an der Fahrt teilnehmen darf

                                        -9-



und dem Master-Nutzer werden die geänderten fahrtbezogenen Parameter mitgeteilt (Merkmale M6, M6.1 und M6.2).


Stimmt der Master-Nutzer der Mitnahme des Slave-Nutzers und den geänderten
fahrtbezogenen Parametern zu, wird dem Slave-Nutzer eine Bestätigung gesendet, dass die Fahrt stattfindet (Merkmal 6.3).


Schließlich erhalten beide Nutzer eine Bestätigung mit den geänderten Preisen für
die gemeinsame Fahrt (Merkmal M7).




In Anspruch 1 nach Hilfsantrag 1 ist zusätzlich angegeben, dass über ein Bestätigungssignal oder ein Nichtbestätigungssignal des Master-Nutzers (M1) entschieden wird, ob die Taxifahrt nach Anfrage durch den Slave-Nutzer (S1) mit den ursprünglichen tarifbezogenen Parametern (p1) oder mit den geänderten taxifahrtbezogenen Parametern (p2) stattfindet (Merkmal M8).




Anspruch 1 nach Hilfsantrag 2 ist identisch mit Anspruch 1 nach Hilfsantrag 1.




Als Fachmann ist im vorliegenden Fall ein Diplom-Ingenieur oder Informatiker mit
mehrjähriger Berufserfahrung in der Entwicklung von Client-Server-Applikationen
– insbesondere auf dem Gebiet der Organisation von Dienstleistungen – anzusehen.




2.     Der jeweilige Gegenstand des Patentanspruchs 1 nach Hauptantrag und
nach den Hilfsanträgen 1 und 2 beruht nicht auf einer erfinderischen Tätigkeit, da
deren zu berücksichtigende Merkmale aus der Druckschrift D1 bekannt sind, bzw.

                                       - 10 -



für den Fachmann naheliegen und somit ohne erfinderisches Zutun erreicht werden.


2.1    Der Gegenstand des Patentanspruchs 1 nach Hauptantrag beruht gegenüber dem aus der D1 Vorbekannten nicht auf einer erfinderischen Tätigkeit.


Aus der D1 ist ein Verfahren bzw. ein System für die Vermittlung zwischen mehreren Nutzern, die eine Fahrt von einem Startort zu einem Zielort bei einem von
mehreren Anbietern, wie bspw. bei einem Taxiunternehmen, buchen, zu entnehmen (Absätze [0014], [0018]). Damit sind die Merkmale M1 und M2 gezeigt.


Die Kommunikation zwischen den Nutzern und dem Anbieter erfolgt über einen
Server, welcher über Schnittstellen und Netzwerke entsprechende Verbindungen
bereitstellt, sowie den Nutzern und den Anbietern Daten sendet (Fig.2, Absatz
[0032]). Der Server vermittelt die Fahrten. D.h. auf die Anfragen der Nutzer über
Fahrten werden diese an die Anbieter weitergegeben und wenn ein Anbieter die
Fahrt durchführt, wird dies den Nutzern mitgeteilt (Absatz [0039]). Damit sind auch
die Merkmale M3 und M4 gezeigt.


Weiter ist in der D1 beschrieben, dass ein erster Fahrgast (Nutzer A) eine Anfrage
für eine Fahrt von x nach y zu einer Zeit z sendet. Diese Anfrage wird auf dem
Server in einer Datenbank gespeichert (Fig.3, Fig.4, Absätze [0039], [0050]). Somit ist auch das Anlegen eines Datensatzes mit den Parametern der Fahrt, d.h.
einer Taxifahrt mit einer entsprechenden Kennung beschrieben – Merkmal M5.


Für die Reihenfolge der Vermittlung der Fahrgäste (Nutzer) mit den Transportanbietern sowie für die Vermittlung zwischen den Fahrgästen (Nutzern) untereinander zeigt die D1 mehrere Alternativen (Absätze [0018], [0081], [0122]).
So kann ein Nutzer A erst mit einem weiteren Nutzer B zusammengeführt werden
und für beide wird anschließend ein Transportanbieter gesucht.

                                       - 11 -



Alternativ kann ein Nutzer A auf seine Anfrage für eine Fahrt direkt zu dem Transportanbieter vermittelt werden und eine weiterer Nutzer B kann später der Fahrt
beitreten. D.h. die Fahrt kann nur für den Nutzer A durchgeführt werden oder es
kann sich nach der Vermittlung zwischen dem Nutzer A und dem Transportanbieter ein weiterer Nutzer B der Fahrt anschließen.
Hinsichtlich der Kommunikation zwischen dem Server bzw. den Nutzern und den
Transportanbietern ist angegeben, dass die Anbieter die Verfügbarkeit von Transportmöglichkeiten übermitteln, wobei die Anbieter dafür verantwortlich sein können, dass diese Verfügbarkeit aktualisiert wird (Absatz [0025]). Implizit ist damit
aber auch beschrieben, dass die auf dem Server hinterlegte Verfügbarkeit nicht
aktuell sein kann.
Da der Fachmann stets bestrebt ist bekannte Fehlerquellen zu umgehen, wird er
nach der Anfrage eines Nutzers und der folgenden direkten Vermittlung zu den
Transportanbietern (Absatz [0018]) eine Abfrage installieren, die den aktuellen
Status der Verfügbarkeit abbildet. Diese Abwandlung liegt für den Fachmann ohnehin auf der Hand, da die direkte Anfrage bei einem Taxiunternehmen für eine
Fahrt, bspw. per Telefon, schon lange bekannt war. Überdies wird eine derartige
direkte Kommunikation zwischen dem Nutzer A und/oder dem Nutzer B mit dem
Transportanbieter in der D1 beschrieben (Absatz [0071]).
Somit gelangt der Fachmann aufgrund der Lehre der D1 und seines Fachwissens
ohne erfinderisches Zutun zu Merkmal M5.1.


Die direkte Kommunikation zwischen dem Nutzer A und/oder dem Nutzer B mit
dem Transportanbieter umfasst dabei auch die Übertragung von Informationen,
wie bspw. einen Treffpunkt, ein Erkennungszeichen (Absatz [0071]). Damit ist die
Übertragung von Parametern der Fahrt sowie die indirekte Bestätigung der Durchführung der Fahrt an den Nutzer A, welcher die Fahrt auch alleine buchen kann
(Absatz [0018]), gezeigt – Merkmale M5.2 und M5.3.


Nach der Buchung einer Fahrt durch einen ersten Nutzer A kann später ein weiterer Nutzer B der Fahrt beitreten (Absatz [0018]). Dem Nutzer B wird eine Liste ge-

                                       - 12 -



buchter Fahrten aller anderen Nutzer gezeigt, wobei die Liste z.B. basierend auf
der Nähe der Start- und Zielorte der anderen Nutzer relativ zu dem Start- und Zielort des Nutzers B geordnet sein kann. Anschließend kann der Nutzer B aufgrund
dieser Daten die Fahrt mit einem der anderen Nutzer teilen. Ebenso ist die automatische Zusammenführung des Nutzers B mit einem der anderen Nutzer durch
das System möglich (Absatz [0054]). Dabei kann der erste Nutzer A bspw. bis zu
einer bestimmten Zeit vor der Fahrt auf einen zweiten Nutzer B warten (Absatz
[0077]). Damit ist auch Merkmal M6 aus der Druckschrift zu entnehmen.


Teilt ein weiterer Nutzer mit, dass er an der Fahrt teilnehmen möchte, bzw. wählt
das System einen weiteren Nutzer aus, erhält der erste Nutzer A die Information,
dass ein weiterer Nutzer an der Fahrt teilnehmen möchte. Der Nutzer A kann angeben, ob er die Fahrt mit diesem Nutzer teilen möchte (Absätze [0040], [0061]).
Dabei kann der Nutzer A seine Entscheidung auf weitere Informationen, z.B. wie
weit sich das Ziel von dem weiteren Nutzer von seinem eigenen Ziel unterscheidet, stützen (Absatz [0042]). Wenn der Nutzer A entschieden hat die Fahrt zu teilen und dies dem System mitteilt, wird der weitere Nutzer vom System benachrichtigt, dass die geteilte Fahrt mit Nutzer A stattfindet. Die Benachrichtigung enthält
dabei auch Angaben zur Fahrt, wie bspw. den Zeitpunkt sowie Start und Zielort
(Absatz [0049]). Somit sind die Merkmale M6.1, M6.2 und M6.3 aus der Druckschrift zu entnehmen.


Ebenso erhält der erste Nutzer A die Benachrichtigung, dass die geteilte Fahrt
stattfindet (Absatz [0049]). Beide Nutzer erhalten zusätzliche Informationen wie
bspw. einen Treffpunkt, ein Erkennungszeichen (Absatz [0071]). Ebenso ist angegeben, dass der Nutzer A und/oder der Nutzer B den Transportanbieter direkt bezahlen können (Absatz [0071]), wobei hierfür der zu bezahlende Preis für die Fahrt
dem Nutzer bzw. den Nutzern mitgeteilt werden muss. Damit ist auch Merkmal M7
aus der Druckschrift zu entnehmen.

                                      - 13 -



2.2   Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 und Hilfsantrag 2 beruht gegenüber dem aus der D1 Vorbekannten nicht auf einer erfinderischen Tätigkeit, wobei die Merkmale, welche nicht zu einer technischen Problemlösung beitragen, nicht zu berücksichtigen sind.


Für die Beurteilung der Patentfähigkeit wird im Folgenden nur das geänderte
Merkmal M8 betrachtet. Zu den übrigen Merkmalen wird auf die Ausführungen
zum Hauptantrag verwiesen.


Gemäß diesem Merkmal wird aufgrund eines Bestätigungssignals oder eines
Nichtbestätigungssignals des Master-Nutzers entschieden, ob die Taxifahrt nach
Anfrage   durch   den Slave-Nutzer mit         den   ursprünglichen   tarifbezogenen
Parametern oder mit den geänderten taxifahrtbezogenen Parametern stattfindet.


Aus der D1 ist zu entnehmen, dass die Anfrage über das Teilen der Fahrt eines
weiteren Nutzers an den Nutzer A übermittelt wird. Der Nutzer A kann diese Anfrage annehmen oder ablehnen (Absätze [0019], [0084]). Dabei kann der Nutzer A
seine Entscheidung von weiteren Werten, wie bspw. der Entfernung des Startpunktes und des Zielpunktes beider Nutzer, abhängig machen (Absatz [0084]).
D.h. der Nutzer A entscheidet aufgrund von fahrtbezogenen Parametern, ob er die
Fahrt mit dem weiteren Nutzer teilen möchte oder nicht – teilweise Merkmal M8.


Die Angabe, wonach der Nutzer A auch die ursprünglichen tarifbezogenen Parameter in seine Entscheidung einbezieht (restlicher Teil des Merkmals M8), diese
also dem Nutzer A übermittelt werden, geht aus der D1 nicht hervor.


Dies kann jedoch das Vorliegen einer erfinderischen Tätigkeit nicht begründen.


Die Übermittlung von Daten an den Nutzer A, z.B. einer Anfrage oder weiterer
Werte, ist aus der D1 zu entnehmen (Absätze [0083], [0084]). Damit ist der technische Weg der Datenübertragung an den Nutzer A vorbeschrieben. Ob es sich bei

                                         - 14 -



den Daten um fahrtbezogene Parameter oder um tarifbezogene Parameter handelt, ist ohne Belang und bei der Prüfung auf erfinderische Tätigkeit nicht zu berücksichtigen. Denn der Bedeutungsinhalt der Daten kann die Zugänglichkeit zum
Patentschutz nicht begründen, da die Art der Daten für die Beurteilung der Zugänglichkeit der beanspruchten Lehre zum Patentschutz keine Relevanz hat (vgl.
BGH GRUR 2005, 143 – Rentabilitätsermittlung)




2.3   Die Ausführungen des Vertreters des Anmelders führen zu keinem anderen
Ergebnis.


So offenbare die D1 ein Beförderungsverfahren, bei dem alle Nutzer des Taxiunternehmens die Taxifahrt akzeptieren müssten. Zwar könne der Fachmann aus
der D1 einen Master-Nutzer A herauslesen, jedoch sei die Vorzugsstellung des
Master-Nutzers darauf beschränkt, die Route der Taxifahrt vorzugeben. Eine endgültige Buchung der Taxifahrt erfolge erst, wenn ein weiterer Nutzer gefunden
worden ist.
Demgegenüber zeichne sich der Master-Nutzer gemäß der Anmeldung dadurch
aus, dass er nicht nur die Taxifahrt bezogenen Parameter vorgebe, sondern auch
die Buchung der Taxifahrt selbst. Denn gemäß Anspruch 1 würde der Master-Nutzer ein Bestätigungssignal über die gebuchte Taxifahrt erhalten. Eine Änderung der Taxifahrt ergäbe sich erst, wenn ein weiterer Slave-Nutzer gefunden
werde, der eine Änderung der Taxifahrt erforderlich mache. Falls dieser Slave-Nutzer nicht gefunden werde, würde die bereits gebuchte Taxifahrt für den Master-Nutzer stattfinden.
Der Vorteil der Lehre der Anmeldung bestehe darin, dass durch die anfängliche
Buchung der Einzelfahrt durch den Master-Nutzer derselbe sich der Durchführung
der Taxifahrt sicher sein könne. Diese werde in jedem Fall durchgeführt, egal ob
sich weitere Nutzer finden oder nicht.


Diese Ausführungen greifen letztendlich zu kurz.

                                       - 15 -



Zwar ist den Ausführungen insoweit zuzustimmen, als in der D1 eine Ausführungsform gezeigt ist, bei der ein erster Nutzer eine Fahrt anmeldet, anschließend ein
weiterer Nutzer gesucht wird, der die Fahrt des ersten Nutzers teilt, und erst nach
dem Zusammenführen beider Nutzer für die gemeinsame Fahrt ein Transportanbieter gesucht wird (vgl. Fig.5).
Darüber hinaus beschreibt die D1 jedoch auch, dass ein erster Nutzer A auf seine
Anfrage für eine Fahrt direkt zu dem Transportanbieter vermittelt wird, d.h. der erste Nutzer führt die Fahrt alleine durch. Ein weiterer Nutzer B kann später der Fahrt
beitreten (Absatz [0018]). Ebenso ist angegeben, dass das System für die Fahrt
des ersten Nutzers A versucht einen weiteren Nutzer zu finden, bis der Nutzer A
beschließt einen nicht geteilten Transport zu nehmen (Absatz [0081]). Schließlich
zeigt die D1 auch, dass der erste Nutzer A bspw. bis zu einer bestimmten Zeit vor
der Fahrt auf einen zweiten Nutzer B wartet (Absatz [0077]) und somit die bereits
gebuchte Fahrt alleine durchführt, falls kein weiterer Nutzer gefunden wird.




3.     Ebenso wie der jeweilige Anspruch 1 nach Hauptantrag und nach den
Hilfsanträgen 1 und 2 sind auch die weiteren Ansprüche der einzelnen Anträge
nicht gewährbar, da über einen Antrag nur einheitlich entschieden werden kann
(BGH GRUR 1997, 120 - Elektrisches Speicherheizgerät).

                                            - 16 -




                                Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
       Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
       Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                  Bayer                   Hoffmann                   Dr. Harth
