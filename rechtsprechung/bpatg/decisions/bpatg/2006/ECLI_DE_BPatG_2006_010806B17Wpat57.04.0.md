---
ecli: "ECLI:DE:BPatG:2006:010806B17Wpat57.04.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 57/04"
decided: "2006-08-01"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2006&Sort=1&Seite=65&nr=1728&anz=1665&pos=985&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2006-08-01_17_W-pat_57_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0079.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 57/04 vom 2006-08-01

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 57/04                                                 Verkündet am
 _______________                                                  1. August 2006
    (Aktenzeichen)                                                      …




                           BESCHLUSS

                          In der Beschwerdesache


               betreffend die Patentanmeldung 102 29 676.6-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 1. August 2006 unter Mitwirkung …




BPatG 154
08.05

                                      -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
       Markenamts vom 12. Dezember 2003 aufgehoben und die Sache
       im Umfang des Hauptantrags zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückverwiesen.


                                   Gründe


                                       I.


Die vorliegende Patentanmeldung ist am 27. Juni 2002 beim Deutschen Patentund Markenamt eingereicht worden unter der Bezeichnung:


          „Verfahren und Steuergerät zur Steuerung des Ablaufs eines
                   multitaskingfähigen Computerprogramms“.


Sie wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts vom 12. Dezember 2003 mit der Begründung zurückgewiesen, dass der Gegenstand des Patentanspruchs 1 auf keiner erfinderischen
Tätigkeit beruhe; hinsichtlich des nebengeordneten Anspruchs 15 lasse allein die
Beanspruchung von Mitteln in einem Computerprogramm zur Ausführung des Verfahrens keine für den Fachmann ausführbare Lehre erkennen.

                                      -3-



Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin. Sie stellt
den Antrag:


       Der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 12. Dezember 2003 wird aufgehoben und das Patent erteilt auf der Grundlage folgender Unterlagen:


       - Patentanspruch 1 + 2, überreicht in der mündlichen Verhandlung vom 1. August 2006, sowie noch anzupassende Unterlagen (weitere Ansprüche, Beschreibung, Zeichnungen)


       - hilfsweise:
            Patentanspruch 1 nach Hilfsantrag, überreicht in der mündlichen Verhandlung vom 1. August 2006, sowie noch anzupassende Unterlagen (weitere Ansprüche, Beschreibung, Zeichnungen).


Die Anmelderin regt ferner die Rückerstattung der Beschwerdegebühr an.


Die Patentansprüche 1 und 2 gemäß Hauptantrag lauten:


       1.     Verfahren zur Steuerung und/oder Regelung eines Systems,
       das verschiedene mögliche Systemzustände (30) einnehmen
       kann, mittels eines multitaskingfähigen Computerprogramms (22)
       auf einem Rechengerät (21) eines Steuergeräts (20),

                                -4-



umfassend die nachfolgenden vor dem eigentlichen Ablauf des
Computerprogramms (22) auszuführenden Verfahrensschritte:


- Unterteilen des Computerprogramms (22) in mehrere funktional
  zusammenhängende Funktionalitäten (X);


- Definition von möglichen Betriebszuständen (A, B, C) für die
  Funktionalitäten (X);


- Definition der möglichen Systemzustände (30) des Systems, indem den Funktionalitäten (X) für jeden Systemzustand (30)
  vorgebbare Betriebszustände (A, B, C) zugeordnet werden; und


- Ermitteln von Abhängigkeiten der Funktionalitäten (X) untereinander, wobei eine erste Funktionalität von einer zweiten Funktionalität abhängig ist, wenn mindestens eine Eingangsgröße
  (Ein_i) der ersten Funktionalität in der zweiten Funktionalität
  ermittelt wird,


dadurch gekennzeichnet, dass das System in einem ersten Systemzustand betrieben wird und während der Laufzeit des Computerprogramms (22):


- Fehler (11, 12) in dem System erkannt werden;


- anhand der Fehler (11, 12) ein Fehlerzustand (13) des Systems
  ermittelt wird;


