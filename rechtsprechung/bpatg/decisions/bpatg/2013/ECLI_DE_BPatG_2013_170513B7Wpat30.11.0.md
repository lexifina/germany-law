---
ecli: "ECLI:DE:BPatG:2013:170513B7Wpat30.11.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 30/11"
decided: "2013-05-17"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=29&nr=25047&anz=1167&pos=440&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-05-17_7_W-pat_30_11_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 7 W (pat) 30/11 vom 2013-05-17

## Entscheidung

BUNDESPATENTGERICHT


  7 W (pat) 30/11                                                 Verkündet am
_______________                                                   17. Mai 2013
    (Aktenzeichen)                                                      …




                            BESCHLUSS

                          In der Beschwerdesache


               betreffend die Patentanmeldung 102 92 364.7-53


…




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 17. Mai 2013 durch den Richter Dipl.-Phys. Dipl.-
Wirt.-Phys. Maile als Vorsitzenden sowie die Richter Schwarz, Dipl.-Phys. Dr.
Schwengelbeck und die Richterin Dipl.-Phys. Dr. Otten-Dünnweber




BPatG 154
05.11

                                       -2-



beschlossen:


                       Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                         I.


Die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts hat
mit Beschluss vom 6. Dezember 2006 die Patentanmeldung 102 92 364.7-53 mit
der Bezeichnung


        Sichere Maschinenplattform, die mit Betriebssystemen und anwendungsspezifischen Steuerprogrammen eine Schnittstelle bildet


zurückgewiesen, weil die Gegenstände des Anspruchs 1 nach Hauptantrag sowie
der Ansprüche 1 nach den Hilfsanträgen 1, 2 und 3, eingegangen jeweils am
21. November 2006, im Hinblick auf die im Prüfungsverfahren ermittelten Druckschriften


        D1: US 6 154 818 A und
        D5: SMITH, S. W., WEINGART, S.: Building a high-performance, programmable secure coprocessor. Computer Networks 31 (1999). Seite 831 - 860. Elsevier Science B.V.


nicht auf einer erfinderischen Tätigkeit des Fachmanns beruhen würden.


Die Anmelderin hat gegen die Zurückweisung ihrer Patentanmeldung mit Schriftsatz vom 22. Januar 2007 fristgerecht Beschwerde eingelegt, mit der sie die Erteilung des Patents mit den dem Zurückweisungsbeschluss zugrunde liegenden

                                         -3-



Patentansprüchen 1 bis 20 laut Hauptantrag, hilfsweise mit den Patentansprüchen
1 bis 19 laut Hilfsantrag 1 oder jeweils mit den Patentansprüchen 1 bis 18 laut
Hilfsantrag 2 und laut Hilfsantrag 3 sowie der Beschreibung und den Zeichnungen
laut Anmeldeunterlagen weiterverfolgt.


Der geltende, seitens des Senats mit einer Gliederung versehene Patentanspruch
1 nach Hauptantrag lautet:


     M1      „Computersystem, das ein Steuerprogramm (1506) hostmäßig ausführt, wobei das Steuerprogramm entweder ein Betriebssystem oder ein anwendungsspezifisches Steuerprogramm ist, wobei das Computersystem folgende Merkmale
             aufweist:
             eine Hardwareplattform (1508), die eine Anzahl von Ausführungsprivilegpegeln, nicht-privilegierten Anweisungen und
             nicht-privilegierten Registern und privilegierten Anweisungen
             und privilegierten Registern bereitstellt;


     M2      einen Satz aus Softwarediensten,


     M2.1    die durch das Steuerprogramm zum Ausführen von Operationen, die die privilegierten Anweisungen und/oder privilegierten Register oder beide verwenden, aufrufbar sind,


     M2.2    wobei die Softwaredienste vor der Ausführung authentifiziert
             werden,


     M2.3    auf einem Privilegpegel ausgeführt werden, der privilegierter
             als ein Privilegpegel ist, auf dem das Steuerprogramm ausgeführt wird und eines oder mehrere der privilegierten Anweisungen und privilegierten Register verwenden; und

                                          -4-



     M3      eine    Kombinierte-Hardware-und-Software-Sicherheitsplattform-Schnittstelle (1502), die direkten Zugriff des Steuerprogramms auf die privilegierten Anweisungen und privilegierten
             Register verhindert,


     M4      wobei die Sicherheitsplattform-Schnittstelle dem Steuerprogramm statt dessen Zugriff zu dem Satz von Softwarediensten und den nicht-privilegierten Anweisungen und nicht-privilegierten Registern bereitstellt;


     M5      ferner mit einem Sicherheitsplattform-Betriebskern (1504),
             der auf einem am meisten privilegierten Pegel ausgeführt
             wird,


     M6      und ausgebildet ist, um Aufrufe an die Softwaredienste vor
             dem Beginnen der Ausführung der Softwaredienste zu authentifizieren.“


