---
ecli: "ECLI:DE:BPatG:2006:051006B17Wpat82.04.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 82/04"
decided: "2006-10-05"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2006&Sort=1&Seite=82&nr=1729&anz=1665&pos=1244&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2006-10-05_17_W-pat_82_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 17 W (pat) 82/04 vom 2006-10-05

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 82/04                                                Verkündet am
 _______________                                                5. Oktober 2006
    (Aktenzeichen)                                                     …




                           BESCHLUSS

                          In der Beschwerdesache


               betreffend die Patentanmeldung 100 56 046.6-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 5. Oktober 2006 unter Mitwirkung …




BPatG 154
08.05

                                        -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.


                                   Gründe


                                         I.


Die vorliegende Patentanmeldung ist am 11. November 2000 beim Deutschen Patent- und Markenamt eingereicht worden unter der Bezeichnung:


         „Verfahren zur Realisierung einer lntertask-Kommunikation in einem Multitasking-Betriebssystem“.


Sie wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts vom 21. Juni 2004 mit der Begründung zurückgewiesen,
die Erfindung sei in der Anmeldung nicht so deutlich und vollständig offenbart,
dass ein Fachmann sie ausführen könne (§ 34 Absatz 4 PatG). Dies gelte für den
Hauptantrag und mutatis mutandis für jeden der Hilfsanträge.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie stellt
den Antrag,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       gemäß Hauptantrag mit Patentansprüchen 1 - 9 vom 30. Oktober 2003,    eingegangen    am     3. November 2003,    noch   anzupassender     Beschreibung     und   6 Blatt   Zeichnungen    mit
       9 Figuren, jeweils vom Anmeldetag,

                                       -3-



        gemäß Hilfsantrag 1 mit Patentansprüchen 1 - 9,
        gemäß Hilfsantrag 2 mit Patentansprüchen 1 - 8,
        gemäß Hilfsantrag 3 mit Patentansprüchen 1 - 8,
        gemäß Hilfsantrag 4 mit Patentansprüchen 1 - 8,
        gemäß Hilfsantrag 5 mit Patentansprüchen 1 - 8,
        gemäß Hilfsantrag 6 mit Patentansprüchen 1 - 8,
        gemäß Hilfsantrag 7 mit Patentansprüchen 1 - 7,
        gemäß Hilfsantrag 8 mit Patentansprüchen 1 - 6,
        gemäß Hilfsantrag 9 mit Patentansprüchen 1 - 5,
        jeweils vom 30. Oktober 2003, eingegangen am 3. November 2003, jeweils auch mit noch anzupassender Beschreibung und
        sonstigen Unterlagen wie Hauptantrag.


Der Anspruch 1 gemäß Hauptantrag, hier zusätzlich mit einer denkbaren Gliederung versehen, lautet:


        „a) Verfahren zur Realisierung einer Intertask-Kommunikation in
           einem Multitasking-Betriebssystem, das die Ausführung eines
           Computerprogramms steuert, das in mehrere Tasks mit jeweils
           mindestens einem Prozess unterteilt ist,


        b) wobei alle in dem Computerprogramm benutzten Variablen ermittelt (12) werden


        gekennzeichnet durch die nachfolgenden Verfahrensschritte:


        c) für jede Variable automatisches Ermitteln der Tasks, in denen
           auf die Variable zugegriffen wird und automatisches Ermitteln (13) der Variablen (Intertask-Variablen), die in mehreren
           Tasks benutzt werden;

                                       -4-



        d) für jede Intertask-Variable zur Sicherung der Datenkonsistenz
           der Intertask-Variablen automatisches Ermitteln (15) von möglichen anwendbaren Mechanismen für eine Intertask-Kommunikation aus zur Verfügung stehenden Mechanismen;


        e) für die Intertask-Variablen, für die mehrere Mechanismen anwendbar sind, Auswahl (20) eines Mechanismus für eine Intertask-Kommunikation aus den möglichen anwendbaren Mechanismen; und


        f) in Abhängigkeit von dem möglichen anwendbaren Mechanismus oder dem ausgewählten Mechanismus automatisches Einfügen (23) von Maßnahmen in die Tasks für einen Datenaustausch in dem Computerprogramm.“


Bezüglich der Unteransprüche 2 – 9 wird auf die Akte verwiesen.