- in Abhängigkeit des Fehlerzustands (13) ein zweiter Systemzustand und eine Strategie (14) zum Übergang in den zweiten Systemzustand ermittelt wird;

                                         -5-



        - überprüft wird, ob die den zweiten Systemzustand charakterisierenden Funktionalitäten die für den zweiten Systemzustand
             geforderten Betriebszustände aufweisen und


        - in den zweiten Systemzustand übergegangen wird, wenn die
             den zweiten Systemzustand charakterisierenden Funktionalitäten die für den zweiten Systemzustand geforderten Betriebszustände aufweisen.


        2.     Verfahren nach Anspruch 1, dadurch gekennzeichnet, dass
        die Fehler (11, 12) zur Laufzeit nicht verfügbare Eingangsgrößen
        (Ein_i) umfassen und in dem zweiten Systemzustand nicht verfügbare Eingangsgrößen


        - anhand anderer Größen modelliert,


        - mittels alternativer Algorithmen berechnet, oder


        - durch andere verfügbare Größen ersetzt werden.


Im Patentanspruch 1 gemäß Hilfsantrag sind die Merkmale des Anspruchs 2 nach
Hauptantrag in den Anspruch 1 mit aufgenommen worden; wegen des genauen
Wortlauts wird auf die Akte verwiesen.


Diesen Patentansprüchen soll die Aufgabe zugrunde liegen, bei komplexen
sicherheitskritischen   Steuer-   und    Regelungssystemen,   die   mittels   eines
multitaskingfähigen Computerprogramms arbeiten, die Verfügbarkeit und Sicherheit der Steuerung / Regelung zur Laufzeit zu gewährleisten bzw. zu erhöhen.


Zur Begründung ihrer Beschwerde führte die Anmelderin aus, dass die nunmehr
geltenden Patentansprüche eine ausführbare technische Lehre gäben, die neu sei

                                       -6-



und – erst recht in der Fassung nach Hilfsantrag – durch den im Verfahren befindlichen Stand der Technik nicht nahegelegt werde.


Die Rückzahlung der Beschwerdegebühr entspreche der Billigkeit, denn ihr Anspruch auf rechtliches Gehör sei verletzt worden, weil die Prüfungsstelle ihr die
beantragte Anhörung verweigert habe. Ferner sei die Begründung des Zurückweisungsbeschlusses mängelbehaftet, da dort auf die in der letzten Eingabe vorgebrachte ausführliche Argumentation nicht eingegangen werde und in unzulässiger
Weise die Frage der Technizität und die Frage der erfinderischen Tätigkeit vermischt würden.


                                        II.


Die in rechter Frist und Form erhobene Beschwerde ist zulässig. Sie führt zur Aufhebung des angefochtenen Beschlusses und zur Zurückverweisung der Sache an
das Deutsche Patent- und Markenamt (§ 79 Abs. 3 Satz 1 PatG) im Umfang des
Hauptantrags.


1.    Die von der Anmelderin in der mündlichen Verhandlung eingereichten
Patentansprüche nach Haupt- und Hilfsantrag sind zulässig, denn Ansprüche
können bis zur Patenterteilung im Rahmen der ursprünglichen Offenbarung beliebig geändert, ggf. auch erweitert werden (BGH GRUR 1988, 197 „Runderneuern“).
Im vorliegenden Fall ergibt sich die ursprüngliche Offenbarung aus Seite 1 letzter
Absatz, Anspruch 1, Anspruch 5 / 6, Figur 3 und Seite 15 Absatz 2 bis Seite 19
Absatz 1 der Anmeldungsunterlagen.


Zumindest unter Heranziehung der Beispiele aus der Beschreibung geben sie
dem Fachmann auch eine klare und ausführbare Lehre.


Als Fachmann ist hier ein Entwicklungsingenieur für Steuer- und Regelungssysteme mit Hochschulschulausbildung und mehrjähriger Berufserfahrung anzusehen,

                                        -7-



der mit der Programmierung von Mikroprozessorsystemen vertraut ist und gute
Kenntnisse in der Parallel-Programmierung (Multitasking-Programmierung) hat.


2.    Die nunmehr beanspruchte Lehre ist auch technischer Natur.


Denn um bei komplexen sicherheitskritischen Steuer- und Regelungssystemen die
Auswirkungen des Einsatzes eines multitaskingfähigen Computerprogramms zu
erkennen und eine geeignete Lösung dafür zu entwickeln, ist technischer Sachverstand erforderlich. Ein konkretes technisches Problem ist in der Frage zu sehen,
wie das Aufrechterhalten des Steuer- oder Regelungsbetriebs bei Fehlerzuständen sichergestellt werden kann, und die technischen Maßnahmen zur Lösung liegen hier insbesondere darin, anhand geforderter Betriebszustände definierte
Systemzustände vorzusehen, deren Betriebsweise vorbestimmt ist, und Übergangsstrategien zwischen den Systemzuständen festzulegen, so dass das Gesamtsystem auch bei Auftreten von Fehlersignalen immer in einem definierten
Funktionszustand ist. Um eine solche Lehre zu formulieren, sind zwangsläufig
technische Überlegungen notwendig, die Kenntnisse eines Informatikers allein reichen nicht aus.