Der geltende Patentanspruch 1 nach 1. Hilfsantrag unterscheidet sich von Anspruch 1 nach Hauptantrag durch das zusätzlich angefügte Merkmal


     M7      „wobei das Computersystem ferner einen sicheren Boot-Prozeß umfaßt, der in Hardware, Software, Firmware oder einer
             Kombination aus zwei oder mehreren von Hardware, Software und Firmware enthalten ist, der jede Firmware- und
             Softwareroutine, die ausgeführt wird, um das Computersystem bis zur Ausführung eines Betriebssystems zu initialisieren, authentifiziert und validiert.“


Der geltende Patentanspruch 1 nach 2. Hilfsantrag unterscheidet sich von Anspruch 1 nach 1. Hilfsantrag durch das weiter zusätzlich angefügte Merkmal

                                       -5-



     M8     „und bei dem der sichere Boot-Prozeß jede Software- und
            Firmwareroutine vor der Ausführung der Firmware- oder
            Softwareroutine einschließlich Betriebssystemsroutinen und
            Benutzeranwendungsprogrammen validiert.“

Der geltende Patentanspruch 1 nach 3. Hilfsantrag unterscheidet sich von Anspruch 1 nach 2. Hilfsantrag durch einen Einschub in Merkmal M7, das nunmehr
lautet (Änderungen gegenüber Merkmal M7 des 1. und 2. Hilfsantrags hervorgehoben):


     M7‘    „wobei das Computersystem ferner einen sicheren Boot-Prozeß umfaßt, der in Hardware, Software, Firmware oder einer
            Kombination aus zwei oder mehreren von Hardware, Software und Firmware enthalten ist, wobei die Hardware einen
            Nur-Lese-Speicher (1806), der mit digitalen Signaturen (1812
            - 1815) signierte Sätze von Firmwareanweisungen (1808 -
            1811) enthält und einen Prozessor (1802), der einen initialen
            Firmwarevalidierungsmechanismus (1804) enthält aufweist,
            und wobei der Boot-Prozeß ausgebildet ist, um die digitalen
            Signaturen der Sätze von Firmwareanweisungen zu validieren, so dass jede Firmware- und Softwareroutine, die ausgeführt wird, um das Computersystem bis zur Ausführung eines Betriebssystems zu initialisieren, authentifiziert und validiert ist;“


Wegen den nach Hauptantrag geltenden nebengeordneten Ansprüchen 10, 19
und 20 sowie den abhängigen Ansprüchen 2 bis 9 und 11 bis 18, den nach Hilfsantrag 1 geltenden nebengeordneten Ansprüchen 9, 18 und 19 sowie den abhängigen Ansprüchen 2 bis 8 und 10 bis 17 und den nach den Hilfsanträgen 2 und 3
geltenden jeweiligen nebengeordneten Ansprüchen 8, 17 und 18 sowie den abhängigen Ansprüchen 2 bis 7 und 9 bis 16 wird auf den Akteninhalt verwiesen.

                                        -6-