Die Patentansprüche gemäß den Hilfsanträgen 1 – 9 können ebenfalls in der Akte
(Patentamts-Akte Blatt 80 - 115) eingesehen werden.


Diesen Ansprüchen soll (siehe Offenlegungsschrift Absatz [0010]) die Aufgabe
zugrundeliegen, ein Verfahren zur Realisierung einer Intertask-Kommunikation
dahingehend auszugestalten und weiterzubilden, dass das Verfahren eine möglichst hohe Flexibilität und die Intertask-Kommunikation eine möglichst alle Anforderungen abdeckende Funktionalität aufweist.


Wie die Anmelderin näher erläuterte, betrifft die Anmeldung Computerprogramme
für Multitasking-Betriebssysteme, bei denen verschiedene Teilaufgaben (tasks)
quasi gleichzeitig ausgeführt werden; üblicherweise würden diese Tasks ereignisgesteuert gestartet, so dass zum Startzeitpunkt der Status der übrigen Tasks für
den Programmierer nicht sicher vorhersehbar sei. Probleme könnten entstehen,

                                        -5-



wenn ein Programm so geschrieben sei, dass verschiedene Tasks auf dieselbe
definierte Variable zugriffen. So könne z. B. eine erste Task den Wert einer Variablen festsetzen, eine zweite diesen Wert mehrfach benutzen; dann müsse sichergestellt werden, dass sich der Wert während des Ablaufs der zweiten Task nicht
ändere.


Diejenigen Variablen, die in mehr als einer Task benutzt werden, seien in der vorliegenden Anmeldung als „Intertask-Variable“ bezeichnet. Die Eigenschaft, dass
sich der Wert solcher Variablen nicht zum falschen Zeitpunkt ändert, dass aber
andererseits jederzeit und überall der gleiche „richtige“ Wert zur Verfügung steht,
werde „Datenkonsistenz“ genannt.


Das vorgeschlagene Verfahren zur Realisierung einer Intertask-Kommunikation
entlaste nun den Programmierer dadurch, dass dieser die Intertask-Variablen nicht
besonders als solche zu definieren und sich um deren Datenkonsistenz nicht weiter zu kümmern brauche. Diese Arbeit übernehme das erfindungsgemäße Verfahren, indem es auf die „Rohfassung“ eines geschriebenen Programmes angewendet werde: es ermittle dann automatisch die Intertask-Variablen und erlaube – abhängig z. B. von der Priorität der jeweiligen Task –, für jeden Fall einen geeigneten
anwendbaren Mechanismus der Intertask-Kommunikation (etwa aus einer vorgegebenen Liste möglicher Mechanismen) auszuwählen; um diesen Mechanismus
zu implementieren, füge es jeweils geeignete Programmteile in das Programm ein.


Der Senat hat in der mündlichen Verhandlung auf die neuere BGH-Rechtsprechung hingewiesen und die Frage aufgeworfen, ob hier ein „konkretes technisches
Problem“ mit „technischen Mitteln“ gelöst werde. Insoweit verwies die Anmelderin
auf ihren Beschwerde-Schriftsatz. Demnach dient der Anmeldungsgegenstand der
Lösung des technischen Problems, ein multitaskingfähiges Computerprogramm
derart zu erstellen, dass einerseits für eine Intertask-Kommunikation eine möglichst alle Anforderungen abdeckende Flexibilität erzielt wird und andererseits
diese Intertask-Kommunikation für möglichst viele unterschiedliche Computerpro-

                                       -6-



gramme, die (wie mündlich erläutert) insbesondere auch auf unterschiedlichen
Prozessoren lauffähig sind, erzeugt werden kann. Dadurch werde eine schnellere
und Ressourcen sparende Abarbeitung von multitaskingfähigen Computerprogrammen ermöglicht.


                                         II.


Die Beschwerde ist frist- und formgerecht eingelegt und auch sonst zulässig. Sie
ist jedoch nicht begründet, denn das Verfahren gemäß Patentanspruch 1 des
Hauptantrags wie auch der Hilfsanträge 1 bis 9 unterliegt als „Programm als solches“ dem Patentierungsausschluss nach § 1 Abs. 3 Nr. 3 und 4 PatG.


