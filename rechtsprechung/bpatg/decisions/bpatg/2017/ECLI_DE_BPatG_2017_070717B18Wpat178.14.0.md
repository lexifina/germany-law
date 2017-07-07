---
ecli: "ECLI:DE:BPatG:2017:070717B18Wpat178.14.0"
court: "Bundespatentgericht"
spruchkoerper: "18"
aktenzeichen: "18 W (pat) 178/14"
decided: "2017-07-07"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=29&nr=29241&anz=809&pos=445&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-07-07_18_W-pat_178_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0038.md"]
---

# Bundespatentgericht, 18 W (pat) 178/14 vom 2017-07-07

## Entscheidung

BUNDESPATENTGERICHT


 18 W (pat) 178/14                                                  Verkündet am
_______________                                                      7. Juli 2017
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2007 006 190.2-53


…




hat der 18. Senat (Techn. Beschwerdesenat) des Bundespatentgerichts auf die
mündliche Verhandlung vom 7. Juli 2017 durch die Vorsitzende Richterin Dipl.-Ing.
Wickborn sowie die Richter Kruppa, Dipl.-Phys. Dr. Schwengelbeck und Dipl.-Ing.
Altvater




BPatG 154
05.11

                                         -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der
       Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
       Markenamts vom 19. Oktober 2012 aufgehoben und das Patent
       auf der Grundlage der folgenden Unterlagen erteilt:


       -       Patentansprüche 1 bis 4, eingereicht in der mündlichen
               Verhandlung,
       -       Beschreibung Seiten 1, 2, 2a, 3 bis 9, eingereicht in der
               mündlichen Verhandlung,
       -       Figuren 1 bis 5, eingereicht in der mündlichen Verhandlung.




                                     Gründe


                                          I.


Die am 7. Februar 2007 beim Deutschen Patent- und Markenamt unter
Inanspruchnahme einer US-amerikanischen Priorität vom 7. Februar 2006 (US
11/349,661) eingereichte Patentanmeldung 10 2009 006 190.2 mit der Bezeichnung


                  „Technik zur Verwendung von Speicherattributen“


wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamtes vom 19. Oktober 2012 zurückgewiesen. Die Prüfungsstelle hat ihren Zurückweisungsbeschluss damit begründet, dass der
Gegenstand des Anspruchs 1 sowohl in der Fassung des (damaligen) Hauptantrags als auch in der Fassung des (damaligen) Hilfsantrags mangels

                                       -3-



erfinderischer Tätigkeit nicht patentfähig sei, wobei auf folgende Druckschrift
verwiesen wurde:


      D8:    US 2005 / 0 149 702 A1.


Im Prüfungsverfahren sind außerdem folgende Druckschriften berücksichtigt
worden:


      D1:    DE 103 09 919 A1,
      D2:    US 2005 / 0 198 637 A1,
      D3:    US 5 974 438 A,
      D4:    US 5 428 761 A,
      D5:    US 5 974 507 A,
      D6:    US 6 189 112 B1 und
      D7:    US 6 748 496 B1.


Die Beschwerde der Anmelderin richtet sich gegen den vorstehend genannten
Beschluss.


Sie beantragt,


       den Beschluss der Prüfungsstelle für Klasse G 06 F des
       Deutschen Patent- und Markenamts vom 19. Oktober 2012
       aufzuheben und das Patent auf der Grundlage der folgenden
       Unterlagen zu erteilen:


       -     Patentansprüche 1 bis 4, eingereicht in der mündlichen Verhandlung,
       -     Beschreibung Seiten 1, 2, 2a, 3 bis 9, eingereicht in der
             mündlichen Verhandlung,
       -     Figuren 1 bis 5, eingereicht in der mündlichen Verhandlung.

                                      -4-



