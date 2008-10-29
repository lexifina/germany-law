---
ecli: "ECLI:DE:BPatG:2008:291008B20Wpat344.04.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 344/04"
decided: "2008-10-29"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2008&Sort=1&Seite=82&nr=10538&anz=1485&pos=1244&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2008-10-29_20_W-pat_344_04_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 20 W (pat) 344/04 vom 2008-10-29

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 344/04                                                    Verkündet am
_______________                                                      29. Oktober 2008
    (Aktenzeichen)                                                          …




                               BESCHLUSS

                              In der Einspruchssache


                         betreffend das Patent 196 50 515


…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die     mündliche    Verhandlung   vom    29. Oktober 2008   durch   den   Richter
Dipl.-Phys. Dr. Hartung als Vorsitzenden, die Richterin Martens sowie die Richter Dipl.-Ing. Gottstein und Dipl.-Ing. Kleinschmidt




BPatG 154
08.05

                                         -2-



beschlossen:


        Das Patent wird mit folgenden Unterlagen beschränkt aufrechterhalten:


        Patentansprüche 1 – 3, überreicht in der mündlichen Verhandlung,


        Beschreibung wie Patentschrift mit Einfügung auf Seite 2 am Ende
        von Absatz [0004], überreicht in der mündlichen Verhandlung,


        Zeichnungen wie Patentschrift.


                                    Gründe


                                          I.


Auf die am 5. Dezember 1996 eingereichte Patentanmeldung hat das DPMA das
Patent mit der Bezeichnung "Verfahren zum Decodieren von Zusatzdaten" erteilt.
Das erteilte Patent umfasst 7 Patentansprüche.


Die Patenterteilung wurde am 6. Mai 2004 im Patentblatt veröffentlicht.


Der angegriffene Patentgegenstand betrifft ein Verfahren zum Decodieren von Zusatz-Daten, welche in einem Datenstrom aus Bild- und/oder Toninformationen zusätzlich enthalten sind und welche beispielsweise neben Steuerinformationen
auch ladbare, ablauffähige Rechenprogramme, Textinformationen und/oder Grafikinformationen umfassen. Das Verfahren beruht darauf, dass die Zusatzdaten,
umfassend Steuerinformationen, Rechenprogramme für die Ablaufsteuerung,
Dienstprogramme sowie Text- und Grafikinformationen von der vorhandenen Softund Hardware der Set-Top-Box entkoppelt und attributbezogen in einem Sammelspeicher abgelegt werden. Für die Verwaltung und den Zugriff auf diese Daten ist

                                         -3-



in der Verarbeitungseinheit der jeweiligen Set-Top-Box eine Software in Form einer logischen Schicht eingefügt, die vom Betriebssystem der Set-Top-Box unabhängig ist.


