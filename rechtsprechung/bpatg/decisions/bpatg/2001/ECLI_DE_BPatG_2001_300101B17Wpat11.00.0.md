---
ecli: "ECLI:DE:BPatG:2001:300101B17Wpat11.00.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 11/00"
decided: "2001-01-30"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2001&Sort=1&Seite=8&nr=21112&anz=1792&pos=122&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2001-01-30_17_W-pat_11_00_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 11/00 vom 2001-01-30

## Entscheidung

BUNDESPATENTGERICHT

                                                                     Verkündet am
                                                                    30. Januar 2001
 17 W (pat) 11/00
                                                                           …
    (Aktenzeichen)




                               BESCHLUSS

                              In der Beschwerdesache


               betreffend die Patentanmeldung 195 26 800.8-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 30. Januar 2001 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Grimm, der Richter Dipl.-Ing. Bertl und Dipl.-Ing. Prasch
sowie der Richterin Püschel




BPatG 154
6.70

                                     - 2 -



beschlossen:


        Die Beschwerde wird zurückgewiesen.




                                  Gründe:


                                       I.


Die Patentanmeldung mit der Bezeichnung


        "Verfahren zum Datenaustausch zwischen einer Datenverarbeitungseinrichtung und einer Bussteuereinrichtung"


wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts zurückgewiesen. In den Gründen ist ausgeführt, daß der Patentanspruch 1 nicht gewährbar sei, da sein Gegenstand nicht auf einer erfinderischen
Tätigkeit beruhe.


Gegen diesen Beschluß richtet sich die Beschwerde der Anmelderin.


Der geltende Patentanspruch 1 nach Hauptantrag lautet:


        "Verfahren zum Datenaustausch zwischen einer Datenverarbeitungseinrichtung und einer an einer Busleitung eines bidirektionalen, seriellen und asynchronen Bussystems zur Übertragung
        von Datenpaketen begrenzter Länge angeschlossenen Bussteuereinrichtung, die zumindest im Empfangskanal Puffermittel zur
        abrufbaren Zwischenspeicherung einer Mehrzahl empfangener
        Datenpakete aufweist und die nach Empfang eines Datenpaketes
        ein Unterbrechungssignal generiert und an die Datenverarbei-

                                      - 3 -



        tungseinrichtung sendet, wobei die Datenverarbeitungseinrichtung
        und die Bussteuereinrichtung über einen Datenbus, einen
        Adreßbus und einen Steuersignalbus miteinander verbunden sind,
        dadurch gekennzeichnet,
        daß das Unterbrechungssignal in Abhängigkeit von der Anzahl der
        empfangenen Datenpakete und der seit Empfang des letzten
        Datenpaketes verstrichenen Zeit generiert wird."


Beim Patentanspruch 1 nach Hilfsantrag sind gegenüber dem Hauptantrag die
Worte "dadurch gekennzeichnet, daß " ersetzt durch "und wobei".


Der Anmeldung liegt die Aufgabe zugrunde, ein Verfahren zum Datenaustausch
zwischen einer Datenverarbeitungseinrichtung und einer Bussteuereinrichtung
anzugeben, das es gestattet, unter Berücksichtigung wechselnder Transferraten
mit möglichst wenigen Unterbrechungen der Abarbeitung in der Datenverarbeitungseinrichtung zum Zwecke des Datenaustausches auszukommen und trotzdem
einen verzugsarmen Datendurchsatz zu realisieren (Beschreibung Seite 2, letzter
Absatz und Seite 2a, Absatz 1).


Bei der ursprünglichen Art Daten zu übertragen sei, wie die Anmelderin ausführt,
jedes Wort sofort übernommen worden, was zu einer starken Belastung der CPU
geführt habe. Zur Abhilfe sei schon früher ein Puffer vorgesehen worden, in dem
die Datenpakete aufgesammelt wurden. Dieser Puffer werde bei einem vorgegebenen Füllstand geleert. Der Nachteil dieser Lösung liege darin, daß bei einem
geringen Datenverkehr der Füllstand nicht erreicht werde und so die Daten über
einen unzulässig langen Zeitraum in dem Puffer verblieben. Mit dem vorliegenden
Verfahren werde erreicht, die Daten vor ihrem "Verfallsdatum" auszulesen. Mit der
einteiligen Fassung des Patentanspruchs nach Hilfsantrag solle ausgedrückt werden, daß die beiden Alternativen, Füllstand und Zeitablauf, gleichwertig seien. Die
Verknüpfung dieser beiden Optionen im Patentanspruch 1 mit "und" sei im Sinne
einer Aufzählung zu verstehen.

                                      - 4 -




Die Anmelderin stellt den Antrag,


        den angefochtenen Beschluß aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen: ursprünglich eingereichte Patentansprüche 1 bis 5,
        Beschreibung Seiten 2, 2a, eingegangen am 10. Juni 1996, mit
        der Maßgabe, daß es auf Seite 2a in der ersten Zeile "verzugsarmen" statt "vorzugsarmen" heißt, sowie ursprünglich eingereichte
        Seiten 1, 3 bis 5,
        ursprünglich eingereichte 1 Blatt Zeichnung mit Figur 1,
        hilfsweise mit dem am 22. September 2000 eingegangenen Patentanspruch 1 gemäß Hilfsantrag, übrige Unterlagen wie Hauptantrag.




                                           II.


