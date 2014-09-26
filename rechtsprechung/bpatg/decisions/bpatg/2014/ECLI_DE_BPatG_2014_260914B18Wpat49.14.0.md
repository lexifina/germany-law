---
ecli: "ECLI:DE:BPatG:2014:260914B18Wpat49.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 49/14"
decided: "2014-09-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2014&Sort=1&Seite=55&nr=26692&anz=1119&pos=839&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2014-09-26_18_W-pat_49_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0042.md", "germany/bund/acts/patg/0045.md", "germany/bund/acts/patg/0046.md", "germany/bund/acts/patg/0048.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 18 W (pat) 49/14 vom 2014-09-26

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 49/14                                                       Verkündet am
_______________                                                      26. September 2014
    (Aktenzeichen)                                                             …




                              BESCHLUSS

                            In der Beschwerdesache


             betreffend die Patentanmeldung 11 2004 001 652.5-53




…




hat der 18. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. September 2014 durch die Vorsitzende
Richterin   Dipl.-Ing. Wickborn   sowie   die   Richterinnen   Hartlieb,   Dipl.-Phys.
Dr. Otten-Dünnweber und den Richter Dipl.-Ing. Altvater




BPatG 154
05.11

                                         -2-



beschlossen:


       1.      Auf die Beschwerde der Anmelderin wird der Beschluss der
               Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
               Markenamts vom 8. Juni 2009 aufgehoben und das Patent 11 2004 001 652 erteilt.


               Bezeichnung: „Vektorieren eines Interrupt oder einer Ausnahme bei Wiederaufnahme des Betriebs einer virtuellen
               Maschine“


               Anmeldetag: 15. September 2004


               Die Priorität der Anmeldung in den Vereinigten Staaten von
               Amerika (Az.: US 10/663,205) vom 15. September 2003 ist in
               Anspruch genommen.


               Der Erteilung liegen folgende Unterlagen zugrunde:

                  Patentansprüche 1 bis 9, überreicht in der mündlichen
                   Verhandlung vom 26. September 2014,

                  Beschreibung, Seiten 1 bis 12, 2a, überreicht in der
                   mündlichen Verhandlung vom 26. September 2014,

                  3 Blatt Zeichnungen: Figuren 1 bis 4, eingegangen am
                   9. März 2006.




       2.      Die Beschwerdegebühr wird zurückgezahlt.

                                         -3-



                                      Gründe


                                            I.


Die vorliegende Patentanmeldung 11 2004 001 652.5 geht hervor aus einer PCT-Anmeldung      (Veröffentlichungsnummer          WO 2005/029327 A1),      die    am
15. September 2004 unter Inanspruchnahme einer US-amerikanischen Priorität
vom 15. September 2003 eingereicht worden ist. Sie trägt in der deutschen Übersetzung die Bezeichnung


         „Vektorieren eines Interrupt oder einer Ausnahme bei Wiederaufnahme des Betriebes einer virtuellen Maschine“.


Die Anmeldung wurde durch die Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts mit Beschluss vom 8. Juni 2009 zurückgewiesen, weil
der Gegenstand des (damals geltenden) Anspruchs 1 im Hinblick auf die im Prüfungsverfahren ermittelte Druckschrift


             D2:     COFFING, C. L.: An x86 Protected Mode Virtual Machine
                     Monitor for the MIT Exokernel. Department of Electrical
                     Engineering      and    Computer   Science.     Massachusetts
                     Institute   of   Technology.    21. Mai 1999.    Seiten 63 – 75
                     <http://pdos.csail.mit.edu/papers/exo:coffing-meng.ps>
                     (recherchiert von der Prüfungsstelle am 4. August 2008)


unter Nichtberücksichtigung der gedanklich nicht nachvollziehbaren Merkmale
nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.

                                        -4-



Im Prüfungsverfahren war ferner die Druckschrift


               D1:   NANBA,     S.   u.a.:    VM/4:   ACOS-4     Virtual   Machine
                     Architecture. In: ACM SIGARCH Computer Architecture
                     News, Vol. 13, Iss. 3, Juni 1985, Seiten 171 – 178


eingeführt worden und auf die nachveröffentlichte Druckschrift


               D3:   Intel Virtualization Technology. Intel Technology Journal.
                     Vol. 10, Iss. 03, 10. August 2006


hingewiesen worden.


Mit Anlage zur Ladung vom 20. August 2014 hat der Senat zur Vorbereitung auf
die mündliche Verhandlung auf die in dem internationalen Recherchebericht aufgeführte Druckschrift


               F1:   WO 02/052404 A2


hingewiesen.


Die Beschwerdeführerin beantragt,


      den angegriffenen Beschluss vom 8. Juni 2009 aufzuheben und das Patent
      zu erteilen auf der Grundlage folgender Unterlagen:

      -        Patentansprüche 1 bis 9, eingereicht in der mündlichen Verhandlung,

      -        Beschreibung Seiten 1 bis 12, 2a, eingereicht in der mündlichen Verhandlung,

      -        Figuren 1 bis 4, eingegangen am 9. März 2006.

                                        -5-