Der erteilte Patentanspruch 1 hat folgenden Wortlaut (mit eingefügten Aufzählungszeichen):


        1. Verfahren zum Decodieren von Zusatz-Daten, welche in einem Datenstrom aus Bild- und/oder Toninformationen, insbesondere MPEG 2-Datenstrom, zusätzlich enthalten sind und
              welche beispielsweise neben Steuerinformationen auch ladbare,   ablauffähige   Rechenprogramme,         Textinformationen
              und/oder Grafikinformationen umfassen, bei dem
        1a) die Zusatzdaten von dem Datenstrom abgetrennt werden (Stufe 20);
        1b) die abgetrennten Zusatz-Daten in dem Sammelspeicher (110)
              einer Verarbeitungseinheit (100) abgelegt werden;
        1c) die abgelegten Zusatz-Daten nach Maßgabe von Dienstprogrammen von der Verarbeitungseinheit (100) verwaltet und
              verarbeitet werden, wobei Dienstprogramme als residente Rechenprogramme und/oder als ladbare, ablauffähige Rechenprogramme vorliegen, und
        1d) verarbeitete Zusatz-Daten zu ihrer Wiedergabe und/oder zur
              Steuerung der aus dem Datenstrom abgetrennten Bildund/oder Toninformationen bereitgestellt werden (Stufe 40),
        dadurch gekennzeichnet, dass
        1e) die als Tuples vorliegenden Zusatz-Daten unabhängig von ihrem jeweiligen Inhalt abgelegt werden, dass
        1f) das Dienstprogramm für die Verwaltung des Sammelspeichers (100) eine logische Schicht (121) darstellt, welche von
              einer, aus einer begrenzten Anzahl von logischen Befehlen

                                        -4-



            ("FROM", "TO", "COPY") bestehenden ersten Sprache angesprochen wird, die von der Maschinensprache der Verarbeitungseinheit (100) unabhängig ist und welche die alleinige
            Schnittstelle darstellt für den Zugriff (1214) der übrigen Dienstprogramme auf die abgelegten Zusatz-Daten, dass
        1g) die logische Schicht (121) einen Initialisierer (1211) aufweist,
            welcher den Sammelspeicher (110) nach abgelegten Zusatzdaten durchsucht und vorhandene abgelegte Zusatz-Daten
            zur Verwendung in der Verarbeitungseinheit (100) freigibt sowie die freigegebenen Zusatzdaten nach ablauffähigen Rechenprogrammen durchsucht und gegebenenfalls startet, und
            dass
        1h) die logische Schicht (121) einen selbstverwaltenden Suchalgorithmus (Sammelspeicher-Zugriff 1214) enthält, welcher
            adressfrei nach Maßgabe der Struktur der abgelegten Zusatzdaten auf deren Inhalt zugreift.


Bezüglich des Wortlauts der erteilten Unteransprüche 2 bis 7 wird auf die Patentschrift verwiesen.


Gegen das Patent hat die Interessengemeinschaft für Rundfunkschutzrechte am
4. August 2004 Einspruch erhoben, den sie auf die im § 21 (1) Nr. 1 PatG angegebenen Gründe stützt. Sie vertritt insbesondere die Auffassung, dass der angegriffene Patentgegenstand gegenüber dem Stand der Technik auf keiner erfinderischen Tätigkeit nach § 4 PatG beruhe und begründet dies mit folgendem Stand
der Technik:


        D1 WO 96/28904 A1
        D2 Fachzeitschrift FKT Heft 3/1996, Seiten 92 - 102
        D3 Fachzeitschrift FKT Heft 3/1996, Seiten 84 – 89

                                      -5-



        D4 Fachzeitschrift FKT Heft 3/1996, Seiten 115 – 118
        D5 Fachzeitschrift mc Heft 3/1987, Seiten 72 -78.


Im Prüfungsverfahren wurden für die Beurteilung der Patentfähigkeit neben der
Druckschrift D1 noch die Druckschriften


        D6 US 55 59 549
        D7 EP 07 05 036 A2 und
        D8 WO 96 19 779 A1


berücksichtigt.


Mit Schriftsatz vom 26. September 2008 hat die Einsprechende den Einspruch zurückgenommen.


Die Patentinhaberin verteidigt das Patent mit in der mündlichen Verhandlung überreichten neuen Patentansprüchen 1 - 3.