Neben den eingangs genannten Druckschriften lagen dem Prüfungsverfahren außerdem die folgenden Druckschriften zugrunde:

       D2: WHITAKER, A. et al.: Lightweight Virtual Machines for
             Distributed and Networked Applications; University of
             Washington Technical Report 02-02-01, Seite 1 - 14
             (http://denali.cs.washington-edu/pubs/index.html,         recherchiert am 21.04.05),
       D3: FORD, B. et al.: Microkernels Meet Recursive Virtual Machines; In: Proceedings of the second USENIX symposium on Operating systems design and implementation,
             Seattle, Washington, US, 1996, Seite 137 - 151,
       D4: WO 01 / 06 374 A2
       D6: Message authentication code, Wikipedia-Auszug vom
             03.02.2006


Zur Vorbereitung auf die mündliche Verhandlung hat der Senat die Beschwerdeführerin mit Schreiben vom 7. Mai 2013 auf die Druckschrift


       D7: US 5 948 097 A


als weiteren möglicherweise relevanten Stand der Technik aufmerksam gemacht.
Ferner wurde darauf hingewiesen, dass auch die Zulässigkeit des Anspruchs 1
nach Hauptantrag fraglich sei, insbesondere im Hinblick auf das Merkmal, dass
„die Softwaredienste vor der Ausführung authentifiziert werden“. Dies gelte ebenso
für den Anspruch 10 nach Hauptantrag, die Ansprüche 1 und 9 nach Hilfsantrag 1
sowie jeweils die Ansprüche 1 und 8 nach Hilfsantrag 2 und 3.


Die ordnungsgemäß geladene Anmelderin hat, wie mit Telefax vom 14. Mai 2013
angekündigt, an der mündlichen Verhandlung nicht teilgenommen.

                                      -7-



Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.



                                       II.


Die zulässige Beschwerde hat in der Sache keinen Erfolg. Denn nach dem Ergebnis der mündlichen Verhandlung sind die jeweiligen Ansprüche 1 nach Hauptantrag sowie nach den Hilfsanträgen 1 bis 3 nicht zulässig (§ 38 Satz 1 PatG). Es
kann somit dahingestellt bleiben, ob die Gegenstände der geltenden Ansprüche
nach Hauptantrag bzw. nach den drei Hilfsanträgen im Hinblick auf die §§ 1 bis 5
PatG patentfähig sind.


1) Die Patentanmeldung betrifft eine sichere Maschine und eine sichere Maschinenschnittstelle, die sichere Dienste für Betriebssysteme und anwendungsspezifische      Steuerprogramme          liefert   (vgl.   Offenlegungsschrift
   DE 102 92 364 T5, Abs. [0002]). Dabei wird eine kombinierte Hardware- und
   Software-Sicherheitsplattform verwendet, deren Hardwareplattform für Anweisungen und Register mehrere Privilegpegel aufweist und den Betriebssystemen und anwendungsspezifischen Steuerprogrammen die nicht-privilegierten Anweisungen und Register liefert. Ein Satz von aufrufbaren Softwarediensten liefert Sicherheitsplattformverwaltungsdienste für die Betriebssteuerung von Hardwareressourcen (vgl. Abs. [0020] der Offenlegungsschrift).


   Nach Angaben der Anmelderin werden Computersicherheitsprobleme im Stand
   der Technik erst nach der Herstellung neuer Computersysteme erkannt und es
   werde nachträglich versucht, Sicherheitsprobleme auszubessern (vgl. Abs.
   [0004] der Offenlegungsschrift). Bei vielen Computersystemen könnten die
   Steuerungen für die I/O-Vorrichtungen direkt auf den physischen Speicher zugreifen. Die anmeldungsgemäße Sicherheitsplattform (SP) dagegen erlaube
   keinen direkten Zugriff auf den physischen Speicher durch eine beliebige
   Nicht-SP-Routine oder durch eine externe Hardware (vgl. Abs. [0107] der Offenlegungsschrift).

                                      -8-



