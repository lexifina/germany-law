---
ecli: "ECLI:DE:BPatG:2014:050914B18Wpat42.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 42/14"
decided: "2014-09-05"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=51&nr=26613&anz=1119&pos=767&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-09-05_18_W-pat_42_14_NA_0.txt"
---

# Bundespatentgericht, 18 W (pat) 42/14 vom 2014-09-05

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 42/14                                                    Verkündet am
_______________                                                   5. September 2014
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache




             betreffend die Patentanmeldung 11 2005 002 347.8-53




…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 5. September 2014 durch die Vorsitzende
Richterin Dipl.-Ing. Wickborn sowie den Richter Kruppa, die Richterin Dipl.-Phys.
Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater




BPatG 154
05.11

                                        -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                         I.


Die vorliegende Patentanmeldung 11 2005 002 347.8 geht hervor aus einer PCT-Anmeldung       (Veröffentlichungsnummer      WO 2006/050534       A1),   die   am
31. Oktober 2005 unter Inanspruchnahme einer US-amerikanischen Priorität vom
29. Oktober 2004 eingereicht worden ist. Sie trägt in der deutschen Übersetzung
die Bezeichnung


         „Zeitgeber-Versetzungsmechanismus in der Umgebung einer virtuellen Maschine“.


Die Anmeldung wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts mit Beschluss vom 8. April 2009 zurückgewiesen, weil
die Gegenstände der (damals geltenden) Ansprüche 1 nach Haupt- und Hilfsantrag im Hinblick auf die im Prüfungsverfahren ermittelte Druckschrift


               D1: Microsoft Releases Virtual PC 2004 to Manufacturing To
                   Ease Customer Migration to Windows XP, Microsoft Press
                   Release: Redmond, Wash., 10. November 2003;
                   http://www.microsoft.com/presspass/press/2003/nov03/11-
                   10VPC2004RTMPR.mspx (recherchiert von der
                   Prüfungsstelle am 23. Mai 2008);
                   aktuelle Adresse: http://www.microsoft.com/en-

                                        -3-



                    us/news/press/2003/nov03/11-10vpc2004rtmpr.aspx
                    (recherchiert am 20. Mai 2014)


und unter Berücksichtigung fachmännischer Überlegungen nicht auf einer erfinderischen Tätigkeit beruhten.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Mit Anlage zur Ladung vom 10. Juni 2014 hat der Senat zur Vorbereitung auf die
mündliche Verhandlung u.a. auf die in dem internationalen Recherchebericht aufgeführten Druckschriften


               D2: US 5 317 754 A und
               D3 : US 5 381 535 A


hingewiesen.


Die Beschwerdeführerin beantragt,


      den Beschluss der Prüfungsstelle für Klasse G06F des Deutschen Patentund Markenamts vom 08. April 2009 aufzuheben und das Patent auf der
      Grundlage der folgenden Unterlagen zu erteilen:


      -        Patentansprüche 1 - 19, eingereicht in der mündlichen Verhandlung,


      -        Beschreibung Seiten 1 - 21, eingegangen am 28. März 2007,


      -        Figuren 1 - 5, eingegangen am 28. März 2007.

                                          -4-



Der seitens des Senats mit einer Gliederung versehene geltende Patentanspruch 1 lautet:

             „Verfahren, das aufweist:

     M1      Erhalten einer Anfrage, die Steuerung von einem Monitor für virtuelle
             Maschinen (VMM) an eine virtuelle Maschine (VM) zu übergeben;

     M2      Übergeben der Steuerung an die VM nach dem Erhalt der Anfrage
             von dem VMM,

     M2.1    wobei das Übergeben ein Berechnen eines Versetzungswertes umfaßt,

     M3      wobei der Versetzungswert eine Ansammlung von Zeitintervallen ist,
             während der die VM wegen einer Ausführung durch den VMM und
             anderer VMs nicht gelaufen ist, und das Berechnen des Vesetzungswertes aufweist:

     M3.1            Bestimmen einer Differenz zwischen einem Zeitgeberwert, der
                     beim Erhalt der Anfrage, die Steuerung an die VM zu übergeben, gelesen wurde und einem Zeitgeberwert, der beim Erfassen eines vorangehenden Ereignisses, das mit einer Übergabe der Steuerung von der VM an den VMM verbunden war,
                     gesichert worden ist; und
                     Subtrahieren der Differenz von einem Wert eines Zeitgeber-Versetzungsfeldes;

     M4      Empfangen, während des Betriebes der VM, einer Anfrage nach einem gegenwärtigen Wert eines Zeitgebers;

     M5      Anpassen des gegenwärtigen Wertes des Zeitgebers basierend auf
             dem Versetzungswert; und

     M6      Liefern des angepaßten Zeitgeberwertes an die VM.“

                                         -5-