Der verteidigte Patentanspruch 1 umfasst die Merkmale des erteilten Patentanspruchs 1, an die sich die nachfolgenden Merkmale anschließen (mit eingefügten,
fortlaufenden Aufzählungszeichen):


        1i) dass als weiteres Dienstprogramm ein Umformer (124) vorgesehen ist, welcher mit der logischen Schicht (121) kommuniziert und Steuerinformationen, welche in abgelegten Zusatz-Daten enthalten sind, aus dem Sammelspeicher (110) liest
            und zu Befehlen für Dienstprogramme der Verarbeitungseinheit (100) umformt, wobei diese Befehle in dem Sammelspeicher (110) abgelegt werden,
        1j) dass die Befehle Bestandteil einer zweiten, aus einem begrenzten Befehlssatz bestehenden Sprache (HTML) sind,

                                        -6-



          1k) dass als weiteres Dienstprogramm eine Grafikoberfläche (123)
             vorgesehen ist, welche mit der logischen Schicht (121) kommuniziert und nach Maßgabe der für die Grafikoberfläche (123) bestimmten, im Sammelspeicher (110) abgelegten
             Befehle des Umformers (124) Text- und/oder Grafikinformationen zur Wiedergabe aufbereitet, und
          1l) dass die logische Schicht (121) eine Freispeicherverwaltung (1213) aufweist, welche abgelegte Daten nach bestimmten Kriterien löscht, beispielsweise wenn ein Verfallsdatum erreicht ist oder nach Maßgabe einer Lösch-Strategie, und den
             Speichenraum des Sammelspeichers (110) für die abgelegten
             Daten derart reorganisiert, dass der zusammenhängende
             Speicherbereich eine maximale Größe aufweist.


Bezüglich des Wortlauts der Unteransprüche 2 und 3 wird auf den Akteninhalt verwiesen.


Die Patentinhaberin sieht die Patentfähigkeit des Verfahrens nach dem Patentanspruch 1 nunmehr als gegeben und beantragt wie entschieden.


                                         II.


Der Einspruch ist zulässig und führt zur beschränkten Aufrechterhaltung des Patents. Den geltenden Patentansprüchen kann Bestandsfähigkeit zuerkannt werden.


Der streitpatentliche Gegenstand richtet sich bezüglich der anstehenden Fragen
nach der Neuheit und dem Zugrundeliegen einer erfinderischen Tätigkeit seinem
sachlichen Inhalt nach an einen Diplomingenieur der elektrischen Nachrichtentechnik, der mit der Entwicklung von Empfangsgeräten der digitalen Fernsehübertragungstechnik befasst ist.

                                        -7-



1. Zulässigkeit der Patentansprüche 1 – 3


Die im Patentanspruch 1 gegenüber der ursprünglichen Fassung des Patentanspruchs 1 vorgenommenen Änderungen sind zulässig.


Der geltende Patentanspruch 1 umfasst die Merkmale der erteilten Patentansprüche 1 bis 4 und 6 und geht damit zurück auf die Merkmale der ursprünglichen Patentansprüche 1 bis 4 ( → Merkmale 1a) bis 1f) und 1h) bis 1k)), 6 und 7 ( →
Merkmale 1g) und 1l)), wobei im Merkmal 1e) ursprünglich die Zusatzdaten als "in
einer einheitlichen Datenstruktur" vorliegend nunmehr "als Tuples" vorliegend charakterisiert werden. Diese Konkretisierung der Datenstrukturen als Tuples findet
ihre Stütze in der Offenlegungsschrift Sp. 2, Z. 62 – 63 oder Sp. 8, Z. 31 - 35 und
ist damit für den fachkundigen Leser an entsprechender Stelle in den ursprünglichen Unterlagen als zu der beanspruchten Erfindung gehörend zu erkennen (vgl.
BGH GRUR 1991, 307 - Bodenwalze).


Die Unteransprüche 2 und 3 entsprechen den ursprünglich eingereichten Unteransprüchen 5 und 8.


2. Der - zweifelsfrei gewerblich anwendbare - Gegenstand des Patentanspruchs 1
ist neu und beruht auf einer erfinderischen Tätigkeit.


2.1. Neuheit