Patentanspruch 1 lautet unter senatsseitiger Hinzufügung einer Merkmalsgliederung wie folgt:


      M1     „Maschinenlesbares Medium, auf dem ein Satz Befehle gespeichert
             ist, die, wenn sie von der Maschine ausgeführt werden, die Maschine
             dazu veranlassen, ein Verfahren auszuführen, das aufweist:


      M2     Lesen eines Attributbits (115), welches einer Cache-Speicherlinie
             (105) zugeordnet ist, wobei die Cache-Speicherlinie (105) nur einem
             Software-Thread in einem Multi-Thread-Programm zugeordnet ist,
             wobei das Attributbit (115) als ein Ergebnis des Ausführens eines
             Befehls geprüft wird, und wobei das Attributbit (115) durch Ausführen
             eines load_check Befehls gelesen wird und das Attributbit durch
             Ausführen eines load_set Befehls gesetzt wird;


      M3     Bestimmen des Werts des Attributbits (115), wobei das Bestimmen
             des Werts des Attributbits (115) das Ausführen eines Architekturszenarios in einem Prozessor der Maschine aufweist, wobei das
             Szenario bestimmt, ob die Cache-Speicherlinie (115) sich in einem
             unerwarteten Zustand befindet;


      M4     Ausführen eines leichtgewichtigen Yield-Ereignisses in Reaktion auf
             das Bestimmen des Werts des Attributbits (115).“


Der nebengeordnete Patentanspruch 3 lautet unter senatsseitiger Hinzufügung
einer Merkmalsgliederung wie folgt:


             „System, aufweisend:


      N1     einen Speicher zum Speichern eines load_set Befehls und eines
             load_check Befehls, wobei der load_set Befehl so ausgelegt ist, dass

                                       -5-



             eine Information von einer Cache-Linie (105) geladen und ein
             zugehöriges Attributbit (115) gesetzt wird, und der load_check Befehl
             so ausgelegt ist, dass eine Information von einer Cache-Linie (105)
             geladen und ein zugehöriges Attributbit (115) geprüft wird, wobei die
             Cache-Linie (105) nur einem Software-Thread in einem Multi-Thread
             Programm zugeordnet ist und das Attributbit (115) anzeigt, dass die
             Cache-Linie (105) sich in einem unerwarteten Zustand befindet,


      N2     mindestens einen Prozessor, welcher wenigstens einen Verarbeitungskern zum Abrufen wenigstens eines der load_set und
             load_check Befehle und eine Logik zum Implementieren eines
             Szenarios in Reaktion auf ein Prüfen des Attributbits (115) aufweist,


      N3     wobei das Szenario darin besteht, ein leichtgewichtiges Yield-Ereignis zu verursachen, wobei das leichtgewichtige Yield-Ereignis
             darin besteht, eine Steuerprogrammroutine aufzurufen, um auf den
             unerwarteten Zustand, der erfasst wurde, zu reagieren.“




Der nebengeordnete Patentanspruch 4 lautet unter senatsseitiger Hinzufügung
einer Merkmalsgliederung wie folgt:


             „Verfahren, aufweisend:


      O1     Lesen eines Attributbits (115), welches einer Cache-Linie (105)
             zugeordnet ist, wobei die Cache-Linie (105) einem Software-Thread
             in einem Multi-Thread-Programm zugeordnet ist, und das Attributbit
             (115) anzeigt, ob ein Programm einen vorherigen Bezug auf die
             Cache-Linie (105) zur Analyse durch ein Werkzeug aufgenommen
             hat, welches aus einer Gruppe gewählt ist, bestehend aus einem

                                         -6-



              Leistungsüberwachungswerkzeug und einem Fehlerbeseitigungswerkzeug;


       O2     Bestimmen des Werts des Attributbits (115);


       O3     Ausführen eines leichtgewichtigen Yield-Ereignisses in Reaktion auf
              ein Bestimmen des Werts des Attributbits, wobei das Bestimmen des
              Werts des Attributbits das Durchführen eines Architekturszenarios in
              einem Prozessor aufweist, wobei das Architekturszenario bestimmt,
              ob die Cache-Linie (105) in einem unerwarteten Zustand ist.“


Wegen des Wortlauts des Unteranspruchs 2 wird auf den Akteninhalt verwiesen.


Die Beschwerdeführerin vertritt die Auffassung, dass die geltenden Ansprüche
zulässig und patentfähig sind.


Wegen der weiteren Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die zulässige Beschwerde hat in der Sache Erfolg. Denn die zweifelsfrei
gewerblich anwendbaren Gegenstände der unabhängigen Patentansprüche 1, 3
und 4 sind im Lichte der im Verfahren befindlichen Druckschriften neu und
beruhen auf einer erfinderischen Tätigkeit; auch die übrigen Kriterien zur
Patenterteilung sind erfüllt (§§ 1 bis 5, 34, 38 PatG).


