---
ecli: "ECLI:DE:BPatG:2006:020306B17Wpat8.04.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 8/04"
decided: "2006-03-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2006&Sort=1&Seite=17&nr=278&anz=1665&pos=264&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2006-03-02_17_W-pat_8_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0079.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 8/04 vom 2006-03-02

## Entscheidung

BUNDESPATENTGERICHT



    17 W (pat) 8/04
_______________________

    (Aktenzeichen)




                              BESCHLUSS

                            In der Beschwerdesache


                 betreffend die Patentanmeldung P 40 39 891.9-53


…




hat der 17. Senat des Bundespatentgericht am 2. März 2006 unter Mitwirkung …




BPatG 152
08.05

                                        -2-



beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 6. Oktober 2003 aufgehoben. Die Sache wird unter
        Zugrundelegung der folgenden Unterlagen zur weiteren Prüfung
        an das Deutsche Patent- und Markenamt zurückverwiesen:


        -      Patentansprüche 1 und 11 eingeg. 29. Juli 2004,
        -      Patentansprüche 2–10 und 12 eingeg. 15. Mai 2002,
        -      Beschreibung Seiten 2, 4–8, 10–17, 23, 25, 39, 40, 42–45,
               47–50, 53, 57–62, 65 eingeg. am 29. Juli 2004,
        -      übrige Beschreibungsseiten vom Anmeldetag
        -      34 Seiten Zeichnungen Figuren 1–45 vom 13. März 1991.


        Die Rückzahlung der Beschwerdegebühr wird angeordnet.


                                     Gründe


                                         I.


Die   vorliegende    Patentanmeldung,    für   die   die   Priorität   der   Anmeldung
JP 1-323396 in Japan vom 13. Dezember 1989 in Anspruch genommen wird, ist
am 13. Dezember 1990 beim Deutschen Patent- und Markenamt unter der Bezeichnung


        „Verfahren und Vorrichtung zur Cachespeichersteuerung"


angemeldet worden.

                                        -3-



Sie wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
Markenamts durch Beschluss vom 6. Oktober 2003 mit der Begründung zurückgewiesen, dass der Patentanspruch 1 einen Widerspruch aufweise und dem Fachmann daher keine klare Lehre zum technischen Handeln gebe.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin. Sie beantragt:


         •    die Anmeldung an die Prüfungsstelle zurückzuverweisen,
         •    hilfsweise, eine Erteilung des Patents mit den geltenden
              Unterlagen zu beschließen,
         •    weiter hilfsweise, eine mündliche Verhandlung anzusetzen.


Sie macht geltend, dass im Patentanspruch 1 kein Widerspruch vorliege. Auch sei
der Zurückweisungsbeschluss unnötig gewesen und habe im Sinne einer effizienten Durchführung des Prüfungsverfahrens vermieden werden können; ferner setze
er sich in keinster Weise mit ihren in der Eingabe vom 15. Mai 2002 angeführten
Argumenten auseinander, insofern scheine ein Verstoß gegen den Grundsatz des
rechtlichen Gehörs vorzuliegen.


Der geltende Patentanspruch 1 lautet:


         Cachespeicher-Schreibverfahren für ein Informationsverarbeitungssystem mit einer Datenverarbeitungseinheit (200), einer
         Steuereinheit (23) mit einem Cachespeicher (26) und einer Speichereinheit (24), die eine Vielzahl von physikalischen Bereichen (300) zum Speichern von jeweils mehreren Datensätzen (301) mit variablen Längen aufweist, die jeweils zumindest ein
         eine Datensatznummer (602) enthaltendes Steuerfeld (600) besitzen, wobei die Datenverarbeitungseinheit (200), die Steuerein-

                               -4-



heit (23) und die Speichereinheit (24) miteinander verbunden sind,
und


wobei die Steuereinheit (23) folgende Schritte ausführt:


(a)   Empfangen einer Schreibanforderung von der Datenverarbeitungseinheit (200), wobei die Schreibanforderung eine Datensatzinformation (3400: 1-3) zum Bestimmen eines Datensatzes (301) und eine Feldinformation (3400: 4) zum Bestimmen eines Feldes (606) in dem Datensatz (301) enthält,