1.     Zum Hauptantrag:
1.1    Die Anmeldung betrifft Computerprogramme für Multitasking-Betriebssysteme. Das beanspruchte Verfahren soll den Programmierer entlasten, indem es die
„Rohfassung“ eines neuen Programms durchsucht – beispielsweise in Form eines
Parsers, der die Quelldateien des Programms auswertet, siehe Offenlegungsschrift Absatz [0057] – und darin automatisch die Variablen ermittelt, die in mehreren Tasks verwendet werden, um deren Datenkonsistenz durch Einfügen geeigneter Programmteile sicherzustellen.


Als Fachmann, an den sich eine solche Lehre richtet, sieht der Senat einen Informatiker oder Systemprogrammierer mit mehrjähriger Erfahrung in der Programmierung von Anwendungen für Multitasking-Betriebssysteme an.


1.2    Die Patentansprüche 1 – 9 nach Hauptantrag sind zulässig. Sie weisen gegenüber den ursprünglichen Patentansprüchen geringfügige Klarstellungen und
Ergänzungen auf, die den Rahmen der ursprünglichen Offenbarung nicht verlassen.

                                       -7-



1.3   Der Zurückweisungsbeschluss der Prüfungsstelle ist im Wesentlichen damit
begründet worden, dass der Fachmann der Anmeldung nicht entnehmen könne,
wie ein Computerprogramm automatisch so verarbeitet werden kann, dass die von
ihm erzeugten Tasks den benutzten Variablen zugeordnet werden könnten. Die für
betriebssystemnahe Programmierung üblichen Programmiersprachen C oder C++
unterstützten keine Sprachmittel für Tasks und Prozesse eines Multitasking-Betriebssystems. Zwar ließen sich mit diesen Sprachen Tasks oder Prozesse erzeugen, jedoch nicht in einer durch die Grammatik der Sprache vorgegebenen Form,
die automatisch erkennbar und verarbeitbar wäre.


Diese Argumentation vermag nicht zu überzeugen; denn die Lehre der Anmeldung
ist in keiner Weise auf die Verwendung der Sprachen C oder C++ ausgerichtet.
Vielmehr erwartet die Anmeldung, dass die einzelnen Tasks (mit den jeweils verwendeten Variablen) separat programmiert vorliegen. Welche Programmiersprache dafür geeignet sein könnte, ist nicht Gegenstand der Anmeldung, eine solche
zu finden stellt an den Fachmann auch keine überzogenen Anforderungen (vgl.
die Beispiele in der Beschwerde-Begründung vom 1. Oktober 2004, Seite 6
Abs. 2).


Insoweit greift der geltend gemachte Zurückweisungsgrund nicht.


1.4   Das Verfahren bzw. Computerprogramm nach dem Patentanspruch 1 gemäß Hauptantrag kann jedoch nicht als eine schutzwürdige Bereicherung der
Technik angesehen werden, da weder ein konkretes technisches Problem vorliegt
noch technische Mittel zur Lösung eingesetzt sind (BGH BlPMZ 2004 S. 428
„elektronischer Zahlungsverkehr“, vgl. BGH BlPMZ 2005 S. 77 „Anbieten interaktiver Hilfe“; BGH BlPMZ 2005, 177 „Rentabilitätsermittlung“; BGH BlPMZ 2002, 114
„Suche fehlerhafter Zeichenketten“).

                                       -8-



1.4.1 Welches technische Problem durch eine Erfindung gelöst wird, ist objektiv
danach zu bestimmen, was die Erfindung tatsächlich leistet (s. o. BGH „Anbieten
interaktiver Hilfe“, II. 4 b).


Im vorliegenden Fall liegt die objektive Leistung darin, durch automatisches Durchsuchen und Ergänzen eines neu geschriebenen Computerprogramms die sichere
Verwendung von Intertask-Variablen möglich zu machen, ohne dass der Programmierer sich darum besonders zu kümmern braucht. Das gelöste Problem besteht
offensichtlich darin, in einem Multitasking-Betrieb die Datenkonsistenz der Intertask-Variablen sicherzustellen, die ohne besondere Schutzmaßnahmen wegen der
unabhängig voneinander stattfindenden Abarbeitung verschiedener Tasks gefährdet wäre.


Dieses objektive Problem ist kein technisches. Der Fachmann, der vor dieses Problem gestellt wird, braucht sich in keiner Weise mit dem technischen Aufbau oder
der technischen (!) Funktion des verwendeten Computers auseinanderzusetzen.
Vielmehr tritt dieses Problem bei jedem Multitasking-Betriebssystem auf, wenn
dieselbe Variable von mehreren Tasks benutzt werden soll; welche (möglicherweise technischen) Anwendungen davon bearbeitet werden sollen, ist für Problemstellung und Lösung ohne jeden Belang.