Der seitens des Senats mit einer Gliederung versehene geltende Patentanspruch 1 lautet:


             „Verfahren zur Unterstützung eines Prozessors bei der Handhabung
             von Fehlern in der Umgebung einer virtuellen Maschine (VM) mit

     M1      einer Rechenplattform, die einen Monitor einer virtuellen Maschine
             (VMM) und eine oder mehrere virtuelle Maschinen (VM) repräsentierende Gast-Software ausführt, sowie

     M2      einer vom VMM separaten Fehlerübergabelogik des Prozessors,

     M3      wobei die Fehlerübergabelogik Folgendes ausführt:

     Ma      -     Erhalten (202) einer Anforderung von dem VMM für den Übergang der Kontrolle an eine virtuelle Maschine (VM);

     Mb      -     Zugreifen auf eine von dem VMM kontrollierte Steuerungsstruktur einer virtuellen Maschine (VMCS) zum Bestimmen eines
             momentanen Werts eines in der VMCS enthaltenen Fehlerindikators,
             wobei der momentane Wert des Fehlerindikators spezifiziert, ob der
             VMM eine Übergabe eines Fehlers an die VM angefordert hat;

     Mc      -     wenn der VMM die Übergabe des Fehlers an die VM angefordert hat, Übergeben (206) des Fehlers an die VM, wenn die Kontrolle
             an die VM übergeht, wobei die Fehlerübergabelogik den Fehler an
             die VM unter Verwendung von Fehleridentifizierungsinformationen
             liefert, die durch den VMM in der VMCS in Verbindung mit dem Fehlerindikator gespeichert sind;

     Md      -     Feststellen (208), ob die Übergabe des Fehlers an die VM
             erfolgreich war; und

     Me      -     wenn die Übergabe des Fehlers an die VM nicht erfolgreich
             war, Feststellen (210), ob ein resultierender zusätzlicher Fehler einen
             VM-Austritt verursacht, und

                                        -6-



     Mf      -      wenn der resultierende zusätzliche Fehler keinen VM-Austritt
             verursacht, Übergeben (214) des resultierenden zusätzlichen Fehlers
             an die VM und

     Mg      -      wenn der resultierende zusätzliche Fehler einen VM-Austritt
             verursacht, Generieren (212) eines VM-Austritts.“


Der geltende Patentanspruch 7 lautet:


             „Vorrichtung zur Handhabung von Fehlern, die zur Durchführung des
             Verfahrens nach einem der Ansprüche 1 bis 6 geeignet ist und Folgendes umfasst:

             -      einen Speicher (120) mit einer Datenstruktur, die durch einen
             VMM (112) kontrolliert wird, wobei die Datenstruktur einen Fehlerindikator und entsprechende Fehleridentifizierungsinformationen speichert; und

             -      einen mit dem Speicher gekoppelten Prozessor (118), wobei
             der Prozessor (118) eine vom VMM (112) separate Fehlerübergabelogik aufweist.“


Wegen der geltenden abhängigen Ansprüche 2 bis 6, 8 und 9 wird auf den Akteninhalt verwiesen.


Die Beschwerdeführerin macht hierzu geltend, dass die geänderte Anspruchsfassung zulässig sei und die Gegenstände der Ansprüche neu und erfinderisch seien.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                       -7-



                                        II.


Die frist- und formgerecht eingelegte und auch sonst zulässige Beschwerde hat
Erfolg. Denn der zweifelsfrei gewerblich anwendbare Gegenstand des nunmehr
geltenden Patentbegehrens ist gegenüber dem im Verfahren befindlichen Stand
der Technik neu und beruht auf einer erfinderischen Tätigkeit. Auch die weiteren
Voraussetzungen zur Patenterteilung sind erfüllt (PatG §§ 1 bis 5, § 34).




1.    Die Patentanmeldung betrifft virtuelle Maschinen und die Handhabung von
Fehlern in der Umgebung einer virtuellen Maschine (vgl. die deutsche Offenlegungsschrift der Anmeldung DE 11 2004 001 652 T5, Abs. [0001]).


Die Anmeldung geht von einem System aus, bei dem ein Monitor für virtuelle Maschinen (VMM) die Steuerung, d.h. den Zugriff auf die physikalischen Ressourcen,
an verschiedene virtuelle Maschinen (VM) überträgt. Zum Hintergrund wird angegeben, dass in der Umgebung einer virtuellen Maschine der Monitor einer virtuellen Maschine (VMM), der als Host für die Gastbetriebssysteme fungiere, die letztendliche Kontrolle über die Ereignisse und Hardware-Ressourcen haben solle, um
für einen korrekten Betrieb sorgen zu können. In der Regel erhalte der Monitor für
virtuelle Maschinen (VMM) die Kontrolle, wenn Gast-Software versuche, auf eine
geschützte Ressource zuzugreifen oder wenn sonstige Ereignisse wie Interrupts
oder Ausnahmen einträten. Wenn eine Operation in einer virtuellen Maschine eine
Systemvorrichtung veranlasse, einen Interrupt zu erzeugen, so werde die momentan laufende virtuelle Maschine unterbrochen und die Kontrolle gehe an den
VMM über, welcher den Interrupt entweder selbst handhabe oder an eine entsprechende virtuelle Maschine übergebe (vgl. Offenlegungsschrift, Abs. [0002] -
[0003]). In der Umgebung einer virtuellen Maschine umfasse die Plattformhardware eine Rechenplattform, die beispielsweise ein standardmäßiges Betriebssystem und einen Monitor für virtuelle Maschinen ausführen könne. Dabei enthalte die

                                        -8-



Plattform-Hardware einen Prozessor und einen Speicher (vgl. Offenlegungsschrift,
Abs. [0016] - [0018]).