3.    Der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag ist neu gegenüber dem im bisherigen Prüfungsverfahren genannten Stand der Technik und beruht insoweit auch auf erfinderischer Tätigkeit.


Von den im Verfahren befindlichen Druckschriften:


        D1   EP 0 990 966 A2
        D2   DE 38 72 421 T2
        D3   US 6 219 590 B1
        D4   DE 195 00 957 A1
        D5   DE 199 24 461 A1

                                        -8-



kommt D5 dem Anmeldungsgegenstand am nächsten. Sie beschreibt eine objektorientierte Werkzeugmaschinensteuerung durch einen Mikroprozessor (3), wobei
Multitasking-Betriebssysteme in diesem Zusammenhang als bekannt erwartet werden (siehe z. B. Spalte 5 Zeile 33 – 37). Als „Systemzustände“ können dabei die
Initialisierungsphase der Steuerung einerseits, der reguläre Betrieb der Steuerung
andererseits verstanden werden (siehe Spalte 6 Zeile 23 – 28). Das auf dem Mikroprozessor laufende Programm ist vorab in Funktionalitäten unterteilt worden,
die verschiedene Betriebszustände haben können (z. B. „noch nicht fertig“ und
„fertig initialisiert“, vgl. Spalte 4 Zeile 60 – Spalte 5 Zeile 3). Für den Wechsel in
den Systemzustand „regulärer Betrieb der Steuerung“ sind entsprechende Betriebszustände der Funktionalitäten erforderlich (Spalte 8 Zeile 36 – 49). Gemäß
den vorab ermittelten Abhängigkeiten der Funktionalitäten untereinander haben
übergeordnete Funktionalitäten die Meldungen der untergeordneten abzuwarten
(Spalte 4 Zeile 64 – Spalte 5 Zeile 3). Das Erkennen von Fehlern während des
laufenden Betriebs und Übergangsstrategien hin zu verschiedenen bestimmte
Fehler berücksichtigenden Systemzuständen und zurück sind jedoch in D5 nicht
beschrieben.


Eine Anregung in dieser Richtung könnte der Fachmann teilweise der D3 entnehmen. Diese beschreibt eine Regelung für Gebäude-Klimaanlagen (Heizung und
Kühlung) mittels eines Mikroprozessor-Programms. Gemäß Spalte 9 Zeile 17 – 63
führt das Erkennen von Fehlern zu einer Änderung des Regelungsverfahrens;
nach Behebung des Fehlers schaltet das Programm selbständig auf Normalbetrieb zurück. Dies ist jedoch nur eine sehr einfache Lösung, vor allem weil in D3
keine Abhängigkeiten der verschiedenen Funktionalitäten voneinander vorgesehen sind. Daher braucht keine Strategie für den Übergang in einen zweiten Systemzustand ermittelt zu werden, und der Übergang in den zweiten Systemzustand
setzt nicht voraus, dass zunächst die beteiligten Funktionalitäten überprüft werden, ob sie die geforderten Betriebszustände aufweisen, bevor dann ein definierter
Systemübergang erfolgen darf.

                                       -9-



Anregungen in diese Richtung fehlen im bisher vorliegenden Stand der Technik;
D1, D2 und D4 liegen noch weiter entfernt und helfen hier nicht weiter. So beschreibt D1 eine Steuerung für ein Spritzgießsystem als multitaskingfähiges Programm für einen Mikroprozessor. Verschiedene Systemzustände, neben dem Normalbetrieb etwa „slowdown“ oder „stepped shutdown“ als Reaktion auf einen Fehler, sind zwar vorgesehen, nicht aber systematisierte Voraussetzungen für einen
Zustandswechsel. D2 betrifft die Reaktion einer adaptiven Motorsteuerung mit verschiedenen Systemzuständen auf einen erkannten Zustandswechsel, nicht die
Herbeiführung eines Zustandswechsels nach Vorliegen der dafür definierten Bedingungen. In D4 geht es um ein Verfahren zur Steuerung technischer Vorgänge,
ausgeführt als Steuerprogramm für einen Mikrorechner, mit einem Multitasking-Betriebssystem. Hier wird etwa beschrieben, dass eine Task, die Daten von anderen Tasks benötigt, auf diese warten muss; von Fehlerzuständen oder Strategien
zum Wechsel des Systemzustands als Reaktion auf Fehler ist jedoch keine Rede.