Damit wird jedoch der Bereich der Technik gar nicht erst betreten. Zur zielgerichteten Ergänzung eines Computerprogramms durch aus einer Liste entnommene
Programmteile, die anhand bestimmter, automatisch aus diesem Programm ermittelter Parameter auszuwählen sind, genügt ein entsprechend programmierter handelsüblicher Computer. Die beanspruchte Lehre verlangt keinerlei Kenntnisse der
physikalischen Welt, etwa über die technischen Eigenheiten dieses Computers
(soweit die auszuwählende Ergänzung des Computerprogramms etwa davon abhängig sein sollte, für welche Art von Mikroprozessor das Programm vorgesehen
ist, fehlt es an einer entsprechenden Offenbarung in der Anmeldung). Besondere
„technische Mittel“ sind somit zur Lösung des Problems nicht nötig und wurden

                                        -9-



von der Anmelderin auch auf Nachfrage nicht benannt. Allein der bestimmungsgemäße Einsatz eines Computers rechtfertigt jedoch nicht, die beanspruchte Lehre
als patentierbar anzusehen (s. o. BGH „Suche fehlerhafter Zeichenketten“).


1.4.2 Auch der Einwand, dass – im Sinne der „Seitenpuffer“-Entscheidung (BGH
BlPMZ 1991, 345) – die Funktionsfähigkeit der Datenverarbeitungsanlage als solche und das unmittelbare Zusammenwirken ihrer Elemente betroffen sei, kann zu
keiner anderen Beuteilung führen.


Denn die Lehre des dortigen Hauptanspruchs bezieht sich konkret auf die technischen Elemente der Datenverarbeitungsanlage und deren technisches Zusammenwirken, siehe insbesondere BGH, a. a. O. - III. 5b, 5c. Sie setzt sich mit dem
technischen Aufbau der Anlage (Hauptspeicher, Seitenpuffer, freigebbare Speicherseiten, mehrfache Seitenanforderungen erfordern Wartezeiten des Prozessors) auseinander; es ist technisches Fachwissen erforderlich, um zur beanspruchten Lehre zu gelangen. Im Mittelpunkt der dortigen Lehre stehen „Elemente
einer Datenverarbeitungsanlage“, die „beim Betrieb unmittelbar auf bestimmte Art
und Weise“ benutzt werden.


Demgegenüber sind im hier zu entscheidenden Fall nicht konkrete „Elemente der
Datenverarbeitungsanlage“ von Bedeutung, sondern Programmteile (Tasks), darin
verwendete Variable, und die Priorität der Tasks. Die technische Arbeitsweise der
Elemente der Datenverarbeitungsanlage spielt keine Rolle.


Daher ist die „Seitenpuffer“-Entscheidung für den vorliegenden Fall nicht relevant.


1.4.3 Das mit dem Patentanspruch 1 beanspruchte Verfahren ist somit als „Programm als solches“ im Sinne der Ausschlusskriterien des § 1 Abs. 3 Nr. 3 und 4
PatG zu bewerten und deshalb nicht patentfähig.

                                       - 10 -



2.     Zu den Hilfsanträgen 1 bis 9:
Die verschiedenen Patentansprüche 1 nach den Hilfsanträgen 1 bis 9 basieren auf
dem Anspruch 1 gemäß Hauptantrag. Sie unterscheiden sich davon durch zusätzliche Merkmale, die aber allein aus der Welt der Programmierung stammen und in
keinem Fall den im Hauptantrag fehlenden Bezug zur Technik herstellen können.
Gegenteiliges hat auch die Anmelderin nicht vorgetragen.


Sonach kann keiner der Hilfsanträge anders beurteilt werden als der Hauptantrag,
die dortige Argumentation gilt in entsprechender Weise (Busse, PatG, 6. Aufl.,
§ 100 Rdn. 96). Die Patentansprüche 1 nach den Hilfsanträgen 1 bis 9 unterliegen
ebenso den Ausschlusskriterien des § 1 Abs. 3 Nr. 3 und 4 PatG.


                                        III.


Bei dieser Sachlage war die Beschwerde gegen den Beschluss der Prüfungsstelle
zurückzuweisen.


gez.
Unterschriften