Der in der mündlichen Verhandlung diskutierte Fachartikel D2 beschreibt die Softwarearchitektur für den Betrieb eines interaktiven digitalen Decoders (Set-Top-Box) der Unterhaltungselektronik, der MPEG II codierte Signale empfängt und verarbeitet (vgl. S. 93, Bild 2 i. V. m. linke Sp., die letzten beiden Zeilen bis mittlere Sp., 1. Absatz). Mit dem MPEG II Datenstrom werden neben den Bild- und Audiosignalen auch Zusatzdaten, enthaltend programmspezifische Informationen (PSI) und Service Informationen (SI), übertragen (vgl. S. 94, linke Sp., letz-

                                        -8-



ter Absatz sowie Bild 5, i. V. m. S. 100, linke Sp. Kap. 4.2 "…Dabei gibt es zwei
Arten…") – Merkmal 1.


Diese Zusatzdaten werden im Empfänger vom Datenstrom abgetrennt, im Sammelspeicher einer Verarbeitungseinheit abgelegt und nach Maßgabe von Dienstprogrammen von dem zur Verarbeitungseinheit gehörenden Microcontroller verwaltet und verarbeitet (vgl. Bild 2, Signalpfad von DEMUX zu FLASH und DRAM
i. V. m. S. 93, mittlerer Sp. und S. 94, linke Sp., letzter Absatz Mitte "Darüber hinaus muss es möglich sein…" und Bild 5 i. V. m. S. 100, 4.2. DSMCC – Protokoll
für Zugriff und Kontrolle externer Speicher) – Merkmale 1a), 1b) und 1c).


Die abgespeicherten Zusatz-Daten werden nach ihrer Verarbeitung abhängig vom
jeweiligen Dateninhalt, bspw. als EPG, wiedergegeben (vgl. S. 94 linke Spalte unten) oder als heruntergeladene Anwendung zur Steuerung der aus dem Datenstrom abgetrennten Bild- und/oder Toninformationen verwendet (vgl. Bild 5
"Steuerung") – Merkmal 1d).


Wie im Kapitel 4.1 auf S. 98 dargelegt, wird, um eine betriebssystemunabhängige
Darstellung für interaktive Anwendungen zu ermöglichen, auf den MHEG-Standard zurückgegriffen. Dieser, von der ISO entwickelte Standard zum Austausch
multimedialer Informationen ermöglicht, dass Anwendungen, die sich vor ihrer
Ausführung nicht komplett im Speicher der Set-Top-Box befinden, bedarfsgemäß
von einem Server geholt werden und mit dem dazugehörigen Interpreterprogramm
auf die Set-Top-Box portiert werden können (vgl. Kap. 4.1 insb. S. 100, linke Sp.,
1. Absatz). Die Übertragung der Bild-, Ton- und Anwendungsdaten wird dabei in
Form von MHEG-Objekten vorgenommen die, wie in Bild 5 dargestellt, in den
MPEG II Transportstrom mit eingebettet werden.


Gemäß dem Merkmal 1e) des geltenden Patentanspruchs 1 liegen die Zusatzdaten als Tupels vor. Für die Auslegung des Begriffs "Tupel" wird der Fachmann die
Beschreibung heranziehen (BGH, GRUR 2007, 859 – 862 - Informationsübermitt-

                                         -9-



lungsverfahren I), in der die zugrundezulegende Datenstruktur, bestehend aus einem Kopf und n Elementen unterschiedlichen Typs (vgl.               Patentschrift,
Kap. [0015]) angegeben ist. Der Fachmann schließt aus dieser Angabe, dass dem
Begriff "Tupel" die damit verbundene fachübliche attributbezogenen Datenstruktur
zu unterlegen ist.


Die Datenstruktur der übertragenen Datenelemente ist in der D2 zwar explizit nicht
angegeben, sie ist aber dem zuständigen Fachmann in Kenntnis der auf seinem
Arbeitsgebiet aktuellen Normung jederzeit als bekannt zu unterstellen (BGH,
GRUR 1995, 330 - 333 - Elektrische Steckverbindung), sodass der Fachmann
beim Studium der D2 die im MHEG-Standard gebräuchlichen Datenelemente subsumieren wird. In diesem Zusammenhang ist dem Fachmann bekannt, dass die
Datenelemente ebenfalls attributbezogen strukturiert sind und in ihrer einfachsten
Form aus einem header ( → Kopf) und n Elementen zusammengesetzt sind, die
entsprechend ihren Attributen in einer einheitlichen Struktur und damit unabhängig
von ihrem Inhalt abgespeichert werden - Merkmal 1e).