Der geltende Patentanspruch 8 lautet:


            „Vorrichtung, die aufweist:

            einen Monitor für virtuelle Maschinen (VMM);

            eine Datenstruktur, die von dem VMM gesteuert wird, wobei die Datenstruktur einen Versetzungswert für eine virtuelle Maschine (VM)
            speichert; und

            Zeitgeber-Zugriffslogik, um den Versetzungswert beim Empfang einer Anfrage, die Steuerung von dem VMM an die VM zu übergeben,
            zu berechnen und um einen Wert des Zeitgebers während eines Betriebes der VMM an die VM zu geben, wobei der Wert der Zeitgebung basierend auf dem Versetzungswert angepaßt wird,

            wobei die Zeitgeber-Zugriffslogik weiter dazu dient, die Steuerung
            aufgrund des Empfangs der Anfrage von dem VMM an die VM zu
            übergeben, wobei das Übergeben das Berechnen des Versetzungswertes umfaßt, wobei der Versetzungswert eine Ansammlung von
            Zeitintervallen ist, während der die VM wegen einer Ausführung
            durch den VMM und anderer VMs nicht gelaufen ist, und

            die Zeitgeber-Zugriffslogik dazu dient, den Versetzungswert zu berechnen, indem eine Differenz zwischen einem Zeitgeberwert, der
            beim Empfang der Anfrage, die Steuerung an die VM zu übergeben,
            gelesen wurde, und einem Zeitgeberwert, der beim Erfassen eines
            früheren Ereignisses, das mit Übergang der Steuerung von der VM
            an den VMM verbunden war, gesichert worden ist, bestimmt und die
            Differenz von einem Wert eines Zeitgeber-Versetzungsfeldes subtrahiert wird.“


Der geltende Patentanspruch 15 lautet:


            „System, das aufweist:

                                         -6-



             einen Speicher, um einen Satz Felder zu speichern, die der Zeitgeber-Versetzung für eine virtuelle Maschine (VM) zugewiesen sind;
             und

             einen Prozessor, der an den Speicher gekoppelt ist, um den Satz
             Felder zu verwenden, die der Zeitgeber-Versetzung zugewiesen
             sind, um einen Versetzungswert zu berechnen und um während des
             Betriebes der VM einen Zeitgeberwert, angepaßt basierend auf dem
             Versetzungswert, für die VM als Antwort auf eine Anfrage der VM
             nach einem gegenwärtigen Wert eines Zeitgebers zur Verfügung zu
             stellen,

             wobei bei dem der Prozessor den Versetzungswert berechnet, wenn
             er die Steuerung an die VM übergibt, wobei der Versetzungswert
             eine Ansammlung von Zeitintervallen ist, während der die VM wegen
             einer Ausführung durch den VMM und anderer VMs nicht gelaufen
             ist, und der Prozessor den Versetzungswert berechnet, indem er
             eine Differenz zwischen einem Zeitgeberwert, der beim Empfang der
             Anfrage, die Steuerung an die VM zu übergeben, und einem Zeitgeberwert, der beim Erfassen eines früheren Ereignisses, das mit einem Übergang der Steuerung von der VM an den VMM verbunden
             war, gesichert worden ist, bestimmt und die Differenz von einem
             Wert eines Zeitgeber-Versetzungsfeldes subtrahiert.“


Der geltende Patentanspruch 19 lautet:


             „Maschinenlesbares Medium, welches Befehle enthält, die, wenn sie
             von einem Verarbeitungssystem ausgeführt werden, bewirken, daß
             das Verarbeitungssystem ein Verfahren durchführt nach einem der
             Ansprüche 1 bis 7.“