(b)   Prüfen von Strukturbedingungen (A–C) für einen physikalischen Bereich (300) zum Speichern des bestimmten Datensatzes (301), um festzustellen, ob für den bestimmten Datensatz (301) eine Ermittlung der physikalischen Position in der Speichereinheit (24) möglich ist, wobei folgende Strukturbedingungen (A–C) geprüft werden: die Datensatznummer (602) des Datensatzes (310) am Anfang des physikalischen Bereichs (300) ist
„Null" und die Datensatznummern (602) der folgenden Datensätze (301) liegen in fortlaufender, aufsteigender Reihenfolge
vor (A); jeder Datensatz (301) des physikalischen Bereichs (300)
hat ein vom Steuerfeld (600) verschiedenes Feld (601) und die
Längen der vom Steuerfeld (600) verschiedenen Felder (601) der
Datensätze (301) mit Datensatznummern (602) größer oder gleich
„Eins" sind gleich (B); und das vom Steuerfeld (600) verschiedene
Feld (606) des Datensatzes (310) mit der Datensatznummer „Null"
besitzt eine vorgegebene Länge (C);


(c)   Empfangen von Daten von der Datenverarbeitungseinheit (200), die in das bestimmte Feld (601) des bestimmten Datensatzes (301) zu schreiben sind, falls die Strukturbedingun-

                                        -5-



       gen (A–C) erfüllt sind und das durch die Feldinformation (3400: 4)
       bestimmte Feld (606) das Steuerfeld (600) des Datensatzes (301)
       nicht umfasst;


       (d)   Prüfen, ob der Datensatz (301), für den Daten zu schreiben
       sind, im Cachespeicher (26) vorhanden ist;


       (e)   Speichern der empfangenen Daten in den vorhandenen
       Datensatz (301) im Cachespeicher (26), falls der Datensatz (301)
       im Cachespeicher (26) vorhanden ist, oder Anlegen eines später
       zu schreibenden Datensatzes (160) im Cachespeicher (26) und
       Speichern der empfangenen Daten in dem angelegten, später zu
       schreibenden Datensatz (160), falls der Datensatz (301) nicht vorhanden ist; und


       (f)   Melden des Abschlusses der Schreibanforderung an die Datenverarbeitungseinheit (200).


Der nebengeordnete Patentanspruch 11 ist auf eine entsprechende „Cachespeicher-Steuervorrichtung“ gerichtet, wobei die Verfahrensschritte des Patentanspruchs 1 gegen „Mittel zum …“ ausgetauscht wurden, stimmt aber hinsichtlich
der wesentlichen technischen Lehre mit dem Patentanspruch 1 überein.


Beide Ansprüche unterscheiden sich von den dem Zurückweisungsbeschluss zugrunde liegenden Ansprüchen 1 und 11 nur durch kleinere sprachliche Änderungen und Klarstellungen (vgl. Eingabe vom 28. Juli 2004, Kapitel II.), ohne dass
sich die technische Lehre geändert hätte.


Wegen des genauen Wortlauts des Nebenanspruchs und der Unteransprüche 2 - 10 und 12 wird auf die Akten verwiesen.

                                       -6-



                                        II.


Die Beschwerde führt zur Aufhebung des angefochtenen Beschlusses und zur Zurückverweisung der Sache an das Deutsche Patent- und Markenamt gemäß § 79
Abs. 3 Satz 1 Nr. 1 PatG.


1.    Die Anmeldung betrifft eine Cache-Speicher-Steuerung für ein Informationsverarbeitungssystem mit einer physikalischen Speichereinheit, wie z. B. einem
Plattenspeicher, die das Schreiben von Datensätzen steuert, wobei verschiedene
Fälle unterschieden werden (insbesondere ob der zu überschreibende Datensatz
im Cache-Speicher bereits vorliegt oder nicht).


2.    Der Zurückweisungsbeschluss der Prüfungsstelle wurde damit begründet,
dass beim Patentanspruch 1 ein Widerspruch bestehe zwischen der Voraussetzung einer Speichereinheit mit Bereichen zum Speichern von jeweils mehreren
Datensätzen mit variablen Längen einerseits und der Forderung in der Strukturbedingung (B) andererseits, dass die Längen der vom Steuerfeld verschiedenen Felder (der Datensätze mit Datensatznummern größer oder gleich „Eins“) gleich sein
sollen. Der Widerspruch liege darin, dass variable Felder voraussetzungsgemäß
nicht alle gleich lang sein könnten.


3.    Dieser Widerspruch besteht objektiv nicht. Nach der Formulierung des
Patentanspruchs 1 – ohne wesentlichen Unterschied in der zum Zeitpunkt des
Zurückweisungsbeschlusses wie in der jetzt geltenden Fassung – soll ein bestimmter Arbeitsschritt ausgeführt werden, wenn u. a. die Strukturbedingung (B)
erfüllt ist. Schon dies genügt, um den Widerspruch auszuräumen: es ist formallogisch einwandfrei, dass ein bestimmter Schritt nur dann erfolgen soll, wenn bei
Datensätzen variabler Länge die Längen bestimmter Felder der Datensätze gleich
sind; denn gerade weil die Längen auch ungleich sein können, ist die Prüfung der
Bedingung erforderlich.

                                       -7-