Der MHEG-Standard sieht auch vor, dass die Verarbeitung und Verwaltung von
MHEG-Objekten mittels eines Interpreter-Programms, der sog. MHEG-Engine vorgenommen wird (vgl. Kap. 4.1), das in der für einen Interpreter charakteristischen
Weise auf einen begrenzten, von der Maschinensprache der Verarbeitungseinheit
der Set-Top-Box unabhängigen Befehlssatz zugreift und eine logische Schicht
darstellt (vgl. Bild 5) – Merkmal 1f).


Zu den weiteren Merkmale 1g) bis 1l) sind dem Fachartikel keine weiteren dezidierten Angaben entnehmbar.


Die ebenfalls in der mündlichen Verhandlung behandelte Druckschrift D4 gibt einen Überblick über den MHEG-Standard als Codierverfahren für Multimedia- und
Hypermedia-Anwendungen. In dem Fachartikel stehen dabei weniger die hardwaremäßige Implementierung in einem Empfänger und die dortige Signalführung,

                                       - 10 -



sondern vielmehr die funktionelle Bestimmung aus übertragenen Zusatzdaten
( → MHEG-Objekte) eine strukturierte Darstellung dieser Daten in einem Bild oder
einer ablaufende Präsentation am Bildschirm zusammenzustellen (vgl. Zusammenfassung und Kap. 3) im Mittelpunkt. In diesem Zusammenhang ist dem Fachmann selbstverständlich bewusst, dass das ausführende, als MHEG-Engine bezeichnete Interpreterprogramm als weitere logische Schicht im Empfänger zu implementieren ist – Merkmal 1f).


Die fachgerechte Umsetzung der vorstehenden Abläufe für die Darstellung von
MHEG-Objekten in einer Präsentation erfordert zwangsläufig auch einen - wie
auch immer gearteten - Initialisierer, der zumindest die dafür erforderlichen Grundfunktionalitäten bereitstellen muss, die sich aus der Suche nach abgelegten Objekten ( → Zusatzdaten) in einem Sammelspeicher, deren Freigabe zur Verwendung und dem Start für eine Präsentation zusammensetzen (vgl. Kap. 6 Woraus
besteht MHEG?) – Merkmal 1g).


Zur Datenstruktur der MHEG-Objekten werden in der D4 zwar ebenfalls keine expliziten Aussagen gemacht, allein aber die dem Fachmann gegenwärtige Vorgabe
durch die Normung (vgl. diesbezüglich auch Ausführungen zur D2), dass die Datenstruktur der Datenelemente im MHEG-Standard attributbezogen konzipiert ist,
zieht nach sich, dass sowohl die Abspeicherung (vgl. auch vorstehende Ausführungen zur D2) – Merkmal 1e) – als auch die Suche nach den Datenelementen attributbezogen realisiert ist, so dass der Zugriff auf die Daten attributbezogen und
folglich adressfrei nach Maßgabe der Struktur der abgelegten Zusatzdaten mittels
eines dafür geeigneten Suchalgorythmus umgesetzt ist (vgl. Kap. 6 Woraus besteht MHEG?) – Merkmal 1h).


Die in den Bildern 1 und 2 gezeigte Wiedergabe von MHEG-Objekten als Grafikobjekte bestärkt den Fachmann zudem in der Annahme, dass auch dafür ein
Dienstprogramm in Form einer Grafikoberfläche in funktioneller Form des Merkmals 1k) als hinterlegt vorauszusetzen ist.

                                       - 11 -