Wegen den geltenden abhängigen Ansprüchen 2 bis 7, 9 bis 14 und 16 bis 18 wird
auf den Akteninhalt verwiesen.

                                       -7-



Die Beschwerdeführerin macht hierzu geltend, dass die geänderten Anspruchsfassungen jeweils zulässig, neu und erfinderisch seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                        II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn der Gegenstand
des Anspruchs 1 beruht nicht auf einer erfinderischen Tätigkeit. Die Fragen der
Zulässigkeit der geltenden Ansprüche sowie der Neuheit der Anspruchsgegenstände können somit dahinstehen (vgl. BGH, Urteil vom 18. September 1990 –
X ZR 29/89, GRUR 1991, 120, 121 li. Sp. Abs. 3 – Elastische Bandage).




1.    Die Patentanmeldung betrifft virtuelle Maschinen und das Steuern des Zugriffs von virtuellen Maschinen auf einen Zeitgeber (vgl. die deutsche Offenlegungsschrift der Anmeldung DE 11 2005 002 347 T5, Abs. [0001] und [0010]).


Zum Hintergrund wird in der Anmeldung angegeben, dass Zeitgeber bei Betriebssystemen und Anwendungssoftware eingesetzt würden, um Aktivitäten zu planen.
Als Beispiel genannt wird der Zeitstempelzähler (TSC - time stamp counter) des
Intel Pentium® 4 Prozessors. Dabei handelte es sich um ein 64-bit Register, das
beim Rücksetzen der Hardware auf Null gesetzt werde und dann bei jedem
Taktzyklus des Prozessors inkrementiert werde, auch wenn der Prozessor angehalten werde. Der TSC bilde eine Zeitreferenz, die zum Messen von Zeitintervallen
nützlich sei. Bei Multiprozessorsystemen würden die Werte des TSC auf allen
Prozessoren beim Booten synchronisiert. Wenn die TSC-Werte zwischen den
Prozessoren drifteten, etwa weil ein Prozessor mit einer anderen Rate zähle als
ein anderer, könne das Planen von Prozessen durch das Betriebssystem durcheinandergebracht werden (vgl. Offenlegungsschrift, Abs. [0002] – [0004]).

                                         -8-



Die Anmeldung geht von einem System aus, bei dem ein Monitor für virtuelle Maschinen (VMM) die Steuerung, d.h. den Zugriff auf die physikalischen Ressourcen,
an verschiedene virtuelle Maschinen (VM) überträgt. Da die virtuellen Maschinen
keine Kenntnis voneinander oder von dem Monitor für virtuelle Maschinen haben,
könne es sein, dass die Werte des Zeitgebers, die den virtuellen Maschinen zur
Verfügung gestellt werden, angepasst werden müssten.



Die der Anmeldung zugrunde liegende Aufgabe besteht sinngemäß darin, einen
Zeitgeber-Versetzungsmechanismus zur Verfügung zu stellen, um den Zeitgeber
richtig zu virtualisieren und den auf den virtuellen Maschinen laufenden Gast-Betriebssystemen die Illusion zu vermitteln, dass sie auf einer besonderen Hardware-Plattform, nicht auf einer virtuellen Plattform, laufen (vgl. Offenlegungsschrift, Abs.
[0022] und [0026]).


Die der Erfindung zugrunde liegende objektive Aufgabe besteht darin, ein Verfahren, eine Vorrichtung sowie ein System zu schaffen, bei dem ein Monitor für
virtuelle Maschinen die Steuerung an verschiedene virtuelle Maschinen bei deren
Anforderung überträgt und dabei sicherzustellen, dass die mehreren virtuellen
Maschinen und der Monitor jeweils auf für sie korrekte Zeitwerte zugreifen können,
auch wenn die Steuerung zwischen dem Monitor für virtuelle Maschinen und den
virtuellen Maschinen wechselt.


Als Fachmann zur Lösung dieser Aufgabe sieht der Senat einen Ingenieur der
Informationstechnik an, der mit der Programmierung der Prozessoransteuerung in
einem System mit virtuellen Maschinen vertraut ist.