Die der Anmeldung zugrunde liegende Aufgabe besteht darin, ein Verfahren zur
Unterstützung eines Prozessors bei der Handhabung von Fehlern in der Umgebung einer virtuellen Maschine mit einer Rechenplattform, die einen Monitor einer
virtuellen Maschine und eine oder mehrere virtuelle Maschinen repräsentierende
Gast-Software ausführt, bereitzustellen, mit dem einem Eintreten von zusätzlichen
Fehlern entgegengewirkt werden kann, sowie eine entsprechende Vorrichtung
(vgl. geltende Beschreibung, S. 2a, dr. Abs.).


Die Aufgabe soll gelöst werden durch ein Verfahren nach Anspruch 1 und eine
Vorrichtung nach Anspruch 7.




2.    Als Fachmann sieht der Senat vorliegend einen Ingenieur der Informationstechnik an, der mit der Programmierung der Prozessoransteuerung in einem
System mit virtuellen Maschinen vertraut ist.


Der so definierte Fachmann legt dem Anspruchsgegenstand das folgende Verständnis zugrunde:


Das beanspruchte Verfahren unterstützt einen Prozessor bei der Handhabung von
Fehlern in der Umgebung einer virtuellen Maschine. Unter den Begriff „Fehler“
fallen vorliegend Ereignisse wie interne oder externe Interrupts, Ausnahmen wie
Seitenfehler oder sonstige Fehlerereignisse (vgl. geltende Beschreibung, S. 9,
vierter Abs.). Die Umgebung der virtuellen Maschine besteht aus einer Rechenplattform, auf welcher der Monitor für virtuelle Maschinen und eine oder mehrere
virtuelle Maschinen repräsentierende Gast-Software ausgeführt wird (Merkmal
M1), sowie aus einer vom Monitor für virtuelle Maschinen separaten Logik, welche
die Fehlerübergabe ausführt (Merkmale M2, M3). Der Monitor für virtuelle Maschi-

                                       -9-



nen (VMM), der innerhalb oder auf einem anderen Monitor für virtuelle Maschinen
laufen und in Software, Firmware, Hardware oder durch eine Kombination verschiedener Techniken implementiert sein kann (vgl. geltende Beschreibung, S. 5,
zw. Abs.), hat die Kontrolle darüber, welche virtuelle Maschine Zugriff auf die physikalischen Ressourcen hat.
Die gemäß den Merkmalen Ma bis Mg von der Fehlerübergabelogik des Prozessors ausgeführten Verfahrensschritte sind entsprechend dem in Figur 4 der Anmeldung gezeigten Ablauf als im Wesentlichen zeitlich aufeinander folgend zu
verstehen. Das Verfahren beginnt mit dem Erhalten einer Anforderung vom Monitor für virtuelle Maschinen, die Kontrolle an die virtuelle Maschine (VM) zu übergeben, d.h. mit der Anfrage nach Übergang der Steuerung an eine virtuelle Maschine, was in der Anmeldung auch als „Einstieg“ einer virtuellen Maschine bezeichnet wird (vgl. geltende Beschreibung, S. 7, zw. Abs., Merkmal Ma). Den weiteren Verfahrensablauf beeinflusst der Monitor für virtuelle Maschinen nur insoweit, als er für eine virtuelle Maschine eine bspw. im Speicher gespeicherte Steuerungsstruktur (Virtual Machine Control Structure – VMCS) kontrolliert, in der über
den Wert eines Fehlerindikators festgelegt ist, ob der Monitor die Übergabe des
Fehlers an die virtuelle Maschine anfordert (Merkmal Mb). Wenn der Monitor die
Übergabe des Fehlers an die virtuelle Maschine angefordert hat, so übergibt die
Fehlerübergabelogik den Fehler an die virtuelle Maschine und überprüft anschließend, ob die Übergabe erfolgreich war (Merkmale Mc, Md). Wenn die Übergabe
des Fehlers nicht erfolgreich war, bedeutet dies, dass während des Einstiegs der
virtuellen Maschine ein weiterer Fehler aufgetreten ist, welcher in der Anmeldung
als resultierender zusätzlicher Fehler bezeichnet wird. Nur in dem Fall, dass es
sich bei diesem Fehler nicht um einen Fehler handelt, der zu einem Ausstieg der
virtuellen Maschine führt, übergibt die Fehlerübergabelogik den resultierenden
zusätzlichen Fehler an die virtuelle Maschine (vgl. Merkmale Me, Mf i.V.m. Fig. 2).
Andernfalls generiert die Fehlerübergabelogik den Austritt der virtuellen Maschine
(Merkmal Mg), was bedeutet, dass die Kontrolle an den Monitor für virtuelle Maschinen übergeht.

                                       - 10 -



Wesentlich für das beanspruchte Verfahren zur Unterstützung eines Prozessors
bei der Handhabung von Fehlern in der Umgebung einer virtuellen Maschine ist,
dass es von einer von dem Monitor für virtuelle Maschinen separaten Fehlerübergabelogik ausgeführt wird. Mit dem Verfahren wird verhindert, dass Fehler, die
beim Einstieg einer virtuellen Maschine auftreten, sich bei einem darauffolgenden
Einstieg der virtuellen Maschine wiederholen; solche Fehler werden vielmehr von
der Fehlerübergabelogik an den Monitor für virtuelle Maschinen übergeben. Davon
umfasst sind insbesondere Fehler, die aus Fehlern bei der Vorbereitung des Einstiegs der virtuellen Maschine resultieren (vgl. geltende Beschreibung, S. 8, letzter
Abs. – S. 9, erster Abs.).




3.     Der Erteilungsantrag liegt im Rahmen der ursprünglichen Offenbarung.