2) Die Gegenstände der geltenden Ansprüche 1 nach Hauptantrag bzw. nach
   den Hilfsanträgen 1 bis 3 gehen über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus. Denn in sämtlichen geltenden Anspruchsfassungen wird gemäß Merkmal M2.2 beansprucht, dass Softwaredienste vor der Ausführung authentifiziert werden. Dass Softwaredienste in
   der im Merkmal M2.2 aufgeführten allgemeinen Form vor der Ausführung authentifiziert werden, ist den ursprünglichen Unterlagen jedoch nicht zu entnehmen.


   So offenbaren die ursprünglichen Unterlagen (vgl. Seite 52, Zeile 22 der ursprünglichen Beschreibung) dem Fachmann – der vorliegend als ein Ingenieur
   auf dem Gebiet der Technischen Informatik mit Fachhochschulabschluss und
   mehrjähriger Erfahrung im Bereich der Computersteuerungen, zu definieren ist
   – lediglich, dass   „die SPK-Codebilder […] digital signiert [sind] und […] vor
   der Ausführung verifiziert [werden].“. Mit SPK wird in der vorliegenden Anmeldung jedoch der Sicherheitsplattform-Betriebskern bezeichnet (vgl. Seite 47,
   Zeile 28 der ursprünglichen Beschreibung), was aber nicht gleichbedeutend
   mit den im Merkmal M2.2 in verallgemeinerter Form aufgeführten Softwarediensten ist, welche gemäß dem vorherigen Merkmal M2.1 des Anspruchs 1
   durch das Steuerprogramm zum Ausführen von Operationen, die die privilegierten Anweisungen bzw. privilegierten Register oder beide verwenden, aufrufbar sind.


   Auch die übrigen ursprünglich eingereichten Unterlagen geben keinen Hinweis
   darauf, dass Softwaredienste, die durch das Steuerprogramm zum Ausführen
   von Operationen, die die privilegierten Anweisungen bzw. privilegierten Register oder beide verwenden, aufrufbar sind, vor der Ausführung authentifiziert
   werden. Zwar wird in der vorliegenden Anmeldung im ursprünglichen Anspruch 10 ein Zusammenhang einer Authentifizierung mit dem Begriff Softwaredienst hergestellt, insofern als dass „der Sicherheitsplattform-Betriebskern Aufrufe an die Softwaredienste vor dem Beginnen der Ausführung der

                                       -9-



   Softwaredienste authentifiziert“. Dieses Merkmal, das sich im geltenden Anspruch 1 als Merkmal M6 wiederfindet, betrifft aber nicht die Authentifizierung
   der Softwaredienste selbst, sondern die Authentifizierung der Aufrufe an die
   Softwaredienste, das heißt der Feststellung, ob das Steuerprogramm zu dem
   Aufruf an den Softwaredienst berechtigt ist.


   Eine allgemeine Authentifizierung von Softwarediensten vor deren Ausführung
   ist somit den ursprünglichen Anmeldeunterlagen nicht als zur Erfindung gehörend zu entnehmen. Der Fachmann muss in diesem Zusammenhang eine
   weitergehende Erkenntnis, zu der er möglicherweise aufgrund seines allgemeinen Fachwissens gelangen kann, dem ursprünglichen Inhalt der Gesamtheit der ursprünglichen Unterlagen hinzufügen.


   Somit liegt vorstehend sowohl beim Gegenstand des Anspruchs 1 nach
   Hauptantrag wie auch bei den entsprechenden Gegenständen der Ansprüche 1 nach den drei Hilfsanträgen mit dem nachträglich aufgenommenen
   Merkmal, dass „die Softwaredienste vor der Ausführung authentifiziert werden“, eine unzulässige Erweiterung der Ursprungsoffenbarung vor. Die entsprechenden Ansprüche 1 nach Hauptantrag bzw. nach den drei Hilfsanträgen
   sind daher nicht zulässig.




3) Mit den jeweils nicht zulässigen Ansprüchen 1 nach Hauptantrag und der
   Hilfsanträgen 1 bis 3 sind auch die nebengeordneten Ansprüche 10, 19 und
   20 nach Hauptantrag, die nebengeordneten Ansprüche 9, 18 und 19 nach
   Hilfsantrag 1 und die nebengeordneten jeweiligen Ansprüche 8, 17 und 18
   nach den Hilfsanträgen 2 und 3 sowie die auf diese Ansprüche direkt oder
   indirekt rückbezogenen Unteransprüche nicht schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet war (vgl. BGH, GRUR
   2007, 862 Leitsatz – „Informationsübermittlungsverfahren II“).

                                   - 10 -



4) Bei dieser Sachlage war die Beschwerde zurückzuweisen.




Maile          Schwarz          Dr. Schwengelbeck     Dr. Otten-Dünnweber


                                                                       Hu