Die Aufgabe soll gelöst werden durch ein Verfahren nach Anspruch 1, eine Vorrichtung nach Anspruch 8, ein System nach Anspruch 15 und ein maschinenlesbares Medium nach Anspruch 19.

                                       -9-



Ein Monitor für virtuelle Maschinen kann hierfür einen Zeitgeber verwenden und
den verschiedenen virtuellen Maschinen angepasste Werte des Zeitgebers zur
Verfügung stellen. Bei Erhalten einer Anfrage, die Steuerung von einem Monitor
für virtuelle Maschinen an eine virtuelle Maschine zu übergeben, wird ein Versetzungswert berechnet, der gegenwärtige Wert des Zeitgebers darauf basierend
angepasst und der angepasste Zeitgeberwert an die virtuelle Maschine geliefert.




2.    Einige der in Anspruch 1 aufgeführten Merkmale bedürfen der Auslegung.


Das beanspruchte Verfahren umfasst das Erhalten einer Anfrage, die Steuerung
vom Monitor für virtuelle Maschinen (VMM) an die virtuelle Maschine (VM) zu
übergeben, d.h. die Anfrage nach Übergabe der Steuerung an eine virtuelle Maschine, was in der Anmeldung auch als „Eintritt“ einer virtuellen Maschine bezeichnet wird (vgl. Offenlegungsschrift, Abs. [0024], Merkmal M1). Dabei besteht
die Umgebung der virtuellen Maschine aus einer Rechenplattform, auf welcher der
Monitor für virtuelle Maschinen ausgeführt wird. Der Monitor für virtuelle Maschinen (VMM) kann innerhalb oder über einem anderen Monitor für virtuelle Maschinen laufen und in Hardware, Software, Firmware oder durch eine Kombination
verschiedener Techniken implementiert sein (vgl. Abs. [0017] und [0018] der Offenlegungsschrift). Nach dem Erhalt der Anfrage soll die Steuerung von dem Monitor für virtuelle Maschinen an die virtuelle Maschine übergeben werden (Merkmal
M2), d.h. es soll ein Eintritt der virtuellen Maschine erfolgen (vgl. Offenlegungsschrift, Abs. [0024]). Während der Übergabe der Steuerung wird ein Versetzungswert berechnet, der die Summe der Zeitintervalle ist, während der die virtuelle Maschine, an die die Steuerung übergeben werden soll, wegen einer Ausführung
durch den Monitor für virtuelle Maschinen oder anderer virtueller Maschinen nicht
gelaufen ist (Merkmal M3). Der Versetzungswert gibt demnach die Zeitspanne seit
dem letzten Austritt dieser virtuellen Maschine, d.h. der Übertragung der Steuerung von der virtuellen Maschine an den Monitor für virtuelle Maschinen (vgl. Of-

                                      - 10 -



fenlegungsschrift, Abs. [0024]), an und dient als Korrekturwert für den gegenwärtigen Wert eines Zeitgebers (vgl. Merkmal M5). Unter dem Begriff des gegenwärtigen Wertes des Zeitgebers ist der Zeitwert zu verstehen, der beispielsweise durch
den Zeitstempelzähler der Rechenplattform fortlaufend inkrementiert wird und eine
Systemzeit darstellt, die unabhängig von den einzelnen Laufzeiten der unterschiedlichen virtuellen Maschinen weiterläuft (vgl. Abs. [0003], [0026] und [0028]
der Offenlegungsschrift). Auf eine während des Betriebs der virtuellen Maschine
gestellte Anfrage nach einem gegenwärtigen Wert eines Zeitgebers hin wird an die
virtuelle Maschine (VM) schließlich ein angepasster Zeitgeberwert übergeben,
welcher anhand des gegenwärtigen Werts des Zeitgebers und des Versetzungswerts ermittelt wird (Merkmale M4, M5, M6). Merkmal M3.1 legt als konkrete Berechnungsvorschrift des Versetzungswertes fest, dass eine Differenz zwischen
Werten des Zeitgebers zu bestimmten Zeitpunkten – dem Zeitpunkt der Anfrage
nach dem VM-Eintritt und dem Zeitpunkt eines vorangegangenen VM-Austritts –
bestimmt werden soll und dass diese Differenz von einem Wert eines Zeitgeber-Versetzungsfeldes subtrahiert werden soll. Welchen Wert das Zeitgeber-Versetzungsfeld besitzt, ist durch den Anspruch nicht festgelegt. Das Zeitgeber-Versetzungsfeld kann als ein Datenfeld verstanden werden, in dem der vor der aktuell
erfolgenden Berechnung geltende Versetzungswert für die jeweilige virtuelle Maschine abgelegt ist – bei erstmaligem Durchlauf des beanspruchten Verfahrens
kann dieses Versetzungsfeld beispielsweise den Wert Null aufweisen.