a)     Die Merkmale der geltenden Ansprüche sind durch die ursprünglichen Patentansprüche sowie die ursprünglich eingereichte Beschreibung mit den Figuren
1 bis 4 als zur Erfindung zugehörend offenbart: Der Anspruch 1 basiert auf den
ursprünglichen Ansprüchen 1 und 3 i.V.m. den Figuren 1 bis 4 und Seite 5, zweiter
Absatz, Seite 7, letzter Absatz bis Seite 8, erster Absatz, Seite 9, zweiter Absatz
bis Seite 10, zweiter Absatz, Seite 10, letzter Absatz, Zeile 13 bis 15 sowie Seite
11, vorletzter Absatz bis Seite 12, zweiter Absatz der ursprünglichen deutschsprachigen Anmeldeunterlagen. Der unabhängige Anspruch 7 basiert auf den ursprünglichen Ansprüchen 10 und 12 i.V.m. den vorgenannten, zu Anspruch 1
angegebenen Offenbarungsstellen. Die Unteransprüche 2, 4, 5, 6, 8 und 9 basieren auf den ursprünglichen Ansprüchen 2, 5, 6, 7, 15 und 16; der Unteranspruch 3
basiert auf dem ursprünglichen Anspruch 13 i.V.m. Seite 11, dritter Absatz der
ursprünglichen deutschsprachigen Anmeldunterlagen.
Die Patentansprüche sind somit zulässig.

                                      - 11 -



b)    Die Änderungen in der Beschreibung sind zulässig. Der relevante Stand der
Technik wurde in der Beschreibungseinleitung gewürdigt und die Beschreibung
wurde an das geltende Patentbegehren angepasst.




4.    Der Gegenstand des Anspruchs 1 ist neu gegenüber dem im Verfahren
befindlichen Stand der Technik und beruht auch auf einer erfinderischen Tätigkeit.


a)    Aus keiner der im Verfahren genannten Druckschriften ist ein Verfahren mit
sämtlichen in Anspruch 1 geforderten Merkmalen bekannt.


Druckschrift D1 offenbart ein Verfahren zur Unterstützung eines Prozessors bei
der Handhabung von Fehlern in der Umgebung einer virtuellen Maschine (vgl.
S. 172, Abs. 2.1 d), S. 174, Abs. 2.7: Exception handling on Virtual Machines),
wobei eine Rechenplattform einen Monitor einer virtuellen Maschine (VM/4 Control
Program) und mehrere virtuelle Maschinen (VM) ausführt (vgl. S. 172, li. Sp.,
vierter Abs.: integrated virtual machine system, Fig. 6: B: OS/VM, D: Control Program / Merkmal M1). Die eigentliche Übergabe der Prozesse nimmt dabei ein im
Prozessor als Hard- oder Firmware implementierter Dispatcher (integrated dispatcher) vor, welcher eine allgemeine Übergabelogik in einem Prozessor darstellt
(vgl. S. 173, Abs. 2.3 Virtual Machine Dispatching / teilweise Merkmal M2, ohne
dass die Übergabelogik mit der Übergabe von Fehlern befasst ist). Dabei ist auch
vorgesehen, dass diese Übergabelogik von dem Monitor für virtuelle Maschinen
eine Anforderung für den Übergang der Kontrolle an eine virtuelle Maschine erhält
(vgl. in Fig. 6: Control Program, start_VP, Virtual Process Dispatcher, OS/VM /
Merkmal Ma). Die Übergabelogik greift dabei auf eine von dem Monitor für virtuelle
Maschinen kontrollierte Steuerungsstruktur (virtual processor control block) zu,
wobei der Monitor für virtuelle Maschinen eine Nachricht generiert, welche bei der
Verarbeitung eines Fehlers – in Druckschrift D1 ist als Fehler eine Ausnahme
(exception) beschrieben – zum Einsatz kommt (vgl. S. 174, re. Sp., vorle. Abs.).
Die Angabe, dass der Fehler von dem Kontrollprogramm, d.h. dem Monitor für

                                       - 12 -



virtuelle Maschinen detektiert wird, bedeutet, dass der Monitor die Übergabe eines
Fehlers anfordert (Merkmal Mb). Da die Übergabelogik (dispatcher), wie zum
Merkmal Ma ausgeführt, die eigentliche Übergabe der Prozesse an die virtuelle
Maschine vornimmt, bedeutet die Überprüfung des in der Steuerungsstruktur
gesetzten Flags nichts anderes als die in Merkmal Mc gemachte Übergabe des
Fehlers (exception) mit Lieferung der Fehleridentifizierungsinformationen.


Aus Druckschrift D1 ist somit ein Verfahren mit den Merkmalen M1, Ma bis Mc
sowie teilweise Merkmal M2 bekannt. Der Druckschrift sind jedoch weder Angaben zu einer speziell bei der Handhabung von Fehlern in der Umgebung einer
virtuellen Maschine zum Einsatz kommenden Fehlerübergabelogik zu entnehmen,
noch gibt es Hinweise darauf, dass eine Übergabelogik feststellt, ob die Übergabe
eines Fehlers an eine virtuelle Maschine erfolgreich war oder nicht oder wie Fehler
zu behandeln sind, die einen Austritt einer virtuellen Maschine verursachen
(Merkmale Md bis Mg fehlen).