1. Die vorliegende Anmeldung betrifft gemäß geltender Beschreibungseinleitung
    eine Technik, um Speicherzustände oder andere Information zu verwenden
    bzw. zu prüfen und einzustellen, die in Verbindung mit einem oder mehreren

                                    -7-



Speicherorten stehen und die Attributbits verwenden, welche dem einen oder
den mehreren Speicherorten zugeordnet sind (vgl. S. 1 erster Abs. zw. Satz).


In modernen Computersystemen können gemäß geltender Beschreibungseinleitung Mikroprozessoren oder Mikroprozessorkerne auf einen sehr großen
Speicherraum zugreifen, welcher eine sehr große Anzahl an Speichertypen
umfassen könne. Zum Beispiel könne ein Speicheradressbereich in einem
Computersystem Information speichern, welche nur durch einen bestimmten
Prozessor oder Prozessorkern angesprochen werden könne, wohingegen auf
andere Adressbereiche durch Mehrfachprozessoren oder Prozessorkerne
zugegriffen werden könne. Die Ausschließlichkeit eines Speichers sei nur ein
Attribut, welches einem Speicheradressbereich zugeordnet werden könne
(vgl. S. 1 zweiter Abs.).


In einigen Systemen des Stands der Technik könnten Speicherberechtigungen
oder Zugriffsregeln durch das Betriebssystem (OS) mittels eines virtuellen
Speichermanagements in einer relativ groben Körnigkeit von virtuellen
Speicherseiten gesteuert werden. Die Körnigkeit virtueller Speicherseiten sei
in einigen Systemen gemäß dem Stand der Technik unterschiedlich, von
ungefähr 4 Kilobyte bis viele Megabyte in der Größe. Das Verändern der
Speicherberechtigungen könne ein aufwendiger Vorgang in Bezug auf
Systemwartezeit, Platzverhältnissen von Dies oder Systemkosten sein (vgl.
S. 1 vorle. Abs.). Es könne Situationen geben, in welchen ein Programm eine
Speicheradresse vor dem Zugreifen darauf prüfen wolle. Zum Beispiel könne
ein Programm eine Adresse vor dem Zugreifen prüfen, wenn Programmfehler
beseitigt werden, wobei Grenzen und Typensicherheit in verschiedenen
Computerprogrammsprachen geprüft würden, wenn Programmprofile zur
Analyse ihrer Leistung erstellt würden oder wenn andere Gründe vorlägen
(vgl. S. 1 und 2 seitenübergreifender Abs.).

                                   -8-



Wenn ein Programm eine Adresse gemäß einem Satz Regeln prüfe, könnten
wenigstens zwei Lösungswege gemäß dem Stand der Technik eingesetzt
werden: Ein Lösungsweg bestehe darin, das Betriebssystem zu verwenden,
um sicher zu stellen, dass Adressen, welche nicht den Regeln entsprechen,
durch das Virtuelle-Speicher-Management erkannt werden. Bei diesem
Lösungsweg könne die Körnigkeit auf das relativ grobe Adressierschema des
Virtuelle-Speicher-Managements begrenzt werden und das Verändern der
Zugriffsregeln könne sehr kostspielig sein. Ein anderer Lösungsweg gemäß
dem Stand der Technik bestehe darin, einen Satz Prüfungen für eine Adresse
im Programm selbst auszuführen, bevor die Adresse verwendet werde, um auf
den Speicher zuzugreifen. Der Satz Prüfungen könne die Adresse gegen
jeden Satz Regeln mit jeder beliebigen Körnigkeit vergleichen. Der Nachteil
dieses Lösungswegs gemäß dem Stand der Technik bestehe darin, dass ein
wesentlicher Leistungsoverhead für jeden Speicherbezug gezahlt werden
müsse, um die richtigen Prüfungen durchzuführen (vgl. geltende Beschreibung
S. 2 zweiter Abs.).