3.     Das Verfahren des Patentanspruchs 1 beruht nicht auf einer erfinderischen
Tätigkeit gegenüber dem Stand der Technik gemäß Druckschrift D3 i.V.m. Druckschrift D2.


Druckschrift D3 offenbart ein Datenverarbeitungssystem, auf dem ein Host-Betriebssystem und mehrere Level von virtuellen Maschinen (virtual machine guests)
laufen (vgl. Abstract) und bei dem auch der virtuellen Maschine des zweiten Levels (second level guest) ein Zeitgeber zur Verfügung gestellt werden soll, wobei
auf zusätzliche Taktgenerator-Hardware verzichtet werden soll (vgl. Sp. 6, Z. 32 –

                                        - 11 -



34 i.V.m. Sp. 7, Z. 23 – 25). Dabei stellen das erste Level einer virtuellen Maschine (first level virtual machine) einen Monitor für virtuelle Maschinen (VMM)
und das zweite Level von virtuellen Maschinen (second level virtual machine) eine
virtuelle Maschine (VM) im Sinne der vorliegenden Anmeldung dar (vgl. Fig. 1 und
Sp. 3, Z. 59 – 61 i.V.m. Anspruch 1, dr. Abs.). Bei dem von dem Datenverarbeitungssystem durchgeführten Verfahren wird während der Prozessor unter der
Kontrolle des ersten Levels von virtuellen Maschinen läuft, eine Anfrage (request)
erhalten, ein zweites Level von virtuellen Maschinen zu initiieren, was einer Anfrage, die Steuerung von einem Monitor für virtuelle Maschinen an eine virtuelle
Maschine zu übergeben, entspricht (vgl. Anspruch 1, dr. Abs.: means for detecting
a request from a guest operating system program executing on a processor under
a first level virtual machine to initiate operation of a second level virtual machine;
vgl. auch Sp. 3, Z. 59 – 62: The creation of first level and second level guests occurs through the execution of a Start Interpretive Execution (SIE) instruction /
Merkmal M1). Nach dem Erhalt der Anfrage von der einen Monitor für virtuelle
Maschinen darstellenden virtuellen Maschine des ersten Levels wird die Ausführung des Programms des zweiten Levels der virtuellen Maschinen durch den Prozessor initiiert, was nichts anderes bedeutet, als dass die Steuerung an die virtuelle Maschine (second level virtual machine) übergeben wird (vgl. Anspruch 1,
fünfter Abs.: means for initiating program execution of tile second level virtual machine on the processor in the response to the request … / Merkmal M2).


Druckschrift D3 ist auch zu entnehmen, dass in einem System mit einer einen Monitor für virtuelle Maschinen darstellenden virtuellen Maschine des ersten Levels
und mehreren virtuellen Maschinen des zweiten Levels die jeweiligen virtuellen
Maschinen die Zeitintervalle, in denen eine andere virtuelle Maschine die Kontrolle
über die physikalischen Ressourcen besitzt, berücksichtigen müssen, wofür Zeitintervalle und Zeitkomparatoren bereitzustellen sind (vgl. Sp. 2, Z. 33 – 42 i.V.m.
Anspruch 1, dr. Abs.). Dies bedeutet nichts anderes, als dass in dem System ein
Versetzungswert berechnet wird, der eine Ansammlung von Zeitintervallen ist. Da
die virtuelle Maschine des ersten Levels einen Monitor für virtuelle Maschinen dar-

                                       - 12 -