Druckschrift D2 beschreibt für eine Rechenplattform, die einen Monitor einer virtuellen Maschine (monitor) und eine oder mehrere virtuelle Maschinen (guest) ausführt, wie Interrupts und Ausnahmen virtualisiert werden können (vgl. S. 65 –
S. 70, erster Abs. / Merkmal M1). Dabei werden Registerwerte, welche die Übergabe eines Fehlers an die Gastsoftware betreffen, von dem Monitor geändert (vgl.
S. 72, vierter Abs.: To give an interrupt or exception to the guest, the monitor must
manipulate the guest’s stack and registers …), was als eine von dem Monitor für
virtuelle Maschinen kontrollierte Steuerungsstruktur angesehen werden kann
(teilweise Merkmal Mb). Die Druckschrift bezieht sich allein auf eine in Software
ausgestaltete Handhabung von Fehlern und gibt keinen Hinweis auf eine dem
Monitor für virtuelle Maschinen bei der Handhabung von Fehlern zur Seite gestellte Fehlerübergabelogik in einem Prozessor. Druckschrift D2 gibt an, dass sobald ein Fehler während der Ausführung einer virtuellen Maschine auftritt, die
Kontrolle an den Monitor für virtuelle Maschine zu übergeben ist (vgl. S. 67 ff., Abschnitt 8.3.1); diese Verfahrensweise ist im Hinblick auf die in den Merkmalen Md

                                       - 13 -



bis Mg definierten Abfragen vom beanspruchten Gegenstand wegführend, wonach
nur unter festgelegten Bedingungen ein resultierender zusätzlicher Fehler von der
virtuellen Maschine bearbeitet werden soll, und die Übergabe eines solchen Fehlers an die virtuelle Maschine erfolgt, ohne dass die Kontrolle an den Monitor für
virtuelle Maschinen übergeht.


Druckschrift F1 offenbart ein Verfahren zur Handhabung von Fehlern (interrupts,
exceptions) in der Umgebung einer virtuellen Maschine (guest software) mit einer
Rechenplattform, die einen Monitor für virtuelle Maschinen (VMM) und eine oder
mehrere virtuelle Maschinen (V32 mode) ausführt (vgl. Fig. 1 und 3 mit zugehöriger Beschreibung / Merkmal M1). Dabei legt der Monitor für virtuelle Maschinen in
einer Steuerungsstruktur (redirection map) fest, welche Fehler von der virtuellen
Maschine selbst und welche nur über den Monitor für virtuelle Maschinen bearbeitet werden dürfen (vgl. Fig. 7 mit zugehörigem Text S. 17, Z. 18 – S. 18, Z. 7).
Die Steuerungsstruktur wird von dem Prozessor konsultiert, um zu bestimmen, ob
der anhängige Prozessor-Modus verlassen werden soll (vgl. den dortigen Anspruch 24: … the processor is to consult a redirection bitmap to determine whether
to exit said processor mode …); der Prozessor weist somit eine Fehlerübergabelogik auf, welche separat vom Monitor für virtuelle Maschinen ist (vgl. den dortigen
Anspruch 15 / Merkmal M2). Dabei liest der Fachmann bei den in Druckschrift F1
offenbarten Verfahrensabläufen der Figuren 4, 6 und 7 mit, dass diese von der
Fehlerübergabelogik ausgeführt werden (Merkmal M3). Dies betrifft das Erhalten
einer Anforderung für den Übergang der Kontrolle an eine virtuelle Maschine, was
explizit beschrieben ist für den Einstieg einer virtuellen Maschine nach Bearbeitung eines Fehlers durch den Monitor für virtuelle Maschinen (vgl. Fig. 4,
Schritt 412 / Merkmal Ma), wie auch das Zugreifen auf die von dem Monitor kontrollierte Steuerungsstruktur zum Bestimmen eines momentanen Werts eines
Fehlerindikators (vgl. Fig. 7, Schritte 708 und 710 / Merkmal Mb). Druckschrift F1
beschreibt, dass wenn der Monitor für virtuelle Maschinen die Übergabe eines
Interrupts oder einer Ausnahme durch Festsetzen des in der Steuerungsstruktur
hinterlegten Wertes angefordert hat, dieser Fehler an das Gast-Betriebssystem,

                                         - 14 -



d.h. an die virtuelle Maschine übergeben wird (vgl. Fig. 7, Schritt 714 i.V.m. S. 17,
Z. 19 – S. 18, Z. 5); aus dem in Figur 7 dargestellten Ablauf ergibt sich für den
Fachmann, dass es vorrangig um Fehler geht, die auftreten, während die Kontrolle
bei der virtuellen Maschine liegt (vgl. Fig. 7, Schritt 712, der einen Austritt der virtuellen Maschine beschreibt, was impliziert, dass in den vorhergehenden Schritten
der Einstieg bereits erfolgt war), so dass das Merkmal Mc teilweise realisiert ist,
ohne die Angabe, dass die Übergabe des Fehlers erfolgt, wenn die Kontrolle an
die virtuelle Maschine übergeht. Druckschrift F1 zeigt somit zwar auf, dass bestimmte Fehler einen Ausstieg aus der virtuellen Maschine zur Folge haben sollen,
wenn dies durch den Monitor für virtuelle Maschinen – vorab – festgelegt worden
ist. Einen Hinweis darauf, bei während des Einstiegs einer virtuellen Maschine ggf.
auftretenden Fehlern, d.h. bei nicht erfolgreicher Übergabe eines Fehlers, von der
Fehlerübergabelogik überprüfen zu lassen, ob der resultierende zusätzliche Fehler
den Ausstieg der virtuellen Maschine verursacht, ist der Druckschrift jedoch nicht
zu entnehmen (Merkmale Md bis Mg fehlen). Der Fachmann erhält aus Druckschrift F1 somit keine Anhaltspunkte, zwischen dem Monitor für virtuelle Maschinen und einer davon separaten Fehlerübergabelogik des Prozessors eine Aufgabenteilung gemäß den Angaben des vorliegenden Anspruchs 1 vorzunehmen.