Da derartig komplexe Überlegungen, wie sie den kennzeichnenden Merkmalen
des Patentanspruchs 1 gemäß Hauptantrag zugrunde liegen, für den Fachmann
auch nicht als ohne Weiteres naheliegend bezeichnet werden können, beruht der
Gegenstand dieses Anspruchs gegenüber dem abgehandelten Stand der Technik
auf erfinderischer Tätigkeit.


4.     Im Laufe des Beschwerdeverfahrens hat sich das Patentbegehren jedoch
wesentlich geändert. Somit konnte das Deutsche Patent- und Markenamt für die
geltende Fassung bisher nicht prüfen, ob die Voraussetzungen für die Erteilung
eines Patents erfüllt sind. Weil es damit noch nicht in der Sache selbst entschieden hat, war die Anmeldung – auch um der Anmelderin keine Tatsacheninstanz zu
nehmen – nach § 79 Absatz 3 Satz 1 Nr. 1 PatG dorthin zurückzuverweisen.


Das Deutsche Patent- und Markenamt wird dabei zunächst zu prüfen haben, ob
die Änderungen in der Anspruchsformulierung nicht auch eine Änderung der Klas-

                                      - 10 -



sifizierung und damit einen Wechsel der zuständigen Prüfungsstelle zur Folge haben.


5.     Da dem Hauptantrag stattgegeben wurde, war auf den Hilfsantrag nicht
einzugehen.


                                       III.


Für die von der Anmelderin angeregte Rückzahlung der Beschwerdegebühr sieht
der Senat keine hinreichende Veranlassung.


Der Grundsatz des rechtlichen Gehörs ist nicht verletzt worden, da die Anmelderin
mit ihrer Eingabe vom 8. Juli 2003 zu den Argumenten der Prüfungsstelle hatte
Stellung nehmen können und im Zurückweisungsbeschluss nicht anders argumentiert wurde. Zwar ist eine einmalige Anhörung i. d. R. sachdienlich (siehe
BPatGE 18, 30); allerdings ist dem Prüfer dabei ein der gerichtlichen Nachprüfung
entzogener Beurteilungsspielraum zuzugestehen (BPatGE 26, 44).


So mag im vorliegenden Fall der Senat zwar der Ansicht sein, dass die Durchführung der beantragten Anhörung für die Anmelderin vermutlich verfahrensökonomischer gewesen wäre; objektive Gründe dafür, dass die Prüfungsstelle ihren Beurteilungsspielraum überschritten hätte, sind jedoch nicht ersichtlich (vgl. Busse,
PatG, 6. Auflage (2003), § 46 Rdnr. 13, 19 – 21). Hierbei ist insbesondere auch zu
berücksichtigen, dass die Anmelderin mit der Verteidigung der zurückgewiesenen
Patentansprüche 1 und 15 vor dem Senat ebenfalls keinen Erfolg hatte.


Der Zurückweisungsbeschluss ist - im Rahmen der Prüfung des § 80 Abs. 3
PatG - auch nicht deswegen fehlerbehaftet, weil die Prüfungsstelle auf die ausführliche Argumentation der Anmelderin in ihrer Eingabe vom 8. Juli 2003 nicht in
gleichem Umfang eingegangen ist. Selbstverständlich ist die Prüfungsstelle verpflichtet, auch dieses Vorbringen zur Kenntnis zu nehmen und in Erwägung zu

                                      - 11 -



ziehen; hieraus kann aber nicht abgeleitet werden, dass sie sich mit jedem Argument in der Begründung ihrer Entscheidung ausdrücklich befassen muss (vgl.
BGH BlPMZ 1999, 310 „Zugriffsinformation“ für gerichtliche Entscheidungen).
Dass die Eingabe vom 8. Juli 2003 bei der Entscheidung berücksichtigt wurde,
zeigt sich an mehreren Formulierungen im Zurückweisungsbeschluss, nicht zuletzt
an der wörtlichen Wiedergabe des mit ihr neu eingereichten Patentanspruchs 1.


Auch die Frage, inwieweit Technizität und erfinderische Tätigkeit unzulässig vermischt wurden, betrifft allenfalls die Qualität der Argumentation, vermag aber das
Ergebnis, nämlich die zu Recht erfolgte Zurückweisung, nicht zu ändern.


Die von der Prüfungsstelle im vorliegenden Fall gewählte Vorgehensweise liegt
nach Auffassung des Senats daher noch im Rahmen ihres pflichtgemäßen Ermessens.


gez.
Unterschriften
