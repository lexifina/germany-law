---
ecli: "ECLI:DE:BPatG:2013:190613B7Wpat57.11.0"
court: "Bundespatentgericht"
spruchkoerper: "7"
aktenzeichen: "7 W (pat) 57/11"
decided: "2013-06-19"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2013&Sort=1&Seite=36&nr=25337&anz=1167&pos=541&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2013-06-19_7_W-pat_57_11_NA_0.txt"
---

# Bundespatentgericht, 7 W (pat) 57/11 vom 2013-06-19

## Entscheidung

BUNDESPATENTGERICHT


  7 W (pat) 57/11                                                  Verkündet am
_______________                                                    19. Juni 2013
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 11 2004 001 564.2-53


…




hat der 7. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 19. Juni 2013 durch den Richter Dipl.-Phys. Dipl.-
Wirt.-Phys. Maile als Vorsitzenden und die Richter Schwarz, Dipl.-Phys. Dr. rer.
nat. Schwengelbeck und Dipl.-Ing. Altvater


beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                         I.


Die am 3. September 2004 als PCT-Anmeldung PCT/US2004/029276 eingereichte Patentanmeldung 11 2004 001 564.2-53 mit der Bezeichnung


                               „Low-contention Lock“


nimmt die Priorität der US-Anmeldung 10/658,626 vom 8. September 2003 in Anspruch   und    wurde    als   WO 2005/026948 A2       in   englischer   und    als
DE 11 2004 001 564 T5 in deutscher Sprache veröffentlicht.


Die Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts hat
die Anmeldung mit Beschluss vom 20. Juni 2008 mit der Begründung zurückgewiesen, der damals geltende Patentanspruch 1 in der Fassung vom 16. April 2008
lasse nicht erkennen, was als patentfähig unter Schutz gestellt werden solle.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


In der Beschwerdebegründung vom 19. August 2008 verteidigt die Anmelderin
ihre Patentanmeldung mit neuen geltenden Ansprüchen 1 bis 9. Sie führt aus,
dass geltende Anspruchsfassung - ohne inhaltliche Änderung - schärfer gefasst
sei als die, die dem Prüfungsverfahren zugrunde gelegen habe.

Der vom Senat mit einer Gliederung versehene, geltende Patentanspruch 1 lautet
(Änderungen gegenüber dem ursprünglich eingereichten Anspruch 1 hervorgehoben):


(M1) „Ein Verfahren zum Verwalten eines von einem Thread benutzen Locks,
        das folgendes umfasst von einer Mehrzahl von auf einem Rechner ausgeführten Threads zum Koordinieren des Zugangs zu einer geteilten Ressource genutzt wird, mit den folgenden Schritten:


(M2) Auswählen (110) einer an dem Lock auszuführenden Aktion durch einen
        der Threads, um auf das Lock einzuwirken wobei die Aktion ausgewählt
        wird ist aus einer Gruppe die umfasst bestehend aus:
        -     Erwerben des Locks,
        -     Versuchen des Erwerbens des Locks und
        -     Freigeben des Locks,


(M3) asynchrones Abfragen (120) des aktuellen Zustands Status des Locks
        durch den Thread das einen Mehrwertzustand aufweist,


(M4) spekulatives Bestimmen (130) des nächsten Zustands Status des Locks
        durch den Thread basierend auf dem abgefragten aktuellen Status und der
        ausgewählten Aktion,


(M5) Versuchen (140) durch den Thread, das Lock vom abgefragten aktuellen
        Zustand Status in den spekulativ bestimmten nächsten Zustand Status
        übergehen zu lassen, und


(M6) Zugreifen, Nicht-Zugreifen oder Freigeben auf die bzw. der geteilten Ressource durch den Thread basierend wenigstens zum Teil auf dem Ergebnis
        des Versuchs den Lockstatus übergehen zu lassen,

(M7) wobei die vier möglichen Status sind
       -    der Lock wird nicht gehalten und kein Thread wartet auf den Zugang zu
            der der geteilten Ressource,
       -    der Lock wird gehalten und kein Thread wartet auf den Zugang zu der
            geteilten Ressource,
       -    der Lock wird gehalten und ein Thread wartet auf den Zugang zu der der
            geteilten Ressource,
       -    der Lock wird gehalten und wenigstens zwei Threads warten auf den
            Zugang zu der der geteilten Ressource.“


Wegen des Wortlauts des geltenden nebengeordneten Anspruchs 8 und der jeweiligen geltenden Unteransprüche 2 bis 7 und 9 wird auf den Akteninhalt verwiesen.


Die Anmelderin hat mit der Beschwerdebegründung vom 19. August 2008 sinngemäß beantragt,


           den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamtes vom 20. Juni 2008 aufzuheben
           und ein Patent mit Patentansprüchen 1 bis 9 in der geltenden Fassung vom 19. August 2008 zu erteilen.


Der Senat hat die Anmelderin von der mündlichen Verhandlung u.a. darauf hingewiesen, dass der geltende Anspruch 1 möglicherweise Merkmale aufweist, die den
Gegenstand der Anmeldung unzulässig erweitern.


Zu der mündlichen Verhandlung am 19. Juni 2013 ist die ordnungsgemäß geladene Anmelderin entsprechend vorheriger Ankündigung nicht erschienen


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                      II.