Druckschrift D3 ist als nachveröffentlichte Schrift für die Prüfung auf Neuheit und
erfinderische Tätigkeit irrelevant.


Weiterer relevanter Stand der Technik ist nicht bekannt geworden.


Der Gegenstand des Anspruchs ist daher neu.


b)     Der Gegenstand des Anspruchs 1 beruht auch auf einer erfinderischen
Tätigkeit.

                                       - 15 -



Wie in Abschnitt a) erläutert, ist keiner der im Verfahren befindlichen Schriften ein
Hinweis darauf zu entnehmen, von einer vom Monitor für virtuelle Maschinen separaten Fehlerübergabelogik überprüfen zu lassen, ob die Übergabe eines Fehlers an die virtuelle Maschine erfolgreich war oder nicht; ebenso machen die
Druckschriften keine Angaben, wie beim Einstieg einer virtuellen Maschine auftretende resultierende zusätzliche Fehler zu behandeln sind, die einen Austritt der
virtuellen Maschine verursachen.


Auch das allgemeine Fachwissen gibt dem Fachmann keine Anregungen, zur
Unterstützung eines Prozessors bei der Fehlerhandhabung in der Umgebung einer virtuellen Maschine durch eine Fehlerübergabelogik Verfahrensschritte gemäß
den Merkmalen Md bis Mg zu implementieren.


Selbst wenn die von der Fehlerübergabelogik auszuführenden Verfahrensschritte
Ma bis Mg softwareunterstützt implementiert sind, so stellen diese vorliegend
keine Datenverarbeitungsmaßnahmen dar, die außerhalb der Technik liegen und
bei der Beurteilung der erfinderischen Tätigkeit unberücksichtigt bleiben könnten
(BGH, Beschluss vom 20. Januar 2009 – X ZB 22/07, GRUR 2009, 479 – Steuerungseinrichtung     für    Untersuchungsmodalitäten;        BGH,     Urteil    vom
26. Oktober 2010 – X ZR 47/07, GRUR 2011, 125, Leitsatz b) – Wiedergabe topografischer Informationen; BGH, Urteil vom 18. Dezember 2012 – X ZR 3/12,
GRUR 2013, 275, Leitsatz a) – Routenplanung). Denn diesen Maßnahmen kommt
im vorliegenden Fall eine technische Bedeutung zu, da durch sie ein möglichst
ungestörter Betrieb der Datenverarbeitungsanlage auch bei Auftreten von Fehlern
während der Steuerung der Zugriffe auf die physikalischen Ressourcen durch den
Monitor für virtuelle Maschinen gewährleistet wird. Zudem sind auch Sicherheitsaspekte beim Betrieb der virtuellen Maschinen betroffen, da durch das beanspruchte Zusammenwirken der Fehlerübergabelogik des Prozessors mit dem
Monitor für virtuelle Maschinen im Verfahren sichergestellt wird, dass bestimmte
Fehlerereignisse von dem Monitor für virtuelle Maschinen gehandhabt werden
müssen (vgl. die Merkmale Mb und Mg).

                                      - 16 -



Das beanspruchte Verfahren geht somit über das übliche fachmännische Handeln,
ausgehend von den Lehren der betrachteten Druckschriften D1, D2 und F1 und
unter Einbeziehung des Fachwissens hinaus.


Der Gegenstand des Anspruchs 1 beruht somit auf einer erfinderischen Tätigkeit.




5.      Der Gegenstand des nebengeordneten Anspruchs 7 ist ebenfalls patentfähig.


Wie vorstehend zum Verfahren nach Anspruch 1 dargelegt, ist aus dem im Verfahren befindlichen Stand der Technik kein Verfahren zur Unterstützung eines Prozessors bei der Handhabung von Fehlern in der Umgebung einer virtuellen Maschine mit den Merkmalen M1 bis Mg bekannt. Da keine der Druckschriften D1,
D2 und F1 ein solches Verfahren vorsieht, ist auch eine auf ein solches Verfahren
rückbezogene Vorrichtung gemäß Anspruch 7 gegenüber dem im Verfahren befindlichen Stand der Technik neu. Wie zu Anspruch 1 ausgeführt, beruht das Verfahren auch auf einer erfinderischen Tätigkeit; daher ist auch der Gegenstand der
zur Ausführung eines solchen Verfahrens geeignet eingerichteten Vorrichtung zur
Handhabung von Fehlern dem Fachmann nicht nahegelegt.




6.     Die abhängigen Ansprüche 2 bis 6, 8 und 9 betreffen über das Selbstverständliche hinausgehende Ausgestaltungen des Verfahrens nach Anspruch 1
bzw. der Vorrichtung nach Anspruch 7. Die abhängigen Ansprüche sind daher
ebenfalls patentfähig.




7.      Die Lehre der Patentansprüche ist in der vorliegenden Fassung so deutlich
und vollständig offenbart, dass ein Fachmann sie ausführen kann. Da die vorgelegten geltenden Unterlagen auch den weiteren Anforderungen des § 34 PatG

                                       - 17 -