In der D4 wird in Kap. 4 (vgl. insb. rechte Spalte) des Weiteren HTML und damit
eine zweite, aus einem beschränkten Befehlssatz bestehenden Sprache erwähnt.
Aus dem Kontext entnimmt der Fachmann aber nur in Form eines Vergleichs der
beiden Programmiersprachen, dass HTML speziell auf Internetanwendungen und
der Standard MHEG auf die Bedürfnisse von Inhaltsanbietern aus dem Interactive-TV- oder Video-on-Demand-Bereich angepasst ist. Ein Hinweis auf die Implementierung eines weiteren Dienstprogramms in einer weiteren Sprache ist in der D4
aber nicht enthalten – Merkmale 1i) und 1j).


Auch die Realisierung einer Freispeicherverwaltung ist aus der D4 nicht herleitbar
– Merkmal 1l).


Die weiteren im Verfahren befindlichen Druckschriften haben in der mündlichen
Verhandlung keine Rolle gespielt und reichen im Hinblick auf den Patentgegenstand inhaltlich nicht näher an die vorstehend abgehandelten heran. Sie bringen
auch hinsichtlich der Beurteilung der erfinderischen Tätigkeit keine neuen Gesichtspunkte.


2.2. Erfinderische Tätigkeit


Aus der D2 erhält der Fachmann zwar nur die Lehre, welche funktionalen Komponenten er für die Separierung und Ablage der attributbezogen strukturierten
MHEG-Objekte ( → Zusatzdaten) zu ergreifen hat (Merkmale 1 bis 1f)), er wird
dabei aber nicht deren bestimmungsgemäße Verwendung für die Wiedergabe als
Bild- und/oder Textinformationen bzw. lauffähige Anwendungen aus den Augen
verlieren und sich selbstverständlich Gedanken über den Zugriff und die Darstellung der abgelegten Zusatzdaten machen. Er wird sich daher dem in der gleichen
Fachzeitschrift abgedruckten Fachartikel D4 zuwenden, der sich gleichfalls mit
dem von der ISO entwickelten Standard MHEG zur Normung von Austauschformaten und Codierungsverfahren für Multimediasysteme auseinandersetzt und der
ihm Möglichkeiten für die Darstellung der Zusatzdaten aufzeigt. Zusammen mit

                                     - 12 -



diesem als bekannt vorauszusetzenden Standard MHEG erschließen sich daraus
die Merkmale 1g), 1h) und 1k).


Ausgehend von der gleichen Thematik und der gemeinsamen Positionierung in
der identischen Ausgabe einer Fachzeitschrift wird der Fachmann die in den Fachartikeln D2 und D4 enthaltenen Teilaspekte unter Anwendung seines fachlichen
Könnens zu dem Decodierverfahren nach dem Patentanspruch 1, umfassend die
Merkmale 1 bis 1h) und 1k) zusammenfassen.


Es mag auch, angeregt durch den Vergleich von MHEG mit HTML in der D4, im
Bereich seiner fachmännischen Überlegungen liegen, weitere Dienstprogramme
bei Bedarf in einer zweiten, vom Betriebssystem der Verarbeitungseinheit unabhängigen Sprache abzufassen – Merkmale 1i) und 1j), die Implementierung einer
Freispeicherverwaltung mit einer nach bestimmten Kriterien ausgerichteten Löschfunktion oder Löschstrategie – Merkmal 1l), zu der im Stand der Technik keinerlei
Hinweise aufzufinden sind, übersteigt nach Überzeugung des Senats jedoch das
Durchschnittskönnen und –wissen des zuständigen Fachmanns.


3. Die auf den Patentanspruch 1 direkt oder indirekt rückbezogenen Patentansprüchen 2 und 3 betreffen über das Selbstverständliche hinausgehende Ausgestaltungen und Weiterbildungen des Verfahrens nach dem Patentanspruch 1 und werden von diesem mitgetragen.


4. Die Beschreibung genügt den an sie nach § 34 PatG zu stellenden Anforderungen.




Dr. Hartung             Martens               Gottstein            Kleinschmidt




                                                                              Pü