Die frist- und formgerecht erhobene Beschwerde ist zulässig. Sie hat jedoch keinen Erfolg, da der Gegenstand des Patentanspruchs 1 weder nach Haupt- noch
nach Hilfsantrag auf einer erfinderischen Tätigkeit beruht und deshalb nach § 4
PatG nicht patentfähig ist.


Beim vorliegenden Verfahren geht es um den Datenaustausch zwischen einer
Datenverarbeitungseinrichtung und einer Busleitung oder eigentlich um die Übernahme der empfangenen Daten aus einem Empfangspuffer in den Mikroprozessor. Die Daten werden von der Busleitung empfangen und in einem FIFO-Speicher gesammelt. Der Mikroprozessor soll nicht bei jedem Datenpaket unterbrochen werden, deshalb werden mehrere Pakete aufgesammelt. Ein Füllstandsanzeiger (4411) überwacht den Füllstand des FIFOs und erzeugt bei einem vorgegebenen Wert ein Signal. Andererseits soll aber ein Datenpaket, bei geringem

                                     - 5 -



Datenverkehr, nicht zu lange im FIFO verbleiben. Deshalb wird nach einer vorgegebenen Zeit ein Signal erzeugt, um das FIFO auszulesen.


Im Prüfungsverfahren wurde die Druckschrift


        DE 41 04 957 A1


genannt.


Sie betrifft eine Schaltung zur Verbindung eines Mikroprozessorsystems mit einem
Kommunikationskanal. Die empfangenen Daten werden in einem FIFO (F2)
gespeichert. Eine Signalisierungsschaltung (S) erzeugt abhängig vom Füllstand
des FIFOs ein Signal für den Mikroprozessor (MP).


Hauptantrag:


Das Verfahren nach dem Patentanspruch 1 ist neu, da es aus dieser Druckschrift
nicht bekannt ist, ein Unterbrechungssignal in Abhängigkeit von der seit Empfang
des letzten Datenpakets verstrichenen Zeit zu generieren.


Der Gegenstand des Patentanspruchs 1 beruht jedoch nicht auf einer erfinderischen Tätigkeit.


Aus der DE 41 04 957 A1 ist ein Verfahren zum Datenaustausch zwischen einer
Datenverarbeitungseinrichtung (MP) und einer an einer Busleitung eines bidirektionalen, seriellen und asynchronen Bussystems (K) bekannt. Zur Übertragung
von Datenpaketen begrenzter Länge ist eine Bussteuereinrichtung (S) angeschlossen. Die Datenverarbeitungseinrichtung weist im Empfangskanal Puffermittel (F2) zur abrufbaren Zwischenspeicherung einer Mehrzahl empfangener
Datenpakete auf. Die Bussteuereinrichtung generiert nach Empfang eines Datenpaketes ein Unterbrechungssignal und sendet dieses an die Datenverarbeitungs-

                                      - 6 -



einrichtung. Die Datenverarbeitungseinrichtung und die Bussteuereinrichtung sind
über einen Datenbus, einen Adreßbus und einen Steuersignalbus (zusammen in
B) miteinander verbunden. Das Unterbrechungssignal wird in Abhängigkeit von
der Anzahl der empfangenen Datenpakete generiert.


Nicht zu entnehmen ist der zweite Teil des letzten Merkmals, daß ein Unterbrechungssignal in Abhängigkeit der seit des letzten Datenpaketes verstrichenen Zeit
generiert wird.


Nach der genannten Aufgabe soll auch ein verzugsarmer Datendurchsatz realisiert werden (Beschreibung Seite 2, letzter Absatz und Seite 2a, Absatz 1). Diese
Aufgabe ergibt sich für den Fachmann zwingend, wenn auf dem in Rede stehenden System zeitkritische Abläufe realisiert werden sollen.


Zur Lösung dieser Teilaufgabe kann entweder der Füllstand, bei dem der Empfangspuffer ausgelesen wird, gesenkt werden, bis hin zu einem Datenpaket, wodurch jedoch die ursprüngliche, nachteilige Lösung wieder erreicht würde, oder
nach einem gerade noch akzeptablen Zeitraum der Pufferinhalt geleert werden.
Eine übliche Methode für die zweite Möglichkeit ist, einen Timer vorzusehen, der
einen Interrupt erzeugt, um den Puffer auszulesen, was nichts anderes heißt, als
daß das Unterbrechungssignal in Abhängigkeit von dem seit dem letzten Datenpaket verstrichenen Zeit generiert wird.


Der Patentanspruch 1 nach Hauptantrag ist somit nicht gewährbar.

                                      - 7 -



Hilfsantrag:


Der Patentanspruch 1 nach Hilfsantrag unterscheidet sich vom Patentanspruch 1
nach Hauptantrag nur durch die Form, er ist nämlich einteilig formuliert. Inhaltlich
stimmen die beiden Fassungen überein. Somit gelten die obigen Ausführungen
zum Hauptantrag auch für den Patentanspruch 1 nach Hilfsantrag. Dieser ist deshalb ebenfalls nicht gewährbar.


Mit den nicht gewährbaren Patentansprüchen 1 nach Haupt- bzw. Hilfsantrag fallen auch die auf sie rückbezogenen Patentansprüche 2 bis 5.




Grimm                         Bertl               Prasch                   Püschel


                                                                                prö