genügen und die Gegenstände der unabhängigen Ansprüche – wie vorstehend
gezeigt – auf einer erfinderischen Tätigkeit beruhen, war auf die Beschwerde des
Anmelders der Zurückweisungsbeschluss der Prüfungsstelle für Klasse G 06 F
des Deutschen Patent- und Markenamts aufzuheben und ein Patent gemäß Antrag zu erteilen.




                                         III.


Die Rückzahlung der Beschwerdegebühr war nach § 80 Abs. 3 PatG anzuordnen.


Nach dieser Vorschrift kann die Rückzahlung der Beschwerdegebühr angeordnet
werden, wenn dies der Billigkeit entspricht. Dies kommt insbesondere bei Verfahrensfehlern    oder   unsachgemäßer        Sachbehandlung   in   Betracht    (vgl.
Schulte/Püschel, PatG, 9. Aufl., § 80 Rdn. 111 - 113 und § 73 Rdn. 131 ff.;
Busse/Engels, PatG, 7. Aufl., § 80 Rdn. 90 ff.).


Im angefochtenen Beschluss liegen Verfahrensfehler vor (Schulte/Püschel, a.a.O.,
§ 73 Rdn. 142, 145, 154). Das rechtliche Gehör wurde verletzt, da die Prüfungsstelle eine von der Anmelderin im Schriftsatz vom 19. Januar 2009 hilfsweise beantragte Anhörung nicht durchgeführt hat sowie auf die mit Schriftsatz vom
19. Januar 2009 neu eingereichten Ansprüche erstmals im Beschluss eingeht.


1.     Die Ablehnung der von der Anmelderin beantragten Anhörung stellt einen
die Rückzahlung der Beschwerdegebühr rechtfertigenden Verfahrensverstoß dar.
§ 46 Abs. 1 Satz 2 PatG gibt in der bis zum 31. März 2014 geltenden Fassung vor,
dass der Anmelder bis zum Beschluss über die Erteilung auf Antrag zu hören ist,
wenn es sachdienlich ist. Sachdienlich ist eine Anhörung nach ständiger Rechtsprechung immer dann, wenn sie aus objektiver Sicht das Verfahren fördern kann,
insbesondere wenn sie eine schnellere und bessere Klärung als eine schriftliche
Auseinandersetzung verspricht (Schulte/Rudloff-Schäffer, PatG, 9. Aufl., § 46

                                      - 18 -



Rdn. 11 m.w.N.). Eine Ablehnung eines Antrags auf Anhörung kommt nur ausnahmsweise in Betracht, nämlich wenn triftige Gründe dafür vorliegen, etwa weil
die Anhörung zu einer überflüssigen Verfahrensverzögerung eines einfach gelagerten Verfahrens führen würde oder wenn nach mehreren Prüfungsbescheiden
absehbar ist, dass der Anmelder auch zukünftig keine Bereitschaft zur Anpassung
der Patentansprüche zeigt (Schulte/Rudloff-Schäffer, a.a.O., § 46 Rdn. 15).


Vorliegend hat die Prüfungsstelle den Beurteilungsspielraum bei der Einschätzung
der Erforderlichkeit der hilfsweise beantragten Anhörung überschritten. Zwar hatte
die Prüfungsstelle mit dem zweiten Prüfungsbescheid, der auf den 20. Mai 2008
datiert ist und am 17. Juni 2008 versandt wurde, zu einer Anhörung am
20. Juni 2008   geladen.   Ausweislich   einer   Eingabe   des   Anmelders    vom
18. Juni 2008 wurde in einem Telefonat zwischen Anmelderin und Prüfungsstelle
vereinbart, den Termin für die Anhörung auf den 4. August 2008 zu verschieben.
Mit Eingabe vom 30. Juli 2008 hat die Anmelderin neue Ansprüche eingereicht
und angekündigt, von einer Teilnahme an der Anhörung abzusehen, ferner wurde
um Entscheidung nach Aktenlage gebeten. Ausweislich der Amtsakte ist keine
Anhörung durchgeführt worden. Am 4. August 2008 erging ein weiterer Prüfungsbescheid, in dem u.a. bemängelt wurde, dass nicht zu erkennen sei, was mit dem
Anspruch 1 unter Schutz gestellt werden solle und in dem die Druckschrift D2 eingeführt wurde. Darauf reichte die Anmelderin mit Schriftsatz vom 19. Januar 2009
neue Ansprüche ein, mit denen den Beanstandungen hinsichtlich der Klarheit einzelner Anspruchsmerkmale Rechnung getragen werden sollte. Ferner nahm die
Anmelderin zu Druckschrift D2 Stellung und beantragte die Fortsetzung des Prüfungsverfahren sowie hilfsweise eine mündliche Anhörung. Darauf erfolgte die Zurückweisung der Anmeldung. In ihrem Beschluss vom 8. Juni 2009 lehnt die Prüfungsstelle die Anberaumung einer weiteren Anhörung als nicht sachdienlich ab,
„da aus dem Verlauf des Prüfungsverfahrens ersichtlich keine weitere Klärung der
sich gegenüberstehenden Ansichten zu erwarten gewesen“ wäre, ferner hätte die
Anmelderin im Verlauf des Prüfungsverfahrens hinreichend Gelegenheit zur Klärung des Sachverhalts gehabt.

                                      - 19 -