Die der Erfindung zugrundeliegende Aufgabe bzw. das zugrundeliegende
technische Problem ist darin zu sehen, ein maschinenlesbares Medium, ein
System und ein Verfahren anzugeben, welches jeweils dazu eingerichtet ist,
es einem Programm-Thread zu ermöglichen, Adressen mit feineren
Granularitäten als der virtuellen Speicherverwaltungsadressierung zu prüfen,
um festzustellen, ob ein bestimmter Thread die Kontrolle über die Adresse,
wie beispielsweise einen adressierten Speicherort, hat (vgl. geltende
Beschreibungseinleitung S. 2a letzter Abs.).


Als zuständiger Fachmann wird vorliegend ein Diplom-Ingenieur der
Fachrichtung Elektrotechnik mit Schwerpunkt Informationstechnik angesehen,
der eine mehrjährige Erfahrung auf dem Gebiet der Cache-Verwaltung in
Multithread-Systemen aufweist.

                                   -9-



Zur Lösung der Aufgabe ist ein maschinenlesbares Medium gemäß
Anspruch 1 vorgesehen, auf dem ein Satz Befehle gespeichert ist, welche,
wenn sie von der Maschine ausgeführt werden, die Maschine dazu
veranlassen, ein Verfahren mit den Merkmalen M2 bis M4 auszuführen (vgl.
Merkmal M1). Merkmal M2 beinhaltet das Lesen eines Attributbits, welches
einer Cache-Speicherlinie, d. h. einer Cachezeile, zugeordnet ist, wobei diese
Cache-Speicherlinie nur einem Software-Thread in einem Multi-Thread-Programm zugeordnet ist. Das Attributbit wird durch das Ausführen eines
„load_check“ Befehls zur Überprüfung eines Ladevorgangs gelesen, wobei ein
„load_set“ Befehl verwendet wird, um das Attributbit zu setzten (vgl. Merkmal
M2 / Beschreibung S. 5 zweiter Abs.). Weiterhin ist vorgesehen, dass der
Werts des Attributbits bestimmt wird, wobei das Bestimmen des Werts des
Attributbits das Ausführen eines Architekturszenarios in einem Prozessor der
Maschine beinhaltet - das Architekturszenario dient dabei zur Bestimmung, ob
sich die Cache-Speicherlinie in einem unerwarteten Zustand befindet (vgl.
Merkmal M3). In Reaktion auf die Bestimmung des Wertes des Attributbits
wird dann ein leichtgewichtiges Yield-Ereignis ausgeführt (vgl. Merkmal M4).


Zur Lösung der Aufgabe ist zudem ein System gemäß Anspruch 3
vorgesehen, welches einen Speicher zum Speichern eines „load_set“ Befehls
und eines „load_check“ Befehls aufweist, wobei die Cache-Linie ebenfalls nur
einem Software-Thread in einem Multi-Thread Programm zugeordnet ist und
das Attributbit anzeigt, dass die Cache-Linie sich in einem unerwarteten
Zustand befindet. Mit dem „load_set“ Befehl wird eine Information der Cache-Linie geladen und ein zugehöriges Attributbit gesetzt. Mit dem „load_check“
Befehl wird ein zugehöriges Attributbit geprüft (vgl. Merkmal N1). Weiterhin ist
vorgesehen, dass das System mindestens einen Prozessor aufweist, welcher
wenigstens einen Verarbeitungskern zum Abrufen wenigstens eines der
„load_set“ bzw. „load_check“ Befehle und eine Logik zum Implementieren
eines Szenarios in Reaktion auf ein Prüfen eines Attributbits aufweist (vgl.
Merkmal N2). Das Szenario besteht wiederum darin, ein leichtgewichtiges

                                     - 10 -



   Yield-Ereignis zu verursachen, wobei das leichtgewichtige Yield-Ereignis darin
   besteht, eine Steuerprogrammroutine aufzurufen, um auf einen erfassten
   unerwarteten Zustand zu reagieren (vgl. Merkmal N3).


   Zur Lösung der vorstehend genannten Aufgabe ist weiterhin ein Verfahren
   gemäß Anspruch 4 vorgesehen, bei dem ein Attributbit gelesen wird, welches
   einer Cache-Speicherlinie zugeordnet ist, die wiederum einem Software-Thread in einem Multi-Thread-Programm zugeordnet ist; das Attributbit zeigt
   dabei an, ob ein Programm einen vorherigen Bezug auf die Cache-Linie zur
   Analyse durch ein Werkzeug aufgenommen hat, welches aus einer Gruppe
   gewählt ist, die aus einem Leistungsüberwachungswerkzeug und einem
   Fehlerbeseitigungswerkzeug besteht (vgl. Merkmal O1). Des Weiteren wird
   der Wert des Attributbits bestimmt (vgl. Merkmal O2). Zudem ist bei dem
   anspruchsgemäßen Verfahren ebenfalls das Ausführen eines leichtgewichtigen Yield-Ereignisses in Reaktion auf das Bestimmen des Werts des
   Attributbits vorgesehen, wobei das Bestimmen des Werts des Attributbits das
   Durchführen eines Architekturszenarios in einem Prozessor beinhaltet und das
   Architekturszenario in Analogie zu den vorstehend aufgeführten Ansprüchen 1
   und 3 bestimmt, ob sich die Cache-Linie in einem unerwarteten Zustand
   befindet (vgl. Merkmal O3).