Darüber hinaus betrifft die Forderung nur die Datensätze mit Datensatznummern
größer oder gleich „Eins“; der Datensatz mit der Nummer „Null“ soll nach Strukturbedingung (C) ein vom Steuerfeld verschiedenes Feld vorgegebener Länge haben, damit wird sich im Normalfall für diesen Datensatz insgesamt eine andere
Länge ergeben. Schließlich zeigt ein Vergleich der Figuren 4 und 5 der Anmeldung, dass die Datensatzlänge außer vom „vom Steuerfeld verschiedenen Feld“
(601, 606) auch davon abhängt, ob ein Schlüsselfeld (607) vorgesehen ist oder
nicht. Auch so ergibt sich, dass Datensätze unterschiedlich lang sein und trotzdem
die Strukturbedingung (B) erfüllen können.


Somit kann die gegebene Begründung den Zurückweisungsbeschluss nicht tragen.


4.     Wenn auch die Anmeldung insgesamt, wie von der Prüfungsstelle mehrfach
zu Recht bemängelt, einige Unklarheiten aufweist, so gibt der Hauptanspruch in
der geltenden Fassung (die im Wesentlichen der dem Zurückweisungsbeschluss
zugrunde liegenden Fassung entspricht) dem Fachmann trotzdem eine klare,
nacharbeitbare Lehre. Die bisher im Prüfungsverfahren zitierten Druckschriften 1)
bis 3) stehen nicht entgegen, wie die Anmelderin zutreffend ausgeführt hat (siehe
Eingabe vom 28. Juli 2004, Kapitel IV.), zumindest weil keine von ihnen entsprechend Schritt b) des Hauptanspruchs eine Prüfung, ob für den bestimmten Datensatz eine Ermittlung der physikalischen Position in der Speichereinheit möglich ist,
anhand dreier konkreter Bedingungen beschreibt oder in dieser Richtung Anregungen gibt.


Insoweit könnte der Hauptanspruch daher patentfähig sein. Ähnliches gilt für den
nebengeordneten Patentanspruch 11.


5.     Dennoch sieht sich der Senat an einer Patenterteilung gehindert. Wie sich
aus der Eingabe vom 15. Mai 2002 ergibt, wurden die in den drei Prüfungsbescheiden und der Anhörung behandelten Patentansprüche aus der vorliegenden

                                       -8-



Anmeldung herausgeteilt und in einer Teilungsanmeldung weiterverfolgt. Hingegen basieren der geltende wie schon der der Zurückweisung zugrunde liegende
Patentanspruch 1 (und ähnlich Nebenanspruch 11) auf den ursprünglichen Ansprüchen 8 und 9, welche offenkundig bisher nicht Gegenstand des Prüfungsverfahrens waren. Insbesondere die in Schritt b) beanspruchten Strukturbedingungen (A) bis (C) sind im bisherigen Verfahren nicht erwähnt und ersichtlich auch
nicht recherchiert worden.


Demnach hat das Deutsche Patent- und Markenamt für die geltende Fassung der
Patentansprüche bisher nicht geprüft, ob die Voraussetzungen für die Erteilung
eines Patents erfüllt sind. Weil es damit noch nicht in der Sache selbst entschieden hat, war die Anmeldung – auch um der Anmelderin keine Tatsacheninstanz zu
nehmen – zurückzuverweisen.


6.     Über die Unteransprüche brauchte bei dieser Sachlage nicht befunden zu
werden.


                                       III.


Die Rückzahlung der Beschwerdegebühr nach § 80 Abs. 3 PatG war anzuordnen,
weil sie der Billigkeit entspricht.

                                       -9-



Zwar dürfte in der Regel eine beantragte zweite Anhörung in derselben Sache
nicht mehr sachdienlich sein. Hier liegt der Fall aber anders, weil die Anmelderin
überhaupt keine Gelegenheit hatte, zu dem vermeintlichen Widerspruch Stellung
zu nehmen; denn der zurückgewiesene Patentanspruch 1 war erst mit der letzten
Eingabe eingereicht worden und die ihm zugrunde liegenden ursprünglichen Ansprüche 8 und 9 waren zuvor nicht Gegenstand des Prüfungsverfahrens gewesen.




gez.
Unterschriften