Die Durchführung der beantragten Anhörung hätte nur bei fehlender Sachdienlichkeit unterbleiben dürfen. Objektive Gründe, die die Ablehnung eines Antrags auf
Anhörung rechtfertigen könnten, sind nicht ersichtlich. Dass in der vorliegenden
Akte die Anmelderin in einem früheren Verfahrensstadium erklärt hatte, den Termin für eine Anhörung nicht wahrnehmen zu wollen, entzieht dem mit Schriftsatz
vom 19. Januar 2009 gestellten hilfsweisen Antrag auf Anhörung nicht die Grundlage. Die Anmelderin hat sich in der Eingabe vom 19. Januar 2009 bemüht, den
Beanstandungen der Prüfungsstelle durch Anpassung des Patentbegehrens
Rechnung zu tragen und auf die aus ihrer Sicht bestehenden Unterschiede zum
Stand der Technik hingewiesen. Es bestand daher keine Veranlassung davon
auszugehen, dass die Anmelderin in einer Anhörung nur auf ihrer bisherigen Position beharren würde. Der Zurückweisungsbeschluss bezieht sich als die erfinderische Tätigkeit in Frage stellenden Stand der Technik einzig auf Druckschrift D2,
welche erst in dem dem letzten Schriftsatz vorangehenden Prüfungsbescheid vom
4. August 2008 ins Verfahren eingeführt wurde. Dieser Verfahrensablauf kann die
Auffassung der Prüfungsstelle, die Anhörung sei nicht sachdienlich, nicht stützen.
Denn die Anmelderin durfte auf ihren Schriftsatz vom 19. Januar 2009, in dem zu
dieser Druckschrift Stellung genommen wird und mit dem sie ein neues Patentbegehren einreichte, vor einer endgültigen Zurückweisung noch mit einem weiteren
Hinweis der Prüfungsstelle rechnen. In der Ablehnung der mit Schriftsatz vom
19. Januar 2009 beantragten Anhörung ist daher bereits ein Verfahrensfehler zu
sehen, der die Rückzahlung der Beschwerdegebühr rechtfertigt (Busse, a.a.O.,
§ 80 Rdn. 102 und Schulte/Püschel, a.a.O., §73 Rdn. 154).




2.    Die Prüfungsstelle hat mit der Begründung ihres Zurückweisungsbeschlusses eine Verletzung des rechtlichen Gehörs der Anmelderin begangen. Der
Grundsatz der Gewährung rechtlichen Gehörs beinhaltet, dass sich der Einzelne
vor einer Entscheidung, die seine Rechte betrifft, zum Verfahren und seinem voraussichtlichen Ergebnis äußern kann. Damit darf eine Entscheidung nur auf
Gründen beruhen, zu denen sich der Beteiligte äußern konnte. Dies umfasst

                                            - 20 -



denknotwendig, dass sie ihm zuvor mitgeteilt werden müssen. Ausfluss dieses
Grundsatzes sind u.a. die Vorschriften der § 42 Abs. 3 Satz 2 PatG, § 45 Abs. 2
PatG und § 48 Satz 2 PatG (vgl. Schulte/Rudloff-Schäffer, a.a.O., § 48 Rdn 14 ff.).
Die Anmelderin konnte sich aber im vorliegenden Verfahren nicht zu den Gründen,
auf denen der Zurückweisungsbeschluss beruht, äußern.


Die Prüfungsstelle hat in ihrem Beschluss zu dem mit Schriftsatz vom
19. Januar 2009 neu eingereichten Anspruch 1 erstmals im Beschluss Stellung
genommen und damit ihre Entscheidung auf Umstände gestützt, die der Anmelderin   noch   nicht   mitgeteilt    waren.     Im     vorangegangenen   Bescheid   vom
4. August 2008 hatte die Prüfungsstelle zum einen bemängelt, der Gegenstand
des (damals geltenden) Anspruchs 1 lasse nicht erkennen, was als patentfähig
unter Schutz gestellt werden soll. Zum anderen lasse Anspruch 1 in einer Interpretation seines Gegenstands gegenüber Druckschrift D2 keine erfinderische Tätigkeit erkennen. Die Anmelderin hat daraufhin ihr Patentbegehren überarbeitet
und neue Ansprüche eingereicht, in denen insbesondere die die Fehlerübergabelogik betreffenden Merkmale umfassend umformuliert waren. Die Anmelderin
konnte daher davon ausgehen, ein wesentlich geändertes Anspruchsbegehren
vorgelegt zu haben. Die Prüfungsstelle hat die Anmeldung ohne Erlass eines
weiteren Bescheides zurückgewiesen. Zu den die Fehlerübergabelogik betreffenden, umformulierten Merkmalen führt sie im Beschluss aus, diese Merkmale seien
„in Bezug auf die Prüfung einer erfinderischen Tätigkeit nicht zu berücksichtigen,
da nur in seiner Wirkung gedanklich Nachvollziehbares auf ein Naheliegen des
Gedankens geprüft werden“ könne. Es kann dahinstehen, ob die Begründung
selbst inhaltlich vertretbar ist. Denn diese dem Zurückweisungsbeschluss zugrunde liegende Argumentation zu dem mit Schriftsatz vom 19. Januar 2009 eingereichten Anspruch 1 ist der Anmelderin erstmals im Beschluss mitgeteilt worden, was     ebenfalls die        Rückzahlung der Beschwerdegebühr rechtfertigt
(Busse/Engels, a.a.O., § 80 Rdn. 98 und Schulte/Püschel, a.a.O., § 73 Rdn 142,
145).

                                       - 21 -



                                         IV.

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




Wickborn                 Hartlieb      Dr. Otten-Dünnweber              Altvater


                                                                              Hu