2. Die geltenden Ansprüche und Beschreibungsunterlagen sind zulässig
   (§ 38 PatG).


   Anspruch 1 weist Merkmale des ursprünglichen nebengeordneten Anspruchs 9 sowie die Merkmale der ursprünglichen Unteransprüche 10 und 12
   bis 15 auf. Im Einzelnen ist das Merkmal M1 des Anspruchs 1 dabei im
   ursprünglichen Anspruch 9 offenbart, während Merkmal M2 auf Merkmalen
   des ursprünglichen Anspruchs 9 sowie den Merkmalen der ursprünglichen
   Ansprüche 12 bis 14 basiert. Die Merkmale M3 und M4 des Anspruchs 1
   basieren ebenfalls auf dem ursprünglichen Anspruchs 9, wobei Merkmal M3

                                  - 11 -



außerdem die Merkmale der ursprünglichen Unteransprüche 10 und 15
aufweist.


Unteranspruch 2 basiert auf dem ursprünglichen Unteranspruch 11.


Das Merkmal N1 des nebengeordneten Anspruchs 3 basiert auf den ursprünglichen Ansprüchen 16 bis 18, 20 und 22, wobei bezüglich Merkmal N1 auch
auf die vorherigen Ausführungen zur Zulässigkeit des Merkmals M2 des
Anspruchs 1 verwiesen wird, die hier in gleicher Weise gelten. Das Merkmal
N2 des Anspruchs 3 ist im ursprünglichen Anspruch 16 sowie dem ursprünglichen Unteranspruch 19 offenbart, während Merkmal N3 des Anspruchs 3 die
Merkmale der ursprünglichen Unteransprüche 20 und 21 aufweist.


Merkmal O1 des nebengeordneten Anspruchs 4 basiert auf dem ursprünglichen nebengeordneten Anspruch 31 sowie dem ursprünglichen Unteranspruch 32; Merkmal O2 des Anspruchs 4 basiert auf dem letzten Teilmerkmal
des ursprünglichen Anspruchs 31. Das weitere Merkmal O3 basiert auf den
Merkmalen der ursprünglichen Unteransprüche 33 und 34, wobei bezüglich
Merkmal O3 zudem auf die vorherigen Ausführungen zur Zulässigkeit des
Merkmals N1 des Anspruchs 3 verwiesen wird, die hier in gleicher Weise
gelten.


Die geltende Beschreibung beinhaltet eine zulässige Anpassung der
Beschreibung an den Wortlaut der geltenden nebengeordneten Ansprüche 1,
3 und 4, wobei diesbezügliche sprachliche Anpassungen auf den ursprünglich
in englischer Sprache eingereichten Anmeldungsunterlagen basieren (vgl.
Beschreibung S. 1 und 2a). Die geltenden Figuren 1 bis 5 entsprechen den
ursprünglich eingereichten Figuren.

                                      - 12 -