stellt und die Zeitintervalle, während der eine virtuelle Maschine wegen der Ausführung anderer virtueller Maschinen nicht gelaufen ist, berechnet werden (vgl.
insbes. Sp. 2, Z. 39 – 40: … must account for the periods of time when a different
guest has control of the real machine resources), schließt dies auch die Berücksichtigung von Zeitintervallen ein, während der eine virtuelle Maschine wegen
Ausführung durch den Monitor für virtuelle Maschinen nicht gelaufen ist (Merkmal
M3).


Angegeben wird auch, dass die Zeitintervalle ermittelt werden können, indem die
Zeit des (einzigen) Zeitgebers (clock) zu verschiedenen Zeitpunkten miteinander
verglichen wird (vgl. Sp. 2, Z. 36 – 38). Für den Fachmann versteht es sich von
selbst, dass in Zusammenhang mit einem System aus einem Monitor für virtuelle
Maschinen und einer oder mehrerer virtueller Maschinen, beispielsweise der Eintritt und der Austritt einer virtuellen Maschine geeignete Zeitpunkte darstellen, um
die zu kontierenden Zeitintervalle zu ermitteln (teilweise Merkmal M3.1, ohne konkrete Angabe der Berechnungsvorschrift).
Der Versetzungswert lässt sich prinzipiell auf verschiedene Arten berechnen. Wie
in der vorliegenden Anmeldung ausgeführt, kann er anstatt wie in Merkmal M3.1
beansprucht, durch Subtraktion einer ermittelten Differenz von einem Wert eines
Zeitgeber-Versetzungsfeldes auch als Differenz zwischen dem tatsächlichen Zeitgeberwert und dem Zeitgeberwert, der von der jeweiligen virtuellen Maschine erwartet wird, berechnet werden oder als Summe aus dem gegenwärtigen Zeitgeberwert und dem durch den Monitor für virtuelle Maschinen konfigurierten Zeitgeberwert (vgl. Offenlegungsschrift, Abs. [0028]). Welche Rechenvorschrift der
Fachmann letztlich für das Verfahren implementiert, liegt in seinem Belieben.
Denn für die Wahl einer konkreten Rechenvorschrift für den Versetzungswert sind
keine technischen Überlegungen, die sich auf Parameter der für die Durchführung
des beanspruchten Verfahrens verwendeten Rechenplattform beziehen, erforderlich. Die Auswahl einer Rechenvorschrift aus einer Vielzahl von alternativ möglichen Rechenvorschriften, welche zum selben Ergebnis eines Versetzungswertes
führen, kann daher keine erfinderische Tätigkeit begründen. Für den Fachmann ist

                                        - 13 -



es vielmehr naheliegend, als konkrete Rechenvorschrift beispielsweise vorzusehen, dass der ermittelte Differenzwert von einem Wert eines in einem Datenfeld
gespeichert vorliegenden Versetzungswertes abgezogen wird, und damit den Wert
zu bestimmen, mit dem die Systemzeit für die virtuelle Maschine zu korrigieren ist
(Merkmal M3.1).


Druckschrift D3 sieht vor, beim Einstieg einer virtuellen Maschine Parameter einer
Zeitgebereinheit (timing facility parameters), die in einem Kontrollblock der virtuellen Maschine gespeichert sind, zu laden, die Werte der Zeitgeberparameter während des Betriebes der virtuellen Maschine periodisch zu aktualisieren und beim
Ausstieg der virtuellen Maschine die aktualisierten Werte abzuspeichern (vgl. Anspruch 4, dritter – fünfter Abs.). Beschrieben wird, dass die Zeitgebereinheit der
virtuellen Maschine nur dann überprüft wird, wenn die virtuelle Maschine läuft (vgl.
Sp. 6, Z. 55 – 57: The second level guest timing facilities are checked only when a
second level guest is running.), was bedeutet, dass nur während des Betriebs der
virtuellen Maschine eine Anfrage nach einem gegenwärtigen Wert des Zeitgebers
der virtuellen Maschine gestellt und damit empfangen werden kann (Merkmal M4).