Die zulässige Beschwerde führt nach dem Ergebnis der mündlichen Verhandlung
nicht zum Erfolg, da der geltende Anspruch 1 wenigstens ein Merkmal aufweist,
das den Gegenstand der Anmeldung unzulässig erweitert. Die Frage der Neuheit
oder erfinderischen Tätigkeit der Gegenstände der geänderten geltenden Patentansprüche kann daher dahinstehen (vgl. BGH GRUR 1991, 120, 121 li. Sp.
Abs. 3 - „Elastische Bandage“).


1.
Die Anmeldung betrifft das Erwerben und Freigeben einer geteilten Ressource
über ein Lock-Semaphor, das eine Zustandsmaschine benutzt. Typischerweise
erlauben es Prozess- oder Computersysteme mehrere Programme im Wesentlichen simultan auszuführen, indem sie Techniken wie z.B. Zeitscheibentechnik,
Parallelausführung oder Multiprozessormaschinen benutzen. Außerdem ist es
möglich, mehrere Teile eines Programms oder Threads in nahezu derselben
Weise simultan auszuführen. Techniken, die eine solche im Wesentlichen simultane Ausführung ermöglichen, werden als Multitasking, Multithreading oder Hyper-Threading bezeichnet. Diese Threads, Prozesse oder Programme greifen oft auf
gemeinsame Ressourcen zurück. Es sind eine Reihe von Techniken bekannt, um
Fehler oder unerwünschte Auswirkungen zu verhindern, die auftreten können,
wenn mehrere Threads versuchen, simultan eine gemeinsam genutzte, geteilte
Ressource zu benutzen. So kann der Zugriff auf eine geteilte Ressource von einem Semaphor-Lock gesteuert sein, das anderen potentiellen Nutzern anzeigt,
dass diese Ressource gerade benutzt wird. Durch das Lock wird außerdem der
Zugriff durch mehr als einen Nutzer verhindert. Bei modernen Systemen ist die
Summe der Anzahl von Locks, Threads und von Lock-Anforderungen oft recht
groß und häufige Speicherzuweisungen und -freigaben können eine große Menge
an Prozesszeit und anderen Systemressourcen verbrauchen (vgl. Offenlegungsschrift, Abs. [0002]-[0006]).

Der Anmeldung liegt daher die Aufgabe zugrunde, ein verbessertes System zum
Durchführen des Erwerbens und Freigebens von geteilten Ressourcen über ein
Lock-Semaphore zu schaffen.


Diese Aufgabe soll durch die Merkmale des geltenden Anspruchs 1 gelöst werden.


2.
Der geltende Anspruch 1 geht in seinen Merkmalen über die ursprüngliche Offenbarung in den Anmeldungsunterlagen hinaus.


Gemäß Merkmal M6 des geltenden Anspruchs 1 soll durch den Thread ein Zugreifen bzw. Nicht-Zugreifen auf die geteilte Ressource, basierend wenigstens
zum Teil auf dem Ergebnis des Versuchs den Lockstatus übergehen zu lassen,
erfolgen. Ein solcher Verfahrensschritt ist den ursprünglichen Anmeldungsunterlagen jedoch nicht zu entnehmen. Gemäß der ursprünglichen Offenbarung der Anmeldungsunterlagen folgt aus einem erfolgreichen Versuch, den Lockstatus übergehen zu lassen, vielmehr nur, dass ein Erwerb des Locks bzw. dessen Freigabe
erfolgt (vgl. Offenlegungsschrift, Fig. 2 und Abs. [0027] - [0030]). Ein – wie vorliegend im geltenden Anspruch 1 aufgeführtes – Zugreifen bzw. Nicht-Zugreifen
durch den Thread auf die geteilte Ressource, basierend wenigstens zum Teil auf
dem Ergebnis des Versuchs, den Lockstatus übergehen zu lassen, ist somit den
ursprünglichen Anmeldeunterlagen nicht unmittelbar und eindeutig zu entnehmen.
Der Fachmann – vorliegend ein Diplom-Informatiker mit Fachhochschulausbildung
und mehrjähriger Berufserfahrung auf dem Gebiet der Multitasking- sowie Multithreading-Systeme – muss in diesem Zusammenhang vielmehr eine weitergehende
Erkenntnis, zu der er möglicherweise aufgrund seines allgemeinen Fachwissens
gelangen kann, dem ursprünglichen Inhalt der Gesamtheit der ursprünglichen
Unterlagen hinzufügen. Dies begründet jedoch den Tatbestand einer unzulässigen
Erweiterung (vgl. BGH GRUR 2010, 509 „Hubgliedertor I“ und BGH GRUR 2010,
910 „Fälschungssicheres Dokument“).

Insofern liegt vorstehend beim Gegenstand des Anspruchs 1 eine unzulässige Erweiterung der Ursprungsoffenbarung vor. Der Patentanspruch 1 des geltenden
Anspruchssatzes ist daher nicht zulässig.


3.
Mit dem nicht zulässigen Anspruch 1 sind auch jeweils die weiteren Ansprüche 2
bis 9 nicht schutzfähig, da auf diese Ansprüche kein eigenständiges Patentbegehren gerichtet ist (vgl. BGH GRUR 2007, 862, Leitsatz – „Informationsübermittlungsverfahren II“).


4.
Nachdem der geltende Anspruchssatz nicht schutzfähig ist, war die Beschwerde
zurückzuweisen.




Maile              Schwarz          Dr. Schwengelbeck                  Altvater


                              Zugleich für Herrn Ri. Maile,
                              der an das DPMA abgeordnet
                              ist.

                                                                             Hu