3. Der Gegenstand des geltenden Patentanspruchs 1 ist neu gegenüber dem
   Stand der Technik gemäß den Druckschriften D1 bis D8 (§ 3 PatG).


   Druckschrift D8, die dem Zurückweisungsbeschluss der Prüfungsstelle für
   G 06 F des Deutschen Patent- und Markenamts zugrunde gelegen hat,
   offenbart im Hinblick auf das Merkmal M1 einen Satz von Befehlen (u. a.
   „load check (LDCHK) instruction“), der auf einer Maschine in Form eines
   Computersystems mit einem Prozessor und einem Cache-Speicher (u. a.
   „memory rename cache 260“) ausgeführt wird (vgl. u. a. Abs. [0015], [0016]
   und [0018]). Hinsichtlich Merkmal M2 ist aus der Druckschrift bekannt, dass
   das Ausführen eines Load-Check-Befehls („load check (LDCHK) instruction“)
   bewirkt, dass durch den Vergleich eines im weitesten Sinne als Attribut
   anzusehenden     Identifikators   („identifier“)   mit   einem   prognostizierten
   Identifikator („predicted store identifier“) überprüft wird, ob eine erfolgte
   Speicher-Umbenennung („memory renaming“) korrekt war (vgl. Abs. [0028]
   und [0036]).


   Der in Merkmal M2 aufgeführte Zusammenhang mit einem Software-Thread
   bzw. einem Multithread-Programm sowie ein Zusammenhang mit einem
   Attributbit, welches einer Cache-Speicherlinie zugeordnet ist, kann Druckschrift D8 jedoch nicht entnommen werden. Mangels eines solchen Attributbits
   sind dieser Druckschrift auch die Merkmale M3 und M4 bezüglich einem
   Bestimmen des Wertes eines Attributbits im Zusammenhang mit einer
   Bestimmung, ob sich eine Cache-Speicherlinie in einem unerwarteten Zustand
   befindet, sowie das Ausführen eines leichtgewichtigen Yield-Ereignisses in
   Reaktion auf das Bestimmen des Attribut-Wertes nicht zu entnehmen
   (Merkmale M3 und M4 fehlen).


   Druckschrift D3 beschreibt im Hinblick auf die Merkmale M1 und M2 ein
   Threadmanagement für ein Computersystem mit einem Cache-Speicher
   („cache 402“), auf den mehrere Programm-Threads über eine jeweils

                                    - 13 -