Während der Prozessor unter der Steuerung der virtuellen Maschine des zweiten
Levels läuft, werden gemäß Druckschrift D3 die Zeitwerte auf dem zweiten Level
wiederkehrend überprüft (vgl. Sp. 6, Z. 46 – 57, insbes. Z. 47 - 52: … the second
level timing facilities are only checked periodically and not at every clock tick. …
This processing occurs, for example, every 256 microseconds …), was ein Anpassen eines gegenwärtigen Werts des virtuellen Zeitgebers der virtuellen Maschine
darstellt. Bei dieser Anpassung wird für die virtuelle Maschine der Zeitkomparator
und der Wert des CPU Zeitgebers bezogen auf den Hardware-Zeitwert ermittelt,
was bedeutet, dass die Anpassung basierend auf einem Versetzungswert erfolgt
(vgl. Sp. 6, Z. 51 – 55, insbes. Z. 51 - 54: This processing … includes an evaluation of the second level guest clock comparator 612 and CPU timer values relative
to the hardware TOD value … / Merkmal M5). In Druckschrift D3 wird der ermittelte angepasste Zeitgeberwert in einem speziell für die virtuelle Maschine des

                                       - 14 -



zweiten Levels vorgesehenen Arbeitsspeicherbereich abgelegt (vgl. Sp. 6, Z. 57 –
59 i.V.m. Fig. 6: The timing facility values are stored in a local reserve working
store array as shown in Fig. 6.); dieses Abspeichern des angepassten Zeitgeberwertes in einen der virtuellen Maschine jederzeit zugänglichen Bereich des Arbeitsspeichers entspricht einem Liefern des angepassten Zeitgeberwerts an die
virtuelle Maschine (Merkmal M6).


Der Fachmann entnimmt Druckschrift D3 somit ein Verfahren mit einem Zeitgeber-Versetzungsmechanismus in der Umgebung einer virtuellen Maschine, das die
Merkmale M0, M1, M2, M3, M3.1, M4, M5 und M6 des Patentanspruchs 1 aufweist, bei dem die Berechnung eines Versetzungswertes jedoch nicht, wie in
Merkmal M2.1 angegeben, zum Zeitpunkt der Übergabe der Steuerung an die
virtuelle Maschine erfolgt, sondern zu bestimmten wiederkehrenden Zeitpunkten.


Druckschrift D3 ist ferner der Hinweis zu entnehmen, dass eine fortwährende Abfrage der Zeitgebereinheit der virtuellen Maschine zu einem Overhead führt und
die Effizienz des Prozessors vermindert (vgl. Sp. 6, Z. 43 – 45), weswegen – wie
zu Merkmal M5 ausgeführt – eine periodische Abfrage vorgeschlagen wird. Wenn
der Fachmann beim Nacharbeiten der Lehre der Druckschrift D3 feststellt, dass
selbst bei einer nur periodisch vorgesehenen Abfrage des Zeitgebers der virtuellen
Maschine die Effizienz des Prozessors leidet, so steht er vor der Frage, wie er
diesen Overhead weiter reduzieren kann.


Hierzu kann er die Druckschrift D2 heranziehen, in der es um das effiziente Betreiben von virtuellen Maschinen auf einem Hostsystem geht (vgl. D2, Sp. 2, Z. 59
– Sp. 3, Z. 4, Abschnitt Summary of the Invention).


Druckschrift D2 offenbart ein Verfahren zur Steuerung von virtuellen Maschinen
(virtual machines – VM), bei dem ein Monitor für virtuelle Maschinen (host control
program) und fakultativ ein Zeitgeberversetzungsmechanismus (timing facility)
zum Einsatz kommen (vgl. Anspruch 1, Fig. 1 und 7, Sp. 3, Z. 36 – 37). Nach dem

                                        - 15 -