zugewiesene Cache-Linie („cache line 408“) zugreifen (vgl. u. a. den Abstract
sowie Fig. 4 mitsamt zugeh. Text in Sp. 13 Z. 12-22). Jeder Cache-Linie ist
Status-Information zugeordnet („“MESI“ (Modified, Exclusive, Shared and
Invalid“ / „MESI status 412 for each line 408“), wobei der Fachmann hier
mitliest, dass der Status mittels Attributbits definiert wird (vgl. Sp. 2 Z. 65 bis
Sp. 3 Z. 9 i. V. m. Sp. 12 Z. 25-39 und Sp. 13 Z. 12-22). Neben der Status-Information („MESI“) ist jeder Cache-Linie eine Thread-Identifikation („414“)
und ein Process-aktiv-Statusbit („416“) zugeordnet (vgl. Sp. 13 Z. 23-36 sowie
Fig. 4). In dieser Druckschrift ist jedoch bereits nicht offenbart, dass ein
Attributbit durch Ausführen eines load_check Befehls zur Überprüfung gelesen
und das Attributbit durch Ausführen eines load_set Befehls gesetzt wird
(Merkmal M2 fehlt teilweise). Die Merkmale M3 und M4 bezüglich einem
Attributbit im Zusammenhang mit einer Bestimmung, ob sich eine Cache-Speicherlinie in einem unerwarteten Zustand befindet, sowie das Ausführen
eines leichtgewichtigen Yield-Ereignisses in Reaktion auf das Bestimmen des
Attribut-Wertes sind dieser Druckschrift ebenfalls nicht zu entnehmen
(Merkmale M3 und M4 fehlen).


Die übrigen im Prüfungsverfahren genannten Druckschriften liegen noch
weiter ab und sind zur Beurteilung des Gegenstands des Patentanspruchs 1
nicht weiter relevant. Aus keiner der Druckschriften D1, D2 und D4 bis D7 sind
Befehle bekannt, die den in Merkmal M2 genannten Befehlen (load_check /
load_set) im Zusammenhang mit Attributbits entsprechen, welche einer
Cache-Speicherlinie zugeordnet sind, wobei eine Cache-Speicherlinie einem
Software-Thread eines Multi-Thread-Programms zugeordnet ist. Auch die
weiteren Merkmale M3 und M4, die eine Bestimmung eines unerwarteten
Zustands einer Cache-Speicherlinie im Zusammenhang mit dem vorstehend
genannten Attributbit sowie das Ausführen eines leichtgewichtigen Yield-Ereignisses betreffen, sind keiner der Druckschriften D1, D2 und D4 bis D7 zu
entnehmen (vgl. in D1 u. a. die Zusammenfassung sowie Abs. [0053]; vgl. in
D2 u. a. Abstract und Fig. 3 mitsamt zugeh. Text in Abs. [0031] ff.; vgl. in D4

                                          - 14 -



   u. a. Abstract und Sp. 5 Z. 23 bis Sp. 6 Z. 28 sowie Fig. 2 mitsamt zugeh.
   Text; vgl. in D5 u. a. Abstract, Sp. 2 Z. 31 ff sowie Fig. 6 mitsamt zugeh. Text;
   vgl. in D6 u. a. Abstract und Sp. 6, Z. 37-42; vgl. in D7 u. a. Abstract, Sp. 4
   Z. 7 ff. sowie Fig. 5, Sp. 6 Z. 50 ff. und Sp. 7, Z. 19-21).


   Der Gegenstand des Anspruchs 1 ist damit neu gegenüber dem Stand der
   Technik gemäß den von der Prüfungsstelle ins Verfahren eingeführten
   Druckschriften D1 bis D8, denen - wie vorstehend ausgeführt - ein Hinweis auf
   wesentliche Merkmale des Anspruchs 1 nicht entnehmbar ist (vgl. insbesondere die Merkmale M3 und M4).


4. Der Gegenstand des geltenden Patentanspruchs 1 beruht auch auf einer
   erfinderischen Tätigkeit (§ 4 PatG).


   Wie zuvor bereits ausgeführt, kann der Fachmann dem Stand der Technik
   gemäß den Druckschriften D1 bis D8 keinen Hinweis auf die Merkmale M3
   und M4 entnehmen. Auch eine Zusammenschau der Lehren der Druckschriften D1 bis D8 führt damit nicht zu dem Gegenstand des Anspruchs 1 mit
   den Merkmalen M3 und M4, da diese dem Stand der Technik nicht entnehmbar sind. Ein solcher Anspruchsgegenstand ist dem Fachmann auch
   unter Einbeziehung seines Fachwissens nicht nahegelegt.


   Der Gegenstand des Patentanspruchs 1 beruht somit auf einer erfinderischen
   Tätigkeit und ist daher patentfähig.


 5. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 3 ist
    ebenfalls neu gegenüber dem Stand der Technik (§ 3 PatG).


   Druckschrift D8 beschreibt ein Computersystem mit einem Speicher und
   einem Prozessor sowie das Ausführen eines Load-Check-Befehls („load check
   (LDCHK) instruction“), wobei zur Vermeidung von Wiederholungen auf die

                                        - 15 -



   Ausführungen in Abschnitt II. 3. verwiesen wird. Insbesondere die Merkmale
   N2 und N3 bezüglich einer Logik zum Implementieren eines Szenarios in
   Reaktion auf ein Prüfen eines solchen Attributbits sowie das Ausführen eines
   leichtgewichtigen Yield-Ereignisses bzw. ein damit verbundener Aufruf einer
   Steuerprogrammroutine zur Reaktion auf einen erfassten unerwarteten
   Zustand sind Druckschrift D8 nicht zu entnehmen (vgl. die Ausführungen in
   Abschnitt II. 3., die hier in gleicher Weise gelten).


   Auch den weiteren im Prüfungsverfahren genannten Druckschriften D1 bis D7
   ist eine Bestimmung eines unerwarteten Zustands einer Cache-Speicherlinie
   im Zusammenhang mit einem Attributbit sowie das Ausführen eines
   leichtgewichtigen Yield-Ereignisses entsprechend den Merkmalen N2 und N3
   nicht zu entnehmen (vgl. u. a. die Ausführungen in Abschnitt II. 3., die hier
   wiederum in gleicher Weise gelten).


   Das im Patentanspruchs 3 aufgeführte System ist damit ebenfalls neu
   gegenüber den von der Prüfungsstelle ins Verfahren eingeführten Druckschriften D1 bis D8, denen - wie zuvor ausgeführt - kein Hinweis auf die
   Merkmale N2 und N3 des Patentanspruchs 3 entnehmbar ist.


6. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 3 beruht
   ebenfalls auf einer erfinderischen Tätigkeit (§ 4 PatG).


   Wie vorstehend ausgeführt, kann der Fachmann dem Stand der Technik
   gemäß den Druckschriften D1 bis D8 keinen Hinweis auf die Merkmale N2
   und N3 entnehmen. Auch eine Zusammenschau der Lehren der Druckschriften D1 bis D8 führt damit nicht zu dem Gegenstand des Patentanspruchs 3 mit den Merkmalen N2 und N3, da diese dem Stand der Technik
   nicht entnehmbar sind. Ein solcher Anspruchsgegenstand ist dem Fachmann
   auch unter Einbeziehung seines Fachwissens nicht nahegelegt.

                                     - 16 -



7. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 4 ist
  ebenfalls neu gegenüber dem Stand der Technik (§ 3 PatG).


  Der Fachmann kann dem Stand der Technik gemäß den Druckschriften D1 bis
  D8 keinen Hinweis auf ein Verfahren entnehmen, bei dem ein Attributbit einer
  Cache-Speicherlinie anzeigt, ob ein Programm entsprechend Merkmal O1
  einen vorherigen Bezug auf die Cache-Linie zur Analyse durch ein Leistungsüberwachungswerkzeug oder ein Fehlerbeseitigungswerkzeug aufgenommen hat (vgl. u. a. die in Abschnitt II. 3. aufgeführten Zitatstellen in den
  Druckschriften D1 bis D8). Auch das Merkmal O3, welches das Bestimmen
  eines Wertes des Attributwertes im Zusammenhang mit dem Ausführen eines
  leichtgewichtigen Yield-Prozesses in Reaktion auf das Bestimmen des Wertes
  des Attributbits sowie eine Bestimmung, ob eine Cache-Linie in einem
  unerwarteten Zustand ist, kann keiner der im Verfahren befindlichen Druckschriften D1 bis D8 entnommen werden. Zur Vermeidung von Wiederholungen
  wird auf die vorstehenden Ausführungen zur Neuheit des Gegenstands des
  Anspruchs 1 mit den entsprechenden Merkmalen M3 und M4 in Abschnitt II. 3.
  verwiesen, die hier in gleicher Weise gelten.


8. Der Gegenstand des geltenden nebengeordneten Patentanspruchs 4 beruht
  ebenfalls auf einer erfinderischen Tätigkeit (§ 4 PatG).


  Wie zuvor ausgeführt, kann der Fachmann dem Stand der Technik gemäß
  den Druckschriften D1 bis D8 keinen Hinweis auf die Merkmale O1 und O3
  des Verfahrens gemäß Patentanspruch 4 entnehmen. Eine Zusammenschau
  der Druckschriften D1 bis D8 führt damit auch nicht zu den Merkmalen O1
  bis O3 des nebengeordneten Patentanspruchs 4. Ein solchermaßen ausgestaltetes Verfahren ist dem Fachmann auch unter Einbeziehung seines
  Fachwissens nicht nahegelegt.

                                       - 17 -



 9. Der abhängige Anspruch 2 betrifft eine über das Selbstverständliche
    hinausgehende Ausgestaltung des Gegenstands des Anspruchs 1 und ist
    daher ebenfalls patentfähig.


10. Da die vorgelegten Unterlagen auch den Anforderungen des § 34 PatG
    genügen, war das Patent im Umfang der geltenden Ansprüche 1 bis 4, der
    geltenden Beschreibung, Seiten 1, 2, 2a und 3 bis 9 sowie der geltenden
    Figuren 1 bis 5 zu erteilen.




                                         IV.


                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht der am Beschwerdeverfahren Beteiligten das
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

                                    - 18 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Wickborn             Kruppa              Schwengelbeck                Altvater




                                                                           Me