Erhalten einer Anfrage, die Steuerung an eine virtuelle Maschine zu übergeben,
wird die Steuerung an die virtuelle Maschine übergeben, wobei Parameter der
virtuellen Maschine aus einer Zustandsbeschreibung heraus geladen werden (vgl.
Sp. 3, Z. 61 – 63 / Merkmale M1, M2). Sofern durch einen Indikator (timing mode
subset indicator 612) festgelegt ist, dass der Zeitgeberversetzungsmechanismus
aktiviert ist, werden beim Eintritt einer virtuellen Maschine auch Zeitgeberwerte
übergeben (vgl. die den Einstieg einer virtuellen Maschine betreffende Fig. 7:
Block 712 mit Beschreibung Sp. 5, Z. 34). Da die Übergabe von Zeitgeberwerten
nur fakultativ vorgesehen ist, liest der Fachmann mit, dass auch eine Berechnung
der Zeitgeberwerte nur dann erfolgt, wenn diese angefordert werden, da andernfalls die Zeitgeberwerte überflüssigerweise berechnet worden wären; dem Fachmann ist es damit nahegelegt, mit dem Übergeben der Steuerung an die virtuelle
Maschine – bei entsprechendem Indikatorwert – auch die Berechnung der Zeitgeberwerte vorzunehmen (Merkmal M2.1). Für die Art der Berechnung wird in
Druckschrift D2 keine konkrete Angabe gemacht, in allgemeiner Form aber in
Spalte 2, Zeilen 48 bis 55 wortidentisch zu Druckschrift D3 auf die Ermittlung von
Zeitintervallen verwiesen (vgl. D3, Sp. 2, Z. 36 – 42).


Die Anmelderin hat ausgeführt, das beanspruchte Verfahren sei besonders ressourcenschonend und nicht äquivalent zu den in Druckschrift D3 oder D2 offenbarten Methoden. Insbesondere die in Druckschrift D3 erläuterte periodische Ermittlung von Zeitgeberwerten sei eine technisch schlechtere Lösung, zudem gehe
es bei dem Verfahren in Druckschrift D3 allein um die Tageszeit (TOD – time of
day).


Dieser Argumentation kann der Senat nicht beitreten. Dem geltenden Anspruch 1
ist kein Hinweis zu entnehmen, um welche Art von Zeit (Tageszeit, CPU Zeit, etc.)
es sich bei den verschiedenen Werten eines Zeitgebers (vgl. die Merkmale M3.1
bis M6) handeln soll. Zum anderen gibt gerade der in Druckschrift D3 (vgl. Sp. 6,
Z. 43 – 45) und in Druckschrift D2 (vgl. Abstract, dr. und vorle. Satz und Sp. 2,
Z. 55 – 58) explizit im Zusammenhang mit einem Zeitgeber-Versetzungsmecha-

                                       - 16 -



nismus angesprochene Overhead dem Fachmann Veranlassung, zu dessen Vermeidung weitere Optimierungsmaßnahmen vorzusehen, welche, wie zu Druckschrift D2 erläutert, auch darin bestehen können, den Zeitgeber-Versetzungsmechanismus nur beim Eintritt einer virtuellen Maschine zu aktivieren. Bereits die in
Druckschrift D3 gemachte Angabe, dass eine ständige Ermittlung des Zeitgeberwertes vorteilhaft zu ersetzen ist durch eine nur mehr in bestimmten periodischen
Abständen vorzusehende Ermittlung (vgl. D3, Sp. 6, Z. 43 – 48) ist für den Fachmann ein Hinweis, dass zur Vermeidung des Overheads eine seltenere Ermittlung
sinnvoll ist. Druckschrift D2 entnimmt der Fachmann, dass als geeigneter Zeitpunkt der Ermittlung der Zeitpunkt der Anfrage nach einem Eintritt einer virtuellen
Maschine ist.


Das Verfahren des geltenden Patentanspruchs 1 ist für den Fachmann daher in
Kenntnis von Druckschrift D3 i.V.m. Druckschrift D2 nahegelegt. Das Verfahren
des Anspruchs 1 beruht somit nicht auf einer erfinderischen Tätigkeit.


Der geltende Patentanspruch 1 ist daher nicht patentfähig.




4.    Mit dem nicht patentfähigen Anspruch 1 sind auch die nebengeordneten
Ansprüche 8, 15 und 19 und die auf diese Ansprüche direkt oder indirekt rückbezogenen Unteransprüche nicht schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war und über einen Antrag nur einheitlich entschieden werden kann (vgl. BGH, Beschluss vom 27. Juni 2007 – X ZB 6/05,
GRUR 2007, 862, Abschnitt III. 3. a) aa) – Informationsübermittlungsverfahren II).




5.    Die Beschwerde war somit zurückzuweisen.

                                       - 17 -



                                         III.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass

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




Wickborn                 Kruppa        Dr. Otten-Dünnweber              Altvater


                                                                              Hu
